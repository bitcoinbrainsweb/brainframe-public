---
name: roadmap-planner
description: "Use when working with any project roadmap — reading, writing, updating, or planning. Triggers on: roadmap, upgrade spec, phase planning, sequencing, open items, feature additions, or \'what should we build next\'."
---

# Roadmap Planner
Version: 1.0

Write better upgrade specs. Preserve sequencing logic. Keep roadmap versions clean.

## What This Is NOT For

- Writing implementation prompts → use project-specific prompt skill
- Architecture decisions → flag as open item, do not resolve inline
- Silently converting blocked items into assumptions

## Item State Machine

```
Open Item → Clarified → Candidate → Drafted Spec → Ready → In Progress → Shipped
                                          ↓
                                       Blocked (unresolved gate)
                                       Deferred (postponed, reason documented)
                                       Superseded (replaced — never silently reused)
                                       Abandoned (dropped — reason recorded)
```

## Minimum Spec Contract

Every upgrade spec must contain before it is Drafted:

| Field | Notes |
|---|---|
| ID | Immutable once assigned |
| Title | Sentence case |
| Intent | Two lines: why + what must not be lost |
| Scope In | What this does |
| Scope Out | What this explicitly does NOT do |
| Prerequisites | Other IDs or named conditions |
| Hard Gates | Explicit stop conditions. "None" is valid. |
| Lane | Fast / Guarded / Manual / Blocked |
| Acceptance Evidence | How to verify it is done |
| Stop Condition | What causes this to halt and surface |
| Provenance | Where this came from |

## Sequencing Rules

1. Infrastructure before features
2. Security and auth before data or user-facing work
3. Blocking items resolved before dependent items start
4. Never schedule two items that share the same files in the same sprint

## Scan Triggers

Re-read the roadmap when:
- A new feature is proposed
- A bug is found that implies a gap
- An upgrade completes
- A dependency changes
- Dave asks "what are we missing"
