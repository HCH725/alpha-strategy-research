---
schema: strategy-research-record-v1
title: "Moving Average Crossover Family Representative"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - moving-average-crossover_ohlcv
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/双模式自适应趋势交易策略EMA交叉结合ATR波动率风险管理系统-Dual-Mode-Adaptive-Trend-Trading-Strategy-EMA-Crossover-with-ATR-Volatility-Based-Risk-Management-System.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Crossover Family Representative

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 双模式自适应趋势交易策略EMA交叉结合ATR波动率风险管理系统-Dual-Mode-Adaptive-Trend-Trading-Strategy-EMA-Crossover-with-ATR-Volatility-Based-Risk-Management-System.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/双模式自适应趋势交易策略EMA交叉结合ATR波动率风险管理系统-Dual-Mode-Adaptive-Trend-Trading-Strategy-EMA-Crossover-with-ATR-Volatility-Based-Risk-Management-System.md

## Economic mechanism
### Source-reported
> The Dual-Mode Adaptive Trend Trading Strategy is a highly flexible quantitative trading system capable of intelligently switching between trend-following and counter-trend trading modes. This strategy utilizes EMA crossover signals as its core entry indicator, while employing the RSI indicator to determine market conditions, and integrating ATR volatility metrics for precise risk management. The strategy implements a fixed 5x leverage and features an automated position sizing mechanism based on account risk percentage, ensuring strict risk control for each trade.

Analysis of the code reveals that the strategy generates trading signals through crossovers between the fast EMA(3) and slow EMA(8), while using the trend EMA(55) to confirm the overall market direction. The innovation lies in its adaptive mechanism—when RSI indicates the market is in a clear trend state, the strategy executes trend-following logic; when the market is volatile but lacks a clear direction, the strategy automatically switches to counter-trend mode, capturing oversold/overbought rebound opportunities.

### Research interpretation
Moving Average Crossover logic. Standard MA crossover verified by code. Data dependency: OHLCV

## Signal
> The core principle of this strategy is to combine multiple indicators to determine market conditions and generate trading signals. The specific implementation logic is as follows:

1. **Indicator Calculation**:
   - Fast EMA(3): Captures short-term price movements
   - Slow EMA(8): Filters short-term market noise
   - Trend EMA(55): Determines overall market direction
   - ATR(14): Measures market volatility, used for stop-loss and take-profit settings
   - RSI(14): Evaluates whether the market is in a trending state

2. **Adaptive Trend Detection**:
   - Calculates trend strength through the distance between RSI and 50: `trendStrength = math.abs(rsiValue - 50) / 50`
   - Determines the market is trending when trend strength exceeds 0.3
   - Uses comparison between 5-period and 20-period SMAs to determine trend direction

3. **Intelligent Trading Logic**:
   - **Trend Market Mode** (RSI far from 50, trend strength > 0.3):
     - Long: Fast EMA crosses above Slow EMA + Price above Trend EMA + Short-term MA above Long-term MA
     - Short: Fast EMA crosses below Slow EMA + Price below Trend EMA + Short-term MA below Long-term MA
   - **Oscillating Market Mode** (RSI near 50, trend strength < 0.3):
     - Long: Fast EMA crosses above Slow EMA + Price below Trend EMA (oversold rebound)
     - Short: Fast EMA crosses below Slow EMA + Price above Trend EMA (overbought pullback)

4. **Risk Management Mechanism**:
   - Stop-loss set at 1.2 times ATR
   - Take-profit set at 2.0 times ATR
   - Dynamic position size calculation based on account risk percentage (default 1%)
   - Fixed 5x leverage

5. **Trade Execution Control**:
   - Minimum trade interval setting (default 72 minutes) to prevent overtrading
   - Ensures new signals are generated only when there is no existing position

At the execution level, the strategy selects the appropriate trading mode based on current market conditions, calculates precise position size, and sets dynamic stop-loss and take-profit levels b...

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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/双模式自适应趋势交易策略EMA交叉结合ATR波动率风险管理系统-Dual-Mode-Adaptive-Trend-Trading-Strategy-EMA-Crossover-with-ATR-Volatility-Based-Risk-Management-System.md
