# Quitchat — Axiom Close Procedure
*Fetched by quitchat skill when project is detected as Axiom.*

## Detection Signals
axiom, pattern library, AX-UPGRADE-XXX, JAI/DAI, bitcoinbrainsweb/axiom

## Fast close: Steps 2, 4, 6, 7
## Full close: All steps

**Step 1 — Chat sweep** (full only)
recent_chats(n=10) + read _docs/JAI_HANDOFF.md. State findings. SKIPPED if unavailable.

**Step 2 — Unsaved context sweep**
Scan for: decisions not persisted, pattern library changes not pushed, PROVISIONAL items
unconfirmed, prompts written not run, merges done but state not updated.

**Step 3 — GitHub file updates** (full only)
Repo: bitcoinbrainsweb/axiom
Write order — HANDOFF before build-log:
1. _docs/AGENT_HANDOFF.md
2. _docs/build-log.md — new entry (3-5 lines: Built / Decided / Open)
3. _docs/AGENT_TASKS.md — if tasks changed
4. _docs/axiom-roadmap.md — date bump + Next Build Priorities

**Step 4 — Promotion candidates** (full only)
Same protocol as Nightwatch. Read PROMOTION_LOG.md first, check for conflicts,
commit direct to brainframe-public main, append log entry.

**Step 5 — Memory audit**
Fetch all edits. Fix stale/duplicated/missing. Report: N reviewed / N changed.

**Step 6 — Skills + instructions check** (full only)
Check axiom-prompts, axiom-close, axiom-roadmap, perplexity skill, gpt skills.
If updates needed: produce files and present. Never ask Dave.

**Step 7 — Handoff file**
Produce /mnt/user-data/outputs/SESSION_HANDOFF.md. Self-contained.
Include: session summary, what built/decided, pattern library state, next priority,
open decisions, Johnny action items, first action next session.

**Step 8 — File delivery**
Present all output files via present_files.

## Audit Log Format
Tier: FAST / FULL — [signals]
Step 1: RAN / SKIPPED / [findings]
Step 2: [N found / N routed / N unresolved]
Step 3: RAN / SKIPPED / [files]
Step 4: [N promoted / NONE / CONFLICT — flagged]
Step 5: [N reviewed / N changed]
Step 6: RAN / SKIPPED / [result]
Step 7: READY
Step 8: [files listed]
