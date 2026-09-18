---
schema: strategy-research-record-v1
title: "TradingView BTC RSI + Stochastic + EMA200 Trend-Conditioned Mean Reversion"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - bitcoin
  - mean-reversion
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - https://www.tradingview.com/script/pIrgsDpT-Optimized-BTC-Mean-Reversion-RSI-20-65/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView BTC RSI + Stochastic + EMA200 Trend-Conditioned Mean Reversion

## Provenance

- **Source type:** public TradingView open-source strategy page.
- **Title:** `Optimized BTC Mean Reversion (RSI 20/65)`.
- **Author:** `malli_007`.
- **Stable URL:** https://www.tradingview.com/script/pIrgsDpT-Optimized-BTC-Mean-Reversion-RSI-20-65/
- **TradingView publication date:** December 13, 2025.
- **Source inspected as of:** 2026-09-18.
- The page is marked **OPEN-SOURCE SCRIPT**. This record normalizes the public source description rather than redistributing Pine code.
- Current-`main` GitHub dedup found no record citing canonical TradingView script ID `pIrgsDpT`. A nearby BTC RSI+Bollinger mean-reversion record exists, but its normalized signal is materially different: this source conditions reversal entries on EMA200 trend regime and Stochastic confirmation rather than Bollinger-band displacement.

## Economic mechanism

### Source-reported

The author describes a rule-based Bitcoin mean-reversion strategy intended to capture temporary deviations from equilibrium while respecting the broader trend. RSI identifies an extreme, Stochastic supplies momentum confirmation, and the 200 EMA filters the direction of trades. The source describes buying sharp pullbacks in bullish structures and selling relief rallies in bearish structures.

### Research interpretation

The falsifiable hypothesis is **trend-conditioned mean reversion**: oscillator extremes may revert more reliably when the trade is aligned with the slow market regime rather than taken indiscriminately. EMA200 acts as a regime gate, RSI supplies the primary overextension condition, and Stochastic supplies a second short-horizon exhaustion confirmation.

This differs materially from unconditional oscillator fading. The research question is whether the EMA regime restriction and Stochastic confirmation add cost-adjusted predictive value beyond RSI alone.

## Signal

### Source-reported

- **Long:** RSI(14) below `20`, Stochastic below `25`, and price above the 200 EMA (the source also mentions being within a `controlled deviation`, but does not define that phrase in the reviewed description).
- **Short:** RSI(14) above `65`, Stochastic above `75`, and price below the 200 EMA.
- **Risk exit:** fixed stop loss `4%` and fixed take profit `6%`, corresponding to a source-described 1:1.5 risk/reward ratio.
- **Pyramiding:** none; one position at a time.
- **Position sizing:** source states full-equity sizing is the default and adjustable.

### Underspecified boundaries

- Exact Stochastic lookback/smoothing parameters are not stated in the reviewed public description.
- The long-side `controlled deviation` relative to EMA200 is not quantitatively defined; it must not be invented.
- Exact signal-evaluation timestamp and same-bar versus next-bar fill semantics are not stated.
- Re-entry behavior after an exit is not stated beyond no pyramiding.
- The source says the strategy works across timeframes and is optimized for intraday/swing use, but the reviewed description does not identify one canonical bar interval.
- No Scout-chosen execution rule is promoted to source semantics. Any later causal next-bar implementation would be `research-proposed`.

## Required data

- **Primary instrument/universe:** Bitcoin; the source says it is primarily optimized for Bitcoin and adaptable to other liquid cryptocurrencies.
- **Market type / venue:** `underspecified` in the reviewed description.
- **Fields:** OHLC price bars sufficient to compute RSI, Stochastic and EMA200.
- **Derived features:** RSI(14), Stochastic oscillator, EMA200.
- **Timeframe:** `underspecified`; source characterizes the strategy as suitable for intraday and swing trading rather than fixing one interval in the reviewed description.
- **Point-in-time constraint:** all indicators must be computed causally from data available at signal formation; implementation must not use future-bar information.
- Volume, order book, funding, open interest, basis and options data are not required by the stated signal.

## Execution assumptions

- Signal-to-order timing: `underspecified`.
- Market versus limit orders: `underspecified`.
- Fees, spread, slippage, impact and latency: not specified in the reviewed description.
- The source-reported 4% stop and 6% target define price-risk exits but do not establish actual fill quality.
- If tested on perpetual futures, funding, mark/index price, leverage and liquidation mechanics must be modeled separately; these are not supplied by the source.
- Full-equity sizing is source-described but should be separated from the alpha test because sizing changes portfolio risk rather than the predictive content of the signal.

## Evidence

### Source-reported

The TradingView page presents the strategy as optimized for Bitcoin and describes the rule set and predefined 4% stop / 6% take-profit structure. The reviewed public description does not expose a sufficiently traceable Sharpe, CAGR, drawdown, profit factor or other performance statistic suitable for preservation here, so none is inferred.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source labels the strategy `optimized`, creating parameter-selection/overfitting risk unless the optimization process and out-of-sample protocol are independently established.
- The asymmetric RSI thresholds (`20` long, `65` short) may encode sample-specific tuning rather than a stable market mechanism.
- The Stochastic specification and EMA `controlled deviation` clause are incomplete in the reviewed prose.
- Trading costs and execution timing are not stated.
- None of the source-described performance or robustness claims were independently reproduced in this Scout cycle.

## Falsification plan

1. Recover the exact Stochastic parameters, any quantitative EMA-deviation rule, and Pine order semantics before claiming exact reproduction.
2. Freeze the recovered parameters before out-of-sample evaluation on later BTC data spanning bull, bear, range and high-volatility regimes.
3. Model fees, spread and slippage explicitly; if perpetuals are used, include funding and mark/index mechanics.
4. Ablate the components: compare RSI-only, RSI+EMA200, RSI+Stochastic, and the full RSI+Stochastic+EMA200 rule.
5. Split long and short results because the asymmetric thresholds and Bitcoin's directional asymmetry may produce materially different behavior.
6. `research-defined falsification threshold`: reject the composite-alpha thesis if the full signal fails to improve cost-adjusted out-of-sample performance over the simpler RSI-only or RSI+EMA baseline, or if the apparent edge disappears under realistic costs.

## Crypto portability

`direct` for the broad hypothesis because the cited source is explicitly designed around Bitcoin and liquid cryptocurrencies.

Portability across venues and between spot and perpetual markets remains `adapted`. Differences in spread, funding, leverage, liquidation, mark/index pricing and candle boundaries must be handled in downstream tests.

## Limitations

- Stochastic parameters: `underspecified`.
- EMA `controlled deviation`: `underspecified`.
- Exact timeframe: `underspecified`.
- Exact venue/market type: `underspecified`.
- Signal-to-fill timing: `underspecified`.
- Optimization methodology and out-of-sample evidence are not established by the reviewed description.
- Not independently reproduced.
- No profitability or trading approval is implied.

## Implementation status

`not-implemented`.

No backtest, quantitative-runtime change, paper trading, testnet or live implementation was performed in this Scout cycle.

## Adoption boundary

Research material only. This record is not evidence of validated alpha and is not approval for implementation, paper trading, testnet or live trading.

## Related Wiki records

No Hermes Wiki Brain resource was consulted or asserted in this GitHub-only Scout run.

Repository-level adjacent record used only for dedup context:

- `tradingview-btc-rsi-bollinger-mean-reversion-2026-09-17.md` — materially different Bollinger-displacement + RSI mean-reversion rule.

## Sources

- https://www.tradingview.com/script/pIrgsDpT-Optimized-BTC-Mean-Reversion-RSI-20-65/
