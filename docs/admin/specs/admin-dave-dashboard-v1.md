# Spec: Dave Dashboard — Personal Command Centre
Project: admin
Version: v1
Status: DRAFT
Upgrade ref: TBD
Created: 2026-04-12
Last updated: 2026-04-12

---

## Problem Statement

Dave manages 8+ active projects simultaneously across multiple AI systems, with no single place to see project health, open blockers, daily AI news, and personal todos. Context-switching between GitHub, DECISIONS.md, and ad-hoc AI Pulse scans burns time and loses signal. This dashboard is a personal command centre — a single always-available view of what matters right now.

---

## Users / Use Cases

**Primary user:** Dave (desktop daily driver, mobile condensed view on the go)

Use cases:
1. Morning check-in — scan AI pulse digest, review open todos, check overnight project activity
2. Mid-session context switch — quickly see where each project is without opening multiple tabs
3. Mobile glance — condensed view of blockers and top AI news while away from desk
4. Manual refresh — trigger a fresh AI pulse or project status pull on demand

---

## Success Metrics

1. Dave opens the dashboard instead of manually scanning GitHub/DECISIONS.md for project status
2. AI Pulse digest is readable without triggering a full ai-pulse skill run
3. Todo system replaces scattered NEXT_ACTION.md items
4. Mobile view is usable in under 10 seconds

---

## Requirements

**AI Pulse Panel**
1. Fetch top AI news via Tavily API on hourly schedule
2. Manual "Refresh" button triggers an immediate Tavily fetch outside the schedule
3. Display: headline, source, 1-sentence summary, timestamp — max 10 items
4. Filter: Bitcoin/crypto news excluded unless significant (consistent with existing ai-pulse rules)
5. Pulse entries stored in Base44 — last 7 days retained, older auto-archived

**Project Status Panel**
6. Display one card per active project: Nightwatch, Axiom, Mambamode, Coinbeast, Winston, Bitcoin Brains, Block Rewards
7. Each card shows: last GitHub commit (date + message), open roadmap blockers (pulled from brainframe-comms _status files), current status (Active / Blocked / Dormant)
8. GitHub data refreshed hourly alongside AI pulse; manual refresh applies to both
9. Clicking a project card expands to show last 3 commits + full open blocker list

**Todo System**
10. Todos are created, edited, and completed within the dashboard — no external source
11. Todos have: title, project tag (dropdown from active project list), priority (High / Medium / Low), due date (optional)
12. Views: All, By Project, Due Today, High Priority
13. Completed todos archived (not deleted) — viewable in a separate "Done" list
14. Todos persist in Base44 entities

**Layout**
15. Desktop: three-panel layout — AI Pulse (left), Project Status (centre), Todos (right)
16. Mobile: single-column, condensed — AI Pulse collapsed to top 3 headlines, Project Status as a status-dot list, Todos as a simple checklist
17. Dark mode default

---

## Non-Goals

- No notifications or push alerts (v1)
- No multi-user access — Dave only
- No integration with external todo tools (Linear, GitHub Issues) — v1 is standalone
- No AI-generated summaries of project status — raw data only in v1
- No Supabase — Base44 handles all data persistence

---

## Constraints / Assumptions

- Tavily free tier: 1,000 req/month. Hourly refresh = 720/month. Manual refreshes must be rate-limited (max 1 per 5 minutes) to stay within free tier. ASSUMED: Dave will get a Tavily API key.
- GitHub API: unauthenticated = 60 req/hour. Authenticated PAT = 5,000 req/hour. Must use authenticated PAT for reliable polling across 8 projects. PAT stored in Base44 environment, not in frontend code.
- brainframe-comms _status files: currently exist for most projects but format varies. Dashboard should be tolerant of missing/malformed status files.
- Base44 free tier limits apply — no PII per ADR-001.
- Scheduled hourly refresh requires Base44 backend function or external cron (e.g., GitHub Actions). TBD which approach.

---

## Database Notes

**Base44 entities required:**

1. **PulseEntry**
   - Fields: id, headline (text), source (text), summary (text), url (text), fetched_at (datetime), archived (boolean)
   - Index on: fetched_at (for 7-day retention query)
   - Migration: new entity

2. **Todo**
   - Fields: id, title (text), project (enum: nightwatch|axiom|mambamode|coinbeast|winston|bitcoinbrains|blockrewards|admin), priority (enum: high|medium|low), due_date (date, optional), completed (boolean), completed_at (datetime, optional), created_at (datetime)
   - Index on: project, priority, completed
   - Migration: new entity

3. **ProjectSnapshot**
   - Fields: id, project (enum), last_commit_message (text), last_commit_date (datetime), last_commit_sha (text), blockers (json array of strings), status (enum: active|blocked|dormant), fetched_at (datetime)
   - One record per project — upsert on refresh, not append
   - Migration: new entity

OQ-DB-001: Does Base44 support scheduled backend functions (cron)? If not, hourly refresh must be triggered by GitHub Actions or an external scheduler calling a Base44 API endpoint.
OQ-DB-002: Base44 enum fields — confirm supported before designing project/priority enums. Alternative: text fields with frontend validation.

---

## Open Questions

OQ-001: How does the hourly scheduler work in Base44? If cron is not supported natively, need a GitHub Actions workflow that POSTs to a Base44 backend function every hour. Evaluate before build starts.
OQ-002: Tavily rate limiting — should the manual refresh button be disabled for 5 minutes after use, or should we show a countdown timer?
OQ-003: brainframe-comms _status files — should the dashboard parse these directly via GitHub API, or should each project DAI be responsible for writing a structured JSON status file that the dashboard reads?
OQ-004: Block Rewards project status — no GitHub repo. How should this project's card be populated? Manual entry only?
OQ-005: Mobile breakpoint — does Base44 support custom responsive layouts, or does this require CSS overrides?
OQ-006: Todo due dates — should overdue todos surface a visual alert (red highlight), or just sort to top?

---

## Dependencies

- Tavily API key (Dave to obtain: tavily.com)
- GitHub PAT with read access to all project repos (Admin PAT already exists in REGISTRY.md)
- Base44 backend function support (OQ-001 gates build start)
- brainframe-comms _status file format standardisation (OQ-003)

---

## Flows / Design Notes

**Desktop layout:**
```
┌─────────────────┬──────────────────────┬───────────────┐
│   AI PULSE      │   PROJECT STATUS     │    TODOS      │
│                 │                      │               │
│ [Refresh] 12:04 │ Nightwatch  ● Active │ ▶ High        │
│                 │ Axiom       ● Active │   [ ] item    │
│ • Headline 1    │ Mambamode   ● Active │   [ ] item    │
│ • Headline 2    │ Coinbeast   ● Dormant│               │
│ • Headline 3    │ Winston     ● Active │ ▶ Medium      │
│ • ...           │ BB          ● Active │   [ ] item    │
│                 │ Block Rwd   ● TBD    │               │
└─────────────────┴──────────────────────┴───────────────┘
```

**Mobile layout:** Single column — pulse (3 headlines collapsed), project dots, todo checklist.

---

## Related Docs

- FUTURE_INTEL.md: Tavily AI entry (2026-04-12)
- FUTURE_INTEL.md: Free-for-Dev stack gaps entry (2026-04-12)
- DECISIONS.md: Admin self-note on Tavily + daily update skill (2026-04-12)
- brainframe-comms/specs/admin/admin-ai-pulse-v1.md (existing ai-pulse spec — this dashboard supersedes standalone ai-pulse for Dave's personal use)
