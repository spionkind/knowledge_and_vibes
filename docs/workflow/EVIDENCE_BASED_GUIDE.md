# Evidence-Based Guide: The Complete Pipeline

The operational manual for Knowledge & Vibes—a gated, artifact-driven pipeline that maximizes the probability of correct outcomes.

**Evidence-based means:** Every stage is justified by research. Every gate exists because skipping it causes predictable failures.

---

## Table of Contents

- [The 2025 Reality](#the-2025-reality-why-this-pipeline-exists)
- [The Five Principles](#the-five-principles-that-shape-everything)
- [Roles: Operator vs Agents](#roles-who-does-what)
- [The Tool Stack](#the-tool-stack)
- [The 10-Stage Pipeline](#the-10-stage-pipeline)
  - [Stage 0: North Star](#stage-0--north-star-ground-truth)
  - [Stage 1: REQ/AC](#stage-1--requirements-that-compile-reqac)
  - [Stage 2: Requirements QA](#stage-2--requirements-qa-make-ambiguity-expensive)
  - [Stage 3: Decision Search](#stage-3--decision-search-options-then-select)
  - [Stage 4: Risks & Spikes](#stage-4--risks--spikes-collapse-uncertainty)
  - [Stage 5: Plan Pack](#stage-5--plan-pack-lossless-specs)
  - [Stage 6: Phase Breakdown](#stage-6--phase-breakdown-short-context)
  - [Stage 7: Bead Decomposition](#stage-7--bead-decomposition-tdd-first-adaptive)
  - [Stage 8: Execution Loops](#stage-8--execution-loops-generate--run--repair)
  - [Stage 9: Calibration](#stage-9--calibration-hard-stop-between-phases)
  - [Stage 10: Release Readiness](#stage-10--release-readiness-ship-with-confidence)
- [What To Read Next](#what-to-read-next)

---

## The 2025 Reality (Why This Pipeline Exists)

The research is clear about the current state of AI-assisted development:

| Finding | Number | Implication |
|---------|--------|-------------|
| Best models solve realistic tasks | ~23% | Don't assume success; verify everything |
| Experienced devs slower with AI on unfamiliar code | 19% | Human verification required, not optional |
| LLM code with security vulnerabilities | ~40% | Security scanning is mandatory |
| TDD improvement over non-TDD | 45.97% | Tests FIRST is the highest-impact practice |

This pipeline exists because:
- Single prompts fail 77% of the time on realistic tasks
- Confidence in AI output correlates poorly with correctness
- Security degrades with repeated self-correction
- Long context causes silent omission of requirements

The solution isn't better prompts. It's a workflow where failures get caught before they matter.

---

## The Five Principles That Shape Everything

### 1. Truth Lives Outside the Model

The AI's confident output is not truth. Truth is:
- Tests that pass or fail
- Code that compiles or doesn't
- Documentation that exists or doesn't
- Measurements you can observe

**Implication:** Every claim that matters must be verified, not trusted.

**Evidence:** `research/008-api-hallucination.md`, `research/022-chatrepair.md`

### 2. Planning is Search + Selection

Don't bet on one plan. Generate multiple candidates, then select using evidence.

**Implication:** Stages 3-5 produce options before committing.

**Evidence:** `research/019-plansearch.md`, `research/020-codetree.md`

### 3. Tests Adjudicate Disagreements

When agents disagree, the answer is not more debate. Voting alone beats extended rhetorical debate.

**Implication:** Write discriminating tests, run them, let results decide.

**Evidence:** `research/003-debate-or-vote.md`, `research/041-debatecoder.md`

### 4. Minimal Plans Beat Massive Plans

> "The smallest set of high-signal tokens that enables correct behavior." — Anthropic

**Implication:** Plan size matches project complexity. "Lossless" = no guessing, not "huge."

**Evidence:** `research/004-context-length-hurts.md`, `research/057-anthropic-context-engineering.md`

### 5. Decompose When Reality Demands It

Don't pre-decompose "just in case." Start coarse, split only when execution fails.

**Implication:** ADaPT pattern in Stage 7-8.

**Evidence:** `research/038-adapt.md`, `research/011-agentless.md`

---

## Roles: Who Does What

### Operator (You)

You do **value decisions** and **gate enforcement**:

| Your Responsibility | Why It's Yours |
|---------------------|----------------|
| Define goals, stakes, priorities (North Star) | Only you know what success means for your context |
| Answer clarifying questions about intent | Only you know what you actually want |
| Choose between A/B/C options | Only you can make value tradeoffs |
| Enforce "no tests = not done" | This is the core quality gate |
| Approve plan changes during calibration | Drift must be intentional, not accidental |

You do NOT need to: validate code, review implementations, debug technical problems, or decide architecture.

### Agents

Agents do **technical work + evidence production**:

| Agent Responsibility | Why Agents |
|----------------------|------------|
| Convert intent to `REQ-*` / `AC-*` | Technical translation |
| Ground claims (Warp-Grep, Exa) | Access to verification tools |
| Implement in verifiable beads | Technical execution |
| Run verification loops | Automated checking |
| Coordinate via Agent Mail | Multi-agent orchestration |
| Maintain traceability | Coverage tracking |

---

## The Tool Stack

Each tool addresses a specific failure mode:

| Tool | Command | Addresses |
|------|---------|-----------|
| **Beads** | `bd` | Work tracking, dependency management |
| **BV** | `bv --robot-*` | Execution ordering, blocker detection |
| **Agent Mail** | MCP tools | Multi-agent coordination, file reservations |
| **Warp-Grep** | MCP tool | Codebase truth (reduces hallucination) |
| **Exa** | MCP tool | Web truth (current docs, APIs) |
| **UBS** | `ubs --staged` | Security scanning (mandatory) |
| **CASS/cm** | `cass`, `cm` | History, learned patterns |

**For detailed tool usage, what happens behind the scenes, and multi-agent coordination:** See `docs/guides/TOOL_STACK_AND_OPERATIONS.md`

---

## The 10-Stage Pipeline

### Overview

```
Stage 0: North Star        → What are we building? Why?
Stage 1: REQ/AC            → What must be true when done?
Stage 2: Requirements QA   → Is it unambiguous?
Stage 3: Decision Search   → What are the options?
Stage 4: Risks & Spikes    → What could go wrong?
Stage 5: Plan Pack         → Complete spec for execution
Stage 6: Phase Breakdown   → Manageable chunks
Stage 7: Bead Decomposition → Executable tasks
Stage 8: Execution         → Build with verification
Stage 9: Calibration       → Check and correct
Stage 10: Release          → Ship with confidence
```

**Critical rule:** Don't skip stages. The gates exist because skipping them causes predictable failures.

---

### Stage 0 — North Star (Ground Truth)

**Purpose:** Establish what we're building and why before anyone writes code.

**Artifact:** `templates/NORTH_STAR_CARD_TEMPLATE.md` pinned at top of plan.

**Must include:**
- Success metrics (how will you know it worked?)
- Stakes (what happens if it fails?)
- Non-goals (what are we explicitly NOT doing?)
- Stop/ask rule (when should agents pause for human input?)

**Gate:** Card is explicit enough that agents can resolve tradeoffs without guessing.

**Why this matters:** Without explicit goals, agents optimize for whatever seems reasonable. "Reasonable" often isn't what you wanted.

---

### Stage 1 — Requirements That "Compile" (REQ/AC)

**Purpose:** Convert intent into testable requirements.

**Artifact:** `PLAN/01_requirements.md` with:
- `REQ-*` — Observable outcomes or constraints
- `AC-*` — Acceptance criteria (ideally test-shaped)
- Priority (P0/P1/P2)

**Template:** `templates/REQUIREMENTS_TEMPLATE.md`

**Gate:** Every P0 requirement has at least one falsifiable AC.

**Why this matters:** "Correct" must be checkable by tests, not vibes. If you can't test it, it's not a requirement—it's a wish.

**Evidence:** `research/032-tdd-code-generation.md`, `research/033-requirements-to-code.md`

---

### Stage 2 — Requirements QA (Make Ambiguity Expensive)

**Purpose:** Eliminate ambiguity before it becomes expensive rework.

**Artifact:** Updated requirements with:
- Ambiguous requirements rewritten
- Missing constraints added
- Inconsistent requirements resolved

**Template:** `templates/REQUIREMENTS_QA_TEMPLATE.md`

**Gate:** No P0 requirement remains ambiguous or untestable.

**Why this matters:** Ambiguity in requirements becomes divergent implementations. Fix it early when it's cheap.

**Evidence:** `research/036-requirements-qa-iso-29148.md`

---

### Stage 3 — Decision Search (Options, Then Select)

**Purpose:** Don't bet on one approach. Generate options, then select with evidence.

**Artifact:** `PLAN/02_decisions_adrs.md` with ADRs containing:
- Options A/B/C
- Tradeoffs for each
- Risks
- "What would change our mind" (reversal triggers)

**Template:** `templates/DECISIONS_ADRS_TEMPLATE.md`

**Gate:** Every architecturally significant requirement is decided or explicitly "TBD pending spike."

**Why this matters:** Single-path planning is fragile. Search over diverse plans improves outcomes.

**Evidence:** `research/019-plansearch.md`, `research/020-codetree.md`

---

### Stage 4 — Risks & Spikes (Collapse Uncertainty)

**Purpose:** Identify unknowns and resolve them before committing to a path.

**Artifact:** `PLAN/06_risks_and_spikes.md` with:
- Top risks/unknowns
- Spike beads that produce evidence
- Decision impact (which ADR does each spike unlock?)

**Template:** `templates/RISKS_AND_SPIKES_TEMPLATE.md`

**Gate:** High-risk unknowns are converted into spikes with explicit outputs.

**Why this matters:** Unknown unknowns kill projects. Spikes turn them into known knowns.

**Evidence:** `research/031-alphacodium.md`, `research/014-codeplan.md`

---

### Stage 5 — Plan Pack (Lossless Specs)

**Purpose:** Produce specs complete enough that implementation requires no guessing.

**Artifacts:**
- `PLAN/03_system_map.md`
- `PLAN/04_data_model.md`
- `PLAN/05_api_and_error_model.md`
- `PLAN/08_testing_spec.md`
- `PLAN/09_ops_security.md`
- `PLAN/10_dependencies_and_phases.md`

**Gate:** A competent engineer could implement without guessing.

**Important:** Plan size should match project complexity. Simple projects need simple plans. "Lossless" means no guessing, not "comprehensive."

**Evidence:** `research/033-requirements-to-code.md`, `research/057-anthropic-context-engineering.md`

---

### Stage 6 — Phase Breakdown (Short Context)

**Purpose:** Break the plan into chunks that fit in working memory without loss.

**Artifact:** Phase documents using `.claude/templates/planning/phase-document.md`

**Heuristic:** ~500-1000 lines per phase (not a hard rule—based on semantic coherence)

**Gate:** No phase is large enough to cause silent omission.

**Why this matters:** Long context causes 30-50% degradation in reasoning quality. Critical requirements get "lost in the middle."

**Evidence:** `research/004-context-length-hurts.md`, `research/005-lost-in-middle-code.md`

---

### Stage 7 — Bead Decomposition (TDD-First, Adaptive)

**Purpose:** Convert phases into executable tasks with built-in verification.

**Artifact:** Beads with:
- **Tests FIRST** (written before implementation)
- Edit locus (exactly what files/functions to change)
- REQ/AC linkage
- Verification plan

**Template:** `.claude/templates/beads/bead-structure.md`

**Command:** `/decompose-task [phase]`

**Gate:** Every bead has tests in the description before implementation begins.

**Key rules:**
- **TDD-first:** Tests before code (45.97% improvement)
- **Adaptive decomposition:** Start coarse, split only when execution fails

**Operations:**
```bash
# Decompose a phase into beads
/decompose-task [phase]

# Validate the dependency graph
bv --robot-suggest   # Missing deps, duplicates
bv --robot-plan      # Sane execution order?
bv --robot-alerts    # Drift signals, risky topology
```

**Why this matters:** TDD is the single highest-impact practice. Tests define "done" and enable verification.

**Evidence:** `research/054-tdd-ai-code-gen.md`, `research/038-adapt.md`

---

### Stage 8 — Execution Loops (Generate → Run → Repair)

**Purpose:** Implement with verification, not hope.

**Artifact per bead:**
- Code changes
- Tests added/updated
- Verification evidence (commands run, outputs)
- `ubs --staged` output

**Gate:** No bead closes without:
- All tests passing
- `ubs --staged` clean (no high/critical findings)

**Key rules:**
- **Max 3 repair iterations** — Security degrades with more
- **If still failing after 3:** STOP, spawn sub-bead for failing part, notify operator

**Operations:**
```bash
# Session startup (run once)
/prime                           # Register with Agent Mail, check inbox

# Find and claim work
/next-bead                       # Full discovery + claim flow
# or manually:
bd ready --json                  # What's available
bv --robot-next                  # Recommendation
bd update <id> --status in_progress --assignee YOUR_NAME

# During work
pytest                           # Run tests
ubs --staged                     # Security check (mandatory)

# Close work
bd close <id>.1 --reason "..."   # Close sub-beads FIRST
bd close <id> --reason "..."     # Then parent
# Agent Mail: release file reservations, send [CLOSED]
```

**Why this matters:** Unlimited self-correction makes code worse, not better. Fail fast, escalate early.

**Evidence:** `research/053-feedback-loop-security.md`, `research/022-chatrepair.md`

---

### Stage 9 — Calibration (Hard Stop Between Phases)

**Purpose:** Check for drift and correct course before continuing.

**Artifact:** Calibration decision memo + plan updates + change log

**Command:** `/calibrate [phase_or_milestone]`

**Gate:** No next phase begins until calibration produces falsifiable decisions.

**Key rules:**
- Disagreements must be resolved by **tests**, not rhetoric
- If tests don't discriminate, preserve both positions for human decision
- Update plan with any changes

**Operations:**
```bash
# Trigger calibration
/calibrate [phase]

# Behind the scenes:
# 1. Broadcasts analysis request to all agents via Agent Mail
# 2. Collects independent assessments
# 3. Challenges resolved by discriminating tests (not debate)
# 4. Produces decision memo and plan updates
# 5. Gates next phase

# Multi-agent: if disagreement
# - Write tests that BREAK the other approach if your concern is valid
# - Run tests against both proposals
# - Test results decide
```

**Why this matters:** Drift compounds. Small deviations early become major problems late.

**Evidence:** `research/003-debate-or-vote.md`, `research/041-debatecoder.md`

---

### Stage 10 — Release Readiness (Ship With Confidence)

**Purpose:** Ensure "done" means "actually shippable."

**Artifact:** Release checklist tied to rigor tier:
- All tests passing
- Security scan clean
- Observability in place
- Rollback plan documented

**Mandatory gates:**
- **P13 Security Gate:** `ubs --staged` clean
- **P14 Human Verification:** Operator sign-off on P0 implementations

**Gate:** System meets success metrics at chosen rigor tier.

**Reality check:** Strong benchmark scores don't guarantee robustness. Best models solve only ~23% of realistic tasks. Human review is not optional.

**Evidence:** `research/050-swe-bench-pro.md`, `research/051-metr-rct.md`

---

## What To Read Next

| If you want... | Read... |
|----------------|---------|
| Exact protocol checklists | `PROTOCOLS.md` |
| Deep planning tutorial | `PLANNING_DEEP_DIVE.md` |
| Decomposition mechanics | `DECOMPOSITION.md` |
| **Tool operations & multi-agent coordination** | `docs/guides/TOOL_STACK_AND_OPERATIONS.md` |
| Research summaries | `research/README.md` |
| Why this approach works | `PHILOSOPHY.md` |
