# SWE-agent (Agent-Computer Interfaces)

**Paper:** SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering  
**URL:** https://arxiv.org/abs/2405.15793  
**Date:** May 2024  
**Venue:** NeurIPS 2024

---

## The Core Idea

Most “agent” gains aren’t just model IQ — they come from the **interface** the model uses to act.

SWE-agent argues that language-model agents are a new class of “computer user”, and like humans benefit from purpose-built interfaces (analogous to IDEs vs raw terminals).

---

## What The Agent-Computer Interface (ACI) Actually Changes

Instead of forcing the model through generic shell commands and noisy outputs, the ACI provides:
- Purpose-built commands for searching, opening, editing files with consistent feedback
- Output shaping to avoid “lost-in-the-noise” terminal dumps
- Guardrails (e.g., structured editing operations, error summaries)

The paper’s thesis: **tool ergonomics** is a primary determinant of agent performance.

---

## Reported Results (Headline)

SWE-agent reports strong improvements on:
- **SWE-bench** (pass@1 around **12.5%** in their reported setup)
- **HumanEvalFix** (pass@1 around **87.7%**)

The key claim is that *the same model* performs much better when the interface is tailored to agent needs.

---

## Why This Paper Matters

It reframes “planning” in agent systems as partly a **product design** problem:
- Reduce friction for common actions (search, open file, patch, run tests)
- Make tool outputs compact, consistent, and decision-ready
- Treat context as a scarce resource; the interface should manage it

---

## Critical Caveats

1. **System quality depends on harness fidelity:** environment setup and test invocation still dominate in repo-level tasks.
2. **Interface gains can be misattributed to “better reasoning”:** improvements may come from reduced noise and better action primitives, not a fundamentally smarter model.

---

## Relevance to Knowledge & Vibes

### Strongly supports
- Your emphasis on **structured workflows** (beads/phases) + **calibration checkpoints**
- Building agent-native capabilities (slash commands) that standardize high-leverage actions

### Practical implication
You should treat “/commands” as part of the agent’s IDE:
- Encode best practices as ergonomic, repeatable tool flows
- Minimize output verbosity and maximize “next-action clarity”

