# Effective Prompting

Prompting is the skill of communicating with AI systems to get useful results. Like any communication skill, it improves with practice and understanding of the medium.

## Core Principles

### 1. Be Specific

Vague requests produce vague results. Compare:

| Less Effective | More Effective |
|----------------|----------------|
| "Write a function to process data" | "Write a function that takes a list of user objects and returns only those with verified email addresses" |
| "Fix this code" | "This function throws a null reference error when the input array is empty. Add a guard clause." |
| "Make this better" | "Refactor this to extract the validation logic into a separate function" |

### 2. Provide Context

AI can only work with information you provide. Include:

- **Relevant code**: The function, class, or file being discussed
- **Constraints**: Language, framework, style requirements
- **Purpose**: What the code should accomplish
- **Environment**: Where this code runs, what it interacts with

!!! tip "The Context Checklist"
    Before prompting, ask yourself:

    - Does the AI have the code it needs to see?
    - Does it know what I'm trying to achieve?
    - Are there constraints it should know about?
    - Is there existing code it should match?

### 3. Show, Don't Just Tell

Examples are powerful. When you want a specific format or style:

```
Generate API endpoints following this pattern:

router.get('/users/:id', async (req, res) => {
  const { id } = req.params;
  const user = await userService.findById(id);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }
  return res.json({ data: user });
});

Now create similar endpoints for: GET /posts/:id, GET /comments/:id
```

This technique (few-shot prompting) guides the AI toward your desired output format.

### 4. Break Down Complex Tasks

Large tasks often produce better results when decomposed:

Instead of: "Build a user authentication system"

Try:

1. "Design the data model for user authentication (users, sessions, tokens)"
2. "Write the password hashing and verification functions"
3. "Create the login endpoint with validation"
4. "Add session management logic"

Each focused prompt allows you to verify and refine before continuing.

## Prompting Patterns

### The Structured Request

Organize complex requests with clear sections:

```
## Task
Refactor the UserService class to use dependency injection.

## Current Code
[paste code here]

## Requirements
- Constructor should accept dependencies
- No direct instantiation of dependencies inside the class
- Maintain all existing public method signatures

## Constraints
- Keep changes minimal
- No new external dependencies
```

### The Iterative Refinement

Start broad, then narrow:

1. "Suggest three approaches to implement caching for this API"
2. "Expand on approach #2 with implementation details"
3. "Write the cache invalidation logic for that approach"

### The Rubber Duck

Use AI as an intelligent sounding board:

```
I'm trying to decide between these approaches for handling user permissions:

Approach A: Store permissions as a JSON array on the user record
Approach B: Create a separate permissions table with a many-to-many relationship

Our use case: ~10k users, permissions change rarely, we query permissions on every API request.

What are the tradeoffs I should consider?
```

### The Constraint-First Request

When you have specific requirements, state them upfront:

```
Requirements:
- Must be a pure function (no side effects)
- Must handle null/undefined inputs
- Must be O(n) time complexity or better

Write a function that finds duplicate values in an array.
```

## Handling Poor Results

When AI output isn't what you need:

### Add More Context

The AI may be missing information:

```
[Previous request didn't work]

Additional context: This code runs in a browser environment, so Node.js APIs aren't available. 
Also, we need to support IE11.
```

### Provide Negative Examples

Show what you don't want:

```
Don't use class-based components like:
class MyComponent extends React.Component { ... }

Instead, use functional components with hooks.
```

### Ask for Alternatives

If the first approach isn't suitable:

```
That approach won't work because [reason]. 

Can you suggest an alternative that doesn't require [problematic aspect]?
```

### Correct and Continue

Point out specific issues:

```
The function you provided has a bug: it doesn't handle the case where the array contains null values.

Please fix this specific issue while keeping the rest of the implementation.
```

## Anti-Patterns

### Prompt Dumping

Throwing massive amounts of unstructured information:

```
Here's my entire codebase [10,000 lines]. Fix the bug.
```

Better: Identify the relevant code and include only that.

### Assumption of Context

Expecting the AI to know things you haven't told it:

```
Update the user model.
```

Better: "Update the User model in `src/models/user.ts` to add an `isVerified` boolean field."

### Vague Quality Requests

```
Make this code better.
```

Better: Specify what "better" means—more readable? More performant? Better error handling?

### Ignoring Output

Accepting AI output without review. Always:

- Read the generated code
- Verify it does what you expect
- Test it
- Check for security issues

## Key Takeaways

- Specificity beats verbosity
- Context enables accurate responses
- Examples guide output format
- Break complex tasks into steps
- Iterate and refine based on results
- Always review and verify output
