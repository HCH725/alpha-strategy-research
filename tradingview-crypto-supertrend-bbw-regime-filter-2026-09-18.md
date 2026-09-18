---
schema: strategy-research-record-v1
title: Crypto SuperTrend with BBW regime filter
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/9x9ohJ2R-santoshpsiii-Crypto-Algo/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto SuperTrend with BBW regime filter

## Provenance

Primary source: public TradingView open-source strategy page, `@santoshpsiii Crypto Algo`, by `smvdtravelsolutions`.

Stable URL: https://www.tradingview.com/script/9x9ohJ2R-santoshpsiii-Crypto-Algo/

TradingView page date shown at source review: May 19. Source reviewed 2026-09-18. The page identifies the script as open source and describes it as designed for high-volatility crypto markets including BTC, ETH, and major altcoins.

## Economic mechanism

### Source-reported

The author combines SuperTrend direction with a Bollinger Band Width (BBW) regime filter. BBW compression is used to identify flat/choppy conditions; directional entries are allowed only when BBW indicates a trending state. The stated intent is to suppress trend-following trades during sideways regimes.

### Research interpretation

Falsifiable hypothesis: SuperTrend direction changes may have better continuation expectancy when volatility has expanded out of a compressed regime than when the same direction changes occur during low-volatility chop. BBW is therefore a regime gate rather than the primary directional alpha signal.

Component roles:

- Regime: BBW relative to its base moving average.
- Primary signal: current-timeframe SuperTrend direction flip.
- Exit/reversal: opposite SuperTrend direction shift.
- Multi-timeframe SuperTrend states: source describes a 5m/15m/1h/4h dashboard, but does not state that all dashboard timeframes are entry requirements.

## Signal

Source-reported normalized logic:

- Long entry: market is in the source-defined `TRENDING` state (`BBW > Base MA`) and current SuperTrend flips bullish.
- Short entry: market is in `TRENDING` state and current SuperTrend flips bearish.
- Exit: close/reverse when the core SuperTrend direction shifts.
- Source describes 5-minute and 15-minute charts as optimized usage and BTCUSDT/ETHUSDT and other high-volatility crypto pairs as intended instruments.

Underspecified by the reviewed source description: exact BBW formula inputs, Base MA type and length, SuperTrend ATR period/factor, exact bar-close/intrabar signal semantics, pyramiding/re-entry behavior, and whether higher-timeframe dashboard states constrain entries. These are not inferred here.

## Required data

Source-supported minimum data: OHLCV bars sufficient to calculate SuperTrend and Bollinger Band Width on crypto instruments. The source describes BTC, ETH, and major altcoins and emphasizes 5m/15m use.

For exact reconstruction, indicator parameter values and timestamp semantics remain a data/ specification gap. Venue and spot-versus-perpetual market type are not fixed by the reviewed source description.

## Execution assumptions

The source reports automated buy/close-long/sell-short/close-short webhook alerts and reversal on SuperTrend direction changes, but does not fully specify order type, fill timestamp, fees, spread, slippage, market impact, leverage/margin, funding, latency, partial fills, or failure handling.

Any later backtest must define these explicitly. A next-bar execution convention would be `research-proposed`, not source-reported.

## Evidence

### Source-reported

The source describes the strategy architecture and intended crypto/timeframe use but the reviewed page does not provide a sufficiently traceable performance statistic that is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed source; absence is not evidence of no negative result. Trend-following reversal systems are structurally vulnerable to repeated direction flips, and the incremental value of the BBW gate remains unverified.

## Falsification plan

Test the normalized source hypothesis on liquid crypto instruments with point-in-time OHLCV. Compare:

1. SuperTrend flips without a BBW gate.
2. SuperTrend flips gated by the source-described BBW trending state.

Ablate the BBW component and stratify results by volatility regime, instrument, and 5m versus 15m horizon. Include realistic fees, spread/slippage, and perpetual funding where applicable. The hypothesis is weakened if the BBW gate does not improve out-of-sample risk-adjusted performance or materially reduce whipsaw/cost burden relative to the ungated SuperTrend baseline. Exact numeric acceptance thresholds are intentionally not invented here and would be `research-defined falsification threshold` in a downstream experiment specification.

## Crypto portability

direct

The source explicitly targets crypto. Portability still depends on venue-specific OHLCV, 24/7 candle boundaries, liquidity, spot-versus-perpetual differences, and funding/mark-index accounting for perpetuals.

## Limitations

- Not independently reproduced.
- Exact indicator parameters are underspecified in the reviewed source description.
- Higher-timeframe dashboard states are described but their role in entry logic is underspecified.
- Execution and transaction-cost assumptions are underspecified.
- Source claims of filtering bad/choppy trades are a thesis, not independently verified evidence.

## Implementation status

Not implemented in the research stack. No backtest or runtime changes were performed by this Scout.

## Adoption boundary

Research-only. Presence in this repository does not imply validated alpha, profitability, implementation approval, paper/testnet approval, or live-trading approval.

## Related Wiki records

None linked; no stable related Wiki record was established during this GitHub-only Scout run.

## Sources

- TradingView, `@santoshpsiii Crypto Algo`, `smvdtravelsolutions`: https://www.tradingview.com/script/9x9ohJ2R-santoshpsiii-Crypto-Algo/ (public open-source strategy page; reviewed 2026-09-18).
