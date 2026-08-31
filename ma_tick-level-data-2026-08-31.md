---
schema: strategy-research-record-v1
title: "Moving Average Crossover/Trend Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - ma_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ADR均线交叉策略-融合多维度技术指标和严格止盈止损的交易方法EMA-Cross-ADR-Strategy-A-Multidimensional-Technical-Indicator-Based-Trading-Method-with-Strict-Risk-Management.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover/Trend Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: ADR均线交叉策略-融合多维度技术指标和严格止盈止损的交易方法EMA-Cross-ADR-Strategy-A-Multidimensional-Technical-Indicator-Based-Trading-Method-with-Strict-Risk-Management.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ADR均线交叉策略-融合多维度技术指标和严格止盈止损的交易方法EMA-Cross-ADR-Strategy-A-Multidimensional-Technical-Indicator-Based-Trading-Method-with-Strict-Risk-Management.md

## Economic mechanism
### Source-reported
> The EMA Cross ADR Strategy is a quantitative trading strategy based on the TradingView platform. It combines multiple technical indicators to determine trends, filter signals, and set stop-loss and take-profit levels. The strategy employs two Exponential Moving Averages (EMAs) with different periods to identify the main trend, uses the Average Daily Range (ADR) as a volatility filter, and dynamically sets stop-loss and take-profit levels based on a risk-reward ratio. In addition, the strategy incorporates risk management measures such as a trading time window, break-even stops, and a maximum daily loss limit, aiming to capture trend opportunities while strictly controlling downside risk.

### Research interpretation
Moving Average Crossover/Trend logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> 1. Dual EMA Crossover: The strategy uses two EMAs with different periods to determine the trend. When the short-term EMA crosses above the long-term EMA, it is considered an uptrend, generating a long signal; conversely, when the short-term EMA crosses below the long-term EMA, it is considered a downtrend, generating a short signal.

2. ADR Volatility Filter: To avoid generating trading signals in low volatility environments, the strategy introduces the ADR indicator as a volatility filter. Positions are only allowed to be opened when the ADR value is above a pre-set minimum threshold.

3. Trading Time Window: The strategy allows users to set the start and end times for daily trading. Trades are only executed within the specified time window, which helps avoid illiquid or highly volatile periods.

4. Dynamic Stop-Loss and Take-Profit: The strategy dynamically calculates the stop-loss and take-profit prices based on the average highest and lowest prices of the most recent N candlesticks, combined with a pre-set risk-reward ratio. This ensures that the risk-reward of each trade is controllable.

5. Break-Even Stops: When a position reaches a certain profit level (user-defined risk-reward ratio), the strategy moves the stop-loss to the break-even point (entry price). This helps protect profits that have already been earned.

6. Maximum Daily Loss Limit: To control the maximum loss per day, the strategy sets a daily loss limit. Once the daily loss reaches this limit, the strategy stops trading until the next day's opening.

7. Close All Positions at End of Day: Regardless of whether positions have hit the take-profit or stop-loss levels, the strategy closes all positions at a fixed time each trading day (e.g., 16:00) to avoid overnight risk.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/ADR均线交叉策略-融合多维度技术指标和严格止盈止损的交易方法EMA-Cross-ADR-Strategy-A-Multidimensional-Technical-Indicator-Based-Trading-Method-with-Strict-Risk-Management.md
