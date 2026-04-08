---
name: prompt-writing
description: >-
  Writes Cursor upgrade prompts for any project. MUST be loaded before writing any Cursor prompt or upgrade spec. Detects project, fetches project config from repo, applies universal prompt standards. Replaces prompt-writing and prompt-writing.
---


## SPEC GATE

Before writing any Cursor prompt for an upgrade:
1. Check `brainframe-comms/specs/{project}/` for a spec matching this upgrade ref.
2. If no spec exists → flag to Dave, offer to stub one. Do not proceed without spec unless Dave explicitly overrides.
3. If spec exists → include this block in the prompt:

```
## Spec Reference
File: specs/{filename}
Version: v{N}
Key constraints: [pull Requirements + Non-Goals + Constraints — 3-5 bullets]
Open questions (do not resolve — flag in RESULT): [OQ-XXX list]
```

# Prompt Writing Skill
Version: 1.2 | 2026-04-08

Writes Cursor prompts for any project. Detects project context, fetches project-specific
config, applies universal prompt standards.

---

## PROJECT DETECTION → FETCH CONFIG

Detect project from session context, then fetch:
- **Nightwatch** (NW-UPGRADE-XXX, Base44, Amanda, great-horn-aml):
  `https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/references/prompt-writing-config.md`
- **Axiom** (AX-UPGRADE-XXX, pattern library, JAI/DAI, bitcoinbrainsweb/axiom):
  `https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/references/prompt-writing-config.md` — also on Axiom repo at `_docs/prompt-writing-config.md`
- **Mambamode** (NE-UPGRADE-XXX, mambamode, mamba, balldontlie, odds-api):
  `https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-public/main/references/mambamode-prompts-config.md`
- **Other projects**: ask Dave for config file location

Fetch via GitHub API before writing any prompt.

---

## UNIVERSAL PROMPT STRUCTURE

Every prompt regardless of project:

```
[PROJECT] CURSOR PROMPT
[UPGRADE-ID] — [Title]
Version: 1.0

MODE: [ARCHITECT | IMPLEMENTER | REVIEWER | DEBUGGER]

Objective
[One sentence for simple; one paragraph for complex.]

Scope
[Exact file list. No wildcards.]

Do Not Modify
[Exact exclusions.]

BEFORE STARTING
git pull --rebase origin main
git checkout -b [UPGRADE-ID]
[Branch hard-stop check — see project config]

PLAN [MEDIUM and HIGH risk prompts only — omit for LOW]
Before writing any code, output a numbered step list with dependency tags:
  1. [step description] — depends on: none
  2. [step description] — depends on: step 1
  3. [step description] — depends on: steps 1, 2
Do not proceed to implementation until the PLAN block is complete.
If a dependency is unresolvable, stop and surface to Dave.

[Implementation steps]

BEFORE FINISHING
[Tests if applicable]
[Commit and push — see project config for PowerShell vs bash]
[RESULT file]
[State file update]
[HANDOFF block — sequential upgrades only, omit for standalone]

Branch: [UPGRADE-ID]
```

---

## UNIVERSAL RULES

**Scope discipline**
- Exact file list — no wildcards, no "and related files"
- Do Not Modify section is mandatory
- Scope creep found mid-execution → stop, write to RESULT, surface to Dave

**SANITYCHECK — every prompt**
- Produced as a file before any code is written
- Branch check is a hard stop — wrong branch = do not proceed
- Risk rating: LOW / MEDIUM / HIGH
- Rollback strategy required for MEDIUM and HIGH

**RESULT file — every prompt**
- Produced after git push completes — never before
- Status: PASS | PASS WITH NOTES | FAIL
- Files changed with descriptions
- Verification checklist

**Merge rules (all projects)**
- PASS → merge automatically via GitHub API
- PASS WITH NOTES → surface, ask Dave
- FAIL → do not merge

**State file update — every prompt**
Cursor must update the project state file at end of every prompt.
Fetch SHA immediately before writing — never use cached SHA.

**Never ask Dave to do anything a tool can do.**
Never deliver prompts as inline copy blocks — use present_files.

---

## KERNEL PRINCIPLES (apply to every prompt)

- Single clear objective — no multi-task combining
- Explicit constraints (Do Not Modify section)
- Narrow scope (exact files only)
- Explicit success criteria before Cursor starts
- Context blocks over 5 lines: challenge whether Cursor actually needs them

---

## MODE DEFINITIONS

Every prompt declares exactly one MODE. It constrains what Cursor is allowed to do.

| MODE | Allowed | Locked out |
|------|---------|------------|
| ARCHITECT | Analysis, design, file/folder planning | No code, no implementation order decisions |
| IMPLEMENTER | Write and modify code per spec | No scope creep, no refactoring outside ticket |
| REVIEWER | Read code, report issues | No fixes, no refactoring — report only |
| DEBUGGER | Root cause investigation and targeted fix | No new features, no unrelated refactoring |

Include this line immediately after the MODE declaration in every prompt:
```
Do not switch modes mid-execution. If scope requires a different mode, stop and surface to Dave.
```

---

## HANDOFF BLOCK

Include at the end of BEFORE FINISHING for sequential upgrades only. Omit for standalone upgrades.

Cursor writes this entry to DECISIONS.md via GitHub API before closing:

```
HANDOFF: [UPGRADE-ID] complete.
Changed: [key files / components touched]
Deferred: [anything explicitly out of scope that the next upgrade needs]
Blocked on: [any unresolved dependency]
Next prompt must fetch: [exact files next Cursor session needs as context]
```

Rule: next prompt in the sequence must open with:
```
Fetch DECISIONS.md. Read last HANDOFF entry. Proceed from deferred items.
```

---

## PROMPT OUTPUT RULES

- Every Cursor prompt delivered via present_files as a file
- Filename: [UPGRADE-ID].md
- One prompt per file
- Never summarize the prompt in chat — present the file, done
