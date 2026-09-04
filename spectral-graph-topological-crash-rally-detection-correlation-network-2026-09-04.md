---
schema: strategy-research-record-v1
title: "ORCA: Spectral Graph-Topological Crash and Rally Detection via Cross-Asset Correlation Network Features"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - regime-detection
  - spectral-graph-theory
  - random-matrix-theory
  - correlation-network
  - tail-event-prediction
  - risk-on-risk-off
  - random-forest
status: research-only
confidence: medium
source_as_of: 2026-04-19
sources:
  - https://arxiv.org/abs/2604.17251
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ORCA: Spectral Graph-Topological Crash and Rally Detection via Cross-Asset Correlation Network Features

## Provenance

- **Source**: arXiv:2604.17251v1, submitted April 19, 2026
- **Authors**: Boris Kriuk (Department of Computer Science & Engineering, Hong Kong University of Science and Technology), Fedor Kriuk (Faculty of Engineering & Information Technology, University of Technology Sydney)
- **Title**: "ORCA — Online Regime Correlation Analyzer"
- **Subject**: cs.CE (Computational Engineering, Finance, and Science)
- **Paper**: 11 pages, 5 figures
- **Source URL**: https://arxiv.org/abs/2604.17251
- **Data as-of**: 2009–2024 daily US market data (~3,750 trading days)
- **Live demo**: https://orca.boriskriuk-powered.com/

## Economic mechanism

### Source-reported

Financial crises exhibit a distinctive structural signature: assets that are normally weakly correlated begin moving in lockstep, compressing the eigenvalue spectrum of the cross-asset correlation matrix before headline volatility indicators react. The dominant eigenvalue absorbs an increasing share of total variance as herding intensifies, the spectral gap narrows, and effective rank collapses — signalling that diversification is evaporating. The paper argues that extracting spectral and graph-topological features from dynamic correlation networks captures regime shift precursors invisible to univariate volatility measures.

### Research interpretation

The hypothesised mechanism is structural regime detection through correlation network topology: when cross-asset correlations reorganise (clustering coefficient drops, edge density shifts, eigenvalue ratios compress), it signals a transition from normal to stressed or euphoric states. The signal is bifurcated:

- **Crash detection**: driven by graph-topological features (clustering coefficient, edge density, eigenvalue percentile ranks) — correlation network structural collapse precedes drawdowns
- **Rally detection**: driven by traditional price features (drawdown depth, price-to-SMA, max loss) — mean-reversion after distress

The economic thesis is that correlation topology shifts are *leading* indicators while volatility measures are *coincident/lagging* indicators. The risk-on/risk-off exposure map converts these probabilities into dynamic equity allocation with rotation into defensive assets (Gold, Treasuries, USD).

Component roles:
- **Regime signal (spectral)**: 127 features from 3 parallel correlation estimators (60-day, 120-day, 30-day EWM half-life) — absorption ratios, eigenvalue entropy, effective rank, spectral gap, condition number, eigenvector concentration, graph-topological descriptors at thresholds {0.3, 0.5, 0.7}
- **Price signal (traditional)**: 79 features — multi-horizon returns, realised/GARCH volatility, momentum, RSI, drawdown, higher moments, cross-asset return dispersion
- **Classifier**: Random Forest (200 trees, max depth 6, balanced sub-sample weighting) predicting binary rally (>3% in 10 days) and crash (>7% intra-window drawdown in 10 days)
- **Exposure map**: piecewise function of 126-day rolling percentile ranks of rally and crash probabilities → equity exposure ∈ [0, 1.5x]
- **Risk-off rotation**: when equity exposure < 1.0x, freed capital rotates to 50% GLD / 30% IEF / 20% UUP

## Signal

- **Formation timestamp**: Daily, at market close (US Eastern). Prediction horizon is 10 trading days forward.
- **Lookback**: Three parallel correlation estimators: 60-day trailing window, 120-day trailing window, 30-day half-life exponential weighted. Traditional features use 1-to-60-day lookbacks. All strictly causal.
- **Long entry**: When rally rank ∈ [0.78, 0.90] AND crash rank < 0.40 → equity exposure = 1.5x (maximum). Intermediate exposures of 0.3x–1.2x for other joint signal states.
- **Short entry**: Not applicable — strategy is long-only with risk-off rotation.
- **Exit**: When rally rank ≥ 0.90 (euphoria exit) OR crash rank ≥ 0.60 (danger exit) → equity exposure = 0, rotate to defensive portfolio. Exit overrides holding period.
- **Holding period**: Minimum 8 trading days for non-exit positions. Exit signals override.
- **Parameters**:
  - Rally threshold: >3% endpoint return in 10 days
  - Crash threshold: >7% max intra-window drawdown in 10 days
  - Exposure map thresholds: calibrated via grid search over ~50,000 combinations on first 55% of signal history, with ensemble averaging over top-20 parameter sets
  - Correlation estimation windows: 60d, 120d, 30d EWM half-life
  - Graph thresholds: {0.3, 0.5, 0.7}
  - RF config: 200 trees, max depth 6, min 30 samples/leaf, min 60 samples/split
  - All parameters are research-defined / tuned (not source-reported as optimal)
- **Position sizing**: Dynamic equity exposure ∈ [0, 1.5x] based on joint rally/crash regime. Average leverage across evaluation: 0.39x.

## Required data

- **Instrument**: 24 diversified exchange-traded instruments across 6 asset classes
- **Universe**: SPY, QQQ, IWM (broad equities); XLF, XLE, XLK, XLV, XLU, XLP, XLY, XLI, XLB, XLRE (US sector ETFs); EFA, EEM, VGK, EWJ (international equities); TLT, IEF, LQD, HYG (fixed income); GLD, USO (commodities); UUP (US Dollar)
- **Venue**: US-listed ETFs, data from EODHD API
- **Market type**: Spot ETFs (no derivatives/leverage products)
- **Timeframe**: Daily adjusted close prices
- **Fields**: Adjusted close prices → simple daily returns. Forward-fill gaps up to 5 trading days.
- **Point-in-time**: Not explicitly addressed; adjusted close prices with forward-filling
- **Timestamp**: US market close, daily frequency
- **Missing-data**: Forward-fill up to 5 trading days; remaining gaps dropped
- **Funding/fee/spread**: Transaction costs of 5 bps per trade; leverage costs of 50 bps/year on exposure > 1.0x. Spread, slippage, and market impact beyond 5 bps not modeled.

## Execution assumptions

- **Signal-to-order timing**: End-of-day signal → next-day execution (implicit from daily frequency)
- **Fill model**: Not explicitly specified; 5 bps per trade assumed
- **Market order**: Assumed (no limit order specification)
- **Fees**: 5 bps per unit of position change
- **Spread/Slippage**: 5 bps total cost per trade; spread and slippage not separately modeled
- **Leverage**: Up to 1.5x equity exposure; average 0.39x; leverage cost 50 bps/year above 1.0x
- **Capacity**: Not addressed — 24-ETF universe with daily rebalancing suggests high capacity for institutional-scale capital
- **Latency**: Daily frequency; no intraday latency requirements
- **Execution**: Ensemble averaging over top-20 parameter sets smooths parameter sensitivity; minimum 8-day hold period controls turnover

## Evidence

### Source-reported

- **Classification (Table I)**: Walk-forward out-of-sample BCD-AUC = 0.741 (Rally AUC = 0.772, Crash AUC = 0.711). Best among 6 models evaluated.
- **Ablation (Table II)**: Spectral features contribute +10.3 pp AUC for crash detection and +5.2 pp for rally detection vs. traditional-only baseline.
- **Backtest (Table III)**: Ensemble WFO strategy — Sharpe 1.13, CAGR 15.6%, Max DD -7.5%, Calmar 2.09. Benchmark (S&P 500 buy-and-hold): Sharpe 0.09, CAGR 3.7%, Max DD -33.7%, Calmar 0.11.
- **Risk-free rate assumed**: 4%
- **Sample period**: 2009–2024 (15 years, ~3,750 trading days)
- **Walk-forward**: 8 expanding-window folds, 3-year training, 10-day anti-leakage gap, 6-month test window
- **Transaction costs included**: 5 bps per trade, 50 bps/year leverage cost
- **Base rates**: Rally ~7.7%, Crash ~0.9%
- **SHAP analysis**: For crash detection, spectral/graph features account for 71.3% of total SHAP mass (0.376 vs. 0.151 for traditional). For rally detection, more balanced (spectral 46.9%, traditional 53.1%).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- HAR-RV achieves higher Crash AUC (0.763 vs. ORCA's 0.711) but lower Rally AUC (0.696 vs. 0.772), resulting in lower BCD-AUC (0.729 vs. 0.741). Crash-only models may outperform on that specific task.
- Turbulence baseline (Mahalanobis distance) performs poorly (BCD-AUC 0.605), confirming it is a coincident rather than leading indicator.
- The paper acknowledges the model is evaluated exclusively on US equity markets; generality to other geographies/asset classes is untested.
- Backtested results are subject to historical simulation caveats: execution slippage, liquidity constraints, and regime changes not in sample could erode live performance.

## Falsification plan

1. **Out-of-sample extension**: Extend test period beyond 2024 to include post-2024 market regimes (rate cuts, geopolitical shocks). Required: BCD-AUC > 0.65 (above random) across the extended period.
2. **Alternative universe**: Test on non-US equity markets (European, Asian, EM) and non-equity asset classes (crypto, commodities, FX). Required: spectral features retain >5 pp AUC contribution vs. traditional-only.
3. **Parameter perturbation**: Vary RF hyperparameters (tree count, depth, min samples) ±50%. Required: Sharpe remains > 0.8 across perturbations.
4. **Regime breakdown**: Evaluate performance separately in bull (2012–2019), crisis (2020 COVID, 2022 rate hikes), and recovery regimes. Required: no single regime has negative CAGR.
5. **Fee stress**: Triple transaction costs to 15 bps per trade. Required: Sharpe remains > 0.7.
6. **Ablation test**: Evaluate crash detection with spectral features removed entirely. Required: if Crash AUC drops below 0.65, the spectral mechanism is essential for crash alpha.
7. **Competing explanation**: Test whether the same performance is achievable with a simpler volatility-based regime filter (e.g., VIX level + momentum). Required: if a 5-feature baseline achieves comparable BCD-AUC (>0.72), the 206-dimensional model is overfitted.
8. **Live/paper validation**: The paper acknowledges this as future work; until live paper-trading results exist, the strategy remains backtested-only.

## Crypto portability

**unproven**

The ORCA framework is designed for daily US equity ETFs with a 10-day forward horizon. Crypto portability faces several challenges:

- **Universe construction**: The 24-ETF universe is US-centric. A crypto-native version would need to define a diversified crypto correlation universe (major coins, DeFi tokens, layer-1s, meme coins) — this is a non-trivial design choice.
- **Time horizon mismatch**: 10-day horizon works for daily equity data; crypto's 24/7 session structure and higher-frequency regime shifts may require shorter horizons or intraday correlation estimation.
- **Funding and leverage**: The strategy uses up to 1.5x leverage; in crypto perpetual futures, funding rates would significantly affect the carry cost of leveraged positions.
- **Correlation regime differences**: Crypto markets exhibit different correlation dynamics — altcoin correlation spikes during market-wide selloffs are more extreme and faster-moving than equity sector correlation.
- **Execution**: Daily rebalancing in crypto is feasible but exchange fragmentation, withdrawal times, and different fee structures across venues add complexity.
- **The spectral crisis-precursor hypothesis is theoretically transferable** — correlation network topology shifts likely precede crypto drawdowns — but the specific feature importance (clustering coefficient, edge density) and threshold calibrations are equity-specific and would need re-tuning.

## Limitations

- **US-only evaluation**: The model is tested exclusively on US equity ETFs; international or crypto applicability is untested (noted by authors).
- **Backtested-only**: No live or paper-trading validation has been conducted (acknowledged as future work).
- **Transaction cost model is simplified**: 5 bps per trade aggregates spread, slippage, and market impact into a single figure; no separate fill model.
- **Random Forest architecture**: May leave performance on the table vs. gradient-boosted or deep-learning alternatives (noted by authors).
- **Parameter tuning**: Ensemble averaging over top-20 parameter sets mitigates overfitting but does not eliminate it; the exposure map thresholds are calibrated on in-sample data.
- **Class imbalance**: Crash base rate is ~0.9% (severely imbalanced); balanced sub-sample weighting addresses this but rare-event detection remains inherently difficult.
- **Not independently reproduced**: All results are source-reported; no independent replication exists.
- **Publication context**: arXiv preprint (not peer-reviewed); authors are from HKUST and UTS.
- **Ensemble parameter averaging**: The top-20 parameter set averaging is a form of model averaging that reduces variance but adds complexity and may not transfer to different market regimes.

## Implementation status

Not implemented. This is a research-only capture from an arXiv preprint. The authors provide a live demo dashboard at https://orca.boriskriuk-powered.com/ but no open-source code repository was identified in the paper.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- The strategy is profitable
- The alpha has been validated
- Implementation is approved
- Paper trading, testnet, or live trading is authorized

The strategy has been backtested with transaction costs but has not been validated in our research stack (PyBroker/Nautilus) or any live/paper environment.

## Related Wiki records

- [[quant/cross-asset-reconfiguration-premium-subdominant-eigenspace-vrp]] — Uses eigenspace concepts but for a different mechanism (unspanned VRP dimension, not crash/rally classification)
- [[quant/cross-sectional-volatility-regime-gated-residual-mixture-of-experts]] — Regime-gated approach but uses MoE architecture rather than spectral graph features
- [[quant/deepm-regime-robust-macro-graph-causal-sieve-evar]] — Macro portfolio regime-robust approach using graph neural networks, distinct from spectral correlation topology

## Sources

1. Boris Kriuk, Fedor Kriuk. "ORCA — Online Regime Correlation Analyzer." arXiv:2604.17251v1, April 19, 2026. https://arxiv.org/abs/2604.17251
