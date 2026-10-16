---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse BB + Aroon Lower-Band Crossunder with Aroon-Up Gate"
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20%2B%20Aroon.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse BB + Aroon Lower-Band Crossunder with Aroon-Up Gate

## Provenance

- Source repository: https://github.com/Alorse/pinescript-strategies
- Immutable source commit: 8fb3837ddcd137f1450c3e82d654ff3df24d54d5
- Exact source path: strategies/mean-reversion/BB + Aroon.pine
- Primary source file: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20%2B%20Aroon.pine
- The source signal is preserved. Research execution derivatives are clearly disclosed below; no change is silently represented as lossless.

## Economic mechanism

Trend-recency-gated lower Bollinger band breakdown: a new long is entered on a strict cross BELOW the lower band, provided that Aroon-Up indicates a recently achieved high. This is not a lower-band rebound or a BB upper-band breakout.

## Signal — exact source rules

Pine v5 strategy, pyramiding=0, default_qty_type=percent_of_equity, default_qty_value=100, source commission 0.1% per side. Source inputs: lengthBB=20, src=close, BB multiplier=2.0, lengthAr=288, Confirmation=90, Stop=70.

- basis = SMA(close,20); deviation = 2.0 * stdev(close,20); upper/lower = basis plus/minus deviation.
- AroonUP = 100 * (highestbars(high, lengthAr+1) + lengthAr) / lengthAr. Pine highestbars produces a nonpositive offset of the most recent highest high in the 289-bar window.
- Bullish = crossunder(close, lower): previous close >= previous lower AND current close < current lower.
- Bearish = crossunder(close, upper): previous close >= previous upper AND current close < current upper.
- Long entry = Bullish AND AroonUP > 90. Pine call: strategy.entry Long.
- Long exit = Bearish OR AroonUP < 70. Pine call: strategy.close Long.
- Short disabled by source construction. The calculated AroonDown is unused in order conditions. No stop loss, fixed take profit, trailing, time exit, cooldown, safety order or scale-in. A single same-side position maximum; after flat a subsequent qualifying signal can re-enter.
- Potential same-bar coexistence of entry and exit must follow actual Pine order-call semantics (source lists entry before close); reviewer must not silently assume an execution priority.

## Required data and causality

Single-symbol OHLC, with close for bands and crossings and high for Aroon. The longest rolling window spans 289 completed bars; one preceding computed band value is needed for crossover, so hold warmup through 290 completed bars. Source has no request.security, lookahead or future-bar selection. Values are available only once the signal candle has completed.

## Execution assumptions — disclosed research derivative

Original Pine does not specify process_orders_on_close, so the TradingView default market fill is next-bar-open after the completed-bar decision. For the current independently verified closed-bar/same-bar-close Hummingbot research lane, preserve every source formula, direction, threshold and signal event, but explicitly switch fill timing to same-bar-close. THIS IS A DECLARED RESEARCH EXECUTION DERIVATIVE; it is not a lossless source-execution clone and may change fill prices/PnL. Do not assert compatibility until the existing reviewer verifies the actual controller/executor, time availability, market order fill convention, Binance USDT-M isolated margin and cost assumptions against pinned package 20260920, VERSION dev-2.17.0.

Source default sizing 100% equity and commission 0.1% are provenance only. House leverage 3x/5x, 7-symbol x 3-timeframe coverage and BO/SO DCA belong solely to downstream declared research experiments; DCA can change event timing and is not source-native.

## Deduplication

No direct Alorse source URL found in current main. Closest main families: Aroon oscillator with midline/rail exits, and DMI-gated Bollinger band rule. Neither expresses the exact conjunction of close crossunder below Bollinger lower and Aroon-Up > 90 with this asymmetric exit pair. Independent reviewer must verify open research PRs and current head again.

## Evidence

Primary Pine source inspected completely at pinned commit. No independent Hummingbot, Qlib, trade-by-trade or profitability evidence is claimed. The author's BTC 1d dataset is not a required strategy input.

## Falsification plan

On each completed bar after warmup compare computed signals to strictly lower-band crossunder AND AroonUP > 90; exits are upper-band crossunder OR AroonUP < 70. Verify no shorts, no repeated same-direction orders while positioned and that same-bar overlapping conditions are resolved by the supported execution lane. Check next-open vs derived same-close differences without confusing these with formula divergence.

## Crypto portability and limitations

Signal requires one liquid candle series, not a fixed symbol or timeframe. Its dip entry is exposed to falling-knife risk and no coded protective stop; transport to Binance perpetual is an explicit experiment, not a claim of source economics.

## Implementation status

not-implemented. This is an admission record only; no actual Hummingbot or Qlib execution is claimed.

## Adoption boundary

Research-only, not approved for Testnet/Mainnet. Proposed PASS is subject to independent reviewer validation of all existing six HB_READY gates and exact-head merge; it is not self-certified.

## Sources

- Primary source: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/mean-reversion/BB%20%2B%20Aroon.pine
- Independent review contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
