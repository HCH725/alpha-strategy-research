---
schema: strategy-research-record-v1
title: "TradingView Quantum Flux Universal: Binary-Entropy + Path-Efficiency + Vol-Squash Adaptive Gain Polarity Flipper"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradingview
  - quantum-flux
  - binary-entropy
  - path-efficiency
  - volatility-squash
  - adaptive-smoothing
  - polarity-regime
status: research-only
confidence: low
source_as_of: 2026-09-17
sources:
  - "TradingView public strategy: 'Quantum Flux Universal Strategy', https://www.tradingview.com/script/UVGTSBh0-Quantum-Flux-Universal-Strategy/ (captured 2026-09-17; open-source crypto strategies list)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Quantum Flux Universal: Binary-Entropy + Path-Efficiency + Vol-Squash Adaptive Gain Polarity Flipper

## Provenance

- **Source URL**: https://www.tradingview.com/script/UVGTSBh0-Quantum-Flux-Universal-Strategy/
- **Title**: Quantum Flux Universal Strategy
- **Author**: TradingView handle `exlux`
- **Type**: public open-source TradingView strategy
- **As-of / capture**: 2026-09-17; slug `UVGTSBh0`; no immutable commit SHA.
- **Demo (source)**: **QQQ 1h** (Jan 2014–Oct 2025, 324 trades on example chart); capital 25k; commission 0.05%; slippage 10 ticks; size 5% equity; pyramiding 1; process orders on close ON.
- **Declared scope**: large-cap equities/ETFs, index futures, major FX, **liquid crypto**; 1m–daily. Crypto not demonstrated on the published chart.
- **Related same-author**: FluxVector `Bgceb4if`, Hyper SAR `JNTdgnin` — different gain maps.

## Economic mechanism

### Source-reported

Instead of gating separate indicators, three drivers **modulate the gains of two one-pole filters**:

1. **Directional intensity**: 1 − binary entropy of up-move fraction (RMA-smoothed) — more one-sided → faster tracks.
2. **Path efficiency**: Kaufman-style net/sum |steps|, gamma-shaped — clean trend → higher gain.
3. **Volatility squash**: Z-score of |step| then arctan — caps spike domination.

Weighted blend (source: intensity 50%, efficiency 30%, vol 20%) × blend-power scales mix between fixed and full adaptive. Fast − slow = raw flux; phase assist subtracts delayed value; normalize (Z / percent-rank / MAD-Z); guide = EMA(flux with small lead).

**Polarity**: long when flux and guide both > 0; short when both < 0; flip closes opposite and opens new; flux crossing above guide closes short. **No fixed stop/target in v1** — pure regime flipper.

### Scout interpretation

Adaptive EMA-like smoother with information-theoretic and path-quality gains. Behavioral/technical only. “Quantum” is branding, not quantum computing. Incremental vs vanilla EMA cross is the **gain map**, not a risk premium.

## Signal

### Formation

- Source recommends **on bar close** for alerts; `request.security` unused.
- Timeframe: demo QQQ 1h; crypto untested on listing.

### Entry / exit

- Long: flux > 0 AND guide > 0.
- Short: flux < 0 AND guide < 0.
- Close short when flux crosses above guide; polarity +→− closes long and opens short.
- No SL/TP in v1.

### Key parameters (source-typical ranges)

| Param | Typical |
|---|---|
| Fast / Slow span | 6–24 / 20–60 |
| Guide span | 4–12 |
| Blend power | 0.25–0.85 |
| Vol / Efficiency window | 20–80 / 10–60 |
| Efficiency gamma | 0.8–2.0 |
| Min / Max alpha mult | 0.30–0.80 / 1.2–3.0 |
| Norm window / mode | 100–300; Z / pct-rank / MAD-Z |
| Clamp | 2.0–4.0 |
| Price source | ohlc4 default |

## Required data

- Price source (ohlc4) steps only; no volume, book, funding, or chain data.

## Execution assumptions

### Source-reported

- Standard candles; commission 0.05%; slippage 10; bar magnifier ON in properties; 5% equity; pyramiding 1.
- No performance claims; honest limitations listed (gaps, quiet regimes, thin books).

### Scout interpretation

- Pyramiding 1 + no stop: path risk undefined without external risk overlay.
- Crypto adaptation requires re-optimization (source states QQQ-adapted).

## Evidence

### Source-reported

- Method full disclosure; example chart trade count 324 on QQQ; **no published net performance table**.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None in listing; absence is not evidence of no negative result.

## Falsification

Research-defined (not source-reported):

1. **vs fixed-gain EMA cross**  
   - Same spans, same BTC/ETH H1 sample, same costs.  
   - **Research-defined falsification threshold**: if Quantum Flux net Sharpe ≤ fixed-gain EMA cross over ≥ 100 trades, adaptive gain map is not load-bearing.

2. **Driver ablation**  
   - Intensity-only / efficiency-only / vol-only.  
   - Full model must beat best single driver or fusion claim fails.

3. **Crypto transfer**  
   - Source declares liquid crypto but demo is QQQ.  
   - If crypto net expectancy ≤ 0, portability claim fails.

4. **No-stop risk**  
   - Add ATR stop; if results flip sign, v1 flipper is incomplete for any operational reading.

## Crypto portability

**Declared** (liquid crypto in scope) but **not demonstrated** (QQQ demo). Research-proposed validation required before crypto use. 24/7; funding unmodeled.

Crypto portability is not authorization to trade.

## Limitations

- Equity demo; crypto claim unproven on listing.
- Technical regime flipper; confidence **low**.
- No stop/target; pyramiding 1.
- Concurrent TV scout may capture other exlux scripts; pinned to `UVGTSBh0`.

## Implementation status

- TV paper only; **not implemented** in nautilus-quant-system.
- **Not authorized** for Paper/Testnet/Live.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

## Related Wiki / repo records

- `tradingview-fluxvector-liquidity-...` and `tradingview-hyper-sar-reactor-...` — same author, different engines.
- Existing EMA/Supertrend TV records — fixed or gated, not entropy/efficiency-gain modulation.
- No prior record cites `UVGTSBh0` (searched 2026-09-17).

## Sources

1. https://www.tradingview.com/script/UVGTSBh0-Quantum-Flux-Universal-Strategy/ (captured 2026-09-17).
