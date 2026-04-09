# FUTURE_INTEL.md
Brainframe | Dave Bradley | Created: 2026-04-08

A log of interesting signals flagged for future re-analysis.
When re-reading this file, compare each entry's `Context At Time` to current reality.
Flag any entry where the Revisit Trigger has been met or Status should change.

---

## Graph-Layer AI Memory (GraphRAG / Zep / PlugMem / Graphify) — 2026-04-08
Updated: 2026-04-08 — Concrete tool identified (graphify)

Source: Instagram/TikTok reel (engagement bait — "comment token") + follow-up reel (graphify demo)
Summary: Graph knowledge databases replace flat markdown memory files with node/edge structures. Instead of loading entire MD files into context, the agent retrieves only relevant knowledge units via graph traversal. Benchmarked at 71.5x fewer tokens per query vs raw file reads. Graphify (safishamsi/graphify) is a live, open-source Claude Code skill that does exactly this — ships as a pip package, outputs interactive HTML graph, GRAPH_REPORT.md, graph.json, and optional Obsidian vault. Two-pass extraction: deterministic AST for code, Claude subagents for docs/images. No vector DB required.
Why Interesting: Directly relevant to brainframe memory architecture. Current approach (ADMIN_STATE.md, DECISIONS.md, ADMIN_LOG.md) loads full files every session boot. Graphify could map brainframe-public as a knowledge graph — Claude navigates via GRAPH_REPORT.md instead of grepping raw files. Also relevant for Coinbeast knowledge graph architecture.
Revisit Trigger: When Nightwatch DECISIONS.md exceeds 1000 entries OR session boot token cost becomes a measurable pain point OR Coinbeast knowledge graph architecture is being designed.
Status: WATCHING
Tags: #memory #graph #graphrag #token-efficiency #brainframe-architecture #graphify #coinbeast #claude-code
Context At Time: Nightwatch early-stage, DECISIONS.md ~50 entries. Brainframe uses flat MD files on GitHub. No MCP graph server in stack. Session boot reads 5 files sequentially. Graphify released ~2026-04-07, open source, MIT, pip install graphifyy. Graph layer assessed as overkill at current brainframe volume — but test candidate against brainframe-public as low-risk proof of concept.
Key Tools To Re-Evaluate: graphify — pip install graphifyy && graphify install (github.com/safishamsi/graphify); claude-obsidian (AgriciDaniel) for persistent wiki layer; Zep (getzep.com); Graphiti. Install test: /graphify . inside brainframe-public clone.

---

---

## Paperclip Multi-Agent — Coinbeast Knowledge Graph Freshness — 2026-04-08

Source: TikTok reel (AI company simulation tool)
Summary: Paperclip (npx paperclipai onboard) spins up role-based AI agent teams that coordinate via heartbeat scheduling. 14.2K stars in first week. Agents wake on schedule, act, log decisions with full audit trail.
Why Interesting: Strong fit for Coinbeast's core problem — keeping a Bitcoin product knowledge graph fresh at scale without a human editorial team. Roles that map cleanly: product researcher (monitors new Bitcoin tools/releases), reviewer synthesizer (aggregates community sentiment into structured ratings), competitive analyst (tracks feature changes), content QA agent (checks for staleness/gaps). Heartbeat scheduling means knowledge graph stays current without manual triggering.
Revisit Trigger: When Coinbeast knowledge graph architecture is defined and data freshness workflow is being designed.
Status: WATCHING
Tags: #coinbeast #paperclip #multi-agent #knowledge-graph #bitcoin-intel #freshness
Context At Time: Coinbeast is pre-build, concept stage only. Stack/architecture undefined. Paperclip assessed as stronger fit than Bitcoin Rodeo marketing due to deeper product alignment. Recommend scoping to 4 focused agents max for initial test. Coordination failures at 50 agents noted as real risk.
Key Tools To Re-Evaluate: paperclipai (npx paperclipai onboard), Clipmart marketplace (coming), CrewAI as alternative orchestration layer.

---

## Paperclip Multi-Agent — Coinbeast Knowledge Graph Freshness — 2026-04-08

Source: TikTok reel (AI company simulation tool)
Summary: Paperclip (npx paperclipai onboard) spins up role-based AI agent teams that coordinate via heartbeat scheduling. 14.2K stars in first week. Agents wake on schedule, act, log decisions with full audit trail.
Why Interesting: Strong fit for Coinbeast's core problem — keeping a Bitcoin product knowledge graph fresh at scale without a human editorial team. Four roles map cleanly: product researcher (monitors new Bitcoin tools/releases), reviewer synthesizer (aggregates community sentiment into structured ratings), competitive analyst (tracks feature changes), content QA agent (checks for staleness/gaps). Heartbeat scheduling = knowledge graph stays current without manual triggering.
Revisit Trigger: When Coinbeast knowledge graph architecture is defined and data freshness workflow is being designed.
Status: WATCHING
Tags: #coinbeast #paperclip #multi-agent #knowledge-graph #bitcoin-intel #freshness
Context At Time: Coinbeast is concept stage only — no stack or architecture defined. Paperclip assessed as stronger fit than Bitcoin Rodeo due to deeper product alignment. Coordination failures at 50 agents noted as real risk — recommend scoping to 4 focused agents max for initial test.
Key Tools To Re-Evaluate: paperclipai (npx paperclipai onboard), Clipmart marketplace (coming), CrewAI as alternative orchestration layer.

---

## SIGNAL: Claude Code CMO Skill Stack
**Date:** 2026-04-08
**Source:** Instagram Reel (Type A — Engagement Bait)
**Signal Rating:** Medium-High

### What Was Flagged
A 5-skill Claude Code stack positioned as a "vibe marketing" CMO setup:
1. Design skill — landing pages + conversion
2. Remotion — programmatic video/carousel/print generation
3. Meta Ads skill — full campaign creation via Meta API (campaign → ad set → landing page → UTMs)
4. Google Ads skill — keyword research + campaign build + launch via Google Ads API
5. Ads Analyst — extract + analyze ad data, provide improvement recommendations

### Why It Matters
The underlying tech is real. Meta API + Google Ads API + Claude is a legitimate automation stack.
Remotion (programmatic React video) is the novel inclusion — worth evaluating for Bitcoin Rodeo
and Bitcoin Brains content pipelines (event promos, carousel generation).

### Re-evaluate When
- Building a marketing automation layer for Bitcoin Brains or Bitcoin Rodeo
- Evaluating Remotion for templated video/carousel content
- Standing up any paid ads workflow that could benefit from Claude-driven campaign management

### Next Action (if pursued)
Build the 5 SKILL.md files; wire Meta + Google Ads APIs; evaluate Remotion for carousel output.

## Claude Code Marketing Skills (coreyhaines31/marketingskills) — 2026-04-08

Source: Instagram/TikTok reel (Type B — Straight Info)
Summary: Real GitHub library with 32 marketing skills across 7 pods: SEO, CRO, Content/Copy, Paid/Measurement, Growth/Retention, Sales/GTM, Strategy. Works with Claude Code, Cursor, Codex, Windsurf. The "7 AI employees" framing is just the 7 existing pods renamed. Solid, low-hype tool.
Why Interesting: Could bootstrap marketing execution for Coinbeast, Bitcoin Brains, or Bitcoin Rodeo without hiring. Cursor-compatible — fits existing dev workflow.
Revisit Trigger: When building a marketing automation layer for any Dave property OR when Coinbeast content pipeline design begins.
Status: WATCHING
Tags: #marketing #claude-code #skills #coinbeast #bitcoin-brains #bitcoin-rodeo #cursor-compatible
Context At Time: No active marketing automation in any project. Coinbeast pre-build/concept stage. Bitcoin Rodeo next event planning underway. All dev work in Cursor. Library confirmed real and active (32 skills, 52 CLI tools, cross-agent spec).
Key Tools To Re-Evaluate: github.com/coreyhaines31/marketingskills, alirezarezvani/claude-skills (220+ broader library), OpenClaudia/openclaudia-skills (62+ skills).

---

---

## FUTURE_INTEL — 2026-04-08
Title: Persistent Roadmap Agent
Tags: #nightwatch #axiom #mambamode #brainframe #roadmap #agents
Source: Admin DAI session — agentic design patterns discussion

Idea: A persistent agent whose sole job is roadmap integrity across all projects. Watches for new upgrade IDs being sequenced, checks dependency conflicts with existing roadmap items, flags sequencing violations before they land. Per-project or global (brainframe-public). Authority TBD — flag-only vs block promotion. Trigger TBD — every DECISIONS.md write, every new upgrade ID, or manual call. Needs proper brainstorm session before building — risk of fighting existing promotion workflow.

Re-evaluate when: roadmap conflicts become a recurring pain point, or when promotion workflow is next touched.

## Claude Code SEO Skill (AgriciDaniel/claude-seo + geo-seo-claude fork) — 2026-04-08

Source: Instagram/TikTok reel (Type B — Straight Info)
Summary: Claude Code skills for full-stack SEO — 13 subskills, 6 subagents, technical SEO, on-page, local, schema, GEO/AEO, and llms.txt generation. Two repos: AgriciDaniel/claude-seo (general SEO) and zubair-trabzada/geo-seo-claude (GEO/AI search-first). Free core; DataForSEO/Ahrefs MCP for live data costs money.
Why Interesting: llms.txt generation is already flagged as pending across Bitcoin Brains, Bitcoin Rodeo, Liberty Labs, and Nightwatch. GEO/AEO angle matters specifically for Bitcoin content where AI search (ChatGPT, Perplexity, Google AI Overviews) is eating organic traffic. Could run as a Claude Code session — no extra infra.
Revisit Trigger: When llms.txt deployment is next touched, or when any Bitcoin Brains/Rodeo/Nightwatch marketing session prioritizes SEO/AI search visibility.
Status: WATCHING
Tags: #seo #geo #aeo #llms-txt #bitcoin-brains #bitcoin-rodeo #liberty-labs #nightwatch #claude-code
Context At Time: llms.txt templates drafted (llms-txt-note.md, 2026-04-08) but not deployed on any site. No active SEO tooling on any property. Claude Code skill ecosystem maturing fast — this skill is real and functional, not vaporware.
Key Tools To Re-Evaluate: github.com/AgriciDaniel/claude-seo, github.com/zubair-trabzada/geo-seo-claude, DataForSEO MCP (live SERP data).

---
## AI-Generated Code Security Blind Spots — 2026-04-08

Source: Instagram Reel (https://www.instagram.com/reel/DW2HcxOj_9F/)
Summary: Three critical security issues AI-generated code consistently misses: missing rate limiting on API endpoints, Supabase RLS off by default allowing cross-user data access, and insecure direct object references (IDOR) letting authenticated users access other users' resources by changing IDs in routes.
Why Interesting: All three are real, production-breaking, and invisible during happy-path testing. Directly applicable to Nightwatch (compliance data, FINTRAC records — catastrophic if leaked) and Coinbeast (knowledge graph with user/contributor data).
Revisit Trigger: Before any Nightwatch or Coinbeast feature that touches auth, user-scoped data, or external API endpoints — use as a pre-build security checklist.
Status: WATCHING
Tags: #security #nightwatch #coinbeast #cursor-prompts #aml #rls #rate-limiting #idor
Context At Time: Nightwatch is pre-launch, building auth and role enforcement. Coinbeast stack/auth status unknown. transcript-service just shipped with rate limiting (slowapi) — confirmed working. security-hardening skill exists at /mnt/skills/user/security-hardening/SKILL.md.
Key Tools To Re-Evaluate: security-hardening skill, Supabase RLS docs, slowapi, OWASP IDOR checklist

---
## Gemini CLI — Large Context Ingestion for Nightwatch + Coinbeast — 2026-04-08

Source: Admin DAI session — AI Pulse + Gemini CLI setup discussion
Summary: Gemini CLI (free tier, personal Google account, 1M token context, 1000 req/day) is a lightweight terminal agent suited for bulk data ingestion and large-context extraction tasks. Best fit: pre-session repo scans, bulk PDF/doc extraction, competitor site freshness checks. Not a Cursor replacement — a cheap upstream layer for token-heavy grunt work before Claude/Cursor takes over.
Why Interesting: Nightwatch deals with large FINTRAC guidance docs and growing repo surface area. Coinbeast knowledge graph will require ongoing freshness checks across many sources. Both hit the 'large context ingestion' use case where Gemini CLI's 1M token window and near-zero cost create real ROI.
Revisit Trigger: When Nightwatch pre-session repo scan becomes a recurring friction point OR when Coinbeast knowledge graph freshness workflow is being designed.
Status: WATCHING
Tags: #gemini-cli #nightwatch #coinbeast #large-context #data-curation #knowledge-graph #free-tier
Context At Time: Gemini CLI confirmed free on personal Google account (60 req/min, 1000/day, Gemini 2.5 Pro). Dave has personal Gmail for auth. Workspace account not eligible for free tier. CLI not yet installed. Coinbeast pre-build/concept stage. Nightwatch pre-launch. Workflow pattern identified: Gemini CLI (bulk ingest) → output.md → Claude (planning/critique) → Cursor (build). Claude Managed Agents also just announced (public beta) — potential future overlap for long-running agent tasks.
Key Tools To Re-Evaluate: google-gemini/gemini-cli (github), aistudio.google.com (API key), Firecrawl (scrape-to-markdown for competitor site freshness), Claude Managed Agents (platform.claude.com/docs/en/managed-agents/overview).

---
## Codebase MCP / Knowledge Graph Tools — 2026-04-08

Source: Instagram reel + research session (codebase-mcp-research.md)
Summary: A new category of MCP servers that index codebases into persistent knowledge graphs — enabling AI agents (Cursor, Claude Code) to query structure semantically instead of reading files one by one. Key tools: codebase-memory-mcp (DeusData), claude-context (Zilliz), GitNexus, code-review-graph. Token reduction claims range from 40% to 99%. Space is moving extremely fast — multiple new repos appeared within days of each other.
Why Interesting: Could significantly improve Cursor's architectural understanding on Nightwatch and Axiom — reducing hallucinated edits and missed dependencies. But tooling is immature and Windows support is inconsistent.
Revisit Trigger: After 2026-04-13 (Monday) — re-evaluate which tools have stabilized, gained community validation, and confirmed Windows + Cursor compatibility before any install decision.
Status: WATCHING
Tags: #mcp #codebase-graph #cursor #nightwatch #axiom #token-reduction #tooling
Context At Time: Nightwatch pre-launch, Axiom active build. Primary dev env is Windows + Cursor. codebase-memory-mcp has no Windows support (WSL2 only). claude-context requires Zilliz Cloud + OpenAI key (cost). GitNexus and code-review-graph are zero-dep but brand new. Research file saved at codebase-mcp-research.md (outputs).
Key Tools To Re-Evaluate: github.com/DeusData/codebase-memory-mcp, github.com/zilliztech/claude-context, github.com/jlicerio/gitnexus, github.com/tirth8205/code-review-graph, github.com/colbymchenry/codegraph

---## Leaked AI System Prompts Repos — 2026-04-09

Source: Instagram reel / GitHub discovery
Summary: Multiple public GitHub repos contain extracted system prompts and tool schemas for 28+ AI tools including Cursor, Lovable, Perplexity, v0, Devin, Windsurf, and Replit. The most comprehensive repo (x1xhlol/system-prompts-and-models-of-ai-tools) has 489 commits across 28 contributors, actively updated as of March 2026, and includes JSON tool schemas — not just prompt text.
Why Interesting: Direct competitive intel on how leading AI coding tools structure their agent prompts and tool permissions. Relevant for Nightwatch agent prompt architecture and Coinbeast knowledge graph agent design.
Revisit Trigger: When writing any new agent system prompt for Nightwatch or Coinbeast, or when evaluating a new AI tool competitor.
Status: WATCHING
Tags: #prompts #agents #competitive-intel #nightwatch #coinbeast
Context At Time: Nightwatch AML SaaS in active Cursor development. Coinbeast knowledge graph in early design. No agent system prompts written yet for either. Brainframe on v2.1.
Key Tools To Re-Evaluate: github.com/x1xhlol/system-prompts-and-models-of-ai-tools, github.com/elder-plinius/CL4R1T4S, github.com/asgeirtj/system_prompts_leaks

---## Personalized Cold Outreach Landing Page Tools — 2026-04-09

Source: Instagram reel analysis
Summary: A category of tools generates unique per-prospect landing pages from cold email URLs, dynamically rendering name, company, industry, and competitor intel per visitor. GenPage is the leading purpose-built tool; Personyze and Instapage/Unbounce offer broader platform approaches. Documented results include 3x meeting bookings and 22-28% reply rates.
Why Interesting: Coinbeast will need a go-to-market and outreach strategy when it launches. Personalized landing pages are a proven B2B conversion lever for cold outreach to Bitcoin product companies, exchanges, and hardware vendors.
Revisit Trigger: When Coinbeast reaches GTM/outreach planning phase, or when planning any Bitcoin Rodeo sponsor outreach campaign.
Status: WATCHING
Tags: #coinbeast #gtm #cold-outreach #landing-pages #bitcoin-rodeo
Context At Time: Coinbeast in early design/knowledge graph architecture phase. No GTM planning underway. Bitcoin Rodeo 2026 planning ongoing. No cold outreach tooling in stack.
Key Tools To Re-Evaluate: genpage.ai, personyze.com, instapage.com, unbounce.com

---## Higgsfield AI — Cinematic Video for Coinbeast Tutorials — 2026-04-09

Source: Conversation / Instagram reel analysis
Summary: Higgsfield is an AI cinematic video platform with consistent character locking across shots — same on-screen presenter across multiple videos without a human. Differentiator vs Midjourney (image-only) and ChatGPT (no video): character continuity across scenes. Closest competitors are Runway and Kling but Higgsfield is optimized for storytelling continuity. Open-source alternative: github.com/Anil-matcha/Open-Higgsfield-AI (MIT, self-hosted).
Why Interesting: Coinbeast will need product tutorial videos and explainer content walking users through Bitcoin tools. A consistent AI narrator/character across the series removes the need for a human presenter and enables scalable content production.
Revisit Trigger: When Coinbeast reaches content/marketing phase, or when first tutorial video is planned.
Status: WATCHING
Tags: #coinbeast #video #tutorials #content-marketing #ai-video
Context At Time: Coinbeast in early knowledge graph design. No content production underway. No video tooling in stack.
Key Tools To Re-Evaluate: higgsfield.ai, github.com/Anil-matcha/Open-Higgsfield-AI, runwayml.com, kling.ai

---## Fundraising Deck Visitor Tracking — Bitcoin Brains — 2026-04-09

Source: Conversation / research
Summary: Person-level identity resolution pixels (RB2B, Leadpipe, Identity Matrix) are US-only — Canadian traffic only resolves to company-level (name, industry, pages viewed). For targeted fundraising outreach to known Canadian funders, passive pixel tracking is the wrong tool. Better approach: unique URL per funder (yoursite.com/deck/investor-name) or email open/click tracking (Mailtrack, HubSpot) which gives full identity because you sent it to known people. Company-level tools (Dealfront, Leadfeeder, Clearbit) work globally for anonymous traffic but won't name individuals.
Why Interesting: Bitcoin Brains active fundraising raise. Web-based deck already in use. Need to know which funders are engaging, re-reading, and forwarding the deck.
Revisit Trigger: Before next round of funder outreach emails — implement unique URLs and email tracking at send time.
Status: WATCHING
Tags: #bitcoin-brains #fundraising #deck-tracking #investor-outreach
Context At Time: Bitcoin Brains raise active. Web-based deck in use (not Docsend). Funders primarily Canadian. No tracking currently in place.
Key Tools To Re-Evaluate: Mailtrack (email open/click tracking), HubSpot free tier (email tracking), Dealfront (company-level Canadian/global), unique URL per funder as zero-cost alternative

---

