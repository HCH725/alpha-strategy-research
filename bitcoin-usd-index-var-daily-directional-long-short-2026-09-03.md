---
schema: strategy-research-record-v1
title: "Bitcoin USD-Index VAR Daily Directional Long-Short"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - macro
  - vector-autoregression
  - directional-forecasting
status: research-only
confidence: high
source_as_of: 2024-02-23
sources:
  - "https://doi.org/10.1002/for.70077"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin USD-Index VAR Daily Directional Long-Short

## Provenance

Primary source: Rehan Arain, *When Are Statistical Forecast Gains Economically Relevant? Evidence From Bitcoin Returns*, *Journal of Forecasting* 45(3), 2026, pp. 1245–1260. First published 2025-12-17. DOI `10.1002/for.70077`.

The source studies 1,826 daily observations from 2017-02-23 through 2024-02-23. Its real-time forecast evaluation sample is 2021-10-01 through 2024-02-22. The focal record here captures the paper's **US Dollar Index + Bitcoin bivariate VAR, one-day-ahead directional forecast, daily long-short trading rule**.

Pool-level source-identity search found no record containing this DOI, exact paper title, or materially the same USD-index bivariate-VAR directional rule. A separate Wiki Brain search also returned no matching source record.

## Economic mechanism

### Source-reported

The paper argues that macro-financial information can contain incremental information for Bitcoin returns. For the US Dollar Index, the proposed channel is Bitcoin's role as a store-of-value / currency alternative whose returns may respond to changes in the dollar. The authors emphasize that average directional accuracy alone is insufficient: economically useful forecasts are those that remain accurate when market moves are large.

### Research interpretation

The falsifiable mechanism is delayed cross-asset macro information incorporation. Because the source aligns traditional-market closes before the Bitcoin daily close, a USD-index shock known before the Bitcoin trading decision may contain information not yet fully incorporated into BTC. A bivariate VAR can capture short-lag dynamics between the two series without requiring a large feature set.

This is a predictive relationship, not established causality. The effect may be proxying for broader risk-on/risk-off conditions, U.S. trading-hour liquidity, common macro shocks, or sample-specific covariance structure.

## Signal

Source-normalized focal specification:

1. **Instrument:** Bitcoin priced in U.S. dollars.
2. **Predictor:** US Dollar Index (`USD` in the paper).
3. **Frequency:** daily.
4. **Historical clock:** source predictive-index closes occur between 14:00 and 19:00 EST; Bitcoin's daily close is 19:00 EST. The source states this ordering is intended to ensure predictor information is available before Bitcoin trading decisions.
5. **Transform:** BTC and the USD Index are converted to growth rates for stationarity.
6. **Model:** estimate a bivariate VAR containing BTC and the USD Index.
7. **Lag selection:** choose VAR lag order `p` by Akaike Information Criterion (`AIC`).
8. **Forecast:** form a one-step-ahead BTC return forecast using information available through day `t`.
9. **Long entry:** if forecasted next-day BTC return is positive, hold a long BTC position for the next daily return interval.
10. **Short entry:** if forecasted next-day BTC return is negative, hold a short BTC position for the next daily return interval.
11. **Zero forecast:** source treatment is not explicitly described; mark **underspecified**. A reproduction must predeclare the zero-handling rule.
12. **Rebalance:** positions are reconsidered daily from the sign of the newest one-step-ahead forecast.
13. **Holding period:** one source-defined daily interval.
14. **Exit / flip:** source-normalized interpretation is to close or reverse when the next daily forecast changes sign. Exact trade timestamp and execution price are **underspecified** beyond the source's stated close-time ordering.
15. **Sizing:** source equations imply unit directional exposure; leverage and volatility targeting are not specified.
16. **Stops / take-profit:** none are source-reported.

Optional source branch, not the focal rule: the paper also studies a below-threshold long-short variant that trades only when the absolute real-time forecast is within an expanding-window forecast standard-deviation threshold. Any use of that filter should be treated as a separate branch rather than silently merged into this focal rule.

## Required data

- Bitcoin USD daily closing price.
- US Dollar Index daily closing level.
- Source-faithful timestamp convention matching the paper's traditional-market close and 19:00 EST Bitcoin close.
- Point-in-time daily observations with no future revisions leaking into the forecast.
- Sufficient pre-evaluation history to estimate the bivariate VAR and select lags with AIC.
- Exact calendar/session alignment across the predictor and Bitcoin series.
- Fees, spread, slippage, borrow/funding and executable price data for tradability testing.

Source data are primarily from Investing.com unless otherwise noted. The source states that the variables are available in real time. For a modern reproduction, vendor timestamp and revision history must still be independently audited.

Missing-data handling is **underspecified**. Do not silently forward-fill missing predictor observations.

## Execution assumptions

Source-reported:

- daily position adjustment;
- direction set by the sign of the next-day forecast;
- a simple transaction-cost robustness test using `0.2%` per active trade;
- no source-reported leverage or volatility targeting.

Underspecified:

- exact executable order timestamp relative to the 19:00 EST BTC close;
- venue and instrument used for the short leg;
- market vs limit orders;
- slippage / market impact;
- borrow availability or perpetual funding;
- latency and partial-fill handling.

A modern perpetual-futures implementation is **research-proposed** and is not source-faithful unless funding, mark/index mechanics, liquidation risk, venue availability and execution costs are modeled explicitly.

## Evidence

### Source-reported

The real-time forecast evaluation sample runs from 2021-10-01 through 2024-02-22.

For the USD-index bivariate VAR, Table 2 reports a directional success ratio of `0.526` with `p = 0.074`, significant at the source's 10% level but not at 5%. The same row reports an MSFE ratio of `1.019`, so the model does not improve squared forecast error relative to the random-walk benchmark.

For the daily long-short trading rule, Table 4 reports cumulative return of `146.35%` for the USD model and an Anatolyev-Gerko excess-profitability `p = 0.053` over the evaluation period. The paper states that the USD and Shanghai Stock Exchange predictors are the strongest performers in trading terms even though their mean directional-accuracy gains are modest.

Table 5 reports, for the USD strategy, `146%` gross cumulative return and `140%` net cumulative return under a constant `0.2%` fee per active trade. The source reports 305 trade days for that strategy. These are source-reported results, not independent verification.

The paper further reports that mean forecast accuracy does not reliably rank economic performance: several predictors with higher directional accuracy lose money, while the USD model performs strongly because its directional relationship is more stable across economically important moves.

### Independently reproduced

not independently reproduced

### Negative evidence

- The USD model's directional success ratio is only `0.526` and is not significant at the 5% level.
- Its MSFE ratio exceeds one, so it does not improve squared-error forecast accuracy over the random-walk benchmark.
- The evaluation period is short and ends in February 2024; post-2024 persistence is unproven.
- Reported trading costs use a flat `0.2%` fee per active trade rather than historical venue-specific spread, slippage, funding, borrow and market impact.
- Exact trade timestamp / fill price is underspecified, creating a potentially material close-to-close execution ambiguity.
- The source uses a U.S.-centric daily close convention in a 24/7 asset.
- None of the results in this record have been independently reproduced.
- No contrary replication was identified in the reviewed primary source; absence is not evidence of no negative result.

## Falsification plan

1. **Strict post-source OOS:** freeze the source-normalized specification and test on data strictly after 2024-02-22. **Research-defined falsification threshold:** reject continuation if net directional strategy return is `<= 0` over the locked OOS sample.
2. **Directional-value test:** require one-step-ahead success ratio to remain above `0.50`. **Research-defined falsification threshold:** reject directional predictability if OOS success ratio is `<= 0.50` and no economically significant tail-state accuracy remains.
3. **Excess-profitability test:** rerun an Anatolyev-Gerko-style test or a predeclared equivalent. **Research-defined falsification threshold:** reject economic predictability if the strategy fails to beat a sign-randomized benchmark after realistic costs.
4. **Leakage / timing audit:** verify every USD-index observation was public before the BTC execution timestamp. Any dependency on unavailable same-day data is an immediate failure.
5. **Clock perturbation:** test the source 19:00 EST convention against UTC and exchange-native daily cuts. Fail portability if the effect disappears under plausible causal clocks.
6. **Lag robustness:** perturb AIC-selected lag order within a narrow predeclared neighborhood and compare BIC. Fail if performance depends on one isolated lag specification.
7. **Competing explanation:** add simple BTC lagged return and broad risk-on/risk-off controls. Reject the dollar-specific mechanism if the USD predictor contributes no incremental OOS value.
8. **Placebo:** shuffle USD-index return dates within calendar blocks that preserve unconditional distribution but break temporal alignment. **Research-defined falsification threshold:** observed OOS net performance should exceed the 95th percentile of at least 1,000 placebo runs.
9. **Execution-cost stress:** apply contemporaneous fees, spread, slippage, funding/borrow and impact. **Research-defined falsification threshold:** reject tradability if expected net return is `<= 0` at intended capacity.
10. **Subperiod stability:** separately test bear, bull, low-volatility and high-volatility periods. Fail the generalized mechanism if all performance comes from a single short regime and the sign reverses elsewhere.

## Crypto portability

**Direct**, because the source itself studies Bitcoin.

Portability to current crypto execution is nevertheless incomplete. The original signal uses Bitcoin USD and traditional-market close timing; a perpetual-futures implementation changes instrument economics through funding, mark/index prices, leverage and liquidation constraints. A 24/7 UTC implementation also changes the source's timing convention.

Therefore, modern exchange-specific implementation details are **research-proposed** and require fresh validation.

## Limitations

- **Not independently reproduced.**
- **Underspecified:** exact trade timestamp, fill price, zero-forecast handling, short instrument and venue.
- **Data gap:** point-in-time vendor publication/revision metadata were not independently verified in this Scout cycle.
- **Regime risk:** source OOS evidence ends 2024-02-22.
- **Execution risk:** source fee modeling is much simpler than real BTC spot-margin or perpetual execution.
- **Clock risk:** 19:00 EST daily alignment may not transfer to other crypto-day conventions.
- **Model risk:** a small bivariate VAR can be unstable under structural breaks despite low complexity.
- **Inference risk:** modest mean DA means economic performance may depend on correctly timing a relatively small number of large BTC moves.

## Implementation status

No PyBroker, NautilusTrader, strategy-registry, data-pipeline, paper, testnet or live implementation has been performed for this record.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It does not mean the strategy is profitable, validated, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No matching Hermes Wiki Brain record was found for this DOI or exact USD-index bivariate-VAR signal during the pre-write search.

Concept-level clustering, consolidation, promotion and Wiki Brain ingestion belong to the separate Research Intake Review workflow.

## Sources

1. Rehan Arain, *When Are Statistical Forecast Gains Economically Relevant? Evidence From Bitcoin Returns*, *Journal of Forecasting* 45(3), 2026, pp. 1245–1260. First published 2025-12-17. DOI `10.1002/for.70077`: https://doi.org/10.1002/for.70077
