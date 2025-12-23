# Start Here

This page gives you the fastest path to understanding and using Knowledge & Vibes.

---

## The Problem This Solves

AI-assisted development fails in predictable ways:

| Failure Mode | Root Cause |
|--------------|------------|
| AI builds the wrong thing | Goals weren't explicit |
| Requirements disappear mid-project | Context window limits |
| Multiple agents conflict | No coordination protocol |
| Bugs compound silently | No verification gates |
| "Trust me, it works" | Confidence ≠ correctness |

The 2025 research confirms what practitioners already knew:
- Best models solve **23%** of realistic software tasks
- **40%** of AI code contains security vulnerabilities
- Extended self-correction **degrades** outcomes

This system exists because **the AI's confident output is not truth**. Truth is tests that pass, code that compiles, behavior you can observe. Everything else is hypothesis.

---

## The Solution in 60 Seconds

Knowledge & Vibes enforces a workflow where failures get caught before they matter:

1. **Plan explicitly** — North Star cards, requirements with acceptance criteria, recorded decisions
2. **Track everything** — Beads (tasks) with dependencies, status, verification requirements
3. **Coordinate agents** — File reservations, claim/close announcements, message routing
4. **Verify continuously** — Tests before code (TDD), security scans before commit, calibration between phases
5. **Bound iteration** — Max 3 repair attempts, then decompose or escalate

The result: structured AI development that produces working software, not plausible-sounding code.

---

## Reading Order

### Phase 1: Get Running

| Document | Goal |
|----------|------|
| **[Setup Guide](./docs/guides/SETUP_GUIDE.md)** | Install all tools, verify they work |
| **[Glossary](./GLOSSARY.md)** | Bookmark for when you hit unfamiliar terms |

After this, you can run `bd`, `bv --robot-next`, `ubs`, `cass`, and `cm`.

### Phase 2: Understand the System

| Document | Goal |
|----------|------|
| **[Evidence-Based Guide](./docs/workflow/EVIDENCE_BASED_GUIDE.md)** | See the complete 10-stage pipeline |
| **[Protocols](./docs/workflow/PROTOCOLS.md)** | Learn the 18 procedures that structure work |
| **[Philosophy](./docs/workflow/PHILOSOPHY.md)** | Understand why verification matters |

After this, you understand how the system prevents drift, catches errors, and coordinates multiple agents.

### Phase 3: Learn to Use It

| Document | Goal |
|----------|------|
| **[Tool Stack & Operations](./docs/guides/TOOL_STACK_AND_OPERATIONS.md)** | What each tool and command does |
| **[Tutorial](./docs/guides/TUTORIAL.md)** | Detailed walkthroughs with examples |

After this, you can run `/prime`, `/next-bead`, `/calibrate` and understand what happens under the hood.

### Phase 4: Deep Dives (As Needed)

| Document | When to Read |
|----------|--------------|
| **[Planning Deep Dive](./docs/workflow/PLANNING_DEEP_DIVE.md)** | Starting a new project from scratch |
| **[Decomposition](./docs/workflow/DECOMPOSITION.md)** | Breaking plans into executable tasks |
| **[Research](./research/README.md)** | Understanding why a protocol exists |

---

## If You Only Read 3 Things

1. **[Setup Guide](./docs/guides/SETUP_GUIDE.md)** — Get the tools working
2. **[Evidence-Based Guide](./docs/workflow/EVIDENCE_BASED_GUIDE.md)** — The complete pipeline
3. **[Protocols](./docs/workflow/PROTOCOLS.md)** — The exact moves to make

Everything else is reference material.

---

## The Core Principles

### 1. Truth Lives Outside the Model

AI output is not truth. Truth is:
- Tests that pass or fail
- Code that compiles or doesn't
- Documentation that exists or doesn't

Every claim must be verified, not trusted.

### 2. Tests Adjudicate, Not Rhetoric

When agents disagree, write tests that distinguish the approaches. Run the tests. Let results decide.

Research shows extended debate degrades outcomes. Tests are the tiebreaker.

### 3. Decompose When Reality Demands It

Don't pre-plan everything. Start with coarse tasks (beads). Attempt execution. If it fails after 3 tries, *then* decompose—only the failing part.

### 4. Minimal Viable Planning

A 200-line script doesn't need a 50-page plan. Match plan size to project complexity.

"Lossless" means no guessing required—not "exhaustively long."

---

## What a Session Looks Like

```bash
# Start session
/prime                      # Register, check inbox, discover tasks

# Claim work
/next-bead                  # Find task, reserve files, announce [CLAIMED]

# Implement (TDD-first)
pytest                      # Run tests (expect red)
# ... write implementation ...
pytest                      # Run tests (expect green)
ubs --staged                # Security scan (mandatory)

# Close work
git add -A && git commit
bd close <id> --reason "..."
# Agent releases files, sends [CLOSED]

# Between phases
/calibrate                  # Hard stop, check for drift
```

---

## Quick Links

| I want to... | Go to... |
|--------------|----------|
| Install everything | **[Setup Guide](./docs/guides/SETUP_GUIDE.md)** |
| Look up a term | **[Glossary](./GLOSSARY.md)** |
| See all templates | **[TEMPLATES.md](./TEMPLATES.md)** |
| Understand the research | **[Research](./research/README.md)** |
| Start a new project | **[Setup Guide](./docs/guides/SETUP_GUIDE.md)** → **[North Star Template](./templates/NORTH_STAR_CARD_TEMPLATE.md)** |
| Migrate an existing project | **[Migration Guide](./docs/guides/MIGRATION_GUIDE.md)** |
