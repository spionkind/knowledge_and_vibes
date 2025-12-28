# Knowledge & Vibes — 20‑Minute Deep Dive (Spoken Script)

**Audience:** AI‑savvy, not professional developers  
**Tone:** clear, grounded, confident; “systems thinking”  
**Target length:** ~20 minutes (adjust pacing as needed)

---

## 0:00 — Cold Open (Hook)

Let me describe the most common way AI‑assisted software projects die.

You open an AI coding tool. You type: “Build me the app.”  
And for the first hour, it feels like magic.

You get screens. Buttons. A database. Maybe even authentication.  
You show a friend. They say, “This is insane.”

And then—two days later—everything starts breaking.

Not one bug. Not a missing semicolon. A deeper kind of failure:
- you don’t know what the system is supposed to do anymore
- the AI made decisions you didn’t realize were decisions
- the project is held together by assumptions you can’t see
- and when the AI tries to “fix it,” it often makes it worse

If you’ve felt that, you’re not alone—and the models aren’t the real problem.

The real problem is that **most people are trying to use AI to replace a workflow**.

This video is a deep dive into a repository called **Knowledge & Vibes**—and what it gives you is not “better prompts.”  
It gives you something much more valuable:

**an operating system for building software with AI.**

---

## 1:20 — What This Repo Is (One Sentence + Why It Exists)

Knowledge & Vibes is a **research‑backed framework for building software with AI** where:
- plans are explicit,
- work is tracked,
- and verification is mandatory.

It exists because AI‑assisted development fails in predictable ways when the work is unstructured:
- The AI builds the wrong thing because goals weren’t explicit.
- Requirements evaporate because long context makes the model “forget.”
- Multiple agents conflict because there’s no coordination protocol.
- Bugs compound because there are no gates that force verification.

And here’s the central belief of the project—this is the line you should memorize:

**Truth lives outside the model.**

The AI sounding confident is not evidence.  
Truth is: tests that pass, code that compiles, documentation that exists, measurements you can observe.

Everything else is hypothesis.

[On screen: “Truth lives outside the model.”]

---

## 2:30 — The Compression Trap (Why Prompting Fails)

Here’s the hidden trap that destroys AI coding projects: **compression**.

In your head, your idea contains thousands of tiny decisions:
- what data you store
- what happens when something fails
- what “secure” means for your users
- what’s in scope vs out of scope

Then you compress all of that into twelve words:

“Build a dashboard for tracking personal finances.”

In that moment, you didn’t “ask the AI to code.”  
You **delegated thousands of decisions** to a model that does not have your context.

And the model will fill in gaps with training data—defaults and assumptions—not your intent.

And here’s the dangerous part:

**Gaps become assumptions. Assumptions become architecture. Bad architecture becomes a rewrite.**

So Knowledge & Vibes isn’t trying to get you to “prompt better.”  
It’s trying to make it hard for those gaps to exist.

---

## 3:50 — The Context Window Problem (Why Chunking Is a Feature)

There’s a second failure mode that shows up even when you *do* write a decent plan:

**long context breaks reasoning.**

As conversations and documents get longer, models start dropping details—especially in the middle.  
Not because they’re lazy, but because attention is finite.

In the repo’s research section, there are summaries like:
- “context length hurts”
- “lost in the middle”

The point isn’t the exact percentage. The point is the direction:
more tokens does not automatically mean more correctness.

So Knowledge & Vibes treats **context control** as a first‑class engineering practice:
- big plans get chunked into phases
- phases get chunked into beads
- complex workflows use the orchestrator‑subagent pattern so each phase runs with fresh context

This is why the framework repeats:
“Lossless doesn’t mean huge. Lossless means no guessing.”

[On screen: “Long context → silent omission” → “Chunking → reliability.”]

---

## 5:10 — The Repo Map (So You Don’t Drown)

This repo looks like a wall of documentation until you realize it has a clean structure.

There are four major layers:

### 1) `docs/` — the manual
This is where the workflow is explained: discovery, planning, decomposition, execution, calibration, release.

### 2) `templates/` — the forms
These are the artifacts you copy into your own project: North Star cards, requirements templates, ADRs, risk logs, traceability maps.

### 3) `.claude/` — the automation layer
If you’re using Claude Code, this folder provides slash commands and “skills” that operationalize the workflow.

### 4) `research/` — the evidence base
This is the receipts folder: 50+ research summaries explaining *why* the workflow is shaped the way it is.

[On screen: folder tree highlighting `docs/`, `templates/`, `.claude/`, `research/`.]

If you want the fastest “map inside the map,” there are three files that function like signposts:

- `README.md` tells you what the framework is and why it exists.
- `START_HERE.md` is the reading order and the mental model.
- `docs/workflow/IDEATION_TO_PRODUCTION.md` is the operational manual: the full 11‑stage pipeline.

And I also generated a file‑by‑file walkthrough at `docs/REPO_TOUR.md`—a literal “tour guide” of the repository.

And yes: people say this repo is “so detailed you need a meta understanding.”  
That’s true—because the repo isn’t just content. It’s a system.

So now I’m going to give you the meta understanding: the workflow.

---

## 6:40 — The Six Principles (The “Constitution”)

In `docs/workflow/IDEATION_TO_PRODUCTION.md`, the system is built on six principles.  
I’m going to translate them into plain language:

1) **Give AI few decisions.**  
If you tell an AI “build login,” you just delegated: password rules, session length, security posture, edge cases, error UX.  
The framework’s answer is: make those decisions explicit early so the AI executes instead of invents.

2) **Truth lives outside the model.**  
Don’t trust confidence. Trust evidence.

3) **Planning is search + selection.**  
Don’t bet on one approach. Generate options, then pick.

4) **Tests adjudicate disagreements.**  
When agents disagree, don’t debate—write a test that proves who’s right.

5) **Minimal plans beat massive plans.**  
The goal isn’t “long.” The goal is “lossless”—nothing left to interpret.

6) **Decompose when reality demands it.**  
Start coarse. If you fail after a few tries, split the problem—don’t keep thrashing.

If you understand those, you understand the framework.

Now let’s walk through the actual pipeline.

---

## 8:00 — Roles: What You Do vs What the AI Does

This repo makes a distinction that’s incredibly empowering if you’re not a professional developer:

### The Operator (You)
Your job is **value decisions** and **gate enforcement**.

That means:
- define what success means
- choose tradeoffs when there are real tradeoffs
- answer clarifying questions about intent and constraints
- enforce the rule that “no tests means not done”

You do *not* need to be the person who debugs everything or reviews every line of code.  
You’re enforcing the system of evidence.

### The Agents (AI)
The agents do **technical execution + evidence production**:
- convert intent into testable requirements
- implement beads
- run tests
- run security scans
- document what changed

If you remember one thing: the operator controls the steering wheel. The agent provides horsepower.

---

## 9:30 — The 10‑Stage Pipeline (What Happens at Each Gate)

This system is a gated pipeline. You don’t “vibe” your way forward. You pass gates.

Think of it like flying a plane: you’re not improvising mid‑air. You’re running checklists.

Before Stage 0, there’s a pre‑pipeline stage called **Discovery**.

It lives in `docs/workflow/DISCOVERY.md`, and the goal is simple:
surface every hidden decision until nothing is left to interpret.

Now the pipeline:

### Stage 0 — North Star (Ground Truth)
This is your anchor.

**What you do:** define success, stakes, what’s out of scope, and when the AI should stop and ask.  
**What the AI does:** implements without drifting because the tradeoff policy is explicit.

The template is `templates/NORTH_STAR_CARD_TEMPLATE.md`.

One important detail: the North Star includes a **rigor tier**.  
If this is a hobby project, the process can be lighter.  
If this touches money, health, or production users, the gates need to be stricter.

### Stage 1 — Requirements That “Compile” (`REQ-*` / `AC-*`)
This is where “build me an app” becomes measurable.

Requirements are outcomes.  
Acceptance criteria are how we know it’s true.

**Key rule:** If you can’t test it, it’s not a requirement. It’s a wish.

The repository standardizes this as `REQ-*` and `AC-*` so requirements don’t become vibes again later.

### Stage 2 — Requirements QA
This stage is basically: “pay the cost of clarity up front.”

The system flags ambiguity, rewrites fuzzy language, and forces missing constraints into the open.

### Stage 3 — Decision Search
Instead of committing to one architecture on vibes, you force options:
Option A, Option B, Option C—tradeoffs, risks, reversal triggers.

This gets written down in ADRs: architectural decision records.
The reason is simple: if you don’t record decisions, they get re‑litigated every session.

### Stage 4 — Risks & Spikes
A spike is not “work.” It’s evidence production.

If you don’t know which database to use, you don’t argue about it for two hours.  
You run a spike that produces a decision.

### Stage 5 — Plan Pack (Lossless Specs)
This is where you make the plan “lossless.”

Lossless does not mean huge. It means: **another capable agent could implement without asking you questions**.

The repo even suggests a file layout for plan packs—think:
North Star, requirements, decisions, risks, testing spec, ops/security, dependencies/phases.

### Stage 6 — Phase Breakdown (Short Context Planning)
A big plan gets chunked into phases because long context causes silent omission.

The repo is explicit about this: chunking is a reliability strategy, not a formatting preference.

### Stage 7 — Bead Decomposition (Tasks With Verification)
Phases become beads—tasks with dependencies and verification baked in.

This is where “project management for AI” becomes real.

And the bead template is strict on purpose:
it pushes tests to the top, forces you to localize where changes happen, and includes a context sufficiency check.

### Stage 8 — Execution Loops
This is the loop: test → implement → test → repair.

And here’s where Knowledge & Vibes gets strict:

**Maximum 3 repair attempts.**  
If it’s still failing, you stop and decompose—don’t keep hammering.

This is paired with the ADaPT pattern:
start coarse, attempt execution, and only split into sub‑beads when execution proves something is hard.

### Stage 9 — Calibration
This is the hard stop between phases.

You check: are we aligned with the North Star? are requirements still covered? did we drift?

### Stage 10 — Release
“Done” becomes real:
- tests pass
- security scan clean
- operator sign‑off for the critical things

That’s the pipeline.

[On screen: 10 stages list, highlight “gates” and “verification.”]

Now, a pipeline is only real if it’s executable. So let’s talk about the tool stack.

---

## 14:30 — The Tool Stack (What Each Tool Prevents)

Knowledge & Vibes uses a stack of tools because each tool defends against a specific failure mode.

### 1) Beads (`bd`) — Task Memory
Beads turns “what should we do next?” into a persistent graph:
- tasks
- dependencies
- statuses

So you stop losing work between sessions.

### 2) Beads Viewer (`bv --robot-*`) — Graph Intelligence
When you have many tasks, the hard part is choosing the next one.

BV runs graph analytics to recommend high‑leverage work:
the tasks that unblock other tasks, the risky bottlenecks, the drift signals.

And the repo is explicit: **never run interactive BV in agent sessions**—use the robot flags.

### 3) Agent Mail — Multi‑Agent Coordination
If you have multiple agents, Agent Mail gives you:
- messaging (so work is announced)
- file reservations (so agents don’t edit the same files)

It’s the difference between parallel work and parallel chaos.

### 4) UBS (`ubs --staged`) — Security Gate
This is the pre‑commit scanner.

The repo treats this as non‑negotiable:
**run `ubs --staged` before closing work.**

Because “it works” is not the same thing as “it’s safe.”

### 5) CASS + `cm` — Memory Across Sessions
CASS searches your past AI sessions across tools.  
`cm` distills patterns so you don’t repeat mistakes.

This matters for non‑developers because it turns your history into an asset—not a forgotten pile of chats.

### 6) Grounding tools (Warp‑Grep + Exa)
The repo distinguishes three kinds of truth:
- codebase truth (what does our repo actually do?)
- web truth (what do current docs say?)
- history truth (what worked before?)

That’s what grounding means: verify claims before acting on them.

If you want a "what do I type vs what does the agent do" breakdown, the repo includes:
`docs/guides/TUTORIAL.md`.

And `START_HERE.md` includes a simple, concrete session flow you can follow even if you’re not technical:
prime your session, claim one task, run tests, run the security scan, close the task, calibrate between phases.

Now, the coolest part is that this isn’t just theory—there are actual operational commands.

---

## 17:00 — The Automation Layer: Slash Commands + Skills

Inside `.claude/commands/` you’ll see the slash commands:
- `/prime`
- `/next-bead`
- `/decompose-task`
- `/ground`
- `/calibrate`
- `/execute`
- `/release`

But the deeper layer is `.claude/skills/`.  
Each command maps to a skill, and many skills follow a pattern called the **orchestrator‑subagent pattern**.

Here’s the reason, in plain language:

Long conversations degrade reasoning.  
So instead of one agent holding everything in memory, you split work into phases, and each phase runs in a fresh context.

The orchestrator coordinates. Subagents do focused work.  
The outputs are written to disk as artifacts, not left as chat vapor.

[On screen: diagram from `docs/guides/ORCHESTRATOR_SUBAGENT_PATTERN.md` simplified.]

Let’s make that concrete with two examples.

### Example 1: `/next-bead`
This isn’t just “pick a task.” It’s:
1) close out previous work properly  
2) discover ready tasks  
3) verify there are no conflicts  
4) claim the task, reserve files, and announce it

That’s how you prevent duplicate work and invisible conflicts.

### Example 2: `/calibrate`
Calibration is a roundtable with phases like:
- coverage analysis (are requirements actually covered?)
- drift detection (did we diverge from North Star?)
- test‑based challenge (resolve disagreements with evidence)
- synthesis (falsifiable decisions, preserve dissent)
- user report (you decide)

The key phrase the repo repeats is:

**Tests adjudicate, not rhetoric.**

That’s how you stop “AI arguing” from becoming the project.

One more practical layer: `.claude/rules/`.

These are “always‑on” constraints like:
- how to claim and close beads correctly
- how to communicate in multi‑agent mode (`[CLAIMED]`, `[CLOSED]`, thread IDs)
- safety rules like “don’t delete files without explicit permission” and “don’t run destructive commands”

If you’re not a professional developer, this matters because guardrails prevent accidental self‑sabotage.

---

## 18:30 — A Concrete Walkthrough (Non‑Developer Friendly)

Now let’s imagine you want to build something real.

Not “an app.”  
A specific product: a simple “personal finance dashboard” is a good example because it contains hidden decisions.

### Step 1: Discovery (Before the pipeline)
You open a frontier reasoning model and you interrogate it with curiosity:
- “What decisions are hiding inside this?”
- “What are my options?”
- “What happens if I choose wrong?”
- “What would you need to know before recommending anything?”

You keep going until there’s nothing left to interpret.

This stage is explained in `docs/workflow/DISCOVERY.md`.

### Step 2: North Star (Stage 0)
You fill in the North Star card:
- what success means
- what’s out of scope
- what the AI must stop and ask about

This is where you act like a product manager, not a coder.

### Step 3: Requirements (Stage 1)
You write requirements as outcomes:
- “Users can connect a bank account OR upload a CSV”
- “Transactions are categorized”
- “Monthly spend is shown by category”

Then acceptance criteria:
- “Given a CSV with X rows, dashboard shows X transactions”
- “If upload fails, error is shown and no partial data is stored”

Notice what happened:
you turned “the vibe” into checkable truth.

Now imagine you turn those into beads:

- Bead A: “CSV import”  
  Tests prove: valid CSV imports correctly, invalid CSV fails safely, no partial data writes.

- Bead B: “Categorization rules”  
  Tests prove: known merchants map to categories; unknown merchants go to “Uncategorized”; edits are persisted.

- Bead C: “Dashboard summaries”  
  Tests prove: totals match transaction data; filters behave; empty states display correctly.

And because the tasks are separated, failures are localized.  
You don’t have one gigantic “build the app” blob that you can’t reason about.

### Step 4: Decision Search + Spikes
You might have decisions like:
- Do we use Plaid or CSV only?
- What database?
- What authentication pattern?

Instead of guessing, you timebox spikes that produce evidence.

### Step 5: Plan Pack + Phases
Now you chunk the work so it fits in AI working memory.  
You’re not shrinking it—you’re reorganizing it losslessly.

### Step 6: Beads
Now each chunk becomes tasks with built‑in verification.

And here’s the subtle power move:
the bead template literally forces you to write tests first, define the edit locus, and list what “done” means.

### Step 7: Execution loop with gates
During execution, the system forces three protections:
1) tests first  
2) max three repair attempts  
3) security scan before close

This is how you get reliability without being a professional engineer:
you don’t personally validate every line of code—you validate the evidence gates.

That’s the real promise of Knowledge & Vibes:
it turns you into a competent operator of a technical system.

---

## 19:40 — How To Start (Practical Path)

If you want to actually use this, here’s the “do this next” path:

1) Read `START_HERE.md` for the reading order.
2) Skim `docs/workflow/IDEATION_TO_PRODUCTION.md` to understand the 11 stages.
3) Keep `docs/workflow/PROTOCOLS.md` bookmarked—those are your checklists.
4) Use `TEMPLATES.md` + `templates/` to copy artifacts into your own project.
5) If you’re using Claude Code, copy `.claude/` into your project to get the slash commands and skills.
6) Follow `docs/guides/SETUP_GUIDE.md` to install the toolchain.

And if you ever feel overwhelmed by the repo itself, there’s a generated map at:
`docs/REPO_TOUR.md`.

---

## 20:00 — Closing (Reframe)

The point of this system is not to make you a developer.

It’s to make AI development **reliable**.

You stop trusting confidence. You start trusting gates.

You stop “prompting and hoping.” You start planning, tracking, coordinating, and verifying.

Same hours. Different outcomes.

If you want, the next video can be a live demo:
we’ll take one idea, write a North Star card, convert it to requirements, decompose into beads, and run a real execution loop.

That’s Knowledge & Vibes.
