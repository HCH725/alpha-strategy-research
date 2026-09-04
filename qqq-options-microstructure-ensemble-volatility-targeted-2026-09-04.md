---
schema: strategy-research-record-v1
title: "QQQ Options Market Microstructure Ensemble with Volatility-Targeted Position Sizing and Multi-Tier Volatility Regime Filtering"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options-microstructure
  - gamma-exposure
  - variance-risk-premium
  - volatility-skew
  - ensemble-learning
  - volatility-targeting
  - regime-switching
status: research-only
confidence: medium
source_as_of: 2025-11-26
sources:
  - "https://github.com/SMalaekeh/qqq-options-alpha-research/tree/4ab6181a2284b2a072629eb19dc5e89be26564b5"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QQQ Options Market Microstructure Ensemble with Volatility-Targeted Position Sizing and Multi-Tier Volatility Regime Filtering

## Provenance

- **Repository URL:** [https://github.com/SMalaekeh/qqq-options-alpha-research](https://github.com/SMalaekeh/qqq-options-alpha-research)
- **Author:** Sina Malaekeh (developed for the Quanta Options Big Data Challenge)
- **Immutable Commit SHA:** `4ab6181a2284b2a072629eb19dc5e89be26564b5` (committed November 26, 2025)
- **Exact File Paths Inspected:**
  - `README.md`
  - `docs/strategy_logic.md`
  - `docs/methodology.md`
  - `docs/feature_engineering.md`
  - `src/ensemble_model.py`
  - `src/feature_engineering.py`
  - `src/backtesting.py`
- **Target Instrument:** Invesco QQQ Trust ETF (NASDAQ: QQQ) and its listed options chain.
- **Sample Period:** 1,435 daily observations spanning January 2, 2020 to September 17, 2025, constructed by aggregating over 5,000,000 raw end-of-day options contract records.
- **Partitioning:** Chronological split into 60% training (861 days), 20% validation (287 days), and 20% out-of-sample testing (287 days: July 26, 2024 to September 17, 2025).
- **Source As-Of Date:** November 26, 2025.

## Economic mechanism

### Source-reported

The options market operates as an institutional sentiment barometer and positioning indicator. Large institutional market participants use options primarily for portfolio hedging, collateral underwriting, and tail-risk protection rather than unhedged speculation. Market makers (dealers) who warehouse this inventory must continuously dynamically hedge their net delta and gamma exposures in the underlying ETF market to maintain delta-neutrality. This structural imperative induces predictable, non-random order flows that can forecast next-day returns of the underlying index ETF:

1. **Dealer Gamma Exposure (GEX):** When dealers are net long gamma (typically high strike calls), their hedging requires buying into declining prices and selling into rallies, creating price suppression, reduced volatility, and mean reversion around key pinning strikes. When dealers are net short gamma (heavy put accumulation), their hedging accelerates underlying market moves, widening realized volatility and creating directional momentum.
2. **Variance Risk Premium (VRP):** The systematic spread between implied volatility (IV) and realized volatility (RV) reflects an insurance risk premium demanded by option sellers. When VRP expands abnormally, options markets are overpricing downside risk (panic hedging), creating mean-reversion buying opportunities in the underlying asset.
3. **Put/Call Volume and Open Interest Ratios (PCR):** Elevated put purchasing, especially out-of-the-money (OTM) puts, indicates retail and institutional capitulation, frequently marking short-term market bottoms. Conversely, extreme call volume reflects unhedged speculative complacency that precedes pullbacks.
4. **Volatility Skew:** The implied volatility differential between OTM puts and OTM calls reflects downside tail-risk pricing. Steepening monthly skew signals escalating downside hedging demand (bearish signal), whereas flattening skew indicates diminishing hedging pressure and risk-on appetite.

### Research interpretation

The hypothesized economic mechanism is **structural order-flow feedback and institutional hedging pressure**:
1. **Hedging-induced mechanical drift:** Market makers do not take directional bets; their rehedging trades are price-inelastic and mechanically executed based on Black-Scholes Greeks. By aggregating the cross-section of open interest and volume into normalized GEX, VRP, and skew metrics, the ensemble captures the net directional imbalance of upcoming delta-hedging flows.
2. **Ensemble variance reduction across volatility regimes:** Deep neural networks (LSTMs, Transformers) overfit heavily to non-stationary financial time series. An ensemble combining gradient boosting (LightGBM 30%, XGBoost 30%), bagging (Random Forest 30%), and linear regularization (Ridge 10%) anchors predictions against structural noise while allowing non-linear feature interactions (such as GEX $\times$ Momentum and VRP $\times$ Skew).
3. **Volatility-targeted asymmetric exposure:** Because daily equity returns exhibit volatility clustering and negative return-volatility correlation, sizing positions inversely to 20-day realized volatility stabilizes the portfolio risk contribution across calm bull trends and volatile pullbacks, while explicit kill switches protect against liquidity air-pockets.

## Signal

### Mathematical formulation (Source-reported)

1. **Option Moneyness and Tenor Segmentation:**
   Moneyness is defined as $m = K / S$, where $K$ is the option strike and $S$ is the underlying spot price:
   - Deep OTM Put: $m \in [0.00, 0.90)$
   - OTM Put: $m \in [0.90, 0.97)$
   - ATM: $m \in [0.97, 1.03]$
   - OTM Call: $m \in (1.03, 1.10]$
   - Deep OTM Call: $m \in (1.10, 2.00]$

   Tenor buckets by Days to Expiration (DTE):
   - Weekly: $\text{DTE} \in [0, 10)$
   - Monthly: $\text{DTE} \in [10, 45)$
   - Quarterly: $\text{DTE} \in [45, 90)$
   - Long: $\text{DTE} \in [90, 1000)$

2. **Implied Volatility Proxy:**
   For contracts with vega $\nu > 0.01$, IV is approximated using the vega relationship:
   $$\sigma_{\text{call}} = \frac{C}{\nu \sqrt{\max(\text{DTE}, 1) / 365}}, \quad \sigma_{\text{put}} = \frac{P}{\nu \sqrt{\max(\text{DTE}, 1) / 365}}$$
   $$\sigma_{\text{contract}} = \text{clip}\left(\frac{\sigma_{\text{call}} + \sigma_{\text{put}}}{2}, 0.0, 2.0\right)$$
   For each bucket, daily IV is computed as volume-weighted IV across qualifying contracts:
   $$\mathrm{IV}_{m, \tau} = \frac{\sum_{k \in (m, \tau)} \sigma_k \cdot (V_{\text{call}, k} + V_{\text{put}, k} + 1)}{\sum_{k \in (m, \tau)} (V_{\text{call}, k} + V_{\text{put}, k} + 1)}$$

3. **GEX, VRP, and Skew Metrics:**
   - Total call and put gamma exposures:
     $$\mathrm{GEX}_{\text{call}} = \sum_k \Gamma_k \cdot \mathrm{OI}_{\text{call}, k} \cdot K_k \cdot 100, \quad \mathrm{GEX}_{\text{put}} = \sum_k \Gamma_k \cdot \mathrm{OI}_{\text{put}, k} \cdot K_k \cdot 100$$
     $$\mathrm{GEX}_{\text{raw}} = \mathrm{GEX}_{\text{call}} - \mathrm{GEX}_{\text{put}}$$
   - Point-in-time notional normalization (without look-ahead):
     $$\mathrm{GEX}_{\text{norm}} = \frac{\mathrm{GEX}_{\text{raw}}}{S^2 \cdot 100 + 10^6}$$
   - Rolling 20-day realized volatility:
     $$\mathrm{RV}_{20\text{d}, t} = \sqrt{252} \cdot \sqrt{\frac{1}{19}\sum_{\tau=0}^{19} (r_{t-\tau} - \bar{r}_{20\text{d}})^2}$$
   - Variance Risk Premium:
     $$\mathrm{VRP}_t = \text{clip}(\mathrm{IV}_{\text{ATM}, \text{Monthly}, t} - \mathrm{RV}_{20\text{d}, t}, -0.5, 0.5)$$
   - Volatility Skew:
     $$\mathrm{Skew}_{\text{Monthly}, t} = \text{clip}(\mathrm{IV}_{\text{OTM\_Put}, \text{Monthly}, t} - \mathrm{IV}_{\text{OTM\_Call}, \text{Monthly}, t}, -0.3, 0.3)$$
   - Put/Call Ratios:
     $$\mathrm{PCR}_{\text{Volume}} = \frac{V_{\text{put}}}{V_{\text{call}} + 1}, \quad \mathrm{PCR}_{\text{OTM}} = \frac{V_{\text{OTM\_Put}}}{V_{\text{OTM\_Call}} + 1}$$

4. **Rolling Stationarity Transform (Z-Score):**
   Features are converted to rolling 20-day Z-scores clipped to $[-4.0, +4.0]$:
   $$z(x_t) = \text{clip}\left(\frac{x_t - \mu_{20}(x_t)}{\sigma_{20}(x_t) + 10^{-8}}, -4.0, 4.0\right)$$
   applied to `pcr_volume`, `pcr_otm`, `vrp`, `vol_skew_monthly`, `gex`, `momentum_20d`, and `rv_20d`.

5. **Supervised Target and Model Training:**
   - Target: Next-day percentage return $y_t = \frac{S_{t+1}}{S_t} - 1$.
   - Feature Selection: Top $K=15$ features selected via `f_regression` on the training set.
   - Ensemble Base Models:
     - **LightGBM (30%):** `objective='regression'`, `metric='rmse'`, `n_estimators=500`, `learning_rate=0.01`, `num_leaves=16`, `max_depth=4`, `reg_alpha=1.0`, `reg_lambda=5.0`.
     - **XGBoost (30%):** `n_estimators=500`, `learning_rate=0.01`, `max_depth=3`, `reg_alpha=1.0`, `reg_lambda=5.0`, `random_state=42`.
     - **Random Forest (30%):** `n_estimators=200`, `max_depth=5`, `max_features='sqrt'`, `min_samples_leaf=20`, `random_state=42`.
     - **Ridge Regression (10%):** `alpha=10.0`.
   - Raw Prediction:
     $$\hat{y}_t = 0.30 \cdot \hat{y}_{\text{LGBM}} + 0.30 \cdot \hat{y}_{\text{XGB}} + 0.30 \cdot \hat{y}_{\text{RF}} + 0.10 \cdot \hat{y}_{\text{Ridge}}$$

6. **Signal Smoothing and Volatility-Targeted Position Sizing:**
   - Exponential Moving Average (EMA) smoothing ($\alpha = 0.15$):
     $$\tilde{y}_t = 0.15 \cdot \hat{y}_t + 0.85 \cdot \tilde{y}_{t-1}$$
   - Directional signal with 5 bps deadband threshold:
     $$\text{dir}_t = \begin{cases} +1.0, & \tilde{y}_t > 0.0005 \\ -1.0, & \tilde{y}_t < -0.0005 \\ 0.0, & |\tilde{y}_t| \le 0.0005 \end{cases}$$
   - Volatility targeting ($\sigma_{\text{target}} = 0.15$):
     $$\mathrm{scalar}_t = \text{clip}\left(\frac{0.15}{\mathrm{RV}_{20\text{d}, t}}, 0.5, 1.5\right)$$
   - Four-tier volatility regime filter (kill switch):
     $$\text{signal}_t = \begin{cases} 
     0.0, & \mathrm{RV}_{20\text{d}, t} > 0.40 \quad (\text{crisis exit to cash}) \\
     \text{dir}_t \cdot \mathrm{scalar}_t \cdot 0.50, & 0.28 < \mathrm{RV}_{20\text{d}, t} \le 0.40 \quad (\text{elevated volatility}) \\
     \text{dir}_t \cdot \mathrm{scalar}_t \cdot 0.75, & 0.22 < \mathrm{RV}_{20\text{d}, t} \le 0.28 \quad (\text{medium volatility}) \\
     \text{dir}_t \cdot \mathrm{scalar}_t \cdot 1.00, & \mathrm{RV}_{20\text{d}, t} \le 0.22 \quad (\text{calm regime})
     \end{cases}$$
   - Total portfolio leverage is bounded inside $[-1.0\times, +1.5\times]$.

## Required data

- **Underlying Instrument:** Invesco QQQ Trust Series 1 ETF (NASDAQ: QQQ), daily open, high, low, close, and volume.
- **Options Data:** Complete end-of-day options chain on QQQ including strike $K$, expiration date, contract type (call/put), closing bid/ask, last value, traded volume, open interest (OI), and pre-computed Black-Scholes Greeks ($\Delta$, $\Gamma$, $\nu$).
- **Data Filtering:**
  - `research-proposed: minimum contract open interest of 50 and volume of 10 to filter out stale quotes`.
  - Vega $> 0.01$ required for IV proxy derivation.
- **Aggregation Cadence:** End-of-day (4:00 PM EST market close).
- **Point-in-Time Integrity:** All rolling indicators (Z-scores, moving averages, realized volatility) use historical data up to date $t$. Target is computed strictly on $t+1$. Scaler and feature selector are fitted strictly on the training partition (pre-2024) and applied out-of-sample without leakage.
- **Missing Data Handling:** `SimpleImputer(strategy='constant', fill_value=0.0)` for missing feature values; missing target rows at end of series are dropped.

## Execution assumptions

- **Trade Formation & Fill Timing:**
  - `source-reported`: Features computed from EOD options data at date $t$; target return is defined as $S_{t+1}/S_t - 1$.
  - `research-proposed`: Order execution at market-on-close (MOC) on date $t$ assuming options surface availability 10 minutes prior to close, or market-on-open (MOO) on date $t+1$.
- **Order Type & Execution Model:**
  - `source-reported`: Frictionless execution at daily spot returns (`pct_change()`). Transaction costs are explicitly omitted in primary source code.
  - `research-proposed`: Market orders on liquid underlying QQQ ETF.
- **Transaction Costs & Fees:**
  - `source-reported`: 0 bps (unmodeled).
  - `research-proposed fee assumption`: 0.5 bps commission + 1.0 bps half-spread slippage (total 3.0 bps round-trip transaction cost).
- **Borrow / Shorting:**
  - Short positions (up to $-1.0\times$) require QQQ borrow availability. QQQ is an easy-to-borrow (ETB) mega-cap ETF with typical borrow fee $<0.30\%$ annualized.
- **Margin / Leverage Limits:**
  - Maximum long leverage $+1.5\times$, maximum short leverage $-1.0\times$. Reg-T or portfolio margin requirements apply.

## Evidence

### Source-reported

All performance statistics below are reported directly by Sina Malaekeh from the out-of-sample test partition spanning July 26, 2024 to September 17, 2025 (287 daily observations) under zero transaction costs:

| Metric | Ensemble Strategy | Passive QQQ Buy & Hold Benchmark |
| :--- | :--- | :--- |
| **Calmar Ratio** | **2.14** | ~1.50 |
| **Sharpe Ratio** | **1.92** | ~0.85 |
| **Total Return** | **23.5%** | ~15.0% |
| **Maximum Drawdown** | **-13.7%** | ~-10.0% |
| **Win Rate** | **~55.0%** | ~52.0% |
| **Average Position Exposure** | **~+0.60x** | +1.00x |

**Parameter Sensitivity & Robustness Sweep (Source-reported):**

| Configuration | Parameters (`vol_target`, `ema_alpha`) | Calmar Ratio | Sharpe Ratio | Robustness Evaluation |
| :--- | :--- | :--- | :--- | :--- |
| **Baseline** | (0.15, 0.15) | **2.14** | **1.92** | Target achieved |
| **Lower Vol Target (-20%)** | (0.12, 0.15) | 1.81 | 1.79 | Robust (Calmar > 1.5) |
| **Higher Vol Target (+20%)** | (0.18, 0.15) | 2.25 | 1.94 | Improved (Calmar > 2.0) |
| **Slower Smoothing (-33%)** | (0.15, 0.10) | 1.50 | 1.44 | Robust (Calmar $\ge$ 1.5) |
| **Faster Smoothing (+33%)** | (0.15, 0.20) | 1.56 | 1.39 | Robust (Calmar > 1.5) |
| **Conservative Stress** | (0.12, 0.10) | 1.26 | 1.32 | Stable (Calmar > 1.25) |
| **Aggressive Stress** | (0.18, 0.20) | 1.65 | 1.40 | Robust (Calmar > 1.5) |

The author reports that the strategy maintained Calmar $> 1.25$ across all parameter permutations and Calmar $> 1.50$ for the vast majority, indicating absence of extreme hyperparameter sensitivity.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Overfitting of Deep Architectures (Source-reported):** The author explicitly tested LSTM and Transformer Encoder architectures with Optuna hyperparameter optimization. A Transformer variant achieved an in-sample Calmar ratio of 4.7, but out-of-sample performance collapsed catastrophically upon minor ($\pm 10\%$) lookback changes, confirming that high-capacity neural sequence models memorized noise rather than structural market mechanics.
2. **Omission of Transaction Costs:** In reality, daily rebalancing between $-1.0\times$ and $+1.5\times$ incurs turnover drag. If EMA smoothing ($\alpha = 0.15$) generates 60–80 portfolio turns per year, an unmodeled 3 bps round-trip cost could shave 1.8%–2.4% from annual returns, reducing the realized Sharpe ratio.
3. **Regime Lag:** The 20-day realized volatility indicator exhibits an inherent ~20-day lag in identifying volatility regime transitions, causing delayed de-leveraging during sharp market regime shifts.

## Falsification plan

To falsify the hypothesis that options market microstructure indicators provide predictive alpha for next-day underlying returns:

1. **Transaction Cost & Slippage Hurdle Test:** Re-run the backtest across 2020–2025 with explicit transaction costs of 3 bps, 5 bps, and 10 bps per trade.
   - `research-defined falsification threshold`: The hypothesis is falsified if net Sharpe ratio drops below 0.70 or net Calmar drops below 0.80 at a realistic 3 bps cost.
2. **Options Feature Ablation Test:** Replace the 15 options features with purely equity-derived price/volume features (RSI, Bollinger Bands, ATR, historical momentum) inside the exact same 4-model ensemble.
   - `research-defined falsification threshold`: The hypothesis of options-specific informational superiority is falsified if the equity-only model achieves equivalent or superior out-of-sample Information Coefficient (IC) and Sharpe ratio ($\Delta \text{Sharpe} \le 0.10$).
3. **Placebo Shuffled-Target Test:** Train the ensemble on 500 permutations of randomly permuted next-day target returns while preserving feature autocorrelation.
   - `research-defined falsification threshold`: The hypothesis is falsified if the real test Sharpe ratio (1.92) does not exceed the 99th percentile of the empirical null distribution ($p \ge 0.01$).
4. **Out-of-Sample Walk-Forward Stability (2025–2026):** Evaluate the frozen model on unobserved data post-September 2025.
   - `research-defined falsification threshold`: The strategy is marked broken if out-of-sample 6-month rolling Sharpe falls below 0.30 or if maximum drawdown exceeds 20.0%.

## Crypto portability

- **Portability Classification:** `adapted / unproven` (Research interpretation).
- **Underlying Market Differences:**
  - The source repository models only US equity ETF options (QQQ). Porting this mechanism to cryptocurrency assets (BTC, ETH, SOL) is strictly unproven.
  - **Option Market Structure:** Crypto options trading is concentrated on Deribit (and emerging platforms like Binance, OKX, Bybit). While Deribit publishes full options chains, Greeks, and DVOL (crypto VIX equivalent), options liquidity on crypto assets is predominantly concentrated in BTC and ETH, with altcoins having negligible options volume.
  - **Dealer Hedging Mechanisms:** Crypto options market makers hedge deltas dynamically using perpetual futures (perps) rather than spot ETF shares, introducing funding rate basis risk and 24/7 liquidation mechanics.
  - **Volatility Level & Skew Dynamics:** BTC and ETH realized volatility averages 50%–90% annualized, which would trigger the equity strategy's kill switch ($\mathrm{RV} > 0.40$) near-permanently.
  - `research-proposed adaptation`: Volatility thresholds must be recalibrated for crypto: target volatility $\sigma_{\text{target}} = 0.50$, crisis kill switch $\mathrm{RV} > 1.10$, medium/high thresholds at $0.70$ and $0.90$.

## Limitations

1. **Single-Asset Concentration:** The strategy is trained and evaluated exclusively on QQQ, leaving it exposed to tech sector concentration and regulatory idiosyncratic risks.
2. **Sample Size:** 1,435 daily bars (~5.7 years) constitutes a modest sample size across only one major market cycle (post-COVID bull, 2022 bear, 2023–2024 AI rally).
3. **Omission of Friction:** The source implementation assumes frictionless execution at mid-market close without modeling bid-ask spread or borrow fees for short positions.
4. **Under-specified Options Chain Filtering:** The exact minimum liquidity cutoffs for options strikes are omitted in the source script and are marked `research-proposed`.

## Implementation status

`not-implemented`. This strategy has not been implemented or verified in NautilusTrader, PyBroker, paper trading, testnet, or live trading.

## Adoption boundary

`research-only`. This record represents normalized external research material for intake review and hypothesis synthesis only. It is `not-approved` for trading, implementation, or deployment.

## Related Wiki records

- `[[bitcoin-options-dealer-gamma-exposure-gex-regime-2026-09-01]]` — Dealer gamma exposure regime modeling in cryptocurrency options.
- `[[crypto-options-volatility-risk-premium-zscore-2026-08-31]]` — Variance risk premium Z-score signals in digital asset options.
- `[[relief-gated-relative-rotation-qqq-dia-interaction-filter-2026-09-02]]` — Cross-sectional ETF rotation and feature-filtering in QQQ.
- `[[conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02]]` — Non-parametric volatility and uncertainty scaling for position sizing.

## Sources

1. Sina Malaekeh, *QQQ Options Alpha Research: Regime-Adaptive Options Microstructure Strategy*, GitHub repository `SMalaekeh/qqq-options-alpha-research`, commit `4ab6181a2284b2a072629eb19dc5e89be26564b5`, November 26, 2025. URL: [https://github.com/SMalaekeh/qqq-options-alpha-research](https://github.com/SMalaekeh/qqq-options-alpha-research).
2. Primary source code: `src/ensemble_model.py` (Ensemble Alpha Model implementation), commit `4ab6181a2284b2a072629eb19dc5e89be26564b5`.
3. Primary source documentation: `docs/strategy_logic.md` (Strategy financial logic), `docs/methodology.md` (Training, validation, and robustness results), `docs/feature_engineering.md` (Features and Greeks calculations), commit `4ab6181a2284b2a072629eb19dc5e89be26564b5`.
4. Academic references cited by primary source:
   - Carr, P., & Wu, L. (2009). "Variance risk premiums." *The Review of Financial Studies*, 22(3), 1311-1341.
   - Bollerslev, T., Tauchen, G., & Zhou, H. (2009). "Expected stock returns and variance risk premia." *The Review of Financial Studies*, 22(11), 4463-4492.
   - Gârleanu, N., Pedersen, L. H., & Poteshman, A. M. (2009). "Demand-based option pricing." *The Review of Financial Studies*, 22(10), 4259-4299.
