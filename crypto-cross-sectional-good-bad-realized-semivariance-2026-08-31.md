---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Good vs Bad Realized Semivariance Premium
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - realized-volatility
  - realized-semivariance
  - good-bad-volatility
  - asymmetric-risk
status: research-only
confidence: high
source_as_of: 2023-10
sources:
  - https://doi.org/10.1016/j.irfa.2023.102712
  - https://doi.org/10.1093/jjfinec/nbp025
  - https://doi.org/10.1017/S0022109019000494
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Good vs Bad Realized Semivariance Premium

## Provenance

- **Primary Source:** Zehua Zhang and Ran Zhao, “Good volatility, bad volatility, and the cross section of cryptocurrency returns”, *International Review of Financial Analysis*, Volume 89, Article 102712 (October 2023). DOI: [10.1016/j.irfa.2023.102712](https://doi.org/10.1016/j.irfa.2023.102712).
- **Econometric Framework:**
  - Ole E. Barndorff-Nielsen, Silja Kinnebrock, and Neil Shephard, “Measuring Downside Risk: Realised Semivariance” (2010), in *Volatility and Time Series Econometrics*, Oxford University Press. DOI: [10.1093/jjfinec/nbp025](https://doi.org/10.1093/jjfinec/nbp025).
  - Tim Bollerslev, Jia Li, and Bingzhi Zhao, “Good Volatility, Bad Volatility: A Market Microstructure Perspective”, *Journal of Financial and Quantitative Analysis*, 55(5), 1455–1497 (2020). DOI: [10.1017/S0022109019000494](https://doi.org/10.1017/S0022109019000494).
- **Empirical Dataset:** High-frequency intraday prices and trading volumes across liquid cross-sectional cryptocurrencies, analyzing the decomposition of total quadratic variation into signed continuous and jump semivariances.

## Economic mechanism

### Source-reported

In standard portfolio theory, volatility is treated as a symmetric measure of dispersion. However, investors exhibit strong loss aversion (Kahneman and Tversky, 1979) and react asymmetrically to positive versus negative returns.

Zhang and Zhao (2023) investigate whether decomposing total realized volatility into "good volatility" (realized semivariance of positive returns, $RS^+$) and "bad volatility" (realized semivariance of negative returns, $RS^-$) explains the cross-section of cryptocurrency returns. The authors demonstrate that:
1. **Bad Volatility Premium:** Cryptocurrencies with elevated downside realized semivariance ($RS^-$) command a positive expected return premium. Investors holding tokens prone to severe negative intraday shocks demand compensation for bearing downside tail and liquidation risk.
2. **Good Volatility Discount:** Cryptocurrencies with high upside realized semivariance ($RS^+$) exhibit lower subsequent expected returns. Retail traders and speculative market participants disproportionately chase tokens experiencing positive intraday volatility bursts (lottery-ticket preferences), driving their prices above fair value and leading to subsequent underperformance.
3. **Cross-Sectional Predictability:** The net difference between bad and good realized semivariance ($RS^- - RS^+$) exhibits significant cross-sectional predictive power for forward weekly returns, surviving controls for conventional market beta, size, momentum, idiosyncratic volatility, and liquidity.

### Research interpretation

The economic thesis is **asymmetric risk pricing and behavioral lottery overvaluation**:
1. **Downside Risk Compensation:** Downside volatility directly threatens leveraged traders with margin calls and liquidation cascades in cryptocurrency perpetual and spot markets. Bearing downside inventory risk requires a positive expected excess return to induce market makers and rational arbitrageurs to supply liquidity.
2. **Lottery Chasing & Glamour Overpricing:** Upside volatility surges in crypto are often fueled by social-media-driven FOMO and retail speculation. This excessive demand inflates prices in the short term, resulting in negative expected abnormal returns once the momentum dissipates.
3. **Information Separation:** Standard realized volatility conflates $RS^+$ and $RS^-$, masking their opposite economic effects. Decomposing realized variance into signed semivariances isolates the compensated downside risk factor from the unrewarded upside lottery factor.

## Signal

1. **Intraday Return Sampling:**
   For each cryptocurrency $i$ on day $t$, sample log prices at high-frequency intraday intervals (e.g., 5-minute or 15-minute bars $k = 1, \dots, K$):
   $$r_{i, t, k} = \ln(P_{i, t, k}) - \ln(P_{i, t, k-1})$$

2. **Realized Semivariances:**
   - **Good Realized Semivariance (Upside Volatility):**
     $$RS_{i, t}^+ = \sum_{k=1}^K r_{i, t, k}^2 \cdot \mathbf{1}_{\{r_{i, t, k} > 0\}}$$
   - **Bad Realized Semivariance (Downside Volatility):**
     $$RS_{i, t}^- = \sum_{k=1}^K r_{i, t, k}^2 \cdot \mathbf{1}_{\{r_{i, t, k} < 0\}}$$
   where $\mathbf{1}_{\{\cdot\}}$ is the indicator function. Total realized variance satisfies $RV_{i, t} = RS_{i, t}^+ + RS_{i, t}^-$.

3. **Signed Semivariance Difference Metric:**
   Compute the rolling multi-day (e.g., 7-day) realized semivariance asymmetry:
   $$\Delta RS_{i, t} = \sum_{\tau = t-6}^t RS_{i, \tau}^- - \sum_{\tau = t-6}^t RS_{i, \tau}^+$$
   or the normalized semivariance ratio:
   $$\text{SVAR}_{i, t} = \frac{\sum_{\tau = t-6}^t RS_{i, \tau}^- - \sum_{\tau = t-6}^t RS_{i, \tau}^+}{\sum_{\tau = t-6}^t RV_{i, \tau}}$$

4. **Cross-Sectional Portfolio Construction:**
   - At each weekly rebalancing date $t$, sort the eligible cryptocurrency universe into quintiles based on $\Delta RS_{i, t}$ (or $\text{SVAR}_{i, t}$).
   - **Long Leg:** Top quintile $Q_5$ (highest bad volatility relative to good volatility, capturing the downside risk premium).
   - **Short Leg:** Bottom quintile $Q_1$ (highest good volatility relative to bad volatility, shorting overvalued lottery tokens).
   - Equal-weight or market-cap-weight constituent assets within quintiles and rebalance weekly ($K = 1$ week).

## Required data

- **Universe:** Cross-section of liquid cryptocurrencies with granular intraday trading histories on major exchanges (e.g., Binance, Bybit, Coinbase, OKX).
- **Sampling Frequency:** Intraday 5-minute or 15-minute OHLCV bars.
- **Fields:** Timestamp, open, high, low, close prices, and volume.
- **Point-in-Time Requirement:** Intraday bars must be finalized prior to the weekly rebalancing timestamp (e.g., Sunday 23:59:59 UTC).
- **Data Filtering:** Tokens with missing intraday bars (> 5% of intervals) or zero-trading stretches are filtered out to prevent microstructure bias.

## Execution assumptions

- **Rebalancing Frequency:** Weekly ($K = 1$ week).
- **Execution Mechanism:** Simultaneous market or limit order rebalancing at the open of the new weekly period.
- **Shorting / Derivatives:** In perpetual futures markets, shorting $Q_1$ is directly feasible via linear USDT/USDC perpetual contracts. In spot-only universes, the strategy can be executed as a long-only tilt ($Q_5$ overweight vs. benchmark).
- **Transaction Costs:** 5-minute return sampling is used solely for signal formation; trade execution occurs only once per week, ensuring manageable turnover and low fee drag.

## Evidence

### Source-reported

- Zhang and Zhao (2023) document a statistically significant positive cross-sectional relation between bad realized semivariance ($RS^-$) and future cryptocurrency returns, alongside a negative relation between good realized semivariance ($RS^+$) and future returns.
- Univariate portfolio sorts indicate that sorting by the semivariance difference ($\Delta RS = RS^- - RS^+$) generates a statistically significant positive return spread between the top and bottom quintiles.
- Fama-MacBeth cross-sectional regressions confirm that the semivariance asymmetry factor remains statistically significant after controlling for standard cryptocurrency asset pricing factors, including size, short-term reversal, momentum, idiosyncratic volatility, and Amihud illiquidity.
- The authors show that the pricing of good versus bad volatility in cryptocurrency is consistent with behavioral models of investor asymmetry and lottery-like preferences.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Microstructure Noise at High Frequency:** At very high sampling frequencies (e.g., 1-minute or tick level), bid-ask bounce and asynchronous trading induce artificial negative autocorrelation, distorting realized semivariance estimates unless microstructure noise corrections are applied.
- **Exchange Outages & Data Gaps:** Intraday data drops or flash crashes on individual altcoins can generate massive spurious $RS^-$ spikes that do not reflect persistent systematic downside risk.
- **Regime Vulnerability:** During severe market-wide liquidation crashes, high-$RS^-$ assets can experience extreme compounding drawdowns before recovering, creating negative short-term tail risk for the long leg.

## Falsification plan

The semivariance hypothesis should be rejected or revised if:
1. Re-estimating the cross-sectional sort using 15-minute or 30-minute sampling intervals flips the sign of the return spread or removes statistical significance ($t < 1.96$), showing that the result is an artifact of high-frequency noise.
2. After controlling for idiosyncratic skewness and maximum daily return ($MAX$), the incremental $t\text{-statistic}$ of $\Delta RS$ in multivariate regressions drops below $1.65$.
3. Transaction-cost simulation using realistic taker fees and slippage on perpetual futures contracts reduces the net strategy Sharpe ratio below $0.5$.
4. Out-of-sample testing on 2023–2026 data shows that tokens with high $RS^+$ persistently outperform tokens with high $RS^-$.

## Crypto portability

- **Direct** for liquid spot and perpetual futures markets where continuous intraday price feeds are available.
- **Adapted / Unproven** for illiquid low-cap tokens where infrequent trading leads to zero-return intervals that bias semivariance calculations.
- **Crypto-Specific Portability Risks:** 24/7 continuous trading avoids traditional equity overnight gap issues, making intraday semivariance continuous; however, crypto liquidation cascades can cause extreme discontinuous jump distortions in $RS^-$.

## Limitations

- **Not independently reproduced.**
- **High-Frequency Data Dependency:** Requires continuous historical intraday bar data across hundreds of tokens.
- **Confounding with MAX / Skewness:** Bad vs. good semivariance shares conceptual overlap with idiosyncratic skewness and extreme positive return ($MAX$) anomalies; formal double-sorting is required to verify unique explanatory power.
- **Sample Period:** The primary study was published in 2023; modern post-2023 market structure dynamics require independent verification.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute approval for live capital allocation, paper trading, or testnet deployment.

## Related Wiki records

- `crypto-cross-sectional-jump-diffusion-variance-decomposition-2026-08-31.md` — quadratic variation decomposition into jump and continuous components using Bipower Variation.
- `crypto-cross-sectional-idiosyncratic-skewness-2026-08-31.md` — idiosyncratic skewness and lottery asymmetry pricing.
- `crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31.md` — extreme positive daily return ($MAX$) anomaly.
- `crypto-cross-sectional-idiosyncratic-volatility-pricing-2026-08-31.md` — total idiosyncratic volatility pricing puzzle.

## Sources

1. Zehua Zhang and Ran Zhao, “Good volatility, bad volatility, and the cross section of cryptocurrency returns”, *International Review of Financial Analysis*, Volume 89, Article 102712 (October 2023). DOI: [10.1016/j.irfa.2023.102712](https://doi.org/10.1016/j.irfa.2023.102712).
2. Ole E. Barndorff-Nielsen, Silja Kinnebrock, and Neil Shephard, “Measuring Downside Risk: Realised Semivariance” (2010), in *Volatility and Time Series Econometrics*, Oxford University Press. DOI: [10.1093/jjfinec/nbp025](https://doi.org/10.1093/jjfinec/nbp025).
3. Tim Bollerslev, Jia Li, and Bingzhi Zhao, “Good Volatility, Bad Volatility: A Market Microstructure Perspective”, *Journal of Financial and Quantitative Analysis*, 55(5), 1455–1497 (2020). DOI: [10.1017/S0022109019000494](https://doi.org/10.1017/S0022109019000494).
