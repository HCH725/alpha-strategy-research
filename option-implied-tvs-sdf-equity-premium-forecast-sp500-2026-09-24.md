---
schema: strategy-research-record-v1
title: Option-Implied Time-Varying-Volatility-Scaled SDF Equity-Premium Forecast (S&P 500 Index Options)
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - options
  - equity-premium
  - stochastic-discount-factor
  - option-implied
  - market-timing
status: research-only
confidence: medium
source_as_of: 2026-07-23
sources:
  - "Kenichiro Shiraya, Tomohisa Yamakami, Akira Yamazaki, 'Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium', arXiv:2607.08500v2 [q-fin.MF; q-fin.ST], v2 submitted Thu 23 Jul 2026 13:13:08 UTC. https://arxiv.org/abs/2607.08500"
  - "https://arxiv.org/html/2607.08500v2 (v2 HTML full text, 784,388 bytes, opened and read directly for this record on 2026-09-24)"
  - "https://doi.org/10.48550/arXiv.2607.08500 (DataCite/arXiv DOI; resolves 302 -> 200 https://arxiv.org/abs/2607.08500, checked 2026-09-24)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal: Table 5/6 aggregation-window definitions printed twice in v2 ('Full' is from Dec 18, 2009 to data end where data end corresponds to maturity Feb 28, 2023; '1st/2' is from Dec 18, 2009 to Dec 17, 2015; '2nd/2' is from Dec 18, 2015 to Dec 15, 2017) are internally inconsistent: the two labelled halves end in 2017 and therefore cannot partition the Full window that runs to the 2023 data end. No reconciliation of the '2nd/2' end date appears anywhere in v2."
---

# Option-Implied Time-Varying-Volatility-Scaled SDF Equity-Premium Forecast (S&P 500 Index Options)

## Provenance

- **Primary source:** Kenichiro Shiraya, Tomohisa Yamakami, Akira Yamazaki, *"Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium"*, **arXiv:2607.08500v2 [q-fin.MF]**, v2 submitted **Thu 23 Jul 2026 13:13:08 UTC** (758 KB, submitter Tomohisa Yamakami); v1 Thu 9 Jul 2026 13:59:19 UTC (757 KB). Submission history shows exactly `[v1]` and `[v2]`; `arxiv.org/html/2607.08500v3` returns 404, so **v2 is the pinned current version**. The v2 HTML header prints `arXiv:2607.08500v2 [q-fin.MF] 23 Jul 2026`.
- **Authors and affiliations exactly as printed on the v2 title block:** Kenichiro Shiraya† — Graduate School of Economics, The University of Tokyo; Tomohisa Yamakami† — Graduate School of Economics, The University of Tokyo **and** Mizuho-DL Financial Technology Co., Ltd.; Akira Yamazaki† — Graduate School of Business Administration, Hosei University. The dagger (`†`) symbol appears on all three names and **its footnote meaning is never defined in v2** → `data gap`. Title block also carries the disclaimer "The opinions expressed herein are only those of the authors and do not represent the official views of the company." and the acknowledgment "Supported by Center for Advanced Research in Finance (CARF) at the University of Tokyo."
- **Date-line note:** the v2 title block renders an in-document date line of **"August 24, 2026"**, which postdates the 23 Jul 2026 v2 submission stamp; the authoritative version date is the arXiv submission history (rendering artifact, recorded for transparency).
- **Publication status:** Comments field = "32 page, 4 figures"; **no Journal-ref, no DOI field other than the arXiv/DataCite DOI** → **preprint only**, peer-review status `not stated in source`. Subjects: **Mathematical Finance (q-fin.MF)**; Statistical Finance (q-fin.ST). License on the abs page: **arXiv.org perpetual non-exclusive distribution license** (`licenses/nonexclusive-distrib/1.0/`). DOI `10.48550/arXiv.2607.08500` resolves (302 → 200) on 2026-09-24.
- **Full text actually read:** `https://arxiv.org/html/2607.08500v2`, 784,388 bytes fetched 2026-09-24; §1 Introduction, §2 Methodology (2.1 SDF, 2.2 Estimation, 2.3 Equity Premium, Eqs. 2.13–2.43), §3.1 Data, §3.2 Estimation (Eqs. 3.3–3.5), §3.3 OOS equity premium (Eq. 3.6), §3.4 performance, §4.1 shape, §4.2 rational-expectations regression, §5 Conclusion, Appendices A–B, Tables 1–7, Figures 1–4. Table 5 and Table 7 cell grids were additionally re-extracted directly from the LaTeXML `<tr>/<td>` structure of the pinned v2 HTML to confirm column-to-cell mapping.
- **Code / replication / data availability:** keyword scan of the pinned v2 full text gives `github` 3 hits (all arXiv UI chrome: "Report GitHub Issue", "Submit without GitHub", "Submit in GitHub"), `code availability` 0, `data availability` 0, `replication package` 0 → **no code, no replication package, no data-availability statement anywhere in v2**. Underlying option data is **OptionMetrics** (commercial) → not independently reproducible without a license.
- **Primary-source checksum (performed 2026-09-24 against the pinned v2):** (a) author list = the three names above, affiliations as printed; (b) version/date = v2 23 Jul 2026 (v1 9 Jul 2026), HTML header stamp matches; (c) sample period = OptionMetrics **January 1996 – February 2023**, with the σ̄* in-sample window ending **Dec 18, 2009**, expanding-window estimation, OOS evaluation beginning **Dec 18, 2009**; (d) universe = **S&P 500 index options** (daily index prices plus option bid/ask quotes) at monthly reference dates with maturities **30/60/90/120/180/270/360 days**; (e) transaction-cost treatment = **full-text keyword scan: `slippage` 0, `bid-ask` 0, `bid ask` 0, `latency` 0, `fees` 0, `commission` 0, `transaction cost` 0, `transaction-cost` 0, `financing` 0, `market impact` 0, `borrow` 0, `turnover` 0, `Sharpe` 0, `drawdown` 0, `win rate` 0, `fill` 0, `spread` (word count) 3, `leverage` 1 hit = "leverage constraints faced by these sophisticated market participants", `margin` 1 hit = "marginal rate of substitution", `cost` 0 hits** → §3.1 Data, §3.2 Estimation, §3.3–§3.4 and §4 were read, not just the abstract: **no fee / spread / slippage / borrow / financing / impact / fill / capacity model exists anywhere in v2**; every execution-cost field is `data gap` and is **never** to be read as zero cost; (f) core performance numbers all anchored below to Table 5 / Table 6 / Table 7 with row, column and benchmark identity; (g) publication status = preprint only (see above).
- **Deduplication (2026-09-24, whole repository — not `git log -20`):** ripgrep/`search_files` across **2,507 `*.md` records (hidden-inclusive; `find . -name "*.md"` = 2,507)** and **`coverage_manifest.csv` (5,808 lines)** for `2607.08500`, `10.48550/arXiv.2607.08500`, the exact title *Estimating the Stochastic Discount Factor from Option Prices*, `Kenichiro Shiraya`, `Tomohisa Yamakami`, `Shiraya`, `Yamakami`, `Akira Yamazaki` (only unrelated Konno & Yamazaki 1991 MAD-portfolio citation in one record), `volatility-scaled SDF`, `TVS EP`, `time-varying volatility scaled`, `Martin's bound`, `Martin bound`, `OptionMetrics`, `Option Metrics`, `option-implied SDF`/`pricing kernel`/`implied pricing kernel`/`Breeden-Litzenberger` → **zero records carry this source identity**, and `coverage_manifest.csv` has **0** hits for every token.
- **Materially distinct from adjacent records (four axes stated):** (1) `cross-predictive-sdf-cross-asset-spillover-max-sharpe-2026-09-23.md` (arXiv:2602.20856) — mechanism: cross-sectional characteristic → max-Sharpe SDF with ridge Λ/Ψ spillovers vs **option-implied SDF recovered by Hansen–Jagannathan-distance minimization and read as a time-series premium forecast**; universe: US equity cross-section (CRSP, monthly) vs **single S&P 500 index-option surface**; signal: 138 standardized characteristics vs **polynomial in volatility-scaled log return**; horizon: monthly portfolio rebalance vs **30–360-day maturity-matched EP forecasts**. (2) `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md` (arXiv:2607.11054) — different source and different mechanism (shrinkage over a set of published EP predictors, no option surface). (3) `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24.md` (arXiv:2604.07870) — cross-sectional realized-skewness dispersion timing vs option-implied SDF level forecast; different signal construction and data dependency (realized returns vs option surface). (4) `common-firm-level-investor-fears-equity-options-cross-section-premium-2026-09-24.md` (arXiv:2309.03968) — firm-level option-sourced fear in the **cross-section of stocks** vs index-level time-series EP. (5) `btc-option-implied-vov-predicts-excess-returns-risk-premia-2026-09-19.md` (SSRN 6410838/6771170) — crypto vol-of-vol predictor, different asset class, different statistic, no SDF recovery. No `Goyal-Welch`-style direct record of this source exists in the repository.

## Economic mechanism

### Source-reported

The authors' stated rationale (§1, §2):

1. The stochastic discount factor (pricing kernel) maps the physical to the risk-neutral measure and encodes market-wide risk aversion; it is hard to estimate because it depends on all assets, so it is projected onto a specific asset. Two classical recovery routes exist — risk-neutral density ÷ physical density (Breeden–Litzenberger plus a physical model), or direct parametric estimation from payoff/value relationships — and the paper takes the second route (Chabi-Yo 2012; Song–Xiu 2016; Bakshi et al. 2010, 2023).
2. **Proposed specification:** the SDF is a **piecewise polynomial of the log return normalized by volatility** — `n(S_T) = exp{ f_{p,n}( z ) }` with `z = log(S_{t+τ}/F_{t,t+τ}) / (σ*_{t,t+τ} √τ)` (Eq. 3.5, **TVS** = time-varying volatility scaled) versus the same polynomial normalized by the full-sample average variance-swap rate `σ̄*_τ` (Eq. 3.4, **CVS** = constant volatility scaled). `f_{p,n}` is a degree-`n` polynomial on `[y_min, y_max]` extended linearly with continuous value and first derivative outside (Eq. 3.3). Degrees `n = 2…6` are estimated; `n = 1` is excluded because it yields a monotonic SDF inconsistent with the observed option-return patterns; the maximum order is 6 because Hansen's (1982) J-test requires over-identification (§3.2).
3. **Estimation:** parameters minimize the **Hansen–Jagannathan distance** (Eq. 2.30), whose basis assets are the **option-implied discount bond price and option-implied forward price**, notionals rescaled so prices are `v_t = 1` each date; the CVS SDF uses the CVS strike set and the TVS SDF uses the TVS strike set (§3.2).
4. **Bond-price consistency:** the estimated SDF is adjusted as `m_{t,T}(S_T) = β_{t,T} · n_{t,T}(S_T)` (Eq. 2.36, adjustment attributed to Yamazaki 2022 and Shiraya et al. 2025) so that it reproduces discount bond prices, which the paper argues is what makes a precise equity premium computable — few competing studies impose this condition (§1, §2.1).
5. **Equity premium:** expectations of any payoff are evaluated with Carr–Madan's spanning formula (Eq. 2.34) applied to option prices; the target is the horizon expected excess return `EP_{t,T}` (Eqs. 2.32–2.33), evaluated against the realized excess return `EPR_t = D^{-1}_{t,T}(S_T/F_{t,T} − 1)` (§3.3). Benchmarks without an explicit SDF: the **Martin (2017) M-Bound** (Eq. 2.38–2.39) and the **Chabi-Yo & Loudis (2020) CYL-Bound** extended to continuous dividends (Eqs. 2.41–2.43).
6. **Stated economic content of the shape:** the recovered SDF shows a hump on the shallow-put side that sharpens into a **W-shape as maturity lengthens**; the shallow-put hump is rationalized theoretically by a stochastic-volatility model with a **constant market price of risk** (§1, §4.1), consistent with Cuesdeanu & Jackwerth (2018) ATM humps in calm periods.
7. **Stated predictive claim:** "The equity premium derived from the time-varying volatility scaled SDF demonstrates superior out-of-sample predictive performance relative to existing benchmarks, such as the Martin bounds" (abstract; §3.4, §5), because time-varying scaling removes regime-dependent noise that a constant scaling leaves in the recovered SDF.
8. **All inputs are option-implied:** the underlying price, risk-free rate and dividend yield are extracted **solely from option prices** (Appendix A) rather than from external series, for (i) internal consistency / no cross-market timing mismatch and (ii) capturing the "pure forward-looking expectations of option market participants" (§1, §3.1).

### Research interpretation

Falsifiable hypothesis: **an SDF recovered from the S&P 500 option surface with volatility-scaled polynomial structure contains a time-varying expected-excess-return component that forecasts realized index excess returns out of sample better than historical-average and bound-based estimators, and the volatility-scaling step (TVS vs CVS) is the causal increment.**

Component roles (Scout-normalized):

```text
Regime: none explicit — volatility enters as the normalizer inside the SDF argument
        (the paper's implicit regime statement), not as a trading gate.
Primary signal: option-implied TVS equity premium (EP) at a chosen maturity,
        recomputed at each monthly option-maturity reference date.
Benchmark/ablation: CVS EP (same pipeline, constant scaler); M-Bound; CYL-Bound; HA.
Entry / exit / sizing / holding / stop: NOT PRESENT IN SOURCE — the source is a
        forecast-accuracy study (MSPE / R²_OS and a levels-slope regression), not a
        strategy; any trading rule below is research-proposed.
```

The mechanism is a **risk-premium/expectations channel** (option-implied conditional mean of index returns), not an arbitrage. Nothing in the source demonstrates that the forecast is tradable; ablation of the vol-scaling step (TVS vs CVS) is the single most decisive test of the claimed contribution, and the source's own Table 5/Table 7 already show CVS carrying almost no predictive content.

## Signal

**What the source specifies (source-reported):**

- **Formation timestamp:** reference dates are **the days on which monthly options mature** (monthly cadence, §3.1); the SDF is estimated **expanding-window using data up to the day immediately preceding each reference date** (§3.3). Timezone/session convention for the daily OptionMetrics snapshot is `not stated in source` → `data gap`.
- **Lookback:** expanding (all history from Jan 1996 onward, per reference date); the σ̄* constant-scaler is defined from option maturities **up to and including Dec 18, 2009** (§3.1). Warm-up: first expanding-window SDF estimate leads to an evaluation start of **Dec 18, 2009** (Table 7 note).
- **Instrument grid:** maturities **τ ∈ {30, 60, 90, 120, 180, 270, 360} days**; strikes selected at `z ∈ {−1.0, −0.6, −0.2, 0.2, 0.6, 1.0}` in units of `σ√τ`, snapped to the nearest available strike (Eq. 3.2), producing a **six-strike × seven-maturity** grid per reference date under either strike-set convention (CVS or TVS).
- **Screens (§3.1):** drop observations where **ask < 2 × bid**; drop contracts with **zero open interest or zero volume**; drop contracts with **fewer than 10 days to maturity**; drop strikes violating **monotonicity across strikes** (Fukasawa et al. 2011 Step 2-1).
- **Numerics:** Carr–Madan integration over `[F·e^{−4σ_p√(T−t)}, F]` (puts) and `[F, F·e^{+4σ_c√(T−t)}]` (calls), **1,000 intervals, trapezoidal rule**; option prices → implied vol → **linear interpolation in the volatility domain** → back to prices; empty intervals extrapolated by holding the endpoint implied volatility constant; second derivative by central finite difference (Eq. 3.1, Appendix B).
- **Forecast target:** realized excess return `EPR_t = D^{-1}(S_T/F_{t,T} − 1)` over the matching horizon (§3.3, Eq. 3.6); EP at the target maturity is **linearly interpolated** between the EPs at the surrounding actual maturities (§3.3).
- **Specification selection:** polynomial order is chosen from the OOS comparison itself — "the fourth order specification consistently delivers the strongest and most stable out-of-sample performance … it is therefore adopted in the subsequent analysis" (§3.3, Table 5) — **order 4 is used for all headline Table 6/Table 7 results and for the shape analysis in §4.1.**

**Not specified by the source (therefore `underspecified`, not reconstructible as a strategy):** long/short trigger, threshold, position direction, sizing, holding period, rebalance rule, exit, stop, transaction timing (same-bar/next-bar equivalent), and any portfolio construction. **The source contains no entry, no exit, no sizing and no threshold rule anywhere in v2.**

**Research-proposed operationalization (label: `research-proposed`, not source-reported):** at each monthly reference date, compute TVS EP at a fixed maturity (maturity choice `research-proposed`: 180 days as a mid-horizon compromise between the near-zero 30-day and the numerically unstable 360-day cells); hold a long S&P 500 proxy when the TVS EP exceeds its own trailing 36-month mean (threshold `research-proposed`), otherwise hold cash; monthly rebalance at the reference date's close (timing `research-proposed`). Every parameter in this paragraph was chosen by the Scout and has no support in the source.

## Required data

- **Instrument / universe:** S&P 500 index options (OptionMetrics daily PUT/CALL quotes), plus the S&P 500 index level, an option-implied discount bond price and an option-implied forward price per reference date and maturity; **one index, no cross-section**.
- **Venue / vendor:** OptionMetrics (commercial; exact field names, snapshot convention and license terms `data gap`).
- **Market type:** index options (European-style index option quotes; exercise style `not stated in source` → `data gap`) plus the index itself as the forecast target asset.
- **Timeframe:** daily option quotes; monthly reference dates (option maturity dates); horizons 30–360 days.
- **Fields:** bid/ask quotes, open interest, volume, days to maturity, strikes, underlying index price, option-implied risk-free rate `B_{t,t+τ}`, option-implied dividend yield `q`, option-implied forward `F`, variance-swap rates (for σ̄* and σ*).
- **Point-in-time:** expanding-window estimation strictly uses data up to the day before each reference date (§3.3) — good; but **σ̄* is a full-sample-to-2009 constant**, the polynomial **order is selected on the evaluation sample**, and the §4.1 shape figures are estimated on the **full Jan 1996 – Feb 2023 sample including the evaluation window** → those three components are not point-in-time.
- **Timestamp / timezone:** `not stated in source` → `data gap` (daily close convention, exchange timezone, whether quotes are closing or intraday-snapshot).
- **Missing data:** screens above (bid/ask, OI/volume, DTE, monotonicity); interpolation in the volatility domain; **flat implied-vol extrapolation outside observed strikes**; order-3 360-day cells treated as missing because the call-side SDF collapses toward 0 (§3.3 note). No other imputation rule is declared.
- **Funding / fee / spread needs:** **not addressed anywhere in the source** → `data gap`. Any replication must add its own cost, borrow and financing model (`research-proposed`).

## Execution assumptions

**The source models no execution at all.** Verified by full-text keyword scan of the pinned v2 (Provenance, item (e)): no slippage, no bid-ask cost, no latency, no fees, no commission, no transaction-cost discussion, no financing, no market impact, no borrow, no turnover, no fill model, no leverage/margin model, no capacity statement, and **no Sharpe / drawdown / win-rate / P&L figure anywhere in v2**. The bid and ask quotes that do appear are used **only as a data-quality screen** (ask < 2× bid dropped) and inside the spanning-formula integral — never as a cost.

Consequently: signal-to-order timing, order type, fill model, fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow and latency are **all `data gap`** and must not be inferred as zero. Any statement that this forecast is "tradable" is `research-proposed` and untested.

## Evidence

### Source-reported

All figures below are **source-reported**, read from the pinned **arXiv:2607.08500v2** HTML, with table provenance; none has been independently reproduced.

- **Statistic:** Campbell–Thompson (2008) out-of-sample `R²_OS = 1 − Σ(EPR − EP)² / Σ(EPR − EP̄)²` (Eq. 3.6), benchmark `EP̄` = **historical average (HA) of realized daily excess returns from Jan 1996 up to the predicting point**; positive = lower MSPE than the benchmark. Significance stars (`*`, `**`, `***` = 10%, 5%, 1%) test positiveness **following Clark & West (2007)** with Newey–West (1987) lags set to **1.5 × days to maturity** (Table 6 note). Normalization by the standard deviation of `EPR_t` applies to the "All" aggregation (Table 5 note).
- **Table 5 (R²_OS vs HA, by SDF type and polynomial order; Full/All row, columns read left-to-right as printed: CVS orders 2–6 then TVS orders 2–6):** CVS `4.01%`, `#`, `4.57%`, `3.87%`, `3.21%`; TVS `2.03%`, `#`, `7.04%`, `5.71%`, `6.03%` (`#` = treated as missing per the table note: at 360 days and order 3 the call-side SDF converges toward zero and the EP becomes numerically unstable, values < −500%). Selected per-maturity Full rows for order 4: e.g. 30d CVS `−0.01%` / TVS `1.80%`; 120d CVS `9.72%` / TVS `12.05%`; 270d CVS `16.10%` / TVS `16.18%`; 360d CVS `17.90%` / TVS `22.57%`. Source prose: order 4 maximizes the "All" R²_OS for both types and is "adopted in the subsequent analysis".
- **Table 6 (headline, order 4, `R²_OS`, Full window = Dec 18, 2009 → data end):**
  - **CVS EP vs HA:** 30d `−0.01%`, 60d `1.26%`, 90d `3.79%**`, 120d `9.72%**`, 180d `10.78%*`, 270d `16.10%**`, 360d `17.90%***`. **vs M-Bound:** `−1.88%`, `−1.39%`, `0.50%`, `6.58%**`, `9.10%*`, `17.09%**`, `20.97%***`. **vs CYL-Bound:** `−2.78%`, `−3.64%`, `−3.71%`, `0.82%`, `0.52%`, `5.19%*`, `6.14%**`.
  - **TVS EP vs HA:** 30d `1.80%**`, 60d `4.74%**`, 90d `7.49%**`, 120d `12.05%**`, 180d `11.07%*`, 270d `16.18%**`, 360d `22.57%***`. **vs M-Bound:** `−0.04%`, `2.18%**`, `4.33%**`, `9.00%**`, `9.39%**`, `17.17%***`, `25.46%***`. **vs CYL-Bound:** `−0.92%`, `0.00%`, `0.28%`, `3.39%*`, `0.84%`, `5.28%*`, `11.47%***`.
  - **TVS EP vs HA, sub-windows:** `1st/2` (Dec 18 2009 – Dec 17 2015) `1.55%**`, `3.82%**`, `6.42%**`, `12.13%**`, `10.69%**`, `21.03%**`, `36.16%***`; `2nd/2` (Dec 18 2015 – Dec 15 2017, window as printed — see `contradictions`) `1.93%*`, `5.23%*`, `8.12%*`, `12.01%`, `11.30%`, `13.42%`, `15.06%**`.
  - Source prose: CYL-Bound is the toughest benchmark; TVS produces larger and more frequently significant gains than CVS; gains rise steeply with maturity.
- **Table 7 (OOS regression of realized ER on each EP estimate, evaluation from Dec 18, 2009, NW lags = 1.5 × maturity):**
  - **M-Bound:** slope `3.896 → 3.005` across 30→360d, all 95% CIs strictly above 1 (e.g. 30d `[2.614, 5.179]`), `R² 0.066 → 0.256`.
  - **CYL-Bound:** slope `3.095 → 1.759`, CIs `[2.100, 4.091] → [0.978, 2.541]`, `R² 0.065 → 0.245`; source states the rational-expectations restriction `slope = 1` is **not rejected at 120 days and longer**.
  - **CVS EP:** slope `−0.062, 0.326, 0.870, 1.442, 0.923, 0.660, 0.984`; **every 95% CI contains zero**; `R² 0.000, 0.001, 0.007, 0.026, 0.023, 0.012, 0.019`.
  - **TVS EP:** slope `2.221, 2.856, 2.659, 2.067, 1.473, 2.463, 3.233`; CI lower bounds `−0.052, 0.509, −0.172, −0.479, −1.984, −1.252, 1.027`; `R² 0.018, 0.052, 0.073, 0.084, 0.043, 0.093, 0.203`. Source prose: **`slope = 0` is not rejected except at 60 and 360 days** ("evidence of predictability is inconclusive"), while `slope = 1` is not rejected everywhere except 360 days.
- **Figure 1:** the SDF-based EPs generally sit **above** both M-Bound and CYL-Bound, but **fall below them during the 2020 COVID shock**, and CVS short-maturity EPs turn **negative in 2020**, which the source itself calls "inconsistent with previous studies, which generally find that higher EPs are observed during times of market instability."
- **Figures 2–3 / §4.1:** full-sample (Jan 1996 – Feb 2023) fourth-order CVS and TVS SDFs both display an upward-sloping pattern toward the outside on both the put and call wings; the ATM/shallow-put hump strengthens with maturity and a clear W-shape emerges at long maturities; 2σ confidence bands use Newey–West lags = 1.5 × maturity in months, rounded up.
- **Tables 1–2 (option return statistics, full period):** illustrate why a monotone (`n = 1`) SDF is rejected — e.g. 30-day Put z = −1.0 average return `−48.7%` (sd `17.7%`, 95% bootstrap CI `[−73.8%, −16.9%]`, 1,000 replications), 30-day Call z = +0.2 average `+11.9%`.
- **No turnover, no Sharpe, no drawdown, no hit rate and no P&L are printed anywhere in v2** — this is a forecast-accuracy and coefficient-restriction study, **not a backtest**.

### Independently reproduced

`not independently reproduced.`

What this run actually did (and nothing more): fetched and read the pinned landing page and the v2 HTML full text; re-extracted the Table 5 and Table 7 grids from the LaTeXML markup to confirm column-to-cell mapping; cross-checked Table 5 order-4 cells against the corresponding Table 6 cells (30d CVS `−0.01%`, 30d TVS `1.80%`, 360d TVS `22.57%` match across tables); ran the full-text cost/risk keyword scan; ran the whole-repository source-identity dedup. **No OptionMetrics data was obtained, no SDF was re-estimated, no regression or MSPE was recomputed, and no trading rule was tested.**

### Negative evidence

1. **No cost, fill, leverage, borrow, capacity or turnover model exists anywhere in v2** (keyword scan, Provenance (e)) — every execution field is `data gap`, never zero.
2. **No strategy exists in the source**: no entry, exit, sizing, holding period, threshold or risk layer, and **no Sharpe / drawdown / turnover / P&L figure at all**; the evidence is MSPE ratios and a levels regression.
3. **CVS EP has essentially no predictive content** (source's own Table 7): all seven 95% slope CIs contain zero and `R² ≤ 0.026`. The ablation baseline that isolates the paper's actual contribution (volatility scaling) therefore fails on the source's own numbers.
4. **TVS predictability is called inconclusive by the source itself**: `slope = 0` not rejected at 5 of 7 maturities (Table 7), `R²` as low as 0.018 at 30 days, and the conclusion concedes "wide confidence intervals and low explanatory power that limit inference about predictability … prevents drawing sharp economic conclusions."
5. **Specification selected on the evaluation sample**: polynomial order 4 was chosen *because* it won the OOS comparison over orders 2–6 (Table 5, §3.3) and is then reported as the headline in Tables 6–7 and used for §4.1 — classic test-set selection, no held-out set remains.
6. **Zero multiplicity control** over a grid of 2 SDF types × 5 orders × 7 maturities × 3 aggregation windows × 3 benchmarks (≈ 630 reported cells), with only Clark–West/NW per-cell inference; no deflated-Sharpe, Bonferroni, BH-FDR or MCS anywhere.
7. **Horizon dependence cuts against short-horizon use**: at 30 days the Full-window gains vs HA are `−0.01%` (CVS) and vs CYL-Bound are `−0.92%` (TVS); the source states R²_OS is "near zero or even negative at the 30 day maturity."
8. **Against the toughest benchmark the win rate is thin**: counting printed Full-window cells (our count, not a rerun), TVS EP beats CYL-Bound with a star at only **3 of 7** maturities and CVS at **2 of 7**; vs HA in the `2nd/2` window TVS is starred at only **4 of 7** (and unstarred from 120–270d).
9. **Source-internal contradiction** on aggregation windows (frontmatter `contradictions`): the printed `2nd/2` window ends **Dec 15, 2017** yet `Full` runs to the 2023 data end, so the "half" labels cannot partition the full sample; stated twice in v2, never reconciled.
10. **Numerical instability of the estimator is documented by the source**: order-3 360-day cells are `< −500%` and dropped as missing because the call-side SDF "converge[s] rapidly toward zero" (Table 5 note) — the very object being estimated can collapse.
11. **Crisis-period anomaly**: SDF-implied EPs fall *below* the bounds and short-maturity CVS EPs turn negative during 2020 — opposite to the stylized fact the literature expects (§3.4), and the worst-performing region (short maturity) is exactly where a timing signal would have to act.
12. **Overlapping / ad-hoc inference**: at 180–360-day horizons with monthly reference dates the forecast windows overlap heavily; the only HAC treatment is "1.5 × days to maturity" lags, a rule with no justification or robustness check in the source.
13. **Point-in-time gaps**: σ̄* is a constant estimated on option data through Dec 18, 2009 (fine for the OOS period, but not re-estimated); order selection and §4.1 shape estimation use the evaluation sample; the exact per-maturity OOS end dates are only implied by "data end … maturity is Feb 28, 2023" → `underspecified`.
14. **Data and reproducibility**: OptionMetrics is commercial; **no code, no data-availability statement, no replication package** in v2; numerical choices (1,000-point trapezoid, linear-in-vol interpolation, flat vol extrapolation, the six-strike grid) are untested for sensitivity.
15. **Publication status**: preprint only, no journal reference, no external DOI, peer-review status not stated.
16. **Universe breadth**: a single index (S&P 500) over Jan 1996 – Feb 2023 with no cross-market, cross-index or post-2023 out-of-sample evidence; the sample contains no post-2023 regime.
17. **Benchmarks are themselves premium estimators** (M-Bound, CYL-Bound), so "beating" them is a forecast-MsPE comparison among premium estimates, not evidence of an executable edge over a tradable baseline (e.g. a trend or VRP overlay is never tested).

## Falsification plan

Every threshold below is a Scout-chosen acceptance/failure rule: **`research-defined falsification threshold`**; procedural choices are **`research-proposed`**. Failure of any single test materially weakens the hypothesis; F2, F5 and F8 are the core mechanism tests.

- **F1 — Independent replication (research-proposed):** rebuild the pipeline on a **second option vendor** (not OptionMetrics), same screens, expanding window, fixed order 4. **Fail if** Full-window `R²_OS` vs HA at 180/270/360d is below **50% of the printed values (11.07% / 16.18% / 22.57%)** or Clark–West significance disappears (one-sided t < **2.0** equivalent).
- **F2 — Honest specification selection (research-proposed):** choose polynomial order using **only data through 2009** (the σ̄* in-sample window), freeze it, and re-run Tables 6–7. **Fail if** Full-window `R²_OS` vs HA at 180/270/360d falls to **≤ 0**, or if TVS loses to CVS (the claimed contribution inverts).
- **F3 — Multiplicity (research-defined):** apply **Benjamini–Hochberg at q < 0.10** across the full printed grid (2 types × 5 orders × 7 maturities × 3 windows × 3 benchmarks). **Fail if** fewer than **half** of the starred Full-window cells survive.
- **F4 — Cost ladder (research-proposed strategy, research-defined gate):** implement the research-proposed timing rule (Signal section) on an S&P 500 proxy with a **0/1/2/5/10 bp per-side** ladder plus, for any options-hedged variant, bid-ask paid on both legs. **Fail if** the effect is dead at **5 bp** per side **or** net Sharpe **< 0.5**.
- **F5 — Placebo (research-defined):** circularly shift the EP series **1,000** times relative to realized returns, preserving autocorrelation; **fail if** the observed `R²_OS`-vs-HA at 180/270/360d does not reach **|z| ≥ 2.0** against the placebo distribution.
- **F6 — Stronger baselines (research-proposed):** benchmark against **variance-risk-premium, CAPE-style and 12-1 momentum** forecasts on the same window. **Fail if** TVS EP adds **< 0.05** of `R²_OS` over the best of those baselines at 180–360d.
- **F7 — Frozen forward test (research-defined):** extend the sample past **Feb 2023** with all choices frozen (order 4, screens, scaler rule re-estimated only from data before each date). **Fail if** post-2023 `R²_OS` vs HA at 180/270/360d is **≤ 0** for two consecutive calendar years.
- **F8 — Mechanism ablation: volatility scaling (research-defined):** TVS vs CVS is the paper's causal claim. **Fail the mechanism** if the TVS-minus-CVS `R²_OS` gap at 180/270/360d is **< 0.03**, or if TVS slope CIs still contain zero at **≥ 5 of 7** maturities (as they do now).
- **F9 — Estimator robustness (research-defined):** perturb integration intervals (500 / 1,000 / 2,000), interpolation domain (vol vs price), strike grid offsets, the 10-DTE screen, and the `ask ≥ 2 × bid` screen. **Fail if** the order-4 Full `R²_OS` vs HA at 360d swings by more than **±50%** of 22.57% across these variants, or if the order-3/360d instability spreads to neighbouring orders/maturities.
- **F10 — Point-in-time / leakage audit (research-proposed procedure, research-defined tolerance):** re-estimate everything under a strict "no observation dated after the reference date" rule, re-deriving σ̄* per vintage, and verify that no evaluation-period information enters estimation (including §4.1-style full-sample fits). **Fail if** any input dated after the reference date is found, or if `R²_OS` values shift by more than **±0.02** in absolute terms.

## Crypto portability

`unproven`.

There is **no crypto analogue of the construction in the source**: no S&P-500-like single index with a deep, multi-maturity, six-strike liquid option surface at seven fixed maturities; no option-implied dividend yield; and no comparable variance-swap-rate term structure to define the scaler. Porting would require rebuilding every layer: option-implied forward and discount curve on a fragmented, per-venue surface (Deribit BTC/ETH only, few listed maturities, wide and stale wings), 24/7 timestamping instead of exchange daily closes, **no dividend yield** (so `q` must be set to 0 or to a staking/issuance proxy — a `research-proposed` choice), perpetual funding as a partial substitute for the forward, cross-exchange index/basis manipulation risk, thin open interest outside the front two expiries, and the extra venue/custody/settlement risk that the source never models. Speculative analogues (perpetual funding term structure, quarterly basis, options variance risk premia as premium forecasts) are hypotheses only; **the source demonstrates nothing in crypto**, and perp funding, 8-hour accrual, liquidation and mark-price manipulation are unmodeled here.

## Limitations

- `underspecified`: trading rule (absent entirely), timezone/session convention, exercise style of the options, per-maturity OOS end dates, EP annualization/units in levels, dagger-footnote meaning, OptionMetrics field/snapshot details, conflict-of-interest disclosure (only the CARF acknowledgment and the company disclaimer appear).
- `data gap`: all cost/spread/slippage/fee/financing/borrow/impact/fill/capacity/turnover fields; code; data-availability statement; replication package; journal/peer-review status.
- `not independently reproduced`: every number in Evidence → Source-reported.
- `unproven`: tradability of the forecast; crypto portability; robustness to spec selection, multiplicity and estimator numerics.
- Research-design limitations: order selected on the evaluation set; full-sample shape analysis; single index; preprint status; commercial data; heavy multiplicity; overlapping long-horizon windows with an ad-hoc HAC rule; internally inconsistent sub-window definitions; a source-documented numerical collapse region at order 3 / 360 days.
- Incremental-write threshold and deduplication/update rule were checked before writing (Provenance): no existing record shares this source identity or this mechanism/universe/horizon combination, so a new record is justified rather than an update.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack: no SDF estimation, no OptionMetrics acquisition, no EP series, no timing rule, no backtest, no Qlib run, and no Paper/Testnet/Live connection. This file is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No record may promote itself by wording, evidence count, confidence, or schedule behavior.

## Related Wiki records

Wiki Brain `kb_search` on 2026-09-24 for `stochastic discount factor equity premium option-implied` returned **0 results**; `equity premium prediction option prices` returned only adjacent option/VRP pages, none of which share this mechanism. No Wiki link is asserted for this mechanism itself. Closest existing pages (retrieval hooks, different mechanisms):

- [[quant/option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02]] (option-implied surface signals; skew/crash regimes, not SDF recovery or EP forecasting)
- [[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12]] (crypto VRP harvest; variance-swap estimator fragility)
- [[quant/crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13]] (crypto IV-premium shock as short-horizon spot predictor)

Repository-local neighbours with materially different mechanisms: `cross-predictive-sdf-cross-asset-spillover-max-sharpe-2026-09-23.md`, `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md`, `cross-sectional-realized-skewness-dispersion-market-timing-2026-09-24.md`, `common-firm-level-investor-fears-equity-options-cross-section-premium-2026-09-24.md`, `btc-option-implied-vov-predicts-excess-returns-risk-premia-2026-09-19.md` (four-axis distinctions stated in Provenance).

## Sources

- Kenichiro Shiraya, Tomohisa Yamakami, Akira Yamazaki, *"Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium"*, **arXiv:2607.08500v2 [q-fin.MF; q-fin.ST]**, v2 submitted 23 Jul 2026 (v1 9 Jul 2026). https://arxiv.org/abs/2607.08500
- Full text read for this record: https://arxiv.org/html/2607.08500v2 (784,388 bytes, fetched 2026-09-24) — §1, §2.1–2.3, §3.1–3.4, §4.1–4.2, §5, Appendices A–B, Tables 1–7, Figures 1–4.
- DOI: https://doi.org/10.48550/arXiv.2607.08500 (resolves to the abs page, checked 2026-09-24).
- Benchmarks cited *by the source* and named above only in that capacity: Martin (2017) M-Bound; Chabi-Yo & Loudis (2020) CYL-Bound; Campbell & Thompson (2008) `R²_OS`; Clark & West (2007); Newey & West (1987); Carr & Madan spanning formula; Hansen (1982) HJ/GMM distance; Breeden & Litzenberger (1978); Fukasawa et al. (2011) monotonicity screen; Schreindorfer & Sichert (2025) volatility-scaled polynomial SDF; Cuesdeanu & Jackwerth (2018); Bakshi et al. (2010, 2023); Chabi-Yo (2012); Song & Xiu (2016); Yamazaki (2022, 2025); Shiraya et al. (2025). These references were **not** independently opened for this record; they are reproduced as the pinned v2 cites them.
