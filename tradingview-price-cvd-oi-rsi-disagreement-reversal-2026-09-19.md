---
schema: strategy-research-record-v1
title: TradingView Price-CVD-OI RSI Disagreement Reversal
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
  - https://www.tradingview.com/script/9wJhbGcp-Order-Flow-RSI-Price-CVD-OI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Price-CVD-OI RSI Disagreement Reversal

## Provenance

- Public TradingView open-source script: `Order Flow RSI - Price / CVD / OI`.
- Author / page identity: `exploretranspose`.
- Publication date shown by TradingView: 2025-10-14.
- Stable public URL: https://www.tradingview.com/script/9wJhbGcp-Order-Flow-RSI-Price-CVD-OI/
- Source reviewed as of 2026-09-19.

## Economic mechanism

### Source-reported

The source converts three different market-state series into a common RSI scale: price, cumulative volume delta (CVD), and open interest (OI). It describes agreement at overbought/oversold extremes as broad exhaustion/depletion and opposite extremes between pairs as disagreement between price, participation, and positioning that may precede reversals. Examples given by the source include price rising while OI is weak as a potentially weak rally, and price falling while CVD is strong as possible hidden accumulation.

### Research interpretation

The falsifiable hypothesis is that **cross-domain disagreement contains incremental information beyond price RSI alone**. Price describes realized direction, CVD proxies aggressive buy/sell pressure, and OI describes position expansion/contraction. If price reaches an extreme while one of the participation/positioning series reaches an opposing extreme, the price move may have weaker sponsorship and a greater probability of subsequent reversal.

A separate competing hypothesis is that three-way agreement at an extreme is not exhaustion but strong trend participation and therefore predicts continuation. Both directions must be tested rather than assuming the source interpretation is alpha.

## Signal

Source-supported construction:

- Price is transformed with standard RSI.
- CVD is transformed with standard RSI. The CVD engine uses TradingView native volume-delta data and supports Continuous, session-Anchored, and Rolling-window modes.
- OI is transformed with standard RSI using the symbol's `_OI` feed aligned to chart timeframe.
- Price, CVD, and OI have separate RSI lengths.
- Optional smoothing applies SMA, EMA, RMA, WMA, or VWMA.
- Adjustable overbought / midpoint / oversold levels have source-stated defaults of 70 / 50 / 30.
- The source highlights either all-three extreme agreement or opposite extremes between pairs.
- An optional consensus RSI is the arithmetic mean of selected component RSIs.

The source does not define one canonical trading strategy with complete entry, exit, holding period, re-entry, sizing, or execution rules. Those items are `underspecified`.

`research-proposed`: evaluate event studies separately for (a) price-vs-CVD opposite extremes, (b) price-vs-OI opposite extremes, (c) CVD-vs-OI disagreement, and (d) all-three agreement. Do not combine these into a single trade rule before component attribution is established.

## Required data

- Instrument / universe: instruments with reliable price, volume-delta/CVD, and OI feeds; the source explicitly notes futures and BTC as examples where full CVD + OI data may be available.
- Market type: derivatives/futures are naturally relevant because OI is required for the full three-series signal; exact venue is not fixed by the source.
- Price OHLC/close series for price RSI.
- Lower-timeframe or native TradingView volume-delta data for CVD.
- Open-interest `_OI` series aligned point-in-time to the chart timeframe.
- CVD anchor/reset state when Anchored mode is used.
- Exact timestamps and bar boundaries must be aligned across price, lower-timeframe delta, and OI.
- Missing OI must not be silently imputed into a three-way signal; the source states OI availability varies by exchange/symbol.

## Execution assumptions

The source does not specify a canonical signal-to-order timing, market/limit order choice, fill model, fees, spread, slippage, impact/capacity, funding treatment, leverage/margin, latency, or partial-fill model. All are `underspecified`.

`research-proposed`: form historical signals only after every required component for the bar is point-in-time available, then test next-bar execution as the conservative baseline. Include venue-appropriate fees, spread/slippage, and perpetual funding when applicable.

## Evidence

### Source-reported

The source explains the indicator logic and qualitative interpretations but does not provide a traceable Sharpe, CAGR, drawdown, win rate, or independently audited backtest result. It explicitly says the indicator produces signals of interest rather than guaranteed profitable trades and should be backtested.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source notes CVD depends on accurate tick/volume-delta data and can differ across instruments.
- OI availability varies by exchange and symbol.
- Smoothing reduces noise but adds lag.
- Existing repository research contains negative evidence that some short-horizon retail CVD/order-flow signals can be overwhelmed by trading costs; this record therefore treats cost robustness as mandatory rather than assuming order-flow disagreement is tradeable.

## Falsification plan

1. **Incremental-information ablation:** compare price RSI alone against price+CVD, price+OI, CVD+OI, and price+CVD+OI. Reject the composite thesis if the added data streams do not improve genuinely out-of-sample directional or risk-adjusted performance after controlling for lower event frequency.
2. **Disagreement vs agreement:** test opposite-extreme events separately from all-three agreement. Measure forward returns in both reversal and continuation directions so the label is not assumed ex ante.
3. **CVD construction sensitivity:** compare Continuous, Anchored, and Rolling CVD modes. Large sign instability across reasonable constructions weakens the mechanism.
4. **Threshold sensitivity:** test neighborhoods around the source default 70/30 extremes rather than optimizing a single threshold. Reject fragile parameter islands.
5. **Component placebo:** shuffle CVD and OI timestamps within regime-preserving blocks. A real incremental effect should exceed placebo distributions.
6. **Point-in-time audit:** verify no lower-timeframe delta or OI value enters the signal before it was available historically.
7. **Venue/universe robustness:** test BTC and other sufficiently liquid perpetual/futures instruments across venues with reliable OI. Failure outside one symbol/feed should materially reduce confidence.
8. **Cost sensitivity:** apply realistic fees, spread/slippage, and funding. Reject tradeability if gross predictability does not survive conservative costs.
9. **OOS requirement:** reserve later chronological regimes and require directionally consistent incremental value without retuning the core construction.

## Crypto portability

`direct` for crypto instruments where the required CVD and OI feeds are genuinely available: the cited TradingView source explicitly references futures/BTC and is constructed around data types commonly available in crypto derivatives.

Crypto-specific risks include venue fragmentation, inconsistent OI definitions, inverse versus linear contract units, different CVD/feed construction, perpetual funding, 24/7 session boundaries, and the arbitrary effect of session anchors on Anchored CVD.

## Limitations

- `underspecified`: no canonical trade entry/exit/holding/sizing rule.
- `not independently reproduced`.
- `data gap`: historical TradingView-native volume-delta and `_OI` semantics may not map exactly to external research datasets.
- Indicator interpretation is not evidence of predictive alpha.
- Pairwise and three-way conditions can strongly alter sample size; apparent performance must be compared at matched exposure/event frequency where possible.

## Implementation status

Research capture only. No implementation or backtest in the research stack has been completed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in this repository does not establish profitability, validated alpha, or approval for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain links are asserted from this GitHub-only Scout run.

## Sources

- TradingView, `Order Flow RSI - Price / CVD / OI`, `exploretranspose`, published 2025-10-14, reviewed 2026-09-19: https://www.tradingview.com/script/9wJhbGcp-Order-Flow-RSI-Price-CVD-OI/
