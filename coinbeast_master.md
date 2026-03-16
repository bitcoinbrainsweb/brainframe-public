# MASTER — COINBEAST
Version: 1.0
Last updated: 2026-03-15
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

Goal: Auto-populated demo with 10–20 products scraped from the web.
Purpose: Prove the data model. Get something real to show people.
Tool: Base44 for demo only. Throwaway. Not the real build.
Timeline: This week.

Real build follows immediately after demo validation.

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

1. Build demo this week — auto-populate from web scraper
2. Resolve Trust Score weights using public data — this week
3. Define first 50 products for launch dataset
4. Set up Brainframe file system and Make automation
5. Legal review on buy Bitcoin integration

---

## OPEN ACTION ITEMS

- [ ] Trust Score weights — revisit using public data
- [ ] First 50 products defined
- [ ] Next 50 and next 100 products mapped
- [ ] Product attribute taxonomy finalized
- [ ] Make workflow set up for Brainframe automation
- [ ] Legal review on buy Bitcoin integration
- [ ] Confirm API availability with Bitcoin Well and Bull Bitcoin
- [ ] First batch of podcast creators identified for Dave approval
- [ ] Conflict of interest disclosures documented for Dave, Knut, Luke

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

*Marked provisional — weights to be validated against public data*

---

## V1 LAUNCH TARGETS

- 40–50 product pages
- 15–25 comparison pages (auto-generated)
- 8–12 best-of pages
- 6–8 topic hubs
- 10–15 guides
- Total: ~80–110 pages

---

## TEAM

- Dave Bradley — project lead, @BitcoinBrains
- Knut Svanholm — reviewer, Bitcoin Infinity Show
- Luke de Wolf — reviewer, Bitcoin Infinity Show
- One AI-native collaborator — TBD

Dave's disclosures: co-founder Bull Bitcoin, CRO Bitcoin Well — must appear on all relevant pages.

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
