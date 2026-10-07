---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Larry Williams three-period EMA high-low channel streak-gated trend long system on BTCUSDT 1d bars
created: 2026-10-07
updated: 2026-10-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2024-05-11
sources:
  - https://www.fmz.com/strategy/451075
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The FMZ demo backtest header prints period 1d with basePeriod 1h. The 1h granularity is FMZ execution resolution, not signal logic: every rule reads completed daily-bar values under process_orders_on_close=true with no intrabar, MTF, or clock call. The record pins the 1d decision timeframe; no 1h signal is inferred."
  - "The code contains a third exit branch reading na(time_close[0]). On completed historical bars the bar close time is always known, so under once-per-bar close evaluation this branch never fires; it is recorded as written and evaluated as inert, contributing no time-limit exit to the admitted rule."
---

# Larry Williams three-period EMA high-low channel streak-gated trend long system on BTCUSDT 1d bars

## Provenance

Primary source read end to end (FMZ strategy page mirror plus live re-verification):

- FMZ strategy: https://www.fmz.com/strategy/451075 (`拉里威廉姆斯三周期动态均线交易策略-Larry-Williams-Three-Period-Dynamic-Moving-Average-Trading-Strategy`, page author ChaoZhang; Pine strategy title `Larry Williams 3 Periodos Editável de MarcosJr`, `//@version=5`).
- Last modified (as printed on the page): 2024-05-11.
- FMZ backtest block pinned on the page: `start: 2023-05-05 00:00:00`, `end: 2024-05-10 00:00:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — single pair; the `1h` figure is FMZ demo-execution scope (see decision-timeframe note below), not a signal rule coded anywhere in the script.
- Live re-verification (2026-10-07): the FMZ page returns HTTP 200 (760835 bytes); the page title, the author (ChaoZhang), `period: 1d`, `Futures_Binance` / `BTC_USDT`, `process_orders_on_close=true`, the exact streak line (`checkThreeConsecutiveCandles = (close[0] > close[1] and ...)`), the exact order lines (`strategy.entry("Long", strategy.long, comment="Long", when=strategy.position_size == 0)`, `strategy.close("Long", comment="Close Long")`), `barstate.isconfirmed`, and the last-modified date (2024-05-11) all match the mirror. No live-page fact contradicts the mirror.
- Mirror executable block: one `strategy()` declaration (`overlay=true`, `process_orders_on_close=true`; no `calc_on_every_tick`, no `pyramiding`, no `max_bars_back`, no sizing/commission lines — Pine language defaults), dead date inputs (`startYear/startMonth/startDay/endYear/endMonth/endDay` computed into `startDate`/`endDate` but never read; `inDateRange = true` constant), `emaPeriodHighs = 3`, `emaPeriodLows = 3`, `emaH = ta.ema(high, emaPeriodHighs)`, `emaL = ta.ema(low, emaPeriodLows)`, display-only `plot(emaH)`/`plot(emaL)`, the streak definition, and exactly three live order calls: one `strategy.entry("Long", ...)`, two `strategy.close("Long", ...)` (signal exit plus the inert time branch).
- Censuses over the pinned block: `request.*` 0, `security(` 0, `timeframe` 0, `time(` 0, `timenow` 0, `dayofweek`/`hour` 0, `strategy.exit` 0, `strategy.order` 0, `strategy.close_all` 0, `strategy.cancel` 0, `stop=` 0, `limit=` 0, `crossover` 0, `crossunder` 0, `ta.cross` 0, `strategy.short` 0 live occurrences, `open`/`volume` 0 occurrences in trading logic (the only series read are `close`, `high`, `low`, plus bar `time` via the dead-constant window). `startDate`/`endDate` are written once and read zero times — dead code excluded from the normalized rule as written, not repaired. The rule contains 0 `crossover`/`crossunder` calls, so the prior-bar tie-semantics blocker that closed PR #6 cannot arise here.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-07): working-tree searches for `451075`, `larry`, `williams`, `emaL`, and `three-period` returned 0 matches. Open PRs: only #36 (reconstruction lane, no `research/*` collision). Closest records are different mechanism classes: `three-down-three-up-consec-close-long-btcusdt-1h-2026-10-07.md` (pure close-sequence counting with no indicator — entry fires ONLY on 3-down streaks, while this rule fires on either-direction streaks gated by an EMA high/low channel, and enters on 3-up streaks below the channel where that record exits-or-waits), and the EMA-trend family (`ema-20-50-cross`, `ema-cloud-7-20`, `dual-ema-engulfing-volume-long`, `octa-ema-ichimoku`, `flying-dragon-offset-ma-band` — cross/cloud/engulfing/ribbon/band constructions, none combining 3-monotonic closes with a 3-EMA high/low channel). Five-axis distinction: mechanism differs (streak-plus-channel breakout versus pure count or MA-cross/cloud), signal construction differs (`close<ema(low,3)` entry / `close>ema(high,3)` exit with an either-direction 3-streak gate versus count-only or cross logic), horizon is `1d` BTCUSDT long-only, source identity differs (FMZ 451075), direction handling is long-only by code (sole `strategy.long` entry, zero short calls).

## Economic mechanism

### Source-reported

A Larry Williams three-period dynamic-average trend long: two 3-period EMAs (one on highs, one on lows) form a tight price channel; a trade is considered only when the last three closes run monotonically in one direction (three rising or three falling closes in a row). A long opens when price sits below the low-EMA after such a streak, and closes when price pushes back above the high-EMA after such a streak. No stop, no target — the channel edges are the whole trade management.

### Research interpretation

Streak-confirmed channel-break trading: the 3-streak requirement demands directional conviction before any order, while the EMA(3) high/low channel demands price be extended outside the micro-range (below it for entry, above it for exit). Either-direction streaks qualify, so continuation streaks (3-up while still below the channel) can trigger entries — the opposite of pure down-count mean reversion. No leverage, sizing, or cost edge is embedded in the signal; the source declares no sizing/commission lines at all (Pine defaults), replaced event-neutrally by the house overlay (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Inputs: `emaPeriodHighs = 3`, `emaPeriodLows = 3`, `inDateRange = true` (constant; the date inputs are dead), overbought/oversold-style threshold inputs: none exist — there are no level parameters anywhere.
- Channel: `emaH[t] = ta.ema(high, 3)[t]`, `emaL[t] = ta.ema(low, 3)[t]` (v5 built-in EMA, standard `alpha = 2/(3+1)` smoothing; `high`/`low` are the traded-bar extremes, no off-chart series).
- Streak gate: `checkThreeConsecutiveCandles[t] = (close[t] > close[t-1] and close[t-1] > close[t-2] and close[t-2] > close[t-3]) or (close[t] < close[t-1] and close[t-1] < close[t-2] and close[t-2] < close[t-3])`. Strict inequalities: any equality inside the 4-close window falsifies that leg — the tie case is defined, not ambiguous.
- Entry (long-only): `if (close[t] < emaL[t] and true and checkThreeConsecutiveCandles[t] and barstate.isconfirmed[t])` → `strategy.entry("Long", strategy.long, comment="Long", when=strategy.position_size == 0)`. The flat-book gate means entries fire only with no open position; while long, further entry evaluations are rejected deterministically.
- Exit (full close of the one long): `if (close[t] > emaH[t] and true and checkThreeConsecutiveCandles[t] and barstate.isconfirmed[t])` → `strategy.close("Long", comment="Close Long")`. Evaluated on a flat book it is a deterministic no-op.
- Conflict priority (proven, not assumed): in the normal channel state (`emaL[t] <= emaH[t]`) entry and exit are mutually exclusive (one close cannot be both strictly below `emaL` and strictly above `emaH`). In the transient inverted state (`emaH[t] < close[t] < emaL[t]`) both conditions can fire on one bar; code order governs — entry is evaluated first (blocked unless flat), then the exit. With a flat book an inverted-channel streak bar prints an open-then-close round trip; with an open long the entry is blocked and the exit closes. All four state combinations resolve deterministically with no priority invention.
- `barstate.isconfirmed` plus `process_orders_on_close=true` with `calc_on_every_tick` unset (Pine default `false`): once-per-bar evaluation on the completed bar — no intrabar path exists.
- Re-entry: after an exit the book is flat, so the next bar satisfying entry conditions opens a fresh long. No cooldown is declared and none is needed: re-entry requires the flat state plus a fresh true evaluation, so cooldown semantics are provably irrelevant rather than missing.
- Opposite-signal exit: not applicable — there is no short side (zero short calls); the long is exited only by the channel-plus-streak rule above.
- Stop loss / take profit / trailing / time limit as orders: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`). The `na(time_close[0])` branch is unreachable on completed bars (a completed bar always has a known close time), so no time-limit exit exists in backtest semantics. An adverse drift of any size exits nothing until a 3-streak close above `emaH` prints. No silent Hummingbot defaults are relied upon.

## Required data

- Completed `1d` bars of BTCUSDT: `close`, `high`, `low` only. `open`, `volume` occur 0 times in the trading logic; no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, or cross-venue state is read.
- Single decision timeframe `1d` (explicitly labeled research timeframe under the house overlay; the script is timeframe-agnostic with 0 timeframe references, so no cross-timeframe dependency and no causal alignment is owed). The `basePeriod: 1h` figure is FMZ demo-execution resolution only.
- Warmup: the streak chains on `close[3]` and the channel on `ta.ema(..., 3)`; first possible signal at bar index 3 (the 4th completed bar). No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT under the house overlay (source venue is Binance USDT-M BTC futures; the system is long-only, so no naked-spot-short construction is required or assumed).
- Order timing: all live order calls run under `process_orders_on_close = true`: completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the source declares no sizing, capital, margin, or commission lines (Pine language defaults apply and affect no event); the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5×) and pinned house cost assumptions apply as pure accounting and do not alter signal, timing, direction, or exits. They are never presented as source-native behavior.
- Concurrency: at most one open long (single entry id, flat-book entry gate, default single-position declaration); no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The FMZ page and its embedded description carry no numeric performance claims — no ROI, Sharpe, win rate, drawdown, or trade-count figures appear anywhere in the artifact (the single backtest chart image ships without any numeric caption). Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Entry/exit co-fire is impossible in the normal channel state (strict `< emaL` versus strict `> emaH` with `emaL <= emaH`) — verified by language semantics, not by backtest; the inverted-channel dual-fire resolves by code order (entry first, exit second), documented above.
2. Exact-equality closes inside the streak window falsify that streak leg — defined, so ties extend the holding/wait rather than firing either leg.
3. `strategy.close("Long")` on a flat book is a deterministic no-op — it opens nothing and inverts nothing.
4. `inDateRange`, `startDate`, `endDate` are write-once/read-never or constant-true: no hidden session filter alters any in-scope event.
5. The `na(time_close[0])` exit branch never fires on completed bars — inert dead code, not a second exit rule.
6. No price-level exit exists: a waterfall decline with no 3-streak close above `emaH` rides the full drawdown — the hold is unbounded by construction (see Limitations).

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 3/3 EMA channel, either-direction 3-streak gate, long-only, `1d` BTCUSDT, same-bar-close fills are frozen.

- F1 — Channel relevance: on full-history 1d BTCUSDT, streak-gated entries below `ema(low,3)` must show better forward drift than streak-only entries net of the house overlay; fail ⇒ the channel leg adds nothing.
- F2 — Exit relevance: replacing the channel-plus-streak exit with a fixed 5-bar time exit must not improve net expectancy; fail ⇒ the exit leg is decorative.
- F3 — Streak sensitivity: the 2-streak and 4-streak variants must not both dominate the 3-streak rule net of costs; fail on both sides ⇒ the 3-bar choice is arbitrary rather than structural.
- F4 — Variant discipline: any EMA-length change (e.g. 5/5, 10/10) is a separate variant record, never silently merged; if one dominates, that is a new record, not a repair of this one.

## Crypto portability

Pinned to BTCUSDT (Binance USDT-M lineage) under the house overlay. Long-only channel-streak logic ports to spot or perps without structural change; no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state.

## Limitations

- No risk exit: without a stop, a waterfall decline with no qualifying streak-close above `emaH` rides the full drawdown; the book can stay long through an entire regime fall.
- No participation while waiting: produces zero trades outside qualified streak-plus-channel bars; the book sits flat through entire trends that never print the exact pattern, not hedged.
- Streak fragility: a single flat or counter-tick close breaks the 4-close chain, so near-miss sequences never fire despite sustained directional drift.
- Tight 3-EMA channel whipsaws: `ema(high,3)`/`ema(low,3)` hug price, so choppy markets can alternate entry/exit evaluations bar after bar under the house overlay.
- Source demo window is one year (2023-05-05 → 2024-05-10); full-history behavior is unreported by the source and unclaimed here.
- The source declares no sizing/commission model; expectancy comparisons must use the house overlay, never Pine defaults.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.fmz.com/strategy/451075 (mirror + live page re-verified 2026-10-07; last modified 2024-05-11).
- Pine v5 `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Pine v5 `strategy.entry` semantics: https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
