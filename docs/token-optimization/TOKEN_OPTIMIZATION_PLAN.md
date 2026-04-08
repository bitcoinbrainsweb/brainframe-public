# TOKEN_OPTIMIZATION_PLAN.md
Dave Bradley — Brainframe AI Workflow
Version: 1.1 | 2026-04-07
Status: ACTIVE

Constraint: every rule must preserve or improve output quality and not slow work.
Grounded in: TOKEN_RESEARCH.md (docs/token-optimization/)

---

## WHAT WE KNOW (relevant to Dave's setup)

- **30 skills × ~50 tokens metadata = ~1,500 tokens at startup** (if lazy loading working)
- **Gmail + Drive MCPs: estimated 1,400–15,000 tokens** — guardrailed to admin sessions only (GLOBAL_RULES 132–134). Never disconnected. Enforced by session type.
- **Base44 MCP: unknown token cost** — measure when possible
- **Full session history re-sent every message** — caching gives 90% discount within 5-min window
- **Skill bodies now trimmed 53–82%** — reference files load on demand from GitHub API
- **Project instructions load in full every session** — cached after first message
- **Context rot begins ~32K tokens** — quality degrades, not just cost

---

## THE PLAN

### TIER 1 — ALREADY DONE (implemented this session)

| Change | Impact |
|--------|--------|
| Skill bodies trimmed 53–82% | Bodies load on demand; smaller = less context when triggered |
| Project-specific content in reference files | Loads only when working on that project |
| Gmail/Drive MCP guardrailed to admin sessions | Eliminates ~1,400–15,000 tokens in non-admin sessions |
| All 30 skill descriptions fixed | Correct triggering = right skills load, wrong ones don't |
| `disable-model-invocation` on 4 destructive skills | Prevents accidental loads |
| quitchat refactored to fetch close procedures | Body 170 → 81 lines |

---

### TIER 2 — SESSION DISCIPLINE (behavioral rules, zero implementation)

Rules 135–137 now in GLOBAL_RULES. Repeated here for visibility.

**RULE: Never use /compact (GLOBAL_RULES 135)**
/compact busts the prompt cache and loses fidelity unpredictably.
If context is getting long: ask Claude to save context to a file, then use a handoff to start fresh.
This is something Claude can already do well — no skill needed. The instruction is: 
"Save your current context to SESSION_HANDOFF.md — include session summary, decisions made, next task, and any open items. Be comprehensive." Then quitchat.

**RULE: No manual file edits during a session (GLOBAL_RULES 136)**
Editing files outside Claude during an active session busts the prompt cache.
Finish the session first, edit externally, then restart.

**RULE: MCP tools are guardrailed, never disconnected (GLOBAL_RULES 137)**
Gmail and Drive: admin sessions only (rules 132–134).
Base44: Nightwatch sessions only.
Never add new MCP connections without evaluating token overhead.
The right model: guardrail by session type, not manual connect/disconnect.

**Batch related questions**
Send multiple related questions in one message — not as follow-ups.
Each follow-up re-sends full history. Three questions in one message costs same as one.

**Keep sessions alive during work**
Cache TTL is 5 minutes. If you step away, cache expires.
For long breaks: quitchat + handoff, start fresh.

**Ultrathink deliberately**
"ultrathink" = 31,999 output tokens billed at 5× input rate.
Only use for: novel architecture decisions, complex multi-hypothesis debugging.
Never for: routine prompts, spec writing, description fixes, document generation.

---

### TIER 3 — PROJECT INSTRUCTIONS COMPRESSION (one-time work, high impact)

**Why:** Project instructions load in full every session, cached after first message.
Over 50 lines = bloated startup cost every session forever.

**Key constraint:** Each project writes its own instructions only.
No cross-project instructions. No shared directives in project files.
Global directives live in GLOBAL_RULES.md — project instructions just pointer to it.

**Action — Nightwatch first (most sessions, highest ROI):**
1. Read current Nightwatch project instructions
2. Strip anything that belongs in GLOBAL_RULES instead
3. Strip anything duplicated from skill descriptions
4. Compress what remains: "Rewrite for maximum token density without losing directive content. Use imperative form. No explanations."
5. Target: under 50 lines

**Same for Admin project instructions.**

**Axiom and Coinbeast:** Do when starting active work on those projects.
Don't compress Axiom instructions speculatively — do it at the start of an Axiom session when the context is fresh.

**Status:** Not yet done. Next Nightwatch session should start with this.

---

### TIER 4 — CURSOR PROMPT CONTEXT BLOCKS (ongoing discipline)

KERNEL framework measured 58% token reduction. Your prompt standard already enforces most of it.
One gap: Context blocks in Cursor prompts are sometimes over 5 lines.

Rule: If a context block exceeds 5 lines, challenge whether Cursor actually needs it.
Cursor reads the repo. It doesn't need a recap of what you've already built unless the change is in a non-obvious location.

---

### TIER 5 — DEPENDENCY MAP FOR COINBEAST (future trigger)

When Coinbeast codebase exceeds ~50 files or Cursor starts making cross-file mistakes:
Build a lightweight dependency map (~5KB XML) instead of passing raw source.
96% token reduction for codebase exploration. Research pattern confirmed in TOKEN_RESEARCH.md.

---

### TIER 6 — UNKNOWNS TO RESOLVE

These could change the plan significantly:

| Unknown | Impact if YES | Impact if NO | How to test |
|---------|--------------|--------------|-------------|
| Does claude.ai use deferred MCP loading? | Base44 overhead minimal | Base44 is expensive every session | Check /context in Claude Code, compare |
| Is skill eager-loading bug (#16160) present in claude.ai? | 30 skills = 96K–165K tokens at startup | 30 skills = ~1,500 tokens | API token count measurement |
| Does 5-min cache TTL apply to claude.ai web sessions? | Session discipline rules matter a lot | Cache mechanics differ from API | Anthropic support |

AI Pulse token section will surface answers as they emerge.

---

## IMPLEMENTATION ORDER

| Priority | Action | Effort | Status |
|----------|--------|--------|--------|
| 1 | /compact rule in GLOBAL_RULES | Done | ✓ |
| 2 | MCP guardrail rules in GLOBAL_RULES | Done | ✓ |
| 3 | Compress Nightwatch project instructions | 30 min | Next Nightwatch session |
| 4 | Compress Admin project instructions | 30 min | This session or next |
| 5 | Trim Cursor prompt context blocks | Ongoing | Enforce per-prompt |
| 6 | Resolve Unknown 1 — MCP deferred loading | 1 research session | Queued |
| 7 | Batch questions, keep sessions alive | Behavioral | Ongoing |
| 8 | Dependency map for Coinbeast | Future | When triggered |

---

## WHAT NOT TO DO

- **Never /compact** — busts cache, loses fidelity. Save context to file instead.
- **Never edit files externally during a session** — busts cache.
- **Never disconnect MCPs manually** — guardrail by session type instead.
- **Never add MCPs without token audit** — each one adds 1,400–26,000+ tokens.
- **Don't start fresh sessions aggressively** — one long session is cheaper than two short ones.
- **Don't use ultrathink routinely** — 31,999 output tokens at 5× rate for routine work is waste.
- **Don't over-trim skill bodies** — we're at the right level. Further trimming causes reference file fetches on every invocation, negating savings.

---

## REVIEW TRIGGER

Revisit when:
- Any Tier 6 unknown is resolved
- New model release changes token pricing or behavior
- Project instructions compression completed (Tier 3)
- AI Pulse token section surfaces a material new finding
