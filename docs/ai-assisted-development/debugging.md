# Debugging with AI

AI can be a powerful debugging partner, helping you understand errors, explore hypotheses, and find solutions faster.

## The Debugging Conversation

Unlike traditional debugging tools, AI debugging is conversational. You can:

- Describe symptoms and get diagnostic suggestions
- Share error messages and stack traces for interpretation
- Explore hypotheses through discussion
- Get explanations of why something might be failing

## Effective Debugging Prompts

### Error Interpretation

When you have an error message:

```
I'm getting this error:

[paste error message and stack trace]

This happens when [describe the action/trigger].

Relevant code:
[paste the code around where the error occurs]

What could cause this?
```

### Behavior Debugging

When code runs but produces wrong results:

```
Expected behavior: [what should happen]
Actual behavior: [what actually happens]

Input: [sample input that triggers the issue]

Code:
[relevant code]

Why might this be producing incorrect output?
```

### Intermittent Issues

For bugs that don't always reproduce:

```
This error occurs intermittently (roughly 1 in 10 requests):

[error details]

The code path involves:
[relevant code]

What conditions might cause this to fail sometimes but not always?
```

## Debugging Patterns

### The Hypothesis Generator

Use AI to brainstorm possible causes:

```
This function throws a null reference error somewhere, but I can't figure out where.

[code]

Generate a list of all places where a null value could cause this error.
```

Then systematically verify each hypothesis.

### The Rubber Duck++

Explain your understanding and let AI challenge it:

```
I think this bug is happening because:
1. The cache expires
2. The next request hits the database
3. But the database connection pool is exhausted

Here's the relevant code: [code]

Is my reasoning correct? What might I be missing?
```

### The Trace Explainer

When you have logs or traces but don't understand them:

```
Here's a trace of a failing request:

[log output]

Walk me through what's happening at each step and where things go wrong.
```

### The Fix Validator

Before implementing a fix, validate the approach:

```
I think the bug is [description].

My proposed fix:
[code change]

Will this fix the issue? Are there any edge cases I'm missing?
```

## What AI Debugging Does Well

### Pattern Recognition in Errors

AI has seen countless error messages and can often quickly identify:

- Common causes of specific error types
- Framework-specific issues
- Language-specific gotchas
- Library version conflicts

### Generating Test Cases

```
This function has a bug with certain inputs. Help me generate test cases that might expose edge cases:

[function code]
```

### Explaining Complex Behavior

When code behavior is confusing:

```
Why does this code produce [unexpected result]?

[code]

Walk through the execution step by step.
```

### Suggesting Diagnostic Steps

```
This API endpoint sometimes times out. What diagnostic steps should I take to identify the cause?

[endpoint code]
```

## What AI Debugging Does Poorly

### Stateful System Understanding

AI can't know:

- The actual state of your database
- Current values in your cache
- What's in memory right now
- Your production environment configuration

You need to gather this information and share it.

### Timing-Dependent Issues

Issues involving:

- Race conditions
- Deadlocks
- Timing-sensitive operations

These often require more context than can easily be conveyed to AI.

### Environment-Specific Problems

AI can't directly observe:

- Your network configuration
- Your OS-level settings
- Your specific dependency versions
- Your deployment environment

Share relevant details explicitly.

## Debugging Workflow

### 1. Gather Information First

Before asking AI, collect:

- [ ] Exact error message and stack trace
- [ ] Steps to reproduce
- [ ] Relevant code sections
- [ ] Recent changes that might be related
- [ ] Environment details (if relevant)

### 2. Start Broad, Then Narrow

1. Describe the problem and get initial hypotheses
2. Pick the most likely hypothesis and investigate
3. Share findings and narrow further
4. Repeat until root cause is found

### 3. Verify Fixes Thoroughly

When AI suggests a fix:

1. Understand why it should work
2. Check for side effects
3. Test the fix thoroughly
4. Consider edge cases

!!! warning "Don't Just Apply Fixes Blindly"
    Understanding why a fix works is as important as fixing the bug. Blindly applying suggestions can introduce new bugs or mask the real issue.

## Advanced Techniques

### Bisecting with AI Help

When you're not sure which change introduced a bug:

```
The bug was introduced somewhere in these changes:

[diff or commit list]

Based on the error [description], which changes are most likely to have caused it?
```

### Minimal Reproduction

```
I have this bug in a complex system. Help me create a minimal reproduction case.

The bug: [description]
The system: [high-level description]
The error: [error message]
```

### Comparative Debugging

```
This code works:
[working code]

This similar code doesn't:
[broken code]

The difference seems minor. Why would it fail?
```

## Key Takeaways

- AI debugging is conversational—share context, explore hypotheses
- Gather information before asking for help
- AI excels at pattern recognition and generating hypotheses
- Verify fixes thoroughly; understand why they work
- AI can't observe your system state—you must provide that context
