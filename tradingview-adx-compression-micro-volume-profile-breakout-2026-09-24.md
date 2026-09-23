---
schema: strategy-research-record-v1
title: TradingView ADX Compression Micro-Volume-Profile Breakout
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/9anGnOxj-Low-Volatility-Profiles-BigBeluga/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView ADX Compression Micro-Volume-Profile Breakout

## Provenance

Public TradingView open-source indicator **Low Volatility Profiles [BigBeluga]**, published by `BigBeluga` on 2025-11-28 and visible as of 2026-09-24:

https://www.tradingview.com/script/9anGnOxj-Low-Volatility-Profiles-BigBeluga/

This record normalizes the public TradingView description rather than redistributing Pine source code.

## Economic mechanism

### Source-reported

The source identifies low-volatility/consolidation phases with ADX threshold/cross logic, expands a range box with price during the compression, and builds a micro volume profile inside that range. It highlights the Point of Control (PoC), tracks positive versus negative volume as a delta clue, and treats a break above or below the modeled range as the end of the profile zone. The author presents the construction as a way to map accumulation/distribution structure before volatility expansion, with breakout, in-range mean-reversion, PoC reaction, and delta interpretation as possible uses.

### Research interpretation

The primary falsifiable hypothesis is that **volume-at-price structure formed specifically during an ADX-defined compression contains incremental information about the direction or quality of the subsequent range breakout beyond compression and breakout alone**. In particular, PoC location and the source-described positive/negative volume tilt may encode asymmetric participation inside the range. This interpretation must not upgrade the author's accumulation/distribution language into evidence of informed or institutional flow.

A minimal `research-proposed` test is to compare a plain compression-range breakout with otherwise identical breakouts conditioned on pre-breakout PoC location and/or volume-delta tilt. If the profile layer does not add stable out-of-sample information, reject it rather than adding filters.

## Signal

Source-described construction:

1. Detect a low-volatility/compression state using an ADX threshold and configurable cross logic.
2. While the compression remains active, build a dynamic range from observed highs/lows.
3. Partition the active range into price bins and accumulate volume into a micro volume profile.
4. Identify the PoC as the price bin with the greatest accumulated volume.
5. Track positive versus negative volume within the range to display a delta/imbalance clue.
6. Optionally extend the PoC forward as a potential reaction level.
7. End the profile zone when price breaks above or below the modeled range; the source also removes invalid or very small/short-lived ranges.

The source suggests several uses rather than one complete trading lifecycle: trade a break above/below the compression range, fade range edges while compression persists, use PoC as a reaction/battle zone, and use positive/negative delta as an accumulation/distribution clue. These are source-reported use cases, not a single fully specified strategy.

The reviewed public description does not expose numeric defaults for the ADX period/threshold, exact cross-state transition, minimum valid range duration/size, profile bin count, volume-allocation method within a candle, positive/negative volume classification formula, or precise breakout confirmation semantics. Those items are **underspecified** and must not be invented.

No complete source-specified entry, exit, holding period, re-entry, stop, position sizing, or portfolio rule is available from the reviewed description.

## Required data

- Instrument/universe: not restricted by the public description; crypto use remains to be tested.
- Required market fields: OHLCV sufficient for ADX, dynamic range construction, and the source's volume-profile approximation.
- Timeframe: not fixed in the reviewed description.
- Historical depth sufficient to initialize ADX and maintain the active compression/profile state.
- Point-in-time requirement: only bars and volume available through the signal timestamp may contribute to the active profile.
- Venue-specific traded volume is required; cross-venue aggregation must not be assumed.
- Any reproduction must document candle boundaries, missing bars, binning resolution, and how each bar's volume is assigned across price bins.
- If perpetuals are tested, contract/venue identity and volume semantics must be fixed in advance.

## Execution assumptions

The source is an indicator/context tool and does not specify market versus limit orders, signal-to-order timing, fill model, fees, spread, slippage, impact, capacity, funding, leverage, margin, borrow, latency, or partial fills.

For a `research-proposed` breakout test, determine the compression range and profile only from information available at or before bar close `t`, then execute no earlier than the next executable observation after confirmation. Do not let the breakout bar retroactively alter the pre-breakout profile used to predict that same breakout. Same-bar hindsight fills are not justified.

## Evidence

### Source-reported

The source describes the ADX compression detector, dynamic range, micro volume bins, PoC, positive/negative volume delta, PoC extension, breakout termination, and invalid-range cleanup. It claims these tools can help identify accumulation/distribution zones and prepare for volatility expansion, but the reviewed page does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, predictive coefficient, or controlled out-of-sample comparison establishing alpha.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's volume-profile and delta labels are bar-data constructions, not direct observations of resting liquidity, aggressor side, or institutional positioning. A visually plausible PoC or positive/negative volume tilt therefore need not represent informed accumulation/distribution. ADX is conventionally a trend-strength measure rather than a direct volatility estimator, so an ADX-defined "low-volatility" state must be compared with actual realized-volatility/range compression controls.

No independent negative study specific to this TradingView implementation was identified in this Scout cycle; absence is not evidence of no negative result.

## Falsification plan

1. **Reconstruct before return testing.** Resolve the source's exact ADX parameters/cross logic, profile bins, bar-volume allocation, positive/negative volume classification, validity cleanup, and breakout semantics from auditable source material. If exact defaults remain unavailable, pre-register `research-proposed` values and do not attribute them to the author.
2. **Plain-breakout baseline.** Compare the full construction against a simple high/low range breakout after the same ADX compression. The profile layer fails if it adds no stable OOS improvement after costs.
3. **Compression baseline.** Compare ADX-defined compression against simpler realized-volatility percentile, ATR/range compression, and Bollinger/Keltner-style squeeze states. If ADX contributes no incremental regime information, reject that layer.
4. **Profile ablation.** Test compression+breakout alone, +PoC location, +volume-profile shape/concentration, +delta tilt, and the combined construction. Attribute any effect only to components that survive ablation.
5. **Delta placebo.** Compare the source-style positive/negative volume proxy with simple candle direction, signed return, up/down bar count, and volume-weighted return. If the delta feature merely repackages price direction, do not call it order-flow alpha.
6. **PoC placebo.** Compare the pre-breakout PoC with range midpoint, VWAP, and randomly shifted in-range pseudo-PoCs. A PoC effect that does not beat these controls weakens the volume-at-price mechanism.
7. **No look-ahead profile.** Freeze the predictive profile immediately before breakout confirmation. Recompute only in a separate diagnostic to quantify how much apparent quality comes from including breakout-bar information.
8. **Direction and magnitude separately.** Predeclare tests for breakout direction/follow-through and for subsequent absolute volatility expansion. Do not infer directional alpha merely because compression predicts larger moves.
9. **Crypto robustness.** Test liquid BTC/ETH first, then a predeclared liquid-alt universe across spot and perpetual venues where comparable volume exists. Check multiple bar horizons and shifted UTC candle boundaries.
10. **Cost/turnover sensitivity.** Apply realistic fees, spread, slippage, and perpetual funding where relevant. Reject operational usefulness if any incremental edge disappears under conservative executable costs.
11. **Parameter robustness.** Require broad stability across reasonable ADX thresholds, compression durations, and profile resolutions rather than selecting a single optimum on the final test set.

Failure action: if micro-volume-profile/PoC/delta information does not add stable OOS information over plain compression breakouts and simpler controls, reject the profile layer rather than increasing rule complexity.

## Crypto portability

**unproven**

The construction can be calculated from crypto OHLCV, but the reviewed source does not provide crypto-specific controlled OOS evidence. Crypto volume is venue-fragmented, 24/7 candle boundaries are arbitrary, spot and perpetual volume represent different participant sets, and bar-derived volume delta is not equivalent to exchange trade aggressor data. These issues must be tested rather than assumed away.

## Limitations

- `not independently reproduced`
- `underspecified`: source numeric defaults and several implementation details are not exposed in the reviewed public description.
- `data gap`: exact bar-volume-to-bin allocation and positive/negative volume classification are not established here.
- `unproven`: no controlled crypto OOS evidence is relied upon.
- The source offers multiple discretionary use cases rather than a complete executable strategy lifecycle.
- ADX compression may proxy low trend strength rather than low realized volatility.
- Volume profile built from candles is an approximation and can be sensitive to bin count and bar resolution.
- Source language about accumulation/distribution or smart money should not be interpreted as observed participant identity.

## Implementation status

No implementation or Qlib full-backtest reproduction has been completed in our research stack. This record is normalized external research only.

## Adoption boundary

Research-only. Presence in this repository does not mean this hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No canonical Wiki link is asserted from this GitHub-only Scout cycle. Conceptually related families include volatility/compression breakouts, volume-at-price/PoC analysis, and volume-imbalance conditioning; conceptual similarity is not equivalence.

## Sources

- TradingView — `BigBeluga`, **Low Volatility Profiles [BigBeluga]**, public open-source indicator, published 2025-11-28; accessed/as-of 2026-09-24: https://www.tradingview.com/script/9anGnOxj-Low-Volatility-Profiles-BigBeluga/
