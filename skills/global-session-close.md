---
name: global-session-close
description: "Global session close base pattern. All project quitchat skills extend this. Never duplicate it."
---

# Global Session Close Pattern
Version: 1.0 | 2026-04-03

Run only on explicit close trigger. Never infer.

## STEPS (in order)

1. Verify STATE file is current — flag divergence before proceeding
2. Overwrite STATE with current working state (branch, next task, blockers)
3. Append dated entry to LOG — never overwrite
4. Overwrite HANDOFF files with fresh agent-boundary state
5. Generate build log: `docs/build-log/YYYY-MM-DD-[TASK-ID].md` — commit via GitHub API
6. Audit memory — flag stale items and session decisions worth persisting
7. Produce handoff brief via present_files
8. Suggest chat name

## RULES

- Never say "updated/pushed/saved" unless tool returned success
- Skipped step → "SKIPPED — reason", continue
- Unresolved items go in handoff brief, never silently dropped
- LOG is append-only — never overwrite
- Build log is the primary onboarding artifact for next session
