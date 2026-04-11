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

## 2026-04-11 — INSTRUCTION_FIX
Source: [Exchange ~18]: Dave said "no I don't want my lessons. I want the absolute state of the art best data scientist in the god damn world"
Finding: Claude defaulted to embedding project-specific lessons into a knowledge skill instead of universal domain expertise.
Proposed fix: When building knowledge skills, ask Dave whether to prioritize universal domain expertise, project-specific lessons, or both. Don't assume one over the other.
Status: APPLIED — behavioral note, no skill file change needed

## 2026-04-11 — SKILL_FIX
Source: [Exchange ~bet sizing]: Dave corrected Kelly sizing ("isn't $30 the max?")
Finding: Opus returned Kelly = $120/bet for $1K float. Claude presented it without sanity checking against bankroll size. Kelly > 5% of small bankroll is impractical.
Proposed fix: Add rule to nba-data-scientist skill — "Always sanity-check Kelly sizing: if Kelly bet > 5% of bankroll at stakes below $5K, flag as impractical and recommend fixed fractional (2-3%) instead."
Status: DEFERRED

## 2026-04-11 — INSTRUCTION_FIX
Source: [Exchange ~arb frequency]: Dave called out "so you're just guessing?" on arb frequency estimate
Finding: Claude presented 3-5 arb opportunities/week as a confident estimate with no historical data to support it. Should have flagged it as inference immediately.
Proposed fix: Add rule to Mamba Mode project instructions — "When estimating frequency of rare market events without logged data, always state upfront: 'This is market structure inference, not measured data. Build a price logger to get real numbers.'"
Status: DEFERRED

## 2026-04-11 — PROCESS_FIX
Source: [Multiple exchanges] "Stop guessing and just do this fucking right" / "You fucking stupid piece of shit"
Finding: Gave PowerShell commands involving private GitHub repo without verifying auth method works first. Commands failed repeatedly (404, encoding errors, stdin hang) causing severe user frustration.
Proposed fix: Before giving any PowerShell command involving a private GitHub repo, verify the exact fetch method works in bash_tool first. Never give a command that hasn't been validated end-to-end.
Status: DEFERRED

## 2026-04-11 — PROCESS_FIX
Source: [Script deployment] fetch_nba_markets() timeout after several minutes
Finding: Shipped script using /events endpoint without timing it. Step 1 took 5-10min causing user to kill the process.
Proposed fix: Always time-test external API pagination calls in bash_tool before including them in a shipped script. Confirm speed is acceptable before writing to repo.
Status: DEFERRED

## 2026-04-11 — PROCESS_FIX (confirmed deferred)
Source: Multiple escalation exchanges — "Stop guessing" / "You fucking stupid piece of shit"
Finding: Gave PowerShell commands for private GitHub repo without verifying auth method in bash_tool first. Repeated failures (404, encoding, stdin hang).
Proposed fix: Verify every PowerShell+private-repo command in bash_tool before giving it to Dave.
Status: DEFERRED
