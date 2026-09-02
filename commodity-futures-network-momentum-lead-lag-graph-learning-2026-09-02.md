---
schema: strategy-research-record-v1
title: "Commodity Futures Network Momentum: Signature Lévy Area and Dynamic Time Warping Graph Learning"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - trend-following
  - network-momentum
  - lead-lag
  - commodity-futures
  - dynamic-time-warping
  - path-signatures
  - levy-area
  - graph-learning
status: research-only
confidence: high
source_as_of: 2025-01-13
sources:
  - "Linze Li (Imperial College London), William Ferreira (University College London), 'Follow the Leader: Enhancing Systematic Trend-Following Using Network Momentum', arXiv:2501.07135v1 [q-fin.PM, q-fin.TR], January 2025. URL: https://arxiv.org/abs/2501.07135"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Commodity Futures Network Momentum: Signature Lévy Area and Dynamic Time Warping Graph Learning

## Provenance

- **Primary Source:** Linze Li (Department of Mathematics, Imperial College London) and William Ferreira (Department of Computer Science, University College London), "Follow the Leader: Enhancing Systematic Trend-Following Using Network Momentum", arXiv:2501.07135v1 [q-fin.PM, q-fin.TR], January 2025.
- **Traceable Canonical URL:** [https://arxiv.org/abs/2501.07135](https://arxiv.org/abs/2501.07135)
- **Source Data Sample:** 28 liquid commodity futures markets spanning agriculture, energy, industrial/precious metals, and equity index futures; training period June 2002 to June 2024, evaluated out-of-sample from January 2005 to June 2024 (evaluated over 100 stationary block bootstrap sample paths and historical real market trajectories).

## Economic mechanism

### Source-reported
Trend-following strategies exploit directional persistence driven by slow macroeconomic adjustment, cognitive conservatism, and asynchronous information reception across market participants. While momentum is traditionally measured for single assets (univariate time-series momentum), cross-sectional lead-lag relationships ("momentum spillover") naturally arise between interconnected markets due to asymmetric speed of information processing. 

In commodity markets, firm-like structural links (such as balance sheet co-ownership or analyst coverage) are absent, but strong cross-market economic transmission channels exist (e.g., crude oil leading refining margins, agriculture energy inputs, industrial metals leading equity indices). Leaders in these clusters transmit trend momentum to lagging follower markets. By extracting pairwise lead-lag directional matrices through 2nd-level path signatures (Lévy area) and non-linear sequence alignment (Dynamic Time Warping variants), and then filtering these matrices into a sparse graph topology via convex optimization, one can construct an aggregated "network momentum" indicator that enhances trend persistence signals and mitigates downside drawdown risk.

### Research interpretation
The strategy represents a hybrid cross-sectional network momentum filter layered onto multi-speed trend-following oscillators:
1. **Multi-Method Asymmetric Lead-Lag Extraction:** Pairwise directional leads are quantified using:
   - **Signature-based Lévy Area:** Captures 2nd-level iterated integral path area $A^{\text{Lévy}}_{i,j} = \frac{1}{2}(S(X)^{1,2} - S(X)^{2,1})$, proving theoretically that the sign of the Lévy area matches the sign of the fixed lag $\ell = \pm 1$.
   - **Dynamic Time Warping (DTW / DDTW / shapeDTW / shapeDDTW):** Identifies non-synchronous, variable-length alignment by extracting the warping path mode lag $\text{Mode}(\Delta \mathcal{W})$, with derivative (DDTW) and local shape (shapeDTW) features preventing alignment singularities.
2. **Convex Graph Learning with Logarithmic Barrier:** Solves a regularized graph estimation problem that guarantees no isolated markets (log barrier on node degrees $\mathbf{1}^T \log(A\mathbf{1})$) and penalizes dense spurious edges via Frobenius regularization.
3. **Multi-Lookback Ensemble Adjacency:** Averaging adjacency matrices across lookback windows $\delta \in \{22, 44, 66, 88, 110, 132\}$ days stabilizes edge weights, reducing high-frequency turnover and transaction cost drag.
4. **Non-Linear Reverting Sigmoid Sizing:** Instead of binary sign betting ($+1/-1$), the aggregated network momentum is passed through a reverting sigmoid response function $r(x) = c_\lambda x \exp(-x^2 / 2\lambda^2)$ with $\lambda = \sqrt{2}$, preserving return distribution positive skewness and tapering leverage at extreme trend extensions.

## Signal

The signal computation pipeline executes daily:

### 1. Continuous Price Construction & Volatility Scaling
- Construct continuous contract prices $P_{t,m}$ using the backward Panama Canal method with fixed roll rules.
- Compute daily price deltas $\Delta_{t,m} = P_{t,m} - P_{t-1,m}$.
- Scale deltas by the 22-day exponential weighted moving standard deviation: $\tilde{\Delta}_{t,m} = \frac{\Delta_{t,m}}{\sigma_{t,m}^{22}}$.
- Reconstruct volatility-scaled cumulative price series $\tilde{P}_{t,m} = \tilde{P}_{t-1,m} + \tilde{\Delta}_{t,m}$.

### 2. Time Series Momentum Oscillators ($R_{t,m}^k$)
For each market $m$ and speed index $k \in \{1, 2, 3, 4, 5, 6\}$:
- Fast smoothing parameter: $\alpha_k = (k \sqrt{2})^{-1}$
- Slow smoothing parameter: $\beta_k = (\rho k \sqrt{2})^{-1}$ with ratio $\rho = 4$
- Oscillator feature:
  $$R_{t,m}^k = \frac{\mu(\tilde{P}_m, \alpha_k) - \mu(\tilde{P}_m, \beta_k)}{\sigma(\tilde{P}_m, \alpha_k)}$$
  where $\mu(\tilde{P}, \alpha)$ is the EWMA of volatility-scaled prices.

### 3. Lead-Lag Matrix Estimation ($\mathbf{V}_t \in \mathbb{R}^{M \times M}$)
Construct skew-symmetric lead-lag matrix $\mathbf{V}_t$ using volatility-scaled deltas $\tilde{\mathbf{\Delta}}_t$ over rolling lookback $\delta$:
- **Lévy Area:** $V_{ij} = \sum_{a=s+1}^t (\tilde{X}_a^i - \tilde{X}_{a-1}^i)(\tilde{X}_{a-1}^j + \tilde{X}_a^j) - (\tilde{X}_a^j - \tilde{X}_{a-1}^j)(\tilde{X}_{a-1}^i + \tilde{X}_a^i)$
- **Dynamic Time Warping:** $V_{ij} = \text{Mode}(\{j_l - i_l\}_{l=1}^L)$ along the optimal warping path $\mathcal{W}^*$.

### 4. Graph Learning Optimization
Solve the convex optimization problem for adjacency matrix $\mathbf{A}_t$:
$$\min_{\mathbf{A} \ge 0, \, \text{diag}(\mathbf{A})=0} \frac{1}{2} \|\mathbf{A} \circ \mathbf{W}\|_F^2 - \alpha \mathbf{1}^T \log(\mathbf{A}\mathbf{1}) + \frac{\beta}{2} \|\mathbf{A}\|_F^2$$
where $W_{ij} = \|\vec{v}_i - \vec{v}_j\|^2$ is the Euclidean distance between lead-lag vector profiles, $\alpha > 0$ controls connectedness, and $\beta \ge 0$ controls sparsity.
- Normalize row weights: $\tilde{A}_{m,n} = \frac{A_{m,n}}{\sum_j A_{m,j}}$.
- For ensemble variants ($\bar{\mathbf{A}}_t$), average normalized adjacencies across lookbacks $\delta \in \{22, 44, 66, 88, 110, 132\}$ days.

### 5. Network Momentum Feature & Sizing
- **Network Aggregated Oscillator:**
  $$\tilde{R}_{t,m}^k = \sum_{n \in \mathcal{N}_t(m)} \tilde{A}_{m,n} R_{t,n}^k$$
- **Reverting Sigmoid Response Function:**
  $$r(x) = c_\lambda \, x \exp\left(-\frac{x^2}{2\lambda^2}\right), \quad \lambda = \sqrt{2}$$
- **Target Position Sizing (in lots):**
  $$\tilde{X}_{t,m} = \left(\frac{1}{M} \sum_{k=1}^K \frac{1}{K} r(\tilde{R}_{t,m}^k)\right) \cdot \frac{1}{F_{t,m} E_{t,m} \sigma_{t,m}^{22}} \cdot \left(\Gamma \frac{\sigma_{\text{tgt}}}{\sqrt{252}}\right)$$
  where $F_{t,m}$ is contract point value, $E_{t,m}$ is FX exchange rate to USD, $\Gamma$ is notional AUM, and $\sigma_{\text{tgt}} = 10\%$ annualized portfolio volatility target.

## Required data

- **Universe:** 28 liquid futures markets (WTI Crude, Brent, Natural Gas, Heating Oil, RBOB Gasoline, Gold, Silver, Copper, Platinum, Palladium, Corn, Wheat, Soybeans, Soybean Oil, Soybean Meal, Coffee, Sugar, Cocoa, Cotton, Live Cattle, Feeder Cattle, Lean Hogs, S&P 500, E-mini Nasdaq, Euro Stoxx 50, FTSE 100, Nikkei 225, DAX).
- **Price Data:** Daily settlement prices, continuous contract backadjustment roll dates.
- **Microstructure / FX:** Contract point values, daily spot FX rates to USD.
- **Lookback Windows:** $\delta \in \{22, 44, 66, 88, 110, 132\}$ trading days for lead-lag matrix estimation; 22 days for volatility scaling.

## Execution assumptions

- **Execution Timing:** Next-day execution; PnL at day $t$ generated by position $\tilde{X}_{t-2,m}$ plus transaction costs incurred from adjusting position to $\tilde{X}_{t-1,m}$.
- **Transaction Costs:** Modeled explicitly using fixed exchange + broker fee and variable bid-ask spread models per commodity contract.
- **Portfolio Volatility Target:** Scaled to $\sigma_{\text{tgt}} = 10\%$ annualized target volatility.
- **Rebalancing:** Daily position updates.

## Evidence

### Source-reported
Source: Linze Li and William Ferreira (2025), arXiv:2501.07135v1 (Tables 1, 2, 3, 4 and Figures 1, 2):
1. **Bootstrapped Out-of-Sample Performance (100 Stationary Block Bootstraps, 2005–2024):**
   - **Baseline Univariate MACD:** Gross Return: 0.057, Transaction Cost: 0.027, Net Return: 0.030, **Net Sharpe Ratio: 0.277**, Net Sortino: 0.515, Calmar: 0.155, Skewness: 0.697, Max Drawdown: -0.198, Hit Rate: 0.518.
   - **NMM-DDTW-E (Ensemble Derivative DTW):** Gross Return: **0.064**, Transaction Cost: **0.022** (-19% vs MACD), Net Return: **0.042**, **Net Sharpe Ratio: 0.357** (**+29% vs MACD**), **Net Sortino: 0.684** (**+33% vs MACD**), Calmar: 0.231, Skewness: 0.767, Max Drawdown: -0.183, Hit Rate: 0.523.
   - **NMM-SDDTW-E (Shape Derivative DTW Ensemble):** Highest Avg Profit / Avg Loss ratio, Skewness: **0.778**.
   - **NMM-LEVY (Signature Lévy Area):** Lowest Max Drawdown: **-0.177**, Highest Hit Rate: **0.528**, Transaction Cost: 0.024 (-11% vs MACD).
2. **Statistical Significance Tests:**
   - **Wilcoxon Signed-Rank Test (Paired Net Sharpe > MACD):** $p < 0.05$ across all NMM models (NMM-DTW, NMM-DDTW, NMM-SDTW, NMM-SDDTW, NMM-LEVY, and all ensemble variants).
   - **Kolmogorov-Smirnov Test (Stochastic Dominance):** $p < 0.05$ across all NMM models except non-ensemble NMM-SDDTW.
3. **Long vs Short Directional Asymmetry:**
   - **Short Positions:** MACD baseline exhibits negative net Sharpe (**-0.396**) on bootstrapped data. NMM-DDTW-E increases short net Sharpe to **-0.301** (+24% improvement, 35% loss reduction) with high positive return skewness (1.155 vs 0.804 for MACD).
   - **Long Positions:** NMM-LEVY achieves net Sharpe **0.587** (+6.1% vs MACD 0.559) and reduces Max Drawdown to 0.168.
4. **Historical Real Market Trajectory (2005–2024):**
   - **NMM-DTW-E Net Sharpe:** **0.364** vs **0.233** for baseline MACD (**+56% relative increase**).
   - **NMM-DDTW Skewness:** **0.759** vs **0.645** for baseline MACD.
5. **Correlation with Baseline:**
   - Correlation between NMM strategy returns and univariate MACD ranges from $0.71$ to $0.89$ (lowest correlation: NMM-SDDTW at $0.71$), confirming complementary, non-redundant momentum information.

### Independently reproduced
- Not independently reproduced.

### Negative evidence
- **Short-Side Structural Drag:** In historical commodity data, standalone short momentum positions generated negative net Sharpe ratios across all models due to long-term secular commodity super-cycles and upward drift.
- **Turnover without Ensemble Averaging:** Single-lookback NMM models without ensemble regularization exhibit higher turnover and fee drag.
- **High Market Correlation:** The correlation between NMM and univariate trend following is positive ($0.71 - 0.89$), meaning NMM acts as an overlay/enhancement rather than an orthogonal market-neutral alpha.

## Falsification plan

1. **Synthetic Lead-Lag Permutation Test:** Randomly shuffle cross-sectional time alignment across commodities while keeping individual autocorrelation intact. Falsification threshold: If NMM net Sharpe fails to exceed the shuffled baseline by at least $+0.05$ ($p < 0.01$), reject the hypothesis that cross-sectional lead-lag spillover drives the edge.
2. **Execution Lag & Slippage Sensitivity:** Delay execution by $1$ additional trading bar (rebalance at $t+2$). Falsification threshold: If $> 50\%$ of the Sharpe enhancement over MACD dissipates, reject deployability under execution latency.
3. **Dynamic Time Warping Descriptor Ablation:** Test whether simple Euclidean distance matches shapeDTW/shapeDDTW performance across volatile commodity shock regimes (e.g., 2008 oil spike, 2020 negative oil, 2022 Ukraine commodity spike). Falsification threshold: If DDTW fails to outperform standard DTW in turbulent sub-periods, reject the necessity of derivative warping.
4. **Out-of-Sample Portfolio Expansion:** Evaluate on 20 liquid crypto perpetual contracts and 30 international sovereign bond futures. Falsification threshold: Out-of-sample Net Sharpe enhancement $< 0$.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Crypto-Specific Market Dynamics & Adaptation Requirements:**
  - **Asset Universe:** Replace commodity contracts with liquid cryptocurrency perpetual futures (e.g., BTC, ETH, SOL, BNB, AVAX, NEAR, SUI, LINK, DOGE).
  - **Perpetual Funding Rate Drag:** In crypto perpetuals, 8-hour funding rates replace futures roll yields. Funding carry must be incorporated into net position returns.
  - **24/7 Continuous Trading:** Unlike commodity futures with distinct daily settlement boundaries, crypto trades continuously; lead-lag windows must be defined over synchronized UTC daily snapshots or rolling hourly timestamps.
  - **Lead-Lag Hierarchy:** BTC and ETH act as pronounced directional leaders relative to mid/small-cap altcoins, creating a natural structural fit for signature Lévy area and DTW alignment.

## Limitations

- **Convex Solver Computation:** Daily convex optimization of the graph learning adjacency matrix with MOSEK/CVXPY introduces computational latency when scaled to hundreds of assets.
- **Panama Canal Roll Dependency:** Price history quality depends heavily on continuous contract roll assumptions and volume roll points.
- **Sensitivity to Volatility Normalization:** Volatility-scaled deltas rely on rolling 22-day EWMA standard deviations which may react sluggishly to sudden jump discontinuities.

## Implementation status

- `not-implemented`: This is a research capture only. No backtest, PyBroker model, or NautilusTrader execution strategy has been implemented or authorized.

## Adoption boundary

- `research-only`: Research capture does not constitute approval for live, testnet, or paper trading.
- `not-approved`: Strategy has not passed quantitative intake review.

## Related Wiki records

- `[[quant/commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02]]`
- `[[quant/futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]]`
- `[[quant/futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]]`
- `[[quant/path-portfolio-optimization-signature-defect-lift-2026-09-02]]`

## Sources

1. Linze Li and William Ferreira, "Follow the Leader: Enhancing Systematic Trend-Following Using Network Momentum", arXiv:2501.07135v1 [q-fin.PM, q-fin.TR], January 2025. URL: [https://arxiv.org/abs/2501.07135](https://arxiv.org/abs/2501.07135).
2. Guy Flint and Stefan Zohren, "Network momentum across asset classes", *Applied Network Science*, 8(1):32, 2023. DOI: [10.1007/s41109-023-00557-0](https://doi.org/10.1007/s41109-023-00557-0).
3. Terry Lyons, "Rough paths, signatures and the modelling of functions on streams", *Proceedings of the International Congress of Mathematicians*, 2014. URL: [https://arxiv.org/abs/1405.4537](https://arxiv.org/abs/1405.4537).
