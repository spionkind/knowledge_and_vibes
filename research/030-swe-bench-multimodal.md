# SWE-bench Multimodal (Visual + JavaScript SWE)

**Paper:** SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?  
**URL:** https://openreview.net/forum?id=NGpXq4SoPo  
**Date:** ICLR 2025  
**Venue:** ICLR 2025

---

## The Core Idea

Classic SWE-bench is text-only and Python-heavy. Real SWE often includes:
- screenshots of UI bugs
- visual diffs
- diagrams/mockups
- JS/TS frontends

SWE-bench Multimodal evaluates whether SWE agents generalize to **visual, user-facing JavaScript software** where tasks include images.

---

## Dataset (Headlines)

The benchmark reports:
- **~617** task instances
- **17** JavaScript libraries
- Each task includes at least one image in the problem statement or tests

---

## Key Finding

Systems that score well on text-only SWE-bench often **struggle** here, indicating:
- poor cross-language generalization (Python → JS)
- weak multimodal grounding (images → correct code edits)

The benchmark highlights that interfaces/harness design (e.g., SWE-agent-style systems) can matter a lot in multimodal settings.

---

## Why This Matters

If your goal is “production-grade software indistinguishable from professional work,” you can’t ignore multimodal domains:
- frontend work is inherently visual
- UX bugs are often screenshot-driven

This benchmark pressures agent systems to incorporate image understanding into repo editing workflows.

---

## Critical Caveats

1. **Still a benchmark subset of reality:** UI work involves running apps, manual reproduction, and subjective acceptance criteria.
2. **Tooling dependency:** success likely depends on having the right tools (rendering, snapshot comparison, UI automation).

---

## Relevance to Knowledge & Vibes

### Supports
- Your insistence on “north star” clarity: UI bugs often require explicit acceptance criteria beyond tests.
- Calibration seminars that reason over the *whole product* (not just code correctness).

### Practical implication
Add explicit UX/visual acceptance artifacts to planning templates when the domain is UI-heavy:
- screenshot-based acceptance checks
- visual regression testing plans

