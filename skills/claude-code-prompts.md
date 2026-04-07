---
name: agentic-code-prompts
description: "Use when writing prompts for Claude Code CLI to implement code upgrades autonomously. Covers mandatory prompt structure, pre-flight checks, push/log requirements, context management, and failure modes. ONLY for Claude Code CLI prompts — not for Cursor, GPT, Perplexity, or any other tool."
---

# Claude Code Prompt Writing Skill
Version: 1.3 | 2026-04-07

Write prompts that Claude Code CLI executes autonomously in a terminal. Claude (this chat) writes the prompt as a file. The user pastes it into the Claude Code terminal session.

---

## TRIGGER

Use this skill when the user says: "write a Claude Code prompt", "give me a prompt for Claude Code", or "queue this for Claude Code". Do NOT use for Cursor prompts, GPT prompts, or any other tool.

---

## MANDATORY STRUCTURE — every prompt must have all of these, in order

### 1. Header
```
# Claude Code — [UPGRADE IDs or task name]
Repo: [owner/repo-name]
```

### 2. Read First
List every file Claude Code must read before writing anything. Be exhaustive — missed reads cause overwrites of correct code.

```
Read these files before writing any code:
- [spec or task doc]
- [every source file that will be modified]
- [every hook, util, data file imported by target files]

Then run:
- ls src/  (or equivalent) to verify actual directory structure
- grep -r "import.*[ComponentName]" src/ to find all consumers of files you'll modify
```

Rationale: Claude Code has no session memory. If you don't list it, it won't read it. The discovery step catches dependencies that weren't listed explicitly.

### 3. Current State Description
For each file being modified, describe what currently exists. Pull from live repo reads — never assume. Prevents Claude Code from overwriting correct logic or duplicating what already exists.

### 4. Pre-Flight Checks (MANDATORY — runs before any implementation)
```
Before writing any code:
1. Run: git pull origin main  — sync any changes made via GitHub API or other agents since last local commit
2. Run: git branch --show-current  — confirm you are on the expected branch (should be main)
3. Run: git status  — confirm clean working tree after pull (no conflicts)
4. Verify every spec file listed in Read First actually exists — if any is missing, STOP and report which files are missing
5. Check if implementation already exists — search for key function/component names before creating them. If found, update rather than duplicate.
```

Rationale for git pull: Claude (claude.ai) may write files directly to the repo via GitHub API between Claude Code sessions. Without a pull, Claude Code works from a stale local copy and will overwrite those changes on next push.

### 5. Implementation Instructions
Per task:
- **Files to CREATE** — name + purpose
- **Files to MODIFY** — describe exactly what changes. Modify only the necessary sections — do not rewrite the entire file unless the spec explicitly requires it
- **Component contracts** — props, exports, what it renders
- **Data sources** — which API, hook, or entity
- **Fallback/error states** — required for every data fetch
- **Constraints** — what must not change, what must not be added

### 6. Mandatory Closing Block
Copy this verbatim into every prompt — never omit:

```
## When done

1. Verification before commit:
   - Run build/lint/tests if available (e.g. npm run build, npm run lint)
   - If errors exist, fix them before committing
   - If no build system exists, check line counts: `wc -l` on every modified file vs the original. If any file is >20% shorter than before and the spec didn't require deletions, STOP — output may be truncated. Do not commit.

2. Commit and push:
   git add .
   git commit -m "[descriptive message]"
   git push origin HEAD

3. Append to docs/build-log.md:
   ## [Task name] — YYYY-MM-DD
   **Completed:** [bullet list]
   **Files created:** [list]
   **Files modified:** [list]
   **Acceptance criteria not met:** [list or "None"]
   **Known issues:** [list or "None"]
   Then: git add docs/build-log.md && git commit -m "log: [task name] complete" && git push origin HEAD

4. Print a completion report to terminal:
   - Files created
   - Files modified
   - Acceptance criteria not met and why
   - Any import errors or runtime issues encountered
```

---

## CONTEXT WINDOW RULES

Claude Code's context degrades past ~70% fill. For large task queues:

- **Max 3 tasks per prompt** — more causes silent bail or degraded output
- **Order matters** — tasks execute sequentially; a blocked task stops everything after it
- **Spec files must exist before the prompt runs** — verify in the repo before writing the prompt
- **Large file reads up front** — list all reads at the top so they happen before context fills
- **No narrative filler** — every token counts; Claude Code doesn't need explanations it won't act on

---

## FAILURE MODES

| Symptom | Cause | Fix |
|---|---|---|
| Commits local, doesn't push | No push instruction | Add closing block |
| Doesn't write build log | No log instruction | Add closing block |
| Pushes to wrong branch | Hardcoded `main` | Closing block uses `git push origin HEAD` |
| Overwrites API-written fixes | No git pull before starting | Pre-flight step 1: always pull first |
| Overwrites working code | Didn't read existing file | Add to Read First + discovery step |
| Stops after first task | Spec file missing from repo | Verify all spec files exist before queuing |
| Duplicates logic | Didn't check if already exists | Pre-flight check #4 |
| Silent bail on task 4+ | Context window too full | Split into separate prompts (max 3 tasks) |
| Full rewrite breaks existing logic | No minimal-edit instruction | Spec says "modify only necessary sections" |
| File truncated mid-write, committed broken | Context window cutoff during large rewrite | Line count check in closing block; never rewrite files >100 lines from scratch |
| "File not found" error | Wrong path assumed | Add ls discovery step to Read First |

---

## QUALITY CHECKLIST

Before handing off the prompt:

- [ ] Every file to be modified is in Read First
- [ ] Discovery step (ls + grep imports) included in Read First
- [ ] No file assumed empty — live content described
- [ ] Pre-flight checks section present
- [ ] Closing block present (verify → commit → push HEAD → build log → report)
- [ ] Max 3 tasks in this prompt
- [ ] All spec/dependency files verified to exist in repo
- [ ] No secrets or API keys referenced inline
- [ ] Fallback/error state specified for every new data fetch
- [ ] Mobile behavior described for any UI change
- [ ] Implementation says "modify only necessary sections" not "rewrite"
- [ ] "Do not break existing functionality" stated explicitly

---

## DELIVERY RULE

Write the prompt to a file. Deliver via present_files. Never paste inline in chat.

File naming: `CLAUDE_CODE_[UPGRADE-IDS-OR-TASK].md`
Output path: `/mnt/user-data/outputs/CLAUDE_CODE_[name].md`

---

## GOTCHAS

- **Commits locally by default** — says "committed" but won't push without explicit instruction
- **`git push origin main` is wrong** — use `git push origin HEAD` to push whatever branch is active
- **"All done" ≠ pushed** — verify via repo commit history after every run
- **Spec files must exist before the prompt runs** — cannot find a file that isn't there
- **Check before write** — if a component/function already exists, update it; don't create a duplicate
- **Minimal edits win** — full file rewrites introduce regressions; patch only what changes
- **Truncation detection** — after writing any file, check its line count against the original: `wc -l new_file original_file`. If the new file is more than 20% shorter and the spec didn't require removal of content, STOP — the output was likely cut off mid-generation. Do not commit a truncated file.
- **Never rewrite large files (>100 lines) from scratch** — always read the existing file, make targeted edits using str_replace or patch approach, and preserve all untouched sections verbatim. Full rewrites of large files risk context-window truncation silently cutting off the end of the file.
- **Context window truncation is silent** — if generation is cut off mid-string or mid-block, the resulting file will be syntactically invalid but git will still accept it. The only protection is the line count check and the build verification step.
- **`--dangerously-skip-permissions` is required** for unattended runs — only use in controlled local environments, never on shared machines
- **Desktop app bypass permissions is broken** — always use CLI for agentic runs
