# Decomposition

How to break a completed plan into phases and beads that AI agents can execute without losing requirements.

**Prerequisite:** You have a master plan. If not, start with [Planning Deep Dive](./PLANNING_DEEP_DIVE.md).

**The core problem:** Long context degrades AI reasoning by 30-50%. A 10,000-line plan will have silent omissions. A 500-line phase won't.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [The Hierarchy: Plan → Phases → Beads](#the-hierarchy-plan--phases--beads)
- [Why Phases and Beads Exist](#why-phases-and-beads-exist-context-control)
- [Phase Breakdown](#phase-breakdown-operator-led)
- [Scheduling Calibration Points](#scheduling-calibration-points-between-phases)
- [Adaptive Decomposition (ADaPT)](#adaptive-decomposition-adapt-pattern)
- [Decompose a Phase Into Beads](#decompose-a-phase-into-task-beads-decompose-task)
- [Validate the Graph](#validate-the-graph-bv)
- [Parallel Execution](#parallel-execution-without-chaos)
- [Traceability](#traceability-agent-native)
- [Bead Close](#bead-close-done-means-verified)
- [Anti-Patterns](#anti-patterns)

---

## Prerequisites

This guide assumes you already have:
- A pinned North Star Card (`templates/NORTH_STAR_CARD_TEMPLATE.md`)
- Requirements with falsifiable acceptance criteria (`REQ-*` / `AC-*`)
- Key architectural decisions captured (ADRs), and top risks spiked

If you're still in ideation/requirements, start here instead:
- `PLANNING_DEEP_DIVE.md`
- `EVIDENCE_BASED_GUIDE.md`
- `PROTOCOLS.md`

New to the repo? Start with:
- `START_HERE.md`

---

## The Hierarchy: Plan → Phases → Beads

```
Master Plan (complete specification)
    ↓
Phases (~500-1000 lines each)
    ↓
Phase/Epic Beads (container for each phase, type=epic)
    ↓
Task Beads (individual work items: .1, .2, etc.)
    ↓
ADaPT Sub-Beads (created ONLY when task beads fail: .1.1, .2.1)
```

### Terminology

| Term | When Created | Purpose | Example ID |
|------|--------------|---------|------------|
| **Phase** | Planning | Conceptual slice of the plan | (document, not bead) |
| **Phase/Epic Bead** | Decomposition | Container for a phase's work | `phase-1-auth` |
| **Task Beads** | Decomposition | Individual work items | `phase-1-auth.1`, `.2` |
| **ADaPT Sub-Beads** | Execution (after 3 failures) | Decompose failing task | `phase-1-auth.2.1` |

**Key insight:** Don't decompose all the way upfront. Start coarse (phases → task beads), then split only when execution reveals what's actually hard (ADaPT sub-beads).

---

## Why Phases and Beads Exist (Context Control)

Agents are brittle on large, dense plans: long context encourages silent omission and vague summarization.

So we use **context control artifacts**:
- **Phases** = short, lossless slices of the plan (conceptual, in docs)
- **Phase/Epic Beads** = containers for each phase's work (in bead tracker)
- **Task Beads** = atomic execution tasks with verifiable "done"
- **ADaPT Sub-Beads** = created **only when execution fails** (don't over-decompose upfront)

### Sizing Heuristic (Semantic Units, Not Line Counts)

The goal is **semantic coherence**: can an agent hold the full context without losing track of dependencies?

| Artifact | Heuristic | Why |
|----------|-----------|-----|
| Phase docs | ~500–1000 lines | Coarse guardrail—adjust based on complexity |
| Phase/Epic beads | One per phase | Container for tracking phase work |
| Task beads | One testable capability | Can be verified independently |
| ADaPT sub-beads | Split from failing task bead | Decompose only when execution reveals uncertainty |

**The 500-line number is not about file length.** It's about: "Can an agent understand the full semantic context without degradation?" 500 lines of boilerplate ≠ 500 lines of complex interdependent logic. Adjust based on semantic density.

Evidence anchors: `research/004-context-length-hurts.md`, `research/005-lost-in-middle-code.md`, `research/057-anthropic-context-engineering.md`.

---

## Phase Breakdown (Operator-Led)

Use the phase template:
- `.claude/templates/planning/phase-document.md`

Minimum expectations:
- include the North Star Card verbatim (plus a 1-line alignment note)
- reference the relevant `REQ-*` / `AC-*` items this phase covers
- specify the edit locus (key dirs/files) so agents don’t wander
- define verification (tests/commands) that makes “done” objective
- mark whether this is a **scheduled calibration point**

If a phase can’t be implemented without guessing, it’s not ready to decompose.

---

## Scheduling Calibration Points (Between Phases)

Calibration is the “search controller”: branch/prune/pivot based on evidence.

Schedule calibration when a phase:
- introduces foundational infrastructure (auth, data model, build system)
- merges parallel tracks (integration convergence)
- changes risky assumptions (security/perf/ops)
- unblocks many downstream phases (high centrality in BV)

Implementation pattern:
- create an explicit **calibration bead** that depends on all phase beads
- do not start the next phase until the calibration bead is closed

Slash command:
- `/calibrate [phase_or_milestone]` → `.claude/commands/calibrate.md`

---

## Adaptive Decomposition (ADaPT Pattern)

> **Key insight (ADaPT, 2025):** "Decompose only when execution fails." Don't over-decompose upfront—start coarse and split when reality demands it.

### The ADaPT Flow

```
1. START COARSE: Create task beads at the level you think is atomic
2. ATTEMPT EXECUTION: Run the task bead (tests + implementation)
3. IF SUCCESS: Close bead, move on
4. IF FAILURE (after 3 iterations):
   a. STOP implementation
   b. ANALYZE: What specific sub-problem caused failure?
   c. SPAWN ADaPT SUB-BEAD: Create sub-bead for ONLY the failing part
   d. REPEAT from step 2 for the ADaPT sub-bead
```

**Naming:** ADaPT sub-beads inherit parent ID with suffix: `user-auth.2` → `user-auth.2.1`

### Why ADaPT Works

| Over-Decomposition (Bad) | Adaptive Decomposition (Good) |
|--------------------------|-------------------------------|
| Guesses what will be hard | Discovers what is actually hard |
| Creates unnecessary beads | Creates beads only when needed |
| Front-loads planning time | Distributes planning across execution |
| Assumes you know the unknowns | Reveals unknowns through execution |

Evidence: `research/038-adapt.md`, `research/011-agentless.md` (simple pipelines beat complex agents).

---

## Decompose a Phase Into Task Beads (`/decompose-task`)

Slash command:
- `/decompose-task [phase]` → `.claude/commands/decompose-task.md`

Templates:
- Phase/Epic bead: `.claude/templates/beads/bead-structure.md`
- Task beads: `.claude/templates/beads/bead-structure.md` (same template)
- ADaPT sub-beads: `.claude/templates/planning/sub-bead-structure.md`

Each task bead should include:
- **tests FIRST** (written before implementation—TDD)
- **intent** (tie to `REQ-*` / `AC-*`)
- **edit locus** (exact files/dirs)
- **dependencies** (beads + external constraints)
- **verification** (exact tests/commands + expected outcomes)
- **grounding policy** (what must be verified vs what is an assumption)
- **handoff safety** (another agent can finish this)

If you can't write tests, you don't have a task bead yet — you have a guess.

---

## Validate the Graph (BV)

Before agents execute at scale, validate dependencies:

```bash
bv --robot-suggest   # missing deps, duplicates, cycle break suggestions
bv --robot-plan      # is there a sane execution order?
bv --robot-alerts    # drift signals / risky topology
```

Common dependency patterns:
- schema/migrations task beads → blocks → implementation task beads
- implementation task beads → blocks → test task beads
- all phase task beads → block → calibration bead → blocks → next phase's task beads

---

## Parallel Execution Without Chaos

Parallelism is good until it creates merge conflicts and divergent assumptions.

Safeguards:
- partition by subsystem (`bv --robot-triage --robot-triage-by-track`)
- use Agent Mail file reservations before edits
- keep task beads small (reduce conflict surface area)
- converge via explicit integration task beads (don't "accidentally merge")

---

## Traceability (Agent-Native)

Maintain a single coverage map:
- `templates/TRACEABILITY_TEMPLATE.md`

During decomposition:
- map `REQ-*` / `AC-*` → task beads

During implementation:
- map beads → tests and verification evidence

During calibration:
- scan for “REQ has no beads” / “REQ has no tests” / “AC unverified”

---

## Bead Close (“Done” Means Verified)

Before closing:
- verification passes (tests/build/typecheck as relevant)
- `ubs --staged` is clean for the touched area
- traceability updated for the requirements this bead claims to satisfy
- if this is an integration boundary: schedule or trigger `/calibrate`

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Do Instead |
|--------------|--------------|------------|
| Decomposing directly from massive plan | Lossy summarization | Phase breakdown first |
| Beads without tests | "Looks right" is not evidence | TDD-first: tests before code |
| Starting Phase N+1 before calibrating N | Drift compounds unchecked | Hard stop at calibration points |
| Over-decomposing upfront | Guesses what will be hard | ADaPT: decompose only on failure |
| Rhetorical agent debate | Persuasive agent wins, not correct one | Test-based adjudication |
| One bead touching "everything" | High conflict surface area | Partition by edit locus |
| Massive "lossless" plans | Context length hurts quality | Minimal viable plan for complexity |

---

## Further Reading

- `EVIDENCE_BASED_GUIDE.md` (end-to-end gates + artifacts)
- `PROTOCOLS.md` (protocol cards)
- `PLANNING_DEEP_DIVE.md` (nontechnical planning tutorial)
- `docs/guides/TOOL_STACK_AND_OPERATIONS.md` (tool operations + multi-agent coordination)
- `.claude/templates/planning/phase-document.md` (phase template)
- `.claude/templates/beads/bead-structure.md` (bead template)

---

## NLU (No Longer Used)

- NLU/DECOMPOSITION_LEGACY.md — legacy version kept for reference.
