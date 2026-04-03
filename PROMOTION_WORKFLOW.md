# PROMOTION WORKFLOW
Version: 2.0 | Updated: 2026-04-03 (INFRA-13)
How project-specific decisions get promoted to brainframe-public (global layer).
Claude commits directly to main — no PR, no Dave touch required.

---

## WHAT GETS PROMOTED

Global promotion is for rules, patterns, and decisions that apply to ALL projects — not Nightwatch-specific content.

**Promote:**
- New entries to GLOBAL_RULES.md or STYLE_RULES.md
- New INFRA_PATTERNS.md entries
- New COLLAB_RULES.md entries
- New global skills (skills/global-*.md)
- MODEL_ROUTING.md updates
- ANTI_PATTERNS.md updates

**Never promote:**
- Project-specific state (NIGHTWATCH_STATE.md, etc.)
- PAT values or secrets
- Client data or engagement content
- App IDs or environment config

---

## CLAUDE'S STEPS (at session close or on Dave's instruction)

1. Identify candidates from the session — decisions or rules that should apply globally
2. Fetch current SHA for each target file in brainframe-public
3. Commit directly to main in brainframe-public via GitHub API
4. Report what was promoted

Sync to all four repos fires automatically within 24h, or trigger workflow_dispatch manually.

---

## GITHUB API STEPS

### Read file SHA
```
GET /repos/bitcoinbrainsweb/brainframe-public/contents/[file]
→ sha
```

### Write to main
```
PUT /repos/bitcoinbrainsweb/brainframe-public/contents/[file]
{
  "message": "promote: [description]",
  "content": "[base64]",
  "sha": "[current file SHA]"   ← omit if new file
}
```

---

## SYNC TIMING

- Automatic: daily 6am UTC via brainframe-sync.yml in nightwatch repo
- Manual: trigger workflow_dispatch from Actions tab in nightwatch repo

---

## RELATED DOCS
- `docs/AGENT_REGISTRY.md` — authority matrix
- `.github/workflows/brainframe-sync.yml` (nightwatch repo) — sync engine