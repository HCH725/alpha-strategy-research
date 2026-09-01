---
schema: strategy-research-record-v1
title: SPXW 0DTE Volatility Risk Premium Harvesting via Cross-Sectional Learning-to-Rank
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - volatility-risk-premium
  - options
  - 0dte
  - learning-to-rank
  - spxw
  - lightgbm
  - cross-sectional
  - short-put
status: research-only
confidence: high
source_as_of: 2026-08-25
sources:
  - "Wysocki, M. (2026). Harvesting the Volatility Risk Premium: A Learning-to-Rank Approach. arXiv:2608.24786 [q-fin.CP]. https://arxiv.org/abs/2608.24786"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SPXW 0DTE Volatility Risk Premium Harvesting via Cross-Sectional Learning-to-Rank

## Provenance

- Paper: Wysocki, M. (2026). "Harvesting the Volatility Risk Premium: A Learning-to-Rank Approach."
- arXiv:2608.24786 [q-fin.CP], submitted 25 Aug 2026.
- DOI: 10.48550/arXiv.2608.24786 (arXiv-issued, pending registration).
- Source URL: https://arxiv.org/abs/2608.24786
- Sample: S&P 500 weekly options (SPXW) zero-day-to-expiration (0DTE) surface, 2021–2025.
- Venue: CBOE SPXW options (equity index options, not crypto).
- The paper is a single-author working paper; no independent replication is known.

## Economic mechanism

### Source-reported

The volatility risk premium (VRP) is the systematic tendency of implied volatility to exceed realized volatility, which generates positive expected returns for sellers of variance. The author hypothesizes that cross-sectional ranking of multiple daily short-put candidates on the 0DTE surface, combined with model-uncertainty-driven abstention, can selectively harvest VRP while avoiding adverse selection into low-VRP or high-tail-risk regimes.

### Research interpretation

The alpha mechanism is a combination of:

1. **VRP harvesting** (selling variance premium via short-put positions on 0DTE SPXW options).
2. **Cross-sectional selection** (ranking multiple delta-targeted short-put candidates daily and selecting the best-ranked, rather than mechanically selling a fixed delta).
3. **Regime-conditional abstention** (using model uncertainty to skip days when the ranker is unconfident, reducing tail-risk exposure).

The economic rationale is that the ranker can identify days and strike selections where the VRP is largest relative to tail risk, and the abstention rule avoids selling premium during regimes where the VRP is thin or the tail risk is elevated. The multiplicative regime interactions in the feature set are the primary driver of walk-forward statistical confidence.

## Signal

- **Formation timestamp**: Daily, at market open (US Eastern Time). The ranker scores a cross-section of nine candidates (eight delta-targeted short-put positions plus a SKIP candidate) each trading day.
- **Lookback**: The LightGBM LambdaRank model is trained on historical data with a path-aware Sortino-on-bars label computed at one-minute resolution. Training uses a four-window walk-forward protocol over 2021–2024.
- **Entry**: Select the highest-ranked candidate from the daily cross-section. If the SKIP candidate ranks highest, no position is taken (abstention).
- **Exit**: End-of-day or expiration (0DTE options expire at market close). The holding period is intraday only.
- **Holding period**: Intraday (0DTE options).
- **Parameters**:
  - Nine candidates per day: eight delta-targeted short-put positions at different delta levels, plus SKIP.
  - LightGBM LambdaRank as the ranking model.
  - Path-aware Sortino-on-bars label (computed at 1-minute resolution).
  - Margin-aware position sizing under CBOE index-option margin requirements.
  - Tiered fee schedule and bid-to-mid execution assumptions.
  - Confidence gate (abstention rule) driven by model uncertainty.
  - **All parameters are source-reported.** The specific delta targets, confidence threshold, and feature set are detailed in the paper.

## Required data

- **Instrument**: S&P 500 weekly options (SPXW), zero-day-to-expiration (0DTE) series.
- **Universe**: SPXW options on the 0DTE expiry each trading day.
- **Venue**: CBOE (Chicago Board Options Exchange).
- **Timeframe**: Daily rebalance (one-minute resolution for label computation during training).
- **Fields**: Option chain (bid, ask, mid, delta, strike, expiry), underlying SPX price, implied volatility surface, margin requirements, fee schedule.
- **Point-in-time**: The paper uses a strictly held-out 2025 out-of-time slice for final evaluation, separate from the 2021–2024 walk-forward windows.
- **Timestamp**: US market hours (9:30 AM – 4:15 PM ET for options).
- **Missing-data**: Not explicitly discussed; assumed complete option chain data.
- **Funding/fee/spread**: CBOE tiered fee schedule, bid-to-mid execution assumptions, CBOE index-option margin requirements. All costs are included in the evaluation.

## Execution assumptions

- **Order type**: Assumed market orders at bid-to-mid spread.
- **Fill model**: Bid-to-mid execution (conservative for short options).
- **Latency**: Not specified; assumed end-of-day execution at market open.
- **Signal-to-order timing**: Same-day execution at open.
- **Fees**: CBOE tiered fee schedule included.
- **Slippage/spread**: Bid-to-mid spread modeled.
- **Margin**: CBOE index-option margin requirements enforced.
- **Leverage**: Margin-constrained; sizing is margin-aware.
- **Funding**: Not explicitly modeled beyond margin costs.
- **Position limits**: Not specified; assumed single-position-at-a-time.

## Evidence

### Source-reported

- Walk-forward (2021–2024): Sharpe ratios between 1.90 and 3.11 across seven sizing methods.
- Out-of-time (2025): Annualized Sharpe ratios between 4.31 and 5.76 across seven sizing methods.
- Headline method: Probabilistic Sharpe Ratio of 0.964, sample-period maximum drawdown of -2.28%.
- Out-of-time Sharpe gap over CBOE PUT benchmark: at least 3.84.
- Out-of-time Sharpe gap over internal selection baselines: at least 3.69.
- Ablation: 5.05 of the 5.59 out-of-time Sharpe gap over CBOE PUT is attributable to the ranker and selection layer; the confidence gate and tail-risk features add 0.54 between them.
- Feature ablation: Removing multiplicative regime interactions collapses walk-forward statistical confidence.
- Source reports these results on a single hold-out year (2025) against walk-forward ranges. This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The result depends on a single out-of-time year (2025); robustness to other market regimes is unknown.
- Walk-forward Sharpe (1.90–3.11) is substantially lower than out-of-time (4.31–5.76), suggesting possible overfitting or regime dependency.
- The paper does not address capacity, market impact, or the scalability of the strategy.
- The paper is a single-author working paper, not peer-reviewed.

## Falsification plan

1. **Out-of-sample replication**: Replicate the walk-forward and out-of-time evaluation on an independent data source (e.g., OptionMetrics, ORATS) covering a different time period. **Failure rule**: If the out-of-time Sharpe ratio drops below 1.5, the result is materially weakened.
2. **Regime breakdown**: Evaluate performance during the 2020 COVID crash, 2022 rate-hiking regime, and 2023 regional banking stress. **Failure rule**: If the strategy loses money in any of these regimes, the regime-conditional abstention is insufficient.
3. **Parameter perturbation**: Vary the number of candidates, delta targets, and confidence threshold. **Failure rule**: If Sharpe drops by more than 50% from a 10% parameter change, the result is fragile.
4. **Fee sensitivity**: Test with realistic retail and institutional fee schedules. **Failure rule**: If the strategy becomes unprofitable at institutional fee tiers, it is capacity-constrained.
5. **Crypto portability test**: Apply the same ranking methodology to crypto options (e.g., Deribit BTC options) and evaluate whether the VRP harvesting mechanism transfers. **Failure rule**: If the ranker fails to outperform a mechanical short-put baseline on crypto options, the cross-sectional selection adds no value in that market.

## Crypto portability

**adapted**

The VRP harvesting mechanism (selling variance premium) is known to exist in crypto options markets. However:

- **Spot vs perpetual vs options**: The paper targets 0DTE SPXW options; crypto options markets (primarily Deribit) have different expiry structures, liquidity profiles, and settlement mechanics.
- **24/7 session**: Crypto markets trade 24/7; the intraday 0DTE structure does not directly map.
- **Funding**: Crypto perpetual funding is a separate mechanism from options VRP.
- **Liquidity**: Crypto options liquidity is substantially thinner than SPXW, particularly for shorter expiries.
- **Venue fragmentation**: Crypto options are concentrated on Deribit; SPXW is CBOE.
- **Mark/index price**: Crypto index prices may diverge from spot, affecting option pricing.

The learning-to-rank methodology (using a ranker to select among multiple short-option candidates) is potentially portable to crypto options, but the specific features, training protocol, and abstention rules would need to be re-derived for crypto market microstructure. This is a ported hypothesis, not crypto empirical evidence.

## Limitations

- Single out-of-time year (2025); robustness unknown.
- Walk-forward Sharpe substantially lower than out-of-time Sharpe; possible overfitting.
- Single-author working paper; no peer review.
- Not independently reproduced.
- Capacity and scalability not addressed.
- The result depends on multiplicative regime interactions in the feature set; removing them collapses statistical confidence, suggesting the signal may be fragile.
- Crypto portability is unproven; the 0DTE SPXW structure does not directly map to crypto options.

## Implementation status

Not implemented. No code or data has been made available by the author.

## Adoption boundary

This record is research material only. It does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- [[quant/bitcoin-option-rnd-low-volatility-high-vrp-regime-2026-09-01]] (crypto VRP regime; different mechanism)
- [[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]] (crypto options VRP z-score; different mechanism)
- [[quant/bitcoin-options-implied-volatility-risk-reversal-skew-2026-09-01]] (BTC options IV surface; adjacent)

## Sources

- Wysocki, M. (2026). "Harvesting the Volatility Risk Premium: A Learning-to-Rank Approach." arXiv:2608.24786 [q-fin.CP]. https://arxiv.org/abs/2608.24786
