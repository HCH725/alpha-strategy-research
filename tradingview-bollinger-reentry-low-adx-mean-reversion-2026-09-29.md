---
schema: strategy-research-record-v1
title: TradingView Bollinger Re-entry with Low-ADX Mean Reversion Filter
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2021-07-15
sources:
  - https://www.tradingview.com/script/b4Izc9Je-Bollinger-Bands-ADX-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bollinger Re-entry with Low-ADX Mean Reversion Filter

## Provenance

Primary source: public TradingView open-source strategy **Bollinger Bands + ADX Strategy** by **tweakerID**, published/updated 2021-07-15. Stable source URL: https://www.tradingview.com/script/b4Izc9Je-Bollinger-Bands-ADX-Strategy/ (canonical TradingView script ID: `b4Izc9Je`). Source reviewed 2026-09-29.

## Economic mechanism

### Source-reported

The author describes a Bollinger Bands strategy that buys when price crosses back over the lower band and sells when price crosses back down through the upper band. Trades are permitted only while ADX is below a configurable level, and all trades are exited when ADX rises above that level.

### Research interpretation

The falsifiable hypothesis is **range-regime mean reversion**: an excursion outside a volatility envelope followed by re-entry may identify short-horizon overextension, while low ADX is intended to restrict the signal to weak-trend/ranging regimes where mean reversion should be more plausible. The Bollinger re-entry is the primary signal; ADX is a regime filter and emergency regime-change exit. Whether ADX contributes incremental alpha must be tested separately rather than assumed.

## Signal

Source-supported normalized logic:

- Formation timing: evaluated on chart bars; the source page does not state the exact signal-to-fill timing.
- Long entry: price crosses over the lower Bollinger Band while ADX is below the configured threshold.
- Short entry: price crosses down through the upper Bollinger Band while ADX is below the configured threshold.
- Exit: close all trades when ADX rises above the configured threshold.
- Bollinger lookback, basis type, deviation multiplier, ADX length/smoothing, and the exact ADX threshold are not stated in the public description reviewed here: **underspecified**.
- Holding period, re-entry/pyramiding behavior, and reversal precedence are not stated: **data gap**.

No missing parameter or execution rule is inferred.

## Required data

- OHLC sufficient to reconstruct the source's Bollinger Bands and ADX once their exact parameters are resolved.
- Chart timeframe: **underspecified**.
- Instrument/universe: **underspecified**.
- Venue and market type: **underspecified**.
- Timestamp/candle-boundary convention: **underspecified**.
- Point-in-time requirement: indicators must use only information available by the decision timestamp; exact causal timing remains a **data gap** until source semantics are resolved.

## Execution assumptions

The source description does not specify market versus limit orders, same-bar versus next-bar fills, fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow/shorting, latency, or partial-fill behavior. All are **data gaps**. No zero-cost or frictionless assumption should be attributed to the source.

## Evidence

### Source-reported

No source-reported performance statistic is used in this record. The reviewed TradingView page states the strategy logic but does not provide a traceable quantitative performance claim in its description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself provides no documented negative-result study. Mechanistically, the setup is exposed to persistent directional moves: Bollinger re-entry can occur before an excursion has exhausted, and a low-ADX gate can lag a developing trend. These are research interpretations, not source-reported empirical findings.

None identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Resolve the exact source parameters before implementation; if they cannot be recovered unambiguously, do not silently substitute defaults.
2. Test the full Bollinger-re-entry + low-ADX rule against a Bollinger-re-entry-only baseline to measure incremental value from the ADX regime filter.
3. Compare against frequency-matched random entries within the same low-ADX regime to distinguish regime selection from entry timing.
4. Evaluate trending versus ranging and low- versus high-volatility regimes separately.
5. Run walk-forward/out-of-sample tests with realistic crypto fees, spread and slippage if ported to crypto.
6. Sweep nearby Bollinger and ADX parameters only as robustness analysis, not as a rescue optimization.
7. **Research-defined falsification threshold:** reject the hypothesis if net out-of-sample performance fails to beat both the Bollinger-only baseline and the frequency-matched low-ADX control after realistic costs, or if any apparent advantage depends on a narrow parameter island.

## Crypto portability

**unproven**

The signal can in principle be reconstructed from crypto OHLC data, but the reviewed source does not demonstrate crypto evidence. A crypto port must account for 24/7 candle boundaries, spot versus perpetual market structure, venue fragmentation, fees/slippage, perpetual funding, shorting mechanics, and liquidation/margin effects. Any chosen crypto universe, timeframe, exchange, or candle anchor would be **research-proposed**, not source-reported.

## Limitations

- Exact indicator parameters: **underspecified**.
- Exact signal-to-fill timing: **underspecified**.
- Instrument, venue, market type, and timeframe: **data gap**.
- Execution costs and fill model: **data gap**.
- Crypto efficacy: **unproven**.
- Not independently reproduced.

## Implementation status

Research-only normalization. No implementation in the research stack and no Qlib full backtest has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable or validated alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- TradingView — tweakerID, **Bollinger Bands + ADX Strategy**, published/updated 2021-07-15: https://www.tradingview.com/script/b4Izc9Je-Bollinger-Bands-ADX-Strategy/
