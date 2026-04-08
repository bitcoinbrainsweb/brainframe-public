# SKILLS_RESEARCH.md
Claude skills best practices research for Dave Bradley's AI workflow.
Self-improving: updated weekly by AI Pulse. Never overwrite — append and revise.

Last updated: 2026-04-07 (Perplexity Computer — All 3 Chunks COMPLETE)

---

## CONFIRMED FINDINGS

### Description Field Mechanics

- **Description: recommended, not required.** Omit it and Claude uses the first body paragraph. Always include it.
- **Descriptions >250 chars are truncated in the skill listing.** First 250 chars must stand alone — front-load the key use case.
- **Total description budget = 1% of context window, capped at 8,000 chars.** 30 skills × 250 chars = 7,500 — nearly at the cap. No room for more without trimming.
- **Required structure: [What it does] + [When to use it] + [Key capabilities].** Both WHAT and WHEN are mandatory.
- **Write in third person.** "Processes Excel files" not "I can help you process Excel files." First-person causes discovery problems.
- **No XML angle brackets in descriptions.** Security restriction — frontmatter injects into system prompt.
- **`disable-model-invocation: true`** removes description from context entirely. Zero token cost. User-only invocation.
- **`SLASH_COMMAND_TOOL_CHAR_BUDGET` env var** can raise the 8,000-char description budget limit.

### Undertriggering (The Primary Failure Mode)

- **Anthropic officially acknowledges Claude undertriggers skills.**
- **Without intervention, trigger rate can be 0%.** Tested: 20 obviously-relevant prompts, 0/20 triggered.
- **Simple instruction hook = 20% trigger rate** — "essentially a coin flip."
- **Forced evaluation hook = 84% trigger rate.** Most reliable, highest token cost.
- **RFC 2119 keywords (MUST/SHOULD) significantly reduce undertriggering.** "This MUST be used when..."
- **Pushy activation phrase:** "Make sure to use this skill whenever the user mentions X, even if they don't explicitly ask."
- **Skills are not deterministic.** Even a perfect skill correctly installed may not fire. No guarantee.
- **Claude only triggers for tasks it can't easily handle alone.** Simple queries won't trigger even with matching description.

### Negative Triggers

- **"Do NOT use for X (use Y skill instead)"** prevents false positives.
- **Explicit out-of-scope list** works: "This skill does NOT handle email writing, social media posts, or technical documentation."

### Trigger Mechanics

- **Semantic/LLM-based, not keyword matching.**
- **Multiple skills can compose.** Claude can combine them on its own. Skills cannot explicitly reference one another.
- **Priority when names conflict: enterprise > personal > project.**
- **No documented tie-breaking for simultaneous matching** — non-deterministic.
- **API limit: 8 skills per request.** Skills cannot make external network calls on the API.

### Description Debugging

- **Ask Claude: "When would you use the [skill name] skill?"** Claude quotes the description back.
- **Anthropic eval methodology:** 20 queries (8–10 should-trigger, 8–10 should-not). 60/40 train/test split. Run 3× per query. Max 5 rounds. Select by test score not train score.
- **`pulser eval`** — open-source CLI, tests trigger accuracy, detects conflicts. Can run in CI.

### Token Costs (Confirmed Measurements)

- **Metadata only: ~30–50 tokens per skill at startup** (community measurement, lower than the ~100 token figure).
- **`Skill` tool definition: ~1,831 tokens** added once to system prompt, separate from skill content.
- **30 skills × ~50 tokens = ~1,500 tokens of metadata** — if progressive disclosure working correctly.
- **If Issue #14882 is real (full body loading):** individual skills measured at 9,400–14,600 tokens each. 30 skills = potentially 280K–440K tokens. Critical unknown.
- **Skill duplication bug (Issues #27721, #29520):** stale plugin cache causes each skill to appear twice. 30 skills can become 60 entries. Check with `pulser`.
- **MCP Tool Search does NOT apply to skills.** Feature request #19445 marked stale.

### File Structure

- **3-level progressive disclosure:** Frontmatter (~50 tokens, always) → Body (on invocation) → `references/` (as needed).
- **Required: `skill-name/SKILL.md`** — case-sensitive filename, kebab-case folder. No README.md inside.
- **Keep SKILL.md under 5,000 words / 500 lines.** Over 1,000 lines = loads entirely on every invocation.
- **Recommended body order:** Overview → Input Requirements → Step-by-Step Instructions → Examples (2–3 complete pairs) → Troubleshooting → Constraints.
- **Examples longer than rules.** Critical instructions under `## Important` or `## Critical` at top.
- **References one level deep only.** Nested references cause Claude to partially read files (`head -100`).
- **Don't offer multiple approaches unless necessary.** Inconsistent output follows.
- **HTML comments in CLAUDE.md are stripped before injection** — free documentation tokens.
- **Anthropic recommends max 20–50 skills enabled simultaneously.**

### Invocation Control Matrix

| Setting | User invoke | Claude invoke | Description in context |
|---------|-------------|---------------|------------------------|
| Default | Yes | Yes | Yes |
| `disable-model-invocation: true` | Yes | No | No — zero token cost |
| `user-invocable: false` | No | Yes | Yes |

### Scope Hierarchy

| Level | Path | Applies to |
|-------|------|-----------|
| Enterprise | Managed settings | All org users |
| Personal | `~/.claude/skills/` | All your projects |
| Project | `.claude/skills/` | This project only |
| Plugin | `<plugin>/skills/` | Where plugin is enabled |

- **Personal skills at `~/.claude/skills/` = Brainframe global skills.** Right architecture.
- **Project skills committed to git.** Right architecture.
- **Monorepo: nested `.claude/skills/` auto-discovered** when editing files in that directory.
- **Skills follow Agent Skills open standard** — portable to Cursor, Gemini CLI, Copilot, Codex, Windsurf.

### Memory Hierarchy (What Overrides What)

Loading order (highest priority last-read wins within a level):
1. Auto Memory (`MEMORY.md` first 200 lines/25KB) — at every session start
2. Project Memory (`CLAUDE.md`) — at launch, in full
3. Project Rules (`.claude/rules/*.md`) — at launch (unconditional) or on file match (path-scoped)
4. Project Local (`CLAUDE.local.md`) — appended after CLAUDE.md, gitignored
5. Skills — only when invoked or Claude determines relevant

- **"All discovered files are concatenated, not overriding each other."**
- **"If two rules contradict each other, Claude may pick one arbitrarily."**
- **Skills have no documented authority position relative to CLAUDE.md in a conflict.** Parallel systems.
- **Managed policy CLAUDE.md cannot be excluded.** Always applies.

### What Goes Where (Decision Framework)

```
Does this apply to every conversation in this project?
→ Yes → CLAUDE.md

Is this conditional logic ("when X do Y")?
→ Yes → Skill (CLAUDE.md can't turn itself off by context)

Is this a workflow you invoke directly?
→ Yes → .claude/commands/ (slash command)

Is this a specialized mode for a specific type of work?
→ Yes → .claude/skills/{name}/SKILL.md

Is this context that only applies to specific file types?
→ Yes → .claude/rules/ with paths: frontmatter (path-scoped rule)
```

- **CLAUDE.md bloat:** accuracy drops noticeably past 500 lines per community research. Past 300 lines, rules start getting buried.
- **Conditional logic in CLAUDE.md is an anti-pattern.** Belongs in skills — CLAUDE.md can't turn itself off by context.

### Skills vs. MCP (Confirmed Decision Framework)

| Use Skills when | Use MCP when |
|-----------------|--------------|
| Output entirely generated by Claude from instructions | Need external data, APIs, databases |
| Workflow/template/procedure to follow | Need deterministic execution (same input → same output) |
| Creative judgment or open-ended analysis | Need real-time data |
| Rarely-used capabilities | Frequent, simple API calls |
| Complex scripts (code never enters context) | Structured, predictable tool interactions |

- **Skills can orchestrate MCP calls.** Skill body can explicitly name MCP tools using `ServerName:tool_name` format.
- **Skills = the "how". MCP = the "what" (data/execution).**
- **No conflict resolution documented** when skill description and MCP tool description both match the same query.
- **MCP tools always loaded at session start (fixed cost).** Skills progressively disclosed.
- **MCP Tool Search reduces MCP overhead 85%.** Does NOT apply to skills.

### Token Efficiency: Skills + MCP Combined

```
Session start baseline:
├── Skill metadata (~50 tokens × 30 skills): ~1,500 tokens
└── MCP tool definitions: 1,400–10,000+ tokens per server

Task execution:
├── Full skill body loaded: ~3,000 tokens
├── MCP call: ~200 tokens each
└── Additional MCP calls: ~150–200 tokens each

Simple follow-up query (skill already loaded):
└── MCP call only: ~200 tokens
```

### Versioning and Maintenance

- **`version` field in frontmatter** — documentation only, no runtime effect. 62% of community skills missing it.
- **`skill-semver` tool** — PostToolUse hook auto-backs up and changelogs on SKILL.md edit.
- **"Anthropic does not make skill version control easy. Once you overwrite, it's completely gone."** Git is the only reliable backup.
- **Claude 4.6 breaking changes:** hook format, `AgentOutputTool` → `TaskOutput`, install paths, context window references. Platform ships major updates every few months — maintenance is core, not optional.
- **Anthropic says "periodically" re-run evaluations.** No specific cadence defined.
- **Lesson: read the documentation on every release.** Not blog posts, not Twitter — the docs.

### Governance and Organization

- **Two skill categories:** Capability Uplift (Claude can't do it without the skill) vs. Encoded Preference (your specific way of doing what Claude already knows).
- **Three architecture patterns for skill groups:**
  - Option A: Monolithic orchestrator (single entry point + internal references)
  - Option B: Modular individual skills (each independently invocable)
  - Option C: Thin orchestrator + invocable root-level modules (recommended by buildtolaunch.substack.com)
- **Problem-first design.** Start with the pain point. Not "what can I do with this tool?"
- **Deduplicate shared instructions.** If three skills all say "never modify production without approval," consolidate into one shared constraint skill.
- **Benchmark skill impact.** Measure with and without. If a skill adds tokens but doesn't change behavior — trim or remove.

### Silent Failure Modes (All Open Issues)

- **Issue #14882:** Full bodies may load at startup. Individual skills measured at 9,400–14,600 tokens. Closed "not planned" — behavior unconfirmed.
- **Issue #1249 (2026-04-06):** `claude -p` bypasses user-defined skills entirely. 0% recall.
- **Issue #41530:** v2.1.88 broke all custom skills. Downgrade to v2.1.87 as workaround.
- **Issue #43660 (v2.1.92):** `disable-model-invocation: true` incorrectly reports as unactivatable.
- **Issues #27721/#29520:** skill duplication bug — 30 skills can appear as 60 entries.
- **Broken paths fail silently.** No error. Claude reads nothing and continues.
- **Skills update risk:** Claude frequently drops reference files when updating a skill. Always backup first.

### Anti-Patterns (Full List)

- Using MCP for a prompt template — that's a skill
- Skill body attempting external API/database calls — that's MCP
- Conditional logic in CLAUDE.md — belongs in skills
- System-specific skills at root level (root = broadly applicable)
- Adding skills to fix problems caused by broken skills — audit first
- Missing `disable-model-invocation: true` on side-effect/destructive skills
- Tool-first design instead of problem-first
- References nested more than one level deep
- Offering multiple approaches in skill body
- CLAUDE.md over 300–500 lines
- Vague skill names: `helper`, `utils`, `tools`, `documents`
- First-person descriptions
- Deeply nested references in skill bodies
- Not setting up eval before deploying

### Audit Tools

- **`pulser`** — `npx pulser@latest` — 14-criterion scoring (0–100). Threshold: 70 = reliable, <60 = gambling. Detects conflicts, dead skills, broken references. CI-compatible.
- **`ssot-auditor`** — 3-pass audit: broken references, filesystem structure, duplicate doctrine.
- **`skill-semver`** — semantic versioning + auto-backup via PostToolUse hook.
- **`/context`** — shows context breakdown but may not accurately reflect actual vs. potential skill token cost.
- **Direct invocation test:** `/skill-name` to confirm skill works independent of auto-triggering.

---

## ACTIVE KNOWLEDGE GAPS

**HIGH — Answer before building skills policy**
- Is Issue #14882 (full body loading) affecting Dave's claude.ai setup? Measure actual startup token cost.
- What happens when 8,000-char description budget is exceeded with 30+ skills? Which get truncated first?
- No documented solo-dev unified skills policy — enterprise frameworks only. We're building something new.
- How do skills survive context compaction? Does skill metadata persist after `/compact`?

**MEDIUM**
- Trigger accuracy by model size (Haiku vs. Sonnet vs. Opus) — not systematically published.
- `mode` frontmatter field behavior — effect on trigger probability unknown.
- Skills cannot reference each other — workaround patterns?
- Live change detection during active sessions for project-level skills?

**LOW**
- Cross-platform sync (claude.ai vs. Claude Code vs. API) — no official solution.
- Deferred loading for skills — feature request stale, not on roadmap.
- `ENABLE_TOOL_SEARCH` does not extend to skills — confirmed, no plans.

---

## SOURCES BEING TRACKED

**Tier 1 — Check every model release**
- GitHub anthropics/claude-code issues `area:skills`
- platform.claude.com/docs/en/agents-and-tools/agent-skills/
- github.com/anthropics/skills (official skill-creator + eval methodology)
- r/ClaudeCode — breakage reports first

**Tier 2 — Check weekly**
- buildtolaunch.substack.com (Jenny Ouyang)
- sjramblings.io
- simonwillison.net/tags/skills/
- aimaker.substack.com
- github.com/VoltAgent/awesome-agent-skills
- github.com/cathy-kim/skill-semver
- mind-core.com
- paddo.dev
- natesnewsletter.substack.com

---

## NEXT ACTIONS (Prioritized)

1. **Run `pulser` audit on Dave's 30 skills** — detect broken references, conflicts, dead skills, score each
2. **Fix undertriggering descriptions** — add RFC 2119 language (MUST/SHOULD) + pushy activation phrase
3. **Verify 250-char truncation** — front-load key use case in all descriptions
4. **Add `disable-model-invocation: true`** to any skill that should never auto-trigger
5. **Set up `skill-semver`** in brainframe repos — auto-backup before any skill update
6. **Audit CLAUDE.md / project instructions** — if over 300 lines, move conditional logic to skills
7. **Move Gmail/Drive MCPs to session-specific loading** — disconnect when not needed

---

## RESEARCH LOG

| Date | What was learned | Gaps closed | New gaps opened |
|------|-----------------|-------------|-----------------|
| 2026-04-07 | Chunk 1: Description mechanics, undertriggering (RFC 2119), silent failures, trigger mechanics, file structure, invocation control matrix | Description best practices, trigger mechanics, file structure | Issue #14882 real impact |
| 2026-04-07 | Chunk 3: Versioning (skill-semver), Claude 4.6 breaking changes, governance, scope hierarchy, decision framework, anti-patterns, failure modes, audit tools | Governance patterns, versioning, failure modes, anti-patterns | Solo-dev unified policy gap |
| 2026-04-07 | Chunk 2: Scale token costs (30–50 tokens/skill confirmed), duplication bugs (#27721/#29520), CLAUDE.md vs skills vs rules hierarchy, memory loading schedule, skills+MCP decision framework, token efficiency comparison, combined session cost model | Scale mechanics, memory hierarchy, skills vs MCP, token efficiency | 8,000-char budget overflow behavior; skills don't survive compaction unclear |

---

## YAML FRONTMATTER RULES (Definitive Reference)

*Added 2026-04-07. Use this section as the authoritative source when writing or auditing any SKILL.md.*

### Allowed Fields (claude.ai + Claude Code)

| Field | Required | Type | Constraints |
|-------|----------|------|-------------|
| `name` | Yes | string | Max 64 chars. Lowercase, numbers, hyphens only. No underscores, spaces, uppercase. No reserved words (claude, anthropic). |
| `description` | Yes | string | Max 1024 chars. Non-empty. No XML angle brackets (`<` `>`). Use `>-` block scalar — never double-quoted string. |
| `license` | No | string | SPDX identifier |
| `allowed-tools` | No | list | Tool identifiers |
| `metadata` | No | dict | Nested key-value |
| `disable-model-invocation` | No | bool | Claude Code user skills only. Prevents auto-invocation. Skill hidden from model context entirely. |
| `user-invocable` | No | bool | Claude Code only. `false` = Claude auto-only, not user-callable. |

**`version` is NOT a valid field in claude.ai.** It triggers "unexpected key" errors in the quick validator. Do not include it.

### Description Format — Always Use Block Scalar

```yaml
# CORRECT — block scalar, no quoting, no escape issues
description: >-
  Creates Architecture Decision Records when significant technical
  decisions are made. MUST be used when Dave says we decided or
  lets go with X. Do NOT use for routine decisions.

# WRONG — inner quotes break YAML
description: "MUST be used when Dave says 'we decided' or 'let's go with X'."

# WRONG — colons after space break YAML without quoting
description: Covers: entities, routes, integrations
```

### Complete Failure Mode Catalog

| Failure | Cause | Fix |
|---------|-------|-----|
| `malformed YAML frontmatter` | Inner `"` inside double-quoted description | Use `>-` block scalar |
| `unexpected key` | `version`, `author`, `category`, `tags` in frontmatter | Remove — not allowed in claude.ai |
| `malformed YAML` | Colon + space in unquoted value | Use `>-` block scalar |
| `malformed YAML` | `#` in unquoted value (parsed as comment) | Use `>-` block scalar |
| `malformed YAML` | `&`, `*`, `!`, `|`, `>`, `{`, `}` unquoted | Use `>-` block scalar |
| `malformed YAML` | Tab indentation | Use spaces only |
| `malformed YAML` | Missing closing `---` | Add closing delimiter |
| `invalid name` | Uppercase, underscore, space in name | Kebab-case only |
| `invalid name` | Name > 64 chars | Shorten |
| `invalid description` | `<` or `>` in description | Remove XML chars |
| `invalid description` | Description > 1024 chars | Shorten |
| `skill never triggers` | `disable-model-invocation: true` set | Remove or invoke with `/skill-name` |
| `skill never triggers` | Description too vague for semantic match | Add MUST/SHOULD triggers |
| `skill always triggers` | Description too broad | Add Do NOT guard |

### Block Scalar (`>-`) Cheat Sheet

```yaml
description: >-
  First line of description here.
  Continuation lines are joined with a space.
  Single quotes work fine: it's easy.
  Double quotes work fine: say "hello" freely.
  Colons work fine: key: value is fine here.
  Only restriction: no XML angle brackets.
```

- `>` — folded (newlines → spaces), trailing newline preserved
- `>-` — folded, trailing newline stripped ← **use this**
- `|` — literal (newlines preserved) — don't use for descriptions

### Skill-Creator Skill Requirement

**The skill-creator skill MUST reference this YAML section and the full SKILLS_RESEARCH.md.**
When creating or updating any skill, the skill-creator should:
1. Read SKILLS_RESEARCH.md from brainframe-public for trigger/description best practices
2. Apply the YAML failure mode catalog above to validate frontmatter before outputting
3. Use `>-` block scalar for all descriptions
4. Never include `version` field
5. Include `disable-model-invocation: true` for any skill with side effects or destructive operations
6. Verify description is under 250 chars (truncation point in listing) AND under 1024 chars (hard limit)
7. Run the description through the MUST/SHOULD + Do NOT template
