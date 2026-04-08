# UNIFIED_SKILLS_POLICY.md
Brainframe Skills Policy v1.0
Owner: Dave Bradley
Created: 2026-04-07
Apply to: all projects (Nightwatch, Axiom, Coinbeast, Mambamode, admin)

---

## 1. WHAT IS A SKILL

A skill is a markdown file that loads specialized instructions into Claude's context on demand. Skills are NOT:
- A place for always-on rules (use CLAUDE.md / project instructions)
- A replacement for MCP when external data is needed
- A workaround for instructions that failed elsewhere

Two categories:
- **Capability Uplift** — Claude cannot reliably do this without the skill (e.g. nightwatch-prompts, compliance-research-report)
- **Encoded Preference** — Claude can do this but the skill encodes the specific way (e.g. technical-writing, adr)

---

## 2. WHAT GOES WHERE

```
Does this apply to every conversation in this project?
→ Yes → CLAUDE.md / project instructions

Is this conditional logic ("when X do Y")?
→ Yes → Skill — CLAUDE.md cannot turn itself off by context

Is this a workflow you invoke directly by name?
→ Yes → Slash command (.claude/commands/)

Is this a specialized mode for a specific type of work?
→ Yes → Skill (.claude/skills/{name}/SKILL.md or ~/.claude/skills/)

Does this only apply when working with specific file types?
→ Yes → Path-scoped rule (.claude/rules/ with paths: frontmatter)
```

---

## 3. SKILL SCOPE RULES

| Scope | Path | Use for |
|-------|------|---------|
| Global | `~/.claude/skills/` | Skills used across 2+ projects |
| Project | `.claude/skills/` | Skills specific to one project |
| Path-scoped | `.claude/rules/` with `paths:` | Context that only applies to specific file types |

**Global skills (cross-project):** brainstorming, technical-writing, adr, systematic-debugging, grill-me, prd-to-plan, ubiquitous-language, proof-of-work, code-review-excellence, frontend-design, gpt-critique-skill, gpt-deep-research-prompt-skill, perplexity-pro-research-prompt-skill, ai-pulse, quitchat

**Nightwatch-only:** nightwatch-prompts, nightwatch-upgrade-orchestrator, nightwatch-ux, nightwatch-site-audit, roadmap-planner, base44-entity-design, compliance-research-report, fintrac-compliance, data-policy-enforcer, amanda-decision-recorder, avlm-quiz-generator

**Axiom-only:** axiom-prompts, axiom-close, axiom-health, axiom-roadmap

**Admin-only:** (none currently — admin uses global skills)

---

## 4. DESCRIPTION STANDARD

Every skill description MUST:
1. Be written in **third person** ("Processes X" not "I can help with X")
2. State **what it does** in the first sentence
3. State **when to use it** with explicit trigger conditions
4. Include **MUST/SHOULD** RFC 2119 language for the primary trigger
5. Include a **"Do NOT use"** or **"Never"** guard for the most common false-positive case
6. Fit within **250 characters** (truncation point in skill listing)
7. Front-load the key use case — the first 100 chars must stand alone

**Template:**
```
[What it does]. MUST be used when [primary trigger]. Also triggers on [secondary triggers]. 
Do NOT use for [most common false positive].
```

**Current budget:** 7,183 / 8,000 chars (90%). Adding skills requires trimming existing descriptions.

---

## 5. SKILL BODY STANDARD

Every skill body MUST:
1. Stay under **500 lines / 5,000 words**
2. Open with a 1–2 sentence **Overview** under the frontmatter
3. Follow order: Overview → Input Requirements → Step-by-Step Instructions → Examples → Troubleshooting → Constraints
4. Put critical instructions under `## Critical` or `## Important` at the top
5. Include **2–3 complete input/output examples** — examples section longer than rules section
6. Keep references **one level deep** only — no nested references
7. State **one approach** — never offer multiple options unless the task genuinely requires it
8. Include a **version** field in frontmatter: `version: "X.Y.Z"`

---

## 6. FRONTMATTER STANDARD

Required fields:
```yaml
---
name: skill-name-kebab-case
description: "[250 char max. Third person. MUST trigger language. Do NOT guard.]"
version: "1.0.0"
---
```

Optional but governed:
- `disable-model-invocation: true` — REQUIRED for any skill that has side effects or destructive operations
- `user-invocable: false` — for skills that should only auto-trigger, never be called directly
- `paths:` — use for any skill that only applies to specific file types
- `effort:` — set explicitly when the task has a known cost profile

---

## 7. INVOCATION RULES

- **Auto-invoke** (Claude decides): appropriate for most skills
- **`disable-model-invocation: true`** (user-only): required for destructive operations, skills with side effects, or skills that should run in a controlled sequence only
- **Slash command** (explicit user trigger): for workflows where timing and intent must be explicit

Skills that currently require `disable-model-invocation: true` review:
- `nightwatch-upgrade-orchestrator` — initiates real builds
- `nightwatch-site-audit` — destructive audit operations
- `quitchat` — already has "Run only when user types quitchat" — add frontmatter to match
- `axiom-close` — same
- `axiom-health` — same

---

## 8. VERSIONING RULES

- Every skill has a `version` field in frontmatter
- Version bumps follow semver: MAJOR (breaking workflow change), MINOR (new capability added), PATCH (bug fix, description tweak)
- Before updating any skill: backup current version manually or via `skill-semver`
- After a Claude model release: re-read the official release notes, then test all skills that touched breaking areas
- Known breaking change triggers: hook format changes, tool renames, context window changes, install path changes

---

## 9. AUDIT AND MAINTENANCE

**On every model release:**
- Run `npx pulser@latest` on skill library
- Check GitHub anthropics/claude-code issues for `area:skills` regressions
- Test any skill that uses hooks, tool names, or context window references

**Monthly:**
- Run `pulser eval` to detect dead skills and conflicts
- Check for orphaned skills (installed but never triggered)
- Check for duplicate doctrine across skills — consolidate if found
- Verify description budget is under 8,000 chars

**When adding a skill:**
- Run `pulser` score on new skill before adding — must score 70+
- Run eval to check for conflicts with existing skills
- Check total description budget — if >7,500 chars, trim an existing description first

**When removing a skill:**
- Verify no other skill references it
- Archive to `skills/archived/` in brainframe-public rather than deleting

---

## 10. ANTI-PATTERNS (NEVER DO)

- Using a skill to reach external APIs or databases — use MCP
- Using an MCP server for a prompt template — use a skill
- Conditional logic in CLAUDE.md — put in a skill
- System-specific skills at global scope — scope correctly
- Adding skills to fix problems caused by broken skills — audit first
- Deeply nested references in skill bodies — one level only
- Offering multiple approaches in a skill body — one approach
- Skill names that are vague: `helper`, `utils`, `tools`, `general`
- First-person descriptions
- Skills without version fields
- Updating a skill without backing up the current version first
- Skill bodies over 1,000 lines

---

## 11. CURRENT SKILL INVENTORY STATUS

As of 2026-04-07:
- **Total skills:** 30
- **Description budget used:** 7,183 / 8,000 chars (90%)
- **Skills needing description fixes:** 20 / 30 (missing MUST/SHOULD trigger or negative guard)
- **Skills needing `disable-model-invocation` review:** 4
- **Skills needing version field:** all (none currently have it)
- **Description audit status:** pending `pulser` run

Priority fix list (undertriggering risk):
- ai-pulse — no explicit trigger phrases in first 250 chars
- nightwatch-prompts — no trigger, no negative guard
- code-review-excellence — no trigger, no negative guard
- frontend-design — no trigger, no negative guard
- gpt-critique-skill — no trigger, no negative guard
- gpt-deep-research-prompt-skill — too short (135 chars), no trigger, no negative
- perplexity-pro-research-prompt-skill — too short (130 chars), no trigger, no negative
- technical-writing — no trigger, no negative guard
- ubiquitous-language — no trigger, no negative guard
- prd-to-plan — no trigger, no negative guard

---

## 12. PROMOTION RULES

A skill becomes global (moves to `~/.claude/skills/`) when:
- It is used in 2+ projects
- Its behavior is identical across those projects
- It has passed `pulser` score 70+ and eval conflict check

A skill stays project-scoped when:
- It references project-specific entities, repos, or workflows
- Its trigger conditions are project-specific

---

## 13. OPEN ITEMS

- OI-SKILLS-001: Run `pulser` audit on all 30 skills — get baseline scores
- OI-SKILLS-002: Fix 20 descriptions with missing MUST/SHOULD or negative guards
- OI-SKILLS-003: Add `version` field to all 30 skills
- OI-SKILLS-004: Add `disable-model-invocation: true` to quitchat, axiom-close, axiom-health, nightwatch-upgrade-orchestrator, nightwatch-site-audit
- OI-SKILLS-005: Set up skill-semver for auto-backup in brainframe repos
- OI-SKILLS-006: Verify Issue #14882 — measure actual startup token cost of current skill library
- OI-SKILLS-007: Trim description budget below 7,500 chars (currently at 90% — no headroom)
