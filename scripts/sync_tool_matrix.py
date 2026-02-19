#!/usr/bin/env python3
"""Sync tool-matrix artifact markdown into a compact AI Standards docs page."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


class ParseError(RuntimeError):
    """Raised when the source matrix artifact does not match expected structure."""


def _extract_section(markdown: str, title: str) -> str:
    pattern = rf"^## {re.escape(title)}\n(?P<body>.*?)(?=^## |\Z)"
    match = re.search(pattern, markdown, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise ParseError(f"Missing section: '## {title}'")
    return match.group("body").strip("\n")


def _extract_generated(markdown: str) -> str:
    match = re.search(r"^> Generated:\s*(.+)$", markdown, flags=re.MULTILINE)
    if not match:
        raise ParseError("Missing generated timestamp line: '> Generated: ...'")
    return match.group(1).strip()


def _extract_table(section_body: str, header_prefix: str) -> list[str]:
    lines = section_body.splitlines()
    for idx, line in enumerate(lines):
        if line.strip().startswith(header_prefix):
            table = [line.rstrip()]
            j = idx + 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                table.append(lines[j].rstrip())
                j += 1
            if len(table) < 2:
                raise ParseError(f"Malformed table after header: {header_prefix}")
            return table
    raise ParseError(f"Missing table with header prefix: {header_prefix}")


def _score_intro(score_section: str) -> str:
    lines = score_section.splitlines()
    heading_idx = None
    for idx, line in enumerate(lines):
        if line.strip() == "### Category Legend":
            heading_idx = idx
            break
    if heading_idx is None:
        raise ParseError("Missing '### Category Legend' in score matrix section")

    intro_lines = [ln.strip() for ln in lines[:heading_idx] if ln.strip()]
    if not intro_lines:
        raise ParseError("Missing score matrix introduction text")
    return " ".join(intro_lines)


def _matrix_stats(matrix_table: list[str]) -> tuple[int, int]:
    if len(matrix_table) < 3:
        raise ParseError(
            "Score matrix table must include header, separator, and data rows"
        )

    header_cells = [c.strip() for c in matrix_table[0].strip().strip("|").split("|")]
    if len(header_cells) < 3 or header_cells[0] != "Tool" or header_cells[-1] != "Avg":
        raise ParseError("Unexpected score matrix header format")

    category_count = len(header_cells) - 2

    tool_count = 0
    for line in matrix_table[2:]:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or len(cells) < 3:
            continue
        first = cells[0]
        if first.lower() in {"", "tool", "category meaning"}:
            continue
        tool_count += 1

    if tool_count == 0:
        raise ParseError("No tool rows found in score matrix table")

    return tool_count, category_count


def _indent_block(lines: list[str]) -> list[str]:
    return [f"    {line}" if line else "" for line in lines]


def _clean_sentence(text: str) -> str:
    cleaned = " ".join(text.split()).strip()
    cleaned = cleaned.rstrip(" ;")
    if not cleaned:
        return ""
    if cleaned[-1] not in ".!?":
        cleaned = f"{cleaned}."
    return cleaned


def _format_methodology_list(methodology_text: str) -> list[str]:
    flat = " ".join(methodology_text.split())
    if not flat:
        raise ParseError("Methodology section is empty")

    lines: list[str] = []

    # Split out trailing calibration/context sentences so they become separate bullets.
    tail_match = re.search(r"\bTools were scored relative\b.*$", flat)
    if tail_match:
        tail_text = tail_match.group(0).strip()
        main_text = flat[: tail_match.start()].strip()
    else:
        tail_text = ""
        main_text = flat

    # Parse the numbered evidence-source groups if present.
    if ":" in main_text and "(1)" in main_text:
        prefix, enumerated = main_text.split(":", 1)
        prefix_clean = _clean_sentence(prefix)
        if prefix_clean:
            lines.append(f"- {prefix_clean}")

        matches = list(re.finditer(r"\((\d+)\)\s*(.*?)(?=\s*\(\d+\)\s*|$)", enumerated))
        if not matches:
            raise ParseError("Could not parse numbered methodology evidence groups")

        for idx, match in enumerate(matches, start=1):
            text = _clean_sentence(match.group(2))
            if text:
                lines.append(f"- Source group {idx}: {text}")
    else:
        lines.append(f"- {_clean_sentence(main_text)}")

    if tail_text:
        for sentence in re.split(r"(?<=[.!?])\s+", tail_text):
            sentence = _clean_sentence(sentence)
            if sentence:
                lines.append(f"- {sentence}")

    return lines


def _format_sources_list(sources_text: str) -> list[str]:
    raw_lines = [ln.strip() for ln in sources_text.splitlines() if ln.strip()]
    if not raw_lines:
        raise ParseError("Sources section is empty")

    lines: list[str] = []
    for line in raw_lines:
        url = line[2:].strip() if line.startswith("- ") else line
        if url.startswith("http://") or url.startswith("https://"):
            lines.append(f"- [{url}]({url})")
        else:
            lines.append(f"- {url}")

    return lines


def build_snapshot(markdown: str) -> str:
    generated = _extract_generated(markdown)

    score_section = _extract_section(markdown, "Score Matrix")
    score_intro = _score_intro(score_section)
    legend_table = _extract_table(score_section, "| Category | Meaning |")
    matrix_table = _extract_table(score_section, "| Tool |")

    rec_section = _extract_section(markdown, "Recommendations by Category")
    rec_table = _extract_table(
        rec_section, "| Category | Top Pick | Runner-up | Reasoning |"
    )

    methodology_text = _extract_section(markdown, "Methodology").strip()
    sources_text = _extract_section(markdown, "Sources").strip()

    methodology_lines = _format_methodology_list(methodology_text)
    source_lines = _format_sources_list(sources_text)

    tool_count, category_count = _matrix_stats(matrix_table)

    page_lines: list[str] = []
    page_lines.append("# Tool Matrix Snapshot")
    page_lines.append("")
    page_lines.append(
        "This page provides a concise snapshot of AI tool capabilities by category, "
        "so teams can quickly compare strengths, trade-offs, and recommended fits."
    )
    page_lines.append("")
    page_lines.append("## Overview")
    page_lines.append("")
    page_lines.append(
        f"- Snapshot covers **{tool_count} tools** across **{category_count} categories**."
    )
    page_lines.append(
        "- Scores range from **0 (minimal)** to **100 (best-in-class)**; **N/A** means the tool does not target that category."
    )
    page_lines.append(
        "- **Avg** is the average of numeric category scores, excluding N/A."
    )
    page_lines.append(f"- Generated: `{generated}`")
    page_lines.append("")
    page_lines.append("## Category Legend")
    page_lines.append("")
    page_lines.extend(legend_table)
    page_lines.append("")
    page_lines.append("## Score Matrix")
    page_lines.append("")
    page_lines.append('???+ note "Full score matrix"')
    page_lines.extend(_indent_block([score_intro, ""] + matrix_table))
    page_lines.append("")
    page_lines.append("## Recommendations by Category")
    page_lines.append("")
    page_lines.append('???+ note "Full recommendations"')
    page_lines.extend(_indent_block(rec_table))
    page_lines.append("")
    page_lines.append("## Methodology & Sources")
    page_lines.append("")
    page_lines.append('???+ note "Methodology and source links"')
    page_lines.extend(
        _indent_block(
            ["**Methodology**", ""]
            + methodology_lines
            + ["", "**Sources**", ""]
            + source_lines
        )
    )
    page_lines.append("")

    return "\n".join(page_lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate AI Standards Tool Matrix snapshot page from an artifact markdown file."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("../ai-tool-eval-matrix/artifacts/tool-matrix.md"),
        help="Path to tool-matrix markdown artifact",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/ai-assisted-development/ai-tool-eval-matrix.md"),
        help="Path to generated AI Standards markdown page",
    )
    parser.add_argument(
        "--mode",
        choices=["compact"],
        default="compact",
        help="Rendering mode (currently only 'compact' is supported)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.mode != "compact":
        raise ParseError(f"Unsupported mode: {args.mode}")

    source = args.source
    output = args.output

    if not source.exists():
        raise ParseError(f"Source artifact not found: {source}")

    markdown = source.read_text(encoding="utf-8")

    snapshot = build_snapshot(markdown)

    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".tmp")
    temp.write_text(snapshot, encoding="utf-8")
    temp.replace(output)

    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ParseError as exc:
        print(f"sync_tool_matrix: {exc}", file=sys.stderr)
        raise SystemExit(1)
