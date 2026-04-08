# Nightwatch Upgrade Orchestrator — Stage Reference
*Fetched by nightwatch-upgrade-orchestrator when executing stages 2–9.*
*Contains prompt templates, code, report formats, and failure taxonomy.*

## STAGE 2: PROMPT CONSTRUCTION

### FAST LANE TEMPLATE (40 lines max)

```
CURSOR BACKGROUND AGENT PROMPT
NW-UPGRADE-XXX — [Title]
Version: 1.0

Objective
[One sentence.]

Scope
[Exact file list — no wildcards.]

Do Not Modify
[Exact exclusions.]

Acceptance Criteria
[Concrete testable bullets — 3-5 max.]

BEFORE STARTING
git pull --rebase origin main
git checkout -b NW-UPGRADE-XXX
Confirm branch: $b = git branch --show-current; if ($b -ne "NW-UPGRADE-XXX") { exit 1 }

BEFORE FINISHING
npm test
If tests fail: stop, write docs/NW-UPGRADE-XXX-RESULT.md with status FAIL and failing test output. Do not commit.
git add -A ; git commit -m "NW-UPGRADE-XXX: [desc]" ; git push origin NW-UPGRADE-XXX
Write docs/NW-UPGRADE-XXX-RESULT.md listing every changed file and confirming tests passed.
Update docs/NIGHTWATCH_STATE.md.

Branch: NW-UPGRADE-XXX
END OF CURSOR PROMPT
```

### GUARDED LANE TEMPLATE (full — adds caller check and SANITYCHECK)

```
CURSOR BACKGROUND AGENT PROMPT
NW-UPGRADE-XXX — [Title]
Version: 1.0

Objective
[One paragraph.]

Context
[Minimum context: affected subsystem, relevant graph rule, related upgrades if essential.]

Scope
[Explicit include list.]

Do Not Modify
[Explicit exclude list.]

Safety / Guardrails
- Preserve existing verified behavior unless explicitly replacing it
- No schema or entity changes
- No secrets or env var changes
- No Base44 publish steps
- No unrelated cleanup
- If hidden complexity discovered: write docs/NW-UPGRADE-XXX-REVIEW.md and stop

BEFORE STARTING
git pull --rebase origin main
git checkout -b NW-UPGRADE-XXX

SANITYCHECK — docs/NW-UPGRADE-XXX-SANITYCHECK.md
1. Confirm branch — hard stop if wrong
2. List every file that imports changed shared modules (caller enumeration)
3. For enum/string changes: list every literal in codebase matching old values
4. Assess blast radius: files touched, breakage risk, irreversibility
5. Rate risk: low / medium / high — stop at REVIEW file if high

[Implementation spec]

Acceptance Criteria
[Concrete testable bullets.]

Verification outputs required
- docs/NW-UPGRADE-XXX-SANITYCHECK.md
- docs/NW-UPGRADE-XXX-RESULT.md (with build evidence)

BEFORE FINISHING
npm test
If tests fail: stop, write docs/NW-UPGRADE-XXX-RESULT.md with status FAIL. Do not commit.
git add -A ; git status ; git commit -m "NW-UPGRADE-XXX: [desc]" ; git push origin NW-UPGRADE-XXX
Update docs/NIGHTWATCH_STATE.md.

Branch: NW-UPGRADE-XXX
END OF CURSOR PROMPT
```

### Nightwatch constraints injected into every prompt
- Amanda's work = Effectiveness Review. Never "audit."
- Role checks via roleUtils.js only — never raw array checks
- No legacy module reuse
- No side systems — every feature connects to the canonical graph

---

## STAGE 3: API SUBMISSION

```python
import urllib.request, json

def submit_agent(prompt, branch):
    API_KEY = "CURSOR_API_KEY_FROM_PROJECT_INSTRUCTIONS"
    payload = json.dumps({
        'prompt': {'text': prompt},
        'source': {'repository': 'https://github.com/bitcoinbrainsweb/great-horn-aml-nightwatch', 'ref': 'main'},
        'target': {'branchName': branch}
    }).encode()
    req = urllib.request.Request('https://api.cursor.com/v0/agents', data=payload, method='POST',
        headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())
```

Save the returned agent ID immediately.

---

## STAGE 4: POLLING

Poll strategy — stay under 4-minute bash timeout:
- Call 1: wait 90s | Call 2: wait 90s | Call 3: wait 120s | Call 4+: wait 60s each, up to 30 min

```python
import time

def poll_agent(agent_id):
    API_KEY = "CURSOR_API_KEY_FROM_PROJECT_INSTRUCTIONS"
    waits = [90, 90, 120] + [60]*25
    for i, wait in enumerate(waits):
        time.sleep(wait)
        req = urllib.request.Request(f'https://api.cursor.com/v0/agents/{agent_id}',
            headers={'Authorization': f'Bearer {API_KEY}'})
        with urllib.request.urlopen(req) as r:
            d = json.loads(r.read())
        status = d.get('status')
        print(f'Poll {i+1} (+{wait}s): {status}')
        if status in ('FINISHED', 'ERROR', 'EXPIRED'):
            return status
    return 'TIMEOUT'
```

Terminal states: FINISHED, ERROR, EXPIRED, TIMEOUT — all non-FINISHED treated as failure.

---

## STAGE 5: TIERED VERIFICATION

### FAST LANE
- [ ] Branch exists in GitHub
- [ ] RESULT artifact present
- [ ] No forbidden files touched (base44/entities/, auth, secrets)
- [ ] All acceptance criteria covered in RESULT
- [ ] TEST GATE: RESULT confirms npm test passed on branch

### GUARDED LANE (adds)
- [ ] SANITYCHECK artifact present
- [ ] Caller enumeration performed
- [ ] For enum/string changes: zero old literal values remain
- [ ] No orphaned exports or imports
- [ ] Build/lint evidence present in RESULT
- [ ] TEST GATE: RESULT confirms npm test passed

### IMMEDIATE FAIL triggers (both lanes)
- Schema or entity changes when not authorized
- Secret/env/config changes when not authorized
- Auth, session, permission files touched when not in scope
- Missing RESULT artifact
- Tests failing or not run on branch

### PASS WITH FLAGS rule
Pause the run. Assess each flag before proceeding. Never auto-continue.

---

## STAGE 6: MERGE VIA GITHUB API

```python
def merge_branch(branch, message):
    TOKEN = "GITHUB_PAT_FROM_PROJECT_INSTRUCTIONS"
    payload = json.dumps({'base': 'main', 'head': branch, 'commit_message': message}).encode()
    req = urllib.request.Request(
        'https://api.github.com/repos/bitcoinbrainsweb/great-horn-aml-nightwatch/merges',
        data=payload, method='POST',
        headers={'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read())
    return d['sha'][:12]
```

Only call after verification PASS. Never call after FAIL.

---

## STAGE 7: CHECKPOINT (between consecutive upgrades)

After every merge in a consecutive run:
1. Re-read docs/NIGHTWATCH_STATE.md from main — confirm it reflects just-merged state
2. Check for open flags from this upgrade
3. Changed-surface memory: if upgrade touched shared utils, auth, or report logic → next upgrade min lane = Guarded
4. Every 2 merges: full state re-read before next submit
5. Any unresolved flag → stop run, report to Dave

---

## STAGE 8: REPORT FORMAT

```
NW-UPGRADE-XXX — [Title]
Lane: fast | guarded | manual
Agent ID: [id] (or N/A for manual)
Branch: [branch]
Status: PASS | PASS WITH FLAGS | FAIL

Files changed: [list]
Forbidden changes: none | [list]
Acceptance criteria: [PASS/PARTIAL/FAIL per criterion]
Flags: none | [list with assessment]
Run continues: yes | paused (flag unresolved) | stopped (FAIL)

Merge: completed [sha] | not merged
Next upgrade: [id] | manual stop required
```

---

## STAGE 9: MANUAL PACKAGE (non-API-safe)

When lane = Manual, always produce:
1. Classification decision + reason (one sentence)
2. Base44 editor prompt (if entity/schema change) — labeled STEP 1 OF 2
3. Full Cursor prompt — labeled STEP 2 OF 2
4. Acceptance criteria
5. Verification checklist
6. Merge command template

---

## FAILURE TAXONOMY

| Type | Response |
|------|----------|
| prompt_failure | Retry once with tighter prompt |
| implementation_failure | Manual package |
| verification_failure | Retry once with explicit artifact requirement |
| scope_drift | Manual package, quarantine branch |
| hidden_complexity | Reclassify to higher lane |
| contaminated_branch | Start fresh branch, no retry |

Retry policy: one retry max, only for prompt_failure or verification_failure.
No retry for scope_drift, hidden_complexity, contaminated_branch, or auth/security failures.

---

## PHASE END PROTOCOL

Trigger: Dave says "close out Phase X" or "run phase end for Phase X". Never infer.

Full procedure: fetch `docs/PHASE_END_PROTOCOL.md` from Nightwatch repo before starting.

Quick reference steps:
1. Completeness Check — all upgrades merged, no open REVIEW files, no unresolved flags
2. Roadmap Audit — apply pending ROADMAP_AUDIT.md items scoped to this phase
3. Security Review — live app scan + code scan (GitHub API diff)
4. Open Items Sweep — classify each STATE.md item: RESOLVED / DEFERRED / ESCALATED / STALE
5. Amanda Sign-Off Check — flag phase-gate blockers
6. State File Update — push updated STATE.md, mark phase complete
7. Phase Gate Decision — OPEN or HOLD

Phase Gate Output format:
```
PHASE END REPORT
Phase:              [Phase X — Name]
Date:               [YYYY-MM-DD]
Upgrades merged:    [count] of [count planned]
Security review:    CLEAR | FLAGS | BLOCKED
Open items:         [count] resolved, [count] deferred, [count] escalated
Amanda sign-offs:   [count] pending — blocking | non-blocking

PHASE GATE:         OPEN | HOLD
HOLD REASON:        [if applicable]
NEXT PHASE:         [Phase X+1 — Name]
FIRST UPGRADE:      [NW-XXX]
```

Security Review scope:
- Part A (live app): every route added/modified this phase; auth boundaries, role visibility, console errors
- Part B (code scan): raw role array checks, hardcoded secrets, direct entity access bypassing function gates, console.log with PII, unapproved dependencies
- Finding levels: CLEAR / FLAG (non-blocking) / BLOCK (must resolve before gate opens)
