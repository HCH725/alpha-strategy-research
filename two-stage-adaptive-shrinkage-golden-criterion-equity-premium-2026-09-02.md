---
schema: strategy-research-record-v1
title: "Two-Stage Adaptive Shrinkage Weights and the Golden Criterion for Equity Premium Predictability"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-premium
  - forecast-combination
  - shrinkage-estimation
  - portfolio-optimization
  - golden-criterion
  - naive-diversification
  - market-timing
status: research-only
confidence: medium
source_as_of: 2026-07-13
sources:
  - "Han Feng, Difang Huang, Jue Wang, and Zhengjun Zhang, 'When and Why Naïve Diversification Works: A Simple Diagnostic Strategy', arXiv:2607.11054v1 [econ.GN, q-fin.EC, stat.AP], July 13 2026. https://arxiv.org/abs/2607.11054. DOI: https://doi.org/10.48550/arXiv.2607.11054"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Two-Stage Adaptive Shrinkage Weights and the Golden Criterion for Equity Premium Predictability

## Provenance

- Canonical Source: arXiv:2607.11054v1 [econ.GN, q-fin.EC, stat.AP], submitted July 13, 2026.
- Authors: Han Feng (School of Economics and Management, Southeast University), Difang Huang (Department of Economics, Monash University), Jue Wang (School of Economics, Southwestern University of Finance and Economics), Zhengjun Zhang (Department of Statistics, University of Wisconsin-Madison).
- DOI: https://doi.org/10.48550/arXiv.2607.11054
- Stable Source URLs:
  - Abstract: https://arxiv.org/abs/2607.11054
  - HTML full text: https://arxiv.org/html/2607.11054v1
  - PDF: https://arxiv.org/pdf/2607.11054
- Primary empirical dataset: Monthly excess returns of the S&P 500 index over the 30-day Treasury bill rate (CRSP / Welch and Goyal 2008 / Goyal et al. 2024 dataset), evaluated from January 1996 to August 2019 (284 months) and extended to December 2024 (348 months).
- 13 Goyal-Welch financial and macroeconomic predictors: Dividend-Price ratio (DP), Earnings-Price ratio (EP), Dividend-Earnings ratio (DE), Stock Return Volatility (RVOL), Book-to-Market ratio (BM), Net Equity Expansion (NTIS), Treasury Bill rate (TBL), Long-term Government Bond Yield (LTY), Long-term Government Bond Return (LTR), Term Spread (TMS), Default Yield Spread (DFY), Default Return Spread (DFR), and Inflation (INFL).

## Economic mechanism

### Source-reported

The paper addresses the long-standing "forecast combination puzzle" in empirical finance: why simple equal-weighting ($1/N$) frequently outperforms statistically optimized combinations out-of-sample. The authors prove that the root cause is structural:

1. **The Golden Criterion**: Equal weighting is minimum-variance optimal if and only if the error covariance matrix admits the all-ones vector $\mathbf{1}$ as an eigenvector. Specifically, for an $N \times N$ error covariance matrix $\mathbf{\Sigma}_1$, the condition $\mathbf{\Sigma}_1 \mathbf{1} = \delta_1 \mathbf{1}$ holds if and only if the unconstrained optimal weights $\hat{\mathbf{w}}^{ow} = \frac{\mathbf{\Sigma}_1^{-1}\mathbf{1}}{\mathbf{1}^T \mathbf{\Sigma}_1^{-1}\mathbf{1}}$ collapse to the equal-weight vector $\frac{1}{N}\mathbf{1}$.
2. **Two-Stage Invariance**: If $\mathbf{\Sigma}_1$ satisfies the Golden Criterion in the first stage (training), the adaptive shrinkage path $\hat{\mathbf{w}}^\lambda = \lambda \frac{1}{N}\mathbf{1} + (1-\lambda)\hat{\mathbf{w}}^{ow}$ collapses identically to equal weights $\frac{1}{N}\mathbf{1}$ for all $\lambda \in [0,1]$, regardless of the second-stage error covariance matrix $\mathbf{\Sigma}_2$ (validation).
3. **Market-Mode Alignment**: Under Perron-Frobenius theory, when entries of $\mathbf{\Sigma}_1$ are strictly positive (common at short horizons where macro predictors share broad co-movement), the all-ones eigenvector coincides with the dominant eigenvalue $\rho_{\max}(\mathbf{\Sigma}_1)$. The Rayleigh quotient $\frac{\mathbf{1}^T \mathbf{\Sigma}_1 \mathbf{1}}{N}$ measures the variance along the equal-weight direction. Closeness between $\rho_{\max}(\mathbf{\Sigma}_1)$ and $\frac{\mathbf{1}^T \mathbf{\Sigma}_1 \mathbf{1}}{N}$ confirms that empirical forecast errors share a single dominant market mode with homogeneous factor loadings.
4. **Accuracy-Diversity Trade-off**: At short forecast horizons ($J=1$ month), estimation noise swamps individual predictive signal, causing the Golden Criterion to be approximately satisfied ($\lambda_{opt} \approx 1$). At longer horizons ($J=12, 24$), persistent macroeconomic predictability emerges, error covariance departs from the all-ones alignment, and optimization regains its comparative advantage.

### Research interpretation

The proposed alpha mechanism is a dynamic meta-allocation policy over predictive models. Rather than fixing combination weights or using heuristic cross-validation, the strategy balances predictive precision against forecast diversity using a closed-form shrinkage intensity $\lambda_{opt}$.

The economic justification rests on estimation-risk reduction:
- In high-noise regimes (short-horizon equity timing), unconstrained covariance inversion causes extreme, unstable portfolio weights that degrade out-of-sample risk-adjusted returns.
- Adaptively shrinking toward the $1/N$ vector extracts diversification benefits when forecast errors are dominated by a common market mode.
- Conversely, when market regimes diverge from the Golden Criterion (longer holding horizons or structural breaks), the system smoothly tilts back toward optimal factor-tilted weights.

## Signal

The signal generates market-timing weights $w_t \in [0, 1.5]$ for the risky equity index (S&P 500) vs. risk-free cash (30-day T-bills).

### Formation timestamp
- Monthly rebalancing at month end $t$, tradable for month $t+1$ to $t+J$.
- All predictor variables and returns are observed point-in-time up to month $t$.

### Lookback and sample partitioning
- Expanding estimation window for individual predictive regressions:
  $$r_{t+1, t+J} = \alpha_{i,J} + \beta_{i,J} x_{it} + \epsilon_{i|t+1, t+J}$$
  where $r_{t+1, t+J} = \frac{1}{J}\sum_{k=1}^J r_{t+k}$ is the annualized excess return over horizon $J \in \{1, 3, 6, 12, 24\}$ months.
- Predictors $x_{it}$ are standardized to unit sample standard deviation.
- Sample is sequentially split into:
  - Stage 1 training window ($T_{c1}$ months, e.g., 6 to 48 months) to compute individual forecasts and initial error covariance $\mathbf{\Sigma}_1$.
  - Stage 2 validation window ($T_{c2}$ months, e.g., 84 to 126 months) to evaluate the accuracy vector $\mathbf{S}$ and diversity matrix $\mathbf{D}$.
  - Out-of-sample testing window ($T_{c3}$: January 2007 to August 2019, 152 months; extended to December 2024, 216 months).

### Two-Stage Adaptive Shrinkage Weight (2S-ASW) derivation
1. Optimal weights from training period:
   $$\hat{\mathbf{w}}^{ow} = \frac{\mathbf{\Sigma}_1^{-1}\mathbf{1}}{\mathbf{1}^T \mathbf{\Sigma}_1^{-1}\mathbf{1}}$$
2. Validation evaluation:
   - Accuracy vector $\mathbf{S} = [\text{MSFE}_1, \dots, \text{MSFE}_N]^T$, where $\text{MSFE}_i = \frac{1}{T_{c2}}\sum_{h \in T_{c2}} (y_h - f_{ih})^2$.
   - Diversity matrix $\mathbf{D} \in \mathbb{R}^{N \times N}$, where $D_{ij} = \text{Div}_{ij} = \frac{1}{T_{c2}}\sum_{h \in T_{c2}} (f_{ih} - f_{jh})^2$ for $i \neq j$, and $D_{ii} = 0$.
3. Analytical closed-form optimal shrinkage:
   Let $\mathbf{a} = \frac{1}{N}\mathbf{1} - \hat{\mathbf{w}}^{ow}$. The combination MSFE along the path $\mathbf{w}(\lambda) = \hat{\mathbf{w}}^{ow} + \lambda \mathbf{a}$ is strictly convex if $\mathbf{a}^T \mathbf{D} \mathbf{a} < 0$.
   The stationary point is:
   $$\lambda^* = \frac{\mathbf{S}^T \mathbf{a} - (\hat{\mathbf{w}}^{ow})^T \mathbf{D} \mathbf{a}}{\mathbf{a}^T \mathbf{D} \mathbf{a}}$$
   Constrained to the unit interval:
   $$\lambda_{opt} = \min(\max(\lambda^*, 0), 1)$$
4. Combined return forecast:
   $$\hat{r}_{comb, t+1, t+J} = \sum_{i=1}^N \hat{w}^\lambda_i \hat{f}_{i, t+1, t+J}, \quad \text{where } \hat{\mathbf{w}}^\lambda = \lambda_{opt} \frac{1}{N}\mathbf{1} + (1 - \lambda_{opt}) \hat{\mathbf{w}}^{ow}$$

### Asset allocation rule
A mean-variance investor with risk aversion $\gamma = 3$ allocates wealth to equities according to:
$$w_t = \min\left(\max\left(\frac{\hat{r}_{comb, t+1, t+J}}{\gamma \hat{\sigma}^2_{comb, t+1, t+J}}, 0\right), 1.5\right)$$
where $\hat{\sigma}^2_{comb, t+1, t+J}$ is the forecasted return volatility estimated over a 10-year rolling window. Short sales are prohibited ($w_t \ge 0$) and maximum leverage is capped at 150% ($w_t \le 1.5$). The remaining capital $1 - w_t$ is held in 30-day Treasury bills.

## Required data

- Instrument: S&P 500 total return index (including dividends) and 30-day Treasury bill rate (CRSP).
- Predictor features (13 monthly Goyal-Welch series):
  - Valuation ratios: DP (log dividend-price), EP (log earnings-price), DE (log dividend-earnings), BM (book-to-market).
  - Yields and spreads: TBL (3-month T-bill), LTY (long-term government bond yield), LTR (long-term government bond return), TMS (term spread: LTY - TBL), DFY (default yield spread: BAA - AAA), DFR (default return spread: corporate - government).
  - Macroeconomic indicators: INFL (CPI for All Urban Consumers, BLS), RVOL (12-month moving return volatility), NTIS (net equity expansion ratio on NYSE).
- Timeframe: Monthly observations, end-of-month calendar frequency.
- Point-in-time availability: Macroeconomic and accounting variables (e.g., earnings, book value, CPI) must observe reporting publication lags to eliminate look-ahead bias.

## Execution assumptions

- Signal-to-order timing: Monthly rebalance executed at next-period market open following signal generation at month end.
- Transaction costs: 50 basis points (0.50%) deducted per unit of portfolio turnover, following Rapach et al. (2016).
- Order type: Market on Open (MOO) / rebalancing assumed friction-adjusted at 50 bps fee+slippage.
- Financing / Leverage: Maximum leverage 1.5x, borrow rate set equal to the 30-day T-bill rate; no short selling of equities ($w_t \ge 0$).

## Evidence

### Source-reported

All figures below are cited directly from Feng, Huang, Wang, and Zhang (2026), evaluating the January 2007 to August 2019 out-of-sample period on S&P 500 excess returns:

1. **Out-of-Sample $R^2$ ($R^2_{COS}$)**:
   - At $J=1$ month, 2S-ASWs achieved positive out-of-sample $R^2$ across all sample-splitting configurations, reaching up to **5.41%** ($p < 0.05$ under Clark-West MSFE-adjusted test).
   - In contrast, both constituent methods individually failed at $J=1$: pure optimal weights (OWs) produced negative $R^2_{COS}$ (down to $-70.11\%$ in extended samples), and equal weights (EWs) produced negative or negligible $R^2_{COS}$.
   - Individual Goyal-Welch predictors: Only Dividend-Price (DP) showed positive out-of-sample $R^2$ at $J=1$ (0.77% to 0.87%), while all other 12 predictors yielded negative out-of-sample $R^2$.
2. **Economic Evaluation (Utility & Sharpe Ratio)**:
   - Annualized utility gains for $\gamma = 3$ investors exceeded **200 basis points** across configurations, with a maximum gain of **10.67%** under configuration $(T_1=42, T_{c1}=48, T_{c2}=84)$.
   - Annualized Sharpe ratios (net of 50 bps transaction costs) consistently exceeded 0.50, reaching up to **1.27** (under $T_1=54$).
   - In comparison, the passive buy-and-hold benchmark and historical mean forecasts achieved substantially lower Sharpe ratios (e.g., PCA models had Sharpe ratios as low as 0.26 at $J=12$).
3. **Shrinkage Dynamics ($\lambda_{opt}$)**:
   - At $J=1$ month, $\lambda_{opt}$ clustered heavily near 1: 19.74% of rolling windows had $\lambda_{opt} = 1.0$ exactly, and 66.45% had $\lambda_{opt} > 0.90$.
   - At $J=3$ months, 57.33% had $\lambda_{opt} = 1.0$ exactly, and 84.67% had $\lambda_{opt} > 0.90$.
   - At $J \ge 12$ months, $\lambda_{opt}$ dropped substantially, and OWs$(\mathbf{\Sigma}_2)$ or Blanc & Setzer (2020) bias-corrected weights regained performance (e.g., DMSPE reached $R^2_{COS} = 56.57\%$ at $J=24$).
4. **Extended Sample (to December 2024)**:
   - 2S-ASWs maintained outperformance over benchmarks at $J=1$, though overall market predictability attenuated, matching broader findings in recent empirical literature (Denk and Löffler 2024).

### Independently reproduced

Not independently reproduced. The empirical results rely on the authors' published paper and closed-form derivations.

### Negative evidence

- Intermediate horizon "check-mark" dip: At $J=6$ months, 2S-ASWs experienced a pronounced dip in $R^2_{COS}$, where discount methods (e.g., DMSPE with $\theta = 0.9$) dominated ($R^2_{COS} = 13.00\%$).
- Extended sample attenuation: When extending evaluation through December 2024, predictability weakened across all macroeconomic forecasting combinations, indicating structural shifts or reduced factor relevance post-2020.
- Non-negative weight constraints: Constraining optimal weights to be non-negative in the first stage reduced the hedging benefit of negative weights, slightly lowering out-of-sample $R^2$ at longer horizons.

## Falsification plan

1. **Covariance Eigenstructure Perturbation Test**: Inject synthetic eigenvector misalignment into $\mathbf{\Sigma}_1$ such that the all-ones vector $\mathbf{1}$ is orthogonal to the principal component. If 2S-ASW continues to set $\lambda_{opt} \approx 1$ despite the departure from the Golden Criterion, the adaptive selection mechanism is falsified.
2. **Alternative Predictor Universe Test**: Replace Goyal-Welch macroeconomic series with orthogonal white noise predictors. The out-of-sample $R^2_{COS}$ must collapse to $\le 0$, and annualized utility gains net of 50 bps turnover costs must fail to exceed zero.
3. **Turnover & Cost Frontier Stress Test**: Scale transaction costs from 50 bps to 150 bps. If monthly weight fluctuations between equity and T-bills consume more than 200 bps of annualized utility, the practical market-timing alpha is refuted by execution frictions.
4. **Walk-forward Leakage Audit**: Confirm that macroeconomic variables subject to historical revisions (such as GDP, CPI, and corporate earnings) are strictly lagged to public announcement timestamps rather than post-revision series.

## Crypto portability

Portability status: **adapted / unproven**.

The source paper establishes the Golden Criterion and 2S-ASW framework exclusively on traditional equity indices (S&P 500) and macroeconomic predictors. Porting this mechanism to cryptocurrency requires substantial adaptations:

1. **Target Universe**: S&P 500 market timing must be adapted to Bitcoin/Ethereum directional timing or a cross-sectional multi-token factor combination (e.g., top 50 perpetual futures).
2. **Predictor Feature Space**: Goyal-Welch macroeconomic indicators have slow monthly sampling frequencies and low direct explanatory power for crypto. Predictor sets must be adapted to crypto-native features: funding rate spreads, order flow imbalances (OFI), perpetual basis, on-chain stablecoin issuance, and exchange net inflows.
3. **Rebalancing Horizon**: Monthly rebalancing ($J=1$ to $24$ months) is excessively sluggish for cryptocurrency volatility regimes. The framework must be evaluated on intraday to weekly horizons ($J \in \{1\text{h}, 4\text{h}, 1\text{d}, 7\text{d}\}$).
4. **Market-Mode Breakdown**: In crypto markets, liquidation cascades frequently cause cross-asset correlations to spike to near 1.0, which artificially forces the Golden Criterion to hold during market stress, but with extreme negative expected returns. A simple $1/N$ long tilt during cascades would result in severe drawdowns unless conditioned on a regime volatility filter.

## Limitations

- **Underspecified Code Repository**: The authors provide full equations and sample configurations but do not link an immutable GitHub repository with pre-packaged scripts.
- **Publication & Revision Lags**: Goyal-Welch datasets in macroeconomics are subject to retrospective data revisions; point-in-time vintage data must be verified in live execution.
- **Univariate Predictor Assumptions**: The first stage uses univariate OLS regressions for each predictor before combination, which ignores multivariate interaction effects prior to the combination step.
- **Horizon Sensitivity**: The superior performance of 2S-ASW is concentrated at the shortest horizon ($J=1$ month), with performance degrading or being overtaken by DMSPE and Ridge at intermediate horizons ($J=3, 6$).

## Implementation status

not-implemented. This research record documents a theoretical and empirical study from academic literature; no implementation in NautilusTrader, PyBroker, or live execution engines has been performed.

## Adoption boundary

research-only / not-approved. This record serves strictly as a research hypothesis and diagnostic model. It is not approved for production capital, paper trading, or live order routing.

## Related Wiki records

- [[quant/portfolio-covariance-and-shrinkage-2026-08-28]]
- [[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]
- [[quant/phase9-factor-covariance-redundancy-risk-decomposition-2026-08-28]]
- [[quant/structural-breaks-regime-econometrics-2026-08-28]]
- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
- [[quant/sharpe-deflated-multiple-testing-2026-08-27]]

## Sources

- Han Feng, Difang Huang, Jue Wang, and Zhengjun Zhang, 'When and Why Naïve Diversification Works: A Simple Diagnostic Strategy', arXiv preprint arXiv:2607.11054v1 [econ.GN, q-fin.EC, stat.AP], July 13, 2026. Available at: https://arxiv.org/abs/2607.11054; HTML: https://arxiv.org/html/2607.11054v1. DOI: https://doi.org/10.48550/arXiv.2607.11054.
- Goyal, A., Welch, I., and Zafirov, N. (2024), 'A Comprehensive Look at The Empirical Performance of Equity Premium Predictors', Review of Financial Studies.
- Campbell, J. Y., and Thompson, S. B. (2008), 'Predicting the Equity Premium Out of Sample: Can Anything Beat the Historical Average?', Review of Financial Studies, 21(4), 1509–1531.
- Rapach, D. E., Strauss, J. K., and Zhou, G. (2010), 'Out-of-sample equity premium prediction: Combination forecasts and links to the real economy', Review of Financial Studies, 23(2), 821–862.
- Rapach, D. E., Ringgenberg, M. C., and Zhou, G. (2016), 'Short interest and aggregate stock returns', Journal of Financial Economics, 121(1), 46–65.
