# SWE-bench

**Paper:** SWE-bench: Can Language Models Resolve Real-World GitHub Issues?  
**URL:** https://ar5iv.labs.arxiv.org/html/2310.06770  
**Date:** Oct 2023 (arXiv submission); ICLR 2024  
**Venue:** ICLR 2024

---

## The Core Idea

Evaluate whether LLMs can resolve **real GitHub issues** end-to-end: read an issue, modify a real repo at a specific commit, and produce a patch that makes tests pass.

This is very different from “write a standalone function” benchmarks because it requires:
- Navigating large repositories
- Localizing the correct edit locations
- Coordinating multi-file changes
- Respecting project conventions + APIs
- Passing an execution-based test harness

---

## Dataset Construction (What Counts as a Task)

Each SWE-bench instance is built from a merged PR that links to one or more issues and introduces test changes.

An instance includes:
- **Codebase (`C`)**: repository at the PR’s base commit
- **Problem statement (`P`)**: issue title + description (and linked issue bodies when multiple)
- **Tests (`T`)**: the test suite in the “fixed” version (used for evaluation)
- **Gold patch (`δ`)**: the PR’s code changes

Crucially, tasks are execution-validated: at least one test must flip from failing → passing when applying the gold patch.

---

## Evaluation (What “Solved” Means)

Models output a patch `δ̂`. The harness:
1. Applies `δ̂` to `C`
2. Runs tests `T`
3. Requires the same **FAIL_TO_PASS** / **PASS_TO_PASS** behavior the gold patch induces

This avoids judging by surface similarity to the PR diff; only behavior matters.

---

## Key Results (High-Level)

Even with strong models and retrieval assistance, solve rates are low in the original paper. The headline takeaway is that **localization + correct repo-context editing** is the bottleneck, not just “can you write code”.

The paper also demonstrates how sensitive results are to:
- What context retrieval strategy is used (“oracle” vs heuristic retrieval)
- Patch formatting / application success rates
- Execution environment brittleness

---

## Why This Paper Matters

SWE-bench effectively re-frames “AI coding” as **software engineering in situ**:
- It rewards systems that can reason about *existing* systems, not just generate snippets.
- It makes “tooling” (search, diffing, tests, environment setup) a first-class part of capability.
- It exposes the gap between “looks plausible” and “actually passes CI.”

---

## Critical Caveats

1. **Benchmark brittleness:** environment setup and tests can be flaky; small harness differences can change outcomes.
2. **Issue quality variance:** some issues are underspecified; others contain hints/solutions.
3. **Contamination risk:** once a benchmark becomes popular/public, future models may train on it (a theme later addressed by SWE-Bench+, SWE-bench Verified, SWE-bench-Live, SWE-rebench).

---

## Relevance to Knowledge & Vibes

### Supports
- Planning + decomposition as a response to multi-file, dependency-heavy work.
- Explicit “localization → edit → validate” loops (don’t jump straight to patching).
- Tool-first execution: search, test running, and repo navigation are as important as “reasoning prompts”.

### Implication for your process
If you want production-grade outcomes, the plan should explicitly allocate work to:
1. **Repository understanding/localization**
2. **Patch construction**
3. **Execution-based validation and repair loops**

