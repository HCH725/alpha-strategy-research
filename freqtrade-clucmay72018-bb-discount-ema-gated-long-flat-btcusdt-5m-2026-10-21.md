---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade ClucMay72018 BB-discount EMA-gated long-flat on BTCUSDT 5m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/ClucMay72018.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade ClucMay72018 BB-discount EMA-gated long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-multima`, `freqtrade-hlhb`, `freqtrade-simple-macd-bb-rsi`, `freqtrade-cofibit`, `freqtrade-strategy005`, `freqtrade-universalmacd`, `freqtrade-swinghightosky`, and `freqtrade-combined-binh-cluc` records at this same pin — this record pins ONLY the ClucMay72018 literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; re-verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/ClucMay72018.py`.
- GitHub blob SHA at the pinned commit: `ebb1a80f9bcd8edd570371cff243360467af06bf`, size 2893 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2893 bytes, 84 lines, SHA-256 `d146f7bc8285b5f1e48514d5d6acc53b37b0ca00299780210e3bdf84564978aa`, identical to the GitHub blob (`git hash-object` reproduces `ebb1a80f…af06bf`) — the entire file was retrieved and inspected.
- Registration: the file defines class `ClucMay72018(IStrategy)` (the only class in the file; header credits author Gert Wohlgemuth), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/**` sibling is a different pin with different constants.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `minimal_roi = { "0": 0.01 }`; `stoploss = -0.05`; entry `(dataframe['close'] < dataframe['ema100']) & (dataframe['close'] < 0.985 * dataframe['bb_lowerband']) & (dataframe['volume'] < (dataframe['volume'].rolling(window=30).mean().shift(1) * 20))` (`enter_long = 1`); exit `(dataframe['close'] > dataframe['bb_middleband'])` (`exit_long = 1`). No `trailing`, no `startup_candle_count`, no `can_short`, no `use_exit_signal` / `exit_profit_only` / `ignore_roi_if_entry_signal` override, no `order_types` mapping, no `informative_pairs` definition, no `position_adjustment`, no `max_open_trades` ships anywhere — the execution/position semantics below are disclosed as derived behaviour, never as file literals. The file ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.RSI(dataframe, timeperiod=5)` (TA-Lib RSI over default `close`); `ta.EMA(rsiframe, timeperiod=5)` over the RSI frame renamed to `close` (dead column, fenced below); `ta.MACD(dataframe)` (TA-Lib defaults 12/26/9 — dead column, fenced below); `ta.ADX(dataframe)` (TA-Lib default period 14 — dead column, fenced below); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` (typical price `(high+low+close)/3`, 20-bar mean ± 2σ); `ta.EMA(dataframe, timeperiod=50)` over `close` (stored under the literal column name `ema100` — a file-local misnomer, disclosed and never renamed/repaired). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no `fillna`/`ffill` in the file.
- Full-file token census (verified over the 84 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 1 `volume` line (the pump-cap guard only — the sole volume read in the file); 1 `shift` (the `.shift(1)` inside that same guard — the sole bar offset in the file, causal by construction); 0 `cross` (no `crossed_above`/`crossed_below` edge anywhere — both legs are persistent level states, never one-bar edges); 0 `trailing` / 0 `startup_candle_count` / 0 `can_short` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `process_only_new_candles` / 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` / 0 `stoploss_on_exchange` (all such execution/position/economic semantics are predeclared researcher pins below, never file semantics); 0 `informative` / 0 `resample` / 0 `merge_informative` / 0 `fillna` / 0 `ffill` / 0 `interpolate` (no second pair, no second timeframe, no NaN patching — strict NaN comparisons simply stay false); 0 `position_adjustment` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `IntParameter` / 0 `hyperopt` (no tuning scaffolding of any kind — every literal below is a frozen file constant); 0 `lookahead` / 0 `future` (no future-leakage primitive by name or construction).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 100-bar researcher warmup floor (covers the 50-bar EMA seed, the 30-bar volume window plus its 1-bar shift, and the 20-bar Bollinger seed with margin); (4) framework-default execution semantics pinned as derived behaviour (signal exits enabled as coded with no profit gate, ROI/stop legs bar-close-evaluated — disclosed, never presented as file literals); (5) the house cost/capital overlay replaces the absent source economics. Every period, every threshold, the entry conjunction, the exit comparison, the ROI scalar, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `ClucMay72018`, `cluc-may`, and `clucmay` returns only the admitted `freqtrade-combined-binh-cluc` record (dual-leg OR system with a second BinHV penetration leg, ROI `0.05`, and a profit-gated midline exit) and the admitted `freqtrade-bband-rsi` record (which cites this file only in its sibling-file fence) — no standalone single-leg ClucMay72018 record exists anywhere on `main`. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a BB-discount/EMA-gated dip system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims no behavioural channel anywhere in the 84 lines beyond its code: buy the bar where the close prints under its 50-bar EMA while also printing more than 1.5% under the 20-bar lower Bollinger band on typical price, provided the bar's volume is not an extreme spike (under 20× its trailing 30-bar mean), and stand aside to flat when the close reclaims the 20-bar Bollinger midline, behind a flat 1% take-profit and a −5% stop. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Research interpretation

Mean-reversion dip buyer that only buys dips inside a weak-tape regime, long-only, exited mostly by the midline reclaim or the tight 1% ROI. Unlike pure band-touch buyers that fire on any lower-band penetration, the entry demands a double discount (sub-EMA50 trend filter AND a 1.5% undercut of the lower band — the close must stretch past the band, not merely tag it), so chop-around-the-band bars do not qualify. Unlike volume-breakout entries, the volume conjunct is a veto, not a trigger: it fails only on >20× volume-spike bars, so entries fire on quiet capitulation bars and skip pump/exhaustion bars. The coded consequence is a buyer of quiet, stretched washouts under a sagging EMA that rents exposure until the midline reclaim or, far more often on drifting tape, the 1% take-profit — the −5% stop bounds the failures where the washout keeps washing.

## Signal

Exact rule as pinned (any other band window, multiplier, discount fraction, volume multiple, EMA period, ROI/stop pair, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
bb_lower20[t], bb_mid20[t] = qtpylib BB(20, 2) over typical price (lower / mid)
ema50[t]      = TA-Lib EMA(close, 50)              // column literally named 'ema100' in file — disclosed misnomer
volMA30[t-1]  = mean(volume[t-30 .. t-1])          // rolling(30).mean().shift(1), causal by construction
entry    = (close[t] < ema50[t]) & (close[t] < 0.985 * bb_lower20[t]) & (volume[t] < 20 * volMA30[t-1])  // enter_long = 1
exit_sig = (close[t] > bb_mid20[t])                // exit_long = 1
risk = flat take-profit at +1% from entry (minimal_roi {"0": 0.01});
       fixed stop at -5% (stoploss -0.05); no trailing/trailer of any kind
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the three-conjunct discount state, `direction` long-only; `exit_long=1` on any bar printing the midline reclaim. Both legs are STATE prints in construction (each persists while its levels hold — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code). New-interface `enter_long`/`exit_long` columns read as enter-long/exit-long directly.
- Exact boundaries (pinned semantics): strict throughout (`<`, `>` exactly as coded — a close landing exactly on the EMA50, exactly on `0.985 × lower`, exactly on `20 ×` mean volume, or exactly on the midline fires nothing on that conjunct). The `50` / `20` / `2` / `0.985` / `30` / `20×` / `0.01` / `-0.05` literals are never tuned here.
- Misnomer fence (pinned, disclosed — not a repair site): the column the entry reads is literally named `ema100` but is constructed by `ta.EMA(dataframe, timeperiod=50)` — a 50-bar EMA of close, not a 100-bar one. This record evaluates the 50-bar object the code actually builds; no reviewer repair may substitute a 100-bar EMA.
- Dead-indicator fence (pinned, disclosed — not a repair site): `rsi(5)`, `emarsi` (EMA-5 of the RSI frame), `macd`/`macdsignal`/`macdhist` (12/26/9 defaults), `adx` (14 default), and `bb_upperband` are computed and never read by any gating line. This record never conditions on them and no reviewer repair may promote any of them into a leg.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `close[t] < 0.985 × bb_lower20[t] < bb_lower20[t] ≤ bb_mid20[t]` (σ ≥ 0 orders lower ≤ mid; `0.985 × lower < lower` for the positive bands of positive prices), hence `close[t] > bb_mid20[t]` is false on that bar — entry and signal-exit never co-print outside degenerate non-positive-band windows, which the warmup below excludes. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the ungated midline signal exit, the +1% ROI leg, and the −5% stop are the complete position-closing set (no `use_exit_signal` / `exit_profit_only` override ships anywhere, so the derived rule honors the signal exit as coded on every reclaim bar with no profit gate — disclosed, never presented as a file literal). No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying discount bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`close` for the EMA leg, `high`/`low`/`close` inside typical price for the bands, `close` plus `volume` for the discount-plus-cap leg) with fixed non-negative offsets — the sole `shift(1)` reads the causal `t-30..t-1` volume mean, never a future bar. No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge (no `informative_pairs` definition ships at all), interpolate, or stop/limit order argument anywhere in the gating path. Freqtrade engine column semantics (`enter_long`/`exit_long` per completed bar) are the file's own framework contract.

## Required data

- Completed `5m` bars of BTCUSDT: `close` for the EMA50 leg; `high`/`low`/`close` for the BB(20, 2)-on-typical-price legs; `close` plus `volume` for the discount-plus-cap leg. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only (the volume mean is explicitly shifted one bar back); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher floor, disclosed): the record-rule floor holds 100 five-minute bars flat (~8.3 hours). Covers the 50-bar EMA seed, the 30-bar volume window plus its 1-bar shift, and the 20-bar Bollinger seed with margin. Coded behaviour underneath: TA-Lib/qtyplib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early; no `fillna`/`ffill` exists to smear them). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced `5m` siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal-exit, and ROI/stop legs are all bar-close-evaluated; the mutual-exclusion proof leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted Strategy005 volume-surge Fisher-washout, UniversalMACD EMA-ratio dip-band, CombinedBinHAndCluc dual-leg penetration, CofiBit StochF rail, Quickie TEMA-slope, and Simple MACD-BB-RSI records — all `5m` Freqtrade-sourced long-flat at this repository pin) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding. The volume-cap leg reads the same candle's `volume` field already present on that path (no new feed).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its +1% ROI and −5% stop percentages are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the discount entry opens the full unit on a flat book; signal exit, the ROI leg, or the stop closes it in full; re-entry after an exit needs only the next qualifying discount bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (84 lines: the RSI/EMA-RSI/MACD/ADX/Bollinger/EMA50 precompute block, the three-conjunct discount entry, the midline reclaim exit, and the `timeframe`/`minimal_roi`/`stoploss` literals). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit; no `fillna`/`ffill` exists to smear seeds forward). The 100-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fires nothing on equality on every conjunct (close exactly on EMA50, on `0.985 × lower`, on `20 ×` mean volume, or on the midline holds flat) — disclosed, not smoothed.
3. Co-print arithmetic fenced (impossible, proved — disclosed, not repaired): `close < 0.985 × lower ≤ mid` contradicts `close > mid` on every positive-band bar, so no bar can print both legs; ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins the bands to the flat price (the `0.985` undercut conjunct fails — no entry can print) and the volume mean to the flat volume (the cap conjunct passes trivially but cannot fire alone). No division by zero exists in the gating path (all legs are comparisons; indicator division lives inside the library calls, never in a gate denominator) — disclosed, not repaired.
5. Spike-veto asymmetry fenced: the volume conjunct (`volume < 20 ×` trailing mean) vetoes only >20× spike bars, so entries fire on quiet tape and skip exhaustion bars — disclosed as effective behaviour, never re-thresholded.
6. Dead-code plumbing fenced: `rsi`, `emarsi`, `macd`/`macdsignal`/`macdhist`, `adx`, and `bb_upperband` never govern any gate; the `ema100` column name never changes the 50-bar object it holds — this record never conditions on the dead columns and no reviewer repair may promote any of them into a leg or substitute a 100-bar EMA.
7. Cousin records fenced as different constructions (none trades a single-leg EMA50/`0.985`-discount dip with a volume-spike veto and an ungated midline exit on `5m`): the admitted CombinedBinHAndCluc sibling ORs this file's discount shape with a second BinHV penetration leg, pays ROI `0.05`, and profit-gates its midline exit (different trigger set, different risk pair, gated exit); the admitted BbandRsi sibling trades a lower-band tag with an RSI-momentum filter on `1h` (different primitives, different frame); the admitted Simple sibling trades MACD-plus-Bollinger-plus-RSI momentum confluence (never a band-discount washout); the admitted CofiBit sibling trades a fast-stoch oversold edge with EMA rails (edge primitive, never level states); the admitted Strategy005 sibling trades a volume-surge Fisher washout (surge direction inverted — it buys spikes, this record vetoes them); the admitted UniversalMACD sibling trades a single EMA-ratio band with an empty signal exit (no oscillator, no band exit). Not a threshold re-tuning of any of them: changing any period, fraction, multiple, ROI, or risk literal would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `user_data/strategies/**` sibling is a separate pin — its constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 100-bar warmup floor, derived ungated-signal-exit/roi-on-entry-bar execution semantics, house sizing/costs) — all predeclared above. The `5m` frame, the EMA50/`0.985`-discount/volume-cap entry, the midline reclaim exit, the +1% ROI, the −5% stop, the absent trailer, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: discount entry / all five periods (`50` EMA, `20`/`2` bands, `30` volume, 1-bar shift) / `0.985` fraction / `20×` multiple / reclaim exit / +1% ROI / −5% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Spike-veto relevance: dropping the volume-cap conjunct (pure EMA50/`0.985`-discount entry, same exit/risk) must not improve net expectancy; fail ⇒ the >20× spike veto adds nothing over the bare double-discount entry.
- F2 — Discount-depth relevance: softening the band fraction to `1.0` (mere lower-band tag under EMA50, same veto/exit/risk) must not improve net expectancy; fail ⇒ the 1.5% stretch past the band adds nothing over a plain band tag.
- F3 — Regime-filter relevance: dropping the sub-EMA50 conjunct (pure `0.985`-discount-plus-veto entry, same exit/risk) must not improve net expectancy; fail ⇒ the EMA-regime arm adds nothing over the bare band stretch.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only the `high`/`low`/`close`/`volume` candle fields are read (venue definition differences move only indicator inputs, disclosed). Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib/qtpylib internals live in their libraries outside the pinned file — pinned by call with explicit periods, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local threshold wiring, under the disclosed 100-bar floor.
- No tuning scaffolding exists anywhere in the file: every operative literal is a frozen file constant. Any re-optimization would be a different, unpinned rule.
- The signal exit needs a full reclaim of the 20-bar midline — on drifting tape most round-trips close via the tight +1% ROI or the −5% stop instead. This record repairs nothing: the effective behaviour is fully explicit and complete, and any quicker exit band would be a different, unpinned rule no reviewer may invent.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair. The `ema100`-named-50-bar wiring and the permissive spike veto ride the file literals — disclosed as the record's principal behavioural risks.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close convention; this record makes no claim about any live-order behaviour.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/ClucMay72018.py
- https://github.com/freqtrade/freqtrade-strategies
