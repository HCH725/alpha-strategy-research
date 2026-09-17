---
schema: strategy-research-record-v1
title: "TradingView Parabolic RSI Strategy: Parabolic SAR Applied to RSI for Momentum Reversal"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradingview
  - parabolic-rsi
  - parabolic-sar
  - rsi
  - momentum-reversal
  - oscillator
status: research-only
confidence: low
source_as_of: 2026-09-17
sources:
  - "TradingView public strategy: 'Parabolic RSI Strategy [ChartPrime × PineIndicators]', https://www.tradingview.com/script/8F1vlPeb-Parabolic-RSI-Strategy-ChartPrime-PineIndicators/ (captured 2026-09-17; open-source crypto strategies list). Source credits ChartPrime for original concept (MPL-2.0); implementation by PineIndicators."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Parabolic RSI Strategy: Parabolic SAR Applied to RSI for Momentum Reversal

## Provenance

- **Source URL**: https://www.tradingview.com/script/8F1vlPeb-Parabolic-RSI-Strategy-ChartPrime-PineIndicators/
- **Title**: Parabolic RSI Strategy [ChartPrime × PineIndicators]
- **Authors**: concept **ChartPrime** (MPL-2.0 per source); strategy **PineIndicators**
- **Type**: public open-source TradingView strategy; slug `8F1vlPeb`; no immutable commit SHA.
- **As-of / capture**: 2026-09-17.
- **Demo properties**: not fully printed on listing (underspecified).

## Economic mechanism

### Source-reported

Apply **Parabolic SAR logic to RSI values** rather than price:

1. RSI (default length 14) with overbought/oversold thresholds (default 70/30).
2. Custom SAR (start / increment / max acceleration) tracks RSI trend, not price.
3. **Long**: SAR flips **below** RSI line.
4. **Short**: SAR flips **above** RSI line.
5. Optional RSI filter (e.g. long only if RSI > min, short only if RSI < max).
6. Modes: long-only / short-only / both; optional reverse-on-signal; non-repaint claim.

### Scout interpretation

Momentum-reversal via oscillator trend tracking. Behavioral story: RSI path direction flips earlier or cleaner than price PSAR (source claim of "early reversal insight"). **No economic risk-premium mechanism**; incremental vs price-PSAR is applying trail to oscillator space.

## Signal

### Formation

- Non-repainting claim; RSI length and SAR params are inputs.
- Timeframe: any (source); crypto in scope of listing category but no crypto demo table captured.

### Entry / exit

- Entry on SAR flip relative to RSI; optional RSI filter.
- Exit on opposite flip; optional reverse instead of flat.
- No explicit ATR/SL/TP in listing text.

### Parameters (source-listed)

| Input | Default / note |
|---|---|
| RSI length | 14 |
| OB/OS thresholds | 70 / 30 |
| SAR start / increment / max | configurable |
| RSI filter min/max | optional |
| Direction mode | long / short / both |
| Reverse on signal | optional |

## Required data

- Close (or chosen source) for RSI only. No volume/book/funding.

## Execution assumptions

### Source-reported

- TV standard-candle simulation; properties not fully scraped.

### Scout interpretation

- No stop/target in listing → path risk undefined without overlay.
- SAR-on-RSI can flip in mid-range chop; filter helps but defaults unknown.

## Evidence

### Source-reported

- Method disclosure; **no equity table or live track** on listing.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None in listing; absence is not evidence of no negative result.

## Falsification

Research-defined (not source-reported):

1. **vs price-based PSAR**  
   - Same symbol/TF/costs.  
   - **Research-defined falsification threshold**: if Parabolic RSI net Sharpe ≤ price PSAR over ≥ 100 trades, oscillator-space trail is not load-bearing.

2. **RSI filter ablation**  
   - If filter does not improve net expectancy, drop it.

3. **Crypto transfer**  
   - BTC/ETH H1 net expectancy must be > 0 or crypto claim fails.

## Crypto portability

Listing is under crypto strategies category; **no crypto-specific demo captured**. 24/7 and funding unmodeled.

Crypto portability is not authorization to trade.

## Limitations

- ChartPrime concept + third-party strategy wrapper.
- No stops in listing; confidence **low**.
- Concurrent TV scout may capture related oscillator trails; pinned to `8F1vlPeb`.

## Implementation status

- TV paper only; **not implemented** in nautilus-quant-system.
- **Not authorized** for Paper/Testnet/Live.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

## Related Wiki / repo records

- Existing RSI and PSAR TV records apply to price, not SAR-on-RSI.
- No prior record cites `8F1vlPeb` (searched 2026-09-17).

## Sources

1. https://www.tradingview.com/script/8F1vlPeb-Parabolic-RSI-Strategy-ChartPrime-PineIndicators/ (captured 2026-09-17).
