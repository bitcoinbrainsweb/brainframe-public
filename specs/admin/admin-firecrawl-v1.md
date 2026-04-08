# Spec: Firecrawl Integration
Project: Admin
Version: v1
Status: ACTIVE
Upgrade ref: N/A (shared infrastructure skill)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Multiple projects need to scrape web content to clean markdown: Coinbeast for knowledge graph freshness, AI Pulse for source scraping, Admin for competitive intel. Without a shared integration spec, each project integrates Firecrawl independently and inconsistently — duplicating API key management, ignoring rate limits, and producing incompatible output formats.

## Users / Use Cases
- Coinbeast — product page freshness, competitor monitoring, knowledge graph updates
- AI Pulse — scraping sources that require JS rendering (SPAs, paywalled previews)
- Admin — ad-hoc competitive intel scrapes on demand

## Success Metrics
- Single shared Firecrawl API key — not duplicated per project
- All scrape output in clean markdown — no raw HTML reaching consumers
- Coinbeast batch scraping stays within rate limits without manual throttling
- AI Pulse can distinguish which of its 64+ sources require Firecrawl vs simple web_fetch

## Requirements
1. API key stored in `brainframe-comms/_docs/REGISTRY.md` under `FIRECRAWL_API_KEY` — not hardcoded in any project file
2. Output format: markdown (not raw HTML) — all consumers receive markdown
3. JS rendering: use Firecrawl for sources confirmed to require it; use web_fetch for static sources
4. Skill packaged at `brainframe-public/skills/firecrawl.skill` — load before any Firecrawl call
5. Coinbeast batch scraping: implement request queuing with delay between calls to respect rate limits
6. AI Pulse integration: maintain a flag per source in `ai-pulse-sources.md` indicating `requires_js: true/false`
7. Error handling: on Firecrawl failure, fall back to web_fetch with a warning surfaced to Dave
8. Never store scraped content in brainframe-public — route to consuming project repo or return inline

## Non-Goals
- Replacing web_fetch for static pages (use Firecrawl only where JS rendering is needed)
- Storing scraped content long-term (Firecrawl is fetch-on-demand, not a cache)
- Crawling entire sites (page-level scraping only unless Dave explicitly requests crawl)

## Constraints / Assumptions
- Firecrawl is a managed external API (firecrawl.dev) — rate limits and pricing apply (ASSUMED: free tier limits unknown — OQ-001)
- Paperclip multi-agent: flagged as strong fit for Coinbeast knowledge graph freshness but not yet confirmed (OQ-002)
- Firecrawl skill: `brainframe-public/skills/firecrawl.skill` — treat as packaged, load before use

## Open Questions
| ID | Question | Owner |
|----|----------|-------|
| OQ-001 | What are the Firecrawl rate limits on current plan, and do they affect Coinbeast batch scraping feasibility? | Dave |
| OQ-002 | Is Paperclip multi-agent confirmed as the approach for Coinbeast knowledge graph freshness, or still evaluating? | Dave |
| OQ-003 | Which AI Pulse sources currently require JS rendering — has this been audited against the 64+ source list? | Admin |

## Dependencies
- `brainframe-public/skills/firecrawl.skill` — packaged skill (load before every Firecrawl call)
- `brainframe-comms/_docs/REGISTRY.md` — API key storage
- Coinbeast knowledge graph spec (not yet written — OQ-002 blocks)
- `brainframe-public/skills/ai-pulse-sources.md` — needs `requires_js` flag added per source

## Flows / Design Notes
Load firecrawl.skill → read API key from REGISTRY.md → call Firecrawl API with target URL → receive markdown → pass to consuming project. On failure → fall back to web_fetch → warn Dave. Never store scraped content in transit repos.

## Related Docs
- `brainframe-public/skills/firecrawl.skill`
- `brainframe-public/skills/ai-pulse-sources.md`
- Coinbeast knowledge graph spec (TBD)
