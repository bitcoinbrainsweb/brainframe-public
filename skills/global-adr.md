---
name: global-adr
description: "Global ADR pattern. Create Architecture Decision Records for significant technical and coordination decisions. Triggers on: hard-to-reverse choices, technology selections, autonomy level assignments, handoff protocol changes, state strategy changes."
---

# Global ADR Pattern
Version: 1.0 | 2026-04-03

## When to Write

- Hard-to-reverse architectural choices
- Technology selections
- Autonomy level assignments
- Handoff protocol or state structure changes
- Any "we decided" moment

Coordination decisions qualify — not only code architecture.

## Format

```markdown
# ADR-[NUMBER]: [Title]
Date: YYYY-MM-DD
Status: [PROPOSED / ACCEPTED / DEPRECATED / SUPERSEDED by ADR-XXX]

## Context
[What forced this decision?]

## Decision
[What was decided — stated directly.]

## Rationale
[Why this over alternatives? Name alternatives considered.]

## Consequences
[What becomes easier? Harder? What is now required?]

## Review trigger
[What event causes us to revisit?]
```

## Storage

- `docs/adr/ADR-[NUMBER]-[slug].md`
- Committed to project repo via GitHub API
