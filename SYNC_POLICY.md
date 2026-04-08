# SYNC_POLICY.md
Brainframe v2.0 | Last updated: 2026-04-08

Defines what is and is not synced from brainframe-public to project repos via GitHub Actions.

---

## Sync Targets

| Project | Destination |
|---------|-------------|
| coinbeast | `coinbeast/brainframe/` |
| nightwatch | `nightwatch/brainframe/` (great-horn-aml-nightwatch) |

Axiom and Mamba: not currently synced. Fetch brainframe files manually via GitHub API if needed.

---

## What Syncs

Everything in brainframe-public EXCEPT the exclusions below.

Safe to sync: GLOBAL_RULES.md, STYLE_RULES.md, COLLAB_RULES.md, CLAUDE.md, DECISIONS.md (archived), ENTRY_SCHEMAS.md, FILE_CONVENTIONS.md, skills/, specs/, references/, docs/ (except docs/admin/), templates/ (excluded).

---

## What Does NOT Sync (rsync excludes)

| Excluded | Reason |
|----------|--------|
| `.git/` | Git internals |
| `.github/` | Workflows — not for project repos |
| `templates/` | Bootstrap templates — not runtime files |
| `docs/admin/` | Admin state files (ADMIN_STATE.md, ADMIN_LOG.md, ADMIN_CONFIG.md, build-log/) — never for project repos |

---

## Adding a New Project to Sync

1. Add a new job to `.github/workflows/sync.yml` — copy an existing job, change repo name and path.
2. Ensure `SYNC_TOKEN` secret has write access to the new repo.
3. Verify after first sync: confirm `docs/admin/` is absent from new repo's `brainframe/` directory.
4. Update this file with the new project in the Sync Targets table.

---

## Rollback Procedure

If a bad sync pushes unwanted files to a project repo:
1. Identify the bad files in the project repo.
2. Delete each file via GitHub API (DELETE /repos/:repo/contents/:path with SHA).
3. Fix the exclude rule in sync.yml.
4. Push a no-op change to brainframe-public main to trigger a clean sync.
5. Verify project repo is clean.
