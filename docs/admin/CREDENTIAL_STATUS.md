# CREDENTIAL_STATUS.md
Last Updated: 2026-04-08
Source of truth: brainframe-comms/_admin/PAT_REGISTRY.md

## Credential Registry

| Credential | Location | Status | Notes |
|-----------|----------|--------|-------|
| GitHub PAT (main) | brainframe-comms/_admin/PAT_REGISTRY.md | ACTIVE | Write access all repos |
| GitHub Comms PAT | brainframe-comms/_admin/PAT_REGISTRY.md | ACTIVE | brainframe-comms only |
| Claude API Key | GitHub Secret: CLAUDE_API_KEY (brainframe-public) | ACTIVE | Weekly review workflow |
| OpenAI API Key | brainframe-comms/_docs/REGISTRY.md | ACTIVE | GPT-4o critique |
| Perplexity API Key | brainframe-comms/_docs/REGISTRY.md | DEAD | Quota exhausted -- top up |
| Odds API Key (Mambamode) | brainframe-comms/_admin/PAT_REGISTRY.md | ACTIVE | b6371e... |

## Rules
- Never store credentials in repo files (GitHub secret scanning blocks commits)
- Always fetch from PAT_REGISTRY.md before any API call -- never use cached values from memory
- Dead keys: do not use, update Status here when refreshed
