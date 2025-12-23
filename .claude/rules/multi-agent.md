# Multi-Agent Rules

## Before Claiming Work
- Check inbox for recent `[CLAIMED]` messages
- Check file reservations before editing

## File Reservations
- Reserve files before editing
- Release reservations when done
- If conflict, pick different task or coordinate

## Message Protocol

### Standard Subject Patterns

| Subject | When | Sender | Recipients |
|---------|------|--------|------------|
| `[CLAIMED] bd-XXX - Title` | After claiming task | Worker | All agents |
| `[CLOSED] bd-XXX - Title` | After closing task | Worker | All agents |
| `[BLOCKED] Agent - bd-XXX` | Stuck after 3 tries | Worker | Coordinator |
| `[TRACK COMPLETE] Track Name` | All track beads done | Worker | Coordinator |
| `[PHASE COMPLETE] Phase N` | All tracks done | Coordinator | All agents |
| `[CALIBRATION PASSED] Phase N` | Calibration succeeded | Calibrator | All agents |
| `[CALIBRATION FAILED] Phase N` | Calibration failed | Calibrator | All agents |
| `[NEXT PHASE] Phase N` | New assignments ready | Coordinator | All agents |
| `[PIPELINE COMPLETE]` | All phases done | Coordinator | All agents |
| `Agent Online` | After registration | New agent | Active agents |

### Importance Levels

| Level | When |
|-------|------|
| `normal` | Standard announcements |
| `high` | Phase completions, track completions |
| `urgent` | Blocked agents, calibration failures |

### Thread ID Convention

Always use bead ID as thread_id for related messages:
```
Bead:         bd-123
Thread ID:    bd-123
Subject:      [CLAIMED] bd-123 - Title
Reservation:  reason="bd-123"
Commit:       Closes bd-123
```

### Communication Rules
- Send `[CLAIMED]` when starting
- Send `[CLOSED]` when finishing
- Use bead ID as thread_id for all related messages
- Check inbox periodically while working

## Calibration (`/calibrate`)
- Treat calibration as **test-based adjudication**, not debate or consensus-seeking.
- Make claims with evidence (code/test/doc/measurement) or label as assumptions.
- If you disagree with another agent:
  1. Write a **discriminating test** (one that BREAKS their approach if your concern is valid)
  2. Run the test against their approach
  3. Report results—tests decide, not rhetoric
- If disagreement remains after testing, preserve dissent and state what would resolve it.

## Test-Based Disagreement (Replaces Cross-Examination)
- **Do NOT** engage in extended rhetorical debate (research shows it degrades outcomes)
- **DO** write discriminating tests when you disagree
- **DO** let test results adjudicate conflicts
- **DO** preserve dissent for user decision when tests don't discriminate
- Max 2 rounds of discussion without test results, then escalate to user

## Don't
- Don't edit files another agent has reserved
- Don't skip announcements
- Don't ignore inbox messages
