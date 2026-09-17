---
schema: strategy-research-record-v1
title: "Portfolio Representation Switching Frictions, Residence-Scale Heterogeneity, and Long-Memory Order Flow: First-Passage Renewal Aggregation and Execution-Weight Invariance"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - order-flow-dynamics
  - long-memory
  - first-passage-renewal
  - switching-frictions
  - execution-cost-models
  - institutional-flow
status: research-only
confidence: high
source_as_of: 2026-09-17
sources:
  - "Alejandro Rodríguez Domínguez, 'Switching Frictions, Heterogeneous Trading Horizons, and Long-Memory Order Flow', arXiv preprint arXiv:2609.02525v1 [q-fin.PM], submitted September 2, 2026. https://arxiv.org/abs/2609.02525"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Portfolio Representation Switching Frictions, Residence-Scale Heterogeneity, and Long-Memory Order Flow: First-Passage Renewal Aggregation and Execution-Weight Invariance

## Provenance

- **Primary Academic Source:** Alejandro Rodríguez Domínguez (Quantitative Analysis and Artificial Intelligence Department, Miralta Finance Bank S.A., Madrid, Spain, `arodriguez@miraltabank.com`; Department of Computer Science, University of Reading, Reading, UK; Department of Data and AI, Albert School, Paris, France), *"Switching Frictions, Heterogeneous Trading Horizons, and Long-Memory Order Flow"*, arXiv preprint `arXiv:2609.02525v1 [q-fin.PM]`, submitted September 2, 2026.
- **Canonical arXiv URL:** https://arxiv.org/abs/2609.02525
- **Canonical Full-Text HTML:** https://arxiv.org/html/2609.02525v1
- **Canonical Full-Text PDF:** https://arxiv.org/pdf/2609.02525v1
- **DOI:** [10.48550/arXiv.2609.02525](https://doi.org/10.48550/arXiv.2609.02525)
- **License:** arXiv perpetual non-exclusive license / Creative Commons Attribution 4.0 International.
- **Direct Primary-Source Verification:** The complete preprint full text (Sections 1–5, Equations 1–30, Lemma 2, Assumptions 3, Theorems 4, 7, 8, Propositions 1, Corollaries 5, 6, Figures 1–2, Tables 1–2, and Appendices A–E) was directly retrieved and audited. All mathematical derivations, first-passage renewal scale formulations, Monte Carlo calibration metrics, and empirical testing conditions trace directly to `arXiv:2609.02525v1`.
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero prior citations of `arXiv:2609.02525`, Alejandro Rodríguez Domínguez, representation switching frictions, or first-passage renewal residence scale aggregation. Existing microstructure and order-flow records in the repository address fundamentally different mechanisms:
  - `duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11.md` (Jebali 2026, arXiv:2609.07989) examined duration-aware Bayesian online changepoint detection in high-frequency order flows;
  - `deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md` (Moret & Lillo 2026, arXiv:2609.11614) studied distributional reinforcement learning for market makers facing regime-switching flows;
  - `model-free-passive-execution-order-level-shadowing-2026-09-17.md` (Maciejewski 2026, arXiv:2609.18019) developed order-level shadowing for passive execution without impact kernels;
  - `separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17.md` (Nunes 2026, arXiv:2609.17609) analyzed packing bounds and spectral limits of equal-weighted signal libraries;
  - `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` investigated empirical falsification of retail cumulative volume delta (CVD) heuristics.
  - In contrast, Rodríguez Domínguez (2026) develops the first formal microfoundation connecting upstream institutional portfolio representation switching frictions (the governance, validation, turnover, and margin costs of replacing factor models or predictive representations) to downstream long-memory order-flow persistence ($C_\infty(t) \sim t^{-\theta/2}$), proving exact testable joint exponent restrictions ($H_0^{(R)}: 2\alpha_F - \theta = 0$, $H_0^{(\tau)}: \alpha_F - \beta = 0$), finite-market scaling truncation bounds ($T_{\mathrm{cutoff}} \approx N^{2/\theta}$), and an execution-weighting invariance theorem ($q_a^2 \lambda_a^2 v_a$).

## Economic mechanism

### Source-reported

In modern quantitative and institutional asset management, trading decisions depend on an underlying predictive representation: a factor set, common-driver subspace, statistical model family, or information state that organizes signals, forecasts, constraints, and hedges.

Replacing an incumbent predictive representation is costly:
1. **Governance & Model Validation:** New models require backtesting, out-of-sample risk audit, and investment committee sign-off.
2. **Turnover & Rebalancing Frictions:** Switching factor sets abruptly triggers large portfolio turnover, generating immediate market impact, bid-ask spread costs, and brokerage commissions.
3. **Funding & Inventory Constraints:** Liquidating old hedges and establishing new factor exposures requires margin reallocation and potential borrow search.

Consequently, an institutional portfolio $a$ retains its incumbent representation until the accumulated evidence of superior alternative investment opportunities overcomes an effective switching threshold $\kappa_a > 0$. Rodríguez Domínguez models this decision as a first-passage stopping problem for a local opportunity coordinate $G_{a, t} \ge 0$ evolving as reflected Brownian motion with opportunity volatility $\sigma_a > 0$. The resulting residence time before a representation switch is $\tau_a = R_a^2 \tau_0$, where $R_a = \kappa_a / \sigma_a$ is the portfolio's residence scale and $\tau_0$ is the standard first-exit time from $(-1, 1)$.

Because institutional managers face heterogeneous governance hurdles ($\kappa_a$) and monitor diverse opportunity sets ($\sigma_a$), the cross-sectional distribution of residence scales $R_a$ exhibits a heavy Pareto tail with index $\theta > 0$. When individual portfolios execute trades according to their representation-conditioned demand, the aggregation of these asynchronous renewal processes induces long memory in market-wide signed order flow, with aggregate covariance decaying as a power law $C_\infty(t) \sim t^{-\theta/2}$. The paper demonstrates that upstream representation switching frictions provide a structural complement to the standard downstream metaorder-splitting mechanism (Lillo & Farmer 2004).

### Research interpretation

The economic thesis yields three falsifiable quantitative insights for market microstructure and execution research:
1. **Microstructure Long Memory is Upstream-Restricted:** Financial order-flow long memory cannot be solely attributed to order execution desks breaking large parent orders into child metaorders (downstream splitting). A substantial component originates upstream in the multi-day and multi-week residence times of institutional factor models.
2. **Execution-Weighting Invariance:** Observed market order flow reflects the execution-weighted residence scale distribution $\mu_N^F$, where each portfolio's contribution is scaled by $q_a^2 \lambda_a^2 v_a$ ($q_a$ = order size, $\lambda_a$ = trading intensity, $v_a$ = demand variance). Testing unweighted model durations against market-wide flow covariance creates severe parameter mismatch.
3. **Regime-Aware Finite-Market Truncation:** Real markets contain a finite number of active institutional strategies ($N$). Therefore, true power-law memory exists only within an intermediate scaling window $t \ll T_{\mathrm{cutoff}} \approx N^{2/\theta}$. Beyond this cutoff, order-flow autocorrelation undergoes a sharp crossover into exponential decay. Execution algorithms (e.g. Almgren-Chriss, Bouchaud propagator models) that extrapolate power-law impact kernels beyond $T_{\mathrm{cutoff}}$ will systematically overestimate residual impact and incur excess execution drag.

## Signal

The mathematical model and testable restrictions are formulated in Sections 3, 4, and Appendices A–D of Rodríguez Domínguez (`arXiv:2609.02525v1`, `source-reported`).

### 1. Mathematical Framework & Residence Scale Dynamics (`source-reported`)

- **Local Opportunity Process:** For portfolio $a$, the accumulated evidence coordinate $G_{a, t} \ge 0$ follows reflected Brownian motion between switches:
  $$\mathrm{d}G_{a, t} = \sigma_a \mathrm{d}W_{a, t} + \mathrm{d}L_{a, t}^0, \quad G_{a, t} \ge 0$$
  where $\sigma_a > 0$, $W_a$ is standard Brownian motion, and $L_a^0$ is the local time enforcing reflection at zero.
- **Representation Switch Event:** A switch occurs at first passage:
  $$\tau_a = \inf \{ t > 0 : G_{a, t} = \kappa_a \}$$
  where $\kappa_a > 0$ is the effective threshold offsetting switching costs.
- **Scale Homogeneity & Residence Scale:** By scale equivalence of reflected Brownian motion started at zero to absolute Brownian motion:
  $$\tau_a \overset{d}{=} R_a^2 \tau_0, \quad R_a := \frac{\kappa_a}{\sigma_a}$$
  where $\tau_0$ is the first exit time of standard Brownian motion from $(-1, 1)$, with $\mathbb{E}[\tau_0] = 1$ and $\mathbb{E}[\tau_a] = R_a^2$.
- **Laplace Transform and Survival Function (Equations 4–5):**
  $$\mathbb{E}[e^{-s\tau_a}] = \operatorname{sech}(R_a \sqrt{2s})$$
  $$\mathbb{P}(\tau_0 > t) = \frac{4}{\pi} \sum_{n=0}^\infty \frac{(-1)^n}{2n+1} \exp\left[ -\frac{(2n+1)^2 \pi^2}{8} t \right]$$

### 2. Stationary Renewal Kernel & Aggregate Covariance Mapping (`source-reported`)

- **Representation-Conditioned Demand:** In spell $n$, portfolio $a$ has representation state $S_{a, n}$ and centered conditional demand $B_{a, n} := \mathbb{E}[D_a(t) \mid S_{a, n}]$ with $\mathbb{E}[B_{a, n}] = 0$ and $\operatorname{Var}(B_{a, n}) = v_a \in (0, \infty)$.
- **Stationary Renewal Kernel (Lemma 2):** For lag $t \ge 0$:
  $$\operatorname{Cov}(B_{a, n(0)}, B_{a, n(t)} \mid R_a) = v_a h_0(t / R_a^2)$$
  where $h_0(x)$ is the equilibrium residual-life survival function:
  $$h_0(x) = \int_x^\infty \mathbb{P}(\tau_0 > u) \mathrm{d}u = \frac{32}{\pi^3} \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^3} \exp\left[ -\frac{(2n+1)^2 \pi^2}{8} x \right]$$
  with $h_0(0) = 1$, $h_0(x) > 0$, and exponential decay as $x \to \infty$.
- **Primitive Tail Regular Variation (Proposition 1):** If switching threshold $\kappa$ is regularly varying with index $\theta > 0$ ($\mathbb{P}(\kappa > x) = x^{-\theta} L_\kappa(x)$), $\kappa$ and $\sigma$ are independent, and $\mathbb{E}[\sigma^{-(\theta+\varepsilon)}] < \infty$, then by Breiman's lemma:
  $$\mathbb{P}(R > r) \sim \mathbb{E}[\sigma^{-\theta}] \mathbb{P}(\kappa > r) \sim L(r) r^{-\theta}, \quad r \to \infty$$
- **Residence-Tail Mapping Theorem (Theorem 4):** Under weakly convergent weighted residence measures $\mu_N \Rightarrow \mu$ with tail $\overline{\mu}(r) \sim L(r) r^{-\theta}$ and transitory demand $s(t) = o(L(\sqrt{t}) t^{-\theta/2})$:
  $$C_\infty(t) \sim K_{\mathrm{FP}}(\theta) L(\sqrt{t}) t^{-\theta/2}, \quad t \to \infty$$
  $$K_{\mathrm{FP}}(\theta) = \frac{\theta}{2} \int_0^\infty h_0(u) u^{\theta/2 - 1} \mathrm{d}u$$
  Consequently, the aggregate order-flow memory exponent is $\alpha = \theta / 2$.
- **Memory Boundary (Corollary 5):** Covariance is non-summable (long memory) when $0 < \theta < 2$ and summable (short memory) when $\theta > 2$. When $0 < \theta < 2$, cumulative variance scales as $\operatorname{Var}(\sum_{t=1}^T X(t)) \asymp T^{2 - \theta/2} L(\sqrt{T})$.

### 3. Execution-Clock Invariance and Observable Exponent Restriction (`source-reported`)

- **Execution-Weighted Measure (Equation 28):** In the presence of Poisson execution arrivals with intensity $\lambda_a$ and order quantity $q_a$:
  $$\mu_N^F(\mathrm{d}r) = \frac{\sum_{a=1}^N q_a^2 \lambda_a^2 v_a \delta_{R_a}(\mathrm{d}r)}{\sum_{a=1}^N q_a^2 \lambda_a^2 v_a}$$
- **Observable Exponent Equivalence (Corollary 6 & Theorem 8):** Under common execution weights, the execution-weighted spell duration tail exponent $\beta$ and the aggregate flow covariance decay exponent $\alpha_F$ satisfy the exact dual restrictions:
  $$\mathbb{P}(\tau > t) \sim \mathbb{E}[\tau_0^{\theta/2}] L_F(\sqrt{t}) t^{-\theta/2} \implies \beta = \frac{\theta}{2}$$
  $$\Gamma_\Delta^F(\ell) \sim \Delta^2 K_{\mathrm{FP}}(\theta) L_F(\sqrt{\ell\Delta}) (\ell\Delta)^{-\theta/2} \implies \alpha_F = \frac{\theta}{2}$$
  Yielding the two primary testable null hypotheses:
  $$H_0^{(R)}: 2\alpha_F - \theta = 0, \qquad H_0^{(\tau)}: \alpha_F - \beta = 0$$

### 4. Finite-Market Cutoff and Scaling Window (Theorem 7, `source-reported`)

For a market of $N$ portfolios with Pareto residence scales truncated at $x > 1$:
1. **Power-Law Scaling Regime:** If $t / x^2 \to 0$, then $C_x(t) / C_\infty(t) \to 1$ with relative error:
   $$\left| \frac{C_x(t)}{C_\infty(t)} - 1 \right| = O\left( x^{-\theta} + \left(\frac{\sqrt{t}}{x}\right)^\theta \right)$$
2. **Exponential Cutoff Regime:** If $t / x^2 \to \infty$, covariance collapses exponentially:
   $$C_x(t) \le \frac{A}{1 - x^{-\theta}} \exp(-\kappa t / x^2)$$
3. **Stochastic Cutoff Order:** Across $N$ iid Pareto draws, $R_{\max, N}^2 = O_p(N^{2/\theta})$, establishing that the usable empirical power-law horizon scales as $T_{\mathrm{cutoff}} \approx N^{2/\theta}$.

### 5. Algorithmic Signal Construction for Alpha & Execution (`research-proposed`)

For quantitative strategy research and execution cost optimization:
- **Order-Flow Memory State Estimation (`research-proposed`):** Estimate rolling signed order flow $F_t^\Delta$ across 5-minute to 1-hour bins $\Delta$. Fit empirical covariance decay $\hat{\Gamma}(\ell)$ across lags $\ell \in [24, 256]$ via log-log OLS to estimate $\hat{\alpha}_F$.
- **Horizon-Gated Flow Execution Strategy (`research-proposed`):**
  - If lag $\ell\Delta \le 0.25 \hat{T}_{\mathrm{cutoff}}$ and $\hat{\alpha}_F < 0.80$ (strong long-memory regime): Order flow exhibits structural persistence. Follow institutional signed flow with a passive participation strategy (momentum/continuation signal).
  - If lag $\ell\Delta \ge \hat{T}_{\mathrm{cutoff}}$: Autocorrelation decays exponentially. Frictions from representation switching have dissipated; fade aggressive order flow with contrarian limit orders (mean-reversion signal).
- **Execution Impact Kernel Correction (`research-proposed`):** In propagator market-impact algorithms ($I(t) = \int_0^t G(t-s) \mathrm{d}V_s$), replace generic power-law kernels $G(t) \sim t^{-\gamma}$ with the finite-market truncated first-passage renewal kernel:
  $$G(t) = G_0 \cdot h_0(t / \hat{R}_{\max}^2) \cdot t^{-\hat{\alpha}_F} \quad (\text{research-proposed})$$
  preventing over-conservatism at long multi-day horizons.

## Required data

- **High-Frequency Order Flow:** Timestamped trade prints with signed direction (buyer-initiated $+1$, seller-initiated $-1$) classified via tick rule or Lee-Ready algorithm, execution volume $q_{i, t}$, and venue identifier.
- **Institutional Portfolio / Account Holdings (Empirical Testbed):** Account-level or portfolio-level holdings, target positions, and dated model deployment records (or versioned production algorithm logs).
- **Timeframe & Sampling Intervals:**
  - Intraday flow aggregation bins: $\Delta \in \{ 1\text{ min}, 5\text{ min}, 15\text{ min}, 1\text{ hour} \}$ (`research-proposed`).
  - Estimation lag window: $\ell \in [24, 256]$ bins (`source-reported` in Appendix D).
- **Point-in-Time Discipline:** Estimation of the residence-scale tail index $\hat{\theta}$ and cutoff $\hat{T}_{\mathrm{cutoff}}$ must be conducted strictly on an in-sample training split; flow covariance decay $\hat{\alpha}_F$ must be evaluated out-of-sample on a non-overlapping evaluation split (`source-reported`, Section 4.2).
- **Missing Data & Halt Handling (`research-proposed`):** During market halts or suspended trading intervals, exclude inter-day auction imbalances from the continuous Poisson execution series to prevent artificial zero-autocorrelation prints.

## Execution assumptions

- **Execution Mechanism (`research-proposed`):** Alpha signals derived from representation-persistence regimes are executed via passive limit orders placed inside the spread, capitalizing on predictable multi-hour institutional parent-flow drift.
- **Order Timing (`source-reported`):** Execution arrivals modeled as an independent Poisson point process with intensity $\lambda_a$ and fixed ticket size $q_a$.
- **Execution Cost Model (`research-proposed`):** Exchange taker fee modeled at 2 bps / maker rebate at 0.5 bps for liquid equity/crypto markets; half-spread assumed at 1.5 bps.
- **Finite Population Scaling (`source-reported`):** Simulation results evaluate $N \in [100, 3000]$ portfolios over $T = 4,096$ observation periods.

## Evidence

### Source-reported

All analytical theorems, asymptotic formulas, and Monte Carlo simulation values below are directly reported by Alejandro Rodríguez Domínguez (`arXiv:2609.02525v1`, September 2026, Section 4.1, Figure 1–2, and Appendix D):

#### 1. Simulation Protocol & Calibration Setup (Appendix D)
- **Random Seed:** `260902`.
- **First-Exit Time Generation:** Drawn from the exponential-product representation of $\operatorname{sech}(\sqrt{2s})$, implemented using 48 explicit components and a moment-matched gamma remainder.
- **Equilibrium Residual Draws:** Sampled from the corresponding length-biased distribution.
- **Calibration Pools:** Pools of 200,000 first-exit times and 200,000 residual draws generated prior to experiments.
- **Exit-Clock Moments:** Exit-clock draws possess empirical mean $1.001$ and variance $0.668$; equilibrium residual draws possess empirical mean $0.833$.
- **Monte Carlo Design:** 30 replications for each of three residence-tail indices $\theta \in \{0.8, 1.2, 1.6\}$, with $N = 500$ portfolios and $T = 4,096$ observation periods per replication. An independent sample of 30,000 durations is used for each spell-tail Hill estimate (using the largest 8% of observations).

#### 2. Joint Exponent Recovery Performance (Section 4.1, Figure 1)
Covariance-decay exponents estimated via log-log regression over positive covariance estimates at lags 24–256:
- **Target Exponent $\alpha_F = 0.400$ ($\theta = 0.800$):**
  - Realized flow estimate mean: $0.409$ (Monte Carlo standard error $0.009$).
  - Duration estimate recovers the analytical target closely.
- **Target Exponent $\alpha_F = 0.600$ ($\theta = 1.200$):**
  - Realized flow estimate mean: $0.603$ (Monte Carlo standard error $0.014$).
- **Target Exponent $\alpha_F = 0.800$ ($\theta = 1.600$, near short-memory boundary):**
  - Duration estimate: $0.801$ (Monte Carlo standard error $0.003$).
  - Realized flow estimate mean: $0.898$ (Monte Carlo standard error $0.041$).
  - Realized flow 10th–90th percentile range: $[0.670, 1.217]$.

#### 3. Execution Weighting Distortion (Section 4.1, Figure 2, Left Panel)
Execution intensity parameterized as $\lambda_a = R_a^\eta \exp(0.2 Z)$, where $Z \sim N(0, 1)$, evaluating participation elasticity $\eta \in [0, 0.300]$ across 60 draws per setting with fixed $\theta = 1.6$:
- At $\eta = 0.000$ (target $\alpha_F = 0.800$): Aligned mean estimate $= 0.803$; unweighted mean $= 0.797$.
- At $\eta = 0.300$ (target shifted to $\alpha_F = 0.500$ due to heavy execution weighting):
  - Aligned weighting tracks the shifting target down to mean $0.507$.
  - Unweighted estimate remains distorted at $0.804$ (failing to detect the heavy-tailed flow concentration).

#### 4. Finite-Market Usable Scaling Horizon (Section 4.1, Figure 2, Right Panel)
Evaluating the empirical usable scaling cutoff across 60 draws per population size $N$:
- At $N = 100$ portfolios: Median usable horizon is $68.539$ periods.
- At $N = 3,000$ portfolios: Median usable horizon expands to $12,270.751$ periods.
- Dispersion across draws is wide, and the realized stable range is consistently shorter than the crude proxy $R_{\max, N}^2$.

### Independently reproduced

Not independently reproduced. All theoretical derivations, asymptotic theorems, and numerical simulation statistics represent third-party reported findings from Alejandro Rodríguez Domínguez (`arXiv:2609.02525v1`).

### Negative evidence

- **Flow Estimator Breakdown Near Short-Memory Boundary ($\theta \to 2$):** At $\theta = 1.600$ ($\alpha_F = 0.800$), the flow covariance estimator exhibits substantial upward finite-sample bias (mean $0.898$ vs target $0.800$) and severe variance (10th–90th percentile span $[0.670, 1.217]$), indicating that empirical flow regressions require substantially longer time series or explicit bias correction near the short-memory boundary.
- **Complete Invalidation Under Unweighted Estimation:** When large institutions trade more aggressively (participation elasticity $\eta > 0$), unweighted duration estimators completely decouple from realized market flow (reporting $\hat{\beta} \approx 0.80$ while true flow decay is $\alpha_F = 0.50$). An unweighted persistence test will falsely reject the model.
- **Sharp Finite-Cross-Section Truncation:** In markets with a small number of active quantitative participants ($N \le 100$), the power-law memory regime collapses into exponential decay within only $\sim 68$ time periods, preventing the use of asymptotic long-memory models for multi-day positioning.

## Falsification plan

1. **Joint Exponent Restriction Test ($H_0^{(R)}$ and $H_0^{(\tau)}$, `research-proposed`):**
   - Estimate the residence-scale tail index $\hat{\theta}$ from institutional model change logs (or proxy 13F / rebalancing frequency tables) on a training sample, and estimate the unconditional signed order-flow decay exponent $\hat{\alpha}_F$ on a held-out evaluation sample across lags 24–256.
   - `research-defined falsification threshold`: If the absolute difference $|2\hat{\alpha}_F - \hat{\theta}| > 0.15$ or $|\hat{\alpha}_F - \hat{\beta}| > 0.15$ with $p < 0.05$ under block-resampled standard errors, reject the hypothesis that representation switching frictions drive order-flow long memory.
2. **Metaorder Splitting Residualization Test (`research-proposed`):**
   - Reconstruct parent metaorders using proprietary or cluster-based metaorder reconstruction algorithms (e.g., Bershova-Rakhlin / Vaglica algorithms). Subtract the within-metaorder child order persistence from total signed flow.
   - `research-defined falsification threshold`: If the residual order flow exhibits zero statistically significant autocorrelation at multi-hour lags ($\hat{\Gamma}_{\mathrm{resid}}(\ell) = 0$ for all $\ell > 24$), falsify the upstream representation-switching channel in favor of pure downstream execution splitting.
3. **Finite-Market Truncation Crossover Test (`research-proposed`):**
   - Measure empirical order-flow autocorrelation across assets with varying institutional ownership breadth ($N_{\mathrm{inst}} \in [10, 500]$).
   - `research-defined falsification threshold`: If the empirical scaling cutoff horizon $T_{\mathrm{cutoff}}$ does not exhibit a statistically significant positive power-law relationship with institutional breadth ($\partial \ln T_{\mathrm{cutoff}} / \partial \ln N \le 0$), reject Theorem 7's finite-population scaling bound.

## Crypto portability

- **Portability Status:** Adapted / Unproven (`research-proposed`).
- **Cryptocurrency-Specific Microstructure Adaptations:**
  - *Bot Domination vs Institutional Governance:* In centralized crypto spot and perpetual markets, automated market makers and high-frequency algorithms adjust parameters continuously via programmatic APIs, lacking the human committee governance and formal quarterly validation cycles typical of equity pension funds. However, institutional crypto asset managers and quantitative hedge funds running multi-strategy alpha engines still operate discrete model versioning and risk allocations.
  - *24/7 Session Continuity:* Unlike traditional equities with distinct market closes, crypto trading is continuous. The absence of overnight session halts eliminates artificial boundary resets, providing an ideal continuous observation window for testing first-passage renewal clocks without overnight gap distortions.
  - *Perpetual Funding Rate Squeezes as Switching Accelerators:* In crypto perpetual futures, extreme funding rates ($>0.10\%$ per 8 hours) act as an external forcing drift on the opportunity coordinate $G_{a, t}$, compressing residence times $\tau_a$ and accelerating representation switches during leverage flushes.
  - *Decentralized AMM Liquidity Pools:* In automated market makers (Uniswap v3/v4), liquidity provider range adjustments represent discrete representation switches. The distribution of LP re-centering intervals can be mapped directly to the residence scale framework.

## Limitations

- **One-Dimensional Opportunity Coordinate Approximation (`source-reported`):** Modeling the representation switching decision as a one-dimensional reflected Brownian motion $G_{a, t}$ is a stylized approximation. Real institutional switching decisions involve multi-factor risk dashboards, personnel changes, and multi-asset optimization.
- **Non-Exclusivity Relative to Metaorder Splitting (`source-reported`):** Upstream representation switching is a complementary mechanism, not an exclusive one. Intraday order splitting remains a dominant contributor to high-frequency tick autocorrelation.
- **Severe Sensitivity to Unobserved Execution Weights (`source-reported`):** In public market data lacking trader account identifiers, estimating the exact weighting factor $q_a^2 \lambda_a^2 v_a$ is challenging, creating vulnerability to weighting misspecification.
- **Requirement of Account-Level Data for Direct Empirical Audit (`source-reported`):** A definitive empirical test requires access to account identifiers or timestamped model deployment records; public anonymous trade tapes provide only compatibility evidence, not structural proof.

## Implementation status

- `not-implemented`: No empirical renewal estimation engine, representation-switching detector, or modified execution impact kernel has been integrated into NautilusTrader or our quantitative research repository.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves strictly as upstream theoretical and empirical market microstructure research. It does not constitute trading advice and does not authorize paper, testnet, or live trading capital deployment.

## Related Wiki records

- `[[quant/duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11]]` — Duration-aware Bayesian online changepoint detection for high-frequency order flows.
- `[[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]]` — Distributional RL market making under regime-switching order flow.
- `[[quant/model-free-passive-execution-order-level-shadowing-2026-09-17]]` — Order-level shadowing for passive execution without impact kernels.
- `[[quant/separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17]]` — Cross-sectional signal library packing limits and spectral bounds.
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` — Forensic falsification of retail order flow CVD heuristics.

## Sources

1. Alejandro Rodríguez Domínguez, *"Switching Frictions, Heterogeneous Trading Horizons, and Long-Memory Order Flow"*, arXiv preprint `arXiv:2609.02525v1 [q-fin.PM]`, submitted September 2, 2026.
   - Canonical URL: https://arxiv.org/abs/2609.02525
   - Full-text HTML: https://arxiv.org/html/2609.02525v1
   - Full-text PDF: https://arxiv.org/pdf/2609.02525v1
   - DOI: [10.48550/arXiv.2609.02525](https://doi.org/10.48550/arXiv.2609.02525)
2. Fabrizio Lillo and J. Doyne Farmer, *"The Key Role of the Limit Order Book in Funneling Liquidity into Price Changes"*, *Quantitative Finance*, 4(4):399–411, 2004. DOI: [10.1080/14697680400008627](https://doi.org/10.1080/14697680400008627).
3. Fabrizio Lillo, Mike Szell, and J. Doyne Farmer, *"Theory for the Long Memory in Supply and Demand"*, *Physical Review E*, 71(6):066122, 2005. DOI: [10.1103/PhysRevE.71.066122](https://doi.org/10.1103/PhysRevE.71.066122).
4. Robert Almgren and Neil Chriss, *"Optimal Execution of Portfolio Transactions"*, *Journal of Risk*, 3(2):5–39, 2001. DOI: [10.21314/JOR.2001.041](https://doi.org/10.21314/JOR.2001.041).
5. Leo Breiman, *"On Some Limit Theorems Similar to the Arc-Sin Law"*, *Theory of Probability & Its Applications*, 10(2):303–312, 1965. DOI: [10.1137/1110037](https://doi.org/10.1137/1110037).
6. David R. Cox, *"Renewal Theory"*, Methuen & Co., London, 1962.
7. William Feller, *"An Introduction to Probability Theory and Its Applications"*, Volume II, 2nd edition, John Wiley & Sons, New York, 1971.
8. Alejandro Rodríguez Domínguez, *"Portfolio Choice under Dynamic Common-Driver Geometry"*, Working Paper / arXiv preprint, 2026a.
9. Alejandro Rodríguez Domínguez, *"Equilibrium Selection, Crowding, and Capacity under Shared Representations"*, Working Paper / arXiv preprint, 2026b.
10. Alejandro Rodríguez Domínguez, *"Uniform Inference and Certified Capacity at a Reflexive Stability Boundary"*, arXiv preprint `arXiv:2609.02535v1 [q-fin.PM]`, September 2026c.
