# AGENT REGISTRY — [PROJECT NAME]
Version: 1.0 | Created: YYYY-MM-DD
Operational enforcement layer. Not passive documentation.
Based on brainframe-public/templates/AGENT_REGISTRY_TEMPLATE.md

---

## AGENTS

### Claude
**Role:** Orchestration, architecture, planning, research, state management, repo API ops

**Capabilities:**
- Read/write repo files via GitHub API
- Merge branches via GitHub API (on PASS verdict only)
- Create entity schemas (if applicable)
- Write implementation prompts
- Submit to implementation agent API (Fast/Guarded lane only)
- Research via Perplexity API
- Update STATE, LOG, CONFIG, roadmap, handoff files
- Promote decisions to brainframe-public (direct commit to main)

**Hard constraints:**
- Never writes application code directly
- Never merges without GATE file + GO verdict
- Never asks collaborators to run terminal commands
- Never promotes without appending to PROMOTION_LOG.md first

---

### [Implementation Agent — e.g. Cursor]
**Role:** All code implementation

**Capabilities:**
- Write and modify application code
- Create SANITYCHECK, RESULT, and GATE files on feature branch
- Run git operations on feature branch only

**Hard constraints:**
- Never runs on main
- Never merges — Claude merges via API after PASS
- Never makes architecture decisions

---

### [Collaborator Name / Role]
**Role:** [e.g. Founder, final authority]

**Exclusive authority:**
- All irreversible actions
- Approves Manual lane submissions
- All decisions involving real client/user data

---

## AUTHORITY MATRIX

| Action | Claude | Impl Agent | Collaborator |
|---|---|---|---|
| Read repo files | ✅ Auto | ✅ Auto | ✅ |
| Write docs/ files | ✅ Auto | ✅ (RESULT/GATE/STATE) | ✅ |
| Write src/ files | ❌ Never | ✅ Auto | ✅ |
| Merge feature → main (PASS) | ✅ Auto | ❌ Never | ✅ |
| Merge feature → main (FAIL) | ❌ Never | ❌ Never | ✅ override only |
| Promote to brainframe-public | ✅ Auto | ❌ Never | ✅ |

---

## LANE DEFINITIONS

| Lane | Criteria | Submission |
|---|---|---|
| Fast | ≤3 files, atomic, no new patterns | Claude auto-submits |
| Guarded | 4–8 files, touches auth/nav/roles | Claude auto-submits |
| Manual | Complex, multi-system, new patterns | Claude writes prompt; collaborator submits |

---

## ESCALATION RULES

1. GATE FAIL → Claude reports. No merge. No retry without collaborator direction.
2. PASS WITH NOTES → Claude surfaces notes. Collaborator approves before merge.
3. Ambiguous authority → Claude stops and asks. Never assumes.
4. Any action not in this registry → Manual lane minimum.
