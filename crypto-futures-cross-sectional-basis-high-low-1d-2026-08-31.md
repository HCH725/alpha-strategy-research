---
schema: strategy-research-record-v1
title: "Crypto Futures Cross-Sectional Basis: High-vs-Low Daily Rotation"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - futures
  - cross-sectional
  - basis
status: research-only
confidence: high
source_as_of: 2023-05-22
sources:
  - "https://doi.org/10.1002/fut.22425"
  - "https://onlinelibrary.wiley.com/doi/full/10.1002/fut.22425"
  - "https://www.repository.cam.ac.uk/handle/1810/350136"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Futures Cross-Sectional Basis: High-vs-Low Daily Rotation

## Provenance

Primary source: Yeguang Chi, Wenyan Hao, Jiangdong Hu, and Zhenkai Ran, *An empirical investigation on risk factors in cryptocurrency futures*, Journal of Futures Markets 43(8), 1161-1180, first published 2023-05-22, DOI `10.1002/fut.22425`.

The study uses 1Token data sourced from OKEx/OKX. The sample runs from 2017-11-13 through 2021-03-31 and covers up to 12 major cryptocurrencies: ADA, BCH, BSV, BTC, DOT, EOS, ETC, ETH, LINK, LTC, TRX, and XRP. Minute-level spot and current-quarter futures close prices are resampled to daily, weekly, and monthly frequencies. Spot and futures prices form the signals; only futures are traded.

The Cambridge repository identifies the article as peer-reviewed and provides a published-version record under a CC BY 4.0 license.

This record normalizes the paper's cross-sectional **basis** factor only. Momentum and basis-momentum are separate factors and are not merged into this signal.

## Economic mechanism
### Source-reported

The authors report that contemporaneous basis is the strongest of the tested cross-sectional predictors for cryptocurrency futures. They describe a catch-up process: when spot rises relative to the current-quarter futures contract, or futures falls relative to spot, a high basis can reflect futures lagging spot information; futures may then adjust faster as the pricing gap evolves. The authors state that this is consistent with both risk-based compensation and an information-segmentation explanation between spot and futures markets.

They also report that the basis premium is strongest at short horizons and largely disappears at monthly holding periods.

### Research interpretation

The falsifiable hypothesis is that the relative spot-versus-current-quarter-futures price gap contains short-horizon cross-sectional information about subsequent futures returns. At each daily ranking time, cryptocurrencies with larger positive basis should outperform those with smaller or negative basis over the next holding interval.

The mechanism is not simple mechanical convergence. Under the paper's sign convention, a high basis means spot is expensive relative to the current-quarter futures contract, and the reported premium comes from going long high-basis futures and short low-basis futures. The empirical effect therefore should be tested as a ranked cross-sectional return predictor rather than assumed to be a risk-free cash-and-carry arbitrage.

## Signal

Normalized source rule:

1. **Instrument universe:** the currently available OKEx current-quarter futures contracts among the source's 12 selected cryptocurrencies.
2. **Signal formation:** at the end of each day `t`, obtain spot close `S_t` and current-quarter futures close `F_t^CQ` for every eligible cryptocurrency.
3. **Basis signal:** compute `B_t = (S_t - F_t^CQ) / F_t^CQ`. The paper notes the log-price approximation `B_t ≈ s_t - f_t^CQ`.
4. **Cross-sectional rank:** rank all available cryptocurrencies by `B_t`.
5. **High / medium / low buckets:** allocate the highest-ranked names to the high bucket and the lowest-ranked names to the low bucket. Bucket counts vary with the number of available contracts: for 5 names use 1/3/1 high/medium/low; 7 names use 2/3/2; 6 names use 2/2/2; 8 names use 3/2/3; 9 names use 3/3/3; 11 names use 4/3/4; 12 names use 4/4/4.
6. **Long entry:** long the high-basis futures bucket.
7. **Short entry:** short the low-basis futures bucket.
8. **Holding period:** the focal daily specification holds for 1 day, then recomputes and reranks.
9. **Exit / rebalance:** positions are replaced at the next daily ranking according to the new high and low buckets.
10. **Trading instrument:** current-quarter futures only; spot is a signal input, not a traded leg.

Important specification caveat: the source describes bucket membership and long-high/short-low construction but the reviewed text does not explicitly state constituent weighting inside the high and low buckets. Therefore within-bucket weighting is **underspecified** and must not be silently assumed to be equal-weighted.

The paper explores 1-day, 1-week, and 1-month holding periods. For the basis factor itself, the signal is contemporaneous and does not require a multi-day lookback even though tables compare it alongside momentum variants with explicit lookback windows.

## Required data

- **Venue:** OKEx/OKX for source-faithful reproduction.
- **Market types:** spot plus current-quarter dated futures.
- **Universe:** point-in-time listed contracts among ADA, BCH, BSV, BTC, DOT, EOS, ETC, ETH, LINK, LTC, TRX, XRP, with listing dates respected.
- **Timeframe:** daily signal formation from minute-level source data or a daily series that reproduces the same close convention.
- **Fields:** spot close, current-quarter futures close, futures contract identity and expiry, listing/delisting history, roll timestamps.
- **Roll convention:** the source states OKEx current-quarter contracts roll at 16:00 UTC+8 on the last Friday of each quarter.
- **Timestamp:** exact daily close boundary must be documented and aligned between spot and futures. The source paper does not fully specify the resampled daily close convention beyond the underlying minute data and exchange roll timing; this is a reproduction-sensitive gap.
- **Point-in-time requirements:** only contracts available at each historical date may enter the cross-section.
- **Missing data:** no imputation rule is reported; any reproduction should exclude unavailable observations rather than silently fill them unless a separate rule is justified.
- **Costs:** commissions, spread, slippage, and roll-related execution costs are required for modern validation.

## Execution assumptions

The source reports factor returns using current-quarter futures and evaluates the focal 1-day holding portfolio both gross and after an assumed **5 basis point transaction cost**. It does not provide a complete production execution model.

Order type, intraday latency, bid/ask spread model, market impact, partial fills, position limits, margin treatment, and exact roll execution are **underspecified** in the reviewed source. The signal is formed at the end of the measurement period, so a leakage-safe reproduction should not assume execution at a price that was already needed to compute the signal unless the timing convention proves that price was tradable after formation.

A modern perpetual-futures implementation would be an adaptation, not a replication, because perpetuals replace expiry/roll economics with funding and mark/index-price mechanics.

## Evidence
### Source-reported

For the daily high-minus-low basis portfolio over 2017-11-13 to 2021-03-31, the paper reports an annualized return of **329.21% gross** and **304.98% after the paper's 5 bp transaction-cost assumption**, with reported t-statistics of **7.10 gross** and **6.62 net** and annualized Sharpe ratios of **3.82 gross** and **3.63 net**.

The authors report that the high-basis bucket materially outperforms the medium and low buckets and that a dollar invested in the basis long-short portfolio grew by roughly 150-fold gross and more than 100-fold after the stated transaction cost over the sample.

The paper's spanning regressions report that basis remains statistically significant after controlling for cryptocurrency momentum, basis-momentum, and market risk. The authors also report that much of the premium is associated with the long side rather than the short side.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The paper itself provides an important horizon boundary: the basis premium weakens as holding period increases and is not statistically significant at the monthly horizon. This indicates strong time-scale dependence rather than a persistent long-horizon factor.

The source universe is small, concentrated in major coins, venue-specific, and ends in March 2021. The extraordinarily high historical return and Sharpe estimates therefore face substantial regime, venue, sample-selection, and multiple-testing risk when transported to current markets.

The paper models transaction costs as a fixed 5 bp amount; this does not establish capacity or realistic net returns under modern spreads, impact, margin, roll mechanics, or perpetual-funding costs.

## Falsification plan

A modern reproduction should materially weaken or reject the hypothesis if any of the following occur:

1. A point-in-time reconstruction of spot and dated-futures prices fails to produce a monotonic relationship between basis rank and next-period futures return.
2. The high-minus-low spread is not positive in untouched out-of-sample data or across multiple major venues.
3. The effect vanishes when signal formation and execution are separated with a leakage-safe next-tradable-price convention.
4. The result disappears under realistic fees, spread, slippage, impact, margin, and quarterly-roll costs.
5. The premium is concentrated in a small subset of coins or one historical regime and does not survive leave-one-asset-out or subperiod tests.
6. The long-short portfolio loses significance when controlling for broad crypto beta, volatility, liquidity, and alternative cross-sectional predictors.
7. A perpetual-futures adaptation does not retain the relation after funding, mark/index price, and contract-availability effects are included.

Required controls should include random cross-sectional ranks, spot-return momentum, simple futures momentum, liquidity rank, volatility rank, and a no-signal equal-weight futures benchmark.

## Crypto portability

**Direct** for crypto markets that still offer sufficiently liquid dated futures plus corresponding spot markets and point-in-time historical data.

**Adapted / unproven** for perpetual futures. A natural perpetual analogue would require defining the relative spot-perpetual pricing signal using a consistent tradable/mark/index reference, then explicitly accounting for funding. That rule has not been source-tested here and must not be presented as the same strategy.

Venue fragmentation is material: spot and derivative price discovery can differ by exchange, and a basis measured across mismatched venues may embed transfer, credit, liquidity, or timestamp effects rather than the same signal studied by the paper.

## Limitations

- **Not independently reproduced.**
- **Underspecified:** within-bucket constituent weighting is not explicit in the reviewed methodology text.
- **Underspecified:** exact daily resampling/close boundary and signal-to-order execution timing are not fully specified.
- **Data gap:** faithful replication requires historical point-in-time spot and current-quarter futures series with contract-roll metadata.
- **Unproven:** persistence after March 2021 and across current market structure.
- **Unproven portability:** perpetual-futures adaptation is not the source-tested rule.
- Small major-coin universe and single primary venue limit generalization.
- Fixed 5 bp cost treatment is not a complete execution or capacity model.
- Very large historical annualized returns require strong skepticism and independent OOS validation.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been completed for this research record.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It is not proof that the basis premium persists, not authorization to implement it, and not approval for paper, testnet, or live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain links are asserted in this staging record. Concept-level clustering and Wiki promotion belong to the separate downstream Reviewer workflow.

## Sources

1. Yeguang Chi, Wenyan Hao, Jiangdong Hu, Zhenkai Ran, *An empirical investigation on risk factors in cryptocurrency futures*, Journal of Futures Markets 43(8), 1161-1180, first published 2023-05-22: https://doi.org/10.1002/fut.22425
2. Wiley full text: https://onlinelibrary.wiley.com/doi/full/10.1002/fut.22425
3. University of Cambridge repository record: https://www.repository.cam.ac.uk/handle/1810/350136
