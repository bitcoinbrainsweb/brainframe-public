---
name: security-hardening
description: Enforces security gates before Cursor implements anything touching auth, input handling, PII, external APIs, or data storage. MUST be loaded before writing any code that accepts user input, modifies auth logic, stores sensitive data, adds external integrations, or handles file uploads. Fires automatically when Cursor is about to touch a security boundary. Do NOT skip — security retrofitting is 10x harder than building it in.
---

# Security Hardening

## GATE: Stop Before Implementing

Before writing any code, check: does this change touch any of the following?

- User input (forms, API routes, query params, file uploads)
- Authentication or session logic
- Authorization / access control
- PII, payment data, or sensitive storage
- External API integrations or webhooks
- CORS, rate limiting, or security headers

If YES to any → work through the relevant sections below before writing a line.

---

## Mandatory (No Exceptions)

- Validate all external input at the system boundary — never deeper
- Parameterize all database queries — never concatenate user input into SQL/NoSQL
- Encode output to prevent XSS — use framework auto-escaping, never bypass it
- Hash passwords with bcrypt/scrypt/argon2 (salt rounds ≥ 12) — never store plaintext
- Use httpOnly + secure + sameSite cookies for sessions — never localStorage for auth tokens
- Set security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options)
- Run `npm audit` (or equivalent) before every release
- Never commit secrets — use environment variables, never hardcode

---

## Ask Dave First (Hard Stop)

Do not implement. Surface for approval:

- Adding or modifying any authentication flow
- Storing a new category of sensitive data (PII, payment info, health data)
- Adding a new external service integration
- Changing CORS configuration
- Adding file upload handlers
- Modifying rate limiting or throttling
- Granting new roles or elevated permissions

---

## Never Do

- Commit secrets, API keys, tokens, or passwords to version control
- Log passwords, tokens, or full card numbers
- Trust client-side validation as a security boundary
- Use `eval()` or `innerHTML` with user-provided data
- Expose stack traces or internal error details to users
- Disable security headers for convenience
- Use wildcard `*` in CORS without explicit approval

---

## Input Validation Pattern

Validate at the boundary using schema validation (Zod, Joi, Yup, Pydantic — whatever the project uses):

```
1. Receive input at route/handler
2. Parse against strict schema (type, length, format, enum)
3. Reject with 422 + structured error if invalid
4. Pass only validated, typed data to service layer
```

Never validate in the service layer alone — always at the entry point.

---

## Auth Checklist

- [ ] Passwords hashed (bcrypt/scrypt/argon2, rounds ≥ 12)
- [ ] Session tokens: httpOnly, secure, sameSite
- [ ] Login endpoint has rate limiting (max 10 attempts / 15 min)
- [ ] Password reset tokens expire
- [ ] Every protected endpoint checks both authentication AND authorization
- [ ] Users can only access their own resources (check ownership, not just auth)

---

## Secrets Management

```
.env.example    → committed (placeholder values only)
.env            → NOT committed
.env.local      → NOT committed
*.pem / *.key   → NOT committed
```

Pre-commit check:
```bash
git diff --cached | grep -iE "password|secret|api_key|token|private_key"
```

If any match → do not commit. Move to environment variable.

---

## npm Audit Triage

Not all findings require immediate action:

| Severity | Reachable in prod? | Action |
|---|---|---|
| Critical/High | Yes | Fix before shipping |
| Critical/High | No (dev-only) | Fix soon, not a blocker |
| Moderate | Yes | Fix next release cycle |
| Low | Any | Track, fix during dep updates |

When deferring: document reason + set review date.

---

## Rate Limiting (Apply to All Auth Endpoints)

General API: 100 req / 15 min
Auth endpoints: 10 req / 15 min
File uploads: 10 req / hour

---

## Pre-Ship Security Checklist

```
Input
- [ ] All user input validated at system boundary
- [ ] SQL/NoSQL queries parameterized
- [ ] HTML output encoded/escaped

Auth
- [ ] Passwords hashed (rounds ≥ 12)
- [ ] Session cookies: httpOnly, secure, sameSite
- [ ] Rate limiting on auth endpoints
- [ ] Password reset tokens expire

Authorization
- [ ] Every endpoint checks permissions
- [ ] Resource ownership verified (not just authentication)

Data
- [ ] No secrets in source or git history
- [ ] Sensitive fields excluded from API responses
- [ ] PII encrypted at rest (if applicable)

Infrastructure
- [ ] Security headers set (CSP, HSTS, X-Frame-Options)
- [ ] CORS restricted to known origins
- [ ] npm audit: no critical/high in prod deps
- [ ] Error messages don't expose internals
```

---

## Red Flags — Stop and Flag These

- User input passed directly to DB queries, shell commands, or HTML rendering
- Secrets visible in source code or git diff
- API endpoint with no auth or ownership check
- Missing CORS config or wildcard origin
- No rate limiting on login/signup
- Stack traces exposed in error responses
- Dependencies with known critical vulnerabilities
