# Mambamode Prompt Writing Config
*Project-specific reference for the prompt-writing skill.*
*Fetch when writing any Cursor prompt for Mambamode.*

## Upgrade ID Format
NE-UPGRADE-XXX
Branch: git checkout -b NE-UPGRADE-XXX
Artifacts: docs/NE-UPGRADE-XXX-SANITYCHECK.md, docs/NE-UPGRADE-XXX-RESULT.md

## Repo
https://github.com/bitcoinbrainsweb/mambamode
State file: docs/MAMBAMODE_STATE.md (create if missing)

## Stack
React + Vite + Tailwind + Claude API + the-odds-api.com + balldontlie.io

## Tool Roles
- Claude: planning, prompt writing, GitHub API ops, merging
- Cursor: all code implementation, writes SANITYCHECK/RESULT files

## BEFORE STARTING (every prompt)
```bash
git pull --rebase origin main
git checkout -b NE-UPGRADE-XXX
```

## BEFORE FINISHING (every prompt)
```bash
npm run build
git add -A ; git commit -m "NE-UPGRADE-XXX: [description]" ; git push origin NE-UPGRADE-XXX
```

## SANITYCHECK Contract
Cursor produces docs/NE-UPGRADE-XXX-SANITYCHECK.md before any code:
- Branch check (hard stop if wrong)
- Files in scope
- Risk rating: LOW / MEDIUM / HIGH
- Rollback strategy for MEDIUM/HIGH

## RESULT File Contract
Cursor produces docs/NE-UPGRADE-XXX-RESULT.md after git push:
- Status: PASS | PASS WITH NOTES | FAIL
- Files changed
- Build confirmation (npm run build passed)
- Deviations from spec

## State File Update (every prompt)
Cursor updates docs/MAMBAMODE_STATE.md at end of every prompt.
Fetch SHA immediately before writing.

## Merge Rules
- PASS → merge automatically via GitHub API
- PASS WITH NOTES → surface, ask Dave
- FAIL → do not merge

## No Project-Specific Rules Yet
Add rules here as patterns emerge during development.

