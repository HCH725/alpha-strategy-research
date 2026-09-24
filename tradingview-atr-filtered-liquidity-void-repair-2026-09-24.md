---
schema: strategy-research-record-v1
title: TradingView ATR-Filtered Liquidity-Void Repair Hypothesis
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - https://www.tradingview.com/script/MSo59jMi-Liquidity-Void-and-Repair-Engine/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView ATR-Filtered Liquidity-Void Repair Hypothesis

## Provenance

- Public TradingView open-source script: `Liquidity Void and Repair Engine` by `GammaBulldog`.
- Stable source URL: https://www.tradingview.com/script/MSo59jMi-Liquidity-Void-and-Repair-Engine/
- First published: 2025-12-20.
- Source page reports an update on 2025-12-22 introducing the active shrink/repair behavior.
- Source reviewed as of 2026-09-24.
- The source is public and traceable. This record normalizes the stated mechanism rather than redistributing Pine source code.

## Economic mechanism

### Source-reported

The author describes rapid price moves as leaving market imbalances or fair-value-gap-like "liquidity voids." The script filters candidate voids using an ATR-relative minimum gap-size setting, then keeps an active zone while subsequent price action traverses it. Partial traversal leaves a residual zone; full traversal seals the zone. The author characterizes bullish voids as possible pullback magnets/support and bearish voids as possible relief-rally magnets/resistance, while also describing immediate full traversal as a possible regime-shift clue. The source explicitly states that the indicator is a visualization tool and does not itself provide entry or exit signals.

### Research interpretation

`research-proposed`: The falsifiable mechanism is not that an FVG is inherently "institutional." It is that a volatility-normalized impulse can create a locally unusual price path, and the subsequent degree and speed of traversal of that impulse-defined zone may contain information about short-horizon continuation versus mean reversion. The incremental question is whether the active repair state adds predictive information beyond the original impulse magnitude, ordinary recent returns, ATR/range normalization, and generic gap/FVG geometry.

The labels "institutional," "smart money," "unfilled orders," and "liquidity debt" are source terminology, not independently established market-microstructure facts.

## Signal

Source-supported state construction:

1. Detect a bullish or bearish void / imbalance after an aggressive price move.
2. Apply a user-defined ATR-relative minimum-gap filter so only sufficiently large voids remain active.
3. Track the high and low coordinates of each active void.
4. As subsequent price enters the zone, shrink the remaining active area to represent partial repair.
5. When price fully traverses the zone, terminate its extension and mark it sealed / fully repaired.

The public description supports the state machine above but does not expose enough detail to reconstruct the exact void-formation formula, ATR lookback, default ATR multiplier, exact boundary update convention, or intrabar treatment unambiguously. Those fields are therefore `underspecified`.

The source does not define a complete executable strategy lifecycle: entry, short entry, exit, holding period, re-entry, sizing, stop logic, and order timing are `underspecified`.

`research-proposed` operationalizations for later testing, not source rules:

- Event study forward returns conditional on void direction and repair fraction.
- Compare untouched, partially repaired, and fully sealed states at matched impulse size and volatility.
- Test whether repair speed or first-touch response predicts continuation/reversal after controlling for recent return and ATR-normalized displacement.
- Any entry/exit mapping must be separately preregistered; it is not implied by this record.

## Required data

- Instrument/universe: source claims broad chart applicability; no specific universe is validated.
- Market type: not restricted by the source; crypto portability remains unproven.
- Timeframe: source notes operation even on high-volatility 1-minute charts but does not establish a preferred or validated timeframe.
- Fields: timestamped OHLC sufficient for the source-described geometry; ATR requires high/low/close history.
- Volume: despite source language about repair by subsequent trading volume, the public description of the sealing rule says full price traversal of the void coordinates; whether volume enters the exact repair calculation is `underspecified` and must not be assumed.
- Point-in-time requirement: only bars available at signal formation may define an active void or its repair state. A historical reconstruction must prevent future traversal from leaking backward into the initial event label.
- Timestamp/candle boundary: venue and timezone/session conventions must be frozen for crypto tests because 24/7 bar boundaries can change detected gaps and ATR.

## Execution assumptions

The source does not specify executable trading assumptions. Signal-to-order timing, same-bar versus next-bar execution, order type, fill model, fees, spread, slippage, impact/capacity, funding, leverage/margin, borrow/shorting, latency, partial fills, and failures are all `underspecified`.

For any later research implementation, the repair state must be evaluated only after the relevant bar is complete unless an independently reconstructed intrabar rule is available. Costs must be applied to any strategy mapping rather than to the visualization state itself.

## Evidence

### Source-reported

The reviewed TradingView page describes the indicator's construction and intended interpretation but does not provide a traceable Sharpe ratio, CAGR, drawdown, win rate, statistical test, or controlled backtest establishing predictive alpha. No source-reported profitability figure is recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source explicitly says the indicator does not provide trade signals or entry/exit points.
- The causal language around "institutional" footprints and unfilled orders is not demonstrated by order-book or aggressor-trade evidence on the reviewed page.
- Exact void formation and repair implementation details are not fully reconstructable from the public prose alone.
- A visually compelling FVG may be reducible to recent displacement, volatility, or ordinary gap geometry rather than an independent alpha feature.
- None of these concerns has been independently resolved in this Scout cycle.

## Falsification plan

`research-proposed`:

1. Reconstruct the exact public Pine rule before predictive testing; if the void boundaries or repair state cannot be reproduced unambiguously, stop as a data/specification failure rather than tuning a substitute.
2. Build point-in-time event labels for bullish/bearish void creation, first touch, repair fraction, repair speed, and sealing. Never label an initial event using future repair information.
3. Baselines: recent return/momentum, ATR-normalized displacement, ordinary three-bar FVG/gap geometry, recent realized volatility, and simple distance-to-zone measures.
4. Matched-event test: compare forward returns for repair states while matching on impulse direction, impulse magnitude, ATR regime, timeframe, and asset liquidity.
5. Ablation: remove ATR filtering; remove repair state while retaining the initial void; retain repair state but replace FVG geometry with a generic impulse-defined range. The repair engine must add incremental OOS information to survive.
6. Direction test: separately test continuation and mean-reversion interpretations. Do not choose the better direction on the same final OOS sample.
7. Crypto robustness: test multiple liquid spot/perpetual assets, multiple venues where possible, and alternative UTC candle offsets to detect session-boundary artifacts.
8. Cost sensitivity: any executable mapping must survive realistic fees, spread, slippage, funding/borrow where applicable, and delayed next-bar execution.
9. Reject the alpha hypothesis if the repair variables do not provide stable OOS incremental information over the simple controls, or if apparent results depend materially on one arbitrary candle boundary, threshold, or hindsight-defined repair label.

## Crypto portability

`unproven`

The source is chart-generic rather than crypto-validated. Crypto-specific risks include 24/7 sessions, venue fragmentation, different spot/perpetual price formation, funding on perpetuals, exchange-specific wick behavior, liquidation-driven impulses, and arbitrary candle boundaries. Traditional gap intuition may not transfer directly because crypto trades continuously; a Pine-defined FVG is geometric price-path structure rather than necessarily a session gap.

## Limitations

- `underspecified`: exact void-formation formula and default parameter values are not fully disclosed in the reviewed public description.
- `underspecified`: whether volume materially enters the repair calculation versus merely the narrative is unclear from the public prose.
- `data gap`: no order-book or aggressor-side evidence verifies the claimed institutional-liquidity interpretation.
- `unproven`: predictive alpha and crypto portability.
- `not independently reproduced`.
- Source terminology may overstate microstructure causality relative to what OHLC geometry can establish.

## Implementation status

No implementation in the research stack was completed in this Scout cycle. No backtest was run. No Qlib validation, survivor promotion, leaderboard entry, Paper, Testnet, or Live work was performed.

## Adoption boundary

Research material only. Presence in this repository does not mean the hypothesis passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

No Hermes Wiki Brain lookup was performed because this Scout is GitHub-only. GitHub dedup review found no record using this canonical TradingView source and no materially identical record for the ATR-filtered void plus active partial/full repair-state hypothesis.

## Sources

- TradingView — GammaBulldog, `Liquidity Void and Repair Engine`: https://www.tradingview.com/script/MSo59jMi-Liquidity-Void-and-Repair-Engine/ (public open-source script; published 2025-12-20, updated 2025-12-22; reviewed 2026-09-24).
