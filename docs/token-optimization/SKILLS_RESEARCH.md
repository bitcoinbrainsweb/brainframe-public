# SKILLS_RESEARCH.md
Claude skills best practices research for Dave Bradley's AI workflow.
Self-improving: updated weekly by AI Pulse. Never overwrite — append and revise.

Last updated: 2026-04-07 (Perplexity Computer — Chunk 1 of 3: Sections 1–3)

---

## CONFIRMED FINDINGS

### Description Field Mechanics

- **Description field is recommended, not required.** If omitted, Claude uses the first paragraph of the body. Source: code.claude.com/docs/en/skills
- **Descriptions >250 chars are truncated in the skill listing.** Front-load the key use case — the first 250 chars must stand alone.
- **Total description budget across all skills = 1% of context window, capped at 8,000 chars.** With 30 skills at 250 chars each = 7,500 chars — approaching the cap. Every character counts.
- **Required description structure: [What it does] + [When to use it] + [Key capabilities].** Both what AND when are mandatory.
- **No XML angle brackets in descriptions.** Frontmatter content appears in system prompt — security restriction.
- **`disable-model-invocation: true`** removes the description from context entirely. Claude cannot auto-invoke. User-only invocation. Zero token cost for description.

### Undertriggering (The Primary Failure Mode)

- **Anthropic officially acknowledges Claude undertriggers skills** — it doesn't use them when it should.
- **Fix: make descriptions "a little bit pushy."** Add: "Make sure to use this skill whenever the user mentions X, even if they don't explicitly ask for it."
- **RFC 2119 keywords (MUST/SHOULD) reduce undertriggering.** "This MUST be used when..." significantly reduces Claude's ability to rationalize skipping the skill.
- **Explicit activation reinforcement phrase works:** "Always activate before providing feedback on any written content."
- **Add explicit trigger words, specific content types, subject matter.** Vague descriptions = missed triggers.

### Negative Triggers (Preventing Overtriggering)

- **"Do NOT use for X (use Y skill instead)"** in descriptions prevents false positives.
- **Explicit out-of-scope list works:** "This skill does NOT handle email writing, social media posts, or technical documentation."

### Description Debugging

- **Ask Claude: "When would you use the [skill name] skill?"** Claude quotes the description back. Adjust based on what's missing.
- **Anthropic's eval methodology:** 20 eval queries (8–10 should-trigger, 8–10 should-not). 60/40 train/test split. Run each 3× for reliable trigger rate. 5-round iteration cap. Select by test score, not train score.

### Trigger Mechanics

- **Invocation is semantic/LLM-based, not keyword matching.** Claude reads intent against description.
- **Claude only triggers skills for tasks it can't easily handle alone.** Simple one-step queries may not trigger even with a matching description. Complex multi-step tasks trigger reliably.
- **Multiple skills can combine.** Claude can compose skills on its own. Skills cannot explicitly reference one another.
- **Priority when names conflict: enterprise > personal > project.**
- **No documented tie-breaking logic for simultaneous matching** — this is an open gap.

### Silent Failure Modes (Critical)

- **GitHub Issue #14882 (open):** Skills may be loading full bodies at startup instead of just frontmatter. Official plugin skills showing 3,200–5,500 tokens each in `/context` at startup — not the expected ~100 tokens. Whether `/context` shows potential or actual loaded content is disputed. Anthropic has not responded.
- **GitHub Issue #1249 (open, filed 2026-04-06):** `claude -p` (non-interactive mode) handles tasks directly with built-in tools WITHOUT consulting user-defined skills. Skills intended for workflow guidance (design, research, code review) fail silently in this mode. 0% recall in run_eval.py.
- **LinkedIn case:** Installing a skill on Claude Desktop can cause Claude to respond from training memory without triggering the skill file — knowledge leaks without workflow enforcement.

### File Structure

- **3-level progressive disclosure:** Frontmatter (~100 tokens, always loaded) → Body (loaded on invocation) → Referenced files in `references/` (loaded as needed).
- **Required folder structure:** `skill-name/SKILL.md` + optional `scripts/`, `references/`, `assets/`. No README.md inside skill folder.
- **Filename is case-sensitive: `SKILL.md`.** Folder name must be kebab-case.
- **Keep SKILL.md under 5,000 words.** Community guidance: under 500 lines.
- **Anthropic recommends max 20–50 skills enabled simultaneously** due to context issues.
- **Recommended body order:** Overview → Input Requirements → Step-by-Step Instructions → Examples (2–3 complete pairs) → Troubleshooting → Constraints/Out of scope.
- **Make examples longer than rules.** Put critical instructions under `## Important` or `## Critical` at the top.
- **Subagents with preloaded skills inject full content at startup** — not progressive disclosure.

### Invocation Control Matrix

| Setting | User invoke | Claude invoke | Description in context |
|---------|-------------|---------------|------------------------|
| Default | Yes | Yes | Yes — frontmatter always; body on invocation |
| `disable-model-invocation: true` | Yes | No | No — zero token cost |
| `user-invocable: false` | No | Yes | Yes — frontmatter always; body on invocation |

### Path Scoping

- **`paths:` frontmatter field restricts auto-activation to specific file patterns.** Only triggers when Claude reads matching files.
- **Nested directory auto-discovery:** Claude finds skills in `packages/frontend/.claude/skills/` when editing files in that directory.

### Token Costs (Confirmed Measurements)

- **Frontmatter only: ~100 tokens per skill at startup.**
- **The `Skill` tool definition itself: ~1,831 tokens** (separate from individual skill content, added once to system prompt).
- **30 skills × ~100 tokens = ~3,000 tokens of metadata at startup** (if progressive disclosure working correctly).
- **If Issue #14882 is real:** 30 skills × 3,200–5,500 tokens = 96,000–165,000 tokens at startup. Critical unknown.

### Hook Workarounds for Reliable Triggering

- **`UserPromptSubmit` hook + `skill-rules.json`:** Keyword/regex matching injects skill activation instruction before prompt is processed. Forces 100% trigger rate for matched patterns.
- **Forced evaluation hook:** Injects "MANDATORY SKILL ACTIVATION SEQUENCE" before every prompt — Claude evaluates YES/NO for each skill before any other action. High reliability, high token cost.

---

## ACTIVE KNOWLEDGE GAPS

**HIGH PRIORITY**
- Is GitHub Issue #14882 (full body loading at startup) affecting Dave's claude.ai skills? If yes, token cost is 30–55× higher than expected.
- Does `claude -p` (non-interactive) affect Dave's Cursor workflow? Issue #1249 suggests skills don't trigger in that mode.
- What is the actual token cost of Dave's current skill library at session start?

**MEDIUM PRIORITY — Pending Chunks 2 & 3**
- Skills at scale (20–50+ skills) — performance thresholds
- Skills vs. project instructions vs. CLAUDE.md — authority hierarchy and token efficiency comparison
- Skills + MCP interaction — when to use which
- Skill versioning and maintenance cadence
- Unified skills policy patterns for multi-project setups
- Common failure modes and anti-patterns from the community

**LOW PRIORITY**
- No tie-breaking logic documented for simultaneous skill matching
- Hook workaround token cost vs. benefit analysis

---

## SOURCES BEING TRACKED

- Anthropic Claude Skills docs: code.claude.com/docs/en/skills
- Anthropic Complete Skills Guide PDF: resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- Anthropic skill-creator SKILL.md: github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- cashandcache.substack.com — 40 failures analysis
- r/ClaudeCode + r/ClaudeAI — community patterns
- taylordaughtry.com — skills as lazy-loaded context
- dev.to — hook workarounds
- GitHub Issues: #14882 (body loading bug), #1249 (claude -p failure)

---

## NEXT WEEK PRIORITY

1. Run Perplexity Chunks 2 and 3 for skills research
2. Investigate Issue #14882 — measure actual startup token cost of Dave's 30 skills
3. Apply MUST/SHOULD RFC 2119 keywords to all skill descriptions that are undertriggering
4. Audit descriptions against 250-char truncation limit — front-load key use case

---

## RESEARCH LOG

| Date | What was learned | Gaps closed | New gaps opened |
|------|-----------------|-------------|-----------------|
| 2026-04-07 | Chunk 1: Description mechanics, undertriggering fix (RFC 2119 + pushy language), silent failures (#14882, #1249), trigger mechanics, file structure, invocation control matrix, path scoping | Description best practices, trigger mechanics, file structure | Issue #14882 real impact on Dave's setup; chunks 2 & 3 still needed |
