# Tool Use: Guidelines

Before diving into specific workflows, understand what AI can and cannot do, how to work safely with AI-generated code, and how to establish effective team practices.

!!! info "Related Pages"
    - [Tool Use: Fundamentals](tool-use-fundamentals.md) - Prompting techniques
    - [Tool Use: Workflows](tool-use-workflows.md) - Practical workflows for review, debugging, refactoring

## What AI Does Well vs. Poorly

Understanding AI's strengths and limitations helps set appropriate expectations and choose when to rely on AI versus human expertise.

| AI Strengths | AI Limitations |
|--------------|----------------|
| Pattern recognition (anti-patterns, style issues, common errors) | Business logic correctness |
| Error message interpretation and common causes | Architecture decisions and system design |
| Generating diagnostic hypotheses | Understanding your specific domain/context |
| Applying language/framework best practices | Stateful system behavior (database state, cache contents) |
| Security vulnerability patterns | Historical context and past decisions |
| Code behavior explanations | Timing-dependent issues (race conditions, deadlocks) |
| Test case generation | Environment-specific configurations |

AI excels at recognizing patterns it has seen before but struggles with context it doesn't have. It can suggest likely causes for an error message but cannot know your system's actual state, deployment history, or business constraints.

## Safety Principles

When using AI for code changes, follow safety practices to prevent introducing new issues.

**Make small, focused changes.** Apply one type of change at a time. Don't extract methods, rename variables, and simplify conditionals simultaneously.

**Test before and after.** Run existing tests before changes to establish baseline, apply changes, run tests again to verify behavior unchanged.

**Review like any code change.** Check logic preservation, edge cases, performance, side effects, and readability. Don't lower review standards because AI generated the code.

**Use version control.** Commit clean state before making AI-assisted changes. Review diffs carefully—unexpected changes often signal AI misunderstood requirements.

**Verify behavior, not just syntax.** Code that compiles can still have subtle logic errors. Verify calculations, error handling, edge cases, and security properties are preserved.

## Key Limitations

**AI cannot access running state.** AI sees code, not runtime values, variable contents, or memory state. Provide runtime information explicitly: "The database query returns empty results but there are 1000 rows that match."

**AI guesses without execution.** AI predicts likely issues based on patterns but doesn't actually run code. Verify AI predictions by running code.

**AI may miss environment issues.** Configuration problems, environment variables, network issues, and deployment-specific bugs require explicit context.

**AI focuses on code shown.** Bugs in other files, database schema issues, and infrastructure problems won't be detected if not included in context.

**AI may introduce subtle changes.** When refactoring or fixing code, AI sometimes adds error handling that didn't exist before, changes validation logic, or alters edge case behavior. Always compare before and after behavior.

## Team Practices

**Establish norms.** Agree on which activities benefit from AI assistance, what level of review is required for AI-generated code, and how to handle disagreements with AI suggestions.

**Share effective prompts.** Build a team collection of prompts that work well for your codebase: security review templates, performance review patterns, common debugging scenarios, refactoring request formats.

**Review the reviewer.** Periodically evaluate AI effectiveness: What does it catch that humans miss? What does it miss that humans catch? Where does it generate noise? Adjust usage patterns based on findings.

**Maintain review standards.** AI-generated code must meet the same standards as human-written code. Developers remain responsible for understanding and validating AI output.

## Key Takeaways

- AI excels at pattern recognition but requires human judgment for context-dependent decisions
- Make small, testable changes and verify behavior is preserved
- AI sees code, not runtime state—provide runtime information explicitly
- Use version control and review diffs carefully
- Establish team norms for AI usage and share effective practices
- Maintain the same review standards for AI-generated code as human-written code

Next: Learn [prompting techniques](tool-use-fundamentals.md) to communicate effectively with AI, then explore [practical workflows](tool-use-workflows.md) for specific activities.
