---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade HLHB EMA-RSI-ADX quad-gated trend-state long-flat on BTCUSDT 4h bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/hlhb.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade HLHB EMA-RSI-ADX quad-gated trend-state long-flat on BTCUSDT 4h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official first-party Freqtrade strategy collection — a different repository from the `berlinguyinca/freqtrade-strategies` lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-strategy002`, `freqtrade-strategy004`, and `freqtrade-strategy001` records; no record in the pool pins any file from this official repository).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/hlhb.py`.
- GitHub blob SHA at the pinned commit: `5164cda889e37759d86252f02e7d9a3bfc648fb1`, size 3821 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3821 bytes, 128 lines, SHA-256 `bd4523d134b686b012947896ffd7a5a299add87ac12aa0d18fac36c9e7ca3822`, identical to the GitHub blob (`git hash-object` reproduces `5164cda8…c648fb1`) — the entire file was retrieved and inspected.
- Registration: the file defines class `hlhb(IStrategy)` (the only class in the file). Its docstring lineage reads `The HLHB ("Huck loves her bucks!") System simply aims to catch short-term forex trends` with a pointer to the public Babypips HLHB explainer — lineage only, no sample, window, trade count, or cost basis ships anywhere in the 128 lines, and no performance statistics are printed (unlike the hyperopt-comment siblings in the same directory).
- The file's own words (quoted for gate evidence, never extended): `timeframe = '4h'`; `startup_candle_count: int = 30`; `minimal_roi = { "0": 0.6225, "703": 0.2187, "2849": 0.0363, "5520": 0 }`; `stoploss = -0.3211`; `trailing_stop = True`, `trailing_stop_positive = 0.0117`, `trailing_stop_positive_offset = 0.0186`, `trailing_only_offset_is_reached = True`; `use_exit_signal = True`, `exit_profit_only = False`, `ignore_roi_if_entry_signal = True`; `process_only_new_candles = True`; `order_types = { 'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False }`; entry is the four-way AND of `qtpylib.crossed_above(dataframe['rsi'], 50)`, `qtpylib.crossed_above(dataframe['ema5'], dataframe['ema10'])`, `dataframe['adx'] > 25`, `dataframe['volume'] > 0`; exit is the four-way AND of the `crossed_below` mirrors with the same `adx > 25` and `volume > 0` legs; `informative_pairs` returns `[]`.
- Framework calls pinned (all resolved against contemporaneous first-party commits, strategy pin ± framework pin): `crossed_above`/`crossed_below` re-export chain `freqtrade@3d31927` (`freqtrade/vendor/qtpylib/indicators.py`, a documented re-export shim) → `technical@9c6d8fd366ef0ed3e046b32e534bcec9f9479449` (`technical/vendor/qtpylib/indicators.py`): `crossed_above(s1,s2) = (s1[t] > s2[t]) & (s1[t-1] <= s2[t-1])`, `crossed_below(s1,s2) = (s1[t] < s2[t]) & (s1[t-1] >= s2[t-1])`, with `int`/`float` scalars broadcast to a constant series — so the literal `50` is a pinned constant leg, never a series lookup. `ta.RSI(dataframe, timeperiod=10, price='hl2')` / `ta.EMA(dataframe, timeperiod=5|10)` / `ta.ADX(dataframe)` are TA-Lib abstract calls (close-input default for EMA, 14-bar default for ADX) over the file's own `hl2 = (close+open)/2` column. `can_short` is unset in the file and defaults `False` on `IStrategy` (`interface.py` line 89 at the pinned framework commit — long-only by framework default, never a researcher invention); `position_adjustment_enable` defaults `False` (line 118); `ignore_roi_if_entry_signal` is a real framework control whose backtest semantic is pinned at `interface.py` line 1462 (`roi_reached = not (enter and ignore_roi_if_entry_signal) and min_roi_reached(...)` — ROI skipped on entry-signal bars, quoted verbatim).
- Full-file token census (verified over the 128 lines this cycle): 0 short legs (the single `short` token is the docstring word `short-term`); 2 `crossed_above` + 2 `crossed_below` (exactly the entry/exit edges, no other edge call); 2 `volume` (exactly the two `volume > 0` guards plus their comments — no other volume read); 1 `informative` (the `informative_pairs` stub returning `[]` — single-frame by construction); 0 `resample` / 0 `merge_informative_pair`; 0 `Parameter` (no hyperopt search space anywhere — every constant is a plain literal, unlike the `DecimalParameter`/`IntParameter`/`CategoricalParameter` siblings in the same directory); 1 `position_stacking` (the stray string `position_stacking = "True"` — no such control exists anywhere in the pinned `interface.py`, so it is engine-invisible; fenced, never repaired); 4 `trailing` (the four trailing literals, the only trailing in the file); 0 `heikinashi`; 0 `request` / 0 `security` / 0 session-calendar calls. `numpy as np` / `pandas as pd` are imported and never called (display leftovers — fenced, not repaired); `plot_config` is display-only.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source backtest. Researcher-declared adaptations are exactly six, all predeclared here: (1) market pin `BTCUSDT` on Binance (the source is pair-agnostic — no symbol, no venue, no `trading_mode` anywhere in the file); (2) same-bar-close market fills on completed-bar decisions (the source trades `limit` GTC entries/exits filled on later candles; this record freezes completed-bar evaluation with same-bar-close execution and scopes live/limit-order-book behavior out — the same derivation the admitted TD-Sequential record carries for its own `limit`-GTC source); (3) an adopted 40-bar warmup with pre-warmup bars flat by record rule (covers the source `startup_candle_count = 30` plus ADX-seeding and edge-lag margin; see Required data); (4) house sizing/capital/costs replacing the absent source economics; (5) bar-close evaluation of the fixed stop, the trailing stop, and the ROI ladder with the explicit precedence below (the source evaluates risk intrabar; intrabar sequencing is scoped out, never invented); (6) the source-native `ignore_roi_if_entry_signal = True` flag preserved with its pinned framework semantic (ROI rung skipped on bars printing `enter_long`) under the same-bar-close precedence — preserved, never redefined. The `4h` frame, the `hl2`/RSI10/EMA5/EMA10/ADX14 constructions, all four entry conjuncts, all four exit conjuncts, the four-rung ROI ladder, the −32.11% stop, the trailing triple (1.17% / 1.86% / only-offset), the long-only posture, and the exit-even-at-loss setting are source-native and unmodified.

Pre-write dedup (2026-10-21): working-tree content search for `hlhb`, `huckabee`, and `babypips` returns zero strategy records (the single `huck` hit is `Chuck LeBeau` inside the unrelated Chandelier record; the `universal` hits are `universal-calendar` prose); content search for the exact conjunction (RSI-50-cross × EMA5/10-cross × ADX-25 × volume-guard) returns zero records — the pool's nearest cousins are fenced as different constructions in Negative evidence 7. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross) trades an RSI-cross × EMA-cross × ADX-gated signal; #331 is the closest (ADX-gated MA-cross) but crosses SMA3/6 on `1h` with no RSI leg, no volume guard, and no trailing — a different mechanism, window set, frame, and risk stack. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where short-term momentum reignites (RSI(10) crossing up through 50) exactly as trend structure confirms (EMA5 crossing above EMA10) while trend strength certifies (ADX above 25) and the tape is alive (volume above zero) — and stand aside to flat on the mirror (both crosses pointing down with ADX still above 25 and volume alive), with a four-rung time-decaying ROI ladder (62.25% → 21.87% → 3.63% → 0%), a −32.11% fixed stop, and a trigger-gated trailing stop (arms at +1.86%, trails 1.17% under the peak) behind every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 128 lines.

### Research interpretation

Edge-synchronized momentum-trend-state machine, long-only. Unlike bare MA-cross records (fire on any cross, blind to momentum and strength), both cross edges must co-print on the same bar with ADX certification — a golden cross printing while RSI sits below 50, or while ADX languishes under 25, buys nothing. Unlike pure RSI-50 records (trade every midline cross), nothing fires without the EMA5/10 structural edge on the same bar — an RSI reclaim inside a still-bearish stack holds flat. Unlike level-state records, both trigger legs are one-bar edges: a qualifying bar whose ADX or volume leg fails is gone forever, never re-fires. The exit is the strict mirror with teeth: it demands both crosses pointing down with ADX still elevated — a merely weak tape without the double-cross holds the book until ROI, trailing, or the stop. The coded consequence is a buyer of edge-fresh, strength-certified trend impulses that surrenders only on a doubly-confirmed reversal or the risk stack. The trailing leg (first of its kind in the pool) does the economic work the ROI ladder cannot: with the first ROI rung at +62.25%, almost all profit-taking in any realistic tape runs through the +1.86%-armed 1.17% trailer.

## Signal

Exact rule as pinned (any other lookback, price input, threshold, edge/level choice, ROI rung, stop, trailer, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; framework primitives expand to their pinned contemporaneous definitions:

```text
hl2[t]    = (close[t]+open[t])/2
rsi[t]    = TA-Lib RSI(hl2, 10)
ema5[t]   = TA-Lib EMA(close, 5)
ema10[t]  = TA-Lib EMA(close, 10)
adx[t]    = TA-Lib ADX(high, low, close, 14)
xab(a,b)[t] = (a[t] > b[t]) AND (a[t-1] <= b[t-1])   // pinned crossed_above, scalar broadcast
xbe(a,b)[t] = (a[t] < b[t]) AND (a[t-1] >= b[t-1])   // pinned crossed_below, scalar broadcast
entry = xab(rsi,50)[t] AND xab(ema5,ema10)[t] AND (adx[t] > 25) AND (volume[t] > 0)    // enter_long = 1
exit_sig = xbe(rsi,50)[t] AND xbe(ema5,ema10)[t] AND (adx[t] > 25) AND (volume[t] > 0) // exit_long = 1
risk = time-decaying take-profit minimal_roi {"0": 0.6225, "703": 0.2187, "2849": 0.0363, "5520": 0}; fixed stop at -32.11% (stoploss -0.3211); trigger-gated trailing (positive 0.0117, offset 0.0186, only-offset-reached)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on bars printing the four-conjunct entry, `direction` long-only; `exit_long=1` on bars printing the four-conjunct exit. Both trigger legs are EDGE-gated (each cross fires only on its cross bar — a cross bar whose ADX/volume legs fail never re-fires; no one-shot latch, no level hold anywhere in code).
- Exact boundaries (pinned semantics): strict `>`/`<` on current bars with `<=`/`>=` admitted on the prior bar per the pinned `crossed` expansion — an RSI landing exactly on 50, or EMA5 landing exactly on EMA10, on the current bar fires nothing, while touching from the armed side on the prior bar still arms the edge; `adx` exactly `25` and `volume` exactly `0` both fail their strict legs. The `10` / `5` / `10` / `14` lookbacks, the `50` midline, the `25` strength line, the four ROI rungs, the stop literal, and the trailing triple are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): entry needs `rsi[t] > 50` while exit needs `rsi[t] < 50` on the same bar (and likewise strictly opposite EMA5/EMA10 relations) — the two regions are strictly disjoint, so entry and signal-exit never co-print even if ADX/volume legs hold, and the project-documented collide rule (entry ignored on collision) is a backstop that never activates. The reviewer is never asked to invent an ordering.
- Direction: long-only. `can_short` is unset and defaults `False` at the pinned framework commit; zero `enter_short`/`exit_short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the double-cross-plus-strength signal exit, the four-rung ROI ladder, the −32.11% fixed stop, and the trigger-gated trailer are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` apply — exits fire even at a loss; disclosed file literals). No breakeven move, no time exit beyond the ROI clock's terminal `0` leg — explicitly none, not invented. The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"703"`/`"2849"`/`"5520"`), preserved verbatim.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — the file's stray `position_stacking = "True"` string names no framework control and is engine-invisible, fenced above); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying four-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Bar-close precedence (predeclared derivation, disclosed): on a positioned book each completed bar evaluates closing legs in fixed order — (1) fixed stop, (2) trailing stop, (3) ROI rung (skipped when `enter_long` prints on the same bar, per the pinned `ignore_roi_if_entry_signal` semantic), (4) signal exit; entry is evaluated only on a flat book. At most one net position change per bar by construction plus the mutual-exclusion proof.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`open`/`close` for `hl2`, `close` for RSI/EMA seeds, `high`/`low`/`close` for ADX, `volume` for the guard) with fixed non-negative offsets (trailing windows plus one `shift(1)` lag inside each edge — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. `plot_config` is display-only. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar, `process_only_new_candles = True` set explicitly) are the file's own framework contract.

## Required data

- Completed `4h` bars of BTCUSDT: `open`/`close` (the `hl2` transform and RSI/EMA seeds), `high`/`low` (ADX), `volume` (the `volume > 0` guard — source-native, no repair needed; on 24/7 crypto tape this leg is almost always true and is kept verbatim, never optimized away). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (`informative_pairs` returns `[]`).
- Single decision timeframe `4h` (source-native — the file prints `timeframe = '4h'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 40 four-hour bars held flat. Covers the source `startup_candle_count = 30`, the ~27-bar ADX seeding span, the 10-bar RSI seed, and the one-bar edge lag with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed; the file's own lineage is a forex-system port, and no FX-session, calendar, or venue concept ships in the gating path, so the 24/7 crypto port changes no rule).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use (including the admitted TD-Sequential record, whose source likewise trades `limit` GTC orders and carries the identical limit→close derivation). No maker-touch, queue, or intrabar-path-dependent fill: entry, signal exit, stop, trailer, and ROI legs are all bar-close-evaluated under the fixed precedence above; the Signal mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Engine path (exact, disclosed): exact-`4h` PASS records already sit on `main` (the admitted Eterna TSI dual-path record — frontmatter `hb_ready_status: PASS` re-verified this cycle — plus the Eterna Donchian/Keltner/Chandelier `4h` cohort) — this record rides the same specified single-frame completed-bar `4h` Binance candle path, not an assumed one. Risk legs map onto the pinned engine's own triple-barrier machinery: the ROI ladder plus fixed stop are take-profit/stop-loss barriers of the form already modeled inside admitted records, and the trigger-gated trailer maps 1:1 onto the pinned backtesting tree's `PositionExecutorSimulator` (`HCH725/hummingbot@8b0e067`, `hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py`): `trailing_stop.activation_price` = 0.0186, `trailing_delta` = 0.0117, cummax-gated ratchet closing as `CloseType.TRAILING_STOP` — exactly the file's arm-at-offset / trail-under-peak / only-offset semantics, evaluated on the completed-bar frame under derivation (5) above. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder, stop, and trailer percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the entry edge opens the full unit on a flat book; the signal exit, any ROI rung, the fixed stop, or the trailer closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (128 lines: the `hl2`/RSI/EMA/ADX indicator block, the four-conjunct entry, the four-conjunct exit, the `timeframe`/`startup_candle_count`/`minimal_roi`/`stoploss`/trailing literals, the risk/behavior flags, and the `hlhb(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 40-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict current-bar `>`/`<` fires nothing on equality while the pinned edges admit prior-bar `<=`/`>=`; `adx` exactly `25` and `volume` exactly `0` both fail — disclosed, not smoothed.
3. Co-print arithmetic fenced (proven, not asserted): entry and signal-exit need strictly opposite RSI-vs-50 and EMA5-vs-EMA10 relations on the same bar — mutually exclusive by construction, and the predeclared fixed precedence binds regardless. Stop/trailer/ROI legs start at zero distance on the entry bar — the fixed precedence resolves them without intrabar claims, disclosed, not repaired.
4. Zero-variance fenced: flat tape pins RSI at 50-cross impossibility (no edge without movement), EMA5 == EMA10 (both cross edges false), ADX decaying toward 0 (strength leg false); flat volume prints `volume == 0` (guard leg false). No division by zero exists anywhere (all guards are comparisons; RSI/ADX internals are library-owned) — disclosed, not repaired.
5. Dead-import plumbing fenced: `numpy as np` / `pandas as pd` are imported and never called — display/plumbing leftovers with no gate effect. Zero `Parameter` spaces, zero fitted values, zero hyperopt imports anywhere — disclosed, never repaired into a signal.
6. Stray-attribute plumbing fenced: `position_stacking = "True"` (a string) names no control on the pinned `IStrategy` interface (verified absent from `interface.py` at the contemporaneous framework commit) — engine-invisible, with the single-unit/no-add pin above governing instead. Disclosed, never reinterpreted as stacking permission.
7. Cousin records fenced as different constructions (none conjoins an RSI-50 edge with an EMA5/10 edge under an ADX-25 strength gate, a volume guard, an ROI ladder, a fixed stop, and a trigger-gated trailer on `4h`): the admitted bare `ema-20-50-cross` sibling trades a naked EMA cross (no RSI, no ADX, no volume, different windows); the admitted `freqtrade-strategy001` sibling conjoins EMA-cross edges with Heikin-Ashi color states under an ROI ladder plus disaster stop (no RSI, no ADX, no volume, `5m`); the admitted `adx-di-cross-strength-gated` sibling crosses DI lines (not RSI, not EMAs) with an EMA50 level filter on `1d` two-sided; the Forven `adx-trend-pulse-reclaim` sibling reclaims pullbacks off custom EMA21/55 ewm bands on `1h` (no edge conjunction, no RSI, no trailer); open PR #331 `AdxSmas` crosses SMA3/6 on `1h` (no RSI leg, no volume guard, no trailing). Dropping either cross edge, the ADX gate, the volume guard, or the trailer would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other file in the official `user_data/strategies/` directory at the pinned commit (including the capitalized `Strategy001.py`–`Strategy005.py`, `Supertrend.py`, `UniversalMACD.py`, `MultiMa.py`, `Diamond.py`, `Bandtastic.py`, and the `berlinguyinca/` subdirectory that already supplies ten pool records) is a separate pin — their constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six predeclared pins (BTCUSDT market choice, same-bar-close market fills, 40-bar warmup floor, house sizing/costs, bar-close risk evaluation with fixed precedence, ROI-suppression folded under its pinned framework semantic) — all predeclared above. The `4h` frame, the `hl2`/RSI10/EMA5/EMA10/ADX14 constructions, the four-conjunct entry, the four-conjunct exit, the four-rung ROI ladder, the −32.11% stop, the trailing triple, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: four-conjunct entry / all lookbacks-inputs / four-conjunct exit / four-rung ROI / −32.11% stop / trailing triple / single-unit long-only / `4h` BTCUSDT / same-bar-close fills with fixed precedence are frozen.

- F1 — RSI relevance: dropping the RSI-50 cross edge (bare EMA5/10 cross with the same ADX/volume legs, same exit/risk) must not improve net expectancy; fail ⇒ the momentum edge adds nothing over the structural cross.
- F2 — Strength-gate relevance: dropping the `adx > 25` legs (same double-cross, same volume guard, same exit/risk) must not improve net expectancy; fail ⇒ strength certification adds nothing over the bare edge conjunction.
- F3 — Trailer relevance: disabling the trigger-gated trailer (ROI ladder plus fixed stop plus signal exit only, same entry) must not improve net expectancy; fail ⇒ the trailing leg adds nothing over the fixed risk stack.

## Crypto portability

BTCUSDT Binance perpetual `4h` is the research pin (source names no market; its docstring lineage is a forex-system port, and no session, calendar, or FX-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. The `volume > 0` guard reads native Binance 4h volume — no exotic feed. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib abstract internals (`RSI`/`EMA`/`ADX` seeding and rolling semantics, including the ADX 14-bar default) and the pinned `technical` `crossed_above`/`crossed_below` implementations live in their libraries outside the pinned strategy file — pinned by call with the contemporaneous definitions quoted above, not re-derived; exact reproduction inherits those modules' seeding alongside the file-local arithmetic, under the disclosed 40-bar floor.
- No breakeven, no time exit beyond the ROI clock's terminal `0` leg, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- Bar-close evaluation of stop/trailer/ROI plus same-bar-close market fills are the disclosed derivations (5) and (2) above: live limit-order-book behaviour, queue priority, and intrabar sequencing are scoped out, and this record makes no claim about the source's own limit-GTC backtest fills.
- `confidence`-style diagnostics do not exist in this file at all — nothing further to fence.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/hlhb.py
- https://github.com/freqtrade/freqtrade-strategies
