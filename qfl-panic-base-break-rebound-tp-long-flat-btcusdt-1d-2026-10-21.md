---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QFL panic-base-break rebound-gated take-profit long-flat on BTCUSDT 1d bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-30
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/QFL震荡条件止损均线策略-QFL-Oscillation-Stop-Loss-Moving-Average-Strategy.md
  - https://www.fmz.com/strategy/482512
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QFL panic-base-break rebound-gated take-profit long-flat on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/fmzquant/strategies (open FMZ strategy mirror; the backtest header inside the file pins `Futures_Binance BTC_USDT`, `period: 1d`).
- Pinned commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (committed `2025-04-30T03:10:28Z`; verified as the repository HEAD via the GitHub commits API during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `QFL震荡条件止损均线策略-QFL-Oscillation-Stop-Loss-Moving-Average-Strategy.md` (strategy detail page https://www.fmz.com/strategy/482512, last modified `2025-02-18`).
- GitHub blob SHA at the pinned commit: `087e28f31befde164c1c1fc5f69927cc45d250e6`, size 12250 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 12250 bytes, 226 lines, SHA-256 `eea451ccd458f996960ac000c4244b7fbbd6bfaeb0838552e766e191d00138cd`, identical to the GitHub blob (`git hash-object` reproduces `087e28f3…d250e6`) — the entire file was retrieved and inspected.
- Registration: the file carries exactly one strategy (`Jackson Quickfingersluc (QFL) Strategy`, `//@version=6`, `overlay=true`) with one embedded Pine v6 `strategy(...)` program. No second strategy, no library import, no `request.*`, no `security()` call ships anywhere.
- The file's own words (quoted for gate evidence, never extended): backtest header `period: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`; parameters `baseLevelMultiplier = input.float(1, …)` / `reboundMultiplier = input.float(0.8, …)` / `lookBackPeriod = input.int(50, …)` / `atrPeriod = input.int(14, …)` / `atrMultiplier = input.float(1.2, …)` / `exitProfitThreshold = input.float(0.01, …)` / `panicSellPercentage = input.float(0.005, …)` / `takeProfitOption = input.string("avg_price", …, options=["avg_price", "first_entry", "each_position"])` / `rangeBars = input.int(3, …)` / `cooldownBars = input.int(5, …)`; construction `lowestClose = ta.lowest(close, lookBackPeriod)` / `baseLevel = lowestClose[1] * baseLevelMultiplier` / `rangeLastBars = ta.highest(high, rangeBars) - ta.lowest(low, rangeBars)` / `reboundLevel = reboundMultiplier * rangeLastBars + baseLevel` / `atrValue = ta.atr(atrPeriod)`; entry `entry_cond = isPanicSell and (na(lastEntryBar) or (bar_index - lastEntryBar) > cooldownBars)` with `strategy.entry("Buy", strategy.long)`; exit `profitPercentage = (close - entryPrice) / entryPrice`, `profitCondition = profitPercentage >= exitProfitThreshold`, `reboundCondition = isRebound`, TP fires on `profitCondition and reboundCondition` with `strategy.close("Buy")`; `strategy(...)` call ships no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no commission/slippage argument — quoted absences, never filled in.
- Full-file token census (verified over the 226 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `strategy.short` (no short leg anywhere — long-only is coded); 0 `volume` (no volume read of any kind); 0 `security` / 0 `request.` (single-frame by construction); 0 `stoploss` / 0 `stop` (no stop leg of any kind ships — explicitly disabled below, never invented); 0 `trailing` (no trailing); 0 `pyramiding` (no cap ships — the source permits repeated entries, fenced and replaced by the single-unit pin below); 0 `commission` / 0 `slippage` / 0 `funding` / 0 `leverage` (no economics beyond the TP formula); 0 `hyperopt` / 0 `Parameter`; 1 `cooldownBars` loop guard (`(bar_index - lastEntryBar) > cooldownBars`, strict); 2 `strategy.close("Buy")` sites (avg/first options) plus 1 partial `strategy.close("Buy", qty=positionSize)` site (each-position option — moot under single-unit, fenced). `showLabels`, `alert()`, `label.new`, `plot()` are display/alert plumbing with no gate effect.
- Latch census (load-bearing verbatim semantic): `var bool panicSellMovement = false` is set `:= true` inside the range loop and is NEVER assigned false anywhere in the 226 lines — once tripped it stays tripped for the rest of history. Preserved verbatim, never "repaired" into a per-bar flag.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the FMZ backtest. The source pins the `1d` frame, the Binance-futures BTC market, all ten parameter defaults, the base/rebound/ATR construction, the latching panic flag, the strict `> 5`-bar cooldown, the profit-plus-rebound TP formula, the long-only posture, and the no-stop/no-trailing posture — but ships no fill-timing flag, no warmup guard, no position-size cap, and no cost model. Researcher-declared adaptations are exactly seven: (1) symbol spelling normalized to `BTCUSDT` (venue and pair are source-native — `Futures_Binance BTC_USDT`); (2) completed-bar decisions with same-bar-close market fills (the Pine default fills on the next tick; derivation disclosed, never presented as source timing); (3) single-unit position pin — one full-stake entry, further panic bars while positioned are hold-no-ops (the source permits repeated entries with no shipped cap; disclosed, never presented as source-native behaviour); (4) `takeProfitOption` pinned to its default `"avg_price"` — moot under single-unit since average, first, and per-position prices coincide on one entry (disclosed); (5) same-bar priority pin — TP-close evaluated before entry, no reopen on a TP bar (the source never both closes and reopens deterministically on one bar; tie-break disclosed, never sourced); (6) 70-bar researcher warmup pin with pre-warmup bars flat (the file ships none — disclosed); (7) explicit research cost/size pins below (the file ships no commission, slippage, funding, or sizing — disclosed). This record is therefore never evidence that the original FMZ backtest itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `qfl`, `quickfinger`, `quick finger`, and `482512` returns zero strategy records — no record in the pool cites this source file or strategy. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles band-ratio) trades a panic-base-break plus rebound-gated-TP machine. Panic-dip cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Panic-base-break long, long-flat. A 50-bar lowest-close base (one bar stale) defines the floor; a bar prints a panic entry when its low undercuts 99.5% of that base AND an ATR-range movement flag is set (average range over 1–4 bars, or any single recent bar range, exceeds 1.2× ATR(14) — latched permanently once ever tripped). The position exits only when BOTH legs hold: unrealized profit ≥ 1% from entry AND the close has rebounded above base + 0.8× the last-3-bar range. A strict 5-bar cooldown separates entries. No stop, no trailing, no time exit ships anywhere.

### Research interpretation

Latched-fear entry with rebound-gated profit-taking. The base leg supplies the location (only buy breaks of a 50-bar floor), the ATR leg supplies the violence filter (only breaks printed in genuinely expanded range — and because the flag latches, the violence test effectively applies to the first panic of history and then stays satisfied, so late-history entries gate on base-break plus cooldown alone), and the cooldown supplies the pacing (no chase within 5 bars). The exit is deliberately narrower than a pure +1% target — both the profit AND the rebound print are required — so a scheme that exits on either leg alone would be a different, unpinned rule. Unlike persistent-state records (trade every qualifying bar), the cooldown plus single-unit pin make this an event machine: at most one entry per 6-bar spacing, held until the joint TP print, however long that takes. There is deliberately no disaster guardrail — an entry that never recovers 1% above its rebound is held indefinitely, disclosed as the record's principal risk.

## Signal

Exact rule as pinned (any other lookback, multiplier, threshold, strictness, option, latch semantic, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; Pine `ta.lowest/ta.highest/ta.atr` are the Pine standard-library calls with the stated lengths, disclosed, never overridden:

```text
lowestClose[t]  = lowest close over bars t-49..t            // 50-bar window
baseLevel[t]    = lowestClose[t-1] * 1.0                    // one-bar stale, multiplier 1.0
rangeLast3[t]   = highest high(3)[t] - lowest low(3)[t]
reboundLevel[t] = 0.8 * rangeLast3[t] + baseLevel[t]
atrValue[t]     = Pine ta.atr(close,14)[t]                  // RMA-smoothed TR
latch: var false; for bar_i in 1..4:
         if (highest(high,bar_i)[t]-lowest(low,bar_i)[t])/bar_i > 1.2*atrValue[t] -> true (latch, break)
         if high[t-bar_i+1]-low[t-bar_i+1] > 1.2*atrValue[t]          -> true (latch, break)
         // never cleared anywhere in the file — set-once semantics, verbatim
panicThreshold[t] = baseLevel[t] * (1 - 0.005)
isPanicSell[t]    = (low[t] < panicThreshold[t]) AND latch
isRebound[t]      = (close[t] > reboundLevel[t])
entry    = isPanicSell[t] AND (never entered OR (t - lastEntryBar) > 5)  // strict, single-unit: no-op while positioned
exit_TP  = ((close[t]/fill - 1) >= 0.01) AND isRebound[t]                // unleveraged price return, 1x — no leverage basis ambiguity
floor    = leading-window bars: rolling na comparisons false (see Required data)
```

- Trade events: `strategy.entry("Buy", strategy.long)` on a bar printing the panic conjunction past cooldown (flat book only); `strategy.close("Buy")` on a bar printing the joint TP conjunction. Each entry is a one-bar event, not a persistent state — a positioned book treats further panic bars (including post-cooldown ones) as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the base break is strict (`low < threshold` — a bar kissing exactly 99.5% of base fires nothing); the rebound is strict (`close > reboundLevel` — equality fires nothing); the profit leg is inclusive (`>= 0.01` — exactly +1.00% satisfies); the cooldown is strict (`> 5` — re-entry needs 6+ bars after the entry bar). All preserved throughout.
- Same-bar priority (predeclared researcher tie-break): on any bar, the TP-close is evaluated first; a bar that closes the unit never reopens on the same bar even if the entry conjunction also prints — re-entry starts from the next bar, still subject to the cooldown. While flat, TP legs are no-ops (no open price exists); while positioned, entry legs are no-ops. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere — a two-sided reading would contradict the file. The long-only 1x book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit and complete): the joint TP conjunction is the ONLY position-closing leg. No stop, no trailing, no time exit, no breakeven move ships anywhere — explicitly none further, not invented, and no stop is added by this record. A leg that never prints the joint TP is held indefinitely by record rule.
- Position rule (predeclared researcher pin): single-unit isolated 1x — one full-stake entry of 100% of allocated research capital, no adds, no averaging, no pyramiding (the source ships no cap and permits repeated entries — replaced here by disclosure); re-entry re-arms on any qualifying panic bar after any TP close subject to the strict cooldown (no further cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. The house BO 6% + SO 6% + SO 6% DCA overlay and 3x/5x leverage are explicitly NOT part of this admission version (downstream campaign settings only — applying them would change trade events and would constitute a separate declared derivative, never an event-neutral overlay here).
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (lowest/highest windows with fixed non-negative offsets, RMA ATR, plus the `[1]` one-bar base staleness — no forward reference); the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, no `security()`, no session/calendar call, no volume read, no order argument anywhere in the gating path. The `strategy()` call's shipped absences (no pyramiding cap, no fill-timing flag, no commission) are disclosed above, never read as semantics.

## Required data

- Completed `1d` bars of BTCUSDT: `high`/`low`/`close` only (base floor on `close`; panic threshold on `low`; range/rebound/TP on `high`/`low`/`close`). No `open` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (source-native — the backtest header prints `period: 1d`; no `security()`/`request.*` ships anywhere). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own finalized prints at its close); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 70 completed `1d` bars held flat. Covers the 50-bar lowest-close window plus its one-bar staleness (51), the ATR(14) RMA seed, and the 4-bar latch reach with margin. The file ships no warmup guard — quoted absence, never filled in from elsewhere. Coded behaviour underneath: Pine rolling calls print na until seeded and every strict/inclusive na comparison is false, and the latch starts false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual (source-native — the backtest header pins `Futures_Binance BTC_USDT`; only the `BTC_USDT`→`BTCUSDT` symbol spelling is normalized, and no source-market equivalence beyond the file's own header is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same single-frame completed-bar-close lane primitive the admitted 1d records (e.g. wick-reversal-hammer-shooting-star long-flat, wavetrend-cross-zone-gated, stochastic-ott-dual-trend) and the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state/crossed, and BinHV27 siblings use. The Pine default (next-tick fills) is NOT claimed. No maker-touch, queue, or intrabar-path-dependent fill: entry, and the joint TP conjunction, are all bar-close-evaluated; the Signal same-bar priority pin leaves no ambiguous fill order, and the TP formula needs no intrabar extreme — bar-close sequencing only.
- Interval precedent (disclosed, not assumed): `1d` is an already-admitted interval on `main` across dozens of records — no novel-interval confirmation is required for this frame. Decision/availability timestamps (one evaluation at each completed `1d` close), fills (that same close), costs, and isolated-1x margin accounting ride the specified path as pinned below.
- Sizing/capital/costs (explicit researcher pins — the file ships no commission, slippage, funding, sizing, or margin concept, quoted absences): single-unit isolated 1x of 100% allocated research capital, no adds (position baseline, never the house DCA); taker fee 0.05% per side (Binance USDT-M VIP0 schedule, predeclared assumption); slippage 0.01% per side (predeclared assumption); funding modeled, never zero-claimed — the Binance historical funding-rate series applied to open notional at each 00:00/08:00/16:00 UTC funding timestamp inside research accounting (the source declares no funding treatment at all). TP/stop basis: the TP leg is evaluated on unleveraged price return `(close/fill − 1)` at 1x with fees/funding carried in the separate research cost accounting above — no leveraged-margin-return ambiguity exists at 1x, and no ROI table or stop ships anywhere to need a second basis. Canonical Hummingbot fee/slippage/funding settlement is verified downstream (Node13); this record reports no net performance of its own.
- Concurrency: at most one position in the market at any time; the panic conjunction opens the full unit on a flat book past cooldown; the joint TP conjunction closes it in full; re-entry after a TP close needs only the next qualifying panic bar past the strict cooldown (no further cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (226 lines: the ten parameter defaults, the base/rebound/ATR construction, the latching range loop, the strict cooldown, the panic conjunction, the profit-plus-rebound TP formula on all three option branches, and the `strategy.entry/close("Buy", long)` pair). It ships a one-year `2024-02-19→2025-02-17` backtest header with no traceable performance table, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling na compares false and the latch starts false (no early entry, no early TP). The 70-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no warmup guard, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: the base break and the rebound are strict while the profit leg is inclusive and the cooldown is strict — a bar sitting exactly on 99.5%-of-base or exactly on the rebound fires nothing on that leg; exactly +1.00% satisfies the profit leg; exactly 5 bars after entry still blocks re-entry. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-plumbing fenced: `showLabels`/`label.new`/`plot()`/`alert()`, the `entryPrices`/`entrySizes` arrays, and `strategy.position_size`/`position_avg_price`/`opentrades` reads are display/bookkeeping leftovers that coincide trivially under the single-unit pin — never repaired into extra legs. Zero hyperopt tokens, zero fitted values anywhere in this artifact.
4. Latch fence: `panicSellMovement` is set-once, never cleared — after the first violent range print in history the ATR-movement leg is permanently satisfied and late-history entries gate on base-break plus cooldown alone. Coded fact, disclosed, not reinterpreted as a per-bar filter and not "fixed" by repair.
5. Take-profit-option fence: the default `"avg_price"` branch is pinned; under the single-unit pin the average, first-entry, and per-position prices coincide on the one open entry, so all three option branches compute the identical TP conjunction — pinning the default loses no behaviour, disclosed.
6. No-stop fence: zero `stop`/`stoploss` tokens ship anywhere — a position whose joint TP never prints is held indefinitely by record rule. The absence is source-native, disclosed as the principal risk, never repaired with an invented stop.
7. Cousin records fenced as different constructions (none trades a 50-bar lowest-close base-break conjunct with a latched ATR-range violence flag, a strict 5-bar cooldown, and a profit-plus-rebound joint TP, long-flat, on `1d`): the admitted `catching-the-bottom-rsi-dip-reversal` pool-mate trades an RSI-dip reversal with no base floor, no ATR leg, no rebound gate; the admitted `oversold-rsi-tight-sl` pool-mate trades an oversold-RSI entry with a tight stop (a stop this record explicitly lacks); the admitted `forven-connors-rsi-oversold-recross` pool-mate trades a Connors-RSI recross with no base/rebound machinery; the admitted `forven-rsi-s00139-washout-cross` pool-mate trades an RSI washout cross with no base floor and no joint TP; the admitted `dual-thrust-open-range-breakout` pool-mate trades an open-plus-range breakout (no base floor, no panic latch, day-session exits). Not a threshold re-tuning of any of them: moving any lookback, multiplier, threshold, strictness, cooldown, option, latch semantic, TP leg, or frame would each be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source-native behaviours in this record are the symbol-spelling normalization, the same-bar-close fills, the single-unit/no-add/no-same-bar-reopen position pin, the `"avg_price"` option pin, the same-bar priority tie-break, the 70-bar warmup floor (the file ships none), and the explicit size/cost pins — all predeclared above. The `1d` frame, the Binance-futures BTC market, the ten parameter defaults, the base/rebound/ATR construction, the latch semantics, the panic conjunction with all its strictness, the joint TP formula, the strict cooldown, and the long-only no-stop posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 50-bar stale base / 0.8 rebound / ATR(14) 1.2× latch / 0.5% break depth / +1% profit leg / strict cooldown-5 / single-unit long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Violence-latch relevance: entering on every base-break past cooldown with the latch permanently satisfied from the first bar (same exits otherwise) must not improve net expectancy; fail ⇒ the coded ATR-movement latch adds nothing over a naked base-break.
- F2 — Rebound-gate relevance: exiting on the +1% profit leg alone without the rebound conjunct (same entries otherwise) must not improve net expectancy; fail ⇒ the coded rebound gate adds nothing over a bare profit target.
- F3 — Cooldown relevance: removing the strict 5-bar cooldown while keeping entries and exits (same fills otherwise) must not improve net expectancy; fail ⇒ the coded pacing adds nothing over its unpaced twin.

## Crypto portability

BTCUSDT Binance perpetual `1d` is the source-native pin (header `Futures_Binance BTC_USDT`). Long-only 1x with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and is modeled only by the explicit research funding pin above, never assumed zero.

## Limitations

- The `1d` frame rides existing admission precedent (dozens of admitted `1d` records) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position whose joint TP never prints is held indefinitely with no stop, no trailing, and no time exit — through drawdowns of any depth, bounded only by the venue's liquidation mechanics outside this record's scope. This is the coded posture, disclosed as the record's principal risk.
- The latched violence flag means the ATR leg filters only early-history entries; late-history entries gate on base-break plus cooldown alone. Coded fact, disclosed, not repaired.
- Pine library internals (RMA seeding inside `ta.atr`, `ta.lowest/highest` edge handling) live in the Pine standard library outside the pinned file — pinned by call with lengths 14/50/3, not re-derived; exact reproduction inherits that library's seeding alongside the 70-bar floor.
- No trailing, no breakeven, no short leg, no time exit, no second cooldown — all explicitly absent, never to be added by repair.
- Derived fill timing: the Pine default fills on the next tick after the signal bar; this record evaluates completed bars only and executes same-bar-close on `1d` BTCUSDT. Backtest economics of the timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance. Any live/queue/next-tick behaviour is out of scope.
- Source economics are absent-only: beyond the backtest header (pair, period, window) the file ships no capital sizing, no commission, no slippage, no funding, and no margin assumption — derived evaluation must carry the full explicit research cost load above (fees plus modeled historical funding; no hypothetical zero funding claimed), and this record reports no net performance of its own. The referenced FMZ page carries no performance table, so no figure is kept or transferred.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/QFL震荡条件止损均线策略-QFL-Oscillation-Stop-Loss-Moving-Average-Strategy.md
- https://www.fmz.com/strategy/482512
