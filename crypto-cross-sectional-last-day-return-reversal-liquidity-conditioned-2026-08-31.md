---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Last-Day Return Reversal with Liquidity Conditioning
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - reversal
  - liquidity
status: research-only
confidence: medium
source_as_of: 2021-09
sources:
  - https://doi.org/10.1016/j.irfa.2021.101908
  - https://ideas.repec.org/a/eee/finana/v78y2021ics1057521921002349.html
  - https://doi.org/10.1080/13504851.2020.1784831
  - https://digitalcommons.fairfield.edu/business-facultypubs/246/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Last-Day Return Reversal with Liquidity Conditioning

## Provenance

Primary source: Adam Zaremba, Mehmet Huseyin Bilgin, Huaigang Long, Aleksander Mercik, and Jan J. Szczygielski, “Up or down? Short-term reversal, momentum, and liquidity effects in cryptocurrency markets,” *International Review of Financial Analysis* 78 (2021), article 101908. DOI: https://doi.org/10.1016/j.irfa.2021.101908.

The primary source states that it studies daily prices for more than 3,600 cryptocurrencies and identifies the previous day’s return as a cross-sectional predictor of the next day’s return. Stable bibliographic mirror: https://ideas.repec.org/a/eee/finana/v78y2021ics1057521921002349.html.

Independent supporting source: Steven E. Kozlowski, Michael R. Puleo, and Jizhou Zhou, “Cryptocurrency return reversals,” *Applied Economics Letters* 28(11), 887–893 (2021), published online 23 June 2020. DOI: https://doi.org/10.1080/13504851.2020.1784831. Fairfield University hosts an accepted-manuscript record at https://digitalcommons.fairfield.edu/business-facultypubs/246/.

The supporting source studies 200 cryptocurrencies over 2015–2019 and reports significant reversal at daily, weekly, and monthly rebalancing frequencies, with stronger reversal among smaller-capitalization and less-liquid cryptocurrencies.

## Economic mechanism

### Source-reported

The primary source reports that cryptocurrencies with low previous-day returns subsequently outperform cryptocurrencies with high previous-day returns. The authors argue that this daily reversal is associated with the illiquidity of the majority of traded cryptocurrencies. They further report that the relationship changes with liquidity: the relatively small set of largest and most tradeable cryptocurrencies shows daily momentum rather than reversal.

The independent supporting source interprets its reversal evidence as consistent with a combination of market inefficiency and compensation for liquidity provision. It likewise reports stronger reversal among smaller-capitalization and less-liquid cryptocurrencies.

### Research interpretation

The falsifiable mechanism is short-horizon price pressure plus liquidity provision. A one-day negative price shock in a thinly traded coin may temporarily push price away from its near-term equilibrium; liquidity providers or contrarian participants earn compensation by taking the opposite side and benefiting from partial next-day normalization. If this mechanism is correct, reversal strength should increase as liquidity deteriorates and should weaken, disappear, or flip into momentum among the most liquid coins.

Liquidity is therefore part of the economic thesis, not merely an execution filter. A universal “buy yesterday’s losers” rule across all cryptocurrencies would misstate the source evidence.

## Signal

Focal source-backed signal family:

1. At each daily formation timestamp `t`, compute each eligible cryptocurrency’s previous-day close-to-close return:
   `r_i,t = P_i,t / P_i,t-1 - 1`.
2. Rank the point-in-time eligible universe cross-sectionally from the lowest previous-day return to the highest.
3. The source-supported direction is contrarian: lower-ranked prior-day losers are the long side; higher-ranked prior-day winners are the short side or comparison side.
4. Hold for the next daily return interval and re-form the ranking daily.
5. Treat liquidity/size as a regime dimension: the hypothesis should be tested separately in liquid/large and illiquid/small subsets because the primary source reports daily momentum among the largest and most tradeable cryptocurrencies.

Signal status: **underspecified** for exact portfolio reconstruction from the public material reviewed in this Scout cycle. The reviewed public sources do not provide enough detail to assert the exact number of rank buckets, breakpoint convention, weighting scheme, minimum-history requirement, universe-entry rule, or precise daily timestamp convention used in the primary portfolio-sort implementation. These details must not be invented.

A valid future reproduction should therefore first reconstruct the paper’s exact portfolio construction from the full methodological text before treating any quintile/decile choice as source faithful.

## Required data

- Point-in-time cryptocurrency universe; survivorship-free inclusion is required for a faithful modern test.
- Daily close prices sufficient to compute previous-day close-to-close returns.
- Point-in-time market capitalization and liquidity measures for regime conditioning and replication of size/liquidity dependence.
- Preferably daily turnover, traded value, or another source-consistent liquidity proxy.
- Listing and delisting dates.
- Venue/data-vendor lineage and timestamp convention.
- Missing/stale-price flags; stale prices must not be silently treated as zero returns.
- If tested on perpetuals rather than spot, funding, mark/index pricing, and contract availability must be added because the original evidence is not a perpetual-futures study.

## Execution assumptions

The reviewed public sources do not fully specify executable order handling. Therefore:

- Exact signal-to-order delay is **underspecified**.
- Same-close execution must not be assumed if the formation return requires that close; a leakage-safe implementation should only trade after the formation price is observable.
- Market versus limit order choice is not source-specified.
- Fees, spread, slippage, market impact, partial fills, and capacity treatment are not fully recoverable from the reviewed public summaries.
- The mechanism is explicitly strongest in less-liquid assets, so implementation costs and fillability are first-order concerns rather than secondary details.
- Short-leg feasibility is venue dependent. A long-only loser portfolio may be separately evaluated, but it would not be identical to a source long-short spread unless the paper’s construction explicitly supports that interpretation.

## Evidence

### Source-reported

Zaremba et al. (2021) report, using daily prices for more than 3,600 cryptocurrencies, that low previous-day-return cryptocurrencies significantly outperform high previous-day-return cryptocurrencies. They report that the result survives cross-sectional tests and portfolio sorts and is not subsumed by a broad set of other return predictors. They also report strong liquidity dependence: most illiquid coins exhibit daily reversal while the handful of largest and most tradeable coins exhibit daily momentum.

Kozlowski, Puleo, and Zhou report significant cryptocurrency return reversal in a 200-coin sample from 2015–2019 at daily, weekly, and monthly rebalancing frequencies. They report robustness to controls for size, turnover, and illiquidity, persistence across both halves of their sample and across high/low market-implied-volatility periods, and stronger reversal among smaller and less-liquid cryptocurrencies.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The most important negative/regime evidence is contained in the primary source itself: the largest and most tradeable cryptocurrencies exhibit daily momentum rather than daily reversal. This directly contradicts any claim that the last-day reversal effect should be applied uniformly to BTC, ETH, or the most liquid major-coin universe.

The existing pool record `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` also preserves related evidence that short-horizon momentum/reversal behavior varies materially by size and liquidity. This reinforces the need for explicit regime segmentation rather than pooling the entire crypto universe.

No independent modern post-2021 reproduction was performed in this Scout cycle.

## Falsification plan

The hypothesis should be considered materially weakened or rejected if, in a survivorship-free modern sample:

1. Prior-day loser-minus-winner returns are not positive out of sample after a leakage-safe one-day formation/holding convention.
2. The relation does not strengthen in lower-liquidity or smaller-capitalization buckets, or the reported liquid-versus-illiquid sign split cannot be reproduced.
3. Net returns disappear under realistic spread, fees, slippage, and participation constraints appropriate for the illiquid coins where the source says the effect is strongest.
4. A small number of stale-price, micro-price, delisting, or extreme-jump observations account for most of the spread.
5. Results vanish when the universe is defined point-in-time with minimum trading-history and stale-price filters.
6. A simple market/size/momentum control or alternative short-horizon factor fully subsumes the spread in modern data.
7. The signal’s sign is unstable across venues or depends on a data-vendor timestamp convention.

Required validation should include liquidity-bucket interaction tests, long-leg versus short-leg decomposition, turnover/cost sensitivity, subperiod stability, and an explicit large/liquid-coin control sample.

## Crypto portability

**Direct**, because both primary and supporting studies are cryptocurrency-specific.

Portability across crypto market segments is nevertheless conditional:

- Spot-to-spot portability is the closest match to the source evidence.
- Spot-to-perpetual portability is **adapted / unproven** because funding, leverage, mark/index mechanics, and perpetual-specific shorting alter both economics and execution.
- The signal may be least portable to BTC/ETH and other highly liquid majors because the primary source reports daily momentum rather than reversal in the largest/tradeable subset.
- 24/7 candle boundaries can materially change “previous day” definitions, so UTC versus venue-native daily closes must be fixed before testing.
- Venue fragmentation and delistings matter strongly for the small/illiquid universe where the effect is reported to be strongest.

## Limitations

- **underspecified**: exact source portfolio bucket count, breakpoints, weighting, and timestamp convention were not fully recoverable from the reviewed public material.
- **not independently reproduced**.
- **data gap**: no point-in-time modern replication dataset was built in this run.
- **execution gap**: realistic costs and capacity are especially important because the reported effect concentrates in less-liquid assets.
- **regime dependence**: large/liquid cryptocurrencies may exhibit the opposite sign.
- **survivorship risk**: a modern all-coin study must preserve listings, delistings, stale prices, and historical universe membership.
- **unproven** for perpetual-futures adaptation.

## Implementation status

No implementation in PyBroker, NautilusTrader, or any other internal research or trading stack has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research memory only. It is not evidence that the strategy remains profitable, not an implementation specification, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain record was queried or modified in this Scout cycle.

Related Alpha Strategy Pool artifact:

- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` — longer-horizon cross-sectional momentum with explicit liquidity/size-dependent reversal evidence.

## Sources

1. Adam Zaremba, Mehmet Huseyin Bilgin, Huaigang Long, Aleksander Mercik, and Jan J. Szczygielski, “Up or down? Short-term reversal, momentum, and liquidity effects in cryptocurrency markets,” *International Review of Financial Analysis* 78 (2021), 101908. DOI: https://doi.org/10.1016/j.irfa.2021.101908
2. RePEc/IDEAS bibliographic record for the same article: https://ideas.repec.org/a/eee/finana/v78y2021ics1057521921002349.html
3. Steven E. Kozlowski, Michael R. Puleo, and Jizhou Zhou, “Cryptocurrency return reversals,” *Applied Economics Letters* 28(11), 887–893 (2021). DOI: https://doi.org/10.1080/13504851.2020.1784831
4. Fairfield University accepted-manuscript repository record: https://digitalcommons.fairfield.edu/business-facultypubs/246/
