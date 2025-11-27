# Key Concepts

Understanding these foundational concepts will help you work effectively with any AI system.

## How Language Models Work

### Tokens and Context Windows

Language models process text as **tokens**—chunks of text that might be words, parts of words, or punctuation. When you interact with an AI:

1. Your input is converted to tokens
2. The model processes these tokens
3. It generates output tokens one at a time

The **context window** is the total amount of tokens a model can process at once—including both your input and its output. Think of it as the model's "working memory."

!!! tip "Practical Implication"
    Larger context windows allow you to provide more code, documentation, or examples. But more context isn't always better—relevance matters more than volume.

### Probabilistic Generation

Models generate text by predicting the most likely next token, then the next, and so on. This means:

- Outputs are **non-deterministic**: the same prompt may produce different results
- The model doesn't "know" things—it predicts plausible continuations
- Confidence varies: some outputs are highly likely, others are educated guesses

### Training and Knowledge Cutoff

Models learn patterns from training data. They have a **knowledge cutoff**—a date after which they have no information. They also may have varying depth of knowledge about different topics based on what was in their training data.

## Mental Models for AI Interaction

### The Knowledgeable but Literal Assistant

AI is like a very knowledgeable assistant who takes instructions literally. It:

- Has broad knowledge but may lack specific context about your situation
- Does exactly what you ask (which may not be what you meant)
- Doesn't ask clarifying questions unless prompted to
- Won't push back on bad ideas unless you ask it to review critically

### The Pattern Matcher

AI excels at recognizing and applying patterns. It works well when:

- The problem resembles patterns in its training data
- You provide clear examples of what you want
- The task has well-established conventions

It struggles when:

- The problem is truly novel
- Requirements are ambiguous
- The solution requires reasoning about things not in the context

### The Confident Generator

AI generates text confidently regardless of accuracy. It will:

- Produce plausible-sounding but incorrect information
- Make up details when it doesn't have information
- Not distinguish between high-confidence and low-confidence outputs

!!! warning "Verification is Essential"
    Never assume AI output is correct. Always verify, especially for:

    - API usage and library behavior
    - Security-sensitive code
    - Business logic
    - Anything you can't easily test

## Key Terms

| Term | Meaning |
|------|---------|
| **Prompt** | The input you provide to an AI system |
| **Completion** | The AI's generated response |
| **Context** | All information available to the model for generating a response |
| **Hallucination** | When an AI generates plausible but false information |
| **Temperature** | A parameter controlling randomness in outputs (higher = more varied) |
| **System prompt** | Instructions that set the AI's behavior for a conversation |
| **Few-shot learning** | Providing examples in your prompt to guide the output format |

## Context Management

One of the most important skills in working with AI is managing context effectively.

### What Goes in Context

- **Relevant code**: Files, functions, or snippets the AI needs to understand
- **Requirements**: What you're trying to achieve
- **Constraints**: Limitations, style guides, or requirements
- **Examples**: Sample inputs/outputs or similar code

### Context Quality Principles

1. **Relevance over volume**: 10 relevant lines beat 1000 tangential ones
2. **Explicit over implicit**: State assumptions; the AI can't read your mind
3. **Structured over scattered**: Organize information clearly
4. **Current over stale**: Ensure context reflects the actual state of your code

### Context Pollution

Too much irrelevant context can degrade output quality. Signs of context pollution:

- AI references code that isn't relevant
- Outputs mix patterns from different parts of the codebase
- Responses become less focused

## The Feedback Loop

Effective AI use is iterative:

```
┌─────────────────────────────────────────────┐
│                                             │
│   Prompt ──► Response ──► Evaluate ──┐      │
│      ▲                               │      │
│      └───────── Refine ◄─────────────┘      │
│                                             │
└─────────────────────────────────────────────┘
```

1. **Prompt**: Provide context and instructions
2. **Response**: AI generates output
3. **Evaluate**: Assess quality and correctness
4. **Refine**: Adjust your prompt or provide feedback

The skill is in making this loop efficient—getting good results with fewer iterations.

## Key Takeaways

- AI systems are probabilistic pattern matchers, not reasoning engines
- Context quality determines output quality
- Verification is always necessary
- Working with AI is an iterative, refinable skill
- Understanding the underlying mechanics helps you debug and improve interactions
