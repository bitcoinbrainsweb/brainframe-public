# Nightwatch Proof of Work Config
*Project-specific reference for proof-of-work skill.*
*Loaded on demand when running proof-of-work on Nightwatch.*

## Default Data Sources
- Repo: `bitcoinbrainsweb/great-horn-aml-nightwatch`
- GitHub PAT: from project instructions
- Base44 MCP: entity count via `Base44:list_entity_schemas`
- App ID: `69afb09f3cf8f7f93f857eb1`
- Roadmap: `docs/Nightwatch_Roadmap_Detailed_v15.md`
- Start date: 2025-01-01 (approximate project start)

## Upgrade Count Section (Nightwatch only)
After the main report, add:

```
UPGRADE COUNT
Upgrades merged to main: [count NW-UPGRADE-XXX branches merged]
Current upgrade: [NW-UPGRADE-XXX]
Phase: [current phase name]
```

Count by fetching merged PRs with branch prefix `NW-UPGRADE-` from the GitHub API.
