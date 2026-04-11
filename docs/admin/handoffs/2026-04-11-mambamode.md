# Session Handoff — Mamba Mode — 2026-04-11

## Summary
Ran adversarial Signal Challenge against all active Mamba Mode signals. Discovered TOT-003's 63.8% win rate was computed from same-game FTA/PF (tautological correlation, not pregame prediction). Killed TOT-003, LIV-002 (pace arithmetic), ENV-004 (zodiac, no mechanism), ENV-003 (eclipse, no mechanism). Demoted LIV-001 to unvalidated. Ran 70-hypothesis hunt across 11 categories — zero new pregame signals found. Mamba Mode has zero confirmed pregame signals above 52.4% break-even.

## Decisions Made
1. **TOT-003 invalidated** — backtest used same-game stats; pregame version (season avgs) = 52.6%. Rejected: keeping as-is with disclaimer.
2. **LIV-002 killed** — tautological vs pregame line. Rejected: claiming it works with caveats.
3. **Zodiac + Eclipse killed** — no mechanism, effect sizes below vig. Rejected: keeping as Tier 2 modifiers.
4. **Strategic pivot** — stop pregame box-score mining. Rejected: trying more exotic stat combinations.

## Last Completed Action
Signal hunt script: 70 hypotheses, 8,909 games, zero actionable results.

## Unresolved Items
- Cursor prompt for false 63.8% removal not yet run
- H1 regression signal (53.3%, p=0.32) needs monitoring
- NE-017 Playoff Mode Cursor prompt ready but not run

## Open Items (Carry-Forward)
- NE-017 Playoff Mode — URGENT
- Live-line infrastructure for LIV-001 validation
- Poly Sharp wallet validation (30-game sample pending)
- Player prop engine build
- NE-019 Injury Alerts

## First Action Next Session
Run CURSOR_PROMPT_tot003_kill.md to remove false win rate, then run NE-017 Playoff Mode prompt.

## Last Commit SHA
Check GitHub — multiple commits this session to SIGNAL_REGISTRY.md, LIVE_SIGNALS.md, MAMBA_STATE.md, build-log.md, scripts/
