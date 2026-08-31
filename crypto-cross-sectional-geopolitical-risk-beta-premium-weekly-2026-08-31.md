---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Geopolitical-Risk Beta Premium (Weekly)
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - geopolitical-risk
  - risk-premium
  - weekly
status: research-only
confidence: medium
source_as_of: 2021-12-12
sources:
  - https://doi.org/10.1016/j.frl.2022.103131
  - https://iris.ru.is/ws/files/216196380/1-s2.0-S1544612322003543-main.pdf
  - https://open.icm.edu.pl/handle/123456789/22622
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - Later evidence on major cryptocurrencies reports no robust positive hedge response to geopolitical-risk shocks, so the high-beta hedge interpretation may not be stable across later samples or large-cap universes.
---

# Crypto Cross-Sectional Geopolitical-Risk Beta Premium (Weekly)

## Provenance

Primary source: Huaigang Long, Ender Demir, Barbara Będowska-Sójka, Adam Zaremba, and Syed Jawad Hussain Shahzad, **“Is geopolitical risk priced in the cross-section of cryptocurrency returns?”** *Finance Research Letters* 49 (2022), article 103131. DOI: `10.1016/j.frl.2022.103131`. The public article states that it was available online on 2022-07-06; the study sample runs from 2014-02-03 through 2021-12-12.

The source uses daily CoinMarketCap cryptocurrency data and the daily Geopolitical Risk (GPR) index of Caldara and Iacoviello. The final research universe contains 1,980 cryptocurrencies after source-specified filters, including active and dead coins to reduce survivorship bias.

This record captures the paper's baseline univariate portfolio hypothesis: **coins with low geopolitical-risk beta subsequently outperform coins with high geopolitical-risk beta in weekly cross-section**.

## Economic mechanism

### Source-reported

The authors interpret a high positive geopolitical beta as a hedging characteristic: the asset tends to perform relatively well when the GPR index spikes. Risk-averse investors may therefore accept lower expected returns to hold such assets. Low or negative geopolitical beta instead represents adverse exposure to geopolitical-risk shocks, for which investors may demand additional compensation.

The source reports a negative cross-sectional relation between geopolitical beta and subsequent cryptocurrency returns that survives controls for size, momentum, market beta, idiosyncratic risk, liquidity, downside risk, lottery preference, co-skewness, co-kurtosis, and cross-sectional seasonality.

### Research interpretation

The falsifiable hypothesis is a **cross-sectional risk-premium sort** rather than a directional GPR timing rule. At each weekly rebalance, estimate each coin's recent sensitivity to daily changes in the global GPR index while controlling for crypto market, size, and momentum factors. Then rank coins by that estimated beta.

If the source mechanism persists, the lowest-beta quintile should earn higher subsequent weekly returns than the highest-beta quintile. The mechanism is economically distinct from generic low-beta, momentum, size, or liquidity effects because the sorting variable is conditional exposure to an external geopolitical-risk shock series.

## Signal

Source-supported baseline construction:

1. Use daily excess returns for each eligible cryptocurrency.
2. Use the daily percentage change in the Caldara-Iacoviello GPR index, `ΔGPR_t`.
3. Over a rolling **21-day** estimation window, estimate for each coin `i`:

```text
R_i,t = alpha_i
      + beta_GPR_i * ΔGPR_t
      + beta_MKT_i * MKT_F_t
      + beta_SIZE_i * SIZE_F_t
      + beta_MOM_i * MOM_F_t
      + error_i,t
```

4. At each weekly portfolio formation date, sort the cross-section on the estimated `beta_GPR` into five quintiles.
5. Baseline long-short portfolio:

```text
long  = bottom beta_GPR quintile
short = top beta_GPR quintile
```

6. Rebalance weekly. The paper reports both equal-weighted and value-weighted versions.

Source controls and robustness checks use alternative estimation periods, but the 21-day window is the stated baseline.

**Underspecified execution details:** the public article does not provide an exchange-specific executable fill convention, exact UTC portfolio-formation timestamp, borrow/futures implementation method for the short leg, or a live transaction-cost model. These must not be invented.

## Required data

- Point-in-time cryptocurrency universe including delisted/dead assets where possible.
- Daily cryptocurrency close/return data.
- Daily market capitalization and trading volume for source-style eligibility and value weighting.
- U.S. risk-free rate / T-bill proxy for excess returns if reproducing the paper exactly.
- Daily Caldara-Iacoviello GPR index and daily percentage changes.
- Crypto market, size, and momentum factor returns matching the source definitions.
- Minimum source filters: price, volume, and market-cap data available; market capitalization at least USD 1 million; trading history at least 60 days.
- Weekly point-in-time cross-sectional membership and ranks.
- Timestamp alignment between crypto daily observations and the GPR publication/date convention.

A modern exchange-specific adaptation would additionally need tradability, listing, delisting, borrow/perpetual availability, and liquidity data unavailable in CoinMarketCap-only research data.

## Execution assumptions

The source evaluates weekly characteristic-sorted portfolios, not a production execution system.

A realistic implementation study must specify:

- the exact weekly signal cutoff and next-tradable-price convention;
- whether the portfolio is implemented in spot, margin, perpetuals, or a mixed long/short universe;
- fees, bid-ask spread, slippage, and market impact;
- borrow availability/cost or perpetual funding for the short leg;
- handling of delistings, stale prices, missing observations, and exchange outages;
- position caps for micro-cap or illiquid assets;
- value-weight concentration limits and rebalance turnover.

The source itself notes that turnover can imply substantial trading costs. Gross source results should therefore not be treated as net executable returns.

## Evidence

### Source-reported

The source sample contains **1,980 cryptocurrencies** from **2014-02-03 to 2021-12-12**. Each week, cryptocurrencies are sorted into geopolitical-beta quintiles and held in equal- or value-weighted portfolios.

For the low-minus-high geopolitical-beta portfolio, the paper reports:

- equal-weighted average weekly return differential: **5.72%**;
- value-weighted average weekly return differential: **5.95%**;
- annualized Sharpe ratio: **0.75** equal-weighted and **0.77** value-weighted;
- three-factor alpha: **4.40% weekly** equal-weighted and **4.41% weekly** value-weighted.

The paper further reports that the predictive relation remains negative in weekly Fama-MacBeth-style cross-sectional regressions after controlling for multiple known cryptocurrency characteristics.

These figures are **source-reported** and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The primary paper identifies material turnover and therefore potential transaction-cost concerns. Its broad CoinMarketCap universe also includes many assets that may be difficult or impossible to short in practice.

A later study by Hakan Yilmazkuday, published in *Review of Financial Economics* in 2025, examines daily geopolitical-risk shocks for ten major cryptocurrencies and reports that none provides a robust positive hedge response across geopolitical-risk, threat, and act shocks. This is not a direct replication of the 2022 cross-sectional beta-sort strategy, but it weakens any assumption that high positive geopolitical beta is a stable hedge property in a later large-cap universe.

The source sample ends in 2021, before several major crypto-market structure changes. Post-2021 persistence is therefore unproven.

## Falsification plan

A modern reproduction should materially weaken or reject the hypothesis if any of the following occurs:

1. A point-in-time reconstruction using the source 21-day beta estimator does not recover a monotonic or economically meaningful negative relation between `beta_GPR` and next-week returns.
2. The low-minus-high spread disappears in a strict post-2021 out-of-sample period.
3. The result vanishes after restricting the universe to assets that are actually tradable and shortable at the portfolio-formation date.
4. Net returns become non-positive after realistic weekly turnover, fees, spread, slippage, borrow/funding, and impact.
5. The signal is subsumed by size, liquidity, momentum, idiosyncratic volatility, or generic market beta in the intended modern universe.
6. Alternative reasonable GPR publication/timestamp alignment removes the effect, indicating look-ahead or calendar alignment sensitivity.
7. Longer estimation windows or shrinkage of the 21-day beta estimate eliminate the ranking stability, suggesting the baseline effect depends on noisy short-window regressions.
8. Equal-weight results survive but value-weight or liquid-universe results do not, indicating that the apparent premium is confined to economically marginal assets.

The baseline 21-day estimator and weekly quintile rebalance should be tested first; alternative windows should be treated as robustness checks rather than mined replacements.

## Crypto portability

**Direct** as a crypto cross-sectional hypothesis because the primary source itself studies cryptocurrencies.

Practical portability to a modern Binance/perpetual universe is **adapted / unproven** because the source universe is CoinMarketCap-wide rather than exchange-specific and includes assets without guaranteed shortability.

Crypto-specific risks include 24/7 timestamp alignment, exchange fragmentation, delistings, micro-cap stale pricing, rapid universe turnover, perpetual funding, borrow constraints, and the possibility that global geopolitical exposure is concentrated differently after institutionalization of BTC/ETH markets.

## Limitations

- **Not independently reproduced.**
- **Post-2021 persistence unproven.**
- **Execution underspecified:** no canonical exchange, fill model, shorting instrument, or transaction-cost specification is supplied.
- **Short-window estimation risk:** `beta_GPR` is estimated from only 21 daily observations in the baseline, so coefficient noise may be substantial.
- **Tradability gap:** the source research universe is much broader than a realistic shortable exchange universe.
- **External-data dependency:** the signal requires reliable point-in-time GPR data and correct release/date alignment.
- **Contested hedge interpretation:** later evidence on major cryptocurrencies does not show robust positive hedging responses to geopolitical shocks.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live reproduction has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the Alpha Strategy Pool does not imply profitable alpha, validated predictability, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this Scout cycle.

Related strategy-pool families include cross-sectional market beta, momentum, liquidity, downside-risk, and seasonality records, but this record remains distinct because the primary ranking variable is rolling exposure to an external geopolitical-risk index.

## Sources

1. Long, H., Demir, E., Będowska-Sójka, B., Zaremba, A., & Shahzad, S. J. H. (2022). “Is geopolitical risk priced in the cross-section of cryptocurrency returns?” *Finance Research Letters*, 49, 103131. DOI: https://doi.org/10.1016/j.frl.2022.103131
2. Public full-text article PDF: https://iris.ru.is/ws/files/216196380/1-s2.0-S1544612322003543-main.pdf
3. Open institutional repository record: https://open.icm.edu.pl/handle/123456789/22622
4. Yilmazkuday, H. (2025). “Geopolitical risks and cryptocurrency returns.” *Review of Financial Economics*, 43(2), 166-191. DOI: https://doi.org/10.1002/rfe.1223
