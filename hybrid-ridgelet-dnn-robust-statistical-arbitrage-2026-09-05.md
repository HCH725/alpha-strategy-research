---
schema: strategy-research-record-v1
title: "Hybrid Ridgelet Deep Neural Networks for Data-Driven Robust Statistical Arbitrage under Ambiguity and Trading Frictions"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - robust-arbitrage
  - ridgelet-transform
  - deep-neural-networks
  - super-replication
  - model-uncertainty
  - transaction-costs
status: research-only
confidence: medium
source_as_of: "2026-07-08"
sources:
  - "Bahadur Yadav, Sanjay Kumar Mohanty, 'Hybrid Ridgelet Deep Neural Networks for Data-Driven Arbitrage Strategies', Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, published 8 July 2026. DOI: 10.1098/rspa.2026.0123. arXiv preprint: arXiv:2510.10599v1 [q-fin.TR, math.PR], 12 October 2025. https://arxiv.org/abs/2510.10599"
  - "Eva Lütkebohmert, Julian Sester, 'Robust statistical arbitrage strategies', Quantitative Finance, 21(3):379-402, 2021. DOI: 10.1080/14697688.2020.1800806"
  - "Ariel Neufeld, Julian Sester, Daiying Yin, 'Detecting data-driven robust statistical arbitrage strategies with deep neural networks', SIAM Journal on Financial Mathematics, 15(2):436-472, 2024. DOI: 10.1137/22M1520697"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hybrid Ridgelet Deep Neural Networks for Data-Driven Robust Statistical Arbitrage under Ambiguity and Trading Frictions

## Provenance

- **Title:** Hybrid Ridgelet Deep Neural Networks for Data-Driven Arbitrage Strategies
- **Authors:** Bahadur Yadav and Sanjay Kumar Mohanty (Department of Mathematics, School of Advanced Sciences, Vellore Institute of Technology, Vellore 632 014, Tamil Nadu, India)
- **Primary Publication:** *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, published online 8 July 2026, DOI: `10.1098/rspa.2026.0123` (`source-reported`)
- **Preprint Identifier:** arXiv:2510.10599v1 [q-fin.TR, math.PR], submitted 12 October 2025 (`source-reported`)
- **Canonical URLs:** `https://arxiv.org/abs/2510.10599` / `https://arxiv.org/html/2510.10599` / `https://doi.org/10.1098/rspa.2026.0123`
- **Benchmark / Predecessor Formulations:**
  - Robust statistical arbitrage via Linear Programming: Lütkebohmert & Sester (2021), *Quantitative Finance* (`source-reported`)
  - Deep neural network numerical arbitrage detection: Neufeld, Sester & Yin (2024), *SIAM Journal on Financial Mathematics* (`source-reported`)
  - Universal approximation of neural networks with Ridgelet frames: Candès (1999), Sonoda & Murata (2017) (`source-reported`)
- **Primary Dataset:** Historical daily equity closing prices from constituents of the U.S. S&P 500 index spanning 2000-01-03 to 2020-12-31, partitioned into portfolios of 10, 20, 30, 40, and 50 securities diversified across GICS industry sectors (`source-reported`).

## Economic mechanism

### Source-reported

Traditional statistical arbitrage and pairs trading rely heavily on the assumption that asset spreads follow stationary, mean-reverting processes (e.g., cointegrated price paths). In non-stationary markets subject to macroeconomic shocks, structural breaks, or corporate realignments, cointegration breaks down, resulting in persistent divergence and catastrophic drawdown.

To overcome the fragility of single-measure models, the authors formulate statistical arbitrage under **Knightian model uncertainty**:
- **Ambiguity Set ($\mathcal{P}$):** Rather than assuming a single physical probability measure $\mathbb{P}$, market dynamics are represented by a non-empty ambiguity set $\mathcal{P} \subseteq \mathcal{M}_1(\Omega)$ of Borel probability measures representing plausible physical models (`source-reported`).
- **$\mathcal{P}$-Robust $\mathcal{G}$-Arbitrage:** A self-financing trading strategy $\Delta$ is defined as a robust arbitrage if:
  1. $\mathbb{E}_P[(\Delta \cdot S)_n - E_n(\Delta) \mid \mathcal{G}] \geq 0$ $P$-a.s. for all $P \in \mathcal{P}$ (non-negative conditional expectation under every measure in the ambiguity set);
  2. $\mathbb{E}_P[(\Delta \cdot S)_n - E_n(\Delta)] > 0$ for some $P \in \mathcal{P}$ (strictly positive expected gain under at least one measure) (`source-reported`).
- **Super-Replication Duality:** When conditioning on terminal prices $\mathcal{G} = \sigma(S_{t_n})$, finding a robust statistical arbitrage corresponds to evaluating whether the conditional super-replication price of the zero payoff $\mathcal{X}_{B,L}(0, \sigma(S_{t_n})) < 0$. A negative super-replication cost proves the existence of a bounded, Lipschitz-continuous trading strategy that extracts positive initial capital while guaranteeing non-negative conditional payoff across all models in $\mathcal{P}$ (`source-reported`).
- **Ridgelet Representation & Universal Density:** Standard feedforward neural networks struggle with high-dimensional sparse representations and curse of dimensionality. The continuous Ridgelet Transform maps functions into continuous superpositions of ridge functions $\psi(a \cdot x - b)$. By Lemma 3.4 and Proposition 3.5, the space of ridgelet strategies $\mathrm{Ridge}_{i,B,L}$ is dense in the space of bounded, $L$-Lipschitz strategies $\mathcal{W}_{B,L}$ under the uniform topology. This enables Hybrid Ridgelet Deep Neural Networks (HRDNN) to approximate the infinite-dimensional super-replication functional $\mathcal{X}_{B,L}(\Phi, \sigma(S_{t_n}))$ with guaranteed convergence (`source-reported`).

### Research interpretation

The economic thesis of robust statistical arbitrage shifts the alpha source from **directional forecasting** or **linear mean reversion** to **manifold misalignment under model uncertainty**. In a basket of 10 to 50 correlated equities, asset prices lie on a high-dimensional non-linear manifold governed by common factor exposures and sector linkages. 

By training the neural network with a penalized loss function that enforces non-negative conditional expectations across all sampled empirical measures in $\mathcal{P}$, the model extracts arbitrage profits from structural dislocations between basket components. The Ridgelet basis provides an effective inductive bias: because ridge functions $\psi(a \cdot x - b)$ are constant along hyperplanes orthogonal to $a$, they naturally identify planar and co-movement constraints among multi-asset baskets.

However, in practice, the ambiguity set $\mathcal{P}$ is populated with historical empirical paths. If an unprecedented regime shift occurs outside the convex hull of $\mathcal{P}$, the theoretical zero-loss guarantee dissolves into an empirical statistical bet with downside tail risk (`research-proposed`).

## Signal

### Mathematical Formulation of Trading Strategy

Let $S_{t_i} = (S_{t_i}^1, \dots, S_{t_i}^a) \in \mathbb{R}^a$ denote the prices of $a$ assets at discrete dates $t_1 < \dots < t_n$, where prices are constrained to compact intervals $S_{t_i}^j \in [\underline{U}^j, \overline{U}^j]$ (`source-reported`).

A trading strategy is a sequence of decision rules $\Delta = (\Delta_i^j)_{i=0,\dots,n-1}^{j=1,\dots,a}$, where at time $t_i$, the position $\Delta_i^j(S_{t_1}, \dots, S_{t_i}) = h_i^j$ is an $L$-Lipschitz function bounded by $B$ (`source-reported`):
- Initial position $\Delta_0^j \in \mathbb{R}$ is constant with $|\Delta_0^j| \leq B$ (`source-reported`).
- Budget constraint: $\|\Delta_i^j\|_{\infty, \Omega_i} \leq B$ (`source-reported`).
- Gross trading profit:
  $$(\Delta \cdot S)_n = \sum_{j=1}^a \sum_{i=0}^{n-1} \Delta_i^j(S_{t_1}, \dots, S_{t_i}) (S_{t_{i+1}}^j - S_{t_i}^j) \quad \text{(`source-reported`)}$$

### Neural Network Architecture & Optimization

1. **Architecture:**
   - Input: Historical price vector $(S_{t_1}, \dots, S_{t_i}) \in \mathbb{R}^{ia}$ processed through a Batch Normalization layer (`source-reported`).
   - Hidden Layers: Three fully connected layers with $32a$, $64a$, and $128a$ neurons, where $a$ is the asset count (`source-reported`).
   - Activation Functions: Tested across SiLU, GELU, Mish, ReLU, and HRDNN (hybrid ridgelet parametrization) (`source-reported`).
   - Output: Asset allocation vector $\Delta_i \in [-B, B]^a$ (`source-reported`).
2. **Terminal State Discretization (Pseudo-Algorithm):**
   - The continuous terminal $\sigma$-algebra $\sigma(S_{t_n})$ is discretized into finite random rectangular partitions $\mathcal{F}_i = \{ S_{t_n}^{-1}(A) : A \in \sigma(H_i) \}$, where $A_i = (p_1^{(i)}, q_1^{(i)}] \times \dots \times (p_a^{(i)}, q_a^{(i)}]$ with $p_j^{(i)} \sim [\underline{U}^j, \overline{U}^j]$ and $q_j^{(i)} \equiv \overline{U}^j$ (`source-reported`).
3. **Penalized Objective Function:**
   - The network minimizes the penalized functional:
     $$\mathcal{X}_{B,L,k}^{\mathrm{Ridge}}(0, \mathcal{F}_i) = \inf_{w_{c,\Delta} \in \mathcal{W}_{B,L}^{\mathrm{Ridge}}} \left\{ c + k \sum_{P \in \mathcal{P}} \int_\Omega \beta\left(\mathbb{E}_P[-w_{c,\Delta}(S) \mid \mathcal{F}_i]\right) dP \right\} \quad \text{(`source-reported`)}$$
   - Penalty function $\beta(x) = 0$ for $x \le 0$ and $\beta(x) > 0$ for $x > 0$, penalizing violations of the conditional super-replication bound (`source-reported`).
4. **Hyperparameters:**
   - Learning rate: $\eta = 1 \times 10^{-4}$ for portfolios with $a \ge 10$ assets (`source-reported`).
   - Training iterations: 1 to 50 iterations; performance peaks near iteration 39 (`source-reported`).
   - Trading cadence: 1-month rebalancing horizon with 1 intermediate trade per cycle ($n=2$) (`source-reported`).
   - Hardware: High-Performance Computing (HPC) cluster with 2 $\times$ NVIDIA H100 NVL GPUs (`source-reported`).

## Required data

- **Asset Universe:** Constituents of the S&P 500 equity index selected to span diverse Global Industry Classification Standard (GICS) sectors (`source-reported`):
  - **10-Asset Universe:** OKE (ONEOK, Energy), PG (Procter & Gamble, Consumer Staples), RCL (Royal Caribbean, Consumer Discretionary), SBUX (Starbucks, Consumer Discretionary), UNM (Unum Group, Financials), USB (U.S. Bancorp, Financials), VMC (Vulcan Materials, Materials), WELL (Welltower, Real Estate), WMB (Williams Companies, Energy), XOM (Exxon Mobil, Energy) (`source-reported`).
  - **20-Asset Universe:** Adds APA, BXP, DXC, F, GD, GS, HPQ, IT, MCD, MMM (`source-reported`).
  - **30-Asset Universe:** Adds GL, HST, LUV, MO, OMC, PCAR, RTX, VFC, XEL, YUM (`source-reported`).
  - **40-Asset Universe:** Adds ATO, CNP, GAP, JNJ, K, NTAP, STT, TAP, TXT, WFC (`source-reported`).
  - **50-Asset Universe:** Expanded to 50 diversified constituents (`source-reported`).
- **Data Fields:** Daily closing prices ($S_{t_i}^j$) (`source-reported`).
- **Data Splits:**
  - Training Period: 2000-01-03 to 2015-11-25 (3,999 trading days) (`source-reported`).
  - Testing Period: 2015-11-26 to 2020-12-31 (1,283 trading days / 61 monthly evaluation cycles, encompassing the March 2020 COVID-19 crash) (`source-reported`).
  - Benchmark Comparison Split (Linear Programming on S&P 500 index): Training 1900-01 to 2013-12; Testing 2013-09 to 2024-12 (`source-reported`).
- **Point-in-Time & Survivorship:** The universe selection requires stocks to be listed and active across the entire 2000–2020 window, introducing survivorship bias (`source-reported` limitation).

## Execution assumptions

- **Total Cost Equation:**
  $$E_n(\Delta) = \sum_{i=0}^{n-1} \sum_{j=1}^a \left[ T_i^j(S_{t_i}^j, x_i^j) + L_i^j(S_{t_i}^j, x_i^j) + B_i^j(S_{t_i}^j, x_i^j) \right] \quad \text{(`source-reported`)}$$
  where $x_i^j = \Delta_i^j - \Delta_{i-1}^j$ is the trade volume (`source-reported`).
- **Three Friction Components:**
  1. **Transaction Costs ($T_i^j$):**
     - Zero Transaction Costs (ZTC): $\lambda_T = 0.0$ (`source-reported`).
     - Proportional Transaction Costs (PTC): $\lambda_T = 0.001$ ($10\text{ bps}$ of traded dollar volume, $T_i^j = \lambda_T S_{t_i}^j |x_i^j|$) (`source-reported`).
     - Per-Share Transaction Costs (PSTC): $\lambda_T = 0.01$ ($\$0.01$ per share traded, $T_i^j = \lambda_T |x_i^j|$) (`source-reported`).
  2. **Bid-Ask Spread / Liquidity Cost ($L_i^j$):**
     - Symmetric spread around mid-price: $\lambda_L = 0.0002$ ($2\text{ bps}$, $L_i^j = \lambda_L S_{t_i}^j |x_i^j|$) (`source-reported`).
  3. **Short Borrowing Cost ($B_i^j$):**
     - Incurred only on short positions: $B_i^j = \lambda_B S_{t_i}^j |x_i^j| \cdot \mathbf{1}_{\{x_i^j < 0\}}$, with daily borrow rate $\lambda_B = 0.10 / 252$ (annualized $10\%$ borrowing cost) (`source-reported`).
- **Execution Fill Model:** Trades executed at daily close prices without intra-day slippage or market impact (`source-reported`).
- **Execution Lag:** Assumes frictionless instant execution at the close of observation date $t_i$ (`source-reported`). A realistic 1-bar execution delay is not modeled (`research-proposed`).
- **Portfolio Sizing & Leverage:** Strategy is self-financing subject to component budget bounds $\|\Delta_i^j\|_{\infty} \le B$ (`source-reported`). Explicit margin call mechanics or cash buffers are omitted (`research-proposed`).

## Evidence

### Source-reported

Empirical results from Yadav & Mohanty (2025/2026, *Proc. R. Soc. A*, arXiv:2510.10599v1) evaluated over the out-of-sample test period (2015-11-26 to 2020-12-31):

#### 1. Predictive Accuracy Across Activations (Tables 1 & 2 in source)

| Portfolio Size | Metric | SiLU | GELU | Mish | ReLU | HRDNN |
|---|---|---|---|---|---|---|
| **10 Assets** | RMSE | **1.4922** | 1.5416 | 1.5384 | 1.7196 | 1.6637 |
| | MAE | **0.9094** | 0.9378 | 0.9526 | 1.0926 | 1.0409 |
| | $R^2$ | **0.9977** | **0.9977** | 0.9976 | 0.9970 | 0.9972 |
| **50 Assets** | RMSE | **1.8499** | 1.9187 | 2.2086 | 3.0853 | 2.5458 |
| | MAE | **1.1117** | 1.1485 | 1.3882 | 2.2244 | 1.7278 |
| | $R^2$ | **0.9983** | 0.9982 | 0.9976 | 0.9952 | 0.9967 |

#### 2. 10-Asset Portfolio Performance Under Varying Frictions (Tables 3, 4, 5 in source)

| Cost Setting | Metric | SiLU | B&H Benchmark | GELU | Mish | ReLU | HRDNN |
|---|---|---|---|---|---|---|---|
| **ZTC** | Overall Profit | 121.93 | -283.70 | 93.99 | 111.22 | 113.34 | **138.13** |
| | Average Profit | 1.02 | -2.36 | 0.78 | 0.93 | 0.94 | **1.15** |
| | % Profitable Trades | 54.22% | 60.00% | 55.22% | 54.60% | 56.65% | **58.48%** |
| | Sharpe Ratio | **0.1643** | -0.0430 | 0.0820 | 0.1159 | 0.0979 | 0.1325 |
| | Sortino Ratio | **0.2659** | -0.0370 | 0.1392 | 0.1599 | 0.1333 | 0.1921 |
| **PTC (10 bps)** | Overall Profit | **94.58** | -449.06 | 67.07 | 57.56 | 66.38 | 75.23 |
| | Average Profit | **0.79** | -3.74 | 0.56 | 0.48 | 0.55 | 0.63 |
| | % Profitable Trades | 52.12% | 60.00% | 53.37% | 50.72% | 55.15% | **65.78%** |
| | Sharpe Ratio | **0.1085** | -0.0680 | 0.0325 | 0.0405 | 0.0346 | 0.0257 |
| | Sortino Ratio | **0.2029** | -0.0580 | 0.0876 | 0.1526 | 0.0646 | 0.0569 |
| **PSTC ($0.01/sh)** | Overall Profit | 87.57 | -523.70 | 64.65 | 87.57 | 88.05 | **94.66** |
| | Average Profit | 0.73 | -4.36 | 0.54 | 0.73 | 0.73 | **0.79** |
| | % Profitable Trades | 52.18% | 60.00% | 52.90% | 52.18% | 56.07% | **56.92%** |
| | Sharpe Ratio | **0.0835** | -0.0790 | 0.0265 | **0.0835** | 0.0540 | 0.0722 |
| | Sortino Ratio | **0.1623** | -0.0680 | 0.0805 | **0.1623** | 0.0800 | 0.1059 |

#### 3. Scalability Across Higher-Dimensional Portfolios (Tables 6, 7, 8 in source)

- **20 Assets (ZTC, Table 6):**
  - Overall Profit: HRDNN **489.40** vs ReLU 365.41, GELU 151.71, SiLU 103.18, Mish 60.51, B&H -331.27
  - Average Profit: HRDNN **4.08** vs ReLU 3.05, B&H -2.76
  - % Profitable Trades: HRDNN **64.88%** vs GELU 63.10%, B&H 61.67%
  - Sharpe Ratio: HRDNN **0.1258** vs GELU 0.0887, ReLU 0.0857, SiLU 0.0724, B&H -0.0220
  - Sortino Ratio: HRDNN **0.0974** vs GELU 0.0822, ReLU 0.0817, B&H -0.0210
- **30 Assets (PTC 10 bps, Table 7):**
  - Overall Profit: HRDNN **871.49** vs ReLU 599.74, GELU 452.54, Mish 380.84, SiLU 371.79, B&H -839.85
  - Average Profit: HRDNN **7.26** vs ReLU 5.00, B&H -7.00
  - % Profitable Trades: HRDNN **64.13%** vs GELU 61.82%, B&H 61.67%
  - Sharpe Ratio: SiLU **0.1797**, GELU 0.1725, HRDNN 0.1313, Mish 0.1225, ReLU 0.0520, B&H -0.0440
  - Sortino Ratio: SiLU **0.1740**, GELU 0.1556, Mish 0.1156, HRDNN 0.1045, B&H -0.0410
- **40 Assets (PSTC $0.01/sh, Table 8):**
  - Overall Profit: HRDNN **1042.54** vs ReLU 977.64, GELU 757.57, SiLU 637.35, Mish 613.16, B&H -1475.84
  - Average Profit: HRDNN **8.69** vs ReLU 8.15, B&H -12.30
  - % Profitable Trades: HRDNN **66.82%** vs ReLU 64.97%, GELU 64.28%, B&H 61.67%
  - Sharpe Ratio: SiLU **0.1928**, GELU 0.1824, HRDNN 0.1372, Mish 0.1310, ReLU 0.1064, B&H -0.0630
  - Sortino Ratio: SiLU **0.1899**, GELU 0.1607, Mish 0.1214, HRDNN 0.1057, B&H -0.0580

#### 4. 50-Asset Portfolio Performance Across Cost Regimes (Tables 9, 10, 11 in source)

| Setting | Metric | SiLU | B&H Benchmark | GELU | Mish | ReLU | HRDNN |
|---|---|---|---|---|---|---|---|
| **ZTC** | Overall Profit | 948.63 | 327.79 | 727.70 | -523.26 | 636.73 | **1548.50** |
| | Average Profit | 7.91 | 2.73 | 6.06 | -4.36 | 5.31 | **12.90** |
| | % Profitable Trades | 64.60% | 65.00% | 61.90% | 65.00% | 62.78% | **67.00%** |
| | Maximum Profit | 1103.61 | **3991.14** | 1101.62 | 3984.52 | 1198.78 | 1639.17 |
| | Minimum Profit | -958.17 | -7118.32 | -978.98 | -7124.48 | -1174.59 | -3120.32 |
| | Sharpe Ratio | **0.2562** | 0.0120 | 0.1947 | -0.0190 | 0.1452 | 0.1777 |
| | Sortino Ratio | **0.2623** | 0.0110 | 0.2049 | -0.0170 | 0.1416 | 0.1377 |
| **PTC (10 bps)** | Overall Profit | 727.70 | -523.26 | 819.92 | 577.49 | 868.70 | **1068.31** |
| | Average Profit | 6.06 | -4.36 | 6.83 | 4.81 | 7.24 | **8.90** |
| | % Profitable Trades | 61.90% | 65.00% | 63.53% | 61.58% | 63.55% | **65.38%** |
| | Maximum Profit | 1101.62 | **3984.52** | 1218.64 | 1278.04 | 1777.29 | 1610.55 |
| | Minimum Profit | -978.98 | -7124.48 | -1419.34 | -1465.63 | -4018.29 | -3126.47 |
| | Sharpe Ratio | **0.1947** | -0.0190 | 0.1801 | 0.1142 | 0.0781 | 0.1206 |
| | Sortino Ratio | **0.2049** | -0.0170 | 0.1667 | 0.1166 | 0.0627 | 0.0942 |
| **PSTC ($0.01/sh)** | Overall Profit | 636.73 | -872.20 | 783.52 | 450.06 | 934.47 | **1036.16** |
| | Average Profit | 5.31 | -7.27 | 6.53 | 3.75 | 7.79 | **8.63** |
| | % Profitable Trades | 62.78% | 65.00% | 64.03% | 62.50% | 64.47% | **66.23%** |
| | Maximum Profit | 1198.78 | **3981.14** | 1366.01 | 1387.04 | 1925.53 | 1829.21 |
| | Minimum Profit | -1174.59 | -7128.32 | -1742.62 | -1772.34 | -4577.70 | -3745.27 |
| | Sharpe Ratio | **0.1452** | -0.0320 | 0.1419 | 0.0735 | 0.0738 | 0.0990 |
| | Sortino Ratio | **0.1416** | -0.0280 | 0.1232 | 0.0669 | 0.0573 | 0.0756 |

#### 5. Comparison With Linear Programming (Section 4.4 in source)
- Tested on S&P 500 index from 1900 to 2024 for low-dimensional cases ($a \leq 3$).
- HRDNN consistently generates higher out-of-sample Sharpe ratios than the LP-based formulation across iterations 1 through 50, with performance peaking around iteration 39.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Sharpe Ratio Erosion Under Proportional Frictions:** While HRDNN dominates in raw cumulative dollar profits ($1068.31$ vs $727.70$ for SiLU on 50 assets PTC), its Sharpe ratio ($0.1206$) is substantially lower than SiLU ($0.1947$) and GELU ($0.1801$). This reflects higher return volatility induced by large position swings.
- **Pronounced Downside Tail Spikes:** Across all high-dimensional tests, HRDNN exhibits severe negative outlier trades (e.g., minimum trade profit of $-3126.47$ under 50-asset PTC and $-3745.27$ under PSTC). While these losses are smaller than buy-and-hold ($-7124.48$), they indicate that the theoretical non-negativity condition fails out-of-sample during acute market stress (such as the March 2020 liquidity shock).
- **Friction Sensitivity:** On 10 assets under proportional transaction costs (Table 4), HRDNN's Sharpe ratio collapses from $0.1325$ (ZTC) to $0.0257$ (PTC), demonstrating extreme vulnerability to transaction friction in smaller baskets.
- **Survivorship & Selection Bias:** Selecting 50 S&P 500 stocks with continuous 21-year trading histories over 2000–2020 excludes all firms that failed, went bankrupt, or were acquired during the 2000 dot-com crash or 2008 global financial crisis.

## Falsification plan

To test whether the statistical arbitrage edge generated by HRDNN represents robust risk-adjusted alpha or is an artifact of survivorship bias and unmodeled execution latency, the following empirical tests are specified:

1. **Point-in-Time Universe Survivorship Audit:**
   - Reconstruct the 50-asset portfolio dynamically using point-in-time S&P 500 constituent lists, including delisted and bankrupt entities (e.g., Enron, Lehman Brothers, Washington Mutual).
   - `research-defined falsification threshold`: If the out-of-sample Sharpe ratio under PTC drops below $0.02$ or annualized return turns negative, the strategy's profitability is falsified as survivorship-conditioned lookahead bias.
2. **Execution Latency & Next-Bar Fill Stress Test:**
   - Impose a mandatory 1-bar execution delay: compute signals at close $t_i$ and execute at the open or volume-weighted average price (VWAP) of bar $t_i+1$.
   - `research-defined falsification threshold`: If net profit on 50 assets under PTC drops by $\ge 40\%$ compared to same-close fills, the strategy is falsified as reliant on simultaneous execution leakage.
3. **Transaction Cost & Slippage Hurdle Test:**
   - Increase proportional transaction costs from $10\text{ bps}$ to $25\text{ bps}$ (reflecting true institutional execution costs for mid-cap constituents during volatile periods).
   - `research-defined falsification threshold`: If HRDNN cumulative net profit becomes negative under $25\text{ bps}$ PTC, the claim of robust tradability under real-world market frictions is falsified.
4. **Placebo / Non-Cointegrated Synthetic Market Test:**
   - Train and evaluate HRDNN on synthetic baskets generated via independent, drift-matched Geometric Brownian Motion paths where true economic arbitrage is mathematically absent.
   - `research-defined falsification threshold`: If the model detects statistically significant "arbitrage" profits ($t > 2.0$, $p < 0.05$) on pure noise, the optimization framework is falsified as prone to spurious numerical overfitting.
5. **Ablation of Ridgelet Representation vs. Standard Feedforward Architecture:**
   - Train an identical 3-layer MLP architecture using standard dense layers without the Ridgelet frame.
   - `research-defined falsification threshold`: If the standard MLP achieves comparable or superior out-of-sample risk-adjusted returns (paired two-tailed $t$-test $p > 0.10$ across 20 random seeds), the theoretical advantage of the Ridgelet Transform is falsified in financial time series.

## Crypto portability

**Portability Classification:** `adapted`

The primary source evaluates U.S. equities listed on the NYSE/NASDAQ. Porting the robust statistical arbitrage framework to cryptocurrency markets is unproven and constitutes research interpretation. Structural cryptocurrency adaptations must be resolved:

1. **Spot vs. Perpetual Funding Carry:** In equities, short positions incur a static borrowing fee ($\lambda_B = 0.10 / 252$). In crypto perpetual markets, short and long positions exchange 8-hour funding rates. In high-funding bull regimes, holding short legs creates severe negative carry drag; during bear cascades, funding flows reverse (`research-proposed`).
2. **24/7 Session & Intra-Month Gap Risk:** Equities observe nightly closes and weekend breaks. Crypto trades 24/7/365 with frequent flash crashes and weekend liquidity dry-ups. A coarse 1-month rebalancing horizon leaves crypto baskets highly exposed to intra-month liquidation shocks (`research-proposed`).
3. **Exchange Fragmentation & Mark Price Liquidation:** Unlike centralized clearing via DTCC, crypto trading is fragmented across Binance, Bybit, OKX, and DEXs. Baskets must model basis divergence between spot, index, and mark prices, as well as exchange-specific maintenance margin liquidation thresholds (`research-proposed`).
4. **Elevated Bid-Ask Spread & Slippage:** Crypto altcoin baskets rarely exhibit $2\text{ bps}$ bid-ask spreads; real-world slippage and spread during volatile sell-offs typically exceed $15\text{--}50\text{ bps}$, which would substantially degrade HRDNN performance (`research-proposed`).

## Limitations

- **Survivorship-Biased Universe:** Equities selected were required to survive continuously from 2000 to 2020.
- **Coarse Rebalancing Cadence:** Strategy assumes only 1 intermediate trade per monthly cycle ($n=2$), ignoring higher-frequency intraday momentum and volatility spikes.
- **Heavy Compute Requirement:** Training high-dimensional HRDNN models requires multi-GPU HPC infrastructure (dual NVIDIA H100 NVL GPUs), limiting real-time deployment on commodity hardware.
- **Downside Tail Vulnerability:** Despite theoretical non-negativity guarantees, out-of-sample stress regimes produce massive negative individual trades ($-3,745.27$ on 50 assets).
- **Preprint / Underspecified Repository:** Open-source code and checkpoint weights were not publicly hosted in an immutable repository at the time of arXiv submission.

## Implementation status

`not-implemented`

This strategy has not been implemented or verified in our quantitative research backtesting stack (`nautilus-quant-system` or `PyBroker`). It is documented here strictly as normalized research material.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an upstream academic research capture. Inclusion in this repository does not constitute evidence of live profitability, approval for production implementation, or permission for paper, testnet, or live trading deployment.

## Related Wiki records

- `[[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]` — Deep learning factor replication and Ornstein-Uhlenbeck statistical arbitrage.
- `[[quant/dynamic-johansen-deep-weighted-ensemble-cryptocurrency-pairs-2026-09-05]]` — Dynamic cointegration and deep weighted ensemble pairs trading in crypto.
- `[[quant/graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05]]` — Graph-based maximum weight matching for statistical arbitrage portfolios.
- `[[quant/moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05]]` — Moving band statistical arbitrage with convex-concave portfolio optimization.
- `[[quant/attention-factors-statistical-arbitrage-residual-portfolios-2026-09-02]]` — Attention factors for statistical arbitrage on residual equity portfolios.

## Sources

1. Bahadur Yadav, Sanjay Kumar Mohanty. "Hybrid Ridgelet Deep Neural Networks for Data-Driven Arbitrage Strategies." *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, published 8 July 2026. DOI: `10.1098/rspa.2026.0123`. Supplementary data on Figshare: `https://doi.org/10.6084/m9.figshare.c.8519915`.
2. Bahadur Yadav, Sanjay Kumar Mohanty. "Hybrid Ridgelet Deep Neural Networks for Data-Driven Arbitrage Strategies." arXiv preprint: arXiv:2510.10599v1 [q-fin.TR, math.PR], submitted 12 October 2025. URL: `https://arxiv.org/abs/2510.10599` / `https://arxiv.org/html/2510.10599`.
3. Eva Lütkebohmert, Julian Sester. "Robust statistical arbitrage strategies." *Quantitative Finance*, 21(3):379–402, 2021. DOI: `10.1080/14697688.2020.1800806`.
4. Ariel Neufeld, Julian Sester, Daiying Yin. "Detecting data-driven robust statistical arbitrage strategies with deep neural networks." *SIAM Journal on Financial Mathematics*, 15(2):436–472, 2024. DOI: `10.1137/22M1520697`.
