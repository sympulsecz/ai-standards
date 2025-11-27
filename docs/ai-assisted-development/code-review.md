# Code Review with AI

AI can augment your code review process, catching certain issues quickly while freeing human reviewers to focus on higher-level concerns.

## What AI Review Does Well

### Pattern Detection

AI excels at recognizing patterns, making it effective at catching:

- **Style inconsistencies**: Naming conventions, formatting, structure
- **Common anti-patterns**: Known problematic patterns in your language/framework
- **Missing error handling**: Unchecked return values, unhandled exceptions
- **Documentation gaps**: Missing docstrings, unclear comments
- **Simple logic errors**: Off-by-one, incorrect conditions, wrong operators

### Boilerplate Verification

AI can quickly verify that standard patterns are followed correctly:

- Required error handling
- Logging conventions
- Input validation patterns
- Standard response formats

### Knowledge Application

AI brings broad knowledge of:

- Language idioms and best practices
- Common security vulnerabilities
- Framework conventions
- Performance considerations

## What AI Review Does Poorly

### Business Logic

AI doesn't understand your domain:

- Is this the right calculation for your pricing model?
- Does this workflow match your business process?
- Are these validation rules correct for your use case?

Human reviewers must verify business logic correctness.

### Architecture Decisions

AI sees code in isolation, missing:

- How this change fits the overall system
- Whether this approach aligns with team decisions
- Long-term maintainability implications
- Strategic technical direction

### Context-Dependent Correctness

AI may miss issues that require understanding:

- Why code was written a certain way
- Historical context and previous decisions
- External system behaviors
- Production environment characteristics

!!! warning "AI as Supplement, Not Replacement"
    AI review should augment human review, not replace it. Use AI to catch what it's good at, freeing humans to focus on what requires human judgment.

## Effective Review Prompts

### General Review

```
Review this code for:
- Potential bugs or logic errors
- Security concerns
- Performance issues
- Adherence to [language] best practices

Code:
[paste code]
```

### Focused Review

When you have specific concerns:

```
Review this authentication code specifically for:
- Session management issues
- Token handling security
- Timing attack vulnerabilities

[paste code]
```

### Comparative Review

When evaluating changes:

```
Compare these two implementations and identify:
- Functional differences
- Potential issues introduced
- Improvements made

Before:
[old code]

After:
[new code]
```

### Style Review

```
Review this code against our style guide:
- Functions should be < 20 lines
- No nested callbacks (use async/await)
- Explicit return types on all functions

[paste code]
```

## AI Review Workflow

### Pre-Commit Review

Before submitting code for human review:

1. Ask AI to review your changes
2. Address obvious issues it catches
3. Consider its suggestions critically
4. Submit cleaner code for human review

Benefits:

- Catch obvious issues early
- Reduce back-and-forth on style issues
- Let human reviewers focus on substance

### During Human Review

Use AI to assist human reviewers:

- Quick verification of complex logic
- Check understanding of unfamiliar code patterns
- Generate test cases to verify behavior
- Explain confusing code sections

### Review Checklist Generation

AI can help ensure comprehensive reviews:

```
Generate a review checklist for a PR that adds a new API endpoint. 
Consider: security, validation, error handling, testing, documentation.
```

## Interpreting AI Review Feedback

### Calibrate Confidence

Not all AI suggestions are equally valid:

| Higher Confidence | Lower Confidence |
|-------------------|------------------|
| Syntax errors | Business logic correctness |
| Null pointer risks | Performance in your specific context |
| Missing error handling | Whether this is the right approach |
| Style violations | Necessity of the code |

### Evaluate, Don't Auto-Accept

For each suggestion:

1. **Understand it**: Why is this flagged?
2. **Verify it**: Is the concern valid?
3. **Contextualize it**: Does it apply to your situation?
4. **Decide**: Accept, modify, or reject with reason

### Handle False Positives

AI will sometimes flag code that's actually correct:

- Note patterns that don't apply to your codebase
- Consider configuring review instructions to skip known false positives
- Don't let false positives erode trust in valid feedback

## Team Practices

### Establish Norms

Agree as a team on:

- What role AI plays in review process
- Which checks are automated vs. human
- How to handle disagreements with AI suggestions
- When AI review is required vs. optional

### Share Effective Prompts

Build a collection of review prompts that work well for your codebase:

- Security review prompt
- Performance review prompt
- API design review prompt
- Test coverage review prompt

### Review the Reviewer

Periodically evaluate AI review effectiveness:

- What does it catch that humans missed?
- What does it miss that humans catch?
- Where does it generate noise?

## Key Takeaways

- AI review catches pattern-based issues effectively
- Business logic and architecture require human judgment
- Use AI review to improve code before human review
- Evaluate suggestions critically, don't auto-accept
- Establish team norms for AI in the review process
