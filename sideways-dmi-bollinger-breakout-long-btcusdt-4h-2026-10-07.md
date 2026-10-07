---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Sideways DMI-filtered Bollinger lower-band breakout long system on BTCUSDT 4h bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-02-21
sources:
  - https://www.fmz.com/strategy/442375
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
  - https://www.tradingview.com/pine-script-reference/v4/#fun_dmi
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The prose says 'when price breaks below the upper band, go short' (当价格下破上轨时做空), but the pinned code contains no short entry anywhere — the only live order reacting to crossunder(close, upper) is strategy.close('long'), i.e. an exit, not a short. The code governs: long-only, short explicitly disabled per code."
  - "The prose says the stop is 'set near the opposite band' (止损点设在相反轨道附近), but the code has zero live stop/target orders — the only SL/TP lines are commented out. The code governs: SL/TP/trailing/time-limit all explicitly none."
  - "A header comment says 'Works on ETHUSD 3h, 1h, 2h, 4h', but the code calls no timeframe- or symbol-dependent function and the pinned FMZ backtest block fixes period 4h on BTC_USDT. The code plus FMZ block govern: single decision timeframe 4h, research market BTCUSDT under the house overlay."
---

# Sideways DMI-filtered Bollinger lower-band breakout long system on BTCUSDT 4h bars

## Provenance

Primary source read end to end (FMZ strategy page mirror plus live re-verification):

- FMZ strategy: https://www.fmz.com/strategy/442375 (`Breakout-Bollinger-Bands-Oscillation-Trading-Strategy`, page author ChaoZhang; Pine strategy title `Sideways Strategy DMI + Bollinger Bands (by Coinrule)`, `//@version=4`).
- Last modified (as printed on the page): 2024-02-21.
- FMZ backtest block pinned on the page: `start: 2024-01-01 00:00:00`, `end: 2024-01-31 23:59:59`, `period: 4h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair, 4h decision timeframe.
- Live re-verification (2026-10-07): the FMZ page returns HTTP 200 (781857 bytes); the page title (`Breakout Bollinger Bands Oscillation Trading Strategy | FMZ`), the strategy declaration (including `process_orders_on_close=true`, `default_qty_type = strategy.percent_of_equity`, `default_qty_value = 100`, `commission_value=0.1`), the DMI/BB formulas, the sideways/entry/exit lines, and the last-modified stamp (2024-02-21 14:39:14) all match the mirror. No live-page fact contradicts the mirror.
- Mirror executable block: one `strategy()` declaration (`process_orders_on_close=true`, no `calc_on_every_tick`, no `pyramiding`, no `max_bars_back`), date inputs plus a hardcoded `window() => true`, one `dmi(14, 14)` call, BB inputs (`lengthBB = 20`, `src = close`, `mult = 2.0`, `offset = 0`), `sma`/`stdev` basis/dev/upper/lower assignments, the commented-out SL/TP block, and exactly two live order calls: one `strategy.entry(id="long", long = true, when = sideways and (crossover(close, lower)) and window())`, one `strategy.close("long", when = (crossunder(close, upper)))`.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-07): a working-tree search for `442375`, `sideways` and `bollinger` (case-insensitive) returned 0 matches — no Bollinger-family record exists on `main`. Closest records on `main`: `ichimoku-cloud-adx-trend-filter-btcusdt-1d-2026-10-06.md` (Coinrule Ichimoku cloud trend system with ADX/DMI filter, 1d, two-sided) and `dmi-swings-contrarian-adx-btcusdt-1d-2026-10-06.md` (DMI-swings contrarian system, 1d). Five-axis distinction: mechanism differs (DMI-spread sideways gate AND lower-BB cross-up entry with upper-BB cross-under exit, long-only mean-reversion-in-range, versus cloud-trend and contrarian-swing constructions), signal construction differs (no other record uses a `abs(+DM - -DM) < 20` gate or BB-band-cross orders), source identity differs (FMZ 442375 Coinrule sideways/BB versus Coinrule Ichimoku and DMI-swings sources), timeframe differs (4h versus 1d), and direction differs (long-only versus two-sided). `gh pr list --state open` shows only PR #36 (reconstruction lane, no `research/*` collision).

## Economic mechanism

### Source-reported

A range-oscillation long system: it trades only when the market is judged sideways (DMI directional spread narrow), buying the moment price crosses back up through the Bollinger lower band (excess-bearish exhaustion inside a range) and exiting when price crosses back down through the upper band. No trend chasing: entries are gated OUT of trending markets by the sideways condition.

### Research interpretation

Mean-reversion inside a DMI-certified range: the `sideways` gate (|+DM − −DM| < 20) suppresses entries when a strong directional move dominates, while the lower-band cross-up times the long entry and the upper-band cross-under takes the exit. The edge, if any, comes from buying range-edge exhaustion rather than breakouts. No leverage, sizing, or cost edge is embedded in the signal; the source `percent_of_equity 100%` / `commission 0.1%` lines are capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v4, defaults quoted — inputs unmodified):

- DMI: `[pos_dm, neg_dm, adx] = dmi(14, 14)` (v4 built-in; `diLength = 14`, `adxSmoothing = 14`; `adx` destructured but never read — inert).
- Bollinger: `lengthBB = 20`, `src = close`, `mult = 2.0`; `basis = sma(src, 20)`; `dev = 2.0 * stdev(src, 20)`; `upper = basis + dev`; `lower = basis - dev`. The `offset = input(0)` value is never applied to any band (formulas use `basis ± dev` directly) — inert dead input.
- Sideways gate: `sideways = (abs(pos_dm - neg_dm) < 20)` — strict inequality both sides; equality (spread exactly 20) does NOT pass.
- Entry (long only): `strategy.entry(id="long", long = true, when = sideways and (crossover(close, lower)) and window())` with `window() => true` unconditionally (the `fromYear/fromMonth/fromDay/thruYear/thruMonth/thruDay/start/finish/showDate` inputs are computed but never consulted — inert). `crossover` is the strict v4 cross-over (close[t-1] <= lower[t-1] AND close[t] > lower[t]); touching without crossing does not enter.
- Exit (long only): `strategy.close("long", when = (crossunder(close, upper)))` — strict cross-under of the upper band; touching without crossing does not exit.
- Direction: long entry explicit; no `strategy.short` leg exists anywhere (0 occurrences) — short explicitly disabled per code.
- Opposite-signal exit: not applicable (no short side); the only exit is the upper-band signal exit above.
- Risk: stop loss none, take profit none, trailing stop none, time limit none — the only SL/TP/position-price lines in the file are commented out (`//Stop_loss`, `//Take_profit`, `//longStopPrice`, `//longTakeProfit`, `//closeLong`), i.e. author-considered and disabled. No silent defaults relied upon.
- Position / re-entry: `pyramiding` unset = Pine language default single position (no same-direction adds); no cooldown input; no `strategy.position_*` read; no position-aware state. After an exit, the next bar satisfying entry conditions re-enters immediately. Sizing lines (`initial_capital = 100`, `default_qty_type = strategy.percent_of_equity`, `default_qty_value = 100`) are event-neutral capital configuration, replaced by the house overlay.
- Order inventory (whole executable block): exactly one `strategy.entry` and one `strategy.close`; 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.cancel`, 0 `limit=`, 0 `stop=`, 0 `qty_percent`, 0 `request.*`, 0 `time(`, 0 `timenow`, 0 `timeframe.`, 0 `dayofweek`/`dayofmonth`/`hour`, 0 `volume`, 0 `openinterest`, 0 funding/OI/mark-price references.

**Lookback, formulas and warmup**

- Parameters as declared: DMI `diLength = 14`, `adxSmoothing = 14`; BB length 20 over `close`, multiplier 2.0 (population `stdev` as in v4 `stdev()`).
- All indicators are causal (current-bar `sma`/`stdev`/`dmi` over completed bars only); no `barssince` state machine, no negative shift, no future extrema, no full-sample normalization, no repaint path.
- Derived warmup: longest primitive lookback 20 (BB) plus Wilder-style DMI smoothing 14 — conservative derived warmup 40 completed 4h bars before the first signal bar is trusted.

## Required data

- 4h OHLC of the traded pair only (`open`/`high`/`low`/`close` via `close`, `hl`-based DMI internals, `sma`/`stdev` of `close`). No volume, no funding, no OI, no mark/index price, no order-book, no sentiment, no cross-venue state.

## Execution assumptions

- Engine: completed-bar decision with same-bar-close execution under the pinned Hummingbot baseline (`20260920` / `dev-2.17.0`), matching the source `process_orders_on_close=true` market-order semantics 1:1.
- Recalculation: neither `calc_on_every_tick` nor `calc_on_order_fills` appears in the declaration (0 occurrences of each); both default to `false` per official documentation. Recorded as source-declared-by-language-default; no intrabar re-evaluation can create a second order on the same bar.
- Research market (house overlay, explicitly labeled): `BTCUSDT` 4h. The FMZ block pins `Futures_Binance BTC_USDT` at `period: 4h`; the code itself is symbol-agnostic and the `basePeriod: 15m` is FMZ execution granularity, not a second decision timeframe — exactly one decision timeframe (`4h`) is admitted.
- Sizing/costs (house overlay, event-neutral, NOT source rules): Base Order 6% + Safety Order 6% + Safety Order 6%, Isolated, 3x/5x tested separately; pinned Binance non-VIP USDⓈ-M fees plus historical realized funding replace the source `commission 0.1% / percent_of_equity` lines. These affect PnL accounting only, never signal, timing, direction, entries, or exits.

## Evidence

### Source-reported

- The FMZ page embeds one backtest-settings image with no readable metric table; the prose claims suitability for sideways markets with no figure, table, or number. Census: zero exact empirical numbers on the page — none are recorded here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Pinned FMZ backtest window is one month (`2024-01-01` to `2024-01-31`); no claim is made about performance outside it, and none is repeated here.

## Falsification plan

- Recompute on 4h BTCUSDT: (a) entry bars must equal exactly the bars where `abs(+DM14 − −DM14) < 20` AND `close` crosses strictly over `sma20 − 2·stdev20`; (b) exit bars must equal exactly the bars where `close` crosses strictly under `sma20 + 2·stdev20`; (c) no short-side order may ever appear; (d) maximum same-side concurrency must never exceed 1. Any deviation falsifies the normalization.
- Research test only (never a substitute rule): if the long-only record shows no edge on full-history 4h data, that is a performance finding, not a licence to add a short leg or a stop — the source omits them and they must stay omitted.

## Crypto portability

- Directly portable within the house overlay: 4h BTCUSDT perpetual is one of the seven pinned baseline symbols; the rule uses only OHLC and needs no spot/short exemption analysis beyond the already-disabled short side. The `// Works on ETHUSD 3h, 1h, 2h, 4h` comment is a non-binding remark — only 4h is admitted by this record.

## Limitations

- Long-only by source construction: bear trends and range-breakdown legs produce no signal; flat through trends is by design, not a malfunction.
- The sideways gate uses a fixed spread threshold (20) with no volatility normalization — in sustained high-ADX regimes entries simply stop; in choppy low-spread regimes whipsaw entries are expected.
- BB `offset` input, date-window inputs, and the destructured `adx` are dead code; they cannot affect orders but document author iteration.
- One-month pinned source window means the source itself evidences almost nothing about robustness; downstream full-history screening must carry that weight.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib port, no parameter tuning, no Paper/Testnet/Live action taken or authorized by this record.

## Adoption boundary

- `not-approved`, `research-only`. Eligibility for Hummingbot/Qlib performance-research screening follows solely from `hb_ready_status: PASS`; profitability, survivor status, and any trading approval are explicitly NOT established by this record.

## Related Wiki records

- None.

## Sources

- Primary: https://www.fmz.com/strategy/442375 (mirror + live page re-verified 2026-10-07; last modified 2024-02-21).
- Pine v4 `strategy` declaration/execution semantics: https://www.tradingview.com/pine-script-reference/v4/#fun_strategy
- `strategy.entry` / `strategy.close` order semantics: https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}entry , https://www.tradingview.com/pine-script-reference/v4/#fun_strategy{dot}close
- `dmi` built-in semantics: https://www.tradingview.com/pine-script-reference/v4/#fun_dmi
- Strategy backtest/execution model: https://www.tradingview.com/pine-script-docs/concepts/strategies/
