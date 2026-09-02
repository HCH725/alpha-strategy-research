---
schema: strategy-research-record-v1
title: "Statistical Arbitrage in Rank Space: Deep Neural Networks, Hybrid-Atlas Rank Decomposition, and Intraday Collision Rebalancing"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - rank-space
  - deep-learning
  - cnn-transformer
  - stochastic-portfolio-theory
  - hybrid-atlas-model
  - mean-reversion
  - pca-market-decomposition
  - intraday-rebalancing
status: research-only
confidence: high
source_as_of: 2026-06-29
sources:
  - "Ying-Fei Li and George C. Papanicolaou, 'Statistical Arbitrage in Rank Space', arXiv:2410.06568v2 [q-fin.MF, stat.ML], revised June 29, 2026. DOI: https://doi.org/10.48550/arXiv.2410.06568. GitHub: https://github.com/Infi-Yingfei-Li/stats-arb-rank-space, commit a526f711720959c930971aff71efbecd72ad4bbd."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Statistical Arbitrage in Rank Space: Deep Neural Networks, Hybrid-Atlas Rank Decomposition, and Intraday Collision Rebalancing

## Provenance

- **Canonical Academic Source:** Ying-Fei Li (Department of Applied Physics, Department of Statistics, Stanford University) and George C. Papanicolaou (Department of Mathematics, Stanford University), *"Statistical Arbitrage in Rank Space"*, arXiv preprint `arXiv:2410.06568v2 [q-fin.MF, stat.ML]`, submitted October 9, 2024, last revised June 29, 2026.
- **Canonical DOI:** [10.48550/arXiv.2410.06568](https://doi.org/10.48550/arXiv.2410.06568).
- **Stable Source URLs:**
  - Abstract: [https://arxiv.org/abs/2410.06568](https://arxiv.org/abs/2410.06568)
  - Version 2 Abstract: [https://arxiv.org/abs/2410.06568v2](https://arxiv.org/abs/2410.06568v2)
  - Full Text HTML: [https://arxiv.org/html/2410.06568v2](https://arxiv.org/html/2410.06568v2)
  - Full Text PDF: [https://arxiv.org/pdf/2410.06568v2](https://arxiv.org/pdf/2410.06568v2)
- **Evaluation Code Scaffold & Replication Package:**
  - GitHub Repository: [https://github.com/Infi-Yingfei-Li/stats-arb-rank-space](https://github.com/Infi-Yingfei-Li/stats-arb-rank-space)
  - Immutable Commit SHA: `a526f711720959c930971aff71efbecd72ad4bbd`
  - Core Execution Scripts:
    - `main_rank.py`: Primary training, evaluation, and backtesting runner for rank-space statistical arbitrage.
    - `main_name.py`: Comparative baseline runner for name-space statistical arbitrage.
    - `main_rank_high_freq.py`: High-frequency intraday rebalancing pipeline.
    - `trading_signal/trading_signal.py`: Signal extraction modules for Ornstein-Uhlenbeck (OU) and CNN-Transformer architectures.
    - `portfolio_weights/portfolio_weights.py`: Portfolio weight construction and mean-variance optimization layer.
    - `market_decomposition/market_factor_classic.py`: PCA market decomposition in name and rank spaces.
    - `neural_network/neural_network.py`: Multi-channel 1D CNN and Multi-Head Attention Transformer encoder implementation.
    - `notebook/portfolio_performance_PnL/portfolio_performance_PnL.ipynb`: PnL calculation, transaction cost analysis, and benchmark tables.
- **Empirical Sample Horizon:**
  - Full data coverage: January 1990 to December 2022 (CRSP daily returns and prices; Kenneth French 1-month T-bill risk-free rate; Polygon.io 1-minute intraday prices from January 2005 to December 2022).
  - Out-of-sample backtest window: January 2007 to December 2022 (16 complete calendar years).

## Economic mechanism

### Source-reported

1. **Failure of Deep Learning in Name Space:**
   - In equity markets, stocks are traditionally indexed by fixed corporate identifiers (company names or tickers), referred to as *name space*.
   - In name space, individual stock return series suffer from extreme non-stationarity, shifting idiosyncratic regimes, low signal-to-noise ratios, and multi-factor complexity (where multiple eigenvalues exceed the Marchenko-Pastur bulk).
   - Consequently, deep neural networks (DNNs) trained on cumulative residual returns in name space fail to generalize, yielding flat or negative risk-adjusted returns out-of-sample.

2. **Stationary Distribution and Spectral Concentration in Rank Space:**
   - In contrast, *rank space* indexes stocks by their descending market capitalization rank $k \in \{1, 2, \dots, N\}$.
   - While the underlying company occupying rank $k$ changes dynamically over time, the cross-sectional distribution of capitalizations across ranks exhibits long-term structural stationarity, grounded in the hybrid-Atlas models of stochastic portfolio theory (Fernholz 2002; Banner, Fernholz, and Karatzas 2005; Ichiba et al. 2011).
   - Principal Component Analysis (PCA) reveals that rank space possesses a substantially larger leading eigenvalue and wider spectral gap than name space: the first principal component explains the vast majority of market variance. This allows a single rank-market factor ($K=1$) to capture systemic market movement, compared to at least five factors ($K=5$) required in name space.

3. **Enhanced Residual Mean Reversion from Interacting Particle Dynamics:**
   - Residual returns in rank space (returns orthogonal to the leading rank factor) display pronounced, persistent mean-reverting dynamics.
   - Mathematically, when two stocks with proximate capitalizations fluctuate near each other, their local time of collision generates an interacting Brownian particle system. Once the temporary capitalization divergence resolves, the stocks swap ranks or revert to their stationary gap distribution.
   - Residual returns in rank space exploit this continuous collision-and-reversion process, providing dense, recurrent arbitrage opportunities that deep models can systematically harvest.

4. **Internal Intelligence of the CNN-Transformer Architecture:**
   - Operating directly on raw cumulative residual trajectories, the CNN-Transformer discovers three structural execution advantages over classical Ornstein-Uhlenbeck (OU) parametric models:
     - *Variable Leverage:* Assigns larger position sizing and leverage to positions exhibiting higher normalized residual deviations $(x_t - \mu)/\sigma$.
     - *Flexible Opportunity Thresholds:* Abandons rigid mean-reversion time cutoffs ($\tau < 30\text{ days}$ in OU models) and instead dynamically concentrates allocations in fast-reverting trajectories while selectively maintaining longer-horizon opportunities.
     - *Shorter Holding Durations:* Reduces the average holding period from ~10 trading days (parametric OU) to ~5 trading days (CNN-Transformer), drastically minimizing carry-over risk.

### Research interpretation

- The strategy represents a fundamental coordinate transformation of statistical arbitrage: shifting the asset basis from non-stationary entity identifiers to stationary rank-distribution coordinates.
- However, rank-space assets are *synthetic instruments*. An investor cannot directly purchase "the 10th largest stock in perpetuity" without executing rebalancing trades whenever the occupant of rank 10 changes.
- Thus, the economic viability of rank-space alpha hinges upon the trade-off between:
  1. Gross alpha generated by rank-residual mean reversion ($206.49\%$ annualized gross return, $9.04$ gross Sharpe ratio).
  2. The frictional cost of physical portfolio rebalancing from rank coordinates back into stock coordinates.
- This friction decomposes into two distinct physical costs:
  - *Latency Cost:* The opportunity loss and tracking error incurred when trading is delayed after a rank swap occurs.
  - *Bid-Ask Spread Cost:* The explicit execution penalty incurred during turnover when actively adjusting share counts.
- The existence of an optimal rebalancing interval ($\mathcal{T} \approx 225\text{ minutes}$) confirms the particle-collision thesis: rebalancing too fast incurs ruinous spread crossing during microscopic collision oscillations; rebalancing too slowly allows large latency drift to erode the mean-reversion alpha.

## Signal

### Signal Architecture and Mathematical Formulation

The strategy operates a two-stage signal pipeline: (1) Daily PCA market decomposition in rank space, and (2) CNN-Transformer residual return forecasting and portfolio optimization.

#### 1. Rank Space Return Definition

Let $c_{i,t}$ be the market capitalization of stock $i$ at trading day $t$. Let $\mathcal{R}_{i,t} \in \{1, \dots, N\}$ denote the capitalization rank of stock $i$ (where rank 1 is the largest stock), and $\mathcal{I}_{(k),t}$ denote the stock index occupying rank $k$ at day $t$.

The daily return on rank $k$ at day $t$ in the continuous-time limit is defined as:
$$\tilde{r}_{(k),t} := \frac{c_{(k),t} - c_{(k),t-1}}{c_{(k),t-1}} = \frac{c_{\mathcal{I}_{(k),t},t} - c_{\mathcal{I}_{(k),t-1},t-1}}{c_{\mathcal{I}_{(k),t-1},t-1}}$$

Let $\tilde{r}_t = \{\tilde{r}_{(k),t}\}_{k=1}^N \in \mathbb{R}^N$ denote the vector of rank returns, and $r_f \in \mathbb{R}$ the risk-free rate.

#### 2. Market Factor Decomposition (Algorithm 1)

1. **Lookback Window:** Factor extraction uses a rolling 252-day lookback window ($T_{\text{factor}} = 252$).
2. **Eigenvector Extraction:** Perform PCA on excess rank returns:
   $$\tilde{r}_t - r_f = U \Sigma V^T$$
   Retain the leading eigenvector $v_1$ (corresponding to $K=1$ factor for rank space):
   $$\tilde{F}_t = v_1$$
3. **Factor Portfolio Weights:** Solve for factor portfolio weights $\tilde{\omega}_t \in \mathbb{R}^{1 \times N}$:
   $$\tilde{F}_t = \tilde{\omega}_t (\tilde{r}_t - r_f)$$
4. **Factor Loadings:** Estimate factor loadings $\tilde{\beta}_t \in \mathbb{R}^{N \times 1}$ via rolling linear regression of $\tilde{r}_t - r_f \sim \tilde{F}_t$ over a 60-day lookback window ($T_{\text{loading}} = 60$).
5. **Linear Transformation Matrix:**
   $$\tilde{\Phi}_t := I - \tilde{\beta}_t \tilde{\omega}_t \in \mathbb{R}^{N \times N}$$
6. **Residual Returns:**
   $$\tilde{\epsilon}_t := \tilde{\Phi}_t (\tilde{r}_t - r_f) \in \mathbb{R}^N$$
   Each row of $\tilde{\Phi}_t$ represents a strictly market-neutral synthetic portfolio.

#### 3. Cumulative Residual Trajectory Input

Over a lookback window $L = 60$ trading days, compute the cumulative residual return trajectory $x_t^L \in \mathbb{R}^{N \times L}$:
$$x_t^L = (x_{t-L+1}, x_{t-L+2}, \dots, x_t)$$
where:
$$x_{t-L+\alpha} = \sum_{j=1}^\alpha \tilde{\epsilon}_{t-L+j}, \quad \alpha = 1, 2, \dots, L$$

#### 4. Deep Neural Network Architecture (Algorithm 3)

The network $\mathcal{N}: x_t^L \to w_t^{\epsilon|\text{NN}} \in \mathbb{R}^N$ maps cumulative residual trajectories directly to residual portfolio weights:

1. **1D Convolutional Blocks (Local Pattern Extraction):**
   - **Layer 1:**
     $$x_t^{(1)} = \frac{x_t^L - \mathbb{E}[x_t^L]}{\sqrt{\text{Var}(x_t^L) + \epsilon_{\text{norm}}}} \cdot \gamma^{(1)} + \beta^{(1)}$$
     $$y_t^{(1)} = W^{(1)} * x_t^{(1)} + b^{(1)}$$
     $$z_t^{(1)} = \text{ReLU}(y_t^{(1)}) + x_t^{(1)}$$
     *Parameters:* Input channels = 1, output channels $D_{\text{channel}} = 8$, kernel size $D_{\text{kernel}} = 2$.
   - **Layer 2:**
     $$x_t^{(2)} = \frac{z_t^{(1)} - \mathbb{E}[z_t^{(1)}]}{\sqrt{\text{Var}(z_t^{(1)}) + \epsilon_{\text{norm}}}} \cdot \gamma^{(2)} + \beta^{(2)}$$
     $$y_t^{(2)} = W^{(2)} * x_t^{(2)} + b^{(2)}$$
     $$z_t^{(2)} = \text{ReLU}(y_t^{(2)}) + x_t^{(2)}$$
     *Parameters:* Input channels = 8, output channels $D_{\text{channel}} = 8$, kernel size $D_{\text{kernel}} = 2$.

2. **Transformer Encoder Layer (Global Temporal Relationship):**
   - Transpose output to sequence format: $x_t^{\text{transformer}} = (z_t^{(2)})^T \in \mathbb{R}^{N \times L \times D_{\text{channel}}}$.
   - Multi-Head Self-Attention with $H = 4$ heads, key/query dimension $d_k = D_{\text{channel}} / H = 2$:
     $$\text{head}_i = \text{softmax}\left(\frac{Q_i K_i^T}{\sqrt{D_{\text{channel}} / H}}\right), \quad i = 1, \dots, H$$
     $$y_t = \text{Concat}(\text{head}_1 V_1, \dots, \text{head}_H V_H)$$
     $$z_t = \text{LayerNorm}(x_t^{\text{transformer}} + y_t)$$
     $$o_t = \text{LayerNorm}(W^O z_t + b^O + y_t)$$
     *Regularization:* Dropout with $p = 0.25$ applied to attention projection layers.

3. **Output Linear Head:**
   - Extract the final temporal slice $o_t[:, -1, :] \in \mathbb{R}^{N \times D_{\text{channel}}}$.
   - Map to scalar residual weights:
     $$w_t^{\epsilon|\text{NN}} = W^F (o_t[:, -1, :]) + b^F \in \mathbb{R}^N$$
     where $W^F \in \mathbb{R}^{1 \times D_{\text{channel}}}$ and $b^F \in \mathbb{R}$.

4. **Mean-Variance Objective Function:**
   - Train network parameters $\theta_{\mathcal{N}}$ over a trailing window $T_{\text{PnL}} = 24$ days to maximize the annualized mean-variance utility:
     $$\max_{\theta_{\mathcal{N}}} \mathbb{E}[(w_t^{R|\text{NN}})^T (r_{t+1} - r_f)] - \gamma \text{Var}[(w_t^{R|\text{NN}})^T (r_{t+1} - r_f)]$$
     where risk aversion $\gamma = 2.0$.
   - The unnormalized equity weights are obtained by projection:
     $$\tilde{w}_t^{R|\text{NN}} = \tilde{\Phi}_t^T w_t^{\epsilon|\text{NN}}$$
   - Sizing and leverage are standardized via $L_1$ normalization:
     $$w_t^{R|\text{NN}} = \frac{\tilde{w}_t^{R|\text{NN}}}{\|\tilde{w}_t^{R|\text{NN}}\|_1}$$

#### 5. Intraday Collision Rebalancing Rule (Algorithm 4)

To convert synthetic rank-space positions into executable stock positions:
- At market open ($t=0$), initialize stock weights:
  $$w_{\mathcal{I}_{(k),t},t}^{\text{name}} = w_{(k),t}^{R|\text{NN}}, \quad \forall k \in \{1, \dots, N\}$$
- Between rebalance points ($t + j\mathcal{T} < t + \tau \le t + (j+1)\mathcal{T}$):
  Holdings evolve passively with stock capitalizations:
  $$w_{i,t+\tau}^{\text{name}} = w_{i,t+(j\mathcal{T})^+}^{\text{name}} \times \frac{c_{i,t+\tau}}{c_{i,t+(j\mathcal{T})^+}}$$
- At rebalance intervals $\tau = (j+1)\mathcal{T}$ with $\mathcal{T} = 225\text{ minutes}$ (and at market close):
  Re-align stock positions to match the target rank weights:
  $$w_{i,t+((j+1)\mathcal{T})^+}^{\text{name}} = \sum_{k=1}^N w_{(k),t+(j+1)\mathcal{T}}^{\text{rank}} \mathbf{1}_{\{\mathcal{R}_{i,t+(j+1)\mathcal{T}} = k\}}$$
- Transaction cost deduction at each rebalance point:
  $$\text{cost}(t+\tau) = \left|\sum_{i=1}^N w_{i,t+\tau^+}^{\text{name}} - \sum_{k=1}^N w_{(k),t+\tau}^{\text{rank}}\right| + \eta \sum_{i=1}^N \left|w_{i,t+\tau^+}^{\text{name}} - w_{i,t+\tau}^{\text{name}}\right|$$
  where $\eta = 0.0002$ ($2\text{ bps}$).

## Required data

- **Universe:** Top 500 US equities by daily market capitalization ($N = 500$). Daily universe re-screened at market close based on available capitalization and valid forward-day trading status.
- **Venues & Historical Sources:**
  - Center for Research in Security Prices (CRSP): Daily prices, dividend-adjusted daily returns, shares outstanding, and market capitalizations (January 1990 to December 2022).
  - Polygon.io: 1-minute intraday bar prices across all constituent stocks (January 2005 to December 2022).
  - Kenneth R. French Data Library: 1-month US Treasury bill rate as risk-free rate $r_f$.
- **Data Fields Required:**
  - Intraday price: 1-minute resolution timestamped bars (`price_high_freq` $(N \times T_{\text{intraday}})$).
  - Intraday capitalization: Derived via $c_{i,t+\tau} = \text{Price}_{i,t+\tau} \times \text{SharesOutstanding}_{i,t}$.
  - Daily dividend-adjusted returns: CRSP `DlyRet`.
  - Intraday capitalization rank array: $\mathcal{R}_{i,t+\tau} \in \{1, \dots, N\}$.
- **Point-in-Time Integrity:**
  - Factor decomposition ($T_{\text{factor}} = 252$) and loadings ($T_{\text{loading}} = 60$) use only historical end-of-day data available prior to session $t$.
  - Model weights are precomputed overnight prior to market opening.
  - Shares outstanding updated as of previous filing date from CRSP.
- **Missing Data Handling:**
  - If a stock is halted or missing intraday quotes, its last observed price and capitalization carry forward within the day.
  - Universe requires valid trading return on day $t+1$ to participate in evaluation.

## Execution assumptions

- **Execution Timing:** Daily portfolio weights generated pre-open; intraday rebalancing executed at fixed $\mathcal{T} = 225\text{ minute}$ clock intervals and at 15:59 market close.
- **Order Mechanism:** Rebalancing executed as instantaneous market/cross orders against prevailing bid-ask quotes.
- **Friction and Cost Model:**
  - Baseline cost factor $\eta = 2\text{ bps}$ ($0.0002$), representing half-spread of 5–10 cents on large-cap US equities.
  - Latency cost modeled explicitly by tracking the divergence between drifting stock positions and true continuous rank positions prior to rebalancing.
  - Shorting borrow fee: Assumed $0.0000$ in baseline large-cap universe (all top 500 stocks assumed easy-to-borrow).
- **Leverage & Sizing:** Leverage fixed at $\Lambda = 1.0$ ($L_1$-norm of long positions plus short positions equals $1.0$).
- **Market & Dollar Neutrality:** By construction ($\tilde{w}_t^R = \tilde{\Phi}_t^T w_t^\epsilon$), the portfolio is analytically market-factor neutral. Dollar neutrality is maintained on average across the cross-section.

## Evidence

### Source-reported

All performance figures below are transcribed directly from Li & Papanicolaou (arXiv:2410.06568v2, June 2026), evaluated over the 16-year out-of-sample period (January 2007 to December 2022):

#### 1. Out-of-Sample Portfolio Performance Summary (2007–2022 Average)

| Configuration | Space | Model | Ann. Return | Ann. Volatility | Sharpe Ratio | Source Reference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gross ($\eta = 0\text{ bps}$)** | Name Space | Parametric OU | $2.36\%$ | $0.02$ ($2.0\%$) | $0.96$ | Table 1, Column 1 |
| **Gross ($\eta = 0\text{ bps}$)** | Rank Space | Parametric OU | $34.33\%$ | $0.06$ ($6.0\%$) | $6.14$ | Table 1, Column 2 |
| **Gross ($\eta = 0\text{ bps}$)** | Name Space | CNN-Transformer | $3.60\%$ | $0.08$ ($8.0\%$) | $0.45$ | Table 1, Column 3 |
| **Gross ($\eta = 0\text{ bps}$)** | Rank Space | CNN-Transformer | $\mathbf{206.49\%}$ | $0.23$ ($23.0\%$) | $\mathbf{9.04}$ | Table 1, Column 4 |
| **Net ($\eta = 2\text{ bps}$)** | Name Space | Parametric OU | $1.14\%$ | $0.02$ ($2.0\%$) | $0.41$ | Table 2, Column 1 |
| **Net ($\eta = 2\text{ bps}$)** | Rank Space | Parametric OU | $-29.37\%$ | $0.03$ ($3.0\%$) | $-9.95$ | Table 2, Column 2 |
| **Net ($\eta = 2\text{ bps}$)** | Name Space | CNN-Transformer | $-3.93\%$ | $0.08$ ($8.0\%$) | $-0.48$ | Table 2, Column 3 |
| **Net ($\eta = 2\text{ bps}$)** | Rank Space | CNN-Transformer | $\mathbf{35.68\%}$ | $0.11$ ($11.0\%$) | $\mathbf{3.28}$ | Table 2, Column 4 |

#### 2. Year-by-Year Net Performance (Rank Space CNN-Transformer with $\eta = 2\text{ bps}$, Table 2)

- **2007:** Return = $26.07\%$, Vol = $0.10$, Sharpe = $2.55$
- **2008 (GFC):** Return = $36.40\%$, Vol = $0.18$, Sharpe = $2.04$
- **2009:** Return = $48.97\%$, Vol = $0.13$, Sharpe = $3.67$
- **2010:** Return = $43.14\%$, Vol = $0.10$, Sharpe = $4.32$
- **2011:** Return = $14.32\%$, Vol = $0.10$, Sharpe = $1.45$
- **2012:** Return = $20.41\%$, Vol = $0.08$, Sharpe = $2.42$
- **2013:** Return = $52.51\%$, Vol = $0.10$, Sharpe = $5.37$
- **2014:** Return = $35.55\%$, Vol = $0.07$, Sharpe = $4.76$
- **2015:** Return = $22.82\%$, Vol = $0.10$, Sharpe = $2.32$
- **2016:** Return = $56.09\%$, Vol = $0.13$, Sharpe = $4.31$
- **2017:** Return = $49.00\%$, Vol = $0.09$, Sharpe = $5.16$
- **2018:** Return = $27.94\%$, Vol = $0.10$, Sharpe = $2.81$
- **2019:** Return = $34.13\%$, Vol = $0.10$, Sharpe = $3.38$
- **2020 (COVID):** Return = $56.62\%$, Vol = $0.14$, Sharpe = $4.14$
- **2021:** Return = $31.14\%$, Vol = $0.13$, Sharpe = $2.47$
- **2022 (Rate Hikes):** Return = $15.69\%$, Vol = $0.12$, Sharpe = $1.26$
- **16-Year Average:** Return = $\mathbf{35.68\%}$, Vol = $0.11$, Sharpe = $\mathbf{3.28}$

#### 3. Holding Period and Structural Efficiency

- Average holding period for CNN-Transformer in rank space is approximately $5\text{ days}$ (Figure 6f), compared to $\approx 10\text{ days}$ for the parametric OU model.
- Net Sharpe ratio exhibits strict positivity in every single out-of-sample calendar year from 2007 through 2022.

### Independently reproduced

- Not independently reproduced in this scout cycle.
- The authors' public Python replication package (`Infi-Yingfei-Li/stats-arb-rank-space`, commit `a526f711720959c930971aff71efbecd72ad4bbd`) contains complete training scripts, PCA decomposition routines, and backtest notebooks, but executing the full 16-year walk-forward backtest requires external CRSP and Polygon.io high-frequency datasets and approximately 130 GPU hours on dual Nvidia RTX 4090s.

### Negative evidence

1. **Extreme Transaction Cost Cliff:**
   - As documented in Appendix G.3 and Figure 13, the strategy's profitability collapses rapidly as execution costs increase:
     - At $\eta = 0\text{ bps}$: Sharpe = $9.04$
     - At $\eta = 2\text{ bps}$: Sharpe = $3.28$
     - At $\eta = 5\text{ bps}$: Sharpe $\le 0.0$ (strategy ceases to profit).
   - This demonstrates that the strategy cannot tolerate retail execution fees, wide bid-ask spreads, or market impact exceeding 2–3 bps per leg.
2. **Failure of Parametric Models in Net Terms:**
   - While the parametric OU model achieves a gross Sharpe of $6.14$ in rank space, its net Sharpe collapses to $-9.95$ after 2 bps transaction costs (Table 2). The parametric model turns over positions without accounting for rebalancing drag, destroying capital.
3. **Weight Volatility and Margin Requirements:**
   - In Appendix G.2 (Figure 12), the authors document that portfolio weights derived from the CNN-Transformer are significantly more volatile over time than those from parametric models due to dynamic variable leverage, creating substantial margin and operational rebalancing demands.

## Falsification plan

1. **Transaction Cost Degradation Audit:**
   - *Test:* Evaluate net performance across a fine grid of fee levels $\eta \in [1.0, 2.0, 3.0, 4.0, 5.0, 7.5]\text{ bps}$.
   - *Falsification Rule:* If net Sharpe ratio drops below $1.0$ at $\eta = 3.0\text{ bps}$, reject the thesis that the strategy is commercially executable without proprietary low-latency market-making infrastructure.
2. **Rebalancing Timescale Sensitivity Test:**
   - *Test:* Shift the rebalancing interval $\mathcal{T}$ away from the optimal 225-minute mark to $\mathcal{T} \in [15, 30, 60, 120, 225, 390]\text{ minutes}$.
   - *Falsification Rule:* If the PnL does not exhibit the inverted-U profile predicted by the collision/idle regime theory (where both high-frequency rebalancing $\mathcal{T} < 60\text{ min}$ and low-frequency rebalancing $\mathcal{T} > 390\text{ min}$ underperform), reject the proposed interacting Brownian particle mechanism as an overfitted narrative.
3. **Synthetic Rank Permutation Placebo Test:**
   - *Test:* Randomly permute the mapping between stock identifiers and assigned ranks each day, destroying the economic link between market capitalization and rank ordering while preserving cross-sectional return statistics.
   - *Falsification Rule:* If the CNN-Transformer achieves a Sharpe ratio $> 0.5$ on permuted ranks, the reported performance is an artifact of model data leakage or lookahead bias rather than genuine rank-space market structure.
4. **Out-of-Sample Expansion (2023–2026):**
   - *Test:* Evaluate the frozen model architecture over the post-publication period (January 2023 to August 2026).
   - *Falsification Rule:* Reject the strategy if realized net annualized return drops below $5\%$ or annualized Sharpe drops below $0.75$ over the forward 3-year period.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Porting Risks and Market-Structure Frictions:**
  1. *Traditional-Asset Provenance:* The mechanism was derived and tested exclusively on US equities (CRSP/Polygon.io top 500 stocks). The authors provide no cryptocurrency evaluation.
  2. *Extreme Fee Barrier:* On cryptocurrency centralized exchanges (e.g., Binance, Bybit, OKX), standard taker fees range from $2\text{ bps}$ to $5\text{ bps}$ per trade. Because the rank-space strategy ceases to profit at $\eta \ge 5\text{ bps}$, running this strategy via taker orders would be instantly unprofitable. Implementation in crypto is feasible only for VIP/MM tiers with zero or negative maker rebates.
  3. *Continuous 24/7 Rebalancing Drag:* US equities trade 6.5 hours per day, requiring only 1–2 intraday rebalances plus close rebalance. In 24/7 crypto markets, maintaining an equivalent 225-minute rebalance schedule requires $6.4$ rebalance cycles per day, compounding turnover and fee drag by more than $3\times$.
  4. *Rank Instability in Long-Tail Altcoins:* Crypto market capitalization rankings outside the top 10 are highly volatile, prone to speculative pumps, sudden illiquidity, and delistings. A top-50 crypto universe would experience massive rank churning, multiplying rebalance turnover far beyond equity levels.
  5. *Ambiguity of Crypto Market Capitalization:* Crypto circulating supply numbers are subject to unlocks, vesting, and reporting inaccuracies across data vendors (CoinGecko vs CoinMarketCap), introducing noise into the fundamental ranking coordinate.

## Limitations

1. **Frictional Vulnerability:** Extreme sensitivity to execution fees and slippage; performance turns negative at 5 bps costs.
2. **High Computational Burden:** Quarterly retraining requires approximately 130 GPU hours across dual RTX 4090s for a 16-year evaluation, limiting rapid parameter experimentation.
3. **Survivorship & Restructuring Risk:** While the top-500 daily filter mitigates selection bias, sudden corporate bankruptcies or delistings within intraday intervals require explicit fallback logic not fully detailed in the continuous-time framework.
4. **Lack of Independent Replication:** Performance claims rely on author-reported empirical backtests and have not been replicated in our internal PyBroker/Nautilus pipeline.

## Implementation status

- **Status:** `not-implemented`.
- No prototype, backtest script, or execution model currently exists in our internal NautilusTrader or PyBroker repositories.
- This research record represents an external research capture only.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- Recording this strategy does not constitute authorization for paper trading, testnet validation, or live capital allocation. Progression to implementation requires prior ChatGPT intake review, Wiki Brain promotion, and formal NautilusTrader historical verification.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/hybrid-resnet-rmt-covariance-denoising-crypto-mvp-2026-09-02]]`
- `[[quant/observable-matrix-dynamics-portfolio-optimization-2026-09-02]]`

## Sources

1. **Primary Working Paper:**
   - Authors: Ying-Fei Li and George C. Papanicolaou (Stanford University).
   - Title: *"Statistical Arbitrage in Rank Space"*.
   - Canonical arXiv Identifier: `arXiv:2410.06568v2 [q-fin.MF, stat.ML]`.
   - Date: Submitted October 9, 2024; revised June 29, 2026.
   - Canonical DOI: [10.48550/arXiv.2410.06568](https://doi.org/10.48550/arXiv.2410.06568).
   - URLs:
     - Abstract: [https://arxiv.org/abs/2410.06568](https://arxiv.org/abs/2410.06568)
     - Full Text HTML: [https://arxiv.org/html/2410.06568v2](https://arxiv.org/html/2410.06568v2)
     - Full Text PDF: [https://arxiv.org/pdf/2410.06568v2](https://arxiv.org/pdf/2410.06568v2)
2. **Replication Package & Codebase:**
   - Repository: [https://github.com/Infi-Yingfei-Li/stats-arb-rank-space](https://github.com/Infi-Yingfei-Li/stats-arb-rank-space)
   - Immutable Commit SHA: `a526f711720959c930971aff71efbecd72ad4bbd`
   - Key Modules:
     - `main_rank.py`
     - `main_name.py`
     - `main_rank_high_freq.py`
     - `trading_signal/trading_signal.py`
     - `portfolio_weights/portfolio_weights.py`
     - `market_decomposition/market_factor_classic.py`
     - `neural_network/neural_network.py`
     - `notebook/portfolio_performance_PnL/portfolio_performance_PnL.ipynb`
3. **Data Sources Cited by Primary Source:**
   - Center for Research in Security Prices (CRSP): US equity daily prices, returns, shares outstanding, and capitalizations (1990–2022).
   - Polygon.io: US equity 1-minute intraday tick/bar price data (2005–2022).
   - Kenneth R. French Data Library: 1-month US Treasury bill rate ($r_f$) and benchmark Fama-French factors.
