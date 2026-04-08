# Nightwatch Roadmap Config
*Project-specific reference for roadmap-planner skill.*
*Loaded on demand when working on the Nightwatch roadmap.*

## File Location
- Roadmap file: `docs/Nightwatch_Roadmap_Detailed_v15.md`
- Repo: `bitcoinbrainsweb/great-horn-aml-nightwatch`
- New version = new file (Nightwatch_Roadmap_Detailed_vXX.md)
- Update fetchRoadmap Base44 function to point to new file when versioning

## Amanda Flags

Every upgrade spec must include an Amanda flag:

| Flag | Meaning |
|------|---------|
| **Needs input before build** | Amanda's judgment must inform the spec before implementation. Hard gate. |
| **Needs sign-off after build** | Amanda reviews and approves before it ships. Built-in acceptance criterion. |
| **Amanda-informed, not blocking** | Amanda's preferences shaped design but active input not required. |
| **No Amanda dependency** | This upgrade has no Amanda dependency. |

If Amanda's input changes build eligibility → update dependency class to Human and re-evaluate state.

## Dependency Classes

| Class | Meaning |
|-------|---------|
| **Sequential** | Must follow a specific prior upgrade |
| **Parallel** | Can run alongside other upgrades |
| **External** | Outside repo/team control (FINTRAC API, Amanda, third party) |
| **Human** | Amanda or Dave decision/input required before proceeding |

## AVLM Dependencies
- Track: AVLM_PROJECT_CONTEXT.md version, voice model version, logic model version
- Always check AVLM_PROJECT_CONTEXT.md before any upgrade touching AVLM

## Re-read Triggers
Re-read the roadmap file proactively when:
- A new upgrade is being spec'd
- A feature gap is identified
- Amanda input changes build eligibility
- An upgrade completes and the next needs sequencing
- Dave asks "what's next" or "what are we missing"

## File-Specific Update Triggers
| File | When to update |
|------|---------------|
| `docs/AVLM_PROJECT_CONTEXT.md` | Upgrade affects AVLM architecture or voice model usage |
| `docs/AVLM_INDEX.md` | New voice/logic module ships |
| `docs/NIGHTWATCH_STATE.md` | After every merge |

## Provenance Tracking

Every upgrade spec must record its origin:
```
PROVENANCE:
  source: [roadmap | session_discussion | bug_report | competitive_gap | Amanda_input | Dave_decision]
  session_date: YYYY-MM-DD
  context: [one sentence explaining why this was added]
```

## Version Management

New roadmap version = new file: Nightwatch_Roadmap_Detailed_vXX.md
Update fetchRoadmap Base44 function to point to new file.
Never edit the current version file in place if it has been referenced by completed upgrades.

## Contract-Change Detection

A contract change occurs when: a function signature changes, an entity field is renamed/removed,
an enum value changes, or a shared utility changes its return shape.

When detected during spec review:
1. Flag immediately — do not queue the upgrade
2. List all callers of the changed contract
3. Require a migration spec before the change lands
4. Update lane to Guarded or Manual

## Circular Dependency Resolution

If upgrade A depends on B and B depends on A:
1. Extract the shared dependency into a new standalone upgrade C
2. Sequence: C → A → B
3. Document the extraction in both specs

## Competitive Awareness Rule

When a competitive gap is identified (feature competitor has, Nightwatch lacks):
1. Add to roadmap as a PROPOSED item immediately
2. Tag with source: competitive_gap
3. Do not auto-prioritize — flag to Dave for sequencing decision
4. Link to the competitor reference if available

## Planning Checklist

When Dave asks "what are we missing" or "what should we consider":
- [ ] Open items in NIGHTWATCH_STATE.md not yet specced
- [ ] AVLM dependencies blocking drafting features
- [ ] Amanda sign-off items blocking their downstream upgrades
- [ ] Security review findings from last phase end
- [ ] Competitive gaps identified since last planning session
- [ ] Technical debt items deferred from prior phases
- [ ] Graph integrity gaps (nodes/edges defined but not implemented)

## Reference Files

| File | When to update |
|------|---------------|
| docs/AVLM_PROJECT_CONTEXT.md | Upgrade affects AVLM architecture or voice model usage |
| docs/AVLM_INDEX.md | New voice/logic module ships |
| docs/NIGHTWATCH_STATE.md | After every merge |
| docs/NIGHTWATCH_CONFIG.md | Only when identity/config changes |

## Cross-File Awareness

When writing an upgrade spec, check:
- Does this touch any file referenced in NIGHTWATCH_STATE.md open items?
- Does this affect the AVLM drafting pipeline?
- Does this require an Amanda flag update?
- Does this change a shared contract? (trigger contract-change detection)
