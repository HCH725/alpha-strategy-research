---
schema: strategy-research-record-v1
title: TradingView OI-Weighted Aggregated Funding Extremes
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/EiZmDJlt-Aggregated-Funding-Rate-for-Crypto-with-Alerts/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView OI-Weighted Aggregated Funding Extremes

## Provenance

Public TradingView open-source indicator, **Aggregated Funding Rate for Crypto with Alerts**, author/page identity `LuckSoon`. Stable source: https://www.tradingview.com/script/EiZmDJlt-Aggregated-Funding-Rate-for-Crypto-with-Alerts/ . Source reviewed as of 2026-09-19. The page describes aggregation of perpetual funding rates across Binance, Bybit, OKX, Bitget, and Coinbase, using open-interest weighting by default.

## Economic mechanism
### Source-reported

The source presents funding as a measure of leveraged positioning cost: positive funding means longs pay shorts and negative funding means shorts pay longs. It states that extreme funding can be associated with crowded positioning and may precede reversals or accelerations as leveraged positions are squeezed. Its distinguishing construction is to aggregate funding across venues with open-interest weights so venues with more capital at stake contribute more to the market-wide reading.

### Research interpretation

Hypothesis: a cross-venue, OI-weighted funding extreme may contain more useful information about market-wide leveraged crowding than a single-venue or equal-weight funding measure. The predictive direction is not assumed: extreme funding may support a contrarian reversal hypothesis, a continuation/squeeze hypothesis, or only a regime-conditioning signal. These alternatives must be tested rather than selected from hindsight.

## Signal

Source-supported construction:

- Obtain perpetual funding-rate observations for the charted base asset from up to five venues: Binance, Bybit, OKX, Bitget, and Coinbase.
- Obtain corresponding open interest where available.
- Aggregate valid venue funding rates using open-interest weighting by default; venues without the symbol/data are excluded.
- The source specifically notes that OKX OI is reported in USD and is converted using current price so units are comparable across venues.
- Identify funding that is moving sharply relative to its recent norm as a state worth investigating.

The public page does not provide, in the reviewed description, a unique numerical extreme threshold, a fully specified formation lookback, trade entry/exit Boolean, holding period, re-entry rule, or position-sizing rule. Those elements are **underspecified**.

Research-proposed operationalizations for later testing, not source-reported rules:

1. Standardize the point-in-time OI-weighted aggregate funding against its own trailing history and test symmetric positive/negative extreme thresholds.
2. Test both contrarian and continuation responses to an extreme; do not choose direction using the evaluation sample.
3. Compare the aggregate against equal-weight and individual-venue funding signals.

## Required data

- Crypto perpetual contracts for symbols supported across the relevant venues.
- Venue-level funding rates from Binance, Bybit, OKX, Bitget, and Coinbase where available.
- Venue-level open interest with consistent notional/unit normalization.
- Price needed where an OI feed must be converted to comparable units, as the source describes for OKX.
- Point-in-time timestamps for funding, OI, and conversion prices.
- Exact funding publication/prediction versus settlement status must be retained; do not use a later finalized value at an earlier decision timestamp.
- Missing venue observations must be represented point-in-time rather than backfilled using future availability.

## Execution assumptions

The source is an indicator and does not specify an executable trading model. Signal-to-order timing, order type, fills, fees, spread, slippage, impact, leverage, margin, funding cash-flow accounting, latency, partial fills, and failure handling are **underspecified**. Any later backtest must delay decisions until all constituent venue data used by the aggregate were actually observable.

## Evidence
### Source-reported

The source describes the OI-weighted cross-exchange aggregation and motivates extreme funding as leveraged-positioning context. No independently verified profitability, Sharpe, CAGR, drawdown, win rate, or other performance statistic is claimed here from the reviewed page.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself notes that funding-rate data availability and update frequency depend on TradingView's exchange feeds. Venue coverage can therefore vary by symbol and time. No independent evidence reviewed in this Scout cycle establishes that OI weighting is more predictive than equal weighting or the best single venue.

## Falsification plan

1. **Aggregation ablation:** compare OI-weighted funding with equal-weight aggregation and each major single venue using identical timestamps and signal thresholds. If OI weighting does not add stable out-of-sample information, reject the weighting thesis.
2. **Direction test:** predefine contrarian and continuation hypotheses separately. If neither survives OOS after costs, reject funding extremes as standalone directional alpha.
3. **Weighting integrity:** recompute weights using point-in-time, consistently normalized OI. Test whether results disappear when avoiding current-price/current-coverage leakage.
4. **Venue-dropout robustness:** repeat with leave-one-venue-out cohorts and periods of changing exchange coverage. Reject results driven by one venue or survivorship in available feeds.
5. **Extreme definition robustness:** test a bounded family of trailing standardization windows and thresholds, with parameters fixed before OOS evaluation. Reject narrow parameter islands.
6. **Settlement timing:** separate predicted/intraperiod funding information from finalized settlement values and ensure the backtest uses only values available at decision time.
7. **Costs:** include trading fees, spread/slippage and realized funding cash flows. Reject any directional implementation whose edge is not robust net of realistic costs.

## Crypto portability

direct

The source is explicitly built for cryptocurrency perpetual funding across major crypto venues. Portability remains venue- and contract-specific because funding intervals, symbol coverage, OI units, feed update times, mark/index conventions, and liquidity differ across exchanges.

## Limitations

- Signal direction and trading rules: **underspecified**.
- Exact historical-normalization lookback/threshold in the reviewed source description: **underspecified**.
- TradingView feed timing and revisions may differ across venues.
- OI normalization must be audited carefully; inconsistent coin/notional units can distort weights.
- A high OI weight measures exposure concentration, not necessarily informed positioning.
- Funding can remain extreme during persistent trends; an extreme is not automatically a reversal signal.
- Not independently reproduced.

## Implementation status

Research record only. No implementation or backtest in our research stack has been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`. Presence in this repository does not establish profitable alpha and does not authorize paper, testnet, or live trading.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was resolved or fabricated in this GitHub-only Scout cycle.

## Sources

- TradingView, `LuckSoon`, **Aggregated Funding Rate for Crypto with Alerts** (public open-source indicator), reviewed 2026-09-19: https://www.tradingview.com/script/EiZmDJlt-Aggregated-Funding-Rate-for-Crypto-with-Alerts/
