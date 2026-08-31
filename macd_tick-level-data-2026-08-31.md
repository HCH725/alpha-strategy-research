---
schema: strategy-research-record-v1
title: "MACD Momentum Trend Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - macd_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/反转双MACD交易策略Dual-MACD-Reversal-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD Momentum Trend Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 反转双MACD交易策略Dual-MACD-Reversal-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/反转双MACD交易策略Dual-MACD-Reversal-Trading-Strategy.md

## Economic mechanism
### Source-reported
> The Dual MACD Reversal Trading Strategy is a quantitative trading strategy that uses the MACD indicator to identify trend reversal signals. This strategy also combines the RVI indicator and the CCI indicator to confirm buy signals and filter out some false reversals. This strategy is suitable for intraday and short-term trading.

### Research interpretation
MACD Momentum Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> The strategy is mainly based on the MACD indicator. MACD is the fast moving average EMA(12) minus the slow moving average EMA(26) to get the fast line, and then use SIGNAL(9) as the slow line. When the fast line crosses above the slow line to generate a Golden Cross, it is bullish; When the fast line crosses below the slow line to generate a Dead Cross, it is bearish.

This strategy uses dual time frame MACD indicators to identify reversal opportunities. The strategy uses the 6-hour MACD to determine the overall trend direction and the 1-hour MACD to find reversal signals. When the 6-hour MACD is in an uptrend, if the 1-hour fast line crosses below the slow line to generate a death cross signal, it indicates that the price may reverse upwards. At this point, combine the RVI indicator and CCI indicator to further confirm and generate a buy signal.

The RVI indicator measures the relationship between the closing price and opening price of the most recent few candlesticks versus the highest and lowest prices. An RVI below 0.2 is considered oversold. The CCI indicator below -100 indicates oversold. So the strategy uses the RVI indicator below 0.2 and the CCI indicator below -95 to help confirm the buy signal.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Tick-level data

## Execution assumptions
- Source-derived execution logic is underspecified in pure technical descriptions unless detailed in the signal logic block above. Assumes generic next-bar execution unless tick-level data is strictly required.
- Fees and slippage not strictly accounted for.

## Evidence
### Source-reported
Source claims vary by variant. Not independently reproduced.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan
- Construct explicit PyBroker implementation honoring `Tick-level data` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- None explicitly detected in structural scan; manual semantic review required for hidden repainting.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/反转双MACD交易策略Dual-MACD-Reversal-Trading-Strategy.md
