# Requirements (REQ/AC) Template

Use this after the North Star Card is pinned. Requirements are the operator-facing interface: **outcomes and constraints**, not solutions.

If you’re new to the repo, start with:
- `START_HERE.md`

Evidence-backed workflow context:
- `docs/workflow/EVIDENCE_BASED_GUIDE.md` (pipeline + gates)
- `docs/workflow/PROTOCOLS.md` (P1 / P2)

---

## Conventions

- `REQ-*` = observable requirement / outcome / constraint
- `AC-*` = acceptance criteria that proves the requirement is true (ideally “test-shaped”)
- Priority: `P0` / `P1` / `P2`
- Confidence labels for assumptions: `HIGH` / `MED` / `LOW`

Rules:
- If it can’t be falsified, it isn’t a requirement yet.
- If it changes architecture/security, it must be grounded or labeled as an assumption.
- Every `P0` `REQ-*` must have at least one measurable `AC-*`.

---

## Template

```markdown
# Requirements

## Scope
- Project:
- Date:
- Rigor tier:
- Owner of truth (who decides intent disputes):

## Glossary (Optional)
- Term:
- Term:

## Requirements List

### REQ-1 (P0): <short title>

Requirement (what must be true):
- <observable outcome or constraint>

Acceptance Criteria (proof it’s true):
- AC-1: <falsifiable check>
- AC-2: <falsifiable check>

Notes / Assumptions (must be labeled):
- ASSUMPTION (HIGH/MED/LOW): <...>

Dependencies / Integrations:
- <external system, API, policy, data source>

Non-Goals / Out of Scope (if specific to this REQ):
- <...>

### REQ-2 (P1): <short title>
...

## Open Questions (Stop/Ask List)
- Q1:
- Q2:
```

---

## Agent Prompt (Recommended)

Send this to a planning agent:

```markdown
You are drafting REQ/AC requirements.

Rules:
1) Requirements must be outcomes/constraints, not solutions.
2) Each P0 REQ must have at least one falsifiable AC.
3) Mark any non-trivial claim that depends on external truth as either grounded (cite) or ASSUMPTION (HIGH/MED/LOW).
4) If the correct answer depends on user intent, apply stop/ask and write the exact clarifying question(s).

Input:
- North Star Card: <paste>

Output:
- `REQ-*` list with `AC-*`
- open questions (operator confirmations needed)
```
