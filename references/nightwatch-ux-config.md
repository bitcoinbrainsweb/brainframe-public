# Nightwatch UX Config
*Project-specific reference for the ux skill.*
*Fetch when doing any UX work on Nightwatch.*

## The Two Users

Every design decision is filtered through one of two lenses. When they share
a screen, optimize for Amanda and add orientation cues for clients —
never the reverse.

### Amanda — Compliance Expert, Power User
- Works inside Nightwatch daily, across multiple engagements
- Arrives at every screen with intent — she already knows what she wants
- Time is billable. Every extra click has a dollar cost
- Failure mode: burying her next action behind summaries, confirmations, or dead screens
- Design standard: 2 clicks or fewer from screen landing to routine task completion
- Amanda-first is a core Nightwatch design principle

### MSB/VASP Client — Portal User, Infrequent
- May log in monthly or less, does not remember the layout
- Arrives without a clear next action — needs orientation
- Failure mode: dropping them into complexity with no obvious entry point
- Design standard: no compliance terminology, no internal IDs, plain language status

## Amanda-Specific Accelerators
- Bulk confirm available when 2+ items are in the same confirmable state
- Keyboard shortcuts for accept/reject on review items (future roadmap)
- Filters and sort persist across sessions within an engagement
- "Quick confirm all matched" available on post-import when zero errors exist

## Nightwatch-Specific Screen Guidance

### Post-Import Screen
The stat strip format: `42 matched · 3 need review · 1 error`
Each value filters the section list below. Amanda lands here and starts work
immediately — there is no separate "go to results" step.

### Engagement Overview Screen
- Status badge top-left (In Progress / Awaiting Review / Complete)
- Next required action top-right — always a button, never a label
- Section progress compact: "14 of 19 sections reviewed"
- Recent activity below the fold

### Client Portal Screen
- Single primary action above the fold
- Engagement status in plain language
- No section names, no IDs, no compliance jargon visible to clients

## Terminology
- Amanda's work = Effectiveness Review — never "audit"
- Client-facing = MSB/VASP portal — not "admin panel"
- Section = ER section — not "report section" or "chapter"

## Design Decisions Log
*Add dated decisions here as they are made.*
- 2026-04-07: Amanda-first principle established as non-negotiable. When
  Amanda and client needs conflict on a shared screen, Amanda wins.
