---
schema: strategy-research-record-v1
title: "Price Reversal Family Representative (Renko charts)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reversal_renko-charts
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多步骤非重绘Renko仿真趋势反转量化交易策略-Multi-Step-Non-Repainting-Renko-Emulation-Trend-Reversal-Quantitative-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Reversal Family Representative (Renko charts)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多步骤非重绘Renko仿真趋势反转量化交易策略-Multi-Step-Non-Repainting-Renko-Emulation-Trend-Reversal-Quantitative-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多步骤非重绘Renko仿真趋势反转量化交易策略-Multi-Step-Non-Repainting-Renko-Emulation-Trend-Reversal-Quantitative-Trading-Strategy.md

## Economic mechanism
### Source-reported
> Underspecified in source.

### Research interpretation
Price Reversal logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Renko charts.

## Signal
> The core principle of this strategy is to implement Renko brick functionality on a standard time-based chart while solving the repainting problem found in traditional Renko charts. The specific working principles are as follows:

1. **Parameter Configuration & Initialization**:
   - `brickSize`: Defines the brick size, determining how much price must move to form a new brick
   - `renkoPrice`: Stores the closing price of the last completed Renko brick
   - `prevRenkoPrice`: Stores the price level of the previous Renko brick
   - `brickDir`: Tracks the direction of bricks (1=up, -1=down)
   - `newBrick`: A boolean flag indicating whether a new brick has been formed
   - `brickStart`: Stores the bar index at which the current brick started

2. **Non-Repainting Renko Brick Identification**:
   - The system performs calculations only on confirmed bars, ensuring historical data is not recalculated
   - Calculates the difference between the current price and the last Renko brick level
   - When the price difference reaches or exceeds the brick size, a new Renko brick is formed
   - Updates the brick price level based on the number of bricks that would fit within the price movement
   - Updates the direction (brickDir) and sets a flag (newBrick) indicating a new brick has been formed

3. **Renko Visualization on Time-Based Charts**:
   - Uses graphical elements to draw Renko-style bricks on a standard chart
   - Green boxes represent bullish bricks
   - Red boxes represent bearish bricks
   - Once formed, bricks never change or disappear

4. **Multi-Step Trend Reversal Detection**:
   - The strategy checks not only the current brick direction but also compares multiple historical bricks
   - Confirms genuine trend reversals by verifying direction changes across consecutive bricks

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Renko charts

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
- Construct explicit PyBroker implementation honoring `Renko charts` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多步骤非重绘Renko仿真趋势反转量化交易策略-Multi-Step-Non-Repainting-Renko-Emulation-Trend-Reversal-Quantitative-Trading-Strategy.md
