# CodeTree (Agent-Guided Tree Search for Code)

**Paper:** CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models  
**URL:** https://arxiv.org/html/2411.04329v2  
**Date:** Nov 2024  
**Venue:** arXiv preprint

---

## The Core Idea

Hard coding tasks have huge search spaces; single “plan then code” often collapses.

CodeTree explicitly performs **tree search over strategies and solutions**, using:
- Execution feedback (run/tests)
- LLM self-critique

It organizes attempts as a tree: different strategies at the top, implementations below, refinements under each.

---

## How It’s Structured

CodeTree uses specialized agent roles internally (as system components, not roleplay):
- **Thinker:** proposes strategies
- **Solver:** writes code from a strategy
- **Debugger:** iteratively fixes based on feedback
- **Critic:** decides which nodes to expand/stop based on feedback signals

---

## Reported Results (Headlines)

The paper reports strong gains across multiple benchmarks; with GPT-4o, they report results in the neighborhood of:
- ~**95%** HumanEval
- ~**99%** MBPP
- ~**43%** CodeContests

They also report improvements on SWE-bench-style tasks (harder repo-level), framed as benefiting from better exploration.

---

## Why This Matters

CodeTree is a concrete example of “planning + debugging” being insufficient without **search control**:
- You need a mechanism that decides *what to try next* under uncertainty.
- Execution feedback should actively shape the search, not just be a post-hoc check.

---

## Critical Caveats

1. **Compute-heavy:** tree search multiplies tokens/tool calls.
2. **Implementation complexity:** requires good orchestration, caching, and guardrails to avoid loops.
3. **Benchmark variance:** performance depends on the tool execution environment and stopping criteria.

---

## Relevance to Knowledge & Vibes

### Supports
- Your desire for periodic “roundtables”: they can function as a *search controller* (deciding next branch).
- Building agent-native tooling that can “pause and re-plan” before committing to a path.

### Practical implication
Your `/calibrate` can be framed as: “should we expand this branch, prune it, or open a new branch?”

