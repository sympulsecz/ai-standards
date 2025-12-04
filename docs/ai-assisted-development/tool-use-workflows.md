# Tool Use: Workflows

This page covers practical workflows for common activities: understanding unfamiliar code, reviewing code, debugging issues, and refactoring systems. Each section provides specific prompts, patterns, and examples.

!!! info "Complementary Pages"
    This page focuses on specific workflows and examples. For universal principles that apply across all activities, see [Tool Use: Fundamentals](tool-use-fundamentals.md).

## Understanding Code

When encountering unfamiliar code, AI can explain behavior, document intent, and trace execution flow.

### Explaining Legacy Code

**Basic explanation:**

```
Explain what this function does:
- What is its purpose?
- What are the inputs and outputs?
- What are the main steps?

[paste function]
```

**Detailed analysis:**

```
Analyze this code section:
- What problem does it solve?
- Why might it be structured this way?
- What edge cases does it handle?
- Are there any subtle behaviors or gotchas?

[paste code]
```

### Documentation Generation

**Function documentation:**

```
Generate documentation for this function following our JSDoc style:
- Summary of purpose
- Parameter descriptions with types
- Return value description
- Example usage
- Any important notes or warnings

[paste function]
```

**API documentation:**

```
Document this API endpoint:
- Purpose and use case
- Request format and parameters
- Response format
- Error conditions
- Example request/response

[paste endpoint code]
```

### Tracing Execution

**Following data flow:**

```
Trace how this data flows through the system:
- Input: [describe input]
- Show which functions process it
- Show transformations applied
- Show final output format

[paste relevant code sections]
```

**Understanding side effects:**

```
What side effects does this function have?
- Database modifications
- External API calls
- File system operations
- Global state changes

[paste function]
```

## Code Review

AI review works best as part of a two-stage process: use AI to catch pattern-based issues early, then have humans focus on business logic, architecture, and context-dependent decisions during formal review.

### Review Prompts

**General review:**

```
Review this [authentication/API/database] code for:
- Security vulnerabilities
- Error handling gaps
- Edge cases that might fail
- [Language/framework] best practices

[paste code]
```

**Comparative review:**

```
Compare these implementations and identify functional differences
and potential issues:

Before: [old code]
After: [new code]

Focus on: [specific concerns like performance, correctness, security]
```

**Style and convention review:**

```
Review this code against our conventions:
- Use async/await, not callbacks
- Error handling via Result types
- Functions should be under 50 lines
- Descriptive variable names (no single letters except loop indices)

[paste code]
```

### Review Workflow

**Pre-commit review:** Before submitting for human review, ask AI to review your changes and address obvious issues. This reduces back-and-forth on style and simple errors, allowing human reviewers to focus on higher-level concerns.

**During human review:** Use AI to verify complex logic when reviewers encounter something unclear, explain unfamiliar patterns or library usage, or generate test cases to validate edge case handling.

**Checklist generation:** Ask AI to generate review checklists for specific change types:

```
Generate a review checklist for pull requests that add new API endpoints.
Consider: security, validation, error handling, documentation, tests, backwards compatibility.
```

### Interpreting Feedback

Not all AI suggestions are equally valid. Calibrate confidence based on what's being flagged:

| Higher Confidence | Lower Confidence |
|-------------------|------------------|
| Syntax errors, resource leaks, missing error handling | Business logic correctness, performance in your context |
| Style violations, common security patterns (SQL injection, XSS) | Whether this is the right architectural approach |
| Null pointer risks, off-by-one errors | Appropriateness of abstraction level |

Evaluate each suggestion critically. Valid concerns should be addressed, but false positives and context-mismatched suggestions can be dismissed with clear reasoning.

## Debugging

AI debugging is conversational—you share context, explore hypotheses together, and iterate toward the root cause. The key is providing enough information for AI to generate useful hypotheses while maintaining your own critical judgment.

### When AI Helps with Debugging

AI assistance is valuable for:

- **Pattern recognition**: Correlating error messages with known issues and identifying common causes
- **Code analysis**: Tracing execution flow and spotting logic errors or unhandled edge cases
- **Explanation**: Understanding cryptic errors and identifying which library or framework is involved

### Debugging Prompts

**Error interpretation:**

```
I'm getting this error:
[complete error message and stack trace]

This happens when [trigger condition].

Relevant code:
[paste code section]

What could cause this?
```

**Behavior debugging:**

```
Expected: [what should happen]
Actual: [what happens instead]
Input: [example input that triggers the issue]

Code:
[paste relevant code]

Why the incorrect output?
```

**Intermittent issues:**

```
This error occurs intermittently (~30% of requests):
[error details]

Code path:
[paste code]

What conditions might cause sporadic failures?
```

### Debugging Patterns

**Root cause analysis:**

When bugs are unclear, ask AI to help narrow possibilities:

```
I have a bug where [symptom] occurs under [conditions].

Possible causes I'm considering:
1. [hypothesis 1]
2. [hypothesis 2]
3. [hypothesis 3]

Help me determine which is most likely and suggest diagnostic steps.

[paste relevant code]
```

AI can evaluate each hypothesis, suggest additional possibilities, and recommend diagnostic steps to eliminate options.

**Rubber duck debugging:**

Explaining the problem often reveals the issue:

```
I'm trying to understand why this function returns wrong values.

Here's what it should do:
1. [expected step 1]
2. [expected step 2]
3. [expected step 3]

Here's what I think it's actually doing:
1. [actual step 1]
2. [actual step 2]
3. [actual step 3]

Where's my logic going wrong?

[paste function]
```

**Tracing execution flow:**

For complex code paths:

```
Trace the execution flow for this code when input is [specific input]:
- What value does each variable have at each step?
- Which branches are taken?
- Where might the bug be occurring?

[paste code]
```

**Comparing working vs broken:**

If you have working and broken versions:

```
This function worked correctly before refactoring:
[paste old version]

Now it produces wrong results:
[paste new version]

What changed that could cause [specific symptom]?
```

### Common Debugging Scenarios

**Intermittent bugs:**

For bugs that happen inconsistently:

```
This bug happens intermittently (30% of attempts):
- Symptom: [what happens]
- Conditions: [when it occurs, if known]
- Cannot reliably reproduce

What could cause intermittent behavior here?

[paste code]
```

AI can identify race conditions, timing issues, uninitialized variables, or external dependencies that might cause inconsistency.

**Performance issues:**

For slow code:

```
This function is slower than expected:
- Expected time: [benchmark]
- Actual time: [measured]
- Input size: [data size]

What's the performance bottleneck?

[paste function]
```

AI can spot inefficient algorithms, unnecessary loops, repeated expensive operations, or memory allocation issues.

**Integration bugs:**

When systems don't work together:

```
Integration between [System A] and [System B] is failing:
- Error: [message]
- Expected behavior: [what should happen]
- Data flow: [describe how data moves between systems]

[paste relevant integration code from both sides]
```

**Logic errors:**

For code that runs without errors but produces wrong results:

```
This calculation produces wrong output:
- Input: [example input]
- Expected output: [what it should be]
- Actual output: [what it is]

Walk through the logic step by step.

[paste calculation code]
```

### Verification and Testing

**Verify AI suggestions:**

Never apply fixes without understanding them. For each suggestion:

- Understand why the issue occurs
- Know how the fix addresses it
- Consider whether it might introduce new issues

**Test the fix:**

After applying AI-suggested fixes:

1. Reproduce the original bug to confirm it existed
2. Apply the fix in isolation
3. Verify bug is resolved
4. Test related functionality to ensure no new bugs
5. Run full test suite if available

**Create regression tests:**

Once fixed, add a test that would have caught the bug:

```
Create a test that would catch this bug:
- Bug: [description]
- Fix applied: [what changed]
- Test should fail on broken code, pass on fixed code

[paste relevant code]
```

### Log Analysis

AI can help interpret logs:

```
Analyze these logs to identify the problem:

[paste relevant log excerpt]

The error occurs at [timestamp].
What's the sequence of events leading to the failure?
```

AI can identify error patterns, correlate events, explain cryptic log messages, and suggest what to log additionally for better diagnostics.

## Refactoring

AI can accelerate refactoring by generating transformation patterns, but careful validation ensures behavior remains unchanged.

### When AI Helps with Refactoring

AI assistance works well for:

- **Mechanical transformations**: Renaming consistently, extracting methods from duplicated code, converting between equivalent forms
- **Exploration**: Proposing refactoring approaches, identifying code smells, suggesting design patterns
- **Documentation**: Explaining existing code before refactoring and documenting changes

### Refactoring Patterns

**Extract method:**

Problem: Duplicated code or long functions doing multiple things.

```
Extract this login validation logic into a separate method.
It should:
- Take username and password as parameters
- Return validation result with specific error messages
- Keep the same validation behavior
- Use clear, descriptive naming

[paste code block]
```

**Rename for clarity:**

Problem: Variables, functions, or classes with unclear names.

```
This function is named `process()` but it actually validates
user input and transforms it to API format. Suggest a better name
and show the refactored code with the new name applied everywhere.

[paste function and usage]
```

**Simplify conditionals:**

Problem: Complex nested if statements that are hard to follow.

```
Simplify this conditional logic:
- Use guard clauses to reduce nesting
- Extract complex conditions into named boolean methods
- Preserve exact behavior

[paste conditional logic]
```

**Modernize code:**

Problem: Old code using deprecated patterns or outdated APIs.

```
Modernize this Python code to use:
- Type hints
- F-strings instead of % formatting
- Context managers for file handling
- Dataclasses instead of manual __init__

Keep behavior identical.

[paste old code]
```

### Effective Refactoring Prompts

**Provide clear constraints:**

```
Refactor this function to:
- Extract database logic into separate methods
- Keep exact error handling behavior
- Maintain transaction semantics
- Use existing naming conventions (snake_case, verb_noun pattern)

[paste function]
```

**Show examples of preferred patterns:**

```
Refactor these functions to follow this pattern:

Example of our preferred pattern:
[paste example]

Functions to refactor:
[paste target functions]
```

**Specify what NOT to change:**

```
Refactor the data transformation logic in this function.
DO NOT change:
- Error handling
- Logging statements
- Return type
- Public method signature

[paste function]
```

### Testing Refactored Code

**Behavior verification:**

Run existing test suite and verify all tests still pass. For code without tests, add characterization tests before refactoring—tests that verify current behavior even if it's not ideal.

**Edge case validation:**

Check boundary conditions, null/empty inputs, error cases, and concurrent access patterns if applicable.

**Performance comparison:**

For performance-sensitive code, benchmark before and after refactoring to ensure no degradation.

### Common Pitfalls

**AI changes behavior subtly:** AI might "improve" error handling by adding cases that weren't there, change validation logic while refactoring, or alter edge case behavior inadvertently. Always verify behavior is preserved.

**AI over-abstracts:** AI sometimes creates unnecessary abstractions—extracting methods used only once, creating interfaces for single implementations, or adding layers that don't add value. Prefer simple, direct code over premature abstraction.

**AI misses context:** AI doesn't know about related code outside the context window, team conventions, or why original code was written that way. Provide relevant context explicitly.

**Partial refactoring:** AI might refactor the code you show but miss other places the same pattern occurs, creating inconsistency. Search for similar patterns across the codebase.

### When to Avoid AI for Refactoring

- **Complex business logic**: Domain-specific logic requiring deep understanding
- **Architecture changes**: Significant structural changes need human architectural thinking
- **Code you don't understand**: Always understand code before refactoring
- **High-risk production code**: Critical systems with no test coverage should be approached carefully

## Key Takeaways

**Understanding Code:**
- Ask AI to explain unfamiliar code before modifying it
- Generate documentation for legacy code that lacks it
- Trace execution flow for complex systems

**Code Review:**
- Use AI for pattern-based issues, humans for business logic and architecture
- Provide specific review criteria rather than general "review this"
- Calibrate confidence based on what's being flagged

**Debugging:**
- Provide complete context: errors, expected vs actual behavior, what you've tried
- Use AI for hypothesis generation and pattern recognition
- Always verify fixes and create regression tests

**Refactoring:**
- Make small, focused changes one at a time
- Test before and after to verify behavior preservation
- Watch for subtle behavior changes and over-abstraction
- Understand code before refactoring it

For universal principles that apply across all these workflows, see [Tool Use: Fundamentals](tool-use-fundamentals.md).

## Related Reading

- [Tool Use: Fundamentals](tool-use-fundamentals.md) - Prompting techniques for effective AI communication
- [Instruction Files](instruction-files.md) - Configuring AI for your project
- [Testing with AI](../testing.md) - Generating and improving tests
