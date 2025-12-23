# Setup Guide

This guide installs the Knowledge & Vibes toolchain and verifies everything works.

---

## What Is This?

Knowledge & Vibes is a system for building software with AI assistance. Instead of chatting with AI and hoping for the best, this system gives you:

- **Structured planning** — So the AI builds what you actually want
- **Task tracking** — So nothing gets forgotten
- **Security scanning** — So you don't ship broken or dangerous code
- **Multi-agent coordination** — So multiple AI agents can work together without conflicts

This guide installs the tools that make it work.

---

## Before You Start

### What You Need

| Requirement | How to Check | How to Get It |
|-------------|--------------|---------------|
| **macOS or Linux** | You're on one of these | Windows users: use WSL2 |
| **Terminal access** | Can you open Terminal? | macOS: Cmd+Space, type "Terminal" |
| **Claude Code installed** | Run `claude --version` | [Install Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| **Git installed** | Run `git --version` | macOS: `xcode-select --install` |

### Check Your Setup

Open Terminal and run:

```bash
claude --version && git --version && echo "✓ Ready to continue"
```

If you see version numbers and "Ready to continue", proceed. If not, install the missing pieces first.

---

## What You're Installing

Here's what each tool does (so you're not blindly running scripts):

| Tool | What It Does | Why You Need It |
|------|--------------|-----------------|
| **bd** (Beads) | Task tracker | Tracks what needs to be done, what's blocked, what's finished |
| **bv** (Beads Viewer) | Task analyzer | Recommends what to work on next, finds problems in your task graph |
| **ubs** | Security scanner | Catches bugs and vulnerabilities before you ship |
| **cass** | Session search | Searches your past AI conversations to reuse solutions |
| **cm** | Context memory | Learns patterns from your work to help future sessions |
| **ntm** | Terminal manager | Runs multiple AI agents in parallel (optional, for advanced use) |
| **Agent Mail** | Agent coordinator | Lets multiple AI agents communicate without stepping on each other |

---

## Step 1: Install the Core Tools

Copy and paste this entire block into Terminal:

```bash
# This installs: bd, bv, Agent Mail, and the am command
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/mcp_agent_mail/main/scripts/install.sh | bash -s -- --dir "$HOME/mcp_agent_mail" --yes

# This installs: cass (session search)
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/coding_agent_session_search/main/install.sh | bash -s -- --easy-mode

# This installs: ubs (security scanner)
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/ultimate_bug_scanner/master/install.sh | bash -s -- --easy-mode

# This installs: ntm (terminal manager) - optional but recommended
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/ntm/main/install.sh | bash
```

**What's happening:** These scripts download and install each tool to your system. They're safe to run multiple times (they skip if already installed).

### Install cm (Context Memory)

This one depends on your computer type:

**Mac with Apple Silicon (M1/M2/M3/M4):**
```bash
mkdir -p ~/.local/bin
curl -L https://github.com/Dicklesworthstone/cass_memory_system/releases/latest/download/cass-memory-macos-arm64 -o ~/.local/bin/cm
chmod +x ~/.local/bin/cm
```

**Mac with Intel:**
```bash
mkdir -p ~/.local/bin
curl -L https://github.com/Dicklesworthstone/cass_memory_system/releases/latest/download/cass-memory-macos-x64 -o ~/.local/bin/cm
chmod +x ~/.local/bin/cm
```

**Linux:**
```bash
mkdir -p ~/.local/bin
curl -L https://github.com/Dicklesworthstone/cass_memory_system/releases/latest/download/cass-memory-linux-x64 -o ~/.local/bin/cm
chmod +x ~/.local/bin/cm
```

**Not sure which Mac you have?** Click the Apple menu → "About This Mac". If it says "Apple M1/M2/M3/M4", you have Apple Silicon. Otherwise, you have Intel.

### Add Tools to Your PATH

If the tools aren't found after installation, add this to your shell config:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

(If you use bash instead of zsh, replace `.zshrc` with `.bashrc`)

---

## Step 2: Verify Installation

Run this command:

```bash
bd --version && bv --version && cass --version && cm --version && ubs --version && echo "✓ All tools installed!"
```

**Expected output:** Version numbers for each tool, ending with "All tools installed!"

### Troubleshooting

| Problem | Solution |
|---------|----------|
| `command not found: bd` | Run: `source ~/.zshrc` then try again |
| `command not found: cm` | Check Step 1 - did you run the right command for your Mac type? |
| `Permission denied` | Run: `chmod +x ~/.local/bin/*` |
| Script hangs or fails | Check your internet connection and try again |
| "curl: command not found" | Install curl: `brew install curl` (requires [Homebrew](https://brew.sh)) |

---

## Step 3: Set Up Search Tools (Optional but Recommended)

These tools let the AI search the web and your codebase more effectively. They require free API keys.

### Get API Keys

1. **Exa** (web and code search): https://dashboard.exa.ai
   - Sign up, go to API Keys, create one
   - Free tier: 1000 searches/month

2. **Morph** (codebase search): https://morphllm.com
   - Sign up, get your API key
   - Free tier available

### Install the MCP Servers

Replace `<your-exa-key>` and `<your-morph-key>` with your actual keys:

```bash
# Exa - searches the web and code repositories
claude mcp add exa -s user -e EXA_API_KEY=<your-exa-key> -- npx -y @anthropic-labs/exa-mcp-server

# Morph (Warp-Grep) - parallel codebase search
claude mcp add morph-fast-tools -s user -e MORPH_API_KEY=<your-morph-key> -e ALL_TOOLS=true -- npx -y @morphllm/morphmcp
```

**What's an MCP server?** It's a way to give Claude Code extra capabilities. These add web search and advanced code search.

### Verify MCP Setup

```bash
claude mcp list
```

You should see `exa` and `morph-fast-tools` in the list.

---

## Step 4: Initialize Your First Project

Now let's set up a project to use with Knowledge & Vibes.

### Option A: Start a New Project

```bash
mkdir my-project
cd my-project
git init
bd init
```

### Option B: Add to an Existing Project

```bash
cd /path/to/your/project
bd init
```

### Add the Agent Instructions File

This file tells AI agents how to work in your project:

```bash
curl -o AGENTS.md https://raw.githubusercontent.com/Mburdo/knowledge_and_vibes/master/templates/AGENTS_TEMPLATE.md
```

### Commit the Setup

```bash
git add .beads/ AGENTS.md
git commit -m "Initialize Knowledge & Vibes"
```

---

## Step 5: Test That Everything Works

### Test Task Tracking

```bash
# Create a test task
bd create "Test task - delete me" -t task -p 2

# See your tasks
bd list

# Delete the test task (get the ID from bd list, like bd-a1b2)
bd delete bd-XXXX --yes
```

### Test the Viewer

```bash
bv --robot-next
```

This should output a recommendation (or say "no ready tasks" if you deleted the test).

### Test Security Scanning

```bash
echo 'password = "secret123"' > test.py
ubs test.py
rm test.py
```

This should flag the hardcoded password as a security issue.

### Test Session Search

```bash
cass index --full
cass search "test" --robot --limit 3
```

If you have past Claude Code sessions, this searches them. If not, it returns empty results (that's fine).

---

## Step 6: Add Slash Commands (Recommended)

Slash commands give you shortcuts like `/prime` (start a session) and `/calibrate` (check progress).

```bash
mkdir -p .claude/commands

# Download the commands
for cmd in prime next-bead ground decompose-task calibrate; do
  curl -fsSL -o .claude/commands/$cmd.md \
    https://raw.githubusercontent.com/Mburdo/knowledge_and_vibes/master/.claude/commands/$cmd.md
done

git add .claude/commands
git commit -m "Add slash commands"
```

### Test a Slash Command

Start Claude Code and type:

```
/prime
```

The agent should run through a startup checklist.

---

## Step 7: Add Safety Rules (Recommended)

These rules prevent AI agents from accidentally deleting files or running dangerous commands:

```bash
mkdir -p .claude/rules

curl -fsSL -o .claude/rules/safety.md \
  https://raw.githubusercontent.com/Mburdo/knowledge_and_vibes/master/.claude/rules/safety.md

git add .claude/rules
git commit -m "Add safety rules"
```

---

## You're Done!

### What You Installed

| Tool | Command | What It Does |
|------|---------|--------------|
| Beads | `bd` | Task tracking |
| Beads Viewer | `bv --robot-next` | Task recommendations |
| Security Scanner | `ubs --staged` | Catch bugs before commit |
| Session Search | `cass search "query" --robot` | Find past solutions |
| Context Memory | `cm context "task" --json` | Get relevant patterns |

### Quick Reference

```bash
# See available tasks
bd ready --json

# Get recommended next task
bv --robot-next

# Get full analysis
bv --robot-triage

# Scan for security issues before committing
ubs --staged

# Search past sessions
cass search "how did I solve X" --robot

# Get context for a task
cm context "what I'm about to do" --json
```

### What's Next?

1. **Read the workflow:** `START_HERE.md` → `docs/workflow/EVIDENCE_BASED_GUIDE.md`
2. **Try the tutorial:** `docs/guides/TUTORIAL.md`
3. **Create your first plan:** Use the North Star template in `templates/NORTH_STAR_CARD_TEMPLATE.md`

---

## Appendix: Updating Tools

Tools improve over time. Here's how to update them:

```bash
# Update bv (Beads Viewer)
bv --check-update && bv --update --yes

# Update other tools - rerun their install scripts
# They detect existing installs and upgrade
```

---

## Appendix: Uninstalling

If you need to remove everything:

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

---

## Getting Help

| Problem | Where to Go |
|---------|-------------|
| Tool not working | Check the troubleshooting section above |
| Confused about workflow | Read `START_HERE.md` |
| Bug in the tools | GitHub issues for each tool |
| Questions about this system | Open an issue on the knowledge_and_vibes repo |
