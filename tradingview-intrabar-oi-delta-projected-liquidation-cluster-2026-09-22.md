---
schema: strategy-research-record-v1
title: TradingView Intrabar OI-Delta Projected Liquidation Clusters
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-22
sources:
  - https://www.tradingview.com/script/d2LdGqQO-Liquidation-Heatmap-Proxy-victhoreb/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Intrabar OI-Delta Projected Liquidation Clusters

## Provenance

Public TradingView open-source indicator **Liquidation Heatmap Proxy [victhoreb]**, author `victhoreb`, published 2025-08-06 and updated 2025-08-09. Stable source URL: https://www.tradingview.com/script/d2LdGqQO-Liquidation-Heatmap-Proxy-victhoreb/. Source reviewed as of 2026-09-22.

The source explicitly describes itself as a proxy rather than an exchange liquidation feed.

## Economic mechanism

### Source-reported

The author reconstructs candidate leveraged-position entry locations from positive intrabar open-interest delta (OID), optionally conditioned on a main-bar open-interest peak. Intrabar price movement is used to classify estimated newly opened long versus short positions. User-selected leverage assumptions are then applied to project liquidation levels. Estimated contracts associated with each projected level are accumulated into price bins; subsequent estimated position additions can increase a pre-existing bin's weight.

The source presents these levels as estimates of where liquidation pressure may exist, not as actual exchange-reported liquidation prices.

### Research interpretation

The falsifiable hypothesis is that **point-in-time clusters of projected liquidation exposure derived from newly added intrabar open interest contain incremental information about subsequent price-path behavior**. If leveraged positions are concentrated near similar inferred entry prices, mechanically related liquidation thresholds may create nonlinear forced-flow risk when price approaches those thresholds.

Two competing behaviors must be tested rather than selected after observing results:

1. **Cascade / continuation:** first penetration of a sufficiently dense projected cluster is followed by same-direction continuation because forced liquidations add market-order pressure.
2. **Sweep / exhaustion:** traversal of a dense cluster is followed by reversal after forced flow is consumed.

The distinction from generic OI-anomaly research is the explicit state variable: a persistent **price-level distribution of leverage-conditioned projected liquidation exposure**, built from positive intrabar OID, rather than only contemporaneous OI change or liquidation-event classification.

## Signal

The source is an indicator, not a complete trading strategy.

Source-supported construction:

- Formation uses intrabar observations inside each parent bar.
- Candidate position formation is restricted to sub-bars with positive open-interest delta; an optional source filter further conditions these on a main bar with an OI peak.
- Long/short position classification is inferred from intrabar price movement and a configurable dispersion factor.
- The source notes that the dispersion factor can be set to zero when tick intrabar resolution is used.
- Liquidation levels are projected from inferred positions using user-selected leverage values.
- Level width is `syminfo.mintick × scale`.
- Intrabar OID is used as the weight representing estimated contracts exposed at each projected liquidation level.
- Repeated estimated exposure at an existing level is accumulated.
- The source provides alerts for estimated liquidation in the long or short direction.

The public description does not establish a canonical leverage set, scale, OI-peak threshold, entry rule, exit rule, holding period, re-entry rule, position sizing rule, or execution model. Those elements are **underspecified** and must not be inferred from the visualization.

Research-proposed operationalization for falsification only:

- Freeze each cluster using only OI and price observations available at signal time.
- Define cluster density from the accumulated OID weight using a rolling, past-only normalization.
- Test first-touch, first-penetration, and completed-sweep events separately.
- Evaluate continuation and reversal outcomes over pre-registered forward horizons rather than selecting the best horizon ex post.
- Compare multiple leverage assumptions only as a declared parameter domain; do not treat the visually strongest historical tier as canonical.

All items in the preceding research-proposed block are hypotheses for later testing, not source-reported rules.

## Required data

- Crypto perpetual/futures instruments with reliable open-interest history.
- Intrabar or tick-level timestamps, prices, and open-interest values sufficient to compute point-in-time OI delta.
- Parent-bar OHLC for event alignment.
- Contract specification and `mintick` for price-bin construction.
- Venue/symbol identity and contract changes through time.
- Point-in-time data availability; revised/backfilled OI must not be treated as contemporaneously known.
- If validating the proxy mechanism, exchange-reported liquidation events or another independently sourced liquidation feed aligned by timestamp and side.

The source description does not establish that its inferred long/short positions or projected liquidation levels equal exchange account-level positions. They are model-derived estimates.

## Execution assumptions

No complete execution model is source-specified. Signal-to-order timing, next-bar versus same-bar execution, market versus limit orders, fees, spread, slippage, impact, capacity, funding, leverage/margin of the research trade itself, latency, partial fills, and failure handling are unspecified.

Any later backtest must prevent parent-bar look-ahead: an intrabar OI observation may affect a cluster only after that observation exists. Same-bar fills at levels reconstructed using later sub-bars would be invalid.

## Evidence

### Source-reported

The TradingView page describes the construction and states that the result is a proxy. It does not provide a traceable backtest, Sharpe ratio, CAGR, drawdown, win rate, statistical significance, or independently validated accuracy against exchange liquidation records.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself cautions that the model is only a proxy. Inferred position direction comes from intrabar price movement rather than account-level position data, and projected liquidation prices depend on assumed leverage rather than observed leverage. The source also documents a visualization limitation: when additional estimated exposure appears at an existing level, the entire displayed level is repainted with the brighter accumulated weight, whereas the underlying exposure increase occurred only from that later time onward. A backtest must reconstruct the state point-in-time rather than consume the final repainted chart.

No source-backed profitability evidence was identified on the reviewed TradingView page; absence of reported negative performance is not evidence of profitability.

## Falsification plan

1. **Proxy-validity gate:** compare projected clusters against independently sourced, timestamped liquidation events. If cluster density has no meaningful association with subsequent actual liquidations beyond price proximity and volatility controls, reject the proposed mechanism before testing return alpha.
2. **Point-in-time reconstruction:** store cluster state as it existed at each timestamp. Never use the source's retrospectively repainted visual state.
3. **Baselines:** compare against price-only distance to recent highs/lows, realized volatility, volume, raw OI delta, and an OI-anomaly baseline without projected leverage levels.
4. **Leverage ablation:** test each pre-declared leverage tier separately and a pooled cluster representation. Require stability rather than one isolated winning leverage assumption.
5. **OID ablation:** compare positive-OID position reconstruction with simpler OI-change features. The projection layer must add OOS information to justify its complexity.
6. **Event definitions:** separately test approach, first touch, penetration, and completed sweep. Do not merge continuation and reversal labels.
7. **Direction test:** pre-register both cascade-continuation and sweep-exhaustion hypotheses. Reject any direction that fails independently.
8. **Timing placebo:** lag or jitter cluster timestamps. Comparable placebo performance would indicate alignment leakage or generic price-level effects.
9. **Regime robustness:** evaluate high/low volatility, trend/range, positive/negative funding, and high/low OI regimes without choosing regimes after seeing performance.
10. **Cost sensitivity:** apply realistic fees, spread, slippage, funding, and latency. Reject tradable-alpha claims if the effect does not survive costs.
11. **Out-of-sample requirement:** parameter choices must be frozen before OOS evaluation. Failure to beat the strongest simple baseline on leakage-safe OOS data rejects the added liquidation-cluster layer.

## Crypto portability

**direct** — the source is designed around crypto derivatives open interest and explicitly discusses perpetual-market OI behavior. Portability still depends on venue-specific OI definitions, contract denomination, leverage availability, funding, 24/7 timestamp boundaries, and historical symbol continuity.

## Limitations

- `underspecified`: canonical leverage tiers, scale, OI-peak threshold, trading lifecycle, and execution rules are not fully established by the public description.
- `not independently reproduced`: no internal reproduction was performed in this Scout cycle.
- `data gap`: historical point-in-time intrabar OI and independent liquidation-event data may be difficult to source consistently across venues.
- `model risk`: inferred side and liquidation prices are proxies, not account-level positions or exchange liquidation prices.
- `visualization risk`: retrospective repainting of accumulated level intensity can create severe look-ahead if chart pixels/final states are used directly.
- `parameter risk`: leverage assumptions can move projected liquidation levels materially.

## Implementation status

Research record only. No implementation, Qlib full backtest, survivor validation, paper trading, testnet, or live-trading verification has been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitability, or received Paper/Testnet/Live approval.

## Related Wiki records

No Hermes Wiki lookup was performed because this Scout is GitHub-only. GitHub repository neighbors include multi-exchange OI anomaly/liquidation-zone and aggregated OI/volume-delta/liquidation-absorption research families; this record is retained only for the materially distinct persistent leverage-conditioned projected price-level distribution described above.

## Sources

- TradingView — victhoreb, **Liquidation Heatmap Proxy [victhoreb]**: https://www.tradingview.com/script/d2LdGqQO-Liquidation-Heatmap-Proxy-victhoreb/ (published 2025-08-06; updated 2025-08-09; reviewed 2026-09-22).
