# Traceability Matrix (Template)

**Purpose:** Maintain a single, explicit map from the North Star to phases, beads, tests, and acceptance criteria. This prevents drift and makes gaps obvious.

**Agent-native workflow:** Agents update this file during decomposition, implementation, and calibration. The user is not expected to manage it.

**Why this matters:** Without explicit traceability, requirements get "lost in the middle" as context grows. A single coverage map catches gaps before they become bugs.

---

## Conventions

- **IDs:** `NS-#` (North Star items), `REQ-#` (requirements), `AC-#` (acceptance criteria)
- **Beads:** use bead IDs (e.g., `bd-123.2`)
- **Tests:** use file paths or test identifiers
- **Status:** `planned` → `in_progress` → `code_done` → `tests_done` → `accepted`
- **Evidence:** test runs, file paths, commits, or calibration summary links

---

## Traceability Matrix

| ID | Requirement | Phase | Beads | Tests | Acceptance | Status | Evidence |
|----|-------------|-------|-------|-------|------------|--------|----------|
| NS-1 | [North Star bullet] | Phase 0 | plan.0.1 | [tests] | AC-1 | planned | [link] |
| REQ-3 | [Requirement text] | Phase 2 | bd-123.2 | tests/auth_sso.py | AC-7 | tests_done | run: #127 |

---

## When to Update

| Trigger | Action |
|---------|--------|
| **After `/decompose-task`** | Add bead IDs to REQ rows |
| **After creating tests** | Add test paths to bead rows |
| **After closing a bead** | Update Status + Evidence |
| **During `/calibrate`** | Scan for gaps (see below) |
| **After requirements change** | Add new rows, mark old as deprecated |

---

## Workflow (Agent Use)

1. **Planning:** Add rows for each North Star bullet and requirement.
2. **Decomposition:** Assign trace IDs to beads and fill the **Beads** column.
3. **Implementation:** Fill the **Tests** column with test identifiers (file path + test name where helpful).
4. **Bead Close:** Update **Status** and **Evidence**.
5. **Calibration:** Scan for gaps (no beads, no tests, missing acceptance).

---

## Common Drift Patterns (Check During Calibration)

| Pattern | Symptom | Fix |
|---------|---------|-----|
| **Orphan requirement** | REQ with no beads | Create bead or mark REQ as deferred |
| **Untested bead** | Bead with no tests | Add tests before closing |
| **Unverified AC** | AC with no evidence | Run verification, add evidence |
| **Scope creep** | Bead not linked to any REQ | Either link to REQ or question if needed |
| **Stale status** | Status says "in_progress" but work finished | Update status + evidence |
| **Missing P0 coverage** | P0 REQ without `accepted` status | Block release until verified |

---

## Trace Tagging Examples

Trace tags are optional. They can make future automation easier (e.g., auto‑generating a trace report by scanning tests), but the traceability matrix itself is the source of truth.

**Bead description:**
```
Trace: REQ-3, REQ-5
```

**Test comment:**
```
# Trace: REQ-3
```
