---
schema: strategy-research-record-v1
title: "Compact-RIEnet: Neural Network-Driven Volatility Drag Mitigation and Liquidation Delay under Aggressive Portfolio Leverage"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - global-minimum-variance
  - volatility-drag
  - leverage
  - neural-networks
  - random-matrix-theory
  - covariance-cleaning
  - bigru
status: research-only
confidence: high
source_as_of: 2026-07-26
sources:
  - "Christian Bongiorno, Efstratios Manolakis, and Rosario Nunzio Mantegna, 'Neural Network-Driven Volatility Drag Mitigation under Aggressive Leverage', arXiv:2607.23068v1 [q-fin.PM], July 26, 2026. DOI: 10.48550/arXiv.2607.23068. ACM ICAIF DOI: 10.1145/3768292.3770370. Stable URL: https://arxiv.org/abs/2607.23068."
  - "Christian Bongiorno, 'Compact-RIEnet: Compact Reformulation of Modular End-to-End Neural Network for Global Minimum-Variance Portfolio Optimization', GitHub repository: https://github.com/bongiornoc/Compact-RIEnet, immutable commit 43234177d5830ba06203486c0b3abc98595e7eeb, July 2026."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Compact-RIEnet: Neural Network-Driven Volatility Drag Mitigation and Liquidation Delay under Aggressive Portfolio Leverage

## Provenance

- **Primary Source:** Christian Bongiorno, Efstratios Manolakis, and Rosario Nunzio Mantegna, *"Neural Network-Driven Volatility Drag Mitigation under Aggressive Leverage"*, arXiv preprint `arXiv:2607.23068v1 [q-fin.PM]`, submitted July 26, 2026.
- **Canonical DOI:** [10.48550/arXiv.2607.23068](https://doi.org/10.48550/arXiv.2607.23068) (also published in ACM ICAIF proceedings, DOI: [10.1145/3768292.3770370](https://doi.org/10.1145/3768292.3770370)).
- **Traceable Source URL:** `https://arxiv.org/abs/2607.23068` (HTML full text: `https://arxiv.org/html/2607.23068v1`).
- **Source Code Repository:** `https://github.com/bongiornoc/Compact-RIEnet`
- **Immutable Commit SHA:** `43234177d5830ba06203486c0b3abc98595e7eeb`
- **Author Affiliations:** CentraleSupélec, Université Paris-Saclay (Bongiorno, Manolakis); Università degli Studi di Catania (Manolakis); Università degli Studi di Palermo and University College London (Mantegna).
- **Data Period Evaluated:** 1990–2024 (35-year daily panel of US NYSE/NASDAQ common equities and ADRs; 2000–2024 25-year backtest).

## Economic mechanism

### Source-reported

In leveraged portfolio management with daily rebalancing back to a fixed target weight vector $\mathbf{w}$ and constant gross leverage $\ell > 0$, portfolio equity (Net Asset Value, NLV) compounds geometrically as:
$$m_{\Delta t} = m_0 \prod_{t=1}^{\Delta t} (1 + \ell \mathbf{w}^\top \mathbf{r}_t) = m_0 \exp\left[ \sum_{t=1}^{\Delta t} \ln(1 + \ell \mathbf{w}^\top \mathbf{r}_t) \right]$$

Applying a second-order Taylor expansion $\ln(1+x) \simeq x - \frac{1}{2}x^2$ around zero yields the expected compound growth rate:
$$\mathbb{E}\left[\ln(1 + \ell \mathbf{w}^\top \mathbf{r}_t)\right] \simeq \ell \mu - \frac{1}{2}\ell^2 \sigma^2$$
where $\mu = \mathbb{E}[\mathbf{w}^\top \mathbf{r}_t]$ is the unlevered expected portfolio return and $\sigma^2 = \mathbf{w}^\top \mathbf{\Sigma} \mathbf{w}$ is the unlevered portfolio variance.

The quadratic term $-\frac{1}{2}\ell^2 \sigma^2$ is the **volatility drag**—the geometric erosion of compound returns caused by price variance. Because volatility drag scales quadratically with leverage ($\ell^2$), doubling leverage quadruples the return erosion. Consequently, for any high-leverage investment program to remain viable without experiencing compounding decay or catastrophic margin breaches, minimizing the baseline portfolio variance $\sigma^2$ is an indispensable prerequisite.

Furthermore, under realistic institutional margin accounts (e.g., Regulation T or portfolio margin rules at prime brokers such as Interactive Brokers), adverse intraday price fluctuations trigger maintenance margin calls (typically at a 25% equity-to-asset maintenance threshold). Forced liquidations at intraday price troughs incur terminal capital destruction and transaction penalties. Minimizing portfolio variance directly depresses the probability of hitting maintenance margin limits, thereby extending the maximum deployable leverage corridor before the first forced liquidation occurs.

### Research interpretation

The strategy extracts risk-premia efficiency not by forecasting non-stationary drift $\boldsymbol{\mu}$ (which possesses notoriously low signal-to-noise ratios), but by solving an end-to-end variance minimization problem regularized across the empirical eigenvalue spectrum:

1. **Dimensionality Decoupling via Analytical Kernel Priors:** Conventional empirical covariance estimation suffers from severe sampling noise when the cross-sectional dimension $n$ approaches the lookback horizon $\Delta t_{\text{in}}$ (the Marchenko–Pastur noise limit in Random Matrix Theory). Rather than learning unconstrained matrix operators ($O(n^2)$ parameters), the architecture uses a five-parameter hyperbolic memory decay $\alpha_t$ and saturating exponential clipping $\beta_t$ that models long-memory volatility clustering while remaining invariant to both sample window length $\Delta t_{\text{in}}$ and universe size $n$.
2. **Spectral Eigencleaning via Bidirectional Recurrent Denoisers:** Empirical correlation eigenvalues $\lambda_1, \dots, \lambda_n$ are contaminated by finite-sample noise. Classical Nonlinear Shrinkage (NLS / Ledoit–Wolf) applies asymptotic mathematical shrinkage under strict Marchenko–Pastur assumptions. Compact-RIEnet replaces analytical shrinkage with a 16-hidden-unit Bidirectional GRU (BiGRU) that learns an implicit spectral shrinkage function directly from data against future realized out-of-sample covariance $\mathbf{\Sigma}_{\text{out}}$, correcting both noise-bulk inflation and market-mode distortion.
3. **Decoupled Marginal Volatility Rescaling:** Diagonal asset-specific variances are filtered independently through a per-asset 8-neuron MLP, ensuring that diagonal scaling is isolated from cross-sectional spectral rotation.
4. **Leverage Expansion Feasibility:** Because realized volatility is systematically compressed, an investor can apply elevated leverage ($\ell = 2.5 \text{ to } 3.5$) with lower peak-to-trough drawdowns and delayed forced liquidation relative to standard risk parity (HRP, ERC) or classical Random Matrix Theory shrinkage (QIS).

## Signal

The execution signal operates as a daily risk-optimized allocation policy derived from the internally assembled inverse covariance matrix $\mathbf{\Sigma}_{\text{NN}}^{-1}$:

- **Observation / Formation Timestamp:** Daily at market close $t$ (using prices and corporate actions settled through date $t$). Target shares are determined prior to execution and executed at the market close of day $t$.
- **Lookback Horizon:** Variable historical window $\Delta t_{\text{in}} \in [250, 1200]$ trading days (sampled uniformly during training, calibrated to $\Delta t_{\text{in}} = 1200$ days / 5 years in rolling annual backtest).
- **Module 1: Parametric Lag-Transformation (5 scalar parameters $\boldsymbol{\theta} \in \mathbb{R}_{>0}^5$):**
  For each historical lag $t \in \{1, \dots, \Delta t_{\text{in}}\}$ (with $t=1$ being the most recent day):
  $$\alpha_t = \theta_1 t^{-\theta_2} \quad (\text{hyperbolic weighting})$$
  $$\beta_t = \theta_3 - \theta_4 e^{-\theta_5 t} \quad (\text{saturating exponential clipping threshold})$$
  Transformed returns for asset $i$ at lag $t$:
  $$\widetilde{r}_{t,i} = \frac{\alpha_t}{\beta_t} \tanh\left(\beta_t r_{t,i}\right)$$
- **Module 2: Correlation Cleaning Module (BiGRU Spectral Denoiser):**
  - Compute sample correlation matrix $\mathbf{C} \in \mathbb{R}^{n \times n}$ from lag-transformed features $\widetilde{\mathbf{R}}$.
  - Eigendecomposition: $\mathbf{C} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^\top$, with sorted eigenvalues $\mathbf{\Lambda} = \text{Diag}(\lambda_1, \dots, \lambda_n)$ where $\lambda_1 \ge \dots \ge \lambda_n$.
  - Rank-wise eigenvalue token embedding:
    $$\mathbf{x}_i = \left\{ \lambda_i, \; q = \frac{n}{\Delta t_{\text{in}}}, \; \sqrt{n}, \; \sqrt{\Delta t_{\text{in}}} \right\} \in \mathbb{R}^4$$
  - Bidirectional GRU processing ($k = 16$ hidden units per direction):
    $$\mathbf{h}_i^\rightarrow = \text{GRU}_{k}^\rightarrow(\mathbf{h}_{i-1}^\rightarrow, \mathbf{x}_i), \quad \mathbf{h}_i^\leftarrow = \text{GRU}_{k}^\leftarrow(\mathbf{h}_{i+1}^\leftarrow, \mathbf{x}_i)$$
    $$\mathbf{h}_i = [\mathbf{h}_i^\rightarrow; \mathbf{h}_i^\leftarrow] \in \mathbb{R}^{32}$$
  - Denoised inverse eigenvalue output:
    $$\lambda_{i,\text{NN}}^{-1} = \text{softplus}(\boldsymbol{\gamma}^\top \mathbf{h}_i + \omega)$$
  - Reconstructed cleaned inverse correlation matrix:
    $$\mathbf{C}_{\text{NN}}^{-1} = \mathbf{Q} \text{Diag}(\lambda_{1,\text{NN}}^{-1}, \dots, \lambda_{n,\text{NN}}^{-1}) \mathbf{Q}^\top$$
- **Module 3: Marginal Volatility Network:**
  - Input: Empirical standard deviation $\widetilde{\sigma}_i$ of asset $i$ from lag-transformed return series.
  - Per-asset MLP (single hidden layer of 8 neurons with LeakyReLU activation, followed by softplus output):
    $$\sigma_{i,\text{NN}}^{-1} = \text{MLP}_8(\widetilde{\sigma}_i) > 0$$
  - Inverse diagonal volatility matrix: $\mathbf{D}_{\text{NN}}^{-1} = \text{Diag}(\sigma_{1,\text{NN}}^{-1}, \dots, \sigma_{n,\text{NN}}^{-1})$.
- **Module 4: Inverse Covariance Assembly & Allocation Weights:**
  - Assembled inverse covariance matrix:
    $$\mathbf{\Sigma}_{\text{NN}}^{-1} = \mathbf{D}_{\text{NN}}^{-1} \mathbf{C}_{\text{NN}}^{-1} \mathbf{D}_{\text{NN}}^{-1}$$
  - Unconstrained Global Minimum Variance (analytic):
    $$\mathbf{w}_{\text{unconstrained}} = \frac{\mathbf{\Sigma}_{\text{NN}}^{-1} \mathbf{1}}{\mathbf{1}^\top \mathbf{\Sigma}_{\text{NN}}^{-1} \mathbf{1}}$$
  - Practical Production Allocation (Long-Only Quadratic Program): Inverting $\mathbf{\Sigma}_{\text{NN}}^{-1}$ to obtain regularized covariance $\mathbf{\Sigma}_{\text{NN}}$, weights $\mathbf{w}_t$ are computed daily via QP:
    $$\min_{\mathbf{w}} \mathbf{w}^\top \mathbf{\Sigma}_{\text{NN}} \mathbf{w} \quad \text{subject to} \quad w_i \ge 0, \quad \sum_{i=1}^n w_i = 1$$
- **Leveraged Target Execution:**
  Target share quantity for asset $i$ on day $t$ under fixed gross leverage $\ell$:
  $$s_{t,i} = \text{round}\left( \frac{\ell \cdot w_{t,i} \cdot \widehat{\text{NLV}}'_t}{\hat{p}_{t,i}} \right)$$
  where $\widehat{\text{NLV}}'_t$ is the pre-trade net liquidation value estimated from opening/prior-close prices.

## Required data

- **Asset Universe:** US common equities and ADRs listed on the NYSE or NASDAQ (excluding mutual funds, closed-end funds, and ETFs).
- **Time Horizon:** 1990-01-01 through 2024-12-31 (35 years).
- **Universe Size & Cross-Sectional Dimension:** $n = 1000$ liquid assets re-evaluated daily.
- **Price & Fundamental Fields:**
  - Daily split-adjusted and dividend-adjusted closing prices ($p_{t,i}$), opening prices ($\hat{p}_{t,i}$), daily low prices, and daily trading volumes.
  - Number of shares outstanding and float-adjusted market capitalization.
  - Cash dividend distributions and corporate actions (mergers, delistings).
  - Effective Federal Funds Rate (FRED: `FEDFUNDS`) for borrowing and cash credit interest rates.
- **Data Cleaning & Point-in-Time Universe Selection:**
  - **Look-Ahead Prevention:** Universe selection on day $t$ uses information strictly available up to $t-1$. Any security undergoing a delisting within the subsequent $\Delta t_{\text{out}} = 5$ days is removed.
  - **Tier 1 (Historical Completeness):** Security must have participated in $\ge 95\%$ of closing auctions in every rolling 1-year subperiod across the 5-year calibration window ($\Delta t_{\text{in}} = 1200$ days).
  - **Tier 2 (Short-Term Microstructure Liquidity):** Over the trailing 5 trading days: (a) 100% closing auction participation, (b) average daily volume $\ge 1\%$ of shares outstanding, and (c) average daily dollar turnover $\ge 1\%$ of market capitalization.
  - **Price and Scale Bounds:** Shares outstanding $\ge 5,000,000$; closing price strictly between $\$10$ and $\$2,000$ on day $t-1$.
  - **Univariate Outlier Filter:** Log-standard deviation of returns must exceed the 1.5 Inter-Quartile Range (IQR) lower bound over both 5-day and 20-day windows, preventing the optimizer from collapsing into trivial, illiquid low-risk outliers.
  - **Redundancy & Collinearity Filter:** For multiple share classes, only the largest market-cap class is retained. Any pair with pairwise correlation $> 0.95$ drops one member.
  - **Final Rank:** Top $n = 1000$ names by trailing market capitalization form the daily portfolio universe.

## Execution assumptions

- **Execution Venue & Timing:** Orders submitted prior to close and executed at primary exchange daily closing prices $p_{t,i}$ (MOC orders).
- **Margin Account Model:** Continuous-time simulation of an Interactive Brokers cash-and-margin account:
  - **Cash Balance & Financing:** Negative cash balances incur daily debit interest at the Effective Fed Funds Rate plus broker spread (360-day convention). Positive balances above $\$100,000$ earn tiered credit interest.
  - **Commissions (IBKR Tiered):** $\$0.00035$ per share for monthly volume $< 300,000$ shares; $\$0.00020$ per share thereafter; minimum ticket charge of $\$0.35$.
  - **Exchange & Clearing Fees:** $0.0845\%$ of executed notional.
  - **Regulatory Fees:** SEC Section 31 fee on sales at $1.157$ bps ($0.01157\%$).
- **Maintenance Margin & Liquidation Stress Test:**
  - Permitted gross leverage up to $4:1$ (initial leverage $\ell \in [0.01, 3.99]$, baseline test at $\ell = 3.0$).
  - Maintenance margin requirement: $25\%$ equity / asset ratio.
  - **Intraday Margin Stress Evaluation:** Account equity is evaluated intraday using position-level intraday low prices, conservatively assuming all 1,000 portfolio assets simultaneously hit their daily lows.
  - Low price is floored at $\max\left(\text{low}, \; 0.85 \min(\text{open}, \text{close})\right)$ to cap maximum intraday recognized gap risk at $15\%$.
  - If the simulated intraday margin ratio breaches $25\%$, the account undergoes automatic forced liquidation: sufficient shares are liquidated pro-rata at intraday lows to restore the equity ratio to $27\%$ ($2$ percentage points above maintenance), paying full commissions and regulatory fees.
- **Market Impact:** Zero price impact assumed (exogenous displayed closing prices). The paper notes that while this assumption is realistic for liquid large-cap US stocks at modest fund sizes, it represents an unmodeled friction for large AUM.

## Evidence

### Source-reported

Evaluated over a 25-year backtest (2000-01-01 to 2024-12-31) starting with $\$1,000,000$ initial capital, using rolling annual retraining across 24 separate out-of-sample yearly periods. Compared against 8 established asset allocation benchmarks: Average Oracle (AO), Quadratic-Inverse Shrinkage (QIS / Ledoit–Wolf 2022), Hierarchical Risk Parity (HRP / de Prado 2016), Equal Risk Contribution (ERC / Maillard et al. 2010), Equal Risk Budget (ERB), Maximum Likelihood Sample Covariance (MLE), Equal Weighting (EW), and Market-Cap Weighting (MCW).

**Table 1: Out-of-Sample Performance Summary Across 400 Leverage Grid Points ($0.01 \le \ell \le 3.99$):**

| Method | First Forced Liquidation Leverage ($\ell_{\text{liq}}$) | Incremental Efficiency ($b/a = \frac{\partial \mu / \partial \ell}{\partial \sigma / \partial \ell}$) | Sharpe Ratio at $\ell = 3.0$ | Annualized Volatility at $\ell = 3.0$ | Max Drawdown at $\ell = 3.0$ | Model Confidence Set $p$-value at $\ell = 3.0$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Compact-RIEnet (NN)** | **2.77** | **1.08** | **1.12** | **0.36** | **-0.77** | **1.000** |
| **Average Oracle (AO)** | 2.73 | 0.95 | 0.99 | 0.38 | -0.83 | 0.013 |
| **Quadratic-Inverse Shrinkage (QIS)** | 2.70 | 0.82 | 0.87 | 0.39 | -0.85 | 0.002 |
| **Maximum Likelihood Estimator (MLE)**| 2.69 | 0.85 | 0.89 | 0.38 | -0.86 | 0.002 |
| **Hierarchical Risk Parity (HRP)** | 2.66 | 0.94 | 0.88 | 0.53 | -0.89 | 0.001 |
| **Equal Risk Contribution (ERC)** | 2.63 | 0.89 | 0.89 | 0.57 | -0.90 | 0.002 |
| **Equal Risk Budget (ERB)** | 2.63 | 0.78 | 0.79 | 0.55 | -0.91 | 0.000 |
| **Equally-Weighted (EW)** | 2.62 | 0.86 | 0.86 | 0.63 | -0.92 | 0.001 |
| **Market-Cap Weighted (MCW)** | 2.61 | 0.32 | 0.28 | 0.59 | -0.98 | 0.000 |

Key Quantitative Findings from Table 1 and Section 6:
1. **Delayed Forced Liquidation:** Compact-RIEnet pushes the first liquidation point to $\ell_{\text{liq}} = 2.77$, outlasting all competing covariance filters ($\ell_{\text{liq}} \in [2.61, 2.73]$).
2. **Superior Incremental Efficiency:** In the unconstrained leverage region ($0.5 \le \ell \le 2.5$), realized volatility scales linearly as $\sigma(\ell) \simeq a \cdot \ell$ with $a_{\text{NN}} = 0.1208$ (lowest among all models, vs $0.1275$ for AO, $0.1284$ for QIS, and $0.2089$ for EW). Mean return grows with slope $b = \partial \mu / \partial \ell$. Compact-RIEnet is the **only** estimator satisfying $b/a > 1.0$ ($b_{\text{NN}}/a_{\text{NN}} = 1.08$), proving that incremental leverage yields more return than incremental risk.
3. **High-Leverage Risk-Adjusted Performance ($\ell = 3.0$):** Compact-RIEnet achieves Sharpe ratio $1.12$ with $36\%$ volatility and $-77\%$ maximum drawdown. In a 5% Model Confidence Set (MCS; Hansen et al. 2011) test using 100,000 stationary block bootstrap resamples, Compact-RIEnet is the **sole** surviving strategy in the superior set ($p = 1.000$; nearest rival AO has $p = 0.013$, rejected at 5% significance).
4. **Parameter Compression:** Parameter count reduced from $39,586$ (legacy RIEnet) to $2,175$ parameters ($94.5\%$ reduction) with zero degradation in out-of-sample variance minimization performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Statistical Equivalence to Legacy Architecture:** When the legacy 39,586-parameter RIEnet (Bongiorno et al. 2025) is included in the Model Confidence Set, the test cannot reject equal performance between Compact-RIEnet and the legacy model. The compact formulation saves compute, memory, and training time, but does not generate higher raw Sharpe ratios than the larger model.
- **Severe Maximum Drawdowns under Extreme Leverage:** Despite outperforming benchmarks, operating at $\ell = 3.0$ produces a realized maximum drawdown of $-77\%$. High leverage remains vulnerable to macro regime shifts (such as the 2008 Global Financial Crisis and March 2020 COVID shock) where market-wide correlations converge toward $1.0$.
- **Omission of Price Impact:** The simulation assumes exogenous prices without market impact. For institutional capital (e.g. $> \$50\text{M}$ AUM rebalancing daily across 1,000 equities), market impact in closing auctions would erode net returns and trigger earlier liquidations.
- **Infeasibility of Pure Long-Short Without Drift Alpha:** The authors explicitly note that unconstrained long-short minimum-variance optimization with realistic short borrowing fees was impractical without reliable return forecasting; the architecture had to be deployed via long-only quadratic programming constraints to prevent borrow-cost bleed.

## Falsification plan

1. **Market Impact Haircut Test:** Implement an Almgren–Chriss square-root impact cost model $\Delta P / P = \eta \sigma \sqrt{V_{\text{trade}} / V_{\text{ADV}}}$ calibrated to institutional AUM levels ($\$10\text{M}$, $\$50\text{M}$, $\$100\text{M}$). If the first liquidation threshold at $\$50\text{M}$ AUM collapses from $\ell_{\text{liq}} = 2.77$ to below $2.30$, the thesis that neural variance minimization enables aggressive leverage in practical deployment is falsified.
2. **Ablation of BiGRU Spectral Denoiser:** Replace the BiGRU eigencleaning module with an identity matrix (raw sample eigenvalues) or a constant scalar shrinkage parameter while retaining the 5-parameter lag-transformation. If the resulting portfolio achieves Sharpe ratio $\ge 1.05$ at $\ell = 3.0$, the hypothesis that sequential bidirectional recurrent denoising provides statistically significant incremental alpha over simple shrinkage is disproven.
3. **Cross-Asset Transferability Without Retraining:** Evaluate the pre-trained 2,175-parameter model directly on European (STOXX 600) and Japanese (Nikkei 225) equity panels without fine-tuning. If realized out-of-sample portfolio variance exceeds that of Quadratic-Inverse Shrinkage (QIS) by $> 5\%$, the claim that the architecture decouples complexity and generalizes across universes without retraining is falsified.
4. **Intraday Tick-Level Margin Breach Audit:** Evaluate the strategy against actual tick-level intraday drawdown histories (rather than daily low approximations). If intraday tick-level drawdowns trigger $> 5$ additional forced liquidations during the 2020 crash, the margin resilience claim is invalidated.
5. **Rejection Rule:** If out-of-sample Sharpe ratio at $\ell = 2.0$ over any trailing 36-month rolling window falls below $0.40$ or experiences $> 2$ margin liquidations, freeze model evaluation.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Porting Rationale:** The core mathematical mechanism—compressing portfolio variance $\mathbf{w}^\top \mathbf{\Sigma} \mathbf{w}$ to mitigate quadratic volatility drag $-\frac{1}{2}\ell^2 \sigma^2$ and delay liquidation—is theoretically applicable to leveraged crypto spot and perpetual baskets (e.g., top 30–50 altcoins on Binance, Bybit, or OKX).
- **Crypto-Specific Impediments & Hazards:**
  1. **Extreme Systematic Co-Movement:** Unlike US equities where idiosyncratic risk is substantial ($40\text{--}60\%$ of total variance), crypto assets exhibit extreme Bitcoin-beta dominance. Pairwise altcoin correlations often surge above $0.85\text{--}0.95$ during market selloffs, severely compressing the eigenvalue spectrum and eliminating the diversification benefits required by minimum-variance portfolios.
  2. **Continuous Intraday Margin Engines:** Equity margin calls occur at or after market close with discretionary broker cure periods. In crypto perpetuals, margin engines operate continuously at sub-second latency. Flash-wicks driven by cascade liquidations trigger immediate, irreversible liquidation without warning.
  3. **Funding Rate Carry Asymmetry:** Holding leveraged perpetual futures incurs 8-hour funding rate payments. In bullish regimes, long positions in altcoins carry annualized funding costs of $20\%\text{--}80\%$, which would rapidly consume any incremental variance-reduction gain.
  4. **Liquidity Fragmentation & Survivorship:** The crypto universe undergoes extreme turnover, exchange delistings, and illiquid order books, violating the 5-year continuous listing criteria ($\Delta t_{\text{in}} = 1200$ days) required by the training pipeline.

## Limitations

- **Not Independently Reproduced:** All reported statistics, liquidation thresholds, and regression numbers are third-party empirical findings from Bongiorno, Manolakis, and Mantegna (arXiv:2607.23068v1).
- **Exogenous Price Assumption:** The backtest simulator does not model endogenous market impact, which becomes material under multi-million dollar leveraged rebalancing.
- **Severe Tail Drawdowns:** Maximum drawdown at $3\times$ leverage reaches $-77\%$, requiring rigorous institutional risk overrides.
- **Lookback Data Requirements:** The initial universe filter requires 5 years of continuous daily closing auction participation, restricting the strategy to mature large-cap equities.

## Implementation status

`not-implemented`. This strategy research record represents normalized academic research capture. No implementation exists in PyBroker, NautilusTrader, or production execution engines.

## Adoption boundary

`research-only`. This document is intended solely for research analysis and hypothesis generation. It does not constitute approval for strategy implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/portfolio-covariance-and-shrinkage-2026-08-28]]`
- `[[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]`
- `[[quant/fractional-kelly-2026-08-28]]`
- `[[quant/expected-shortfall-and-risk-of-ruin-2026-08-28]]`
- `[[quant/execution-impact-capacity-almgren-square-root-2026-08-28]]`
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]`
- `[[quant/phase8-regularized-nonlinear-ml-toolbox-2026-08-28]]`
- `[[quant/phase9-factor-covariance-redundancy-risk-decomposition-2026-08-28]]`
- `[[quant/phase10-universe-lifecycle-survivorship-2026-08-28]]`
- `[[quant/phase12-implementation-shortfall-tca-markouts-maker-taker-2026-08-28]]`

## Sources

- Christian Bongiorno, Efstratios Manolakis, and Rosario Nunzio Mantegna, *"Neural Network-Driven Volatility Drag Mitigation under Aggressive Leverage"*, arXiv preprint `arXiv:2607.23068v1 [q-fin.PM]`, submitted July 26, 2026. DOI: [10.48550/arXiv.2607.23068](https://doi.org/10.48550/arXiv.2607.23068). ACM ICAIF DOI: [10.1145/3768292.3770370](https://doi.org/10.1145/3768292.3770370). Stable URL: `https://arxiv.org/abs/2607.23068`.
- Christian Bongiorno, *"Compact-RIEnet: Compact Reformulation of Modular End-to-End Neural Network for Global Minimum-Variance Portfolio Optimization"*, GitHub repository: `https://github.com/bongiornoc/Compact-RIEnet`, immutable commit `43234177d5830ba06203486c0b3abc98595e7eeb`, July 2026.
