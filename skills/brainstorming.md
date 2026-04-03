---
name: brainstorming
description: "Use before any feature design, architectural decision, or new capability. Explores intent, requirements, and design approaches through Socratic dialogue before any implementation begins. Triggers on: \'how should we build\', \'what\'s the best approach\', \'design for\', \'thinking about adding\', \'explore options for\', or any ambiguous build request."
---

# Brainstorming
Version: 1.0

Turn ideas into fully formed designs through collaborative dialogue before any implementation begins.

<HARD-GATE>
Do NOT write any code, produce any implementation prompt, or take any implementation action until you have presented a design and the user has approved it.
</HARD-GATE>

## Process

1. **Understand context** — check relevant files, state, recent decisions
2. **Clarify intent** — ask one question at a time until intent is unambiguous
3. **Explore constraints** — surface technical, product, and user constraints
4. **Present design options** — two or three approaches with tradeoffs
5. **Recommend** — state which option you recommend and why
6. **Get approval** — explicit approval before any implementation action

## Rules

- Ask one question at a time. Never a list of questions.
- If the answer can be found in existing context, find it instead of asking.
- Design before code. Always.
- State tradeoffs honestly. Never oversell an approach.
