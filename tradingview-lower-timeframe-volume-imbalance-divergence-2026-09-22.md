---
schema: strategy-research-record-v1
title: "Lower-Timeframe Volume-Imbalance Divergence and Exhaustion"
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
  - https://www.tradingview.com/script/ZnjdMdIv-Long-Short-Ratio-BigBeluga/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Lower-Timeframe Volume-Imbalance Divergence and Exhaustion

## Provenance

- Public TradingView open-source script: **Long/Short Ratio [BigBeluga]** by `BigBeluga`.
- Stable source URL: https://www.tradingview.com/script/ZnjdMdIv-Long-Short-Ratio-BigBeluga/
- TradingView page displays publication date `Apr 6`; the year is not asserted because the reviewed public page does not display it unambiguously.
- Source reviewed as of 2026-09-22.
- The source calls the output a long/short ratio, but it is not exchange-reported positioning. It is reconstructed directional volume from lower-timeframe candles.

## Economic mechanism

### Source-reported

The source estimates buyer-versus-seller dominance inside each chart bar by sampling lower-timeframe volume. A lower-timeframe candle with `close > open` contributes its volume to buyer pressure; `close < open` contributes to seller pressure. Buyer and seller totals are converted to percentages. The author interprets agreement between price direction and Buy % as participation confirmation, price/ratio disagreement as possible weakness or absorption, and extreme imbalance as possible exhaustion or squeeze fuel.

### Research interpretation

The falsifiable hypothesis is that intrabar directional-volume composition contains information beyond the chart bar's OHLCV. Two competing mechanisms must be tested rather than assumed:

1. **Continuation:** rising Buy % and positive imbalance momentum during an advance identify genuine participation and predict short-horizon continuation; the symmetric condition applies to declines.
2. **Exhaustion / absorption:** extreme one-sided imbalance or divergence between price and Buy % identifies aggressive flow being absorbed and predicts reversal.

The classification is only a candle-direction proxy for aggressive flow. It must not be treated as true trade-side CVD without validation.

## Signal

Source-specified construction:

1. Select lower-timeframe bars automatically from the current chart timeframe using TradingView `request.security_lower_tf()`.
2. For each lower-timeframe bar:
   - `close > open` -> classify that bar's volume as buyer volume;
   - `close < open` -> classify that bar's volume as seller volume.
3. Aggregate buyer and seller volume inside the current chart bar.
4. Compute `Buy % = buyer volume / total classified volume` and the complementary Sell %.
5. `50%` is the balance reference.
6. A smoothed HMA of a user-defined change in Buy % represents dominance acceleration/deceleration.
7. Source default extreme marker: buyer or seller share above `80%`.
8. Source recommends use on `5-minute and higher` chart timeframes.

Source interpretations include rising price + rising Buy % as bullish participation, rising price + falling Buy % as weak-trend/divergence, falling price + rising Buy % as absorption, and extreme imbalance as a possible squeeze or exhaustion setup.

The source does not specify a complete executable strategy: exact divergence window, HMA/change defaults, entry timing, exit, holding period, re-entry, position sizing, and stop logic are underspecified.

**Research-proposed operationalization:** test the source components separately before combining them: (a) signed imbalance level around 50%, (b) change/HMA momentum, (c) price-versus-imbalance divergence, and (d) extreme `80%` states. Evaluate continuation and reversal labels independently across fixed forward horizons. No component should be presumed additive.

## Required data

- Crypto spot or derivatives OHLCV for the target instrument.
- Lower-timeframe OHLCV sufficient to reconstruct each parent chart bar without look-ahead.
- Exact parent/lower-timeframe boundaries and timezone.
- Point-in-time availability: only completed lower-timeframe observations available by the signal timestamp may enter a historical signal.
- Venue-specific volume; cross-venue portability is unproven.
- True trade/aggressor-side data is not required for the source reconstruction but is highly desirable as a validation control for the candle-direction proxy.

## Execution assumptions

The source does not specify an execution model.

For research, signal formation must be evaluated only after the parent bar's required lower-timeframe observations are complete; execution should therefore begin no earlier than the next executable observation unless a separate intrabar protocol is explicitly defined. Fees, spread, slippage, market impact, order type, leverage, funding, borrow, latency, partial fills, and capacity are unspecified and must be modeled independently.

## Evidence

### Source-reported

The TradingView author describes the indicator as useful for participation shifts, divergence, absorption, exhaustion and participation-driven breakouts, and recommends `5-minute and higher` chart timeframes. The source does not report a traceable Sharpe, CAGR, drawdown, win rate, or independent backtest result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The directional-volume classifier infers buy/sell pressure from lower-timeframe candle direction rather than actual aggressor-side trades. A green lower-timeframe candle can contain substantial aggressive selling and vice versa, so the proxy can misclassify order flow. The source also explicitly allows both breakout/continuation and exhaustion interpretations of extreme imbalance, making horizon and state definition critical.

No independent negative performance result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the signal without look-ahead on liquid BTC and ETH venues, then test additional liquid crypto only after the core result is stable.
2. Compare against parent-bar controls: return sign, close location value, volume, range/ATR, and ordinary price momentum. Reject the added lower-timeframe construction if it has no leakage-safe OOS incremental information.
3. Validate the candle-direction volume proxy against true aggressor-side trade delta where available. Measure sign agreement and predictive performance. Material proxy disagreement weakens the mechanism.
4. Ablate `imbalance level -> imbalance momentum -> price/imbalance divergence -> extreme threshold`. Do not retain components that fail independently.
5. Test continuation and reversal hypotheses separately at fixed forward horizons; do not choose the winning direction after inspecting the same OOS sample.
6. Sweep the `80%` extreme threshold and lower-timeframe mapping in broad neighborhoods. A result confined to one threshold or one parent/lower-TF pairing is evidence of fragility.
7. Run timestamp placebo / one-bar-delay tests and ensure incomplete lower-timeframe bars never leak into historical signals.
8. Test venue portability and leave-one-venue-out behavior because volume composition is venue-specific.
9. Apply realistic fees, spread and slippage. If any gross edge disappears under plausible round-trip costs, reject the trading hypothesis.
10. Failure action: if lower-timeframe imbalance does not improve OOS prediction or cost-adjusted performance over simple OHLCV controls, reject the added complexity rather than adding filters.

## Crypto portability

**direct** — the source explicitly targets market participation analysis and discusses crypto use; the construction can operate on crypto symbols with lower-timeframe volume. Portability remains venue-dependent because reported volume and microstructure differ across spot and perpetual markets, and 24/7 candle boundaries can alter aggregation.

## Limitations

- `underspecified`: no complete entry/exit/holding/sizing strategy is supplied.
- `not independently reproduced`.
- Candle-direction volume is a proxy, not authenticated aggressor-side order flow.
- Automatic lower-timeframe selection must be reconstructed exactly or treated as a research-proposed variant.
- Intrabar signals can be especially vulnerable to timestamp leakage if historical parent bars are built from information not yet available at decision time.
- Extreme imbalance has competing continuation and reversal interpretations.

## Implementation status

Not implemented in the research stack. No Qlib full backtest, survivor promotion, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

Research-only. Presence in this repository does not mean the record passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor, demonstrated profitability, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

## Sources

- TradingView, **Long/Short Ratio [BigBeluga]**, author `BigBeluga`, public open-source script, reviewed 2026-09-22: https://www.tradingview.com/script/ZnjdMdIv-Long-Short-Ratio-BigBeluga/
