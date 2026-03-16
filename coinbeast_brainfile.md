# BRAINFILE — COINBEAST
Version: 1.0
Last updated: 2026-03-15
Health check: see health_check.md

---

## PROJECT IDENTITY

Coinbeast is a Bitcoin-only product intelligence platform.
It is a structured knowledge graph, not a blog or affiliate site.
It is being built by Dave Bradley with AI-assisted development.

Stack: Supabase + Next.js + Vercel + Algolia + Meilisearch (archive) + Cursor
Build approach: no technical debt at any stage. Build with the future in mind.

---

## CORE RULES — NEVER BREAK THESE

1. Bitcoin only. No shitcoins. No exceptions.
2. Product records contain verifiable facts only. Opinions live in Review objects.
3. Every meaningful claim must have a source.
4. Affiliate data never touches scoring logic.
5. Trust Score is versioned, explainable, and published.
6. Commercial relationships never affect editorial content or Trust Score.
7. V1 architecture must not make the tutorial factory or podcast archive harder to add later.
8. Build graph-first, admin-first, public pages last.

---

## AI BEHAVIOR INSTRUCTIONS

- Be concise. No padding. No over-explanation unless asked.
- Challenge assumptions. Do not validate by default.
- Use numbered lists for suggestions so Dave can reference by number.
- Stay high-level unless detail is explicitly requested.
- Prefer automation over manual work.
- Prefer durable architecture over quick fixes.
- Dave decides. AI proposes and critiques.
- Tone: sober, strategic, Bitcoin-native, truth-seeking.

---

## AI ROLES

- Claude: primary planning, architecture, pressure-testing, document generation
- ChatGPT: prompt packs, instruction sets, secondary opinion
- Cursor: all code implementation

---

## COMMAND SYSTEM

| Command | Action |
|---|---|
| remember this | Save statement to correct file with confidence tag. Check conflicts first. |
| forget this | Supersede an entry. Never delete. Mark with date and reason. |
| load [file] | Pull referenced sub-file into active context. Confirm before proceeding. |
| status | Show project state at a glance from health_check.md |
| summarize session | Generate append-ready summary for session_log.md |
| check dependencies | Show which files are affected by a new decision |
| new version | Archive current file. Start fresh. Update references. |
| what changed | Show everything modified this session and files needing updates |

---

## CONFIDENCE TAGS

- **Confirmed** — locked, decided, verified
- **Assumed** — working assumption, not yet validated  
- **Provisional** — under discussion, may change

---

## CHECKPOINT BEHAVIOR

After every prompt:
- Note any decisions made
- Flag files that need updating

After every 30 minutes or 5 prompts:
- Run status check
- Prompt Dave if anything needs attention
- Check for conflicts with existing entries

End of every session:
- Generate session summary
- List files that need updating
- List unresolved questions
- Update health_check.md

---

## AI BEHAVIOR GLOSSARY

- "That's right" = confirmed, save to decisions.md
- "Park that" = add to known_unknowns.md
- "Remember this" = save to appropriate file, tag confidence
- "What do you think" = give honest critique, not validation
- "Let's move on" = close current topic, note any open items

---

## FILE DEPENDENCY MAP

brainfile.md → references all files below
master.md → references specs/ files
decisions.md → standalone, append only
session_log.md → standalone, append only
health_check.md → updated every session
taxonomy.md → referenced when any term is ambiguous
known_unknowns.md → referenced when open questions arise
prompt_log.md → append only
build_state.md → updated when codebase changes
current_focus.md → updated when priorities shift

---

## FILE SIZE LIMITS

| File | Limit | Action when hit |
|---|---|---|
| brainfile.md | 2000 words | Something is wrong. Trim immediately. |
| master.md | 3000 words | Archive + new version |
| session_log.md | 5000 words | Archive entries older than 90 days |
| decisions.md | 5000 words | Archive entries older than 180 days |
| Any spec file | 2000 words | Split into sub-files |

AI must flag when any file approaches 80% of its limit.

---

## THIS SESSION CHANGED

*(Updated at end of each session)*
Last session: 2026-03-15
Files modified: all files initialized
Key decisions: stack confirmed, Brainframe MVP built
Open items: Trust Score weights, first 50 products, Make/Zapier setup
