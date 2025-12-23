# SWE-smith (Scaling Training Data for SWE Agents)

**Paper:** SWE-smith: Scaling Data for Software Engineering Agents  
**URL:** https://arxiv.org/abs/2504.21798  
**Date:** Apr 2025  
**Venue:** arXiv preprint

---

## The Core Idea

SWE agents are data-hungry, but real SWE-bench-style tasks are expensive to curate because each task needs:
- a working environment
- tests
- a real issue/PR

SWE-smith generates **synthetic SWE tasks at scale** by:
1. Taking a repo with passing tests
2. Introducing bugs that break existing tests
3. Packaging the result as a solvable “issue” instance

---

## Why This Is Clever

Instead of building a new environment per task, SWE-smith:
- builds a shared environment per repository
- synthesizes many tasks inside it

This reduces storage and makes scaling feasible.

---

## Bug Generation Strategies (High Level)

The paper describes multiple strategies, including:
- LLM-based rewrites/modifications of functions/classes to introduce subtle logic bugs
- Procedural AST transformations (zero-cost bug injection)
- Combining multiple bugs into harder tasks
- “PR mirroring” (reverting real PRs with an LLM when naive reversions fail)

---

## Reported Results (Headlines)

They report generating a dataset of **~50k** task instances across **128** repos, and training open-weight agents that achieve around:
- **~40% pass@1** on SWE-bench Verified for a 32B open-weight agent in their setup

---

## Why This Matters

It’s a strong signal that “frontier-style” SWE agents will increasingly be trained, not just prompted.

And it suggests a path toward making robust SWE agent performance accessible without closed-source proprietary data.

---

## Critical Caveats

1. **Synthetic ≠ real:** synthetic bugs may not match real issue distributions.
2. **Test dependence:** only repos with decent tests are amenable.
3. **Language scope:** Python-first; generalization across ecosystems is open work.

---

## Relevance to Knowledge & Vibes

### Supports
- The idea that rigorous planning can be taught by repeated exposure to validated tasks.
- “Project rigor modes”: enterprise-grade workflows need stronger feedback loops and more training-like iteration.

### Practical implication
In your process docs, emphasize that “tests are leverage”: they enable training, validation, and safe autonomy.

