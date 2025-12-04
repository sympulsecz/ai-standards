# Tool Use: Fundamentals

Effective AI-assisted development requires understanding both how to communicate with AI (prompting) and which interaction mode to use for different tasks. Modern AI coding tools offer multiple ways to interact, each suited to different types of work.

!!! info "Related Pages"
    - [Tool Use: Guidelines](tool-use-guidelines.md) - What AI does well, safety principles, limitations
    - [Tool Use: Workflows](tool-use-workflows.md) - Practical workflows for review, debugging, refactoring

## Understanding Interaction Modes

Most AI coding tools provide three distinct modes of interaction. Understanding when to use each mode improves efficiency and results.

### Ask Mode

**What it is**: Single-question, single-answer interactions. The AI responds to your question without taking action or maintaining conversation history.

**When to use**:
- Quick lookups ("What does this error mean?")
- Syntax questions ("What's the TypeScript syntax for generics?")
- Conceptual clarification ("How does async/await work?")
- Code explanation ("What does this function do?")

**Characteristics**:
- Fast, immediate responses
- No memory of previous questions
- No code modification
- Low cost per interaction

**Example uses**:
```
Ask: "What's the difference between map and forEach in JavaScript?"
Ask: "How do I check if a file exists in Python?"
Ask: "Explain this regex pattern: ^[a-z0-9]+$"
```

### Chat Mode

**What it is**: Conversational interaction where the AI maintains context across multiple exchanges. You can discuss approaches, iterate on solutions, and refine ideas before implementation.

**When to use**:
- Exploring different approaches to a problem
- Iterative design of complex logic
- Learning unfamiliar concepts or patterns
- Debugging issues through conversation
- Reviewing and refining generated code before applying it

**Characteristics**:
- Maintains conversation history
- Allows iterative refinement
- You manually apply suggested changes
- Built-in review checkpoint (you decide what to use)

**Example workflow**:
```
You: "I need to implement rate limiting for our API"
AI: "Here are three approaches: token bucket, sliding window, fixed window..."
You: "Tell me more about token bucket"
AI: "Token bucket works by..."
You: "Show me an implementation using Redis"
AI: [provides code]
You: "Adjust this to allow burst traffic"
AI: [refines code]
```

**Best practices**:
- Start new chat for new topics (don't let context get too long)
- Summarize key decisions before requesting final code
- Copy useful code into your editor incrementally
- Verify each piece before requesting the next

### Agent Mode

**What it is**: Autonomous operation where the AI plans multi-step tasks, modifies multiple files, runs commands, and iterates based on results—all without requiring approval for each action.

**When to use**:
- Implementing features across multiple files
- Refactoring that touches many locations
- Setting up project scaffolding
- Running tests and fixing failures iteratively
- Tasks requiring coordination between files

**Characteristics**:
- High autonomy within defined scope
- Can create, modify, delete files
- Can execute commands (tests, builds, git)
- Continues working until goal achieved or stuck
- Higher cost per task

**Example uses**:
```
"Add input validation to all API endpoints using Zod schemas"
"Refactor authentication to use the new AuthService across all routes"
"Set up Jest testing infrastructure with example tests"
"Implement the User model, repository, service, and controller layers"
```

**Important considerations**:

Agent mode trades speed for autonomy. It works well when:
- The goal is well-defined
- Project conventions are documented in instruction files
- You can review changes before committing
- The cost of mistakes is low (development environment, version controlled)

Agent mode struggles when:
- Requirements are ambiguous
- You haven't established clear conventions
- The task requires subjective judgment
- Each decision depends on previous outcomes you need to validate

**Working with agent mode**:
- Provide clear, specific goals
- Ensure instruction files are current
- Monitor progress (don't disappear while agent works)
- Intervene if agent gets stuck in loops
- Review all changes before committing

### Choosing the Right Mode

| Scenario | Recommended Mode | Why |
|----------|-----------------|-----|
| "What does this error mean?" | Ask | Simple lookup, no action needed |
| "How should I structure this feature?" | Chat | Explore approaches, iterate on design |
| "Implement user authentication" | Chat first, then Agent | Design in chat, implement with agent |
| "Add type hints to all Python files" | Agent | Mechanical task across many files |
| "Why is this test failing?" | Chat | Need interactive debugging |
| "Fix this test failure" | Agent | Once you know the fix, agent can apply it |
| "Review this code for issues" | Chat | You control what gets changed |
| "Refactor to use our new pattern" | Agent | Well-defined transformation |

**Progressive escalation**:

Often the best workflow moves through modes:

1. **Ask**: "What's the best way to handle file uploads in Express?"
2. **Chat**: Discuss approach, review example code, refine for your use case
3. **Agent**: "Implement file upload handling following the pattern we discussed"

This progression lets you stay in control of decisions while delegating implementation to the agent.

## Core Prompting Principles

Regardless of mode, effective prompting follows consistent principles.

### Be Specific

Vague requests produce vague results. Compare:

| Less Effective | More Effective |
|----------------|----------------|
| "Write a function to process data" | "Write a function that takes a list of user objects and returns only those with verified email addresses" |
| "Fix this code" | "This function throws a null reference error when the input array is empty. Add a guard clause." |
| "Make this better" | "Refactor this to extract the validation logic into a separate function" |

### Provide Context

AI needs sufficient context to generate appropriate solutions. Include:

- **Relevant code**: The function, class, or file being discussed
- **Constraints**: Language, framework, style requirements
- **Purpose**: What the code should accomplish
- **Environment**: Where this code runs, what it interacts with

!!! tip "Context vs Instruction Files"
    Project conventions belong in instruction files (see [Instruction Files](instruction-files.md)). Don't repeat coding standards or framework choices in every prompt—AI tools read instruction files automatically.

    **Do include in prompts**: Task-specific context like "this function is called on every request" or "this runs in a background worker."

!!! tip "The Context Checklist"
    Before prompting, ask yourself:

    - Does the AI have the code it needs to see?
    - Does it know what I'm trying to achieve?
    - Are there constraints it should know about?
    - Is there existing code it should match?

### Show, Don't Just Tell

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

### Break Down Complex Tasks

Large tasks often produce better results when decomposed:

Instead of: "Build a user authentication system"

Try:

1. "Design the data model for user authentication (users, sessions, tokens)"
2. "Write the password hashing and verification functions"
3. "Create the login endpoint with validation"
4. "Add session management logic"

Each focused prompt allows you to verify and refine before continuing.

## Prompting Patterns

### Structured Request

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

### Iterative Refinement

Start broad, then narrow:

1. "Suggest three approaches to implement caching for this API"
2. "Expand on approach #2 with implementation details"
3. "Write the cache invalidation logic for that approach"

This pattern works particularly well in chat mode.

### Rubber Duck

Use AI as an intelligent sounding board:

```
I'm trying to decide between these approaches for handling user permissions:

Approach A: Store permissions as a JSON array on the user record
Approach B: Create a separate permissions table with a many-to-many relationship

Our use case: ~10k users, permissions change rarely, we query permissions on every API request.

What are the tradeoffs I should consider?
```

### Constraint-First Request

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

### When to Switch Modes

If chat mode repeatedly produces poor results, consider:
- Switching to ask mode to clarify specific concepts
- Switching to agent mode if the issue is execution rather than approach
- Starting a new chat to clear confused context

## Anti-Patterns

### Prompt Dumping

Throwing massive amounts of unstructured information:

```
Here's my entire codebase [10,000 lines]. Fix the bug.
```

**Better**: Identify the relevant code and include only that.

### Assumption of Context

Expecting the AI to know things you haven't told it:

```
Update the user model.
```

**Better**: "Update the User model in `src/models/user.ts` to add an `isVerified` boolean field."

### Vague Quality Requests

```
Make this code better.
```

**Better**: Specify what "better" means—more readable? More performant? Better error handling?

### Wrong Mode for Task

Using ask mode for complex implementation or agent mode for exploratory questions. Match the mode to the task complexity and autonomy needs.

### Ignoring Output

Accepting AI output without review. Always:

- Read the generated code
- Verify it does what you expect
- Test it
- Check for security issues

This applies regardless of mode, but is especially critical in agent mode where changes are applied automatically.

## Key Takeaways

- Choose the right interaction mode for your task (ask for questions, chat for iteration, agent for implementation)
- Escalate through modes as tasks become more complex
- Specificity beats verbosity
- Context enables accurate responses, but don't repeat instruction files
- Examples guide output format
- Break complex tasks into steps
- Iterate and refine based on results
- Always review and verify output

Next: Apply these techniques in [practical workflows](tool-use-workflows.md) for code review, debugging, and refactoring.
