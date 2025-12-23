# FLAMES (Semantic-Guided Search for Program Repair)

**Paper:** Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation (FLAMES)  
**URL:** https://arxiv.org/abs/2410.16655  
**Date:** Oct 2024  
**Venue:** arXiv preprint

---

## The Core Idea

LLM-based program repair often uses beam search, but large beams:
- explode VRAM usage
- cause OOM failures
- still don’t guarantee correct fixes

FLAMES replaces beam search with:
- **greedy decoding** (beam size 1)
- a **semantic-guided best-first search** that uses test feedback as a reward signal to decide which tokens/branches to explore next

---

## Key Claim

You can get better repair outcomes with far less GPU memory by using **semantic feedback** (tests passing/failing) as the search guide rather than relying on model probability mass from large beams.

---

## Reported Results (Headlines)

The paper reports:
- **Up to ~83% VRAM reduction** vs beam-search APR baselines
- **133** correct fixes on Defects4J in their setup (outperforming prior baselines by ~10 fixes)
- Better performance on related Java benchmarks (e.g., HumanEval-Java) and transformed APR datasets

---

## Why This Matters

It’s evidence for a broader agent principle:
> Execution feedback should steer search, not just be a final check.

And it highlights a systems reality: efficiency constraints (memory/time) change what “best practice” looks like.

---

## Critical Caveats

1. **Depends on test signal quality:** weak tests mislead the reward.
2. **Search-policy engineering:** best-first policies and rewards require tuning.
3. **APR scope:** repo-scale issue resolution adds environment and multi-file complexity.

---

## Relevance to Knowledge & Vibes

### Supports
- Explicit repair loops that prioritize “minimal compute, maximal feedback”.
- Designing workflows that can run on constrained resources (a real-world factor frontier labs optimize heavily).

### Practical implication
When possible, treat tests as an online reward signal and steer exploration adaptively instead of brute-force sampling.

