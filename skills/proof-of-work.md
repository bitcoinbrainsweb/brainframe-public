---
name: proof-of-work
description: "Generate a Proof of Work report for any software project. Run when asked \'proof of work\', \'pow\', or \'how much have we built\'. Reports lines of code, estimated human team build time, AI leverage ratio, cost at market rate, and velocity. Always uses live GitHub API data."
---

# Proof of Work
Version: 1.0

Generate a structured report showing project size, complexity, velocity, and AI leverage ratio.

## Trigger

"proof of work", "pow", "how much have we built", "show me the stats", "what have we shipped"

## Required Inputs

- Repo path (owner/repo)
- GitHub PAT (if private)
- Start date (if different from repo creation date)
- Dave's actual hours spent (ask if unknown — default 3hrs/day)

## Data to Fetch (GitHub API)

```
GET /repos/{owner}/{repo}/git/trees/main?recursive=1   # file tree + sizes
GET /repos/{owner}/{repo}                               # created_at, metadata
GET /repos/{owner}/{repo}/commits?per_page=1            # total commit count via Link header
GET /repos/{owner}/{repo}/commits?since=<7d_ago>        # week 0 velocity
GET /repos/{owner}/{repo}/commits?since=<14d_ago>&until=<7d_ago>   # week -1
GET /repos/{owner}/{repo}/commits?since=<21d_ago>&until=<14d_ago>  # week -2
```

## Calculations

**LOC:** sum src file sizes / 45 (chars per line for JS/JSX/TS)
**Human build time:** LOC / 150 (lines/day per senior dev) × domain multiplier
**Domain multipliers:** standard CRUD = 1.0×, regulated/complex = 1.4–1.8×
**Cost:** human dev-weeks × team rate (ask for local market rates if unknown)
**AI leverage:** estimated human hours / actual hours spent

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PROOF OF WORK — [Project]
  Generated: [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📐 SIZE
  Source LOC (est):  ~XX,XXX
  Source files:      XXX

📅 TIME
  Project age:       XX days
  Total commits:     X,XXX

🤖 AI LEVERAGE
  Est. human build:  XX dev-weeks
  Cost at market:    ~$XXX,XXX
  Actual time:       ~XX hours
  ──────────────────────────────
  AI Leverage:       XX×
  ──────────────────────────────

📈 VELOCITY
  Week −2: NNN [bar]
  Week −1: NNN [bar]
  Week  0: NNN [bar]
  Trend: [Accelerating/Steady/Decelerating]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
