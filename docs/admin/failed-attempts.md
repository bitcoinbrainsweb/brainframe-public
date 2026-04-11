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
