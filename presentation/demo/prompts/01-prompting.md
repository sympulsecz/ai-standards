# Prompting Demo Prompts

## Part 1: Vague vs Specific

### Vague Prompt (show this first)

```
Write a function to get users
```

**What to point out:** The AI will produce something, but it has to guess:

- What programming language?
- Get users from where?
- What format should they be in?
- Which users - all of them? Filtered?

### Specific Prompt (show this second)

```
Write a TypeScript function that:
- Takes an array of User objects (with id, email, isVerified properties)
- Returns only users where isVerified is true
- Sorts results by email alphabetically
```

**What to point out:** Same task, but AI knows exactly what you need.

---

## Part 2: Iterative Refinement

Use this sequence with `code/user-service.ts` open.

### Step 1: Initial Request

```
Add a function to this file that finds a user by email address.
Return undefined if not found.
```

### Step 2: Refine (after seeing result)

```
Good, but make the email comparison case-insensitive
```

### Step 3: Add Constraint

```
Also add input validation - throw an error if email is empty or not a valid email format
```

### Step 4: Polish

```
Add JSDoc comments explaining the function, its parameters, and what it throws
```

**What to point out after each step:**

- "I didn't try to specify everything upfront"
- "Each iteration builds on the verified previous result"
- "This is how real conversations with AI work"

---

## Part 3: Structured Request (Optional)

If you have time, show how a well-structured request works:

```
## Task
Add pagination to the getVerifiedUsers function

## Current Behavior
Returns all verified users at once

## Requirements
- Accept page number and page size parameters
- Return an object with: users array, total count, hasMore boolean
- Default to page 1, size 10

## Constraints
- Don't modify the User interface
- Keep the existing sorting behavior
```

**What to point out:** Structure makes complex requests clearer.

---

## Prompt Principles Recap

1. **Be specific about outcome** - what, not how
2. **Provide context** - show relevant code
3. **Iterate** - 2-3 rounds is normal
4. **Verify** - check the result makes sense
