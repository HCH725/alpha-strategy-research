---
schema: strategy-research-record-v1
title: "LiMT: Hierarchical Multi-Task Learning with Liquidity-Aware Signals and Participation-Capped Adaptive Portfolio Optimization on CSI300/CSI500 A-Shares"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning
  - multi-task-learning
  - liquidity-aware
  - cross-sectional
  - china-ashare
  - qlib
  - portfolio-construction
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - "https://arxiv.org/abs/2609.25617v1 (arXiv landing, v1 submitted 22 Sep 2026, cs.CE; accessed 2026-09-23)"
  - "https://arxiv.org/pdf/2609.25617v1 (primary PDF read in full, 9 pages; SHA-256 0d83206c3f7999cf753491c44b6e629f413ebb6245974992d4c8b08f4ce5ac0a, 2087999 bytes, retrieved 2026-09-23)"
  - "https://doi.org/10.48550/arXiv.2609.25617 (arXiv DOI)"
  - "anonymous.4open.science/r/LiMT-F039 (code-availability statement on page 1 of the PDF; returned HTTP 401 when checked 2026-09-23, not publicly retrievable)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LiMT: Hierarchical Multi-Task Learning with Liquidity-Aware Signals and Participation-Capped Adaptive Portfolio Optimization on CSI300/CSI500 A-Shares

## Provenance

- **Primary source (only source used for every empirical claim below):** Hengyi Yang, Sida Lin, Yiyan Qi, Yankai Chen, Haohan Zhang, Xianhua Peng, Jian Guo, *"Hierarchical Multi-Task Learning with Liquidity-Aware Signals for Stock Forecasting"*, **arXiv:2609.25617v1 [cs.CE]**, submitted **22 Sep 2026**; DOI `10.48550/arXiv.2609.25617`; license CC BY 4.0. Landing: https://arxiv.org/abs/2609.25617v1 · PDF: https://arxiv.org/pdf/2609.25617v1 (`source-reported`).
- **Author list exactly as printed on the PDF title page (page 1), with affiliations and contribution markers:** `Hengyi Yang¹*,‡, Sida Lin²*, Yiyan Qi³*, Yankai Chen⁴, Haohan Zhang⁵, Xianhua Peng¹,†, Jian Guo³,†` — ¹Peking University, Shenzhen, China · ²The Chinese University of Hong Kong, Shenzhen, China · ³International Digital Economy Academy (IDEA), Shenzhen, China · ⁴Cornell University, Ithaca, United States · ⁵The Hong Kong University of Science and Technology, Guangzhou, China. `*` Equal contribution; `†` Corresponding authors (Xianhua Peng, Jian Guo); `‡` "This work was conducted during his internship at IDEA Research" (`source-reported`).
- **Version/date verification:** the PDF footer stamp reads `arXiv:2609.25617v1 [cs.CE] 22 Sep 2026`; the landing page shows a single version `[v1] … Submitted on 22 Sep 2026`; PDF metadata `/arXivID = https://arxiv.org/abs/2609.25617v1`, `/Author = Hengyi Yang; Sida Lin; Yiyan Qi; Yankai Chen; Haohan Zhang; Xianhua Peng; Jian Guo`, `/Title` matches the landing title, `/Creator = arXiv GenPDF (tex2pdf:0d14211)`. No v0/v2 and no separate journal version exists as of 2026-09-23 (`source-reported`).
- **Primary-source artifact checksum (this run):** PDF fetched 2026-09-23 = **2,087,999 bytes, SHA-256 `0d83206c3f7999cf753491c44b6e629f413ebb6245974992d4c8b08f4ce5ac0a`**, 9 pages, full text extracted locally and read end-to-end (title page, §I–§V, Tables I–IV, Figures 1–5 captions, Appendices A–C, 37 references). All fields below were checked against this exact version; nothing is taken from a search snippet or secondary summary.
- **Sample period (§IV.1 "Datasets", page 4):** Chinese A-share data spanning **2008–2020**, splits **train 2008-01-01 → 2014-12-31**, **validation 2015-01-01 → 2016-12-31**, **test 2017-01-01 → 2020-08-01**. Backtest window reported separately as **CSI300, 2017–2020** (§IV-C, pages 6–7) (`source-reported`).
- **Universe (§IV.1, page 4):** **CSI300** and **CSI500** constituents of the Chinese A-share market; features = the public **Alpha158** set from Qlib [ref 28]; lookback **τ = 21** days; prediction horizon **w = 1 day** (`source-reported`). Index-constituent point-in-time/rebalance rule: **not stated in source** → `data gap`.
- **Transaction-cost / slippage treatment (read from §III-D Eq. 22–26, §IV-C.1 pages 6–7, and Appendix A page 8 — not inferred from the abstract):** the APO backtest allocates **CNY 1×10⁹ to each side** (long and short), charges **transaction cost of 10 basis points per trade**, and caps each stock's traded value at **2% of its daily turnover** (participation cap `α = 2%` inside Eq. 26). **Spread, slippage, market impact, borrow/securities-lending fee, sell-side stamp duty and latency: not stated in source** (whole-PDF scan of `commission`, `spread`, `slippage`, `impact`, `borrow`, `stamp`, `latency` returns only bibliography/usages unrelated to the backtest cost model) → the only modeled friction is the flat 10 bps + participation cap → `data gap`.
- **Publication / preprint status:** **arXiv preprint only**. The PDF carries no journal, conference-acceptance, DOI-beyond-arXiv, or peer-review statement; index terms are "Regression, time series, financial data mining, machine learning". Treat as **not peer-reviewed** (`source-reported`). Code-availability line on page 1: *"An anonymized repository is available at anonymous.4open.science/r/LiMT-F039"* — that URL was opened during this run and returned **HTTP 401**, i.e. the code is **not publicly retrievable** → `data gap` for independent reproduction.
- **Pre-write deterministic dedup (2026-09-23, ripgrep across ALL 894 `*.md` records in this repository, not `git log`):** `2609.25617`, `10.48550/arXiv.2609.25617`, `LiMT`, `Hierarchical Multi-Task Learning with Liquidity-Aware Signals`, `Liquidity-Aware Signals for Stock Forecasting`, `Market Regime Encoder`, `Liquidity-Driven Learning`, `Hengyi Yang`, `Xianhua Peng`, `4open.science/r/LiMT`, `20 replacements per day` → **zero records carry this source identity**. The only hit for the generic phrase `Adaptive Portfolio Optimization` is `latent-drift-kalman-bucy-macd-optimal-portfolio-2026-09-03.md`, a different source with a different mechanism (Kalman–Bucy drift filter), so it is not a duplicate. Same-lab adjacency: `janus-q-event-driven-trading-hierarchical-gated-reward-modeling-2026-09-04.md` shares co-author Yiyan Qi (IDEA) but is a different paper, mechanism and market object. Worktree was clean (`git status --porcelain --untracked-files=no` empty) and `origin/main` was fast-forwarded before researching.

## Economic mechanism

### Source-reported

The authors argue three linked mechanisms (`source-reported`, i.e. the authors' stated rationale, not established fact):

1. **Order-of-operations in representation learning.** Prior relation-aware architectures fix an ordering between temporal aggregation and cross-sectional interaction, which either averages away day-specific peer effects or entangles transient co-movement with stock-specific momentum. LiMT's **Market Regime Encoder (MRE)** therefore applies **cross-stock attention independently at every historical step first**, and only then runs a **within-stock temporal attention** encoder, so market-wide synchronisation and within-stock dynamics stay separable (§I, §III-B).
2. **Liquidity variables carry alpha and are usable as auxiliary supervision.** Volume and volatility "carry independent alpha content" and "directly affect risk-adjusted performance and execution feasibility" (§I, citing [24], [25] including Goyenko–Kelly–Moskowitz–Su–Zhang, *"Trading Volume Alpha"*). The **Liquidity-Driven Learning (LDL)** module is a multi-gate mixture-of-experts that jointly predicts next-day **return**, **volume shock** and **volatility**, and transfers the two auxiliary tasks into the return head through **stock-wise sigmoid gates** `β_v`, `β_σ`, so liquidity/risk information is injected only where it helps and negative transfer is suppressed (§III-C, Eq. 15–21).
3. **Prediction accuracy must be converted into executable weights.** The **Adaptive Portfolio Optimization (APO)** rule de-normalises the predicted volume/volatility into physical units, min-max normalises them inside the candidate group, linearly fuses a **liquidity-preference weight** with an **inverse-volatility risk weight** via parameter `r ∈ [0,1]`, and then **clips each name to a 2% participation cap** before any weight is tradable (§III-D, Eq. 22–26). The authors explicitly frame the reported gain as APO improving "how the signal is executed, rather than merely amplifying conventional style exposures", supported by a Fama–French five-factor regression (§IV-C.2, page 7).

### Research interpretation

Falsifiable restatement of the hypothesis this record captures (Scout wording, not the authors'):

- **Regime (implicit, not label-driven):** time-varying cross-sectional synchronisation is learned per step by cross-stock attention rather than imposed by a discrete regime label.
- **Primary signal:** cross-sectional rank/score of predicted 1-day-forward return `z_r = Close(t+2)/Close(t+1) − 1`, z-scored across the universe at each day.
- **Confirmation / auxiliary signal:** jointly predicted volume shock `z_v` and normalized range `z_σ`, gated into the return head; at portfolio time they re-enter as **liquidity preference (predicted volume)** and **risk aversion (predicted volatility)** weights.
- **Position sizing / risk:** `w* = min(r·w^σ + (1−r)·w^A, α·A_{i,t}/C)` with `α = 2%` participation cap — a **sizing/execution overlay, not an alpha source**, and it must be ablated separately from the forecast.
- **Hypothesized channel:** cross-sectional mispricing is corrected noisily by liquidity-constrained flow; conditioning sizing on expected volume and expected volatility raises realized (executable) return per unit of turnover, while cross-task gating makes the return forecast itself liquidity-aware. **Do not assume each component contributes alpha** — the paper's own ablation (Table II) is mixed, see Negative evidence.

## Signal

All items below are `source-reported` unless explicitly marked `research-proposed` / `underspecified`.

- **Targets (§II, page 1–2).** On trading day `t` the model uses the historical feature window to predict targets realized at `t+2`:
  - Main task return `z_r = Close(t+2) / Close(t+1) − 1`.
  - Auxiliary volume shock `z_v = log(volume_{t+2}) − (1/5)·Σ_{i=1..5} log(volume_{t+2−i})`.
  - Auxiliary volatility `z_σ = (high_{t+2} − low_{t+2}) / vwap_{t+2}`.
  - Every target is cross-sectionally z-scored on its own trading day: `ZS(y) = (y − μ_y)/std_y`.
- **Inputs:** Alpha158 feature set (Qlib), lookback `T = τ = 21` trading days, prediction horizon `w = 1 day`, hidden size `d = 256`, `head_cross = 4`, `head_temp = 2`, learning rate `1e-5`, ≤100 epochs with early stopping, 3 random seeds reported as mean ± std (§III-B, §IV.4, Appendix A).
- **MRE (§III-B, Eq. 1–14):** linear feature projection → multi-head **cross-stock attention on each time-step slice** `H*[:,k,:]` (softmax over the S×S contemporaneous similarity matrix) → residual + LayerNorm → per-stock multi-head **temporal attention** over the 21-step window → last-step hidden state `h_q` per stock.
- **LDL (§III-C, Eq. 15–21):** MMoE with per-task softmax gates `α_k` over `n` shared experts; task-specific projection `G_k` to `d/2`; stock-wise sigmoid transfer gates `β_v`, `β_σ`; enhanced return representation `o'_r = G_r(o_r) + β_v⊙G_v(o_v) + β_σ⊙G_σ(o_σ)`; loss `L = Σ_{i∈{r,v,σ}} λ_i·MSE(ẑ_i, z_i)` with `λ_r ∈ {0.63,0.65,0.68,0.7}`, `λ_v ∈ {0.3,0.33,0.35}`, `λ_σ ∈ {0.03,0.05,0.08}` selected by validation IC (Appendix A). **Number of experts `n`: not stated in source** → `underspecified`.
- **Formation timestamp / tradability:** features and targets are daily; target uses `t+2` closes with a stated `w = 1 day` horizon, i.e. the signal is meant to be acted on between the `t` close and the `t+1`/`t+2` reference prices — **the exact signal-to-order timestamp and execution price are not specified** → `underspecified` (material for any replication).
- **Long entry / short entry (§III-D + §IV-C.1):** at day `t`, sort stocks by predicted `ẑ_r`; **top decile = long candidate set, bottom decile = short candidate set**; APO then assigns weights `w*` inside each set.
- **Two different portfolio constructions appear in the paper — both preserved, not merged:**
  1. **Benchmark predictive evaluation (§IV.3, page 4):** "The portfolio simulation follows a **daily top-50 long strategy with 20 replacements per day**." This is the construction behind Table I's `AR_excess` / `IR_excess`.
  2. **Deployment backtest (§IV-C.1, pages 6–7):** **daily long-short decile portfolios** (top decile long, bottom decile short) weighted by APO or by the three baselines, over **CSI300 2017–2020**. This is Table III/IV.
- **Rebalance / holding period:** daily re-ranking and daily re-weighting; turnover is reported (Table III) rather than a fixed holding period. Whether positions are held exactly 1 day is **not stated** → `underspecified`.
- **Parameters (all `source-reported`, fixed values unless noted):** participation cap `α = 2%`; APO risk/liquidity mixing `r` swept over `{0.1 … 0.9}` with **best reported at `r = 0.1`**; baseline weighting rules defined in Appendix A Eq. 28 (equal weight), Eq. 29–30 (20-day inverse-volatility risk parity), Eq. 31–32 (rank-based linear normalisation with reversed ranks on the short side).
- **Selection caveat (`research-proposed` reading):** `r = 0.1` is chosen as the best of 9 values **on the same 2017–2020 window that is reported** — no separate validation window for `r` is stated → treat the headline APO number as selection-affected until re-run out-of-sample.
- **Ties / simultaneous signals / suspensions / limit-up-limit-down handling:** **not stated in source** → `underspecified`. This is material in Chinese A-shares (daily ±10%/±20% bands, T+1 buy-then-sell rule, trading halts).

## Required data

- **Instrument / universe:** Chinese A-share equities, **CSI300** (large-cap) and **CSI500** (mid-cap) constituents; backtest on CSI300 only (§IV.1, §IV-C).
- **Venue / market type:** Chinese onshore stock exchanges (Shanghai/Shenzhen) — the paper says "Chinese A-share market" and cites Qlib; **specific exchange(s), data vendor beyond Qlib, and index-constituent source: not stated** → `data gap`.
- **Timeframe:** daily bars (OHLCV, VWAP, volume); lookback 21 trading days.
- **Fields used:** close, high, low, vwap, volume (targets); Alpha158 features (Qlib public set: price/volume/turnover-derived rolling features).
- **Point-in-time:** train/val/test split dates are given, but **constituent membership point-in-time correctness, corporate actions, suspension handling, and any feature publication lag: not stated** → `data gap`. The test split ends **2020-08-01**; nothing after that date appears anywhere in the paper → **no post-2020 out-of-sample evidence**.
- **Timestamp / timezone:** daily session convention, close-time definition and timezone are **not stated** → `data gap`.
- **Missing data:** imputation/exclusion rules for suspended or newly listed names: **not stated** → `data gap`.
- **Cost/fee fields:** flat 10 bps per trade + 2% daily-turnover participation cap are specified; **spread, slippage, impact, borrow/lending fee, sell stamp duty, latency: not stated** → `data gap`.
- **Capital:** CNY 1×10⁹ per side in the APO backtest (§IV-C.1) — a scale at which a 2% participation cap on CSI300 names is already binding; capacity above that is **not studied** → `data gap`.

## Execution assumptions

`source-reported` unless marked otherwise.

- **Signal-to-order timing:** **not stated** (see Signal) → `underspecified`; do not assume same-bar or next-bar fills.
- **Order type / fill model:** not stated → `underspecified`. Only the **2%-of-daily-turnover participation cap** per stock is explicit (Eq. 26 and Appendix A, page 8).
- **Fees:** 10 basis points per trade, applied in the APO backtest (§IV-C.1, Appendix A). Whether that 10 bps is intended to absorb commission + stamp duty + venue fees is **not stated** → `data gap`.
- **Spread / slippage / impact:** **not modeled, not stated** → `data gap`; every Table III/IV figure therefore rests on a flat-10 bps friction assumption.
- **Gross vs net:** the paper reports **no separate gross-of-cost series** for Table III/IV → `data gap`. The reported figures come from a simulation configured with 10 bps per trade and the participation cap; they are *not* fully-loaded net-of-everything numbers.
- **Leverage / margin / shorting:** long-short decile construction is assumed implementable; **A-share short availability (margin/securities-lending inventory, recall risk, borrow cost), T+1 settlement rule, and margin financing: not stated** → `data gap`. This is the single largest executability question for the reported backtest.
- **Order success rate (OSR):** reported as a metric (Table III, Appendix B) with values 29.27%–38.00%, but its **definition and computation are not given** → `underspecified`; do not reinterpret it as a fill-rate or a win-rate without the code (which is not retrievable).
- **Latency / partial fills / failures:** not stated → `data gap`.
- **Independent assumptions of ours:** none. No Scout-side execution rule is introduced in this record.

## Evidence

### Source-reported

Every figure below is `source-reported`, traced to **arXiv:2609.25617v1** at the cited table/section, on the cited sample, and has **not** been independently reproduced.

- **Table I (page 5), test split 2017-01-01 → 2020-08-01, mean ± std over 3 seeds, portfolio simulation = daily top-50 long with 20 replacements/day:**
  - **CSI300 — LiMT:** IC **0.0575 ± 0.00**, ICIR **0.4462 ± 0.03**, `AR_excess` **0.1809 ± 0.00**, `IR_excess` **2.0414 ± 0.03**. Paper-stated relative improvement over the strongest baseline: **+6.88% / +5.41% / +56.22% / +51.98%**; the corresponding strongest baselines read off Table I are MASTER (IC 0.0496), GRU (ICIR 0.2448 → not the max; the max baseline ICIR is MASTER 0.4321), DoubleEnsemble (`AR_excess` 0.1158, `IR_excess` 1.3432).
  - **CSI500 — LiMT:** IC **0.0496 ± 0.00**, ICIR **0.452 ± 0.02**, `AR_excess` **0.1529 ± 0.00**, `IR_excess` **2.0166 ± 0.03**; paper-stated relative improvement **+13.94% / +14.08% / +23.11% / +32.26%** (strongest baselines read off Table I: MASTER IC 0.0435, GRU ICIR 0.3962, MASTER `AR_excess` 0.1242, LightGBM `IR_excess` 1.5247).
  - Baseline dispersion that matters for interpretation: on CSI500, **TCN `AR_excess` = −0.0682 (IR −1.0386)** and **TabNet `AR_excess` = −0.0016**; tree models (XGBoost IC 0.0538 on CSI300) remain competitive on IC while converting less of it into return.
- **Table II (page 5), ablation on CSI300, same four metrics (IC / ICIR / `AR_excess` / `IR_excess`):**
  - full LiMT (Table I) **0.0575 / 0.4462 / 0.1809 / 2.0414**
  - `w/o Auxiliary Tasks` **0.0543 / 0.4035 / 0.1734 / 1.9418**
  - `w/o LDL` **0.0568 / 0.4342 / 0.1845 / 1.9993**
  - `w/o Auxiliary Tasks & LDL` **0.0528 / 0.3841 / 0.1687 / 1.8104**
  - `w/o Cross-Stock Modeling` **0.0493 / 0.4130 / 0.1277 / 1.6929**
  - `w/o Auxiliary Tasks & LDL & Cross-Stock Modeling` **0.0489 / 0.4060 / 0.1049 / 1.3838**
  - Auxiliary heads on the held-out split (§IV-B, page 6): volume-shock **IC/ICIR 0.3435 / 2.95**; volatility **IC/ICIR 0.5157 / 4.36**.
- **Table III (page 7), CSI300 long-short decile backtest 2017–2020, CNY 1×10⁹ per side, 10 bps per trade, 2% daily-turnover cap per stock:**

  | Metric (paper's direction) | Equal-weighted | Risk parity | Rank-based | **APO (r = 0.1)** |
  |---|---|---|---|---|
  | OSR ↑ | 32.13% | 29.27% | 30.05% | **38.00%** |
  | AR ↑ | 3.99% | 3.19% | 3.38% | **10.01%** |
  | Downside Vol ↓ | 0.031 | 0.027 | 0.0278 | **0.050** |
  | MD ↓ | 3.73% | 3.15% | 3.28% | **4.94%** |
  | Turnover ↓ | 20.73% | 19.13% | 19.42% | **24.98%** |
  | ShR ↑ | 1.22 | 1.16 | 1.18 | **1.86** |
  | P/L ↑ | 1.59 | 1.69 | 1.67 | **1.73** |
  | SoR ↑ | 1.29 | 1.20 | 1.22 | **2.00** |
  | CR ↑ | 1.07 | 1.01 | 1.03 | **2.03** |

  Headline claim (abstract, §I, §IV-C.2, §V): APO lifts **annualized return 3.99% → 10.01%**, **Sharpe 1.22 → 1.86** versus equal weighting; versus rank-based, **AR 3.38% → 10.01%**, **Sharpe 1.18 → 1.86** (`source-reported`).
- **Risk-adjusted check (§IV-C.2, page 7):** over the same 2017–2020 window, a **Fama–French five-factor regression of the model-induced long-short spread yields a daily alpha of 0.35%, p < 0.01** (`source-reported`; same window as the `r` selection, no separate OOS).
- **Table IV (page 8), sensitivity to `r` (OSR / AR / ShR / MD / P/L / SoR / CR / Downside Vol / Turnover):** `r = 0.1` → 0.3800 / **0.1001** / **1.8607** / 0.0494 / 1.7309 / 2.0030 / 2.0260 / 0.0500 / 0.2498; monotone degradation to `r = 0.9` → 0.2913 / **0.0262** / **1.1035** / 0.0282 / 1.6274 / 1.1405 / 0.9297 / 0.0230 / 0.1937. Note `r = 0.9` Sharpe **1.1035 is below the equal-weighted 1.22** baseline of Table III.
- **Ablation claim (§IV-B):** removing modules drops performance "by 1.39% to 7.80%"; the largest single IC drop is removing cross-stock modeling (0.0575 → 0.0493).

### Independently reproduced

`not independently reproduced`. No re-run of LiMT/APO was performed in this repository; the anonymized code URL returns HTTP 401 (2026-09-23), so the reported figures could not even be executed against the authors' own implementation. Everything above remains a third-party claim on a non-peer-reviewed v1 preprint.

### Negative evidence

**Carried by the source itself:**

- **Cross-task transfer does not dominate on every metric:** `w/o LDL` posts a **higher `AR_excess` (0.1845) than the full model (0.1809)** and a near-identical IC (0.0568 vs 0.0575) — Table II. The paper narrates the ablation as uniformly degrading ("Performance drops across all metrics, by 1.39% to 7.80%") but its own table contradicts that for `AR_excess`.
- **Profitability is bought with risk and turnover:** APO raises **max drawdown 3.73% → 4.94%**, **downside vol 0.031 → 0.050**, **turnover 20.73% → 24.98%** (Table III); the authors themselves call this "a deliberate return–risk trade-off rather than mechanically lower-risk allocations".
- **The weighting parameter is fragile:** across `r = 0.1 … 0.9` the Sharpe falls monotonically **1.8607 → 1.1035** and AR **10.01% → 2.62%** (Table IV); at high `r` the construction underperforms the equal-weighted baseline Sharpe.
- **Universe dependence:** gains are reported as less stable on CSI500 than CSI300 (§IV-A), and several baselines are outright negative on CSI500 (Table I), showing how much the conclusion depends on the universe.
- **Capital-scale assumption:** each side is CNY 1×10⁹ with a 2% participation cap; no capacity/impact analysis beyond that cap is presented.

**Flagged by Scout (not in the source):**

- **No post-2020 evidence at all** — every headline number sits inside 2017-01-01 → 2020-08-01, a window that ends before the 2021 China small-cap drawdown, the 2022–2024 A-share bear, and the 2024-09 policy-driven reversal; the model-selection window and the reporting window are the same.
- **Cost model is one flat number:** 10 bps/trade with no spread, slippage, impact, borrow fee or sell stamp duty; A-share round-trip costs plus stamp duty and a realistic spread routinely exceed 10 bps on mid-caps, so the 10.01% AR and 1.86 Sharpe are **upper bounds**.
- **Short-leg executability is assumed, not demonstrated:** no treatment of securities-lending availability/cost, T+1 settlement, price-limit bands, or halts — precisely the frictions that decide whether a daily long-short decile book on CSI300 is implementable at all.
- **Multiple-testing / selection:** 14 baselines × 2 universes × 6 ablations × 9 values of `r`, 3 seeds, all reported without any deflated-Sharpe or multiple-comparison correction; `r = 0.1` and the FF5 alpha are evaluated on the same window.
- **Ambiguous "the strategy":** Table I's top-50 long book and Table III's decile long-short book are different constructions; a reader cannot tell which one the abstract's "10.01% / 1.86" generalizes from beyond the stated backtest.
- **Code not retrievable** (HTTP 401), so metric definitions (notably OSR), fill rules and constituent handling cannot be audited.
- Related literature the paper itself cites as context — Goyenko et al. *"Trading Volume Alpha"* [25] and the A-share-specific records already in this repository (see Related) — is where independent cost/decay evidence for volume- and liquidity-based signals would have to come from; this paper supplies none.

## Falsification plan

Ten tests. Every threshold below is **`research-defined falsification threshold`** (Scout-chosen, not from the source); every construction rule not in the paper is marked **`research-proposed`**. Failure action in all cases: keep the record at `research-only / not-implemented / not-approved`, and do **not** rescue the claim by re-tuning.

1. **Frozen post-2020 holdout (`research-proposed` data):** re-train with the identical 2008–2016 split and evaluate **2021-01-01 → present** on point-in-time CSI300/CSI500 constituents. **Reject if** net Sharpe ≤ **1.0** (below the source's own equal-weighted 1.22) or `IC ≤ 0` on that window.
2. **Full cost ladder (`research-proposed`):** 10 / 20 / 40 bps per trade plus explicit A-share sell stamp duty and a half-spread term, applied identically to all four weighting rules. **Reject the APO edge if** APO annualized return falls **below the equal-weighted 3.99%** at any rung ≤ 20 bps.
3. **Executability overlay (`research-proposed`):** add T+1, ±10%/±20% price-band, and suspension/limit-up-or-down fill rules (skip-and-carry unfilled orders). **Reject the deployability claim if** realized AR drops by **more than 50%** versus the paper's 10.01%.
4. **Short-leg ablation (`research-proposed`):** run long-only (top decile) versions of all four weightings. **Reject the "sizing adds alpha" claim if** APO long-only Sharpe ≤ equal-weight long-only Sharpe.
5. **Auxiliary-shuffle placebo (`research-proposed`):** keep architecture and hyperparameters, randomly permute the volume-shock and volatility targets across stocks within each day before training. **Reject the liquidity-information channel if** the shuffled-auxiliary Sharpe stays **within 20% of 1.86** (i.e. ≥ 1.49) — that would mean the gain is architecture/regularization, not liquidity signal.
6. **LDL replication of the paper's own contradiction (`research-defined`):** re-run Table II on CSI300. **Treat the cross-task-transfer claim as refuted if** `w/o LDL` ≥ full LiMT on **all four** metrics (currently it already wins on `AR_excess`).
7. **`r`-selection hygiene (`research-proposed`):** choose `r` on the 2015–2016 validation split only, freeze it, then evaluate 2017–2020. **Reject the reported magnitude if** the frozen-`r` test Sharpe < **1.4** (midpoint between baseline 1.22 and reported 1.86).
8. **Multiple-testing deflation (`research-defined`):** compute a deflated Sharpe over the 14 × 2 × 6 × 9 grid actually searched. **Treat the edge as unproven if** DSR < **0.95**.
9. **Capacity stress (`research-proposed`):** scale each side from CNY 1×10⁹ to 1×10¹⁰ with a square-root market-impact term layered on the 2% participation cap. **Cap the capacity claim if** AR halves at 1×10¹⁰.
10. **Competing-explanation controls (`research-proposed`):** regress the long-short spread on FF5 plus size, turnover and Amihud illiquidity; compare against the A-share factor-library and low-volatility records already staged in this repository. **Attribute the result to style/liquidity beta, not to LiMT, if** residual daily alpha < **0.10%** (one third of the reported 0.35%).

## Crypto portability

**`unproven`.** The source contains **zero** crypto content (whole-PDF scan for `crypto`, `bitcoin`, `perpetual`, `token`, `24/7` → no hits), so this must not be labeled `direct` or `adapted` — it is a ported hypothesis with no crypto empirical evidence.

Portability analysis (Scout interpretation):

- **What ports conceptually:** the architecture (per-step cross-stock attention → per-stock temporal attention), the multi-task gating of return/volume/volatility, and the participation-capped liquidity/risk weighting rule are venue-agnostic math.
- **What does not port directly:**
  - **Universe:** CSI300/CSI500 index constituents have no crypto analogue; a port would need a `research-proposed` top-N-by-ADV universe with listing/survivorship rules written from scratch, and index-rebalance effects (a real A-share signal component) disappear entirely.
  - **Data dependency:** the whole construction sits on **Alpha158 features recomputed on crypto bars** — a different feature distribution, plus 24/7 candle boundaries instead of a single daily session; day boundaries, funding settlements and weekend gaps change every rolling window in the paper.
  - **Shorting & costs:** the long-short decile book assumes short availability. In crypto-perps shorting is easy but **funding, isolated margin, liquidation cascades and venue-specific fee tiers** replace borrow fees — none of which the source models.
  - **Participation cap:** `α = 2% of daily turnover` was calibrated implicitly on CSI300 liquidity; crypto depth is fragmented across venues, so the cap constant would have to be re-estimated per venue (`research-proposed`).
  - **Frictions in the other direction:** no price-limit bands and T+0 in crypto remove two of the A-share frictions the source ignores — so porting could plausibly *improve* fill realism while changing the mechanism's binding constraint. Neither direction has been tested.
- **Bottom line:** any claim that "liquidity-aware multi-task sizing works on crypto" is a **different mechanism under different data dependencies** and would require its own record with its own primary source.

## Limitations

- `not independently reproduced` — no re-run, and the anonymized code repository returns HTTP 401 (checked 2026-09-23).
- `data gap`: spread, slippage, market impact, borrow/lending fee, sell stamp duty, latency — none stated; only 10 bps/trade + 2% participation cap are modeled.
- `data gap`: no gross-of-cost backtest series for Table III/IV; no post-2020 sample; no capacity analysis above CNY 1×10⁹ per side.
- `data gap`: index-constitute point-in-time rule, exchange/data vendor, timezone/session convention, suspension and corporate-action handling, missing-data policy.
- `underspecified`: number of MoE experts `n`; batch size; signal-to-order timestamp and execution price; holding-period/rebalance fill mechanics; treatment of ties; T+1 / price-band / halt rules; definition of OSR; whether `r` was selected on a validation window (no such window is stated).
- `unproven`: generalization beyond 2017–2020, beyond CSI300/CSI500, and to any crypto market.
- **Source quality:** single non-peer-reviewed arXiv v1 preprint in `cs.CE`, submitted one day before this record was written; IEEE-style two-column formatting suggests a conference submission but **no acceptance is stated** → publication status `not stated in source` beyond "arXiv preprint".
- **Internal inconsistency preserved, not repaired:** the §IV-B narrative claims uniform degradation across ablations while Table II shows `w/o LDL` beating the full model on `AR_excess`.
- **Selection/multiplicity:** `r`, hyperparameters and baselines were all tuned/reported on overlapping windows with no deflated-Sharpe correction.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack: no Qlib run, no production card, no Paper/Testnet/Live activity, no reproduction of Tables I–IV. The paper's own implementation is not retrievable (HTTP 401), so even a code-level audit has not occurred. This record is a normalized research capture only; implementation authorization is a separate, explicitly reviewed decision.

## Adoption boundary

Presence of this record in this repository means only that normalized research material entered the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. All frontmatter gates remain `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — authoritative schema this record conforms to.
- Adjacent records already staged in this repository (filename-level adjacency only; none shares this source identity — verified by the dedup search in Provenance):
  - `mim-stocr-momentum-integrated-multitask-approxndcg-cqb-2026-09-06.md` — another multi-task equity record, different source and construction.
  - `nystrom-attention-cross-sectional-stock-transformer-low-rank-2026-09-11.md` — cross-sectional stock transformer architecture record.
  - `csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05.md` — CSI300 regime/gating record.
  - `china-ashare-factor-library-overfitting-audit-amihud-illiquidity-falsification-2026-09-13.md` — A-share factor-library overfitting/illiquidity audit (competing-explanation control for falsification test 10).
  - `china-ashare-limit-up-momentum-unfillable-execution-falsification-2026-09-13.md` — A-share limit-up fill unavailability (directly relevant to falsification test 3).
  - `china-ashare-l2-burst-volume-recency-imbalance-intraday-2026-09-13.md` — A-share intraday volume/microstructure record.
  - `maple-multi-alpha-position-aware-listwise-ensembling-2026-09-04.md` — multi-signal alpha ensembling with position awareness.
  - `latent-drift-kalman-bucy-macd-optimal-portfolio-2026-09-03.md` — the only record containing the generic phrase "Adaptive Portfolio Optimization"; different source and mechanism, retained here as the dedup disambiguation note.

## Sources

1. Hengyi Yang, Sida Lin, Yiyan Qi, Yankai Chen, Haohan Zhang, Xianhua Peng, Jian Guo. *"Hierarchical Multi-Task Learning with Liquidity-Aware Signals for Stock Forecasting."* **arXiv:2609.25617v1 [cs.CE]**, submitted 22 Sep 2026. DOI: https://doi.org/10.48550/arXiv.2609.25617 · Landing: https://arxiv.org/abs/2609.25617v1 · PDF: https://arxiv.org/pdf/2609.25617v1 (9 pages, 2,087,999 bytes, SHA-256 `0d83206c3f7999cf753491c44b6e629f413ebb6245974992d4c8b08f4ce5ac0a`, retrieved 2026-09-23; full text read for this record — §I–§V, Tables I–IV, Appendices A–C).
2. Code-availability statement cited *inside* source 1 (page 1): `anonymous.4open.science/r/LiMT-F039` — checked 2026-09-23, HTTP 401, not retrievable (recorded as a provenance/reproduction gap, not used for any claim).
3. No secondary summary, search-result snippet, abstract-only page, blog or aggregator was used to fill any field of this record; the arXiv landing metadata was used only to confirm version/date/author identity already verified on the PDF title page.
