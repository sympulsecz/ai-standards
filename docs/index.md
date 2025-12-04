# AI Standards

This documentation covers practical patterns for working with AI in software development. It focuses on concepts that remain useful regardless of which specific tools or models you're using. The content addresses three main areas: using AI coding assistants effectively, building AI-powered features into applications, and integrating AI into development workflows.

The sections explain how AI systems actually work, what makes them fail, and how to handle common concerns around security, testing, and reliability. Products are mentioned as examples to illustrate concepts, not as recommendations.

## Quick Navigation

<div class="grid cards" markdown>

- :material-rocket-launch:{ .lg .middle } **Getting Started**

    ---

    How AI actually works: prompts, context, embeddings, inference. Foundation for everything else.

    [:octicons-arrow-right-24: Key concepts](getting-started/key-concepts.md)

- :material-code-braces:{ .lg .middle } **AI-Assisted Development**

    ---

    Practical patterns for using AI coding tools: prompting, code review, debugging, refactoring.

    [:octicons-arrow-right-24: Daily workflows](ai-assisted-development/index.md)

- :material-robot:{ .lg .middle } **Agents**

    ---

    How autonomous AI systems work—from using agentic coding tools to building your own.

    [:octicons-arrow-right-24: Explore agents](agents/index.md)

- :material-cog-sync:{ .lg .middle } **Operations**

    ---

    Integrate AI into CI/CD pipelines, testing workflows, and code review.

    [:octicons-arrow-right-24: CI/CD & Testing](ci-cd.md)

- :material-shield-check:{ .lg .middle } **Security**

    ---

    Data classification, enterprise agreements, prompt injection, protecting applications.

    [:octicons-arrow-right-24: Security](security/index.md)

- :material-book-open-variant:{ .lg .middle } **Reference**

    ---

    Quick lookup for AI terminology.

    [:octicons-arrow-right-24: Glossary](glossary.md)

</div>

## Find Your Path

Different roles need different starting points.

### Using AI Coding Tools

**What you're doing:** Writing code with Cursor, Claude Code, GitHub Copilot, or similar assistants.

**Start here:**

1. [Key Concepts](getting-started/key-concepts.md) - How these tools actually work
2. [AI-Assisted Development](ai-assisted-development/index.md) - Effective prompting and workflows
3. [Working with Agents](agents/working-with-agents.md) - Understanding agentic coding tools

**What you'll learn:** How to write prompts that produce useful results, when AI suggestions are trustworthy, and how to debug issues when tools behave unexpectedly.

---

### Building AI Features

**What you're doing:** Adding AI capabilities to applications—chatbots, autonomous agents, AI-powered features.

**Start here:**

1. [Key Concepts](getting-started/key-concepts.md) - Foundation for building with AI
2. [Security](security/index.md) - Data handling and prompt injection before shipping
3. [Building Agents](agents/building-agents.md) - API integration, tool design, testing
4. [RAG Systems](agents/rag.md) - Ground AI responses in your data

**What you'll learn:** How to handle data classification with AI services, test non-deterministic systems, implement proper guardrails, and understand failure modes.

---

### Automating Development Workflows

**What you're doing:** Integrating AI into CI/CD pipelines, automated testing, or code review processes.

**Start here:**

1. [Key Concepts](getting-started/key-concepts.md) - Understand how AI behaves
2. [CI/CD](ci-cd.md) - Pipeline integration patterns
3. [Testing](testing.md) - Generate and verify tests with AI
4. [Security](security/index.md) - Data classification for AI services

**What you'll learn:** Integration patterns that don't break pipelines, when AI automation helps versus when it adds overhead, and how to maintain reliability.

---

**Not sure where to start?** Everyone benefits from [Key Concepts](getting-started/key-concepts.md). Begin there.

**Need a specific term?** Check the [Glossary](glossary.md).

## Contributing

This documentation is maintained collaboratively. See the repository for contribution guidelines.
