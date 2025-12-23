# ThinkRepair (Self-Directed Automated Program Repair)

**Paper:** ThinkRepair: Self-Directed Automated Program Repair  
**URL:** https://arxiv.org/html/2407.20898v1  
**Date:** Jul 2024  
**Venue:** arXiv preprint

---

## The Core Idea

Instead of hand-crafted prompts, ThinkRepair builds a **self-generated knowledge pool** of:
- buggy function
- correct fix
- chain-of-thought rationale

Then, for a new bug, it selects relevant examples and runs a guided interaction loop with test feedback.

---

## Two-Phase Workflow

1. **Collection phase**
   - Prompt an LLM to propose fixes + reasoning on known buggy functions
   - Keep only fixes that pass tests
   - Store (bug, fix, CoT) as high-quality few-shot data

2. **Fixing phase**
   - Retrieve/select diverse relevant examples (clustering / contrastive selection)
   - Generate a fix with few-shot CoT prompting
   - If tests fail, feed failure info back and iterate a limited number of rounds

---

## Reported Results (Headlines)

ThinkRepair reports strong gains on classic APR datasets, including:
- Fixing on the order of **~98 bugs** on Defects4J v1.2 in their experiments
- Outperforming multiple SOTA APR baselines across Defects4J / QuixBugs

The main claimed contributor is better example selection + iterative feedback, not just more sampling.

---

## Why This Matters

ThinkRepair is an example of an important “frontier” pattern:
> Turn weak prompting into strong performance by building a validated exemplar pool.

It’s not roleplay; it’s a data/selection pipeline.

---

## Critical Caveats

1. **Benchmark leakage risk:** exemplar pools can inadvertently memorize dataset artifacts.
2. **Test quality:** still bounded by “passes tests” as correctness.
3. **Single-function focus:** repo-level issues add more uncertainty (environment, multi-file edits).

---

## Relevance to Knowledge & Vibes

### Supports
- Your desire for repeatable rigor: you can formalize “example pools” as internal project memory.
- Multi-session planning: build a validated knowledge base over time rather than solve everything in one shot.

### Practical implication
Capture “solved beads” as reusable exemplars (problem → plan → patch → validation outcome) and retrieve them in future work.

