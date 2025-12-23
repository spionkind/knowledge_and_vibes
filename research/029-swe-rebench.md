# SWE-rebench (Decontaminated, Standardized SWE Eval)

**Paper:** SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents  
**URL:** https://arxiv.org/pdf/2505.20411  
**Date:** May 2025  
**Venue:** arXiv preprint

---

## The Core Idea

Two major problems plague SWE agent evaluation:
1. **Contamination**: popular benchmarks become training data
2. **Incomparable scaffolds**: every lab uses different prompts, tools, and orchestration

SWE-rebench attempts to fix both by:
- continuously mining new tasks
- standardizing the evaluation scaffold
- explicitly tracking contamination risk by task date vs model release

---

## Pipeline (High Level)

The paper describes an automated pipeline that:
1. Mines real issues/PRs from GitHub at scale
2. Builds environment setup recipes (LLM-assisted) and iteratively repairs them using failure logs
3. Execution-validates tasks
4. Scores task quality (issue clarity, complexity, patch correctness) via automated assessment

It also produces a large interactive dataset (reported **>21k** Python tasks in one release) suitable for training/RL.

---

## Evaluation Principles That Matter

SWE-rebench emphasizes:
- **Standardized minimal scaffold** (fixed prompts, minimal ReAct-like loop)
- **Multiple runs per model** (e.g., 5 runs) and reporting **pass@5** + mean/SEM to account for stochasticity
- **Explicit contamination marking** for potentially leaky evaluations

This is closer to how serious benchmarking is done when variance is high.

---

## Why This Matters

For “frontier-labs style” internal agent development, this is the direction:
- build infrastructure that keeps benchmarks fresh
- separate model capability from scaffold engineering
- report uncertainty, not just a single number

---

## Critical Caveats

1. **Still scaffold-dependent:** even a “minimal” scaffold is a design choice.
2. **Automation can introduce subtle biases:** LLM-assisted environment recipes may skew toward ecosystems the model already understands.
3. **Python-first:** multi-language coverage is a future direction.

---

## Relevance to Knowledge & Vibes

### Supports
- Your desire for evidence-based planning across many sessions: standardized evaluation is how you learn what works.
- Calibration as a guardrail against drift: re-check performance/assumptions as the benchmark moves.

### Practical implication
Adopt SWE-rebench’s reporting mindset internally:
- run important tasks multiple times (or multiple models)
- measure variance
- don’t overfit to a single outcome

