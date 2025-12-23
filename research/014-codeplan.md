# CodePlan (Repository-level Planning + Chain of Edits)

**Paper:** CodePlan: Repository-level Coding using LLMs and Planning  
**URL:** https://dl.acm.org/doi/10.1145/3643757  
**Date:** FSE 2024 (paper); arXiv Sep 2023  
**Venue:** FSE 2024

---

## The Core Idea

Repository-level tasks (migrations, refactors, fixing type/build errors) usually require a **sequence of interdependent edits**. You can’t do them in one shot because:
- The repo doesn’t fit in context
- Each change creates new obligations elsewhere (imports, call sites, types)

CodePlan frames this as a **planning problem**: synthesize and execute a “chain of edits”, where each edit is a grounded, local LLM call informed by repository analysis.

---

## How CodePlan Works (Mechanistically)

1. **Seed edit specs**: start with known obligations (e.g., migrate API X → Y, or fix a specific static error)
2. **Dependency analysis** (incremental): build/update a repo dependency graph as edits land
3. **May-impact propagation**: infer derived obligations (what else must change because of this edit)
4. **Plan execution**: for each obligation:
   - pull *spatial context* (related code)
   - pull *temporal context* (what has already changed)
   - call LLM to produce the edit
5. **Oracle check**: run an external oracle (build/typecheck/tests) to surface new errors → become new obligations

The key idea is that the plan is **not fully known upfront**; it expands as consequences appear.

---

## Reported Results (Headlines)

Across repo-level tasks (e.g., package migration, multi-file edits), CodePlan reports:
- Substantially better “end validity” (repos building/typechecking) than baselines that use the same oracle but don’t do structured planning / propagation
- A common headline: CodePlan gets multiple repos to pass validity checks while baselines get ~0 in their comparisons

---

## Why This Matters

This paper is one of the most direct academic validations of your “beads/phases” instinct:
- The correct unit of work is often a **chain**, not a single patch.
- Planning should be **adaptive** and driven by downstream errors, not rigid.

---

## Critical Caveats

1. **Relies on analysis infrastructure:** dependency graphs and impact analysis are non-trivial per language.
2. **Oracle quality limits progress:** if the oracle is weak/noisy (or too slow), the planning loop degrades.
3. **Not “agent debate”:** the win is mostly from program analysis + planning, not multi-agent discussion.

---

## Relevance to Knowledge & Vibes

### Strong supports
- Your “after-phase calibration” design: a natural checkpoint is “oracle feedback → update plan”.
- Treating future tasks as *conditional*: “If build fails with X, spawn bead Y”.

### Practical implication
Your master plan format should allow for **conditional beads** triggered by validation outcomes, not only linear phases.

