# PlanSearch (Search Over Natural-Language Plans)

**Paper:** Planning In Natural Language Improves LLM Search For Code Generation  
**URL:** https://arxiv.org/html/2409.03733v1  
**Date:** Sep 2024  
**Venue:** arXiv preprint

---

## The Core Idea

Repeated sampling from an LLM often produces near-duplicate wrong solutions → search is inefficient because there’s no diversity.

PlanSearch improves search by **moving the search space up a level**:
- Generate diverse *observations/hints* about the task
- Combine observations into multiple candidate **natural-language plans**
- Generate code conditioned on each plan

So you explore “idea space” rather than “code space”.

---

## Key Results (Headlines)

PlanSearch reports substantial improvements at high-sample regimes:
- On LiveCodeBench with Claude 3.5 Sonnet, reported **pass@200 ~77%** vs repeated sampling ~60% in their setup.

Important nuance: these gains come with increased token usage and can trade off with pass@1 in some cases.

---

## Why This Matters

It’s strong evidence for a workflow pattern that matches your system:
> Don’t just decompose tasks — explicitly generate *diverse plans* and then select/validate.

This supports multi-agent “debate” as a mechanism for diversity, but it also suggests you can get some of the benefit from *single-model* plan diversification if you structure it correctly.

---

## Critical Caveats

1. **Token cost:** PlanSearch uses meaningfully more compute/tokens than naive sampling.
2. **Selection is still hard:** you need a good filter/reranker to convert pass@k into pass@1.
3. **Mostly competitive-programming evaluation:** not directly repo-scale.

---

## Relevance to Knowledge & Vibes

### Supports
- Generating multiple “bead plans” and selecting with evidence (tests, constraints).
- Viewing planning as a *search problem*.

### Practical implication
In calibration, explicitly ask: “What alternative plans exist that solve the same goal with different tradeoffs?” Then choose with evidence.

