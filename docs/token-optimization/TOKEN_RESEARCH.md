# TOKEN_RESEARCH.md
Token optimization research for Dave Bradley's AI workflow.
Self-improving: updated weekly by AI Pulse. Never overwrite — append and revise.
Constraint: findings must not slow work or degrade quality.

Last updated: 2026-04-07 (Perplexity Computer deep research — Chunks 1 & 2)

---

## CONFIRMED FINDINGS

### MCP Token Overhead

- **MCP cost is from tool definitions, not the protocol.** Each MCP server loads tool schemas into context. The JSON-RPC transport itself is zero cost.
- **Per-tool cost: 100–300 tokens for simple tools; 300+ for enterprise tools.** Input schemas are 60–80% of each tool definition's token cost.
- **Gmail MCP estimate: 1,400–5,100 tokens** (~14–17 tools × 100–300 tokens). No direct measurement for the claude.ai connector version.
- **Google Workspace MCP (full): ~5,000–10,000 tokens** depending on which services are enabled.
- **Multi-MCP setups compound fast:** GitHub + Slack + Sentry + Grafana + Splunk = ~55,000 tokens before conversation starts.
- **MCP adds ~37% more input tokens vs CLI tools** — and that's the optimistic estimate.

### On-Demand Tool Loading (Critical)

- **As of January 2026, Claude Code defers MCP tool loading by default.** Tool Search auto-enables when tool definitions exceed 10% of context window.
- **Impact: up to 95% reduction in startup token cost.** Anthropic's own test: traditional = ~77,000 tokens; with Tool Search = ~8,700 tokens (85% reduction). Accuracy also improved.
- **UNKNOWN for Dave's workflow:** Whether claude.ai (non-Claude Code) MCP connectors use deferred loading. This is the most important open question.

### Session Management

- **Full conversation history is re-sent on every message.** Token cost compounds: Turn n = (2n-1)× first message cost.
- **Prompt caching gives ~90% discount on previously-seen tokens.** Cache hit rate = ~10% of base input price.
- **Cache TTL is 5 minutes (default).** Pause >5 min = cache expires. 200K cached tokens cost 12.5× more after expiry.
- **One long continuous session is almost always cheaper than two shorter ones** — re-caching at session start costs full price again.
- **Extended 1-hour TTL available** at 2× base input price — worth it for very long uninterrupted sessions.
- **Typical savings from caching: 40–50% on input token costs** in a normal day.

### Auto-Compaction

- **Triggers at ~95% context capacity.** Compaction prompt itself costs 1,121 tokens.
- **Fidelity is lost.** Best practice: run `/compact` manually at logical task breakpoints.

### Handoff Files

- **500–1,500 token handoff file replaces 5,000–15,000 tokens of history.** 80–95% reduction, no fidelity loss.
- Dave's Brainframe system already implements this correctly.

### Prompt Caching Mechanics (Confirmed)

- **Cache prefix order: tools → system → messages.** Any change at a level invalidates that level and everything after.
- **Changing any MCP tool definition invalidates the entire cache** — all levels re-price on next message.
- **Minimum cache threshold:** 1,024 tokens (Sonnet/Opus); 4,096 tokens (Haiku 4.5, Opus 4.5).
- **Output tokens are NOT affected by caching** — always billed at full output rate.
- **Caching does NOT skip processing** — it's a billing/infrastructure optimization. Model still processes full context.

### System Prompt / Project Instructions

- **CLAUDE.md loads in full at every session start.** Every word costs tokens on every message — but gets cached after first message (90% discount on subsequent turns).
- **Anthropic recommends CLAUDE.md under 200 lines.** Best practice teams keep it under 50, some under 30.
- **CLAUDE.md is delivered as a user message, not a true system prompt.** Instructions there have less enforcement than actual system prompt content.
- **Compression technique:** Ask Claude to rewrite instructions for "maximum token density without losing any directive content." Can reduce instruction tokens significantly.
- **Output verbosity instructions in CLAUDE.md reduce output tokens by ~63%** — net positive when output volume is high enough.
- **Place long-form content before instructions** in prompts — improves response quality by up to 30% (Anthropic guidance).

### Skills / Context File Loading

- **Skills use a 3-level lazy loading architecture:**
  - Level 1 (startup, always): name + description = ~100 tokens/skill
  - Level 2 (on invocation): full skill body = up to ~5,000 tokens
  - Level 3 (as needed): files referenced in the skill body
- **This means Dave's ~30 skills load ~3,000 tokens of metadata at startup,** with bodies only loading when triggered. Healthy.
- **CONFLICT in sources:** A GitHub issue (#16160, Jan 2026) reports Claude Code loading ALL skills fully at startup (~180K tokens for 50+ skills). Anthropic has not responded. May be a version-specific bug or environment-specific behavior.
- **Best practice for skill files:** Smaller, more focused skills over large monolithic ones. Avoid premature grouping.
- **Skill trigger accuracy depends entirely on the description field** (max 1,024 chars). This is the most important field.
- **There is no mechanism to reference a file by path without loading its content into context.** All file reads, @ references, and URL fetches result in content entering the token window.
- **Path-scoped rules** (`.claude/rules/*.md` with YAML `paths:` frontmatter) are Anthropic's native conditional loading mechanism — rules only load when Claude reads files matching the specified glob patterns.
- **CLAUDE.md as index pattern:** Keep CLAUDE.md under 50 lines. Point to detailed files. Claude reads detailed files only when working on related tasks.
- **Hooks as preprocessors:** Instead of Claude reading a 10,000-line log file, a hook can grep for errors and return only matching lines. Anthropic-official mechanism for large file reads.
- **1,000 lines of code ≈ 10,000 tokens.** Reading 10 files adds ~100,000 tokens to context.

### Key Benchmarks

- Skills vs MCP (Google ADK): BigQuery MCP alone = 13,763 tokens / 9 turns. BigQuery MCP + skill = 6,653 tokens / 5 turns. Multi-MCP without skill = 328,083 tokens. Same MCPs + skill = 39,622 tokens (**87% fewer tokens**).
- Progressive disclosure across 20+ skills: ~15,000 tokens recovered per session vs loading everything into CLAUDE.md upfront (82% improvement).
- Auto-compaction compression ratio: 98.7%. But "total tokens to complete a task" is the right metric, not tokens per request — lost details require re-fetching.

---

## ACTIVE KNOWLEDGE GAPS

**HIGH PRIORITY**
- Does claude.ai (non-Claude Code) use deferred/on-demand MCP tool loading or eager loading? Single most important unknown.
- What are the exact token costs of Dave's specific MCP connectors (Gmail, Drive, Base44) in the claude.ai interface?
- Does the 5-minute cache TTL apply to claude.ai web sessions or only the API/Claude Code?
- Is the skill lazy-loading bug (GitHub #16160) present in the current claude.ai skills implementation? Or does claude.ai skills work differently?

**MEDIUM PRIORITY**
- What is the token cost of Dave's current project instructions across all Brainframe projects?
- How does the Cursor prompt structure (SANITYCHECK/RESULT/GATE) affect token consumption per upgrade?
- Does claude.ai automatically apply the 1-hour extended TTL for long sessions, or must it be explicitly requested?

**LOW PRIORITY**
- LLMLingua-2 — viable as a preprocessing step for very large Cursor prompts?
- MCP spec proposal SEP-1576 (schema deduplication) — open, not yet implemented.
- SuperClaude UltraCompressed Mode — 70% reduction claim unverified.

---

## SOURCES BEING TRACKED

- Anthropic Prompt Caching Docs: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Anthropic Advanced Tool Use: https://www.anthropic.com/engineering/advanced-tool-use
- Anthropic Claude Code Cost Docs: https://code.claude.com/docs/en/costs
- Anthropic Claude Code Memory Docs: https://code.claude.com/docs/en/memory
- Simon Willison: https://simonwillison.net
- r/ClaudeCode + r/ClaudeAI: community measurements
- systemprompt.io: https://systemprompt.io/guides/claude-code-cost-optimisation
- Limited Edition Jonathan (Substack): https://limitededitionjonathan.substack.com
- Richard Seroter (Skills vs MCP): https://seroter.com/2026/03/16/my-custom-agent-used-87-fewer-tokens-when-i-gave-it-skills-for-its-mcp-tools/
- Taylor Daughtry (Skills lazy loading): https://taylordaughtry.com/posts/claude-skills-are-lazy-loaded-context/
- Factory.ai (compression evaluation): https://factory.ai/news/evaluating-compression
- GitHub Issue #16160 (skill loading bug): https://github.com/anthropics/claude-code/issues/16160
- Nate Jones Substack: https://natesnewsletter.substack.com
- MindStudio token hacks: https://www.mindstudio.ai/blog/claude-code-token-management-hacks-3/

---

## NEXT WEEK PRIORITY

1. Run Perplexity Chunk 3 — community patterns, knowledge gaps, new sources
2. Investigate: does claude.ai use deferred MCP loading? (highest impact unknown)
3. Audit Dave's project instructions token cost across Brainframe projects
4. Consider: path-scoped rules as a pattern for Nightwatch skill files

---

## RESEARCH LOG

| Date | What was learned | Source | Gaps closed | New gaps opened |
|------|-----------------|--------|-------------|-----------------|
| 2026-04-07 | Seed file created | — | — | Initial gaps |
| 2026-04-07 | Chunk 1: MCP overhead measured, session compounding confirmed, caching mechanics, handoff patterns, Skills vs MCP 87% benchmark | Perplexity Computer | MCP overhead structure, session cost model, caching mechanics | Whether claude.ai uses deferred MCP loading |
| 2026-04-07 | Chunk 2: System prompt mechanics, skill lazy loading architecture, path-scoped rules, CLAUDE.md index pattern, hooks as preprocessors, compression techniques, cache invalidation rules | Perplexity Computer | Skill loading architecture, compression options, cache invalidation rules | Skill loading bug (#16160) status in claude.ai, cache TTL in web interface |
