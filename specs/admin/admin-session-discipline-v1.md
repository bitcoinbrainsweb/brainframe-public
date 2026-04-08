# Spec: Session Discipline / Quitchat Workflow
Project: Admin
Version: v1
Status: ACTIVE
Upgrade ref: N/A (operational protocol)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Admin session state is complex — three-layer state files, PROMOTION_LOG, DECISIONS.md bus, memory audit, build log, open items. Without a spec, the quitchat workflow drifts between sessions and open items get silently dropped. This spec is the authoritative contract for what "session close" means.

## Users / Use Cases
- Admin DAI — executes at every session close when Dave types "quitchat"
- Dave — receives a clean handoff summary with no dropped context

## Success Metrics
- Zero open items silently dropped across session boundaries
- ADMIN_STATE.md always reflects current reality when next session boots
- Memory audit catches stale or incorrect entries every session
- Build log entry written every session — no session ends without a log entry
- PROMOTION_LOG.md always current — no un-logged promotions

## Requirements
1. Trigger: Dave types "quitchat" — never infer from "wrap up", "new chat", or any other phrase
2. Sweep unsaved context: surface any decisions made this session not yet written to DECISIONS.md or state files
3. Check PROMOTION_LOG.md — flag any promotion candidates from this session not yet promoted
4. Overwrite ADMIN_STATE.md with current state snapshot (path: `brainframe-public/docs/admin/ADMIN_STATE.md`)
5. Append session entry to ADMIN_LOG.md — never overwrite (path: `brainframe-public/docs/admin/ADMIN_LOG.md`)
6. Write build log entry to `brainframe-public/docs/admin/build-log/YYYY-MM-DD.md` (create if not exists, append if exists)
7. Memory audit: review userMemories for stale, incorrect, or missing entries — surface diff to Dave
8. Surface open items summary: all unresolved items from this session + any carried forward
9. All GitHub API writes: fetch fresh SHA immediately before write — never use cached SHA
10. FULL tier quitchat (default): all 9 steps above. Standard tier: steps 1, 4, 5, 8 only — Dave must explicitly request standard tier

## Non-Goals
- Mid-session state saves (quitchat is end-of-session only)
- Automated session close without Dave typing "quitchat"
- Merging open items from other projects (admin session only)

## Constraints / Assumptions
- State files: `brainframe-public/docs/admin/ADMIN_STATE.md`, `ADMIN_LOG.md`, `ADMIN_CONFIG.md`
- PROMOTION_LOG.md: `brainframe-public/PROMOTION_LOG.md`
- Build log: `brainframe-public/docs/admin/build-log/YYYY-MM-DD.md`
- GitHub API write pattern: fetch SHA → decode → modify → re-encode → PUT (applies to all state file writes)
- FULL tier is the default — Dave must explicitly request standard tier if he wants abbreviated close

## Open Questions
| ID | Question | Owner |
|----|----------|-------|
| OQ-001 | Memory audit format: full audit every session or diff vs last session? | Dave |
| OQ-002 | Build log: one entry per calendar day (append if same day) or one entry per session? | Dave |

## Dependencies
- `brainframe-public/docs/admin/ADMIN_STATE.md` — overwritten each session
- `brainframe-public/docs/admin/ADMIN_LOG.md` — append-only
- `brainframe-public/PROMOTION_LOG.md` — checked and updated
- `brainframe-public/DECISIONS.md` — sweep for any unwritten decisions
- quitchat skill (`/mnt/skills/user/quitchat/SKILL.md`) — loads this spec's workflow

## Flows / Design Notes
Trigger → sweep unsaved context → check PROMOTION_LOG → overwrite ADMIN_STATE → append ADMIN_LOG → write build log → memory audit → surface open items → confirm close to Dave. Linear — no branching. All writes use fresh SHA.

## Related Docs
- `/mnt/skills/user/quitchat/SKILL.md`
- `brainframe-public/GLOBAL_RULES.md`
- `brainframe-public/docs/admin/ADMIN_STATE.md`
