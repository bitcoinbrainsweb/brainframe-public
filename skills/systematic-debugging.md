---
name: systematic-debugging
description: "Use when diagnosing any bug, unexpected behaviour, test failure, or production incident. Triggers on: error messages, stack traces, 'it\'s not working', 'something broke', or any report of unexpected system behaviour. Enforces root-cause-first diagnosis — never apply a fix before identifying the root cause."
---

# Systematic Debugging
Version: 2.0

READ → CONFIRM → FIX. No exceptions. No guessing.

<BREVITY>
Debug output is strict. No walk-throughs, no narration, no hypotheses shared mid-investigation.
Only output when you have confirmed root cause. Then use the output format below.
</BREVITY>

<HARD-GATE>
Do NOT suggest a fix until root cause is confirmed from code you have read.
</HARD-GATE>

## Process

1. **READ** — fetch and read every file relevant to the symptom before forming a hypothesis
2. **CONFIRM** — state the root cause in one sentence with the exact file + line
3. **FIX** — propose the minimal fix that addresses root cause only

## Output Format

```
ROOT CAUSE: [one sentence — file, line, what it does wrong]
FIX: [what to change]
RISK: [what else this touches]
```

## Rules

- Never guess. If the relevant code is not in context, fetch it.
- Never fix a symptom without confirming root cause.
- Never fix multiple things at once unless they share the same root cause.
- If root cause cannot be confirmed from available code, say so and list what else needs to be read.
- One fix per response. If multiple issues exist, rank by severity and address in order.
