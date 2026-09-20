---
schema: strategy-research-record-v1
title: OI-Flow and Spot-Perpetual Participation Regime
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
  - https://www.tradingview.com/script/Rq4tIneq-Smart-OI-Color-Read-CBDelta/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# OI-Flow and Spot-Perpetual Participation Regime

## Provenance

Public TradingView open-source indicator **Smart OI Color Read + CBDelta**, author/page identity `Marius-Gabriel`, stable URL https://www.tradingview.com/script/Rq4tIneq-Smart-OI-Color-Read-CBDelta/ . The page shows publication on May 19 and update on June 3; the page view reviewed on 2026-09-20 does not expose a year alongside those dates, so no year is inferred. Source reviewed as of 2026-09-20.

## Economic mechanism

### Source-reported

The source classifies derivatives participation from the joint direction of price and aggregated open interest: price up/OI up as new-long expansion, price down/OI up as new-short expansion, price up/OI down as short covering, and price down/OI down as long liquidation/deleveraging. It supplements ambiguous states with OBV slope, CVD slope and absorption context. A stronger short-squeeze state additionally requires rising price, falling OI, elevated relative volume and a large candle body relative to ATR.

The source also reports a Coinbase-versus-Bybit premium layer, `CBDelta = ((Bybit - Coinbase) / Coinbase) × 1000`, as contextual information for whether participation appears more spot-led or perpetual-led. The source describes spot-led movement as potentially healthier continuation and strong perpetual premium as possible leverage crowding; CBDelta does not directly determine its candle colors.

### Research interpretation

The falsifiable hypothesis is not that any individual color/state is intrinsically predictive. The research question is whether a causal **participation-state interaction**—price direction × OI direction, conditioned by aggressive-flow confirmation and spot/perpetual leadership—contains incremental information about subsequent return direction, continuation probability, reversal probability, or realized volatility beyond price momentum, OI change, flow, and venue premium used separately.

A particularly testable mechanism is that price/OI expansion confirmed by same-direction CVD/OBV and spot leadership represents broader participation and should persist more reliably, while price moves dominated by OI contraction or perpetual leadership may be more vulnerable to exhaustion or reversal. These are research interpretations, not source-verified alpha.

## Signal

Source-described state variables:

- Price up + OI up: new-long / bullish participation expansion.
- Price down + OI up: new-short / bearish participation expansion.
- Price up + OI down: short covering.
- Price down + OI down: long liquidation / deleveraging.
- Stronger short-squeeze context: price up + OI down + elevated relative volume + strong candle body relative to ATR.
- Ambiguous OI states may be classified using OBV slope, CVD slope and absorption context.
- CBDelta compares Bybit and Coinbase prices and is used as contextual spot-versus-perpetual participation information.

The source does not specify a standalone entry, exit, holding period, re-entry rule, position sizing rule, canonical OI aggregation threshold, relative-volume threshold, ATR-body threshold, CVD/OBV slope lookback, absorption algorithm, or CBDelta decision threshold in the reviewed page text. Those elements are **underspecified** and must not be inferred as source rules.

Research-proposed operationalization for later testing only: construct point-in-time categorical states from contemporaneously available price/OI direction, then test incremental conditioning layers in sequence: CVD/OBV agreement, squeeze-strength variables, and CBDelta sign/rank. Use multiple forward horizons rather than selecting one ex ante from this source, because the source does not specify a holding horizon. Any concrete lookback, percentile, threshold, execution delay, or horizon introduced in implementation is `research-proposed`.

## Required data

- Crypto instruments with reliable derivatives OI and corresponding price history.
- Aggregated or venue-level open interest with timestamped point-in-time availability.
- OHLCV for price direction, relative volume and ATR/body measurements.
- CVD or aggressor-side trade data; if CVD is approximated from lower-timeframe bars, that approximation must be documented and tested separately.
- OBV inputs and the exact causal slope construction used in implementation.
- Coinbase spot and Bybit price series for CBDelta, with synchronized timestamps and explicit market-type/symbol mapping.
- Venue availability metadata because aggregated OI coverage can change across assets and time.
- Consistent UTC timestamps and explicit candle-boundary rules for 24/7 crypto markets.

## Execution assumptions

The source is a participation-analysis indicator, not a standalone trading system, and does not provide an execution model. Signal-to-order timing, next-bar versus same-bar execution, order type, fees, spread, slippage, market impact, funding, leverage, margin, latency, partial fills and failure handling are unspecified.

Any later backtest must form the signal only after all component observations for the decision timestamp are available and execute no earlier than the first causally available price. Intrabar states must not be treated as final before bar close unless an explicit event-time implementation is tested; the source warns that intrabar candle colors can fluctuate.

## Evidence

### Source-reported

The source describes the participation classifications and their intended interpretations but does not report a traceable backtest, Sharpe ratio, CAGR, win rate, drawdown, or other verified performance statistic on the reviewed page. It explicitly states that the indicator is intended for positioning/participation analysis rather than as a standalone trading system.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly notes that aggregated OI depends on exchange-data availability, OI alone does not determine direction, funding/OI/CVD/price can diverge in volatile conditions, CBDelta can behave differently across timeframes, and intrabar classifications can fluctuate before the candle is complete. These are material risks to treating the visual state labels as stable causal signals.

No independent negative-result study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Build leakage-safe point-in-time states and test forward returns and realized volatility across multiple predeclared horizons.
2. Run nested ablations: price direction only → + OI direction → + CVD/OBV agreement → + relative-volume/ATR squeeze context → + CBDelta. Reject the composite-alpha claim if added layers do not improve OOS performance or calibration after costs.
3. Compare the four basic price/OI states against matched controls with the same price return, volatility and volume but randomized or matched OI direction.
4. Test whether spot-led versus perp-led conditioning adds information beyond the standalone Coinbase-Bybit spread/premium and beyond ordinary price momentum.
5. Separate continuation and reversal hypotheses. Do not label covering/liquidation states as reversal signals unless OOS evidence supports that direction.
6. Repeat with venue-level OI, aggregate OI and leave-one-venue-out aggregates to detect dependence on one exchange or changing data coverage.
7. Replace proxy CVD with true aggressor-side trade delta where available; materially disappearing effects weaken the mechanism.
8. Apply timestamp-shift/placebo tests to OI, CVD and CBDelta and audit all multi-venue timestamp alignment.
9. Evaluate fees, spread, slippage and perpetual funding where a tested rule trades perpetuals.
10. Require held-out time periods and materially different volatility/funding regimes. Failure to retain incremental OOS information after controls and realistic costs rejects the trading-use hypothesis even if state descriptions remain useful diagnostically.

## Crypto portability

`direct` — the cited source is explicitly designed around crypto derivatives positioning and Coinbase-versus-Bybit participation. Portability is nevertheless venue- and instrument-dependent. OI units, spot/perpetual symbol mapping, exchange outages, fragmented liquidity, stablecoin basis, funding regimes and candle boundaries can change the measured state.

## Limitations

- `underspecified`: no complete trading rule or holding horizon is provided by the source.
- `not independently reproduced`: no Scout backtest or independent replication was performed.
- Aggregated OI composition may vary with TradingView data availability.
- Price-direction × OI-direction labels are interpretations of positioning mechanics, not direct identification of individual traders' positions.
- OBV/CVD/absorption classification details are not fully specified in the reviewed page text.
- CBDelta is a two-venue relative-price measure and can reflect venue/stablecoin/microstructure differences as well as spot-versus-perpetual leadership.
- Intrabar state instability creates a material point-in-time/repainting-like usage risk if a backtest incorrectly assumes final-bar classifications were known earlier.

## Implementation status

Research-only capture. No implementation in the research stack, Qlib full backtest, frozen-survivor validation, or execution validation has been completed.

## Adoption boundary

This record is normalized external research material only. Its presence does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor or leaderboard entry, demonstrated profitable alpha, or received implementation, Paper, Testnet, or Live approval.

## Related Wiki records

No stable Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- Marius-Gabriel, **Smart OI Color Read + CBDelta**, TradingView open-source script: https://www.tradingview.com/script/Rq4tIneq-Smart-OI-Color-Read-CBDelta/ — reviewed 2026-09-20.
