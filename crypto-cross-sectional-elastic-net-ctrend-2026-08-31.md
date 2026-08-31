---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Multi-Horizon Technical Trend Factor (CTREND)
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - trend-following
  - machine-learning
  - elastic-net
  - technical-indicators
status: research-only
confidence: medium
source_as_of: 2025-07
sources:
  - "Christian Fieberg, Gerrit Liedtke, Thorsten Poddig, Thomas Walker, and Adam Zaremba, 'A Trend Factor for the Cross Section of Cryptocurrency Returns', Journal of Financial and Quantitative Analysis 60(7) (2025). DOI: 10.1017/S0022109024000378"
  - "Yukun Liu, Aleh Tsyvinski, and Xi Wu, 'Common Risk Factors in Cryptocurrency', The Journal of Finance 77(2), 1133-1177 (2022). DOI: 10.1111/jofi.12935"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Multi-Horizon Technical Trend Factor (CTREND)

## Provenance

- **Primary Source:** Christian Fieberg, Gerrit Liedtke, Thorsten Poddig, Thomas Walker, and Adam Zaremba, "A Trend Factor for the Cross Section of Cryptocurrency Returns", *Journal of Financial and Quantitative Analysis*, Volume 60, Issue 7 (November 2025). DOI: [10.1017/S0022109024000378](https://doi.org/10.1017/S0022109024000378).
- **Asset Pricing Benchmark:** Comparison against the Liu, Tsyvinski, and Wu (2022) three-factor model (*The Journal of Finance*, DOI: [10.1111/jofi.12935](https://doi.org/10.1111/jofi.12935)).
- **Universe & Sample:** Cross-section of over 3,000 cryptocurrencies covering historical daily price, volume, and capitalization data.

## Economic mechanism

### Source-reported
Fieberg et al. (2025) demonstrate that individual hand-crafted technical trading rules (e.g., single moving average crossovers or isolated momentum oscillators) suffer from acute parameter sensitivity, data snooping, and regime-dependent decay in cryptocurrency markets. By employing machine learning regularization (Elastic Net), the authors aggregate information across 28 widely used technical indicators (TI28) spanning short-, intermediate-, and long-term price and volume dynamics. The resulting aggregate trend factor—termed **CTREND**—effectively filters out high-frequency noise and captures a robust, systematic trend premium across the cryptocurrency cross-section that is not spanned by existing market, size, or vanilla momentum factors.

### Research interpretation
The economic thesis is **information aggregation and multi-horizon trend persistence**:
1. **Regularized Trend Extraction:** Financial market participants utilize diverse lookback windows and technical heuristics (e.g. trend-following moving averages, oscillators, volume confirmation). No single heuristic consistently outperforms across all market conditions. Elastic Net regularization automatically balances $L_1$ sparsity (feature selection) and $L_2$ shrinkage (handling collinearity among overlapping technical indicators) to construct a robust consensus trend score.
2. **Underreaction Across Participant Horizons:** Retail and institutional participants react to price discovery over differing temporal horizons. Multi-horizon aggregation captures the full spectrum of momentum propagation while attenuating idiosyncratic single-indicator false breakouts.
3. **Cross-Sectional Factor Pricing:** Tokens with the strongest composite CTREND scores experience ongoing buying pressure and trend continuation, while tokens with negative composite scores suffer persistent liquidation drift.

## Signal

- **Universe Selection:**
  - Eligible universe: Liquid cryptocurrencies with at least 60 days of historical price and volume data and minimum 30-day average daily volume ($ADV > \$1\text{M}$).
- **Feature Set (TI28 Technical Indicator Suite):**
  - **Moving Average Rules:** Short-, intermediate-, and long-term Simple Moving Average (SMA), Exponential Moving Average (EMA), and Weighted Moving Average (WMA) price-to-average ratios:
    $$MA_{i,t,L} = \frac{P_{i,t}}{MA(P_{i}, L)_t} - 1, \quad L \in \{5, 10, 20, 50, 100, 200\}$$
  - **Momentum Oscillators:** Relative Strength Index ($RSI(14)$), Rate of Change ($ROC(L)$ for $L \in \{7, 14, 28\}$), Stochastic Oscillator ($\%K, \%D$), Moving Average Convergence Divergence ($MACD(12, 26, 9)$ signal line difference).
  - **Price-Volume Interactions:** On-Balance Volume ($OBV$), Volume-Price Trend ($VPT$), Chaikin Money Flow ($CMF(20)$), Volume Moving Average ratio ($V_{i,t} / \overline{V}_{i, t, 20}$).
  - **Volatility & Range Breakouts:** Bollinger Band percentage width ($\%B(20, 2)$), Average True Range normalized ratio ($ATR(14) / P_{i,t}$).
- **Machine Learning Regularization (Elastic Net):**
  - Rolling cross-sectional regression predicting 1-week ahead return $R_{i, t+1}$:
    $$\min_{\beta_0, \beta} \left\{ \frac{1}{2N} \sum_{i=1}^N \left( R_{i, t+1} - \beta_0 - \sum_{k=1}^{28} \beta_k X_{i,k,t} \right)^2 + \lambda \left( \alpha \|\beta\|_1 + \frac{1-\alpha}{2} \|\beta\|_2^2 \right) \right\}$$
    where $\alpha \in (0, 1)$ balances lasso and ridge penalties, and $\lambda$ is selected via expanding-window cross-validation.
  - Composite signal: Expected score $\widehat{CTREND}_{i,t} = \sum_{k=1}^{28} \hat{\beta}_k X_{i,k,t}$.
- **Portfolio Construction:**
  - Sort universe cross-sectionally by $\widehat{CTREND}_{i,t}$ into 5 quintiles at weekly rebalance epoch $t$ (00:00 UTC every Monday).
  - **Long Leg ($Q5$):** Equal-weighted top quintile of cryptocurrencies with highest CTREND score.
  - **Short Leg ($Q1$):** Equal-weighted bottom quintile of cryptocurrencies with lowest CTREND score.
  - **Strategy Spread:** Long $Q5$ minus Short $Q1$ ($L/S$).

## Required data

- **Universe:** Cross-sectional crypto spot and perpetual markets.
- **Timeframe:** Daily OHLCV bars (00:00 UTC boundary).
- **Fields:** Open, High, Low, Close, Volume in base and quote currency, circulating market capitalization.
- **Lookback:** Minimum 200 daily bars to compute longest MA indicators, plus expanding rolling window for Elastic Net parameter training.

## Execution assumptions

- **Execution Timing:** Rebalancing orders executed at next-bar open (00:00 UTC) via 15-minute TWAP.
- **Order Types:** Limit orders with execution buffers or TWAP taker orders.
- **Transaction Costs:** 5–10 bps trading fees per side; 2–5 bps slippage on liquid top-tier pairs.
- **Shorting Mechanism:** Perpetual futures contracts with adequate liquidity and margin availability.

## Evidence

### Source-reported
- Fieberg et al. (2025) report that the long-short CTREND quintile strategy generates a statistically significant average return spread of approximately $3.87\%$ per week over their multi-year empirical sample.
- The CTREND alpha remains statistically significant ($t > 3.0$) when controlled against the Liu, Tsyvinski, and Wu (2022) crypto three-factor model (Market, Size, Momentum) and traditional asset pricing factors.
- The predictive performance persists after deducting realistic transaction costs and remains robust when restricted to large, liquid cryptocurrencies.

### Independently reproduced
Not independently reproduced.

### Negative evidence
- During sudden macro regime switches or market-wide liquidity crunches (e.g. abrupt deleveraging cascades), cross-sectional trend rankings may experience severe short-term momentum crashes.
- High turnover associated with weekly quintile rebalancing requires careful cost-mitigation overlays in live deployment.

## Falsification plan

1. **Ablation vs. Single Indicator Baselines:** Compare CTREND portfolio returns against individual moving average (e.g. 20-day EMA) and vanilla 30-day momentum benchmarks. If CTREND fails to generate statistically significant incremental Sharpe ratio or information ratio, the regularized aggregation thesis is falsified.
2. **Transaction Cost Sensitivity:** Test net strategy performance under varying round-trip fee assumptions ($10\text{ bps}, 20\text{ bps}, 30\text{ bps}$). If net annualized alpha drops below zero at $15\text{ bps}$, reject practical viability.
3. **Out-of-Sample Rolling Validation:** Evaluate model on post-sample data (2025–2026). If the out-of-sample $t$-statistic on the long-short spread falls below $1.96$, reject temporal persistence.

## Crypto portability

**Direct**: The underlying study was conducted directly on cryptocurrency cross-sections (CoinMarketCap / crypto exchanges), utilizing native 24/7 crypto price and volume data.

## Limitations

- **not independently reproduced**: Historical validation in our internal PyBroker / Nautilus pipeline is pending.
- **model complexity & turnover**: Requires continuous rolling retraining of Elastic Net hyperparameters and weekly cross-sectional portfolio rebalancing.
- **short-leg borrow/perpetual constraints**: Shorting illiquid altcoins in $Q1$ may incur high funding rates or borrow limitations.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]`
- `[[crypto-cross-sectional-frog-in-the-pan-momentum-discreteness-2026-08-31]]`
- `[[crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]`

## Sources

1. Christian Fieberg, Gerrit Liedtke, Thorsten Poddig, Thomas Walker, and Adam Zaremba, "A Trend Factor for the Cross Section of Cryptocurrency Returns", *Journal of Financial and Quantitative Analysis*, Volume 60, Issue 7 (November 2025). DOI: [10.1017/S0022109024000378](https://doi.org/10.1017/S0022109024000378)
2. Yukun Liu, Aleh Tsyvinski, and Xi Wu, "Common Risk Factors in Cryptocurrency", *The Journal of Finance*, Volume 77, Issue 2, Pages 1133–1177 (April 2022). DOI: [10.1111/jofi.12935](https://doi.org/10.1111/jofi.12935)
