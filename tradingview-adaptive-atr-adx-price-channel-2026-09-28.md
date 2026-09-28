---
schema: strategy-research-record-v1
title: TradingView Adaptive ATR-ADX Price Channel
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - crypto
  - breakout
  - volatility
  - trend
status: research-only
confidence: medium
source_as_of: 2026-09-28
sources:
  - https://www.tradingview.com/script/nG1ML8dM-Adaptive-Price-Channel-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Adaptive ATR-ADX Price Channel

## Provenance

Public TradingView open-source strategy **Adaptive Price Channel Strategy**, published 2023-04-29 by **HomeCryptoTrader**.

Stable source: https://www.tradingview.com/script/nG1ML8dM-Adaptive-Price-Channel-Strategy/

Canonical TradingView script ID: `nG1ML8dM`.

Source reviewed as of 2026-09-28.

## Economic mechanism

### Source-reported

The author describes an adaptive channel using ATR and ADX to identify sideways versus trending conditions. The channel is built from rolling highest high / lowest low and ATR. ADX and directional indicators classify the market regime. Entries occur when price closes beyond the appropriate channel boundary; the author states that the strategy either takes a channel strategy or trades volatility according to the current trend.

The author reports that the strategy works well on BTC at 2h, 3h, 4h, and 12h timeframes. This is a source claim, not independently verified evidence.

### Research interpretation

The falsifiable hypothesis is that an ATR-inset rolling-extreme channel identifies meaningful price expansion while ADX/+DI/-DI conditions gate direction according to trend strength. The proposed alpha mechanism is conditional breakout persistence: a close through a volatility-adjusted boundary may contain more information when its direction is consistent with an established directional regime.

The ADX regime layer and channel breakout should be tested separately. Their combination must not be assumed to add alpha merely because both are standard indicators.

## Signal

Source-reported normalized rules:

- Common lookback length: **20** in the author's stated settings.
- Compute rolling highest high (HH) and lowest low (LL) over the selected length.
- Compute ATR over the same length.
- Upper channel boundary: **HH - ATR multiplier × ATR**.
- Lower channel boundary: **LL + ATR multiplier × ATR**.
- ATR multiplier in the author's stated settings: **3.2**.
- Compute +DI, -DI, and ADX from directional movement.
- **Sideways regime:** ADX < 25.
  - Long when close is above the upper channel boundary.
  - Short when close is below the lower channel boundary.
- **Bullish trend regime:** ADX >= 25 and +DI > -DI.
  - Long when close is above the upper channel boundary.
- **Bearish trend regime:** ADX >= 25 and +DI < -DI.
  - Short when close is below the lower channel boundary.
- Exit after `exit_length` bars from entry; the author's stated setting is **10 bars**.
- Author-stated properties: initial capital 1000, order size 2 contracts, pyramiding 1, commission 0.05. These are execution/backtest settings, not alpha components.

Signal formation is described in terms of bar close. Exact order-fill timing after a qualifying close is **underspecified** by the accessible source and must not be inferred.

Re-entry behavior beyond the stated pyramiding property, tie behavior when +DI == -DI, and exact state handling across regime transitions are **underspecified**.

## Required data

Source-supported requirements:

- OHLCV bars sufficient to calculate rolling HH/LL, ATR, ADX, +DI, and -DI.
- BTC is explicitly mentioned by the author.
- Source-mentioned timeframes: 2h, 3h, 4h, 12h.

Venue, BTC market type (spot/perpetual/futures), exchange, timezone/candle boundary, and missing-bar treatment are **data gaps**.

Point-in-time implementation must ensure each bar's signal uses only information available by that bar close.

## Execution assumptions

Source-reported:

- Position size in the author's stated TradingView properties: 2 contracts.
- Pyramiding: 1.
- Commission: 0.05 as displayed by the source; the accessible description does not unambiguously state the unit/percentage semantics.

Underspecified:

- signal-to-order timing and next-bar versus same-bar fill;
- market versus limit order;
- spread and slippage;
- impact/capacity;
- funding;
- leverage and margin;
- shorting/borrow mechanics;
- partial fills and order failures.

No missing execution assumption is silently supplied.

## Evidence

### Source-reported

The author states that the strategy works well on BTC on 2h, 3h, 4h, and 12h timeframes. No traceable Sharpe, CAGR, profit factor, maximum drawdown, win rate, or other quantitative performance statistic is provided in the reviewed public description, so none is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly describes this as a first attempt at creating a strategy and says better risk management may be investigated later. No independent negative study was identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

Research-defined tests:

1. Compare the full adaptive rule against an unconditional ATR-channel breakout using identical lookback, holding period, universe, and execution assumptions.
2. Ablate the ADX/+DI/-DI regime gate to determine whether it adds incremental out-of-sample information.
3. Compare the ATR-inset channel against a plain rolling-high/rolling-low breakout to determine whether volatility adjustment adds value.
4. Test neighboring lengths, ATR multipliers, and holding periods rather than accepting the reported 20 / 3.2 / 10 combination as privileged.
5. Evaluate separately across trending and choppy regimes and across the source-mentioned BTC timeframes.
6. Require leakage-safe out-of-sample performance after realistic fees, spread, slippage, and—if perpetuals are used—funding.

**Research-defined falsification threshold:** reject the alpha interpretation if the full rule does not improve risk-adjusted out-of-sample performance versus the simpler matched-exposure channel baseline after realistic costs, or if apparent performance is concentrated narrowly around the reported parameter combination.

## Crypto portability

**direct**

The source explicitly discusses BTC and identifies 2h, 3h, 4h, and 12h use. Portability beyond BTC is unproven.

Crypto-specific risks remain: 24/7 candle boundaries, venue fragmentation, spot/perpetual differences, funding, leverage, and exchange-specific liquidity. The source does not resolve these.

## Limitations

- Not independently reproduced.
- Venue and market type are **data gaps**.
- Exact signal-to-fill semantics are **underspecified**.
- Commission-unit semantics are **underspecified**.
- Re-entry/state-transition details are **underspecified**.
- Source-reported qualitative performance is not quantitative evidence.
- Parameter robustness is unproven.
- Generalization beyond BTC is unproven.

## Implementation status

No implementation in the research stack has been completed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only.

Presence in this repository does not mean the strategy passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a survivor/leaderboard entry, is profitable, or is approved for Paper, Testnet, or Live trading.

`status: research-only`  
`adoption: not-approved`  
`approval_scope: research-only`

## Related Wiki records

No stable related Hermes Wiki Brain record is identified from the GitHub-visible contract; no Wiki link is fabricated.

## Sources

1. HomeCryptoTrader, **Adaptive Price Channel Strategy**, TradingView, published 2023-04-29. https://www.tradingview.com/script/nG1ML8dM-Adaptive-Price-Channel-Strategy/ — reviewed 2026-09-28.
