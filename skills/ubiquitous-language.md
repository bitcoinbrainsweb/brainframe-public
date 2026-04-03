---
name: ubiquitous-language
description: "Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonical terms. Saves to UBIQUITOUS_LANGUAGE.md. Use when user wants to define domain terms, build a glossary, harden terminology, create a ubiquitous language, or mentions \'domain model\' or \'DDD\'."
---

# Ubiquitous Language
Version: 1.0

Extract and formalize domain terminology into a consistent glossary.

## Process

1. Scan conversation for domain-relevant nouns, verbs, concepts
2. Identify: ambiguities (same word, different meanings), synonyms (different words, same concept), vague terms
3. Propose canonical glossary with opinionated term choices
4. Write to `UBIQUITOUS_LANGUAGE.md`
5. Output summary inline

## Entry Format

```markdown
## [Term]
**Definition:** [One sentence — what it is]
**Used in:** [Where this concept appears in the system]
**Not to be confused with:** [Common confusion, if any]
**Status:** CONFIRMED | PROVISIONAL | DISPUTED
```

## Rules

- Prefer the collaborator's existing language over invented terms
- When two terms mean the same thing, pick one and mark the other as SUPERSEDED
- When one term means two things, split it and name both explicitly
- PROVISIONAL terms need a decision before implementation begins
