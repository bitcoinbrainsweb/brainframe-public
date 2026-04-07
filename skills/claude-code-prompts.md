---
name: claude-code-prompts
description: "Use when writing prompts for Claude Code CLI to implement code upgrades autonomously. Covers mandatory prompt structure, push/log requirements, context management, and failure modes. ONLY for Claude Code CLI prompts — not for Cursor, GPT, Perplexity, or any other tool."
---

# Claude Code Prompt Writing Skill
Version: 1.0 | 2026-04-07

Write prompts that Claude Code CLI executes autonomously in a terminal. Claude (this chat) writes the prompt as a file. The user pastes it into the Claude Code terminal session.

---

## TRIGGER

Use this skill when the user says: "write a Claude Code prompt", "give me a prompt for Claude Code", or "queue this for Claude Code". Do NOT use for Cursor prompts, GPT prompts, or any other tool.

---

## MANDATORY STRUCTURE — every prompt must have all of these

### 1. Header
```
# Claude Code — [UPGRADE IDs or task name]
Repo: [owner/repo-name]
```

### 2. Read First
List every file Claude Code must read before writing anything. Be exhaustive — missed reads lead to overwrites of correct code.

```
Read these files before writing any code:
- [spec or task doc]
- [every source file that will be modified]
- [every hook, util, data file imported by target files]
```

Rationale: Claude Code has no session memory. If you don't list it, it won't read it.

### 3. Current State Description
For each file being modified, describe what currently exists. Pull from live reads — never assume. Prevents Claude Code from overwriting correct logic or duplicating what already exists.

### 4. Implementation Instructions
Per task:
- **Files to CREATE** — name + purpose
- **Files to MODIFY/REWRITE** — describe the change explicitly, not just "update this"
- **Component contracts** — props, exports, what it renders
- **Data sources** — which API, hook, or entity
- **Fallback/error states** — required for every data fetch
- **Constraints** — what must not change, what must not be added

### 5. Mandatory Closing Block
Copy this verbatim into every prompt — never omit it:

```
## When done

1. Push to remote:
   git push origin main

2. Append to docs/build-log.md:
   ## [Task name] — YYYY-MM-DD
   **Completed:** [bullet list]
   **Files created:** [list]
   **Files modified:** [list]
   **Acceptance criteria not met:** [list or "None"]
   **Known issues:** [list or "None"]
   Commit: "log: [task name] complete"
   Push: git push origin main

3. Print a completion report to terminal:
   - Files created
   - Files modified
   - Acceptance criteria not met and why
   - Any import errors or runtime issues encountered
```

---

## CONTEXT WINDOW RULES

Claude Code's context degrades past ~70% fill. For large task queues:

- **Max 3 upgrades per prompt** — more causes silent bail or degraded output
- **Order matters** — list tasks sequentially; Claude Code executes in order and stops if blocked
- **One blocking dependency = everything after it stops** — always verify spec files exist in the repo before queueing a prompt that depends on them
- **Large file reads up front** — list all reads at the top so they happen before the context fills
- Don't add narrative or explanation Claude Code doesn't need — every token counts

---

## FAILURE MODES

| Symptom | Cause | Fix |
|---|---|---|
| Commits local, doesn't push | No push instruction | Add closing block |
| Doesn't write build log | No log instruction | Add closing block |
| Overwrites working code | Didn't read existing file first | Add file to Read First |
| Stops after first task | Spec file missing from repo | Verify all spec files exist before queueing |
| Duplicates logic | Didn't read dependencies | List all related hooks/utils in Read First |
| Silent bail on task 4+ | Context window too full | Split into separate prompts (max 3 tasks) |
| Commits but Base44 doesn't update | Push succeeded but sync lag | Wait 60s, check Base44 editor |
| "File not found" error | Wrong path assumed | Read actual file tree first, list exact paths |

---

## QUALITY CHECKLIST

Before handing off the prompt:

- [ ] Every file to be modified is in Read First
- [ ] No file assumed empty — live content described
- [ ] Closing block present (push + build log + report)
- [ ] Max 3 tasks in this prompt
- [ ] All spec/dependency files verified to exist in repo
- [ ] No secrets or API keys referenced inline
- [ ] Fallback/error state specified for every new data fetch
- [ ] Mobile behavior described for any UI change
- [ ] "Do not break existing functionality" stated explicitly

---

## DELIVERY RULE

Write the prompt to a file. Deliver via present_files. Never paste inline in chat.

File naming: `CLAUDE_CODE_[UPGRADE-IDS-OR-TASK].md`
Output path: `/mnt/user-data/outputs/CLAUDE_CODE_[name].md`

---

## GOTCHAS

- **Claude Code commits locally by default** — it will say "committed" but not push unless explicitly told to
- **"All done" does not mean pushed** — always verify via repo commit history after
- **Spec files must exist before the prompt runs** — Claude Code cannot find a file that isn't there
- **Base44 projects**: Claude Code writes to the repo; Base44 bidirectional sync picks up commits automatically — no manual rebuild needed, but allow ~60s
- **dangerously-skip-permissions flag is required** for unattended runs: `claude --dangerously-skip-permissions`
- **Desktop app bypass permissions is broken** — always use CLI, never the desktop app for agentic runs
