---
schema: strategy-research-record-v1
title: "RSI Mean Reversion Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - rsi-mean-reversion_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重指标动态反转交易系统RSI与VWAP协同反转策略-Multi-Indicator-Dynamic-Reversal-Trading-System-RSI-and-VWAP-Synergistic-Reversal-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI Mean Reversion Family Representative

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多重指标动态反转交易系统RSI与VWAP协同反转策略-Multi-Indicator-Dynamic-Reversal-Trading-System-RSI-and-VWAP-Synergistic-Reversal-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重指标动态反转交易系统RSI与VWAP协同反转策略-Multi-Indicator-Dynamic-Reversal-Trading-System-RSI-and-VWAP-Synergistic-Reversal-Strategy.md

## Economic mechanism
### Source-reported
> The RSI and VWAP Synergistic Reversal Strategy is an intelligent trading system that combines the Relative Strength Index (RSI), Volume Weighted Average Price (VWAP), and price action confirmation. This strategy identifies the relationship between market overbought/oversold conditions and VWAP position, incorporating price reversal confirmation signals to execute long and short trades when market conditions meet specific criteria. The strategy also includes risk management mechanisms such as trading cooldown periods, dynamic stop-loss/take-profit levels, and trailing stops, designed to capture short-term market reversal opportunities while controlling risk.

### Research interpretation
RSI Mean Reversion logic. Standard RSI strategy verified by code. Data dependency: OHLCV

## Signal
> The core principles of this strategy are based on the synergistic action of several key components:

1. **RSI Overbought/Oversold Identification**: Using the Relative Strength Index (RSI) to identify market overbought (RSI>72) and oversold (RSI<28) conditions. When RSI crosses down from the overbought zone or crosses up from the oversold zone, it may indicate an impending market reversal.

2. **VWAP Reference Line**: Volume Weighted Average Price (VWAP) serves as an important price reference line to confirm whether the price is in a reasonable zone. The relative position of price to VWAP is a key factor in determining the quality of potential reversal signals.

3. **Price Action Confirmation**: 
   - Short condition: Current close lower than previous close (downtrend) but still above VWAP, indicating price may be starting to fall from a high position
   - Long condition: Current close higher than previous close (uptrend) but still below VWAP, indicating price may be starting to bounce from a low position

4. **Volume Filter**: Ensures trade signals occur in sufficiently active market environments (volume>500), avoiding signals in conditions of insufficient liquidity.

5. **Cooldown Mechanism**: After executing a trade, the system forces a wait of a certain number of candles (default 10) before executing another trade in the same direction, preventing excessive trading in a short period.

6. **Dynamic Stop-Loss/Take-Profit**: Sets stop-loss and take-profit levels based on ATR (Average True Range), allowing them to automatically adjust to market volatility, with a default of 1.5 times ATR.

7. **Trailing Stop Option**: Provides a trailing stop feature option that can protect profits as the price moves in a favorable direction, with a default setting of 1.5% of price.

Signal triggering logic:
- Short signal: RSI crosses down through overbought level + Volume greater than minimum threshold + Price closes lower than previous close but higher than VWAP + Cooldown period ...

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- OHLCV

## Execution assumptions
- Signal-to-fill timing: underspecified; implementation must choose and test a causal execution convention.
- Fees/slippage/latency: underspecified; standard institutional assumptions must be supplied.

## Evidence
### Source-reported
Source claims vary by variant. Not independently reproduced.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan
- Construct explicit PyBroker implementation honoring `OHLCV` and the detailed signal rules.
- Test out-of-sample against structurally relevant assets.
- For hybrid candidates: isolate components via ablation to verify standalone predictive power of the core indicator.

## Crypto portability
direct

## Limitations
- underspecified parameter robustness
- not independently reproduced
- leakage/repainting risk: manual semantic review required for hidden repainting in original source code.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. Not approved for trading.

## Related Wiki records
None

## Sources
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重指标动态反转交易系统RSI与VWAP协同反转策略-Multi-Indicator-Dynamic-Reversal-Trading-System-RSI-and-VWAP-Synergistic-Reversal-Strategy.md
