---
name: quitchat
description: >-
  Closes any project session: sweeps unsaved context, updates tracking files, audits memory, produces handoff file. Run ONLY when Dave types quitchat or run quitchat. Never infer from wrap up or new chat. Works for any project.
---
# Quitchat Skill
Version: 3.1 | 2026-04-09

Run only on explicit `quitchat` or `run quitchat`. Never infer.

---

## PROJECT DETECTION

Scan conversation context for project signals:
- **Nightwatch** — NW-UPGRADE-XXX, Base44, Amanda, AVLM, great-horn-aml-nightwatch
- **Axiom** — AX-UPGRADE-XXX, axiom, pattern library, JAI/DAI, bitcoinbrainsweb/axiom
- **Admin** — brainframe-public, admin session, no project-specific signals

If ambiguous: ask Dave which project before proceeding.

Once detected, fetch the project close procedure:
- Nightwatch: `https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/references/quitchat-nightwatch.md`
- Axiom: `https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/references/quitchat-axiom.md`
- Admin/other: use UNIVERSAL STEPS only

---

## TIER SELECTION — AUTO

**Full close** if ANY: 3+ upgrades merged, roadmap changed, arch decisions made,
skills/instructions changed, session 20+ exchanges.
**Fast close** otherwise.

State tier before proceeding.

---

## UNIVERSAL STEPS (all projects, all tiers)

These run regardless of project. Project-specific steps are in the reference file.

---

### PHASE 0 — DELIVERABLE SCAN (mandatory, runs first, every close)

Scan the **entire conversation** — every message, every tool output — and produce a checklist. Nothing leaves this step unclassified.

For each item found, assign one of:
- `SAVED` — written to GitHub, outputted via present_files, or confirmed persisted this session
- `NEEDS SAVE` — created or decided this session, not yet persisted
- `NEEDS SPEC` — a feature or decision with no spec written
- `NEEDS PROMPT` — a Cursor prompt discussed but not finalized or run
- `NEEDS TRACKING` — a bug, open question, or action item not in any state file
- `FLAGGED` — something Dave needs to decide before this chat can close

Categories to scan for explicitly:
- Files created or modified (specs, prompts, docs, skills, state files)
- Decisions made (architectural, tooling, naming, process)
- Upgrades discussed or planned
- Cursor prompts written, drafted, or referenced
- Specs written, updated, or needed
- Bugs identified
- Open questions raised and not resolved
- Action items assigned to Dave, Amanda, or others
- Memory changes made or needed
- Skills created or updated — packaged and installed?
- Any deliverable Dave asked for — delivered?

Output format:
```
DELIVERABLE SCAN
─────────────────────────────────────────
[SAVED]          Item description
[NEEDS SAVE]     Item description → route to: [file/repo]
[NEEDS SPEC]     Item description → trigger spec-writing skill
[NEEDS PROMPT]   Item description → needs Cursor prompt before implementation
[NEEDS TRACKING] Item description → add to ADMIN_STATE.md / roadmap
[FLAGGED]        Item description → Dave must decide
─────────────────────────────────────────
Items requiring action before close: N
```

If N > 0: resolve each `NEEDS SAVE` and `NEEDS TRACKING` item now (automate where possible). Surface `FLAGGED` items to Dave one at a time. Only proceed to Phase 1 when all resolvable items are handled or explicitly deferred to handoff.

---

### PHASE 1 — UNSAVED CONTEXT SWEEP

After Deliverable Scan, confirm anything remaining:
- Decisions not persisted
- Bugs not tracked
- Features not in roadmap
- Prompts written but not run
- Merges done but state not updated

Each item: state it + where routed. Unresolvable → handoff.

---

### PHASE 2 — PROMOTION CANDIDATES (full close only)

Scan session for decisions, rules, or patterns that should apply globally.
1. Read PROMOTION_LOG.md from brainframe-public — check for same-day edits
2. If no conflict: commit directly to brainframe-public main via GitHub API
3. Append: `YYYY-MM-DD | [project] | [file] | [description]`
4. If conflict: stop, flag to Dave

---

### PHASE 3 — MEMORY AUDIT (every close)

Fetch all memory edits. Fix stale, duplicated, missing. Report: N reviewed / N changed.

---

### PHASE 4 — HANDOFF FILE (every close)

Produce `/mnt/user-data/outputs/SESSION_HANDOFF.md`. Self-contained.
Assume zero memory of session. Include: session summary, last completed,
next task, open decisions, first action next session, all unresolved deliverables from Phase 0.

**File delivery**
Present all output files via `present_files`.

---

## CHAT NAME — FINAL STEP

```
💬 Suggested chat name: [name]
```
- Max 5 words. Lead with project name (NW, Axiom, Admin).
- Capture the most important thing: decision, upgrade batch, feature shipped.
- No filler: "session", "work", "stuff".

---

## GLOBAL RULES

1. Never say "updated/pushed/saved" unless tool returned success.
2. Can't run a step → "SKIPPED — reason", continue.
3. Unresolved items go in handoff brief, never silently dropped.
4. All output files via `present_files`. No inline copy blocks.
5. Project-specific steps are in the reference file — always fetch before executing.
6. Phase 0 is non-negotiable. Never skip it. Never abbreviate it.
