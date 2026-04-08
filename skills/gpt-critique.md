---
name: gpt-critique
description: "Use when writing a critique prompt for GPT. Covers feature critique, architecture review, and product decisions. Load before generating any GPT critique prompt."
---

# GPT Critique Skill
Version: 1.0

Get GPT to critique a feature spec, architecture decision, or product direction — and surface what's missing.

## Prompt Structure

```
You are a senior [domain] advisor reviewing a [feature spec / architecture decision / product direction].

CONTEXT:
[paste the spec, decision, or description]

YOUR TASK:
1. Identify the three most significant risks or weaknesses
2. Identify what is missing that should be there
3. Suggest improvements — be specific, not generic
4. Rate overall soundness: Strong / Adequate / Weak — with one sentence of reasoning

CONSTRAINTS:
- Do not write implementation code or Cursor prompts
- Do not suggest adding scope unless it addresses a critical gap
- Be direct. No diplomatic softening.
```

## Rules

- Always include the actual spec/decision text in the prompt — never describe it abstractly
- Specify the domain so GPT calibrates appropriately (e.g. "AML compliance platform", "B2B SaaS", "developer tooling")
- Ask for specific weaknesses, not general feedback
- One critique prompt per decision — do not bundle multiple specs


---

> **Token optimization gate:** Before selecting a model or designing an API call, check `brainframe-public/docs/TOKEN_OPTIMIZATION.md`. Default Sonnet 4.6. Escalate to Opus only when justified. Downgrade to Haiku for structured/data ops.