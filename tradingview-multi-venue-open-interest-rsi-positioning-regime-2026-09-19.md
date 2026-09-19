---
schema: strategy-research-record-v1
title: Multi-Venue Open-Interest RSI Positioning Regime
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/vHlNouol-Open-Interest-RSI-BackQuant/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Multi-Venue Open-Interest RSI Positioning Regime

## Provenance

Public TradingView open-source indicator/research page **Open Interest RSI [BackQuant]**, author/page identity `BackQuant`, initially published 2025-12-07 and shown as updated 2025-12-08. Stable source: https://www.tradingview.com/script/vHlNouol-Open-Interest-RSI-BackQuant/ . Source reviewed as of 2026-09-19.

The source describes aggregation of futures open interest across Binance, Bybit, OKX, Bitget, Kraken, HTX and Deribit, including multiple contract suffixes, followed by normalization to COIN or approximate USD notional and an RSI transform of the aggregated OI close.

## Economic mechanism

### Source-reported

The author frames the oscillator as a measure of positioning pressure, crowding and leverage-flow mean reversion rather than price momentum. High OI RSI is described as aggressive OI expansion/crowding; low OI RSI as aggressive deleveraging or position closure. The page explicitly presents both trend and mean-reversion interpretations rather than asserting one universal direction.

### Research interpretation

The falsifiable hypothesis is that the **rate and persistence of change in aggregate cross-venue derivatives positioning** contains incremental information about subsequent crypto returns or volatility beyond price momentum and raw single-venue OI.

Two competing mechanisms must be tested rather than assumed:

1. **Continuation / participation:** elevated or rising aggregate OI RSI confirms that fresh leverage is joining a price move, increasing short-horizon continuation probability.
2. **Crowding / mean reversion:** extreme aggregate OI RSI marks crowded leverage, increasing subsequent squeeze or reversal risk; very low OI RSI may mark deleveraging exhaustion and later re-risking.

The multi-venue aggregation is the material data dependency: if it does not improve on a Binance-only or other single-venue OI RSI, the aggregation thesis is not supported.

## Signal

Source-supported construction:

- Build synthetic OI OHLC by requesting available OI streams across Binance, Bybit, OKX, Bitget, Kraken, HTX and Deribit and multiple contract suffixes for the same underlying.
- Normalize streams either to COIN units or approximate USD notional; in USD mode coin OI is multiplied by price before aggregation.
- Sum OI open/high/low/close across included venue-contract streams.
- Compute RSI on aggregated OI close using a configurable `Calculation Period`.
- Apply configurable SMA smoothing (`Smoothing Period`) to OI RSI.
- Optionally apply a configurable EMA to the smoothed OI RSI.
- Midpoint is typically 50; source examples use extreme upper/lower levels of 80/20, but these are user-configurable rather than asserted universal optima.
- Source-supported observable events include bullish/bearish midpoint crosses, entry/exit of upper/lower extreme zones, and OI-RSI/EMA relative state.

The source does **not** specify one canonical trade entry/exit system, holding period, re-entry rule or position sizing rule. Any mapping from these states into positions is therefore `research-proposed`, not source-reported.

Research-proposed tests should separately evaluate: midpoint-regime continuation, extreme-zone continuation, extreme-zone contrarian response, and OI-RSI/EMA crossover. Do not combine these into a composite before individual ablation.

## Required data

- Crypto derivatives/futures open interest for the same underlying across supported venues.
- Source-supported venues: Binance, Bybit, OKX, Bitget, Kraken, HTX and Deribit.
- Multiple perpetual/futures contract suffixes may be required, including USDT-, USD- and USDC-linked contracts where available.
- Price series is required when converting coin-denominated OI to approximate USD notional and for testing forward returns.
- Timestamp alignment across venues is essential; venue feeds must be point-in-time available at signal formation.
- Timeframe is configurable/underspecified by the source.
- Missing venue-contract streams must be handled without using future availability information.

## Execution assumptions

The source is an indicator, not a complete execution specification. Signal-to-order timing, same-bar versus next-bar execution, order type, fees, spread, slippage, funding, impact, leverage, margin, latency and partial fills are underspecified.

For research, signals should be formed only from information available at the completed observation timestamp, with any tradable implementation executed no earlier than the next causally available price. This is `research-proposed`.

## Evidence

### Source-reported

The TradingView page explains the construction and qualitative interpretations but does not provide a source-traceable Sharpe ratio, CAGR, drawdown, win rate or other independently auditable performance statistic for a canonical trading rule. No performance precision is inferred here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative backtest was identified on the reviewed page; absence is not evidence of no negative result. The page itself presents both trend and mean-reversion readings of extremes, which means directional interpretation is empirically unresolved rather than established.

## Falsification plan

1. Reconstruct point-in-time aggregate OI RSI without future venue availability or timestamp leakage.
2. Test COIN-normalized and USD-notional variants separately.
3. Compare multi-venue aggregate OI RSI against single-venue baselines (especially Binance) and raw aggregate OI change.
4. Compare against price RSI and simple price-momentum baselines to determine whether the OI transform contributes incremental information.
5. Test continuation and contrarian hypotheses separately across midpoint states, 80/20-style extremes, and OI-RSI/EMA crosses; do not select direction after inspecting the full sample without OOS confirmation.
6. Use walk-forward/OOS evaluation across BTC, ETH and a broader liquid-perpetual cohort, with bull, bear, high-volatility and low-volatility regimes separated.
7. Measure forward returns and forward realized volatility at multiple predeclared horizons rather than forcing one holding period.
8. Ablate venues one at a time and test stable venue subsets to determine whether apparent alpha is dominated by one exchange or changing data coverage.
9. Apply realistic fees, spread, slippage and funding to any tradable operationalization.
10. Reject or materially weaken the hypothesis if aggregate OI RSI has no stable OOS incremental predictive value over single-venue OI and price-only baselines, if sign flips are unstable across regimes, or if results depend materially on look-ahead venue coverage or a narrow parameter island.

## Crypto portability

direct

The source is explicitly built from crypto derivatives OI. Portability still depends on venue fragmentation, contract denomination, symbol mapping, changing exchange coverage, perpetual-versus-dated-futures composition, funding, and synchronized candle boundaries. USD normalization using contemporaneous price also requires careful point-in-time handling.

## Limitations

- Not independently reproduced.
- No canonical trading rule is specified; entry, exit and holding horizon are underspecified.
- Calculation Period, smoothing length and EMA length are configurable and no universal defaults are established by the reviewed description.
- 80/20 extreme levels are presented as examples/configurable thresholds, not validated optima.
- Aggregating heterogeneous venue contracts can mix contract specifications and participant populations.
- USD conversion can mechanically couple OI notional to price, potentially creating spurious apparent association with price momentum.
- Historical exchange/symbol availability can create survivorship or coverage bias unless reconstructed point-in-time.

## Implementation status

Research-only external material. No implementation or validation in our quantitative research stack has been completed.

## Adoption boundary

This record is normalized research material only. It is not evidence of profitable alpha and is not approved for implementation, paper trading, testnet, live trading, leverage or capital allocation.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- BackQuant, **Open Interest RSI [BackQuant]**, TradingView public open-source script/research page, published 2025-12-07, updated 2025-12-08, reviewed 2026-09-19: https://www.tradingview.com/script/vHlNouol-Open-Interest-RSI-BackQuant/
