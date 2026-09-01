---
schema: strategy-research-record-v1
title: "Multi-Scale TCN with Profit-Optimized Thresholds for Economically Significant Bitcoin Move Forecasting"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - deep-learning
  - temporal-convolutional-network
  - multi-scale
  - sentiment
  - on-chain
  - large-move-forecasting
status: research-only
confidence: medium
source_as_of: 2026-07-25
sources:
  - https://arxiv.org/abs/2608.26174 (arXiv:2608.26174v1, submitted 25 Jul 2026)
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Multi-Scale TCN with Profit-Optimized Thresholds for Economically Significant Bitcoin Move Forecasting

## Provenance

- **Paper:** Parsa Yousefnezhad, Gholamreza Mansourfar, Mohammadreza Feizi Derakhshi. "Forecasting Economically Significant Bitcoin Moves: A Multi-Scale TCN with Profit-Optimized Thresholds." arXiv:2608.26174v1 [q-fin.ST], July 25, 2026.
- **arXiv URL:** https://arxiv.org/abs/2608.26174
- **DOI:** https://doi.org/10.48550/arXiv.2608.26174
- **Subject areas:** Statistical Finance (q-fin.ST), Trading and Market Microstructure (q-fin.TR)
- **Data period:** February 2018 to December 2025
- **Data sources:** On-chain data, market data, and sentiment data for Bitcoin

## Economic mechanism

### Source-reported

The authors propose that Bitcoin's economically significant price movements (>5% within 7 days) can be forecasted by capturing multi-scale temporal patterns across on-chain, market, and sentiment data streams. The multi-scale TCN architecture with InceptionTCN blocks processes features at horizons from 1 to 4 days simultaneously, while CNN channel attention learns which data channels are most informative at each scale. The pairwise ranking loss aligns the model's training objective with ordinal prediction rather than point estimation.

### Research interpretation

The hypothesized alpha mechanism is that Bitcoin's large moves exhibit exploitable temporal structure across multiple data modalities:

- **On-chain activity** (e.g., exchange flows, active addresses, miner behavior) provides lead indicators of regime shifts
- **Market microstructure** (e.g., volume, volatility, order flow) captures short-term momentum and mean-reversion dynamics
- **Sentiment data** provides an independent information channel about crowd positioning and attention

The multi-scale architecture is motivated by the observation that different data sources operate at different time scales: on-chain signals may lead at 2-4 day horizons, while market microstructure signals are more informative at 1-day horizons. The profit-optimized threshold converts a probabilistic forecast into a trading decision by maximizing expected profit rather than classification accuracy.

**This is a ported hypothesis.** The paper does not demonstrate this mechanism in live trading; the reported results are from historical backtesting only.

## Signal

- **Formation timestamp:** End-of-day (UTC) when daily on-chain, market, and sentiment features are computed.
- **Lookback:** Multi-scale dilated convolutions with receptive fields covering 1-4 day horizons. Bottleneck and fusion layers combine features across scales.
- **Entry:** When the model's predicted probability of a >5% BTC price increase within 7 days exceeds the profit-optimized decision threshold, go long. The threshold is calibrated to maximize expected profit on the validation set rather than optimize AUC or accuracy.
- **Exit:** After 7 days (the prediction horizon), or when the model no longer signals a large move (research-proposed; source does not specify explicit exit rules beyond the 7-day horizon).
- **Holding period:** 7 days maximum per signal.
- **Parameters:**
  - Prediction target: >5% BTC price increase within 7 days
  - Architecture: Multi-scale TCN with InceptionTCN blocks, CNN channel attention, adaptive average pooling
  - Loss function: Pairwise ranking loss
  - Decision threshold: Profit-optimized (research-defined; optimized on validation set)
  - Data: On-chain + market + sentiment features
- **Underspecified:** The exact feature set, specific on-chain metrics, sentiment data source, and the precise profit-optimization procedure are not fully detailed in the abstract.

## Required data

- **Instrument:** BTC/USD (Bitcoin)
- **Venue:** Not specified (likely major exchange OHLCV + on-chain data)
- **Market type:** Spot or perpetual (not specified)
- **Timeframe:** Daily bars
- **Fields:** On-chain metrics (exact features unspecified), market OHLCV, sentiment data
- **Point-in-time:** Data from Feb 2018 to Dec 2025; specific point-in-time protections not detailed
- **Missing-data:** Not specified
- **Funding/fee/spread:** Not included in the reported results

## Execution assumptions

- Signal-to-order: End-of-day signal, assumed next-open execution (research-proposed)
- Order type: Not specified (research-proposed assumption: market order)
- Fill model: Not specified
- Fees, spread, slippage: Not included in reported profit figure
- Leverage: Not specified
- The reported profit figure (1.703) does not account for transaction costs

## Evidence

### Source-reported

- AUC: 0.6316 on the test set
- Profit: 1.703 (units not specified in abstract; likely cumulative return or profit factor)
- Comparison: Outperformed 5 baselines (ImprovedTCN_GRU, LSTM, TCN, XGBoost, Random Forest)
- Sample: Feb 2018 to Dec 2025 (test period not explicitly separated from full period in abstract)
- Class imbalance handled via AUC rather than accuracy

### Independently reproduced

Not independently reproduced.

### Negative evidence

- AUC of 0.6316 is modest; the economic significance of this edge after costs is unclear
- The profit figure (1.703) does not account for transaction costs, spread, or slippage
- No walk-forward or out-of-sample validation protocol is described in the abstract
- The model's performance in different market regimes (bull, bear, sideways) is not decomposed
- 7-day holding period exposes the position to significant drawdown risk within the horizon

## Falsification plan

1. **Out-of-sample walk-forward test:** Re-run the model with expanding or rolling windows, ensuring no look-ahead bias. Failure metric: AUC drops below 0.55 or profit turns negative after costs.
2. **Transaction cost sensitivity:** Apply realistic fees (10-20 bps round-trip), spread, and slippage. Failure threshold: profit drops below 1.0 (break-even).
3. **Parameter perturbation:** Vary the profit-optimized threshold by ±20%. Failure criterion: profit becomes negative for more than half the perturbation range.
4. **Regime decomposition:** Test separately in bull (>20% quarterly return), bear (<-20%), and sideways regimes. Failure criterion: AUC below 0.50 in any regime.
5. **Baseline comparison with simple rules:** Compare against a naive "buy when 20-day momentum > 0" or "buy when funding rate < 0" baseline. Failure criterion: TCN does not outperform simple momentum after costs.
6. **Feature ablation:** Remove on-chain, market, or sentiment features individually. Failure criterion: no single feature group contributes more than 0.02 AUC improvement.

## Crypto portability

**direct**

The paper is specifically designed for Bitcoin crypto markets. The on-chain data component is crypto-native. However:
- The exact on-chain metrics are unspecified, making independent reconstruction difficult
- The sentiment data source is not identified
- Performance on other crypto assets (ETH, etc.) is not tested
- 24/7 market structure means the 7-day holding period includes weekends and holidays without closure risk
- Funding costs for perpetual positions are not modeled

## Limitations

- **Underspecified:** The exact feature set, on-chain metrics, sentiment source, and profit-optimization procedure are not fully detailed in the abstract
- **Modest AUC:** 0.6316 is a weak signal; economic significance after costs is uncertain
- **No cost accounting:** Profit figure excludes transaction costs, fees, spread, and slippage
- **No walk-forward validation:** The abstract does not describe a rigorous out-of-sample protocol
- **No regime decomposition:** Performance across bull/bear/sideways markets is not reported
- **Single asset:** Tested only on BTC; cross-asset generalizability unknown
- **Class imbalance:** While AUC addresses this, the base rate of >5% moves in 7 days is low, meaning the strategy may have very few trades
- **Not independently reproduced**

## Implementation status

Not implemented. This is a research capture of an external paper's findings. No PyBroker, Nautilus, paper, testnet, or live implementation has been performed.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/bitcoin-ga-alpha-factor-sentiment-stacking-ensemble-2026-09-01]] — Different ML architecture (GA factor optimization vs TCN), different target (daily direction vs 7-day large move), both use sentiment
- [[quant/crypto-mofe-fourier-neural-operator-mixture-of-experts-crypto-forecasting-2026-09-01]] — Different deep learning architecture (Fourier Neural Operator vs TCN) for crypto forecasting
- [[quant/bitcoin-intraday-time-series-momentum-volume-session-2026-08-31]] — Different time scale (intraday vs 7-day) and different mechanism (time-series momentum vs multi-modal TCN)

## Sources

- Yousefnezhad, P., Mansourfar, G., & Derakhshi, M. F. (2026). Forecasting Economically Significant Bitcoin Moves: A Multi-Scale TCN with Profit-Optimized Thresholds. arXiv:2608.26174 [q-fin.ST]. https://arxiv.org/abs/2608.26174
