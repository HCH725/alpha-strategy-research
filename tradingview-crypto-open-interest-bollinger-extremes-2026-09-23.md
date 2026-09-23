---
schema: strategy-research-record-v1
title: TradingView Crypto Multi-Exchange Open-Interest Bollinger Extremes
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/fLsLSg9p-Open-Interest-Oscillator/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Crypto Multi-Exchange Open-Interest Bollinger Extremes

## Provenance

Public TradingView open-source indicator **Open Interest Oscillator** by `mezor13`, originally published 2024-01-04 and updated 2024-03-17. Stable source URL: https://www.tradingview.com/script/fLsLSg9p-Open-Interest-Oscillator/ . Reviewed 2026-09-23.

The source describes aggregation of crypto open-interest data across multiple exchanges, including Binance, BitMEX, Bitfinex and Kraken, with an oscillator based on changes in open interest and a standard-deviation/Bollinger-band layer. The 2024-03-17 release added alerts for crossings of upper and lower channel boundaries in either direction.

## Economic mechanism

### Source-reported

The author interprets positive oscillator bars as leveraged positions being opened and negative bars as positions being closed. The Bollinger-band layer is intended to contextualize unusually large open-interest changes relative to their recent distribution. The source presents the tool as a way to assess leverage, market activity, volatility and momentum across crypto pairs.

### Research interpretation

Falsifiable hypothesis: an extreme standardized change in aggregate multi-exchange open interest may identify unusually rapid leverage accumulation or deleveraging. Subsequent crypto returns and volatility may differ after an upper- or lower-band crossing because crowded leverage can amplify continuation while forced deleveraging or leverage saturation can produce reversal. Direction is therefore not assumed ex ante; continuation and mean-reversion variants must be tested separately.

The potentially distinct information is **multi-exchange aggregate OI-change extremeness**, not raw price momentum and not funding-rate crowding.

## Signal

Source-supported construction:

- aggregate open-interest information from multiple crypto exchanges/pairs;
- transform open-interest changes into oscillator bars, with negative values representing positions closing and positive values representing leveraged positions opening according to the author's interpretation;
- apply a standard-deviation/Bollinger-band channel to the open-interest-change oscillator;
- detect crossings of upper and lower channel boundaries in either direction.

The public description does not unambiguously specify the exact aggregation weights, normalization formula, Bollinger lookback, standard-deviation multiplier, default threshold values, bar-close timing, entry/exit mapping, holding period, re-entry rule, position sizing, or whether each supported venue contributes identically for every symbol. These are **underspecified** and must not be inferred.

`research-proposed`: after source-compatible reconstruction, test four event definitions independently: upper-band breakout, upper-band re-entry, lower-band breakdown, and lower-band re-entry. Evaluate both forward-return direction and forward realized volatility over fixed horizons rather than assuming that every extreme is a reversal signal.

## Required data

- Crypto spot/perpetual price OHLCV for the tested instrument.
- Point-in-time open-interest series from the exchanges represented in the reconstruction; source explicitly names Binance, BitMEX, Bitfinex and Kraken among its aggregation inputs.
- Exchange/symbol mapping and unit normalization sufficient to prevent summing incompatible contract, coin and notional units.
- Timestamp alignment across venues and price bars.
- Point-in-time availability timestamps for OI observations; no use of revised or future values.
- Missing-venue policy for listings, delistings, feed outages and unsupported pairs.

The exact TradingView feed identifiers and aggregation implementation are a **data gap** in the reviewed page description.

## Execution assumptions

The source does not specify an executable trading lifecycle. Same-bar fills, next-bar fills, order type, fees, spread, slippage, impact, leverage, margin, funding, partial fills and failure handling are all unspecified.

`research-proposed`: form a signal only after all constituent OI observations required for that bar are available, then evaluate tradable variants from the next eligible bar. Apply venue-appropriate fees, spread/slippage and perpetual funding when the test instrument is a perpetual contract.

## Evidence

### Source-reported

The source describes the indicator's construction and interpretation but does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate or other performance statistic that should be treated as evidence of profitability. No such figure is inferred here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The reviewed source provides no independent validation that Bollinger extremes in OI predict return direction. Aggregate OI can also change because of venue migration, contract specification differences, listings/delistings, collateral changes or feed coverage rather than a common economic shock. None identified beyond these structural concerns in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct the source-compatible aggregate OI-change oscillator without forward filling unavailable venue data across signal timestamps.
2. Compare multi-exchange aggregation against single-venue OI change and simple aggregate OI percentage change. Reject the aggregation layer if it adds no stable out-of-sample information.
3. Compare Bollinger-band extremes against raw OI-change z-score/percentile baselines. Reject the channel transformation if it adds no incremental information.
4. Test upper/lower breakout and re-entry events separately; do not choose reversal versus continuation direction using the full sample.
5. Control for contemporaneous and lagged price return, realized volatility, trading volume and, where available, funding. The OI signal should retain incremental predictive content after these controls.
6. Stress plausible lookback and band-width neighborhoods rather than selecting one historically optimal pair.
7. Use walk-forward/out-of-sample evaluation across bull, bear, sideways, high-volatility and deleveraging regimes, with venue-coverage stability checks.
8. Run timestamp-delay/placebo tests to detect accidental use of OI values not actually available at signal formation.
9. Apply realistic costs and funding for executable variants. If apparent alpha disappears under conservative costs, treat the trading hypothesis as falsified even if the descriptive regime relationship survives.
10. If only one exchange or one isolated market regime carries the result, reject the claimed multi-exchange structural interpretation.

## Crypto portability

`direct` — the cited TradingView source is explicitly designed for cryptocurrency markets and crypto open interest.

Portability across venues remains nontrivial because OI units, contract types, collateral, settlement, listing history, funding conventions and data availability differ. A normalized aggregate must not silently mix contracts with incompatible units.

## Limitations

- `underspecified`: exact source aggregation weights/formula, Bollinger parameters, thresholds and trading lifecycle are not fully exposed by the reviewed description.
- `data gap`: exact historical TradingView OI feed identifiers and point-in-time venue coverage require reconstruction before testing.
- `not independently reproduced`.
- `unproven`: no claim is made that OI extremes predict reversal, continuation or profitability.
- Cross-venue OI aggregation is sensitive to unit normalization and changing venue coverage.
- The source's interpretive labels for positions opening/closing do not identify trader direction; OI alone does not reveal whether new exposure is net bullish or bearish.

## Implementation status

Research-only. No implementation in the research stack, Qlib full backtest, frozen-survivor validation, Paper, Testnet or Live verification has been completed.

## Adoption boundary

This record is normalized external research material only. Its presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor, is profitable, or is approved for implementation, Paper, Testnet or Live trading.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was resolved or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView, `mezor13`, **Open Interest Oscillator** (public open-source indicator), published 2024-01-04, updated 2024-03-17, reviewed 2026-09-23: https://www.tradingview.com/script/fLsLSg9p-Open-Interest-Oscillator/
