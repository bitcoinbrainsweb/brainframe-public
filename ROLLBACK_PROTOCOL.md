# ROLLBACK PROTOCOL
Version: 1.0 | Created: 2026-04-03 (INFRA-04)
Formal recovery path for failed upgrades.

---

## UPGRADE LIFECYCLE STATES

| State | Meaning |
|---|---|
| IN PROGRESS | Branch exists, Cursor running |
| PASS | RESULT + GATE: GO — Claude merges |
| PASS WITH NOTES | Merged with flagged items — next upgrade addresses |
| FAIL | RESULT shows failures or GATE: NO-GO — do not merge |
| FAILED (merged) | Bad code reached main — rollback required |

---

## ROLLBACK TRIGGER

Rollback is required when:
- A FAILED upgrade was merged to main (shouldn't happen — GATE prevents this)
- A PASS upgrade causes a regression discovered post-merge
- Dave explicitly calls rollback

---

## ROLLBACK STEPS (Claude executes)

1. **Identify the bad commit SHA** — GitHub API: `GET /repos/.../commits?sha=main&per_page=10`
2. **Create revert branch** — `git revert [sha]` via Cursor prompt (Manual lane)
3. **Update STATE.md** — record rollback, set LAST COMPLETED to rollback upgrade ID
4. **Append LOG entry** — `## YYYY-MM-DD — ROLLBACK NW-XXX: [reason]`
5. **Update HANDOFF_CURSOR.md** — flag rollback, note what failed and why
6. **Report to Dave** — state what was reverted, what needs fixing, proposed next step

---

## ROLLBACK UPGRADE NAMING

Rollback upgrades use suffix `-ROLLBACK`: e.g. `NW-317-ROLLBACK`

---

## RELATED DOCS
- `docs/AGENT_REGISTRY.md` — escalation rules
- `docs/NIGHTWATCH_WORKFLOW.md` — upgrade lifecycle