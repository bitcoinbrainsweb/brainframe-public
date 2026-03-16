# ENTRY_SCHEMAS.md
Brainframe v2.0
Schema version: 1.0
Load on demand. Reference when creating entries in decisions, anti-patterns, or known unknowns.

---

## SCHEMA VERSION RULE

When the schema changes, old entries are not forcibly migrated.
Each entry includes the schema version it was created under.
Old and new entries coexist cleanly.

---

## DECISION ENTRY

Use for: DECISIONS.md

```
### [ID] — [Title]
Schema: 1.0
What: [The decision]
Why: [The reasoning]
How to apply: [How this should influence behavior]
Status: CONFIRMED / PROVISIONAL / SUPERSEDED
Superseded by: [ID of replacement, if applicable]
Review by: [Date or trigger condition]
Date: YYYY-MM-DD
Source: [Session, person, or AI that produced this]
```

**Status definitions:**
- CONFIRMED — locked, decided, verified. Do not re-litigate without new information.
- PROVISIONAL — working assumption. Must be revisited before influencing downstream decisions.
- SUPERSEDED — replaced. Points to the replacement entry. Never deleted.

---

## ANTI-PATTERN ENTRY

Use for: ANTI_PATTERNS.md

```
### [ID] — [Title]
Schema: 1.0
What: [The failure mode or mistake]
Why: [Why it causes problems]
How to apply: [How to detect and prevent it]
Status: CONFIRMED / PROVISIONAL / SUPERSEDED
Superseded by: [ID of replacement, if applicable]
Date: YYYY-MM-DD
Source: [Session, person, or AI that produced this]
```

---

## KNOWN UNKNOWN ENTRY

Use for: KNOWN_UNKNOWNS.md

```
### [ID] — [Title]
Schema: 1.0
Question: [What is unknown or unresolved]
Why deferred: [Why this hasn't been decided yet]
Impact if wrong: [What breaks if the assumption is incorrect]
Owner: [Who needs to resolve this]
Target: [Date or milestone when this should be resolved]
Status: Open / Resolved / Dropped
Resolution: [How it was resolved, if applicable]
Date opened: YYYY-MM-DD
Date resolved: YYYY-MM-DD (if applicable)
```

---

## SESSION LOG ENTRY

Use for: SESSION_LOG.md

```
## Session [number]
Date: YYYY-MM-DD
AI used: [Claude / ChatGPT / Cursor / other]
Phase: [Current project phase]

Key decisions:
- [Decision summary → see DECISIONS.md ID if logged]

Files modified:
- [filename]

Open items carried forward:
- [item]

Unresolved questions:
- [question → see KNOWN_UNKNOWNS.md ID if logged]
```

---

## REMEMBER THIS PROTOCOL

When Dave says "remember this":
1. Identify the correct file for the entry type
2. Check for conflicts with existing entries
3. Apply the correct schema for that file type
4. Tag confidence: CONFIRMED / PROVISIONAL / ASSUMED
5. Save the entry
6. Confirm to Dave: "Saved to [filename] as [ID] — [confidence tag]"
7. Nothing else

---

## FORGET THIS PROTOCOL

When Dave says "forget this":
1. Locate the entry
2. Change status to SUPERSEDED
3. Add "Superseded by: [reason or replacement ID]"
4. Add date
5. Never delete the entry
6. Confirm to Dave: "[ID] marked SUPERSEDED"
