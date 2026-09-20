---
schema: strategy-research-record-v1
title: Spot-vs-Perpetual Volume Momentum Leadership Divergence
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
  - https://www.tradingview.com/script/H7a405kd-Aggregated-Spot-vs-Perp-Volume-Change/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Spot-vs-Perpetual Volume Momentum Leadership Divergence

## Provenance

Public TradingView open-source script **Aggregated Spot vs Perp Volume (% Change)** by `mindyourbuisness`, published 2025-03-24. Stable source: https://www.tradingview.com/script/H7a405kd-Aggregated-Spot-vs-Perp-Volume-Change/ . Source reviewed as of 2026-09-20.

The source aggregates spot and perpetual volume across up to 12 exchanges and compares the one-bar percentage change of the two volume pools. Repository deduplication on current `main` found no record for this canonical TradingView source. A related existing record, `tradingview-bitcoin-spot-perpetual-volume-delta-divergence-2026-09-19.md`, studies estimated directional volume delta; this record is materially distinct because its signal is **relative spot-versus-perpetual volume growth/leadership**, not buy/sell volume delta.

## Economic mechanism

### Source-reported

The author states that spot markets represent actual asset trading while perpetual markets attract leveraged speculative activity. Comparing percentage changes rather than absolute volume makes the two pools directly comparable. A sharp rise in perpetual volume without a corresponding spot-volume rise is presented as evidence that perpetual markets are leading; the source suggests using such divergence with price to confirm trends or identify possible reversals.

### Research interpretation

Hypothesis: **the relative acceleration of spot and perpetual participation contains incremental information about the quality and likely continuation of a price move.** Spot-led participation may represent broader unlevered demand/supply, while perp-led participation may represent leverage-driven speculative flow that can either accelerate momentum or become fragile/exhausted.

The directional consequence is intentionally not assumed. Two competing hypotheses must be tested:

1. **Confirmation/continuation:** spot-volume momentum leading perp-volume momentum during a directional price move predicts stronger continuation than an otherwise similar perp-led move.
2. **Speculative acceleration:** perp-volume momentum leading spot-volume momentum predicts short-horizon continuation before any later reversal.
3. **Fragility/reversal:** extreme perp-over-spot volume acceleration predicts weaker subsequent returns or reversal because participation is disproportionately leveraged.

## Signal

Source-specified construction:

- Aggregate spot and perpetual volume for the selected crypto across supported exchanges.
- Spot volume is included only when a corresponding perpetual pair is available, to improve comparability.
- Volume may be expressed in coin units or USD; USD mode uses volume multiplied by spot price.
- For each bar and each market pool, compute:

  `volume_pct_change_t = ((volume_t - volume_{t-1}) / volume_{t-1}) * 100`

- Compare spot-volume percentage change with perpetual-volume percentage change. A divergence where perp percentage change rises sharply without spot confirmation is explicitly described by the source as perp leadership.

The source does **not** define a canonical numeric divergence threshold, price-trend definition, entry, exit, holding period, re-entry rule, position sizing, stop, or take-profit. Those items are `underspecified`.

Research-proposed operationalization for falsification only: define `leadership_t = perp_volume_pct_change_t - spot_volume_pct_change_t`, evaluated only after bar close. Test the continuous value first; any percentile threshold, winsorization, smoothing, or event bucket introduced later must be fitted using past data only and labeled `research-proposed`.

## Required data

- Crypto spot and perpetual-futures/perpetual-swap volume.
- Source-listed venues: Binance, Bybit, OKX, Coinbase, Bitget, MEXC, Phemex, BingX, WhiteBIT, BitMEX, Kraken, and HTX, subject to actual pair availability.
- Pair mapping that prevents mixing different base assets or contract identities.
- Bar OHLCV for the traded instrument and corresponding spot/perpetual feeds.
- Coin-denominated and/or USD-normalized volume as robustness variants.
- Point-in-time venue/pair availability; do not backfill present-day listings into historical periods.
- Consistent bar timestamps and candle boundaries across venues.
- Missing-feed handling must be explicit; a changing venue set can mechanically alter aggregated volume.

## Execution assumptions

The source is an indicator, not an executable strategy, and does not specify execution mechanics.

For research, signal formation must use completed bars and any trade response must occur no earlier than the next executable observation. Market/limit order choice, fill model, fees, spread, slippage, impact, funding, leverage, margin, latency, partial fills and failures are all `underspecified` and must be modeled before any performance claim.

## Evidence

### Source-reported

The source explains the construction and suggests that spot/perp volume divergences can reveal which market is leading a move. It provides no independently audited backtest, Sharpe ratio, CAGR, drawdown, win rate, or other performance statistic.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No direct negative empirical result is reported on the source page. However, one-bar volume percentage change is mechanically unstable when prior-bar volume is small, venue coverage can change through time, and volume leadership may simply proxy contemporaneous volatility or price momentum rather than provide incremental alpha. Absence of source-reported negative evidence is not evidence of no negative result.

## Falsification plan

1. Build point-in-time aligned spot and perpetual aggregate volumes with explicit venue coverage and no future listing information.
2. Test the continuous `perp %Δ volume - spot %Δ volume` leadership variable before selecting thresholds.
3. Condition on contemporaneous price direction and compare three competing outcomes: continuation, later reversal, and volatility-only/no directional edge.
4. Ablate `price-only -> total-volume-change -> spot-volume-change -> perp-volume-change -> spot/perp leadership interaction`. Reject the incremental-alpha interpretation if leadership does not improve out-of-sample directional information beyond simpler controls.
5. Compare equal venue sets, single-venue variants, and leave-one-venue-out aggregates. A result dominated by one venue materially weakens the cross-market mechanism.
6. Compare coin-denominated versus USD-normalized volume. A result that exists only under one denomination without a defensible mechanism is suspect.
7. Control for realized volatility, absolute return, ordinary relative volume, funding and open-interest changes where available. The leadership signal must not merely relabel a generic high-activity episode.
8. Stress prior-volume near-zero observations, outliers and missing venues. Any clipping/winsorization rule must be trained point-in-time.
9. Use walk-forward/out-of-sample evaluation across BTC, ETH and sufficiently liquid additional assets; do not infer cross-asset portability from BTC alone.
10. Apply realistic fees, spread, slippage and funding to any trading operationalization. Reject if gross predictability is too small or short-lived to survive execution costs.
11. Use placebo tests that randomly permute spot/perp leadership within matched volatility and time-of-day buckets. The real signal should exceed placebo distributions out of sample.

## Crypto portability

`direct`

The source itself is crypto-specific and explicitly compares crypto spot with perpetual markets. Portability across assets remains unproven. Venue fragmentation, 24/7 candle boundaries, contract denomination, stablecoin/USD differences, missing pairs, exchange-specific volume quality and changing market share can materially change the aggregate.

## Limitations

- `underspecified`: no canonical trading threshold, entry, exit, holding period or sizing rule.
- `not independently reproduced`.
- One-bar percentage change can explode when previous volume is very small.
- Aggregated volume can suffer composition drift when venues/pairs appear or disappear.
- TradingView feed semantics and historical availability must be audited before implementation.
- The source's market-leadership interpretation is a hypothesis, not verified causal evidence.
- Spot/perp leadership may be contemporaneous rather than predictive.

## Implementation status

Research record only. No implementation, backtest, robustness campaign, paper trading, testnet or live validation has been completed in our research stack.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply profitability, validated alpha, implementation approval, paper-trading approval, testnet approval or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

Repository-relative conceptual neighbor: `tradingview-bitcoin-spot-perpetual-volume-delta-divergence-2026-09-19.md` (directional volume-delta disagreement rather than relative volume-growth leadership).

## Sources

- TradingView — **Aggregated Spot vs Perp Volume (% Change)**, `mindyourbuisness`, published 2025-03-24, reviewed 2026-09-20: https://www.tradingview.com/script/H7a405kd-Aggregated-Spot-vs-Perp-Volume-Change/
