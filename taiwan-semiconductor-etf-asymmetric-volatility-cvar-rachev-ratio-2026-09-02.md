---
schema: strategy-research-record-v1
title: "Asymmetric Volatility and Coherent Tail-Risk Optimization for Semiconductor-Concentrated ETFs: GJR-GARCH-t Modeling and Long-Short CVaR Allocation"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - semiconductor-etf
  - tail-risk
  - asymmetric-volatility
  - cvar-optimization
  - rachev-ratio
  - starr-ratio
  - gjr-garch
  - extreme-value-theory
status: research-only
confidence: medium
source_as_of: 2026-07-17
sources:
  - "Ting-Jung Lee, Abootaleb Shirvani, Farzana Afroz, Svetlozar T. Rachev, and Frank J. Fabozzi, 'Portfolio Optimization under Heavy Tails and Asymmetric Volatility: Evidence from Taiwan-Exposed ETFs', arXiv:2607.16450v1 [q-fin.PM], July 17, 2026. https://arxiv.org/abs/2607.16450. DOI: https://doi.org/10.48550/arXiv.2607.16450"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Asymmetric Volatility and Coherent Tail-Risk Optimization for Semiconductor-Concentrated ETFs: GJR-GARCH-t Modeling and Long-Short CVaR Allocation

## Provenance

- Canonical Source: arXiv:2607.16450v1 [q-fin.PM], submitted July 17, 2026.
- Authors: Ting-Jung Lee (Department of Finance, Chung Yuan Christian University, Taiwan), Abootaleb Shirvani (Department of Mathematics and Statistics, Texas Tech University), Farzana Afroz (Department of Finance and Economics, Texas Tech University), Svetlozar T. Rachev (Department of Mathematics and Statistics, Texas Tech University), Frank J. Fabozzi (Carey Business School, Johns Hopkins University).
- DOI: https://doi.org/10.48550/arXiv.2607.16450
- Stable Source URLs:
  - Abstract: https://arxiv.org/abs/2607.16450
  - HTML Full Text: https://arxiv.org/html/2607.16450v1
  - PDF: https://arxiv.org/pdf/2607.16450
- Primary Empirical Dataset:
  - Universe: 31 US-listed ETFs spanning Taiwan equities (EWT), dedicated semiconductor equities (SMH, SOXX), global technology sector equities (IXN), emerging market equities (EEM, IEMG, AAXJ, AIA, EEMA, GMF, ECON, SCHE, SPEM, VWO, EWX), style and dividend emerging market funds (DEM, DGS, EDIV, EELV, EEMV, FEM, PIE, PXH, DBEM), and global equity benchmarks (ACWI, ACWX, CWI, IXUS, VEU, VXUS).
  - Sample Period: Daily observations from February 20, 2015 to February 20, 2025 (2,516 trading days).
  - Estimation Protocol: Rolling 4-year (1,008 trading days) estimation windows for daily rebalancing across the 2019–2025 evaluation horizon, with pre-COVID (2015–2019) and post-COVID (2020–2025) subsample robustness checks.

## Economic mechanism

### Source-reported

Global semiconductor manufacturing is geographically concentrated in Taiwan, where Taiwan Semiconductor Manufacturing Company (TSMC) accounts for over 50% of the capitalization of the iShares MSCI Taiwan ETF (EWT) and serves as the primary foundry for global chip designers (Nvidia, Apple, AMD, Qualcomm). This industrial concentration creates unique econometric properties:

1. **Extreme Tail Asymmetry and Power-Law Decay**: Heavy capital intensity, technological obsolescence cycles, export controls, and geopolitical friction produce fat-tailed return distributions. Left-tail Hill estimates $\\widehat{\\alpha}_k$ cluster between 2.5 and 3.5, indicating that fourth moments (kurtosis) and potentially third moments diverge or exhibit extreme sample instability.
2. **Asymmetric Volatility and Long Memory**: Downside market shocks generate substantially larger volatility spikes than positive shocks of equal magnitude (leverage effect). Furthermore, absolute and squared returns display persistent fractional integration ($d > 0$), indicating long memory in conditional volatility.
3. **Failure of Classical Mean-Variance Optimization**: The classic Markowitz framework relies on variance as the sole risk measure, penalizing upside and downside volatility symmetrically. Under fat-tailed, skewed semiconductor return dynamics, variance-minimizing portfolios systematically starve capital from high-growth semiconductor assets while failing to protect against catastrophic left-tail losses.
4. **Coherent Downside Risk Control**: Conditional Value-at-Risk (CVaR), defined as the conditional expectation of losses exceeding the Value-at-Risk threshold ($\\text{CVaR}_\\alpha(L) = \\mathbb{E}[L \\mid L \\ge \\text{VaR}_\\alpha(L)]$), satisfies the Artzner coherence axioms (subadditivity, convexity). Optimizing CVaR via Rockafellar-Uryasev linear programming provides an asymmetric risk buffer tailored to supply-chain and geopolitical disruptions.

### Research interpretation

The proposed alpha mechanism exploits structural tail asymmetry through dynamic risk-budget allocation:
- **Asymmetric Tail Hedging**: By separating upside participation from downside tail loss, CVaR-based optimization allows systematic over-weighting of technology-driven momentum during stable regimes while deploying bounded short positions ($-0.3 \\le w_i \\le 1.3$) against vulnerable satellite emerging-market ETFs to hedge supply-chain shocks.
- **Reward-to-Risk Re-anchoring**: Conventional Sharpe ratios reward high unhedged beta in bull markets but conceal vulnerability to structural breaks. Evaluating strategies via coherent tail ratios—specifically the Rachev ratio ($RR_{\\beta,\\gamma}$), which measures the ratio of expected extreme gains to expected extreme losses—reveals that CVaR optimization delivers structural downside protection without requiring subjective macro timing rules.

## Signal

### Econometric volatility & tail estimation
1. **GJR-GARCH(1,1)-$t$ Volatility Model**:
   Conditional variance follows:
   $$\\sigma_t^2 = \\omega + \\alpha \\epsilon_{t-1}^2 + \\gamma I_{\\{\\epsilon_{t-1} < 0\\}} \\epsilon_{t-1}^2 + \\beta \\sigma_{t-1}^2$$
   where $\\gamma$ measures volatility asymmetry, and standardized residuals $\\epsilon_t / \\sigma_t$ follow a standardized Student-$t$ distribution with $\\nu$ degrees of freedom. Volatility persistence is given by $\\alpha + \\beta + \\frac{\\gamma}{2}$.
2. **Hill Tail Index Estimator**:
   For ordered tail losses $L_{(1)} \\ge L_{(2)} \\ge \\dots \\ge L_{(m)}$:
   $$\\widehat{\\alpha}_k = \\left\\{ \\frac{1}{k} \\sum_{i=1}^k \\left( \\ln L_{(i)} - \\ln L_{(k+1)} \\right) \\right\\}^{-1}$$
   evaluated over optimal sample threshold $m = \\lfloor n^{0.5} \\rfloor$.
3. **Long Memory Parameterization**:
   Fractional integration parameter $d$ estimated via Geweke and Porter-Hudak (GPH) log-periodogram regression and Gaussian Semiparametric (Local Whittle) methods on squared returns.

### Portfolio optimization formulations
1. **Minimum-Variance Portfolio (MVP)**:
   $$\\min_{w} w^\\top \\Sigma_t w \\quad \\text{s.t.} \\quad w^\\top \\mathbf{1} = 1$$
2. **Rockafellar-Uryasev CVaR Optimization**:
   For confidence level $\\alpha \\in \\{0.05, 0.01\\}$ (corresponding to 95% and 99% confidence):
   $$\\min_{\\mathbf{w}, \\gamma} \\left\\{ \\gamma + \\frac{1}{\\alpha T} \\sum_{t=1}^T \\max(0, -r_t^\\top \\mathbf{w} - \\gamma) \\right\\} \\quad \\text{s.t.} \\quad \\mathbf{w}^\\top \\mathbf{1} = 1$$
3. **Constraint Regimes**:
   - **Long-Only (LO)**: $w_i \\ge 0, \\; \\forall i$.
   - **Long-Short (LS)**: $-0.30 \\le w_i \\le 1.30, \\; \\forall i$, permitting up to 30% short exposure per ETF to finance leveraged long holdings in high-tail-efficiency assets while maintaining net market exposure $\\sum w_i = 1.0$.

### Coherent risk-adjusted evaluation metrics
1. **Rachev Ratio ($RR_{\\beta,\\gamma}$)**:
   $$RR_{\\beta,\\gamma}(T) = \\frac{\\text{CVaR}_\\beta[r_f(t) - r_p(t)]_{[0,T]}}{\\text{CVaR}_\\gamma[r_p(t) - r_f(t)]_{[0,T]}}$$
   where $\\beta = \\gamma = 0.95$ and $0.99$. The numerator measures the expected magnitude of extreme positive excess returns (right tail), while the denominator measures the expected magnitude of extreme negative excess returns (left tail).
2. **STARR Measure ($\\text{STARR}_\\beta$)**:
   $$\\text{STARR}_\\beta(T) = \\frac{\\mathbb{E}[r_p(t) - r_f(t)]_{[0,T]}}{\\text{CVaR}_\\beta[r_p(t) - r_f(t)]_{[0,T]}}$$

## Required data

- **Universe**: 31 liquid US-listed ETFs covering Taiwan, semiconductors, global tech, and emerging markets (EWT, SMH, SOXX, IXN, ACWI, ACWX, IXUS, VEU, VXUS, AAXJ, EEM, IEMG, etc.).
- **Price Series**: Adjusted daily closing prices from February 20, 2015 to February 20, 2025.
- **Risk-Free Rate**: 3-month US Treasury bill yield.
- **Data Hygiene**: Elimination of asynchronous exchange holidays across US and Asian underlying exchanges via trade-date synchronization; dividends and corporate distributions fully reinvested in total return series.

## Execution assumptions

- **Rebalancing Cadence**: Daily re-estimation and rebalancing using a trailing 1,008 trading-day (4-year) rolling window over the 2019–2025 evaluation horizon.
- **Execution Timing**: Next-day market open following close-of-day signal computation.
- **Short Selling**: Permitted in the long-short regime up to -30% per asset, subject to standard borrow availability on liquid US-listed ETFs.
- **Turnover & Frictions**: Reported empirical price paths assume baseline friction-free rebalancing across liquid ETFs; transaction cost robustness examined in tail-spread stability.

## Evidence

### Source-reported

All figures below are cited directly from Lee, Shirvani, Afroz, Rachev, and Fabozzi (arXiv:2607.16450v1, July 17, 2026):

1. **Descriptive Return & Extreme Tail Statistics (Table 1)**:
   - **EWT (iShares MSCI Taiwan ETF)**: Mean annualized return **4.977%**, annualized volatility **21.529%**, skewness **-1.740**, excess kurtosis **17.279**, minimum daily return **-16.997%**, maximum daily return **6.525%**, maximum drawdown **41.272%**.
   - **Emerging Market Benchmarks**: IXUS mean return 2.272%, volatility 16.993%, skewness -1.158, kurtosis 14.656, max DD 39.920%; AAXJ mean return 1.776%, volatility 19.861%, max DD 45.935%.
2. **Econometric Dynamics (Tables 9 & 14)**:
   - **GJR-GARCH(1,1)-$t$ Volatility Asymmetry**: For EWT, asymmetry parameter $\\gamma = 0.0746$ ($p = 0.098$), ARCH parameter $\\alpha = 0.0810$ ($p = 0.030$), GARCH parameter $\\beta = 0.7837$ ($p < 0.001$), Student-$t$ tail degrees of freedom $\\nu = 4.738$ ($p < 0.001$), total persistence = **0.9020**. For EWP, $\\gamma = 0.1175$ ($p < 0.001$), $\\nu = 6.994$ ($p < 0.001$), total persistence = **0.9602**.
   - **Long Memory in Squared Returns**: GPH fractional integration estimate $d = 0.187$ ($p < 0.001$) for EWP and $d = 0.163$ ($p = 0.093$) for EWT; Local Whittle $d = 0.235$ for EWP; Hurst exponent $H = 0.650$ for EWP, confirming strong persistence in volatility shocks.
3. **Portfolio Realized Performance & Tail Risk (Sections 5.2 & 6)**:
   - **Rachev Ratio ($RR$) Leadership**: Under long-only constraints at the 95% confidence level, the Minimum-CVaR at 99% (C99) achieved the **highest median Rachev ratio** among all strategies. In contrast, the Minimum-Variance Portfolio (MVP) produced the lowest median Rachev ratio, demonstrating that variance minimization impairs the ratio of extreme upside to extreme downside.
   - **Cumulative Wealth & Long-Short Stability**: The equally weighted portfolio (EWP) achieved the highest unconstrained cumulative value due to unhedged exposure to the post-2020 AI semiconductor rally. However, long-short CVaR portfolios achieved **substantially smoother return paths**, sharply reducing downside tail dispersion and eliminating severe crash drawdowns during the 2020 COVID shock and 2022 tech drawdown.
   - **STARR Measure Dynamics**: EWP showed higher median STARR under long-only due to broad diversification, while C99 long-short exhibited more negative median STARR due to the structural opportunity cost of shorting during a persistent secular semiconductor bull market.

### Independently reproduced

Not independently reproduced. Empirical findings are cited directly from the authors' published econometric derivations and rolling backtests.

### Negative evidence

- **Secular Bull Market Opportunity Cost**: During aggressive structural rallies (e.g., the 2020–2024 generative AI hardware boom), tail-risk CVaR optimization systematically curtails exposure to top-performing semiconductor assets (SMH, SOXX, EWT), underperforming naive equal weighting (EWP) on raw cumulative return and Sharpe ratio.
- **Long-Short Parameter Sensitivity**: Introducing short positions ($-0.3 \\le w_i \\le 1.3$) substantially increased the dispersion of realized STARR and Sharpe values across rolling windows due to estimation error in tail quantiles, showing that unconstrained shorting in heavy-tailed assets amplifies estimation risk.

## Falsification plan

1. **Synthetic Gaussian Tail Control Test**: Replace empirical ETF return innovations with multivariate Gaussian noise calibrated to match sample means and covariances. If CVaR optimization continues to generate statistically significant differences in portfolio weights and Rachev ratios compared to Mean-Variance Optimization, the tail-specific alpha hypothesis is falsified.
2. **Semiconductor Concentration Removal Test**: Remove EWT, SMH, and SOXX from the 31-ETF universe. If the divergence between CVaR and MVP allocations collapses to statistical insignificance, the mechanism is confirmed to depend strictly on semiconductor supply-chain concentration rather than general emerging-market factor structures.
3. **Turnover & Cost Stress Test**: Impose 10 bps to 25 bps transaction costs on daily rolling rebalancing. If daily turnover costs erode the cumulative wealth of the long-short CVaR portfolio below that of a static buy-and-hold benchmark, the strategy is deemed practically unexecutable without a rebalancing deadband or buffer filter.
4. **Subsample Regime Inversion Test**: Test the allocation rule across a pure semiconductor down-cycle (e.g., 2000–2002 dot-com bust or 2008 global financial crisis). The long-short CVaR portfolio must achieve lower maximum drawdown and higher Sortino/Rachev ratios than both EWP and MVP to survive falsification.

## Crypto portability

Portability status: **adapted / unproven**.

The source paper establishes the econometric framework on US-listed ETFs with direct semiconductor exposure. Porting this mechanism to crypto markets involves critical structural considerations:

1. **Concentration Analogue**: Bitcoin and Ethereum play a role analogous to TSMC in Taiwan: they dominate market capitalization (>65% aggregate crypto cap) and drive directional tail risk for all altcoins.
2. **Heavy-Tail Severity**: Cryptocurrency return distributions exhibit even lower degrees of freedom ($\\nu \\approx 2.5 - 3.5$) and extreme power-law tail decay, making Gaussian variance optimization completely invalid and rendering CVaR and EVaR (Entropic VaR) mathematically mandatory.
3. **Short Selling & Borrow Costs**: Implementing the long-short constraint ($-0.30 \\le w_i \\le 1.30$) requires shorting altcoins via perpetual futures or margin borrow. Crypto perpetuals incur highly volatile, path-dependent funding rates that can exceed 30% annualized during bull regimes, creating an asymmetric carry cost that can destroy long-short tail hedges.
4. **24/7 Liquidation Cascades**: Unlike equity ETFs with exchange circuit breakers and continuous auction halts, crypto markets experience unbuffered cascading liquidations across decentralized lending protocols and centralized exchanges, accelerating tail realization speeds from days to minutes.

## Limitations

- **Daily Rolling Rebalancing Turnover**: Rebalancing daily across 31 ETFs without an explicit turnover penalty generates substantial cumulative transaction costs in real-world trading.
- **Concentration in TSMC**: EWT is effectively a single-stock proxy for TSMC (>50% weighting), meaning the empirical results reflect single-company geopolitical and operational risk as much as broad Taiwan market dynamics.
- **Subsample Dependency**: The 2015–2025 sample period covers an unprecedented secular super-cycle in semiconductor capital expenditure and AI hardware demand; performance under prolonged structural deflation or global foundry redundancy remains untested.
- **Absence of Dedicated Implementation Repository**: The authors present detailed econometric specifications and rolling figures but do not publish an open-source GitHub repository with automated execution pipelines.

## Implementation status

not-implemented. This research record documents an empirical econometric study. No implementation in NautilusTrader, PyBroker, or live production environments has been performed.

## Adoption boundary

research-only / not-approved. This record is strictly for research interpretation and hypothesis tracking. It is not approved for live trading, testnet, paper execution, or capital commitment.

## Related Wiki records

- [[quant/multiscale-multifractal-cross-correlation-signed-portfolio-2026-09-02]]
- [[quant/two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02]]
- [[quant/hybrid-resnet-rmt-covariance-denoising-crypto-mvp-2026-09-02]]
- [[quant/portfolio-covariance-and-shrinkage-2026-08-28]]
- [[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]
- [[quant/structural-breaks-regime-econometrics-2026-08-28]]
- [[quant/sharpe-deflated-multiple-testing-2026-08-27]]

## Sources

- Ting-Jung Lee, Abootaleb Shirvani, Farzana Afroz, Svetlozar T. Rachev, and Frank J. Fabozzi, "Portfolio Optimization under Heavy Tails and Asymmetric Volatility: Evidence from Taiwan-Exposed ETFs", arXiv preprint arXiv:2607.16450v1 [q-fin.PM], submitted July 17, 2026. Available at: https://arxiv.org/abs/2607.16450; HTML: https://arxiv.org/html/2607.16450v1; PDF: https://arxiv.org/pdf/2607.16450. DOI: https://doi.org/10.48550/arXiv.2607.16450.
- Rockafellar, R. T., and Uryasev, S. (2000), 'Optimization of conditional value-at-risk', Journal of Risk, 2(3), 21–42.
- Artzner, P., Delbaen, F., Eber, J.-M., and Heath, D. (1999), 'Coherent measures of risk', Mathematical Finance, 9(3), 203–228.
- Glosten, L. R., Jagannathan, R., and Runkle, D. E. (1993), 'On the relation between the expected value and the volatility of the nominal excess return on stocks', Journal of Finance, 48(5), 1779–1801.
- Rachev, S. T., Stoyanov, S. V., and Fabozzi, F. J. (2008), Advanced Stochastic Models, Risk Assessment, and Portfolio Optimization: The Ideal Risk, Uncertainty, and Performance Measures, John Wiley & Sons.
- DeMiguel, V., Garlappi, L., and Uppal, R. (2009), 'Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy?', Review of Financial Studies, 22(5), 1915–1953.
