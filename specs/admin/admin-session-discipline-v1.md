# Spec: Session Discipline / Quitchat Workflow
Project: Admin
Version: v2
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
- Memory audit diff surfaces every change since last session
- Build log entry written every session
- PROMOTION_LOG.md always current — no un-logged promotions in either tier

## Requirements

### Trigger
1. Dave types "quitchat" — never infer from "wrap up", "new chat", or any other phrase

### Unsaved context criteria (Step 2)
2. Unsaved context = any of:
   - Decision made this session (CONFIRMED or PROVISIONAL) with no corresponding DECISIONS.md entry
   - File written or modified this session with no PROMOTION_LOG entry
   - Open item surfaced this session not yet added to ADMIN_STATE.md

### FULL tier steps (default)
3. Check PROMOTION_LOG.md — flag any promotions from this session not yet logged
4. Sweep unsaved context per criteria above — surface list to Dave
5. Overwrite ADMIN_STATE.md with current state snapshot
6. Append session entry to ADMIN_LOG.md — never overwrite
7. Write build log entry to `docs/admin/build-log/YYYY-MM-DD.md` — append if same-day file exists, create if not
8. Memory audit — diff format: show only entries changed, added, or removed since last session. Full audit on Dave's request only.
9. Surface open items summary: all unresolved items this session + carried forward
10. Confirm close to Dave with one-line summary: "Session closed. [N] decisions written, [N] open items carried, memory [N changes]."

### Standard tier (Dave must explicitly request)
11. Standard tier runs steps 1, 3, 4, 5, 6, 9 only — skips build log and memory audit. PROMOTION_LOG check (step 3) is mandatory in both tiers.

### All writes
12. All GitHub API writes: fetch fresh SHA immediately before write — never use cached SHA

## Non-Goals
- Mid-session state saves
- Automated session close without Dave typing "quitchat"
- Cross-project open item merging

## Constraints / Assumptions
- ADMIN_STATE.md, ADMIN_LOG.md: `brainframe-public/docs/admin/`
- PROMOTION_LOG.md: `brainframe-public/PROMOTION_LOG.md`
- Build log: `brainframe-public/docs/admin/build-log/YYYY-MM-DD.md`
- FULL tier is default — Dave must say "standard quitchat" for abbreviated close
- PROMOTION_LOG check is mandatory in BOTH tiers — collision guard decision (2026-04-03) applies always

## Open Questions
| ID | Question | Resolution |
|----|----------|------------|
| OQ-001 | Memory audit: full vs diff | RESOLVED: diff by default, full on Dave's explicit request |
| OQ-002 | Build log: per-day vs per-session | RESOLVED: per-session, append to same-day file |

## Dependencies
- `brainframe-public/docs/admin/ADMIN_STATE.md`
- `brainframe-public/docs/admin/ADMIN_LOG.md`
- `brainframe-public/PROMOTION_LOG.md`
- `brainframe-comms/_decisions/DECISIONS.md`
- quitchat skill (`/mnt/skills/user/quitchat/SKILL.md`)

## Flows / Design Notes
Trigger → check PROMOTION_LOG → sweep unsaved context → overwrite ADMIN_STATE → append ADMIN_LOG → write build log → memory diff audit → surface open items → confirm close. Linear. All writes use fresh SHA.

## Related Docs
- `/mnt/skills/user/quitchat/SKILL.md`
- DECISIONS.md entry 2026-04-03: PROMOTION_LOG as collision guard (all sessions)
- DECISIONS.md entry 2026-04-03: three-layer state split
