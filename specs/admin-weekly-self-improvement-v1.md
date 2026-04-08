# Spec: Weekly Brainframe Self-Improvement Review
Project: Admin
Version: v1
Status: ACTIVE
Upgrade ref: N/A
Created: 2026-04-08
Last updated: 2026-04-08

---

## Problem Statement
Claude sessions improve based on in-session feedback only. No mechanism exists to review patterns across sessions and surface systemic workflow improvements. Brainframe setup never evolves without manual intervention from Dave.

## Users / Use Cases
- Dave: receives a weekly suggested improvement list without having to think about it
- Brainframe system: self-improving setup that compounds over time

## Success Metrics
- At least one actionable improvement suggestion surfaced per week
- Suggestions are grounded in actual ADMIN_LOG.md patterns, not generic advice
- Dave can apply suggestions in under 5 minutes

## Requirements
1. Scheduled task runs every Sunday at 4pm MT
2. Reads ADMIN_LOG.md from brainframe-public via GitHub API
3. Reads ADMIN_STATE.md for current open items and project context
4. Identifies recurring friction patterns: repeated errors, repeated re-explanations, tasks that took multiple attempts, skipped rules, fallback-to-memory incidents
5. Outputs a structured improvement suggestion file (IMPROVEMENT_SUGGESTIONS.md) appended to brainframe-public/docs/admin/
6. Suggestions are specific: target a named rule, skill, file, or workflow — never generic advice
7. Each suggestion includes: pattern observed, proposed change, effort estimate (low/medium/high)
8. Maximum 5 suggestions per week — prioritized by impact

## Non-Goals
- Does not auto-apply any changes — suggestions only, Dave approves
- Does not read project repos (Nightwatch, Axiom, etc.) — admin layer only
- Does not replace quitchat or session discipline

## Constraints / Assumptions
- ADMIN_LOG.md is the primary signal source — quality of suggestions depends on log quality
- Scheduled tasks in Claude.ai have access to tools (GitHub API via bash) — ASSUMED
- Sunday 4pm MT cadence

## Open Questions
- OQ-001: Does Claude.ai scheduled tasks support bash/GitHub API tool calls, or is it prompt-only?
- OQ-002: Should suggestions be appended to a rolling file or create a new dated file per week?

## Dependencies
- ADMIN_LOG.md (brainframe-public/docs/admin/) — must be consistently written at quitchat
- ADMIN_STATE.md (brainframe-public/docs/admin/) — current project state

## Flows / Design Notes
1. Task fires Sunday 4pm
2. Fetch ADMIN_LOG.md → scan last 7 days of entries
3. Fetch ADMIN_STATE.md → load current context
4. Identify top friction patterns
5. Write IMPROVEMENT_SUGGESTIONS.md with dated entry
6. Done — Dave reviews Monday morning

## Related Docs
- brainframe-public/docs/admin/ADMIN_LOG.md
- brainframe-public/docs/admin/ADMIN_STATE.md
- GLOBAL_RULES.md (improvement suggestions should target rules violations specifically)
