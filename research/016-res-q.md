# RES-Q (Repository-Scale Editing Benchmark)

**Paper:** RES-Q: Evaluating Code-Editing Large Language Model Systems at the Repository Scale  
**URL:** https://arxiv.org/html/2406.16801v2  
**Date:** Jun 2024  
**Venue:** arXiv preprint

---

## The Core Idea

Most coding benchmarks are too small (single file/function) or too saturated to differentiate modern models.

RES-Q evaluates **repository editing systems**: given a repo at a base commit + a compact (often vague) instruction, produce a patch that passes a handcrafted test suite.

---

## What Makes RES-Q Different

- **100 tasks** derived from real GitHub commits
- Multi-file edits are common
- Instructions often resemble real-world “lazy edit requests”
- Evaluation is binary: patch must apply + tests must pass (`pass@k`)

This targets the actual skill needed for agentic editing: interpret an ambiguous request, explore repo, implement a coherent change, and validate it.

---

## Notable Findings (Headlines)

The paper reports that:
- On RES-Q, **Claude Sonnet 3.5** outperforms **GPT-4o** by ~**12% pass@1** in their main unconstrained setting, despite small gaps on traditional coding benchmarks.
- Constraining context windows (e.g., 8K) hurts closed models but can help some open models (suggesting poor long-context utilization in some open weights).
- RES-Q can differentiate models where HumanEval-like tasks saturate.

---

## Why This Matters

RES-Q formalizes a reality your system already assumes:
> The hard part isn’t writing code. It’s navigating ambiguity + repo context under tight context budgets.

---

## Critical Caveats

1. **Only 100 tasks:** good for signal, but limited coverage.
2. **System-level benchmark:** results depend on the editing system scaffold, not just the base model.
3. **Handcrafted tests:** strong, but expensive to scale.

---

## Relevance to Knowledge & Vibes

### Supports
- Your push for standardized workflows: when benchmarks are system-dependent, the system design matters.
- “Calibration after phase”: ambiguity resolution + plan correction is part of real work.

### Practical implication
In your planning tutorial, treat “vague instruction → clarified requirement” as a formal step, not an ad-hoc conversation.

