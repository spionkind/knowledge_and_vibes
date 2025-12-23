---
name: full-pipeline
description: Execute the complete 10-stage evidence-based pipeline from ideation to release. Use when starting a new project, when the user says "full pipeline" or "end-to-end", or when orchestrating the complete development lifecycle.
---

# Full Pipeline — Orchestrator

Complete 10-stage evidence-based development pipeline.

> **Pattern:** This skill uses the orchestrator-subagent pattern. The full pipeline has 10 stages grouped into 6 subagents, each with fresh context. See `docs/guides/ORCHESTRATOR_SUBAGENT_PATTERN.md`.

## When This Applies

| Signal | Action |
|--------|--------|
| Starting new project | Run full pipeline |
| User says "full pipeline" | Run full pipeline |
| User says "end-to-end" | Run full pipeline |
| User says "/pipeline" | Run full pipeline |
| Need complete lifecycle | Run full pipeline |

---

## The 10 Stages

```
Stage 0: North Star           → What are we building? Why?
Stage 1: Requirements         → REQ-*, AC-* with trace IDs
Stage 2: Requirements QA      → Ambiguity removal
Stage 3: Decision Search      → ADRs for key decisions
Stage 4: Risk Assessment      → P0 risks identified
Stage 5: Spikes               → Unknowns resolved
Stage 6: Plan Assembly        → Phase structure (phases with calibration points)
Stage 7: Decomposition        → Phase beads → Task beads created
Stage 8: Execution            → TDD implementation (ADaPT sub-beads if failures)
Stage 9: Calibration          → Phase boundary checks
Stage 10: Release             → Ship with evidence
```

### Hierarchy Reference

```
Master Plan
    ↓
Phases (~500-1000 lines each, with calibration points)
    ↓
Phase/Epic Beads (container for each phase)
    ↓
Task Beads (.1, .2, etc. - created during Stage 7)
    ↓
ADaPT Sub-Beads (.1.1, .2.1 - created ONLY when task beads fail in Stage 8)
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   FULL-PIPELINE ORCHESTRATOR                     │
│  - Creates session: sessions/pipeline-{timestamp}/               │
│  - Manages TodoWrite for all 10 stages                          │
│  - Spawns subagents for grouped stages                          │
│  - User approval gates between major phases                     │
│  - Coordinates 10+ parallel Claude Code instances in Stage 8    │
└─────────────────────────────────────────────────────────────────┘
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
    ▼                         ▼                         ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  North Star  │     │ Requirements │     │  Decisions   │
│  agents/     │     │  agents/     │     │  agents/     │
│  northstar.md│     │  requirements│     │  decisions.md│
│  Stage 0     │     │  Stages 1-2  │     │  Stages 3-5  │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       │   (Sequential)     │                    │
    ┌──┴────────────────────┴────────────────────┴──┐
    │                                               │
    ▼                                               ▼
┌──────────────┐                            ┌──────────────┐
│ Plan Assembly│                            │   Release    │
│  agents/     │                            │  agents/     │
│  planning.md │                            │  release.md  │
│  Stages 6-7  │                            │  Stage 10    │
└──────┬───────┘                            └──────────────┘
       │                                           ▲
       │                                           │
       ▼                                           │
┌─────────────────────────────────────────────────────────────────┐
│                    PARALLEL EXECUTION (Stage 8-9)                │
│                                                                  │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐       ┌─────────┐       │
│  │Agent 1  │  │Agent 2  │  │Agent 3  │  ...  │Agent 10 │       │
│  │BlueLake │  │GreenCastle│ │RedStone │       │PurpleBear│      │
│  │Track A  │  │Track B  │  │Track C  │       │Track J  │       │
│  │bd-101   │  │bd-201   │  │bd-301   │       │bd-401   │       │
│  └────┬────┘  └────┬────┘  └────┬────┘       └────┬────┘       │
│       │            │            │                  │            │
│       └────────────┴────────────┴──────────────────┘            │
│                              │                                   │
│                    Agent Mail Coordination                       │
│              (File reservations, [CLAIMED], [CLOSED])            │
│                              │                                   │
│                    ┌─────────┴─────────┐                        │
│                    │   CALIBRATION     │                        │
│                    │  (Phase boundary) │                        │
│                    └───────────────────┘                        │
└─────────────────────────────────────────────────────────────────┘
```

## Subagents

| Subagent | Stages | Input | Output |
|----------|--------|-------|--------|
| `agents/northstar.md` | 0 | user intent | North Star Card |
| `agents/requirements.md` | 1-2 | North Star | REQ/AC (QA'd) |
| `agents/decisions.md` | 3-5 | requirements | ADRs + spikes |
| `agents/planning.md` | 6-7 | decisions | phases + beads |
| `agents/parallel-coordinator.md` | 8 | beads | spawns 10+ agents |
| `agents/execution.md` | 8 | per-agent | implements assigned beads |
| `agents/calibration.md` | 9 | all agents done | phase boundary check |
| `agents/release.md` | 10 | execution | release checklist |

---

## Parallel Execution (Stage 8)

Stage 8 is where 10+ Claude Code instances work simultaneously on parallel work tracks.

### How It Works

```
1. TRACK IDENTIFICATION
   ├── BV identifies parallel tracks: bv --robot-triage-by-track
   ├── Beads with no blocking dependencies between them → parallel
   └── Example: Track A (auth), Track B (API), Track C (UI) can run together

2. AGENT SPAWNING
   ├── Spawn N Claude Code instances (default: 10, configurable)
   ├── Each gets: project_path, track_assignment, agent_name
   └── Each runs /prime to register with Agent Mail

3. WORK DISTRIBUTION
   ├── Each agent claims beads from their assigned track
   ├── Agent Mail prevents conflicts via file reservations
   └── Agents work independently until track complete

4. PHASE SYNCHRONIZATION
   ├── All agents must complete their track before calibration
   ├── Coordinator monitors via Agent Mail inbox
   └── Calibration runs when all tracks report DONE

5. NEXT PHASE
   ├── After calibration passes, reassign tracks for next phase
   └── Repeat until all phases complete
```

### Track Assignment Strategy

```markdown
## Phase 1: Core Auth (24 beads, 10 agents)

| Track | Agent | Beads | Files |
|-------|-------|-------|-------|
| A: JWT | BlueLake | bd-101, bd-102 | src/auth/jwt/** |
| B: Sessions | GreenCastle | bd-103, bd-104 | src/auth/session/** |
| C: Middleware | RedStone | bd-105, bd-106 | src/middleware/** |
| D: Models | PurpleBear | bd-107 | src/models/** |
| E: Tests (JWT) | OrangeFox | bd-108, bd-109 | tests/auth/jwt/** |
| F: Tests (Session) | YellowBird | bd-110, bd-111 | tests/auth/session/** |
| G: Integration | SilverWolf | bd-112 | tests/integration/** |
| H: Docs | GoldEagle | bd-113 | docs/** |
| I: Config | BronzeTiger | bd-114 | config/** |
| J: DevOps | CopperSnake | bd-115 | .github/**, docker/** |
```

### Coordination Protocol

Each parallel agent follows this loop:

```
while track_has_work:
    1. /next-bead (claims from assigned track)
    2. Work on bead (TDD, implement, test, ubs)
    3. Close bead
    4. Check inbox for coordination messages
    5. Repeat

when track_complete:
    1. Send "[TRACK COMPLETE] Track A" to coordinator
    2. Wait for calibration or next assignment
```

### Agent Mail Messages

```python
# Agent completing a track
send_message(
    to=["Coordinator"],
    subject="[TRACK COMPLETE] Track A - Auth JWT",
    body_md="All beads in Track A closed. Waiting for calibration.",
    importance="high"
)

# Coordinator detecting phase complete
send_message(
    to=[ALL_AGENTS],
    subject="[PHASE COMPLETE] Phase 1 - Starting Calibration",
    body_md="All tracks complete. Calibration beginning. Stand by.",
    importance="high"
)

# After calibration
send_message(
    to=[ALL_AGENTS],
    subject="[NEXT PHASE] Phase 2 - New Track Assignments",
    body_md="Calibration passed. New assignments attached.",
    importance="high"
)
```

### Spawning Agents

The coordinator spawns agents using Claude Code's Task tool:

```python
# Spawn 10 parallel agents
for i, track in enumerate(tracks[:10]):
    Task(
        description=f"Execute Track {track.name}",
        prompt=f"""
You are Agent {i+1} for the full-pipeline execution.

Your assignment:
- Track: {track.name}
- Beads: {track.beads}
- Files: {track.files}

Instructions:
1. Run /prime to register
2. Claim and complete all beads in your track
3. When done, send [TRACK COMPLETE] to Coordinator
4. Wait for next assignment

Constraints:
- ONLY work on your assigned track
- NEVER touch files outside your track
- Check inbox between beads for coordination
""",
        subagent_type="general-purpose",
        run_in_background=True
    )
```

---

## Execution Flow

### 1. Setup (Orchestrator)

```markdown
1. Create session directory:
   mkdir -p sessions/pipeline-{timestamp}

2. Initialize TodoWrite with stages:
   - [ ] Stage 0: North Star
   - [ ] Stage 1-2: Requirements
   - [ ] Stage 3-5: Decisions
   - [ ] Stage 6-7: Planning
   - [ ] Stage 8-9: Execution
   - [ ] Stage 10: Release

3. Gather initial input:
   - user_intent: What does the user want to build?
```

### 2. Stage 0: North Star

**Spawn:** `agents/northstar.md`

**Input:**
```json
{
  "session_dir": "sessions/pipeline-{timestamp}",
  "user_intent": "Build a user authentication system with SSO"
}
```

**Output:**
```json
{
  "north_star_path": "PLAN/00_north_star.md",
  "mission": "Secure, scalable auth with SSO support",
  "success_criteria": ["SSO login works", "10k concurrent users", "Sub-100ms latency"]
}
```

**USER GATE:** Review and approve North Star before proceeding.

### 3. Stages 1-2: Requirements

**Spawn:** `agents/requirements.md`

**Input:**
```json
{
  "session_dir": "sessions/pipeline-{timestamp}",
  "north_star_path": "PLAN/00_north_star.md"
}
```

**Output:**
```json
{
  "requirements_path": "PLAN/01_requirements.md",
  "req_count": 12,
  "ac_count": 28,
  "qa_passed": true,
  "ambiguities_resolved": 3
}
```

**USER GATE:** Review requirements before decisions.

### 4. Stages 3-5: Decisions

**Spawn:** `agents/decisions.md`

**Input:**
```json
{
  "session_dir": "sessions/pipeline-{timestamp}",
  "requirements_path": "PLAN/01_requirements.md",
  "north_star_path": "PLAN/00_north_star.md"
}
```

**Output:**
```json
{
  "decisions_path": "PLAN/02_decisions_adrs.md",
  "adr_count": 4,
  "spikes_completed": 2,
  "risks_identified": 3,
  "risks_mitigated": 2
}
```

**USER GATE:** Review ADRs and spike results.

### 5. Stages 6-7: Planning

**Spawn:** `agents/planning.md`

**Input:**
```json
{
  "session_dir": "sessions/pipeline-{timestamp}",
  "requirements_path": "PLAN/01_requirements.md",
  "decisions_path": "PLAN/02_decisions_adrs.md"
}
```

**Output:**
```json
{
  "phases_path": "PLAN/03_phases.md",
  "phase_count": 4,
  "beads_created": 24,
  "dependency_graph": "valid",
  "calibration_points": [1, 2, 4]
}
```

**USER GATE:** Review phase structure and bead breakdown.

### 6. Stages 8-9: Execution

**Spawn:** `agents/execution.md`

**Input:**
```json
{
  "session_dir": "sessions/pipeline-{timestamp}",
  "phases_path": "PLAN/03_phases.md",
  "beads_path": ".beads/issues.jsonl"
}
```

**Output:**
```json
{
  "phases_completed": 4,
  "beads_closed": 24,
  "calibrations_passed": 3,
  "test_coverage": "94%",
  "security_clean": true
}
```

### 7. Stage 10: Release

**Spawn:** `agents/release.md`

**Input:**
```json
{
  "session_dir": "sessions/pipeline-{timestamp}",
  "execution_summary": "<from Stage 8-9>"
}
```

**Output:**
```json
{
  "release_checklist_path": "PLAN/04_release.md",
  "all_p0_verified": true,
  "traceability_complete": true,
  "ready_to_ship": true
}
```

### 8. Finalize (Orchestrator)

1. Update TodoWrite (all stages complete)
2. Present final summary to user
3. Archive session artifacts

---

## User Gates

The pipeline pauses for user approval at these points:

| After | Gate | User Reviews |
|-------|------|--------------|
| Stage 0 | North Star | Mission and success criteria |
| Stage 2 | Requirements | REQ/AC completeness |
| Stage 5 | Decisions | ADRs and spike results |
| Stage 7 | Planning | Phase structure and beads |
| Stage 10 | Release | Final checklist |

**If user rejects:** Return to relevant stage with feedback.

---

## Research Backing

| Stage | Research |
|-------|----------|
| 0 | North Star prevents drift (`PHILOSOPHY.md`) |
| 1-2 | Requirements quality is decisive (`research/033-requirements-to-code.md`) |
| 3-5 | 76.5% success vs 43.6% with proper search (`research/019-plansearch.md`) |
| 6-7 | Lossless decomposition prevents context bombing |
| 8-9 | TDD +45.97% success (`research/054-tdd-ai-code-gen.md`) |
| 9 | Tests adjudicate (`research/041-debatecoder.md`) |
| 10 | Evidence-based verification (`PHILOSOPHY.md`) |

---

## See Also

- `agents/` — Subagent definitions
- `docs/workflow/EVIDENCE_BASED_GUIDE.md` — Full pipeline reference
- `docs/workflow/PLANNING_DEEP_DIVE.md` — Detailed stage guide
- `docs/guides/ORCHESTRATOR_SUBAGENT_PATTERN.md` — Pattern documentation
