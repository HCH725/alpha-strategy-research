---
schema: strategy-research-record-v1
title: "TradingView Hyper SAR Reactor: Logistic-Boosted Adaptive PSAR with ATR Hysteresis and Bear-Bias Short Gate"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - tradingview
  - parabolic-sar
  - adaptive-psar
  - logistic-af
  - atr-hysteresis
  - bear-bias
  - trend-following
status: research-only
confidence: low
source_as_of: 2026-09-17
sources:
  - "TradingView public strategy: 'Hyper SAR Reactor Trend Strategy', https://www.tradingview.com/script/JNTdgnin-Hyper-SAR-Reactor-Trend-Strategy/ (captured 2026-09-17; open-source crypto strategies list)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Hyper SAR Reactor: Logistic-Boosted Adaptive PSAR with ATR Hysteresis and Bear-Bias Short Gate

## Provenance

- **Source URL**: https://www.tradingview.com/script/JNTdgnin-Hyper-SAR-Reactor-Trend-Strategy/
- **Title**: Hyper SAR Reactor Trend Strategy
- **Author**: TradingView handle `exlux`
- **Type**: public open-source TradingView strategy
- **As-of / capture**: 2026-09-17; slug `JNTdgnin`; no immutable commit SHA.
- **Demo (source)**: **BTC 60m**; capital 10k; size 3% equity; commission 0.05%; slippage 5 ticks; pyramiding 0.
- **Related same-author (different record)**: FluxVector `Bgceb4if` — different fusion (liquidity pulse vs PSAR).

## Economic mechanism

### Source-reported

Adaptive Parabolic SAR intended to be **faster yet calmer** than vanilla PSAR:

1. **Adaptive AF**: base step + boost × logistic(strength), where strength is drift/ATR over a window.
2. **Trail inertia**: one-sided blend keeps SAR monotone.
3. **Flip hysteresis**: price must clear SAR by `buffer × ATR`.
4. **Volatility gate**: ATR / mean(ATR) ≥ ratio.
5. **Bear bias for shorts**: price below EMA(91) and negative slope (window 54) — shorts only in bear regime when enabled.
6. Optional cooldown bars after entry; optional ATR take-profit per side.

### Scout interpretation

Technical/behavioral: dynamic trail acceleration + confirmation buffers to reduce chop flips and weak-downtrend shorts. **No economic risk-premium story.** Incremental vs vanilla PSAR is the logistic AF + gates, not a new alpha family.

## Signal

### Formation

- Bar-close conservative alerts recommended; shapes may move intrabar (source).
- Timeframe: 1m–daily; **demo BTC H1**.

### Entry

- **Long**: internal PSAR flip up AND close > SAR + buffer×ATR AND gates (vol, cooldown if on).
- **Short**: flip down AND close < SAR − buffer×ATR AND (if enabled) bear-bias regime.

### Exit

- SAR as trailing stop; optional ATR TP per side (default TP long 1.0 ATR, short 0.0 = off).
- Source tie handling: stop first if both stop and TP could fill same bar.

### Key parameters (source-listed defaults)

| Param | Default / typical |
|---|---|
| Start AF / Max AF / Base step | 0.02 / 1 / 0.04 |
| Strength window / ATR length | 18 / 16 |
| Strength gain / center / boost | 4.5 / 0.45 / 0.03 |
| AF smoothing / Trail smoothing | 0.50 / 0.35 |
| Flip confirm buffer ATR | 0.50 |
| Cooldown bars | 0 |
| Vol gate length / ratio | 30 / 1.0 |
| Bear bias window / Bias MA | 54 / 91 |
| TP long / TP short ATR | 1.0 / 0.0 |

## Required data

- OHLC + ATR; EMA for bear bias. No order-book, funding, or alternative data.
- Crypto majors declared in scope; demo BTC.

## Execution assumptions

### Source-reported

- Standard candles; commission 0.05%; slippage 5 ticks; no pyramiding; % equity sizing.
- No performance claims.

### Scout interpretation

- Hysteresis + cooldown reduce trade count; path dependency of AF boost untested on listing.
- Bear-bias EMA(91) on H1 is multi-day regime filter — research-proposed note on lookback choice.

## Evidence

### Source-reported

- Full method disclosure on listing; **no published equity table or live track**.
- Limitations listed: gaps, thin books, quiet regimes.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None in listing; absence is not evidence of no negative result.

## Falsification

Research-defined (not source-reported):

1. **vs vanilla PSAR**  
   - Same BTC H1 sample, same costs.  
   - **Research-defined falsification threshold**: if Hyper SAR net Sharpe ≤ vanilla PSAR over ≥ 100 trades, adaptive AF is not load-bearing.

2. **Bear-bias gate ablation**  
   - Disable short gate.  
   - If shorts without gate improve net expectancy without raising MAE beyond tolerance, gate is not required.

3. **Buffer / AF grid**  
   - If best-in-grid is far from defaults and defaults lose money, source defaults are not portable.

4. **Crypto regime split**  
   - Trend vs chop halves; must not magically win both.

## Crypto portability

**Direct** for liquid crypto (demo BTC). 24/7; funding not modeled. Portable across symbols via ATR yardstick (source claim).

Crypto portability is not authorization to trade.

## Limitations

- Technical PSAR variant; confidence **low**.
- Listing reconstruction; some gates optional and may be off in user configs.
- Concurrent TV scout may capture other exlux scripts; pinned to `JNTdgnin`.

## Implementation status

- TV paper only; **not implemented** in nautilus-quant-system.
- **Not authorized** for Paper/Testnet/Live.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

## Related Wiki / repo records

- `tradingview-fluxvector-liquidity-dlp-vol-curvature-impact-efficiency-2026-09-17.md` — same author, different mechanism.
- Existing Supertrend/Keltner/Donchian TV records — different trail constructions.
- No prior record cites `JNTdgnin` (searched 2026-09-17).

## Sources

1. https://www.tradingview.com/script/JNTdgnin-Hyper-SAR-Reactor-Trend-Strategy/ (captured 2026-09-17).
