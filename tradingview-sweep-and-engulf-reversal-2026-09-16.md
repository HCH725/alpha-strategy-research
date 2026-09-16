---
schema: strategy-research-record-v1
title: TradingView Sweep-and-Engulf Reversal
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
  - https://www.tradingview.com/script/2RRJF9yE-Sweep-and-Engulf-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Sweep-and-Engulf Reversal

## Provenance

Public TradingView open-source strategy page: **Sweep and Engulf Strategy**, author `mthibs21`, published Aug 13 (TradingView page observed 2026-09-16). Stable source URL: https://www.tradingview.com/script/2RRJF9yE-Sweep-and-Engulf-Strategy/

This record normalizes the public description rather than reproducing the Pine source.

## Economic mechanism

### Source-reported

The author frames the setup as a liquidity sweep followed by strong reversal confirmation. A bullish event first trades below the prior candle's low, then closes above that prior candle's high; the bearish event is symmetric. The strategy can optionally require alignment with a 200-period EMA trend filter and can invert the signals for testing exhaustion/reversal behavior.

### Research interpretation

The falsifiable hypothesis is that a one-bar failed auction beyond the immediately preceding bar's extreme, followed by a close through the opposite extreme, contains more reversal information than a simple wick rejection. The full engulf close acts as a strong rejection/impulse confirmation after the putative liquidity sweep.

The EMA option is a regime filter rather than the primary alpha signal. ATR- or candle-based stops and reward/risk targets are risk/execution rules, not evidence that the sweep-and-engulf event itself predicts returns.

## Signal

Signal formation: evaluated from the completed current bar relative to the immediately preceding completed bar.

Lookback for the primary pattern: one prior candle.

Long event, source-reported: current bar trades below the previous candle's low and subsequently closes above the previous candle's high.

Short event, source-reported: current bar trades above the previous candle's high and subsequently closes below the previous candle's low.

Optional filters/features reported by the source:

- EMA trend filter, default 200 periods, adjustable;
- optional previous-candle direction filtering;
- standard or inverted trade signals;
- stop loss based either on ATR or the signal candle high/low;
- adjustable ATR stop multiplier;
- configurable reward-to-risk target.

Exit/holding behavior: the source description indicates automatic stop-loss and take-profit calculations but does not expose enough detail in the reviewed page text to establish exact order timing, default ATR multiplier, default reward/risk target, intrabar fill priority, or behavior when both levels are touched in one bar. These details are **underspecified** here and must not be inferred.

Re-entry/pyramiding behavior is **underspecified** in the reviewed source description.

## Required data

- OHLC bars for the traded instrument;
- volume is not required by the described core sweep-and-engulf rule;
- EMA history when the optional trend filter is enabled;
- true-range/OHLC history when ATR-based stops are enabled;
- consistent bar timestamp/timezone and candle boundaries.

The TradingView page states that settings can be adjusted across markets and timeframes; it does not establish a single canonical instrument, venue, market type, or timeframe. Those dimensions are therefore **underspecified** rather than assumed.

Point-in-time requirement: decisions must use only completed prior-bar values and the current bar only after the required close confirmation. A backtest must not expose the final current-bar close before that bar has closed.

## Execution assumptions

The source page does not unambiguously specify signal-to-order timing, same-close versus next-bar execution, market versus limit orders, fill model, commissions, spread, slippage, impact/capacity, leverage/margin, funding, borrow availability, latency, or partial fills.

For research, these must remain explicit experimental assumptions rather than source-reported facts. In particular, entering at the same closing price that establishes the engulf condition can create optimistic timing if the implementation cannot transact at that known close.

## Evidence

### Source-reported

The TradingView page states that the strategy is Strategy Tester compatible and is intended for analysis/backtesting. No source-reported performance statistic is relied upon in this record.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No independent negative evidence was identified in the reviewed source. Absence is not evidence of no negative result.

Mechanistically, the hypothesis is exposed to whipsaw and transaction-cost sensitivity because a complete prior-bar sweep plus opposite-side close can occur during high-volatility noise; this is a research risk, not independently established negative evidence.

## Falsification plan

Test the normalized completed-bar event without optional filters first, then require evidence that forward returns improve versus controls.

- Compare long/short event returns with unconditional returns and with simple wick-only sweep events that do not engulf the opposite prior-bar extreme.
- Evaluate multiple forward horizons and require out-of-sample persistence rather than selecting the best horizon in-sample.
- Stratify by volatility, trend/range regime, asset liquidity and direction.
- Ablate the EMA filter and previous-candle-direction filter separately; reject claims that the composite adds value if the primary event has no incremental information.
- Apply realistic fees, spread and slippage and test next-bar execution as a conservative timing baseline.
- For crypto, test spot and perpetual samples separately and include funding where positions are held across funding timestamps.
- Treat materially non-positive net expectancy out of sample, instability across reasonable parameter choices, or disappearance after conservative execution costs as evidence against adoption of the hypothesis.

## Crypto portability

**unproven**

The rule uses generic OHLC price action and is mechanically portable to crypto bars, but the cited TradingView page does not provide crypto-specific empirical evidence sufficient to call the hypothesis validated or direct crypto evidence.

Crypto testing must account for 24/7 candle-boundary choices, venue fragmentation, spot-versus-perpetual microstructure, spread/slippage, funding for perpetuals, and differences in liquidity across symbols.

## Limitations

- **not independently reproduced**;
- exact execution timing and fill semantics are **underspecified**;
- canonical market, venue and timeframe are **underspecified**;
- exact default risk parameters are **underspecified** in the reviewed page text;
- the liquidity-sweep interpretation is a behavioral hypothesis, not proof that stop orders or institutional activity caused the observed candle pattern;
- optional filters create multiple-testing risk and require ablation rather than being assumed beneficial.

## Implementation status

No implementation in our research stack has been completed. No PyBroker, Nautilus, paper, testnet or live validation is claimed.

## Adoption boundary

Research material only. Presence in this repository does not mean profitable, validated alpha, approved for implementation, or approved for paper, testnet, or live trading.

## Related Wiki records

None linked; no stable related Wiki record was established from the public repository contract.

## Sources

- TradingView — `mthibs21`, **Sweep and Engulf Strategy**: https://www.tradingview.com/script/2RRJF9yE-Sweep-and-Engulf-Strategy/ (public page; source observed 2026-09-16).
