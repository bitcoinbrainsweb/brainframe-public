# Spec: Critique-Spec Pipeline
Project: Admin
Version: v1
Status: ACTIVE
Upgrade ref: N/A (skill-based)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Feature specs written by a single AI have blind spots — missed edge cases, unstated assumptions, contradictions with other specs. A two-AI sequential critique (GPT-4o then Perplexity sonar-pro) stress-tests specs before Cursor implements them. Without a spec for the pipeline itself, the workflow is fragile and can't be extended or audited.

## Users / Use Cases
- Dave — triggers critique on any spec before implementation begins
- spec-writing skill — auto-triggers critique after every new spec creation

## Success Metrics
- Every new spec receives a critique summary before a Cursor prompt is written for it
- Disagreements between GPT-4o and Perplexity are explicitly flagged — never silently resolved
- Open questions surfaced by critique are added as OQ-XXX entries back to the spec
- Full critique output persisted to `brainframe-comms/specs/{project}/critiques/` for audit trail

## Requirements
1. Trigger: Dave says "critique spec" OR spec-writing skill auto-triggers on new spec creation
2. Dave confirms which spec before firing (if manually triggered); spec-writing skill passes spec path directly
3. Fetch spec from `brainframe-comms/specs/{project}/` — always source of truth, never from mirror
4. Sequential execution: GPT-4o critique first, then Perplexity sonar-pro critique
5. Surface to Dave: summary only — top 2-3 issues, OQs flagged, GPT vs Perplexity disagreements
6. Save full critique output to `brainframe-comms/specs/{project}/critiques/{spec-slug}-critique-{YYYY-MM-DD}.md`
7. Do NOT auto-increment spec version — Dave decides when to update spec post-critique
8. Skill files live at `brainframe-comms/skills/critique-spec/` (SKILL.md + prompts/)

## Non-Goals
- General research (use perplexity-pro-research-prompt-skill)
- Replacing Dave's judgment on design decisions
- Auto-resolving disagreements between the two AIs

## Constraints / Assumptions
- GPT-4o and Perplexity sonar-pro both required — neither alone is sufficient coverage
- Perplexity key: in REGISTRY.md (brainframe-comms)
- gpt-critique-skill is being retired — critique-spec skill replaces it for all spec critique workflows
- Retirement of gpt-critique-skill requires Dave to delete from skills provisioning repo (source TBD — OQ-003)

## Open Questions
| ID | Question | Owner |
|----|----------|-------|
| OQ-001 | Full critique output: `brainframe-comms/specs/{project}/critiques/` confirmed as path? | Dave |
| OQ-002 | Which repo contains gpt-critique-skill that needs to be deleted for retirement? | Dave |
| OQ-003 | Should critique summary be appended to the spec file itself, or kept separate only? | Dave |

## Dependencies
- critique-spec skill (`brainframe-comms/skills/critique-spec/SKILL.md`)
- spec-writing skill — triggers this pipeline on spec creation
- GPT-4o API (via ChatGPT or direct)
- Perplexity sonar-pro (key in brainframe-comms REGISTRY.md)
- GitHub API — for fetching spec and writing critique output

## Flows / Design Notes
Trigger → confirm spec → fetch from comms → GPT-4o critique → Perplexity critique → compare → surface summary to Dave → save full output → offer spec update. Never auto-update spec.

## Related Docs
- `brainframe-comms/skills/critique-spec/SKILL.md`
- Replaces: gpt-critique-skill (retirement pending)
