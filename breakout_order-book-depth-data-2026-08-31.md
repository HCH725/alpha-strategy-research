---
schema: strategy-research-record-v1
title: "Price Level Breakout Family Representative (Order book / Depth data)"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - breakout_order-book-depth-data
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重周期唐奇安指标趋势跟踪与背离交易策略-Multi-Period-Donchian-Channel-Trend-Following-and-Divergence-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Price Level Breakout Family Representative (Order book / Depth data)

## Provenance
- Repository: https://github.com/fmzquant/strategies
- Commit: 7853bb2bf262c4567ac238d3552d97f0e50cb801
- File path: 多重周期唐奇安指标趋势跟踪与背离交易策略-Multi-Period-Donchian-Channel-Trend-Following-and-Divergence-Trading-Strategy.md
- URL: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重周期唐奇安指标趋势跟踪与背离交易策略-Multi-Period-Donchian-Channel-Trend-Following-and-Divergence-Trading-Strategy.md

## Economic mechanism
### Source-reported
> This strategy builds a trend following system based on multi-period Donchian Channels. By analyzing Donchian Channel breakouts across different timeframes and combining main and local trend relationships, it forms an visually intuitive trend ribbon. The strategy uses varying color depths to display trend strength, with green representing uptrends and red representing downtrends, where deeper colors indicate more pronounced trends.

### Research interpretation
Price Level Breakout logic. Based on actual source body semantics, grouped by materially compatible signal logic. Data dependency: Order book / Depth data.

## Signal
> The core of the strategy is trend determination based on the Donchian Channel indicator. The Donchian Channel consists of upper and lower bands, determining trends by comparing current price position relative to the channel. Key components include:
1. Main trend determination: Using 20-period Donchian Channel, uptrend forms when price breaks above upper band, downtrend forms when breaking below lower band
2. Local trend determination: Under the main trend framework, shorter period Donchian Channels determine local trend direction
3. Trend ribbon: Combination of 10 different period Donchian Channels forms a trend ribbon, with color depth reflecting trend strength
4. Trading signals: Long entries on uptrend, short entries on downtrend, positions closed on trend reversal

*Normalized Signal Interpretation:*
Entry and exit semantics are strictly defined by the source logic described above. Unknown parameters must be identified during PyBroker implementation.

## Required data
- Order book / Depth data

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
- Construct explicit PyBroker implementation honoring `Order book / Depth data` and the detailed signal rules.
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
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/多重周期唐奇安指标趋势跟踪与背离交易策略-Multi-Period-Donchian-Channel-Trend-Following-and-Divergence-Trading-Strategy.md
