---
name: gpt-deep-research
description: "Use when writing prompts for ChatGPT Deep Research. Load before generating any GPT deep research prompt."
---

# GPT Deep Research Prompt Skill
Version: 1.0

## What Deep Research Is

Autonomous research agent. Proposes its own plan, browses hundreds of sources, produces a cited report. Takes 5–30 minutes.

Not a chatbot — behaves like a research analyst given a brief.

**Access:** Tools menu → "Run deep research". Attach files for context before submitting.

## Prompt Structure

```
[OBJECTIVE]
[One sentence: what decision this research supports]

[RESEARCH QUESTIONS]
1. [Most important question]
2. [Second question]
3. [Third question — max three]

[CONTEXT]
[What we already know — so it doesn't rehash basics]

[CONSTRAINTS]
- Recency: focus on [year range]
- Geography: [jurisdiction if relevant]
- Perspective: [industry lens]

[OUTPUT]
Structured report with: executive summary, findings per question, source quality assessment, recommended next steps.
```

## Rules

- Max three research questions. Deep Research loses focus beyond that.
- Include what you already know — saves time and improves depth
- Specify the decision it supports — anchors the research to something actionable
- Attach any relevant documents before submitting


---

> **Token optimization gate:** Before selecting a model or designing an API call, check `brainframe-public/docs/TOKEN_OPTIMIZATION.md`. Default Sonnet 4.6. Escalate to Opus only when justified. Downgrade to Haiku for structured/data ops.