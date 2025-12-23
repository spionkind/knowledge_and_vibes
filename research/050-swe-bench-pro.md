# SWE-Bench Pro 2025

**Paper:** SWE-Bench Pro: A More Realistic Benchmark for AI Software Engineering
**URL:** https://arxiv.org/abs/2501.xxxxx (2025)
**Date:** 2025

---

## Summary

SWE-Bench Pro is a more realistic benchmark that addresses contamination and unrealistic task selection issues in original SWE-Bench.

**Key findings:**
- Best models (GPT-5, Claude Opus 4.1) solve only **~23%** of realistic tasks
- This is a dramatic drop from inflated scores on contaminated benchmarks
- Tasks require multi-file changes, realistic context retrieval, and genuine problem-solving

**Why the drop:**
1. No data contamination (fresh tasks post-training cutoff)
2. Realistic task complexity (not cherry-picked easy cases)
3. Multi-file changes required (not single-function patches)
4. Context retrieval challenges (models must find relevant code)

---

## Practical Implications

1. **Don't assume AI will succeed** — ~77% of tasks will fail even with best models
2. **Human verification is essential** — Cannot trust AI output without review
3. **Plan for failures** — Build escalation paths, spike beads, iteration caps
4. **Tests are non-negotiable** — Only way to catch the 77% failure rate

### For Knowledge & Vibes

This paper justifies:
- P14 Human Verification Gate (operator sign-off required)
- Conservative expectations throughout the workflow
- Strong emphasis on tests and verification
- Iteration caps (don't waste time on likely failures)

---

## Key Quote

> "The gap between benchmark performance and real-world performance is larger than the field anticipated. Realistic evaluation reveals fundamental limitations in current approaches."

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P12 Release Readiness | Add reality check: ~23% success rate |
| P14 Human Verification | Justified by this evidence |
| P9 Execution Loop | Iteration caps prevent wasted effort |
