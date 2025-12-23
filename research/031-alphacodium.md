# AlphaCodium (Flow Engineering for Code Generation)

**Paper:** Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering  
**URL:** https://arxiv.org/abs/2401.08500  
**Date:** Jan 2024  
**Venue:** arXiv preprint

---

## The Core Idea

For code generation, “better prompting” plateaus. AlphaCodium argues the bigger win is **flow engineering**:
- plan in structured intermediate artifacts
- generate tests (including AI-generated edge-case tests)
- iterate: generate → run → fix → rerun

This is essentially a test-driven execution loop wrapped in a disciplined multi-stage pipeline.

---

## What The Flow Looks Like (High Level)

Two phases:
1. **Pre-processing**
   - “Problem reflection” (spec distilled into bullet points)
   - Reason about public tests
   - Generate and rank candidate solution approaches
   - Generate additional AI tests for edge cases
2. **Code iterations**
   - Implement a candidate
   - Run public tests, fix failures
   - Run AI tests, fix failures while anchoring against already-passing public tests

---

## Reported Results (Headline)

On CodeContests / Codeforces-style problems, AlphaCodium reports large improvements versus a single direct prompt.

One cited headline:
- GPT-4 pass@5: **19% → 44%** with the AlphaCodium flow (validation setting in the paper)

---

## Why This Matters

AlphaCodium is strong empirical support for a workflow principle:
> For hard coding tasks, “write code” should be downstream of a *flow* that creates executable checks and iteratively repairs based on feedback.

This aligns directly with how modern SWE agents succeed: not by one-shot code, but by disciplined generate/run/fix loops.

---

## Critical Caveats

1. **Token/compute cost:** multi-stage flows spend more tokens than a single prompt.
2. **Benchmark shape:** CodeContests differs from repo-level issue resolution (SWE-bench); principles transfer but mechanics differ.
3. **Test generation risk:** AI tests can be wrong; anchor strategies matter.

---

## Relevance to Knowledge & Vibes

### Supports
- Treating planning as a **pipeline** (not a prompt).
- Making “tests as spec” a first-class artifact.
- Calibration checkpoints that are driven by **execution evidence**, not reflection.

### Practical implication
Add explicit “flow stages” to beads/phases:
spec → tests → implementation → run → repair → rerun.

