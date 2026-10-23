---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade SmoothScalp StochF-oversold-cross ADX-MFI-CCI-gated long-flat on BTCUSDT 1m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothScalp.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade SmoothScalp StochF-oversold-cross ADX-MFI-CCI-gated long-flat on BTCUSDT 1m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official first-party Freqtrade strategy collection).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/SmoothScalp.py`.
- GitHub blob SHA at the pinned commit: `9d0718b04aad27e8bc989b2362a22934485e9520`, size 3861 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3861 bytes, 102 lines, SHA-256 `e32a8f758d8d57876210d479576e7e415ff924400b8d037bb0f30799cd801a5b`, and `git hash-object` reproduces `9d0718b0…e9520` — the entire file was retrieved and inspected.
- Registration: the file defines class `SmoothScalp(IStrategy)` (the only class in the file). Its docstring idea reads `generating a lot of potentials buys and make tiny profits on each trade` with `we recommend to have at least 60 parallel trades at any time to cover non avoidable losses` — recommendation only, no sample, window, trade count, or cost basis ships anywhere in the 102 lines, and no performance statistics are printed anywhere (unlike the hyperopt-comment siblings in the same directory).
- The file's own words (quoted for gate evidence, never extended): `timeframe = '1m'`; `minimal_roi = { "0": 0.01 }` (single fixed rung); `stoploss = -0.5`; `INTERFACE_VERSION: int = 3`; entry is the seven-way AND of `dataframe['open'] < dataframe['ema_low']`, `dataframe['adx'] > 30`, `dataframe['mfi'] < 30`, `dataframe['fastk'] < 30`, `dataframe['fastd'] < 30`, `qtpylib.crossed_above(dataframe['fastk'], dataframe['fastd'])`, `dataframe['cci'] < -150`; exit is `(dataframe['open'] >= dataframe['ema_high']) | qtpylib.crossed_above(dataframe['fastk'], 70) | qtpylib.crossed_above(dataframe['fastd'], 70)` all AND `dataframe['cci'] > 150`. Indicators: `ta.EMA(dataframe, timeperiod=5, price='high'|'close'|'low')`, `ta.STOCHF(dataframe, 5, 3, 0, 3, 0)`, `ta.ADX(dataframe)`, `ta.CCI(dataframe, timeperiod=20)` then overwritten by `ta.CCI(dataframe)`, `ta.MFI(dataframe)`, `ta.RSI(dataframe, timeperiod=14)`, `ta.MACD(dataframe)`, `qtpylib.bollinger_bands(dataframe['close'], window=20, stds=2)`.
- Framework calls pinned (all resolved against contemporaneous first-party commits, read this cycle): `crossed_above` → `crossed(s1, s2, "above") = (s1[t] > s2[t]) & (s1[t-1] <= s2[t-1])` (`technical@9c6d8fd366ef0ed3e046b32e534bcec9f9479449`, `technical/vendor/qtpylib/indicators.py` lines 227–243), with `int`/`float` scalars broadcast to a constant series (lines 231–232) — so the exit legs `crossed_above(fastk, 70)` / `crossed_above(fastd, 70)` are pinned constant-threshold edges. `IStrategy` at `freqtrade@3d31927` (`freqtrade/strategy/interface.py`, fetched and grepped this cycle): `can_short: bool = False` (line 89), `trailing_stop: bool = False` (line 82), `position_adjustment_enable: bool = False` (line 118), `startup_candle_count: int = 0` (line 128), `process_only_new_candles: bool = True` (line 110); exit-signal gating is `if self.use_exit_signal: if exit_ and not enter:` → `EXIT_SIGNAL` (lines 1469–1471) — the framework itself suppresses an exit on a bar that also prints entry.
- Full-file token census (verified over the 102 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `can_short`; 0 `trailing`; 0 `resample` / 0 `informative` / 0 `merge`; 0 `Parameter` (no hyperopt search space anywhere — every constant is a plain literal); 0 `time_limit` / 0 `max_open` / 0 `leverage` / 0 `order_types` / 0 `process_only` / 0 `startup_candle` / 0 `use_exit_signal` / 0 `custom_stoploss`; 1 `crossed_above` in entry (fastk/fastd) + 2 in exit (fastk-70, fastd-70); `macd`/`macdsignal`/`macdhist`/`rsi`/`bb_lowerband`/`bb_upperband`/`bb_middleband`/`ema_close` computed but never referenced by any gating line (fenced, never repaired); `numpy`, `reduce`, `Dict`, `List`, `DatetimeIndex`, `merge` imported and never called (duplicate-import plumbing leftovers — fenced, not repaired).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source backtest. Researcher-declared adaptations are exactly eight, all predeclared here: (1) market pin `BTCUSDT` on Binance spot (the source is pair-agnostic — no symbol, no venue, no `trading_mode` anywhere in the file); (2) `MARKET` same-bar-close fills on completed-bar decisions (`open_order_type = MARKET`; the source sets no `order_types`, so no source fill convention is overridden — the limit-order-book path is scoped out, never invented); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (covers ADX seeding plus edge-lag margin; see Required data); (4) house sizing/capital/costs replacing the absent source economics; (5) bar-close-atomic evaluation of the fixed stop, the fixed take-profit, and the signal exit with the explicit precedence stop-loss → take-profit → signal exit, at most one net position change per bar (the source evaluates risk intrabar; intrabar sequencing is scoped out, never invented); (6) single-unit, at most one open position, no averaging (against the docstring's 60-parallel-trades recommendation — kept as source context, explicitly not followed; see Limitations); (7) a strategy-specific directional controller that stops the open executor with `keep_position=False` on exit-signal bars (follows the shipped `stop_actions_proposal` override pattern — see Execution assumptions); (8) pinned engine run parameter `trade_cost = 0.0002` (the pinned engine's own default). The `1m` frame, the EMA5-high/low/close, STOCHF(5,3,0,3,0), ADX/MFI/CCI/RSI constructions, all seven entry conjuncts, the full exit disjunction-plus-CCI conjunction, the single 1% take-profit rung, the −50% stop literal, the long-only posture, and the absent trailing/time-exit are source-native and unmodified.

Pre-write dedup (2026-10-23): working-tree content search for `smoothscalp`, `smooth-scalp`, and `smooth_scalp` returns zero strategy records; the exact seven-conjunct entry (open-under-EMA5-low × ADX-30 × MFI-30 × StochF-double-under-30 × fastk/fastd-cross × CCI-150) returns zero records. The pool's nearest cousins are fenced as different constructions in Negative evidence 8. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018, #353 Heracles KCD-ratio) trades a StochF-cross × ADX × MFI × CCI conjunction on `1m`; #353 Heracles pins a different file in the same directory. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the minute where price taps under its own short EMA-low rail (`open < ema_low(5)`) while a trend exists (`ADX > 30`) exactly as the tape reads washed-out on three independent oscillators (`MFI < 30`, StochF `fastk` and `fastd` both under 30, `CCI < −150`) and the fast StochF line turns up through the slow one — and stand aside to flat when the tape reads overbought (`CCI > 150`) with price back above the EMA-high rail or either StochF line crossing up through 70, behind a fixed 1% take-profit and a −50% fixed stop. No behavioural, structural, or risk-premium channel is claimed anywhere in the 102 lines.

### Research interpretation

Washed-out-impulse scalper, long-only, single-position. Unlike bare oversold records (buy every low RSI/CCI print), nothing fires without the fastk/fastd cross edge on the same bar — a deeply oversold tape whose StochF lines have not yet turned buys nothing, and a cross bar whose ADX/MFI/CCI legs fail is gone forever, never re-fires. Unlike level-state records, the trigger is a one-bar edge while the exit is a state-plus-edge disjunction: a merely overbought tape without the rail reclaim or a 70-cross holds the book until the 1% take-profit. The coded consequence is a buyer of edge-fresh, triply-certified washout turns that surrenders on the first overbought confirmation or the fixed take-profit. The −50% stop is economically inert on minute bars (kept verbatim as the file literal, never re-tuned) — the genuine risk exits are the signal exit and the 1% take-profit.

## Signal

Exact rule as pinned (any other lookback, price input, threshold, edge/level choice, stop, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own; framework primitives expand to their pinned contemporaneous definitions:

```text
ema_high[t] = TA-Lib EMA(high, 5); ema_low[t] = TA-Lib EMA(low, 5)   // ema_close computed, unused
fastk/fastd[t] = TA-Lib STOCHF(5, 3, 0, 3, 0)                        // fastk_period 5, fastd_period 3
adx[t]      = TA-Lib ADX(high, low, close, 14)                        // library default lookback
mfi[t]      = TA-Lib MFI(high, low, close, volume, 14)                // library default lookback
cci[t]      = TA-Lib CCI(high, low, close, 14)                        // effective: file writes CCI(20) then overwrites with CCI(14); last write wins
xab(a,b)[t] = (a[t] > b[t]) AND (a[t-1] <= b[t-1])                    // pinned crossed_above, scalar broadcast
entry = (open[t] < ema_low[t]) AND (adx[t] > 30) AND (mfi[t] < 30) AND (fastk[t] < 30) AND (fastd[t] < 30) AND xab(fastk,fastd)[t] AND (cci[t] < -150)   // enter_long = 1
exit_sig = ((open[t] >= ema_high[t]) OR xab(fastk,70)[t] OR xab(fastd,70)[t]) AND (cci[t] > 150)                                                        // exit_long = 1
risk = fixed take-profit 0.01 (single minimal_roi rung {"0": 0.01}); fixed stop -0.50 (stoploss literal); no trailing (file-unset, framework default False); no time exit (none in file)
guard = leading-window bars: NaN comparisons false (see Required data)
```

- Trade events: `enter_long=1` on bars printing the seven-conjunct entry, `direction` long-only; `exit_long=1` on bars printing the exit conjunction. The trigger leg is EDGE-gated (the fastk/fastd cross fires only on its cross bar — a cross bar whose ADX/MFI/CCI/rail legs fail never re-fires; no one-shot latch, no level hold anywhere in code).
- Exact boundaries (pinned semantics): strict `<`/`>`/`>=` as written; the cross legs admit prior-bar `<=` per the pinned expansion — fastk landing exactly on fastd on the current bar fires nothing, while touching from below on the prior bar still arms the edge; `adx` exactly `30`, `mfi` exactly `30`, `fastk`/`fastd` exactly `30`, `cci` exactly `−150`/`150` all fail their strict legs. The `5` / `5,3,0,3,0` / `14` / `30` / `150` / `70` / `0.01` / `0.5` literals are never tuned here.
- Mutual-exclusion proof (no tie-break pin required): entry needs `cci[t] < −150` while exit needs `cci[t] > 150` on the same bar — strictly disjoint regions, so entry and signal-exit never co-print, and the framework-documented collide rule (`exit_ and not enter`, interface.py line 1470) is a backstop that never activates. The reviewer is never asked to invent an ordering.
- Direction: long-only. `can_short` is unset and defaults `False` at the pinned framework commit; zero `enter_short`/`exit_short` tokens ship anywhere — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the exit conjunction, the single 1% take-profit rung, and the −50% fixed stop are the complete position-closing set (effective `use_exit_signal=True` so the defined `exit_long` legs are honored, `exit_profit_only=False` so they fire even at a loss — framework defaults, disclosed as effective pins). No trailing, no time exit, no breakeven — explicitly absent, not invented.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — `position_adjustment_enable` defaults `False` at the pinned framework commit); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying seven-conjunct bar after any exit (cooldown pinned at 60s — one decision bar, see Execution assumptions — explicitly the pin, not invented as zero). Pre-first-signal and pre-warmup bars are flat by record rule.
- Bar-close precedence (predeclared derivation, disclosed): on a positioned book each completed bar evaluates closing legs in fixed order — (1) fixed stop, (2) fixed take-profit, (3) signal exit; entry is evaluated only on a flat book. At most one net position change per bar by construction plus the mutual-exclusion proof.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`open`/`high`/`low`/`close`/`volume`) with fixed non-negative offsets (indicator windows plus one `shift(1)` lag inside each edge — no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. `process_only_new_candles = True` is the file's own framework contract (interface.py line 110).

## Required data

- Completed `1m` bars of BTCUSDT: `open` (rail comparisons), `high`/`low` (EMA rails, ADX, MFI, CCI, STOCHF), `close` (indicator seeds), `volume` (MFI). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (zero `resample`/`informative` tokens — single-frame by construction).
- Single decision timeframe `1m` (source-native — the file prints `timeframe = '1m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 60 one-minute bars held flat. Covers the ~28-bar ADX seeding span, the 14-bar RSI/MFI/CCI seeds, the STOCHF seed, the 5-bar EMA seeds, and the one-bar edge lag with margin. Coded behaviour underneath: TA-Lib seeds print NaN until windowed (every strict NaN comparison false — no leg can fire early). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Spot is a no-funding venue by construction: there is no funding term to model, hence no hypothetical-zero-funding record (see Costs).
- Order timing (derived, disclosed): completed-bar decision with same-bar-close `MARKET` fills — the decision bar's own close, via `open_order_type = MARKET` on the triple-barrier config. The pinned simulator resolves non-limit entry as `start_timestamp = df['timestamp'].min()` with `entry_price = df.loc[start_timestamp, 'close']` (`HCH725/hummingbot@8b0e067`, `position_executor_simulator.py` lines 14–15, 40) — the decision row's own close, no maker-touch, no queue, no intrabar-path-dependent fill. Take-profit is evaluated on the fee-inclusive close-return series (line 45), stop-loss on the completed bar's `low`/`high` against `entry × (1 ∓ sl)` (lines 60–64); intrabar sequencing inside the bar is scoped out under derivation (5) above, never invented.
- Engine path (exact, disclosed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, all files below read line-by-line at that commit this cycle. Each entry creates one `PositionExecutorConfig` (`triple_barrier_config = {take_profit: 0.01, stop_loss: 0.5, time_limit: None, trailing_stop: None}`, `open_order_type: MARKET`, `leverage: 1`) through the shipped `DirectionalTradingControllerBase.get_executor_config` (lines 204–218), which natively builds position executors with the controller's triple-barrier config; single-position state is the shipped `max_executors_per_side = 1` setting (shipped default 2, line 37–42) combined with the shipped active-per-side gate (lines 185–195). Signal exits ride `StopExecutorAction(keep_position=False)` from the strategy-specific controller's `stop_actions_proposal` override — the designated override point (base returns `[]`, lines 197–202) with a shipped override precedent in `MarketMakingControllerBase.stop_actions_proposal`/`executors_to_early_stop` (lines 263–275); a keep-position-False stop books `net_pnl_quote` as `CloseType.EARLY_STOP` realized PnL (`backtesting_engine_base.py` lines 593–595), never touching the position-hold ledger. Naturally terminated TP/SL/TL executors book the same way (lines 428–430) into `_executor_realized_pnl`, which `summarize_results` includes in `net_pnl_quote` (line 624) from the complete run ledger `stopped_executors_info` (lines 337–348, 321–335) — closed positions never vanish from results. No `OrderExecutor`, no DCA/grid executor, no hold conversion exists anywhere on this specified path (only `CloseType.POSITION_HOLD` routes to the hold ledger, line 422 — unreachable here since no executor on this path can print that close type).
- Cost/fee accounting (verified mechanism, not performance): the pinned simulator defines `cumulative_returns = ((1+returns).cumprod()-1) × side − 2 × trade_cost` (line 45) with `cum_fees_quote = 2 × trade_cost × filled` (line 49) — round-trip fees are deducted inside `net_pnl_quote` by construction. A stdlib-plus-pandas isolation check executed the real pinned file with minimal interface doubles this cycle (10 assertions, all passed): TP fires as `TAKE_PROFIT` with `net_pct == gross − 2×trade_cost` exactly (0.01166016 vs 0.01206016 at `trade_cost=0.0002`), SL fires as `STOP_LOSS` on low breach, flat tape closes `TIME_LIMIT`, explicit `time_limit=3600` truncates at exactly 3600.0, and no run prints `POSITION_HOLD`. This is mechanism evidence only — no performance is asserted.
- Data path: decision timeframe `1m` equals backtesting resolution `1m`; `1m` is a supported interval (`candles_base.py` line 33: `"1m": 60`) and the `binance_spot_candles` feed ships at the pinned commit. Row-atomic completed-bar semantics (disclosed): each row is processed as one completed bar — `update_state` prices off `row["close_bt"]` (line 366); REST rows are keyed by kline open time (`binance_spot_candles.py` lines 80–85), so the record's availability pin is that a row's full OHLCV becomes decidable exactly at that row's processing tick, with features computed on completed decision bars only and the backward merge (`prepare_market_data`, lines 466–470) resolving to the exact-timestamp identity mapping in the single-frame case. No HTF merge, no interpolation, no forming-bar read.
- State/handoff (why the 3600s window does not bind here): flat-vs-positioned is read off the exact active-executor list, never the windowed terminated view; the terminated view (`terminated_executors_window`, default 3600s = 60 decision rows) only bounds lookbacks the specified controller never performs beyond one bar. Cooldown is pinned at 60s (one bar; the shipped field requires `gt=0`, line 44) — with the max-1 active gate it can never bind across bars, disclosed. Re-entry needs only the next qualifying entry bar on a flat book.
- Sizing/capital/costs: the source ships no sizing, capital, fee, or margin concept — the 1% rung and −50% stop are preserved verbatim as barrier distances while sizing rides the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated) with the pinned run parameter `trade_cost = 0.0002` (the engine's own `run_backtesting` default, line 224); the live Binance spot taker (0.001) differs and is downstream calibration, never claimed here. Precision rides the engine's real connector trading-rules load (`backtesting_data_provider.py` lines 75–79). `leverage = 1` follows the shipped config's own spot instruction ("Set it to 1 for spot trading", line 52); no short executor is ever created so `position_mode` never takes effect (left at default, explicitly irrelevant). Pin fees/precision downstream; funding is venue-absent on spot, never modeled, never reported as realized.

## Evidence

### Source-reported

The file ships the full construction (102 lines: the indicator block, the seven-conjunct entry, the exit conjunction, the `timeframe`/single-rung-ROI/stop literals, and the `SmoothScalp(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Mechanism-level only (see Execution assumptions): the real pinned `position_executor_simulator.py` was executed under interface doubles on synthetic 1m bars — 10/10 assertions passed (TP/SL/TL close types, exact fee-inclusive net, truncation, no-hold). No performance backtest was run; no returns are claimed.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib rolling seeds print NaN until windowed (every strict NaN comparison false — no early entry, no early exit). The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict current-bar inequalities fire nothing on equality while the pinned edges admit prior-bar `<=`; `adx` exactly `30`, `mfi`/`fastk`/`fastd` exactly `30`, `cci` exactly `−150`/`150` all fail — disclosed, not smoothed.
3. CCI-overwrite fenced (read, not assumed): the file assigns `dataframe['cci'] = ta.CCI(dataframe, timeperiod=20)` and later reassigns `dataframe['cci'] = ta.CCI(dataframe)` (TA-Lib default 14) — last write wins, so both entry and exit read CCI(14). Disclosed, never re-derived as CCI(20).
4. Computed-but-unused columns fenced: `macd`/`macdsignal`/`macdhist`, `rsi(14)`, `bb_lowerband`/`bb_middleband`/`bb_upperband` (written twice — first on `typical_price`, then overwritten on `close` — both unused), `ema_close` — none is read by any gating line. Disclosed, never rewired into the signal.
5. Dead-import plumbing fenced: `numpy`, `reduce`, `Dict`, `List`, `DatetimeIndex`, `merge` imported and never called — no gate effect. Zero `Parameter` spaces, zero fitted values, zero hyperopt imports anywhere — disclosed, never repaired into a signal.
6. Stop-literal paradox fenced: the file prints `stoploss = -0.5` beside a comment musing `should not be below 3% loss` — the literal governs and is preserved verbatim as the 0.5 barrier; the comment is advisory prose, never promoted into the rule. Economically the barrier is near-inert on minute bars; the genuine risk exits are the signal exit and the 1% take-profit — disclosed, not re-tuned.
7. Docstring-concurrency fenced: the `at least 60 parallel trades` recommendation is source context for a multi-slot Freqtrade deployment; the derived executable pins single-position (derivation (6)) because shared-capital multi-slot sizing is unspecified in the file. Disclosed, never presented as source-native behaviour.
8. Cousin records fenced as different constructions (none conjoins an open-under-EMA5-low rail with an ADX-30 trend leg, an MFI-30 leg, a double-under-30 StochF leg, a fastk/fastd cross edge, and a CCI-150 washout leg on `1m` with a single 1% rung and a −50% stop): the admitted `freqtrade-cofibit-stochf-ema-rail-adx-gated` sibling crosses StochF over an EMA rail on `5m` (no MFI/CCI washout conjunction, no cross-edge trigger, different risk); the admitted `freqtrade-strategy004-adx-cci-dual-stoch-recross` sibling recrosses dual StochRSI bands on `5m` (no EMA rail, no MFI, no fastk/fastd edge, different risk); the admitted `freqtrade-strategy003-rsi-fisher-mfi-washout` sibling washes out on RSI/Fisher/MFI on `5m` (no StochF, no ADX, no EMA rail). Dropping the cross edge, any washout leg, the ADX leg, or the rail would each be a different, unpinned rule — none is admitted here.
9. Sibling-file fence: every other file in the official `user_data/strategies/` directory at the pinned commit (including `Diamond.py`, `Bandtastic.py`, `Supertrend.py`, `FixedRiskRewardLoss.py`, `hlhb.py`, `Strategy001.py`–`Strategy005.py`, `UniversalMACD.py`, `MultiMa.py`, and the `berlinguyinca/` siblings `Simple.py`/`CCIStrategy.py`/`MultiRSI.py`/`Low_BB.py`) is a separate pin — their constants must never be substituted into this record. In particular the pool's `freqtrade-simple-macd-bb-rsi-momentum` record already owns the `Simple.py` mechanism (MACD-over-zero × BB-upper-rising × RSI-70), which this record does not touch.
10. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the eight predeclared pins (BTCUSDT spot market choice, MARKET same-bar-close fills, 60-bar warmup floor, house sizing/costs, bar-close risk evaluation with fixed stop → take-profit → signal precedence, single-position/no-add book, strategy-specific stop-on-signal controller, `trade_cost = 0.0002`) — all predeclared above. The `1m` frame, all indicator constructions, the seven-conjunct entry, the exit conjunction, the 1% rung, the −50% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: seven-conjunct entry / all lookbacks-inputs / exit conjunction / single 1% rung / −50% stop / single-unit long-only / `1m` BTCUSDT spot / same-bar-close MARKET fills with fixed precedence are frozen.

- F1 — Cross-edge relevance: replacing the fastk/fastd cross edge with the level state (fastk > fastd, same ADX/MFI/CCI/rail legs, same exit/risk) must not improve net expectancy; fail ⇒ the edge adds nothing over the oversold state.
- F2 — Trend-gate relevance: dropping the `adx > 30` leg (same washout conjunction, same exit/risk) must not improve net expectancy; fail ⇒ trend certification adds nothing over the bare washout conjunction.
- F3 — Take-profit relevance: disabling the 1% barrier (signal exit plus fixed stop only, same entry) must not improve net expectancy; fail ⇒ the fixed take-profit adds nothing over the signal exit.

## Crypto portability

BTCUSDT Binance spot `1m` is the research pin (source names no market; no session, calendar, or venue-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape). Long-only with full-unit open/close expresses unchanged on spot with no naked shorting. No volume guard ships in the file (kept absent verbatim — 24/7 BTCUSDT minute tape has no zero-volume pathology to guard). Funding is venue-absent on spot and modeled nowhere.

## Limitations

- TA-Lib abstract internals (`EMA`/`STOCHF`/`ADX`/`MFI`/`CCI` seeding and rolling semantics, including the 14-bar defaults) and the pinned `technical` `crossed_above` implementation live in their libraries outside the pinned strategy file — pinned by call with the contemporaneous definitions quoted above, not re-derived; exact reproduction inherits those modules' seeding alongside the file-local arithmetic, under the disclosed 60-bar floor.
- No trailing, no time exit, no breakeven, no short leg — all explicitly absent, never to be added by repair. `time_limit = None` resolves to frame-end close in the pinned simulator — disclosed engine semantic, not a strategy time exit.
- Bar-close-atomic risk evaluation plus same-bar-close MARKET fills are the disclosed derivations (5) and (2) above: live limit-order-book behaviour, queue priority, and intrabar sequencing are scoped out, and this record makes no claim about the source's own default-limit backtest fills.
- The single-position book contradicts the docstring's 60-parallel-trades deployment recommendation by disclosed derivation (6); multi-slot shared-capital behaviour is out of scope for this record.
- `confidence: medium` reflects interpretation confidence in the rule transcription and engine-path mapping, never expected profitability.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothScalp.py
- https://github.com/freqtrade/freqtrade-strategies
