# Spec: Cross-Project DECISIONS.md Bus
Project: Admin
Version: v1
Status: ACTIVE
Upgrade ref: N/A (operational protocol, not a code upgrade)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Inter-project communication routes through DECISIONS.md in brainframe-public. Rules exist in GLOBAL_RULES.md but there is no spec defining the bus contract — schema, routing, conflict resolution, and size management. Without a spec, implementations drift and the bus degrades silently across sessions.

## Users / Use Cases
- All project DAIs — write decisions to bus, read decisions filtered by their project tag
- Admin DAI — owns and maintains the bus, enforces schema compliance
- Nightwatch — reads synced local copy at `brainframe/DECISIONS.md` filtering for `Applies to: nightwatch`

## Success Metrics
- Every DECISIONS.md entry includes all Schema 1.0 required fields (What/Why/How/Status/Date/Source + Applies-to)
- No same-day write conflicts go undetected — Rule 131 catches and merges all conflicts
- File stays under 5000-word cap; archive procedure fires at 4000 words (80%)
- Every project DAI can filter entries by `Applies to: {project}` without reading the full file

## Requirements
1. Canonical bus: `brainframe-public/DECISIONS.md` only — no other inter-project channel
2. Schema: Schema 1.0 per ENTRY_SCHEMAS.md — fields: What / Why / How to apply / Status / Date / Source / Applies to
3. Write pattern: fetch fresh SHA → decode base64 → append entry → re-encode → PUT — never use cached SHA
4. Same-day conflict (Rule 131): detect by re-reading file before write; if conflict exists, merge then write
5. Tags on every entry: CONFIRMED / PROVISIONAL / SUPERSEDED
6. Size limit: 5000 words (FILE_CONVENTIONS.md) — archive procedure triggers at 4000 words
7. Archive procedure: move entries older than 90 days with status CONFIRMED to `docs/admin/decisions-archive/YYYY.md`
8. Nightwatch reads synced local copy at `{nightwatch-repo}/brainframe/DECISIONS.md` — acceptable lag is one sync cycle
9. All other projects fetch directly from brainframe-public via GitHub API
10. Project-internal decisions stay in project repos — do not route through this bus

## Non-Goals
- Project-internal decisions (use project repo files for those)
- Real-time notification (polling / sync lag is acceptable)
- Storing sensitive credentials or PII in DECISIONS.md

## Constraints / Assumptions
- ENTRY_SCHEMAS.md is authoritative for Schema 1.0 — never infer schema from memory
- FILE_CONVENTIONS.md defines 5000-word cap — check at session start
- GitHub API write returns 409 on stale SHA — always re-fetch before write
- Nightwatch sync lag: one GitHub Actions cycle (push to brainframe-public → trigger → push to nightwatch)

## Open Questions
| ID | Question | Owner |
|----|----------|-------|
| OQ-001 | Archive procedure confirmed: move entries >90 days + CONFIRMED status to `docs/admin/decisions-archive/YYYY.md`? | Dave |
| OQ-002 | Should projects other than Nightwatch also maintain a synced local copy, or always fetch live? | Dave |

## Dependencies
- `brainframe-public/ENTRY_SCHEMAS.md` — Schema 1.0 definition
- `brainframe-public/FILE_CONVENTIONS.md` — size limits
- `brainframe-public/GLOBAL_RULES.md` — routing rules and Rule 131
- GitHub Actions sync.yml — Nightwatch local copy sync mechanism

## Flows / Design Notes
Write: any DAI → fetch SHA → decode → append Schema 1.0 entry → re-encode → PUT. 
Read: fetch file → filter lines containing `Applies to: {project}` → process matching entries only.
Conflict: re-read current content → identify added entries since last read → merge → write.

## Related Docs
- `brainframe-public/ENTRY_SCHEMAS.md`
- `brainframe-public/DECISIONS.md`
- `brainframe-public/FILE_CONVENTIONS.md`
- `.github/workflows/sync.yml` (Nightwatch sync mechanism)
