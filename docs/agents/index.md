# Agents

AI agents represent a paradigm shift from simple request-response interactions to systems that can take actions, use tools, and work toward goals over multiple steps.

!!! info "Who This Is For"
    This section serves two audiences:

    1. **Tool users** (Cursor, Claude Code, etc.): Understand what's happening under the hood so you can use these tools more effectively and know when they might fail
    2. **Application builders**: Learn to build agent systems using LLM APIs, frameworks, or from scratch

    Start with this overview, then choose your depth based on your needs. If you're just using AI coding tools daily, also check [AI-Assisted Development](../ai-assisted-development/index.md).

## What You'll Learn

- **Architectures**: The patterns and designs that make agents work
- **Building Agents**: Practical approaches to creating reliable agents
- **Safety & Guardrails**: Ensuring agents behave as intended

## What Makes an Agent

The term "agent" is used loosely, but generally refers to AI systems that can:

1. **Take actions**: Execute code, call APIs, modify files—not just generate text
2. **Use tools**: Invoke external capabilities to accomplish tasks
3. **Reason about goals**: Break down objectives into steps
4. **Operate autonomously**: Continue working without constant human guidance
5. **Adapt**: Adjust approach based on results

### Agent vs. Chatbot

| Chatbot | Agent |
|---------|-------|
| Generates text responses | Takes actions in the world |
| Single request-response | Multi-step execution |
| Stateless between messages | Maintains working state |
| Human drives each step | Autonomous within bounds |

### The Agency Spectrum

Systems exist on a spectrum of agency:

```
Low Agency                                              High Agency
    │                                                        │
    ▼                                                        ▼
Autocomplete → Chat → Tool-Using Chat → Task Agent → Autonomous Agent
```

Most practical applications today sit in the "tool-using chat" to "task agent" range.

## Why Agents Matter

Agents unlock capabilities that simple chat interfaces cannot provide:

- **Complex tasks**: Multi-step operations that require sequencing
- **Integration**: Connecting AI reasoning to real systems and data
- **Automation**: Delegating entire workflows, not just individual questions
- **Persistence**: Working on tasks over time, not just in a single session

## The Key Challenge

With increased capability comes increased risk. Agents that can take actions can also:

- Take wrong actions
- Take actions with unintended consequences
- Get stuck in loops
- Cost money (compute, API calls, etc.)
- Affect production systems

This makes reliability and safety critical concerns—covered in detail in the [Safety & Guardrails](safety-guardrails.md) section.

## When to Use Agents

Agents are appropriate when:

- Tasks require multiple steps or decisions
- Integration with external systems is needed
- The task is well-defined but execution varies
- Human oversight can be maintained

Simpler approaches may be better when:

- Tasks are single-step
- Deterministic automation suffices
- Reliability requirements are very high
- The cost of mistakes is severe

## Sections

- [Architectures](architectures.md) - Common patterns for building agents
- [Building Agents](building-agents.md) - Practical implementation guidance
- [API Integration](api-patterns.md) - Patterns for working with LLM APIs
- [RAG Systems](rag.md) - Retrieval-Augmented Generation for grounding responses
- [Safety & Guardrails](safety-guardrails.md) - Ensuring agents behave safely
