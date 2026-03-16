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
