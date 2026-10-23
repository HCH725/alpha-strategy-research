---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade FSample RSI-edge TEMA-BBmid reversal two-sided on BTCUSDT 1h bars
created: 2026-10-23
updated: 2026-10-23
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

# Freqtrade FSample RSI-edge TEMA-BBmid reversal two-sided on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, and `freqtrade-technical-cmf` records — this is only its twelfth record, the first pinned to this exact file, and the first pinned under the `futures/` directory).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/futures/FSampleStrategy.py`.
- GitHub blob SHA at the pinned commit: `cb55a9253473697fb7ccb71c8a8fe3454929cd92`, size 5413 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 5413 bytes, 162 lines, SHA-256 `3fcbe2ed16dd097fd6e4548172acbde871bdfe64c5a7341f337f19caf3daa225`, identical to the GitHub blob (`git hash-object` reproduces `cb55a925…92c9d92`) — the entire file was retrieved and inspected.
- Registration: the file defines class `FSampleStrategy(IStrategy)` (the only class in the file). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path, both unique. Repo-wide, the sibling files `futures/FAdxSmaStrategy.py` (two-sided ADX/SMA with a three-rung ROI ladder), `futures/FOttStrategy.py` and `futures/FSupertrendStrategy.py` (two-sided, trailing, four-rung ROI ladders), `futures/TrendFollowingStrategy.py` (two-sided, trailing, three-rung ROI), `futures/VolatilitySystem.py` (3h-resampled ATR merge plus `custom_stoploss`/`custom_stake_amount` callbacks), and every other admitted pin are different pins with different gates — this record pins ONLY the FSampleStrategy file's literals below, and no reviewer repair may substitute a sibling constant or a sibling indicator.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "1h"`; `minimal_roi = {"0": 1}` (single-rung +100% target); `stoploss = -0.05`; `can_short = True`; `trailing_stop = False`; `process_only_new_candles = True`; `startup_candle_count: int = 30`; indicators `dataframe["rsi"] = ta.RSI(dataframe)` (TA-Lib default period 14 — no override in the file, disclosed), `dataframe["tema"] = ta.TEMA(dataframe, timeperiod=9)` (explicit 9), `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` with `bb_middleband = bollinger["mid"]` (explicit 20/2 on typical price); long edge `(qtpylib.crossed_above(dataframe["rsi"], 30)) & (tema <= bb_middleband) & (tema > tema.shift(1)) & (volume > 0)` (`enter_long = 1`); short edge `(qtpylib.crossed_above(dataframe["rsi"], 70)) & (tema > bb_middleband) & (tema < tema.shift(1)) & (volume > 0)` (`enter_short = 1`); long exit repeats the short-edge conjunction verbatim (`exit_long = 1`); short exit repeats the long-edge conjunction verbatim (`exit_short = 1`). No `use_exit_signal` / `exit_profit_only` override, no `order_types` mapping, no `leverage` / `trading_mode`, no `position_adjustment`, no `cooldown`, no `max_open_trades`, no `time_limit` ships anywhere — the framework defaults and controller bindings below are disclosed as derived behaviour, never as file literals.
- Out-of-file call pinned (resolved by name, standard vendored library): `qtpylib.crossed_above` from `freqtrade.vendor.qtpylib.indicators`, whose base is `crossed(series1, series2, direction)`: for a scalar threshold, `above = (series1 > series2) & (series1.shift(1) <= series2.shift(1))` (verified against `freqtrade/freqtrade@2025.6`, `freqtrade/vendor/qtpylib/indicators.py`, `def crossed`/`def crossed_above` — fixed one-bar-back comparison, causal, disclosed, never redefined). So `crossed_above(rsi, 30)` is exactly `(rsi[t] > 30) & (rsi[t-1] <= 30)` — a one-bar edge, never a persistent state. No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter instantiation, no informative-pair call in the file.
- Full-file token census (verified over the 162 lines this cycle): 0 `IntParameter(` / 0 `DecimalParameter(` / 0 `CategoricalParameter(` / 0 `BooleanParameter(` (the four Parameter classes are imported and never instantiated — zero tuning scaffolding, every effective constant is a frozen literal); 1 `enter_long` / 1 `exit_long` / 1 `enter_short` / 1 `exit_short` (each set once via `.loc`, no zero-init — unset bars are NaN/false, disclosed); `can_short = True` is the only posture flag; 4 `shift` (the four `tema.shift(1)` slope guards — the only lag calls; fixed one-bar offset, no forward reference; the edge's own `shift(1)` lives inside the vendored `crossed`, disclosed above); 4 `volume` (the four `volume > 0` guards); 0 `resample` / 0 `informative` / 0 `merge_` / 0 `request` / 0 `security` / 0 `date` / 0 `.dt.` (single-frame, no calendar/session read); 1 `stoploss` attribute (`-0.05`) and 1 `minimal_roi` (the single-rung `{"0": 1}`) as the only risk legs; 0 shipped `custom_stoploss` / 0 `custom_exit` / 0 `custom_stake` / 0 `order_types` / 0 `leverage` / 0 `funding` / 0 `mark_price` (no economics beyond ROI/stop); 0 `position_adjust` / 0 `cooldown` / 0 `max_open_trades` / 0 `pyramid` (the position pin below is a predeclared researcher rule, never a file semantic). `np`/`pd` are imported and never referenced (`np.`/`pd.` zero hits) — dead imports, fenced as plumbing with no gate effect. Live columns are exactly `rsi`, `tema`, `bb_middleband`, `volume`; every other computed column (`adx`, `fastd`/`fastk`, `macd`/`macdsignal`/`macdhist`, `mfi`, `bb_lowerband`/`bb_upperband`/`bb_percent`/`bb_width`, `sar`, `htsine`/`htleadsine`) is computed and never read by any order line — dead columns, fenced in Negative evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `1h` frame, the RSI(14)-cross-30/70 one-bar edges, the TEMA9-vs-BBmid(20-typical) positional rails, the TEMA slope guards, the volume gate, the mirrored long/short edge pair, the single-rung +100% ROI target, the −5% stop, the disabled trailing, the two-sided posture, the 30-bar startup count, and per-completed-bar evaluation — but ships no venue spelling, no fill-timing flag, no sizing rule, no time-limit value, and no controller binding. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` perpetual (the file names no market; the `futures/` directory plus `can_short = True` selects a perpetual venue that can express the short leg — venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close MARKET fills and no publication lag (the file's own framework contract evaluates per completed bar — derivation disclosed, never presented as the source engine's own timing; the no-lag mapping matches the pinned engine's actual call order, see Execution assumptions); (3) directional-controller binding with scalar signal (+1/−1/0), at most one executor per side, same-pass opposite-side stops, controller-default 300s cooldown (provably non-binding on the `1h` grid), `time_limit = None` (the file ships no time exit — disclosed, never a file literal), and leverage 1 isolated; (4) the source's absent sizing/costs ride the explicit house overlay with no safety-order/add tranche activating under the single-unit/no-add pin (see Execution assumptions); (5) double-edge bars resolve LONG by record rule (disclosed tie-break, never a file semantic). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-23): working-tree filename/content search for `fsample` (case-insensitive) returns zero strategy records — no record in the pool cites this source file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an RSI-cross/TEMA-BBmid system. TEMA cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where short-horizon pressure flips up through 30 (RSI crossing above 30) while trend position is weak-or-mid (TEMA9 at or below the 20-bar typical-price midline) and still rising; sell/short the mirror bar where pressure flips up through 70 while TEMA9 sits above the midline and is falling. Exits are the exact mirror edges, so every entry signal on one side is simultaneously the exit signal for the other side — a symmetric reversal machine. A single-rung +100% ROI target and a fixed −5% stoploss backstop every position; trailing is explicitly off. The file header calls itself a sample (`This class is a sample. Feel free to customize it`) and ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Edge-triggered percentile reversal with a trend-position filter, two-sided. Unlike state systems (which hold while a condition prints), each leg fires only on the single bar where RSI crosses its threshold — a market that sits at RSI 50 prints nothing on either side. Unlike pure oscillator reversals, two permission keys gate every edge: TEMA9 must sit on the signal's own side of the Bollinger midline (weak-side for longs, strong-side for shorts) AND slope the confirming way (rising for longs, falling for shorts), so late-chasing edges against a turned trend print nothing. The failure mode is plain: the mirror construction means a positioned book reverses on the very next opposite edge — chop that alternates 30-crosses and 70-crosses whipsaws the book side-to-side with no cooldown; and a trend that never prints the opposite edge holds the unit until the −5% stop (the +100% rung is coded but economically inert on `1h` crypto bars — disclosed, never presented as a live profit-taking leg). There is deliberately no time exit, no breakeven, no partial — disclosed, not repaired.

## Signal

Exact rule as pinned (any other RSI period, TEMA length, band window, threshold, slope direction, risk rung, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; TA-Lib RSI default period 14 applies (no override in the file — disclosed default, never a file literal):

```text
rsi14[t]  = TA-Lib RSI(close, 14)
tema9[t]  = TA-Lib TEMA(close, 9)
bbmid[t]  = rolling-mean-20 of typical_price = (high+low+close)/3
edgeL[t]  = (rsi14[t] > 30) & (rsi14[t-1] <= 30) & (tema9[t] <= bbmid[t])
              & (tema9[t] > tema9[t-1]) & (volume[t] > 0)     // enter_long = 1, one-bar edge
edgeS[t]  = (rsi14[t] > 70) & (rsi14[t-1] <= 70) & (tema9[t] > bbmid[t])
              & (tema9[t] < tema9[t-1]) & (volume[t] > 0)   // enter_short = 1, one-bar edge
exitL[t]  = edgeS[t]    // exit_long repeats the short-edge conjunction verbatim
exitS[t]  = edgeL[t]    // exit_short repeats the long-edge conjunction verbatim
risk      = ROI {"0": 1} (fraction of entry-price distance, by position age in minutes);
          fixed stop at -5% (stoploss -0.05, same basis)
floor     = first 30 bars flat by source startup_candle_count (see Required data)
```

- Trade events: `edgeL` opens long (flat book) / exits short (positioned-short book); `edgeS` opens short (flat book) / exits long (positioned-long book). Each edge is a one-bar event, never a persistent state — a book already positioned on the edge's side treats further same-side prints as hold-no-ops under the position pin below (same-side re-entry is blocked while that side is active; no pyramiding, no averaging — no `position_adjustment` ships anywhere).
- Mirror proof (no ordering invented for the common case): `exitL ≡ edgeS` and `exitS ≡ edgeL` by code identity — every long-entry bar is simultaneously a short-exit bar and vice versa. Under the single-executor-per-side pin, a positioned book treats such a bar as close-then-open (reversal, engine-native same-pass semantics — see Execution assumptions), while a flat book treats it as a one-sided open. The reviewer is never asked to invent an entry/exit ordering.
- Double-edge pin (rare, resolved by record rule — disclosed, not repaired): `edgeL` needs `rsi14[t-1] <= 30` while `edgeS` needs `rsi14[t-1] <= 70`, so a bar leaping from RSI ≤ 30 to RSI > 70 in one `1h` print fires BOTH edges. Scalar-signal mapping resolves LONG-first on such bars (flat book opens long only; positioned-short book stops short and opens long; positioned-long book holds). No engine ordering is invented: the pin is a complete mapping from the four book-states, and double-edge bars are the only bars where it activates.
- Exact boundaries (pinned semantics): strict throughout (`>`, `<=`, `<`, never `>=` on the wrong side — RSI exactly on 30/70, TEMA exactly on the midline against the strict side, or a flat TEMA slope fires nothing on that conjunct). Volume gate is strict (`> 0`). All literals are never tuned here.
- Direction: two-sided by code (`can_short = True` ships in the file — never a researcher extension). Long-only or short-only readings would contradict the file. Both sides express on the perpetual venue (see Crypto portability for the spot boundary).
- Exits and risk (explicit): the mirror signal exits, the single-rung +100% ROI target, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). ROI rung and stop are fractions of entry-price distance (close-to-close price return for the rung; low/high extremes for the stop — see Execution assumptions for the engine-verbatim evaluation), leverage-invariant events, so downstream leverage/margin accounting cannot alter any exit event. No trailing (`trailing_stop = False` ships), no time exit (none ships — `time_limit = None` binding, disclosed), no breakeven move — explicitly none further, not invented. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): at most one open executor per side per market; same-side edges while that side is active are hold-no-ops; opposite-side edges reverse (close-then-open, same pass); re-entry after any TP/SL/signal close needs only the next qualifying edge (no cooldown specified in the file — explicitly none; the controller-default 300s cooldown is provably non-binding on the 3600s grid, see Execution assumptions). Pre-startup bars are flat by source rule.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` (typical-price midline, TEMA, RSI) plus bar `volume`, with fixed non-negative offsets (trailing windows, the two one-bar lags, the vendored edge's own one-bar-back comparison — no forward reference) under the file's own framework contract (`process_only_new_candles = True` ships — one evaluation per completed bar, disclosed as a file literal). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `close` (RSI14/TEMA9 construction), `high`/`low`/`close` (typical-price midline), `volume` (the four `> 0` guards). No `open` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (source-native — the file prints `timeframe = "1h"`; no `informative_pairs` method ships anywhere, so the file is single-frame by construction).
- Warmup (source-native, never a researcher pin): `startup_candle_count = 30` ships in the file — the first 30 completed `1h` bars are flat by source rule. Covers the RSI14 seed, the TEMA9 seed, the 20-bar midline seed, and the two one-bar edge lags with margin. Coded behaviour underneath: TA-Lib seeds print NaN until warmed and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; the `futures/` directory plus `can_short = True` selects a perpetual venue that can express the short leg, and no source-market equivalence is claimed). Leverage 1, isolated (researcher binding — the file ships no leverage; the ROI/stop percentages are leverage-invariant price-distance events, so the leverage pin cannot alter any exit event).
- Order timing (derived, disclosed — no publication lag): completed-bar decision with same-bar-close MARKET fills. This mapping is verbatim the pinned engine's call order (Hummingbot `HCH725/hummingbot@8b0e067`, package `20260920`, VERSION `dev-2.17.0`): per bar, `update_state` loads that bar's `close_bt` into the price provider and stamps time BEFORE any action (`backtesting_engine_base.py:364-368`); only then does `determine_executor_actions()` run (`:282-284`), and each created executor is simulated over the slice starting at the current row (`:287`, `processed_features.loc[i:max_ts]`), with MARKET open orders filled at that row's close (`position_executor_simulator.py:11-15`, entry price pinned at `:40`). The decision bar's own completed print is therefore legitimately available at decision time — no future price is read, and no lag state is needed or admitted. No maker-touch, queue, or intrabar-path-dependent fill.
- Barrier semantics (engine-verbatim, adopted — never defined away): the simulator evaluates TP on close-based net return from the entry row on (`:43-46`, `:58`) and SL on the rows' `low`/`high` against the entry-relative stop price from the entry row on (`:60-64`, entry row included); close order on ties is TAKE_PROFIT → STOP_LOSS → TRAILING_STOP (none here) → TIME_LIMIT (`:66-76`, TP checked first). This record adopts all three consequences verbatim: (a) a bar satisfying both the +100% rung and the −5% stop closes TAKE_PROFIT; (b) an entry bar whose own low/high already breaches the −5% distance closes STOP_LOSS on the entry bar — the pre-fill extreme is evaluated as coded, disclosed as the strategy's own semantic, never claimed away; (c) with `time_limit = None` the time-limit timestamp falls back to the data end (`:26`), so positions held past every signal/barrier leg terminate only at the backtest boundary — a boundary effect, disclosed.
- Signal-exit semantics (engine-native): same-pass opposite-side stops terminate still-active executors at the decision bar with `CloseType.EARLY_STOP`, booking the simulator's per-bar realized pnl (`backtesting_engine_base.py:568-599`); naturally barrier-closed executors are removed from the active set during `update_state` BEFORE the pass's actions (`:413-437`), so a bar co-printing a natural barrier close and a signal stop applies the natural close — no double-count, no invented ordering. Creates and stops share one deterministic pass (`directional_trading_controller_base.py:152-159`, creates proposed before stops; per-side active counts gate only same-side creation, `:185-195`), so a reversal bar closes the old side and opens the new side at the same bar close without any hedge accumulation. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride this specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` across many records — no novel-interval confirmation is required for this frame.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentages are preserved verbatim as the risk legs (leverage-invariant events) while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal — no safety-order/add tranche activates in this derived version, so position events are fully determined by the legs above and sizing changes no event, never presented as source-native behaviour.
- Concurrency: at most one executor per side per market at any time; the mirror edges open one side while stopping the other on reversal bars; same-side re-edges while active are hold-no-ops; re-entry after any close needs only the next qualifying edge. Single engine position per side; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (162 lines: the RSI/TEMA/BB-midline indicator block, the two mirrored edge conjunctions for entries and exits, the `timeframe`/`minimal_roi`/`stoploss`/`can_short`/`trailing_stop`/`process_only_new_candles`/`startup_candle_count` literals, and the `FSampleStrategy(IStrategy)` class pin). Its header declares itself a sample (`This class is a sample. Feel free to customize it`). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib seeds print NaN until warmed and every strict NaN comparison is false (no early edge, no early rail print). The 30-bar source startup count additionally holds every pre-seed bar flat — source-native, never misattributed.
2. No zero-init fence: the four order columns are `.loc`-set without zero-init — unset bars are NaN, deterministically non-firing. No second leg is hidden in the initialization style.
3. Dead-column fence: `adx`, `fastd`/`fastk`, `macd`/`macdsignal`/`macdhist`, `mfi`, `bb_lowerband`/`bb_upperband`/`bb_percent`/`bb_width`, `sar`, `htsine`/`htleadsine` are computed and never read by any order-gating line — disclosed, never promoted into guards. Their library-internal periods cannot alter any trade event.
4. Dead-import fence: `BooleanParameter`/`CategoricalParameter`/`DecimalParameter`/`IntParameter` are imported and instantiated zero times; `numpy`/`pandas` are imported and referenced zero times — plumbing with no gate effect, never a hidden tuning space.
5. Inert-rung fence: the +100% single-rung ROI target is coded and engine-mapped (`take_profit = 1.0`), but economically inert on `1h` crypto bars — disclosed as inert, never presented as a live profit-taking leg and never tightened by repair. The −5% stop is the only binding price leg besides the mirror signal exits.
6. Edge-vs-state fence: both legs are one-bar `crossed_above` edges (vendored definition quoted in Provenance), never persistent states — converting either leg to a level state (or vice versa) would be a different, unpinned rule with different trade events. A market sitting at RSI 50 prints nothing on either side, by code.
7. Cousin records fenced as different constructions (none trades RSI-cross edges gated by TEMA9-vs-BBmid position plus TEMA slope with full mirror reversal): the admitted `freqtrade-quickie` pool-mate trades a sub-mid rising-TEMA9-slope STATE (not an edge) with an ADX30 floor and SMA200 filter, long-flat, `5m` (a market that sits hot prints state entries there but nothing here; a 70-cross with falling TEMA prints here but nothing there); the admitted `freqtrade-multima` pool-mate trades a TEMA stack trend state, long-flat, `4h`; the admitted `forven-tema-cross` pool-mate trades a bare dual-TEMA edge-cross pair with no Bollinger rail, no slope leg, no RSI; the admitted `forven-rsi-s00139` pool-mate trades an SMA-gated RSI-threshold state pair with a moving-average exit (level construction, no midline rail, no slope, no reversal symmetry). Not a threshold re-tuning of any of them: moving either RSI threshold, converting either edge to a state, dropping the midline rail or either slope guard, or breaking the mirror would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `FAdxSmaStrategy.py`, `FOttStrategy.py`, `FSupertrendStrategy.py`, `TrendFollowingStrategy.py`, `VolatilitySystem.py`, `FReinforcedStrategy.py`, and every other file in the collection are separate pins — their ROI ladders, trailing flags, resample merges, custom callbacks, constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-perpetual market choice, the same-bar-close MARKET fills with no publication lag, the scalar-signal controller binding (LONG-first double-edge pin, one executor per side, same-pass opposite stops, non-binding 300s cooldown, `time_limit = None`, leverage 1 isolated), the framework-default readings (`use_exit_signal=True`, `exit_profit_only=False`, per-completed-bar evaluation), and house sizing/costs with safety tranches deactivated — all predeclared above. The `1h` frame, the RSI(14)-cross edges with all their literals and strictness, the TEMA9-vs-BBmid rails, the slope guards, the volume gate, the mirror exit pair, the single-rung ROI target with the −5% stop, the disabled trailing, the two-sided posture, and the 30-bar startup count are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14) / 30-70 cross edges with pinned strictness / TEMA9 / BBmid(20-typical) rails / slope guards / volume gate / mirror reversal / +100% inert rung / −5% stop / one-per-side two-sided book / `1h` BTCUSDT-perp / same-bar-close fills are frozen.

- F1 — Edge relevance: replacing both one-bar cross edges with their persistent level twins (rsi>30 / rsi>70 held states, same rails/guards/risk) must not improve net expectancy; fail ⇒ the coded edges add nothing over level exposure.
- F2 — Rail relevance: dropping the TEMA-vs-midline rails and slope guards (bare RSI 30/70 cross reversal, same risk) must not improve net expectancy; fail ⇒ the trend-position filter adds nothing over the naked oscillator reversal.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (mirror-signal exits only) must not improve net expectancy; fail ⇒ the +100% rung plus −5% stop adds nothing over the bare reversal machine.

## Crypto portability

BTCUSDT Binance perpetual `1h` is the research pin (source names no market; the `futures/` directory plus `can_short = True` requires a venue that can express the short leg). The long leg expresses unchanged on a spot venue with no naked shorting; the short leg has no spot expression — two-sided figures are perpetual-only, disclosed. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Bar volume is a native Binance kline field on both spot and perpetual venues. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `1h` frame rides existing admission precedent across many `main` records — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A trend that never prints the opposite edge holds the unit until the −5% stop (or the data-end boundary) — there is no decay, chop, trend-loss, or further time exit, disclosed, not repaired. Alternating 30/70-cross chop reverses the book side-to-side with no cooldown to damp it — disclosed as the principal friction.
- Double-edge bars (RSI leaping from ≤30 to >70 in one `1h` print) resolve LONG by record rule — rare, deterministic, disclosed, never smoothed.
- TA-Lib internals (RSI/TEMA seeding, NaN propagation, Hilbert internals behind the dead HT columns) live in libraries outside the pinned file — pinned by call with explicit/default periods, not re-derived; exact reproduction inherits those libraries' seeding alongside the 30-bar source floor.
- No trailing, no breakeven, no partial, no time exit, no short-side amputation — all explicitly absent or present as coded, never to be added or removed by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/FSampleStrategy.py
- https://github.com/freqtrade/freqtrade-strategies
