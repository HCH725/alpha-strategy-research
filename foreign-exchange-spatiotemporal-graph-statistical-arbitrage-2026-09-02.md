---
schema: strategy-research-record-v1
title: "Spatiotemporal Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage: Edge Regression, Dual Node Influence Networks, and Execution-Lag Optimization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - foreign-exchange
  - statistical-arbitrage
  - graph-neural-networks
  - spatiotemporal-graph
  - triangular-arbitrage
  - execution-lag
status: research-only
confidence: high
source_as_of: 2025-08-20
sources:
  - "Yoonsik Hong and Diego Klabjan, 'Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage', arXiv:2508.14784v1 [q-fin.ST, cs.LG], August 20, 2025. Presented at 6th ACM International Conference on AI in Finance (ICAIF '25). DOI: 10.48550/arXiv.2508.14784. https://arxiv.org/abs/2508.14784"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Spatiotemporal Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage: Edge Regression, Dual Node Influence Networks, and Execution-Lag Optimization

## Provenance

- **Primary Source:** Yoonsik Hong and Diego Klabjan (Department of Industrial Engineering and Management Sciences, Northwestern University), *"Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage"*, arXiv preprint `arXiv:2508.14784v1 [q-fin.ST, cs.LG]`, published August 20, 2025. Presented at the *6th ACM International Conference on AI in Finance (ICAIF '25)*. DOI: [10.48550/arXiv.2508.14784](https://doi.org/10.48550/arXiv.2508.14784). Full text: [https://arxiv.org/abs/2508.14784](https://arxiv.org/abs/2508.14784).
- **Primary Categories:** Statistical Finance (`q-fin.ST`), Machine Learning (`cs.LG`), Trading and Market Microstructure (`q-fin.TR`).
- **Context:** Classical foreign exchange rate prediction (FXRP) and foreign exchange statistical arbitrage (FXSA) models predominantly rely on decoupled pair-wise time-series or static triangular arbitrage identities. Hong and Klabjan propose a unified two-stage graph-learning framework: Stage 1 formulates multi-currency rate prediction as an edge-level regression problem on a discrete-time spatiotemporal graph (currencies as nodes, exchange rates as edges, sovereign bond yields as node features), and Stage 2 solves a stochastic optimization problem on a dual exchange-influence graph that explicitly models observation-to-execution latency and enforces empirical arbitrage constraints via projection and ReLU layers.

## Economic mechanism

### Source-reported

1. **Multi-Currency Graph Topology & Triangular Consistency:** In global FX markets, exchange rates do not evolve in isolation; currency valuations are interlinked by macroeconomic fundamentals, cross-currency balance-of-payments flows, and no-arbitrage cycle constraints (e.g., $S_{i,j} \cdot S_{j,k} \cdot S_{k,i} = 1$). Treating currency pairs independently ignores cross-sectional spillover dynamics and yield differentials.
2. **Interest-Rate Anchoring on Graph Nodes:** By assigning macroeconomic fundamentals (such as 1-year government bond yields reflecting uncovered interest rate parity pressures) directly to currency nodes and historical rate returns to directed edges, spatiotemporal message passing propagates monetary policy shocks across the global currency topology.
3. **Observation-Execution Lag Friction in Statistical Arbitrage:** Prior statistical arbitrage models assume instantaneous execution upon signal generation. In practice, quote dissemination, computation, and order transmission introduce a non-zero time lag $\tau_{\mathrm{exec}}$, during which prices drift. Formulating FXSA as a stochastic optimization problem with lag constraints prevents phantom arbitrage captures.
4. **Constrained Portfolio Policy via Dual Graph Projection:** In the arbitrage stage, exchange pairs become graph nodes whose edges capture cross-pair influence/correlation. The portfolio policy network optimizes risk-adjusted returns (Sortino and Information ratios) while satisfying budget conservation and no-arbitrage boundary conditions through differentiable projection operations.

### Research interpretation

The falsifiable thesis is that **incorporating sovereign yield node features into a spatiotemporal edge-regression graph extracts structural cross-currency lead-lag dynamics that outperform decoupled time-series models, and that conditioning statistical arbitrage allocations on execution-lag bounds eliminates latency-induced negative alpha**:
- Standard triangular arbitrage algorithms fail out-of-sample because execution latency converts theoretical cross-rate mispricings into adverse execution drag.
- Spatiotemporal graph neural networks regularize edge forecasts toward global multi-currency consistency, preventing overfitting to idiosyncratic single-pair noise.

## Signal

### 1. Spatiotemporal Currency Graph Formulation (Stage 1: FXRP)

At discrete observation time $t$:
- **Graph Structure:** Directed graph $\mathcal{G}_t = (\mathcal{V}, \mathcal{E})$, where vertices $v_i \in \mathcal{V}$ represent sovereign currencies ($N = |\mathcal{V}|$) and directed edges $e_{ij} \in \mathcal{E}$ represent traded currency pairs ($M = |\mathcal{E}|$).
- **Node Features:** $X_t^v \in \mathbb{R}^{N \times d_v}$, containing sovereign interest rates (e.g., 1-year government bond yields) and sovereign macroeconomic indicators.
- **Edge Features:** $X_t^e \in \mathbb{R}^{M \times d_e}$, containing historical normalized exchange rate returns, log-spreads, and realized volatility over lookback window $L$.
- **Edge Regression Objective:** Predict forward exchange rate return vector $\hat{Y}_{t+\Delta t}^e \in \mathbb{R}^M$ using a spatiotemporal Graph Convolutional Network coupled with Gated Recurrent Units (GCN-GRU):
  $$\hat{Y}_{t+\Delta t}^e = f_{\Theta}(\mathcal{G}_t, X_{t-L:t}^v, X_{t-L:t}^e)$$
  trained via Mean Squared Error (MSE) loss regularized by triangular cycle consistency penalties.

### 2. Dual Influence Graph & Statistical Arbitrage Optimization (Stage 2: FXSA)

- **Dual Graph Construction:** Construct dual line-graph $\mathcal{G}_t^{\mathrm{dual}} = (\mathcal{V}_{\mathrm{dual}}, \mathcal{E}_{\mathrm{dual}})$, where nodes $u \in \mathcal{V}_{\mathrm{dual}}$ represent currency pairs (exchanges) and edges $(u, w) \in \mathcal{E}_{\mathrm{dual}}$ represent statistical co-movement / influence weights.
- **Node Features for Dual Graph:** Combine stage-1 predicted returns $\hat{Y}_{t+\Delta t}^e$, historical variance $\hat{\sigma}_u^2$, and recent return momentum.
- **Execution Lag Modeling:** Assume a non-negligible delay $\delta_{\mathrm{lag}}$ between observation $t$ and fill $t + \delta_{\mathrm{lag}}$. The realized return is evaluated over $[t + \delta_{\mathrm{lag}}, t + \delta_{\mathrm{lag}} + H]$, where $H$ is the holding period.
- **Constrained Policy Network:** The network outputs portfolio allocation weights $w_t \in \mathbb{R}^M$ parameterized by:
  $$w_t = \Pi_{\mathcal{W}}\left( \mathrm{ReLU}(g_{\Phi}(\mathcal{G}_t^{\mathrm{dual}}, \hat{Y}_{t+\Delta t}^e)) \right)$$
  where $\Pi_{\mathcal{W}}$ is a projection operator onto the feasible asset allocation simplex satisfying leverage and budget bounds $\sum_{i=1}^M |w_{t,i}| \le W_{\max}$.
- **Objective Function:** Maximize the empirical Information Ratio (IR) or Sortino Ratio over the training trajectory:
  $$\mathcal{L}_{\mathrm{FXSA}}(\Phi) = -\frac{\mathbb{E}[R_{p} - R_b]}{\sqrt{\mathbb{E}[\min(0, R_p - R_b)^2] + \epsilon}}$$

## Required data

- **Universe:** Major sovereign currency pairs across G10 and high-liquidity FX markets (specifically evaluated with USD, EUR, and JPY as home currencies).
- **Timeframe:** Daily and intraday sampled observation bars (weekday sessions, excluding weekend settlement gaps).
- **Price Series:** Bid, ask, and mid exchange rates $S_{i,j}(t)$ for all cross pairs.
- **Interest Rate / Macro Data:** 1-year sovereign government bond yields for all constituent currency nodes, published on a point-in-time basis without look-ahead revisions.
- **Calendar & Clock:** Strict UTC alignment; weekend non-trading intervals masked to prevent artificial autoregressive distortion.

## Execution assumptions

- **Execution Lag:** Explicit observation-execution delay $\delta_{\mathrm{lag}} \ge 1\text{ bar}$ enforced during training and validation.
- **Transaction Costs:** Full bid-ask spread crossing and institutional broker commissions applied on every portfolio turnover.
- **Position Sizing:** Continuous capital allocation weights bounded by maximum gross leverage constraint $W_{\max}$.
- **Order Type:** Taker market orders executed at $t + \delta_{\mathrm{lag}}$ against prevailing top-of-book bid/ask quotes.

## Evidence

### Source-reported

- **Sample Period:** Historical market data starting from the first trading days of 2015 through recent periods, restricted to active weekday trading sessions.
- **Currencies Evaluated:** Top traded global currencies evaluated with USD, EUR, and JPY designated as primary home currencies.
- **Stage 1 (FXRP) Accuracy:** The spatiotemporal graph learning model achieved statistically significant reductions in Mean Squared Error (MSE) compared to baseline non-graph time-series models (ARIMA, Vector Autoregression, standalone LSTM).
- **Stage 2 (FXSA) Arbitrage Performance:**
  - **Information Ratio:** The proposed FXSA method achieved a **61.89% higher Information Ratio** relative to the benchmark statistical arbitrage strategy.
  - **Sortino Ratio:** The proposed FXSA method achieved a **45.51% higher Sortino Ratio** relative to the benchmark strategy.
  - **Mathematical Guarantee:** The authors provide formal proof that the projection-ReLU constrained policy network strictly satisfies empirical arbitrage bounds under observation-execution lag.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Performance is sensitive to interest-rate data timeliness; stale bond yield prints during unscheduled central bank policy interventions can cause temporary misallocation.

## Falsification plan

1. **Ablation of Node Features (Interest Rates):** Train the spatiotemporal GCN-GRU without sovereign bond yield node features ($X^v = \mathbf{0}$). If the Sortino ratio improvement drops by less than 10%, the hypothesized macroeconomic transmission mechanism is falsified, indicating the graph is merely memorizing cross-rate correlation.
2. **Triangular Shuffled-Label Placebo Test:** Randomize the adjacency matrix of the currency graph while preserving individual time-series marginal distributions. If the randomized graph achieves performance within 1.0 standard error of the true topology, graph structure provides no genuine predictive alpha.
3. **Execution Latency Stress Test:** Increase the execution delay parameter $\delta_{\mathrm{lag}}$ from 1 to 5 bars. If net Sharpe ratio decays faster than a standard linear time-series arbitrage baseline, the model overfits to unexecutable microstructure lags.
4. **Transaction Cost Breakeven:** Apply synthetic spread widening (e.g., doubling base FX spreads). If net portfolio returns turn negative at transaction costs below typical institutional tiers (1.5 bps), the strategy lacks economic robustness.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Crypto Adaptation Mechanism:**
  - In crypto markets, an analogous asset graph can be constructed where nodes represent Layer-1/Layer-2 native tokens and major stablecoins (BTC, ETH, SOL, BNB, USDT, USDC), directed edges represent spot and perpetual cross pairs (e.g., ETH/BTC, SOL/ETH, BTC/USDT), and node features represent on-chain staking yields, funding rates, or Aave/Compound deposit rates.
  - Triangular arbitrage in crypto DEX pools (e.g., Uniswap v3 multi-hop routing) and cross-CEX triangular pairs exhibit substantial execution lag due to block confirmation times and network latency.
- **Portability Risks:**
  - Crypto markets operate 24/7/365 without weekend closures, eliminating weekday masking needs but introducing continuous funding settlement regimes every 8 hours.
  - Perpetual funding rates and liquidation cascades introduce high non-linear jump dynamics absent in sovereign G10 FX markets.

## Limitations

- **Model Complexity & Inference Latency:** Spatiotemporal GNN forward passes require multi-hop message passing; at high frequencies ($< 1\text{s}$), inference latency may consume the execution-lag budget.
- **Sovereign Yield Data Granularity:** Bond yield data is typically available at daily/hourly frequencies, whereas FX prices tick continuously, necessitating asynchronous feature aggregation.
- **Regime Shifts in Correlation:** Central bank monetary policy divergence vs. coordinated quantitative easing alters cross-currency co-movement graphs over multi-year horizons.

## Implementation status

- Not implemented in our research stack.
- No PyBroker, NautilusTrader, paper, testnet, or live trading validation has been performed.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record represents theoretical and empirical research capture for quantitative intake review. It does not constitute authorization for deployment or capital allocation.

## Related Wiki records

- `[[quant/spatiotemporal-graph-neural-networks-cross-asset-arbitrage]]`
- `[[quant/triangular-arbitrage-execution-lag-latency-bounds]]`
- `[[quant/uncovered-interest-rate-parity-crypto-funding-carry]]`

## Sources

- Yoonsik Hong and Diego Klabjan, "Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage", arXiv preprint `arXiv:2508.14784v1 [q-fin.ST, cs.LG]`, August 20, 2025. Presented at 6th ACM International Conference on AI in Finance (ICAIF '25). DOI: [10.48550/arXiv.2508.14784](https://doi.org/10.48550/arXiv.2508.14784). Full text: [https://arxiv.org/abs/2508.14784](https://arxiv.org/abs/2508.14784).
