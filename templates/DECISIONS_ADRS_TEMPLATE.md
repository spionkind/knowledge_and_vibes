# Decisions / ADRs (Template)

Use this to record architecturally significant decisions so agents don’t silently pick defaults.

New to the repo? Start with:
- `START_HERE.md`

Evidence-backed workflow context:
- `docs/workflow/EVIDENCE_BASED_GUIDE.md` (Stage 3: decision search)
- `docs/workflow/PROTOCOLS.md` (P4)

---

## Conventions

- ADR IDs: `ADR-001`, `ADR-002`, …
- Status: `proposed` → `accepted` → `superseded`
- Every ADR should include:
  - A/B/C options
  - tradeoffs grounded in the North Star priority order
  - “what would change our mind” (reversal triggers)
  - verification hooks (tests/experiments) when possible

---

## Template

```markdown
# Decisions / ADR Log

## ADR-001: <title>

Status: proposed / accepted / superseded
Date:
Owner:

Context (what problem are we solving?):
- <constraints, assumptions, relevant REQ/AC>

Decision (what we chose):
- <choice>

Options (A/B/C):

| Option | Summary | Pros | Cons | Risks | Complexity | Notes |
|--------|---------|------|------|-------|------------|-------|
| A | ... | ... | ... | ... | low/med/high | ... |
| B | ... | ... | ... | ... | low/med/high | ... |
| C | ... | ... | ... | ... | low/med/high | ... |

Rationale (why this choice wins under the North Star):
- <tie to priority order + context/stakes>

Consequences (what this implies downstream):
- <what changes in design, testing, ops, cost, maintenance>

Reversal Triggers (what evidence would make us change course?):
- <metric, test failure, spike result, scale threshold, security finding>

Verification Hooks (how we prove it works):
- <tests, experiments, benchmarks, grounded doc links>

Open Questions / Follow-ups:
- <spikes to run, unknowns to resolve>
```

---

## Agent Prompt (Recommended)

```markdown
We need an ADR. Provide A/B/C options and help us select using the North Star.

Rules:
1) Don’t argue by rhetoric. Ground facts or label assumptions (HIGH/MED/LOW).
2) Tie tradeoffs to the North Star priority order.
3) Provide reversal triggers and verification hooks (tests/experiments).
4) If the right answer depends on user intent, apply stop/ask and write the exact question(s).

Input:
- North Star Card: <paste>
- Relevant REQ/AC: <paste>
- Decision to make: <paste>

Output:
- ADR entry in the template format
```
