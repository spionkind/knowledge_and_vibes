# LiveCodeBench (Contamination-Resistant Code Eval)

**Paper:** LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code  
**URL:** https://arxiv.org/html/2403.07974v1  
**Date:** Mar 2024  
**Venue:** arXiv preprint

---

## The Core Idea

Most coding benchmarks (HumanEval/MBPP) are:
- Small
- Static
- Increasingly contaminated (models may have trained on them)

LiveCodeBench is designed to be:
- **Continuously updated** (new problems over time)
- **Date-filterable** (evaluate only problems released after a model’s cutoff)
- **Holistic** (measure more than “write code”)

---

## What It Measures (4 Scenarios)

1. **Code generation**
2. **Self-repair** (fix code given execution feedback)
3. **Code execution** (predict outputs)
4. **Test output prediction** (infer outputs from problem statement + inputs)

This is closer to how agents actually work: they generate, run, observe failures, and repair.

---

## Dataset

Problems are pulled from contest platforms (e.g., LeetCode, AtCoder, Codeforces) and tagged by release dates. The paper reports ~**400** problems in the initial release windows.

---

## Why This Matters

It’s a practical warning:
> High scores on static benchmarks can hide brittleness, contamination, or overfitting.

And it legitimizes “self-repair” as a first-class capability, not an afterthought.

---

## Critical Caveats

1. **Mostly Python-focused** in early versions.
2. **Date-cutoff filtering can shrink sample sizes**, adding variance (especially for newer models).
3. **Still not repo-scale:** it’s competitive-programming style, not SWE-bench style.

---

## Relevance to Knowledge & Vibes

### Supports
- Multi-pass planning and verification loops: self-repair is a measurable capability.
- Your push for “calibrate between phases”: iterative correction is normal, not failure.

### Practical implication
Treat “repair loops” as an explicit bead type: generate → run → diagnose → patch → rerun.

