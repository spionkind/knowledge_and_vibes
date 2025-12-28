# Knowledge & Vibes — Visual + Editing Notes (20‑min Deep Dive)

## Style Guide (recommended)

- Visual rhythm: alternate between (1) talking head, (2) repo screen captures, (3) simple motion graphics for key ideas.
- On-screen text: short, high-contrast phrases; avoid paragraphs.
- Rule: when you mention a file path, show it on screen for 2–3 seconds.

## Chapter Cards (suggested)

1) “Why AI projects collapse”  
2) “Truth lives outside the model”  
3) “Repo map”  
4) “The pipeline”  
5) “Tools + commands”  
6) “Walkthrough”  
7) “How to start”

## Key On‑Screen Pull Quotes (use as lower thirds)

- “Truth lives outside the model.”  
- “Gaps become assumptions. Assumptions become architecture.”  
- “Lossless means no guessing.”  
- “Tests adjudicate, not rhetoric.”  
- “Three tries, then decompose.”

## Repo Screen Captures (in order)

### 1) What this is
- `README.md` (title + “research-backed framework” line)
- Mermaid workflow diagram in `README.md` (quick flash to establish scope)

### 2) Reading order / mental model
- `START_HERE.md` (reading order table)
- “What a session looks like” snippet in `START_HERE.md`

### 3) Pipeline overview
- `docs/workflow/IDEATION_TO_PRODUCTION.md` (the 11-stage pipeline block)
- `docs/workflow/PROTOCOLS.md` (show Table of Contents or protocol summary table)

### 4) Discovery and planning
- `docs/workflow/DISCOVERY.md` (show “Plan is complete when there’s nothing left to interpret”)
- `docs/workflow/PLANNING_DEEP_DIVE.md` (show Plan Pack layout)

### 5) Templates (artifacts)
- `TEMPLATES.md` (the “How templates fit together” diagram)
- `templates/NORTH_STAR_CARD_TEMPLATE.md`
- `templates/REQUIREMENTS_TEMPLATE.md`
- `templates/DECISIONS_ADRS_TEMPLATE.md`
- `templates/RISKS_AND_SPIKES_TEMPLATE.md`
- `templates/TRACEABILITY_TEMPLATE.md`

### 6) Decomposition and beads
- `docs/workflow/DECOMPOSITION.md` (hierarchy: plan → phases → beads)
- `.claude/templates/beads/bead-structure.md` (show “Tests FIRST” section)

### 7) Tool stack / operations
- `docs/guides/TUTORIAL.md` (show the "what you do vs what agent does" framing, tool list, bead lifecycle)

### 8) Slash commands (Claude Code)
- `.claude/commands/prime.md` (quick flash)
- `.claude/commands/next-bead.md` (quick flash)
- `.claude/commands/calibrate.md` (quick flash)
- `.claude/commands/release.md` (quick flash)

### 9) Multi-agent + safety rules (quick but memorable)
- `.claude/rules/multi-agent.md` (show `[CLAIMED]` / `[CLOSED]` subject patterns)
- `.claude/rules/safety.md` (show “Never delete files without permission”)

### 10) “Map of the repo” payoff
- `docs/REPO_TOUR.md` (scroll briefly; show it exists as a meta guide)

## Motion Graphic Ideas (simple)

- “Compression trap” graphic: High‑definition idea → tiny prompt → AI fills gaps → assumptions.
- “Truth outside the model” graphic: model output (hypothesis) vs tests/build/docs (truth).
- “3 tries” graphic: Attempt 1 / 2 / 3 → stop → decompose (ADaPT).
- “Multi-agent” graphic: two agents + file lock preventing collision.

## Call‑To‑Action (end screen)

- “Start: `START_HERE.md`”
- “Copy: `templates/NORTH_STAR_CARD_TEMPLATE.md`”
- "Workflow: `docs/workflow/IDEATION_TO_PRODUCTION.md`"

