---
schema: strategy-research-record-v1
title: TradingView VN30 Keltner Breakout with SMA200 Slope Filter
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://www.tradingview.com/script/q8uGKGN6-PSOL-02-Keltner-Breakout/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView VN30 Keltner Breakout with SMA200 Slope Filter

## Provenance

Public TradingView open-source strategy “PSOL 02 Keltner Breakout” by Khanhtq26, published May 26 (year not exposed in the reviewed page), stable script ID `q8uGKGN6`. Source was reviewed as of 2026-09-29. The source states Pine Script v5 and identifies VN30F1M (Vietnamese stock-index futures) as its intended market.

## Economic mechanism
### Source-reported

The author describes a breakout strategy using an EMA/ATR Keltner Channel, with an optional SMA(200) slope filter to trade in the prevailing trend direction. A close outside the channel is treated as breakout confirmation.

### Research interpretation

Hypothesis: volatility-adjusted price-channel breaks may capture short-horizon trend continuation, while the SMA200 slope condition may suppress counter-trend breakouts. The Keltner break is the primary predictive signal; the SMA slope is a regime filter. Fixed stop/take-profit and session liquidation are risk/execution rules, not alpha.

This is a traditional-futures hypothesis. Its applicability to crypto is unproven.

## Signal

- Formation: signal is confirmed at bar close.
- Long: close crosses above the upper Keltner band; if the optional trend filter is enabled, SMA(200) must be rising.
- Short: close crosses below the lower Keltner band; if the optional trend filter is enabled, SMA(200) must be falling.
- Entry: source explicitly states execution at the open of the next bar after close confirmation.
- Keltner construction: EMA center with ATR-based bands; exact EMA length, ATR length and multiplier are underspecified in the reviewed description.
- Trend filter: SMA(200) slope; exact slope comparison/lookback is underspecified.
- Exit: fixed stop default 10 points; optional take-profit default 20 points; opposite fully qualified breakout reverses the position; positions are closed at session end.
- Session: default 09:00–14:30, intended to avoid ATO 08:45–09:00 and ATC 14:30–15:00. Timezone/exchange-calendar semantics are not explicitly stated in the reviewed description.
- Holding period: variable until stop, optional target, opposite reversal, or end-of-session close.
- Re-entry/pyramiding: underspecified.

## Required data

Source setting requires VN30F1M OHLC bars and enough history for EMA/ATR Keltner bands and SMA200. Exact chart timeframe is not specified in the reviewed description. Exchange calendar/session timestamps are required for the source's session logic. Venue, contract roll treatment, continuous-futures construction and missing-data policy are data gaps.

A crypto portability test would require venue-specific OHLCV and explicit 24/7 candle boundaries; volume is not part of the source-reported signal.

## Execution assumptions

Next-bar-open entry is source-reported. Stop and target are fixed point distances from entry, but order type, same-bar stop/target precedence, gap handling, spread, commission, slippage, impact, latency, partial fills, leverage and margin treatment are underspecified. End-of-session close and reversal fill semantics are also underspecified.

## Evidence
### Source-reported

The TradingView description states that the strategy is designed for VN30F1M intraday trading and provides the rule set above. No independently auditable performance statistic was relied upon for this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical result was identified in the reviewed description; absence is not evidence of no negative result. The source is market-specific, uses fixed point risk distances, and omits material transaction-cost assumptions.

## Falsification plan

1. Reconstruct the exact Keltner and SMA-slope definitions from an auditable specification before backtesting; fail closed if they cannot be resolved.
2. Test the primary Keltner breakout against a frequency-matched random-entry baseline and a simple price-momentum baseline.
3. Ablate the SMA200 slope filter to measure incremental contribution rather than assuming it adds alpha.
4. Use next-bar-open execution and stress realistic fees, spread and slippage; reject if net expectancy is not positive out of sample.
5. Separate the predictive signal from the 10/20-point stop/target overlay and test multiple volatility-normalized risk rules to detect dependence on one fixed-point setting.
6. Use walk-forward/out-of-sample periods spanning trend, range and volatility regimes; reject material instability or a result concentrated in one regime.
7. For any crypto adaptation, define the session anchor before testing and compare continuous 24/7 operation with the research-proposed sessionized variant. Do not tune the session after observing results.

## Crypto portability

adapted

The source is explicitly designed for Vietnamese index futures, not crypto. Keltner breakout and SMA slope are mechanically portable, but the source's session exclusions, fixed point stops, contract behavior and end-of-session liquidation are market-specific. Crypto trades 24/7 and introduces venue fragmentation, spot/perpetual differences, funding, mark/index pricing and different liquidity/candle-boundary behavior. Any crypto session definition is research-proposed rather than source-reported.

## Limitations

Exact Keltner parameters, SMA slope definition, chart timeframe, exchange-calendar semantics, re-entry/pyramiding behavior, cost model and several fill details are underspecified. No profitability claim is treated as verified. Not independently reproduced.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full-backtest validation has been completed.

## Adoption boundary

This record is research-only, not-implemented and not-approved. Presence in this repository does not imply Research Intake Review approval, Wiki Brain ingestion, production-candidate status, Qlib validation, survivor status, profitability, or Paper/Testnet/Live approval.

## Related Wiki records

None linked; no stable related Wiki record was verified during this GitHub-only Scout run.

## Sources

- TradingView — “PSOL 02 Keltner Breakout,” Khanhtq26: https://www.tradingview.com/script/q8uGKGN6-PSOL-02-Keltner-Breakout/ (reviewed 2026-09-29).
