---
schema: strategy-research-record-v1
title: Relative-Value Price-Ratio LightGBM Classifier with a Trend AND Hurst Regime Gate on Three Newly Listed Binance USDS-M Perpetuals - Walk-Forward Negative Audit (Scientific Reports 16:29336, DOI 10.1038/s41598-026-70423-7)
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - relative-value
  - machine-learning
  - regime-gate
  - hurst-exponent
  - event-time-bars
  - walk-forward
  - negative-result
status: research-only
confidence: high
source_as_of: 2026-09-21
sources:
  - "https://www.nature.com/articles/s41598-026-70423-7 - Scientific Reports 16(1), Article 29336 (2026), DOI 10.1038/s41598-026-70423-7, Received 07 June 2026 / Accepted 02 September 2026 / Published 21 September 2026 / Version of record 21 September 2026, open access CC BY 4.0; full article HTML pinned and read end to end on 2026-09-28"
  - "https://www.nature.com/articles/s41598-026-70423-7/tables/1 through /tables/6 - the six table pages of the same article (Table 1 inventory, Tables 2-4 original fixed-split precision, Table 5 walk-forward model benchmarks, Table 6 LightGBM and rule ablation), each fetched and read on 2026-09-28"
  - "https://doi.org/10.1038/s41598-026-70423-7 - publisher DOI of record"
  - "Binance Data Vision archive for USDS-M perpetual-futures trades - named by the article Methods as the trade source (the article prints no URL for it); sample March-May 2025, 28,157,374 trades across MLNUSDT, PLUMEUSDT, SIRENUSDT"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Stated '61.5% average gap reduction' (Results, Original fixed-split record) cannot be reproduced from the printed Tables 2-4 under any of three natural aggregation conventions: research-computed 62.96% (ratio of the mean unfiltered gap 0.0378 to the mean filtered gap 0.0140), 33.65% (mean of the nine per-cell reduction ratios) and 68.50% (mean reduction over the seven improving cells). The article does not state which aggregation it used; left unreconciled, not resolved by the Scout."
  - "F1 column versus the printed precision/recall columns: Table 5 and Table 6 columns are described only as 'macro means over nine pair/event-bar configurations and three forward folds', and the harmonic mean of the printed mean precision and mean recall differs from the printed F1 by up to +0.057 (research-computed: LightGBM 0.301 vs printed 0.251; logistic regression 0.246 vs printed 0.189; XGBoost 0.287 vs printed 0.235). Consistent with averaging cell-level F1 values rather than recomputing from means, but the exact aggregation (mean of per-cell F1 versus pooled confusion counts) is never printed; left unreconciled."
  - "Two printed gap cells disagree by 0.0001 with |validation - test| recomputed from the printed precision values (research-computed: Table 3 MLN/PLUME unfiltered printed 0.0736 vs 0.0735 from 0.4604 and 0.3869; Table 4 MLN/SIREN filtered printed 0.0128 vs 0.0129 from 0.5125 and 0.5254). Consistent with rounding of unrounded internal values, but the tables do not say so; left unreconciled."
  - "Data provenance tension inside one article: the Data availability statement says the datasets 'used and analyzed during the current study are available from the corresponding author on reasonable request', while Methods names the source as the public Binance Data Vision archive; the article carries no code availability statement, and the Limitations section states that 'The original source code, fitted models, and prediction vectors were unavailable'. Tables 2-4 therefore rest on an unverifiable submitted pipeline while Tables 5-6 rest on an independent public-data reconstruction that the authors themselves call 'not a bit-for-bit replication'; left unreconciled."
---

# Relative-Value Price-Ratio LightGBM Classifier with a Trend AND Hurst Regime Gate on Three Newly Listed Binance USDS-M Perpetuals - Walk-Forward Negative Audit (Scientific Reports 16:29336, DOI 10.1038/s41598-026-70423-7)

## Provenance

- **Primary source (canonical):** Hassanie, Souad; Atalay, Can; Khan, Talha Ali; Ali, Raja Hashim; Mateus, Cristhian David Caceres; Ahmed, Iftikhar (six authors, complete list exactly as printed in the article's Authors and Affiliations block and in the `citation_author` meta tags; no seventh author is hidden behind the collapsed byline). Article: *"Improving the robustness of binary classifiers in cryptocurrency exchange rate forecasts"*, **Scientific Reports volume 16, Article number 29336 (2026)**, **DOI `10.1038/s41598-026-70423-7`**, ISSN 2045-2322.
- **Affiliations as printed:** Department of Business, University of Europe for Applied Sciences, Potsdam, 14469, Germany (all six authors); CIRAME Research Center, Holy Spirit University of Kaslik, Jounieh, 446, Lebanon (Souad Hassanie only). Corresponding author: **Talha Ali Khan**. Contributions block: S.H. and C.A. conceived the experiments; T.A.K. and R.H.A. conducted them; C.D.C.M. and I.A. rewrote and reviewed the article; all authors drafted, reviewed and approved the final manuscript. Ethics: `The authors declare no competing interests.`
- **Version / dates (all four as printed, mutually consistent):** `Received: 07 June 2026`, `Accepted: 02 September 2026`, `Published: 21 September 2026`, `Version of record: 21 September 2026`. No preprint identifier, no arXiv ID and no SSRN ID appear in the article -> preprint status `not stated in source`; publication status is **peer-reviewed journal article, open access**.
- **License:** Creative Commons Attribution 4.0 International (`creativecommons.org/licenses/by/4.0`), stated in the Rights and permissions block; only short printed values and section references are normalised here.
- **Funding statement:** the article contains **no funding / acknowledgement section** -> `not stated in source` (never read as "no funding").
- **Pinned primary text:** `https://www.nature.com/articles/s41598-026-70423-7`, fetched 2026-09-28 as **331,503 bytes** of HTML, converted to **35,583 characters / 659 lines** and read end to end: Abstract, Introduction, Related work, Economic motivation and scope, Methods (Data/listing coverage/ratio construction; Features/trend cue/Hurst gate; Evaluation design and baselines), Results (Original fixed-split record; Walk-forward model benchmarks; Component ablation/coverage/costs; Hurst-threshold sensitivity and seed stability), Discussion, Limitations, Future work, Conclusion, Data availability, the 21-item reference list, Author information, Contributions, Corresponding author, Competing interests, Rights and permissions and the citation block.
- **Pinned table pages (read 2026-09-28, each fetched separately):** `/tables/1` 164,405 bytes; `/tables/2` 164,421 bytes; `/tables/3` 164,433 bytes; `/tables/4` 164,433 bytes; `/tables/5` 164,531 bytes; `/tables/6` 165,377 bytes. **Every numeric value in the Evidence section below was transcribed from these seven pinned pages.**
- **Figures:** Figures 1-17 appear in the HTML only as image references plus captions; their underlying data values are not machine-readable from the pinned HTML -> any figure-only value is `data gap` (the article's Wilson intervals and per-cell curves are figure-level).
- **Underlying data (source-reported, Methods):** the public **Binance Data Vision archive for USDS-M perpetual-futures trades**, March-May 2025 files, **28,157,374 trades** total, split **MLNUSDT 6,809,556 / PLUMEUSDT 6,289,933 / SIRENUSDT 15,057,885**; first archived observations 31 Mar 08:45:08 UTC (MLN), 21 Mar 13:00:25 UTC (PLUME), 22 Mar 09:00:13 UTC (SIREN). The article prints no URL and no archive version hash for the feed -> `data gap` on feed snapshot identity.
- **Execution agent / provenance of the numbers:** the independent audit is an **author-run reconstruction from public trades**; the article states that the original source code, fitted models and prediction vectors were unavailable, so Tables 5-6 are an independent reconstruction and **not a bit-for-bit replication of the submitted Tables 2-4** (Limitations). No LLM or third-party agent is named anywhere in the article -> agent provenance `not stated in source`.
- **Source-quality classification:** primary peer-reviewed journal article with Methods, Results, Discussion, Limitations and six tables read directly from the publisher's pinned pages; **no secondary summary, search snippet or model-generated summary was used to fill any field.**
- **Repository deduplication audit (2026-09-28, whole checkout, hidden-inclusive):** `rg -uuu` over `/Users/hong/workspace/alpha-strategy-research` (including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, `coverage_manifest.csv`) for `s41598-026-70423-7`, `Improving the robustness of binary classifiers`, `Hassanie`, `MLNUSDT`, `PLUMEUSDT`, `SIRENUSDT`, `28,157,374`, `full AND-gate` and `event-time bars` returned **0 hits** before this draft; the positive control `novy-marx` returned **14 files** in the same command, so the search was live; `coverage_manifest.csv` has no `70423` hit. `git log --oneline -20` was run as a convenience glance only and does not by itself satisfy dedup.
- **What this record is not:** it is not a record of a profitable strategy. It is a **negative-audit capture** of one specific gated classifier design (relative-value price ratio + LightGBM + trend AND Hurst gate) that the source itself concludes "failed its stronger audit".

## Economic mechanism

### Source-reported

- The article studies **relative-value price ratios**, `R_t = P_i,t / P_j,t`, over three pairs of newly listed Binance USDS-M perpetuals, and is explicit that a ratio alone "does not establish stationarity, cointegration, or mean reversion, and no such claim is made"; the construction is positioned as **distance-based relative-value logic** in the tradition of Gatev, Goetzmann and Rouwenhorst (2006), deliberately *not* as cointegration-based arbitrage (Introduction; Related work).
- The **engineering hypothesis under audit** (Introduction, three questions): (i) do event-time relative-value ratios show repeatable forward classification behaviour in this short sample; (ii) does Hurst conditioning add value beyond the model and trend rule; (iii) do apparent improvements survive component ablation, alternative classifiers, multiple seeds, walk-forward evaluation and cost stress. The framing hypothesis is that a **trend-continuation cue plus a rolling Hurst regime threshold** shrink the validation-to-test precision gap and make a classifier more deployment-ready.
- **Stated mechanism for why the filter was expected to help:** a regime gate should retain only observations in trending / persistent conditions and discard choppy ones, so the retained predictions should be more precise and more stable forward. The article's own contribution claim is narrow - "an auditable event-time implementation, a component-level stress test, and explicit separation of predictive performance from prediction coverage" - and it credits Sidhu et al. (SSRN 3824032) with Hurst-segmented machine-learning models and Bui & Slepaczuk (Physica A 592, 126784) with Hurst-regime-conditioned pair trading as prior art.
- **Stated mechanism for the observed failure (Discussion):** "The trend condition and Hurst condition mainly suppress positive predictions." Suppression can raise precision in some cells, but in the aggregate it removes most true positives, so coverage collapses and no cost-robust edge appears. The source adds that Hurst may still be useful as a *descriptive* regime variable, but the data "do not justify a universal 0.40 boundary".
- **Stated methodological thesis (Abstract, Discussion, Conclusion):** a small generalization gap, discrimination, coverage and net return are four separate questions; "a small validation-to-test gap near a precision of 0.5 can simply describe stable random-like behavior". The article's declared outcome is "a reproducible negative stress test of a plausible engineering idea".
- The **economic motivation block (equations 1-3)** is explicitly labelled conceptual: a long/short single-trade growth factor with leverage `L`, fee `f` and proportional slippage factors, plus the geometric expected-growth condition `E[g] = (g_win)^P (g_loss)^(1-P) > 1`. The source states these equations are retained "as economic motivation, not as evidence of realized profitability".

### Research interpretation

- **Hypothesis in falsifiable form (Scout framing):** on event-time bars of newly listed Binance USDS-M perpetual price ratios, adding a positive trend-continuation cue **and** a rolling Hurst threshold to a binary LightGBM direction classifier increases forward precision enough to survive a 10 bp round-trip cost while keeping economically useful signal coverage. On the source's own three-month, three-contract sample this hypothesis is **rejected**: the AND-gate lowers precision (0.511 -> 0.473), collapses recall (0.213 -> 0.014) and coverage (20.8% -> 1.34%), and every cost-adjusted accepted-signal return is negative.
- **Component roles (as normalized from the source):**
  - *Regime:* rolling Hurst estimate over the preceding 100 closes (log lagged-difference dispersion slope, lags 2-20, clipped to [0,1]), threshold `h` in {0.40, 0.45, 0.50, 0.55, 0.60}, selected on validation precision only.
  - *Primary signal:* LightGBM binary classifier predicting whether the **next event bar's close exceeds its open**, from lagged ratio-bar features.
  - *Confirmation:* trend cue `T_t = 1[log(C_t/C_t-1) > 0 and C_t > EMA_10,t]`.
  - *Risk / exit:* **none specified** - there is no stop, no take-profit, no position limit and no volatility sizing anywhere in the article; the only "risk layer" is the flat cost deduction used in the stress test. Any stop, sizing or exit rule applied downstream is **`research-proposed`**, not source-reported.
- **Mechanism in market terms (Scout reading):** this is a **coverage-reduction device**, not an alpha source. The gate admits long-only positive predictions (`1[M_t=1]`), so the audited object is a one-sided long signal on a ratio; precision near 0.47-0.51 with 1-21% coverage is consistent with chance-level discrimination plus thin sampling, and the economic question is settled by the cost ladder rather than by the gap statistic.
- **Boundary:** the source refuses to upgrade any of this into a deployable claim - "not evidence of a universally robust or deployable system", "proof-of-concept and reconstruction audit", "live paper trading should be attempted only after a fully specified cost model shows positive performance on an untouched historical period". Nothing in this record changes that boundary.

## Signal

All items below are **source-reported** unless explicitly marked `research-proposed`, `research-defined` or `data gap`.

1. **Ratio formation (Methods, "Data, listing coverage, and ratio construction").** For each pair, take the **union of trade timestamps**; carry each leg's most recently observed trade price forward; emit the ratio **only after both legs have been observed** (deterministic as-of rule, stated as look-ahead-free but able to retain a stale leg). Ratios analysed: **MLN/SIREN, MLN/PLUME, SIREN/PLUME**. Timestamps are exchange timestamps sorted together with the trade identifier; no duplicate rows were found.
2. **Bars (formation timestamp).** **Event-time bars** containing **20, 50 or 1,000 ratio updates** (not clock time), with open/high/low/close = first/maximum/minimum/last ratio of the bar. The tradable timestamp of a signal is therefore the **end of an event bar**, whose wall-clock position varies with activity; the article gives no timezone conversion beyond stating that the first observations are UTC -> bar-to-wall-clock mapping is `data gap` at execution level.
3. **Features (all strictly past-and-current bar values):** lagged log returns, rolling volatility, high-low range, exponential moving-average distance, and relative-strength index. Rows with unavailable lags are discarded **before splitting**.
4. **Target:** `1` when the **next bar's close exceeds its open**, else `0`.
5. **Trend cue (Equation 4):** `T_t = 1[log(C_t / C_t-1) > 0 AND C_t > EMA_10,t]` with a **10-bar EMA**.
6. **Hurst gate (Equation 5):** `S_t(h) = 1[M_t = 1] * 1[T_t = 1] * 1[H_t > h]`, where `H_t` is the rolling Hurst estimate over the **preceding 100 closes**, computed as the slope of log lagged-difference dispersion against log lag over **lags 2-20**, clipped to **[0,1]**; candidate grid **h in {0.40, 0.45, 0.50, 0.55, 0.60}**; for each pair, bar size and fold the threshold is chosen **on validation precision**, with coverage as deterministic tie-breaker and the lower threshold as final tie-breaker; **the test fold is untouched during selection** (source-reported selection protocol).
7. **Entry / direction:** accepted signals are **positive (long) only** - the gate is `1[M_t=1]`, so a negative model prediction never produces a trade. The treatment of the short side (whether a symmetric short gate exists, or shorts are simply omitted) is **not stated in source** -> `data gap`.
8. **Exit / holding period:** the audited return is **one event bar** - the next bar's open-to-close return, deducted a fixed round-trip cost. No stop, take-profit, time-based exit beyond that bar, re-entry rule or overlapping-position rule is specified -> those are `data gap` / `research-proposed` downstream.
9. **Evaluation splits (source-reported):**
   - *Original submitted experiment (retained as a descriptive record only):* a single **60/20/20 chronological train/validation/test split** with LightGBM hyperparameter search on the training interval.
   - *Independent audit:* **three expanding folds** - training ends at **45%**, **60%** and **75%** of each configuration's usable series; the next **10%** is validation; the following **15%** is the forward test window (research-computed fold edges: 0-45/45-55/55-70, 0-60/60-70/70-85, 0-75/75-85/85-100 of the usable series). Preprocessing is fitted on **training data only**.
10. **Model grid (source-reported):** standardized **logistic regression, random forest, XGBoost, LightGBM** under a common feature set, plus LightGBM re-fitted under **seeds 11, 29, 47**; rule controls **trend only** and **trend + Hurst**; component ablations **LightGBM only, +trend, +Hurst, full AND-gate**; a passive price-ratio return over each test interval is reported separately "as a sample-dependence reference, not as a prediction baseline" (its numeric values are figure-level -> `data gap`).
11. **Metrics:** precision, recall, F1, balanced accuracy, average precision, accepted positive-signal count and coverage (Equation 6), with a **95% Wilson interval** on positive-signal precision and **configuration-level bootstrap intervals** described as descriptive because cells share assets and calendar periods; the nine fixed-split gap changes are tested with an **exact sign test** and an **exact paired Wilcoxon test**.
12. **Position sizing:** the audit is explicitly **unlevered** and reports the **average per-accepted-signal return**; no capital allocation, weighting between the nine configurations, portfolio construction, gross exposure or leverage is specified -> `underspecified` / `data gap`. Equations 1-3 introduce leverage only as an unexecuted conceptual illustration (source says so).
13. **LightGBM hyperparameters:** the original experiment used "hyperparameter search on the training interval"; the grid, budget, early stopping and the fitted values are **never printed** -> `data gap`.
14. **Parameters that are fixed design choices rather than fitted values (source-reported):** bar sizes {20, 50, 1000}, EMA window 10, Hurst window 100 closes, Hurst lag range 2-20, Hurst clipping [0,1], threshold grid {0.40...0.60}, fold cut-offs 45/60/75/10/15%, seeds {11, 29, 47}, cost ladder {0, 10, 20} bp. The source calls 0.40 "a prespecified candidate", states the candidate grid and 100-bar window "remain prespecified design choices", and states that **test outcomes never determine the threshold**.

## Required data

- **Instrument / universe:** three Binance **USDT-margined perpetual futures** - **MLNUSDT, PLUMEUSDT, SIRENUSDT** - and their three pairwise price ratios. Universe is **fixed and tiny by construction**; there is no liquidity screen, no minimum-history screen and no reconstitution rule because the contracts are simply the ones the reconstruction covered.
- **Venue / market type:** Binance USDS-M perpetual futures; **single venue**, crypto derivatives, no spot leg and no cross-exchange data.
- **Timeframe / data granularity:** **tick-level public trades** (exchange timestamp, trade identifier, price), aggregated into **event-time bars of 20 / 50 / 1,000 ratio updates**. Sample window **March-May 2025**; usable histories are shorter than three months because listing dates differ (Table 1).
- **Fields required:** per-trade exchange timestamp (UTC), trade identifier, trade price for each of the three contracts; derived: ratio, event-bar OHLC, log returns, rolling volatility, high-low range, EMA(10) distance, RSI, rolling Hurst statistic. **Price-only** - the source states its features omit funding, open interest, liquidations, order-flow imbalance and network information.
- **Fields named as required for a tradable reading but absent from the source's data:** order-book depth, bid-ask spread, queue position, latency, two-leg fill synchronisation, market impact, funding, borrow/margin state -> `data gap`, never zero.
- **Point-in-time / availability:** the as-of rule prevents look-ahead; **listing bias is first-order** - PLUME starts 21 Mar, SIREN 22 Mar, MLN 31 Mar, so fold windows differ per configuration and the earliest bars of each contract cover a launch period (source flags this in Table 1 and Limitations).
- **Timestamp / timezone:** exchange timestamps in **UTC** (first observations are printed with UTC); no clock synchronisation, no session boundaries (24/7 market) and no corporate actions apply -> no adjustment layer is described.
- **Missing data:** identifier discontinuities are logged as diagnostics, not as outages - **1,228 gap events / 1,329 missing identifiers (MLNUSDT), 500 / 516 (PLUMEUSDT), 1,684 / 1,812 (SIRENUSDT)**; maximum timestamp gaps per contract are **209.956 s / 257.298 s / 181.275 s** (Table 1). Carried-forward legs can be **stale**, which the source treats as an explicit limitation rather than hiding it with interpolation.
- **Cost / fee fields:** only a **flat round-trip deduction of 0 / 10 / 20 bp**; no fee schedule, no spread series and no funding series is consumed.

## Execution assumptions

Determined from a **Methods-level read** of "Economic motivation and scope", "Evaluation design and baselines", "Component ablation, coverage and costs", "Hurst-threshold sensitivity and seed stability", "Limitations" and "Future work" of the pinned article, plus a whole-document term scan of the 35,583-character extracted text.

- **Cost treatment (source-reported, explicit):** the empirical audit is **unlevered** and applies **fixed round-trip deductions of 0, 10 and 20 basis points to the next bar's open-to-close return** (Economic motivation and scope; repeated in Results). Research-computed check: the printed nets are exactly gross minus the deduction - LightGBM-only `+0.97 -> -9.03 -> -19.03` bp and full gate `-0.16 -> -10.16 -> -20.16` bp at 0 / 10 / 20 bp. Every headline net in this record is therefore a **flat-deduction net, not an execution-modelled net**.
- **What the cost model explicitly does not include (verbatim scope, section "Economic motivation and scope"):** funding, spread variation, two-leg market impact, borrow constraints and latency are **not modelled**; the Results add that these "do not represent a two-leg executable portfolio". Equations 1-3 (leverage, fee, proportional slippage) are declared conceptual and are **not** used to produce any empirical number.
- **Order type / fill model / signal-to-order delay / participation / partial fills / capacity / margin:** **zero occurrences** as modelled terms -> `data gap`, never zero. The article names them only in Limitations/Future work as missing.
- **Two-leg synchronisation:** explicitly absent - "The public trade archive does not provide contemporaneous order-book depth, bid-ask spread, queue position, latency, two-leg fill synchronization, or market impact" (Limitations). A ratio trade requires both legs; the audit's single-bar open-to-close proxy is therefore an **upper bound on executability**, as the source itself frames it.
- **Borrow / shorting:** not stated; the audited signals are long-only, and shorting the ratio is not part of the audited rule -> `data gap`.
- **Sizing / leverage:** unlevered; leverage appears only in the conceptual growth-factor equations, where the source says the manuscript "does not infer deployability from this illustration".
- **Sharpe / drawdown / turnover:** **none reported** - the article reports no Sharpe ratio, no drawdown, no turnover and no capacity number anywhere -> `data gap`.
- **Scout-added assumptions:** **none.** No cost, fill, latency, sizing or liquidity assumption has been introduced by this record; every operational cutoff below the Signal section is `research-defined` only inside the Falsification plan.

## Evidence

### Source-reported

All figures below are third-party, **source-reported**, traced to the pinned article or its six table pages; none has been independently reproduced. All of them concern **crypto perpetual futures**, three newly listed Binance USDS-M contracts, March-May 2025 - they are not equity, futures or other-asset evidence.

**Table 1 - public-trade inventory (table page /tables/1):**

| Contract | Trades | Share | First observation (UTC) | Max gap (s) |
|---|---|---|---|---|
| MLNUSDT | 6,809,556 | 24.2% | 31 Mar 08:45:08 | 209.956 |
| PLUMEUSDT | 6,289,933 | 22.3% | 21 Mar 13:00:25 | 257.298 |
| SIRENUSDT | 15,057,885 | 53.5% | 22 Mar 09:00:13 | 181.275 |
| Total | 28,157,374 | 100.0% | - | - |

Research-computed arithmetic on these inputs: the three contracts sum to **28,157,374** exactly, and the shares recompute to **24.18% / 22.34% / 53.48%**, matching the printed 24.2 / 22.3 / 53.5 after rounding.

**Tables 2-4 - original fixed-split precision record (table pages /tables/2, /tables/3, /tables/4), retained by the source as a descriptive record only.** Columns are validation (`Val.`), test (`Test`) and their printed gap, for the unfiltered model (`U`) and the filtered model (`F`):

| Bar size | Ratio | Val. U | Test U | Gap U | Val. F | Test F | Gap F |
|---|---|---|---|---|---|---|---|
| 1,000 events | MLN/SIREN | .571 | .500 | .071 | .611 | .636 | .025 |
| 1,000 events | MLN/PLUME | .423 | .520 | .097 | .636 | .600 | .036 |
| 1,000 events | SIREN/PLUME | .542 | .509 | .033 | .407 | .379 | .028 |
| 50 events | MLN/PLUME | .4604 | .3869 | .0736 | .4110 | .4074 | .0036 |
| 50 events | MLN/SIREN | .4918 | .4777 | .0141 | .5127 | .5152 | .0025 |
| 50 events | SIREN/PLUME | .5045 | .5094 | .0049 | .5103 | .5086 | .0017 |
| 20 events | MLN/PLUME | .3551 | .3866 | .0315 | .3958 | .3939 | .0019 |
| 20 events | MLN/SIREN | .4894 | .4836 | .0058 | .5125 | .5254 | .0128 |
| 20 events | SIREN/PLUME | .5166 | .5073 | .0093 | .5192 | .5047 | .0145 |

Source statement on these tables (Results, "Original fixed-split record"): "Seven of nine cells have a descriptively smaller filtered gap. Two 20-event cells become worse after filtering, and several test precisions remain close to 0.5. Across the nine cells, the exact sign test gives p = 0.180 and the exact paired Wilcoxon test gives p = 0.074. Accordingly, the 61.5% average gap reduction is not described as statistically significant, general, or economically useful."

Research-computed checks on these printed cells (arithmetic only, not a reproduction): the improvement count is **7 of 9** exactly; the exact two-sided sign test for 7 of 9 is **p = 0.179688**, which rounds to the printed **0.180**; the two worsening cells are **MLN/SIREN at 20 events** (Gap .0058 -> .0128) and **SIREN/PLUME at 20 events** (.0093 -> .0145); recomputing gaps from the printed precisions reproduces every cell except the two 0.0001 disagreements listed in frontmatter contradiction 3; and the printed **61.5%** reduction is **not** reproducible under any of the three natural conventions (62.96% / 33.65% / 68.50%), see contradiction 1.

**Table 5 - independent walk-forward, model-only macro means over the 27 test cells (table page /tables/5):**

| Model | Precision | Recall | F1 | Coverage | Net bps (10) |
|---|---|---|---|---|---|
| Logistic regression | .491 | .164 | .189 | 15.8% | -8.66 |
| Random forest | .513 | .187 | .222 | 18.1% | -8.65 |
| XGBoost | .516 | .199 | .235 | 19.2% | -8.39 |
| LightGBM | .511 | .213 | .251 | 20.8% | -9.03 |

Source statement (Results, "Walk-forward model benchmarks"): "XGBoost has the highest model-only precision (0.516), whereas LightGBM has the highest F1 (0.251). The comparison does not support a uniquely superior LightGBM result across metrics. All mean accepted-signal returns are negative after a 10-basis-point round-trip cost." The 27-cell denominator (9 pair/bar configurations x 3 folds) is research-computed from the caption wording "macro means over nine pair/event-bar configurations and three forward folds".

**Table 6 - LightGBM and rule ablation in the independent walk-forward audit (table page /tables/6):**

| Signal | Prec. | Recall | F1 | Coverage | Gap | Net bps (10) |
|---|---|---|---|---|---|---|
| LightGBM only | .511 | .213 | .251 | 20.8% | .024 | -9.03 |
| + trend | .492 | .060 | .100 | 5.9% | .041 | -11.59 |
| + Hurst | .480 | .040 | .067 | 3.9% | .075 | -9.74 |
| Full AND-gate | .473 | .014 | .026 | 1.34% | .177 | -10.16 |
| Trend only | .462 | .331 | .386 | 34.1% | .019 | -11.77 |
| Trend + Hurst | .450 | .069 | .109 | 6.9% | .056 | -10.62 |

Source statement (Results, "Component ablation, coverage and costs"): "Relative to LightGBM alone, the full gate lowers precision from 0.511 to 0.473, recall from 0.213 to 0.014, F1 from 0.251 to 0.026, and coverage from 20.8% to 1.34%. The model-only mean validation-to-test precision gap is 0.024, compared with 0.177 for the full gate. The full-gate configuration-bootstrap precision interval is [0.400, 0.538]. A small gap therefore cannot compensate for weak discrimination and sparse signals."

**Cost ladder (Results, same subsection):** at **0 bp**, LightGBM-only accepted signals average **+0.97 bp** and the full gate averages **-0.16 bp**; at **10 bp** they are **-9.03 bp** and **-10.16 bp**; at **20 bp** they are **-19.03 bp** and **-20.16 bp**. Research-computed: each net equals the zero-cost value minus the deduction exactly, i.e. the ladder is arithmetic, not re-simulated execution.

**Hurst-threshold sensitivity (Results, "Hurst-threshold sensitivity and seed stability"):** validation selection chose **h = 0.40 in six cases, 0.45 in five, 0.50 in two, 0.55 in five, 0.60 in nine** (research-computed sum = **27**, equal to 9 configurations x 3 folds). Across the complete test grid, **coverage falls from 3.16% at h = 0.40 to 0.22% at h = 0.60**, **recall falls from 0.032 to 0.002**, **mean precision ranges from 0.460 to 0.482**, and **no threshold is positive after a 10 bp cost**. The article presents the full grid rather than "a preferred stable boundary".

**Seed stability (same subsection):** LightGBM model-only mean precision for seeds 11 / 29 / 47 is **0.511 / 0.511 / 0.512**; full-gate precision is **0.473 / 0.482 / 0.493**. Source conclusion: "Seed stability does not rescue the full gate because the recurring result is weak recall, low coverage and negative cost-adjusted return."

**Original fixed-split inference (Results):** exact sign test **p = 0.180**, exact paired Wilcoxon **p = 0.074** - both above 5%, so the source does not claim the gap reduction is significant.

**Abstract-level headline:** "These results do not establish a general or cost-robust trading edge." And the Conclusion: "The main conclusion is therefore methodological... On the present three-asset, three-month sample, the proposed gate is a proof-of-concept that failed its stronger audit, not a general or deployable trading framework."

**Research-computed arithmetic observations (clearly labelled - these are checks of printed values, not reproduction):** harmonic means of the printed mean precision/recall columns are 0.246 (logistic), 0.274 (random forest), 0.287 (XGBoost), 0.301 (LightGBM) against printed F1 of 0.189 / 0.222 / 0.235 / 0.251, and 0.301 (LightGBM-only), 0.107 (+trend), 0.074 (+Hurst), 0.027 (full gate) against printed 0.251 / 0.100 / 0.067 / 0.026 - i.e. the F1 column is not the harmonic mean of the printed columns, consistent with macro-averaging cell-level F1 (frontmatter contradiction 2). Also: full-gate precision **0.473 is below 0.5**, i.e. below the accuracy of a coin flip on balanced labels, while its coverage is 1.34% (about 1 accepted signal in 75).

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Source's own headline:** "These results do not establish a general or cost-robust trading edge" (Abstract) and the gate is "a proof-of-concept that failed its stronger audit" (Conclusion).
2. **The gate destroys the signal it was meant to protect:** relative to LightGBM alone, precision **0.511 -> 0.473**, recall **0.213 -> 0.014**, F1 **0.251 -> 0.026**, coverage **20.8% -> 1.34%** (Table 6).
3. **Full-gate precision is below chance:** **0.473 < 0.500**, with a configuration-bootstrap interval **[0.400, 0.538]** that straddles 0.5 (Table 6, Results).
4. **Every model-only backbone is unprofitable at 10 bp:** net **-8.66 / -8.65 / -8.39 / -9.03 bp** for logistic, random forest, XGBoost and LightGBM (Table 5) - i.e. the failure is not LightGBM-specific.
5. **Even the model-only signal barely clears zero before costs and dies immediately after:** LightGBM-only **+0.97 bp** at 0 bp, **-9.03 bp** at 10 bp, **-19.03 bp** at 20 bp; the full gate is **negative already at zero cost (-0.16 bp)** (Results).
6. **No Hurst threshold works:** across the full h grid, precision stays in **0.460-0.482** and **no threshold is positive after 10 bp** (Results).
7. **Coverage collapses monotonically with the threshold:** **3.16% (h = 0.40) -> 0.22% (h = 0.60)**, recall **0.032 -> 0.002** (Results) - the gate's only consistent effect is to stop trading.
8. **The original improvement claim is statistically insignificant on its own data:** exact sign test **p = 0.180**, exact paired Wilcoxon **p = 0.074**, with **two of nine cells worsening** (Tables 2-4, Results).
9. **The headline 61.5% gap reduction is not reproducible from the printed tables** under three natural conventions (research-computed 62.96% / 33.65% / 68.50%) - frontmatter contradiction 1.
10. **The gap statistic inverts under honest evaluation:** model-only mean validation-to-test gap **0.024** versus full-gate **0.177** (Table 6) - the filtered system is *less* stable forward than the unfiltered one, the opposite of the design intent.
11. **Backbone ranking is metric-dependent:** XGBoost beats LightGBM on precision (.516 vs .511) while losing on F1 (.235 vs .251) (Table 5); the source states there is no uniquely superior model.
12. **Seed stability does not rescue it:** full-gate precision 0.473 / 0.482 / 0.493 across seeds 11 / 29 / 47 with persistently weak recall and coverage (Results).
13. **The sample is three launch-period contracts over roughly one quarter:** "only three newly listed perpetual-futures contracts over March-May 2025", where "launch periods may have unusual volatility, changing liquidity, incentives, and participant composition" (Limitations).
14. **The 27 fold cells and 9 pair/bar configurations are not independent replications** - they share underlying assets and a short shared market regime; the source says configuration-level bootstrap intervals are descriptive for that reason (Methods, Limitations).
15. **Execution is unmodelled:** no order-book depth, spread, queue position, latency, two-leg fill synchronisation or market impact; funding, borrow and margin are absent; the cost analysis is "an unlevered next-bar stress test" that "cannot establish realized profitability" (Limitations).
16. **The submitted tables cannot be verified:** original source code, fitted models and prediction vectors were unavailable, so Tables 2-4 rest on an unverifiable pipeline and the reconstruction is explicitly "not a bit-for-bit replication" (Limitations) - frontmatter contradiction 4.
17. **Price-only features omit the very variables that drive perp returns:** funding, open interest, liquidations, order-flow imbalance and network information (Limitations).
18. **The Hurst estimator itself is fragile:** "sensitive to window length, lag range, and finite-sample bias"; the 0.40 boundary is a prespecified candidate and the source states the data "do not justify a universal 0.40 boundary" (Related work, Discussion, Limitations).
19. **Adjacent contrary evidence already in this repository (different source identities; context, not tests of this source):** `crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12.md` (Hurst used as an anti-persistence filter in cointegration-based perp pairs), `crypto-fer-hurst-adx-regime-gated-amo-kama-momentum-source-code-audit-2026-09-14.md` and `crypto-hurst-fld-cycle-state-source-code-audit-2026-09-14.md` (Hurst/Fld regime gates audited against source code), `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12.md` (a stationarity gate that suppresses ETF-pair signals in walk-forward tests), `btc-perpetual-information-bars-tick-minute-directional-failure-2026-09-02.md` (event/tick-versus-clock bar construction failing a directional test), `factorvae-crypto-cross-sectional-latent-ranking-momentum-filter-2026-09-23.md` (deep generative cross-sectional crypto ranking), `bitget-perpetual-shuffled-null-falsification-cross-sectional-momentum-2026-09-13.md` and `crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12.md` (cost-gated crypto signal falsifications). Source identity and mechanism differ in every pair.
20. **Absence caveat:** none identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

All thresholds, windows and decision rules in this section are **`research-defined falsification thresholds`** set by this Scout; none are source-reported. `research-proposed` adaptations are marked inline. The object of every test is the source's central claim: *the trend AND Hurst gate does not deliver a cost-robust edge, and a small generalization gap is not evidence of robustness.*

- **F1 - Printed-value reproduction gate (primary).** `research-defined`: rebuild Tables 5 and 6 from the public Binance Data Vision archive with an independent implementation (same ratios, event bars, folds and thresholds); **fail** if any macro metric differs from the printed value by more than **0.02 precision**, **0.02 F1**, **2 percentage points of coverage** or **1 bp** on the 10 bp net. Action on failure: mark every affected number `data gap` and set `contested: true` with a reproduction note; the negative verdict is then source-claim only.
- **F2 - Frozen forward replication.** `research-defined`: freeze the normalized Signal section exactly as written and run it from **2026-10-01** for **12 months** on the same three ratios (and on whatever successor contracts the same listing cohort produces); **fail the record's negative verdict** (i.e. the gate survives) if the full AND-gate attains precision **>= 0.53** with coverage **>= 5%** *and* net accepted-signal return **> 0 bp at 10 bp**. Action: promote only the surviving gate to a separate candidate record; otherwise retain as negative evidence.
- **F3 - Launch-period ablation (universe extension).** `research-proposed`: repeat the audit on **>= 20 perpetual contracts** spanning mature majors, mid-caps and newer listings over **>= 24 months** of data; **fail** the "launch-period artefact" reading of the negative result if the full gate beats model-only on precision *and* posts **> 0 bp at 10 bp** in the mature-contract subsample.
- **F4 - Cost ladder with a real fee schedule.** `research-defined`: charge **0 / 2 / 5 / 10 / 20 / 30 bp** round trip, then replace the flat deduction with Binance's published taker schedule plus a spread proxy; **fail** any tradeable reading of any cell whose net is **<= 0 at 5 bp** (currently every cell fails at 10 bp).
- **F5 - Two-leg executability test.** `research-proposed`: reconstruct the ratio as a **simultaneous two-leg order** using book snapshots, and compare against the paper's single-bar open-to-close proxy; **fail** the proxy if the sign of the mean accepted-signal return flips, or if the proxy overstates the mean by **> 2 bp**.
- **F6 - Funding-inclusive test.** `research-proposed`: charge realised funding on both legs at each 8-hour interval inside the held bar; **fail** the proxy if funding moves the mean accepted-signal return by **> 2 bp** or flips its sign.
- **F7 - Nested threshold selection.** `research-defined` (the source's own stated future work): re-estimate `h` **inside each training window** rather than on the fold's validation segment, with the same grid; **fail** the source's "gates suppress predictions" interpretation if nested selection raises full-gate precision above model-only precision **and** keeps coverage **>= 5%**.
- **F8 - Gate-removal ablation ladder.** `research-defined`: run the four ablations already defined by the source (model-only, +trend, +Hurst, full gate) plus **Hurst-only-as-direction** (which the source refuses to call directional) and a **no-gate + threshold-on-confidence** variant; **fail** the "regime gating" mechanism claim if no gating variant raises precision above model-only while keeping coverage **>= 5%**.
- **F9 - Bar-construction robustness.** `research-defined`: re-run with **clock-time bars (1 s, 1 min, 5 min)** and with **trade-count bars of 100 and 500**, holding everything else fixed; **fail** if the sign of the model-only 10 bp net flips between bar families, which would mean the negative result is a bar artefact rather than a statement about the signal.
- **F10 - Stale-leg sensitivity.** `research-defined`: drop every ratio update whose older leg is older than **1 s** and then **5 s** at emission; **fail** if any headline macro precision moves by **> 0.02**, which would show the result is driven by the as-of carry-forward rather than by the signal.
- **F11 - Placebo / permutation control.** `research-defined`: within each test fold, evaluate the same pipeline on **1,000 label permutations** and on **1,000 circular shifts** of the target series; **fail** the "chance-level discrimination" reading if the observed model-only precision does not exceed the **95th percentile** of both null distributions.
- **F12 - Multiplicity audit.** `research-defined`: the audited search space is 9 configurations x 3 folds x 5 thresholds x 4 models plus 6 ablation rows = well over **500 evaluated cells**; apply **Benjamini-Hochberg at q < 0.10** over the full family; **fail** if no cell survives, in which case every precision figure stays descriptive (this is the expected outcome and would confirm the source's own framing).
- **F13 - Independent-engine and seed-breadth audit.** `research-defined`: re-run on a second engine with **10 seeds** instead of 3; **fail** if model-only precision moves by **> 0.02** or its 10 bp net by **> 1 bp**, which would make the whole comparison engine- or seed-dependent.
- **F14 - Action on failure.** `research-defined`: F1 failure => quarantine the printed tables and keep the record as `research-only` with numbers marked `data gap`; F2 survival => open a new candidate record for the surviving gate and keep this record as historical negative evidence; F3, F5 or F6 survival => revise the "no cost-robust edge" boundary but keep status `research-only`; all other failures => retain the negative verdict and the methodological claim that gap, discrimination, coverage and net value must be reported separately. No outcome of this plan promotes the record beyond `research-only`.

## Crypto portability

**Verdict: `direct`.**

- The source **is crypto research**: three Binance USDT-margined perpetual futures, tick-level public trades, event-time bars over a 24/7 market. No porting of venue, instrument or session structure is required to re-run the audited object on crypto.
- **Crypto-specific risks that remain even at `direct`:**
  - **Listing / survivorship:** all three contracts are launch-period instruments; a crypto universe screen would need explicit listing-age, liquidity and delisting rules (research-proposed), because delisting and incentive-driven launches dominate such short samples.
  - **Spot vs perpetual / funding:** the ratios are perp-to-perp on the same venue, so there is no spot-perp basis leg, but **funding is unmodelled** and perp funding is charged every 8 hours on both legs - the single largest missing cost term for a held position.
  - **Two-leg synchronisation and venue fragmentation:** the audit is single-venue (Binance) and uses a carried-forward as-of join; a real ratio book needs both legs filled together, and cross-venue or CEX-DEX versions would add a different basis and a different failure mode.
  - **24/7 sessions and timestamp boundaries:** event bars have no wall-clock meaning; funding intervals, UTC day boundaries and candle resets are absent from the audited rule and must be added explicitly by any implementer (`research-proposed`).
  - **Mark / index price, liquidation, leverage:** none of mark price, liquidation price, margin state or leverage enters the signal or the cost model, although the conceptual equations 1-3 discuss leverage.
  - **Liquidity and depth:** three small-cap perps in their first weeks; depth, spread and queue position are not in the source's data at all.
- **Conclusion:** portability of the *object* is `direct`; portability of a *profitable* variant is **not implied** - the source's own result on crypto data is negative, and no crypto-specific claim of edge is made anywhere in the article. Crypto portability is not authorization to trade.

## Limitations

- **`not independently reproduced`:** no reproduction by this Scout or by any record in this repository; no code, notebook, environment file or fitted-model artifact is linked from the article, and there is no code availability statement.
- **`data gap` - execution economics:** order type, fill model, signal-to-order delay, latency, participation, market impact, slippage, partial fills, capacity, margin and borrow are not modelled (term scan of the pinned text); they must never be read as "zero".
- **`data gap` - missing strategy parameters:** the LightGBM hyperparameter grid/budget and fitted values; the passive price-ratio reference values (figure-level); Wilson interval numerics (figure-level); the per-cell fold metrics behind the macro means; whether F1 columns are means of cell-level F1 or pooled-count F1.
- **`data gap` - feed identity:** the Binance Data Vision archive is named but no snapshot date, file manifest or hash is printed, so the exact 28,157,374-trade input set cannot be pinned beyond the stated month range.
- **`underspecified` - portfolio construction:** the audit reports per-accepted-signal averages with no capital allocation, weighting across the nine configurations, turnover, holding overlap or capacity; a portfolio reading of these numbers is not supported by the source.
- **`underspecified` - short side:** the gate is long-only by construction; whether a symmetric short gate was tested is never stated.
- **`underspecified` - tradability of event time:** signals fire at event-bar boundaries whose wall-clock position varies with activity; no order timing relative to that boundary is specified.
- **Sample and regime limits:** three contracts, roughly one calendar quarter, launch-period dynamics, shared regime across folds, and ratios that share underlying assets - the source states the 27 cells are not independent replications.
- **Statistical limits:** the only inferential tests in the article are on the nine original fixed-split gaps (p = 0.180 and p = 0.074); the walk-forward audit reports descriptive macro means and one configuration-bootstrap interval, with **no significance test on the walk-forward comparisons and no multiplicity correction over the >500-cell search space**.
- **Cost-model limits:** a flat 0/10/20 bp round-trip deduction applied to a single-bar open-to-close return; no spread, no funding, no two-leg impact, no latency. The source explicitly says this "cannot establish realized profitability".
- **Reproducibility limits:** submitted tables rest on unavailable code and models; the auditable tables are an independent reconstruction; data availability is by request even though the raw feed is public - see frontmatter contradiction 4.
- **Source-quality context:** peer-reviewed open-access journal article (Received 07 June 2026, Accepted 02 September 2026), six authors all in a business-school department, no competing interests declared, no funding statement printed, no preprint stage, and an article whose title ("Improving the robustness...") predates its own negative result - the source states it retained the original title deliberately.
- **Unreconciled contradictions:** see the four items in the frontmatter `contradictions` block.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No ratio panel has been assembled, no LightGBM model has been fitted, no Hurst gate has been coded, no walk-forward has been re-run and no Qlib, Paper, Testnet or Live stage has been touched. This record is a normalised, source-traceable capture of a peer-reviewed negative audit plus a Scout-authored falsification plan.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. The record's `confidence: high` refers only to the fidelity of this **research interpretation** to the pinned publisher pages - it is not confidence that the audited gate (or any variant of it) makes money, and it is not authorisation to trade. The source's own result is negative; capturing it does not invert it.

## Related Wiki records

Read-only `kb_search` on the Wiki Brain vault (2026-09-28). The query `Hurst exponent regime gate cryptocurrency trading classifier` returned **0 pages**; the query `relative value price ratio pairs trading walk-forward robustness audit` returned **7 pages**, of which the following verified paths are materially related:

- [[quant/crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12]] - Hurst used as an anti-persistence filter inside cointegration-based crypto-perp pairs trading; shares the Hurst-regime ingredient but the mechanism (cointegration half-life ranking) and the signal construction differ, and that record's evidence is its own source's.
- [[quant/pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12]] - an ADF stationarity gate falsified in walk-forward ETF pairs trading; same "gate that suppresses signals" posture, different market (ETF pairs), different filter statistic, different source.
- [[quant/crypto-rl-pair-trading-dynamic-scaling-a2c-2026-09-12]] - reinforcement-learning pair trading with dynamic scaling on high-frequency crypto pairs; different mechanism (RL sizing) and different source.
- [[quant/causal-knn-predictive-flow-leakage-falsification-2026-09-13]] - causal kNN feature matching with IC falsification; different mechanism (leakage control) and different source.
- [[quant/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05]] - ensemble signal-quality filtering in US equities; shares the "quality gate on a classifier score" idea, different universe, different mechanism, different source.
- [[quant/forex-retail-execution-friction-wide-stop-ratchet-falsification-2026-09-13]] - pre-registered walk-forward falsification of retail FX rules; shares the falsification posture, different market and mechanism.
- [[quant/futures-quad-trend-carry-skew-vov-composite-2026-09-11]] - multi-alpha futures composite; different mechanism, different universe, different source.

No Wiki link was fabricated for the query that returned 0 pages.

Adjacent records in **this repository** (source identity differs in every pair; four-axis distinction stated):

- `crypto-fer-hurst-adx-regime-gated-amo-kama-momentum-source-code-audit-2026-09-14.md` - **different source**; **mechanism differs** (Hurst/ADX gating a KAMA momentum rule on price series rather than gating a ratio classifier); **signal construction differs** (rule-based trend following vs supervised classification); **horizon differs** (clock-time bars vs event-time bars).
- `crypto-hurst-fld-cycle-state-source-code-audit-2026-09-14.md` - **different source**; uses Hurst and the FLD as **cycle-state diagnostics for timing** rather than as a precision gate on a classifier; different data dependency (price-cycle geometry).
- `btc-perpetual-information-bars-tick-minute-directional-failure-2026-09-02.md` - **different source**; shares the bar-construction question but compares **tick versus minute information bars for direction forecasting** on BTC, with no regime gate and a different universe (single major vs three small-cap alts).
- `factorvae-crypto-cross-sectional-latent-ranking-momentum-filter-2026-09-23.md` - **different source**; **mechanism differs** (deep generative latent-factor cross-sectional ranking over 50 cryptocurrencies vs pairwise ratio classification); **universe differs** (50-coin cross-section vs 3 contracts); **horizon differs** (daily strategy variants vs one event bar).
- `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12.md` - **different source**; **market type differs** (US ETF pairs, cash equity) and the gate statistic is stationarity rather than Hurst persistence; shares only the "filter that thins the signal" failure mode.
- `bitget-perpetual-shuffled-null-falsification-cross-sectional-momentum-2026-09-13.md` and `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13.md` - **different sources**; **mechanism differs** (cross-sectional momentum with shuffled-label nulls and taker-fee walls vs a time-series ratio classifier with a regime gate); **signal construction differs** (cross-sectional rank vs within-pair ratio prediction).

## Sources

1. Hassanie, S., Atalay, C., Khan, T.A., Ali, R.H., Mateus, C.D.C. & Ahmed, I. "Improving the robustness of binary classifiers in cryptocurrency exchange rate forecasts." *Scientific Reports* **16**, 29336 (2026). DOI `10.1038/s41598-026-70423-7`; article page `https://www.nature.com/articles/s41598-026-70423-7` (Received 07 June 2026, Accepted 02 September 2026, Published 21 September 2026, CC BY 4.0). **Primary source; author list, dates, sample, universe, methods, cost treatment and every number in this record were verified on this page and on its table pages.**
2. Table pages of the same article, read 2026-09-28: `https://www.nature.com/articles/s41598-026-70423-7/tables/1` (trade inventory), `/tables/2` (1,000-event fixed-split precision), `/tables/3` (50-event), `/tables/4` (20-event), `/tables/5` (walk-forward model benchmarks), `/tables/6` (LightGBM and rule ablation). All Table 1-6 values in this record were transcribed from these pages.
3. Data source **as named by the article's Methods** (not independently snapshotted for this record): Binance Data Vision archive of USDS-M perpetual-futures trades, March-May 2025 files, 28,157,374 trades across MLNUSDT, PLUMEUSDT and SIRENUSDT. The article prints no URL or version hash for the archive -> identity `data gap`.
4. References **cited by the source and not independently read for claims in this record**: Gatev, Goetzmann & Rouwenhorst, "Pairs trading: Performance of a relative-value arbitrage rule", Review of Financial Studies 19, 797-827 (2006); Ke et al., "LightGBM", NeurIPS 30 (2017); Breiman, Machine Learning 45 (2001); Chen & Guestrin, KDD (2016); Sidhu et al., SSRN 3824032 (2021); Bui & Ślepaczuk, Physica A 592, 126784 (2022); Saito & Rehmsmeier, PLOS ONE 10, e0118432 (2015); White, Econometrica 68 (2000); Bailey, Borwein, Lopez de Prado & Zhu, SSRN 2326253 (2013); de Prado, *Advances in Financial Machine Learning* (2018); Zenkova & Ślepaczuk, Central European Economic Journal 5, 186-205 (2019); Bysik & Ślepaczuk, arXiv:2606.00060 (2026); Płachta & Ślepaczuk, SSRN 5272156 (2025); Bieganowski & Ślepaczuk, arXiv:2602.00776 (2026); Choi, Research in International Business and Finance 90, 103494 (2026) and Physica A 697, 131735 (2026); Urquhart, Economics Letters 148, 80-82 (2016); Kroha & Škoula, ICEIS (2019); Rostamian & O'Hara, Neural Computing and Applications 34, 17193-17206 (2022); Atwa, Sedky & Kholief, International Journal of Data Science and Analytics (2025); ur Rehman Ghaffar et al., Financial Innovation 8 (2022).

**Status literals:** `research-only` | `not-implemented` | `not-approved` | `approval_scope: research-only` | `not independently reproduced`.
