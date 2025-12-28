---
title: Repo Tour (Generated)
description: File-by-file walkthrough of Knowledge & Vibes: purpose, workflow, tools, and agent configuration.
---

# Knowledge & Vibes — Repo Tour (Generated)

_Generated at 2025-12-28 01:39:34Z by `scripts/generate_repo_tour.py`._

## What This Project Is

Knowledge & Vibes is a research-backed framework for building software with AI. It formalizes planning (North Star + REQ/AC + ADRs), decomposes work into **beads** (tracked tasks with dependencies), coordinates multiple agents via Agent Mail (messaging + file reservations), and enforces verification gates (TDD-first tests, iteration caps, and security scanning via `ubs`).

## Workflow (10-Stage Pipeline)

- Stage -1 — Discovery (Before the Pipeline)
- Stage 0 — Set the Rigor Mode (Context drives process)
- Stage 1 — Requirements That "Compile" (REQ/AC as the operator interface)
- Stage 2 — Requirements QA Pass (ISO‑style "make ambiguity expensive")
- Stage 3 — Decision Search (multiple viable plans, then select)
- Stage 4 — Risk‑Driven Spikes (collapse uncertainty before committing)
- Stage 5 — Plan Pack Assembly (turn decisions into lossless specs)
- Stage 6 — Phase Breakdown (short-context planning to avoid omission)
- Stage 7 — Bead Decomposition (convert phases to executable task units)
- Stage 8 — Execution Loops (generate → run → fix, not "think harder")
- Stage 9 — /calibrate (search controller + drift correction)
- Stage 10 — Release Readiness (make "done" real)

## How To Use This Repo (Fast Path)

- Start: `README.md`
- Orientation hub: `START_HERE.md`
- Workflow reference: `docs/workflow/IDEATION_TO_PRODUCTION.md` and `docs/workflow/PROTOCOLS.md`
- Practical tooling: `docs/guides/TUTORIAL.md`
- Templates: `TEMPLATES.md` and `templates/`
- Evidence: `research/README.md`

## File-by-File Walkthrough

### Root: Orientation

- `GLOSSARY.md` — Glossary: The pre-pipeline phase where you surface every decision hiding in your idea through curiosity-driven interrogation of frontier models. Discovery happens before formal planning begins.
- `README.md` — Knowledge & Vibes: [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Research-Backed](https://img.shields.io/badge/Research-50%2B%20Papers-green.svg)](./research/README.md)
- `START_HERE.md` — Start Here: Knowledge & Vibes gives you a structured system for building software with AI:
- `TEMPLATES.md` — Templates: > Each template feeds the next. Skip one and you're guessing.

### Docs: Workflow

- `docs/workflow/DECOMPOSITION.md` — Decomposition: How to break a completed plan into phases and beads that AI agents can execute without losing requirements.
- `docs/workflow/DISCOVERY.md` — Discovery: The phase before planning. Where you surface every decision hiding in your idea through curiosity-driven interrogation of frontier models.
- `docs/workflow/IDEATION_TO_PRODUCTION.md` — Ideation → Shipped Product: The complete end-to-end pipeline from idea to shipped product. This is the single-page reference for the full lifecycle.
- `docs/workflow/PHILOSOPHY.md` — Philosophy: There's a widening divide in software development right now. Not between languages or frameworks. Between developers who've restructured how they work around AI and those still operating at manual speed.
- `docs/workflow/PLANNING_DEEP_DIVE.md` — Planning Deep Dive: How to take a vague idea and turn it into a complete master plan that AI agents can execute without guessing.
- `docs/workflow/PROTOCOLS.md` — Evidence-Backed Protocols: Each protocol exists because skipping it causes predictable failures.

### Docs: Guides

- `docs/guides/CLAUDE_CONFIG_GUIDE.md` — Claude Code Configuration Guide: How to organize agent instructions using Claude Code's official configuration system: rules, skills, and commands.
- `docs/guides/MIGRATION_GUIDE.md` — Migration Guide: Bring an existing project into the Knowledge & Vibes stack. This guide covers restructuring Claude Code configuration, installing tools, and setting up proper documentation.
- `docs/guides/ORCHESTRATOR_SUBAGENT_PATTERN.md` — Orchestrator-Subagent Pattern: Instead of one agent holding everything in context, spawn specialized subagents for each phase. Each gets fresh context. Pass only **summaries and file paths** between phases, not full content.
- `docs/guides/SETUP_GUIDE.md` — Setup Guide: Knowledge & Vibes is a system for building software with AI assistance. Instead of chatting with AI and hoping for the best, this system gives you:
- `docs/guides/TUTORIAL.md` — Tutorial: The Complete Tool Guide: This tutorial explains what each tool does, why it matters, and how to use it effectively.

### Templates (Operator-Facing)

- `templates/AGENTS_TEMPLATE.md` — AGENTS.md: - **Name**: [Project Name] - **Language**: [TypeScript/Python/Go/etc.] - **Key Paths**: `src/`, `tests/`, `docs/`
- `templates/CODEMAPS_TEMPLATE.md` — Codemaps Template: **Token-aware architecture documentation for AI agents.**
- `templates/DECISIONS_ADRS_TEMPLATE.md` — Decisions Template (ADRs): ADRs (Architecture Decision Records) capture significant decisions so they don't get relitigated later.
- `templates/NORTH_STAR_CARD_TEMPLATE.md` — North Star Card: The North Star Card anchors everything. Before anyone writes code, this document pins down what success looks like, what's out of scope, and when to stop and ask.
- `templates/REQUIREMENTS_QA_TEMPLATE.md` — Requirements QA (Template): Use this after drafting `REQ-*` / `AC-*`. The goal is to remove ambiguity and make requirements "compile" into tests and implementation tasks.
- `templates/REQUIREMENTS_TEMPLATE.md` — Requirements Template: Requirements define what must be true when you're done. They describe outcomes and constraints, not solutions.
- `templates/RISKS_AND_SPIKES_TEMPLATE.md` — Risks & Spikes Template: Spikes are timeboxed investigations that produce evidence. They're not features. They exist to reduce uncertainty before you commit to a path.
- `templates/TRACEABILITY_TEMPLATE.md` — Traceability Matrix Template: A traceability matrix maps requirements to implementation. It prevents drift and makes gaps obvious.

### .claude: Slash Commands

- `.claude/commands/calibrate.md` — /calibrate: Pause all agents and run a calibration roundtable to realign the plan
- `.claude/commands/decompose-task.md` — /decompose-task: Decompose Task - Turn a Phase Plan into Beads
- `.claude/commands/execute.md` — /execute: Parallel execution orchestrator. Picks up existing beads and runs them with multiple agents working in parallel.
- `.claude/commands/ground.md` — /ground: Manually trigger grounding check before implementation
- `.claude/commands/next-bead.md` — /next-bead: Find and safely claim the next Beads task (conflict-checked)
- `.claude/commands/prime.md` — /prime: New agent startup checklist (Agent Mail + Beads)
- `.claude/commands/release.md` — /release: Pre-ship checklist for release readiness (Protocol P12)
- `.claude/commands/resolve.md` — /resolve: Resolve disagreements between agents or approaches using test-based adjudication

### .claude: Rules

- `.claude/rules/beads.md` — Beads Rules: - Always claim parent AND all sub-beads together - Always include `--assignee YOUR_NAME` - Always send `[CLAIMED]` announcement before starting work
- `.claude/rules/multi-agent.md` — Multi-Agent Rules: These rules apply to **orchestrators and top-level worker agents** — agents with persistent identity in the Agent Mail ecosystem.
- `.claude/rules/safety.md` — Safety Rules: Never delete any file or directory without explicit user permission in this session. - This includes files you just created (tests, scripts, temp files) - You do not get to decide something is "safe" to remove

### .claude: Skills (and Subagents)

- `.claude/skills/agent-mail/SKILL.md` — agent-mail: Multi-agent coordination with Agent Mail MCP. Use when registering agents, reserving files, sending messages, coordinating with other agents, or when the user mentions "agent mail", "coordination", "file reservation", or "multi-agent".
- `.claude/skills/bead-workflow/SKILL.md` — bead-workflow: Manage beads correctly including claiming, closing, announcements, and dependencies. Use when starting work on a task, when finishing a task, when the user mentions beads or tasks, or when coordinating with other agents on task ownership.
- `.claude/skills/bead-workflow/dependencies.md` — Dependency Management: How to work with bead dependencies.
- `.claude/skills/bead-workflow/multi-agent.md` — Multi-Agent Coordination: Extra protocols when multiple agents are active.
- `.claude/skills/beads-cli/SKILL.md` — beads-cli: Task tracking with the bd (Beads) CLI. Use when creating tasks, claiming work, closing beads, managing dependencies, or when the user mentions "beads", "bd", or "tasks".
- `.claude/skills/beads-viewer/SKILL.md` — beads-viewer: Graph analysis with bv (Beads Viewer). Use when analyzing the task graph, finding blockers, getting recommendations, checking critical path, or when the user mentions "bv", "graph", "dependencies", or "what should I work on".
- `.claude/skills/calibrate/SKILL.md` — calibrate: Run an evidence-seeking calibration roundtable to realign the plan with the North Star. Use when pausing between phases, when agents disagree, when reviewing work, when the user mentions "calibrate" or "realign", or when making decisions that affect the plan.
- `.claude/skills/calibrate/agents/challenge.md` — Test-Based Challenge Subagent: You are the **Test-Based Challenge** subagent for calibration. Your job is to challenge findings with discriminating tests, not rhetoric.
- `.claude/skills/calibrate/agents/coverage.md` — Coverage Analysis Subagent: You are the **Coverage Analysis** subagent for calibration. Your job is to check requirement coverage for the completed phase.
- `.claude/skills/calibrate/agents/drift.md` — Drift Detection Subagent: You are the **Drift Detection** subagent for calibration. Your job is to identify where implementation has drifted from the North Star.
- `.claude/skills/calibrate/agents/report.md` — User Report Subagent: You are the **User Report** subagent for calibration. Your job is to present findings objectively to the user so they can make informed decisions.
- `.claude/skills/calibrate/agents/synthesize.md` — Synthesis Subagent: You are the **Synthesis** subagent for calibration. Your job is to synthesize findings into falsifiable decisions while preserving dissent.
- `.claude/skills/calibrate/evidence-standard.md` — Evidence Standard: Detailed guide for the calibration evidence standard.
- `.claude/skills/cass-memory/SKILL.md` — cass-memory: Cross-agent learning with cm (cass-memory). Use before starting non-trivial tasks, when looking for patterns from past work, when the user mentions "cm", "memory", "learned rules", or "what do we know about".
- `.claude/skills/cass-search/SKILL.md` — cass-search: Search past AI sessions with CASS. Use when looking for past solutions, searching session history, finding how something was done before, or when the user mentions "cass", "history", or "past sessions".
- `.claude/skills/decompose-task/SKILL.md` — decompose-task: Decompose a phase plan into atomic beads and sub-beads. Use when breaking down a phase into tasks, when the user mentions "decompose" or "break down", when creating beads from a plan, or when structuring work for parallel execution.
- `.claude/skills/decompose-task/agents/create-beads.md` — Create Beads Subagent: You are the **Create Beads** subagent for task decomposition. Your job is to create the actual beads from the manifest.
- `.claude/skills/decompose-task/agents/dependencies.md` — Dependencies Subagent: You are the **Dependencies** subagent for task decomposition. Your job is to set up the dependency graph between beads.
- `.claude/skills/decompose-task/agents/manifest.md` — Manifest Subagent: You are the **Manifest** subagent for task decomposition. Your job is to create a LOSSLESS enumeration of everything that must be captured in beads.
- `.claude/skills/decompose-task/agents/understand.md` — Understanding Subagent: You are the **Understanding** subagent for task decomposition. Your job is to deeply understand the phase before any decomposition begins.
- `.claude/skills/decompose-task/agents/validate.md` — Validation Subagent: You are the **Validation** subagent for task decomposition. Your job is to validate the decomposition before execution begins.
- `.claude/skills/disagreement-resolution/SKILL.md` — disagreement-resolution: Resolve disagreements between agents or approaches using test-based adjudication. Use when agents disagree, when multiple valid approaches exist, when the user asks "which approach", or when making architectural decisions with tradeoffs.
- `.claude/skills/disagreement-resolution/agents/adjudicate.md` — Adjudication Subagent: You are the **Adjudication** subagent for disagreement resolution. Your job is to make a decision based on test results, or preserve dissent for user decision.
- `.claude/skills/disagreement-resolution/agents/execute.md` — Test Execution Subagent: You are the **Test Execution** subagent for disagreement resolution. Your job is to run the discriminating tests and record results.
- `.claude/skills/disagreement-resolution/agents/positions.md` — Positions Subagent: You are the **Positions** subagent for disagreement resolution. Your job is to clearly articulate each position without advocating for any.
- `.claude/skills/disagreement-resolution/agents/tests.md` — Test Generation Subagent: You are the **Test Generation** subagent for disagreement resolution. Your job is to write discriminating tests that would PASS for one approach and FAIL for another.
- `.claude/skills/exa-search/SKILL.md` — exa-search: Web and code search with Exa MCP. Use for current documentation, API references, code examples, latest library info, or when the user mentions "exa", "web search", "docs", or "current API".
- `.claude/skills/execute/SKILL.md` — execute: Parallel execution orchestrator. Picks up existing beads, computes parallel tracks, spawns worker agents, coordinates via Agent Mail, runs calibration at phase boundaries.
- `.claude/skills/external-docs/SKILL.md` — external-docs: Verify external libraries, APIs, and frameworks against current documentation before writing code. Use when about to implement features using external dependencies, when writing import statements for third-party libraries, when unsure if a pattern or method is current, or when the user mentions grounding or verification.
- `.claude/skills/external-docs/patterns.md` — Grounding Patterns: How to ground for any framework or library.
- `.claude/skills/external-docs/queries.md` — Exa Query Examples: Query patterns that work well for grounding.
- `.claude/skills/next-bead/SKILL.md` — next-bead: Find and safely claim the next Beads task with conflict checking. Use when looking for work, when finishing a task and need the next one, when the user mentions "next task" or "what should I work on", or when coordinating with other agents on task ownership.
- `.claude/skills/next-bead/agents/claim.md` — Claiming Subagent: You are the **Claiming** subagent for next-bead. Your job is to safely claim a task, reserve files, and announce to other agents.
- `.claude/skills/next-bead/agents/closeout.md` — Closeout Subagent: You are the **Closeout** subagent for next-bead. Your job is to properly close any in-progress work before claiming new tasks.
- `.claude/skills/next-bead/agents/discover.md` — Discovery Subagent: You are the **Discovery** subagent for next-bead. Your job is to find all available work and gather coordination context.
- `.claude/skills/next-bead/agents/verify.md` — Verification Subagent: You are the **Verification** subagent for next-bead. Your job is to verify a task can be safely claimed without conflicts.
- `.claude/skills/prime/SKILL.md` — prime: New agent startup checklist for Agent Mail and Beads. Use when starting a new agent session, when the user says "prime" or "startup", or when beginning work on a multi-agent project.
- `.claude/skills/prime/agents/coordinate.md` — Coordination Subagent: You are the **Coordination** subagent for agent startup. Your job is to coordinate with other agents via Agent Mail.
- `.claude/skills/prime/agents/discover.md` — Discovery Subagent: You are the **Discovery** subagent for agent startup. Your job is to find available work and recommend a task to claim.
- `.claude/skills/prime/agents/identity.md` — Identity Subagent: You are the **Identity** subagent for agent startup. Your job is to register the agent with Agent Mail and establish identity.
- `.claude/skills/prime/agents/orient.md` — Orientation Subagent: You are the **Orientation** subagent for agent startup. Your job is to understand the project context and recent history.
- `.claude/skills/project-memory/SKILL.md` — project-memory: Retrieve relevant context from past sessions before starting implementation. Use when beginning work on a task, when the user describes what to build, when about to write significant code, or when stuck on a problem that may have been solved before.
- `.claude/skills/project-memory/deep-dive.md` — Deep Dive with CASS: When `cm context` isn't enough, dig into specific sessions.
- `.claude/skills/release/SKILL.md` — release: Release readiness checklist for shipping. Use after execution completes, when the user says "release" or "ship", or before deploying to production.
- `.claude/skills/ubs-scanner/SKILL.md` — ubs-scanner: Bug scanning with UBS (Ultimate Bug Scanner). Use before commits, when scanning for bugs, when the user mentions "ubs", "bugs", "scan", or "code quality".
- `.claude/skills/warp-grep/SKILL.md` — warp-grep: Parallel code search with Warp-Grep MCP. Use for codebase discovery, understanding how things work, data flow analysis, or when the user asks "how does X work" about the codebase.

### .claude: Runtime Templates

- `.claude/templates/beads/bead-structure.md` — Enhanced Bead Structure Template: A properly enhanced bead is a complete specification that any agent can implement correctly.
- `.claude/templates/beads/claimed.md` — Claimed Announcement: Send when claiming a bead to notify all agents.
- `.claude/templates/beads/closed.md` — Closed Announcement: Send when completing a bead to notify all agents.
- `.claude/templates/beads/next-bead-output.md` — Next Bead Output: Summary after claiming a bead.
- `.claude/templates/beads/verification.md` — Pre-Claim Verification: Complete before claiming any bead.
- `.claude/templates/calibration/broadcast.md` — Broadcast Analysis: Agent broadcasts to all other agents.
- `.claude/templates/calibration/change-log-entry.md` — Change Log Entry Template: Use this template when recording plan changes during `/calibrate`.
- `.claude/templates/calibration/decision.md` — Falsifiable Decision: Every decision must have success and reversal criteria.
- `.claude/templates/calibration/response.md` — Response: Reply to challenges from other agents.
- `.claude/templates/calibration/summary.md` — Calibration Summary: Agent-to-agent summary after synthesis.
- `.claude/templates/calibration/user-report.md` — User Report: Final output to user. Objective. Clear. User decides.
- `.claude/templates/calibration/verification.md` — Verification Assignment: Cross-verification before resuming work.
- `.claude/templates/planning/audit-report.md` — Audit Report Template: Use this template when auditing another agent's decomposition work.
- `.claude/templates/planning/content-manifest.md` — Content Manifest: Create before decomposing to ensure nothing is lost.
- `.claude/templates/planning/decompose-output.md` — Decomposition Output: Summary after decomposing a phase.
- `.claude/templates/planning/phase-document.md` — Phase Document Template: Use this structure when creating phase documents during Phase 2 breakdown.
- `.claude/templates/planning/sub-bead-structure.md` — Sub-Bead Structure (ADaPT Pattern): > **Key insight (ADaPT, 2025):** Sub-beads are created **only when execution fails**, not during upfront planning. Don't over-decompose—let execution reveal what's actually hard.

### Other AI Tooling

- `.codex/rules` — UBS Quick Reference for AI Agents: ubs file.ts file2.py # Specific files (< 1s) — USE THIS ubs $(git diff --name-only --cached) # Staged files — before commit ubs --only=js,python src/ # Language filter (3-5x faster)
- `.cursor/rules` — UBS Quick Reference for AI Agents: ubs file.ts file2.py # Specific files (< 1s) — USE THIS ubs $(git diff --name-only --cached) # Staged files — before commit ubs --only=js,python src/ # Language filter (3-5x faster)
- `.gemini/rules` — UBS Quick Reference for AI Agents: ubs file.ts file2.py # Specific files (< 1s) — USE THIS ubs $(git diff --name-only --cached) # Staged files — before commit ubs --only=js,python src/ # Language filter (3-5x faster)

### Research Summaries

- `research/001-live-swe-agent.md` — Live-SWE-agent: Dynamic Tool Creation: **Paper:** Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly? **URL:** https://arxiv.org/abs/2511.13646 **Date:** November 2025
- `research/002-planning-driven-programming.md` — Planning-Driven Programming (LPW): **Paper:** Planning-Driven Programming: A Large Language Model Programming Workflow **URL:** https://arxiv.org/abs/2411.14503 **Date:** November 2024
- `research/003-debate-or-vote.md` — Debate or Vote: Multi-Agent Decision Making: **Paper:** Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models? **URL:** https://arxiv.org/abs/2508.17536 **Date:** August 2025
- `research/004-context-length-hurts.md` — Context Length Alone Hurts Performance: **Paper:** Context Length Alone Hurts LLM Performance Despite Perfect Retrieval **URL:** https://arxiv.org/abs/2510.05381 **Date:** October 2025
- `research/005-lost-in-middle-code.md` — Lost-in-Middle for Code: **Paper:** Sense and Sensitivity: Examining the Influence of Semantic Recall on Long Context Code Reasoning **URL:** https://arxiv.org/abs/2505.13353 **Date:** May 2025
- `research/006-dark-side-self-correction.md` — The Dark Side of LLM Self-Correction: **Paper:** Understanding the Dark Side of LLMs' Intrinsic Self-Correction **URL:** https://arxiv.org/abs/2412.14959 **Date:** December 2024
- `research/007-swe-gym.md` — SWE-Gym: Training Software Engineering Agents: **Paper:** Training Software Engineering Agents and Verifiers with SWE-Gym **URL:** https://arxiv.org/abs/2412.21139 **Date:** December 2024
- `research/008-api-hallucination.md` — API Hallucination and Documentation Augmented Generation: **Paper:** On Mitigating Code LLM Hallucinations with API Documentation **URL:** https://arxiv.org/abs/2407.09726 **Date:** July 2024
- `research/009-swe-bench.md` — SWE-bench: Real-World GitHub Issue Resolution: **Paper:** SWE-bench: Can Language Models Resolve Real-World GitHub Issues? **URL:** https://ar5iv.labs.arxiv.org/html/2310.06770 **Date:** October 2023
- `research/010-swe-agent.md` — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering: **Paper:** SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering **URL:** https://arxiv.org/abs/2405.15793 **Date:** May 2024
- `research/011-agentless.md` — Agentless: Demystifying SWE Agents: **Paper:** Agentless: Demystifying LLM-based Software Engineering Agents **URL:** https://arxiv.org/html/2407.01489v2 **Date:** July 2024
- `research/012-autocoderover.md` — AutoCodeRover: Autonomous Program Improvement: **Paper:** AutoCodeRover: Autonomous Program Improvement **URL:** https://arxiv.org/html/2404.05427v1 **Date:** April 2024
- `research/013-specrover.md` — SpecRover: Code Intent Extraction via LLMs: **Paper:** SpecRover: Code Intent Extraction via LLMs **URL:** https://arxiv.org/html/2408.02232v4 **Date:** August 2024 (latest revisions November 2024)
- `research/014-codeplan.md` — CodePlan: Repository-level Planning + Chain of Edits: **Paper:** CodePlan: Repository-level Coding using LLMs and Planning **URL:** https://dl.acm.org/doi/10.1145/3643757 **Date:** FSE 2024 (paper published September 2023)
- `research/015-coeditor.md` — Coeditor: Leveraging Repo-level Diffs for Code Auto-Editing: **Paper:** Coeditor: Leveraging Repo-level Diffs for Code Auto-editing **URL:** https://arxiv.org/html/2305.18584v2 **Date:** May 2023 (arXiv); ICLR 2024
- `research/016-res-q.md` — RES-Q: Repository-Scale Evaluation Benchmark: **Paper:** RES-Q: Evaluating Code-Editing Large Language Model Systems at the Repository Scale **URL:** https://arxiv.org/html/2406.16801v2 **Date:** June 2024
- `research/017-context-retrieval-repo-editing.md` — Reasoning for Context Retrieval in Repository-Level Code Editing: **Paper:** On The Importance of Reasoning for Context Retrieval in Repository-Level Code Editing **URL:** https://arxiv.org/abs/2406.04464 **Date:** June 2024
- `research/018-livecodebench.md` — LiveCodeBench: Contamination-Free Code Evaluation: **Paper:** LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code **URL:** https://arxiv.org/html/2403.07974v1 **Date:** March 2024
- `research/019-plansearch.md` — PlanSearch: Search Over Natural-Language Plans: **Paper:** Planning In Natural Language Improves LLM Search For Code Generation **URL:** https://arxiv.org/html/2409.03733v1 **Date:** September 2024
- `research/020-codetree.md` — CodeTree: Agent-Guided Tree Search for Code Generation: **Paper:** CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models **URL:** https://arxiv.org/html/2411.04329v2 **Date:** November 2024
- `research/021-swe-bench-plus.md` — SWE-Bench+: Enhanced Coding Benchmark for LLMs: **Paper:** SWE-Bench+: Enhanced Coding Benchmark for LLMs **URL:** https://arxiv.org/html/2410.06992v1 **Date:** October 2024
- `research/022-chatrepair.md` — ChatRepair: Conversation-Driven Program Repair: **Paper:** Automated Program Repair via Conversation: Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT **URL:** https://lingming.cs.illinois.edu/publications/issta2024.pdf **Date:** ISSTA 2024
- `research/023-toggle.md` — Toggle: Token-Level Bug Localization and Repair: **Paper:** A Deep Dive into Large Language Models for Automated Bug Localization and Repair (Toggle framework) **URL:** https://arxiv.org/html/2404.11595v1 **Date:** April 2024
- `research/024-thinkrepair.md` — ThinkRepair: Self-Directed Automated Program Repair: **Paper:** ThinkRepair: Self-Directed Automated Program Repair **URL:** https://arxiv.org/html/2407.20898v1 **Date:** July 2024
- `research/025-appatch.md` — APPATCH: Automated Adaptive Prompting for Vulnerability Patching: **Paper:** APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching **URL:** https://arxiv.org/html/2408.13597v1 **Date:** August 2024
- `research/026-flames.md` — FLAMES: Semantic-Guided Search for Program Repair: **Paper:** Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation (FLAMES) **URL:** https://arxiv.org/abs/2410.16655 **Date:** October 2024
- `research/027-swe-smith.md` — SWE-smith: Scaling Training Data for SWE Agents: **Paper:** SWE-smith: Scaling Data for Software Engineering Agents **URL:** https://arxiv.org/abs/2504.21798 **Date:** April 2025
- `research/028-swe-bench-live.md` — SWE-bench-Live: Continuously Updating SWE Benchmark: **Paper:** SWE-bench Goes Live! **URL:** https://arxiv.org/abs/2505.23419 **Date:** May 2025
- `research/029-swe-rebench.md` — SWE-rebench: Decontaminated, Standardized SWE Evaluation: **Paper:** SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents **URL:** https://arxiv.org/pdf/2505.20411 **Date:** May 2025
- `research/030-swe-bench-multimodal.md` — SWE-bench Multimodal: Visual Software Engineering Tasks: **Paper:** SWE-bench Multimodal: Does Your Agent Write Better Code When It Can See? **URL:** https://arxiv.org/abs/2410.03859 **Date:** October 2024
- `research/031-alphacodium.md` — AlphaCodium: Flow Engineering for Code Generation: **Paper:** Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering **URL:** https://arxiv.org/abs/2401.08500 **Date:** January 2024
- `research/032-tdd-code-generation.md` — Test-Driven Development for Code Generation: **Paper:** Test-Driven Development for Code Generation **URL:** https://arxiv.org/abs/2402.13521 **Date:** February 2024 (revised June 2024)
- `research/033-requirements-to-code.md` — Requirements Are All You Need: From Requirements to Code with LLMs: **Paper:** Requirements are All You Need: From Requirements to Code with LLMs **URL:** https://arxiv.org/abs/2406.10101 **Date:** June 2024
- `research/034-llms-in-re-guideline.md` — LLMs in Requirements Engineering: Systematic Guideline: **Paper:** Using Large Language Models for Natural Language Processing Tasks in Requirements Engineering: A Systematic Guideline **URL:** https://arxiv.org/abs/2402.13823 **Date:** February 2024
- `research/035-llm-vs-human-re.md` — LLMs vs Human Experts in Requirements Engineering: **Paper:** Analysis of LLMs vs Human Experts in Requirements Engineering **URL:** https://arxiv.org/abs/2501.19297 **Date:** January 2025
- `research/036-requirements-qa-iso-29148.md` — Requirements QA with LLMs: ISO 29148 Validation: **Paper:** Leveraging LLMs for the Quality Assurance of Software Requirements **URL:** https://arxiv.org/abs/2408.10886 **Date:** August 2024
- `research/037-requirements-to-code-practices.md` — From Requirements to Code: How Practitioners Actually Work with LLMs: **Paper:** From Requirements to Code: Understanding Developer Practices in LLM-Assisted Software Engineering **URL:** https://arxiv.org/abs/2507.07548 **Date:** July 2025
- `research/038-adapt.md` — ADaPT: As-Needed Decomposition and Planning with Language Models: **Paper:** ADaPT: As-Needed Decomposition and Planning with Language Models **URL:** https://arxiv.org/abs/2311.05772 **Date:** November 2023 (v2 April 2024)
- `research/039-tdag.md` — TDAG: Dynamic Task Decomposition and Agent Generation: **Paper:** TDAG: A Multi-Agent Framework based on Dynamic Task Decomposition and Agent Generation **URL:** https://arxiv.org/abs/2402.10178 **Date:** February 2024
- `research/040-mapcoder.md` — MapCoder: Multi-Agent Code Generation Pipeline: **Paper:** MapCoder: Multi-Agent Code Generation for Competitive Problem Solving **URL:** https://arxiv.org/abs/2405.11403 **Date:** May 2024
- `research/041-debatecoder.md` — DebateCoder: Test-Case-Driven Debate for Code Generation: **Paper:** DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation **URL:** https://aclanthology.org/2025.acl-long.589/ **Date:** 2025
- `research/042-rankef.md` — RankEF: Execution-Feedback Reranking: **Paper:** Sifting through the Chaff: On Utilizing Execution Feedback for Ranking the Generated Code Candidates **URL:** https://arxiv.org/abs/2408.13976 **Date:** August 2024
- `research/043-rlef.md` — RLEF: Reinforcement Learning from Execution Feedback: **Paper:** RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning **URL:** https://arxiv.org/abs/2410.02089 **Date:** October 2024 (updates in 2025)
- `research/044-iris.md` — IRIS: LLM-Assisted Static Analysis for Security: **Paper:** IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities **URL:** https://arxiv.org/abs/2405.17238 **Date:** May 2024 (updated April 2025)
- `research/045-repairagent.md` — RepairAgent: Autonomous Program Repair Agent: **Paper:** RepairAgent: An Autonomous, LLM-Based Agent for Program Repair **URL:** https://arxiv.org/abs/2403.17134 **Date:** March 2024
- `research/046-d4c.md` — D4C: Aligning the Objective of LLM-Based Program Repair: **Paper:** Aligning the Objective of LLM-based Program Repair **URL:** https://arxiv.org/abs/2404.08877 **Date:** April 2024
- `research/047-humaneval-pro.md` — HumanEval Pro: Self-Invoking Code Generation: **Paper:** HumanEval Pro and MBPP Pro: Evaluating Large Language Models on Self-invoking Code Generation **URL:** https://arxiv.org/abs/2412.21199 **Date:** December 2024
- `research/048-eg-cfg.md` — EG-CFG: Execution-Guided Line-by-Line Code Generation: **Paper:** Execution Guided Line-by-Line Code Generation **URL:** https://arxiv.org/abs/2506.10948 **Date:** June 2025
- `research/049-codeform-planning.md` — Code-Form Planning: Structured Plans for Reasoning: **Paper:** Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning **URL:** https://arxiv.org/abs/2409.12452 **Date:** October 2024
- `research/050-swe-bench-pro.md` — SWE-Bench Pro: Realistic AI Software Engineering Benchmark: **Paper:** SWE-Bench Pro: A More Realistic Benchmark for AI Software Engineering **URL:** https://arxiv.org/abs/2501.xxxxx (2025) **Date:** 2025
- `research/051-metr-rct.md` — METR Randomized Controlled Trial 2025: **Paper:** Measuring the Impact of AI Coding Assistants on Developer Productivity: A Randomized Controlled Trial **URL:** https://metr.org/blog/2025-01-rct-results/ **Date:** January 2025
- `research/052-llm-security-vulnerabilities.md` — LLM Security Vulnerabilities 2025: **Paper:** Security Vulnerabilities in LLM-Generated Code: A Comprehensive Analysis **URL:** Multiple 2025 security research papers (aggregated analysis) **Date:** 2025
- `research/053-feedback-loop-security.md` — Feedback Loop Security Degradation 2025: **Paper:** Security Implications of Iterative LLM Code Repair **URL:** Multiple 2025 security research papers **Date:** 2025
- `research/054-tdd-ai-code-gen.md` — TDD for AI Code Generation 2025: **Paper:** Test-Driven Development for AI-Assisted Code Generation **URL:** https://arxiv.org/abs/2502.xxxxx **Date:** 2025
- `research/055-test-intentions.md` — Test Intentions 2025: **Paper:** Using Test Intentions to Improve AI-Generated Test Coverage **URL:** Multiple 2025 testing research papers **Date:** 2025
- `research/056-multi-agent-orchestrator.md` — Multi-Agent Orchestrator Patterns 2025: **Paper:** Orchestrator-Worker Patterns for Multi-Agent Code Generation **URL:** Multiple 2025 multi-agent research papers **Date:** 2025
- `research/057-anthropic-context-engineering.md` — Anthropic Context Engineering 2025: **Paper:** Context Engineering for Claude: Best Practices from Anthropic **URL:** https://www.anthropic.com/engineering/context-engineering **Date:** 2025
- `research/058-lita-lightweight-agents.md` — Lita: Lightweight Agents for Agentic Coding 2025: **Paper:** Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs **URL:** https://arxiv.org/abs/2509.25873 **Date:** September 2025
- `research/059-multi-agent-orchestrator-2025.md` — Multi-Agent Orchestrator Patterns 2025: **Sources:** - Anthropic: "How we built our multi-agent research system" (June 2025) - "Conductors to Orchestrators: The Future of Agentic Coding" (November 2025)
- `research/060-debugging-decay-index.md` — Debugging Decay Index 2025: **Paper:** Measuring and mitigating debugging effectiveness decay in code language models **URL:** https://www.nature.com/articles/s41598-025-27846-5 **Date:** December 2025
- `research/061-llm-security-2025.md` — LLM Code Security Vulnerabilities 2025: **Sources:** - Veracode 2025 GenAI Code Security Report (100+ LLMs tested) - OWASP Top 10 for LLM Applications 2025
- `research/062-rag-repository-code.md` — Retrieval-Augmented Code Generation 2025: **Sources:** - "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches" (September 2025) - CodeRAG-Bench (2024-2025)
- `research/063-agentic-se-3.md` — Agentic Software Engineering (SE 3.0) 2025: **Sources:** - "Agentic Software Engineering: Foundational Pillars and a Research Roadmap" (September 2025) - "The Rise of AI Teammates in Software Engineering (SE) 3.0" (July 2025)
- `research/064-deepcode-open-agentic.md` — DeepCode: Open Agentic Coding: **Paper:** DeepCode: Open Agentic Coding **URL:** https://arxiv.org/abs/2512.07921 **Date:** December 8, 2025
- `research/065-confucius-code-agent.md` — Confucius Code Agent: Scalable Agent Scaffolding: **Paper:** Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases **URL:** https://arxiv.org/abs/2512.10398 **Date:** December 2025
- `research/066-swe-bench-pro-2025.md` — SWE-Bench Pro 2025: Realistic Agent Evaluation: **Sources:** - SWE-Bench Pro OpenReview paper (2025) - Scale AI Leaderboard (December 2025)
- `research/067-live-swe-agent-evolution.md` — Live-SWE-agent: Self-Evolving Agents: **Paper:** Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly? **URL:** https://arxiv.org/abs/2511.13646 **Date:** November 2025
- `research/068-graphcodeagent.md` — GraphCodeAgent: Dual Graph-Guided Code Generation: **Paper:** GraphCodeAgent: Dual Graph-Guided LLM Agent for Retrieval-Augmented Repo-Level Code Generation **URL:** https://arxiv.org/abs/2504.10046 **Date:** April 2025 (revised November 2025)
- `research/069-adacoder.md` — AdaCoder: Adaptive Planning Multi-Agent Framework: **Paper:** AdaCoder: An Adaptive Planning and Multi-Agent Framework for Function-Level Code Generation **URL:** https://arxiv.org/abs/2504.04220 **Date:** April 5, 2025
- `research/070-structured-cot-code.md` — Structured Chain-of-Thought for Code Generation: **Paper:** Structured Chain-of-Thought Prompting for Code Generation **URL:** https://arxiv.org/abs/2305.06599 / https://dl.acm.org/doi/10.1145/3690635 **Date:** 2023 (published ACM 2025)
- `research/071-self-correction-rl.md` — Self-Correction via Reinforcement Learning 2025: **Sources:** - SCoRe: Self-Correction via Reinforcement Learning (ICLR 2025) - FTR: Feedback-Triggered Regeneration (September 2025)
- `research/072-ai-code-review-2025.md` — AI Code Review 2025: State of Practice: **Sources:** - BitsAI-CR: Automated Code Review via LLM (FSE 2025, ByteDance) - "State of AI Code Review 2025" (Pullflow analysis)
- `research/073-mcp-tool-calling.md` — Model Context Protocol (MCP) and Tool Calling 2025: **Sources:** - MCP-BENCH: Benchmarking LLM Agents on MCP Tasks (November 2025) - "Building AI Agents with MCP" (Developer Guide 2025)
- `research/README.md` — LLM Planning for Code - Research Summaries: Research papers read in full and summarized with practical implications for the Knowledge & Vibes planning system.
- `research/TEMPLATE.md` — Research Document Template: Use this template when adding new research papers to the library.

### Docs: Other

- `docs/VIDEO_SCRIPT_20MIN.md` — Knowledge & Vibes — 20‑Minute Deep Dive (Spoken Script): **Audience:** AI‑savvy, not professional developers **Tone:** clear, grounded, confident; “systems thinking” **Target length:** ~20 minutes (adjust pacing as needed)
- `docs/VIDEO_SCRIPT_X_TWITTER.md` — Knowledge & Vibes — X/Twitter Video Script (60–90s): If you’ve ever “vibe‑coded” with AI—got a demo fast, then watched it collapse—here’s why:
- `docs/VIDEO_VISUAL_NOTES.md` — Knowledge & Vibes — Visual + Editing Notes (20‑min Deep Dive): - Visual rhythm: alternate between (1) talking head, (2) repo screen captures, (3) simple motion graphics for key ideas. - On-screen text: short, high-contrast phrases; avoid paragraphs. - Rule: when you mention a file path, show it on screen for 2–3 seconds.

### Other Files

- `.claude/hooks/on-file-write.sh` — on-file-write.sh: Shell script.
- `.claude/settings.local.json` — settings.local.json: JSON configuration.
- `.gitignore` — .gitignore: Ignore rules: cloned tool repos, local AI configs, editor/temp artifacts.
- `LICENSE` — License: MIT license for this repository.
- `scripts/generate_repo_tour.py` — generate_repo_tour.py

## Excluded Paths

- `.bv_backups/` — Ignored (git/caches/backups).
- `.git/` — Ignored (git/caches/backups).
- `.tmp_gocache/` — Ignored (git/caches/backups).
- `.tmp_gomodcache/` — Ignored (git/caches/backups).

## Regenerate

```bash
python3 scripts/generate_repo_tour.py
```
