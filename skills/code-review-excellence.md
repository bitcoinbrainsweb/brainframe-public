---
name: code-review-excellence
description: "Comprehensive code review guidance for React, TypeScript, and JavaScript. Use when reviewing pull requests, checking code quality, finding bugs, or giving feedback on code changes."
---

# Code Review Excellence
Version: 1.0

Review for correctness first, then clarity, then style. Never reverse this order.
Report only what matters. Skip observations that don't affect correctness, safety, or maintainability.

## Severity Levels

### CRITICAL — must fix before merge
- Logic errors producing wrong output or silent data corruption
- Security vulnerabilities (auth bypass, injection, exposed secrets)
- Data loss or irreversible state corruption
- Breaking changes to public interfaces without versioning

### HIGH — should fix before merge
- Missing error handling on external calls (API, DB, filesystem)
- Race conditions or async bugs
- Performance issues that will hit production at scale
- Accessibility violations (WCAG AA minimum)

### MEDIUM — fix in follow-up
- Code duplication that creates maintenance risk
- Missing or misleading comments on complex logic
- Inconsistent naming within a module
- Untested edge cases

### LOW — optional / style
- Formatting inconsistencies not caught by linter
- Minor naming improvements
- Documentation gaps on non-public functions

## Review Process

1. Read the diff top to bottom once without commenting
2. Identify the intent of the change
3. Check CRITICAL issues first
4. Work down severity levels
5. Group related comments

## Output Format

```
[CRITICAL] file.js:42 — [what is wrong and why it matters]
[HIGH] file.js:67 — [what is wrong and why it matters]
[MEDIUM] file.js:89 — [suggestion]
```

Overall verdict: APPROVE / REQUEST CHANGES / NEEDS DISCUSSION
