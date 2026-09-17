---
schema: strategy-research-record-v1
title: "TradingView Dual-Phase Trend Regime: Median-Split Volatility Clusters Switching Fast/Slow Oscillators"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradingview
  - dual-phase
  - volatility-regime
  - median-split
  - oscillator-switch
  - regime-shift
status: research-only
confidence: low
source_as_of: 2026-09-17
sources:
  - "TradingView public strategy: 'Dual-Phase Trend Regime Strategy [Zeiierman X PineIndicators]', https://www.tradingview.com/script/iJKQeI6A-Dual-Phase-Trend-Regime-Strategy-Zeiierman-X-PineIndicators/ (captured 2026-09-17; open-source crypto strategies list). Concept credited by source to Zeiierman; implementation by PineIndicators."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Dual-Phase Trend Regime: Median-Split Volatility Clusters Switching Fast/Slow Oscillators

## Provenance

- **Source URL**: https://www.tradingview.com/script/iJKQeI6A-Dual-Phase-Trend-Regime-Strategy-Zeiierman-X-PineIndicators/
- **Title**: Dual-Phase Trend Regime Strategy [Zeiierman X PineIndicators]
- **Authors**: concept **Zeiierman**; strategy implementation **PineIndicators** (source credits).
- **Type**: public open-source TradingView strategy; slug `iJKQeI6A`; no immutable commit SHA.
- **As-of / capture**: 2026-09-17.
- **Demo properties not fully printed** on listing (no commission/slippage table in scraped text); mark as underspecified.

## Economic mechanism

### Source-reported

1. **Volatility regime**: stdev of returns; **median-split** clustering into low/high vol clusters; current vol compared to clusters to assign regime.
2. **Dual oscillators**: **fast** in high-vol (react quickly); **slow** in low-vol (reduce noise). System selects active oscillator by regime.
3. **Trend regime**: bullish if oscillator > 0.5; bearish if < 0.5; neutral at 0.5.
4. Trade on **regime shift** (arrows) or **oscillator cross** (user mode).
5. Close opposing positions before opening new ones; long/short/both modes.

### Scout interpretation

Regime-conditional oscillator selection (vol-adaptive smoothing), not a new risk premium. Behavioral story: match signal speed to vol state. Concept credited to Zeiierman — this is a **strategy wrapper** around an indicator concept.

## Signal

### Formation

- Non-repainting claim on listing; refit interval for vol clusters is an input.
- Timeframe: any (source); no crypto-specific demo chart in scraped text.

### Entry / exit (source)

- **Long**: bullish regime shift OR fast crosses above slow (mode-dependent).
- **Short**: bearish shift OR fast below slow.
- **Exit**: opposite shift/cross; close before reverse open.

### Parameters (source-listed inputs)

| Input | Role |
|---|---|
| Oscillator periods | fast / slow lengths |
| Refit interval | how often vol clusters update |
| Volatility lookback & smoothing | regime detector |
| Signal mode | regime shift vs oscillator cross |
| Trade direction | long / short / both |
| Colors | UI |

Exact oscillator formula (e.g. which oscillator, length defaults) must be pinned from script source — listing does not print numeric defaults.

## Required data

- Returns (for stdev) + price source for oscillators. No volume/book/funding in listing.

## Execution assumptions

### Source-reported

- TV standard-candle simulation; properties panel not fully captured.
- No performance claims.

### Scout interpretation

- Cluster refit lag can cause regime whipsaw; costs unknown on listing.

## Evidence

### Source-reported

- Method description only; **no equity table or live track** on listing.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None in listing; absence is not evidence of no negative result.

## Falsification

Research-defined (not source-reported):

1. **Regime switch vs single oscillator**  
   - Same symbol/TF, dual-phase vs always-fast and always-slow.  
   - **Research-defined falsification threshold**: if dual-phase net Sharpe ≤ best single oscillator over ≥ 100 trades, switching is not load-bearing.

2. **Median-split vs fixed threshold**  
   - Replace clusters with fixed vol percentile.  
   - If no difference, median-split is cosmetic.

3. **Crypto transfer**  
   - BTC/ETH H1/H4 net-of-cost expectancy must be > 0 or crypto portability fails.

## Crypto portability

**Declared** any market/TF by source; crypto not separately demonstrated in listing text. 24/7 and funding unmodeled.

Crypto portability is not authorization to trade.

## Limitations

- Concept vs implementation split (Zeiierman / PineIndicators).
- Oscillator constants underspecified on listing.
- Technical regime wrapper; confidence **low**.
- Concurrent TV scout may capture related Zeiierman ports; pinned to `iJKQeI6A`.

## Implementation status

- TV paper only; **not implemented** in nautilus-quant-system.
- **Not authorized** for Paper/Testnet/Live.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

## Related Wiki / repo records

- Existing regime/vol-filter TV records use different switch logic (ADX/choppiness gates, not median-split dual oscillator).
- No prior record cites `iJKQeI6A` (searched 2026-09-17).

## Sources

1. https://www.tradingview.com/script/iJKQeI6A-Dual-Phase-Trend-Regime-Strategy-Zeiierman-X-PineIndicators/ (captured 2026-09-17).
