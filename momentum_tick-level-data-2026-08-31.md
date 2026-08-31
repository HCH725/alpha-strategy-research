---
schema: strategy-research-record-v1
title: "Momentum Family Representative (Tick-level data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum_tick-level-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势动量渗透指标交易策略-Trend-Momentum-Penetration-Indicator-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Momentum Family Representative (Tick-level data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 趋势动量渗透指标交易策略-Trend-Momentum-Penetration-Indicator-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势动量渗透指标交易策略-Trend-Momentum-Penetration-Indicator-Trading-Strategy.md

## Economic mechanism
### Source-reported
> The Trend Momentum Penetration Indicator Trading Strategy is a quantitative trading system based on a combination of daily chart technical indicators. It primarily utilizes moving average systems, volatility indicators, volume confirmation, and price momentum to identify potential trending markets and enter positions when key technical levels are breached. The strategy confirms long-term trend direction through daily EMA systems, identifies price breakouts using ATR volatility indicators, and employs volume indicators and candlestick patterns as auxiliary confirmation signals, thereby constructing a multi-factor market entry system.

### Research interpretation
Momentum logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Tick-level data.

## Signal
> The core principle of this strategy is based on the synergy of multiple technical indicators forming a complete trading system. Specifically, the strategy confirms entry signals through the following four conditions:

1. **Trend Confirmation Condition**: By determining whether the 50-day moving average is above the 100-day moving average (dailyEMA50 > dailyEMA100), confirming that the market is in an uptrend.

2. **Breakout Confirmation Condition**: By determining whether the daily closing price has broken through the level of the 10-day moving average plus ATR (dailyClose > ema_plus_atr), indicating that the price has broken through the upper band of the recent volatility range, showing strong upward momentum.

3. **Candlestick Pattern Confirmation**: By determining whether the daily closing price is higher than the opening price (dailyClose > dailyOpen), confirming that the day is a bullish candle, indicating buyer dominance.

4. **Volume Confirmation**: By determining whether the daily volume is higher than the 12-day volume moving average (dailyVol > dailyVolEMA12), confirming increased market participation and enhancing signal reliability.

When these four conditions are simultaneously met, the strategy generates an entry signal on the daily chart. After entry, the strategy sets ATR-based stop-loss and take-profit points:
- Stop-loss level: 10-day moving average minus ATR (ema_minus_atr)
- Take-profit level: 10-day moving average plus 3 times ATR (ema_plus_atr1)

Additionally, the strategy implements a risk management mechanism, controlling the risk per trade within 2% of account equity by calculating the risk per share and the number of shares that can be traded.

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/趋势动量渗透指标交易策略-Trend-Momentum-Penetration-Indicator-Trading-Strategy.md
