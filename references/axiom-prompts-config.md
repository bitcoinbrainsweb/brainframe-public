# Axiom Prompt Writing Config
*Project-specific reference for the prompt-writing skill.*
*Fetch when writing any Cursor prompt for Axiom.*

## Upgrade ID Format
AX-UPGRADE-XXX
Branch: git checkout -b AX-UPGRADE-XXX
Artifacts: _docs/AX-UPGRADE-XXX-SANITYCHECK.md, _docs/AX-UPGRADE-XXX-RESULT.md

## Repo
https://github.com/bitcoinbrainsweb/axiom
State file: _docs/AXIOM_STATE.md
Roadmap: _docs/axiom-roadmap.md
Build log: _docs/build-log.md (append-only)

## Tool Roles
- Claude (DAI): planning, architecture, critique, prompt writing, GitHub API ops, merging
- Cursor: all code implementation, generates SANITYCHECK/RESULT
- Johnny (JAI): visual design only — works from separate Claude Project. Deliverable: design-system.md. Do not block or modify his work stream.
- Perplexity Pro: research pipeline (tool data extraction) — not a code tool
- ChatGPT: secondary review and validation only

## Pre-Prompt Checklist
Run via GitHub API before any prompt:
1. Previous branch merged? If unmerged PASS branch exists → merge first
2. New env vars required? Add before prompt runs — never let deploy fail on missing env var
3. package.json changes? Flag that package-lock.json must be committed in same commit
4. Conflict risk? Flag if upgrade touches files recent upgrades also touched
5. Pending agent tasks? Read _docs/AGENT_TASKS.md and _docs/AGENT_HANDOFF.md

## BEFORE STARTING (every prompt)
```powershell
git pull --rebase origin main ; git checkout -b AX-UPGRADE-XXX
```
Read before writing any code:
- _docs/build-log.md
- _docs/AXIOM_STATE.md

## BEFORE FINISHING (every prompt)
```powershell
git add -A ; git status ; git commit -m "AX-UPGRADE-XXX: [description]" ; git push origin AX-UPGRADE-XXX
```

## SANITYCHECK Contract
Cursor produces _docs/AX-UPGRADE-XXX-SANITYCHECK.md before any code:
- Branch check (PowerShell hard stop if wrong)
- Files in scope and verified to exist
- Risk rating: LOW / MEDIUM / HIGH + justification
- Rollback strategy (required for MEDIUM/HIGH)
- api-contract.md check: does this change any frontend-facing response field? If YES → update api-contract.md or BLOCK

## RESULT File Contract
Cursor produces _docs/AX-UPGRADE-XXX-RESULT.md after git push:
- Status: PASS | PASS WITH NOTES | FAIL
- Files changed
- Verification checklist
- Deviations from spec

## State File Update (mandatory every prompt)
Cursor updates BOTH:
1. _docs/AXIOM_STATE.md — what changed, updated pattern_count and tool_count
2. _docs/axiom-roadmap.md — track rows, API table, Next Build Priorities, date header

## Pattern Library Rules
- Never overwrite existing records — append or patch only
- AI classification: real execution AI / assistive AI / marketing label
- Every tool record: name, category, AI features, pricing, user complaints (2 with source), source URLs, verification metadata
- Flag JS-rendered pricing as "pricing_status: not extractable — verify in browser" — never estimate
- After any update: confirm record count incremented correctly in RESULT

## Scoring/Matching Engine Rules
- Engine queries pattern library only — never hardcoded tool data
- Intake data schema defined before engine logic
- Output maps to pattern cards, not raw JSON blobs
- Any schema change requires AXIOM_STATE.md update

## Merge Rules
- PASS → merge automatically via GitHub API
- PASS WITH NOTES → surface notes, ask Dave
- FAIL → do not merge, report failure type

## PowerShell Rules
Use ; not &&. Use Select-String not grep. Use Select-Object -First N not head.

## Prompt Delivery
All prompts delivered as downloadable file via present_files.
Filename: AX-UPGRADE-XXX.md
Never as copy blocks or prose in chat.

## UI Work Gate
If upgrade touches UI layer: SANITYCHECK must verify _docs/design-system.md exists and is populated.
If missing or empty — STOP. Report to Dave. Do not proceed with UI work.

## Common Mistakes
1. Upgrade directly on main
2. RESULT file before git steps complete
3. && in PowerShell — use ;
4. grep instead of Select-String
5. Skipping SANITYCHECK
6. Files outside stated scope
7. Asking Dave to do anything a tool can do
8. Not updating both AXIOM_STATE.md AND axiom-roadmap.md
9. Carrying deployment table forward — always rewrite fresh
10. Hardcoding tool data instead of querying pattern library
11. Overwriting pattern library records — append only
12. Estimating JS-rendered pricing
13. Proceeding with UI work if design-system.md missing
14. Delivering prompts as copy blocks — always present_files
15. Shipping upgrade that changes frontend-facing response field without updating api-contract.md
16. Omitting rollback strategy on MEDIUM or HIGH risk — SANITYCHECK hard stop
