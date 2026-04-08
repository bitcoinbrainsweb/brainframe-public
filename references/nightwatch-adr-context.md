# Nightwatch ADR Context
*Project-specific reference for the adr skill.*
*Fetch when writing ADRs in the Nightwatch project.*

## Nightwatch-Specific ADR Guidance

For **security/auth decisions**: include threat model impact and any FINTRAC audit trail implications.

For **data residency decisions**: reference DATA_POLICY.md Section 8. Note whether decision affects FINTRAC reporting obligations or where client data is processed.

For **AI provider decisions**: note Judgment Preservation constraints. Record whether human review is required before AI output is used in compliance deliverables.

For **graph schema decisions**: show impact on the canonical graph and whether existing nodes/edges are affected.

## ADR Storage
Save to: `docs/decisions/ADR-NNN-short-title.md` in the Nightwatch repo.
Update `docs/decisions/INDEX.md` with new entry after each ADR.
If decision supersedes a prior ADR, update the prior ADR status field.

## Open Decisions Requiring ADRs
- Data residency: Anthropic direct vs AWS Bedrock ca-central-1 (see DATA_POLICY.md §8)
- RLS design approach for Phase 11
- AI provider model selection rationale (Sonnet/Opus/Haiku assignment)
