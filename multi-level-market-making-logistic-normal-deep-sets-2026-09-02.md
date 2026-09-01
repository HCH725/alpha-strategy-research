---
schema: strategy-research-record-v1
title: Multi-Level Limit Order Book Market Making via Deep Sets and Logistic-Normal Actor-Critic Policy
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-18
sources:
  - "https://arxiv.org/abs/2608.18195"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Multi-Level Limit Order Book Market Making via Deep Sets and Logistic-Normal Actor-Critic Policy

## Provenance

This research capture is based on the working paper:
- **Title:** Multi-Level Market Making with Reinforcement Learning
- **Authors:** Patrick Cheridito and Moritz Weiss (ETH Zürich)
- **Publication Identifier:** arXiv:2608.18195v1 [q-fin.TR, cs.LG]
- **Submission Date:** 18 August 2026
- **Canonical DOI:** [10.48550/arXiv.2608.18195](https://doi.org/10.48550/arXiv.2608.18195)
- **Traceable Source URL:** `https://arxiv.org/abs/2608.18195` / `https://arxiv.org/html/2608.18195v1`

The paper addresses the practical limitation of classical market-making models (e.g., Avellaneda–Stoikov, Guéant) and earlier reinforcement learning formulations, which typically restrict quoting actions to single limit buy and sell orders at fixed or unit quantities. It formulates a continuous simplex action space parameterized by a multivariate logistic-normal distribution, aggregates variable-length resting limit orders via a permutation-invariant deep-set encoder, and employs potential-based reward shaping to train an actor-critic market maker across multi-depth order books.

## Economic mechanism

### Source-reported

Market makers earn revenue by continuously posting bids and asks in a limit order book (LOB), capturing the bid-ask spread while managing inventory exposure to avoid adverse price movements. Real-world limit order books feature multiple price levels and queue priority dynamics.

When the market is populated solely by noise traders, order arrivals are symmetric and non-directional; simple heuristic quoting at the inside spread (TOP1) or skewing inventory (INV) suffices to capture spread. However, when the market includes:
1. **Tactical traders:** participants who react to instantaneous volume imbalance ($I_t$), generating sharp, temporary price jumps.
2. **Strategic traders:** participants who execute in the direction of an exponentially smoothed volume imbalance signal ($\bar{I}_t$), inducing persistent price trends.

Under tactical and strategic order flow, passive limit orders posted at the top of the book suffer severe adverse selection—getting executed immediately prior to an unfavorable directional price run. The authors demonstrate that an optimal policy must:
- Dynamically distribute liquidity across multiple price depths ($K$ levels) rather than concentrating solely on the top level;
- Shift quote mass deeper into the book as adverse selection pressure and inventory imbalance increase;
- Selectively cancel lower-priority resting orders to protect against informed order flow while preserving queue priority for orders likely to be filled favorably.

### Research interpretation

The proposed policy acts as an adaptive liquidity provision mechanism that conditions simultaneous multi-level quote allocations on both exogenous order-flow state signals (OFI, price drift, book volume profile) and endogenous private inventory/queue states. 

By modeling quote allocations as continuous fractions on the simplex $\mathbb{S}^{2(K+1)}$ via a logistic-normal distribution, the policy avoids boundary pathologies associated with Dirichlet distributions while preserving differentiable closed-form densities for policy gradients. The deep-set encoder resolves the variable-dimension representation problem of resting limit orders, ensuring that the feature encoding remains permutation-invariant to order internal indexing while retaining exact price level, queue priority, and lot size.

## Signal

The decision and control cycle operates at discrete intervals $t_n = n\Delta t$ for $n=0, 1, \dots, N-1$ across a finite horizon $[0, T]$ with $\Delta t = 30\,\text{s}$, $T = 600\,\text{s}$, and $N = 20$.

### State Space Representation

At each step $t_n$, the agent observes an augmented state $s_n$ composed of public market states and private agent states:

1. **Market States (Public):**
   - Normalized best bid and ask percentage returns: $100 \times (p_n^b - p_0^b)/p_0^b$ and $100 \times (p_n^a - p_0^a)/p_0^a$.
   - Normalized resting depth volumes across the first $K=3$ levels: $v_n^{b,k}/100$ and $v_n^{a,k}/100$ for $k \in \{1, 2, 3\}$.
   - Normalized mid-price percentage return over the last interval: $100 \times (p_n - p_{n-1})/p_{n-1}$.
   - Normalized market order flow: $\Delta_n^M / (\text{Total Market Buy} + \text{Sell Volume})$.
   - Normalized limit order flow: $\Delta_n^L / (\text{Total Limit Buy} + \text{Sell Volume})$.
   - Normalized cancellation order flow: $\Delta_n^C / (\text{Total Cancellation Buy} + \text{Sell Volume})$.

2. **Private States (Agent):**
   - Normalized time: $t_n / T \in [0, 1]$.
   - Normalized inventory: $Q_n / M \in \mathbb{R}$.
   - Remaining order counts: $m_n^b$ and $m_n^a$.
   - Order features: For each resting limit order $i$, normalized triples $(l_n^{b,i}, q_n^{b,i}/100, w_n^{b,i}/M)$ indicating tick distance $l$, queue position $q$, and lot size $w$.
   - Fractional allocation vector: $\kappa_n \in [0, 1]^{2(K+1)}$ representing current lot allocation across levels.

### Deep-Set Encoder Architecture

Because the number of active resting orders $m_n^b, m_n^a$ varies dynamically, order features are processed via a deep-set network $f_\phi^o$ (single hidden layer with 2 nodes and ReLU activation). For each price level $k \in \{1, \dots, K\}$:
$$f_{n,\phi}^{e,b,k} = \frac{1}{|I_n^{b,k}|} \sum_{i \in I_n^{b,k}} f_\phi^o(l_n^{b,i}, q_n^{b,i}/100, w_n^{b,i}/M)$$
where $I_n^{b,k}$ is the set of active buy orders at level $k$ (set to 0 if empty). The resulting fixed-dimensional vector $f_\phi^e(s_n)$ concatenates the pooled order embeddings with market and private scalar features.

### Action Space & Policy Parameterization

The action $a_n \in \mathbb{S}^{2(K+1)}$ (8-dimensional simplex for $K=3$) specifies:
- $a^0$: fraction of capacity $M$ unallocated (inactivity).
- $a^1$: fraction allocated to market buy orders.
- $a^2, a^3, a^4$: fraction allocated to limit buy orders at best bid ($k=1$), 1 tick below ($k=2$), and 2 ticks below ($k=3$).
- $a^5$: fraction allocated to market sell orders.
- $a^6, a^7, a^8$: fraction allocated to limit sell orders at best ask ($k=1$), 1 tick above ($k=2$), and 2 ticks above ($k=3$).

The action is generated by mapping an underlying normal latent variable $X \sim \mathcal{N}(\mu_{\theta^m}, \Sigma_{\theta^v})$ through the logistic transformation $h: \mathbb{R}^{2(K+1)} \to \mathbb{S}^{2(K+1)}$:
$$a^0 = \frac{1}{1 + \sum_{j=1}^{2(K+1)} e^{X^j}}, \quad a^k = \frac{e^{X^k}}{1 + \sum_{j=1}^{2(K+1)} e^{X^j}}$$
where:
- $\mu_{\theta^m} = f_{\theta^m}^m(f_\phi^e(s_n))$ is output by a policy feedforward network (2 hidden layers of 128 tanh nodes).
- $\Sigma_{\theta^v} = \operatorname{diag}(e^{\theta^{v,1}}, \dots, e^{\theta^{v,2(K+1)}})$ is a state-independent learnable diagonal covariance matrix.
- Output lot sizes $a^k M$ are mapped to exact integer lot counts using the Hamilton apportionment (largest remainder) method.
- Reallocations cancel resting orders with lower queue priority first to maintain high-priority queue spots.

### Objective & Reward Shaping

The agent optimizes expected discounted reward under potential-based reward shaping:
$$r(s_n, a_n) = \bar{r}(s_n, a_n) + (Q_{n+1}p_{n+1} - Q_n p_n) - \gamma |Q_{n+1}|$$
where $\bar{r}(s_n, a_n)$ represents cash flows from filled orders, $Q_{n+1}p_{n+1} - Q_n p_n$ evaluates mark-to-mid wealth delta (dense credit assignment), and $\gamma = 0.01$ is the running inventory penalty parameter.

At terminal time $t_N = T$, a terminal market order $\text{MO}_\nu(s_N)$ forces inventory liquidation to $|Q_{N+}| \le \lceil \nu M \rceil$ (baseline $\nu = 0$, liquidating all inventory).

## Required data

- **LOB Granularity:** Level-2 / Level-3 limit order book data capturing depth up to $D=30$ price levels, with order-level queue position tracking ($q$) and order sizes ($w$).
- **Timeframe / Cadence:** High-frequency event stream aggregated to decision steps of $\Delta t = 30\,\text{s}$ over trading horizons $T = 600\,\text{s}$ ($N = 20$ decision epochs).
- **Public Variables:** Best bid $p_t^b$, best ask $p_t^a$, mid-price $p_t = (p_t^b + p_t^a)/2$, depth volumes $v_t^{b,k}, v_t^{a,k}$ ($k=1,2,3$), market order flow $\Delta_t^M$, limit order flow $\Delta_t^L$, cancellation order flow $\Delta_t^C$.
- **Private Variables:** Executed inventory $Q_t$, active limit order levels $l$, queue positions $q$, remaining sizes $w$, and current capacity utilization $M$.

## Execution assumptions

- **Decision Frequency:** Actions evaluated every $\Delta t = 30\,\text{s}$.
- **Order Queue Matching:** FIFO queue priority on each price level. A limit buy (sell) order is executed when aggregate market sell (buy) order volume consumes all orders ahead in the queue at that price level. Partial fills reduce resting lot size without losing queue position.
- **Capacity Constraint:** Total active lots allocated to market and limit orders cannot exceed $M$ (evaluated at $M=2$ lots and $M=20$ lots).
- **Cancellation Latency:** Resting limit orders that are not reallocated in the new action are cancelled at decision time $t_n$ prior to submitting new limit orders.
- **Terminal Liquidation:** At terminal time $t_N = 600\,\text{s}$, any remaining inventory $Q_N$ is liquidated via a market order walking the book ($\nu = 0$), incurring full spread crossing and adverse depth impact.

## Evidence

### Source-reported

The authors evaluate the model across 10,000 out-of-sample test episodes in three simulated limit order book environments populated by Poisson-arrival trader classes:

1. **Adverse Selection & Markouts (Table 1):**
   - Expected 30-second markouts for baseline static quoting (TOP1) deteriorate substantially when strategic traders are introduced:
     - In noise-trader market: TOP1 markout is $+0.485$ ticks ($M=2$) and $+0.505$ ticks ($M=20$).
     - In noise + tactical market: TOP1 markout drops to $+0.334$ ticks ($M=2$) and $+0.286$ ticks ($M=20$).
     - In noise + tactical + strategic market: TOP1 markout drops further to $+0.124$ ticks ($M=2$) and $+0.089$ ticks ($M=20$).
   - Posting at the second-best price (TOP2) provides markout protection (+0.852 to +1.341 ticks), but results in significantly fewer fills.

2. **Comparative Cash Flow Performance (Table 2, 10,000 test episodes):**
   - **Noise-trader environment:**
     - $M=2$: LN achieves mean normalized cash flow $+27.02$ ($\text{SD}=2.81$), outperforming TOP1 ($+24.16, \text{SD}=4.20$), TOP2 ($+14.39, \text{SD}=4.22$), and INV ($+24.58, \text{SD}=3.49$).
     - $M=20$: LN achieves $+217.43$ ($\text{SD}=34.25$), outperforming TOP1 ($+199.98, \text{SD}=42.50$), TOP2 ($+123.64, \text{SD}=42.84$), and INV ($+200.77, \text{SD}=35.39$).
   - **Noise + Tactical environment:**
     - $M=2$: LN achieves $+21.37$ ($\text{SD}=3.38$), outperforming TOP1 ($+19.16, \text{SD}=5.14$), TOP2 ($+15.77, \text{SD}=4.93$), and INV ($+19.04, \text{SD}=4.32$).
     - $M=20$: LN achieves $+173.80$ ($\text{SD}=38.25$), outperforming TOP1 ($+146.40, \text{SD}=50.19$), TOP2 ($+132.84, \text{SD}=49.09$), and INV ($+132.32, \text{SD}=43.99$).
   - **Noise + Tactical + Strategic environment (severe adverse selection):**
     - $M=2$: LN achieves $+14.99$ ($\text{SD}=4.07$), outperforming TOP1 ($+11.89, \text{SD}=6.21$), TOP2 ($+13.14, \text{SD}=5.86$), and INV ($+10.98, \text{SD}=5.31$).
     - $M=20$: LN achieves $+123.34$ ($\text{SD}=44.02$), significantly outperforming TOP1 ($+83.69, \text{SD}=61.71$), TOP2 ($+106.87, \text{SD}=58.85$), and INV ($+74.19, \text{SD}=53.48$).

3. **Behavioral Profile (Table 3 & Figure 5):**
   - In the strategic trader environment ($M=20$), the LN agent adapts by shifting filled order volume across deeper levels: 69.34% at Level 1, 22.36% at Level 2, and 8.30% at Level 3 (compared to only 2.10% at Level 3 in the tactical-only market).
   - Limit fill rate decreases from 74.65% (noise, $M=2$) to 43.99% (strategic, $M=20$), while cancellation rate rises to 56.01%, confirming active repositioning away from toxic order flow.
   - Voluntary market order usage remains negligible (1.90% to 2.74% total volume, driven predominantly by terminal mandatory liquidation).
   - Logistic-normal policy convergence is strictly superior to Dirichlet (DR) parameterization, which exhibits policy gradient instability and lower terminal rewards (Table 7, Figure 9).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The empirical results are derived exclusively within a stylized, synthetic Poisson-driven order-book simulation rather than calibrated historical L2/L3 market tick feeds.
- The inventory penalty parameter $\gamma = 0.01$ shows degraded effectiveness in reducing variance in state-dependent markets compared to purely random noise markets (standard deviation drops by 65.7% under noise for $M=2$, but only by modest amounts under strategic flow), indicating that static inventory penalties fail under persistent trends.
- The policy assumes zero latency and no queue cancellation penalties or exchange throttling.

## Falsification plan

1. **Historical Replay L3 Backtest:** Train and test the LN actor-critic framework on tick-level L3 order book replays (e.g., Binance BTC/USDT and ETH/USDT perpetuals) incorporating exact WebSocket API round-trip latencies ($20\text{--}50\,\text{ms}$) and message throttling rules.
2. **Architecture Ablation Test:** Replace the permutation-invariant deep-set encoder with a naive zero-padded fixed-coordinate multilayer perceptron. If the naive network achieves comparable out-of-sample reward and policy stability across varying queue lengths, the necessity of deep sets is falsified.
3. **Simplex Distribution Ablation:** Compare the logistic-normal actor against Gaussian-with-softmax and Dirichlet policies. If the logistic-normal parameterization fails to show statistically superior PnL or training stability on real market feeds, its specific mathematical advantage is disconfirmed.
4. **Fee Tier Stress Test:** Introduce realistic exchange fee schedules (e.g., maker rebate of $0.00\%$ to $+0.01\%$ vs. taker fee of $0.04\%\text{--}0.05\%$). If the terminal mandatory market order liquidation wipeout exceeds total accumulated spread capture, the unconstrained terminal liquidation mechanism is disproven.

## Crypto portability

- **Portability Status:** `adapted`, `unproven`.
- **Porting Rationale:** High-frequency centralized and decentralized crypto CLOBs (Binance, OKX, Bybit, Hyperliquid, dYdX v4) exhibit persistent directional order flow driven by cross-venue arbitrageurs and toxic liquidation cascades, closely matching the tactical and strategic trader dynamics modeled in the paper.
- **Portability Frictions:**
  - *Fee Structures:* Crypto exchanges charge significant taker fees ($2\text{--}5\,\text{bps}$) relative to maker rebates ($0\text{--}1\,\text{bp}$); the agent's terminal market order liquidation would incur severe drag unless replaced with soft-horizon passive inventory unwinding.
  - *Rate Limits & Cancellation Penalties:* Heavy cancellation activity (up to 56% in strategic regimes) may trigger exchange order-to-trade ratio (OTR) penalties or API rate limit bans.
  - *Funding & Basis Drift:* Holding inventory across 8-hour funding intervals introduces funding cash flows not modeled in the spot simulation.

## Limitations

- **Underspecified Execution Latency:** The model assumes instantaneous order placement and cancellation upon the 30-second decision boundary without network propagation delays.
- **Synthetic Simulator Bias:** Trader arrival processes follow compound Poisson intensities parameterized by static volume damping factors ($c=0.65, \beta=0.1$); real crypto microstructure exhibits power-law clustering, Hawkes self-excitation, and cross-venue latency arbitrage.
- **Fixed Capacity Horizon:** The model enforces a hard terminal horizon $T=600\,\text{s}$ with forced market order liquidation, which is artificial for continuous 24/7 crypto perpetual market making.

## Implementation status

`not-implemented` in our research repository or execution pipelines.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Scope:** Purely theoretical and simulated research capture. Does not authorize deployment to PyBroker, NautilusTrader, Paper, Testnet, or Live execution environments.

## Related Wiki records

- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]`
- `[[quant/funding-aware-market-making-perpetual-dex-2026-08-31]]`
- `[[quant/crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]]`
- `[[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`

## Sources

- Cheridito, P., & Weiss, M. (2026). *Multi-Level Market Making with Reinforcement Learning*. arXiv preprint [arXiv:2608.18195v1](https://arxiv.org/abs/2608.18195) [q-fin.TR]. Submitted August 18, 2026. DOI: [10.48550/arXiv.2608.18195](https://doi.org/10.48550/arXiv.2608.18195).
- Cont, R., Stoikov, S., & Talreja, R. (2010). *A stochastic model for order book dynamics*. Operations Research, 58(3), 549–563.
- Ng, A. Y., Harada, D., & Russell, S. J. (1999). *Policy invariance under reward transformations: Theory and application to reward shaping*. ICML 1999, 278–287.
- Zaheer, M., Kottur, S., Ravanbakhsh, S., Poczos, B., Salakhutdinov, R. R., & Smola, A. J. (2017). *Deep Sets*. Advances in Neural Information Processing Systems (NeurIPS 30).
