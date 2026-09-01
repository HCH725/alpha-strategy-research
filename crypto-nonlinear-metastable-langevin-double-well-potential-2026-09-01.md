---
schema: strategy-research-record-v1
title: Cryptocurrency Non-Linear Meta-Stable Langevin Dynamics and Double-Well Potential Regime Detection
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - market-microstructure
  - statistical-physics
  - langevin-equation
  - kramers-moyal
  - non-linear-drift
  - double-well-potential
  - metastable-dynamics
  - instantons
  - uniswap-v3
  - arbitrum
  - regime-detection
status: research-only
confidence: high
source_as_of: 2026-08-24
sources:
  - "Halperin, I. (2026). Non-Linear and Meta-Stable Dynamics in Financial Markets: Evidence from High Frequency Crypto Currency Market Makers. arXiv preprint arXiv:2509.02941v1 [q-fin.ST / physics.comp-ph / q-fin.TR / q-fin.GN]. https://arxiv.org/abs/2509.02941"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cryptocurrency Non-Linear Meta-Stable Langevin Dynamics and Double-Well Potential Regime Detection

## Provenance

- **Primary Source:** Igor Halperin (Fidelity Investments), *"Non-Linear and Meta-Stable Dynamics in Financial Markets: Evidence from High Frequency Crypto Currency Market Makers"*, arXiv preprint `arXiv:2509.02941v1 [q-fin.ST / physics.comp-ph / q-fin.TR]`, published August 24, 2026 (first submitted September 2025). URL: https://arxiv.org/abs/2509.02941, DOI: https://doi.org/10.48550/arXiv.2509.02941.
- **Underlying Theoretical Framework & Software:**
  - Gardiner, C. M. (2004). *Handbook of Stochastic Methods* (3rd ed.). Springer.
  - Gorjão, L. R., & Meirinhos, F. (2019). "kramersmoyal: Kramers–Moyal Coefficients for Stochastic Processes." *Journal of Open Source Software* / arXiv preprint `arXiv:1912.09737`. Repository: https://github.com/LRydin/KramersMoyal.
  - Halperin, I., & Dixon, M. F. (2020). "Quantum Equilibrium-Disequilibrium: Asset Price Dynamics, Symmetry Breaking, and Defaults as Dissipative Instantons." *Physica A: Statistical Mechanics and its Applications*, 537, 122187.
  - Halperin, I. (2020). "The Inverted World of Classical Quantitative Finance: a Non-Equilibrium and Non-Perturbative Finance Perspective." arXiv preprint `arXiv:2008.03623`.
  - Halperin, I. (2022). "Non-Equilibrium Skewness, Market Crises, and Option Pricing: Non-Linear Langevin Model of Markets with Supersymmetry." *Physica A*, 594, 127065.
  - Halperin, I., & Itkin, A. (2025). "Marketron games: Self-propelling stocks vs dumb money and metastable dynamics of the Good, Bad and Ugly markets." arXiv preprint `arXiv:2501.12676`.
  - Adams, H., Zinsmeister, N., Salem, M., Keefer, R., & Robinson, D. (2021). "Uniswap v3 Core." Uniswap Labs.
- **Empirical Dataset:** High-frequency transaction and liquidity data from liquid Uniswap v3 pools on the Arbitrum Layer-2 network:
  1. USDC-WETH pool (01-01-2024 to 12-31-2024, ~300,000 transaction records);
  2. USDC-WETH pool (01-01-2025 to 06-30-2025);
  3. WBTC-WETH pool (01-01-2024 to 12-31-2024).
- **Public-Use Status:** Open-access academic publication / arXiv preprint distributed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

## Economic mechanism

### Source-reported

Conventional quantitative finance models (e.g., Geometric Brownian Motion, Ornstein-Uhlenbeck processes, Black-Scholes) assume linear diffusion drifts $\mu(x) = -k(x - x_0)$, which mathematically correspond to a simple harmonic (quadratic) potential $U(x) = \frac{1}{2} k (x - x_0)^2$ where the drift force is the negative gradient $\mu(x) = -\partial U(x) / \partial x$.

Halperin (2026) demonstrates from first principles of money flows, concentrated liquidity profiles, and high-frequency market microstructure that the effective drift function governing asset log-prices $x_t = \ln P_t$ exhibits higher-order (cubic and higher) non-linearities, resulting in non-quadratic self-interaction potential landscapes $U(x) = -\int \mu(x') dx'$:

1. **Langevin Representation of Market Microstructure:**
   The asset log-price evolves according to the non-linear Langevin stochastic differential equation:
   $$\dot{x}(t) = \mu(x) + \sigma(x) \xi_t \quad \Longleftrightarrow \quad dx_t = \mu(x_t) dt + \sigma(x_t) dW_t$$
   where $\mu(x) = -\frac{\partial U(x)}{\partial x}$ represents the state-dependent deterministic force pulling prices toward equilibrium states, $\sigma(x)$ is state-dependent diffusion, and $\xi_t$ is Gaussian white noise ($\langle \xi_t \xi_{t'} \rangle = \delta(t - t')$).

2. **Topological Regimes of the Potential Landscape:**
   - **Single-Well Potential (Stable Equilibrium):** Characterized by a single global minimum $x^* = \arg\min U(x)$ where $\mu(x^*) = 0$ and $U''(x^*) > 0$. Indicates a resilient market state with strong mean-reverting forces anchoring prices to a single fair-value consensus.
   - **Double-Well Potential (Metastable Stress Regime):** Characterized by two competing local minima ($x_1^*, x_2^*$) separated by a potential barrier at $x_b$ ($U'(x_b) = 0, U''(x_b) < 0$). Indicates a metastable market regime where two competing price equilibria co-exist, signaling heightened market uncertainty, structural disagreement among liquidity providers, or regime transition stress.

3. **Metastability and Instanton Jumps:**
   When the potential possesses a double-well topology, thermal fluctuations (order flow noise) allow the price "particle" to reside in a metastable local minimum for extended periods before undergoing a rapid, near-instantaneous escape transition ("instanton") across the potential barrier into the deeper global minimum. This generates endogenous jump dynamics and volatility bursts without requiring exogenous jump processes.

4. **Multi-Scale Horizon Dependence:**
   Non-linearities are pronounced at high sampling frequencies ($< 1\text{ hour}$, e.g. 10 minutes to 6 hours across 2-month rolling windows). At low sampling frequencies ($> 1\text{ day}$) or very short observation windows ($\le 1\text{ month}$ due to tail data sparsity), the estimated potential collapses into an apparent single well.

### Research interpretation

The alpha hypothesis is **Non-Linear Potential Well Detection and Metastable Instanton Anticipation**:

1. **State-Dependent Mean Reversion vs. Breakout Filtering:**
   - In a **Single-Well Regime** ($U(x)$ has a unique minimum), trade mean reversion toward $x^* = \arg\min U(x)$, sizing positions proportionally to the restoring drift force $|\mu(x_t)| = |\partial U / \partial x|$.
   - In a **Double-Well Regime** ($U(x)$ has two minima separated by barrier $x_b$), mean reversion is hazardous if the price is near the barrier. As $x_t$ approaches $x_b$, the restoring force weakens to zero ($\mu(x_b) = 0$), and crossing $x_b$ triggers an instanton acceleration toward the opposite well $x_2^*$. The strategy switches from mean-reversion to an instanton breakout / trend-following mode.

2. **Market Making Spread and Skew Modulation:**
   - Automated market makers quoting on concentrated liquidity pools (Uniswap v3) or high-frequency order books can dynamically modulate bid-ask spreads: widen spreads when $U(x)$ enters a double-well configuration (reflecting barrier crossing risk), and skew quotes toward the deeper potential minimum where terminal drift is directed.

## Signal

The normalized signal and regime-detection engine operate as follows:

1. **Data Pre-processing & Subsampling:**
   - Construct smoothed log-price series $x_t = \ln P_t$, averaged over 15 consecutive transaction prints ($\Delta t \approx 100\text{ s}$) to filter microstructure bounce.
   - Trim extreme 0.5% upper and 0.5% lower outliers over rolling lookback window $W = 60\text{ days}$ (2 months).

2. **Non-Parametric Kramers-Moyal Expansion:**
   - For subsampling lag $\tau \in \{10\text{m}, 30\text{m}, 1\text{h}, 2\text{h}, 6\text{h}\}$, estimate the first two Kramers-Moyal conditional moment coefficients using Epanechnikov or Gaussian kernel density estimation:
     $$K_1(x) = \lim_{\tau \to 0} \frac{1}{\tau} \mathbb{E}[x_{t+\tau} - x_t \mid x_t = x]$$
     $$K_2(x) = \lim_{\tau \to 0} \frac{1}{\tau} \mathbb{E}[(x_{t+\tau} - x_t)^2 \mid x_t = x]$$
   - Physical drift rate: $\mu(x) = \frac{K_1(x)}{\Delta t}$.
   - Physical diffusion rate: $\sigma^2(x) = \frac{K_2(x)}{\Delta t}$.

3. **Potential Reconstruction:**
   - Numerically integrate the estimated physical drift function:
     $$U(x) = -\int_{x_{\min}}^x \mu(x') dx'$$
   - Normalize $U(x)$ such that $\min_{x} U(x) = 0$.

4. **Topology Classification & Barrier Extraction:**
   - Identify critical points $\{x_k\}$ where $\mu(x_k) = 0$.
   - Calculate second derivative $U''(x_k) = -\mu'(x_k)$.
   - Classify topology:
     - **Regime 1 (Single-Well):** Exactly 1 critical point $x^*$ with $U''(x^*) > 0$.
     - **Regime 2 (Double-Well / Metastable):** 3 critical points $x_1^* < x_b < x_2^*$, where $x_1^*, x_2^*$ are minima ($U'' > 0$) and $x_b$ is the potential barrier ($U''(x_b) < 0$).
   - Compute barrier height: $\Delta U_1 = U(x_b) - U(x_1^*)$ and $\Delta U_2 = U(x_b) - U(x_2^*)$.

5. **Trading Execution Rules:**
   - **Case A: Single-Well State:**
     - Long Signal: $x_t < x^* - k \cdot \sigma(x_t)$, targeting exit at $x^*$.
     - Short Signal: $x_t > x^* + k \cdot \sigma(x_t)$, targeting exit at $x^*$.
   - **Case B: Double-Well State (Metastable Instanton Mode):**
     - If $x_t \in [x_1^*, x_b]$ and $|x_t - x_b| < \epsilon_{\text{threshold}}$ with positive momentum ($\dot{x}_t > 0$):
       - Enter **Long Instanton Breakout** targeting $x_2^*$.
       - Set strict stop-loss at $x_b - \delta_{\text{stop}}$.
     - If $x_t \in [x_b, x_2^*]$ and $|x_t - x_b| < \epsilon_{\text{threshold}}$ with negative momentum ($\dot{x}_t < 0$):
       - Enter **Short Instanton Breakout** targeting $x_1^*$.
       - Set strict stop-loss at $x_b + \delta_{\text{stop}}$.

## Required data

- **Venue & Instruments:** Decentralized AMM pools (Uniswap v3 Arbitrum USDC-WETH 0.05%, WBTC-WETH 0.05%) and centralized high-frequency spot/perpetuals (Binance BTCUSDT/ETHUSDT, Hyperliquid).
- **Timeframe:** High-frequency transaction logs, resampled/smoothed at $\Delta t \approx 100\text{ s}$; multi-scale lag evaluation from $10\text{ minutes}$ to $6\text{ hours}$.
- **Lookback Window:** Rolling 60-day (2-month) estimation buffer for stable Kramers-Moyal kernel integration.
- **Fields:** Timestamp (millisecond UTC), swap execution price ($P_t$), volume, liquidity ticks.
- **Point-in-time Alignment:** Strictly causal rolling windows; estimation of $\mu(x)$ and $U(x)$ computed exclusively on $[t - W, t]$ data.

## Execution assumptions

- **Order Types:** Limit orders when executing mean-reversion around stable potential wells; aggressive market/IOC orders when executing instanton breakout crossing the potential barrier $x_b$.
- **Latency & Sampling Delay:** Execution occurs on the subsequent 100-second tick after signal evaluation.
- **Transaction Costs:** Arbitrum Layer-2 swap fee (5 bps for Uniswap v3 pool + ~$0.05 gas) or CEX perpetual taker fee (2–4 bps).
- **Slippage & Market Impact:** Modeled via state-dependent liquidity depth around tick price $x_t$.

## Evidence

### Source-reported

Halperin (2026) provides empirical evidence from Uniswap v3 Arbitrum data:
- **USDC-WETH 2024 Dataset (~300k transactions):** Strong non-linear drift $\mu(x)$ observed across 2-month rolling windows. For time scales between 10 minutes and 6 hours, the derived potential $U(x)$ exhibits a pronounced double-well potential in 2 out of 3 representative 2-month test windows.
- **USDC-WETH 2025 Dataset (Jan–Jun 2025):** Confirms non-quadratic potentials with wide basins and local minima to the right of stable global equilibria at intraday frequencies ($< 1\text{ h}$).
- **WBTC-WETH 2024 Dataset (Crypto-Cross Pair):** Displays single-well (yet distinctly non-harmonic/non-quadratic) potentials across all analyzed windows, reflecting the absence of a stable fiat peg anchor.
- **Window Length Sensitivity:** 1-month and shorter windows collapse into single-well profiles due to sample sparsity in the distribution tails, validating the necessity of $\ge 2$-month lookbacks for non-parametric barrier resolution.
- **Drift Stochasticity:** Tests show fast stochastic components ($\eta_s$) self-average within hours/days, while slow-varying macro components ($\eta_l$) govern the smooth migration between single-well and double-well regimes over multi-week horizons.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Lookback Latency Lag:** Because a 2-month window is required for tail density estimation, rapid intraday structural breaks may take time to reflect in the non-parametric potential $U(x)$, leading to temporary barrier mislocalization.
- **Bandwidth Sensitivity:** Non-parametric Kramers-Moyal estimation is sensitive to kernel bandwidth selection; oversmoothing erases shallow double wells, while undersmoothing creates spurious artificial local minima.
- **Cross-Pair Variation:** The double-well phenomenon is prominent in stablecoin-anchored pairs (USDC-WETH) but weaker or absent in relative crypto-cross pairs (WBTC-WETH), indicating asset-class and numeraire dependency.

## Falsification plan

The hypothesis that non-linear potential estimation generates tradable alpha will be falsified if:
1. **Regime Identification Null Result:** An out-of-sample backtest over 2024–2026 shows that trading mean-reversion in single-well regimes yields an annualized Sharpe ratio $< 0.50$ after deducting 3 bps transaction costs.
2. **Instanton Jump Failure:** Post-barrier breakout trades across $x_b$ fail to achieve a positive drift within the subsequent 24 hours in $> 50\%$ of double-well occurrences.
3. **Placebo Permutation Test:** Shuffling the temporal sequence of log-return increments generates identical pseudo-potential barriers and critical points, demonstrating that the observed double wells are statistical artifacts of marginal distributions rather than dynamical drift features.
4. **Parametric Linear Benchmark Superiority:** A standard linear Ornstein-Uhlenbeck mean-reversion model outperforms the Kramers-Moyal potential model in risk-adjusted net return across all out-of-sample test splits.

## Crypto portability

**Direct**: The underlying empirical study was conducted directly on cryptocurrency markets (Uniswap v3 pools on Arbitrum L2, analyzing USDC-WETH and WBTC-WETH).

Portability considerations:
- Direct applicability to EVM DEX pools (Uniswap v3, Uniswap v4, Camelot, Curve) and high-frequency centralized perpetual order books (Binance, Bybit, Hyperliquid).
- Numeraire selection is critical: stablecoin-quoted pairs (USDC, USDT) exhibit clear potential wells due to dollar valuation anchoring, whereas crypto-cross pairs (WBTC-WETH) exhibit broader relative-valuation dynamics.

## Limitations

- **not independently reproduced**;
- **lookback data requirement:** requires $\ge 60\text{ days}$ of granular transaction data to avoid tail estimation collapse;
- **computational overhead:** non-parametric kernel density and numerical integration require continuous calculation across rolling windows;
- **execution frictions:** on-chain gas spikes during high-volatility instanton transitions can diminish net breakout alpha.

## Implementation status

not-implemented

No implementation in PyBroker, NautilusTrader, or internal live trading pipelines has been completed.

## Adoption boundary

research-only

This record is research material only. It does not constitute investment advice, a validated trading strategy, or authorization for Paper, Testnet, or Live execution.

## Related Wiki records

- [[quant/crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31]] — AMM liquidity dynamics and adverse selection.
- [[quant/crypto-microstructure-complexity-measures-wash-trading-filter-2026-09-01]] — high-frequency crypto microstructure complexity.
- [[quant/crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]] — microstructure price impact and order flow.

## Sources

1. Halperin, I. (2026). "Non-Linear and Meta-Stable Dynamics in Financial Markets: Evidence from High Frequency Crypto Currency Market Makers." *arXiv preprint arXiv:2509.02941v1 [q-fin.ST / physics.comp-ph / q-fin.TR / q-fin.GN]*, published 24 August 2026. URL: https://arxiv.org/abs/2509.02941. DOI: https://doi.org/10.48550/arXiv.2509.02941.
2. Gorjão, L. R., & Meirinhos, F. (2019). "kramersmoyal: Kramers–Moyal Coefficients for Stochastic Processes." *Journal of Open Source Software*, 4(44), 1693 / *arXiv preprint arXiv:1912.09737*. URL: https://arxiv.org/abs/1912.09737.
3. Gardiner, C. M. (2004). *Handbook of Stochastic Methods for Physics, Chemistry and the Natural Sciences* (3rd ed.). Springer Series in Synergetics, Vol. 13. Springer-Verlag Berlin Heidelberg.
4. Halperin, I., & Dixon, M. F. (2020). "Quantum Equilibrium-Disequilibrium: Asset Price Dynamics, Symmetry Breaking, and Defaults as Dissipative Instantons." *Physica A: Statistical Mechanics and its Applications*, 537, 122187. DOI: https://doi.org/10.1016/j.physa.2019.122187.
5. Adams, H., Zinsmeister, N., Salem, M., Keefer, R., & Robinson, D. (2021). "Uniswap v3 Core." Technical Whitepaper, Uniswap Labs. URL: https://uniswap.org/whitepaper-v3.pdf.
