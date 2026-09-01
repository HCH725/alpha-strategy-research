---
schema: strategy-research-record-v1
title: "Statistical Arbitrage in Options Markets by Graph Learning and Synthetic Long Positions: RNConv Tree-Structured Message Passing and Black-Scholes Risk Factor Neutrality"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - statistical-arbitrage
  - graph-neural-networks
  - synthetic-long
  - risk-factor-neutrality
status: research-only
confidence: high
source_as_of: 2025-08-20
sources:
  - "Yoonsik Hong and Diego Klabjan, 'Statistical Arbitrage in Options Markets by Graph Learning and Synthetic Long Positions', arXiv:2508.14762v1 [q-fin.ST, cs.LG], August 20, 2025. https://arxiv.org/abs/2508.14762"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Statistical Arbitrage in Options Markets by Graph Learning and Synthetic Long Positions: RNConv Tree-Structured Message Passing and Black-Scholes Risk Factor Neutrality

## Provenance

- **Primary Source:** Yoonsik Hong and Diego Klabjan (Department of Industrial Engineering and Management Sciences, Northwestern University), *"Statistical Arbitrage in Options Markets by Graph Learning and Synthetic Long Positions"*, arXiv preprint `arXiv:2508.14762v1 [q-fin.ST, cs.LG]`, submitted August 20, 2025. Full text: [https://arxiv.org/abs/2508.14762](https://arxiv.org/abs/2508.14762).
- **Subject Classifications:** Statistical Finance (`q-fin.ST`), Machine Learning (`cs.LG`), Computational Finance (`q-fin.CP`).
- **Research Scope:** The authors investigate the direct identification and exploitation of statistical arbitrage (StatArb) in derivatives markets using deep learning and graph neural networks. They observe that options surface data possesses high tabular structure where traditional GNNs struggle, and that naive statistical mispricing predictors do not guarantee risk-factor neutrality. They address this through a two-stage framework: (1) Stage 1 introduces a prediction target isolating pure mispricing relative to synthetic bonds and predicts it via RNConv (a graph learning architecture embedding tree structures), and (2) Stage 2 introduces SLSA (Synthetic Long Synthetic Arbitrage / Synthetic Long positions for Statistical Arbitrage), a class of portfolio positions provably neutral to all first- and second-order Black-Scholes Greeks under no-arbitrage conditions with minimal variance risk.

## Economic mechanism

### Source-reported

1. **Option Surface Graph Coupling:** Options written on a common underlying asset are linked across strikes $K$ and expiration horizons $T$ by no-arbitrage constraints (put-call parity, convexity, monotonic time value, absence of butterfly/calendar arbitrage). Standard time-series models treat option contracts independently, neglecting the interconnected topology of the volatility surface.
2. **Tabular GNN Deficiencies & Tree-Structured Convolutions:** Financial option feature sets (strike, moneyness, implied volatility, Greeks, bid-ask spreads) are tabular in nature, where gradient-boosted decision trees typically outperform standard multi-layer perceptrons. By embedding decision-tree splits directly into graph convolution operations (RNConv), message passing propagates structural mispricing without loss of tabular partitioning fidelity.
3. **Synthetic Bond Construct as Pure Arbitrage Anchor:** Discrepancies between theoretical synthetic bond valuations (formed by portfolios of calls, puts, and underlying cash positions) and prevailing market prices represent localized capital dislocations. Isolating synthetic bond mispricings allows the prediction target to focus strictly on structural arbitrage rather than directional market drift.
4. **Black-Scholes Greek Neutrality via SLSA:** Standard StatArb strategies in derivatives carry significant residual exposure to underlying directional drift ($\Delta$), volatility shocks ($\mathcal{V}$), gamma risk ($\Gamma$), time decay ($\Theta$), and interest rate shifts ($\rho$). The SLSA construct guarantees that the synthesized long/short option position cancels out all analytical Black-Scholes Greeks, generating a return profile driven purely by mispricing convergence.

### Research interpretation

The falsifiable hypothesis is that **structuring the options chain as a bipartite strike-maturity graph processed through tree-embedded convolutions (RNConv) isolates non-linear volatility surface distortions, and projecting predicted anomalies onto an SLSA Greek-neutral manifold extracts positive risk-adjusted returns without incurring market-directional or volatility-jump drawdown risk**:
- Tree-structured graph convolution captures sharp local boundary breaks across the implied volatility surface that smooth polynomial approximations fail to detect.
- Explicit Black-Scholes Greek projection removes the need for high-frequency dynamic delta-hedging, significantly reducing transaction costs that typically erode option statistical arbitrage alpha.

## Signal

### 1. Options Chain Graph Formulation (Stage 1)

At discrete observation timestamp $t$:
- **Graph Nodes $\mathcal{V}_t$:** Each traded option contract $(K_i, T_j, \text{type} \in \{\text{Call}, \text{Put}\})$ is represented as a node $v \in \mathcal{V}_t$.
- **Graph Edges $\mathcal{E}_t$:** Directed and undirected edges connect contracts sharing identical strike $K$, identical maturity $T$, or adjacent moneyness buckets.
- **Node Features $X_t \in \mathbb{R}^{|\mathcal{V}_t| \times d}$:** Tabular feature vectors comprising moneyness $S_t/K$, annualized time to maturity $\tau = T - t$, implied volatility $\sigma_{\mathrm{IV}}$, bid-ask spread, historical open interest, trading volume, and analytical Greeks ($\Delta, \Gamma, \mathcal{V}, \Theta, \rho$).
- **Prediction Target $Y_{t+\Delta t}$:** Relative mispricing deviation of the option contract relative to the theoretical synthetic bond benchmark evaluated at target forward horizon $\Delta t$.
- **RNConv Neural Architecture:** Message aggregation incorporates differentiable tree partition kernels that recursively segment neighbor feature spaces before passing node representations into GNN aggregation layers:
  $$h_v^{(l+1)} = \sigma\left( W_0 h_v^{(l)} + \sum_{u \in \mathcal{N}(v)} \alpha_{uv} \mathcal{T}_{\Phi}\left( h_u^{(l)}, e_{uv} \right) \right)$$
  where $\mathcal{T}_{\Phi}$ parameterizes tree-structured routing functions.

### 2. SLSA Projection and Portfolio Construction (Stage 2)

- **Greek Sensitivity Matrix $G_t \in \mathbb{R}^{5 \times N_t}$:** Matrix containing the 5 analytical Black-Scholes Greeks $(\Delta_i, \Gamma_i, \mathcal{V}_i, \Theta_i, \rho_i)_{i=1}^{N_t}$ for all $N_t$ active contracts.
- **Raw Signal Allocation:** Model outputs raw anomaly scores $\hat{y}_t \in \mathbb{R}^{N_t}$ indicating relative under-/over-valuation.
- **SLSA Projection Operator $\Pi_{\mathrm{SLSA}}$:** Portfolio weights $w_t \in \mathbb{R}^{N_t}$ are obtained by solving the constrained quadratic projection:
  $$\min_{w_t} \| w_t - \hat{y}_t \|_2^2 \quad \text{subject to} \quad G_t w_t = \mathbf{0}, \quad \sum_{i=1}^{N_t} |w_{t,i}| \le W_{\max}, \quad w_t^{\top} \mathbf{1} = 0$$
- **Minimal Risk Guarantee:** The resulting position $w_t$ constitutes a zero-cost synthetic long portfolio that is provably orthogonal to first-order and second-order market state perturbations under the no-arbitrage null hypothesis.

## Required data

- **Universe:** Listed equity or index options chains (empirically evaluated on KOSPI 200 Index options).
- **Timeframe:** Intraday option tick/quote intervals aggregated to discrete observation intervals (e.g., 5-minute or daily closing snapshots).
- **Fields:** Bid price, ask price, trade price, trading volume, open interest for every call and put strike; underlying spot index / futures level; risk-free rate curve (CD 91-day rate or government short-rate).
- **Point-in-Time:** Strictly synchronized underlying price snapshots and option quotes; stale quotes (zero volume / no bid-ask updates within lookback window) filtered out prior to graph construction.
- **Missing Data:** Unlisted strikes or illiquid far out-of-the-money options ($|\Delta| < 0.05$) excluded from graph topology.

## Execution assumptions

- **Execution Model:** Simultaneous execution of multi-leg option orders at prevailing top-of-book quotes.
- **Transaction Costs:** Full half-spread crossing costs and exchange transaction fees accounted for per executed contract.
- **Position Limits:** Aggregate gross leverage bounded by $W_{\max}$; maximum allocation per individual option strike capped to avoid illiquid market impact.
- **Rebalance Cadence:** Evaluated at fixed daily or multi-bar rebalancing intervals with target holding horizon $\Delta t$.

## Evidence

### Source-reported

- **Dataset / Universe:** Historical KOSPI 200 Index options dataset spanning multi-year trading regimes.
- **Stage 1 (Prediction) Performance:** RNConv achieved statistically significant improvements in Mean Squared Error (MSE) and directional classification accuracy over conventional GNN baselines (GCN, GAT, GraphSAGE) and standard tabular ML baselines.
- **Stage 2 (SLSA Strategy) Performance:**
  - The SLSA strategy consistently generated positive returns across out-of-sample test periods.
  - Achieved an **average P&L-contract Information Ratio of 0.1627**.
  - Confirmed empirical neutrality to underlying market trends and market-wide implied volatility swings.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Strategy performance degrades significantly if bid-ask spreads widen substantially during severe market stress, as multi-leg crossing costs can exceed the small synthetic bond pricing dislocation.

## Falsification plan

1. **Synthetic Greeks Perturbation Test:** Measure empirical exposure of the SLSA portfolio to large underlying spot jumps ($\pm 5\%$) and implied volatility shifts ($\pm 20\%$). If empirical delta or vega beta exceeds 0.05, the Black-Scholes neutrality guarantee is falsified by model mis-specification or smile curvature.
2. **Ablation of RNConv Tree Module:** Replace RNConv with a standard linear Graph Convolutional Network (GCN). If out-of-sample Information Ratio does not decline by at least 25%, the hypothesis that tree-structured convolutions are essential for tabular options features is rejected.
3. **Transaction Cost Stress Threshold:** Incrementally increase assumed option bid-ask spread slippage from 1 tick to 5 ticks. If the net Information Ratio drops below zero at less than 2 ticks of slippage, the strategy is deemed unexecutable in non-institutional environments.
4. **Cross-Exchange Universe Transfer:** Apply the identical architecture to US Index Options (SPX / NDX) or liquid single-stock options. If Information Ratio fails to exceed 0.05 out-of-sample, the effect is idiosyncratic to the KOSPI 200 market structure.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Crypto Adaptation Mechanism:**
  - Crypto options markets (primarily Deribit, Paradigm, and emerging DeFi on-chain options protocols like Aevo, Lyra, Derive) offer full strike and expiration term structures for BTC and ETH.
  - The bipartite options graph can be mapped directly to BTC/ETH option chains, using Deribit order book feeds and synthetic inverse/linear contract conversions.
- **Crypto Portability Risks:**
  - Crypto options suffer from wide bid-ask spreads on out-of-the-money strikes, high fee structures (e.g., Deribit 0.03% of underlying cap), and fragmented liquidity across expirations.
  - Unlike equity index options with continuous cash settlement, crypto options are often margin-settled in coin (inverse contracts) or stablecoins, introducing margin-currency volatility and liquidation risk into the Greek-neutral portfolio.

## Limitations

- **Complex Multi-Leg Execution:** Simultaneous execution of 4+ option legs across different strikes carries execution lag and leg-risk where one side fills and the other misses.
- **Tabular GNN Overhead:** Real-time inference of tree-embedded GNNs on dense options matrices introduces computational latency.
- **Model Risk:** Black-Scholes Greek neutrality assumes continuous local diffusion; discrete jumps and stochastic volatility dynamics can cause residual Greek leakage.

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
- `[[quant/black-scholes-greeks-neutrality-arbitrage-mechanisms]]`
- `[[quant/crypto-options-volatility-surface-modeling]]`

## Sources

- Yoonsik Hong and Diego Klabjan, "Statistical Arbitrage in Options Markets by Graph Learning and Synthetic Long Positions", arXiv preprint `arXiv:2508.14762v1 [q-fin.ST, cs.LG]`, August 20, 2025. Full text: [https://arxiv.org/abs/2508.14762](https://arxiv.org/abs/2508.14762).
