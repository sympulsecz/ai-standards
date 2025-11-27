# Evaluation

Evaluating AI systems is different from traditional testing. Outputs are variable, correctness is often subjective, and edge cases are hard to anticipate. This guide covers practical approaches to AI evaluation.

## Why Evaluation Matters

Without systematic evaluation:
- You don't know if changes improve or degrade quality
- Problems reach users before you notice them
- Optimization is guesswork
- Regression goes undetected

## Evaluation Types

### Offline Evaluation

Test against prepared datasets before deployment:

```
Test Dataset → System → Outputs → Comparison → Metrics
```

**Pros:**
- Controlled, reproducible
- Can test many cases quickly
- Catches regressions

**Cons:**
- May not reflect real usage
- Limited by dataset quality
- Can be gamed

### Online Evaluation

Measure in production with real users:

```
Real Traffic → System → User Behavior → Metrics
```

**Pros:**
- Real-world performance
- Catches issues offline evaluation misses
- Measures actual impact

**Cons:**
- Users experience problems
- Slower feedback loop
- Harder to attribute causes

### Human Evaluation

People assess quality:

```
Outputs → Human Reviewers → Quality Ratings
```

**Pros:**
- Captures subjective quality
- Can assess nuance
- Ground truth for training automated evals

**Cons:**
- Expensive, slow
- Requires clear guidelines
- Inter-rater variability

## Building Test Sets

### What to Include

A good test set covers:

- **Common cases**: Typical usage patterns
- **Edge cases**: Unusual but valid inputs
- **Failure cases**: Inputs that should be rejected/handled specially
- **Adversarial cases**: Inputs designed to break the system

### Test Case Structure

```python
test_case = {
    "id": "unique-identifier",
    "input": "User question or input",
    "expected": "Expected output or criteria",
    "category": "categorization for analysis",
    "metadata": {
        "difficulty": "easy|medium|hard",
        "source": "where this case came from"
    }
}
```

### Collecting Test Cases

Sources for test cases:
- Real user queries (anonymized)
- Generated examples
- Expert-created cases
- Production failures
- Competitor analysis

### Maintaining Test Sets

Test sets need maintenance:
- Add cases for new failure modes
- Remove outdated cases
- Balance across categories
- Update expected outputs when requirements change

## Evaluation Metrics

### Exact Match Metrics

When there's a clearly correct answer:

```python
def exact_match(predicted, expected):
    return predicted.strip().lower() == expected.strip().lower()

def f1_score(predicted_tokens, expected_tokens):
    # Precision: how many predicted tokens are correct
    # Recall: how many expected tokens were predicted
    # F1: harmonic mean
    ...
```

Use for: Classification, extraction, factual Q&A

### Semantic Similarity

When meaning matters more than exact wording:

```python
def semantic_similarity(text1, text2):
    emb1 = embedding_model.encode(text1)
    emb2 = embedding_model.encode(text2)
    return cosine_similarity(emb1, emb2)
```

Use for: Summarization, paraphrase, open-ended generation

### LLM-as-Judge

Use an LLM to evaluate outputs:

```python
evaluation_prompt = """
Evaluate the following response for quality.

Question: {question}
Response: {response}

Rate on a scale of 1-5:
- Relevance: Does it answer the question?
- Accuracy: Is the information correct?
- Completeness: Does it cover all aspects?
- Clarity: Is it well-written?

Return JSON with ratings and brief explanations.
"""
```

**Considerations:**
- Judges can be biased (prefer verbose, prefer their own style)
- Different judges give different scores
- Need to calibrate against human judgment
- Cost of evaluation scales with test size

### Task-Specific Metrics

Design metrics for your specific use case:

| Task | Metrics |
|------|---------|
| Summarization | ROUGE scores, compression ratio, key fact coverage |
| Translation | BLEU, chrF, human adequacy/fluency |
| Code generation | Pass rate, syntax validity, test passage |
| Classification | Accuracy, precision, recall, F1 per class |
| Extraction | Field accuracy, completeness, spurious extractions |

## Running Evaluations

### Baseline Comparison

Always compare against something:

```
Options:
- Previous version (regression testing)
- Simple baseline (keyword matching, rule-based)
- Human performance
- Competitor systems
```

### Statistical Significance

With variable outputs, ensure differences are meaningful:

- Run multiple times (same model can give different results)
- Use confidence intervals
- Consider effect size, not just statistical significance

### Evaluation Pipeline

```python
def run_evaluation(test_set, system):
    results = []
    for case in test_set:
        output = system.process(case["input"])
        score = evaluate(output, case["expected"])
        results.append({
            "case_id": case["id"],
            "output": output,
            "score": score
        })
    
    return aggregate_results(results)
```

### Tracking Over Time

Track metrics across versions:

```
Version 1.0: Accuracy 78%, Latency 230ms
Version 1.1: Accuracy 82%, Latency 245ms  (+4% accuracy, +15ms latency)
Version 1.2: Accuracy 81%, Latency 180ms  (-1% accuracy, -65ms latency)
```

## Evaluation Challenges

### Subjectivity

Many AI outputs have no single correct answer:

**Mitigations:**
- Multiple human raters
- Clear evaluation criteria
- Accept range of good answers
- Focus on ranking rather than absolute scores

### Dataset Contamination

Models may have seen your test data during training:

**Mitigations:**
- Use recent, private data
- Create synthetic test cases
- Regularly refresh test sets
- Track performance on fresh vs. old cases

### Metric Gaming

Optimizing for metrics may not improve real quality:

**Mitigations:**
- Use multiple metrics
- Include human evaluation
- Monitor user satisfaction
- Regularly review metric validity

### Coverage

Test sets can't cover everything:

**Mitigations:**
- Stratified sampling across categories
- Continuous expansion of test sets
- Production monitoring
- User feedback loops

## Practical Workflow

### Before Changes

1. Run evaluation on current version (baseline)
2. Note current metrics

### During Development

1. Make changes
2. Run quick evaluation subset
3. Iterate until promising

### Before Deployment

1. Run full evaluation
2. Compare to baseline
3. Check for regressions in any category
4. Human review of sample outputs

### After Deployment

1. Monitor production metrics
2. Collect feedback
3. Add failures to test set
4. Periodic re-evaluation

## Key Takeaways

- Evaluation is essential for improving AI systems
- Build representative test sets and maintain them
- Use multiple metrics to capture different quality aspects
- Compare against baselines to understand impact
- Combine offline evaluation with production monitoring
- Expect subjectivity and design for it

