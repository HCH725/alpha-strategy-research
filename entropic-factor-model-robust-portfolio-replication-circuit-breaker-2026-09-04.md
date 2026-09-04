---
schema: strategy-research-record-v1
title: Entropic Factor Model for Robust Portfolio Replication and Circuit-Breaker Allocation
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-03
sources:
  - "https://arxiv.org/abs/2609.03552"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Entropic Factor Model for Robust Portfolio Replication and Circuit-Breaker Allocation

## Provenance

- **Primary Source:** Argimiro Arratia (Department of Computer Science, Universitat Politècnica de Catalunya, Barcelona, Spain) and Henryk Gzyl (Centro de Finanzas, IESA, Caracas, Venezuela), *"An Entropic Factor Model for Robust Portfolio Replication"*, arXiv preprint `arXiv:2609.03552v1 [q-fin.PM, q-fin.CP]`, submitted September 3, 2026.
- **Canonical Stable URLs:**
  - Abstract: [https://arxiv.org/abs/2609.03552](https://arxiv.org/abs/2609.03552)
  - Full text HTML: [https://arxiv.org/html/2609.03552v1](https://arxiv.org/html/2609.03552v1)
  - Full text PDF: [https://arxiv.org/pdf/2609.03552v1](https://arxiv.org/pdf/2609.03552v1)
  - DOI: [10.48550/arXiv.2609.03552](https://doi.org/10.48550/arXiv.2609.03552)
- **Licensing:** CC BY-NC-SA 4.0.
- **Verification Integrity:** This record was generated following a complete, line-by-line inspection of the primary paper text, derivations, and numerical tables in `arXiv:2609.03552v1`. No secondary search snippets, AI aggregator summaries, or synthetic extrapolations were used to formulate strategy mechanics or empirical figures. A pre-write repository audit confirmed zero existing records matching `arXiv:2609.03552` or the two-stage Fermi-Dirac entropic factor replication framework.

## Economic mechanism

### Source-reported
Replicating a target benchmark (or factor portfolio) from a restricted basket of assets is fundamentally an ill-posed inverse problem characterized by high collinearity and noisy data. Standard variance-minimization techniques (e.g., Ordinary Least Squares [OLS] or quadratic programming) minimize squared residual errors, which inherently exhibits an "error maximization" property: the optimizer overfits to sample-specific covariance spikes, pushes weights to erratic corner solutions, and misinterprets idiosyncratic data corruption or flash crashes as structural shifts in beta. Under market turbulence, rolling OLS estimators thrash across boundary constraints, creating severe rebalancing churn (portfolio turnover) that erodes net returns after transaction costs.

To solve this, Arratia and Gzyl introduce an information-theoretic framework based on the Principle of Maximum Entropy using a Fermi-Dirac entropy function over box-constrained linear systems:
1. **Stage 1 (Factor Extraction):** Constrains the regression of asset returns against benchmark factors within explicit empirical volatility-ratio bounds, simultaneously optimizing factor loadings $(\beta_{0,i}, \boldsymbol{\beta}_i)$ and residual noise terms $\epsilon_i(t)$ within an empirical noise envelope $[-E_i, E_i]$. The Fermi-Dirac entropy acts as a logarithmic barrier; as residuals approach $E_i$, the marginal entropic cost diverges to infinity, preventing single-period outliers from corrupting structural factor exposures.
2. **Stage 2 (Portfolio Synthesis):** Solves the inverse allocation problem to match desired factor exposures $\boldsymbol{p}$ subject to budget and soft-margin box constraints ($w_i \in [-0.05, 0.999]$). The entropic dual formulation naturally distributes capital across assets, regularizing against extreme concentrations.
3. **Probabilistic Circuit Breaker:** When an asset suffers a massive idiosyncratic failure (e.g., a flash crash or corrupted print) with no corresponding factor movement, the widened uncertainty causes the entropic solver to retreat toward the uninformative prior, drastically slashing capital allocation to the compromised asset rather than doubling down on mean-reversion.

### Research interpretation
The Entropic Factor Model (EFM) is an information-theoretic regularization mechanism for Factor Mimicking Portfolios (FMPs), sparse index replication, and cross-asset factor hedging. Instead of shrinking parameter estimates toward zero (as in $L_1$ Lasso or $L_2$ Ridge regression, which ignore domain-specific economic bounds and cause boundary "sloshing" across rolling windows), EFM pulls parameter loadings toward the center of an empirically bounded domain $\frac{1}{2}(L_{i,j} + U_{i,j})$.

In quantitative execution and portfolio operations, EFM addresses two distinct structural alpha frictions:
- **Turnover Frictional Alpha:** In turbulent regimes (such as the March 2020 COVID-19 crash), unconstrained covariance-matching models thrash allocations attempting to track transient volatility spikes, burning capital on bid-ask spreads and market impact. EFM penalizes epistemic parameter adjustments, drastically lowering turnover (-151.58% annualized turnover reduction in the COVID-19 stress test) while maintaining factor parity.
- **Idiosyncratic Shock Defense:** By treating the noise envelope as an explicit optimization variable with infinite marginal boundary costs, the model does not attempt to "explain" an idiosyncratic jump via inflated factor betas, automatically insulating the replicating portfolio from single-asset blowups.

## Signal

### Mathematical Formulation of the Entropic Inverse Problem
Both stages of EFM solve an underdetermined linear inverse system with box constraints:
$$\boldsymbol{A} \boldsymbol{\xi} = \boldsymbol{y}, \quad \boldsymbol{\xi} \in \mathcal{K} = \prod_{n=1}^N [a_n, b_n]$$

The unique solution $\boldsymbol{\xi}^*$ minimizes the convex Fermi-Dirac entropy:
$$\Psi(\boldsymbol{\xi}) = \sum_{n=1}^N \left( \frac{\xi_n - a_n}{b_n - a_n} \ln\frac{\xi_n - a_n}{b_n - a_n} + \frac{b_n - \xi_n}{b_n - a_n} \ln\frac{b_n - \xi_n}{b_n - a_n} \right)$$
whose Lagrange-Fenchel dual is the moment-generating function:
$$\Phi(\boldsymbol{\tau}) = \sum_{n=1}^N \ln\left( e^{a_n \tau_n} + e^{b_n \tau_n} \right)$$

The dual problem consists of finding the unconstrained vector of Lagrange multipliers $\boldsymbol{\lambda}^* \in \mathbb{R}^M$ that minimizes $-\Sigma(\boldsymbol{\lambda}, \boldsymbol{y})$:
$$-\Sigma(\boldsymbol{\lambda}, \boldsymbol{y}) = \Phi(\boldsymbol{A}^T \boldsymbol{\lambda}) - \langle \boldsymbol{\lambda}, \boldsymbol{y} \rangle = \sum_{n=1}^N \ln\left( e^{a_n (\boldsymbol{A}^T \boldsymbol{\lambda})_n} + e^{b_n (\boldsymbol{A}^T \boldsymbol{\lambda})_n} \right) - \sum_{m=1}^M \lambda_m y_m$$

The reconstructed solution $\boldsymbol{\xi}^*(\boldsymbol{\lambda}^*)$ is given analytically by:
$$\xi_j^* = \frac{a_j e^{a_j (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_j} + b_j e^{b_j (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_j}}{e^{a_j (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_j} + e^{b_j (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_j}}, \quad j = 1, \dots, N$$

Convergence stopping criterion: gradient norm $\|\nabla_{\boldsymbol{\lambda}} \Sigma(\boldsymbol{\lambda}, \boldsymbol{y})\|_2 = \|\boldsymbol{y} - \boldsymbol{A} \boldsymbol{\xi}(\boldsymbol{\lambda})\|_2 < 10^{-5}$.

---

### Stage 1: Factor Loading Extraction ($\boldsymbol{B}$)
Given asset return series $\boldsymbol{X}_i \in \mathbb{R}^T$ and factor matrix $\boldsymbol{F} \in \mathbb{R}^{T \times K}$ over lookback window $T$:
1. **Linear System Setup:**
   $$\boldsymbol{A} = [1 \,\, \boldsymbol{F} \,\, I_T] \in \mathbb{R}^{T \times (1 + K + T)}, \quad \boldsymbol{\xi} = [\beta_{0,i}, \boldsymbol{\beta}_i, \boldsymbol{\epsilon}_i]^T \in \mathbb{R}^{1 + K + T}, \quad \boldsymbol{y} = \boldsymbol{X}_i \in \mathbb{R}^T$$
2. **Empirical Parameter Bounds:**
   - Factor loading bounds for factor $j \in \{1, \dots, K\}$:
     $$L_{i,j} = \inf \left\{ \frac{X_i(t) - X_i(t-1)}{F_j(t) - F_j(t-1)} : t = 2, \dots, T \right\}$$
     $$U_{i,j} = \sup \left\{ \frac{X_i(t) - X_i(t-1)}{F_j(t) - F_j(t-1)} : t = 2, \dots, T \right\}$$
   - Intercept bounds:
     $$L_{0,i} = \inf_{t,j} \left\{ X_i(t) - U_{i,j} F_j(t) : j = 1, \dots, K; \, t = 2, \dots, T \right\}$$
     $$U_{0,i} = \sup_{t,j} \left\{ X_i(t) - L_{i,j} F_j(t) : j = 1, \dots, K; \, t = 2, \dots, T \right\}$$
3. **Data-Driven Noise Envelope:**
   - Central model midpoints:
     $$\hat{\beta}_{0,i}^{\text{mid}} = \frac{1}{2}(L_{0,i} + U_{0,i}), \quad \hat{\beta}_{i,j}^{\text{mid}} = \frac{1}{2}(L_{i,j} + U_{i,j})$$
   - Central model residuals:
     $$\hat{r}_i(t) = X_i(t) - \left( \hat{\beta}_{0,i}^{\text{mid}} + \sum_{j=1}^K \hat{\beta}_{i,j}^{\text{mid}} F_j(t) \right)$$
   - Maximum absolute residual: $r_i^{\max} = \max_t |\hat{r}_i(t)|$.
   - Noise threshold $E_i$:
     $$E_i = \max\left( 1.05 \cdot r_i^{\max}, \, 0.5 \cdot \sigma(X_i) \right)$$
   - Box constraints for asset $i$:
     $$\mathcal{K}_i = [L_{0,i}, U_{0,i}] \times \prod_{j=1}^K [L_{i,j}, U_{i,j}] \times [-E_i, E_i]^T$$
4. **Optimization:** Solve for $\boldsymbol{\lambda}^* \in \mathbb{R}^T$ via L-BFGS or Newton-Raphson to determine $(\beta_{0,i}^*, \boldsymbol{\beta}_i^*)$ for each asset $i = 1, \dots, N$.

---

### Stage 2: Replicating Portfolio Synthesis ($\boldsymbol{w}^*$)
Given estimated factor loadings $\boldsymbol{B} \in \mathbb{R}^{N \times K}$ and desired target factor exposure $\boldsymbol{p} \in \mathbb{R}^K$ (e.g., $\boldsymbol{p} = [1.0]$ for single-factor market replication, or $\boldsymbol{p} = [0.8, 0.2]$ for multi-asset equity/crypto benchmark):
1. **Linear System Setup:**
   $$\boldsymbol{A} = \begin{bmatrix} \boldsymbol{B}^T \\ \mathbf{1}^T \end{bmatrix} \in \mathbb{R}^{(K+1) \times N}, \quad \boldsymbol{\xi} = \boldsymbol{w} \in \mathbb{R}^N, \quad \boldsymbol{y} = \begin{bmatrix} \boldsymbol{p} \\ 1 \end{bmatrix} \in \mathbb{R}^{K+1}$$
2. **Soft-Margin Box Constraints (Remark 1):**
   To eliminate boundary thrashing and artificial turnover spikes, apply soft margins:
   $$w_i \in [a_i, b_i] = [-0.05, 0.999], \quad \forall i \in \{1, \dots, N\}$$
3. **Dual Minimization:**
   Minimize $-\Sigma(\boldsymbol{\lambda}, \boldsymbol{y})$ over $\boldsymbol{\lambda} \in \mathbb{R}^{K+1}$:
   $$-\Sigma(\boldsymbol{\lambda}, \boldsymbol{y}) = \sum_{i=1}^N \ln\left( e^{a_i (\boldsymbol{A}^T \boldsymbol{\lambda})_i} + e^{b_i (\boldsymbol{A}^T \boldsymbol{\lambda})_i} \right) - \sum_{j=1}^K \lambda_j p_j - \lambda_{K+1}$$
   where $(\boldsymbol{A}^T \boldsymbol{\lambda})_i = \sum_{j=1}^K \beta_{i,j} \lambda_j + \lambda_{K+1}$.
4. **Replication Weights Output:**
   $$w_i^* = \frac{a_i e^{a_i (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_i} + b_i e^{b_i (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_i}}{e^{a_i (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_i} + e^{b_i (\boldsymbol{A}^T \boldsymbol{\lambda}^*)_i}}$$
   Re-normalize if strict non-negativity and exact sum-to-one budget compliance is required at trade execution.

---

### Rebalancing and Execution Rules
- **Rebalance Cadence:**
  - Benign / low-turnover regime: 21 trading days (monthly), lookback window $T = 252$ days.
  - High-volatility / stress regime: 10 trading days (biweekly), lookback window $T = 126$ days.
- **Position Sizing:** Directly dictated by the solved weight vector $\boldsymbol{w}^*$. If an asset experiences severe idiosyncratic volatility, its entropic beta expands, driving its weight $w_i^* \to 0$ without manual rules.

## Required data

- **Universe:** 
  - Replication basket: $N$ liquid constituent assets (e.g., large-cap equities, liquid sector ETFs, or major crypto spot/perpetual tokens).
  - Target factors: $K$ factor return series (e.g., SPY for market beta, BTC for crypto market beta, Fama-French style factors, or macroeconomic proxies).
- **Timeframe:** Daily bar closes (OHLCV), evaluated over rolling windows ($T = 126$ or $T = 252$ trading days).
- **Point-in-Time Integrity:**
  - Returns $X_i(t)$ and $F_j(t)$ must be computed strictly on historical closing prices up to timestamp $t$.
  - Rebalance orders are generated at close $t$ for execution at open $t+1$ (or next-bar execution).
- **Data Hygiene & Preprocessing:**
  - Outlier detection is handled natively by the entropic noise envelope $E_i$; no manual winsorization or clipping is required.
  - Zero-division guard: when computing incremental ratios $\frac{X_i(t) - X_i(t-1)}{F_j(t) - F_j(t-1)}$, filter out periods where $F_j(t) = F_j(t-1)$ to prevent singular bounds.

## Execution assumptions

- **Order Types & Fill Timing:** Next-bar market orders or VWAP execution across the rebalancing window.
- **Transaction Cost Model:** Proportional execution friction $c = 10$ basis points ($0.10\%$) applied to gross turnover:
  $$\Delta w_t = \sum_{i=1}^N |w_{i,t} - w_{i,t^-}|, \quad \text{Cost}_t = c \cdot \Delta w_t$$
- **Slippage & Impact:** Linear friction model. Break-even analysis tests friction levels $c \in [1, 50]$ bps.
- **Shorting / Borrowing:** Primarily long-only with soft boundary allowance ($w_i \ge -0.05$) to facilitate interior optimization convergence. No unhedged leverage ($\sum w_i = 1.0$).

## Evidence

### Source-reported
All empirical statistics below trace directly to Arratia & Gzyl (arXiv:2609.03552v1, September 3, 2026), evaluated across five experimental configurations:

#### Experiment 1: Baseline Equity Replication (S&P 500 Tracking via 20 Large Caps)
- **Universe:** 20 US equities across sectors (XOM, CVX, MSFT, AAPL, IBM, INTC, CSCO, AMZN, JPM, BAC, GS, AXP, JNJ, PFE, MRK, PG, KO, WMT, MCD, BA) tracking SPY.
- **Training Period:** 2015-01-01 to 2021-04-20. **Out-of-Sample Test:** 2021-04-21 to 2023-12-29.
- **Reported Out-of-Sample Metrics (Table 1):**
  - Gross Tracking Error (Ann. %): OLS 6.79% vs. **EFM 7.22%**
  - Mean Tracking Bias (Ann. %): OLS 1.36% vs. **EFM 1.08%** (EFM cuts directional drift)
  - Annualized Turnover (%): OLS 117.94% vs. **EFM 115.37%**
  - Annualized Net Return (%): OLS 7.25% vs. **EFM 7.06%**
  - Annualized Volatility (%): OLS 15.13% vs. **EFM 14.50%**
  - Maximum Drawdown (%): OLS 19.24% vs. **EFM 17.53%** (lower drawdown under EFM)
  - Reconstruction Error: $\approx 2 \times 10^{-7}$ for EFM.
- **Factor Sensitivity Identification (Table 7):**
  - OLS estimates for JPM and BA betas: 1.228 and 1.488.
  - EFM estimates for JPM and BA betas: 1.699 and 2.388 (+0.471 and +0.900 higher). EFM flags these assets as hyper-sensitive to market tail variance and defensively curtails their portfolio weights.

#### Experiment 2: Multi-Asset Class Replication (80% SPY + 20% BTC Hybrid Benchmark)
- **Universe:** 20 equities + 2 crypto proxies: Ethereum (ETH-USD) and Litecoin (LTC-USD).
- **Training Period:** 2018-01-03 to 2022-03-11. **Out-of-Sample Test:** 2022-03-14 to 2023-12-29.
- **Target Exposures:** $\boldsymbol{p} = [0.8, 0.2]$.
- **Reported Out-of-Sample Metrics (Table 2):**
  - Gross Tracking Error (Ann. %): OLS 8.68% vs. **EFM 8.65%**
  - Mean Tracking Bias (Ann. %): OLS -1.56% vs. **EFM -1.55%**
  - Annualized Turnover (%): OLS 173.12% vs. **EFM 172.81%**
  - Annualized Net Return (%): OLS 8.64% vs. **EFM 8.66%**
  - Annualized Volatility (%): OLS 21.70% vs. **EFM 21.66%**
  - Maximum Drawdown (%): OLS 27.49% vs. **EFM 27.45%**
  - Structural Proxy Resolution: EFM estimated Bitcoin beta for ETH as 0.999, and for LTC as 1.05, cleanly routing the 20% crypto exposure without manual rule intervention.

#### Experiment 3: Flash Crash / Idiosyncratic Anomaly Stress Test
- **Setup:** Clean 2019 market data; on Day 20, an artificial $-25\%$ return shock was injected into Amazon (AMZN) while the market factor remained flat. 60 days training (including crash), ~191 days out-of-sample testing.
- **Asset Allocation Response (Table 3):**
  - Clean True Benchmark: Beta 1.749.
  - OLS response: Estimated Beta drops to 1.219; assigns **5.73% weight** ("averaging the error" / betting on mean-reversion).
  - EFM response: Estimated Beta flips to **-1.261**; assigns **0.27% weight** (acting as an automated "circuit breaker", cutting exposure to ~1/20th of OLS).
- **Out-of-Sample Tracking Post-Crash (Table 4):**
  - Annualized Net Return (%): OLS 15.54% vs. **EFM 17.01%** (+1.47% net excess return)
  - Mean Tracking Bias (Ann. %): OLS -2.65% vs. **EFM -1.37%** (bias cut by nearly half)
  - Maximum Drawdown (%): OLS 7.92% vs. **EFM 7.73%**
  - Gross Tracking Error (%): OLS 3.55% vs. EFM 3.78%
  - Annualized Turnover (%): OLS 91.42% vs. EFM 91.86%

#### Experiment 4: Rolling-Window Partial Replication Under Trading Frictions (Benign Regime)
- **Setup:** 2018–2023 rolling window ($T = 252$ days, 21-day monthly rebalance, 10 bps transaction friction). Out-of-sample evaluation covers 2019–2023 (5 years).
- **Reported Performance (Table 5):**
  - Gross Tracking Error (%): OLS 4.29% vs. **EFM 5.12%**
  - Mean Tracking Bias (%): OLS 3.07% vs. **EFM 2.87%**
  - Annualized Turnover (%): OLS 139.51% vs. **EFM 135.24%** (-4.27% turnover reduction)
  - Annualized Net Return (%): OLS 18.65% vs. **EFM 18.29%**
  - Break-Even Friction Threshold: $c^* \approx 9.25$ bps. Below 9.25 bps, OLS retains a slight edge in gross tracking variance; above 9.25 bps, EFM dominates on net efficiency.

#### Experiment 5: Real-World COVID-19 Crash Stress Test (Turbulent Regime)
- **Setup:** June 2019 to December 2020 ($T = 126$ days [6 months], 10-day biweekly rebalance, 10 bps transaction friction). Out-of-sample evaluation: December 2019 through December 2020. Benchmark: SPY ETF.
- **Reported Crisis Performance (Table 6):**
  - **Annualized Turnover (%):** OLS 418.51% vs. **EFM 266.93%** (**-151.58% massive turnover reduction!**)
  - **Annualized Net Return (%):** OLS 25.64% vs. **EFM 27.85%** (**+2.21% net annualized outperformance**, vs. SPY buy-and-hold 18.72%)
  - **Maximum Drawdown (%):** OLS 31.27% vs. **EFM 30.04%** (vs. SPY 33.72%)
  - **Annualized Volatility (%):** OLS 33.80% vs. **EFM 33.44%** (vs. SPY 32.38%)
  - **Gross Tracking Error (%):** OLS 5.76% vs. **EFM 6.11%** (conceding only 35 bps in gross precision)
- **Break-Even Friction Analysis:**
  $$c^* = \frac{\text{TE}_{\text{EFM}}^2 - \text{TE}_{\text{OLS}}^2}{2 \cdot (\text{Turnover}_{\text{OLS}} - \text{Turnover}_{\text{EFM}})} = \frac{0.0611^2 - 0.0576^2}{2 \cdot (4.1851 - 2.6693)} \approx \frac{0.000415}{3.0316} \approx 0.000137 \quad (1.37 \text{ bps})$$
  In crisis regimes where real-world spreads and market impact exceed 1.37 bps (typically 20–50 bps), EFM strictly dominates OLS.

### Independently reproduced
Not independently reproduced. All empirical findings, parameter bounds, optimization tolerances, and crisis turnover statistics cited above reflect direct extractions from Arratia & Gzyl (arXiv:2609.03552v1, 2026).

### Negative evidence
- **Frictionless Tracking Precision Gap:** In continuous, low-volatility regimes without meaningful transaction costs ($c < 9.25$ bps), unconstrained OLS achieves lower gross tracking error (4.29% vs. 5.12% in Exp. 4; 6.79% vs. 7.22% in Exp. 1). EFM deliberately trades away unconstrained in-sample variance minimization to enforce structural stability.
- **Parameter Boundary Sensitivity:** If the empirical incremental ratio bounds $[L_{i,j}, U_{i,j}]$ are computed without proper filtering of near-zero factor returns ($F_j(t) \approx F_j(t-1)$), the bounding domain can expand toward infinity, causing EFM to asymptotically degenerate to unconstrained least-squares and losing its entropic regularization benefit.
- **Boundary Thrashing Under Strict Non-Negativity:** When strict $w_i \in [0, 1]$ constraints are enforced during rapid beta regime shifts, the optimizer can experience numerical instability and corner thrashing. Introducing the recommended soft-margin relaxation ($w_i \in [-0.05, 0.999]$) is essential to preserve smooth convergence.

## Falsification plan

1. **Ablation of the Logarithmic Noise Barrier:** Replace the Fermi-Dirac entropy $\Psi(\boldsymbol{\xi})$ in Stage 1 with an $L_2$ quadratic penalty on residuals. If the model fails to trigger the circuit breaker during single-asset return shocks (allocating $> 2.0\%$ weight instead of $< 0.5\%$), the hypothesis that Fermi-Dirac boundary divergence causes defensive pruning is confirmed.
2. **Turnover Under High-Frequency Rebalancing:** Rebalance daily instead of biweekly/monthly. If EFM's turnover advantage over OLS disappears or reverses under daily sampling, EFM's structural parsimony depends on multi-day bar aggregation.
3. **Transaction Friction Break-Even Test:** Evaluate net-of-fee tracking performance across synthetic fee grids $c \in [0.5, 25]$ bps. If the empirical break-even cost $c^*$ significantly exceeds the theoretical $1.37$ bps in turbulent regimes or $9.25$ bps in normal regimes, the quadratic transaction cost model assumption is invalid.
4. **Crypto Spanning Test:** Construct a replicating basket of 15 altcoins to track a BTC+ETH composite factor index. If the entropic solver fails to converge within $10^{-5}$ gradient tolerance or produces tracking errors $> 15\%$ annualized, the empirical bounds formulation requires crypto-specific volatility rescaling.

## Crypto portability

- **Classification:** **Adapted / Unproven**.
- **Empirical Precedent in Paper:** Experiment 2 explicitly verified that EFM handles crypto assets (ETH-USD and LTC-USD) as structural factor proxies for Bitcoin within a multi-asset benchmark, estimating Bitcoin betas of 0.999 (ETH) and 1.05 (LTC).
- **Crypto-Specific Market Frictions:**
  - **24/7 Session Drift & High Idiosyncratic Noise:** Crypto markets do not have market opens/closes. Estimating empirical incremental bounds $\frac{\Delta X_i}{\Delta F_j}$ requires fixed UTC timestamp sampling (e.g., 00:00 UTC) to avoid intraday liquidity distortion.
  - **Fat Tails & Jump Diffusion:** Crypto returns exhibit significantly higher kurtosis and jump frequency than US large-cap equities. The minimum noise floor $0.5 \cdot \sigma(X_i)$ and the 5% padding buffer ($1.05 \cdot r_i^{\max}$) may need widening (e.g., 10–15% buffer) to prevent feasible region collapse.
  - **Perpetual Funding Rate Arbitrage:** For perpetual futures portfolios, the replication target must account for continuous funding rate payments. Holding replicating assets with divergent funding rates creates non-factor tracking drag.
  - **Liquidity Fragmentation & Execution Sinks:** Crypto liquidity is fragmented across Binance, Bybit, OKX, and DEXes. Rebalancing at 10-day intervals could incur higher slippage if constituent tokens have low market depth.

## Limitations

- **Underspecified Dynamic Bound Updating:** The paper evaluates fixed training windows ($T = 126$ and $T = 252$ days) before rebalancing. The exact causal time required to detect that an asset's flash-crash shock has permanently subsided (allowing re-entry) is not parameterized.
- **Soft Margin Leverage Slippage:** The soft-margin bounds $w_i \in [-0.05, 0.999]$ permit nominal short exposures up to $-5\%$ per asset. While this stabilizes numerical convergence, it requires margin capability and cannot be deployed directly in strict cash-only long accounts without post-hoc truncation.
- **Small Universe Evaluation:** The empirical validation utilizes a restricted universe of 20 stocks and 2 crypto tokens. Performance on high-dimensional cross-sections ($N > 500$ assets) was not tested and may face computational scalability constraints in the dual optimization step.

## Implementation status

- **Status:** **not-implemented**.
- **Research Boundary:** This record captures theoretical and empirical research published in arXiv:2609.03552v1. No implementation in `nautilus-quant-system`, PyBroker, or NautilusTrader has been executed. No strategy family has been created, and no backtest campaign has been initiated.

## Adoption boundary

- **Status:** **not-approved**.
- **Approval Scope:** **research-only**.
- **Boundary Contract:** This research capture does not constitute approval for paper trading, testnet deployment, or live capital allocation. Any potential future adoption requires isolated PyBroker factor-screening, signal parity verification, and rigorous out-of-sample backtesting against realistic execution models.

## Related Wiki records

- `[[quant/portfolio-covariance-and-shrinkage-2026-08-28]]` — Classical Ledoit-Wolf and shrinkage regularizers for portfolio covariance.
- `[[quant/phase9-multifactor-portfolio-attribution-cost-handoff-2026-08-28]]` — Multifactor attribution, Factor Mimicking Portfolios, and transaction cost handoffs.
- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]` — Analytical models for turnover friction, market impact, and break-even transaction costs.
- `[[quant/structural-breaks-regime-econometrics-2026-08-28]]` — Covariance destabilization and regime transitions during financial market crises.
- `[[quant/entropic-value-at-risk-tempered-stable-levy-portfolio-optimization-2026-09-02]]` — Entropic risk measures (EVaR) under heavy-tailed non-Gaussian return processes.
- `[[quant/neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02]]` — Regularization of indefinite correlation matrices for high-dimensional portfolios.

## Sources

1. Argimiro Arratia and Henryk Gzyl, *"An Entropic Factor Model for Robust Portfolio Replication"*, arXiv preprint `arXiv:2609.03552v1 [q-fin.PM, q-fin.CP]`, submitted September 3, 2026.
   - Abstract: [https://arxiv.org/abs/2609.03552](https://arxiv.org/abs/2609.03552)
   - Full text HTML: [https://arxiv.org/html/2609.03552v1](https://arxiv.org/html/2609.03552v1)
   - DOI: [10.48550/arXiv.2609.03552](https://doi.org/10.48550/arXiv.2609.03552)
2. Argimiro Arratia and Henryk Gzyl, *"An Entropic Approach to Constrained Linear Regression"*, Mathematics, 13(3), 456, 2025. DOI: [10.3390/math13030456](https://doi.org/10.3390/math13030456).
3. E. T. Jaynes, *"Information theory and statistical mechanics"*, Physical Review, 106(4), 620–630, 1957.
4. M. S. Lobo, M. Fazel, and S. Boyd, *"Portfolio optimization with linear and fixed transaction costs"*, Annals of Operations Research, 152(1), 341–365, 2007.
