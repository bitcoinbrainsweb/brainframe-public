# Base44 Master Research Report
*Merged: 2026-04-08 | Sources: Claude research + Perplexity deep research*

---

## 1 — What Base44 Is

- AI-powered full-stack app builder: describe an app in plain English → deployed frontend, database, auth, hosting
- Founded early 2025 by Maor Shlomo (Israeli solo founder). 10k users in 3 weeks, 250k in 6 months, ~$200k/mo MRR before acquisition
- Acquired by Wix (NASDAQ: WIX) for $80M cash in June 2025. Operates as standalone product. 8-person team received $25M retention bonus.
- 400k+ users, 5M+ generated apps as of early 2026
- Also positioned as a **developer backend platform** — same backend powering the app editor exposed as standalone SDK/CLI for AI agents and developers
- MCP servers explicitly designed for AI assistants (ChatGPT, Claude, Cursor) to create and manage Base44 apps
- Core promise: "describe it → it exists." Reality: excellent for MVPs and internal tools, degrades badly under complexity, zero exit path for backend

---

## 2 — Core Capabilities

**What it generates:**
- React frontend (confirmed via GitHub export)
- Auto-provisioned NoSQL database (MongoDB-compatible)
- Built-in auth: OAuth, magic links, traditional passwords, RBAC, session handling
- File storage (File field type — specific size limits NOT documented)
- Hosting with instant deployment
- Auto-generated CRUD API endpoints
- Built-in analytics
- Email/SMS via integrations (no extra setup)
- Real-time updates (subscription model — specific transport mechanism not documented)

**Field types supported:**
- Text, Number, Yes/No (Boolean), Date/Time, File, Reference, Object
- Reference fields link tables (e.g., order → customer, TeamMember → User)
- Object fields support JSON-like structures but can cause schema errors if misconfigured

**Multi-user/collaboration:**
- Workspaces introduced July 2025 (up to 2 per account, view/edit roles)
- Multi-role apps supported — tested at 3 roles (gym scheduling app)
- Row-level and field-level security per entity

**Code editing:**
- Manual code editor: Starter+
- GitHub sync: Builder+ (frontend only — backend stays on Base44 infra)
- `npx skills add base44/skills -g` installs AI agent skills for CLI-assisted development

**AI models (Builder+):**
- Claude Sonnet 4 (default), Claude Opus 4.5, Claude Sonnet 4.5
- Gemini 2.5 Pro, Gemini 3 Pro, GPT-5
- Platform auto-selects; can override

**What it cannot do:**
- No native mobile (web only)
- Backend cannot be exported or run outside Base44 infra
- No end-to-end testing — manual testing only
- No SOC 2 / ISO 27001 (as of late 2025)
- Unsupported npm packages → silent build failure
- Login/signup UI stays Base44-branded even with custom domain (Builder+)
- No credit top-ups — must upgrade plan tier or wait for billing cycle

---

## 3 — MCP Integration

### Official MCP Server
**URL:** `https://app.base44.com/mcp`  
**Auth:** OAuth only (not API key). One-time sign-in per tool. Builder plan+.

**Tools:**

| Tool | Type | What it does |
|------|------|-------------|
| `create_base44_app` | ASYNC | Create new project from text description — returns editorUrl immediately, build runs in background |
| `edit_base44_app` | ASYNC | Modify existing project — same async pattern |
| `list_user_apps` | sync | List all projects, filterable by name |
| `list_entity_schemas` | sync | Get entity schemas for a project |
| `query_entities` | sync | Read records from an entity (filter, limit — no write) |
| `get_app_status` | internal | Poll build progress — not for direct use |
| `get_app_preview_url` | internal | Get preview link after build — not for direct use |
| `create_entities` | sync | Create entity **records** (instances) in existing entity — NOT schema creation |

**What MCP cannot do (critical gaps):**
- Cannot create, update, or delete entity **schemas** — requires CLI (`entities push`) or UI
- Cannot create, update, or delete records directly (only `query_entities` for reads; `create_entities` adds records to existing entities)
- Cannot manage backend functions, auth rules, or security rules
- Cannot do anything requiring visual editor or UI config

### Docs MCP Server (separate)
**URL:** `https://docs.base44.com/mcp`  
**Auth:** None (public)  
**Tools:** Single search tool — queries live Base44 docs, returns excerpts + links. Use from Cursor/Claude for SDK questions.

### SDK / CLI (non-MCP)
- SDK docs: `https://doc-sdk.base44.app` (unofficial mirror) and `https://docs.base44.com/developers/references/sdk`
- CLI: `entities push` deploys entity schemas. `deploy` deploys full project.
- Entity schemas: JSON files in `base44/entities/` directory
- Community MCP (unofficial): `github.com/maorfr/base44-mcp` — `get_app_entity_instances` (read only)

---

## 4 — Entity System Deep Dive

- **Backend:** MongoDB-compatible NoSQL. Documents per entity. No migrations required (flexible schema).
- **Schema definition:** JSON Schema files in `base44/entities/`. Deploy via `entities push`.
- **Relations:** No native foreign keys. Use Reference fields (store IDs), join in frontend logic.
- **Real-time:** Subscribe to create/update/delete events per entity.
- **Security:** Row-level (RLS) + field-level security rules. Auth0/Okta can be layered.
- **Import behavior:** Append-only. Re-import with schema changes requires deleting existing records first. Schema changes only applied "where safe" — silent partial application possible.

**Known failure modes:**
- Object fields with input type mismatch → `properties is required for object type` error → blank screen post-publish (silent)
- App names with emoji/special characters → `UnicodeEncodeError` → permanent editor lockout
- Schema-data mismatch after editing live entity → blank screen (no warning)
- RLS misconfiguration (common in AI-generated security rules) → 403 errors or silent data exposure
- Import schema mismatch → Base44 updates "where safe," silently skips the rest

---

## 5 — AI Builder (Prompt Interface)

**How it works:**
- Conversational builder chat (consumes message credits per prompt, success or failure)
- **Discussion Mode:** brainstorm without triggering a build — zero credits consumed
- **Visual editor:** click-to-tweak colors, copy, layout — zero credits consumed
- "Revert this" button per prompt — instant undo
- Supports image/doc/video/audio attachments in prompts

**Prompt format that works:**
- Include: entities, key fields, auth requirements, workflow in one concise description
- Example: "Create a task management app with users, tasks with due dates and priority levels, and team assignments. Add authentication and deploy it."
- For edits: entity-focused, targeted — "Add a follow-up date field to the Contacts entity"
- Single strong workflow per build > feature-heavy builds ("apps with one strong workflow perform better and are easier to improve")

**What it follows reliably:** High-level structure, style tokens, multi-role auth, entity-level modifications  
**What it breaks:** Complex state logic, iterative edits on large apps (rewrites components it shouldn't), unsupported packages (generates code, fails at deploy), heavy builds (sandbox timeout)

**Credit mechanics:**
- 1 message credit per prompt (regardless of outcome)
- 1 integration credit per user-triggered integration in deployed app
- Bug-fix loops = #1 credit killer (broken code → AI fix → still broken → repeat)
- Credits don't roll over. No top-ups. Hit limit → building stops AND deployed app integrations stop.

---

## 6 — Pricing (verified Feb 2026)

| Plan | Monthly | Annual | Msg Credits | Integration Credits | Key unlocks |
|------|---------|--------|-------------|-------------------|-------------|
| Free | $0 | $0 | 25/mo (5/day cap) | 100 | Core features only. Private apps removed Feb 6 2026. |
| Starter | $20 | $16 | 100 | 2,000 | Code editing, private apps, no custom domain |
| Builder | $50 | $40 | 250 | 10,000 | Custom domain, GitHub, backend functions, model select, MCP |
| Pro | $100 | $80 | 500 | 20,000 | Beta access, priority support |
| Elite | $200 | $160 | 1,200 | 50,000 | Max limits, priority support |

**Gotchas:**
- No credit top-ups — upgrade tier or wait for cycle reset
- Both credit types can block you independently (build credits OR integration credits)
- Custom domain login pages stay Base44-branded (not white-label)
- GitHub export = frontend only — backend permanently locked to Base44 infra
- MCP requires Builder+
- No money-back guarantee
- No subscription self-cancel in UI — users report having to block payment to stop charges

---

## 7 — Known Failure Modes

**Infrastructure:**
- Feb 3, 2026: platform-wide outage, 2h 53min. ALL apps → 502. Builder inaccessible. Support unresponsive.
- Feb 17 and Feb 20, 2026: additional incidents. Single infra failure = every app on the platform goes down simultaneously.

**Security (patched, but tells you about the architecture):**
- July 2025 (Wiz): `app_id` hardcoded in URI paths → anyone could register as user of private apps without auth. Patched in 24h.
- March 2025 (Imperva): stored XSS in app builder, open redirect leaking JWTs, client-side-only premium feature enforcement. Partial fixes April 2025.
- Gradio API file path traversal exposing env vars — status unknown.

**AI builder patterns:**
- Fix-one-break-one: fixing a bug routinely breaks adjacent functionality
- Credit drain loop: broken build → AI fix attempt → still broken → repeat, credits burn each cycle
- Context loss: AI forgets earlier decisions in long sessions
- Unsupported packages: generates code, fails silently at deploy
- Sandbox timeouts: heavy dependency trees hit runtime limit, credit burned

**Entity / data:**
- Schema-data mismatch = silent blank screen post-publish
- Special characters in app names = permanent editor lockout
- RLS misconfiguration (AI-generated) = 403s or silent data exposure
- Import is append-only — schema mismatch silently applies partial changes

**Trustpilot: 2.2/5 from 433 reviews, 66% one-star:**
- Credits drain in debugging loops with no usable output
- No self-cancel — must block payment
- Workspace lock-in (30+ days of work lost to permissions trap reported)

---

## 8 — Actionable Insights for Our Workflow

### A — MCP Mental Model (what Claude can and cannot do)

```
AVAILABLE VIA MCP:
  READ:    list_user_apps, list_entity_schemas, query_entities
  WRITE:   create_entities (records only — entity must already exist)
  BUILD:   create_base44_app (async), edit_base44_app (async)
  POLL:    get_app_status (after async build calls — always poll before assuming done)

NOT AVAILABLE VIA MCP (→ CLI or UI):
  - Create / update / delete entity schemas
  - Update / delete records
  - Backend function management
  - Auth / security rule changes
  - Visual editor operations
```

**Rule:** I must never attempt schema DDL via MCP. If a schema needs to change → Cursor writes CLI command (`entities push`). Full stop.

---

### B — Prompt Discipline Rules (to stop burning credits)

1. **Discussion Mode first.** Before any build prompt, use Discussion Mode to lock requirements. Zero credits. Switch to build only when spec is confirmed.
2. **One feature per prompt.** Never bundle features. Each prompt = one scoped change.
3. **Revert immediately on break.** Never prompt-fix a broken component. Revert → adjust spec → rebuild targeted.
4. **Visual editor for cosmetic changes.** Color, copy, layout → never use a build prompt for these.
5. **Pre-spec entity schemas in JSON** before sending to the AI builder. Don't let the AI infer schema from vague language.
6. **Never use unusual npm packages.** No official supported list exists. Stick to common libraries. Unknown packages = silent build failure.

---

### C — Entity Design Rules (to stop blank screens and schema errors)

1. **Spec schemas as JSON files first** — then deploy via `entities push`. Never rely on AI to infer schema.
2. **Treat schema changes on live apps as high-risk.** Mismatch = silent blank screen. Always test in a non-production app first.
3. **Import is append-only.** If re-importing with schema changes, delete existing records first.
4. **Object fields are fragile.** Type-check all inputs to Object fields. Mismatch = `properties is required` error + blank screen.
5. **No emoji or special characters in app names.** Ever. Causes permanent editor lockout.
6. **Review AI-generated RLS rules manually.** AI generates security rules that look right but silently expose data or return 403s.

---

### D — Infrastructure Risk Posture

- Base44 has had 3 incidents in 6 weeks (Feb 2026). All apps share infra — one failure = everything down.
- **For Nightwatch:** do not use Base44 for anything client-facing or compliance-critical. Keep it for internal tooling and rapid prototyping only.
- **For any Base44 app with real users:** document the outage risk explicitly. Build a status monitoring alert (UptimeRobot or equivalent against your Base44 subdomain).

---

### E — Session Workflow Change (immediate)

**Before any Base44 session:**
1. Load `base44-entity-design` skill
2. Confirm entity schemas exist before attempting any `create_entities` MCP call
3. After any `create_base44_app` or `edit_base44_app` call → poll `get_app_status` before proceeding
4. Use Docs MCP (`https://docs.base44.com/mcp`) from Cursor for any SDK/entity questions rather than relying on memory

---

## Sources

**Claude research:** Official docs, Trustpilot, Imperva security research, Wiz vulnerability disclosure, Shipper.now failure modes, AllAboutCookies review, nocode.mba  
**Perplexity research:** Official docs, Wavespeed review, Rocket.new comparison, Base44 Developer Platform docs, r/nocode, r/Base44, Banani.co pricing, YouTube tutorials, Capterra, Product Hunt, LobeHub SDK MCP listing
