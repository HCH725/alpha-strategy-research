---
schema: strategy-research-record-v1
title: TradingView OI-Spike Projected Liquidation-Zone Reaction
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
  - https://www.tradingview.com/script/DGJ1oqjE-Liquidation-Heatmap-by-Rumiancev/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView OI-Spike Projected Liquidation-Zone Reaction

## Provenance

Public TradingView open-source indicator **Liquidation Heatmap by Rumiancev**, author/page identity `Rumiancev`, reviewed 2026-09-20. Stable source URL: https://www.tradingview.com/script/DGJ1oqjE-Liquidation-Heatmap-by-Rumiancev/ . The page shows the script as open source, originally published February 11 and updated April 17. The source explicitly warns that its zones are estimates from a proxy model, not exchange-native liquidation prices.

## Economic mechanism

### Source-reported

The source assumes that unusually large participation spikes can represent bursts of leveraged activity. On perpetual markets it prefers open-interest delta; when OI is unavailable it can fall back to volume. At each spike event it projects potential long-liquidation levels below a reference price and short-liquidation levels above it for up to three leverage tiers, bins the projected levels, and accumulates weight. The author describes denser zones as potential crowded stress areas or liquidity magnets where price may react.

The updated source also distinguishes combinations of price direction and OI direction to make long-side versus short-side pressure attribution more realistic, rather than treating absolute OI change alone as directional evidence.

### Research interpretation

The falsifiable hypothesis is that **point-in-time OI shocks contain information about newly concentrated leveraged positioning, and mechanically projected leverage-distance zones derived from those shocks condition subsequent price behavior when revisited**. Two competing mechanisms must be tested rather than assumed: (1) a dense projected zone acts as a liquidity magnet and price continues toward/through it; or (2) forced deleveraging near the zone produces exhaustion/reaction and short-horizon reversal. A third null is that the zones add no directional information beyond volatility, OI magnitude, and ordinary price distance.

The source's liquidation-zone construction is a proxy, not observed trader leverage or exchange liquidation data. Any alpha claim therefore belongs to the projected-zone state, not to actual liquidation concentrations.

## Signal

Source-supported formation logic:

- **Primary stream:** `AUTO` uses OI delta when available and otherwise volume; `OI` forces OI delta; `VOL` forces volume.
- **Spike detection:** abnormal absolute stream activity relative to a configurable lookback. The source supports Z-Score, EMA Z-Score, and Average Multiple approaches; sensitivity controls event frequency.
- **Event spacing:** optional minimum bars between spike events.
- **Directional context:** the updated model distinguishes price-up/OI-up, price-down/OI-up, price-up/OI-down, and price-down/OI-down states when assigning likely long/short pressure.
- **Projection:** for each detected spike, estimated liquidation levels are projected below/above a configurable reference price for as many as three leverage tiers.
- **Aggregation:** projected levels are snapped to tick-scaled bins; bin weight accumulates over time.
- **Touch state:** when price touches a bin by wick or close, depending on configuration, that bin is frozen and stops updating.

The source does **not** specify a canonical standalone trade entry, exit, holding period, sizing rule, leverage set, spike lookback, sensitivity value, bin scale, or execution model. Those items are `underspecified`.

`research-proposed` operationalization for falsification only: freeze every event's projected bins using information available at event close; evaluate forward returns conditional on first subsequent approach/touch of active bins. Separately test continuation-through-zone, reaction/reversal-after-touch, and volatility-only outcomes over predeclared horizons. Do not retroactively rebuild historical bins using later information.

## Required data

- **Preferred instrument/market:** crypto perpetual futures; the source recommends BTCUSDT.P for consistent OI availability.
- **Fields:** OHLCV, open interest and OI delta where available; volume fallback; tick size; timestamps.
- **Venue:** source is chart/data-feed dependent and does not establish a canonical multi-venue aggregation rule.
- **Timeframe:** source says the indicator runs on any timeframe and recommends 15m / 1H / 4H as a signal-to-noise balance; 12H / 1D are described as cleaner/fewer-zone views and 1m / 3m / 5m as noisier.
- **Point-in-time requirement:** OI/volume observations, spike state, reference price, bin weights, active/frozen status, and any local-range filtering must be reconstructed exactly as they would have existed at each historical timestamp.
- Missing or revised OI feeds must not be silently substituted. Volume fallback must be analyzed separately because it changes the information set materially.

## Execution assumptions

No complete execution model is source-specified. Market versus limit order, signal-to-order timing, fees, spread, slippage, impact/capacity, funding, leverage/margin, partial fills, and latency are `underspecified`.

For research, any touch-based reaction test must avoid same-bar fill/look-ahead ambiguity. A conservative baseline should form the touch state only after the relevant bar is observable and execute no earlier than the next executable price. This is `research-proposed`, not source-reported.

## Evidence

### Source-reported

The source presents the indicator as a research/context tool for spotting nearby estimated stress zones, possible liquidity magnets, and areas where price may react after aggressive participation spikes. It explicitly says the model is not an exchange liquidation feed, does not know traders' real positions, and should not be treated as exact liquidation data. No independently verified performance statistic is reported on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies substantial model risk: projected zones are estimates from simplified spike detection plus leverage projections; results depend on symbol, timeframe, exchange OI availability, and configuration. Volume fallback can be noisier than OI. The model does not observe actual position leverage or real liquidation prices. No reviewed source evidence establishes that a projected zone predicts reversal rather than continuation, or adds alpha beyond generic volatility/OI shocks.

## Falsification plan

1. **Point-in-time reconstruction:** replay bin creation, accumulation, trimming, eviction and freezing without future data. Any inability to reproduce historical states without look-ahead invalidates the test.
2. **Competing directional hypotheses:** at first approach/touch, measure reversal, continuation-through-zone, and absolute-return/volatility responses. Reject a directional thesis if only volatility rises.
3. **Component ablation:** compare price/volatility baseline → OI-spike event only → projected leverage distance → bin accumulation/density → full directional OI-context model. Require incremental OOS information from the projection/density stages.
4. **Placebo zones:** generate matched-distance random or mechanically shifted levels with the same event times and zone counts. Reject zone-specific alpha if real projected bins do not outperform placebo levels.
5. **OI versus volume:** test OI mode and volume fallback separately. Do not pool them as equivalent signals.
6. **Leverage-tier robustness:** test predeclared leverage grids and nearby perturbations. Reject if results depend on one narrow arbitrary tier selection.
7. **Timeframe/regime robustness:** evaluate at least the source-highlighted 15m, 1H and 4H contexts and stratify by volatility/trend regimes.
8. **Cost sensitivity:** apply realistic spread, fees, slippage and funding for perpetual execution. Reject any tradeable interpretation that does not survive conservative costs.
9. **Out-of-sample:** freeze all event/projection parameters before final OOS evaluation; no tuning on the OOS period.

## Crypto portability

direct

The source is explicitly designed around crypto and recommends perpetual futures because OI delta is available and more directly related to leveraged positioning changes than spot volume. Portability across venues remains unproven because OI definitions, contract specifications, mark/index conventions, liquidity, timestamp boundaries and data revisions differ.

## Limitations

- `underspecified`: canonical spike parameters, leverage tiers, bin scale, entry/exit/holding and execution model.
- `not independently reproduced`.
- `data gap`: the source uses a proxy model rather than actual exchange liquidation positions.
- `unproven`: whether projected-zone density predicts direction, only volatility, or nothing incremental.
- OI feed availability and revisions can materially change historical reconstruction.
- Configuration flexibility creates substantial multiple-testing risk unless parameters are frozen ex ante.

## Implementation status

Research record only. No implementation, backtest, reproduction, or validation in the research stack has been completed.

## Adoption boundary

This record is research material only. It does not establish profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- TradingView — **Liquidation Heatmap by Rumiancev**, `Rumiancev`: https://www.tradingview.com/script/DGJ1oqjE-Liquidation-Heatmap-by-Rumiancev/ (reviewed 2026-09-20).
