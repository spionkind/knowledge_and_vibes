# RepairAgent (Autonomous Program Repair Agent)

**Paper:** RepairAgent: An Autonomous, LLM‑Based Agent for Program Repair  
**URL:** https://arxiv.org/abs/2403.17134  
**Date:** Mar 2024  
**Venue:** ICSE 2025 (later publication)

---

## Summary

RepairAgent treats program repair as an **agentic tool-using loop**, not a fixed prompt:
- it interleaves “understand the bug → gather info → attempt fix → validate”
- it chooses tools (search, read, tests) dynamically
- it uses a finite-state machine to avoid aimless wandering

This is strong evidence that **structured tool loops + validation** beat freeform prompting for repair.

---

## Key Results (Reported)

On Defects4J:
- **164** bugs repaired autonomously
- includes **39** bugs not fixed by several prior techniques (reported)
- average cost reported around **270k tokens per bug** (their estimates; depends on pricing/model)

---

## Practical Implications (For Knowledge & Vibes)

1. **Codify the repair loop.** When tests fail, switch into an explicit “repair mode” protocol (repro → localize → patch → re-run).
2. **Use state machines / checklists in beads.** Prevent infinite loops by forcing state transitions and “stop conditions.”
3. **Validation is the control signal.** RepairAgent’s success depends on repeatedly grounding in tests, not on deeper reflection.

---

## Caveats

- Program repair benchmarks are narrower than full feature work; still, the repair-loop discipline generalizes.

