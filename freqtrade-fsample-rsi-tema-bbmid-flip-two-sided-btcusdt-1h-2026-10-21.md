---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade FSample RSI-cross TEMA-rail symmetric flip two-sided on BTCUSDT 1h bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade FSample RSI-cross TEMA-rail symmetric flip two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, and `freqtrade-macd-cross-cci-edge` records — this is only its eleventh record, and the first pinned to the `futures/` directory).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/futures/FSampleStrategy.py`.
- GitHub blob SHA at the pinned commit: `cb55a9253473697fb7ccb71c8a8fe3454929cd92`, size 5413 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 5413 bytes, 162 lines, SHA-256 `3fcbe2ed16dd097fd6e4548172acbde871bdfe64c5a7341f337f19caf3daa225`, identical to the GitHub blob (`git hash-object` reproduces `cb55a925…4929cd92`) — the entire file was retrieved and inspected.
- Registration: the file defines class `FSampleStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `futures/FAdxSmaStrategy.py`, `futures/FOttStrategy.py`, `futures/FReinforcedStrategy.py`, `futures/FSupertrendStrategy.py`, `futures/TrendFollowingStrategy.py`, `futures/VolatilitySystem.py`, and every `berlinguyinca/*.py` file are different pins with different gates — this record pins ONLY the FSampleStrategy literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): header comment `This class is a sample. Feel free to customize it.` (sample status disclosed — lineage only; every rule below is pinned from the shipped code, never from an imagined customization); `timeframe = "1h"`; `minimal_roi = {"0": 1}`; `stoploss = -0.05`; `can_short = True`; `trailing_stop = False` (the two `trailing_stop_positive*` lines ship commented — quoted absence); `process_only_new_candles = True`; `startup_candle_count: int = 30`; `informative_pairs` returns `[]` (empty — quoted, never a second frame); long entry `crossed_above(rsi, 30) & (tema <= bb_middleband) & (tema > tema.shift(1)) & (volume > 0)` (`enter_long = 1`); short entry `crossed_above(rsi, 70) & (tema > bb_middleband) & (tema < tema.shift(1)) & (volume > 0)` (`enter_short = 1`); long exit repeats the short-entry conjunction verbatim (`exit_long = 1`); short exit repeats the long-entry conjunction verbatim (`exit_short = 1`). No `order_types` / `order_time_in_force` / `position_adjustment` / `pyramiding` / `cooldown` / `max_open_trades` / `funding` / `mark_price` / `leverage` ships anywhere — the framework defaults below are disclosed as defaults, never as file literals.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.RSI(dataframe)` (TA-Lib RSI on close, default timeperiod 14 — no override in the file); `ta.TEMA(dataframe, timeperiod=9)` (explicit 9); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` (explicit window/stds on typical price — only `mid` is read by any order line, fenced below); `qtpylib.crossed_above(series, scalar)` (standard one-bar edge: `(s[t] > k) & (s[t-1] <= k)` — causal two-bar comparison, disclosed, never redefined); `ta.ADX`, `ta.STOCHF`, `ta.MACD`, `ta.MFI`, `ta.SAR`, `ta.HT_SINE` (all computed into the frame and read by no order line — dead columns, fenced below). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` are imported and never called — zero `(` constructions, zero `.value` reads), no informative-pair call beyond the empty list.
- Full-file token census (verified over the 162 lines this cycle): 1 `can_short` (the `= True` attribute — the only direction switch); 4 `crossed_above` (exactly the two entries plus the two mirrored exits, no other edge call); 0 `crossed_below`; 4 `shift` (exactly the four TEMA-slope legs — the only lag calls; fixed one-bar offset, no forward reference); 8 `volume` (the four `volume > 0` guards plus their four comment echoes — the only volume reads); 0 `resample` / 0 `interpolate` / 0 `informative` beyond the empty stub / 0 `request` / 0 `security`; 2 `stoploss` (one comment line plus the `-0.05` attribute) and 3 `minimal_roi` (two commented ladders plus the live `{"0": 1}`) as the only risk legs; 3 `trailing_stop` (one live `= False` plus two commented lines — explicitly disabled, not invented); 1 `startup_candle_count` (the source-native 30-bar floor); 0 shipped `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `hyperopt` / 0 `.value`; 1 `htleadsine` + 1 `htsine` (dead Hilbert pair, fenced below). `numpy`/`pandas` are imported and never called — dead imports, fenced as plumbing with no gate effect.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the RSI-30/70 cross triggers, the TEMA9-vs-BBmid rail plus one-bar slope legs, the `volume > 0` guards, the symmetric flip exits, the +100% take-profit leg, the −5% stop, the disabled trailing, the `can_short = True` two-sided stance, the 30-bar floor, and per-completed-bar evaluation — but ships no venue spelling, no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close fills (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing); (3) per-side single-unit pin with exit-before-entry flip sequencing plus the source-native 30-bar floor adopted verbatim (the file carries no position reference — disclosed, never presented as source-native behaviour); (4) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `fsamplestrategy` and `futures/FSampleStrategy` returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles KCD-ratio) trades an RSI-threshold-cross-plus-TEMA-rail symmetric flip. RSI/TEMA cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the single bar where RSI crosses up through 30 while TEMA9 sits on/below its Bollinger midline and rises bar-over-bar with non-zero volume (oversold-throw turn confirmed against the mean rail); short the mirror bar where RSI crosses up through 70 while TEMA9 sits above its midline and falls with non-zero volume. Each side exits on the opposite side's entry print. A +100% take-profit leg (`{"0": 1}`) and a fixed −5% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Oversold/overbought-throw turn catcher with a mean rail, two-sided and symmetric. The RSI-cross leg supplies the trigger (an oscillator throw crossing a fixed tripwire on this exact bar) while the TEMA-rail-plus-slope legs veto throws printed on the wrong side of the mean or without a turn — so an RSI-30 cross fired with TEMA9 already stretched above its midline prints nothing, and a below-rail rising TEMA9 without a fresh RSI cross prints nothing either. Unlike persistent-state records (trade every bar the condition holds), each trigger is a one-bar cross edge — a book already positioned on that side treats further same-side bars as hold-no-ops until the opposite print, the take-profit leg, or the stop. Unlike long-only records, the exit of each side IS the entry of the other: a short-side trigger bar closes a held long and opens a short on the same close (declared flip sequencing below) — the system is always eligible, never stranded in a one-way book. The coded consequence is a buyer of below-mean oversold turns and a seller of above-mean overbought turns that surrenders each side only when the opposite throw prints.

## Signal

Exact rule as pinned (any other RSI period, TEMA period, threshold, strictness, edge-vs-state pairing, risk rung, fill, frame, or book is a different, unpinned rule). All identifiers below are the program's own; the RSI period is the TA-Lib library default (14) and TEMA/BB literals are file-explicit:

```text
rsi[t]    = TA-Lib RSI(close, 14)            // default — no file override
tema[t]   = TA-Lib TEMA(close, 9)            // explicit 9
bbmid[t]  = SMA20(typical(high,low,close), 2 stds)[mid]  // explicit 20/2
xab(s,k)[t] = (s[t] > k) AND (s[t-1] <= k)   // standard crossed_above with scalar
long_trig  = xab(rsi,30)[t] AND (tema[t] <= bbmid[t]) AND (tema[t] > tema[t-1]) AND (vol[t] > 0)
short_trig = xab(rsi,70)[t] AND (tema[t] >  bbmid[t]) AND (tema[t] < tema[t-1]) AND (vol[t] > 0)
enter_long = long_trig;  enter_short = short_trig
exit_long  = short_trig; exit_short  = long_trig   // symmetric flip, verbatim
risk       = take-profit +100% (minimal_roi {"0": 1}, fraction, any age);
             fixed stop at -5% (stoploss -0.05, each side)
floor      = startup_candle_count 30 (source-native) + rolling-NaN falseness (see Required data)
```

- Trade events: `enter_long=1` / `enter_short=1` on bars printing their respective one-bar trigger; `exit_long=1` is the identical print as `enter_short=1` and `exit_short=1` the identical print as `enter_long=1`. A flat book treats exit/risk legs as no-ops; a positioned side treats further same-side triggers as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): the cross edges are strict on the decision bar (`rsi > 30` / `rsi > 70`) with inclusive previous-bar equality (`prev rsi <= 30` / `prev rsi <= 70` inside the standard edge); the rail legs are inclusive below (`tema <= bbmid`) and strict above (`tema > bbmid`) — a bar with `tema == bbmid` fires the long rail, never the short rail; the slope legs are strict (a flat TEMA bar fires neither side); the volume guards are strict (`vol > 0` — a zero-volume bar fires nothing). All preserved throughout.
- Mutual-exclusion proof, same side (no tie-break pin required): any long-trigger bar has `tema[t] <= bbmid[t]` with a rising slope while any long-exit bar (= short trigger) has `tema[t] > bbmid[t]` with a falling slope — rail and slope are both mutually exclusive on every bar, so same-side entry and signal-exit never co-print. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent a same-side ordering.
- Flip sequencing (predeclared researcher rule, never a file semantic): a bar printing `short_trig` while a long is held closes the long AND opens a short at the same decision-bar close (exit evaluated before entry — declared order); the mirror holds for `long_trig` against a held short. At most one net book change per side per bar. No intrabar touch or queue semantics are claimed.
- Direction: two-sided. `can_short = True` ships in the file (disclosed file literal, never a default reading) — a long-only reading would contradict the file. Both books express on a perpetual venue; spot expression of the short book is out of scope (see Crypto portability).
- Exits and risk (explicit): the mirrored signal exits, the +100% take-profit leg, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). The +100% leg binds only on run-ups of 100% or more from entry — coded magnitude, disclosed, never softened into a live profit-taking claim and never tightened by repair. No trailing (`trailing_stop = False` ships), no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit per side, at most one open long and one open short per market; the two sides are managed independently with no shared state (no pyramiding, no averaging — no `position_adjustment` ships anywhere); re-entry re-arms on any qualifying trigger bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close`/`volume` (RSI/TEMA/BB trailing windows plus the standard one-bar edge lookback plus the one-bar slope lag — no forward reference) with no `shift` call beyond the four TEMA-slope legs; the decision bar's own forming values are never read. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` for the RSI/TEMA/BB paths plus `typical = (high+low+close)/3` for the Bollinger path, and `volume` for the four `volume > 0` guards only. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (`informative_pairs` returns `[]` — quoted).
- Single decision timeframe `1h` (source-native — the file prints `timeframe = "1h"`). One evaluation per completed bar (`process_only_new_candles = True` ships); every window reads the decision bar's causal past only (plus the one-bar edge/slope lookbacks); fills land on the decision bar's own close under the derived rule below.
- Warmup (source-native, adopted verbatim): `startup_candle_count = 30` ships in the file — covers the 20-bar Bollinger seed, the 14-bar RSI seed, and the 9-bar TEMA seed with margin. Coded behaviour underneath: rolling windows print NaN until seeded and every strict/inclusive NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, and BinHV27 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entries, the mirrored signal exits, and the take-profit/stop legs are all bar-close-evaluated; the same-side mutual-exclusion proof leaves no ambiguous same-side fill order, the declared flip order (exit before entry) covers every cross-side co-print, and any bar co-printing a signal exit with a risk leg closes the full side flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` across many records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its +100% take-profit leg and −5% stop are preserved verbatim as price-distance risk legs (leverage applies only in downstream equity sizing, never in trigger levels) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the per-side single-unit/no-add position pin from Signal. Safety Orders are disabled under this pin (no averaging-down events — the overlay contributes only base-size conventions and cost assumptions, never additional entry events), never presented as source-native behaviour.
- Concurrency: at most one unit long and one unit short per market at any time, managed independently; a trigger opens its full side on a flat-or-opposite book (flip when opposite is held); the mirrored signal exit, the take-profit leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying trigger bar (no cooldown specified — explicitly none, not invented). No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (162 lines: the default-period RSI and explicit TEMA9/BB20-2 calls, the four `crossed_above`/rail/slope/volume conjunctions with mirrored exits, the `timeframe`/`minimal_roi`/`stoploss`/`can_short`/`trailing_stop`/`startup_candle_count`/`process_only_new_candles` literals, the empty informative stub, and the `FSampleStrategy(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling NaNs compare false (no early entry, no early exit). The source-native 30-bar floor additionally holds every pre-seed bar flat — adopted verbatim, never misattributed.
2. Exact-touch rule fenced: the cross edges are strict on the decision bar while admitting previous-bar equality; the long rail is inclusive (`<=`) while the short rail is strict (`>`); slopes and volume guards are strict — a bar sitting exactly on the midline satisfies the long rail only; a flat-TEMA or zero-volume bar fires nothing on either side. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-import plumbing fenced: `numpy`, `pandas`, `BooleanParameter`, `CategoricalParameter`, `DecimalParameter`, `IntParameter` are imported and never called anywhere in the 162 lines — zero `(` constructions, zero `.value` reads, zero fitted values. Display/plumbing leftovers with no gate effect, never repaired into a signal.
4. Dead-indicator fence: `adx`, `fastd`/`fastk`, `macd`/`macdsignal`/`macdhist`, `mfi`, `sar`, `htsine`/`htleadsine`, `bb_lowerband`/`bb_upperband`/`bb_percent`/`bb_width` are computed into the frame and read by no order line — the Hilbert pair in particular plays no gating role despite the `ta.HT_SINE` call, never repaired into a leg. Only `rsi`, `tema`, `bb_middleband`, and `volume` gate orders.
5. Commented-ladder fence: the two commented `minimal_roi` ladders and the two commented `trailing_stop_positive*` lines are file comments, never live legs — the live risk pair is exactly `{"0": 1}` plus `stoploss = -0.05` with trailing explicitly `False`. Comments never widen or narrow the coded legs.
6. Far-target fence: the +100% take-profit leg binds only on doublings — by construction the stop and the mirrored signal exits do nearly all the closing in ordinary tape. Coded magnitude, disclosed, not reinterpreted as an active profit-taking regime and not tightened by repair.
7. Cousin records fenced as different constructions (none trades an RSI-threshold-cross edge conjunct with a TEMA-vs-BBmid rail plus slope and volume guard, symmetric two-sided flip, with this risk pair): the admitted `freqtrade-quickie` pool-mate trades a long-only `5m` persistent TEMA-slope/BBmid state gated by ADX30/70 and an SMA200 under-close filter (no RSI trigger, no cross edge, no short book, different risk); the admitted `freqtrade-strategy001` pool-mate trades Heikin-Ashi EMA-cross edges with color legs (no oscillator tripwire, no Bollinger rail, long-flat); the admitted `freqtrade-cofibit` pool-mate trades a fast-stoch rail system (different trigger family, `5m` long-flat); the pool's `forven-tema-cross` record trades a naked dual-TEMA edge-cross pair (no rail, no slope leg, no RSI); the pool's `ehlers-sinewave-phase-cross` record trades Hilbert phase crossings (the live leg there is phase geometry — here the Hilbert columns are dead); the pool's `tema-dema-hma-cross` record trades a triple-MA cross stack (no threshold trigger, no rail). Not a threshold re-tuning of any of them: moving the RSI period, either tripwire, the TEMA period, the BB window, flipping any strictness, dropping the slope or volume legs, breaking the exit mirror, or changing any risk rung, the frame, or the book would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `FAdxSmaStrategy.py`, `FOttStrategy.py`, `FReinforcedStrategy.py`, `FSupertrendStrategy.py`, `TrendFollowingStrategy.py`, `VolatilitySystem.py`, and every `berlinguyinca/*.py` file are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills, the per-side single-unit/no-add pin with declared flip sequencing, and house sizing/costs — all predeclared above. The `1h` frame, the RSI-30/70 cross triggers with all their literals and strictness, the TEMA9-vs-BBmid rail plus slope legs, the volume guards, the mirrored exits, the +100% take-profit leg with the −5% stop, the disabled trailing, the `can_short = True` stance, the 30-bar floor, and per-completed-bar evaluation are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14) / TEMA(9) / BB(20,2) mid / `30`+`70` tripwires with pinned strictness / one-bar-edge triggers / rail-plus-slope conjunctions / `volume > 0` guards / mirrored flip exits / +100% take-profit / −5% stop / per-side single-unit two-sided / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — RSI-trigger relevance: replacing both cross triggers with persistent rail states (long while `tema <= bbmid` and rising, short while `tema > bbmid` and falling, same risk) must not improve net expectancy; fail ⇒ the oscillator tripwire adds nothing over the rail alone.
- F2 — Rail-and-slope relevance: dropping the TEMA rail and slope legs (naked RSI-30/70 cross triggers, same mirrored exits, same risk) must not improve net expectancy; fail ⇒ the mean-rail turn filter adds nothing over the bare throws.
- F3 — Risk-pair relevance: removing the take-profit/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the +100% leg plus −5% backstop adds nothing over the bare flip machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market). The long book expresses unchanged on a spot venue with no naked shorting; the short book requires a venue with short permission (perpetual declared here) and is out of scope for spot. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Volume is consumed only as a `> 0` guard, satisfiable by any venue printing trade volume. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent across many `main` records — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A side whose opposite throw never prints is held until the take-profit leg or the −5% stop, however long that takes — there is no decay, chop, trend-loss, or further time exit; in a one-way grind the held side accrues while the opposite book stays flat (flip profile, disclosed). No trailing, no breakeven, no cooldown — all explicitly absent, never to be added by repair.
- TA-Lib indicator internals (EMA seeding, RSI Wilder smoothing, TEMA triple-EMA arithmetic, typical-price Bollinger bands) and the standard `crossed_above` one-bar edge live in libraries outside the pinned file — pinned by call with RSI default 14, TEMA 9, BB 20/2, never re-derived; exact reproduction inherits those libraries' seeding alongside the 30-bar floor.
- The `numpy`/`pandas`/hyperopt-parameter imports and all dead indicator columns are inert — nothing further to fence.
- The file's `This class is a sample` header is an explicit non-guarantee — this record makes no claim about the file's fitness, maintenance, or authorship beyond the pinned literals.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
