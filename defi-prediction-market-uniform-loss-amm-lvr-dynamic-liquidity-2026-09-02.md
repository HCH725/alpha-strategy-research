---
schema: strategy-research-record-v1
title: "Uniform-Loss Automated Market Making for Prediction Markets: State-Independent LVR and Dynamic Liquidity Scheduling"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - prediction-markets
  - loss-versus-rebalancing
  - lvr
  - dynamic-liquidity
  - win-martingale
  - adverse-selection
status: research-only
confidence: medium
source_as_of: 2026-07-25
sources:
  - "Ciamac C. Moallemi, Dan Robinson, Brian Zhu, 'Uniform-Loss Automated Market Making for Prediction Markets', arXiv:2607.17428v1 [q-fin.TR], July 2026. https://arxiv.org/abs/2607.17428"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Uniform-Loss Automated Market Making for Prediction Markets: State-Independent LVR and Dynamic Liquidity Scheduling

## Provenance

- **Paper URL:** https://arxiv.org/abs/2607.17428
- **Full arXiv ID:** arXiv:2607.17428v1 [q-fin.TR]
- **Authors:** Ciamac C. Moallemi (Columbia University / Paradigm), Dan Robinson (Paradigm), Brian Zhu (Paradigm)
- **Publication Date:** July 2026
- **Conference Acceptance:** Advances in Financial Technologies (AFT 2026)
- **Primary Category:** Quantitative Finance - Trading and Market Microstructure (`q-fin.TR`)
- **Theoretical Scope:** Mathematical formulation and closed-form derivation of "Uniform AMMs" for binary prediction markets, establishing the relationship between win-martingales, boundary value problems (BVPs), and state-independent Loss-Versus-Rebalancing (LVR) profiles.

## Economic mechanism

### Source-reported

In standard Automated Market Makers (such as Constant Product Market Makers or logarithmic market scoring rules / LMSR), liquidity providers (LPs) or market creators who subsidize price discovery suffer from **Loss-Versus-Rebalancing (LVR)** due to adverse selection from informed arbitrageurs. In prediction markets where terminal payoffs collapse to $\{0, 1\}$ at a fixed expiration time $T$, standard AMMs generate highly non-uniform loss rates: LVR spikes exponentially when probability $p$ is in certain regions or when price approaches resolution boundaries, causing LPs to be depleted unevenly across price states and time.

The authors prove that:
1. **Uniform AMM Definition:** A "uniform AMM" is an automated market maker characterized by the property that its instantaneous Loss-Versus-Rebalancing is strictly proportional to total pool value and **completely independent of the current token price $p \in (0, 1)$**:
   $$\frac{d\text{LVR}_t}{dt} = \lambda \cdot V(p_t)$$
   where $V(p)$ is the pool-value function and $\lambda$ is a state-independent rate constant.
2. **Win-Martingale & Boundary Value Problem Correspondence:** The authors model price evolution as a "win-martingale" $P_t$ (a martingale bounded on $[0, 1]$ converging to 0 or 1 at time $T$). Requiring state-independent uniform LVR yields a second-order ordinary differential equation / Boundary Value Problem (BVP) on the pool-value function $V(p)$:
   $$\frac{1}{2} \sigma^2(p) V''(p) + \lambda V(p) = 0$$
   subject to the boundary conditions $V(0) = V(1) = 0$ (or target terminal subsidization constraints).
3. **Dynamic Liquidity Management:** By varying pool liquidity $L(t)$ dynamically over the market lifecycle $t \in [0, T]$, market designers can implement any pre-specified target expected cumulative loss schedule $\mathbb{E}[\text{LVR}_{[0, t]}]$, ensuring that information aggregation subsidies are distributed uniformly per unit of time rather than exhausted in early trading bursts.

### Research interpretation

This theoretical advance provides two quantitative mechanisms for decentralized prediction market operators and LP capital allocators:
1. **LVR-Neutral Prediction Market Liquidity Provision (Defensive Yield Alpha):**
   - Traditional AMMs (e.g., Uniswap v2/v3 or standard LMSR) subject LPs to unpredictable toxic arbitrage extraction whenever prices drift away from initialization points.
   - By depositing liquidity into a Uniform AMM whose invariant $F(x, y, L)$ satisfies the derived BVP, LPs guarantee that adverse-selection decay occurs at a predictable, state-independent rate $\lambda$, eliminating price-state convexity drag.
2. **Dynamic Liquidity Scheduling Arbitrage & Fee Harvesting (Execution Alpha):**
   - Prediction market volume and information arrival typically spike near event resolution ($t \to T$).
   - Dynamically adjusting liquidity $L(t) \propto \sqrt{\tau(t)}$ (where $\tau(t) = T - t$) matches the time-decay of the underlying win-martingale volatility, maximizing fee capture from uninformed retail volume while bounding maximum worst-case LVR extraction by informed traders.

## Signal

### Signal A: Uniform Pool Invariant Reconstruction
- **Fair Price Variable:** $p \in (0, 1)$ representing the binary outcome probability.
- **Pool-Value Function $V(p)$:** Derived as the unique solution to the BVP for a chosen win-martingale volatility profile $\sigma(p)$:
  $$V(p) = \frac{1}{\lambda} \phi(\Phi^{-1}(p)) \quad \text{(for Bachelier / Normal win-martingales)}$$
  where $\Phi(\cdot)$ and $\phi(\cdot)$ are the standard normal CDF and PDF.
- **Reserve Demand Functions:**
  $$X(p) = V(p) + (1 - p) V'(p)$$
  $$Y(p) = V(p) - p V'(p)$$
- **AMM Invariant $F(x, y, L)$:**
  $$F(x, y, L) = \inf_{p \in (0, 1)} \frac{p x + (1 - p) y}{V(p)} - L = 0$$

### Signal B: Dynamic Liquidity Allocation Schedule
- **Time to Resolution:** $\tau = T - t$.
- **Target Loss Budget:** Total allocated subsidy $S_{\text{max}}$.
- **Dynamic Liquidity Rule:** Set active liquidity $L(t)$ proportional to remaining duration and instantaneous event volatility:
  $$L^*(t) = S_{\text{max}} \cdot \frac{\sqrt{T - t}}{\int_0^T \sqrt{T - s} \, ds}$$
- **Rebalancing Trigger:** If market probability $p_t$ shifts by $\Delta p > 0.05$ or time elapsed $\Delta t > 1\text{ hour}$, rebalance pool invariant parameters via on-chain smart contract parameter update to maintain uniform LVR rate $\lambda$.

## Required data

- **Instrument:** Prediction market binary outcome tokens (Yes/No outcome pairs settling to $\{0, 1\}$ at expiration $T$).
- **Universe:** Binary prediction market contracts (e.g., Polymarket, Kalshi, Gnosis conditional tokens).
- **Venue:** Automated Market Maker contracts deploying custom CFMM invariants on EVM-compatible networks (Ethereum, Arbitrum, Polygon, Base).
- **Timeframe:** Continuous-time theoretical framework; block-by-block parameter updates and swap execution.
- **Fields:**
  - Token reserves $x$ and $y$.
  - Fair market probability $p$ (observed from external oracles or high-frequency order books).
  - Time to expiration $\tau = T - t$.
  - Pool value $V(p)$ and invariant liquidity parameter $L$.
- **Point-in-time:** Strictly causal state variables without future knowledge of event resolution.

## Execution assumptions

- **AMM Model:** Constant Function Market Maker (CFMM) with state-dependent or dynamic invariant parameters.
- **Arbitrageur Fill Model:** Continuous-time zero-latency external arbitrageurs who trade against the pool whenever the marginal price $p_{\text{AMM}} \neq p_{\text{external}}$, extracting instantaneous LVR.
- **Fees:** Swap fee $\gamma \in [0.001, 0.02]$ (10 to 200 bps) levied on incoming taker volume to offset LVR subsidization costs.
- **Gas / Rebalancing Cost:** Modeled at $50,000–$120,000 gas per on-chain swap / parameter recalibration transaction.

## Evidence

### Source-reported

- **Mathematical Proof of Uniformity:** Analytical proof that the unique class of AMMs satisfying state-independent instantaneous Loss-Versus-Rebalancing ($\frac{d\text{LVR}}{dt} \propto V(p)$) corresponds directly to solutions of the second-order BVP derived from the win-martingale drift-diffusion generator.
- **Separable Win-Martingale Equivalence:** Proof that for any separable win-martingale with volatility function $\sigma(p, t) = \alpha(t) \beta(p)$, there exists a concave pool-value function $V(p)$ yielding uniform LVR across all price states.
- **Normal pm-AMM Solution:** Closed-form solution showing that the Gaussian win-martingale yields a pool-value function proportional to the standard normal density $\phi(\Phi^{-1}(p))$, producing bounded, smooth bonding curves across the entire open interval $p \in (0, 1)$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Oracle Discrepancy & Jumps:** If the underlying binary event experiences discontinuous jump processes (e.g., sudden breaking news or court rulings), continuous win-martingale assumptions break down, and arbitrageurs extract jump losses exceeding continuous-time LVR bounds.
- **Smart Contract Gas Overhead:** Dynamic liquidity rescheduling requires periodic on-chain parameter updates; during high Ethereum L1 gas regimes, transaction costs can erode the theoretical subsidization efficiency gains.

## Falsification plan

1. **Empirical LVR Uniformity Verification:** Simulate high-frequency arbitrage trading against the Gaussian Uniform AMM versus standard Uniswap v2 and LMSR invariants using historical 1-second price series from 500 resolved Polymarket contracts. **Failure rule:** If the variance of realized $\frac{\text{LVR}(p)}{V(p)}$ across price buckets $p \in [0.05, 0.95]$ is not at least 70% lower than that of LMSR, the state-independence thesis is rejected.
2. **Cumulative Subsidy Budget Adherence:** Evaluate the dynamic liquidity schedule $L^*(t)$ across 100 simulated event paths. **Failure rule:** If total realized LVR deviates from the target budget $S_{\text{max}}$ by more than $\pm 15\%$, dynamic liquidity scheduling is falsified.
3. **Net LP Profitability under Fee Inflows:** Backtest net LP return (swap fees collected minus realized LVR) with realistic retail order flow. **Failure rule:** If net LP return is negative across $> 60\%$ of markets, uniform subsidization alone is insufficient to protect passive capital without dynamic fee scaling.

## Crypto portability

**direct**

The mechanism is designed directly for decentralized finance (DeFi) automated market makers and prediction market protocols.
- **Smart Contract Implementation:** The invariant $F(x, y, L)$ can be implemented directly as an EVM custom AMM contract (e.g., Uniswap v4 hook, Balancer v3 custom pool, or standalone prediction AMM).
- **Binary Token Mechanics:** Naturally maps to ERC-1155 / Gnosis Conditional Token Framework (CTF) contracts where outcome tokens have hard boundaries at 0 and 1 USDC.

## Limitations

- **Theoretical Model Reliance:** Assumes continuous-time Brownian belief dynamics (win-martingales); does not explicitly incorporate discrete jumps or discontinuous event resolutions.
- **No Free Lunch in Subsidization:** Uniform AMMs optimize the *distribution* and *predictability* of adverse selection loss, but cannot eliminate the fundamental informational cost of price discovery in prediction markets.
- **Computation Complexity:** Solving the implicit invariant equation $F(x, y, L) = 0$ on-chain requires numerical approximations (e.g., Newton-Raphson or piecewise Chebyshev polynomial expansions) to stay within EVM gas limits.

## Implementation status

No implementation in our research stack. The source paper (Moallemi, Robinson, Zhu, July 2026 / AFT 2026) provides theoretical derivations and analytical proofs; no on-chain smart contract or simulation harness has been deployed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]] — Canonical Loss-Versus-Rebalancing foundation in AMMs
- [[quant/crypto-bounded-liquidity-lvr-harmonic-arbitrage-2026-09-01]] — Bounded liquidity LVR under imperfect market liquidity
- [[quant/defi-amm-continuous-installment-options-lvr-delta-hedge-2026-09-01]] — Continuous installment options and LVR delta hedging

## Sources

1. Ciamac C. Moallemi, Dan Robinson, and Brian Zhu, "Uniform-Loss Automated Market Making for Prediction Markets", arXiv:2607.17428v1 [q-fin.TR], July 2026. Accepted to Advances in Financial Technologies (AFT 2026). URL: https://arxiv.org/abs/2607.17428.
