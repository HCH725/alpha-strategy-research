---
schema: strategy-research-record-v1
title: TradingView CVD absorption with price non-confirmation and reversal confirmation
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
  - https://www.tradingview.com/script/LzJGJVHc-CVD-Absorption-Confirmation-Orderflow-Volume/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView CVD absorption with price non-confirmation and reversal confirmation

## Provenance

Public TradingView open-source indicator page, **CVD Absorption + Confirmation [Orderflow & Volume]**, author/page identity `ratipetya`, published 2025-08-21. Stable source: https://www.tradingview.com/script/LzJGJVHc-CVD-Absorption-Confirmation-Orderflow-Volume/ . Source reviewed as of 2026-09-19.

The source is an indicator rather than a complete execution strategy. This record therefore preserves the predictive setup as an alpha hypothesis and does not invent a portfolio or order-execution layer.

## Economic mechanism

### Source-reported

The source describes absorption as a disagreement between aggressive order flow and price response. Bearish absorption occurs when CVD reaches a higher high while price fails to follow; bullish absorption occurs when CVD reaches a lower low while price fails to follow. It interprets this as passive limit liquidity absorbing aggressive market orders and uses price/volume confirmation to identify potential reversal points.

### Research interpretation

The falsifiable hypothesis is that **an extreme in cumulative aggressive-flow pressure that fails to produce a corresponding price extreme contains reversal information**, because marginal aggressive flow is being absorbed rather than translated into price impact. A subsequent candle, volume, or CVD-slope confirmation is intended to reduce false positives by requiring evidence that the failed price response is beginning to reverse.

Component roles:

- Primary signal: CVD extreme versus price non-confirmation (absorption divergence).
- Confirmation: engulfing candle, pin bar, or CVD flattening/slope reversal, with source-described volume conditions where applicable.
- Context suggested by source: supply/demand, VWAP, opening-range, or liquidity levels; these are contextual suggestions, not mandatory rules in the normalized hypothesis.
- Risk / exit: not specified by the source.

The mechanism is distinct from ordinary price-only divergence because its thesis depends on the mismatch between inferred aggressive volume and realized price movement.

## Signal

**Source-supported directional setup:**

- Bearish absorption: CVD makes a higher high while price does not make the corresponding higher high.
- Bullish absorption: CVD makes a lower low while price does not make the corresponding lower low.
- The source displays a signal only when absorption is validated by at least one listed confirmation pattern: an engulfing candle with low volume, an engulfing candle with high volume, a high-volume pin bar, or CVD flattening / slope reversal.

**Underspecified:** the public description does not expose enough detail to state the exact pivot/extreme lookback, exact CVD construction and reset rule, candle-pattern Boolean definitions, high/low-volume thresholds, slope calculation, conflict resolution when confirmations disagree, signal timestamp, re-entry rule, holding period, exit rule, or position sizing without inspecting/reproducing code logic beyond the normalized public description. These details are therefore not invented here.

No `research-proposed` operationalization is promoted to a canonical rule in this capture. A later implementation would need to freeze these choices before testing.

## Required data

- Instrument / universe: source says all markets and timeframes where volume is reliable; crypto is therefore eligible but not uniquely specified.
- Market type / venue: not fixed by source; must be frozen before testing.
- Price: OHLC sufficient to construct price extrema and candidate engulfing/pin-bar confirmations.
- Volume: reliable volume series is required.
- CVD input: cumulative volume-delta series or the inputs required to reconstruct it point-in-time.
- Timestamp/timezone: must be consistent across price and CVD; source does not specify a canonical timezone/session reset.
- Point-in-time requirement: extrema and confirmation must use only information available at the signal timestamp. Any pivot-style implementation requiring future bars must delay signal availability accordingly rather than backdating the signal.

A major data-risk item is that the public page does not establish whether its CVD represents true aggressor-side trade classification or an approximation. This must be resolved before implementation because the economic interpretation depends materially on that distinction.

## Execution assumptions

The source is an indicator and does not specify a complete executable strategy. Market versus limit entry, same-bar versus next-bar fill, fees, spread, slippage, latency, stop/target logic, capacity, leverage, funding, borrow/shorting, partial fills, and failure handling are all **underspecified**.

Any later backtest must separate signal formation from fill timing and apply a causal next-available execution model unless the reconstructed source unambiguously supports another convention.

## Evidence

### Source-reported

The TradingView page describes the absorption and confirmation logic and presents it as a way to identify potential reversal setups. No independently verified performance statistic is taken from the source in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-backed negative performance study was identified on the reviewed page; absence is not evidence of no negative result. The source itself does not establish that the CVD measure is true trade-side order flow, nor does it provide out-of-sample evidence that the confirmation layer improves the raw absorption signal.

## Falsification plan

1. Freeze a causal CVD definition, reset convention, extrema lookback, confirmation definitions, venue, market type, timeframe, and signal-to-fill timing before measuring results.
2. Test the raw absorption divergence against unconditional and simple price-divergence/reversal baselines.
3. Ablate each confirmation family separately: engulfing, pin bar, CVD slope/flattening, and volume condition. Compare raw absorption versus each confirmation and the combined rule.
4. Test whether the signal has forward-return information after fees, spread and slippage across multiple liquid crypto instruments and both trending and ranging regimes.
5. Explicitly compare true aggressor-side delta, if available, with any OHLCV-derived CVD approximation. If the effect disappears with better order-flow data or exists only under one arbitrary approximation, materially weaken or reject the mechanism.
6. Enforce point-in-time extrema/pivot construction. Any result that depends on backdated future-confirmed pivots is invalid.
7. Require untouched out-of-sample survival after all rule choices are frozen. Reject or demote the hypothesis if reversal expectancy is not stable, confirmation adds no incremental value, or realistic costs erase the effect.

## Crypto portability

**direct, but unproven.** The source explicitly says the indicator can be used where reliable volume exists, which includes crypto, but it does not provide a crypto-specific validated sample in the reviewed description.

Crypto-specific risks include venue fragmentation, spot-versus-perpetual volume differences, exchange-specific trade classification, 24/7 session/reset conventions, wash/noisy volume, funding for perpetual positions, and materially different liquidity across symbols. Aggregating venues or mixing spot and perpetual flow would constitute a separate data design choice and must not be assumed silently.

## Limitations

- Signal details are materially **underspecified** beyond the public normalized description.
- CVD construction and whether it reflects true aggressor-side flow are a **data gap**.
- Entry, exit, holding period and execution model are **underspecified**.
- The passive-liquidity absorption interpretation is a hypothesis, not independently verified causality.
- Confirmation components may be redundant indicator stacking unless ablation demonstrates incremental information.
- Not independently reproduced.
- Profitability is unproven.

## Implementation status

Research capture only. No implementation or backtest in our research stack has been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply validated alpha or approval for implementation, paper trading, testnet, or live trading.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page is asserted from this GitHub-only Scout.

## Sources

- TradingView — `ratipetya`, **CVD Absorption + Confirmation [Orderflow & Volume]**, published 2025-08-21, reviewed 2026-09-19: https://www.tradingview.com/script/LzJGJVHc-CVD-Absorption-Confirmation-Orderflow-Volume/
