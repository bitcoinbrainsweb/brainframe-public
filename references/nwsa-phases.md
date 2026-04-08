# Nightwatch Site Audit — Phase Reference
*Fetched by nightwatch-site-audit skill before executing any phase.*
*Contains full phase checklists, report format, push commands, and known issues.*

## PHASE 1 — REPO AUDIT (GitHub API)

Fetch via GitHub API. Never use web_fetch for GitHub.
Base: https://api.github.com/repos/bitcoinbrainsweb/great-horn-aml-nightwatch

### 1.1 Branch State
- List all branches: GET /branches
- Flag: any branch other than main that is older than 7 days
- Flag: any NW-UPGRADE-XXX branch not merged
- Flag: main branch protection disabled

### 1.2 State File Freshness
- Fetch docs/NIGHTWATCH_STATE.md
- Check: last_updated date — flag if older than 7 days
- Check: active_branch field — confirm matches any open branch
- Check: next_upgrade field — confirm it exists in roadmap

### 1.3 GATE Files
- List all docs/NW-UPGRADE-*-GATE.md files
- Flag: any GATE file with STATUS: FAIL
- Flag: any GATE file with READY_TO_MERGE: no (unresolved)
- Flag: any branch with no GATE file

### 1.4 CLAUDE.md and Config
- Fetch CLAUDE.md — confirm it exists and is not empty
- Fetch docs/NIGHTWATCH_CONFIG.md — confirm identity fields present
- Flag: any hardcoded credentials found in any docs/ file

### 1.5 Open Items
- Fetch docs/NIGHTWATCH_STATE.md open items section
- List all open items with age (days since added)
- Flag: any open item older than 30 days with no progress

### 1.6 Recent Merges
- List last 10 merged PRs
- Confirm each has a corresponding RESULT file
- Flag: any merge with missing RESULT

---

## PHASE 2 — SITE AUDIT (Browser Extension)

Requires Claude in Chrome browser tool. If unavailable: SKIPPED — log capability gap.
Live app: https://nightwatch-risk-hub.base44.app

### 2.1 Auth and Role Boundaries
- Log in as each role: admin, compliance_officer, client
- Confirm each role sees only its permitted routes
- Flag: any route accessible without appropriate role
- Flag: any raw role string visible in network responses

### 2.2 Route Coverage
For every route in the app:
- Confirm route loads without error
- Confirm no console errors on load
- Confirm primary action is visible above the fold
- Flag: any dead screen (no action available)
- Flag: any non-clickable element that should be clickable

### 2.3 Network Errors
- Open browser console during normal workflow
- Flag: any 4xx or 5xx responses
- Flag: any failed network requests
- Flag: any CORS errors

### 2.4 UI Issues
Apply UX skill criteria:
- Stat values are tappable filters
- Lists sort by urgency (errors → review → unconfirmed → complete)
- Complete items collapsed by default
- Back preserves state
- Navigation consistent across screens

### 2.5 Feature Gaps
Compare current state to roadmap DONE items:
- Flag: any DONE item not reflected in live app
- Flag: any UI element referencing a feature not yet built

---

## PHASE 3 — REPORT FORMAT AND PUSH

### Report Structure

```markdown
# Nightwatch Site Audit Report
Date: YYYY-MM-DD
Auditor: Claude (Comsworth Bellingham)

## Summary
Phase 1 (Repo): [CLEAR | N flags]
Phase 2 (Site): [CLEAR | N flags | SKIPPED]
Total flags: N critical, N warnings

## Critical Flags (must resolve before next upgrade)
- [Flag]: [description] | [file or route] | [recommended action]

## Warnings (should resolve this phase)
- [Flag]: [description] | [file or route] | [recommended action]

## Phase 1 Detail
[findings per section]

## Phase 2 Detail
[findings per route/check]

## Resolved Since Last Audit
[items from KNOWN ISSUES now clear]
```

### Push Report to Repo

```bash
# Step 1: get SHA (needed for update)
SHA=$(curl -s -H "Authorization: token $GITHUB_PAT" \
  "https://api.github.com/repos/bitcoinbrainsweb/great-horn-aml-nightwatch/contents/docs/AUDIT_REPORT.md" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('sha',''))")

# Step 2: base64 encode
ENCODED=$(cat /tmp/audit_report.md | base64 -w 0)

# Step 3: build payload (include sha only if file exists)
if [ -n "$SHA" ]; then
  PAYLOAD=$(echo "{"message": "audit: $(date +%Y-%m-%d)", "content": "$ENCODED", "sha": "$SHA"}")
else
  PAYLOAD=$(echo "{"message": "audit: $(date +%Y-%m-%d)", "content": "$ENCODED"}")
fi

# Step 4: push
curl -s -X PUT \
  -H "Authorization: token $GITHUB_PAT" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/bitcoinbrainsweb/great-horn-aml-nightwatch/contents/docs/AUDIT_REPORT.md" \
  -d "$PAYLOAD"
```

---

## KNOWN ISSUES (pre-seeded)

Issues identified in March 25, 2026 audit — check each run:
- Stat values on post-import screen not tappable (Phase 2 check 2.1)
- Help config missing on 3 routes added in Phase 2 (Phase 2 check 2.2)
- Back navigation resets scroll position on engagement overview (Phase 2 check 2.4)

Mark each as RESOLVED if no longer present. Add new issues found this run.
