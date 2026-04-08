---
name: project-instructions
description: >-
  Regenerates Claude Project instructions for any Brainframe project. MUST be used when Dave says "redo instructions", "regenerate project instructions", "update project instructions", or when project instructions need rebuilding after structural changes. Fetches live state from GitHub, enforces a locked template per project type, diffs against prior version to flag bloat, and delivers a one-click copyable output. Never regenerates from memory alone — always pulls live state first.
---

# Project Instructions Skill
Version: 1.0 | 2026-04-08

Run only on explicit instruction regeneration request. Never infer.

---

## PURPOSE

Prevent drift and bloat in Claude Project instruction files by enforcing:
1. A locked section template (no freeform additions)
2. Live state fetch before every regeneration (no memory-only rewrites)
3. Bloat detection (flag any section growing >20% vs prior)
4. One-click copyable delivery

---

## STEP 1 — DETECT PROJECT

Identify which project's instructions to regenerate from conversation context:

| Signal | Project |
|--------|---------|
| "admin", "brainframe", no project-specific signals | Admin DAI |
| "nightwatch", "NW-UPGRADE", "Amanda", "AVLM" | Nightwatch |
| "axiom", "AX-UPGRADE", "pattern library" | Axiom |
| "mambamode", "mamba-mode", "NE-UPGRADE" | Mambamode |

If ambiguous — ask Dave before proceeding.

---

## STEP 2 — FETCH LIVE STATE

Always fetch. Never regenerate from memory.

**For all projects, fetch from brainframe-public:**
- `GLOBAL_RULES.md` — tool routing, response style
- `STYLE_RULES.md` — brevity, tone, formatting
- `docs/admin/ADMIN_CONFIG.md` — identity, contacts, repos
- `docs/admin/ADMIN_STATE.md` — open items, next task

**Project-specific additions:**

| Project | Also fetch |
|---------|-----------|
| Nightwatch | `great-horn-aml-nightwatch/CLAUDE.md` |
| Axiom | `axiom/CLAUDE.md` |
| Mambamode | `mamba-mode/CLAUDE.md` |

PAT is in project instructions CREDENTIALS section. Use GitHub API via bash.

---

## STEP 3 — APPLY LOCKED TEMPLATE

Each project type has a fixed section order. Add nothing outside these sections. Remove nothing from the template. Only the content within sections changes.

### Admin DAI Template

```
# Claude Project Instructions — Dave Bradley / Admin DAI
Brainframe v2.0 | Reload at 30 exchanges

## CREDENTIALS
[PAT only]

## RULE ZERO — BREVITY
[Hard cap, forbidden phrases, terse rule]

## IDENTITY
[Name, orgs, role, dev tool]

## SESSION START — MANDATORY, IN ORDER
[Fetch sequence + SESSION GATE block]

## REPOS
[Table: name → slug. Full write-access list.]

## TOOL ROUTING
[Table only]

## EXECUTION RULES
[Bullet list — max 10 items]

## INTER-PROJECT MESSAGES
[Canonical bus rules]

## PROMOTION
[3-step checklist]

## STATE + DECISION DISCIPLINE
[4 bullets]

## EXCHANGE LIMITS
[3 lines]

## SKILLS
[Trigger → skill table]

## ALWAYS FLAG IMMEDIATELY
[4 bullets max]
```

### Nightwatch / Axiom / Mambamode Template

```
# Claude Project Instructions — [Project Name]
Brainframe v2.0 | Reload at 30 exchanges

## CREDENTIALS
[PAT only]

## RULE ZERO — BREVITY
[Same as Admin]

## IDENTITY
[Project name, repo, stack, current upgrade prefix]

## SESSION START — MANDATORY, IN ORDER
[Project-specific fetch sequence + GATE block]

## TOOL ROUTING
[Table only]

## EXECUTION RULES
[Project-specific bullets — max 10]

## UPGRADE DISCIPLINE
[Upgrade prefix, SANITYCHECK rules, branch gates]

## EXCHANGE LIMITS
[3 lines]

## SKILLS
[Trigger → skill table]

## ALWAYS FLAG IMMEDIATELY
[Project-specific flags — max 4]
```

---

## STEP 4 — BLOAT CHECK

Before writing, compare section word counts against the previous version if available in context.

Flag any section that grew >20%:
```
⚠️ BLOAT WARNING: [Section] grew from ~N words to ~N words (+X%). Review before accepting.
```

If no prior version available — skip bloat check, note it.

---

## STEP 5 — ANTI-DRIFT RULES

Apply these when populating the template:

- **No filler rules.** Every line must be actionable. If it restates what Claude already does by default — cut it.
- **No failure patches.** If a rule exists only because Claude did something wrong once — evaluate whether it's still needed. If the behavior is fixed in Claude 4 — cut it.
- **No aggressive emphasis.** Replace "CRITICAL: MUST always..." with "Always...". Claude 4 overtriggers on caps.
- **No negative constraints.** Reframe "Never use bullet points" → "Use flowing prose." Pink Elephant effect.
- **Prohibitions over instructions for behavioral rules.** "Avoid X" holds longer in long sessions than "Do X."
- **Keep CREDENTIALS at the top.** PAT must be findable in the first 10 lines.
- **Open items stay in ADMIN_STATE.md**, not in project instructions. Only standing flags belong here.

---

## STEP 6 — DELIVER

1. Produce the regenerated instructions as a file at `/mnt/user-data/outputs/project-instructions.md`
2. Present via `present_files`
3. State what changed vs prior version (additions, cuts, bloat flags)
4. Do NOT paste inline

---

## GLOBAL RULES

1. Never regenerate from memory. Always fetch first.
2. Never add sections outside the locked template.
3. Never say "updated" unless GitHub API returned success (for any writes).
4. Bloat warnings are advisory — Dave decides whether to accept.
5. One output file only. No inline copy blocks.
