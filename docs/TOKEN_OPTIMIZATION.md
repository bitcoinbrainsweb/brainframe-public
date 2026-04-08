# Token Optimization Plan — Brainframe Global Standard
**Version:** 2.0 | **April 2026** | **Applies to: all projects**

---

## Priority Order

**Quality first. Speed second. Token cost third.** Never sacrifice output quality for cost. Never sacrifice speed on user-facing surfaces for marginal token savings. Eliminate waste — don't cut corners.

---

## Model Routing

| Task Type | Model | Rationale |
|-----------|-------|-----------|
| Architecture, deep compliance reasoning, long-horizon planning | Opus 4.6 | Use only where quality gap is real |
| Analysis, narrative, multi-step reasoning, client-facing content | Sonnet 4.6 | Default for interactive sessions |
| Classification, formatting, data parsing, routing logic | Haiku 4.5 | ~10–20x cheaper; sufficient for structured I/O |
| Batch / async / non-urgent jobs | Haiku 4.5 + Batch API | 50% discount; no latency requirement |

**Rule:** Default Sonnet. Escalate to Opus only when task genuinely demands it. Downgrade to Haiku when output is structured and verifiable.

---

## Prompt Caching (API Surfaces)

- Enable automatic caching (`cache_control`) on every API request
- Static content first (system prompt, tool definitions, docs) — dynamic content last
- Never inject timestamps, session IDs, or per-user variables into the system prompt
- Monitor `cache_read_input_tokens` — zero after first call means caching is broken
- 5-min TTL default; 1-hour TTL only for large infrequently-reused docs
- Up to 4 explicit breakpoints available; use automatic mode first

**Expected impact:** 85–90% reduction on cached input tokens in multi-turn sessions.

---

## Context Engineering

- Load only state files and skills the current task requires — no speculative fetches
- Never send raw conversation history to the API — summarize or extract entities
- Mask irrelevant tool outputs before including in next prompt
- Keep system prompts / project instructions lean — every line is injected every turn
- Reasoning degrades past ~3,000 tokens regardless of context window size

---

## Output Discipline

- Set `max_tokens` explicitly on every API call
- Request structured JSON for data operations — prose only when it is the product
- Avoid extended thinking output unless the reasoning trace is the deliverable
- Optimal prompt length: 150–300 words. Longer = vaguer outputs (attention dilution)
- Output tokens cost 5x input — length discipline has the highest ROI of any optimization

---

## Per-Surface Checklist

**Interactive sessions:** Load skills/state on trigger only → honour exchange-limit rules → run session-close procedure → keep project instructions lean → Opus only when justified

**API surfaces:** Cache on every request → static system prompt → summarize history → JSON outputs → route by complexity → monitor cache hit rate

**Batch/async:** Haiku 4.5 default → Batch API discount → pre-summarize inputs before batching

---

## Metrics

| Metric | Target |
|--------|--------|
| Cache hit rate (API) | > 80% of input tokens from cache |
| Output tokens per call (data ops) | < 500 tokens |
| Session length | Below project exchange limit |
| System prompt size | < 50% of project limit |

---

## Amendments

Project-specific exceptions live in that project's `DECISIONS.md`. Global amendments go here via the standard PROMOTION_LOG.md workflow. Reference this file as `brainframe-public/docs/TOKEN_OPTIMIZATION.md`.
