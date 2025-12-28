<div align="center">

# Setup Guide

### Install the Knowledge & Vibes toolchain and verify everything works

</div>

---

## 🗂️ What Goes Where (Read This First)

Knowledge & Vibes has three types of components. Understanding this prevents confusion:

### 1. Global Tools (Install Once, Use Everywhere)

These CLI tools install to `~/.local/bin/` and work across all your projects:

| Tool | What It Is | Install Location |
|:-----|:-----------|:-----------------|
| `bd` | Task tracker CLI | `~/.local/bin/bd` |
| `bv` | Task graph analyzer | `~/.local/bin/bv` |
| `ubs` | Security scanner | `~/.local/bin/ubs` |
| `cass` | Session search | `~/.local/bin/cass` |
| `cm` | Context memory | `~/.local/bin/cm` |
| `ntm` | Terminal manager | `~/.local/bin/ntm` |

**MCP servers** also install globally (user-level):
- `exa` — Web and code search
- `morph-fast-tools` — Parallel codebase search
- `mcp-agent-mail` — Multi-agent coordination

### 2. Per-Project Files (Copy Into Each Project)

These files go into YOUR project's repository:

```
your-project/
├── .beads/                    # Task database (created by `bd init`)
│   └── issues.jsonl           # Your tasks live here
├── .claude/
│   ├── commands/              # Slash commands (/prime, /calibrate, etc.)
│   │   ├── prime.md
│   │   ├── next-bead.md
│   │   ├── calibrate.md
│   │   ├── decompose-task.md
│   │   └── ground.md
│   ├── rules/                 # Agent behavior rules
│   │   ├── safety.md          # File deletion protection
│   │   ├── beads.md           # Task claiming protocol
│   │   └── multi-agent.md     # Coordination protocol
│   ├── skills/                # Skill definitions (agent capabilities)
│   │   ├── prime/
│   │   ├── next-bead/
│   │   ├── calibrate/
│   │   ├── execute/
│   │   ├── bead-workflow/
│   │   └── ... (13 skills total)
│   └── templates/             # Runtime templates for agent output
│       ├── beads/
│       ├── planning/
│       └── calibration/
├── AGENTS.md                  # Project-specific agent instructions
└── PLAN/                      # Your planning artifacts (optional)
    ├── 00_north_star.md
    └── 01_requirements.md
```

### 3. Reference Material (Stays in K&V Repo)

The `knowledge_and_vibes` repository itself contains documentation you READ but don't copy:

- `docs/workflow/*` — How the system works (philosophy, pipeline, protocols)
- `docs/guides/*` — Tutorials and setup guides
- `research/*` — Evidence base (73 research summaries)
- `templates/*` — Templates to ADAPT (not copy verbatim)

**You don't copy these into your project.** You reference them when needed.

---

## 🎯 What Is This?

Knowledge & Vibes is a system for building software with AI assistance. Instead of chatting with AI and hoping for the best, this system gives you:

| Capability | What It Does |
|:-----------|:-------------|
| **Structured planning** | So the AI builds what you actually want |
| **Task tracking** | So nothing gets forgotten |
| **Security scanning** | So you don't ship broken or dangerous code |
| **Multi-agent coordination** | So multiple AI agents can work together without conflicts |

---

## ✅ Before You Start

### Requirements

| Requirement | How to Check | How to Get It |
|:------------|:-------------|:--------------|
| **macOS or Linux** | You're on one of these | Windows users: use WSL2 |
| **Terminal access** | Can you open Terminal? | macOS: Cmd+Space → "Terminal" |
| **Claude Code** | `claude --version` | [Install Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| **Git** | `git --version` | macOS: `xcode-select --install` |

### Quick Check

```bash
claude --version && git --version && echo "✓ Ready to continue"
```

If you see version numbers and "Ready to continue", proceed.

---

## 📦 What You're Installing

| Tool | What It Does | Why You Need It |
|:-----|:-------------|:----------------|
| **bd** (Beads) | Task tracker | Tracks what needs to be done, what's blocked, what's finished |
| **bv** (Beads Viewer) | Task analyzer | Recommends what to work on next, finds problems in your task graph |
| **ubs** | Security scanner | Catches bugs and vulnerabilities before you ship |
| **cass** | Session search | Searches your past AI conversations to reuse solutions |
| **cm** | Context memory | Learns patterns from your work to help future sessions |
| **ntm** | Terminal manager | Runs multiple AI agents in parallel (optional) |
| **Agent Mail** | Agent coordinator | Lets multiple AI agents communicate without stepping on each other |

---

## Step 1: Install the Core Tools

Copy and paste this entire block into Terminal:

```bash
# Beads (bd, bv) and Agent Mail
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/mcp_agent_mail/main/scripts/install.sh | bash -s -- --dir "$HOME/mcp_agent_mail" --yes

# CASS (session search)
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/coding_agent_session_search/main/install.sh | bash -s -- --easy-mode

# UBS (security scanner)
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/ultimate_bug_scanner/master/install.sh | bash -s -- --easy-mode

# NTM (terminal manager) - optional but recommended
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/ntm/main/install.sh | bash
```

### Install cm (Context Memory)

Choose the right command for your system:

<table>
<tr>
<td width="33%" valign="top">

**Mac (Apple Silicon)**

M1, M2, M3, M4

```bash
mkdir -p ~/.local/bin
curl -L https://github.com/Dicklesworthstone/cass_memory_system/releases/latest/download/cass-memory-macos-arm64 -o ~/.local/bin/cm
chmod +x ~/.local/bin/cm
```

</td>
<td width="33%" valign="top">

**Mac (Intel)**

Older Macs

```bash
mkdir -p ~/.local/bin
curl -L https://github.com/Dicklesworthstone/cass_memory_system/releases/latest/download/cass-memory-macos-x64 -o ~/.local/bin/cm
chmod +x ~/.local/bin/cm
```

</td>
<td width="33%" valign="top">

**Linux**

x64

```bash
mkdir -p ~/.local/bin
curl -L https://github.com/Dicklesworthstone/cass_memory_system/releases/latest/download/cass-memory-linux-x64 -o ~/.local/bin/cm
chmod +x ~/.local/bin/cm
```

</td>
</tr>
</table>

> **Not sure which Mac?** Apple menu → "About This Mac". If it says M1/M2/M3/M4, use Apple Silicon.

### Add Tools to Your PATH

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

*(Use `.bashrc` instead if you use bash)*

---

## Step 2: Verify Installation

```bash
bd --version && bv --version && cass --version && cm --version && ubs --version && echo "✓ All tools installed!"
```

### Troubleshooting

| Problem | Solution |
|:--------|:---------|
| `command not found: bd` | Run: `source ~/.zshrc` then try again |
| `command not found: cm` | Check Step 1 - did you run the right command for your system? |
| `Permission denied` | Run: `chmod +x ~/.local/bin/*` |
| Script hangs or fails | Check your internet connection and try again |
| `curl: command not found` | `brew install curl` (requires [Homebrew](https://brew.sh)) |

---

## Step 3: Set Up Search Tools (Optional)

These tools let the AI search the web and your codebase more effectively.

### Get API Keys

| Service | Where to Get It | Free Tier |
|:--------|:----------------|:----------|
| **Exa** | https://dashboard.exa.ai | 1000 searches/month |
| **Morph** | https://morphllm.com | Available |

### Install MCP Servers

Replace `<your-key>` with your actual keys:

```bash
# Exa - web and code search
claude mcp add exa -s user -e EXA_API_KEY=<your-exa-key> -- npx -y @anthropic-labs/exa-mcp-server

# Morph (Warp-Grep) - parallel codebase search
claude mcp add morph-fast-tools -s user -e MORPH_API_KEY=<your-morph-key> -e ALL_TOOLS=true -- npx -y @morphllm/morphmcp
```

### Verify

```bash
claude mcp list
```

You should see `exa` and `morph-fast-tools` listed.

---

## Step 4: Initialize Your Project

<table>
<tr>
<td width="50%" valign="top">

### Option A: New Project

```bash
mkdir my-project
cd my-project
git init
bd init
```

</td>
<td width="50%" valign="top">

### Option B: Existing Project

```bash
cd /path/to/your/project
bd init
```

</td>
</tr>
</table>

This creates `.beads/` with an empty task database.

---

## Step 5: Copy Project Files

Now copy the files your agents need. Choose your setup level:

### Minimal Setup (Solo Agent, Simple Projects)

```bash
# Agent instructions
curl -o AGENTS.md https://raw.githubusercontent.com/Mburdo/knowledge_and_vibes/master/templates/AGENTS_TEMPLATE.md

# Essential slash commands
mkdir -p .claude/commands
for cmd in prime next-bead calibrate decompose-task ground; do
  curl -fsSL -o .claude/commands/$cmd.md \
    https://raw.githubusercontent.com/Mburdo/knowledge_and_vibes/master/.claude/commands/$cmd.md
done

# Safety rules (prevents accidental file deletion)
mkdir -p .claude/rules
curl -fsSL -o .claude/rules/safety.md \
  https://raw.githubusercontent.com/Mburdo/knowledge_and_vibes/master/.claude/rules/safety.md
```

### Full Setup (Multi-Agent, Complex Projects)

```bash
# Clone the K&V repo temporarily to copy files
git clone --depth 1 https://github.com/Mburdo/knowledge_and_vibes.git /tmp/kv-setup

# Copy agent instructions
cp /tmp/kv-setup/templates/AGENTS_TEMPLATE.md ./AGENTS.md

# Copy all commands, rules, skills, and templates
cp -r /tmp/kv-setup/.claude/commands .claude/
cp -r /tmp/kv-setup/.claude/rules .claude/
cp -r /tmp/kv-setup/.claude/skills .claude/
cp -r /tmp/kv-setup/.claude/templates .claude/

# Clean up
rm -rf /tmp/kv-setup
```

### What You Just Copied

| Directory | Files | Purpose |
|:----------|:------|:--------|
| `.claude/commands/` | 6 files | Slash commands like `/prime`, `/calibrate` |
| `.claude/rules/` | 3 files | Safety rules, bead protocol, multi-agent protocol |
| `.claude/skills/` | 13 dirs | Full skill definitions for each capability |
| `.claude/templates/` | 3 dirs | Output templates for beads, planning, calibration |
| `AGENTS.md` | 1 file | Project-specific agent instructions (EDIT THIS) |

### Customize AGENTS.md

Open `AGENTS.md` and update it for YOUR project:

```markdown
# Project: [YOUR PROJECT NAME]

## Tech Stack
- [Your languages, frameworks, tools]

## Architecture
- [Key directories and their purpose]

## Conventions
- [Your coding standards, naming conventions]

## What NOT To Do
- [Project-specific restrictions]
```

### Commit

```bash
git add .beads/ .claude/ AGENTS.md
git commit -m "Initialize Knowledge & Vibes"
```

---

## Step 6: Test Everything

### Test Task Tracking

```bash
bd create "Test task - delete me" -t task -p 2   # Create
bd list                                            # View
bd delete bd-XXXX --yes                           # Delete (use actual ID)
```

### Test Viewer

```bash
bv --robot-next
```

### Test Security Scanner

```bash
echo 'password = "secret123"' > test.py
ubs test.py
rm test.py
```

Should flag the hardcoded password.

### Test Session Search

```bash
cass index --full
cass search "test" --robot --limit 3
```

### Test Slash Commands

Start Claude Code and type `/prime`. The agent should run a startup checklist.

---

## ✅ You're Done!

### What's Now In Your Project

```
your-project/
├── .beads/                    ← Task database
├── .claude/
│   ├── commands/              ← Slash commands (/prime, /calibrate, etc.)
│   ├── rules/                 ← Safety and coordination rules
│   ├── skills/                ← Agent capabilities (full setup only)
│   └── templates/             ← Output templates (full setup only)
└── AGENTS.md                  ← YOUR project instructions (edit this!)
```

### Global Tools You Installed

| Tool | Command | Purpose |
|:-----|:--------|:--------|
| Beads | `bd` | Task tracking |
| Beads Viewer | `bv --robot-next` | Task recommendations |
| Security Scanner | `ubs --staged` | Catch bugs before commit |
| Session Search | `cass search "query" --robot` | Find past solutions |
| Context Memory | `cm context "task" --json` | Get relevant patterns |

### Quick Reference

```bash
# Task management
bd create "Task name" -t task -p 2   # Create a task
bd ready --json                       # See available tasks
bd update bd-XXX --status in_progress # Claim a task
bd close bd-XXX --reason "Done"       # Close a task

# Analysis
bv --robot-next              # Get recommended next task
bv --robot-triage            # Get full analysis

# Security
ubs --staged                 # Scan before committing

# History
cass search "query" --robot  # Search past sessions
cm context "task" --json     # Get context for a task
```

### What's Next?

| Step | Resource |
|:-----|:---------|
| 1. Read the workflow | [START_HERE.md](../../START_HERE.md) → [Pipeline Reference](../workflow/IDEATION_TO_PRODUCTION.md) |
| 2. Try the tutorial | [Tutorial](./TUTORIAL.md) |
| 3. Create your first plan | [North Star Template](../../templates/NORTH_STAR_CARD_TEMPLATE.md) |

### First Session Checklist

1. Open Claude Code in your project directory
2. Type `/prime` to start a session
3. The agent will register, check for tasks, and orient itself
4. Ask the agent to help you create your first North Star card

---

## 📎 Appendix

<details>
<summary><strong>Updating Tools</strong></summary>

```bash
# Update Beads Viewer
bv --check-update && bv --update --yes

# Other tools - rerun their install scripts
# They detect existing installs and upgrade
```

</details>

<details>
<summary><strong>Uninstalling</strong></summary>

```bash
# Remove binaries
rm -rf ~/.local/bin/{bd,bv,cass,cm,ubs,ntm,am}
rm -rf ~/mcp_agent_mail

# Remove MCP servers
claude mcp remove exa
claude mcp remove morph-fast-tools

# Remove project files (run in your project)
rm -rf .beads/ .claude/ AGENTS.md
```

</details>

<details>
<summary><strong>Getting Help</strong></summary>

| Problem | Where to Go |
|:--------|:------------|
| Tool not working | Check troubleshooting above |
| Confused about workflow | Read [START_HERE.md](../../START_HERE.md) |
| Bug in the tools | GitHub issues for each tool |
| Questions about the system | Open an issue on the knowledge_and_vibes repo |

</details>
