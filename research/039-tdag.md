# TDAG (Dynamic Task Decomposition + Agent Generation)

**Paper:** TDAG: A Multi‑Agent Framework based on Dynamic Task Decomposition and Agent Generation  
**URL:** https://arxiv.org/abs/2402.10178  
**Date:** Feb 2024  
**Venue:** arXiv preprint (later journal version)

---

## Summary

TDAG proposes a multi-agent framework where:
- the system **dynamically decomposes** a complex task into subtasks
- for each subtask, it **generates a specialized sub‑agent** (prompted/configured for that subtask)
- the decomposition can be **revised** based on intermediate outcomes (to reduce error propagation)

It’s an argument for **adaptive task graphs**: the correct decomposition is often *not knowable* upfront; it emerges as execution reveals new constraints.

---

## Key Contributions

- **Dynamic decomposition:** refine the task tree as new information arrives.
- **Agent generation:** don’t reuse one fixed agent for every subtask; generate subagents tuned to the subtask.
- **Skill accumulation (library):** capture useful solutions/skills for future reuse (conceptually similar to an exemplar/memory bank).

---

## Practical Implications (For Knowledge & Vibes)

1. **“Agents as components,” not roleplay.** TDAG’s “agent generation” maps cleanly to spawning purpose-built sub-agents/beads with constrained scope and explicit outputs.
2. **Calibration as decomposition control.** Use `/calibrate` to decide whether to (a) keep current decomposition, (b) split, (c) merge, or (d) pivot, based on evidence.
3. **Skill library ≈ project memory.** The “skill accumulation” idea aligns with your `cm`/CASS memory layer: store solved patterns and reuse them.

---

## Caveats

- Evaluated on planning/tool-use tasks (not repo-scale SWE). Treat it as evidence for *adaptive decomposition*, not a full SWE recipe.

