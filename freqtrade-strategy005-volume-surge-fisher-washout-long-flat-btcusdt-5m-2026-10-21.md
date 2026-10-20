---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Strategy005 volume-surge Fisher-washout fade RSI-cross exit long-flat on BTCUSDT 5m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Strategy005.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Strategy005 volume-surge Fisher-washout fade RSI-cross exit long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that supplied the admitted `freqtrade-combined-binh-cluc` record at this same pin — this is only its second record from this repository identity, and its first `Strategy00x` numbered record; the admitted strategy001/002/003/004 records come from the older `berlinguyinca` upstream at pin `ae998ae`, a different repository with different file literals).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/Strategy005.py`.
- GitHub blob SHA at the pinned commit: `c0d2025f62ea9cfc4f0f2335905f18b55556627e`, size 6667 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 6667 bytes, 185 lines, SHA-256 `797b293f5acd809f8c77f26b38c004c87b75d8847be4cde4d0224040cc591030`, identical to the GitHub blob (`git hash-object` reproduces `c0d2025f…556627e`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Strategy005(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/*.py` sibling is a different pin with different constants — this record pins ONLY the Strategy005 literals below, and no reviewer repair may substitute a sibling constant.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '5m'`; `minimal_roi = { "1440": 0.01, "80": 0.02, "40": 0.03, "20": 0.04, "0": 0.05 }`; `stoploss = -0.10`; `trailing_stop = False`; `process_only_new_candles = True`; `use_exit_signal = True`, `exit_profit_only = True`, `ignore_roi_if_entry_signal = False`; `order_types = { 'entry': 'limit', 'exit': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False }`; frozen hyperopt file literals `buy_params = { "buy_fastd": 1, "buy_fishRsiNorma": 5, "buy_rsi": 26, "buy_volumeAVG": 150 }` and `sell_params = { "sell_fishRsiNorma": 30, "sell_minusDI": 4, "sell_rsi": 74, "sell_trigger": "rsi-macd-minusdi" }`. The docstring attribution (`Strategy 005 / author@: Gerald Lonlas`) is lineage only — no performance, sample, window, trade count, or cost basis ships anywhere in the 185 lines.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.MACD(dataframe)` (TA-Lib defaults fastperiod 12 / slowperiod 26 / signalperiod 9 — `macd`/`macdsignal` live the exit leg); `ta.MINUS_DI(dataframe)` (TA-Lib default `timeperiod=14` — lives the exit gate); `ta.RSI(dataframe)` (TA-Lib default `timeperiod=14` — lives both legs); inverse-Fisher file-local arithmetic `fisher_rsi = (exp(2*r)-1)/(exp(2*r)+1)` with `r = 0.1*(rsi-50)` and `fisher_rsi_norma = 50*(fisher_rsi+1)` (pure functions of the RSI column — no new seed beyond RSI14); `ta.STOCHF(dataframe)` with NO explicit arguments (TA-Lib abstract defaults fastk_period 5 / fastd_period 3 / fastd_matype 0 — `fastd`/`fastk` live the entry legs; the same default triple the admitted CofiBit sibling pins explicitly); `ta.SAR(dataframe)` (TA-Lib defaults 0.02/0.2 — computed but read ONLY by the unfrozen `sar-fisherRsi` exit branch, dead at the frozen trigger, fenced below); `ta.SMA(dataframe, timeperiod=40)` (explicit 40 — lives the entry regime leg). `informative_pairs()` returns `[]` (empty list literal — no second pair, no second timeframe, single-frame by construction). No DB, no network, no `request.*`, no `security()` in the file.
- Full-file token census (verified over the 185 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 3 `volume` (the surge-gate column read plus its rolling mean — the ONLY volume touch, fenced as the gating leg, never a second feed); 0 `resample` (no resampling anywhere — the leaky upsample-interpolate helper of the berlinguyinca `CCIStrategy`/`Reinforced*` siblings does not exist in this file); 0 `position_adjustment` / 0 `max_open_trades` / 0 `startup_candle_count` (the position pin and the 200-bar floor below are predeclared researcher rules, never file semantics); 0 `leverage` / 0 `can_short` / 0 `funding` / 0 `mark_price` (no economics beyond ROI/stop/order-types); 0 `fillna` / 0 `ffill` / 0 `interpolate` (no NaN patching anywhere — strict NaN comparisons simply stay false); 0 `shift` (the only edge is the single `crossed_above` exit — a fixed one-bar offset, no forward reference); 1 `crossed_above` (the exit RSI-74 edge — the only edge primitive); 10 hyperopt/`Parameter` tokens (the `IntParameter`/`CategoricalParameter` declarations plus the `buy_params`/`sell_params` freeze — the optimize-spaces are fenced out, the frozen file literals are the rule, see Signal); 1 `order_types` (limit/limit/market plumbing, mapped to the derived fill convention below); 0 `position_size` reads; 0 `syminfo` (the file names no market).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (no full-sample scalar, no repainting primitive, no multi-timeframe merge, no external package — no repair site exists). Researcher-declared adaptations are exactly four: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills (the source declares limit entry/exit plus market stop — mapped to bar-close evaluation under the house path, disclosed); (3) single-unit/no-add/no-cooldown position pin plus a 200-bar researcher warmup pin (covers the 150-bar volume-mean seed, the SMA40 seed, the MACD seed, and the RSI/Fisher/STOCHF/MINUS_DI/SAR seeds with margin); (4) the house cost/capital overlay replaces the absent source economics. Every threshold, every lookback, the frozen hyperopt literals, the entry conjunction, the frozen exit branch, the ROI ladder, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `fishRsiNorma`, `fisher_rsi_norma`, `buy_volumeAVG`, and `sell_trigger` returns zero strategy records — no record trades this file's volume-surge-plus-Fisher-washout entry or its RSI-cross/MACD/minusDI exit. The `Strategy005` filename hits are prose sibling-fence mentions only (the admitted HLHB record names it as an explicitly unpinned sibling, never a record of it). The two loose `minus_di`-adjacent hits are different mechanisms (Alexander filter trailing extremum; dual-thrust range breakout — neither trades a DMI exit leg). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas) trades a Fisher-washout/volume-surge system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where a 4× volume surge erupts while price still sits beneath its 40-bar average, the fast stochastic stays bearishly aligned (fastd above fastk) yet above 1, RSI holds above 26, and the normalized Fisher presses under 5 — and stand aside to flat when RSI crosses up through 74 while MACD stays negative and minusDI holds above 4 (profitable exits only), behind a decaying take-profit ladder (5% inside 20 min down to 1% after 24 h) and a −10% stop. No behavioural, structural, or risk-premium channel is claimed anywhere in the 185 lines.

### Research interpretation

Volume-backed washout fade, long-only, with an exit that demands overheating-plus-non-confirmation. Unlike pure dip systems that buy any cheap print, the entry needs fuel (volume over 4× its 150-bar mean — quiet drifts print nothing) AND structure (close under SMA40 with the stoch still bearishly stacked — no chasing prints that already reclaimed the average) AND a bounded washout (Fisher under 5 with RSI still above 26 — despair, but not a dead tape). Unlike oscillator-exit records, the exit never sells weakness: it fires only on RSI crossing 74 into heat while MACD refuses to confirm (still negative) and minusDI stays bid — a top-tick fade of unconfirmed strength, further gated to profitable closes only. The coded consequence is a buyer of loud-MFI-free washouts (no MFI anywhere — unlike the strategy003 sibling) that harvests unconfirmed RSI heat, laddered profits, or the wide stop.

## Signal

Exact rule as pinned (any other hyperopt literal, lookback, threshold, edge construction, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
macd[t], macdsignal[t] = TA-Lib MACD(close; 12/26/9)
minus_di[t]  = TA-Lib MINUS_DI(high/low/close, 14)
rsi[t]       = TA-Lib RSI(close, 14)
fisher[t]    = (exp(2*r[t])-1)/(exp(2*r[t])+1), r[t] = 0.1*(rsi[t]-50)
norma[t]     = 50*(fisher[t]+1)                      // [0,100] washout gauge
fastk[t], fastd[t] = TA-Lib STOCHF(close windows; 5/3/0 defaults)
sar[t]       = TA-Lib SAR(high/low; 0.02/0.2, DEAD at frozen trigger)
sma40[t]     = TA-Lib SMA(close, 40)
volMA150[t]  = mean(volume[t-149 .. t])
entry = (close[t] > 0.000002) AND (volume[t] > 4*volMA150[t])
        AND (close[t] < sma40[t]) AND (fastd[t] > fastk[t])
        AND (rsi[t] > 26) AND (fastd[t] > 1) AND (norma[t] < 5)   // enter_long = 1
exit_sig = crossed_above(rsi, 74)[t] AND (macd[t] < 0) AND (minus_di[t] > 4)
                                                 // exit_long = 1, profitable closes only
risk = decaying take-profit minimal_roi {"1440":0.01,"80":0.02,"40":0.03,"20":0.04,"0":0.05};
       fixed stop at -10% (stoploss -0.10); trailing_stop False (0.01/0.02 present-but-disabled)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the seven-conjunct state, `direction` long-only; `exit_long=1` on bars printing the frozen three-conjunct exit. The `crossed_above` leg is an edge print (true only on the crossing bar); the level legs persist while true — close-and-hold-flat. New-interface `enter_long`/`exit_long` columns read as enter-long/exit-long directly.
- Hyperopt freeze (pinned file literals, never tuned here): entry uses `buy_volumeAVG=150`, `buy_rsi=26`, `buy_fastd=1`, `buy_fishRsiNorma=5` exactly as printed in the file's `buy_params` dict; exit uses `sell_rsi=74`, `sell_minusDI=4`, `sell_trigger='rsi-macd-minusdi'` exactly as printed in `sell_params`. The `IntParameter` low/high ranges and `optimize=True` spaces are unfrozen search scaffolding — excluded from the rule, and adopting any other point in those spaces would be a different, unpinned rule. The `CategoricalParameter` declaration's anomalous `default=30` (an int outside its own two-string menu) never governs: the file's `sell_params` literal pins the trigger to `'rsi-macd-minusdi'` — disclosed, not repaired. The `sar-fisherRsi` exit branch (`sar > close` AND `fisher > sell_fishRsiNorma`) is therefore unreachable under the frozen trigger and fenced as an unpinned variant — no reviewer repair may activate it.
- Exact boundaries (pinned semantics): strict throughout (`>`, `<` exactly as coded — volume exactly at 4× mean, close exactly on SMA40, rsi exactly on 26, fastd exactly on 1, norma exactly on 5, macd exactly on 0, minusDI exactly on 4 fires nothing on that conjunct; the exit edge fires only on the strict cross above 74). The dust literal `0.000002` is a permanent no-op on BTCUSDT (pinned, never dropped — disclosed). The `4×` volume multiple and the `150`-bar mean window are literals, never tuned here.
- Same-bar co-print pin (arithmetically impossible, resolved by position pin — disclosed, not repaired): entry needs `norma < 5` (a strict monotone transform of RSI — norma under 5 forces RSI deep under 30) while the exit needs `crossed_above(rsi, 74)` on the same bar — one bar's RSI cannot satisfy both; the exit's `macd < 0` further excludes hot tapes the entry could never print on. No engine ordering is invented: under the single-unit position pin, a flat book treats any residual co-print bar as entry (the exit leg needs a position and is a no-op without one — no same-bar round-trip), while a positioned book treats it as exit-close. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the frozen three-conjunct signal exit (profitable closes only via file-literal `exit_profit_only = True` with `use_exit_signal = True`), the five-rung decaying ROI ladder, and the −10% market stop (`stoploss_on_exchange = False` — exchange emulation off, disclosed) are the complete position-closing set. `ignore_roi_if_entry_signal = False` is the file literal (entry bars do not suppress ROI — disclosed default, never a file invention). No trailing (`trailing_stop = False` file literal — the `0.01`/`0.02` values are present-but-disabled, never to be enabled by repair), no time exit beyond the ladder, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying seven-conjunct bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`close` for SMA/RSI/Fisher/STOCHF/MACD/dust, `high`/`low` for MINUS_DI/SAR internals, `volume` only for the surge multiple) with fixed non-negative offsets (trailing windows plus the one-bar `crossed_above` edge — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge (`informative_pairs` returns `[]`), interpolate, or stop/limit order argument anywhere in the gating path. `process_only_new_candles = True` is the file's own completed-bar contract.

## Required data

- Completed `5m` bars of BTCUSDT: `close` for the SMA40 regime, RSI/Fisher/STOCHF/MACD paths, dust filter, and exit legs; `high`/`low` for the MINUS_DI(14) path (SAR internals dead at the frozen trigger); `volume` for the 4×-surge gate against its 150-bar mean. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 200 five-minute bars held flat (~16.7 hours). Covers the 150-bar volume-mean seed (the longest window), the SMA40 seed, the MACD 26+9 seed, the RSI14/Fisher seed, the STOCHF seed, the MINUS_DI14 seed, and the SAR seed with margin. Coded behaviour underneath: rolling/TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early; no `fillna` exists to smear them). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced siblings use. The source's `limit` entry/exit plus market-stop plumbing is mapped to bar-close evaluation (no maker-touch, queue, or intrabar-path-dependent fill): entry, signal exit, and ROI/stop legs are all bar-close-evaluated; the Signal co-print rule leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin. `process_only_new_candles = True` is source-native completed-bar semantics.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` (the admitted ASDTSRockwellTrading MACD-polarity state, MACDStrategy MACD-CCI dip-state, strategy002 hammer-gated oversold, strategy003 RSI-Fisher-MFI washout, strategy004 ADX-gated CCI washout, Quickie TEMA-slope, Simple MACD-BB-RSI, and CofiBit fast-stoch records — all `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding. Volume for the surge gate rides the same candle feed (the EMASkipPump sibling already evidences a `5m` volume-guard leg on this path).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the seven-conjunct entry opens the full unit on a flat book; the signal exit, any ROI rung, or the stop closes it in full (profitable closes only for the signal leg per file literal); re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (185 lines: the MACD/MINUS_DI/RSI/Fisher/STOCHF/SAR/SMA indicator block, the seven-conjunct entry with its volume-surge-plus-washout legs, the frozen `rsi-macd-minusdi` exit branch, the `timeframe`/`minimal_roi`/`stoploss`/`trailing_stop`/`use_exit_signal`/`exit_profit_only`/`order_types` literals, the `buy_params`/`sell_params` freeze, and the `Strategy005(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib/rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit; no `fillna` exists to smear seeds forward). The 200-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `>`/`<` fires nothing on equality on every conjunct; the exit edge fires only on the strict cross above 74. Volume exactly at 4× mean, RSI exactly on 26, norma exactly on 5 holds flat — disclosed, not smoothed.
3. Co-print arithmetic fenced (impossible, resolved — disclosed, not repaired): `norma < 5` forces RSI deep under 30 by strict monotone transform while the exit needs a cross above 74 on the same bar — one RSI print cannot satisfy both. The position pin resolves any residual (flat → enter, positioned → exit-close, never a same-bar round-trip). ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
4. Zero-variance fenced: flat tape pins RSI midscale (failing the norma-under-5 conjunct), STOCHF midscale (failing the fastd-under-or-over legs as coded), volume to its own mean (the 4× multiple fails), and SMA40 onto the flat line (the `close < sma40` leg fails on exact equality). No division by zero exists anywhere in the gating path (all legs are comparisons or library-internal rolling arithmetic) — disclosed, not repaired.
5. Dead-column plumbing fenced: `macdsignal` and `sar` are computed every bar and read nowhere under the frozen trigger (signal-line and SAR are display/plumbing leftovers with no gate effect — the exit reads `macd < 0` only); the `sar-fisherRsi` exit branch is unreachable under the frozen `sell_trigger` and fenced as an unpinned variant. This record never conditions on them and no reviewer repair may promote either into a leg. The optimize-spaces (`IntParameter` ranges, `optimize=True`) are scaffolding, never signal — the frozen `buy_params`/`sell_params` literals are the rule.
6. Hyperopt freeze fenced: the ten hyperopt tokens resolve to the eight frozen file literals plus the two dict containers — `150/26/1/5` buy, `30/4/74/'rsi-macd-minusdi'` sell (the `sell_fishRsiNorma=30` literal governs only the unfrozen branch and is fenced with it). Adopting any other point of the declared low/high spaces would be a different, unpinned rule. The `default=30` anomaly on the trigger declaration never governs under the `sell_params` freeze — disclosed, not repaired.
7. Cousin records fenced as different constructions (none conjoins a 4× volume surge with a sub-SMA close, an inverted-stoch alignment, an RSI floor, and a normalized-Fisher washout, exited by RSI-74-cross with MACD-negative and minusDI gate): the admitted strategy003 sibling trades an RSI-ceiling (`< 28`) plus MFI `< 16` washout with an EMA-regime OR-arm and a SAR-plus-Fisher exit (RSI direction inverted, MFI-gated, no volume leg, different exit, different risk); the admitted strategy004 sibling trades an ADX-gated CCI washout with a hand-rolled dual-STOCHF recross, a volume floor (`mean-volume > 0.75`), and a slowADX exit (no Fisher, no SMA regime, level-recross construction, different exit); the admitted CofiBit sibling trades a fast-stoch oversold EDGE (`crossed_above` fastk/fastd under 30) with EMA high/low rails and an ADX gate (edge primitive, never the level alignment `fastd > fastk` used here; no volume, no Fisher, no SMA); the admitted MACDStrategy sibling trades a MACD-CCI dip-state (no Fisher washout, no volume surge, no SMA regime). Not a threshold re-tuning of any of them: dropping the volume surge, flipping any RSI/Fisher inequality, or substituting the exit triple would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `user_data/strategies/*.py` and `berlinguyinca/*.py` sibling is a separate pin — its constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the four declared adaptations (BTCUSDT market choice, same-bar-close fills mapped from limit/market plumbing, single-unit/no-add/no-cooldown position pin with 200-bar warmup floor, house sizing/costs) — all predeclared above. The `5m` frame, the seven-conjunct entry with every literal, the frozen three-conjunct exit, the ROI ladder, the −10% stop, the disabled trailer, the profitable-exits-only gate, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: seven-conjunct entry / all lookbacks, thresholds, frozen hyperopt literals / frozen exit branch / ROI ladder / −10% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — Volume-surge relevance: dropping the `volume > 4×mean(150)` conjunct (same washout-plus-regime entry, same exit/risk) must not improve net expectancy; fail ⇒ the fuel gate adds nothing over the quiet washout state.
- F2 — Washout relevance: dropping the `norma < 5` conjunct (same surge-plus-regime entry, same exit/risk) must not improve net expectancy; fail ⇒ the Fisher-washout gauge adds nothing over the ungated surge-plus-dip state.
- F3 — Exit-triple relevance: replacing the frozen exit with ROI/stop-only exits (same entry, same risk) must not improve net expectancy; fail ⇒ the RSI-74-cross/MACD-negative/minusDI gate adds nothing over fixed risk alone.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only standard OHLCV candle fields are read (`close`/`high`/`low` for indicators, `volume` for the surge multiple against its own rolling mean — venue volume-definition differences move only that multiple, disclosed). Funding is declared nowhere in the source and modeled only downstream by house assumptions. The dust literal never binds on BTCUSDT (quoted as written, disclosed as no-op here).

## Limitations

- TA-Lib MACD/MINUS_DI/RSI/STOCHF/SAR/SMA internals and the `qtpylib.crossed_above` edge arithmetic live in their libraries outside the pinned file — pinned by call with defaults/explicits, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local Fisher wiring, under the disclosed 200-bar floor. The no-argument `ta.STOCHF(dataframe)` call inherits the library's 5/3/0 defaults — quoted as written, never reinterpreted.
- Hyperopt scaffolding is frozen, not searched: the `IntParameter` ranges and `optimize` flags never execute under this record; only the eight `buy_params`/`sell_params` literals govern. Any re-optimization would be a different, unpinned rule.
- The `sar-fisherRsi` exit branch and the `sell_fishRsiNorma=30` literal are unreachable under the frozen trigger — a reader must not mistake them for gates; they gate nothing here.
- No trailing, no breakeven, no time exit beyond the ROI ladder, no short leg, no cooldown — all explicitly absent, never to be added by repair. Signal exits fire on profitable closes only (`exit_profit_only` literal) — a hot RSI cross at a loss holds, disclosed as the record's principal risk.
- The limit-order plumbing is mapped to same-bar-close market fills under the derived convention — the adaptation is disclosed, not hidden, and this record makes no claim about the source plumbing's performance.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Strategy005.py
- https://github.com/freqtrade/freqtrade-strategies
