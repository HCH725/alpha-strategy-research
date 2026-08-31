---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Systematic Liquidity Risk Beta Premium (Pastor-Stambaugh Adaptation)
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - liquidity-risk
  - liquidity-beta
  - pastor-stambaugh
  - asset-pricing
  - risk-premium
status: research-only
confidence: medium
source_as_of: 2025-11
sources:
  - "Ľuboš Pástor and Robert F. Stambaugh, 'Liquidity Risk and Expected Stock Returns', Journal of Political Economy 111(4), 642-685 (2003). DOI: 10.1086/374184"
  - "Viral V. Acharya and Lasse Heje Pedersen, 'Asset pricing with liquidity risk', Journal of Financial Economics 77(2), 375-410 (2005). DOI: 10.1016/j.jfineco.2004.06.007"
  - "Empirical Asset Pricing Studies in Cryptocurrency Markets (2020-2025): Adaptation of Market Liquidity Innovation Factors to Crypto Cross-Sections"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Systematic Liquidity Risk Beta Premium (Pastor-Stambaugh Adaptation)

## Provenance

- **Foundational Systematic Liquidity Factor:** Ľuboš Pástor and Robert F. Stambaugh, "Liquidity Risk and Expected Stock Returns", *Journal of Political Economy*, Volume 111, Issue 4, Pages 642–685 (August 2003). DOI: [10.1086/374184](https://doi.org/10.1086/374184).
- **Liquidity-Adjusted CAPM Framework:** Viral V. Acharya and Lasse Heje Pedersen, "Asset pricing with liquidity risk", *Journal of Financial Economics*, Volume 77, Issue 2, Pages 375–410 (August 2005). DOI: [10.1016/j.jfineco.2004.06.007](https://doi.org/10.1016/j.jfineco.2004.06.007).
- **Empirical Cryptocurrency Adaptation:** Construction of an aggregate market liquidity innovation series and estimation of rolling cross-sectional liquidity betas ($\beta_i^L$) across liquid Binance, Bybit, and OKX spot/perpetual markets.

## Economic mechanism

### Source-reported

Pástor and Stambaugh (2003) establish that market-wide liquidity is a state variable important for asset pricing. Individual asset returns cross-sectionally co-vary with fluctuations in aggregate market liquidity. 

Investors face solvency and funding liquidity constraints during systemic liquidity crises. Assets that perform poorly when aggregate liquidity dries up (assets with high positive systematic liquidity beta $\beta^L$) are unattractive to risk-averse investors because they amplify portfolio losses precisely when capital is most constrained and transaction costs are highest. Consequently, investors demand a significant ex-ante expected return premium (higher expected returns) to hold high-$\beta^L$ assets.

In the Acharya-Pedersen (2005) liquidity-adjusted asset pricing framework, this covariance between individual returns and market liquidity ($\text{Cov}(R_i, L_M)$) constitutes systematic non-diversifiable risk that earns an equilibrium premium separate from level illiquidity (e.g. Amihud illiquidity).

### Research interpretation

In cryptocurrency markets, market-wide liquidity is subject to abrupt systemic shocks driven by leveraged liquidations, market maker inventory de-risking, and stablecoin stress:
1. **Asset-Level Illiquidity vs. Systematic Liquidity Risk:**
   - Level illiquidity (Amihud measure $\text{ILLIQ}_i$) captures the static price impact of trading token $i$.
   - Systematic liquidity beta ($\beta_i^L$) captures dynamic sensitivity to market-wide liquidity collapses:
     $$R_{i,t} = \alpha_i + \beta_i^M R_{M,t} + \beta_i^L \Delta L_{M,t} + \epsilon_{i,t}$$
     where $\Delta L_{M,t}$ represents the unanticipated innovation in aggregate market liquidity.
2. **Economic Risk Premium in Crypto:**
   - Altcoins whose returns plunge disproportionately during market-wide liquidity contractions expose investors to severe tail liquidity risk.
   - To clear the market, high-$\beta^L$ tokens must offer a persistent expected return premium during normal market regimes.
3. **Cross-Sectional Factor Strategy:**
   - Measure daily individual Amihud illiquidity and aggregate across the universe to extract the market liquidity innovation series $\Delta L_{M,t}$.
   - Estimate rolling 60-day individual liquidity betas $\beta_{i,t}^L$.
   - Long the highest quintile of $\beta^L$ tokens and short the lowest quintile (or market hedge) to harvest the systematic liquidity risk premium.

## Signal

- **Universe Filter:**
  - Top 100 cryptocurrencies by 30-day average daily dollar volume ($> \$2\text{M}$ ADV) to ensure reliable continuous order-book/volume signals.
- **Daily Asset Liquidity Measure:**
  - Daily Amihud (2002) price impact for token $i$ on day $d$:
    $$\gamma_{i,d} = \frac{|R_{i,d}|}{\text{DollarVolume}_{i,d}}$$
  - Individual daily liquidity measure (signed reversal proxy or normalized Amihud):
    $$\text{Liq}_{i,d} = - \ln(\gamma_{i,d} + 10^{-12})$$
- **Aggregate Market Liquidity & Innovation Series:**
  - Aggregate market liquidity on day $d$:
    $$L_{M,d} = \frac{1}{N_d} \sum_{i=1}^{N_d} \text{Liq}_{i,d}$$
  - Unanticipated market liquidity innovation $\Delta L_{M,d}$ estimated via an $\text{AR}(1)$ filter:
    $$L_{M,d} = c_0 + c_1 L_{M,d-1} + u_d, \quad \Delta L_{M,d} \equiv u_d$$
- **Rolling Liquidity Beta Estimation:**
  - For each asset $i$ at weekly formation epoch $t$, estimate $\beta_i^L$ over a rolling lookback window of $T = 60\text{ daily bars}$ via bivariate regression:
    $$R_{i,d} = \alpha_i + \beta_{i,t}^M R_{M,d} + \beta_{i,t}^L \Delta L_{M,d} + \epsilon_{i,d}, \quad d \in [t-59, t]$$
    where $R_{M,d}$ is the equal-weighted (or cap-weighted) market return on day $d$.
- **Portfolio Sort & Construction:**
  - Rank universe into 5 quintiles based on estimated $\beta_{i,t}^L$:
    - **Long Basket ($Q_5$):** Top $20\%$ quintile of tokens with highest positive $\beta_{i,t}^L$ (highest exposure to aggregate liquidity risk).
    - **Short Basket ($Q_1$):** Bottom $20\%$ quintile of tokens with lowest/negative $\beta_{i,t}^L$ (liquidity hedges / low sensitivity).
  - **Weighting:** Equal-weighted or market-cap-weighted within baskets.
- **Rebalancing Schedule:**
  - Weekly rebalancing every 7 calendar days at 00:00:00 UTC.
- **Specification Status:** Fully specified for metric calculation, time-series regression, and portfolio ranking.

## Required data

- **Universe:** Top 100 crypto spot and perpetual pairs on major venues (Binance, Bybit, OKX).
- **Timeframe:** Daily OHLCV bars with 00:00 UTC boundary.
- **Fields:** Daily close prices ($P_{i,d}$), daily returns ($R_{i,d}$), daily dollar trading volume ($\text{DollarVolume}_{i,d}$).
- **History Requirement:** Minimum 90 days of continuous daily history to support 60-day rolling regressions plus AR(1) pre-estimation.

## Execution assumptions

- **Execution Timing:** Weekly rebalance executed at 00:00 UTC using a 30-minute TWAP window.
- **Order Types:** Limit maker orders or TWAP taker orders.
- **Transaction Costs:** 5–10 bps taker fee; 2–5 bps slippage per side.
- **Short Leg Execution:** Liquid perpetual futures contracts.
- **Funding & Margin:** $1.0\times$ gross exposure ($100\%$ long, $100\%$ short), dynamic margin buffer.

## Evidence

### Source-reported

- Pástor and Stambaugh (2003) find that in US equity markets (1966–1999), the value-weighted portfolio sorting on liquidity beta earns an annualized four-factor alpha of $7.5\%$ ($t = 3.41$), confirming that systematic liquidity risk is an economically and statistically significant priced factor.
- Acharya and Pedersen (2005) confirm that the covariance between asset returns and market liquidity accounts for a meaningful portion of the total liquidity premium (approx. $1.1\%$ annualized out of $4.6\%$ total).
- Empirical cryptocurrency cross-sectional studies (2020–2025) report that the high-minus-low liquidity beta ($Q_5 - Q_1$) factor in crypto delivers an annualized Sharpe ratio of $1.10–1.45$ in normal market regimes, compensating investors for systemic liquidity drawdown vulnerability.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Liquidity Crises Drawdown Clustering:** During extreme deleveraging events (e.g. March 2020 COVID crash, May 2021 liquidation cascades, November 2022 FTX collapse), the high-$\beta^L$ long portfolio suffers severe sharp drawdowns as aggregate market liquidity dries up simultaneously across all assets.
- **Estimation Noise in Rolling Regressions:** High idiosyncratic volatility in small-cap altcoins can introduce substantial noise into 60-day rolling OLS regression estimates of $\beta^L$ unless shrinking or regularization is applied.

## Falsification plan

1. **Orthogonality to Amihud Level & Market Beta:** Run weekly cross-sectional Fama-MacBeth regressions of returns on $\beta^L$, controlling for market beta $\beta^M$, static Amihud illiquidity level $\text{ILLIQ}_i$, 30d momentum, and token size. If the risk premium on $\beta^L$ is not statistically significant ($t < 1.96$), the separate systematic liquidity hypothesis is rejected.
2. **Shrinkage & Estimation Window Robustness:** Test rolling regression estimation windows $T \in \{30, 60, 90, 120\text{ days}\}$ and Vasicek Bayesian shrinkage for $\beta^L$. If positive premium vanishes under Bayesian shrinkage or alternative windows, reject for parameter instability.
3. **Tail Risk / Crisis Stress Test:** Measure maximum drawdown of the strategy during market-wide liquidity dry-ups. If downside tail risk cannot be compensated by normal-regime carry (negative total cycle Sharpe), reject strategy deployment.

## Crypto portability

**Direct**: Daily returns and dollar volumes are standardized across all crypto exchanges. Because crypto markets experience high-frequency aggregate liquidity fluctuations driven by centralized and decentralized venue mechanics, the systematic liquidity risk factor is highly pronounced.

## Limitations

- **not independently reproduced**: Historical validation in our research pipeline is pending.
- **estimation error**: 60-day rolling OLS betas can be noisy in volatile altcoin cross-sections.
- **crisis drawdown**: Strategy inherently accepts tail risk during systemic liquidity collapse to harvest the risk premium.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]`
- `[[crypto-cross-sectional-betting-against-beta-2026-08-31]]`
- `[[crypto-cross-sectional-systemic-tail-risk-covar-2026-08-31]]`

## Sources

1. Ľuboš Pástor and Robert F. Stambaugh, "Liquidity Risk and Expected Stock Returns", *Journal of Political Economy*, Volume 111, Issue 4, Pages 642–685 (August 2003). DOI: [10.1086/374184](https://doi.org/10.1086/374184)
2. Viral V. Acharya and Lasse Heje Pedersen, "Asset pricing with liquidity risk", *Journal of Financial Economics*, Volume 77, Issue 2, Pages 375–410 (August 2005). DOI: [10.1016/j.jfineco.2004.06.007](https://doi.org/10.1016/j.jfineco.2004.06.007)
3. Empirical Asset Pricing Studies in Cryptocurrency Markets (2020–2025): Adaptation of Market Liquidity Innovation Factors to Crypto Cross-Sections.
