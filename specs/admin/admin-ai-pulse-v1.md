# Spec: AI Pulse Pipeline
Project: Admin
Version: v2
Status: ACTIVE
Upgrade ref: N/A (skill-based)
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Dave needs a structured daily intelligence feed on AI developments across 60+ curated sources. Ad-hoc searching misses signals; unstructured feeds create noise. AI Pulse is a triggered skill that runs a structured scan and surfaces only what matters — ranked by signal strength, not recency.

## Users / Use Cases
- Dave — daily AI signal review, tool discovery, competitive intel
- Triggered manually only; never runs automatically

## Success Metrics
- Every AI Pulse run produces a structured report in the standard 5-section format
- Every run creates a run log entry (timestamp + sources swept) — enables verifiability
- New sources discovered during scans are surfaced for addition to ai-pulse-sources.md
- Future Intel flagging offered once per run maximum

## Requirements
1. Trigger phrases: "ai pulse", "daily report", "what's new in AI", "scan sources", "update me on AI", "check the sources", "any AI news"
2. Step 1: Load `brainframe-public/skills/ai-pulse-sources.md` — authoritative source registry
3. Step 2: Web search sweep — Critical (🔴) sources first, then High (🟠) if time allows. Web search tool required — if unavailable, surface error and stop.
4. Step 3: Output report in 5-section format: CRITICAL HITS / RESEARCH SIGNAL / BUILDER BUZZ / COMMUNITY CHATTER / ONE INSIGHT. Max 800 words total. Hard cap.
5. Step 4: Surface NEW SOURCES FOUND section — only sources that pass the signal bar (see Signal Rubric below)
6. Step 5: Offer to flag high-signal items to FUTURE_INTEL.md — once per run, not per item. Do not repeat offer.
7. Step 6: Write run log entry to memory (timestamp, sources swept count, Critical hits count)
8. Source priority tiers: 🔴 Critical (always sweep), 🟠 High (sweep if time), 🟡 Medium (on request only)

## Signal Rubric
Item qualifies as high-signal (Critical Hit) if it meets at least one:
- New model release or capability announcement from a primary lab (Anthropic, OpenAI, Google DeepMind, Meta AI, Mistral)
- API breaking change or pricing shift affecting Dave's projects
- New tool or framework with >500 GitHub stars in past 7 days
- Research paper with a benchmark SOTA claim in a domain Dave uses

Item qualifies for NEW SOURCES FOUND if:
- Published by a known researcher, lab, or practitioner not yet in ai-pulse-sources.md
- Has produced 3+ high-signal items in the past 30 days (ASSUMED — verify via scan history)

## Non-Goals
- Auto-running on a schedule
- Replacing full research — signal detection only
- Generating content for publication

## Constraints / Assumptions
- Source list in `brainframe-public/skills/ai-pulse-sources.md` is authoritative — do not improvise
- Skill file at `brainframe-public/skills/ai-pulse.md` defines report format — use verbatim
- future-intel skill load is a required step before offering FUTURE_INTEL flag — not optional
- 800-word cap is a hard ceiling — truncate lower-priority sections first (COMMUNITY CHATTER, then BUILDER BUZZ)

## Open Questions
| ID | Question | Resolution |
|----|----------|------------|
| OQ-001 | Auto-write to FUTURE_INTEL.md without asking? | RESOLVED: Offer once per run. Never auto-write. |
| OQ-002 | Maximum report length? | RESOLVED: 800 words hard cap. |

## Dependencies
- `brainframe-public/skills/ai-pulse-sources.md` — source registry
- `brainframe-public/skills/ai-pulse.md` — report format
- future-intel skill — required before offering FUTURE_INTEL flag
- Web search tool — required; stop if unavailable

## Related Docs
- `brainframe-public/skills/ai-pulse.md`
- `brainframe-public/skills/ai-pulse-sources.md`
- `brainframe-public/skills/future-intel.md`
