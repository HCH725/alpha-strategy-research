---
schema: strategy-research-record-v1
title: CVD Divergence at Volume-Profile Liquidity Zones with Trend Alignment
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/Mz2yrgYE/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CVD Divergence at Volume-Profile Liquidity Zones with Trend Alignment

## Provenance

Public TradingView open-source indicator **CVD Divergence & Volume Profile** by `Makadave`, published 2025-06-03. Stable source: https://www.tradingview.com/script/Mz2yrgYE/ . Source reviewed as of 2026-09-20.

The source combines Cumulative Volume Delta (CVD) divergence, simplified volume-profile levels (VAH, VAL, POC), proximity filtering, and an optional SMA trend filter. Repository deduplication on current `main` found no record for this canonical TradingView source. Existing CVD/order-flow records are conceptually related but materially distinct because this hypothesis conditions divergence on **price-location within volume-profile liquidity zones** and optionally on broad-trend alignment.

## Economic mechanism

### Source-reported

The author describes bullish divergence as price making a lower low while CVD makes a higher low, and bearish divergence as price making a higher high while CVD makes a lower high. The source interprets these patterns as weakening selling or buying pressure, respectively. It further treats VAH, VAL, and POC from a user-defined volume-profile range as important reaction zones, and only generates divergence signals when price is within a user-specified proximity of one of those levels. An optional SMA filter requires bullish signals above the SMA and bearish signals below it.

### Research interpretation

Hypothesis: **CVD-price divergence contains more useful short-horizon reversal information when it occurs at a point-in-time volume-profile liquidity/value boundary than when the same divergence occurs at arbitrary price locations; trend alignment may further distinguish pullback continuation from generic countertrend reversal.**

The components have distinct proposed roles:

- Primary signal: price/CVD divergence indicating aggression-result decoupling.
- Location filter: proximity to VAH, VAL, or POC, representing concentrated prior trading activity.
- Optional regime filter: SMA trend direction, converting the setup into a trend-aligned pullback/rejection hypothesis.

The mechanism is falsifiable and the components must be ablated. Volume-profile proximity or the SMA filter should not be presumed to add alpha merely because they create confluence.

## Signal

Source-specified elements:

- Bullish divergence: price makes a lower low while CVD makes a higher low or fails to make a new low.
- Bearish divergence: price makes a higher high while CVD makes a lower high or fails to make a new high.
- Compute simplified volume-profile levels over a user-defined `vp_range` of candles.
- VAH and VAL bound the source-described 70% value area; POC is the price level with the greatest volume within the range.
- A signal is eligible only when the current close is within user-defined `zone_thresh` proximity of VAH, VAL, or POC.
- Optional trend filter: bullish divergence requires close above the SMA; bearish divergence requires close below the SMA. The source states a default SMA period of 200.
- Source suggests entry on the signal candle or subsequent confirmation candle. It discusses stops beyond the divergence extreme or nearby profile level and targets at the opposite profile level, prior swing, or fixed risk/reward, but does not designate one canonical execution rule.

The reviewed source page does not unambiguously specify the exact divergence pivot/lookback algorithm, default `vp_range`, default `zone_thresh`, profile binning/allocation method, canonical entry choice, exit, holding period, re-entry, sizing, or risk/reward parameter. These are `underspecified` and must not be invented.

Research-proposed operationalization for falsification only: first reproduce each component causally using completed bars and point-in-time profile levels. Test divergence continuously/event-wise before introducing any research-selected threshold. Any pivot width, profile range, proximity threshold, execution delay, stop, target, or holding horizon introduced by research must be labeled `research-proposed` and selected without future information.

## Required data

- Crypto spot or perpetual OHLCV at the chosen chart timeframe.
- Lower-timeframe trades or bars sufficient to construct a defensible CVD proxy; true aggressor-side trade data should be preferred when available for robustness.
- Point-in-time volume-by-price information or a causally reconstructed volume profile from information available through the signal bar.
- Synchronized timestamps and explicit candle-boundary/timezone rules.
- Fees, spread and funding where perpetual markets are tested.
- Missing-data and venue-outage handling.

## Execution assumptions

The source is an indicator and does not define one canonical executable strategy. Signal-to-order timing, order type, fill model, fees, spread, slippage, impact/capacity, funding, leverage/margin, latency, partial fills and failures are not specified.

Research must avoid same-bar look-ahead: divergence pivots and volume-profile levels must be known at the decision timestamp, and a conservative baseline should execute no earlier than the next executable observation after signal confirmation. Any profile implementation that uses future bars to finalize bins, value area, pivots or extrema is invalid.

## Evidence

### Source-reported

The source explains the component logic and presents potential long/short interpretations, including bullish divergence near VAL/POC in an uptrend and bearish divergence near VAH/POC in a downtrend. It reports no independently audited backtest, Sharpe ratio, CAGR, drawdown, win rate or other strategy-performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No direct negative empirical result is reported on the reviewed source page. Important adverse possibilities are structural: CVD can be venue-specific or approximate rather than true aggressor flow; simplified volume-profile construction can be sensitive to binning and bar-level volume allocation; divergence detection can hide pivot-confirmation delay; and adding location plus trend filters can reduce sample size enough to create unstable apparent performance. Absence of source-reported negative evidence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the divergence, profile and SMA components causally; audit every timestamp for pivot confirmation and profile availability before measuring returns.
2. Ablate `price swing reversal baseline -> CVD divergence -> divergence + profile proximity -> divergence + profile proximity + SMA trend filter`. Reject the confluence thesis if location/trend filters add no stable out-of-sample information.
3. Separate VAH, VAL and POC events rather than pooling them initially. Test whether boundary reactions and POC interactions have materially different conditional outcomes.
4. Compare the source-style CVD construction with true aggressor-side trade delta where available. Reject robustness if the effect disappears with higher-quality order-flow data.
5. Compare the source-style simplified volume profile with alternative causal volume-by-price constructions and multiple pre-registered `vp_range` values. Reject if results depend on one arbitrary binning/range choice.
6. Evaluate reversal versus continuation as competing outcomes. A divergence at a profile level may signal absorption, but it may also precede a level break and continuation.
7. Use matched controls for contemporaneous return, realized volatility, total volume and distance from ordinary swing support/resistance. Require incremental information beyond generic reversal-at-level behavior.
8. Run timestamp-shift and randomized-level placebos. Real profile-conditioned divergence should outperform mechanically shifted divergence or matched random price levels.
9. Test bull, bear, high/low-volatility and high/low-liquidity regimes separately with walk-forward/out-of-sample evaluation.
10. Apply realistic fees, spread, slippage and funding. Reject any trading operationalization whose apparent edge is consumed by plausible costs or whose sample count is too small for stable inference.

## Crypto portability

`direct`

The source is applicable to volume-bearing crypto markets, but portability across venues and instruments is unproven. CVD is fragmented across exchanges; perpetuals introduce funding and mark/index mechanics; 24/7 trading removes a universal session anchor; and volume-profile/CVD behavior can vary materially with venue liquidity and candle boundaries.

## Limitations

- `underspecified`: exact divergence detection, `vp_range`, `zone_thresh`, profile construction, canonical entry/exit and holding rules are not fully specified in the reviewed source description.
- `not independently reproduced`.
- CVD may be an approximation and may not represent consolidated crypto order flow.
- Volume-profile levels are construction-sensitive and are not inherently causal support/resistance.
- Pivot/divergence confirmation can introduce hidden delay or look-ahead if implemented incorrectly.
- Multi-filter confluence risks data-mining and low effective sample size.
- Source interpretations are hypotheses, not verified causal evidence.

## Implementation status

Research record only. No implementation, backtest, robustness campaign, paper trading, testnet or live validation has been completed in our research stack.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply Research Intake Review passage, Hermes Wiki Brain entry, production-candidate admission, Qlib validation, profitability, validated alpha, survivor status, implementation approval, paper-trading approval, testnet approval or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

Repository-relative conceptual neighbors include existing CVD/order-flow divergence and volume/microstructure records; this record is differentiated by the explicit interaction between **CVD divergence, volume-profile location, and optional trend alignment**.

## Sources

- TradingView — **CVD Divergence & Volume Profile**, `Makadave`, published 2025-06-03, reviewed 2026-09-20: https://www.tradingview.com/script/Mz2yrgYE/
