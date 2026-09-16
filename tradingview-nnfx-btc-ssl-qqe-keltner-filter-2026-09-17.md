---
schema: strategy-research-record-v1
title: "TradingView NNFX BTC SSL Baseline + QQE Confirmation + Keltner Filter Trend System"
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
  - nnfx
  - ssl-channel
  - qqe
  - keltner
  - trend-following
  - atr-exit
status: research-only
confidence: low
source_as_of: 2026-09-17
sources:
  - "TradingView public strategy: 'NNFX BTC SSL+QQE - SignalForge', https://www.tradingview.com/script/ymepYSLq/ (captured 2026-09-17; open-source strategies list, most-recent crypto)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView NNFX BTC SSL Baseline + QQE Confirmation + Keltner Filter Trend System

## Provenance

- **Source URL**: https://www.tradingview.com/script/ymepYSLq/
- **Title**: NNFX BTC SSL+QQE - SignalForge
- **Author (TradingView handle)**: SignalForge-Ai
- **Type**: public open-source TradingView strategy (crypto scripts, most-recent)
- **As-of / capture**: page listing as of 2026-09-17; no immutable commit SHA (TradingView artifact).
- **Identity**: TradingView script slug `ymepYSLq`.
- **Related in-repo TV records**: Keltner/EMA200/ADX breakout, Donchian/choppiness, RSI-box grid, volume-weighted Supertrend — different constructions; this record is the **named NNFX SSL+QQE stack** and has not been captured (dedup search 2026-09-17).

## Economic mechanism

### Source-reported

The script describes an **NNFX-style** (No Nonsense Forex practitioner framework) BTC trend-following stack:

1. **SSL baseline**: price crosses an SSL channel midline (EMA-based) for direction.
2. **QQE histogram agreement**: quantitative qualitative estimation histogram must agree with SSL direction.
3. **Keltner channel filter**: only take entries when price is *inside* the Keltner channel (avoid chasing overextended moves).
4. **Exits**: ATR stop/target (default 33× ATR each side) plus early exit when SSL baseline or QQE flips against the position.
5. Signals **confirm on bar close** (no repaint claim); pyramiding off; one position per direction.
6. Default commission 0.04% and 2-tick slippage pre-set for crypto backtests.

### Scout interpretation

The practitioner story is **trend capture with overextension filter and dual confirmation**: SSL supplies baseline regime, QQE supplies momentum confirmation, Keltner prevents chasing. Economic mechanism is behavioral/technical (trend continuation + volatility-normalized exits), not a named microstructure or risk-premium story. NNFX is a community methodology, not a peer-reviewed model.

## Signal

### Formation

- Bar-close confirmation (source claim: no repainting).
- Timeframe: not fixed on the listing; typical NNFX use is H1–H4 for majors (research-proposed note, not source-stated default).

### Entry

- **Long**: price crosses above SSL baseline AND QQE histogram agrees (bullish) AND price inside Keltner channel.
- **Short**: mirror.
- Source also exposes `Invert Signals` for testing.
- One position per direction; pyramiding off.

### Exit

1. ATR stop: default **33 × ATR** below/above entry (source default; unusually wide — research-proposed note that this is a swing-scale stop).
2. ATR target: default **33 × ATR** opposite side.
3. Early exit: SSL baseline flip or QQE flip against position.

### Parameters (source-listed defaults / user inputs)

| Input | Role |
|---|---|
| Price source | all calculations |
| Invert Signals | test flip |
| Baseline / Keltner / QQE periods | independent windows |
| ATR length + stop/target multipliers | 33× / 33× default |
| Commission / slippage in backtest | 0.04% / 2 ticks |

Exact SSL (typically 21, 2 EMA) and QQE (typically RSI 14, SF 5, QQE 3/1.6/4.2 in NNFX recipes) numbers are **not fully printed** on the listing; reconstruction must pin them from the script source or inputs panel. Mark as **underspecified until source is read line-by-line**.

## Required data

- Instrument: BTC (crypto major); script is crypto-script category.
- Venue: TradingView chart symbol (user-selected exchange feed).
- Fields: OHLC for SSL/ATR/Keltner; close for QQE RSI path.
- Point-in-time: bar-close confirmation only (no intrabar alerts claimed).
- Missing data: TV engine defaults; not modeled in listing.

## Execution assumptions

### Source-reported

- Standard candle simulation; commission 0.04%; slippage 2 ticks; alert JSON for webhook bridges.
- No live fill model beyond TV backtest engine.

### Scout interpretation

- 33× ATR stop/target implies multi-week holds on H1+; capacity and funding not modeled.
- Keltner-inside filter reduces chase but also skips strongest breakout legs (selection trade-off).
- Webhook automation assumed; partial fills / queue not modeled.

## Evidence

### Source-reported

- Open-source strategy listing with method description; **no published equity curve table or live track record** on the scraped listing.
- Source states past performance ≠ future results.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None identified in the listing; absence is not evidence of no negative result.
- Research-proposed: 33× ATR stops have pathological path dependency in crypto regimes; must be stress-tested before any operational reading.

## Falsification

Research-defined tests (not source-reported):

1. **Walk-forward vs baseline**  
   - Same SSL+QQE without Keltner filter; and SSL-only; on BTC H1/H4.  
   - **Research-defined falsification threshold**: if net-of-cost expectancy ≤ 0 or Sharpe ≤ SSL-only baseline over ≥ 100 trades, reject the stack as incremental.

2. **ATR multiplier grid**  
   - 5× / 10× / 33× stops.  
   - If 33× is not better than tighter stops after costs, default is not load-bearing.

3. **Keltner gate ablation**  
   - Disable inside-channel filter.  
   - If filter does not improve MAE or win rate, reject the chase-protection story.

4. **Regime split**  
   - Trend vs chop halves of sample.  
   - NNFX claim is trend-following; must fail or flat in chop (expected), not magically win both.

## Crypto portability

**Direct** for liquid crypto majors/perps on TV-listed feeds. Notes:

- 24/7 session; no equity session filter in listing.
- Funding/fees beyond 0.04% commission not modeled.
- SSL/QQE/Keltner are OHLCV-only; portable across venues with same bar schema.

Crypto portability is not authorization to trade.

## Limitations

- Listing-level reconstruction: some SSL/QQE constants must be read from source, not assumed.
- No published performance; confidence **low**.
- Indicator-stack economic mechanism is thin; incremental value is **named NNFX methodology + Keltner-inside gate**, not a new risk premium.
- Concurrent TV scout may capture related SSL/QQE variants; this record is pinned to slug `ymepYSLq`.

## Implementation status

- TradingView paper strategy only; **not implemented** in nautilus-quant-system.
- **Not authorized** for Paper/Testnet/Live. This record does not modify NautilusTrader or authorize execution.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

Research capture of a public TV strategy only — not adoption, not implementation authorization.

## Related Wiki / repo records

- `tradingview-keltner-ema200-adx-volume-volatility-breakout-2026-09-16.md` — Keltner used as breakout context, different entry.
- `tradingview-btc-donchian-adx-ema200-breakout-continuation-2026-09-16.md` — Donchian breakout, not SSL/QQE.
- No prior record cites `ymepYSLq` or NNFX SSL+QQE (searched 2026-09-17).

## Sources

1. https://www.tradingview.com/script/ymepYSLq/ (NNFX BTC SSL+QQE - SignalForge; captured 2026-09-17).
