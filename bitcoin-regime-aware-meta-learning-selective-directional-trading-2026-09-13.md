---
schema: strategy-research-record-v1
title: "Bitcoin Regime-Aware Meta-Learning for Selective Directional Trading"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - meta-learning
  - regime-gating
  - selective-classification
  - directional-trading
  - ensemble
status: research-only
confidence: medium
source_as_of: 2026-09-06
sources:
  - "https://github.com/manavmax/Bitcoin-Alpha-System (commit 4bf76065f79aaaff3cc740a28b2bfe61f91b02d7, 2026-09-06)"
  - "Manav Sharma, 'A Regime-Aware Meta-Learning Framework for Selective Directional Trading in Cryptocurrency Markets', IEEE ICIPTM 2026. DOI: 10.1109/ICIPTM69057.2026.11466047"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Regime-Aware Meta-Learning for Selective Directional Trading

## Provenance

- **Primary Repository:** `https://github.com/manavmax/Bitcoin-Alpha-System`
- **Full Commit SHA:** `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7` (main branch as of September 6, 2026)
- **Associated Conference Paper:** Manav Sharma, *"A Regime-Aware Meta-Learning Framework for Selective Directional Trading in Cryptocurrency Markets"*, IEEE 2026 International Conference on Information Processing and Technology Management (ICIPTM 2026), DOI: [10.1109/ICIPTM69057.2026.11466047](https://doi.org/10.1109/ICIPTM69057.2026.11466047).
- **Author:** Manav Sharma (first author)
- **License Status:** Unlicensed / no formal license selected (`source-reported` in README: *"No license has been selected yet"*).
- **Primary Source Code & Artifact Inspection:** Directly cloned and inspected repository structure, scripts, and evaluation data:
  - `model_1_price_dynamics` (`src/prepare_data.py`, `src/train_lstm.py`, `src/train_tcn.py`, `src/train_nbeats.py`, `src/model1_ensemble.py`)
  - `model_2_volatility_risk` (`src/train_garch.py`, `src/train_volatility_lstm.py`, `src/model2_ensemble.py`)
  - `model_3_derivatives_flow` (`src/fetch_binance_long_short_ratio.py`, `src/fetch_coinalyze.py`, `src/train_model3_cnn_lstm.py`, `src/train_model3_tcn.py`)
  - `model_4_onchain_fundamentals` (`src/train_onchain_transformer.py`)
  - `model_6_macro_liquidity` (`src/fetch_fred_data.py`, `src/train_macro_lstm.py`, `src/train_macro_tree.py`, `src/model6_ensemble.py`)
  - `model8_meta_classifier` (`src/train_model8A.py`, `src/train_model8B.py`, `src/regime_aware_gating.py`, `src/model8_final.py`, `reports/generate_daily_report.py`)
  - Committed results data: `model8_meta_classifier/results/model8_regime_gated.csv` (2,919 daily samples, 2018–2025), `model8_confidence_curve.csv`, `model8_final_signal.csv`, and benchmark price data `data/raw/btc_price_daily.csv` (1,000 daily bars, 2023–2026).
- **Repository Deduplication Audit:** Full text regex and string search across all existing records in `alpha-strategy-research` confirmed zero matches for `Bitcoin-Alpha-System`, `manavmax`, `10.1109/ICIPTM69057.2026.11466047`, or author `Manav Sharma`. Related crypto records (`raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04.md`, `two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05.md`) evaluate different mechanisms.

## Economic mechanism

### Source-reported

Cryptocurrency markets are characterized by severe non-stationarity, regime instability, and low signal-to-noise ratios. Standard machine learning models trained to output directional bets on every timestamp suffer from poor generalizability and severe drawdowns during chaotic, noisy, or illiquid market conditions. The author proposes a meta-learning framework with an abstention mechanic: rather than forcing a directional guess on every daily candle, the system first identifies whether the current market environment warrants active trading based on latent volatility and macroeconomic liquidity regimes. A two-stage meta-classifier executes directional trades (LONG or SHORT) only when confidence exceeds a regime-conditioned threshold; otherwise, it abstains from the market (`NO_TRADE`).

### Research interpretation

The strategy formalizes selective classification (rejection option / Chow's rule) within a macro-micro hierarchical architecture for Bitcoin. The core hypothesis is that directional edge in cryptocurrency markets is temporally sparse and heavily clustered by macro-volatility states:
1. **Low Volatility, Risk-On Macro:** Trending persistence is highest and retail whipsaw risk is muted. Lower confidence thresholds ($\tau = 0.55$) are permitted.
2. **High Volatility, Risk-Off Macro:** Adverse selection, cascading liquidations, and violent mean-reversions dominate. Stricter confidence thresholds ($\tau = 0.70$) or outright abstention are required.

The architecture decomposes into:
- **Base Feature Encoders (Models 1–6):** Domain-specific representations extracting price dynamics (LSTM/TCN/N-BEATS), volatility regime (GARCH/LSTM), derivatives positioning (Binance long/short ratio, Coinalyze open interest, funding rates via CNN-LSTM/TCN), on-chain activity (Transformer), and macro liquidity (FRED yield curve, liquidity indicators).
- **Stage 1 Regime Selector (Model 8A):** An XGBoost classifier that maps volatility regime, macro regime, and macro signal into a binary tradability decision $T_t \in \{0, 1\}$.
- **Stage 2 Directional Classifier (Model 8B):** An XGBoost classifier trained on base signal features that outputs directional probabilities $P(\text{Up})$ and $P(\text{Down})$.
- **Confidence Gating:** Computes prediction confidence $C_t = \max(P(\text{Up}), P(\text{Down}))$ and abstains unless $T_t = 1$ and $C_t \ge \tau(\text{vol\_regime}_t, \text{macro\_regime}_t)$.

## Signal

### Formation timestamp

- Signal formed daily at 00:00 UTC upon close of the daily BTC candle (`source-reported`).
- Execution assumed on the next bar / next-day open (`source-reported` in backtest logic via `position.shift(1)`).
- Timezone: UTC.

### Lookback

- Base model inputs: Trailing sequence windows of 14 to 60 days depending on module (e.g. 30-day lookback for LSTM/TCN price sequences, rolling GARCH conditional variance, 30-day rolling macro indicators).
- Model 8A/8B inference: Uses contemporaneous day-$t$ outputs from Models 1, 2, 3, 4, and 6.

### Entry

- **LONG entry:** Conditioned on $T_t = 1$ (tradable regime from Model 8A), predicted class $D_t = 1$ (LONG from Model 8B), and confidence $C_t \ge \tau(\text{regime}_t)$.
- **SHORT entry:** Conditioned on $T_t = 1$, predicted class $D_t = 0$ (SHORT from Model 8B), and confidence $C_t \ge \tau(\text{regime}_t)$.
- **Abstention (Flat):** If $T_t = 0$ or $C_t < \tau(\text{regime}_t)$, output is `NO_TRADE` and target position is 0 (`research-proposed` position sizing of 0 exposure).

### Exit

- Positions exit to cash (0) immediately when the subsequent day's signal evaluates to `NO_TRADE`.
- Positions flip between LONG and SHORT when opposite active signals trigger on consecutive days.
- No stop-loss, take-profit, or trailing stop is implemented in the primary source (`source-omitted`).

### Holding period

- Variable holding period depending on consecutive active regime signals. Daily rebalance cadence.

### Parameters

| Parameter | Value | Status |
|---|---|---|
| Model 8A Model Type | XGBoost Classifier (`n_estimators=300, max_depth=4, lr=0.03, subsample=0.9, colsample_bytree=0.9`) | Source-reported |
| Model 8B Model Type | XGBoost Classifier (`n_estimators=500, max_depth=4, lr=0.03, subsample=0.8, colsample_bytree=0.8`) | Source-reported |
| Model 8B Features | `signal_1, signal_2, signal_3, signal_4, signal_6` + missingness flags | Source-reported |
| Threshold $\tau(0, 1)$ (Low Vol, Risk-On) | 0.55 | Source-reported |
| Threshold $\tau(0, 0)$ (Low Vol, Risk-Off) | 0.65 | Source-reported |
| Threshold $\tau(1, 1)$ (High Vol, Risk-On) | 0.60 | Source-reported |
| Threshold $\tau(1, 0)$ (High Vol, Risk-Off) | 0.70 | Source-reported |
| Benchmark Threshold $\tau$ | 0.60 | Source-reported |
| Base Position Sizing | Equal weight / 1x notional (+1 for LONG, -1 for SHORT, 0 for FLAT) | Research-proposed |
| Transaction Cost Stress Test | 5 bps taker fee + 5 bps slippage per turn | Research-proposed |

## Required data

- **Instrument:** Bitcoin (BTC) spot or perpetual swap (e.g. BTC/USDT, BTC/USD).
- **Universe:** Single-asset BTC (`source-reported`).
- **Venues:** Binance (derivatives flow, long/short ratio), Coinalyze (aggregated funding rates, open interest), Federal Reserve Economic Data / FRED (macro liquidity), Glassnode / CoinMetrics (on-chain metrics).
- **Timeframe:** 1-day (daily) bars.
- **Fields:**
  - Daily OHLCV for BTC.
  - Volatility metrics: GARCH conditional volatility estimates and historical realized volatility.
  - Derivatives flow: Binance top-trader long/short account ratio, aggregated futures open interest, funding rate, liquidation volume.
  - On-chain metrics: Active addresses, transaction volume, NVT ratio, miner reserve outflows.
  - Macro liquidity: US Treasury yields (10Y, 2Y), Fed balance sheet assets, High Yield spread, DXY.
- **Missing Data Handling:** Binary missingness indicator features (`signal_1_missing`, `signal_2_missing`, `signal_3_missing`, `signal_4_missing`, `signal_6_missing`) are explicitly fed to XGBoost (`source-reported`).
- **Point-in-Time Integrity:** Macroeconomic and on-chain metrics must be lagged by at least 1 publication day to prevent look-ahead bias (`research-proposed` data safeguard).

## Execution assumptions

- **Signal-to-Order Timing:** Signal computed at daily close (00:00 UTC); order executed on next candle open (`source-reported` in backtest logic via `position.shift(1)`).
- **Order Type:** Market order at open/close price.
- **Fill Model:** 100% fill assumed at reported close/open price (`source-reported`).
- **Fees:** Not modeled in primary source backtest (`source-omitted`).
- **Slippage / Spread:** Not modeled in primary source (`source-omitted`).
- **Leverage / Margin:** 1x notional long/short exposure; cash when abstaining (`research-proposed`).
- **Borrow / Shorting:** Assumes frictionless shorting via perpetual swaps; funding rate carry cost omitted in source backtest (`source-omitted`).

## Evidence

### Source-reported

The primary source repository contains two evaluation datasets with empirical backtest artifacts:

#### 1. In-Sample / Regime-Gated Evaluation (`model8_regime_gated.csv`, 2018-01-01 to 2025-12-28, 2,919 daily bars)

All figures below are extracted directly from `model8_regime_gated.csv` and `model8_confidence_curve.csv`:
- **Total Sample Window:** 2018-01-01 to 2025-12-28 (2,919 calendar days).
- **Active Trade Days:** 773 days (26.48% market coverage).
- **Directional Accuracy on Active Trades:** 80.47% (622 correct directional predictions out of 773 active trades).
- **Cumulative Strategy Return (unadjusted for transaction costs):** Reported in backtest script as >10,000x due to compounding daily returns over 8 years without friction.
- **Strategy Annualized Sharpe Ratio:** 4.55 (compared to Buy & Hold BTC Sharpe: 0.58).
- **Maximum Drawdown:** -19.67% (compared to Buy & Hold BTC Maximum Drawdown: -81.18%).
- **Confidence Threshold Curve (`model8_confidence_curve.csv`):**
  - $\tau = 0.60$: Coverage = 42.75%, Directional Accuracy = 78.85%
  - $\tau = 0.65$: Coverage = 27.61%, Directional Accuracy = 84.99%
  - $\tau = 0.70$: Coverage = 17.27%, Directional Accuracy = 86.90%

### Independently reproduced

Not independently reproduced. All metrics above represent third-party reported findings from `manavmax/Bitcoin-Alpha-System` commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.

### Negative evidence

#### 1. Severe Out-of-Sample Performance Collapse on Benchmark Data (`btc_price_daily.csv`, 2023-06-16 to 2026-03-10, 999 daily bars)

Executing the exact backtesting script `generate_daily_report.py` provided in `model8_meta_classifier/reports/` against the author's committed benchmark dataset `data/raw/btc_price_daily.csv` reveals catastrophic failure:
- **Sample Window:** 2023-06-16 to 2026-03-10 (999 daily bars).
- **Strategy Total Return:** -27.04% (compared to Buy & Hold BTC: +165.51%).
- **Strategy Annualized Sharpe Ratio:** -0.28 (compared to Buy & Hold BTC: +0.82).
- **Maximum Drawdown:** -51.29% (worse than Buy & Hold BTC: -49.53%).
- **Win Rate:** 46.72% across 274 active trades.
- **Coverage:** 27.43%.

#### 2. Author's Own Validation Warning

The repository README contains an explicit caveat regarding performance claims:
> *"A rigorous walk-forward and out-of-sample validation pass is in progress, and no performance number is being published in this README until it's been through that process — a number quoted before validation is complete is worse than no number at all, since it can't yet be distinguished from noise."*

#### 3. Overfitting Diagnosis

The massive divergence between the 2018–2025 in-sample Sharpe (4.55) and the 2023–2026 forward Sharpe (-0.28) demonstrates severe empirical vulnerability:
- The 8-module ensemble exhibits substantial parameter tuning and model selection bias.
- Static threshold gating calibrated in-sample fails when macro liquidity regimes or perpetual funding dynamics undergo structural shifts.
- Absence of transaction costs in the backtest engine hides approximately 10–15% annual drag from turnover.

## Falsification plan

1. **Walk-Forward Expanding-Window Re-Training:** Re-train Models 8A and 8B strictly on expanding windows (e.g. 3-year train, 6-month test) without refitting hyperparameters post-hoc.
   - *Research-defined falsification threshold:* If the walk-forward out-of-sample Sharpe ratio remains below 0.50 or directional accuracy on active trades drops below 52%, the meta-learning selective advantage is falsified.
2. **Transaction Cost & Funding Drag Stress:** Apply realistic crypto perpetual trading costs: 5 bps taker fee per execution, 2 bps slippage, and historical 8-hour funding rates.
   - *Research-defined falsification threshold:* If net strategy CAGR turns negative or Sharpe degrades by >1.5 under 7 bps total execution drag across the ~100 rebalance trades per year, the strategy is falsified as non-viable after execution costs.
3. **Random-Abstention Placebo Test:** Replace the Model 8A tradability decisions with a synthetic Bernoulli process matching the 26.5% coverage rate, while maintaining Model 8B directional signals.
   - *Research-defined falsification threshold:* If the Sharpe ratio or win rate of the regime-gated strategy does not exceed the random-abstention baseline at a 95% bootstrap confidence level ($p > 0.05$), the hypothesis that macro-volatility regime gating provides genuine predictive abstention is rejected.
4. **Permutation Test on Macro & Volatility Regimes:** Randomly shuffle the date index of `vol_regime` and `macro_regime` prior to Model 8A gating.
   - *Research-defined falsification threshold:* If shuffled regime gating produces equivalent or superior Sharpe ratios to the true regime series, the economic validity of the regime-switching mechanism is refuted.

## Crypto portability

**direct**

- The strategy is natively designed for, trained on, and tested with Bitcoin (BTC).
- Specific crypto market structural dependencies:
  - **Perpetual Funding Rate:** Holding short positions during prolonged bull markets incurs substantial negative funding payments on perpetual futures exchanges (Binance, Bybit, OKX). The primary source omits funding cash flows.
  - **24/7 Continuous Trading:** Daily candle boundaries must be rigorously synchronized to 00:00 UTC across spot, perpetuals, and macro feeds.
  - **Regime Transition Lags:** Macro liquidity indicators from FRED are published with multi-day lags, requiring strict point-in-time publication timestamp alignment to avoid look-ahead contamination.

## Limitations

- **Catastrophic Out-of-Sample Decay:** Severe degradation from in-sample Sharpe 4.55 to out-of-sample Sharpe -0.28 indicates extreme over-parameterization and lack of generalizability.
- **Omission of Transaction Costs:** Zero fees and zero slippage modeled in the source backtest code; real-world taker execution would substantially compound negative returns.
- **Look-Ahead & Leakage Vulnerability:** Multi-model feature alignment across 6 distinct sub-models creates significant attack surfaces for data leakage and look-ahead bias in data preparation.
- **No Stop-Loss or Risk Controls:** Active positions lack intraday stop-losses or volatility-scaled sizing, exposing capital to uncapped tail risk during high-volatility regimes.
- **Unlicensed Codebase:** The repository author declares no formal open-source license, restricting direct code redistribution.

## Implementation status

`not-implemented`

No implementation exists in our PyBroker or NautilusTrader research stacks. Not backtested, not paper-traded, not live-deployed.

## Adoption boundary

`research-only`, `not-approved`

A record being present in this repository does NOT mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- `[[quant/two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]]` (Two-level uncertainty cross-sectional ranking with regime trust gating)
- `[[quant/raml-regime-aware-multimodal-bitcoin-sentiment-fusion-2026-09-04]]` (Regime-aware multimodal fusion of social sentiment and technical features for Bitcoin)
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` (Microstructure order flow, CVD, and funding rate signal falsification)

## Sources

1. Manav Sharma. *"Bitcoin-Alpha-System: A regime-aware meta-learning system for BTC markets."* GitHub repository, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7` (September 6, 2026). URL: https://github.com/manavmax/Bitcoin-Alpha-System.
2. Manav Sharma. *"A Regime-Aware Meta-Learning Framework for Selective Directional Trading in Cryptocurrency Markets."* IEEE 2026 International Conference on Information Processing and Technology Management (ICIPTM 2026), DOI: [10.1109/ICIPTM69057.2026.11466047](https://doi.org/10.1109/ICIPTM69057.2026.11466047). Document URL: https://ieeexplore.ieee.org/document/11466047/.
3. Source file `model8_meta_classifier/results/model8_regime_gated.csv` in `manavmax/Bitcoin-Alpha-System`, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.
4. Source file `model8_meta_classifier/results/model8_confidence_curve.csv` in `manavmax/Bitcoin-Alpha-System`, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.
5. Source file `model8_meta_classifier/reports/generate_daily_report.py` in `manavmax/Bitcoin-Alpha-System`, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.
6. Source file `model8_meta_classifier/src/regime_aware_gating.py` in `manavmax/Bitcoin-Alpha-System`, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.
7. Source file `model8_meta_classifier/src/model8_final.py` in `manavmax/Bitcoin-Alpha-System`, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.
8. Source file `model8_meta_classifier/src/train_model8A.py` in `manavmax/Bitcoin-Alpha-System`, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.
9. Source file `model8_meta_classifier/src/train_model8B.py` in `manavmax/Bitcoin-Alpha-System`, commit `4bf76065f79aaaff3cc740a28b2bfe61f91b02d7`.
