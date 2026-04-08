---
name: perplexity-research
description: "Use when writing prompts for Perplexity Pro. Load before generating any Perplexity research prompt."
---

# Perplexity Research Prompt Skill
Version: 1.0

## What Perplexity Pro Is

Real-time answer engine. Searches first, then answers. Every response grounded in live web search with inline citations.

**Modes:**
- **Pro Search** — default for complex queries
- **Deep Research** — slower, report-style, for synthesis

Key difference from ChatGPT: vague prompts produce vague searches. Domain-specific language produces precise results.

## Prompt Structure

```
[CONTEXT]
[one paragraph: what project, what decision, what we already know]

[QUESTION]
[one focused question — not a list]

[CONSTRAINTS]
- Recency: [timeframe if relevant]
- Geography: [jurisdiction if relevant]
- Exclude: [sources or topics to ignore]

[OUTPUT FORMAT]
[what you want back: list / comparison table / narrative / citations only]
```

## Rules

- One question per prompt. Never ask five things at once.
- Include domain-specific terms. Perplexity uses them as search terms.
- Specify output format explicitly. Default is prose — ask for tables or lists if needed.
- For regulatory or legal research: specify jurisdiction.
- For competitive research: name the specific competitors to compare.


---

> **Token optimization gate:** Before selecting a model or designing an API call, check `brainframe-public/docs/TOKEN_OPTIMIZATION.md`. Default Sonnet 4.6. Escalate to Opus only when justified. Downgrade to Haiku for structured/data ops.