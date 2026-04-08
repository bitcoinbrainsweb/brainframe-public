# TOOL_ROLES.md
Brainframe v2.0 | April 2026
Load at session start. Replaces MODEL_ROUTING.md.

---

## Claude
**Primary role:** Planning, architecture, critique, document generation, Cursor prompt design, executive assistant.

**Use for:**
- Architecture decisions and critique
- Sequencing and roadmap review
- Generating Cursor prompts
- Generating Brainframe files and project documents
- Post-build critique, pressure-testing, challenging assumptions
- Gmail, Google Drive, calendar (admin sessions only)

**Never use for:**
- Code implementation
- Direct interaction with Cursor or Base44
- Autonomous commits or deploys

**Model selection:** See `docs/TOKEN_OPTIMIZATION.md`. Default Sonnet 4.6. Escalate to Opus for architecture/deep reasoning. Haiku for structured/data ops.

---

## ChatGPT / GPT Deep Research
**Primary role:** Long autonomous research, secondary opinion, operationalization of plans.

**Use for:**
- Multi-hour research tasks (Deep Research mode)
- Generating Brainframe system files when explicitly assigned
- Secondary opinion on architecture decisions
- Critique prompts (GPT-4o via critique spec skill)

**Never use for:**
- Primary architecture decisions
- Overriding Claude outputs without Dave review
- Autonomous commits or deploys

---

## Perplexity
**Primary role:** Fast web-grounded research and source verification.

**Use for:**
- Real-time factual lookups and source sweeps
- AI pulse source scanning
- Rapid competitive or market research
- Verifying claims before acting on them

**Never use for:**
- Architecture decisions
- Code generation
- Replacing Claude for planning

**Key:** Perplexity key in project memory (Mambamode). Use sonar-pro for best results.

---

## Cursor
**Primary role:** All code implementation. Cursor 3 (April 2026) supports parallel agents across repos.

**Use for:**
- Writing and modifying code
- Repository-level changes
- Debugging
- Generating SANITYCHECK / REVIEW / RESULT artifacts
- Parallel agents across Nightwatch / Axiom / Mambamode simultaneously (Cursor 3)

**Never use for:**
- Architecture decisions
- Planning or roadmap work
- Autonomous merges or deploys without Dave approval

**Prompt requirements:**
- Always include branch name
- Always include scope (in and out)
- Always include expected artifacts
- Always define what success looks like
- Risky changes require REVIEW artifact before implementation

**Cursor 3 note:** Parallel agents (Agents Window) allow concurrent upgrades across repos. Use This PC (local) as default environment. Cloud agents when explicitly needed.

---

## Base44
**Primary role:** Rapid app prototyping and MCP-connected internal tools.

**Use for:**
- Quick demos and proof of concept builds
- Internal tools with MCP integrations (Gmail, Drive, etc.)
- Prototypes that will be rebuilt properly later

**Never use for:**
- Production systems unless explicitly decided per project
- Systems requiring complex graph relationships at scale

---

## Make
**Primary role:** Brainframe file automation and staging commits.

**May do:**
- Generate files, stage git changes, prepare system artifacts
- Commit Brainframe file updates to staging branch only

**May never do:**
- Merge branches, deploy code, modify production infrastructure
- Commit to main without Dave approval

---

## WORKFLOW SEQUENCE

Standard development flow:
```
Claude designs → Dave reviews → Cursor implements → Dave commits → Dave pushes → Dave deploys
```

Parallel agent flow (Cursor 3):
```
Claude designs all upgrades → Dave reviews → Cursor runs agents in parallel per repo → Dave reviews artifacts → Dave commits
```

Brainframe file update flow:
```
Claude proposes → GitHub API → brainframe-public main directly (no PR)
```

---

## CONTEXT LOADING BY TOOL

| Tool | Always load | Load on demand |
|------|-------------|----------------|
| Claude | GLOBAL_RULES.md + STYLE_RULES.md | State files, skills, specs |
| ChatGPT | Task-specific context via paste | Brainframe files if assigned |
| Perplexity | Query only | Source list (ai-pulse-sources.md) |
| Cursor | Cursor prompt only | Referenced spec files |
| Base44 | App context | MCP server configs |
| Make | Workflow config only | — |

---

## MODEL SELECTION

For Claude model tier (Opus / Sonnet / Haiku), prompt caching, and token cost standards — see `docs/TOKEN_OPTIMIZATION.md`. This file governs which tool to use. That file governs which model within the Claude API.
