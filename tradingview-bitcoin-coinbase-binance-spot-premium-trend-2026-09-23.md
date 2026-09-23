---
schema: strategy-research-record-v1
title: Bitcoin Coinbase-Binance Spot Premium Trend
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/Cp0aRqoy-CB-BTCUSD-Premium/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Coinbase-Binance Spot Premium Trend

## Provenance

Public TradingView open-source indicator **CB BTCUSD Premium**, author/page identity `Tin2100`, originally published 2024-03-26 and updated 2024-10-14. Stable source URL: https://www.tradingview.com/script/Cp0aRqoy-CB-BTCUSD-Premium/ . Source reviewed as of 2026-09-23.

The source compares Coinbase BTC/USD spot with Binance BTC/USDT spot and plots their price difference plus a user-configurable simple moving average of that premium; the source states a default moving-average period of 14.

## Economic mechanism
### Source-reported

The author presents the Coinbase-versus-Binance spot premium/discount as a way to compare Bitcoin pricing across two major exchanges in real time. The moving average is intended to help identify trends in that premium.

### Research interpretation

A falsifiable hypothesis is that persistent changes in the Coinbase-minus-Binance spot premium may proxy venue-segmented demand imbalance and therefore contain information about subsequent BTC returns or short-horizon relative-price convergence. A positive premium can arise when marginal USD spot demand on Coinbase is stronger than USDT spot demand on Binance; a negative premium can reflect the reverse. This interpretation is not established by the source and is `research-proposed`.

The key distinction from spot-versus-perpetual basis is that both legs here are spot markets. Consequently, any alpha must survive controls for USD/USDT conversion effects, venue-specific microstructure, latency, and asynchronous candles rather than being attributed to derivatives leverage or funding.

## Signal

Source-supported construction:

- Coinbase leg: Coinbase BTC/USD spot.
- Binance leg: Binance BTC/USDT spot.
- Premium: Coinbase spot price minus Binance spot price.
- Premium sign: positive when Coinbase trades above Binance; negative when Coinbase trades below Binance.
- Trend overlay: simple moving average of the premium, user configurable; default period reported by the source is 14 bars.

The source does not specify a complete trading lifecycle. Entry, exit, holding period, re-entry, position sizing, premium threshold, execution venue, and whether the premium/SMA relationship should be traded as continuation or convergence are **underspecified**.

`research-proposed` tests should separately evaluate: (1) premium sign, (2) premium change, (3) premium minus its 14-bar SMA, and (4) premium/SMA crossovers as candidate predictors. Continuation and mean-reversion interpretations must both be tested rather than assumed.

Signal formation must use only completed, timestamp-aligned observations available at decision time. Same-bar close-to-close execution must not be assumed.

## Required data

- Bitcoin spot prices from Coinbase BTC/USD and Binance BTC/USDT.
- Synchronized timestamps and candle boundaries for both venues.
- Sufficient history for the selected premium-SMA window; source default is 14 bars.
- USD/USDT price or a defensible USD-USDT normalization series to isolate stablecoin-basis contamination (`research-proposed`).
- Venue-specific bid/ask or trade data if testing executable convergence rather than predictive direction.
- Point-in-time symbol/venue availability; exchange outages, symbol changes, and missing bars must not be backfilled with future information.
- Timeframe is **underspecified** by the reviewed source description.

## Execution assumptions

The source does not specify signal-to-order timing, order type, fill model, fees, spread, slippage, market impact, latency, capacity, or shorting/borrow assumptions.

For research, use next-observation execution after signal formation and venue-specific costs rather than same-bar fills (`research-proposed`). Cross-venue convergence tests must account for transfer/settlement constraints or, if inventory is assumed pre-positioned on both venues, state that assumption explicitly. Predictive BTC-direction tests should not silently inherit arbitrage execution assumptions.

## Evidence
### Source-reported

The source describes the premium/discount visualization and a configurable SMA of the premium for identifying premium trends. No independently verified Sharpe, CAGR, drawdown, win rate, or other performance statistic is reported in the reviewed source description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical result was identified in the reviewed page; absence is not evidence of no negative result. Material alternative explanations include USD/USDT basis movement, venue latency, candle misalignment, fragmented liquidity, and transient exchange-specific order flow.

## Falsification plan

1. Reconstruct the two spot legs point-in-time with synchronized timestamps and verify that the premium is not an artifact of candle alignment.
2. Compare raw price-difference premium with percentage/log-price spread so nominal BTC price level does not mechanically change signal scale.
3. Control explicitly for USD/USDT basis. Reject the venue-demand interpretation if apparent predictability is explained by stablecoin conversion moves.
4. Test premium sign, premium change, premium-minus-SMA, and crossover variants separately; do not select the best variant on the full sample.
5. Test both continuation and convergence hypotheses with predeclared forward horizons and walk-forward/OOS evaluation.
6. Compare against BTC price momentum, simple cross-venue return lead/lag, and a no-premium baseline. Require incremental OOS information after these controls.
7. Stress the source-reported default SMA length of 14 with a local parameter neighborhood. Reject a result that depends on a narrow isolated setting.
8. Include realistic two-venue spreads, fees, slippage, latency, and asynchronous-update stress. For executable relative-value tests, require net profitability after both legs' costs.
9. Segment exchange outages, high-volatility episodes, and USDT depeg/basis regimes. A signal that only works during data-quality or stablecoin dislocation episodes should not be generalized as persistent alpha.
10. Failure action: if point-in-time OOS results do not show stable incremental information versus simple baselines after USD/USDT and cost controls, reject the hypothesis rather than adding filters.

## Crypto portability

direct

The source is explicitly Bitcoin/crypto and compares two crypto spot venues. Portability to other crypto assets is unproven because Coinbase/Binance liquidity, quote currencies, listing histories, and participant composition differ by asset. A BTC result must not automatically be generalized to altcoins.

## Limitations

- Complete trading lifecycle: **underspecified**.
- Source timeframe: **underspecified**.
- Economic interpretation of the premium as directional alpha: **unproven**.
- USD versus USDT quote-currency difference is a material confound.
- Historical exchange accessibility, latency, and candle synchronization can create false lead/lag.
- No independent reproduction has been performed.

## Implementation status

Research-only normalization. No implementation or Qlib full-backtest validation has been completed.

## Adoption boundary

This record is external research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, demonstrated profitability, or received Paper/Testnet/Live approval.

## Related Wiki records

- [[bitcoin-cross-venue-spot-premium]]
- [[crypto-market-fragmentation]]
- [[stablecoin-basis]]
- [[cross-venue-lead-lag]]

## Sources

- Tin2100, **CB BTCUSD Premium**, TradingView open-source indicator, published 2024-03-26, updated 2024-10-14, reviewed 2026-09-23: https://www.tradingview.com/script/Cp0aRqoy-CB-BTCUSD-Premium/
