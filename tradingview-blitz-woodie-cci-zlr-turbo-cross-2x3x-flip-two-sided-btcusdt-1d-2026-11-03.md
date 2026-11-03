---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView blitz Woodie CCI ZLR-turbo cross 2x3x flip two-sided on BTCUSDT 1d
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-21
sources:
  - https://www.tradingview.com/script/uC1oajDr-Woodies-CCI-Trend-Strategy-Zero-Line-Reject-Turbo-Cross/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView blitz Woodie CCI ZLR-turbo cross 2x3x flip two-sided on BTCUSDT 1d

## Provenance

Primary source identity verified end to end (page opened live and Pine read line by line this cycle, 2026-11-03):

- TradingView strategy `Woodies CCI Trend Strategy | Zero-Line Reject & Turbo Cross` (page title carries a leading horse emoji and the `by blitz_algo` byline) by publisher `blitz_algo`, stable URL `https://www.tradingview.com/script/uC1oajDr-Woodies-CCI-Trend-Strategy-Zero-Line-Reject-Turbo-Cross/` (script ID part `uC1oajDr`). Page markers confirm `OPEN-SOURCE SCRIPT` with `blitz_algo` authorship and an Oct-21 publication badge (page `created_at` reads `2026-10-20T21:43:10+00:00`, i.e. Oct 21 Asia/Taipei — record `source_as_of` is that stamp, never a fetch date).
- Full Pine source read verbatim this cycle through the page's `Source code` tab (Pine v6 `//@version=6`, 205 lines per the page's own Pine-Editor count, MPL-2.0 header stamped `© blitz_locked` — page byline vs code stamp recorded exactly as found, never reconciled by inference). Pinned declaration: `strategy("Woodies CCI Strategy", shorttitle = "Woodies CCI Strat", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 20, commission_type = strategy.commission.percent, commission_value = 0.05, slippage = 1, initial_capital = 10000, pyramiding = 0, calc_on_every_tick = false)` — no `process_orders_on_close` anywhere. Order census over the captured text this cycle: 2 `strategy.entry` (ids `Long`/`Short`, `strategy.long`/`strategy.short`), 2 `strategy.exit` (ids `XL`/`XS`, stop+limit from the fill price), 2 `strategy.close` (ids `Long`/`Short`, exit-on-flip/zero legs), 0 `strategy.order`, 0 `strategy.close_all`, 0 `request.*`, 0 `security(`. Entries therefore fill next-bar-open market by Pine default; the bracket legs arm from the fill price; the flip/zero legs close at the next open.
- Pinned inputs (frozen defaults): CCI source `hlc3`, CCI length `14` (7–50), Turbo CCI length `6` (3–14), Bars Before Trend `4` (1–20); Entry Mode `Both` (ZLR Hook / Turbo Cross / Both); ZLR pullback lookback `5` (2–15), pullback level `50.0`, max counter excursion `100.0`, max |CCI| at entry `200.0`; counter-trend extreme hook `false`, extreme level `200.0`; price-vs-EMA filter `true`, EMA length `34`; LSMA-direction filter `true`, LSMA length `25`; EMA-slope filter `false`, min slope `0.05` ATR/bar; ATR length `14`, stop `2.0x`, target `3.0x` (0 = off); exit-on-flip `true`, exit-on-zero-cross `false`; allow longs `true`, allow shorts `true`; date-window gate `false` (window 2020-01-01 → 2030-01-01 inactive under the pin). Visuals group (three color modes, gradient fill/bars, stop/target lines, LSMA line, entry labels) is display only.
- Licence and rights: this record cites and normalizes the rule (short phrases and definitional recurrence only) and reproduces no extended prose, figures, or performance numbers. The page's `Strategy report` tab was never opened; no author backtest number is adopted anywhere in this record.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the source's CCI-zero-side trend latch with ZLR-hook / Turbo-cross pullback entries ported to BTCUSDT 1d with fixed sizing, next-open entries, and post-hoc bracket-plus-flip resolution — not a lossless reproduction of the author's chart-tester setup. Researcher-declared adaptations are exactly eight: (1) single-asset BTCUSDT Binance USDT-M perpetual 1d venue (the source ships no venue pin); (2) fixed 0.01 BTC 1x isolated sizing replacing the author's 20%-of-equity compounding (tester economics, never ported); (3) the inactive tester date window stays dropped (identical to default behavior — `useDate = false` — disclosed, never re-denominated); (4) exits resolved post-hoc: the fill-anchored 2x/3x ATR box by first-touch against completed-bar high/low with the pinned stop-first same-bar rule, plus trend-flip closes at the next open with bracket priority on touch bars — the declared conversion of the author's intrabar stop/limit fills into the admitted latched-bracket-plus-flip resolution class (entries stay source-native next-bar-open market — no conversion there); same-bar long+short dual-fire resolves long-then-short to a net short book at the same next open (source code order — pinned); reversals resolve as flat-close plus fresh entry at the same next open (two fills, fees on both); (5) display drop (all plots/fills/bar-colors/labels/level lines) and dead-option pins (fade OFF, slope filter OFF, zero-cross exit OFF — all source defaults, never deleted from the source); (6) live-option pins (Entry Mode `Both`, EMA filter ON, LSMA filter ON, exit-on-flip ON, longs+shorts ON — all source defaults; the TP-off branch and the single-mode branches are dead code under the pin — disclosed); (7) structural 100-completed-bar warmup (the source ships none — first fully defined signal needs bars 0..33; the margin absorbs SMA/RMA seeding); (8) explicit research cost overlay: 0.05% taker fee per filled side plus modeled funding from realized settlements while open; slippage unmodeled by declaration (the source's 1-tick TV slippage does not port). The CCI 14 / Turbo 6 arithmetic, the 5-bar trend latch, the 5-bar pullback window, the 50/100 ZLR bands, the hook predicates, the crossover convention, the EMA34/LSMA25 filters, the 200 |CCI| cap, the 2x/3x latch arithmetic, the fill-price anchor, pyramiding 0, and the two-sided reversal book are source-faithful. This record is therefore never evidence that the author's script passes.

Pre-write dedup (2026-11-03): working-tree base is current `main@f53f5a6e` (536 root strategy records, READMEs excluded; the README pool-count line still reads 486 — count lag outside this PR's touch boundary, never edited here). Case-insensitive content searches for `uC1oajDr`, `Woodie`, `zero-line reject`, `zero line reject`, `turbo CCI`, `bars before trend`, and `ZLR hook` return zero same-source/same-construction hits. The sole `blitz_algo` pool hit (`tradingview-blitzalgo-displaced-donchian-decycler60-mfi14-atr2-3-bracket`, same publisher shop, code stamp `blitz_locked`) is a displaced-Donchian/decycler/MFI machine on 1h — no CCI leg, no trend latch, no hook/cross entries. The `blitz_locked` mention in the heatsweep volume-profile record is a different script and mechanism. CCI pool records (threshold-cross, EMA-RSI-cross, freqtrade CCI stacks, washout, MACD-pivot) carry no zero-side latch, no pullback-band hook, and no Turbo-cross leg. All 17 open `research/*` PRs enumerated by number/title/branch (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725) — none is this script, publisher construction, or signal. Five-axis distinction: no pool record and no open PR conditions exposure on a CCI(hlc3,14) zero-side 5-bar trend latch with ZLR-hook (5-bar pullback to the 50 band, contained within 100) OR Turbo-CCI(6) cross entries, EMA34-price plus LSMA25-direction filtered, |CCI| < 200 capped, exited by a fill-anchored 2x/3x ATR bracket with trend-flip closes, single-unit two-sided reversal book.

## Economic mechanism

### Source-reported

Zero-side trend regime with pullback timing: CCI(14) must hold one side of zero for the confirmation span to declare the trend, then entries buy the pullback (ZLR hook back toward zero that turns with the trend) or the fast Turbo CCI(6) crossing the slow CCI in the trend direction, while EMA/LSMA filters veto sideways tapes and the |CCI| cap vetoes chasing. The 2x-stop/3x-target box and the flip exit then manage the leg without re-reading the oscillator. (Author's framing; never adopted as a crypto claim.)

### Research interpretation

Latched-regime pullback capture, two-sided, daily cadence. Unlike oscillator-cross records there is no cross-and-go: the cross/hook is necessary but never sufficient — the 5-bar zero-side latch kills unconfirmed wiggles, the pullback band (touch 50, contained in 100) kills both non-pullback chases and trend-breaks, and the EMA34/LSMA25 pair kills counter-trend prints, so the signal set is the intersection of four independent conditions. Unlike bracket-only records the box is fill-anchored (levels derive from the fill price and the signal-bar ATR, never re-armed), and unlike pure-bracket records a trend flip can end the trade at the next open even mid-box. Unlike reversal records entries never fade the latch — both triggers fire with the trend; the short book is the mirror image, not a fade. The bet, as derived, is purely that this latch-plus-pullback intersection with a fixed-ratio box ports arithmetically to BTCUSDT daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries next-bar-open market; bracket post-hoc first-touch; flip closes next-open; two-sided single-unit reversal book — any other window, grid, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — CCI pair (source formula, pinned): `CCI(n)[i] = (hlc3[i] − SMA(hlc3,n)[i]) / (0.015 · mean(|hlc3 − SMA|)[i])` with `n = 14` (`cci14`) and `n = 6` (`turbo`). First fully defined at bar indices 13 and 5. (Zero-deviation stretches print 0.0 — explicit holds, not missing rules.)
- R3 — ATR (source variant, pinned): Wilder-RMA ATR(14) over the true range, SMA-seeded. First fully defined at bar index 13.
- R4 — Filters (source formulas, pinned): `ema34 = EMA(close, 34)` (SMA-seeded; first defined at index 33); `lsma = linreg(close, 25, 0)` (OLS fitted value at the current bar over the trailing 25 closes; first defined at index 24). Slope-filter leg pinned OFF (adaptation 5 — `emaSlopeOk` identically true).
- R5 — Trend latch (source state machine, pinned): `barsAbove`/`barsBelow` count consecutive bars with `cci14 >= 0` / `cci14 < 0` (na resets — explicit; equality latches above, pinned); `trend := 1` once `barsAbove >= 5`, `:= −1` once `barsBelow >= 5` (Bars Before Trend 4 + confirming bar); the latch persists until the opposite side confirms. First confirmation at index 17. Flips `trendFlipUp`/`trendFlipDown` compare against `trend[1]` (na-startup never fires — explicit).
- R6 — ZLR hook (source predicate, pinned): `lowRecent = lowest(cci14,5)[1]`, `highRecent = highest(cci14,5)[1]`; `hookUp = cci14 > cci14[1] AND cci14[1] <= cci14[2]` (prior-bar equality arms, current-bar equality never fires — pinned); `zlrLong = trend==1 AND lowRecent <= 50 AND lowRecent >= −100 AND hookUp AND cci14 > lowRecent`; mirrored short (`highRecent >= −50 AND highRecent <= 100 AND hookDown AND cci14 < highRecent`). A pullback that never touches 50, or that prints past 100 on the wrong side, never fires — explicit holds.
- R7 — Turbo cross (source predicate, pinned): `turboLong = trend==1 AND cci14 > 0 AND crossover(turbo, cci14)` under the builtin convention (prior-bar equality fires, current-bar equality never fires — pinned); `turboShort` mirrored with `cci14 < 0` and crossunder. Equality on the zero-side leg holds (never fires).
- R8 — Signal conjunction (source arithmetic, pinned): `trendLongSig = (zlrLong OR turboLong) AND close > ema34 AND lsma > lsma[1] AND cci14 < 200`; mirrored short (`close < ema34`, `lsma < lsma[1]`, `cci14 > −200`). Strict inequalities throughout — equality on any leg holds, never fires. Counter-trend fade legs pinned OFF (adaptation 5 — dead code under the pin).
- R9 — Entry timing (source-native): signal-bar-close decision; fills at the next bar's open market (Pine default under no `process_orders_on_close` — no conversion). Guards `position_size <= 0` / `>= 0` with `pyramiding = 0` pinned: flat-or-opposite books fill; same-side adds are explicit no-ops (the latch ATR is not re-armed — pinned). Opposite fills reverse: flat-close plus fresh entry at the same next open, fees on both fills (pinned). Same-bar dual-fire (both signals while flat) fills Long first then reverses to Short at the same next open — net short book (source code order — pinned researcher conversion of broker sequencing).
- R10 — Bracket latch (pinned arithmetic, source-faithful): signal bar `s` latches `entryAtr = ATR14[s]`; levels derive from the fill price `F` (next open): long `SL = F − 2·entryAtr`, `TP = F + 3·entryAtr` (mirrored short; TP-off branch dead under the pin — disclosed). Levels never trail after arming.
- R11 — Bracket resolution (declared post-hoc conversion, adaptation 4): the armed pair is eligible from the entry bar (`s+1`) onward. Each held bar resolves first-touch against the bar's `H/L` with the stop-first same-bar rule (both touched → the SL price wins — explicit researcher pin in the admitted bracket class). Fills print at touch prices before fees.
- R12 — Flip exits (source-faithful timing, post-hoc lane): `longExit = trendFlipDown` (exit-on-flip pinned ON; zero-cross leg pinned OFF — adaptation 5) closes the full book at the next bar's open. Bracket has priority on touch bars: an intrabar stop/target touch closes first and the pending flip-close becomes a flat no-op (pinned broker-faithful order). After any exit the next qualifying bar may re-enter on schedule with freshly latched levels (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R13 — Risk legs (pinned absences, not invented): no trailing, no time exit, no opposite-gate exit beyond the flip, no cooldown — explicitly none, matching the shipped code (zero `strategy.order`, zero recycle logic).
- R14 — Position state: one 0.01-BTC unit max, either side, never both; the single `strategy.close` leg per side always closes the whole side book (full flat, no partials). Safety orders: explicitly none.
- R15 — Warmup and gaps: flat until 100 completed `1d` bars (structural need is bars 0..33 — the EMA34 leg dominates CCI 13 / Turbo 5 / ATR 13 / LSMA 24 / latch 17; the 67-bar margin absorbs SMA/RMA seeding per the admitted precedent chain). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat.
- R16 — Invariant identifier: `TV:blitz-uC1oajDr|CCI14hlc3_TURBO6_latch5_ZLR5x50w100_XO_EMA34_LSMA25_cap200_ATR2x3x_flip|independent-derived-v1|BinanceFutures:BTC-USDT:1d|TWO-SIDED|nextopen-MARKET+bracket-posthoc-stopfirst+flipnextopen|fee0.0005|lev1x|size0.01|warmup100|2026-11-03` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT only: `open` (entry/flip fills), `high`/`low` (true range, bracket touches), `close` (EMA/LSMA/hook/cross predicates), `hlc3` (both CCI legs). No volume (no volume read anywhere in the shipped code), no funding/OI/mark-index read gates on any order, no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; entries land at the next bar's open; bracket touches resolve post-hoc against completed-bar extremes; flip closes land at the next open. No provisional intrabar value is ever used.
- Warmup: flat until 100 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing statistic; boundaries are constants). The `[1]`/`[2]` pullback offsets read past-confirmed values — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual, 1x isolated, fixed 0.01 BTC per unit, single-unit book, no compounding. Both sides explicitly enabled (the source ships both legs under default toggles). 1x posture: no liquidation path exists inside a −100% move short of total loss; no margin-call/forced-close event can pre-empt the bracket or the flip (disclosed). Fills are never conditional on equity, funding, or buying power.
- Order timing (entries source-native, exits declared post-hoc): signal-bar-close decision; entries fill at the next bar's open market (Pine default under no `process_orders_on_close` — no conversion); the latched 2x/3x fill-anchored box resolves first-touch post-hoc with the stop-first pin — the same resolution class admitted records in `main` use for ATR brackets; flip closes fill at the next open with bracket priority on touch bars. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈767.9 USDT at the cycle's last completed close 76,791.30 — above the cycle-verified Binance USDT-M BTCUSDT `MIN_NOTIONAL 50`, `LOT_SIZE minQty/stepSize 0.001/0.001`, `MARKET_LOT_SIZE minQty 0.001`, `PRICE_FILTER tickSize 0.10`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.05% taker fee per filled side; modeled funding = sum of realized BTCUSDT-perp settlements (00:00/08:00/16:00 UTC, realized period rate on full notional, sign as settled) while a position is open — a defined, reproducible research model, never hypothetical zero funding and never realized/canonical funding; slippage unmodeled by declaration (the source's 1-tick TV slippage does not port). Any run missing settlement inputs is void, never zero-filled.
- Concurrency: one single-unit two-sided reversal book (`pyramiding = 0` pinned — source-faithful); re-entry after any exit is explicitly allowed on the next qualifying bar with fresh levels; no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.
- Pinned-engine path (re-verified against local checkout `2dbc844` this cycle, `VERSION=2.17.0`; pinned source `8b0e067e80ab62f10846d518dcb5a8218527ddb3` verified an ancestor of this checkout via `merge-base --is-ancestor`): `data_feed/candles_feed/binance_perpetual_candles/constants.py` maps `1d → 86400`; `strategy_v2/backtesting/backtesting_engine_base.py` iterates completed rows and calls `controller.determine_executor_actions()` (`strategy/strategy_v2_base.py`-family `controller_base.py:465`, verified this cycle) feeding completed-row windows into `simulate_executor`; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:22-30` fills MARKET at the first window row's `close`. Hence a completed-bar-`s` decision fills at the next row's open in the next-open lane — the coded timing. The CCI/latch/hook/cross/filter arithmetic, the `entryAtr` latch, the guard/reversal branches, and the flat/add/close branches are deterministic controller logic over completed klines; no external feed is required. A strategy-specific, not-yet-implemented `DirectionalTradingControllerBase` child must compute exactly R2–R14; the generic executor does not calculate the strategy. Admitted bracket-plus-flip lane precedent in `main` (same-shop displaced-Donchian decycler/MFI record plus the KST/dual-EMA9-21/FMZ-445467/FMZ-434428/MACD-zero-cross-SMA50 bracket records) shows latched-box post-hoc resolution with the stop-first pin and next-open flip closes on this engine class; sibling PASS records are path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The script page and header ship every adopted headline fact quoted in Provenance: the CCI-14/Turbo-6/latch/pullback/filter construction, the MPL-2.0 licence, the 20%-equity sizing, the 0.05% commission, the 1-tick slippage, next-bar-open fills, pyramiding 0, the inactive 2020→2030 window, and all fourteen indicator lengths/thresholds. It ships zero adopted performance numbers for this record: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from the page, header, or reference engine is adopted anywhere — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the Pine-faithful signal/latch/bracket/flip pipeline (CCI pair, SMA-seeded RMA ATR14, SMA-seeded EMA34, OLS linreg-25, 5-bar latch, strict hook/cross predicates, pullback bands, filter conjunction, 200 cap, guards, reversal/dual-fire sequencing, `entryAtr` latch, stop-first post-hoc resolution, flip-close deferral, 100-bar warmup), run in scratch (never committed):

- Synthetic drift tape (seeded, 700 bars): first-defined indices CCI14 13 / Turbo 5 / ATR 13 / EMA34 33 / LSMA25 24 / trend 17 — matching the structural analysis exactly; 33 post-warmup opens driving 10 SL / 15 TP / 7 FLIP, ending SHORT (digest `d4f338ffbc76`); two independent runs identical.
- Live microstructure (Binance futures 1d klines fetched live this cycle, 999 completed bars, verified contiguous at 86400s steps, last close 76,791.30): 47 post-warmup opens (22 long / 25 short) driving 11 SL / 13 TP / 22 FLIP (0 reversals, 0 dual-fires), ending SHORT (digest `9fc2b1c5c44f`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 767.9 USDT notional at window close.
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Fill-conversion fenced: derived bracket exits resolve post-hoc against completed-bar extremes while the author's tester fills stops/limits intrabar — touch-bar timing and touch-vs-gap economics differ on some exits by construction. Flip closes resolve at the next open while the author's tester closes through the same next-open lane (no conversion there). This is the coded trade, disclosed, not a tunable parameter here.
2. Dual-fire rarity fenced: no long+short same-bar dual-fire printed in either probe window (0 duals); the long-then-short net-short pin is an explicit source-order conversion for an unobserved branch — flagged, never silently interchangeable with a no-op.
3. Sizing-removal fenced: the source's 20%-of-equity compounding is replaced by fixed 0.01 BTC — multi-trade equity paths diverge from the author's tester by construction. No equity curve is claimed here for exactly this reason.
4. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from the script page, header, or reference engine is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
5. Derivation boundary fenced: the only non-author behavior is the eight declared adaptations (venue, fixed sizing, window drop, post-hoc bracket/flip resolution with sequencing pins, display/dead-option pins, live-option pins, 100-bar warmup, cost overlay); the CCI arithmetic, the 5-bar latch, the pullback bands, the hook/cross predicates, the filters, the 200 cap, the 2x/3x fill-anchored latch, pyramiding 0, and the two-sided reversal book are source-faithful. This record is therefore never evidence that the author's script passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CCI `hlc3 14` / Turbo `6` / latch `5` / pullback `5 × 50 / 100` / `EMA34` / `LSMA25` / cap `200` / `2x/3x` ATR14 / strict predicates / Both mode / two-sided reversal / next-open entries / post-hoc stop-first bracket + flip closes / fixed 0.01 BTC 1x / BTCUSDT `1d` / 100-bar warmup are frozen.

- F1 — ZLR relevance: a turbo-only twin (ZLR legs removed, same latch/filters/bracket/flip) must not improve net expectancy; fail ⇒ the pullback-band hook adds nothing over latch-plus-cross.
- F2 — Turbo relevance: a ZLR-only twin (cross legs removed, same rest) must not improve net expectancy; fail ⇒ the Turbo cross is decoration on the hook.
- F3 — Filter relevance: a filter-blind twin (EMA34/LSMA25 legs removed, same rest) must not improve net expectancy; fail ⇒ the Woodie trend filters are fee-burning decoration.
- F4 — Bracket relevance: a width twin (1x stop / 2x target, same entries/flip) must not improve net expectancy by more than the pinned box's declared tolerance; fail ⇒ the author's 2x/3x ratio destroys more expectancy than its source authority justifies.
- F5 — Flip relevance: a flip-blind twin (flip closes removed, bracket-only exits, same rest) must not improve net expectancy; fail ⇒ the trend-flip exit buys nothing but whipsaw.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual (decision grid completed `1d` bar closes; entries at next opens; bracket touches resolved post-hoc; flip closes at next opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, windows, levels, coefficients, grids, or unit counts would be a different, unpinned claim.

## Limitations

- Single-asset port: the author's evidence is chart-tester context on the author's own symbols; BTCUSDT 1d latch-plus-pullback behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Conversion lag: post-hoc bracket resolution deviates from the author's intrabar stop/limit fills on some exits — the derived event set is its own object, never the author's tester output.
- Seeding: Pine SMA/RMA seeding transients are absorbed by the 100-bar warmup; an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Predicate equality: every strict/weak boundary (latch `>= 0`, hook `<=`, cross builtins, filter `>`/`<`, cap `<`) is pinned exactly as coded; an implementation flipping any boundary prints a different event set — flagged, never silently interchangeable.
- Stale-level holds: post-close retained `entryAtr` numbers are inert while flat; zero-deviation CCI stretches print 0.0 by construction — fenced, never traded around.
- Unobserved branch: the dual-fire net-short pin never printed in either probe window — carried as an explicit conversion, not as verified behavior.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- TradingView OPEN-SOURCE STRATEGY by blitz_algo, code stamp `© blitz_locked` (script ID `uC1oajDr`), page opened and Pine read live 2026-11-03: https://www.tradingview.com/script/uC1oajDr-Woodies-CCI-Trend-Strategy-Zero-Line-Reject-Turbo-Cross/
- Exchange verification (fetched live 2026-11-03): Binance futures `fapi/v1/exchangeInfo` (BTCUSDT `PERPETUAL`, `tickSize 0.10`, `LOT_SIZE minQty/stepSize 0.001/0.001`, `MARKET_LOT_SIZE minQty 0.001`, `MIN_NOTIONAL 50`) plus `fapi/v1/klines` 1d microstructure probes (999 completed contiguous bars, last close 76,791.30; 47 opens → 11 SL / 13 TP / 22 FLIP, plant digest `d4f338ffbc76`, live digest `9fc2b1c5c44f`)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (verified ancestor of local checkout `2dbc844`, `VERSION=2.17.0`, this cycle)
- Same-lane siblings (resolution-class evidence only, different mechanisms): same-shop displaced-Donchian decycler/MFI record plus KST / dual-EMA9-21 / FMZ-445467 / FMZ-434428 / MACD-zero-cross-SMA50 ATR-bracket records on `main`
- Pine reference: `ta.cci` / `ta.ema` / `ta.rma` (`ta.atr`) / `ta.linreg` / `ta.lowest` / `ta.highest` / `ta.crossover` / `ta.crossunder` causal semantics (v6); code-governs over prose throughout
