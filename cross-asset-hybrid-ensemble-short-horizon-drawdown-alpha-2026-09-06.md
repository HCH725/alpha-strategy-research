---
schema: strategy-research-record-v1
title: "Cross-Asset Hybrid Neural-Tree Ensemble for Short-Horizon Drawdown Risk Forecasting and Alpha Generation"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning
  - ensemble
  - mlp
  - xgboost
  - catboost
  - drawdown-prediction
  - cross-asset
  - equity-index
  - spy
  - shap
  - mutual-information
  - hurst-exponent
status: research-only
confidence: medium
source_as_of: 2025-10-26
sources:
  - "arXiv:2510.22348v1 — https://arxiv.org/abs/2510.22348"
  - "DOI: 10.48550/arXiv.2510.22348"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Asset Hybrid Neural-Tree Ensemble for Short-Horizon Drawdown Risk Forecasting and Alpha Generation

## Provenance

- **Paper:** Ranjan, A. (2025). "Causal and Predictive Modeling of Short-Horizon Market Risk and Systematic Alpha Generation Using Hybrid Machine Learning Ensembles." *arXiv preprint* arXiv:2510.22348v1 [q-fin.CP / q-fin.TR].
- **Author & Affiliation:** Aryan Ranjan, University of Oxford, United Kingdom (`aryan.ranjan@stcatz.ox.ac.uk`).
- **Submission Date:** October 26, 2025.
- **Canonical arXiv Abstract URL:** https://arxiv.org/abs/2510.22348
- **Canonical arXiv PDF:** https://arxiv.org/pdf/2510.22348
- **DOI:** https://doi.org/10.48550/arXiv.2510.22348
- **Primary Source Inspection:** Direct full-text LaTeX manuscript (`main.tex`, figures `mutual_info.png`, `confusion_matrix.png`, `crash.png`, `non_crash.png`, `risk_quantile.png`, `dist.png`, `signal.png`, `strategy.png`) inspected and verified via the official arXiv source package.
- **Code & Repository Provenance:** No public repository link was included in the manuscript (provenance gap noted).
- **Publication Status:** Working paper / preprint on arXiv; not verified as peer-reviewed journal publication as of record date.

## Economic mechanism

### Source-reported

Conventional risk forecasting frameworks (e.g., univariate GARCH, linear multi-factor models) assume linear dependencies and Gaussian error distributions, rendering them ineffective at capturing sudden intramonth market dislocations and cross-asset spillover dynamics (e.g., the March 2023 regional banking stress, April 2025 tariff announcements, and sharp weekly corrections from record index highs). While recurrent neural networks (LSTMs) combined with GARCH have been proposed in earlier literature, their complex gating structures and high computational overhead hinder practical latency-sensitive deployment.

The author proposes that short-horizon equity drawdowns ($\ge 1\%$ over a 5-day horizon in the SPY ETF) are preceded by detectable, non-linear stress signals across non-equity asset classes—specifically energy commodities (crude oil), foreign exchange (EUR/USD, JPY/USD, USD Index), and short- and long-term interest rates (13-week Treasury Bill IRX, 10-year Treasury Note TNX):
1. **Leading cross-asset transmission:** Equity markets often behave as reactive rather than proactive systems. Macroeconomic pressures, monetary tightening signals, and commodity supply/demand imbalances materialize in fixed income, FX, and commodity derivatives prior to equity index repricing.
2. **Asymmetric regime roles:** In crash regimes, commodities and small-cap equities (IWM) act as shock amplifiers, exhibiting extreme higher-order moments (skewness and kurtosis) that signal systemic liquidity stress. Conversely, in non-crash (calm) regimes, FX markets act as risk-redistribution and stabilization mechanisms, where orderly capital flows dampen market volatility.
3. **Decoupling of unconditional vs. conditional predictability:** While unconditional mutual information (MI) highlights multiscale Hurst exponents (persistence and mean-reversion metrics) as the strongest individual dependencies, conditional feature attribution (SHAP) demonstrates that immediate cross-asset shocks and higher-order moments absorb the predictive power of long-term memory metrics during actual crash timing.

### Research interpretation

Hypothesized mechanism: **cross-market liquidity and tail-risk transmission into equity index drawdowns**.

The economic premise relies on institutional capital rebalancing across asset classes under emerging macro-financial stress. When short-term money markets (IRX) tighten or crude oil futures experience sharp negative skew/elevated kurtosis, margin demands, risk-parity deleveraging, and institutional portfolio hedges trigger selling in high-beta and small-cap equities (IWM) first, subsequently spilling into broad-market index products (SPY).

**Critical research caveat on sample evaluation:**
The author's headline performance metrics (Sharpe ratio 2.51, CAPM alpha $+0.28$ annualized, CAPM beta 0.51, and CAGR 40.84%) represent **in-sample backtest results** over the 2005–2025 sample. Although base learner hyperparameter optimization utilized time-series split cross-validation, the final soft-voting ensemble was fitted over the complete dataset, and the trading strategy was evaluated in-sample without transaction cost deduction or walk-forward out-of-sample isolation. The empirical results must therefore be treated as an in-sample upper-bound feasibility proof rather than verified executable alpha.

## Signal

- **Instrument traded:** SPY (SPDR S&P 500 ETF Trust).
- **Target definition (Source-reported):** Binary weekly drawdown indicator $y_t \in \{0, 1\}$:
  $$y_t = \mathbf{1}\Bigg\{ \sum_{k=1}^h r_{\text{SPY}, t+k} \le -\delta \Bigg\}$$
  where $h = 5$ trading days, $\delta = 1\%$ ($0.01$), and $r_{\text{SPY}, t} = \ln(P_{\text{SPY}, t}) - \ln(P_{\text{SPY}, t-1})$.
- **Cross-asset universe $\mathcal{U}$ (10 assets, Source-reported):**
  - Equities: SPY, QQQ, IWM, TLT
  - Volatility: VIX
  - Commodities: GLD, CL=F (Crude Oil Futures)
  - Foreign Exchange: DX-Y.NYB (US Dollar Index), EURUSD=X, JPYUSD=X
  - Treasuries: TNX (10-Year Treasury Yield), IRX (13-Week Treasury Bill Yield)
- **Feature engineering (178 raw candidate features, Source-reported):**
  1. *Time-series moments:* Rolling standard deviation $\sigma_{i,t}^{(w)}$, skewness $\gamma_{i,t}^{(w)}$, excess kurtosis $\kappa_{i,t}^{(w)}$, and Shannon entropy $H_{i,t}^{(w)}$ (with $B=30$ histogram bins) over windows $w \in \{21, 63\}$ trading days.
  2. *Multiscale Hurst exponent:* $H_{i,t}^{(\tau)}$ over $\tau \in \{16, 64, 256\}$ days using vectorized rescaled range ($R/S$) methodology centered on powers of two.
  3. *Cross-asset relations:* Rolling OLS beta $\beta_{i,\text{SPY},t}^{(w)}$ and rolling Pearson correlation $\rho_{i,\text{SPY},t}^{(w)}$ over windows $w \in \{21, 63\}$ days.
  4. *Information-theoretic measures:* Rolling Kullback-Leibler divergence $\text{KL}_{i,t}^{(w_{\text{curr}}, w_{\text{ref}})}$ between a short-term window ($w_{\text{curr}}=21$ days) and a long-term reference window ($w_{\text{ref}}=126$ days).
- **Feature selection pipeline (Source-reported):**
  - Step 1: Low-variance filter removing features with variance $< 10^{-4}$.
  - Step 2: Collinearity filter removing one feature from any pair with Pearson $|r| \ge 0.95$, reducing feature count from 178 to 134.
  - Step 3: Mutual Information (MI) ranking against target $y_t$, retaining the top 80 features.
- **Model architecture (Hybrid Soft-Voting Ensemble, Source-reported):**
  - Base learner $M_1$: Shallow Multi-Layer Perceptron (MLP) with 1 to 3 hidden layers, moderate width, ReLU/tanh activations, and softmax output.
  - Base learners $M_2, \dots, M_K$: Gradient Boosted Decision Trees (XGBoost and CatBoost) minimizing logistic loss.
  - Hyperparameter tuning: Grid search with temporal `TimeSeriesSplit` cross-validation maximizing ROC-AUC.
  - Probability aggregation:
    $$\hat{p}(\mathbf{x}_t) = \frac{1}{K} \sum_{k=1}^K \hat{p}_k(\mathbf{x}_t)$$
    where $\hat{p}_k(\mathbf{x}_t)$ is the estimated probability of a $\ge 1\%$ SPY 5-day drawdown from learner $M_k$.
- **Trading decision rules (Source-reported):**
  - **Long Entry:** Enter long SPY when predicted crash probability $\hat{p}(\mathbf{x}_t) < 0.50$ (benign / low-risk environment).
  - **Short Entry:** Enter short SPY when predicted crash probability $\hat{p}(\mathbf{x}_t) \ge 0.50$ (elevated drawdown risk).
  - **Position Sizing:** Scaled dynamically according to predicted probability. *(Author states exposure is scaled with confidence but does not specify the exact continuous formula; provenance gap noted).*
    - `research-proposed: linear continuous exposure $w_t = 2 \cdot (0.50 - \hat{p}_t) \in [-1.0, +1.0]$, or quintile step function allocating $+1.0$ in Q1-Q2, $+0.5$ in Q3, $0.0$ in Q4, and $-1.0$ in Q5`
- **Execution cadence:** Daily trading rebalance (`source-reported: trades are made daily`).
- **Signal formation timestamp:** Daily close ($t$) after calculating rolling moments and model prediction (`research-proposed: 15:59:00 EST daily evaluation`).

## Required data

- **Universe / Instruments:**
  - SPY (target trading instrument and feature input)
  - QQQ, IWM, TLT, VIX, GLD, CL=F, DX-Y.NYB, EURUSD=X, JPYUSD=X, TNX, IRX
- **Timeframe:** Daily OHLCV price series and yield levels.
- **Sample period:** 2005-01-01 to 2025-05-31 (5,423 daily observations).
- **Data preprocessing:** Forward-filled to align cross-asset non-trading days/holidays; z-score standardized.
- **Point-in-time constraints:** All features must use strictly backward-looking windows ($t-w+1:t$). Target $y_t$ uses forward returns $t+1:t+5$ and must be quarantined from model inputs during training.

## Execution assumptions

- **Source-reported status:** The author explicitly discloses: *"These metrics do not currently account for transaction costs nor have they been forward tested. This remains an active consideration for future work."*
- **Order type:** `research-proposed: Market-On-Close (MOC) at 15:59:30 EST or Market-On-Open (MOO) at 09:30:00 EST on day t+1`.
- **Transaction costs:** `research-proposed: 1.0 bps brokerage/clearing commission + 1.0 bps half-spread slippage per trade (2.0 bps round-turn)`.
- **Borrow / Shorting constraints:** `research-proposed: SPY is assumed hard-to-borrow exempt with 25 bps annualized borrow fee for short exposure`.
- **Slippage & Market Impact:** `research-proposed: negligible for retail/mid-frequency volumes due to SPY daily liquidity > $30B; capacity threshold estimated at $250M AUM under 1.0% ADV participation`.

## Evidence

### Source-reported

All figures below are directly extracted from the primary manuscript (Ranjan 2025, Table 2, Table 4, and Section 3.3/4.2) over the 2005–2025 dataset (5,423 observations):

- **Validation Set Classification Performance (In-sample, Table 2):**
  - Accuracy: 0.95
  - Class 0 (Non-crash, Support: 4,232): Precision 0.95, Recall 0.99, F1-score 0.97
  - Class 1 (Crash, Support: 1,191): Precision 0.95, Recall 0.82, F1-score 0.88
  - Macro Average: Precision 0.95, Recall 0.90, F1-score 0.92
  - Weighted Average: Precision 0.95, Recall 0.95, F1-score 0.95
  - Confusion Matrix: 93 false negatives (missed mild drawdowns), 240 false positives (transient volatility without 5-day drop).
- **Risk Quantile Returns (Realized 5-day SPY Return, Section 3.3):**
  - High-risk quintile (Q5, HIGH-risk period): Average 5-day SPY return = $-1.89\%$.
  - Lower-risk quintiles (Q1–Q4, LOW-risk period): Average 5-day SPY return = $+0.75\%$.
- **Trading Strategy Performance (In-sample 2005–2025, Table 4):**
  - Sharpe Ratio: 2.51
  - Information Ratio vs. SPY: 1.73
  - Maximum Drawdown: $-18.12\%$
  - Annualized Return: $40.84\%$
  - Annualized Volatility: $13.23\%$
  - CAPM Alpha (daily): $0.00111$ ($t$-statistic: 14.03; annualized $\approx +0.28$ reported in abstract)
  - CAPM Beta: 0.51
- **Top Mutual Information Features (Table 1):**
  - `CL=F_hurst_short`: 0.109211
  - `JPYUSD=X_hurst_short`: 0.107575
  - `IRX_hurst_short`: 0.107422
  - `GLD_hurst_short`: 0.106937
  - `TNX_hurst_short`: 0.104463
  - `DX-Y.NYB_hurst_short`: 0.103586
  - `EURUSD=X_hurst_short`: 0.103037
  - `TLT_hurst_short`: 0.101677
  - `VIX_hurst_short`: 0.100433
  - `QQQ_hurst_short`: 0.098766
  - `IWM_hurst_short`: 0.098508
  - `IRX_vol_63d`: 0.095007
  - `SPY_hurst_short`: 0.092049

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **In-sample fitting bias:** The reported Sharpe ratio of 2.51 and alpha $t$-statistic of 14.03 reflect in-sample strategy simulation where the final ensemble was fitted over the full 20-year sample (2005–2025). The paper does not provide an out-of-sample forward test or walk-forward validation curve.
- **Zero friction assumption:** No trading commissions, borrow fees, or execution slippage were deducted. Given daily rebalancing and frequent state switching, turnover drag could substantially erode reported Sharpe.
- **Missed drawdown clusters:** The author reports 93 false negatives during the sample period, corresponding to market episodes where drawdowns occurred without preceding cross-asset turbulence.
- **Divergence of Hurst utility:** While Hurst exponents ranked highest in unconditional MI, conditional SHAP attribution revealed their contribution was largely redundant when combined with short-term return moments.

## Falsification plan

To disconfirm the validity of the cross-asset drawdown prediction alpha:
1. **Walk-forward out-of-sample test:**
   - Train on expanding windows (e.g., initial train 2005–2014, test 2015–2025) with strictly purged and embargoed feature sets.
   - `research-defined falsification threshold: out-of-sample Sharpe ratio < 0.80 or annualized CAPM alpha t-statistic < 2.0`.
2. **Transaction cost stress test:**
   - Apply realistic execution costs of 2.5 bps per one-way trade (5.0 bps round-turn) plus 0.50% annualized short borrow fee.
   - `research-defined falsification threshold: post-cost Sharpe reduction > 50% relative to gross performance, or net CAGR < SPY buy-and-hold CAGR`.
3. **Cross-asset ablation test:**
   - Train ensemble using only equity features (SPY, QQQ, IWM, VIX) excluding commodity, FX, and Treasury signals.
   - `research-defined falsification threshold: cross-asset ensemble fails to outperform equity-only ensemble by at least 0.30 Sharpe points out-of-sample`.
4. **Placebo / Shuffled label test:**
   - Randomly permute target labels $y_t$ preserving time-series autocorrelation via block-bootstrap.
   - `research-defined falsification threshold: synthetic noise model achieves test-set ROC-AUC > 0.60`.

## Crypto portability

- **Portability status:** `adapted / unproven` (Research interpretation; primary source investigates traditional US equities, commodities, FX, and Treasuries exclusively).
- **Mechanism adaptation:**
  - In cryptocurrency markets, Bitcoin (BTC) serves as the systemic market proxy analogous to SPY.
  - Cross-asset predictive signals could be mapped to:
    1. *Stablecoin supply & treasury yield dynamics:* Tether (USDT)/Circle (USDC) mint/burn flows and DeFi lending yields (Aave/Compound) replacing Treasury bill yields (IRX/TNX).
    2. *Derivatives liquidity & funding rates:* BTC perpetual funding rate skew, annualized basis on CME futures, and options implied volatility surface (Deribit DVOL) replacing VIX.
    3. *Altcoin liquidity beta:* High-beta altcoins (e.g., SOL, ETH, meme baskets) replacing small-cap equities (IWM) as early-warning liquidity canaries.
- **Portability risks:**
  - *24/7 continuous trading:* No daily market close/open auction; requires rolling timestamp discretization (e.g., 00:00 UTC).
  - *Extreme non-stationarity:* Crypto market structure undergoes rapid structural shifts (e.g., spot ETF approvals, exchange insolvencies), making 20-year feature stability assumptions invalid.
  - *Shorting / funding friction:* Perpetual short positions incur variable 8-hour funding rates that can become heavily negative during panic cascades, penalizing short hedges.

## Limitations

- **In-sample strategy evaluation:** The primary empirical limitation is the absence of a split train/validation/test forward evaluation.
- **Underspecified position-sizing formula:** The exact mathematical mapping from predicted probability $\hat{p}_t$ to exposure weight $w_t$ is not documented in the text.
- **Zero friction accounting:** Neglect of fees, short borrow interest, and slippage.
- **Look-ahead vulnerability in feature selection:** The mutual information selection of top 80 features was computed over the full sample, potentially introducing subtle look-ahead bias into feature selection.
- **Survivorship / constituent changes:** While SPY, QQQ, and IWM are surviving ETFs, the underlying index constituents change over time.

## Implementation status

- Frontmatter status: `not-implemented`.
- No implementation has been created in NautilusTrader or PyBroker.
- No backtest, paper trading, or live execution has been performed in our stack.

## Adoption boundary

- Research-only capture.
- Not approved for trading, live deployment, or automated signal execution.
- Any future progression requires formal out-of-sample replication with purged walk-forward cross-validation and strict fee accounting in Loop B (PyBroker / NautilusTrader).

## Related Wiki records

- [[quant/same-day-open-to-close-directional-spy-walk-forward-2026-09-02]]
- [[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]
- [[quant/phase8-regularized-nonlinear-ml-toolbox-2026-08-28]]
- [[quant/phase8-temporal-validation-calibration-uncertainty-2026-08-28]]
- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
- [[quant/backtest-overfitting-pbo-cscv-2026-08-27]]
- [[quant/sharpe-deflated-multiple-testing-2026-08-27]]

## Sources

- Ranjan, Aryan. (2025). "Causal and Predictive Modeling of Short-Horizon Market Risk and Systematic Alpha Generation Using Hybrid Machine Learning Ensembles." *arXiv preprint* arXiv:2510.22348v1 [q-fin.CP / q-fin.TR], submitted 2025-10-26. https://arxiv.org/abs/2510.22348.
- Primary LaTeX source package inspected from arXiv: `https://arxiv.org/src/2510.22348` (containing `main.tex`, `00README.json`, and all visual diagnostic assets).
- Digital Object Identifier (DOI): `https://doi.org/10.48550/arXiv.2510.22348`.
