---
schema: strategy-research-record-v1
title: "FaVOR: Hypothesis-Grounded Agentic Factor Mining with Distributional Factor-Validation Gates (CSI 500 / S&P 500 top-50 daily portfolios)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: low
source_as_of: 2026-08-31
sources:
  - "https://arxiv.org/abs/2608.30192 (arXiv:2608.30192v1 [cs.AI], submitted 31 Aug 2026)"
  - "https://arxiv.org/pdf/2608.30192v1 (pinned v1 PDF, 28 pages, SHA-256 d42b8bafa7b7c2a6662eb6a2c680bddf7b7363c1318a801384007458f2a9db62)"
  - "https://github.com/damilab/FaVOR tree at commit 98f692af9e60f1edd3ce8cae74bed7adf0a7ae5a"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FaVOR: Hypothesis-Grounded Agentic Factor Mining with Distributional Factor-Validation Gates (CSI 500 / S&P 500 top-50 daily portfolios)

## Provenance

**Primary source identity.** arXiv preprint `arXiv:2608.30192v1 [cs.AI]`, title *FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation*, landing page `https://arxiv.org/abs/2608.30192`, pinned PDF `https://arxiv.org/pdf/2608.30192v1`. arXiv submission history shows exactly one version: `[v1] Mon, 31 Aug 2026 03:16:06 UTC (2,674 KB)`. The Comments field, the Journal-reference field and the DOI field on the landing page are all empty; the arXiv DOI `https://doi.org/10.48550/arXiv.2608.30192` answers HTTP 302 → abs page → 200 (checked 2026-09-24) → **preprint only, no peer-reviewed venue, no v2 as of 2026-09-24** (`source_as_of: 2026-08-31` = v1 submission date).

**Author list (three-way match).** Exactly six authors, identical ordering in (a) the landing-page `Authors:` block, (b) the PDF title block (`Hyeonjin Kim1*, Minseok Kim1*, Seunghyeon Jung1*, Sujin Pyo2, Huisu Jang3, Woojin Lee1†`), and (c) the PDF `/Author` metadata (`Hyeonjin Kim; Minseok Kim; Seunghyeon Jung; Sujin Pyo; Huisu Jang; Woojin Lee`): **Hyeonjin Kim\*, Minseok Kim\*, Seunghyeon Jung\*, Sujin Pyo, Huisu Jang, Woojin Lee†** (\* equal contribution, † corresponding). Affiliations printed on page 1: 1 Department of Computer Science and Artificial Intelligence, Dongguk University-Seoul; 2 Department of Industrial Engineering, Seoul National University; 3 School of Finance, Soongsil University.

**Pinned PDF read-back (primary-source checksum, performed 2026-09-24).** 28 pages, 3,604,761 bytes, SHA-256 `d42b8bafa7b7c2a6662eb6a2c680bddf7b7363c1318a801384007458f2a9db62`; pypdf extraction yields 2,816 lines / 100,019 characters; §1–§5, the Limitations block, References and Appendices **A–Q** (operator library, validation criteria, metric definitions, hyperparameters, all prompt templates, run-to-run variance, trade statistics, regime context, hypothesis provenance, selectivity sensitivity, variance/baseline context, interpretability scope, computational cost, software/data) were read line by line. Every quantitative claim below carries its Table/Section anchor from this pinned v1 PDF.

**Code identity.** `https://github.com/damilab/FaVOR`, pinned at full commit SHA `98f692af9e60f1edd3ce8cae74bed7adf0a7ae5a` (commit message "Initial public FaVOR source release", committer date 2026-08-30T02:53:04Z). GitHub API read on 2026-09-24: repo created 2026-08-30T02:23:26Z, last push 2026-08-30T02:53:06Z, default branch `main`, 1 star, license `NOASSERTION` (see `LICENSE-DECISION.md`). The tree at the pinned SHA is **not a stub**: 132 entries including `README.md` (4,190 B), `configs/paper_2026.yaml`, `configs/runtime.env.example`, `docs/DATA_AND_REPRODUCIBILITY.md`, `docs/FRAMEWORK.md`, `docs/PROVENANCE.md`, `favor/agent/validation_agent.py` (47,478 B), `favor/agent/formula_agent.py` (39,166 B), `favor/agent/hypothesis_validation_agent.py` (40,048 B), `favor/coder/factor_coder/{function_lib.py,eva_utils.py,evolving_strategy.py,prompts.yaml}`, `favor/coder/CoSTEER/*`, and `.github/workflows/ci.yml`.

**Repository-wide dedup audit (2026-09-24).** `grep -rIl --include='*.md'` across the entire repository root — 2,484 `*.md` files including hidden directories (`.mimo-worktrees`, `.agents`, `.hermes`) and `coverage_manifest.csv` — for each of `2608\.30192`, `damilab`, `FaVOR`, `Agentic Framework for Factor Mining`, `Observable Reasoning`, `Factor Validation through` → **0 matching files for every pattern**. Case-insensitive `favor` hits are only the ordinary English word. `git log --oneline -20` inspected separately for convenience (latest `76ea556` Beyond Prompting agentic-factor record). Adjacent agentic/LLM factor-mining records in this repository are different source identities with different search machinery — `beyond-prompting-agentic-factor-investing-composite-long-short-2026-09-24.md` (arXiv 2603.14288, ReAct/CoT primitives → 12 hand-shaped CRSP factors), `alphacfg-…-2026-09-05` (grammar-guided MCTS), `alphaschema-…-2026-09-05` (plan-space surrogate evolution), `alphalogics-…-2026-09-05` (market-logic multi-agent), `agonalpha-…-2026-09-04` (adversarial review), `alphacrafter-…-2026-09-03`, `alphar1-…-2026-09-03` (GRPO screening), `factorengine-…-2026-09-05` (program synthesis), `factorminer-self-evolving-experience-memory-formulaic-alpha-2026-09-20`, `alphaforge-…-2026-09-17`, `vst-…-2026-09-12`, `aeap-seads-…-2026-09-03`, `goant-…-2026-09-12`, `agora-…`. None of them reports FaVOR's pre-backtest **distributional construct-validation gate** (Stage 2) or its CSI 500 / S&P 500 2025 numbers, and FaVOR cites none of them; the paper's own baseline set (AlphaForge, AlphaQCM, R&D-Agent-Quant, AlphaAgent) is disjoint from the repository's recorded sources. Materially distinct mechanism = independent record under the dedup contract.

## Economic mechanism

### Source-reported

The authors' thesis (§1, Figure 1, Figure 2) is a failure-mode claim: return-oriented LLM factor automation optimises a formula for realised returns without ever checking that the formula still measures the economic hypothesis that produced it, so "mathematical form" and "economic meaning" drift apart, which they argue makes such factors indistinguishable from spurious fits and prone to breaking under regime shifts (§1, citing Bailey et al. 2014, McLean–Pontiff 2016, Lopez de Prado–Zoonekynd 2025).

FaVOR restructures mining into a three-stage **consistency loop** that never uses future returns as a selection input before Stage 4:

- **Stage 1 — Hypothesis decomposition (§3.1).** A Hypothesis agent `A_H` turns a human market insight into a 1–3 sentence causal, daily-OHLCV-observable behavioural hypothesis plus an integer `horizon_days ∈ {1..10}`; an Observation agent `A_O` splits it into `m` distinct observable market conditions `{o_i}`; a Factor agent `A_F` emits `n_i = 2–3` candidate formulas per condition drawn only from the fixed operator library (Appendix A, Table 5).
- **Stage 2 — Factor-level validation (§3.2, Appendix B).** For each candidate the pipeline cross-sectionally sorts stocks within each date into `l = 5` quantile bins and builds a statistical profile `S_{i,j}` from four OHLCV state variables — intraday return `DIR = C−O`, range `MAG = H−L`, close position `POS = (C−L)/(H−L)`, volume `VOL = V` — recording mean, median, q10, q90, kurtosis, dispersion per bin. A Validation agent (temperature 0.1) must return PASS only if **all four** criteria hold: (i) central-tendency shift — mean and median of the same state variable move with the same sign across adjacent bins *and* the bin index has non-zero correlation with the bin means; (ii) non-trivial tail behaviour — some pair of bins differs in tail spread `q0.9 − q0.1` by more than a tolerance `ϵ`; (iii) statistical consistency — the same state variable is supported by at least one admissible pair from {mean+median, median+q10, median+q90, q90+kurtosis} (mean+q90 explicitly rejected); (iv) semantic consistency — the induced distributional pattern agrees with the wording of `o_i`. The paper stresses the LLM only maps observation text to state variables and directions; the verdict is the deterministic conjunction of the four checks (§3.2.2). Crucially, Stage 2 uses market variables observed at time `t`, **never** returns at `t+T` (§3.2).
- **Stage 3 — Factor integration / Directional Selectivity (§3.3).** Candidate combinations are the Cartesian product of the validated factors across conditions. A combination "triggers" only when **every** constituent factor crosses its in-sample `σ`-quantile in the condition's polarity simultaneously. The authors then ladder `σ₁ < σ₂ < …` and keep only combinations whose per-ticker support rate (average realised return *or* win rate rising as `σ` tightens) exceeds a fixed pass-rate threshold (0.5, strict variant 0.7), with the combination-level pass-rate to Stage 4 at 0.5 and a Directional Selectivity threshold of 0.8 (Table 7).
- **Stage 4 — Optimisation and backtest (§3.4).** Factor-specific cutoffs are optimised per retained combination with Optuna (20 trials, search range `σ ∈ [0.55, 0.95]`, combined-signal quantile `q = 0.9`, objective `Calmar = AR/|MDD|`) on the validation year, then frozen for the test year. An outer-loop hypothesis memory (3 iterations) stores prior hypothesis IDs, observation descriptions, formula names and "a single scalar summary of average information ratio"; it explicitly does not store raw returns, formula definitions or fitted thresholds.

Reported economic reading of the winning signals (§4.2, Figure 4, Appendix H): on the CSI 500 the pipeline "captures an early-year gain and preserves it" through a consolidation-then-rally 2025; on the S&P 500 it "remains near zero through early months and compounds steadily from mid-year" through a drawdown-to-recovery 2025. The paper explicitly disclaims any causal or fundamental economic mechanism for the validation decisions (Appendix J and Appendix O: interpretability is "empirical consistency between a formula and the OHLCV observable condition that motivated it").

### Research interpretation

Hypothesised mechanism in falsifiable form: **a construct-validity gate that filters formulas by their induced cross-sectional market-state statistics (rather than by realised forward returns) reduces the multiple-testing/data-mining component of automated factor discovery, so the surviving combination retains excess return out of sample where return-optimised generation decays.** Component roles:

- Regime / context: none inside FaVOR (no trend filter, no volatility regime gate; regime labels in Appendix H are post-hoc only and "not used by FaVOR during selection or trading").
- Primary signal: conjunction of validated OHLCV formula quantile triggers (Table 12 combination).
- Selection layer (the actual research claim): Stage 2 distributional gate + Stage 3 directional-selectivity gate.
- Risk / execution: Qlib `TopkDropout (k=50, n=5)` holding rule, holding horizon `T = 7`, stop-loss disabled — **risk management, not alpha** (repository rule 8).

Two caveats I mark rather than resolve. First, the mechanism story of the *final* disclosed signals is not narrated anywhere in the source: the CSI 500 portfolio ranks on a 7d/60d volume ratio, a 30-day close z-score, `Z20(min10 low) − Z20(max10 high)` and `Δvol10`, while the S&P 500 portfolio ranks on two range/std proxies plus a `min20 close / max15 close` ratio with **mixed polarity** (Table 12, which the authors say is "included only to identify the selected signals") — no economic rationale is given for these particular constructs → `underspecified`. Second, whether Stage 2's gate adds return rather than merely consistency is *denied by the source's own table*: PASS formulas show no standalone RankIC advantage over FAIL formulas in 7 of 8 market×horizon rows (Table 14), which the authors present as evidence that Stage 2 "is not a standalone alpha, IC, or RankIC filter" (Appendix I). I therefore treat the claim at the **pipeline level** only, not at the individual-factor level.

## Signal

**Formation timestamp.** One record per ticker per trading day from daily OHLCV; cross-sectional ranking is performed within each date on training data for validation/integration and with frozen thresholds for the test period (§3.2, §4.1). Timezone, session/candle-boundary convention and point-in-time publication lag → **not stated in source** (`data gap`); for the S&P 500 the Yahoo Finance daily bar convention is whatever `yfinance` returns (Appendix Q) → `data gap`.

**Lookback.** Formula windows are literal integer constants inside the released operator expressions (e.g. `SMA(vol,7)/SMA(vol,60)`, `MA30/STD30(close)`, `Z20(...)`, `STD15(close)`; Table 12); Stage-2 binning uses the full training panel (2022-01-01 → 2023-12-31); Stage-4 thresholds use the validation panel (2024-01-01 → 2024-12-31). Warm-up handling for the first `n` bars → `not stated in source`.

**Long / short entry.** Source-reported execution rule is Qlib `TopkDropout (k=50, n=5)` with `stop-loss: Disabled` (Table 9), i.e. a top-50 holding rule that drops 5 names per rebalance from the factor ranking; the paper never states a short leg, borrow, or margin requirement, and reports only *excess* returns versus the CSI 500 / S&P 500 benchmark indexes (Appendix C). The long/short stance, weighting scheme (equal-weight vs score-weight) and whether cash is held when no signal fires are **not stated in source** → `data gap`; interpreting `TopkDropout` as the standard long-only top-k Qlib rule is a `research interpretation`, not a source statement.

**Trigger.** `Signal(f, σ) = 1` iff every constituent factor of combination `f` simultaneously crosses its in-sample `σ`-quantile in the direction implied by its condition (§3.3.2); combined-signal quantile `q = 0.9` (Table 8); per-factor `σ` values are Optuna-selected per combination in `[0.55, 0.95]` on 2024 and are **not disclosed** for the two reported portfolios → `underspecified` (the pipeline is not reconstructable from the paper without the released code plus the undisclosed thresholds).

**Exit / holding period.** Holding horizon `T = 7` trading days, chosen by the LLM from `{1..10}` (Table 8 caption), plus unspecified "stop conditions" mentioned in §4.1 while the shared environment disables stop-loss (Table 9) → internally inconsistent with the reported **average holding period of 9.64 days** (Table 11 and the Limitations "Cost Model" paragraph) → `underspecified` exit precedence.

**Position sizing / rebalance cadence.** `TopkDropout (k=50, n=5)` implies daily top-50 with 5-name turnover per decision; actual weights, cash treatment, participation caps and position limits → `not stated in source`.

**Parameters actually published (Table 6–9).** Agent temperatures: hypothesis 0.9, observation 0.7, formula 0.7, validation 0.1. Stages 1–3: 2–3 candidate formulas per condition, 5 quantile bins, minimum 3 valid bins to retain a factor, maximum 5 refinement iterations, strictness levels q50/q70/q90, Directional Selectivity threshold 0.8, cross-ticker PASS 0.5 (strict 0.7), combination pass-rate to Stage 4 0.5. Stage 4: `σ` search `[0.55, 0.95]`, combined-signal quantile 0.9, `T = 7`, objective Calmar, 20 Optuna trials, entry "raw signal entry", 3 outer-loop iterations, 4 Stage-4 combo workers, 1 Optuna job per combo. Backbone for all main-table results: **GPT-4o**. Data splits 2022–2023 / 2024 / 2025; CSI 500 buy/sell fee 0.0005 / 0.0015; S&P 500 buy/sell fee 0 / 0.0005; execution `TopkDropout (k=50, n=5)`; stop-loss disabled.

**Reconstructability verdict.** Signal is **partially specified**: the architecture, operator library, gates, splits, costs and the two final formula sets are disclosed; the selected per-factor thresholds, the ticker-level cutoffs, the weights, the seed `concept_text`/knowledge inputs and the exact OOS combination-selection trace are not → `underspecified`, reconstructable only from the pinned code.

## Required data

- **Instrument / universe:** CSI 500 index constituents (Chinese A-shares, Baostock) and S&P 500 index constituents (US, Yahoo Finance via `yfinance`) (§4.1, Appendix Q). No other market, no futures/perpetual/options, no crypto.
- **Venue / data vendor:** Baostock (BSD-licensed package) and Yahoo Finance (`yfinance`, Apache-2.0 package; underlying Yahoo data under Yahoo's terms, used non-commercially, raw data not redistributed — Appendix Q).
- **Timeframe / fields:** daily bars, exactly `$open, $high, $low, $close, $volume` for the FaVOR pipeline (§4.1); ML/DL baselines additionally receive the Alpha158 feature family, which the paper says is "provided to FaVOR and the LLM-based baselines as the underlying observable column set" (Appendix D) — a tension with the "daily OHLCV only" framing → `underspecified` (which columns the LLM agents actually see).
- **Point-in-time / survivorship:** index membership as-of dates, constituent reconstitution, delisting, ST/special-treatment stocks, price-limit hits and corporate actions → **not stated in source** → `data gap`. S&P 500 constituents fetched from Yahoo today would be the current index (retrospective membership) unless the authors used a point-in-time constituent file; nothing in §4.1 or Appendix Q states which → `data gap` (survivorship risk unquantified).
- **Timestamps / timezone:** not stated → `data gap`.
- **Missing data / suspensions / halted days:** imputation policy and null handling → not stated → `data gap`.
- **Train/validation/test boundaries (§4.1):** train 2022-01-01 → 2023-12-31, validation 2024-01-01 → 2024-12-31, test 2025-01-01 → 2025-12-31. A second, separate protocol appears in Appendix K: formula combination selected on train **2015–2019** + validation **2020**, then held fixed across test years **2021–2025**, with per-ticker cutoffs re-estimated from the immediately preceding validation window and frozen per test year (Table 17), plus 49 overlapping monthly-start 12-month test windows each preceded by a trailing 24-month validation window (Table 18).
- **Benchmark:** CSI 500 index level and S&P 500 index level (Figure 4, Figure 6); all headline metrics are *excess* over that benchmark except MDD, which Appendix C.3 defines on the portfolio's own NAV → mixed definition (see Negative evidence).
- **No** funding, borrow, options-surface, order-book, trade-print, open-interest or on-chain fields are used.

## Execution assumptions

**Source-reported (§4.1 "Backtest Settings", Table 9, Limitations "Cost Model").**

- Signal at time `t` → positions opened "according to the predefined execution protocol" and closed by the holding horizon `T` or stop conditions; thresholds fixed and "applied unchanged throughout the testing period".
- **Costs:** "All backtest results include proportional transaction costs per traded value." CSI 500 — **0.0005 per buy, 0.0015 per sell**; S&P 500 — **0 buy-side, 0.0005 per sell** (Table 9 prints `S&P 500 buy / sell fee 0 / 0.0005`; §4.1 text says "the cost rate is 0.0005 for sells only" — consistent). So the US book pays **no entry-side commission or spread at all**.
- **Slippage / spread / market impact:** explicitly argued away rather than modelled — "daily-bar data, where market impact and slippage are typically negligible at the trade sizes and holding periods we consider … average holding period of 9.64 days, which keeps turnover low. Future work … may require a high-fidelity execution simulator" (Limitations).
- **Borrow / shorting:** not stated in source → `data gap`.
- **Latency / signal-to-order delay, fill model, partial fills, leverage / margin, capacity:** not stated in source → `data gap`.
- **Turnover level:** only a run-to-run *variance* of turnover (0.046, Table 10) is reported; no turnover rate anywhere → `data gap`.
- Baselines are re-run by the authors in the identical shared environment ("Data splits, transaction costs, Qlib execution rule, and stop-loss policy are applied identically across all methods"; ML/DL baselines use the Qlib reference workflow with Alpha158) — Appendix D.

**Research-proposed (not from the source) if this record is ever executed:** symmetric 5 bp per-side cost on both markets, plus an explicit 10 bp slippage and a 1 % ADV participation cap, plus a long-only top-50 equal-weight interpretation of `TopkDropout`, each verified against the released `paper_2026.yaml` before use. These are `research-proposed` operationalizations, not source claims.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned v1 PDF; all are **excess-return** metrics over the stated benchmark (Appendix C), after the paper's own proportional-cost schedule, and have **not** been independently reproduced.

**Table 1 — main results, out-of-sample 2025 (train 2022–2023, validation 2024, test 2025-01-01→2025-12-31):**

| Method | CSI 500 AR | CSI IR | CSI MDD | CSI CR | S&P 500 AR | S&P IR | S&P MDD | S&P CR |
|---|---|---|---|---|---|---|---|---|
| Linear | -0.0702 | -0.5008 | -0.1649 | -0.0778 | -0.0010 | -0.0104 | -0.1403 | -0.0055 |
| XGBoost | -0.0123 | -0.1642 | -0.1370 | -0.0152 | -0.0357 | -0.3345 | -0.2326 | -0.0426 |
| LightGBM | -0.1576 | -1.3954 | -0.2173 | -0.1530 | -0.0302 | -0.3389 | -0.2154 | -0.0353 |
| MLP | -0.0493 | -0.4812 | -0.1725 | -0.0537 | -0.0895 | -0.8041 | -0.1686 | -0.0956 |
| Transformer | -0.0521 | -0.3943 | -0.1760 | -0.0597 | -0.1744 | -1.5509 | -0.1860 | -0.1729 |
| AlphaForge (RL) | -0.0133 | -0.1255 | -0.1260 | -0.0167 | -0.0833 | -0.8617 | -0.2093 | -0.0819 |
| AlphaQCM (RL) | 0.0869 | 1.0604 | -0.1396 | 0.0803 | 0.0619 | 0.8250 | -0.2345 | 0.0583 |
| R&D-Agent (LLM) | 0.1382 | 1.3360 | -0.1427 | 0.1452 | 0.0604 | 0.8028 | -0.1704 | 0.0624 |
| AlphaAgent (LLM) | -0.0192 | -0.1490 | -0.1369 | -0.0275 | -0.0060 | -0.0631 | -0.1428 | -0.0110 |
| **FaVOR** | **0.2067** | **1.5295** | **-0.0853** | **0.2225** | **0.1062** | **1.1315** | **-0.0443** | **0.1123** |

Abstract and §1 restate the same pair: cumulative excess return **0.2225 with IR 1.5295 (CSI 500)** and **0.1123 with IR 1.1315 (S&P 500)**.

**Table 4 — Stage ablation, CSI 500 out-of-sample 2025** (same hypothesis and Stage-4 configuration as the main result): FaVOR `AR 0.2067 / IR 1.5295 / MDD -0.0853`; `w/o Stage 2` `0.0492 / 0.1526 / -0.2091`; `w/o Stage 3` `-0.3902 / -1.2748 / -0.4260`; `w/o Stage 2 & 3` `-0.2793 / -1.4316 / -0.3087`. **Table 13** extends the Stage-2 removal to the S&P 500: IR `1.1315 → -0.8831`.

**Table 3 — backbone sensitivity (all pipeline settings fixed):** CSI 500 IR — GPT-4o **1.5295**, GPT-5.4-mini 1.3246, Qwen3-235B 1.0598, Claude-Sonnet-4.6 0.5364, Gemini-2.5-Flash 0.4998, Llama-3.3-70B 0.4183. S&P 500 IR — GPT-4o **1.1315**, Gemini-2.5-Flash 0.7039, GPT-5.4-mini 0.2553, Qwen3-235B 0.1670, Llama-3.3-70B 0.1545, Claude-Sonnet-4.6 0.0817 (all still positive in AR/IR, per §4.5).

**Table 10 / Table 21 — run-to-run dispersion over 10 independent full-pipeline runs (CSI 500, identical hypothesis prompt and identical thresholds, 3 outer-loop rounds each):** variance IR **0.152** (std 0.390), variance AR **0.042** (std 0.205), variance MDD 0.120 (std 0.346), variance turnover 0.046. R&D-Agent comparator: variance IR 0.191 (std 0.438), variance AR 0.033 (std 0.182), variance MDD 0.055 (std 0.235). The paper adds that this "is not used to claim a statistically significant return gap" (Table 21 note).

**Table 11 — trade-level statistics, CSI 500 out-of-sample:** 1,255 trades; average holding period **9.64 days**; mean per-trade excess return **+2.279 %**; profit factor **1.986**; 10th percentile trade −7.24 %; 90th percentile trade +8.52 % (framed as "gains are broadly distributed", §4.2/Appendix G).

**Table 17 — fixed-combination longitudinal test (one combination per market selected on 2015–2019 train / 2020 validation, formula set and quantile frozen, per-ticker cutoffs re-estimated from the immediately preceding validation window):**

| Test year | CSI 500 AR | CSI 500 IR | S&P 500 AR | S&P 500 IR |
|---|---|---|---|---|
| 2021 | +0.6964 | +1.7117 | +0.0564 | +0.4356 |
| 2022 | +0.1356 | +0.4543 | +0.2377 | +0.9225 |
| 2023 | +0.3317 | +1.2020 | +0.3590 | +2.5526 |
| 2024 | +0.0449 | +0.1259 | +0.3340 | +1.2453 |
| 2025 | +0.1310 | +0.5819 | +0.0826 | +0.5362 |

**Table 18 — 49 overlapping monthly-start 12-month test windows (each preceded by a trailing 24-month validation window; authors note windows overlap and are start-date sensitivity checks, not independent trials):** CSI 500 — CR>0 in **33/49**, mean CR **+0.1931**, mean IR **+0.5919**, mean AR **+0.1894**, mean MDD **−0.2649**; S&P 500 — CR>0 in **39/49**, mean CR **+0.1964**, mean IR **+0.9119**, mean AR **+0.1866**, mean MDD **−0.1406**.

**Table 19 — hypothesis-to-strategy funnel (saved runs):** 10 seed concepts → **520** unique LLM hypotheses (486 in the "paper split", 67 under the single sell-off hypothesis) → **696** outer-loop iterations (622 / 81) → **6,782** candidate formulas (6,058 / 716) → **18,699** Stage-3 candidate combinations (16,741 / 1,148) → **49** iterations passing Stage 3 (41 / 5) → **1,118** combinations with positive OOS return (832 / 47). Appendix L: "Only 49 of 696 hypothesis iterations clear the Stage 3 gate."

**Table 14 — Stage-2 PASS vs FAIL standalone daily cross-sectional RankIC (first-iteration formulas, 437 PASS vs 24 FAIL):**

| Market | Horizon | PASS RankIC | FAIL RankIC |
|---|---|---|---|
| CSI 500 | 1 day | +0.0039 | +0.0025 |
| CSI 500 | 3 days | +0.0025 | +0.0030 |
| CSI 500 | 5 days | +0.0023 | +0.0035 |
| CSI 500 | 10 days | +0.0023 | +0.0047 |
| S&P 500 | 1 day | +0.0040 | +0.0062 |
| S&P 500 | 3 days | +0.0027 | +0.0073 |
| S&P 500 | 5 days | +0.0017 | +0.0065 |
| S&P 500 | 10 days | +0.0021 | +0.0057 |

**Table 20 — unconditional mean 2025 cumulative excess return across *all* Stage-3 combinations under one shared global selectivity:** `σ=0.55` → CSI **+0.2048**, S&P **+0.0817**; `σ=0.75` → +0.0958 / +0.0340; `σ=0.90` → +0.0012 / +0.0245; `σ=0.95` → +0.0048 / +0.0134.

**§M (Directional Selectivity scope):** among **212** evaluated Stage-3 combinations, **81** were rejected for direction instability, and **47 of those 81** still produced a positive after-cost cumulative return in the held-out evaluation; Table 20 meanwhile reports "all **649** Stage 3 combinations".

**Table 15/16 — semantic-validation reliability:** coded-rule comparison against an independent re-implementation of the same checklist over **8,362** cases (no agreement rate printed in the read text → `data gap`); blinded expert assessment over **100** cases (52 CSI / 48 S&P, 50 PASS / 50 FAIL, 44 observation groups): **39 agreement, 49 partial agreement, 12 disagreement**.

**Table 2 — case study (single sell-off / intraday-recovery hypothesis, `horizon_days = 3` narrative):** the three observable conditions are Post Sell-off State, Intraday Recovery and Early Stabilization; for each, one candidate PASSes and one FAILs, e.g. `(close − TS_MIN(low,3)) / (high − TS_MIN(low,3) + eps)` PASS with `POS` mean/median rising 0.083 → 0.914, while `-CORR(rank(DELTA(logV)), rank(DIR))` FAIL because its distribution moves against the stated polarity.

**Table 12 — the two disclosed out-of-sample formula combinations:** CSI 500 (4 formulas, all positive polarity): `f006 = SMA(vol,7)/SMA(vol,60)`, `f008 = (close − MA30)/STD30(close)`, `f002 = Z20(min10 low) − Z20(max10 high)`, `f010 = Δvol10`. S&P 500 (3 formulas, mixed polarity): `f004 = STD7(high − low)` (+), `f001 = min20 close / max15 close` (−), `f007 = STD15(close)` (+).

**Cost / coverage statement from the source:** results are net of the asymmetric proportional fee schedule only (CSI 5 bp buy / 15 bp sell; S&P 0 bp buy / 5 bp sell); no slippage, spread, impact, borrow, latency or capacity treatment exists anywhere in the PDF (the Limitations paragraph argues they are negligible rather than measuring them).

### Independently reproduced

not independently reproduced. No FaVOR pipeline run, no Baostock/Yahoo pull, no Optuna re-run, no baseline re-run and no metric recomputation was executed for this record. The only quantities computed by this scout are file/page/byte/SHA-256 checksums of the pinned PDF and the pinned GitHub tree listing.

### Negative evidence

1. **Run-to-run noise is the same size as the headline.** Table 10/21 put the standard deviation of AR across 10 identical-configuration runs at **0.205** against a headline CSI AR of **0.2067** (IR std 0.390 vs headline IR 1.5295; MDD std 0.346 vs headline MDD −0.0853). A single draw from that distribution can be negative or far larger; the source itself declines to claim significance (Table 21 note).
2. **No multiple-testing control anywhere.** The funnel is 520 hypotheses → 6,782 formulas → 18,699 Stage-3 combinations → 832 (paper split) / 1,118 (all runs) combinations with *positive out-of-sample* return, from which one is selected and reported. No deflated Sharpe, White's reality check, Hansen SPA, Benjamini–Hochberg, Bonferroni or any trial-count correction appears in the PDF (Appendices A–Q read in full). The repository already holds the companion methodological critique family (`[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]`), which is precisely the test this record does not pass.
3. **The unconditional average candidate nearly matches the headline.** Table 20: at `σ=0.55` the mean 2025 cumulative excess return across *all* Stage-3 combinations is **+0.2048 (CSI)** and **+0.0817 (S&P)** versus FaVOR's selected **+0.2225 / +0.1123** — i.e. the selection machinery adds roughly +1.8 pp (CSI) and +3.1 pp (S&P) over "pick any combination at loose selectivity", while at `σ=0.90` the cross-sectional mean collapses to +0.0012 / +0.0245. Either the generation prior is itself strongly tilted or the evaluation is, and the source does not decompose it.
4. **Stage 2 PASS is not a predictiveness filter — by the source's own Table 14.** FAIL formulas beat PASS formulas on mean RankIC in **7 of 8** market×horizon rows (only CSI 1-day goes the other way), with FAIL at +0.0073 vs PASS +0.0027 on S&P 3-day. The paper concedes the gate is "a semantic and distributional consistency filter rather than an individual-factor return predictor" (Appendix I), so the headline improvement cannot be attributed to picking better individual factors.
5. **Backbone dependence on the reported market.** On the S&P 500 the IR moves from **1.1315 (GPT-4o)** to 0.0817 (Claude), 0.1545 (Llama), 0.1670 (Qwen), 0.2553 (GPT-5.4-mini) — a ~14× spread with only the default backbone near the headline; "uniformly positive" (§4.5) is true but several configurations are economically indistinguishable from zero.
6. **Thin and asymmetric cost model.** S&P 500 **entry cost is literally zero** (Table 9), CSI sell cost is 3× the buy cost, and slippage, spread, impact, borrow, latency, capacity and partial fills are argued away (Limitations) rather than measured. Reported results are therefore "net" only in a very narrow sense.
7. **Exit mechanics contradict the stated holding rule.** Holding horizon `T = 7` (Table 8) with stop-loss disabled (Table 9), yet the average holding period is **9.64 days** (Table 11) and §4.1 references additional "stop conditions" that are never defined → exit precedence and the true time-stop are `underspecified`.
8. **Directional Selectivity demonstrably throws away profitable signals.** 81 of 212 evaluated combinations were rejected for direction instability and **47 of those 81 were still positive after costs OOS** (§M); the Limitations block also concedes the criterion cannot handle reversal/contrarian signals at all. The gate therefore selects on a property that is explicitly *not* profitability.
9. **Internally inconsistent metric definitions in Table 1.** Under Appendix C.1/C.4 with a one-year test window, `AR = (1+CR)^(N/T) − 1 = CR`; Table 1 reports CSI AR 0.2067 vs CR 0.2225 (Δ1.6 pp) and S&P AR 0.1062 vs CR 0.1123 (Δ0.6 pp). Additionally, Table 1 is captioned "excess returns" while Appendix C.3 defines MDD on the portfolio's *own* NAV (explicitly not the excess curve) — so the four columns are not all measured on the same series → `data gap` on which quantity is reported.
10. **Unreconciled "Stage 3 combination" denominators.** Table 19 says 18,699 candidate combinations with 49 iterations passing; §M speaks of **212** evaluated Stage-3 combinations; Table 20 speaks of **649** Stage-3 combinations. Three different populations, never reconciled → selection trace `underspecified`.
11. **Same-year, two protocols, wide spread.** For calendar 2025 the main protocol reports CSI AR/IR 0.2067/1.5295 while the fixed-combination protocol (Table 17) reports **0.1310/0.5819** for the same year and market; Table 17 also shows CSI 2024 IR of only 0.1259, and Table 18's mean CSI MDD is **−0.2649** versus the headline −0.0853. The headline is the most favourable of several source-reported views of overlapping claims.
12. **Possible test-set adaptation through the outer loop (not proven, but not excluded).** The regeneration prompt instructs the agent that "previous hypotheses have already been tested (IS/OOS), and you must propose a NEW hypothesis that addresses what failed", and §3.4 says evaluation outcomes flow back as hypothesis memory across **3 outer-loop iterations**. Whether those OOS summaries include the 2025 window that Table 1 reports is never stated → `data gap`; the strict one-shot OOS claim is unverifiable from the paper alone.
13. **Universe construction and survivorship unstated.** Baostock CSI 500 and Yahoo S&P 500 membership is used with no as-of constituent file, no delisting/attrition handling, no ST or price-limit handling documented (§4.1, Appendix Q) → `data gap`; retrospective index membership would embed survivorship bias directly into a top-50 long-only ranking.
14. **Single-year, two-path test regimes.** The authors themselves characterise test-2025 as consolidation→rally (CSI) and drawdown→recovery (S&P) (Appendix H); there is no breadth across volatility regimes, no crisis period inside the headline window, and no turnover level, capacity study, Sharpe/t-stat/IC significance test, or benchmark-mismatch analysis for the portfolio itself.
15. **Semantic-validity evidence is weakly affirmative at best.** Blinded experts gave only **39/100** full agreement with 49 "partial" and 12 outright disagreements (Table 16); the 8,362-case coded-rule comparison is reported without an agreement rate in the read text; the source explicitly limits the interpretability claim to empirical consistency and denies establishing a causal or fundamental mechanism (Appendix J/O).
16. **Provenance/status limits.** Single-authorship-order preprint, v1 only, no journal reference, no comments, submitted 2026-08-31; code dropped in one commit (`98f692a`, 2026-08-30) with no CI evidence read, no third-party replication found, and baselines re-implemented/re-run by the same authors inside their own harness (Appendix D) — baseline rows are self-reported comparisons, not independently verified numbers.
17. **Same author pair already appears in this repository on a different paper.** `Sujin Pyo` and `Huisu Jang` are the authors of `crypto-cross-sectional-low-volatility-premium-post-2017-2026-09-01.md` (FRL 2026 crypto low-volatility) — different source identity, different mechanism, no dedup impact, recorded here only so future scouts do not mistake the name overlap for a duplicate.

## Falsification plan

Each item is a `research-defined falsification threshold` (Scout-chosen, not the source's), stated so that failure is decidable without rescue-by-retuning.

- **F1 — Headline reproducibility.** Using pinned commit `98f692af9e60f1edd3ce8cae74bed7adf0a7ae5a`, `configs/paper_2026.yaml`, Baostock CSI 500 and Yahoo S&P 500 daily data with the documented splits and fee schedule, re-run the pipeline end to end. Failure if the reproduced test-2025 CSI numbers miss `AR 0.2067 ± 0.03` **or** `IR 1.5295 ± 0.25`, or the S&P numbers miss `AR 0.1062 ± 0.03` **or** `IR 1.1315 ± 0.25`. Action: mark the headline `unverified`.
- **F2 — Decoding robustness.** Reproduce the paper's own 10-run protocol (identical prompt and thresholds). Failure if `std(AR) ≥ 0.15` (paper reports 0.205) **or** the fraction of runs with `CR ≤ 0` exceeds 20 %. Action: treat the headline as a single lucky draw, downgrade to `falsified-robustness`.
- **F3 — Selection/multiple-testing control.** Compute the distribution of the reported metric across **all** Stage-3 combinations that the pipeline generates (paper: 16,741 in the "paper split") and apply a deflated-Sharpe / reality-check correction at trial count `N = 16,741`. Failure if the selection-adjusted p-value ≥ 0.05 on either market. Action: reject the claim that the *selection* adds value; retain only "the generator's prior is tilted".
- **F4 — Base-rate decomposition.** Compare the selected combination against the cross-sectional mean of all Stage-3 combinations at matched selectivity (extend Table 20 to the actual per-factor `σ` used). Failure if the selected-minus-mean uplift is < +5 pp CR on the CSI 500 (observed at `σ=0.55`: +0.2225 vs +0.2048 ≈ +1.8 pp). Action: attribute any edge to generation, not to FaVOR's gates.
- **F5 — Cost stress.** Re-price with symmetric entry+exit costs (5 bp/side on S&P instead of 0 bp entry, 15 bp/side on CSI) plus 10 bp slippage and a 1 % ADV cap. Failure if CSI or S&P test-2025 `CR ≤ 0`, or `IR < 0.5` on either market. Action: reject the net-alpha reading.
- **F6 — Test-set contamination audit.** Inspect the released outer-loop logging to determine whether any 2025 test-window metric entered the iteration feedback consumed by the 3 regeneration rounds. Failure if the reported test window appears in any feedback payload. Action: invalidate the strict-OOS framing; reclassify Table 1 as adaptive-selection evidence.
- **F7 — Non-overlapping window replication.** Re-run Table 18 with **non-overlapping** 12-month test windows and a fixed pre-declared combination. Failure if the CSI 500 mean CR ≤ 0 across non-overlapping windows, or if fewer than 60 % of windows are positive on either market (source reports 33/49 = 67 % and 39/49 = 80 % on overlapping windows). Action: reject cross-period robustness.
- **F8 — Gate ablation under new hypotheses.** Repeat Stage-2/Stage-3 ablation (Table 4/13) on ≥ 3 *new* seed concepts and a held-out market period not used in the paper. Failure if removing Stage 2 does not degrade IR by at least 0.3 on a majority of runs. Action: restrict the paper's claim to its single sell-off hypothesis family.
- **F9 — Point-in-time universe audit.** Rebuild both universes with as-of-date constituents and delisting handling. Failure if headline CR falls by more than half. Action: reattribute the result to survivorship.

## Crypto portability

**unproven.** The mechanism is demonstrated only on daily equity index constituents (CSI 500, S&P 500) with a long-only-style top-50 daily holding rule and excess return measured against a broad equity benchmark index. Porting risks:

- **Universe/breadth:** a top-50 `TopkDropout` book needs ~50 liquid, independently rotating names; most crypto spot/perp universes that pass basic liquidity screens are far narrower and dominated by beta to BTC/ETH, so cross-sectional breadth and the benchmark-relative framing both break.
- **Benchmark:** there is no crypto analogue of the CSI 500/S&P 500 total-return index with the same construction; "excess return vs index" would have to be redefined (e.g. vs BTC) — `research-proposed`.
- **24/7 sessions:** daily candle boundaries, timezone and close-to-close alignment differ across venues; the source states no timestamp convention at all (`data gap`), which matters more in 24/7 markets.
- **Perpetuals/funding:** no funding, basis, or carry treatment exists in the source; a crypto port would need funding-aware P&L and an explicit decision on spot vs perpetual.
- **Manipulation/data quality:** the winning signals are volume-ratio and range/std constructs (`SMA(vol,7)/SMA(vol,60)`, `Δvol10`, `STD7(high−low)`), which are exactly the features most exposed to wash trading, thin-book artefacts and venue-specific volume regimes.
- **Execution:** no slippage/impact/borrow model in the source; crypto taker fees and gaps make the S&P "zero entry cost" assumption untenable.
- **Survivorship/listing history:** delistings and short history lengths are far more severe in crypto than in equity indexes; the source already leaves constituent handling unstated.

This is a ported hypothesis, not crypto empirical evidence; `crypto portability: unproven`.

## Limitations

- `underspecified`: per-factor Optuna thresholds, ticker-level cutoffs, position weights, cash treatment, exit precedence, `stop conditions`, turnover level, warm-up, timezone/session convention, seed `concept_text`/knowledge inputs, exact LLM column set (OHLCV-only vs Alpha158-backed), and the mapping between the 49 / 212 / 649 "Stage 3" populations.
- `data gap`: point-in-time constituents, survivorship/delisting/ST/price-limit handling, borrow/shorting, latency, capacity, partial fills, leverage/margin, slippage/spread/impact measurement, whether outer-loop OOS feedback touches the 2025 test window, and the agreement rate for the 8,362-case coded-rule audit.
- `not independently reproduced`: every performance number in this record.
- `unproven`: the causal reading that Stage 2 removes spurious fits; the source explicitly disclaims causal/fundamental mechanism (Appendix J, O) and its own Table 14 shows PASS formulas are not better individual predictors.
- Definition tension: Table 1 AR ≠ CR under the Appendix C formulas for a one-year window; MDD is defined on portfolio NAV while the table is captioned "excess returns".
- Single preprint, v1, no peer review; single headline year (2025) per market in Table 1 with a favourable-of-several protocols; run-to-run AR std equals the headline point estimate; ~14× IR spread across backbones; baseline rows are the authors' own re-runs; released code is one day older than the submission and has no visible independent replication.
- Selection economics: the Directional Selectivity gate discards reversal-type signals by construction (Limitations) and rejected 47 profitable-but-unstable combinations (§M), so the framework is scoped to monotone continuation signals only.
- No Sharpe/t-stat/IC significance test, no turnover or capacity analysis for the reported portfolio; IR is the only risk-adjusted statistic and is reported without a confidence interval.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no FaVOR pipeline execution, no Baostock/Yahoo data pull, no Qlib run, no candidate-pool entry, no Paper / Testnet / Live activity, and no write to any downstream system. This artifact is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this file in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered `/results/_handoff/candidates.json`; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Those stages remain separate and gated.

## Related Wiki records

- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — adjacent multi-agent factor generation with an explicit market-logic prior; different source and mechanism (debate/prior-constrained generation vs FaVOR's distributional construct-validation gate).
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — grammar-guided MCTS/LSTM formulaic alpha search; different search space and no pre-backtest consistency gate.
- `[[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]` — surrogate-guided plan-space evolution; different selection surrogate (performance surrogate vs state-consistency rules).
- `[[quant/factorengine-program-level-knowledge-infused-factor-mining-2026-09-05]]` — Turing-complete program synthesis for factors; different representation and no Stage-2 analogue.
- `[[quant/vst-verifiable-structured-transport-agentic-alpha-discovery-2026-09-12]]` — auditable agent-to-agent alpha discovery with disjoint temporal partitions; complementary audit machinery.
- `[[quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03]]` — LLM-agentic autonomous factor discovery; different harness.
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — leakage-safe, search-aware deflated evaluation; this is the exact multiple-testing test FaVOR does not report (Negative evidence item 2).
- `[[quant/goant-quality-diversity-multi-agent-microstructure-alpha-discovery-2026-09-12]]` — quality-diversity search over microstructure features; different data family.
- Adjacent repository records (file paths, not verified Wiki pages): `beyond-prompting-agentic-factor-investing-composite-long-short-2026-09-24.md`, `factorminer-self-evolving-experience-memory-formulaic-alpha-2026-09-20.md`, `alphaforge-generative-formulaic-alpha-dynamic-factor-timing-2026-09-17.md`, `btc-perpetual-factor-mining-point-in-time-audit-negative-2026-09-04.md`, `crypto-cross-sectional-low-volatility-premium-post-2017-2026-09-01.md` (same two co-authors, different paper and mechanism).

## Sources

1. Hyeonjin Kim, Minseok Kim, Seunghyeon Jung, Sujin Pyo, Huisu Jang, Woojin Lee. *"FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation."* arXiv:2608.30192v1 [cs.AI], submitted 31 Aug 2026 03:16:06 UTC. Landing page: https://arxiv.org/abs/2608.30192 (retrieved 2026-09-24; Comments / Journal-ref / DOI fields empty).
2. Pinned full text: https://arxiv.org/pdf/2608.30192v1 — 28 pages, 3,604,761 bytes, SHA-256 `d42b8bafa7b7c2a6662eb6a2c680bddf7b7363c1318a801384007458f2a9db62`; all tables cited above (Tables 1–24, Figures 1–6, Appendices A–Q) were read directly from this PDF on 2026-09-24.
3. arXiv DOI: https://doi.org/10.48550/arXiv.2608.30192 (HTTP 302 → abs → 200, verified 2026-09-24).
4. Released code: https://github.com/damilab/FaVOR at commit `98f692af9e60f1edd3ce8cae74bed7adf0a7ae5a` ("Initial public FaVOR source release", 2026-08-30T02:53:04Z); 132-entry tree read via the GitHub API on 2026-09-24, including `configs/paper_2026.yaml`, `favor/agent/validation_agent.py`, `favor/coder/factor_coder/function_lib.py`, `docs/DATA_AND_REPRODUCIBILITY.md`.
5. Data/software cited by the source (not fetched for this record): Baostock (CSI 500 daily), Yahoo Finance via `yfinance` (S&P 500 daily), Qlib (`https://arxiv.org/abs/2009.11189`), Optuna, Alpha158 (`https://github.com/microsoft/qlib/blob/85cc74846b5af2e3e6d18666a2f6e399396980b9/qlib/contrib/data/loader.py#L61` as cited by the paper).
