---
schema: strategy-research-record-v1
title: ETH Five-EMA ATR Trend-Reversal Scalping
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
  - https://www.tradingview.com/script/eBiTvw92-Crypto-EMA-Trend-Reversal-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ETH Five-EMA ATR Trend-Reversal Scalping

## Provenance

Public TradingView open-source strategy `Crypto EMA Trend Reversal Strategy` by `ADHDCRYPT0`, published 2021-06-10. Stable source URL: https://www.tradingview.com/script/eBiTvw92-Crypto-EMA-Trend-Reversal-Strategy/ . Source reviewed 2026-09-18.

The public description identifies ETHUSDT on the 5-minute timeframe as the default configuration that the author reports works particularly well. A separately tuned LINKUSDT 5-minute variant is also mentioned.

## Economic mechanism

### Source-reported

The author describes a five-EMA crossover strategy that trades both long and short. The strategy uses two take-profit mechanisms: TP1 is ATR-based and TP2 is an EMA crossover. Stop loss is ATR-based. An optional volume condition exists in the script, but the author states that they do not currently use it.

### Research interpretation

The falsifiable hypothesis is short-horizon trend persistence following coordinated changes in several exponential moving averages. Requiring a multi-EMA configuration may suppress isolated fast-average noise and identify stronger changes in local trend structure. ATR-based TP1 and stop loss are volatility-scaled risk management rather than independent alpha signals; the second EMA-crossover exit attempts to retain exposure while the inferred trend persists.

The incremental value of five EMAs over a simpler one- or two-crossover baseline is unproven and should be tested by ablation rather than assumed.

## Signal

- **Market / source use case:** ETHUSDT, 5-minute bars; source also mentions a separately tuned LINKUSDT 5-minute variant.
- **Direction:** long and short.
- **Primary signal:** a crossover configuration involving five EMAs triggers trades.
- **TP1:** ATR-based.
- **Stop loss:** ATR-based.
- **TP2:** EMA-crossover based.
- **Volume filter:** optional in the source implementation; the author says it is not currently used.

The public page does not expose enough source text to establish the five EMA lengths, exact ordering/crossover Boolean, ATR period or multipliers, exact TP1/TP2 allocation, re-entry behavior, or whether signals are evaluated strictly at bar close. These fields are **underspecified** and are not inferred here.

Any later reconstruction that selects values for those missing fields must label them `research-proposed` unless recovered directly from a traceable primary-source representation.

## Required data

- ETHUSDT OHLCV bars for the source-described use case.
- 5-minute timeframe for the source-described default ETH configuration.
- Sufficient historical close data to calculate all five EMAs once their source parameters are known.
- High/low/close data sufficient for ATR once its source period is known.
- Volume is needed only if testing the optional source-described volume condition.
- Venue is not stated unambiguously in the reviewed description; TradingView tags include Binance, but this record does not upgrade a tag into a precise execution-venue claim.
- Point-in-time calculations must use only information available at the signal timestamp.

## Execution assumptions

The source description does not specify same-bar versus next-bar execution, market versus limit orders, fill model, commission, spread, slippage, latency, partial fills, leverage, margin, or funding treatment. These are **underspecified**.

For later research, execution timing, transaction costs and any perpetual-funding model must be declared explicitly as `research-proposed` unless independently sourced.

## Evidence

### Source-reported

The author reports that the default settings work particularly well as an ETHUSDT 5-minute scalping strategy and that a separately tuned LINKUSDT 5-minute version produced very similar results. The reviewed public description does not provide a sufficiently traceable numerical Sharpe, return, drawdown, win-rate, sample window or transaction-cost result, so no performance number is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative evidence was established in this Scout cycle. The source itself leaves important parameters and execution semantics unspecified in the reviewed public description. Five-EMA crossover systems are also structurally exposed to repeated reversals in choppy regimes; that is a research hypothesis to test, not a source-reported result.

## Falsification plan

1. Recover the exact source EMA and ATR parameters before claiming source-faithful reproduction; otherwise treat a reconstruction as `research-proposed`.
2. Test ETHUSDT 5-minute data with strict point-in-time signal construction and realistic fees, spread and slippage.
3. Compare the full five-EMA signal against simpler EMA baselines to test whether the additional averages add out-of-sample information.
4. Ablate the optional volume condition separately because the author states it is not part of their current default use.
5. Separate alpha from risk management by comparing the entry signal with fixed exits versus the ATR/EMA exit stack.
6. Test trend, range, high-volatility and low-volatility regimes separately.
7. Require out-of-sample persistence after costs; material collapse versus simple EMA baselines or after realistic costs would weaken or falsify the proposed alpha mechanism.

## Crypto portability

direct

The source explicitly describes ETHUSDT and LINKUSDT crypto use cases. Portability beyond those pairs remains unproven. Crypto-specific testing must account for 24/7 candle boundaries, venue-specific OHLCV, spot-versus-perpetual differences, fees, spread/slippage and funding when perpetual contracts are used.

## Limitations

- **underspecified:** exact five-EMA lengths and crossover logic.
- **underspecified:** ATR period, TP1/SL multipliers and TP allocation.
- **underspecified:** exact execution timing and fill assumptions.
- **data gap:** reviewed public description does not provide traceable numerical performance statistics or a complete parameter table.
- **not independently reproduced.**
- **unproven:** incremental alpha from five EMAs versus simpler trend baselines.

## Implementation status

Not implemented in our research stack. No backtest, paper, testnet or live validation was performed in this Scout cycle.

## Adoption boundary

Research-only. Presence in this repository does not establish profitability, validated alpha, implementation approval, paper-trading approval, testnet approval or live-trading approval.

## Related Wiki records

No stable related Hermes Wiki Brain record was identified or accessed; this GitHub-only Scout does not query Hermes Wiki Brain.

## Sources

- TradingView — `Crypto EMA Trend Reversal Strategy`, ADHDCRYPT0, published 2021-06-10: https://www.tradingview.com/script/eBiTvw92-Crypto-EMA-Trend-Reversal-Strategy/
