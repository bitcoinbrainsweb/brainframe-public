# Axiom Research Context
*Project-specific reference for research prompt skills.*
*Loaded on demand when writing research prompts for Axiom.*

## Axiom Perplexity Space
The Axiom Perplexity Space contains the pattern library PDF and segment queue.
Always include in prompts: "Refer to the attached pattern library and segment queue."
This avoids re-researching tools already covered in completed segments.

## Axiom Rules for Research Prompts
1. Max 3 tools per Perplexity prompt — output cap constraint
2. Always include "Do not display in chat. Save as file for download only."
3. Always reference the Space files
4. No pattern generation in Perplexity — Claude does Phase B
5. No AI classification in Perplexity — Claude does Phase B
6. Flag NOT_FOUND — never estimate or infer
7. Bring output files back to Claude for integration

## Segment Sequencing
Current state lives in `_docs/segment-queue.md` in the Axiom repo.
Read that file — do not rely on this reference for current segment status.

Completed: Segments 1–6 (built-in stack, sales, marketing, ops/PM, support, finance/admin)
Remaining: Segments 7 (HR), 8A–8F (Verticals), 9 (Cross-cutting)

## GPT Deep Research — Axiom-Specific
For Axiom segment research, attach the pattern library PDF before submitting.
Use the segment queue to avoid duplicating completed segments.
