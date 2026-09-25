---
schema: strategy-research-record-v1
title: TradingView RSI-Filtered Jaws SMA Mean-Reversion Strategy
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-25
sources:
  - https://www.tradingview.com/script/fdhtixF2/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView RSI-Filtered Jaws SMA Mean-Reversion Strategy

## Provenance

Public TradingView open-source strategy page: **HYE Mean Reversion SMA [Strategy]**, author **HYE0619**.

Stable source URL: https://www.tradingview.com/script/fdhtixF2/

TradingView shows the strategy published on 2021-07-01 and updated on 2021-07-27. The page identifies it as an RSI-filtered version of PJ Sutherland's Jaws mean-reversion algorithm. This record was normalized from the public page as available on 2026-09-25. No Pine source code is reproduced here.

## Economic mechanism

### Source-reported

The source combines a short-versus-long moving-average displacement with an RSI filter. For longs, the 2-period SMA must be at least 3% below the 5-period SMA while a 5-period exponential average of 2-period RSI is below 30. The symmetric short setup requires the 2-period SMA at least 3% above the 5-period SMA while the smoothed RSI is above 70. Positions close when the fast SMA crosses back through the slower SMA.

The source presents the strategy as mean reversion and allows the displacement percentage, moving-average periods, RSI levels, and trade direction to be changed.

### Research interpretation

The falsifiable hypothesis is that an unusually large short-horizon price displacement from a slightly slower local mean has higher subsequent reversal probability when an independently constructed very-short-horizon momentum oscillator also indicates an extreme.

Component roles:

- Primary signal: percentage displacement of the 2-period SMA from the 5-period SMA.
- Confirmation: 5-period EMA of RSI(2) in an extreme zone.
- Exit: fast/slow SMA mean recross.
- Direction control: long only, short only, or both; source default is long only.

The RSI condition may be redundant with the moving-average displacement rather than incremental alpha. That is an empirical question and should be tested by ablation.

## Signal

Source-supported rules:

**Long entry, on the close:**
1. SMA(2) is 3% or more below SMA(5).
2. EMA(5) of RSI(2) is below 30.

**Long exit, on the close:**
- SMA(2) closes above SMA(5).

**Short entry, on the close:**
1. SMA(2) is 3% or more above SMA(5).
2. EMA(5) of RSI(2) is above 70.

**Short exit, on the close:**
- SMA(2) closes below SMA(5).

Source-supported configurable parameters include the displacement percentage, SMA periods, RSI thresholds, and trade direction. The source states that the default direction is long only.

Underspecified by the reviewed page:

- exact RSI price input if different from the conventional close;
- order fill timing after the close signal;
- position sizing;
- pyramiding/re-entry behavior;
- fees and slippage;
- instrument universe beyond the source's general setup context;
- canonical timeframe.

Any additional operational choice is **research-proposed**, not source-reported.

## Required data

Minimum requirements:

- point-in-time OHLC bars sufficient to calculate close-based SMA and RSI;
- timestamps defining bar boundaries;
- instrument identity and venue;
- enough warm-up history for SMA(5), RSI(2), and EMA(5) of RSI.

Volume, order book, funding, open interest, and options data are not required by the source signal itself.

## Execution assumptions

The source states that entries and exits trigger "on the close," but the reviewed public description does not specify whether a backtest fill occurs at that same closing price or at the next tradable price.

Not specified:

- market versus limit order;
- same-close versus next-bar execution;
- spread;
- fees;
- slippage;
- impact/capacity;
- latency;
- partial fills;
- leverage/margin;
- borrow availability and borrow cost for shorts;
- position sizing.

A leakage-safe test should distinguish signal formation at bar close from the earliest executable price available after that signal.

## Evidence

### Source-reported

The source provides explicit strategy rules and configurable parameters but does not provide a source-traceable Sharpe, CAGR, drawdown, win rate, or other performance statistic on the reviewed page.

The page is labeled open-source by TradingView.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- No independently reproduced performance evidence is available in this Scout cycle.
- No transaction-cost or execution model is specified on the reviewed page.
- The signal uses very short lookbacks and may be sensitive to microstructure noise and trading costs.
- The RSI confirmation is mechanically related to recent price movement and may add little information beyond the SMA displacement.
- The 3% displacement threshold may have strongly different event frequency across instruments and volatility regimes.
- Short-side portability depends on borrow or derivatives mechanics not addressed by the source.
- The source allows parameter changes, creating selection and overfitting risk if optimized without a frozen validation protocol.

## Falsification plan

All items below are **research-proposed**.

1. Reconstruct the source-supported close-based rules exactly before parameter optimization.
2. Compare the full signal against:
   - SMA displacement alone;
   - smoothed RSI extreme alone;
   - a simple short-horizon reversal baseline;
   - buy-and-hold or appropriate directional benchmark.
3. Test whether the RSI filter improves out-of-sample expectancy, Sharpe, and drawdown after accounting for reduced trade count.
4. Test nearby displacement thresholds and moving-average/RSI parameters without selecting the best full-sample combination.
5. Use walk-forward or otherwise leakage-safe out-of-sample evaluation across multiple instruments and volatility regimes.
6. Apply realistic fees, spread, slippage, and shorting/funding costs where applicable.
7. Reject the composite-alpha interpretation if the RSI-filtered rule fails to add stable out-of-sample value over the simpler displacement-only rule after costs.
8. Reject portability claims if results depend on one instrument, one timeframe, or one narrow volatility regime.

## Crypto portability

**adapted**

The required price inputs exist directly in crypto markets, so the mathematical signal is easy to port. However, the source page does not demonstrate crypto-specific empirical validity.

Crypto-specific risks include:

- 24/7 candle-boundary dependence;
- high variation in volatility across assets, making a fixed 3% displacement non-comparable;
- spot versus perpetual differences;
- perpetual funding and liquidation mechanics;
- venue fragmentation;
- short-side execution and borrow differences;
- materially higher microstructure noise on lower-liquidity assets.

A volatility-normalized threshold would be a separate **research-proposed** hypothesis, not the source strategy.

## Limitations

- not independently reproduced;
- execution timing underspecified;
- no cost model;
- no position-sizing rule;
- no canonical timeframe;
- no validated crypto evidence;
- possible indicator redundancy;
- parameter-selection risk;
- fixed percentage displacement may not scale across volatility regimes.

## Implementation status

Research record only.

No implementation in the current research stack has been completed. No Qlib full backtest, survivor promotion, Paper, Testnet, or Live validation is implied.

## Adoption boundary

This record is **research-only**.

Its presence in this repository does not mean it:

- passed Research Intake Review;
- entered Hermes Wiki Brain;
- entered the production candidate pool;
- completed Qlib full-backtest validation;
- became a frozen survivor or leaderboard entry;
- is profitable;
- is validated alpha;
- is approved for implementation;
- is approved for Paper, Testnet, or Live trading.

## Related Wiki records

No stable related Wiki record is asserted in this GitHub-only Scout run.

## Sources

- TradingView — **HYE Mean Reversion SMA [Strategy]**, HYE0619: https://www.tradingview.com/script/fdhtixF2/ (published 2021-07-01; updated 2021-07-27; public open-source strategy page; reviewed 2026-09-25).
