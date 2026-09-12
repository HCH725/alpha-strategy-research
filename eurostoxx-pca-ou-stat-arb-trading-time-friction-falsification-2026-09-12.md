---
schema: strategy-research-record-v1
title: "Empirical Falsification of Avellaneda-Lee PCA Statistical Arbitrage on Euro Stoxx 50: Turnover Drag, Factor Overfitting, and Volume-Adjusted Trading Time Breakdown"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pca-factor-model
  - ornstein-uhlenbeck
  - s-score
  - euro-stoxx-50
  - trading-time-falsification
  - transaction-cost-attrition
  - factor-overfitting
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "https://github.com/SimoneCerrone/StatArb-EMU-Equities (commit e56c954f46111f116b3c6e6b988c6bce10e9b36c, 2026-09-11)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Empirical Falsification of Avellaneda-Lee PCA Statistical Arbitrage on Euro Stoxx 50: Turnover Drag, Factor Overfitting, and Volume-Adjusted Trading Time Breakdown

## Provenance

- **Authors:** Simone Cerrone (Matr. 303432), Filippo Tacconi (Matr. 314998), Vittoria Tomasini (Matr. 304183), Aloïs Maréchal (Matr. 294708) (Group 12, Mathematical Engineering – Financial Engineering, Politecnico di Milano, FY 2025–2026) (`source-reported`).
- **Repository:** `SimoneCerrone/StatArb-EMU-Equities`
- **Repository URL:** [https://github.com/SimoneCerrone/StatArb-EMU-Equities](https://github.com/SimoneCerrone/StatArb-EMU-Equities)
- **Canonical Immutable Commit SHA:** `e56c954f46111f116b3c6e6b988c6bce10e9b36c` (`source-reported`)
- **Commit Date:** September 11, 2026 (`source-reported`)
- **Key Primary Source Artifacts Examined Directly:**
  - Academic Paper / Report: `Assignement_4a__Group_12_RM.pdf` (17 April 2026) (`source-reported`)
  - Execution Notebook: `ex4a_notebook.ipynb` (`source-reported`)
  - Factor Modeling & Signal Generation: `utilities/statistical_arbitrage.py` (`source-reported`)
  - Backtesting & Frictional Accounting Engine: `utilities/backtest_2.py` (`source-reported`)
  - Principal Component Decomposition: `utilities/principal_component_analysis.py` (`source-reported`)
  - Covariance & Correlation Validation: `utilities/covariance_utilities.py` (`source-reported`)
  - Underlying Price Panel: `data/sx5e_underlyings.csv` (2,600 daily rows, 46 assets, 2013-01-02 to 2023-02-17) (`source-reported`)
  - Volume Panel: `data/volume.csv` (2,600 daily rows, 46 assets) (`source-reported`)
- **Sample Period:** January 2, 2013 to February 17, 2023 (10-year period; 252-day initial estimation window; out-of-sample rolling backtest covers 2,287 rebalance dates from December 24, 2013 to February 17, 2023) (`source-reported`).
- **Primary Source Integrity:** All quantitative figures, parameter bounds, threshold sensitivity tables, and empirical performance metrics below were extracted directly from the verified PDF report and raw notebook execution outputs at commit `e56c954f46111f116b3c6e6b988c6bce10e9b36c`. No secondary model summaries or web snippets were used.

## Economic mechanism

### Source-reported

The classical statistical arbitrage framework of Avellaneda and Lee (2008, 2010) decomposes cross-sectional stock returns into systematic risk factors (extracted via Principal Component Analysis on the asset correlation matrix) and idiosyncratic residual returns. The theoretical premise is:
1. **Idiosyncratic Mean Reversion:** Asset-specific residuals $X_{i,t} = \sum_{s=1}^t \epsilon_{i,s}$ reflect temporary supply/demand imbalances or non-fundamental price shocks that mean-revert to an equilibrium level $m_i$ following a continuous-time Ornstein-Uhlenbeck (O-U) process $dX_t = \kappa (m - X_t) dt + \sigma dW_t$.
2. **Trading Time Hypothesis:** Measuring returns in "trading time" (volume-adjusted returns $\bar{R}_{i,t} = R_{i,t} \cdot \frac{\langle V_i \rangle}{V_{i,t}}$) theoretically amplifies price moves occurring on low-volume days—which are presumed to reflect temporary liquidity dislocations ideal for mean-reversion—while dampening high-volume moves that reflect permanent fundamental news repricing.

The primary authors investigated this methodology on the Euro Stoxx 50 index (European Economic and Monetary Union blue-chips) and established three fundamental falsifications of the classical narrative:
1. **Turnover Execution Cost Attrition:** In a concentrated universe of large-cap blue-chips, idiosyncratic mispricings are narrow and short-lived. Capturing them requires high daily turnover (~19.3 active positions rebalanced daily), which incurs continuous transaction friction. A modest 5 bps one-way cost obliterates 86.3% of annual return (collapsing from 3.44% to 0.47%) and destroys the Sharpe ratio (from 0.61 to 0.08).
2. **Volume-Adjusted Trading Time Falsification:** In liquid European mega-caps, low-volume trading sessions are driven by institutional holidays or calendar news lulls rather than illiquid liquidity shocks. Amplifying low-volume returns artificially injects statistical noise into the O-U calibration, destabilizes parameter estimation, and turns net performance negative (Sharpe drops to -0.01 with costs).
3. **Factor Extraction Overfitting Dilemma:** Targeting excessive explained variance (e.g., $\tau = 75\%$, extracting ~12 principal components out of 46 assets) strips meaningful idiosyncratic alpha out of the residuals by fitting noise as "systematic factors", collapsing the Sharpe ratio to 0.22. Conversely, extracting too few factors ($\tau = 40\%$, ~1.4 factors) leaves systematic sector exposure in the residuals, producing deep drawdowns (-19.35%).

### Research interpretation

This study highlights the severe structural differences between broad-universe statistical arbitrage (e.g., US equities with 500–1,500 names across diverse capitalization tiers) and concentrated mega-cap universes (Euro Stoxx 50 with 46 eligible blue-chips). In a small, highly liquid universe:
- Idiosyncratic variance is heavily compressed because institutional coverage and index arbitrage rapidly extinguish pure mispricings.
- The Avellaneda-Lee "trading time" transformation is conceptually flawed when applied to large-caps: quiet trading days do not represent unabsorbed inventory dislocations; they represent lack of market participation. Scaling returns inversely with volume converts uninformative holiday drift into large synthetic outliers, corrupting the discrete AR(1) estimation of mean-reversion parameters.
- Statistical arbitrage without explicit turnover regularization (e.g., transaction-cost-aware optimization, minimum holding periods, or trade deadbands) cannot survive realistic European market friction even on institutional accounts.

## Signal

The strategy employs a rolling, daily re-estimated PCA factor model coupled with discrete Ornstein-Uhlenbeck parameter estimation and modified s-score thresholding.

### 1. Daily Rolling Factor Decomposition

- **Estimation Window:** Trailing $T = 252$ trading days (1 calendar year), rolling daily (`source-reported`).
- **Standardization:** Raw simple daily returns $R_{i,t}$ are standardized: $\tilde{R}_{i,t} = \frac{R_{i,t}}{\hat{\sigma}_i}$, where $\hat{\sigma}_i$ is the sample standard deviation over the 252-day window (`source-reported`).
- **Correlation Matrix:** Sample correlation matrix $C \in \mathbb{R}^{N \times N}$ ($N=46$ assets) (`source-reported`). (Note: the authors explicitly identified and corrected a code defect where sample covariance was called instead of correlation; correlation ensures scale invariance across assets) (`source-reported`).
- **Eigendecomposition:** $C = Q \Lambda Q^T$, where eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_N$ and corresponding eigenvectors $q_j$ (`source-reported`).
- **Factor Selection ($K$):**
  - Baseline: Fixed $K = 4$ principal components (`source-reported`).
  - Dynamic Explained Variance Variant: Select minimum $K$ such that $\frac{\sum_{j=1}^K \lambda_j}{\sum_{j=1}^N \lambda_j} \ge \tau$, with $\tau \in \{0.40, 0.55, 0.65, 0.75\}$ (`source-reported`).
- **Factor Returns:** $F_{j,t} = \tilde{R}_t \cdot q_j$ (`source-reported`).
- **Multifactor OLS Regression:**
  - Sub-window: Trailing 60 trading days (`source-reported`).
  - Model: $R_{i,t} = \alpha_i + \sum_{j=1}^K \beta_{i,j} F_{j,t} + \epsilon_{i,t}$ (`source-reported`).
  - Intercept $\alpha_i$ (daily drift) and factor exposures $\beta_{i,j}$ estimated via ordinary least squares (`source-reported`).
- **Cumulative Residuals:** $X_{i,t} = \sum_{s=1}^t \epsilon_{i,s}$ over the 60-day sub-window (`source-reported`).

### 2. Ornstein-Uhlenbeck Estimation

- **Continuous-Time Specification:** $dX_t = \kappa (m - X_t) dt + \sigma dW_t$ (`source-reported`).
- **Discrete AR(1) Formulation:** $X_{t+1} = a + b X_t + \eta_t$, estimated via OLS on the 60-day cumulative residuals with $\Delta t = 1/252$ (`source-reported`):
  $$b = \frac{\text{Cov}(X_t, X_{t+1})}{\text{Var}(X_t)}, \quad a = \bar{X}_{t+1} - b \bar{X}_t$$
  $$\kappa = -\frac{\ln b}{\Delta t}, \quad m = \frac{a}{1 - b}, \quad \sigma_{eq} = \sqrt{\frac{\text{Var}(\eta)}{1 - b^2}}$$
- **Equilibrium De-Meaning:** The authors do *not* subtract the cross-sectional mean from $m$ in their primary baseline backtest, adhering strictly to the assignment specifications (`source-reported`).
- **Stationarity Filter:** Only assets with mean-reversion speed $\kappa \ge 8.4\text{ yr}^{-1}$ (half-life $\tau_{1/2} = \frac{\ln 2}{\kappa} \le 25$ trading days) and stationary autoregressive coefficient $b \in (0, 1)$ are eligible for trading (`source-reported`). If $b \ge 1$ or $\kappa < 8.4$, the asset is classified as invalid and existing positions are immediately liquidated (`source-reported`).

### 3. Modified S-Score Computation

The modified s-score accounts for the annualized residual drift $\alpha_i^{ann} = \alpha_i / \Delta t = 252 \cdot \alpha_i$ (`source-reported`):
$$s_{mod, i}(t) = \frac{X_{i,t} - m_i}{\sigma_{eq, i}} - \frac{\alpha_i^{ann}}{\kappa_i \sigma_{eq, i}} = \frac{X_{i,t} - m_i - \frac{\alpha_i^{ann}}{\kappa_i}}{\sigma_{eq, i}}$$
(Note: the authors corrected the primary utility pipeline to pass the regression drift $\alpha_i$ from the factor OLS into the s-score function) (`source-reported`).

### 4. Trading Rules and State Machine

Symmetric threshold state machine operating daily (`source-reported`):
- **Buy to Open (Long entry):** If $s_{mod, i} < -s_{bo}$ (baseline $s_{bo} = 1.25$), set position = $+1$ (`source-reported`).
- **Sell to Close (Long exit):** If previous position was $+1$ and $s_{mod, i} > -s_{bc}$ (baseline $s_{bc} = 0.50$), set position = $0$ (`source-reported`).
- **Sell to Open (Short entry):** If $s_{mod, i} > +s_{so}$ (baseline $s_{so} = 1.25$), set position = $-1$ (`source-reported`).
- **Buy to Close (Short exit):** If previous position was $-1$ and $s_{mod, i} < +s_{sc}$ (baseline $s_{sc} = 0.50$), set position = $0$ (`source-reported`).
- **Hold Position:** If no threshold is breached and the asset remains valid, maintain existing position (`source-reported`).
- **Invalidation Exit:** If asset fails the $\kappa \ge 8.4$ filter or $b \ge 1$, force close position to $0$ immediately (`source-reported`).

### 5. Trading Time (Volume-Adjusted) Variant

- **Volume-Adjusted Return:** $\bar{R}_{i,t} = R_{i,t} \cdot \frac{\langle V_i \rangle_t}{V_{i,t}}$ (`source-reported`).
- **Trailing Volume Baseline:** $\langle V_i \rangle_t = \frac{1}{60} \sum_{k=1}^{60} V_{i, t-k}$ (shifted by 1 bar to prevent lookahead bias) (`source-reported`).
- **Clipping Guardrail:** Adjustment ratio $\frac{\langle V_i \rangle_t}{V_{i,t}}$ clipped to a maximum of $10.0$ to prevent explosive return amplification on near-zero volume prints (`source-reported`).

## Required data

- **Universe:** Euro Stoxx 50 (SX5E) constituent equities (46 continuous assets after dropping tickers with incomplete historical coverage) (`source-reported`).
- **Venue:** European national exchanges (Euronext Paris/Amsterdam/Brussels, Deutsche Börse Xetra, BME Spanish Exchanges, Borsa Italiana) (`source-reported`).
- **Market Type:** Cash Equities (Long/Short margin accounts) (`source-reported`).
- **Timeframe:** Daily bars (close-to-close) (`source-reported`).
- **Fields Required:**
  - Price: Adjusted daily close prices in EUR (`source-reported`).
  - Volume: Daily share trading volume (`source-reported`).
- **Sample Range:** 2013-01-02 to 2023-02-17 (2,600 trading dates) (`source-reported`).
- **Point-in-Time Separation:**
  - Initial 252-day estimation window: 2013-01-03 to 2013-12-24 (`source-reported`).
  - Rolling backtest execution: 2013-12-24 to 2023-02-17 (2,287 rebalance periods) (`source-reported`).
  - Volume moving average strictly shifted by 1 day (`vol.shift(1).rolling(60).mean()`) to avoid contemporaneous leakage (`source-reported`).
- **Missing Data Handling:** Assets with incomplete records across the 252-day estimation window are excluded from the correlation decomposition for that window (`source-reported`).

## Execution assumptions

- **Execution Timing:** Signals calculated at daily close; execution occurs at next-day returns using an explicit 1-day portfolio shift (`aligned_portfolios = portfolios.shift()`) (`source-reported`).
- **Order Fill Model:** Modeled fill at daily closing price with no intraday price slippage or fill delay beyond the 1-day discrete shift (`source-reported`).
- **Portfolio Construction & Sizing:**
  - Equal-weighted across active positions targeting 100% gross exposure (`source-reported`):
    $$w_{i,t} = \frac{\text{position}_{i,t}}{\sum_{k=1}^N |\text{position}_{k,t}|}$$
  - Not dollar-neutral: If the number of active longs exceeds shorts, the portfolio holds an unhedged directional market tilt (`source-reported`).
- **Transaction Costs:** Flat 5 bps (0.0005) all-in friction rate applied to one-way portfolio turnover (`source-reported`):
  $$\text{Turnover}_t = \sum_{i=1}^N |w_{i,t} - w_{i, t-1}|, \quad \text{Cost}_t = \text{Turnover}_t \times 0.0005$$
- **Short Borrow & Financing Fees:** Omitted in the primary model (`source-reported`). (No short borrow fee or cash borrowing cost is explicitly simulated).
- **Position Capacity:** Unlimited within the 100% gross exposure constraint; market impact is not modeled (`source-reported`).

## Evidence

### Source-reported

All quantitative performance figures trace directly to `Assignement_4a__Group_12_RM.pdf` (Tables 1, 2, 3, and 4) and execution outputs in `ex4a_notebook.ipynb` at commit `e56c954f46111f116b3c6e6b988c6bce10e9b36c`:

#### 1. Baseline Strategy Performance & Transaction Cost Attrition (Table 1)

Fixed $K=4$ factors, $s_{bo} = s_{so} = 1.25$, $s_{bc} = s_{sc} = 0.50$, 2,287 rebalance dates (`source-reported`):
- **Gross (No Costs):**
  - Annualised Return: **3.44%** (`source-reported`)
  - Annualised Volatility: **5.67%** (`source-reported`)
  - Sharpe Ratio: **0.61** (`source-reported`)
  - Maximum Drawdown: **-8.96%** (`source-reported`)
- **Net (5 bps Transaction Costs):**
  - Annualised Return: **0.47%** (`source-reported`) (an 86.3% return reduction)
  - Annualised Volatility: **5.67%** (`source-reported`)
  - Sharpe Ratio: **0.08** (`source-reported`) (an 86.9% Sharpe collapse)
  - Maximum Drawdown: **-10.05%** (`source-reported`)
- **Position Count:** Averages ~10 long and ~10 short positions (total 19.3 to 20 active positions) (`source-reported`).

#### 2. Sensitivity to Opening Threshold (Table 2, No Costs, $K=4$)

Closing thresholds held fixed at $s_{bc} = s_{sc} = 0.50$ (`source-reported`):
- $s_{bo} = 1.00$: Annualised Return 2.96%, Volatility 5.08%, Sharpe **0.58**, Max DD -8.10% (`source-reported`).
- $s_{bo} = 1.25$: Annualised Return 3.44%, Volatility 5.67%, Sharpe **0.61**, Max DD -8.96% (`source-reported`).
- $s_{bo} = 1.50$: Annualised Return 1.86%, Volatility 6.92%, Sharpe **0.27**, Max DD -16.11% (`source-reported`).
- $s_{bo} = 2.00$: Annualised Return **-1.41%**, Volatility 10.10%, Sharpe **-0.14**, Max DD **-31.93%** (`source-reported`).
- *Finding:* Widening entry thresholds to $s_{bo} = 2.0$ causes severe performance collapse into negative territory because signals become overly concentrated, leaving insufficient diversification across the 46 assets (`source-reported`).

#### 3. Variable Factor Selection vs Fixed $K=4$ (Table 3, No Costs)

Selecting factors to meet explained-variance threshold $\tau$ (`source-reported`):
- $\tau = 40\%$ (average 1.4 factors): Return 3.75%, Vol 7.00%, Sharpe **0.54**, Max DD **-19.35%** (`source-reported`). Leaves un-modeled sector effects in residuals.
- $\tau = 55\%$ (average 3.5 factors): Return 4.10%, Vol 6.77%, Sharpe **0.61**, Max DD **-13.22%** (`source-reported`).
- $\tau = 65\%$ (average 6.8 factors): Return 3.75%, Vol 5.75%, Sharpe **0.65**, Max DD **-9.97%** (`source-reported`). Achieves peak Sharpe ratio by absorbing more systematic risk.
- $\tau = 75\%$ (average 12.0 factors): Return 1.20%, Vol 5.44%, Sharpe **0.22**, Max DD **-14.74%** (`source-reported`).
- Fixed $K=4$ (4.0 factors): Return 3.44%, Vol 5.67%, Sharpe **0.61**, Max DD **-8.96%** (`source-reported`).
- *Finding:* Overfitting occurs sharply at $\tau = 75\%$. Extracting 12 components from 46 stocks fits sample noise into factor returns, stripping the residuals of true mean-reverting alpha and reducing Sharpe by 66% (`source-reported`).

#### 4. Volume-Adjusted Trading Time Falsification (Table 4)

Calendar time vs volume-adjusted trading time ($K=4$, $s_{bo} = 1.25$) (`source-reported`):
- **Calendar Time Gross:** Return 3.44%, Vol 5.67%, Sharpe **0.61**, Max DD -8.96% (`source-reported`).
- **Calendar Time Net (5 bps):** Return 0.47%, Vol 5.67%, Sharpe **0.08**, Max DD -10.05% (`source-reported`).
- **Trading Time Gross:** Return 3.00%, Vol 6.23%, Sharpe **0.48**, Max DD -14.35% (`source-reported`).
- **Trading Time Net (5 bps):** Return **-0.05%**, Vol 6.23%, Sharpe **-0.01**, Max DD **-16.31%** (`source-reported`).
- *Finding:* Trading time underperforms calendar time across every metric, and becomes net-negative under realistic transaction costs (`source-reported`).

### Independently reproduced

Not independently reproduced. All metrics and diagnostic results represent verified primary-source findings extracted directly from the repository's executed codebase and documentation.

### Negative evidence

- The Avellaneda-Lee volume-adjusted "trading time" concept fails completely in concentrated liquid equity universes; volume adjustment increases volatility (+56 bps), increases maximum drawdown (-539 bps gross, -626 bps net), and flips net Sharpe negative (-0.01).
- Daily rebalanced PCA statistical arbitrage on large-cap European equities cannot withstand standard institutional trading friction: an all-in cost of 5 bps reduces annual return from 3.44% to 0.47%, rendering the strategy economically unviable.
- High-order factor extraction ($\tau \ge 75\%$) introduces severe factor overfitting, destroying the residual mean-reversion signal.
- Wider entry thresholds ($s_{bo} \ge 2.0$) produce large losses (-1.41% return, -31.93% drawdown) due to extreme signal sparsity and lack of cross-sectional diversification.

## Falsification plan

To falsify whether any refined variation of PCA factor-residual statistical arbitrage can deliver positive net alpha in concentrated equity markets, an independent quantitative research pipeline must evaluate:

1. **Transaction-Cost Deadband / Turnover Throttle:** Implement a minimum holding period $\ge 3$ trading days or an execution deadband where rebalancing orders are withheld if target weight adjustment $|\Delta w_i| < 1.5\%$ (`research-proposed`). Falsification criterion: If annual portfolio turnover cannot be reduced by at least 50% without reducing gross Sharpe below 0.40, reject the strategy as an unmitigated turnover artifact (`research-defined falsification threshold`).
2. **True Dollar-Neutrality Constraint:** Replace the unconstrained 100% gross exposure equal-weighting scheme with an explicit cash-and-beta neutrality quadratic programming solver ($\sum w_i = 0$ and $\sum w_i \beta_{i,j} = 0, \forall j$) (`research-proposed`). Falsification criterion: If dollar-neutral gross Sharpe drops below 0.30 (`research-defined falsification threshold`), confirm that baseline returns were driven by residual market-beta exposure rather than idiosyncratic mean-reversion alpha.
3. **Execution Cost Stress Ladder:** Step execution costs across 1, 3, 5, 8, and 10 bps (`research-proposed`). Falsification cutoff: If the net Sharpe ratio crosses zero at an execution friction $\le 4.0\text{ bps}$ (`research-defined falsification threshold`), deem the strategy un-executable in production.
4. **Volume Adjustment Inversion Test:** Invert the trading-time hypothesis by dampening rather than amplifying low-volume returns ($\bar{R}_{i,t} = R_{i,t} \cdot \frac{V_{i,t}}{\langle V_i \rangle}$) or conditioning entry exclusively on volume spikes ($V_t > 1.5 \cdot \langle V \rangle$) (`research-proposed`). Falsification criterion: If volume-spike conditioning fails to outperform calendar time by at least +0.20 Sharpe (`research-defined falsification threshold`), reject volume-conditioning as an alpha filter in mega-cap equities.

## Crypto portability

**Adapted / Unproven.** The primary source investigates European cash equities (Euro Stoxx 50) exclusively. Porting this Avellaneda-Lee PCA statistical arbitrage framework to cryptocurrency markets represents a theoretical adaptation (`research-proposed`):

Structural and operational crypto differences:
1. **Dominant Single-Factor Market Structure:** Unlike equities where 4–7 principal components explain 55–65% of cross-sectional variance across diverse industrial sectors, cryptocurrency returns (top 30–50 altcoins) are overwhelmingly dominated by a single market mode (Bitcoin/Ethereum beta), which routinely accounts for 60–80% of total variance. Higher-order PCA components in crypto are notoriously unstable and drift rapidly across regimes.
2. **Perpetual Funding Drag:** Crypto statistical arbitrage typically trades perpetual futures. Holding 10 long and 10 short positions across altcoins subjects the portfolio to asymmetric 8-hour funding rates. If active longs carry positive funding while shorts carry negative funding, net funding drag will rapidly exceed the modest 3–4% gross annual returns observed in equity factor stat-arb.
3. **Asymmetric Liquidity & Spreads:** In the Euro Stoxx 50, all 46 assets are ultra-liquid blue-chips with median spreads below 3–5 bps. In crypto, altcoin spreads widen dramatically outside the top 5 names, with taker fees of 4–6 bps and high slippage on liquidations, exacerbating the turnover cost destruction identified in the primary study.
4. **Volume Meaning Divergence:** In crypto perpetuals, low-volume periods frequently indicate low retail participation during Asian/weekend hours, but sharp moves on low volume can trigger cascading liquidations. The volume-adjusted trading time distortion would be even more severe in crypto.
5. **Portability Verdict:** `unproven`. Direct implementation of Avellaneda-Lee PCA statistical arbitrage in crypto spot or perpetuals is strongly contraindicated without continuous funding-cost hedging, market-mode isolation, and strict turnover suppression.

## Limitations

- **Survivorship Bias:** The underlying dataset was constructed using fixed Euro Stoxx 50 constituents as of early 2023, excluding historical index deletions across 2013–2022 (`source-reported`). This survivorship bias likely flatters gross baseline performance by approximately 50–100 bps annually (`research-proposed`).
- **Unmodeled Short Borrow Costs:** The backtest assumes zero borrow fee for short positions (`source-reported`). While large-cap Euro Stoxx 50 names are general collateral (GC) with modest borrow fees (10–30 bps/year), hard-to-borrow spikes during corporate events would further reduce net returns.
- **Concentrated Universe Scope:** The study is restricted to 46 mega-cap assets (`source-reported`). The findings regarding volume adjustment cannot be generalized to small-cap or cross-sectional equity universes where liquidity shocks may follow different dynamics.
- **Lack of Out-of-Sample Walk-Forward Split:** The factor model and O-U parameters are re-estimated daily rolling, but hyperparameter selections ($s_{bo}=1.25$, $s_{bc}=0.50$, $\kappa \ge 8.4$, $K=4$) were evaluated over the full 2013–2023 backtest period rather than on an isolated out-of-sample test fold (`source-reported`).

## Implementation status

`not-implemented`. This record captures research and empirical falsification findings only. No code or configuration has been implemented in PyBroker, NautilusTrader, paper trading, testnet, or live production environments.

## Adoption boundary

`research-only`. This record is cataloged strictly for research documentation, risk control design, and algorithmic falsification awareness. It does **not** authorize implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]` — Forensic falsification of cointegration pairs trading, unbounded beta artifacts, and regime fragility.
- `[[statistical-arbitrage-methodology-degradation-ladder-falsification-2026-09-12]]` — Grant J. Kim's 8-rung degradation ladder isolating look-ahead bias and O-U half-life proxy effects.
- `[[pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12]]` — Walk-forward ADF filtering demonstrating formation-window variance compression.
- `[[johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md]]` — Multi-asset Johansen cointegration with execution friction asymmetry.
- `[[crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]` — Avellaneda-Lee PCA residual and Johansen cointegration breakdown in cryptocurrency spot markets.
- `[[sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]` — S&P 500 Johansen cointegration vs Ornstein-Uhlenbeck ablation under multiple hypothesis testing.
- `[[global-equity-sac-hierarchical-dirichlet-adaptive-retraining-2026-09-04]]` — Soft Actor-Critic RL portfolio allocation evaluated across NASDAQ-100, Nikkei 225, and EURO STOXX 50.

## Sources

1. **Primary Codebase & Data:** Simone Cerrone (`SimoneCerrone`), *StatArb-EMU-Equities: Statistical Arbitrage in the Euro Stoxx 50 Equities Market*, GitHub repository `SimoneCerrone/StatArb-EMU-Equities`, commit `e56c954f46111f116b3c6e6b988c6bce10e9b36c`, September 11, 2026. Stable URL: [https://github.com/SimoneCerrone/StatArb-EMU-Equities](https://github.com/SimoneCerrone/StatArb-EMU-Equities).
2. **Academic Report:** Simone Cerrone, Filippo Tacconi, Vittoria Tomasini, Aloïs Maréchal, *Assignment 4a: Buy Side - Statistical Arbitrage in the EMU Equity Market*, Group 12, Politecnico di Milano (Financial Engineering FY 2025–2026), 17 April 2026. File path: `Assignement_4a__Group_12_RM.pdf`.
3. **Execution Notebook:** `ex4a_notebook.ipynb` (Jupyter notebook containing complete rolling backtest pipeline, parameter calibration, sensitivity analyses, and output tables).
4. **Code Modules:**
   - `utilities/statistical_arbitrage.py` (PCA factor model estimation, discrete AR(1) O-U parameter estimation, modified s-score computation, position state machine, and volume-adjusted return transformation).
   - `utilities/backtest_2.py` (Portfolio alignment, discrete 1-bar execution shift, daily turnover tracking, and transaction cost deduction).
   - `utilities/principal_component_analysis.py` (Eigendecomposition and eigenvector alignment).
   - `utilities/covariance_utilities.py` (Correlation matrix validation and symmetry checking).
5. **Reference Literature:**
   - Marco Avellaneda and Jeong-Hyun Lee, *Statistical arbitrage in the U.S. equities market*, Quantitative Finance, 10(7), 761–782, 2010. DOI: [10.1080/14697680903124632](https://doi.org/10.1080/14697680903124632).
