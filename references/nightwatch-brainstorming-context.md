# Nightwatch Brainstorming Context
*Project-specific reference for the brainstorming skill.*
*Fetch when brainstorming features or architecture for Nightwatch.*

## Design Principles

Every feature must strengthen or serve the canonical graph:
Policy → Procedure → Operation → Risk → Control → Test → Evidence → Observation → Remediation → Assurance → Effectiveness Review

- Additive only — no breaking changes to existing graph nodes
- Role checks always go through roleUtils.js — never raw arrays
- Amanda's work = Effectiveness Review, never 'audit'
- Every new entity must map to a graph node before being built
- No side systems — if it doesn't connect to the graph, question whether it belongs
