---
name: test-driven-development
description: Enforces test-first discipline before Cursor implements any logic, fixes any bug, or modifies any existing behavior. MUST be loaded before writing code for new features, bug fixes, or behavioral changes. Fires automatically when Cursor is about to implement logic or fix a reported bug. Do NOT skip — "seems to work" is not done. Tests are proof.
---

# Test-Driven Development

## GATE: Stop Before Implementing

Before writing any implementation code, determine which mode applies:

**New behavior** → Write a failing test first (RED → GREEN → REFACTOR)
**Bug fix** → Write a reproduction test first (Prove-It Pattern)
**Behavioral change** → Write tests covering current behavior before modifying

Skip this skill only for: pure config changes, documentation, static content with zero behavioral impact.

---

## The TDD Cycle

```
RED                   GREEN                 REFACTOR
Write failing test → Make it pass (min) → Clean up → repeat
```

### RED — Write the Test First

The test must fail. A test that passes immediately proves nothing.

Write the test against the interface you want, not the implementation you're about to build. This forces clean API design before code exists.

### GREEN — Minimum Code to Pass

Write the minimum code to make the test pass. Do not over-engineer. Do not add features not covered by a test.

### REFACTOR — Clean Up

Tests are green. Now: extract duplication, improve naming, remove dead code. Run tests after every change. If they go red, undo.

---

## The Prove-It Pattern (Bug Fixes)

**Never start with the fix. Start with the reproduction.**

```
1. Receive bug report
2. Write a test that demonstrates the bug — it must FAIL with current code
3. Confirm it fails (bug is proven)
4. Implement the fix
5. Confirm the test now passes
6. Run full suite — no regressions
```

A bug fix without a reproduction test is not done. The test is what prevents this bug from coming back silently.

---

## The Test Pyramid

```
         ╱╲
        ╱  ╲        E2E (~5%) — critical user flows only
       ╱────╲
      ╱      ╲      Integration (~15%) — API boundaries, DB, component interaction
     ╱────────╲
    ╱          ╲    Unit (~80%) — pure logic, isolated, milliseconds
   ╱────────────╲
```

Most tests should be small (single process, no I/O, no network). Fast tests get run. Slow tests get skipped.

**Decision guide:**
- Pure logic, no side effects → unit test
- Crosses a boundary (API, DB, filesystem) → integration test
- Critical end-to-end user flow → E2E (keep these minimal)

---

## Writing Good Tests

### Assert on Outcomes, Not Implementation

Test what the function does, not how it does it internally. Tests tied to implementation break on every refactor.

```
Good: Assert the returned data shape / state change / error thrown
Bad:  Assert that a specific internal method was called
```

### Arrange-Act-Assert

Every test follows this structure:
1. **Arrange** — set up the scenario
2. **Act** — call the thing being tested
3. **Assert** — verify the outcome

### One Concept Per Test

Each test verifies one behavior. If a test has five assertions testing five different things, split it into five tests. Failures become instantly diagnosable.

### DAMP Over DRY

Tests should read like specifications. Acceptable to repeat setup code if it makes each test independently understandable. Don't force a reader to trace through shared helpers to understand what a test is checking.

### Descriptive Names

Test names are the specification. They should read as: `[unit] [does what] [under what conditions]`

```
Good: "completeTask sets status to completed and records timestamp"
Bad:  "test 3" / "works" / "handles errors"
```

### Prefer Real Implementations Over Mocks

```
1. Real implementation    (highest confidence)
2. Fake (in-memory stub)
3. Stub (canned data)
4. Mock (interaction verification) — use sparingly
```

Mock only at boundaries where real dependencies are non-deterministic, too slow, or have uncontrollable side effects (external APIs, email sending, payment processors).

---

## Pre-Ship Test Checklist

```
- [ ] Every new behavior has a corresponding test
- [ ] All tests pass
- [ ] Bug fixes include a reproduction test that failed before the fix
- [ ] Test names describe the behavior being verified
- [ ] No tests skipped or disabled to make the suite pass
- [ ] Coverage hasn't decreased (if tracked)
- [ ] No tests asserting on internal implementation details
```

---

## Red Flags — Stop and Flag These

- Writing implementation code before any test exists
- Test passes on the first run without any implementation (test is wrong)
- Bug fix shipped without a reproduction test
- Test names that don't describe expected behavior
- Tests disabled or skipped to make CI green
- All assertions in one massive test block
- Mocking everything — test suite passes but production breaks
- "I tested it manually" — manual tests don't persist
