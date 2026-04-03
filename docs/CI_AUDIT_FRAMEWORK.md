# CI & Audit Framework — Implementation Guide
Version: 1.0 | Source: Nightwatch Phase 15 (NW-317–324) | Date: 2026-04-07

This guide documents the full CI and audit tooling framework built for Nightwatch.
Copy this into any new project (Coinbeast, Axiom, etc.) before building begins.
Every section is a discrete step — complete them in order.

---

## What This Framework Gives You

- Every push and PR runs automated checks before anything reaches main
- Secrets, bad patterns, and dependency vulnerabilities are caught automatically
- Dependency updates happen on a schedule without manual tracking
- A quarterly audit cadence with a standardized report format
- A rule promotion loop — recurring bugs become permanent lint rules

---

## Step 1 — CI Pipeline (`ci.yml`)

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    name: ci
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Gitleaks (secret detection — blocking)
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: oxlint (advisory — remove || true after baseline clean)
        run: npx oxlint@latest src/ --deny-warnings || true

      - name: ESLint
        run: npm run lint

      - name: Tests (advisory — promote to blocking after 2 clean runs)
        run: npm test || true
        env:
          NODE_ENV: test

      - name: npm audit (high/critical only)
        run: npm audit --audit-level=high || true

      - name: Semgrep (custom rules — blocking)
        run: |
          pip install semgrep --quiet
          semgrep --config semgrep/rules/ --error --quiet .

      - name: Semgrep (advisory rules — non-blocking)
        run: |
          semgrep --config semgrep/advisory/ --quiet . || true
```

**Notes:**
- `fetch-depth: 0` is required for Gitleaks to scan full git history
- ESLint is the only step that must be blocking on day one — get it passing first
- oxlint and npm audit start advisory (`|| true`) — promote after baseline cleanup
- Tests start advisory — promote after 2 consecutive clean CI runs
- Semgrep blocking step requires rules in `semgrep/rules/` — see Step 4
- Adjust `npm test` to match your actual test script name

---

## Step 2 — ESLint Plugins

Install:
```
npm install --save-dev eslint-plugin-sonarjs eslint-plugin-no-only-tests
```

Add to ESLint config (preserve all existing rules):
- `sonarjs/recommended` → **warn** (advisory — document baseline violations first)
- `no-only-tests/no-only-tests` → **error** (always blocking — catches `.only` test leaks)
- `react-hooks/exhaustive-deps` → **error** (if React project)

Run ESLint after adding sonarjs and capture the warning count — this is your baseline.
Document it in `docs/AUDIT_BASELINE.md`:

```markdown
# Audit Baseline
Created: YYYY-MM-DD

## sonarjs baseline
Total pre-existing warnings: [N]
Promotion to blocking: after baseline violations are resolved (target: quarterly audit)

## oxlint baseline
Total findings: [N]
Promotion to blocking: after findings are resolved
```

---

## Step 3 — Gitleaks Baseline

Before Gitleaks can block CI, you must scan the full repo history:

```
gitleaks detect --source . --log-opts="--all" -v
```

For each finding:
- **True secret** (real credential): rotate it immediately, then add to `.gitleaksignore`
- **False positive** (test string, example token): add to `.gitleaksignore` with rationale

`.gitleaksignore` format:
```
# [reason this is safe — required for every entry]
[commit-sha]:[file-path]:[line-number]:[rule-id]
```

Never add a `.gitleaksignore` entry without a comment explaining why it is safe.

---

## Step 4 — Semgrep Custom Rules

Create `semgrep/rules/` and write rules specific to your project's known failure patterns.

**Rule template:**
```yaml
rules:
  - id: [project]-[pattern-name]
    patterns:
      - pattern: [pattern]
    message: >
      [What went wrong and what to do instead.]
    languages: [javascript, typescript]
    severity: ERROR
    metadata:
      category: correctness
      upgrade: [upgrade-id]
```

**Hard requirement before enabling any rule as blocking:**
Run the rule against the full codebase. It must return zero false positives.
- 0 findings → enable as blocking
- True positives found → fix them, then enable as blocking
- False positives found → refine the pattern until 0 false positives

Nightwatch's 5 rules (in `semgrep/rules/` of great-horn-aml-nightwatch) are good references:
- `nightwatch-filter-pk-lookup.yaml` — wrong PK lookup pattern
- `nightwatch-raw-role-comparison.yaml` — raw role string comparisons
- `nightwatch-assurance-reference.yaml` — references to a retired entity
- `nightwatch-service-role-context.yaml` — wrong auth context for reads
- `nightwatch-sort-field-unverified.yaml` — advisory, unverifiable at static analysis time

Create a `.semgrepignore` for generated files, test fixtures, and docs:
```
node_modules/
dist/
build/
docs/
*.txt
*.md
**/__tests__/
**/*.test.js
**/*.spec.js
```

---

## Step 5 — Renovate

Create `renovate.json` at repo root:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "schedule": ["every weekend"],
  "timezone": "America/Edmonton",
  "prConcurrentLimit": 3,
  "prCreation": "not-pending",
  "automerge": false,
  "packageRules": [
    {
      "matchUpdateTypes": ["patch"],
      "groupName": "patch updates",
      "automerge": false
    },
    {
      "matchUpdateTypes": ["minor"],
      "groupName": "minor updates",
      "automerge": false
    },
    {
      "matchUpdateTypes": ["major"],
      "automerge": false
    },
    {
      "matchManagers": ["github-actions"],
      "pinDigests": true
    }
  ],
  "vulnerabilityAlerts": {
    "enabled": true,
    "labels": ["security"]
  },
  "labels": ["dependencies"],
  "commitMessagePrefix": "deps:",
  "ignorePaths": ["**/node_modules/**"]
}
```

**Manual step (repo owner only):** Install the Renovate GitHub App at
https://github.com/apps/renovate and grant access to this repo only.

**Auto-merge promotion:** Enable `automerge: true` for patch updates only after:
- CI has been stable for 2+ weeks with no flaky failures
- Tests are promoted from advisory to blocking

---

## Step 6 — Socket.dev (Supply Chain)

**Manual step (repo owner only):** Install the Socket.dev GitHub App at
https://github.com/apps/socket-security and grant access to this repo only.

Socket.dev is advisory only — it adds comments to PRs when a dependency shows
suspicious behavior (new network calls, new shell access, etc.). Never blocks CI.

---

## Step 7 — Quarterly Audit

Copy `docs/AUDIT_REPORT_TEMPLATE.md` and `docs/AUDIT_CHECKLIST.md` from Nightwatch.
These are the standardized format for every quarterly audit.

Cadence: End of each quarter (Q2: June 30, Q3: Sep 30, Q4: Dec 31, Q1: Mar 31).

Each quarterly audit:
1. Claude runs `docs/AUDIT_CHECKLIST.md` against the repo via GitHub API
2. Output saved to `docs/AUDIT_REPORT_YYYY_QN.md`
3. Every finding becomes a GitHub Issue tagged `audit-finding`
4. Findings recurring 2+ times become Semgrep or ESLint rules (rule promotion loop)

---

## Severity Ladder

| Priority | Class | Tools | Behavior |
|---|---|---|---|
| P0 | Always blocking | Custom Semgrep rules, no-only-tests, Gitleaks | Block merge immediately |
| P1 | Blocking after stabilization | sonarjs errors, oxlint errors, ESLint errors | Warn first, promote after baseline |
| P2 | Advisory | React XSS Semgrep, Socket.dev, npm audit low/medium | Never block |
| P3 | Scheduled | TruffleHog, quarterly checklist | Run on schedule |

---

## Implementation Order for a New Project

1. `ci.yml` with ESLint blocking, everything else advisory
2. Run full Gitleaks history scan → create `.gitleaksignore` → enable Gitleaks as blocking
3. Install sonarjs + no-only-tests → document sonarjs baseline in `AUDIT_BASELINE.md`
4. Write project-specific Semgrep rules → validate zero false positives → enable as blocking
5. Add `renovate.json` → install Renovate GitHub App
6. Install Socket.dev GitHub App
7. Copy audit template + checklist → schedule first quarterly audit

Do not skip the baseline step for sonarjs or Gitleaks. Enabling blocking checks
without a clean baseline will break CI immediately and require emergency rollback.

---

## Open Items to Track Per Project

Add these to your STATE file when the framework is installed:

- `OI-CI-01`: oxlint — promote from advisory to blocking after baseline cleanup
- `OI-CI-02`: sonarjs — promote warnings to errors after baseline resolved
- `OI-CI-03`: Tests — promote from advisory to blocking after 2 clean CI runs
- `OI-CI-04`: Renovate — enable auto-merge for patches after CI stable 2+ weeks
- `OI-CI-05`: TruffleHog weekly scan — schedule after Gitleaks is stable
- `OI-CI-06`: First quarterly audit — run before end of current quarter

---

## Reference: Nightwatch Phase 15 Upgrades

| Upgrade | What it built |
|---|---|
| NW-317 | CI pipeline (ESLint blocking, oxlint + npm audit advisory) |
| NW-318 | sonarjs warn + no-only-tests error + exhaustive-deps + baseline |
| NW-319 | 5 Semgrep custom rules (4 blocking, 1 advisory) |
| NW-320 | Gitleaks secret detection (blocking) |
| NW-321 | Auth smoke tests in CI (advisory permanently — need staging env to promote) |
| NW-322 | Renovate dependency management (no auto-merge) |
| NW-323 | Socket.dev supply chain (manual install) |
| NW-324 | Quarterly audit format + checklist + rule promotion loop |
