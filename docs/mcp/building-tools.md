# Building MCP Tools

This guide covers practical patterns for creating MCP servers that expose useful capabilities to AI systems.

## Design First

Before writing code, design your server's interface:

### Define the Purpose

What problem does this server solve? Be specific:

```
✓ "Allow AI to search and read our internal documentation"
✗ "Documentation server" (too vague)
```

### Identify Capabilities

What tools, resources, or prompts will you expose?

```
Documentation Server:
├── Tools:
│   └── search_docs(query, filters) → results
├── Resources:
│   ├── doc://{doc_id} → document content
│   └── doc://index → document listing
└── Prompts:
    └── analyze_docs → template for document analysis
```

### Consider the AI's Perspective

The AI will read your tool descriptions to decide what to use. Write descriptions that:

- Explain what the tool does in plain language
- Describe when to use it
- Note any limitations or requirements
- Provide examples if helpful

## Tool Design Patterns

### Query Tools

Tools that retrieve information:

```
search_documents:
  description: |
    Search the documentation for relevant information.
    Returns matching documents with relevance scores.
    Use when the user asks about features, APIs, or concepts.
  input:
    query: string (search terms)
    limit: number (max results, default 10)
    category: string? (optional filter)
  output:
    results: array of {title, excerpt, url, score}
```

**Best practices:**

- Return structured data
- Include relevance/confidence indicators
- Paginate large results
- Support filtering

### Action Tools

Tools that do something:

```
create_ticket:
  description: |
    Create a support ticket in the ticketing system.
    Use when the user wants to report an issue or request help.
    Returns the ticket ID for reference.
  input:
    title: string (brief description)
    description: string (full details)
    priority: "low" | "medium" | "high"
  output:
    ticket_id: string
    url: string (link to ticket)
```

**Best practices:**

- Validate inputs thoroughly
- Return confirmation of action taken
- Include references/links to created items
- Consider idempotency

### Composite Tools

Tools that combine multiple operations:

```
analyze_and_report:
  description: |
    Run analysis on the specified data and generate a report.
    This combines data fetching, analysis, and formatting.
    Use for comprehensive analysis requests.
  input:
    data_source: string
    analysis_type: string
    format: "summary" | "detailed"
  output:
    report: string (formatted report)
    metadata: object (analysis details)
```

**Best practices:**

- Document what operations are combined
- Consider if granular tools would be better
- Provide progress updates for long operations

## Input Validation

Validate all inputs before processing:

### Schema Validation

Define schemas precisely:

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "minLength": 1,
      "maxLength": 500
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 100,
      "default": 10
    }
  },
  "required": ["query"]
}
```

### Business Logic Validation

Beyond schema, validate business rules:

```python
def validate_search_request(query, path):
    # Schema validation passed, now check business rules
    
    # Ensure path is within allowed directories
    if not is_within_allowed_paths(path):
        raise ValidationError("Path not accessible")
    
    # Check for potentially dangerous patterns
    if contains_injection_attempt(query):
        raise ValidationError("Invalid query pattern")
    
    # Verify user has access
    if not user_can_access(path):
        raise PermissionError("Access denied")
```

## Error Handling

Provide useful error information:

### Error Categories

```
User errors (4xx equivalent):
- Invalid input format
- Missing required fields
- Resource not found
- Permission denied

System errors (5xx equivalent):
- Service unavailable
- Timeout
- Internal failure
```

### Error Response Pattern

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid search query",
    "details": {
      "field": "query",
      "issue": "Query cannot be empty",
      "suggestion": "Provide at least one search term"
    }
  }
}
```

Include:

- Error code for programmatic handling
- Human-readable message
- Actionable details when possible

## Resource Design

### URI Structure

Design consistent, intuitive URIs:

```
Good:
  doc://guides/getting-started
  config://database/connection
  file:///src/main.py

Avoid:
  internal_12345
  resource?type=doc&id=123
```

### Static vs. Dynamic Resources

**Static resources** (content rarely changes):

- Configuration files
- Reference documentation
- Schema definitions

**Dynamic resources** (content changes frequently):

- Live data
- Status information
- Generated content

For dynamic resources, consider:

- Caching strategies
- Freshness indicators
- Subscription/notification patterns

## Performance Considerations

### Response Time

AI interactions expect quick responses:

```
Target response times:
  Simple queries: < 100ms
  Database lookups: < 500ms
  Complex operations: < 2s
  Long operations: Use progress updates
```

### Caching

Cache when appropriate:

```python
# Cache expensive operations
@cache(ttl=300)  # 5 minutes
def get_document(doc_id):
    return fetch_from_storage(doc_id)

# Don't cache user-specific or frequently changing data
def get_user_tickets(user_id):
    return fetch_fresh_from_api(user_id)
```

### Pagination

For large result sets:

```
search_documents:
  input:
    query: string
    page: number (default 1)
    page_size: number (default 20, max 100)
  output:
    results: array
    pagination:
      page: 1
      page_size: 20
      total_results: 150
      has_more: true
```

## Security Best Practices

### Principle of Least Privilege

Expose only what's necessary:

```
✓ Read-only access to documentation
✗ Full database access when only reads are needed
```

### Input Sanitization

Never trust input:

```python
def search(query):
    # Sanitize before using in any system
    sanitized = sanitize_search_query(query)
    
    # Use parameterized queries for databases
    results = db.execute(
        "SELECT * FROM docs WHERE content MATCH ?",
        [sanitized]
    )
```

### Audit Logging

Log significant operations:

```python
def create_ticket(title, description, priority):
    log.info("Creating ticket", extra={
        "action": "create_ticket",
        "user": current_user(),
        "title": title,
        "priority": priority
    })
    
    result = ticket_service.create(...)
    
    log.info("Ticket created", extra={
        "ticket_id": result.id
    })
```

## Testing Your Server

### Unit Tests

Test individual tools:

```python
def test_search_returns_results():
    result = search_tool.execute({"query": "authentication"})
    assert len(result["results"]) > 0
    assert "score" in result["results"][0]

def test_search_validates_input():
    with pytest.raises(ValidationError):
        search_tool.execute({"query": ""})
```

### Integration Tests

Test the full server:

```python
async def test_server_lists_tools():
    async with mcp_client(server) as client:
        tools = await client.list_tools()
        assert "search_docs" in [t.name for t in tools]

async def test_tool_execution():
    async with mcp_client(server) as client:
        result = await client.call_tool("search_docs", {"query": "test"})
        assert result.content is not None
```

### Manual Testing

Test with actual AI clients:

1. Connect your server to an AI assistant
2. Try various queries and edge cases
3. Verify responses are useful and accurate
4. Check error handling

## Key Takeaways

- Design the interface before implementing
- Write descriptions that help AI understand when to use tools
- Validate inputs thoroughly
- Provide useful error messages
- Consider performance and caching
- Follow security best practices
- Test at unit, integration, and user experience levels
