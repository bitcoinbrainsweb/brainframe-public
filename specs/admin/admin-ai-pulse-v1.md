# Spec: AI Pulse Pipeline
Project: Admin
Version: v1
Status: ACTIVE
Upgrade ref: N/A (skill-based, not a Cursor upgrade)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Dave needs a structured daily intelligence feed on AI developments across 60+ curated sources. Ad-hoc searching misses signals; unstructured feeds create noise. AI Pulse is a triggered skill that runs a structured scan and surfaces only what matters — ranked by signal strength, not recency.

## Users / Use Cases
- Dave — daily AI signal review, tool discovery, competitive intel for all projects
- Triggered manually; never runs automatically

## Success Metrics
- Every AI Pulse run produces a structured report in the standard 5-section format
- No Critical Hit (model release, API change, pricing shift) is missed within 48h of publication
- New sources discovered during scans are surfaced for addition to ai-pulse-sources.md
- Future Intel flagging works: high-signal items auto-offered for FUTURE_INTEL.md write

## Requirements
1. Trigger phrases: "ai pulse", "daily report", "what's new in AI", "scan sources", "update me on AI", "check the sources", "any AI news"
2. Step 1: Load `brainframe-public/skills/ai-pulse-sources.md` — 64+ sources, 7 categories
3. Step 2: Web search sweep — Critical (🔴) sources first, then High (🟠) if time allows
4. Step 3: Output report in exact 5-section format: CRITICAL HITS / RESEARCH SIGNAL / BUILDER BUZZ / COMMUNITY CHATTER / ONE INSIGHT
5. Step 4: Surface NEW SOURCES FOUND section — suggest adding to ai-pulse-sources.md
6. Step 5: Offer to flag high-signal items to FUTURE_INTEL.md via future-intel skill
7. Source categories: Primary Labs, Newsletters, Researchers, Reddit, GitHub, Academic, Podcasts
8. Priority tiers: 🔴 Critical (always sweep), 🟠 High (sweep if time), 🟡 Medium (on request)

## Non-Goals
- Auto-running on a schedule (Dave triggers manually)
- Replacing full research — this is signal detection, not deep analysis
- Generating content for publication

## Constraints / Assumptions
- Source list in `brainframe-public/skills/ai-pulse-sources.md` is the authoritative registry — do not improvise sources
- Skill file at `brainframe-public/skills/ai-pulse.md` defines the exact report format — use it verbatim
- Web search tool required — no skill run without it
- future-intel skill must be loaded separately if flagging to FUTURE_INTEL.md

## Open Questions
| ID | Question | Owner |
|----|----------|-------|
| OQ-001 | Should AI Pulse auto-write flagged items to FUTURE_INTEL.md without asking, or always prompt Dave? | Dave |
| OQ-002 | Is there a maximum report length? Long reports risk losing Dave in noise. | Dave |

## Dependencies
- `brainframe-public/skills/ai-pulse-sources.md` — source registry (must be loaded each run)
- `brainframe-public/skills/ai-pulse.md` — report format definition
- future-intel skill — downstream for flagged items
- Web search tool — required for every run

## Flows / Design Notes
Trigger → load sources → sweep Critical tier → sweep High tier → fill report template → surface report → offer FUTURE_INTEL writes → done. No state written unless Dave confirms a flag.

## Related Docs
- `brainframe-public/skills/ai-pulse.md`
- `brainframe-public/skills/ai-pulse-sources.md`
- `brainframe-public/skills/future-intel.md`
