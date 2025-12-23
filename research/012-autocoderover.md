# AutoCodeRover (Autonomous Program Improvement)

**Paper:** AutoCodeRover: Autonomous Program Improvement  
**URL:** https://arxiv.org/html/2404.05427v1  
**Date:** Apr 2024  
**Venue:** arXiv preprint

---

## The Core Idea

AutoCodeRover frames “LLM SWE” as a **program-structure problem**, not a “bag of files” problem.

It combines:
- Structure-aware code search (classes/methods/AST-level navigation)
- Iterative context retrieval (search → read → refine hypothesis)
- Patch generation
- Optional spectrum-based fault localization (SBFL) when tests exist

---

## What’s Novel Here

The key differentiator is the **context retrieval API**: the system encourages the agent to traverse code by program structure (e.g., symbol-level navigation) rather than brute-force grep + long-context dumping.

This is an early example of “tooling beats prompting” in repo-level tasks.

---

## Reported Results (Headlines)

AutoCodeRover reports:
- ~**19–22%** solve rate on SWE-bench Lite (depending on evaluation protocol / multiple runs)
- Lower average cost per issue than some competing agents (they report costs on the order of **<$1** per issue in their setup)
- Meaningful gains when SBFL signals are available

---

## Why This Matters

It validates a key principle for long-context repo work:
> You don’t win by stuffing the repo into context; you win by building tools that let the model *navigate to the right slices*.

---

## Critical Caveats

1. **Test availability matters:** SBFL only helps when you can run tests and compute suspiciousness.
2. **Heavily scaffolded retrieval:** the “agent” performance depends on the search primitives and how outputs are summarized.
3. **SWE-bench Lite-specific:** improvements may not translate 1:1 to other repo benchmarks or languages without similar structure tools.

---

## Relevance to Knowledge & Vibes

### Strong supports
- Your plan structure that separates **context discovery** from **editing**.
- Building agent-native tools (slash commands) that encapsulate structure-aware repo navigation.

### Practical implication
Your workflow should treat “repo search/navigation” as a first-class phase artifact:
- What symbols were inspected?
- What hypothesis was formed?
- What evidence narrows the edit site?

