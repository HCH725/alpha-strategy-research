---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade BinHV27 RSI-ADX-DI regime-state long-flat on BTCUSDT 5m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BinHV27.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade BinHV27 RSI-ADX-DI regime-state long-flat on BTCUSDT 5m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-emaskippump`, `freqtrade-simple-macd-bb-rsi`, `freqtrade-cofibit`, `freqtrade-strategy005`, `freqtrade-universalmacd`, and `freqtrade-swinghightosky` records at this same pin — this record pins ONLY the BinHV27 literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` twice during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/BinHV27.py`.
- GitHub blob SHA at the pinned commit: `0c205b558dc5b9d1b83525fa4c3f754c7cb36885`, size 5879 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 5879 bytes, 137 lines, SHA-256 `e94ea092f9d277f29ce593f5adc1d9efffb846c27f1c1abfa51c57f1c53257b5`, identical to the GitHub blob (`git hash-object` reproduces `0c205b55…cb36885`) — the entire file was retrieved and inspected.
- Registration: the file defines class `BinHV27(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/*.py` sibling is a different pin with different constants.
- The file's own words (quoted for gate evidence, never extended): docstring `strategy sponsored by user BinH from slack`; `timeframe = '5m'`; `minimal_roi = { "0": 1 }`; `stoploss = -0.50`; indicator block `ta.RSI(dataframe, timeperiod=5)`, `ta.EMA(rsiframe, timeperiod=5)`, `ta.ADX(dataframe)`, `ta.MINUS_DI(dataframe)`, `ta.EMA(minusdiframe, timeperiod=25)`, `ta.PLUS_DI(dataframe)`, `ta.EMA(plusdiframe, timeperiod=5)`, `ta.EMA(dataframe, timeperiod=60)`, `ta.EMA(dataframe, timeperiod=120)`, `ta.SMA(dataframe, timeperiod=120)`, `ta.SMA(dataframe, timeperiod=240)` — every call wrapped in `numpy.nan_to_num`, disclosed below; entry common prefix `slowsma.gt(0)`, `close.lt(highsma)`, `close.lt(lowsma)`, `minusdi.gt(minusdiema)`, `rsi.ge(rsi.shift())` plus a four-arm OR (`adx.gt(25|30|35)`, `bigdown`/`bigup`, `emarsi.le(20|25)` — see Signal); exit is a five-arm OR over `preparechangetrendconfirm` / `continueup` / `close.gt(lowsma|highsma)` / `highsma.gt(0)` / `slowsma.gt(0)` / `emarsi.ge(75|80)` / `adx.gt(30)` / `minusdi.lt(plusdi)` / `slowingdown` — see Signal. No `trailing`, no `startup_candle_count`, no `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `order_types` mapping ships anywhere — the framework defaults below are disclosed as derived behaviour, never as file literals. The file ships no sample, window, trade count, or cost basis.
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.RSI` (TA-Lib RSI over default `close`, explicit period 5); `ta.EMA` (TA-Lib EMA; explicit periods 5/25/60/120 over the stated inputs); `ta.SMA` (TA-Lib SMA over default `close`, explicit periods 120/240); `ta.ADX` / `ta.MINUS_DI` / `ta.PLUS_DI` (TA-Lib directional system over `high`/`low`/`close` with default period 14 — no override in the file, disclosed). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no `fillna`/`ffill`, no hyperopt parameter of any kind.
- Full-file token census (verified over the 137 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume read of any kind — the rule is pure price/oscillator state); 0 `cross` (no `crossed_above`/`crossed_below` edge anywhere — both legs are persistent level states, never one-bar edges); 0 `resample` / 0 `informative` / 0 `request` / 0 `security(` (single-frame, no external feed); 0 `trailing` / 0 `startup_candle` / 0 `can_short` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `process_only_new_candles` / 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` (all such execution/position/economic semantics are predeclared researcher pins below, never file semantics); 0 `position_adjust` / 0 `max_open_trades` / 0 `cooldown` / 0 `pyramid` / 0 `position_size` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `hyperopt` / 0 `IntParameter` / 0 `DecimalParameter` / 0 `CategoricalParameter` / 0 `BooleanParameter` (no tuning scaffolding — every constant is a frozen literal); 0 `ffill` / 0 `fillna` / 0 `interpolate` / 0 `dropna` (seeds are handled by `nan_to_num`, disclosed); 0 `merge_informative`; 0 negative `shift(-` (every offset is a causal non-negative lag — `shift()` / `shift(2)` only); 5 `ta.EMA` / 2 `ta.SMA` / 1 `ta.RSI` / 1 `ta.ADX` / 1 `ta.MINUS_DI` / 1 `ta.PLUS_DI` (the complete indicator set); 11 `nan_to_num` (one per indicator column); 1 `enter_long` / 1 `exit_long` / 0 `enter_short` / 0 `exit_short`; 0 `print(`. `Dict`, `List`, `reduce`, `DatetimeIndex`, `merge`, and the duplicated `qtpylib` import are imported and never called — dead imports, fenced as plumbing with no gate effect. `plusdiema` is computed and never read by any order line — fenced as a dead column (see Negative evidence).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (all shifts non-negative, no resample/merge, no repainting primitive, no multi-timeframe feed, no external package — no repair site exists). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` (the source names no market); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-cooldown position pin plus a 300-bar researcher warmup floor (covers the 240-bar SMA seed and the two-step shift chains with margin); (4) framework-default execution semantics pinned as derived behaviour (`can_short` defaults False → long-only, `use_exit_signal` defaults True → signal exits enabled, ROI/stop legs bar-close-evaluated — disclosed, never presented as file literals); (5) the house cost/capital overlay replaces the absent source economics. Every period, every threshold, the four-arm entry, the five-arm exit, the ROI rung, and the stop are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `BinHV27`, `binhv27`, and `minusdiema` returns zero strategy records — the single pool-wide `emarsi` hit is the unrelated Forven EMA-RSI pullback-reclaim record (EMA12/34 trend plus RSI 45-reclaim/62-rollover one-bar edges on SOLUSDT 1h — a different source, mechanism, frame, and market, fenced in Negative evidence). The admitted `freqtrade-combined-binh-cluc` sibling record explicitly names only `BinHV45.py` and `ClucMay72018.py` as its neighbour pins — BinHV27 is a third, distinct file. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount) trades an RSI/ADX/DI/SMA regime-state system. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims no behavioural channel beyond its code: buy the bar parked under both slow EMA rails (`close < EMA120`, `close < EMA60`) with rising-or-flat RSI(5), bearish-directional permission (`minusdi > minusdiema(25)`), and one of four ADX/regime arms (weak-trend-rejecting washout, continuation-up washout, strong-trend breakout, continuation-up breakout — all demanding depressed EMARSI ≤ 20/25); stand aside to flat on any of five reclaim arms (SMA reclaim, EMARSI-or-SMA reclaim, ADX-confirmed EMARSI reclaim, trend-confirm-plus-deceleration EMARSI reclaim, trend-confirm directional-flip reclaim). A single 100% ROI rung (effectively no take-profit) and a −50% stop backstop every position. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Research interpretation

Four-regime dip buyer, long-only, exited by reclaim states. Unlike single-threshold dip buyers that fire on one oscillator print, the entry first demands a uniform tape posture (price under both slow EMA rails, RSI not falling, directional system bearish versus its own average) and only then selects among four ADX-and-SMA-regime arms — so a dip in a dead-ADX tape prints nothing, and a dip whose EMARSI is not washed out prints nothing either. Unlike stop/trailing exits, the position exits through five reclaim states: the signal legs do the work (the 100% ROI rung is unreachable on 5m crypto tape and the −50% stop is a catastrophe backstop), so round-trips close on tape repair, not on profit targets — disclosed, never repaired into a livelier ROI ladder.

## Signal

Exact rule as pinned (any other period, threshold, strictness, arm combination, risk rung, fill, frame, book, or leg is a different, unpinned rule). All identifiers below are the program's own; `lowsma`/`highsma` are the file's own (mis)names for EMA(60)/EMA(120) — fenced as written, never renamed:

```text
rsi[t]        = nan_to_num(RSI(close, 5))[t]
emarsi[t]     = nan_to_num(EMA(rsi_series, 5))[t]
adx[t]        = nan_to_num(ADX(hlc, 14))[t]            // TA-Lib default period
minusdi[t]    = nan_to_num(MINUS_DI(hlc, 14))[t]       // TA-Lib default period
minusdiema[t] = nan_to_num(EMA(minusdi_series, 25))[t]
plusdi[t]     = nan_to_num(PLUS_DI(hlc, 14))[t]        // TA-Lib default period
lowsma[t]     = nan_to_num(EMA(close, 60))[t]          // file's own name — EMA, not SMA
highsma[t]    = nan_to_num(EMA(close, 120))[t]         // file's own name — EMA, not SMA
fastsma[t]    = nan_to_num(SMA(close, 120))[t]
slowsma[t]    = nan_to_num(SMA(close, 240))[t]
bigup[t]      = (fastsma[t] > slowsma[t]) & ((fastsma[t]-slowsma[t]) > close[t]/300)
bigdown[t]    = ~bigup[t]
trend[t]      = fastsma[t] - slowsma[t]
prep[t]       = trend[t] > trend[t-1]
prepconf[t]   = prep[t] & (trend[t-1] > trend[t-2])
contup[t]     = (slowsma[t] > slowsma[t-1]) & (slowsma[t-1] > slowsma[t-2])
delta[t]      = fastsma[t] - fastsma[t-1]
slowdown[t]   = delta[t] < delta[t-1]
entry = (slowsma[t] > 0) & (close[t] < highsma[t]) & (close[t] < lowsma[t])
      & (minusdi[t] > minusdiema[t]) & (rsi[t] >= rsi[t-1])
      & ( (~prep[t] & ~contup[t] & (adx[t] > 25) & bigdown[t] & (emarsi[t] <= 20))
        | (~prep[t] &  contup[t] & (adx[t] > 30) & bigdown[t] & (emarsi[t] <= 20))
        | (~contup[t] & (adx[t] > 35) & bigup[t] & (emarsi[t] <= 20))
        | ( contup[t] & (adx[t] > 30) & bigup[t] & (emarsi[t] <= 25)) )   // enter_long = 1
exit_sig = ( (~prepconf[t] & ~contup[t] & (close[t] > lowsma[t] | close[t] > highsma[t]) & (highsma[t] > 0) & bigdown[t])
           | (~prepconf[t] & ~contup[t] & (close[t] > highsma[t]) & (highsma[t] > 0) & ((emarsi[t] >= 75) | (close[t] > slowsma[t])) & bigdown[t])
           | (~prepconf[t] & (close[t] > highsma[t]) & (highsma[t] > 0) & (adx[t] > 30) & (emarsi[t] >= 80) & bigup[t])
           | ( prepconf[t] & ~contup[t] & slowdown[t] & (emarsi[t] >= 75) & (slowsma[t] > 0))
           | ( prepconf[t] & (minusdi[t] < plusdi[t]) & (close[t] > lowsma[t]) & (slowsma[t] > 0)) )  // exit_long = 1
risk = single take-profit rung {"0": 1} (100% — effectively disabled, explicit);
       fixed stop at -50% (stoploss -0.50); no trailing of any kind
guard = nan_to_num seeds read as 0 (see Required data)
```

- Exact boundaries (pinned semantics): strict `.gt`/`.lt` throughout except three non-strict legs exactly as coded — `rsi[t] >= rsi[t-1]` (flat RSI still passes), `emarsi <= 20/25` (exact 20/25 still enters), `emarsi >= 75/80` (exact 75/80 still exits). Strict legs fire nothing on equality (close exactly on a rail, ADX exactly on 25/30/35, EMARSI-adjacent ties hold flat) — disclosed, not smoothed.
- Trade events: `enter_long=1` on any bar printing the entry state, `direction` long-only; `exit_long=1` on any bar printing any of the five reclaim arms. Both legs are STATE prints in construction (each persists while its levels hold — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code).
- Mutual-exclusion proof (no tie-break pin required): the entry prefix demands `close < lowsma AND close < highsma` (both strict), while exit arms 1/2/3/5 each demand `close > lowsma OR close > highsma` (strict) — jointly unsatisfiable with the prefix on one bar, including equality (strict legs fire nothing on ties). The remaining exit arm 4 demands `emarsi >= 75` while every entry arm demands `emarsi <= 25` — disjoint by 50 points. No single bar satisfies both legs; the reviewer is never asked to invent an ordering. ROI/stop legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere and `can_short` is absent (Freqtrade default False) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the five-arm signal exit, the single 100% ROI rung, and the −50% stop are the complete position-closing set. No trailing, no breakeven, no time exit — explicitly none, not invented. `use_exit_signal` is absent (Freqtrade default True — signal exits enabled as coded, disclosed as derived behaviour).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying regime bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`high`/`low`/`close` for ADX/DI paths, `close` for RSI/EMA/SMA paths) with fixed non-negative window offsets (no forward reference) — no volume/funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, `ffill`/`fillna`, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `5m` bars of BTCUSDT: `high`/`low`/`close` for the ADX/MINUS_DI/PLUS_DI paths; `close` for the RSI/EMA/SMA paths. No `volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `5m` (source-native — the file prints `timeframe = '5m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only (`shift()` / `shift(2)`); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher floor, disclosed): the record-rule floor holds 300 five-minute bars flat (~25 hours). Covers the 240-bar SMA seed, the two-step `shift(2)` chains built on it (242 bars effective), and all EMA/RSI/ADX/DI construction with margin. Coded behaviour underneath: `nan_to_num` maps every pre-seed NaN to exactly 0.0 — so pre-seed `slowsma`/`highsma` read 0, failing the `> 0` guards on both legs (entries blocked by `slowsma.gt(0)`, exits blocked by `highsma.gt(0)`/`slowsma.gt(0)` on every arm that could otherwise print); no `fillna`/`ffill` exists to smear seeds forward. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close market fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced `5m` siblings use. No maker-touch, queue, or intrabar-path-dependent fill: entry, signal-exit, and ROI/stop legs are all bar-close-evaluated; entry/exit co-prints are arithmetically impossible (see Signal), leaving no invented engine ordering.
- Interval precedent (exact, disclosed): exact-`5m` PASS records already sit on `main` at this same repository pin (the admitted CombinedBinHAndCluc dual-leg record and the EMASkipPump record — both `5m` Freqtrade-sourced long-flat) — this record rides the same specified single-frame completed-bar `5m` Binance candle path, not an assumed one. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the same specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding. The price-only feed is a strict subset of that path's candle (no volume leg exists here at all).
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI rung and stop percentage are preserved verbatim as the risk legs while sizing and costs ride the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) with pinned house cost assumptions (fees plus historical funding; the source declares no funding treatment at all), under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the regime entry opens the full unit on a flat book; any signal arm, the ROI rung, or the stop closes it in full; re-entry after an exit needs only the next qualifying regime bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (137 lines: the eleven-column `nan_to_num` indicator block, the derived regime booleans, the four-arm entry, the five-arm exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `BinHV27(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: `nan_to_num` maps pre-seed NaNs to 0.0 — entries blocked by `slowsma > 0`, exits blocked by `highsma > 0` / `slowsma > 0` on every arm that could otherwise print; no `fillna`/`ffill` smears seeds forward. The 300-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `.gt`/`.lt` fires nothing on equality (close exactly on a rail, ADX exactly on 25/30/35 holds flat); the three non-strict legs (`rsi >= prior`, `emarsi <= 20/25`, `emarsi >= 75/80`) fire on equality exactly as coded — disclosed, not smoothed.
3. Co-print arithmetic fenced (impossible, proved — not pinned): entry prefix (`close` under both EMA rails) contradicts exit arms 1/2/3/5 (`close` over either rail); exit arm 4 (`emarsi >= 75`) contradicts every entry arm (`emarsi <= 25`). No bar prints both legs; no ordering invented.
4. Zero-variance fenced: flat tape zeroes every oscillator via `nan_to_num`-adjacent library seeds (RSI prints midscale/0, ADX prints 0 — failing the `> 25` arm floor; both sides of `minusdi > minusdiema` read 0 — strict `>` fails). No division exists in the gating path except `close/300` (denominator is a price, never zero on live tape) — disclosed, not repaired.
5. Dead-code plumbing fenced: `plusdiema` (EMA(5) over PLUS_DI) is computed and never read by any order line; `Dict`, `List`, `reduce`, `DatetimeIndex`, `merge`, and the duplicated `qtpylib` import are never called — this record never conditions on them and no reviewer repair may promote any of them into a leg. The `lowsma`/`highsma` names are file-literal misnomers for EMA(60)/EMA(120) — fenced as written, never renamed.
6. Cousin records fenced as different constructions (none trades a four-arm RSI/ADX/DI/SMA regime entry with a five-arm reclaim exit on `5m`): the admitted CombinedBinHAndCluc sibling trades a dual-leg BB-penetration entry (BinHV45 BB(40) leg OR Cluc EMA50/BB(20)-discount leg) with a BB-mid profit-gated exit — penetration-plus-body-guards, never ADX/DI regime arms; the admitted EMASkipPump sibling trades an EMA-stack dip with a volume veto (different primitives, different exit); the admitted MACD/CCI/AO/SMA siblings trade oscillator-cross or cross-edge systems (never level-state regime arms); the pool's lone `emarsi` neighbour is the Forven EMA-RSI pullback record (EMA12/34 trend plus one-bar RSI 45-reclaim/62-rollover edges on SOLUSDT 1h — edge primitives, different source, frame, and market). Not a threshold re-tuning of any of them: changing any period, threshold, strictness, or arm would each be a different, unpinned rule — none is admitted here.
7. Sibling-file fence: every other `user_data/strategies/*.py` sibling is a separate pin — its constants must never be substituted into this record.
8. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 300-bar warmup floor, derived `can_short=False`/`use_exit_signal=True`/market-fill execution semantics, house sizing/costs) — all predeclared above. The `5m` frame, the eleven-column indicator block, the derived regime booleans, the four-arm entry, the five-arm exit, the 100% ROI rung, the −50% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: regime entry / all eleven periods / all frozen thresholds / five-arm exit / ROI rung / −50% stop / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

- F1 — EMARSI-severity relevance: softening every entry EMARSI leg to `<= 40` (same ADX arms, same exit/risk) must not improve net expectancy; fail ⇒ the ≤ 20/25 washout severity adds nothing over a mild-soft filter.
- F2 — Signal-exit relevance: dropping the five-arm signal exit entirely (ROI/stop-only exits, same entry) must not materially change round-trip outcomes; fail ⇒ the reclaim arms carry weight beyond decoration (expectation: they carry nearly all of it, the 100% rung being unreachable).
- F3 — Directional-permission relevance: dropping the `minusdi > minusdiema` entry conjunct (pure price-plus-RSI/ADX regime entry, same exit/risk) must not improve net expectancy; fail ⇒ the bearish-directional permission adds nothing over the bare regime state.

## Crypto portability

BTCUSDT Binance perpetual `5m` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only the `high`/`low`/`close` candle fields are read (venue definition differences move only oscillator inputs, disclosed). Funding is declared nowhere in the source and modeled only downstream by house assumptions.

## Limitations

- TA-Lib RSI/EMA/SMA/ADX/MINUS_DI/PLUS_DI internals live in their library outside the pinned file — pinned by call with explicit periods (defaults 14 disclosed where the file passes none), not re-derived; exact reproduction inherits that module's seeding and rolling semantics alongside the file-local `nan_to_num` wiring, under the disclosed 300-bar floor.
- The 100% ROI rung is effectively unreachable on 5m crypto tape and the −50% stop is a catastrophe backstop — round-trips close overwhelmingly via the five signal arms. This record repairs nothing: the effective behaviour is fully explicit and complete, and any livelier ROI ladder would be a different, unpinned rule no reviewer may invent.
- No trailing, no breakeven, no time exit, no short leg, no cooldown — all explicitly absent, never to be added by repair.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close convention; this record makes no claim about any live-order behaviour.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/BinHV27.py
- https://github.com/freqtrade/freqtrade-strategies
