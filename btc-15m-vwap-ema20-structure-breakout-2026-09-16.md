---
schema: strategy-research-record-v1
title: "BTC 15m VWAP / EMA20 Structure Breakout Alert"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/zC2Ix4xO/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC 15m VWAP / EMA20 Structure Breakout Alert

## Provenance

Public TradingView open-source indicator **BTC 15m VWAP Structure Breakout [ALERT]**, published by StockdalePD on 2026-01-08. Stable source URL: https://www.tradingview.com/script/zC2Ix4xO/. Source reviewed 2026-09-16. The source explicitly targets BTC on the 15-minute timeframe and describes an alert-only setup rather than automatic execution.

## Economic mechanism

### Source-reported

The author frames the setup as a trend-aligned structural-breakout filter intended to distinguish continuation breakouts from moves occurring inside ranging conditions. VWAP supplies directional/value alignment, EMA20 slope supplies short-term trend direction, and a breakout of recent structure supplies the trigger.

### Research interpretation

This is a composite trend-continuation hypothesis. The VWAP location acts as a market-bias gate; EMA20 slope acts as a short-horizon trend-persistence gate; and the prior 25-bar extreme plus a 0.15% clearance requirement acts as the structural breakout signal. The falsifiable hypothesis is that requiring all three conditions reduces false structural breakouts relative to an otherwise identical 25-bar breakout rule without the VWAP/EMA gates.

## Signal

Source-specified target: BTC, 15-minute bars.

Bullish bias requires:

- bar close above VWAP; and
- EMA20 higher than its value two bars earlier.

Bearish bias requires:

- bar close below VWAP; and
- EMA20 lower than its value two bars earlier.

Long alert requires bullish bias, close above EMA20, and price breaking above the previous 25-candle high by at least 0.15%.

Short alert requires bearish bias, close below EMA20, and price breaking below the previous 25-candle low by at least 0.15%.

The source describes these as alerts requiring manual confirmation, not automatic entries. It suggests checking volume expansion, breakout confirmation or pullback/reclaim, and higher-timeframe alignment after an alert, but does not specify deterministic thresholds for those discretionary checks. Those checks therefore remain **underspecified** and are not promoted into the normalized signal.

Signal formation is interpreted at completed 15-minute bar close because the source repeatedly states conditions in terms of closes; exact order-entry timing after an alert is not source-specified.

## Required data

- BTC OHLCV on 15-minute bars.
- VWAP inputs, requiring price and volume.
- EMA20 derived from price.
- At least 25 prior completed bars for the structural high/low plus sufficient EMA/VWAP warm-up history.
- Point-in-time construction must use only information available by the signal bar close; the prior 25-candle structural level must exclude future bars.
- The source does not require funding, open interest, order-book, mark/index, or derivatives-specific fields.

## Execution assumptions

The source is alert-only and explicitly leaves entry confirmation to the trader. Market versus limit execution, next-bar versus same-close fill, fees, spread, slippage, funding, leverage, sizing, stop loss, take profit, holding period, re-entry, and position-exit logic are not specified. Any later backtest must predeclare these rather than infer them from the source.

## Evidence

### Source-reported

The source claims the design is intended for trending BTC markets and breakout/expansion phases and characterizes choppy or low-volatility ranges as unfavorable. It does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, or other quantitative performance result suitable for recording as evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies choppy and low-volatility ranging markets as poor conditions. No independent negative study was identified in this TradingView-only Scout cycle; absence is not evidence of no negative result.

## Falsification plan

Test on point-in-time BTC 15-minute data with fees and realistic slippage. Compare the full rule against a baseline 25-bar high/low breakout using the same 0.15% clearance and identical execution assumptions. Ablate the VWAP gate and EMA20-slope gate separately and together. Require out-of-sample evaluation across trending, ranging, high-volatility, and low-volatility regimes. The core hypothesis is weakened if the filters do not improve risk-adjusted or drawdown-aware outcomes after costs versus the baseline, or if any apparent improvement disappears out of sample. Exit and holding rules must be fixed before testing because the source leaves them unspecified.

## Crypto portability

direct

The source explicitly targets BTC 15-minute trading. Portability beyond BTC is unproven. For perpetual-futures implementation, later research would additionally need to specify venue, funding treatment, mark/index conventions, leverage/margin, and 24/7 candle-boundary semantics.

## Limitations

- Alert-to-entry confirmation is discretionary and **underspecified**.
- Exit, holding period, sizing, and risk-management rules are **underspecified**.
- Exact VWAP session/reset convention is not stated in the published description and is therefore a **data gap** for strict reproduction.
- No independently reproduced performance evidence.
- Performance portability beyond BTC is **unproven**.

## Implementation status

No implementation or backtest in the user's research runtime has been performed. This record is research-only.

## Adoption boundary

This record is not evidence of profitable or validated alpha and does not authorize implementation, paper trading, testnet trading, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this GitHub-only Scout cycle; none is fabricated.

## Sources

- StockdalePD, **BTC 15m VWAP Structure Breakout [ALERT]**, TradingView, published 2026-01-08, reviewed 2026-09-16: https://www.tradingview.com/script/zC2Ix4xO/
