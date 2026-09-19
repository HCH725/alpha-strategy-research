---
schema: strategy-research-record-v1
title: TradingView Aggregated Long/Short Ratio + OI Crowding Reversal
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://www.tradingview.com/script/yy8LZXNr/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Aggregated Long/Short Ratio + OI Crowding Reversal

## Provenance

- Public TradingView open-source indicator: **Aggregated Long Short Ratio (Binance + Bybit)** by `carlosbucci`.
- Stable source URL: https://www.tradingview.com/script/yy8LZXNr/
- TradingView publication date shown by the public page: 2025-10-17.
- Source reviewed as of 2026-09-20.
- The source describes Binance and Bybit long/short-ratio series, their aggregate average, configurable timeframe, explicit extreme zones, and an Open Interest confirmation rule.

## Economic mechanism

### Source-reported

The author treats the long/short ratio (LSR) as a positioning/sentiment measure: values above 1 indicate more long than short accounts and values below 1 indicate the reverse. The source marks LSR above 1.5 as very bullish / a possible market-top condition and below 0.5 as very bearish / a possible market-bottom condition. It explicitly says LSR should be analyzed together with Open Interest (OI): rising OI strengthens the positioning signal, while extreme LSR with falling OI should be ignored. The source also describes price/LSR divergences with rising OI as potential reversal setups and recommends perpetual-futures charts.

### Research interpretation

Falsifiable hypothesis: **cross-venue account-positioning crowding may contain incremental reversal information when the crowd is extreme and leverage is still being added, while the same LSR extreme with contracting OI should contain less information.**

The mechanism is behavioral/positioning rather than mechanical arbitrage. An extreme account ratio can proxy one-sided crowding; rising OI can distinguish active leverage accumulation from simple position closure. If crowded positioning is vulnerable to forced exits or failed continuation, subsequent price rejection may be followed by reversal. This interpretation is unverified and must compete against the alternative that extreme LSR simply accompanies persistent trends.

The cross-venue aggregation is itself testable: averaging Binance and Bybit may reduce venue-specific noise, but it may also destroy useful venue-specific information.

## Signal

### Source-specified observations

- LSR = 1.0: balanced long/short accounts.
- LSR > 1.5: source-defined high/extreme-long zone and possible top condition.
- LSR < 0.5: source-defined low/extreme-short zone and possible bottom condition.
- Source reversal setup: extreme LSR + rising OI + price rejection.
- Source trend setup: LSR trending with price + steadily rising OI.
- Source caution: extreme LSR + falling OI => ignore the signal.
- Source divergence examples:
  - price higher highs + falling LSR + rising OI => bearish divergence;
  - price lower lows + rising LSR + rising OI => bullish divergence.
- Source says higher timeframes such as 4h and 1D are more reliable, but provides no independently verified evidence for that claim.

### Research-proposed operationalization

For later testing only, not source-reported trading rules:

1. Treat Binance LSR, Bybit LSR, and their source-described average as three separate candidate features.
2. Define an event only after the relevant bar closes; do not use future OI, future price rejection, or future LSR observations to label the event bar.
3. Test source thresholds 1.5 and 0.5 separately from leakage-safe rolling percentile alternatives. Percentile thresholds are `research-proposed`, not source-reported.
4. Test two competing outcomes after an extreme with rising OI: reversal versus continuation. Do not assume the author's reversal interpretation is correct.
5. Test divergence conditions separately from simple level extremes; do not merge them into one optimized composite unless each component survives ablation.

Exact entry timing, rejection definition, OI-rise threshold, exit, holding period, re-entry, stop, sizing, and leverage are **underspecified** by the source.

## Required data

- Crypto perpetual-futures instruments; source specifically describes USDT perpetual charts.
- Binance long/short ratio account series.
- Bybit long/short ratio account series.
- Open Interest aligned to the same instrument/timeframe and venue definition used in each test.
- OHLCV for price reaction, divergence, and baseline construction.
- Source-supported timeframes include configurable chart timeframe; 4h and 1D are specifically recommended by the author.
- All LSR and OI observations must be timestamped point-in-time and available before signal formation.
- Venue/API history, symbol changes, missing values, and revisions require explicit handling; the source notes that data availability depends on exchange/API support and that unavailable data may appear as NA.

## Execution assumptions

The source is an indicator, not a complete execution specification. Market/limit order choice, signal-to-order delay, same-bar versus next-bar fill, fees, spread, slippage, impact, funding, leverage, margin, liquidation handling, latency, partial fills, and capacity are **underspecified**.

A later backtest should form the signal only from data known at bar close and use a separately declared executable fill model. Funding and transaction costs are material for perpetual-futures implementation.

## Evidence

### Source-reported

The TradingView page describes the threshold and confluence logic above and recommends using LSR together with OI. It does not provide a traceable backtest, Sharpe ratio, CAGR, drawdown, statistical significance, or other independently auditable performance result.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-backed performance validation was found on the reviewed TradingView page. The source itself warns against using LSR without OI context and says extreme LSR with falling OI should be ignored. No independent evidence was reviewed establishing that the stated 1.5 / 0.5 thresholds are stable across assets, venues, or regimes. Absence of additional negative evidence is not evidence of no negative result.

## Falsification plan

1. Reconstruct point-in-time Binance and Bybit LSR plus OI without forward filling across unavailable periods.
2. Test source thresholds (1.5 / 0.5) before any alternative threshold search.
3. Compare next-period returns after extreme-LSR + rising-OI events with matched unconditional, volatility, momentum, and OI-only controls.
4. Test reversal and continuation as competing hypotheses over fixed horizons; reject a directional story if signs are unstable across horizons or regimes.
5. Ablate `LSR only -> OI only -> LSR + OI -> LSR + OI + price rejection/divergence`.
6. Compare Binance-only, Bybit-only, equal-weight aggregate, and leave-one-venue-out variants. Aggregation must add out-of-sample information to justify itself.
7. Compare fixed source thresholds against `research-proposed` trailing-percentile normalization using only past observations.
8. Separate 4h and 1D results rather than pooling them; include high/low volatility and bull/bear regimes.
9. Apply realistic fees, spread, slippage, and funding to any executable derivative implementation.
10. Require untouched out-of-sample or walk-forward confirmation. Material weakening occurs if the interaction adds no incremental predictive value over price/OI baselines, flips sign repeatedly, depends on one venue/regime, or disappears after costs.

## Crypto portability

**direct** — the source is explicitly designed for cryptocurrency perpetual futures and uses Binance/Bybit positioning data.

Portability is nevertheless venue-dependent. Binance and Bybit may define long/short account ratios differently; account ratios are not position-size ratios, and venue clientele can differ. 24/7 candle boundaries, contract changes, missing historical metrics, funding, and venue fragmentation must be normalized before comparison.

## Limitations

- Not independently reproduced.
- Source provides indicator logic and heuristic interpretations, not validated alpha evidence.
- Entry, exit, holding period, rejection definition, OI confirmation threshold, sizing, and execution model are underspecified.
- LSR measures account positioning rather than necessarily notional exposure; a large account and a small account need not contribute proportionally.
- Equal-weight cross-venue aggregation may mix non-equivalent definitions or client populations.
- Fixed 1.5 / 0.5 thresholds may be regime- and venue-dependent.
- Divergence rules require point-in-time definitions to avoid discretionary hindsight.

## Implementation status

Research capture only. No implementation or backtest in the quantitative research stack has been completed for this record.

## Adoption boundary

This record is external research material only. It is not evidence of profitable alpha and is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- `carlosbucci`, **Aggregated Long Short Ratio (Binance + Bybit)**, TradingView open-source indicator, published 2025-10-17; reviewed 2026-09-20: https://www.tradingview.com/script/yy8LZXNr/
