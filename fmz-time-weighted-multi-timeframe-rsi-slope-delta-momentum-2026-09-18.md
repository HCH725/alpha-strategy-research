---
schema: strategy-research-record-v1
title: "FMZ Time-Weighted Multi-Timeframe RSI Slope and Delta Momentum Strategy"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - multi-timeframe
  - RSI
  - slope-momentum
  - dynamic-threshold
  - adaptive
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ strategy 509733, 'Time-Based Slope & Delta RSI Strategy (HA & Source Selectable)'. https://www.fmz.com/strategy/509733. Created 2025-09-25, reviewed 2026-09-18."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Time-Weighted Multi-Timeframe RSI Slope and Delta Momentum Strategy

## Provenance

- **Source**: FMZ strategy 509733, publicly available on https://www.fmz.com/strategy/509733
- **Strategy name**: "Time-Based Slope & Delta RSI Strategy (HA & Source Selectable)"
- **Author**: FMZ community author (username not individually attributed in the public page)
- **Created**: 2025-09-25
- **Source data as-of**: 2026-09-18 (strategy page reviewed)
- **Platform**: FMZ Quant (Pine Script v5, deployed on Binance Futures)
- **Backtest window**: 2025-01-01 to 2025-09-24 (as shown in strategy page backtest header)
- **Instrument**: ETH/USDT perpetual, Binance Futures (as shown in backtest configuration)
- **Primary source inspection**: The full Pine Script source code and strategy description were read directly from the FMZ strategy page on 2026-09-18.

## Economic mechanism

### Source-reported

The strategy integrates RSI data from five timeframes (5-minute, 15-minute, 1-hour, 4-hour, daily) plus the chart timeframe using logarithmic weighting to compute a composite "weighted RSI." Rather than using RSI levels (overbought/oversold), the strategy analyzes the rate of change of this weighted RSI (its slope) and the acceleration of that slope (Delta). Trading signals are triggered only when both the RSI slope and its moving-average slope exceed a dynamic threshold that auto-adjusts based on the chart timeframe, AND the momentum Delta simultaneously amplifies. The source claims this dual confirmation mechanism filters out invalid breakouts during sideways consolidation.

The source also claims the dynamic threshold system improves signal quality by 25% over fixed thresholds, and that multi-timeframe fusion reduces false signals by approximately 40% compared to single-timeframe RSI. These are source-reported claims; the source does not provide a peer-reviewed paper, formal methodology, or independently audited backtest results to support these specific numbers.

### Research interpretation

The falsifiable hypothesis is that the **rate of change** (slope) of a multi-timeframe weighted RSI contains directional information that simple RSI levels or single-timeframe RSI do not capture, and that combining slope with acceleration (Delta) provides a dual-confirmation filter that reduces false signals in trending markets. The logarithmic weighting scheme assigns more weight to higher-timeframe RSI values, which is consistent with the empirical finding that higher-timeframe signals tend to be more persistent and less noisy.

The dynamic threshold mechanism is an adaptive scaling rule: `dynamicSlopeThreshold = slopeThreshold × √(current period minutes / base period minutes)`. This means the signal becomes less sensitive on longer timeframes (requiring stronger slope confirmation), which is consistent with the intuition that longer-timeframe trends should be confirmed by larger moves.

The Heikin Ashi mode smooths price data before RSI computation, which should reduce whipsaw signals from candle noise. The reversal re-entry mechanism (re-entering opposite positions within 3 bars of a take-profit exit) captures trend-continuation opportunities at potential inflection points.

## Signal

### Formation timestamp

Signals are formed at bar close. The strategy evaluates conditions only after a bar has completed. No lookahead is used in the signal formation.

### Lookback

- **RSI period**: 14 (default)
- **RSI MA period**: 5 (default, applied to the weighted RSI)
- **MA type**: EMA (default)
- **Multi-timeframe RSI**: computed from 5-minute, 15-minute, 1-hour, 4-hour, and daily timeframes, plus the chart timeframe
- **Logarithmic weighting**: weight_i = ln(minutes_i / baseMinutes + 1), where baseMinutes = 15 (default)
- **Chart time effect ratio**: 2.0 (multiplier applied to the chart-timeframe weight)

### Entry (source-reported)

**Long entry**: When `rsiSlope > dynamicSlopeThreshold` AND `rsiMASlope > dynamicSlopeThreshold` AND `rsiSlopeDelta > deltaThreshold` AND `rsiMASlopeDelta > deltaThreshold`

**Short entry**: When `rsiSlope < -dynamicSlopeThreshold` AND `rsiMASlope < -dynamicSlopeThreshold` AND `rsiSlopeDelta < -deltaThreshold` AND `rsiMASlopeDelta < -deltaThreshold`

Where:
- `rsiSlope = weightedRSI - weightedRSI[1]` (1-bar change in weighted RSI)
- `rsiMASlope = weightedRSIMA - weightedRSIMA[1]` (1-bar change in weighted RSI MA)
- `rsiSlopeDelta = rsiSlope - rsiSlope[1]` (acceleration of slope)
- `rsiMASlopeDelta = rsiMASlope - rsiMASlope[1]` (acceleration of MA slope)
- `dynamicSlopeThreshold = slopeThreshold × min(√(chartMinutes / baseMinutes), 2.0)` (capped at 2×)
- `deltaThreshold = 0.02` (default)
- `slopeThreshold = 0.05` (default)

### Exit (source-reported)

- **Take-profit**: distance = 1.5 × ATR (default ATR period 14, multiplier 1.5)
- **Stop-loss**: distance = max(ATR × 1.5, 0.5 points)
- Risk-reward ratio locked at 1:1.5

### Re-entry (source-reported)

After a take-profit exit, if a strong opposite signal appears within 3 bars, the strategy reverses position. This is the "reversal re-entry" mechanism.

### Holding period

Not explicitly specified as a maximum; positions are held until take-profit or stop-loss triggers.

### Position sizing

Not specified in the source. The strategy page shows 100% equity allocation in the backtest header, but no position-sizing logic is described in the strategy documentation.

### Parameters (defaults from source)

| Parameter | Default | Description |
|-----------|---------|-------------|
| RSI period | 14 | RSI lookback window |
| RSI MA period | 5 | MA applied to weighted RSI |
| MA type | EMA | Moving average type |
| Log weight | true | Use logarithmic weighting |
| Base minutes | 15.0 | Reference timeframe for weighting |
| Chart time effect ratio | 2.0 | Multiplier for chart-timeframe weight |
| Slope threshold | 0.05 | Minimum slope for signal |
| Delta threshold | 0.02 | Minimum momentum Delta |
| Re-entry window | 3 bars | Window for reversal re-entry after TP |
| ATR period | 14 | ATR lookback |
| ATR multiplier | 1.5 | Stop-loss distance in ATR units |
| Min ATR distance | 0.5 | Floor for stop-loss distance |

## Required data

- **Instruments**: Any cryptocurrency perpetual (tested on ETH/USDT per source)
- **Venue**: Binance Futures (per source backtest configuration)
- **Market type**: USDT-margined perpetual futures
- **Timeframe**: Configurable; default backtest on 1-hour
- **Multi-timeframe data**: 5-minute, 15-minute, 1-hour, 4-hour, and daily OHLCV
- **Fields**: OHLCV (close, high, low, open, volume)
- **Heikin Ashi option**: Optional HA mode uses computed HA candles
- **Source mode options**: Close, OHLC4, HL2, HLC3
- **Timestamp**: Standard exchange timestamps; alignment to timeframe boundaries required for multi-timeframe computation

## Execution assumptions

- **Signal-to-order timing**: Signal evaluated at bar close; order submitted at next bar open (research-proposed assumption; source does not specify)
- **Fill model**: Not specified; assumed market order
- **Fees**: Source backtest header shows default commission settings; specific fee assumptions not documented
- **Slippage**: Not explicitly modeled in source documentation
- **Spread / impact / funding**: Not modeled
- **Leverage**: Strategy shows leverage configuration option but default is 1x
- **Capacity**: Not discussed; strategy is designed for individual traders

## Evidence

### Source-reported

The source reports the following backtest results (from the strategy page; specific numbers are not independently verifiable):

- Maximum drawdown controlled within 8% (source claim)
- Reversal re-entry contributes approximately 20% of additional returns (source claim)
- Multi-timeframe fusion reduces false signals by approximately 40% compared to single RSI (source claim)
- Dynamic thresholds improve signal quality by 25% over fixed thresholds (source claim)
- HA mode reduces false breakout signals by approximately 30% (source claim)

These are all source-reported claims from the strategy page author. The source does not provide a peer-reviewed paper, formal methodology document, or independently audited backtest results. The specific percentage claims (40%, 25%, 30%, 20%) are not traceable to any table, figure, or formal backtest report.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source itself warns: "oscillating markets perform poorly, consecutive stop-loss risk is high"
- The source warns: "multi-timeframe calculation increases strategy complexity, requires sufficient historical data"
- The source warns: "reversal re-entry may cause double losses during false breakouts"
- The source warns: "historical backtests do not guarantee future returns; live performance may differ"
- No formal walk-forward or out-of-sample validation is documented
- The source provides no transaction-cost-adjusted results

## Falsification plan

1. **Backtest replication**: Reproduce the strategy on ETH/USDT with the exact default parameters and the same backtest window (2025-01-01 to 2025-09-24). Research-defined failure threshold: if the replicated Sharpe ratio is ≤ 0 after accounting for realistic fees (5 bp taker one-way), the signal has no standalone edge.
2. **Parameter perturbation**: Vary slopeThreshold (0.03–0.07), deltaThreshold (0.01–0.03), and ATR multiplier (1.0–2.0) to test robustness. If optimal parameters are isolated in a narrow region, the strategy is likely overfitted.
3. **Out-of-sample test**: Run on post-2025-09-24 data (or a different asset like BTC/USDT) to test generalization.
4. **Single-timeframe ablation**: Remove the multi-timeframe weighting and test with chart-timeframe RSI only. If performance does not degrade, the multi-timeframe component adds no value.
5. **Slope-only vs. slope+Delta**: Test entry signals without the Delta confirmation. If false positive rate does not increase, the Delta filter adds no value.
6. **Regime breakdown**: Separate trending vs. ranging market periods. The source acknowledges poor performance in ranging markets; quantify this.
7. **HA mode ablation**: Compare HA mode vs. raw OHLC mode. If HA mode does not materially improve risk-adjusted returns, the smoothing adds complexity without benefit.

## Crypto portability

**Direct**

The strategy is designed for and tested on cryptocurrency perpetual futures. The multi-timeframe approach, ATR-based risk management, and Heikin Ashi smoothing are all crypto-native in their current form.

Crypto-specific considerations:
- 24/7 trading means the daily timeframe has no overnight gap; multi-timeframe alignment is continuous
- Funding rate is not modeled; positions held through funding settlement times incur additional cost
- High volatility in crypto may cause frequent stop-loss hits; the minimum ATR distance (0.5 points) may need adjustment for low-price assets
- Venue fragmentation: strategy is tested on Binance only; cross-venue replication untested
- The logarithmic weighting scheme is timeframe-agnostic and should transfer to any market with sufficient data

## Limitations

- **Not independently reproduced**
- **Source-quality**: FMZ community strategy, not a peer-reviewed paper or formal research publication. The specific performance claims (40% reduction, 25% improvement, etc.) are not backed by auditable backtest reports
- **No formal backtest report**: The strategy page shows a backtest header but no detailed performance metrics (Sharpe, Sortino, win rate, profit factor, etc.)
- **No transaction-cost analysis**: Fees, slippage, and funding are not modeled in the documented results
- **Parameter sensitivity unknown**: The source provides default parameters but no parameter sensitivity analysis
- **Overfitting risk**: The backtest window (9 months) is short; the strategy has multiple tuning parameters (RSI period, MA period, slope threshold, delta threshold, ATR multiplier, chart effect ratio, re-entry window)
- **Underspecified**: Position sizing, maximum holding period, overlap handling (what happens if a new signal appears while a position is open), and the interaction between the re-entry mechanism and the primary signal are not fully specified
- **Source does not provide walk-forward or cross-validation results**
- **Working-product risk**: The strategy is a community contribution to FMZ, not a formal research contribution

## Implementation status

`not-implemented`

No implementation in our research stack. The source provides a complete Pine Script implementation on FMZ, but no PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed in our system.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in this repository does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

The strategy is a community-contributed technical indicator combination strategy with source-reported backtest results that have not been independently verified. The specific performance improvement claims are not traceable to auditable evidence.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted in this Scout cycle.

Related strategy-pool records include:
- `tradingview-ema-slope-rsi-ntz-momentum-2026-09-18.md` — EMA-slope RSI oscillator strategy; distinct source and mechanism (single-timeframe EMA slope + RSI oscillator, not multi-timeframe weighted slope)
- `visibility-graphs-relative-strength-index-multitimeframe-momentum-2026-09-02.md` — Visibility-graphs RSI with multi-timeframe approach; distinct mechanism (graph-theoretic, not slope-based)

## Sources

1. FMZ strategy 509733, "Time-Based Slope & Delta RSI Strategy (HA & Source Selectable)". https://www.fmz.com/strategy/509733. Created 2025-09-25; full Pine Script v5 source code and strategy description available on the public page. Reviewed 2026-09-18.
