---
schema: strategy-research-record-v1
title: Crypto Perpetual LOB Explainable CatBoost GMADL Microstructure Alpha
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - market-microstructure
  - machine-learning
  - catboost
  - order-flow-imbalance
  - high-frequency
  - adverse-selection
status: research-only
confidence: high
source_as_of: 2025-10
sources:
  - "Bartosz Bieganowski and Robert Ślepaczuk, 'Explainable Patterns in Cryptocurrency Microstructure', arXiv:2602.00776v1 [q-fin.TR], January 2026. DOI: 10.48550/arXiv.2602.00776. https://arxiv.org/abs/2602.00776"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual LOB Explainable CatBoost GMADL Microstructure Alpha

## Provenance

- **Primary Source:** Bartosz Bieganowski and Robert Ślepaczuk (University of Warsaw, Department of Quantitative Finance), "Explainable Patterns in Cryptocurrency Microstructure", arXiv:2602.00776v1 [q-fin.TR], January 2026. DOI: [10.48550/arXiv.2602.00776](https://doi.org/10.48550/arXiv.2602.00776).
- **Universe & Sample:** Binance Futures perpetual contracts across five digital assets spanning different market capitalization tiers (BTC, LTC, ETC, ENJ, ROSE), recorded at 1-second frequency from January 1, 2022 to October 12, 2025.
- **Dataset Composition:** High-frequency synchronized 1-second top-of-book limit-order-book quotes and trade records, including the extreme market dislocation of the October 10, 2025 flash crash ($19B liquidation event).
- **Evaluation Framework:** Rolling time-series cross-validation with purged gaps, inner-fold Bayesian hyperparameter optimization via Optuna (Tree-structured Parzen Estimator), and TreeSHAP explainability on outer held-out folds.

## Economic mechanism

### Source-reported

Bieganowski and Ślepaczuk (2026) investigate whether short-horizon return predictability in cryptocurrency limit order books admits a universal, portable representation across assets with heterogeneous liquidity, capitalization, and volatility.

Key source-reported empirical findings:
1. **Universal Feature Importance & SHAP Structures:** Across large-cap (BTC) down to long-tail altcoins (ROSE), the same compact feature library dominates predictive power:
   - **Order Flow Imbalance (OFI):** Exhibits a monotone relationship with future 3-second returns, displaying concavity at extreme imbalances (diminishing incremental price impact).
   - **Bid-Ask Spread Width:** Wider spreads correlate with attenuated directional predictability and higher adverse selection risk.
   - **VWAP-to-Mid Deviations:** Deviations of buy and sell trade VWAPs from mid-price reflect short-lived liquidity-taking pressure followed by mean-reverting depth replenishment.
2. **Tick Size Modulation & Microprice:** Imbalance effect magnitude increases with relative tick size. In coarse-tick instruments, top-of-book depth asymmetry maps directly into discrete uptick/downtick probabilities (evidenced by spot W/USDT order book imbalance predicting continuous fine-ticked futures mid-price location with correlation $c=0.94$).
3. **Execution Asymmetry & Flash Crash Dynamics:**
   - **Taker Execution:** Marking inventory pessimistically (longs to bid, shorts to ask) produces statistically significant outperformance ($p < 0.05$) on altcoins (ETC, ENJ, ROSE) under realistic taker fee modeling.
   - **Maker Execution:** While capturing steady spread in quiescent markets, passive limit-order provision suffers severe adverse selection (picking-off risk) during sharp dislocations (e.g. October 10, 2025 flash crash), resulting in severe drawdowns, whereas active taker execution captures rapid directional momentum.

### Research interpretation

The falsifiable thesis is a **scale-invariant microstructure flow-pressure and adverse-selection model**:
1. **Microstructure Price Formation Channel:** When normalized into scale-invariant relative quantities (spread-to-mid, volume imbalance ratios, VWAP-to-mid), limit-order book pressure transmits into short-horizon price moves identically across asset market caps.
2. **Direction-Aware Loss Alignment (GMADL):** Standard MSE loss overweights trivial high-frequency noise around zero. Training with direction-aware objectives (GMADL) aligns model capacity to predict high-amplitude directional dislocations where trading edge exceeds the bid-ask spread and taker fees.
3. **Regime-Dependent Execution Selection:** Active taker execution is optimal during high-conviction order flow imbalances and liquidation cascades where adverse selection makes passive market making unprofitable.

## Signal

1. **Feature Engineering (1-Second Synchronized Cadence):**
   - **Spread-to-Mid:** $\text{Spread}_t = \frac{P_{\text{ask},1,t} - P_{\text{bid},1,t}}{P_{\text{mid},t}}$.
   - **Top-of-Book Volume Imbalance:** $\text{Imbalance}_t = \frac{V_{\text{bid},1,t} - V_{\text{ask},1,t}}{V_{\text{bid},1,t} + V_{\text{ask},1,t}}$.
   - **Signed Order Flow:** Net trade volume over rolling 1s–5s windows: $\text{SOF}_t = V_{\text{buy},t} - V_{\text{sell},t}$.
   - **VWAP-to-Mid Deviations:**
     $$\Delta\text{VWAP}_{\text{buy},t} = \frac{\text{VWAP}_{\text{buy},t} - P_{\text{mid},t}}{P_{\text{mid},t}}, \quad \Delta\text{VWAP}_{\text{sell},t} = \frac{\text{VWAP}_{\text{sell},t} - P_{\text{mid},t}}{P_{\text{mid},t}}$$
2. **Model Architecture & Objective:**
   - CatBoost Gradient Boosted Decision Trees trained to forecast the 3-second log mid-price return $r_{t \to t+3s} = \ln(P_{\text{mid}, t+3s} / P_{\text{mid}, t})$.
   - Model selection guided by Generalized Mean-Absolute Directional Loss (GMADL):
     $$\text{GMADL} = \frac{1}{N} \sum_{i=1}^N |r_i - \hat{r}_i| \cdot \left[1 - \text{sign}(r_i \cdot \hat{r}_i)\right]$$
3. **Execution Decision Rule:**
   - Symmetric confidence threshold $\theta > 0$.
   - If $\hat{r}_{t \to t+3s} > \theta$: Submit market buy order at best ask.
   - If $\hat{r}_{t \to t+3s} < -\theta$: Submit market sell order at best bid.
   - If $|\hat{r}_{t \to t+3s}| \le \theta$: Maintain neutral position / do not trade.
   - Position holding duration: Event-driven (exited on signal flip or after 3 seconds).

## Required data

- **Instruments:** Liquid Binance USDT perpetual futures contracts (BTC, LTC, ETC, ENJ, ROSE).
- **LOB Data:** 1-second top-of-book best bid/ask prices and level-1 depth.
- **Trade Feed:** Millisecond tick trades with price, quantity, timestamp, and aggressor side.
- **Derived Series:** Rolling 1-second buy/sell VWAPs and net trade volume imbalance.

## Execution assumptions

- **Timing:** 1-second discrete decision steps predicting $t+3\text{s}$ mid-price returns.
- **Order Types:** Aggressive market orders (taker) or passive limit orders placed at top of book (maker).
- **Pessimistic Inventory Marking:** In the backtest, long positions are marked to bid price and short positions to ask price (unrealized PnL penalized by full bid-ask spread).
- **Fees & Slippage:** Taker fees modeled; zero latency idealized assumption (upper bound on fastest execution speed).

## Evidence

### Source-reported

All figures below are directly reported by Bieganowski and Ślepaczuk (arXiv:2602.00776v1, January 2026):
- **Universal SHAP Importance:** Feature importance rankings ($S_j$) for OFI, spread, and VWAP deviation are highly correlated across BTC, LTC, ETC, ENJ, and ROSE, demonstrating cross-asset structural invariance.
- **Taker Strategy Statistical Significance (t-test vs Buy-and-Hold):**
  - ETC, ENJ, and ROSE taker strategies achieve statistically significant outperformance at the 5% level ($p < 0.05$).
  - BTC and LTC taker strategies do not reach statistical significance ($p \ge 0.05$) under taker fees due to tighter spreads and higher competitive efficiency.
- **Maker Strategy Statistical Significance:**
  - Maker strategies fail to achieve statistically significant outperformance ($p > 0.05$ across all 5 assets) due to severe adverse selection drag.
- **October 10, 2025 Flash Crash ($19B liquidation event):**
  - Taker strategy achieved windfall profits across altcoins by detecting sudden selling pressure and shorting ahead of cascade continuation.
  - Maker strategy suffered catastrophic picking-off losses as resting bids were filled by toxic flow before quote cancellation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Pure maker execution using the 1-second CatBoost signal exhibits negative skew and severe tail losses during market crashes, failing to reject the null hypothesis of zero excess return.
- Taker strategy edge on mega-cap contracts (BTCUSDT) is consumed by taker fees at 1-second cadence, showing statistical significance primarily on higher-spread altcoin perpetuals.

## Falsification plan

1. **Latency Sensitivity Test:** Introduce realistic network jitter (50ms–200ms API latency) and exchange queue simulation. If net Sharpe ratio drops below 0 on ETC/ENJ/ROSE under 100ms latency, reject live high-frequency feasibility.
2. **Fee Schedule Stress Test:** Test taker strategy across VIP fee tiers (from VIP 0 at 5 bps to VIP 9 at 1.5 bps). If strategy requires sub-2 bps taker fees to break even, classify as institutional-only.
3. **Out-of-Sample Horizon Decay:** Evaluate CatBoost GMADL models trained on pre-2025 data across post-2025 regimes. If out-of-fold directional accuracy drops below 51.5%, reject structural feature invariance.

## Crypto portability

**Direct**: Tested directly on Binance perpetual futures contracts across 2022–2025 tick-level order book and trade datasets.

## Limitations

- **Not independently reproduced.**
- **Latency Modeling:** Source backtest does not explicitly model sub-second network latency and queuing dynamics.
- **Fee Sensitivity:** High-frequency taker turnover requires low fee tiers to capture net alpha on large-cap contracts.
- **Capacity:** Signal operates at 1-second to 3-second horizon; position capacity is bounded by top-of-book depth.

## Implementation status

Not implemented. No PyBroker, NautilusTrader, paper, testnet, or live deployment.

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for live trading.

## Related Wiki records

- `[[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`
- `[[quant/contrarian-market-making-fill-probability-order-flow-2026-09-01]]`
- `[[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]]`

## Sources

1. Bartosz Bieganowski and Robert Ślepaczuk, "Explainable Patterns in Cryptocurrency Microstructure", arXiv:2602.00776v1 [q-fin.TR], January 2026. DOI: [10.48550/arXiv.2602.00776](https://doi.org/10.48550/arXiv.2602.00776). https://arxiv.org/abs/2602.00776.
2. Complete text and figures: https://arxiv.org/html/2602.00776v1.
