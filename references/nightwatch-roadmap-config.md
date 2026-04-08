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
