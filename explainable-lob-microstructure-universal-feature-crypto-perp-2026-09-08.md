---
schema: strategy-research-record-v1
title: "Explainable Patterns in Cryptocurrency Microstructure: Universal LOB Feature Library for Short-Horizon Return Prediction"
created: 2026-09-08
updated: 2026-09-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - microstructure
  - machine-learning
  - catboost
  - LOB
status: research-only
confidence: medium
source_as_of: 2026-02-03
sources:
  - "https://arxiv.org/abs/2602.00776v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Explainable Patterns in Cryptocurrency Microstructure: Universal LOB Feature Library for Short-Horizon Return Prediction

## Provenance

- **Primary paper**: Bartosz Bieganowski and Robert Ślepaczuk, "Explainable Patterns in Cryptocurrency Microstructure", arXiv preprint `arXiv:2602.00776v1 [q-fin.TR, q-fin.CP, q-fin.ST]`, submitted 2026-01-31, published on arXiv landing page 2026-02-03.
- **Authors**: Bartosz Bieganowski (University of Warsaw, Faculty of Economic Sciences, Department of Quantitative Finance and Machine Learning, Quantitative Finance Research Group); Robert Ślepaczuk, PhD, DSc (Habil.), prof. UW (same affiliation).
- **arXiv DOI**: 10.48550/arXiv.2602.00776
- **Version**: v1 (no subsequent versions found at time of capture).
- **Sample period**: January 1, 2022 – October 12, 2025.
- **Universe**: Five Binance Futures perpetual contracts: BTC, LTC, ETC, ENJ, ROSE (market cap ranks ~1, 20, 40, 60, 100 at dataset start per CoinMarketCap historical).
- **Data frequency**: 1-second order book and trade data from Binance Futures.
- **Replication code**: The paper references code availability but no public GitHub repository was found at time of capture (data gap on replication code URL).

## Economic mechanism

### Source-reported

The authors hypothesize that short-horizon return predictability in crypto admits a universal representation: a compact set of features engineered from the top of the order book and contemporaneous trade flow exhibits similar predictive importance and functional dependence shapes across assets spanning an order of magnitude in market capitalization. The economic channels are: (1) order flow imbalance captures aggressive trading pressure that moves prices via market impact; (2) bid–ask spreads proxy adverse selection risk and liquidity quality; (3) VWAP-to-mid deviations capture transient pressure and informed trading signatures. The authors connect these to Kyle (1985) and Glosten–Milgrom (1985) models of information asymmetry and adverse selection.

### Research interpretation

The hypothesis is that a scale-invariant microstructure representation exists in crypto perpetual markets: once normalized into relative prices and flows, the mapping from order book state to short-horizon returns is stable across capitalization tiers. The economic mechanism is compensated liquidity provision: aggressive taker flow creates temporary price pressure that mean-reverts as depth replenishes, and the signal is the order flow imbalance at the top of the book. The directional GMADL objective incentivizes the model to focus on correct sign prediction for large moves, aligning with the economic intuition that liquidity-taking pressure has a monotone but concave effect on returns (diminishing marginal impact at extremes).

## Signal

### Formation timestamp

Model predictions are formed at each 1-second observation timestamp using the current order book state and recent trade flow. The prediction target is the 3-second forward mid-price log return: r_{t→t+3s} = log(mid_{t+3s} / mid_t), where mid_t = (ask_0 + bid_0) / 2.

### Lookback

Feature engineering uses contemporaneous top-of-book metrics (spread, volumes), order flow and trade imbalance features aggregated over a recent window, and VWAP-to-mid deviations for buy and sell trades. Exact aggregation windows are not specified in the paper (data gap). Deep order book levels beyond top-of-book are deliberately omitted.

### Long entry

Model prediction R̂_t > θ (threshold, value not specified in paper — underspecified). Position entered as a market buy at best ask.

### Short entry

Model prediction R̂_t < −θ. Position entered as a market sell at best bid.

### Exit

Positions are adjusted only on signal changes (i.e., when the sign of R̂_t crosses zero or the magnitude drops below θ). Holding period is expected to be short (typically 1–2 seconds in normal conditions), though during the October 2025 flash crash one holding lasted ~20 seconds. No explicit stop-loss or take-profit is specified.

### Holding period

Prediction horizon is 3 seconds. Holding times can be shorter than 3 seconds if the signal changes. No maximum holding period is specified (data gap).

### Parameters

- Prediction horizon: 3 seconds (source-reported).
- Model: CatBoost gradient-boosted decision trees with GMADL (direction-aware) objective (source-reported).
- Hyperparameters: tuned via Optuna (TPE) using inner time-series cross-validation within the training window (source-reported).
- Symmetric threshold θ for signal generation: not specified in the paper (underspecified).
- Position sizing: fixed notional trades, no leverage (source-reported).
- Cross-validation: rolling time-series with deliberate temporal gap between training and validation (source-reported).

### Position-sizing logic

Fixed notional position sizing. No leverage or dynamic sizing specified (source-reported).

### Multi-timeframe dependencies

None. Single 1-second frequency with 3-second prediction horizon.

### Specification completeness

The signal is partially specified. The core modeling pipeline (CatBoost + GMADL + feature library) is reproducible. The signal generation threshold θ and exact feature aggregation windows are underspecified.

## Required data

- **Instrument**: Binance Futures perpetual contracts (BTC, LTC, ETC, ENJ, ROSE USDT-margined).
- **Venue**: Binance Futures.
- **Market type**: Perpetual futures.
- **Timeframe**: 1-second order book snapshots and trade records.
- **Fields**: Top-of-book bid/ask price and volume, trade records (price, volume, side), derived features (spread, mid price, order flow imbalance, VWAP deviations).
- **Point-in-time**: Data sourced from Binance Futures historical data, exact availability lag not specified (data gap).
- **Timestamp**: 1-second resolution, timezone not specified (data gap — likely UTC given Binance convention).
- **Missing-data**: Forward filling for short-lived gaps in order book data; samples with missing essential information excluded (source-reported).
- **Funding/fee/spread needs**: Taker fee assumed but not modeled as a drag on performance in the main results; the paper reports both gross and fee-adjusted returns using taker fee (source-reported). Spread is captured implicitly through best bid/ask execution.

## Execution assumptions

- **Signal-to-order timing**: Immediate — model prediction triggers a market order at the current best bid/ask (source-reported).
- **Execution model**: Taker strategy executes at best ask (buys) or best bid (sells); maker strategy posts limit orders at bid (buys) or ask (sells) with simulated fill based on trade-through and queue priority (source-reported).
- **Fill model**: Taker: assumed full fill at best bid/ask (conservative — inventory marked to unfavorable side). Maker: simulated fill based on subsequent trade-through and queue priority (source-reported).
- **Fees**: Taker fee acknowledged but not explicitly modeled as a performance drag in the main tables; the paper notes fee-adjusted returns are reported separately (source-reported). Exact fee rate not stated in the paper (data gap).
- **Slippage**: Conservative execution framework — inventory is marked to the unfavorable side of the book (longs to bid, shorts to ask) to penalize unrealized PnL relative to mid-marking. This understates performance (source-reported).
- **Spread**: Implicitly captured through bid/ask execution. The maker strategy uses a constant spread (not dynamically adjusted), which is a research-specified choice that contributed to its failure during the flash crash.
- **Latency**: Not explicitly modeled; results interpreted as an upper bound in the fastest regime (source-reported).
- **Impact / capacity**: Not modeled. Fixed notional sizing isolates signal quality from capacity effects (source-reported).
- **Leverage / margin**: None — fixed notional trades (source-reported).
- **Partial fills / failures**: Not modeled (data gap).

## Evidence

### Source-reported

**Taker strategy backtest (Table 2 in paper):**

| Asset | ARC | ASD | IR* | MDD |
|-------|-----|-----|-----|-----|
| BTC | 0.13 | 0.53 | 0.25 | 0.29 |
| ENJ | 4.06 | 0.62 | 6.58 | 0.26 |
| ETC | 5.78 | 0.64 | 8.97 | 0.24 |
| LTC | 0.07 | 0.99 | 0.07 | 0.64 |
| ROSE | 7.00 | 1.33 | 5.28 | 0.43 |

**Maker strategy backtest (Table 3 in paper):**

| Asset | ARC | ASD | IR* | MDD |
|-------|-----|-----|-----|-----|
| BTC | 2.93 | 0.54 | 5.47 | 0.38 |
| ENJ | −0.81 | 1.05 | −0.77 | 0.91 |
| ETC | −0.07 | 1.31 | −0.05 | 0.71 |
| LTC | 0.10 | 1.40 | 0.07 | 0.59 |
| ROSE | 0.27 | 0.84 | 0.32 | 0.55 |

**Combined 50/50 taker+maker strategy (Table 5 in paper):**

| Asset | ARC | ASD | IR* | MDD |
|-------|-----|-----|-----|-----|
| BTC | 1.25 | 0.39 | 3.24 | 0.23 |
| ENJ | 0.19 | 0.59 | 0.32 | 0.59 |
| ETC | 2.26 | 0.74 | 3.05 | 0.40 |
| LTC | 0.59 | 0.84 | 0.70 | 0.34 |
| ROSE | 3.44 | 0.75 | 4.60 | 0.42 |

**Statistical significance (Table 4 in paper):** Taker strategies on ETC (t=1.72, p=0.043), ENJ (t=1.79, p=0.037), and ROSE (t=2.08, p=0.019) are statistically significant at the 5% level. Taker strategies on BTC (p=0.747) and LTC (p=0.569) are not significant. Maker strategies are not statistically significant for any asset (all p > 0.05).

**Flash crash analysis (October 10, 2025):** The taker strategy profited during the flash crash by correctly detecting selling pressure via order book imbalance and initiating a short position. The maker strategy suffered catastrophic losses due to adverse selection — accumulating unprofitable long positions as the price collapsed. This is described as a stress test, not a separately backtested strategy.

**Cross-asset universality:** SHAP feature importance rankings are highly correlated across assets. The same feature families (order flow imbalance, spreads, VWAP deviations) dominate across all five assets. SHAP dependence shapes are consistent: order flow imbalance has a monotone effect with concavity at extremes; wider spreads reduce predictive power; VWAP-to-mid deviations show asymmetric short-horizon effects. A positive relationship between effective tick size and imbalance SHAP magnitude is documented.

**Source-reported caveats (from paper):** "The profits observed in this idealized setting may not be fully realizable in a live trading environment where microsecond advantages are paramount." "A crucial test for any trading strategy is its performance during such periods of extreme market stress." The flash crash profits are acknowledged as potentially non-repeatable.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The maker strategy is not statistically significant for any asset and loses money on ENJ and ETC, demonstrating that passive liquidity provision using the same signals is vulnerable to adverse selection.
- The combined taker+maker strategy underperforms the pure taker strategy, suggesting the maker component adds drag.
- BTC taker strategy has the lowest IR* (0.25) and is not statistically significant, suggesting the signal is weakest on the most liquid asset.
- The authors acknowledge that "causal identification of order flow effects remains an open avenue."
- The October 2025 flash crash analysis is a single-event stress test, not statistical evidence of robustness.

## Falsification plan

- **Out-of-sample validation**: Extend the sample beyond October 12, 2025, or test on other venues (Bybit, OKX) to verify cross-venue portability (research-proposed).
- **Transaction cost stress**: The current backtest uses conservative execution but does not model explicit taker fees, latency, or market impact. A full cost model including taker fees (typically 2–5 bps round-trip on Binance Futures), latency (microseconds matter for 1-second data), and queue position for the maker strategy is needed (research-proposed).
- **Parameter perturbation**: Test sensitivity to the signal threshold θ, which is underspecified in the paper. Vary θ to assess the return-vs-participation trade-off (research-proposed).
- **Regime breakdown**: The flash crash is a single event. Test performance across multiple volatility regimes (high-vol vs. low-vol periods) and multiple crash events to assess regime dependence (research-proposed).
- **Ablation tests**: Remove individual feature families (imbalance, spreads, VWAP) to assess each component's marginal contribution (research-proposed).
- **Alternative model families**: Test whether the universality result holds with linear models or deep learning architectures, or whether it is specific to CatBoost (research-proposed).
- **Capacity/liquidity limits**: Assess whether the fixed-notional backtest scales to meaningful position sizes, especially for less liquid assets like ENJ and ROSE (research-proposed).
- **Failure metric**: If taker strategy Sharpe drops below 1.0 after realistic cost modeling across all assets, the alpha thesis is materially weakened (research-defined falsification threshold).
- **Action on failure**: If falsified, the universal feature library claim is weakened but the individual SHAP dependence structures may still be informative for model design (research-proposed).

## Crypto portability

**direct**

The strategy is natively designed for and tested on crypto perpetual futures. The five-asset sample spans a wide capitalization range on Binance Futures, and the universality finding is specifically about cross-asset stability within the crypto perpetual universe.

Crypto-specific considerations:
- **Spot vs. perpetual**: Tested on perpetual contracts only. Spot markets have different tick sizes, funding mechanics, and order book dynamics. The universality claim does not extend to spot without testing.
- **Funding**: Funding rate costs are not included in the backtest. For holding periods of 1–2 seconds, funding is negligible, but during the flash crash the taker held a position for ~20 seconds, still short enough for funding to be immaterial.
- **24/7 session**: The 1-second data and 3-second horizon are naturally suited to 24/7 crypto markets.
- **Venue fragmentation**: Tested on Binance Futures only. Cross-venue generalization (OKX, Bybit) is not tested.
- **Liquidity**: The less liquid assets (ENJ, ROSE) show the strongest signal, suggesting the strategy may be capacity-constrained on illiquid pairs.
- **Mark/index price**: Mid price is computed from top-of-book bid/ask, not mark or index price. This is appropriate for the 1-second horizon.

## Limitations

- **Single venue**: All data from Binance Futures. Cross-venue portability untested (data gap).
- **Single model family**: CatBoost only. Universality across model families not tested (data gap).
- **Single prediction horizon**: 3 seconds only. Whether the universality extends to other horizons is unknown (data gap).
- **Underspecified threshold**: The signal generation threshold θ is not specified in the paper (data gap).
- **No live or paper trading**: All results are from historical backtest only.
- **Transaction cost model incomplete**: Taker fees acknowledged but not explicitly modeled in main results; latency not modeled; impact not modeled (data gap).
- **Feature aggregation windows unspecified**: The exact lookback windows for order flow and VWAP features are not detailed in the paper (data gap).
- **Flash crash is single event**: The October 2025 stress test is informative but not statistical evidence.
- **Survivorship in asset selection**: Five assets selected from a broader universe; selection criteria beyond market cap ranking not stated (data gap).
- **Maker strategy constant spread**: The maker strategy's inability to dynamically adjust spreads is a research-specified limitation, not a finding about the signal itself.
- **Not independently reproduced**: Results are source-reported only.

## Implementation status

No implementation in our research stack. The paper provides a complete methodology (CatBoost + GMADL + feature engineering + SHAP) that is reproducible in principle, but no public replication code repository was found at time of capture (data gap).

## Adoption boundary

This record represents research material only. A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The taker strategy shows promising backtest results on three of five assets, but the signal threshold is unspecified, transaction costs are incompletely modeled, and no live validation exists.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`

No materially related existing records found in the repository. The short-horizon mean reversion literature (e.g., Kitron & Wengrowicz 2026, arXiv:2608.21888) shares the 15-minute mean reversion theme but operates at a different horizon (15 minutes vs. 3 seconds), uses different signals (lag-one return sign vs. LOB features), and does not use machine learning. These are independent research captures.

## Sources

1. Bartosz Bieganowski and Robert Ślepaczuk, "Explainable Patterns in Cryptocurrency Microstructure", arXiv preprint `arXiv:2602.00776v1 [q-fin.TR]`, submitted 2026-01-31, published 2026-02-03. https://arxiv.org/abs/2602.00776v1
2. Data: Binance Futures perpetual contract order books and trades, 1-second frequency, January 1, 2022 – October 12, 2025.
3. Assets: BTC, LTC, ETC, ENJ, ROSE USDT-margined perpetual contracts.
