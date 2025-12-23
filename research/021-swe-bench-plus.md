# SWE-Bench+ (Benchmark Quality + Decontamination)

**Paper:** SWE-Bench+: Enhanced Coding Benchmark for LLMs  
**URL:** https://arxiv.org/html/2410.06992v1  
**Date:** Oct 2024  
**Venue:** arXiv preprint

---

## The Core Idea

SWE-bench is hugely valuable, but the paper argues prior reported scores are inflated by:
- **Solution leakage** (issue comments essentially give the fix)
- **Weak tests** (patch passes but doesn’t truly fix)
- **Contamination risk** (issues predating model cutoffs; data may be in training corpora)

SWE-Bench+ is a refined benchmark designed to reduce these artifacts.

---

## Key Findings (From Their Analysis)

They report that, among “successful” patches on SWE-bench:
- ~**32.7%** relied on solutions present in issue text/comments (“cheating”)
- ~**31.1%** were suspicious due to weak tests

When they filter out problematic instances, previously-reported solve rates drop sharply.

---

## What SWE-Bench+ Changes

The refined set aims to ensure:
- Issues are created after relevant model cutoffs (reducing contamination)
- Issues do not contain the solution in the text/comments (reducing leakage)

However, the paper emphasizes weak tests remain a core challenge even after decontamination.

---

## Why This Matters

This paper is a cautionary note for your whole “frontier-labs workflow replication” goal:
> You can’t optimize an agent workflow if your feedback signal (tests/benchmark) is leaky or weak.

---

## Critical Caveats

1. **Harder doesn’t always mean better:** some “hard” instances may be underspecified rather than genuinely complex.
2. **Still Python / SWE-bench-shaped:** improvements in benchmark hygiene don’t fully generalize.

---

## Relevance to Knowledge & Vibes

### Supports
- Your insistence that agents ground claims in evidence and tests.
- Building “evidence standards” into calibration.

### Practical implication
Your planning protocol should explicitly address test strength:
- “What tests would falsify our patch?”
- “Are we passing because tests are weak?”

