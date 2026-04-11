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


---

# Mamba Mode Handoff — 2026-04-11 (Session 26)

## Session Summary
Built and shipped the complete live game tracking infrastructure from scratch. A Supabase Edge Function polls ESPN every minute via pg_cron, capturing Q1 foul/FT/pts data for every NBA game and firing LIV-001/LIV-002 signals. App was simultaneously restructured — all dead spread signal pages deleted, new nav built around Live as primary page. First live validation: LIV-002 went 4-1 (80%), LIV-001 standalone went 0-3, confirming LIV-001 is not independently actionable. Kelly sizing at 3% cap ($30/bet on $1,000) yielded +$79.08 tonight.

## Decisions Made
1. **LIV-001 standalone not actionable** — only bet when LIV-002 fires. Live data: LIV-001-only 0-3, LIV-002 4-1.
   - Rejected: raising FT threshold, combining signals only
2. **App nav restructure** — Live (/) / Pregame / Track Record / Bankroll / Players. All spread pages deleted.
   - Rejected: keeping Research page as archive
3. **Supabase pg_cron over GitHub Actions** — 1-min cadence vs 5-min minimum on GHA.
4. **Pregame page deprioritized** — kaggle_games 2025-26 has FTA=0. Cannot compute TOT-003 without current-season FTA data.
5. **total_line_at_signal column** — captures line at exact moment signal fires for future line movement analysis.

## Last Completed Action
Poller v4 deployed + committed. Adds post-game handling (signal_result), total_line_at_signal capture, and result computation using signal-fire line (not opening line).

## Infrastructure State
- Edge Function: q1-live-poller v4 (ACTIVE)
- pg_cron: every 1 min
- Tables: live_game_states, live_signal_alerts (both have signal_result + total_line_at_signal)
- Repo: bitcoinbrainsweb/mamba-mode, main branch
- Base44 app: 69d2285f56e43c699b195c79

## Open Items
- NE-034: UI redesign (logos, larger fonts, signal outcome on cards, line movement) — not yet specced
- Pregame full implementation blocked — needs 2025-26 FTA/PF data decision
- Track Record rebuild — strip dead ATS picks, log LIV-002 OVER bets
- Line movement dataset: starts accumulating 2026-04-12 (column added tonight)
- NE-017 Playoff Mode — playoffs imminent, previously shelved

## First Action Next Session
Write NE-034 Cursor prompt for Live page UI redesign (logos, outcome badges, line movement delta).

## Failed Attempts
- pg_cron using net.http_post — pg_net not available on free tier, switched to http extension
- exec_sql RPC — schema cache miss, switched to Supabase MCP apply_migration
- kaggle_games as TOT-003 data source — FTA column is 0 throughout 2025-26 data
- Cursor ran play_by_play.csv commit (2GB) instead of dashboard — reset required, now gitignored
- Branch grep showing empty = file missing (false negative) — actual files were on feature branch

## Bet Sizing Reference
Bankroll: $1,000 | Bet: $30 (3% Kelly cap) | Odds: -110 | Break-even: 52.4%
LIV-002 expected win rate: 75.3% | Tonight: 80% (4-1)
