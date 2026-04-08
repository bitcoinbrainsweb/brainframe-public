# Quitchat — Nightwatch Close Procedure
*Fetched by quitchat skill when project is detected as Nightwatch.*

## Detection Signals
NW-UPGRADE-XXX, Base44, Amanda, AVLM, nightwatch repo, great-horn-aml-nightwatch

## Fast close: Steps 2, 4, 5, 6
## Full close: All steps

**Step 1 — Chat sweep** (full only)
recent_chats(n=10) for Nightwatch context not in this session. State findings. SKIPPED if unavailable.

**Step 2 — Unsaved context sweep**
Scan conversation for: decisions not persisted, bugs not in open items, features not in roadmap,
prompts written but not run, merges done but state not updated.
Each item: state it + where routed. Unresolvable → handoff.

**Step 3 — Repo sync** (full only)
Repo: bitcoinbrainsweb/great-horn-aml-nightwatch
Write in this order — fetch SHA immediately before each write:
1. docs/NIGHTWATCH_STATE.md — overwrite with current working state (branch, next task, blockers, open items). No history, no config.
2. docs/NIGHTWATCH_LOG.md — APPEND one dated entry. Format: ## YYYY-MM-DD — [description]. Include: completed, decisions, blockers, files changed.
3. docs/Nightwatch_Roadmap_Detailed_v15.md — write new roadmap items if any.
4. Push stale: AVLM_PROJECT_CONTEXT.md, AVLM_INDEX.md, AMANDA_PROFILE.md if changed.

STATE rules:
- Contains: last completed, active branch, next task, active blockers, open items
- Does NOT contain: historical decisions, config, app IDs, agent roles, phase definitions

LOG rules:
- Append-only. Never overwrite. One entry per session.

**Step 4 — Promotion candidates** (full only)
Scan session for decisions/rules/patterns that should apply globally.
1. Read PROMOTION_LOG.md from brainframe-public — check for same-day edits
2. If no conflict: commit directly to brainframe-public main via GitHub API
3. Append: YYYY-MM-DD | nightwatch | [file] | [description]
4. If conflict: stop, flag to Dave

**Step 5 — Memory audit**
Fetch all memory edits. Fix stale, duplicated, missing. Report: N reviewed / N changed.

**Step 6 — Skills + instructions check** (full only)
Check nightwatch-prompts, roadmap-planner, nightwatch-upgrade-orchestrator, quitchat.
If updates needed: produce SKILL.md and present. Check project instructions for stale content.

**Step 7 — Handoff file**
Produce /mnt/user-data/outputs/SESSION_HANDOFF.md. Self-contained. Assume zero memory of session.
Include: session summary, last completed, next task, open decisions, first action next session.

## Audit Log Format
Tier: FAST / FULL — [signals]
Step 1: RAN / SKIPPED / [findings]
Step 2: [N found / N routed / N unresolved]
Step 3: STATE overwritten / LOG appended / Roadmap [N items] / others UNCHANGED
Step 4: [N promoted / NONE / CONFLICT — flagged]
Step 5: [N reviewed / N changed]
Step 6: [result]
Step 7: READY
