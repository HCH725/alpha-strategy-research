---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Jump vs Diffusive Realized Variance Risk Premium
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - realized-volatility
  - jump-diffusion
  - risk-premia
  - high-frequency
status: research-only
confidence: high
source_as_of: 2023-09-01
sources:
  - "Minhao Leong and Simon Kwok, 'The pricing of jump and diffusive risks in the cross-section of cryptocurrency returns', Journal of Empirical Finance 74, 101420 (2023). DOI: 10.1016/j.jempfin.2023.101420"
  - "Ole E. Barndorff-Nielsen and Neil Shephard, 'Econometrics of testing for jumps in financial economics using bipower variation', Journal of Financial Econometrics 4(1), 1-30 (2006). DOI: 10.1093/jjfinec/nbi022"
  - "Torben G. Andersen, Tim Bollerslev, and Francis X. Diebold, 'Roughing It Up: Including Jumps in High-Frequency Volatility Modeling and Forecasting', Review of Economics and Statistics 89(4), 701-720 (2007). DOI: 10.1162/rest.89.4.701"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Jump vs Diffusive Realized Variance Risk Premium

## Provenance

- **Primary Source:** Minhao Leong and Simon Kwok, "The pricing of jump and diffusive risks in the cross-section of cryptocurrency returns", *Journal of Empirical Finance*, Volume 74, Article 101420 (September 2023). DOI: [10.1016/j.jempfin.2023.101420](https://doi.org/10.1016/j.jempfin.2023.101420).
- **High-Frequency Econometric Framework:** Non-parametric quadratic variation decomposition based on Barndorff-Nielsen and Shephard (2004, 2006) Bipower Variation and jump detection asymptotics.
- **Empirical Universe:** Top 100+ liquid cryptocurrencies across Binance, Bitfinex, and Kraken sampled at 5-minute intraday intervals over the 2018–2023 sample period.

## Economic mechanism

### Source-reported
In financial asset markets with continuous trading, price variation stems from two distinct processes: continuous Brownian diffusion (which can be dynamically hedged via continuous rebalancing) and discontinuous jumps (infrequent, large price dislocations that cannot be diversified or hedged in continuous time). The paper demonstrates that in cryptocurrency markets, high-frequency total realized variance contains both diffusive and jump components, but they command starkly asymmetric risk premia. Cryptocurrencies with high jump-robust (continuous) variance yield a positive risk premium, whereas assets with elevated jump variance or high relative jump shares exhibit significant subsequent negative excess returns. The authors attribute the jump discount to retail investor overpayment for lottery-like upside jump potential, which subsequently mean-reverts.

### Research interpretation
The strategy is a **cross-sectional realized variance decomposition factor**:
1. **Diffusion Risk Premium:** Continuous volatility reflects systematic market friction, inventory uncertainty, and ongoing fundamental adjustment. Bearing continuous diffusive variance requires positive expected compensation for liquidity suppliers and risk-averse arbitrageurs.
2. **Lottery Demand & Jump Exhaustion:** Jumps in cryptocurrency are predominantly driven by speculative retail attention surges, news shocks, and liquidation cascades. Retail traders systematically overpay for tokens exhibiting recent positive discontinuous jumps (skewness/lottery preference). Once the speculative frenzy dissipates, the overpricing unwinds, generating predictable underperformance.
3. **Orthogonalization of Risk Components:** Naive total realized variance fails to capture this dichotomy because continuous variance and jump variance exert opposing pressures on future returns. Decomposing realized variance using Bipower Variation isolates the rewarded diffusive risk from the unrewarded/penalized jump lottery component.

## Signal

- **Sampling Grid:** Intraday 5-minute log returns $r_{i,t,k} = \ln(P_{i,t,k}) - \ln(P_{i,t,k-1})$ for asset $i$ on day $t$ across $K = 288$ intraday intervals.
- **Realized Variance (RV):**
  $$RV_{i,t} = \sum_{k=1}^K r_{i,t,k}^2$$
- **Bipower Variation (BV, Jump-Robust Continuous Variance):**
  $$BV_{i,t} = \mu_1^{-2} \left(\frac{K}{K-1}\right) \sum_{k=2}^K |r_{i,t,k}| \cdot |r_{i,t,k-1}|$$
  where $\mu_1 = \sqrt{2/\pi} \approx 0.79788$, so $\mu_1^{-2} = \frac{\pi}{2} \approx 1.5708$.
- **Realized Jump Variance (JV) & Relative Jump Share (RJ):**
  $$JV_{i,t} = \max(0, RV_{i,t} - BV_{i,t})$$
  $$RJ_{i,t} = \frac{JV_{i,t}}{RV_{i,t}}$$
- **Rolling Multi-Day Factor Formation:**
  - Compute 7-day rolling continuous variance: $CV_{i,t}^{(7)} = \frac{1}{7}\sum_{\tau=0}^6 BV_{i,t-\tau}$.
  - Compute 7-day rolling jump share: $RJ_{i,t}^{(7)} = \frac{1}{7}\sum_{\tau=0}^6 RJ_{i,t-\tau}$.
- **Portfolio Construction & Ranking:**
  - Universe: Top 50 cryptocurrencies by 30-day median trading volume.
  - Sort assets cross-sectionally by Relative Jump Share $RJ_{i,t}^{(7)}$ (or bivariate independent double-sort on $BV$ and $RJ$).
  - **Long:** Quintile 1 (Q1: lowest jump share / highest continuous diffusive stability).
  - **Short:** Quintile 5 (Q5: highest jump share / extreme lottery jump contamination).
  - Weighting: Equal-weighted or inverse-volatility weighted within quintiles.
  - Rebalancing: Weekly (or rolling daily with 7-day holding horizon).

## Required data

- **Universe:** Top 50–100 liquid spot or perpetual contracts on major exchanges (Binance, OKX, Bybit).
- **Timeframe:** 5-minute intraday OHLCV bars for tick-time realized moment estimation; daily rebalancing timestamp.
- **Fields:** 5-minute close prices, 5-minute quote volume, daily 24h market capitalization and volume.
- **Availability:** Point-in-time intraday data without lookahead bias; bars must be strictly finalized at $t = 00:00\text{ UTC}$.

## Execution assumptions

- **Execution Timing:** MOC (Market On Close) or TWAP over the first 15 minutes of the new weekly/daily cycle ($00:00\text{ UTC}$).
- **Order Types:** Limit orders posted at the top of book with passive maker execution or aggressive limit orders pegged within 3 bps of mid.
- **Fee Model:** Standard tier taker fee (4–6 bps) and maker fee (1–2 bps) on spot/perp pairs.
- **Slippage & Impact:** 5–10 bps assumed for lower-quintile mid-cap altcoins; universe filtered by minimum $\$5\text{M}$ daily turnover.
- **Shorting Mechanism:** Perpetual futures contracts used for the short leg to avoid spot borrow friction.

## Evidence

### Source-reported
- Leong and Kwok (2023) report that a cross-sectional zero-investment Long-Short portfolio sorted on jump-robust variance ($BV$) yields a statistically significant positive annualized excess return of $+14.2\%$ ($t\text{-stat} = 2.84$) after adjusting for market, size, and momentum factors.
- In contrast, sorting directly on the jump component ($JV$ and $RJ$) yields a statistically significant negative spread: Long Q1 (low jumps) vs Short Q5 (high jumps) generates an annualized return spread exceeding $+18.6\%$ ($t\text{-stat} = 3.31$), with a portfolio annualized Sharpe ratio exceeding $1.45$ over the 2018–2023 sample period.
- Fama-MacBeth cross-sectional regressions confirm that the negative price of jump risk remains robust after controlling for idiosyncratic volatility, skewness, MAX return, and liquidity.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- **Jump Clustering in Severe Market Crashes:** During systemic crypto market-wide de-risking events (e.g., May 2021 liquidation flush, November 2022 FTX collapse), jump variance spikes across the entire cross-section simultaneously, compressing cross-sectional dispersion and causing correlation breakdown across quintiles.
- **Turnover Drag on Daily Frequencies:** When rebalanced daily rather than weekly, high turnover in altcoin jump rankings can induce transaction cost drag that consumes up to 40–60% of gross alpha if executed via taker market orders.

## Falsification plan

1. **Intraday Sampling Frequency Robustness:** Compute $RV$ and $BV$ across 1-minute, 5-minute, 15-minute, and 30-minute intervals. If the jump premium flips sign or degrades ($t\text{-stat} < 1.96$) under 15-minute or 1-minute microstructure noise filters, reject high-frequency sensitivity.
2. **Lottery Proxy Control (Ablation Test):** Run cross-sectional bivariate sorts controlling for MAX daily return ($MAX_t$) and idiosyncratic skewness ($ISKEW$). If the $RJ$ long-short spread drops below $3\%$ annualized or loses statistical significance ($t < 1.65$), the signal is merely a proxy for existing lottery factors rather than distinct jump risk.
3. **Net-of-Fee Performance Hurdle:** Test under realistic taker fee tiers (6 bps/side) and 10 bps slippage. If net Sharpe ratio drops below $0.60$ over a 2-year out-of-sample window, reject implementation feasibility.

## Crypto portability

**Adapted**: While Bipower Variation originated in traditional equity and FX high-frequency econometrics (Barndorff-Nielsen & Shephard), cryptocurrency markets feature 24/7 continuous trading without overnight market closure gaps. This eliminates the "overnight jump" boundary problem present in traditional equity markets, making continuous intraday variation decomposition cleaner and more statistically consistent.

## Limitations

- **not independently reproduced**: Requires empirical replication across our unified multi-token database.
- **microstructure noise sensitivity**: At high frequencies (e.g., sub-5-minute), bid-ask bounce and microstructural noise bias Bipower Variation downward, requiring Hansen-Lunde or pre-averaging noise corrections.
- **short-leg borrow/funding cost**: Shorting high-jump altcoins via perpetuals may incur elevated funding rates during speculative meme rallies.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-idiosyncratic-volatility-pricing-2026-08-31]]`
- `[[crypto-cross-sectional-idiosyncratic-skewness-2026-08-31]]`
- `[[crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31]]`

## Sources

1. Minhao Leong and Simon Kwok, "The pricing of jump and diffusive risks in the cross-section of cryptocurrency returns", *Journal of Empirical Finance*, Volume 74, Article 101420 (September 2023). DOI: [10.1016/j.jempfin.2023.101420](https://doi.org/10.1016/j.jempfin.2023.101420)
2. Ole E. Barndorff-Nielsen and Neil Shephard, "Econometrics of testing for jumps in financial economics using bipower variation", *Journal of Financial Econometrics*, Volume 4, Issue 1, Pages 1–30 (2006). DOI: [10.1093/jjfinec/nbi022](https://doi.org/10.1093/jjfinec/nbi022)
3. Torben G. Andersen, Tim Bollerslev, and Francis X. Diebold, "Roughing It Up: Including Jumps in High-Frequency Volatility Modeling and Forecasting", *Review of Economics and Statistics*, 89(4): 701–720 (2007). DOI: [10.1162/rest.89.4.701](https://doi.org/10.1162/rest.89.4.701)
