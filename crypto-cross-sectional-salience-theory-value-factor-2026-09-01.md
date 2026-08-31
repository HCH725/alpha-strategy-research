---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Salience Theory (Salience Value Factor)
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - behavioral-finance
  - salience-theory
  - anomaly-factor
  - lottery-preference
status: research-only
confidence: high
source_as_of: 2024-02-01
sources:
  - "Charlie X. Cai and Ran Zhao, 'Salience theory and cryptocurrency returns', Journal of Banking & Finance 159, Article 107052 (2024). DOI: 10.1016/j.jbankfin.2023.107052"
  - "Pedro Bordalo, Nicola Gennaioli, and Andrei Shleifer, 'Salience Theory of Choice Under Risk', The Quarterly Journal of Economics 127(3), 1243-1285 (2012). DOI: 10.1093/qje/qjs018"
  - "Pedro Bordalo, Nicola Gennaioli, and Andrei Shleifer, 'Salience and Asset Prices', American Economic Review: Papers & Proceedings 103(3), 623-628 (2013). DOI: 10.1257/aer.103.3.623"
  - "Mathijs Cosemans and Rik Frehen, 'Salience Theory and Stock Prices: Empirical Evidence', Journal of Financial Economics 140(2), 460-483 (2021). DOI: 10.1016/j.jfineco.2020.12.007"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Salience Theory (Salience Value Factor)

## Provenance

- **Primary Source:** Charlie X. Cai and Ran Zhao, "Salience theory and cryptocurrency returns", *Journal of Banking & Finance*, Volume 159, Article 107052 (February 2024). DOI: [10.1016/j.jbankfin.2023.107052](https://doi.org/10.1016/j.jbankfin.2023.107052).
- **Foundational Behavioral Econometric Framework:** Salience Theory of Choice Under Risk developed by Pedro Bordalo, Nicola Gennaioli, and Andrei Shleifer (2012, *QJE*; 2013, *AER*), extended to empirical cross-sectional asset pricing by Cosemans and Frehen (2021, *JFE*).
- **Empirical Universe & Data Sample:** Comprehensive cross-section of cryptocurrencies traded across major spot venues (CoinMarketCap / Binance / Coinbase data universe) evaluated across multi-year historical cycles (2014–2023).

## Economic mechanism

### Source-reported

In standard neoclassical expected utility theory, investors assign objective probabilities to potential return outcomes. Salience theory posits that human decision-makers possess bounded cognitive attention and systematically overweight states where an asset's payoff stands out prominently relative to the average payoff of available alternatives (salient payoffs).

The authors demonstrate that this cognitive distortion operates with extreme intensity in cryptocurrency markets, documenting that the salience effect in crypto is more than 20 times stronger than the corresponding effect in traditional equity markets. Cryptocurrency investors—predominantly retail participants subject to intense attention constraints, social media echo chambers, and fear-of-missing-out (FOMO)—disproportionately fixate on extreme upward return spikes (positive salience). This leads to systemic overvaluation of tokens that recently experienced standout gains. As the speculative attention subsides, these overvalued high-salience tokens underperform in subsequent periods. Conversely, cryptocurrencies exhibiting downward or subdued salience are cognitively neglected, become undervalued, and generate superior subsequent risk-adjusted returns.

### Research interpretation

The strategy is a **cross-sectional behavioral mispricing factor** targeting distorted probability weighting:

1. **Salience as Payoff Contrast:** Salience measures how far a cryptocurrency's daily return $r_{i,d}$ departs from the cross-sectional market average return $\bar{r}_d$ across a rolling formation window. A token with an isolated $+40\%$ daily surge on a flat market day receives maximal salience weight, distorting investor expectations.
2. **Distorted Valuation vs. Objective Expected Return:** Salience value ($SV_{i,t}$) calculates the subjective valuation of token $i$ under salience-distorted probability weights. When $SV_{i,t}$ is high, the asset is perceived by salient thinkers as attractive, bidding its current price above fundamental equilibrium.
3. **Mean-Reversion of Attention-Chased Outliers:** Once the salient event recedes from the rolling memory horizon, selling pressure dominates as overoptimistic retail traders exit, generating predictable negative alpha. A zero-investment cross-sectional factor that goes Long low-$SV$ tokens (undervalued/neglected) and Short high-$SV$ tokens (overvalued/salient) captures this behavioral risk premium.

## Signal

- **Daily Return and Market Payoff:**
  For each cryptocurrency $i$ on day $d \in \{t - D + 1, \dots, t\}$ (lookback window $D = 30$ days):
  $$r_{i,d} = \frac{P_{i,d} - P_{i,d-1}}{P_{i,d-1}}$$
  $$\bar{r}_d = \frac{1}{N_d} \sum_{j=1}^{N_d} r_{j,d}$$
  where $N_d$ is the number of active cryptocurrencies on day $d$.

- **Salience Function:**
  The salience of asset $i$'s return on day $d$ relative to the market benchmark is:
  $$\sigma(r_{i,d}, \bar{r}_d) = \frac{|r_{i,d} - \bar{r}_d|}{|r_{i,d}| + |\bar{r}_d| + \theta}$$
  where $\theta > 0$ is a standard small positive constant parameter (set to $\theta = 0.1$) preventing division by zero and ensuring the ordering property of salience.

- **Salience Ranking and Distorted Probability Weights:**
  - For asset $i$, rank the $D$ daily return observations in descending order of their salience values $\sigma(r_{i,d}, \bar{r}_d)$, assigning integer rank $k(i,d) \in \{1, 2, \dots, D\}$, where $k = 1$ is the most salient day.
  - Compute the salience-distorted subjective probability weight $\pi_{i,d}$:
    $$\pi_{i,d} = \frac{\delta^{k(i,d)}}{\sum_{\tau=1}^D \delta^{k(i,\tau)}}$$
    where $\delta \in (0, 1]$ is the salience distortion parameter (empirically calibrated to $\delta = 0.70$).

- **Salience Value ($SV_{i,t}$):**
  $$SV_{i,t} = \sum_{d=1}^D \pi_{i,d} \cdot r_{i,d}$$

- **Cross-Sectional Portfolio Construction:**
  - **Universe:** Top 100–300 cryptocurrencies by 30-day average daily dollar trading volume ($> \$5\text{M}$ turnover filter to eliminate microcap illiquidity).
  - **Ranking:** At the end of each week (or rolling daily), sort the universe by $SV_{i,t}$ into quintiles or deciles.
  - **Long Leg (Q1 / Decile 1):** Lowest Salience Value $SV_{i,t}$ (tokens with downward/low salience, underpriced).
  - **Short Leg (Q5 / Decile 10):** Highest Salience Value $SV_{i,t}$ (tokens with extreme upward salience, overpriced).
  - **Weighting:** Equal-weighted or inverse-volatility weighted within portfolios.
  - **Rebalancing:** Weekly rebalancing at 00:00 UTC (with 7-day holding horizon).

## Required data

- **Universe:** Top 100–300 liquid cryptocurrencies across major centralized exchanges (Binance, OKX, Bybit, Coinbase).
- **Timeframe:** Daily OHLCV price series (00:00 UTC candle close).
- **Fields:** Daily closing prices, 24h dollar volume, market capitalization.
- **Derived Series:** Cross-sectional daily market average return $\bar{r}_d$, rolling 30-day salience ranking $k(i,d)$, subjective weights $\pi_{i,d}$, and Salience Value $SV_{i,t}$.
- **Availability:** Point-in-time cross-sectional data strictly finalized at 00:00 UTC without survivorship or look-ahead bias.

## Execution assumptions

- **Execution Timing:** Weekly execution at 00:00 UTC (MOC or 15-minute TWAP at the start of the new weekly bar).
- **Order Types:** Limit orders placed inside the spread or TWAP execution on liquid spot/perpetual markets.
- **Fee Model:** Standard taker fee (4–6 bps) and maker fee (1–2 bps) per leg.
- **Slippage & Impact:** 5–10 bps assumed for altcoin constituents; universe restricted to coins with minimum $\$5\text{M}$ daily turnover.
- **Shorting Mechanism:** Perpetual swap contracts used for the short leg to ensure linear execution without spot borrow friction.

## Evidence

### Source-reported

- Charlie X. Cai and Ran Zhao (2024, *Journal of Banking & Finance*) report that the cross-sectional Salience Value factor generates an economically large and statistically significant negative return spread in the cross-section of cryptocurrencies.
- A zero-cost Long-Short strategy buying low-$SV$ tokens (Decile 1) and selling high-$SV$ tokens (Decile 10) yields highly significant abnormal returns across the sample period ($t\text{-statistic} > 3.0$).
- Bivariate portfolio sorts and Fama-MacBeth cross-sectional regressions confirm that the salience premium remains statistically robust after controlling for size (market cap), 1-day/7-day short-term reversal, 30-day price momentum, Amihud illiquidity, idiosyncratic volatility, and maximum daily return ($MAX$).
- The authors document that the magnitude of salience-driven mispricing in crypto is over 20 times larger than in traditional equities, directly attributable to the high proportion of retail participants and the extreme skewness of cryptocurrency returns.

All claims above are source-reported and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Momentum Regime Dislocation:** During speculative altcoin bull cycles (e.g., DeFi summer 2020, memecoin surges 2021, 2024), tokens exhibiting high upward salience can continue running for multiple weeks driven by reflexive retail inflows. Shorting high-$SV$ tokens during strong market-wide uptrends carries severe tail-risk drawdown without strict momentum stop-loss overlays.
- **Turnover and Cost Drag:** Daily rebalancing of salience portfolios induces significant turnover drag. Weekly or bi-weekly rebalancing is required to prevent transaction costs from eroding gross alpha.
- **Limits to Arbitrage on Low-Cap Altcoins:** While the salience effect is strongest in smaller-cap tokens, those assets frequently feature elevated bid-ask spreads, shallow liquidity depth, and punitive perpetual funding rates.

## Falsification plan

1. **Ablation vs. MAX Factor and Idiosyncratic Skewness:** Conduct bivariate independent double sorts of $SV$ against the MAX daily return factor ($MAX_{i,t}$) and Idiosyncratic Skewness ($ISKEW_{i,t}$). If the Long-Short return spread on $SV$ falls below $4\%$ annualized or loses statistical significance ($|t| < 1.96$) within neutral MAX/ISKEW buckets, reject the claim that salience theory provides distinct incremental alpha beyond standard lottery-demand proxies.
2. **Parameter Sensitivity Sweep:** Vary the distortion parameter $\delta \in [0.50, 0.90]$ in steps of $0.05$ and the lookback window $D \in [14, 60\text{ days}]$. If the strategy alpha collapses or inverts sign across reasonable parameter choices, reject the model as overfitted.
3. **Net-of-Cost Perpetual Implementation Test:** Simulate the strategy exclusively on liquid Binance/Bybit perpetual contracts with realistic taker fees (6 bps) and funding rate accounting. If net Sharpe ratio falls below $0.65$, reject operational implementation.

## Crypto portability

**Direct**: The primary source empirically tests and validates the salience theory framework directly on cryptocurrency price and return data. No traditional-market translation assumption is required.

## Limitations

- **not independently reproduced**: Historical validation in our NautilusTrader/PyBroker environment is pending.
- **short-leg borrow/funding cost**: Shorting high-salience altcoins via perpetuals may incur high positive funding rates during retail speculative frenzies.
- **parameter calibration**: The salience parameter $\delta$ and constant $\theta$ represent behavioral calibrations that may vary across market regimes.
- **liquidity filtering necessity**: The signal requires strict turnover filters ($> \$5\text{M}$ daily) to avoid illiquidity traps in microcap altcoins.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31]]`
- `[[crypto-cross-sectional-idiosyncratic-skewness-2026-08-31]]`
- `[[crypto-cross-sectional-abnormal-volume-disagreement-2026-08-31]]`
- `[[crypto-cross-sectional-abnormal-investor-attention-momentum-2026-08-31]]`

## Sources

1. Charlie X. Cai and Ran Zhao, "Salience theory and cryptocurrency returns", *Journal of Banking & Finance*, Volume 159, Article 107052 (February 2024). DOI: [10.1016/j.jbankfin.2023.107052](https://doi.org/10.1016/j.jbankfin.2023.107052)
2. Pedro Bordalo, Nicola Gennaioli, and Andrei Shleifer, "Salience Theory of Choice Under Risk", *The Quarterly Journal of Economics*, Volume 127, Issue 3, Pages 1243–1285 (August 2012). DOI: [10.1093/qje/qjs018](https://doi.org/10.1093/qje/qjs018)
3. Pedro Bordalo, Nicola Gennaioli, and Andrei Shleifer, "Salience and Asset Prices", *American Economic Review: Papers & Proceedings*, Volume 103, Issue 3, Pages 623–628 (May 2013). DOI: [10.1257/aer.103.3.623](https://doi.org/10.1257/aer.103.3.623)
4. Mathijs Cosemans and Rik Frehen, "Salience Theory and Stock Prices: Empirical Evidence", *Journal of Financial Economics*, Volume 140, Issue 2, Pages 460–483 (May 2021). DOI: [10.1016/j.jfineco.2020.12.007](https://doi.org/10.1016/j.jfineco.2020.12.007)
