# Risks & Spikes (Template)

Use this to collapse uncertainty **before** you commit to architecture or long sequences of implementation beads.

The output is a list of **spike beads** whose job is to produce evidence (docs, prototypes, measurements) that unlocks decisions.

Evidence base:
- Flow engineering + execution feedback loops: `research/031-alphacodium.md`, `research/032-tdd-code-generation.md`
- Adaptive planning / derived obligations: `research/014-codeplan.md`
- “Requirements first” reduces downstream guesswork: `research/033-requirements-to-code.md`

---

## Template

```markdown
# Risks & Spikes

## Scope
- Project:
- Date:
- Rigor tier:
- Owner:

## Top Risks / Unknowns

List the top uncertainties that could cause rework, failure, or major cost.

| ID | Risk / Unknown | Why It Matters | Likelihood | Impact | Evidence Needed | Decision Unblocked |
|----|----------------|----------------|------------|--------|-----------------|-------------------|
| RISK-1 | ... | ... | L/M/H | L/M/H | docs / spike / benchmark | ADR-? |

## Spike Beads

Each spike must have explicit outputs and a “done” definition.

| Spike | Goal | Inputs | Steps | Outputs (Evidence) | Timebox | Owner |
|------|------|--------|-------|---------------------|---------|-------|
| SPIKE-1 | Prove X works | repo + docs | 1) … 2) … | links, logs, prototype, numbers | 1–4h | Agent |

## Rules
- A spike is not a feature. It is evidence.
- Spikes may be thrown away; keep outputs and conclusions.
- Spikes must end with one of:
  - ✅ Decision can be made
  - ⚠️ Decision still ambiguous (explain what’s missing)
  - ❌ Approach rejected (why)

## Integration With Plan
- Update ADRs based on spike outcomes
- Convert confirmed work into normal beads
- Schedule a `/calibrate` after the spike sprint
```

