---
schema: strategy-research-record-v1
title: TradingView Adaptive Volatility Trend Breakout
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/A5ZDJE6e-Adaptive-Volatility-Trend-Breakout-4H-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Adaptive Volatility Trend Breakout

## Provenance

Public TradingView open-source strategy page, **Adaptive Volatility Trend Breakout (4H+ Strategy)**, author/page identity `SpankyFPV`, published 2026-02-17. Stable source: https://www.tradingview.com/script/A5ZDJE6e-Adaptive-Volatility-Trend-Breakout-4H-Strategy/ . Source reviewed as of 2026-09-19.

## Economic mechanism

### Source-reported

The author describes a higher-timeframe trend-following system intended for 4H, daily, and weekly charts. A moving-average baseline defines a central value area. Dynamic bands are derived from the variability of real-time percentage price changes over a historical lookback, using a standard-deviation multiplier to form a neutral zone. A state-memory rule enters only after a definitive close outside a band and retains the trend state until price closes beyond the opposite boundary. The stated rationale is that volatility-adaptive bands expand in turbulent periods and contract in consolidation, suppressing some sideways-market noise while allowing persistent moves to be held.

### Research interpretation

The falsifiable hypothesis is that a volatility-normalized breakout distance around a moving-average baseline contains more useful trend information than a fixed-distance breakout, and that hysteresis/state memory reduces repeated whipsaw transitions. The alpha thesis is trend persistence after a volatility-scaled displacement; the neutral zone and state memory are filters, not independent evidence of alpha.

Component roles:

- Regime / baseline: moving average.
- Primary signal: close outside a standard-deviation-scaled volatility band.
- State filter: retain the active direction until an opposite-band close occurs.
- Exit / reversal: opposite-boundary close.

## Signal

Signal formation is evaluated on candle close according to the source description.

- Preferred source timeframes: 4H, daily, weekly.
- Baseline: moving average; exact MA type and default length are not stated on the reviewed public page.
- Volatility input: percentage price change over a historical lookback; exact return convention and default lookback are not stated on the reviewed page.
- Bands: volatility measure scaled by a standard-deviation multiplier around the baseline; exact formula and defaults are underspecified in the reviewed page text.
- Long entry: candle closes above the upper adaptive band.
- Short entry: candle closes below the lower adaptive band.
- Holding / state: remain in the established direction while price remains short of the opposite boundary.
- Exit / reversal: source states that exit occurs when price crosses and closes beyond the opposite boundary.
- Re-entry behavior beyond the state-memory description: underspecified.
- Position sizing: underspecified.

The public description identifies three main adjustable inputs — MA Length, Lookback, and Multiplier — but does not expose their default values in the reviewed page text. Do not infer them.

## Required data

At minimum:

- OHLC price bars sufficient to evaluate candle closes, percentage price changes, moving average, and adaptive bands;
- 4H or higher timestamps for the source-intended use case;
- enough warm-up history for the MA and volatility lookback.

The source page does not restrict the strategy to a particular crypto instrument, venue, or spot/perpetual market type. Those dimensions are therefore underspecified. Point-in-time construction must use only information available at each completed signal bar; future volatility or revised values must not enter the band calculation.

## Execution assumptions

The source specifies signal decisions on candle close but does not fully specify executable fill mechanics. A research implementation must distinguish signal-bar close from next-bar execution and must not assume a same-close fill without an explicit model.

Fees, spread, slippage, market/limit order choice, impact, capacity, funding, leverage, margin, borrow/shorting, latency, partial fills, and failure handling are not specified on the reviewed source page.

## Evidence

### Source-reported

The source describes the strategy as intended for 4H, daily, and weekly trend following and states that volatility-adaptive bands are intended to reduce premature entries during noisy periods. No source-reported Sharpe, CAGR, drawdown, win rate, or other performance statistic was used for this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative result was identified in the reviewed source. The page's robustness and noise-reduction statements are author rationale, not independently established evidence. The strategy also requires asset-specific multiplier calibration according to the author, creating parameter-selection and multiple-testing risk.

## Falsification plan

Test the normalized rule across liquid crypto instruments with strict chronological OOS splits and realistic costs. Required comparisons should include:

1. adaptive volatility-band breakout versus an otherwise comparable fixed-percentage or fixed-width breakout;
2. state-memory/hysteresis versus a rule that reacts independently to every band crossing;
3. MA-baseline + adaptive bands versus simpler price-channel or volatility-scaled trend baselines;
4. 4H, daily, and weekly cohorts without choosing the best timeframe after seeing full-sample results;
5. parameter stability across broad MA-length, lookback, and multiplier neighborhoods rather than a single optimized point;
6. cost and slippage sensitivity, especially around large volatility expansions.

The hypothesis is materially weakened if adaptive scaling and state memory fail to add stable OOS risk-adjusted value over simpler breakout controls, if results depend on a narrow parameter island, or if cost-adjusted performance disappears across instruments/regimes. Failure should lead to rejection or simplification rather than further indicator stacking.

## Crypto portability

direct

The source explicitly positions the system for high-volatility assets and higher-timeframe trading, but does not identify a fixed crypto venue or contract type. Crypto validation must separately account for 24/7 candle boundaries, venue fragmentation, spot versus perpetual prices, and perpetual funding where applicable.

## Limitations

- Exact MA type/default length: underspecified.
- Exact percentage-change and standard-deviation band formula: underspecified from the reviewed public description.
- Default lookback and multiplier: underspecified.
- Instrument, venue, and spot/perpetual scope: underspecified.
- Fill model and transaction-cost model: underspecified.
- Asset-specific calibration may create overfitting risk.
- Not independently reproduced.

## Implementation status

Research record only. No implementation or backtest in our research stack has been completed as part of this Scout cycle.

## Adoption boundary

This record is normalized external research material only. It is not evidence that the strategy is profitable or validated, and it is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

None asserted; no Wiki link is fabricated for this GitHub-only Scout record.

## Sources

- TradingView — SpankyFPV, **Adaptive Volatility Trend Breakout (4H+ Strategy)**, public open-source strategy, published 2026-02-17, reviewed 2026-09-19: https://www.tradingview.com/script/A5ZDJE6e-Adaptive-Volatility-Trend-Breakout-4H-Strategy/
