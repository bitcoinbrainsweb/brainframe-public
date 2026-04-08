# Nightwatch Code Review Rules
*Project-specific reference for code-review-excellence skill.*
*Loaded on demand when reviewing Nightwatch code.*

## Nightwatch-Specific Rules

These apply to all Nightwatch code reviews and override general rules where they conflict.

### Role Checks
- Role checks via `src/lib/roleUtils.js` ONLY — never raw array checks or string comparisons
- Flag any `user.role === 'admin'` or `roles.includes(...)` pattern — must be roleUtils helper
- Verify roleUtils is imported, not reimplemented

### Terminology
- Amanda's work = Effectiveness Review — never "audit"
- Client-facing = MSB/VASP portal — not "admin panel"

### Schema Alignment
- All entity access via Base44 SDK — no raw API calls
- Enum values must match `base44/entities/*.json` exactly
- No hardcoded string literals where enums exist

### Graph Integrity
- Every new entity must have a graph node mapping
- FK relationships must be explicit, never inferred
- No orphaned entities (entities with no graph parent)
