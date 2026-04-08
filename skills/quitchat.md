---
name: quitchat
description: "Explicit session close skill. Run only when the user types quitchat or run quitchat. Never infer intent from other phrases. Sweeps unsaved context, updates tracking files, checks promotion candidates, and produces a handoff file."
---

# Quitchat
Version: 1.1 | 2026-04-08

Run only on explicit `quitchat` or `run quitchat`. Never infer.

## Tier Selection

**Full close** if ANY: significant decisions made, files changed, 20+ exchanges, new features discussed.
**Fast close** otherwise. State tier before proceeding.

## Steps

**Fast: 2, 4, 5**
**Full: all**

**Step 1 — Chat sweep** (full only)
Check recent chats for context not in this session. State findings.

**Step 2 — Unsaved context sweep**
Unsaved context = any of:
- Decision made this session (CONFIRMED or PROVISIONAL) with no DECISIONS.md entry in brainframe-comms/_decisions/DECISIONS.md
- File written or modified this session with no PROMOTION_LOG.md entry
- Open item surfaced this session not yet in project state file

Each item: state it + where routed.

**Step 3 — Repo sync** (full only)
Admin project: overwrite `brainframe-public/docs/admin/ADMIN_STATE.md`, append to `brainframe-public/docs/admin/ADMIN_LOG.md`, write build log to `brainframe-public/docs/admin/build-log/YYYY-MM-DD.md`.
Other projects: update project state file, append log entry, update roadmap if items changed.
Fetch fresh SHA immediately before each write — never use cached SHA.

**Step 4 — Promotion candidates**
Scan session for decisions that should apply globally across all projects.
For each candidate:
1. Read PROMOTION_LOG.md from brainframe-public — check for same-day conflicts on the same file
2. No conflict → commit directly to brainframe-public main via GitHub API
3. Append to PROMOTION_LOG.md: `YYYY-MM-DD | [project] | [file] | [description]`
4. Conflict → stop, flag to Dave

PROMOTION_LOG check is mandatory in both Fast and Full tiers.

If nothing to promote: state "No promotion candidates this session."

**Step 5 — Memory audit**
Fetch memory edits. Diff format: report only entries changed, added, or removed since last session. Full audit on Dave's explicit request only.
Report: N reviewed / N changed.

**Step 6 — Skills + instructions check** (full only)
Check project skills for staleness. If updates needed: produce updated SKILL.md files.

**Step 7 — Handoff file**
Produce SESSION_HANDOFF.md. Self-contained. Assume zero memory of session.
Include: summary, last completed, next task, open decisions, first action next session.

## Key Paths (Admin project)

| File | Path | Operation |
|------|------|-----------|
| ADMIN_STATE.md | brainframe-public/docs/admin/ADMIN_STATE.md | Overwrite |
| ADMIN_LOG.md | brainframe-public/docs/admin/ADMIN_LOG.md | Append only |
| Build log | brainframe-public/docs/admin/build-log/YYYY-MM-DD.md | Append or create |
| PROMOTION_LOG.md | brainframe-public/PROMOTION_LOG.md | Append only |
| DECISIONS.md (write) | brainframe-comms/_decisions/DECISIONS.md | Append only |
| DECISIONS.md (read) | brainframe-public/DECISIONS.md | Read-only archive |

## Audit Log Format

```
Tier: FAST / FULL — [project]
Step 2: [N found / 0 found]
Step 3: [files written]
Step 4: [N promoted / none]
Step 5: [N reviewed / N changed]
```
