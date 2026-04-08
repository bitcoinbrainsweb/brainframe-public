# ADMIN_LOG.md
Append-only. Never overwrite.

---

## Session 1 — 2026-04-05
AI: Claude Sonnet 4.6
Tasks: AI Pulse skill built and packaged. Source list (64+ sources, 7 categories) created and pushed to brainframe-public. Daily report run. 4 new sources added. Project instructions rewritten. CLAUDE.md written and pushed to brainframe-public. Inter-project message bus wired via DECISIONS.md. Nightwatch onboarding guide received. Brainframe best-practices audit completed. ENTRY_SCHEMAS, FILE_CONVENTIONS, INFRA_PATTERNS read and adopted.
Files created: skills/ai-pulse.md, skills/ai-pulse-sources.md, CLAUDE.md (brainframe-public)
Decisions: AI Pulse confirmed. Cursor (not Claude Code) confirmed. DECISIONS.md as canonical bus confirmed.
Open items carried forward: OI-001 through OI-005 (see ADMIN_STATE.md)
## 2026-04-07 — Skills Library Overhaul + Token Optimization Plan

### Completed
- Full 30-skill library audit and overhaul
- All YAML frontmatter fixed: >- block scalar descriptions, version field removed, 11 inner-quote bugs resolved
- All skills validated clean through YAML parser
- 6 global skills had project-specific content extracted to brainframe-public reference files
- 5 oversized skill bodies trimmed 53-82% (nw-orchestrator, nw-prompts, roadmap-planner, nw-site-audit, axiom-health)
- Reference files pushed: nwo-stages, nwp-detail, nwsa-phases, axiom-health-checks, nightwatch-roadmap-config (extended)
- 5 additional global skills cleaned: adr, brainstorming, systematic-debugging, technical-writing, quitchat
- quitchat refactored: project detection → fetch close procedure from brainframe-public
- new `ux` skill created (renamed from nightwatch-ux, general + reference file)
- nightwatch-ux-config.md pushed to brainframe-public
- skill-creator skill extended with Brainframe Standards section + brainframe-skill-standards.md reference
- SKILLS_RESEARCH.md updated with YAML frontmatter definitive reference
- TOKEN_OPTIMIZATION_PLAN.md v1.0 written and pushed (6 tiers)
- Gmail/Drive MCP restriction added to GLOBAL_RULES (rules 132-134) — from prior session

### Decisions Made
- All skill descriptions use >- block scalar — no exceptions
- version field banned from all skill frontmatter
- Global skills must be project-agnostic — project config in reference files
- disable-model-invocation on 4 skills: quitchat, axiom-close, axiom-health, nightwatch-site-audit
- nightwatch-ux renamed to ux — general skill, Nightwatch config in reference file
- frontend-design: keep user version (control over updates), not Anthropic public version
- ubiquitous-language and prd-to-plan: keep both, start using prd-to-plan
- Token plan: MCP session matching, no manual edits during session, batch questions, keep sessions alive

### Files Changed (brainframe-public/references/)
nightwatch-entities, nightwatch-review-rules, nightwatch-ux-config, nightwatch-roadmap-config,
nightwatch-config, nightwatch-adr-context, nightwatch-brainstorming-context, nightwatch-writing-context,
axiom-research-context, quitchat-nightwatch, quitchat-axiom, brainframe-skill-standards,
nwo-stages, nwp-detail, nwsa-phases, axiom-health-checks

### Pending (Dave to action)
- Install 30 updated SKILL.md files
- Install new ux skill, remove nightwatch-ux
- Install skill-creator skill
- Compress project instructions (Nightwatch first)

## 2026-04-08 — Cross-project best practices audit
- BEST_PRACTICES.md v3.0 synthesized from all global files + 30 skills, pushed to brainframe-public
- Deleted: DIAGNOSTIC_PLAYBOOK.md, MODEL_ROUTING.md, docs/token-optimization/TOKEN_OPTIMIZATION_PLAN.md
- Section 18 fixed (open items → pointer to ADMIN_STATE.md)
- Nightwatch: brainframe sync refreshed, 215 pre-NW-200 artifacts archived, roadmap v13 deleted
- Mambamode: brainframe/ bootstrapped (10 files), CLAUDE.md fixed, CI scaffold added
- Axiom: MODEL_ROUTING removed, BEST_PRACTICES/TOOL_ROLES/DECISIONS/PROMOTION_LOG added, GATE added to .cursorrules, CI scaffold added, CLAUDE.md fixed
- Coinbeast: .cursorrules created (CB-UPGRADE-XXX), CI scaffold added, CLAUDE.md fixed
- Winston: brainframe/ bootstrapped (13 files), CLAUDE.md fixed + boot sequence, .cursorrules created (WN-UPGRADE-XXX), CI scaffold, AGENT_REGISTRY created
- Web: deferred — dormant
- Fintrac: skipped — static info repo, no dev infrastructure needed

---
## 2026-04-08 — Perplexity skill research + instruction rebuild

**Summary:** Researched best practices for Claude project instructions via Perplexity Computer. Updated perplexity-research.md skill with copyable prompt rule and key research findings. Rebuilt project instructions: PAT now in CREDENTIALS section, full repo list explicit, bloat removed.

**Decisions:**
- CONFIRMED: All Perplexity prompts must be delivered in one-click copyable widget
- CONFIRMED: PAT lives in project instructions field, not chat history
- PROVISIONAL: project-instructions skill to be built next session

**Promoted:** perplexity-research.md skill, project-instructions.md
