# Spec: Brainframe GitHub Actions Sync
Project: Admin
Version: v2
Status: ACTIVE
Upgrade ref: N/A (infrastructure — already fixed 2026-04-08)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
The GitHub Actions sync workflow (sync.yml) used rsync --delete to push brainframe-public wholesale into project repos, including docs/admin/ (containing ADMIN_STATE.md, ADMIN_LOG.md, ADMIN_CONFIG.md). This propagated admin-only state files into coinbeast and nightwatch repos. Fixed 2026-04-08.

## Current State (post-fix)
- sync.yml updated: docs/admin/ excluded from rsync
- docs/admin/ deleted from coinbeast/brainframe/ and nightwatch/brainframe/
- SYNC_POLICY.md written to brainframe-public root
- CLAUDE.md confirmed safe to sync (no credentials, no admin routing)

## Users / Use Cases
- Nightwatch — receives brainframe sync into `nightwatch/brainframe/`
- Coinbeast — receives brainframe sync into `coinbeast/brainframe/`
- Admin — owns sync config, maintains as projects are added

## Success Metrics
- No admin content (docs/admin/) in any project repo's brainframe/ directory
- Sync propagates legitimate global rules correctly on every push
- Adding a new project = one job added to sync.yml, SYNC_POLICY.md updated
- SYNC_POLICY.md is readable and current

## Requirements
1. sync.yml rsync excludes: `.git`, `.github`, `templates/`, `docs/admin/`
2. SYNC_POLICY.md at brainframe-public root — lists what syncs and what doesn't, updated when exclusions change
3. Axiom and mamba-mode: NOT currently synced — fetch brainframe files manually via GitHub API if needed (Dave confirmed: add later if needed)
4. Verification after any sync.yml change: check that `docs/admin/` is absent from all project brainframe/ directories
5. Adding a new project: add one job to sync.yml + update SYNC_POLICY.md Sync Targets table

## Rollback Procedure
If a bad sync pushes unwanted files to a project repo:
1. Identify bad files in project repo
2. Delete each via GitHub API: DELETE /repos/:repo/contents/:path with current SHA
3. Fix exclude rule in sync.yml
4. Push any change to brainframe-public main to trigger clean sync
5. Verify project repo is clean

## Non-Goals
- Changing sync mechanism from GitHub Actions rsync
- Encrypting synced content
- Syncing to axiom/mamba-mode (manual fetch only for now)

## Constraints / Assumptions
- SYNC_TOKEN secret configured in brainframe-public — provides push access to coinbeast and nightwatch
- rsync --delete: files removed from brainframe-public are removed from project repos on next sync
- CLAUDE.md: safe to sync — contains no credentials or admin routing
- docs/admin/: never sync — contains admin state files that are brainframe-wide, not project-specific

## Open Questions
| ID | Question | Resolution |
|----|----------|------------|
| OQ-001 | Contamination audit | RESOLVED: docs/admin/ was in both repos. Deleted 2026-04-08. |
| OQ-002 | Add axiom + mamba-mode to sync? | RESOLVED: Not now. Add manually if needed later. |
| OQ-003 | Transition plan for project AIs reading CLAUDE.md | RESOLVED: CLAUDE.md unchanged — no transition needed. |

## Dependencies
- `.github/workflows/sync.yml` in brainframe-public
- `SYNC_POLICY.md` in brainframe-public

## Related Docs
- `SYNC_POLICY.md` (brainframe-public)
- `.github/workflows/sync.yml` (brainframe-public)
