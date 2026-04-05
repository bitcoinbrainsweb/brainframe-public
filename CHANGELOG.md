# CHANGELOG.md
Brainframe version history. Append-only.

---

## v2.0 — 2026-03-15

### What changed
- Moved from flat file system to typed context categories
- Added global/ directory (brainframe-public repo) separating universal rules from project state
- Added ANTI_PATTERNS.md as first-class memory category
- Added standard entry schema: What / Why / How to apply / Status / Superseded by / Review by / Date / Source
- Added STYLE_RULES.md for tone and formatting preferences
- Added MODEL_ROUTING.md as global file with explicit tool roles and handoff formats
- Added FILE_CONVENTIONS.md with size limits, naming conventions, session end protocol, Make payload format
- Added ENTRY_SCHEMAS.md with versioned schemas for all entry types
- Added Superseded by field to decisions and anti-patterns
- Added schema version field to all entries
- Added rule priority order: Dave decision > project rules > global rules > tool defaults
- Added clarification vs action protocol replacing ambiguous questioning rule
- Added dependency gate rule — steps blocked on unverified prerequisites
- Added upgrade closeout rule — no upgrade closed without artifacts and verified gate status
- Added cross-project contamination rule — rules stay project-scoped until Dave promotes them
- Added temporary state rule — all temporary states require removal or replacement trigger
- Added Make authority clarification — staging only, never commit/merge/deploy
- Added protocol refresh failure handling — continue on last confirmed rule state, never assume missing rules
- Brainframe treats itself as a project in brainframe-private/projects/brainframe/
- Four-repo architecture confirmed: brainframe-public, brainframe-private, coinbeast, nightwatch
- GitHub Actions sync: brainframe-public → project repos on merge to main

### Why
V1 was directionally correct but too generic. Typed memory, explicit reasoning, global separation, and deterministic conflict resolution make the system reliable across multiple AI tools and long-running projects.

### What did not change
- Brainfile remains a loader only — under 500 words
- Append-only files remain append-only
- Command system unchanged
- Known unknowns remains a permanent category
- Dave-only taxonomy governance unchanged
- Dave approves all irreversible actions

---

## v1.0 — 2026-03-15

Initial Brainframe MVP. Flat file structure. Eight core files.
Solved context loss, file bloat, and discipline failure at basic level.
Built during initial Coinbeast planning session with Claude.


## v2.1 — 2026-04-05

### What changed
- Added `templates/NEW_PROJECT_ONBOARDING.md` — single prompt that bootstraps any new project from zero: reads all 14 brainframe files, processes DECISIONS.md messages, creates three-layer state files, creates AGENT_REGISTRY.md, drafts project instructions, confirms via DECISIONS.md. Replaces ad-hoc onboarding.
- Added `templates/PROJECT_INSTRUCTIONS_TEMPLATE.md` — canonical structure for Claude project instructions. All projects should align to this structure. Includes DECISIONS.md boot step, brainframe-public PAT reference, verification gate with new-decisions reporting.
- DECISIONS.md boot step is now mandatory in all project session-start sequences. Projects that do not read DECISIONS.md at session start will miss global decisions. Update project instructions to add this step.
- Identified gap: SETUP_INSTRUCTIONS.md references stale Make.com workflow — no longer accurate. Retained for historical context but do not follow.

### Why
Mamba onboarding revealed friction: new projects had to discover DECISIONS.md as the message bus through trial and error, no standard project instructions structure existed, and best practices propagated only when a project happened to check in.

### What did not change
- Three-layer state split unchanged (STATE/LOG/CONFIG)
- DECISIONS.md as the only message bus unchanged
- Promotion workflow unchanged
- All 14 brainframe files remain authoritative
