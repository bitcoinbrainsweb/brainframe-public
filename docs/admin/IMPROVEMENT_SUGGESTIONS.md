# Brainframe Improvement Suggestions
Weekly self-improvement review log.

---

## Week of 2026-04-08 -- Sunday Review

| # | Pattern Observed | Proposed Change | Effort |
|---|-----------------|-----------------|--------|
| 1 | Cross-project contamination discovered 2026-04-08 (docs/admin/ sync pollution in coinbeast/nightwatch) requiring manual cleanup across 4 repos | Add SYNC_CONTAMINATION_CHECK to session boot sequence - scan for unexpected brainframe-public mirror files in project repos before starting work | Medium |
| 2 | Multiple quitchat skill updates (v1.1 on 2026-04-08) and project-specific quitchat variants (quitchat-nightwatch, quitchat-axiom) indicate context switching friction | Build universal quitchat-router skill that detects current project context and auto-selects appropriate quitchat variant without Dave specifying | High |
| 3 | Repeated "Next Session First Action" truncation in ADMIN_STATE.md (ends mid-sentence "Write Curs") suggests 6000 char limit hitting critical content | Move ADMIN_STATE.md "Next Session First Action" to dedicated NEXT_ACTION.md file, keep ADMIN_STATE.md under 4000 chars | Low |
| 4 | PAT/credentials scattered across sessions - PAT moved to CREDENTIALS section 2026-04-08, then PAT_REGISTRY.md created same day, Perplexity API key noted dead | Consolidate all credential references into single CREDENTIAL_STATUS skill that checks/reports all API key states and locations in one command | Medium |
| 5 | Skill promotion workflow requires manual "Dave to action" steps (30 updated skills pending install 2026-04-07, skill-installer created but not automated 2026-04-08) | Integrate skill-installer into PROMOTION_LOG.md writes - auto-generate installation commands when skills promoted, eliminate manual tracking | High |

Generated: 2026-04-08

---
## 2026-04-10 — PROCESS_FIX
Source: quitchat-close Phase 1 — promotions written without asking Dave
Finding: Promotions were auto-applied to GLOBAL_RULES and PROMOTION_LOG without surfacing to Dave via quiz first. Spec says all changes require approval.
Proposed fix: quitchat-close must add every promotion candidate to the fix quiz before writing. No promotion writes without explicit Yes.
Status: NEEDS_SPEC_UPDATE — update admin-quitchat-v2.md Phase 1 to enforce quiz gate on promotions.

## 2026-04-11 — PROCESS_FIX
Source: [Exchange ~85]: Dave said "I don't add things to files like that" re: VITE_BITQUERY_API_KEY
Finding: Claude asked Dave to manually add env var to .env, then failed via MCP, then wrote a confusing prompt
Proposed fix: Add rule to Mamba Mode project instructions — env var management is always Claude's job. Attempt Base44 MCP first; if unavailable surface exact Base44 UI path and confirm done before proceeding.
Status: DEFERRED

## 2026-04-11 — SKILL_FIX
Source: [Exchange ~2]: Dave said "You don't need the video intel skill. I just told you what the video is about."
Finding: Claude loaded video-intel skill on a verbal description of a reel, not a URL
Proposed fix: video-intel skill description should explicitly state it only triggers on a pasted URL (instagram.com/reel, youtube.com/watch, etc.) — NOT on verbal references to video content.
Status: DEFERRED

## 2026-04-11 — INSTRUCTION_FIX
Source: [Exchange ~90]: Dave said "I don't want this kind of micro lesson. not trying to learn technical stuff that you handle."
Finding: Claude appended a technical micro-lesson after delivering a Cursor prompt
Proposed fix: Suppress micro-lesson skill for Mamba Mode — micro-lessons apply to learning contexts, not to sessions where Claude is the implementer and Dave is the decision-maker.
Status: DEFERRED
