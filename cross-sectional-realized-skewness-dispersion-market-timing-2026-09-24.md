---
schema: strategy-research-record-v1
title: "Cross-Sectional Realized Skewness Dispersion as an Aggregate Equity-Premium Timing Signal (S&P 500 Mean-Variance Allocation)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-04-09
sources:
  - "Mykola Babiak, Jozef Baruník, Josef Kurka, 'Skewness Dispersion and Stock Market Returns', arXiv:2604.07870v1 [q-fin.GN], submitted 9 Apr 2026. https://arxiv.org/abs/2604.07870"
  - "https://doi.org/10.48550/arXiv.2604.07870"
  - "https://arxiv.org/pdf/2604.07870 (52-page primary-source PDF downloaded and read in full via text extraction for this record on 2026-09-24; 626,424 bytes; SHA-256 08f0a95b600c32bda145c036771f0994ca4d242168c0cc5c1a911fb22f59ad92)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Realized Skewness Dispersion as an Aggregate Equity-Premium Timing Signal (S&P 500 Mean-Variance Allocation)

## Provenance

- **Primary source (authors, exactly as the source):** Mykola Babiak (Lancaster University Management School, UK), Jozef Baruník (Institute of Economic Studies, Charles University, Prague; and Institute of Information Theory and Automation, Academy of Sciences of the Czech Republic), Josef Kurka (same two Prague institutions). The arXiv abstract-page authors field, the PDF title page, and the PDF `/Author` metadata (`Mykola Babiak; Jozef Barunik; Josef Kurka`) are consistent.
- **Version / date:** **arXiv v1 only** — submission history shows a single entry, `[v1] Thu, 9 Apr 2026 06:33:53 UTC` (submitter: Jozef Baruník); page stamp `arXiv:2604.07870v1 [q-fin.GN] 9 Apr 2026`; no Comments field, **no `journal_ref`, no publisher DOI** → `preprint only`. arXiv-issued DOI `10.48550/arXiv.2604.07870` (also present as PDF `/DOI`).
- **PDF checksum (measured 2026-09-24):** `https://arxiv.org/pdf/2604.07870` → HTTP 200, **52 pages, 626,424 bytes, SHA-256 `08f0a95b600c32bda145c036771f0994ca4d242168c0cc5c1a911fb22f59ad92`**. PDF metadata: `/Title` = "Skewness Dispersion and Stock Market Returns", `/arXivID` = `https://arxiv.org/abs/2604.07870v1`, `/DOI` = `https://doi.org/10.48550/arXiv.2604.07870`.
- **Full text read directly:** extracted with `pypdf` (119,354 characters) and read end-to-end for this record — §1 Introduction, §2 Data (§2.1 construction, §2.2 other predictors), §3 Quantitative results (§3.1 univariate, §3.2 bivariate, §3.3 out-of-sample incl. forecast-encompassing, §3.4 asset allocation), §4 Interpretation (§4.1 rational/behavioral channels, §4.2 information diffusion around FOMC, §4.3 kurtosis dispersion), §5 Conclusion, Tables 1–8, Figures 1–3, references, Appendix Tables A1–A3. Every quantitative claim below carries a Table/Section anchor from this pinned v1.
- **Sample period (source):** **December 2000 – December 2022** (high-frequency prices from **Kibot**, December 2000 to December 2022, §2); out-of-sample estimation uses an **expanding window from December 2005 (t₀) to December 2022 (T)** (§3.3, §3.4).
- **Universe (source):** **6,770 US stocks listed on NYSE, AMEX and NASDAQ that are also present in CRSP** (§2); the *dependent* variable throughout is the **S&P 500 log excess return** (§3.1) — i.e. an aggregate market-timing design, not a stock-level long-short cross-section.
- **Transaction-cost treatment (source):** **not stated in source** (`data gap`). Verified by keyword scan over the complete extracted v1 text: `cost`/`costs`/`transaction cost` → **0 occurrences**; `turnover|slippage|bid-ask|commission|borrow|friction|short sale|short-sell|fees` → **0 occurrences**. §3 Methods, §3.1–§3.4 Experimental setup and §3.4 asset-allocation formulation were read in full; no cost, spread, fill, borrow, or impact term appears in any equation or portfolio rule. This is recorded as a gap and **not** inferred to mean costs are zero — see Execution assumptions and Negative evidence.
- **Core performance numbers (source-reported, all from pinned v1):** Table 1 Panel A (full sample, mean-based `SD75−25`, Newey–West `h−1` lags): β = −0.099 (t = −2.95), −0.086 (−4.04), −0.071 (−3.37), −0.050 (−3.42) at h = 1/3/6/12 months, adjusted R² = 4.09/9.19/11.18/9.50. Table 3 (out-of-sample vs. historical average, Clark–West): R²_OOS = 2.91/6.12/7.85 (t = 2.49/3.95/3.71) at h = 1/3/6; stated ranges across the five `SD` specifications are 2.31–3.97% (h=1), 4.74–8.90% (h=3), 4.30–8.33% (h=6). Table 6 (out-of-sample mean-variance allocation): 1-month CER gains 709–875 bp and Sharpe 0.82–0.91 versus "240 basis points and 0.57 for the passive strategy" (§1 wording; Table 6 rows: `SD75−25` 8.36/0.89, `SD85−15` 8.75/0.91, `SD95−5` 7.09/0.82; Buy-and-hold 2.40/0.57; Prevailing mean CER 0.42). Table 7 Panel B (one-month-ahead, month split by FOMC): FOMC β = −0.133 (t = −3.28), pre-FOMC −0.108 (−2.97), post-FOMC −0.080 (−1.95), **non-FOMC −0.018 (−0.31), adjusted R² 0.15**.
- **Pre-write dedup (deterministic, whole repository):** ripgrep across **all 914 tracked `*.md` records plus `coverage_manifest.csv`** for `2604.07870`, `10.48550/arXiv.2604.07870`, exact title `Skewness Dispersion and Stock Market Returns`, `skewness dispersion`, `Babiak`, `Barunik`, `Kurka` → **0 matches**. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup. Wiki Brain `kb_search`: `"skewness dispersion equity premium prediction"` → 0 results; `"realized skewness stock market returns"` → 7 hits, **none** of which covers this paper or this predictor. Nearest same-domain sibling records in this repository are different sources with different mechanisms: `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md` (model-combination forecasting of the premium), `conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04.md` (nonlinear time-series return decomposition), `beta-times-quantity-noise-trader-flow-factor-pricing-2026-09-07.md` (cross-sectional factor pricing), `supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04.md` (cross-sectional stock selection). None shares source identity or the inter-percentile realized-skewness-dispersion signal → no duplicate.
- **Replication assets:** no GitHub link, no replication-code reference and no data-availability statement for the authors' own construction appears anywhere in v1 (keyword scan for `github|replication|code|dataset` returned only generic thank-you notes to other authors' public datasets) → `data gap`. The core inputs (Kibot 5-minute US equity data; CRSP linkage) are commercial, so independent replication requires a paid feed or a documented substitute.

## Economic mechanism

### Source-reported

The authors propose a novel aggregate-return predictor, **skewness dispersion**: the inter-percentile range (main specification `SD75−25`, robustness `SD80−20`/`SD85−15`/`SD90−10`/`SD95−5`) of the *cross-sectional distribution of daily realized skewness* computed from 5-minute intraday returns, averaged over the last five trading days of each month (§2.1). Elevated dispersion means the cross-section is unusually heterogeneous in return asymmetry — some stocks with pronounced positive jumps, others with pronounced negative jumps. The source reports a **significantly negative relation with future S&P 500 returns over 1–12 month horizons**, robust to overlapping/non-overlapping estimation, recession exclusion, persistence-robust IVX inference, out-of-sample tests against the historical average, and incremental to a benchmark set of 50 established predictors (§3.1–§3.3).

Stated rationale (§1, §4): skewness is well known to explain *individual* stock returns, but the *average* firm-level skewness masks cross-sectional variation; if investors disagree about asymmetric payoffs, that heterogeneity shows up in the *dispersion* of skewness. The mechanism section reports two complementary channels (§4.1–§4.2): (a) a **risk channel** — `SD75−25` is contemporaneously negatively correlated with market option-implied variances, variance risk premia and average stock correlation, i.e. high dispersion is a "good times / lower aggregate risk" state that demands lower subsequent returns; (b) a **behavioral / information channel** — dispersion correlates with AAII bullish (+0.30) and bearish (−0.28) survey sentiment and is most strongly correlated of all 50 controls with **aggregate short interest** (Table A2: `SIIoos` 0.32, `SIIis` 0.27), while being unrelated to analyst/investor disagreement measures; predictive power is **sharply concentrated in FOMC-adjacent months** (Table 7 Panel B), which the authors read as gradual incorporation of macro news into prices ahead of salient announcements. §4.3 shows cross-sectional **kurtosis** dispersion predicts too but generally more weakly, so asymmetry rather than generic tail heaviness is the active ingredient (Table 8).

### Research interpretation

Falsifiable hypothesis in normalized form: **cross-sectional heterogeneity in return asymmetry is a state variable for the aggregate equity premium** — when the stock cross-section is unusually split between right-tailed and left-tailed names (high `SD`), expected market returns over the next 1–12 months are lower, because that state reflects either complacent/low aggregate risk or belief heterogeneity that is being resolved around scheduled macro information releases. Component roles:

```text
Signal (primary): monthly cross-sectional inter-percentile range of daily realized
                  skewness (5-minute returns), averaged over the last five trading
                  days of month t  →  negative forecast of S&P 500 log excess return
Portfolio layer:  mean-variance weight on the market vs. risk-free bill, refreshed
                  at horizon h (source's §3.4 rule; this is the only tradable form
                  the source actually specifies)
Diagnostic (not part of the source's rule): predictive power concentrates in
                  FOMC pre/during/post months (Table 7 Panel B)
```

The hypothesized frictions are (i) short-sale constraints plus heterogeneous beliefs (the source invokes Miller 1977 in §4.1, while reporting that disagreement proxies do *not* correlate with `SD`), and (ii) information-arrival dynamics around scheduled macro announcements (FOMC). No claim is made that every component contributes alpha; the FOMC conditioning is a source-reported *diagnostic*, and turning it into an entry filter would be a `research-proposed` operationalization (see Falsification plan). This is a **market-timing / equity-premium hypothesis**, not a cross-sectional stock-selection strategy: the source never sorts individual stocks into portfolios.

## Signal

All items below are **source-reported** unless explicitly labeled `research-proposed` / `research-defined` / `underspecified`.

- **Formation timestamp:** daily realized skewness per stock `RS^s_t` is computed from the 78 five-minute log returns of day `t` (09:30–16:00 EST grid, last price within each previous five-minute window; §2, eq. (1)–(2)). The daily cross-sectional dispersion `SD^{a−b}_t` is the `a`-th minus `b`-th percentile of that day's cross-section. The **monthly** predictor is the **mean of `SD` over the last five trading days of each month** (median used as the robustness variant; §2.1, Figure 1 caption). Availability: all inputs are same-day intraday prices and month-end aggregation — the predictor for month `t` is fully observable at the close of the last trading day of `t`.
- **Lookback:** per-day lookback = one trading session of 78 five-minute returns; monthly aggregation lookback = last 5 trading days of the month (endpoints inclusive, per "over the last five trading days of each month"). Warm-up period / minimum number of stocks required for the cross-sectional percentiles to be computed: **`data gap`** (not stated).
- **Predictive relation:** `r_{t,t+h} = α_h + β_h SD^{a−b}_t + ε_{t,t+h}`, with `r` the S&P 500 log excess return and `h ∈ {1, 3, 6, 12}` months (§3.1, eq. (3)); source-reported sign is **β < 0** at all horizons and in all five percentile specifications (Table 1).
- **Long entry / short entry:** the source does not run a long-short stock portfolio. Its only tradable form is the §3.4 mean-variance allocation executed "at the end of period t": `w^h_t = (1/γ) · r̂_{t,t+h} / σ̂²_{t,t+h}` with **γ = 3**, equity weight **clamped to [−0.5, 1.5]**, rebalanced at frequency `h`, investing in the **value-weighted market excess return vs. the risk-free rate** (Table 6 caption; §3.4). A negative forecast therefore produces a net short-market weight down to −0.5.
- **Exit / holding period:** holding period equals the forecast/rebalance horizon `h` (1, 3 or 6 months in the reported allocation results; 12-month results appear in the regressions). Positions are continuously re-forecast at the same cadence; no stop, no tactical exit, no re-entry rule beyond the scheduled rebalance (§3.4 "the weights are rebalanced at the same frequency as the forecast horizon").
- **Estimation protocol (part of the signal):** out-of-sample forecasts use an **expanding window starting December 2005**, re-estimated each month (§3.3, §3.4); benchmark for forecast accuracy is the historical average of `h`-month excess returns.
- **Parameters:** percentile pairs `{75−25, 80−20, 85−15, 90−10, 95−5}` (source's grid; `75−25` is the headline spec), aggregation mean vs. median (both reported), γ = 3, weight clamp [−0.5, 1.5], horizons `h ∈ {1,3,6,12}` — all **source-specified** and described by the source as common modeling choices (Campbell and Thompson 2008; Rapach et al. 2016; Han and Li 2021), not tuned on the evaluation sample in any way the source discloses.
- **`underspecified` items:** (a) §3.4 says "compute **realized volatility** as a proxy for the volatility forecast" while eq. (6) divides by `σ̂²` — whether the proxy enters squared is not stated; (b) the instrument used to take the −0.5 market weight (index futures, inverse ETF, index short) is not specified; (c) minimum cross-sectional breadth / missing-stock handling when computing daily percentiles is not specified; (d) no explicit rule for trading-cost-aware rebalancing (none is modeled at all). The signal is therefore **reconstructable for the predictor and the allocation formula, but not for executable fills**.

## Required data

- **Instrument / universe:** predictor input = individual common stocks of 6,770 NYSE/AMEX/NASDAQ issuers also present in CRSP (Dec 2000–Dec 2022); trading instrument = value-weighted US equity market (S&P 500 as the return target) plus a risk-free bill.
- **Venue / market type:** US cash equities for measurement; the allocation itself is implied for a broad equity index vehicle (unspecified — `underspecified`).
- **Timeframe / fields:** 5-minute intraday prices 09:30–16:00 EST (78 returns/day) from **Kibot**; monthly S&P 500 log excess return and risk-free rate; NBER recession dates (Panel B of Table 1); FOMC meeting calendar (Table 7 Panel B); realized-volatility series for the variance proxy (§3.4). The 50 comparison predictors (Appendix Table A1) are needed only to replicate the incremental-value claims, not to trade the signal.
- **Point-in-time:** predictor uses only data through the last trading day of month `t`; the source allocates "at the end of period t" (§3.4), so no look-ahead is implied by the stated timing. Publication lags do not apply to the price-based predictor itself.
- **Timestamp / timezone:** US equity session times in EST as recorded by Kibot; monthly boundaries are calendar trading days.
- **Missing data:** **`data gap`** — no rule for suspensions, halts, stocks with incomplete sessions, or minimum names per day when computing cross-sectional percentiles; no survivorship or delisting handling statement beyond "listed … and also available in CRSP".
- **Funding / fee / spread needs:** none specified by the source (`not stated in source`); any net-of-cost replication must add maker/taker-or-commission, index-tracking spread, and shorting/borrow or futures basis costs itself (`research-proposed`).

## Execution assumptions

- **Source assumptions (as stated):** signal-to-order timing = end of month `t` (predictor observability) with weight refresh every `h` months; allocation is a single line between market and risk-free asset; weight clamp [−0.5, 1.5]; γ = 3; expanding-window estimation from Dec 2005.
- **Order type, fill model, latency, signal-to-order delay beyond the monthly cadence, liquidity/participation caps, position limits beyond the weight clamp, leverage/margin, borrow availability and cost for the −0.5 short-market weight, funding, slippage, spread, market impact, partial fills:** **not stated in source** — confirmed by full-text keyword scan (`cost`, `fees`, `slippage`, `bid-ask`, `commission`, `borrow`, `friction`, `turnover` all 0 occurrences in v1). §3 Methods / §3.4 formulation were read directly; no cost term exists in any equation.
- **Net-vs-gross status:** because no cost is modeled, every reported CER gain, Sharpe ratio and R² is **gross** of trading frictions by construction; the record marks them `source-reported (gross)` and does **not** treat "no cost mentioned" as "cost = zero".
- **Capacity / impact:** `not stated in source`.
- **`research-proposed` (ours, not the source's):** implement the monthly switch through a liquid index vehicle (e.g. index futures or a broad ETF), charge κ bps per unit of absolute turnover in the equity weight (grid in Falsification plan), allow the weight clamp as-is, and log realized turnover so the net CER can be computed. Nothing here is validated.

## Evidence

### Source-reported

All figures below are third-party claims from Babiak, Baruník and Kurka, arXiv:2604.07870v1 (Dec 2000–Dec 2022, S&P 500 / US equities, **gross of any cost**), and have not been independently reproduced. Table/Panel anchors are given for every number.

- **In-sample univariate (Table 1, mean `SD`, Newey–West `h−1` lags):** Panel A (Full sample): `SD75−25` β = **−0.099 (t −2.95)**, **−0.086 (−4.04)**, **−0.071 (−3.37)**, **−0.050 (−3.42)** at h = 1/3/6/12; adjusted R² = 4.09 / 9.19 / 11.18 / 9.50 — all five percentile specs carry `***` (1%) at every horizon in Panel A and in Panel D (IVX). Panel B (Excluding NBER recessions): e.g. `SD75−25` h=1 −0.095 (−2.96); significance is at least 5% for most cells but drops to 10% for `SD95−5` at h=6 (−0.011, t −1.90). Panel C (non-overlapping observations, Martin 2017): `SD75−25` h=1 −0.099 (−2.95), h=3 −0.083 (−2.74), h=6 −0.074 (−2.55), h=12 −0.052 (−2.59), with `SD95−5` h=12 at 10% (−0.013, t −1.87). Panel D (IVX, Kostakis et al. 2015): `SD75−25` Wald = 10.98 / 16.54 / 17.79 / 13.50 across h (critical values 2.706 / 3.842 / 6.634 for 10% / 5% / 1%) — i.e. significance survives persistence-robust inference. Note: §3.1's prose says Panel B coefficients "remain statistically significant at least at the 5% confidence level", which its own `SD95−5` h=6 cell (10%) contradicts — a minor source-internal inconsistency, recorded rather than smoothed over.
- **Bivariate increment (Table 2, Panels A–E):** `SD75−25` stays significant at 1% against each of the four alternative skewness measures, all six stock-cross-section controls, all sentiment controls, all variance controls and all macro/financial controls; market skewness (`Skm`) and average skewness (`Skew`, `Skvw`) become insignificant once `SD` is included (Panel A). The source states that of 50 controls, **only six** show incremental power in *both* in-sample and OOS tests (§1 and footnote 2).
- **Out-of-sample accuracy (Table 3, expanding window Dec 2005 → Dec 2022, Clark–West):** `SD75−25` mean-based R²_OOS = **2.91 (t 2.49) / 6.12 (3.95) / 7.85 (3.71)** at h = 1/3/6; across all specs and mean/median variants the source states ranges **2.31–3.97% (1m), 4.74–8.90% (3m), 4.30–8.33% (6m)** (§3.3.1). Figure 2 shows the cumulative forecast-error advantage over the historical average is not driven by single events (with noted declines at end-2011, COVID and 2022 at h=1).
- **Forecast encompassing (Table 5):** the optimal weight λ on the `SD75−25` forecast exceeds 0.5 in all but the attention-index case, and `H0: λ = 0` is rejected at 10% (5%) in all (a vast majority of) control–horizon combinations; e.g. vs. dividend yield at h=3 λ = 0.95 (t 3.31), vs. the attention index at h=3 λ = 0.31 (t 1.58).
- **Economic value (Table 6, out-of-sample allocation, γ = 3, weights [−0.5, 1.5], gross):** 1-month CER gains **709 bp (`SD95−5`) – 875 bp (`SD85−15`)** with `SD75−25` = 836 bp, Sharpe **0.82 – 0.91** (`SD75−25` = 0.89), versus passive buy-and-hold **CER 2.40 / Sharpe 0.57** and prevailing-mean CER 0.42 (Table 6 rows; §1 states "240 basis points and 0.57 for the passive strategy"). 3-month: CER gains 395–469 bp, Sharpe 0.69–0.74. 6-month: CER gains 445–729 bp, Sharpe 0.78–0.94. Figure 3 shows `SD75−25` wealth pulling ahead of benchmarks after the GFC.
- **Mechanism splits (Table 7):** Panel A — high AAII bullish-bearish regime h=1 β = **−0.164 (−4.32)**, R²_adj 13.45 vs. low regime −0.072 (−1.56, insignificant at h=1); Baker–Wurgler low-sentiment regime is stronger (−0.111, −2.14). Panel B — FOMC month **−0.133 (−3.28), R²_adj 7.08**; pre-FOMC −0.108 (−2.97); post-FOMC −0.080 (−1.95); **non-FOMC −0.018 (−0.31), R²_adj 0.15**.
- **Placebo-like robustness within the source (Table 8):** kurtosis dispersion `KD75−25` also predicts (h=1 β −0.034, t −3.34; OOS R² 4.91, t 3.09), but is weaker at longer horizons — the source argues this isolates asymmetry rather than generic tail risk.
- **Correlations (Table A2 / §4.1):** `SD75−25` vs. aggregate short interest `SIIoos` **+0.32\*\*\***, `SIIis` +0.27\*\*\*; vs. average stock correlation **−0.28\*\*\***; vs. implied variance −0.18\*\*\*; vs. all disagreement measures statistically insignificant; AAII bullish +0.30 / bearish −0.28 (§4.1 text).
- **Asset class boundary:** this is **US-equity evidence only** (S&P 500 timing built from a US stock cross-section). It must not be read as crypto evidence.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **The source's own table contradicts a "pervasive" version of the hypothesis:** non-FOMC months show β = −0.018, t = −0.31, adjusted R² = 0.15 (Table 7 Panel B). The edge is episodic and concentrated in FOMC pre/during/post months, so a rule that stays invested every month spends the non-FOMC part of the sample with **no demonstrated predictive power**.
2. **Several existing predictors beat it on the economic metric the source itself reports:** attention index CER gain 947 bp and Sharpe 1.12 at h=1, short-interest index CER gain 927 bp / Sharpe 0.93 at h=3 and 1,109 bp / Sharpe 1.12 at h=6 (Table 6). Skewness dispersion is *not* the top predictor in the source's own horse race.
3. **Regime splits are mixed and one leg is null:** under the AAII bullish-bearish split, the h=1 coefficient in the *low* regime is −0.072 with t = −1.56 (insignificant, Table 7 Panel A); under the Baker–Wurgler split it is the *low*-sentiment regime that is stronger — i.e. the two behavioral conditionings point in opposite directions, which the source itself calls "mixed results" (§4.1).
4. **Zero cost/borrow/turnover treatment:** full-text keyword scan of v1 returns 0 occurrences of `cost(s)`, `transaction cost`, `fees`, `slippage`, `bid-ask`, `commission`, `borrow`, `friction`, `short sale`, `turnover`. The allocation can hold a −0.5 market weight, yet no borrow/futures-basis or rebalancing cost appears anywhere → CER gains and Sharpe ratios are **gross** and untested against frictions (`not stated in source`, not zero).
5. **Sample and review status:** data end **December 2022** (no post-2022 out-of-sample evidence), 265 monthly observations total with OOS beginning Dec 2005; the paper is a **v1 preprint with no journal reference** (52 pages, single version, no peer review on record as of 2026-09-24).
6. **Replication is blocked by commercial data plus missing artifacts:** inputs are Kibot 5-minute US equity prices and CRSP linkage, and v1 contains no replication-code, repository or data-availability statement (`data gap`) — so nobody outside the authors has, on the record, re-derived these numbers. Absence of a published failed replication is not evidence that none exists.
7. **Estimator fragility acknowledged by the source itself:** at 5-minute frequency realized skewness "in the limit captures mainly the jump part" and does not capture the leverage effect (footnote 5, §2.1), and kurtosis-type higher moments are outlier-sensitive — the source reports the wider `SD95−5` spec has the weakest t-stats (Table 1) and that broader kurtosis ranges degrade results (§4.3).
8. **Engaged literature is itself largely negative:** the source frames its contribution against Welch and Goyal (2008) and Goyal, Welch and Zafirov (2024), which document that most proposed premium predictors fail out-of-sample; the source states "most established variables exhibit weak out-of-sample performance in our sample" (§1). A single surviving predictor in that literature carries the standard selection-bias concern.

## Falsification plan

Items labeled `research-defined` are Scout-chosen acceptance/failure cutoffs; items labeled `research-proposed` are operationalizations absent from the source.

1. **True forward out-of-sample (F1, `research-defined`):** extend the predictor beyond Dec 2022 to the latest month on an independent 5-minute feed (or a documented daily-return approximation, `research-proposed`). Fail if, on 2023-01 → latest, expanding-window R²_OOS ≤ 0 **or** the Clark–West one-sided t-statistic for h=1 is < 1.645 against the historical-average benchmark. Action: hypothesis rejected for adoption; record stays research-only.
2. **Net-of-cost survival (F2, `research-defined` + `research-proposed` grid):** re-run the §3.4 allocation charging κ ∈ {10, 20, 30, 50} bps per unit of absolute turnover in the equity weight, including index-tracking spread and the cost of the short-market leg. Fail if the annualized CER gain over the prevailing-mean benchmark is ≤ 0 at κ = 20 bps, or if realized turnover exceeds 100% of the equity book per month on average (`research-defined`).
3. **FOMC-conditioning placebo (F3, `research-defined`):** replicate Table 7 Panel B. The *pervasive* version already fails on the source's own numbers (non-FOMC t = −0.31); an event-conditioned version survives only if, on a fresh sample, FOMC-adjacent months keep β < 0 with |t| ≥ 1.96 while non-FOMC months remain statistically indistinguishable from zero. If non-FOMC months also turn significant with the opposite sign, the mechanism story is wrong.
4. **Parameter perturbation (F4, `research-defined`):** re-estimate across the source's percentile grid {75−25, 80−20, 85−15, 90−10, 95−5} × γ ∈ {1, 2, 3, 4, 5} (`research-proposed` γ grid) × clamp ∈ {[0, 1], [−0.5, 1.5], [−1, 2]} (`research-proposed`). Fail if the sign of β flips or loses significance at 5% in a majority of specifications, or if the net CER gain is positive in fewer than 60% of the γ × clamp cells (`research-defined`).
5. **Shuffled-label placebo (F5, `research-defined`):** 500 block-shuffles of the monthly `SD` series (`research-proposed` count of 500 and block length of 12 months). Fail if the empirical |t| at h=1 does not exceed the 95th percentile of the null |t| distribution, or if ≥ 2.5% of shuffles produce a net CER gain as large as the real one at κ = 20 bps.
6. **Benchmark competition (F6, `research-defined`):** on the same sample, the signal must beat (a) the historical average, (b) buy-and-hold, and (c) at least the two rivals the source itself identifies — attention index and short-interest index — on net CER. Failing (c) does not falsify the mechanism but does falsify any claim of *dominance*.
7. **Ablation / mechanism probes (F7, `research-proposed`):** (i) replace realized skewness with a daily-close skewness approximation to test whether the 5-minute jump content is essential; (ii) extend the announcement split beyond FOMC to CPI/NFP months; (iii) test whether the aggregate-short-interest channel (Table A2) is doing all the work by orthogonalizing `SD` against `SIIoos`. Failure of (i) with success of (iii) would reframe the signal as a short-interest proxy rather than a skewness-dispersion signal.
8. **Alternative universe (F8, `research-proposed`):** replicate the construction on a non-US developed index cross-section to test whether the effect is a US/FOMC-specific artifact. Action on failure: mechanism classified as US-macro-announcement-specific; no portability claims.

## Crypto portability

**unproven.** The source contains zero crypto evidence — it is built on a 6,770-stock US cross-section, a 9:30–16:00 EST session, CRSP/Kibot data, S&P 500 excess returns, and its strongest mechanism evidence is concentration around **FOMC** months. This is a **ported hypothesis**, not crypto empirical evidence.

- **Mechanically portable part (`research-proposed`):** the construction itself (5-minute bars → daily realized skewness per asset → inter-percentile range across a liquid cross-section → monthly average over the last five days → negative forecast of a broad-market return) can be recomputed on top-N crypto pairs, which do have continuous 5-minute data.
- **Why it may not transfer:** (a) crypto has no point-in-time analogue of the aggregate short-interest and analyst-disagreement control set that the source uses to identify its channel; (b) the FOMC-event concentration would need a crypto-native conditioning calendar (macro prints do move crypto, but the source demonstrates nothing about it); (c) the cross-section is far smaller and turnover-heavy — percentile estimates over a few hundred symbols are noisier and dominated by listing/delisting churn; (d) 24/7 sessions mean "last five trading days of the month" and candle boundaries do not align with the source's EST session definition; (e) the tradable layer (spot vs. perpetual vs. index futures) changes funding, borrow and mark-price mechanics the source never models; (f) venue fragmentation and index-price basis add an execution layer absent from a single consolidated US cash index.
- Crypto portability of a research capture is not authorization to trade.

## Limitations

- `data gap` — transaction costs, spread, slippage, borrow/futures-basis, turnover, capacity and fill model: **not stated in source** (0 keyword hits across the full v1 text); results are gross.
- `data gap` — no replication code, repository or data-availability statement in v1; core inputs (Kibot, CRSP) are commercial.
- `data gap` — no minimum-cross-section-breadth, missing-session, suspension or survivorship rule for the daily percentile computation.
- `underspecified` — whether the §3.4 "realized volatility proxy" enters eq. (6) squared; the instrument behind the −0.5 market weight; the exact basis of the Table 6 buy-and-hold row (the caption labels all columns "CER gain", while §1 compares 240 bp directly against the gains as if it were a level — the two readings differ by the prevailing-mean CER of 0.42 and are not reconciled in the source).
- `underspecified` — Table 1's caption places "(excluding NBER recessions)" parenthetically after the joint Panel A (B) description even though Panel A is labeled "Full sample"; the panel labels and §3.1 text resolve it, but the typeset caption is ambiguous.
- `not independently reproduced` — no third party has re-derived Tables 1–8 on the record as of 2026-09-24.
- `unproven` — crypto portability (see above); also unproven for any post-2022 period.
- Sample/design: 265 monthly observations (Dec 2000–Dec 2022) with the OOS segment starting Dec 2005; single market, single country, single index; preprint v1 without peer review; the source itself notes most competing predictors fail OOS (Welch–Goyal 2008; Goyal et al. 2024), which is both its motivation and a caution about selection in this literature.
- Evidence-class boundary: every performance figure above is `source-reported (gross, US equities)` and must not be re-labeled as validated alpha, crypto evidence, or our own result.

## Implementation status

`not-implemented`. Nothing from this record has been implemented in our research stack: no predictor pipeline, no portfolio backtest, no Qlib full backtest, no production card, no Paper, Testnet or Live run. The record is a normalized research capture only; the body of this document is the only artifact produced by this run.

## Adoption boundary

This record being present in this repository means only that normalized research material entered the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

Pre-write search of Hermes Wiki Brain found **no record covering this paper or this predictor**: `kb_search "skewness dispersion equity premium prediction"` → 0 results; `kb_search "realized skewness stock market returns"` → 7 hits (e.g. `quant/drift-regime-gated-cross-sectional-value-reversal-2026-09-05.md`, `quant/futures-quad-trend-carry-skew-vov-composite-2026-09-11.md`), none of which shares this source identity or the inter-percentile realized-skewness-dispersion signal — so no Wiki link is asserted here rather than fabricating one. Nearest same-domain sibling records in this repository (different sources, different mechanisms): `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md`, `conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04.md`, `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md`, `beta-times-quantity-noise-trader-flow-factor-pricing-2026-09-07.md`.

## Sources

- Mykola Babiak, Jozef Baruník, Josef Kurka, *"Skewness Dispersion and Stock Market Returns"*, arXiv preprint **arXiv:2604.07870v1 [q-fin.GN]**, submitted 9 April 2026.
  - Abstract: https://arxiv.org/abs/2604.07870
  - PDF (pinned v1, read in full for this record on 2026-09-24): https://arxiv.org/pdf/2604.07870 — 52 pages, 626,424 bytes, SHA-256 `08f0a95b600c32bda145c036771f0994ca4d242168c0cc5c1a911fb22f59ad92`
  - Canonical arXiv DOI: https://doi.org/10.48550/arXiv.2604.07870
  - Publication status: preprint only — no `journal_ref`, no publisher DOI as of 2026-09-24.
