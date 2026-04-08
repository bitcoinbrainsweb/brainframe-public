# Spec: Brainframe GitHub Actions Sync
Project: Admin
Version: v1
Status: ACTIVE
Upgrade ref: TBD (fix required — contamination unresolved)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
The GitHub Actions sync workflow (`sync.yml` in brainframe-public) uses `rsync --delete` to push the entire brainframe-public repo into `{project}/brainframe/` for coinbeast and nightwatch. This includes CLAUDE.md, which contains admin-specific content (credentials references, admin-only routing rules, internal tool config). That content propagates into coinbeast and nightwatch repos, creating a security and contamination risk that has been flagged but not yet resolved.

## Users / Use Cases
- Nightwatch — receives brainframe sync into `nightwatch/brainframe/` on every push to brainframe-public main
- Coinbeast — receives brainframe sync into `coinbeast/brainframe/` on every push to brainframe-public main
- Admin — owns sync config, must maintain it as projects are added

## Success Metrics
- CLAUDE.md in project repos contains only project-relevant global rules — zero admin-specific content
- Sync continues to propagate legitimate global rules (GLOBAL_RULES.md, STYLE_RULES.md, etc.) correctly
- Adding a new project to the sync requires only adding one job to sync.yml — no bespoke configuration
- Audit confirms no credentials or admin routing content in any project repo's brainframe/ directory

## Requirements
1. Audit current sync scope: determine exactly which files from brainframe-public are reaching project repos
2. Split CLAUDE.md into `CLAUDE-global.md` (safe to sync) and `CLAUDE-admin.md` (never synced)
3. Add rsync exclude rule for `CLAUDE-admin.md` and any other admin-only files identified in audit
4. Update sync.yml to exclude: `.git`, `.github`, `templates/`, `CLAUDE-admin.md`, `docs/admin/`
5. Verify: after fix, run sync and confirm project brainframe/ directories contain no admin content
6. Document: add `SYNC_POLICY.md` to brainframe-public root listing what is and is not synced
7. Current sync targets: coinbeast (`coinbeast/brainframe/`) and nightwatch (`nightwatch/brainframe/`)

## Non-Goals
- Changing the sync mechanism from GitHub Actions rsync (this approach works — just needs filtering)
- Syncing to axiom, mamba-mode, or other repos not currently in sync.yml (add separately if needed)
- Encrypting synced content (filtering is the fix, not encryption)

## Constraints / Assumptions
- sync.yml confirmed: two jobs (sync-to-coinbeast, sync-to-nightwatch), rsync --delete, excludes .git and .github and templates/ only
- SYNC_TOKEN secret is already configured in brainframe-public for push access to project repos
- CLAUDE.md split is a breaking change — any project AI reading `brainframe/CLAUDE.md` must be updated to read `brainframe/CLAUDE-global.md` instead
- `docs/admin/` contains ADMIN_STATE.md, ADMIN_LOG.md, ADMIN_CONFIG.md — these must never be synced to project repos

## Open Questions
| ID | Question | Owner |
|----|----------|-------|
| OQ-001 | Has anyone confirmed which content currently in project repos' brainframe/ directories is contaminated? Run audit before implementing fix. | Admin |
| OQ-002 | Should axiom and mamba-mode be added to the sync, or stay manual? | Dave |
| OQ-003 | After CLAUDE.md split, what is the transition plan for project AIs currently reading the unsplit file? | Dave |

## Dependencies
- `.github/workflows/sync.yml` in brainframe-public — the sync definition (modify here)
- CLAUDE.md in brainframe-public — must be split before re-syncing
- All project AIs that read `brainframe/CLAUDE.md` — must be updated to new filename

## Flows / Design Notes
Fix sequence: (1) audit current contamination → (2) split CLAUDE.md → (3) update sync.yml excludes → (4) push to main → (5) verify project repos → (6) update project AI instructions to new filename → (7) write SYNC_POLICY.md.
Do not push the fix until CLAUDE.md split is confirmed — partial fix risks worse contamination.

## Related Docs
- `.github/workflows/sync.yml` (brainframe-public)
- Flagged in memory: "CLAUDE.md cross-project contamination risk — flagged, not yet resolved"
