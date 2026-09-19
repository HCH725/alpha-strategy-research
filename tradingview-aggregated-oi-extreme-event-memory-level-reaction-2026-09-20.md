---
schema: strategy-research-record-v1
title: Aggregated OI Extreme-Event Memory-Level Reaction
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
  - https://www.tradingview.com/script/7EI5Bhe0-Open-Interest-Bubbles-BackQuant/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Aggregated OI Extreme-Event Memory-Level Reaction

## Provenance

- Public TradingView open-source script: **Open Interest Bubbles [BackQuant]** by BackQuant.
- TradingView publication date shown by the source: 2025-12-19.
- Stable public URL: https://www.tradingview.com/script/7EI5Bhe0-Open-Interest-Bubbles-BackQuant/
- Source reviewed as of 2026-09-20.
- The source states that it aggregates futures open interest across Binance, Bybit, OKX, Bitget, Kraken, HTX, and Deribit when data are available, normalizes selected OI measures, and can anchor horizontal levels at prices where extreme OI events occur.

## Economic mechanism

### Source-reported

The author describes unusually large normalized OI changes as positioning events that can reflect fresh leverage, forced liquidations, or aggressive de-risking. The script can preserve the event price as a horizontal “positioning memory” level. The author explicitly cautions that these levels are not support or resistance by themselves, but suggests that a later revisit may be informative: rejection can indicate that the historical positioning zone mattered, while passage without reaction can indicate that the event was transitional.

### Research interpretation

The falsifiable hypothesis is that an unusually large, point-in-time multi-venue OI event creates a price-conditioned positioning-memory state, and that a later first revisit of the frozen event price contains incremental information about short-horizon price response beyond ordinary price levels and OI shocks alone.

The economic interpretation is deliberately agnostic about direction. A positive OI shock can represent new long or short leverage, and a negative OI shock can reflect position closure or liquidation. Therefore the primary research object is **event-level reaction conditional on later revisit**, not a rule such as “OI up = bullish.” Rejection/reversal and acceptance/continuation are competing hypotheses.

## Signal

Source-supported components:

- Aggregate OI across enabled venues when the corresponding OI series exist.
- Select an OI source: delta, raw OI, delta percent, or raw-OI percent form.
- Normalize using ZScore, StdNorm, AbsZScore, AbsStdNorm, or no normalization.
- Trigger meaningful/extreme events using user-configurable base and extreme thresholds.
- Filter positive, negative, or both event sides.
- Anchor the event to one of HL2, close, open, high, low, or VWAP.
- Optionally retain a horizontal level at the anchor price.

The source does not define a canonical entry, exit, holding period, re-entry rule, position size, or universally preferred normalization/threshold combination. These are **underspecified**.

Research-proposed operationalization for falsification, not source-reported trading rules:

1. Use only information available at each completed bar to construct the aggregated OI series and trailing normalization.
2. Define an extreme OI event using a pre-declared trailing normalization and threshold; freeze the event timestamp, sign, normalized magnitude, venue set, and anchor price at formation.
3. Do not move the stored event price after formation.
4. Define the first subsequent revisit using a pre-declared price-distance tolerance and minimum separation from the event bar.
5. Measure forward signed return, absolute return, maximum favorable/adverse excursion, and probability of rejection versus acceptance over fixed horizons after that first revisit.
6. Test positive and negative OI events separately before considering pooled magnitude-only specifications.

All numerical revisit tolerances, trailing windows, thresholds, horizons, and response classifications introduced in research must be labeled `research-proposed` and selected without future information.

## Required data

- Crypto derivatives instruments with point-in-time open-interest history.
- Source-supported venues include Binance, Bybit, OKX, Bitget, Kraken, HTX, and Deribit, subject to symbol/data availability.
- Timestamp-aligned price OHLCV and OI series at the tested timeframe.
- Venue/instrument mapping sufficient to avoid summing incompatible contracts or duplicate representations.
- For USD aggregation, point-in-time conversion into a comparable dollar representation.
- VWAP data if VWAP is used as the anchor.
- Historical venue availability and missing observations must be represented point-in-time; do not backfill a venue into periods before its data were available.

## Execution assumptions

The source is primarily an indicator and does not specify a canonical execution model. Market/limit order choice, signal-to-order timing, fill assumptions, fees, spread, slippage, impact, funding, leverage, margin, latency, and partial fills are underspecified.

For research, any actionable variant should form the revisit/reaction signal only after the required bar information is observable and should execute no earlier than the next feasible price after signal formation. Cost and funding sensitivity must be included before interpreting a trading result.

## Evidence

### Source-reported

The source describes extreme normalized OI events as markers of large positioning changes and suggests that retained event-price levels can later serve as attention/reaction zones. It gives qualitative examples including clustered extreme events around breakout/retest zones, negative events near capitulation lows, and positive positioning build near resistance followed by unwind. No independently verified performance statistic is reported here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly states that event levels do not claim to be support/resistance by themselves. The source also notes incomplete OI availability across symbols/venues and fails rather than silently producing an aggregate when it cannot construct the series. Directional interpretation is intrinsically ambiguous because OI change does not identify long-versus-short initiation on its own. No independent evidence of predictive profitability was established during this Scout cycle.

## Falsification plan

1. **Event-level incremental value:** compare revisit responses at extreme-OI event levels against matched ordinary price anchors formed at random/non-event timestamps with similar volatility and distance-to-price distributions.
2. **OI-shock-only baseline:** compare the event-level/revisit state machine against trading or forecasting directly after the OI shock. If the stored price level adds no incremental information, reject the positioning-memory component.
3. **Price-structure baseline:** compare against recent swing high/low, VWAP, rolling support/resistance, and simple return-reversal controls. The hypothesis weakens if OI levels add no out-of-sample information.
4. **Multi-venue ablation:** compare the multi-venue aggregate with each sufficiently liquid single-venue OI series and leave-one-venue-out aggregates. Reject the aggregation claim if improvement is unstable or dominated by one venue.
5. **Signal-construction ablation:** separately test delta, delta-percent, raw-OI and raw-relative forms, and signed versus absolute normalization. Do not select the winner on the full sample.
6. **Reaction versus continuation:** predefine both rejection/reversal and acceptance/continuation outcomes. Do not assume the level's directional effect in advance.
7. **First-revisit discipline:** primary tests should use the first causally observed revisit; later revisits should be separate decay tests to avoid repeated-observation dependence.
8. **Placebo levels:** shift event anchors by matched ATR/percentage distances and randomize event timestamps within regime-matched blocks. A genuine event-price effect should exceed these placebos out of sample.
9. **Regime robustness:** test trend, range, high/low realized volatility, and OI expansion/contraction regimes separately.
10. **Costs and OOS:** require walk-forward/out-of-sample validation with fees, spread, slippage and funding where applicable. Reject or materially weaken the hypothesis if the effect disappears out of sample, is explained by ordinary price structure, or cannot survive realistic costs.

## Crypto portability

direct

The source is explicitly designed around crypto futures OI and names major crypto derivatives venues. Portability is nevertheless venue- and contract-sensitive: linear versus inverse contracts, quote currency, contract multipliers, symbol coverage, venue launches/delistings, 24/7 candle boundaries, and differing OI units can distort aggregation. USD conversion and timestamp alignment must be point-in-time.

## Limitations

- Not independently reproduced.
- Canonical trading rule is underspecified.
- OI does not reveal whether newly opened positions are net bullish or bearish.
- Historical multi-venue aggregation is vulnerable to survivorship and availability bias if current venue coverage is projected backward.
- Normalization window and event thresholds are user-configurable rather than source-established alpha parameters.
- Horizontal levels are a visualization/research primitive, not source-proven support/resistance.
- Revisit definitions and response horizons require research-proposed choices and therefore parameter-robustness controls.

## Implementation status

Research-only normalization of the public TradingView hypothesis. No implementation or backtest in the research stack has been completed.

## Adoption boundary

This record is research material only. It is not evidence of profitable alpha and is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain record is cited in this GitHub-only Scout cycle.

## Sources

- TradingView — BackQuant, **Open Interest Bubbles [BackQuant]**, public open-source script, published 2025-12-19, reviewed 2026-09-20: https://www.tradingview.com/script/7EI5Bhe0-Open-Interest-Bubbles-BackQuant/
