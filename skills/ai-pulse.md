---
name: ai-pulse
description: Bleeding-edge AI intelligence skill. Use when Dave asks to run the daily AI report, check what's new in AI, scan for AI developments, stay current on LLMs or AI tools, or review the master sources list. Also triggers when Dave says "ai pulse", "daily report", "what's new in AI", "scan sources", or "update me on AI". Loads the full curated source list across 7 categories (primary labs, newsletters, researchers, Reddit, GitHub, academic, podcasts) and runs a structured daily intelligence report against them using web search. Always use this skill rather than improvising — it ensures consistent source coverage and report format.
---

# AI Pulse — Bleeding Edge AI Intelligence

Keeps Dave current on the absolute frontier of AI. Covers model releases, research papers, tooling, community signal, and thought leadership across 60+ curated sources.

## Trigger Phrases
- "ai pulse" / "run ai pulse"
- "daily report" / "ai daily report"
- "what's new in AI" / "scan AI sources"
- "update me on AI" / "what happened in AI today/this week"
- "check the sources" / "any AI news"

## Workflow

### Step 1 — Load Source List
Read `skills/ai-pulse-sources.md` from this repo for the full categorized source list.

### Step 2 — Run Web Search Sweep
Search across the high-priority (🔴 Critical) sources first, then 🟠 High if time allows:

**Critical sweep queries (run these):**
- `Anthropic news site:anthropic.com` 
- `OpenAI news release` (last 48h)
- `Google DeepMind Gemini announcement`
- `AI research paper arxiv week`
- `GitHub trending AI python`
- `r/MachineLearning hot posts`
- Any lab-specific query if a known release is imminent

### Step 3 — Fill Report Template

Output the report in this exact format:

---

## 📡 AI Pulse Report — [DATE]

### 🔴 CRITICAL HITS
*New model releases, major capability jumps, API changes, pricing shifts*

- [Source]: [What happened] — [Why it matters in 1 sentence]

### 🧪 RESEARCH SIGNAL
*arXiv papers, benchmarks, SOTA updates*

- [Paper title] ([source link if found]): [2-sentence summary]

### 🛠️ BUILDER BUZZ
*GitHub trending, tool launches, framework updates*

- [Tool/repo]: [What changed] — [Practical impact]

### 📡 COMMUNITY CHATTER
*Reddit signal, X/Twitter discussion worth noting*

- [r/sub or @handle]: [What the community is reacting to]

### 💡 ONE INSIGHT
*The single most important thing from today's scan*

> [One crisp paragraph. What changes tomorrow because of this?]

### 📌 NEW SOURCES FOUND
*Any new blogs, researchers, repos, or communities to add to the master list*

- [Name] ([URL or handle]): [Why worth adding]
  → Memory: suggest adding to `ai-pulse-sources.md`

---

## Report Cadence

| Frequency | What to check |
|-----------|--------------|
| Daily | GitHub Trending, The Rundown AI, TLDR AI, r/MachineLearning |
| Weekly | Import AI, Latent Space, Interconnects, The Batch, arXiv digest |
| On release | All primary lab blogs (Anthropic, OpenAI, DeepMind, Meta AI) |

## Source Categories Quick Reference

See `skills/ai-pulse-sources.md` for full list. Summary:

- **Primary** (12 sources): Lab official blogs — Anthropic, OpenAI, DeepMind, Meta AI, Mistral, HuggingFace, DeepSeek, Cohere, xAI, Perplexity
- **Newsletters** (10): Import AI, Latent Space, Interconnects, TLDR AI, The Rundown, The Batch, One Useful Thing, Ben's Bites, Superhuman AI, AI_Distilled
- **Researchers** (13 on X): @karpathy, @simonw, @swyx, @emollick, @ylecun, @rasbt, @dair_ai, @AndrewYNg, @DrJimFan, @jasonwei20, @drfeifei, @OfficialLoganK, @yoshuabengio
- **Reddit** (8): r/MachineLearning, r/LocalLLaMA, r/AI_Agents, r/artificial, r/ClaudeAI, r/PromptEngineering, r/ChatGPT, r/singularity
- **GitHub** (8): LangChain, Ollama, CrewAI, AutoGen, DSPy, awesome-ai-agents-2026, awesome-opensource-ai, GitHub Trending
- **Academic** (6): arXiv cs.AI, arXiv cs.LG, Papers With Code, alphaXiv, Semantic Scholar, LessWrong
- **Podcasts** (5): Latent Space, Dwarkesh Patel, The AI Daily Brief, Lex Fridman, TWIML

## Notes
- Signal tiers: 🔴 Critical → always check | 🟠 High → check weekly | 🟡 Medium → when relevant
- When a new source is found during a report, flag it and suggest adding to `ai-pulse-sources.md`
- The React dashboard artifact (`ai-sources-dashboard.jsx`) is the visual version of the source list

## Standing Weekly Research Items

In addition to the standard AI news sweep, always check the following on weekly runs:

### 🪙 TOKEN OPTIMIZATION WATCH
*Research cadence: weekly + triggered on any new model release*
*Purpose: inform OI-008 token optimization plan (must not slow work or degrade quality)*

Search queries to run weekly:
- `Claude token optimization best practices 2026`
- `LLM context window efficiency techniques`
- `AI agent token cost reduction production`
- `Claude MCP token usage overhead`

Report format — add a section to the weekly AI Pulse output:

#### Token Optimization Signal
- [Finding]: [What changed or was discovered] — [Impact on Dave's workflow]
- Flag any new model releases immediately — these trigger a prompt audit (OI-006)
