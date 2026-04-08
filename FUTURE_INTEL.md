# FUTURE_INTEL.md
Brainframe | Dave Bradley | Created: 2026-04-08

A log of interesting signals flagged for future re-analysis.
When re-reading this file, compare each entry's `Context At Time` to current reality.
Flag any entry where the Revisit Trigger has been met or Status should change.

---

## Graph-Layer AI Memory (GraphRAG / Zep / PlugMem) — 2026-04-08

Source: Instagram/TikTok reel (engagement bait — "comment token")
Summary: Graph knowledge databases replace flat markdown memory files with node/edge structures. Instead of loading entire MD files into context, the agent retrieves only relevant knowledge units via graph traversal. Real token savings benchmarked at up to 100x vs full-context loading.
Why Interesting: Directly relevant to brainframe memory architecture. Current approach (ADMIN_STATE.md, DECISIONS.md, ADMIN_LOG.md) loads full files every session boot. Graph layer would enable selective retrieval at scale.
Revisit Trigger: When Nightwatch DECISIONS.md exceeds 1000 entries OR session boot token cost becomes a measurable pain point.
Status: WATCHING
Tags: #memory #graph #graphrag #token-efficiency #brainframe-architecture
Context At Time: Nightwatch early-stage, DECISIONS.md ~50 entries. Brainframe uses flat MD files on GitHub. No MCP graph server in stack. Session boot reads 5 files sequentially. Graph layer assessed as overkill at current volume — complexity and infrastructure overhead outweigh gains.
Key Tools To Re-Evaluate: Zep (getzep.com), Graphiti, PlugMem (Microsoft Research), claude-mem with graph backend.

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
