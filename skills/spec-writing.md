---
name: spec-writing
description: >-
  Writes, updates, versions, and mirrors feature specs across brainframe-comms and project repos.
  MUST be used when Dave says "spec this", "write a spec", "stub this", "update spec", or describes
  a feature, module, or idea that needs documenting. Also triggers automatically at the end of a
  brainstorm session when a decision is reached, when a new roadmap item is added, when quitchat
  surfaces an open item with no spec, or when a Cursor prompt is requested for an unspecced upgrade.
  Do NOT skip — no Cursor prompt gets written for an unspecced upgrade without Dave explicitly overriding.
---

# Spec Writing Skill
Version: 1.1 | 2026-04-09

Writes feature specs, saves them to brainframe-comms, mirrors to project repo, then auto-fires
the critique-spec skill. Surfaces a summary + open questions to Dave. Versions on every meaningful update.

---

## MODES

| Mode | Trigger |
|------|---------|
| FULL | "spec this", "write a spec", post-brainstorm decision |
| STUB | "stub this", random idea, roadmap item added, quitchat open item |
| UPDATE | "update spec", post-critique resolution |
| GAP | "gap analysis" — cross-project scan |

Start in STUB if context is thin. Upgrade to FULL when Dave provides enough detail.

---

## STEP 1 — DETECT PROJECT + LOCATE EXISTING SPEC

1. Detect project from session context (Nightwatch / Axiom / Mambamode / Coinbeast / Winston / Admin / BitcoinBrains).
2. Check `brainframe-comms/specs/{project}/` for an existing spec matching this feature.
3. If found → load it, go to UPDATE mode.
4. If not found → proceed to STEP 2.

---

## STEP 2 — DETERMINE MODE

**STUB mode** — use when:
- Idea is half-baked, no detail yet
- Brainstorm just ended, decision captured but not fleshed out
- Quitchat surfaces an open item

STUB saves immediately. Fields not yet known → `TBD`. Status: `DRAFT`.

**FULL mode** — use when:
- Dave provides enough context to fill most fields
- Explicit "spec this" with detail

---

## STEP 2B — DATABASE GATE (runs before writing Requirements)

Scan the feature description for any of these signals:
- Tables, schemas, columns, rows, migrations, indexes, queries
- Supabase, Postgres, SQLite, Prisma, Drizzle
- Storing, fetching, querying, persisting structured data
- Entity relationships, foreign keys, joins
- Data model, data layer, data structure

**If any signal is present:**
1. Load `/mnt/skills/user/db-engineer/SKILL.md`
2. Apply db-engineer judgment to the Requirements section — flag schema decisions, naming conventions, index implications, migration needs
3. Add a `## Database Notes` section to the spec with:
   - Affected tables (known or proposed)
   - Schema considerations
   - Migration required? (yes / no / TBD)
   - Index implications
   - Open questions for db layer (assigned OQ-XXX IDs)
4. Continue to STEP 3.

**If no signal present:** skip this gate, proceed to STEP 3.

---

## STEP 3 — WRITE THE SPEC

Use this schema. Mark optional fields as `N/A` if not applicable. Never omit required fields.

```markdown
# Spec: [Feature / Module Name]
Project: [project name]
Version: v1
Status: DRAFT | ACTIVE | SUPERSEDED
Upgrade ref: [NW-UPGRADE-XXX / AX-UPGRADE-XXX / etc — if known, else TBD]
Created: [YYYY-MM-DD]
Last updated: [YYYY-MM-DD]

---

## Problem Statement
[What problem does this solve? Why does it matter? 2–4 sentences.]

## Users / Use Cases
[Who uses this? What are they trying to accomplish?]

## Success Metrics
[How do we know this worked? Measurable outcomes. If discovery/exploration: learning goals instead.]

## Requirements
[What must exist. Numbered list. Specific and testable.]

## Non-Goals
[Explicit scope exclusions — what this does NOT do.]

## Constraints / Assumptions
[Technical limits, data availability, third-party dependencies, known unknowns.]

## Database Notes
[Only present if DB gate triggered. Affected tables, schema considerations, migration required, index implications, OQ-XXX for db open questions.]

## Open Questions
[Unresolved issues. Each gets an ID: OQ-001, OQ-002. These become critique targets.]

## Dependencies
[Other specs, upgrades, external APIs, or team inputs this blocks on or is blocked by.]

## Flows / Design Notes
[Interaction flows, mockups, UX intent. Optional — omit if Cursor-only implementation.]

## Timeline
[Optional. Populate when humans are involved. Omit for solo/Cursor-only work.]

## Stakeholders
[Optional. Populate when humans are involved. Omit for solo/Cursor-only work.]

## Related Docs
[Links to DECISIONS.md entries, roadmap items, other specs, research files.]
```

---

## STEP 4 — SAVE TO BRAINFRAME-COMMS (source of truth)

Filename convention: `{project}-{feature-slug}-v{N}.md`
Path: `brainframe-comms/specs/{project}/{filename}`

1. Fetch SHA of existing file if it exists.
2. Write via GitHub API (PUT). Append, never overwrite previous versions — increment N.
3. Comms PAT: from `brainframe-comms/_docs/REGISTRY.md`.

---

## STEP 5 — MIRROR TO PROJECT REPO

Path: `{project-repo}/specs/{filename}` (same filename as comms)

Rules:
- Mirror is READ-ONLY for Cursor — never edited directly
- All updates go to comms first, mirror second
- Write via GitHub API immediately after comms write confirms

Project repo mapping:
| Project | Repo |
|---------|------|
| Nightwatch | bitcoinbrainsweb/great-horn-aml-nightwatch |
| Axiom | bitcoinbrainsweb/axiom |
| Mambamode | bitcoinbrainsweb/mamba-mode |
| Coinbeast | bitcoinbrainsweb/coinbeast |
| Winston | bitcoinbrainsweb/winston |
| Admin | bitcoinbrainsweb/brainframe-public |

---

## STEP 6 — AUTO-CRITIQUE (HARD GATE — cannot be skipped)

This step is mandatory for every FULL spec. STUB mode: skip critique, note it's pending until spec is promoted to FULL.

After both writes confirm:

1. Load `/mnt/skills/user/critique-spec/SKILL.md`.
2. Fetch the saved spec from brainframe-comms via raw URL (do not use the in-memory version).
3. Run the critique pipeline:
   - Generate GPT-4o critique prompt from `prompts/gpt-critique-prompt.md`
   - Present to Dave as a copyable widget
   - Wait for Dave to paste GPT output back
   - Generate Perplexity sonar-pro critique prompt from `prompts/perplexity-critique-prompt.md`
   - Present to Dave as a copyable widget
   - Wait for Dave to paste Perplexity output back
   - Synthesize both outputs per critique-spec output format
4. If Dave explicitly says "skip critique" — note it in the spec as `Critique: SKIPPED — Dave override` and proceed.

**Do not mark a FULL spec as ACTIVE until critique has run or Dave has explicitly overridden.**

Surface to Dave only:
```
SPEC SAVED: {filename} v{N}
Comms: ✅ | Mirror: ✅ | DB gate: triggered / skipped

CRITIQUE SUMMARY
Top issues: [2–3 bullets, max one sentence each]
Open questions flagged: [OQ-001, OQ-002 — one line each]
Recommended next: [one action]
```

---

## STEP 7 — UPDATE MODE

Triggered by: "update spec", post-critique resolution, feature change mid-build.

1. Fetch current spec from comms (source of truth — never from mirror).
2. Apply changes.
3. Increment version: v1 → v2.
4. Update `Last updated` date.
5. Save to comms → mirror → surface summary (no auto-critique unless Dave requests it).

Previous versions are NOT deleted. Archive by keeping vN-1 in place — only the latest vN is active.

---

## GAP ANALYSIS MODE

Trigger: Dave says "gap analysis"

1. List all specs in `brainframe-comms/specs/` across all projects.
2. Cross-reference against roadmap items in each project's `_status/` file.
3. Surface:
   - Roadmap items with no spec (unspecced upgrades)
   - Specs with status DRAFT > 14 days old (stale drafts)
   - Open questions (OQ-XXX) with no resolution across all specs
   - Specs referencing each other with no dependency link declared
4. Present as a table. Dave decides what to action.

---

## INTEGRATION WITH PROMPT-WRITING SKILL

Before any Cursor prompt is written for an upgrade:
1. Check if a spec exists for that upgrade ref in `brainframe-comms/specs/{project}/`.
2. If no spec → flag to Dave, offer to stub one before proceeding.
3. If spec exists → include this block in the Cursor prompt:

```
## Spec Reference
File: specs/{filename}
Version: v{N}
Key constraints: [pull Requirements + Non-Goals + Constraints from spec — 3–5 bullets]
Open questions (do not resolve — flag in RESULT): [OQ-XXX list]
```

---

## RULES

- Comms is always source of truth. Never read from mirror.
- No Cursor prompt without a spec — enforce this. Dave can override explicitly.
- STUB immediately rather than waiting for full detail.
- Never drop open questions — they become critique targets.
- DB gate runs before Requirements are finalized — not after.
- Auto-critique is a hard gate on FULL specs. STUB specs are exempt until promoted.
- Timeline and Stakeholders: omit for solo/Cursor-only work; populate when humans involved.
- 5000-word cap per FILE_CONVENTIONS.md. If spec approaches limit, split into sub-specs.
