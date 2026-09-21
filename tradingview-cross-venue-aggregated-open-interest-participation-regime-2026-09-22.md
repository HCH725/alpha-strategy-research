---
schema: strategy-research-record-v1
title: TradingView Cross-Venue Aggregated Open Interest Participation Regime
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-12-09
sources:
  - https://www.tradingview.com/script/fE2QsHhr-Aggregated-Open-Interest/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Cross-Venue Aggregated Open Interest Participation Regime

## Provenance

Public TradingView open-source indicator **Aggregated Open Interest** by `VisioNBG`, first published 2025-11-17 and updated 2025-12-09. Stable public URL: https://www.tradingview.com/script/fE2QsHhr-Aggregated-Open-Interest/ . Source reviewed as of 2026-09-22.

The source aggregates open-interest data across ten named crypto exchanges: Binance, Bybit, Kraken, MEXC, Bitget, BingX, Coinbase, Deribit, HTX, and Crypto.com. Individual venues can be enabled or disabled. The 2025-12-09 update also added an optional ATR-style histogram and moving average for visualizing the rate of change.

## Economic mechanism

### Source-reported

The source presents aggregated open interest as a market-wide view of outstanding crypto derivatives participation rather than relying on one venue. It displays rising and falling aggregate OI and provides optional rate-of-change visualization. The public description does not claim a complete trading strategy, entry/exit rule, or verified profitability.

### Research interpretation

**Research-proposed hypothesis:** because crypto derivatives positioning is fragmented across venues, aggregate OI may distinguish broad leverage creation/destruction from venue-specific positioning noise. The useful information, if any, should appear as an interaction between price direction and aggregate OI change rather than the OI level alone.

Competing hypotheses must be tested separately rather than selected after observing results:

- price up + aggregate OI up: broad participation expansion may confirm continuation;
- price down + aggregate OI up: broad short/leverage build may confirm downside continuation;
- large aggregate OI contraction during a large price move: deleveraging/liquidation may mark either continuation stress or exhaustion/reversal, so both horizons must be pre-registered and compared;
- disagreement between aggregate OI and the largest single venue may identify venue-local noise, but this is **research-proposed**, not source-reported.

The economic claim is therefore incremental information from cross-venue participation breadth/aggregation, not that high OI is intrinsically bullish or bearish.

## Signal

The source itself is an indicator and does not specify a complete trading lifecycle. The following operationalization is **research-proposed** and must not be attributed to the author:

1. Align point-in-time OI observations across the available venue universe for the same underlying asset and market type.
2. Normalize contract units into a common notional representation before aggregation where raw OI units differ.
3. Compute aggregate OI and lagged changes over pre-registered horizons; do not use future venue observations to fill missing values.
4. Classify joint price/OI states from contemporaneously available bar-close data.
5. Test continuation and post-deleveraging reversal as separate hypotheses over pre-registered forward horizons.
6. Compare aggregate OI against the strongest single-venue OI baseline and simpler price/volume/volatility controls.

No source-supported entry threshold, exit rule, holding period, re-entry rule, position sizing, leverage, stop, or take-profit rule is available. These are **underspecified** and must not be invented.

## Required data

- Crypto derivatives open interest for the same underlying across Binance, Bybit, Kraken, MEXC, Bitget, BingX, Coinbase, Deribit, HTX, and Crypto.com where historically available.
- Point-in-time venue and contract universe; venues/contracts must not be backfilled into periods before they existed or before TradingView/data-provider coverage began.
- Contract specification and unit metadata sufficient to normalize coin-denominated versus quote/notional-denominated OI.
- Synchronized timestamps and common bar boundaries.
- Underlying/perpetual price OHLCV for state classification and controls.
- Missing-data flags. A stale or absent venue must not be silently forward-filled as fresh OI.
- Venue-level series must be retained so leave-one-venue-out and concentration tests are possible.

## Execution assumptions

The source does not specify signal-to-order timing, order type, fill model, fees, spread, slippage, market impact, funding, leverage/margin, latency, partial fills, or failure handling.

For research, any signal formed from bar-close OI must execute no earlier than the next tradable observation after all required point-in-time inputs are available. Costs and funding must be included for any perpetual implementation. Same-bar close execution using a value only finalized at that close would be look-ahead unless independently justified by timestamped data availability.

## Evidence

### Source-reported

The source documents aggregation across ten major crypto exchanges and visualization of total market OI, including an optional rate-of-change mode. It does not report a traceable Sharpe ratio, CAGR, drawdown, win rate, or other strategy-performance statistic in the reviewed public description.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source does not establish that aggregation predicts returns. OI is non-directional by construction: every derivatives contract has counterparties, so OI growth alone does not identify whether informed pressure is bullish or bearish. Cross-venue aggregation can also be distorted by incompatible contract units, duplicated economic exposure, venue coverage changes, stale feeds, and concentration in a dominant venue.

No independent negative empirical result was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. **Aggregation ablation:** compare price-only controls, strongest single-venue OI, simple aggregate OI, venue-normalized aggregate OI, and aggregate OI plus venue breadth. Reject added aggregation layers that do not improve leakage-safe OOS performance.
2. **Leave-one-venue-out:** remove each venue in turn. A result that depends on one exchange while being described as market-wide fails the cross-venue thesis.
3. **Concentration control:** compare equal-venue aggregation, notional aggregation, and largest-venue-only baselines. Determine whether the signal is merely a transformed dominant-venue series.
4. **Joint-state ablation:** test OI change alone versus price direction alone versus their interaction. The interaction must add incremental OOS information to justify the mechanism.
5. **Deleveraging direction:** pre-register continuation and reversal horizons after extreme OI contraction. Do not choose the profitable direction post hoc.
6. **Point-in-time integrity:** rebuild the active venue/contract universe by date; prohibit survivorship backfill, stale forward-fill, and use of OI updates before their actual availability.
7. **Unit robustness:** verify results survive consistent notional normalization and do not arise from mixing coin-denominated and USD/USDT-denominated contracts.
8. **Regime robustness:** test bull, bear, high-volatility, low-volatility, and major deleveraging periods separately.
9. **Timestamp placebo:** lead the OI series by one bar as a leakage diagnostic and lag it by one or more bars as an availability stress test. Implausible improvement under a lead is a red flag.
10. **Costs:** apply fees, spread, slippage, and funding to any derived trading rule.

Material failure criterion: if cross-venue aggregation cannot consistently beat the strongest single-venue OI and price-only baselines out of sample, reject the aggregation hypothesis rather than adding filters.

## Crypto portability

**direct** — the cited source is explicitly built for crypto open interest across crypto exchanges.

Portability is nevertheless venue- and contract-sensitive. Perpetual versus dated futures, inverse versus linear contracts, coin versus quote denomination, venue fragmentation, 24/7 bar boundaries, and historical symbol changes can materially alter the aggregate.

## Limitations

- **underspecified:** no source-defined entry, exit, holding period, sizing, or risk-management lifecycle.
- **not independently reproduced:** no local or independent empirical validation was performed in this Scout cycle.
- **data gap:** exact historical coverage and contract mapping for every named venue must be established point in time before testing.
- **unproven:** predictive value of aggregate OI, venue breadth, and price/OI interaction remains a falsifiable research hypothesis.
- Aggregation can create false precision if heterogeneous OI units are summed without normalization.
- The optional ATR-style histogram is a visualization transform, not evidence of alpha.

## Implementation status

Research record only. No implementation in the research stack, Qlib full backtest, survivor validation, or production integration has been completed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor/leaderboard entry, demonstrated profitability, or received Paper, Testnet, or Live approval.

## Related Wiki records

Repository-adjacent families for later deduplication/ablation include OI-RSI/funding divergence, CVD+OI participation-state, and other derivatives-positioning records. No claim is made that those repository records already exist as ingested Wiki Brain records.

## Sources

1. VisioNBG. **Aggregated Open Interest**. TradingView open-source script. First published 2025-11-17; updated 2025-12-09. https://www.tradingview.com/script/fE2QsHhr-Aggregated-Open-Interest/ . Reviewed 2026-09-22.
