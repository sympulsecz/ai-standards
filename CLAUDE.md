# AI Standards Project - AI Assistant Instructions

This file provides context and guidelines for AI assistants working on this documentation project.

## Project Purpose

This is an internal documentation site teaching developers best practices for working with AI. The goal is to help teams understand AI-assisted development, agents, automation, and related concepts.

## Guiding Philosophy: Concepts Over Products

**This is the most important principle.** All content should focus on transferable concepts and patterns, not specific products or tools.

- Teach "how to think about X" rather than "how to use Tool Y"
- Products are mentioned only as examples to illustrate concepts
- Patterns and mental models should work across different tools
- Content should remain valuable even as specific tools change

### What to Avoid

- Version numbers (e.g., "GPT-4 has 128k context")
- Pricing information
- Feature comparisons between products
- Step-by-step tutorials for specific tools
- Product evangelism or recommendations

### What to Include

- Underlying mechanisms and how they work
- Design patterns that apply across implementations
- Decision frameworks for choosing approaches
- Trade-offs and considerations
- Concrete examples that illustrate concepts (tools mentioned as "one example of this pattern")

## Writing Style

### Tone

- Technical but accessible
- Direct and practical
- Pattern-focused
- Neutral on specific products

### Structure

- Start with the "why" before the "how"
- Use clear headings and scannable sections
- Include practical examples
- End sections with key takeaways when appropriate

### Formatting

- Use MkDocs admonitions for tips, warnings, notes
- Use code blocks with language hints
- Keep paragraphs focused and concise
- Use lists for scannable information
- Always add a blank line before and after lists

## File Structure Conventions

```
docs/
├── index.md                    # Homepage
├── {section}/
│   ├── index.md               # Section overview
│   └── {topic}.md             # Individual topics
└── reference/
    └── glossary.md            # Terminology reference
```

- Section folders use kebab-case: `ai-assisted-development/`
- Topic files use kebab-case: `effective-prompting.md`
- Each section has an `index.md` as the entry point
- All new pages must be added to `nav` in `mkdocs.yml`

## MkDocs Specifics

### Adding a New Page

1. Create the markdown file in the appropriate directory
2. Add the page to the `nav` section in `mkdocs.yml`
3. Link to related pages where appropriate

### Useful Admonitions

```markdown
!!! tip "Title"
    Tip content here.

!!! warning "Title"
    Warning content here.

!!! note "Title"
    Note content here.

!!! example "Title"
    Example content here.
```

### Code Blocks

Always specify the language:

```markdown
```python
def example():
    pass
```

```

### Local Preview

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open <http://localhost:8000>

## Quality Checklist

Before considering content complete, verify:

- [ ] Focuses on concepts, not products
- [ ] No version numbers or pricing
- [ ] Practical examples included
- [ ] Clear structure with headings
- [ ] Added to navigation in mkdocs.yml
- [ ] Cross-links to related topics where relevant
- [ ] Code examples have language hints
- [ ] Renders correctly in local preview

## Common Tasks

### Adding a New Section

1. Create directory under `docs/`
2. Create `index.md` with section overview
3. Create topic files
4. Add all pages to `nav` in `mkdocs.yml`

### Updating Existing Content

1. Make changes to the markdown file
2. Preview locally with `mkdocs serve`
3. Ensure links still work
4. Verify navigation is correct

### Building for Production

```bash
mkdocs build
```

Output goes to `site/` directory.
