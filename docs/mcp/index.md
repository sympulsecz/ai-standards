# Model Context Protocol (MCP)

The Model Context Protocol is an open standard for connecting AI systems to external data sources and tools. Understanding MCP helps you build more capable AI integrations.

## What You'll Learn

- **Architecture**: How MCP works and its core concepts
- **Building Tools**: How to create MCP servers that expose capabilities

## What is MCP?

MCP provides a standardized way for AI systems to:

- Access external data sources
- Execute tools and functions
- Retrieve contextual information
- Interact with services and APIs

Think of it as a universal adapter between AI assistants and the tools they need.

### The Problem MCP Solves

Without standardization, every AI integration requires custom code:

```
┌─────────────┐     Custom      ┌─────────────┐
│   AI App    │◄───────────────►│  Database   │
└─────────────┘    Protocol     └─────────────┘
       │
       │            Custom      ┌─────────────┐
       └───────────────────────►│    API      │
                   Protocol     └─────────────┘
```

With MCP, integrations use a common protocol:

```
┌─────────────┐                 ┌─────────────┐
│   AI App    │                 │  Database   │
│  (Client)   │◄────────┐       │  (Server)   │
└─────────────┘         │       └─────────────┘
                        │               ▲
                       MCP              │
                     Protocol     ┌─────┴─────┐
                        │         │    API    │
                        │         │  (Server) │
                        ▼         └───────────┘
                ┌───────────────┐
                │  Any Server   │
                └───────────────┘
```

### Key Benefits

- **Interoperability**: Servers work with any MCP client
- **Modularity**: Capabilities can be added/removed independently
- **Security**: Clear boundaries between AI and external systems
- **Reusability**: Build once, use across different AI applications

## Core Concepts

### Servers and Clients

**MCP Server**: Exposes capabilities (tools, resources, prompts)  
**MCP Client**: Consumes capabilities (AI applications, assistants)

A single AI application can connect to multiple servers, gaining combined capabilities.

### Capabilities

MCP servers can provide:

| Capability | Purpose | Example |
|------------|---------|---------|
| **Tools** | Actions the AI can take | Search files, query database, send email |
| **Resources** | Data the AI can read | Configuration files, documentation, databases |
| **Prompts** | Pre-defined prompt templates | Code review template, analysis framework |

### The Protocol

MCP uses JSON-RPC for communication, supporting:

- Synchronous request/response
- Notifications
- Progress updates
- Error handling

## When to Use MCP

MCP is valuable when:

- You want AI to access internal systems
- You're building AI features that need external data
- You want modular, composable AI capabilities
- You need to share AI integrations across teams

MCP might be overkill when:

- Simple API calls suffice
- The integration is one-off and won't be reused
- You don't need the standardization benefits

## Sections

- [Architecture](architecture.md) - Deeper dive into how MCP works
- [Building Tools](building-tools.md) - Practical guide to creating MCP servers

