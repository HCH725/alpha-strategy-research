---
schema: strategy-research-record-v1
title: Hourly Bitcoin Machine-Learning Return Forecasting with Cost-Aware Execution Filtering
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - machine-learning
  - xgboost
  - walk-forward
  - transaction-costs
  - execution-filter
  - intraday
status: research-only
confidence: high
source_as_of: 2026-05-31
sources:
  - https://arxiv.org/abs/2606.00060
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hourly Bitcoin Machine-Learning Return Forecasting with Cost-Aware Execution Filtering

## Provenance

Primary source:
- Andrei Bysik and Robert Ślepaczuk. "Machine Learning-Based Bitcoin Trading Under Transaction Costs: Evidence From Walk-Forward Forecasting." arXiv:2606.00060v1 [q-fin.CP / q-fin.ST], May 31, 2026. Quantitative Finance Research Group, Faculty of Economic Sciences, University of Warsaw.
- arXiv URL: https://arxiv.org/abs/2606.00060
- DOI: https://doi.org/10.48550/arXiv.2606.00060

Sample and evaluation protocol:
- **Data Source:** Hourly OHLCV data for BTC/USDT USD-margined perpetual futures from Binance public API.
- **Sample Period:** 1 December 2017 to 1 January 2026 (70,872 hourly observations; 70,128 effective walk-forward evaluation hours net of December 2017 burn-in).
- **Validation Protocol:** 27 sequential non-anchored rolling walk-forward folds (12-month train, 3-month validation, 3-month test).
- **Models Compared:** XGBoost (tree ensemble), LSTM (gated recurrent network), iTransformer (inverted attention multivariate transformer).
- **Feature Tiers:** OHLCV (raw price/volume), OHLCV+TA (rolling technical indicators selected by Spearman correlation), OHLCV+TA+EGARCH (augmented with conditional volatility regime features).

## Economic mechanism

### Source-reported

Bysik and Ślepaczuk (2026) investigate the "prediction-to-trading gap" in high-frequency cryptocurrency markets: statistical predictability does not automatically translate into profitable trading because frequent position switching incurs heavy transaction friction.

1. **Failure of Naive Sign-Based Execution:** Converting 1-hour return forecasts directly into positions ($\text{pos}_t = \text{sign}(\hat{r}_{t+1})$) generates extreme turnover (over 10,000–18,000 trades over the 2018–2026 evaluation period). When conservative proportional transaction costs ($c = 10\text{ bps}$ per unit turnover) are applied, all naive machine-learning strategies collapse into persistent losses (gross annual returns drop from $+73.5\%$ to $-64.0\%$ for XGBoost, and $+181.8\%$ to $-98.6\%$ for iTransformer).
2. **Cost-Aware Execution Filter:** Introducing an execution threshold proportional to transaction costs:
   $$|\hat{r}_{t+1}| > \lambda \cdot c \cdot |\text{pos}_t^* - \text{pos}_{t-1}|$$
   prevents trades when forecast magnitude is insufficient to overcome friction. Setting $\lambda = 2.0$ cuts turnover by over an order of magnitude, suppresses noisy churn around zero, and restores positive net-of-cost performance ($\text{ARC} = 65.4\%$, Sharpe $> 1.0$ for long-only XGBoost).
3. **Architecture and Feature Dynamics:** Tabular gradient boosting (XGBoost) descriptively outperforms neural sequence models (LSTM, iTransformer) in the cost-aware setting, while technical indicators provide incremental gain and EGARCH volatility features provide mixed/fragile benefits.

### Research interpretation

The hypothesis is that **hourly Bitcoin returns contain weak, non-linear predictive structure that is economically exploitable only when filtered through a cost-aware execution hurdle that penalizes low-magnitude forecasts**:

1. **Signal Structure:** Price momentum, volatility compression, and intraday volume imbalances provide short-lived statistical predictability at the 1-hour horizon.
2. **Turnover Erosion Channel:** Because noise dominates small hourly predictions, unconstrained sign trading triggers trades on near-zero forecast fluctuations where expected gross return is less than the 10 bps round-trip friction.
3. **Selective Execution:** By enforcing a minimum forecast magnitude hurdle (e.g. $0.20\%$ for 1-unit position entry/exit, $0.40\%$ for 2-unit long/short flip), the strategy acts only on high-conviction signals, transforming a loss-making high-turnover strategy into a disciplined, low-turnover trend/momentum capture engine.

## Signal

Normalized model specification and cost-aware execution rule:

1. **Forecast Generation:**
   - At each hour $t$, compute normalized feature vector $X_t$ containing OHLCV, 10 selected rolling technical indicators (RSI, ATR, EMA, SMA, MACD over lookback windows $w \in \{3, 6, 12, 24, 48, 72, 168, 336\}$ hours), and EGARCH conditional variance features.
   - Generate point prediction $\hat{r}_{t+1}$ for next-hour log return $r_{t+1} = \ln(P_{t+1}/P_t)$ using walk-forward retrained XGBoost regression model.

2. **Target Sign Position ($\text{pos}_t^*$):**
   - Long-only mode: $\text{pos}_t^* = 1$ if $\hat{r}_{t+1} > 0$, else $\text{pos}_t^* = 0$.
   - Long-short mode: $\text{pos}_t^* = 1$ if $\hat{r}_{t+1} > 0$, else $\text{pos}_t^* = -1$.

3. **Cost-Aware Execution Filter:**
   - Let $\text{pos}_{t-1}$ be the active position at hour $t$.
   - Update position if and only if:
     $$|\hat{r}_{t+1}| > \lambda \cdot c \cdot |\text{pos}_t^* - \text{pos}_{t-1}|$$
     where $c = 0.0010$ (10 bps) and $\lambda = 2.0$.
   - Position decision:
     $$\text{pos}_t = \begin{cases} \text{pos}_t^* & \text{if } |\hat{r}_{t+1}| > \lambda \cdot c \cdot |\text{pos}_t^* - \text{pos}_{t-1}| \\ \text{pos}_{t-1} & \text{otherwise} \end{cases}$$
   - Execution threshold values:
     - Long-only entry (from 0 to 1) or exit (from 1 to 0): $|\Delta \text{pos}| = 1 \implies \text{threshold} = 2.0 \times 0.0010 \times 1 = 0.0020$ ($0.20\%$).
     - Long-short reversal (from -1 to +1 or +1 to -1): $|\Delta \text{pos}| = 2 \implies \text{threshold} = 2.0 \times 0.0010 \times 2 = 0.0040$ ($0.40\%$).

4. **Rebalancing Frequency:** Hourly on bar close.

## Required data

- **Universe:** BTC/USDT USD-margined perpetual futures (or spot).
- **Venue:** Binance (or equivalent liquid centralized exchange).
- **Timeframe:** 1-hour completed bars (OHLCV).
- **Feature Pipeline:**
  - Raw Open, High, Low, Close, Volume.
  - Rolling Technical Indicators computed over windows $w \in \{3, 6, 12, 24, 48, 72, 168, 336\}$ hours.
  - EGARCH(p,q) fitted recursively on training segment with Student-$t$ innovations.
- **Timestamp Integrity:** Strictly causal feature construction with no forward-looking data leakage.

## Execution assumptions

- **Timing:** Orders executed at the open of hour $t+1$ following model inference on hour $t$ close.
- **Transaction Costs:** Proportional cost $c = 10\text{ bps}$ ($0.0010$) per unit of turnover (accounting for 2–4 bps exchange fee + bid-ask spread crossing + slippage).
- **Order Type:** Market on open / aggressive taker fill.
- **Leverage:** 1x notional (unlevered).

## Evidence

### Source-reported

All empirical figures below are directly reported by Andrei Bysik and Robert Ślepaczuk (arXiv:2606.00060v1, 2026) across the consolidated 2018–2026 out-of-sample walk-forward evaluation (70,128 test hours, 27 folds):

1. **Impact of Transaction Costs on Naive Sign-Based ML Strategies (Table 4):**
   - **Zero Cost (Frictionless):**
     - XGBoost (Long-Only, OHLCV+TA+EGARCH, MSE loss): Annualized Return $\text{ARC} = 73.50\%$, $\text{Sharpe} = 1.18$, Trades = $10,619$.
     - iTransformer (Long-Short, OHLCV+TA+EGARCH, MSE loss): $\text{ARC} = 181.76\%$, $\text{Sharpe} = 1.48$, Trades = $18,485$.
     - LSTM (Long-Only): $\text{ARC} = 65.59\%$, $\text{Sharpe} = 1.09$, Trades = $9,864$.
   - **With 10 bps Transaction Costs ($c = 0.0010$):**
     - XGBoost (Long-Only): $\text{ARC} = -64.00\%$, $\text{Sharpe} = -1.03$, $\text{Max Drawdown} = -99.98\%$.
     - iTransformer (Long-Short): $\text{ARC} = -98.62\%$, $\text{Sharpe} = -1.97$, $\text{Max Drawdown} = -100.00\%$.
     - LSTM (Long-Only): $\text{ARC} = -63.78\%$, $\text{Sharpe} = -1.02$, $\text{Max Drawdown} = -99.97\%$.
     - 24h Momentum Benchmark (Long-Only): Gross $\text{ARC} = 56.40\%$ drops to net $\text{ARC} = -43.20\%$ (Trades = $2,279$).
   - **Statistical Test of Cost Drag (Table 5):**
     - Paired circular block-bootstrap test (168-hour blocks, 10,000 replications): Mean hourly cost drag equals $+4.01\text{ bps/hour}$ for XGBoost LO and $+6.06\text{ bps/hour}$ for iTransformer LS. All pairwise tests reject $H_0$ at $p < 0.001$ after Holm adjustment.

2. **Restoration of Performance via Cost-Aware Execution Filter ($\lambda = 2.0$, Table 6):**
   - **XGBoost Long-Only (OHLCV+TA+EGARCH, MSE loss, 10 bps costs):**
     - *Loss-Best Selector:* $\text{ARC} = 65.40\%$, $\text{ASD} = 56.45\%$, $\text{Sharpe Ratio} = 1.08$, $\text{Max Drawdown} = -68.32\%$, $\text{Max Loss Duration} = 2.50\text{ years}$, Trades = $251$ (turnover cut by $97.6\%$).
     - *IC-Best Selector:* $\text{ARC} = 54.34\%$, $\text{ASD} = 56.32\%$, $\text{Sharpe Ratio} = 0.94$, $\text{Max Drawdown} = -73.20\%$, Trades = $261$.
     - *$IR^{**}$-Best Selector:* $\text{ARC} = 55.43\%$, $\text{ASD} = 54.67\%$, $\text{Sharpe Ratio} = 0.97$, $\text{Max Drawdown} = -70.43\%$, Trades = $239$.
   - **Statistical Test of Cost-Aware Filter Gain (Table 7):**
     - Circular block-bootstrap test (168-hour blocks): Mean return difference (Cost-Aware minus Baseline) equals $+3.64\text{ bps/hour}$ ($p < 0.001$, Holm-adjusted reject) for XGBoost LO.

3. **Feature Tier Comparison:**
   - Adding Technical Indicators (OHLCV+TA) systematically improves performance over raw OHLCV.
   - Adding EGARCH features yields marginal/fragile incremental improvements that are not statistically dominant across all bootstrap tests.

4. **Architecture Comparison:**
   - In the cost-aware long-only setting, XGBoost ($\text{ARC} = 65.40\%$, $\text{SR} = 1.08$) descriptively outperforms LSTM ($\text{ARC} = 42.15\%$, $\text{SR} = 0.76$) and iTransformer ($\text{ARC} = 38.90\%$, $\text{SR} = 0.71$).
   - However, paired bootstrap tests with Holm correction show that differences between model architectures do not reach formal statistical significance after multiple testing adjustments.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Long-Short Mode Failure:** Under cost-aware execution, long-short ML models achieve only modest positive returns ($\text{ARC} \approx 12\text{--}24\%$, $\text{Sharpe} \approx 0.2\text{--}0.4$) and significantly underperform passive Buy-and-Hold ($\text{ARC} = 54.20\%$, $\text{Sharpe} = 0.86$). Shorting Bitcoin at hourly horizons generates high whipsaw losses.
- **Passive Benchmark Dominance:** Formal bootstrap tests comparing the best long-only XGBoost strategy against Buy-and-Hold fail to reject the null hypothesis of equal Sharpe ratios, due to high variance across market cycles.
- **Regime Fragility:** Fold-level decomposition reveals that performance is highly concentrated in strong trend regimes (2020–2021 bull market) while experiencing extended drawdowns during choppy sideways consolidation phases (e.g. 2018–2019 bear market).

## Falsification plan

1. **Out-of-Sample Walk-Forward Extension (2026+):** Apply the trained XGBoost model and cost-aware filter to live/forward 2026 data. The strategy is falsified if net-of-cost Sharpe ratio drops below 0.0 over 12 consecutive months.
2. **Transaction Cost Sensitivity Threshold:** Increment cost parameter $c$ from 10 bps to 15, 20, and 25 bps. If the strategy's Sharpe ratio turns negative at $c \le 15\text{ bps}$, the edge is too fragile for live execution.
3. **Cross-Asset Replication:** Test identical walk-forward pipeline on ETH/USDT and SOL/USDT. If the cost-aware execution filter fails to produce positive net returns on other major crypto pairs, the Bitcoin result is an artifact of asset-specific trending behavior.

## Crypto portability

direct

The strategy is developed, backtested, and validated directly on Binance BTC/USDT perpetual futures hourly market data.

## Limitations

- **Not independently reproduced.**
- **Single-Asset Focus:** Primary empirical results focus exclusively on BTC/USDT.
- **Execution Model Simplification:** Assumes fixed 10 bps proportional fee rather than dynamic order-book depth simulation, variable spreads, or maker rebate models.
- **High Drawdown:** Best performing long-only model experiences a maximum drawdown of $-68.32\%$ with a loss duration of 2.5 years, requiring external portfolio-level risk overlays.

## Implementation status

No implementation in our research stack has been completed.

## Adoption boundary

Research material only.

A record being present in this repository does NOT mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `[[quant/crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]]`
- `[[quant/crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]]`
- `[[quant/machine-learning-knn_ohlcv-2026-08-31]]`
- `[[quant/crypto-cross-sectional-elastic-net-ctrend-2026-08-31]]`
- `[[quant/crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31]]`

## Sources

1. Bysik, Andrei, and Robert Ślepaczuk. "Machine Learning-Based Bitcoin Trading Under Transaction Costs: Evidence From Walk-Forward Forecasting." arXiv:2606.00060v1 [q-fin.CP], May 31, 2026.
   - URL: https://arxiv.org/abs/2606.00060
   - Key tables & figures: Table 1 (literature positioning), Table 2 (descriptive statistics: 70,872 hours, std 0.7278%, kurtosis 42.6), Section 4.1 (Equations 4–7: cost-aware execution filter), Section 4.2 (walk-forward design: 27 folds, 12m train, 3m val, 3m test), Table 4 (zero-cost vs 10 bps cost results: XGBoost LO +73.50% vs -64.00%), Table 5 (circular block bootstrap tests of cost drag), Table 6 (cost-aware filter results: XGBoost LO ARC 65.40%, Sharpe 1.08, trades 251), Table 7 (cost-aware bootstrap improvements).
2. Binance USD-M Futures Data: Historical hourly OHLCV archives: https://data.binance.vision
