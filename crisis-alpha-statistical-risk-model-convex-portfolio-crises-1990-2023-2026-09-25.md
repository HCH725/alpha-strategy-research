---
schema: strategy-research-record-v1
title: "Risk-Model-Driven Long-Only Convex Portfolios Across Four Market Eras (Min-Variance, Maximum Diversification, Risk Parity under Three Covariance Estimators)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-construction
  - covariance-shrinkage
  - crisis-episodes
  - equity-long-only
status: research-only
confidence: medium
source_as_of: 2024-08-18
sources:
  - https://arxiv.org/abs/2409.14510
  - https://doi.org/10.48550/arXiv.2409.14510
  - https://arxiv.org/pdf/2409.14510v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal contradiction 1 (frontmatter-declared): the abstract states that the proposed models 'consistently outperformed market excess returns across all periods', while Section 5 Conclusion states that 'no single strategy consistently outperforms across all conditions'; the paper's own printed tables support the Conclusion, not the abstract — the minimum-variance column prints a LOWER average excess return than the value-weighted benchmark in 11 of 12 printed panels (our count from Tables 1(a)-4(c)) and a negative average excess return in the post-COVID panels (Table 4(a) -3.98%, Table 4(b) -3.38%)."
  - "Source-internal contradiction 2 (frontmatter-declared): the abstract says the models are tested using 'five different investment strategies', while Section 3 Proposed Methodology says 'We evaluated four investment diversification strategies'; the printed tables in Section 4 carry five strategy columns (Market value-weighted, Equal Weighted, Minimum Variance, Maximum Diversification, Risk Parity)."
  - "Source-internal contradiction 3 (frontmatter-declared): the Section 4 discussion of Table Group 4 says 'For simplicity, we don't include risk parity portfolio analysis for this period', yet Table 4(a) and Table 4(b) both print a populated Risk Parity column (12.25% / 13.66% average excess return, Sharpe 0.70 / 0.68); only Table 4(c) prints Risk Parity as NaN."
  - "Source-internal numeric inconsistency 4 (frontmatter-declared, our arithmetic): in every printed cell the Sharpe ratio equals the printed average excess return divided by the printed standard deviation to within 0.011, except Table 4(b) Minimum Variance, where -3.38 / 2.72 = -1.24 while the printed Sharpe is -1.49."
---

# Risk-Model-Driven Long-Only Convex Portfolios Across Four Market Eras (Min-Variance, Maximum Diversification, Risk Parity under Three Covariance Estimators)

## Provenance

- **Primary source (pinned version):** Maysam Khodayari Gharanchaei and Reza Babazadeh, *"Crisis Alpha: A High-Performance Trading Algorithm Tested in Market Downturns"*, arXiv preprint `arXiv:2409.14510v1 [q-fin.PM primary; q-fin.CP, q-fin.RM, q-fin.TR]`.
- **Complete author list exactly as source (two authors, both with `*`/`†` "corresponding author" footnotes):**
  1. Maysam Khodayari Gharanchaei — *1 Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania, US*; footnote: "First Corresponding author: M. Khodayari G. (mkhodaya@andrew.cmu.edu)".
  2. Reza Babazadeh — *2 Faculty of Engineering, Urmia University, Urmia, West Azerbaijan Province, Iran*; footnote: "Second Corresponding author: R. Babazadeh (r.babazadeh@urmia.ac.ir)".
  Per-author affiliation mapping is explicitly numbered in the title block (`1` / `2`), so it is source-stated, not inferred.
- **Version / date:** arXiv API returns `published` = `updated` = **2024-08-18T19:35:07Z**, single version only — submission history shows **`[v1] Sun, 18 Aug 2024 19:35:07 UTC (1,889 KB)`** submitted by Maysam Khodayari Gharanchaei; **no v2/v3** (nothing beyond v1 in the history block, checked on the abs page 2026-09-25). Source-metadata observation, not interpreted: the identifier month prefix `2409` does not match the recorded 2024-08-18 submission timestamp.
- **Stable URL / identifier:** `https://arxiv.org/abs/2409.14510`; canonical DataCite DOI `10.48550/arXiv.2409.14510` → `curl` returned **HTTP 302 → https://arxiv.org/abs/2409.14510** (verified 2026-09-25).
- **Pinned full text actually read:** `https://arxiv.org/pdf/2409.14510v1` downloaded 2026-09-25 at **1,934,423 bytes** (matching the abs-page "(1,889 KB)"), **31 pages**, extracted with pypdf 6.16.2 to **60,373 characters / 1,104 lines** and read end to end, covering the title block, Abstract, Sections 1-5 (Introduction, Literature Review, Proposed Methodology, Computational Results, Conclusion), all 12 printed result tables (Tables 1(a)-1(c), 2(a)-2(c), 3(a)-3(c), 4(a)-4(c)), Figures 1(a)-5(c) captions, and the full References list. The arXiv HTML endpoint for this identifier returns **HTTP 404** (`/html/2409.14510v1`), so the PDF is the only machine-readable primary text and is the pin for every figure quoted below.
- **Publication / preprint status (measured 2026-09-25):** abs page has **no Comments field, no Journal-ref, no publisher DOI beyond the DataCite arXiv DOI, and no peer-review statement anywhere** → **preprint / working paper only, no claim of peer review**. License is the **arXiv.org non-exclusive distribution license (`licenses/nonexclusive-distrib/1.0/`)** — *not* a Creative Commons licence — therefore this record cites and normalizes the work and does not reproduce it. No SSRN, RePEc, NBER or journal mirror was located in this run.
- **Declarations:** **no** data-availability statement, **no** code/GitHub statement, **no** conflict-of-interest / funding / acknowledgement declaration, and **no** generative-AI statement anywhere in the pinned PDF → all recorded as **`data gap`** (word scan of the pinned text: `code` 0, `github` 0, `data availability` 0, `declaration` 0, `conflict of interest` 0, `chatgpt` 0).
- **Cost-treatment determination (mandatory Methods-level read, not abstract-based):** Section 3 *Proposed Methodology* was read in full (pinned PDF lines 258-372: data source, estimation window, the three covariance estimators, the three convex programs (5), (7), (8), the 5% upper band, the CVXPY/GUROBI solver, the PSD failure note), plus Section 4 setup and Section 5 Conclusion. Pinned-text word-boundary scan: `transaction` 2 and `cost` 2 (both inside the *Literature Review* sentence about an unrelated 52-year buy-and-hold study), `trading cost` 1 (same sentence), `slippage` 0, `bid-ask`/`bid ask` 0, `fee` 0, `commissi` 0, `spread` 1 (the phrase "spread of the crisis", not a bid-ask spread), `borrow` 0, `short sell` 0, `participation` 0, `ADV` 0, `turnover` 0, `capacity` 0, `market impact` 0, `marketimpact` 0, `drawdown` 0, `rebalanc` 1 (Literature Review only), `holding period` 0, `latency` 0, `fill` 0, `leverag` 2 (abstract verb "leverage the CRSP dataset" and a Literature Review sentence), `risk-free` 1 (French data-library download). → **No fee, spread, slippage, borrow, impact, fill, latency, participation, capacity, turnover, drawdown or P&L-cost model exists anywhere in the source; every one of those fields is `data gap` / `underspecified`, never zero.** Because the strategy is long-only, borrow is structurally less relevant, but that does not licence assuming zero cost.
- **Repo-wide source-identity dedup (performed 2026-09-25 before writing, `rg --hidden` over ALL `*.md` including `.mimo-worktrees/`, `.agents/`, `.hermes/` — 2,526 files — plus `coverage_manifest.csv`, 5,808 lines):** patterns `2409.14510`, `10.48550/arXiv.2409.14510`, `Crisis Alpha: A High-Performance Trading Algorithm`, `Khodayari`, `Gharanchaei`, `Babazadeh`, `Crisis Alpha` → **zero hits in every existing record and in the manifest.** Family-neighbour screen: `maximum diversification` matched only `observable-matrix-dynamics-portfolio-optimization-2026-09-02.md`; `risk parity` matched 85 files but only as a benchmark/loss-name mention; `covariance shrinkage` / `minimum variance portfolio` matched the GNN-minimum-variance record, the two-stage adaptive-shrinkage record, the AttentionLSTM omega-CVaR-risk-parity record, the Special-Markowitz record and the neural-shrinkage record — all inspected as **different source identities and different mechanisms**.
- **Four-axis distinction from nearest in-repo captures** (different source identity in every case): `graph-neural-network-volatility-minimum-variance-portfolio-2026-09-03.md` (macro-conditioned GNN *volatility forecasting* feeding a minimum-variance portfolio → signal is a learned forecast; here the covariance estimator *is* the whole signal and no forecast enters); `deep-portfolio-optimization-attention-lstm-omega-cvar-risk-parity-2026-09-03.md` (end-to-end learned allocation with a differentiable omega-CVaR-risk-parity objective → learned weights, tail-loss objective; here weights come from three classical convex programs with no learning); `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md` (shrinkage applied to *predictive regressions for equity premium* → different object of shrinkage and different horizon); `special-markowitz-thermodynamic-joint-regularisation-returns-covariance-2026-09-17.md` (thermodynamic joint regularisation of returns and covariance → different estimator and no crisis-episode panel); `observable-matrix-dynamics-portfolio-optimization-2026-09-02.md` (observable-matrix dynamics + ranking forecasts → different signal construction). Mechanism (statistical-risk-model portfolio construction vs forecast-driven or learned allocation), signal construction (three covariance estimators × three convex programs vs learned/forecast inputs), universe (1,000 largest US stocks vs S&P 500 / crypto / cross-asset), horizon/regime (four named crisis-era sub-samples 1990-2023 vs single windows), and data dependency (CRSP monthly + French library, no alternative data) all differ.
- **Schema provenance:** structure and frontmatter follow the canonical Wiki Brain contract resolved this run — `kb_read` `quant/strategy-research-record-spec-v1.md` (10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`); `kb_read` v2 → file not found → **v1 remains canonical**. `README.md` (575 lines) re-read this run.
- **Primary-source coverage:** `git pull origin main` → `Already up to date` (HEAD `8fc2a17` before this run); `git log --oneline -20` used only as a convenience glance; the dedup decision rests on the repo-wide search above.

## Economic mechanism

### Source-reported

The source frames the exercise as *crisis-period* portfolio construction: statistical risk models are re-estimated from monthly data and fed to convex optimizers that produce long-only, fully-invested weights, and the resulting portfolios are compared with value-weighted and equal-weighted benchmarks over four named eras (Dot-Com Bubble, GFC, COVID-19, Post-COVID) covering January 1990 - December 2023. The three risk models are (Section 3):

1. **Single-factor (market-factor) covariance** `V = σ_f² · b bᵀ + D` with a shrinkage adjustment of the loadings `βᵢ := (2/3)β̂ᵢ + 1/3` and of the log idiosyncratic variances `log ωᵢ := (2/3) log ω̂ᵢ + (1/3N) Σⱼ log ω̂ⱼ` (formulas (1)-(3)).
2. **Constant-correlation covariance** `V = ρ · σσᵀ + (1-ρ) Diag(σ)²` with `ρ` = the average of all sample correlations and log-volatilities shrunk one third toward their average (formula (4)).
3. **Sample covariance with shrinkage toward a structured target**, explicitly "the same method as Clarke et al. (2006)", run over the US equity market.

The three optimizers (Section 3, solved with CVXPY and **GUROBI**) are: **minimum variance** `min xᵀ V x s.t. 1ᵀx = 1, 0 ≤ x ≤ u` with the upper band **u = 5% for all assets**; **maximum diversification** written through `Kx = z` as `min zᵀ V z s.t. σᵀ z = 1, 1ᵀ z = K, z ≤ Ku, z ≥ 0`; and **risk parity** `min ½ yᵀ V y − Σ log(yᵢ)` with `y ≥ 0`, `y ≤ d`, mapped back as `x = y / 1ᵀy`. Effective breadth is reported with the Strongin et al. (2000) "effective number of stocks".

The source's stated economic story (Section 4 prose) is that maximum diversification "could catch idiosyncratic alphas" when cross-sectional correlations move together, minimum variance reduces market sensitivity (betas printed as low as 0.00-0.08), and risk parity behaves like an equal-weighted book "with better risk control". No formal alpha attribution, no factor regression of the strategy residuals, and no risk-budgeting decomposition is performed.

### Research interpretation

The falsifiable hypothesis this record normalizes is **not** the paper's marketing title; it is:

> *A re-estimated (rolling 60-month) statistical risk model, combined with a long-only convex allocation subject to a 5% name cap, produces a persistent risk-adjusted difference against a value-weighted top-1,000 benchmark that survives across crisis and non-crisis regimes — i.e. the covariance estimator, not a return forecast, is the operative signal.*

Mechanism candidates that must be separated before any adoption: (a) **estimation-shrinkage effect** — shrunk/structured covariance reduces weight dispersion and estimation error; (b) **breadth/concentration effect** — the minimum-variance and maximum-diversification columns hold 20-230 names against the benchmark's 1,000, so their printed excess returns embed a very different breadth; (c) **beta effect** — the constant-correlation maximum-diversification column prints market betas of 1.73-2.65, so part of its excess-return advantage may be uncompensated market exposure rather than alpha; (d) **constraint effect** — under the constant-correlation estimator the 5% band binds (our count: average positions 20.0-20.3 = 1/0.05, effective N 20.0-20.1), i.e. the optimizer is pinned at the cap and the "strategy" degenerates into an equal-weighted 20-name portfolio. Ablation of (a)-(d) is a precondition for treating any part of the printed gap as mechanism. **No component of the mechanism is demonstrated by the source; the source itself concludes that "no single strategy consistently outperforms across all conditions".**

## Signal

**Fully specified by the source (source-reported):**

- **Estimation input:** monthly time series of the **past 60 monthly excess returns and market excess returns** used to estimate the covariance matrix and the optimal holdings (Section 3). Market returns and risk-free returns come from **Kenneth French's data library**; stock returns are **CRSP adjusted returns "to neutralize dividend effects"**.
- **Universe:** "the 1000 largest stocks of US markets" / "1,000 floating stocks in the US market" (Section 3 and Abstract). **The ranking variable (market cap, price, volume, other), the exchange/ share-code filters, and the point-in-time construction rule are never stated → `data gap`.**
- **Lookback:** 60 monthly observations, endpoints inclusive as implied by "the past 60 monthly excess returns"; warm-up, missing-month handling and any minimum-history screen are **not stated → `data gap`**.
- **Weights:** output of one of the three convex programs above, long-only, fully invested, 5% per-name upper band (for minimum variance and maximum diversification as written; risk parity carries its own upper bound `d`, value not stated → `underspecified`).
- **Benchmarks printed in every table:** `Market (Value-Weighted)` and `Equal Weighted`, both printed with 1,000 average positions; the source calls the value-weighted column "the indicator of market excess return" — the exact construction of that benchmark column is **not further specified → `data gap`**.

**Not specified by the source (therefore `underspecified`, and anything operational below is `research-proposed`):**

- **Formation timestamp / availability convention:** none. The text never states when weights become tradable, whether month-t covariance uses month-t returns, or whether returns are measured over the same month as the weights → **no explicit anti-look-ahead lag exists in the source** (word scan: `lag` 0, `next month` 0, `formation` appears only in prose about factor formation elsewhere, `executed` 0, `traded at` 0, `close price` 0).
- **Rebalance / holding cadence:** never stated (word scan `rebalanc` 1 hit, inside the Literature Review about *another* paper; `holding period` 0). Section 3 says monthly data were "utilized to estimate the covariance matrix and optimal holdings for each scenario", which *implies* monthly re-optimization but does not state it → recorded as source-implied, not source-stated.
- **Entry / exit:** there is no entry or exit rule in the ordinary sense — the source reports **static end-of-era panel statistics** (average excess return, standard deviation, Sharpe, beta, average positions, effective N) per period, not a trade-by-trade rule. Position-level entry, exit, tie-handling between simultaneous signals and any de-listing rule are absent.
- **Parameters and their provenance:** 60-month window (fixed, source), 5% cap (fixed, source), one-third shrinkage constants in formulas (2)-(3) and in the constant-correlation vol shrinkage (fixed, source), `ρ` = average sample correlation (source), Clarke et al. (2006) target for model 3 (source), GUROBI solver (source). No tuning protocol, no search grid, no selection criterion is reported (`train` 0, `test set` 0, `out-of-sample` 3 hits but only as the label "out-of-sample tests" with no separation protocol).
- **Research-proposed operationalization (NOT source-reported, provided only so an independent researcher has something executable):** rebalance monthly at the next month's close using month t-1 data for month t weights; rank the universe by month t-1 market capitalization; drop names with fewer than 60 valid months; treat the benchmark as the value-weighted return of the same 1,000 names. Every clause in this paragraph is `research-proposed`.

## Required data

- **Instrument / universe:** US common equities (CRSP). The source does not state share codes, exchanges or listing screens → `data gap`. "1,000 largest" implies a size ranking whose variable is unstated → `data gap`. Survivorship handling: **not mentioned anywhere** (word scan `survivorship` 0, `point-in-time` 0, `universe` 0) → `data gap`.
- **Venue / market type:** US stock market, cash equities, long-only. No futures, options, derivatives, shorting or leverage (word scan `short sell` 0; `leverage` hits are unrelated to the strategy).
- **Timeframe:** monthly bars, 60-month estimation window; results reported per era.
- **Fields:** adjusted total returns (dividends neutralized), market excess return, risk-free rate (French MKT/RF), per-stock volatilities and correlations (or betas and idiosyncratic vols), and a size ranking field (unstated).
- **Point-in-time / availability:** no publication timestamps involved (prices only), but the point-in-time *composition* of the 1,000-name panel is unspecified → `data gap`.
- **Timestamp / timezone:** not stated; monthly CRSP convention assumed by the data vendor, not declared by the source → `underspecified`.
- **Missing data:** imputation, suspension and de-listing treatment are **not stated → `data gap`** (the source only says the stocks are "floating", a term it never defines).
- **Costs/fees/spread/borrow needs:** none observed, none modeled, none reported — see Execution assumptions; **every cost field is `data gap`, never zero.**

## Execution assumptions

All of the following were determined from Section 3 (Proposed Methodology), Section 4 setup and the full-text scan of the pinned PDF — **not** from the abstract:

- **Signal-to-order timing:** `not stated in source` (no lag, no execution convention).
- **Rebalance cadence:** `data gap` (monthly estimation is source-implied only).
- **Order type / fill model / latency / partial fills:** `not stated in source` (word scan `fill` 0, `latency` 0).
- **Fees / commission / spread / slippage / market impact:** `not stated in source` (`commissi` 0, `fee` 0, `slippage` 0, `bid-ask` 0, market-impact 0) → **all 12 panels are gross of cost by construction.**
- **Turnover / capacity / participation:** `not stated in source` (`turnover` 0, `capacity` 0, `participation` 0, `ADV` 0); position counts are printed (average positions 20.0-229.7 for the optimized columns) but no trade counts are → capacity is `data gap`.
- **Leverage / margin:** long-only, fully invested (`1ᵀx = 1`, `x ≥ 0`) → no leverage assumed by the source; no margin model → `data gap`.
- **Borrow / shorting:** not applicable to the printed strategies (long-only); the source never discusses borrow → `data gap` rather than "free".
- **Funding / dividend:** returns are dividend-adjusted ("adjusted returns to neutralize dividend effects"); whether the excess returns are over the French risk-free rate is implied by "market returns and risk-free returns were downloaded from Kenneth French's data library" → source-implied, exact pairing `underspecified`.
- **Diversification/weight constraints:** 5% per-name band (source); risk-parity upper bound `d` numeric value not stated → `underspecified`.
- **Failure handling:** the source reports that under the shrinkage estimator the risk-parity program is numerically non-PSD and **produced NaN in all four eras**, and recommends "employing other diversification strategies along with this risk model" → the failure is disclosed, not repaired.
- **Scout vs source:** no Scout execution assumption is used anywhere in the Evidence section; every operational rule added by the Scout is labelled `research-proposed` (Signal section) or `research-defined` (Falsification plan).

## Evidence

### Source-reported

All figures below are **third-party, source-reported, gross of any transaction cost**, read from the pinned `arXiv:2409.14510v1` PDF and anchored to the printed table. Rows are `Average Excess Return / Standard Deviation / Sharpe / Market Beta / Average Positions / Effective N`; columns are `Market (VW), Equal Weighted, Minimum Variance, Maximum Diversification, Risk Parity`.

**Table 1(a) Market-factor model — Dot-Com Bubble (01/1990-03/2000):** Market 17.09% / 13.41% / 1.27 / 1.00 / 1000.0 / 190.2; EW 14.13% / 14.07% / 1.00 / 0.99 / 1000.0 / 1000.0; MinVar 2.04% / 8.85% / 0.23 / 0.06 / 68.7 / 38.8; MaxDiv 35.32% / 19.96% / 1.77 / 0.48 / 65.1 / 39.1; RiskParity 11.03% / 11.97% / 0.92 / 0.82 / 1000.0 / 866.4.
**Table 1(b) Constant-correlation — Dot-Com:** MinVar −0.02% / 7.53% / 0.00 / 0.33 / 21.6 / 20.6; MaxDiv 80.83% / 52.27% / 1.55 / 2.11 / 20.0 / 20.0; RiskParity 13.07% / 13.66% / 0.96 / 0.98 / 1000.0 / 994.1 (benchmark columns identical to 1(a)).
**Table 1(c) Shrinkage — Dot-Com:** MinVar 2.76% / 4.96% / 0.56 / 0.28 / 171.3 / 99.0; MaxDiv 35.90% / 19.02% / 1.89 / 1.09 / 45.3 / 29.1; RiskParity **NaN**.

**Table 2(a) Market-factor — GFC era (03/2000-09/2008):** Market 7.43% / 13.31% / 0.56 / 1.00 / 1000.0 / 161.0; EW 12.78% / 14.22% / 0.90 / 1.01 / 1000.0 / 1000.0; MinVar 10.37% / 8.73% / 1.19 / 0.05 / 87.2 / 52.7; MaxDiv 26.35% / 16.43% / 1.60 / 0.05 / 94.8 / 54.4; RiskParity 12.24% / 10.91% / 1.12 / 0.71 / 1000.0 / 761.3.
**Table 2(b) Constant-correlation — GFC:** MinVar 4.37% / 8.29% / 0.53 / 0.32 / 21.5 / 20.5; MaxDiv 47.63% / 59.99% / 0.79 / 2.65 / 20.0 / 20.0; RiskParity 12.29% / 13.75% / 0.89 / 0.98 / 1000.0 / 994.1. Source prose on this panel: "An exceptional return of almost 48% during the GFC", with portfolio risk "much higher than other approaches".
**Table 2(c) Shrinkage — GFC:** MinVar 4.30% / 4.34% / 0.99 / 0.25 / 146.4 / 83.0; MaxDiv 20.67% / 11.47% / 1.80 / 0.70 / 54.2 / 33.7; RiskParity **NaN**.

**Table 3(a) Market-factor — COVID era (09/2008-04/2020):** Market 11.60% / 15.28% / 0.76 / 1.00 / 1000.0 / 205.7; EW 11.14% / 17.31% / 0.64 / 1.11 / 1000.0 / 1000.0; MinVar 4.66% / 4.80% / 0.97 / 0.00 / 39.4 / 25.6; MaxDiv 22.63% / 16.64% / 1.36 / 0.31 / 51.7 / 33.5; RiskParity 10.59% / 14.01% / 0.76 / 0.90 / 1000.0 / 831.1.
**Table 3(b) Constant-correlation — COVID:** MinVar 1.61% / 5.46% / 0.29 / 0.18 / 21.0 / 20.4; MaxDiv 51.26% / 42.12% / 1.22 / 2.13 / 20.1 / 20.0; RiskParity 10.52% / 16.65% / 0.63 / 1.07 / 1000.0 / 989.8.
**Table 3(c) Shrinkage — COVID:** MinVar 3.71% / 3.97% / 0.93 / 0.21 / 111.9 / 54.6; MaxDiv 25.73% / 18.68% / 1.38 / 0.98 / 39.97 / 27.86; RiskParity **NaN**.

**Table 4(a) Market-factor — Post-COVID (04/2020-12/2023):** Market 18.50% / 19.69% / 0.94 / 1.00 / 1000.0 / 113.8; EW 15.17% / 20.88% / 0.73 / 1.02 / 1000.0 / 1000.0; MinVar **−3.98%** / 3.23% / **−1.23** / 0.07 / 26.0 / 21.8; MaxDiv 49.26% / 50.36% / 0.98 / 0.60 / 38.3 / 27.2; RiskParity 12.25% / 17.53% / 0.70 / 0.86 / 1000.0 / 842.7.
**Table 4(b) Constant-correlation — Post-COVID:** MinVar **−3.38%** / 2.72% / **−1.49** (printed) / 0.08 / 21.3 / 20.5; MaxDiv 88.39% / 63.64% / 1.39 / 1.73 / 20.3 / 20.1; RiskParity 13.66% / 20.08% / 0.68 / 0.99 / 1000.0 / 986.4.
**Table 4(c) Shrinkage — Post-COVID:** MinVar 0.06% / 5.67% / 0.01 / 0.23 / 229.7 / 121.0; MaxDiv 53.00% / 48.37% / 1.10 / 0.92 / 37.1 / 25.7; RiskParity **NaN**.

**Source-stated conclusions (Section 5):** "no single strategy consistently outperforms across all conditions"; maximum diversification "often delivers high returns during market upswings but comes with significant risk"; minimum variance "proves more effective for risk-averse investors, particularly during uncertain or declining market conditions"; risk parity under the shrunk covariance model is left as future work.

**Our own arithmetic on printed cells — labelled `our count`, a consistency audit of the printed table, NOT a rerun of the backtest (2026-09-25):**
- **Panel count:** 4 eras × 3 risk models = **12 panels**; 5 strategy columns each = **60 cells**, of which **4 are printed NaN** (Risk Parity under shrinkage in every era) → **56 populated cells**.
- **Sharpe consistency:** in **55 of 56** populated cells the printed Sharpe equals printed average excess return ÷ printed standard deviation to within 0.011 (e.g. 17.09/13.41 = 1.274 → 1.27; 35.32/19.96 = 1.770 → 1.77; 88.39/63.64 = 1.389 → 1.39; −3.98/3.23 = −1.232 → −1.23). **The single exception is Table 4(b) Minimum Variance: −3.38/2.72 = −1.24 against a printed −1.49.** The consistency of the other 55 cells is also why the return/vol figures appear to be on one common (annualized) scale — **but the source never says "annualized" (0 hits) or states any compounding/period convention → that reading is `data gap`, not source-stated.**
- **Benchmark dominance counts:** Maximum Diversification prints a higher average excess return than the value-weighted benchmark in **12 of 12** panels and a higher Sharpe in **12 of 12**. Minimum Variance prints a *lower* average excess return than the benchmark in **11 of 12** panels and a higher Sharpe in only **4 of 12**. Risk Parity prints a higher Sharpe than the benchmark in **2 of 12**, equal in **1**, lower in **5**, NaN in **4**.
- **Cap-binding check:** under the constant-correlation estimator the Maximum Diversification column prints average positions of **20.0, 20.0, 20.1, 20.3** with effective N of **20.0, 20.0, 20.0, 20.1**, while `1/0.05 = 20.0` — i.e. the 5% band binds in **all four eras** and the effective breadth equals the headcount, consistent with an equal-weighted 20-name book. Its market betas in those four panels are **2.11, 2.65, 2.13, 1.73**, all above 1.6.
- **Period-boundary overlap:** the four era windows are printed as 01/1990-03/2000, 03/2000-09/2008, 09/2008-04/2020, 04/2020-12/2023, so **each boundary month (Mar 2000, Sep 2008, Apr 2020) is inside two adjacent windows** — the era panels are not a strict partition of 1990-2023 (our count of inclusive months: 123 + 103 + 140 + 45 = **411** against the **408** months of Jan 1990-Dec 2023, i.e. exactly three duplicated boundary months).
- **Benchmark columns:** the Market and Equal-Weighted rows are numerically identical across the three risk models within each era (they do not depend on the estimator), as expected.

**Not reproduced by the source:** no confidence interval, t-statistic, p-value, HAC/Newey-West standard error, bootstrap, block bootstrap or multiple-testing adjustment is printed anywhere (word scan: `t-stat` 0, `p-value` 0, `confidence interval` 0, `bootstrap` 0, `Newey` 0, `robust standard` 0); the 24 `significan*` hits are prose about betas and about *other* papers. **No drawdown, VaR, CVaR or tail metric is printed** (`drawdown` 0) despite the paper's risk-management framing.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Zero cost, fill, borrow, turnover, capacity, drawdown or P&L-cost model anywhere in the pinned text** (Methods-level read of Section 3 + word scan) → every printed number is gross; missing items are `data gap`, never zero.
2. **Zero statistical inference:** no standard errors, t-stats, p-values, confidence intervals, HAC, bootstrap or multiplicity control over a 60-cell grid → the word "significant" is used rhetorically only.
3. **The headline claim is contradicted by the source's own tables and conclusion** (frontmatter contradiction 1): minimum variance trails the benchmark in 11/12 panels and is negative in both post-COVID market-factor and constant-correlation panels (−3.98%, −3.38%).
4. **Source-internal strategy-count contradiction** (frontmatter contradiction 2): "five" in the abstract vs "four" in Section 3 vs five printed columns.
5. **Source-internal risk-parity contradiction** (frontmatter contradiction 3): prose excludes risk parity from the post-COVID era while Tables 4(a)/4(b) print it.
6. **Source-internal numeric inconsistency** (frontmatter contradiction 4): Table 4(b) minimum-variance Sharpe printed −1.49 vs −1.24 implied by its own printed mean and standard deviation.
7. **The best-looking column's advantage coincides with a binding constraint and with beta > 1.6** (our count): under the constant-correlation estimator the 5% band binds in all four eras and effective N equals headcount, so the "maximum diversification" result is a 20-name equal-weight book with beta 1.73-2.65 — the source attributes this to "idiosyncratic alphas" without running any alpha attribution, factor regression of residuals, or beta-matched comparison.
8. **No execution/timing layer at all:** no rebalance cadence, no formation timestamp, no signal-to-execution lag, no fill price convention (`lag` 0, `rebalanc` 0 in the source's own methods, `executed` 0, `close price` 0) → a look-ahead window between covariance estimation and realized returns cannot be ruled out from the text.
9. **Universe construction undocumented:** "1,000 largest" with no ranking variable, no share-code/exchange screen, no point-in-time rule and no survivorship treatment (`survivorship` 0, `point-in-time` 0, `universe` 0) → selection and survivorship bias are unaddressed and unquantified.
10. **No train/test, walk-forward or parameter-selection protocol:** the four era windows are contiguous slices of one 1990-2023 sample with shared boundary months, chosen after the fact; the 60-month window and the 5% cap are never perturbed (`train` 0, `test set` 0).
11. **The 60-month covariance window cannot span most of the crises it is judged on:** e.g. the post-COVID window spans only **45 months** (04/2020-12/2023, our count) while estimation requires 60 months — the source never reconciles estimation-window availability with era length → `underspecified`.
12. **Risk parity is numerically broken under the shrinkage model in 4 of 4 eras (NaN)** and the source defers the fix to "a separate study" — a whole model×strategy cell of the advertised grid is missing.
13. **Model × strategy instability is large:** e.g. minimum-variance Sharpe swings from 1.19 (market-factor, GFC) to 0.53 (constant-correlation, GFC) to 0.99 (shrinkage, GFC) within the *same* era; maximum-diversification average excess return swings from 26.35% to 47.63% to 20.67% in the same era — no robustness rule is offered.
14. **Source-quality flags:** preprint only (no Comments, no Journal-ref, no publisher DOI, no peer-review statement), no data/code availability statement, no declarations, no generative-AI statement; and the Literature Review cites unrelated medical-imaging papers as evidence for "AI-equipped algorithms" (References: Ajami 2024, *Disentangled Representation Learning vs. ResNet 18 for White Matter Lesion Detection in Multiple Sclerosis*; Ajami, Nigjeh & Umbaugh 2023, white-matter lesion MRI segmentation; Nigjeh, Ajami & Umbaugh 2023) — a visible reference-hygiene red flag.
15. **No drawdown / risk-of-ruin evidence despite the framing:** the title promises a "high-performance trading algorithm tested in market downturns", yet no drawdown, tail-loss, or crisis-dummy statistic is reported; the only risk metrics are standard deviation and beta.
16. **No capacity or liquidity analysis** (`capacity` 0, `liquidity` 3 hits all in prose/References) for portfolios holding as few as 20 names out of a 1,000-name panel.
17. **License constraint:** arXiv non-exclusive distribution licence (not CC) → the source text cannot be redistributed here, only cited and normalized.

## Falsification plan

Every threshold below is a `research-defined` acceptance/failure threshold chosen by the Scout; every operational rule is `research-proposed`. None of it is source-reported. Data assumed: CRSP monthly (or an equivalent survivorship-free point-in-time panel) plus French MKT/RF.

- **F1 — Point-in-time universe repair (leakage audit).** Rebuild the panel as "top 1,000 by month t-1 market capitalization among NYSE/AMEX/Nasdaq share codes 10/11 with ≥60 valid months", weights formed on months ≤ t-1 and applied to month t. **Failure rule:** if the Maximum-Diversification Sharpe advantage over the value-weighted benchmark falls below half of the printed 12-panel mean advantage, the source's result is treated as selection/look-ahead driven; action = reject mechanism claim.
- **F2 — Cost ladder.** First measure one-way turnover of each column (unreported by the source), then charge 0/5/10/20/30 bp per side plus 50 bp/year on any short-balance proxy. **Failure rule:** if the net Sharpe advantage of Maximum Diversification over the benchmark drops below +0.20 at 10 bp, or the sign flips at any rung, the effect is declared cost-fragile; action = stop.
- **F3 — Beta/leverage decomposition.** Regress each optimized column's excess return on the market factor and compare alpha (not gross excess) against the benchmark, with Newey-West errors at lag 12. **Failure rule:** if the beta-adjusted alpha advantage is ≤ 0 in at least 8 of the 12 panels, the printed advantage is reclassified as beta exposure, not alpha; action = reclassify mechanism.
- **F4 — Cap ablation (mechanism test for the binding constraint).** Re-run with the name cap at 2.5%, 5%, 10% and uncapped. **Failure rule:** if the cross-model ranking of columns flips in ≥ 6 of 12 panels, the "maximum diversification" result is a constraint artefact; action = drop the strategy claim.
- **F5 — Covariance-estimator robustness.** Add Ledoit-Wolf and a rolling exponentially-weighted estimator alongside the three printed estimators. **Failure rule:** if the Sign of the era-level Sharpe advantage changes for any estimator swap in ≥ 4 of 12 panels, the risk-model dependence is declared unstable; action = reframe as estimator-specific.
- **F6 — Statistical inference with multiplicity control.** Compute NW t-statistics for the 56 populated cells and apply Benjamini-Hochberg at q < 0.10 across the grid. **Failure rule:** if fewer than half of the printed Sharpe advantages survive, all "outperformance" language is withdrawn; action = reject.
- **F7 — Placebo breadth test.** Simulate 1,000 random long-only portfolios matched on name count and beta to each optimized column (same era, same rebalance rule). **Failure rule:** if the observed Maximum-Diversification Sharpe lies inside the placebo 95% band in ≥ 6 of 12 panels, no alpha claim survives; action = reject.
- **F8 — Crisis vs non-crisis split with a pre-declared calendar.** Fix the crisis calendar before looking at results (NBER US recessions, or a −20% drawdown rule on the benchmark applied point-in-time). **Failure rule:** if the crisis-period Sharpe advantage is ≤ 0, the "crisis alpha" framing fails regardless of any other result; action = rename/reject.
- **F9 — Rebalance-cadence and lag sensitivity.** Compare monthly next-close execution against quarterly and against a one-month-delayed weight application. **Failure rule:** if the sign of the era-level advantage flips under a one-month delay, the source result is deemed leak-sensitive; action = reject pending a leakage audit.
- **F10 — Second-vendor transport.** Rebuild the panel from an independent vendor (e.g. Compustat/WRDS or an exchange-official tape) with the identical rule. **Failure rule:** if fewer than half of the 12 panels reproduce within ±0.20 Sharpe of the printed values, treat the printed grid as unreproducible; action = archive as unverified.
- **F11 — Forward window (post-publication).** Extend 2024-01 to the present with the rule frozen. **Failure rule:** if the Maximum-Diversification Sharpe advantage is non-positive in ≥ 2 consecutive forward years, the historical result is declared regime-bound; action = demote to historical-only evidence.

## Crypto portability

**unproven.**

- The source contains **no crypto evidence of any kind** — US cash equities only, CRSP + French factors, four crisis eras ending December 2023.
- **Universe:** "1,000 largest US stocks" has no clean crypto analogue: top-N-by-market-cap tables are vendor- and venue-specific, restated continuously, and full of survivorship/ delisting and stablecoin ranking artefacts; no point-in-time top-1,000 crypto panel with CRSP-like restatement exists in the source's sense.
- **Market structure:** crypto trades 24/7, so "monthly era windows" and any session-based return convention have no counterpart; candle boundaries, index/last-price definitions and venue fragmentation would each need their own rule (`research-proposed`).
- **Instrument:** the printed strategies are long-only cash equity weights. A crypto port would need spot vs perpetual distinctions, funding on any perp exposure, mark/index price choice, venue-level liquidity, and leverage/margin rules — **none of which appear in the source's cost model** (which is itself empty).
- **Risk model:** a 60-month covariance window spans five crypto years, a regime length the source never studies; correlations among crypto names are dominated by a single common factor, which changes the geometry of both the minimum-variance and the constant-correlation estimators.
- **Risk-free / excess-return convention:** the source uses the French risk-free rate; the crypto analogue (stablecoin yield, funding rate, or zero) would change every "excess return" figure and is `research-proposed` at best.
- Therefore any crypto version is a **ported hypothesis with no empirical support from this source**, not `adapted` evidence and certainly not `direct`.

## Limitations

- **underspecified:** rebalance cadence, formation/execution timing, benchmark construction, ranking variable for "1,000 largest", risk-parity upper bound `d`, annualization/compounding convention, dividend-vs-excess pairing.
- **data gap:** all cost/fill/latency/turnover/capacity/drawdown lines; survivorship and point-in-time construction; missing-data handling; code, data-availability, funding, conflict and AI statements; any statistical inference.
- **not independently reproduced:** every number in Evidence/Source-reported; this record is a normalization of a third-party preprint, not a verification of it.
- **unproven:** the existence of any tradable edge — the source is a static era-panel comparison of portfolio statistics, not a strategy specification with a testable execution rule.
- **Source-quality:** preprint-only, no peer review, no replication package, visibly unrelated references in the Literature Review, and four source-internal contradictions (frontmatter).
- **Publication-bias / framing:** the title and abstract assert consistent outperformance that the tables and the conclusion do not support; readers of the abstract alone would overstate the evidence.
- **Capacity:** nothing is known about how the 20-name concentrated portfolios would trade at size; no liquidity, participation or impact analysis exists.
- **Regime:** four hand-chosen era windows with shared boundary months; no crisis calendar is pre-declared and the post-COVID window is shorter than the 60-month estimation window.
- **Incremental-write check:** no existing record in this repository shares this source identity; the nearest in-repo captures were inspected and are mechanism-distinct (see Provenance four-axis list).

## Implementation status

`implementation_status: not-implemented`.

Nothing from this record has been implemented in our research stack: no portfolio constructor, no covariance estimator, no optimizer, no Qlib backtest, no Paper/Testnet/Live run, and no candidate-pool entry. The only work performed in this run was source verification (full-text read of the pinned v1 PDF), repo-wide dedup, and normalization of the source's reported design and numbers. The `research-proposed` operationalization in the Signal section and the `research-defined` thresholds in the Falsification plan exist solely to give a future reviewer something executable; they are not evidence and not authorization.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Adoption or implementation would require an explicit, separately reviewed decision based on this record plus current sources — and, on the present evidence, would additionally require clearing F1-F11 above, since the source itself reports no cost model, no inference, and no consistent outperformance.

## Related Wiki records

Read-only search this run (`kb_search`); only pages actually returned by the vault are linked, no page was fabricated, and **no Wiki Brain write was performed**:

- Query `risk parity minimum variance covariance shrinkage portfolio construction equity` → 2 results.
- Query `maximum diversification portfolio crisis drawdown equity allocation regime` → 8 results.

Linked as mechanism-adjacent (portfolio construction / crisis-conditional allocation, different sources):

- [[quant/smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05]] — decision-focused allocation *with explicit turnover costs*, the cost discipline this source lacks.
- [[quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]] — defensive/crisis-conditional allocation with walk-forward evidence, contrasted here against this source's hand-picked era windows.

No record for this source identity exists in Wiki Brain search results; if this artifact later passes intake, the ingestion decision belongs to ChatGPT Research Intake Review, not to this Scout.

## Sources

- Maysam Khodayari Gharanchaei, Reza Babazadeh, *"Crisis Alpha: A High-Performance Trading Algorithm Tested in Market Downturns"*, arXiv:2409.14510v1 [q-fin.PM], submitted 2024-08-18T19:35:07Z (sole version). Landing page: https://arxiv.org/abs/2409.14510 (checked 2026-09-25: no Comments, no Journal-ref, no publisher DOI, no peer-review statement; arXiv non-exclusive distribution licence).
- Pinned primary full text read for this record: https://arxiv.org/pdf/2409.14510v1 (downloaded 2026-09-25, 1,934,423 bytes, 31 pages, 60,373 extracted characters; all 12 result tables and Sections 1-5 plus References read). All quantitative claims in Evidence/Source-reported trace to Tables 1(a)-4(c) of that PDF; the abstract is never used as a number source.
- Canonical identifier DOI: https://doi.org/10.48550/arXiv.2409.14510 (HTTP 302 → abs page, verified 2026-09-25).
- Data inputs named by the source (not fetched by this Scout): CRSP monthly equity data; Kenneth French data library (market and risk-free returns); CVXPY with the GUROBI solver; Clarke et al. (2006) shrinkage target; Strongin et al. (2000) effective-number-of-stocks definition.
- Related in-repo records were identified through repo-wide `rg --hidden` dedup (2,526 `*.md` files plus `coverage_manifest.csv`, 5,808 lines, 2026-09-25); no other source was used to fill any field of this record.
