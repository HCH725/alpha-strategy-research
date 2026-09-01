---
schema: strategy-research-record-v1
title: AMM Loss-versus-Rebalancing Decomposition and Optimal Block Time under Jump-Diffusion Prices
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - cpmm
  - lvr
  - loss-versus-rebalancing
  - jump-diffusion
  - mev
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-08
sources:
  - "Nils Bundi, 'Optimal Block Time for AMM Liquidity Providers under Jump-Diffusion Prices', arXiv:2608.30321v1 [q-fin.MF, q-fin.CP], August 2026. DOI: 10.48550/arXiv.2608.30321. https://arxiv.org/abs/2608.30321"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AMM Loss-versus-Rebalancing Decomposition and Optimal Block Time under Jump-Diffusion Prices

## Provenance

- **Primary Source:** Nils Bundi (ETH Zurich / Quantitative Finance), "Optimal Block Time for AMM Liquidity Providers under Jump-Diffusion Prices", arXiv:2608.30321v1 [q-fin.MF, q-fin.CP], August 31, 2026. DOI: [10.48550/arXiv.30321](https://doi.org/10.48550/arXiv.2608.30321). Full text: [https://arxiv.org/html/2608.30321v1](https://arxiv.org/html/2608.30321v1). Accepted at MARBLE 2026 (Lecture Notes in Operations Research, Springer Nature).
- **Empirical Calibration Dataset:** Binance ETH/USDT 5-minute trade closes spanning January 2020 through June 2026 (2,373 trading days). Continuous diffusion volatility $\sigma$ estimated via bipower variation; jump intensity $\lambda$ and jump size standard deviation $\delta$ extracted via the non-parametric Lee-Mykland jump-detection test at the 1% significance level.

## Economic mechanism

### Source-reported

1. **Diffusion vs. Jump LVR Dichotomy:** Loss-versus-Rebalancing (LVR) measures the adverse selection cost incurred by Automated Market Maker (AMM) liquidity providers (LPs) when external reference prices move faster than pool quotes. Under pure Geometric Brownian Motion (GBM), LVR vanishes as block time $\Delta t \to 0$, providing the primary theoretical justification for sub-second block times. However, cryptocurrency markets exhibit frequent discontinuous price jumps (e.g., liquidations, CEX order flow shocks).
2. **Irreducible Jump Floor:** When reference prices follow a Merton jump-diffusion process, LVR decomposes into two distinct channels:
   - A **diffusion channel** that scales as $\mathcal{O}(\sqrt{\Delta t})$ and decays toward zero as blocks become faster.
   - A **jump channel** that is strictly positive and **invariant to block time** ($\Delta t$). Discontinuous price jumps immediately breach the AMM fee band $[-\gamma, \gamma]$, allowing arbitrageurs to extract concavity rent regardless of block frequency.
3. **The Planner's Block-Time Optimum:** Shorter blocks impose non-zero consensus costs (block gossip, BLS signature aggregation, validator state bloat) scaling as $c / \Delta t$. Balancing marginal diffusion LVR reduction against per-block consensus costs yields an explicit, unique social planner optimal block time $\Delta t^{\mathrm{opt}}$.

### Research interpretation

The falsifiable thesis is an **AMM adverse selection decomposition and liquidity provisioning regime mechanism**:
1. **Sub-Second Block Time Diminishing Returns:** For AMM LPs on high-speed chains (e.g., Solana, Arbitrum, Monad, MegaETH), lowering block time below ~250ms yields negligible marginal LVR reduction because the residual adverse selection is dominated by the jump floor (>60% of total LVR).
2. **Fee Tier & Architecture as Primary Levers:** Because block time cannot mitigate jump LVR, LP profitability in jump-dominated regimes depends entirely on fee-tier scaling ($\gamma / \delta$), continuous batch auctions (eliminating block-boundary arbitrage), or LVR-rebate mechanisms (e.g., dynamic MEV taxes / Dutch auctions), rather than infrastructure speed alone.

## Signal

### 1. Jump-Diffusion Reference Price & Constant-Product Pool Model

- **Price Process ($S_t$):** Follows a Merton jump-diffusion model under measure $\mathbb{P}$:
  $$\frac{dS_t}{S_{t-}} = \mu dt + \sigma dW_t + (e^J - 1) dN_t$$
  where $N_t$ is a Poisson process with intensity $\lambda$, and jump sizes $J \sim \mathcal{N}(m, \delta^2)$ with $m = 0$.
- **Constant Product Market Maker (CPMM):** Reserves $(x_t, y_t)$ satisfy $x_t y_t = L$. Pool value function $V(S) = 2\sqrt{LS}$. Proportional swap fee is $\gamma \in (0, 1)$ in log-price units.

### 2. Instantaneous LVR Rate Decomposition Formula

The total annualized instantaneous LVR rate $\ell(\Delta t)$ decomposes into:
$$\ell(\Delta t) = \ell_{\mathrm{diff}}(\Delta t) + J_{\mathrm{LVR}}$$

#### A. Diffusion LVR Component
$$\ell_{\mathrm{diff}}(\Delta t) = \frac{\sigma^2 V}{8} F(\kappa(\Delta t))$$
where $\kappa(\Delta t) = \frac{\gamma}{\sigma \sqrt{\Delta t}}$ is the dimensionless fee-to-volatility ratio per block, and the fee attenuation factor is:
$$F(\kappa) = \frac{1}{(1 + \sqrt{2}\kappa)^2}$$

#### B. Invariant Jump Floor Component
$$J_{\mathrm{LVR}} = \lambda V \cdot G(\gamma; m, \delta^2) = \lambda V \cdot \delta^2 \Psi\left(\frac{\gamma}{\delta}\right)$$
where the jump loss function $\Psi(u)$ for symmetric normal jumps ($u = \gamma/\delta$) is:
$$\Psi(u) = (1 + u^2) \Phi(-u) - u \phi(u) + \frac{1}{2} e^{2 u^2} \Phi(-2 u)$$
with standard normal CDF $\Phi(\cdot)$ and PDF $\phi(\cdot)$.

### 3. Optimal Block Time Equation

The social planner minimizes total cost per unit time $W(\Delta t) = \ell_0(\Delta t) + \frac{c}{\Delta t}$, where $c = r \cdot \frac{V}{V_{\mathrm{chain}}}$ is the per-pool validator consensus cost.

The exact optimum solves the cubic in $\eta^{\mathrm{opt}} = \sqrt{2} \kappa(\Delta t^{\mathrm{opt}})$:
$$\eta^{\mathrm{opt}} (1 + \eta^{\mathrm{opt}})^2 = \frac{V \gamma^2}{8 c}$$
$$\Delta t^{\mathrm{opt}} = \frac{2 \gamma^2}{\sigma^2 (\eta^{\mathrm{opt}})^2}$$

## Required data

- **Reference Market Data:** High-frequency (1-second to 5-minute) CEX spot trades and order book mid-prices (Binance ETH/USDT, BTC/USDT).
- **On-Chain AMM Data:** DEX pool state snapshots (Uniswap v2/v3 reserves, tick liquidity, swap fee tier $\gamma$, TVL $V$).
- **Consensus & Network Data:** Block production interval $\Delta t$, validator issuance rate $r$, staking market cap $V_{\mathrm{chain}}$.
- **Statistical Estimators:**
  - Bipower variation estimator for continuous diffusion volatility $\sigma$: $\mathrm{BV}_t = \frac{\pi}{2} \sum_{i=2}^M |r_{t,i}| |r_{t,i-1}|$.
  - Lee-Mykland jump detection statistic $\mathcal{L}_{t,i} = \frac{|r_{t,i}|}{\hat{\sigma}_{t,i}}$ evaluated at test threshold $S_M = -\ln(-\ln(0.99))$.

## Execution assumptions

- **Arbitrage Execution:** Risk-neutral, capital-unconstrained arbitrageurs observe external reference price $S_t$ continuously and trade at discrete block arrival times $\tau_i = i \cdot \Delta t$.
- **Arbitrage Trigger:** Trade executed at block $\tau_i$ if and only if absolute log mispricing $|z_{\tau_i}| = |\ln(S_{\tau_i} / P_{\tau_i})| > \gamma$.
- **Pool Type:** Full-range Constant-Product Market Maker (CPMM) with TVL $V = \$1,000,000$.
- **Consensus Cost Allocation:** Pro-rata attribution based on TVL share $V / V_{\mathrm{chain}} = 4.8 \times 10^{-6}$.

## Evidence

### Source-reported

All figures below are directly reported by Nils Bundi (arXiv:2608.30321v1, August 2026) calibrated on Binance ETH/USDT 5-minute data (Jan 2020 – Jun 2026, 2,373 days) and Ethereum network parameters:

#### 1. Baseline Calibrated Parameters (Table 1)

- Diffusion volatility: $\sigma = 0.8156$ ($81.56\%/\text{year}$)
- Jump intensity: $\lambda = 283.3/\text{year}$ (~0.78 jumps/day)
- Mean log jump: $m = 0$ (sample $\hat{m} = -0.0012$, 99% CI $[-0.0026, +0.0003]$ contains zero)
- Jump size std: $\delta = 0.0192$ ($1.92\%$)
- AMM swap fee: $\gamma = 0.0005$ ($5\text{ bps}$)
- Pool TVL: $V = \$1,000,000\text{ USD}$
- Validator consensus cost: $c = \$260 \times 10^{-5}\text{ USD/block}$ pro-rata

#### 2. Chain-by-Chain LVR Rate & Diffusion Share (Table 2)

| Chain / Infrastructure | Block Time ($\Delta t$) | Total LVR Rate $\ell$ (bp/year) | Diffusion Share (%) | Jump Floor Share (%) |
| :--- | :--- | :--- | :--- | :--- |
| **Ethereum L1** | 12 s | 471 bp/yr | 73% | 27% |
| **Base / Optimism L2** | 2 s | 312 bp/yr | 60% | 40% |
| **Solana** | 400 ms | 221 bp/yr | 43% | 57% |
| **Arbitrum** | 250 ms | 203 bp/yr | 38% | 62% |
| **High-Speed App-Chain** | 50 ms | 162 bp/yr | 23% | 77% |
| **Asymptotic Limit ($\Delta t \to 0$)** | 0 ms | **125 bp/yr** | **0%** | **100%** |

#### 3. Regime Sensitivity Analysis at Ethereum 12s Block Time (Table 3)

| Regime ($\sigma \backslash \lambda$) | $\lambda = 71/\text{yr}$ (Low Jump) | $\lambda = 283/\text{yr}$ (Baseline) | $\lambda = 1,133/\text{yr}$ (Elevated) | $\lambda = 4,533/\text{yr}$ (Extreme Crisis) |
| :--- | :--- | :--- | :--- | :--- |
| **$\sigma = 0.30$ (Calm)** | 55 bp (43% diff) | 148 bp (16% diff) | 524 bp (4% diff) | 2,027 bp (1% diff) |
| **$\sigma = 0.816$ (Baseline)** | 377 bp (92% diff) | **471 bp (73% diff)** | 847 bp (41% diff) | 2,350 bp (15% diff) |
| **$\sigma = 1.50$ (High Vol)** | 1,107 bp (97% diff) | 1,201 bp (90% diff) | 1,577 bp (68% diff) | 3,079 bp (35% diff) |

#### 4. Social Planner Optimum Solution

- For baseline parameters ($A = \frac{V \gamma^2}{8 c} = 12.02$):
  - Optimal dimensionless parameter: $\eta^{\mathrm{opt}} = 1.677$
  - **Optimal block time:** $\Delta t^{\mathrm{opt}} \approx 1.05\text{ seconds}$
  - Total welfare loss at optimum: $W(\Delta t^{\mathrm{opt}}) = 398\text{ bp/year}$ (compared to $661\text{ bp/year}$ at 12s when including consensus costs).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Failure of the Sub-Second Block Speed Panacea:** The standard narrative that reducing block time to zero eliminates AMM LVR is disproven under jump-diffusion dynamics. On a 50ms app-chain, 77% of remaining LVR is invariant jump loss ($125\text{ bp/yr}$ out of $162\text{ bp/yr}$).
- **Severe Jump-Regime Ineffectiveness:** During market stress with elevated jump arrivals ($\lambda = 4,533/\text{yr}$), diffusion LVR accounts for only 1% to 15% of total losses, rendering block-time optimization virtually powerless to protect LPs.
- **Fee Ineffectiveness on Tail Jumps:** Standard proportional fees recover only the fraction $1 - \Psi(\gamma/\delta)$ of jump LVR; for $\gamma = 5\text{ bps}$ and $\delta = 1.92\%$, the fee absorbs less than $3\%$ of the jump concavity loss.

## Falsification plan

1. **Empirical Jump LVR Invariance Test:** Measure LVR on Uniswap v3 full-range pools across Ethereum L1 (12s), Arbitrum (250ms), and Base (2s). Filter realized swap events into diffusion vs. jump intervals using high-frequency Binance trades. If jump-window LVR decreases with faster block time rather than remaining invariant, falsify the jump floor decomposition theorem.
2. **Fee-to-Jump Ratio Perturbation ($\gamma / \delta$):** Compare LVR on 5 bps vs 30 bps vs 100 bps pools during high-jump regimes. If the ratio of empirical jump LVR matches $\Psi(\gamma_1/\delta) / \Psi(\gamma_2/\delta)$ within a 15% tolerance band, confirm the analytical jump loss formula.
3. **Block-Time LVR Scaling Test:** Fit empirical diffusion LVR against $\kappa(\Delta t)^{-2}$ across multiple L2s. If diffusion LVR fails to scale as $\mathcal{O}(\sqrt{\Delta t})$, reject the continuous-time Markovian thinning model.
4. **App-Chain Batch Auction Comparison:** Deploy a frequent batch auction AMM (e.g. CoW AMM / Diamond) alongside a continuous CPMM on a 50ms chain. If batch auctions do not reduce total LVR below the $125\text{ bp/yr}$ jump floor, reject the hypothesis that batching eliminates discrete jump arbitrage.

## Crypto portability

`direct`

The theory, empirical calibration, and policy implications are formulated directly for decentralized automated market makers (Uniswap, Sushiswap, Curve) and Layer 1/Layer 2 blockchain consensus architectures:
- **Concentrated Liquidity (Uniswap v3):** For concentrated liquidity positions within range $[P_a, P_b]$, LVR scales by the leverage factor $\frac{1}{1 - \sqrt{P_a/P_b}}$, which amplifies both diffusion and jump LVR proportionally while leaving the relative jump share invariant.
- **Dynamic Fee Pools & Hooks (Uniswap v4):** Volatility-triggered dynamic fee hooks can temporarily expand $\gamma$ during detected jump events, mitigating the jump floor without permanently penalizing normal retail swaps.
- **Cross-Chain / Rollup MEV Extraction:** Arbitrageurs utilize private builder bundles (Flashbots, MEV-Boost) and searcher infrastructure to atomically extract jump LVR at the exact block boundary.

## Limitations

- **Not independently reproduced.**
- **Full-Range Liquidity Assumption:** Analytical decomposition is derived in closed form for full-range CPMM ($x y = L$); concentrated liquidity truncation introduces boundary edge effects during large jumps.
- **Uncorrelated Jump & Diffusion:** Assumes Poisson jump arrivals are independent of the Brownian motion increments, ignoring jump clustering / self-excitation (Hawkes dynamics).
- **Consensus Cost Proxy:** Uses native-token issuance as a proxy for network consensus cost $c$, which includes economic security subsidies beyond pure hardware/bandwidth resource costs.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation.

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for live trading.

## Related Wiki records

- `[[quant/defi-amm-continuous-installment-options-lvr-delta-hedge-2026-09-01]]`
- `[[quant/crypto-dynamic-weight-amm-tfmm-dutch-reverse-auction-rebalancing-2026-09-01]]`
- `[[quant/dex-cyclic-arbitrage-constant-product-amm-2026-09-01]]`
- `[[quant/crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01]]`

## Sources

1. Nils Bundi, "Optimal Block Time for AMM Liquidity Providers under Jump-Diffusion Prices", arXiv:2608.30321v1 [q-fin.MF, q-fin.CP], August 31, 2026. DOI: [10.48550/arXiv.2608.30321](https://doi.org/10.48550/arXiv.2608.30321). https://arxiv.org/abs/2608.30321.
2. Full article text, proofs, and tables: https://arxiv.org/html/2608.30321v1.
3. Milionis, J., Moallemi, C. C., Roughgarden, T., & Zhang, A. L. (2022). "Automated Market Making and Loss-Versus-Rebalancing." *arXiv preprint arXiv:2208.06046*.
4. Lee, S. S., & Mykland, P. A. (2008). "Jumps in financial markets: A new nonparametric test and jump dynamics." *The Review of Financial Studies*, 21(6), 2535–2563.
