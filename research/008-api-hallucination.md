# API Hallucination and Documentation Augmented Generation

**Paper:** On Mitigating Code LLM Hallucinations with API Documentation
**URL:** https://arxiv.org/abs/2407.09726
**Date:** July 2024

---

## Summary

Code LLMs hallucinate APIs, especially **low-frequency APIs** (rarely seen in training). GPT-4o achieves only 38.58% valid invocations for low-frequency cloud APIs. Documentation augmentation helps but can hurt high-frequency APIs.

**CloudAPIBench:** 622 tasks testing AWS/Azure API invocations, categorized by frequency:
- Low frequency: 0-10 occurrences in training data
- Medium: 11-100
- High: ≥101

**Base model performance:**

| API Frequency | StarCoder2-15B | GPT-4o |
|---------------|----------------|--------|
| High | 88.78% | 93.66% |
| Low | 24.72% | 38.58% |

**The problem:** LLMs make up non-existent APIs, use wrong syntax, or hallucinate arguments for APIs they rarely saw during training.

---

## Documentation Augmented Generation (DAG)

**The approach:**
1. Model generates initial API invocation attempt
2. Use that as query to retrieve matching docs
3. Re-generate with docs in context

**DAG results:**
- Low-frequency APIs: 41.80% → 86.82% (huge improvement)
- High-frequency APIs: Can DROP up to 39.02% (docs distract from known APIs)

**DAG++ (smart retrieval):**
- Only trigger retrieval when: API doesn't exist in index OR confidence is low
- Result: +8.20% overall improvement without hurting high-frequency

---

## Practical Implications

1. **Low-frequency APIs are the problem** - Common APIs work fine; rare ones don't
2. **Documentation retrieval helps for rare APIs** - But must be selective
3. **Confidence is calibrated** - LLM probability over API tokens indicates when to trust it
4. **Over-retrieval hurts** - Adding docs for well-known APIs degrades performance

**For your system:**
- The external-docs skill should be selective, not always-on
- Check if the API is "well-known" before fetching docs
- The confidence heuristic: if the model seems sure, maybe trust it
- For rare/new APIs, grounding is essential

**Triggers for doc retrieval:**
- API doesn't exist in known index
- Low confidence in API invocation
- User explicitly says "use X library version Y"
- Domain-specific/cloud-specific APIs (AWS, Azure, GCP)

**Skip doc retrieval for:**
- Standard library (os, json, datetime)
- Extremely common APIs (requests.get, pandas.DataFrame)
- When model shows high confidence
