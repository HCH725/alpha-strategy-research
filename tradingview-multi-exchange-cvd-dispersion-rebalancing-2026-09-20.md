---
schema: strategy-research-record-v1
title: TradingView multi-exchange CVD dispersion and rebalancing hypothesis
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-10-05
sources:
  - https://www.tradingview.com/script/hu62GTix-CVD-Spaghetti-Multi-Exchange-Perpetuals/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView multi-exchange CVD dispersion and rebalancing hypothesis

## Provenance

- **Primary source:** mxdvt07, “CVD Spaghetti - Multi-Exchange (Perpetuals),” TradingView open-source script, first published 2025-09-08 and updated 2025-10-05.
- **Stable public URL:** https://www.tradingview.com/script/hu62GTix-CVD-Spaghetti-Multi-Exchange-Perpetuals/
- **Source type:** Public TradingView open-source indicator / research implementation.
- **Source as-of:** 2025-10-05, the latest update date visible on the reviewed page.
- The source describes a multi-venue perpetual-futures CVD comparison and does not provide an independently validated trading backtest.

## Economic mechanism

### Source-reported

The author states that cumulative volume delta can differ materially across crypto perpetual venues. Synchronized CVD direction across major exchanges is presented as confirmation of broad buying or selling pressure, while one-venue or small-subset divergence is described as a possible localized liquidity imbalance. The source further suggests that cross-exchange discrepancies may precede rebalancing as arbitrage activity restores alignment.

### Research interpretation

The falsifiable hypothesis is that **cross-venue dispersion in contemporaneous perpetual CVD contains incremental short-horizon information beyond aggregate CVD and price momentum**. A venue-specific order-flow shock may be temporary and mean-revert as arbitrageurs and liquidity providers rebalance across venues; conversely, synchronized CVD across venues may indicate broader participation and improve continuation odds.

This creates two competing, testable mechanisms rather than assuming a fixed directional rule:

1. **Dispersion/rebalancing:** unusually isolated CVD leadership or lagging predicts convergence or reversal of the localized move.
2. **Consensus/continuation:** low dispersion with same-sign CVD across venues confirms broad participation and predicts continuation.

Any numerical dispersion threshold, normalization window, entry rule, holding horizon, or execution rule introduced for testing is `research-proposed`; the source does not specify a canonical tradable rule.

## Signal

### Source-supported construction

- Market: cryptocurrency perpetual futures.
- CVD is computed separately by exchange and reset on a user-defined anchor period; the source states a default daily anchor and notes examples such as 1D, 4H, and 8H.
- The current source version reconstructs volume delta from lower-timeframe data using TradingView's volume-delta method. The author explicitly characterizes this as an approximation rather than true tick-level directional volume.
- Volume units are normalized across venue/contract conventions. The source states that USD-denominated contracts are divided by price; tick-denominated venues are scaled by tick size and normalized to price; multiple contracts from one exchange can be combined into one representative venue curve.
- The reviewed version names Binance, Bybit, OKX, Bitget and, after updates, Gate.io, HTX and MEXC among supported venues.
- Source interpretation: synchronized CVD supports trend confirmation; isolated venue divergence can indicate local imbalance; cross-exchange discrepancies may precede rebalancing.

### Research-proposed operationalization

For later testing only:

- At each fully closed bar, normalize each available venue's anchored CVD using only information available through that bar.
- Define a point-in-time cross-venue consensus statistic and a dispersion statistic across valid venues.
- Test whether high dispersion with one/few venue outliers predicts subsequent convergence/reversal, and whether low dispersion with same-sign consensus predicts continuation.
- Require a minimum venue count and explicitly track the venue availability set at every timestamp to avoid survivorship or silent missing-data bias.

The exact normalization, thresholds, formation horizon, entry, exit, holding period, re-entry, and position sizing are **underspecified by the source** and must remain research-proposed until separately defined and tested.

## Required data

- Synchronized crypto perpetual-futures price and volume data across multiple venues.
- Venue and contract identity, including base/quote denomination and contract/tick conversion metadata needed to normalize volume.
- Lower-timeframe data sufficient to reconstruct the TradingView-style volume-delta approximation if reproducing the source method.
- Point-in-time venue/symbol availability; missing venues must not be backfilled from future listings.
- Common timestamp boundaries and explicit timezone/candle-alignment rules across exchanges.
- For stronger validation, true aggressor-side trade data should be evaluated as an alternative to the source's price-direction volume-delta approximation.

## Execution assumptions

The source is an indicator, not a complete trading strategy. It does not specify canonical signal-to-order timing, order type, fills, fees, spread, slippage, impact, capacity, funding treatment, leverage, margin, latency, partial fills, or failure handling.

For later research, signals should be formed only after all required venue bars are closed and available. Any next-bar execution, taker/maker model, costs, latency, or cross-venue execution assumptions are `research-proposed` and must be tested explicitly.

## Evidence

### Source-reported

The source describes synchronized multi-exchange CVD as broad order-flow confirmation and cross-exchange divergence as potentially reflecting localized liquidity shocks, large-player activity, or inefficiencies that may rebalance. It does not report a traceable Sharpe ratio, CAGR, drawdown, win rate, or controlled out-of-sample performance result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly states that the CVD method is an approximation rather than true directional tick volume. The source's release notes also document prior data-accuracy/context issues and a critical exchange-total bug that was subsequently fixed, underscoring implementation and data-quality risk. No independent evidence establishing predictive alpha was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. **Consensus baseline:** Compare price-only momentum and single-venue CVD against aggregate/consensus CVD. The multi-venue hypothesis is weakened if it adds no stable out-of-sample information.
2. **Dispersion test:** At matched volatility, volume and price-momentum states, compare high cross-venue CVD dispersion with low dispersion. Test both future convergence/reversal and continuation rather than selecting the favorable interpretation after seeing results.
3. **Outlier ablation:** Compare full venue set, each single venue, leave-one-venue-out aggregates, and explicit one-venue-outlier events. A result dependent on one exchange is evidence against a general cross-venue mechanism.
4. **CVD construction ablation:** Where data permit, compare the TradingView-style lower-timeframe approximation with true aggressor-side trade delta. Reject conclusions that disappear under materially better order-flow measurement.
5. **Anchor robustness:** Test source-supported anchor choices separately and require qualitative stability rather than optimizing a single reset horizon.
6. **Placebo:** Randomly permute venue labels within matched market states or use matched pseudo-outlier timestamps. The real venue-dispersion signal must outperform placebo distributions.
7. **Point-in-time audit:** Enforce historical symbol availability, synchronized timestamps, no look-ahead normalization, and explicit missing-data handling.
8. **Costs and latency:** Apply realistic fees, spread, slippage and latency appropriate to the intended venue and horizon. Any apparent edge that is not net-positive after plausible costs fails the tradable-alpha interpretation.
9. **OOS/regime requirement:** Evaluate across multiple assets, venues and non-overlapping market regimes. Failure to persist out of sample materially weakens the hypothesis.

## Crypto portability

**direct** for the research hypothesis: the source itself is constructed from cryptocurrency perpetual-futures venue data.

Portability remains venue-dependent. Contract denomination, tick/volume conventions, liquidity, funding, symbol availability, exchange outages and candle boundaries can distort cross-venue comparisons. A result on BTC or one set of venues must not be assumed to transfer to altcoins or another venue set.

## Limitations

- **Not independently reproduced.**
- **Underspecified:** no canonical tradable threshold, entry, exit, holding period, sizing, or cost model.
- The source's CVD is an approximation based on lower-timeframe price/volume classification, not true tick-level aggressor flow.
- Cross-venue volume normalization may remain imperfect across contract types and venue reporting conventions.
- Exchange listings and data availability vary through time; naïve present-day venue selection can introduce survivorship bias.
- Divergence may reflect measurement differences or venue-specific client composition rather than exploitable arbitrage pressure.
- Multiple venue/anchor/normalization choices create substantial researcher degrees of freedom and require strict OOS control.

## Implementation status

Research record only. No implementation, backtest, reproduction, or quantitative-runtime integration has been completed as part of this Scout cycle.

## Adoption boundary

This record is research material only. It is not evidence of profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- mxdvt07, “CVD Spaghetti - Multi-Exchange (Perpetuals),” TradingView, public open-source script, published 2025-09-08, updated 2025-10-05: https://www.tradingview.com/script/hu62GTix-CVD-Spaghetti-Multi-Exchange-Perpetuals/
