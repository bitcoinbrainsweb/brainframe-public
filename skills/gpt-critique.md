---
name: gpt-critique
description: "RETIRED — use critique-spec skill instead. This skill has been superseded by the critique-spec pipeline which runs GPT-4o + Perplexity sonar-pro sequentially via API. Do not use for new work."
---

# GPT Critique Skill
Version: 1.0 — RETIRED 2026-04-08

**This skill is retired. Use the `critique-spec` skill for all spec critique work.**

The critique-spec skill:
- Fetches specs directly from brainframe-comms via GitHub API
- Runs GPT-4o critique via API (key in brainframe-comms/_docs/REGISTRY.md)
- Runs Perplexity sonar-pro critique via API (key in REGISTRY.md)
- Synthesizes findings and saves critique to brainframe-comms/specs/{project}/critiques/
- No manual copy-paste required

Trigger: `critique spec`

This file is kept for historical reference only.
