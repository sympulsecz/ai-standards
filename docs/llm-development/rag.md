# RAG (Retrieval-Augmented Generation)

RAG enhances LLM responses by retrieving relevant information and including it in the prompt. This allows LLMs to answer questions about specific data they weren't trained on.

## Why RAG?

LLMs have limitations:

- Knowledge cutoff (don't know recent information)
- No access to private data
- Can hallucinate facts
- Limited context window

RAG addresses these by:

- Providing current information
- Grounding responses in actual data
- Reducing hallucination
- Focusing context on relevant information

## RAG Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  Query ──► Retrieval ──► Context Assembly ──► LLM ──► Response  │
│               │                  │                               │
│               ▼                  │                               │
│         ┌─────────┐              │                               │
│         │ Vector  │◄─────────────┘                               │
│         │   DB    │  (relevant documents)                        │
│         └─────────┘                                              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## Core Components

### Document Processing

Transform raw documents into retrievable chunks:

```
Source Documents
      │
      ▼
┌─────────────┐
│   Parsing   │  Extract text from files
└─────────────┘
      │
      ▼
┌─────────────┐
│  Chunking   │  Split into manageable pieces
└─────────────┘
      │
      ▼
┌─────────────┐
│  Embedding  │  Convert to vectors
└─────────────┘
      │
      ▼
┌─────────────┐
│  Indexing   │  Store for retrieval
└─────────────┘
```

### Chunking Strategies

How you split documents affects retrieval quality:

**Fixed-size chunks:**
```
Split every N characters/tokens
Simple, predictable
May split mid-sentence or mid-concept
```

**Semantic chunks:**
```
Split at natural boundaries (paragraphs, sections)
Preserves meaning
Variable sizes
```

**Overlapping chunks:**
```
Chunks overlap by some percentage
Helps with context at boundaries
Increases storage
```

**Hierarchical chunks:**
```
Multiple levels (document → section → paragraph)
Enables different granularity retrieval
More complex implementation
```

!!! tip "Chunk Size Trade-off"
    - **Smaller chunks**: More precise retrieval, but may miss context
    - **Larger chunks**: More context, but may include irrelevant information
    
    Start with 200-500 tokens and adjust based on results.

### Embeddings

Convert text to vectors for similarity search:

```python
# Conceptual example
text = "How do I reset my password?"
embedding = embedding_model.encode(text)
# Returns: [0.12, -0.34, 0.56, ...] (hundreds of dimensions)
```

**Considerations:**
- Match embedding model to your content type
- Same model for indexing and querying
- Consider multilingual needs

### Vector Storage

Store embeddings for efficient retrieval:

**Options range from:**
- Simple in-memory (development)
- Dedicated vector databases (production)
- Extensions to existing databases

**Key operations:**
- Insert embeddings
- Similarity search (nearest neighbors)
- Filtered search (similarity + metadata)

### Retrieval

Find relevant documents for a query:

```python
# Conceptual example
def retrieve(query, k=5):
    query_embedding = embed(query)
    results = vector_db.similarity_search(
        embedding=query_embedding,
        k=k
    )
    return results
```

**Retrieval strategies:**

| Strategy | Description |
|----------|-------------|
| Simple similarity | Return top-k most similar |
| Filtered | Add metadata filters (date, source, etc.) |
| Hybrid | Combine semantic + keyword search |
| Reranking | Retrieve more, then rerank with another model |

### Context Assembly

Combine retrieved documents into a prompt:

```python
def build_prompt(query, retrieved_docs):
    context = "\n\n".join([doc.content for doc in retrieved_docs])
    
    return f"""Answer based on the following context:

Context:
{context}

Question: {query}

Answer based only on the context provided. If the context doesn't contain 
the answer, say you don't have enough information."""
```

## Common Patterns

### Basic RAG

```
Query → Retrieve → Generate

Simple, good starting point
Works well for straightforward Q&A
```

### Query Enhancement

Improve retrieval by enhancing the query:

```
Query → Expand/Rewrite → Retrieve → Generate

Examples:
- Add synonyms
- Rewrite for clarity
- Generate multiple query variants
```

### Iterative RAG

Multiple retrieval rounds:

```
Query → Retrieve → Generate → Need more info? → Retrieve again → ...

Useful when initial retrieval isn't sufficient
Adds latency but improves completeness
```

### Agentic RAG

Agent decides retrieval strategy:

```
Query → Agent decides:
         - Which sources to search
         - What queries to run
         - When to stop retrieving
       → Generate
```

## Quality Factors

### Retrieval Quality

The most important factor. Bad retrieval = bad responses.

**Measure:**
- Are relevant documents being retrieved?
- Are irrelevant documents being filtered out?
- Is the ranking correct?

**Improve:**
- Better chunking strategy
- Query enhancement
- Hybrid search
- Reranking

### Context Utilization

Does the LLM use retrieved context effectively?

**Problems:**
- Ignoring relevant context
- Over-relying on weak evidence
- Mixing up information from multiple sources

**Solutions:**
- Clear instructions to use context
- Source attribution requirements
- Structured context presentation

### Hallucination Prevention

RAG reduces but doesn't eliminate hallucination.

**Strategies:**
- Instruct to only use provided context
- Ask for source citations
- Verify claims against context
- Use lower temperature

## Implementation Considerations

### Indexing Pipeline

```
Source Data → Processing → Vector DB

Considerations:
- How often does data change?
- Incremental vs. full reindex
- Processing parallelization
- Error handling for bad documents
```

### Query Pipeline

```
User Query → Enhancement → Retrieval → Assembly → LLM → Response

Considerations:
- Latency budget
- Caching opportunities
- Fallback strategies
- Cost management
```

### Maintenance

RAG systems require ongoing maintenance:

- Reindex when sources change
- Monitor retrieval quality
- Update embeddings when models improve
- Handle growing data volumes

## Evaluation

Evaluate RAG systems on:

| Metric | What It Measures |
|--------|------------------|
| Retrieval precision | Are retrieved docs relevant? |
| Retrieval recall | Are all relevant docs retrieved? |
| Answer relevance | Does the answer address the question? |
| Faithfulness | Is the answer supported by context? |
| Answer completeness | Does it cover all aspects? |

## Key Takeaways

- RAG grounds LLM responses in actual data
- Chunking strategy significantly impacts quality
- Retrieval quality is the foundation—invest here
- Start simple, add complexity based on evaluation
- Monitor and maintain the system over time

