---
schema: strategy-research-record-v1
title: "State-Dependent Market (In)Efficiency in Cryptocurrency Markets: meta-learning selection of a Directional-Change threshold from on-chain and trend features (SSRN 5525163)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - ethereum
  - binance-futures
  - meta-learning
  - regime-switching
  - directional-change
  - on-chain
  - adaptive-market-hypothesis
status: research-only
confidence: medium
source_as_of: 2025-09-24
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5525163 (SSRN landing, fetched 2026-09-26: '42 Pages', 'Posted: 25 Sep 2025', 'Date Written: September 18, 2025', 0 References, 0 Citations, copyright notice 'The copyright holder has granted SSRN a license ... All rights reserved. No reuse allowed without permission.')"
  - "https://doi.org/10.2139/ssrn.5525163 (DOI; dx.doi.org resolves to https://www.ssrn.com/abstract=5525163 — the bare host is Cloudflare-blocked to non-browser clients, HTTP 403, checked 2026-09-26)"
  - "https://papers.ssrn.com/sol3/Delivery.cfm/5525163.pdf?abstractid=5525163&mirid=1 (pinned PDF retrieved inside an authenticated browser session on 2026-09-26 after curl and scrapling both returned Cloudflare 403: 1,698,816 bytes, 42 pages, SHA-256 1a23ff6ba301d1b53aa6c8ca9a58f2d57e21190aa0ee77ed86deae066eeb8acc; text extracted with pdf.js to 102,814 characters and read end to end — title page, Sections 1-6, Tables 1-4, Figures 1-9, References, Appendices A-J including Algorithm 2 and Tables G.1, H.1, I.1)"
  - "https://api.openalex.org/works/doi:10.2139/ssrn.5525163 (OpenAlex W7083296082, retrieved 2026-09-26: type 'preprint', indexed_in crossref, single location = the DOI landing page, no alternate full-text PDF; Semantic Scholar DOI lookup returned HTTP 404)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal numeric contradiction, our count on the pinned PDF read 2026-09-26: Section 4.4 claims the return-weighted loss 'improved the total rate of return in four of the five model specifications', but Table H.1 shows only three of five improving (Strategy Meta-Info 296.85 -> 323.77, On-Chain 137.06 -> 199.04, Market Regime 250.38 -> 372.15 improve; DC Indicators 309.02 -> 194.30 and Combined 496.57 -> 445.98 both get worse). The paper's flagship Combined model is therefore better WITHOUT the paper's own novel weighted loss (Sharpe 1.37 unweighted vs 1.34 weighted). Both readings are printed as-is; we do not resolve which is intended."
  - "Source-internal label-timing inconsistency: Section 3.4.1 prose says the meta-model predicts, 'at the end of each day d, which of the base strategies will yield the highest return on the subsequent day, d+1', while Eq. 11 defines the ground-truth label as theta* = argmax over theta_i of Return(theta_i, d) — the same day d. Whether the label is day d or day d+1 determines whether the meta-label is contemporaneous with the feature vector m_d or shifted one day forward. Not resolved anywhere in the source (`underspecified`)."
  - "Source-internal cross-reference mismatch: Section 3.4 states that 'the specific features and trading logic used in these base models are formally defined in Appendix C', but Appendix C contains only the four DC prediction features; the trading logic (Algorithm 2) is filed under Appendix D.1."
  - "Source-internal editorial defects in the pinned PDF: the paragraph block beginning 'While MFDFA is excellent for describing the statistical footprint of inefficiency...' is duplicated verbatim across Section 2.2 and Section 2.3 (pages 4-5); Section 3 contains two different subsections both numbered 3.1 and seven consecutive subsections all numbered 3.4 (plus three numbered 3.5); the PDF cover is dated September 24, 2025 while the SSRN landing states Date Written September 18, 2025 and Posted 25 Sep 2025, with no revision history listed."
---

# State-Dependent Market (In)Efficiency in Cryptocurrency Markets: meta-learning selection of a Directional-Change threshold from on-chain and trend features (SSRN 5525163)

## Provenance

- **Paper**: Sasan Barak, Siavash Razmi, Alireza Mousavi, *State-Dependent Market (In)Efficiency in Cryptocurrency Markets*, SSRN Working Paper, abstract id `5525163`, DOI `10.2139/ssrn.5525163`.
- **Author list and affiliations (verbatim from the PDF title page)**: Sasan Barak (1), Siavash Razmi (2), Alireza Mousavi (1); `1 = Department of Decision Analytics and Risk, Southampton Business School, University of Southampton, Southampton, UK`; `2 = Department of Computer Science, University of Innsbruck, Innsbruck, Austria`. Footnote: `* Corresponding Author: s.barak@soton.ac.uk`. JEL classification printed on page 1: `G11, G12, G14, C58`.
- **Version / date**: PDF cover **September 24, 2025**; SSRN landing **Date Written: September 18, 2025**, **Posted: 25 Sep 2025**, **42 Pages**, **0 References / 0 Citations** shown, no revision or "earlier version" entry → single posted version as captured **2026-09-26**. The two manuscript dates are inconsistent; both are recorded rather than reconciled.
- **Publication status**: **preprint / working paper only**. No journal, no venue, no peer-review statement, no "under review" line, no acknowledgement, no funding statement, no conflict-of-interest or ethics statement anywhere in the pinned 42 pages (word scan: `peer`, `under review`, `Acknowledg`, `Conflict of interest`, `Ethic`, `Funding` → 0 relevant hits). Not independently peer reviewed.
- **Pinned primary source**: PDF `1,698,816 bytes`, `42 pages`, **SHA-256 `1a23ff6ba301d1b53aa6c8ca9a58f2d57e21190aa0ee77ed86deae066eeb8acc`**, retrieved **2026-09-26** inside an authenticated browser session — plain `curl`, `dx.doi.org` and `scrapling` 0.4.9 all receive a Cloudflare "Just a moment..." **HTTP 403** from this host, so the bytes were fetched through the page's own session, hashed in-page with `crypto.subtle`, and converted with pdf.js to **102,814 characters** which were read end to end.
- **Licence**: the SSRN landing states *"The copyright holder has granted SSRN a license ... All rights reserved. No reuse allowed without permission."* → this record cites and normalises claims and printed figures only; no source text is reproduced.
- **Code / data / AI-use**: word scan of the pinned PDF for `github`, `code`, `data availability`, `upon request`, `supplementary` → **0 hits**. **No code repository, no dataset link, no data-availability statement** → every availability field is `not stated in source`. OpenAlex lists only the DOI location (no repository full text) and Semantic Scholar has no record, so no alternative open copy exists to cross-check.
- **Source / data as-of**: full sample **January 2021 – January 2024**; in-sample static-theta optimisation **January 2021 – January 2022**; out-of-sample evaluation **January 2022 – January 2024** (Tables 2, 3, 4, I.1 captions). Universe source: CoinMarketCap, cited with `Accessed: 2024-09-29` in the References. Manuscript as-of 2025-09-24; captured 2026-09-26.
- **Pre-write source-identity dedup (whole repository, hidden trees and manifest included)**: `5525163`, `State-Dependent Market (In)Efficiency`, `10.2139/ssrn.5525163`, `Razmi`, `Mousavi`, `symmetric uncertainty` → **0 hits** across all `*.md`, `*.csv`, `*.json`, `*.txt` including `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` (5,808 lines) before the write. `Barak` → 1 file (`decision-focused-learning-kkt-mvo-etf-allocation-2026-09-25.md`), cleared as the substring in "Ibaraki" (University of Tsukuba address). `state-dependent market` → 1 hidden-tree hit (`multi-level-market-making-logistic-normal-deep-sets-2026-09-02.md`), cleared as unrelated inventory-penalty prose. `Directional Change` / `directional change` → 4 files, cleared: in `cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03.md` it is the name of Alpha191 formula *Alpha 086 (10-Day Price Acceleration vs. Directional Change)*, and in `disclosed-human-capital-disruption-firm-specific-risk-2026-09-25.md` it is the sentence "do not detect a common directional change" — neither uses event-based DC sampling. `dual-threshold` → 13 files, all hysteresis/volatility/dual-threshold *indicator* usages, none DC event time. `theta_s` → 1 file (optimal-execution notation), unrelated.
- **Four-axis material-distinction statement vs the nearest existing repository records**: (1) `bitcoin-regime-aware-meta-learning-selective-directional-trading-2026-09-13.md` — same broad "crypto + meta-learning + regime" neighbourhood, but a different source (IEEE ICIPTM 2026 paper + `manavmax/Bitcoin-Alpha-System` commit `4bf76065…`), single-asset BTC daily bars, and a *selective-classification abstention gate* (trade / NO_TRADE on a confidence threshold) rather than *daily selection of a DC event threshold*; (2) `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` and the wider `bitcoin-onchain-*` family — single-indicator static cycle timing versus a 43-metric Glassnode feature block feeding a regime-conditional parameter selector; (3) `market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12.md` — equity timing on GitHub `davidxu277/alpha-timing`, regime-routed specialist regressors with dual-threshold hysteresis, no event-based sampling and no on-chain data; (4) `path-signature-regime-detection-crypto-leverage-cycle-2026-09-13.md` — rough-path regime *classification* as the signal itself, different source and mechanism; (5) `crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04.md` — walk-forward momentum with cost attrition, different source, different signal. Source identity differs in every pair, and mechanism differs in every pair: DC event-time counter-trend trading with meta-selected theta versus abstention gating / single-indicator cycle timing / equity regime routing / rough-path classification / walk-forward momentum.

## Economic mechanism

### Source-reported

The paper's stated question is whether crypto-market inefficiency is constant or state-dependent. It sides with the Adaptive Market Hypothesis (Lo 2004): abnormal-return opportunities are temporary, appearing and dissipating with regimes, so predictability should be evaluated per state rather than pooled.

Three stated channels carry the argument:

1. **Event-based time.** Fixed calendar sampling is said to be systematically violated in high-frequency crypto; the Directional Change (DC) method (Tsang 2017; Aloud 2012) therefore only registers an event when price moves by a threshold `theta` from its last extreme, making the sampling frequency endogenous to volatility. Dual thresholds `theta_s < theta_b` turn the descriptive DC summary into a binary *trend-persistence* task (Eq. 3): label 1 if a `theta_s` extreme point is also a `theta_b` extreme point — read by the source as momentum, 0 as impending reversal.
2. **Two novel information sets.** (a) ~300 Glassnode on-chain metrics for BTC and ETH, reduced to the **43** most informative inside the walk-forward loop, in seven categories (Supply, Exchange, Transactions, Mining, Valuation, Spent Outputs & Activity, Price Indicators) — intended as a transparent, near-real-time read on network fundamentals and holder/sentiment behaviour; (b) DC-derived trend-asymmetry indicators, justified by the documented asymmetric multifractality of crypto returns and by prospect-theory loss aversion.
3. **A meta-learning layer.** Base strategies each run the *same* counter-trend trading logic at a *fixed* `theta_s`; each day the meta-model predicts which base strategy will earn the most on the next day, using four feature families (strategy meta-information, on-chain, DC indicators, market-regime statistics). The stated hypothesis pair: `H0` — the adaptive strategy's Sharpe is not distinguishable from the best static-theta strategy; `H1` — it is statistically and economically greater.

A supporting methodological claim: portfolio formation uses symmetric uncertainty (SU) hierarchical clustering instead of Pearson correlation, so the DC engine can be run on one aggregated portfolio price series while still representing the market rather than one asset.

### Research interpretation

Stated as a falsifiable hypothesis rather than a finding: **the economically tradable residue is a regime-conditional parameter-selection effect on top of a two-sided counter-trend event strategy** — if state information (on-chain + trend asymmetry + market statistics) has real predictive content about which DC aggressiveness will pay next, then an adaptive choice of `theta` should beat the best fixed `theta` out of sample after costs, and the gain should survive ablation of the on-chain and DC feature blocks. Component roles: *regime* = the meta-model's daily `theta` choice plus monthly SU re-clustering; *primary signal* = the DC event stream on the aggregated portfolio price, gated by a binary trend-persistence classifier and then by the selected `theta`; *confirmation* = the `DC_b`-event branch of Algorithm 2 (enter counter-trend only when the previous small-theta prediction was 1); *risk / exit* = **absent from the source** — no stop, no sizing rule, no leverage cap and no liquidation logic is printed. We do not assume any component contributes alpha; F4, F5 and F6 below are the ablations that decide it.

## Signal

**Source-reported construction (all from the pinned 42-page PDF):**

- **Data & universe**: minute-level **Binance futures** bars; universe = **top 50 cryptocurrencies by market capitalisation "representative of the sample period (January 2021 to January 2024), as reported by CoinMarketCap 2024"**. The source explicitly prefers futures as "a centralized and highly liquid venue" that avoids spot fragmentation. **Timezone, session and candle-boundary conventions are never printed** (`underspecified`); contract type (perpetual vs dated), tick size, and whether minute bars are mark- or last-price are `not stated in source`.
- **Portfolio layer (Section 3.3)**: re-executed **monthly**; a pairwise **symmetric-uncertainty** matrix on the preceding month's daily returns for all 50 assets feeds hierarchical clustering; the number of clusters is chosen by the **silhouette** method; the single most central asset per cluster is selected; capital is **1/N equal-weighted**. Each constituent price is unitised at the analysis start and the series are **summed** into one aggregate portfolio price `P_T(t)` (Eqs. 9-10); DC is then applied to that aggregate series.
- **DC definitions**: a new trend is confirmed when `P_c >= P_low x (1 + theta)` in a downtrend (Eq. 1) or `P_c <= P_high x (1 - theta)` in an uptrend (Eq. 2); extreme points are assigned retrospectively (Algorithm 1, Appendix B). Dual summarisation uses `theta_s` and `theta_b` with **`theta_b > theta_s`; the numeric value of `theta_b` is never printed** (`data gap`).
- **Base DC prediction model**: binary target Eq. 3 over features `TMV`, `T`, `OSV`, `COP` (Eqs. C.1-C.4). **The algorithm behind this first-level classifier is never stated** (`data gap`) — only the meta-model's LightGBM/XGBoost identity is disclosed.
- **Theta set**: `Theta = {0.01, 0.02, 0.04}` (Table 3 Panel A and Figure 6, three classes). The static benchmark uses `theta_s = 0.026`, selected by Sharpe maximisation over the in-sample window **January 2021 – January 2022** (Figure 5).
- **Meta-model**: LightGBM classifier (XGBoost replication in Appendix I), trained **at the end of day d** on feature vector `m_d` to output `theta_hat(d+1)`; label per Eq. 11. Four feature families with windows `h_strategy`, `h_dc`, `h_regime`, `h_onchain` (defaults in Table G.1: 1, 30, 10, 1) and weighted-loss scale `alpha = 5`. Weight `w_d = exp(alpha x (r_max,d - r_min,d))` with daily returns clipped at 3 standard deviations (Eqs. 13-14). Full feature list in Appendix J (J.1 strategy meta-information incl. number of orders, average position length, long ratio, win rate, average return, DC-type ratio, model accuracy, average confidence; J.2 DC indicators incl. coastline, trend duration, overshoot duration/magnitude, uptrend-downtrend asymmetry of time, return and volume, COP; J.3 market regime incl. RSI(14), MACD signal, price stdev/skew/kurtosis, Z-score).
- **Validation protocol (Section 3.5)**: k-fold explicitly rejected as look-ahead-prone; **rolling-origin walk-forward with a fixed-length window for the base DC models**, **expanding-window walk-forward (called "fixed-origin" in the source) for the meta-model**; feature selection for the 43 on-chain metrics is performed *inside* the loop using training data only. The naming of the two schemes is internally inconsistent (`underspecified`), so the exact meta-model refit schedule must be re-derived by a reproducer.
- **Trading logic (Algorithm 2, Appendix D.1 — two-sided counter-trend)**: *no open position* → on a `DC_s` event run `f([TMV, OSV, T, COP])`; if `y_hat = 0` **open a counter-trend position**, if `y_hat = 1` wait; alternatively, if a `DC_b` event occurs **and** the previous `y_hat` was 1, open a counter-trend position. *Position open* → close all when an opposing `DC_s` event occurs.
- **Metrics (Appendix E)**: Rate of Return `RR = (V_T - V_0)/V_0`, Profit Factor, MDD, Longest Drawdown Duration, Sharpe (SRPR), Sortino (SORR).
- **What is not reconstructible from the source (`data gap`, never invented)**: position **sizing**; leverage and margin (Section 5.2 states the returns "reflect the strategy's high-frequency nature within a **leveraged futures market**" but never quantifies leverage); stop / take-profit / liquidation handling; order type and execution price; whether positions are netted across constituents; turnover; the numeric `theta_b`; the first-level classifier; and the meta-label timing ambiguity above.
- **Scout-labelled operationalisation (`research-proposed`, not from the source)**: size each counter-trend position at a fixed fraction of equity with an explicit leverage cap, enter at the next minute bar's mid, close at the DC confirmation bar, re-form the SU portfolio monthly and re-select `theta` daily after the UTC close. Any threshold or failure rule in the Falsification plan is `research-defined`.

## Required data

- **Instrument / universe**: top-50 crypto by market cap with **point-in-time** membership preferred; the source's own construction is whole-sample ("representative of the sample period"), so a reproducer must rebuild membership month by month to avoid survivorship.
- **Venue / market type**: Binance **futures**, minute bars, single venue; long and short both used (Algorithm 2 is two-sided, and Appendix J.1 defines a Long Ratio feature).
- **Timeframe / fields**: minute OHLCV on the 50 contracts; daily closes for SU clustering and for the aggregate portfolio series.
- **On-chain**: Glassnode (~300 metrics for BTC and ETH, reduced to 43) — a **paid, licensed** feed; categories Supply / Exchange / Transactions / Mining / Valuation / Spent Outputs & Activity / Price Indicators (full list in Appendix A).
- **Reference data**: CoinMarketCap top-50 market-cap ranking (cited as accessed 2024-09-29) for universe construction.
- **Point-in-time**: on-chain feature selection must stay inside the walk-forward loop (the source does this); universe membership, exchange netflow publication lag and Glassnode revision policy are `not stated in source`.
- **Timestamp / timezone**: `data gap` — no timezone, no candle-boundary or funding-settlement convention is printed.
- **Cost inputs**: none are requested by the source — no fee schedule, funding series, spread, borrow or impact model appears anywhere (`data gap`).
- **Missing data**: delistings, halted contracts and incomplete minute series are not discussed (`underspecified`).

## Execution assumptions

**Cost determination from a Methods-level read** of Sections 3 (3.1 data, 3.2 DC, 3.3 portfolio, 3.4 meta-learning, 3.5 empirical design), 4 (4.1-4.5 results and robustness), 5 (discussion), 6 (conclusion), and Appendices A-J including Algorithm 1, Algorithm 2, Tables G.1/H.1/I.1, plus a word scan of the pinned 42-page text for `fee, commission, spread, bid-ask, slippage, funding, turnover, leverage, liquidat, borrow, latency, fill, capacity, impact, gross, net of`:

- The **only** cost statement in the entire paper is in Section 6, verbatim in substance: *"our analysis is presented **gross of transaction costs** to isolate the strategy's raw predictive power. Incorporating a realistic model of trading frictions — such as exchange fees, funding rates, and price slippage — is a complex undertaking ... a comprehensive study of the strategy's performance on a **net** return basis is left for future work."*
- Consequently `fees`, `spread`, `slippage`, `impact`, `participation`, `ADV`, `capacity`, `borrow`, `financing`, `leverage`, `margin`, `latency`, `fill / partial fill / failure handling`, `funding`, and `turnover` are all **`data gap`, never zero**; the words `turnover`, `commission`, `bid-ask`, `liquidat`, `borrow`, `latency`, `fill` and `capacity` appear **0 times** in the pinned text.
- Two look-alikes that are **not** cost models: the `fee` hits are Glassnode's on-chain `Miner Revenue (Fees)` / `Fees (Mean)` *features*, and `gross` also appears in the Profit-Factor definition ("gross profits to gross losses"); `leverage` appears twice, both qualitative (Section 5.2 "leveraged futures market", Section 6 "systematically leveraged") with **no leverage number anywhere**.
- **Gross-versus-net status is stated** (gross, and explicitly deferred). Everything about execution — signal-to-order timing, order type, fill price, latency, position limits, sizing, margin, liquidation, failure handling — is `underspecified` or `data gap`.
- Because the strategy is a high-frequency, two-sided, minute-bar event strategy on leveraged futures, the gross numbers carry an unquantified cost exposure that the source does not bound; no break-even cost, no net Sharpe and no capacity figure can be formed from this source.

## Evidence

### Source-reported

All figures below are read from the pinned PDF (SHA-256 `1a23ff6b…`) on the out-of-sample window **January 2022 – January 2024** and are **gross of trading costs**. They have **not** been independently reproduced. Metric order is `RR % | MDD % | PF | SRPR | SORR | LDD (days)`.

**Table 2 — out-of-sample, optimised static `theta_s = 0.026` (in-sample-selected), against a single-asset Bitcoin implementation and three benchmark portfolios:**

| Column | RR % | MDD % | PF | SRPR | SORR | LDD |
|---|---|---|---|---|---|---|
| Portfolio (`theta_s = 0.026`) | 31.25 | −56.31 | 1.09 | 0.46 | 0.63 | 316 |
| Bitcoin (single-asset DC) | 75.96 | −37.90 | 1.18 | 0.63 | 0.94 | 434 |
| Equally Weighted (EW) | −19.05 | −66.20 | 1.01 | 0.07 | 0.10 | 728 |
| HRP | −17.79 | −65.97 | 1.02 | 0.08 | 0.11 | 728 |
| HERC | −17.76 | −65.95 | 1.02 | 0.08 | 0.11 | 728 |

Source's reading (Section 4.1): the SU portfolio beats EW/HRP/HERC but is beaten on both absolute and risk-adjusted basis by the single-asset Bitcoin implementation (0.46 vs 0.63), which is the stated economic motivation for going adaptive.

**Table 3 — adaptive vs static (headline), same window:**

| Strategy | RR % | MDD % | PF | SRPR | SORR | LDD |
|---|---|---|---|---|---|---|
| Panel A — Static `theta_s = 0.01` | 63.19 | −47.87 | 1.11 | 0.59 | 0.81 | 261 |
| Panel A — Static `theta_s = 0.02` | −30.43 | −56.14 | 1.02 | 0.11 | 0.15 | 458 |
| Panel A — Static `theta_s = 0.04` | 45.23 | −50.50 | 1.11 | 0.53 | 0.73 | 356 |
| **Panel B — Adaptive, combined features** | **445.98** | **−29.91** | **1.27** | **1.34\*\*** | **1.94** | **156** |
| Panel C — EW | −19.05 | −66.20 | 1.01 | 0.07 | 0.10 | 728 |
| Panel C — HRP | −17.79 | −65.97 | 1.02 | 0.08 | 0.11 | 728 |
| Panel C — HERC | −17.76 | −65.95 | 1.02 | 0.08 | 0.11 | 728 |

`\*\*` = the Sharpe is statistically greater than the best static strategy (`theta_s = 0.01`) at the 1% level by the robust bootstrap of Ledoit and Wolf (2008). Section 4.2 states the bootstrap p-value for the Sharpe difference is **0.008** and that `H0` is rejected at 1%.

**Table 4 — out-of-sample performance by information set (each meta-model trained on one feature family only):**

| Feature set | RR % | MDD % | PF | SRPR | SORR | LDD |
|---|---|---|---|---|---|---|
| Strategy Meta-Information | 323.77 | −28.16 | 1.23 | 1.17 | 1.68 | 109 |
| On-Chain Information | 199.04 | −39.60 | 1.18 | 0.93 | 1.33 | 133 |
| DC-Derived Indicators | 194.30 | −48.24 | 1.18 | 0.92 | 1.30 | 171 |
| Market Regime Information | 372.15 | −44.69 | 1.24 | 1.19 | 1.71 | 323 |

Section 4.3 reads this as evidence that the two *novel* sets (on-chain 0.93, DC 0.92) are valuable while the combined model (1.34) beats every single-family model, implying complementarity; Appendix F reports pairwise correlations of the models' daily output probabilities, mostly near zero with the usual within-model class competition around −0.43 to −0.57.

**Table G.1 — hyperparameter sensitivity (combined model, out-of-sample)**: `h_strategy` 1/5/7/10 → RR 445.98 / 408.68 / 225.21 / 559.00, SRPR 1.34 / 1.24 / 0.97 / 1.37; `h_dc` 5/10/20/30 → 375.91 / 247.83 / 420.66 / 445.98, SRPR 1.23 / 1.03 / 1.30 / 1.34; `h_regime` 7/10/12/15 → 445.88 / 445.98 / 371.49 / 115.94, SRPR 1.34 / 1.34 / 1.22 / **0.76**; `h_onchain` 1/5/7/10 → 445.98 / 269.70 / 336.28 / 293.74, SRPR 1.34 / 1.07 / 1.19 / 1.12; `alpha` 5/10/50/100 → 445.98 / 361.18 / 206.70 / 313.77, SRPR 1.34 / 1.20 / 0.96 / 1.14. Asterisked "original" values: `h_strategy=1`, `h_dc=30`, `h_regime=10`, `h_onchain=1`, `alpha=5`.

**Table H.1 — weighted vs unweighted loss**: unweighted combined **496.57 / −37.54 / 1.28 / 1.37 / 2.02 / 143**; weighted combined **445.98 / −29.91 / 1.27 / 1.34 / 1.94 / 156**. Unweighted → weighted for the four single families: 296.85→323.77, 137.06→199.04, 309.02→194.30, 250.38→372.15.

**Table I.1 — alternative learner**: adaptive **XGBoost** 412.33 / −31.54 / 1.26 / **1.28** / 1.85 / 168 vs best static 63.19 / −47.87 / 1.11 / 0.59 / 0.81 / 261.

**Section 4.5 (qualitative)**: temporal feature importance shows DC-derived indicators dominating during the high-volatility early-2022 regime and on-chain metrics plus strategy meta-information dominating as volatility subsided in late 2022-2023; SHAP plots are read as the model choosing a small `theta_s` (mean-reverting conditions: high Z-score + positive ETH exchange netflow) and a large `theta_s` (accumulation: long average position lengths + negative exchange netflow).

### Independently reproduced

not independently reproduced

We verified only the artefact and the reading: PDF byte count, page count and SHA-256 recorded above, full 42-page text extraction and end-to-end read, DOI resolution through OpenAlex/Semantic Scholar, and every quoted number located in its named table of the pinned PDF. No strategy was re-implemented, no model was re-trained, no portfolio was re-run, and the source ships no code and no data.

### Negative evidence

1. **Explicitly gross of costs.** Section 6 defers the net-of-cost study to future work; fees, funding, spread, slippage, impact, participation, capacity, borrow, financing, leverage, margin, latency, fill, failure handling and turnover are all `data gap`, never zero. The source's own §5.2 warns the returns come from "a leveraged futures market" — so the gross figure is exposed to an unquantified, plausibly large cost and funding drag.
2. **Turnover is never reported**, even though the strategy re-evaluates minute DC events, closes on the opposing small-theta event, and re-selects `theta` daily — words like `turnover`, `commission`, `bid-ask`, `capacity` appear zero times.
3. **The paper's own novel contribution does not help the headline model.** Table H.1: unweighted combined RR 496.57 / Sharpe 1.37 beats the weighted combined 445.98 / 1.34, and §4.4's claim of improvement in "four of the five" specifications is contradicted by its own table (three of five improve).
4. **Label-timing ambiguity** between the §3.4 prose (predict day `d+1` from `m_d`) and Eq. 11 (label = argmax of `Return(theta_i, d)`), which is exactly the difference between a legitimate next-day prediction task and a contemporaneous fit.
5. **The chosen main configuration has no stated selection rule.** Appendix G prints out-of-sample Sharpe from **0.76 to 1.37** and RR from **115.94 to 559.00** across 16 configurations, with the reported "original" cell starred, but the paper never says the starred cell was fixed before the out-of-sample window → possible out-of-sample hyperparameter selection, untestable from the source.
6. **Whole-sample universe construction.** The top-50 set is chosen as "representative of the sample period (January 2021 to January 2024)", i.e. using the full sample including the evaluation window; delisted, renamed or re-ranked coins are not discussed → survivorship / point-in-time gap.
7. **Static parameter fragility is extreme**: adjacent `theta_s` values flip sign out of sample (0.01 → +63.19%, 0.02 → −30.43%, 0.04 → +45.23%), and the in-sample-optimised 0.026 gives only 0.46 Sharpe — the exact fragility the adaptive claim is built on, but also evidence that the underlying edge per threshold is thin.
8. **The multi-asset portfolio does not beat the single-asset BTC implementation in the static case** (0.46 vs 0.63, Table 2), and the adaptive model is never run on the single-asset BTC case, so the paper never shows that its SU portfolio construction adds value where the adaptation happens.
9. **Benchmark set is weak and mixed.** EW/HRP/HERC are passive portfolios printing −17.8% to −19.1% and Sharpe 0.07-0.08 over the window, while a *traded* single-asset BTC column prints +75.96%; a long-short leveraged futures DC book and long-only passive portfolios are printed side by side without an apples-to-apples control, and no buy-and-hold BTC baseline is shown for the adaptive model.
10. **Statistical support is one bootstrap on one window.** A single Ledoit and Wolf (2008) p = 0.008 on the Jan 2022-Jan 2024 daily returns, with no multiplicity control across Tables 2, 3, 4, G.1, H.1, I.1 (16+ configurations, 4 feature families, 3 static thetas, 2 learners).
11. **Two-year out-of-sample, one market path**, no subperiod or regime breakdown table, no second confirmation window, no walk-forward repetition with different origins.
12. **An unsupported negative claim**: Section 5.3 asserts that "a naive volatility-timing strategy fails to replicate our results" — no table, no numbers, no specification for that control appears anywhere.
13. **No code, no data, no availability statement**; the Glassnode feed is paid/licensed; the first-level DC classifier algorithm and the numeric `theta_b` are never disclosed → the printed strategy cannot be re-run from the document.
14. **Execution layer entirely missing**: sizing, leverage, margin, liquidation, order type, fill price, funding treatment, contract specification (perpetual vs dated), timezone/session convention.
15. **Walk-forward terminology is internally inconsistent** (§3.5 labels an expanding-window scheme "fixed-origin" and a fixed-length scheme "rolling-origin"), so the refit schedule must be re-derived rather than copied.
16. **Source-internal editorial defects**: duplicated paragraph across §2.2/§2.3, repeated subsection numbering (two 3.1s, seven 3.4s), and Appendix C referenced for "features and trading logic" while the logic (Algorithm 2) sits in Appendix D.1.
17. **Version identity is not perfectly pinned**: PDF cover 2025-09-24 vs SSRN Date Written 2025-09-18 vs Posted 2025-09-25, with no revision entry; 0 references / 0 citations shown on the landing page.
18. **Status**: preprint working paper, no venue, no peer review, no independent replication; all performance claims are third-party, source-reported and gross.

## Falsification plan

Every threshold below is `research-defined` (Scout-chosen) and every operational rule not printed by the source is `research-proposed`. Data: Binance minute futures bars for a point-in-time top-50 universe, plus a licensed on-chain feed, with the source window (Jan 2021 – Jan 2024) extended forward. Action on failure: record the hypothesis as disproved for this deployment and drop the candidate — no retuning of thresholds after seeing results.

- **F1 — frozen forward replication.** Re-run the entire pipeline on a later frozen window of ≥ 6 months ending after 2026-01 with ≥ 3 independent runs (different walk-forward origins). **Pass** only if the adaptive book's Sharpe exceeds the best static `theta` with a moving-block-bootstrap 95% CI on the difference excluding zero. **Fail** otherwise.
- **F2 — cost ladder (decisive for tradability).** Net the identical book at 0/1/5/10/20/30 bp per side plus a Binance-style taker-fee and funding schedule (funding applied at each settlement while a position is open). **Fail** if net Sharpe < 0.50 at 10 bp one-way, or if realistic frictions erase > 50% of the gross Sharpe advantage (1.34 → below 0.67).
- **F3 — turnover and capacity audit.** Measure one-way daily turnover of the DC book and participation versus 10% of 20-day ADV on the held contracts. **Fail** if daily one-way turnover exceeds 40% or the book cannot be filled within the participation cap; the source prints neither number, so this test produces what the source lacks.
- **F4 — decisive adaptive-layer ablation.** Compare (a) adaptive combined, (b) adaptive with the on-chain block removed, (c) adaptive with the DC block removed, (d) best static `theta`, all on the same frozen window. **Pass** only if (a) beats (d) by ≥ 0.30 Sharpe *and* (b) or (c) is materially worse than (a) — otherwise the result is "adaptive helps" but the two claimed novel information sets do not.
- **F5 — weighted-loss claim.** Re-run combined and the four single families with and without `w_d = exp(alpha·Δr)`. **Fail** the paper's methodological contribution if the weighted loss does not improve RR in ≥ 4 of 5 specifications (the source's own criterion) or if unweighted combined still wins.
- **F6 — label-timing audit.** Rebuild the meta-label under both readings (label = argmax of day `d` vs day `d+1` returns) and re-evaluate. **Fail** if the reported advantage only appears under the reading that uses same-day `d` returns alongside same-day features.
- **F7 — hyperparameter-selection audit.** Pre-register the starred configuration using in-sample data only, then evaluate once out of sample; repeat across ≥ 3 walk-forward origins. **Fail** if the pre-registered cell's Sharpe advantage over the best static `theta` disappears, or if the Appendix G spread (0.76–1.37) shows the reported 1.34 sits in the top quartile of a grid searched on the test window.
- **F8 — point-in-time universe.** Rebuild the top-50 ranking month by month with no look-ahead, including delisted and re-ranked names. **Fail** if adaptive Sharpe drops by more than 25% relative to the whole-sample universe.
- **F9 — permutation null.** Circularly shift the meta-model's daily `theta` choices relative to realized base-strategy returns (1000 draws). **Pass** only if the observed adaptive Sharpe exceeds the 95th percentile of the null.
- **F10 — multiplicity.** Apply Benjamini–Hochberg over the family of adaptive-vs-static comparisons (4 feature sets × 3 thetas × 2 learners × the reported grid). **Fail** if nothing survives `q < 0.10`.
- **F11 — regime / subperiod stability.** Split the extended window into ≥ 3 contiguous subperiods (and label each as high/low volatility a priori). **Fail** if ≥ 2 of 3 subperiods are non-positive for the adaptive-minus-static spread.
- **F12 — reproducibility gate.** If no code and no data become public within 12 months of 2025-09-24, mark the result permanently `unverifiable` and drop it regardless of printed numbers; if they do, a third party must reproduce Table 3 within ±20% on RR and ±0.15 on Sharpe.
- **F13 (crypto-native control).** Because the venue is already crypto, run the funding-aware and liquidation-aware variant: cap leverage, model mark-price liquidation, and add a 24/7 session-stress split (Asia/EU/US hours). **Fail** if the advantage exists only in one session block or only when funding is ignored.

## Crypto portability

**`direct`.**

The source's own evidence is crypto: Binance minute futures on a top-50 crypto universe, Jan 2021 – Jan 2024, long and short. No porting of a traditional-asset mechanism is required, so this is not a `research-proposed` adaptation. What remains `data gap` *inside* that direct setting: whether the contracts are **perpetual or dated** (never stated), **funding-rate** treatment (explicitly unmodelled and deferred), **mark vs last price** for candle and liquidation logic, **margin and liquidation** handling (absent, while §5.2 states the returns come from a leveraged futures market), **single-venue** dependence (Binance only, no venue-fragmentation analysis), and **timestamp/timezone** convention for minute bars and DC event detection. The 24/7 structure is naturally handled by DC event time, but minute-bar boundaries still require an explicit convention that the source does not print.

Crypto portability is not authorisation to trade; F2, F3 and F13 must pass before any deployment consideration.

## Limitations

- **`data gap`**: every trading-cost field (fees, spread, slippage, impact, participation, capacity, borrow, financing, leverage, margin, latency, fill, failure handling, turnover, funding); contract specification; timezone/session convention; the numeric `theta_b`; the first-level DC classifier algorithm; position sizing; code and data availability; data vendor for the on-chain feed beyond "Glassnode".
- **`underspecified`**: meta-label timing (Eq. 11 vs §3.4 prose), walk-forward naming and exact refit schedule, order type and execution price, liquidation handling, missing-data and delisting treatment, month-by-month universe membership.
- **`not stated in source`**: whether any hyperparameter in Appendix G was chosen before the out-of-sample window; the specification behind the §5.3 "naive volatility-timing" control.
- **`not independently reproduced`**: every number in this record; we hashed and read the pinned 42-page PDF but re-ran nothing, and the source provides no code or data.
- **`unproven`**: out-of-sample stability beyond one two-year window; any net-of-cost profitability; any capacity claim; multiplicity-adjusted significance; the paper's claim that on-chain and DC feature sets are *causally* the source of the gain.
- **Design limitations**: whole-sample top-50 selection, passive-versus-leveraged-book benchmark mixing, single bootstrap, no subperiod table, one internally contradicted ablation claim (Table H.1 vs §4.4), duplicated and mis-numbered sections, inconsistent appendix cross-references, manuscript date mismatch, preprint status with no venue and no peer review.
- **Scope**: this is a record of *research material*. Presence in this repository does not imply the strategy works, was validated, or may be traded.

## Implementation status

`implementation_status: not-implemented`. No implementation exists in our research stack: no DC engine was built, no meta-model was trained, no portfolio was constructed, and no backtest, Paper, Testnet or Live run has occurred. The source itself ships no code and no data. Nothing here implies Qlib full-backtest validation or any downstream approval.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record did **not** pass Research Intake Review, did **not** enter Hermes Wiki Brain as an adopted record, did **not** enter the production candidate pool, did **not** complete Qlib validation, and did **not** become a frozen survivor or leaderboard entry. It is not evidence of profitability, not validated alpha, and not approval to implement, paper-trade, testnet-trade or trade.

## Related Wiki records

Mechanism-adjacent pages returned and verified by Wiki Brain `kb_search` for this run (`crypto regime trading strategy` → 10 hits; `on-chain metrics` → 10 hits; `directional change threshold extreme point` → 10 hits; queries `cryptocurrency regime-dependent predictability meta-learning adaptive market hypothesis trading`, `on-chain Glassnode bitcoin metrics directional change event-based sampling portfolio` and `State-Dependent Market Inefficiency Cryptocurrency Markets Barak` each returned 0):

- [[quant/bitcoin-regime-aware-meta-learning-selective-directional-trading-2026-09-13]]
- [[quant/path-signature-regime-detection-crypto-leverage-cycle-2026-09-13]]
- [[quant/bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31]]
- [[quant/ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01]]
- [[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]]

No other Wiki Brain pages were verified for this record; no page is linked beyond the five returned by search, and no Wiki Brain page exists for this SSRN paper.

## Sources

1. Barak, S., Razmi, S., & Mousavi, A. (2025). *State-Dependent Market (In)Efficiency in Cryptocurrency Markets* (Date Written 18 September 2025; PDF cover 24 September 2025; Posted 25 September 2025; 42 pages). SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5525163 — DOI https://doi.org/10.2139/ssrn.5525163. Corresponding author Sasan Barak, Southampton Business School, University of Southampton. JEL G11, G12, G14, C58. SSRN landing shows 0 References / 0 Citations and the notice "All rights reserved. No reuse allowed without permission."
2. Pinned full text (PDF): https://papers.ssrn.com/sol3/Delivery.cfm/5525163.pdf?abstractid=5525163&mirid=1 — 1,698,816 bytes, 42 pages, SHA-256 `1a23ff6ba301d1b53aa6c8ca9a58f2d57e21190aa0ee77ed86deae066eeb8acc`, retrieved 2026-09-26 through an authenticated browser session (curl and scrapling receive Cloudflare HTTP 403), text extracted to 102,814 characters and read end to end.
3. OpenAlex work record `W7083296082` (https://api.openalex.org/works/doi:10.2139/ssrn.5525163), retrieved 2026-09-26 — confirms type `preprint`, single DOI location, no alternate open full text; Semantic Scholar DOI lookup returned HTTP 404.

All quantitative claims above are labelled source-reported and trace to Table 2, Table 3, Table 4, Table G.1, Table H.1, Table I.1, Table 1 (notations), Figure 5, Figure 6, Figure 7, Figure 8, Figure 9, Sections 3.1-3.5, 4.1-4.5, 5.2, 5.3, 6, Appendix A, Appendix C (Eqs. C.1-C.4), Appendix D.1 (Algorithm 2), Appendix E, Appendix F, Appendix G, Appendix H, Appendix I and Appendix J of source 1 as rendered in source 2. All are gross of trading costs and none has been independently reproduced.
