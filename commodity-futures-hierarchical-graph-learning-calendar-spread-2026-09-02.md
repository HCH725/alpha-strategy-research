---
schema: strategy-research-record-v1
title: Commodity Futures Hierarchical Graph Learning Calendar Spread Statistical Arbitrage
created: 2026-09-02T07:30:00Z
updated: 2026-09-02T07:30:00Z
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - calendar-spread
  - commodity-futures
  - graph-neural-networks
  - term-structure
status: research-only
confidence: medium
source_as_of: 2026-06-24T00:00:00Z
sources:
  - "Hong, Y., & Klabjan, D. (2026). Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets. arXiv:2606.25811 [q-fin.TR]. https://arxiv.org/abs/2606.25811"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Commodity Futures Hierarchical Graph Learning Calendar Spread Statistical Arbitrage

## Provenance

- Canonical source identity: arXiv:2606.25811 (`https://arxiv.org/abs/2606.25811`, `https://arxiv.org/html/2606.25811v1`).
- Authors: Yoonsik Hong and Diego Klabjan (Department of Industrial Engineering and Management Sciences, Northwestern University).
- Primary paper title: *Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets*.
- Repository / implementation snapshot: Academic preprint under perpetual non-exclusive distribution license. No official standalone public GitHub repository claimed in preprint; paper specifies mathematical operators, network layer equations, hyperparameter grids, and optimization details fully.
- Data as-of date: August 1977 through December 2025 (CME, CBOT, NYMEX, COMEX, eCBOT via LSEG Datastream / WRDS).

## Economic mechanism

### Source-reported
Commodity futures prices are driven by two main components: underlying spot asset dynamics ($S_{tc}$) and net cost-of-carry term-structure rates ($Q_{tcd}$). Directional single-contract or cross-sectional long-only strategies are predominantly exposed to volatile spot price shocks. In contrast, calendar spread (CS) strategies take long and short positions across different maturities of the same commodity ($\mathbf{1}^\top \mathbf{w}_{tc} = 0$), immunizing the portfolio against common spot price moves and isolating relative term-structure mispricing (convenience yields, storage costs, seasonal inventory constraints). Furthermore, cross-commodity economic linkages (substitution, production chains, macroeconomic demand) vary systematically across the maturity curve (e.g., short-term supply disruptions vs. long-term substitution), meaning graph convolutions must condition information propagation on time-to-maturity (TTM).

### Research interpretation
The strategy extracts statistical arbitrage alpha from term-structure carry and basis mispricing across multi-maturity commodity curves. By projecting cross-sectional return predictions onto the zero-sum subspace ($\mathbf{1}^\top \mathbf{w}_{tc} = 0$), the strategy hedges out systematic commodity-level directional factor exposure. The predictive edge relies on a bi-level hierarchical graph architecture that decouples TTM-aligned inter-commodity economic linkages (via virtual basis node lifting) from intra-commodity term-structure message passing (nearest-maturity relative deviations).

## Signal

The signal generation pipeline operates on a daily cadence with annual rolling retraining:

1. **Universe & Sampling Window**:
   - For trading day $t$, filter active commodity futures contracts listed on CME Group exchanges with time-to-maturity $T_{cd} - t \le \tau^{\max} = 1\text{ year}$ (52 weeks) and trading history spanning at least $n_{\text{sam}}^{\min} = 28$ consecutive trading days.
   - Commodity set $\hat{C}_{t+2}$, contract set $\hat{U}_{t+2}$.

2. **Feature Construction**:
   - For each contract $(c,d) \in \hat{U}_{t+2}$, compute normalized log-price features $\mathbf{x}_{tcd} = [x_{tcd\tau}]_{\tau=0}^{n_{\text{sam}}^{\min}-1} \in \mathbb{R}^{28}$.
   - Features undergo two-way ANOVA-style centering across time and contracts, commodity-wise scaling by standard deviation $\sigma_{tc}^x$, and standard normal transformation.

3. **Bi-Level Graph Formulation & Lifting**:
   - **Upper level**: Commodity nodes $c \in \hat{C}_{t+2}$ connected by positive/negative correlation edges $E_t^{\text{CC+}}, E_t^{\text{CC-}}$ where inter-commodity Pearson correlation $|\hat{\rho}_{tcc'}| \ge \rho^*$.
   - **Lower level**: Contract nodes $(c,d) \in \hat{U}_{t+2}$ connected by intra-commodity nearest-maturity edges $E_t^{\text{UU}}$.
   - **Cross-level**: Edges $E_t^{\text{CU}}, E_t^{\text{UC}}$ connecting underlying commodities to their contracts.
   - **Graph Lifting ($f^{\text{L}}$)**: Expands upper-level commodities into $n_{\text{bas}} + 1 = 53$ virtual basis nodes $\tau_j = j \cdot (\tau^{\max} / n_{\text{bas}})$ ($j \in [0:52]$), interpolating lower-level contract representations onto the synchronized virtual TTM grid.

4. **Bi-Level Convolution ($f^{\text{B}}$)**:
   - Stacks $l_{\text{con}}$ layers of four sequential operators:
     1. $g_{kl}^{\text{UC}}$: Elevates contract embeddings to TTM-aligned virtual nodes via linear interpolation across adjacent maturities.
     2. $g_{kl}^{\text{CC}}$: Propagates information across different commodities sharing the exact same virtual TTM index $j$ via GNN convolution (GAT, GCN, or GraphSAGE).
     3. $g_{kl}^{\text{CU}}$: Lowers aggregated virtual node embeddings back to physical contract nodes via inverse linear interpolation.
     4. $g_{kl}^{\text{UU}}$: Propagates intra-commodity term-structure messages between nearest maturities, computing relative deviations: $\mathbf{z}_{tlcdd'}^{\text{UU*}} = \text{Dropout}(\phi(W_{\text{U},kl}(\mathbf{z}_{tlcd}^{\text{CU}} - \mathbf{z}_{tlcd'}^{\text{CU}})/\sqrt{|T_{cd}-T_{cd'}|} + \mathbf{b}_{\text{U},kl}))$.

5. **Target & Prediction Head ($f^{\text{H}}$)**:
   - Target $Y_{t+2,cd} = \Phi^{-1}(\widehat{\text{cdf}}(R_{t+2,cd}^\circ))$, where $R_{t+2,cd}^\circ = R_{t+2,cd} - \text{avg}_{d'}(R_{t+2,cd'})$ is the commodity-wise demeaned forward return.
   - Final linear head outputs predicted normalized demeanor score $\hat{Y}_{t+2,cd} = W_{\text{H},k} \mathbf{z}_{tl_{\text{con}}cd} + \mathbf{b}_{\text{H},k}$.

6. **Calendar Spread Position Weight Projection**:
   - Compute commodity-wise mean score: $\hat{Y}_{tc}^\bullet = \frac{1}{\hat{n}_{tc}} \sum_{d \in \hat{D}_{tc}} \hat{Y}_{tcd}$.
   - Demean scores: $\hat{Y}_{tcd}' = \hat{Y}_{tcd} - \hat{Y}_{tc}^\bullet$.
   - Compute final portfolio weights via Euclidean projection and $\ell_1$-norm unit scaling:
     $$w_{t+2,cd} = \frac{\hat{Y}_{tcd}'}{\sum_{(c',d') \in \hat{U}_{t+2}} |\hat{Y}_{tc'd'}'|}$$
   - Guarantees exact dollar-neutrality per commodity ($\sum_{d \in \hat{D}_{tc}} w_{t+2,cd} = 0, \forall c$) and global leverage normalization ($\|\mathbf{w}_{t+2}\|_1 = 1$).

## Required data

- **Universe**: CME Group commodity futures (CME, CBOT, NYMEX, COMEX, eCBOT). Covers energy (Crude Oil, Natural Gas, Heating Oil, Gasoline), metals (Gold, Silver, Copper, Platinum), agriculture (Corn, Soybeans, Wheat, Soybean Oil, Soybean Meal), and livestock.
- **Data fields**: Daily settlement price ($F_{tcd}$), trading volume ($V_{tcd}$), contract maturity/expiration schedule ($T_{cd}$).
- **Timeframe**: Daily resolution.
- **Availability / Point-in-time**: Signals formed after market close at date $t$ using data up to $t$. Positions constructed at $t+1$ close and liquidated at $t+2$ close (or held over daily rebalancing cycle). No look-ahead data past $t$ in feature or correlation matrix construction.
- **Missing Data Handling**: Contracts require active trading volume on all $n_{\text{sam}}^{\min} = 28$ preceding trading days; illiquid or unobserved contracts are filtered out prior to graph construction.

## Execution assumptions

- **Execution Timing**: Positions established at $t+1$ close and liquidated/rebalanced at $t+2$ close using daily settlement prices.
- **Order Type**: MOC (Market-On-Close) / settlement price fills.
- **Transaction Costs & Slippage**: Source paper assumes zero transaction costs and unconstrained short selling in baseline theoretical/empirical sections; notes that turnover and CME calendar spread margin offsets significantly reduce practical implementation drag.
- **Margin / Financing**: 100% margin assumed for unit gross exposure baseline ($\|\mathbf{w}\|_1 = 1$); under CME margin rules, exchange-recognized calendar spread margin requirements are typically 70–90% lower than outright gross margin.

## Evidence

### Source-reported
- **Evaluation Period**: 10 annual out-of-sample test periods (2016 through 2025) under expanding-window retraining.
- **Risk-Adjusted Performance**:
  - Daily Information Ratio (IR): **0.0846** (annualized approx. $1.34$).
  - Daily Sortino Ratio (SR): **0.1241** (annualized approx. $1.97$).
  - Improvements of **96%** in IR and **82%** in SR relative to best non-graph/flat-GNN benchmarks.
  - Outperformed S&P 500 benchmark by **75%** in IR and **113%** in SR over the same 2016–2025 evaluation span.
- **Risk Metrics**:
  - Volatility and Maximum Drawdown (MDD) were over **6x lower** and **15x lower**, respectively, than Long-Only (LO) baseline configurations.
  - Near-zero empirical correlation with S&P 500 equity returns.
- **Theoretical Condition Verification**:
  - 81.109% of $(t,c)$ pairs in the 1977–2025 dataset satisfy Proposition 1 conditions for variance reduction over Long-Only positions.
  - 99.976% satisfy Proposition 3 conditions for strict delta risk reduction ($3\Delta^{\min} > \Delta^{\max}$).
- **Ablation Studies**:
  - Ablation A1 (intra-commodity term structure message passing only, removing inter-commodity GNN): degraded IR/SR.
  - Ablation A2 (inter-commodity propagation only, removing intra-commodity nearest-maturity diffs): severe degradation in prediction accuracy and Sharpe.

### Independently reproduced
- Not independently reproduced.

### Negative evidence
- Source model performance was evaluated without explicit bid-ask spread and transaction cost modeling. In illiquid back-month contracts with wide bid-ask spreads, calendar spread roll friction could erode a portion of the reported 0.0846 daily IR.
- Requires simultaneous execution of multiple futures legs; leg execution risk (slippage on the distant maturity leg) during fast market conditions is not accounted for in daily settlement backtests.

## Falsification plan

1. **Cost Stress & Bid-Ask Drag Test**: Apply tiered transaction cost models (1 to 5 bps per leg per turnover) to evaluate whether positive Information Ratio survives on CME calendar spreads.
2. **Spread Liquidity & Volume Filter Sensitivity**: Restrict trading universe to top 3 liquid maturities per commodity and evaluate whether term-structure alpha is driven by illiquid back-month pricing anomalies or structural convenience yield dynamics.
3. **Maturity Gap Perturbation**: Test calendar spread pairs with varying time gaps ($\Delta T = 1, 3, 6, 12$ months) against a baseline OLS curve-fitting model to determine if the bi-level GNN captures genuine multi-commodity spillover rather than simple curve slope mean-reversion.
4. **Execution Delay Test**: Introduce a 1-day execution lag ($t+2$ entry instead of $t+1$) to test signal decay horizon.

## Crypto portability

- **Portability status**: Adapted / unproven.
- **Portability rationale**: The source paper evaluates traditional commodity futures (CME Group). Crypto markets have distinct market structure:
  - The vast majority of crypto volume resides in perpetual swaps (no fixed expiration date, continuous funding rate) rather than dated futures curves.
  - Dated futures (e.g., quarterly and bi-quarterly contracts on Deribit, Binance COIN-M, OKX, and CME BTC/ETH futures) have limited tenor depth (typically 2 to 4 active expiries) compared to agricultural and energy futures (12+ active monthly expiries).
  - An adapted crypto application would construct calendar spreads between perpetuals and 3-month / 6-month dated delivery futures, or term-structure spreads on crypto interest-rate/lending protocols (e.g., Pendle principal/yield tokens, Term Finance fixed rates).
  - Basis risk, exchange counterparty risk, and fragmented liquidity across venues represent crypto-specific implementation barriers.

## Limitations

- **Friction Omission**: Baseline results do not deduct execution fees, exchange fees, or bid-ask crossing costs.
- **Data Dependency**: Requires synchronized multi-tenor price/volume feeds across multiple underlying commodity curves.
- **Model Complexity**: High computational overhead during annual retraining (8,790 hyperparameter training runs across GNN architectures).
- **Execution Synchronization**: Assumes synchronous closing price fills across multiple futures legs, which may encounter execution slippage in live trading.

## Implementation status

- Not implemented in local research stack (`not-implemented`).
- No NautilusTrader or PyBroker execution actors configured.

## Adoption boundary

- Research-only capture.
- Not approved for paper, testnet, or live trading execution.

## Related Wiki records

- `[[quant/commodity-perpetual-oracle-roll-funding-arbitrage-2026-09-01]]`
- `[[quant/crypto-futures-term-structure-roll-yield-carry-2026-08-31]]`
- `[[quant/options-statistical-arbitrage-graph-learning-synthetic-long-2026-09-02]]`
- `[[quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]]`

## Sources

- Hong, Y., & Klabjan, D. (2026). *Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets*. arXiv preprint arXiv:2606.25811 [q-fin.TR]. https://arxiv.org/abs/2606.25811
- CME Group. (n.d.). *Understanding futures spreads: futures spread overview*. CME Group Education. https://www.cmegroup.com/education/courses/understanding-futures-spreads/futures-spread-overview
