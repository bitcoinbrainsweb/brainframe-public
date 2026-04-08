# Nightwatch Entity Reference
*Project-specific reference for base44-entity-design skill.*
*Loaded on demand when working on Nightwatch entities.*

## Canonical Graph Alignment

Every Nightwatch entity must map to a node in the canonical graph:
`Regulation → Risk → Control → Test → Evidence → Observation → Remediation → Assurance`

Ask before creating any entity:
- Which graph node does this entity belong to or support?
- Does it have a parent entity in the graph? What is the FK?
- Is there an existing entity that should be extended instead?

If the entity doesn't map to the graph and doesn't support a graph node: question it. Everything in Nightwatch connects to the graph or it doesn't belong.

## Entity Inventory (Current)

| Entity | Graph Node | Key FK |
|--------|------------|--------|
| Engagement | Root | — |
| Client | Root | engagement_id |
| RiskDomain | Risk | engagement_id |
| RiskFactor | Risk | domain_id |
| ControlLibrary | Control | — |
| Control | Control | library_id |
| ControlTest | Test | control_id |
| Evidence | Evidence | test_id |
| Observation | Observation | evidence_id |
| Remediation | Remediation | observation_id |
| AssuranceRecord | Assurance | engagement_id |
| DocumentIntelligenceItem | (AVLM) | engagement_id |
| ERSection | Report | engagement_id |
| ERDraftedSection | Report | section_id |
| QuizQuestion | (Amanda's Desk) | — |
| QuizAnswer | (Amanda's Desk) | question_id |
| AIGenerationLog | Audit | — |

## Repo Config
- Repo: `bitcoinbrainsweb/great-horn-aml-nightwatch`
- Entity JSON path: `base44/entities/EntityName.json`
- App ID: `69afb09f3cf8f7f93f857eb1`

## Pending Entities
- **NightwatchTask** — task management entity (NW-215, blocked on spec)
