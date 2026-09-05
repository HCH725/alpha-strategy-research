---
schema: strategy-research-record-v1
title: "Adaptive TFT Pattern-Conditioned Crypto Volatility Forecasting"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - deep-learning
  - transformer
  - adaptive-segmentation
  - pattern-conditioned-routing
status: research-only
confidence: medium
source_as_of: 2026-09-05
sources:
  - "arXiv:2509.10542v1 — https://arxiv.org/abs/2509.10542"
  - "GitHub: https://github.com/arashitc2/Adaptive-TFT (commit acd2d4fdb1b13ff01f0f455e9345050a5fbf6cab)"
  - "Data: https://github.com/arashitc2/Binance-1-minute-candles"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adaptive TFT Pattern-Conditioned Crypto Volatility Forecasting

## Provenance

- **Paper:** Peik, A., Zare Chahooki, M.A., Milani Fard, A., Sarram, M.A. (2025). "Adaptive Temporal Fusion Transformers for Cryptocurrency Price Prediction." arXiv:2509.10542v1 [q-fin.ST]. Submitted 2025-09-06; preprint dated 2025-09-16.
- **arXiv URL:** https://arxiv.org/abs/2509.10542
- **PDF:** https://arxiv.org/pdf/2509.10542
- **Code:** https://github.com/arashitc2/Adaptive-TFT (commit `acd2d4fdb1b13ff01f0f455e9345050a5fbf6cab`)
- **Data:** https://github.com/arashitc2/Binance-1-minute-candles (1-minute ETH-USDT candles, Binance)
- **Status:** Preprint ("A PREPRINT - SEPTEMBER 16, 2025"). Not peer-reviewed at time of record.

## Economic mechanism

### Source-reported

The authors propose that standard fixed-length sliding windows arbitrarily truncate meaningful market phases in cryptocurrency price data. By segmenting the volatility time series at natural boundaries (thresholded relative maxima — significant upward price movements), the resulting variable-length subseries align more closely with actual market regimes. Categorizing each subseries by the fixed-length "end pattern" of the preceding subseries and training specialized TFT models per category creates context-aware specialists that capture typical market evolution following specific recent patterns. The economic rationale is that immediate past price behavior conditions near-future behavior, and specialist models outperform generic models.

### Research interpretation

Hypothesized mechanism: **pattern-conditioned regime specialization**. The idea is that recent local price structure (the tail of the prior market phase) carries predictive information about the next phase's trajectory. This is a form of local regime conditioning — not a global Markov regime switch, but a local pattern→trajectory mapping.

The adaptive segmentation (variable-length segments ending at relative maxima) is hypothesized to capture "natural market phases" more accurately than fixed windows. The pattern-conditioned routing (Category P of subseries Si+1 determined by the end-pattern Pi of Si) is hypothesized to create specialist TFT models that become experts on the typical evolution following specific recent patterns.

**Critical note:** The economic mechanism is not independently validated — it is a modeling hypothesis. The paper's own results show that the performance gain comes primarily from very high recall (92.31%) at the expense of very low specificity (19.28%), which is consistent with a bullish-bias strategy rather than genuinely superior pattern recognition.

## Signal

**Formation timestamp:** Signal formed at the close of each 10-minute bar; tradable at the open of the next 10-minute bar. Timezone: UTC (Binance candle timestamps).

**Lookback:** Variable-length, determined by adaptive segmentation. The segmentation partitions the volatility rate series into subseries ending at thresholded relative maxima. The threshold Th controls peak sensitivity.

**Entry:** If the specialized TFT model (selected by the end-pattern of the preceding subseries) predicts an upward trend for the next 10-minute bar → buy signal. A buy signal triggers a spot long position (or holds if already long).

**Exit:** If the model predicts a downward trend for the next 10-minute bar → sell signal. The paper uses a simple directional signal: buy on up-prediction, sell on down-prediction.

**Holding period:** Variable; depends on consecutive directional predictions. No explicit maximum holding period.

**Parameters:**
- Th (relative maximum threshold): controls segmentation sensitivity; optimal value determined empirically per asset (paper-specific, not stated as a universal constant). Described as requiring "careful tuning" and likely asset/timeframe-dependent.
- plen (end-pattern length): determines the number of categories (2^plen - 1); larger plen → more specific categories but potential data sparsity. Optimal value depends on asset and timeframe.
- TFT architecture: standard Temporal Fusion Transformer with LSTM encoder-decoder, Variable Selection Networks, and multi-head attention, implemented via the Darts library.
- Both Th and plen are described as hyperparameters requiring tuning, not fixed universal constants. Their values are provided in the GitHub repository.

**Position-sizing logic:** Not specified; paper uses simple directional signals with no sizing logic.

**Re-entry rules:** Re-enter on next buy signal after sell.

**Fully specified / underspecified:** Partially underspecified. Th and plen are described as empirically tuned per asset and are available in the code but not presented as universally optimal values. The paper acknowledges they "likely depend on the specific asset and timeframe and require careful tuning."

## Required data

- **Instrument:** ETH-USDT (single asset, single pair)
- **Venue:** Binance (spot)
- **Market type:** Spot (ETH-USDT)
- **Timeframe:** 10-minute OHLCV (aggregated from 1-minute candles)
- **Fields:** Open, High, Low, Close, Volume. Primary input: volatility rate series derived from closing prices (log-returns or price change rate, per Equation 1 in the paper).
- **Point-in-time:** Data collected from Binance API; 1-minute candles from December 27, 2021 to November 22, 2024.
- **Missing-data:** Not explicitly addressed in the paper.
- **Timestamp:** Binance candle timestamps (UTC).
- **External data:** None — the model uses only price-derived volatility rates. No sentiment, on-chain, funding, or order book data.

## Execution assumptions

- **Signal-to-order timing:** Next-bar execution (10-minute horizon).
- **Order type:** Assumed market order at open of next 10-minute bar.
- **Fill model:** Not specified; paper uses "zero transaction fees for simplicity" (Section 4.2.3).
- **Fees:** Explicitly omitted (zero fees assumed).
- **Slippage:** Not modeled.
- **Spread:** Not modeled.
- **Impact / capacity:** Not modeled.
- **Funding:** Not applicable (spot trading).
- **Leverage / margin:** Not applicable (spot trading, initial capital 100 USDT).
- **Latency:** Not modeled.
- **Partial fills / failures:** Not modeled.

**Critical gap:** The paper explicitly assumes zero transaction costs. The trading simulation starts with 100 USDT and reports final asset values including simulated buys and sells with no fees. This is a significant omission — the 17.22% return over one week with frequent trading would be materially reduced by Binance maker/taker fees and spread.

## Evidence

### Source-reported

**Dataset:** ETH-USDT 10-minute candles from Binance, December 27, 2021 to November 22, 2024. Chronological split: training up to November 14, 2024; test period: November 15–22, 2024 (one week).

**Test period characteristics:** The authors note the validation period was "characterized by abnormal upward volatility" — a bullish regime.

**Table 1 — Predictive Accuracy (ETH-USDT test period):**

| Model | Accuracy (%) | Precision (%) | Recall (%) | Specificity (%) |
|-------|-------------|---------------|------------|-----------------|
| Standard LSTM | 49.15 | 49.90 | 49.80 | 49.70 |
| Standard TFT | 47.75 | 48.90 | 48.61 | 48.90 |
| FL-Cat-TFT | 50.32 | 50.11 | 58.72 | 52.79 |
| **Adaptive TFT** | **51.36** | **51.11** | **92.31** | **19.28** |

**Table 2 — Simulated Trading Profitability (ETH-USDT test period, 100 USDT initial):**

| Strategy / Model | Final Asset Value (USDT) |
|-----------------|------------------------|
| Buy and Hold | 108.32 |
| Standard LSTM Trading | 112.43 |
| Standard TFT Trading | 102.90 |
| FL-Cat-TFT Trading | 114.07 |
| **Adaptive TFT Trading** | **117.22** |

**Key observations (source-reported):**
- The Adaptive TFT achieves the highest recall (92.31%) but lowest specificity (19.28%) among all models.
- The authors acknowledge this as an "aggressive bullish strategy" — the model frequently classifies minor downward periods as continuations of upward trends.
- The high recall drove the simulated trading profit, but this performance is regime-dependent (bullish test period).
- The accuracy improvement over baselines is modest (51.36% vs 50.32% for FL-Cat-TFT).
- The paper states: "The results do not show high values for accuracy and precision, and the improvement does not seem to be considerable."

**All performance figures are source-reported and have not been independently reproduced.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Regime-dependent performance:** The test period (November 15–22, 2024) was explicitly characterized as having "abnormal upward volatility." The model's high recall / low specificity trade-off is specifically effective in this bullish regime. In a sideways or bearish market, the low specificity (19.28% — misclassifying ~80% of non-upward moves) would likely generate significant losses.

2. **Very short test window:** One week (7 days) of 10-minute data is an extremely small sample. The authors acknowledge this limitation but do not quantify the statistical significance of the result.

3. **Zero-fee assumption:** With no transaction costs, spread, or slippage modeled, the reported 17.22% weekly return overstates actual profitability. Frequent directional trading (buy/sell every 10 minutes) would incur substantial fees on Binance.

4. **Single asset, single venue:** Results are reported only for ETH-USDT on Binance. Generalizability to other cryptocurrencies, timeframes, or venues is not demonstrated.

5. **Accuracy barely above chance:** 51.36% accuracy on directional prediction is only marginally above the 50% baseline, and the paper itself acknowledges this.

6. **No out-of-sample walk-forward validation:** The model is trained on all data up to November 14, 2024, then tested on a single contiguous week. There is no walk-forward or cross-validation to demonstrate robustness.

## Falsification plan

1. **Walk-forward backtest:** Train on rolling windows (e.g., 6 months training, 1 week test, rolling forward) across the full 2021–2024 period. If the directional accuracy consistently drops to near 50% or below buy-and-hold risk-adjusted returns in bearish/sideways regimes, the hypothesis is weakened.

2. **Fee sensitivity:** Re-run the trading simulation with realistic Binance fees (0.1% maker, 0.1% taker for spot; or lower with BNB discount). If the simulated profit drops below buy-and-hold after fees, the practical edge is nullified. Research-proposed threshold: if net-of-fee return is negative or materially below buy-and-hold Sharpe, the strategy fails.

3. **Cross-asset validation:** Apply the same adaptive TFT framework to BTC-USDT, SOL-USDT, and at least 3 other major crypto pairs. If the accuracy improvement disappears on most pairs, the result may be specific to ETH-USDT during this period.

4. **Bearish regime test:** Apply the model during a known bearish period (e.g., ETH-USDT November 2022, May 2021 crash). If the low specificity generates outsized losses during drawdowns, the pattern-conditioned routing is regime-dependent and not robust.

5. **Ablation: adaptive vs fixed segmentation:** Compare adaptive TFT against FL-Cat-TFT with matched training/test splits. If the improvement from adaptive segmentation is marginal or absent, the segmentation contribution is not validated.

6. **Ablation: pattern-conditioning vs generic TFT:** Train a single TFT on all subseries (no categorization) and compare. If the generic TFT performs comparably, the pattern-conditioned routing adds no value.

7. **Parameter perturbation:** Vary Th and plen across reasonable ranges. If performance is highly sensitive to these parameters, the approach is brittle and overfit to specific parameter choices.

8. **Failure metric:** Directional accuracy below 51% or simulated net-of-fee return below buy-and-hold risk-adjusted return on a 1-month rolling window → strategy rejected.

## Crypto portability

**adapted**

The mechanism is crypto-native (applied directly to ETH-USDT on Binance). However, the portability claim is limited by:

- **Single-venue, single-pair results:** Only ETH-USDT on Binance is tested.
- **Spot-only:** The paper uses spot trading, not perpetuals. Funding rate dynamics are not modeled.
- **24/7 session structure:** The 10-minute timeframe works in 24/7 markets, but the adaptive segmentation relies on relative maxima that may behave differently in continuous vs session-based markets.
- **Liquidity:** ETH-USDT on Binance is highly liquid, but the zero-fee assumption ignores real-world execution costs.
- **No on-chain or funding data:** The model uses only price-derived volatility rates, which is a simplification.
- **Venue fragmentation:** Results are Binance-specific; other venues may have different candle boundaries or data quality.

## Limitations

- **Extremely short test period:** One week (November 15–22, 2024) is insufficient to establish statistical significance or regime robustness.
- **Regime-dependent performance:** The bullish test period inflated the model's performance via high recall. The low specificity (19.28%) suggests the model is a "buy-the-dip" strategy masquerading as pattern recognition.
- **Zero transaction costs:** All trading is simulated with no fees, spread, or slippage. This materially overstates actual profitability.
- **Single asset, single venue:** ETH-USDT on Binance only. No cross-asset or cross-venue validation.
- **Parameter sensitivity:** Th and plen require per-asset tuning; optimal values are not transferable without re-tuning.
- **Modest accuracy improvement:** 51.36% accuracy is barely above chance. The paper itself acknowledges the improvement "does not seem to be considerable."
- **No walk-forward validation:** Single contiguous train/test split; no cross-validation or out-of-sample robustness testing.
- **Not peer-reviewed:** Preprint status; no independent replication.
- **Data gap:** Missing data handling is not addressed. Imputation rules are not specified.
- **Not independently reproduced.**
- **Underspecified:** Exact Th and plen values are in the code but not presented as universally optimal. The relationship between these parameters and market regime is not characterized.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker / NautilusTrader) has been completed.

## Adoption boundary

This record is research material only. It does not constitute:
- Proof of profitable alpha
- Validation of the pattern-conditioned routing hypothesis
- Authorization for paper trading, testnet, or live execution
- Evidence that the mechanism generalizes beyond ETH-USDT on Binance during a bullish one-week window

## Related Wiki records

No directly related Wiki Brain records identified. Adjacent strategy families in the repository include:
- Transformer-based crypto forecasting records (e.g., MoFE fourier neural operator, KASPER)
- Adaptive regime-switching records (e.g., HMM reinforcement learning ETF allocation)
- Crypto volatility forecasting records

## Sources

1. Peik, A., Zare Chahooki, M.A., Milani Fard, A., Sarram, M.A. (2025). "Adaptive Temporal Fusion Transformers for Cryptocurrency Price Prediction." arXiv:2509.10542v1 [q-fin.ST]. https://arxiv.org/abs/2509.10542
2. GitHub repository: https://github.com/arashitc2/Adaptive-TFT (commit `acd2d4fdb1b13ff01f0f455e9345050a5fbf6cab`)
3. Data repository: https://github.com/arashitc2/Binance-1-minute-candles
