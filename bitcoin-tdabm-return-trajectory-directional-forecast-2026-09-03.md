---
schema: strategy-research-record-v1
title: "Bitcoin TDABM Return-Trajectory Directional Forecast"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - time-series
  - topology
  - directional-forecast
status: research-only
confidence: medium
source_as_of: 2024-12-12
sources:
  - "Simon Rudkin, Wanling Rudkin, Pawel Dlotko, 'Return trajectory and the forecastability of bitcoin returns', Financial Review 60(2), 509-539. DOI: https://doi.org/10.1111/fire.12420"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 6.1 states that, after epsilon calibration, new TDABM covers are constructed across the combination of the test and calibration sets. If read literally, this would contaminate an out-of-sample forecast because the cover colouration depends on realized labels. The surrounding text instead treats the test set as held out and trains LO/RF on training+calibration. The paper/code must be checked before treating the reported TDABM OOS results as leakage-safe."
---

# Bitcoin TDABM Return-Trajectory Directional Forecast

## Provenance

Primary source: Simon Rudkin, Wanling Rudkin, and Pawel Dlotko, *Return trajectory and the forecastability of bitcoin returns*, **Financial Review**, 60(2), 509-539; first published 2024-12-12; DOI `10.1111/fire.12420`.

The paper is open access through Wiley. The source states that daily BTC price data are obtained from CoinMarketCap through 2023-03-15, while trajectory evaluation is limited to 2022-12-31 so longer-horizon forward returns remain observable. Returns are percentage log returns from daily closes. The paper also states that replication R code is available from the corresponding author's website, but no immutable code snapshot was reviewed in this Scout cycle.

Repository-wide and Hermes Wiki Brain searches found no existing record for DOI `10.1111/fire.12420`, the exact paper title, `TDABM`, or `topological data analysis ball mapper`. This record is materially distinct from generic time-series momentum, FPCA return forecasting, and cross-sectional momentum records because the signal is defined by **local geometry in a lagged-return trajectory space**, not by cumulative return, moving-average state, factor rank, or functional-principal-component score.

## Economic mechanism

### Source-reported

The authors argue that Bitcoin return predictability is not uniform across history. Instead, only subsets of recent return trajectories appear to contain information about subsequent return direction. They define a trajectory as the chronological vector of recent BTC returns and use Topological Data Analysis Ball Mapper (TDABM) to group geometrically similar trajectories into equal-radius neighborhoods. If past trajectory shape contains information, trajectories occupying the same neighborhood should exhibit similar subsequent return signs.

The paper links this idea loosely to time-series momentum and technical-analysis predictability, but its central claim is narrower: **predictability is state-dependent on the path of recent returns rather than on one scalar momentum statistic**.

### Research interpretation

The falsifiable mechanism is **path-dependent local-state persistence / reversal**. A scalar trailing return collapses ordering information; two windows can have the same cumulative return but very different sequences of shocks, reversals, and jumps. A local-neighborhood method can distinguish these histories and estimate the empirical probability of a positive future return conditional on trajectory shape.

The hypothesis is not that every trajectory is predictable. The source explicitly finds that the dense/common part of trajectory space is often close to 50/50, while rarer peripheral regions sometimes have much stronger directional consistency. Therefore any deployable version should be tested as a **conditional signal or gating variable**, not assumed to provide unconditional directional alpha.

## Signal

### Source-reported construction

Daily BTC return:

`r_t = 100 * (log(P_t) - log(P_{t-1}))`

where `P_t` is the CoinMarketCap daily closing price.

For a trajectory length `d`, construct the point:

`x_t = [r_t, r_{t-1}, ..., r_{t-d+1}]`.

The daily forecasting experiments use:

- `d = 7` daily returns (one-week trajectory cloud);
- `d = 14` daily returns (two-week trajectory cloud).

The source evaluates five forecast targets:

1. sign of next-day return;
2. sign of the return one week ahead;
3. sign of the return two weeks ahead;
4. sign of cumulative buy-and-hold return over the next week;
5. sign of cumulative buy-and-hold return over the next two weeks.

At a candidate ball radius `epsilon`, TDABM creates a cover of the training trajectory point cloud. The paper uses **100 random TDABM covers per epsilon** because landmark choice is stochastic. Candidate epsilon values are evaluated in increments of `0.1`; the exact common lower/upper search bounds for the forecasting experiment are **underspecified** in the text reviewed in this cycle.

For each calibration point:

- assign it to every ball whose landmark lies within `epsilon`;
- if it falls in no ball, assign it to the nearest landmark's ball;
- each ball's colouration is the proportion of constituent training points whose future-return sign equals 1;
- average colouration across assigned balls;
- classify **up** when average colouration is `>= 0.5`, otherwise classify **down**;
- majority-vote the binary classification across the 100 stochastic covers at that epsilon.

Choose `epsilon*` as the radius with the highest calibration classification accuracy.

The source then applies the calibrated TDABM classifier to the test set. However, Section 6.1 contains a material ambiguity: it says new covers are constructed across the **combination of the test and calibration set** at `epsilon*`, while the surrounding description treats test points as out-of-sample observations to be assigned to the learned cover. If the phrase is literal and test labels affect colouration, this is leakage. If it is a wording error and the intended set is training+calibration, the design is conventional. This ambiguity must be resolved from replication code before independent use.

### Research-proposed operationalization

No live trading rule is source-reported. For a testable trading translation only:

- Use a leakage-safe expanding or rolling train/calibration/test split.
- Build the TDABM cover using **training labels only** during parameter search, then rebuild on training+calibration only after selecting `epsilon*`.
- At UTC daily close, form the most recent 7- or 14-day trajectory from fully closed daily bars.
- Produce `p_up` from the average ball colouration.
- **Research-proposed entry:** long BTC for the chosen forecast horizon only when `p_up >= 0.55`; short or flat when `p_up <= 0.45`; remain flat in the middle band.
- The `0.55/0.45` thresholds are **research-proposed** and are not in the source.
- **Research-proposed exit:** time exit at the forecast horizon; do not overlap positions unless overlap is explicitly modeled.
- Position sizing, stops, leverage, and re-entry rules are **underspecified** by the source and must not be inferred from the reported classification study.

## Required data

- **Instrument:** Bitcoin.
- **Source-reported venue/data vendor:** CoinMarketCap daily BTC closing prices.
- **Market type:** the source studies a generic BTC price series rather than a specified executable spot/perpetual instrument.
- **Timeframe:** daily; weekly experiments also exist in the paper but this record focuses on the stronger daily forecasting result.
- **Fields:** daily closing price sufficient for source-reported trajectory construction; executable testing additionally needs bid/ask or realistic next-bar prices and transaction-cost inputs.
- **Trajectory features:** 7 or 14 consecutive percentage log returns, with exact chronological ordering preserved.
- **Labels:** sign of future point return or cumulative return at 1-day, 7-day, or 14-day horizons as defined by the experiment.
- **Point-in-time requirement:** every trajectory must use only fully observed returns at signal time; future-return labels must be restricted to training/calibration partitions during fitting.
- **Timestamp:** the source's CoinMarketCap daily closing convention must be matched exactly for replication. Crypto UTC/day-boundary differences are material.
- **Missing data:** source handling is not described in sufficient detail; no silent imputation should be used.
- **Execution data:** fees, spread, slippage, funding, borrow and impact are not part of the source's classification evidence and must be added for tradability tests.

## Execution assumptions

The paper is a return-direction forecasting study, not a live execution study.

Source-reported execution assumptions are therefore largely **underspecified**:

- no market-vs-limit order rule;
- no fill model;
- no spread/slippage model;
- no maker/taker fee treatment;
- no market impact/capacity model;
- no perpetual funding treatment;
- no short-borrow or margin assumption;
- no explicit signal-to-order latency.

A valid trading test must use the first executable price after the daily signal is finalized and must prevent same-bar look-ahead. If translated to perpetual futures, funding and liquidation/margin risk must be modeled separately from directional forecast accuracy.

## Evidence

### Source-reported

The paper reports that daily TDABM forecasts achieve roughly **55% out-of-sample directional accuracy on average in some settings, with individual forecasts reaching as high as approximately 67%**. The authors report that TDABM produces the highest forecast accuracy in 29 of 70 daily forecast cases, the same count as random forest, while logit is best in 17 cases; ties cause totals to exceed 70.

The paper further reports that TDABM beats the best naive all-up/all-down forecast in **15** daily cases, versus **10** for random forest and **4** for logit. Six TDABM cases are described as having accuracy near 60%, while random forest never reaches 60% in their comparison.

The daily forecasting design uses expanding annual training windows: the smallest configuration trains on calendar 2014, calibrates on 2015, and tests on 2016; calibration and test years then roll forward while the training sample expands.

Important negative result: the **weekly** TDABM forecaster performs poorly. In the 2022 weekly test, TDABM generally underperforms the logit and random-forest alternatives and often resembles a naive all-up classifier. The paper therefore does not support an unconditional claim that TDABM works at every horizon.

All figures above are source-reported and have not been independently reproduced.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source itself reports weak weekly forecasting performance and states that many trajectory regions are close to 50/50 directional outcomes.
- The signal appears strongest in smaller/rarer trajectory neighborhoods, raising small-sample and multiple-testing concerns.
- The classifier optimizes `epsilon` on calibration accuracy and scans many radii/horizons/trajectory lengths; robust nested validation is required to estimate data-snooping risk.
- The paper does not report net trading PnL, turnover, fees, slippage, funding, borrow, capacity, or implementation shortfall.
- **Potential leakage ambiguity:** Section 6.1 says the post-calibration cover is built from the combination of the test and calibration sets. If test-set labels enter ball colouration, the headline OOS result is invalid. The replication code must resolve this before the evidence is treated as leakage-safe.
- CoinMarketCap's historical daily close construction may differ from executable exchange close/mid prices and may have historical data revisions.
- The sample ends around the 2022 regime, before the U.S. spot-Bitcoin-ETF era and later market-structure changes.

## Falsification plan

1. **Leakage audit — mandatory first gate**
   - Data: exact source-style BTC daily series and, if obtainable, the authors' R code.
   - Test: verify that test labels never enter cover construction, colouration, epsilon selection, nearest-ball assignment statistics, or any preprocessing.
   - **Research-defined falsification threshold:** any use of future test labels in feature construction or ball colouration invalidates the claimed out-of-sample evidence; stop and classify the source result as contaminated until corrected.

2. **Exact source replication**
   - Reconstruct 7- and 14-day trajectory clouds and annual train/calibration/test splits.
   - Reproduce Table 4 classification accuracies within rounding tolerance.
   - **Research-defined falsification threshold:** if a leakage-safe implementation cannot reproduce the qualitative ranking and reported accuracy range, downgrade the hypothesis materially.

3. **Strict post-2022 out-of-sample test**
   - Freeze signal construction and epsilon-search protocol using only pre-2023 history.
   - Test 2023 onward, including the spot-ETF era, without retuning after observing results.
   - Metrics: balanced accuracy, MCC, Brier score, log loss, and directional accuracy relative to all-up/all-down and simple sign-momentum/reversal baselines.
   - **Research-defined falsification threshold:** reject incremental forecasting value if TDABM does not beat the best naive and simple autoregressive/sign baselines on balanced accuracy/MCC over the held-out period.

4. **Economic-value test**
   - Translate probabilities into the research-proposed no-trade-band policy.
   - Include realistic spot and perpetual fees, spread, slippage, funding, and delayed next-bar execution.
   - **Research-defined falsification threshold:** reject tradability if net expected return is non-positive or if performance disappears under modest cost stress.

5. **Trajectory-ablation test**
   - Compare TDABM against scalar 7-day/14-day cumulative return, realized volatility, max drawdown, and simple k-nearest-neighbor models on the same lag vector.
   - **Research-defined falsification threshold:** if the topology-based neighborhood adds no stable OOS information beyond these simpler summaries, reject the claim that trajectory geometry provides incremental alpha.

6. **Radius and rarity robustness**
   - Evaluate predeclared epsilon grids and minimum ball-membership thresholds.
   - Track accuracy by neighborhood support count.
   - **Research-defined falsification threshold:** if performance is concentrated only in tiny neighborhoods whose confidence intervals span the naive rate after multiple-testing correction, treat the effect as unstable/noise.

7. **Clock / venue robustness**
   - Rebuild daily bars on at least two liquid executable venues and UTC boundary variants.
   - **Research-defined falsification threshold:** if sign predictions materially flip with reasonable day-boundary or venue choices, reject portability as operationally fragile.

## Crypto portability

**direct** for the research mechanism because the cited source itself studies Bitcoin.

Trading portability remains unproven. The source uses a CoinMarketCap daily price series rather than a specified executable venue/instrument. A deployment test must decide whether the signal targets:

- BTC spot;
- BTCUSDT perpetual;
- BTCUSD inverse perpetual/futures;
- another venue-specific contract.

Crypto-specific risks include 24/7 bar-boundary sensitivity, exchange fragmentation, perpetual funding, index/mark-price differences, stablecoin quote effects, liquidation/margin risk, and venue outages. These are not addressed by directional classification accuracy alone.

## Limitations

- **underspecified:** exact forecasting epsilon search bounds are not fully specified in the reviewed text.
- **contested methodology:** Section 6.1 contains a potentially serious train/calibration/test wording inconsistency that may imply leakage if literal.
- **not independently reproduced**.
- **data gap:** no immutable replication-code snapshot was reviewed in this cycle.
- No trading-cost or fillability evidence.
- Single-asset evidence only.
- Possible data-snooping across trajectory lengths, horizons, and epsilon choices.
- Classification accuracy is not equivalent to positive expected trading return.
- Results may be regime-dependent and may not survive post-2022 market structure.

## Implementation status

No implementation in PyBroker, NautilusTrader, Paper, Testnet, or Live has been created or authorized from this record.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not establish profitable alpha, does not authorize implementation, and does not authorize Paper, Testnet, or Live trading.

Any thresholds or executable rules added by this Scout are explicitly labeled **research-proposed** or **research-defined falsification threshold** and are not source-reported.

## Related Wiki records

No matching TDABM / return-trajectory record was found in Hermes Wiki Brain during the pre-write search.

Conceptually adjacent repository records include the Bitcoin rolling FPCA hourly return-direction record and generic momentum / return-sign forecasting records, but they use materially different signal constructions and are not duplicates.

## Sources

1. Simon Rudkin, Wanling Rudkin, Pawel Dlotko, *Return trajectory and the forecastability of bitcoin returns*, **Financial Review** 60(2), 509-539. First published 2024-12-12. DOI: https://doi.org/10.1111/fire.12420
2. Wiley open-access full text for the same article: https://onlinelibrary.wiley.com/doi/10.1111/fire.12420
