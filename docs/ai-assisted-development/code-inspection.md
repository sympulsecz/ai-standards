# Code Inspection

AI can assist with inspecting code for issues, understanding behavior, and finding bugs—freeing you to focus on higher-level concerns that require human judgment.

## What AI Does Well vs. Poorly

Understanding AI's strengths and limitations helps you use it effectively and know when to rely on human expertise.

| AI Strengths | AI Limitations |
|--------------|----------------|
| Pattern recognition (anti-patterns, style issues, common errors) | Business logic correctness |
| Error message interpretation and common causes | Architecture decisions and system design |
| Generating diagnostic hypotheses | Understanding your specific domain/context |
| Applying language/framework best practices | Stateful system behavior (database state, cache contents) |
| Security vulnerability patterns | Historical context and past decisions |
| Code behavior explanations | Timing-dependent issues (race conditions, deadlocks) |
| Test case generation | Environment-specific configurations |

!!! warning "AI as Supplement, Not Replacement"
    AI inspection should augment human judgment, not replace it. Use AI to catch what it excels at, freeing you to focus on what requires domain knowledge and strategic thinking.

## Code Review with AI

AI review works best as part of a two-stage process: use AI to catch pattern-based issues early, then have humans focus on business logic, architecture, and context-dependent decisions during formal review.

### Review Prompts

**General or focused review:**

```
Review this [authentication/API/etc.] code for:
- [Specific concerns: security, performance, bugs, etc.]
- [Language/framework] best practices

[paste code]
```

**Comparative review:**

```
Compare these implementations and identify functional differences
and potential issues:

Before: [old code]
After: [new code]
```

**Style review:**

```
Review against our conventions:
- [Convention 1]
- [Convention 2]

[paste code]
```

### Review Workflow

**Pre-commit:** Before submitting for human review, ask AI to review your changes and address obvious issues. This reduces back-and-forth on style and simple errors.

**During human review:** Use AI to verify complex logic, explain unfamiliar patterns, or generate test cases when reviewers encounter something unclear.

**Checklist generation:** Ask AI to generate comprehensive review checklists for specific change types (new endpoints, refactors, etc.).

### Interpreting Feedback

Not all AI suggestions are equally valid. Calibrate your confidence based on what's being flagged:

| Higher Confidence | Lower Confidence |
|-------------------|------------------|
| Syntax errors, resource leaks, missing error handling | Business logic correctness, performance in your context |
| Style violations, common security patterns | Whether this is the right architectural approach |

For each suggestion, evaluate critically before accepting.

## Debugging with AI

AI debugging is conversational—you share context, explore hypotheses together, and iterate toward the root cause. The key is providing enough information for AI to generate useful hypotheses while maintaining your own critical judgment.

### Debugging Prompts

**Error interpretation:**

```
I'm getting this error:
[error message and stack trace]

This happens when [trigger].

Relevant code:
[paste code]

What could cause this?
```

**Behavior debugging:**

```
Expected: [what should happen]
Actual: [what happens]
Input: [sample input]

Code: [paste code]

Why the incorrect output?
```

**Intermittent issues:**

```
This error occurs intermittently (~1 in 10 requests):
[error details]

Code path:
[paste code]

What conditions might cause sporadic failures?
```

### Debugging Techniques

Beyond basic prompts, these conversational patterns help navigate complex debugging scenarios:

| Technique | Example Prompt | Use Case |
|-----------|----------------|----------|
| **Hypothesis generator** | "This throws a null error. List all places where a null could cause this: [code]" | Systematic elimination |
| **Rubber duck++** | "I think this bug happens because: [theory]. Here's the code: [code]. Is my reasoning correct?" | Validate reasoning |
| **Trace explainer** | "Here's a trace of a failing request: [logs]. Walk me through what's happening." | Understand execution |
| **Fix validator** | "I think the bug is [X]. My fix: [code]. Will this work? Edge cases?" | Verify solution |
| **Comparative debugging** | "This works: [code A]. This doesn't: [code B]. Why would it fail?" | Find subtle differences |

### Debugging Workflow

**Before asking AI:** Gather exact error messages/stack traces, reproduction steps, relevant code sections, recent changes, and environment details. This context is essential since AI can't observe your system state.

**Start broad, then narrow:** Begin with initial hypotheses, investigate the most likely one, share findings, and iterate. Each round should narrow the search space.

**Verify fixes thoroughly:** When AI suggests a fix, understand why it should work, check for side effects, and test edge cases. Blindly applying fixes can introduce new bugs or mask the real issue.

## Evaluating AI Suggestions

Whether reviewing or debugging, evaluate AI suggestions critically rather than accepting them automatically:

- **Understand the reasoning:** Why is this being suggested? What problem does it claim to solve?
- **Verify validity:** Is the concern actually present? Does the suggestion address it?
- **Contextualize:** Does this apply to your specific situation, conventions, and constraints?
- **Decide:** Accept, modify, or reject with clear reasoning. Document patterns that don't apply to your codebase.
- **Handle false positives:** Note recurring false positives to refine your prompts, but don't let them erode trust in valid feedback.

## Team Practices

### Establish Norms

Agree on AI's role in inspection: which checks are automated vs. human-reviewed, how to handle disagreements with AI suggestions, and when AI inspection is required vs. optional.

### Share Effective Prompts

Build a team collection of prompts that work well for your codebase: security review templates, performance review patterns, common debugging scenarios, and API design checklists.

### Review the Reviewer

Periodically evaluate AI effectiveness by tracking what it catches that humans miss, what it misses that humans catch, and where it generates noise. Adjust your usage patterns based on these findings.

## Key Takeaways

- AI inspection excels at pattern recognition and hypothesis generation but requires human judgment for business logic, architecture, and context-dependent decisions.
- Use it as the first pass before human review to catch routine issues and reduce back-and-forth on simple errors.
- Gather information systematically before debugging sessions—AI can't observe your system state.
- Always verify suggestions critically rather than accepting them automatically.
- Establish clear team practices to maximize benefits while maintaining quality standards.
