# NEXT_ACTION — Admin DAI
Last updated: 2026-04-10

## FIRST ACTION NEXT SESSION
Run Nightwatch logger Cursor prompt — in brainframe-comms DECISIONS.md dated 2026-04-10 "Nightwatch — AI usage logger Cursor prompt". Paste into Cursor in Nightwatch project. Verify data lands in Admin Supabase ai_usage_log.

## OPEN ITEMS
- [ ] Nightwatch logger Cursor prompt — needs running (prompt in DECISIONS.md 2026-04-10)
- [ ] brainframe-private — decide if scope should expand beyond Coinbeast (currently: team context + conflict disclosures only)
- [ ] AI usage dashboard — query Admin Supabase and visualize token burn per project per week (no spec yet)
- [ ] Axiom, Winston, Coinbeast, BitcoinBrains — logger bakes in at first AI call (spec: admin-ai-usage-logger-v1.md)
- [ ] TRANSCRIPT-BUILD-004 — Instagram auth via dummy account. Create throwaway IG account, grab sessionid cookie from DevTools, paste in next Admin session to wire into transcript service + Render env vars
- [ ] Nightwatch AML credibility detection spec — flagged to FUTURE_INTEL, stub spec next Nightwatch session
- [ ] Bitcoin Brains deck — human media moat section needs defining (owner, content, timeline TBD)
- [ ] Coinbeast AEO spec v1 — DRAFT in brainframe-comms/specs/coinbeast/coinbeast-founder-network-aeo-v1.md — critique pending next Coinbeast session
- [ ] Memory edits at cap (30) — review and consolidate before next session

## RESOLVED THIS SESSION
- [x] LOGGER_API_KEY set in Supabase + stored in REGISTRY.md
- [x] ai_usage_log table created in Admin Supabase
- [x] log-ai-usage edge function deployed and smoke-tested
- [x] Axiom ai-validator.js patched with inline logger
- [x] Mamba test table dropped
- [x] 9 FUTURE_INTEL entries written (MemPalace, Ruflo, Coinbeast AEO, black hat white hat, Nightwatch AML credibility, human media moat, Instagram auth, Stitch MCP + 21st.dev)
- [x] Coinbeast founder network AEO spec v1 written + mirrored + DECISIONS.md message sent to Coinbeast DAI

## FLAGGED 2026-04-12 — ACTION TOMORROW

- [ ] **Credential storage upgrade** — migrate REGISTRY.md from GitHub to GitHub Secrets + 1Password. REGISTRY.md becomes hashed refs only. (Plex critique: PAT compromise = all keys exposed)
- [ ] **Nightwatch sync scope** — decision needed: does Nightwatch prod repo need access to brainframe-public admin/ content? Current GitHub Actions sync copies everything including docs/admin/*. Likely answer: NO. Fix: exclude admin/ from sync workflow.
- [ ] **Unified admin dashboard** — design session needed. Visibility across Supabase/Stripe/Sentry/Render/GitHub Actions all projects. Flag for design.
- [ ] **quitchat failure runbook** — write QUITCHAT_RUNBOOK.md. Distraction = unsaved ADMIN_STATE across 6 repos. Fix path needed.
- [ ] **DECISIONS.md sharding** — cross-project decisions must double-store: in `brainframe-comms/_decisions/DECISIONS.md` AND in each affected project's status/decisions file. Single-project decisions stay local. Prevents 5000-word cap choke at 8+ projects.

## NOTE — NOT ACTING ON
- PAT rotation policy — Dave decision: no forced rotation policy at this time.
