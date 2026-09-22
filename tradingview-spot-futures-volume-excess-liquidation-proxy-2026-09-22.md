---
schema: strategy-research-record-v1
title: TradingView Spot-Futures Volume-Excess Liquidation Proxy
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-03-26
sources:
  - https://www.tradingview.com/script/kPIEzGqV-Liquidations-by-volume-TG-fork/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Spot-Futures Volume-Excess Liquidation Proxy

## Provenance

- Public TradingView open-source indicator: `Liquidations by volume (TG fork)` by `tartigradia`.
- Stable source URL: https://www.tradingview.com/script/kPIEzGqV-Liquidations-by-volume-TG-fork/
- Published: 2022-11-30.
- Latest source-page update reviewed: 2023-03-26.
- The page states that this fork extends an earlier liquidation-by-volume idea, automatically detects supported Binance crypto symbols with a USDTPERP pair, and adds multi-timeframe support.
- Source/data as-of date for this record: 2023-03-26.

## Economic mechanism

### Source-reported

The author describes a liquidation proxy based on the difference between spot-market and futures-market volume. The stated rationale is that futures volume should become unusually large relative to spot volume when forced liquidations occur. The source labels the inferred direction so that short liquidations correspond to bullish movement and long liquidations to bearish movement. It also cautions that long-liquidation inference should theoretically be more accurate than short-liquidation inference because spot markets generally do not provide an equivalent shorting channel.

### Research interpretation

The falsifiable hypothesis is that an abnormal futures-volume excess relative to matched spot volume contains incremental information about forced deleveraging beyond price return and total volume alone. If the excess is genuinely liquidation-related rather than ordinary derivatives participation, it may identify either (a) continuation during an active cascade or (b) exhaustion/reversal after forced flow peaks.

These two horizons are competing hypotheses and must be tested separately rather than selected after observing results.

## Signal

### Source-supported construction

- Compare volume in a crypto futures market with volume in the corresponding spot market.
- Treat unusually greater futures activity relative to spot activity as a proxy for liquidation activity.
- Use price direction to distinguish inferred long-liquidation versus short-liquidation events.
- The fork automatically maps supported crypto assets to Binance USDTPERP pairs and supports multi-timeframe use.

The public description does not expose enough detail to reconstruct every numerical threshold, normalization step, exact spot symbol mapping, or full entry/exit lifecycle unambiguously. Those elements are `underspecified` and must not be invented.

### Research-proposed operationalization

For falsification only, construct a point-in-time matched spot/perpetual pair and measure normalized futures-volume excess using only information available at signal time. Test both a ratio/difference normalized by trailing history and a simple contemporaneous futures-versus-spot comparison. Condition the sign on contemporaneous price direction, then test separately:

1. **Cascade continuation:** extreme signed volume excess predicts same-direction returns over the next short horizon.
2. **Forced-flow exhaustion:** an extreme signed volume excess followed by normalization predicts opposite-direction returns.

Exact normalization window, extreme threshold, holding horizon, and re-entry rule are `research-proposed` parameters to be selected only through a predeclared training/validation procedure. They are not source-reported rules.

## Required data

- Matched crypto spot and perpetual/futures markets for the same base asset.
- Point-in-time OHLCV for both legs with identical timestamps and candle boundaries.
- Contract/symbol metadata sufficient to reconstruct the historically active Binance perpetual mapping rather than applying today's symbol universe backward.
- Timeframe must be identical across spot and futures legs; multi-timeframe tests require explicit bar-boundary alignment.
- Missing or delisted symbols must remain missing; do not forward-fill volume across unavailable periods.
- For validation of the proxy itself, independently sourced actual liquidation data is desirable where historically available.

## Execution assumptions

The TradingView source is an indicator rather than a complete executable strategy. It does not specify a complete signal-to-order timing rule, order type, fill model, fees, spread, slippage, market impact, leverage, margin policy, funding treatment, position sizing, or portfolio allocation.

Any backtest should therefore execute only after the bar containing all required spot/futures volume information has closed, unless a lower-frequency point-in-time reconstruction proves the information was available earlier. Same-bar fills using final bar volume would be look-ahead.

## Evidence

### Source-reported

The source states that the spot-versus-futures volume difference can be used to infer liquidation activity and that the indicator may help identify trends by locating liquidation events. No traceable Sharpe, CAGR, drawdown, win rate, or other strategy-performance statistic is reported on the reviewed public page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself makes clear that the construction is an inference rather than a direct liquidation feed. Ordinary speculative trading, market making, venue migration, contract changes, or differences in spot/futures volume units can also create futures-volume excess without forced liquidation. The stated asymmetry between inferred long and short liquidations is an additional structural caveat.

No independent negative empirical result specific to this exact TradingView construction was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct matched spot/perpetual volume point-in-time with identical quote/unit normalization and candle boundaries.
2. Compare against price-only, futures-volume-only, spot-volume-only, total-volume, and futures/spot-volume-ratio baselines.
3. Where actual liquidation prints are available, test whether the proxy materially predicts their sign and magnitude. Failure to identify real liquidation events weakens the mechanism before any return test.
4. Test cascade-continuation and post-spike-exhaustion hypotheses separately on predeclared horizons.
5. Run ablations for raw difference, ratio, trailing z-score/percentile normalization, and price-direction conditioning.
6. Slice by asset liquidity, bull/bear/high-volatility regimes, and periods surrounding contract/symbol changes.
7. Audit point-in-time venue availability and repeat with lagged signals plus timestamp-placebo shifts to expose accidental leakage.
8. Apply realistic fees, spread, slippage and perpetual funding. Intraday edge that disappears under conservative costs fails.
9. Require leakage-safe out-of-sample persistence across multiple assets and periods. If the normalized proxy cannot outperform the strongest simple volume/return baseline, reject the added spot-futures construction rather than adding filters.

## Crypto portability

`direct`

The source itself targets crypto assets and Binance perpetual/spot-style market structure. Portability is nevertheless venue- and contract-sensitive: volume units, quote currencies, perpetual funding, historical symbol availability, spot shorting asymmetry, 24/7 candle boundaries, and venue fragmentation can all alter the proxy.

## Limitations

- `underspecified`: exact numerical thresholds and complete symbol mapping are not fully recoverable from the public description reviewed here.
- `not independently reproduced`.
- This is a liquidation proxy, not an exchange liquidation feed.
- Futures-volume excess is not uniquely caused by liquidation.
- Historical Binance contract naming and availability require point-in-time reconstruction.
- Cross-market volume must be normalized into comparable units before subtraction or ratio formation.
- The source provides no complete trading lifecycle or independently verified performance evidence.

## Implementation status

Research record only. No implementation or Qlib full-backtest validation has been completed as part of this Scout cycle.

## Adoption boundary

This record is research material only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

- [[crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01]] — related liquidation-cascade mechanism, but based on taker-flow/variance rather than matched spot-futures volume excess.
- [[crypto-perp-aggregated-oi-volume-delta-conviction-filter-2026-09-14]] — related derivatives-participation/order-flow family; materially different construction and data dependency.
- [[tradingview-lower-timeframe-volume-imbalance-divergence-2026-09-22]] — related volume-pressure proxy, but reconstructed from lower-timeframe candle direction rather than spot-versus-futures excess.

## Sources

- TradingView, `Liquidations by volume (TG fork)`, tartigradia, published 2022-11-30, updated through 2023-03-26: https://www.tradingview.com/script/kPIEzGqV-Liquidations-by-volume-TG-fork/
