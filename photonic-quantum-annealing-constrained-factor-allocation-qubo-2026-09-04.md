---
schema: strategy-research-record-v1
title: Photonic Quantum Annealing vs. Classical Solvers for Constrained Factor Portfolio Optimization
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-14
sources:
  - "https://arxiv.org/abs/2608.14134"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Photonic Quantum Annealing vs. Classical Solvers for Constrained Factor Portfolio Optimization

## Provenance

- **Primary Source:** Nirvik Sahoo, Chyng Wen Tee, and Paul Robert Griffin (School of Computing and Information Systems / Lee Kong Chian School of Business, Singapore Management University), *"Photonic Quantum Computing vs. Classical Solvers in Constrained Factor Portfolio Optimization"*, arXiv preprint `arXiv:2608.14134v1 [q-fin.PM, quant-ph]`, submitted August 14, 2026.
- **Canonical Stable URLs:**
  - Abstract: [https://arxiv.org/abs/2608.14134](https://arxiv.org/abs/2608.14134)
  - Full text HTML: [https://arxiv.org/html/2608.14134v1](https://arxiv.org/html/2608.14134v1)
  - Full text PDF: [https://arxiv.org/pdf/2608.14134v1](https://arxiv.org/pdf/2608.14134v1)
  - DOI: [10.48550/arXiv.2608.14134](https://doi.org/10.48550/arXiv.2608.14134)
- **Licensing:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Verification Integrity:** This record was generated following a line-by-line inspection of the primary paper text, derivations, equations, and empirical tables in `arXiv:2608.14134v1`. No search engine snippets, secondary summaries, or synthetic extrapolations were used to formulate strategy mechanics or empirical figures. A repository-wide audit and Hermes Wiki Brain cross-check confirmed zero existing records matching `arXiv:2608.14134` or photonic quantum annealing factor allocation.

## Economic mechanism

### Source-reported
Institutional asset allocation frequently incorporates cardinal constraints, such as limits on active factor bets, turnover restrictions, transaction costs, and higher-order risk shaping (volatility and skewness penalties). These real-world constraints transform standard mean-variance optimization into an NP-hard mixed-integer or non-convex combinatorial problem. Standard quadratic programming cannot natively enforce discrete inclusion budgets and complex penalty trade-offs without continuous relaxation or heuristic approximations.

To explore whether non-classical computing architectures provide advantages in navigating these non-convex spaces, Sahoo, Tee, and Griffin evaluate three architecturally distinct optimization engines over 13 Jensen–Kelly–Pedersen (JKP) equity anomaly factors across a 164-month horizon:
1. **Dirac-3 (Quantum Computing Inc.):** An entropy-based photonic quantum annealer that natively processes Higher-Order Unconstrained Binary Optimization (HUBO) and continuous-variable objectives using non-qubit optical degrees of freedom.
2. **Gurobi (MIP):** A commercial deterministic branch-and-bound mixed-integer programming solver serving as the classical optimality benchmark.
3. **Soft Actor-Critic (SAC):** An off-policy model-free deep reinforcement learning agent learning continuous portfolio weight policies directly via entropy-regularized policy gradients.

The source authors report three primary findings:
- Photonic quantum annealing achieves superior risk-adjusted alpha capture within a narrow, localized operating window ($\beta_1 \in \{1, 2\}$ in the primary sweep, $\beta_2 \in [0.5, 1]$ at $\beta_1=0$ in the joint sweep), capturing peak Sharpe (0.760) and Calmar (0.567) ratios and maximum drawdown attenuation (-2.63%). This advantage is structurally driven by the photonic annealer's stochastic sampling bias toward high-persistence, quality-adjacent anomaly factors (accruals and investment).
- Classical mixed-integer programming (Gurobi) consistently delivers the most robust tail-risk protection ($\text{CVaR}_{5\%} = -0.863\%$), minimal cross-seed variance, and stable factor diversification (HHI bounded in $[0.135, 0.228]$) without catastrophic failure modes.
- Deep reinforcement learning (SAC) exhibits structural mode collapse under unanchored higher-moment penalties ($\beta_2 \ge 10$ with $\beta_1=0$), where the absence of a binding volatility penalty forces the policy gradient to regularize excessively toward low-activity factors, resulting in extreme single-factor concentration (HHI expanding to 0.593, CR-5 to 0.985–0.996) and severe drawdown (-14.64%).

### Research interpretation
The comparative evaluation provides an empirical benchmark for portfolio optimization engines operating under transaction costs and multi-moment regularization.

From a quantitative research perspective:
- **Heuristic Combinatorial Search vs. Deterministic Branching:** Mapping factor selection to a Quadratic Unconstrained Binary Optimization (QUBO) problem allows photonic hardware to sample low-energy combinatorial subsets rapidly. In factor allocation, where true factor alphas are sparse and subject to structural co-movement, Dirac-3's natural search dynamics isolate persistent low-tail-risk anomaly clusters (accruals + investment). However, this creates a structural trade-off: photonic heuristic efficiency comes at the price of hyper-concentration (top-5 concentration ratio $\text{CR-5} > 0.90$), which requires active post-optimization constraints or strict hyperparameter gating.
- **Objective Function Misspecification in Policy-Gradient RL:** The documented failure of SAC under unanchored skewness shaping ($\beta_2 \ge 10$, $\beta_1=0$) reveals a fundamental risk in end-to-end policy gradients for portfolio management: when higher-order reward terms lack an anchoring variance constraint, the stochastic actor minimizes penalty step-sizes by allocating all capital to stagnant low-volatility assets (low-risk, low-leverage), destroying cross-sectional diversification and causing catastrophic out-of-sample drawdowns (-14.64%).
- **Circuit-Breaker Architecture:** Real-time monitoring of factor allocation entropy (HHI) and tracking single-factor exposure caps (30% threshold) acts as a structural defense mechanism, providing early-warning signals of optimizer destabilization before drawdowns manifest.

## Signal

### Mathematical Formulation
The factor allocation problem optimizes an active portfolio across $N=13$ equity anomaly factors at monthly rebalancing step $t$, subject to the budget constraint $\sum_{i=1}^N w_{i,t} = 1$ and long-only constraints $w_{i,t} \ge 0$.

#### 1. Multi-Moment Objective Function
$$\max_{w_t} \left[ w_t^\top r_t - \beta_1 \widehat{\sigma}_{t,m} + \beta_2 \widehat{\kappa}_{t,m} - c_{\text{tc}} \|w_t - w_{t-1}\|_1 \right]$$
where:
- $r_t \in \mathbb{R}^{13}$: realized monthly factor return vector.
- $\widehat{\sigma}_{t,m}$: rolling $m$-period realized portfolio volatility ($m=6$ months for rolling window evaluation).
- $\widehat{\kappa}_{t,m}$: rolling bias-corrected Fisher skewness coefficient of the portfolio return series.
- $c_{\text{tc}} = 0.002$ (20 bps): proportional transaction cost per unit of $L_1$-norm turnover.
- $\beta_1 \ge 0$: primary volatility penalty parameter governing risk aversion.
- $\beta_2$: secondary skewness incentive parameter (positive values reward positive skewness / fat right tails, mitigating drawdown risk).

#### 2. Two-Stage QUBO + Restricted MVO Architecture (Dirac-3 and Gurobi)
To solve the combinatorial selection problem, factor inclusion is mapped to a binary decision vector $x \in \{0, 1\}^N$, where $x_i = 1$ includes factor $i$ in the active allocation and $x_i = 0$ excludes it:
$$\max_{x \in \{0,1\}^N} \left[ \sum_{i=1}^N \alpha_i x_i - c_{\text{pos}} \sum_{i=1}^N x_i - \lambda \sum_{i=1}^N \sum_{j=1}^N \Sigma_{ij} x_i x_j - \sum_{i=1}^N \delta_i x_i \right]$$
where:
- $\alpha \in \mathbb{R}^{13}$: expected return forecast generated by the policy model.
- $\bm{\Sigma} \in \mathbb{R}^{13 \times 13}$: Ledoit-Wolf shrinkage covariance matrix of factor returns.
- $c_{\text{pos}} = 0.01$: fixed cardinality opening penalty per active factor.
- $\lambda = 1.0$: baseline risk-aversion scalar.
- $\delta_i = \pm \tau_{\text{pen}}$: dynamic turnover penalty with $\tau_{\text{pen}} = 0.10$, where $\delta_i = +\tau_{\text{pen}}$ if factor $i$ was absent in $t-1$ (penalizing turnover) and $\delta_i = -\tau_{\text{pen}}$ if factor $i$ was active in $t-1$ (rewarding persistence).

Expressed in QUBO matrix form $Q \in \mathbb{R}^{N \times N}$:
- Diagonal terms: $Q_{ii} = -\alpha_i + c_{\text{pos}} + \lambda \Sigma_{ii} + \delta_i$
- Off-diagonal terms: $Q_{ij} = 2 \lambda \Sigma_{ij}$

#### 3. Solver Dispatch
- **Dirac-3:** The sparse polynomial matrix $Q$ is submitted to the Dirac-3 photonic annealer with relaxation schedule $\text{RS}=2$, extracting the minimum-energy binary ground state $x^* \in \{0, 1\}^N$.
- **Gurobi:** Solved as a binary quadratic program via exact branch-and-bound, with solution thresholded at $x_i^* = \mathbb{I}[x_i > 0.5]$.
- **SAC (Direct Weight Baseline):** Directly generates continuous actions $a_t \in \mathbb{R}^{13}$ mapped to weights via softmax $w_t = \text{softmax}(a_t)$, bypassing QUBO formulation.

#### 4. Weight Reconstruction and Turnover Smoothing
Given the selected active subset $\mathcal{S} = \{i : x_i^* = 1\}$:
1. Continuous weights are computed via restricted mean-variance optimization:
   $$w_{\mathcal{S}} = \frac{\bm{\Sigma}_{\mathcal{S}}^{-1} \bm{\alpha}_{\mathcal{S}}}{\mathbf{1}^\top \bm{\Sigma}_{\mathcal{S}}^{-1} \bm{\alpha}_{\mathcal{S}}}$$
2. Box constraints are enforced: $w_i \in [0.00, 0.60]$, followed by unit-sum renormalization $\sum_{i \in \mathcal{S}} w_i = 1$.
3. Turnover dampening exponential filter:
   $$w_t = (1 - \eta) w_{t-1} + \eta w_{\mathcal{S}}, \quad \eta = 0.10$$
   Realized portfolio return is $r_{\text{port},t} = w_t^\top r_t$, and fractional $L_1$-norm turnover is $\text{TO}_t = \|w_t - w_{t-1}\|_1$.

## Required data

- **Asset Universe:** $N = 13$ value-weighted, capped US equity anomaly factors from the Jensen–Kelly–Pedersen (JKP 2023) factor library:
  1. Value
  2. Momentum
  3. Short-term Reversal
  4. Quality
  5. Profitability
  6. Investment
  7. Low-Risk
  8. Low-Leverage
  9. Seasonality
  10. Accruals
  11. Debt Issuance
  12. Idiosyncratic Volatility
  13. Size
- **Timeframe & Sampling:** Monthly factor returns covering $T = 164$ months (approximately 13.7 years), encompassing market stress regimes including the March 2020 COVID-19 crash and 2022 interest rate tightening.
- **Partitioning:** Chronological 80/20 train/test split:
  - In-sample training window: 131 months.
  - Out-of-sample evaluation window: 33 months (all empirical metrics reported exclusively on test set).
- **Covariance Estimation:**
  - Rolling lookback window: $m_{\text{cov}} = 24$ months.
  - Estimator: Ledoit–Wolf shrinkage covariance matrix $\widehat{\bm{\Sigma}}_t$.
  - Conditioning & Symmetrization: $\widehat{\bm{\Sigma}}_t \leftarrow \frac{1}{2}(\widehat{\bm{\Sigma}}_t + \widehat{\bm{\Sigma}}_t^\top) + \varepsilon \mathbf{I}$ with diagonal perturbation $\varepsilon = 10^{-8}$ to guarantee positive definiteness.
- **Missing Data Handling:** Universe pre-filtered to include only capped factor return series with zero missing observations across the entire 164-month panel; no interpolation or synthetic imputation.

## Execution assumptions

- **Rebalancing Cadence:** Monthly rebalancing at month-end close.
- **Transaction Costs:** Proportional cost $c_{\text{tc}} = 0.002$ (20 bps per half-turn), matching institutional factor turnover drag in JKP (2023).
- **Turnover Dampening:** Fixed blend parameter $\eta = 0.10$ between prior weights $w_{t-1}$ and newly optimized weights $w_{\mathcal{S}}$.
- **Position Limits:** Maximum allocation to any single factor capped at $w_{\max} = 0.60$ (60%); no short selling permitted ($w_{\min} = 0.00$).
- **Solver Interface Latency:**
  - Dirac-3: Evaluated via Quantum Computing Inc. cloud API with relaxation schedule $\text{RS}=2$. Network round-trip latency and QPU queuing times are not modeled in backtest returns (appropriate for monthly cadence, but binding for high frequency).
  - Gurobi: Classical local branch-and-bound solver with exact global feasibility certificate.
  - SAC: Local policy-gradient inference.

## Evidence

### Source-reported
All empirical metrics below are directly reported by Nirvik Sahoo, Chyng Wen Tee, and Paul Robert Griffin (`arXiv:2608.14134v1`, Sections 4.1–4.5, Exhibits 2–11) on the held-out 33-month test window under 48 hyperparameter configurations:

#### 1. Primary Volatility Penalty Sweep ($\beta_2 = 0$, varying $\beta_1 \in \{0, 0.5, 1, 2, 5, 10, 20, 50\}$)
- **Dirac-3 (Photonic Quantum Annealer):**
  - Narrow optimal operating window at $\beta_1 \in \{1, 2\}$.
  - At $\beta_1 = 1$: Calmar ratio of **0.376** (sweep peak), Maximum Drawdown (MDD) of **-3.37%**, annualized Sharpe ratio of **0.697**, and $\text{CVaR}_{5\%}$ of **-1.015%**.
  - At $\beta_1 = 2$: Peak annualized Sharpe ratio of **0.715**, annual volatility of **2.05%**, and positive realized skewness of **+0.265**.
  - Factor composition at optimum: Dominant allocations to quality-adjacent persistent factors: Accruals (20.5%), Investment (14.5%), and Low-Leverage (10.2%).
  - Concentration: Average HHI of 0.228 across the sweep; CR-5 climbs to 0.965 at $\beta_1 = 10$.
  - Cross-seed stability: Controlled cross-seed Sharpe standard deviation $< 0.08$ across 3 independent seeds.
- **Gurobi (Classical MIP Branch-and-Bound):**
  - Peak performance at $\beta_1 = 5$: Sharpe ratio of **0.718**, Sortino ratio of **0.764**, annualized volatility of **1.81%**, HHI of **0.157**, CR-5 of **0.816** (Low-Leverage 13.9%, Debt-Issuance 10.0%).
  - At $\beta_1 = 0$: Sweep-best $\text{CVaR}_{5\%}$ of **-0.983%**.
  - Tail risk and concentration stability: HHI tightly bounded in $[0.136, 0.170]$ across all $\beta_1$; no single factor exceeds 17.7%.
  - Cross-seed stability: At $\beta_1 = 20$, Calmar ratio of 0.224, cross-seed return std of 0.10 percentage points, cross-seed Sharpe std $< 0.05$ across 5 independent seeds.
- **Soft Actor-Critic (SAC - Deep RL):**
  - At $\beta_1 = 2$: Generates highest nominal annualized return (**1.85%** vs Gurobi 1.34%), but suffers severe tail-risk expansion: $\text{CVaR}_{5\%}$ expands fourfold to **-2.388%**, realized skewness turns negative (**-0.237**).
  - At $\beta_1 = 50$: Strong penalty regularization improves $\text{CVaR}_{5\%}$ to **-1.223%**, but Sharpe (0.572) and Calmar (0.200) remain suboptimal.
  - Cross-seed instability: High variance across 5 seeds; at $\beta_1 = 20$, cross-seed Sharpe std reaches **0.206**, spanning a spread of 0.55 points (0.168 to 0.718).

#### 2. Joint Volatility & Skewness Sweep ($\beta_1 \in \{0, 1\}$, $\beta_2 \in \{0, 0.5, 1, 2, 5, 10, 20, 50\}$)
- **Dirac-3 Global Optimum $(\beta_1 = 0, \beta_2 = 1)$:**
  - Annualized Sharpe ratio: **0.760** (global peak of the entire 48-configuration study).
  - Sortino ratio: **0.841**.
  - Calmar ratio: **0.567** (global peak).
  - Maximum Drawdown: **-3.47%**.
  - $\text{CVaR}_{5\%}$: **-1.278%**.
  - Factor composition: Accruals (**25.9%**) and Investment (**19.6%**) jointly command **45.5%** of total portfolio weight.
- **Dirac-3 Capital-Preservation Optimum $(\beta_1 = 0, \beta_2 = 0.5)$:**
  - Maximum Drawdown: **-2.63%** (lowest drawdown of the entire 48-configuration experiment).
  - Calmar ratio: **0.538**, $\text{CVaR}_{5\%}$: **-1.107%**, Sharpe ratio $> 0.72$, HHI: **0.196**, CR-5: **0.943** (Investment 20.0%, Low-Leverage 20.0%).
- **Dirac-3 Tail-Risk Optimum in $\beta_1 = 1$ Regime $(\beta_1 = 1, \beta_2 = 10)$:**
  - $\text{CVaR}_{5\%}$: **-0.895%**, Sharpe ratio: **0.655**, MDD: **-3.41%**, Calmar: **0.381**, HHI: **0.254**, CR-5: **0.933**.
- **Dirac-3 vs. Classical Benchmarks Premium:**
  - Comparing Dirac-3 $(\beta_1 = 0, \beta_2 = 1)$ against Gurobi's peak Sharpe configuration $(\beta_1 = 0, \beta_2 = 50)$ (Sharpe 0.715): Dirac-3 delivers a Sharpe premium of **+0.045**, Sortino premium of **+0.100**, Calmar premium of **+0.310**, and MDD attenuation of **1.48 percentage points**, with trade-off of $\text{CVaR}_{5\%}$ differential of -0.367 percentage points and higher HHI (0.340 vs. 0.187).
- **Gurobi Global Tail-Risk Optimum $(\beta_1 = 0, \beta_2 = 1)$:**
  - $\text{CVaR}_{5\%}$: **-0.863%** (lowest downside tail risk recorded in the entire study). Balanced leadership across Accruals, Investment, and Quality.
  - At $(\beta_1 = 0, \beta_2 = 50)$: Sharpe of **0.715**, $\text{CVaR}_{5\%}$ of **-0.911%**, HHI of **0.187** (Quality 17.1%, Low-Leverage 11.3%, Seasonality 10.9%).
  - Structural robustness: HHI strictly bounded in $[0.135, 0.228]$ across all 16 joint configurations.
- **SAC Structural Failure Modes (Degeneracy Zones):**
  - At $\beta_1 = 0$ and $\beta_2 \ge 10$: Objective function misspecification causes catastrophic collapse into low-activity factors.
  - At $(\beta_1 = 0, \beta_2 = 20)$: Collapses into Low-Leverage (30.0%) and Investment (27.9%) (jointly 57.9%). Sharpe collapses to **0.088**, MDD expands to **-14.64%**, $\text{CVaR}_{5\%}$ deepens to **-2.237%**, HHI surges to **0.593**, CR-5 reaches **0.985**.
  - At $(\beta_1 = 0, \beta_2 = 50)$: CR-5 reaches **0.996** (effective single-factor collapse).
  - At $(\beta_1 = 1, \beta_2 = 20)$: Low-Risk factor commands **45.5%** allocation (highest single factor weight across study), $\text{CVaR}_{5\%}$ drops to **-2.505%**, HHI rises to **0.537**.

### Independently reproduced
Not independently reproduced. All reported metrics, comparisons, and parameter surfaces are third-party empirical findings published by Nirvik Sahoo, Chyng Wen Tee, and Paul Robert Griffin (arXiv:2608.14134v1).

### Negative evidence
- **Brittle Operational Windows:** Outside localized sweet spots ($\beta_1 \in \{1, 2\}$ and $\beta_2 \in [0.5, 1]$ at $\beta_1=0$), Dirac-3 performance degrades severely. At $\beta_1 = 0.5$, a momentum spike to 20.6% causes volatility expansion and turnover spikes. At $(\beta_1 = 0, \beta_2 = 20)$, Sharpe drops to 0.421 and MDD expands to -11.09%.
- **Structural Hyper-Concentration:** Dirac-3 portfolios consistently exhibit high concentration (mean HHI 0.228, mean CR-5 0.916, never below 0.825 across either sweep), conflicting with explicit institutional diversification mandates unless active post-optimization constraints are enforced.
- **Reinforcement Learning Mode Collapse:** Unanchored higher-moment penalty shaping causes SAC to suffer catastrophic single-factor collapse (Sharpe 0.088, MDD -14.64%, HHI 0.593), demonstrating that deep RL without hard constraints is unsuitable for unmonitored factor allocation.
- **Cross-Seed Fragility of RL:** High seed variance (Sharpe spread of 0.55 points across random seeds) highlights significant model risk in stochastic actor-critic architectures.

## Falsification plan

Operational tests to disconfirm the proposed mechanism:
1. **Out-of-Sample Rolling Window Validation:** Extend the backtest past the 164-month JKP sample across 2024–2026. Falsified if Dirac-3 fails to sustain Sharpe $> 0.65$ within its calibrated sweet spot $(\beta_1=0, \beta_2=1)$ or if Gurobi fails to maintain $\text{CVaR}_{5\%} > -1.00\%$.
2. **Cardinality and Weight Cap Perturbation:** Enforce a hard constraint that no factor weight may exceed 15% ($w_i \le 0.15$) and CR-5 must remain below 0.65. If capping factor concentration degrades Dirac-3's Sharpe below Gurobi's, it proves that Dirac-3's performance edge is entirely driven by unconstrained factor bets rather than quantum combinatorial optimization advantage.
3. **Execution Latency and Slippage Stress Test:** Impose realistic cloud QPU API turnaround latencies (e.g., 30–60 second delay per rebalance) and simulate slippage scaling with factor portfolio rebalancing volume. If transaction costs $> 40$ bps erase the +0.045 Sharpe premium over Gurobi, the quantum advantage is non-executable.
4. **Placebo / Shuffled Factor Covariance Test:** Shuffle the off-diagonal elements of the factor covariance matrix $\widehat{\bm{\Sigma}}_t$ while preserving diagonal variances. If Dirac-3 continues to output identical factor selections, its heuristic search is unguided by covariance risk structure.
5. **Ablation of Dynamic Turnover Penalty:** Set $\tau_{\text{pen}} = 0$ in the QUBO formulation. If turnover expands beyond 40% monthly and erodes net returns, the dynamic turnover term is the primary driver of realizable alpha rather than the solver technology.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Rationale:** The primary source investigates US equity anomaly factors (JKP 13 library). Porting the QUBO / photonic quantum annealing framework to cryptocurrency requires defining a crypto-native factor universe:
  - Crypto Momentum (cross-sectional return momentum over 7d/30d/90d)
  - Basis / Funding Rate Carry (perpetual funding rate yield spreads)
  - Open Interest Dynamics (leverage expansion / contraction)
  - Liquidity & Volume (bid-ask spread, order book depth, market impact)
  - Tokenomics & Staking Yields
  - Idiosyncratic Volatility (relative to BTC/ETH index benchmarks)
  - Size / Market Capitalization
- **Crypto-Specific Frictions & Risks:**
  - **Rebalancing Horizon:** Monthly rebalancing is too slow for fast-decaying crypto alpha; however, cloud QPU API access latency (Dirac-3 job submission and queue wait times) makes millisecond-to-minute intraday execution unfeasible. A weekly or daily rebalancing schedule is the only feasible operational cadence.
  - **Non-Stationary Covariance:** Crypto factor covariance exhibits extreme regime shifts and correlation breakdown during liquidity cascades (e.g., stablecoin depegs or flash crashes), requiring much faster shrinkage adaptation than rolling 24-month windows.
  - **Shorting & Borrowing Constraints:** Unlike US equities where borrow costs are relatively stable, crypto short borrowing fees on altcoin perpetuals fluctuate violently with funding rates.

## Limitations

- **Hardware-Specific Generational Artifact:** Results reflect a specific photonic hardware generation (Dirac-3, Quantum Computing Inc.) with relaxation schedule $\text{RS}=2$; performance may vary across device revisions or parameterizations.
- **Single Historical Path:** Evaluated on a single 164-month historical realization of JKP factor returns; cross-market validation (e.g., international equities or commodities) was not conducted.
- **Unmodeled API Queuing Latency:** Cloud API turnaround time, job queuing, and communication latency are omitted from backtest accounting.
- **Narrow Calibrated Sweet Spot:** Quantum performance outperformance is confined to a brittle hyperparameter band ($\beta_1 \in \{1,2\}$, $\beta_2 \in [0.5, 1]$); slight parameter shifts trigger factor misallocation.
- **Underspecified Policy Network Architecture:** The exact neural network layer specifications for the SAC agent and the return-forecasting policy network are high-level in the text.

## Implementation status

- **Status:** **not-implemented**.
- **Research Boundary:** This record represents an external research capture of `arXiv:2608.14134v1`. No implementation exists within `nautilus-quant-system`, PyBroker, or NautilusTrader. No strategy family, paper trading, or live execution pipeline has been created or authorized.

## Adoption boundary

- **Status:** **not-approved**.
- **Approval Scope:** **research-only**.
- **Boundary Contract:** This research capture is solely for conceptual analysis and portfolio construction research. It does not constitute approval for capital allocation, paper trading, or live deployment. Any future engineering adoption requires separate formal review, rigorous out-of-sample backtesting, and full execution modeling.

## Related Wiki records

- `[[quant/portfolio-covariance-and-shrinkage-2026-08-28]]` — Classical Ledoit–Wolf shrinkage covariance estimation and numerical conditioning.
- `[[quant/phase9-multifactor-portfolio-attribution-cost-handoff-2026-08-28]]` — Multifactor portfolio attribution, turnover friction, and transaction cost handoffs.
- `[[quant/phase9-factor-covariance-redundancy-risk-decomposition-2026-08-28]]` — Factor redundancy, collinearity, and risk decomposition.
- `[[quant/gaussian-boson-sampling-asset-clustering-statistical-arbitrage-2026-09-02]]` — Photonic quantum computing algorithms (GBS) for combinatorial asset clustering.
- `[[quant/dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]` — Dynamic portfolio optimization under conditional value-at-risk (CVaR) constraints.
- `[[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]]` — Cross-sectional factor evaluation, correlation pruning, and iterative compression in crypto markets.

## Sources

1. Nirvik Sahoo, Chyng Wen Tee, and Paul Robert Griffin, *"Photonic Quantum Computing vs. Classical Solvers in Constrained Factor Portfolio Optimization"*, arXiv preprint `arXiv:2608.14134v1 [q-fin.PM, quant-ph]`, submitted August 14, 2026.
   - Stable Abstract URL: [https://arxiv.org/abs/2608.14134](https://arxiv.org/abs/2608.14134)
   - Full Text HTML: [https://arxiv.org/html/2608.14134v1](https://arxiv.org/html/2608.14134v1)
   - Full Text PDF: [https://arxiv.org/pdf/2608.14134v1](https://arxiv.org/pdf/2608.14134v1)
   - DOI: [10.48550/arXiv.2608.14134](https://doi.org/10.48550/arXiv.2608.14134)
2. T. I. Jensen, B. T. Kelly, and L. H. Pedersen, *"Is there a replication crisis in finance?"*, Journal of Finance 78 (5), pp. 2465–2518 (2023). [Underlying global factor library source for 13 US equity anomaly factors].
3. O. Ledoit and M. Wolf, *"Honey, I shrunk the sample covariance matrix"*, Journal of Portfolio Management 30 (4), pp. 110–119 (2004). [Covariance shrinkage formulation used in Stage 2 QUBO formulation].
4. Quantum Computing Inc., *"Dirac-3 Technical Reference"* (2024). URL: https://quantumcomputinginc.com. [Photonic quantum hardware reference].
5. Gurobi Optimization, LLC, *"Gurobi Optimizer Reference Manual"* (2024). URL: https://www.gurobi.com. [Classical branch-and-bound baseline].
