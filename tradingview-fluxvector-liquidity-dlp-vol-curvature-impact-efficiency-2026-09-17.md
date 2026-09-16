---
schema: strategy-research-record-v1
title: "TradingView FluxVector Liquidity Universal Trendline: DLP + Volatility Curvature + Impact Efficiency Adaptive State"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - tradingview
  - fluxvector
  - liquidity-pulse
  - volatility-curvature
  - impact-efficiency
  - adaptive-trendline
  - kalman-like
status: research-only
confidence: low
source_as_of: 2026-09-17
sources:
  - "TradingView public strategy: 'FluxVector Liquidity Universal Trendline', https://www.tradingview.com/script/Bgceb4if-FluxVector-Liquidity-Universal-Trendline/ (captured 2026-09-17; open-source crypto strategies, most-recent)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView FluxVector Liquidity Universal Trendline: DLP + Volatility Curvature + Impact Efficiency Adaptive State

## Provenance

- **Source URL**: https://www.tradingview.com/script/Bgceb4if-FluxVector-Liquidity-Universal-Trendline/
- **Title**: FluxVector Liquidity Universal Trendline (FFTL)
- **Author**: TradingView handle `exlux`
- **Type**: public open-source TradingView strategy
- **As-of / capture**: 2026-09-17 listing scrape; no immutable commit SHA.
- **Identity**: slug `Bgceb4if`.
- **Demo chart properties (source)**: SPY 30m; capital 25k; commission 0.03%; slippage 5; size 3% equity; pyramiding 0. Crypto is in declared scope but demo is equity.

## Economic mechanism

### Source-reported

FFTL fuses three drivers into a **Kalman-like one-dimensional adaptive state** (not ATR/VWAP/MA):

1. **Directional Liquidity Pulse (DLP)**: signed participation from candle body/wick imbalance × normalized volume, variance-stabilized.
2. **Volatility Curvature**: second difference of realized volatility from log returns (expansion vs compression).
3. **Impact Efficiency**: price change per unit range and volume (boosts gain on efficient moves).

Z-scores of the three form an **energy score** mapped by a logistic function to a gain \(k \in [k_{\min}, k_{\max}]\). State updates toward price plus a small flow push; **one-bar projection** of current slope anticipates crosses.

### Scout interpretation

Behavioral/technical story: signed flow pressure + vol regime shape how fast a single trend state tracks price; projection reduces lag. **No named risk-premium or microstructure theory**; not a Kyle/Amihud construction despite the “liquidity” label. Incremental value is the **explicit three-driver gain map**, not a new economic channel.

## Signal

### Formation

- Shapes settle on bar close (source caveat: can move intrabar). Conservative alerts: **on bar close**.
- Timeframe: 1m–daily declared; demo SPY 30m.

### Entry / exit (source signal rule)

- **Long / flip long**: close **below** trend AND one-bar projection **above** trend.
- **Short / flip short**: close **above** trend AND projection **below** trend.
- Exit on opposite condition; pyramiding 0.

### Parameters (source-listed; typical ranges given)

| Input | Typical / note |
|---|---|
| Flow window | 20–80 |
| Vol window | 30–120 |
| Energy window | 20–80 |
| Min / Max gain | user |
| Price source | close default |
| Show 1-bar projection | UI |

Weights inside energy: source describes weighted sum then logistic; exact numeric weights must be read from script source (underspecified on listing).

## Required data

- OHLC (log returns, range, body/wick imbalance) + volume.
- Instrument: liquid crypto majors declared in scope; demo is SPY.
- No order-book depth, funding, or on-chain fields.

## Execution assumptions

### Source-reported

- Standard candle simulation; commission 0.03%; slippage 5; 3% equity; no pyramiding.
- No performance claims on listing.

### Scout interpretation

- Projection + flip exit can churn in thin books; costs not stress-tested in listing.
- “Impact efficiency” is a bar-level ratio, not market impact in the Almgren–Chriss sense.

## Evidence

### Source-reported

- Method disclosure on listing; **no equity table or live track**.
- Honest limitations: gaps, quiet regimes, thin liquidity.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None in listing; absence is not evidence of no negative result.

## Falsification

Research-defined (not source-reported):

1. **Ablation of three drivers**  
   - DLP-only, curvature-only, efficiency-only vs full FFTL on BTC H1.  
   - **Research-defined falsification threshold**: if full FFTL does not beat best single driver net-of-cost over ≥ 100 trades, the fusion is not load-bearing.

2. **Projection vs no-projection**  
   - If 1-bar projection does not improve expectancy or reduce MAE, drop it.

3. **vs simple EMA cross**  
   - Same costs, same symbols.  
   - If FFTL ≤ EMA cross, incremental claim fails.

4. **Crypto demo gap**  
   - Re-run on BTC/ETH (declared scope) not only SPY.  
   - If crypto net Sharpe ≤ 0, crypto portability claim fails.

## Crypto portability

**Declared direct** by source (liquid crypto in scope) but **demo is equity**. Research-proposed: validate on BTC/ETH perps before any crypto reading. 24/7 and funding not modeled.

Crypto portability is not authorization to trade.

## Limitations

- Listing-level reconstruction; energy weights need source pin.
- Technical mechanism only; confidence **low**.
- Concurrent TV scout may capture other exlux strategies (Hyper SAR, Quantum Flux); this record is pinned to `Bgceb4if`.

## Implementation status

- TV paper strategy only; **not implemented** in nautilus-quant-system.
- **Not authorized** for Paper/Testnet/Live.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

## Related Wiki / repo records

- Existing TV trend records (Keltner/Donchian/SSL+QQE) use different fusion; no prior record cites `Bgceb4if` (searched 2026-09-17).

## Sources

1. https://www.tradingview.com/script/Bgceb4if-FluxVector-Liquidity-Universal-Trendline/ (captured 2026-09-17).
