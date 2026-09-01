---
schema: strategy-research-record-v1
title: Genetic Algorithm Alpha Factor Construction with Sentiment Stacking Ensemble for Bitcoin Daily Trend
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - machine-learning
  - alpha-factor-construction
  - genetic-algorithm
  - sentiment
  - ensemble
  - bitcoin
  - daily
status: research-only
confidence: medium
source_as_of: 2024-11-05
sources:
  - https://arxiv.org/abs/2411.03035
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Genetic Algorithm Alpha Factor Construction with Sentiment Stacking Ensemble for Bitcoin Daily Trend

## Provenance

- **Paper:** Quechen Yang. "Blending Ensemble for Classification with Genetic-algorithm generated Alpha factors and Sentiments (GAS)." arXiv:2411.03035v1 [q-fin.CP], November 5, 2024.
- **arXiv URL:** https://arxiv.org/abs/2411.03035
- **DOI:** https://doi.org/10.48550/arXiv.2411.03035
- **Subject areas:** Computational Finance (q-fin.CP), Machine Learning (cs.LG), Trading and Market Microstructure (q-fin.TR)
- **Data sources used in the study:**
  - Yahoo Finance daily OHLCV for BTC (3,109 trading days, 2015-07-14 to 2024-01-16)
  - jin10.com news heatmap data (377,295 records, 1,354 trading days, 2019-10-10 to 2023-07-13)
- **Note:** News sentiment data source is a Chinese financial news platform (jin10.com). Translation via Google Translate API; classification via transformer model.

## Economic mechanism

### Source-reported

The author proposes that combining genetically-optimized technical alpha factors with news sentiment signals in a stacked ensemble captures both market microstructure patterns and information-driven price movements. Genetic algorithms automate the construction of alpha factors from combinations of price, volume, and technical indicator primitives, potentially discovering non-linear factor interactions that manual feature engineering would miss. Sentiment factors from financial news provide an independent information channel. The stacking ensemble (LightGBM + XGBoost + Random Forest) leverages complementary strengths of different tree-based learners.

### Research interpretation

The hypothesized alpha mechanism is:

1. **GA-optimized factor construction:** Genetic programming evolves combinations of OHLCV primitives (price differences, moving averages, momentum oscillators, volume ratios) into composite alpha factors. This is a form of automated feature engineering that may discover non-obvious non-linear relationships in price-volume data. The economic rationale is that certain combinations of trend, momentum, and volume signals contain incremental predictive information about next-day direction.

2. **Sentiment as independent information channel:** News sentiment from financial news platforms captures information that is not yet reflected in price-volume data. The hypothesis is that sentiment shifts precede or amplify price moves, particularly in crypto markets where retail sentiment has outsized influence.

3. **Stacking ensemble diversification:** Combining LightGBM, XGBoost, and Random Forest via a blending/stacking meta-learner reduces model-specific overfitting and captures different aspects of the feature-target relationship.

**Component roles:**
- GA factors: primary predictive signals (34 factors)
- Sentiment factors: supplementary information channel (8 factors)
- Stacking ensemble: meta-learner combining base predictions

## Signal

- **Prediction target:** Binary classification of next-day BTC return direction (up/down) using a 0.1% log-return threshold
- **Lookback:** Daily OHLCV data; technical indicators computed over standard windows (MA, KAMA, MACD, KDJ, RSI variants)
- **Alpha factors (34):**
  - Trend following: price-MA differences, MA crossovers, KAMA, MACD
  - Baseline: O-C, H-L, GAP
  - Reversal signals: KDJ, RSI, lagged returns, increments
  - Volume-price: OBV, VWAP variants, volume ratios
  - Volatility: ATR, Bollinger Band width, realized volatility
  - GA-evolved composite factors (non-linear combinations of the above primitives)
- **Sentiment factors (8):**
  - Transformer-based classification of jin10.com news into positive/negative/neutral
  - Aggregated sentiment scores at daily frequency
- **Ensemble architecture:**
  - Base learners: LightGBM, XGBoost, Random Forest Classifier
  - Meta-learner: blending layer combining base learner outputs
  - Training: time-series cross-validation (TSCV) to prevent look-ahead bias
- **Execution:** Daily rebalance; predict direction at market close, position at next open
- **Parameters:** Grid search over base learner hyperparameters; 0.1% threshold for label balancing
- **Underspecified:** Exact GA evolution parameters (population size, generations, crossover/mutation rates) not fully detailed in the paper

## Required data

- **Instrument:** BTC/USD (Bitcoin)
- **Venue:** Spot market (data from Yahoo Finance)
- **Market type:** Spot
- **Timeframe:** Daily
- **OHLCV fields:** Open, High, Low, Close, Adjusted Close, Volume
- **Sentiment data:** Financial news text from jin10.com (Chinese platform); requires translation and transformer-based sentiment classification
- **Timestamp:** Daily close; prediction for next-day open
- **Point-in-time:** Sentiment data must be strictly point-in-time (no future news leakage)
- **Missing data:** Forward-fill imputation used for missing values

## Execution assumptions

- **Signal-to-order timing:** Signal generated at daily close; position taken at next-day open
- **Execution:** Market order at next open
- **Fees:** Not explicitly stated; assumed standard exchange fees
- **Slippage:** Not modeled
- **Capacity:** BTC daily volume is deep enough for retail/institutional size
- **Leverage:** Not specified; strategy is directional (long/flat or long/short)
- **Rebalancing:** Daily
- **Fill model:** Assumed full fill at open
- **Latency:** Not relevant for daily frequency

## Evidence

### Source-reported

- The GAS stacking model achieves competitive performance compared to buy-and-hold strategy on BTC daily data (2015-2024).
- Time-series cross-validation prevents look-ahead bias.
- The model outperforms individual base learners (LightGBM, XGBoost, RF alone).
- Source does not report exact Sharpe, CAGR, or drawdown figures in the abstract; full results are in the paper's experimental section.
- Source-reported result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Sentiment data source (jin10.com) is a Chinese-language platform; English-language generalization is untested.
- The 0.1% threshold for label creation may introduce look-ahead bias if not carefully implemented.
- GA-evolved factors may overfit to the specific sample period (2015-2024).
- Grid search over three base learners with ~71 hours runtime suggests high computational cost for daily retraining.
- The paper does not address transaction costs, slippage, or real-world execution constraints.

## Falsification plan

- **Required sample:** Out-of-sample period beyond 2024-01-16; ideally 12+ months of unseen data.
- **Baseline:** Compare against simple buy-and-hold, individual base learners, and a naive sentiment-only model.
- **Ablation tests:**
  - Remove sentiment factors → test if GA factors alone carry alpha
  - Remove GA factors → test if sentiment alone carries alpha
  - Replace GA factors with standard technical indicators → test if GA evolution adds value
  - Replace stacking with simple averaging → test if meta-learning adds value
- **Cost sensitivity:** Apply realistic taker fees (0.04-0.1%) and slippage to assess net profitability.
- **Regime testing:** Evaluate performance across bull (2020-2021), crash (2022), and recovery (2023-2024) regimes.
- **Failure metric:** If out-of-sample accuracy is ≤52% (barely above chance for binary classification), the strategy fails.
- **Failure action:** Discard the GA factor construction approach; consider simpler factor sets.

## Crypto portability

direct

The strategy is already designed for Bitcoin (BTC/USD daily). Crypto-specific considerations:
- 24/7 market means daily candles have different boundary semantics than equities
- Higher volatility may require wider threshold for label creation
- Sentiment data from Chinese crypto community may have different dynamics than Western crypto sentiment
- Exchange-specific microstructure (funding, liquidations) not captured in this framework

## Limitations

- not independently reproduced
- sentiment data source is platform-specific (jin10.com) and may not generalize
- GA-evolved factors may overfit to sample period
- computational cost for daily retraining is high (~71 hours with grid search)
- no transaction cost or slippage modeling
- underspecified: exact GA evolution parameters and full factor construction details require paper's appendix
- single-asset (BTC only); cross-sectional generalization untested

## Implementation status

Not implemented in our research stack.

## Adoption boundary

This record represents normalized research material only. It does NOT mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31]]
- [[crypto-cross-sectional-elastic-net-ctrend-2026-08-31]]
- [[crypto-cross-sectional-instrumented-latent-mispricing-ipca-2026-09-01]]

## Sources

1. Yang, Q. (2024). "Blending Ensemble for Classification with Genetic-algorithm generated Alpha factors and Sentiments (GAS)." arXiv:2411.03035v1 [q-fin.CP]. https://arxiv.org/abs/2411.03035
