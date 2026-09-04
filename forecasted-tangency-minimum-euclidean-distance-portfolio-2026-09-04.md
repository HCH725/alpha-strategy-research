---
schema: strategy-research-record-v1
title: "Forecasted Tangency Portfolios via Efficient Frontier Coefficient Dimensionality Reduction and Minimum Euclidean Distance Allocation"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - mean-variance
  - tangency-portfolio
  - efficient-frontier
  - vector-autoregression
  - varx
  - out-of-sample-sharpe
status: research-only
confidence: medium
source_as_of: 2026-04-05
sources:
  - https://arxiv.org/abs/2604.03948
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forecasted Tangency Portfolios via Efficient Frontier Coefficient Dimensionality Reduction and Minimum Euclidean Distance Allocation

## Provenance

- **Primary Source**: arXiv:2604.03948v1 [q-fin.PM], submitted April 5, 2026; originally presented at the 9th International Conference on Time Series and Forecasting (ITISE 2023), Gran Canaria, Spain, July 12–14, 2023; published in *Engineering Proceedings* (MDPI), Vol. 39.
- **Authors**: Nolan Alexander and William Scherer (Department of Systems Engineering, University of Virginia, Charlottesville, VA; email: `nolan_alex2018@yahoo.com`, `wts@virginia.edu`).
- **Title**: "Forecasting Tangency Portfolios and Investing in the Minimum Euclidean Distance Portfolio to Maximize Out-of-Sample Sharpe Ratios"
- **Canonical DOI / URL**: [https://doi.org/10.48550/arXiv.2604.03948](https://doi.org/10.48550/arXiv.2604.03948) / [https://arxiv.org/abs/2604.03948](https://arxiv.org/abs/2604.03948)
- **Data As-Of**: 1990–2022 (33 years of daily market asset data collected via Yahoo Finance API; French–Fama three-factor data for risk-free rates). Out-of-sample evaluation windows: 2000–2022 (23 years for Growth/Value/Market-Cap universe) and 2008–2022 (15 years for Sector ETF universe).
- **Source Deduplication Audit**: Repository-wide search on 2026-09-04 confirmed zero existing records citing `2604.03948`, Nolan Alexander, or William Scherer. Adjacent portfolio records (e.g., Ledoit-Wolf shrinkage, entropic factor models, or Black-Litterman variants) focus on direct estimation of the $N$-dimensional expected return vector $\mathbf{r}$ or $N \times N$ covariance matrix $\mathbf{V}$. This paper represents a distinct geometric dimensionality reduction paradigm operating directly on the three scalar coefficients of the Merton efficient frontier.

## Economic mechanism

### Source-reported

Classical Modern Portfolio Theory (Markowitz, 1952) and the Capital Asset Pricing Model (Sharpe, 1964; Tobin, 1958) prove that rational investors seeking to maximize risk-adjusted returns should hold the tangency portfolio—the point where the Capital Market Line (CML) is tangent to the efficient frontier. However, standard tangency portfolio construction relies on the foundational assumption that historical sample returns and covariances will match future realized parameters.

Alexander and Scherer (2026) emphasize the empirical failure of this assumption:
1. **Sample Estimation Error and Instability**: Estimating population parameters $(\mathbf{r}, \mathbf{V})$ from historical sample windows introduces severe estimation error (Dickinson, 1974), causing portfolio weights to be violently unstable and leading to severe out-of-sample Sharpe ratio collapse (Kan & Zhou, 2007).
2. **Shortcomings of Conventional Regularization**:
   - The Black–Litterman model (1992) requires an investor to supply extensive subjective views, confidence matrices, and tuning hyperparameters that are difficult to operationalize (Mankert, 2010).
   - Covariance shrinkage (Ledoit & Wolf, 2003) and DCC MV-GARCH (Engle & Sheppard, 2001) stabilize the covariance matrix $\mathbf{V}$, but leave the expected return vector $\mathbf{r}$ unmodeled, which is the primary source of portfolio optimization error.
3. **Dimensionality Reduction to Efficient Frontier Coefficients**: Merton (1972) established that the entire Markowitz efficient frontier can be expressed analytically as a square-root second-order polynomial governed by three scalar constants $(A, B, C)$. Rather than forecasting $N$ expected returns and $N(N+1)/2$ covariance terms, the dimensionality of the asset allocation problem can be reduced directly to forecasting the 3-dimensional trajectory of the frontier itself.
4. **Interpretable Geometric Decomposition**: The authors derive a transformation of $(A, B, C)$ into three intuitive coordinates:
   - $r_{mvp} = B/A$: Expected return of the global minimum variance point (MVP).
   - $\sigma_{mvp} = 1/\sqrt{A}$: Volatility of the minimum variance point.
   - $u = \sqrt{(AC - B^2)/A}$: Curvature rate (utility coefficient) of the efficient frontier, reflecting the tradeoff speed between risk and return across the feasible set.
5. **The Minimum Euclidean Distance Principle**: Because market dynamics are non-stationary, the forecasted tangency portfolio $(\hat{r}_{tp}, \hat{\sigma}_{tp})$ will generally not lie exactly on the currently observable efficient frontier. Projecting onto the portfolio on the current frontier that minimizes the Euclidean distance to the forecasted tangency point produces an allocation that is robust to structural shifts and eliminates parameter oversensitivity.

### Research interpretation

The strategy operationalizes an empirical macro-geometric asset allocation mechanism:
- **Geometry Over Parameters**: By modeling the efficient frontier vertex $(r_{mvp}, \sigma_{mvp})$ and curvature $u$, the framework captures collective market risk tolerance and aggregate risk-return trade-offs rather than idiosyncratic asset drift.
- **Autoregressive Frontier Inertia**: Frontier coefficients exhibit significant persistence over 1-year windows. Autoregressive dynamics (VARX) exploit the lead-lag relationship between long-term macro dispersion and short-term (1-month forward) opportunity sets.
- **Orthogonal Projection Regularization**: Selecting the minimum Euclidean distance point acts as an implicit shrinkage operator on the capital allocation line. When market conditions deteriorate (e.g., 2008 Global Financial Crisis or 2020 COVID shock), the Euclidean projection automatically pulls weights toward lower-variance regions of the feasible frontier, preventing extreme long/short leverage spikes.

## Signal

### Mathematical Formulation

1. **Merton Efficient Frontier Geometry (Source-reported)**:
   Given asset universe with expected log-return vector $\mathbf{r} \in \mathbb{R}^N$, covariance matrix $\mathbf{V} \in \mathbb{R}^{N \times N}$, and ones vector $\mathbf{e} \in \mathbb{R}^N$, Merton's quadratic constants are:
   $$A = \mathbf{e}^\top \mathbf{V}^{-1} \mathbf{e} > 0, \quad B = \mathbf{r}^\top \mathbf{V}^{-1} \mathbf{e}, \quad C = \mathbf{r}^\top \mathbf{V}^{-1} \mathbf{r} > 0$$
   The efficient frontier variance function is:
   $$\sigma^2(r) = \frac{A r^2 - 2B r + C}{AC - B^2}$$

2. **Novel Interpretable Coefficients (Source-reported)**:
   Alexander and Scherer re-parameterize the frontier into canonical vertex-curvature form:
   $$\sigma^2(r) = \left( \frac{r - r_{mvp}}{u} \right)^2 + \sigma_{mvp}^2$$
   where:
   $$r_{mvp} = \frac{B}{A}, \quad \sigma_{mvp} = \frac{1}{\sqrt{A}}, \quad u = \sqrt{\frac{AC - B^2}{A}}$$
   The authors establish the structural decomposition of $u$:
   $$u = \sqrt{\mathbf{r}^\top \mathbf{V}^{-1} \mathbf{r} \cdot \left(1 - S_c^2(\mathbf{r}, \mathbf{e})\right)}$$
   representing the product of the Mahalanobis distance of $\mathbf{r}$ to the origin and the sine of the angle formed by $\mathbf{r}$ and $\mathbf{e}$ under cosine similarity $S_c(\mathbf{r}, \mathbf{e})$.

3. **Closed-Form Tangency Portfolio from Coefficients (Source-reported)**:
   With risk-free rate $r_f$, setting the tangent line intercept at $(0, r_f)$ and matching the derivative $\sigma'(r)$:
   $$\sigma'(r) = \frac{r - r_{mvp}}{u^2 \sqrt{\left(\frac{r - r_{mvp}}{u}\right)^2 + \sigma_{mvp}^2}}$$
   Yields the exact tangency portfolio return $\hat{r}_{tp}$ and standard deviation $\hat{\sigma}_{tp}$:
   $$\hat{r}_{tp} = \frac{r_{mvp}^2 + u^2 \sigma_{mvp}^2 - r_{mvp} r_f}{r_{mvp} - r_f}, \quad \hat{\sigma}_{tp} = \sigma(\hat{r}_{tp}) = \sqrt{\left(\frac{\hat{r}_{tp} - r_{mvp}}{u}\right)^2 + \sigma_{mvp}^2}$$

4. **Online VARX(1) Frontier Forecasting (Source-reported)**:
   Forecast 1-month forward (21 business days, superscripts denote window length) average coefficients using 1-year (252 business days) historical rolling variables:
   - Minimum variance return:
     $$\hat{r}_{mvp, t}^{(21)} = \beta_{1,1} r_{mvp, t}^{(252)} + \beta_{0,1}$$
   - Minimum variance volatility:
     $$\hat{\sigma}_{mvp, t}^{(21)} = \beta_{1,2} \sigma_{mvp, t}^{(252)} + \beta_{0,2}$$
   - Curvature utility coefficient:
     $$\hat{u}_t^{(21)} = \beta_{2,3} \sigma_{mvp, t}^{(252)} + \beta_{1,3} \bar{r}_{EW, t}^{(252)} + \beta_{0,3}$$
   where $\bar{r}_{EW, t}^{(252)}$ is the historical 1-year equal-weighted universe return moving average. Model parameters are updated daily in an online rolling loop upon observation of the current day's realized coefficients.

5. **Minimum Euclidean Distance Optimization (Source-reported)**:
   The optimal target return $r^*$ minimizes the Euclidean distance from the current efficient frontier to the forecasted tangency coordinates $(\hat{r}_{tp}, \hat{\sigma}_{tp})$:
   $$\min_r D(r)^2 = (\hat{r}_{tp} - r)^2 + \left( \hat{\sigma}_{tp} - \sqrt{\left(\frac{r - r_{mvp}}{u}\right)^2 + \sigma_{mvp}^2} \right)^2$$
   Taking the first derivative and setting to zero yields the root equation solved via Newton's method:
   $$0 = 2(\hat{r}_{tp} - r) + 2(r - r_{mvp}) \frac{\hat{\sigma}_{tp} u - \sqrt{(r - r_{mvp})^2 + \sigma_{mvp}^2 u^2}}{u^2 \sqrt{(r - r_{mvp})^2 + \sigma_{mvp}^2 u^2}}$$

6. **Weight Extraction and Operational Parameters**:
   - **Weight Allocation**: Solve standard quadratic program (CVXPY / SciPy SLSQP) at target return $r^*$ (`source-reported`):
     $$\min_{\mathbf{w}} \mathbf{w}^\top \mathbf{V} \mathbf{w} \quad \text{s.t.} \quad \mathbf{w}^\top \mathbf{r} = r^*, \quad \mathbf{e}^\top \mathbf{w} = 1$$
     Shorting is permitted (`source-reported`).
   - **Leverage Constraint Scaling (Source-reported)**:
     To prevent unbounded leverage, weights are scaled to maximum leverage $l = 1.5\times$ (and tested at $2.0\times$):
     $$w_{i, pos}^{adj} = w_{i, pos} \frac{l - 1}{2 \sum |w_{pos}|}, \quad w_{i, neg}^{adj} = w_{i, neg} \frac{l - 1}{2 \sum |w_{neg}| + 1}$$
   - **Signal Cadence & Lookback**: Daily online update, 1-month (21-day) rolling lookback for immediate optimization input, 1-year (252-day) lookback for VARX predictors (`source-reported`).
   - **Signal Formation Timestamp**: Close of trading day $t$ (`source-reported`).
   - **Execution Timestamp**: Market-on-open (MOO) on day $t+1$ (`research-proposed`; source calculates on daily closing price series).

## Required data

- **Instruments / Universes**:
  - **Universe 1 (GVMC + Bonds)**: 6 mutual funds spanning Fama–French size and value dimensions (FDGRX: large-cap growth, FGRIX: large-cap value, FLPSX: mid-cap growth, FOCPX: mid-cap value, HRTVX: small-cap growth, OPOCX: small-cap value) plus FPNIX (FPA New Income Fund, intermediate bond proxy).
  - **Universe 2 (Sector ETFs + Bonds)**: 9 original Select Sector SPDR ETFs (XLB: Materials, XLE: Energy, XLF: Financials, XLI: Industrials, XLK: Technology, XLP: Consumer Staples, XLU: Utilities, XLV: Health Care, XLY: Consumer Discretionary) plus FPNIX.
- **Risk-Free Rate**: Kenneth French Data Library 1-month Treasury bill rate (`source-reported`).
- **Timeframe**: Daily adjusted closing returns (accounting for corporate splits and dividend distributions).
- **Price Vendor**: Yahoo Finance API (`source-reported`).
- **Missing Data Handling**: Forward-fill and alignment across trading calendar; assets requiring continuous 252-day history for initial VARX warm-up (`source-reported`).

## Execution assumptions

- **Execution Cadence**: Daily portfolio rebalancing (`source-reported`).
- **Execution Price Model**: Market-on-close or next-day opening auction (`research-proposed`; source assumes execution at closing prices).
- **Transaction Costs & Turnover Penalty (Source-reported)**:
  - The authors impose a punitive **1.0% daily transaction cost** model:
    $$\text{Cost}_t = 0.01 \times \sum_{i=1}^N |\Delta w_{i,t}|$$
    subtracted directly from daily portfolio returns to simulate friction under unconstrained turnover.
- **Leverage Limits**: Maximum gross leverage constrained to **1.5×** (GVMC) and **2.0×** (Sector ETFs) via post-optimization weight rescaling (`source-reported`).
- **Shorting / Borrow Availability**: Short positions permitted; cost of short borrow assumed zero in baseline gross model (`source-reported`). In live deployment, borrow fees on mutual funds or illiquid shares must be considered (`research-proposed`).

## Evidence

### Source-reported

All metrics below are third-party empirical findings directly extracted from Section 3 (Table 1) and Section 5 (Tables 2, 3, 4) of Alexander and Scherer (2026):

#### 1. Out-of-Sample Forecasting Accuracy of VARX(1) (Table 1)
- **Minimum Variance Return ($r_{mvp}$)**:
  - GVMC Out-of-Sample $R^2$: **13%**
  - Sector ETFs Out-of-Sample $R^2$: **2%**
- **Minimum Variance Volatility ($\sigma_{mvp}$)**:
  - GVMC Out-of-Sample $R^2$: **34%**
  - Sector ETFs Out-of-Sample $R^2$: **9%**
- **Curvature / Utility Coefficient ($u$)**:
  - GVMC Out-of-Sample $R^2$: **1%**
  - Sector ETFs Out-of-Sample $R^2$: **2%**

#### 2. Out-of-Sample Performance: GVMC + Bonds Universe (Table 2, 2000–2022, 23 Years)
Evaluated with 1-month rolling optimization, daily rebalancing, $1.5\times$ leverage cap, net of transaction costs:
- **Minimum Distance Portfolio to Tangency (Proposed)**:
  - Sharpe Ratio: **1.00**
  - Sortino Ratio: **1.31**
  - Annualized Return: **10.7%**
  - Maximum Drawdown: **-18.7%**
- **Standard Tangency Portfolio (Rolling 1-month)**:
  - Sharpe Ratio: **0.67**
  - Sortino Ratio: **0.71**
  - Annualized Return: **7.0%**
  - Maximum Drawdown: **-25.0%**
- **Equal-Weighted Benchmark**:
  - Sharpe Ratio: **0.41**
  - Sortino Ratio: **0.53**
  - Annualized Return: **9.2%**
  - Maximum Drawdown: **-50.6%**
- **S&P 500 Total Return**:
  - Sharpe Ratio: **0.33**
  - Sortino Ratio: **0.42**
  - Annualized Return: **8.3%**
  - Maximum Drawdown: **-55.3%**
- **60/40 Stocks and Bonds (60% S&P 500 / 40% FPNIX)**:
  - Sharpe Ratio: **0.47**
  - Sortino Ratio: **0.60**
  - Annualized Return: **5.3%**
  - Maximum Drawdown: **-22.6%**

#### 3. Out-of-Sample Performance: S&P Sector ETFs + Bonds Universe (Table 3, 2008–2022, 15 Years)
Evaluated with $2.0\times$ leverage scaling, daily rebalancing:
- **Minimum Distance Portfolio to Tangency (Proposed, 2× Levered)**:
  - Sharpe Ratio: **0.76**
  - Sortino Ratio: **0.99**
  - Annualized Return: **10.7%**
  - Maximum Drawdown: **-29.3%**
- **Standard Tangency Portfolio (Rolling 1-month)**:
  - Sharpe Ratio: **0.01**
  - Sortino Ratio: **0.01**
  - Annualized Return: **6.3%**
  - Maximum Drawdown: **-25.8%**
- **Equal-Weighted Benchmark**:
  - Sharpe Ratio: **0.52**
  - Sortino Ratio: **0.63**
  - Annualized Return: **10.6%**
  - Maximum Drawdown: **-46.7%**
- **S&P 500 Total Return**:
  - Sharpe Ratio: **0.48**
  - Sortino Ratio: **0.58**
  - Annualized Return: **11.2%**
  - Maximum Drawdown: **-51.8%**
- **60/40 Stocks and Bonds**:
  - Sharpe Ratio: **0.57**
  - Sortino Ratio: **0.69**
  - Annualized Return: **5.5%**
  - Maximum Drawdown: **-22.0%**

#### 4. Alpha Regressions Against Benchmarks (Table 4)
- **GVMC Universe**:
  - vs. Rolling 1-mo Tangency Portfolio: Alpha = **0.06**, $p$-value $< 1 \times 10^{-4}$
  - vs. Equal-Weighted: Alpha = **0.07**, $p$-value $< 1 \times 10^{-4}$
  - vs. S&P 500: Alpha = **0.06**, $p$-value $< 1 \times 10^{-4}$
  - vs. 60/40 Portfolio: Alpha = **0.06**, $p$-value $< 1 \times 10^{-4}$
- **Sector ETFs Universe**:
  - vs. Rolling 1-mo Tangency Portfolio: Alpha = **0.10**, $p$-value = **0.0003**
  - vs. Equal-Weighted: Alpha = **0.06**, $p$-value = **0.01**
  - vs. S&P 500: Alpha = **0.06**, $p$-value = **0.02**
  - vs. 60/40 Portfolio: Alpha = **0.05**, $p$-value = **0.02**

### Independently reproduced

Not independently reproduced. All metrics and statistical claims are third-party results reported by Nolan Alexander and William Scherer (2026).

### Negative evidence

1. **Low Predictability of Curvature ($u$)**: The out-of-sample predictive power for the curvature parameter $u$ is minimal ($R^2 = 1\%$ in GVMC, $2\%$ in Sectors, Table 1). While MVP volatility is moderately predictable ($R^2 = 34\%$ in GVMC), forecasting higher-order risk-return curvature remains noisy.
2. **Collapse of Standard Tangency in Sector ETFs**: Standard rolling 1-month tangency optimization completely collapses on the Sector ETF panel, yielding a near-zero Sharpe ratio of **0.01** (Table 3), demonstrating extreme sensitivity of classical Markowitz optimization to sector correlation shifts.
3. **Turnover Sensitivity**: Because the model solves a Euclidean distance minimization on daily recomputed frontiers, unconstrained rebalancing generates substantial daily turnover. Without leverage scaling or cost management, high transaction frictions could erode out-of-sample advantages.

## Falsification plan

To falsify the claim that forecasting efficient frontier coefficients via VARX and Euclidean distance projection generates persistent out-of-sample Sharpe alpha:

1. **Permutation Placebo Test (Frontier Parameter Shuffling)**:
   - Randomly permute the time-series order of the forecasted coefficient vectors $(\hat{r}_{mvp}, \hat{\sigma}_{mvp}, \hat{u})$ across the out-of-sample evaluation window (500 iterations, `research-proposed`).
   - `Research-defined falsification threshold`: If the real-time VARX-forecasted portfolio fails to exceed the 95th percentile Sharpe ratio of the shuffled placebo distribution, reject the hypothesis that the VARX time-series structure possesses genuine predictive alpha over unconditional frontier averaging.
2. **Transaction Cost & Slippage Attrition Test**:
   - Evaluate performance under realistic proportional bid-ask spread and turnover drag: 5 bps for liquid sector ETFs, 15 bps for mutual fund proxies, plus quadratic market impact (`research-proposed`).
   - `Research-defined falsification threshold`: Net-of-friction annual Sharpe ratio drops below **0.50** or alpha against the 60/40 benchmark loses statistical significance ($p > 0.05$).
3. **Out-of-Sample Expansion (2023–2026 Audit)**:
   - Extend the test window from 2023 through 2026 across the same 9 sector ETFs and bond fund.
   - `Research-defined falsification threshold`: Out-of-sample Sharpe ratio $< 0.40$ or annualized maximum drawdown $> 35\%$, confirming regime vulnerability to rapid interest rate shifts.
4. **Comparison Against Shrinkage Baselines**:
   - Benchmark the Minimum Euclidean Distance Portfolio against Linear Ledoit-Wolf shrinkage and Non-linear Analytical Shrinkage (Ledoit & Wolf, 2020) on identical asset universes (`research-proposed`).
   - `Research-defined falsification threshold`: If covariance shrinkage alone without coefficient forecasting achieves an identical or higher Sharpe ratio with lower turnover, the marginal complexity of VARX coefficient forecasting is falsified.

## Crypto portability

- **Portability Status**: `adapted` / `unproven`.
- **Primary Source Demonstration**: The cited primary source evaluates exclusively traditional U.S. mutual funds, SPDR sector ETFs, and U.S. Treasury bills. It contains zero empirical evidence in cryptocurrency markets. Porting to digital assets is a `research-proposed` adaptation and remains unproven.
- **Crypto-Specific Market Adaptation Considerations**:
  1. *Perpetual Futures Universe*: In crypto, the strategy could be ported to a cross-sectional basket of liquid perpetual futures (e.g., top 10–20 tokens by open interest on Binance/Bybit).
  2. *24/7/365 Non-Stationary Drift*: Crypto asset correlations experience rapid regime transitions during market liquidations, which may cause Merton coefficient estimates $(A, B, C)$ to degenerate or matrix $\mathbf{V}$ to become near-singular. Robust condition-number regularization or shrinkage must precede coefficient calculation (`research-proposed`).
  3. *Funding Rate and Borrow Cost Asymmetry*: Holding long-short portfolios across crypto perpetuals incurs continuous 8-hour funding cash flows. The standard Markowitz return vector $\mathbf{r}$ must be adjusted for net funding costs ($r_i - f_{rate, i}$) to prevent funding drag from dominating the small expected return differential (`research-proposed`).
  4. *Absence of a True Risk-Free Asset*: In crypto, the risk-free rate $r_f$ is not a sovereign Treasury bill; synthetic proxies (e.g., Aave USDC lending rate, sUSDe yield, or exchange cash-and-carry basis) must be substituted (`research-proposed`).

## Limitations

- **Source Methodology**: Evaluated on two small asset universes ($N = 7$ for GVMC, $N = 10$ for Sectors). Performance on high-dimensional equity panels ($N > 100$) where covariance matrices are rank-deficient is unproven.
- **Mutual Fund Executability**: The GVMC universe employs mutual funds (e.g., FDGRX, HRTVX) which only execute at 4:00 p.m. ET NAV and frequently impose redemption fees or trading frequency limits on daily rebalancing.
- **Simplified VARX Specification**: The time-series model uses only lag-1 coefficients and 1-year equal-weighted returns; nonlinear dynamics or macro regime switching are unmodeled.
- **Shorting Feasibility**: The theoretical formulation allows unrestricted short sales; in practice, borrow locate availability and short rebate costs on smaller mutual funds or volatile ETFs can materially impair returns.

## Implementation status

- `not-implemented`. No implementation exists in PyBroker, NautilusTrader, or our live execution environments.
- This record serves solely as upstream theoretical and empirical documentation.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- A record being present here does not constitute authorization for trading, paper execution, testnet deployment, or live capital allocation. Implementation requires subsequent validation in PyBroker, transaction cost analysis, and formal risk committee review.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`

## Sources

1. Nolan Alexander and William Scherer, *"Forecasting Tangency Portfolios and Investing in the Minimum Euclidean Distance Portfolio to Maximize Out-of-Sample Sharpe Ratios"*, arXiv preprint `arXiv:2604.03948v1 [q-fin.PM]`, submitted April 5, 2026. DOI: [10.48550/arXiv.2604.03948](https://doi.org/10.48550/arXiv.2604.03948). Canonical URL: [https://arxiv.org/abs/2604.03948](https://arxiv.org/abs/2604.03948). Published in *Engineering Proceedings*, MDPI, Vol. 39 (ITISE 2023).
2. R. C. Merton, *"An Analytic Derivation of the Efficient Portfolio Frontier"*, *Journal of Financial and Quantitative Analysis*, Vol. 7, No. 4, pp. 1851–1872, 1972. DOI: [10.2307/2329621](https://doi.org/10.2307/2329621).
3. H. Markowitz, *"Portfolio Selection"*, *The Journal of Finance*, Vol. 7, No. 1, pp. 77–91, 1952. DOI: [10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x).
4. W. F. Sharpe, *"Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk"*, *The Journal of Finance*, Vol. 19, No. 3, pp. 425–442, 1964. DOI: [10.1111/j.1540-6261.1964.tb02865.x](https://doi.org/10.1111/j.1540-6261.1964.tb02865.x).
5. O. Ledoit and M. Wolf, *"Improved estimation of the covariance matrix of stock returns with an application to portfolio selection"*, *Journal of Empirical Finance*, Vol. 10, No. 5, pp. 603–621, 2003. DOI: [10.1016/S0927-5398(03)00007-0](https://doi.org/10.1016/S0927-5398(03)00007-0).
6. R. Kan and G. Zhou, *"Optimal Portfolio Choice with Parameter Uncertainty"*, *Journal of Financial and Quantitative Analysis*, Vol. 42, No. 3, pp. 621–656, 2007. DOI: [10.1017/S0022109000004129](https://doi.org/10.1017/S0022109000004129).
7. F. Black and R. Litterman, *"Global Portfolio Optimization"*, *Financial Analysts Journal*, Vol. 48, No. 5, pp. 28–43, 1992. DOI: [10.2469/faj.v48.n5.28](https://doi.org/10.2469/faj.v48.n5.28).
