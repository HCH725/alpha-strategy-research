---
schema: strategy-research-record-v1
title: "Climate Attention (Global Warming Google Search) as a Predictor of U.S. Treasury Bond Excess Returns"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bonds
  - macro-timing
  - alternative-data
status: research-only
confidence: medium
source_as_of: 2026-07-30
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7203448"
  - "https://dx.doi.org/10.2139/ssrn.7203448"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Climate Attention (Global Warming Google Search) as a Predictor of U.S. Treasury Bond Excess Returns

## Provenance

- **Primary source**: Deshui Yu, Jiachen Tang, Luyang Li, and Mingtao Zhou, *"Climate Attention and Treasury Bond Risk Premia"*, SSRN working paper, DOI `10.2139/ssrn.7203448`, stable page `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7203448`.
- **Version / date**: SSRN abstract page states *"41 Pages Posted: 30 Jul 2026"* and *"There are 2 versions of this paper"*; the individual version label/date of the PDF read here is `not stated in source` (only "Posted: 30 Jul 2026" is visible on the landing page). **Publication status**: preprint / working paper — the SSRN page states *"This is a preprint article, it offers immediate access but has not been peer reviewed"*, and every PDF page carries the watermark *"Preprint not peer reviewed"*. No journal DOI or acceptance is stated in source.
- **Author list (exactly as primary source)**: Deshui Yu; Jiachen Tang; Luyang Li; Mingtao Zhou (four authors). PDF title-page affiliations: (a) College of Finance and Statistics, Hunan University (Yu, Tang); (b) Business School, Xiangtan University (Li); (c) School of Economics and Management, Changsha University of Science and Technology (Zhou). **Affiliation inconsistency**: the SSRN author metadata lists Luyang Li as "Monash University - Department of Economics", which contradicts the PDF title page ("Business School, Xiangtan University"); author names and order are identical in both, only the Li affiliation conflicts — marked `underspecified`.
- **Verification method (primary-source checksum)**: the SSRN abstract page and the SSRN-served PDF (`Delivery.cfm/9e41f4fc-4405-4e18-9d86-2e55f9c3745a-MECA.pdf?abstractid=7203448`, 419,248 bytes, `%PDF-1.7`) were both retrieved on 2026-09-23 and the full 41-page text (Sections 1–6, References, Tables 1–13, Figure 1) was read. Every quantitative field below is located to a specific Table/Section of that pinned PDF; nothing is taken from secondary summaries.
- **Discovery aid (not a claim source)**: Alpha in Academia newsletter issue *"Recent Academic Research"* (2026-08-04), `https://alphainacademia.com/p/recent-academic-research-68c`, which surfaced the citation. All empirical content in this record comes from the SSRN primary source only.
- **Sample period**: monthly, **January 2004 – December 2024** (start set by Google Trends availability); pseudo-out-of-sample evaluation window **January 2010 – December 2024** (robustness: January 2015 – December 2024).
- **Universe**: U.S. zero-coupon Treasury bonds, maturities **n ∈ {2, 5, 7, 10} years** baseline, robustness **{12, 16, 20, 24} years**, on the Gürkaynak, Sack and Wright (2007) zero-coupon yield curve; benchmark/short leg is the **1-year** zero-coupon bond.
- **Transaction cost treatment**: Table 8 caption states explicitly *"Portfolio performance is evaluated using nonoverlapping one-year holding-period returns, and **transaction costs are set to zero**."* Order type, fill model, bid-ask spread, slippage, market impact, latency, turnover, borrow, leverage beyond the stated weight cap, and capacity are `not stated in source` (not inferred as unmodeled beyond the explicit zero-cost statement for Table 8).

## Economic mechanism

### Source-reported

The authors frame two non-exclusive channels by which public attention to global warming (GWA) should raise subsequent Treasury excess returns:

1. **Expected policy-rate channel.** Heightened climate attention leads investors to mark down expected economic activity and to expect costlier climate-policy adjustment, implying a lower future path of the federal funds rate and therefore higher current bond prices / subsequent excess returns. Evidence: higher GWA predicts slower expected industrial production growth (β = −0.11, NW-t = −1.46, R² = 1.19%) and higher expected unemployment (β = 0.27, NW-t = 3.08, R² = 3.40%) — Table 12, Panel A.
2. **Safe-haven / flight-to-safety channel.** Rising climate concern raises perceived macro and financial risk and risk aversion, boosting demand for safe liquid Treasuries. Evidence: GWA predicts a higher risk-aversion index (β = 0.27, NW-t = 2.29, R² = 7.07%), higher VIX (β = 0.22, NW-t = 2.07, R² = 4.47%) and higher foreign net purchases of long-term Treasuries (β = 0.28, NW-t = 4.08, R² = 7.82%) — Table 12, Panel B. The authors explicitly qualify FLOW as *"mechanism-consistent rather than conclusive evidence of flight-to-safety behavior"* (Section 5.1).

Transmission into prices is localized with the Kim and Wright (2005) yield decomposition: GWA predicts the **expected-short-rate component** (β = −0.22, NW-t = −2.47, R² = 4.90%) but **not the term premium** (β = −0.05, NW-t = −0.64, R² = 0.20%) — Table 12, Panel C. State dependence: predictive power is weak before COP21 and strong after the December 2015 Paris Agreement, and is amplified in upper-tercile investor-attention, investor-sentiment and investor-disagreement states — Table 13, Panels A–D.

### Research interpretation

Falsifiable hypothesis: **a slow-moving, publicly observable attention series (worldwide Google search intensity for "global warming") contains time-series timing information for the one-year-ahead excess return of intermediate/long U.S. Treasuries over the 1-year bill, beyond yield-curve and standard bond-predictor information.** Candidate mechanisms are (a) attention-driven downward revision of expected policy rates and (b) attention-driven safe-asset demand; the source's own decomposition favors (a). The signal is a *macro/attention timing* hypothesis, not a cross-sectional premium, and its economic content plausibly depends on climate policy salience (post-Paris-Agreement regime), which is a testable regime dependency rather than a permanent feature. Alternative competing explanations that must be ruled out in any replication: GWA as a slow proxy for recession risk/uncertainty already spanned by CP/FB factors, Google Trends normalization artifacts, and post-hoc multiple testing across 4–8 maturities and ~11 control predictors.

## Signal

Normalized from Sections 2.1–2.2, 4.1, 4.4 and Equations (1)–(14) of the pinned PDF:

- **Predictor construction (GWA)**: worldwide Google Trends series for the topic **"global warming"**, monthly, Jan-2004–Dec-2024. Following Choi et al. (2020) for the topic choice and Huang et al. (2021) for smoothing: take the **log of the raw Google Trends index**, then a **12-month moving average**, then **standardize to mean 0 / standard deviation 1** (Figure 1 caption: *"The 12-month moving-average series is standardized and used as the global warming attention index (GWA)"*). Summary stats of the standardized series: mean 0.04, sd 0.86, min −1.23, max 2.01, ρ(1) = 0.99 (Table 1).
- **Formation timestamp / tradability**: GWA at month *t* predicts the bond excess return over *t→t+1*; the source's stated advantage is that search data is *"available in near real time and is not subject to subsequent data revisions"* (Section 1). The exact within-month observation date, publication lag and timezone convention are `not stated in source`.
- **Lookback**: 12-month moving average of the logged SVI (inclusive monthly window); warm-up therefore begins January 2004 with usable smoothed values from December 2004 — the paper does not state a separate warm-up rule (`not stated in source`).
- **Target variable**: one-year log holding-period excess return of an *n*-year zero bought at *t* and sold at *t+1* as an *(n−1)*-year zero, minus the 1-year zero yield observed at *t* (Equations 2–3), *n ∈ {2,5,7,10}*.
- **Predictive relation (the source's specification)**: `rx(t+1) = α + β·GWA(t) + ε(t+1)` univariate, plus variants adding the three yield-curve PCs (level/slope/curvature from 1–5y zero yields), FB, CP, LN, or one of FU/MU/GPR/PFU/VRP (Equations 4–7). Estimated with Newey–West (1987) standard errors.
- **Portfolio rule actually specified by the source (Section 4.4, Equations 12–14)**: a mean–variance investor allocates between the *n*-year bond and the 1-year bond with `ω(t) = E_t[rx(t+1)] / (γ · Var_t[rx(t+1)])`, **γ ∈ {5, 10}**, conditional mean from each forecasting method, conditional variance from *"a rolling window of past excess returns"* (**window length `not stated in source` → `underspecified`**), and weights **constrained to ω ∈ [−1, 2]** (shorting and leverage limited). Baseline forecasts use a **recursive expanding window** from the T₁ training origin (Jan 2004 – Dec 2009), with a **six-year rolling-window** variant; benchmark forecast is the recursively updated historical average of excess returns.
- **Rebalancing / holding**: **nonoverlapping one-year holding-period returns** (Table 8 caption); there is no stop, take-profit, intraperiod exit, or re-entry rule in the source (`not stated in source`).
- **Entry/exit thresholds**: the source reports **no** discrete long/cash or long/short threshold rule — it is a continuous-allocation and predictive-regression design. Any threshold implementation (e.g. "long duration when GWA > 0, cash otherwise") would be **research-proposed**, not source-reported.
- **Reproducibility verdict**: the predictor and regression are reconstructible; the allocation rule is **partially underspecified** (rolling variance window length, exact rebalance month/day, and data-vintage handling are not given). Marked `underspecified` in Limitations.

## Required data

- **Instrument / universe**: U.S. Treasury zero-coupon yields from Gürkaynak, Sack and Wright (2007) (maturities 1–24 years used); cash leg = 1-year zero-coupon yield. Government debt, USD-denominated, no credit risk; roll treatment for the maturity-matched bond follows the log-price construction of Equation (2) (sell the *n*-year bond after one year as an *(n−1)*-year bond) — no futures, no coupon/corporate-action treatment needed.
- **Venue / market type**: U.S. Treasury cash/strip market (or any vehicle tracking constant-maturity zero-coupon returns); venue `not stated in source`.
- **Timeframe**: monthly frequency; one-year forecast horizon and one-year nonoverlapping holding period.
- **Fields**: worldwide Google Trends Search Volume Index for the topic "global warming" (monthly, 0–100 normalized); zero-coupon yields/log prices at 1, 2, 5, 7, 10 (and 12/16/20/24 for robustness) maturities; controls: first three yield-curve PCs (1–5y yields), FB forward-spread factor, Cochrane–Piazzesi forward-rate factor, Ludvigson–Ng macro factor (from the author's site, footnote 2), FU/MU (Ludvigson site), GPR (Iacoviello site), PFU (Rossi–Sekhposyan site), VRP; channel variables: expected IP growth, expected unemployment, risk-aversion index, VIX, foreign net purchases of long-term Treasuries (Equation 16), Kim–Wright (2005) expected-short-rate and term-premium decomposition.
- **Point-in-time / availability**: search index described as near real-time and unrevised (Section 1); Google Trends SVI is *relative* normalization (0–100 against total search activity for the selected region/period), which makes historical values re-normalizable as the sample extends — the source does **not** document a fixed-vintage reconstruction rule → `data gap`.
- **Timestamp / timezone**: monthly observation convention; exact day/time and timezone `not stated in source`.
- **Missing data**: imputation rules, holiday handling, and treatment of Google Trends outages are `not stated in source` (imputation is forbidden in our own replication unless explicitly justified).

## Execution assumptions

What the source actually assumes, versus what it leaves open:

- **Signal-to-order timing**: forecast formed at month *t* from month-*t* data applied to the *t→t+1* one-year return; within-month execution timing (trade date, at-the-close vs next-open) `not stated in source`.
- **Order type / fill model / latency / partial fills**: `not stated in source`.
- **Fees, spread, slippage, impact, capacity**: **Table 8 explicitly sets transaction costs to zero**; spread, slippage, market impact, borrow and capacity are `not stated in source` (no claim that they are negligible — one-year holding periods and low portfolio turnover are only implied by the nonoverlapping one-year design, and **turnover is never reported**).
- **Leverage / margin / shorting**: implied bounds are the hard constraint **ω ∈ [−1, 2]** on the *n*-year-bond-vs-1-year-bond allocation (Equation 14 discussion); margin, financing and repo costs `not stated in source`.
- **Benchmark**: recursive historical-average excess-return forecast (expectations-hypothesis benchmark) for both MSFE and CER comparisons.
- **Scout-added assumptions**: none. Any execution convention we later adopt (trade at month-end close, futures replication instead of cash zeros, cost model) is **research-proposed**.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned SSRN PDF (Yu, Tang, Li, Zhou; posted 2026-07-30), all for the sample Jan-2004–Dec-2024, U.S. Treasury zero-coupon bonds, and **have not been independently reproduced**:

- **In-sample baseline (Table 3, univariate, PC columns = No)**: β = **0.68%** (2y), **2.26%** (5y), **2.91%** (7y), **3.49%** (10y) per 1-σ GWA; Newey–West t = **5.59, 6.13, 5.99, 5.26**; R² = **24.33%, 22.58%, 19.03%, 13.88%** (adjusted 24.02/22.26/18.71/13.53). With the three yield-curve PCs: β = 0.76 / 2.98 / 4.29 / 5.86, NW-t = 6.66 / 8.20 / 7.91 / 7.11, R² = 63.95 / 62.39 / 54.89 / 45.03%.
- **Control robustness (Table 4)**: with FB/CP/LN added separately, univariate-plus-control β stays positive at 1% significance — 2y 0.45–0.60, 5y 1.67–2.39, 7y 2.21–3.44, 10y 2.67–4.58; with CP **and** PCs: β = 1.11 / 3.76 / 5.26 / 7.22, NW-t = 8.16 / 8.65 / 8.30 / 7.63.
- **Uncertainty controls (Table 5)**: β range without PCs 0.54–3.62 (NW-t 3.70–7.21); with PCs 0.72–8.97 (NW-t 6.27–12.25) across FU, MU, GPR, PFU, VRP controls.
- **Out-of-sample accuracy (Table 6, evaluation 2010-01 → 2024-12, recursive expanding window vs historical average)**: R²_OS = **13.90% / 18.06% / 17.70% / 14.16%** (2/5/7/10y); Clark–West = **4.20 / 3.74 / 3.94 / 3.99** (reject at 1% in all four cases); forecast-encompassing weight λ = **0.73 / 1.00 / 1.00 / 1.00** with Harvey et al. (1998) stats 4.42 / 4.00 / 4.18 / 4.22.
- **Horse race vs 11 established predictors × 4 maturities (Table 7)**: equal-weight GWA+competitor combination lowers MSFE in **all 44** comparisons; R²_OS range **3.56–27.59% (2y)**, **4.55–22.39% (5y)**, **3.60–17.68% (7y)**, **1.26–11.93% (10y)**; 38 significant at 1%, five at 5%, the smallest (1.26% vs PC1, 10y) at 10%; λ reaches 1.00 in 40 of 44 cases.
- **Economic value (Table 8, OOS 2010–2024, ω ∈ [−1,2], nonoverlapping 1-year returns, `transaction costs = zero`)**: with **γ = 5**, ΔCER = **0.14pp (2y, test 0.62, insignificant)**, **2.16pp (5y)**, **2.62pp (7y)**, **2.56pp (10y)** with CER tests 4.57 / 5.77 / 6.09; ΔSR = **0.17 (2y, JK 1.26, insignificant)**, **0.43**, **0.29**, **0.17** with JK tests 6.13 / 6.67 / 6.44. With **γ = 10**, ΔCER = 0.05 (2y, insignificant) / 1.72 / 2.06 / 1.87; ΔSR = 0.15 (2y, insignificant) / 0.36 / 0.22 / 0.12.
- **Robustness — later start (Table 9, OOS from 2015-01)**: R²_OS = 27.11 / 29.76 / 27.85 / 21.82%, CW = 4.35 / 4.68 / 4.77 / 4.59, λ = 1.00 at every maturity.
- **Robustness — six-year rolling estimation (Table 10)**: R²_OS falls to **4.04 / 7.42 / 9.61 / 10.84%**, CW = 3.92 / 3.05 / 3.54 / 3.65, λ = 0.58 / 0.75 / 0.87 / 0.93.
- **Robustness — long maturities (Table 11)**: R²_OS = 17.94 (12y) / 12.85 (16y) / 10.66 (20y) / 9.83% (24y), CW = 4.32 / 3.73 / 3.40 / 3.31, λ = 1.00 throughout.
- **Mechanism (Table 12)** and **state dependence (Table 13)**: as reported under Economic mechanism — post-COP21 β₁ = 0.20 / 0.80 / 1.06 / 1.42% (all 1% significant) vs pre-COP21 β₂ = 0.02 / 0.18 / 0.34 / 0.43% (all insignificant); high-sentiment state β₁ = 0.69 → 4.36% vs low-sentiment 0.18 / 0.43 / 0.39 / 0.15% (only 2y and 5y significant).
- **No gross/net distinction for costs exists beyond the explicit zero-cost statement in Table 8**; no turnover, MDD, t-statistic of the *strategy's* Sharpe (only differences vs benchmark), deflated Sharpe, or capacity figures are reported → `data gap`.

### Independently reproduced

not independently reproduced

### Negative evidence

- **The source's own state-split weakens the average effect**: before COP21 (three years prior to Dec-2015) GWA's slope is statistically insignificant at every maturity (Table 13 Panel A, β₂ 0.02–0.43%), i.e. roughly the first 12 of 21 sample years carry no detectable signal.
- **Economic value is concentrated at ≥5 years**: for the 2-year bond, both ΔCER and ΔSR are positive but statistically insignificant at γ = 5 and γ = 10 (Table 8, tests 0.62/1.26 and 0.20/1.05).
- **Cost sensitivity untested**: Table 8 sets transaction costs to zero and turnover is never reported, so the headline CER/Sharpe gains are gross; whether they survive any positive cost model is unknown (`data gap`, not a claim that they fail).
- **Estimation-window fragility**: switching to a six-year rolling window cuts R²_OS from ~14–18% to **4.04–10.84%** (Table 10 vs Table 6) — a material sensitivity to the estimation scheme.
- **Thin horse-race margin exists**: the gain vs PC1 for the 10-year bond is only 1.26% and significant at 10% (Table 7) — the weakest of the 44 comparisons.
- **Term-premium channel is a null result** (β = −0.05, t = −0.64, R² = 0.20%; Table 12 Panel C) and the IP-growth channel is only marginally significant (Table 12 Panel A).
- **The predictor itself trends down**: GWA rises to ~2007 then declines "particularly after 2010" with event rebounds (Section 2.1/Figure 1) — a persistent level predictor with a structural decline raises spurious-regression/Stambaugh-bias concerns that the paper handles only with Newey–West errors and PC controls.
- **Source-quality caveat**: preprint, explicitly *not peer reviewed*, 0 citations and 31 downloads on SSRN as observed 2026-09-23; no independent replication or contrary study of this specific index was found in the reviewed sources.
- **Adjacent literature was checked but is not contradictory evidence for this index**: no repo or Wiki Brain record covers SSRN 7203448; nearby climate-attention studies (e.g. climate media attention in corporate bonds, climate attention in carbon futures) study different assets and different indices and were not used as evidence here.

## Falsification plan

Each item states data / sample / metric / threshold / action. Thresholds are **research-defined** unless marked source-specified.

1. **Full-sample replication (source-specified design)** — Data: GS worldwide "global warming" monthly SVI + GSW zero-coupon yields, Jan-2004–Dec-2024. Metric: univariate β and Newey–West t for n ∈ {2,5,7,10}. **research-defined threshold**: |NW-t| < 2.0 at ≥3 of 4 maturities ⇒ the in-sample claim fails (Table 3 says all are 5.26–6.13). Action: reject the hypothesis as reported.
2. **Out-of-sample replication (source-specified design)** — recursive expanding window, evaluation 2010-01→2024-12 vs historical average. **research-defined threshold**: R²_OS ≤ 0 at ≥2 of 4 maturities, or Clark–West < 1.64 in ≥3 of 4, ⇒ falsifies the OOS claim (source reports 13.90–18.06% and CW 3.74–4.20). Action: downgrade to in-sample-only artifact.
3. **Cost stress (research-proposed extension of Table 8)** — re-run the ω ∈ [−1,2] allocation with explicit annual cost assumptions of 0 / 5 / 10 / 20 bp plus one-way bid-ask on the traded maturity, and report turnover. **research-defined threshold**: at any source-plausible cost level, ΔCER ≤ 0 for the 5y/7y/10y portfolio ⇒ economic-value claim fails at that cost. Action: record as cost-fragile; no adoption.
4. **Estimation-window sensitivity** — expanding vs 6-year rolling vs 3/10-year rolling, plus a fixed 2010 start. **research-defined threshold**: if the rolling-window R²_OS ≤ 0 for any baseline maturity, the effect is judged window-dependent (source already shows it drops to 4.04–10.84%). Action: report window dependence as a primary limitation.
5. **Regime / pre-post split** — pre-COP21 (to 2015-12) vs post-COP21, and sub-periods 2004–2010 / 2010–2017 / 2017–2024. **research-defined threshold**: post-2015 β insignificant (NW-t < 1.96) at ≥3 maturities ⇒ the "salience" mechanism fails. Action: treat as historical-regime artifact.
6. **Placebo predictors (research-proposed)** — 500+ placebo search topics of matched persistence (ρ(1) ≈ 0.99) and matched volatility, run through the identical pipeline. **research-defined threshold**: GWA's R²_OS must exceed the 95th percentile of the placebo R²_OS distribution ⇒ otherwise data-mining/multiple-testing rejection. Action: reject.
7. **Alternative attention series / vintage robustness (research-proposed)** — rebuild GWA from a frozen Google Trends vintage and from log-levels without the 12-month MA; also test neighbouring topics ("climate change", "global warming theory"). **research-defined threshold**: sign flip or |NW-t| < 1.96 in ≥2 maturities under any reasonable construction ⇒ signal is a construction artifact. Action: reject that construction and report non-robustness.
8. **Encompassing vs established predictors (source-specified)** — combined forecasts vs FB, CP, LN, PCs, FU, MU, GPR, PFU, VRP with Harvey–Leybourne–Newbold tests. **research-defined threshold**: λ ≤ 0.5 in a majority of the 44 cells ⇒ GWA does not dominate; competing explanation survives. Action: reclassify as redundant.
9. **Mechanism ablation (research-proposed)** — regress subsequent ER/TP components and channel variables; **research-defined thresholds**: ER coefficient insignificant while TP significant, or UNE/RAI/VIX/FLOW all |NW-t| < 1.96, ⇒ the stated mechanism is not supported even if returns are predicted. Action: keep as prediction-only, drop mechanism claim.
10. **Capacity / instrument replication (research-proposed)** — re-run with CME Treasury futures (2/5/10y notes, long bond) and with a duration-matched ETF at realistic spreads. **research-defined threshold**: net ΔCER ≤ 0 at 10 bp one-way ⇒ not implementable as a Treasury timing overlay. Action: research-only, no production candidate.
11. **Out-of-extension-window honesty check (research-defined)** — because the sample ends 2024 while the paper posts 2026, a true hold-out on 2025–2026 data must be run before any adoption; failure = R²_OS ≤ 0 on the untouched extension ⇒ frozen as rejected for trading.

## Crypto portability

**Unproven.**

- The source contains **zero crypto evidence**: universe is U.S. Treasury zero-coupon bonds, and both channels (policy-rate expectations, flight-to-safety into a sovereign safe asset) are specific to a rate-setting sovereign with a reserve-currency safe asset.
- Crypto has no policy-rate path in the same sense, no duration-matched sovereign instrument, and its "safe haven" narrative is contested within our own record pool; perp funding, basis and 24/7 session structure are unrelated to this monthly attention signal.
- **Possible (research-proposed) ports, none validated**: (a) use an equivalent search-attention index (e.g. Google Trends "bitcoin crash"/"crypto") as a *regime/timing* covariate for BTC/ETH beta exposure; (b) test whether attention shocks predict subsequent 12-month crypto excess returns under the same 1-SD → return regression; (c) attention as a control variable rather than a signal.
- Crypto-specific risks if ever ported: exchange fragmentation and survivorship of venues, funding/borrow asymmetry, 24/7 candles vs monthly SVI alignment, stablecoin/quote-currency effects, and Google Trends' relative-normalization instability across an ever-extending sample. Any crypto version is a **new hypothesis**, not an empirical extension of this source.

## Limitations

- `underspecified`: rolling variance-window length in Equation (14); exact within-month formation/trade timing and timezone; Google Trends fixed-vintage reconstruction rule; SSRN version numbering ("2 versions" with no labels); Luyang Li's affiliation conflict between SSRN metadata and PDF title page.
- `data gap`: turnover, MDD, gross-vs-net decomposition beyond the explicit zero-cost Table 8, t-stats for *level* Sharpe (only difference tests), deflated Sharpe / multiple-testing correction across 4–8 maturities × 11 controls × several state splits, capacity/liquidity, borrow and financing costs.
- `not stated in source`: order type, fill model, slippage, spread, impact, latency, partial fills, venue, missing-data handling for Google Trends outages.
- `not independently reproduced`: every performance figure here is source-reported from a preprint that is explicitly not peer reviewed.
- Sample is short for a monthly macro predictor (252 months, 2004–2024), starts in 2004 by data availability, and the effect is documented as weak for the first ~12 years (pre-COP21) — effective post-2015 sample is only ~10 years / 120 monthly observations.
- The predictor is highly persistent (ρ(1) = 0.99), raising Stambaugh-type predictive-regression bias; the source addresses this only with Newey–West errors, not with the full battery of persistence-robust estimators.
- Publication-bias and researcher-degree-of-freedom concerns apply: single search topic chosen with justification but not pre-registered; multiple maturities, multiple controls, multiple state variables and two risk-aversion settings are reported.
- Google Trends is a proprietary, normalized, silently re-scalable series; long-horizon levels are not stable across vintages — a replication may not reproduce the published index exactly.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack: no signal pipeline, no backtest, no Qlib run, no futures/ETF replication, no Wiki Brain ingestion, no candidate-pool entry, no Paper/Testnet/Live activity. The record is a normalized research capture of a preprint's claims only.

## Adoption boundary

This record is **research material only**. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

Pre-write `kb_search` on Wiki Brain for "Treasury bond return predictability climate attention Google search" returned **0 results**; a broader "investor attention search volume cross-sectional factor" query returned only unrelated mechanism families (`quant/crypto-token-unlock-72h-supply-shock-event-short-2026-09-12`, `quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02`). **No matching or materially adjacent Wiki Brain page for this climate-attention bond-timing hypothesis exists**; this section is the retrieval hook for future synthesis.

Repository-adjacent records (different mechanisms, read-only neighbors, not sources for this record):

- `crypto-cross-sectional-abnormal-investor-attention-momentum-2026-08-31.md` — Google-search attention as a *cross-sectional crypto* signal, versus this *time-series U.S. Treasury* predictor.
- `crypto-cross-sectional-fundamental-network-sentiment-fmp-sorting-2026-09-01.md` — Google Trends sentiment inside factor-mimicking portfolios for a crypto panel.
- `mfast-market-friction-aware-llm-news-sentiment-quintile-2026-09-22.md` — alternative-data sentiment with explicit frictions, a contrast to this source's zero-cost Table 8.
- `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md` — excess-return timing from text signals.

## Sources

1. Yu, Deshui; Tang, Jiachen; Li, Luyang; Zhou, Mingtao. **"Climate Attention and Treasury Bond Risk Premia."** SSRN working paper, 41 pages, posted 30 July 2026, DOI `10.2139/ssrn.7203448`. Abstract page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7203448 (retrieved 2026-09-23). Full PDF read for this record: SSRN `Delivery.cfm/9e41f4fc-4405-4e18-9d86-2e55f9c3745a-MECA.pdf?abstractid=7203448` (419,248 bytes; Sections 1–6, Tables 1–13, Figure 1). Preprint, not peer reviewed.
2. Discovery aid only (no empirical claim taken from it): Alpha in Academia, "Recent Academic Research", 2026-08-04, https://alphainacademia.com/p/recent-academic-research-68c.

Data/code provenance referenced by the source (not by us): Gürkaynak, Sack and Wright (2007) zero-coupon yield curve; Google Trends worldwide topic "global warming"; Ludvigson macro/uncertainty series; Iacoviello geopolitical risk index; Rossi–Sekhposyan professional-forecast uncertainty; Kim and Wright (2005) arbitrage-free three-factor yield decomposition. No replication code or repository is provided by the source (`not stated in source`).
