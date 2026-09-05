---
schema: strategy-research-record-v1
title: "Korean Venue Share Indicator (KVSI) for RL-Based Crypto Trading"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-exchange
  - reinforcement-learning
  - venue-signal
  - korean-premium
status: research-only
confidence: medium
source_as_of: 2026-01-21
sources:
  - "https://doi.org/10.3390/systems14010111"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Korean Venue Share Indicator (KVSI) for RL-Based Crypto Trading

## Provenance

- **Primary source:** Han, D.; Kim, Y. "Enhancing Reinforcement Learning-Based Crypto Asset Trading: Focusing on the Korean Venue Share Indicator." *Systems* **2026**, *14*(1), 111. DOI: [10.3390/systems14010111](https://doi.org/10.3390/systems14010111)
- **Published:** 21 January 2026 (received 14 Dec 2025; revised 13 Jan 2026; accepted 19 Jan 2026)
- **Authors:** Deok Han (ORCID 0009-0008-3469-0245), YoungJun Kim (corresponding). Graduate School of Management of Technology, Korea University, Seoul, Republic of Korea.
- **Journal:** MDPI *Systems*, Special Issue "Data-Driven Modeling and Predictive Analysis in Business, Social, Economic, Education, and Engineering Applications (2nd Edition)."
- **Funding:** None declared.
- **Data source:** Public REST APIs of Binance, Upbit, and Bithumb; daily OHLCV and exchange-level volume aggregates, 2021–2024.
- **Data availability statement:** Data obtainable from Binance API, Upbit API, and Bithumb API.

## Economic mechanism

### Source-reported

Korean crypto exchanges (Upbit, Bithumb) account for a substantial share of global spot trading activity and exhibit persistent price premiums over offshore venues (the "Kimchi premium"). This segmentation arises from capital mobility restrictions, residency-based rules, listing policies, and participant composition differences. The authors hypothesize that the relative volume share of Korean exchanges captures time-varying venue-level liquidity concentration, which in turn reflects shifts in price discovery leadership and regional order flow imbalances. By injecting this scalar into the state space of RL trading agents, the model can learn to adjust exposure when segmentation frictions are binding — particularly in non-trending or declining regimes.

### Research interpretation

The hypothesized mechanism is venue-level information asymmetry driven by market segmentation. When Korean exchanges dominate trading volume for a given asset, localized demand/supply shocks may widen cross-venue price gaps under limits to arbitrage, creating exploitable signals that standard price-based technical indicators miss. The signal is regime-dependent: most informative in downturns and range-bound markets where segmentation frictions bind, and least informative in strong uptrends where global common factors dominate and prices co-move tightly. This is a cross-sectional venue-flow signal, not a directional price prediction — it captures *where* trading intensity concentrates, not the direction of trades.

## Signal

### KVSI definition

$$\text{KVSI}_{i,t} = \frac{V_{i,t}^{\text{Upbit}} + V_{i,t}^{\text{Bithumb}}}{V_{i,t}^{\text{Upbit}} + V_{i,t}^{\text{Bithumb}} + V_{i,t}^{\text{Binance}}}$$

- **Formation timestamp:** Daily (end-of-day), using daily aggregate volume from each exchange's public API.
- **Lookback:** Current day only (no lookback window; instantaneous share).
- **Value range:** [0, 1]. Values closer to 1 indicate Korea-centered liquidity; closer to 0 indicate offshore-centered liquidity.
- **Universe restriction:** Only assets simultaneously listed on all three exchanges (Binance, Upbit, Bithumb). From 307 collected assets, k-means clustering on (mean KVSI, log average daily volume) selects the middle-KVSI cluster; extreme clusters (mean KVSI near 0 or 1) are excluded. 40 assets retained for main experiments.
- **Clustering:** k-means with k=3, silhouette score 0.62. Cluster 2 (middle KVSI) retained. Fitted on 2021–2023 training statistics; 2024 assets assigned to fixed centroids.

### RL state space and trading logic

- **Base state space:** Daily OHLCV + technical indicators (SMA 5/20/60, RSI-14, MACD, Bollinger Bands, Stochastic %K/%D, 10-day momentum). Technical indicators PCA-compressed to 3 components (~92% explained variance). OHLCV and KVSI retained in original form.
- **Proposed model (PM):** Base state space + KVSI.
- **Baseline model (BM):** Base state space only (no KVSI).
- **RL algorithms:** PPO, A2C, DQN (Stable-Baselines3). Each trained 500,000 steps per run.
- **Action space:** {Buy, Sell, Hold} — binary long/flat (each algorithm interprets this as position adjustment).
- **Reward:** Previous day's log return multiplied by the previously fixed position (dampens feedback distortions from action synchronization).
- **Execution:** Next day's open (eliminates look-ahead bias).
- **Evaluation:** 30 independent seeds per algorithm per model per quarter. Quarterly evaluation in 2024. Cross-sectional mean across 40 assets, then averaged across PPO/A2C/DQN within each seed.
- **Signal underspecification:** The KVSI itself is fully specified. The exact RL hyperparameters (learning rate, network architecture, batch size) are reported in the paper but are research-specific tuning choices. The action semantics (long/flat vs. directional) vary by algorithm and are not uniformly specified across PPO/A2C/DQN.

## Required data

- **Instrument:** Crypto spot assets (BTC, ETH, and altcoins) listed on Binance, Upbit, and Bithumb simultaneously.
- **Venue:** Binance (global reference), Upbit and Bithumb (Korean domestic).
- **Market type:** Spot only.
- **Timeframe:** Daily bars.
- **Fields:** OHLCV per exchange, exchange-level daily volume aggregates.
- **KVSI computation:** Requires concurrent daily volume from all three venues for each asset.
- **Point-in-time:** Data collected via public APIs as of 31 May 2025; training window 2021–2023; test window 2024.
- **Timestamp:** Daily, UTC-resampled.
- **Missing-data:** Gap handling for missing observations applied during collection.
- **Funding/fee/spread:** Not modeled in the primary backtest. A fee-adjusted robustness check applies a flat 0.1% Binance spot trading fee.

## Execution assumptions

- **Signal-to-order timing:** Daily signal formed at end-of-day; execution at next day's open.
- **Order type:** Assumed market order at next-day open.
- **Fill model:** Assumed perfect fill at next-day open price.
- **Fees:** Primary backtest is gross-of-fee. Fee-adjusted robustness uses 0.1% Binance spot fee. No spread, slippage, or market impact modeled.
- **Capacity:** Not assessed. Universe of 40 mid-KVSI assets; daily rebalancing assumed.
- **Leverage:** Not specified; assumed unlevered.
- **Latency:** Not modeled (daily frequency).
- **Partial fills/failures:** Not modeled.

## Evidence

### Source-reported

- **Annual aggregate (2024):** PM achieves CR 18.66%, SR 0.24, MDD 28.10% vs. BM 17.26%, 0.21, 28.71%. Paired t-test across 30 seeds: ΔCR = +1.40 pp (p = 0.0046), ΔSR = +0.03 (p = 0.0002), ΔMDD = −0.61 pp (p = 0.0366). All significant at 5%.
- **Quarterly breakdown:**
  - Q1 (upward with corrections): PM CR 34.23% vs. BM 32.44% (p = 0.096 marginal). SR 0.73 vs. 0.68 (p = 0.004). MDD 24.11% vs. 24.82% (p = 0.043).
  - Q2 (decline): PM CR −26.75% vs. BM −28.29% (p = 0.044). SR −0.81 vs. −0.85 (p = 0.054 marginal).
  - Q3 (range-bound): PM CR −1.28% vs. BM −2.21% (p = 0.013). SR 0.11 vs. 0.07 (p = 0.005).
  - Q4 (strong uptrend): PM CR 68.43% vs. BM 67.11% (non-significant).
- **Benchmark comparison (2024):** PM vs. Buy-and-Hold: ΔCR = +3.12 pp, ΔSR = +0.08, ΔMDD = −8.87 pp. PM vs. MA Crossover: ΔCR = +17.15 pp, ΔSR = +0.52. PM vs. Random Trader: ΔCR = +3.79 pp, ΔSR = −0.01, ΔMDD = −5.92 pp.
- **Algorithm-specific (PPO, 2024 total):** PM CR 21.17 ± 3.63% vs. BM 18.30 ± 2.53% (Δ = +2.87 pp). SR 0.29 vs. 0.23 (Δ = +0.07). MDD 28.88% vs. 30.21% (Δ = −1.33 pp).
- **Fee-adjusted robustness:** Qualitatively consistent with gross results; significance levels maintained.
- **Regime dependence:** KVSI contribution concentrated in non-trending regimes (Q2 decline, Q3 range-bound). Washes out in strong uptrend (Q4). Consistent with venue-share information being most informative when segmentation frictions bind.
- These results have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper's own results show KVSI has no statistically significant incremental value in Q4 (strong uptrend), consistent with the regime-dependent interpretation.
- Absolute performance levels are modest (SR 0.24 for the full year); the paper does not claim the KVSI signal alone generates strong standalone alpha.
- MDPI *Systems* is an open-access journal with a rapid review cycle; the paper has not been independently replicated or peer-reviewed by independent researchers as of the source as-of date.
- The universe is restricted to assets simultaneously listed on Binance, Upbit, and Bithumb — this may introduce survivorship and listing-selection bias.

## Falsification plan

1. **Out-of-sample extension:** Validate KVSI incremental effect on a second test year (e.g., 2025) with the same training window frozen. **Threshold:** If ΔCR or ΔSR loses statistical significance (p > 0.10) across all quarters, the signal's robustness is weakened.
2. **Alternative venue pairs:** Construct venue-share indicators for other regional clusters (e.g., China Venue Share Indicator, Japan Venue Share Indicator) and test whether the same incremental pattern holds. **Threshold:** If the venue-share signal fails to improve performance on any alternative regional cluster, the mechanism may be Korea-specific rather than generalizable.
3. **Parameter sensitivity:** Vary the clustering threshold (number of clusters, silhouette cutoff) and the RL hyperparameters. **Threshold:** If the KVSI effect is fragile to clustering choices or algorithm-specific, the result may be overfit to the specific experimental design.
4. **Transaction cost stress:** Apply realistic bid-ask spreads, slippage, and market impact models. **Threshold:** If the gross incremental ΔCR (+1.40 pp) is fully consumed by realistic costs, the strategy is not executable.
5. **Universe expansion:** Test on assets not restricted to the three-exchange intersection. **Threshold:** If the effect disappears on broader universes, it may be an artifact of the constrained listing set.
6. **Ablation:** Run the KVSI signal alone (without other technical indicators) as a standalone alpha. **Threshold:** If KVSI alone produces no significant incremental return over a random baseline, its value is purely as a conditioning variable, not an independent alpha source.

## Crypto portability

**Direct**

The signal is native to crypto markets — it is defined on cross-exchange spot volume shares for crypto assets, leveraging the specific market segmentation of the Korean crypto ecosystem. The mechanism (venue-level liquidity concentration under segmented markets) is directly applicable to crypto. However:

- **Spot vs. perpetual:** The paper studies spot only. Cross-exchange volume dynamics may differ for perpetual futures where funding rates and leverage create additional segmentation channels.
- **Venue fragmentation:** The three-exchange universe (Binance, Upbit, Bithumb) captures the dominant Korean premium venues but misses DEX volume, other CEXs (OKX, Bybit), and regional exchanges (Coinbase for US, etc.).
- **Regulatory risk:** Korea's Virtual Asset User Protection Act (effective July 2024) and potential future restrictions could compress or eliminate the Kimchi premium, reducing KVSI informativeness over time.
- **Liquidity:** Daily frequency is conservative; the signal could potentially be computed at intraday frequency for higher-resolution venue-flow tracking.
- **24/7 session:** The daily aggregation is straightforward in 24/7 crypto markets.

## Limitations

- **Single test year:** Out-of-sample evidence covers only 2024, which happened to include both decline (Q2) and strong uptrend (Q4) regimes. Longer validation needed.
- **Gross-of-fee primary result:** The 0.1% fee adjustment is a first-order approximation; spread, slippage, and market impact not modeled.
- **RL-specific:** The KVSI effect is demonstrated only within RL agent state spaces; it is not tested as a standalone rule-based signal or as a conditioning variable for non-RL strategies.
- **Universe construction:** k-means clustering on (KVSI, volume) may be sensitive to the training period and could introduce look-ahead bias if the cluster boundaries shift materially.
- **No economic magnitude context:** The incremental ΔCR of +1.40 pp and ΔSR of +0.03 are statistically significant but economically modest; whether this warrants the additional data/computational overhead is a practical question.
- **Source quality:** MDPI *Systems* is an open-access journal; while peer-reviewed, it is not a top-tier venue for financial research. The paper's claims should be treated as preliminary until independently replicated.
- **No code or data released:** The paper states data is available from public APIs but does not provide a reproducible code repository.
- **Limited theoretical foundation:** The mechanism is interpreted post-hoc through price discovery literature; no formal model derives KVSI as an optimal or sufficient statistic for segmentation-driven alpha.

## Implementation status

Not implemented. No implementation in our research stack has been completed. The KVSI signal is straightforward to compute (daily volume share from public APIs) but has not been validated outside the paper's specific RL framework.

## Adoption boundary

This record represents research material only. A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `[[crypto-cross-exchange-fiat-carry-btc-factor-2026-09-01]]` — Examines cross-exchange dynamics and carry factors in BTC markets; related venue-level analysis.
- `[[crypto-perpetual-spot-cross-venue-lead-lag-vecm-2026-09-01]]` — Analyzes cross-venue price discovery and information share dynamics between spot and derivative crypto venues.
- `[[crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01]]` — Pre-registered adversarial audit of retail systematic crypto trading; relevant context for evaluating backtest reliability.

## Sources

1. Han, D.; Kim, Y. "Enhancing Reinforcement Learning-Based Crypto Asset Trading: Focusing on the Korean Venue Share Indicator." *Systems* **2026**, *14*(1), 111. DOI: [10.3390/systems14010111](https://doi.org/10.3390/systems14010111). Published 21 January 2026.
