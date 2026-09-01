---
schema: strategy-research-record-v1
title: "AdaptiveTrend: Asymmetric Long-Short Trend-Following with Dynamic Trailing Stops and Adaptive Portfolio Construction"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - trend-following
  - momentum
  - portfolio-construction
  - trailing-stop
  - regime-adaptive
status: research-only
confidence: medium
source_as_of: 2026-02-12
sources:
  - https://arxiv.org/abs/2602.11708 (arXiv:2602.11708v1, submitted 12 Feb 2026)
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AdaptiveTrend: Asymmetric Long-Short Trend-Following with Dynamic Trailing Stops and Adaptive Portfolio Construction

## Provenance

- **Source:** arXiv:2602.11708v1, "Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets"
- **Authors:** Duc Bui, Thanh Nguyen (Talyxion Research, Hanoi, Vietnam)
- **Submitted:** 12 February 2026
- **URL:** https://arxiv.org/abs/2602.11708
- **Data source:** Binance Futures, 150+ perpetual swap contracts, 6-hour OHLCV bars, Jan 2021–Dec 2024
- **Market cap data:** CoinGecko API, daily granularity
- **Evaluation window:** Out-of-sample Jan 2022–Dec 2024 (36 months)

## Economic mechanism

### Source-reported

The authors propose a three-stage systematic framework:

1. **Signal Generation:** Momentum-based entry on 6-hour candlesticks with dynamic trailing stop exits calibrated to local ATR (Average True Range). Long entry when momentum score exceeds a monthly-optimized threshold; exit when price falls below trailing stop level.
2. **Portfolio Selection:** Monthly rebalancing that first filters by market capitalization (top-K for longs, bottom-K for shorts), then selects assets based on rolling Sharpe ratio of the trailing-stop strategy over the preceding month.
3. **Capital Allocation:** Asymmetric 70/30 long-short allocation, motivated by the empirical positive drift of crypto markets and higher borrowing costs for shorts.

The dynamic trailing stop is defined as: S_t = max(S_{t-1}, P_t − α · ATR_t), where α is a volatility multiplier and ATR is computed over k periods. The stop level monotonically increases during favorable moves, locking in profits while adapting to local volatility.

### Research interpretation

This is a **hybrid regime-adaptive trend-following strategy** with the following falsifiable economic hypotheses:

- **Trend persistence:** Crypto markets exhibit intermediate-frequency (6-hour) momentum effects that persist long enough for systematic capture.
- **Volatility regime adaptation:** Dynamic trailing stops calibrated to local ATR reduce drawdowns compared to fixed-parameter stops by tightening in low-vol regimes and widening in high-vol regimes.
- **Asymmetric allocation alpha:** A structural positive drift in crypto markets means a net-long bias (70/30) outperforms dollar-neutral (50/50) on a risk-adjusted basis.
- **Adaptive universe filtering:** Monthly market-cap filtering plus rolling Sharpe-based selection avoids exposure to illiquid or deteriorating assets in the rapidly shifting crypto universe.

The 6-hour timeframe is presented as a superior trade-off between signal fidelity and transaction cost efficiency compared to H1 (too noisy, too many trades) and D1 (misses intermediate trends).

## Signal

- **Formation timestamp:** End of each 6-hour candle.
- **Lookback window (momentum):** Parameter L, optimized monthly via grid search over preceding month's data.
- **Long entry:** MOM_t = (P_t − P_{t−L}) / P_{t−L} > θ_entry (monthly-optimized threshold).
- **Short entry:** MOM_t < −θ_entry^{(s)} (separate threshold for shorts).
- **Trailing stop (long):** S_t = max(S_{t−1}, P_t − α · ATR_t(k)). Exit when P_t < S_t.
- **Trailing stop (short):** Analogous inverted logic.
- **Holding period:** Indefinite until trailing stop is hit; no fixed holding period.
- **Re-entry:** Allowed after stop-out; next signal evaluated at next candle close.
- **Parameters:** θ_entry, α (ATR multiplier), L (lookback), k (ATR period) — all re-optimized monthly via grid search.
- **Universe filtering:** Top-K_L = 15 assets by market cap for long candidates; bottom-K_S for short candidates.
- **Sharpe-based selection:** Assets included only if trailing-month Sharpe ≥ γ_L = 1.3 (long) or γ_S = 1.7 (short).
- **Position sizing:** Equal weight within each leg; w_i = λ / n_L for longs (λ = 0.7), w_j = (1−λ) / n_S for shorts.
- **Fully specified:** Yes — all parameters, thresholds, and selection rules are explicitly defined.

## Required data

- **Instruments:** 150+ Binance perpetual swap contracts.
- **Venue:** Binance Futures.
- **Market type:** Perpetual swaps (USD-M).
- **Timeframe:** 6-hour OHLCV candles.
- **OHLCV fields:** Open, High, Low, Close, Volume.
- **Funding rate:** Incorporated as rolling 8-hour charge/rebate for perpetual positions.
- **Market cap:** Daily from CoinGecko API (for universe filtering).
- **Timestamp:** UTC candle boundaries.
- **Point-in-time:** Market cap data assumed point-in-time at daily granularity.

## Execution assumptions

- **Signal-to-order:** End-of-candle execution (next-bar).
- **Order type:** Market order assumed.
- **Fill model:** Assumes full fill at candle close price.
- **Fees:** Taker fee of 4 bps per trade.
- **Slippage:** Modeled as linear function of trade size relative to prevailing 5-minute volume, calibrated from historical order book data.
- **Funding:** Rolling 8-hour funding rate cost/rebate included.
- **Leverage:** Not explicitly stated; positions sized as fraction of account balance.
- **Capacity:** Not formally analyzed; the authors note this as future work.
- **Latency:** Not modeled; assumes end-of-candle execution.

## Evidence

### Source-reported

- **Out-of-sample (Jan 2022–Dec 2024):** Annualized return 40.5%, annualized volatility 16.8%, Sharpe ratio 2.41, maximum drawdown −12.7%, Calmar ratio 3.18, Sortino ratio 3.62.
- **vs. Vol-Scaled TSMOM:** Sharpe 2.41 vs. 1.83 (p = 0.024, 10,000 bootstrap replications, significant at 5% level).
- **vs. BTC buy-and-hold:** Sharpe 2.41 vs. 0.17; MDD −12.7% vs. −64.1%.
- **Regime-conditional:** Near-flat performance during bear markets (−4.2% annualized) vs. catastrophic B&H losses.
- **Ablation:** Dynamic trailing stop contributes most (ΔSharpe = +0.73, ΔMDD = −9.7pp). Monthly parameter optimization second (ΔSharpe = +1.07).
- **Statistical significance:** Block bootstrap (Ledoit-Wolf methodology, 10,000 replications, block length 20) confirms outperformance over all benchmarks at 5% level.
- **70/30 vs. 50/50:** 70/30 variant outperforms by 29 bps Sharpe, confirming asymmetric allocation captures structural drift.

This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- The paper notes that the short-side threshold (γ_S = 1.7) is higher than the long-side (γ_L = 1.3), suggesting short-side alpha is weaker and harder to capture — consistent with known structural bullishness of crypto markets.
- Monthly parameter re-optimization via grid search introduces potential overfitting risk to the specific training window; robustness across different calibration periods is not tested.

## Falsification plan

- **Required sample:** Replicate on independent time periods (e.g., 2025+) and different exchanges (OKX, Bybit).
- **Relevant regimes:** Test specifically in extended bear markets and high-volatility crash periods.
- **Baseline / control:** Compare against simple buy-and-hold, equal-weight rebalanced, and basic TSMOM with fixed parameters.
- **Ablation tests:** Remove each component (trailing stop, monthly optimization, market-cap filter, asymmetric allocation) individually to isolate marginal contribution.
- **Cost sensitivity:** Vary transaction costs from 1 bps to 20 bps to find break-even threshold.
- **Out-of-sample requirement:** Must survive forward testing on data not used in the original study.
- **Failure metric:** Sharpe ratio < 1.0 or MDD > −25% over any 12-month rolling window.
- **What action follows failure:** Abandon or fundamentally redesign; the framework's value depends on the specific combination of adaptive components.

## Crypto portability

direct

This strategy is natively designed for crypto perpetual swaps on Binance. Crypto-specific considerations:
- Funding rate costs are explicitly modeled but may vary significantly across venues and regimes.
- Market cap data from CoinGecko may have delays or inconsistencies for smaller-cap assets.
- 24/7 trading means the 6-hour candle framework captures all sessions without gaps.
- Liquidity fragmentation across 150+ pairs may cause slippage to exceed the modeled linear model during stress periods.

## Limitations

- **Not independently reproduced** — all results are source-reported.
- **Single-venue study** — Binance Futures only; cross-venue generalization unknown.
- **Monthly re-optimization** introduces potential look-ahead and overfitting risk; the grid search over preceding month's data may not generalize.
- **No formal capacity analysis** — strategy may degrade significantly under realistic AUM constraints.
- **Market-cap filtering** may introduce survivorship bias if delisted or migrated contracts are excluded from the sample.
- **The 6-hour timeframe** is a specific design choice; sensitivity to candle boundaries and session structure is not fully explored.
- **Data gap:** Funding rate data details (how exactly the 8-hour charge/rebate is computed and whether it uses actual or estimated rates) are not fully specified.

## Implementation status

Not implemented in our research stack. No PyBroker, Nautilus, paper trading, testnet, or live trading has occurred.

## Adoption boundary

This record is research material only. Presence in this repository does not imply:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- [[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]] (related momentum signal)
- [[crypto-cross-sectional-dispersion-scaled-momentum-20d-daily-2026-09-01]] (related momentum signal)
- [[crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31]] (related momentum signal)

## Sources

1. Bui, D., Nguyen, T. (2026). "Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets." arXiv:2602.11708v1. https://arxiv.org/abs/2602.11708
