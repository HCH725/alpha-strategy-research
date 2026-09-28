---
schema: strategy-research-record-v1
title: "TradingView Supertrend Pullback RSI EMA200 Continuation"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-29
sources:
  - https://www.tradingview.com/script/kRMAa3JF-JS-TechTrading-Supertrend-Strategy-Basic-version/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Supertrend Pullback RSI EMA200 Continuation

## Provenance

Public TradingView open-source strategy **JS-TechTrading: Supertrend-Strategy_Basic version** by **JS_TechTrading**, published 2023-04-28. Canonical public source: https://www.tradingview.com/script/kRMAa3JF-JS-TechTrading-Supertrend-Strategy-Basic-version/ . Source reviewed as of 2026-09-29. TradingView script identity: `kRMAa3JF`.

This record normalizes the public description and does not redistribute the Pine source code.

## Economic mechanism

### Source-reported

The author combines Supertrend, RSI and EMA. Supertrend defines trend direction and the pullback/rebound setup; RSI is described as a momentum filter; EMA is used to keep trades aligned with the longer-term trend.

### Research interpretation

The falsifiable hypothesis is **trend continuation after a shallow volatility-adjusted pullback**. Supertrend supplies the local ATR-based trend reference and pullback boundary; the two-bar rebound/drop is the primary continuation trigger; RSI(50-side) and price versus EMA200 are optional momentum/regime confirmations. Stop-loss and profit-target choices are risk management rather than alpha evidence.

## Signal

- **Formation timing:** bar-based; exact order-submission/fill timing is not stated by the source.
- **Long setup:** price is above Supertrend; a pullback candle has its low cross below Supertrend; the following candle's high rises above the pullback candle's high.
- **Short setup:** price is below Supertrend; a pullback candle has its high cross above Supertrend; the following candle's low falls below the pullback candle's low.
- **Optional long filters:** RSI > 50 and price > EMA(200).
- **Optional short filters:** RSI < 50 and price < EMA(200).
- **Exit:** long exits when price closes below Supertrend; short exits when price closes above Supertrend. The source also permits configurable target-profit or stop-loss exits.
- **Holding period:** not fixed; source-described exit is event-driven.
- **Re-entry / pyramiding:** underspecified.
- **Parameters:** EMA length 200 and RSI threshold 50 are explicit. Supertrend ATR length/factor, RSI length, stop-loss and target-profit values are not specified in the public description.
- **Rule completeness:** core pullback/rebound geometry is reconstructable from the description, but indicator defaults and execution semantics are underspecified.

## Required data

- OHLC bars sufficient to construct candle highs/lows/closes, EMA, RSI, ATR and Supertrend.
- Instrument/universe: source says the approach can be used across markets but does not specify a validated universe.
- Venue and market type: underspecified.
- Timeframe: underspecified.
- Timestamp/timezone and candle-boundary requirements: underspecified.
- Point-in-time requirement: all indicator values and the pullback candle must use only information available by the decision timestamp; no future-bar completion may be used.

## Execution assumptions

The source does not specify order type, signal-to-order delay, same-bar versus next-bar fill, fill model, fees, spread, slippage, market impact/capacity, funding, leverage/margin, borrow/shorting, latency, or partial-fill/failure handling.

For later testing, next-bar-open execution after the confirming bar closes is a **research-proposed** conservative operationalization, not a source-reported rule. Cost assumptions must likewise be declared by the downstream test rather than attributed to this source.

## Evidence

### Source-reported

The author states that the strategy has been tested on various markets and timeframes and makes promotional profitability claims, but provides no traceable sample, performance table, Sharpe, CAGR, drawdown, win rate, or other auditable quantitative result in the reviewed public description. No quantitative performance claim is carried into this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independently verified negative result was identified in the reviewed source. The source provides no auditable empirical sample, and the unspecified Supertrend/RSI parameters and execution model create material replication risk. Absence of reported negative evidence is not evidence of robustness.

## Falsification plan

1. Reconstruct the source-described two-bar Supertrend pullback trigger without optimizing parameters broadly; any missing indicator defaults must be explicitly **research-proposed** before testing.
2. Compare the full rule against Supertrend direction-change/trend-following alone and a frequency-matched entry control.
3. Ablate RSI and EMA200 separately and jointly to test whether either confirmation layer adds incremental information.
4. Test chronological out-of-sample periods across trending, ranging, high-volatility and low-volatility regimes.
5. Apply realistic fee/spread/slippage sensitivity and next-bar execution; reject any apparent edge that exists only under frictionless or unavailable same-bar fills.
6. Test a small predeclared neighborhood around any research-proposed missing parameters rather than selecting a narrow in-sample optimum.
7. **Research-defined falsification threshold:** reject the incremental pullback hypothesis if the full rule does not improve out-of-sample risk-adjusted performance over the Supertrend-only baseline after costs, or if the improvement is confined to one asset/timeframe/regime.

## Crypto portability

**unproven.** The rule uses ordinary OHLC-derived indicators and is mechanically portable to crypto, but the source does not demonstrate crypto-specific evidence. A crypto test must specify spot versus perpetual, venue, 24/7 candle boundaries, liquidity, and—where relevant—funding, mark/index pricing, leverage and liquidation assumptions.

## Limitations

- Not independently reproduced.
- Supertrend ATR length/factor: underspecified.
- RSI length: underspecified.
- Timeframe and validated universe: data gap.
- Execution and cost model: data gap.
- Stop/target settings: underspecified.
- Source performance assertions are not accompanied by auditable quantitative evidence.
- Optional filters make component attribution unproven until ablation.

## Implementation status

Research capture only. No implementation in the research stack and no Qlib full backtest was performed by this Scout.

## Adoption boundary

This record is **research-only**, **not-implemented**, and **not-approved**. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, demonstrated profitable alpha, or received Paper/Testnet/Live approval.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted here; GitHub-only operation was used and no Wiki link was fabricated.

## Sources

- TradingView, JS_TechTrading, **JS-TechTrading: Supertrend-Strategy_Basic version**, published 2023-04-28, reviewed 2026-09-29: https://www.tradingview.com/script/kRMAa3JF-JS-TechTrading-Supertrend-Strategy-Basic-version/
