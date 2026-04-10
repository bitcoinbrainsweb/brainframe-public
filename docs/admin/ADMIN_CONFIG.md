# ADMIN_CONFIG.md
Change rarely and deliberately.

## IDENTITY
Project: Brainframe General Chat (admin)
Owner: Dave Bradley — dave@bitcoinbrains.com — Calgary, AB
AI role: Planning, architecture, critique, document generation, prompt design, research

## REPOS
- brainframe-public: bitcoinbrainsweb/brainframe-public
- Nightwatch: bitcoinbrainsweb/great-horn-aml-nightwatch
- Axiom: bitcoinbrainsweb/axiom
- Mambamode: bitcoinbrainsweb/mambamode

## KEY CONTACTS
- Amanda Haverluck — calendar, Bitcoin Rodeo logistics
- Josh Curlett — Block Rewards CEO
- Travis MacDonald — Block Rewards CFO (DocuSign resolutions)
- Scott Reeves — Block Rewards lawyer, Tingle Merrett
- Adam O'Brien — Bitcoin Well

## TOOL ROUTING
| Task | Tool |
|------|------|
| Planning, architecture, critique | Claude |
| Code implementation | Cursor |
| Long research, secondary opinion | ChatGPT |
| Rapid prototyping | Base44 |
| File reads/writes/merges | GitHub API via bash |

## UPCOMING
- BTC Prague 2026
- Bitcoin Ireland Conference 2026 (Dave speaking)
- Larine archive review: May 8, 2026

## AGENT REGISTRY
| Agent | Can Do | Cannot Do | Authority |
|-------|--------|-----------|-----------|
| Claude | Plan, critique, generate docs, GitHub API ops, research | Implement code, autonomous irreversible actions | Level 1-3 |
| Cursor | All code implementation, SANITYCHECK/RESULT/GATE artifacts | Architecture decisions, merges without GATE | Level 3 |
| Dave | Everything | — | Final authority |


---

**Token optimization standard:** `brainframe-public/docs/TOKEN_OPTIMIZATION.md` — load on demand, not every session.

## SESSION BOOT GATE ADDITION
At session boot, after fetching STATE, run SYNC_CONTAMINATION_CHECK:
- Scan for unexpected brainframe-public mirror files appearing in project repos (Nightwatch, Axiom, Mambamode, Coinbeast)
- Flag immediately if docs/admin/ content found outside brainframe-public
- Known risk: GitHub Actions sync pushes brainframe-public content into all project repos


---

## STANDING RULES

### Document Decisions, Not Activity
Document: what was decided, what standard was set, what capability was confirmed, and why. Do NOT document: that something happened, status updates, or activity logs (those belong in ADMIN_LOG.md). Rule: if a future Claude session would need to know it to make a correct decision, write it down. If it is just a record of work done, log it — do not embed it in config files.

---

## LOCAL TOOLCHAIN SETTINGS

### ENABLE_TOOL_SEARCH (Claude Code CLI)
Setting that lazy-loads MCP tool definitions — tools are only fetched when Claude actually needs them, saving thousands of prompt tokens per session.

**How to enable (one-time, per machine):**
Add to :
```json
{
  "ENABLE_TOOL_SEARCH": true
}
```
Must be set manually on every machine running Claude Code CLI. Applies globally across all projects.
**Source:** Validated by multiple practitioners (GPT Deep Research sweep, 2026-04-10). Confirmed no downside risk.

---

## CLAUDE API INFRA STANDARDS

### Prompt Caching
When any project adds direct Claude API calls, prompt caching must be implemented from day one — not retrofitted.

**Standard:** Set  on static prompt blocks (system prompt, document context, tool definitions). Claimed benefit: up to 90% cost reduction and 50% latency reduction on repetitive calls.

**Applies to:** Any project making Claude API calls server-side (Nightwatch, Mambamode backend, Winston, Coinbeast — when applicable).
**Status:** No projects currently make server-side Claude API calls (confirmed 2026-04-10). Document and implement at first API integration point.
**Reference:** Anthropic prompt caching docs — verify exact syntax before implementing.
**Source:** GPT Deep Research sweep, 2026-04-10.
