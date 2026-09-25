---
schema: strategy-research-record-v1
title: TradingView Relative Volume + Consolidation Price-Action Long Strategy
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-25
sources:
  - https://www.tradingview.com/script/HNmT0VUi-KL-Relative-Volume-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Relative Volume + Consolidation Price-Action Long Strategy

## Provenance

Public TradingView open-source strategy page: **[KL] Relative Volume Strategy**, author **DojiEmoji**.

Stable source URL: https://www.tradingview.com/script/HNmT0VUi-KL-Relative-Volume-Strategy/

The public page shows an original publication date of 2021-07-06 and later release-note updates through 2021-07-18. This record uses the public page as available on 2026-09-25.

No Pine source code was copied into this record. The page-level strategy description and release notes were normalized into research form.

## Economic mechanism

### Source-reported

The author describes a long-only strategy that requires:

- relatively high volume;
- a period of price consolidation;
- price-action support/confirmation after later release-note refinements.

The source measures consolidation by comparing twice the standard deviation of closing prices over a 20-candle lookback with twice ATR over a user-configurable ATR length. The source treats volatility as relatively low when the standard-deviation measure is below the ATR measure.

The source states that positions are exited either when a stop-loss limit is reached or when price action becomes bearish. Release notes mention refinements to bearish-engulfing logic and entry-side price-action conditions.

### Research interpretation

The falsifiable hypothesis is that **unusually strong participation during a compressed price state, followed by supportive price action, contains incremental upside information beyond relative volume, compression, or candle confirmation used separately**.

Possible mechanism:

1. relative volume acts as a participation/attention proxy;
2. low close-to-close dispersion relative to ATR identifies compression rather than already-expanded directional movement;
3. supportive price action attempts to distinguish accumulation/continuation from high-volume rejection.

This interpretation is research-only. The source does not establish that the conjunction produces persistent alpha out of sample.

## Signal

Source-supported logic:

- Direction: long only on the reviewed public description.
- Consolidation lookback: 20 candles for the close-price standard deviation.
- Consolidation condition: approximately `2 × stdev(close, 20) < 2 × ATR(user-defined length)`.
- Participation condition: current volume must be "relatively high"; the exact normalization formula and threshold are not specified in the reviewed public description.
- Entry confirmation: later release notes state that the current candlestick should provide strong support, or at minimum not be weak, according to the strategy's price-action indicators.
- Exit: stop-loss condition or bearish price-action condition.
- Bearish-engulfing logic is mentioned in release notes, but the complete bearish-exit rule is not fully specified in the reviewed page text.

Underspecified:

- exact relative-volume formula and threshold;
- ATR lookback default;
- exact supportive-candle rule;
- exact bearish price-action rule;
- stop-loss distance and whether it is fixed, volatility-scaled, or otherwise adaptive;
- signal formation timestamp;
- same-bar versus next-bar entry;
- holding period;
- re-entry rule;
- position sizing;
- pyramiding;
- exact timeframe and instrument universe.

Any concrete implementation choices beyond the source-supported items above are **research-proposed** and must not be attributed to the original author.

## Required data

Minimum source-compatible inputs:

- OHLCV bars;
- closing prices for the 20-bar standard-deviation calculation;
- high/low/close data for ATR;
- volume for relative-volume normalization;
- timestamps sufficient to reproduce bar boundaries.

For crypto research, point-in-time venue-specific OHLCV is required. Because exchange volume is fragmented, a venue definition or aggregation policy would also be required before testing portability.

## Execution assumptions

The public page does not fully specify:

- market versus limit order;
- same-bar versus next-bar execution;
- intrabar stop processing;
- fill priority when entry/exit conditions coexist;
- fees;
- bid/ask spread;
- slippage;
- market impact;
- partial fills;
- capacity;
- borrow/shorting, which is not relevant to the reviewed long-only rule but would matter for any research-proposed extension;
- leverage or margin.

A leakage-safe implementation should form signals only from information available at the chosen decision timestamp and apply conservative execution assumptions.

## Evidence

### Source-reported

The reviewed source reports the strategy logic and subsequent rule refinements. No source-reported Sharpe, CAGR, drawdown, profit factor, or other performance statistic from this exact page is carried into this record.

The source is publicly accessible and marked open-source by TradingView.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The public page text does not fully specify the relative-volume formula or threshold.
- ATR length is configurable but the reviewed page does not establish a single canonical default for this strategy.
- The exact price-action confirmation and bearish-exit state machine are not fully reconstructable from the public prose alone.
- Stop-loss calibration is not specified in the reviewed description.
- No independently verified out-of-sample evidence was found during this Scout cycle.
- Parameter flexibility creates selection/overfitting risk.
- The Pine implementation was not independently audited during this run.

## Falsification plan

All items below are **research-proposed**.

1. **Source-compatible reconstruction gate**
   - Do not backtest until the relative-volume calculation, entry price-action condition, bearish exit, stop-loss rule, and execution timing can be reconstructed without guessing.
   - If exact source-compatible reconstruction is not possible, keep the record research-only and do not manufacture a proxy as if it were the source strategy.

2. **Component ablation**
   - relative-volume condition only;
   - compression condition only;
   - price-action confirmation only;
   - relative volume + compression;
   - relative volume + price action;
   - compression + price action;
   - full conjunction.

3. **Simple baselines**
   - ordinary relative-volume breakout/continuation;
   - Bollinger-bandwidth or rolling-standard-deviation compression alone;
   - ATR-normalized compression alone;
   - simple bullish-candle confirmation;
   - price momentum without the composite filters.

4. **Parameter robustness**
   - neighborhood tests around the 20-bar standard-deviation lookback;
   - multiple ATR lengths;
   - multiple relative-volume thresholds once the source-compatible formula is known;
   - avoid selecting one best parameter combination from the full sample.

5. **Out-of-sample requirement**
   - walk-forward evaluation across multiple instruments and market regimes;
   - separate trending, ranging, high-volatility, and low-volatility periods;
   - evaluate net of fees, spread, and slippage.

6. **Failure criterion**
   - Reject the composite-alpha interpretation if the full rule does not provide stable out-of-sample incremental value over the best simpler component/baseline after realistic costs.
   - If most performance is explained by one component, preserve that simpler component rather than the full stack.

## Crypto portability

**adapted**

The mechanism is portable in principle to crypto because OHLCV, ATR, dispersion, and relative volume are available. Important crypto-specific risks:

- 24/7 market structure changes the interpretation of consolidation and candle boundaries;
- venue volume is fragmented and exchange-specific;
- spot and perpetual markets can show materially different volume behavior;
- perpetual funding, mark/index prices, and liquidation dynamics are absent from the source rule;
- low-liquidity altcoins can create unstable relative-volume spikes and unrealistic fills.

Any crypto implementation would therefore be a ported hypothesis, not source-demonstrated crypto evidence.

## Limitations

- underspecified relative-volume rule;
- underspecified ATR default;
- underspecified price-action confirmation;
- underspecified bearish-exit logic;
- underspecified stop-loss rule;
- execution model missing;
- no independently reproduced evidence;
- no validated crypto portability;
- parameter-selection and data-snooping risk.

## Implementation status

Research record only.

No implementation in the current research stack has been completed. No Qlib full backtest, survivor promotion, Paper, Testnet, or Live validation is implied.

## Adoption boundary

This record is **research-only**.

Its presence in this repository does not mean it:

- passed Research Intake Review;
- entered Hermes Wiki Brain;
- entered the production candidate pool;
- completed Qlib validation;
- became a survivor or leaderboard entry;
- is profitable;
- is validated alpha;
- is approved for implementation;
- is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable related Wiki record is asserted in this GitHub-only Scout run.

## Sources

- TradingView — **[KL] Relative Volume Strategy**, DojiEmoji: https://www.tradingview.com/script/HNmT0VUi-KL-Relative-Volume-Strategy/ (public open-source strategy page; source reviewed as of 2026-09-25).
