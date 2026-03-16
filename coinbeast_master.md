# MASTER — COINBEAST
Version: 1.1
Last updated: 2026-03-16
Status: Pre-build. Planning complete. Demo phase next.

---

## WHAT COINBEAST IS

Bitcoin-only product intelligence platform.
Knowledge graph architecture. Not a CMS. Not a blog.
Pages are generated from structured data automatically.

Strategic moats:
1. Product intelligence database — structured, sourced, versioned
2. Tutorial factory — automated, research-generating, B2B revenue
3. Podcast archive — irreproducible over time, compounds with every episode

---

## CURRENT PHASE

**Phase: Demo build**

Goal: Skip throwaway demo tools. Build real from day one using Cursor + Supabase.
Purpose: Prove the data model. Get something real to show people.
Approach: Minimal admin + seeded product records. Everything built is production-ready.
Timeline: This week.

---

## CONFIRMED STACK

| Layer | Tool | Cost |
|---|---|---|
| Database | Supabase | ~$25/month |
| Frontend | Next.js on Vercel | ~$20/month |
| Product search | Algolia | ~$50/month, evaluate over time |
| Archive search | Meilisearch (self-hosted) | Free |
| Editorial content | MDX in repo (V1) | Free |
| Transcription | Whisper | Free |
| Automation bridge | Make | ~$10/month |
| Implementation | Cursor | Subscription |
| Total | | ~$100-120/month |

---

## CURRENT PRIORITIES

1. Build real product from day one — Cursor + Supabase, minimal admin, seeded records
2. Trust Score weights — parked until after V1 launch
3. Define first 50 products for launch dataset (ChatGPT researching)
4. Make automation — parked until core build is underway
5. Legal review on buy Bitcoin integration — in hand, not a blocker

---

## OPEN ACTION ITEMS

- [ ] First 50 products defined (ChatGPT researching)
- [ ] Next 50 and next 100 products mapped
- [ ] Product attribute taxonomy finalized
- [ ] Trust Score weights validated (post-V1)
- [ ] Make workflow set up (parked)
- [ ] Legal review on buy Bitcoin integration (in hand)
- [ ] First batch of podcast creators identified for Dave approval

---

## ARCHITECTURE RULES

- Entity is the root object. Everything is an Entity.
- Product records: verifiable facts only
- Opinions live in Review objects only
- Every claim needs a source
- Affiliate data never touches scoring logic
- Trust Score is versioned — v1.0, v1.1 etc.
- Commercial layer never affects editorial content
- Build order: data model → admin → import → source layer → public pages → Trust Score

---

## TRUST SCORE — V1 WEIGHTS (PROVISIONAL)

| Category | Weight |
|---|---|
| Security | 30% |
| Privacy | 20% |
| Custody | 15% |
| Open Source | 15% |
| Bitcoin Alignment | 10% |
| Reputation | 10% |

*Marked provisional — weights to be validated against public data post-V1*

---

## V1 LAUNCH TARGETS

- 40–50 product pages
- 15–25 comparison pages (auto-generated)
- 8–12 best-of pages
- 6–8 topic hubs
- 10–15 guides
- Total: ~80–110 pages

---

## SPEC FILES

Load these on demand:

- specs/trust_score.md
- specs/ai_pipeline.md
- specs/tutorial_factory.md
- specs/podcast_archive.md
- specs/data_model.md
- specs/b2b_revenue.md
- specs/buy_bitcoin.md
- specs/company_dashboard.md
- specs/voice_profiles.md

---

## WHAT NOT TO BUILD IN V1

- Company dashboard commercial layer
- B2B subscription system
- Full podcast archive
- PGP signing, file uploads, graph visualization
- Lightning node channel health data
- Advanced contributor permissions beyond three tiers
