# Failed Attempts Log

| Date | Project | What Was Tried | Why It Failed |
|------|---------|----------------|---------------|
2026-04-10 | Admin | Perplexity API critique (first attempt) | 503 Service Unavailable — transient outage
2026-04-10 | Admin | Perplexity API critique (second attempt) | 503 Service Unavailable — retried after 5s, still down
2026-04-10 | Admin | micro-lesson persistent state via in-session tracking | No mechanism to enforce across sessions — switched to GitHub state file

2026-04-11 | Mambamode | Dune polymarket schema query | Free tier cannot access polymarket spellbook tables — Table does not exist
2026-04-11 | Mambamode | Bitquery wallet P&L query | Credit exhaustion risk; abandoned for Polymarket data API direct
2026-04-11 | Mambamode | Gamma API tag_slug=nba | Returned non-NBA markets; switched to keyword filtering on question field
2026-04-11 | Mambamode | NE-030B merge to main | 409 conflict (98 commits behind); resolved via file-by-file port to main
2026-04-11 | Mambamode | Bitquery ory_at_ token | Initially rejected as non-API key; confirmed it IS the Bitquery API v2 token

2026-04-11 | mambamode | signal_hunt.py join failed (0 enriched games) | Season format mismatch: odds uses int (2019), tgs uses string ('2018-19'). Fixed with odds_season_to_tgs() mapping.
2026-04-11 | mambamode | scipy.stats.binom_test removed | Upgraded to binomtest().pvalue in newer scipy.

2026-04-11 | Mambamode | Goldsky tokenId_in query for NBA wallet PnL | Timeout — large numeric token IDs cause statement timeout in Goldsky PNL subgraph. Fix: use conditionId with splits+redemptions on activity-subgraph instead.
2026-04-11 | Mambamode | series_id=10345 Gamma API filter for NBA markets | Returns 51K contaminated markets (non-NBA content dominates top volume). Fix: use tag=NBA parameter instead.
2026-04-11 | Mambamode | PolyRouter API signup via API endpoint | 404 — signup is web-only at polyrouter.io. Skipped based on Opus analysis (rate limits insufficient, OddsPapi already covers same data).
2026-04-11 | Mambamode | ProphetX API | Returns 403 on all tested endpoints — no public API access. Blocked.
2026-04-11 | Mambamode | Novig API | All endpoints blocked (403/tunnel failure). No usable API. Skipped.
2026-04-11 | Mambamode | Kalshi NBA market data via api.elections.kalshi.com with NBA filter | Returns 0 markets — NBA ticker filter not working as expected. Workaround: use OddsPapi which wraps Kalshi.
2026-04-11 | Mambamode | [UNCERTAIN] Goldsky demo API key from docs | Key 5fa709a5-0634... returned 401 — key may be expired/demo only. Need own account signup.

2026-04-11 | Mambamode | git pull origin main to fetch updated script | Merge conflict — branch NE-UPGRADE-032C had diverged 18 commits behind main, conflicts in build-log.md and seed_polymarket_wallets.py
2026-04-11 | Mambamode | Invoke-WebRequest to fetch script from private repo | 404 — raw.githubusercontent.com requires auth token, PowerShell Invoke-WebRequest cannot pass PAT easily
2026-04-11 | Mambamode | python -c one-liner to overwrite script | PowerShell single-quote handling caused stdin hang (>> prompt appeared)
2026-04-11 | Mambamode | fix_seed.py helper script write with default encoding | UnicodeEncodeError on Windows cp1252 — fixed by adding encoding="utf-8" to open()
2026-04-11 | Mambamode | fetch_nba_markets() via /events endpoint | Slow pagination through 5,100 events caused timeout — fixed to /markets endpoint
2026-04-11 | Mambamode | Running seed script via bash_tool | bash_tool timeout — 30s+ processes can't run here; requires local execution
