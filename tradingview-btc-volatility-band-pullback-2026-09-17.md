---
schema: strategy-research-record-v1
title: BTC Volatility-Band Trend Pullback
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2021-07-05
sources:
  - https://www.tradingview.com/script/LDCIPS8i-BTC-Volatility-Band-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC Volatility-Band Trend Pullback

## Provenance

Public TradingView open-source strategy `BTC Volatility Band Strategy` by `gary_trades`, published 2021-07-05. Stable source URL: https://www.tradingview.com/script/LDCIPS8i-BTC-Volatility-Band-Strategy/ . Source reviewed 2026-09-17.

The source explicitly describes BTC/USDT use, daily and 3-hour examples, a trend moving-average filter, an inner/outer volatility-band pullback rule, and range-based stop/take-profit logic. This record normalizes the public description rather than redistributing the Pine source.

## Economic mechanism

### Source-reported

The author presents the system as a pullback strategy for highly volatile securities, with Bitcoin described as a natural fit. A moving-average trend filter determines directional regime. The strategy seeks pullbacks that reach an inner volatility band while rejecting moves that continue through a wider outer band as excessively large volatility excursions.

### Research interpretation

The falsifiable hypothesis is that, conditional on an established directional trend, a moderate volatility-normalized countertrend excursion is more likely to revert back toward the prevailing trend than continue, while a sufficiently extreme excursion represents a materially different state and should be excluded rather than faded.

Component roles:

- Regime: price relative to a configurable moving-average trend filter.
- Primary signal: pullback into the inner volatility band.
- Rejection filter: excursion through the outer volatility band suppresses the entry.
- Risk / exit: take-profit and stop-loss levels based on a multiple of the recent seven-candle trading range.

The inner-versus-outer excursion distinction is the principal research feature; the moving-average filter and risk rules should be ablated separately before attributing alpha to them.

## Signal

Source-described normalized logic:

- The volatility construction compares closes of the previous two candles and uses that price change to construct a moving-average volatility reference.
- Inner and outer bands are placed at configurable standard-deviation distances around that reference; the source describes defaults of 1 standard deviation for the inner band and 2 for the outer band.
- Long regime: price is above the configured moving-average trend filter.
- Long setup: in the long regime, a pullback spikes/touches the lower inner deviation band; if the move continues through the lower outer band, the buy is suppressed.
- Short regime: price is below the configured moving-average trend filter.
- Short setup: price spikes/touches the upper inner band while in the short regime; the symmetric outer-band rejection is a plausible interpretation but is not stated with the same explicit detail as the long case and therefore remains underspecified.
- The author reports that a volatility-tracking period of 3 worked well in the daily BTC example and 5 in the 3-hour example. These are source-reported examples, not independently validated parameters.
- Take-profit and stop-loss levels are described as multiples of the trading range over the previous seven candles.

Underspecified in the public description: the exact mathematical transformation of the two prior closes before smoothing, the trend-filter MA type and default period, exact crossing/touch semantics, confirmed-bar versus intrabar formation timing, exact short-side outer-band rejection rule, take-profit/stop-loss multipliers, re-entry/cooldown behavior, and order timing.

Research-proposed operationalization for later testing only: reconstruct the published Pine logic independently from the public source before parameter expansion, then compare (a) inner-band pullback only, (b) trend-filtered inner-band pullback, and (c) trend-filtered inner-band pullback with outer-band rejection. Do not treat this proposal as source-reported logic.

## Required data

- Instrument/universe: source specifically discusses BTC/USDT and recommends liquid coins for execution.
- Venue: source states an attached result used one BTCUSDT contract on Binance; portability to other venues is unproven.
- Market type: the public description does not unambiguously specify spot versus derivative contract semantics.
- Timeframes: daily and 3-hour are explicitly discussed; the author says they had not tested below 1 hour at publication.
- Fields: timestamped OHLC data is required; volume is not described as part of the signal.
- Point-in-time requirement: all rolling means, deviations, prior-close changes, trend filter, and seven-candle range must use only information available at the signal timestamp.
- Missing-data handling and candle-boundary convention are not specified.

## Execution assumptions

The source recommends liquid coins because positions may need to be entered and exited quickly. It does not sufficiently specify signal-to-order timing, market versus limit orders, fill model, fees, spread, slippage, impact/capacity, leverage/margin, funding, borrow/short mechanics, latency, partial fills, or failed orders.

Any later reproduction must model these explicitly rather than inheriting TradingView defaults silently.

## Evidence

### Source-reported

The author states that the strategy is designed for high-volatility securities, specifically discusses BTC/USDT, reports favorable personal observations for daily and 3-hour settings, and says an attached result trades one BTCUSDT contract on Binance. No precise performance statistic is relied upon in this record because the public text reviewed here does not provide a traceable numeric performance result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author states that they had not tested the strategy below the 1-hour timeframe at publication and recommends high-liquidity coins for fast entry/exit. No independent contrary result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

Test BTC/USDT first on point-in-time-clean daily and 3-hour data, preserving the source-described parameter examples before broad search. Require chronological out-of-sample evaluation across bull, bear, high-volatility, and low-volatility regimes.

Key controls and ablations:

1. Compare against trend-only and unconditional pullback baselines.
2. Remove the outer-band rejection filter to test whether excluding extreme excursions adds information.
3. Remove the trend filter to test whether the effect is genuinely conditional on trend.
4. Compare inner-band distances and volatility-tracking windows only after the source logic is reconstructed without ambiguity.
5. Apply realistic fees, spread and slippage; reject the hypothesis if the apparent edge is cost-fragile.
6. Test whether performance is concentrated in one historical BTC regime or one venue/candle convention.
7. Treat failure to outperform simple trend-pullback controls out of sample as evidence against the claimed mechanism.

## Crypto portability

direct

The source itself explicitly targets Bitcoin/BTCUSDT and discusses Binance, so the mechanism is directly crypto-originated. Portability beyond BTC remains unproven. Material risks include 24/7 candle-boundary choices, venue fragmentation, spot-versus-perpetual differences, funding for perpetuals, liquidity variation, and exchange-specific execution.

## Limitations

- Exact volatility-band formula is underspecified in the public prose reviewed here.
- Trend-filter MA type/default period is underspecified.
- Exact order and bar-confirmation timing is underspecified.
- Exit/stop multipliers are underspecified.
- Market type is ambiguous.
- Source-reported favorable observations are not independent evidence.
- Not independently reproduced.

## Implementation status

No implementation in our research stack has been completed. No PyBroker, Qlib, Nautilus, paper, testnet, or live verification is claimed.

## Adoption boundary

Research material only. Presence in this repository does not mean the strategy is profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted here.

## Sources

- TradingView — `BTC Volatility Band Strategy`, `gary_trades`, published 2021-07-05: https://www.tradingview.com/script/LDCIPS8i-BTC-Volatility-Band-Strategy/
