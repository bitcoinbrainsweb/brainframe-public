# Nightwatch Prompt Writing Config
*Project-specific reference for the prompt-writing skill.*
*Fetch when writing any Cursor prompt for Nightwatch.*

## Upgrade ID Format
NW-UPGRADE-XXX
Branch: git checkout -b NW-UPGRADE-XXX
Artifacts: docs/NW-UPGRADE-XXX-SANITYCHECK.md, docs/NW-UPGRADE-XXX-RESULT.md, docs/NW-UPGRADE-XXX-GATE.md

## Repo
https://github.com/bitcoinbrainsweb/great-horn-aml-nightwatch
State file: docs/NIGHTWATCH_STATE.md
Log file: docs/NIGHTWATCH_LOG.md (append-only)
Roadmap: docs/Nightwatch_Roadmap_Detailed_v15.md

## Tool Routing
| Goal | Tool |
|------|------|
| Create entity schema | Base44 MCP create_entity_schema — Claude does this, never Cursor |
| Verify entity schema | Base44 MCP list_entity_schemas |
| Edit app UI/code | edit_base44_app |
| Update entity records | Cursor one-shot script via Base44 SDK |
| Read/write repo files | GitHub API curl (bash_tool) — never web_fetch |
| Merge branch | GitHub API POST /merges |

## Tool Roles
- Claude: planning, prompt writing, GitHub API ops, entity creation via MCP, merging
- Cursor: all code implementation, writes SANITYCHECK/RESULT/GATE files
- Base44 MCP: creates/reads/verifies entities only — no update, no delete

## Repo Check Before Any Prompt
1. Fetch docs/NIGHTWATCH_STATE.md — confirm last_completed, active_branch, next_upgrade
2. If state stale or conflicts → reconcile before writing prompt

## GATE File — Required in Every Prompt
Cursor writes docs/NW-UPGRADE-XXX-GATE.md before finishing:
```
STATUS: PASS | FAIL
TESTS: passed | failed — [details]
FILES_CHANGED: [list]
FORBIDDEN_TOUCHED: none | [list]
READY_TO_MERGE: yes | no — [reason if no]
```
Claude reads GATE file before merging. Never merge without STATUS: PASS.

## Nightwatch Constraints (inject into every prompt)
- Amanda's work = Effectiveness Review. Never "audit."
- Role checks via src/lib/roleUtils.js only — never raw array checks
- No legacy module reuse
- No side systems — every feature connects to the canonical graph
- Help config required on every new page (HelpContext)

## State File Update (every prompt)
Cursor must update docs/NIGHTWATCH_STATE.md at end of every prompt.
Fetch SHA immediately before writing.

## SANITYCHECK Contract
Cursor produces docs/NW-UPGRADE-XXX-SANITYCHECK.md before any code:
- Branch check (hard stop if wrong)
- Files in scope
- Caller enumeration for shared modules
- Risk rating: LOW / MEDIUM / HIGH
- Blast radius assessment

## RESULT File Contract
Cursor produces docs/NW-UPGRADE-XXX-RESULT.md after git push:
- Status: PASS | PASS WITH NOTES | FAIL
- Files changed with line counts
- Verification checklist
- npm test confirmation
- Deviations from spec

## Merge Rules
- PASS → merge automatically via GitHub API
- PASS WITH NOTES → surface notes, ask Dave
- FAIL → do not merge

## PowerShell Rules
Use ; not &&. Semicolons only.

## Common Mistakes
- Writing prompt before Base44 entity confirmed live (list_entity_schemas first)
- Using web_fetch for GitHub API (use bash_tool curl)
- Merging without reading GATE file
- Skipping git pull --rebase at start
- Using && in PowerShell commands
- Forgetting to update NIGHTWATCH_STATE.md after merge
