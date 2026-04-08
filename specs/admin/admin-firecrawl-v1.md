# Spec: Firecrawl Integration
Project: Admin
Version: v2
Status: ACTIVE
Upgrade ref: N/A (shared infrastructure skill)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Multiple projects need to scrape web content to markdown: Coinbeast for knowledge graph freshness, AI Pulse for source scraping, Admin for competitive intel. Without a shared spec, each project integrates Firecrawl independently — duplicating key management, ignoring rate limits, producing incompatible output.

## Users / Use Cases
- Coinbeast — product page freshness, knowledge graph updates
- AI Pulse — scraping JS-rendered sources
- Admin — ad-hoc competitive intel

## Success Metrics
- Single shared Firecrawl API key — not duplicated per project
- All scrape output in clean markdown
- Coinbeast batch scraping respects rate limits (once OQ-001 resolved)
- AI Pulse sources have requires_js flags set for top 20 Critical/High sources

## Requirements
1. API key: `brainframe-comms/_docs/REGISTRY.md` under `FIRECRAWL_API_KEY` — not hardcoded anywhere
2. Output format: markdown — all consumers receive markdown, never raw HTML
3. JS rendering: use Firecrawl only for sources confirmed to need it; use web_fetch for static sources
4. Skill: load `brainframe-public/skills/firecrawl.skill` before every Firecrawl call
5. Batch scraping rate limiting: BLOCKED on OQ-001 (rate limits unknown) — implement queuing only after limits confirmed
6. AI Pulse integration: Admin DAI to audit top 20 Critical/High sources in ai-pulse-sources.md and set `requires_js: true/false` flag per source — target: next AI Pulse session
7. Error handling: on Firecrawl failure → log error with URL + timestamp to session context → fall back to web_fetch → surface warning to Dave inline (not deferred)
8. Output size limit: truncate scraped content at 50,000 characters before passing to consumer — log truncation
9. Never store scraped content in brainframe-public or brainframe-comms

## Non-Goals
- Replacing web_fetch for static pages
- Long-term content caching
- Full-site crawling (page-level only unless Dave explicitly says crawl)

## Constraints / Assumptions
- Firecrawl rate limits: unknown on current plan — OQ-001 must be resolved before batch implementation
- Paperclip multi-agent: not yet confirmed for Coinbeast (OQ-002)
- Dave's security posture: REGISTRY.md key access is acceptable — all DAIs can read it

## Open Questions
| ID | Question | Owner |
|----|----------|-------|
| OQ-001 | Firecrawl rate limits on current plan? | Dave — check firecrawl.dev dashboard |
| OQ-002 | Paperclip multi-agent confirmed for Coinbeast knowledge graph? | Dave |
| OQ-003 | requires_js audit: top 20 sources by next AI Pulse session | Admin DAI |

## Dependencies
- `brainframe-public/skills/firecrawl.skill`
- `brainframe-comms/_docs/REGISTRY.md` — API key
- `brainframe-public/skills/ai-pulse-sources.md` — needs requires_js flags
- Coinbeast knowledge graph spec (not yet written — unblocked when OQ-002 resolved)

## Flows / Design Notes
Load firecrawl.skill → read API key from REGISTRY.md → call Firecrawl API → receive markdown → truncate at 50k chars if needed → pass to consumer.
On failure: log error (URL + timestamp) → fall back to web_fetch → warn Dave inline.

## Related Docs
- `brainframe-public/skills/firecrawl.skill`
- `brainframe-public/skills/ai-pulse-sources.md`
