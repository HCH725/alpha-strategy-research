---
schema: strategy-research-record-v1
title: "Put–Call Parity Carry Gap with Physical-Drift Margin-Burden Term (SPX/RUT Index Options): r·μ̂·τ Explains the Option-Implied vs OIS Discount Wedge"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - index-options
  - put-call-parity
  - carry-gap
  - option-implied-discount-factor
  - physical-drift
  - implementation-premium
  - limits-to-arbitrage
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-05-24
sources:
  - "Useong Shin, 'The P behind Q: Empirical Evidence from Physical Drift in Put–Call Parity', arXiv:2605.12250v5 [q-fin.GN], v1 Tue 12 May 2026 15:19:55 UTC, v5 Sun 24 May 2026 10:33:31 UTC, CC BY 4.0. https://arxiv.org/abs/2605.12250"
  - "Full-text HTML of the pinned version (v5), read 2026-09-24: https://arxiv.org/html/2605.12250v5"
  - "DOI: https://doi.org/10.48550/arXiv.2605.12250 (resolves 200 to the abs page, checked 2026-09-24)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Put–Call Parity Carry Gap with Physical-Drift Margin-Burden Term (SPX/RUT Index Options): r·μ̂·τ Explains the Option-Implied vs OIS Discount Wedge

## Provenance

- **Primary source:** Useong Shin (sole author), *"The P behind Q: Empirical Evidence from Physical Drift in Put–Call Parity"* (`source-reported`).
- **Author line exactly as source:** Useong Shin — Sogang Business School, Sogang University (Seoul, Korea); ORCID 0009-0003-0197-9003; email useong@sogang.ac.kr (HTML title block). Single author; no co-authors.
- **Version / date:** `arXiv:2605.12250v5 [q-fin.GN] 24 May 2026` printed in the HTML header. Submission history on the abs page: v1 Tue 12 May 2026 15:19:55 UTC (441 KB), v2 Wed 13 May 2026 07:37:06 UTC (441 KB), v3 Mon 18 May 2026 09:24:00 UTC (4,547 KB), v4 Tue 19 May 2026 13:25:29 UTC (4,547 KB), v5 Sun 24 May 2026 10:33:31 UTC (4,544 KB, submitter Useong Shin). `arxiv.org/html/2605.12250v6` returns **404 → v5 pinned** (checked 2026-09-24).
- **Title-block date line prints August 24, 2026** — later than the v5 stamp → recorded as a rendering artifact, not a version (`source-reported`).
- **Subjects:** General Finance (**q-fin.GN**) primary; no secondary subject class listed on the abs page.
- **Comments / Journal-ref / DOI field on abs page:** Comments field **absent**, Journal reference **absent**, publisher DOI **absent** → **preprint only**; peer-review status `not stated in source`. arXiv DataCite DOI `10.48550/arXiv.2605.12250` resolves (HTTP 200 → abs page) as checked 2026-09-24. License **CC BY 4.0** (HTML header).
- **JEL / keywords (source-reported, title block):** JEL G12, G13, G14; keywords *carry gap; put–call parity; physical drift; path risk; P–Q tension; limits to arbitrage*.
- **Funding (source-reported, Funding section):** "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors." **Declaration of interest:** no competing interests. **AI-usage declaration (source-reported):** the author used ChatGPT (OpenAI) and Claude (Anthropic) for language refinement and structural clarity; all outputs reviewed/edited by the author, who takes full responsibility. **Acknowledgment (source-reported):** gratitude to Michele Azzone (Politecnico di Milano) for *generously sharing OIS data*, guidance on the implied-discount-factor pipeline, and feedback.
- **Universe:** European-style **SPX and RUT index options** (no weeklies/flex split stated → `data gap`), minute-level NBBO quotes from **ThetaData**; benchmark = bootstrapped **daily OIS curve** (`source-reported`, §4.1 and Appendix A.1–A.3).
- **Sample period:** common OIS-matched sample **January 2016 – October 2025** (`source-reported`, §6.3 prose and Figure 6.2 caption); **2,456 trading days (SPX), 2,455 (RUT)**; panel = **48,013** market–date–maturity observations pooled, **29,368 SPX**, **18,645 RUT** (`source-reported`, Table 5.1).
- **Stable URLs:** https://arxiv.org/abs/2605.12250 · full text https://arxiv.org/html/2605.12250v5 · DOI https://doi.org/10.48550/arXiv.2605.12250.
- **Companion/baseline source dependency:** the paper's baseline (the `r·σ·√τ` GBM support-capital model and the motivating Figure 1.1 wedge) is attributed to and partly **reproduced from** *Shin, U. (2026), "The Cost of a Free Lunch," SSRN Working Paper No. 6407379* (`https://dx.doi.org/10.2139/ssrn.6407379`) — a **different source identity** that is not itself recorded in this repository.
- **Dedup audit (pre-write, entire repository, not `git log`):** hidden-inclusive `find . -name "*.md"` = **2,509** files, plus `coverage_manifest.csv` (**5,808 lines**), searched for `2605.12250`, `10.48550/arXiv.2605.12250`, exact title *The P behind Q*, *Physical Drift in Put*, `Useong Shin`, `carry gap`, `6407379`, `Cost of a Free Lunch`, `ThetaData`, `Azzone`, `synthetic forward`, `implementation hurdle`, `drift burden`, `margin burden` → **zero hits for the source identity** (`2605.12250` / DOI / title: 0 in `*.md` and 0 in `coverage_manifest.csv`). The **only `Useong Shin` hit** is the materially distinct record `option-funding-basis-year-end-boundary-wedge-spx-rut-box-implied-2026-09-22.md` (**different arXiv ID 2609.20224**, submitted 21 Aug 2026, i.e. *after* this pinned v5): that record studies a **fixed ~2–3 bp December-31 calendar-boundary price wedge**, whereas this record studies a **continuous physical-drift (r·μ̂·τ) margin-burden loading on the level/time-variation of the carry gap** — distinct source identity **and** distinct mechanism (four-axis distinction stated below). `ThetaData` hits three other options records (equity earnings-IV, index dispersion, put-call-parity borrow-dividend) all using an EOD option lake on single-name/ETF universes with different mechanisms; `Azzone` hits one unrelated climate record plus the Year-End Toll record's citation of Azzone & Baviera (2021); `carry gap` and `6407379`/`Cost of a Free Lunch` return **0** repository hits.
- **Four-axis material distinction vs nearest neighbors:** (1) vs `option-funding-basis-year-end-boundary-wedge-spx-rut-box-implied-2026-09-22` (same author, different paper 2609.20224): **mechanism** discrete Dec-31 reporting-boundary jump vs **continuous drift-sensitive margin burden**; **horizon/regime** Q4 boundary-local design vs full-sample time-series regression; **signal construction** boundary indicator h(t,T) vs 504-day prior rolling-OLS drift slope regressor. (2) vs `put-call-parity-implied-borrow-dividend-confounding-falsification-2026-09-13`: borrow/dividend confounding of parity-implied rates vs **enforcement-capital/path-risk** loading; different universe treatment and different regressors. (3) vs `bitcoin-ibit-options-cme-futures-implied-carry-wedge-2026-09-01`: ETF-vs-futures basis carry in a crypto-linked wrapper vs **option-implied vs OIS discount wedge** in equity index options (this mechanism is also the sole Wiki Brain retrieval hook found). (4) vs `cross-predictive-sdf`/option-implied-SDF-family records: discount-factor *estimation for premium forecasting* vs *parity-enforcement cost explanation* — different dependent object (carry gap vs equity premium).
- **Wiki Brain `kb_search` (read-only, no writes):** `put-call parity carry gap option-implied discount factor implementation premium` → **0 results**; `put-call parity option-implied rate synthetic forward box margin` → **1 result**, `quant/bitcoin-ibit-options-cme-futures-implied-carry-wedge-2026-09-01` (listed below as a real existing page; **no Wiki page for this mechanism is asserted**).
- **As-of date:** source/data as-of **2026-05-24** (v5 submission date); primary source opened and full text read **2026-09-24**.

## Economic mechanism

### Source-reported

Put–call parity is exact as a **terminal-payoff identity** (Stoll 1969; Black–Scholes 1973; Merton 1973; Gould–Galai 1974), but the *trading strategy that enforces it before maturity is path-dependent and capital-using* (§2). The paper's object is the **carry gap**: `CG_t(T) = (1/τ)·log( D_t^OIS(T) / B̂_t(T) )`, the annualized log wedge between the OIS benchmark discount factor and the **option-implied** discount factor `B̂` recovered with the synthetic-forward cross-sectional procedure of Azzone & Baviera (2021) (§4.1, Eq. 7–8; Appendix A.2–A.3). Quoted price-space parity residuals are tightly compressed, yet the OIS-discounted synthetic-forward vs traded-futures channel retains a systematic wedge (Figure 1.1, **reproduced from Shin 2026, SSRN 6407379**); the author interprets the wedge as an **implementation premium under finite arbitrage capital** (Abstract; §1; §7.2).

Two parity-enforcement directions, `+C−P−F` and `−C+P+F`, deliver the same terminal relation but carry **opposite futures-leg exposure before maturity**, so daily variation margin makes the burden asymmetric across the two sides (§3.1 motivating Alice/Bob example). Under a zero-drift Brownian approximation of interim P&L, minimum support capital is the running maximum of adverse P&L with `E[ℓ_u] = σ√(2u/π)`, giving average burden `(2/3)·σ√(2τ/π)` and, at opportunity-cost rate `r`, the **baseline `r·σ·√τ` path-risk term** (§3.2, Eq. 1, `GBM^{σ,OIS,xY}` scaled by one-year and ten-year OIS rates, with `Vol = VIX` for SPX and `RVX` for RUT). **Preserving physical drift** in the same support-capital calculation (first-order expansion of the expected running maximum of Brownian motion with drift, §3.3) adds a directional component: `r_t·B̄^(q)(τ) = r_t·(2/3)·σ√(2τ/π) − (q/4)·r_t·μ·τ + O(μ²τ^{3/2}/σ)`, i.e. the theory motivates a first-order **directional margin-burden regressor proportional to `r·μ·τ`** (§3.3, Eq. 2). Because true drift `μ` is unobserved, the empirical term uses `μ̂` = **prior-only rolling-OLS slope of the log total-return index**, annualized ×252: `GBM^{μ̂,OIS,1Y} = 10⁴ · (OIS1Y_t/100) · μ̂_i,t^ann · τ_i,t` (Eq. 10–11, 15, 17). The source is explicit that `μ̂` is a **reduced-form historical-drift proxy, not an observed expected return or structural estimate of μ**, and that the result does **not** mean physical drift prices option payoffs — it enters *the capital-using process that enforces risk-neutral parity* (Abstract; §7; §8).

### Research interpretation

Falsifiable hypothesis: **the level and time-variation of the option-implied-vs-OIS carry gap in SPX/RUT index options load positively and stably on a maturity-scaled, one-year-OIS-scaled trailing physical-drift proxy after controlling for `r·σ·√τ` diffusion path risk, median bid–ask/τ trading frictions, and NFCI financial conditions** — i.e. enforcement capital is *directionally* burdened, not only diffusively burdened. This is a **friction/implementation-cost measurement mechanism**, not a directional forecast of the index and not (in the source) a trading strategy. The source is a **fit/explanatory-power study** (R², RMSE, MAE, HAC coefficients); it reports **no PnL, no Sharpe, no backtest**. Any trade construction — e.g. the source's own §7.3 suggestion that an observed parity residual be compared against a model-implied **price-space implementation hurdle** `Ĥ = F·τ·CĜ/10⁴` — is explicitly **`research-proposed`**; the source states outright "This is not a mechanical trading rule" (§7.3).

Component roles if operationalized (all `research-proposed`, none source-reported as a strategy):

```text
Measurement (source-reported): synthetic-forward carry gap CG^bp = 10^4·(1/τ)·log(D^OIS/B̂)
Regressor block (source-reported): r·σ·√τ terms (OIS 1Y/10Y, VIX/RVX) + BA^med/τ + NFCI
Added signal term (source-reported): r·μ̂·τ drift burden, 504-day prior-only rolling slope
Entry/exit/size/hold (research-proposed only): none exists in the source — data gap
```

## Signal

**The source specifies a measurement/regression signal, not a trading signal.**

- **Formation timestamp (source-reported):** daily market–date–maturity panel; daily variables (`OIS_t`, `NFCI_t`, `Vol_i,t`, `μ̂_i,t`) are matched to all maturity cells observed on the same date `t`; `τ_i,t = T − t` in years (§3, notational paragraph). Timezone / exchange-calendar convention for "date" is **not stated → data gap** (exchange-traded Cboe index options implied).
- **Carry-gap construction (source-reported, §4.1 + Appendix A.2–A.3):** for each date–maturity cell, form matched call–put pairs at the same strike/maturity; synthetic forward `𝒢 = C − P` from mid quotes; jointly estimate `B̂` and `F̂` from the strike cross-section of `𝒢` (no external dividend input required); bootstrap the daily OIS curve and maturity-match it; `CG^bp = 10⁴·(1/τ)·log(D^OIS/B̂)`. Daily market-level series use the **within-date median** across maturity cells (Appendix A.4).
- **Drift proxy (source-reported, §6.1, Eq. 13–14):** regress `log TR_{t−n+ℓ}` on `ℓ = 0…n−1` using **only information through `t−1` (explicit look-ahead guard)**; annualize slope ×252. **Main horizon `n = 504` trading days for both markets** (common across markets to restrict flexibility); horizon scan (Figure 6.1) reports pointwise LOYO-pooled OOS optima of **542 (SPX), 514 (RUT), 525 (two-market average)** days, with the 504-day choice costing negligible OOS R² (0.310 vs 0.314 SPX optimum; 0.188 vs 0.189 RUT; 0.249 vs 0.250 average).
- **Estimation (source-reported):** **separate-market** OLS (baseline Eq. 9 / extended Eq. 12, 16); baseline regressors `GBM^{σ,OIS,1Y}`, `GBM^{σ,OIS,10Y}`, `BA^med/τ`, `NFCI`; extended model adds **only** `GBM^{μ̂,OIS,1Y}` (ψ). A pooled common-slope + SPX-dummy variant is reported for the baseline only (Table 5.1/5.2).
- **Inference (source-reported):** date-based **HAC (Newey–West) with maximum lag 21 trading days** (§4.3; table notes); stars *** / ** / * = 1% / 5% / 10%.
- **Evaluation (source-reported, §4.3 + Appendix A.5):** in-sample R², adjusted R², RMSE, MAE; **leave-one-year-out (LOYO)** OOS R², RMSE, MAE, fitted–actual correlation over 10 holdout years (2016–2025); LOYO training samples contain ~2,200 trading dates.
- **Entry / short entry / exit / holding period / re-entry / position sizing / multi-timeframe / order timing:** **none specified anywhere in the source — data gap.** Any downstream threshold, entry, exit, stop, sizing, or fill rule must be labeled `research-proposed`.
- **Reproducibility of the *measurement* signal:** fully specified at equation level (thresholds for the quote filters are not printed → see Required data). **Reproducibility of any *trading* signal:** underspecified (no trading signal exists in the source).

## Required data

- **Instrument / universe (source-reported):** European-style SPX and RUT index options; matched call–put pairs by strike and maturity; maturity buckets used for reporting run **1–2m, 2–3m, 3–5m, 5–7m, 7–10m, 10–14m, 14–21m, 21m+** (Table 6.2). Contract/weekly-vs-monthly split and explicit DTE filter are **not stated → data gap**.
- **Venue / market type (source-reported):** U.S. index options on the underlying Cboe-listed series (SPX, RUT) — the paper says "European-style index options on SPX and RUT" without naming the exchange or vendor venue field; **market type = index options**. Venue field/vendor brand for the quotes = **ThetaData** (§4.1, Appendix A.1, reference entry "Historical SPX and RUT option NBBO data, retrieved April 3, 2026").
- **Fields (source-reported):** minute-level NBBO option quotes (bid/ask/mid, strike, maturity, date); bootstrapped **daily OIS curve** and maturity-matched OIS discount factors; **OIS 1-year and OIS 10-year rates**; **VIX** (SPX) and **RVX** (RUT); **NFCI** (FRED, Chicago Fed National Financial Conditions Index, "retrieved from FRED … April 3, 2026"); **SPX and RUT total-return indices** for the drift proxy (vendor **not stated → data gap**); median bid–ask `BA^med` per market–date–maturity. Reference entry **Databento (2026) "Historical ES and RTY futures BBO data, retrieved April 3, 2026"** appears in the bibliography; its exact role in *this* paper's figures vs the companion paper is **`underspecified`** (the traded-futures channel figure is reproduced from Shin 2026).
- **OIS data provenance:** the acknowledgment thanks Michele Azzone for **sharing OIS data**; the OIS curve **provider/tenor set is not named → data gap** (bootstrapping procedure described in Appendix A.3).
- **Point-in-time (source-reported):** drift proxy computed only from information through `t−1` at each date `t` (explicit anti-look-ahead statement, §4.2/§6.1/A.5); OIS and daily regressors matched to same-date maturity cells; NFCI/FRED series as retrieved April 3, 2026. The **LOYO evaluation is explicitly *not* a real-time forecast**: training includes years *after* the holdout year (source-disclosed, §6.3).
- **Timestamp / timezone:** exchange-date alignment convention delegated, not restated → `data gap`.
- **Missing data (source-reported filters, Appendix A.4 / §4.1):** drop observations without a valid same-strike same-maturity call–put pair; drop **extremely low prices**; drop **excessive bid–ask spreads**; drop date–maturity cells with **too few valid strikes**; drop dates where **OIS curve construction fails**. **Numeric thresholds are not printed → `underspecified`** (a reproducer must choose and label them `research-proposed`). Daily aggregation = median across valid maturity cells.
- **Funding/fee/spread needs:** bid–ask enters (a) as a sample filter and (b) as the regressor `BA^med/τ` (an execution-friction *control*, positive and significant: 0.158***/0.256***/0.130*** baseline, Table 5.2) — **not** as a trading-cost model. Maker/taker fees, commissions, slippage, borrow, financing charges, and capacity are **not modeled → `not stated in source`** (never read as zero-cost).

## Execution assumptions

- **The source performs no trade simulation.** Order type, fill model, latency, signal-to-order delay, participation cap, position limits, leverage/margin modeling for a position, shorting/borrow availability, failure handling: **all `not stated in source`**. Keyword scan of the pinned v5 full text (2026-09-24): `slippage` 0, `latency` 0, `commission` 0, `market impact` 0, `turnover` 0, `backtest` 0, `round-trip` 0, `PnL` 0, `leverage` 0, `fees` 0 (both `fee` hits are the substring in "feedback"), `Sharpe` 0 real hits (both matches are the substring in "sharper"), `drawdown` 0, `win rate` 0, `fill` 0; `transaction cost`/`transaction costs` 2 hits = one literature sentence (§2) and the Gould–Galai (1974) reference title; `bid–ask` (en dash) 4 hits = quote filter, `BA^med/τ` regressor, and §7.3 caveat; `margin` 46 hits = the paper's *mechanism* (variation margin), not a margin-model for a backtest. **No fee, spread-cost, slippage, borrow, financing, impact, fill, or capacity model exists → `data gap`, not zero.**
- **Source-reported qualitative execution caveats (§7.3):** "Actual profitability also depends on bid–ask spreads, execution risk, margin rules, financing spreads, balance-sheet costs, inventory constraints, and model error"; the fitted carry gap is a **"reduced-form screening heuristic"**, not a mechanical rule. §1 likewise frames the wedge as the residual cost of maintaining compressed parity when *arbitrage capital, funding, margin capacity, and execution liquidity are finite*.
- If a researcher operationalizes a hurdle-based parity trade, **every** element (threshold multiple over `Ĥ`, entry price, legs, order type, fill assumption, cost ladder, sizing, holding to expiry, exit) is `research-proposed`.

## Evidence

### Source-reported

All figures below are `source-reported` from arXiv:2605.12250v5, **fit/regression evidence only — there is no strategy PnL anywhere in the paper**, and none has been independently reproduced.

1. **Baseline in-sample fit (Table 5.1):** pooled common + SPX dummy R² **0.309** / adj 0.309 / RMSE **13.57 bp** / MAE **9.26 bp** (48,013 obs; 2,456 days); SPX separate R² **0.312** / 0.312 / **13.20** / **8.68** (29,368 obs); RUT separate R² **0.281** / 0.281 / **13.95** / **10.10** (18,645 obs; 2,455 days).
2. **Baseline coefficients, HAC(21) (Table 5.2), columns = pooled / SPX / RUT:** intercept **24.901\*\*\* (5.816) / 23.134\*\*\* (5.713) / 24.577\*\*\* (5.407)**; `GBM^{σ,OIS,1Y}` **−0.557\*\*\* (0.148) / −0.548\*\*\* (0.170) / −0.555\*\*\* (0.124)**; `GBM^{σ,OIS,10Y}` **0.469\*\*\* (0.151) / 0.411\*\* (0.172) / 0.541\*\*\* (0.130)**; `BA^med/τ` **0.158\*\*\* (0.029) / 0.256\*\*\* (0.064) / 0.130\*\*\* (0.022)**; `NFCI` **−24.598\*\* (10.283) / −25.839\*\* (10.359) / −23.961\*\* (10.013)**.
3. **Baseline LOYO (Table 5.3):** common-market SPX mean R² **0.049**, median **0.187**, pooled **0.212**, years with R²>0 **9/10**, mean corr **0.189**, mean RMSE **13.93 bp**; common-market RUT **0.065 / 0.063 / 0.173 / 6/10 / 0.252 / 15.16**; separate SPX **0.059 / 0.130 / 0.221 / 7/10 / 0.205 / 13.95**; separate RUT **0.075 / 0.108 / 0.171 / 6/10 / 0.243 / 15.07**. Baseline LOYO sign stability (Table 5.4): all four non-intercept regressors keep sign 10/10 folds in both markets (SPX `GBM^{σ,1Y}` significant at 5% in 9/10 folds; `GBM^{σ,10Y}` 8/10; RUT all three main terms 1% in 10/10).
4. **Horizon scan (Figure 6.1 + §6.1 prose):** pointwise LOYO-pooled OOS optima **542 / 514 / 525** trading days (SPX / RUT / average); at the chosen **n = 504**, OOS R² **0.310 vs 0.314** (SPX opt), **0.188 vs 0.189** (RUT opt), **0.249 vs 0.250** (average opt).
5. **In-sample, baseline → drift-extended (Table 6.1):** **SPX** R² **0.3124 → 0.3475** (Δ **+0.0350**), adj R² **0.3123 → 0.3473**, ΔRMSE **−0.341 bp**, ΔMAE **−0.364 bp**; **RUT** R² **0.2809 → 0.2869** (Δ **+0.0060**), adj **0.2807 → 0.2867**, ΔRMSE **−0.058 bp**, ΔMAE **−0.061 bp**.
6. **In-sample by maturity bucket (Table 6.2; Δ = extended − baseline; our arithmetic on printed cells, labeled `our count`, not a rerun):** SPX ΔR² **+0.005 (1–2m, n=2,472), +0.013 (2–3m, 2,377), +0.027 (3–5m, 4,501), +0.057 (5–7m, 3,702), +0.060 (7–10m, 5,263), +0.042 (10–14m, 6,067), +0.049 (14–21m, 3,751), +0.106 (21m+, 1,235)** with ΔRMSE negative in **8/8** buckets. RUT ΔR² **+0.001, +0.001, +0.005, +0.028, +0.041, +0.020, −0.013, −0.052** → positive in **6/8**, **negative in the two longest buckets** (14–21m and 21m+). Bucket obs sums check to Table 5.1 totals (SPX 29,368; RUT 18,645).
7. **Year-by-year LOYO OOS R² (Table 6.3; baseline → extended):** **SPX** 2016 0.185→0.178, 2017 0.074→−0.016, 2018 0.221→0.211, 2019 0.023→0.065, **2020 −1.221→−0.748**, **2021 0.416→0.733**, 2022 0.357→0.391, 2023 0.571→0.680, 2024 −0.016→0.161, 2025 −0.022→0.053 → improves **7/10** years (source prose agrees). **RUT** 2016 −0.350→−0.304, 2017 −0.152→−0.218, 2018 0.213→0.233, 2019 −0.041→−0.060, 2020 −0.587→−0.533, 2021 0.477→0.522, 2022 0.308→0.271, 2023 0.661→0.692, 2024 0.153→0.187, 2025 0.064→0.059 → improves **6/10** years.
8. **LOYO summary (Table 6.4):** SPX baseline mean/median/pooled R² **0.059 / 0.130 / 0.221**, mean RMSE **13.947 bp** → extended **0.171 / 0.169 / 0.310**, **13.100 bp**; RUT baseline **0.075 / 0.108 / 0.171**, **15.075 bp** → extended **0.085 / 0.123 / 0.188**, **14.930 bp**.
9. **Main coefficients of the added term, HAC(21) (Table 6.5):** `GBM^{μ̂,OIS,1Y}` = **ψ = 0.119\*\*\* (0.020) SPX**, **0.054\*\*\* (0.018) RUT**; accompanying rows (SPX baseline→extended; RUT baseline→extended): intercept 23.134\*\*\*→27.475\*\*\*; 24.577\*\*\*→25.859\*\*\*; `GBM^{σ,OIS,1Y}` −0.548\*\*\*→−0.473\*\*\*; −0.555\*\*\*→−0.467\*\*\*; `GBM^{σ,OIS,10Y}` **0.411\*\*→0.125 (n.s.) SPX**; 0.541\*\*\*→0.406\*\*\* RUT; `BA^med/τ` 0.256\*\*\*→0.261\*\*\*; 0.130\*\*\*→0.135\*\*\*; `NFCI` −25.839\*\*→−19.577\*\*; −23.961\*\*→−22.286\*\*; R² 0.312→0.347 (SPX), 0.281→0.287 (RUT); RMSE 13.199→12.858, 13.951→13.893 bp; MAE 8.682→8.318, 10.103→10.043 bp.
10. **Economic sensitivity (source prose, §6.4):** at `OIS1Y = 4%`, `τ = 0.5`, a **+1 percentage-point** rise in `μ̂` implies **+0.24 bp (SPX)** and **+0.11 bp (RUT)** carry gap; a **+10 pp** rise in the 504-day `μ̂` proxy ⇒ **≈2.4 bp SPX / ≈1.1 bp RUT**. (`0.119×4×0.5 = 0.24`; `0.054×4×0.5 = 0.11` — the source's own worked example.)
11. **Sign stability of the drift term (Table 6.6):** `GBM^{μ̂,OIS,1Y}` positive in **10/10** LOYO folds in **both** markets; significant at 1% in **all ten SPX folds**; "in most folds" for RUT (exact per-fold RUT count **not printed → `underspecified`**).
12. **Maturity-scaling pattern (source interpretation, §6.2):** SPX gains rise monotonically-ish with tenor (0.005 → 0.106), "consistent with the `r·μ̂·τ` structure … visibility should increase at longer tenors"; RUT weaker/non-monotone.
13. **No Sharpe / CAGR / drawdown / win rate / turnover / capacity / PnL figure exists anywhere in v5 → `data gap`.** There is no gross-vs-net distinction to make because no strategy return is reported. This is an explanatory time-series regression study, not a backtest.

### Independently reproduced

`not independently reproduced`

(Our activity this run was limited to: opening the arXiv abs page and the pinned v5 LaTeXML HTML full text (417,721 bytes fetched 2026-09-24), reading all sections and Tables 5.1–6.6, verifying version history/DOI resolution/license/funding/AI declarations, running full-text keyword counts for cost/PnL vocabulary, arithmetic checks of printed bucket-obs sums and printed Δ values, and a repo-wide source-identity dedup. **No carry-gap panel was rebuilt, no OIS curve was bootstrapped, no drift proxy recomputed, no regression re-estimated, no trading rule simulated.**)

### Negative evidence

- **No strategy, no cost model, no PnL:** the entire execution/fee/fill/latency/borrow/capacity layer is absent (`data gap`, keyword counts above) — any tradability claim would be ours, not the source's.
- **Selection on the evaluation sample:** the drift horizon `n = 504` (and the reported optima 542/514/525) was chosen by scanning **the same LOYO pooled OOS R² grid later reported as the headline** (Figure 6.1); no selection/multiplicity adjustment over the scanned horizon grid is printed. The source mitigates but does not remove this by showing a plateau.
- **LOYO is not real-time OOS:** for each holdout year the training set contains years *after* it (source-disclosed, §6.3: "should not be interpreted as a fully causal real-time forecasting test"); an expanding-window design was explicitly declined as too short a sample.
- **COVID regime still fails:** even with the drift term, the 2020 holdout OOS R² is **−0.748** (baseline −1.221); RUT holdouts 2016 (−0.304) and 2017 (−0.218) remain negative; SPX gets *worse* in 2016/2017/2018 (Δ −0.008 / −0.090 / −0.010).
- **RUT gain is marginal and turns negative at long tenors:** in-sample ΔR² **+0.006**, pooled OOS 0.171→0.188, and the two longest buckets worsen (−0.013, −0.052) — the mechanism is not uniform across markets or maturities (source-disclosed, §6.2/§7.4).
- **Competing-explanation risk (drift vs rates):** when the drift term enters, SPX `GBM^{σ,OIS,10Y}` collapses from **0.411\*\* to 0.125 and loses significance** — the source itself says the `μ̂` proxy "absorbs part of the low-frequency variation previously captured by the long-horizon OIS path-risk component" (§6.4). Because `GBM^{μ̂,OIS,1Y}` mechanically multiplies `OIS1Y × μ̂ × τ`, the drift regressor can act as a low-frequency rate/trend proxy rather than a directional-margin signal; **no orthogonalization against rate trends is performed in the source.**
- **Motivating wedge figure is external:** Figure 1.1 (and the tight-parity-vs-wedge contrast) is **reproduced from the companion SSRN paper (Shin 2026, 6407379)** rather than re-derived inside v5 — the headline stylized fact depends on a different, also-unvetted source.
- **Source's own caveats:** Figure 1.2 comovement is "only suggestive … cumulative financial series can comove for spurious reasons" (§3.4); the coefficient is "a reduced-form loading … not a structural estimate of μ" (§7.4); the paper "does not propose a replacement for Black–Scholes–Merton" and leaves a structural model to future work (§7.4).
- **Breadth:** only two underlyings (SPX, RUT), one market, one vendor, **Jan 2016–Oct 2025 (<10 years)**, no cross-asset/international replication, no holdout after Oct 2025.
- **Reproducibility:** no code, no data-availability statement, no replication package (`github` 3 hits = arXiv UI; `code availability`/`data availability`/`replication package`/`source code` all 0); OIS data is a private share from a named individual; ThetaData quotes are a **commercial subscription** → **not independently reproduced**.
- **Publication status:** preprint only (no journal-ref, no peer-review statement), single author, AI-assisted editing declared; **no cost or execution evidence exists to offset these risks**.
- **Effect magnitude vs tradeability:** the source's own worked example implies a **~2.4 bp (SPX, 6-month)** carry-gap response to a **10 pp** drift move — plausibly dominated by index-option execution frictions if anyone tried to trade it; whether any residual exceeds round-trip cost is `not stated in source`.
- None identified beyond the source's own disclosures for the narrow claim "ψ > 0 under this design"; absence of further negative results is not evidence of no negative result.

## Falsification plan

Thresholds below are **`research-defined falsification threshold`**; constructions are **`research-proposed`** unless marked `source-reported`.

1. **Second-vendor replication (`research-proposed`):** rebuild the panel from a different option-quote vendor and an independently sourced OIS curve; re-estimate Eq. 12 with the source's HAC(21). **Fail if** SPX ψ ≤ 0 or HAC t < 2.0, or SPX ΔR² < 0.010 in-sample. (t ≥ 2.0 and ΔR² ≥ 0.010 `research-defined`.)
2. **Honest rolling/expanding OOS (`research-proposed`):** estimate coefficients only on data strictly before each test year (2021–2025), freeze the 504-day proxy rule, and score pooled OOS R². **Fail if** extended-minus-baseline pooled OOS R² ≤ 0.030. (0.030 `research-defined`, ≈ 10% of the source's 0.310 pooled level and ≈ 90% below its LOYO Δ of 0.089.)
3. **Horizon-selection hygiene (`research-proposed`):** select `n` using only 2016–2019 data, freeze it, and evaluate 2020–2025. **Fail if** the frozen-horizon Δ pooled OOS R² ≤ 0 (selection artifact) or if the selected `n` leaves the source's stated plateau band (>±50% away from 504 days).
4. **Drift-vs-rates orthogonalization (`research-proposed`):** residualize `μ̂` against same-day changes in the OIS 1Y/10Y curve and NFCI, rebuild `GBM^{μ̂,OIS,1Y}`, re-estimate. **Fail if** the orthogonalized ψ falls below HAC t = 2.0 in SPX **or** in-sample ΔR² < 0.010 → the "physical drift" reading collapses into a rate-trend reading (competing explanation of §6.4's 0.411→0.125 collapse).
5. **Drift-proxy placebo (`research-proposed`):** replace `μ̂` with 1,000 circular-shift (year-block) surrogates matched on marginal distribution; re-estimate ΔR² each time. **Fail if** the real ΔR² does not exceed the placebo 95th percentile (`research-defined`).
6. **Quote-screen / spread robustness (`research-proposed`):** re-derive `B̂` from half-spread-adjusted (bid+ask)/2 quotes, then from strict moneyness-restricted strike sets, and re-run Tables 6.1/6.2. **Fail if** the SPX long-bucket (10–14m, 14–21m, 21m+) ΔR² gains shrink by >50% or change sign in either variant. (50% `research-defined`.)
7. **Regime concentration (`research-proposed`):** recompute LOYO excluding the 2020–2021 pandemic years entirely. **Fail if** the pooled OOS gain concentrates in 2020–2021 such that Δ pooled OOS R² ≤ 0 on the remaining eight years.
8. **Cross-market generalization (`research-proposed`):** repeat the design on two additional European index-option surfaces (e.g. NDX and a non-U.S. index). **Fail if** ψ ≤ 0 in a majority of the new markets (`research-defined`) — a two-name result is too brittle to carry a mechanism claim.
9. **Cost ladder for any operationalization (`research-proposed`):** implement the §7.3 hurdle comparison as an explicit rule — enter the parity-enforcement trade when the observed price-space residual exceeds the model-implied hurdle `Ĥ = F·τ·CĜ/10⁴` by ≥ 2× the in-sample regression RMSE converted to price space (`research-proposed` threshold multiplier; `research-defined` 2×RMSE gate), hold to expiry, size equally per episode — and mark it only as a *screening* test. Stress at **0 / 1 / 2 / 5 / 10 bp per side per leg plus futures-leg spread and variation-margin financing at the overnight rate**. **Fail if** net Sharpe < 0.5 at 5 bp **or** the episode win rate is ≤ 50% over ≥100 independent episodes (both `research-defined`).
10. **Action on failure:** keep this record `research-only`; if tests 1–4 fail, mark the drift-margin-burden mechanism `rejected` in a future update rather than retuning `n`, screens, or HAC lag until significance returns (no unconstrained-retuning rescue). Tests 9 failing alone downgrades tradability to `dead-as-specified` while leaving the measurement claim intact.

## Crypto portability

**unproven.**

- All evidence is in **U.S. equity index options (SPX, RUT)** against a **risk-free OIS curve**, with **VIX/RVX** vol inputs, exchange futures daily settlement, and CRSP-style total-return series — **no crypto evidence exists in the source.**
- Porting gaps: crypto index/option surfaces (e.g. Deribit BTC/ETH options) are European-style and could support a synthetic-forward carry gap, but there is **no OIS curve analogue** (candidates: stablecoin/FRA/funding curves — a different object, `research-proposed`), no exchange futures leg with the same daily variation-margin design for the exact `+C−P−F` construction, and no VIX/RVX analogue (realized/IV proxies would be substituted).
- 24/7 sessions and non-standard candle/date boundaries alter the "prior-only through t−1" drift proxy and the date-maturity cell definition; venue fragmentation across Deribit/OKX/Binance means one vendor's NBBO is not the market; borrow/short mechanics, liquidation, and cross-venue margin are unmodeled here.
- Not `direct` (source demonstrates nothing in crypto); not yet `adapted` (nothing has been adapted). Crypto porting is **not** authorization to trade.

## Limitations

- `not independently reproduced`; `data gap`: no code, no data-availability statement, no replication package; commercial ThetaData quotes plus privately shared OIS data.
- `data gap`: preprint only (arXiv v5, 24 May 2026); no journal-ref, no stated peer-review status; single author; AI-assisted language editing declared by the author.
- `data gap`: OIS curve provider/tenor set, total-return index vendor, quote-filter thresholds, timezone/exchange-date convention, weekly-vs-monthly contract split, and the exact role of the Databento ES/RTY reference are not stated.
- `underspecified`: exact per-fold RUT significance count behind Table 6.6's "most folds".
- The study is a **reduced-form fit comparison**, not a forecast or backtest; LOYO includes post-holdout data; the drift horizon was chosen on the reported evaluation grid; no multiplicity control over the horizon scan.
- Mechanism asymmetry: strong in SPX, marginal in RUT, negative in RUT's two longest buckets; 2020 holdout stays deeply negative; gains are low-frequency level-calibration gains, not high-frequency predictability (source's own framing, §6.3).
- The drift regressor is not orthogonal to interest-rate trends (SPX long-rate coefficient collapses when it enters); no structural identification of `μ`; effect size in price space (~2.4 bp per 10 pp drift at 6m) is small relative to plausible execution frictions.
- The motivating wedge figure and baseline model come from a **companion SSRN working paper (6407379)** that is itself unreviewed and not recorded here.
- Incremental-write check: no prior record covers the `r·μ̂·τ` physical-drift margin-burden loading on the carry gap; the same-author Year-End Toll record, the borrow/dividend-confounding parity record, and the IBIT-vs-CME carry-wedge record study different mechanisms (see Provenance four-axis distinction).

## Implementation status

`not-implemented`.

No implementation in our research stack exists: no carry-gap panel, no OIS bootstrap, no drift proxy, no regression, no backtest, no Qlib run, no Paper/Testnet/Live verification. The source itself ships no code and proposes no strategy to port — only an econometric design (Eqs. 7, 9–17) and a non-mechanical §7.3 screening heuristic.

## Adoption boundary

This record is **research material only**. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

- `[[option-funding-basis-year-end-boundary-wedge-spx-rut-box-implied-2026-09-22]]` — same author (Useong Shin) and same SPX/RUT synthetic-forward machinery, **different paper (arXiv:2609.20224) and different mechanism** (discrete December-31 boundary wedge vs continuous drift-sensitive margin burden); read together they delimit *calendar* vs *drift* sources of parity-enforcement cost.
- `[[put-call-parity-implied-borrow-dividend-confounding-falsification-2026-09-13]]` — same parity identity, different confound (borrow/dividend in implied rates vs enforcement-capital path risk).
- `[[bitcoin-ibit-options-cme-futures-implied-carry-wedge-2026-09-01]]` — implied-carry wedge in a different market/wrapper (spot ETF vs futures); **also the only Wiki Brain page returned by `kb_search` for this mechanism family** (`quant/bitcoin-ibit-options-cme-futures-implied-carry-wedge-2026-09-01`, confirmed to exist 2026-09-24).
- `[[spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]]` — index-options relative-value with execution frictions; adjacent cost evidence.
- `[[equity-index-dispersion-correlation-risk-premium-spread-friction-falsification-2026-09-13]]` — index-options spread-friction falsification; different mechanism.

(Wiki Brain `kb_search` for "put-call parity carry gap option-implied discount factor implementation premium" returned **0 pages** — **no Wiki link is fabricated for this specific mechanism**; the paths above are repository records used as retrieval hooks, except the IBIT page which is a confirmed Wiki Brain page.)

## Sources

1. Useong Shin. *"The P behind Q: Empirical Evidence from Physical Drift in Put–Call Parity."* arXiv:2605.12250v5 [q-fin.GN], v1 12 May 2026 15:19:55 UTC, v5 24 May 2026 10:33:31 UTC. CC BY 4.0. https://arxiv.org/abs/2605.12250 — DOI: https://doi.org/10.48550/arXiv.2605.12250. Full text (pinned, read 2026-09-24): https://arxiv.org/html/2605.12250v5. (Sections 1–8 and Appendices A.1–A.5; Equations 1–17; Tables 5.1–5.4, 6.1–6.6; Figures 1.1, 1.2, 6.1–6.4.) — all `source-reported` claims above trace to this pinned version.
2. Useong Shin (2026). *"The Cost of a Free Lunch."* SSRN Working Paper No. 6407379. https://dx.doi.org/10.2139/ssrn.6407379 — cited by the primary source as the origin of the baseline `r·σ·√τ` model and the reproduced Figure 1.1; **not opened in this run → used only as the primary source's own citation, no numbers taken from it** (`data gap` for anything beyond the citation).
3. Azzone, M., & Baviera, R. (2021). *Synthetic Forwards and Cost of Funding in the Equity Derivative Market.* Finance Research Letters, 41, 101841. https://doi.org/10.1016/j.frl.2020.101841 — the synthetic-forward identification procedure used by the primary source (cited within it).
4. FRED, Chicago Fed National Financial Conditions Index (NFCI), series page retrieved 3 April 2026 per the primary source's reference list. https://fred.stlouisfed.org/series/NFCI
5. ThetaData (2026). *Historical SPX and RUT option NBBO data.* https://www.thetadata.net — commercial quote vendor named by the primary source (retrieved 3 April 2026 per its reference list).
6. Databento (2026). *Historical ES and RTY futures BBO data.* https://databento.com — cited in the primary source's reference list; exact in-paper role `underspecified`.

Secondary discovery aids (not used to fill any field): the arXiv abs page and LaTeXML HTML build for v5, both retrieved directly 2026-09-24.
