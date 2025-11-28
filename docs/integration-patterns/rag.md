# RAG (Retrieval-Augmented Generation)

RAG enhances LLM responses by retrieving relevant information and including it in the prompt, allowing LLMs to answer questions about data they weren't trained on.

## Why RAG?

RAG addresses LLM limitations (knowledge cutoff, no private data access, hallucination, limited context) by providing current information, grounding responses in actual data, and focusing context on relevant information.

## Architecture

The RAG pipeline flows: Query → Retrieval → Context Assembly → LLM → Response. Retrieved documents come from a vector database containing embedded versions of source documents.

## Core Components

### Document Processing

Source documents are transformed through parsing (extract text), chunking (split into pieces), embedding (convert to vectors), and indexing (store for retrieval).

### Chunking Strategies

| Strategy | Characteristics | Trade-offs |
|----------|----------------|------------|
| **Fixed-size** | Split every N tokens | Simple and predictable, may split mid-concept |
| **Semantic** | Split at natural boundaries | Preserves meaning, variable sizes |
| **Overlapping** | Chunks overlap by percentage | Helps with context at boundaries, increases storage |
| **Hierarchical** | Multiple levels (doc → section → paragraph) | Different granularity retrieval, more complex |

!!! tip "Chunk Size Trade-off"
    Smaller chunks enable precise retrieval but may miss context. Larger chunks provide more context but may include irrelevant information. Start with 200-500 tokens and adjust based on results.

### Embeddings

Embeddings convert text to high-dimensional vectors for similarity search. Use the same embedding model for both indexing and querying, match the model to your content type, and consider multilingual needs if applicable.

### Vector Storage

Vector databases store embeddings and support similarity search (nearest neighbors) and filtered search (similarity + metadata filters). Options range from simple in-memory solutions for development to dedicated vector databases for production.

### Retrieval Strategies

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Simple similarity** | Return top-k most similar | Basic use cases |
| **Filtered** | Add metadata filters (date, source, etc.) | When you need scoping |
| **Hybrid** | Combine semantic + keyword search | Improves recall |
| **Reranking** | Retrieve more, then rerank with another model | Maximize precision |

### Context Assembly

Combine retrieved documents into a prompt that instructs the LLM to answer based only on provided context and to acknowledge when information is insufficient.

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

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Basic RAG** | Query → Retrieve → Generate | Straightforward Q&A |
| **Query Enhancement** | Expand/rewrite query before retrieval | Improve retrieval quality |
| **Iterative RAG** | Multiple retrieval rounds based on need | Complex questions requiring multiple sources |
| **Agentic RAG** | Agent decides retrieval strategy | Dynamic scenarios with multiple sources |

## Quality Factors

### Retrieval Quality

The most critical factor in RAG systems. Bad retrieval produces bad responses regardless of LLM quality. Measure whether relevant documents are retrieved, irrelevant ones filtered out, and ranking is correct. Improve through better chunking strategies, query enhancement, hybrid search, or reranking.

### Context Utilization

Ensure the LLM uses retrieved context effectively through clear instructions, source attribution requirements, and structured context presentation. Watch for problems like ignoring relevant context or mixing up information from multiple sources.

### Hallucination Prevention

RAG reduces but doesn't eliminate hallucination. Strategies include instructing to use only provided context, requiring source citations, verifying claims against context, and using lower temperature settings.

## Implementation Considerations

### Indexing Pipeline

Consider how often source data changes, whether to use incremental or full reindex, how to parallelize processing, and how to handle malformed documents.

### Query Pipeline

Balance latency budget against quality, identify caching opportunities (embeddings, frequent queries), define fallback strategies for retrieval failures, and manage costs from embedding and LLM calls.

### Maintenance

RAG systems require ongoing work: reindex when sources change, monitor retrieval quality metrics, update embeddings when better models become available, and handle growing data volumes.

## Evaluation

| Metric | What It Measures |
|--------|------------------|
| **Retrieval precision** | Are retrieved docs relevant? |
| **Retrieval recall** | Are all relevant docs retrieved? |
| **Answer relevance** | Does the answer address the question? |
| **Faithfulness** | Is the answer supported by context? |
| **Answer completeness** | Does it cover all aspects? |

## Key Takeaways

RAG grounds LLM responses in actual data through a retrieval pipeline. Chunking strategy significantly impacts quality, and retrieval quality is the foundation of a successful RAG system. Start simple with basic retrieval and add complexity based on evaluation results. Monitor and maintain the system over time as data and requirements evolve.
