---
schema: strategy-research-record-v1
title: "TradingView RSI Box Volume-Weighted Grid Breakout"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - breakout
  - rsi
  - volume-weighted
  - grid
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/I4XXBAtK-RSI-Box-Strategy-pseudo-Grid-Bot/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView RSI Box Volume-Weighted Grid Breakout

## Provenance

Public TradingView open-source strategy **RSI Box Strategy (pseudo- Grid Bot)** by **wbburgin**, published 2023-10-09. Stable public source: https://www.tradingview.com/script/I4XXBAtK-RSI-Box-Strategy-pseudo-Grid-Bot/ . Source reviewed as of 2026-09-16.

The source describes the strategy logic publicly; this record normalizes that description rather than redistributing the Pine source code.

## Economic mechanism

### Source-reported

The author describes the system as a pseudo-grid breakout strategy for algorithmic traders. Unlike a conventional grid that tends to sell into higher grid levels, this strategy builds a dynamic volume-weighted range when RSI crosses configured overbought/oversold conditions, divides that range into five evenly spaced levels, and trades directional breaches of the adjacent level.

### Research interpretation

The falsifiable hypothesis is that RSI extreme transitions can define event-driven reset points for a locally relevant price range, while volume-weighted extrema make that range more representative of traded participation than an unweighted high/low box. Once the box is frozen until the next qualifying RSI transition, crossing the adjacent grid boundary tests short-horizon directional continuation rather than conventional grid mean reversion.

The alpha-bearing elements should be separated from position-management effects: RSI-triggered box resets and adjacent-level breakout direction are the predictive hypothesis; pyramiding and order sizing are risk/exposure choices rather than evidence of alpha.

## Signal

Source-described normalized logic:

1. Use a configurable source series `src` and configurable RSI length plus overbought/oversold levels.
2. When the configured RSI crossunder/crossover condition occurs, update the dynamic box using volume-weighted highest and lowest values of `src`.
3. Divide the resulting high-low range into five evenly spaced grid lines.
4. Determine which grid line is currently closest to `src`.
5. If `src` crosses over the grid line immediately above the current/nearest line, enter a buy order.
6. If `src` crosses under the grid line immediately below the current/nearest line, enter a sell order when shorts are enabled.
7. The source states that closing the strategy sells 100% of pyramiding orders.

The public description does not state exact default RSI length, exact overbought/oversold defaults, the precise formula used for the volume-weighted extrema, causal ordering when an RSI reset and grid crossing occur on the same bar, or a separately specified holding-period exit beyond the described grid/order behavior. These details are **underspecified** and must not be invented.

## Required data

At minimum:

- timestamped OHLCV bars for the traded instrument;
- the selected `src` price series derivable from those bars;
- volume for construction of the volume-weighted box;
- sufficient lookback/history for the configured RSI calculation;
- deterministic bar ordering and candle boundaries.

The source is not venue-specific. Crypto portability therefore requires explicit venue/instrument selection during later testing rather than assuming identical behavior across spot and perpetual markets.

## Execution assumptions

The source describes directional orders on grid-line crosses but does not fully specify intrabar versus confirmed-close evaluation, fill model, slippage, spread, latency, or market/limit semantics in the public description.

For the strategy results discussed by the author, the source states **0.1% fee per trade**, **1% of equity order size**, and **maximum pyramiding of 33**. These are source-reported test settings, not independently validated recommendations and not part of the alpha hypothesis itself.

Any later research implementation must predeclare signal timing and next-bar/same-bar execution semantics before backtesting.

## Evidence

### Source-reported

The TradingView page presents the strategy as intended primarily for algorithmic trading and describes the dynamic volume-weighted RSI-reset grid and adjacent-level breakout rules. It also reports the fee, sizing, and pyramiding settings above for displayed strategy results. No performance statistic is promoted into this record because the reviewed public description does not provide a sufficiently attributable quantitative result needed for independent use here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative study was identified in the reviewed source. The mechanism nevertheless has clear testable failure risks: repeated RSI reset events may make the box unstable in oscillating regimes; five equal-price grid intervals may not correspond to equal volatility or information content; and high pyramiding can amplify exposure independently of signal quality. Absence of source-reported negative evidence is not evidence of robustness.

## Falsification plan

Test the normalized hypothesis without broad parameter mining.

- Compare the volume-weighted RSI-reset grid against a matched unweighted high/low grid and a simple breakout baseline.
- Include a negative control in which box-reset timestamps are shifted or otherwise decoupled from RSI transitions while preserving comparable trade opportunity count.
- Evaluate trending, ranging, high-volatility, and low-volatility regimes separately.
- Predeclare a small RSI parameter set before evaluation; do not optimize a large grid after observing returns.
- Measure whether adjacent-grid crossings retain value after realistic fees, spread, and slippage.
- Run a pyramiding ablation so signal quality is not confused with exposure scaling.
- Require out-of-sample persistence; failure to outperform the matched breakout/control after costs, or dependence on extreme pyramiding for acceptable results, materially weakens the hypothesis.

## Crypto portability

**unproven**

The rule only requires OHLCV-derived price and volume plus RSI, so it is technically portable to liquid crypto spot or perpetual bars. The cited source does not establish crypto-specific empirical validity in the reviewed description. Later crypto testing must account for 24/7 candle boundaries, venue-specific volume, spot-versus-perpetual differences, fees, spread/slippage, and funding where perpetuals are used.

## Limitations

- Not independently reproduced.
- Exact volume-weighted extrema formula is underspecified in the reviewed public description.
- Exact default RSI parameters are not preserved here because they were not explicitly stated in the reviewed description.
- Intrabar/close confirmation and fill semantics are underspecified.
- Pyramiding can dominate portfolio risk and must be separated from alpha evaluation.
- Equal spacing in price does not imply equal spacing in volatility-adjusted risk.
- Source publication is a TradingView community strategy, not peer-reviewed evidence.

## Implementation status

Research record only. No Qlib or other quantitative-runtime implementation or backtest has been completed as part of this Scout capture.

## Adoption boundary

This record is research material only. It is not evidence that the strategy is profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki record was resolved in this GitHub-only Scout cycle; no Wiki link is fabricated.

## Sources

- TradingView — wbburgin, **RSI Box Strategy (pseudo- Grid Bot)**, published 2023-10-09, public open-source strategy: https://www.tradingview.com/script/I4XXBAtK-RSI-Box-Strategy-pseudo-Grid-Bot/ (reviewed 2026-09-16).
