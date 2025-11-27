# MCP Architecture

Understanding MCP's architecture helps you design better integrations and debug issues when they arise.

## Protocol Structure

MCP uses a layered architecture:

```
┌─────────────────────────────────────────────────┐
│              Application Layer                   │
│         (Tools, Resources, Prompts)              │
├─────────────────────────────────────────────────┤
│              Protocol Layer                      │
│              (JSON-RPC 2.0)                      │
├─────────────────────────────────────────────────┤
│              Transport Layer                     │
│       (stdio, HTTP+SSE, WebSocket)               │
└─────────────────────────────────────────────────┘
```

### Transport Layer

MCP supports multiple transport mechanisms:

**stdio**: Communication via standard input/output

- Simple, works locally
- Server runs as a subprocess
- Common for local tools

**HTTP with SSE**: HTTP requests with Server-Sent Events for responses

- Works over networks
- Supports long-running operations
- Good for remote servers

**WebSocket**: Bidirectional communication

- Full duplex
- Lower latency
- Suitable for real-time applications

### Protocol Layer

MCP uses JSON-RPC 2.0:

```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_files",
    "arguments": {
      "query": "authentication",
      "path": "/src"
    }
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found 3 files matching 'authentication'..."
      }
    ]
  }
}
```

## Server Capabilities

### Tools

Tools are functions the AI can invoke:

```
Tool Definition:
├── name: unique identifier
├── description: what it does (helps AI decide when to use)
├── inputSchema: JSON Schema for parameters
└── returns: content (text, images, etc.)
```

**Design considerations:**

- Clear, descriptive names
- Thorough descriptions for AI understanding
- Strict input validation
- Informative error messages

### Resources

Resources are data sources the AI can read:

```
Resource:
├── uri: unique identifier (e.g., "file:///config.json")
├── name: human-readable name
├── description: what the resource contains
├── mimeType: content type
└── contents: the actual data
```

Resources can be:

- **Static**: Fixed content
- **Dynamic**: Generated on request
- **Templated**: URI patterns with parameters

### Prompts

Prompts are reusable templates:

```
Prompt:
├── name: identifier
├── description: when to use this prompt
├── arguments: parameters the prompt accepts
└── messages: the prompt content (with placeholders)
```

Useful for:

- Standardizing common tasks
- Ensuring consistent approach
- Sharing best practices

## Lifecycle

### Connection

1. Client initiates connection
2. Server and client exchange capabilities
3. Server lists available tools, resources, prompts
4. Client can start making requests

### Capability Discovery

```
Client                                   Server
  │                                        │
  │──── initialize ───────────────────────►│
  │◄─── capabilities ─────────────────────│
  │                                        │
  │──── tools/list ───────────────────────►│
  │◄─── available tools ──────────────────│
  │                                        │
  │──── resources/list ───────────────────►│
  │◄─── available resources ──────────────│
```

### Request Handling

```
Client                                   Server
  │                                        │
  │──── tools/call ───────────────────────►│
  │     (name, arguments)                  │
  │                                        │
  │                               Execute tool
  │                                        │
  │◄─── result ───────────────────────────│
  │     (content)                          │
```

## Security Model

MCP provides security through boundaries:

### Capability Restriction

Servers only expose what they're designed to expose. The client cannot:

- Access files not exposed as resources
- Call functions not defined as tools
- Bypass the defined interfaces

### Input Validation

Servers validate all inputs against schemas:

- Type checking
- Range validation
- Required fields
- Format constraints

### Sandboxing

Servers run as separate processes:

- Crashes don't affect the client
- Resource limits can be applied
- Permissions can be restricted

!!! warning "Trust Boundaries"
    MCP defines a trust boundary between client and server. Servers should not blindly trust client inputs, and clients should not assume server outputs are safe.

## Error Handling

MCP defines standard error responses:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": {
      "details": "Parameter 'path' must be a valid directory"
    }
  }
}
```

Standard error codes:

- `-32700`: Parse error
- `-32600`: Invalid request
- `-32601`: Method not found
- `-32602`: Invalid params
- `-32603`: Internal error

## Practical Architecture Patterns

### Single-Purpose Servers

One server, one job:

```
┌─────────────┐
│  Database   │──► SQL queries only
│   Server    │
└─────────────┘
```

Benefits: Simple, focused, easy to maintain

### Composite Servers

Multiple capabilities in one server:

```
┌─────────────────┐
│   DevTools      │──► File operations
│    Server       │──► Git commands
│                 │──► Build tasks
└─────────────────┘
```

Benefits: Related capabilities together, fewer connections

### Gateway Pattern

One server aggregates others:

```
┌───────────┐     ┌───────────┐
│  Client   │────►│  Gateway  │────►│ Server A │
└───────────┘     │   Server  │────►│ Server B │
                  └───────────┘────►│ Server C │
```

Benefits: Single connection point, unified access control

## Key Takeaways

- MCP separates transport, protocol, and application layers
- Servers expose tools, resources, and prompts
- Security comes from boundaries and validation
- Error handling follows JSON-RPC conventions
- Choose architecture patterns based on your needs
