# Session Handoff — Mambamode — 2026-04-11

## Summary
Built and installed the `nba-data-scientist` skill v3 — a world-class analytical methodology skill that encodes elite quant practices (Gelman Bayesian workflow, walk-forward CV, SHAP, ensemble stacking, CLV benchmarking, DAG-based tautology detection, simulation-based power analysis). Ran Perplexity Deep Research on NBA data science methods, then two rounds of GPT-4o + Perplexity API critique. Drafted NE-035 Analytical Engine spec covering four tracks: composite pregame modeling, live signal expansion, event-level EPV (LSTM on PBP data), and production monitoring with CUSUM halt rules.

## Decisions Made
1. **Skill scope:** Data scientist skill is behavioral guardrails only (how to think), not project-specific data or architecture. Rejected: embedding Dave's lessons, embedding feature catalogs, embedding signal state.
2. **Deep learning excluded from v1:** XGBoost vs neural nets is 77.49% vs 77.26% on NBA data — marginal gain for significant complexity. Path 4 placeholder added for when PBP data is available. Rejected: including deep learning in v1.
3. **Critique decisions (all accepted):** Gap-window holdout (not just 2-season), RFE mandatory before composite builds, Brier score mandatory, simulation-based power analysis, hierarchical models as recommended default.
4. **NE-035 spec architecture:** Four tracks (composite pregame, live expansion, event-level EPV, monitoring). Rejected: single monolithic approach.

## Last Completed Action
NE-035 spec draft delivered to Dave via present_files.

## Open Items
- NE-035 spec needs saving to brainframe-comms + mirror to mamba-mode repo
- NE-035 spec critique not yet run (DRAFT status, pending)
- Signal challenge results (TOT-003 killed, LIV-002 killed) need propagation to METHODOLOGY.md and BACKTEST_FINDINGS.md
- build-log and MAMBA_STATE need updating (doing now)

## First Action Next Session
Resolve OQ-009 (current season data gap) — this blocks Track A. Then save NE-035 spec to repos and run critique.


---

# Session Handoff — Mamba Mode — 2026-04-11

## Session Summary

Deep research and design session covering prediction market intelligence, arb system architecture, and Polymarket historical data pipeline. No code was shipped. Session produced 10 new specs, updated MAMBA_STATE.md, and proved the Goldsky wallet seeding pipeline works. Key finding: Polymarket NBA has NO O/U totals — spread/moneyline only. SX.bet is the O/U prediction market venue. Bet365/Polymarket arb gap frequency is unknown and must be logged empirically before building execution infrastructure.

---

## Decisions Made

### D1: Bet sizing at $1K float = $30 flat (NOT Kelly)
Opus initially calculated half-Kelly at $120/bet for TOT-003 but this is wrong at $1K — 3 consecutive losses would destroy 36% of bankroll. Fixed fractional 3% = $30/bet is correct until 10x+ the bankroll.
Rejected: Kelly sizing at small bankroll.

### D2: Polymarket NBA = spread/moneyline only
51K markets under series_id=10345 are contaminated (non-NBA content). True NBA game markets fetched via `tag=NBA` on Gamma API. 959 closed markets confirmed. No O/U totals exist on Polymarket NBA.
Rejected: series_id=10345 filter.

### D3: Build price logger first, measure arb frequency empirically
Bet365 vs Polymarket historical gap data does not exist. Must log prices (4-venue, 4-min polling) for 2 weeks of playoffs before building alert/execution system.
Rejected: Building arb execution before knowing frequency.

### D4: Goldsky wallet seeder = splits + redemptions per conditionId
tokenId_in queries on Goldsky PNL subgraph timeout (numeric IDs too large). Correct approach: query activity-subgraph splits + redemptions per conditionId. Proven in session — 46 wallets from 15 markets.
Rejected: tokenId_in queries, The Graph (requires API key), Polygon node.

### D5: PolyRouter = skip
10 req/min free tier insufficient for 15-game polling. OddsPapi already covers Polymarket + Kalshi + sportsbooks. PolyRouter's additional platforms (ProphetX, Limitless) have weak NBA coverage.
Rejected: PolyRouter integration.

### D6: SX.bet vs Polymarket arb = fully automatable
Both have open APIs. When gap detected, both legs execute without manual step. Bet365 leg always manual (no API).
Rejected: Treating all arbs as semi-manual.

---

## Specs Written This Session (all saved to brainframe-comms + mamba-mode mirror)

| Ref | File |
|-----|------|
| NE-WALLET-001 | mamba-ne-wallet-001-polymarket-wallet-seeder-v1.md |
| NE-ARB-002 | mamba-ne-arb-002-full-arb-system-v1.md |
| NE-DIVERGENCE-001 | mamba-ne-divergence-001-cross-platform-signal-v1.md |
| NE-STEAM-001 | mamba-ne-steam-001-steam-move-arb-alert-v1.md |
| NE-ARB-001 | mamba-ne-arb-001-poly-bet365-arb-alert-v1.md |
| NE-MM-001 | mamba-ne-mm-001-polymarket-market-maker-hedge-v1.md |
| NE-EXT-001 | mamba-ne-ext-001-chrome-extension-bet365-autofill-v1.md |
| NE-SXBET-001 | mamba-ne-sxbet-001-sxbet-arb-signal-hedge-v1.md |
| NE-PROPHETX-001 | mamba-ne-prophetx-001-prophetx-signal-v1.md |
| NE-PROPS-001 | mamba-ne-props-001-correlated-props-signal-v1.md |

---

## Last Completed Action

Both specs (NE-WALLET-001, NE-ARB-002) saved to GitHub. MAMBA_STATE.md overwritten. Memory updated.

---

## Unresolved Items

- NE-017 Playoff Mode — Cursor prompt written, not run. TIME SENSITIVE — playoffs start soon.
- Polymarket CLOB wallet setup — ~1 hour, prerequisite for NE-ARB-002 execution
- SX.bet wallet setup — Polygon wallet + SX token for gas
- PWA service worker — prerequisite for push notifications
- Chrome extension build (NE-EXT-001) — standalone artifact
- Price logger — Phase 1 of NE-ARB-002, must start before playoffs for useful data
- NE-WALLET-001 full pipeline — 959 markets, ~45 min, dedicated session

---

## First Action Next Session

Run NE-017 Playoff Mode Cursor prompt. Then run NE-WALLET-001 Goldsky pipeline script.

---

## Carry-Forward Open Questions

- OQ: Does Mamba Mode have a PWA service worker? (Required for push alerts)
- OQ: Bet365 account limits — does arbing totals trigger soft limits?
- OQ: SX.bet write API — Polygon wallet signing, same wallet as Polymarket CLOB?
