# Axiom Health — Check Reference
*Fetched by axiom-health skill before running checks.*
*Contains full check procedures, auto-fix rules, and JAI handoff format.*

## CHECK 1 — REPO STRUCTURE SCAN

GitHub API base: https://api.github.com/repos/bitcoinbrainsweb/axiom

Expected files (flag if missing or empty):
- _docs/AGENT_HANDOFF.md
- _docs/JAI_HANDOFF.md
- _docs/AGENT_TASKS.md
- _docs/build-log.md
- _docs/axiom-roadmap.md
- _docs/KNOWN_UNKNOWNS.md

Expected structure (flag if absent):
- Pattern library directory
- Design system file
- Segment queue file

Flag: any file over 500 lines that should be lean (state files, handoffs)
Flag: any placeholder content ("[TBD]", "[PLACEHOLDER]") in active files
Auto-fix: update file timestamps where content is valid but metadata is stale

---

## CHECK 2 — STATE FILE CONSISTENCY

Fetch _docs/AGENT_HANDOFF.md and _docs/JAI_HANDOFF.md.

Cross-check:
- Last completed item in AGENT_HANDOFF matches build-log.md most recent entry
- Next priorities in both files are consistent
- No contradictory decisions between the two handoffs
- Active branch (if any) mentioned in both files

Flag: any contradiction between DAI and JAI handoffs
Flag: handoff last updated more than 7 days ago
Auto-fix: update "Last Updated" date if content is current

---

## CHECK 3 — PATTERN LIBRARY INTEGRITY

Fetch all pattern files.

Check each pattern for:
- Required fields: name, problem, solution, when_to_use, when_not_to_use
- Status field present: CONFIRMED | PROVISIONAL | DEPRECATED
- No PROVISIONAL patterns older than 14 days without a decision
- No duplicate patterns (same problem, different solutions)

Flag: missing required fields
Flag: PROVISIONAL pattern older than 14 days
Flag: apparent duplicates (similar names or problem statements)
Auto-fix: standardize field names if minor formatting variation only

---

## CHECK 4 — DAI→JAI HANDOFF AUDIT

Fetch _docs/AGENT_HANDOFF.md.

Verify structure:
- Session Summary section present and dated
- Urgent Items section (empty is OK, section must exist)
- What Was Built section
- Decisions Made section
- Blockers Removed section
- Open Questions for JAI section
- Next DAI Priorities section
- Rules Version field

Flag: any missing section
Flag: Open Questions for JAI contains items older than 2 sessions without response
Auto-fix: add missing sections with placeholder content if structure is otherwise valid

---

## CHECK 5 — JAI→DAI HANDOFF AUDIT

Fetch _docs/JAI_HANDOFF.md.

Verify:
- Design decisions documented with rationale
- Component library status current
- Any blocking design questions for DAI are flagged
- Last updated date matches recent session activity

Flag: design decisions without rationale
Flag: blocking questions for DAI older than 7 days
Flag: file not updated in 14+ days despite active development

---

## CHECK 6 — OPEN DECISIONS AUDIT

Fetch _docs/KNOWN_UNKNOWNS.md.

For each open decision:
- Note age (days since added)
- Check if it has been implicitly resolved in recent build-log entries
- Flag if it is blocking a queued upgrade

Flag: open decision older than 21 days with no progress
Flag: open decision blocking a queued upgrade
Auto-fix: mark as RESOLVED if resolution found in build-log

---

## CHECK 7 — CONTRACT DRIFT CHECK

Compare current pattern library against build-log entries from last 7 days.

Flag: any pattern marked CONFIRMED but recent code changes contradict it
Flag: any new code pattern appearing in 2+ recent entries that has no corresponding pattern library entry

This check is heuristic — flag for Dave's review, do not auto-fix.

---

## CHECK 8 — UNMERGED BRANCHES CHECK

Fetch all branches via GitHub API.

Flag: any branch older than 14 days not merged to main
Flag: any branch with a build-log entry showing FAIL not yet addressed
Auto-fix: none — unmerged branches require Dave decision

---

## CHECK 9 — AUTO-FIX PASS

After all checks, apply auto-fixes for:
- Stale timestamps (update to today's date where content is valid)
- Missing section headers (add with placeholder content)
- Minor formatting inconsistencies in pattern files

For each auto-fix:
1. Fetch SHA from GitHub API
2. Apply fix to content
3. PUT updated file via GitHub API
4. Report: "Auto-fixed: [file] — [what changed]"

Never auto-fix: decisions, priorities, design choices, content that requires judgment.

---

## AUTO-FIX RULES — JAI_HANDOFF UPDATE

When updating JAI_HANDOFF.md, use this exact structure:

```markdown
# JAI_HANDOFF.md

## Agent Naming
DAI = Dave's AI (Claude) | JAI = Johnny's AI

## Session Summary
[Date and brief description of last DAI session]

## Urgent Items
[Empty if none — section must exist]

## What Was Built
[List of completed items]

## Decisions Made
[List with rationale]

## Blockers Removed
[List]

## Open Questions for DAI
[List — empty if none]

## Next JAI Priorities
[List]

## Rules Version
[Current rules version]
```

---

## RATING DEFINITIONS

| Rating | Meaning |
|--------|---------|
| GREEN | All checks passed, no flags |
| AMBER | Warnings present, no critical flags |
| RED | Critical flags present — resolve before next session |

Overall rating = worst rating across all checks.

---

## COMMON MISTAKES — NEVER DO

- Reporting a file as updated unless GitHub API PUT returned success
- Auto-fixing decisions or priority ordering without flagging to Dave
- Skipping a check without logging the reason
- Using stale in-memory state — always re-fetch before each check
- Marking PROVISIONAL patterns as CONFIRMED without Dave approval
