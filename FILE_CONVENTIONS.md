# FILE_CONVENTIONS.md
Brainframe v2.0
Load on demand.

---

## FILE SIZE LIMITS

| File | Limit | Action when hit |
|---|---|---|
| brainfile.md | 500 words | Architecture is wrong. Trim immediately. |
| MASTER.md | 3000 words | Archive + new version |
| SESSION_LOG.md | 5000 words | Archive entries older than 90 days |
| DECISIONS.md | 5000 words | Archive entries older than 180 days |
| Any spec file | 2000 words | Split into sub-files |
| GLOBAL_RULES.md | 4000 words | Review and consolidate |
| ANTI_PATTERNS.md | 3000 words | Archive oldest confirmed entries |

AI must flag when any file approaches 80% of its limit.

---

## FILE NAMING

- All Brainframe system files: UPPERCASE.md
- Project-specific files: lowercase.md
- Spec files: descriptive-name.md (lowercase, hyphens)
- Archive files: original-name_YYYY-MM-DD.md
- Never use spaces in filenames

---

## VERSIONING

- When a file hits its size limit: archive current version, start new version
- Archive naming: DECISIONS_2026-03-15.md
- New version references its archive: "See /archive/ for entries before YYYY-MM-DD"
- Brainfile versioning: brainfile_v1.md, brainfile_v2.md when rules change significantly

---

## APPEND-ONLY FILES

These files are never rewritten — only appended:
- SESSION_LOG.md
- DECISIONS.md
- ANTI_PATTERNS.md
- PROMPT_LOG.md

New entries go at the bottom. Never edit existing entries — only supersede them using the SUPERSEDED status.

---

## SESSION END PROTOCOL

Every AI must follow this sequence at session end:

1. Generate session summary using `summarize session` format
2. List all files that need updating
3. List all decisions made this session
4. List all unresolved questions
5. Update HEALTH_CHECK.md
6. Propose Make commit payload for Brainframe file updates
7. Flag any files approaching size limits

Dave reviews and approves the commit payload before Make stages it.

---

## MAKE COMMIT PAYLOAD FORMAT

At session end, AI generates a structured payload:

```
## BRAINFRAME UPDATE — [date]

Files to update:
- [filename]: [what changed]

New entries:
- [file] → [entry ID]: [one-line summary]

Status changes:
- [entry ID]: [old status] → [new status]

Proposed branch: brainframe-update-[YYYY-MM-DD]
```

Dave approves → Make stages → Dave merges to main → GitHub Actions syncs to project repos.

---

## MANUAL FALLBACK

If Make is unavailable:
1. AI generates the file content as a copyable block
2. Dave copies and pastes into the correct file
3. Dave commits manually
4. Log the manual update in SESSION_LOG.md

---

## FILE DEPENDENCY MAP (GLOBAL)

```
brainfile.md
  → GLOBAL_RULES.md (public repo)
  → STYLE_RULES.md (public repo)
  → MODEL_ROUTING.md (public repo)
  → MASTER.md (project)
  → DECISIONS.md (project)
  → KNOWN_UNKNOWNS.md (project)
  → HEALTH_CHECK.md (project)
  → SESSION_LOG.md (project)
  → ANTI_PATTERNS.md (public repo, on demand)
  → ENTRY_SCHEMAS.md (public repo, on demand)
  → FILE_CONVENTIONS.md (public repo, on demand)
  → /specs/*.md (project, on demand)
  → /archive/ (project, on demand)
```
