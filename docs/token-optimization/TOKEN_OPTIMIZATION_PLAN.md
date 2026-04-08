# TOKEN_OPTIMIZATION_PLAN.md
Dave Bradley — Brainframe AI Workflow
Version: 1.0 | 2026-04-07
Status: ACTIVE

Constraint: every rule must preserve or improve output quality and not slow work.
Grounded in: TOKEN_RESEARCH.md (docs/token-optimization/)

---

## WHAT WE KNOW (relevant to Dave's setup)

- **30 skills × ~50 tokens metadata = ~1,500 tokens at startup** (if lazy loading working)
- **Gmail + Drive MCPs: estimated 1,400–15,000 tokens** loaded before you type — now restricted to admin sessions (GLOBAL_RULES 132–134)
- **Base44 MCP: unknown token cost** — measure when possible
- **Full session history re-sent every message** — caching gives 90% discount within 5-min window
- **Skill bodies now trimmed 53–82%** — reference files load on demand from GitHub API
- **Project instructions load in full every session** — cached after first message
- **Context rot begins ~32K tokens** — quality degrades, not just cost

---

## THE PLAN

### TIER 1 — ALREADY DONE (implemented this session)

These are complete. No action needed.

| Change | Impact |
|--------|--------|
| Skill bodies trimmed 53–82% | Bodies load on demand; smaller = less context when triggered |
| Project-specific content in reference files | Loads only when working on that project |
| Gmail/Drive MCP restricted to admin sessions | Eliminates ~1,400–15,000 tokens in non-admin sessions |
| All 30 skill descriptions fixed | Correct triggering = right skills load, wrong ones don't |
| `disable-model-invocation` on 4 destructive skills | Prevents accidental loads, saves ~50 tokens each |
| quitchat refactored to fetch close procedures | Body down from 170 → 81 lines |

---

### TIER 2 — SESSION DISCIPLINE (behavioral rules, zero implementation)

These require no code changes. Add to GLOBAL_RULES and practice.

**Rule: MCP session matching**
Before starting any session, disconnect MCPs not needed for that session's primary task.
- Nightwatch session: disconnect Gmail, Drive. Keep Base44.
- Axiom session: disconnect Gmail, Drive, Base44.
- Admin session: Gmail + Drive permitted.
- Add this to project instructions for each project.

**Rule: No manual file edits during a session**
Editing files outside Claude during an active session busts the prompt cache.
Cache expiry on 200K tokens = 12.5× cost spike on next message.
If you need to edit externally: finish the Claude session first, restart after.

**Rule: Batch related questions**
Send multiple related questions in one message — not as follow-ups.
Each follow-up re-sends full history. Three questions in one message costs same as one.

**Rule: Keep sessions alive during work**
Cache TTL is 5 minutes. If you step away mid-session, cache expires.
Resume within 5 minutes or expect a cost spike on the next message.
For long breaks: use quitchat, start fresh with handoff file.

**Rule: Use "save context to file" not /compact**
If context is getting long, ask Claude to save context to a file rather than using /compact.
/compact busts the cache. Manual save preserves it and gives you control over what's retained.

**Rule: Ultrathink deliberately**
"ultrathink" = 31,999 output tokens. "think hard" = 10,000. Both billed at output rate (5× input).
Only use for: novel architecture decisions, complex debugging where multiple hypotheses exist.
Never use for: routine prompts, spec writing, description fixes, document generation.

---

### TIER 3 — PROJECT INSTRUCTIONS AUDIT (one-time work, high impact)

**What:** Project instructions load in full every session and are cached after the first message.
Anything over 50 lines costs tokens every session forever. Conditional logic in instructions
fires even when irrelevant.

**Action per project:**
1. Measure current project instructions length (count lines)
2. Extract any conditional logic ("when X do Y") into skills
3. Compress remaining instructions for token density
4. Target: under 50 lines per project

**Priority order:** Nightwatch (most sessions) → Admin → Axiom → Coinbeast

**How to compress:** Paste current instructions into Claude with prompt:
"Rewrite these instructions for maximum token density without losing any directive content.
Remove redundancy, use imperative form, eliminate explanations that Claude already knows."

---

### TIER 4 — CURSOR PROMPT STRUCTURE (KERNEL principles)

**What:** KERNEL framework measured 58% token reduction, 72% first-try success.
Your Nightwatch prompt standard already enforces most of it.
Gaps to close:

| KERNEL principle | Current state | Gap |
|-----------------|---------------|-----|
| Single objective per prompt | ✓ enforced | None |
| Explicit constraints | ✓ (Do Not Modify) | None |
| Narrow scope | ✓ (exact file list) | None |
| No multi-task combining | Occasionally violated | Flag when violated |
| Explicit success criteria | ✓ (acceptance criteria) | None |
| Avoid verbose output in prompts | Partially — some prompts have long context blocks | Trim context blocks |

**Action:** When writing any Cursor prompt, trim the Context section to minimum viable information.
Context blocks over 5 lines should be challenged — does Cursor actually need this?

---

### TIER 5 — DEPENDENCY MAP FOR COINBEAST (future, when codebase grows)

**What:** Dependency map pattern replaces 500K tokens of raw source with ~5KB XML.
96% token reduction for codebase exploration tasks.

**Trigger:** Implement when Coinbeast codebase exceeds ~50 files or when Cursor
starts making cross-file mistakes from incomplete context.

**How:** Build a lightweight tool that generates:
```xml
<depmap>
  <file path="src/products.ts" exports="ProductCard, useProducts" imports="api, types"/>
  <file path="src/api.ts" exports="fetchProducts, fetchPrices" imports="config"/>
</depmap>
```
Pass map instead of raw files. Claude deduces "src/products.ts imports src/api.ts" without reading either.

---

### TIER 6 — UNKNOWNS TO RESOLVE (research actions)

These are the highest-impact unknowns from TOKEN_RESEARCH.md.
Each one could change the plan significantly.

**Unknown 1 (CRITICAL): Does claude.ai use deferred MCP loading?**
If YES: Base44 MCP overhead is minimal (deferred). Current setup is fine.
If NO: Base44 is loading full tool definitions every session — significant waste.
How to test: check /context in a Claude Code session to see MCP overhead. Compare with claude.ai.

**Unknown 2: Is skill eager-loading bug (#16160) present in claude.ai?**
If YES: 30 skills could be loading 96K–165K tokens at startup instead of ~1,500.
How to test: claude.ai doesn't expose /context. Indirect: measure session token count in API.

**Unknown 3: Does 5-min cache TTL apply to claude.ai web sessions?**
Affects whether session discipline rules (Tier 2) actually matter in practice.
How to test: Anthropic support or API response headers analysis.

---

## IMPLEMENTATION ORDER

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | MCP session matching (Tier 2) | 5 min | High — eliminates Gmail/Drive overhead |
| 2 | No manual edits during session (Tier 2) | Behavior change | High — preserves cache |
| 3 | Batch questions (Tier 2) | Behavior change | Medium |
| 4 | Compress Nightwatch project instructions (Tier 3) | 30 min | High — paid every session |
| 5 | Compress Admin project instructions (Tier 3) | 30 min | Medium |
| 6 | Trim Cursor prompt context blocks (Tier 4) | Ongoing | Medium |
| 7 | Resolve Unknown 1 — MCP deferred loading (Tier 6) | 1 research session | Potentially very high |
| 8 | Deliberate ultrathink usage (Tier 2) | Behavior change | Medium |
| 9 | Dependency map for Coinbeast (Tier 5) | Future | High when triggered |

---

## WHAT NOT TO DO

- **Don't start fresh sessions aggressively.** One long session is cheaper than two short ones
  (re-caching costs full price). Only start fresh when task is genuinely unrelated or context has rotted.
- **Don't strip skill bodies below their functional minimum.** We've trimmed to the right level.
  Further trimming would require Claude to refetch reference files on every invocation, negating savings.
- **Don't use /compact.** Busts cache, loses fidelity unpredictably. Use manual context save instead.
- **Don't use ultrathink routinely.** 31,999 output tokens at 5× input rate = expensive for routine work.
- **Don't add more MCPs.** Every MCP server adds 1,400–26,000+ tokens at startup.
  New capability should be a skill or reference file first, MCP only if it needs live data.

---

## METRICS TO TRACK

When the weekly AI Pulse token research runs, watch for:
- Any change in MCP deferred loading behavior in claude.ai
- New community measurements of claude.ai session token costs
- Any Anthropic guidance on cache TTL for web sessions
- Emerging techniques for project instruction compression

---

## REVIEW TRIGGER

Revisit this plan when:
- Any of the 3 critical unknowns (Tier 6) are resolved
- A new model release changes token pricing or behavior
- A project instruction audit is completed (Tier 3)
- AI Pulse token section surfaces a material new finding
