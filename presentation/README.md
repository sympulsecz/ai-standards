# AI Best Practices Presentation

A 40-minute LaTeX Beamer presentation covering best practices for working with AI in software development.

## Contents

- **Foundations** - How language models work, mental models, feedback loops
- **Effective Prompting** - 4 core principles, 3 essential patterns
- **Code Inspection** - Review and debugging workflows
- **Automation** - CI/CD integration patterns
- **Security** - Threats and mitigations
- **Demo Transition** - Bridge to live demonstration

## Requirements

- LaTeX distribution with Beamer (BasicTeX or MacTeX on macOS)
- Required packages: `beamer`, `pgf`, `booktabs`, `listings`, `tikz`

## Quick Start

### Compile the Presentation

```bash
make
```

This will run `pdflatex` twice to generate `presentation.pdf`.

### View the PDF

```bash
make view
```

### Clean Auxiliary Files

```bash
make clean
```

## Manual Compilation

If you prefer to compile manually:

```bash
pdflatex -interaction=nonstopmode presentation.tex
pdflatex -interaction=nonstopmode presentation.tex
```

## Installation (macOS)

If you don't have LaTeX installed:

```bash
# Install BasicTeX (lightweight, ~100MB)
brew install --cask basictex

# Add to PATH
export PATH="/Library/TeX/texbin:$PATH"
echo 'export PATH="/Library/TeX/texbin:$PATH"' >> ~/.zshrc

# Install required fonts
sudo tlmgr install cm-super

# Update font database
sudo tlmgr update --self
sudo mktexlsr
```

## Customization

Edit `presentation.tex` to customize:

- **Line 31-33:** Author name and organization
- **Line 5:** Theme (`Madrid`, `Berlin`, `Singapore`, etc.)
- **Line 6:** Color scheme (`beaver`, `whale`, `dolphin`, etc.)

## Presentation Structure

- **Duration:** ~40 minutes of presentation
- **Total Session:** 1.5 hours including demo and discussion
- **Slides:** 31 slides + 1 thank you slide
- **Format:** Guide-style with bullet points for speaker notes

## Demo Suggestions

After the presentation, consider demonstrating:

1. **Effective Prompting** (15 min) - Show iterative refinement in action
2. **Code Review/Debugging** (15 min) - Use AI to diagnose a bug
3. **Workflow Integration** (10 min) - Pre-commit, PR review, release notes
4. **Security** (5-10 min) - Spot security issues in AI-generated code

## License

Content based on the AI Standards documentation in this repository.
