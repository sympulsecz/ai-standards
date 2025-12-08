# Code Review & Debugging Prompts

## Part 1: Code Review

### Basic Review Request

Use with `code/buggy-cart.ts`:

```
Review this shopping cart implementation for potential bugs or issues:

[paste the code]
```

**Expected findings:**

- The `removeItem` function has an issue with array indexing
- Empty cart handling might be problematic
- No validation on quantity values

### Focused Review

```
Review this code specifically for:
- Edge cases that might cause errors
- Off-by-one errors
- Empty/null handling
```

**What to point out:** Being specific about what to look for gets better results.

---

## Part 2: Debugging with Context

### Structured Debugging Prompt

```
I'm getting this error:
TypeError: Cannot read property 'price' of undefined

Happens when: I remove the last item from the cart, then try to get the total

Relevant code:
[paste buggy-cart.ts]

What's causing this and how do I fix it?
```

**What to point out:**

- Error message alone isn't enough
- The trigger condition is crucial
- Relevant code helps AI understand context

### Quick Debug

For simpler issues:

```
This code throws an error when the array is empty. Why?

[paste small code snippet]
```

---

## Part 3: Comparative Review

When you have two implementations:

```
Compare these two approaches and tell me which is better and why:

Approach A:
[paste code A]

Approach B:
[paste code B]

Context: This runs on every API request, so performance matters.
```

---

## Part 4: Understanding Unfamiliar Code

```
Explain what this function does in plain English:

[paste code]

Focus on:
- What it takes as input
- What it returns
- Any side effects
```

---

## Review Workflow Recap

1. **First pass with AI** - catch obvious issues
2. **Human review** - context-dependent decisions
3. **Verify fixes** - don't blindly apply suggestions
4. **Document learnings** - what patterns to watch for
