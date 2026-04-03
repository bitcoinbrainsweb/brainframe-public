# AI Development Workflow
Version: 1.0 | Promoted from Nightwatch, 2026-04-03
Generic — applies to any project using AI-assisted development.

---

## Overview

An AI development operating system workflow coordinates implementation, review, and deployment across AI tools and human decision-makers.

Enforces:
- Sequential, controlled upgrades
- Mandatory pre-implementation sanity checks
- Risk-gated review escalation
- Post-implementation GATE approval before any next upgrade

---

## Upgrade Protocol

Every upgrade follows this exact sequence. No steps may be skipped.

```
SANITYCHECK → REVIEW (if medium/high risk) → IMPLEMENT → RESULT → GATE
```

### Step 1 — SANITYCHECK
Assess scope, risk, and readiness before writing any code.
Classify risk: LOW / MEDIUM / HIGH.
Confirm: correct branch, prerequisites met, no conflicting in-progress work.

### Step 2 — REVIEW (conditional)
Required when risk is MEDIUM or HIGH.
Documents: implementation plan, risk analysis, rollback strategy.

### Step 3 — IMPLEMENT
Execute the smallest durable change set.
Sequential execution only — never parallel changes within one upgrade.

### Step 4 — RESULT
Document what was done, what was validated, deviations from plan, follow-ups.

### Step 5 — GATE
Canonical go/no-go decision artifact. Binary. No next upgrade until GATE exists with a VERDICT.

---

## GATE Structure

```
BUILD:          [UPGRADE_ID]
DATE:           YYYY-MM-DD
SMOKE TEST:     PASS / FAIL / SKIPPED — reason
CHECKLIST:      [verification items, each PASS/FAIL]
VERDICT:        GO / NO-GO
FAILURE REASON: [if NO-GO]
NEXT ACTION:    [next upgrade ID or follow-up]
```

---

## Tool Roles

| Tool | Role |
|---|---|
| Implementation agent (Cursor/etc.) | Code changes, SANITYCHECK, RESULT, GATE artifacts |
| Orchestration agent (Claude) | Planning, verification, merge authority on PASS |
| Decision authority (human) | Scope, approval, final GATE review |

---

## Standing Rules

1. Follow the upgrade protocol exactly. No steps skipped.
2. Preserve prior verified fixes unless explicitly replacing them.
3. Make the smallest durable fix.
4. No next upgrade proceeds until the current GATE exists with VERDICT.
5. Implementation agent never merges to main — orchestration agent merges via API after PASS.
6. Sequential execution only within each upgrade.
7. Every upgrade on a feature branch — never directly on main.

---

## Lane Classification

| Lane | Criteria | Who submits |
|---|---|---|
| Fast | ≤3 files, atomic, no new patterns | Orchestration agent auto-submits |
| Guarded | 4–8 files, or touches auth/roles/nav | Orchestration agent auto-submits |
| Manual | Complex, multi-system, new patterns, debugging | Human submits |
