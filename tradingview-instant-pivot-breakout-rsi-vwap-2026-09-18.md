---
schema: strategy-research-record-v1
title: TradingView Instant Pivot Breakout with RSI and VWAP
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/4juJumUH-Instant-Breakout-Strategy-with-RSI-VWAP/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Instant Pivot Breakout with RSI and VWAP

## Provenance

- Source: TradingView open-source strategy, **Instant Breakout Strategy with RSI & VWAP**, author **thetraderlodge**.
- Stable public URL: https://www.tradingview.com/script/4juJumUH-Instant-Breakout-Strategy-with-RSI-VWAP/
- Published: 2025-08-22.
- Reviewed/as-of: 2026-09-18.
- The public description exposes the strategy logic and parameter defaults sufficiently for a normalized research record; no Pine source code is reproduced here.

## Economic mechanism

### Source-reported

The source describes a pivot breakout system intended for very short horizons. Price crossing the latest confirmed pivot high or low supplies the breakout event. Optional filters require volume expansion, same-bar directional momentum, RSI alignment, and price location relative to VWAP before accepting the breakout. ATR defines take-profit and stop-loss distances.

### Research interpretation

The falsifiable hypothesis is that a break of a recently confirmed local pivot is more likely to persist when several independent state variables agree with the direction of the break: abnormal volume indicates participation, same-bar return indicates impulse, RSI indicates short-horizon momentum, and VWAP location indicates whether price is trading on the directional side of an intraday reference price.

Component roles:

- Primary signal: crossover above latest confirmed pivot high / crossunder below latest confirmed pivot low.
- Participation confirmation: current volume versus 20-period average.
- Momentum confirmation: directional percentage move from current bar open.
- Momentum-state confirmation: 3-period RSI relative to 50.
- Price-location confirmation: price relative to VWAP.
- Risk / exit: 14-period ATR stop-loss and take-profit distances.

The source allows all filters to be disabled, so the unfiltered pivot breakout and the filtered composite should be treated as separate experimental configurations during later testing rather than assuming the filters add alpha.

## Signal

Source-reported rules:

- Intended timeframe: 1-second; the source states it is optimized for and best used on that timeframe.
- Pivot detection: `ta.pivothigh` / `ta.pivotlow` with left/right pivot bars defaulting to 3; the latest confirmed pivot high is resistance and latest confirmed pivot low is support.
- Long breakout: price crosses above the latest pivot high.
- Short breakout: price crosses below the latest pivot low.
- Filters are optional and default off.
- With filters enabled, long confirmation requires:
  - volume greater than 1.5 times the 20-period average volume;
  - price increase greater than 1% from the current bar open;
  - 3-period RSI above 50;
  - price above VWAP.
- With filters enabled, short confirmation requires the directional counterparts:
  - volume surge under the same threshold definition;
  - price decrease greater than 1% from the current bar open;
  - 3-period RSI below 50;
  - price below VWAP.
- Long entry closes any short; short entry closes any long.
- ATR period: 14.
- Take-profit distance: 9.0 ATR from the entry reference described by the source as `close ± atr * 9.0`.
- Stop-loss distance: 1.0 ATR from the entry reference described by the source as `close ± atr * 1.0`.

Underspecified:

- Exact order-fill timing relative to the crossover bar is not stated in the public prose.
- Exact VWAP session/reset semantics are not stated.
- Pyramiding/re-entry behavior beyond opposing-position closure is not stated.
- Position sizing is not stated.

## Required data

- Bar OHLCV at the selected timeframe; the source specifically targets 1-second bars.
- Sufficient bar history for pivot confirmation, 20-period volume average, 3-period RSI, 14-period ATR, and VWAP.
- A point-in-time implementation must respect right-side pivot confirmation: a pivot cannot be treated as known before the required right bars have elapsed.
- VWAP requires a defined session/reset convention; this is a data/implementation gap in the public description.
- The source is asset-agnostic in the reviewed description; venue and market type are not specified.

## Execution assumptions

Source-reported:

- Entries occur on bullish/bearish breakout conditions and close an existing position in the opposite direction.
- ATR-based TP and SL are attached conceptually to each entry.

Underspecified:

- Market versus stop/limit order type.
- Same-bar versus next-bar fill semantics.
- Fees, spread, slippage, latency, queue position, impact and partial fills.
- Leverage, margin and short-borrow assumptions.

These omissions are especially material on the stated 1-second horizon. No execution assumptions are silently supplied here.

## Evidence

### Source-reported

The source states that the strategy is optimized for the 1-second timeframe and recommends backtesting before live use. The reviewed public description does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or other performance statistic, so none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly notes that disabling filters produces more signals with less confirmation. No independent negative evidence was reviewed in this Scout cycle. The 1-second target horizon creates an obvious execution-sensitivity risk because spread, fees, latency and slippage are omitted from the public description; this is a research limitation, not a reproduced failure result.

## Falsification plan

- Reconstruct the pivot logic point-in-time, including the 3-right-bar confirmation delay, and reject any implementation that leaks future pivot information.
- Compare unfiltered pivot breakout against the fully filtered configuration and ablate volume, impulse, RSI and VWAP filters individually.
- Test whether net performance survives realistic fees, spread, latency and slippage appropriate to 1-second data.
- Test neighboring pivot lengths and thresholds rather than relying only on the published defaults.
- Separate liquid crypto spot and perpetual samples and include funding where perpetuals are used.
- Require out-of-sample performance across distinct volatility/liquidity regimes.
- Research-defined falsification threshold: reject the alpha hypothesis if the filtered rule does not improve out-of-sample risk-adjusted net performance or false-breakout behavior versus the plain point-in-time pivot breakout after realistic costs.

## Crypto portability

**unproven**

The rule uses generic OHLCV, RSI, ATR and VWAP inputs and is mechanically portable to liquid crypto markets, but the reviewed source does not establish crypto-specific empirical validity. Crypto testing must define venue-specific volume, 24/7 VWAP reset semantics, spot-versus-perpetual market type, funding for perpetuals, and realistic microstructure costs. These issues are particularly important at 1-second resolution.

## Limitations

- Not independently reproduced.
- Crypto validity is unproven.
- Exact fill timing and order type are underspecified.
- VWAP reset/session semantics are underspecified.
- Position sizing and re-entry/pyramiding behavior are underspecified.
- Source provides no traceable performance statistics in the reviewed public description.
- Pivot implementations are vulnerable to look-ahead error if right-side confirmation is mishandled.
- 1-second trading is highly sensitive to execution costs and latency omitted by the source.

## Implementation status

Not implemented in our research stack. No internal backtest, paper, testnet, or live verification has been performed.

## Adoption boundary

Research-only. Presence in this repository does not mean profitable, validated alpha, approved implementation, or approval for paper, testnet, or live trading.

## Related Wiki records

None linked; no Wiki record was accessed or fabricated in this GitHub-only Scout cycle.

## Sources

- thetraderlodge, **Instant Breakout Strategy with RSI & VWAP**, TradingView, published 2025-08-22, reviewed 2026-09-18: https://www.tradingview.com/script/4juJumUH-Instant-Breakout-Strategy-with-RSI-VWAP/
