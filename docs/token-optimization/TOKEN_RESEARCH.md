# TOKEN_RESEARCH.md
Token optimization research for Dave Bradley's AI workflow.
Self-improving: updated weekly by AI Pulse. Never overwrite — append and revise.
Constraint: findings must not slow work or degrade quality.

Last updated: 2026-04-07 (Perplexity Computer deep research — Chunk 1)

---

## CONFIRMED FINDINGS

### MCP Token Overhead

- **MCP cost is from tool definitions, not the protocol.** Each MCP server loads tool schemas into context. The JSON-RPC transport itself is zero cost.
- **Per-tool cost: 100–300 tokens for simple tools; 300+ for enterprise tools.** Input schemas are 60–80% of each tool definition's token cost.
- **Gmail MCP estimate: 1,400–5,100 tokens** (~14–17 tools × 100–300 tokens). No direct measurement exists for the claude.ai connector version.
- **Google Workspace MCP (full): ~5,000–10,000 tokens** depending on which services are enabled.
- **Multi-MCP setups compound fast:** GitHub + Slack + Sentry + Grafana + Splunk = ~55,000 tokens before conversation starts.
- **MCP adds ~37% more input tokens vs CLI tools** — and that's the optimistic estimate. Tool results (screenshots, large payloads) can dwarf this.

### On-Demand Tool Loading (Critical)

- **As of January 2026, Claude Code defers MCP tool loading by default.** Tool Search auto-enables when tool definitions exceed 10% of context window. Tools only load when actually called.
- **Impact: up to 95% reduction in startup token cost.** 50,000+ token startup configurations now show minimal overhead.
- **Anthropic's own test:** Traditional (all tools upfront) = ~77,000 tokens. With Tool Search = ~8,700 tokens. **85% reduction.** Accuracy also improved (Opus 4 from 49% → 74%).
- **UNKNOWN:** Whether claude.ai (non-Claude Code) MCP connectors use deferred loading or eager loading. This is the most important unknown for Dave's workflow.

### Session Management

- **Full conversation history is re-sent on every message** — not summarized, not referenced. Literal full text every time.
- **Token cost compounds:** Turn 1 = 1×, Turn 2 = 3×, Turn n = (2n-1)×. A 10-turn session costs ~19× what the first message cost in input tokens.
- **Prompt caching gives ~90% discount on previously-seen tokens** (cache hit rate = ~10% of base input price). This is the primary mechanism that makes long sessions economical.
- **Cache TTL is 5 minutes (default).** If you pause >5 min, cache expires. Reloading 200K cached tokens costs 12.5× more after expiry vs. within window.
- **Extended TTL (1 hour) available** at 2× base input price — worth it for very long sessions.
- **One long continuous session is almost always cheaper than two shorter ones** covering the same ground — because re-caching at session start costs full price again.

### Auto-Compaction

- **Triggers at ~95% context capacity.** Claude summarizes history, replaces it with a compressed version.
- **The compaction summarization prompt itself costs 1,121 tokens.**
- **Fidelity is lost** — instructions, constraints, and patterns from early conversation get compressed unpredictably.
- **Best practice:** Run `/compact` manually at logical task breakpoints rather than waiting for auto-compact to trigger mid-task.

### Handoff Files

- **A well-written handoff file = 500–1,500 tokens replacing 5,000–15,000 tokens of history.** 80–95% reduction with no quality loss (vs. auto-compaction which loses fidelity).
- Dave's Brainframe system (NIGHTWATCH_STATE.md, SESSION_HANDOFF.md, etc.) is already implementing this pattern correctly.

### Prompt Caching Mechanics

- **Tool definitions CAN be cached** via the `tools` array. Cache prefix order: tools → system → messages.
- **Modifying any tool definition invalidates the entire cache** — tools + system prompt + messages all re-price.
- **Minimum threshold for caching:** 1,024 tokens (Sonnet/Opus); 4,096 tokens (Haiku 4.5, Opus 4.5).
- **Typical savings from caching: 40–50% on input token costs** in a normal day.

### Skills vs MCP (Key Finding)

- **Skills dramatically outperform MCP for token efficiency when the use case fits.**
- Google ADK benchmark: BigQuery MCP alone (no skill) = 13,763 tokens over 9 turns. BigQuery MCP + skill = 6,653 tokens over 5 turns (52% fewer tokens, fewer turns).
- Multi-MCP without skill: 328,083 tokens. Same MCPs + skill: 39,622 tokens. **~87% fewer tokens.**
- **Implication for Dave:** Where Brainframe skills can replace or supplement MCP calls, they should.

---

## ACTIVE KNOWLEDGE GAPS

**HIGH PRIORITY**
- Does claude.ai (non-Claude Code) use deferred/on-demand MCP tool loading or eager loading? This single answer changes the entire optimization strategy for Dave's sessions.
- What are the exact token costs of Dave's specific MCP connectors (Gmail, Drive, Base44) in the claude.ai interface?
- Does the 5-minute cache TTL apply to claude.ai web sessions or only the API?

**MEDIUM PRIORITY**
- What is the token cost of Dave's current project instructions / Brainframe boot sequence across all projects?
- Are there techniques for compressing skill files without degrading trigger accuracy?
- How does the Cursor prompt structure (SANITYCHECK/RESULT/GATE pattern) affect token consumption per upgrade?

**LOW PRIORITY**
- Emerging techniques: KV cache management, speculative decoding — relevance timeline unclear.
- MCP spec proposal SEP-1576 (schema deduplication via JSON $ref) — open, not yet implemented.

---

## SOURCES BEING TRACKED

- Anthropic Prompt Caching Docs: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Anthropic Advanced Tool Use (Engineering Blog): https://www.anthropic.com/engineering/advanced-tool-use
- Anthropic Claude Code Cost Docs: https://code.claude.com/docs/en/costs
- Simon Willison: https://simonwillison.net (MCP overhead coverage)
- r/ClaudeCode: https://reddit.com/r/ClaudeCode (measured community findings)
- r/ClaudeAI: https://reddit.com/r/ClaudeAI
- Mario Giancini: https://mariogiancini.com/the-hidden-cost-of-mcp-servers-and-when-theyre-worth-it
- DeployStack MCP token guide: https://deploystack.io/blog/how-mcp-servers-use-your-context-window
- systemprompt.io cost optimization: https://systemprompt.io/guides/claude-code-cost-optimisation
- Limited Edition Jonathan (Substack): https://limitededitionjonathan.substack.com
- Richard Seroter (Skills vs MCP): https://seroter.com/2026/03/16/my-custom-agent-used-87-fewer-tokens-when-i-gave-it-skills-for-its-mcp-tools/
- Nate Jones Substack: https://natesnewsletter.substack.com

---

## NEXT WEEK PRIORITY

1. Run Perplexity Chunks 2 and 3 — system prompt optimization, context file loading, community patterns, knowledge gaps
2. Investigate: does claude.ai use deferred MCP loading? (highest impact unknown)
3. Measure Dave's actual MCP token costs if possible

---

## RESEARCH LOG

| Date | What was learned | Source | Gaps closed | New gaps opened |
|------|-----------------|--------|-------------|-----------------|
| 2026-04-07 | Seed file created. | — | — | Initial gaps listed |
| 2026-04-07 | Perplexity Chunk 1 complete. MCP overhead measured, session compounding confirmed, caching mechanics documented, Skills vs MCP benchmark found (87% reduction). | Perplexity Computer deep research | MCP overhead structure, session cost model, caching mechanics, handoff patterns | Whether claude.ai uses deferred MCP loading (critical unknown) |
