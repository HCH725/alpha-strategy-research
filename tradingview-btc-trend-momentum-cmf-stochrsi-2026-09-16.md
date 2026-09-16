---
schema: strategy-research-record-v1
title: "TradingView BTC Trend-Momentum with EMA200, CMF and Stochastic RSI"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.tradingview.com/script/OKxIjdsz/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC Trend-Momentum with EMA200, CMF and Stochastic RSI

## Provenance

- Source: TradingView open-source strategy, **BTC Trend-Momentum Strategy**, author **SystemsOverFeelings**.
- Stable public URL: https://www.tradingview.com/script/OKxIjdsz/
- Source publication date shown by TradingView: 2026-07-15.
- Source reviewed/as-of: 2026-09-16.
- The publication describes a rules-based Bitcoin long/short strategy and exposes its source code publicly on TradingView.

## Economic mechanism

### Source-reported

The author combines three complementary roles: EMA200 defines the prevailing trend, Chaikin Money Flow (CMF) confirms buying or selling pressure, and Stochastic RSI times entries when momentum turns back from an extreme. An optional ATR-versus-ATR-average filter can restrict trades to above-average volatility.

### Research interpretation

This is a **trend-persistence plus participation-confirmation plus pullback/re-acceleration** hypothesis rather than three interchangeable indicators:

- **Regime:** EMA200 selects the directional trend state.
- **Participation confirmation:** CMF tests whether volume-weighted accumulation/distribution agrees with that direction.
- **Primary timing trigger:** Stochastic RSI attempts to enter when short-horizon momentum turns back from an oversold/overbought state inside the larger trend.
- **Optional regime filter:** ATR relative to its moving average excludes low-volatility conditions.

The falsifiable thesis is that a momentum turn after a short-term exhaustion event has greater continuation value when both the long-horizon price trend and volume-pressure state agree. CMF, EMA and the optional ATR gate should be ablated separately because their incremental contribution is not independently established.

## Signal

### Signal formation

The TradingView description specifies directional filters and a Stochastic RSI crossover trigger. Exact Pine evaluation/order-fill semantics should be reproduced from the public source before implementation; this record does not assume an intrabar fill rule that the source description does not state.

### Long entry

- Price is above EMA200.
- CMF confirms positive buying pressure / agrees with the bullish trend direction.
- Stochastic RSI `%K` crosses back out of the oversold region.
- If the optional volatility filter is enabled, ATR must be above its moving average.

### Short entry

- Price is below EMA200.
- CMF confirms negative selling pressure / agrees with the bearish trend direction.
- Stochastic RSI `%K` crosses back out of the overbought region.
- If the optional volatility filter is enabled, ATR must be above its moving average.

### Exit

The source states that there is **no built-in stop-loss or take-profit**. Positions are closed by the opposing strategy signal; a new long signal closes an existing short and vice versa.

### Parameters and underspecification

- EMA trend length: **200**, explicitly source-reported.
- The public description identifies CMF, Stochastic RSI and optional ATR-vs-average filtering but does not expose all lookback lengths, exact oversold/overbought thresholds, or crossover boundary details in the descriptive text captured for this record. Those values must be taken from the public Pine source during implementation rather than guessed here.
- Position sizing is not treated as alpha. The author's reported backtest used 100% equity per trade, but that is a backtest configuration rather than a predictive rule.

## Required data

- Instrument: Bitcoin; the source describes the strategy specifically for BTC.
- Market/venue: source reports a BTC/USD backtest but does not establish portability across every BTC venue or contract type.
- OHLCV bars sufficient to calculate EMA200, CMF, Stochastic RSI and ATR plus the ATR moving average.
- Volume must be meaningful for the selected venue because CMF is a material signal component.
- Point-in-time computation is required: all indicator values used for a decision must be based only on information available at the signal timestamp.
- Exact timeframe is not stated in the descriptive source material captured here and remains an implementation-time provenance item.

## Execution assumptions

Source-reported backtest configuration includes:

- initial capital: USD 1,000;
- commission: 0.075% per trade;
- slippage: zero;
- position size: 100% equity per trade;
- BTC/USD sample beginning in 2018.

The source does not establish that zero slippage is realistic. Market/limit order choice, bar-close versus next-bar execution, spread, impact, latency, partial fills, leverage/margin, funding for perpetuals, and short-borrow mechanics are not established by the descriptive source material and must not be silently assumed.

## Evidence

### Source-reported

The TradingView publication reports the backtest configuration above but the reviewed descriptive material does not provide a source-traceable Sharpe, CAGR, maximum drawdown, profit factor, or statistically supported edge estimate. No performance figure is promoted here as verified evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source explicitly warns that the strategy has no built-in stop-loss or take-profit and therefore a position can remain at a loss for an extended period until an opposing signal occurs.
- Zero-slippage backtesting is optimistic for executable trading.
- CMF is venue-volume dependent; fragmented crypto volume can produce different pressure states across exchanges.
- EMA200 trend filtering can react slowly around regime transitions, while Stochastic RSI can generate repeated turns during chop.
- The incremental value of CMF and the optional ATR filter has not been independently demonstrated.

## Falsification plan

1. Reconstruct the exact public Pine rules without changing thresholds or timing semantics.
2. Test BTC on point-in-time OHLCV across multiple liquid venues and preserve venue-specific volume rather than merging it casually.
3. Use chronological in-sample/OOS separation and include trending, ranging, high-volatility and low-volatility regimes.
4. Compare against simple controls: EMA200 directional exposure alone and EMA200 + Stochastic RSI without CMF.
5. Ablate CMF and the optional ATR filter independently to measure whether each improves OOS risk-adjusted results rather than merely reducing trade count.
6. Apply realistic fees, spread and slippage; for perpetual implementations also include funding and contract-specific execution assumptions.
7. Treat the thesis as weakened or rejected if the combined signal does not outperform its simpler controls OOS after costs, if results are dominated by one venue/regime, or if small parameter changes destroy the effect.

## Crypto portability

**direct** for the Bitcoin hypothesis because the source itself is explicitly designed and backtested for Bitcoin.

Portability is nevertheless not automatic across BTC spot, perpetuals and venues. CMF depends on venue volume; perpetuals add funding, mark/index-price mechanics and leverage/margin effects; 24/7 candle boundaries and chosen timeframe can alter EMA, Stochastic RSI and ATR states.

## Limitations

- Not independently reproduced.
- Exact timeframe and several indicator lookbacks/thresholds are underspecified in the descriptive source material captured here; implementation must resolve them from the public Pine source.
- No independently verified performance statistics.
- Zero-slippage source backtest assumption is optimistic.
- No native protective stop or profit target.
- Venue-volume dependence is material because CMF participates directly in signal qualification.

## Implementation status

Not implemented in our research stack. No Qlib or other internal backtest has been performed for this record.

## Adoption boundary

Research material only. Presence in this repository does not mean the strategy is profitable, validated alpha, approved for implementation, approved for paper/testnet trading, or approved for live trading.

## Related Wiki records

No stable related Wiki record is asserted here.

## Sources

- TradingView — SystemsOverFeelings, **BTC Trend-Momentum Strategy**: https://www.tradingview.com/script/OKxIjdsz/ (public open-source strategy; published 2026-07-15; reviewed 2026-09-16).
