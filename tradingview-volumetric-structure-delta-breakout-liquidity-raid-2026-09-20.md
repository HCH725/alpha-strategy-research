---
schema: strategy-research-record-v1
title: TradingView Volumetric Structure Delta Breakout and Liquidity-Raid Reaction
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
  - https://www.tradingview.com/script/Xm3bgeHB-Volumetric-Order-Flow-Structure-LuxAlgo/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Volumetric Structure Delta Breakout and Liquidity-Raid Reaction

## Provenance

Public TradingView open-source indicator **Volumetric Order Flow Structure [LuxAlgo]**, author/page identity `LuxAlgo`, reviewed 2026-09-20. Stable source URL: https://www.tradingview.com/script/Xm3bgeHB-Volumetric-Order-Flow-Structure-LuxAlgo/ . The TradingView page shows the open-source script dated February 16.

## Economic mechanism

### Source-reported

The source combines market-structure breaks with volumetric context. It detects Change of Character (CHoCH) and Break of Structure (BOS); breakout bars are represented by volumetric bars whose horizontal fill is based on the breakout bar's volume delta. Active order blocks contain a 15-row volume profile with a Point of Control (POC). The source also marks a liquidity raid when price wicks beyond a zone but fails to close through it, with bubble size reacting to volume. The author frames these features as ways to distinguish high-conviction breakouts from low-volume fakeouts and to identify possible reversal or continuation around liquidity raids.

### Research interpretation

The falsifiable hypothesis is that **a structural price break contains incremental directional information when confirmed by contemporaneous volume-delta pressure, while a wick-through/close-back liquidity raid at an active volumetric zone contains short-horizon rejection information; the zone's internal POC may further condition that reaction**.

These are competing conditional mechanisms, not assumptions that every BOS continues or every raid reverses. A null explanation is that structure, delta, POC and raid labels add no information beyond ordinary price breakout magnitude, total volume and volatility.

## Signal

Source-supported components:

- **Structure formation:** pivot highs/lows are detected using a configurable `Pivot Length`; the script identifies BOS and CHoCH events.
- **Breakout context:** the breakout bar carries a volume-delta representation intended to show internal buying or selling pressure.
- **Volumetric zone:** active order blocks use a 15-row horizontal volume distribution derived from the pivot candle, with the POC marking the highest-volume price node.
- **Zone lifetime:** active zones extend until price closes beyond them.
- **Liquidity raid:** price wicks beyond a zone but fails to close through it; the source marks the event with a volume-scaled bubble.
- **Relative-volume context:** `Volume Lookback` controls the window used for relative-volume scaling/sensitivity.
- **Overlap handling:** an optional filter keeps the more relevant/higher-volume block when zones overlap.

The reviewed source does **not** specify a canonical standalone trading entry, exit, holding period, re-entry rule, position sizing, stop, target, exact default pivot length, exact volume-lookback value, or execution model. Those elements are `underspecified`.

`research-proposed` operationalization for falsification only:

1. At each confirmed BOS/CHoCH, freeze all structure and delta information available at bar close and test forward returns conditional on delta alignment versus weak/opposing delta.
2. At the first point-in-time wick-through/close-back event for an active zone, test reversal versus continuation from the next executable bar.
3. Separately test whether distance to the zone POC and relative volume improve either conditional signal.

No same-bar trade assumption should be introduced unless the source timing can be reproduced without look-ahead.

## Required data

- Instrument/universe: source is presented as cross-asset and explicitly says ATR scaling is intended to work on high-priced cryptocurrencies as well as other assets; crypto applicability remains to be tested per instrument.
- Market type/venue: not canonically specified by the source.
- Timeframe: not canonically specified.
- Fields: OHLCV; volume information sufficient to reconstruct the source's volume-delta representation; tick/price resolution sufficient for the stepped profile; timestamps.
- Derived point-in-time state: confirmed pivots, BOS/CHoCH state, active/inactive zone state, zone boundaries, 15-row profile, POC, breakout-bar delta, relative-volume state, and wick-versus-close raid state.
- Point-in-time requirement: pivot confirmation and zone creation must be timestamped only when knowable. Historical structure labels must not be backfilled to their visual pivot location as if known earlier.
- If the source's volume delta is an approximation rather than exchange-native aggressor-side trade delta for a given feed, that distinction must be preserved and tested rather than silently treated as true signed flow.

## Execution assumptions

The source does not provide a complete execution specification. Signal-to-order timing, market versus limit order, fills, fees, spread, slippage, impact/capacity, funding, leverage/margin, shorting constraints, latency and partial fills are `underspecified`.

For research, a conservative `research-proposed` baseline is to form signals only after the confirming bar closes and execute no earlier than the next executable price. Raid tests must not use the same bar's completed wick/close pattern to assume an intrabar fill at a favorable earlier price.

## Evidence

### Source-reported

The source states that the tool is intended to distinguish high-conviction breakouts from low-volume fakeouts, identify high-volume/POC levels inside zones, and flag liquidity raids that may precede reversal or continuation. The reviewed page does not report a traceable backtest, Sharpe, CAGR, drawdown, win rate or other strategy-performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself presents liquidity raids as potentially preceding either reversal or continuation, so the directional sign is not established. Its labels combine several discretionary-looking structural concepts whose incremental contribution is unknown. Pivot-based structure can introduce confirmation delay, and volume-delta/profile construction may depend materially on TradingView data resolution and feed semantics. No reviewed source evidence demonstrates that delta confirmation, POC location or raid bubbles add out-of-sample alpha beyond price structure, total volume and volatility.

## Falsification plan

1. **Leakage-safe structure replay:** reconstruct pivot confirmation, BOS/CHoCH, zone creation and invalidation strictly point in time. Reject any result that depends on assigning a pivot or zone before it was confirmable.
2. **Breakout ablation:** compare price breakout/BOS alone → + total volume → + volume-delta alignment → + volumetric-zone/POC context. Require incremental OOS information from delta and profile features.
3. **Raid competing hypotheses:** after wick-through/close-back events, measure both reversal and continuation over predeclared horizons. Reject a directional raid thesis if the effect is only higher absolute return/volatility.
4. **POC specificity:** compare true zone POC distance with zone midpoint, uniformly shifted levels and matched random within-zone levels. Reject POC-specific alpha if placebo levels perform similarly.
5. **Delta validation:** compare the TradingView-compatible delta construction with true aggressor-side trade delta where available. Treat divergence in results as model risk rather than confirmation.
6. **Volume placebo:** preserve event timestamps but shuffle/match volume or delta ranks within volatility regimes. Require real volumetric conditioning to beat placebo conditioning.
7. **Parameter robustness:** predeclare reasonable pivot-length and volume-lookback grids; reject effects that exist only at a narrow setting.
8. **Regime/timeframe robustness:** stratify trend/range and volatility regimes and test multiple liquid crypto timeframes without pooling incompatible candle boundaries.
9. **Costs:** apply realistic fees, spread and slippage; include funding for perpetual implementations. Reject a tradeable interpretation that disappears under conservative costs.
10. **Out-of-sample:** freeze signal definitions and parameter selection before final OOS evaluation.

## Crypto portability

unproven

The source explicitly presents the visualization as usable on high-priced cryptocurrencies, but the reviewed page does not provide crypto-specific performance evidence. Crypto portability therefore remains unproven. Venue fragmentation, 24/7 candle boundaries, spot-versus-perpetual volume semantics, funding, contract specification and differences between estimated and true signed order flow are material risks.

## Limitations

- `underspecified`: canonical entry, exit, holding, sizing, stops/targets, exact parameter defaults and execution model.
- `not independently reproduced`.
- `unproven`: incremental alpha from delta confirmation, POC, volumetric zones or liquidity-raid labels.
- Pivot confirmation can create material timing delay and look-ahead risk if reconstructed incorrectly.
- Volume-delta semantics may vary by feed and may not equal true aggressor-side trade flow.
- Combining BOS/CHoCH, order blocks, POC, delta and raid features creates multiple-testing risk; component ablation is mandatory.

## Implementation status

Research record only. No implementation, backtest, reproduction or validation in the research stack has been completed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitability, or received implementation, Paper, Testnet or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — **Volumetric Order Flow Structure [LuxAlgo]**, `LuxAlgo`: https://www.tradingview.com/script/Xm3bgeHB-Volumetric-Order-Flow-Structure-LuxAlgo/ (reviewed 2026-09-20).
