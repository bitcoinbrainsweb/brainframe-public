# Nightwatch Writing Context
*Project-specific reference for the technical-writing skill.*
*Fetch when writing documentation for the Nightwatch project.*

## Audience Profiles

- **MSB/VASP portal users** — plain language, action-oriented, no jargon, numbered steps
- **Compliance professionals** — precise regulatory language, citations where relevant
- **Regulators/auditors** — formal, evidence-backed, no hedging
- **Developers** — concrete, example-driven, structured

## Document Type Patterns

### User-Facing Guides (Nightwatch client portal)
- Lead with what the user is trying to accomplish
- Use numbered steps for procedures
- Avoid mentioning implementation details (entities, functions, etc.)
- End each section with 'what happens next'

### Compliance Methodology Descriptions
- Cite the specific regulation (PCMLTFA, SOR/2002-184, etc.)
- State the obligation → state the test → state the evidence required
- Use Amanda's terminology: Effectiveness Review (not audit), observations, recommendations
- Separate factual findings from recommendations clearly

### Engagement Letters and Client-Facing Reports
- Executive summary first — 3-5 sentences, no jargon
- Scope section: what was reviewed, what was not
- Findings section: observation → evidence → risk rating → recommendation
- Risk table at end with colour-coded ratings
- Consistent tone: professional, direct, non-accusatory

## Style Rules
- **Effectiveness Review** not 'audit' (for Amanda's work)
- **FINTRAC Audit** only when referring to a FINTRAC-conducted examination
- **MSB** and **VASP** not 'client' in regulatory context
- **Reporting entity** when referring to entities with PCMLTFA obligations
- Canonical graph node names always capitalized: Policy, Procedure, Risk, Control, etc.
- Never say 'AI-generated' in client-facing output — say 'draft' or 'prepared'

## Review Checklist Addition (Nightwatch)
- [ ] Is terminology consistent with Nightwatch style rules above?
- [ ] Would a new compliance officer at Great Horn understand this without asking?
- [ ] Are recommendations clearly separated from observations?
- [ ] Is the risk rating table complete if this is a review report?
