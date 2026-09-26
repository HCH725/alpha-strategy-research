---
schema: strategy-research-record-v1
title: TradingView Rolling VWAP Standard-Deviation Mean Reversion
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - https://www.tradingview.com/script/oZcWZsvU-RVWAP-Mean-Reversion-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Rolling VWAP Standard-Deviation Mean Reversion

## Provenance

Public TradingView open-source strategy `RVWAP Mean Reversion Strategy` by `vvedding`. Stable source URL: https://www.tradingview.com/script/oZcWZsvU-RVWAP-Mean-Reversion-Strategy/ . The public page displays publication date “Mar 5”; the year is not stated in the reviewed page text, so no year is inferred. Source reviewed 2026-09-26.

Canonical TradingView source identity: `oZcWZsvU`.

Before writing, current GitHub `main` was searched for the canonical ID, exact stable URL, title, and normalized rolling-VWAP/standard-deviation mean-reversion concept. No same-source record was found. Nearby records include RSI/Bollinger mean reversion, adaptive dominant-cycle VWAP extremes, and an RSI-filtered short/long-period VWAP strategy; this hypothesis is materially distinct because its primary state variable is deviation from a rolling volume-weighted mean and its trigger requires re-entry through a rolling VWAP standard-deviation band.

## Economic mechanism

### Source-reported

The author frames rolling VWAP as a volume-weighted mean and proposes fading excursions outside its standard-deviation bands after price crosses back through the breached band. The page states that rapid declines or rises can create larger drawdowns.

### Research interpretation

The falsifiable hypothesis is that an excursion beyond a rolling volume-weighted standard-deviation envelope followed by a close back inside that envelope contains short-horizon reversal information. The excursion represents temporary price displacement from a volume-weighted reference; the re-entry condition is intended to avoid entering solely because price is extreme.

This interpretation does not establish profitability. A useful ablation is whether the re-entry trigger adds information beyond simple distance from rolling VWAP, and whether volume weighting adds information beyond an ordinary rolling mean with volatility bands.

## Signal

Source-reported normalized logic:

- Reference: TradingView Rolling VWAP with standard-deviation bands.
- Long setup: price dips below the lower RVWAP standard-deviation band.
- Long entry: price subsequently crosses back above the lower band and closes above it.
- Short setup: price rises above the upper RVWAP standard-deviation band.
- Short entry: price subsequently crosses back below the upper band and closes below it.
- Long exit: exit after price crosses the RVWAP.
- Short exit: exit after price crosses the RVWAP.
- Direction can be configured as long-only, short-only, or both.
- Rolling period and the first standard-deviation setting are configurable.
- A user-defined backtest date range is supported.

Underspecified in the public page text: exact default rolling period, exact standard-deviation multiplier/default, RVWAP implementation details, whether an excursion and re-entry may occur on the same bar, precise cross semantics, order timing/fill price, re-entry behavior, pyramiding, and position sizing. No missing value is inferred.

## Required data

- OHLCV bars sufficient to calculate the rolling VWAP and its standard-deviation bands.
- Instrument/universe: not constrained by the source page.
- Venue/market type: not specified.
- Timeframe: not specified.
- Timestamp/timezone/candle-boundary convention: data gap.
- Point-in-time requirement: all rolling inputs must use only information available by the signal timestamp; exact TradingView implementation should be audited before replication.
- Missing-volume and missing-bar treatment: data gap.

## Execution assumptions

The source describes entries and exits using crosses/closes but does not specify the executable order timestamp or fill model.

Data gaps: same-close versus next-bar execution, market versus limit order, spread, commission, slippage, market impact, capacity, leverage/margin, funding, borrow/short availability, latency, partial fills, and failed orders.

Any concrete convention introduced for replication would be `research-proposed`.

## Evidence

### Source-reported

The author states that high win rates are commonly observed after tuning the rolling period and first standard-deviation setting, and says Sharpe and Sortino can indicate an edge depending on configuration. No exact performance statistic, sample, instrument, timeframe, cost model, or out-of-sample result is stated in the reviewed public page text, so no numerical performance claim is recorded.

The author also warns that fast directional moves may produce larger drawdowns.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself flags vulnerability to rapid directional moves. No independently verified negative study was identified in the reviewed source; absence is not evidence of no negative result.

The page encourages parameter tuning, creating an explicit overfitting risk when rolling length and band width are selected on the same sample used for evaluation.

## Falsification plan

1. Freeze a small parameter grid before evaluation and test chronologically out of sample.
2. Compare against three controls: simple RVWAP-distance entry without re-entry confirmation, ordinary rolling-mean standard-deviation bands, and a no-signal baseline.
3. Ablate volume weighting and the band re-entry requirement separately.
4. Stress realistic fees, spread, slippage, and one-bar execution delay.
5. Split results by trend/volatility regime, especially fast directional markets highlighted by the source.
6. Require stability across multiple instruments and non-overlapping periods rather than selecting the best rolling period/band width after observing results.
7. Any numerical acceptance or failure cutoff chosen during later testing is a `research-defined falsification threshold`, not source-reported.

## Crypto portability

`unproven`.

The mechanism can be calculated from crypto OHLCV, but the reviewed source does not provide crypto-specific empirical evidence. A crypto adaptation must account for 24/7 candle boundaries, venue-specific volume, spot versus perpetual volume, fragmented liquidity, funding, mark/index prices, and continuous short availability. Those choices would be `research-proposed` unless independently sourced.

## Limitations

- `underspecified`: rolling VWAP implementation and default rolling period.
- `underspecified`: standard-deviation calculation and default multiplier.
- `underspecified`: exact cross/close timing and order-fill semantics.
- `data gap`: source instrument, venue, timeframe, cost model, sizing, and re-entry/pyramiding behavior.
- `unproven`: crypto portability.
- `not independently reproduced`.
- Parameter tuning described by the source can create selection bias.

## Implementation status

Research normalization only. No implementation in the research stack, no Qlib full backtest, and no independent reproduction was performed in this Scout cycle.

## Adoption boundary

This record is research-only, not implemented, and not approved. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable Hermes Wiki Brain page was verified during this GitHub-only run; no Wiki link is fabricated.

## Sources

- TradingView, `RVWAP Mean Reversion Strategy`, vvedding: https://www.tradingview.com/script/oZcWZsvU-RVWAP-Mean-Reversion-Strategy/ (public open-source strategy page; reviewed 2026-09-26).
