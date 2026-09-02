---
schema: strategy-research-record-v1
title: "Information-Driven Bar Sampling and Downstream Directional Alpha Failure on Bitcoin Perpetual Futures: A Frequency-Controlled Empirical Study"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - perpetual-futures
  - information-bars
  - dollar-bars
  - volume-bars
  - volatility-bars
  - renko-bars
  - tick-data
  - machine-learning
  - directional-alpha
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-08-30
sources:
  - "Muhammad Toheed Fayyaz, Abdul Jabbar, Faheem Ahmad Qureshi, and Syed Qaisar Jalil, 'A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars for Cryptocurrency Markets', arXiv:2608.26158v1 [q-fin.TR, cs.LG], August 2026. Stable URL: https://arxiv.org/abs/2608.26158. Full text HTML: https://arxiv.org/html/2608.26158v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Information-Driven Bar Sampling and Downstream Directional Alpha Failure on Bitcoin Perpetual Futures: A Frequency-Controlled Empirical Study

## Provenance

- **Primary Source:** Muhammad Toheed Fayyaz, Abdul Jabbar, Faheem Ahmad Qureshi, and Syed Qaisar Jalil, *"A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars for Cryptocurrency Markets"*, arXiv preprint `arXiv:2608.26158v1 [q-fin.TR, cs.LG]`, August 2026.
- **Identifier:** `arXiv:2608.26158v1`
- **Stable URL:** [https://arxiv.org/abs/2608.26158](https://arxiv.org/abs/2608.26158)
- **Full Text HTML:** [https://arxiv.org/html/2608.26158v1](https://arxiv.org/html/2608.26158v1)
- **Market & Sample:** Binance USDT-margined perpetual futures market for Bitcoin (`BTCUSDT`), covering six full calendar years from January 1, 2020 through December 31, 2025.
- **Data Layers:** Compares raw tick-level executions (`aggTrade` stream: price, quantity, timestamp, buyer/seller aggressor flag) directly against aggregated 1-minute OHLCV bars and fixed calendar baselines (1h, 4h, 6h, 8h, 12h).

## Economic mechanism

### Source-reported

In classical market microstructure literature (e.g., Marcos López de Prado, *Advances in Financial Machine Learning*, 2018), time-sampled calendar bars (e.g., 1-minute, 1-hour) are criticized for oversampling low-activity periods and undersampling high-activity periods. Sampling by information arrival (cumulative dollar volume, trade quantity, price range, or realized volatility) is hypothesized to:
1. Restore statistical normality to return distributions by synchronizing observations with genuine economic information flow;
2. Eliminate serial correlation and variance-ratio deviations;
3. Provide downstream machine learning algorithms with better-conditioned inputs that enhance directional predictability.

The authors test this foundational hypothesis by constructing an adaptive EMA calibration framework that evaluates six distinct information bar families across tick and minute data resolutions, followed by walk-forward training of machine learning classifiers (Random Forest, Gradient Boosting, SVM).

### Research interpretation

This paper provides crucial **negative evidence and falsification of the assumption that information-bar statistical improvements translate into directional trading alpha**:

1. **Orthogonality of Statistical Quality and Alpha:** Improving statistical properties (e.g., lower variance-ratio deviation $|\text{VR}(4)-1| = 0.020$ on tick Renko, or recovering Ljung-Box serial independence $p = 0.510$ on frequency-matched tick volatility bars) exhibits zero correlation with downstream classification AUC. Models trained on information bars achieve near-chance predictive power ($\text{AUC} \in [0.498, 0.596]$), failing to outperform standard calendar baselines (4h calendar $\text{AUC} = 0.589$).
2. **Mean-Reversion Extrapolation & Catastrophic Short Bias:** When standard technical features (RSI, Bollinger Bands, MACD) are applied across information bars in a strongly trending market (Bitcoin appreciated ~14-fold over 2020–2025), walk-forward tree models overfit to localized mean reversion. The models predicted upward moves only $7\%$ of the time despite positive price drift occurring on $52\%$ of bars. This directional miscalibration produced total account liquidations ($-99.9\%$ to $-100.0\%$ cumulative return), which persisted even when transaction fees were artificially set to zero ($-40.2\%$ at zero fees).
3. **Annualization Mirage in High-Frequency Sampling:** On high-frequency bar regimes (e.g., tick volatility bars generating 71,619 trades), the standard annualization multiplier $\sqrt{N_{\text{trades/year}}}$ inflates nominal Sharpe ratios to astronomical levels ($\text{Sharpe} = 19.75$) despite modest directional accuracy ($54.0\%$) and near-chance AUC ($0.563$). This exposes a critical methodological hazard in evaluating high-turnover crypto strategies.

## Signal

### Bar Generation Mechanics

The paper formalizes six information bar constructions under both minute-aggregated and tick-native streams:

1. **Dollar Bars:**
   - *Minute Pipeline:* Sample at bar $n$ when cumulative dollar volume reaches threshold:
     $$S_n^{\text{dv}} = \sum_{m=1}^n c_m \cdot v_m \ge \hat{\theta}_{\text{dv}}$$
   - *Tick Pipeline:* Sample when tick dollar volume reaches threshold:
     $$S_n^{\text{dv}} = \sum_{i=1}^n p_i \cdot q_i \ge \hat{\theta}_{\text{dv}}$$
2. **Volume Bars:**
   - *Minute:* $\sum_{m=1}^n v_m \ge \hat{\theta}_{\text{vol}}$
   - *Tick:* $\sum_{i=1}^n q_i \ge \hat{\theta}_{\text{vol}}$
3. **Volatility Bars:**
   - *Minute:* Cumulative absolute close-to-close return:
     $$S_n^{\text{ctc}} = \sum_{m=1}^n \frac{|c_m - c_{m-1}|}{c_{m-1}} \ge \hat{\theta}_{\text{vol}}$$
   - *Tick:* Cumulative absolute log return:
     $$S_n^{\text{rv}} = \sum_{i=1}^n \left|\log\left(\frac{p_i}{p_{i-1}}\right)\right| \ge \hat{\theta}_{\text{vol}}$$
4. **Range Bars:**
   - Triggers when normalized high-low bar range exceeds threshold:
     $$\delta_n = \frac{H_b^{(n)} - L_b^{(n)}}{p_{\text{open}}} \ge \hat{\theta}_{\text{rng}}$$
5. **Renko Bars:**
   - Triggers when price change from reference price $p_{\text{ref}}$ exceeds threshold:
     $$\delta_i = \frac{|p_i - p_{\text{ref}}|}{p_{\text{ref}}} \ge \hat{\theta}_{\text{renko}}$$
6. **Hybrid Bars:** Dual condition requiring joint attainment of both volume and volatility thresholds.

### Adaptive Threshold Calibration

To prevent non-stationarity from distorting bar frequency across multi-year cycles, thresholds update adaptively via an Exponential Moving Average (EMA) with clipping:
$$\hat{\theta}_{n+1} = (1-\alpha)\hat{\theta}_n + \alpha \cdot \min\left(s_n,\; 2\hat{\theta}_n\right)$$
where $s_n$ is the realized accumulator value at bar completion, $\alpha$ is the smoothing rate, and the $2\hat{\theta}_n$ cap prevents outlier spikes (e.g., flash crashes) from permanently inflating thresholds.

### Downstream Predictive Model & Decision Rule

1. **Feature Vector:** Unified 14-variable state vector extracted per bar, including:
   - Lagged log returns ($k = 1, 2, 3, 5$);
   - Normalized Volume / Dollar Intensity;
   - Relative Strength Index (RSI-14);
   - Moving Average Convergence Divergence (MACD);
   - Bollinger Band percentage $b$;
   - Normalized Average True Range (NATR).
2. **Classifiers:** Random Forest (RF), Gradient Boosting (GB), Support Vector Machine with RBF kernel (SVM).
3. **Decision Rule:**
   $$\text{Signal}_t = \begin{cases} +1 \; (\text{Long}) & \text{if } P(y_{t+1} = 1 \mid \mathbf{x}_t) \ge \tau_{\text{clf}} \\ -1 \; (\text{Short}) & \text{if } P(y_{t+1} = 0 \mid \mathbf{x}_t) \ge \tau_{\text{clf}} \\ 0 \; (\text{Flat}) & \text{otherwise} \end{cases}$$
   where $\tau_{\text{clf}} \in [0.55, 0.75]$.

## Required data

- **Instrument:** Binance BTCUSDT USDT-margined perpetual contract.
- **Data Period:** January 1, 2020 through December 31, 2025.
- **Tick Data Source:** Binance public data archive `aggTrade` records (aggregate trade execution price, quantity, execution timestamp in ms, buyer maker boolean flag).
- **Minute Data Source:** Binance official 1-minute OHLCV perpetual k-lines.
- **Point-in-Time Discipline:** Bars are formed sequentially tick-by-tick or minute-by-minute; features are computed only on completed bars; target is strictly the subsequent bar return.

## Execution assumptions

- **Execution Model:** Order placed at the opening print of bar $t+1$ following completion of bar $t$.
- **Fees:** Binance VIP taker fee tier (assumed at 2–4 bps in the baseline backtest; explicitly compared against a frictionless zero-fee setting).
- **Fill Assumptions:** Full fill at next-bar open; slippage modeled in threshold stress tests.
- **Funding Rates:** Perpetual 8-hour funding intervals (00:00, 08:00, 16:00 UTC) apply to positions held across funding boundary prints.

## Evidence

### Source-reported

All figures, statistical test results, and trading outcomes trace directly to Fayyaz et al. (*arXiv:2608.26158v1*, Tables 20–23, Section VI):

#### 1. Downstream ML Directional Predictability Across Bar Types (Table 21)
Evaluated via out-of-sample walk-forward cross-validation across the entire 6-year period (2020–2025):

- **Calendar Baselines:**
  - `12h`: Best Classifier RF, $\text{AUC} = 0.580$, Accuracy $= 0.654$, Annualized Sharpe $= 2.56$, $N = 243$.
  - `8h`: Best Classifier GB, $\text{AUC} = 0.584$, Accuracy $= 0.573$, Annualized Sharpe $= 1.17$, $N = 614$.
  - `6h`: Best Classifier GB, $\text{AUC} = 0.542$, Accuracy $= 0.491$, Annualized Sharpe $= -0.64$, $N = 967$.
  - `4h`: Best Classifier RF, $\text{AUC} = 0.589$, Accuracy $= 0.562$, Annualized Sharpe $= 1.43$, $N = 883$.
  - `1h`: Best Classifier RF, $\text{AUC} = 0.538$, Accuracy $= 0.539$, Annualized Sharpe $= -0.04$, $N = 7,619$.

- **Information Bars (Minute Pipeline):**
  - `Dollar (Min)`: Best Classifier GB, $\text{AUC} = 0.528$, Accuracy $= 0.526$, Annualized Sharpe $= 0.84$, $N = 1,803$.
  - `Volume (Min)`: Best Classifier RF, $\text{AUC} = 0.537$, Accuracy $= 0.458$, Annualized Sharpe $= -6.10$, $N = 2,837$.
  - `Volatility (Min)`: Best Classifier SVM, $\text{AUC} = 0.498$, Accuracy $= 0.499$, Annualized Sharpe $= -0.49$, $N = 2,444$.
  - `Range (Min)`: Best Classifier RF, $\text{AUC} = 0.518$, Accuracy $= 0.513$, Annualized Sharpe $= -0.43$, $N = 1,781$.
  - `Renko (Min)`: Best Classifier RF, $\text{AUC} = 0.596$, Accuracy $= 0.577$, Annualized Sharpe $= 1.31$, $N = 894$.
  - `Hybrid (Min)`: Best Classifier RF, $\text{AUC} = 0.529$, Accuracy $= 0.502$, Annualized Sharpe $= -0.97$, $N = 1,236$.

- **Information Bars (Tick Pipeline):**
  - `Dollar (Tick)`: Best Classifier GB, $\text{AUC} = 0.500$, Accuracy $= 0.478$, Annualized Sharpe $= -7.67$, $N = 39,743$.
  - `Volume (Tick)`: Best Classifier SVM, $\text{AUC} = 0.528$, Accuracy $= 0.552$, Annualized Sharpe $= 2.14$, $N = 5,506$.
  - `Volatility (Tick)`: Best Classifier RF, $\text{AUC} = 0.563$, Accuracy $= 0.540$, Annualized Sharpe $= 19.75$, $N = 71,619$ *(Authors explicitly note: this extreme Sharpe is an annualization artifact of >70,000 trades, not deployable alpha)*.
  - `Range (Tick)`: Best Classifier RF, $\text{AUC} = 0.547$, Accuracy $= 0.527$, Annualized Sharpe $= -1.53$, $N = 7,378$.
  - `Renko (Tick)`: Best Classifier SVM, $\text{AUC} = 0.508$, Accuracy $= 0.516$, Annualized Sharpe $= -2.56$, $N = 6,500$.
  - `Hybrid (Tick)`: Best Classifier SVM, $\text{AUC} = 0.501$, Accuracy $= 0.509$, Annualized Sharpe $= 0.42$, $N = 2,881$.

#### 2. Trading Execution Backtest Results (Table 22)
Evaluated across confidence thresholds $\tau_{\text{clf}}$:
- **Random Forest ($\tau = 0.55$):** $34,464$ trades, Total Return $= -99.9\%$.
- **Random Forest ($\tau = 0.65$):** $13,559$ trades, Total Return $= -45.3\%$. (With zero transaction costs, return is $-40.2\%$).
- **Gradient Boosting ($\tau = 0.55$):** $39,743$ trades, Total Return $= -100.0\%$.
- **Gradient Boosting ($\tau = 0.75$):** $494$ trades, Total Return $= -32.1\%$.
- **SVM ($\tau = 0.55$):** $5,279$ trades, Total Return $= -73.3\%$.
- **SVM ($\tau = 0.75$):** $212$ trades, Total Return $= -17.3\%$.

#### 3. Frequency-Matched Statistical Robustness (Table 23)
When tick series are coarsened to match the minute pipeline's bar count:
- Coarsened tick dollar bars lead on $6/6$ statistical criteria ($|\text{VR}(4)-1| = 0.029$, Kurtosis $20.83$).
- Coarsened tick volatility bars achieve Ljung-Box independence $p = 0.510$ ($|\text{VR}(4)-1| = 0.020$, Kurtosis $1.79$).

### Independently reproduced

Not independently reproduced. Findings reflect the source-reported experimental results from arXiv:2608.26158v1.

### Negative evidence

- **Orthogonal to Alpha:** The paper conclusively shows that achieving De Prado's statistical quality criteria (normality, variance ratio near 1.0, low autocorrelation) does not improve directional predictability. All information bar models perform near chance ($\text{AUC} \approx 0.50$–$0.56$).
- **Catastrophic Short Bias:** Walk-forward models using technical features developed an extreme short bias (predicting "up" only 7% of the time), resulting in complete equity destruction ($-99.9\%$ to $-100\%$) during Bitcoin's multi-year bull market.
- **Not a Friction Artefact:** Even after eliminating all trading fees (zero transaction cost), the strategy lost $-40.2\%$ at $\tau = 0.65$, proving that losses stem from fundamentally inverted directional predictions rather than fee churn.
- **Annualization Mirage:** Sharpe ratios calculated on high-frequency information bars (e.g., tick volatility Sharpe 19.75 on 71,619 trades) are mathematical scaling distortions that collapse entirely under realistic equity-curve accounting.

## Falsification plan

1. **Native Order Flow Feature Injection:** Test whether replacing generic technical indicators with tick-native order flow features (cumulative volume delta, bid-ask trade imbalance, trade size entropy, cancel-to-trade ratio) raises out-of-sample AUC above 0.60. If AUC remains below 0.55, confirm that information bars do not yield directional edge even with microstructural features.
2. **Trend-Regime Conditioning:** Enforce a hard trend filter (e.g., 200-period EMA on daily bars) forbidding short positions when price is above the trend filter. If total return remains negative across information bar types, falsify the hypothesis that short-bias alone caused strategy collapse.
3. **Cross-Asset Perpetuals Validation:** Replicate the pipeline on Ethereum (`ETHUSDT`) and Solana (`SOLUSDT`) perpetual futures. If directional AUC similarly fails to exceed calendar baselines, confirm that the findings are structural across digital assets.
4. **Funding-Rate Arbitraged Execution:** Incorporate continuous perpetual funding rate payments into bar return calculation. Assess whether net-of-funding returns further degrade performance.

## Crypto portability

**Direct.** The study is conducted natively on Binance BTCUSDT USDT-margined perpetual futures using 6 years of tick and 1-minute exchange data. 

Relevant market dynamics evaluated:
- **Perpetual Contract Architecture:** Operates directly on the standard crypto trading instrument (USDT perpetual swap).
- **24/7 Liquidity Flow:** Information bars dynamically adjust to crypto's non-stop trading cycle, compressing low-volume Asian night sessions and expanding during US macro announcements.
- **Aggregated Trade Idiosyncrasies:** Identifies that Binance `aggTrade` compression merges simultaneous fills into single records, requiring explicit handling of trade counts and timestamps.

## Limitations

- **Generic Technical Indicator Bias:** The downstream ML benchmark utilized standard technical indicators rather than order-book depth or microstructural alpha signals, which may have contributed to poor classifier performance.
- **Single Underlying Asset:** Evaluated exclusively on BTCUSDT; altcoin perpetuals with lower liquidity may exhibit different dynamics.
- **Asymmetric Class Distribution:** Bull-market drift in Bitcoin created label imbalance that simple tree models failed to accommodate without explicit class weighting or focal loss.
- **Execution Latency:** High-frequency tick bars (70,000+ trades) require low-latency co-located execution infrastructure that is not captured in bar-open fill models.

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live environments has been conducted.

## Adoption boundary

`research-only`. This capture serves as a normalized research record and cautionary empirical benchmark against naive information-bar deployment. It does not constitute an approved strategy, does not guarantee profitability, and explicitly documents strategy failure modes.

## Related Wiki records

- `[[quant/information-bars-dollar-volume-volatility-de-prado]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/crypto-perpetual-futures-market-microstructure]]`

## Sources

1. Muhammad Toheed Fayyaz, Abdul Jabbar, Faheem Ahmad Qureshi, and Syed Qaisar Jalil, *"A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars for Cryptocurrency Markets"*, arXiv preprint `arXiv:2608.26158v1 [q-fin.TR, cs.LG]`, August 2026. DOI: [10.48550/arXiv.2608.26158](https://doi.org/10.48550/arXiv.2608.26158). Stable URL: [https://arxiv.org/abs/2608.26158](https://arxiv.org/abs/2608.26158). Full text HTML: [https://arxiv.org/html/2608.26158v1](https://arxiv.org/html/2608.26158v1).
