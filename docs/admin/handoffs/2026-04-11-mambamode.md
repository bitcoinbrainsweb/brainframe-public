# Session Handoff — Mamba Mode — 2026-04-11

## Summary
Built and shipped NE-004A: Polymarket Sharp Wallet Signal end-to-end in one session. This adds a new signal layer to every game card showing whether profitable Polymarket wallets have taken positions on tonight's NBA games. The feature includes a complete spec (v6, critiqued by Opus + GPT + Perplexity), a Cursor-built implementation (polymarketPoller.js, usePolySharp.js, GameCard badge), 5 Supabase tables, and 40 seeded wallets sourced live from the Polymarket data API. The signal idea originated from an Instagram reel about copy-trading profitable prediction market wallets.

## Decisions Made

### D-001: Wallet copy-trading signal = read-only signal layer only
- Approach: surface Polymarket wallet positions as a badge signal, no execution
- Rejected: automated copy-trading bot (scope too large, regulatory risk)

### D-002: Dune Analytics for historical P&L seed
- Approach: Dune free tier for bootstrap
- Rejected: Bitquery (7-day window only), manual curation
- Reality: Dune free tier cannot access polymarket spellbook tables — fell back to Polymarket data API (gamma-api + data-api) for live seed. Workaround works but win_rate is NULL for all wallets until markets resolve.

### D-003: Wallet selection — ≥10 trades, ≥65% win rate, bot-filtered
- Approach: 65% seed floor, de-list at 60%, inter-trade timing + hedge ratio bot filters
- Rejected: 58% threshold (Perplexity found this too low), no bot filtering

### D-004: Tiered signals — Poly Lean (1 wallet) vs Poly Sharp (2+ wallets)
- Approach: tiered display with wallet count in tooltip
- Rejected: hard NoSignal cutoff at <2 wallets

### D-005: Hybrid confidence scoring
- Formula: 0.7 × (log10(relative_size)/log10(100)) + 0.3 × (log10(abs/10K)/log10(10))
- Rejected: pure relative sizing (over-weights small bettors scaling up), pure absolute

### D-006: Poly conflict badge
- Approach: orange conflict badge when Poly Sharp opposes LIV-001/LIV-002, same pattern as playoff conflict detector
- Rejected: muting either signal

### D-007: Append-only polymarket_signals table
- Approach: every poll inserts a new row; UI reads latest per game_id
- Rejected: upsert-only (loses signal drift history for backtesting)

### D-008: Position size — no floor
- Approach: all positions count; confidence display scales by relative size
- Rejected: $500 floor (small bets from historically small bettors are still signal)

## Last Completed Action
Seeded 40 wallets into polymarket_wallets via Polymarket data API (all 102 NBA condition IDs scraped, 3+ trade threshold, sorted by total volume).

## Open Items (carry-forward)
- win_rate NULL for all 40 wallets — populates as markets resolve (30-game validation cycle)
- Dune free tier insufficient for Polymarket historical P&L — upgrade path: Dune Analyst ($50/mo) or Allium
- LIV-001/LIV-002 conflict badge dormant — activates when those signals are built
- Weekly wallet refresh cron — not yet automated (runs manually via Dune/data API)

## First Action Next Session
Run NE-017 Playoff Mode Cursor prompt — playoffs start in ~2 weeks. URGENT.

## Last Commit SHAs
- mamba-mode main: check via GitHub API (multiple commits this session)
- brainframe-comms: NE-004A spec v6 + critique artifacts

## Failed Attempts This Session
- Dune `polymarket` schema → Table does not exist (free tier)
- Dune `polymarket_polygon.trades` → Table does not exist
- Bitquery ad-hoc wallet query → Credit exhaustion risk, abandoned for data API
- Gamma API with tag_slug=nba → returned non-NBA markets (tag not working)
- NE-030B → main merge → 409 conflict (98 commits behind); resolved via file-by-file port
