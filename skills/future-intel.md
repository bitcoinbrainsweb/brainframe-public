---
name: future-intel
description: >-
  Flags interesting signals to FUTURE_INTEL.md in brainframe-public for later re-analysis.
  MUST be used when Dave says "flag this", "save this for later", or "add to future intel".
  Also triggers on "review future intel", "re-read future intel", or "what have we flagged".
---

# Future Intel Skill
Version: 1.0 | 2026-04-08

Manages FUTURE_INTEL.md — Dave's log of interesting signals flagged for future re-analysis.

---

## TRIGGER WORDS

| Trigger | Action |
|---------|--------|
| `flag this` | Append new entry to FUTURE_INTEL.md |
| `review future intel` | Fetch file, re-analyze all WATCHING entries |
| `what have we flagged` | Fetch file, list all entries with current Status |

---

## WRITE PROTOCOL (flag this)

1. Fetch current FUTURE_INTEL.md SHA from brainframe-public
2. Decode content
3. Append new entry using schema below
4. Re-encode and PUT with fresh SHA

### Entry Schema

```
## [TOPIC] — [DATE]

Source: [reel / article / conversation / tool discovery / etc.]
Summary: [2-3 sentences — what it is and why it matters]
Why Interesting: [what caught Dave's attention]
Revisit Trigger: [specific condition — time, event, or threshold]
Status: WATCHING
Tags: [#tag1 #tag2 #tag3]
Context At Time: [what was true when flagged — stack state, project stage, volume metrics, current constraints]
Key Tools To Re-Evaluate: [specific products/repos to check on revisit]
```

Rules:
- `Context At Time` is mandatory — it's what enables meaningful re-analysis later
- `Revisit Trigger` must be specific and testable — not "when relevant" 
- Never overwrite existing entries
- Append only — always below the last `---` separator
- End new entry with `---`

---

## RE-ANALYSIS PROTOCOL (review future intel)

Fetch FUTURE_INTEL.md. For each entry where Status = WATCHING:

1. Compare `Context At Time` to current reality
2. Check if `Revisit Trigger` condition has been met
3. Research `Key Tools To Re-Evaluate` — has anything changed? (search if needed)
4. Produce a verdict per entry:
   - **TRIGGERED** — revisit condition met, recommend action
   - **CLOSER** — not there yet but meaningfully closer than when flagged
   - **SUPERSEDED** — something else solved this, or it turned out not to matter
   - **STILL WATCHING** — no meaningful change

Report format:
```
## FUTURE INTEL REVIEW — [DATE]

[TOPIC] — Status: [verdict]
Then: [context at time of flagging]
Now: [what has changed]
Verdict: [1-2 sentences — act, wait, or close]
```

---

## FILE LOCATION

`bitcoinbrainsweb/brainframe-public` → `FUTURE_INTEL.md` (root)

Always fetch fresh SHA before writing. Never use cached SHA.
