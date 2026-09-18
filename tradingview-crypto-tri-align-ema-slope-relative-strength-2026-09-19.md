---
schema: strategy-research-record-v1
title: Crypto Tri-Align EMA-Slope Relative-Strength Regime
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
  - https://www.tradingview.com/script/0iSbKeVC-Tri-Align-Crypto-Trend-EMA-Slope/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Tri-Align EMA-Slope Relative-Strength Regime

## Provenance

- Public TradingView open-source indicator: **Tri-Align Crypto Trend (EMA + Slope)** by `Frey_Crypto`.
- Stable source URL: https://www.tradingview.com/script/0iSbKeVC-Tri-Align-Crypto-Trend-EMA-Slope/
- Published: 2025-10-30.
- Source reviewed as of: 2026-09-19.
- The source describes an indicator/alert condition rather than a complete executable trading strategy.

## Economic mechanism

### Source-reported

The source proposes checking trend alignment across three related markets: `COIN/USDT`, `BTC/USDT`, and `COIN/BTC`. Each is classified bullish, bearish, or neutral using fast/slow EMA ordering plus the slope of the fast EMA. The author highlights the `COIN/BTC` leg as relative strength versus Bitcoin and suggests that requiring all three legs to align can avoid chasing coins that lag BTC.

### Research interpretation

The falsifiable hypothesis is that an altcoin trend is more persistent when three conditions agree simultaneously: the altcoin has directional momentum in USD terms, Bitcoin has the same directional market regime, and the altcoin is also gaining or losing relative strength versus Bitcoin. The `COIN/BTC` leg may add information beyond two correlated USD trend filters by requiring benchmark-relative confirmation.

This interpretation does not establish profitability. The incremental alpha question is whether the three-leg alignment improves forward returns or risk-adjusted outcomes relative to simpler `COIN/USDT` trend-only and `COIN/USDT + BTC/USDT` controls.

## Signal

Source-described classification for each of the three pairs:

- Bullish: `EMA_fast > EMA_slow` and fast-EMA slope is at least the configured positive slope threshold.
- Bearish: `EMA_fast < EMA_slow` and fast-EMA slope is at or below the negative slope threshold.
- Otherwise: neutral.
- Composite bullish event: all three pairs are bullish.
- Composite bearish event: all three pairs are bearish.

The source states that Fast EMA, Slow EMA, Slope Lookback, minimum absolute slope percentage, symbols, and an optional signal timeframe are configurable. Default symbols shown by the source are BNB/USDT, BTC/USDT, and BNB/BTC.

The source does not state a unique default value for the EMA lengths, slope lookback, slope threshold, or signal timeframe in the reviewed page text. Entry fill timing, exit, holding period, re-entry, position sizing, and whether an opposite/neutral classification closes a position are also **underspecified**. Any conversion of the alignment event into a complete trading strategy is therefore `research-proposed` and must be declared explicitly during later testing.

## Required data

- Three synchronized crypto price series: `COIN/USDT`, `BTC/USDT`, and `COIN/BTC`, or economically equivalent consistently sourced pairs.
- OHLC close data sufficient to calculate fast/slow EMAs and fast-EMA slope.
- Common signal timeframe and timestamp alignment across all three legs.
- Point-in-time availability is required: all three classifications must use only information available at the signal timestamp.
- Venue and market type are not uniquely specified by the source. Spot/perpetual mixing is a material data-design choice and should not be silently introduced.

## Execution assumptions

The source is an indicator and does not specify an execution model. Market versus limit orders, signal-to-order delay, same-bar versus next-bar fills, fees, spread, slippage, impact, funding, leverage, margin, borrow, latency, and partial fills are **underspecified**.

For later research, a next-bar execution convention after all three component bars are finalized is a `research-proposed` leakage-safe baseline, not a source-reported rule.

## Evidence

### Source-reported

The source explains the classification and alert logic but does not provide a traceable performance statistic or independently validated profitability claim on the reviewed page. No performance figure is imported into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-reported negative empirical result was identified on the reviewed page; absence is not evidence of no negative result. The three legs are mechanically related, so apparent confirmation may be redundant rather than incremental. Using synthetic or differently sourced `COIN/BTC` data may also introduce timestamp or venue inconsistencies.

## Falsification plan

1. Freeze a liquid crypto universe and test multiple non-overlapping market regimes with strictly point-in-time membership.
2. Compare the full three-leg alignment against: (a) `COIN/USDT` EMA+slope alone, (b) `COIN/USDT + BTC/USDT`, and (c) `COIN/USDT + COIN/BTC`.
3. Test whether the `COIN/BTC` leg adds statistically and economically meaningful OOS information after fees/slippage rather than merely reducing trade count.
4. Run component ablations for EMA ordering and slope threshold separately.
5. Freeze a small, bounded parameter grid before evaluation; reject parameter combinations selected only by broad in-sample search.
6. Test venue-consistent spot data separately from perpetual data and include funding where perpetuals are used.
7. Require causal bar alignment across the three symbols and next-bar execution in the leakage-safe baseline.
8. Use placebo tests such as lagged or shuffled BTC-relative classifications to check whether apparent benefit comes from generic trade-frequency reduction.
9. Materially weaken or reject the hypothesis if the full tri-align rule fails to outperform simpler controls OOS after costs, if results depend on a narrow parameter choice, or if the `COIN/BTC` confirmation has no stable incremental value.

## Crypto portability

direct

The source itself is explicitly designed for cryptocurrency markets and uses crypto pairs. Portability still depends on consistent symbol construction, venue, spot/perpetual choice, 24/7 candle boundaries, liquidity, and timestamp synchronization. A `COIN/BTC` cross may not be equally liquid or directly traded for every candidate asset, so synthetic construction requires separate validation.

## Limitations

- Complete trade lifecycle: **underspecified**.
- Exact EMA lengths, slope lookback, slope formula details, threshold, and signal timeframe: **underspecified in the reviewed page text**.
- No independent reproduction.
- No source-backed evidence that three-leg alignment adds alpha beyond simpler trend filters.
- The three price relationships are not independent; `COIN/BTC` is algebraically related to the two USD legs, creating redundancy risk.
- Cross-venue or synthetic pair construction can create a data gap or timestamp mismatch.

## Implementation status

Research record only. No implementation or backtest in our research stack has been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not mean profitable, validated alpha, or approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was established from the permitted GitHub-only evidence, and no Wiki link is fabricated.

## Sources

- TradingView, Frey_Crypto, **Tri-Align Crypto Trend (EMA + Slope)**, published 2025-10-30, reviewed 2026-09-19: https://www.tradingview.com/script/0iSbKeVC-Tri-Align-Crypto-Trend-EMA-Slope/
