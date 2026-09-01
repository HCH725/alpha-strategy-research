---
schema: strategy-research-record-v1
title: "Observable Matrix Dynamics for Dynamic Portfolio Optimization and Ranking Forecasts"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - observable-matrix-dynamics
  - markov-chains
  - momentum
  - cross-sectional-ranking
  - statistical-finance
status: research-only
confidence: medium
source_as_of: 2026-07-29
sources:
  - "Igor Halperin, 'Are Three Matrices All You Need To Beat the Market? Observable Matrix Dynamics for Portfolio Optimization', arXiv:2607.27461v1 [q-fin.PM, q-fin.ST], July 29, 2026. https://arxiv.org/abs/2607.27461"
  - "Igor Halperin, 'Observable Matrix Dynamics of Stocks', arXiv:2607.19005v1 [q-fin.ST], July 2026. https://arxiv.org/abs/2607.19005"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Observable Matrix Dynamics for Dynamic Portfolio Optimization and Ranking Forecasts

## Provenance

- **Primary Paper:** Igor Halperin, *"Are Three Matrices All You Need To Beat the Market? Observable Matrix Dynamics for Portfolio Optimization"*, arXiv preprint `arXiv:2607.27461v1 [q-fin.PM, q-fin.ST]`, published July 29, 2026. URL: https://arxiv.org/abs/2607.27461.
- **Foundational Paper:** Igor Halperin, *"Observable Matrix Dynamics of Stocks"*, arXiv preprint `arXiv:2607.19005v1 [q-fin.ST]`, published July 2026. URL: https://arxiv.org/abs/2607.19005.
- **Author:** Igor Halperin (Fidelity Investments / New York University).
- **Dataset / Empirical Sample:** S&P 500 constituent universe daily prices, trading volume, and market capitalization. Out-of-sample evaluation periods: January 2022 to December 2024 (OOS-1, 3 years) and January 2025 to July 2026 (OOS-2, 1.5 years).
- **Code Artifact Reference:** Repository structure described in paper as `ighalp/omd_portfolio`.

## Economic mechanism

### Source-reported

Classical Markowitz Mean-Variance Optimization (MVO) constructs optimal asset weights $w^* = \lambda \Sigma^{-1} \mu$ using an unobservable expected return vector $\mu$ and covariance matrix $\Sigma$. In practice, sample covariance matrices suffer from severe estimation noise, high condition numbers, and inversion instability ($O(N^3)$), leading to out-of-sample fragility and excessive turnover.

Halperin proposes **Observable Matrix Dynamics (OMD)**, replacing latent statistical estimation with a geometric and dynamic state representation using three fixed-size observable matrices:
1. **Distance Matrix ($D$):** Measures pairwise information distance between assets using angular correlation distances $D_{ij} = \arccos(\rho_{ij})/\pi$.
2. **Return Rank Transition Matrix ($T_R$):** A discrete Markov transition matrix modeling cross-sectional migration across monthly return ranking quantiles.
3. **Volatility Rank Transition Matrix ($T_V$):** A discrete Markov transition matrix modeling cross-sectional migration across monthly realized volatility ranking quantiles.

Empirical analysis in the paper reveals an asymmetry: cross-sectional return ranks are largely unforecastable (mean-reverting and diffuse), whereas volatility ranks exhibit strong one-step-ahead Markovian predictability. By forecasting future volatility ranks and combining them with return-rank expectations and market-removed residual distance diversification, optimal portfolio weights can be constructed directly without matrix inversion.

### Research interpretation

The strategy exploits two distinct structural phenomena:
1. **Volatility Clustering & Cross-Sectional Dispersion:** Volatility states are persistent across months. Low-volatility and high-volatility regimes can be reliably projected forward one period via transition probabilities, allowing dynamic risk weighting without noisy covariance estimation.
2. **Residual Distance Diversification:** Assets that are close in return correlation space share common systematic risk factors. By filtering out the first principal component (market mode) to obtain "market-removed residual distance" $D^{\text{res}}$, an opportunistic long sleeve can maximize idiosyncratic diversification while a long-short sleeve captures cross-sectional momentum.

## Signal

### 1. State Matrix Construction
- **Angular Distance Matrix:** For daily returns $r_{i, \tau}$ over rolling window $W = 252$ days:
  $$\rho_{ij} = \text{Corr}(r_i, r_j), \quad D_{ij} = \frac{\arccos(\rho_{ij})}{\pi} \in [0, 1]$$
- **Cross-Sectional Quantile Binning:**
  - Rank all $N$ assets by 1-month trailing return into $M$ discrete bins $s_{R, i, t} \in \{1, \dots, M\}$ (e.g., $M = 5$ quintiles or $M = 10$ deciles).
  - Rank all $N$ assets by 1-month trailing realized volatility into $M$ discrete bins $s_{V, i, t} \in \{1, \dots, M\}$.
- **Markov Transition Matrices:**
  - $T_R(a, b) = \mathbb{P}(s_{R, i, t+1} = b \mid s_{R, i, t} = a)$
  - $T_V(a, b) = \mathbb{P}(s_{V, i, t+1} = b \mid s_{V, i, t} = a)$

### 2. Predictive Scoring
- **One-Step-Ahead Rank Expectations:**
  $$\hat{s}_{R, i, t+1} = \sum_{b=1}^M b \cdot T_R(s_{R, i, t}, b)$$
  $$\hat{s}_{V, i, t+1} = \sum_{b=1}^M b \cdot T_V(s_{V, i, t}, b)$$
- **Combined Asset Score:**
  $$S_{i, t} = \alpha \cdot \hat{s}_{R, i, t+1} - \beta \cdot \hat{s}_{V, i, t+1}$$
  where $\alpha, \beta \ge 0$ are fixed weighting coefficients.

### 3. Portfolio Allocation Architecture
- **Market-Neutral Long-Short Momentum Sleeve ($w_{\text{LS}}$):**
  - Long the top $K$ assets ranked by $\hat{s}_{R, i, t+1}$ (equal-weighted or inverse-volatility-weighted).
  - Short the bottom $K$ assets ranked by $\hat{s}_{R, i, t+1}$.
  - Net exposure: zero dollar / beta neutral.
- **Opportunistic Long-Only Sleeve ($w_{\text{LO}}$):**
  - Select the top $2K$ assets ranked by combined score $S_{i, t}$.
  - Weight assets to maximize the dispersion of market-removed residual distance:
    $$\max_w \sum_{i, j} w_i w_j D_{ij}^{\text{res}} \quad \text{s.t.} \quad \sum w_i = 1, \; 0 \le w_i \le w_{\max}$$
- **Blended Portfolio:** $w_t = \gamma w_{\text{LS}, t} + (1 - \gamma) w_{\text{LO}, t}$, where $\gamma \in [0.3, 0.5]$.
- **Rebalance Cadence:** Monthly at month-end closing prices.

## Required data

- **Instrument:** S&P 500 equity constituents (or cross-sectional crypto perpetual contracts).
- **Universe:** Top $N = 100$ to $500$ liquid assets by market capitalization and 30-day average daily volume (ADV).
- **Venue:** US Equities (or major crypto derivatives venues: Binance, OKX, Bybit).
- **Timeframe:** Daily OHLCV bars.
- **Fields:**
  - Close price ($P_{i,t}$).
  - Daily return ($r_{i,t}$).
  - Realized volatility ($\sigma_{i,t} = \sqrt{\frac{1}{21} \sum_{\tau=1}^{21} (r_{i, t-\tau} - \bar{r}_i)^2}$).
  - Free-float market capitalization and trading volume.
- **Point-in-time:** Causal monthly ranking updates; survivorship-bias-free historical index constituent panels.

## Execution assumptions

- **Execution Timing:** Rebalancing signals calculated at month-end close (T); orders executed at market open on T+1.
- **Order Type:** Market-on-Open (MOO) or TWAP over the first 30 minutes of the session.
- **Transaction Costs:** 5 to 10 bps per one-way trade in US equities; 2 to 5 bps maker/taker fee + 2 bps slippage in liquid crypto.
- **Borrow / Short Availability:** Assumes availability of borrow for bottom-ranked equity constituents or perpetual shorting capability with standard margin collateral.

## Evidence

### Source-reported

- **Out-of-Sample Performance (OOS-1: Jan 2022 – Dec 2024):**
  - Strategy Sharpe ratio: **1.06** (net of transaction costs).
  - Benchmark S&P 500 Sharpe ratio: **0.78**.
  - Outperformance observed during the 2022 market downturn and subsequent recovery.
- **Out-of-Sample Performance (OOS-2: Jan 2025 – July 2026):**
  - Strategy Sharpe ratio: **1.32** (net of transaction costs).
  - Benchmark S&P 500 Sharpe ratio: **1.14**.
- **Benchmark Comparisons:** Strategy consistently delivered higher risk-adjusted returns than classical Minimum Variance Portfolios (MVP) and Maximum Diversification Portfolios (MDP).
- **Residual Distance Edge:** Adding market-removed residual distance diversification to the long-only sleeve systematically increased annualized return and reduced maximum drawdown compared to equal-weighted or raw-distance sleeves.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Short Momentum Squeeze Risk:** During rapid market regime pivots (e.g., sharp macroeconomic relief rallies), the short leg composed of bottom-ranked momentum stocks can suffer violent short squeezes, eroding long-short sleeve alpha.
- **Cross-Market Fragility:** Independent analyses on non-US equity markets (such as Chinese A-shares) indicate that momentum short legs frequently generate negative returns due to strong mean-reversion characteristics in retail-dominated markets.
- **Monthly Turnover Drag:** If cross-sectional rankings fluctuate rapidly across quartile boundaries, monthly portfolio turnover can exceed 40–60%, creating substantial transaction cost drag.

## Falsification plan

1. **Synthetic Markov Shuffling Test:** Replace the empirical transition matrices $T_R$ and $T_V$ with uniform random stochastic matrices. **Failure rule:** If the strategy Sharpe ratio with true matrices does not exceed the randomized baseline by at least $0.30$ ($p < 0.01$), the OMD predictive mechanism is rejected as spurious curve fitting.
2. **Cost Stress & Turnover Threshold:** Evaluate strategy net Sharpe across stepped transaction cost levels (5, 15, 30, and 50 bps one-way). **Failure rule:** If net Sharpe drops below $0.50$ at 15 bps fee level, the strategy is deemed non-tradable due to turnover friction.
3. **Cross-Sectional Subperiod Walk-Forward Test:** Test across rolling 12-month windows spanning high-inflation (2022), AI rally (2023–2024), and sideways regimes (2025). **Failure rule:** If the long-short sleeve produces negative alpha in $> 40\%$ of 12-month rolling subperiods, the return-rank forecasting hypothesis is falsified.

## Crypto portability

**adapted**

The Observable Matrix Dynamics (OMD) framework ports to cryptocurrency markets with substantial structural adaptations:
- **Universe Definition:** Applied to the top 50–100 liquid perpetual contracts (e.g., Binance / Bybit USDT perps) rather than equity constituents.
- **Shorter Time Horizons:** Due to faster crypto market cycles, monthly ranking windows should be compressed to weekly (7-day) or bi-weekly (14-day) lookbacks to capture rapid momentum rotation.
- **Funding Rate Friction:** The short leg in perpetuals is subject to variable 8-hour funding rates. When the market is deeply negative (bear market), shorting incurs funding penalties, requiring funding-rate adjustment in the combined asset score $S_{i,t}$.
- **Status:** Unproven in crypto until independently backtested on crypto-native perpetual cross-sections.

## Limitations

- **Stationarity Assumption:** Assumes transition matrices $T_R$ and $T_V$ remain relatively stable over multi-year regimes; macroeconomic shocks can cause sudden structural breaks in state transition dynamics.
- **Heuristic Quantile Granularity:** The choice of quantile bins ($M = 5$ vs $10$) and blending parameters ($\alpha, \beta, \gamma$) represents potential hyperparameters subject to overfitting.
- **Capacity Constraints:** The long-short sleeve requires liquid short borrow or perpetual open interest, limiting single-fund capacity in mid-cap constituents.

## Implementation status

No implementation in our research stack. The paper provides theoretical formulation and empirical backtest results from S&P 500 data; no production code or live execution pipeline has been deployed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]] — Cross-sectional momentum quintile sorting
- [[quant/crypto-cross-sectional-volatility-managed-momentum-2026-08-31]] — Volatility-managed momentum strategies
- [[quant/crypto-nonlinear-metastable-langevin-double-well-potential-2026-09-01]] — Non-linear potential dynamics in financial markets

## Sources

1. Igor Halperin, "Are Three Matrices All You Need To Beat the Market? Observable Matrix Dynamics for Portfolio Optimization", arXiv preprint arXiv:2607.27461v1 [q-fin.PM, q-fin.ST], July 29, 2026. URL: https://arxiv.org/abs/2607.27461.
2. Igor Halperin, "Observable Matrix Dynamics of Stocks", arXiv preprint arXiv:2607.19005v1 [q-fin.ST], July 2026. URL: https://arxiv.org/abs/2607.19005.
