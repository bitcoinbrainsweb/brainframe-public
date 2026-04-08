# Spec: Critique-Spec Pipeline
Project: Admin
Version: v2
Status: ACTIVE
Upgrade ref: N/A (skill-based)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Feature specs written by a single AI have blind spots. A two-AI sequential critique (GPT-4o then Perplexity sonar-pro) stress-tests specs before Cursor implements them. This spec defines the pipeline contract so the workflow is auditable and extensible.

## Users / Use Cases
- Dave — triggers critique on any spec before implementation
- spec-writing skill — auto-triggers critique after every new spec creation

## Success Metrics
- Every new spec receives a critique before a Cursor prompt is written
- Disagreements between GPT-4o and Perplexity explicitly flagged — never silently resolved
- Open questions surfaced by critique added as OQ-XXX entries back to the spec
- Full critique persisted to `brainframe-comms/specs/{project}/critiques/` for audit trail
- Version gate: critique always runs against the current spec version (no stale critiques)

## Requirements
1. Step 0 (version gate): fetch spec from comms, confirm version matches Dave's expectation before firing
2. Trigger: "critique spec" OR spec-writing skill auto-triggers on new spec creation
3. Dave confirms which spec before firing (if manually triggered)
4. Sequential: GPT-4o first, then Perplexity sonar-pro — using prompt templates in `brainframe-comms/skills/critique-spec/prompts/`
5. Spec fetched from `brainframe-comms/specs/{project}/` — always source of truth, never mirror
6. Surface to Dave: summary only — top 2-3 issues, OQs flagged, disagreements between models
7. Save full critique: `brainframe-comms/specs/{project}/critiques/{spec-slug}-critique-{YYYY-MM-DD}.md`
8. Spec update that follows a critique must reference the critique filename in the commit message
9. Do NOT auto-increment spec version — Dave decides
10. gpt-critique-skill: retired — do not use for spec critique

## Non-Goals
- General research (use perplexity-pro-research-prompt-skill)
- Replacing Dave's judgment
- Auto-resolving AI disagreements

## Constraints / Assumptions
- GPT-4o and Perplexity sonar-pro both required — Claude adversarial critique is the fallback if Perplexity quota is exhausted
- GPT-4o key: `brainframe-comms/_docs/REGISTRY.md` under "## OpenAI"
- Perplexity key: `brainframe-comms/_docs/REGISTRY.md` under "## Perplexity"
- Critique runs via API from bash_tool — no manual copy-paste required
- Prompt templates: `brainframe-comms/skills/critique-spec/prompts/gpt-critique-prompt.md` and `perplexity-critique-prompt.md`

## Open Questions
| ID | Question | Resolution |
|----|----------|------------|
| OQ-001 | Critique output path | RESOLVED: `brainframe-comms/specs/{project}/critiques/` |
| OQ-002 | gpt-critique-skill retirement repo | RESOLVED: Retired in place — skill file exists but workflow replaced by critique-spec skill. Dave to delete skill file from skills provisioning if desired. |
| OQ-003 | Critique summary: append to spec or keep separate? | RESOLVED: Keep separate in critiques/. Spec commit message must reference critique filename. |

## Dependencies
- `brainframe-comms/skills/critique-spec/SKILL.md`
- `brainframe-comms/skills/critique-spec/prompts/` — prompt templates
- GPT-4o API (key in REGISTRY.md)
- Perplexity sonar-pro (key in REGISTRY.md)
- spec-writing skill — triggers this pipeline on spec creation

## Related Docs
- `brainframe-comms/skills/critique-spec/SKILL.md`
- `brainframe-comms/_docs/REGISTRY.md`
