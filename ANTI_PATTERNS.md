# ANTI_PATTERNS.md
Brainframe v2.0
Append-only. Load on demand. Reference when a familiar failure mode appears.

---

### AP001 — Validating without challenging
**What:** AI agrees with a decision instead of pressure-testing it.
**Why:** Unchallenged decisions accumulate into brittle architecture.
**How to apply:** Default to critique. Ask what could go wrong before confirming anything.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Claude planning session

---

### AP002 — Brainfile bloat
**What:** Adding detailed content to the brainfile instead of referencing sub-files.
**Why:** A bloated brainfile exceeds context window limits and defeats the loader architecture.
**How to apply:** If something is more than two sentences, it belongs in a sub-file. The brainfile points, never embeds.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Claude planning session

---

### AP003 — Premature commercialization
**What:** Building commercial or monetization features before the core editorial product is proven.
**Why:** Premature monetization signals desperation and undermines trust — the core asset of any intelligence platform.
**How to apply:** No commercial features until the editorial product stands on its own.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Claude planning session

---

### AP004 — Silent file overwrites
**What:** Saving new information that contradicts an existing entry without flagging the conflict.
**Why:** Contradictions accumulate silently and corrupt project state.
**How to apply:** Always run check dependencies before saving. Flag conflicts explicitly. Never overwrite silently.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Brainframe design session

---

### AP005 — Silent scope expansion
**What:** A task quietly expands into architecture or system design work without acknowledgment.
**Why:** Scope drift derails sessions and produces outputs that weren't reviewed or approved.
**How to apply:** Label any expansion explicitly. Confirm new scope before continuing. If Dave is unavailable, log to KNOWN_UNKNOWNS.md and continue with original scope.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Brainframe v2 design session

---

### AP006 — Assumptions presented as facts
**What:** An AI presents an unverified assumption as confirmed information.
**Why:** Decisions built on unverified assumptions produce cascading errors.
**How to apply:** Mark all unverified claims as ASSUMED. Never remove the label until verified.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Brainframe v2 design session

---

### AP007 — Proceeding through unknown dependencies
**What:** Implementing a step before its prerequisite has been verified.
**Why:** Unknown dependencies produce broken builds and wasted implementation work.
**How to apply:** Block the step. State the dependency explicitly. Do not proceed until it is confirmed.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Brainframe v2 design session

---

### AP008 — Temporary states without removal triggers
**What:** A temporary workaround or placeholder is implemented without a defined removal condition.
**Why:** Temporary always becomes permanent without a trigger to remove it.
**How to apply:** Every temporary state must have a removal trigger or replacement trigger defined at creation.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Brainframe v2 design session

---

### AP009 — Cross-project rule contamination
**What:** A rule or decision from one project silently applies to another project.
**Why:** Projects have different contexts. Silent propagation produces incorrect behavior.
**How to apply:** Rules stay project-scoped unless Dave explicitly promotes them to global and they are written to GLOBAL_RULES.md immediately.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Brainframe v2 design session

---

### AP010 — Implied production readiness
**What:** A placeholder, scaffolded, or unverified component is presented without labeling.
**Why:** Unlabeled incomplete work gets treated as production-ready and causes failures downstream.
**How to apply:** Always label placeholder, UI-only, scaffolded, or unverified components explicitly. Never imply production readiness unless confirmed.
**Status:** CONFIRMED
**Date:** 2026-03-15
**Source:** Brainframe v2 design session
