---
schema: strategy-research-record-v1
title: "Entropic Value-at-Risk Portfolio Optimization for Tempered Stable Lévy Processes: Parametric EVaR, E-STAR, and E-Rachev Allocation"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - entropic-value-at-risk
  - tempered-stable-levy
  - normal-tempered-stable
  - classical-tempered-stable
  - independent-component-analysis
  - tail-risk
  - sector-etfs
status: research-only
confidence: medium
source_as_of: 2026-08-18
sources:
  - "Jaehyung Choi, 'Entropic Value-at-Risk portfolio optimization for tempered stable Lévy processes', arXiv:2608.18022v1 [q-fin.PM, q-fin.RM], August 18, 2026. DOI: 10.48550/arXiv.2608.18022. Stable URL: https://arxiv.org/abs/2608.18022. Full text: https://arxiv.org/html/2608.18022v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Entropic Value-at-Risk Portfolio Optimization for Tempered Stable Lévy Processes: Parametric EVaR, E-STAR, and E-Rachev Allocation

## Provenance

- **Primary Source:** Jaehyung Choi, *"Entropic Value-at-Risk portfolio optimization for tempered stable Lévy processes"*, arXiv preprint `arXiv:2608.18022v1 [q-fin.PM, q-fin.RM]`, submitted August 18, 2026.
- **Canonical DOI:** [10.48550/arXiv.2608.18022](https://doi.org/10.48550/arXiv.2608.18022)
- **Traceable Source URL:** `https://arxiv.org/abs/2608.18022` / HTML full text: `https://arxiv.org/html/2608.18022v1`
- **Author Contact / Provenance:** Jaehyung Choi (`jj.jaehyung.choi@gmail.com`).

## Economic mechanism

### Source-reported

Classical portfolio selection balances expected return against variance (Markowitz mean-variance), which treats upside volatility identically to downside volatility and ignores heavy tails and skewness. Downside risk measures such as Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR / Expected Shortfall) address this asymmetry, but VaR is non-coherent and ignores loss severity beyond the quantile threshold, while CVaR only captures average tail losses beyond a single cutoff. 

Entropic Value-at-Risk (EVaR), introduced by Ahmadi-Javid (2012) via the Chernoff inequality, is the tightest coherent upper bound on both VaR and CVaR. Derived from the moment-generating function (MGF), EVaR reflects the entire tail behavior and has an information-theoretic dual representation based on Kullback-Leibler divergence. However, parametric EVaR portfolio optimization has historically been intractable for multivariate heavy-tailed distributions because the portfolio return distribution and its admissible MGF domain change with every candidate weight vector $\boldsymbol{w}$.

Choi (2026) develops parametric EVaR portfolio optimization for tempered stable Lévy processes—specifically Classical Tempered Stable (CTS) and Normal Tempered Stable (NTS) distributions—which model fat tails and skewness while possessing finite MGFs on parameter-dependent domains. The author derives closed-form portfolio cumulant-generating functions and weight-dependent admissible domains under two multivariate constructions:
1. **Multivariate Normal Tempered Stable (MNTS) Projection:** Capitalizes on closure under linear projection. Any portfolio combination $\boldsymbol{w}^T \boldsymbol{X}$ is analytically another univariate NTS process, allowing direct evaluation of portfolio EVaR without refitting.
2. **Independent Component Analysis (ICA) Factorization:** Decomposes asset returns into statistically independent components with fitted CTS or NTS marginals. The portfolio cumulant is the linear combination of component cumulants, evaluated over the intersection of component-level admissible MGF domains.

Using these expressions, the paper formulates and solves minimum-EVaR, Entropic Stable Tail Adjusted Return (E-STAR, maximizing return per unit of EVaR downside risk), and Entropic Rachev (E-Rachev, maximizing entropic upper-tail reward over entropic downside-tail risk) portfolio optimizations.

### Research interpretation

The economic alpha mechanism is risk-adjusted factor/sector allocation driven by asymmetric heavy-tail modeling:

1. **Superior Tail-Risk Bound:** EVaR penalizes extreme tail events more strictly than CVaR because the exponential weighting of the Chernoff bound accounts for catastrophic outliers beyond conventional 95% or 99% cutoffs. In equity sector allocations, portfolios optimized for minimum EVaR naturally tilt away from assets with severe negative skewness or fragile jump distributions during pre-crisis stress periods.
2. **Dimension Reduction Without Re-Estimation Bias:** Traditional parametric tail optimization requires re-fitting the portfolio distribution for every weight iteration, introducing substantial estimation noise and numerical instability. By expressing the portfolio MGF directly through MNTS projection or ICA mixing matrices, the optimizer operates on a fixed, pre-estimated parameter manifold, avoiding optimizer overfitting.
3. **Decoupling Downside Penalization from Upside Truncation:** While minimum-variance strategies penalize large positive returns as volatility, E-STAR and E-Rachev explicitly differentiate upside jump potential from downside crash risk, permitting high exposure to right-skewed recovery sectors while hedging left-tail collapse.

## Signal

The allocation engine executes a monthly parametric risk-measure optimization over a rolling 12-month estimation window:

- **Formation Timestamp & Cadence:** Monthly rebalance. In-sample parameter estimation uses the preceding 12 months (252 trading days) of daily adjusted close returns. Positions are held fixed for one calendar month ($l = 1\text{ month}$).
- **Universe & Data Inputs:** Vector of daily simple asset returns $\boldsymbol{X}_t \in \mathbb{R}^N$ for $t = 1, \ldots, T$.
- **Distributional Fitting (Executed at each monthly rebalance):**
  - **MNTS Model:**
    - Fit univariate NTS distribution $\text{NTS}(\alpha_i, \theta_i, \beta_i, \gamma_i, \mu_i)$ to each asset return series using the empirical cumulative distribution function mean squared error (ECDF-MSE) estimator.
    - Set common tempered stable subordinator parameters $(\alpha, \theta)$ to the cross-sectional mean of marginal estimates.
    - Re-estimate marginal skewness $\beta_i$, scale $\gamma_i$, and location $\mu_i$ conditional on $(\alpha, \theta)$.
    - Estimate Brownian correlation matrix $\boldsymbol{\rho}$ from the sample covariance matrix matching second moments.
  - **ICA Model (ICA-NTS / ICA-CTS):**
    - Center in-sample returns: $\boldsymbol{X} - \boldsymbol{m}\mathbf{1}^T$.
    - Apply FastICA (Hyvärinen and Oja, 2000) to estimate unmixing matrix $\mathbf{G} \in \mathbb{R}^{N \times N}$ and mixing matrix $\mathbf{A} = \mathbf{G}^{-1}$, recovering $N$ independent components $\boldsymbol{S}_t$.
    - Fit univariate NTS or CTS distributions independently to each component using ECDF-MSE.
- **Portfolio Cumulant & Admissible Domain Construction:**
  - **MNTS Projected Portfolio:**
    - Projected parameters: $\bar{\alpha} = \alpha$, $\bar{\theta} = \theta$, $\bar{\beta} = \boldsymbol{w}^T \boldsymbol{\beta}$, $\bar{\gamma}^2 = \boldsymbol{w}^T \boldsymbol{\Sigma} \boldsymbol{w}$ (where $\boldsymbol{\Sigma} = \text{diag}(\boldsymbol{\gamma}) \boldsymbol{\rho} \text{diag}(\boldsymbol{\gamma})$), $\bar{\mu} = \boldsymbol{w}^T \boldsymbol{\mu}$.
    - Admissible MGF domain: $u \in \mathcal{U}_{\text{MNTS}}(\boldsymbol{w}) = \left(0, \frac{\sqrt{\bar{\beta}^2 + 2\bar{\theta}\bar{\gamma}^2} - \bar{\beta}}{\bar{\gamma}^2}\right)$.
    - Portfolio EVaR: $\text{EVaR}_{1-\eta}^{\text{MNTS}}(\boldsymbol{w}^T \boldsymbol{X}) = \inf_{u \in \mathcal{U}_{\text{MNTS}}(\boldsymbol{w})} \frac{\Psi_{X_t}^{\text{NTS}}(-u; \bar{\alpha}, \bar{\theta}, \bar{\beta}, \bar{\gamma}, \bar{\mu}) - \ln \eta}{u}$.
  - **ICA Projected Portfolio:**
    - Projected component exposures: $\tilde{\boldsymbol{w}} = \mathbf{A}^T \boldsymbol{w}$.
    - Portfolio cumulant: $\Psi_{\boldsymbol{w}^T \boldsymbol{X}_t}(-u) = -u t \boldsymbol{w}^T \boldsymbol{m} + \sum_{i=1}^N \Psi_{S_t^{(i)}}(-u \tilde{w}_i)$.
    - Admissible domain: $\mathcal{U}_{\text{ICA}}(\boldsymbol{w}) = \left(0, \min_{i: u_{i,\max} > 0} \frac{u_{i,\max}}{|\tilde{w}_i|}\right)$, where for NTS: $u_{i,\max} = \frac{\sqrt{\beta_i^2 + 2\theta_i \gamma_i^2} - \beta_i \text{sgn}(\tilde{w}_i)}{\gamma_i^2}$.
- **Portfolio Optimization Objectives:**
  - **Feasible Set:** Long-only, fully invested: $\mathcal{W} = \{\boldsymbol{w} \in \mathbb{R}^N : \boldsymbol{w} \ge 0, \boldsymbol{w}^T \boldsymbol{e} = 1\}$.
  - **1. Minimum-EVaR:**
    $$\min_{\boldsymbol{w} \in \mathcal{W}} \text{EVaR}_{1-\eta}^\mathcal{A}(\boldsymbol{w}^T \boldsymbol{X})$$
    Solved via the perspective reciprocal transform $v = 1/u$, which is strictly jointly convex in $(\boldsymbol{w}, v)$.
  - **2. E-STAR Ratio (Entropic Stable Tail Adjusted Return):**
    $$\max_{\boldsymbol{w} \in \mathcal{W}} \frac{\mathbb{E}[\boldsymbol{w}^T \boldsymbol{X}]}{\text{EVaR}_{1-\eta}^\mathcal{A}(\boldsymbol{w}^T \boldsymbol{X})}$$
    Solved via Dinkelbach fractional programming iterations.
  - **3. E-Rachev Ratio (Symmetric / Asymmetric):**
    $$\max_{\boldsymbol{w} \in \mathcal{W}} \frac{\text{EVaR}_{1-\zeta}^\mathcal{A}(-\boldsymbol{w}^T \boldsymbol{X})}{\text{EVaR}_{1-\eta}^\mathcal{A}(\boldsymbol{w}^T \boldsymbol{X})}$$
    Symmetric uses $\zeta = \eta = 0.05$ (95% upper/lower tail). Asymmetric uses $\zeta = 0.50$ (median/upside) vs. $\eta = 0.05$. Solved via multi-start sequential least-squares programming (SLSQP).
- **Execution:** Drift-adjusted rebalancing to target weights $\boldsymbol{w}_t^*$ at the close of the first trading day of each month.

## Required data

- **Instruments:** 11 State Street Select Sector SPDR ETFs:
  - Original 9 funds (inception Dec 1998): XLE (Energy), XLF (Financials), XLU (Utilities), XLI (Industrials), XLK (Technology), XLV (Health Care), XLY (Consumer Discretionary), XLP (Consumer Staples), XLB (Materials).
  - Added funds: XLRE (Real Estate, added in 2015) and XLC (Communication Services, added in 2018).
  - Each fund enters the investable universe after 12 months of trading history.
- **Timeframe / Sampling:** Daily dividend-adjusted closing prices.
- **Sample Period:** January 2000 through March 2026 (approx. 26 years out-of-sample). Initial 12-month estimation window spans 1999.
- **Fields:** Adjusted daily close prices, dividend-reinvested returns.
- **Data Vendor:** Yahoo Finance.

## Execution assumptions

- **Execution Cadence:** Monthly rebalancing at month-end / first trading day.
- **Holding Period:** 1 month fixed holding period between rebalancing dates.
- **Turnover Tracking:** One-way turnover measured at each rebalance date: $\text{TO}_t = \frac{1}{2} \sum_{i=1}^N |w_{i,t} - \tilde{w}_{i,t^-}|$, where $\tilde{w}_{i,t^-}$ is the drift-adjusted weight immediately prior to rebalancing.
- **Transaction Costs:** Evaluated at 0 bps (gross), 5 bps, 10 bps, and 25 bps per trade.
- **Shorting / Leverage:** Long-only ($w_i \ge 0$), zero leverage ($\sum w_i = 1$). No borrow fees incurred.

## Evidence

### Source-reported

All performance figures below are transcribed directly from Choi (arXiv:2608.18022v1, August 2026), evaluated over the 26-year out-of-sample period (January 2000 to March 2026, lookback=12m, holding=1m):

**Table 8: Full Out-of-Sample Performance (January 2000 – March 2026):**
- **Top Performer — ICA++NTS Minimum-EVaR ($\text{EVaR}_{95}^{\text{NTS}}$):**
  - Cumulative Return: **766.96%**
  - CAGR: **8.60%**
  - Annualized Volatility: **15.28%**
  - Annualized Sharpe Ratio: **0.616** (highest gross Sharpe in entire 31-strategy study)
  - Sortino Ratio: **0.880**
  - Maximum Drawdown: **38.30%**
  - Calmar Ratio: **0.224**
  - Historical 95% VaR: **1.38%**
  - Historical 95% CVaR: **2.21%**
  - Skewness: **0.069** | Excess Kurtosis: **18.435**
- **Matched Benchmark — ICA++NTS Minimum-CVaR ($\text{CVaR}_{95}^{\text{NTS}}$):**
  - Cumulative Return: **495.43%**
  - CAGR: **7.05%**
  - Annualized Volatility: **14.22%**
  - Annualized Sharpe Ratio: **0.550**
  - Sortino Ratio: **0.776**
  - Maximum Drawdown: **37.79%**
  - Calmar Ratio: **0.187**
  - Historical 95% VaR: **1.32%** | Historical 95% CVaR: **2.09%**
  - *EVaR vs. CVaR Spread:* EVaR outperforms matched CVaR by **+0.066 Sharpe** and **+271.53 percentage points** cumulative return.
- **Standard Allocation Benchmarks:**
  - **Equal Weight (EW):** Cumulative Return: 735.31%, CAGR: 8.44%, Ann. Vol: 18.16%, Sharpe: **0.537**, Sortino: 0.754, Max DD: **53.51%**, Calmar: 0.158.
  - **Global Minimum Variance (MinVar):** Cumulative Return: 509.64%, CAGR: 7.15%, Ann. Vol: 14.15%, Sharpe: **0.559**, Sortino: 0.786, Max DD: **37.36%**, Calmar: 0.191.
  - **Maximum Sharpe (MaxSharpe):** Cumulative Return: 604.55%, CAGR: 7.74%, Ann. Vol: 19.81%, Sharpe: **0.476**, Sortino: 0.668, Max DD: **51.74%**, Calmar: 0.150.
- **Alternative EVaR Specifications:**
  - **Normal Minimum-EVaR ($\text{EVaR}_{95}^{\text{Normal}}$):** Return: 506.49%, Sharpe: 0.558, Max DD: 37.27% (essentially identical to MinVar).
  - **MNTS Minimum-EVaR ($\text{EVaR}_{95}^{\text{MNTS}}$):** Return: 499.57%, Sharpe: 0.555, Max DD: 37.77%.
  - **ICA++CTS Minimum-EVaR ($\text{EVaR}_{95}^{\text{CTS}}$):** Return: 645.76%, Sharpe: 0.572, Max DD: 39.21%.
  - **Symmetric MNTS E-Rachev ($\text{E-Rachev}_{95,95}^{\text{MNTS}}$):** Highest cumulative return in study: **976.15%** (CAGR 9.50%), but at the expense of extreme volatility (26.68%) and severe Max Drawdown (**77.59%**), resulting in Sharpe of 0.474.

**Transaction Cost Sensitivity (Table 14 & Table 16):**
- **ICA++NTS Minimum-EVaR Net Sharpe Ratios:**
  - 0 bps: **0.616**
  - 5 bps: **0.608**
  - 10 bps: **0.599**
  - 25 bps: **0.573** (still exceeds gross MinVar 0.559, EW 0.537, and MaxSharpe 0.476).
- **Turnover (Table 13):**
  - ICA++NTS Minimum-EVaR mean monthly turnover is **21.67%** (median 18.25%), compared to 9.52% for MinVar and 1.35% for EW.
  - Rachev portfolios exhibit much higher turnover (59.18% to 64.74% for ICA-based specifications).

**Regime Robustness (Table 15 & Table 17):**
- **Global Financial Crisis (GFC, 2007-10 to 2009-02):**
  - ICA++NTS Minimum-EVaR lost **-12.18%**.
  - Matched Minimum-CVaR lost **-17.61%**.
  - MinVar lost **-18.60%**.
  - Equal Weight lost **-33.77%**.
- **Post-GFC Recovery (2009-03 to 2019-12):**
  - ICA++NTS Minimum-EVaR gained **+364.59%** vs. +289.84% for Minimum-CVaR.
- **COVID-and-Inflation Period (2020-01 to 2022-12):**
  - ICA++NTS Minimum-EVaR gained **+58.73%** vs. +26.96% for Minimum-CVaR.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Turnover Drag on Aggressive Reward-Risk Objectives:** While Minimum-EVaR turnover is manageable (21.67% monthly), E-Rachev and Rachev ratio portfolios exhibit monthly turnover exceeding 60%, causing net Sharpe to degrade rapidly as transaction costs approach 25 bps.
- **MNTS Formulation Parity with CVaR:** Under the shared-subordinator MNTS approach, EVaR and CVaR Sharpe differences were virtually zero (+0.001 to +0.003), indicating that the benefits of EVaR over CVaR require the flexible component-level marginal parameters afforded by ICA rather than a single joint subordinator.
- **Post-Inflation Expansion Lag:** During the recent post-inflation expansion (2023–2026), ICA++NTS Minimum-EVaR gained +8.87% while matched Minimum-CVaR gained +19.66%, demonstrating that strict entropic tail penalties can cause underperformance in narrow, momentum-driven bull markets.
- **Non-Convexity of E-Rachev:** E-Rachev optimization is non-quasiconcave, requiring multi-start local optimization (SLSQP) without guaranteed global convergence.

## Falsification plan

1. **Transaction Cost Escalation Stress Test:** Model transaction costs at 35 bps to 50 bps. If ICA++NTS Minimum-EVaR net Sharpe falls below equal-weight (0.537), the practical tradeability of the allocation model under retail/institutional friction is falsified.
2. **Fat-Tail Tail-Parameter Perturbation Test:** Randomly perturb the fitted NTS tail parameters $(\alpha_i, \theta_i)$ by $\pm 20\%$. If optimal weights fluctuate by $> 30\%$ turnover without corresponding changes in asset return covariance, the optimization manifold suffers from parametric fragility.
3. **Bootstrap Out-of-Sample Falsification:** Conduct 5,000 circular block bootstraps comparing ICA++NTS Minimum-EVaR against MinVar and matched CVaR. If the two-sided bootstrap $p$-value for Sharpe outperformance exceeds 0.10, the claim of statistically significant risk-adjusted outperformance is disconfirmed.
4. **Single-Asset Concentration Check:** Audit historical weights for excessive concentration in defensive sectors (XLU, XLP). If outperformance vanishes after constraining individual sector weights to $\le 20\%$, the alpha is a static low-beta anomaly rather than genuine dynamic entropic timing.
5. **Failure Threshold:** If rolling 3-year net Sharpe drops below 0.0 during a major equity correction, the tail-hedging hypothesis is considered invalid.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Mechanism Mapping:** The mathematical core—EVaR optimization under tempered stable Lévy models—directly applies to multi-asset crypto portfolios (e.g., allocating among top 10–20 liquid crypto tokens or DeFi/L1 sector baskets). Crypto returns exhibit pronounced jump clustering, negative skewness, and extreme excess kurtosis, theoretical conditions where EVaR's Chernoff bound is even more advantageous than in equities.
- **Crypto-Specific Obstacles:**
  - **Parameter Estimation Instability:** Extreme jump frequency and non-stationary volatility regimes in crypto may cause ECDF-MSE fitting of NTS/CTS parameters to fail or produce unstable admissible MGF domains ($\mathcal{U}(\boldsymbol{w})$ collapsing to near zero).
  - **FastICA Component Breakdown:** In crypto crashes, cross-asset correlations spike toward 0.95+, violating the statistical independence assumption required by ICA factorization.
  - **Execution & Rebalancing Costs:** Monthly rebalancing in crypto is operationally feasible, but rebalancing illiquid altcoins during tail events encounters severe market impact and DEX slippage.
  - **Stablecoin / Quote Asset Dynamics:** Sector ETF cash is USD; crypto portfolio optimization requires accounting for quote currency choices (USDT, USDC, or BTC base).

## Limitations

- **Traditional Asset Sample Only:** Evaluated exclusively on U.S. large-cap equity sector SPDR ETFs. Behavior on individual single stocks, commodities, or crypto is unproven.
- **Computational Sensitivity:** Evaluating the inner one-dimensional infimum across hundreds of outer optimization iterations requires Brent's bounded minimization with subinterval discretization; numerical errors near domain boundaries can stall SLSQP solvers.
- **Parametric Model Risk:** If the underlying asset returns depart significantly from tempered stable Lévy processes (e.g., regime-switching stochastic volatility without jumps), the derived MGF cumulant will be misspecified.
- **Not Independently Reproduced:** All performance metrics are third-party empirical findings from Choi (arXiv:2608.18022v1).

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

## Adoption boundary

Research-only. This document represents a theoretical and computational research capture. It does not authorize capital deployment, paper trading, or live execution.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/portfolio-optimization-cvar-stochastic-control]]`

## Sources

- Jaehyung Choi, *"Entropic Value-at-Risk portfolio optimization for tempered stable Lévy processes"*, arXiv preprint `arXiv:2608.18022v1 [q-fin.PM, q-fin.RM]`, submitted August 18, 2026. DOI: [10.48550/arXiv.2608.18022](https://doi.org/10.48550/arXiv.2608.18022). Stable URL: `https://arxiv.org/abs/2608.18022`.
- References cited in source for foundational models:
  - Ahmadi-Javid, A. (2012). "Entropic value-at-risk: A new coherent risk measure." *Journal of Optimization Theory and Applications*, 155:1105–1123.
  - Rockafellar, R. T., & Uryasev, S. (2000). "Optimization of conditional value-at-risk." *Journal of Risk*, 2:21–42.
  - Kim, Y. S. (2022). "Portfolio optimization and marginal contribution to risk on multivariate normal tempered stable model." *Annals of Operations Research*, 312(2):853–881.
  - Hyvärinen, A., & Oja, E. (2000). "Independent component analysis: algorithms and applications." *Neural Networks*, 13(4-5):411–430.
