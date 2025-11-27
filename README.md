# AI Standards

Internal documentation for best practices when working with AI in software development.

**📖 [View the documentation](https://sympulsecz.github.io/ai-standards/)**

---

## What's Inside

- **AI-Assisted Development** — Effective prompting, code review, debugging with AI
- **Agents** — Architectures, building reliable agents, safety guardrails
- **Model Context Protocol (MCP)** — Understanding and building MCP tools
- **Automation** — CI/CD integration, AI-powered testing
- **LLM Development** — API patterns, RAG, evaluation strategies
- **Security** — Data handling, prompt injection prevention

## Philosophy

This documentation focuses on **concepts over products**. Tools and models change rapidly; the underlying patterns and mental models remain valuable. Products are mentioned only as examples to illustrate concepts.

## Local Development

### Prerequisites

- Python 3.10+

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Start local server
mkdocs serve
```

Open <http://localhost:8000> to view the documentation.

### Building

```bash
mkdocs build
```

Output goes to the `site/` directory.

## Deployment

The documentation automatically deploys to GitHub Pages when changes are pushed to `main` or `master`.

To enable deployment:

1. Go to repository Settings → Pages
2. Set Source to "GitHub Actions"

## Contributing

1. Create or edit markdown files in `docs/`
2. Add new pages to `nav` in `mkdocs.yml`
3. Preview locally with `mkdocs serve`
4. Submit a pull request

See `CLAUDE.md` for detailed content guidelines.
