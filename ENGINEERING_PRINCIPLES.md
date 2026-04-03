# Engineering Principles
Version: 1.0 | Promoted from Nightwatch, 2026-04-03
Generic — applies to any AI-assisted software project.

---

## 1. Additive Upgrades

Every upgrade must be additive where possible. Avoid breaking changes that destabilize existing data or workflows. When breaking changes are unavoidable, they require explicit review and sign-off.

---

## 2. Single Source of Truth for Authorization

All permission/role checks must use a single canonical utility — never inline string comparisons or array checks scattered through the codebase. A single utility breaks when the authorization model changes; duplicated checks break silently everywhere.

---

## 3. Security First

Security design must include:
- Least privilege access
- Token security and expiration
- Audit/activity logging
- Secure authentication flows
- No user enumeration
- Row-level security before real user data enters the system

---

## 4. Small, Documented Upgrades

Every change is delivered as a clearly defined upgrade with a branch, RESULT artifact, and state file update. The implementation agent never merges to main. The orchestration agent merges via API after verification. The human is the final authority.

---

## 5. Single Deployment Layer

There is one canonical deployment path. No parallel deploy mechanisms. No "just push it manually" shortcuts. Every change goes through the same pipeline.

---

## 6. Repo as Source of Truth

All architectural documents, roadmap, state files, and workflow definitions live in the repo. Nothing authoritative lives in an AI's project knowledge alone. The AI fetches live from the repo — never relies on stale cached knowledge for operational decisions.

---

## 7. Terminology Discipline

Every project must define its canonical terms and enforce them. Wrong terminology in UI copy, help text, or code comments is a defect — not a style issue. Terminology drift compounds over time and confuses users, regulators, and collaborators.

---

## 8. Infrastructure Before Features

Security closure and operational infrastructure before visualization or intelligence features. Build the engine before the dashboard. A feature built on a broken foundation costs more to fix than to delay.

---

## 9. No Workarounds

If the correct tool cannot accomplish a task, immediately route to the tool that can. Never attempt alternatives that bypass the canonical path. Workarounds become load-bearing walls.

---

## 10. AI Judgment Boundaries

AI assists — it does not decide. Any AI output that influences a consequential decision must:
- Be reviewed by a human before acting on it
- Be logged with its inputs
- Not overstate certainty beyond what the evidence supports

The human reviewer's judgment is the output. The AI draft is an input.
