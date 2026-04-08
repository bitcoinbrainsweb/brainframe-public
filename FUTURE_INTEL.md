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
