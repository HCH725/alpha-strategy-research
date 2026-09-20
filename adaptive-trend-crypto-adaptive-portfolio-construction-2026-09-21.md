---
schema: strategy-research-record-v1
title: AdaptiveTrend — Systematic Crypto Trend-Following with Adaptive Portfolio Construction
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - trend-following
  - momentum
  - portfolio-construction
  - adaptive
status: research-only
confidence: medium
source_as_of: 2026-02-12
sources:
  - https://arxiv.org/abs/2602.11708
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AdaptiveTrend — Systematic Crypto Trend-Following with Adaptive Portfolio Construction

## Provenance

- Paper: "Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets"
- Authors: Duc Bui, Thanh Nguyen (Talyxion Research, Hanoi, Vietnam)
- arXiv: https://arxiv.org/abs/2602.11708 (v1, submitted 2026-02-12)
- HTML version: https://ar5iv.labs.arxiv.org/html/2602.11708
- Published as arXiv preprint (not peer-reviewed at time of capture)

## Economic mechanism

### Source-reported

The authors propose that cryptocurrency markets exhibit pronounced momentum effects and regime-dependent volatility that can be exploited through intermediate-frequency trend-following combined with adaptive portfolio construction. Three structural features of crypto markets motivate the approach: (i) non-stationarity of volatility regimes renders fixed lookback windows suboptimal; (ii) asymmetric return distributions with positive skewness during bull markets and heavy left tails during crashes; (iii) rapidly evolving tradable universe where market capitalizations shift dramatically on monthly timescales. The dynamic trailing stop mechanism is calibrated to local volatility via ATR, providing tighter stops during low-volatility regimes and wider stops during high-volatility regimes. The asymmetric 70/30 long-short allocation captures the empirical positive drift of crypto markets while maintaining short-side exposure for downside protection.

### Research interpretation

The hypothesized alpha mechanism is time-series momentum (trend persistence) at the 6-hour frequency, enhanced by three adaptive layers: (1) volatility-adaptive trailing stops that dynamically adjust to local price dynamics; (2) monthly re-optimization of entry/stop parameters on a per-asset basis; (3) universe rotation via rolling Sharpe-ratio filtering with market-cap-aware partitioning. The economic rationale is that crypto markets exhibit persistent momentum at intermediate horizons (longer than noise-driven microstructure, shorter than monthly rebalancing), and that adaptive parameter calibration captures regime shifts more effectively than fixed-parameter approaches. The 70/30 long-short split is a structural bet on positive drift, not a risk-neutral allocation.

## Signal

### Formation timestamp

Signals form at each 6-hour candle close (aligned to Binance Futures perpetual swap candle boundaries). The 6-hour interval was chosen as the optimal trade-off between signal fidelity and transaction cost efficiency (H6 outperformed H1, H4, H8, H12, and D1 in ablation). The H6 interval naturally aligns with the 4-times-daily funding rate cycle on perpetual swap markets.

### Lookback

- Momentum score: `MOM_t^(i) = (P_t^(i) - P_{t-L}^(i)) / P_{t-L}^(i)`, where L is the lookback window (optimized monthly via grid search over preceding month's data).
- ATR: computed over k periods (parameter, value not specified in source beyond "k periods").
- Rolling Sharpe for asset selection: computed over the preceding month's data.
- Warm-up period: in-sample period Jan 2021 – Dec 2021 used for initial parameter calibration.

### Long entry

Long entry triggered when `MOM_t^(i) > θ_entry`, where θ_entry is optimized monthly via grid search on the preceding month's data. Only assets in the top-K_L = 15 by market cap that pass the Sharpe filter (SR_{m-1}^(i) ≥ γ_L = 1.3) are eligible.

### Short entry

Short entry triggered when `MOM_t^(i) < -θ_entry^(s)`. Only assets in the bottom-K_S by market cap that pass the Sharpe filter (SR_{m-1}^(i) ≥ γ_S = 1.7) are eligible. The higher threshold for shorts reflects elevated risk of short positions in a structurally bullish asset class.

### Exit

Dynamic trailing stop: `S_t^(i) = max(S_{t-1}^(i), P_t^(i) - α · ATR_t^(i))`. Position closed when `P_t^(i) < S_t^(i)`. α is the ATR multiplier (optimized monthly; optimal region α ∈ [2.0, 3.5], default α = 2.5). The trailing stop is monotonically increasing for long positions, locking in profits. For short positions, the analogous logic applies with inverted direction (not explicitly detailed in source — research-proposed symmetric inversion).

### Holding period

No explicit maximum holding period stated. Position held until trailing stop is hit. Average trade duration not reported.

### Parameters

- Momentum lookback L: optimized monthly via grid search (values not specified).
- ATR period k: not specified.
- ATR multiplier α: default 2.5, optimal range [2.0, 3.5].
- Long allocation ratio λ: 0.70 (70/30 long-short split).
- Long Sharpe threshold γ_L: 1.3.
- Short Sharpe threshold γ_S: 1.7.
- Long candidate universe K_L: top 15 by market cap.
- Short candidate universe: bottom assets by market cap (K_S not explicitly stated).
- Monthly re-optimization: grid search over preceding month's data.
- Parameters labeled research-proposed where source specifies optimization ranges but not fixed values for L, k, or θ_entry.

### Position sizing

Equal-weight within each portfolio leg. Long leg: λ / n_L^(m) per asset. Short leg: (1-λ) / n_S^(m) per asset. No explicit volatility scaling within the base strategy (the vol-scaled variant uses 10% annualized vol target but this is a benchmark, not the core AdaptiveTrend).

### Multi-timeframe dependencies

The paper explicitly compares timeframes (H1, H4, H6, H8, H12, D1) and selects H6 as optimal. The 6-hour interval aligns with the perpetual swap funding rate cycle (funding occurs every 8 hours on Binance, but the 6-hour candle boundaries provide clean signal points).

## Required data

- Instruments: 150+ cryptocurrency perpetual swap contracts on Binance Futures.
- Venue: Binance Futures.
- Market type: perpetual swaps.
- Timeframe: 6-hour OHLCV candles.
- Fields: Open, High, Low, Close, Volume.
- Additional data: market capitalization from CoinGecko API (daily granularity) for universe filtering.
- Funding rate: rolling 8-hour charge/rebate for perpetual swap positions.
- Timestamp: 6-hour candle close times (timezone not explicitly stated; Binance Futures uses UTC).
- Point-in-time: data sourced from Binance Futures historical API; CoinGecko market cap with daily granularity.

## Execution assumptions

- Taker fee: 4 bps per trade (source-reported).
- Slippage: modeled as linear function of trade size relative to prevailing 5-minute volume, calibrated from historical order book data (source-reported).
- Funding rate: incorporated as rolling 8-hour charge/rebate for perpetual positions (source-reported).
- Signal-to-order timing: assumed next-bar execution at candle close (research-proposed; not explicitly stated).
- Fill model: not specified (data gap).
- Market/limit order: not specified (research-proposed market order).
- Impact/capacity: acknowledged as a limitation; smaller-cap short portfolio liquidity may constrain capacity.
- Leverage/margin: not specified (data gap).
- Latency: not modeled.
- Partial fills/failures: not modeled.

## Evidence

### Source-reported

Source reports out-of-sample backtest (Jan 2022 – Dec 2024, 36 months) on Binance Futures perpetual swaps:

- AdaptiveTrend (70/30): Annualized return 40.5%, Annualized vol 16.8%, Sharpe 2.41 (rf = 4.5%), MDD −12.7%, Calmar 3.18, Sortino 3.62.
- AdaptiveTrend (50/50): Annualized return 34.2%, Sharpe 2.12, MDD −14.3%.
- Vol-Scaled TSMOM: Annualized return 22.8%, Sharpe 1.83, MDD −16.1%.
- TSMOM-1M: Sharpe 0.65, MDD −34.8%.
- BTC buy-and-hold: Sharpe 0.17, MDD −64.1%.

Regime-conditional performance (AdaptiveTrend 70/30):
- Bull: Ann. return 68.3%, Sharpe 3.42, MDD −7.1%.
- Sideways: Ann. return 18.7%, Sharpe 1.87, MDD −9.4%.
- Bear: Ann. return −4.2%, Sharpe −0.31, MDD −12.7%.

Ablation study:
- Without dynamic trailing stop: Sharpe 1.68, MDD −22.4%.
- Without market cap filter: Sharpe 2.05, MDD −17.8%.
- Without Sharpe ratio selection: Sharpe 1.92, MDD −19.1%.
- Without asymmetric allocation: Sharpe 2.12, MDD −14.3%.
- Fixed parameters (no optimization): Sharpe 1.34, MDD −28.6%.

Transaction cost impact:
- 0 bps: Sharpe 2.87.
- 4 bps: Sharpe 2.41.
- 8 bps: Sharpe 2.01.
- 12 bps: Sharpe 1.62.

Statistical significance: circular block bootstrap (10,000 replications, block length 20) shows AdaptiveTrend outperforms all benchmarks at 5% level. Smallest margin vs Vol-Scaled TSMOM (p = 0.024).

Source reports ~140% cumulative returns over the full evaluation period for both allocation variants. Average 142 trades/month.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample extension**: Extend evaluation beyond Dec 2024 into 2025+ data to test whether the 2022–2024 results generalize to different market regimes. Research-defined threshold: Sharpe < 1.0 over any rolling 12-month OOS window.
2. **Parameter perturbation**: Test sensitivity to α, λ, L outside the reported optimal ranges. If Sharpe degrades by >50% under ±20% perturbation of α or λ, the strategy is fragile.
3. **Venue/asset substitution**: Test on non-Binance venues (Bybit, OKX, dYdX) and on spot markets to assess whether the alpha is venue-specific or structural.
4. **Capacity stress test**: Increase AUM assumptions and model market impact explicitly. If Sharpe drops below 1.5 at $10M+ notional, capacity is binding.
5. **Regime breakdown**: Separate performance in extreme drawdown regimes (e.g., >30% BTC decline in <30 days) to test whether the trailing stop mechanism survives flash crashes.
6. **Ablation of monthly re-optimization**: Fix parameters at in-sample-optimal values and test OOS. If fixed-parameter Sharpe (1.34) is the true baseline, the adaptive component adds ~1.07 Sharpe units.
7. **Multiple testing correction**: The paper tests many configurations; apply Bonferroni or Holm correction across all reported variants.

## Crypto portability

direct — the strategy is natively designed for crypto perpetual swaps on Binance Futures.

Crypto-specific considerations:
- Funding rate cycle: the H6 candle interval aligns with the 8-hour funding cycle, but funding costs are explicitly modeled.
- 24/7 trading: no session boundaries to disrupt signals.
- Exchange fragmentation: strategy tested only on Binance Futures; cross-venue execution would require separate calibration.
- Liquidity: smaller-cap assets in the short portfolio may have thin order books, increasing slippage beyond model assumptions.
- Perpetual-specific: the strategy uses perpetual swap contracts; spot or quarterly futures would require different funding/carry treatment.

## Limitations

- **Single-venue backtest**: Only Binance Futures tested; exchange-specific effects (fee structure, liquidity, funding mechanics) may not generalize.
- **Sample period**: 36-month OOS (2022–2024) covers a full bear-bull cycle but may not capture structural market changes (e.g., ETF-driven regime shifts in 2024+).
- **Bear market performance**: Near-flat in bear markets (−4.2% annualized) is better than buy-and-hold but still negative; the trailing stop may not prevent all losses in crash regimes.
- **Capacity unknown**: No explicit capacity analysis; smaller-cap short portfolio liquidity is acknowledged as a limitation.
- **Transaction cost model**: Slippage modeled as linear function of volume; extreme conditions (flash crashes, exchange outages) not modeled.
- **Parameter optimization**: Monthly grid search introduces potential overfitting risk; the 24-hour buffer mitigates but does not eliminate look-ahead bias.
- **No code available**: The paper does not provide public code or data for replication.
- **Market cap data dependency**: Requires daily CoinGecko market cap data, which may have reporting lags or inaccuracies for smaller tokens.
- **Preprint quality**: arXiv preprint, not peer-reviewed.

## Implementation status

not-implemented. No implementation in our research stack has been completed. The paper does not provide public code.

## Adoption boundary

This record is research-only. A record being present in this repository does not mean:
- passed Research Intake Review;
- entered Hermes Wiki Brain;
- entered the production candidate pool;
- completed Qlib full-backtest validation;
- became a frozen survivor or leaderboard entry;
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

No directly related Wiki records identified. Tangentially related concepts include time-series momentum and volatility-targeted trend-following, which appear in the broader crypto strategy literature.

## Sources

- Bui, D. and Nguyen, T. (2026). "Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets." arXiv:2602.11708. https://arxiv.org/abs/2602.11708
