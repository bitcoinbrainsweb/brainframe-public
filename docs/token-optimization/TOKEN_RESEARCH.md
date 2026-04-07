# TOKEN_RESEARCH.md
Token optimization research for Dave Bradley's AI workflow.
Self-improving: updated weekly by AI Pulse. Never overwrite — append and revise.
Constraint: findings must not slow work or degrade quality.

Last updated: 2026-04-07 (Perplexity Computer deep research — All 3 Chunks COMPLETE)

---

## CONFIRMED FINDINGS

### MCP Token Overhead

- **MCP cost is from tool definitions, not the protocol.** Each server loads tool schemas into context before conversation starts.
- **Per-tool cost: 100–300 tokens simple; 300+ enterprise tools.** Input schemas = 60–80% of each tool's token cost.
- **Gmail MCP estimate: 1,400–5,100 tokens.** No direct measurement for claude.ai connector version.
- **Google Workspace MCP (full): ~5,000–10,000 tokens** depending on services enabled.
- **Multi-MCP setups compound fast:** GitHub + Slack + Sentry + Grafana + Splunk = ~55,000 tokens before you type anything.
- **MCP adds ~37% more input tokens vs CLI** — and that's optimistic. Tool results (screenshots, large payloads) can dwarf this.
- **500+ tools = 100K+ tokens on definitions alone.** Sparse definitions save tokens but increase hallucination. No winning without dynamic loading.

### On-Demand Tool Loading

- **Claude Code defers MCP loading by default since Jan 2026.** 85–95% startup token reduction. Tool Search = ~500 tokens; 3–5 on-demand tools = ~3,000 tokens vs ~77,000 upfront.
- **CRITICAL UNKNOWN:** Whether claude.ai (non-Claude Code) uses deferred loading. Single most important unanswered question.

### Session Management

- **Full history re-sent every message. No exceptions.** Cost compounds: Turn n = (2n-1)× first message.
- **Agentic sessions consume 4–15× more tokens than chat.** 3-agent team = ~7× standard session.
- **Prompt caching: 90% discount on cached prefixes (5-min TTL).** Typical savings: 40–50% on input costs.
- **Cache expires after 5 min idle.** 200K tokens cost 12.5× more after expiry vs. within window.
- **One long continuous session is cheaper than two shorter ones** — re-caching costs full price each time.
- **Context rot is real.** Quality starts degrading after ~32K tokens. Lost-in-the-middle effect: model ignores content placed in the middle of large contexts.
- **Four failure modes:** Context Poisoning (hallucination enters context), Context Distraction (over-reliance on context vs. training), Context Confusion (superfluous info), Context Clash (conflicting info accumulates).
- **Never edit files manually during a session — busts prompt cache.** Never use /compact (also busts cache). Don't leave sessions idle >5 min.
- **Avoid grep/find — can produce thousands of tokens of output.** Tell Claude to read specific files only.
- **Sonnet 4.6 uses ~3× more output tokens than Sonnet 4.5** despite only 8 point intelligence improvement.

### Auto-Compaction

- **Triggers at ~95% context.** Compaction prompt = 1,121 tokens. Fidelity lost unpredictably.
- **Better alternative:** Ask Claude to "Save your current context to a file" — then reload it. Preserves cache. Gives you control over what's retained.
- **Factory.ai finding:** "Total tokens to complete a task" is the right metric, not tokens per request. Lost details require re-fetching, which can exceed compression savings.

### Handoff Files

- **500–1,500 token handoff replaces 5,000–15,000 tokens of history.** 80–95% reduction, no fidelity loss.
- Dave's Brainframe system already implements this correctly.
- **Three-tier context system (community pattern):** Tier 1 = vault summary (~10 tokens), Tier 2 = project summaries (~5K tokens), Tier 3 = detailed context (~3K tokens, only when active). 60–80% reduction vs loading everything.

### System Prompt / Project Instructions

- **CLAUDE.md loads in full every session, cached after first message** (90% discount on subsequent turns).
- **Keep under 50 lines** (Anthropic says 200, best practice teams say 30–50).
- **CLAUDE.md as index pattern:** Point to detailed files. Claude reads them only when working on related tasks.
- **CLAUDE.md is delivered as a user message, not true system prompt.** Instructions there have less enforcement weight.
- **Compression:** Ask Claude to rewrite instructions for "maximum token density without losing any directive content."
- **Output verbosity instructions reduce output tokens ~63%.** Net positive when output volume is high.
- **Thinking tokens:** "ultrathink" = 31,999 tokens; "megathink"/"think deeply" = 10,000 tokens. Billed as output tokens (expensive). Use deliberately.

### Skills / Context File Loading

- **3-level lazy loading:** Level 1 = name + description (~100 tokens/skill, always loaded). Level 2 = body (~5K tokens, on invocation). Level 3 = referenced files (as needed).
- **Dave's ~30 skills = ~3,000 tokens of metadata at startup.** Bodies only load when triggered. Healthy.
- **CONFLICT:** GitHub issue #16160 reports Claude Code loading ALL skills fully at startup (~180K tokens for 50 skills). Anthropic unresponsive. May be version-specific or claude.ai-specific behavior — unknown.
- **Skill description field (max 1,024 chars) is the most important field.** Drives trigger accuracy AND whether body loads.
- **Smaller focused skills > large monolithic ones.** Avoid premature grouping.
- **Path-scoped rules** (`.claude/rules/*.md` with YAML `paths:` frontmatter) = native conditional loading. Rules only load when Claude reads matching files.
- **No mechanism exists to reference a file without loading its content.** All reads, @ references, URL fetches = content enters token window.
- **Hooks as preprocessors:** Filter large files before they enter context. Instead of reading 10K-line log, hook greps for errors and returns hundreds of lines.
- **1,000 lines of code ≈ 10,000 tokens.** Reading 10 files = ~100K tokens added to context.

### Community Patterns (High Signal)

- **Dependency map instead of full source:** ~5KB XML file replaces 500K tokens of raw code. 96% reduction. Agent deduces file relationships without reading contents.
- **Sub-agent isolation:** Main agent holds clean context. Sub-agents do dirty work (file reads, exploration). 50K tokens of sub-agent exploration returns 2K token summary to main context.
- **Plan-then-execute:** Agent outlines approach before writing code. Catches direction errors before they compound across 20 tool calls.
- **Writer/Reviewer pattern:** Separate sessions for writing vs. reviewing. Prevents bias, resets context.
- **KERNEL framework:** Single clear objective per prompt, explicit constraints, narrow scope. Measured: 58% token reduction, 72% first-try success, 67% faster to useful result.
- **Multi-model orchestration:** Lightweight model (Haiku) handles routing, JSON formatting, summarization (~70% of agent tokens). Heavier model (Opus) only for complex reasoning.
- **Inject project identity upfront** to reduce discovery tokens: "You are a staff engineer with 15 years in [tech stack]. Files are located at [paths]. Testing framework is [X]."
- **Restart agent after each discrete feature/task** to prevent context rot accumulation.
- **Suppress verbose build/test output** to reduce tool result tokens.

### Key Benchmarks (All Confirmed)

| Technique | Token Reduction |
|-----------|----------------|
| Skills supplementing MCP (Google ADK) | 87% |
| Dependency map vs full source | 96% |
| Memory pointers (Anthropic research) | 84–87% |
| Three-tier context system | 60–80% |
| HollowOS JSON-native OS | 68.5% |
| KERNEL prompt framework | 58% |
| Sub-agent isolation (deep exploration) | ~96% |
| DSP framework (Stanford) | 50–80% |
| On-demand MCP loading | 85–95% |
| Deferred skill loading | 82% vs full CLAUDE.md load |

---

## ACTIVE KNOWLEDGE GAPS (PRIORITIZED)

**HIGH — Answer these first**
- Does claude.ai (non-Claude Code) use deferred MCP loading or eager loading?
- Exact token counts for Dave's Gmail, Drive, Base44 MCPs in claude.ai interface
- Is GitHub issue #16160 (skills eager loading bug) present in claude.ai?
- Does the 5-min cache TTL apply to claude.ai web sessions or API only?

**MEDIUM — Next research cycle**
- At what session length does fresh session + handoff beat continuing long session? (break-even analysis)
- Thinking token ROI by task type — when does ultrathink justify cost?
- Are compound technique savings additive, multiplicative, or overlapping?
- Optimal CLAUDE.md / project instructions structure to maximize cache hit rate
- Prompt caching mechanics for MCP tool definitions — when does mid-session tool call bust cache?

**LOW — Monitor**
- LLMLingua-2 as preprocessor for very large Cursor prompts
- MCP spec SEP-1576 (schema deduplication) — open proposal, unimplemented
- KV cache management becoming practitioner-relevant (SpeCache, etc.)
- Speculative decoding — server-side only for now, not practitioner-actionable

---

## SOURCES BEING TRACKED

**Tier 1 — Check weekly**
- simonwillison.net/tags/context-engineering/ — named pattern taxonomy, Drew Breunig updates
- stackone.com/blog — production token measurements, practitioner patterns
- latent.space (AINews) — model benchmark token efficiency, emerging tools
- news.smol.ai — daily aggregation of r/LocalLLaMA, practitioner discourse
- Anthropic Engineering Blog: anthropic.com/engineering/
- r/ClaudeCode — active practitioner community, MCP token costs
- dbreunig.com — context failure mode taxonomy

**Tier 2 — Check monthly**
- LangChain Blog: blog.langchain.com
- Verdent AI Guides: verdent.ai/guides/
- arxiv.org — SpeCache, structured context engineering papers
- systemprompt.io/guides/claude-code-cost-optimisation
- Nate Jones Substack: natesnewsletter.substack.com

---

## NEXT WEEK PRIORITY

1. Investigate: does claude.ai use deferred MCP loading? (single highest impact unknown)
2. Measure Dave's actual project instructions token cost across Brainframe projects
3. Apply KERNEL framework principles to Nightwatch Cursor prompt structure
4. Evaluate dependency map approach for Coinbeast/Nightwatch codebase context
5. Audit skill descriptions against "would agent know when NOT to use this?" test

---

## RESEARCH LOG

| Date | What was learned | Source | Gaps closed | New gaps opened |
|------|-----------------|--------|-------------|-----------------|
| 2026-04-07 | Seed file created | — | — | Initial gaps |
| 2026-04-07 | Chunk 1: MCP overhead, session compounding, caching mechanics, handoff patterns, Skills vs MCP 87% benchmark | Perplexity Computer | MCP overhead structure, session cost model, caching mechanics | Whether claude.ai uses deferred MCP loading |
| 2026-04-07 | Chunk 2: System prompt mechanics, skill lazy loading architecture, path-scoped rules, CLAUDE.md index pattern, hooks as preprocessors, compression techniques, cache invalidation rules | Perplexity Computer | Skill loading architecture, compression options, cache invalidation | Skill loading bug #16160 status in claude.ai |
| 2026-04-07 | Chunk 3: Context rot failure modes (named taxonomy), sub-agent isolation, dependency maps, KERNEL framework, multi-model orchestration, plan-then-execute, thinking token tiers, 10 new sources added | Perplexity Computer | Context failure modes, community patterns, thinking token mechanics | Break-even analysis for session length, compound savings measurement |
