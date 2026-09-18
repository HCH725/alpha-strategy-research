---
schema: strategy-research-record-v1
title: TradingView OBV Price-Containment Leading Breakout
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
  - https://www.tradingview.com/script/dQV3MQCV/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView OBV Price-Containment Leading Breakout

## Provenance

Public TradingView open-source indicator `OBV Breakout Screener (By Tarso)` by `tulyodetarso`. Stable source: https://www.tradingview.com/script/dQV3MQCV/ . TradingView shows original publication 2025-08-11 and an update on 2026-04-13. Source reviewed 2026-09-18.

The current public description explicitly notes that v3 corrected self-referencing bias by comparing both OBV and price against prior-bar lookback levels rather than levels that include the current bar.

## Economic mechanism

### Source-reported

The author describes a bullish setup in which On-Balance Volume breaks its recent high while price remains below its own recent high. The intended interpretation is that volume-based buying pressure is leading price before a subsequent price breakout. The updated filtered signal can additionally require sufficient average volume and price above a 50-period SMA.

### Research interpretation

Hypothesis: a point-in-time divergence where cumulative signed volume (OBV) reaches a new lookback high before price does may identify latent accumulation or participation pressure that can precede an upside price breakout. Price containment distinguishes the signal from an already-realized price breakout; the optional SMA filter is a trend-regime gate and the liquidity filter is primarily a tradability/quality constraint rather than alpha by itself.

The causal claim that this represents `smart money` is not established by the source and is not adopted here. The falsifiable object is simply whether OBV-leading-price states have positive forward-return or breakout-probability information after costs and controls.

## Signal

Source-specified normalized logic:

- Default lookback: 20 periods; configurable, with 50 given as an example alternative.
- OBV breakout: current OBV exceeds its lookback high, with the current public v3 description specifying comparison against the previous-bar lookback level to avoid self-reference.
- Price containment: price has not broken its corresponding recent high; v3 likewise uses a prior-bar comparison level.
- Raw advanced-breakout state: OBV breakout is true while price breakout is false.
- Price breakout method is selectable between `Close` (default) and `High`.
- Optional/filtered quality conditions include minimum 20-day average volume (source default 500K) and price above SMA(50).
- Source recommends Daily (1D) for its stock-screening setup, while the Pine Screener workflow can select other timeframes such as 4h or 1h.

This source is an indicator/screener, not a complete order-execution strategy. Entry timing after a qualifying state, exit logic, holding period, re-entry, short logic, sizing, and trade-management rules are underspecified. Any later conversion of the signal into orders must be labeled research-proposed and tested separately.

## Required data

- OHLCV sufficient to calculate price lookback highs, OBV, average volume, and optional SMA(50).
- Point-in-time bars with the current bar excluded from the historical comparison window as described by the v3 correction.
- Timeframe is configurable; source recommends 1D for the stated screening setup.
- The source describes use with stock, Crypto, or Forex screeners, but its stated minimum-volume default is stock-oriented and must not be assumed portable across crypto venues or quote units.
- For crypto research, venue, pair, spot/perpetual market type, quote currency, candle boundary, and volume definition must be fixed before testing.

## Execution assumptions

The source does not specify a trade execution model. Market versus limit orders, signal-to-order timing, next-bar versus same-bar fills, fees, spread, slippage, impact, capacity, funding, leverage, margin, shorting, latency, partial fills, and failure handling are underspecified.

For causal research, the signal should only become actionable after all data used by the qualifying bar are available; any later executable strategy requires an explicit fill convention.

## Evidence

### Source-reported

The TradingView page describes the signal construction and screening workflow but does not provide independently auditable performance statistics in the reviewed public description. It states that OBV-leading-price is intended to identify potential opportunities before a possible upward move; this is a source hypothesis, not verified profitability evidence.

The 2026-04-13 update explicitly reports correction of a self-referencing comparison bug in prior versions and adds the price-method selector, volume filter, SMA(50) trend filter, and separate raw/filtered screener outputs.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself documents that earlier versions had self-referencing bias because the current bar was included in the comparison high. This is material negative implementation evidence and makes strict point-in-time reconstruction mandatory.

No independent negative performance study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Reconstruct OBV and price lookback levels strictly from information available before the signal comparison, reproducing the v3 prior-bar convention.
2. Test the raw state `OBV new lookback high AND price not new lookback high` against matched controls with similar trend, volatility, liquidity, and recent returns.
3. Measure both forward returns and probability/time-to subsequent price breakout over predeclared horizons rather than selecting the best horizon ex post.
4. Run ablations for raw signal versus SMA(50) regime filter versus liquidity filter; do not attribute filter effects to OBV.
5. Test multiple crypto cohorts and market regimes with an untouched out-of-sample segment. Predeclare any lookback alternatives rather than optimizing freely.
6. Include realistic fees, spread and slippage in any executable translation. For perpetuals, include funding where the holding horizon makes it material.
7. Reject or materially weaken the hypothesis if the OBV-leading state does not outperform matched controls out of sample, if the effect disappears after costs, or if results depend narrowly on one venue, lookback, timeframe, or bull regime.

## Crypto portability

unproven

The source says the screener can be used with Crypto, but the reviewed description does not present crypto-specific empirical validation. Crypto volume is fragmented across venues, OBV is therefore venue-dependent, perpetual volume can differ structurally from spot volume, and 24/7 candle boundaries can change lookback extrema. The source's absolute average-volume threshold is not directly portable across quote currencies or exchanges.

A crypto implementation should treat the core OBV/price divergence as a ported hypothesis and specify venue, instrument type, volume field, timezone/candle boundary, and any liquidity normalization before testing.

## Limitations

- Not independently reproduced.
- No source-reported auditable performance statistics were used.
- Complete trading entry/exit and holding rules are underspecified because the source is a screener/indicator.
- The source's behavioral language about buying pressure or `smart money` is interpretive rather than demonstrated causal evidence.
- Prior versions had a documented self-referencing bias; only the corrected point-in-time convention is suitable for research.
- Crypto portability is unproven and volume fragmentation is a material data dependency.

## Implementation status

Not implemented in the research stack. No backtest, reproduction, paper trading, testnet, or live validation was performed during this Scout cycle.

## Adoption boundary

Research material only. Presence in this repository does not mean the signal is profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

None linked; no stable related Hermes Wiki Brain record was resolved within this GitHub-only Scout boundary.

## Sources

- TradingView — `OBV Breakout Screener (By Tarso)` by `tulyodetarso`: https://www.tradingview.com/script/dQV3MQCV/ (public open-source page; source reviewed 2026-09-18).
