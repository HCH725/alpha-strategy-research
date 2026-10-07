---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Three-down-three-up consecutive-close mean-reversion long system on BTCUSDT 1h bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2025-02-19
sources:
  - https://www.fmz.com/strategy/482589
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ demo backtest header prints period 1h (2025-01-19 to 2025-02-18), but the pinned Pine script itself contains zero timeframe references (0 request/security/timeframe calls). The record pins 1h as the explicitly labeled research decision timeframe under the house overlay — the FMZ demo scope's own timeframe, adopted as the research frame, not a source-declared signal timeframe."
---

# Three-down-three-up consecutive-close mean-reversion long system on BTCUSDT 1h bars

## Provenance

Primary source read end to end (FMZ strategy page mirror plus live re-verification):

- FMZ strategy: https://www.fmz.com/strategy/482589 (`均值回归型连续K线反转交易策略-Mean-Reversion-Consecutive-Candle-Reversal-Trading-Strategy`, page author ChaoZhang; Pine strategy title `3 Down, 3 Up Strategy`, `//@version=6`).
- Last modified (as printed on the page): 2025-02-19 10:51:35.
- FMZ backtest block pinned on the page: `start: 2025-01-19 00:00:00`, `end: 2025-02-18 00:00:00`, `period: 1h`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1h` figure is FMZ demo-execution scope (see decision-timeframe note below), not a signal rule coded anywhere in the script.
- Live re-verification (2026-10-07): the FMZ page returns HTTP 200 (754045 bytes); the page title (`Mean Reversion Consecutive Candle Reversal Trading Strategy | FMZ`), the author (ChaoZhang), the Pine title (`3 Down, 3 Up Strategy`), `process_orders_on_close = true`, the exact counter lines (`aboveCount := close > close[1] ? ...`, `belowCount := close < close[1] ? ...`), the exact condition lines (`longCondition = belowCount >= buyTriggerInput and isWithinTradingWindow`, `exitCondition = aboveCount >= sellTriggerInput`), the exact order lines (`strategy.entry("Long", strategy.long)`, `strategy.close_all()`), the default-off EMA filter (`useEmaFilter = input.bool(false, ...)`), and the last-modified stamp (2025-02-19) all match the mirror. No live-page fact contradicts the mirror.
- Mirror executable block: one `strategy()` declaration (`"3 Down, 3 Up Strategy"`, `overlay=true`, `process_orders_on_close = true`, `calc_on_every_tick = true`, no `pyramiding`, no `max_bars_back`), dead time-window inputs (`startTimeInput`/`endTimeInput` declared but never read; `isWithinTradingWindow = true` constant), `buyTriggerInput = input.int(3, ...)`, `sellTriggerInput = input.int(3, ...)`, `useEmaFilter = input.bool(false, ...)`, `emaPeriodInput = input.int(200, ...)`, the two `var int` counters, `emaValue = ta.ema(close, emaPeriodInput)` (computed but gated behind the default-off filter), and exactly two live order calls: one `strategy.entry("Long", strategy.long)`, one `strategy.close_all()`.
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.close(` 0, `stop=` 0, `limit=` 0, `crossover` 0, `crossunder` 0, `ta.cross` 0, `strategy.short` 0 live occurrences, `open`/`high`/`low`/`volume` 0 occurrences in trading logic (the only series read is `close`, plus bar `time` via the dead-constant window). `startTimeInput`/`endTimeInput` are written once and read zero times — dead code excluded from the normalized rule as written, not repaired.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-07): working-tree searches for `482589`, `belowCount`, and `consecutive.*candle` returned 0 matches. Open PRs: only #36 (reconstruction lane, no `research/*` collision). Closest records are different mechanism classes: `ibs-mean-reversion-short-ethusdt-1h-2026-10-06.md` (mean reversion via the internal-bar-strength position-within-range ratio, short side, threshold exit — not consecutive-close counting) and `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` (oscillator-level signal, not close-sequence counting). Five-axis distinction: mechanism differs (3-consecutive-lower-close entry plus 3-consecutive-higher-close exit versus IBS-ratio or RSI-level signals), signal construction differs (strict close-vs-prior-close chains with equality resetting both counters versus range-position or oscillator thresholds), horizon is `1h` BTCUSDT long-only, source identity differs (FMZ 482589, Pine title `3 Down, 3 Up Strategy`), direction handling is long-only by code (sole `strategy.long` entry, zero short calls).

## Economic mechanism

### Source-reported

A consecutive-close mean-reversion long: it waits until sellers print three straight lower closes in a row (short-horizon decline judged exhausted), opens a long, and holds until buyers print three straight higher closes in a row, then closes everything. No stop, no target — the exit is purely the mirror-image count.

### Research interpretation

Short-horizon snap-back harvesting with symmetric count symmetry: the `3-down` leg buys only into washed-out sequences, the `3-up` leg demands a confirmed recovery sequence before banking. The optional EMA-200 filter exists in code but defaults OFF and is pinned OFF here, so the admitted system is pure close-sequence counting. No leverage, sizing, or cost edge is embedded in the signal; the source `percent_of_equity`/`margin_*` lines are capital configuration replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v6, defaults quoted — inputs unmodified):

- Inputs: `buyTriggerInput = 3`, `sellTriggerInput = 3`, `useEmaFilter = false`, `emaPeriodInput = 200` (inert while the filter is OFF), `isWithinTradingWindow = true` (constant; the timestamp inputs are dead).
- Counters (state carried bar to bar, seeded `na` then 1-or-0): `aboveCount[t] = (close[t] > close[t-1]) ? ((na(aboveCount[t-1])) ? 1 : aboveCount[t-1] + 1) : 0`, `belowCount[t] = (close[t] < close[t-1]) ? ((na(belowCount[t-1])) ? 1 : belowCount[t-1] + 1) : 0`. Strict inequalities: a doji bar (`close[t] == close[t-1]`) resets BOTH counters to 0 — the tie case is defined, not ambiguous. The rule contains 0 `crossover`/`crossunder` calls, so the prior-bar tie-semantics blocker that closed PR #6 cannot arise here.
- Entry (long-only): `longCondition[t] = (belowCount[t] >= 3) and true`, live via `if longCondition` → `strategy.entry("Long", strategy.long)`. The EMA-filter branch (`if useEmaFilter` → `longCondition := longCondition and close > emaValue`) is pinned inactive by the default `false`; the admitted rule never evaluates it.
- Exit (full close of the book): `exitCondition[t] = (aboveCount[t] >= 3)`, live via `if exitCondition` → `strategy.close_all()`. With the long-only book, `close_all()` closes exactly the one open long; evaluated on a flat book it is a deterministic no-op.
- Mutual exclusion (proven, not assumed): `belowCount[t] >= 3` requires `close[t] < close[t-1]`; `aboveCount[t] >= 3` requires `close[t] > close[t-1]`; one bar cannot satisfy both, and equality zeroes both. Entry-before-exit code order therefore needs no priority ruling — both branches can never fire on the same bar.
- Re-entry: after an exit the book is flat, so the next bar with `longCondition[t]` true opens a fresh long. While long, further entry signals are rejected under the default single-position declaration (`pyramiding` unset = language-default no pyramiding). No cooldown is declared and none is needed: re-entry requires the flat state plus a fresh true evaluation, so cooldown semantics are provably irrelevant rather than missing.
- Opposite-signal exit: not applicable — there is no short side (zero short calls); the long is exited only by the 3-up-close rule above.
- Stop loss / take profit / trailing / time limit as orders: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`). There is no price-level exit anywhere: an adverse drift of any size exits nothing until three consecutive higher closes print. No silent Hummingbot defaults are relied upon.

## Required data

- Completed `1h` bars of BTCUSDT: `close` only. `open`, `high`, `low`, `volume` occur 0 times in the trading logic; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, or cross-venue state is read.
- Single decision timeframe `1h` (explicitly labeled research timeframe under the house overlay; the script is timeframe-agnostic with 0 timeframe references, so no cross-timeframe dependency and no causal alignment is owed). The constant `isWithinTradingWindow` reads no bar time at decision — causal, no future reference.
- Warmup: the counters chain on `close[1]`, needing 3 directed closes; first possible signal at bar index 3 (the 4th completed bar). `ta.ema(close, 200)` is computed in code but gated behind the pinned-OFF filter and affects no admitted event; pinned-OFF warmup is 4 bars. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the system is long-only, so no naked-spot-short construction is required or assumed).
- Order timing: the two live order calls run under `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. `calc_on_every_tick = true` is recorded as written — it permits intrabar script recalculation, but with close-gated order processing no intrabar order, price, or path-dependent fill exists anywhere in the rule. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: source `default_qty_type = strategy.percent_of_equity, default_qty_value = 200`, `initial_capital = 1000000`, and `margin_long = 5, margin_short = 5` are event-neutral capital configuration, replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and never presented as source-native behavior. The source declares no commission model; the pinned house cost assumptions apply as pure accounting and do not alter signal, timing, direction, or exits.
- Concurrency: at most one open long (single entry id, default single-position declaration); no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page and its embedded description carry no numeric performance claims — no ROI, Sharpe, win rate, drawdown, or trade-count figures appear anywhere in the artifact (the single backtest chart image ships without any numeric caption). Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Entry/exit co-fire is impossible (strict `<` versus strict `>` on the same `close[t]` vs `close[t-1]` pair; equality zeroes both) — verified by language semantics, not by backtest.
2. Exact-equality bars (`close[t] == close[t-1]`) reset both counters — defined, so ties extend the holding/wait rather than firing either leg.
3. `strategy.close_all()` on a flat book (exit condition true while flat, e.g. three up-closes with no position) is a deterministic no-op — it opens nothing and inverts nothing.
4. Enabling the EMA filter (`useEmaFilter = true`) would be a different, unpinned rule (adds `close > ema(close, 200)` to entries and a 200-bar warmup); the admitted record pins the default OFF.
5. `startTimeInput`/`endTimeInput` are write-once/read-never: no hidden session filter alters any in-scope event.
6. No price-level exit exists: a vertical adverse move with no 3-up sequence exits nothing — the hold is unbounded by construction (see Limitations).

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `3-down` entry, `3-up` exit, EMA filter OFF, long-only, `1h` BTCUSDT, same-bar-close fills are frozen.

- F1 — Entry relevance: on full-history 1h BTCUSDT, longs opened after 3 consecutive lower closes must show better forward drift than unconditional longs net of the house overlay; fail ⇒ the down-count leg adds nothing.
- F2 — Exit relevance: replacing the 3-up-close exit with a fixed 5-bar time exit must not improve net expectancy; fail ⇒ the up-count leg is decorative.
- F3 — Count sensitivity: the (2,2) and (4,4) count variants must not both dominate (3,3) net of costs; fail on both sides ⇒ the 3/3 choice is arbitrary rather than structural.
- F4 — Filter discipline: enabling the EMA-200 filter must be evaluated as a separate variant, never silently merged; if it dominates, that is a new record, not a repair of this one.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. Long-only close-sequence logic ports to spot or perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state.

## Limitations

- No risk exit: without a stop, a waterfall decline with no 3-up interlude rides the full drawdown; the book can stay long through an entire regime fall.
- No participation while waiting: produces zero trades outside 3-down sequences; the book sits flat through entire rallies, not hedged.
- Count fragility: a single doji or counter-tick close resets the chain to 0, so near-miss sequences (down, down, flat, down, down) never fire despite five weak closes in six bars.
- Source demo window is one month (2025-01-19 → 2025-02-18); full-history behavior is unreported by the source and unclaimed here.
- Source `percent_of_equity 200` / `margin 5` sizing in the source is replaced event-neutrally by the house overlay; expectancy comparisons must use the overlay, never the source sizing.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/482589 (mirror + live page re-verified 2026-10-07; last modified 2025-02-19 10:51:35).
- Pine v5 `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine v5 `strategy.entry` semantics: https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
