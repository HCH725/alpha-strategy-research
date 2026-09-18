---
schema: strategy-research-record-v1
title: ETH Bollinger Midline Two-Candle MTF Pullback
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
  - https://www.tradingview.com/script/nUmHknsY/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ETH Bollinger Midline Two-Candle MTF Pullback

## Provenance

- Source: TradingView public open-source strategy page, `ETH-BB + 2 Candles`.
- Author/page identity: `sgwxrbtn`.
- Stable URL: https://www.tradingview.com/script/nUmHknsY/
- Publication display on the reviewed page: `Feb 25`; the year is not explicitly shown in the reviewed public page text.
- Source reviewed as of: 2026-09-18.
- The public description was used to normalize the hypothesis; no Pine source code is reproduced here.

## Economic mechanism

### Source-reported

The source describes a 5-minute ETHUSDT strategy that trades only in the direction of a higher-timeframe trend. A 30-minute EMA provides the directional filter. Entry requires a retest of the Bollinger Band midline followed by two consecutive candles in the intended direction. An ATR-based dynamic trailing stop manages exits.

### Research interpretation

The falsifiable hypothesis is that a short-horizon pullback to a local volatility-adjusted mean (the Bollinger midline) has positive continuation expectancy when the higher-timeframe EMA trend agrees and immediate two-candle price action confirms resumption of that trend.

Component roles:

- Regime: 30-minute EMA trend filter.
- Primary setup: 5-minute price retest of the Bollinger Band midline.
- Confirmation: two consecutive bullish candles for long entries or bearish candles for short entries.
- Risk / exit: ATR-based dynamic trailing stop.

The economic interpretation is trend persistence after a controlled pullback; whether the Bollinger retest or two-candle confirmation adds incremental alpha beyond the higher-timeframe trend filter is unproven and requires ablation.

## Signal

Source-reported logic:

- Instrument: ETHUSDT.
- Trading timeframe: 5 minutes.
- Higher-timeframe trend input: 30 minutes.
- Long regime: 30-minute EMA indicates an uptrend.
- Short regime: 30-minute EMA indicates a downtrend.
- Entry setup: price retests the Bollinger Band midline.
- Long confirmation: two consecutive bullish candles.
- Short confirmation: two consecutive bearish candles.
- Exit / risk: dynamic ATR-based trailing exit.
- Direction modes: long-only, short-only, or long/short are supported.

Underspecified in the reviewed public description:

- EMA length and exact definition of `uptrend` / `downtrend`;
- Bollinger lookback, deviation multiplier, price source, and exact mathematical definition/tolerance of a `retest`;
- whether the two confirming candles must occur immediately after the retest and whether their bodies, closes, or full ranges define bullish/bearish status;
- ATR lookback, multiplier, trailing-update semantics, and activation timing;
- re-entry, pyramiding, and position-sizing rules;
- exact signal-to-order timing.

No missing operational detail is filled by assumption in this record.

## Required data

- ETHUSDT OHLCV bars at 5-minute resolution.
- ETHUSDT 30-minute OHLCV or point-in-time-safe aggregation from lower-frequency bars sufficient to calculate the higher-timeframe EMA.
- High, low, and close fields sufficient for Bollinger and ATR calculations; open is also required to classify bullish/bearish candles under the usual candle convention, but the source does not explicitly state its candle-classification formula.
- Point-in-time handling is material: the 30-minute trend state must not use information from an incomplete future portion of the higher-timeframe bar.
- Venue is not fixed by the source; the page states compatibility with Gate.io, Bybit, and other exchanges supporting trailing stops.

## Execution assumptions

The source states that an ATR-based dynamic trailing stop is used and mentions exchange compatibility, but the reviewed public description does not specify:

- same-bar versus next-bar entry;
- market versus limit execution;
- fill model;
- fees, spread, slippage, or impact;
- funding for perpetual contracts;
- leverage / margin;
- latency, partial fills, or failed orders;
- exact trailing-stop order semantics.

These remain underspecified. Any later implementation choice for these fields must be labeled `research-proposed` unless independently recovered from the primary source.

## Evidence

### Source-reported

The reviewed TradingView description explains the rule structure and intended ETHUSDT 5-minute / 30-minute configuration but does not provide a traceable quantitative performance statistic in the reviewed text. No profitability, Sharpe, drawdown, win-rate, or other performance figure is therefore recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. The rule is structurally exposed to whipsaw in sideways regimes, higher-timeframe/lower-timeframe synchronization errors, and execution sensitivity from a 5-minute horizon; these are research risks rather than source-reported empirical failures.

## Falsification plan

A future test should compare the complete rule against at least these ablations on point-in-time-safe ETH data:

1. 30-minute EMA trend filter alone;
2. trend filter + Bollinger-midline retest;
3. trend filter + two-candle confirmation without the Bollinger retest;
4. complete trend + retest + two-candle rule.

Test multiple market regimes and include realistic fees, spread/slippage, and perpetual funding where applicable. The hypothesis is materially weakened if the full rule fails to improve out-of-sample risk-adjusted or cost-adjusted performance over simpler trend-only / partial-component baselines, or if results disappear under causal higher-timeframe alignment and plausible execution costs. Exact numerical acceptance thresholds are intentionally not invented here; any later threshold is a `research-defined falsification threshold`.

## Crypto portability

direct

The source itself targets ETHUSDT. Portability across venues remains unproven because 5-minute candle boundaries, venue-specific prices/liquidity, spread, fees, and perpetual funding can change realized results. Higher-timeframe bar alignment must be causal in a 24/7 market.

## Limitations

- Signal is partially underspecified at the parameter and event-sequencing level.
- Exact source code was not reproduced in this record.
- Not independently reproduced.
- No source-reported performance statistic was retained because none was traceable in the reviewed description.
- The incremental contribution of each component is unproven.
- Five-minute execution may be materially sensitive to costs and venue microstructure.

## Implementation status

Not implemented in our research stack. No backtest, Qlib research run, paper trading, testnet, or live verification was performed by this Scout.

## Adoption boundary

Research-only. Presence in this repository does not establish profitability, validated alpha, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

None linked; no stable related Hermes Wiki Brain record was established during this GitHub-only Scout cycle.

## Sources

- TradingView — `ETH-BB + 2 Candles`, author `sgwxrbtn`: https://www.tradingview.com/script/nUmHknsY/ (reviewed 2026-09-18).
