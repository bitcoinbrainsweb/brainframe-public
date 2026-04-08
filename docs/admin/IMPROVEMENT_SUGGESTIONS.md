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
