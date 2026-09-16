---
schema: strategy-research-record-v1
title: Crypto Cross-Asset SMT Liquidity-Sweep Divergence
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - https://www.tradingview.com/script/Bj46W5Gs-liquidity-sweep-divergence-smt/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Asset SMT Liquidity-Sweep Divergence

## Provenance

Public TradingView open-source indicator **Liquidity sweep divergence (SMT)** by `crypto_daytrade`, published 2026-04-12. Stable source URL: https://www.tradingview.com/script/Bj46W5Gs-liquidity-sweep-divergence-smt/. Source reviewed as of 2026-09-17.

The source explicitly lists crypto pairings including BTC + ETH, BTC + TOTAL3, and ETH + TOTAL3. This record normalizes the public description rather than redistributing the Pine source.

## Economic mechanism

### Source-reported

The author distinguishes this construction from ordinary consecutive swing-high/swing-low divergence. The proposed event is a **liquidity asymmetry between correlated markets**: one market sweeps a prior swing extreme while the comparison market fails to sweep its corresponding extreme. The source interprets that disagreement as weakening continuation and a possible reversal condition.

### Research interpretation

The falsifiable hypothesis is that synchronized crypto markets normally participate together when a directional move represents broad information or risk repricing. If one leg breaches a previously identified liquidity extreme while a correlated leg does not, the isolated breach may contain more transient stop-driven flow than common-factor information. Subsequent returns may therefore favor reversal of the sweeping leg, conditional on correlation/regime stability.

This is a cross-asset relative-confirmation hypothesis, not evidence that every wick beyond a swing is caused by stop hunting. The incremental feature is **cross-market sweep/non-sweep disagreement**, rather than single-instrument divergence or generic liquidity-sweep reversal.

## Signal

**Source-reported core event:**

- Identify corresponding prior swing highs and lows in a main chart instrument and a second correlated instrument.
- Bearish SMT event: the main instrument sweeps a prior swing high while the comparison instrument fails to sweep its corresponding prior swing high.
- Bullish SMT event: the main instrument sweeps a prior swing low while the comparison instrument fails to sweep its corresponding prior swing low.
- Crypto examples named by the source include BTC/ETH and BTC or ETH versus TOTAL3.

**Underspecified by the public description:** exact pivot lookback/strength, how correspondence between pivots across instruments is determined, whether a sweep requires wick-only penetration or a close condition, synchronization tolerance, signal formation timestamp, entry trigger after the divergence, exit, holding period, re-entry, and position sizing.

**Research-proposed operationalization for later testing, not source-reported:** use only completed bars; define pivots with a fixed symmetric rule whose right-side confirmation delay is respected point-in-time; pair each confirmed main-instrument pivot with the latest comparison-instrument pivot known at that timestamp; define sweep as a completed-bar high above the prior confirmed high (or low below the prior confirmed low); require the comparison instrument not to breach its paired level during the same bar interval; enter reversal no earlier than the next executable bar. Test multiple bounded holding horizons rather than selecting an exit from the same sample.

The rule is therefore **underspecified for direct implementation from the public description**; only the cross-asset event definition is source-reported.

## Required data

- Two synchronized correlated market series.
- Crypto candidates: BTC and ETH; BTC or ETH with TOTAL3 where a point-in-time reproducible TOTAL3 series is available.
- OHLC timestamps sufficient to reconstruct swing extremes and sweep events.
- Identical or explicitly aligned bar intervals and timezone/candle boundaries across both series.
- Point-in-time availability for the comparison series; no forward-confirmed pivot may be treated as known before its confirmation bar.
- For TOTAL3, methodology/history/vendor availability must be frozen before testing; a present-day reconstructed index must not silently replace historical point-in-time composition.

Volume, funding, open interest, liquidation data, and order book data are not required by the source-reported core signal.

## Execution assumptions

The public source does not specify executable order timing, order type, fees, spread, slippage, impact/capacity, funding, leverage/margin, partial fills, or failure handling.

A leakage-safe test must delay any pivot-dependent decision until the pivot is actually confirmable and must not fill at a price that predates confirmation. For perpetual implementations, funding and venue-specific execution costs must be included separately from the alpha signal.

## Evidence

### Source-reported

The TradingView page presents the sweep/non-sweep asymmetry as a possible reversal signal and explicitly identifies BTC/ETH and BTC/ETH versus TOTAL3 as crypto use cases. No independently verified performance statistic from this source is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source description itself does not establish that a sweep represents forced stop flow, nor does it provide independent crypto performance evidence. Cross-asset relationships can decouple structurally; a non-sweep may reflect different venue/index composition, volatility, candle boundaries, or idiosyncratic news rather than reversal information.

None other identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. Freeze instrument pairs, venue/index definitions, timeframe, pivot rule, synchronization rule, and holding horizons before evaluation.
2. Compare bullish/bearish SMT events with matched controls where both markets sweep and where neither market sweeps.
3. Measure forward return of the sweeping leg at fixed horizons and test whether reversal conditional on SMT exceeds matched unconditional and single-market-sweep baselines after fees/slippage.
4. Purge overlapping events and use chronological out-of-sample evaluation; pivot confirmation must be delayed correctly.
5. Segment by rolling correlation, relative volatility, trend regime, and major idiosyncratic-news windows. The mechanism weakens if apparent edge exists only during unstable cross-asset correlation.
6. Ablate the cross-asset condition: if a simple single-instrument sweep performs equivalently after costs, the SMT disagreement contributes no demonstrated incremental alpha.
7. Repeat BTC/ETH tests with roles reversed. Persistent benefit should not depend solely on choosing whichever leg looks best ex post.
8. For TOTAL3 variants, rerun with a point-in-time reproducible index. Reject that variant if the result depends materially on non-point-in-time index reconstruction.
9. Treat the hypothesis as failed if out-of-sample, cost-adjusted reversal returns are not materially distinguishable from the matched controls or if the sign is unstable across reasonable predeclared parameter choices.

## Crypto portability

direct

The cited TradingView source explicitly proposes crypto pairings, so the mechanism is directly framed for crypto. That does not constitute empirical validation. Important portability risks remain: BTC and ETH trade across fragmented venues; TOTAL3 is an aggregate index rather than an executable instrument; spot and perpetual candles can disagree; perpetual funding and mark/index construction can create different extremes; and 24/7 candle boundaries must be synchronized exactly.

## Limitations

- `underspecified`: pivot construction and cross-instrument pivot correspondence.
- `underspecified`: precise sweep confirmation and timing.
- `underspecified`: entry, exit, holding period, re-entry, and sizing.
- `data gap`: point-in-time TOTAL3 construction/availability is not established by the source.
- `unproven`: cross-asset sweep disagreement has not been shown here to add alpha beyond a single-market sweep.
- `not independently reproduced`.
- The behavioral label "liquidity sweep" is an interpretation of price structure; OHLC alone does not identify the underlying order-flow cause.

## Implementation status

Research capture only. No implementation in the research stack and no backtest, PyBroker, Nautilus, paper, testnet, or live verification has been performed for this record.

## Adoption boundary

This record is research material only. Repository presence does not imply profitability, validated alpha, approval for implementation, or approval for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from the public GitHub-only Scout context.

## Sources

- TradingView — `crypto_daytrade`, **Liquidity sweep divergence (SMT)**, published 2026-04-12; reviewed 2026-09-17: https://www.tradingview.com/script/Bj46W5Gs-liquidity-sweep-divergence-smt/
