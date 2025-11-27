# API Patterns

Reliable LLM API integration requires handling the unique characteristics of LLM services: variability, latency, rate limits, and costs.

## Request Patterns

### Basic Request Structure

Most LLM APIs follow a similar pattern:

```python
response = client.chat.completions.create(
    model="model-name",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "User's question here"}
    ],
    temperature=0.7,
    max_tokens=500
)
```

Key parameters:
- **model**: Which model to use
- **messages**: Conversation history
- **temperature**: Randomness (0 = deterministic, 1+ = creative)
- **max_tokens**: Maximum response length

### System Prompts

System prompts set behavior for the conversation:

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

**Best practices:**
- Define the role clearly
- Specify constraints and style
- Include examples of desired behavior
- Keep focused (don't overload with instructions)

### Structured Outputs

Request specific output formats for reliable parsing:

```python
response = client.chat.completions.create(
    model="model-name",
    messages=[...],
    response_format={"type": "json_object"}
)
```

Or via prompt instructions:

```python
system_prompt = """Respond with JSON in this format:
{
  "summary": "brief summary",
  "sentiment": "positive" | "negative" | "neutral",
  "confidence": 0.0-1.0
}"""
```

**Best practices:**
- Validate output against expected schema
- Have fallback for malformed responses
- Include examples in prompt for complex formats

### Function Calling / Tool Use

Define functions the model can call:

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_database",
            "description": "Search the product database",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "limit": {"type": "integer", "default": 10}
                },
                "required": ["query"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="model-name",
    messages=[...],
    tools=tools
)
```

The model returns function calls, your code executes them.

## Error Handling

### Common Errors

| Error Type | Cause | Response |
|------------|-------|----------|
| Rate limit | Too many requests | Backoff and retry |
| Timeout | Request took too long | Retry with shorter prompt |
| Invalid request | Bad parameters | Fix and retry |
| Content filter | Flagged content | Handle gracefully |
| Server error | Provider issues | Retry with backoff |

### Retry Strategy

Implement exponential backoff:

```python
def call_with_retry(func, max_retries=3, base_delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
```

### Timeout Handling

Set appropriate timeouts:

```python
response = client.chat.completions.create(
    ...,
    timeout=30.0  # seconds
)
```

Consider:
- Shorter timeouts for interactive use
- Longer timeouts for batch processing
- Timeout per token for streaming

### Graceful Degradation

When LLM fails, have fallbacks:

```python
try:
    response = get_ai_response(query)
except LLMError:
    # Fallback to simpler approach
    response = get_keyword_response(query)
    log.warning("LLM unavailable, using fallback")
```

## Streaming

For long responses, stream tokens as they're generated:

```python
stream = client.chat.completions.create(
    model="model-name",
    messages=[...],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

Benefits:
- Better perceived latency
- Can show progress
- Can cancel early if response is wrong

Considerations:
- More complex error handling
- Need to reassemble full response
- May need different parsing approach

## Cost Management

### Token Awareness

Understand token usage:

```python
response = client.chat.completions.create(...)

usage = response.usage
print(f"Input: {usage.prompt_tokens}")
print(f"Output: {usage.completion_tokens}")
print(f"Total: {usage.total_tokens}")
```

### Cost Reduction Strategies

**Prompt optimization:**
- Remove unnecessary context
- Use concise instructions
- Avoid repetition

**Model selection:**
- Use smaller models when appropriate
- Reserve large models for complex tasks

**Caching:**
```python
def get_completion(prompt):
    cache_key = hash(prompt)
    if cache_key in cache:
        return cache[cache_key]
    
    response = call_llm(prompt)
    cache[cache_key] = response
    return response
```

**Batching:**
- Process multiple items in one request
- Reduces per-request overhead

### Budget Controls

Implement spending limits:

```python
class CostTracker:
    def __init__(self, daily_limit):
        self.daily_limit = daily_limit
        self.daily_spend = 0
    
    def can_request(self, estimated_tokens):
        estimated_cost = self.estimate_cost(estimated_tokens)
        return self.daily_spend + estimated_cost <= self.daily_limit
    
    def record_usage(self, usage):
        self.daily_spend += self.calculate_cost(usage)
```

## Observability

### Logging

Log for debugging and monitoring:

```python
def call_llm(messages, **kwargs):
    request_id = generate_id()
    
    log.info("LLM request", extra={
        "request_id": request_id,
        "model": kwargs.get("model"),
        "message_count": len(messages),
        "max_tokens": kwargs.get("max_tokens")
    })
    
    start = time.time()
    response = client.chat.completions.create(messages=messages, **kwargs)
    duration = time.time() - start
    
    log.info("LLM response", extra={
        "request_id": request_id,
        "duration_ms": duration * 1000,
        "tokens_used": response.usage.total_tokens,
        "finish_reason": response.choices[0].finish_reason
    })
    
    return response
```

### Metrics

Track operational metrics:
- Request latency (p50, p95, p99)
- Error rate by type
- Token usage over time
- Cost per request/user/feature

### Tracing

For complex pipelines, use distributed tracing:
- Trace ID across LLM calls
- Parent-child relationships
- Timing for each step

## Provider Abstraction

Abstract provider specifics for flexibility:

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

Benefits:
- Switch providers easily
- A/B test different models
- Fallback between providers

## Key Takeaways

- Structure prompts consistently (system, user, assistant roles)
- Handle errors gracefully with retries and fallbacks
- Use streaming for better user experience
- Monitor costs and set budget limits
- Log thoroughly for debugging
- Abstract providers for flexibility

