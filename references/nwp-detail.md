# Nightwatch Prompts — Detail Reference
*Fetched by nightwatch-prompts skill on demand.*
*Contains Base44 setup, verification, help config, regression scan, data classification, deployment tracking, role checks, copy block rules.*

## BASE44 SETUP BEFORE CURSOR — CLAUDE DOES THIS

Before writing any Cursor prompt that adds or modifies entities:

1. Claude creates the entity via MCP: `Base44:create_entity_schema` or `Base44:edit_base44_app`
2. Claude verifies via MCP: `Base44:list_entity_schemas` — confirm entity is live
3. Only then write the Cursor prompt — Cursor writes the entity JSON for repo sync only

Never write a Cursor prompt that assumes an entity exists before step 2 is confirmed.

## VERIFICATION — AUTO-FETCH, NEVER ASK DAVE

After any upgrade lands:
1. Fetch `docs/NW-UPGRADE-XXX-RESULT.md` from GitHub — confirm it exists and shows PASS
2. Fetch `docs/NIGHTWATCH_STATE.md` — confirm it reflects the merged state
3. If RESULT missing or shows FAIL → do not proceed, report to Dave
4. If STATE stale → update it before next upgrade

## HELP CONFIG — REQUIRED ON EVERY NEW PAGE

Every new page/route added to Nightwatch must include:
```javascript
// At the top of the page component
import { useHelp } from '@/contexts/HelpContext';

const { setHelpContent } = useHelp();

useEffect(() => {
  setHelpContent({
    title: '[Page Title]',
    description: '[One sentence describing what this page is for]',
    steps: ['Step 1', 'Step 2', 'Step 3'],
  });
}, [setHelpContent]);
```

Include this in every Cursor prompt that adds a new page. Never skip.

## POST-MERGE REGRESSION SCAN

After every merge, run:
1. Fetch the diff of the merged branch from GitHub API
2. Check for: roleUtils bypassed, entity access without function gate, console.log with PII, hardcoded credentials
3. If any found → create a follow-up upgrade spec immediately, do not defer

## DATA CLASSIFICATION IMPACT — MANDATORY IN EVERY SPEC

Every upgrade spec must include a one-line data classification assessment:

```
DATA CLASSIFICATION: [No PII | PII in transit | PII at rest | Client data | Audit trail]
RESIDENCY IMPACT: [None | Affects Canadian data residency | Requires DATA_POLICY review]
```

If PII at rest or client data: reference DATA_POLICY.md and load data-policy-enforcer skill before writing spec.

## BASE44 ENTITY WORKFLOW

Entity creation order — non-negotiable:
1. Claude designs the entity (base44-entity-design skill)
2. Claude creates via MCP (Base44:create_entity_schema)
3. Claude verifies via MCP (Base44:list_entity_schemas)
4. Cursor writes entity JSON to base44/entities/EntityName.json (repo sync only)

Never skip steps 2–3. Never have Cursor create entities.

## DEPLOYMENT TRACKING

After every merge to main:
1. Update docs/NIGHTWATCH_STATE.md: set last_completed, clear active_branch, set next_upgrade
2. Check if Base44 auto-deployed (GitHub → Base44 sync is automatic on merge)
3. If auto-deploy fails: note in STATE.md, flag to Dave

## ROLE CHECKS — MANDATORY

Every Cursor prompt touching auth or display logic must include:
```
Role check requirement: all role checks via src/lib/roleUtils.js only.
Never use raw role string comparisons or array includes for role logic.
Flag any existing raw checks found in scope files.
```

## COPY BLOCK RULES

- One-click copy blocks: ONLY for text Dave will paste into Base44, Cursor, terminal, or another tool
- Never apply copy blocks to explanations, status updates, analysis, or reviews
- Cursor prompts: always in a copy block
- Merge commands: always in a copy block (PowerShell format, semicolons not &&)
- Everything else: plain chat
