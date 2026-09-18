---
schema: strategy-research-record-v1
title: ETH Short-Term VWAP + EMA/RSI Momentum with ATR Risk Control
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/hlAZd4Ot-ETH-Short-Term-VWAP-EMA-RSI-ATR-Risk-1h-James-Logan/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ETH Short-Term VWAP + EMA/RSI Momentum with ATR Risk Control

## Provenance

Public TradingView open-source strategy **ETH Short-Term VWAP+EMA/RSI (ATR Risk, <1h) (James Logan)** by `jamesbmlogan1`, published 2025-11-09. Stable source URL: https://www.tradingview.com/script/hlAZd4Ot-ETH-Short-Term-VWAP-EMA-RSI-ATR-Risk-1h-James-Logan/. Source reviewed as of 2026-09-18.

## Economic mechanism
### Source-reported

The author describes a short-horizon ETH system that combines EMA trend alignment, VWAP location, an RSI momentum trigger, an optional EMA21 pullback condition, and ATR-based risk controls. The intended use is intraday ETH trading on 5- to 15-minute charts.

### Research interpretation

The falsifiable hypothesis is that short-horizon ETH momentum has better continuation odds when three conditions agree: the medium/long EMA structure identifies the prevailing trend, price is on the same side of session VWAP, and RSI crosses its neutral threshold in the trend direction. The optional EMA21 pullback is a timing filter rather than an independent alpha thesis. ATR stop, target, and trailing rules are risk/exit logic, not assumed sources of predictive alpha.

Component roles:

- Regime: EMA50 versus EMA200 trend alignment.
- Location confirmation: price relative to VWAP.
- Primary trigger: RSI crossing 50 in the regime direction.
- Optional timing filter: pullback confirmation around EMA21.
- Risk / exit: ATR stop, target, trailing stop, plus a maximum holding-bars exit.

## Signal

Source-described normalized logic:

- Intended instrument: ETH/USDT or ETH-based market data.
- Intended chart horizon: 5- to 15-minute bars; strategy is described as short-term, under one hour.
- Long regime: EMA50 > EMA200.
- Long location filter: price above VWAP.
- Long trigger: RSI crosses above 50 while the long regime and VWAP filter hold.
- Short regime: EMA50 < EMA200.
- Short location filter: price below VWAP.
- Short trigger: RSI crosses below 50 while the short regime and VWAP filter hold.
- Optional entry filter: confirmation of a pullback to EMA21.
- Stop loss: 1.6 ATR by the source defaults.
- Take profit: 2.2 ATR by the source defaults.
- Trailing stop: 2.0 ATR by the source defaults.
- Additional exit: automatic flat-out after a configurable number of bars.
- Source says orders and exits are simulated at bar close.
- Source states default position sizing is USD-based, with an example of USD 1,000 per trade.

The public description does not expose the RSI calculation length, ATR calculation length, exact EMA21 pullback Boolean condition, exact maximum holding-bar default, VWAP reset/anchor convention, or conflict precedence among stop, target, trail, and time exit. Those details are **underspecified** and are not inferred here.

## Required data

- ETH OHLCV bars.
- 5- to 15-minute timestamps for the intended use case.
- Volume is required for VWAP.
- Sufficient history to initialize EMA21, EMA50, EMA200, RSI, and ATR.
- Venue can be Binance, Bybit, Coinbase, or another ETH venue according to the source description; venue-specific results must not be assumed equivalent.
- The source says the concept can use spot or perpetual data. Perpetual-specific funding, mark/index data, and liquidation mechanics are not part of the described signal.
- VWAP anchor/reset semantics are not stated in the public description and must be fixed point-in-time before reproduction.

## Execution assumptions

The source states that orders and exits are simulated at bar close and suggests using a 1-minute bar magnifier for finer fill modeling. It describes defaults as balanced for a 0.05% per-side fee assumption.

Spread, market impact, latency, partial fills, order type, adverse selection, perpetual funding, leverage/margin, and the exact intrabar ordering of stop/target/trailing events are not fully specified. These must not be silently supplied in a reproduction.

## Evidence
### Source-reported

The source describes the system as intended for ETH/USDT on 5- to 15-minute charts and gives the rule/parameter defaults summarized above. It recommends validating with at least 200 trades and profit factor above 1.25; this is an author-proposed validation criterion, not a verified performance result.

No source-reported realized Sharpe, CAGR, drawdown, win rate, or independently auditable profitability statistic is used in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-specific independent negative result was identified in the reviewed TradingView page. Absence is not evidence of no negative result. The multi-filter construction also creates parameter-selection and ablation risk: EMA regime, VWAP location, RSI trigger, EMA21 pullback, and ATR exits must each demonstrate incremental value rather than benefiting from in-sample stacking.

## Falsification plan

1. Reconstruct only after resolving the underspecified RSI length, ATR length, VWAP reset convention, EMA21 pullback Boolean rule, and maximum holding period from an auditable source or by declaring any chosen operationalization `research-proposed`.
2. Test ETH spot and ETH perpetual separately on 5m and 15m bars with strict point-in-time indicators and bar-close signal timing.
3. Use chronological train/OOS splits and walk-forward checks across bull, bear, high-volatility, and low-volatility/chop regimes.
4. Compare against simple baselines: EMA50/200 regime alone, RSI50 cross alone, and VWAP-side momentum alone.
5. Ablate VWAP, EMA21 pullback, and each ATR exit component to determine whether the composite adds stable incremental value.
6. Apply realistic maker/taker fees, spread, slippage, and perpetual funding where applicable; stress costs above the source's 0.05% per-side assumption.
7. Treat the hypothesis as materially weakened if the composite fails to improve net OOS risk-adjusted performance over simpler baselines, if the edge disappears under modest cost stress, or if performance depends narrowly on one venue/timeframe/parameter setting.

## Crypto portability

direct

The source is explicitly framed around ETH and major crypto venues. Portability is nevertheless venue- and market-type-sensitive: spot and perpetual markets differ in funding, leverage, liquidation, basis, and microstructure. Crypto's 24/7 session structure also makes the VWAP reset convention material.

## Limitations

- Not independently reproduced.
- RSI length is underspecified in the public description.
- ATR length is underspecified in the public description.
- EMA21 pullback condition is underspecified.
- VWAP anchor/reset convention is underspecified and materially affects a 24/7 crypto market.
- Maximum holding-bars default is underspecified.
- Exact exit-order precedence and intrabar fill behavior are underspecified.
- Multi-component parameter stacking creates overfitting risk.

## Implementation status

Research-only capture. No implementation or validation in our research stack has been completed.

## Adoption boundary

This record is normalized external research material only. It is not evidence of profitable alpha and is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted here.

## Sources

- TradingView — `ETH Short-Term VWAP+EMA/RSI (ATR Risk, <1h) (James Logan)` by `jamesbmlogan1`, published 2025-11-09, reviewed 2026-09-18: https://www.tradingview.com/script/hlAZd4Ot-ETH-Short-Term-VWAP-EMA-RSI-ATR-Risk-1h-James-Logan/
