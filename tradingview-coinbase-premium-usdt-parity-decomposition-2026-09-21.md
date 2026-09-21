---
schema: strategy-research-record-v1
title: Coinbase Premium Decomposition: U.S. Spot Demand vs USDT/USD Parity
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-21
sources:
  - https://www.tradingview.com/script/hAyQ6OLi-BTC-Coinbase-Premium/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coinbase Premium Decomposition: U.S. Spot Demand vs USDT/USD Parity

## Provenance

Public TradingView open-source script **BTC Coinbase Premium** by `traderview2`. Stable source: https://www.tradingview.com/script/hAyQ6OLi-BTC-Coinbase-Premium/ . TradingView shows initial publication 2024-08-11 and update 2025-01-10. Source reviewed as of 2026-09-21.

The 2025-01-10 release note materially revises the interpretation of the displayed Coinbase-versus-Binance price difference: the author argues that the apparent BTC Coinbase premium can substantially reflect the USDT/USD quote-currency relationship rather than uniquely identifying Coinbase-led BTC demand.

## Economic mechanism
### Source-reported

The script compares Coinbase BTCUSD with Binance BTCUSDT. The original description presents a positive Coinbase premium as associated with bullish BTC strength and a negative premium with weakness. The 2025-01-10 update explicitly cautions that this apparent premium can instead be driven by USDT/USD parity: changes in the dollar value of USDT mechanically alter the BTCUSDT quote relative to BTCUSD.

### Research interpretation

This creates a falsifiable decomposition hypothesis rather than a simple directional indicator. The raw Coinbase-minus-Binance premium may contain at least two economically different components:

1. venue-specific U.S. spot demand/supply imbalance; and
2. quote-currency basis caused by USDT deviating from USD parity.

A residual premium that remains after controlling for contemporaneous USDT/USD could contain more venue-specific information than the raw spread. Conversely, if USDT/USD explains the raw premium and its apparent predictive power, the common interpretation of the spread as U.S. institutional demand should be rejected.

Any residualization rule, threshold, horizon, entry or exit described below is `research-proposed`, not source-reported.

## Signal

**Source-supported observable:** percentage or price difference between Coinbase BTCUSD and Binance BTCUSDT. The source does not specify a complete systematic trading rule.

**Research-proposed test:** construct the raw cross-venue premium and contemporaneous USDT/USD deviation from 1.00 using synchronized point-in-time observations. Estimate a trailing-only relationship between the raw premium and USDT parity, then define a residual premium using only coefficients available at the signal timestamp.

Competing hypotheses:

- **Venue-demand continuation:** unusually positive residual premium predicts positive subsequent BTC returns; unusually negative residual premium predicts negative subsequent returns.
- **Temporary-dislocation reversion:** extreme residual premium mean-reverts and predicts the opposite sign after the venue imbalance dissipates.
- **Null / quote-currency explanation:** raw premium has no incremental predictive content after USDT/USD and broad BTC return controls.

Lookback, residual threshold, holding horizon, re-entry rule and position sizing are **underspecified** by the source and must be selected only under a leakage-safe research protocol.

## Required data

- BTCUSD spot prices from Coinbase.
- BTCUSDT spot prices from Binance.
- Point-in-time USDT/USD price from an independent USD venue or defensible composite.
- Synchronized timestamps at a common sampling frequency.
- Bid/ask or spread data if executable cross-venue economics are tested.
- Venue availability/outage flags and missing-data handling.
- 24/7 timestamp convention and explicit candle-boundary alignment.

Historical symbols and venue feeds must be point-in-time valid. No present-day symbol mapping should silently rewrite historical availability.

## Execution assumptions

The source does not provide a complete execution model, order type, fees, spread, slippage, latency, transfer assumptions, capacity model or position sizing.

For directional predictive tests, signal values must be formed only after all component prices for the timestamp are observable and execution should occur no earlier than the next executable observation. For any arbitrage interpretation, both legs, venue-specific fees, latency, inventory, transfer constraints and quote-currency conversion costs must be modeled explicitly. These are research requirements, not source claims.

## Evidence
### Source-reported

The source states that traders have associated strong Coinbase premium with BTC bullish strength and strong discount with weakness, but it provides no traceable backtest statistic, Sharpe, CAGR, drawdown or win rate. Its 2025-01-10 release note provides the important counter-interpretation that the BTCUSD-versus-BTCUSDT difference can be driven by USDT/USD parity.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself supplies material negative evidence against a naive interpretation: the author later identifies quote-currency parity as a mechanical confounder. No independently verified performance evidence was identified in the reviewed source.

## Falsification plan

1. Compare a BTC return baseline against raw Coinbase premium, USDT/USD deviation alone, and USDT-adjusted residual premium.
2. Require rolling or expanding estimation only; never residualize using full-sample coefficients.
3. Test both continuation and reversion hypotheses over multiple predeclared horizons rather than selecting the better sign ex post.
4. Use timestamp-shift placebos to detect asynchronous-feed artifacts.
5. Repeat with bid/ask midpoints where available to test whether the effect survives executable spreads.
6. Segment USDT depeg/stress periods versus normal parity regimes.
7. Test whether the residual survives controls for contemporaneous BTC momentum, volatility and broad crypto-market returns.
8. Where data permit, replace Binance BTCUSDT with alternative USDT venues and Coinbase BTCUSD with another USD venue to separate quote-currency effects from venue identity.
9. Reject the venue-demand hypothesis if residual premium has no stable leakage-safe out-of-sample incremental predictive value after costs and controls. Prefer the simpler USDT-parity explanation if it accounts for the apparent signal.

## Crypto portability

direct

The source is explicitly about Bitcoin spot pricing across Coinbase and Binance. Portability to other crypto assets is unproven and depends on simultaneous liquid USD and USDT markets. Venue fragmentation, stablecoin basis, 24/7 trading, exchange outages, different fee schedules and asynchronous quotes are central rather than incidental risks.

## Limitations

- The source does not define a complete entry/exit strategy.
- Thresholds, horizons and residualization parameters are underspecified.
- Raw close-to-close comparisons may embed stale-quote and candle-alignment artifacts.
- USDT/USD itself can differ across venues; the chosen parity reference can change the decomposition.
- A residual spread is not automatically an executable arbitrage.
- The institutional-demand interpretation is unproven.
- Not independently reproduced.

## Implementation status

Research record only. No implementation in the research stack and no Qlib full-backtest validation has been completed.

## Adoption boundary

This artifact is research-only. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, demonstrated profitable alpha, or received Paper, Testnet or Live approval.

## Related Wiki records

None identified with sufficient certainty from the GitHub-only research context. No Hermes Wiki lookup was performed.

## Sources

- TradingView, `traderview2`, **BTC Coinbase Premium**, public open-source script: https://www.tradingview.com/script/hAyQ6OLi-BTC-Coinbase-Premium/ (published 2024-08-11; updated 2025-01-10; reviewed 2026-09-21).
