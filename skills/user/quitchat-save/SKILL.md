---
name: quitchat-save
description: >-
  Memory audit, GitHub handoff write, and failed attempts capture for session close.
  Called by quitchat orchestrator after quitchat-scan. Can also be run standalone.
---
# Quitchat-Save — Memory, Handoff, Failed Attempts
Version: 4.1 | 2026-04-12
Spec: brainframe-comms/specs/admin/admin-quitchat-v2.md v4

PAT: fetch from brainframe-comms/_docs/REGISTRY.md before any operation. Never hardcode.

---

## PROJECT ROUTING

Resolve paths from detected project before any file operation. Use the table below.

| Project | Repo | State file | Next action file | Handoff dir | Failed attempts file |
|---------|------|-----------|-----------------|-------------|----------------------|
| admin | bitcoinbrainsweb/brainframe-public | docs/admin/ADMIN_STATE.md | docs/admin/NEXT_ACTION.md | docs/admin/handoffs/ | docs/admin/failed-attempts.md |
| nightwatch | bitcoinbrainsweb/great-horn-aml-nightwatch | docs/admin/ADMIN_STATE.md | docs/admin/NEXT_ACTION.md | docs/admin/handoffs/ | docs/admin/failed-attempts.md |
| axiom | bitcoinbrainsweb/axiom | docs/admin/ADMIN_STATE.md | docs/admin/NEXT_ACTION.md | docs/admin/handoffs/ | docs/admin/failed-attempts.md |
| mambamode | bitcoinbrainsweb/mamba-mode | docs/admin/ADMIN_STATE.md | docs/admin/NEXT_ACTION.md | docs/admin/handoffs/ | docs/admin/failed-attempts.md |
| coinbeast | bitcoinbrainsweb/coinbeast | docs/admin/ADMIN_STATE.md | docs/admin/NEXT_ACTION.md | docs/admin/handoffs/ | docs/admin/failed-attempts.md |
| winston | bitcoinbrainsweb/winston | docs/admin/ADMIN_STATE.md | docs/admin/NEXT_ACTION.md | docs/admin/handoffs/ | docs/admin/failed-attempts.md |

**Fallback:** If project not in table, use admin row and flag it.

All `{REPO}`, `{STATE_FILE}`, `{NEXT_ACTION_FILE}`, `{HANDOFF_DIR}`, `{FAILED_FILE}` references below resolve from this table at runtime.

---

## PHASE 1 — MEMORY AUDIT

Fetch all memory edits via memory_user_edits tool (command: view).
Fix: stale entries, duplicates, missing context from this session.
Report: `N reviewed / N changed`

---

## PHASE 2 — READ BEFORE WRITE

Before writing handoff, fetch and scan these files to prevent conflicts:

```bash
# STATE FILE
curl -sH "Authorization: token {PAT}" \
  "https://api.github.com/repos/{REPO}/contents/{STATE_FILE}" \
  | python3 -c "import sys,json,base64; print(base64.b64decode(json.load(sys.stdin)['content']).decode())"

# NEXT ACTION FILE
curl -sH "Authorization: token {PAT}" \
  "https://api.github.com/repos/{REPO}/contents/{NEXT_ACTION_FILE}" \
  | python3 -c "import sys,json,base64; print(base64.b64decode(json.load(sys.stdin)['content']).decode())"

# DECISIONS (last 10 entries — always brainframe-comms)
curl -sH "Authorization: token {PAT}" \
  "https://api.github.com/repos/bitcoinbrainsweb/brainframe-comms/contents/_decisions/DECISIONS.md" \
  | python3 -c "import sys,json,base64; content=base64.b64decode(json.load(sys.stdin)['content']).decode(); print('\n'.join(content.split('\n')[-60:]))"
```

Merge any open items found into the handoff content. Never write without reading first.

---

## PHASE 3 — HANDOFF TO GITHUB

**Path:** `{REPO}/{HANDOFF_DIR}YYYY-MM-DD-{project}.md`

**Handoff content — must include:**
- Session summary (3–5 sentences, self-contained, zero memory assumed)
- Decisions made this session — each with `Rejected alternatives:` field
- Last completed action
- All unresolved items from quitchat-scan
- Open items (carry-forward)
- First action next session
- Last commit SHA from active repos this session

**Write pattern:**
```python
import urllib.request, json, base64, time

PAT = "{PAT}"  # fetch from brainframe-comms/_docs/REGISTRY.md before running
REPO = "{REPO}"          # resolved from PROJECT ROUTING table
PATH = f"{'{HANDOFF_DIR}'}{date}-{project}.md"  # resolved from PROJECT ROUTING table

# Check if exists (same-day append)
req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/contents/{PATH}",
    headers={"Authorization": f"token {PAT}"})
sha = None
try:
    with urllib.request.urlopen(req) as r:
        d = json.load(r); sha = d['sha']
        existing = base64.b64decode(d['content']).decode()
        content = existing + "\n\n---\n\n" + new_content  # append
except:
    content = new_content  # create

encoded = base64.b64encode(content.encode()).decode()
payload = {"message": f"handoff: {project} {date}", "content": encoded}
if sha: payload["sha"] = sha

req2 = urllib.request.Request(f"https://api.github.com/repos/{REPO}/contents/{PATH}",
    data=json.dumps(payload).encode(),
    headers={"Authorization": f"token {PAT}", "Content-Type": "application/json"},
    method="PUT")

# Retry once on failure
for attempt in range(2):
    try:
        with urllib.request.urlopen(req2, timeout=30) as r:
            result = json.load(r)
            print("Saved:", result['content']['path'])
            break
    except Exception as e:
        if attempt == 0:
            time.sleep(3)
            # Re-fetch SHA before retry
        else:
            print("FAILED:", e)
            # Fall back to present_files
```

**On failure after retry:** deliver via `present_files`, log as open item. Never silent drop.

---

## PHASE 4 — FAILED ATTEMPTS

**Path:** `{REPO}/{FAILED_FILE}` (resolved from PROJECT ROUTING table)

Scan conversation for:
- Tool calls that errored or were retried
- Approaches abandoned mid-session
- Dave corrections mid-attempt ("that didn't work", "try a different way")

Append each finding:
```
YYYY-MM-DD | {project} | {what was tried} | {why it failed}
```

Same write pattern as handoff (append-only, fresh SHA, retry once).

Note: scan is heuristic — subtle tool switches or gradual abandons may be missed. When uncertain, include with a `[UNCERTAIN]` tag.

---

## STATUS

Report: `save: ✅` / `save: ⚠️ PARTIAL — [what failed]` / `save: ❌ — [reason], fell back to present_files`
