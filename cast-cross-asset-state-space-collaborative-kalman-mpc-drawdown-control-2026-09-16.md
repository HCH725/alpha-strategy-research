---
schema: strategy-research-record-v1
title: "CAST: Cross-Asset State-Space Collaborative Kalman Filter with Model Predictive Control for Drawdown Control"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - state-space
  - kalman-filter
  - model-predictive-control
  - cross-asset
  - drawdown-control
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "Yu Peng, Matloob Khushi, and Josiah Poon, 'CAST: A Cross-Asset State-Space Trading System for Drawdown Control in Stock Markets', arXiv:2609.14205v1 [cs.AI, q-fin.TR], September 13, 2026. https://arxiv.org/abs/2609.14205"
  - "FanBroWell/CAST GitHub repository, commit 8ae60cf28aebd93e6499312bdbf93ad839890756, https://github.com/FanBroWell/CAST"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CAST: Cross-Asset State-Space Collaborative Kalman Filter with Model Predictive Control for Drawdown Control

## Provenance

- **Primary Research Paper:**
  - Authors: Yu Peng, Matloob Khushi, and Josiah Poon (School of Computer Science, The University of Sydney).
  - Title: *"CAST: A Cross-Asset State-Space Trading System for Drawdown Control in Stock Markets"*.
  - Publication: arXiv preprint `arXiv:2609.14205v1 [cs.AI, q-fin.TR]`, submitted September 13, 2026.
  - Abstract URL: https://arxiv.org/abs/2609.14205
  - Full-Text HTML: https://arxiv.org/html/2609.14205v1
  - Full-Text PDF: https://arxiv.org/pdf/2609.14205v1
  - Canonical DOI: [10.48550/arXiv.2609.14205](https://doi.org/10.48550/arXiv.2609.14205)

- **Primary Source Code Repository:**
  - URL: https://github.com/FanBroWell/CAST
  - Full Immutable Commit SHA: `8ae60cf28aebd93e6499312bdbf93ad839890756`
  - Inspected Paths: `README.md`, `APPENDIX.md`, `src/mpc.py`, `src/filter/cokf.py`, `src/filter/single_ckf.py`, `src/backtest.py`, `experiments/m30_main_results.py`.

- **Verification Integrity:**
  - The complete full-text HTML and the exact public GitHub codebase (commit `8ae60cf28aebd93e6499312bdbf93ad839890756`) were directly retrieved and inspected.
  - All state-space operator definitions, dynamic credibility equations, MPC linear programming formulations, constraint stacks, ablation findings, and multi-market performance metrics trace directly to the primary paper text and repository source files.
  - No secondary summaries, search engine snippets, or model-generated hallucinations were used to formulate strategy rules or empirical claims.

- **Repository Deduplication Audit:**
  - A comprehensive search of all existing records in `alpha-strategy-research` confirmed zero existing records matching `arXiv:2609.14205`, `FanBroWell/CAST`, Yu Peng, Matloob Khushi, Josiah Poon, or the CAST framework.
  - Related records examining Kalman filters in the repository (`sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md`, `tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12.md`) focus on pairs-trading hedge ratio estimation and forensic unbounded drift falsification.
  - Related records on state-space models (`strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02.md`) investigate deep selective state spaces (Mamba/S4) for cross-sectional ranking rather than recursive Kalman-MPC drawdown control.

## Economic mechanism

### Source-reported

Mainstream stock price forecasting methods predominantly train deep neural networks or statistical models offline under the independent and identically distributed (i.i.d.) assumption. Real equity markets violate this assumption: distributions shift across market regimes, and asset prices exhibit strong cross-sectional correlation. When an offline-trained model encounters a regime shift or macroeconomic shock (e.g., 2008 GFC, 2020 COVID-19 crash, 2022 rate-hike shock), its forecasts degrade, triggering severe compounding drawdowns that threaten fund survival.

CAST resolves this failure mode by replacing offline frozen models with online recursive state-space estimation coupled to an explicit control layer:
1. **Predictor (Cross-Asset Collaborative Kalman Filter, CoKF):** Tracks latent price trajectories using three parallel integrated random walk (IRW) models of degrees $r \in \{1, 2, 3\}$ (representing constant level, linear velocity, and acceleration/curvature). CoKF dynamically weights each order's credibility online based on its recent $L$-step squared forecast error, allowing the effective dynamical order to adapt without retraining. Crucially, CoKF couples all $M$ assets by embedding their empirical correlation matrix $\boldsymbol{\rho}$ into the off-diagonal blocks of the joint process-noise covariance matrix $\widetilde{Q}$, ensuring market-wide shocks update all latent states simultaneously.
2. **Controller (Model Predictive Control, MPC):** Decomposes portfolio trading into $M$ risk-isolated accounts and plans an $L$-step trading trajectory daily. MPC formulates an objective that maximizes predicted cumulative horizon profit while penalizing position sizes scaled by the predictor's forecast uncertainty $\omega_l$ and risk aversion $\lambda$. Only the first planned trade $u_{k+1}$ is executed, and the optimization is re-solved at every bar, converting posterior filter uncertainty directly into automated de-risking during market crises.

### Research interpretation

The primary alpha mechanism is not an unconstrained directional prediction edge, but an **adaptive state-space trend/curvature filter combined with an uncertainty-gated inventory controller**:
- **Dynamical Order Switching as Regime Filter:**
  - Degree $r=1$ assumes a pure random walk ($P_{k+1} = P_k + w_k$); its directional forecast is zero ($\Delta \hat{P} = 0$), producing zero trades.
  - Degrees $r=2$ and $r=3$ generate linear and quadratic trend projections.
  - During stable trending regimes, orders 2 and 3 exhibit low forecast errors and capture directional momentum. During choppy or crashing regimes, orders 2 and 3 produce large forecast errors; the credibility weight rapidly shifts toward order 1 ($r=1$), automatically dampening directional aggression and flattening positions.
- **Cross-Asset Process-Noise Coupling:**
  - Because market shocks impact latent asset dynamics rather than idiosyncratic measurement noise, cross-asset correlation $\boldsymbol{\rho}$ belongs strictly in process noise $\widetilde{Q}$.
  - When a leading asset experiences an abrupt movement, the Kalman gain immediately propagates that information across the correlated off-diagonals of $\widetilde{Q}$, updating the latent velocities of peer assets before their own prices have fully completed the move.
- **Uncertainty-Gated MPC De-Risking:**
  - The risk penalty $\lambda \sum_l |u_{k+l}| \omega_l$ links position sizing to multi-step forecast variance $\omega_l = c \sqrt{\sum_{j=0}^{l-1} [\bar{F}^j]_{1,1}^2}$.
  - In periods of heightened volatility or diverging filter predictions, $\omega_l$ inflates rapidly. Because the penalty is linear in transaction size $|u|$, it overrides marginal expected return, compelling the linear program to reduce trade sizes or unwind existing holdings into cash before drawdowns compound.

## Signal

### Formation timestamp

- Observations are formed on daily close prices $P_k^{(i)}$ of day $k$.
- Trading decisions $u_{k+1}^{(i)}$ are computed at the close of day $k$ and executed at the close of day $k+1$ (next-day close execution convention) `[source-reported]`.

### Lookback and Calibration

- **Offline Parameter Calibration Window:** 2005-01-03 to 2009-12-31 (~5 years) `[source-reported]`:
  - Process noise variance $\sigma_v^{(i)}$ and observation noise variance $\sigma_w^{(i)}$ calibrated once per asset via grid search on 1-step RMSE over calibration data, then frozen `[source-reported]`.
  - Correlation matrix $\boldsymbol{\rho} \in \mathbb{R}^{M \times M}$: Pearson correlation of raw price first differences over the calibration window, symmetrized, unit diagonal, NaN set to 0, then frozen `[source-reported]`.
- **Online Recursive Lookback Window:**
  - The model does not use a sliding window of historical raw bars for retraining.
  - Credibility scoring lookback: $L = 7$ trading days. Each filter's credibility is evaluated on its realized $L$-step squared forecast errors over the preceding $L$ days `[source-reported]`.

### Mathematical Signal Construction

1. **State-Space Operators (for order $r \in \{1, 2, 3\}$):**
   - Individual companion transition matrix $F \in \mathbb{R}^{r \times r}$, observation vector $H = [1, 0, \dots, 0] \in \mathbb{R}^{1 \times r}$.
   - Joint transition operator across $M$ assets: $\widetilde{F} = \text{blkdiag}(F, \dots, F) \in \mathbb{R}^{Mr \times Mr}$.
   - Joint observation operator: $\widetilde{H} \in \mathbb{R}^{M \times Mr}$ where $\widetilde{H}[i, (i-1)r + 1] = 1$.
   - Joint observation noise covariance: $\widetilde{W} = \text{diag}\left((\sigma_w^{(1)})^2, \dots, (\sigma_w^{(M)})^2\right) \in \mathbb{R}^{M \times M}$.
   - Joint process noise covariance: $\widetilde{Q} \in \mathbb{R}^{Mr \times Mr}$ where $\widetilde{Q}[(i-1)r + 1, (j-1)r + 1] = \rho_{ij} \sigma_v^{(i)} \sigma_v^{(j)}$, and all other entries are 0 `[source-reported]`.

2. **Recursive Kalman Filtering:**
   - State prediction: $\mathbf{X}_{k|k-1}^{(r)} = \widetilde{F} \mathbf{X}_{k-1|k-1}^{(r)}$
   - Covariance prediction: $\mathbf{P}_{k|k-1}^{(r)} = \widetilde{F} \mathbf{P}_{k-1|k-1}^{(r)} \widetilde{F}^\top + \widetilde{Q}$
   - Measurement update: $\mathbf{X}_{k|k}^{(r)} = \mathbf{X}_{k|k-1}^{(r)} + K_k \left( \mathbf{P}_k - \widetilde{H} \mathbf{X}_{k|k-1}^{(r)} \right)$
   - Kalman gain: $K_k = \mathbf{P}_{k|k-1}^{(r)} \widetilde{H}^\top \left( \widetilde{H} \mathbf{P}_{k|k-1}^{(r)} \widetilde{H}^\top + \widetilde{W} \right)^{-1}$
   - Covariance update: $\mathbf{P}_{k|k}^{(r)} = (I - K_k \widetilde{H}) \mathbf{P}_{k|k-1}^{(r)}$ (symmetrized each step) `[source-reported]`.

3. **Multi-Order Credibility Weighting:**
   - For each asset $i$ and order $r$, compute $L$-step trajectory squared error:
     $$E_{k}^{(i, r)} = \sum_{l=1}^{L} \left( P_{k-L+l}^{(i)} - \hat{P}_{k-L+l|k-L}^{(i, r)} \right)^2 + \delta, \quad \delta = 10^{-12}$$
   - Compute normalized credibility weight:
     $$\mu_k^{(i, r)} = \frac{\left(E_k^{(i, r)}\right)^{-L/2}}{\sum_{m=1}^R \left(E_k^{(i, m)}\right)^{-L/2}}$$
   - Asset $i$'s combined $L$-step predicted price path:
     $$\bar{\mathbf{P}}_k^{(i)} = \sum_{r=1}^R \mu_k^{(i, r)} \hat{\mathbf{P}}_k^{(i, r)} \in \mathbb{R}^L$$

4. **MPC Optimization (Per-Asset Linear Program):**
   - At day $k$, for asset $i$, solve for trade plan $u_{k+1}, \dots, u_{k+L-1}$ over $n = L - 1$ steps:
     $$\max_{u_{k+1}, \dots, u_{k+L-1}} \sum_{l=1}^{L-1} \left( u_{k+l} \Delta \bar{P}_{k+l|k}^{(i)} - \lambda \omega_l |u_{k+l}| \right)$$
     subject to:
     $$\sum_{l=1}^{L-1} u_{k+l} = -u_{\text{applied}} \quad \text{(unwind constraint)}$$
     $$|u_{k+l}| \bar{P}_{k+l|k}^{(i)} \leq \beta V_k^{(i)} \quad \text{(per-trade cap, } \beta = 0.5\text{)}$$
   - Here $\Delta \bar{P}_{k+l|k}^{(i)} = \bar{P}_{k+l|k}^{(i)} - \bar{P}_{k+l-1|k}^{(i)}$, and forecast standard deviation is:
     $$\omega_l = c \cdot \sqrt{\sum_{j=0}^{l-1} \left[ \bar{F}^j \right]_{1,1}^2}, \quad \bar{F} = \sum_{r=1}^R \mu_k^{(i, r)} F^{(r)}, \quad c = 1.5$$
   - The $L_1$ norm $|u_{k+l}|$ is linearized with auxiliary slack variables $z_l \geq |u_{k+l}|$, solved via HiGHS interior-point/simplex solver `[source-reported]`.

5. **Position Sizing and Execution:**
   - Execute only the first planned increment $u_{k+1}$.
   - Apply no-leverage clipping:
     $$u_{\text{committed}} = \text{clip}\left(u_{k+1}, -\frac{V_k}{P_k} - N_k, \frac{V_k}{P_k} - N_k\right)$$
     ensuring gross position value $|(N_k + u) P_k| \leq V_k$ at all times `[source-reported]`.
   - Long entry / addition occurs when $u_{\text{committed}} > 0$.
   - Short entry / addition occurs when $u_{\text{committed}} < 0$.

### Exit and De-risking Logic

- **Horizon Unwind:** The equality constraint $\sum_{l=1}^{L-1} u_{k+l} = -u_{\text{applied}}$ mechanically unwinds open positions over $L$ steps unless new directional signals renew exposure `[source-reported]`.
- **Uncertainty De-risking:** When forecast variance $\omega_l$ expands, the risk penalty $\lambda \omega_l$ suppresses $|u|$, preventing entry or scaling down active positions `[source-reported]`.
- **Margin Floor Stop:** If account equity breaches $V_k < 0.2 \cdot V_0$ ($200 on a $1,000 account), the position is immediately liquidated to cash and trading permanently ceases for that asset `[source-reported]`.

### Parameters

All parameters are specified by the primary source and repository:
- $L = 7$ trading days (MPC planning horizon and credibility error lookback) `[source-reported]`.
- $r \in \{1, 2, 3\}$ (IRW model orders: constant, linear, quadratic) `[source-reported]`.
- $\beta = 0.5$ (per-trade transaction value cap as a fraction of equity) `[source-reported]`.
- $V_0 = \$1,000$ (initial capital per asset account) `[source-reported]`.
- $c = 1.5$ (forecast uncertainty scaling multiplier) `[source-reported]`.
- $\lambda \in \{0.05, 0.1, 0.3, 0.6\}$ (risk aversion parameter; tested as fixed grid or monthly adaptive switching) `[source-reported]`.
- $\delta = 10^{-12}$ (credibility denominator stability floor) `[source-reported]`.
- Margin floor fraction = $0.20$ of initial capital $V_0$ `[source-reported]`.
- Annualization factor = 252 trading days `[source-reported]`.
- If an adaptive or modified parameter set is deployed in an alternative asset class, label `research-proposed`.

## Required data

- **Instrument Universe:** Equity baskets. Primary study evaluates four distinct 30-stock panels ($M = 30$):
  1. `NASDAQ`: 30 US large-caps across 6 sectors (financials, real estate, mature tech, biotech, consumer, industrials). Mean calibration correlation $\bar{\rho} = 0.38$.
  2. `CSI300`: 30 Chinese A-share large-caps selected for high pairwise correlation on 2005–2010. Mean calibration correlation $\bar{\rho} = 0.43$.
  3. `TPX100`: 30 Tokyo Stock Exchange large-caps across 10 sectors. Mean calibration correlation $\bar{\rho} = 0.38$.
  4. `Global30`: 30 multi-currency blue chips spanning 5 currency zones (USD, EUR, JPY, GBP, HKD, CNY, DKK). Mean calibration correlation $\bar{\rho} = 0.20$ `[source-reported]`.
- **Venue:** National exchanges (NASDAQ, NYSE, SSE, SZSE, TSE, LSE, Euronext, HKEX) `[source-reported]`.
- **Timeframe:** Daily bars (adjusted close prices) `[source-reported]`.
- **Fields:** Single-series close price $P_t^{(i)}$ per asset. No volume, order book, or alternative data required `[source-reported]`.
- **Point-in-Time Integrity:**
  - Calibration partition: 2005-01-03 to 2009-12-31 (~5 years).
  - Out-of-sample test partition: 2010-01-04 to 2025-04-30 (15+ years).
  - Strict separation: no test-segment data is accessed during noise/correlation calibration `[source-reported]`.
- **Normalization:**
  - Raw prices used for `NASDAQ`, `CSI300`, and `TPX100`.
  - For `Global30`, each stock series is divided by its price on the first day of the panel (2005-01-03) to eliminate currency-scale disparities across USD, EUR, JPY, GBP, etc. `[source-reported]`.
- **Missing Data:** Zero missing values in the twenty-year panels; fill policy is `ffill().bfill()` `[source-reported]`.
- **Data Gap / Operational Rule:** In live trading or non-equities, missing bars or halted trading must trigger a flat position action `[research-proposed]`.

## Execution assumptions

- **Signal-to-Order Delay:** 1 trading day. Trade decisions $u_{k+1}$ calculated at day $k$ close are filled at day $k+1$ close `[source-reported]`.
- **Order Type:** Market-on-close / market order at next close `[source-reported]`.
- **Fill Model:** Deterministic fill at next-day close price $P_{k+1}$ `[source-reported]`.
- **Transaction Fees:** $0.00\%$ in primary benchmark (frictionless backtest) `[source-reported]`.
- **Slippage and Spread:** $0.00\%$ modeled in primary benchmark `[source-reported]`.
- **Market Impact / Capacity:** Not modeled in primary benchmark `[source-reported]`.
- **Borrow Costs and Shorting Constraints:** Frictionless shorting assumed; short positions held without borrow fee, locate limits, or short-sale circuit breakers `[source-reported]`.
- **Leverage / Margin:** Zero leverage. Position size clipped so gross market value $|(N_k + u) P_k| \leq V_k$ `[source-reported]`.
- **Operational Reality:** In any real-world live trading or paper simulation, a minimum fee of 5–10 bps and 5 bps slippage must be applied `[research-proposed]`.

## Evidence

### Source-reported

All empirical figures trace directly to Peng, Khushi & Poon (`arXiv:2609.14205v1`, Tables I–V, Section IV & V) and repository `APPENDIX.md`:

1. **Overall Performance (15-Year Test Window, 2010–2025, 30 Independent Accounts per Panel):**
   - **NASDAQ ($M=30$):**
     - CAST (Fixed $\lambda$): Annualized Sharpe = 0.523, Maximum Drawdown = 11.4% (0.114), Calmar Ratio = 0.448.
     - CAST (Adaptive $\lambda$, monthly): Annualized Sharpe = 0.717, Maximum Drawdown = 11.7% (0.117).
     - CKF (Single-Asset Collaborative): Fixed Sharpe = 0.339, MaxDD = 10.3%; Adaptive Sharpe = 0.392, MaxDD = 13.5%.
   - **CSI300 ($M=30$):**
     - CAST (Fixed $\lambda$): Annualized Sharpe = 0.269, Maximum Drawdown = 15.8% (0.158), Calmar Ratio = 0.177.
     - CAST (Adaptive $\lambda$, monthly): Annualized Sharpe = 0.248, Maximum Drawdown = 15.5% (0.155).
     - CKF: Fixed Sharpe = 0.138, MaxDD = 21.8%; Adaptive Sharpe = -0.007, MaxDD = 19.3%.
   - **TPX100 ($M=30$):**
     - CAST (Fixed $\lambda$): Annualized Sharpe = 0.228, Maximum Drawdown = 13.4% (0.134), Calmar Ratio = 0.198.
     - CAST (Adaptive $\lambda$, monthly): Annualized Sharpe = 0.227, Maximum Drawdown = 21.2% (0.212).
     - CKF: Fixed Sharpe = 0.384, MaxDD = 15.0%; Adaptive Sharpe = 0.222, MaxDD = 13.6%.
   - **Global30 ($M=30$):**
     - CAST (Fixed $\lambda$): Annualized Sharpe = 0.516, Maximum Drawdown = 3.1% (0.031), Calmar Ratio = 1.050.
     - CAST (Adaptive $\lambda$, monthly): Annualized Sharpe = 0.483, Maximum Drawdown = 10.5% (0.105).
     - CKF: Fixed Sharpe = 0.331, MaxDD = 10.7%; Adaptive Sharpe = 0.237, MaxDD = 10.7%.

2. **Comparison with Mainstream Deep Learning / Transformer Baselines:**
   - 15 external baselines tested (Informer, PatchTST, iTransformer, DLinear, TiDE, TimeMixer, ALSTM, RSR, ESTIMATE, THGNN, MASTER, StockMixer, DDG-DA, DoubleAdapt, Enhancer).
   - Only 3 of 15 baselines maintained positive Sharpe ratios across all four markets (Informer, DLinear, StockMixer).
   - Distribution-shift adaptation methods (DoubleAdapt, DDG-DA, Enhancer) suffered drawdowns of 35% to 65% and negative Sharpe ratios in multiple markets.
   - CAST occupied the empirical Pareto frontier of Final Value vs. Maximum Drawdown across all four markets.

3. **Crisis Stress Testing (COVID-19 2020 & Rate-Hike 2022 Crashes):**
   - Market buy-and-hold drawdowns during crisis periods ranged between -15% and -34%.
   - CAST restricted portfolio drawdown to low single digits across both crises (lowest at 0.9%, maximum 4.2%).

4. **Component Ablation Findings (Section V, Tables IV & V):**
   - **Removing Risk Penalty ($\lambda = 0$):** Maximum drawdown escalated to ~80% in NASDAQ and CSI300; ending account capital collapsed from $1,000 to $200 and $240.
   - **Removing MPC Multi-Step Horizon ($L = 1$ single-step decision):** NASDAQ Sharpe collapsed from +0.52 to -0.27; MaxDD surged from 11.4% to 46.7%.
   - **Single-Order IRW Models:**
     - Order $r=1$ (random walk): zero trades executed (no directional gradient).
     - Order $r=2$ (linear) and $r=3$ (quadratic): negative Sharpe ratios and drawdowns exceeding 40%.
     - Collaborative multi-order aggregation (CKF/CoKF) is strictly required to stabilize performance.

### Independently reproduced

Not independently reproduced. All empirical findings reflect direct extraction from Peng, Khushi & Poon (`arXiv:2609.14205v1`, September 13, 2026) and code inspection of `FanBroWell/CAST` (commit `8ae60cf28aebd93e6499312bdbf93ad839890756`).

### Negative evidence

- **Frictionless Backtest Distortion:** The reported results assume zero commission, zero exchange fees, zero borrow fees, and zero market impact. Given daily portfolio rebalancing across 30 assets, trading costs would substantially reduce the net Sharpe ratio.
- **TPX100 Cross-Asset Underperformance:** On the TPX100 panel under fixed $\lambda$, single-asset CKF (without cross-asset coupling) outperformed CAST (Sharpe 0.384 vs 0.228). This indicates that when correlation estimates from a historical window diverge from live regimes, cross-asset coupling in $\widetilde{Q}$ can transmit noise rather than signal.
- **Low Absolute Return / Modest Sharpe:** Annualized Sharpe ratios under fixed $\lambda$ range from 0.23 to 0.52. While drawdowns are exceptionally low (3%–16%), the strategy functions as a capital-preservation / defensive overlay rather than a high-return alpha generator.
- **Survivorship and Continuity Bias:** Universe selection required unbroken 20-year trading histories. Companies that underwent bankruptcy, merger, or extended suspension were excluded, introducing potential survivorship bias.

## Falsification plan

1. **Transaction Cost and Slippage Friction Test:**
   - Implement realistic trading costs: 5 bps maker/taker commission plus 5 bps slippage per side `[research-proposed]`.
   - *Falsification Criterion:* If net annualized Sharpe falls below 0.0 or net return falls below the risk-free rate on NASDAQ or CSI300, the tradable viability of the alpha is falsified `[research-defined falsification threshold]`.
2. **Shuffled Cross-Asset Correlation Placebo:**
   - Randomly permute the off-diagonal correlation matrix $\boldsymbol{\rho}$ while preserving diagonal unit variances and single-asset noise calibrations.
   - *Falsification Criterion:* If the permuted placebo model matches or exceeds the calibrated CAST model on out-of-sample Sharpe and Calmar ratio across 3 of 4 markets, the hypothesized cross-asset state coupling mechanism is falsified `[research-defined falsification threshold]`.
3. **Rolling Correlation Walk-Forward Stability Test:**
   - Replace the frozen 2005–2009 correlation matrix with rolling 252-day or 504-day correlation windows.
   - *Falsification Criterion:* If rolling dynamic correlations degrade Sharpe by more than 35% or increase MaxDD by more than 50% relative to the frozen baseline, the stability of the state-space covariance prior is falsified `[research-defined falsification threshold]`.
4. **Execution Timing and Fill Model Perturbation:**
   - Shift execution from day $k+1$ close to day $k+1$ open or TWAP.
   - *Falsification Criterion:* If changing fill timing reduces Sharpe by greater than 40%, the strategy relies on unrealistic close-to-close fill synchrony `[research-defined falsification threshold]`.
5. **Ablation of Dynamic Credibility Weights:**
   - Fix model order weights $\mu^{(r)} = [1/3, 1/3, 1/3]$ static throughout the 15-year test.
   - *Falsification Criterion:* If static equal weighting matches the adaptive credibility weighting within 0.05 Sharpe, the online credibility adaptation mechanism provides no significant advantage `[research-defined falsification threshold]`.

## Crypto portability

**adapted** / **unproven**

The primary paper evaluated equity indices only (NASDAQ, CSI300, TPX100, Global30). Application to crypto markets represents a research-proposed adaptation and remains unproven:

- **Structural Alignment with Crypto Perpetuals:**
  - Major crypto perpetual markets (Binance, Bybit, OKX, Hyperliquid) feature baskets of 30+ liquid tokens with high cross-asset correlation ($\bar{\rho} \approx 0.60 - 0.85$), which theoretically strengthens the cross-asset coupling mechanism in $\widetilde{Q}$.
  - Daily closes can be adapted to 8-hour funding epochs or 1-hour / 4-hour bar intervals `[research-proposed]`.
  - 24/7 continuous trading eliminates the weekend and overnight session gap risks that affect traditional equity implementations.
- **Portability Risks and Gaps:**
  - **Funding Rate Friction:** Holding perpetual contracts incurs 8-hour funding fees. In strong bull or bear regimes, cumulative funding drag can exceed 20–50% APR, violating the paper's zero-holding-cost assumption `[research-proposed]`.
  - **Fat-Tailed Jump Dynamics:** Crypto returns exhibit extreme kurtosis, volatility clustering, and liquidation cascades that violate the Gaussian process noise assumption $\mathbf{v}_k \sim \mathcal{N}(\mathbf{0}, \widetilde{Q})$ underlying linear Kalman filters.
  - **Asymmetric Shorting Costs:** Borrow rates for spot tokens or negative funding on perpetuals make short holding costly, unlike the frictionless shorting modeled in the equity backtest.
  - **Exchange and Counterparty Risk:** The 15-year equity hold assumption ignores crypto venue insolvencies, contract de-listings, and API liquidation latency.

## Limitations

- **Frictionless Execution:** Zero fees, zero slippage, and zero impact in primary reported benchmarks.
- **Survivorship Screen:** 20-year continuous trading requirement excludes delisted or defaulted names.
- **Single Calibration Period:** Noise parameters and correlations were calibrated once on 2005–2009 data and frozen for 15 years; live performance under completely unprecedented macro regimes is unverified.
- **Unconstrained Shorting:** The backtest permits unconstrained short selling without borrowing costs or borrow limits.
- **Scalability Bottleneck:** $\mathcal{O}(M^2)$ parameters in the cross-asset correlation matrix limits universe size to $M \approx 30 - 50$ assets without hierarchical tiering.
- **Modest Sharpe Ratio:** Maximum annualized Sharpe is 0.52 (fixed) / 0.72 (adaptive), reflecting a defensive, capital-preservation profile rather than a high-octane alpha generator.
- **Not Independently Reproduced:** All evidence derives from author-reported paper and repository results.

## Implementation status

`not-implemented`. No implementation in our production or validation research stack (PyBroker, NautilusTrader, paper trading, or live execution) has been completed.

## Adoption boundary

- Status: `research-only`
- Adoption: `not-approved`
- Approval Scope: `research-only`
- This record captures external academic and open-source quantitative research. Its presence in this repository does not indicate commercial profitability, validated alpha, or permission to deploy in paper trading, testnet, or live trading environments.

## Related Wiki records

- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]` — Forensic analysis of Kalman filter hedge ratio drift and cointegration breakdown in equities.
- `[[quant/tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12]]` — Kalman filter state-space application to crypto stablecoin pairs.
- `[[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]` — Deep selective state spaces (Mamba/S4) for cross-sectional ranking.
- `[[quant/two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]]` — Uncertainty estimation and tail-risk gating in cross-sectional rankers.

## Sources

1. Yu Peng, Matloob Khushi, and Josiah Poon, *"CAST: A Cross-Asset State-Space Trading System for Drawdown Control in Stock Markets"*, arXiv preprint `arXiv:2609.14205v1 [cs.AI, q-fin.TR]`, submitted September 13, 2026.
   - Abstract URL: https://arxiv.org/abs/2609.14205
   - Full-Text HTML: https://arxiv.org/html/2609.14205v1
   - Full-Text PDF: https://arxiv.org/pdf/2609.14205v1
   - Canonical DOI: https://doi.org/10.48550/arXiv.2609.14205

2. Yu Peng, Matloob Khushi, and Josiah Poon, *CAST: Code and data for reproducing the main results of CAST*, GitHub repository, commit `8ae60cf28aebd93e6499312bdbf93ad839890756`, September 2026.
   - Repository URL: https://github.com/FanBroWell/CAST
   - Source Code Paths:
     - `src/filter/cokf.py` (CrossAssetCollaborativeKF and JointKF implementation)
     - `src/filter/single_ckf.py` (CollaborativeKF and IRW state space setup)
     - `src/mpc.py` (PaperMPC linear program and uncertainty penalty)
     - `src/backtest.py` (30 independent accounts loop, no-leverage clip, margin floor)
     - `APPENDIX.md` (universe definitions, parameter registry, and ablation results)
