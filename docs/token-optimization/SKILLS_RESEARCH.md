# SKILLS_RESEARCH.md
Claude skills best practices research for Dave Bradley's AI workflow.
Self-improving: updated weekly by AI Pulse. Never overwrite — append and revise.

Last updated: 2026-04-07 (Perplexity Computer — Chunks 1 & 3 complete; Chunk 2 pending)

---

## CONFIRMED FINDINGS

### Description Field Mechanics

- **Description is recommended, not required.** Omit it and Claude uses the first paragraph of the body. Always include it.
- **Descriptions >250 chars are truncated in the skill listing.** Front-load the key use case — first 250 chars must stand alone.
- **Total description budget = 1% of context window, capped at 8,000 chars.** 30 skills × 250 chars = 7,500 chars — nearly at the cap. No headroom for more skills without trimming.
- **Required structure: [What it does] + [When to use it] + [Key capabilities].** Both WHAT and WHEN are mandatory.
- **No XML angle brackets in descriptions.** Security restriction — frontmatter injects into system prompt.
- **Write descriptions in third person.** "Processes Excel files" not "I can help you process Excel files." First-person causes discovery problems.
- **`disable-model-invocation: true`** removes description from context entirely. Zero token cost. User-only invocation.

### Undertriggering (The Primary Failure Mode)

- **Anthropic officially acknowledges Claude undertriggers skills.** It's conservative about activating them.
- **Without any intervention, trigger rate can be 0%.** One developer tested 20 obviously-relevant prompts and got 0/20 triggers.
- **Simple instruction hook alone = 20% trigger rate** — "essentially a coin flip."
- **Forced evaluation hook = 84% trigger rate.** Most reliable but high token cost.
- **RFC 2119 keywords (MUST/SHOULD) significantly reduce undertriggering.** "This MUST be used when..." reduces Claude's ability to rationalize skipping.
- **Pushy activation phrase works:** "Make sure to use this skill whenever the user mentions X, even if they don't explicitly ask."
- **Explicit trigger words, specific content types, subject matter in description.** Vague descriptions = dead skills.
- **"Skills are not deterministic."** Even a perfect skill correctly installed may not fire. There is no guarantee.

### Negative Triggers (Preventing Overtriggering)

- **"Do NOT use for X (use Y skill instead)"** prevents false positives.
- **Explicit out-of-scope list:** "This skill does NOT handle email writing, social media posts, or technical documentation."

### Description Debugging

- **Ask Claude: "When would you use the [skill name] skill?"** Claude quotes the description back. Adjust from there.
- **Anthropic eval methodology:** 20 queries (8–10 should-trigger, 8–10 should-not). 60/40 train/test split. Run 3× per query. Max 5 iteration rounds. Select by test score not train score.
- **`pulser eval`** — open-source CLI that tests trigger accuracy across a skill set. Can run in CI.

### Trigger Mechanics

- **Semantic/LLM-based, not keyword matching.** Claude reads intent against description.
- **Claude only triggers for tasks it can't easily handle alone.** Simple one-step queries may not trigger even with matching description.
- **Complexity threshold exists.** Multi-step specialized queries trigger reliably; simple queries don't.
- **Multiple skills can compose.** Claude can combine skills on its own. Skills cannot explicitly reference one another.
- **Priority when names conflict: enterprise > personal > project.**
- **No documented tie-breaking for simultaneous matching** — confirmed gap, behavior non-deterministic.

### Silent Failure Modes (Critical — All Open)

- **Issue #14882:** Full skill bodies may load at startup instead of just frontmatter. `/context` may show potential size vs. actual loaded — ambiguity unresolved. Anthropic closed as "not planned" without confirming behavior.
- **Issue #1249 (filed 2026-04-06):** `claude -p` (non-interactive) bypasses user-defined skills entirely. 0% recall. Affects workflow guidance, design, research, code review skills.
- **Issue #41530:** Claude Code v2.1.88 broke all custom skills. Downgrade to v2.1.87 as workaround.
- **Issue #43660 (v2.1.92):** `disable-model-invocation: true` skills incorrectly report as unactivatable.
- **Stale plugin cache duplication:** outdated plugin cache directories cause skills to appear twice in system prompt. One user's 30 skills became 60 entries. Check with `pulser`.
- **Broken paths fail silently.** Claude reads a broken path reference and continues as if the line wasn't there. No error.
- **Skills update risk:** When updating a skill via Claude, it frequently drops reference files or applies edits incorrectly. Always backup before updating.

### Claude 4.6 Breaking Changes (BMAD Post-Mortem)

- **Hook format changed:** PreToolUse/PostToolUse now require `matcher/hooks[]` array wrapper. Old format silently does nothing.
- **`AgentOutputTool` renamed to `TaskOutput`.**
- **`$schema` URL moved.**
- **All 200K token references required updating to 1M.**
- **Lesson:** "When you build on a platform that ships major updates every few months, maintenance isn't optional. It's the core of the work."

### File Structure

- **3-level progressive disclosure:** Frontmatter (~100 tokens, always) → Body (on invocation) → `references/` files (as needed).
- **Required: `skill-name/SKILL.md`** — case-sensitive filename, kebab-case folder. No README.md inside skill folder.
- **Keep SKILL.md under 5,000 words / 500 lines.** Over 1,000 lines = loads everything on every request, bloating context.
- **Recommended body order:** Overview → Input Requirements → Step-by-Step Instructions → Examples (2–3 complete pairs) → Troubleshooting → Constraints.
- **Examples section should be longer than rules section.**
- **Put critical instructions under `## Important` or `## Critical` at the top.**
- **Keep references one level deep.** Nested references cause Claude to partially read files (`head -100`), losing content.
- **Don't offer multiple approaches unless necessary.** Leads to inconsistent output.
- **Anthropic recommends max 20–50 skills enabled simultaneously.**

### Invocation Control Matrix

| Setting | User invoke | Claude invoke | Description in context |
|---------|-------------|---------------|------------------------|
| Default | Yes | Yes | Yes — frontmatter always; body on invocation |
| `disable-model-invocation: true` | Yes | No | No — zero token cost |
| `user-invocable: false` | No | Yes | Yes — frontmatter always; body on invocation |

### Scope Hierarchy

| Level | Path | Applies to |
|-------|------|-----------|
| Enterprise | Managed settings | All org users |
| Personal | `~/.claude/skills/` | All your projects |
| Project | `.claude/skills/` | This project only |
| Plugin | `<plugin>/skills/` | Where plugin is enabled |

- **Personal skills at `~/.claude/skills/` apply across all projects** — right approach for Brainframe global skills.
- **Project skills committed to version control** — right approach for project-specific skills.
- **Monorepo pattern:** Claude auto-discovers nested `.claude/skills/` when editing files in that directory.
- **Skills follow Agent Skills open standard** — portable to Cursor, Gemini CLI, Copilot, Codex, Windsurf.

### Governance and Versioning

- **`version` field in frontmatter** — documentation only, doesn't affect runtime. 62% of community skills missing it.
- **`skill-semver` tool** — auto-backup and changelog on SKILL.md edit via PostToolUse hook. Semantic versioning (MAJOR/MINOR/PATCH).
- **Anthropic enterprise versioning:** pin to versions, full eval before promoting, maintain previous version as rollback, compute checksums, signed commits.
- **Anthropic enterprise registry fields:** Purpose, Owner, Version, Dependencies, Evaluation status.
- **"Anthropic does not make skill version control easy. Once you overwrite, it's completely gone."** GitHub for Claude Code skills is the only reliable backup.
- **Lifecycle: Plan → Create+Review → Test → Deploy → Monitor → Iterate or Deprecate.**
- **Re-run evaluations periodically.** No specific cadence from Anthropic — "periodically" only.

### Decision Framework: What Goes Where

```
Does this apply to every conversation in this project?
→ Yes → CLAUDE.md / project instructions

Is this a workflow you invoke directly (slash command)?
→ Yes → .claude/commands/

Is this a specialized mode for a specific type of work?
→ Yes → Skill in .claude/skills/{name}/SKILL.md
```

### Two Skill Categories (Emerging Taxonomy)

- **Capability Uplift:** Claude cannot do this without the skill (web scraping, PDF creation, browser testing).
- **Encoded Preference:** Claude can do this but the skill encodes your specific way of doing it (NDA reviews, commit formats, code review checklists).

### Anti-Patterns (Confirmed)

- **Using MCP for a prompt template.** If it just returns a string, it's a skill not an MCP.
- **Skill body attempting to reach external systems.** Skills cannot query databases or APIs — that's MCP's job.
- **Conditional logic in CLAUDE.md.** "When writing articles do X; when editing SEO do Y" — belongs in skills, not CLAUDE.md.
- **System-specific skills at root level.** Root = broadly applicable. Nested = system-specific.
- **Adding more skills to fix problems caused by broken skills.** Audit first.
- **Missing `disable-model-invocation: true` on side-effect skills.** Claude may auto-invoke destructive skills.
- **Tool-first design.** Start with the pain point, not the tool.
- **Deeply nested references.** Keep one level deep from SKILL.md.
- **Offering too many options in skill body.** One approach, one output.
- **CLAUDE.md over 300–500 lines.** Accuracy drops noticeably past 500 lines per community research.
- **Vague skill names:** `helper`, `utils`, `tools`, `documents`. Name for the workflow not the technology.

### Token Costs (Confirmed)

- **Frontmatter: ~100 tokens/skill at startup.**
- **`Skill` tool definition: ~1,831 tokens** (added once, separate from skill content).
- **30 skills: ~3,000 tokens if progressive disclosure works correctly.**
- **If Issue #14882 is real: 30 skills × 3,200–5,500 tokens = 96K–165K tokens at startup.** Critical unknown.
- **Deferred loading for skills explicitly NOT implemented.** Feature request #19445 marked stale. MCP Tool Search does NOT extend to skills.

---

## ACTIVE KNOWLEDGE GAPS

**HIGH — Answer before building skills policy**
- Is Issue #14882 (full body loading) affecting Dave's claude.ai setup? Measure actual startup token cost.
- Does Chunk 2 confirm skills vs. project instructions hierarchy?
- What is behavior when 8,000-char description budget is exceeded with 30+ skills?
- No documented solo-dev unified skills policy (all governance targets enterprise teams).
- How do skills survive context compaction? Does skill metadata persist after `/compact`?

**MEDIUM — Next research cycle**
- Trigger accuracy by model size (Haiku vs. Sonnet vs. Opus) — Haiku may need more explicit guidance.
- `mode` frontmatter field behavior — places skill at top of list, effect on trigger probability unknown.
- Skills cannot reference each other — workaround patterns?
- Live change detection: does it apply to project-level skills during an active session?

**LOW**
- Cross-platform sync tooling (claude.ai vs. Claude Code vs. API) — no official solution exists.
- Deferred loading for skills — feature request stale, not on roadmap.

**PENDING — Chunk 2**
- Skills at scale performance thresholds (20, 30, 50+ skills)
- Skills vs. project instructions vs. CLAUDE.md token efficiency comparison
- Skills + MCP interaction — when to use which
- Full scope of multi-project patterns

---

## SOURCES BEING TRACKED

**Tier 1 — Check every model release**
- GitHub anthropics/claude-code issues `area:skills`: github.com/anthropics/claude-code/issues
- platform.claude.com/docs/en/agents-and-tools/agent-skills/ — official docs
- github.com/anthropics/skills — official skill-creator and eval methodology
- r/ClaudeCode — breakage reports surface here first

**Tier 2 — Check weekly**
- buildtolaunch.substack.com (Jenny Ouyang) — SSOT audit methodology, governance patterns
- sjramblings.io — troubleshooting and distribution patterns
- simonwillison.net/tags/skills/
- aimaker.substack.com — Anthropic release cadence tracking
- github.com/VoltAgent/awesome-agent-skills — cross-platform catalog
- github.com/cathy-kim/skill-semver — versioning tooling
- mind-core.com — enterprise governance patterns
- natesnewsletter.substack.com

---

## NEXT WEEK PRIORITY

1. Integrate Chunk 2 (sections 4–6) when it arrives
2. Run `pulser` audit on Dave's skill library — detect broken references, conflicts, dead skills
3. Apply RFC 2119 language to undertriggering descriptions
4. Verify 250-char truncation on all skill descriptions — front-load key use case
5. Set up `skill-semver` for version tracking in brainframe repos
6. Add `disable-model-invocation: true` to any skill that should only be user-invoked

---

## RESEARCH LOG

| Date | What was learned | Gaps closed | New gaps opened |
|------|-----------------|-------------|-----------------|
| 2026-04-07 | Chunk 1: Description mechanics, undertriggering (RFC 2119), silent failures (#14882, #1249), trigger mechanics, file structure, invocation control matrix | Description best practices, trigger mechanics, file structure | Issue #14882 real impact; chunks 2 & 3 needed |
| 2026-04-07 | Chunk 3: Versioning (skill-semver), Claude 4.6 breaking changes, governance framework, scope hierarchy, decision framework, anti-patterns, failure modes (73% broken community skills), audit tools (pulser, ssot-auditor) | Governance patterns, versioning, failure modes, anti-patterns | Solo-dev unified policy gap; chunk 2 still needed |
