# ADaPT (As‑Needed Decomposition and Planning)

**Paper:** ADaPT: As‑Needed Decomposition and Planning with Language Models  
**URL:** https://arxiv.org/abs/2311.05772  
**Date:** Nov 2023 (v2 Apr 2024)  
**Venue:** arXiv preprint

---

## Summary

ADaPT argues that *fixed* “plan‑then‑execute” breaks down when execution fails, but *always* re-planning is wasteful. Instead, ADaPT decomposes and plans **only when needed**:
- an **Executor** LLM attempts the current task/subtask directly
- when the executor fails, a **Planner** LLM decomposes that subtask into smaller pieces
- recursion continues until the executor can reliably complete pieces

This is an **adaptive decomposition** policy: defer planning until the system has evidence it is required.

---

## Key Results (Reported)

Across interactive decision-making benchmarks, ADaPT reports sizeable gains over common baselines (ReAct / Plan‑and‑Execute / Reflexion variants), with headline improvements like:
- **ALFWorld:** up to **+28.3%** success
- **WebShop:** **+27%** success
- **TextCraft:** **+33%** success

---

## Practical Implications (For Knowledge & Vibes)

1. **Don't over-decompose up front.** Start with coarse beads, then decompose *as-needed* when an execution attempt reveals uncertainty or failure.
2. **Treat "failure" as a signal to branch.** When a bead gets stuck after 3 iterations, spawn sub-beads (or spikes) rather than forcing the same bead to grow without bound.
3. **Make decomposition conditional.** Your plan format should allow "if X fails, decompose into Y/Z" instead of committing to a rigid tree.

---

## The ADaPT Flow (As Applied in This Repo)

```
1. START COARSE: Create beads at the level you think is atomic
2. ATTEMPT EXECUTION: Run the bead (tests + implementation)
3. IF SUCCESS: Close bead, move on
4. IF FAILURE (after 3 iterations):
   a. STOP implementation (security degrades with more iterations)
   b. ANALYZE: What specific sub-problem caused failure?
   c. SPAWN SUB-BEAD: Create sub-bead for ONLY the failing part
   d. REPEAT from step 2 for sub-bead
```

**Key insight:** This approach discovers what's *actually* hard rather than guessing upfront.

---

## Integration with Other Research

| Research | Connection to ADaPT |
|----------|---------------------|
| `research/011-agentless.md` | Simple pipelines beat complex agents—supports starting coarse |
| `research/053-feedback-loop-security.md` | Security degrades with >3 iterations—supports stopping and decomposing |
| `research/057-anthropic-context-engineering.md` | Minimal context is better—supports not over-planning |

---

## Caveats

- The benchmarks are not repo-scale SWE tasks; the principle (adaptive decomposition) transfers, but magnitudes may not.
- Requires a crisp definition of "failure" (tests, build breaks, unmet AC) to avoid noisy triggering.
- Combined with 3-iteration cap from security research, this creates a principled stopping rule.

