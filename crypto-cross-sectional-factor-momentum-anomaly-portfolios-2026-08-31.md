---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Factor Momentum Across Anomaly Portfolios
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - factor-momentum
  - meta-strategy
  - anomalies
status: research-only
confidence: high
source_as_of: 2023-11
sources:
  - https://doi.org/10.1080/14697688.2023.2269999
  - https://doi.org/10.1111/jofi.13115
  - https://ideas.repec.org/p/arx/papers/2301.07468.html
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Factor Momentum Across Anomaly Portfolios

## Provenance

- **Primary Source:** Christian Fieberg, Gerrit Liedtke, Daniel Metko, and Adam Zaremba, “Cryptocurrency factor momentum”, *Quantitative Finance*, Volume 23, Issue 12, Pages 1853–1869 (November 2023). DOI: [10.1080/14697688.2023.2269999](https://doi.org/10.1080/14697688.2023.2269999). Working paper version: arXiv:2301.07468 / RePEc: https://ideas.repec.org/p/arx/papers/2301.07468.html.
- **Foundational Theoretical Framework:** Sina Ehsani and Juhani T. Linnainmaa, “Factor Momentum and the Momentum Factor”, *The Journal of Finance*, Volume 77, Issue 3, Pages 1877–1919 (June 2022). DOI: [10.1111/jofi.13115](https://doi.org/10.1111/jofi.13115).
- **Empirical Universe:** Over 3,900 cryptocurrencies from CoinMarketCap and major exchange histories covering January 2014 through June 2022, replicating 34 cross-sectional anomaly factor portfolios across size, liquidity, momentum, and volatility categories.

## Economic mechanism

### Source-reported

In traditional equity markets, Ehsani and Linnainmaa (2022) established that individual stock momentum is subsumed by factor momentum: past winning factors continue to outperform past losing factors due to pervasive positive autocorrelation in factor returns.

Fieberg, Liedtke, Metko, and Zaremba (2023) examine whether this factor momentum phenomenon generalizes to cryptocurrency markets. Replicating 34 published cryptocurrency anomaly factors, the authors document that:
1. Past winner factors consistently outperform past loser factors in the cryptocurrency cross-section.
2. The economic magnitude of cryptocurrency factor momentum is comparable to that observed in equities.
3. Unlike in equity markets—where factor momentum is driven by broad, pervasive autocorrelation across almost all individual factors—cryptocurrency factor momentum primarily originates from underlying asset-level price momentum that aggregates into the factor portfolios.
4. Direct autocorrelation in factor returns is not ubiquitous across all 34 factors, but is heavily concentrated in size-related and volatility-related anomaly portfolios.

### Research interpretation

The strategy is a **meta-strategy (second-order cross-sectional factor)**:
1. **Factor-Level Momentum Dynamics:** Instead of sorting individual cryptocurrency tokens directly by past return, the strategy sorts long-short anomaly factor portfolios by their recent realized performance over a lookback window (e.g., $J = 1$ to $12$ weeks).
2. **Aggregated Price Information:** Individual crypto tokens are subject to idiosyncratic noise, liquidity shocks, and extreme token-specific manipulation. Aggregating tokens into diversified characteristic-sorted anomaly factor portfolios (e.g., market cap, Amihud illiquidity, idiosyncratic volatility, downside beta) filters out idiosyncratic noise while preserving persistent macro-regime preferences (e.g., flight to liquidity, retail lottery chasing, low-beta outperformance).
3. **Regime Tracking:** Dynamic capital allocation across factor portfolios acts as an adaptive regime-following mechanism, overweighting styles and characteristics that are currently rewarded by the market and underweighting or shorting decaying styles.

## Signal

The factor momentum portfolio construction follows the standardized framework:

1. **Underlying Factor Set:** Form $M = 34$ long-short zero-cost anomaly factor portfolios at weekly frequency $t$ across four broad thematic categories:
   - **Size:** Market capitalization (`mcap`), price level (`prc`), maximum daily price (`maxdprc`), age, etc.
   - **Liquidity / Trading Activity:** Dollar volume (`vol`), turnover (`turn`), Amihud illiquidity (`illiq`), bid-ask proxies.
   - **Momentum / Trend:** Short-term reversal (`rev1w`), intermediate momentum (`mom4w`, `mom12w`), 52-week high nearness (`near52w`).
   - **Volatility / Tail Risk:** Total return volatility (`volat`), idiosyncratic volatility (`ivol`), downside beta (`beta_minus`), coskewness (`coskew`), realized skewness (`rskew`).
   Each factor $m \in \{1, \dots, 34\}$ is constructed as a top-quintile minus bottom-quintile (or top-tercile minus bottom-tercile) zero-investment portfolio with weekly return $R_{m, t}$.

2. **Factor Performance Measurement:**
   For each factor $m$ at weekly rebalancing date $t$, calculate its cumulative return over a formation lookback window of $J$ weeks (baseline $J = 1, 4, 12$ weeks):
   $$R_{m, t-J \to t} = \prod_{\tau = t-J+1}^{t} (1 + R_{m, \tau}) - 1$$

3. **Cross-Sectional Factor Momentum (FMOMCS):**
   - Sort the 34 anomaly factors based on their past cumulative return $R_{m, t-J \to t}$.
   - Partition the sorted factors into quintiles (or terciles).
   - Go long the top quintile of factors (past winner factors, equal-weighted or risk-parity weighted across the winner factor portfolios).
   - Go short the bottom quintile of factors (past loser factors, equal-weighted or risk-parity weighted across the loser factor portfolios).
   - Hold the meta-portfolio for a holding horizon of $K = 1$ week (or $K = 4$ weeks).

4. **Time-Series Factor Momentum (FMOMTS):**
   - For each factor $m$, if $R_{m, t-J \to t} > 0$, take a $+1$ long position in factor $m$; if $R_{m, t-J \to t} \le 0$, take a $-1$ short position in factor $m$.

## Required data

- **Universe:** Cross-section of liquid and semi-liquid cryptocurrencies (spot or perpetual futures) with valid price, volume, and market capitalization data.
- **Data Granularity:** Daily and weekly OHLCV, circulating market capitalization, and volume.
- **Derived Factor Characteristics:** Point-in-time calculation of 34 anomaly metrics for all eligible tokens at each weekly boundary.
- **Timing / Timestamps:** Synchronized weekly observation cutoffs (e.g., Sunday 00:00 UTC) with strict point-in-time calculation avoiding lookahead bias.
- **Missing Data Handling:** Tokens with fewer than required historical observations for a specific factor calculation are omitted from that factor's sort for the week; factor portfolios require a minimum threshold of constituent tokens to ensure diversification.

## Execution assumptions

The academic study evaluates factor portfolios using standard cross-sectional asset pricing conventions:
- Rebalancing frequency: Weekly ($K = 1$ week).
- Portfolio weighting: Equal-weighted combination of the underlying long-short anomaly portfolios.
- Execution timing: Next-week opening prices following signal calculation at the close of the observation week.
- Friction assumptions: The source baseline reports gross-of-fee returns. Executing a live meta-strategy requires simultaneous positions across dozens of constituent cryptocurrencies in both long and short legs.
- Shorting feasibility: Short legs of underlying anomaly factors assume short availability or perpetual futures contracts on constituent tokens. In crypto spot markets, shorting illiquid altcoins carries severe borrow fees or operational barriers.

## Evidence

### Source-reported

- **Return Spread:** The cross-sectional factor momentum strategy ($\text{FMOMCS}$) yields a statistically significant average return of **$0.52\%$ per week** ($t\text{-statistic} = 2.01$, significant at the $5\%$ level) over the 2014–2022 sample period.
- **Winner vs. Loser Factor Performance:**
  - Past winner factor portfolios generate a mean weekly return of **$1.65\%$** with an annualized Sharpe ratio of **$1.28$**.
  - Past loser factor portfolios generate a mean weekly return of **$0.62\%$** with an annualized Sharpe ratio of **$0.61$**.
- **Time-Series Factor Momentum:** The time-series factor momentum strategy ($\text{FMOMTS}$) earns a positive return with a $t\text{-statistic}$ of **$1.86$**.
- **Subperiod Persistence:** Risk-adjusted performance of $\text{FMOMCS}$ did not experience post-2018 alpha decay; the annualized Sharpe ratio increased from **$0.59$** in the first subperiod (2014–2018) to **$0.86$** in the second subperiod (2018–2022).
- **Driver Decomposition:** Cross-sectional factor momentum profits are shown to stem primarily from underlying asset price momentum rather than exogenous factor autocorrelation, except in size and volatility factors where factor-level autocorrelation is strong.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Turnover and Transaction Costs:** Because the strategy operates on 34 multi-token portfolios, weekly portfolio turnover is high. For smaller altcoins with wide bid-ask spreads and high taker fees, transaction costs can significantly erode the $0.52\%$ weekly gross spread.
- **Short-Leg Execution Constraints:** Many underlying anomaly factors require shorting small-cap tokens. If shorting is restricted to perpetual futures, the effective universe shrinks from thousands of tokens to only top perpetual listings (typically 100–300 tokens), which may alter factor dispersion.
- **Narrow Autocorrelation:** The finding that factor autocorrelation is concentrated in size and volatility rather than ubiquitous across all 34 factors implies that equal-weighting all 34 factors may introduce noise from non-persistent anomalies.

## Falsification plan

A rigorous quantitative test in our research stack should reject or materially adjust the hypothesis if:
1. Restricting the underlying token universe to liquid perpetual futures contracts (e.g., top 100 Binance/Bybit perps) reduces the factor momentum weekly return spread below statistical significance ($t < 1.96$).
2. Applying realistic exchange trading fees (e.g., 5 bps taker fee per trade) and simulated slippage reduces net annualized Sharpe ratio below $0.5$.
3. An ablation test that restricts the factor universe strictly to size and volatility factors outperforms the full 34-factor universe, confirming that non-persistent anomalies dilute the meta-signal.
4. Out-of-sample testing on post-2022 data (July 2022 – present) shows structural breakdown or negative information ratio.
5. Placebo tests with randomly shuffled factor returns produce comparable return spreads, disproving genuine factor momentum persistence.

## Crypto portability

- **Adapted / Unproven:** Ported from equity factor momentum (Ehsani & Linnainmaa, 2022) to crypto by Fieberg et al. (2023). While the source empirically demonstrates the effect on a historical crypto dataset (2014–2022), live execution requires substantial adaptation.
- **Crypto-Specific Implementation Constraints:**
  - Token listing/delisting turnover is orders of magnitude higher than in equities.
  - High borrow costs and liquidation risks on small-cap crypto spot tokens require shifting the execution layer to liquid perpetual futures or long-only tilt implementations.
  - 24/7 continuous trading requires standardized weekly snapshot conventions (e.g., Sunday 00:00 UTC) to prevent calendar misalignment.

## Limitations

- **Not independently reproduced.**
- **High Turnover / Fee Sensitivity:** Gross statistical significance ($t = 2.01$) may not survive institutional trading frictions without portfolio optimization and turnover reduction techniques.
- **Universe Survivorship Bias:** Historical CoinMarketCap datasets may suffer from delisting/survivorship quirks, though Fieberg et al. utilize historical dead-coin archives to mitigate this.
- **Data Gap:** The empirical sample ends in June 2022; performance during the post-FTX regime (2022–2026) is unverified.
- **Underspecified Live Execution:** The paper presents an academic portfolio sort rather than an executable production order routing and risk allocation model.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute approval for live capital allocation, paper trading, or testnet deployment.

## Related Wiki records

- `crypto-cross-sectional-elastic-net-ctrend-2026-08-31.md` — machine learning trend factor across technical indicators; same research group (Fieberg et al.), complementary signal aggregation philosophy.
- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` — individual token price momentum; source paper establishes the transmission mechanism between token momentum and factor momentum.
- `crypto-cross-sectional-volatility-managed-momentum-2026-08-31.md` — volatility scaling applied to momentum portfolios.

## Sources

1. Christian Fieberg, Gerrit Liedtke, Daniel Metko, and Adam Zaremba, “Cryptocurrency factor momentum”, *Quantitative Finance*, Volume 23, Issue 12, Pages 1853–1869 (2023). DOI: [10.1080/14697688.2023.2269999](https://doi.org/10.1080/14697688.2023.2269999).
2. Sina Ehsani and Juhani T. Linnainmaa, “Factor Momentum and the Momentum Factor”, *The Journal of Finance*, Volume 77, Issue 3, Pages 1877–1919 (2022). DOI: [10.1111/jofi.13115](https://doi.org/10.1111/jofi.13115).
3. Working paper / RePEc archive: https://ideas.repec.org/p/arx/papers/2301.07468.html and arXiv:2301.07468.
