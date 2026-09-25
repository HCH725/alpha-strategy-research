---
schema: strategy-research-record-v1
title: "VolRouter — State-Conditioned Routing over Estimator–Controller Pairs as a Volatility-Control Overlay (arXiv:2608.10375v1)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - volatility-control
  - policy-routing
  - risk-overlay
  - llm-router
  - crypto-portability
status: research-only
confidence: medium
source_as_of: "2026-08-11 (arXiv v1 submission date); market-data references printed in the source are marked 'Accessed April 2026'"
sources:
  - https://arxiv.org/abs/2608.10375
  - https://arxiv.org/html/2608.10375v1
  - https://arxiv.org/pdf/2608.10375v1
  - https://doi.org/10.48550/arXiv.2608.10375
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# VolRouter — State-Conditioned Routing over Estimator–Controller Pairs as a Volatility-Control Overlay (arXiv:2608.10375v1)

## Provenance

- **Source**: arXiv preprint **arXiv:2608.10375**, *"Beyond Forecasting: Recasting Volatility Control as a Routing Problem"*.
- **Authors (exactly as source, complete list, 2 authors)**: **Hongji Pu** (corresponding author, `hongjip2@illinois.edu`) and **Leyang Zhou**; both list **University of Illinois, Urbana-Champaign, Urbana, Illinois, USA** in the pinned v1 HTML title block.
- **Version / date**: **[v1] only**, submitted and last updated **2026-08-11 02:14:20 UTC** (`published == updated` in the arXiv API record); **no v2 exists as of 2026-09-25**. Identifier printed in the pinned HTML as `arXiv:2608.10375v1 [cs.CE] 11 Aug 2026`.
- **Categories**: `cs.CE` (Computational Economics) primary, `cs.AI` secondary. No `q-fin.*` classification.
- **Comments / status**: Comments field = **"24 pages, 6 figures, ACM ICAIF"**; the pinned HTML masthead additionally prints `Conference: ACM International Conference on AI in Finance; 2026; TBD`. **No `journal-ref`, no publisher DOI, no acceptance statement, no peer-review statement anywhere in the record → publication status is preprint-with-conference-formatting; peer-review/acceptance outcome is a `data gap`.**
- **DOI**: DataCite `10.48550/arXiv.2608.10375` resolves **HTTP 200 → https://arxiv.org/abs/2608.10375** (checked 2026-09-25).
- **License**: arXiv non-exclusive distribution license, `http://arxiv.org/licenses/nonexclusive-distrib/1.0/` (linked from the abs page). Because redistribution rights are non-exclusive rather than open, the text below is **quoted/normalised and arithmetically re-derived, never reproduced wholesale**.
- **Pinned primary snapshot read for this record**:
  - HTML v1 `https://arxiv.org/html/2608.10375v1` → **650,184 bytes**, **SHA-256 `ba911ef2d2a413f7846722daffc96116d5145da49779fd30a990984f4c104497`**, converted to **122,736 characters**, read end to end: Sections 1–7, Table 1 (main results) and Table 2 (canonical settings), Figures 1–6 captions, References, and **Appendices A–N** (routing specification, prompts, evaluation protocol, timing/no-lookahead audit, estimator/controller mathematics, data pipeline, cost/switching accounting, reproducibility notes).
  - PDF v1 `https://arxiv.org/pdf/2608.10375v1` → **2,740,544 bytes**, **SHA-256 `98e54bbfc3c16c8fc9f4817aef2d9fae89f45f305fd1d867a264266d7a9571f6`**, used as a byte-identity cross-check of the pinned version (page count not re-derived in this run; the source's own Comments field states 24 pages).
- **Code**: **no repository URL, no code-availability statement and no data-availability statement appear anywhere in the pinned v1 text** (word scan for repository/GitHub/available-at beyond arXiv chrome returns nothing) → **code `data gap`; reproduction is not possible from the source alone.**
- **Data/vendor provenance printed in the source**: References list **Yahoo Finance** (`https://finance.yahoo.com/`, "Accessed April 2026") and **Databento** (`https://databento.com/`, "Accessed April 2026"); the multi-asset engine reads **FRED `DGS3MO`**. The **vendor for the `BTCUSD` and `USDTUSD` series is not stated** → `data gap`.
- **Deduplication (repo-wide, hidden-inclusive)**: `rg --hidden` across the whole working tree (excluding `.git`) plus `coverage_manifest.csv` for `2608.10375`, `VolRouter`, `Recasting Volatility`, `Hongji Pu`, `Leyang Zhou`, `10.48550/arXiv.2608.10375`, `arxiv.org/(abs|html|pdf)/2608.10375` → **0 hits before writing**; only this record matches afterwards. 2,542 `.md` files scanned (1,564 of them inside hidden lanes). The single near-string hit on "Order Routing" belongs to `fifo-queue-partial-identification-l2-execution-sensitivity-2026-09-16.md` and is an unrelated L2-execution policy, cleared.

## Economic mechanism

### Source-reported

The authors argue that volatility control is not primarily a forecasting problem: "Volatility control converts risk estimates into portfolio exposure, yet many existing approaches rely on a fixed estimator or a pre-specified control rule across changing market conditions." Their stated mechanism is to make **policy selection an explicit layer between risk estimation and portfolio action**: the market is summarised into a control-relevant state, a *switch review* decides whether the active pair should be retained, and only then does *pair selection* choose a replacement estimator–controller pair. Portfolio actions are still produced by predefined control policies; the router "does not predict returns or directly generate weights", and the language model "never outputs a portfolio weight or leverage level".

The source attributes its gains to **risk allocation, not return prediction**: "The improvements primarily reflect better risk allocation rather than uniformly higher raw returns", and "the main benefit of routing is improved risk allocation rather than unconditional return maximisation". It further states the benefit is conditional on control heterogeneity: routing "is most useful in environments where the appropriate estimator–controller policy changes with market state", while "in an unusually stable and low-volatility environment, a simpler state-dependent rule may already capture much of the available benefit" (the USDT boundary case).

### Research interpretation

Hypothesis, in falsifiable form: **the identity of the best (volatility estimator → exposure controller) mapping is state-dependent, and a persistent hold/switch gate with *relative* candidate evaluation over trailing diagnostics captures enough of that state-dependence to beat any single fixed pair.** This is a **meta-policy / regime-adapter hypothesis about a risk-allocation overlay — it contains no return-forecasting claim**, and it must not be read as a directional alpha.

Component roles (per the record contract):

```text
Regime / state layer: 3-state volatility label (low / middle / high) inferred at t
                       from decision-time market information by a rule-based,
                       learnable, contextual-bandit or LLM router.
Confirmation layer:    switch review gate g_t ∈ {hold, switch} using trailing
                       H = 63-day diagnostics (risk-adjusted performance,
                       drawdown, volatility tracking, turnover, estimation
                       diagnostics) that end at t-1; switching is further
                       restricted by sticky-period / persistence rules.
Primary selection:     pair selection over the eligible estimator–controller
                       library (209 named pairs before experiment-specific
                       eligibility filters), invoked only when g_t = switch.
Execution / sizing:     the selected pair alone generates the exposure w_t
                       (vol-target scaling, no-trade band, drawdown brake,
                       CVaR targeting, multi-asset covariance scaling, …).
Risk / exit:            controller-internal drawdown brake (d_start 0.10,
                       d_full 0.30, b_min 0.75), CVaR targeting (ES* 0.02),
                       exposure clipping (defaults w_min 0, w_max 1.5;
                       multi-asset Γ = 1.5, single-name cap 0.45).
```

The source's own ablation reads as evidence that the *routing layer* rather than the *library size* carries the effect: "Replacing dynamic routing with a fixed pair causes one of the largest performance degradations" and "simply adding policies does not guarantee better performance unless the Router can select among them effectively." Downstream research should still treat every component as non-alpha until ablated.

## Signal

- **Formation timestamp**: decisions are made at date `t` on a daily grid. "All estimator inputs and market-state features are constructed only from information available before the corresponding portfolio action, and the resulting action is evaluated on subsequent returns." Routing diagnostics use only completed historical transitions over `H_t = {t-H, …, t-1}`, **H = 63**; "No routing diagnostic at date t contains r_{t+1} or later realized portfolio returns." **Timezone / session-boundary convention for the daily cut is not stated → `data gap`.**
- **Decision chain (fully specified at the formulation level)**: `I_t → s_t → g_t → k_t → w_t`, i.e. state inference → switch review → pair selection → controller action. Structured JSON outputs are validated against admissible labels and the supplied candidate set; invalid/failed outputs fall back to deterministic logic.
- **Lookback**: estimator-specific and enumerated in Appendix D (e.g. EWMA/GARCH/HAR windows, `T_train = 504` training days, candidate score evaluated on the training window, 252-observation rolling standard deviation used for ±5σ winsorisation of estimator inputs, 63-day trend window, 252-day loss buffer for ES). Router diagnostic window H = 63.
- **Entry / exit**: this is an exposure-scaling overlay, not a long/short entry rule. Documented controllers are **long-only with cash**: `w_min = 0` defaults, multi-asset normalisation floors weights with `max(w, 0)`, exposure scaling is `clip(v* / max(σ̂_t, ε), w_min, w_max)` with a **5% no-trade band**, and multi-asset portfolio scaling is clipped at **Γ = 1.5**. Exit = the controller lowering exposure; there is no short entry, no stop order, no take-profit in the source.
- **Holding / rebalancing**: daily re-decision; actual weight change is what the turnover cost charges. Switching is regularised by the hold/switch gate, minimum-hold logic and persistence guidance; **a monetary penalty for changing pair identity is explicitly not applied in the reported runs** (Appendix M).
- **Parameters (all `source-reported`)**: volatility targets / costs / annualisation / estimation windows from Table 2 — S&P 500 `σ*=0.10, 5 bp, 252, 252`; Multi-Asset `0.10, 5 bp, 252, 126`; Bitcoin `0.35, 8 bp, 365, 90`; USDT `0.02, 2 bp, 365, 90`. Walk-forward driver defaults `T_train = 504, T_test = 126, T_step = 126` (non-overlapping OOS tiles). Training-window candidate score `J_train(k) = SR_net − 0.5·DD − 0.5·TO − 0.5·VTE − 1.0·QLIKE` with 80th-percentile constraints on estimator loss, turnover and volatility-tracking error. Candidate-pool diagnostic sizes `{27, 42, 57, 72, 87, 102, 117}`; multi-asset pool-reduction seed `20260703`; ML estimators `random_state = 42`; hosted LLM inference at `temperature = 0`.
- **Underspecified / `data gap` in the source (not repaired here)**: (i) the **headline S&P 500 OOS window dates** — only the component-ablation window `2023-02-10 → 2026-02-10` and the multi-asset start `2024-02-09` (history from `2023-02-10`) are printed; (ii) the **Bitcoin and USDT evaluation windows** are never dated; (iii) the **multi-asset constituent list** ("cross-asset panel" only, plus a hard-coded defensive set `{IEF, TLT, GLD, UUP}` inside one controller); (iv) the **exact state-profile feature vector and the deterministic/rule-based router thresholds**; (v) the **identities of the four LLM router backbones** (Figure 6 labels them graphically only); (vi) switch-rate / dwell-time / turnover values are said to be "implementation outputs" but **no numeric turnover table is printed**. Consequently the routing rule is **reconstructible in structure but not bit-for-bit reproducible**: mark the signal **underspecified** for exact reproduction.

## Required data

- **Instruments / universe** (Table 2): S&P 500 setting = **`SPY` / ES futures**; Multi-Asset = **"cross-asset panel"** (constituents not enumerated → `data gap`); Digital Market = **`BTCUSD`**; USDT = **`USDTUSD`**.
- **Venue / market type**: equity index futures + ETF (SPY) — Databento minute data for ES with roll-date detection and a back-adjusted continuous close; a multi-asset daily panel; two crypto **spot-style daily series (market type not stated: spot vs perpetual vs index → `data gap`)**.
- **Timeframe**: minute ES data resampled to business-day frequency; daily bars elsewhere; annualisation 252 (equity, multi-asset) vs 365 (Bitcoin, USDT).
- **Fields**: log returns; realised/EWMA/GARCH/HAR volatility inputs; **VIX variance, change in VIX variance, variance-risk-premium, jump indicator, yield-curve and inversion features, term-spread and credit-spread information** for the XGBoost estimator and for state features; drawdown/equity path; turnover; FRED `DGS3MO` as the multi-asset risk-free leg.
- **Point-in-time**: features are lag-shifted one day; "all features are shifted one day"; estimator/controller state is rebuilt before OOS evaluation so "fitted estimator/controller state does not cross the train/test boundary"; Appendix G provides a decision-time information-set audit. Publication timestamps for VIX/yield-curve inputs are not separately documented → `data gap`.
- **Timestamp / timezone**: not stated (daily grid, business-day calendar for equity; 365-day annualisation for crypto) → `data gap`.
- **Missing data**: multi-asset panel drops all-missing rows and **sets remaining missing asset returns to zero** ("equivalent to treating a missing asset observation as a flat return for that day") — the source flags this as an interpretation caveat; ES series is forward-filled on the business-day calendar; crypto missing-data treatment not stated → `data gap`. Winsorisation is applied to estimator inputs (±5×252-day rolling σ) while raw returns are retained for P&L.
- **Funding / fee / spread needs**: **not present in the source** (see Execution assumptions).

## Execution assumptions

- **Cost model (the only cost that exists)**: net return is `R_{t+1}^{net} = w_tᵀ r_{t+1} − λ_to ‖w_t − w_{t−1}‖_1`, i.e. a **flat proportional charge on one-way weight turnover**, with λ = **5 bp (S&P 500), 5 bp (Multi-Asset), 8 bp (Bitcoin), 2 bp (USDT)**; "Portfolio returns are evaluated after the transaction costs specified for each setting." The multi-asset implementation includes the cash leg. **No monetary penalty is charged for changing pair identity** in the reported runs (Appendix M); switching is only regularised by the gate and persistence rules.
- **Signal-to-order timing**: routing uses information strictly before `t`; the resulting action "is evaluated on subsequent returns" → **next-period (daily) execution, effectively close-to-next-bar in the source's own convention**; exact same-bar vs next-bar price used for the trade is not further specified → `data gap`.
- **Order type / fill model / latency / spread / slippage / impact / participation / capacity**: **word-boundary scan of the pinned v1 text: `slippage` 0, `bid-ask` 0, `commission` 0, `fees` 0, `borrow` 0, `shorting` 0, `margin` 0, `market impact` 0, `latency` 0, `fill` 0, `participation` 0, `liquidity` 0; `transaction cost` 8 occurrences all inside the λ_to model and its sensitivity sweep; `spread` hits are macro term-spread/credit-spread *features*; `capacity` hit is intra-portfolio weight redistribution, not market capacity; `funding` hit is arXiv's funding-support footer; `leverage` hits are an XGBoost feature and the "LLM never outputs leverage" constraint.** → **every one of those items is a `data gap`, never a zero.**
- **Shorting / borrow**: not used and not discussed → long-only overlay with cash; borrow availability `data gap`.
- **Funding, mark/index price, liquidation (crypto legs)**: **absent → `data gap`.**
- **Leverage / margin**: exposure bounds are model constraints (`w_max` defaults 1.5, multi-asset Γ = 1.5, single-name cap 0.45); no margin or margin-call model → `data gap`.
- **Capacity / partial fills / failures**: not modelled → `data gap`.
- **What the source assumes vs what we assume**: everything above is `source-reported`. Any additional friction we would add (funding on a perp leg, real spread on BTC/USDT, venue slippage) is **`research-proposed`** and belongs to the falsification ladder, not to the reported evidence.

## Evidence

### Source-reported

All figures below are **source-reported**, read from the **pinned v1 Table 1 ("Main out-of-sample results across four volatility-control settings")**, columns `Ann. Ret. (%) / Ann. Vol. (%) / Sharpe / MDD (%) / CVaR (%)` (daily 95% CVaR), each block read row-by-row so that method, market and column identity stay aligned; returns are **net of the per-setting proportional turnover charge only** (Section 4.2, Table 2).

| Setting | Method | Ann. Ret | Ann. Vol | Sharpe | MDD | CVaR |
|---|---|---|---|---|---|---|
| S&P 500 | RV + Naive Scaling | 11.11 | 11.67 | 0.952 | 15.10 | 1.76 |
| S&P 500 | EWMA Targeting | 10.31 | 10.85 | 0.951 | 14.02 | 1.63 |
| S&P 500 | Regime-Aware Fixed | 10.28 | 12.39 | 0.830 | 15.85 | 1.81 |
| S&P 500 | Mixture-of-Experts | 10.45 | 10.90 | 0.958 | 15.06 | 1.66 |
| S&P 500 | Contextual Bandit | 9.35 | 10.45 | 0.895 | 13.41 | 1.60 |
| S&P 500 | **VolRouter** | **10.84** | **8.87** | **1.222** | **12.58** | **1.32** |
| Multi-Asset | RV + Naive Scaling | 16.35 | 10.91 | 1.498 | 7.84 | 1.56 |
| Multi-Asset | EWMA Targeting | 11.62 | 9.05 | 1.283 | 8.88 | 1.32 |
| Multi-Asset | Regime-Aware Fixed | 11.60 | 8.86 | 1.309 | 6.26 | 1.30 |
| Multi-Asset | Mixture-of-Experts | 12.41 | 8.88 | 1.398 | 6.28 | 1.27 |
| Multi-Asset | Contextual Bandit | 10.59 | 8.04 | 1.318 | 9.24 | 1.20 |
| Multi-Asset | **VolRouter** | **13.20** | **8.57** | **1.540** | **6.60** | **1.18** |
| Bitcoin | RV + Naive Scaling | 29.56 | 39.57 | 0.747 | 51.69 | 4.68 |
| Bitcoin | EWMA Targeting | 27.26 | 36.56 | 0.745 | 51.95 | 4.30 |
| Bitcoin | Regime-Aware Fixed | 1.60 | 6.73 | 0.238 | 7.24 | 0.99 |
| Bitcoin | Mixture-of-Experts | 5.99 | 7.51 | 0.798 | 6.85 | 1.00 |
| Bitcoin | Contextual Bandit | 10.28 | 36.27 | 0.283 | 51.47 | 4.56 |
| Bitcoin | **VolRouter** | **30.81** | **27.43** | **1.123** | **39.39** | **3.25** |
| USDT | RV + Naive Scaling | −4.71 | 4.37 | −1.078 | 17.75 | 0.32 |
| USDT | EWMA Targeting | −3.81 | 2.99 | −1.274 | 15.95 | 0.27 |
| USDT | Regime-Aware Fixed | 4.75 | 0.52 | 9.140 | 0.89 | 0.05 |
| USDT | Mixture-of-Experts | 4.10 | 1.04 | 3.943 | 2.70 | 0.08 |
| USDT | Contextual Bandit | 4.94 | 0.52 | 9.566 | 0.81 | 0.05 |
| USDT | **VolRouter** | **4.41** | **0.53** | **8.379** | **1.25** | **0.06** |

Other source-reported results, each anchored to its own figure/section:

- **Headline claim** (Abstract / Section 5.1): VolRouter "achieves the highest Sharpe ratio in three of the four settings"; S&P Sharpe 0.952 → 1.222 with MDD 15.10% → 12.58% and CVaR 1.76% → 1.32% while **annualised return is slightly lower (10.84% vs 11.11%)**; Multi-Asset Sharpe 1.498 → 1.540 with CVaR 1.56% → 1.18%; Bitcoin both highest return (30.81%) and Sharpe (1.123) with MDD 51.69% → 39.39%.
- **Ablation (Figure 4, Section 5.2)**: full VolRouter Sharpe **1.47 under the ablation driver** — explicitly *not* comparable to Table 1, and the error bars "should not be interpreted as confidence intervals for Table 1". Largest degradations come from removing relative pair comparison, removing temporal/previous-action context, and **replacing dynamic routing with a fixed pair**.
- **Sensitivity (Figure 5, Section 5.3)**: Sharpe **1.55 at a 5% target** falling to **≈0.9–1.0 at 15–25% targets**; transaction-cost sweep moves Sharpe only mildly ("within a relatively compact range"); switching sensitivity is **non-monotonic**; pool-size relationship "not monotonic at every pool size".
- **Library size (Section 6)**: expanding the candidate pool **27 → 117** moves Sharpe **0.97 → 1.11** (`our count`: +0.14), "without monotonic gains at every intermediate size".
- **Backbones (Figure 6, Section 5.4)**: "no single model uniformly dominates every setting"; Bitcoin shows the widest rolling-Sharpe dispersion, USDT the narrowest.
- **Timing/audit**: routing diagnostics end at `t−1`; pair objects reconstructed before OOS evaluation; Appendix G gives a decision-time information-set table.

**Our own arithmetic on the printed Table 1 cells, labelled `our count`** (VolRouter minus `RV + Naive Scaling` within the same market block): S&P Sharpe **+0.270**, return **−0.27 pp**, realised vol **−2.80 pp**, MDD **−2.52 pp**, CVaR **−0.44 pp**; Multi-Asset Sharpe **+0.042**, return **−3.15 pp**, vol **−2.34 pp**, MDD **−1.24 pp**, CVaR **−0.38 pp**; Bitcoin Sharpe **+0.376**, return **+1.25 pp**, vol **−12.14 pp**, MDD **−12.30 pp**, CVaR **−1.43 pp**; USDT Sharpe **+9.457 vs RV + Naive** but **−1.187 vs the best baseline (Contextual Bandit 9.566)** and **−0.761 vs Regime-Aware Fixed (9.140)**. Bitcoin realised volatility **27.43% sits 7.57 pp below its own 35% target** (`our count`).

### Independently reproduced

not independently reproduced.

### Negative evidence

1. **The source itself attaches no statistics to the headline**: Appendix I states the manuscript "does not attach block-bootstrap confidence intervals or formal multiple-comparison-adjusted significance tests to the main table" and that statements of outperformance are "descriptive of the reported held-out backtests rather than claims of population-level statistical dominance."
2. **The USDT block is a losing case for routing**: VolRouter Sharpe 8.379 < Contextual Bandit 9.566 and < Regime-Aware Fixed 9.140 — the source concedes "pair-level routing is most useful when the appropriate control action varies meaningfully across market states."
3. **USDT Sharpe magnitudes (9.14, 9.57, 8.38) are an artefact of a ≈0.5% volatility denominator**, so the whole USDT block is weak evidence in either direction.
4. **The S&P gain is not a return effect**: VolRouter's annualised return (10.84%) is *below* the fixed RV + Naive baseline (11.11%); the Sharpe improvement comes from holding realised vol at 8.87% against a 10% target.
5. **The Multi-Asset margin is thin**: Sharpe +0.042 over RV + Naive while raw return is −3.15 pp, and the baseline RV + Naive has the highest raw return in that block.
6. **Selection risk in the headline S&P run**: Appendix F.3 — "the headline S&P results are a contiguous OOS evaluation with train-window preselection, **not an average over repeated walk-forward folds**", and only the ablation window is dated (`2023-02-10 → 2026-02-10`).
7. **LLM component is not seed-controlled**: "Hosted LLM generation is not fully seed-controlled even at temperature zero", and the four backbone identities are not printed → run-to-run variance cannot be bounded from the paper.
8. **Cost model is proportional turnover only** — no spread, slippage, borrow, impact, latency, fill, participation, capacity, funding or leverage cost (see Execution assumptions), so the Bitcoin 8 bp and USDT 2 bp settings are almost certainly optimistic for a daily-rebalanced overlay.
9. **Implementation caveats in Appendix D contradict the labels of several library members**: `NaiveVolEstimator` uses an uncentered second moment; the wavelet estimator is fully commented out and non-functional; `HybridEWMARegime` returns only the slow scalar on the main path; `GJR-GARCH` parameters are held fixed between 63-step recalibrations; regime estimators use RV quantiles rather than an HMM; missing multi-asset returns are zero-filled. Twelve such caveats are enumerated by the source.
10. **No code and no data-availability statement** → no independent reproduction is even possible from the record alone.
11. **Bitcoin and USDT evaluation windows are never dated**, so the crypto results cannot be tied to a regime.
12. **Preprint status**: no journal-ref, no acceptance statement, peer-review outcome unknown (ACM ICAIF 2026 "TBD" in the masthead).
13. **Library-size effect is small and non-monotonic** (27 → 117 pairs gives only +0.14 Sharpe, without monotonicity), which weakens any "more policy diversity" story and puts more weight on the single reported configuration.
14. **No capacity, turnover or switch-rate numbers are printed** despite the source saying these are produced by the engine.
15. **Cross-record neighbours (same repo, different source identity)**: `simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11.md`, `aegis-momentum-gated-hierarchical-minimax-sortino-allocation-2026-09-12.md` and `cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02.md` already cover volatility-managed/regime-gated overlays from other sources; none of them studies *router-level* estimator–controller switching, so no direct contradiction was located — and the absence of located contradiction is not evidence that none exists.

## Falsification plan

Every threshold below is a **`research-defined falsification threshold`** and every construction step is **`research-proposed`**; none of these are source claims.

- **F1 — Walk-forward replication**: rebuild the S&P setting as **≥5 non-overlapping folds** (`T_train = 504, T_test = 126, T_step = 126`) with pair preselection frozen inside each training window. **Fail** if VolRouter's net Sharpe margin over `RV + Naive Scaling` is ≤ 0 in **≥3 of 5 folds**, or if the median margin is < +0.10.
- **F2 — Statistical significance**: **1,000-draw 63-day moving-block bootstrap** on the daily net-return differential vs `RV + Naive Scaling` and vs `Contextual Bandit` for each setting. **Fail** if the 95% interval includes 0 in the S&P and Bitcoin comparisons (the two settings carrying the headline).
- **F3 — Multiplicity audit**: Benjamini–Hochberg **q < 0.10** across the full grid of 4 settings × 5 baselines. **Fail** if no pairwise comparison survives.
- **F4 — Honest cost ladder**: **0 / 5 / 10 / 20 / 30 bp** per unit traded, plus a paid-spread run at **20% ADV participation**, plus **5 bp/year financing** on the 1.5× exposure and (for a perpetual port) **funding charged every 8 h**. **Fail** if the Bitcoin Sharpe margin is ≤ 0 at **10 bp** or the S&P margin is ≤ 0 at **20 bp**.
- **F5 — Is the LLM layer carrying the result?** Replace the router with a **frozen deterministic rule-based** state/hold/switch policy using the same state features and diagnostics. **Fail** if ≥ **80%** of the reported Sharpe margin survives *only* with the LLM (i.e. the deterministic router collapses the margin by >80%, or if the deterministic router matches it, the "LLM router" framing is unsupported — either outcome must be reported).
- **F6 — Backbone and seed invariance**: run **4 named backbones × 3 seeds** (plus the deterministic router) on the same frozen windows. **Fail** if run-to-run Sharpe standard deviation > **0.10**, or if the sign of the margin vs `RV + Naive` flips in ≥ 2 of 4 settings.
- **F7 — Look-ahead audit**: recompute with routing diagnostics ending at **t−2** and with the train-window champion frozen for the whole OOS block. **Fail** if the S&P margin shrinks by > **50%**.
- **F8 — Regime-heterogeneity test (the paper's own claim)**: split each sample into high-state and low-state blocks defined by the frozen state profile. **Fail** if routing does not beat the fixed pair in the **high-state** blocks (the mechanism predicts the gain concentrates there), or if the gain appears only in low-state blocks.
- **F9 — Router-vs-random control**: add a **random pair selector** and a **random hold/switch gate** matched to VolRouter's switch rate. **Fail** if VolRouter's margin over the random router is < **50%** of its margin over `RV + Naive Scaling`.
- **F10 — Crypto portability**: port the overlay to BTC/ETH perps with funding, 24/7 day boundaries, venue-fragmented candles, and a long-only vs 1.5× exposure comparison. **Fail** if the net Sharpe margin over a fixed EWMA target is ≤ 0 after funding, or if the result depends on the unspecified crypto vendor/period (i.e. reverses under a second data source).
- **Action on failure**: record the failed axis in this record's negative evidence, downgrade `confidence` to `low`, and do not advance beyond research-only. No failure outcome authorises any implementation.

## Crypto portability

**`adapted`** — with a partial empirical foothold.

- **What already exists**: the source itself runs `BTCUSD` (35% target, 8 bp, 365-day annualisation, 90-day estimation window) and `USDTUSD` (2% target, 2 bp) as "digital-market stress tests", and Bitcoin is the setting where VolRouter's margin is largest (Sharpe 0.747 → 1.123). So the mechanism is **not purely a ported equity hypothesis**.
- **Why it is still only `adapted`**: (i) the **crypto series vendor, market type (spot/perp/index) and evaluation windows are all unstated**; (ii) the cost model has **no funding, no mark/index basis, no liquidation, no venue fragmentation, no 24/7 session or day-boundary convention**; (iii) the USDT block behaves like a stablecoin-hold overlay and produces a metric artefact rather than evidence; (iv) Bitcoin realised vol lands **7.57 pp below its 35% target**, i.e. the overlay systematically under-deploys the stated risk budget on the crypto leg; (v) a daily grid with an unspecified cut cannot represent perp funding timestamps or 24/7 candle boundaries.
- **Porting risks to price before any test**: spot vs perpetual replacement of `BTCUSD`, funding charged every 8 hours against a long-only 1.5× exposure, mark-price vs last-price discrepancies, exchange fragmentation across candle boundaries, and the fact that a 2 bp turnover charge is far below realistic crypto spreads for a daily-rebalanced overlay.
- Crypto portability is **not** authorisation to trade.

## Limitations

- **underspecified**: headline S&P OOS dates; Bitcoin and USDT evaluation windows; multi-asset constituents; crypto data vendor and market type; state-profile feature vector; deterministic-router thresholds; LLM backbone identities; turnover/switch-rate numbers; timezone/session conventions.
- **not independently reproduced** — and **not reproducible from the source**: no code repository, no data-availability statement, hosted LLM inference that is not seed-controlled.
- **data gap (never to be read as zero)**: spread, slippage, borrow, shorting, margin, funding, market impact, capacity, participation, latency, partial fills, and any market-quality constraint on the crypto legs.
- **Point estimates only**: no confidence intervals, no multiple-comparison control, no placebo test, no significance test anywhere in the pinned v1.
- **Single configuration, single research group, single paper**, preprint status with unknown peer-review outcome; **publication-bias risk** applies.
- **Identification**: this is a four-setting backtest with train-window preselection; the USDT block shows the method can *lose* to simpler selectors, and the Multi-Asset margin (+0.042 Sharpe) is inside the noise one would expect without significance tests.
- **Scope**: this is a **risk-allocation overlay with no return-forecast claim**. It must not be recorded or presented as a directional alpha, and its Sharpe improvements must not be compared against unrelated records' gross figures — the printed numbers are net only of a 2–8 bp proportional turnover charge.
- **Implementation caveats**: twelve source-enumerated discrepancies between library member names and their audited behaviour (Appendix D), plus zero-filling of missing multi-asset returns, limit how literally the "209-pair library" can be read.
- **Capacity/liquidity**: never modelled; no turnover, switch-rate or ADV numbers are printed.

## Implementation status

`implementation_status: not-implemented`.

Nothing in our research stack has been implemented for this record: no router, no estimator–controller library, no backtest, no Qlib run, no production card, and no Paper/Testnet/Live activity of any kind. This document is a research capture of an external preprint only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, or received Paper, Testnet or Live approval — nor that the strategy is profitable, validated alpha, or approved for implementation. Those are separate, explicitly gated decisions.

## Related Wiki records

Verified by `kb_search` against the vault before writing (only vault-returned pages are linked):

- [[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]] — adjacent: regime-routed specialist models with volatility targeting and dual-threshold hysteresis; different source, different selection mechanism (regime-gated model selection rather than estimator–controller policy routing).
- [[quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]] — adjacent: macro-conditioned risk matching with walk-forward evidence in a timing/allocation context.

`kb_search` for "volatility targeting routing policy selection portfolio control" returned 3 pages, "volatility control regime switch drawdown risk overlay" returned 7, and "LLM agent selects trading policy regime label mixture of experts selector" returned **0** — so no LLM-router page exists and none is linked. No page was written to Wiki Brain.

## Sources

- arXiv abs page: https://arxiv.org/abs/2608.10375 (v1 only; Comments: "24 pages, 6 figures, ACM ICAIF"; license: arXiv non-exclusive distribution 1.0) — accessed 2026-09-25.
- Pinned primary full text (HTML v1): https://arxiv.org/html/2608.10375v1 — 650,184 bytes, SHA-256 `ba911ef2d2a413f7846722daffc96116d5145da49779fd30a990984f4c104497` — Sections 1–7, Tables 1–2, Figures 1–6 captions, References, Appendices A–N.
- Pinned primary PDF (v1): https://arxiv.org/pdf/2608.10375v1 — 2,740,544 bytes, SHA-256 `98e54bbfc3c16c8fc9f4817aef2d9fae89f45f305fd1d867a264266d7a9571f6`.
- DataCite DOI: https://doi.org/10.48550/arXiv.2608.10375 (resolves to the abs page) — checked 2026-09-25.
- Data references cited *by the source* (not independently opened for this record): Yahoo Finance (`https://finance.yahoo.com/`, accessed April 2026), Databento (`https://databento.com/`, accessed April 2026), FRED series `DGS3MO`.
