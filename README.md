# Knowledge & Vibes

**The production-grade framework for multi-agent AI development.**

Most AI coding fails. Not because models are weak, but because confidence doesn't equal correctness. The best models solve only 23% of realistic software tasks. 40% of AI-generated code contains security vulnerabilities. Extended self-correction makes things *worse*, not better.

This framework exists because **workflow beats prompting**. You can't prompt your way to reliability—but you can build a system where failures get caught before they matter.

---

## What You Get

| Problem | Solution |
|---------|----------|
| AI builds the wrong thing | **North Star Cards** anchor intent before coding starts |
| Requirements get dropped mid-project | **Beads** track every task with dependencies and verification |
| Multiple agents step on each other | **Agent Mail** coordinates work, prevents conflicts |
| AI introduces vulnerabilities | **UBS** scans every commit, blocks unsafe code |
| "It works" isn't evidence | **TDD-first protocol** with mandatory test coverage |
| Sessions lose context | **CASS** searches past solutions; **cm** retrieves patterns |

Every protocol is backed by research. Every tool addresses a specific failure mode.

---

## Quick Start

### 1. Install the Tools

```bash
# Core tools
pipx install beads-cli
pipx install beads-viewer
pipx install ubs-cli
pipx install cass-cli
pipx install context-memory

# Verify installation
bd --version && bv --version && ubs --version
```

Full setup (including MCP servers for Claude): **[Setup Guide](./docs/guides/SETUP_GUIDE.md)**

### 2. Initialize a Project

```bash
cd your-project
bd init
curl -o AGENTS.md https://raw.githubusercontent.com/Mburdo/knowledge_and_vibes/main/templates/AGENTS_TEMPLATE.md
git add .beads/ AGENTS.md && git commit -m "Initialize Knowledge & Vibes"
```

### 3. Run a Session

```bash
/prime              # Register agent, check inbox, discover tasks
/next-bead          # Claim work, reserve files, announce [CLAIMED]
# ... implement with TDD ...
ubs --staged        # Security scan (mandatory)
bd close <id>       # Complete task, release files, announce [CLOSED]
/calibrate          # Between phases: check for drift
```

---

## The Core Idea

> **Truth lives outside the model.**

The AI's confident output is not truth. Truth is tests that pass, code that compiles, documentation that exists. Everything else is a hypothesis requiring verification.

This framework enforces that distinction through:

- **Explicit artifacts** — North Star, requirements, decisions recorded before coding
- **Mandatory verification** — Tests before implementation, security scans before commit
- **Structured coordination** — File reservations, claim/close announcements, calibration gates
- **Bounded iteration** — Max 3 repair attempts (research shows more makes things worse)

The result: **a system where it's hard to be wrong**, even when individual AI outputs are fallible.

---

## Documentation

### Start Here

| Document | What You'll Learn |
|----------|-------------------|
| **[Setup Guide](./docs/guides/SETUP_GUIDE.md)** | Install all tools, configure MCP servers |
| **[START_HERE.md](./START_HERE.md)** | The reading order and system overview |
| **[Glossary](./GLOSSARY.md)** | Every term defined |

### The Workflow

| Document | What You'll Learn |
|----------|-------------------|
| **[Evidence-Based Guide](./docs/workflow/EVIDENCE_BASED_GUIDE.md)** | The complete 10-stage pipeline |
| **[Protocols](./docs/workflow/PROTOCOLS.md)** | 18 repeatable procedures for every situation |
| **[Decomposition](./docs/workflow/DECOMPOSITION.md)** | Breaking plans into executable tasks |

### Going Deeper

| Document | What You'll Learn |
|----------|-------------------|
| **[Planning Deep Dive](./docs/workflow/PLANNING_DEEP_DIVE.md)** | From vague idea to complete plan |
| **[Philosophy](./docs/workflow/PHILOSOPHY.md)** | Why this approach works |
| **[Research](./research/README.md)** | 73 papers summarized |

---

## The Toolkit

### CLI Tools

| Tool | Purpose | Key Command |
|------|---------|-------------|
| **Beads** (`bd`) | Task tracking with dependencies | `bd ready --json` |
| **Beads Viewer** (`bv`) | Graph analysis, next-task recommendations | `bv --robot-next` |
| **UBS** | Security scanner | `ubs --staged` |
| **CASS** | Session search | `cass search "query" --robot` |
| **cm** | Context memory | `cm context "task" --json` |

### MCP Servers

| Server | Purpose |
|--------|---------|
| **Agent Mail** | Multi-agent coordination, file reservations, messaging |
| **Warp-Grep** | Fast parallel codebase search |
| **Exa** | Web search for current documentation |

---

## Templates

| Template | When to Use |
|----------|-------------|
| **[North Star Card](./templates/NORTH_STAR_CARD_TEMPLATE.md)** | Start of every project |
| **[Requirements](./templates/REQUIREMENTS_TEMPLATE.md)** | Defining what to build |
| **[Decisions (ADRs)](./templates/DECISIONS_ADRS_TEMPLATE.md)** | Recording architectural choices |
| **[AGENTS.md](./templates/AGENTS_TEMPLATE.md)** | Agent instructions for your repo |

See **[TEMPLATES.md](./TEMPLATES.md)** for the complete index.

---

## Multi-Agent Coordination

When multiple agents work simultaneously:

1. **Reserve files before editing** — `file_reservation_paths()` prevents conflicts
2. **Announce claims** — `[CLAIMED] bd-123` tells others what's taken
3. **Announce completions** — `[CLOSED] bd-123` releases work
4. **Check inbox before claiming** — Avoid duplicate effort
5. **Calibrate between phases** — Catch drift before it compounds

See **[Orchestrator-Worker Pattern](./docs/guides/ORCHESTRATOR_SUBAGENT_PATTERN.md)** for the full coordination model.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `bd: command not found` | `export PATH="$HOME/.local/bin:$PATH"` |
| `bv` hangs | Use `--robot-*` flags (never bare `bv`) |
| CASS finds nothing | `cass index --full` |
| UBS errors | `ubs doctor --fix` |

**Health check:** `bd doctor && cm doctor && ubs doctor && cass health`

---

## Repository Structure

```
knowledge_and_vibes/
├── docs/
│   ├── guides/        # Setup, tutorial, migration
│   └── workflow/      # Protocols, planning, philosophy
├── templates/         # North Star, requirements, ADRs
├── research/          # 73 paper summaries
└── .claude/
    ├── commands/      # /prime, /calibrate, /next-bead
    ├── rules/         # Safety guardrails
    ├── skills/        # On-demand playbooks
    └── templates/     # Runtime templates
```

---

## About

This framework is the distillation of three years of building with AI—starting from zero.

When GPT-3.5 launched, I was in high finance. I couldn't write a line of code. But I recognized immediately that AI was going to fundamentally change how things get built, and I wanted to be part of it.

So I went all in. Not with tutorials or bootcamps, but with a first principles approach: What can these models actually do? Where do they fail? How do you extract every ounce of capability while catching the inevitable mistakes?

The early days were rough. The models were weaker. The tooling didn't exist. Every technique had to be discovered through trial and error. But I stayed in it—learning, building, refining—session after session, project after project.

Three years later, I'm shipping complex applications with real users and real revenue. Not because I became a traditional developer, but because I learned how to work *with* AI in a way that produces reliable results.

This framework is everything I've learned, systematized. The protocols that prevent the common failures. The tools that catch mistakes before they ship. The workflow that turns "AI-assisted coding" from a gamble into a repeatable process.

If you're technical, this will make you faster. If you're not, this is proof that you can build real things anyway.

**Follow my work:** [@YachtsmanCap](https://x.com/YachtsmanCap)

---

## License

MIT
