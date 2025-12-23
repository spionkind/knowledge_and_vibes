# Philosophy: Make It Hard To Be Wrong

## The Problem We're Solving

AI-assisted software development has a fundamental problem that no amount of prompt engineering can fix:

> **LLMs generate plausible text. They do not reliably generate truth.**

This isn't a criticism—it's physics. Language models are trained to predict probable next tokens, not to verify facts against reality. When the model says "this code handles all edge cases," it's expressing what sounds right, not what it has verified.

### The 2025 Reality

The research is now clear about the limitations:

| Finding | Number | Source |
|---------|--------|--------|
| Best models solve realistic software tasks | **~23%** | SWE-Bench Pro |
| Experienced devs slower with AI on unfamiliar code | **19%** | METR RCT |
| LLM-generated code with security vulnerabilities | **~40%** | LLM Security Research |
| Pass@1 improvement from TDD-first | **45.97%** | TDD for AI Code Gen |

These numbers should change how you think about AI-assisted development:

- **Don't assume AI will succeed.** Best case is ~23% on realistic tasks.
- **Don't trust AI on unfamiliar code.** You'll be slower, not faster.
- **Don't skip security scanning.** Nearly half of AI code has vulnerabilities.
- **Do use TDD.** It's the single highest-impact improvement available.

---

## The Core Insight

The job is not "get the model to be right." The job is:

> **Build a workflow where it's hard for the system to be wrong.**

This is a different problem. Instead of trying to make AI output perfect (impossible), we build a system that:
- Catches failures early through verification
- Prevents drift through explicit artifacts
- Limits damage through iteration caps
- Ensures security through mandatory gates

The model can be wrong 77% of the time and you still ship correct software—if your workflow catches the failures before they matter.

---

## The Five Pillars

### 1. Truth Lives Outside the Model

**What this means:** The AI's confident output is not evidence. Truth is external:
- Tests that pass or fail
- Code that compiles or doesn't
- Documentation that exists or doesn't
- Measurements you can observe

**What you do:** Require verification for every claim that matters. "The API supports pagination" isn't verified until you see `?page=2` return different results than `?page=1`.

**Evidence:** `research/008-api-hallucination.md` (38% of low-frequency API calls are invalid), `research/022-chatrepair.md` (execution feedback loops improve correctness).

### 2. Tests Adjudicate Disagreements

**What this means:** When agents disagree, the answer is not more debate. Research shows extended rhetorical debate actually **degrades** outcomes—voting alone beats unstructured debate.

**What you do:**
1. Write discriminating tests (tests that PASS for one approach, FAIL for another)
2. Run the tests
3. Let results decide

If tests can't discriminate, preserve both positions for human decision.

**Evidence:** `research/003-debate-or-vote.md` (more debate rounds made things worse), `research/041-debatecoder.md` (tests as medium of disagreement).

### 3. Decompose When Reality Demands It

**What this means:** Don't over-plan. Don't pre-decompose everything "just in case." You don't know what's actually hard until you try.

**What you do (ADaPT Pattern):**
1. Start with coarse-grained work (beads)
2. Attempt execution
3. If it fails after 3 iterations, decompose—only the failing part
4. Repeat

This discovers what's *actually* hard, not what you guessed would be hard.

**Evidence:** `research/038-adapt.md` (decompose only when needed), `research/011-agentless.md` (simple pipelines beat complex agents).

### 4. Minimum Viable Planning

**What this means:** Plan size should match project complexity. A 200-line script doesn't need a 50-page plan.

> "The smallest set of high-signal tokens that enables correct behavior." — Anthropic Context Engineering

**What you do:**
- Include only what reduces guessing
- "Lossless" means no guessing, not "huge"
- If you're adding detail "just in case," you're adding noise

**Evidence:** `research/004-context-length-hurts.md` (30-50% degradation as context grows), `research/057-anthropic-context-engineering.md` (minimal high-signal context).

### 5. Fail Fast, Escalate Early

**What this means:** Security degrades with repeated self-correction. After 3 iterations of trying to fix something, continuing makes it worse, not better.

**What you do:**
- Max 3 repair iterations per task
- If still failing: STOP, don't keep trying
- Spawn a sub-task for the specific failing part
- Notify the human

**Evidence:** `research/053-feedback-loop-security.md` (security degrades with iterations), `research/006-dark-side-self-correction.md` ("are you sure?" without new info makes things worse).

---

## What The Operator Does

You don't need to be a software engineer. You do **value decisions** and **gate enforcement**:

| Your Job | Not Your Job |
|----------|--------------|
| Define goals, stakes, priorities (North Star) | Validate implementation details |
| Answer clarifying questions about intent | Write or review code |
| Choose between tradeoffs you understand (A/B/C) | Debug technical problems |
| Enforce "no tests = not done" | Decide architecture |
| Approve plan changes during calibration | Judge technical correctness |

Your superpower is insisting that "correct" means **testable and verified**, not "looks right."

---

## What Agents Do

Agents produce technical artifacts and evidence:

- Convert your intent into `REQ-*` and falsifiable `AC-*`
- Ground claims (repo truth via Warp-Grep; web truth via Exa)
- Implement in small, verifiable beads
- Keep traceability current (North Star → REQ/AC → beads → tests)
- Coordinate via Agent Mail and resolve disagreement through tests

---

## What We Avoid (And Why)

### Anti-Patterns With Evidence

| Anti-Pattern | Why It Fails | Evidence | Do Instead |
|--------------|--------------|----------|------------|
| Implementing before tests | Miss 45.97% improvement | `054-tdd-ai-code-gen.md` | Tests FIRST, always |
| Unlimited repair loops | Security degrades | `053-feedback-loop-security.md` | Max 3 iterations |
| Skipping `ubs --staged` | ~40% vulnerability rate | `052-llm-security-vulnerabilities.md` | Mandatory gate |
| Trusting AI on unfamiliar code | 19% slower | `051-metr-rct.md` | Human verification (P14) |
| Assuming high success rates | ~23% realistic success | `050-swe-bench-pro.md` | Verify everything |
| Over-decomposing upfront | Guesses at complexity | `038-adapt.md` | ADaPT: decompose on failure |
| Rhetorical agent debate | Voting beats debate | `003-debate-or-vote.md` | Test-based adjudication |
| Massive "lossless" plans | Context hurts quality | `004-context-length-hurts.md` | Minimal viable plans |
| One-shot prompts | Single path is fragile | `019-plansearch.md` | Search + selection |
| "Are you sure?" without evidence | Overturns correct answers | `006-dark-side-self-correction.md` | Only revise with new info |

---

## How This System Operationalizes The Philosophy

| Principle | Implementation |
|-----------|----------------|
| Truth lives outside | Tests, grounding, verification evidence |
| Tests adjudicate | P10a protocol, calibration skill |
| Adaptive decomposition | P8 ADaPT, sub-bead-structure template |
| Minimum viable planning | Phase sizing, adaptive artifacts |
| Fail fast, escalate | P9 iteration cap, spike beads |

---

## The Key Structural Principles

### 1. Adaptive Decomposition (ADaPT)
> "Decompose only when execution fails"

Start coarse. Attempt execution. Split only when reality demands it.

### 2. Test-Based Disagreement Resolution
> "Tests are the medium of disagreement, not rhetoric"

When agents disagree: write discriminating tests, run them, let results decide.

### 3. Minimal Viable Planning
> "Smallest set of high-signal tokens that enables correct behavior"

Plan size matches project complexity. "Lossless" means no guessing, not "huge."

### 4. TDD-First Everywhere
> "TDD yields 45.97% pass@1 improvement"

Tests in bead descriptions, written before implementation. This is the single highest-impact practice.

---

## Where To Go Next

- **Full lifecycle and gates:** `docs/workflow/EVIDENCE_BASED_GUIDE.md`
- **Exact repeatable moves:** `docs/workflow/PROTOCOLS.md`
- **Phase → beads mechanics:** `docs/workflow/DECOMPOSITION.md`
- **Deep planning tutorial:** `docs/workflow/PLANNING_DEEP_DIVE.md`
- **Research index:** `research/README.md`
