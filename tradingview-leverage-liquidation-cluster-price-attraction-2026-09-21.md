---
schema: strategy-research-record-v1
title: TradingView leverage liquidation-cluster price-attraction hypothesis
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/VBLeqKvy-Liquidation-Levels-LuxAlgo/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView leverage liquidation-cluster price-attraction hypothesis

## Provenance

- Primary source: LuxAlgo, “Liquidation Levels [LuxAlgo],” public TradingView open-source script, published 2023-10-19.
- Stable public URL: https://www.tradingview.com/script/VBLeqKvy-Liquidation-Levels-LuxAlgo/
- Source reviewed as of 2026-09-21.
- The source describes an estimator of potential liquidation zones rather than observed exchange liquidation events. No Pine source code is reproduced here.

## Economic mechanism

### Source-reported

The author states that the indicator estimates price levels where large liquidation events may occur. It identifies bars with significant trading activity using volume as the primary detector and volatility as a secondary detector, then projects potential liquidation zones from a reference price for configurable leverage tiers. The page specifically describes 100x, 50x, and 25x leverage as default high-leverage examples and states that price generally heads toward liquidity zones or clusters.

### Research interpretation

The falsifiable hypothesis is that dense estimated leveraged-position liquidation clusters can act as short-horizon price-attraction zones because movement toward a cluster may trigger forced position closures, adding directional market orders and creating a feedback loop. A competing hypothesis is that these estimated zones behave only as ordinary support/resistance proxies derived from price and volume and contain no incremental information about future returns, path, or realized volatility.

The source does not establish that its inferred levels correspond to actual exchange liquidation inventory. Treat “liquidation cluster” as a model-derived proxy, not ground truth.

## Signal

Source-specified components:

- Detect significant trading activity using a configurable **Volume Threshold**.
- Use a configurable **Volatility Threshold** as a secondary detector for significant price movement occurring with relatively lower trading activity.
- Use a configurable **Reference Price** as the base for liquidation-level calculations.
- Project potential long/short liquidation zones using configurable leverage assumptions; the source highlights 100x, 50x, and 25x.
- Larger plotted bubbles represent more significant inferred liquidation levels; attached lines represent estimated liquidation zones.

The public description does not specify enough numerical defaults or full formulas to reconstruct the detector and liquidation-price projection exactly from prose alone. Those elements are therefore **underspecified** here rather than inferred.

Research-proposed operationalization for later testing, not source-reported trading rules:

1. Reconstruct the source logic only from auditable point-in-time inputs and the public implementation when a later implementation stage begins.
2. At each bar close, form the set of liquidation zones that were already observable at that timestamp.
3. Measure signed distance to the nearest zone above and below price and a point-in-time cluster-density/strength measure.
4. Test whether price is more likely than matched controls to touch the nearest dense zone before moving an equal volatility-scaled distance in the opposite direction.
5. Separately test post-touch continuation versus rejection/reversal. Do not assume either outcome in advance.

Entry, exit, holding period, re-entry, sizing, stop, target, and portfolio rules are not specified by the source and remain **research-proposed / underspecified**.

## Required data

- Liquid crypto spot or perpetual OHLCV sufficient to reproduce the source’s price, volume, and volatility inputs.
- Exact venue and instrument identity; venue fragmentation can materially change volume and inferred zones.
- Bar timestamps and candle boundaries with strict point-in-time availability.
- If the hypothesis is validated against actual liquidation events, independently sourced exchange liquidation/trade data aligned to the same timestamps and venue.
- Leverage-tier assumptions and contract-specific maintenance-margin rules if converting the proxy into exchange-specific liquidation estimates.

Missing-data handling is not specified by the source.

## Execution assumptions

The source is an indicator and does not specify a complete executable strategy. Signal-to-order timing, market versus limit execution, fills, fees, spread, slippage, market impact, funding, leverage, margin, latency, partial fills, and failure handling are unspecified.

Any later backtest should form signals only after all required bar data is available and should execute no earlier than the next executable timestamp unless an independently justified intrabar model is used. This is **research-proposed**, not source-reported.

## Evidence

### Source-reported

The source states that estimated liquidation levels may help identify support/resistance, sentiment, and areas of potential volatility, and that price generally heads toward liquidity zones or clusters. It does not provide a traceable Sharpe ratio, CAGR, drawdown, hit rate, or controlled out-of-sample result on the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The indicator estimates potential liquidations from price/volume/volatility and leverage assumptions rather than observing actual account positions and maintenance margins. This creates substantial model-risk: apparent predictive power could be ordinary price/volume structure relabeled as liquidation information. No independently verified performance evidence was identified on the reviewed source page; absence is not evidence of no negative result.

## Falsification plan

1. **Price/volume baseline:** compare the liquidation-zone feature against matched models using the same OHLCV, volatility, pivots/reference-price information, and distance-to-recent-support/resistance without liquidation labels. Reject incremental-alpha claims if the liquidation transformation adds no stable OOS information.
2. **Attraction test:** for each point-in-time zone, test whether the nearest zone is touched before an equal ATR/realized-volatility-scaled move away. Use unconditional and regime-matched baselines.
3. **Actual-liquidation validation:** where reliable venue liquidation data exists, test whether predicted zones coincide with subsequently observed liquidation intensity more often than distance- and volatility-matched placebo levels. Failure materially weakens the proposed mechanism.
4. **Direction competition:** test pre-touch attraction separately from post-touch continuation and post-touch reversal. Do not combine opposing effects into one headline statistic.
5. **Ablation:** volume detector only → + volatility detector → + leverage projection → + cluster density. Retain added complexity only if it improves leakage-safe OOS results.
6. **Leverage sensitivity:** vary 25x/50x/100x assumptions and plausible contract-specific margin rules. A signal that exists only at one arbitrary leverage setting is fragile.
7. **Venue robustness:** compare major liquid venues and spot versus perpetual markets. A venue-volume artifact should not be generalized as market-wide liquidation pressure.
8. **Timestamp placebo:** shift inferred zones forward/backward and randomize leverage labels while preserving price/volume distributions. Similar performance under placebo weakens the causal interpretation.
9. **Costs:** evaluate fees, spread, slippage, funding and adverse selection for any executable research-proposed rule.
10. Require walk-forward or other leakage-safe out-of-sample evaluation. Any Scout-chosen acceptance cutoff is a **research-defined falsification threshold**, not a source claim.

## Crypto portability

**direct** — the source explicitly discusses leveraged positions and liquidation levels and is presented for markets including crypto. Portability still depends on venue-specific margin rules, leverage availability, contract type, funding, 24/7 trading, fragmented liquidity, mark/index-price conventions, and liquidation-engine design.

## Limitations

- **underspecified:** the reviewed public prose does not expose all formulas/defaults required for exact independent reconstruction.
- **not independently reproduced.**
- **proxy risk:** inferred liquidation zones are not observed liquidation books.
- **data gap:** actual historical account leverage distributions and maintenance-margin states are generally unavailable from ordinary OHLCV.
- **venue dependence:** volume and liquidation mechanics differ across exchanges and contracts.
- The source provides no independently verified profitability evidence on the reviewed page.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, leaderboard entry, Paper, Testnet, or Live validation has occurred.

## Adoption boundary

Research-only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No stable related Hermes Wiki record is asserted here. Repository-level deduplication found no existing record for the canonical TradingView source `VBLeqKvy-Liquidation-Levels-LuxAlgo` before this write.

## Sources

- LuxAlgo, “Liquidation Levels [LuxAlgo],” TradingView open-source script, published 2023-10-19, reviewed 2026-09-21: https://www.tradingview.com/script/VBLeqKvy-Liquidation-Levels-LuxAlgo/
