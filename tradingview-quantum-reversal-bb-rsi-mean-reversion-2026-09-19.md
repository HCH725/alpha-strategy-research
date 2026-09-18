---
schema: strategy-research-record-v1
title: TradingView Quantum Reversal BB-RSI Bitcoin Mean Reversion
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - https://www.tradingview.com/script/YWrR4aHm-Quantum-Reversal/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Quantum Reversal BB-RSI Bitcoin Mean Reversion

## Provenance

Public TradingView open-source strategy **Quantum Reversal**, published June 23, 2025 by `ArganaBridgeCapital`. Stable source URL: https://www.tradingview.com/script/YWrR4aHm-Quantum-Reversal/. Source reviewed as of 2026-09-19.

The source is explicitly presented as a Bitcoin-oriented quantitative mean-reversion strategy. This record normalizes the public description rather than redistributing Pine source code.

## Economic mechanism

### Source-reported

The author describes Bitcoin as oscillating around a statistical mean and proposes buying overextension using a volatility-adjusted Bollinger Band condition or a smoothed-RSI oversold condition. Bollinger Bands are intended to adapt the price-deviation threshold to volatility, while RSI smoothing is intended to reduce oscillator noise. The strategy is long-only and the author notes that the mean-reversion assumption can fail during trending regimes.

### Research interpretation

The falsifiable hypothesis is that downside price or momentum overextension in Bitcoin contains short-horizon reversal information. The two entry components are alternative triggers rather than confirmations:

- **Price-deviation trigger:** lower-Bollinger-band breach identifies an unusually negative deviation from a rolling mean.
- **Momentum trigger:** smoothed RSI below a threshold identifies persistent downside momentum interpreted as oversold.
- **Regime exposure:** long-only construction implicitly assumes downside overextensions are more useful reversal opportunities than symmetric short-side overextensions.

The OR gate is material. It should be tested against each component independently because increased trade frequency is not evidence that combining them improves alpha.

## Signal

Source-described configuration:

- Bollinger moving-average lookback: 20 periods.
- Bollinger standard-deviation multiplier: 2.2.
- RSI lookback: 14 periods.
- RSI smoothing: 5-period simple moving average.
- Smoothed-RSI threshold: 45.
- Long entry: `price <= lower Bollinger Band OR smoothed RSI < 45`.
- Direction: long-only.
- Position sizing: source states fixed 10% of equity per trade.
- Position management: source states a single-position limit.
- Exit: source says positions are closed only while unrealized P&L is positive and describes exit timing as dynamic rather than a fixed profit target; the exact Boolean exit trigger is not specified in the public description.

Signal formation timestamp, exact price field used for the Bollinger comparison, order timing, re-entry behavior, maximum holding period, and the precise profitable-position exit condition are **underspecified** in the public description.

## Required data

At minimum:

- Bitcoin OHLC data on the selected bar timeframe;
- sufficient rolling history for the 20-period Bollinger calculation, 14-period RSI, and 5-period RSI smoothing;
- timestamps with deterministic candle boundaries;
- position entry price / unrealized P&L state for the source-described exit constraint.

The public description does not specify exchange, BTC spot versus perpetual/futures market, quote currency, or a canonical timeframe. Those are data gaps and must not be inferred.

## Execution assumptions

The source does not unambiguously specify signal-to-order timing, same-bar versus next-bar execution, market versus limit orders, spread, slippage, fees, impact, latency, funding, leverage, margin, or partial-fill handling.

For later research, these must be explicit and point-in-time safe. In particular, a bar-close signal must not receive an impossible fill earlier within the same bar. If perpetuals are used, funding must be modeled separately from spot results.

## Evidence

### Source-reported

The source presents the strategy as designed for Bitcoin mean reversion and states that Bollinger volatility adaptation plus RSI smoothing are intended to improve signal quality. It provides the parameter values and rule structure above but does not provide a sufficiently documented independent empirical result in the reviewed public description to treat profitability as evidence.

The source also associates the 2.2-standard-deviation setting with normal-distribution coverage language. That rationale should not be treated as empirical evidence that Bitcoin returns are normally distributed or that the threshold is optimal.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source itself notes that the mean-reversion assumption may not persist in trending market phases and that performance may vary during extreme volatility. No independent negative-result study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

A later test should fail the hypothesis if the entry logic does not retain economically meaningful OOS value after realistic costs and robust parameter perturbation.

Required tests:

1. Compare the full OR rule with Bollinger-only, smoothed-RSI-only, and unconditional long baselines.
2. Evaluate multiple non-overlapping OOS periods including bull trends, bear trends, sideways markets, and high-volatility stress regimes.
3. Test nearby parameter values around BB 20/2.2, RSI 14/45, and smoothing 5 rather than accepting the published tuple as privileged.
4. Separate signal alpha from the unusual exit constraint by testing a clearly defined common exit across all entry variants, then test any reconstructable source exit separately.
5. Apply realistic fee, spread, slippage, and—if perpetuals are used—funding assumptions.
6. Verify all indicators and fills use only information available at the decision timestamp.

Reject or materially weaken the hypothesis if performance is concentrated in the exact published parameter tuple, disappears after costs, fails across OOS regimes, or the OR combination does not improve on its simpler component baselines.

## Crypto portability

**direct** for the research hypothesis because the cited TradingView source explicitly targets Bitcoin.

Portability beyond the source remains unproven. Results can differ between BTC spot and perpetuals, across venues, quote currencies, liquidity conditions, funding regimes, and candle boundaries in the 24/7 market.

## Limitations

- Exact exit Boolean logic: **underspecified**.
- Canonical timeframe and venue: **underspecified**.
- Spot versus derivatives market type: **underspecified**.
- Execution and transaction-cost model: **underspecified**.
- The source's statistical-distribution rationale is not independent evidence of Bitcoin return normality.
- Published parameter choices create optimization / multiple-testing risk unless independently stress-tested.
- **Not independently reproduced.**

## Implementation status

Research record only. No implementation or backtest in our research stack has been completed.

## Adoption boundary

`research-only / not-implemented / not-approved`.

Presence in this repository does not imply profitable alpha, successful validation, approval for implementation, or authorization for paper, testnet, or live trading.

## Related Wiki records

None linked; no stable Hermes Wiki Brain page was established from the allowed GitHub-only evidence, so no Wiki link is fabricated.

## Sources

- ArganaBridgeCapital, **Quantum Reversal**, TradingView open-source strategy, published 2025-06-23, reviewed 2026-09-19: https://www.tradingview.com/script/YWrR4aHm-Quantum-Reversal/
