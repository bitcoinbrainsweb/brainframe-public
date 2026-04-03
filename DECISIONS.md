# DECISIONS
Append-only. Cross-project decisions log. Never delete or edit past entries.
Format: one entry per decision. Timestamp required.

---

## Entry Format

```
### YYYY-MM-DD | [project] | [decision title]
**Decision:** [what was decided — one sentence]
**Rationale:** [why — one sentence]
**Applies to:** [all projects / nightwatch / axiom / etc.]
**Status:** CONFIRMED | PROVISIONAL | SUPERSEDED
**Supersedes:** [prior decision title, if any]
```

---

## 2026-04-03 | nightwatch | Cross-project promotion protocol
**Decision:** Any Claude instance may commit directly to brainframe-public main — no PR required.
**Rationale:** PAT has write access; PR step added unnecessary human friction.
**Applies to:** All projects
**Status:** CONFIRMED

## 2026-04-03 | nightwatch | PROMOTION_LOG as collision guard
**Decision:** Every promotion must append to PROMOTION_LOG.md before writing the target file.
**Rationale:** Multiple collaborators running concurrent sessions creates last-write-wins risk.
**Applies to:** All projects
**Status:** CONFIRMED

## 2026-04-03 | nightwatch | Generic skills in brainframe-public
**Decision:** Project-agnostic skills live in brainframe-public/skills/ and sync to all repos.
**Rationale:** Eliminates drift when methodology changes — update once, all projects benefit.
**Applies to:** All projects
**Status:** CONFIRMED

## 2026-04-03 | nightwatch | AGENT_REGISTRY is project-specific
**Decision:** Each project maintains its own AGENT_REGISTRY.md. No cross-project registry.
**Rationale:** Authority mapping is project-scoped; collaborators and roles differ per project.
**Applies to:** All projects
**Status:** CONFIRMED

## 2026-04-03 | nightwatch | Three-layer state split
**Decision:** STATE (working), LOG (append-only history), CONFIG (identity) are separate files.
**Rationale:** Prevents session state from contaminating historical record or stable config.
**Applies to:** Nightwatch (pattern available to all projects)
**Status:** CONFIRMED
