# North Star Card (Template)

Use this template at the very top of your master plan. It is the anchor for:
- requirements (`REQ-*` / `AC-*`)
- architectural decisions (ADRs)
- phase breakdown + bead decomposition
- calibration (`/calibrate`) checkpoints

If the North Star is vague, agents will drift.

---

## Build Profile Presets (Pick One)

This is the fastest way to make your intent “honest” to the system. The same feature can be built with very different rigor depending on why you’re building it.

| Preset | Typical context | Default rigor tier | What “good” looks like |
|--------|------------------|--------------------|------------------------|
| Personal / Hobby | Solo, low stakes, learning | 1 | Fast iteration, minimal architecture, smoke tests on core flows |
| Startup MVP | Early product, speed with guardrails | 2 | Critical-path tests, clear boundaries, pragmatic security |
| Internal Tool (Business-Critical) | Used by a team/company; real impact | 2–3 | Strong correctness on workflows, integration tests, observability, access control |
| Enterprise / Regulated | Compliance/audit; high stakes | 3 | Traceability, threat modeling, hardened ops, formal change control |

---

## Rigor Tiers (Pick 1–3)

| Tier | Focus | Minimum bar |
|------|-------|-------------|
| 1 (Speed-First) | Learn fast, ship quickly | Smoke tests + basic sanity checks for critical paths |
| 2 (Balanced) | Build right without over-process | Unit + integration on critical paths, ADRs for major decisions |
| 3 (High Assurance) | Correctness, security, auditability | Full test matrix for P0s, threat model, observability, traceability |

---

## Template

```markdown
## North Star Card
- Desired end state (one sentence, concrete):
- Primary user + core problem:
- Context & stakes (e.g., F500 internal tool, regulated, public SaaS, personal hobby):
- Build profile preset (choose one, and why):
- Success metrics (observable, ranked):
- Rigor tier (1-3) + rationale:
- Maintenance horizon (weeks/months/years):
- Risk tolerance (low/med/high):
- Non-goals (explicitly out of scope):
- Must-not-violate invariants (hard constraints):
- Priority order for decisions (e.g., Safety > Correctness > UX > Speed):
- Constraints (time, budget, tech, compliance):
- Source of truth (docs/owner of truth):
- Stop/ask rule (when to pause and ask user):
- Open questions (clarifiers outstanding):
```

---

## Notes

- “Build profile preset” and “Rigor tier” drive the minimum bar for testing, architecture, and operational discipline.
- “Stop/ask rule” is mandatory: it prevents silent guessing when the correct answer depends on user intent.
