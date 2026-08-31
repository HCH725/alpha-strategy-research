---
schema: strategy-research-record-v1
title: Copula-Based Trading of Cointegrated Cryptocurrency Pairs
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - relative-value
status: research-only
confidence: high
source_as_of: 2023-05-11
sources:
  - "https://arxiv.org/abs/2305.06961 (DOI: 10.48550/arXiv.2305.06961)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Copula-Based Trading of Cointegrated Cryptocurrency Pairs

## Provenance

- **Source:** "Copula-Based Trading of Cointegrated Cryptocurrency Pairs" by Masood Tadi, Jiří Witzany
- **Venue:** arXiv:2305.06961, https://arxiv.org/abs/2305.06961 (later published in Financial Innovation, 2025)
- **Target:** Pairs trading / statistical arbitrage on cryptocurrency pairs.

## Economic mechanism
### Source-reported
The strategy combines cointegration tests (linear and non-linear) with copula functions to identify and trade mispriced cryptocurrency pairs. Copula families (Elliptical, Archimedean, Extreme-Value) are fitted to capture the complex, non-linear dependency structures between the assets. Trading signals are generated from the conditional distribution of the copula, reflecting a mispricing index.

### Research interpretation
Traditional statistical arbitrage assumes a linear, normally distributed mean-reverting spread (e.g., OLS regression). Cryptocurrencies exhibit heavy tails, volatility clustering, and non-linear dependencies. Copulas separate the marginal distributions of individual assets from their joint dependency structure. The economic mechanism remains liquidity provision / relative-value mean reversion (betting that a temporarily dislocated cointegrated pair will revert to its historical joint distribution), but the entry/exit thresholds are determined probabilistically via the copula's conditional CDF rather than simple Z-scores.

## Signal

- **Formation/trading cycle:** Each rolling one-month cycle uses 3 weeks for formation and the remaining 1 week for trading; the study runs 94 overlapping cycles.
- **Pair selection:** Use BTCUSDT as the reference asset. Apply Engle-Granger and KSS cointegration tests, rank eligible relationships by Kendall's Tau, and select the two highest-correlation assets for the trading week.
- **Copula construction:** Build stationary spread processes, transform them through empirical CDFs to uniform variables, fit candidate copulas by maximum likelihood, and select the best fit by AIC.
- **Hourly signal:** Compute conditional copula probabilities `h1|2` and `h2|1` from each hourly observation.
- **Open long S1 / short S2:** `h1|2 < alpha1` AND `h2|1 > 1 - alpha1`.
- **Open short S1 / long S2:** `h1|2 > 1 - alpha1` AND `h2|1 < alpha1`.
- **Close both legs:** `abs(h1|2 - 0.5) < alpha2` AND `abs(h2|1 - 0.5) < alpha2`.
- **Reported trigger study:** `alpha1` is backtested at 0.05, 0.10, 0.15, and 0.20. The paper illustrates the confidence bands with `alpha2 = 0.10`; implementation should not silently treat an illustrative value as universally optimal.
- **Position weights:** The paper provides beta-weighted price-position rules based on the cointegration spread coefficients; preserve those source-defined hedge weights rather than substituting equal or dollar-neutral sizing.

## Required data

- **Instrument / universe:** Twenty Binance USDT-margined futures contracts listed in the paper's appendix, with BTCUSDT as the reference asset.
- **Frequency/sample:** Historical hourly close prices from 2021-01-01 through 2022-11-10.
- **Formation inputs:** Hourly prices sufficient to estimate the cointegration spreads, empirical marginal CDFs, Kendall's Tau, and fitted copula parameters.
- **Trading inputs:** Hourly prices/returns needed to update the spread-derived uniform variables and conditional copula probabilities during the one-week trading period.

## Execution assumptions

- The reported backtest assumes market orders for all trades and includes transaction fees in P&L.
- The paper cites Binance taker fees of 0.04% and maker fees of 0.02% for its study context; these are historical source assumptions and must not be treated as current exchange fees.
- Both legs use the source-defined beta hedge weights. Exact live legging/latency behavior is not established by this paper and remains an implementation concern.

## Evidence
### Source-reported
The study reports that the copula-based pairs trading method outperforms buy-and-hold trading strategies in terms of both profitability and risk-adjusted returns based on historical back-testing across various entry triggers.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result. Pairs trading in crypto frequently suffers from structural breaks where cointegration relationships permanently fail.

## Falsification plan

- Reproduce the source design first: 20 Binance USDT-margined futures, hourly closes, BTC reference asset, 3-week formation / 1-week trading cycles, EG and KSS selection paths, Kendall's Tau ranking, AIC-selected copula, beta hedge weights, and the published `alpha1` trigger grid.
- Compare the copula conditional-probability rule with a simpler cointegration/spread baseline using the same pairs, formation windows, hedge weights, and costs.
- Run a strictly later point-in-time sample without selecting thresholds on the test period. Failure to retain positive net relative-value performance after costs or repeated breakdown of the selected cointegration relationships falsifies portability.

## Crypto portability

direct

The strategy is explicitly formulated and tested for the cryptocurrency market.

## Limitations

- The reported universe/window are historically fixed (20 Binance USDT-margined futures; 3-week formation / 1-week trading). Portability to a later universe, current contract specifications, and current fee schedule is unproven.
- The paper backtests multiple entry triggers, so a downstream implementation must predeclare its trigger choice rather than select it post hoc on the evaluation sample.
- unproven: not tested on our internal Nautilus/PyBroker infrastructure.

## Implementation status

not-implemented

## Adoption boundary

research-only

## Related Wiki records


## Sources
- Tadi, Witzany, "Copula-Based Trading of Cointegrated Cryptocurrency Pairs", https://arxiv.org/abs/2305.06961
