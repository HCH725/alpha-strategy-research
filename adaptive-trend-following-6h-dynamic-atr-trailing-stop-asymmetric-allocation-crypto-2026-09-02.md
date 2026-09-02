---
schema: strategy-research-record-v1
title: "AdaptiveTrend: Systematic 6-Hour Trend-Following with Dynamic ATR Trailing Stop, Monthly Adaptive Portfolio Construction, and Asymmetric 70/30 Long-Short Allocation in Cryptocurrency Markets"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - trend-following
  - momentum
  - dynamic-trailing-stop
  - adaptive-portfolio
  - asymmetric-allocation
  - perpetual-futures
status: research-only
confidence: medium
source_as_of: 2026-09-02
sources:
  - "arXiv:2602.11708v1 [cs.CE], 'Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets', February 2025. DOI: 10.48550/arXiv.2602.11708. https://arxiv.org/abs/2602.11708"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AdaptiveTrend: Systematic 6-Hour Trend-Following with Dynamic ATR Trailing Stop, Monthly Adaptive Portfolio Construction, and Asymmetric 70/30 Long-Short Allocation in Cryptocurrency Markets

## Provenance

- **Primary Source:** *"Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets"*, arXiv preprint `arXiv:2602.11708v1 [cs.CE]`, February 2025. DOI: [10.48550/arXiv.2602.11708](https://doi.org/10.48550/arXiv.2602.11708). Full text: [https://arxiv.org/abs/2602.11708](https://arxiv.org/abs/2602.11708).
- **Primary Subject Area:** Computational Engineering, Finance, and Science (`cs.CE`).
- **Context:** The paper proposes AdaptiveTrend, a multi-component algorithmic trading framework integrating intermediate-frequency (6-hour) trend-following, adaptive monthly portfolio construction, and asymmetric long-short capital allocation. Evaluated on 150+ cryptocurrency perpetual swap contracts over 36 months (2022–2024 OOS).

## Economic mechanism

### Source-reported

The framework exploits three interacting mechanisms:
1. **Trend persistence at intermediate frequency:** 6-hour candlesticks capture momentum signals that are too short-lived for daily bars but too noisy for hourly bars, aligning with the 4-times-daily funding rate cycle on perpetual swaps.
2. **Adaptive risk management:** Dynamic ATR-based trailing stops calibrate exit levels to local volatility regimes, tightening in calm markets and widening during turbulence.
3. **Asymmetric allocation reflecting structural positive drift:** The 70/30 long-short split captures the empirical positive drift of cryptocurrency markets while maintaining short exposure for downside protection.
4. **Monthly performance-based selection:** Rolling Sharpe-ratio-based asset selection with market-cap filtering ensures inclusion of only assets demonstrating recent risk-adjusted momentum.

### Research interpretation

The falsifiable thesis is that **intermediate-frequency (H6) trend-following combined with volatility-adaptive exits and adaptive universe selection generates superior risk-adjusted returns in cryptocurrency perpetual futures**:

- The H6 timeframe sits at an optimal trade-off point: high enough to capture short-lived crypto momentum, low enough to avoid excessive turnover and transaction costs.
- Dynamic ATR trailing stops provide regime-adaptive risk management that static stops or volatility-scaling alone cannot achieve.
- Monthly Sharpe-ratio-based selection acts as a quality filter, removing assets whose trend signal has deteriorated.
- The 70/30 asymmetric split is motivated by the structural positive drift in crypto markets, unlike equity markets where long-short is typically dollar-neutral.

## Signal

### Formation timestamp
- Signal computed at each 6-hour candle close.
- Entry: momentum score exceeds threshold (computed from 6H OHLCV data).
- Execution: assumed at the next 6-hour candle open.

### Lookback
- Momentum lookback window `L` is a grid-searched parameter, optimized monthly over the preceding month's data.
- ATR computed over `k` periods (grid-searched).
- Rolling Sharpe ratio for asset selection computed over the preceding month's data.

### Long entry
- Long signal: `MOM_t(i) = (P_t(i) - P_{t-L}(i)) / P_{t-L}(i) > θ_entry` where `θ_entry` is grid-searched monthly.
- Entry at the next 6H candle open after signal.

### Short entry
- Short signal: `MOM_t(i) < -θ_entry^(s)` where `θ_entry^(s)` is grid-searched separately for shorts.
- Short portfolio candidate set: bottom-K_S assets by market cap.
- Short Sharpe threshold γ_S = 1.7 (higher than long threshold γ_L = 1.3) reflecting elevated risk of shorting in structurally bullish markets.

### Exit
- Dynamic trailing stop: `S_t(i) = max(S_{t-1}(i), P_t(i) - α · ATR_t(i))`
- Position closed when `P_t(i) < S_t(i)` (long) or `P_t(i) > S_t(i)` (short).
- Stop level monotonically ratchets in the direction of profit, locking in gains.
- ATR multiplier α grid-searched; optimal α = 2.5 (robust plateau α ∈ [2.0, 3.5]).

### Holding period
- Variable: held until trailing stop is hit or monthly rebalancing triggers exit.
- Average 142 trades/month across full portfolio (150+ assets).
- Monthly rebalancing: universe reconstituted on first trading day of each month.

### Parameters
- ATR multiplier α: grid-searched monthly; optimal ~2.5, robust range [2.0, 3.5].
- Long allocation ratio λ = 0.7 (70/30 long-short); robust range [0.60, 0.80].
- Long candidate pool: top K_L = 15 assets by market cap.
- Short candidate pool: bottom K_S assets by market cap.
- Long selection threshold: monthly Sharpe ≥ 1.3.
- Short selection threshold: monthly Sharpe ≥ 1.7.
- All parameters grid-searched monthly over preceding month's data.

### Position sizing
- Equal-weight within each leg: `w_i = λ / n_L` (long) or `w_j = (1-λ) / n_S` (short).

## Required data

- **Instrument:** 150+ cryptocurrency perpetual swap contracts.
- **Venue:** Binance Futures (USD-M perpetual swaps).
- **Market type:** Perpetual futures.
- **Timeframe:** 6-hour OHLCV bars; market capitalization data from CoinGecko at daily granularity.
- **Fields:** Open, High, Low, Close, Volume (6H), market cap (daily).
- **Point-in-time:** Standard OHLCV convention.
- **Timestamp:** UTC.
- **Missing-data:** Not explicitly addressed.
- **Funding/fee/spread:** Taker fee 4 bps per trade; slippage modeled as linear function of trade size relative to 5-minute volume; funding rate costs incorporated as rolling 8-hour charge/rebate.

## Execution assumptions

- **Order type:** Market order at next 6H candle open after signal.
- **Fill model:** Assumed full fill.
- **Latency:** Not specified; 6H signal cadence implies low latency sensitivity.
- **Fees:** 4 bps taker fee per trade (default); sensitivity tested at 0, 4, 8, 12 bps.
- **Slippage:** Linear function of trade size relative to 5-minute volume, calibrated from historical order book data.
- **Funding:** Rolling 8-hour perpetual swap funding rate incorporated.
- **Impact / capacity:** Short leg limited by lower-cap asset liquidity; practical capacity estimated at $5–10M for short leg before slippage exceeds 10 bps per trade. Long leg (top-15 market cap) generally liquid up to ~$50M.
- **Leverage / margin:** Not explicitly specified; perpetual swap contracts used.
- **Liquidity:** 150+ perpetual swap contracts; market cap filtering ensures minimum liquidity.

## Evidence

### Source-reported

- **Main OOS result (Jan 2022 – Dec 2024, 36 months):**
  - AdaptiveTrend 70/30: Ann. Return 40.5%, Ann. Vol. 16.8%, Sharpe 2.41, MDD -12.7%, Calmar 3.18, Sortino 3.62.
  - AdaptiveTrend 50/50: Ann. Return 34.2%, Sharpe 2.12, MDD -14.3%.
  - Vol-Scaled TSMOM: Sharpe 1.83, MDD -16.1%.
  - TSMOM-1M: Sharpe 0.65, MDD -34.8%.
  - BTC Buy-and-Hold: Sharpe 0.17, MDD -64.1%.
- **Regime-conditional:** Bull Sharpe 3.42, Sideways Sharpe 1.87, Bear Sharpe -0.31 (MDD -12.7%).
- **Ablation study:**
  - w/o Dynamic Trailing Stop: Sharpe 1.68 (−0.73).
  - w/o Market Cap Filter: Sharpe 2.05.
  - w/o Sharpe Selection: Sharpe 1.92.
  - w/o Asymmetric Allocation: Sharpe 2.12.
  - Fixed Parameters: Sharpe 1.34 (−1.07).
- **Transaction cost sensitivity:** Sharpe 2.87 (0 bps), 2.41 (4 bps), 2.01 (8 bps), 1.62 (12 bps).
- **Timeframe comparison:** H6 optimal (Sharpe 2.41); H1 (1.54), H4 (2.08), H8 (2.18), D1 (1.63).
- **Statistical significance:** Block bootstrap (10,000 reps, block length 20) confirms outperformance vs all benchmarks at 5% level; smallest margin vs Vol-Scaled TSMOM (p=0.024).
- Source reports all results; this result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Bear market performance is negative (Sharpe -0.31, Ann. Return -4.2%), though far better than buy-and-hold.
- The strategy's capacity is limited by short-leg liquidity ($5–10M).
- Monthly reoptimization introduces look-ahead bias risk if not carefully implemented (author notes 24-hour buffer mitigation).
- Strategy assumes continuous access to Binance Futures perpetual swaps; regulatory constraints may apply.

## Falsification plan

1. **Out-of-sample extension:** Extend evaluation beyond December 2024 using live data. If OOS Sharpe drops below 1.0 over a rolling 12-month window, the thesis is materially weakened.
2. **Alternative venue test:** Re-run on OKX, Bybit, or DEX perpetuals. If performance degrades substantially, venue-specific effects may dominate.
3. **Parameter robustness:** Hold all parameters fixed (no monthly reoptimization) and re-run OOS. If fixed-parameter Sharpe drops below 1.0, the monthly reoptimization is essential and the strategy may be curve-fit.
4. **Frequency decomposition:** Test H4 vs H6 vs H8 with identical portfolio construction. If the specific H6 advantage disappears, the funding-rate alignment thesis is falsified.
5. **Ablation of selection:** Run with random monthly asset selection (no Sharpe filter). If performance is comparable, the selection module adds no value.
6. **Capacity test:** Scale capital linearly and measure performance degradation. If Sharpe drops below 1.5 at $10M AUM, practical deployment is questionable.
7. **Regime stress:** Isolate bear-market subperiods (rolling 60d BTC return < -15%). If the strategy cannot achieve near-flat returns in bear regimes, the dynamic trailing stop is insufficient.

## Crypto portability

**Direct.** The study is conducted entirely on Binance cryptocurrency perpetual swap contracts.

- **Perpetual vs spot:** Funding rate costs are explicitly modeled as 8-hour rolling charges. Deployment on spot would remove funding but also remove shorting capability.
- **24/7 session:** 6H candlesticks provide natural session boundaries aligned with funding cycles.
- **Venue fragmentation:** Results are Binance-specific; liquidity and funding dynamics may differ on other venues.
- **Leverage:** Perpetual swaps enable leverage; strategy assumes leveraged access but does not specify leverage multiplier.
- **Liquidation risk:** Not explicitly modeled; extreme moves could trigger forced liquidation on leveraged positions.

## Limitations

- **Binance-only:** All data and results from Binance Futures; cross-venue portability unverified.
- **Monthly reoptimization complexity:** Grid-searching parameters monthly adds operational complexity and potential for overfitting to recent data.
- **Capacity constrained:** Short leg limited to $5–10M before slippage exceeds 10 bps.
- **Bear market underperformance:** Strategy loses money in bear markets, albeit modestly.
- **No live execution:** All results are backtested; real-world execution, API latency, and exchange outages are not modeled.
- **Anonymous paper:** No author information provided; limited independent review.
- **Look-ahead bias risk:** Monthly parameter grid-search uses the preceding month's data; the 24-hour buffer mitigates but may not fully eliminate this.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker, Nautilus, or paper trading) has been completed. No public code repository is provided.

## Adoption boundary

This record represents research material only. A record being present in this repository does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- [[quant/futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]] — related trend-following family; different mechanism (autocorrelation drift decomposition vs. adaptive ATR trailing stop with portfolio selection).

## Sources

- *"Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets"*, arXiv:2602.11708v1 [cs.CE], February 2025. DOI: 10.48550/arXiv.2602.11708. https://arxiv.org/abs/2602.11708.
