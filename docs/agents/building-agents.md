# Building Agents

Building your own agent system means integrating with LLM APIs, designing tools the agent can use, and handling the unique challenges of autonomous systems. This guide covers practical patterns for creating reliable agents from scratch.

!!! tip "Start Simple"
    Begin with minimal agency and add complexity only when needed. Many tasks that seem to require autonomous agents can be solved with simpler approaches like structured prompts or fixed workflows.

Before building an agent, ask: Could a simple prompt solve this? Could a fixed sequence of steps work? Do I really need autonomous decision-making?

## Working with LLM APIs

Agent systems interact with LLMs through APIs. Understanding API patterns helps you build reliable, cost-effective agents.

### Request Structure

Most LLM APIs follow a common pattern:

**Messages**: Conversation history including system prompts, user messages, and assistant responses.

**Model selection**: Choose based on task complexity—smaller models for simple tasks, larger models for complex reasoning.

**Parameters**: Control behavior through temperature (randomness), max_tokens (response length), and top_p (nucleus sampling).

### Anatomy of a Prompt

LLM APIs structure conversations as an array of messages, each with a role and content:

```python
messages = [
    {
        "role": "system",
        "content": "You are a code review assistant..."
    },
    {
        "role": "user",
        "content": "Review this function for security issues:\n[code]"
    },
    {
        "role": "assistant",
        "content": "I found these potential issues..."
    },
    {
        "role": "user",
        "content": "Fix the SQL injection vulnerability"
    }
]
```

**System role**: Sets behavior, constraints, and capabilities for the entire conversation. The agent doesn't "see" this as a user message—it's more like configuration. Only appears once at the start.

**User role**: Represents input from the human or system calling the agent. Contains questions, requests, or context.

**Assistant role**: The LLM's previous responses. Including prior assistant messages maintains conversation context and helps the model understand what it said before.

The LLM generates the next assistant message based on the complete message history. This structure allows agents to maintain context, reference previous decisions, and have coherent multi-turn conversations.

### System Prompts

System prompts define agent behavior for the entire conversation. They should clearly define the role, specify constraints and style, and remain focused without overloading instructions.

```python
system_prompt = """You are a customer service agent that helps resolve user issues.

Your role:
- Verify user identity before accessing sensitive information
- Search orders, process refunds, send emails
- Escalate complex cases to human agents

Guidelines:
- Be helpful but don't make promises you can't keep
- Refunds over $100 require escalation
- Always explain your reasoning before acting

Available tools:
- search_orders(user_id)
- process_refund(order_id, amount, reason)
- send_email(to, subject, body)
- escalate_to_human(summary)
"""
```

### Structured Outputs

Agents often need to return data in specific formats. Request structured outputs using JSON schemas:

```python
response_format = {
    "type": "object",
    "properties": {
        "reasoning": {"type": "string"},
        "action": {"type": "string", "enum": ["search", "refund", "email", "escalate"]},
        "parameters": {"type": "object"}
    },
    "required": ["reasoning", "action", "parameters"]
}
```

Always validate output against expected schemas and have fallbacks for malformed responses.

### Function Calling

Many LLM APIs support function calling, where the model can invoke predefined functions. Define functions with clear descriptions, parameter schemas, and required fields:

```python
functions = [
    {
        "name": "search_orders",
        "description": "Search for customer orders by user ID or email",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string", "description": "Customer user ID"},
                "status": {"type": "string", "enum": ["pending", "shipped", "delivered"]}
            },
            "required": ["user_id"]
        }
    }
]
```

The model returns function calls which your code executes, then returns results to the model to continue reasoning.

## Error Handling and Resilience

LLM APIs introduce unique failure modes that agents must handle gracefully.

### Common Error Types

| Error Type | Cause | Response Strategy |
|------------|-------|-------------------|
| Rate limit | Too many requests | Exponential backoff and retry |
| Timeout | Request too long | Retry with shorter prompt/context |
| Invalid request | Bad parameters | Fix and retry once |
| Content filter | Flagged content | Handle gracefully, log, inform user |
| Server error | Provider issues | Retry with backoff |

Implement exponential backoff for transient errors. Stop retrying after a maximum number of attempts and set appropriate timeouts based on use case (shorter for interactive, longer for batch).

## Managing Context

Agents need context to make good decisions, but context windows are limited.

### What to Include

- **Goal**: What the agent is trying to accomplish
- **Current state**: What has happened so far
- **Available tools**: What actions are possible
- **Constraints**: Limits on behavior
- **Examples**: How to handle similar situations

### Context Window Management

As agents work, context grows. Strategies for managing this:

**Summarization**: Periodically summarize history

```
Previous actions:
- Searched for user (found ID: 12345)
- Retrieved order history (3 orders)
- Identified refund request for ORD-789

[detailed logs available if needed]
```

**Relevance filtering**: Include only relevant history

```
Relevant context for this step:
- User ID: 12345
- Current task: Process refund
- Order ID: ORD-789 (damaged item)
- Refund amount: $45
```

**Chunking**: Break long operations into phases with fresh context between phases.

## Cost Management

LLM API calls have measurable costs. Track and control spending.

### Token Awareness

Track usage from response metadata:

```python
response = llm.complete(messages)
usage = response.usage
# usage.prompt_tokens, usage.completion_tokens, usage.total_tokens
```

### Cost Reduction Strategies

| Strategy | Approach |
|----------|----------|
| **Prompt optimization** | Remove unnecessary context, use concise instructions |
| **Model selection** | Use smaller models for simple tasks, large models for complexity |
| **Caching** | Cache identical or similar prompts, invalidate based on TTL |
| **Batching** | Process multiple items in one request to reduce overhead |

### Budget Controls

Implement spending limits:

- Track daily/monthly usage
- Estimate costs before requests
- Reject requests that would exceed limits
- Alert when approaching limits

## Observability

Make agent behavior observable through logging and metrics. Log reasoning/thought process, tool selections with rationale, inputs/outputs, and state changes at each step. Use structured logging with request IDs to enable tracing across operations.

Track key metrics: latency (p50, p95, p99), error rates by type, token usage, cost per request, and quality metrics like task completion rate. For complex workflows, implement distributed tracing with unique trace IDs per task and parent-child relationships for nested operations.

## Testing Agents

Agents don't behave like traditional software—the same input can yield different outputs, and there's often more than one "correct" solution. You need testing strategies that work with this variability while catching real problems.

### Test for Outcomes, Not Exact Outputs

Check whether the agent achieves its goal, not whether it follows a specific path. If you ask an agent to refactor code, verify the refactored code works correctly—don't expect character-for-character identical results across runs. For a customer service agent, verify the issue gets resolved, not that it uses specific phrasing.

### Define Hard Boundaries

Some things must never happen. Test for violations rather than prescribing exact behavior: agents should never expose sensitive data, never execute dangerous operations without confirmation, never violate defined constraints. These boundaries are deterministic even when the agent's approach isn't.

### Run Scenarios Multiple Times

Execute the same test scenario 5-10 times and measure consistency. If your agent succeeds 9/10 times, that's measurable reliability. Track success rates, common failure modes, and where performance varies. This statistical approach surfaces real issues while accepting inherent variability.

### Build a Golden Set

Maintain a curated collection of representative scenarios with known-good characteristics. While exact outputs vary, successful runs share verifiable properties: retrieved the right data, invoked appropriate tools, respected constraints, achieved the goal. These become your regression suite.

### Cover Different Failure Modes

Test happy paths where everything works, error conditions like API failures and rate limits, edge cases with empty results or malformed inputs, and adversarial attempts to bypass constraints or jailbreak guardrails.

### Track Meaningful Metrics

Measure task completion rate (achieving the goal), step efficiency (optimal vs wasteful paths), error and recovery rates (how often it fails and bounces back), and cost per task (token usage, API calls). These metrics tell you if the agent is improving or degrading.

### Maintain Regression Tests

As you modify the agent, run your test suite to ensure changes don't break existing capabilities. Track metrics over time to detect degradation early, and review failures to identify patterns in what breaks.

## Building and Extending Agents with Tools

Agents become more powerful when connected to external systems and data sources. Tools are the actions your agent can take—good tool design is crucial for agent capability.

### Tool Design Principles

**Clear, specific names:**

```
✓ search_documentation
✓ get_user_by_email
✓ create_github_issue

✗ do_thing
✗ helper
✗ process
```

**Explicit parameters:**

```
✓ send_email(to: string, subject: string, body: string)
✗ send_email(data: object)
```

**Predictable behavior:**

- Same inputs should produce same outputs
- Side effects should be documented
- Errors should be clear and actionable

### Tool Descriptions

The agent needs to understand what tools do. Write descriptions that explain what the tool does, when to use it, what parameters mean, what it returns, and common errors:

```
search_documentation:
  description: |
    Search the technical documentation for relevant information.
    Use this when you need to find API details, configuration options,
    or implementation guidance. Returns relevant excerpts with source links.
  parameters:
    query: The search query (be specific for better results)
    limit: Maximum number of results (default: 5)
  returns: Array of {content, source_url, relevance_score}
  errors:
    - "No results found" - try rephrasing the query
    - "Rate limited" - wait and retry
```

### Tool Granularity

Find the right level of abstraction. Too granular forces agents to manage low-level orchestration (like `click_button()`, `type_text()`). Too coarse removes flexibility (like `do_entire_workflow()`). The right level provides meaningful operations that compose well: `fill_form(form_id, field_values)`, `submit_form(form_id)`, `verify_submission_success()`.

### Extending with MCP

The Model Context Protocol (MCP) provides a standardized way to extend agents with custom capabilities—connecting them to databases, APIs, internal systems, and more. MCP servers expose tools, resources, and prompts that work across different agent systems.

For implementation patterns, security considerations, and examples of building MCP servers, see [MCP (Model Context Protocol)](mcp.md).

## Key Takeaways

- Start simple; add complexity only when needed
- Structure API interactions with clear system prompts and error handling
- Manage context carefully as it grows
- Track and control API costs through optimization and limits
- Design tools with clear names, explicit parameters, and proper granularity
- Make agent behavior observable through logging and metrics
- Test for outcomes, define hard boundaries, and run scenarios multiple times
- Use MCP to extend agents with standardized custom capabilities

## Related Reading

- [Working with Agents](working-with-agents.md) - Understanding how agents work
- [MCP (Model Context Protocol)](mcp.md) - Extending agents with custom capabilities
