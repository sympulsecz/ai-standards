# AI-Assisted Development

This section covers practical patterns for integrating AI into your daily coding workflow.

!!! info "Who This Is For"
    This section is for developers using AI coding tools like Cursor, Claude Code, GitHub Copilot, or similar assistants in their daily work. If you're building AI features into applications, check [Agents](../agents/index.md) and [Security](../security/index.md) instead.

## What You'll Learn

- **Evaluating Tools**: How to choose AI coding tools based on context capability, data handling, and workflow fit
- **Tool Use: Guidelines**: What AI does well vs poorly, safety principles, limitations, and team practices
- **Tool Use: Fundamentals**: Prompting techniques to communicate effectively with AI
- **Tool Use: Workflows**: Practical workflows for code review, debugging, refactoring, and understanding code
- **Instruction Files**: Configuring AI tools to match your project conventions and encode your workflows

## The Core Skill

The fundamental skill in AI-assisted development is **effective communication**. Unlike traditional tools that do exactly what you instruct, AI tools interpret your intent and generate responses. The quality of your input directly affects the quality of output.

## When AI Assistance Helps Most

AI assistance tends to be most valuable when:

- **Boilerplate generation**: Repetitive code that follows clear patterns
- **Translation tasks**: Converting between formats, languages, or styles
- **Exploration**: Understanding unfamiliar code or concepts
- **First drafts**: Getting a starting point to refine
- **Documentation**: Explaining code or generating comments
- **Test generation**: Creating test cases from specifications

## When to Be Cautious

Exercise extra care when:

- **Security-sensitive code**: Authentication, encryption, authorization
- **Complex business logic**: Rules that require deep domain knowledge
- **Performance-critical code**: Where subtle inefficiencies matter
- **Novel problems**: Situations unlike common patterns in training data

!!! warning "Always Verify"
    AI-generated code can contain subtle bugs, security vulnerabilities, or logic errors. Review all generated code as carefully as you would review a colleague's work.

## The Collaboration Mindset

Think of AI as a capable but imperfect collaborator:

| AI Does Well | AI Needs Help |
|--------------|---------------|
| Generating code that follows patterns | Understanding your specific requirements |
| Explaining concepts | Knowing your project's conventions |
| Suggesting approaches | Making final decisions |
| Catching certain errors | Guaranteeing correctness |

The most effective approach is collaborative: use AI to accelerate your work while maintaining your judgment and oversight.

## Sections

- [Evaluating Tools](evaluating-tools.md) - Choosing AI coding tools based on context, data handling, and workflow
- [Tool Use: Guidelines](tool-use-guidelines.md) - What AI does well, safety principles, and team practices
- [Tool Use: Fundamentals](tool-use-fundamentals.md) - Prompting techniques for effective AI communication
- [Tool Use: Workflows](tool-use-workflows.md) - Practical workflows for review, debugging, and refactoring
- [Instruction Files](instruction-files.md) - Configuring AI tools to match your project conventions
