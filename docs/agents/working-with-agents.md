# Working with Agents

Agentic coding tools like Cursor, Claude Code, and similar assistants differ fundamentally from chat-based AI or autocomplete systems. Rather than suggesting code and waiting for you to apply it, these tools autonomously execute individual steps—creating files, running commands, and modifying code—as they work toward your goal.

This autonomy within steps doesn't mean agents work in isolation. They collaborate with you: asking clarifying questions when requirements are unclear, reporting progress, and seeking guidance when stuck. Understanding this balance between autonomous execution and collaborative direction helps you work effectively with agents.

## How Agentic Tools Work

At their core, agentic coding tools follow a continuous loop:

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│   Observe → Reason → Act → Observe (new state) ─┐    │
│      ▲                                          │    │
│      └──────────────────────────────────────────┘    │
│                                                      │
└──────────────────────────────────────────────────────┘
```

The agent gathers information about the current state (observe), decides what to do next (reason), executes an action (act), and repeats until the goal is achieved or it determines it needs guidance. This continuous loop differs from chat-based assistants that generate a single response and stop.

## What Agents Can Do

Agentic tools have access to various capabilities that enable multi-step work:

**File operations**: Reading any file in the project, creating new files, modifying existing files, and moving or deleting files.

**Command execution**: Running tests, executing build commands, invoking linters and formatters, and running git commands.

**Codebase search**: Searching for text patterns, finding function definitions, locating usages of symbols, and understanding project structure.

**Context management**: Reading instruction files, accessing git history, examining recent changes, and maintaining conversation context.

The combination of these capabilities allows agents to handle complex tasks that would require multiple manual steps from a developer.

## Agent Behaviors

Agents use different patterns to accomplish tasks. Recognizing these helps you understand what's happening and when to intervene.

| Behavior | What You'll See | Why It Matters |
|----------|-----------------|----------------|
| **Planning** | "Here's what I'll do: 1... 2... 3..." | Review and adjust approach before execution starts |
| **Reasoning & Acting** | "Thinking: I need to..." followed by action | Most common pattern—shows decision process before each step |
| **Reflection** | "Let me review this..." before final output | Agent self-correcting to catch errors (less common, explains delays) |
| **Tool Use** | "Searching codebase...", "Running tests..." | Agent invoking specific capabilities—recognize if it's choosing wrong tools |

## Agent Limitations

Agents work well within defined boundaries but struggle in certain scenarios.

**What agents handle well**:

- Implementing well-specified features with clear patterns in the codebase
- Refactoring code using established patterns from instruction files
- Writing tests based on existing test patterns
- Debugging with clear error messages and reproduction steps
- Following explicit project conventions

**What agents struggle with**:

- Ambiguous requirements without clear acceptance criteria
- Novel problems unlike patterns in training data or codebase
- Complex business logic requiring deep domain knowledge
- Tasks requiring human judgment about trade-offs
- Understanding unstated organizational context

Recognizing these boundaries helps you decide when to provide more context versus when to handle something manually.

## Security and Safety Considerations

Agentic tools can execute commands and modify files autonomously, which introduces risks that don't exist with chat-based assistants.

**Command execution risks**: Agents might run expensive operations (cloud deployments, database migrations), modify production configuration if not properly scoped, or execute commands with unintended side effects.

**File modification risks**: Overwriting important files without backups, modifying files outside the intended scope, or introducing security vulnerabilities through generated code.

**Mitigation strategies**:

Use version control and commit frequently so agent changes can be reviewed and reverted. Configure agents to request confirmation for dangerous operations (deployments, database changes, file deletions). Review agent-generated code as carefully as you'd review a colleague's work. Maintain instruction files that specify security patterns and required checks. Work in development environments, not directly in production.

Many agentic tools offer safety features like dry-run modes, confirmation prompts for certain operations, or sandboxed execution environments. Configure these based on your risk tolerance.

## When to Use Agents

Not every problem needs an agent. Agents excel at certain tasks but simpler approaches work better for others.

**When agents work well**:

| Task Type | Why Agents Help |
|-----------|----------------|
| Rename a variable across multiple files | Agent can search and replace accurately across the codebase |
| Implement a feature following existing patterns | Agent can reference patterns from instruction files and apply consistently |
| Debug a failing test with clear error | Agent can iterate on fixes based on error output |
| Refactor code to match established patterns | Agent can apply transformations systematically |
| Set up boilerplate following conventions | Agent can generate structured code from templates |

**When to work manually**:

| Task Type | Why Manual is Better |
|-----------|---------------------|
| Fix a typo in one place | Manual fix is instant; agent overhead adds no value |
| Design a new architecture | Requires human judgment about trade-offs and long-term implications |
| Understand why a feature was designed a certain way | Requires historical/organizational context agents don't have |
| Make quick exploratory changes | Manual editing is faster for rapid trial-and-error |
| Handle highly sensitive production code | Risk of agent mistakes outweighs convenience |

!!! warning "Key Principle"
    Use agents for well-defined, pattern-based work where iteration and systematic application add value. Work manually for tasks requiring a lot of careful judgment, deep or hidden domain knowledge, prior historical context, or where the overhead of explaining the task exceeds doing it yourself.

Be specific when you do use agents. Vague requests produce vague results:

❌ **Vague**: "Make the code better"

✅ **Specific**: "Refactor the authentication logic to use the middleware pattern shown in src/middleware/auth.ts"

## Iterating with Agents

Complex tasks require iteration between you and the agent. You provide a goal, the agent works autonomously until it encounters an issue or ambiguity, then asks for clarification before continuing with refined understanding.

This collaborative approach works better than expecting a single prompt to cover all scenarios. Agents are autonomous in execution but collaborative in direction—like a capable junior developer who can handle tasks independently but checks in when uncertain.

### Leverage Instruction Files

Agents automatically read instruction files when making decisions. You don't need to repeat conventions from your `CLAUDE.md` or `.cursorrules` in every prompt—the agent already has that context.

Instead of saying "Use TypeScript strict mode and functional components with hooks," rely on your instruction files to specify that. Your prompts can focus on the specific task.

!!! tip "Using Git Worktrees with Agents"
    Git worktrees let you work on multiple branches simultaneously in separate directories. This is particularly useful when working with agents:

    - Run multiple agents in parallel on different tasks without conflicts
    - Keep your main workspace clean while agents experiment in worktrees
    - Easily compare agent outputs across different approaches
    - Switch between agent work and manual work without stashing changes

    Create a worktree with: `git worktree add ../feature-branch feature-branch`

### Monitor and Intervene

Watch what the agent is doing to catch issues early. Most tools provide visibility through logs, step-by-step output, or conversation history. Pay attention to which files it reads (context it's considering), which tools it executes (its approach), reasoning steps it outputs (decision-making process), and how it responds to errors (learning vs looping).

Agents can get stuck in loops, repeatedly trying the same failing approach. Signs include making the same change multiple times, running the same failing test without adjusting code, or searching for the same thing repeatedly. When you notice loops, interrupt and provide additional context or constraints to break the pattern.

## Next Steps

If you're building your own agent systems rather than using existing tools, see [Building Agents](building-agents.md) for API integration patterns and implementation guidance.

To extend agentic tools with custom capabilities, see [MCP (Model Context Protocol)](mcp.md) for connecting agents to external data sources and tools.

## Related Reading

- [Instruction Files](../ai-assisted-development/instruction-files.md) - Configuring agent behavior for your project
- [Tool Use: Workflows](../ai-assisted-development/tool-use-workflows.md) - Practical patterns that work with agents
- [Building Agents](building-agents.md) - Creating your own agent systems
