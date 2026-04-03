---
name: quitchat
description: "Explicit session close skill. Run only when the user types quitchat or run quitchat. Never infer intent from other phrases. Sweeps unsaved context, updates tracking files, checks promotion candidates, and produces a handoff file."
---

# Quitchat
Version: 1.0 (generic base)

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
Scan for: decisions not persisted, bugs not logged, features not in roadmap, prompts written but not run.
Each item: state it + where routed.

**Step 3 — Repo sync** (full only)
Update project state file, append log entry, update roadmap if items changed.
Fetch SHA immediately before each write.

**Step 4 — Promotion candidates**
Scan session for decisions that should apply globally across all projects.
For each candidate:
1. Read PROMOTION_LOG.md from brainframe-public — check for same-day conflicts on the same file
2. No conflict → commit directly to brainframe-public main
3. Append to PROMOTION_LOG.md: `YYYY-MM-DD | [project] | [file] | [description]`
4. Conflict → stop, flag to collaborator

If nothing to promote: state "No promotion candidates this session."

**Step 5 — Memory audit**
Fetch memory edits. Fix stale, duplicated, missing. Report: N reviewed / N changed.

**Step 6 — Skills + instructions check** (full only)
Check project skills for staleness. If updates needed: produce updated SKILL.md files.

**Step 7 — Handoff file**
Produce SESSION_HANDOFF.md. Self-contained. Assume zero memory of session.
Include: summary, last completed, next task, open decisions, first action next session.

## Audit Log Format

```
Tier: FAST / FULL — [signals]
Step 1: RAN / SKIPPED / [findings]
Step 2: [N found / N routed / N unresolved]
Step 3: [files written / UNCHANGED]
Step 4: [N promoted / NONE / CONFLICT — flagged]
Step 5: [N reviewed / N changed]
Step 6: [result]
Step 7: READY
💬 Suggested chat name: [5 words max, lead with project name]
```
