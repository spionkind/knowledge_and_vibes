# Code‑Form Planning (CODEPLAN)

**Paper:** Unlocking Reasoning Potential in Large Language Models by Scaling Code‑form Planning  
**URL:** https://arxiv.org/abs/2409.12452  
**Date:** Oct 2024  
**Venue:** arXiv preprint

---

## Summary

This work studies *plan representation*. It trains LLMs to:
1) generate a **code‑form plan** (pseudocode with control flow: loops, conditionals, functions)  
2) then produce the final answer conditioned on that plan

The claim is that code-form plans are:
- more structured than natural language plans
- easier for models to learn and follow for multi-step reasoning
- automatically extractable at scale to create large training datasets

---

## Key Claims (Reported)

- Trained on ~**2M** prompt/plan/response triples.
- Reports ~**25% relative improvement** (averaged) across a set of multi-step reasoning benchmarks, with bigger gains on harder tasks.

---

## Practical Implications (For Knowledge & Vibes)

1. **Prefer “pseudocode specs” for complex logic.** For algorithmic beads, require a pseudocode plan + invariants before implementation.
2. **Plans should be executable-ish.** Use structured plans (bulleted steps with inputs/outputs, or pseudocode) rather than prose.
3. **Plan verification becomes easier.** Code-form plans are easier to check for missing branches and edge cases than narrative plans.

---

## Caveats

- This is reasoning-focused, not repo-scale SWE; treat it as evidence that plan structure matters.

