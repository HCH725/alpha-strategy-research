---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Woodies CCI zero-line-reject and turbo-cross ATR-bracket trend two-sided on BTCUSDT 1h bars
created: 2026-10-23
updated: 2026-10-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-23
sources:
  - https://www.tradingview.com/script/uC1oajDr-Woodies-CCI-Trend-Strategy-Zero-Line-Reject-Turbo-Cross/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Woodies CCI zero-line-reject and turbo-cross ATR-bracket trend two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Stable public URL: https://www.tradingview.com/script/uC1oajDr-Woodies-CCI-Trend-Strategy-Zero-Line-Reject-Turbo-Cross/ (`Woodies CCI Trend Strategy | Zero-Line Reject & Turbo Cross`, author `blitz_locked`, `OPEN-SOURCE SCRIPT`, Mozilla Public License 2.0 header, `Pine Script v6`, `strategy()` — a real strategy account, not a study).
- As-of: the page exposes no publish date (no time meta found at fetch); observed `9` boosts / `177` views on 2026-10-23, consistent with a days-old script. Record `source_as_of` is the fetch-and-read date `2026-10-23`, never an invented publish date. The page's own prose (`How it works`, `Features`, `Tips`, `Warnings`) was read and agrees with the code on trend confirmation, both entry modes, filters, ATR stop/target, and flip/zero exits — prose never overrides code below.
- Code identity: the `Source code` tab prints `205` numbered lines (`View in Pine Editor - 205 lines`, observed). The full fenced block (MPL header through the entry-marker `plotshape` calls) was read verbatim across two fetches this cycle; code-only slice length `10749` characters. No revision history ships on the page, so this record pins the observed block exactly as read — any later author edit is a different, unpinned rule.
- The file's own words (quoted for gate evidence, never extended): `strategy("Woodies CCI Strategy", shorttitle="Woodies CCI Strat", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=20, commission_type=strategy.commission.percent, commission_value=0.05, slippage=1, initial_capital=10000, pyramiding=0, calc_on_every_tick=false)` — one `strategy(` declaration; no `process_orders_on_close` ships anywhere (Pine default `false` applies — disclosed default, never a file literal); no `max_bars_back`, no `margin_*`, no `fill_*` call ships anywhere.
- Full-block token census (verified over the code-only slice this cycle): 2 `strategy.entry` (exactly the `Long`/`Short` calls, no other entry call); 2 `strategy.exit` (exactly the `XL`/`XS` bracket calls); 2 `strategy.close` (exactly the flip-exit calls); 0 `strategy.order`; 33 `input.*` (every literal below is a pinned default — zero unlisted constants gate any order); 0 `request.*`; 0 `security(`; 0 `volume`; 0 `barstate.*`; 0 `timeframe*`; 1 `syminfo` (the visuals-only `atrSafe = math.max(atr, syminfo.mintick)` candle-color denominator — never read by any order-gating line, fenced); 4 bare `time` tokens (exactly the two `input.time` declarations plus the two `inWindow` comparisons — the whole date-window branch is dead at the pinned `useDate = false` default, fenced); 2 `ta.crossover` (exactly `turboLong` and the dead-by-default `shortExit` zero leg); 2 `ta.crossunder` (exactly `turboShort` and the dead-by-default `longExit` zero leg).
- All 33 input defaults pinned (grouped as shipped): CCI Setup `cciSrc = hlc3`, `cci14Len = 14`, `turboLen = 6`, `barsBT = 4`; Entry Logic `entryMode = "Both"`, `pbLookback = 5`, `zlrNear = 50.0`, `zlrFloor = 100.0`, `maxCCIEntry = 200.0`, `useHookFade = false`, `extremeLvl = 200.0`; Trend Filters `useEmaFilt = true`, `emaLen = 34`, `useLsmaFilt = true`, `lsmaLen = 25`, `useSlopeFilt = false`, `minSlopeAtr = 0.05`; Risk Management `atrLen = 14`, `slMult = 2.0`, `tpMult = 3.0`, `exitOnFlip = true`, `exitOnZero = false`, `allowLong = true`, `allowShort = true`; Backtest Window `useDate = false`, `startDate = 2020-01-01`, `endDate = 2030-01-01`; Visuals `colMode = "Standard"`, `showFill = true`, `showBars = true`, `showLevels = true`, `showLsma = false`, `barSmooth = 5`. Every non-default option (single entry modes, slope filter, fade hook, zero exit, date window, color modes, all visual toggles) is a dead branch at pinned defaults — fenced, never adopted.
- Out-of-file calls pinned by name to documented Pine v6 semantics (no hidden library): `ta.cci(src, len)` is the Lambert CCI `(src - SMA(src,len)) / (0.015 * meanAbsDev(src,len))` — mean absolute deviation, never standard deviation; `ta.atr(14)` is the RMA-smoothed true range; `ta.ema(close, 34)` is the standard EMA; `ta.linreg(close, 25, 0)` is the least-squares endpoint estimate; `ta.lowest/highest(cci, 5)[1]` are 5-bar extrema excluding the decision bar; `ta.crossover(a,b) = (a > b) and (a[1] <= b[1])`, `ta.crossunder` the mirror. No repainting construction exists: only `[1]`/`[2]` historical offsets, `calc_on_every_tick = false` (completed-bar evaluation only), no intrabar state anywhere in the gating path.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the author's TradingView deployment. The source pins the Pine v6 construction, all 33 defaults, the two-sided stance, the ATR-bracket risk legs, the flip-close leg, and the 0.05%-per-side plus 1-tick cost model — but ships no market and no chart timeframe. Researcher-declared adaptations are exactly five, all predeclared here: (1) research market `BTCUSDT` on Binance (venue spelling and symbol normalization are the only market steps; no source-market equivalence is claimed); (2) decision timeframe `1h` (the script is timeframe-agnostic; the author's own Tips point at intraday use, and `1h` rides deep pool precedent — disclosed choice, never a source fact); (3) completed-bar decisions with next-bar-open market fills (the source's own Pine-default timing, preserved — not converted to same-bar-close); (4) a 150-bar researcher warmup floor held flat (the script ships no warmup guard — disclosed pin); (5) house capital/leverage overlay beneath the source-native sizing and costs (see Execution assumptions). The indicator constructions, all thresholds, both entry modes, the filters, the bracket multiples, the flip-close leg, the two-sided stance, and the cost literals are source-native and unmodified.

Pre-write dedup (2026-10-23): working-tree content search (case-insensitive) for `woodies`, `zero-line reject`, `zlr`, `turbo cross`, `turboLong`, `blitz_locked` returns zero strategy records. CCI cousins in the pool are fenced as different constructions in Negative evidence 6 — none conjoins a side-of-zero N-bar trend latch with a ZLR-hook-plus-Turbo-cross trigger pair, EMA34/LSMA25 filters, a |CCI| ceiling, and a per-trade ATR bracket. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a Woodies-CCI rule. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only qualitative behavior (its page prose plus what the code prints): read which side of zero CCI(14) sits on to define the trend (confirmed after `barsBT + 1` bars), buy pullback-hook and fast-Turbo-cross entries in that direction behind EMA/LSMA filters while skipping overextended prints, and manage every trade with an ATR-anchored stop and target plus a trend-flip close. No behavioral, structural, or risk-premium channel beyond pullback-plus-confirmation trend following is claimed, and no performance numbers are printed anywhere in the 205 lines — this record adopts none.

### Research interpretation

Side-of-zero trend-latch impulse machine, two-sided. Unlike bare CCI-threshold records (fire on any extreme print), nothing fires until CCI has held one side of zero for five straight bars — a single-bar zero touch never confirms a trend and never arms a trigger. Unlike cross-only records, the ZLR leg buys the pullback geometry (dip toward zero without violating the counter-side floor, then hook back above the pullback extreme) while the Turbo leg buys fast-line confirmation (CCI(6) crossing CCI(14) on the trend side of zero) — either trigger suffices in `Both` mode, but both are gated by the same latch, the same EMA34/LSMA25 filters, and the same |CCI| < 200 anti-chase ceiling. The coded consequence is a buyer of trend-confirmed pullbacks that refuses both chop (filters) and exhaustion (ceiling), then holds each unit behind a fixed 2R bracket (2.0x stop, 3.0x target from the fill) until the bracket or the opposite trend confirmation takes it off. The failure mode is plain: a latch that flips every few bars exits winners at the flip-close and re-enters the new direction immediately — whipsaw is the principal friction, disclosed, not repaired.

## Signal

Exact rule as pinned (any other length, threshold, price input, edge/level choice, mode, filter, multiple, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; Pine primitives expand to their documented v6 definitions:

```text
cci14[t] = CCI(hlc3, 14)          // Lambert, mean-abs-dev denominator
turbo[t] = CCI(hlc3, 6)
atr[t]   = ATR(14)                // RMA true range
ema34[t] = EMA(close, 34)
lsma[t]  = linreg(close, 25, 0)   // endpoint estimate
barsAbove[t] = cci14>=0 ? barsAbove+1 : 0      // CCI exactly 0 counts as above
barsBelow[t] = cci14<0  ? barsBelow+1 : 0
trend[t] = 1  if barsAbove>=5; -1 if barsBelow>=5; else latched prior (starts 0)
trendFlipUp[t]   = (trend==1)  and (trend[1]!=1)
trendFlipDown[t] = (trend==-1) and (trend[1]!=-1)
lowRecent[t]  = lowest(cci14,5)[1];  highRecent[t] = highest(cci14,5)[1]
hookUp[t]   = cci14>cci14[1] and cci14[1]<=cci14[2]
hookDown[t] = cci14<cci14[1] and cci14[1]>=cci14[2]
zlrLong[t]  = trend==1  and lowRecent<=50  and lowRecent>=-100 and hookUp   and cci14>lowRecent
zlrShort[t] = trend==-1 and highRecent>=-50 and highRecent<=100 and hookDown and cci14<highRecent
turboLong[t]  = trend==1  and cci14>0 and crossover(turbo,cci14)[t]
turboShort[t] = trend==-1 and cci14<0 and crossunder(turbo,cci14)[t]
longFilt[t]  = (close>ema34)  and (lsma>lsma[1])    // slope leg true by default
shortFilt[t] = (close<ema34)  and (lsma<lsma[1])
longSignal[t]  = (zlrLong or turboLong)   and longFilt  and cci14<200
shortSignal[t] = (zlrShort or turboShort) and shortFilt and cci14>-200
exit: long SL = fill - entryAtr*2.0, long TP = fill + entryAtr*3.0 (mirror short),
      entryAtr = signal-bar ATR(14); flip-close on trendFlipDown/Up
floor = leading-window bars: unseeded prints compare false (see Required data)
```

- Trade events: a completed `1h` bar printing `longSignal` opens the full long unit when flat; `shortSignal` mirrors. A bar printing the opposite signal while positioned reverses the book (see ordering pin below). The bracket legs and the flip-close leg close the full unit. Pre-first-signal and pre-warmup bars are flat by record rule.
- Exact boundaries (pinned semantics): the latch admits `cci14` exactly `0` as above (`>= 0` vs `< 0` is exhaustive — no dead zone); the ZLR floor admits `lowRecent` exactly `-100` / `highRecent` exactly `100` and the near leg admits exactly `50`; the hook admits equality on the middle bar (`cci14[1] <= cci14[2]`); the ceiling is strict (`cci14 < 200`, `cci14 > -200` — a print exactly at `200` buys nothing); filters are strict (`close` exactly on `ema34`, or `lsma` exactly flat, fails); `barsBT + 1 = 5` straight bars confirm. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required at defaults): `longSignal` needs `trend == 1` while `shortSignal` needs `trend == -1` on the same bar — the latch holds one value, so both signals never co-print (the fade legs that could bypass the latch are `false` at pinned defaults). Entry-vs-own-flip co-print is likewise impossible (a flip-down needs `trend == -1`, a long signal needs `trend == 1`). The reviewer is never asked to invent an ordering for signal ties.
- Ordering pin (predeclared derivation, source-faithful): the script's `EXECUTION` block submits entries before closes in code order with `pyramiding = 0`, so a same-bar opposite-signal reversal nets to ONE position change (close-then-open atomic at the next open) — never two fills. Completed-bar evaluation order per bar: (1) bracket legs on the fill-bar-onward range with TP-before-SL precedence (the pinned simulator's own `CloseType` order), (2) flip-close at the bar close, (3) next-signal evaluation. At most one net position change per bar by construction plus the exclusion proof.
- Direction: two-sided at pinned defaults (`allowLong` and `allowShort` both true; both `strategy.long` and `strategy.short` entries present). The short leg requires margin — the house futures overlay applies (as with the admitted two-sided Stochastic-OTT reversal record); no side is disabled or fenced.
- Exits and risk (explicit, complete): the per-trade 2.0x-ATR stop and 3.0x-ATR limit (OCA bracket anchored to `position_avg_price`, `entryAtr` frozen at the signal bar, `tpMult = 3.0 > 0` so the limit is live) plus the trend-flip market close (`exitOnFlip = true`) are the complete position-closing set. No trailing, no time exit, no breakeven move — explicitly none, not invented. The `exitOnZero` legs, the fade-hook entries, the slope filter, and the date window are shipped-but-disabled branches (`false` at defaults) — recorded as explicitly disabled, never as missing rules.
- Position rule (source-native): `pyramiding = 0` — at most one unit per market; a positioned book treats same-side signal bars as hold-no-ops; the opposite signal reverses atomically; re-entry after any exit needs only the next qualifying signal bar (no cooldown specified — explicitly none, not invented). No DCA, no averaging, no `position_adjustment` concept ships anywhere.
- Determinism note for the reviewer: the gating path reads only completed-bar OHLC (`hlc3` for both CCIs, `close` for EMA/LSMA, `high`/`low`/`close` for ATR) with fixed non-negative offsets — no volume, funding/OI/mark-price, `request.*`, `security()`, `barstate.*`, `timeframe*`, session/calendar, resample, hyperopt, or stop/limit argument beyond the pinned multiples anywhere in the gating path. The `syminfo.mintick` read and all `input.time`/`time` reads live in visuals-only or dead-by-default branches, fenced above.

## Required data

- Completed `1h` bars of BTCUSDT: `open`/`high`/`low`/`close` (the `hlc3` transform feeds both CCIs; `close` seeds EMA/LSMA; `high`/`low`/`close` feed ATR; the range evaluates the bracket). No bar `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher pin — the script is timeframe-agnostic; see derivation declaration). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the next bar's open under the source's own Pine-default timing below.
- Warmup (researcher pin, disclosed): 150 one-hour bars held flat. Covers the EMA34 convergence tail (dominant), the LSMA25 seed, the RMA-ATR14 seed (~28 bars), the CCI14 seed, the 5-bar extrema-plus-one lag, and the 5-bar latch with margin. Coded behaviour underneath: Pine seeds prints `na` until windowed and every `na` comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (source-native, preserved): completed-bar decision with next-bar-open market fills — the script ships no `process_orders_on_close`, so Pine fills market orders at the next tick (the next bar's open under `calc_on_every_tick = false`); this record preserves that timing instead of converting it to same-bar-close. The flip-close market order fills at the next bar's open the same way. Barriers go live from the fill bar's own range onward (the fill bar's high/low can take a fresh position — fully specified, matching both Pine intrabar-stop behavior and the pinned simulator's per-row range logic).
- Engine path (exact, disclosed): the specified single-frame completed-bar `1h` Binance candle path the admitted `1h` cohort already rides — decision/availability timestamps, fills, costs, and leverage/margin accounting ride that path. Risk legs map onto the pinned backtesting tree's own triple-barrier machinery (`HCH725/hummingbot@8b0e067`, `hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py`, the same simulator the review policy cites): per-position `take_profit` = 3.0x signal-bar ATR above the fill and `stop_loss` = 2.0x below it (mirror short), evaluated on each bar's high/low touch with the simulator's own TP-before-SL `CloseType` precedence; the flip-close maps to the controller-level early market close on the completed-bar trend state, filled next open, subordinate to any same-bar barrier touch. Pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships its own economics and this record adopts them verbatim — 20% of current equity per trade (`default_qty_value = 20`, compounding, source-native), 0.05% commission per side, 1 tick slippage. Barrier levels derive from the slippage-inclusive fill price (deterministic); commission changes only the performance report, never whether a trigger fires (disclosed). Funding accrues from the realized historical Binance funding series while positioned (signed by side — longs pay when the realized rate is positive), never assumed zero; any run substituting a zero/constant funding series is a different, unpinned rule. Quantity is rounded down to the venue lot step with the venue minimum-notional enforced; sizing is event-neutral (all barriers are price-level and the liquidation gap is relative), so sizing changes no event. Leverage/margin ride the house overlay (Isolated, 3x/5x); the 2.0x-ATR(14) stop binds far inside the isolated-liquidation gap in ordinary tape, and any bar whose range touches both the stop and the venue liquidation price closes the unit flat at the worse of the two (conservative tail rule, predeclared — not a second risk leg).
- Concurrency: at most one position per market at any time; the qualifying signal opens the full 20%-equity unit on a flat book; the bracket, the flip-close, or the liquidation tail rule closes it in full; re-entry needs only the next qualifying signal bar. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The script ships the full construction (205 lines: the `strategy()` declaration, all 33 input defaults, the CCI/Turbo/ATR/EMA/LSMA block, the latch, both trigger geometries, the filters, the ceiling, the entry/bracket/flip-close execution block, and visuals). It ships no sample, window, trade count, or cost basis beyond the 0.05%-per-side plus 1-tick model — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: Pine prints `na` until each window seeds and every `na` comparison is false — no early latch, no early trigger, no early bracket. The 150-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The script ships no warmup guard, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: latch and ZLR legs admit equality where coded (`>= 0`, `<= 50`, `>= -100`, middle-bar `<=`/`>=`); the ceiling, filters, and Turbo edges are strict — a print exactly at `|CCI| = 200` buys nothing while a pullback extreme exactly at the floor still qualifies. Strictness preserved throughout — disclosed, not smoothed.
3. Latch-exhaustiveness fenced (proven, not asserted): `cci14 >= 0` vs `cci14 < 0` partitions every bar including exact zero, so the counters never stall and the latch always holds exactly one of `1`/`-1`/`0`. With `trend == 0` (pre-confirmation) neither signal leg can print — disclosed, not repaired into a neutral stance.
4. Dead-branch fence: the fade-hook entries (`useHookFade = false`), the slope filter (`useSlopeFilt = false`, `emaSlopeOk` identically true), the zero-line exits (`exitOnZero = false`), the date window (`useDate = false`), the single-entry modes, and every visual toggle are shipped-but-inert at pinned defaults — adopting any of them would be a different, unpinned rule. The `entryAtr` `var` persists across trades but is re-pinned on every signal bar before any bracket reads it — no stale-barrier path exists.
5. Fill-bar range fence: barriers go live from the fill bar's own high/low, so a gap-through-fill bar can stop a fresh position on its first bar under the TP-before-SL precedence — disclosed, not repaired. The bracket multiples are strictly positive, so barrier distance is always non-zero at the fill.
6. Cousin records fenced as different constructions (none conjoins a side-of-zero 5-bar CCI latch with a ZLR-hook-plus-Turbo-cross trigger pair, EMA34/LSMA25 filters, a |CCI|-200 ceiling, and a per-trade 2R ATR bracket): the admitted `cci-ema-rsi-cross-trailing-stop` sibling crosses CCI against EMA/RSI with a trailing stop (`1h`, no latch, no bracket); the admitted `cci-threshold-extreme-reversal` sibling fades ±100/±200 extremes two-sided (`4h`, no latch, no ATR risk); the admitted Forven `chaikin-mf`/`stochastic`/`kdj` siblings trade different oscillators; the admitted freqtrade `macd-cci-dip-state` and `macd-cross-cci-edge` siblings gate MACD constructions with a single CCI leg (`5m`, no latch, ROI/stop risk, long-flat). Moving any lookback, threshold, multiple, mode, filter, ceiling, or the frame would each be a different, unpinned rule — none is admitted here.
7. Sibling-script fence: any other script by any author (including other Woodies-CCI or Turbo-CCI scripts on TradingView) is a separate pin — their constants must never be substituted into this record, and this record's `1h`/BTCUSDT pins must never be read back as source facts.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the `1h` frame pin, the 150-bar warmup floor, the TP-before-SL-plus-flip precedence mapping, the fill-bar-live barrier rule, the liquidation tail rule, and house capital/leverage beneath source-native sizing and costs — all predeclared above. The Pine v6 construction, all 33 defaults, both trigger geometries, the filters, the ceiling, the 2.0x/3.0x bracket, the flip-close leg, the two-sided stance, and the 0.05%-plus-1-tick cost model are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CCI(14)/Turbo(6) pair / 5-bar latch / ZLR geometry / Turbo cross / EMA34-plus-LSMA25 filters / |CCI|-200 ceiling / 2.0x stop plus 3.0x target / flip-close / single-unit two-sided / `1h` BTCUSDT / next-bar-open fills with fixed precedence are frozen.

- F1 — Trigger-pair relevance: running ZLR-only and Turbo-only twins (same latch, filters, ceiling, bracket, flip-close) must not both weakly dominate the pinned `Both` book on net expectancy net of the adopted costs; fail ⇒ the trigger pair adds nothing over either single leg.
- F2 — Latch relevance: replacing the 5-bar latch with a bare side-of-zero state (trade any qualifying trigger while `cci14` sits on the trend side, no confirmation count, same everything else) must not improve net expectancy; fail ⇒ the confirmation count adds nothing over the raw zero side.
- F3 — Bracket relevance: removing the ATR bracket (flip-close exits only, same entries) must not improve net expectancy; fail ⇒ the 2R bracket adds nothing over the bare signal book.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market and no timeframe). Two-sided with full-unit open/reversal/close expresses on the perpetual venue with margin; a spot-only port would have to disable the short leg and is a different, unpinned rule. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume, funding, or external feed is read by any order-gating line. Funding is modeled only by the realized historical series while positioned (see Execution assumptions), never zeroed.

## Limitations

- The `1h` frame rides existing admission precedent on `main` — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A trend latch that flips every few bars exits winners at the flip-close and reverses immediately — whipsaw across consecutive bars with no cooldown to damp it is the principal friction, disclosed as the system's own coded behavior.
- The script is days old with no revision history: the pinned rule is exactly the 205-line block read on 2026-10-23. A later author edit, a deleted page, or a settings change is outside this pin — downstream must re-verify the URL content before any exact-head reliance.
- EMA34 convergence tail extends past the nominal indicator seeds; the 150-bar floor covers it with margin, but the tail shape is inherited from the standard EMA construction, not measured here.
- No trailing, no time exit, no breakeven, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://www.tradingview.com/script/uC1oajDr-Woodies-CCI-Trend-Strategy-Zero-Line-Reject-Turbo-Cross/
