---
name: prd-to-plan
description: "Turn a PRD into a multi-phase implementation plan using tracer-bullet vertical slices, saved as a local Markdown file in ./plans/. Use when user wants to break down a PRD, create an implementation plan, plan phases from a PRD, or mentions \'tracer bullets\'."
---

# PRD to Plan
Version: 1.0

Break a PRD into a phased implementation plan using vertical slices (tracer bullets).
Output: Markdown file in `./plans/`.

## Process

1. **Confirm PRD is in context** — if not, ask user to paste it
2. **Identify durable architectural decisions** — data models, auth patterns, integration points
3. **Define tracer bullet slices** — each slice is end-to-end, shippable, proves an architectural seam
4. **Sequence phases** — order by: risk reduction first, dependency order second, value third
5. **Write the plan** — one file per plan, saved to `./plans/[project-name]-plan.md`

## Slice Rules

- Every slice must be independently testable
- Every slice must touch all layers (data → logic → UI where applicable)
- No slice should be "just the database" or "just the UI"
- Each slice title = one sentence describing what a user can do after it ships

## Output Format

```markdown
# Implementation Plan — [Project Name]
Generated: YYYY-MM-DD

## Architectural Decisions
- [decision]: [rationale]

## Phase 1 — [Title]
**Slice:** [What user can do]
**Scope:** [What gets built]
**Validates:** [What architectural risk this proves]
**Acceptance:** [How to verify it works]

## Phase 2 — ...
```
