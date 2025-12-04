# Agents

Agents are AI systems that autonomously plan tasks, use tools, and iterate toward goals. If you're using agentic coding tools like Cursor or Claude Code, this section explains how they work and how to use them effectively. If you're building agent systems into your applications, this section covers API integration, tool design, and extending agents with custom capabilities.

## What You'll Learn

**[Working with Agents](working-with-agents.md)** explains how agentic coding tools differ from chat-based AI and autocomplete systems. You'll understand the observe-reason-act loop that powers these tools, learn what agents can and cannot do well, and develop strategies for working effectively with autonomous systems.

**[MCP (Model Context Protocol)](mcp.md)** covers extending agents with custom capabilities through the Model Context Protocol standard. You'll learn to use existing MCP servers to connect agents to databases and internal systems, understand when to create custom servers, and learn security considerations for agent extensions.

**[Building Agents](building-agents.md)** covers creating your own agent systems: integrating with LLM APIs, managing context and costs, designing tools agents can use, implementing error handling and observability, and testing agent behavior.

Start with [Working with Agents](working-with-agents.md) if you're using tools like Cursor or Claude Code. Explore [MCP](mcp.md) to extend agents with custom capabilities. Move to [Building Agents](building-agents.md) if you're creating agent systems for your applications.

## Related Topics

The [AI-Assisted Development](../ai-assisted-development/index.md) section covers daily workflows with AI coding tools. Many patterns there work with agentic tools, but that section focuses on usage while this section explains the underlying systems and how to build them.

The [Testing](../testing.md) and [CI/CD](../ci-cd.md) pages cover patterns for integrating AI into development workflows.

The [Security](../security/index.md) section addresses security concerns specific to AI systems, including data handling and compliance considerations that apply when using or building agents.
