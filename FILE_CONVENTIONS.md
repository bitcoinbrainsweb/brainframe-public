# FILE_CONVENTIONS.md
Brainframe v2.1
Load on demand.

---

## FILE SIZE LIMITS

| File | Limit | Action when hit |
|---|---|---|
| brainfile.md | 500 words | Architecture is wrong. Trim immediately. |
| MASTER.md | 3000 words | Archive + new version |
| SESSION_LOG.md | 5000 words | Archive entries older than 90 days |
| DECISIONS.md | 5000 words | Archive per policy below |
| Any spec file | 2000 words | Split into sub-files |
| GLOBAL_RULES.md | 4000 words | Review and consolidate |
| ANTI_PATTERNS.md | 3000 words | Archive oldest confirmed entries |

AI must flag when any file approaches 80% of its limit.

---

## DECISIONS.md ARCHIVE POLICY

DECISIONS.md has a hard 5000-word limit. When the file approaches 4000 words, archive immediately.

**What to archive (move to docs/archive/):**
- Inter-agent communication entries (Message to X, confirmations, first-contact entries)
- SUPERSEDED entries
- Entries where the decision is now fully codified in GLOBAL_RULES, INFRA_PATTERNS, or another canonical file

**What stays active:**
- Operative decisions not yet codified in a global file
- Decisions that projects actively need to reference
- The most recent broadcast/mandate entries (last 30 days)

**Archive file naming:** `docs/archive/DECISIONS-YYYY-Q#.md`
Q1 = Jan–Mar, Q2 = Apr–Jun, Q3 = Jul–Sep, Q4 = Oct–Dec

**Archive file header:**
```
# DECISIONS ARCHIVE — YYYY Q# (Mon–Mon)
Archived from DECISIONS.md on YYYY-MM-DD. Read-only. Do not append.
```

**After archiving:** Add one line at the top of active DECISIONS.md:
`<!-- Archived entries: docs/archive/DECISIONS-YYYY-Q#.md -->`

**Who archives:** Any Claude instance. Log to PROMOTION_LOG.md before writing.

---

## FILE NAMING

- All Brainframe system files: UPPERCASE.md
- Project-specific files: lowercase.md
- Spec files: descriptive-name.md (lowercase, hyphens)
- Archive files: ORIGINAL-NAME-YYYY-Q#.md
- Never use spaces in filenames

---

## VERSIONING

- When a file hits its size limit: archive current version, start new version
- New version references its archive: "See /archive/ for entries before YYYY-MM-DD"
- Brainfile versioning: brainfile_v1.md, brainfile_v2.md when rules change significantly

---

## APPEND-ONLY FILES

These files are never rewritten — only appended:
- SESSION_LOG.md
- DECISIONS.md
- ANTI_PATTERNS.md
- PROMOTION_LOG.md

New entries go at the bottom. Never edit existing entries — only supersede using SUPERSEDED status.
Exception: archival trimming of DECISIONS.md per policy above is permitted.

---

## SESSION END PROTOCOL

Every AI must follow this sequence at session end:

1. Check if DECISIONS.md is approaching 4000 words — archive if so
2. Check for globally applicable discoveries — promote to DECISIONS.md before closing (hard stop)
3. Update STATE file — overwrite with current working state
4. Append LOG entry — dated, what was completed, what was decided
5. Update HANDOFF files — fresh state for next agent
6. Build log entry — commit to docs/build-log/YYYY-MM-DD.md

---

## FILE DEPENDENCY MAP (GLOBAL)

```
SESSION START (fetch in order):
  GLOBAL_RULES.md        (brainframe-public)
  STYLE_RULES.md         (brainframe-public)
  [PROJECT]_CONFIG.md    (project repo)
  [PROJECT]_STATE.md     (project repo)
  HANDOFF_*.md           (project repo)
  DECISIONS.md           (brainframe-public — always from source, never local copy)

ON DEMAND:
  INFRA_PATTERNS.md
  COLLAB_RULES.md
  ENGINEERING_PRINCIPLES.md
  ANTI_PATTERNS.md
  ENTRY_SCHEMAS.md
  FILE_CONVENTIONS.md    (this file)
  MODEL_ROUTING.md
  AI_DEV_WORKFLOW.md
  ROLLBACK_PROTOCOL.md
  PROMOTION_WORKFLOW.md
  /specs/*.md
  /archive/
```
