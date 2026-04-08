# ADMIN_STATE.md
Last Updated: 2026-04-08

## Active Projects
- Nightwatch — AML/compliance SaaS
- Axiom — active
- Mambamode — NBA betting intelligence dashboard
- Coinbeast — Bitcoin product intelligence platform (pre-build)

## Work Completed This Session
- 6 admin specs built from STUB to ACTIVE (ai-pulse, critique-pipeline, decisions-bus, firecrawl, github-actions-sync, session-discipline)
- GPT-4o + Claude adversarial + DECISIONS.md cross-check critique run on all 6 specs
- 6 critique files saved to brainframe-comms/specs/admin/critiques/
- All 6 specs updated to v2 resolving critique findings
- sync.yml fixed: docs/admin/ now excluded from rsync
- docs/admin/ deleted from coinbeast/brainframe/ and nightwatch/brainframe/ (contamination resolved)
- SYNC_POLICY.md written to brainframe-public
- OpenAI API key saved to brainframe-comms/_docs/REGISTRY.md + memory
- GPT critique prompt templates written to brainframe-comms/skills/critique-spec/prompts/
- quitchat.md v1.1 — admin state paths + brainframe-comms references added
- gpt-critique.md — marked retired, redirects to critique-spec
- prompt-writing.md — SPEC GATE added

## Open Items
- [ ] Firecrawl OQ-001: check rate limits at firecrawl.dev dashboard (Dave)
- [ ] Firecrawl OQ-002: confirm Paperclip for Coinbeast knowledge graph (Dave)
- [ ] gpt-critique-skill: delete from skills provisioning repo if desired (Dave)
- [ ] Mambamode NE-UPGRADE-002 — blocked on Odds API key
- [ ] Stripe payout pause on Bitcoin Brains — unresolved
- [ ] Block Rewards DocuSign board resolution (Travis MacDonald) — FLAG IMMEDIATELY
- [ ] RESULT file critic gate — score Cursor RESULT files at session boot (carried)
- [ ] Mambamode Odds API key — NE-UPGRADE-002 blocked

## Next Session First Action
Resolve Firecrawl OQ-001 (rate limits) then write Coinbeast knowledge graph spec.

## Key Paths Reference
- DECISIONS.md write: brainframe-comms/_decisions/DECISIONS.md
- DECISIONS.md read (archive): brainframe-public/DECISIONS.md
- API keys: brainframe-comms/_docs/REGISTRY.md (OpenAI, Perplexity, Comms PAT)
- Specs: brainframe-comms/specs/admin/ (source of truth) + brainframe-public/specs/admin/ (mirror)
- Critiques: brainframe-comms/specs/admin/critiques/
