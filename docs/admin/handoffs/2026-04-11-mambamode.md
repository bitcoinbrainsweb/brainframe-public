# Session Handoff — Mambamode — 2026-04-11

## Summary
Built and installed the `nba-data-scientist` skill v3 — a world-class analytical methodology skill that encodes elite quant practices (Gelman Bayesian workflow, walk-forward CV, SHAP, ensemble stacking, CLV benchmarking, DAG-based tautology detection, simulation-based power analysis). Ran Perplexity Deep Research on NBA data science methods, then two rounds of GPT-4o + Perplexity API critique. Drafted NE-035 Analytical Engine spec covering four tracks: composite pregame modeling, live signal expansion, event-level EPV (LSTM on PBP data), and production monitoring with CUSUM halt rules.

## Decisions Made
1. **Skill scope:** Data scientist skill is behavioral guardrails only (how to think), not project-specific data or architecture. Rejected: embedding Dave's lessons, embedding feature catalogs, embedding signal state.
2. **Deep learning excluded from v1:** XGBoost vs neural nets is 77.49% vs 77.26% on NBA data — marginal gain for significant complexity. Path 4 placeholder added for when PBP data is available. Rejected: including deep learning in v1.
3. **Critique decisions (all accepted):** Gap-window holdout (not just 2-season), RFE mandatory before composite builds, Brier score mandatory, simulation-based power analysis, hierarchical models as recommended default.
4. **NE-035 spec architecture:** Four tracks (composite pregame, live expansion, event-level EPV, monitoring). Rejected: single monolithic approach.

## Last Completed Action
NE-035 spec draft delivered to Dave via present_files.

## Open Items
- NE-035 spec needs saving to brainframe-comms + mirror to mamba-mode repo
- NE-035 spec critique not yet run (DRAFT status, pending)
- Signal challenge results (TOT-003 killed, LIV-002 killed) need propagation to METHODOLOGY.md and BACKTEST_FINDINGS.md
- build-log and MAMBA_STATE need updating (doing now)

## First Action Next Session
Resolve OQ-009 (current season data gap) — this blocks Track A. Then save NE-035 spec to repos and run critique.
