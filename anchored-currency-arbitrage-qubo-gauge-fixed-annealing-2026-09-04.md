---
schema: strategy-research-record-v1
title: "Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage: Exact Anchor-Gauge Reweighting, Provably Sufficient Penalties, and Annealing Baselines (Reinhardt & Hauser 2026)"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - currency-arbitrage
  - qubo
  - quantum-annealing
  - market-microstructure
  - foreign-exchange
status: research-only
confidence: medium
source_as_of: 2026-08-16
sources:
  - "Eric A. F. Reinhardt and Adam J. Hauser, 'Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage', arXiv:2608.15889v1 [q-fin.CP], August 16, 2026. DOI: 10.48550/arXiv.2608.15889. https://arxiv.org/abs/2608.15889"
  - "https://github.com/ereinha/Forex-QUBO (commit 1b4d9e9c67e78d17ce8a7cfcf488f77242a939d2, August 14, 2026, path: Forex_QUBO.ipynb)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage: Exact Anchor-Gauge Reweighting, Provably Sufficient Penalties, and Annealing Baselines (Reinhardt & Hauser 2026)

## Provenance

- **Primary paper:** Eric A. F. Reinhardt and Adam J. Hauser (Department of Physics and Astronomy, The University of Alabama), *"Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage"*, arXiv preprint `arXiv:2608.15889v1 [q-fin.CP]`, submitted August 16, 2026.
- **Canonical stable URL:** [https://arxiv.org/abs/2608.15889](https://arxiv.org/abs/2608.15889)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2608.15889](https://doi.org/10.48550/arXiv.2608.15889)
- **Full Text HTML:** [https://arxiv.org/html/2608.15889v1](https://arxiv.org/html/2608.15889v1)
- **Reference implementation code:** [https://github.com/ereinha/Forex-QUBO](https://github.com/ereinha/Forex-QUBO)
- **Full Commit SHA:** `1b4d9e9c67e78d17ce8a7cfcf488f77242a939d2` (August 14, 2026)
- **Verified Code Path:** `Forex_QUBO.ipynb` (Jupyter notebook containing full QUBO builder, Johnson gauge-fixing transformer, penalty derivations, Held–Karp baseline, and D-Wave SimulatedAnnealingSampler benchmarking suite)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0); code public repository on GitHub
- **Audit confirmation:** Pre-write search against repository commits, file paths, and Hermes Wiki Brain confirmed zero existing records matching `arXiv:2608.15889`, `Forex-QUBO`, or anchored QUBO currency arbitrage.

## Economic mechanism

### Source-reported

Currency arbitrage (CA) exploits transient discrepancies in the relative valuations of currency pairs across foreign exchange markets or venues. When exchange rates across pairs diverge from triangular or polygonal parity, a trader can execute a sequence of trades along a closed cycle $s \to c_1 \to c_2 \to \dots \to c_m \to s$, ending in the same currency with a risk-free net positive gain, minus per-transaction fees.

In real-world systematic trading, practical arbitrage strategies face two critical physical constraints:
1. **Anchor Reserve Currency Constraint:** Traders hold balances in specific liquid reserve currencies (e.g., USD, EUR, AUD). An unanchored cycle requires executing an entering trade to access the cycle, incurring additional transaction fees and execution latency. Anchoring the search to a pre-defined starting currency $s$ eliminates unneeded entry legs and aligns the cycle with operational inventory.
2. **Per-Transaction Friction & Bounded Cycle Length:** Each hop in an arbitrage cycle incurs exchange fees, half-spread crossing costs, and execution risk. Long cycles face exponential degradation in net profitability and heightened vulnerability to latency-induced adverse selection. Practical cyclic arbitrage must balance gross log-returns against an explicit per-step penalty $\gamma / \alpha \approx f$ (where $f$ is the proportional transaction fee).

From a computational complexity perspective, identifying a maximally profitable simple cycle subject to bounded length and anchoring constraints is NP-hard. Classical Held–Karp dynamic programming scales as $O(2^{N-1} N^2)$ time and $O(2^{N-1} N)$ memory per anchor, facing a hard computational wall at $N \approx 20 - 25$ currencies. Mapping the problem to a Quadratic Unconstrained Binary Optimization (QUBO) problem enables heuristic combinatorial solvers and quantum annealers to sample low-energy configurations.

### Research interpretation

The hypothesized economic mechanism is **pure structural cross-rate spatial arbitrage in complete exchange graphs**:
1. **Law of One Price Disruption:** Fragmented liquidity, asynchronous quoting, and idiosyncratic order flow create temporary pricing dislocations where the synthetic cross-rate differs from the direct quote by more than round-trip execution costs.
2. **Combinatorial Graph Search:** In an $N$-asset exchange network, the number of potential simple cycles grows combinatorially ($O(N!)$ unconstrained, $O(N^{K-1})$ for fixed length $K$). When $K$ grows with $N$, deterministic enumeration becomes computationally intractable for real-time execution.
3. **Anchor Gauge Fixing as Precision Conditioning:** Prior QUBO formulations suffered from a dynamic range catastrophe: raw log-exchange rates $L_{ij} = \ln R_{ij}$ have magnitudes $O(1)$, whereas real arbitrage profits are on the order of basis points ($10^{-4}$). Analog hardware (such as superconducting flux-qubit annealers) has finite coupling precision (equivalent to ~4–8 bits of dynamic range), causing true arbitrage signals to be drowned in hardware quantization noise. Exact anchor-gauge reweighting eliminates this friction by subtracting node potentials $\phi_i = L_{si}$, shifting all effective edge weights to the arbitrage deviation scale ($10^{-4}$) without modifying the optimal cycle.

## Signal

### Mathematical formulation (Source-reported)

1. **Variables and Notation:**
   - Let $N$ be the number of currencies, and $s \in \{1, \dots, N\}$ denote the designated anchor currency.
   - $\mathcal{C}^*$ is the set of $N - 1$ non-start currencies.
   - $K$ is the maximum allowed cycle length; horizon $T = K - 1$.
   - $x_{i,k} \in \{0, 1\}$ is a binary decision variable indicating currency $i \in \mathcal{C}^*$ is visited at cycle step $k \in \{1, \dots, T\}$.
   - Logical variable count: $(N - 1) \times T = (N - 1)(K - 1)$.
   - $S_k \equiv \sum_{i \in \mathcal{C}^*} x_{i,k}$ is the total currency count selected at step $k$.
   - $L_{ij} = \ln R_{ij}$ is the log-exchange rate matrix (units of currency $j$ received per unit of currency $i$).

2. **Constraint Hamiltonian $H_c$:**
   - **Column Uniqueness (at most one currency per step):**
     $$H_{col} = 2 A_{col} \sum_{k=1}^T \sum_{\substack{i < j \\ i, j \in \mathcal{C}^*}} x_{i,k} x_{j,k}$$
   - **Row Uniqueness (currency visited at most once across the cycle):**
     $$H_{row} = A_{row} \sum_{i \in \mathcal{C}^*} \sum_{1 \le k < k' \le T} x_{i,k} x_{i,k'}$$
   - **Contiguity (no restarting after cycle termination):**
     $$H_{contig} = A_{contig} \sum_{k=1}^{T-1} (S_{k+1} - S_{k+1} S_k)$$
   - **Non-empty Cycle Initiation (must start at step 1):**
     $$H_{start} = A_{start} (1 - S_1)$$
   - **Total Constraint Hamiltonian:**
     $$H_c = H_{col} + H_{row} + H_{contig} + H_{start}$$

3. **Profit Hamiltonian $H_p$:**
   - **First Step from Anchor:**
     $$H_{step1} = \sum_{j \in \mathcal{C}^*} (-\alpha L_{sj}) x_{j,1}$$
   - **Provisional Return-to-Anchor Close:**
     $$H_{close} = \sum_{k=1}^{T-1} \sum_{i \in \mathcal{C}^*} (-\alpha L_{is}) x_{i,k}$$
   - **Continuation to Next Step (Telescoping Edge Substitution):**
     $$H_{continue} = \sum_{k=1}^{T-1} \sum_{i \in \mathcal{C}^*} \sum_{j \in \mathcal{C}^*} \big(-\alpha (L_{ij} - L_{is})\big) x_{i,k} x_{j,k+1}$$
   - **Horizon Truncation Close:**
     $$H_{truncate} = \sum_{i \in \mathcal{C}^*} (-\alpha L_{is}) x_{i,T}$$
   - **Per-Transaction Fee Length Penalty:**
     $$H_{len} = \gamma \sum_{k=1}^T \sum_{i \in \mathcal{C}^*} x_{i,k}$$
   - **Total Profit Hamiltonian:**
     $$H_p = H_{step1} + H_{close} + H_{continue} + H_{truncate} + H_{len}$$
   - **Full Problem Hamiltonian:**
     $$H = H_c + H_p$$
     For any feasible simple cycle $s \to c_1 \to \dots \to c_m \to s$ ($1 \le m \le T$), the profit Hamiltonian evaluates exactly to:
     $$H_p = -\alpha \left( L_{sc_1} + \sum_{k=1}^{m-1} L_{c_k c_{k+1}} + L_{c_m s} \right) + \gamma m$$
     which is strictly equivalent to maximizing the fee-adjusted net log-return $\sum L - (\gamma / \alpha) m$.

4. **Theorem: Provably Sufficient Penalty Weights (Source-reported):**
   Let $L_\infty = \max_{a \ne b} |L_{ab}|$ over the log-rate matrix supplied to the QUBO. If:
   $$\begin{aligned}
   A_{start} &> \gamma + 2 \alpha L_\infty \\
   A_{contig} &> (T - 1) \max(0, \alpha L_\infty - \gamma) \\
   A_{row} &> 4 \alpha L_\infty \\
   A_{col} &> 2 A_{contig} + 5 \alpha L_\infty + \frac{1}{2} A_{start}
   \end{aligned}$$
   then every ground state of $H$ encodes a nonempty, anchored, contiguous, simple cycle maximizing the fee-adjusted log-return. Every infeasible configuration admits a local single-spin repair move that strictly lowers energy, preventing non-optimal local traps during annealing.

5. **Exact Anchor-Gauge Reweighting (Source-reported):**
   Prior to QUBO construction, exchange rates undergo Johnson-style node-potential reweighting:
   $$\tilde{L}_{ij} = L_{ij} - (\phi_j - \phi_i), \quad \text{where } \phi_i = L_{si}, \quad \phi_s = 0$$
   Because potentials telescope around any closed cycle ($\sum_{\text{cycle}} (\phi_{next} - \phi_{curr}) = 0$), the cycle log-return is algebraically invariant.
   After transformation:
   - $\tilde{L}_{sj} = 0$ identically;
   - $\tilde{L}_{is} = L_{is} + L_{si}$ (anchor round-trip spread);
   - $\tilde{L}_{ij} = L_{ij} - L_{sj} + L_{si}$ (triangular arbitrage deviation through the anchor).
   This reduces the largest QUBO coefficient on the 10-currency $K=6$ instance from $25.3$ to $1.9 \times 10^{-2}$, compressing the dynamic range by roughly $10^3$ and reducing the max-coefficient-to-profit ratio from $3.6 \times 10^4$ to $26$.

### Operational Specifications & Parameter Classifications

- **Formation Timestamp:**
  - `source-reported`: Discrete snapshot of the complete pairwise exchange-rate matrix $R_{ij}$ at evaluation epoch $t$.
  - `research-proposed`: In live FX or crypto, generated on every order-book ticker update or periodic $50\,\text{ms}$ snapshot.
- **Lookback Window:**
  - `source-reported`: Zero lookback (pure spatial instantaneous arbitrage; no historical time-series features).
- **Execution Timestamp / Order Timing:**
  - `source-reported`: Underspecified in paper; assumed instantaneous execution at quoted rates.
  - `research-proposed`: Concurrent execution of all $m+1$ legs via IOC (Immediate-Or-Cancel) limit orders or atomic batch smart contract within $25\,\text{ms}$ of signal formation ($T_{\text{exec}} = t + \tau_{\text{latency}}$).
- **Entry Trigger:**
  - `source-reported`: Ground state configuration of $H$ yields a feasible cycle with positive fee-adjusted log-return:
    $$\text{Score} = \sum_{e \in \text{cycle}} L_e - \frac{\gamma}{\alpha} m > 0$$
- **Exit Trigger:**
  - `source-reported`: The cycle is self-closing by construction; returns to the starting reserve currency $s$ at leg $m+1$.
- **Holding Period:**
  - `source-reported`: Zero nominal holding period (sub-second execution cycle).
- **Position Sizing:**
  - `source-reported`: Unit capital sizing (e.g., $1\,\text{AUD}$ / $1\,\text{USD}$ nominal initial trade).
  - `research-proposed`: Position size $V_0$ set to the minimum executable depth across all legs:
    $$V_0 = \min_{k=0}^m \text{Depth}_{c_k \to c_{k+1}}$$
    capped at maximum inventory allocation (e.g., $\$50,\!000$ in crypto spot or $\$2,\!000,\!000$ in G10 FX).
- **Parameters & Hyperparameters:**
  - `source-reported`:
    - Scale parameter: $\alpha = 1.0$ (arbitrary positive scaling constant).
    - Length fee penalty: $\gamma / \alpha = -\ln(1 - f)$, swept over $\gamma \in [5 \times 10^{-5}, 1 \times 10^{-3}]$ (representing $0.5$ bps to $10.0$ bps per trade).
    - Safety margin multiplier for sufficient weights: $\text{safety} = 1.05$.
    - Heuristic weights used in sweeps: $A_{col} = 2 \alpha L_\infty + \gamma$, $A_{row} = 2 \alpha L_\infty$, $A_{contig} = \alpha L_\infty$, $A_{start} = A_{col}$.
    - Benchmark setting: $N = 10$ currencies, $K = 6$ (horizon $T = 5$), synthetic noise $\sigma = 10^{-4}$ ($1$ bps imbalance).
    - Annealing parameters: 1280 reads, 160 sweeps per run.

## Required data

- **Universe:**
  - `source-reported`: $N \in [6, 17]$ currencies (evaluated on synthetic cross-rate matrices perturbed by monetary noise $\sigma \in [10^{-5}, 10^{-3}]$, and benchmarked against standard G10/G20 FX currency pairs).
  - `research-proposed`: Top 10–20 liquid crypto spot assets paired against USDT, USDC, BTC, and ETH on a single centralized exchange (e.g., Binance), or cross-pool tokens on decentralized AMMs.
- **Venue:**
  - `source-reported`: Generic foreign exchange market infrastructure.
  - `research-proposed`: High-throughput spot exchange order books (Binance Spot, Bybit Spot, or LMAX / Currenex for institutional FX).
- **Market Type:** Spot currency pairs (reciprocal or bid/ask quote matrices).
- **Timeframe:** Tick / order-book snapshot level ($10 - 100\,\text{ms}$ updates).
- **Fields:** Best bid price ($P_{\text{bid}}$), best ask price ($P_{\text{ask}}$), top-of-book depth ($V_{\text{bid}}, V_{\text{ask}}$) for all directed currency pairs $(i, j)$.
- **Point-in-Time & Availability:** Strict point-in-time synchronization required; rate matrix must reflect simultaneous executable quotes across all pairs to prevent phantom arbitrage signals.
- **Missing Data & Asymmetric Pairs:** Missing direct pairs $L_{ij}$ handled by setting $L_{ij} = -\infty$ (or setting $R_{ij} = 0$), preventing selection of nonexistent market pairs.

## Execution assumptions

- **Transaction Costs & Fees:**
  - `source-reported`: Uniform proportional fee $f$ modeled via length penalty $\gamma / \alpha = -\ln(1 - f) \approx f$ across $m$ legs. Pair-specific fees $f_{ij}$ incorporated by mapping $L_{ij} \to L_{ij} + \ln(1 - f_{ij})$, which charges all $m+1$ trades and leaves $H_{len}$ as a pure length regularizer.
  - `research-proposed`: Institutional VIP tier fee schedule assumed (e.g., Binance Spot Maker/Taker: 2.0 bps taker, or G10 FX half-spread: 0.5–1.5 bps).
- **Fill Model:**
  - `source-reported`: 100% full fill at quoted rate assumed.
  - `research-proposed`: Immediate-or-Cancel (IOC) limit order at best quote. Partial fills treated as execution failures requiring immediate market unwinding to reserve currency.
- **Slippage & Impact:**
  - `source-reported`: Omitted in theoretical formulation; rates treated as infinitely liquid at quoted price.
  - `research-proposed`: Market impact modeled via linear price impact function $\Delta P / P = \eta \cdot (V_0 / \text{Depth}_{\text{L1}})$; trades restricted to $V_0 \le 0.5 \times \text{Depth}_{\text{L1}}$ to avoid crossing into deeper order book levels.
- **Latency & Execution Model:**
  - `source-reported`: CPU sampler call time measured ($0.16 - 2.62\,\text{s}$ for simulated annealing; $0.01 - 1.05\,\text{s}$ for exact Held–Karp baseline on single CPU). Paper notes practical CA operates at sub-millisecond to millisecond latency where classical dynamic programming currently dominates up to $N = 17$.
  - `research-proposed`: Colocated execution pipeline required; sub-millisecond execution budget.

## Evidence

### Source-reported

All quantitative results below are from Reinhardt & Hauser (arXiv:2608.15889v1, Sections 3.2, 4, 4.1, Tables 1 & 2, Figures 4–12, and Appendix A data tables):

1. **Logical Variable and Connectivity Scaling (Table 1):**
   - **Proposed Encoding:** $(N - 1)(K - 1)$ logical qubits, maximal connectivity $3N + K - 8$.
   - **Mazzei et al. (2025):** $NK$ logical qubits, maximal connectivity $3N - 1$.
   - **Roy et al. (2025):** $N(K + 1)$ logical qubits, maximal connectivity $3N + K - 3$.
   - **1QBit Node-Based (Rosenberg 2016):** $NK$ logical qubits, maximal connectivity $3N + K - 4$.
   - **Deshpande et al. (2025):** $N^2$ logical qubits, maximal connectivity $2N - 4$.
   - **1QBit Edge-Based (Rosenberg 2016):** $N^2$ logical qubits, maximal connectivity $4N - 7$.
   *At $N=10, K=6$, the proposed model requires 45 logical qubits vs. 60–90 for all prior models.*

2. **Empirical Benchmark at Matched Budget (Table 2, $N=10, K=6, \sigma = 10^{-4}$):**
   - **Proposed (10 anchors):** 45 variables, 10 runs, **Score gap = 0 (exact Held–Karp optimum recovered)**, Total sampler time = $2.62\,\text{s}$, Per-run time = $0.26\,\text{s}$.
   - **Proposed (Worst of 10 anchors):** 45 variables, 1 run, Score gap = $3.3 \times 10^{-5}$, Per-run time = $0.26\,\text{s}$.
   - **Roy et al. (2025):** 70 variables, 4 runs (by length), Score gap = $3.8 \times 10^{-6}$, Sampler time = $0.87\,\text{s}$.
   - **1QBit Node-Based (Rosenberg 2016):** 60 variables, 4 runs, Score gap = $8.0 \times 10^{-6}$, Sampler time = $0.73\,\text{s}$.
   - **Mazzei et al. (2025):** 70 variables, 1 run, Score gap = $1.4 \times 10^{-5}$, Sampler time = $0.16\,\text{s}$.
   - **Deshpande et al. (2025):** 90 variables, 1 run, Score gap = $3.7 \times 10^{-5}$, Sampler time = $0.53\,\text{s}$.
   - **1QBit Edge-Based (Rosenberg 2016):** 90 variables, 1 run, Score gap = $5.5 \times 10^{-5}$, Sampler time = $0.74\,\text{s}$.
   *The proposed encoding is the only model among all six to recover the exact optimal cycle (zero score gap) under matched sampler settings.*

3. **Gauge-Fixing Dynamic Range Compression:**
   - Without gauge fixing, QUBO coefficients spanned $[-25.3, +25.3]$.
   - With anchor-gauge reweighting, maximum coefficient shrank to $1.9 \times 10^{-2}$.
   - Dynamic range ratio (max coefficient / fee-adjusted return) fell from $3.6 \times 10^4$ to $26$.
   - Without gauge fixing, the same sampler budget produced score gaps roughly 10x larger ($2 - 3 \times 10^{-4}$).

4. **Trading Fee / Length Penalty Parameter Sweep ($\gamma \in [5 \times 10^{-5}, 1 \times 10^{-3}]$):**
   - Across the entire sweep (Table 40), the score gap between simulated annealing and the exact Held–Karp baseline never exceeded $1.3 \times 10^{-4}$, and was at floating-point zero for most grid points.
   - For fees exceeding per-edge profit ($\gamma \ge 5 \times 10^{-4}$), both annealer and exact solver correctly collapsed the optimal cycle to length 3 or single-hop round-trips ($0.0$ raw profit).

5. **Classical vs. Annealing Compute Time (Table 37 & 38):**
   - At $N = 10, K = 6$: Held–Karp exact baseline completed in $0.14\,\text{s}$ (CPU), while simulated annealing required $2.27\,\text{s}$ (1280 reads) and $17.52\,\text{s}$ (10240 reads).
   - At $N = 14, K = 6$: Held–Karp required $1.03\,\text{s}$, while simulated annealing required $5.22\,\text{s}$ (1280 reads) and $40.55\,\text{s}$ (10240 reads).
   - The exact solver was 1 to 2 orders of magnitude faster at 1280 reads, and 2 to 3 orders faster at 10240 reads across all tested sizes $N \le 14$.

6. **D-Wave Advantage Hardware Minor-Embedding:**
   - Target architecture: D-Wave Advantage (Pegasus-16 graph, degree 15 native connectivity).
   - Problem instances up to $N = 17$ currencies with maximum cycle length $K = 14$ embed onto Pegasus-16, requiring 4,343 physical qubits with a maximum chain length of 40 and mean chain length of 20.88.
   - Brute-force enumeration at this scale would require evaluating over 59 trillion permutations ($5.9 \times 10^{13}$).

### Independently reproduced

Not independently reproduced. All figures and equations trace directly to Reinhardt & Hauser (2026) and the public repository `Forex_QUBO.ipynb`.

### Negative evidence

1. **Classical Exact Dominance at Practical Scales:**
   On common CPU hardware, classical simulated annealing does **not** outperform the exact Held–Karp dynamic programming baseline anywhere in the tested range ($N \le 14, K \le 11$). The exact solver is 10x to 1000x faster, running in under 1 second for $N \le 14$.
2. **Solution Degradation at Extended Cycle Lengths:**
   When maximum cycle length $K > 5$ at $N = 14$ currencies (Figure 10b), simulated annealing failed to locate the exact global optimum, settling on score-suboptimal configurations.
3. **Hardware Quantum Advantage Remains Unproven:**
   Physical quantum annealing on actual D-Wave hardware was not benchmarked in the paper. Projected performance relies on classical simulated annealing and embedding resource projections; analog noise, chain breaks, thermal excitations, and readout latency on physical QPUs could materially degrade solution fidelity.

## Falsification plan

1. **Exact Baseline Latency Race:**
   - *Test:* Benchmark execution time of the QUBO formulation (either on simulated annealing or physical QPU) against an optimized C++/Rust Held–Karp solver on live market rate matrices.
   - *Failure rule (`research-defined falsification threshold`):* If the exact Held–Karp solver finds the optimal cycle in $< 5\,\text{ms}$ for all universes up to $N = 20$, the QUBO annealing formulation provides zero operational latency advantage for high-frequency trading.
2. **Fee-Inclusion Net Profitability Stress Test:**
   - *Test:* Inject real institutional taker fee schedules ($f = 2.0 - 4.0\,\text{bps}$) and observed bid-ask spreads on Binance or institutional FX feeds across top 15 pairs.
   - *Failure rule (`research-defined falsification threshold`):* If the optimal fee-adjusted cycle net return $\sum L - (\gamma / \alpha) m \le 0$ across $> 99.5\%$ of 1-second snapshots over a 30-day testing window, the spatial arbitrage capacity is fully saturated by latency-arbitrageurs.
3. **Chain Break and Embedding Fidelity Test on Quantum Hardware:**
   - *Test:* Deploy the embedded QUBO onto D-Wave Advantage2 or Advantage Pegasus-16; measure ground-state success probability as a function of chain strength $J_{\text{chain}}$.
   - *Failure rule (`research-defined falsification threshold`):* If physical chain break frequency exceeds $15\%$ or the probability of recovering a feasible simple cycle falls below $5\%$ at 10,000 reads, the embedding overhead invalidates quantum speedup claims.
4. **Adverse Selection & Execution Slippage Test:**
   - *Test:* Simulate sequential order dispatch across the $m$ legs with a realistic $10\,\text{ms}$ network propagation delay per leg.
   - *Failure rule (`research-defined falsification threshold`):* If realized round-trip return degrades below zero on $> 50\%$ of executed cycles due to quotes being cancelled or filled before the final leg closes, the zero-holding-period assumption is falsified.

## Crypto portability

- **Portability Status:** `adapted` and `unproven` (Research interpretation; primary source investigates general FX and synthetic rate matrices).
- **Adaptation Rationale:**
  - In cryptocurrency markets, cyclic spatial arbitrage (e.g., USDT $\to$ BTC $\to$ ETH $\to$ SOL $\to$ USDT) is widely practiced on centralized exchanges (Binance, OKX, Bybit) and across decentralized AMM pools (Uniswap, Curve).
  - The anchored QUBO formulation directly applies to crypto spot books: the anchor $s$ is naturally set to a core quote stablecoin (USDT or USDC).
- **Crypto-Specific Frictions & Risks:**
  - **Asymmetric Multi-Token Fees:** Crypto fee schedules vary by VIP level, BNB/token fee deductions, and currency pair promotions (e.g., zero-fee BTC/FDUSD pairs). Pair-specific fees $f_{ij}$ must be directly absorbed into $L_{ij} \to L_{ij} + \ln(1 - f_{ij})$ as detailed in Section 3 of the source.
  - **Tick Size & Lot Size Discretization:** While the QUBO optimizes continuous log-rates, real crypto order books enforce lot-size step minimums (e.g., 0.00001 BTC) and precision truncation. This causes fractional token dust to accumulate along the cycle.
  - **Exchange Rate Microstructure Noise:** In crypto, inverted rates ($L_{ji} \ne -L_{ij}$) arise from distinct bid/ask spreads. The directed log-rate matrix must use $L_{ij} = \ln(P_{ij}^{\text{bid}})$ when selling asset $i$ for $j$, and $L_{ij} = -\ln(P_{ji}^{\text{ask}})$ when buying asset $j$ with $i$.
  - **Fast MEV & CEX Latency Competition:** On CEXs, internal colocation engines execute triangular cycles in $< 100\,\mu\text{s}$. On DEXs, MEV searchers bundle cyclic arbitrage via Flashbots or PGA (Priority Gas Auctions). A solver requiring $> 10\,\text{ms}$ will be front-run on public mempools.

## Limitations

1. **Underspecified Live Execution Mechanism:** The primary source does not test real-time order submission, socket latency, or order-book queue depletion.
2. **Computational Advantage Threshold:** Classical dynamic programming (Held–Karp) completely dominates simulated annealing across all practical FX problem sizes ($N \le 17$). Quantum annealing can only offer potential value in hypothetical large networks ($N \ge 25$) where cycle lengths are unconstrained.
3. **No Independent Hardware Quantum Execution:** Findings rely on D-Wave's classical CPU `SimulatedAnnealingSampler`; no physical QPU hardware runs are presented.
4. **Single-Seed Sensitivity:** The authors explicitly note that benchmark entries derive from single sampler seeds and thread-dependent random streams, introducing variability at the $10^{-5}$ score gap level.
5. **Static Rate Snapshot Assumption:** In live trading, prices move asynchronously during the time required to solve the QUBO, potentially invalidating the detected cycle before orders reach the matching engine.

## Implementation status

- `not-implemented` in our research stack.
- No NautilusTrader, PyBroker, paper trading, testnet, or live trading components exist.
- Pure theoretical and computational research capture.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record captures external peer-reviewed academic research for strategy discovery. Presence in this repository does **not** authorize implementation, paper trading, testnet verification, or live capital allocation.

## Related Wiki records

- `[[quant/dex-cyclic-arbitrage-constant-product-amm-2026-09-01]]` (Cyclic arbitrage mechanics on decentralized constant-product AMMs)
- `[[quant/photonic-quantum-annealing-constrained-factor-allocation-qubo-2026-09-04]]` (QUBO formulation and quantum annealing for constrained factor allocation)
- `[[quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]]` (Multi-currency FX graph representations and statistical arbitrage)

## Sources

1. Eric A. F. Reinhardt and Adam J. Hauser (Department of Physics and Astronomy, The University of Alabama), *"Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage"*, arXiv preprint `arXiv:2608.15889v1 [q-fin.CP]`, submitted August 16, 2026. DOI: [10.48550/arXiv.2608.15889](https://doi.org/10.48550/arXiv.2608.15889). Stable URL: [https://arxiv.org/abs/2608.15889](https://arxiv.org/abs/2608.15889). Full HTML: [https://arxiv.org/html/2608.15889v1](https://arxiv.org/html/2608.15889v1).
2. Eric A. F. Reinhardt, *Forex-QUBO* reference repository, GitHub repository: [https://github.com/ereinha/Forex-QUBO](https://github.com/ereinha/Forex-QUBO), commit SHA `1b4d9e9c67e78d17ce8a7cfcf488f77242a939d2` (August 14, 2026), file: `Forex_QUBO.ipynb`.
