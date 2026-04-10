# Spec: AI Usage Logger
Project: Admin (cross-project)
Version: v1
Status: ACTIVE
Upgrade ref: ADMIN-LOGGER-001
Created: 2026-04-10
Last updated: 2026-04-10

---

## Problem Statement
There is no visibility into how many tokens are consumed per project, per feature, or per model across the Brainframe stack. Without this data, it's impossible to optimize costs, detect runaway usage, or plan capacity as the project portfolio scales. This spec defines a lightweight centralized logger that all projects instrument from day one.

## Users / Use Cases
- Dave: understand AI spend per project per week, spot anomalies, inform token optimization work (OI-008)
- Future: cost allocation per client (Nightwatch), budget gates per feature

## Success Metrics
- All active projects posting usage records within 2 weeks of logger release
- Weekly token burn visible per project in Supabase dashboard
- Zero instrumentation failures silently swallowed (logger must never crash the calling code)

## Requirements
1. Logger is a single utility function: `logAIUsage({ project, featureTag, model, inputTokens, outputTokens, sessionId?, notes? })`
2. Posts to `ai_usage_log` table in Admin Supabase (`wipwpvsmmpncarvfogbj`)
3. Uses service role key from REGISTRY.md — never anon key for writes
4. Fire-and-forget: logger call is non-blocking, never throws, never awaits in critical path
5. For direct Anthropic SDK projects (Axiom, Winston, Coinbeast, BitcoinBrains): use actual `usage.input_tokens` and `usage.output_tokens` from API response
6. For Base44 projects (Nightwatch, Mambamode): estimate tokens as `Math.round(promptString.length / 4)` for input, `Math.round(outputString.length / 4)` for output — label notes field as `"estimated"`
7. `feature_tag` is required and must be a kebab-case string describing the call site (e.g. `game-analysis`, `risk-narrative`, `ai-pulse`)
8. Logger must work in both browser (fetch) and Node/Deno environments
9. Each project gets its own copy of the utility — no shared package dependency

## Non-Goals
- Real-time dashboarding (Supabase dashboard is sufficient for now)
- Per-user token tracking
- Cost alerting or budget enforcement
- Replacing Base44's internal AIGenerationLog entity

## Constraints / Assumptions
- Admin Supabase URL: `https://wipwpvsmmpncarvfogbj.supabase.co`
- Service role key: in REGISTRY.md under `## Admin Supabase`
- Supabase Postgres 17, RLS enabled, service role bypasses RLS
- Base44 does not expose raw Anthropic token counts — estimation is intentional and acceptable
- Logger must not be imported into CLAUDE.md or any brainframe doc file

## Database Notes
- Table: `ai_usage_log` — already created in Admin Supabase via migration
- Columns: id (uuid), created_at (timestamptz), project (text), feature_tag (text), model (text), input_tokens (int), output_tokens (int), total_tokens (generated), estimated_cost_usd (numeric), session_id (text), notes (text)
- Indexes: project, created_at DESC, (project, created_at DESC)
- Migration: already applied — no further DDL required
- estimated_cost_usd: nullable, populate post-hoc via SQL if needed — do not compute in logger (pricing changes too often)
- OQ-001: Should we add a `version` column for model version pinning? (e.g. claude-sonnet-4-6 vs claude-sonnet-4-6-20260401)

## Open Questions
- OQ-001: Model version granularity — use full dated model string or friendly name?
- OQ-002: Should Base44 estimation log a flag column vs inline notes field? (current: notes field)

## Dependencies
- Admin Supabase project: `wipwpvsmmpncarvfogbj` (live)
- REGISTRY.md: service role key stored (confirmed 2026-04-10)
- Each project's Cursor prompt (one per project — see Cursor prompts section)

## Flows / Design Notes

### Logger utility (JS/TS — direct API projects)
```js
// utils/aiUsageLogger.js
const ADMIN_SUPABASE_URL = 'https://wipwpvsmmpncarvfogbj.supabase.co';
const ADMIN_SERVICE_KEY = '[from REGISTRY.md]';

export async function logAIUsage({ project, featureTag, model, inputTokens, outputTokens, sessionId, notes }) {
  try {
    fetch(`${ADMIN_SUPABASE_URL}/rest/v1/ai_usage_log`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': ADMIN_SERVICE_KEY,
        'Authorization': `Bearer ${ADMIN_SERVICE_KEY}`,
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify({
        project,
        feature_tag: featureTag,
        model,
        input_tokens: inputTokens ?? null,
        output_tokens: outputTokens ?? null,
        session_id: sessionId ?? null,
        notes: notes ?? null
      })
    }).catch(() => {}); // fire and forget — never throws
  } catch {}
}
```

### Usage at call site (direct API)
```js
const response = await anthropic.messages.create({ model, messages, max_tokens });
logAIUsage({
  project: 'axiom',
  featureTag: 'contract-analysis',
  model,
  inputTokens: response.usage.input_tokens,
  outputTokens: response.usage.output_tokens
});
```

### Usage at call site (Base44 estimated)
```js
logAIUsage({
  project: 'nightwatch',
  featureTag: 'risk-narrative',
  model: 'claude-sonnet-4-6',
  inputTokens: Math.round(renderedPrompt.length / 4),
  outputTokens: Math.round(outputText.length / 4),
  notes: 'estimated'
});
```

## Related Docs
- REGISTRY.md: `brainframe-comms/_docs/REGISTRY.md` — service role key
- Token optimization research: `brainframe-public/docs/token-optimization/TOKEN_RESEARCH.md`
- AI Pulse skill: standing LLM Stats watch added 2026-04-10
