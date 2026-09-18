---
schema: strategy-research-record-v1
title: "Fractional Kelly Capital Budget for Long-Only Pullback Grid on Perpetual Futures"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - grid-trading
  - kelly-criterion
  - position-sizing
  - anti-martingale
  - long-only
  - perpetual-futures
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-08-27
sources:
  - "FMZ Quant blog: 'The Grid Shouldn't Determine Position Size: Adding a Fractional Kelly Capital Budget to a Long-Only Grid Strategy', August 27, 2026. https://blog.mathquant.com/2026/08/27/the-grid-shouldnt-determine-position-size-adding-a-fractional-kelly-capital-budget-to-a-long-only-grid-strategy.html"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fractional Kelly Capital Budget for Long-Only Pullback Grid on Perpetual Futures

## Provenance

- Source: FMZ Quant blog post (August 27, 2026).
- URL: https://blog.mathquant.com/2026/08/27/the-grid-shouldnt-determine-position-size-adding-a-fractional-kelly-capital-budget-to-a-long-only-grid-strategy.html
- Author: 小小梦 (FMZ Quant community contributor).
- The article presents an FMZ JavaScript prototype; no immutable commit SHA is available (blog post, not a versioned repository).
- The blog states: "this article presents the strategy architecture and an FMZ engineering implementation. It makes no promise of profitability, nor does it use an attractive in-sample equity curve as a substitute for out-of-sample validation."
- The strategy is described as a research prototype requiring backtesting, out-of-sample validation, paper trading, and small-capital testing before production use.

## Economic mechanism

### Source-reported

The source argues that traditional grid strategies tie position size directly to how far price has fallen (e.g., doubling at each level), which automatically expands the risk budget precisely when the market is moving against the strategy. The proposed fix separates two responsibilities: the grid layer decides **when** to act, while a Kelly layer decides **how much total capital** the grid is allowed to consume. The source describes Kelly as a "budget approval mechanism" rather than an accelerator.

The long-only structure targets assets with a hypothesis of long-term positive drift (major crypto assets or TradFi-mapped perpetuals). The EMA regime filter restricts new grid positions to bullish environments only.

### Research interpretation

The hypothesized alpha mechanism is:

1. **Grid-based mean reversion entry**: buy on pullbacks to predefined grid levels, profit from short-term mean-reversion within a range.
2. **Kelly-constrained risk budgeting**: prevent the grid from over-allocating capital during adverse moves by capping total exposure via Kelly criterion estimation from mark-to-market equity returns.
3. **Anti-martingale position sizing**: deeper grid levels receive progressively smaller allocations (weight decay factor 0.85), rejecting the Martingale structure that increases risk as price moves against the position.
4. **Regime filter**: EMA crossover (FastEMA >= SlowEMA and Close >= SlowEMA) gates new position entries to bullish environments.

The combination targets the specific failure mode of grid strategies: accumulating excessive inventory during prolonged declines. Kelly provides an evidence-based ceiling on total risk, while anti-martingale weighting ensures the grid does not pyramid into losses.

## Signal

### Grid construction

- Grid levels are placed at fixed percentage intervals below the anchor price.
- Grid spacing is the maximum of three constraints:
  - `MinGridPct` (minimum operational spacing)
  - `ATR / Price × AtrMultiplier` (volatility-adaptive spacing)
  - `2 × (FeePerSide + SlippagePerSide) × CostFloorMultiple` (cost floor)
- Clamped between `MinGridPct` and `MaxGridPct`.
- Anchor price is allowed to move upward only when flat (no positions, no active orders, trend healthy). While holding positions, the anchor does not chase price downward.

### Entry

- Regime filter: `FastEMA >= SlowEMA and Close >= SlowEMA` (research-proposed).
- When price crosses downward through a grid level under a bullish regime, buy.
- Each batch is an independent position with its own entry price and exit target.

### Exit

- Each batch exits when price rebounds by one entry-time grid spacing above its actual average fill: `TargetPrice = ActualEntryPrice × (1 + EntrySpacing)`.
- Once a batch is filled, its target is **not** modified by subsequent ATR changes (research-proposed rule to prevent dynamic parameters from postponing exits).
- Hard stop-loss: position return at or below -0.4% (research-defined).
- Take-profit: position return reaches +0.6% (research-defined).
- Maximum holding time: 30 minutes (research-defined).
- Global stop-loss: when account equity drawdown exceeds configured fraction of starting equity, auto-flatten and halt (research-proposed threshold).

### Position sizing (Kelly layer)

- Kelly fraction is computed from mark-to-market equity returns, **not** from completed grid trade win rates (the source explicitly warns against using completed-trade win rates, which exclude unrealized losses).
- `UnitRiskReturn = EquityReturn / AverageExposure` where `AverageExposure = (ExposureFraction_t + ExposureFraction_(t-1)) / 2`.
- `f_raw = argmax mean(log(1 + f × UnitRiskReturn))` over `f ∈ [0, 1]`, with constraint that `1 + f × r > 0` for all observations.
- `KellyFraction = 0.25` (one-quarter Kelly, research-proposed).
- `Confidence = min(1, SampleCount / (2 × MinSamples))`.
- `f_used = min(MaxStrategyEquityPct, f_raw × KellyFraction × Confidence)`.
- Total grid budget = `f_used × ReferenceEquity`.
- Before sufficient Kelly samples accumulate, a warm-up allocation is used (research-proposed).

### Grid level weights (anti-martingale)

- Level weights decrease by factor 0.85 per level deeper: `[1.0000, 0.8500, 0.7225, 0.6141, 0.5220]`.
- After normalization, approximate shares of total budget: Level 1 ≈ 27%, Level 2 ≈ 23%, Level 3 ≈ 19%, Level 4 ≈ 17%, Level 5 ≈ 14% (research-proposed).
- The grid is **not** allowed to increase the total budget on its own; even if price crosses five levels, combined capital cannot exceed the Kelly ceiling.
- When Kelly estimate falls and existing exposure exceeds the new budget, positions are reduced batch by batch starting from deeper lots.

### Parameters (research-proposed defaults)

| Parameter | Default | Meaning |
|---|---|---|
| `KellyFraction` | 0.25 | Fractional Kelly multiplier |
| `MinGridPct` | underspecified | Minimum grid spacing percentage |
| `MaxGridPct` | underspecified | Maximum grid spacing percentage |
| `AtrMultiplier` | underspecified | ATR scaling for grid spacing |
| `CostFloorMultiple` | 2 | Safety multiple on round-trip cost |
| `ReferenceEquity` | user-defined | Fixed equity for budget normalization |
| `WarmUpAllocationPct` | 10% | Initial allocation before Kelly samples accumulate |
| `MaxStrategyEquityPct` | underspecified | Maximum fraction of equity grid may use |
| `WeightDecayFactor` | 0.85 | Anti-martingale level weight decay |

## Required data

- Instrument: linear perpetual futures (Binance USDⓈ-M USDT-margined).
- Universe: configurable; default supports any linear perpetual with `CtValCcy` = base asset.
- Timeframe: EMA periods and grid spacing are research-proposed; the blog does not specify exact candle intervals (underspecified).
- Fields: OHLCV candles, `GetMarkets()` for contract metadata, live Bid/Ask for fill simulation.
- Funding: funding rates are acknowledged as a cost but not explicitly modeled in the grid logic (data gap).
- Missing-data: not addressed in the source.

## Execution assumptions

- Signal-to-order timing: grid level crossing triggers order placement.
- Fill model: in PAPER mode, buys use Ask and sells use Bid; spread is reflected. The `EstimatedOneWayCostBps` parameter adds additional fee estimate on top (research-proposed; source warns against double-counting spread).
- Market / limit orders: not specified (underspecified).
- Fees: one-way cost parameter available (default underspecified in the blog; the APFF strategy on FMZ uses 4 bps as reference).
- Slippage: included in PAPER mode via Bid/Ask; additional slippage parameter available.
- Funding: acknowledged as a cost for structural long positions but not explicitly modeled (data gap).
- Leverage: not specified (underspecified).
- Partial fills: the execution layer handles partial fills and order reconciliation.
- Latency: not addressed.

## Evidence

### Source-reported

The source explicitly states: "this article presents the strategy architecture and an FMZ engineering implementation. It makes no promise of profitability, nor does it use an attractive in-sample equity curve as a substitute for out-of-sample validation."

No backtest results, Sharpe ratios, win rates, or return figures are reported in the blog post. The source recommends establishing five baseline variants for comparison:
- A: Fixed grid spacing + fixed position sizing
- B: ATR + cost floor grid spacing + fixed sizing
- C: ATR + cost floor + one-quarter Kelly
- D: ATR + cost floor + half Kelly
- E: No grid, simple long at the same risk level

Evaluation metrics recommended: cumulative return, maximum drawdown, annualized volatility, Calmar ratio, average log growth, total turnover and transaction costs as percentage of gross profit, average and maximum number of active grid levels, number of trend exits and risk halts, number of times the Kelly estimate falls to zero, and parameter stability across neighboring ranges, timeframes, and instruments.

The source reports that risk parity improved all three metrics (median, win rate, worst result) across the full sample when tested on a separate cross-sectional meme momentum strategy, but this is not evidence for the grid strategy itself.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself identifies several structural risks:
- Grid strategies accumulate inventory during prolonged declines; Kelly constrains but does not eliminate this.
- Kelly estimates are affected by sampling error.
- Combining grid with Kelly "does not automatically produce a low-risk strategy."
- Reducing exposure when Kelly estimate falls creates turnover and slippage.
- A noisy Kelly estimator should not trigger a trade every time it changes slightly (buffer needed).
- For TradFi-mapped perpetuals: trading-session differences, overnight/weekend pricing, earnings gap risk, funding rates, and product-tracking mechanism differences are not addressed.
- The source notes that positive drift is a hypothesis to be tested, not a law of nature.

None identified in the reviewed sources beyond the source's own caveats; absence is not evidence of no negative result.

## Falsification plan

1. **Baseline comparison**: Run variants A–E as specified by the source. If variant C (quarter-Kelly) does not improve the Calmar ratio or average log growth versus variant B (fixed sizing), the Kelly budget layer adds complexity without benefit.
2. **Kelly estimation robustness**: Vary `MinSamples`, `KellyFraction` (0.125, 0.25, 0.5), and `Confidence` discount. If small parameter changes cause the result to disappear, the strategy is likely fitting noise.
3. **Anti-martingale vs. equal-weight vs. Martingale**: Compare the 0.85 decay factor against equal-weight grid levels and increasing-weight (Martingale) structure. If Martingale outperforms on risk-adjusted metrics, the anti-martingale hypothesis is falsified.
4. **Regime filter ablation**: Remove the EMA regime filter. If the unfiltered version performs similarly or better on risk-adjusted metrics, the regime filter is not contributing value.
5. **Cost sensitivity**: Vary `EstimatedOneWayCostBps` from 2 to 10 bps. If the strategy becomes unprofitable below 4 bps, the edge is cost-sensitive.
6. **Out-of-sample walk-forward**: Estimate parameters on training window, freeze, run next OOS period, roll forward. Aggregate all OOS results that were never used for fitting.
7. **Asset-class test**: Apply to both crypto-native perpetuals and TradFi-mapped perpetuals (NVDA, gold, etc.). If the strategy fails on TradFi perps, the long-only drift hypothesis may not transfer.
8. **Failure metric**: If the quarter-Kelly variant shows negative average log growth over a 6-month OOS window, or if maximum drawdown exceeds 30% of starting equity, the strategy should be rejected (research-defined thresholds).

## Crypto portability

direct

The strategy is designed specifically for crypto perpetual futures (Binance USDⓈ-M linear perps). The blog also discusses TradFi-mapped perpetuals as a secondary target but acknowledges several unresolved portability issues for that sub-market.

Crypto-specific considerations:
- Funding rates: structural long positions incur funding costs when rates are positive; the source acknowledges this but does not model it explicitly.
- 24/7 session structure: grid operates continuously; no session boundary issues.
- Venue fragmentation: default targets Binance only; multi-venue not addressed.
- Liquidity: grid levels assume sufficient book depth for fill; not validated.
- Mark/index price: grid uses last price for level crossing detection; index price oracle behavior not addressed.

## Limitations

- **No backtest results reported**: the source is architecture-only with no performance evidence.
- **Parameters underspecified**: `MinGridPct`, `MaxGridPct`, `AtrMultiplier`, EMA periods, candle timeframe, and `MaxStrategyEquityPct` are not concretely specified in the blog.
- **Kelly estimation sample requirements**: the minimum sample count for Kelly estimation is not specified; warm-up allocation is used but its size is research-proposed.
- **Funding cost not modeled**: structural long perpetual positions face funding payments; this is a material cost that is acknowledged but not incorporated.
- **Mark-to-market equity sampling frequency**: not specified (underspecified).
- **Single-venue**: Binance only; cross-venue hedging or multi-exchange operation not addressed.
- **Not independently reproduced**: no third-party validation exists.
- **Long-only bias**: the strategy requires a positive drift hypothesis; if the underlying enters a prolonged bear regime, the EMA filter prevents new entries but existing inventory may suffer large drawdowns before the stop-loss triggers.

## Implementation status

Not implemented in our research stack. The source provides an FMZ JavaScript prototype (v0.1.0, August 2026) described as a research prototype requiring backtesting, out-of-sample validation, paper trading, and small-capital testing.

## Adoption boundary

This record is research material only. Presence in this repository does not mean the strategy is profitable, validated, approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[crypto-dynamic-grid-trading-adaptive-boundary-resets-2026-09-02]] — grid trading with adaptive boundary resets (different mechanism: two-sided grid with Kalman-based resets, not Kelly-constrained long-only).
- [[fmz-adaptive-grid-kalman-rls-ou-cointegration-residual-width-545765-2026-09-18]] — FMZ adaptive grid with Kalman trend and Ornstein-Uhlenbeck residual width (different mechanism: mean-reversion grid with Kalman/RLS, not Kelly budget-constrained).
- [[kellyboost-growth-optimal-gbdt-portfolio-construction-2026-09-02]] — Kelly criterion for portfolio construction with gradient boosting (different domain: cross-sectional portfolio optimization, not grid trading).

## Sources

1. FMZ Quant blog, "The Grid Shouldn't Determine Position Size: Adding a Fractional Kelly Capital Budget to a Long-Only Grid Strategy," August 27, 2026. https://blog.mathquant.com/2026/08/27/the-grid-shouldnt-determine-position-size-adding-a-fractional-kelly-capital-budget-to-a-long-only-grid-strategy.html
