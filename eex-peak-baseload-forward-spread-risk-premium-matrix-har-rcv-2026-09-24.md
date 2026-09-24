---
schema: strategy-research-record-v1
title: EEX Peak-vs-Baseload Forward Spread Risk Premia Predicted by Matrix-HAR Realized-Covariation Forecasts
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - electricity
  - energy-futures
  - risk-premium
  - volatility-forecasting
status: research-only
confidence: medium
source_as_of: 2026-06-04
sources:
  - "https://arxiv.org/abs/2606.05991"
  - "https://arxiv.org/html/2606.05991v1"
  - "https://doi.org/10.48550/arXiv.2606.05991"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "arXiv:2606.05991v1 §5.1 prose states the RCV-based models' spread-risk-premium regression R² 'range between 35 % and 48 %', but the maximum printed R² in Table 4 is 0.472 (47.2 %, row 'RCV from DRD-HAR-P2'); no printed cell equals 48 %. The §7 conclusion's 'doubling the R²-statistic' claim corresponds to 0.472 / 0.244 = 1.93x (our arithmetic from Table 4), i.e. rounded, not exactly 2x. Unreconciled inside v1."
---

# EEX Peak-vs-Baseload Forward Spread Risk Premia Predicted by Matrix-HAR Realized-Covariation Forecasts

## Provenance

- **Primary source:** Thomas K. Kloster, Fred Espen Benth, *"Forecasting of volatility and risk premia in electricity markets"*, `arXiv:2606.05991v1 [q-fin.GN]` (primary General Finance; secondary Econometrics `econ.EM` per arXiv abs subjects line "General Finance (q-fin.GN); Econometrics (econ.EM)").
- **Authors, exactly as printed in the v1 HTML header:**
  1. **Thomas K. Kloster** — Affiliation: Department of Economics and Business Economics, Aarhus University; Affiliation: Department of Data Science and Analytics, BI Norwegian Business School; Affiliation: CoRE, Center for Research in Energy: Economics and Markets.
  2. **Fred Espen Benth** — Affiliation: Department of Data Science and Analytics, BI Norwegian Business School. (`data gap`: a second Benth affiliation is not printed in the v1 header block we read; only the BI affiliation appears there.)
- **Version / date (primary-source checksum, verified 2026-09-24):** submission history on the arXiv abs page shows **only `[v1] Thu, 4 Jun 2026 10:38:46 UTC (281 KB)`**, submitted from Thomas K. Kloster; the v1 HTML header prints `arXiv:2606.05991v1 [q-fin.GN] 04 Jun 2026`. No v2 exists.
- **Publication status:** **preprint only.** The abs page carries **no `Comments` field, no `Journal reference`, and no publisher DOI** (grep count 0 for each). arXiv/DataCite DOI `10.48550/arXiv.2606.05991` resolves **HTTP 200**. License: **CC BY 4.0** (both the v1 HTML "License: CC BY 4.0" line and the abs-page `licenses/by/4.0/` icon).
- **Full text read:** `https://arxiv.org/html/2606.05991v1` → HTTP 200, **343,431 bytes**, fetched and read in full on 2026-09-24; every quantitative claim below is located in a printed Table / Figure / Section of that pinned v1.
- **Funding / disclosure (v1 §8–§9):** authors declare no conflicts of interest; Kloster acknowledges DFF grant 10.46540/5247-00005B and the Center of Research in Energy: Economics and Markets; Benth acknowledges SURE-AI Centre grant 357482, Research Council of Norway.
- **Code / data availability:** `data gap` — **no code, repository, replication-package or data-availability statement anywhere in v1** (full-text search for github / code availability / replication / repository returns only arXiv UI chrome). Spot data is named as public (ENTSO-E Transparency Platform); the futures vendor/product identifiers are not.
- **Sample period (primary source):**
  - *Spot / forecasting arm:* German generation zone hourly day-ahead prices, **2018-10-01 → 2025-10-01**, same dataset as Kloster and Benth (2026) (§5); first 365 days semigroup burn-in, next 200 days initial training, then **daily forecasts from 2020-04-19**, models and semigroup **refit on a rolling 28-day basis**, **1,984 scored forecast origins (2020-04-19 → 2025-09-23)** over `n = 2191` days (Table 1 caption).
  - *Premium arm:* German **monthly forward (futures) contracts on the EEX exchange, trade dates 2020-03-02 → 2025-09-30**, front contract (shortest time to delivery) with `T1 − t` ranging 0–30 days; premium regression on **`n = 1358`** daily observations (§6.1, Table 4 caption).
- **Universe:** (i) physical day-ahead electricity for the German bidding zone (ENTSO-E); (ii) EEX German **monthly peak-load** (hours 8–19 average underlying) and **baseload** (full daily average underlying) futures (§6).
- **Transaction-cost treatment (primary-source full-text keyword scan of pinned v1, our count):** `slippage` 0, `bid-ask` 0, `latency` 0, `fees` 0, `commission` 0, `transaction cost(s)` 0, `leverage` 0, `financing` 0, `market impact` 0, `borrow` 0, `turnover` 0, `Sharpe` 0, `drawdown` 0, `win rate` 0; `fill` 1 hit and it is the phrase "infill limit" (§2 asymptotics), `margin(al)` 2 hits and both are "marginal" variance wording. **No fee, spread, slippage, impact, borrow, financing, margin/collateral, latency or fill model exists anywhere in v1 → recorded as `data gap`, never as zero cost.** Sections 4–6 (model specifications, forecasting horserace, premium regressions) were read directly for this judgement, not just the abstract.
- **Deduplication audit (deterministic, whole repository, 2026-09-24, before writing):** ripgrep `--hidden` (inclusive of `.mimo-worktrees/`, `.agents/`, `.hermes/`) across **all 2,505 `*.md` files** plus `coverage_manifest.csv` (5,808 lines) for `2606.05991`, `10.48550/arXiv.2606.05991`, exact title *"Forecasting of volatility and risk premia in electricity markets"*, `Kloster`, `Benth`, `matrix-HAR`, `matrix HAR`, `realized covariation`, `Bessembinder`, `spread risk premium`, `peak-load`, `peak load`, `risk premia in electricity`, `DRD-HAR` → **0 hits in every `*.md` and 0 in the manifest**. `Redl` returns only inside-word matches (`redLoss`, `redLen`, `redla`) in unrelated crypto records — **no record cites Redl et al.** Family-adjacent probes (`EPEX` 6 files, `ENTSO-E` 1 file, `baseload` 1 file, `forward spread` 3 files) resolve to existing **day-ahead / intraday spot** captures only (see Related records), i.e. different sources. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup. **Four-axis material distinction vs the existing electricity records:** *mechanism* — variance/skewness-priced **forward risk premium** in a traded futures spread (Bessembinder–Lemmon channel) vs day-ahead price mean reversion, forecast-reconciliation battery arbitrage, and intraday orderbook trajectory prediction; *signal construction* — matrix-HAR **realized-covariation forecast used as conditional-variance proxy in a premium regression** vs z-score reversal / hierarchical forecast reconciliation / sequence model; *universe* — **EEX monthly peak-load & baseload futures** vs EPEX/OMIE day-ahead hourly products and the German continuous intraday market; *horizon / data dependency* — front-month futures with 0–30-day delivery lead, RCV refit every 28 days vs next-day auction settlement, daily hierarchy reconciliation and orderbook depth.
- **Wiki Brain (read-only):** `kb_read` of `quant/strategy-research-record-spec-v1.md` → **10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`**; `kb_read` of `...-spec-v2.md` → **file does not exist**, so **v1 remains the canonical specification**. `kb_search` `"electricity forward spread risk premia"` → 0; `"electricity day-ahead price forecasting battery arbitrage"` → 0; `"realized covariation matrix HAR volatility forecasting"` → 1 unrelated hit (`quant/path-portfolio-optimization-signature-defect-lift-2026-09-02.md`); `"electricity"` → 4 hits, none on this mechanism. **No stable Wiki Brain page covers this record; no Wiki link is asserted.**

## Economic mechanism

### Source-reported

- The source builds on the structural equilibrium model of **Bessembinder and Lemmon (2002)** (as cited by v1 §6): a forward price equals expected spot plus a premium linear in the conditional **variance** and **skewness** of the delivery-period average spot price, so `RP_t(T1,T2) = α·V_t[·] + β·Skew_t[·]` (Eqs. 16–17), following the EEX empirics of **Redl et al. (2009)**, who note the two terms do not carry the same structural interpretation but may still carry predictive power.
- Because EEX trades **monthly peak-load** (hours 8–19) and **baseload** (24h) futures on the same delivery month, the difference of the two premia is a **tradable spread risk premium** `SRP = RP^peak − RP^baseload` (Eq. 18), which reduces to `SRP_t = α·V_t[P^p − P^b] + β·Skew_t[P^p − P^b]` (Eq. 19).
- The source's contribution: replace the backward-looking 28-day rolling variance with the **forecast of the realized covariation (RCV) matrix** projected onto the peak-vs-baseload portfolio weights, `V_t[P^p − P^b] ≈ Tr( RCV̂ (ωp − ωb)(ωp − ωb)ᵀ )` (Eq. 20) — "the right hand side of (20) is exactly the predicted RCV of a portfolio that is long a peak-load forward contract and short a baseload contract" (§6). The RCV forecast comes from a **matrix-HAR ("HAR-DRD"/"DRD-HAR") family**: daily/weekly/monthly/**quarterly** (7/28/91-day, electricity trades every calendar day) autoregressive components on the diagonal variances `D` and the correlation matrix `R` separately (A = DRD decomposition, §2–§4), with optional linear+quadratic price covariates (`-P2`), past-week wind+solar generation share (`+ren`), and a RiskMetrics-style (`λ = 0.94`) time-varying spillover regime term (`+tvSpill`).
- Source-reported headline: adding RCV forecasts **"vastly improves"** / provides *"substantially improved forecasts of spread risk premia compared to standard methods relying on backward looking volatility"* (abstract; §7: "capable of doubling the R²-statistic of the classical risk premium regression").

### Research interpretation

- Falsifiable mechanism: **the conditional variance of the within-month peak-minus-baseload spot spread is priced into the EEX peak/baseload forward spread, and that conditional variance is predictable from the recent realized intra-day covariance structure.** When the RCV forecast of the spread portfolio is high, the compensation demanded for holding peak-load vs baseload delivery risk rises, so the *ex-post* spread risk premium is larger; a matrix-HAR forecast sees that state earlier than a 28-day rolling variance does.
- Component roles (hybrid structure, source-reported construction):
  - **Signal input (source-reported):** daily matrix-HAR RCV forecast `RCV̂⁷_{t+7}` → spread-portfolio variance proxy (Eq. 20), plus a **backward-looking 28-day rolling skewness** of the spot spread as the second regressor (§6.1, source-specified).
  - **Estimation layer (source-reported):** two-parameter time-series regression (19) with Newey–West HAC standard errors, bandwidth 60, on `n = 1358` overlapping front-contract daily observations.
  - **Trading layer (entirely research-proposed — the source specifies NO entry, exit, sizing, threshold, holding or execution rule and never claims a strategy):** hold long the front-month peak-load future / short the front-month baseload future while a *past-only* estimate of the predicted `SRP` is positive, otherwise flat. This operationalization is **not** in the source and must not be read as source-reported.
- Do not assume every component contributes alpha: the skewness leg is statistically dead in the source's own Table 4 (see Negative evidence), so the thesis effectively rests on the variance leg alone pending ablation.

## Signal

**Source-reported construction (reconstructable parts):**

- **Formation timestamp:** the RCV model, semigroup and regressions are refit **every 28 days** on a rolling basis with forecasts produced **daily** at day `t` from information through `t` (§5). `data gap`: the paper never states the publication/availability clock of the day-ahead prices relative to the forecast creation time, nor any timezone convention for the hourly series → **point-in-time availability is `underspecified`**.
- **Lookback:** spot sample from 2018-10-01; 365-day burn-in for the semigroup estimator `𝒮_δ` (Eq. 5); 200 further days of initial training; first forecast 2020-04-19; refits on a rolling **28-day** window for the log-variance regression while the correlation regression uses an **expanding** window (§4, "Rolling HAR-DRD" variant); HAR horizons **1 / 7 / 28 / 91 days** (daily/weekly/monthly/quarterly); renewables covariate = average wind+solar generation share **over the past week**; EWMA benchmark uses `λ = 0.94`.
- **Premium regression:** dependent variable = **ex-post** spread risk premium `F_t(T1,T2) − realized average spot over delivery` (computed after the delivery period; §6.1), variance proxy ∈ {28-day rolling variance of the spot spread (baseline), forecast spread RCV from each of the RCV models}, skewness proxy = 28-day rolling skewness in every specification (§6.1).
- **Weekly-ρ-monthly alignment (source-specified approximation):** the source uses the **weekly** `RCV̂⁷` even though delivery is monthly, justified by the annualization in Eq. (7) plus RCV persistence: `E_t[RCV̂^{T2−T1}] ∝ RCV̂⁷_t` (§6.1, source's own words: "does not align with the monthly delivery period … approximately").
- **Entry / exit / holding / sizing / ties / re-entry:** **not stated in source** — the paper contains no trading rule at all. Any sign rule, threshold, stop, sizing, holding period or order timing used later is **`research-proposed`**, e.g. *entry: next session after signal, long peak-load front future and short baseload front future when predicted SRP > 0 (threshold 0 is research-proposed); exit: delivery start or sign flip (research-proposed); sizing: equal-notional two legs (research-proposed); no stop (research-proposed)*.
- **Estimation-window caveat (our reading of §6.1 / Table 4):** Table 4's `α̂, β̂` are estimated **over the full 1,358-observation sample**, i.e. in-sample; the RCV inputs are genuine out-of-sample forecasts, but the premium regression itself is **not** estimated rolling/expanding and is never evaluated out-of-sample. Real-time use requires past-only coefficient estimation → that variant is **`research-proposed`** and untested by the source.
- **Reproducibility status of the signal:** the model equations, horizons, portfolio weights `ωb = (1/24)…`, `ωp = (1/12)` over hours 8–19, and all six Table-4 specifications are printed, but the **EEX contract identifiers, quotation/settlement convention, renewable-share data source, and the exact front-contract selection rule are `data gap`**, so an independent reconstruction would require choices the source does not specify.

## Required data

- **Instrument / universe (i):** hourly day-ahead electricity prices for the **German bidding zone** (EUR/MWh), **ENTSO-E Transparency Platform** (https://transparency.entsoe.eu), 2018-10-01 → 2025-10-01 (§5).
- **Instrument / universe (ii):** **EEX German monthly peak-load (hours 8–19) and baseload (24h) futures**, front contract daily over 2020-03-02 → 2025-09-30 (§6.1). `data gap`: contract codes, quotation/settlement price type (settlement vs last/mid), tick size, and roll/front-selection rule are never stated; vendor beyond "retrieved from the EEX exchange" is never named.
- **Market type:** wholesale power — physical day-ahead auction (signal input) and exchange-traded electricity **futures** (premium arm). Not crypto, not equity.
- **Fields:** 24 hourly day-ahead prices; derived daily/weekly/monthly/quarterly realized variances and the realized correlation matrix (RCV, matrix-valued, 24×24); average **wind + solar generation shares** over the past week for `+ren` (`data gap`: the paper does not name the renewable-generation data source — ENTSO-E is plausible but **not stated in source**); daily peak-load and baseload futures quotes for the front contract; delivery-period average spot to compute the ex-post premium.
- **Point-in-time:** models are refit on rolling 28-day windows with daily forecasts (§5), which limits look-ahead inside the forecasting arm; **but** `data gap` on publication timestamps of day-ahead prices and of the renewable-share series, and **the premium regression coefficients are full-sample** (see Signal). ENTSO-E series are subject to revision/retrospective edits → point-in-time risk is **`data gap`**.
- **Timestamp / timezone:** **not stated in source** (`data gap`). Daylight-saving handling is explicitly imputed (23-hour day: missing hour = average of adjacent hours; 25-hour day: the two overlapping hours merged by their average) — this is a **source-specified imputation rule**, unusual for this contract family and worth re-auditing independently.
- **Missing data:** only the DST rule above is specified; no treatment for missing hours, stale quotes, suspended sessions, or bad prints is described → `data gap`.
- **Funding / fee / spread needs:** **none observed, none modeled, all `data gap`** — futures margin/collateral, exchange and broker fees, bid-ask spread, and slippage are never mentioned (full-text keyword scan above).

## Execution assumptions

- **Order type / fill model / latency / signal-to-order delay:** **not stated in source** — there is no order or execution layer in the paper (`data gap`).
- **Fees, spread, slippage, impact, capacity:** **not stated in source** (0 keyword hits across pinned v1). EEX monthly power futures liquidity, open interest and volume are **never reported** → capacity is `data gap`, not unlimited.
- **Leverage / margin / borrow:** futures imply margin, but the paper discusses **no margin, collateral or leverage** (`margin` appears only inside the word "marginal"); shorting a leg requires no borrow in futures but carries margin and basis risk — all `data gap`.
- **Crossing the research/production boundary:** because the source has **no cost, no fill and no P&L model**, any backtest we later run must attach its own execution assumptions labeled **`research-proposed`**; nothing in this record may be read as a net-of-cost result.
- If costs or fillability are unknown, the result is **not tradable** until a cost ladder test (F3/F4 below) is actually run.

## Evidence

### Source-reported

All figures below are `source-reported`, read directly from the pinned **v1 HTML**, each with its printed location. Nothing here has been re-estimated by us.

**Table 4 — spread risk premium regression (Eq. 19); Newey–West HAC bandwidth 60; `n = 1358` daily observations (the core alpha-adjacent evidence):**

| Variance proxy | `α̂` (s.e.) | `β̂` (s.e.) | `R²` | `ΔR²` |
|---|---|---|---|---|
| Rolling var. (28-day) **(baseline)** | 0.0329\*\*\* (0.0117) | −1.649 (1.497) | 0.244 | — |
| RCV from EWMA-P2 | 0.0507\*\*\* (0.0125) | −2.032 (1.381) | 0.358 | +0.114 |
| RCV from DRD-HAR-P2 | 0.0580\*\*\* (0.0093) | −1.696 (1.233) | 0.472 | +0.227 |
| RCV from DRD-HAR-P2+ren | 0.0495\*\*\* (0.0094) | −0.886 (1.178) | 0.411 | +0.166 |
| RCV from DRD-HAR-P2+tvSpill | 0.0627\*\*\* (0.0112) | −1.804 (1.257) | 0.447 | +0.202 |
| RCV from DRD-HAR-P2+ren+tvSpill | 0.0500\*\*\* (0.0105) | −0.702 (1.174) | 0.384 | +0.139 |

Source statements tied to this table (§6.1): `α̂` is "highly statistically significant in all cases"; `β̂` is "not significant at the 10% level in any case"; `α̂ > 0` always, "meaning that the predicted peak-load risk premium is generally higher than the baseload risk-premium". Significance stars: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01 (Table 4 note).

**Our count (arithmetic on the printed coefficient/s.e. cells only — not a rerun of the regression):** implied `t = α̂/s.e.` = 2.81 / 4.06 / 6.24 / 5.27 / 5.60 / 4.76 (rows in table order); implied `t = β̂/s.e.` = −1.10 / −1.47 / −1.38 / −0.75 / −1.44 / −0.60, i.e. **0 of 6 skewness coefficients clear |t| = 1.65**; the headline `R²` ratio 0.472/0.244 = **1.93×** (Δ = 0.228).

**Table 1 — out-of-sample RCV forecast losses, 13 model specifications, `n = 2191` days, 1,984 scored origins (2020-04-19 → 2025-09-23), MCS p-values from 21-day stationary block bootstrap with 5,000 reps (§5.1):** columns are `# params | Frobenius | QLIKE | Diag MSE (×10⁸) | Off-diag MSE (×10⁸) | MZ R² | MCS p (T_R-stat) | In-MCS ✓ T_R | ✓ T_max`. Selected rows: `EWMA` 0 / 1.399 / **219.78** / 3.550 / 1.306 / 0.3479 / p 0.000 / no ✓; `EWMA-P2` 4 / 1.338 / 214.33 / 3.334 / 1.251 / 0.4251 / p 0.000 / no ✓; `DRD-HAR (3 horizons)` 6 / 1.309 / 181.08 / 3.434 / 1.217 / 0.3485 / p 0.016 / no ✓; `DRD-HAR-P2 (3 horizons)` 8 / 1.270 / 181.00 / 3.341 / 1.180 / 0.4224 / p 0.031 / ✓; `DRD-HAR (4-h, expanding)` 8 / 1.299 / 180.41 / 3.435 / 1.206 / 0.3734 / p 0.031 / ✓; `DRD-HAR-P` 9 / 1.249 / 180.62 / 3.284 / 1.161 / 0.4060 / p 0.031 / ✓; `DRD-HAR-P2` 10 / 1.263 / 180.47 / 3.343 / 1.172 / **0.4427** / p 0.006 / ✓; `DRD-HAR+ren` 10 / 1.266 / 179.91 / 3.344 / 1.176 / 0.4056 / p 0.168 / ✓ ✓; `DRD-HAR-P2+ren` 12 / 1.288 / **179.75** / 3.375 / 1.197 / 0.4385 / p 0.168 / ✓ ✓; `DRD-HAR-P2+tvSpill` 15 / **1.235** / 180.42 / **3.245** / **1.147** / 0.4339 / p 0.016 / ✓; `DRD-HAR-P2+ren+tvSpill` 17 / 1.278 / **179.65** / 3.339 / 1.189 / 0.4293 / p 1.000 / ✓ ✓; plus the `4-horizon 365-day rolling window` group `DRD-HAR` 8 / 1.364 / 180.94 / 3.730 / 1.261 / 0.3354 / p 0.007 and `DRD-HAR-P2` 10 / 1.341 / 181.00 / 3.790 / 1.235 / 0.3896 / p 0.003 (neither ✓).
Source prose (§5.1): "Benchmark and rolling-fitted models are strictly worse than the rest. In particular, the inclusion of the quarterly component seems necessary." / "Models with renewables included (wind and solar production share) dominate the rest." / renewables are "detrimental to the overall mean-squared loss" while quadratic price controls "greatly benefits the Mincer-Zarnowitz R²" / "the three surviving models achieve a Mincer-Zarnowitz R² of 40–45 %". §5.2 opens with "Of the three models in the T_R-based model confidence set, the principle of parsimony prescribes that the simple DRD-HAR+ren model with 10 parameters is preferable." `underspecified`: the exact mapping of the two printed ✓ columns to `T_R`/`T_max` and an explicit list of "the three surviving models" are not stated in text; the p ≥ 0.10 rows (`DRD-HAR+ren` 0.168, `DRD-HAR-P2+ren` 0.168, `DRD-HAR-P2+ren+tvSpill` 1.000) coincide with the 40–45 % MZ R² claim, but we do not assert the identification.

**Table 2 — variance-targeting calibration on four zero-net-volume spread portfolios, 1,984 origins, 95 % stationary-block-bootstrap CI (block 21, 5,000 reps), MZ Wald with NW HAC maxlag 10 (§5.2):** `Peak-OffPeak`: EWMA-P2 mean VR **1.271** CI [1.100, 1.493] **rejected**, MZ Wald p < 0.001, MZ R² 0.145; `DRD-HAR-P2+ren` 1.056 [0.870, 1.325] ✓ not rejected, p < 0.001, R² 0.144; `DRD-HAR-P2+tvSpill` 1.156 [0.968, 1.415] ✓, p 0.001, R² 0.152; `DRD-HAR-P2+ren+tvSpill` 1.055 [0.865, 1.332] ✓, p < 0.001, R² 0.144. `Solar shape`: EWMA-P2 1.188 [1.062, 1.326] **rejected** (R² 0.391); `+ren` 0.994 [0.869, 1.143] ✓ (0.409); `+tvSpill` 1.087 [0.959, 1.234] ✓ (0.408); full 0.981 [0.857, 1.129] ✓ (0.407). `Wind shape`: EWMA-P2 1.201 [1.049, 1.391] **rejected** (0.254); `+ren` 1.011 [0.847, 1.238] ✓ (0.261); `+tvSpill` 1.101 [0.941, 1.313] ✓ (0.270); full 0.994 [0.832, 1.218] ✓ (0.261). `Morning vs Evening`: EWMA-P2 1.159 [0.998, 1.355] ✓ (0.268); `+ren` 1.079 [0.897, 1.287] (remainder of the row not transcribed here → `data gap` for the unread cells). Source conclusion: all three DRD-HAR models' variance ratios are "statistically indistinguishable from 1", which is **not** the case for EWMA, **but** the Mincer–Zarnowitz Wald null `θ̂ = (0,1)` is **strongly rejected across all models** (p < 0.001 except 0.001 in one cell).

**Table 3 — pointwise 95 % prediction-band coverage for the multivariate covariance forecast of `DRD-HAR-P2+ren+tvSpill` (§5.3):** **overall coverage 0.947 vs nominal 0.950**; by hour 0.965 (h1), 0.963, 0.960, 0.951, 0.954, 0.954, 0.950, 0.947 (h8) … 0.941 (h19) … down to **0.935 (h18)**; on the representative date 2025-08-05 the bootstrapped multivariate band multiplier is **c = 2.84** (Figure 5).

**Figures 6–7 (§6.1):** 28-day rolling mean premia "spike during the crisis periods of 2022 and 2023" with peak-load premium "substantially larger in magnitude, thereby leading to a large and positive spread risk premium"; outside that turbulent period "the spread risk premium tends to fluctuate near zero, with a seemingly seasonal pattern". The RCV-based regression "better tracks the shape of the risk premium, in particular in crisis times, but … it is generally difficult to predict when the spread risk premium turns negative. Negative predictions can only arise from the skewness term (since `α̂ > 0`)". **No Sharpe, drawdown, turnover, hit rate, P&L or capacity figure is printed anywhere in v1** — the paper is a forecast/fit comparison, not a backtest.

### Independently reproduced

`not independently reproduced.`

(What this run actually did: read the arXiv landing page and the complete pinned v1 HTML end-to-end; located every quoted number in its printed Table/Figure/Section; ran a full-text transaction-cost/risk-metric keyword scan on the pinned v1; performed whole-repository source-identity dedup; computed implied t-statistics from the printed Table 4 cells. **No ENTSO-E or EEX data was downloaded, no regression was re-estimated, no formula was implemented, no backtest was run.**)

### Negative evidence

1. **No cost, fill, spread, impact, borrow, financing, margin or latency model exists anywhere in v1** (keyword scan above) → every economic claim is gross-of-undefined-cost, `data gap`, **not** zero-cost.
2. **No risk or performance metric at all:** zero occurrences of Sharpe, drawdown, turnover, win rate, P&L, capacity. There is no strategy result to inherit — only an in-sample fit comparison.
3. **The premium regression is in-sample:** `α̂, β̂` are estimated over the full 1,358 observations with no rolling/expanding or held-out evaluation of the premium forecast (our reading of §6.1 + Table 4 caption). The RCV inputs are out-of-sample; the premium mapping is not.
4. **The skewness leg is dead:** our count on Table 4 → 0 of 6 `β̂` reach |t| = 1.65 (max |t| = 1.47), which the source itself states ("not significant at the 10% level in any case"). Since negative predictions "can only arise from the skewness term", the specification **cannot** predict negative spread risk premia (source, Figure 7 discussion).
5. **Level miscalibration persists:** Table 2 MZ Wald rejects `θ̂ = (0,1)` for **all** models (source) — variance ratios near 1 do not translate into unbiased levels; the source attributes this to the extreme right-skew of realized variance and models being "not sufficiently reactive during crisis times".
6. **Structural forecast floor:** Figure 2 discussion — forecasts have a floor and are "essentially unable to meaningfully capture the correlation structure on very calm days", i.e. exactly the low-volatility regime where the premium is near zero.
7. **Regime concentration:** Figure 6/§6.1 — economic value sits almost entirely in the 2022–2023 energy-crisis spike; the premium "fluctuates near zero" otherwise. A single 5.6-year futures sample containing one such episode cannot separate a durable premium from a crisis artefact.
8. **Overlapping observations:** the source itself notes many daily rows share the same front contract (`F_t, F_{t+1}, …` on one underlying) and applies NW bandwidth 60 to cope; effective independent information is far below 1,358.
9. **Proxy horizon mismatch (source's own caveat):** weekly `RCV̂⁷` is used as a stand-in for a monthly delivery-period variance ("does not align … approximately", §6.1).
10. **Ad-hoc DST imputation** (average of adjacent hours / merging overlapping hours) is a data-handling choice that can distort intra-day covariance exactly where the peak/baseload weights differ (hours 8–19 vs 24h).
11. **No code, no replication package, no data-availability statement**; ENTSO-E data are revised retroactively; EEX contract identifiers and vendor are unstated → independent replication requires undocumented choices.
12. **Preprint only, single v1, no peer review** (no journal-ref, no comments field, no publisher DOI).
13. **No multiplicity control** over the 6 Table-4 specifications × 2 proxy families or the 13-model Table-1 horserace (our count); model selection ("best … DRD-HAR-P2") is done on the same table it is reported in.
14. **Source-internal numeric inconsistency** recorded in `contradictions`: §5.1 "35 %–48 %" vs printed maximum `R² = 0.472`.
15. **Baseline already fits well:** `R² = 0.244` for the 28-day rolling-variance baseline, so the incremental claim (`ΔR²` up to +0.227) is an improvement on an already-in-sample-fit regression — not evidence of tradable excess return.
16. **Economic direction is a hedging-premium story, not a forecasting edge:** the trade implied by `α̂ > 0` is selling variance risk to hedgers in crisis states; the paper reports no test that this compensation exceeds trading costs.
17. **Publication/point-in-time gap:** day-ahead price and renewable-share availability timestamps are never stated, so a real-time replication could silently use same-day information.

## Falsification plan

Every threshold below is **`research-defined`** (Scout-chosen, not from the source); every trading choice is **`research-proposed`**. Data: ENTSO-E German day-ahead hourly prices + wind/solar shares + EEX German monthly peak-load/baseload front futures. Action on failure: mark this hypothesis weakened/failed in this record and **do not** advance any implementation; data unavailable → record `not run`, never `pass`.

- **F1 — Independent replication:** rebuild the RCV pipeline and Table 4 from a second, independently sourced futures feed (different vendor or exchange export). `research-defined` failure rule: `α̂` for the DRD-HAR-P2 row loses significance (NW t < 2.0) or `R²` drops below 0.35 → headline not reproducible.
- **F2 — True out-of-sample premium test (addresses Negative evidence #3):** estimate `α̂, β̂` on a rolling past-only window (e.g. expanding with a 365-day minimum) and forecast `SRP` into the next 30 days. `research-defined` failure rule: OOS `R² ≤ 0`, or OOS `R²` does not exceed the 28-day-rolling-variance baseline's OOS `R²` by ≥ 0.05 → the RCV increment does not survive outside the sample it was fit on.
- **F3 — Cost ladder:** long peak / short baseload front contract (equal notional), net of 0/1/2/5/10 bp per side plus observed bid-ask and exchange+broker fees, 20 % participation cap. `research-defined` failure rule: net premium capture ≤ 0 at **5 bp per side**, or net Sharpe < 0.5 → not tradable.
- **F4 — Sign-rule strategy test (`research-proposed` rule):** daily, hold the peak-vs-baseload spread while the past-only predicted `SRP > 0`, flat otherwise, enter next session, exit at delivery start or sign flip. `research-defined` failure rule: net-of-cost Sharpe < 0.5, or the strategy is not profitable in ≥ 3 of the 5 sample years → strategy layer fails even if the regression holds.
- **F5 — Crisis-dependence check (addresses Negative evidence #7):** re-run F1 excluding 2022-03-01 → 2023-12-31. `research-defined` failure rule: `α̂` NW t < 2.0 **or** `ΔR²` < 0.05 outside the crisis window → mechanism is crisis-only and must be relabeled as such in this record.
- **F6 — Placebo:** circular-shift / block-date-shuffle the RCV forecast series relative to `SRP` 1,000 times. `research-defined` failure rule: the observed `ΔR²` gain does not exceed the placebo distribution with |z| ≥ 2.0 → the increment is not date-aligned information.
- **F7 — Ablation against "any variance forecast works":** replace `RCV̂` with a univariate EWMA/GARCH variance of the same peak-minus-baseload spread (matched parameters). `research-defined` failure rule: DRD-HAR no longer adds `ΔR² ≥ 0.10` over that matched univariate proxy → the *matrix/RCV* construction (as opposed to variance forecasting in general) carries no incremental content.
- **F8 — Skewness-repair test (addresses Negative evidence #4):** substitute a genuine conditional-skewness proxy (e.g. forecast third moment or option/implied analogue where available) for the 28-day rolling skewness. Success requires the model to reproduce sign changes of `SRP` (the source cannot); `research-defined` failure rule: negative-`SRP` sign hit rate ≤ 50 % → the "risk-premium" story remains variance-only.
- **F9 — Multiplicity control:** apply Benjamini–Hochberg at `q < 0.10` across the full printed grid (6 Table-4 specifications, and separately the 13 Table-1 models). `research-defined` failure rule: fewer than half of the RCV rows survive → selection artefact.
- **F10 — Capacity/liquidity:** verify EEX front-month open interest/volume supports a position at ≤ 20 % of average daily volume with the F3 cost ladder. `research-defined` failure rule: capacity shortfall or cost ladder failing at 2 bp → hypothesis may be real but is not implementable at size.

## Crypto portability

**unproven.**

- **Why not `direct`:** the source demonstrates the mechanism only in European physical-power futures; it contains zero crypto evidence.
- **What does not port:** peak-load (hours 8–19) vs baseload (24h) delivery definitions, a mandatory day-ahead auction, weather/demand-driven conditional variance with strong intraday seasonality, and a single standardized exchange product pair with a shared delivery-period underlying. Crypto has no comparable two-leg delivery-spread product.
- **Closest analogues (speculative, untested):** perpetual-funding term structure vs quarterly-basis spreads, and options-IV variance risk premia — i.e. a "conditional variance is priced into the term/basis structure" hypothesis. These are **ported hypotheses, not crypto empirical evidence**, and they inherit different dynamics: 8-hour funding accrual, 24/7 sessions with no auction clock, venue-fragmented and manipulable index/mark prices, thin single-venue liquidity, contract-specification and listing churn differences, timestamp/candle-boundary differences, and unmodeled borrow/liquidation on the short leg.
- Crypto portability is **not** authorization to trade.

## Limitations

- `underspecified`: EEX contract identifiers, quotation/settlement convention, front-contract/roll rule, tick size, liquidity/open interest; renewable-generation-share data vendor; price and forecast availability timestamps and timezone; identity of "the three surviving models" and the ✓-column mapping in Table 1; unread Table 2 cells for the "Morning vs Evening" block beyond the first two rows.
- `data gap`: no cost/fill/impact/margin model; no code or replication package; no risk metrics; no out-of-sample premium evaluation; ENTSO-E revision policy not discussed; Benth's full affiliation list beyond BI Norwegian not printed in the header block we read.
- `not independently reproduced`: every number above is source-reported from the pinned v1; no data was downloaded and nothing was re-estimated.
- `unproven`: tradability, capacity, net-of-cost value, and crypto portability.
- **Incremental-write / dedup position:** this capture is a new family for the repository (forward-spread risk-premium prediction from matrix-RCV forecasts) with a distinct source identity, distinct mechanism and distinct universe from the existing day-ahead/intraday electricity records listed below; the whole-repo dedup audit above found **0** existing hits on this source.

## Implementation status

`implementation_status: not-implemented`.

No implementation of this record exists in our research stack: no RCV/matrix-HAR pipeline, no EEX/ENTSO-E data ingestion, no premium regression, no backtest, and no candidate-pool entry. This record does **not** imply Qlib full-backtest validation, and does **not** imply Paper, Testnet or Live verification of any kind — none of those stages has been reached or initiated.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`.

The presence of this record in the staging repository means only that normalized, source-traceable research material exists here. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count, confidence value or schedule behavior in this record promotes it.

## Related Wiki records

- Pre-write `kb_search` in Hermes Wiki Brain: `"electricity forward spread risk premia"` → **0 results**; `"electricity day-ahead price forecasting battery arbitrage"` → **0 results**; `"realized covariation matrix HAR volatility forecasting"` → 1 unrelated hit (`quant/path-portfolio-optimization-signature-defect-lift-2026-09-02.md`, path-signature portfolio construction, different source and mechanism); `"electricity"` → 4 hits, none covering forward risk premia or realized covariation. **No stable Wiki Brain page for this mechanism is known, so no Wiki link is asserted.**
- Related records in this repository (adjacent material, different source identities and mechanisms — listed as plain file references, not Wiki links):
  - `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md` — arXiv:2609.23223; temporal-hierarchy reconciliation of day-ahead hourly/spread forecasts for a 1 MWh battery (Germany/Spain day-ahead).
  - `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23.md` — GitHub `CodingxFaisal/power-spread-trader`; 20-day z-score mean reversion on seven EPEX/Nord Pool bidding zones, daily baseload bars.
  - `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22.md` — arXiv:2609.23598; orderbook deep learning on the continuous German **intraday** market.
- Reference works cited *by the source* (not separate sources we verified): Bessembinder and Lemmon (2002); Redl et al. (2009); Corsi (2009); Quiroz et al. (2024); Hansen et al. (2011) MCS; Patton (2011); Kloster and Benth (2026) (the RCV estimator companion paper — **not looked up**, recorded as `data gap`).

## Sources

1. Thomas K. Kloster and Fred Espen Benth. *"Forecasting of volatility and risk premia in electricity markets."* arXiv:2606.05991v1 [q-fin.GN; econ.EM], submitted **Thu, 4 Jun 2026 10:38:46 UTC** (only version). CC BY 4.0. https://arxiv.org/abs/2606.05991 — DOI: https://doi.org/10.48550/arXiv.2606.05991 (resolves 200). Full text read: https://arxiv.org/html/2606.05991v1 (HTTP 200, 343,431 bytes, retrieved 2026-09-24). All quantitative claims in this record trace to **Abstract; §§2–6.1, 7–9; Eqs. 13–20; Tables 1–4; Figures 1–7** of that pinned v1 and are labeled source-reported; implied t-statistics and the 0.472/0.244 ratio are our own arithmetic on printed cells, labeled "our count".
2. ENTSO-E Transparency Platform — https://transparency.entsoe.eu — named by the source as the public day-ahead price source (§5); not independently fetched for this record.
3. EEX (European Energy Exchange) — named by the source as the venue for the German monthly peak-load/baseload futures (§6.1); contract identifiers `data gap`.
