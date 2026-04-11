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

## MemPalace — Local Verbatim AI Memory (MCP) — 2026-04-10

Source: Instagram reel (Type B — Straight Info) + web research
Summary: MemPalace (github.com/milla-jovovich/mempalace) is a free, open-source local AI memory system. Stores all conversations verbatim in ChromaDB + SQLite. 170-token startup cost, 96.6% LongMemEval recall, 19 MCP tools, zero API cost. Key design: Obsidian = knowledge base (static docs), MemPalace = conversation memory (all sessions verbatim). Do not point both at same source.
Why Interesting: Directly parallels Brainframe memory architecture. Current approach (ADMIN_STATE.md, DECISIONS.md, session files) is the Obsidian layer. MemPalace could replace or augment userMemories for Cursor sessions — storing all Cursor conversation history and retrieving only what is needed per session. Solves the CLAUDE.md bloat problem. 34% retrieval improvement over flat vector search via palace structure (wings/rooms/halls). Supports importing Claude, ChatGPT, and Slack exports.
Revisit Trigger: When Claude Desktop MCP stdout bug is patched (tracks in GitHub issues at milla-jovovich/mempalace) OR when Cursor session context loss becomes a recurring friction point.
Status: WATCHING
Tags: #memory #mcp #cursor #brainframe-architecture #claude-desktop #vector-db #local-first
Context At Time: Brainframe v2.1. Memory handled via userMemories + session state files in GitHub. No MCP memory server in stack. Claude Code not in use (Cursor only). Known bug: MemPalace stdout corrupts JSON stream on Claude Desktop MCP launch as of 2026-04-09 — no issue with Claude Code CLI. Benchmark controversy noted (100% claim revised to 96.6% after community pushback — still best free tool). Co-created by Milla Jovovich + Ben Sigman. 23K+ GitHub stars in 48 hours.
Key Tools To Re-Evaluate: github.com/milla-jovovich/mempalace (pip install mempalace), mempalace.tech, check GitHub issues for stdout MCP fix status.

---

## Ruflo / Claude-Flow — Multi-Agent Orchestration for Claude Code — 2026-04-10

Source: Instagram reel (Type C — Mixed) + GitHub research
Summary: Ruflo (aka claude-flow, github.com/ruvnet/ruflo) is a multi-agent orchestration layer on top of Claude Code. 28.9K stars, 500K downloads, 100K MAU. Spawns hierarchical or mesh agent swarms (54+ specialized agents), shared HNSW-indexed memory, model cost routing. Install: npx ruflo@latest init. Architecture note: Ruflo is the ledger/coordinator — it does NOT execute code. Claude Code (or Codex) is the actual executor. The 75% cost savings claim is unverified but model routing is real.
Why Interesting: If Claude Managed Agents (waitlisted 2026-04-08) is approved, Ruflo and CMA overlap significantly — one may supersede the other. Ruflo is Claude Code-native and currently irrelevant since dev stack is Cursor-only. But directly relevant if Claude Code is ever adopted for Nightwatch agentic compliance scans or Coinbeast knowledge graph agent workflows.
Revisit Trigger: When Claude Managed Agents waitlist is approved OR when evaluating agentic workflows for Nightwatch or Coinbeast that would benefit from parallelized agent swarms.
Status: WATCHING
Tags: #ruflo #claude-flow #multi-agent #claude-code #nightwatch #coinbeast #agentic #orchestration #claude-managed-agents
Context At Time: Dev stack is Cursor-only — Claude Code not in use. Claude Managed Agents waitlisted 2026-04-08 (Outcomes + Multiagent Orchestration + Memory, TypeScript SDK). Nightwatch pre-launch, Coinbeast concept stage. Ruflo v3.5.x actively maintained, high bug velocity noted in changelog. Known past bugs: cleanup wiped entire .claude/ dir, multiple CLI commands crashed with require errors — both patched.
Key Tools To Re-Evaluate: github.com/ruvnet/ruflo (npx ruflo@latest init), Claude Managed Agents (platform.claude.com/docs/en/managed-agents/overview — check waitlist status), CrewAI and LangGraph as alternative orchestration layers.

---

## Model-Layer AML/Compliance Controls — 2026-04-10

Source: AI Pulse scan / Anthropic Claude Mythos + Project Glasswing announcement
Summary: Anthropic withheld Claude Mythos from public release due to offensive cybersecurity risk, deploying it only to select organizations via Project Glasswing. This is the first time a frontier lab explicitly gated a model by institutional access tier rather than subscription level. The implication: future frontier models may require operator-level attestation or regulatory standing before accessing certain capabilities — document analysis, entity screening, risk scoring are the exact use cases most likely to be gated first.
Why Interesting: Nightwatch sits directly in the target profile. AML/compliance SaaS processing regulated financial data via LLM API is the kind of operator category that could require pre-credentialing. Being unregistered when gating lands = forced downtime and scramble. Being pre-credentialed = competitive moat (smaller AML tools won't have the paper trail).
Revisit Trigger: When Anthropic announces any operator tier, capability gating, or API access verification program — OR when Nightwatch approaches first paying client onboarding (whichever comes first).
Status: WATCHING
Tags: #nightwatch #anthropic #model-layer #compliance #aml #api-access #operator-credentialing #regulatory #fintrac
Context At Time: Nightwatch pre-revenue, pre-client. Anthropic API access currently ungated beyond standard ToS. Claude Mythos restricted to ~12 orgs via Project Glasswing (Apr 7, 2026). OpenAI/Anthropic/Google now sharing threat intel via Frontier Model Forum. API access tightening expected across all three platforms following 24K fraudulent account purge. EU AI Act full obligations effective Aug 2, 2026 — high-risk AI systems (which may include AML tooling) will face additional requirements.
Key Tools To Re-Evaluate: Anthropic operator policy (anthropic.com/policies), Frontier Model Forum announcements, EU AI Act high-risk classification list, Nightwatch compliance narrative doc (does not yet exist — create before revisit trigger fires).

---

## Coinbeast GTM — Paid Press Release Syndication for AEO/LLM Visibility — 2026-04-10

Source: Instagram reel analysis (black hat AEO techniques)
Summary: Paid press release syndication via EIN Presswire, Business Wire, PRWeb places content on high-DA publications (Forbes, Yahoo Finance, Entrepreneur, Reuters-level). LLMs heavily weight these sources in citation and recommendation. Cost range: 50–,000 for wire distribution. This is a legitimate grey-hat AEO tactic — not fake reviews or spam, just paid distribution to authoritative domains that LLMs trust.
Why Interesting: Coinbeast needs LLM visibility at launch — when users ask ChatGPT or Perplexity "what's the best tool for X Bitcoin use case," Coinbeast needs to be in the answer set. Press release syndication on launch is a credible, scalable way to seed that. Bitcoin Rodeo could also benefit for event discovery via AI search.
Revisit Trigger: When Coinbeast GTM planning begins OR when Bitcoin Rodeo 2027 launch planning starts.
Status: WATCHING
Tags: #coinbeast #gtm #aeo #llm-visibility #press-release #bitcoin-rodeo #launch
Context At Time: Coinbeast is pre-build, knowledge graph in early design. No GTM plan exists. AEO (Answer Engine Optimization) is an emerging channel — LLMs are eating organic search traffic for product discovery queries. EIN Presswire (~9–99/release), Business Wire (50–,000+), PRWeb (~9–69) are the main distribution options. Reuters/Fortune editorial placement is far more expensive and relationship-driven.
Key Tools To Re-Evaluate: einpresswire.com, businesswire.com, prweb.com, globenewswire.com. Also evaluate: newswire.com for Bitcoin/crypto niche distribution.

---

## Black Hat AEO Techniques — Ethical White Hat Extractions — 2026-04-10

Source: Instagram reel (Type C — straight info + minor bait)
Summary: Reel covered 4 black hat AEO/LLM ranking techniques: (1) fake reviews on Trustpilot/Google/Glassdoor, (2) Reddit seeding/comment buying, (3) paid press release syndication, (4) parasite SEO on Medium/Substack. Dave wants to revisit these and extract ethical/white hat equivalents for Coinbeast and Bitcoin Brains properties.
Why Interesting: Each black hat technique has a legitimate structural analog. Fake reviews → genuine review acquisition program. Reddit seeding → authentic community participation + AMA strategy. Paid syndication → legitimate wire distribution. Parasite SEO → strategic guest posting and content syndication on high-DA platforms. Understanding the mechanism tells you the white hat lever to pull.
Revisit Trigger: When Coinbeast content/AEO strategy is being designed OR when Bitcoin Brains is planning a marketing push.
Status: WATCHING
Tags: #aeo #seo #coinbeast #bitcoin-brains #content-strategy #llm-visibility #white-hat
Context At Time: No active AEO strategy on any Dave property. LLMs (ChatGPT, Perplexity, Claude) are increasingly the first-touch for product discovery. White hat AEO is an emerging, under-competed channel. Coinbeast knowledge graph architecture is being designed — AEO strategy should be baked into launch plan, not retrofitted.
Key Tools To Re-Evaluate: Revisit full reel transcript. Also research: whitespark.ca (review acquisition), reddit.com/r/Bitcoin and /r/CryptoCurrency for authentic participation playbook, Medium Partner Program for legitimate parasite SEO, HARO/Connectively for earned press mentions.

---

## Nightwatch — Black Hat AEO Detection as AML Signal — 2026-04-10

Source: Admin DAI session — AEO black hat analysis
Summary: Online reputation manipulation (fake reviews, seeded Reddit, wire-only press, parasite SEO) maps to the shell operation credibility facade typology in AML. Nightwatch can run a cross-signal credibility audit at onboarding and periodically: (1) review anomaly detection via Trustpilot/Google APIs — volume spikes, clustering, low reviewer history; (2) Reddit mention analysis — new accounts, low karma, single-subreddit promotion; (3) press release vs editorial distinction — brandvoice/wire URLs vs earned editorial; (4) parasite SEO detection — Medium/Substack articles with no organic engagement linking to client domain. Positive flags don't auto-reject — they elevate to EDD tier and trigger source-of-funds scrutiny.
Why Interesting: Novel AML signal not yet in mainstream compliance tooling. A business with manufactured online credibility but no genuine editorial footprint is exhibiting the same pattern as a shell operation building a legitimacy facade. Nightwatch could be first-to-market on this detection layer.
Revisit Trigger: When Nightwatch compliance feature roadmap is next reviewed OR when Amanda is consulted on EDD trigger criteria.
Status: WATCHING
Tags: #nightwatch #aml #edd #aeo #credibility-detection #fintrac #onboarding #risk-signals
Context At Time: Nightwatch pre-launch, building onboarding and EDD flows. No credibility audit layer currently specced. FINTRAC guidance supports online presence as a risk indicator for MSB/VASP onboarding. Detection APIs exist for Trustpilot, Reddit, and press release vs editorial distinction is a parseable URL pattern problem.
Key Tools To Re-Evaluate: Trustpilot public review API, Reddit search API, Moz/Ahrefs for backlink origin classification, press release URL pattern library (businesswire.com, prnewswire.com, einpresswire.com domains).

---

## Human Media Layer — White Hat AEO Moat for Bitcoin Brains + Coinbeast — 2026-04-10

Source: Admin DAI session — strategic insight from black hat AEO analysis
Summary: The human media layer being built around Bitcoin Brains and Coinbeast (genuine community participation, real editorial coverage, authentic reviews, real Reddit presence, real YouTube/podcast appearances) is the structurally identical white hat version of every black hat AEO technique in the reel. As LLMs get better at detecting manufactured vs earned authority, this moat deepens over time. Black hat operators will get penalized; genuine media presence compounds. This is a durable competitive advantage that needs to be (1) maximized operationally and (2) explicitly sold in the deck as a defensible moat.
Why Interesting: Three simultaneous applications: (A) Coinbeast — genuine product reviews, real community discussion, earned press = LLM citation magnet at launch; (B) Bitcoin Brains — existing brand presence, real customer base, real reviews = foundation that black hat competitors cannot replicate authentically; (C) Bitcoin Brains fundraising deck — human media layer as a moat narrative directly addresses the AEO arms race and positions Bitcoin Brains as the brand that wins when AI search matures and filters out fake signals.
Revisit Trigger: When Coinbeast GTM strategy is being written OR when Bitcoin Brains investor deck is next revised OR when AEO strategy session is scheduled.
Status: WATCHING
Tags: #coinbeast #bitcoin-brains #aeo #deck #fundraising #moat #human-media #llm-visibility #white-hat
Context At Time: Bitcoin Brains fundraising raise active. Coinbeast pre-build. No formal AEO strategy documented for either property. Human media layer exists in concept but not yet operationalized or articulated as a competitive moat. LLMs penalizing manufactured signals is directional but not yet fully enforced — first-mover advantage for genuine presence is real and closing window.
Key To Articulate In Deck: The AEO arms race is real. Black hat operators are winning short-term via fake reviews, seeded Reddit, wire press releases. Bitcoin Brains has built a genuine human media layer — real community, real reviews, real editorial — that will compound as AI search matures and penalizes manufactured signals. This is not just a marketing asset; it is a defensible infrastructure moat.

---

## Transcript Service — Instagram Auth via Dummy Account — 2026-04-10

Source: Admin DAI session
Summary: Transcript service blocks ~20% of Instagram reels due to auth requirements. Fix: create a throwaway Instagram account, extract sessionid cookie, add to Render as INSTAGRAM_SESSION_ID env var, wire into yt-dlp call via TRANSCRIPT-BUILD-004. Dummy account will eventually get flagged — replace with new one in ~5 minutes when that happens. Do NOT use Dave real Instagram account.
Why Interesting: Video-intel skill fires on every Instagram reel URL. Auth failures break the workflow silently. Fix is low effort, high value.
Revisit Trigger: Next time an Instagram reel returns auth error and Dave has 5 minutes to create a dummy account.
Status: WATCHING
Tags: #transcript-service #instagram #video-intel #render #build-ticket
Context At Time: Transcript service live on Render. X/Twitter already uses session cookie pattern (auth_token + ct0 in REGISTRY.md). Instagram needs same pattern with sessionid cookie. Build ticket TRANSCRIPT-BUILD-004 not yet written. Requires: (1) Dave creates dummy Instagram account, (2) grabs sessionid from browser DevTools → Application → Cookies → instagram.com, (3) pastes here so it can be added to REGISTRY.md and Render env vars.
Key Tools To Re-Evaluate: Render dashboard env vars (INSTAGRAM_SESSION_ID), yt-dlp --cookies or --cookies-from-browser flag, transcript-service repo for implementation.

---
## Transcript Service: X Broadcast Support + Render Upgrade — 2026-04-10

Source: conversation / build session
Summary: X broadcast URLs (x.com/i/broadcasts/...) require yt-dlp + OpenAI Whisper to transcribe. The blocking constraint is Render free tier (30s request timeout) — a 40-min broadcast would never complete. Upgrading to Render Starter ($7/mo) + routing broadcasts through OpenAI Whisper (same as tweet video path, ~$0.24/40min) would unblock this.
Why Interesting: Broadcast transcription would extend reel-intel and video-intel skills to cover Bitcoin Twitter spaces and long-form live recordings.
Revisit Trigger: When there is another reason to upgrade Render to Starter, or when broadcast transcription becomes a regular use case.
Status: WATCHING
Tags: #transcript-service #render #whisper #broadcast #twitter
Context At Time: Transcript service on Render free tier. Tweet video transcription (TRANSCRIPT-BUILD-003/004) working via fxtwitter + OpenAI Whisper. Broadcast path code written (TRANSCRIPT-BUILD-005) but untested due to timeout constraint. faster_whisper used for non-X platforms.
Key Tools To Re-Evaluate: Render Starter plan pricing, transcript-service TRANSCRIPT-BUILD-005 branch, OpenAI Whisper API pricing.

---

## Google Stitch MCP + 21st.dev — UI Design-to-Code Pipeline for Cursor — 2026-04-10

Source: Instagram reel (Type B — Straight Info)
Summary: Google Stitch (stitch.withgoogle.com) generates high-fidelity UI designs from text prompts via Gemini. Exports a DESIGN.md file (full design system in AI-readable markdown) and connects to Cursor/Claude Code via stitch-mcp package. 21st.dev is an open-source shadcn/ui component registry — install any component with npx shadcn. Together: Stitch generates the layout and design system, 21st.dev provides polished components, Cursor implements. Setup is one command: npx @_davideast/stitch-mcp init.
Why Interesting: Directly applicable to Nightwatch and Axiom UI work in Cursor. Removes the design bottleneck without hiring a designer. DESIGN.md persists design system across sessions — Cursor stays on-brand without re-prompting specs every time. 21st.dev components are MIT licensed, free, production-ready.
Revisit Trigger: When next Nightwatch or Axiom UI screen is being built in Cursor — add stitch-mcp to Cursor MCP config and test against one screen before committing to the workflow.
Status: WATCHING
Tags: #cursor #nightwatch #axiom #ui #design #stitch #mcp #21stdev #frontend
Context At Time: All UI implementation in Cursor. No dedicated designer. Nightwatch and Axiom both have active UI build needs. Stitch MCP supports Cursor natively. 21st.dev is free, shadcn/ui based — matches existing Tailwind stack. Setup cost is ~15 minutes for first screen test.
Key Tools To Re-Evaluate: stitch.withgoogle.com, github.com/davideast/stitch-mcp (npx @_davideast/stitch-mcp init), 21st.dev (npx shadcn@latest add), google-labs-code/stitch-skills for Claude Code skill integration.

---

## SimpleFunctions MCP — Prediction Market Data Layer for Mambamode — 2026-04-11

Source: Instagram reel + web research
Summary: SimpleFunctions MCP (simplefunctions.dev) exposes 29 tools covering 9,706+ active Kalshi and Polymarket contracts via Claude Code or Cursor MCP. Supports read (odds, volume, spreads) and act (order execution with trading credentials). A zero-config open-source alternative exists: `npx -y prediction-mcp` (Polymarket/PredictIt/Kalshi, no API key for reads). Both can be added to Cursor MCP config and queried in natural language.
Why Interesting: Mambamode is an NBA betting intelligence dashboard. Prediction market data (Kalshi NBA playoff odds, Polymarket game contracts) is a distinct signal source from traditional sportsbook odds. Could surface market inefficiencies between bookmaker lines and prediction market consensus — the core Mambamode edge signal.
Revisit Trigger: When Mambamode next adds a new data source OR when building the edge/signal layer that compares sportsbook odds to prediction market implied probabilities.
Status: WATCHING
Tags: #mambamode #prediction-markets #kalshi #polymarket #mcp #odds #nba #edge-signals
Context At Time: Mambamode stack is React + Vite + Tailwind + Claude API + the-odds-api.com + balldontlie.io. Critical path: 017→008→(009D,029,022)→023→018. Supabase live (21 tables). Prediction market NBA contracts exist on Kalshi and Polymarket — volume and liquidity are lower than sportsbooks but the market structure (binary contracts) creates exploitable pricing differentials vs traditional lines.
Key Tools To Re-Evaluate: simplefunctions.dev (SimpleFunctions MCP, 29 tools), github.com/jamesanz/prediction-mcp (npx -y prediction-mcp, no API key for Polymarket reads), kalshi.com/account/profile (API key + PEM for trading credentials), polymarket.com CLOB API.

---
