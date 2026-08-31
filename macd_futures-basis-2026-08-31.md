---
schema: strategy-research-record-v1
title: "MACD Momentum Trend Family Representative (Futures Basis)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - macd_futures-basis
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多级动态MACD趋势跟踪量化策略结合52周高低位延展研判系统-Multi-Level-Dynamic-MACD-Trend-Following-Strategy-with-52-Week-High-Low-Extension-Analysis-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD Momentum Trend Family Representative (Futures Basis)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多级动态MACD趋势跟踪量化策略结合52周高低位延展研判系统-Multi-Level-Dynamic-MACD-Trend-Following-Strategy-with-52-Week-High-Low-Extension-Analysis-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多级动态MACD趋势跟踪量化策略结合52周高低位延展研判系统-Multi-Level-Dynamic-MACD-Trend-Following-Strategy-with-52-Week-High-Low-Extension-Analysis-System.md

## Economic mechanism
### Source-reported
> This strategy combines MACD cross signals from multiple timeframes with dynamic support and resistance levels based on 52-week highs and lows. It confirms trading signals through MACD crossovers on both weekly and daily timeframes while utilizing dynamic support and resistance lines formed by 52-week highs and lows to assist in market trend analysis, enabling more robust trading decisions. The strategy employs a dynamic stop-loss mechanism to effectively control risk while ensuring profits.

### Research interpretation
MACD Momentum Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Futures Basis.

## Signal
> The strategy is based on the following core logic:
1. Entry signals are confirmed by both weekly and daily MACD golden crosses, requiring bullish signals on both timeframes.
2. Exit signals are triggered by daily MACD death crosses, with positions closed once a bearish signal appears.
3. Dynamic stop-loss is set at the lowest price of the day when exit signals are triggered.
4. 52-week high/low lines are dynamically generated based on user-selected calculation basis (high/low or closing prices) and extend rightward as important reference levels.
5. The strategy employs 5% position management with a transaction cost of 1 currency unit per trade.

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Futures Basis

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
- Construct explicit PyBroker implementation honoring `Futures Basis` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- Pine Script `security()` call explicitly uses lookahead, severe leakage risk.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多级动态MACD趋势跟踪量化策略结合52周高低位延展研判系统-Multi-Level-Dynamic-MACD-Trend-Following-Strategy-with-52-Week-High-Low-Extension-Analysis-System.md
