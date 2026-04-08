# Brainframe Skills Standards
*Load this file whenever creating or updating any skill in Dave Bradley's workflow.*
*Fetched from brainframe-public at session start.*

---

## YAML Frontmatter Rules

Always use `>-` block scalar for descriptions — no quoting, no escape issues:

```yaml
---
name: skill-name-kebab-case
description: >-
  What it does. MUST be used when [primary trigger]. Do NOT use for [guard].
disable-model-invocation: true   # only for destructive/side-effect skills
---
```

### Allowed Fields (claude.ai)
`name`, `description`, `license`, `allowed-tools`, `metadata`, `disable-model-invocation`, `user-invocable`

### NEVER include
- `version` — causes "unexpected key" error in claude.ai validator
- `author`, `category`, `tags` — same error

### Failure Modes to Avoid
| Symptom | Cause | Fix |
|---------|-------|-----|
| `malformed YAML frontmatter` | Inner `"` inside double-quoted description | Use `>-` block scalar |
| `unexpected key` | `version` or other unsupported field | Remove it |
| `malformed YAML` | Colon+space, `#`, `&`, `*` in unquoted value | Use `>-` block scalar |
| `malformed YAML` | Tab indentation | Spaces only |
| Skill never triggers | Description too vague | Add MUST/SHOULD trigger |
| Skill always triggers | No negative guard | Add Do NOT clause |

---

## Description Standard

Every description MUST follow this template (within 250 chars — truncation point):

```
[What it does]. MUST be used when [trigger conditions].
Do NOT use for [most common false positive].
```

- Third person only ("Processes X" not "I can help with X")
- MUST/SHOULD RFC 2119 keywords to prevent undertriggering
- Explicit Do NOT guard to prevent overtriggering
- Front-load the key use case — first 100 chars must stand alone
- Hard limit: 1024 chars total, 250 chars effective (truncation)

---

## Skill Architecture

### Project-Agnostic First
Every skill must work across all projects. Project-specific content goes in
`references/` files fetched from brainframe-public via GitHub API — not in
the skill body.

Reference file URL pattern:
`https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/references/[filename].md`

Existing reference files in brainframe-public:
- `nightwatch-entities.md` — Base44 entity inventory and graph schema
- `nightwatch-review-rules.md` — Code review rules (roleUtils, terminology)
- `nightwatch-ux-config.md` — UX user profiles and design constraints
- `nightwatch-roadmap-config.md` — Roadmap file paths and Amanda flags
- `nightwatch-config.md` — Proof of work defaults
- `axiom-research-context.md` — Axiom Perplexity/GPT research context

### Scope
- Global skills: `~/.claude/skills/` — used across 2+ projects
- Project skills: `.claude/skills/` — project-specific

### Body Size
- Keep under 500 lines / 5,000 words
- Over 1,000 lines = loads entirely on every invocation
- Extract large sections to `references/` files

### `disable-model-invocation: true` Required When
- Skill has side effects (writes, deploys, API calls)
- Skill should only run on explicit user trigger
- Destructive or irreversible operations

Current skills with this flag: quitchat, axiom-close, axiom-health,
nightwatch-site-audit

---

## Full Standards References

- **SKILLS_RESEARCH.md**: `docs/token-optimization/SKILLS_RESEARCH.md` in brainframe-public
  Full research on skill trigger mechanics, failure modes, token costs, and best practices.

- **UNIFIED_SKILLS_POLICY.md**: `docs/UNIFIED_SKILLS_POLICY.md` in brainframe-public
  Complete policy covering scope, governance, audit cadence, and anti-patterns.

Fetch either file via GitHub API when making significant skill architecture decisions.

---

## Anti-Patterns

- Using MCP for a prompt template — use a skill
- Skill body attempting external API calls — use MCP
- Conditional logic in CLAUDE.md — belongs in a skill
- Project-specific content in global skill body — extract to reference file
- System-specific skills at global scope
- Adding skills to fix problems caused by broken skills — audit first
- References nested more than one level deep
- First-person descriptions
- `version` field in frontmatter
- Not backing up before updating a skill (Claude frequently drops reference files)
