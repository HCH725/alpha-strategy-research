---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade SmoothOperator V-bottom smoothed-composite long-flat on BTCUSDT 5m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothOperator.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade SmoothOperator V-bottom smoothed-composite long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (open-source Freqtrade strategy collection; the same lane that supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-bband-rsi-dip-buy`, `freqtrade-awesome-macd`, `freqtrade-emaskippump`, `freqtrade-adx-momentum`, `freqtrade-cmcwinner`, `freqtrade-asdts-rockwell`, `freqtrade-macd-cci-dip-state`, `freqtrade-binhv27`, `freqtrade-macd-cross-cci-edge`, `freqtrade-strategy002`, and `freqtrade-strategy004` records — this is only its thirteenth record, and the first pinned to this exact file).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/SmoothOperator.py`.
- GitHub blob SHA at the pinned commit: `cf5b30a86d11bc63e0b2dfb84a2a02ea30590838`, size 13297 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 13297 bytes, 304 lines, SHA-256 `46f608cc51f9b18e9bb52983776a6d55d9b13814a93f7666cc8ecdb4f86c3915`, identical to the GitHub blob (`git hash-object` reproduces `cf5b30a8…090838`) — the entire file was retrieved and inspected.
- Registration: the file defines class `SmoothOperator(IStrategy)` (the strategy class) plus a `StrategyHelper` static-pattern class whose only order-gating member is `eight_green_candles` (the remaining helpers — `seven_green_candles`, `eight_red_candles`, `four_green_one_red_candle`, `four_red_one_green_candle` — are never called by any order line, fenced below). `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/*.py` sibling is a different pin with different constants.
- The file's own words (quoted for gate evidence, never extended): docstring idea `combining several common indicators, with a heavily smoothing, while trying to detect a none completed peak shape`; header caution `DO NOT USE, just playing with smooting and graphs!` (an author-reliability caution, fenced as prose — the coded legs below are deterministic regardless, and this record claims no live suitability); `timeframe = '5m'`; `minimal_roi = { "0": 0.10 }` (a single 10% rung); `stoploss = -0.05`; live indicator block `ta.CCI(dataframe, timeperiod=20)`, `ta.RSI(dataframe, timeperiod=14)`, `ta.ADX(dataframe)` (default period — computed and never read by any order line, fenced dead), `ta.MFI(dataframe)` (default period 14), `ta.EMA(..., timeperiod=11, price='mfi'/'cci'/'rsi')` triple smooth, weighted composite `(rsi_smooth * 1.125 + mfi_smooth * 1.125 + cci_smooth) / 3` with `ta.TEMA(..., timeperiod=21, price='mfi_rsi_cci_smooth')`, `qtpylib.bollinger_bands(dataframe['close'], window=20, stds=2)` mid-band (computed twice with identical parameters — idempotent overwrite, fenced), `average = (close + open + high + low) / 4`; live entry is the uptrend conjunct `(close > close.shift())` gating three OR arms (lopsided V-bottom shape with slow-average, sub-mid prior low, prior CCI < −100, prior RSI < 30; deep-oversold low/CCI −200/RSI 30/MFI 30; extreme MFI 10/CCI −150/RSI-below-MFI — see Signal); live exit is a three-arm OR (`mfi_rsi_cci_smooth` peak-shape, `StrategyHelper.eight_green_candles`, CCI > 200 with RSI > 70 — see Signal). No `trailing_stop` attribute ships anywhere (only a `# should be converted to a trailing stop loss` code comment — quoted absence, never a leg); no `startup_candle_count`, no `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `ignore_roi_if_entry_signal`, no `process_only_new_candles`, no order-type mapping ships anywhere — the framework defaults below are disclosed as derived behaviour, never as file literals. The file ships no sample, window, trade count, or cost basis.
- Out-of-file calls pinned (all resolved by name, all standard): `ta.CCI` (TA-Lib CCI on high/low/close, explicit period 20); `ta.RSI` (TA-Lib RSI over default `close`, explicit period 14); `ta.MFI` (TA-Lib MFI, default period 14 — no override in the file, disclosed); `ta.EMA` (TA-Lib EMA over the stated derived series, explicit period 11); `ta.TEMA` (TA-Lib TEMA over the composite, explicit period 21); `qtpylib.bollinger_bands` (standard 20-period 2-std bands on `close`); `ta.SMA` (only over the dead `bsharp` column — fenced dead); `ta.MACD` / `ta.STOCHF` / `ta.ADX` (computed, never read by any order line — fenced dead). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no hyperopt parameter (`IntParameter`/`BooleanParameter`/`CategoricalParameter`/`DecimalParameter` zero hits), no informative-pair call in the file.
- Full-file token census (verified over the 304 lines this cycle, comments stripped for the live-code counts): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` in live code (the single pump-and-dump volume guard is a commented-out alternative, fenced — the live rule is pure OHLC/oscillator state); 0 `cross` edge calls (no `crossed_above`/`crossed_below` anywhere — both legs are persistent level/shape states, never one-bar edges); 0 negative `shift(-` (every offset is a causal non-negative lag — `.shift()` / `.shift(1)` … `.shift(8)` only); 1 `stoploss` attribute (`-0.05`) and 1 single-rung `minimal_roi` ladder as the only risk legs; 0 shipped `trailing` attribute; 0 `startup_candle_count` (the record's 250-bar floor is a predeclared researcher pin, never a file semantic); 0 `order_types` / 0 `order_time_in_force` / 0 `funding` / 0 `mark_price` / 0 `leverage` (no economics beyond ROI/stop); 0 `pyramid` / 0 `position_adjustment` / 0 `cooldown` / 0 `max_open_trades` in code (the position pin below is a predeclared researcher rule, never a file semantic); 0 `resample` / 0 `informative` / 0 `request` / 0 `security`; 0 `ffill` / 0 `fillna` / 0 `interpolate` / 0 `dropna`; 0 `hyperopt` / 0 `*Parameter`; 0 `print(`; 1 `enter_long = 1` / 1 `exit_long = 1`. `Dict`, `List`, `reduce`, and `numpy` are imported and never called — dead imports, fenced as plumbing with no gate effect. The only live division is the composite's constant `/ 3` (never zero); the `bpercent`/`bsharp` divisions live in dead columns (computed, never gated — pandas yields inf/NaN there without raising, fenced as no gate effect).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Freqtrade deployment. The source pins the `5m` frame, the uptrend-gated three-arm entry, the three-arm smoothed-composite exit, the single 10% ROI rung, the −5% stop, and the long-only stance — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the file names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close market fills, plus a predeclared co-print rule (a bar printing both legs closes first and takes no new entry on the same bar — the Signal mutual-exclusion analysis shows co-prints are not arithmetically excluded, so priority is pinned here rather than left to the reviewer); (3) single-unit position pin with hold-no-op semantics plus a 250-bar researcher warmup pin (the file carries no position reference and no length guard — disclosed, never presented as source-native behaviour); (4) framework-default execution semantics pinned as derived behaviour (`can_short` defaults False → long-only, `use_exit_signal` defaults True → signal exits enabled, `exit_profit_only` defaults False → exits fire even at a loss, `ignore_roi_if_entry_signal` defaults False with zero entry-bar distance so no entry-bar ROI co-fire — disclosed, never presented as file literals); (5) the source's absent sizing/costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-21): working-tree filename/content search for `smoothoperator`, `smooth-operator`, `mfi_rsi_cci`, and `eight_green` returns zero strategy records — no record in the pool cites this source file or trades its composite. The pool's two green-streak neighbours are fenced as different constructions in Negative evidence (a 1h red-green reversal with fixed-RR exits; a 1d consistency-winner book — neither gates entries on a V-bottom/oversold composite nor exits on a TEMA-smoothed peak). The closest oscillator cousins (`freqtrade-cmcwinner` 15m CCI+MFI+CMO triple-oversold state, `freqtrade-macd-cci-dip-state`, `freqtrade-bband-rsi-dip-buy`) are fenced in Negative evidence 7. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a V-bottom/oversold-composite system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code and docstring print: buy a bar that ticks up while printing either a lopsided V-bottom (five descending `average` prints reversing on the decision bar, with the prior low under the 20-bar mid-band and washed-out prior CCI/RSI) or a deep/extreme oversold conjunction (sub-mid low with CCI under −200/−150 and RSI/MFI washed out); sell a bar where the triple-smoothed composite crests over 100 and rolls over, or nine straight green bodies print, or CCI over 200 meets RSI over 70. A single 10% ROI rung and a fixed −5% stoploss backstop every position. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

V-bottom dip machine with a smoothed-exhaustion exit, long-only. Unlike single-threshold dip buyers that fire on one oscillator print, the entry first demands an uptick on the decision bar and only then selects among a shape arm (the V must sit under a slow tape — prior low under the 20-bar mid-band) and two washout arms of increasing severity — so a dip without a shape or without genuine oscillator depression prints nothing, and a deeply oversold bar that still ticks down is held for the next bar. Unlike stop/trailing exits, the position exits through three agreeing-on-exhaustion states: the composite peak (triple-EMA smoothing plus TEMA — slow by construction, sits ~one stop behind the top per the file's own comment), the nine-green run (long sideways climbs exited before the dump, per the file's comment), and the raw overbought conjunction for pumped bars. The 10% rung and −5% stop are the only hard accounting legs — preserved verbatim, disclosed, never re-tuned into a livelier ladder.

## Signal

Exact rule as pinned (any other periods, weights, thresholds, strictness, arm combination, risk rung, fill, frame, book, or leg is a different, unpinned rule). All identifiers below are the program's own; TA-Lib default periods apply wherever the file passes none (MFI 14, ADX 14 — library defaults, disclosed, never overridden in the file):

```text
cci[t]     = TA-Lib CCI(high, low, close, 20)
rsi[t]     = TA-Lib RSI(close, 14)
mfi[t]     = TA-Lib MFI(high, low, close, volume, 14)
mfi_s[t]   = TA-Lib EMA(mfi_series, 11)
cci_s[t]   = TA-Lib EMA(cci_series, 11)
rsi_s[t]   = TA-Lib EMA(rsi_series, 11)
composite[t] = (rsi_s[t] * 1.125 + mfi_s[t] * 1.125 + cci_s[t]) / 3
smooth[t]  = TA-Lib TEMA(composite_series, 21)
bbmid[t]   = 20-bar 2-std Bollinger mid of close
avg[t]     = (close[t] + open[t] + high[t] + low[t]) / 4
uptrend[t] = close[t] > close[t-1]
arm1 = (avg[t-5] > avg[t-4]) & (avg[t-4] > avg[t-3]) & (avg[t-3] > avg[t-2])
     & (avg[t-2] > avg[t-1]) & (avg[t-1] < avg[t])
     & (low[t-1] < bbmid[t]) & (cci[t-1] < -100) & (rsi[t-1] < 30)
arm2 = (low[t] < bbmid[t]) & (cci[t] < -200) & (rsi[t] < 30) & (mfi[t] < 30)
arm3 = (mfi[t] < 10) & (cci[t] < -150) & (rsi[t] < mfi[t])
entry    = uptrend[t] & (arm1 | arm2 | arm3)                    // enter_long = 1, persistent state
peak     = (smooth[t] > 100) & (smooth[t-1] > smooth[t])
         & (smooth[t-2] < smooth[t-1]) & (smooth[t-3] < smooth[t-2])
eight    = 9 consecutive green bodies, bars t-8 .. t (open < close each)
overbought = (cci[t] > 200) & (rsi[t] > 70)
exit_sig = peak | eight | overbought                           // exit_long = 1, persistent state
risk     = single take-profit rung {"0": 0.10} (10% by position age in minutes);
           fixed stop at -5% (stoploss -0.05)
floor    = leading-window bars: rolling NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on any bar printing the uptrend-gated entry state, `direction` long-only; `exit_long=1` on any bar printing any of the three exit arms. Both legs are STATE prints in construction (each persists while its levels hold — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code). A positioned book treats further entry bars as hold-no-ops under the position pin below.
- Exact boundaries (pinned semantics): every comparison in both legs is strict (`<`, `>`) — a bar sitting exactly on any threshold (CCI exactly −100/−200/−150/200, RSI exactly 30/70, MFI exactly 30/10, smooth exactly 100, flat close, doji body) fires nothing on the touched leg. Strictness preserved throughout — disclosed, not smoothed.
- Co-print rule (predeclared researcher pin, not arithmetically excluded): entry and signal-exit CAN co-print in principle (no pairing of legs is jointly unsatisfiable — e.g. a V-bottom arm against a rolling composite peak), so a bar printing both closes the unit flat on the exit leg first and takes no new entry on the same bar (exit priority, no same-bar re-entry). ROI/stop cannot co-fire with entry on the entry bar (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere, and the framework default `can_short = False` applies (disclosed default, never a file literal) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the three-arm signal exit, the single 10% ROI rung, and the −5% stop are the complete position-closing set (`use_exit_signal = True` and `exit_profit_only = False` framework defaults apply — exits fire even at a loss; `ignore_roi_if_entry_signal = False` default applies with zero entry-bar distance; disclosed defaults, never file literals). The ROI clock is minutes-held per the Freqtrade `minimal_roi` time-key convention (`"0"`), preserved verbatim. No trailing (no attribute ships — only a code comment musing about one, never a leg), no time exit, no breakeven move — explicitly none further, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying uptrend-gated bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`open` inside `average` and the green-body helper, `high`/`low` inside `average`/CCI/MFI/BB paths, `close` everywhere) with fixed non-negative offsets (no forward reference) — the decision bar's own forming values are never read. No volume read in any live leg, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, `ffill`/`fillna`, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `open`/`high`/`low`/`close` only (helper green-body run and `average` read `open`; CCI/MFI/BB paths read `high`/`low`; everything reads `close`). No bar `volume` read in any live leg, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar's causal past only (`.shift()` / `.shift(1)` … `.shift(8)`); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 250 five-minute bars held flat (~21 hours). Covers the 200-bar SMA seed (longest structural lookback; the SMA column itself is dead but the floor is set off the file's deepest construction), the TEMA-21-over-EMA-11 smoothing stack, the 20-bar CCI/BB seeds, and the 8-bar shift chains with margin. The file ships no `startup_candle_count` — quoted absence, never filled in from elsewhere. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced BbandRsi, AwesomeMacd, EMASkipPump, ADXMomentum, CMCWinner, ASDTSRockwell, MACDStrategy-state, BinHV27, MACDStrategy-crossed, Strategy002, and Strategy004 siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, the three-arm signal exit, and the ROI/stop legs are all bar-close-evaluated; the Signal co-print rule fixes the one ordering the file leaves open, and any bar co-printing a signal exit with an ROI/stop leg closes the full unit flat either way, so no intrabar ordering assumption is needed.
- Interval precedent (disclosed, not assumed): `5m` is an already-admitted interval on `main` via the EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, BinHV27, Strategy002, and Strategy004 records — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its single ROI rung and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the uptrend-gated entry opens the full unit on a flat book; any signal arm, the ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying uptrend-gated bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (304 lines: the CCI/RSI/MFI/EMA/TEMA/BB indicator block, the `average` helper, the uptrend-gated three-arm entry, the three-arm smoothed-composite exit, the `StrategyHelper` pattern class, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `SmoothOperator(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling/TA-Lib NaNs compare false (no early entry, no early exit). The 250-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: every leg is strict — a bar sitting exactly on any threshold (including a doji body for the green run, smooth exactly 100, flat close for the uptrend conjunct) fires nothing on the touched leg. Strictness preserved throughout — disclosed, not smoothed.
3. Co-print priority fenced (pinned, not proved): unlike records with arithmetically impossible co-prints, this file's legs can co-print in principle, so exit-priority with no same-bar re-entry is predeclared in Signal — a reviewer must not substitute entry-first or same-bar reversal semantics.
4. Zero-division fenced: the sole live division is the composite's constant `/ 3`. The `bpercent`/`bsharp` divisions sit in dead columns (computed, never gated — pandas yields inf/NaN without raising, with no gate effect). No guarded division is involved in any order-gating line — disclosed, not repaired.
5. Dead-code plumbing fenced: `Dict`, `List`, `reduce`, `numpy` are imported and never called; `adx`, `macd/macdsignal/macdhist`, `fastk/fastd`, `ema_high/ema_close/ema_low`, `entry_bb_*`, `bb_lowerband/bb_upperband`, `bpercent/bsharp*`, `sma_slow/sma_medium/sma_fast`, `candle_size` are computed and never read by any order line; `seven_green_candles`, `eight_red_candles`, `four_green_one_red_candle`, `four_red_one_green_candle` are never called — this record never conditions on any of them and no reviewer repair may promote any of them into a leg. The second `bollinger_bands(close, 20, 2)` block overwrites the first with identical parameters — idempotent, fenced as written.
6. Comment-alternative fence: the commented-out volume pump-guard, MACD legs, 3-tick spike legs, hammer-pattern legs, and bottom-curve leg are comments, never code — the live rule is exactly the three live arms plus the uptrend conjunct. Coded legs govern; comments never narrow or widen them. The `DO NOT USE` header and `playground` comments are author cautions, not gate facts — this record claims no live suitability either way.
7. Cousin records fenced as different constructions (none trades an uptrend-gated V-bottom/oversold-composite entry with a TEMA-smoothed peak/nine-green/overbought exit on `5m`): the admitted `freqtrade-cmcwinner` pool-mate trades a persistent CCI+MFI+CMO triple-oversold state (every qualifying bar, threshold-state — never a V shape, never a smoothed composite, never a peak exit, `15m`); the admitted `freqtrade-macd-cci-dip-state` pool-mate trades MACD-polarity-plus-CCI state; the admitted `freqtrade-bband-rsi-dip-buy` pool-mate trades an RSI dip with BB penetration; the pool `1-3-1-red-green-candle-reversal` record trades a red-green reversal with fixed-RR exits (entry streak, `1h` — here the streak is an exit arm, never the entry); the pool `grinblatt-moskowitz-2004-consistency` record trades a daily consistency book (never an oscillator composite). Not a threshold re-tuning of any of them: moving any period, weight, threshold, strictness, or arm, converting any state to an edge, or changing the ROI rung, the stop, or the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `user_data/strategies/*.py` sibling is a separate pin — its constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT market choice, the same-bar-close fills with the exit-priority co-print pin, the single-unit/no-add/no-cooldown position pin, the 250-bar warmup floor (the file ships none), the framework-default readings (`can_short=False`, `use_exit_signal=True`, `exit_profit_only=False`, `ignore_roi_if_entry_signal=False`, per-completed-bar evaluation), the TA-Lib default-period readings (MFI 14 — library default, never a file literal), and house sizing/costs — all predeclared above. The `5m` frame, the eleven-live-column indicator block, the uptrend conjunct, the three-arm entry, the three-arm exit, the single 10% ROI rung with the −5% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: uptrend conjunct / all three entry arms with all literals and strictness / composite weights (1.125/1.125/1, /3) / TEMA-21 peak arms / nine-green arm / overbought arm / single 10% ROI rung / −5% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills with exit-priority are frozen.

- F1 — Uptrend-conjunct relevance: dropping the `close > close.shift()` conjunct (washout arms alone, same exit/risk) must not improve net expectancy; fail ⇒ the uptick timing adds nothing over the bare washout states.
- F2 — Peak-exit relevance: dropping the composite-peak arm (nine-green plus overbought exits only, same entry/risk) must not materially change round-trip outcomes; fail ⇒ the smoothed-peak arm carries weight beyond decoration.
- F3 — Risk-leg relevance: removing the ROI rung/stop pair (signal-only exits) must not improve net expectancy; fail ⇒ the 10% rung plus −5% backstop adds nothing over the bare three-arm exit machine.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed by any live leg, so no venue volume-definition dependence. Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- The `5m` frame rides existing admission precedent (EMASkipPump, CombinedBinHAndCluc, ASDTSRockwell, MACDStrategy-state, MACDStrategy-crossed, BinHV27, Strategy002, Strategy004 `5m`) — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market that never prints an exit arm is held until the 10% rung or the −5% stop; a market that prints repeated entry states with no exit prints repeated hold-no-ops with no flat state to rest in. There is no decay, chop, trend-loss, trailing, breakeven, or further time exit — disclosed, not repaired.
- TA-Lib indicator internals (EMA/TEMA seeding, default-period handling, CCI/MFI arithmetic) and the `qtpylib.bollinger_bands` call live in libraries outside the pinned file — pinned by call with explicit periods 20/14/11/21, not re-derived; exact reproduction inherits those libraries' seeding alongside the 250-bar floor.
- The file's `DO NOT USE` header, `playground` columns, commented-out alternative legs, and dead helpers are fenced in Negative evidence — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothOperator.py
- https://github.com/freqtrade/freqtrade-strategies
