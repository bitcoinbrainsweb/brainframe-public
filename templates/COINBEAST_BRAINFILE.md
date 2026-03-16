# BRAINFILE — COINBEAST
Version: 2.0
Last updated: 2026-03-15

---

## PROJECT IDENTITY

Coinbeast is a Bitcoin-only product intelligence platform. It is a structured knowledge graph, not a blog or affiliate site. Pages are generated from structured data automatically. Being built by Dave Bradley with AI-assisted development.

Stack: Supabase + Next.js + Vercel + Algolia (product search) + Meilisearch (archive search) + Cursor + Make

---

## CORE RULES — NEVER BREAK THESE

1. Bitcoin only. No exceptions.
2. Product records contain verifiable facts only. Opinions live in Review objects.
3. Every claim must have a source.
4. Affiliate data never touches scoring logic.
5. Trust Score is versioned, explainable, and published.
6. Commercial relationships never affect editorial content or Trust Score.
7. V1 architecture must not make the tutorial factory or podcast archive harder to add later.

---

## GLOBAL FILES (fetch at session start)

Fetch these via raw GitHub URL at the start of every session:

- https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/GLOBAL_RULES.md
- https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/STYLE_RULES.md
- https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/MODEL_ROUTING.md

Refresh command: "refresh rules"
Auto-refresh: at 30 exchanges

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

Load at session start:
- MASTER.md

Load on demand:
- DECISIONS.md
- KNOWN_UNKNOWNS.md
- SESSION_LOG.md
- HEALTH_CHECK.md
- TAXONOMY.md
- PROMPT_LOG.md
- /specs/trust_score.md
- /specs/ai_pipeline.md
- /specs/tutorial_factory.md
- /specs/podcast_archive.md
- /specs/data_model.md
- /specs/b2b_revenue.md
- /specs/buy_bitcoin.md
- /specs/voice_profiles.md
- /archive/

---

## THIS SESSION CHANGED

Last session: 2026-03-15
Files modified: All files initialized — Brainframe v2 build
Key decisions: Stack confirmed, Brainframe v2 architecture finalized
Open items: Trust Score weights, first 50 products, Make setup, legal review on buy Bitcoin
