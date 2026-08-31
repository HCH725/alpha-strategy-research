---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Same-Weekday Seasonality, 20-Week Lookback
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - seasonality
status: research-only
confidence: medium
source_as_of: 2024-06
sources:
  - https://doi.org/10.1016/j.frl.2020.101566
  - https://researchportal.northumbria.ac.uk/en/publications/seasonality-in-the-cross-section-of-cryptocurrency-returns/
  - https://doi.org/10.1016/j.frl.2024.105429
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - A 2024 Finance Research Letters study reports that cryptocurrency return seasonality is generally not robust across later samples; its cross-sectional Monday effect is typically negative with wide confidence intervals. This is not an exact replication of the 20-week SEAS construction, but it materially weakens confidence in persistent calendar effects.
---

# Crypto Cross-Sectional Same-Weekday Seasonality, 20-Week Lookback

## Provenance

Primary source:

- Long, Huaigang; Zaremba, Adam; Demir, Ender; Szczygielski, Jan Jakub; Vasenin, Mikhail. “Seasonality in the Cross-Section of Cryptocurrency Returns.” *Finance Research Letters* 35 (2020), 101566.
- DOI: https://doi.org/10.1016/j.frl.2020.101566
- Published online: 12 May 2020; journal publication: 1 July 2020.
- Public university repository record: https://researchportal.northumbria.ac.uk/en/publications/seasonality-in-the-cross-section-of-cryptocurrency-returns/
- Source sample: daily cryptocurrency data from 5 August 2016 through 16 December 2019.
- Universe construction reported by the source: 151 cryptocurrencies, starting from the largest by market capitalization as of 16 December 2019; cross-sectional tests require at least 20 available cryptocurrencies on a given day. The source excludes observations with non-positive market value or turnover and prices not exceeding USD 0.005.

Contradictory / later context:

- Müller, Lukas. “Revisiting seasonality in cryptocurrencies.” *Finance Research Letters* 64 (2024), 105429.
- DOI: https://doi.org/10.1016/j.frl.2024.105429
- The 2024 study reports that cryptocurrency return seasonality is not generally robust in later data; it finds the historical positive Bitcoin Monday effect disappears after 2015 and that the cross-sectional Monday effect across a much larger coin sample is typically negative, though imprecisely estimated.

This record preserves the 2020 source rule as a falsifiable research hypothesis while explicitly retaining later contradictory evidence.

## Economic mechanism
### Source-reported

The 2020 paper frames the effect as cross-sectional seasonality: assets that historically perform better on a given weekday tend to outperform other assets on that same weekday in the future. The authors discuss recurring investor behavior, sentiment, recurring inflows/outflows, and repeated trading patterns as possible origins of this predictability.

The source does not establish one unique causal mechanism. Its empirical claim is that the same-weekday return component contains incremental cross-sectional information beyond momentum, size, beta, turnover, idiosyncratic volatility, and illiquidity controls.

### Research interpretation

The falsifiable mechanism is a recurring calendar-conditioned demand / trading-pattern effect. If certain assets repeatedly attract relatively stronger demand on the same weekday, then the cross-section of historical same-weekday returns may contain information about the next realization of that weekday.

This is distinct from generic momentum. The signal deliberately samples returns at 7-day lags only, so a valid effect should survive controls for ordinary trailing momentum and should disappear if weekday identity is randomized or shifted.

The mechanism is regime-sensitive by construction. A structural change in market participation, exchange geography, weekend liquidity, stablecoin usage, or institutional trading schedules could erase or invert the effect.

## Signal

Baseline source-normalized rule:

1. At the end of each daily observation date `t-1`, for every eligible cryptocurrency `i`, compute the 20-week same-weekday seasonality score:

   `SEAS_i,t = mean(R_i,t-7, R_i,t-14, ..., R_i,t-140)`

   where `R` is the daily log return and the 20 observations are the returns from the same weekday over the prior 20 weeks.

2. On day `t`, rank the eligible cross-section by `SEAS_i,t`.

3. Sort the cross-section into five portfolios (quintiles).

4. Long the highest-SEAS quintile and short the lowest-SEAS quintile.

5. Recompute and rebalance daily so that each day uses the historical returns of that same weekday.

6. The paper reports both equal-weighted and value-weighted portfolio variants.

Signal timing:

- The source formula is lagged through `t-7`, so the current day's return is not used in the signal.
- The economic signal is therefore known before the return on day `t` is realized, assuming daily closes and the signal calculation are aligned without look-ahead.

Portfolio direction:

- Long: highest quintile of `SEAS`.
- Short: lowest quintile of `SEAS`.

Holding period:

- One day, with daily reranking / rebalancing in the source portfolio-sort design.

Parameters:

- Same-weekday lookback: 20 weeks / 20 observations.
- Cross-sectional buckets: quintiles in the baseline; the source also reports robustness using terciles and deciles.

Underspecified execution details:

- Exact exchange venue and executable price used for daily entry/exit are not specified as a live trading protocol.
- Exact portfolio turnover treatment, borrow mechanics, short availability, fee schedule, spread, and slippage are not provided as an executable backtest specification.
- The paper's portfolio sort is an asset-pricing test, not a production trading engine.

Pseudocode:

```text
for each day t:
    universe = eligible_coins_known_at_t_minus_1
    for each coin i in universe:
        seas[i] = mean(log_return[i, t-7*k] for k in 1..20)

    rank coins by seas
    long_bucket  = top 20%
    short_bucket = bottom 20%

    form equal-weighted or value-weighted long-minus-short portfolio
    hold for day t
    rebalance next day
```

## Required data

Minimum research data:

- Point-in-time cryptocurrency universe.
- Daily close prices sufficient to calculate daily log returns.
- Daily market capitalization if reproducing the source's value-weighted portfolios and size-related filters.
- Daily dollar volume / turnover if reproducing source eligibility rules and liquidity controls.
- Daily timestamps with an explicit timezone / daily-boundary convention.

Source-era universe data were obtained from CoinMarketCap. A modern reproduction should not substitute today's survivor list for a historical point-in-time universe.

Point-in-time requirements:

- Asset existence / listing status must be known as of each date.
- Market capitalization, volume, and price filters must use information available at or before signal formation.
- Delisted / failed assets must not be silently removed from historical samples.

Crypto-specific data risk:

- Different venues define daily candles using different UTC or local boundaries.
- Because the alpha is explicitly weekday-conditioned, timezone choice is part of the signal definition and must be tested, not treated as metadata.

## Execution assumptions

The paper is primarily an asset-pricing study. A practical implementation must independently specify and test:

- Signal-to-order timing: e.g. compute after a UTC daily close and execute at the next tradable price.
- Spot versus perpetual implementation.
- Market versus limit orders.
- Trading fees.
- Bid-ask spread.
- Slippage and market impact.
- Shorting / borrow availability for spot implementations.
- Funding and mark/index divergence for perpetual implementations.
- Position caps and minimum-liquidity constraints.
- Delisting and halted-market handling.
- Partial fills and cross-venue fragmentation.

The source-reported gross portfolio returns should not be interpreted as executable net returns without these assumptions.

## Evidence
### Source-reported

The 2020 study examines 151 cryptocurrencies over 5 August 2016 to 16 December 2019 and reports that higher 20-week average same-weekday returns predict higher next-period returns in the cross-section.

For the baseline quintile sorts, the source reports mean daily long-short returns of approximately:

- 0.31% for the equal-weighted high-minus-low SEAS portfolio.
- 0.43% for the value-weighted high-minus-low SEAS portfolio.

The corresponding reported t-statistics are approximately 2.05 and 2.06. The authors further report that the effect remains significant in factor-adjusted tests and in cross-sectional regressions controlling for market beta, size, 20-week momentum, turnover, idiosyncratic volatility, and Amihud illiquidity.

The source also reports robustness to alternative portfolio bucket counts and to restricting the sample to the 20 or 30 largest cryptocurrencies, as well as alternative minimum-price filters.

These are third-party source-reported results. They have not been independently reproduced in this research system.

### Independently reproduced

Not independently reproduced.

### Negative evidence

Material negative / contradictory evidence exists.

Müller (2024), *Finance Research Letters* 64, 105429, reports that broad cryptocurrency return seasonality is not robust in later data. In that study, Bitcoin's positive Monday effect does not persist after 2015, and the cross-sectional Monday effect across a larger set of coins is typically negative, although confidence intervals are wide.

This is not an exact replication of Long et al.'s 20-week same-weekday SEAS ranking signal, so it does not directly falsify the original strategy construction. It does, however, materially lower confidence that weekday-conditioned return anomalies are structurally persistent.

The 2020 paper itself acknowledges a relatively short sample period. Its universe is also selected from the largest cryptocurrencies as of 16 December 2019, which introduces a potential ex-post universe-selection / survivorship concern for a strict modern replication unless reconstructed carefully.

No independent transaction-cost reproduction was found in the reviewed sources.

## Falsification plan

A credible modern test should fail the hypothesis if the same-weekday signal does not survive realistic, leakage-safe reconstruction.

Required tests:

1. **Point-in-time universe reconstruction**
   - Recreate a survivorship-safe universe using only assets known and tradable at each historical date.
   - Compare against a naive survivor-only universe to quantify bias.

2. **Exact source signal replication**
   - `SEAS_i,t = mean(R_i,t-7, ..., R_i,t-140)`.
   - Daily cross-sectional quintile sorting.
   - Equal-weight and value-weight variants.

3. **Timezone / candle-boundary sensitivity**
   - Repeat using at least UTC and one or more alternative venue-native daily boundaries.
   - If alpha changes sign or disappears under small timestamp shifts, treat the effect as fragile.

4. **Placebo weekday test**
   - Randomly permute weekday labels or shift the 7-day lag structure by 1-3 days.
   - A genuine same-weekday effect should materially exceed these placebo constructions.

5. **Momentum ablation**
   - Compare SEAS to ordinary 20-week momentum over the same measurement window.
   - Test SEAS after neutralizing or controlling for momentum.

6. **Liquidity and size stratification**
   - Repeat on large/liquid versus small/illiquid subsets.
   - Determine whether reported profitability is concentrated in hard-to-trade tails.

7. **Post-publication out-of-sample test**
   - Hold out data beginning after the source sample end of 16 December 2019.
   - Include recent market structure and institutionalization regimes.
   - A persistent sign reversal or statistically indistinguishable-from-zero spread after costs should materially weaken or falsify adoption interest.

8. **Cost sensitivity**
   - Apply realistic taker/maker fees, spread, slippage, borrow or funding, and turnover.
   - The hypothesis should be rejected as economically unusable if gross alpha is consumed by plausible execution costs.

9. **Long-only decomposition**
   - Test whether the effect is driven by the long side, short side, or both.
   - This matters because shorting a broad altcoin universe may be infeasible.

Failure action:

- If post-2019 out-of-sample SEAS spreads are non-positive after conservative costs across reasonable timezone definitions, keep the record as negative research evidence and do not advance it toward implementation.

## Crypto portability

direct

The original evidence is already cryptocurrency-specific, so no cross-asset portability step is required for the core hypothesis.

Modern implementation still requires adaptation because:

- 24/7 markets make candle-boundary choice part of the signal.
- The current market relies much more heavily on perpetual futures and stablecoin-quoted markets than the 2016-2019 sample.
- Venue fragmentation may cause the same asset to have different daily close returns depending on data source.
- A broad long-short altcoin implementation may be impossible in spot due to borrow constraints.
- Perpetual implementation adds funding, mark/index basis, leverage, liquidation, and contract-availability effects absent from the normalized source portfolio test.

A Binance-only or perpetual-only version should therefore be labeled an adaptation, not an exact reproduction of the source study.

## Limitations

- **not independently reproduced**: no local PyBroker, Nautilus, paper, testnet, or live reproduction exists.
- **sample-length risk**: the primary source covers only August 2016 to December 2019.
- **post-publication decay risk**: later 2024 research reports weak or unstable crypto calendar anomalies.
- **universe-selection risk**: the source starts from the largest 151 cryptocurrencies as of the sample-end date, which can create ex-post universe bias relative to a strictly point-in-time tradable universe.
- **execution underspecified**: fees, spread, slippage, short availability, and exact order timing are not specified as a live strategy.
- **timezone sensitivity**: weekday identity depends on candle boundary; small timestamp changes may alter the signal.
- **capacity risk**: equal-weighting can emphasize smaller assets where transaction costs and market impact are highest.
- **short-side feasibility risk**: many historical cryptocurrencies may not have had borrowable spot or derivative markets.
- **regime dependence**: market participant composition, stablecoin dominance, weekend liquidity, and derivatives activity have changed materially since the source sample.

## Implementation status

No implementation has been completed in the user's research stack.

- PyBroker: not implemented.
- NautilusTrader: not implemented.
- Paper trading: not implemented.
- Testnet / demo: not implemented.
- Live trading: not implemented.

This record is a normalized research artifact only.

## Adoption boundary

Research only.

Presence in the Alpha Strategy Pool does not mean the strategy is profitable, validated, approved for implementation, approved for paper trading, approved for testnet, or approved for live deployment.

The source-reported results must not be treated as executable truth. The later contradictory evidence, survivorship-safe universe reconstruction, timestamp definition, and realistic transaction-cost tests are mandatory before any consideration of adoption.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this Scout cycle.

Related Alpha Strategy Pool concepts include:

- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` — materially different signal: generic 30-day cross-sectional momentum rather than weekday-conditioned 7-day-lag returns.
- `bitcoin-turn-of-15min-candle-seasonality-1m-2026-08-31.md` — materially different signal: deterministic intraday candle-boundary seasonality rather than daily cross-sectional same-weekday ranking.

## Sources

1. Long, H., Zaremba, A., Demir, E., Szczygielski, J. J., & Vasenin, M. (2020). “Seasonality in the Cross-Section of Cryptocurrency Returns.” *Finance Research Letters*, 35, 101566. DOI: https://doi.org/10.1016/j.frl.2020.101566
2. Northumbria University Research Portal, public metadata and published-version access record: https://researchportal.northumbria.ac.uk/en/publications/seasonality-in-the-cross-section-of-cryptocurrency-returns/
3. University of Pretoria repository record / public copy metadata: https://repository.up.ac.za/items/14b5a5b0-4d67-43d7-b0e0-b3735b317211
4. Müller, L. (2024). “Revisiting seasonality in cryptocurrencies.” *Finance Research Letters*, 64, 105429. DOI: https://doi.org/10.1016/j.frl.2024.105429
