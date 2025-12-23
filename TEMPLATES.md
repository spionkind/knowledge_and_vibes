# Templates

Templates are the artifacts that make plans explicit and verifiable. Each template captures a specific type of decision or context that would otherwise be lost or assumed.

---

## How Templates Fit Together

```
North Star Card          What are we building? Why? What's out of scope?
       ↓
Requirements (REQ/AC)    What must be true when done? How will we test it?
       ↓
Decisions (ADRs)         Which approach did we choose? What were the alternatives?
       ↓
Risks & Spikes           What could go wrong? How will we reduce uncertainty?
       ↓
Decomposition            Phases → Beads → executable tasks with verification
       ↓
Traceability             REQ → Beads → Tests → Evidence (coverage map)
```

Each template feeds the next. Skip one and you're guessing.

---

## Operator-Facing Templates

These are filled out during planning, before implementation begins.

### North Star Card

**Purpose:** Anchor the entire project. Everything traces back to this.

**Use when:** Starting any project, no matter the size.

**Template:** [`templates/NORTH_STAR_CARD_TEMPLATE.md`](./templates/NORTH_STAR_CARD_TEMPLATE.md)

**Contains:**
- Goal (what success looks like)
- Success metrics (how you'll measure it)
- Rigor tier (how much process this project needs)
- Non-goals (what you're explicitly NOT building)
- Stop/ask rules (when the AI should pause for human input)

**Destination in your project:** `PLAN/00_north_star.md`

---

### Requirements (REQ/AC)

**Purpose:** Define what must be true in testable terms.

**Use when:** After North Star is set, before any implementation.

**Template:** [`templates/REQUIREMENTS_TEMPLATE.md`](./templates/REQUIREMENTS_TEMPLATE.md)

**Contains:**
- `REQ-*` — Observable outcomes or constraints
- `AC-*` — Acceptance criteria (test-shaped)
- Priority (P0 = must have, P1 = should have, P2 = nice to have)

**Destination:** `PLAN/01_requirements.md`

**Key rule:** If you can't test it, it's not a requirement—it's a wish.

---

### Requirements QA

**Purpose:** Eliminate ambiguity before it becomes expensive rework.

**Use when:** After drafting requirements, before finalizing.

**Template:** [`templates/REQUIREMENTS_QA_TEMPLATE.md`](./templates/REQUIREMENTS_QA_TEMPLATE.md)

**Contains:**
- Ambiguous requirements flagged
- Suggested rewrites
- Missing constraints identified
- Inconsistencies resolved

**Destination:** `PLAN/01_requirements_qa.md` (or inline in requirements doc)

---

### Decisions (ADRs)

**Purpose:** Record significant decisions so they're not relitigated.

**Use when:** Any decision that affects architecture, technology, or approach.

**Template:** [`templates/DECISIONS_ADRS_TEMPLATE.md`](./templates/DECISIONS_ADRS_TEMPLATE.md)

**Contains:**
- Decision title
- Options considered (A, B, C)
- Tradeoffs for each
- Decision made and rationale
- Reversal triggers (what would change our mind)

**Destination:** `PLAN/02_decisions_adrs.md`

---

### Risks & Spikes

**Purpose:** Identify unknowns and convert them into timeboxed investigations.

**Use when:** Before committing to a major approach.

**Template:** [`templates/RISKS_AND_SPIKES_TEMPLATE.md`](./templates/RISKS_AND_SPIKES_TEMPLATE.md)

**Contains:**
- Top risks/unknowns
- Spike tasks (evidence-producing investigations)
- Expected decision impact (which ADR does this unlock?)

**Destination:** `PLAN/06_risks_and_spikes.md`

---

### Traceability

**Purpose:** Maintain coverage from requirements through implementation.

**Use when:** Throughout implementation, updated as work completes.

**Template:** [`templates/TRACEABILITY_TEMPLATE.md`](./templates/TRACEABILITY_TEMPLATE.md)

**Contains:**
- North Star reference
- REQ → Beads mapping
- AC → Tests mapping
- Coverage gaps

**Destination:** `PLAN/traceability.md`

**Note:** This is agent-maintained. The operator shouldn't need to update it manually.

---

### CODEMAPS

**Purpose:** Orientation documents that help agents understand a codebase.

**Use when:** Working in an existing or complex codebase.

**Template:** [`templates/CODEMAPS_TEMPLATE.md`](./templates/CODEMAPS_TEMPLATE.md)

**Contains:**
- Area overview
- Key files and their purposes
- Conventions and patterns
- Dependencies and relationships

**Destination:** `CODEMAPS/<area>.md`

---

### AGENTS.md

**Purpose:** Project-specific instructions for AI agents.

**Use when:** Any project where agents will work.

**Template:** [`templates/AGENTS_TEMPLATE.md`](./templates/AGENTS_TEMPLATE.md)

**Contains:**
- Project context
- Coding conventions
- Safety rules
- Known gotchas

**Destination:** `AGENTS.md` (project root)

---

## Agent-Native Templates

These are used by slash commands during execution. They live in `.claude/templates/`.

### Bead Templates

Located in `.claude/templates/beads/`:

| Template | Used By | Purpose |
|----------|---------|---------|
| `bead-structure.md` | `/decompose-task` | Structure for new beads |
| `claimed-announcement.md` | `/next-bead` | [CLAIMED] message format |
| `closed-announcement.md` | Bead close | [CLOSED] message format |
| `verification-report.md` | Bead close | Evidence of completion |

### Planning Templates

Located in `.claude/templates/planning/`:

| Template | Used By | Purpose |
|----------|---------|---------|
| `phase-document.md` | Phase breakdown | Structure for phase specs |
| `sub-bead-structure.md` | ADaPT decomposition | When tasks need splitting |
| `audit-report.md` | Plan audits | Gap and risk analysis |

### Calibration Templates

Located in `.claude/templates/calibration/`:

| Template | Used By | Purpose |
|----------|---------|---------|
| `broadcast.md` | `/calibrate` | Request for agent assessments |
| `challenge-response.md` | Calibration | Test-based disagreement resolution |
| `decisions.md` | `/calibrate` | Recording calibration outcomes |
| `user-report.md` | `/calibrate` | Summary for operator |

---

## Using Templates in Your Project

### Option 1: Copy What You Need

```bash
# Copy a specific template
cp templates/NORTH_STAR_CARD_TEMPLATE.md your-project/PLAN/00_north_star.md
```

### Option 2: Reference and Fill

Open the template, copy its structure into your project file, and fill in the sections.

### Option 3: Full Slash Command Setup

Copy the entire `.claude/` directory to get all commands and agent-native templates:

```bash
cp -r .claude/ your-project/.claude/
```

---

## Further Reading

- **[Evidence-Based Guide](./docs/workflow/EVIDENCE_BASED_GUIDE.md)** — How templates fit into the 10-stage pipeline
- **[Protocols](./docs/workflow/PROTOCOLS.md)** — When each template gets used
- **[Planning Deep Dive](./docs/workflow/PLANNING_DEEP_DIVE.md)** — Tutorial on planning with these templates
