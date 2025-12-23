# SWE-bench-Live (Continuously Updating SWE Benchmark)

**Paper:** SWE-bench Goes Live!  
**URL:** https://arxiv.org/abs/2505.23419  
**Date:** May 2025  
**Venue:** arXiv preprint

---

## The Core Idea

Static benchmarks degrade quickly:
- models may train on them (contamination)
- repos evolve; environments rot
- “leaderboard chasing” overfits to artifacts

SWE-bench-Live is a **continuously updating** benchmark for issue resolution that aims to stay fresh and contamination-resistant.

---

## What’s New vs SWE-bench

The paper reports an initial release with:
- **~1,319** tasks from GitHub issues created since Jan 2024
- **~93 repositories** (broader coverage than the original SWE-bench’s small repo set)
- Per-task **Docker images** for reproducible execution
- A more automated instance creation pipeline (referred to as RepoLaunch in the paper)

---

## Key Takeaway

When evaluated on fresh tasks, many systems that look strong on SWE-bench / Verified perform materially worse, suggesting:
- overfitting to static benchmarks
- implicit contamination
- brittleness to repo/environment diversity

---

## Critical Caveats

1. **Still expensive:** building and validating per-task environments is heavy even if automated.
2. **Language scope:** early versions are still skewed toward Python; multi-language is an ongoing direction.
3. **Monthly updates complicate comparisons:** you need frozen splits for apples-to-apples tracking (the project provides “lite/verified” frozen splits for this reason).

---

## Relevance to Knowledge & Vibes

### Supports
- Your emphasis on calibration: static plans drift; reality changes while you build.
- Treating “freshness” as a first-class axis: what worked last month may not work today.

### Practical implication
Build planning workflows that assume drift:
- explicit update points
- structured “what changed?” diffs
- re-validating assumptions against current repo state

