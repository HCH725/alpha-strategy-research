---
schema: strategy-research-record-v1
title: TradingView Multi-Exchange Spot-Perpetual Basis Dislocation
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
  - https://www.tradingview.com/script/i7jzYIbJ-Spot-vs-Derivatives-Basis/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Multi-Exchange Spot-Perpetual Basis Dislocation

## Provenance

Public TradingView open-source indicator **Spot vs. Derivatives Basis** by **truenomic**, published 2025-07-28. Stable public URL: https://www.tradingview.com/script/i7jzYIbJ-Spot-vs-Derivatives-Basis/ . Source reviewed as of 2026-09-19.

The TradingView page states that the indicator computes basis between **average spot** and **average perpetual-futures** prices across user-selected exchanges, permits manual pair enable/disable control, supports SMA/EMA/WMA/VWMA smoothing, and highlights basis deviations beyond ±0.1%. The page tags Binance, Bitfinex, BitMEX, Bybit, Coinbase, Kraken, and OKX, but the public description does not unambiguously specify which exact spot/perpetual symbols are included by default or the averaging formula/weights. Those details therefore remain underspecified here.

## Economic mechanism

### Source-reported

The author presents spot-versus-perpetual basis deviations as context for funding pressure, arbitrage, or market dislocation. The indicator aggregates selected spot and perpetual prices before computing the basis and can flag deviations beyond ±0.1%.

### Research interpretation

The falsifiable hypothesis is that a **multi-venue spot-perpetual price dislocation** may contain incremental information about leveraged positioning or temporary segmentation between cash and derivatives markets. A sufficiently unusual positive or negative basis may either:

1. mean-revert as arbitrage capital closes the dislocation; or
2. persist/expand when leveraged demand is informative and derivatives lead spot.

The source does not establish which directional response dominates. Reversal and continuation must therefore be tested as competing hypotheses. The potentially distinct feature relative to a single-venue basis signal is the cross-venue aggregation: if aggregation suppresses venue-specific noise while retaining common derivatives pressure, it may be more robust; if it merely averages stale or heterogeneous prices, it may destroy information.

## Signal

Source-supported construction:

- Signal formation: basis is calculated from average spot and average perpetual-futures prices across selected exchange pairs.
- Pair selection: manually enable/disable specific pairs.
- Smoothing choices: SMA, EMA, WMA, or VWMA.
- Anomaly marker: basis deviations beyond ±0.1% are highlighted by the source.
- Exact basis equation/sign convention: **underspecified** in the public description.
- Exact venue symbols and averaging weights: **underspecified**.
- Smoothing lookback/default: **underspecified**.
- Canonical timeframe: **underspecified**.
- Long entry: **underspecified**.
- Short entry: **underspecified**.
- Exit: **underspecified**.
- Holding period: **underspecified**.
- Re-entry: **underspecified**.
- Position sizing: **underspecified**.

Research-proposed operationalizations, to be evaluated rather than assumed:

- Standardize the contemporaneous multi-venue basis using a strictly trailing rolling distribution and test extreme positive/negative observations.
- Test both mean-reversion and continuation responses at fixed forward horizons.
- Compare raw basis, source-style ±0.1% anomaly states, and standardized basis extremes without treating any threshold as validated alpha.

## Required data

- Crypto spot prices from the selected venues/pairs.
- Corresponding perpetual-futures prices from selected venues/pairs.
- Timestamped data with a common clock and explicit symbol/contract mapping.
- Sufficient history for any selected smoothing or research-proposed rolling normalization.
- Funding data is useful as a control/ablation but is not stated as an input to the source basis calculation.
- Point-in-time requirement: every constituent price must have been observable at signal formation; no forward-filled future observations or retrospective constituent substitutions.
- Venue outages, stale quotes, symbol migrations, delistings, contract specification differences, and missing legs must be handled explicitly rather than silently averaged.
- Exact source default pair set and weighting: **data/specification gap**.

## Execution assumptions

The source does not specify a canonical executable trading strategy.

- Signal-to-order timing: underspecified.
- Same-bar versus next-bar execution: underspecified.
- Market versus limit orders: underspecified.
- Fees, spread, slippage, impact, latency, partial fills: underspecified.
- Funding cash flows: not specified as part of an executable strategy and must be modeled if a perpetual position is tested.
- Delta-neutral arbitrage versus directional trading: source mentions arbitrage/dislocation context but does not define a trade construction.
- Shorting, leverage, margin, borrow, and collateral assumptions: underspecified.

Any later implementation must model costs separately for each executed spot/perpetual leg and venue.

## Evidence

### Source-reported

The source describes the indicator construction and interpretation but does not provide a traceable performance statistic, Sharpe ratio, CAGR, drawdown, win rate, or independently validated profitability claim on the reviewed public page. No such precision is inferred here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative backtest is identified on the reviewed page. Absence is not evidence of no negative result.

Material reasons the hypothesis may fail include asynchronous venue prices, stale constituent feeds, heterogeneous contract/index conventions, transaction costs, funding, and the possibility that basis primarily reflects carry/mechanical pricing rather than directional information.

## Falsification plan

1. **Point-in-time reconstruction:** reproduce each constituent with timestamp alignment and reject any implementation requiring future bars, retrospective symbol selection, or non-causal fill-forward.
2. **Single-venue baselines:** compare each venue's spot-perpetual basis against the multi-venue aggregate. The aggregation thesis is weakened if it adds no stable out-of-sample information.
3. **Simple controls:** compare against spot return momentum/reversal, perpetual return momentum/reversal, funding alone, and single-venue basis.
4. **Direction competition:** test mean-reversion and continuation at identical horizons after positive and negative basis extremes; do not choose direction after seeing the full sample.
5. **Component/aggregation ablation:** equal-weight versus liquidity-weighted aggregation (liquidity weighting is research-proposed), leave-one-venue-out tests, and raw versus smoothed basis.
6. **Threshold robustness:** test the source's ±0.1% anomaly state separately from research-proposed trailing percentile/z-score states; reject a thesis that survives only a narrow threshold.
7. **Horizon robustness:** predeclare multiple short/medium horizons and require consistent economic sign rather than selecting the best horizon ex post.
8. **Regime robustness:** bull/bear, high/low realized volatility, high/low funding, and venue-stress periods.
9. **Cost sensitivity:** include fees, spread, slippage, funding and, for multi-leg arbitrage variants, all legs and venues. Reject executable-alpha claims that disappear under plausible costs.
10. **Out-of-sample requirement:** freeze construction and thresholds before OOS evaluation. Material instability across venues or OOS windows weakens/rejects the hypothesis.

## Crypto portability

**direct** — the source itself is a crypto spot/perpetual basis indicator and identifies major crypto venues in its page metadata.

Portability risks remain substantial: venue fragmentation, different spot/perpetual symbol availability, quote-currency differences, contract/index conventions, funding schedules, 24/7 candle boundaries, exchange outages, stale feeds, and changing liquidity can alter the aggregate materially.

## Limitations

- The public description does not expose an unambiguous exact basis equation/sign convention.
- Exact default symbols, venue inclusion, averaging weights, smoothing lookback, and missing-data behavior are underspecified.
- The source provides an indicator/context signal, not a complete canonical entry/exit strategy.
- ±0.1% is source-reported anomaly highlighting, not independently validated alpha.
- Cross-venue averaging can create synchronization and stale-price artifacts.
- Funding pressure and arbitrage are source interpretations, not established causal mechanisms.
- Not independently reproduced.

## Implementation status

Research capture only. No implementation or backtest in the research stack has been completed for this record.

## Adoption boundary

This record is research material only. It is not evidence that the signal is profitable, validated alpha, approved for implementation, approved for paper/testnet use, or approved for live trading.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

Repository-level related research includes single-venue spot/perpetual basis and funding/carry records, but this record remains distinct because its primary hypothesis/data dependency is **multi-venue aggregation of spot-versus-perpetual basis**.

## Sources

- TradingView, truenomic, **Spot vs. Derivatives Basis**, public open-source script, published 2025-07-28, reviewed 2026-09-19: https://www.tradingview.com/script/i7jzYIbJ-Spot-vs-Derivatives-Basis/
