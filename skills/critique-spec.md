---
name: critique-spec
description: >-
  Runs a multi-AI spec critique pipeline: fetches a spec from brainframe-comms, fires it sequentially through GPT-4o and Perplexity sonar-pro via API, synthesizes findings, and surfaces disagreements for Dave to resolve. MUST be used when Dave says "critique spec". Replaces gpt-critique-skill and perplexity critique prompts for all spec critique workflows. Do NOT use for general research — use perplexity-pro-research-prompt-skill instead.
---

# Critique Spec Skill
*Multi-AI spec critique pipeline — GPT-4o + Perplexity sonar-pro*
*Fully automated — no manual paste required*
Version: 2.0 | 2026-04-10

---

## What This Skill Does

Fetches a spec from `brainframe-comms/specs/`, calls GPT-4o and Perplexity sonar-pro APIs sequentially via bash, synthesizes both critiques, and presents:
- A brief summary of material findings per model
- Agreements (applied or flagged)
- Disagreements surfaced as `[DECIDE]` items for Dave to resolve one at a time

No manual paste required. Dave never touches GPT or Perplexity interfaces for this workflow.

---

## Credentials — always fetch fresh from REGISTRY.md

Before any API call, fetch credentials:

```bash
# PAT is sourced from project instructions CREDENTIALS section — never hardcoded here
REGISTRY=$(curl -s -H "Authorization: token $PAT" \
  "https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-comms/main/_docs/REGISTRY.md")

OPENAI_KEY=$(echo "$REGISTRY" | grep -A1 "## OpenAI" | grep "^Key:" | awk '{print $2}')
PERPLEXITY_KEY=$(echo "$REGISTRY" | grep -A1 "## Perplexity" | grep "^Key:" | awk '{print $2}')
```

Never hardcode keys. Always parse from REGISTRY.md at runtime.

---

## Pipeline

### Step 1 — Identify spec

**When triggered by spec-writing skill (auto-critique):**
The spec filename and raw URL are passed in context. Skip straight to Step 2.

**When triggered manually by Dave ("critique spec"):**
Fetch the file list from `brainframe-comms/specs/` via GitHub API:

```bash
curl -s -H "Authorization: token $PAT" \
  "https://api.github.com/repos/bitcoinbrainsweb/brainframe-comms/contents/specs"
```

Present the list. Ask: **"Which spec?"** Wait for Dave to name it. Do not proceed until confirmed.

Once spec is identified, build the raw URL:
```
SPEC_RAW_URL="https://raw.githubusercontent.com/bitcoinbrainsweb/brainframe-comms/main/specs/{project}/{filename}"
```

Fetch spec content for injection into prompts:
```bash
SPEC_CONTENT=$(curl -s -H "Authorization: token $PAT" "$SPEC_RAW_URL")
```

---

### Step 2 — Call GPT-4o API

Build the critique prompt by injecting spec content directly (GitHub raw URLs are private — GPT cannot fetch them):

```bash
GPT_PROMPT="# {PROJECT} — Spec Critique: {SPEC_FILENAME}

Read the following spec in full before responding:

---
${SPEC_CONTENT}
---

This is a spec critique. Your output will be passed to Claude to update the spec.
Flag anything that will cause real problems in production, at scale, or across sessions.
Ignore cosmetic issues. Do not rewrite or redesign spec sections.
This is a critique only. Do not write Cursor prompts, implementation plans, or replacement designs.

## Scope boundary
Flag anything outside the current spec scope in the Out of Scope section.
Name it only — do not design it, solve it, or expand it.
If context is unavailable on any point, do not infer it. Critique only what is explicitly stated.

## What I need from you

### 1. Brief version (10 bullets max)
Biggest risks, gaps, and missed opportunities only.
Direct verdicts. No hedging. No option lists without a winner.

### 2. Full critique

Use the exact section headings below in the exact order. Do not add extra main sections.

#### Risks
One section per risk category. For each risk:
- What breaks
- Why it breaks
- Recommendation (opinionated verdict — no option lists without a winner)
- Confidence: HIGH / MEDIUM / LOW

#### Findings
Format every finding as a single atomic item:
- [ACCEPT / REJECT / DECIDE] — statement
- Why it matters
- Recommendation
- Confidence: HIGH / MEDIUM / LOW

ACCEPT = design is sound
REJECT = replace with recommendation
DECIDE = Dave must make a call (state the exact decision with a recommended default)

Every finding must have a tag. No untagged findings.

#### Feature Recommendations
Features or improvements not in the current spec that would materially improve the system.
One atomic item per recommendation:
- Feature name
- What problem it solves
- Why it belongs in this spec (not later)
- Confidence: HIGH / MEDIUM / LOW

#### Open Questions Flagged
Any existing OQ-XXX entries in the spec that you consider blockers.
New open questions you are surfacing that should be added to the spec.
Format: OQ-NEW-001: [question] — [why it blocks]

#### Out of Scope
Things that came up but belong in a later build. One line each. No implementation details.

Be opinionated. Pick a winner on every recommendation.
Every finding must carry [ACCEPT/REJECT/DECIDE] and Confidence: HIGH/MEDIUM/LOW. No exceptions."
```

Call the API:

```bash
GPT_RESPONSE=$(curl -s https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_KEY" \
  -d "$(python3 -c "
import json, sys
prompt = open('/tmp/gpt_prompt.txt').read()
payload = {
  'model': 'gpt-4o',
  'max_tokens': 4000,
  'messages': [{'role': 'user', 'content': prompt}]
}
print(json.dumps(payload))
")")

GPT_TEXT=$(echo "$GPT_RESPONSE" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d['choices'][0]['message']['content'])
")
```

Save to temp file:
```bash
echo "$GPT_TEXT" > /tmp/gpt_critique_output.md
```

If API returns an error (non-200, missing `choices`): surface error to Dave, stop. Do not proceed to Perplexity.

---

### Step 3 — Call Perplexity sonar-pro API

```bash
PERP_PROMPT="# {PROJECT} — Spec Critique: {SPEC_FILENAME}

Read the following spec in full before responding:

---
${SPEC_CONTENT}
---

This is a spec critique. Flag real problems — gaps, contradictions, missing failure modes, unclear contracts, and industry patterns this spec ignores. Do not rewrite or redesign sections.
Critique only what is explicitly stated. Do not infer missing context.

Output the following sections in order. Stay within each section — do not merge them.

## Risks (3 max)
For each risk: what breaks, why it breaks, recommended fix, Confidence: HIGH/MEDIUM/LOW.

## Findings (5 max)
Each finding: [ACCEPT / REJECT / DECIDE] — statement. Why it matters. Recommendation. Confidence: HIGH/MEDIUM/LOW.
Every finding must have a tag. No untagged findings.

## Industry Pattern Gaps
What does current industry practice do for this problem that this spec does not address?
One finding per gap. Source each claim with a URL.

## Open Questions Flagged
Existing OQ-XXX entries you consider blockers, plus any new open questions to add.
Format: OQ-NEW-001: [question] — [why it blocks]

## Out of Scope
One line each. Name only — no design.

Raw findings only. No synthesis. No preamble. Source every industry claim with a URL."
```

Call the API:

```bash
PERP_RESPONSE=$(curl -s https://api.perplexity.ai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $PERPLEXITY_KEY" \
  -d "$(python3 -c "
import json
prompt = open('/tmp/perp_prompt.txt').read()
payload = {
  'model': 'sonar-pro',
  'max_tokens': 2000,
  'messages': [{'role': 'user', 'content': prompt}]
}
print(json.dumps(payload))
")")

PERP_TEXT=$(echo "$PERP_RESPONSE" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d['choices'][0]['message']['content'])
")
```

Save to temp file:
```bash
echo "$PERP_TEXT" > /tmp/perp_critique_output.md
```

If Perplexity key is exhausted (HTTP 429 / quota error): surface to Dave. Use GPT output alone for synthesis, label synthesis as `GPT-only — Perplexity quota exhausted`.

---

### Step 4 — Save raw outputs to brainframe-comms

Save both raw outputs as critique artifacts before synthesis:

Paths:
- `brainframe-comms/specs/{project}/critiques/{spec-slug}-gpt-YYYY-MM-DD.md`
- `brainframe-comms/specs/{project}/critiques/{spec-slug}-perplexity-YYYY-MM-DD.md`

Write via GitHub API (PUT). Fetch SHA first if file already exists.

---

### Step 5 — Synthesize

Read both outputs from `/tmp/gpt_critique_output.md` and `/tmp/perp_critique_output.md`.

Produce synthesis report:

```
## Critique Synthesis — {SPEC_FILENAME}
Run: {YYYY-MM-DD} | GPT-4o ✅ | Perplexity sonar-pro ✅

### GPT-4o Findings
- [ACCEPT/REJECT/DECIDE] Finding — Confidence: HIGH/MEDIUM/LOW
- ...

### Perplexity Findings
- [ACCEPT/REJECT/DECIDE] Finding — Confidence: HIGH/MEDIUM/LOW
- ...

### Agreements
- Finding both models share — note if action required

### Disagreements [DECIDE — resolving one at a time]
- **Topic**: GPT says X / Perplexity says Y
  → Awaiting Dave's call
```

Pause on every `[DECIDE]` item. Present one at a time. Wait for Dave's call before moving to the next.

After all `[DECIDE]` items resolved: output one clean block of accepted/rejected/decided outcomes.

---

## Rules

1. Always confirm spec before calling APIs — never assume most recent
2. Inject spec content directly into prompts — never rely on models to fetch private GitHub URLs
3. All findings must carry `[ACCEPT / REJECT / DECIDE]` + `Confidence: HIGH / MEDIUM / LOW`
4. No bullet count cap on synthesis — include every material finding; cut only noise
5. Disagreements resolved one at a time, in order — never batch
6. Do not apply changes to spec during this session — synthesis feeds next spec revision separately
7. Save raw outputs to brainframe-comms before surfacing synthesis
8. Credentials always from REGISTRY.md — never hardcoded

---

## Failure Modes

| Symptom | Fix |
|---|---|
| OpenAI API error / 401 | Re-fetch key from REGISTRY.md — key may have rotated |
| Perplexity 429 quota exhausted | Surface to Dave. Proceed with GPT-only synthesis, label it clearly |
| GPT returns prose without tags | Re-call with system message: "Every finding must carry [ACCEPT/REJECT/DECIDE] and Confidence: HIGH/MEDIUM/LOW. No untagged findings." |
| GPT hedges without verdicts | Re-call with: "No option lists without a winner. Pick one." |
| Perplexity truncates output | Expected — prompt is scoped to 5 sections with count caps. If still truncated, surface to Dave |
| Spec content too large for prompt | Chunk spec into sections, run critique per section, merge findings before synthesis |
