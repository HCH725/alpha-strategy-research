---
schema: strategy-research-record-v1
title: "S&P 500 Sector Statistical Arbitrage: Causal Two-Stage Residualization, PCA Second-Eigenvector Hedge Ratios, EWM Area Asymmetry Quality Filter, and Empirical Falsification"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - causal-residuals
  - fama-french
  - sp500
  - pca-hedge-ratio
  - mean-reversion
  - area-asymmetry
  - negative-result
  - falsification
  - ibkr-commission-model
  - borrow-costs
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "GitHub repository: alphachain-trading/statarb_sim (commit d09d911098aecd41b6fe5d5d3e52fd12fe4abbef, author Nikolaj Nock, published/updated September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# S&P 500 Sector Statistical Arbitrage: Causal Two-Stage Residualization, PCA Second-Eigenvector Hedge Ratios, EWM Area Asymmetry Quality Filter, and Empirical Falsification

## Provenance

- **Primary Source**: `alphachain-trading/statarb_sim`, *"Systematic statistical arbitrage (pairs, sparse+dense portfolio spreads) trading research platform for S&P 500 equities"*, public quantitative research platform authored by Nikolaj Nock (`source-reported`).
- **Repository URL**: `https://github.com/alphachain-trading/statarb_sim`
- **Full Commit SHA**: `d09d911098aecd41b6fe5d5d3e52fd12fe4abbef` (audited at tree root as of 2026-09-11)
- **Author**: Nikolaj Nock (`alphachain-trading`)
- **Publication / Last Commit Date**: September 11, 2026
- **License**: MIT License
- **Audited Primary Code & Specification Paths**:
  - `README.md`: System overview, empirical findings across 10 S&P 500 sectors (profit factors 1.0–2.1, win rates 55–73%), validated statistical findings (`x_area_asymmetry_ewm` z-separation 1.83, hl252/hl378 vs hl63 timescale performance, risk-free rate adjustment), and documented negative results (`source-reported`).
  - `src/residuals/causal_residuals.py`: Causal two-stage OLS residualization removing broad market (SPY) and sector proxy ETF factor exposures, supporting `EQ_ROLLING`, `EQ_EXPANDING`, and `DECAY_EXPANDING` modes, optional residual PC removal, and explicit risk-free rate yield subtraction (`source-reported`).
  - `src/residuals/spreads.py`: OLS without intercept (`ols_beta_no_intercept`), PCA 2nd eigenvector spread weights, canonical spread identification, and relative weight transformations (`source-reported`).
  - `src/candidates/pair_candidate_panel_creator.py`: Pair candidate generation across sector constituents, `_pca_spread_weights` normalization, pairwise NaN dropping, mandatory `min_obs` filter, and Ornstein-Uhlenbeck discrete mean-reversion parameter estimation ($\kappa$, half-life, $MR$ score) (`source-reported`).
  - `src/analytics/spread_primitives.py`: Analytical primitives including `compute_x_area_asymmetry_ewm` (EWM-weighted signed area asymmetry above vs below local mean), `compute_bw_gain_stats`, `compute_mean_ewm_pct`, and `compute_delta_z_ewm` (`source-reported`).
  - `src/simulator/traders/pair_spread_mean_reversion.py`: Multi-position mean-reversion trading engine, evaluating z-threshold entry (`entry_z = 1.75`), z-cross exit (`exit_z = 0.0`), and time-stop exits (`source-reported`).
  - `src/simulator/execution.py`: Execution engine implementing interactive Brokers (IBKR) Pro Fixed commission model, per-share fees, order caps, and integer share rounding (`source-reported`).
  - `src/simulator/config.py`: Strictly typed configuration dataclasses for Data, Activation, Capital, RiskManager, Sizing, and Execution (`source-reported`).
  - `src/simulator/sweep_defaults.py`: `standard_v1` default bundle pinning $1,000,000 total capital, 10.0x maximum gross exposure, 15% maximum single-ticker net exposure, IBKR commission schedule ($0.005/share, $1.00 min, $9.79 max, 1.0% cap), and 30 bps annual short borrow cost (`source-reported`).
  - `scripts/b_baseline_harness.py`: Frozen experiment driver and baseline test script for Energy and Materials sectors (`source-reported`).
  - `docs/refactor/B_baseline.txt`: PnL and trade log of baseline run (97 trades, Net Sharpe 1.372, Win Rate 68.0%, Profit Factor 2.283, Max Drawdown -8.85%, 2006-09 to 2007-06) (`source-reported`).
  - `docs/refactor/G_hedge_mode.md`: Econometric derivation of decay-expanding vs rolling hedge ratios, matched effective sample size ($hl^* = lb / 2.885$), window-exit discontinuity, and Kalman filter rejection rationale (`source-reported`).
  - `docs/research/z_spectra_sample_note.md`: Null result documentation on multi-lookback z-score spectrum entry confirmation (`source-reported`).

## Economic mechanism

### Source-reported

1. **Idiosyncratic Residual Divergence**: The underlying premise posits that equity pair trading directly on raw price series conflates market-wide macro factors and sector-wide shocks with true idiosyncratic divergence. By applying a causal two-stage Ordinary Least Squares (OLS) residualization—first regressing the sector proxy ETF against the broad market index (SPY), then regressing each constituent stock against both the market index and the orthogonalized sector residual—the resulting series captures pure idiosyncratic firm-level pricing deviations (`source-reported`).
2. **Minimum-Variance Divergence via Principal Component Analysis (PCA)**: When constructing a stationary spread between two residualized assets, simple OLS regression ($y = \beta x + \epsilon$) introduces directional asymmetry and errors-in-variables bias. Utilizing the second principal component (PC2) of the two-asset residual return covariance matrix treats both assets symmetrically, identifying the orthogonal divergence axis and generating optimal hedge ratios ($w_{\text{left}} = 1.0, w_{\text{right}} < 0$) (`source-reported`).
3. **Mean-Reversion Velocity and Spread Diagnostics**: Dislocated residual spreads are evaluated under a discrete Ornstein-Uhlenbeck (OU) mean-reversion process ($\Delta X_t = -\kappa (X_{t-1} - \mu) \Delta t + \sigma_{\epsilon} \epsilon_t$). Spreads exhibiting sufficient mean-reversion velocity ($\kappa \ge 1\times 10^{-6}$) and bounded half-lives ($t_{1/2} = \ln(2)/\kappa \le 126$ days) indicate persistent structural stationary relationships suitable for contrarian exploitation (`source-reported`).
4. **Asymmetric Dislocation Memory via Area Asymmetry**: Standard z-scores measure only the instantaneous snapshot distance from the mean. The `x_area_asymmetry_ewm` primitive measures whether the spread has spent disproportionate recent time on one side of its exponential moving average (EMA). Spreads that have drifted persistently into one-sided dislocation reflect potential structural breaks, whereas fresh or symmetric excursions offer higher probability of rapid reversion (`source-reported`).

### Research interpretation

This repository represents an institutional-grade, causal statistical arbitrage framework addressing critical econometric failure modes common to retail pairs trading:
1. **Resolution of Common-Factor Contamination**: Un-residualized pairs trading frequently confuses sector rotation or interest-rate beta with asset mispricing. In a rate-hiking or trending macro regime, two stocks with unequal market betas will exhibit non-stationary price divergence that never mean-reverts. Causal two-stage residualization with risk-free rate adjustment eliminates systematic beta drift prior to spread formation.
2. **Total Least Squares vs OLS Asymmetry**: In standard pairs trading, assigning Stock A as the regressand and Stock B as the regressor yields $\beta_{A|B} \neq 1 / \beta_{B|A}$. The PCA PC2 eigenvector approach corresponds to Orthogonal Distance Regression (Total Least Squares), which minimizes Euclidean perpendicular distances to the spread line rather than vertical residuals, eliminating arbitrary leg designation and errors-in-variables attenuation.
3. **Rigorous Methodological Falsification and Negative Results**:
   - **Kalman Filter Rejection**: The author explicitly rejects time-varying Kalman filter state-space models for hedge ratios: Kalman estimation introduces two unidentifiable noise covariance hyperparameters, time-varying observation variance re-introduces an arbitrary rolling window, and under constant-gain steady state, the Kalman filter mathematically collapses to an Exponential Weighted Moving Average (EWM).
   - **Multi-Timescale and Blended Z-Scores**: Testing across multi-lookback z-score spectrum grids showed that cross-timescale signal gates and blended entry modes provided zero incremental alpha and added unnecessary model degrees of freedom.
   - **No Momentum in Mean-Reversion Quality**: The author proves that historical backward-window gain does not predict forward-window realization, demonstrating that selecting pairs based on trailing backtest PnL is data-snooping noise.
   - **Sizing Multiplier Degradation**: Scaling position sizes by nonlinear entry feature multipliers consistently degraded out-of-sample Sharpe ratios due to increased leverage variance.

## Signal

### Signal Architecture

The trading signal operates as an event-driven, daily-close mean-reversion strategy evaluated across pre-filtered, weekly-updated candidate pair panels.

### 1. Causal Two-Stage Residualization

- **Observation Frequency**: Daily close log returns aligned across sector constituents, sector proxy ETF, and SPY (`source-reported`).
- **Risk-Free Rate Adjustment**: Annualized 3-month Treasury yield $r_{f,\text{ann}}$ converted to daily log return $r_{f,t} = \ln(1 + r_{f,\text{ann}}/100) / 252$ and subtracted from all asset returns (`source-reported`).
- **Stage 1 (Sector Proxy vs Benchmark)**:
  $$R_{\text{proxy}, t} - r_{f,t} = \alpha_{\text{proxy}} + \beta_{\text{bench}} (R_{\text{SPY}, t} - r_{f,t}) + \epsilon_{\text{proxy}, t}$$
  Estimated via OLS over expanding window (`min_lb_eq_exp = 20` days) or decay-expanding window (`hl = 504` days, `min_history = 1008` days) (`source-reported`).
- **Stage 2 (Constituent Stocks vs Benchmark + Sector Residual)**:
  $$R_{i, t} - r_{f,t} = \alpha_i + \beta_{i, \text{bench}} (R_{\text{SPY}, t} - r_{f,t}) + \beta_{i, \text{proxy}} \hat{\epsilon}_{\text{proxy}, t} + \epsilon_{i, t}$$
  Estimated for each constituent stock $i$ (`source-reported`).
- **Optional PC Projection**: Projecting out top $K$ principal components ($K=0$ in baseline, $K \ge 1$ optional) from the residual covariance matrix (`source-reported`).
- **Cumulative Residual Level**: Cumulative sum of residual returns $S_{i, t} = \sum_{\tau=1}^t \hat{\epsilon}_{i, \tau}$ (`source-reported`).

### 2. Candidate Pair Selection and PCA Hedge Ratio

- **Reconstitution Cadence**: Weekly on Friday closes (`frequency = "W-FRI"`) (`source-reported`).
- **Pair Universe**: All 2-ticker combinations within each sector ($N(N-1)/2$ pairs) (`source-reported`).
- **Pairwise Missing-Data Gate**: Pairwise NaN dropping; pairs retaining fewer than `min_obs` valid overlapping daily observations are rejected (`min_obs = 252` in baseline harness) (`source-reported`).
- **PCA Hedge Ratio Estimation (`_pca_spread_weights`)**:
  - Trailing lookback window: `hedge_ratio_lb = 252` trading days (`source-reported`).
  - Calculate covariance matrix of 2-asset residual returns $X = [\hat{\epsilon}_{\text{left}}, \hat{\epsilon}_{\text{right}}]$ (`source-reported`).
  - Compute eigenvalues and eigenvectors via `np.linalg.eigh` (`source-reported`).
  - Extract PC2 (eigenvector corresponding to smaller eigenvalue $\lambda_0$) (`source-reported`).
  - Normalize so left ticker has weight $w_{\text{left}} = 1.0$; enforce negative sign for right ticker $w_{\text{right}} = -\beta_{\text{pca}} < 0$ (`source-reported`).
- **Discrete Ornstein-Uhlenbeck Screening**:
  - Spread return: $R_{\text{spread}, t} = w_{\text{left}} \hat{\epsilon}_{\text{left}, t} + w_{\text{right}} \hat{\epsilon}_{\text{right}, t}$ (`source-reported`).
  - Spread level: $X_t = \sum_{\tau=1}^t R_{\text{spread}, \tau}$ over `mr_diag_lb = 252` days (`source-reported`).
  - Discrete OU fit: $\Delta X_t = \alpha + \beta X_{t-1} + u_t$, where $\kappa = -\beta$ (`source-reported`).
  - Half-life: $t_{1/2} = \ln(2)/\kappa$ (`source-reported`).
  - Hard admissibility gates:
    - $\text{spread\_return\_std} \ge 1\times 10^{-8}$ (`source-reported`).
    - $\text{level\_std} \ge 1\times 10^{-8}$ (`source-reported`).
    - $\kappa \ge 1\times 10^{-6}$ (`min_kappa`) (`source-reported`).
    - $0 < t_{1/2} \le 126.0$ trading days (`max_half_life`) (`source-reported`).
    - Residual standard deviation $\sigma_u > 0$ (`source-reported`).

### 3. Entry and Exit Logic

- **Spread Z-Score Formation**:
  - Exponential weighted moving average (EWM) with lookback $\tau = 21$ days (`lookback = 21`, `ddof = 1`) (`source-reported`):
    $$\alpha_{\text{ewm}} = 1 - \exp(-1 / \tau)$$
    $$\mu_t = \text{EWM}_{\alpha}(X_t), \quad \sigma_t = \sqrt{\text{EWMVar}_{\alpha}(X_t)}$$
    $$z_t = \frac{X_t - \mu_t}{\sigma_t}$$
- **Long Spread Entry Trigger**:
  - Condition: $z_t \le -\text{entry\_z}$ (where `entry_z = 1.75` in baseline harness, `2.0` in general configuration) (`source-reported`).
  - Action: Buy left ticker with weight $+1.0$, short right ticker with weight $-\beta_{\text{pca}}$ (`source-reported`).
- **Short Spread Entry Trigger**:
  - Condition: $z_t \ge \text{entry\_z}$ (`source-reported`).
  - Action: Short left ticker with weight $-1.0$, buy right ticker with weight $+\beta_{\text{pca}}$ (`source-reported`).
- **Optional Entry Quality Gate (`x_area_asymmetry_ewm`)**:
  - Measures recent dislocation persistence:
    $$\text{disloc}(t) = X_t - \mu_t$$
    $$\text{above}(t) = \max(\text{disloc}(t), 0), \quad \text{below}(t) = |\min(\text{disloc}(t), 0)|$$
    $$\text{asymmetry} = \frac{\text{EWM}(\text{above})_t - \text{EWM}(\text{below})_t}{\text{EWM}(\text{above})_t + \text{EWM}(\text{below})_t} \in (-1, 1)$$
  - Directionally corrected by $\text{sign}(z_t)$. Validated entry gate requires signed area asymmetry $\ge -0.20$ to reject stale exhausted dislocations (`source-reported` / `research-proposed`).
- **Exit Triggers (First Condition Met)**:
  1. **Mean-Reversion Z-Cross**:
     - Long position ($direction > 0$): exit when $z_t \ge -\text{exit\_z}$ (where `exit_z = 0.0`) (`source-reported`).
     - Short position ($direction < 0$): exit when $z_t \le \text{exit\_z}$ (where `exit_z = 0.0`) (`source-reported`).
  2. **Time Stop**:
     - Days open exceeds maximum holding horizon: $\text{days\_open} \ge \text{max\_holding\_days}$ (where `max_holding_days = 40` days in baseline harness) (`source-reported`).
  3. **PnL Stop**:
     - Optional unrealized loss stop: $\text{pnl\_pct} \le -\text{pnl\_stop\_fraction}$ (`research-proposed`).

### 4. Position Sizing and Portfolio Risk Constraints

- **Base Sizing**: Base notional $N_{\text{base}} = \$100,000$ per pair trade (`source-reported`).
- **Volatility Normalization**: Each pair's notional is scaled by inverse trailing spread volatility relative to the cross-sectional median:
  $$\text{Multiplier} = \text{clip}\left(\frac{\text{median}(\sigma_{\text{spread}})}{\sigma_{\text{pair}}}, \text{floor} = 0.2, \text{cap} = 5.0\right) \quad (\text{source-reported})$$
- **Portfolio Risk Caps**:
  - Total portfolio capital reference: $C = \$1,000,000$ (`source-reported`).
  - Max Gross Exposure: $\sum |\text{Notional}_i| \le 10.0 \times C = \$10,000,000$ (`source-reported`).
  - Max Single-Ticker Net Exposure: $|\text{Net Notional}_{\text{ticker}}| \le 0.15 \times C = \$150,000$ (`source-reported`).
  - Concurrency: Uncapped or constrained by risk manager gross limits (`source-reported`).

## Required data

- **Universe**: S&P 500 equity constituents partitioned into 10 GICS sector groups (`consumer_discretionary`, `consumer_staples`, `energy`, `financials`, `health_care`, `industrials`, `information_technology`, `materials`, `real_estate`, `utilities`) (`source-reported`).
- **Benchmark & Sector Proxies**:
  - Market benchmark: SPY ETF (`source-reported`).
  - Sector ETF proxies: XLE (Energy), XLB (Materials), XLK (Tech), XLF (Financials), XLI (Industrials), XLP (Staples), XLY (Discretionary), XLV (Healthcare), XLU (Utilities), XLRE (Real Estate) (`source-reported`).
- **Risk-Free Rate**: Annualized 3-month US Treasury bill rate yield series (`source-reported`).
- **Data Vendor & Asset Type**: US cash equities, daily OHLCV from yfinance/Polygon, with split/dividend adjustment (`source-reported`).
- **Timeframe & Bar Alignment**: Daily closing prices; weekly ranking evaluations on Friday market close (`W-FRI`), trade action generation for Monday market open (`source-reported`).
- **Point-in-Time Availability**: Strictly causal; residual models and PCA hedge ratios fit strictly up to as-of date $t$; zero forward-looking data leakage (`source-reported`).
- **Missing Data Handling**:
  - Tickers with missing data at fit date dropped from candidate universe (`source-reported`).
  - Pairwise dropna for candidate estimation; no forward-filling of missing prices allowed to prevent artificial zero returns and inflated $\kappa$ (`source-reported`).
  - Minimum valid observation count: `min_obs = 252` (`source-reported`).

## Execution assumptions

- **Order Type & Timing**: Market orders simulated at daily closing price on signal date or next-day market open (`source-reported`).
- **Transaction Cost Model (IBKR Pro Fixed Schedule)**:
  - Commission per share: $\$0.005$ (`source-reported`).
  - Commission per order base: $\$0.0$ (`source-reported`).
  - Minimum commission per order: $\$1.00$ (`source-reported`).
  - Maximum commission per order: $\$9.79$ (`source-reported`).
  - Percentage commission cap: $1.0\%$ of traded notional (`source-reported`).
- **Short Borrow Cost**:
  - Annual borrow rate: $30.0$ basis points per annum (`short_borrow_rate_annual_bps = 30.0`), accrued daily on short leg notional (`source-reported`).
- **Share Rounding**: Nearest integer share (`share_rounding = "nearest"`), minimum trade unit 0.5 shares (`source-reported`).
- **Slippage & Market Impact**:
  - Baseline simulation assumes $0.0$ bps slippage (`source-reported`).
  - Institutional execution requires modeling 2.0 to 5.0 bps execution slippage per leg (`research-proposed`).
- **Margin & Leverage**: Up to 10.0x gross leverage across market-neutral long/short pairs supported by Regulation T / Portfolio Margin (`source-reported`).

## Evidence

### Source-reported

1. **Sector-Wide Multi-Year Performance**:
   - Across 10 S&P 500 sectors, systematic stat-arb generates profit factors ranging from 1.0 to 2.1 depending on the sector, with win rates between 55% and 73% (`source-reported` in README).
   - Edge is concentrated in mean-reversion of causal residual spreads rather than raw price spreads (`source-reported` in README).
2. **Track B Baseline Performance Run (Energy + Materials Sectors)**:
   - Evaluated over 2006-09-08 to 2007-06-08 (187 trading days, 97 closed trades) (`docs/refactor/B_baseline.txt`):
     - Total Net Return: 19.61% (Gross: 20.26%) (`source-reported`).
     - Annualized Net Return: 27.29% (Gross: 28.22%) (`source-reported`).
     - Net Sharpe Ratio: 1.372 (Gross: 1.371) (`source-reported`).
     - Net Sortino Ratio: 1.323 (`source-reported`).
     - Net Calmar Ratio: 3.082 (`source-reported`).
     - Maximum Drawdown (Net): -8.85% (Gross: -8.75%) (`source-reported`).
     - Total Closed Trades: 97 trades across 2 sectors (`source-reported`).
     - Win Rate (Net): 68.0% (Gross: 68.0%) (`source-reported`).
     - Loss Rate (Net): 32.0% (`source-reported`).
     - Profit Factor (Net): 2.283 (`source-reported`).
     - Mean Gain per Win: $\$6,891.52$ net ($\$6,943.90$ gross) (`source-reported`).
     - Mean Loss per Loss: $-\$6,426.74$ net ($-\$6,372.38$ gross) (`source-reported`).
     - Average Holding Period: 38.9 trading days (Winning trades: 33.4 days; Losing trades: 50.5 days) (`source-reported`).
     - Average Absolute Entry Z-Score: 2.009; Average Exit Z-Score: -0.005 (`source-reported`).
     - Gross Realized PnL: $\$260,753.86$; Net Realized PnL: $\$255,611.04$ (`source-reported`).
     - Total Transaction Costs: $\$2,272.86$; Total Borrow Costs: $\$2,869.96$; Total Frictional Drag: $\$5,142.82$ (66.4 bps cost drag, $\$53.02$ average cost per trade) (`source-reported`).
3. **Validated Parameter Findings**:
   - `x_area_asymmetry_ewm` achieves statistically significant entry separation with a z-separation statistic of $1.83$, verified as half-split stable across sample partitions (`source-reported` in README).
   - Longer residual timescales (`hl252` and `hl378`) structurally outperform short residual timescales (`hl63`), yielding win rates of 62–72% compared to 54–57% (`source-reported` in README).
   - Inclusion of the risk-free rate in OLS residualization is materially significant in trending rate environments (`source-reported` in README).

### Independently reproduced

Not independently reproduced.

### Negative evidence

The primary source explicitly catalogs and documents five methodological negative results and failure modes:
1. **Multi-Timescale Z-Score Spectrum Null Result**: In `docs/research/z_spectra_sample_note.md`, testing whether z-scores computed across a geometric grid of 35 lookback combinations (5 to 252 days) provide early warning or confirmation filters returned a confirmed null result (`source-reported`).
2. **Blended Z-Score Failure**: Combining or averaging z-scores across multiple lookback windows showed zero performance improvement over a single well-specified EWM lookback (`source-reported` in README).
3. **Cross-Timescale Signal Gates**: Filtering trades via cross-timescale residual agreement was neutral to harmful to realized Sharpe ratios (`source-reported` in README).
4. **Failure of Trailing Performance Predictability**: Backward-window historical gain does not predict forward-window realization when used as an entry criterion, indicating that selecting pairs based on past backtest performance introduces post-selection degradation (`source-reported` in README).
5. **Feature-Weighted Sizing Multiplier Degradation**: Scaling position sizes proportionally to entry feature scores degraded portfolio Sharpe ratios at every tested multiplier due to compounding sizing volatility (`source-reported` in README).
6. **Window-Exit Discontinuity in Rolling Hedge Ratios**: Rolling OLS/PCA hedge ratios experience non-market beta shocks when extreme historical returns drop out of the trailing 252-day window (`docs/refactor/G_hedge_mode.md`) (`source-reported`).
7. **Small-Sample Pairwise Bias**: Fitting hedge ratios on pairs with fewer than `min_obs` observations creates severe upward bias in estimated mean-reversion speed $\kappa$, generating phantom candidates that immediately fail out-of-sample (`source-reported`).

## Falsification plan

To falsify or establish rigorous operational bounds for the S&P 500 causal residual stat-arb mechanism, the following pre-declared experiments must be executed:

1. **Two-Stage Residualization vs 1-Factor vs Raw Price Ablation**:
   - *Test*: Compare three parallel pipelines on identical S&P 500 sector universes across 2010–2025: (a) Two-stage market + sector residualization, (b) One-factor CAPM residualization (SPY only), and (c) Raw unadjusted price spread.
   - *Failure Rule*: If two-stage residualization does not achieve a statistically significant improvement in net Sharpe ratio ($t_{\text{stat}} \ge 2.0$) over 1-factor residualization after accounting for multiple testing, reject the sector-proxy orthogonalization hypothesis (`research-defined falsification threshold`).
2. **PCA Second-Eigenvector vs OLS Hedge Ratio Test**:
   - *Test*: Compare PC2 orthogonal distance hedge ratios against standard OLS regression ($y \sim x$ and $x \sim y$) under identical z-score entry thresholds.
   - *Failure Rule*: If PCA hedge ratios fail to reduce spread return variance by at least 10% or fail to increase mean-reversion parameter $\kappa$ relative to OLS, reject the PC2 geometric optimality hypothesis (`research-defined falsification threshold`).
3. **Area Asymmetry Entry Gate Out-of-Sample Verification**:
   - *Test*: Apply the `x_area_asymmetry_ewm` directional filter on out-of-sample data (2018–2026).
   - *Failure Rule*: If filtering by area asymmetry fails to improve win rate by $\ge 3.0\%$ or reduces total net profit factor below 1.20, reject the area asymmetry filter as an overfitted sample artifact (`research-defined falsification threshold`).
4. **Transaction Cost and Borrow Rate Stress Test**:
   - *Test*: Stress execution parameters: scale commissions to $\$0.01$/share, apply 5.0 bps execution slippage per leg, and scale annual short borrow costs from 30 bps to 150 bps (reflecting real-world hard-to-borrow fees).
   - *Failure Rule*: If the net Sharpe ratio drops below 0.50 or net profit factor falls below 1.10 under 5 bps slippage and 100 bps borrow cost, classify the strategy as non-viable in live institutional execution (`research-defined falsification threshold`).
5. **Crisis Regime Stress (2008 GFC, March 2020 COVID, 2022 Inflation/Rate Hike)**:
   - *Test*: Evaluate maximum drawdown and daily PnL during high-volatility liquidity contraction windows.
   - *Failure Rule*: If maximum portfolio drawdown exceeds -25.0% or pairs experience simultaneous cointegration breakdown ($\Delta z > 4.0$ without reversion within 60 days), reject the structural stability thesis (`research-defined falsification threshold`).

## Crypto portability

- **Portability Status**: `unproven`
- **Asset-Class Differences**:
  - The strategy relies strictly on single-stock equities partitioned into formal GICS industry sectors with liquid benchmark ETFs (SPY, XLB, XLE, XLK, etc.) and stable regulatory balance sheets.
  - In cryptocurrency markets, formal corporate sectors do not exist; crypto "narratives" or "sectors" (DeFi, Layer 1, AI, Meme coins) exhibit non-stationary, shifting memberships without standardized capitalization-weighted ETF baskets (`research interpretation`).
  - Cross-sectional correlation among crypto assets is exceptionally high ($\bar{\rho} > 0.75$), dominated by Bitcoin (BTC) as the primary market factor ($> 70\%$ variance explained) (`research interpretation`).
  - Equity shorting incurs stock loan borrow fees (30 bps base); crypto perpetual futures incur continuous 8-hour funding rates. In trending or asymmetric crypto regimes, funding rate divergence between two perpetuals can easily exceed 20–50% annualized, completely overwhelming mean-reversion spread gains (`research interpretation`).
  - Equity markets operate under defined daily trading sessions (9:30 to 16:00 EST) with overnight gaps; crypto markets operate 24/7/365 with continuous liquidation cascading and venue-specific order book fragmentation (`research interpretation`).
- **Required Adaptation if Attempted**:
  - Replace SPY with BTCUSDT perpetual as the broad market factor (`research-proposed`).
  - Replace sector ETFs with synthetically constructed, market-cap-weighted crypto category baskets (`research-proposed`).
  - Integrate real-time 8-hour funding rate carry into the residual spread pricing model, subtracting net funding carry from the expected mean-reversion drift (`research-proposed`).
  - Enforce strict perpetual liquidation buffer stops rather than unconstrained 40-day time stops (`research-proposed`).

## Limitations

- **Underspecified Execution Slippage**: The baseline backtest reports 0 bps slippage, assuming full fills at closing prices. In physical equities, simultaneous multi-stock rebalancing at market close incurs bid-ask spread crossing and market impact (`source gap`).
- **Unrealistic Constant Borrow Cost**: Assuming a flat 30 bps annual borrow fee across all S&P 500 constituents ignores that dislocated, distressed stocks frequently become hard-to-borrow (HTB), with borrow fees surging past 10–50% per annum or locates becoming unavailable (`source gap`).
- **Survivorship and Corporate Action Bias**: The repository downloads current S&P 500 sector constituent lists via yfinance, creating survivorship bias by omitting companies that were delisted, acquired, or went bankrupt between 2006 and 2026 (`source gap`).
- **Limited Sample in Committed Baseline**: The verified baseline harness covers 187 trading days (2006–2007), representing a benign pre-crisis equity regime; long-term multi-decade performance across GFC 2008 and COVID 2020 remains uncommitted in raw artifacts (`source gap`).

## Implementation status

- `not-implemented` in the target quant research stack (`nautilus-quant-system`).
- The strategy exists as an independent, open-source Python research framework (`alphachain-trading/statarb_sim`), but has not been translated into PyBroker or NautilusTrader execution models.
- No live, paper, or testnet trading has been executed or authorized.

## Adoption boundary

- **Status**: `research-only`
- **Adoption**: `not-approved`
- **Approval Scope**: `research-only`
- This document serves exclusively as an external quantitative research capture and falsification reference.
- Presence in this repository does not constitute evidence of live profitability, approval for capital allocation, or implementation authorization for paper trading, testnet execution, or live deployment.

## Related Wiki records

- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]`
- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]`
- `[[quant/statistical-arbitrage-methodology-degradation-ladder-falsification-2026-09-12]]`
- `[[quant/crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]`
- `[[quant/eurostoxx-pca-ou-stat-arb-trading-time-friction-falsification-2026-09-12]]`

## Sources

- **Primary Repository**: GitHub repository `alphachain-trading/statarb_sim`, commit `d09d911098aecd41b6fe5d5d3e52fd12fe4abbef`, author Nikolaj Nock, published September 2026: `https://github.com/alphachain-trading/statarb_sim`
- **Primary Code Modules**:
  - `src/residuals/causal_residuals.py`: Two-stage OLS residualization and risk-free yield adjustment.
  - `src/residuals/spreads.py`: PCA 2nd eigenvector spread weights and OLS without intercept.
  - `src/candidates/pair_candidate_panel_creator.py`: Candidate pair generation, `_pca_spread_weights`, pairwise dropna, `min_obs` gate, and discrete Ornstein-Uhlenbeck parameter estimation.
  - `src/analytics/spread_primitives.py`: `compute_x_area_asymmetry_ewm` EWM-weighted signed area asymmetry primitive.
  - `src/simulator/traders/pair_spread_mean_reversion.py`: Z-score threshold entry and z-cross exit logic.
  - `src/simulator/execution.py`: IBKR Pro Fixed commission model.
  - `src/simulator/sweep_defaults.py`: `standard_v1` default capital, risk manager, and borrow cost parameters.
  - `scripts/b_baseline_harness.py`: Experiment harness for Energy and Materials sectors.
  - `docs/refactor/B_baseline.txt`: Baseline empirical performance report (97 trades, Sharpe 1.372, win rate 68.0%, 2006-2007).
  - `docs/refactor/G_hedge_mode.md`: Theoretical derivation of decay-expanding vs rolling hedge ratios, window-exit discontinuity, and Kalman filter rejection.
  - `docs/research/z_spectra_sample_note.md`: Null result on multi-lookback z-score spectrum entry confirmation.
