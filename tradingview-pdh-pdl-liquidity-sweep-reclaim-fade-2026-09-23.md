---
schema: strategy-research-record-v1
title: "TradingView Previous-Day High/Low Liquidity Sweep-Reclaim Fade"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-23
sources:
  - https://www.tradingview.com/script/laqnh8CT-Liquidity-Sweep-Guardian-Universal-or-point-based/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Previous-Day High/Low Liquidity Sweep-Reclaim Fade

## Provenance

Public TradingView open-source indicator **Liquidity Sweep Guardian (Universal % or point based)** by `DeLeBlanc`, published 2025-12-19. Stable source URL: https://www.tradingview.com/script/laqnh8CT-Liquidity-Sweep-Guardian-Universal-or-point-based/. Source reviewed as of 2026-09-23.

The source is a warning/context tool rather than a complete trading strategy. It explicitly frames its `UNLOCKED` state as permission to *consider* a fade, not as a trade signal.

## Economic mechanism

### Source-reported

The author argues that price often accelerates into Previous Day High (PDH) or Previous Day Low (PDL), where liquidity is presumed to cluster, before reversing. The tool therefore warns against fading merely because price approaches one of those levels. Its stated sequence is: enter a danger zone around PDH/PDL, allow price to penetrate/sweep the level, require a reclaim back through the level, and only then mark the zone `UNLOCKED` for possible counter-trend consideration.

### Research interpretation

The falsifiable hypothesis is that a **confirmed sweep-and-reclaim of a prior-day extreme contains short-horizon mean-reversion information beyond simple proximity to PDH/PDL or a raw breakout failure**. A plausible behavioral mechanism is stop/breakout-order concentration around salient prior-day extremes: an excursion through the level can consume resting orders, while a subsequent close/reclaim back inside the prior range may reveal failure of continuation.

This interpretation does not assume that every wick beyond PDH/PDL represents actual stop executions or institutional activity; OHLC price action alone cannot establish that causal claim.

## Signal

Source-described state sequence:

- Reference levels: Previous Day High and Previous Day Low.
- Outer danger zone: source default is ±75 points or ±0.30% around the reference level.
- Inner critical zone: source default is ±25 points or ±0.10% around the reference level.
- Sweep: price penetrates the relevant PDH/PDL level.
- Reclaim: price subsequently returns above/below the swept level in the direction back inside the prior range.
- `UNLOCKED`: only after sweep plus reclaim; the source says this permits consideration of a fade but is **not itself an entry signal**.

The source page does not fully specify a standalone entry trigger after `UNLOCKED`, exit, holding period, stop, profit target, position sizing, re-entry lifecycle, or all bar/intrabar state-transition semantics. Those elements are **underspecified**.

Research-proposed operationalization for falsification, not source-reported trading rules:

1. At completed-bar timestamps, identify the most recently completed calendar/session day's high and low without look-ahead.
2. Separately test bearish PDH sweep-and-reclaim and bullish PDL sweep-and-reclaim events.
3. Measure forward returns after the first confirmed reclaim over fixed predeclared horizons rather than inventing an optimized exit.
4. Compare percentage-based zones with point-based zones only where contract/instrument units make point distances economically meaningful.
5. Treat any actual fade entry/exit rule as a later research choice, not as part of the source specification.

## Required data

- Instrument/universe: liquid instruments with reliable intraday OHLC; crypto portability is unproven and must be tested separately.
- Market type: source is universal; spot and perpetual crypto must be evaluated separately if ported.
- Intraday OHLC sufficient to construct prior-day highs/lows and subsequent sweep/reclaim states.
- Exchange/venue timestamps and an explicit day-boundary convention.
- Point-in-time availability: PDH/PDL for day D must be formed only from the fully completed prior day; no revised/future bars.
- For perpetuals, funding and mark/index data are desirable controls but are not required by the source rule.
- Volume, order-book, liquidation, or stop-order data are not required by the source and should not be imputed as observed evidence of a liquidity event.

## Execution assumptions

The source does not specify a complete executable strategy. Same-bar sweep/reclaim can be path-dependent if only OHLC bars are available; a leakage-safe test should either require bar-close confirmation and execute no earlier than the next tradable observation, or use sufficiently granular intrabar data with explicit sequencing.

Fees, spread, slippage, market/limit order choice, impact/capacity, leverage, margin, funding, borrow/shorting, latency, partial fills, and failure handling are not specified by the source. Any backtest must model them explicitly rather than treating the visual marker as a frictionless fill.

## Evidence

### Source-reported

The TradingView page describes the danger-zone → sweep → reclaim → `UNLOCKED` workflow and gives default percentage/point zone widths. It does not present a traceable independent backtest establishing profitability for the resulting fade hypothesis.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No source-backed profitability evidence was identified on the reviewed TradingView page. The source itself cautions that `UNLOCKED` is not a trade signal and still requires entry confirmation, risk management, and a trade plan. Absence of further negative evidence is not evidence that the hypothesis works.

## Falsification plan

1. Build a leakage-safe event study across multiple liquid crypto spot and perpetual instruments with explicit UTC day boundaries; repeat with major venue-native daily boundaries where materially different.
2. Primary event: first PDH/PDL penetration followed by a confirmed reclaim. Predeclare short forward-return horizons and test PDH and PDL symmetrically.
3. Baselines: proximity to PDH/PDL without sweep, simple wick rejection, close outside then close back inside, generic short-horizon reversal, and unconditional returns at matched times of day.
4. Ablation: sweep without reclaim versus sweep + reclaim. The reclaim requirement must add stable out-of-sample information to justify the state machine.
5. Test the source defaults (0.30% outer, 0.10% inner) against coarse neighboring values without selecting the best value on the full sample. Point-based thresholds should not be pooled across instruments with incompatible price scales.
6. Stratify by realized volatility and normalize excursion size by ATR/volatility to determine whether fixed percentage thresholds merely proxy for volatility regime.
7. For perpetuals, control for funding, basis, and liquidation-intensity regimes where point-in-time data exist; do not retroactively label price-only sweeps as liquidation events.
8. Use walk-forward/out-of-sample evaluation and include realistic taker/maker fee, spread and slippage scenarios.
9. Reject or materially weaken the hypothesis if sweep + reclaim does not improve directionally consistent OOS forward returns versus simple breakout-failure/reversal baselines after costs, or if results depend on one venue, one asset, one threshold, or a favorable day-boundary convention.

## Crypto portability

**unproven**

The source presents a universal price-action framework, not crypto-specific empirical evidence. Crypto introduces 24/7 trading and therefore no natural universal `previous day` session boundary; UTC, exchange-native, or trader-local boundaries can produce different PDH/PDL levels. Venue fragmentation can also create a sweep on one exchange but not another. Perpetual funding, mark/index mechanics, leverage-driven liquidation cascades, and around-the-clock liquidity variation are additional confounders.

## Limitations

- **underspecified:** no complete entry/exit/holding/sizing lifecycle after `UNLOCKED`.
- **data gap:** the visual price sweep does not prove actual stop or liquidation execution.
- **unproven:** no independently verified alpha evidence is available from this Scout cycle.
- Fixed point thresholds are not naturally portable across assets with different price scales.
- Fixed percentage zones may proxy for volatility unless tested against volatility-normalized controls.
- Prior-day levels are sensitive to the chosen crypto day boundary.
- Same-bar sweep/reclaim interpretation can be path-dependent at coarse bar resolution.

## Implementation status

Research record only. No implementation in the research stack, Qlib full backtest, or runtime integration has been completed.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain or the production candidate pool, completed Qlib validation, became a frozen survivor or leaderboard entry, is profitable or validated alpha, or is approved for implementation, Paper, Testnet, or Live trading.

## Related Wiki records

No Wiki Brain lookup was performed because this Scout is GitHub-only. GitHub deduplication found no existing record for the canonical TradingView source or a materially identical normalized PDH/PDL sweep → reclaim → fade-permission rule before this write.

## Sources

- DeLeBlanc, “Liquidity Sweep Guardian (Universal % or point based),” TradingView public open-source script, published 2025-12-19, reviewed 2026-09-23: https://www.tradingview.com/script/laqnh8CT-Liquidity-Sweep-Guardian-Universal-or-point-based/
