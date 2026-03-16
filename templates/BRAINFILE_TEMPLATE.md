# BRAINFILE — [PROJECT NAME]
Version: 1.0
Last updated: YYYY-MM-DD

---

## PROJECT IDENTITY

[2-3 sentences maximum. What the project is, what it is not, who is building it.]

---

## CORE RULES — NEVER BREAK THESE

[5-7 project-specific non-negotiable rules. Not global rules — those live in GLOBAL_RULES.md.]

1.
2.
3.
4.
5.

---

## GLOBAL FILES (fetch at session start)

These files live in the public Brainframe repo and apply to all projects.
Fetch via raw URL at the start of every session.

- GLOBAL_RULES.md
- STYLE_RULES.md
- MODEL_ROUTING.md

Refresh command: "refresh rules" — reloads GLOBAL_RULES.md and STYLE_RULES.md immediately.
Auto-refresh: triggered automatically at 30 exchanges.

---

## COMMAND SYSTEM

| Command | Action |
|---|---|
| remember this | Save to correct file with schema and confidence tag. Check conflicts first. Confirm when done. |
| forget this | Mark entry SUPERSEDED. Never delete. Confirm when done. |
| load [file] | Pull referenced file into context. Confirm before proceeding. |
| status | Show HEALTH_CHECK.md summary |
| summarize session | Generate append-ready SESSION_LOG.md entry |
| check dependencies | Show files affected by a new decision |
| what changed | Show all modifications this session |
| new version | Archive current file. Start fresh. Update references. |
| refresh rules | Reload GLOBAL_RULES.md and STYLE_RULES.md immediately. Confirm when done. |

---

## FILE MAP

Always available (load at session start):
- MASTER.md — current project state

Load on demand:
- DECISIONS.md — locked decisions
- KNOWN_UNKNOWNS.md — open questions
- SESSION_LOG.md — session history
- HEALTH_CHECK.md — project status
- TAXONOMY.md — canonical definitions
- PROMPT_LOG.md — significant prompts
- /specs/[filename].md — detail files
- /archive/ — old versions

---

## THIS SESSION CHANGED

*(Updated at end of each session)*
Last session: YYYY-MM-DD
Files modified: [list]
Key decisions: [summary]
Open items: [list]
