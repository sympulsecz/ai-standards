# API Patterns

Reliable LLM API integration requires handling unique characteristics: variability, latency, rate limits, and costs.

## Request Structure

Most LLM APIs follow a common pattern with messages (conversation history), model selection, and parameters controlling behavior (temperature for randomness, max_tokens for length).

### System Prompts

System prompts define behavior for the entire conversation. They should clearly define the role, specify constraints and style, and remain focused without overloading instructions.

```python
system_prompt = """You are a technical documentation assistant.

Your role:
- Answer questions about the codebase
- Provide code examples when helpful
- Admit when you don't know something

Style:
- Be concise and direct
- Use code blocks for code
- Reference specific files when applicable
"""
```

### Structured Outputs

Request specific output formats using `response_format` parameters or prompt instructions specifying JSON schemas. Always validate output against expected schemas and have fallbacks for malformed responses.

### Function Calling

Define functions the model can call with clear descriptions, parameter schemas, and required fields. The model returns function calls which your code then executes.

## Error Handling

| Error Type | Cause | Response Strategy |
|------------|-------|-------------------|
| Rate limit | Too many requests | Backoff and retry |
| Timeout | Request too long | Retry with shorter prompt |
| Invalid request | Bad parameters | Fix and retry |
| Content filter | Flagged content | Handle gracefully |
| Server error | Provider issues | Retry with backoff |

### Retry Strategy

Implement exponential backoff for transient errors. Stop retrying after a maximum number of attempts and set appropriate timeouts based on use case (shorter for interactive, longer for batch).

### Graceful Degradation

When LLM fails, use fallback strategies such as simpler approaches, cached responses, or error messages. Log warnings when using fallbacks.

## Streaming

Stream tokens for long responses to improve perceived latency and allow showing progress. Streaming requires more complex error handling and response reassembly but enables canceling early if the response goes off track.

## Cost Management

### Token Awareness

Track usage from response metadata (prompt tokens, completion tokens, total tokens) to understand and control costs.

### Cost Reduction Strategies

| Strategy | Approach |
|----------|----------|
| **Prompt optimization** | Remove unnecessary context, use concise instructions, avoid repetition |
| **Model selection** | Use smaller models for simple tasks, reserve large models for complexity |
| **Caching** | Cache identical or similar prompts, invalidate based on TTL or changes |
| **Batching** | Process multiple items in one request to reduce per-request overhead |

### Budget Controls

Implement spending limits by tracking daily/monthly usage, estimating costs before requests, and rejecting requests that would exceed limits.

## Observability

### Logging

Log request metadata (model, message count, parameters), timing information (duration, timestamps), token usage, and completion status. Use structured logging with request IDs for tracing.

### Metrics

| Metric Type | Examples |
|-------------|----------|
| **Latency** | p50, p95, p99 response times |
| **Errors** | Rate by error type |
| **Usage** | Token usage over time, requests per feature |
| **Cost** | Spend per request/user/feature |

### Tracing

For complex pipelines, use distributed tracing with trace IDs across LLM calls, parent-child relationships for nested calls, and timing for each step.

## Provider Abstraction

Abstract provider-specific details to enable switching providers, A/B testing different models, and fallback between providers. Create a common interface that adapts to different provider APIs.

```python
class LLMClient:
    def complete(self, messages, **kwargs):
        raise NotImplementedError

class OpenAIClient(LLMClient):
    def complete(self, messages, **kwargs):
        return self.client.chat.completions.create(
            messages=messages, **kwargs
        )

class AnthropicClient(LLMClient):
    def complete(self, messages, **kwargs):
        # Convert to Anthropic format
        return self.client.messages.create(...)
```

## Key Takeaways

Structure prompts consistently with clear system messages, handle errors gracefully with retries and fallbacks, use streaming for better user experience, monitor and control costs actively, log thoroughly for debugging, and abstract providers for flexibility.
