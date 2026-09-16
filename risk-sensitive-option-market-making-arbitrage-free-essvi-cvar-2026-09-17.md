---
schema: strategy-research-record-v1
title: "Risk-Sensitive Option Market Making via Arbitrage-Free eSSVI Volatility Surfaces and Constrained Reinforcement Learning"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - market-making
  - implied-volatility-surface
  - essvi
  - static-no-arbitrage
  - reinforcement-learning
  - constrained-mdp
  - cvar
  - ppo
status: research-only
confidence: medium
source_as_of: 2025-10-06
sources:
  - https://arxiv.org/abs/2510.04569
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Risk-Sensitive Option Market Making via Arbitrage-Free eSSVI Volatility Surfaces and Constrained Reinforcement Learning

## Provenance

- **Primary Academic Source:** Jian'an Zhang (School of Mathematical Sciences, Peking University, `2501111059@stu.pku.edu.cn`), *"Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"*, arXiv preprint `arXiv:2510.04569v1 [q-fin.TR, cs.LG, q-fin.CP, q-fin.MF, q-fin.RM]`, submitted October 6, 2025.
- **Canonical arXiv URL:** https://arxiv.org/abs/2510.04569
- **Full Text HTML:** https://arxiv.org/html/2510.04569v1
- **Digital Object Identifier (DOI):** https://doi.org/10.48550/arXiv.2510.04569
- **Licence:** arXiv.org perpetual non-exclusive license.
- **Repository Deduplication Audit:** A comprehensive audit of all existing `.md` records in `alpha-strategy-research` confirms zero prior citations of `arXiv:2510.04569`, author Jian'an Zhang, or the embedded differentiable extended SSVI (eSSVI) constrained reinforcement learning framework. Prior option-related records in the repository (`option-market-making-hedging-induced-market-impact-2026-09-02.md`, `spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md`, `ad-seq-vol-adaptive-sequential-diffusion-implied-volatility-hedging-2026-09-16.md`, `transformer-ddqn-straddle-option-volatility-trading-2026-09-05.md`) study single-option delta-hedging feedback under transient propagator impact, SVI static RV dispersion falsification, multi-period diffusion surface simulation for SPX tracking hedges, or directional straddle buying. None implement full-surface simultaneous option market making across multiple strike-maturity lattices using an end-to-end differentiable eSSVI layer, softplus butterfly/calendar lattice surrogates, a state-dependent dual Lagrange multiplier, and Rockafellar-Uryasev Conditional Value-at-Risk (CVaR) tail regularizers.

## Economic mechanism

### Source-reported

In option market making, quoting across a full strike-maturity surface requires balancing spread capture (bid-ask half-spread), inventory risk, and adverse selection, while strictly obeying no-arbitrage conditions (butterfly convexity in strike $K$, calendar monotonicity in maturity $T$). Classical heuristics quote independent option contracts or fit static parametric surfaces off-line, which leads to arbitrageable quotes (negative butterfly densities, calendar spreads) or destabilizes during market stress.

The author proposes embedding a fully differentiable extended Stochastic Volatility Inspired (eSSVI) surface layer inside a Constrained Markov Decision Process (CMDP) solved via Proximal Policy Optimization (PPO) with a learnable state-dependent Lagrange multiplier (dual head). The agent controls a 5-dimensional action vector:
1. $\alpha_t \in [\alpha_{\min}, \alpha_{\max}]$: half-spread multiplier trading execution volume for spread capture.
2. $\rho$-shift $\in [-\Delta_\rho, \Delta_\rho]$: surface skew deformation (tilts left/right wings without moving At-The-Money (ATM) implied volatility to first order).
3. $\psi$-scale $\in [1 - \Delta_\psi, 1 + \Delta_\psi]$: surface wing curvature / kurtosis deformation.
4. hedge ratio $\in [0, 1]$: delta-hedging intensity against underlying moves.
5. dual multiplier $\nu_t$: learnable state-dependent Lagrange multiplier enforcing no-arbitrage constraints.

Differentiable softplus penalties enforce butterfly non-negativity ($\mathrm{BF}_m \ge 0$) and calendar monotonicity ($\mathrm{CAL}_m \ge 0$). Differentiable Rockafellar-Uryasev Conditional Value-at-Risk ($\mathrm{CVaR}_{5\%}$) penalizes left-tail execution losses.

### Research interpretation

The economic thesis is that **simultaneous option market making across a multi-strike and multi-maturity book cannot be decoupled from implied volatility surface no-arbitrage geometry. Quoting options independently generates static arbitrage holes that toxic informed flow or arbitrage bots exploit; conversely, rigidly fixing a static volatility surface prevents the market maker from shading skew and wings to shed directional and gamma/vega inventory. Embedding a differentiable eSSVI layer directly into the reinforcement learning loop allows the policy to shade wing quotes dynamically to manage inventory while mathematically guaranteeing no butterfly or calendar arbitrage violations, and shaping left-tail risk through Rockafellar-Uryasev CVaR prevents catastrophic blowout during jump regimes.**

In this hybrid framework:
- **Pricing & Shape Prior:** Differentiable eSSVI parameterization guarantees that quotes across all strikes and maturities adhere to no-arbitrage surfaces, with wing growth strictly bounded by Lee's moment formulas ($\tau_{\max} < 2$).
- **Microstructure Intensity Link:** Counterparty arrival rates follow logistic mispricing intensities where wider spreads reduce fill probabilities while higher quoted prices relative to fair value attract seller flow.
- **Inventory & Risk Control:** Dynamic delta-hedging continuously neutralizes net option delta exposure, while Rockafellar-Uryasev CVaR regularizes episodic downside tail losses.
- **Adaptive Constraint Enforcement:** A state-dependent dual head acts as an implicit dual ascent mechanism, raising penalty weights specifically in states where arbitrage surrogates risk breaching admissibility.

## Signal

### Data Transformation and Surface Parametric State (Source-Reported)

1. **eSSVI Total Variance Formulation:** For maturity $T_m$ and log-moneyness $k = \ln(K / S_t)$, total implied variance $w_m(k) \equiv \sigma_m^2(k) T_m$ is parameterized by:
   $$w_m(k) = \frac{\theta_m}{2} \left[ 1 + \rho_m \phi_m k + \sqrt{(\phi_m k + \rho_m)^2 + (1 - \rho_m^2)} \right]$$
   where $\theta_m > 0$ represents ATM total variance, $\rho_m \in (-1, 1)$ governs skew asymmetry, and $\phi_m > 0$ controls wing curvature.
2. **Reparameterization & Butterfly-Free Condition:**
   Using ATM skew scale $\psi_m \equiv \phi_m \sqrt{\theta_m}$, the classical Gatheral-Jacquier sufficient condition for butterfly-free surfaces is:
   $$\theta_m \phi_m (1 + |\rho_m|) < 4 \iff \psi_m \le \frac{2}{1 + |\rho_m|} - \varepsilon_\psi \equiv \psi_{\max}(\rho_m)$$
   enforced via a smooth squashing function into $[0, \psi_{\max}(\rho_m))$.
3. **Wing Growth Bound (Lee's Moment Constraint):**
   To prevent pathological moment explosion at extreme strikes, the product is capped:
   $$\theta_m \phi_m \le \tau_{\max} < 2$$
   which guarantees $\limsup_{|k| \to \infty} \frac{w_m(k)}{|k|} \le \tau_{\max} < 2$, strictly conforming to Lee's moment formula.
4. **State Vector $s_t \in \mathcal{S}$:**
   $$s_t = \big( f_{\mathrm{price}}(S_t, \text{returns}, \sigma_{\text{realized}}), f_{\mathrm{surf}}(\theta_m, \rho_m, \psi_m), a_{t-1} \big)$$
   where $f_{\mathrm{price}}$ contains underlying price dynamics and realized variance, $f_{\mathrm{surf}}$ tracks current eSSVI parameters, and $a_{t-1}$ records the previous decision.

### Action Space & Policy Parameterization (Source-Reported)

The agent outputs a continuous 5-dimensional raw action $z \in \mathbb{R}^5$ via a two-layer MLP with $\tanh$ activations, mapped to physical controls $a_t = (\alpha_t, \text{hedge}_t, \rho\text{-shift}_t, \psi\text{-scale}_t, \text{dual}_t)$:
- **Half-Spread Control:** $\alpha_t = \alpha_{\min} + (\alpha_{\max} - \alpha_{\min}) \sigma(z_1) \in [\alpha_{\min}, \alpha_{\max}]$.
- **Delta Hedge Intensity:** $\text{hedge}_t = \sigma(z_2) \in [0, 1]$.
- **Skew Tilt ($\rho$-shift):** $\rho\text{-shift}_t = \Delta_\rho \tanh(z_3) \in [-\Delta_\rho, \Delta_\rho]$.
- **Curvature Scale ($\psi$-scale):** $\psi\text{-scale}_t = 1 + \Delta_\psi \tanh(z_4) \in [1 - \Delta_\psi, 1 + \Delta_\psi]$.
- **State-Dependent Dual Multiplier:** $\text{dual}_t = \text{softplus}(z_5) \ge 0$.

### Action-Induced Surface Deformation & Quoting (Source-Reported)

1. **Surface Parameter Update:**
   $$\tilde{\theta}_m = \theta_m, \quad \tilde{\rho}_m = \rho_m + \rho\text{-shift}_t, \quad \tilde{\phi}_m = \phi_m \cdot \psi\text{-scale}_t$$
   followed by the squashing map and wing cap $\tau_{\max}$.
2. **First-Order ATM Invariance:**
   Because $\left.\frac{\partial w_m}{\partial \rho}\right|_{k=0} = 0$ and $\left.\frac{\partial w_m}{\partial \phi}\right|_{k=0} = 0$, deformations in $\rho$ and $\psi$ tilt the wings and skew without altering ATM implied volatility to first order.
3. **Option Quoting:**
   Mid price: $\mathrm{mid}_m(k) = C^{\mathrm{BS}}\big(S_t, K = S_t e^k, T_m, \tilde{\sigma}_m(k)\big)$, where $\tilde{\sigma}_m(k) = \sqrt{\tilde{w}_m(k)/T_m}$.
   Half-spread: $\frac{\mathrm{spread}(m,k)}{2} = \alpha_t S_t \tilde{\sigma}_m(k) \sqrt{T_m} s_0$.
   Quoted ask: $\mathrm{ask}_m(k) = \mathrm{mid}_m(k) + \frac{\mathrm{spread}(m,k)}{2}$.
   Quoted bid: $\mathrm{bid}_m(k) = \mathrm{mid}_m(k) - \frac{\mathrm{spread}(m,k)}{2}$.

### Execution Intensities & Hedging (Source-Reported)

1. **Intensity-Based Fill Dynamics:** For latent fair price $C^\star_m(k)$:
   $$\lambda_{\mathrm{buy}}(m,k) = \lambda_0 w(k) \sigma\left( -\beta (\mathrm{ask}_m(k) - C^\star_m(k)) \right)$$
   $$\lambda_{\mathrm{sell}}(m,k) = \lambda_0 w(k) \sigma\left( -\beta (C^\star_m(k) - \mathrm{bid}_m(k)) \right)$$
   with moneyness weight $w(k) = \exp(-|k|/\kappa)$. Expected fills $v_{\mathrm{buy/sell}} = \lambda_{\mathrm{buy/sell}}$ drive step rewards, while Poisson realizations drive CVaR simulations.
2. **Net Delta & Hedging P&L:**
   $$\Delta_t^{\mathrm{net}} = \sum_{m,k} \big( v_{\mathrm{sell}}(m,k) - v_{\mathrm{buy}}(m,k) \big) \Delta^{\mathrm{BS}}_m(k)$$
   $$\mathrm{PNL}_t^{\mathrm{hedge}} = - \text{hedge}_t \cdot \Delta_t^{\mathrm{net}} \cdot (S_{t+1} - S_t)$$
3. **Quoting P&L:**
   $$\mathrm{PNL}_t^{\mathrm{quote}} = \sum_{m,k} \left[ v_{\mathrm{buy}}(m,k) (\mathrm{ask}_m(k) - C^\star_m(k)) + v_{\mathrm{sell}}(m,k) (C^\star_m(k) - \mathrm{bid}_m(k)) \right]$$

### Smooth Arbitrage Surrogates & Reward Formulation (Source-Reported)

1. **Butterfly Surrogate:**
   $$\mathrm{BF}_m = \frac{1}{|\mathcal{K}'|} \sum_{K \in \mathcal{K}'} \frac{1}{\bar{C}_m} s_\tau\left( - \frac{C_m(K+\Delta K) - 2C_m(K) + C_m(K-\Delta K)}{\Delta K^2} \right)$$
2. **Calendar Surrogate:**
   $$\mathrm{CAL}_m = \frac{1}{|\mathcal{K}|} \sum_{K \in \mathcal{K}} \frac{1}{\bar{C}_{m,m+1}} s_\tau\big( C_m(K) - C_{m+1}(K) \big)$$
   where $s_\tau(x) = \tau \ln(1 + e^{x/\tau})$ is a softplus approximation.
3. **Per-Step Reward:**
   $$r_t = \mathrm{PNL}_t^{\mathrm{raw}} - \lambda_{\mathrm{shape}} \mathrm{Shape}_t - (\lambda_{\mathrm{arb}} + \mathrm{dual}_t) \mathrm{Arb}_t - \lambda_{\mathrm{cvar}} \widehat{\mathrm{CVaR}}_{q,t}^-$$
   where $\mathrm{Shape}_t = \|\Delta \theta\|_2^2 + \|\Delta \rho\|_2^2 + \|\Delta \psi\|_2^2$, $\mathrm{Arb}_t = \sum_m \mathrm{BF}_m + \sum_m \mathrm{CAL}_m$, and $\widehat{\mathrm{CVaR}}_{q,t}^-$ is the Rockafellar-Uryasev smoothed shortfall estimator.

### Operational Strategy Rules (`research-proposed`)

Because the primary paper demonstrates the architecture in a continuous intraday Heston simulation without deploying an exchange gateway, the following operational parameters are `research-proposed`:
- **Execution Timestamp / Decision Interval:** Evaluated every $\Delta t = 30\text{ seconds}$ throughout the continuous trading session (`research-proposed`).
- **Strike-Maturity Lattice Resolution:** 11 log-moneyness buckets $k \in [-0.20, +0.20]$ spaced by $\Delta k = 0.04$, across 3 discrete expiries $T \in \{7, 14, 30\}\text{ days}$ (`research-proposed`).
- **Underlying Delta Hedging:** Executed via perpetual futures / spot market orders whenever $|\Delta_t^{\mathrm{net}}| > 2.0\text{ contracts}$ (`research-proposed`).
- **Inventory Caps & De-risking Gate:** Maximum net delta $|\Delta_t^{\mathrm{net}}| \le 50.0\text{ contracts}$; maximum single-strike net inventory $\le 10.0\text{ contracts}$ (`research-proposed`).
- **Emergency Circuit Breaker:** If rolling intraday drawdown breaches $-3.0\%$ of allocated equity, immediately cancel all quoting limit orders and delta-hedge remaining book to zero (`research-proposed`).

## Required data

- **Underlying Price Stream:** Real-time underlying asset price $S_t$ sampled at 30-second intervals.
- **Option Chain Quotes:** Full option chain bid/ask quotes across available strikes and expiries.
- **Implied Volatility Surface State:** Fitted eSSVI initial parameter set $(\theta_m, \rho_m, \psi_m)$ for active maturities $T_m$.
- **Benchmark / Fair Value Surface:** Midpoint implied volatility reference surface calibrated from top-tier liquidity venues (e.g. Deribit or Cboe).
- **Execution Fills / Microstructure Data:** Real-time trade receipts, passive fill events, and order book depth on quoted option buckets.
- **Point-in-Time Availability:** Surface calibration strictly uses historical and contemporaneous prints; no forward-looking quotes are admitted into the state.
- **Missing-Data Assumptions:** Illiquid strikes with zero trading volume are retained in the eSSVI lattice via parametric interpolation; suspended or halted contracts are excluded from quoting.

## Execution assumptions

- **Source-Reported Settings:**
  - Simulation evaluations utilize 780 decision steps per episode (equivalent to 1 trading day at 30-second steps).
  - Fills follow logistic execution arrival intensities parameterized by spread width and deviation from fair value.
  - Delta hedging is executed synchronously at each decision step with zero fill failure.
- **Research-Proposed Operational Settings:**
  - **Option Quoting Order Type:** Post-only passive limit orders resting at $\mathrm{bid}_m(k)$ and $\mathrm{ask}_m(k)$ (`research-proposed`).
  - **Exchange Fee Model:** Maker rebate/fee of $1.5\text{ bps}$ on options; taker fee of $3.0\text{ bps}$; underlying delta hedge fee of $2.0\text{ bps}$ (`research-proposed`).
  - **Slippage Assumption:** Zero slippage on passive option maker fills; 1 tick slippage ($0.05\%$ of index price) on aggressive delta-hedging market orders (`research-proposed`).
  - **Capital & Margin Requirements:** Portfolio margin requirement modeled under standard exchange margin rules (e.g., Cboe TIMS or Deribit portfolio margin), maintaining minimum $20\%$ cash buffer against adverse gamma shocks (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below are transcribed directly from Jian'an Zhang (arXiv:2510.04569v1, Section 7.1, Section 7.2, Figures 1–2, and Appendix B):

1. **Simulation Configuration (Section 7.1):**
   - 8 intraday episodes evaluated, each consisting of 780 decision steps.
   - Underlying follows stochastic Heston dynamics calibrated to typical SPX intraday variance, with spot-volatility correlation $\rho_{S,v} = -0.5$.
   - Hyperparameter schedule: $\lambda_{\mathrm{shape}}$ annealed from $0 \to 0.5$, $\lambda_{\mathrm{arb}}$ annealed from $0 \to 0.05$, $\lambda_{\mathrm{cvar}} = 0.01$ fixed.
2. **Revenue and Stability (Section 7.2 & Figure 2a):**
   - The agent achieves stable improvement after episode 2, maintaining positive adjusted P&L ($\mathrm{PNL}^{\mathrm{adj}} = \mathrm{PNL}^{\mathrm{raw}} - \text{penalties}$) in **6 of 8 runs**.
   - PPO training stabilizes action exploration variance (`act_std`) and avoids policy collapse.
3. **Static No-Arbitrage Enforcement (Section 7.2 & Figure 2b):**
   - **Calendar violations remain at numerical zero** throughout training.
   - **Butterfly penalties remain at the numerical floor** (dominated by machine precision tolerances).
   - Shape regularization maintains stable values around $10^{-3}$, ensuring a smooth term structure.
4. **Tail Behavior and CVaR Shaping (Section 7.2 & Figure 1a):**
   - Per-step empirical loss distribution displays controlled downside:
     - **$\mathrm{VaR}_{5\%} \approx -1.31$**
     - **$\mathrm{CVaR}_{5\%} \approx -2.16$**
   - Tail thickness remains stable across episodes, verifying the efficacy of the Rockafellar-Uryasev differentiable penalty.
5. **Surface Fidelity (Section 7.2 & Figure 1b):**
   - Quoted and latent true surfaces are virtually indistinguishable across three maturities, confirming in-loop static no-arbitrage consistency without surface distortion.
6. **Behavioral Adaptation (Section 7.2):**
   - Average hedge ratio increases from **$0.41$ to $0.53$** during training.
   - Mean half-spread $\alpha_t$ slightly declines, showing the agent shifts from passive spread-widening to active risk hedging as arbitrage penalties tighten.
7. **Ablation Findings (Section 7.3):**
   - *Without arbitrage penalties:* Raises local arbitrage violations and destabilizes surface smoothness, causing deep wings to diverge.
   - *Without CVaR shaping:* Thickens the left tail of the P&L distribution (substantially heavier drawdowns), despite slightly higher mean raw return.
   - *Without warm-start:* Training from scratch induces severe early instability and large variance in adjusted P&L.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Exogenous Flow Limitation:** In the paper's reported simulation, order flow is modeled exogenously via smooth intensity functions rather than endogenous multi-agent limit order book interactions; queue position priority, tick discreteness, and latency delays are abstracted away.
- **Delta-Only Hedging:** The framework currently penalizes net delta only; higher-order exposures (gamma, vega, vanna, volga) are not explicitly hedged via secondary options, leaving the book exposed to sudden severe volatility spikes or correlation breakdowns.
- **Static vs. Dynamic Arbitrage:** Enforcing butterfly and calendar constraints guarantees static no-arbitrage across space, but does not mathematically eliminate dynamic intertemporal arbitrage across consecutive time steps.
- **Compute Overhead:** Evaluating differentiable Black-Scholes formulas, eSSVI partial derivatives, and Monte Carlo CVaR gradients at every 30-second decision step requires continuous GPU acceleration.

## Falsification plan

1. **Unconstrained Surface Quoting Placebo Test:**
   - Run the market maker policy with $\lambda_{\mathrm{arb}} = 0$ and dual head disabled, allowing unconstrained raw action updates to the volatility surface.
   - *Research-defined falsification threshold:* If the arbitrage-constrained eSSVI model fails to achieve at least a $50\%$ reduction in calendar/butterfly arbitrage violations and a $15\%$ improvement in tail loss ($\mathrm{CVaR}_{5\%}$) over the unconstrained agent in stress simulations, the hypothesis that in-loop eSSVI constraints provide downside protection is falsified.
2. **Adverse Flow & Toxic Selection Stress Test:**
   - Introduce an informed counterparty that trades aggressively against stale quotes whenever mispricing exceeds $0.5 \times \text{spread}$.
   - *Research-defined falsification threshold:* If net session P&L becomes negative across more than $50\%$ of episodes (fewer than 4 of 8 profitable runs), the strategy's spread-setting robustness is falsified.
3. **Transaction Fee & Hedging Drag Test:**
   - Incorporate realistic exchange taker fees ($3.0\text{ bps}$) and $1\text{ tick}$ slippage on all delta-hedging rebalances.
   - *Research-defined falsification threshold:* If net adjusted P&L falls below zero on average across the 8 test episodes due to hedging turnover drag, the operational implementability of the strategy is falsified.
4. **Historical SPX / Crypto Crash Out-of-Sample Test:**
   - Replay the March 2020 COVID shock (SPX) or May 2021 / November 2022 liquidations (Crypto).
   - *Research-defined falsification threshold:* If maximum episodic drawdown exceeds $-10.0\%$ under calibrated jump dynamics, the Rockafellar-Uryasev CVaR tail regularizer is deemed insufficient.

## Crypto portability

**adapted / unproven**

- **Traditional Asset Origin:** The primary source develops and calibrates the framework on S&P 500 (SPX) equity option dynamics within a Heston simulation. The mechanism has not been demonstrated empirically in crypto markets by the authors.
- **Crypto-Specific Operational Differences:**
  - **Deribit / OKX Option Conventions:** Unlike traditional equity options settled in USD, major crypto options on Deribit are inverse and settled in coin (BTC or ETH), introducing non-linear coin margin risk ($S_t \times \text{Payoff}$).
  - **24/7 Continuous Quoting:** Crypto option markets operate 24/7 without market open/close auctions, requiring continuous automated monitoring without overnight halts.
  - **Perpetual Delta Hedging & Funding Rates:** Delta-hedging crypto options is executed primarily via perpetual futures. Holding perpetual hedge positions incurs 8-hour funding rate payments, creating an ongoing carry cost or bonus depending on market positioning.
  - **Wide Wing Spreads & Skew Inversion:** Crypto implied volatility displays much steeper call and put smiles and frequent regime inversions (massive call skew during speculative manias, severe put skew during deleveraging cascades). The eSSVI parameter squashing must be widened to accommodate higher crypto skew without violating wing bounds.

## Limitations

- **Simulation-Only Primary Evidence:** The source results are established in a calibrated Heston stochastic volatility simulator; live exchange deployment has not been executed.
- **Absence of Discrete Queue Dynamics:** The arrival process uses continuous intensities rather than discrete order-book queue queueing, queue jumping, and cancellation dynamics.
- **Delta-Only Hedging:** The policy hedges delta but leaves vega and gamma unhedged, relying solely on CVaR penalties to suppress large open gamma books.
- **Underlying Exogeneity:** The framework does not incorporate permanent or transient market impact on the underlying asset caused by large delta-hedging trades.

## Implementation status

`not-implemented`

No implementation of this differentiable eSSVI constrained RL option market making architecture exists in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader).

## Adoption boundary

`research-only` | `adoption: not-approved` | `approval_scope: research-only`

This record is an upstream research capture. It does not constitute strategy approval, does not authorize live or paper execution, and does not claim verified production alpha.

## Related Wiki records

- `[[quant/option-market-making-hedging-induced-market-impact-2026-09-02]]` — Single-option market making with permanent and transient propagator impact from delta-hedging.
- `[[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md]]` — Falsification of SVI static RV dispersion under adverse selection.
- `[[quant/ad-seq-vol-adaptive-sequential-diffusion-implied-volatility-hedging-2026-09-16]]` — Adaptive sequential diffusion models for implied volatility surface generation and data-driven hedging.
- `[[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]]` — Distributional deep reinforcement learning market maker under regime-switching order flow.

## Sources

- **Primary Academic Paper:** Jian'an Zhang, *"Risk-Sensitive Option Market Making with Arbitrage-Free eSSVI Surfaces: A Constrained RL and Stochastic Control Bridge"*, arXiv preprint `arXiv:2510.04569v1 [q-fin.TR, cs.LG, q-fin.CP, q-fin.MF, q-fin.RM]`, submitted October 6, 2025.
  - Canonical URL: https://arxiv.org/abs/2510.04569
  - Full Text HTML: https://arxiv.org/html/2510.04569v1
  - DOI: https://doi.org/10.48550/arXiv.2510.04569
- **Key Methodological References Cited in Primary Source:**
  - Jim Gatheral and Antoine Jacquier (2014), *"Arbitrage-free SVI volatility surfaces"*, *Quantitative Finance*, 14(1):59–71.
  - Sven Hendriks and Claude Martini (2019), *"The extended SSVI volatility surface"*, *Journal of Computational Finance*, 22(5):25–39.
  - Claude Martini and Andrea Mingone (2022), *"No-arbitrage SVI"*, *SIAM Journal on Financial Mathematics*, 13(1):227–261.
  - Roger W. Lee (2004), *"The moment formula for implied volatility at extreme strikes"*, *Mathematical Finance*, 14(3):469–480.
  - R. Tyrrell Rockafellar and Stanislav Uryasev (2000), *"Optimization of conditional value-at-risk"*, *Journal of Risk*, 2:21–42.
  - John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov (2017), *"Proximal Policy Optimization Algorithms"*, *arXiv preprint arXiv:1707.06347*.
  - Eyal Altman (1999), *"Constrained Markov Decision Processes"*, Chapman and Hall/CRC.
