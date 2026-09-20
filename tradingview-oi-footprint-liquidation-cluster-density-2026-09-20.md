---
schema: strategy-research-record-v1
title: TradingView OI-Footprint Liquidation-Cluster Density
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
  - https://www.tradingview.com/script/LFDkYZ0P-LiquidityMap/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView OI-Footprint Liquidation-Cluster Density

## Provenance

Public TradingView open-source indicator **LiquidityMap**, author/page identity `ralis24`, reviewed 2026-09-20. Stable source URL: https://www.tradingview.com/script/LFDkYZ0P-LiquidityMap/ . The reviewed page describes version 1.1 as a liquidation-cluster heatmap with footprint integration and explicitly states that it estimates, rather than observes, liquidation locations.

## Economic mechanism

### Source-reported

The source treats bars with both expanding open interest and sufficiently high volume as candidate position-entry events. It then classifies those entries as long or short using TradingView footprint volume delta, projects hypothetical liquidation prices across configurable leverage tiers, and aggregates projected liquidation exposure into price bins. The stated intuition is that dense projected clusters represent locations where forced exits could create cascade risk or price reactions.

### Research interpretation

The falsifiable hypothesis is not that the displayed heatmap is a true liquidation book. It is that **point-in-time OI expansion + participation intensity + aggressor-side volume delta contains information about newly established leveraged inventory, and leverage-projected clustering of that inventory may predict conditional volatility, directional continuation into a cluster, or reversal after a cluster is swept**.

This is materially distinct from an OI-spike-only liquidation proxy because footprint delta supplies a directional classification dependency and the signal of interest is accumulated cross-entry cluster density rather than only the presence of an abnormal OI event.

## Signal

Source-supported construction:

- Formation: scan a configurable historical window for bars where open interest increases and volume meets or exceeds a moving-average threshold.
- Default lookback reported by the source: 200 bars.
- Default volume filter reported by the source: volume at or above `1.0 × SMA(20)`.
- Direction classification: version 1.1 uses TradingView `request.footprint()` volume delta to infer buy-versus-sell pressure for qualifying entry bars.
- Projection: candidate entries are mapped to hypothetical liquidation prices using configurable leverage tiers and weights.
- Aggregation: projected levels are accumulated into price bins; denser bins form stronger candidate liquidation clusters.
- Footprint defaults reported by the source: 100 ticks per row and 70% value area.

The source does not specify a canonical systematic long entry, short entry, exit, holding period, re-entry rule, position sizing rule, or execution rule. These are **underspecified**.

Research-proposed operationalization for falsification only:

1. At each decision timestamp, construct cluster density using only information available by that timestamp.
2. Measure distance and signed direction from current price to the nearest high-density projected cluster.
3. Test competing outcomes rather than assuming direction: (a) continuation/attraction toward the cluster, (b) volatility expansion as price approaches or crosses it, and (c) reversal after a sweep.
4. Treat density thresholds, distance buckets, holding horizons, and sweep definitions as research-proposed parameters to be selected only inside the training sample and frozen before out-of-sample evaluation.

## Required data

- Crypto perpetual instrument with reliable point-in-time open-interest history.
- OHLCV at the research timeframe.
- Trade/footprint or equivalent aggressor-side volume delta if reproducing the v1.1 directional classification.
- Timestamp-aligned OI and volume data.
- Contract metadata needed to interpret OI units consistently.
- Configurable leverage-tier assumptions and weights.
- For source-faithful TradingView reproduction, footprint availability and the Binance-style OI feed described by the source are relevant platform dependencies.

Missing-data behavior across venues and historical OI/footprint availability are not fully specified by the source.

## Execution assumptions

The source is an indicator, not a complete executable strategy. Signal-to-order timing, next-bar versus same-bar execution, market/limit orders, fees, spread, slippage, impact, capacity, funding, leverage, margin, latency, partial fills and failure handling are unspecified.

Any backtest must prevent same-bar lookahead from footprint/OI values that are not finalized at the simulated decision timestamp. A practical first test should use next-bar execution after a completed signal bar unless a finer point-in-time event reconstruction is available; that convention would be **research-proposed**, not source-reported.

## Evidence

### Source-reported

The TradingView page states that the heatmap is an estimation tool rather than a direct exchange liquidation feed. It reports that qualifying entry bars require OI expansion plus volume at or above a 20-bar average by default, and that version 1.1 uses footprint volume delta to classify long/short pressure. It also states that validation against CoinGlass maps showed strong alignment in major cluster locations, but the reviewed page does not provide a reproducible sample, statistic, table, or test protocol for that claim; therefore no quantitative validation figure is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly states that it does not observe actual exchange liquidation orders and that absolute density differs from direct-data services. The projected liquidation map depends on assumed leverage distributions and on inferred position direction. OI expansion does not reveal leverage, entry price distribution, trader identity, or liquidation threshold by itself. Footprint delta measures aggressive trade imbalance, not whether every newly opened contract belongs to the inferred long/short side. These identification errors can make projected clusters structurally wrong even when inputs are measured correctly.

## Falsification plan

1. Build a strictly point-in-time sample of crypto perpetual OI, OHLCV and aggressor-side delta.
2. Compare nested baselines: price/volatility only → OI expansion only → OI + volume filter → OI + volume + footprint direction → projected leverage-cluster density.
3. Test three competing dependent variables separately: forward directional return toward the nearest cluster, forward realized volatility, and post-sweep reversal return.
4. Ablate the footprint classifier by replacing it with candle direction and with randomized direction labels; the footprint-dependent hypothesis weakens if these controls perform similarly.
5. Ablate leverage assumptions across broad tier/weight grids. Reject a cluster-location effect that exists only under a narrow leverage configuration selected ex post.
6. Randomize projected level locations while preserving event timestamps and density distribution as a spatial placebo.
7. Evaluate multiple assets, venues, volatility regimes and horizons with frozen parameters and untouched out-of-sample periods.
8. Include fees, spread, slippage and funding for any directional trading interpretation.
9. Where independently licensed direct liquidation data are available, compare proxy cluster locations against them; failure to locate actual liquidation concentration materially weakens the proposed mechanism.
10. Reject or downgrade the hypothesis if incremental out-of-sample information disappears after the OI/volume baselines, fails spatial/time placebos, or is not robust to reasonable leverage assumptions.

## Crypto portability

direct

The source is designed for crypto and specifically discusses perpetual-market OI. Portability is nevertheless venue-sensitive because OI units, contract specifications, footprint availability, liquidity, funding, and venue fragmentation differ. A Binance-derived OI map should not automatically be treated as market-wide positioning.

## Limitations

- Liquidation locations are estimated, not exchange-observed.
- Long/short inventory classification is inferred from footprint delta.
- Leverage distribution and liquidation-price weights are assumptions.
- Canonical entry, exit, holding period and sizing are underspecified.
- Historical footprint/OI availability may constrain reproducibility.
- Source-reported alignment with CoinGlass is not accompanied by a reproducible quantitative validation protocol on the reviewed page.
- Not independently reproduced.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full backtest has been completed for this record.

## Adoption boundary

This artifact is research-only. Its presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain link is asserted here.

## Sources

1. ralis24. **LiquidityMap**. TradingView open-source script, version 1.1 description reviewed 2026-09-20. https://www.tradingview.com/script/LFDkYZ0P-LiquidityMap/
