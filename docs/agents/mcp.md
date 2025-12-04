# MCP (Model Context Protocol)

!!! danger "TODO: Add Screenshot"
    Add a screenshot showing how to configure/add a custom MCP server in an existing coding assistant (Cursor, Claude Code, etc.)

Model Context Protocol (MCP) is an open standard for extending agents with custom capabilities. Whether you're using agentic coding tools like Claude Code and Cursor, or building your own agent systems, MCP provides a standardized way to connect agents to databases, APIs, internal tools, and data sources.

## Why MCP Matters

Most AI coding tools work in isolation from your internal systems. MCP bridges this gap, letting AI tools:

- Query your internal databases
- Access company documentation
- Interact with internal APIs
- Read configuration from your systems
- Integrate with development tools

Instead of copying and pasting data into prompts, MCP lets tools access it directly when needed.

## How MCP Works

MCP uses a client-server architecture:

```
┌─────────────────────┐         ┌──────────────────────┐
│  AI Tool (Client)   │  ◄──►   │   MCP Server         │
│  Cursor, Claude Code│         │   (Database, Docs,   │
│                     │         │    API, etc.)        │
└─────────────────────┘         └──────────────────────┘
```

**AI tools** (clients) discover and use capabilities exposed by **MCP servers**. You configure which servers your tool connects to, and the tool handles the rest.

### What MCP Servers Provide

MCP servers can expose three types of capabilities:

| Capability | Purpose | Example |
|------------|---------|---------|
| **Tools** | Actions AI can invoke | Search codebase, query database, call API |
| **Resources** | Data AI can read | Documentation, config files, schemas |
| **Prompts** | Reusable templates | Code review checklist, analysis framework |

## Using Existing MCP Servers

The MCP ecosystem has servers for common use cases. Before building custom servers, check if existing ones meet your needs.

### Finding MCP Servers

**Official servers** are maintained by Anthropic and cover common integrations:

- File system access
- Database connections (PostgreSQL, SQLite)
- Git operations
- Web search
- Documentation access

**Community servers** extend functionality for specific tools and services. Search GitHub for "mcp-server" to find community-contributed servers.

### Configuring MCP Servers

Configuration varies by AI tool, but generally involves specifying server location, transport method (stdio, HTTP, WebSocket), and any required credentials or parameters.

**Example: stdio server configuration (local process)**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    }
  }
}
```

**Example: HTTP server configuration (remote service)**

```json
{
  "mcpServers": {
    "internal-docs": {
      "url": "https://mcp.internal.company.com/docs"
    }
  }
}
```

### Security Considerations

MCP servers run with permissions of the AI tool process and can access anything the tool can access. Before enabling:

- **Review server source code** if possible
- **Grant minimal access** - only necessary directories, databases, APIs
- **Use authentication** when accessing internal services
- **Monitor server activity** through logging

!!! warning "Data Exposure"
    When AI tools use MCP servers, data from those servers goes into the AI's context and may be sent to AI providers. Use MCP servers only with data appropriate for AI processing. See [Security](../security/index.md) for data classification guidance.

## Creating Simple MCP Servers

For unique internal systems, you might create custom MCP servers. The goal is wrapping existing functionality, not building complex infrastructure.

### When to Create Custom Servers

Create custom MCP servers when:

- You have internal APIs or databases AI tools need to access
- Existing servers don't meet your specific needs
- You want to standardize access across multiple AI tools
- Security or compliance requires self-hosted solutions

Use existing servers when:

- Your use case fits common patterns
- Public servers already exist
- You don't need customization
- Time to value matters more than perfect fit

### Simple Server Patterns

Most custom servers wrap existing services:

**Database query server**: Exposes safe, parameterized queries as tools

```python
# Pseudocode - actual implementation needs MCP SDK
@mcp_tool
def get_user_stats(user_id: int):
    """Get statistics for a user ID"""
    # Parameterized query prevents injection
    result = db.execute(
        "SELECT * FROM user_stats WHERE user_id = ?",
        [user_id]
    )
    return result
```

**Documentation server**: Makes internal docs accessible as resources

```python
@mcp_resource("docs://engineering/{topic}")
def get_documentation(topic: str):
    """Retrieve internal engineering documentation"""
    return read_doc_from_wiki(topic)
```

**API wrapper server**: Provides controlled access to internal APIs

```python
@mcp_tool
def create_deployment(environment: str, version: str):
    """Trigger deployment to specified environment"""
    # Validation before calling actual API
    if environment not in ["staging", "qa"]:
        raise ValueError("Invalid environment")

    return deployment_api.create(environment, version)
```

### Implementation Resources

MCP SDKs exist for common languages:

- **Python**: `mcp` package
- **TypeScript/JavaScript**: `@modelcontextprotocol/sdk`
- **Other languages**: JSON-RPC 2.0 implementation works

Refer to [official MCP documentation](https://modelcontextprotocol.io/) for implementation details, examples, and SDK references.

## Common Use Cases

### Development Workflow Integration

**Codebase search**: Let AI search your entire codebase, not just open files

**Build system access**: Query build status, trigger builds, get error logs

**Test execution**: Run specific tests, get coverage reports

### Internal Knowledge Access

**Documentation**: Company wikis, technical specs, architecture docs

**Code standards**: Style guides, security policies, approved libraries

**Historical context**: Past decisions, design docs, incident postmortems

### Data Access

**Database queries**: Let AI query (read-only) development or staging databases

**Configuration**: Access environment configs, feature flags, service endpoints

**Metrics**: Query monitoring systems, dashboards, logs (sanitized)

## Integration Patterns

### Local Development

For individual developer use, stdio servers work well—they run as subprocess of AI tool, no network required, simple configuration.

### Team Standardization

For team-wide capabilities, HTTP servers deployed internally provide centralized service with authentication, consistent access control, and easier updates.

### Hybrid Approach

Combine both: local servers for file system and git operations, remote servers for shared resources like documentation and databases.

## Key Takeaways

- MCP extends AI tools with access to internal systems, databases, and APIs
- Use existing community servers before building custom ones
- Custom servers should wrap existing services, not reinvent infrastructure
- Security matters: validate inputs, grant minimal access, monitor usage
- Start with high-value integrations and expand based on team needs
- MCP works across different AI tools, making integrations reusable

## Related Reading

- [Working with Agents](working-with-agents.md) - Understanding how agents use tools like MCP
- [Building Agents](building-agents.md) - Designing tools and extending agents
- [Security](../security/index.md) - Data handling and classification
- [Official MCP Documentation](https://modelcontextprotocol.io/){:target="_blank"} - Implementation details and SDK references
