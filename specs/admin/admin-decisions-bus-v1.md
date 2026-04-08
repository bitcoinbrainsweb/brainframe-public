# Spec: Cross-Project DECISIONS.md Bus
Project: Admin
Version: v2
Status: ACTIVE
Upgrade ref: N/A (operational protocol)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Inter-project communication routes through a canonical DECISIONS.md file. Rules exist in GLOBAL_RULES.md but there was no spec defining the bus contract — schema, routing, write permissions, conflict resolution, and size management. Without a spec, implementations drift and the bus degrades silently across sessions.

## Users / Use Cases
- All project DAIs — write to their scoped paths, read decisions filtered by their project tag
- Admin DAI — owns and maintains the bus, enforces schema compliance, archives
- Nightwatch — fetches directly from brainframe-comms via GitHub API (no sync path available)

## Success Metrics
- Every DECISIONS.md entry includes all Schema 1.0 required fields
- No same-day write conflicts go undetected — Rule 131 catches and merges all
- File stays under 5000-word cap; archive fires at 4000 words
- Every project DAI reads only entries tagged for their project — no full-file reads needed

## Requirements
1. Canonical bus: `brainframe-comms/_decisions/DECISIONS.md` — write target as of 2026-04-07. brainframe-public/DECISIONS.md is read-only archive.
2. Schema: Schema 1.0 per ENTRY_SCHEMAS.md — fields: What / Why / How to apply / Status / Date / Source / Applies to
3. Write permissions matrix:
   - Admin DAI → `_decisions/` and `_admin/` only
   - Project DAIs → `_status/[project].md` only
   - No project ever writes to another project's status file
4. Write pattern: fetch fresh SHA → decode base64 → append entry → re-encode → PUT — never use cached SHA
5. Same-day conflict (Rule 131): re-read file before write; if new entries appeared since last read, merge then write
6. Tags on every entry: CONFIRMED / PROVISIONAL / SUPERSEDED
7. Size limit: 5000 words — archive fires at 4000 words (80%)
8. Archive procedure: entries older than 90 days with status CONFIRMED move to `_decisions/archive/YYYY.md`
9. All projects fetch from brainframe-comms/_decisions/DECISIONS.md directly via GitHub API — no sync path
10. brainframe-public/DECISIONS.md: read at session start for historical decisions only — never write

## Non-Goals
- Project-internal decisions (stay in project repos)
- Real-time notification (polling lag acceptable)
- Storing credentials or PII in DECISIONS.md

## Constraints / Assumptions
- brainframe-comms PAT: in REGISTRY.md — all DAIs that write to bus must use this PAT
- ENTRY_SCHEMAS.md is authoritative for Schema 1.0 — never infer schema from memory
- GitHub API returns 409 on stale SHA — always re-fetch immediately before write
- Nightwatch has no sync path to brainframe-comms — must fetch directly via API

## Open Questions
| ID | Question | Owner | Resolution |
|----|----------|-------|------------|
| OQ-001 | Archive procedure: 90 days + CONFIRMED → `_decisions/archive/YYYY.md` confirmed? | Dave | CONFIRMED — implement |
| OQ-002 | Should projects other than Nightwatch maintain a synced local copy? | Dave | No — all fetch live from brainframe-comms |

## Dependencies
- `brainframe-comms/ENTRY_SCHEMAS.md` — Schema 1.0
- `brainframe-comms/FILE_CONVENTIONS.md` — size limits
- `brainframe-comms/_docs/REGISTRY.md` — PAT for bus writes
- brainframe-public/DECISIONS.md — historical archive (read-only)

## Flows / Design Notes
Write: Admin DAI → fetch SHA from brainframe-comms/_decisions/DECISIONS.md → decode → append Schema 1.0 entry → re-encode → PUT.
Read: fetch brainframe-comms/_decisions/DECISIONS.md → filter by `Applies to: {project}`.
Conflict (Rule 131): re-read current content → identify entries added since last read → merge → write.
Historical: fetch brainframe-public/DECISIONS.md at session start → filter `Applies to: admin` → read-only.

## Related Docs
- `brainframe-comms/ENTRY_SCHEMAS.md`
- `brainframe-comms/_decisions/DECISIONS.md`
- `brainframe-comms/_docs/REGISTRY.md`
- `brainframe-public/DECISIONS.md` (archived)
- DECISIONS.md entry 2026-04-07: brainframe-comms is new write target
- DECISIONS.md entry 2026-04-07: trust hierarchy and write scoping
