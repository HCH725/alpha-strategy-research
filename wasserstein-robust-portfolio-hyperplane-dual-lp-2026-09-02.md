---
schema: strategy-research-record-v1
title: "Certified High-Dimensional Wasserstein Robust Portfolio Optimization: Supporting Hyperplane Majorization, Polyhedral Dual LP, and Large-Ambiguity Finite-Threshold Characterization"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - distributionally-robust-optimization
  - wasserstein-metric
  - linear-programming
  - supporting-hyperplanes
  - high-dimensional
status: research-only
confidence: high
source_as_of: 2026-08-12
sources:
  - "Chung-Han Hsieh and Rong Gan, 'Certified High-Dimensional Wasserstein Robust Portfolio Optimization', arXiv preprint arXiv:2608.07032v1 [math.OC], August 12, 2026. DOI: 10.48550/arXiv.2608.07032. Stable URL: https://arxiv.org/abs/2608.07032"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Certified High-Dimensional Wasserstein Robust Portfolio Optimization: Supporting Hyperplane Majorization, Polyhedral Dual LP, and Large-Ambiguity Finite-Threshold Characterization

## Provenance

- **Primary Source:** Chung-Han Hsieh (National Tsing Hua University, Taiwan) and Rong Gan (National Tsing Hua University, Taiwan), *"Certified High-Dimensional Wasserstein Robust Portfolio Optimization"*, arXiv preprint `arXiv:2608.07032v1 [math.OC]`, submitted August 12, 2026. DOI: [10.48550/arXiv.2608.07032](https://doi.org/10.48550/arXiv.2608.07032). Stable URL: [https://arxiv.org/abs/2608.07032](https://arxiv.org/abs/2608.07032).
- **Primary Subject Area:** Optimization and Control (`math.OC`), Computational Engineering (`cs.CE`), Portfolio Management (`q-fin.PM`).
- **Research Funding Context:** Supported in part by the National Science and Technology Council (NSTC), Taiwan, under Grants NSTC113–2628–E–007–015– and NSTC114–2628–E-007–006–.
- **Context & Motivation:** In data-driven portfolio management, Sample Average Approximation (SAA) replaces the unknown true return distribution $\mathbb{F}$ with the empirical distribution $\widehat{\mathbb{F}} = \frac{1}{N} \sum_{j=1}^N \delta_{\widehat{X}_j}$. SAA finite-sample optimizers amplify estimation error and produce fragile out-of-sample allocations (the classical Markowitz error-maximization phenomenon). Distributionally Robust Optimization (DRO) with an order-1 Wasserstein ambiguity set allows probability mass to transport to arbitrary points within the compact return support $\mathfrak{X}$, rather than merely reweighting observed historical scenarios. However, standard Kantorovich duality yields a semi-infinite convex program whose support constraints range over the continuum $\mathfrak{X}$. While an exact sample-specific vertex reformulation exists for long-only box supports under an $\ell_1$ ground norm, it requires up to $N 2^n$ vertex constraints, rendering high-dimensional portfolio rebalancing ($n \ge 100$) computationally intractable via direct vertex enumeration. Hsieh and Gan solve this tractability bottleneck by majorizing the concave utility with supporting hyperplanes, dualizing the support subproblems via strong LP duality, and proving a uniform utility-approximation certificate that bounds the robust-value error and near-optimality gap.

## Economic mechanism

### Source-reported

1. **Adversarial Distributional Shift Protection:** The investor optimizes against the worst-case distribution $\mathbb{Q}$ within an order-1 Wasserstein ball of radius $\varepsilon$ centered at the empirical return distribution $\widehat{\mathbb{F}}$. The optimal transport ground metric $\ell_1$ penalizes probability mass migration across asset returns, protecting the allocation against asset co-movement breakdown, non-Gaussian tails, and estimation errors in expected growth.
2. **Supporting Hyperplane Majorization:** For any concave, strictly increasing utility function $U(\langle w, x \rangle)$ (e.g., logarithmic Kelly growth $U(y) = \log(1+y)$), the nonlinear curve on the compact scalar return range $[\underline{y}, \overline{y}]$ is upper-approximated by $M$ supporting tangent hyperplanes $h_m(y) = \alpha_m y + \beta_m$. Because each hyperplane is affine, the inner worst-case support minimization can be dualized exactly using linear programming duality.
3. **Finite-Threshold Large-Ambiguity Conservatism:** When the ambiguity radius $\varepsilon$ exceeds the support diameter $\bar{\varepsilon} = \sup_{x, x' \in \mathfrak{X}} \|x - x'\|$, the Wasserstein ball expands to the entire probability simplex over the support ($\mathcal{B}_\varepsilon(\widehat{\mathbb{F}}) = \mathcal{M}(\mathfrak{X})$). In this regime, the robust portfolio allocation collapses into a closed-form maximin rule maximizing worst-case support returns $\max_{w \in \Delta_n} \langle w, x_{\min} \rangle$. For symmetric support bounds $x_{\min} = c \mathbf{1}$, every feasible portfolio becomes optimal, recovering conservative diversification.

### Research interpretation

The falsifiable thesis is that **replacing heuristic covariance shrinkage or unconstrained SAA with certified Wasserstein-hyperplane LP optimization produces statistically superior out-of-sample Sharpe and Calmar ratios while maintaining sub-second solver latency on high-dimensional universes ($n \ge 476$)**:
- Rather than solving computationally prohibitive exponential-cone programs or relying on constraint-generation cutting planes that require multiple solver iterations, the entire robust expected-utility problem is collapsed into a single polynomial-size linear program of dimension $O(n N \eta^{-1/2})$.
- The Wasserstein radius $\varepsilon$ functions as an explicit behavioral dial: small $\varepsilon \approx 10^{-4}$ tracks aggressive SAA growth, moderate $\varepsilon \approx 10^{-2}$ maximizes risk-adjusted compounding by mitigating sample overfit, and large $\varepsilon \ge 1.0$ converges to conservative near-equal weighting.

## Signal

### 1. Primal Wasserstein Distributionally Robust Formulation

Let $X \in \mathbb{R}^n$ be a random return vector with support on a bounded polyhedral set:
$$\mathfrak{X} = \{x \in \mathbb{R}^n : H x \le h\}, \quad H \in \mathbb{R}^{r_\mathfrak{X} \times n}, \; h \in \mathbb{R}^{r_\mathfrak{X}}$$
For box support $\mathfrak{X}_{\text{box}} = \{x \in \mathbb{R}^n : x_{\min} \le x \le x_{\max}\}$, $H = [I; -I] \in \mathbb{R}^{2n \times n}$ and $h = [x_{\max}; -x_{\min}]$.

Given $N$ historical i.i.d. observations $\widehat{X}_1, \dots, \widehat{X}_N$, the empirical distribution is $\widehat{\mathbb{F}} = \frac{1}{N} \sum_{j=1}^N \delta_{\widehat{X}_j}$. For radius $\varepsilon > 0$, the order-1 Wasserstein ambiguity set under the $\ell_p$ ground norm is:
$$\mathcal{B}_\varepsilon(\widehat{\mathbb{F}}) = \left\{ \mathbb{F} \in \mathcal{M}(\mathfrak{X}) : d_p(\mathbb{F}, \widehat{\mathbb{F}}) \le \varepsilon \right\}$$
The primal DRO problem selects portfolio weights $w \in \mathcal{W} \subseteq \Delta_n = \{w \ge 0 : w^\top \mathbf{1} = 1\}$ to maximize worst-case expected utility:
$$V^\star(\varepsilon) = \sup_{w \in \mathcal{W}} \inf_{\mathbb{F} \in \mathcal{B}_\varepsilon(\widehat{\mathbb{F}})} \mathbb{E}^\mathbb{F} [U(\langle w, X \rangle)]$$
where $U(y) = \log(1 + y)$ represents the logarithmic growth (Kelly) utility.

### 2. Supporting Hyperplane Approximation and Uniform Error Certificate

For scalar return $y = \langle w, x \rangle \in [\underline{y}, \overline{y}]$, let $f(y) = U(y)$. For integer $M \ge 2$, partition the interval $\underline{y} = y_1 < y_2 < \dots < y_M = \overline{y}$. Define tangent affine hyperplanes:
$$h_m(y) = \alpha_m y + \beta_m = f(y_m) + f'(y_m)(y - y_m), \quad m = 1, \dots, M$$
By concavity of $f$, $f(y) \le h_m(y)$, yielding the upper majorant surrogate:
$$\widehat{U}_M(y) = \min_{1 \le m \le M} (\alpha_m y + \beta_m)$$
If $f'$ is Lipschitz continuous with constant $L_f$ on $[\underline{y}, \overline{y}]$, setting subinterval mesh width $\Delta_y \le \sqrt{8\eta / L_f}$ guarantees a uniform approximation certificate:
$$0 \le \widehat{U}_{M_\eta^\star}(y) - U(y) \le \eta, \quad \forall y \in [\underline{y}, \overline{y}]$$
This bounds both the robust value and the near-optimality gap:
$$V^\star(\varepsilon) \le \widehat{V}_\eta^\star(\varepsilon) \le V^\star(\varepsilon) + \eta$$
$$\inf_{\mathbb{F} \in \mathcal{B}_\varepsilon(\widehat{\mathbb{F}})} \mathbb{E}^\mathbb{F} [U(\langle \widehat{w}_\eta, X \rangle)] \ge V^\star(\varepsilon) - \eta$$

### 3. General Finite Hyperplane-Dual Program (Theorem 3.6)

Substituting $\widehat{U}_{M_\eta^\star}$ into the Kantorovich dual and dualizing the support subproblem via LP strong duality yields the finite norm-constrained convex program:
$$\max_{w \in \mathcal{W}, \, \lambda \ge 0, \, a \in \mathbb{R}^N, \, \mu_j^m \in \mathbb{R}_{+}^{r_\mathfrak{X}}} \lambda \varepsilon + \frac{1}{N} \sum_{j=1}^N a_j$$
subject to:
$$a_j + \langle \mu_j^m, h \rangle + \alpha_m \langle w, \widehat{X}_j \rangle + \langle H^\top \mu_j^m, \widehat{X}_j \rangle \le \beta_m, \quad \forall j=1,\dots,N, \; m=1,\dots,M_\eta^\star$$
$$\|-\alpha_m w - H^\top \mu_j^m\|_* \le \lambda, \quad \forall j=1,\dots,N, \; m=1,\dots,M_\eta^\star$$
where $\|\cdot\|_*$ is the dual norm of the ground norm $\ell_p$. For $p=1$, the dual norm is $\ell_\infty$.

### 4. Box-Specialized Robust Linear Program (Corollary 3.7)

Under $\ell_1$ ground metric, long-only simplex $\mathcal{W} \subseteq \mathbb{R}_+^n$, and box support $\mathfrak{X}_{\text{box}} = [x_{\min}, x_{\max}]$, the dual multipliers simplify in closed form. Introducing auxiliary slack vectors $s^m \in \mathbb{R}_+^n$, the entire problem reduces to a single Linear Program:
$$\max_{w \in \mathcal{W}, \, \lambda \ge 0, \, a \in \mathbb{R}^N, \, s^m \in \mathbb{R}_+^n} \lambda \varepsilon + \frac{1}{N} \sum_{j=1}^N a_j$$
subject to:
$$a_j + \langle \widehat{X}_j - x_{\min}, s^m \rangle - \alpha_m \langle w, \widehat{X}_j \rangle + \lambda \langle \mathbf{1}, \widehat{X}_j - x_{\min} \rangle \le \beta_m, \quad \forall j=1,\dots,N, \; m=1,\dots,M_\eta^\star$$
$$s^m \ge \alpha_m w - \lambda \mathbf{1}, \quad \forall m=1,\dots,M_\eta^\star$$
$$s^m \ge \mathbf{0}, \quad \forall m=1,\dots,M_\eta^\star$$
Total decision variables: $n + 1 + N + n M_\eta^\star$. For $N=20, M=5$, total scalar variables equal $6n + 21$.

### 5. Large-Ambiguity Closed-Form Optimizer (Theorem 3.13 & Corollary 3.15)

For $\varepsilon \ge \bar{\varepsilon} = \sup_{x, x' \in \mathfrak{X}} \|x - x'\|_1$, the optimal solution set collapses to:
$$\mathcal{W}^* = \operatorname{conv} \{ e_i \in \mathbb{R}^n : i \in \arg\max_{1 \le k \le n} (x_{\min})_k \}$$
When $x_{\min} = c \mathbf{1}$, $\mathcal{W}^* = \Delta_n$, and the equal-weight allocation $w = \frac{1}{n} \mathbf{1}$ is within the optimal set.

## Required data

- **Universe:** Cross-sectional asset baskets (e.g., 475 S&P 500 equities + 1-month U.S. Treasury yield proxy; scalable up to 1,000 assets).
- **Timeframe:** Daily adjusted closing prices for estimating monthly return distribution; monthly rebalancing execution cadence.
- **Data Fields:** Daily total returns $R_{t,i}$, historical observation matrix $\widehat{X} \in \mathbb{R}^{N \times n}$ over rolling lookback window $N \in [20, 252]$ trading days.
- **Support Bounds:** Box support bounds $x_{\min}, x_{\max} \in \mathbb{R}^n$ estimated per rolling window as sample-wide minimum and maximum returns, clipped to avoid unbounded growth or negative asset prices ($x_{\min} > -\mathbf{1}$).
- **Risk-Free Rate:** 1-Month Constant Maturity Market Yield on U.S. Treasury Securities (FRED), integrated as an additional asset column.

## Execution assumptions

- **Execution Cadence:** Monthly discrete rebalancing at closing mark prices. The portfolio weight vector $w_t^*$ optimized on month $t-1$ returns is executed and held through month $t$.
- **Order Model:** Full rebalance at market on close / VWAP.
- **Transaction Costs:** Proportional turnover fee schedule modeled ex-post across tiers: $0.0\%$, $0.1\%$, $0.2\%$, and $0.3\%$ ($10, 20, 30$ bps) applied to risky-asset turnover $\mathrm{Turnover}_t = \sum_{i=1}^{n-1} |w_{t,i} - w_{t-1,i}^+|$, where buy-and-hold benchmarks incur zero subsequent turnover.
- **Short-Sale & Margin:** Long-only cash-financed simplex constraints ($w \ge 0, \sum w_i = 1$). No leverage, no borrowing costs.
- **Solver Architecture:** Linear programming solver (MOSEK / HiGHS / Clp) via CVXPY interface; single LP solve per rebalance without outer iterative loops.

## Evidence

### Source-reported

All quantitative figures below are directly reported by Chung-Han Hsieh and Rong Gan (arXiv:2608.07032v1, August 2026):

1. **11-Asset Single-Period Benchmark (10 S&P 500 Mega-caps + 1 Risk-Free Asset, Jan-Mar 2022):**
   - Assets: AAPL, MSFT, AMZN, GOOG, GOOGL, UNH, JNJ, XOM, BRK.B, JPM, and 1-Month Treasury Yield.
   - Prescribed tolerance: $\eta = 10^{-3}$.
   - Numerical Fidelity: Maximum observed robust-value gap between $\texttt{DRO}_{\texttt{HYP}}$ and exact sample-specific vertex formulation $\texttt{DRO}_{\texttt{EX}}$ was **$1.38 \times 10^{-4}$**, strictly below tolerance $\eta = 10^{-3}$. Absolute discrepancy against RSOME implementation was **$1.96 \times 10^{-12}$**.
   - Computation Time: Mean solve time across the Wasserstein radius grid was **0.009 seconds** for $\texttt{DRO}_{\texttt{HYP}}$, compared with **3.702 seconds** for exact $\texttt{DRO}_{\texttt{EX}}$ (**413x speedup**) and **0.504 seconds** for $\texttt{RSOME}_{\texttt{HYP}}$ (**56x speedup**).

2. **476-Asset Rolling Rebalancing Backtest (Jan 2021 – Dec 2025, 60 Monthly Decisions):**
   - Universe: 475 S&P 500 constituents with complete price history + 1-Month Treasury Yield ($n=476$).
   - Solve Latency: Across 300 solves (60 months $\times$ 5 radii), mean solve time was **0.065s**, median was **0.044s**, 90th percentile was **0.137s**, and maximum was **0.534s**.
   - Out-of-Sample Performance (Zero Cost):
     - At small radius $\varepsilon = 10^{-4}$: Cumulative Return (CR) = **4.77**, annualized volatility $\sigma = \mathbf{0.46}$, Maximum Drawdown (MDD) = **0.38** (closely matching SAA: $\text{CR}=5.18, \sigma=0.46, \text{MDD}=0.38$).
     - At moderate radius $\varepsilon = 10^{-2}$: **Sharpe Ratio = 1.11**, **Calmar Ratio = 1.34** (highest risk-adjusted performance among all tested DRO radii).
     - At large radius $\varepsilon = 1.0$: $\text{CR} = \mathbf{0.81}, \sigma = \mathbf{0.16}, \text{MDD} = \mathbf{0.20}$ (closely matching equal-weight buy-and-hold $\text{EW(BH)}$: $\text{CR}=0.83, \sigma=0.16, \text{MDD}=0.20$).
   - Transaction Cost Sensitivity: At $0.1\%, 0.2\%$, and $0.3\%$ cost levels, the $\varepsilon = 10^{-2}$ policy retained the highest Sharpe and Calmar ratios among all rebalanced policies.

3. **Controlled Scalability Benchmark (Dimensions $n=10$ to $n=1000$, $N=20$, $M=5$, $\eta=10^{-3}$, 10 Replications):**
   - At $n=10$: Median solve time was **0.0078s** for $\texttt{DRO}_{\texttt{HYP}}$ vs **0.1253s** for $\texttt{DRO}_{\texttt{EX-CG}}$ (constraint generation).
   - At $n=476$: Median solve time was **0.0580s** vs **1.3076s** (**22.53x speedup**).
   - At $n=1000$: Median solve time was **0.1279s** vs **4.6461s** (**36.32x speedup**).
   - Maximum robust-value gap observed across all synthetic replications was **$2.29 \times 10^{-4}$**, confirming the certified tolerance $\eta = 10^{-3}$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed paper; absence is not evidence of no negative result.
- Authors note that at large ambiguity radii ($\varepsilon \ge 1.0$), periodic rebalancing incurs unnecessary turnover costs from portfolio drift without adding alpha over a passive equal-weight buy-and-hold strategy.
- When transaction costs reach $0.3\%$, aggressive rebalancing under small radii ($\varepsilon \le 10^{-3}$) experiences rapid degradation in realized Sharpe and cumulative return due to excessive turnover.

## Falsification plan

1. **Wasserstein Radius Sensitivity Sweep ($\varepsilon \in [10^{-5}, 10^1]$):** Verify whether intermediate radii ($\varepsilon \in [5 \times 10^{-3}, 5 \times 10^{-2}]$) consistently outperform SAA and equal-weight benchmarks out of sample. If the performance curve is monotonically decreasing or fails to beat $1/N$ after transaction costs across multiple market regimes, the distributionally robust diversification hypothesis is falsified.
2. **Support Boundary Misspecification Stress:** In volatile regimes, asset returns may breach estimated historical box bounds $[x_{\min}, x_{\max}]$. Introduce outlier shocks (returns exceeding $x_{\min}$ by $2\sigma$); evaluate whether truncation distortion invalidates the hyperplane error bound $\eta$.
3. **Turnover & Execution Slippage Hurdle:** Apply realistic execution slippage ($2\text{ bps}$ per trade) alongside $10\text{ bps}$ fees. If monthly turnover exceeds $40\%$ and reduces net Sharpe ratio below $0.6$, the LP formulation requires an explicit turnover-penalty constraint.
4. **Rejection Threshold:** Reject the strategy if out-of-sample annualized Sharpe ratio drops below $0.5$ or maximum drawdown exceeds $30\%$ over a 3-year walk-forward test.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Cross-Sectional Spot/Perp Baskets:** The LP formulation can be ported to top 50–100 liquid crypto perpetual contracts or spot assets (e.g., Binance USDT perps).
- **Fat-Tailed Return Regimes:** Crypto return distributions exhibit severe excess kurtosis, jump diffusion, and regime switches. The box support $[x_{\min}, x_{\max}]$ must be dynamic (e.g., EVT-calibrated or rolling percentile bounds) to prevent support clipping during liquidation cascades.
- **Continuous 24/7 Rebalancing:** Unlike monthly equity schedules, crypto volatility requires weekly or bi-weekly rebalancing epochs to adapt to non-stationary funding and momentum regimes.
- **Funding & Borrow Costs:** In perpetual markets, funding rates introduce asymmetric carrying costs that must be integrated into the net expected return vector prior to LP optimization.

## Limitations

- **Long-Only Box Specialization:** The linear programming reduction (Corollary 3.7) relies strictly on an $\ell_1$ ground norm, long-only portfolio simplex $\mathcal{W} \subseteq \mathbb{R}_+^n$, and compact box support. For short-selling, general polyhedral cones, or $\ell_2$ ground metrics, the formulation requires second-order cone programming (SOCP) or full polyhedral dual variables ($2nNM$ variables).
- **Static In-Sample Estimation:** SAA sample size $N$ is fixed to monthly windows ($N=20$); temporal dependence, autocorrelation, and GARCH volatility clustering are not modeled within the empirical distribution measure.
- **Turnover Omission in Objective:** Transaction costs are evaluated ex-post rather than integrated directly into the primal objective function, necessitating manual radius tuning to balance turnover against diversification.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/portfolio-bayesian-parametric-policies-policy-risk-regularization-2026-09-02]]`
- `[[quant/observable-matrix-dynamics-portfolio-optimization-2026-09-02]]`
- `[[quant/path-portfolio-optimization-signature-defect-lift-2026-09-02]]`

## Sources

1. Chung-Han Hsieh and Rong Gan, *"Certified High-Dimensional Wasserstein Robust Portfolio Optimization"*, arXiv preprint `arXiv:2608.07032v1 [math.OC]`, August 12, 2026. DOI: [10.48550/arXiv.2608.07032](https://doi.org/10.48550/arXiv.2608.07032). Stable URL: [https://arxiv.org/abs/2608.07032](https://arxiv.org/abs/2608.07032).
