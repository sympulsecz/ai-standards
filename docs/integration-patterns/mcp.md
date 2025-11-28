# Model Context Protocol

MCP is an open standard for connecting AI systems to external data sources and tools through a standardized protocol.

## What is MCP?

MCP provides a universal adapter between AI assistants and external systems, replacing custom integrations with a common protocol. Instead of building N×M integrations (every AI app × every data source), MCP enables building N+M (AI apps implement MCP client, data sources implement MCP server).

### Key Benefits

| Benefit | Description |
|---------|-------------|
| **Interoperability** | Servers work with any MCP client |
| **Modularity** | Add/remove capabilities independently |
| **Security** | Clear boundaries between AI and external systems |
| **Reusability** | Build once, use across different AI applications |

## Architecture

MCP uses a three-layer architecture:

```
┌─────────────────────────────────────────────────┐
│         Application Layer                       │
│    (Tools, Resources, Prompts)                  │
├─────────────────────────────────────────────────┤
│         Protocol Layer                          │
│         (JSON-RPC 2.0)                          │
├─────────────────────────────────────────────────┤
│         Transport Layer                         │
│    (stdio, HTTP+SSE, WebSocket)                 │
└─────────────────────────────────────────────────┘
```

### Transport Options

| Transport | Use Case | Characteristics |
|-----------|----------|-----------------|
| **stdio** | Local tools | Simple, subprocess-based, common for local tools |
| **HTTP+SSE** | Remote servers | Network-capable, supports long operations |
| **WebSocket** | Real-time apps | Full duplex, lower latency |

### Protocol Layer

MCP uses JSON-RPC 2.0 for all communication. Requests specify a method and parameters, responses contain results or errors.

## Server Capabilities

MCP servers expose three types of capabilities:

| Capability | Purpose | Example |
|------------|---------|---------|
| **Tools** | Actions the AI can invoke | Search files, query database, send email |
| **Resources** | Data the AI can read | Config files, documentation, databases |
| **Prompts** | Pre-defined templates | Code review template, analysis framework |

### Tools

Tools are functions with defined inputs and outputs. Each tool specifies a name (unique identifier), description (helps AI decide when to use it), input schema (JSON Schema for parameters), and returns content in various formats.

### Resources

Resources are identified by URIs (e.g., `file:///config.json`, `doc://guide/setup`). They can be static (fixed content), dynamic (generated on request), or templated (URI patterns with parameters).

### Prompts

Prompts are reusable templates with parameters, useful for standardizing common tasks and ensuring consistent approaches.

## When to Use MCP

MCP is valuable when you want AI to access internal systems, need modular and composable AI capabilities, or want to share AI integrations across teams. It might be overkill for simple one-off API calls or when standardization benefits aren't needed.

## Building MCP Servers

### Design Process

Before implementation, define the server's purpose, identify which capabilities to expose (tools, resources, prompts), and write descriptions from the AI's perspective.

### Tool Design Patterns

**Query tools** retrieve information and should return structured data with relevance indicators, support filtering, and paginate large results.

**Action tools** perform operations and should validate inputs thoroughly, return confirmation of actions taken, and consider idempotency.

**Composite tools** combine multiple operations but require careful consideration of whether granular tools would be better.

### Input Validation

Validate inputs at two levels:

1. **Schema validation**: Type checking, range validation, required fields
2. **Business logic**: Permissions, path access, injection prevention

```python
def validate_search_request(query, path):
    # Ensure path is within allowed directories
    if not is_within_allowed_paths(path):
        raise ValidationError("Path not accessible")

    # Check for dangerous patterns
    if contains_injection_attempt(query):
        raise ValidationError("Invalid query pattern")
```

### Error Handling

Structure errors with code (for programmatic handling), message (human-readable), and actionable details when possible.

| Error Category | Examples |
|----------------|----------|
| **User errors** | Invalid input, missing fields, resource not found, permission denied |
| **System errors** | Service unavailable, timeout, internal failure |

### Performance Considerations

Target response times: simple queries <100ms, database lookups <500ms, complex operations <2s. Use caching for expensive operations (but not for user-specific or frequently changing data) and implement pagination for large result sets.

### Security Best Practices

Follow the principle of least privilege (expose only what's necessary), sanitize all inputs before use, use parameterized queries for databases, and implement audit logging for significant operations.

### Testing

Test servers at three levels: unit tests for individual tools, integration tests for the full server, and manual testing with actual AI clients to verify usefulness and accuracy.

## Architecture Patterns

| Pattern | Structure | Benefits |
|---------|-----------|----------|
| **Single-Purpose** | One server, one job | Simple, focused, easy to maintain |
| **Composite** | Multiple capabilities in one server | Related capabilities together, fewer connections |
| **Gateway** | One server aggregates others | Single connection point, unified access control |

## Key Takeaways

MCP provides standardized integration between AI systems and external capabilities through a three-layer architecture. Servers expose tools (actions), resources (data), and prompts (templates) with clear security boundaries and validation. Successful MCP servers are well-designed with clear descriptions, thorough validation, useful error messages, and appropriate performance optimizations.
