---
schema: strategy-research-record-v1
title: "Crypto Perpetual OI-RSI Fractal Divergence with Funding-Crowding Filter"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - crypto
  - perpetual-futures
  - open-interest
  - funding-rate
  - divergence
  - mean-reversion
  - tradingview
status: research-only
confidence: low
source_as_of: 2026-09-14
sources:
  - "RezzoRedPriest, 'Open Interest-RSI + Funding + Fractal Divergences', TradingView open-source script, published 2025-06-10, https://www.tradingview.com/script/f7cieOvx-Open-Interest-RSI-Funding-Fractal-Divergences/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual OI-RSI Fractal Divergence with Funding-Crowding Filter

## Provenance

- **Primary source:** RezzoRedPriest, "Open Interest-RSI + Funding + Fractal Divergences," TradingView open-source script, published 2025-06-10.
- **Stable public URL:** https://www.tradingview.com/script/f7cieOvx-Open-Interest-RSI-Funding-Fractal-Divergences/
- **Source type:** Public TradingView open-source indicator / research implementation.
- **Source/as-of:** Page and published signal description reviewed on 2026-09-14.
- **Author/page identity:** TradingView author `RezzoRedPriest`; script title and public URL preserved above.
- **Primary-source verification:** The public TradingView source page was read directly. Its published description specifies the OI-RSI construction, fractal-divergence conditions, funding filter semantics, default inputs, intended instruments/timeframes, confirmation lag, and non-repainting claim. This record does not reproduce or republish the Pine source code.
- **Repository deduplication:** No existing record contains TradingView source ID `f7cieOvx` or the exact OI-RSI + fractal-divergence construction. Materially related records exist, including `crypto-perp-aggregated-oi-volume-delta-conviction-filter-2026-09-14.md`, `crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11.md`, and `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`. The incremental element here is the **price-vs-open-interest momentum divergence** construction: price makes a new fractal extreme while RSI computed on open interest fails to confirm it, with funding used as a crowding gate rather than as the primary standalone signal.

## Economic mechanism

### Source-reported

The source combines three state variables intended to identify leveraged-positioning exhaustion in cryptocurrency perpetual futures:

1. **OI-RSI:** RSI is computed on the open-interest series rather than price. The author describes it as measuring conviction behind position changes rather than conventional price momentum.
2. **Fractal divergence:** A bearish setup occurs when price makes a higher high while OI-RSI makes a lower high; a bullish setup occurs when price makes a lower low while OI-RSI makes a higher low.
3. **Funding context:** Funding indicates which side pays to maintain leveraged exposure. An optional filter removes long signals when funding is above the configured buy threshold and removes short signals when funding is below the configured sell threshold.

The author frames the combined signal as an exhaustion / potential mean-reversion detector: price extends to a new swing extreme, but leveraged participation measured through OI momentum does not confirm the move; funding can additionally identify whether crowding is already biased toward the direction being faded.

### Research interpretation

The falsifiable mechanism is **non-confirmation of price expansion by incremental leveraged participation**. A new price high accompanied by weaker OI momentum can indicate that the move is being sustained by position closing, thinner marginal participation, or spot-led flow rather than fresh derivative leverage. Conversely, a new price low with improving OI momentum can indicate diminishing short-side participation. If the divergence reflects exhaustion rather than structural information arrival, subsequent returns should mean-revert relative to matched price-extreme events without OI divergence.

Funding is best treated as a conditioning variable, not independent proof of reversal. The repository already contains negative evidence that simple funding-rate fade rules and generic CVD divergences can fail out of sample or after costs. Therefore this record does **not** infer that negative funding is automatically bullish or positive funding automatically bearish; the incremental hypothesis is specifically whether funding-conditioned OI-RSI divergence adds predictive information beyond price-only fractal reversals and beyond standalone OI/funding features.

## Signal

### Source-reported signal construction

- **Instrument domain:** Liquid cryptocurrency perpetual-futures charts, explicitly including BTC, ETH, and major Binance contracts.
- **Recommended timeframes:** 15-minute to 4-hour for intraday use; 1-day and above for swing use.
- **OI transform:** Load the chart-compatible `_OI` series and compute RSI on open interest.
- **OI-RSI length:** 14 by default.
- **Reference levels:** High-OI level 70 and Low-OI level 30 by default.
- **Fractal period:** `n = 2` by default, meaning a swing requires left- and right-side confirmation bars around the candidate pivot.
- **Fractals compared:** Default 3 historical swings.
- **Bearish divergence:** price forms a higher high while OI-RSI forms a lower high.
- **Bullish divergence:** price forms a lower low while OI-RSI forms a higher low.
- **Funding filter:** optional. With the filter enabled, a long signal requires funding below the configured Buy threshold; a short signal requires funding above the configured Sell threshold. Both defaults are `0.00%` raw funding.
- **Funding modes:** source permits FR, Avg Premium, Premium Index, Avg Prem + PI, or FR-candle representations. A lower-timeframe option can average 1-minute premiums.
- **Confirmation / repainting:** the source states divergences confirm only after `n` right-side bars and that signals do not repaint after confirmation. Therefore the actionable availability timestamp is the close of the confirmation bar, not the historical pivot bar on which an arrow may be visually overlaid.

### Execution-layer status

The TradingView source is an **indicator**, not a complete `strategy()` execution system. It does not source-report order type, position sizing, stop, profit target, maximum holding period, opposite-signal precedence, pyramiding, or overlapping-position handling. Those fields are therefore **underspecified** by the source and must not be upgraded into source-reported facts.

For future falsification only, a minimal causal test harness may use the following `research-proposed` conventions, to be preregistered before any backtest:

- Observe the signal only after the right-side fractal confirmation bar closes.
- Enter at the next bar open after confirmation, one position at a time.
- Evaluate fixed forward horizons of 1, 4, and 12 bars rather than optimizing a bespoke exit.
- Separately test an opposite-confirmed-divergence exit as an exploratory robustness arm.
- No pyramiding; if a new same-direction signal appears while exposed, ignore it in the baseline arm.

These conventions are deliberately simple and are **not** part of the TradingView author's source-reported rule.

## Required data

- **Market type:** Cryptocurrency perpetual futures.
- **Price fields:** OHLC timestamps sufficient to form causal fractal highs/lows.
- **Open interest:** Symbol-compatible historical OI series used to calculate OI-RSI.
- **Funding / premium:** Funding Rate and/or Premium Index according to the selected source mode; optional 1-minute premium data when lower-timeframe averaging is enabled.
- **Point-in-time discipline:** A fractal pivot is unavailable until `n` bars to its right have completed. Historical arrows plotted on the pivot bar must never be treated as tradable at the pivot timestamp.
- **Missing data:** The source states that some symbols lack OI or funding history and the script stops when required series are unavailable. Binance Premium Index history begins only around mid-2020 according to the source.
- **Venue mapping:** Exact OI/funding ticker mapping is TradingView-feed dependent and must be frozen in any reproduction. Cross-venue OI aggregation is not source-reported.

## Execution assumptions

- The source provides alerts and visual arrows, not a complete fill model.
- Fees, spread, slippage, market impact, funding cash-flow accounting over the holding interval, leverage, liquidation buffer, and margin mode are **not source-reported**.
- Any future test must model fees and slippage separately from the funding variable used as a signal filter; using funding as a predictor does not remove the economic funding cash flow from realized PnL.
- Because signals are confirmed after right-side fractal bars, execution must occur no earlier than the first tradable price after confirmation.
- Capacity is expected to be highest in BTC/ETH major perpetuals and lower in altcoin contracts, but no source-reported capacity analysis is available.

## Evidence

### Source-reported

- The source publicly documents the composite OI-RSI / funding / fractal-divergence rule and publishes it as an open-source TradingView indicator.
- Default parameters reported by the source include OI-RSI length 14, high/low levels 70/30, fractal period 2, three prior fractals to compare, and funding thresholds of 0.00%.
- The author states that confirmed signals do not repaint after the required right-side fractal bars have closed.
- The source recommends use on liquid perpetual futures and identifies missing OI/funding history as an explicit limitation.
- The source publishes **no backtested Sharpe ratio, CAGR, win rate, maximum drawdown, transaction-cost result, sample-period performance table, or out-of-sample result**. No profitability statistic is preserved in this record.

### Independently reproduced

not independently reproduced

### Negative evidence

- The primary TradingView source provides no empirical performance evidence, no transaction-cost study, and no out-of-sample validation.
- Existing repository evidence materially weakens naive extrapolation from the components: `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` reports CVD divergence sign instability and a null funding-rate fade over a multi-year sample, showing that derivative-crowding indicators can look intuitive yet fail as standalone alpha.
- `crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11.md` documents that funding-based signals require execution and regime filters and explicitly notes OI divergence as a separate, incompletely specified strategy family rather than established evidence.
- Fractal divergences are delayed by construction: with `n=2`, a displayed pivot signal is known only two bars later, so naive backtests that enter on the plotted pivot bar would contain look-ahead bias.
- Funding sign is not a stable causal label for direction; positive funding can persist for extended trending periods and negative funding can persist during deleveraging, so a simple contrarian interpretation may fade strong trends prematurely.

## Falsification plan

1. **Causal timestamp / repaint audit**
   - Data: BTCUSDT and ETHUSDT perpetual 15m, 1h, and 4h bars with point-in-time OI and funding/premium data.
   - Test: reconstruct each fractal signal and timestamp it only when all `n` right-side bars exist.
   - `research-defined falsification threshold`: if more than 1% of reproduced historical signals require information unavailable at the declared confirmation close, reject the implementation as leakage-contaminated.
   - Action: discard contaminated results and fix signal availability before any performance analysis.

2. **Incremental-predictability ablation**
   - Compare: (a) price fractal reversal alone, (b) price + OI-RSI divergence, (c) price + OI-RSI + funding filter, and (d) funding filter alone.
   - Metric: net forward return, hit rate, and bootstrap confidence interval at 1/4/12-bar horizons.
   - `research-defined falsification threshold`: if arm (b) does not improve net expectancy versus price-only fractals, the OI-divergence contribution is unsupported; if arm (c) does not improve arm (b), the funding filter adds no measurable value.
   - Action: retain only components with incremental OOS contribution; otherwise classify the composite as redundant indicator stacking.

3. **Walk-forward out-of-sample test**
   - Use expanding or rolling chronological folds with all thresholds frozen before each test fold.
   - `research-defined falsification threshold`: reject broad alpha if median OOS net expectancy is non-positive or if fewer than 60% of folds have the same expectancy sign as the full sample.
   - Action: keep research-only and classify as regime-fragile.

4. **Parameter-neighborhood stability**
   - Perturb OI-RSI length 10/14/21, fractal period 2/3/4, compared swings 2/3/5, and funding thresholds around zero without selecting post-hoc winners.
   - `research-defined falsification threshold`: reject parameter robustness if positive OOS expectancy exists only at one narrow parameter cell or fewer than half of neighboring cells retain the same sign.
   - Action: classify as sample-sensitive / overfit.

5. **Funding-threshold placebo**
   - Replace the funding gate with randomly time-shifted funding values and with sign-preserving shuffled funding blocks matched by volatility regime.
   - `research-defined falsification threshold`: if the real funding-conditioned uplift does not exceed the 95th percentile of placebo uplifts, reject the claim that contemporaneous funding crowding adds information.
   - Action: remove funding from the hypothesized alpha mechanism.

6. **OI placebo / competing explanation**
   - Compare OI-RSI divergence against price RSI divergence and against generic price momentum exhaustion matched on pivot amplitude and realized volatility.
   - `research-defined falsification threshold`: if OI-RSI does not outperform matched price-only exhaustion after costs, classify the effect as generic price mean reversion rather than leveraged-positioning information.
   - Action: weaken the OI-specific causal narrative.

7. **Venue and feed robustness**
   - Reconstruct on at least two independent liquid perpetual venues where comparable OI/funding history is available.
   - `research-defined falsification threshold`: weaken portability if net expectancy changes sign on the second venue or if more than 20% of signals differ solely because of feed-specific OI mapping.
   - Action: classify as TradingView-feed / venue-specific.

8. **Cost and funding-cash-flow stress**
   - Deduct realistic maker/taker fees, spread/slippage, and actual funding cash flows during each holding horizon.
   - `research-defined falsification threshold`: reject tradability if conservative net expectancy is non-positive under an ordinary non-VIP fee schedule or if gross edge is less than 2x median round-trip execution cost.
   - Action: keep as descriptive market-state indicator only.

9. **Regime breakdown**
   - Segment by realized volatility, trend strength, absolute funding, OI growth/decline, and liquidation-stress periods.
   - `research-defined falsification threshold`: reject broad robustness if all positive expectancy concentrates in a single regime representing less than 25% of signals.
   - Action: require a point-in-time regime gate before further research.

## Crypto portability

**direct, but venue/feed dependent**

The source is explicitly built for cryptocurrency perpetual futures and uses crypto-native derivatives variables (open interest and funding/premium). No cross-asset adaptation is required for the core hypothesis. Portability across crypto venues remains unproven because OI definitions, contract universes, funding formulas, premium-index construction, settlement cadence, and TradingView symbol mappings differ across exchanges.

## Limitations

- Indicator rather than complete trading strategy; exits, holding period, sizing, leverage, and fill rules are source-underspecified.
- No source-reported performance evidence or independent reproduction.
- OI is venue-specific and can fall because positions are closed on either side; OI direction alone does not reveal long-versus-short initiation.
- Funding is endogenous to premium and positioning and can remain extreme during persistent trends; it is not a clean exogenous sentiment variable.
- Fractal confirmation introduces unavoidable delay and creates severe look-ahead risk if chart arrows are interpreted at their visually plotted pivot timestamps.
- TradingView feed availability and symbol mapping may prevent exact historical reconstruction for some assets.
- No capacity, liquidation-risk, fee, or market-impact evidence is published by the source.

## Implementation status

- `not-implemented`
- No backtest was run in this Scout cycle.
- No quantitative runtime, Paper, Testnet, or Live workflow was modified.

## Adoption boundary

- `not-approved`
- `approval_scope: research-only`
- This record is staging research only. It does not authorize implementation, paper trading, testnet execution, or live deployment.
- Any future implementation requires an independent backtest/reproduction task and a separate adoption decision.

## Related Wiki records

- `[[quant/crypto-perp-aggregated-oi-volume-delta-conviction-filter-2026-09-14]]` — related OI-based positioning signal, but uses OI expansion plus signed volume-delta confirmation rather than price/OI momentum divergence.
- `[[quant/crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11]]` — related funding-crowding mean-reversion family and execution filtering.
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` — important negative evidence on CVD divergence and funding fades.
- `[[quant/positioning-based-btc-crowd-long-short-ratio-cascade-mechanism-2026-09-14]]` — related derivatives positioning/crowding mechanism using participant long/short ratios rather than OI-RSI divergence.

## Sources

1. RezzoRedPriest. "Open Interest-RSI + Funding + Fractal Divergences." TradingView open-source script. Published June 10, 2025. https://www.tradingview.com/script/f7cieOvx-Open-Interest-RSI-Funding-Fractal-Divergences/ . Reviewed 2026-09-14.
