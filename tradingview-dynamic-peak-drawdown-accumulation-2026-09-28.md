---
schema: strategy-research-record-v1
title: TradingView Dynamic-Peak Drawdown Accumulation
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-28
sources:
  - https://www.tradingview.com/script/chFHGVBm-Continuous-Accumulation-Strategy-DCA-v9/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Dynamic-Peak Drawdown Accumulation

## Provenance

Public TradingView open-source strategy page, **Continuous Accumulation Strategy [DCA] v9**, author/page identity `bbbirkan`, published 2025-09-11. Stable source: https://www.tradingview.com/script/chFHGVBm-Continuous-Accumulation-Strategy-DCA-v9/ . Source reviewed as of 2026-09-28. The page identifies the described release as v9.4.

## Economic mechanism

### Source-reported

The author describes a "Buy the Dip" / DCA backtesting strategy whose distinguishing feature is dynamic peak detection. Rather than anchoring to an old all-time or historical high, it continuously references the highest price inside a user-selected rolling lookback, measures the percentage decline from that peak, and buys when price crosses below a configured drop percentage. The author presents this as an adaptive accumulation cycle and explicitly states that the main logic does not generate sell signals.

### Research interpretation

The falsifiable alpha hypothesis is **rolling-peak drawdown mean reversion**: conditional on a chosen horizon, a fresh downside crossing of a drawdown threshold from the current rolling high may identify temporary negative displacement whose subsequent forward return is higher than an unconditional or schedule-based accumulation baseline.

The predictive component is the rolling-peak drawdown crossing. Fixed-cash repeated purchases are position-sizing / accumulation logic, not independent alpha. The strategy can outperform a fixed schedule merely by changing market exposure timing, so any claimed edge must be separated from buy-and-hold beta and from the cash-deployment path.

## Signal

- Formation: evaluated on each chart bar.
- Rolling reference: highest price over a user-defined `Peak Lookback Period`. The source gives an illustrative Daily-chart value of 5, but does not establish that value as a universal default.
- Drawdown: percentage decline from the current rolling peak.
- Long entry: when price crosses below a user-configured target drop percentage, execute a buy order.
- Position sizing: fixed cash amount per entry; the page gives $100 only as an example and does not establish it as a required value.
- Re-entry: the rolling peak is continuously updated and the cycle may generate later accumulation entries when the configured drawdown condition is crossed again.
- Short entry: none described.
- Exit: the source explicitly says the main logic does not generate sell signals.
- Holding period: therefore open-ended / underspecified by the source.
- Exact price field used for the rolling high, exact crossover implementation, default lookback, default drop threshold(s), pyramiding limits, and same-bar order semantics are underspecified.

Any future choice of exit, terminal valuation rule, maximum inventory, cooldown, or crypto-specific threshold is `research-proposed`, not source-reported.

## Required data

- OHLC price bars sufficient to construct the rolling peak and drawdown.
- Instrument / universe: not restricted by the source; the page invites testing on a user's chosen asset.
- Venue and market type: underspecified.
- Timeframe: user-selected; Daily is used only as an example when explaining a 5-bar peak lookback.
- Volume, funding, order book, open interest, liquidation and options data: not required by the described signal.
- Point-in-time requirement: rolling peak and drawdown must use only information available through the signal bar; no future extrema.
- Timestamp, timezone, candle-boundary and missing-bar conventions: underspecified.

## Execution assumptions

The source says a buy is executed when price crosses below the configured drawdown threshold and uses a fixed cash amount for entries, but does not specify whether the backtest fills intrabar, at signal-bar close, or next bar. Order type, spread, fees, slippage, impact, capacity, partial fills, latency, leverage/margin and — for perpetuals — funding are underspecified.

The page also discloses a symbolic one-time dummy buy and sell at the beginning of the test period solely to satisfy TradingView publication/report requirements. That dummy trade is not part of the economic strategy and must be excluded from research evidence and replication metrics.

## Evidence

### Source-reported

No traceable Sharpe, CAGR, drawdown, profit factor, win rate, or other empirical performance figure is stated on the reviewed public page. The author directs users to evaluate Equity Curve, Net Profit and Max Drawdown in TradingView Strategy Tester and to optimize the lookback and drop percentages for the tested asset.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source explicitly has no main-logic sell signal, so conventional closed-trade profitability can be misleading or undefined without a terminal mark-to-market convention. The disclosed publication-only dummy trade can also contaminate naive trade statistics if not removed. Parameter optimization by asset creates material overfitting risk. No independently verified out-of-sample evidence is supplied on the reviewed page.

## Falsification plan

1. Compare the rolling-peak drawdown entry against matched-capital baselines: periodic fixed-schedule DCA, immediate lump-sum deployment, and randomized entry dates.
2. Test a grid of rolling lookbacks and drawdown thresholds without selecting parameters on the evaluation sample; require a frozen out-of-sample period.
3. Use mark-to-market portfolio returns and cash-aware exposure accounting rather than relying on closed-trade metrics; exclude the source's dummy publication trade.
4. Ablate dynamic peak updating against a fixed historical peak and against simple trailing-return drawdown signals.
5. Segment trend, range, crash and recovery regimes to test whether the signal is merely increasing exposure during persistent bear markets.
6. Apply realistic spot fees/slippage; if adapted to perpetuals, separately model funding and liquidation/margin effects.
7. Research-defined falsification threshold: reject the alpha interpretation if the frozen out-of-sample dynamic-peak rule fails to improve risk-adjusted return or drawdown-adjusted terminal wealth over the matched-capital periodic-DCA baseline after costs, or if any apparent advantage is confined to a narrow parameter choice.

## Crypto portability

**unproven.** The mechanism is generic price-based accumulation and can technically be computed on crypto OHLC data, but the reviewed source does not provide crypto-specific empirical evidence. A crypto test must distinguish spot from perpetuals; perpetual adaptation adds funding, leverage, liquidation and mark/index-price dependencies. Crypto's 24/7 candle boundaries and venue fragmentation also make timeframe and timestamp conventions material.

## Limitations

The source leaves material operational details underspecified: default lookback and drawdown threshold(s), exact rolling-high price field, crossing/fill semantics, re-entry/pyramiding constraints, transaction costs, venue, market type and terminal valuation. The strategy has no source-defined economic exit. The source encourages parameter optimization, increasing data-snooping risk. The accumulation rule changes exposure through time, so raw terminal return is not sufficient evidence of predictive alpha.

Not independently reproduced.

## Implementation status

Research capture only. No implementation in the research stack, Qlib full backtest, survivor validation, Paper, Testnet or Live verification has been completed.

## Adoption boundary

This record is research-only, not-implemented and not-approved. Presence in this repository does not mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, paper trading, testnet or live trading.

## Related Wiki records

No stable related Hermes Wiki Brain record is asserted from this GitHub-only Scout run.

## Sources

- TradingView — bbbirkan, **Continuous Accumulation Strategy [DCA] v9**, published 2025-09-11, reviewed 2026-09-28: https://www.tradingview.com/script/chFHGVBm-Continuous-Accumulation-Strategy-DCA-v9/
