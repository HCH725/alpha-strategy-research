---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade SmoothScalp EMA-rail stoch-cross CCI-washout long-flat on BTCUSDT 1m bars
created: 2026-10-22
updated: 2026-10-22
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

# Freqtrade SmoothScalp EMA-rail stoch-cross CCI-washout long-flat on BTCUSDT 1m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-emaskippump`, `freqtrade-cofibit`, `freqtrade-strategy005`, `freqtrade-universalmacd`, `freqtrade-swinghightosky`, `freqtrade-binhv27`, and `freqtrade-macd-cross-cci-edge` records at this same pin — this record pins ONLY the SmoothScalp literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` twice during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/berlinguyinca/SmoothScalp.py`.
- GitHub blob SHA at the pinned commit: `9d0718b04aad27e8bc989b2362a22934485e9520`, size 3861 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 3861 bytes, 102 lines, SHA-256 `e32a8f758d8d57876210d479576e7e415ff924400b8d037bb1f2c87e38`, identical to the GitHub blob (`git hash-object` reproduces `9d0718b0…e9520`, blob SHA confirmed via the GitHub contents API at the pinned ref this cycle) — the entire file was retrieved and inspected.
- Registration: the file defines class `SmoothScalp(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing). Freqtrade strategies carry no `TYPE_NAME`/roster tuple — identity here is class plus file path plus pin, all unique. Every other `user_data/strategies/*.py` sibling is a different pin with different constants.
- The file's own words (quoted for gate evidence, never extended): `timeframe = '1m'`; `minimal_roi = { "0": 0.01 }` (single rung — the complete ROI table, quoted in full); `stoploss = -0.5`; indicator block `ta.EMA(dataframe, timeperiod=5, price='high'/'close'/'low')`, `ta.STOCHF(dataframe, 5, 3, 0, 3, 0)`, `ta.ADX(dataframe)`, `ta.CCI(dataframe, timeperiod=20)` then overwritten by `ta.CCI(dataframe)` (default period 14 — last write wins, disclosed below), `ta.RSI(dataframe, timeperiod=14)`, `ta.MFI(dataframe)`, `ta.MACD(dataframe)`, `qtpylib.bollinger_bands(dataframe['close'], window=20, stds=2)`; entry is the seven-conjunct `(open < ema_low) & (adx > 30) & (mfi < 30) & (fastk < 30) & (fastd < 30) & crossed_above(fastk, fastd) & (cci < -150)`; exit is `((open >= ema_high) | crossed_above(fastk, 70) | crossed_above(fastd, 70)) & (cci > 150)`. No `trailing`, no `startup_candle_count`, no `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `order_types` mapping, no `custom_stoploss`, no `position_adjustment`, no `time_limit` ships anywhere — the framework defaults below are disclosed as derived behaviour, never as file literals. The file ships no sample, window, trade count, or cost basis. The docstring's `recommend ... at least 60 parallel trades` sentence is author concurrency advice, explicitly NOT adopted (see Signal).
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.EMA` (TA-Lib EMA, explicit period 5 over the stated high/close/low inputs); `ta.STOCHF` (TA-Lib fast stochastic, all five arguments literal `5, 3, 0, 3, 0`); `ta.ADX` (TA-Lib directional system over `high`/`low`/`close`, default period 14 — no override in the file, disclosed); `ta.CCI` (TA-Lib CCI, effective period 14 after the overwrite, disclosed); `ta.RSI` (period 14, dead column — fenced); `ta.MFI` (period 14 over `high`/`low`/`close`/`volume` of the same feed, disclosed); `ta.MACD` (defaults 12/26/9, dead columns — fenced); `qtpylib.bollinger_bands` (window 20, stds 2 over `close`, dead columns — fenced); `qtpylib.crossed_above` (vendored helper: scalar second argument is promoted to a same-index Series, so `crossed_above(fastk, 70)` is exactly `(fastk[t] > 70) & (fastk[t-1] <= 70)` — verified in `technical/vendor/qtpylib/indicators.py` `crossed()` lines 227–243 this cycle; causal, no forward reference). No DB, no network, no `request.*`, no `security()`, no resample/interpolate/merge, no `fillna`/`ffill`, no hyperopt parameter of any kind.
- Full-file token census (verified over the 102 lines this cycle): 0 `enter_short` / 0 `exit_short` / 0 `can_short` (the single case-insensitive `short` hit is the English comment `the shorter the better` — no short leg, no short identifier anywhere in code); 0 `volume` token (the MFI library call reads the same-feed candle `volume` column internally — disclosed, never hidden); 0 `resample` / 0 `informative` / 0 `request` / 0 `security(` (single-frame, no external feed); 0 `trailing` / 0 `startup_candle` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `process_only_new_candles` / 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` (all such execution/position/economic semantics are predeclared researcher pins below, never file semantics); 0 `position_adjust` / 0 `max_open_trades` / 0 `cooldown` / 0 `pyramid` / 0 `position_size` (the position pin below is a predeclared researcher rule, never a file semantic); 0 `hyperopt` / 0 `IntParameter` / 0 `DecimalParameter` / 0 `CategoricalParameter` / 0 `BooleanParameter` (no tuning scaffolding — every constant is a frozen literal); 0 `ffill` / 0 `fillna` / 0 `interpolate` / 0 `dropna` / 0 `merge_informative` (pre-seed NaN comparisons read False — disclosed); 0 negative `shift` of any kind (the only inter-bar references are the helper-internal `shift(1)` inside the three `crossed_above` calls — causal one-bar edges); 3 `ta.EMA` / 1 `ta.STOCHF` / 1 `ta.ADX` / 2 `ta.CCI` (effective one, see Signal) / 1 `ta.RSI` / 1 `ta.MFI` / 1 `ta.MACD` (the complete indicator set); 1 `enter_long` / 1 `exit_long`; 0 `custom_stoploss` / 0 `use_custom_stoploss` / 0 `time_limit`; 0 `print(`. Duplicated `typing`/`functools`/`pandas`/`talib`/`qtpylib` imports are dead imports, fenced as plumbing with no gate effect.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The file is causal as written (all offsets non-negative, no resample/merge, no repainting primitive, no multi-timeframe feed, no external package — no repair site exists). Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` on a Binance **spot** venue (the source names no market; spot is chosen so the admitted economics carry no funding leg by venue construction — see Execution assumptions); (2) completed-bar decisions with same-bar-close market fills; (3) single-unit/no-add/no-effective-cooldown position pin plus a 100-bar researcher warmup floor (covers the 26-bar MACD seed and all 14/20-bar seeds with margin); (4) framework-default execution semantics pinned as derived behaviour (`can_short` defaults False → long-only, `use_exit_signal` defaults True → signal exits enabled, single-TP/single-SL legs bar-evaluated per the pinned simulator's literal rule — disclosed, never presented as file literals); (5) the explicit fee-only cost pin replaces the absent source economics (0.001 taker per side, zero added slippage — disclosed assumptions, never source facts). Every period, every threshold, the seven-conjunct entry, the exit disjunction, the single ROI rung, and the stop are untouched.

Pre-write dedup (2026-10-22): working-tree filename/content search for `SmoothScalp`, `smoothscalp`, and `smooth_scalp` returns zero strategy records. The open `research/*` PRs (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian ratio) contain no SmoothScalp pin and no EMA-rail/stoch-cross/CCI-washout conjunction. The closed #357 `SmoothOperator` PR pins the distinct sibling file `berlinguyinca/SmoothOperator.py` (V-bottom smoothed-composite — different source, different mechanism), never this file. Not a duplicate, paraphrase, or trivial parameter variant — see Negative evidence for the strategy004 fence.

## Economic mechanism

### Source-reported

The source claims no behavioural channel beyond its code: buy the 1m bar printed under the low-rail (`open < EMA5(low)`) with trend permission (`ADX > 30`), washed-out money flow (`MFI < 30`), a cold fast stochastic pair (`fastk < 30`, `fastd < 30`) crossing upward, and deep CCI washout (`CCI < −150`); stand aside to flat when the tape repairs (`CCI > 150`) together with either a high-rail reclaim (`open >= EMA5(high)`) or a hot stochastic cross (`fastk`/`fastd` crossing above 70). A single 1% take-profit rung and a −50% stop backstop every position. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Research interpretation

Seven-conjunct washout buyer, long-only, exited by repair states or a single 1% rung. Unlike single-oscillator dip buyers that fire on one print, the entry first demands a uniform tape posture (price under the low EMA rail, ADX trend permission, cold MFI, cold-and-turning stochastic) and only then requires deep CCI washout — so a dip with warm money flow, a flat stochastic, or shallow CCI prints nothing. Unlike trailing exits, the position exits through repair states or the single scalar rung: the −50% stop is a catastrophe backstop, so round-trips close on tape repair or the 1% rung, not on profit ladders — disclosed, never repaired into a livelier schedule.

## Signal

Exact rule as pinned (any other period, threshold, strictness, arm combination, risk rung, fill, frame, book, or leg is a different, unpinned rule):

```text
ema_high[t]  = TA-Lib EMA(high, 5)[t]
ema_close[t] = TA-Lib EMA(close, 5)[t]            // dead column — never gated, fenced
ema_low[t]   = TA-Lib EMA(low, 5)[t]
fastk[t], fastd[t] = TA-Lib STOCHF(5, 3, 0, 3, 0)[t]
adx[t]       = TA-Lib ADX(hlc, 14)[t]             // TA-Lib default period
cci[t]       = TA-Lib CCI(hlc, 14)[t]             // effective — CCI(20) overwritten line 62
mfi[t]       = TA-Lib MFI(hlcv, 14)[t]            // reads same-feed volume column, disclosed
rsi/macd/bb_*                    // dead columns — computed, never gated, fenced
entry = (open[t] < ema_low[t]) & (adx[t] > 30) & (mfi[t] < 30)
      & (fastk[t] < 30) & (fastd[t] < 30)
      & (fastk[t] > fastd[t]) & (fastk[t-1] <= fastd[t-1])   // crossed_above, scalar-free arm
      & (cci[t] < -150)                                     // enter_long = 1
exit_sig = ((open[t] >= ema_high[t])
         | ((fastk[t] > 70) & (fastk[t-1] <= 70))            // crossed_above(fastk, 70)
         | ((fastd[t] > 70) & (fastd[t-1] <= 70)))           // crossed_above(fastd, 70)
         & (cci[t] > 150)                                   // exit_long = 1
risk = single take-profit rung {"0": 0.01} (scalar 1% — the complete ROI table);
       fixed stop at -50% (stoploss -0.50); no trailing, no breakeven, no time exit
guard = pre-seed NaN comparisons read False (see Required data)
```

- Exact boundaries (pinned semantics): strict `<`/`>` throughout except the three helper-internal `<=` prior-bar legs exactly as the vendored `crossed()` implements them (`fastk[t-1] <= fastd[t-1]`, `fastk[t-1] <= 70`, `fastd[t-1] <= 70` — equality on the prior bar still crosses). Strict legs fire nothing on equality (open exactly on a rail, ADX exactly 30, MFI exactly 30, stochastic exactly 30, CCI exactly ±150 hold flat) — disclosed, not smoothed.
- CCI overwrite (pinned file behaviour): line 48 writes `cci = CCI(20)`, line 62 rewrites `cci = CCI(default 14)` — the gating legs read the rewritten column, so the effective CCI period is 14. Disclosed as written, never repaired into CCI(20).
- Trade events: `enter_long=1` on any bar printing the seven-conjunct state, `direction` long-only; `exit_long=1` on any bar printing the repair disjunction. Both legs are STATE prints in construction (each persists while its levels hold — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code).
- Mutual-exclusion proof (no tie-break pin required): the entry demands `cci[t] < -150` while the exit demands `cci[t] > 150` — disjoint by 300 points on the same column. No single bar satisfies both legs; the reviewer is never asked to invent a signal ordering.
- Barrier/signal co-print pin (predeclared, simulator-literal): the single 1% TP leg and the repair exit can co-print on one bar. Both close the full unit at that bar's close under the derived rule (the simulator settles barrier closes on close-based pnl at `close_timestamp`; the controller stop settles at the exit bar's timestamp — same bar, same close, same economics), so no intrabar ordering assumption is needed and no outcome depends on it.
- Direction: long-only. Zero short-leg code ships anywhere (`can_short` absent → Freqtrade default False) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the repair signal exit, the single 1% ROI rung, and the −50% stop are the complete position-closing set. No trailing, no breakeven, no time exit — explicitly none, not invented. `use_exit_signal` is absent (Freqtrade default True — signal exits enabled as coded, disclosed as derived behaviour).
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment`/`max_open_trades` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying washout bar after any exit; cooldown pinned to 1 second (controller field requires `gt=0`; 1 second sits below the 1m grid — explicitly no effective cooldown, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. The docstring's `60 parallel trades` advice is explicitly NOT adopted — the admitted version is single-unit by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`open`/`high`/`low` for the EMA rails, `high`/`low`/`close` for ADX/CCI, `high`/`low`/`close`/`volume` for MFI, `close`-derived windows for STOCHF/RSI/MACD/BB) with fixed non-negative window offsets plus helper-internal one-bar lags (no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, `ffill`/`fillna`, hyperopt parameter, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1m` bars of BTCUSDT: `open`/`high`/`low`/`close` for the EMA-rail/ADX/CCI/STOCHF paths; same-bar `volume` for the MFI path only (same klines feed, point-in-time, causal — disclosed). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1m` (source-native — the file prints `timeframe = '1m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only (helper-internal `shift(1)` at most); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher floor, disclosed): the record-rule floor holds 100 one-minute bars flat (~1.7 hours). Covers the 26-bar MACD seed, the 20-bar BB/CCI seeds, and all 14-bar ADX/RSI/MFI/CCI seeds plus the one-bar cross lags with margin. Coded behaviour underneath: TA-Lib emits NaN pre-seed and every NaN comparison reads False — so no entry/exit leg can print before its longest window fills; no `fillna`/`ffill` exists to smear seeds forward. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT on a Binance **spot** venue (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Spot is chosen deliberately: a spot book carries no funding leg by venue construction, so the admitted economics are complete with fees alone (see costs).
- Pinned engine (exact, verified this cycle — not a sibling-count claim): the pinned Hummingbot baseline is package `20260920`, VERSION `dev-2.17.0`. Every engine fact below was read at local commit `fac3a7f` (2026-09-20, `hummingbot/VERSION` reads exactly `dev-2.17.0`; that commit touches only the `setup.py` version string, so the cited tree IS the Sep-20 baseline), and each cited file was verified byte-identical to the later working tree (md5): `directional_trading_controller_base.py` md5 `7d213fbe154176e3f51aea4fc1911ede` both sides; `position_executor/data_types.py` md5 `81e674754ff187939c1abbd05d6a1886` both sides; `executors_simulator/position_executor_simulator.py` zero diff; `binance_spot_candles/constants.py` md5 `15d13da9769295f47c12a9d4975be4ed` both sides; `backtesting_engine_base.py` differs ONLY in DCA early-close handling (position path untouched). The one naming wrinkle is disclosed, not hidden: that same Sep-20 commit bumps the `setup.py` string to `20260922` — a version-string label inside the pinned commit, never a different build; no capability is borrowed from any later commit.
- Controller path (pinned file, exact): `DirectionalTradingControllerBase.determine_executor_actions()` returns `create_actions_proposal()` plus `stop_actions_proposal()`; the create arm maps signal > 0 to a BUY `CreateExecutorAction` sized `total_amount_quote / price / max_executors_per_side`; `can_create_executor()` enforces `max_executors_per_side` (pinned 1) and `cooldown_time` (pinned 1, field requires `gt=0`); the base `stop_actions_proposal()` returns `[]`, so the derived controller subclass emits the `StopExecutorAction` on `exit_long` prints — a stated subclass contract, never a claim about the base. `get_executor_config()` builds a `PositionExecutorConfig` (BUY side, market entry, mid-price entry quote).
- Executor path (pinned file, literal semantics adopted verbatim): `PositionExecutorSimulator.simulate()` with a market order starts at the decision bar (`start_timestamp = df min`) and fills at its close (`entry_price = df.loc[start_timestamp, 'close']`) — same-bar-close fill proven from the pinned code, never asserted without a line reference. `TripleBarrierConfig` legs are ALL `Optional` (pinned `data_types.py` lines 32–36: `stop_loss`/`take_profit`/`time_limit`/`trailing_stop` default `None`), and this record uses exactly two: scalar `take_profit = 0.01` (the single `{"0": 0.01}` rung — `tp = float(...) if take_profit else None`, first close-pnl breach wins; no age schedule exists in the file or in the simulator, and none is claimed) and scalar `stop_loss = 0.5` (`sl_price = entry × (1 − 0.5)`, first bar with `low ≤ sl_price` wins). `time_limit` and `trailing_stop` are `None` — explicitly disabled, matching the file's absence of both. Round-trip fees are `2 × trade_cost` on filled notional (simulator lines 45/49).
- Stop-scan scope (declared exactly to avoid any bar-close contradiction): the simulator scans the SL condition over the filtered frame **including the entry bar** — the entry bar's `low` may precede the close fill in wall-clock. This record adopts that literal rule as the derived execution semantic (trigger: first bar from and including the entry bar with `low ≤ 0.5 × entry`; settlement: close-based pnl at `close_timestamp`), disclosed as the pinned engine's defined modelling semantic — never re-described as post-fill-only evaluation. Severity fence: with a −50% stop on 1m BTCUSDT spot tape, a same-entry-bar stop needs a ≥50% intrabar collapse; modelled, never zero-claimed (see Negative evidence).
- Data path (pinned file, exact): `binance_spot_candles` feed (`REST /api/v3/klines`), whose `INTERVALS` map explicitly includes `1m`; the backtest iterates completed candle rows (`update_state(row)` then `determine_executor_actions()`, creating the executor simulation over `processed_features.loc[i:max_ts]`), and stops settle through the pinned two-argument `handle_stop_action(action, row["timestamp"])` at the exit-signal bar. No funding reference ships anywhere in the `strategy_v2/backtesting/` tree (verified by filename-wide grep at the pinned commit) — and on a spot venue there is no funding leg to model in the first place.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its single ROI rung and stop percentage are preserved verbatim as the risk legs while sizing and costs ride explicit researcher pins: single-unit full-amount open/close, leverage pinned 1 with no liquidation branch anywhere in the 88-line simulator (long-only BUY on spot settles as a buy-then-sell round trip), taker fee 0.001 per side with zero added slippage (both disclosed researcher assumptions applied as the simulator `trade_cost`, never presented as source-native behaviour, never reported as realized exchange economics).
- Concurrency: at most one position per market at any time (controller-enforced `max_executors_per_side = 1`); the washout state opens the full unit on a flat book; the repair exit, the 1% rung, or the stop closes it in full; re-entry after a close needs only the next qualifying washout bar. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (102 lines: the EMA/STOCHF/ADX/CCI/RSI/MFI/MACD/BB indicator block, the seven-conjunct entry, the repair-disjunction exit, the `timeframe`/`minimal_roi`/`stoploss` literals, and the `SmoothScalp(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: TA-Lib emits NaN pre-seed and every NaN comparison reads False — no leg can print before its longest window fills; no `fillna`/`ffill` smears seeds forward. The 100-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fires nothing on equality (open exactly on a rail, ADX/MFI/stochastic exactly on 30, CCI exactly ±150 hold flat); the three helper-internal `<=` prior-bar legs fire on equality exactly as the vendored helper implements them — disclosed, not smoothed.
3. Co-print arithmetic fenced (impossible, proved — not pinned): entry demands `cci < -150`, exit demands `cci > 150` on the same column. No bar prints both legs; no ordering invented. The TP-vs-signal same-bar co-print settles identically at the same close (see Execution assumptions) — fenced, not repaired.
4. Entry-bar stop scope fenced (modelled, never zero-claimed): the SL scan includes the entry bar per the simulator's literal rule; a same-entry-bar stop on 1m BTCUSDT spot tape requires a ≥50% intrabar collapse to `0.5 × entry`, settled at close-based pnl. Disclosed engine semantic with severity fence — not a causality repair.
5. Zero-variance fenced: flat tape zeroes oscillators into NaN/constant seeds (ADX prints 0 — failing `> 30`; both sides of each cross read equal — strict `>` fails, `<=` holds, so no cross prints; CCI/MFI print midscale/NaN — failing the washout floors). No division exists in the gating path — disclosed, not repaired.
6. Dead-code plumbing fenced: `ema_close`, `rsi`, `macd`, `macdsignal`, `macdhist`, `bb_lowerband`, `bb_upperband`, `bb_middleband` are computed and never read by any order line; the line-48 `CCI(20)` is overwritten by line-62 `CCI(14)` before any gating read — this record conditions only on the effective CCI(14) and never on any dead column, and no reviewer repair may promote any of them into a leg.
7. Cousin records fenced as different constructions (none trades a seven-conjunct open-rail/ADX/MFI/dual-threshold-stoch-cross/CCI-washout entry with a rail-or-hot-cross/CCI-repair exit on `1m` with a single 1% rung): the admitted strategy004 sibling trades a nine-conjunct dual-STOCHF-stack/volume-floor entry (ADX14 > 50 or slow-ADX35 > 26, CCI20 < −100, lagged dual-stack thresholds, trailing volume floor, dust line) with a slow-ADX-collapse exit and a four-rung decaying ROI ladder on `5m` — different legs (no MFI, no open-vs-EMA rails, no CCI-150 washout, dual slow stack, volume floor), different frame, different risk (four rungs vs one, −30% vs −50%); the admitted BbandRsi/CMCWinner/ASDTSRockwell/MACD siblings trade band-dip, triple-oscillator, MACD-polarity, or cross-edge systems (never this conjunction); the closed SmoothOperator PR pins a different file and a V-bottom composite. Not a threshold re-tuning of any of them: changing any period, threshold, strictness, or arm would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `user_data/strategies/*.py` sibling is a separate pin — its constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT spot market choice, same-bar-close fills, single-unit/no-add/1-second-cooldown position pin with 100-bar warmup floor, derived `can_short=False`/`use_exit_signal=True`/market-fill execution semantics, fee-only costs) — all predeclared above. The `1m` frame, the indicator block, the seven-conjunct entry, the repair exit, the single 1% rung, the −50% stop, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: washout entry / all eleven periods / all frozen thresholds / repair exit / single 1% rung / −50% stop / single-unit long-only / `1m` BTCUSDT spot / same-bar-close fills are frozen.

- F1 — CCI-severity relevance: softening the entry CCI leg to `< -100` (same six conjuncts, same exit/risk) must not improve net expectancy; fail ⇒ the −150 washout depth adds nothing over a mild-washout filter.
- F2 — Signal-exit relevance: dropping the repair signal exit entirely (1%-rung/stop-only exits, same entry) must not materially change round-trip outcomes; fail ⇒ the repair arms carry weight beyond decoration.
- F3 — Money-flow relevance: dropping the `mfi < 30` entry conjunct (six-conjunct entry, same exit/risk) must not improve net expectancy; fail ⇒ the cold-money-flow permission adds nothing over the bare rail/stoch/CCI state.

## Crypto portability

BTCUSDT Binance spot `1m` is the research pin (source names no market). Long-only with full-unit open/close is native to a spot venue with no naked shorting and no funding leg. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only the `open`/`high`/`low`/`close`/`volume` candle fields are read (venue definition differences move only oscillator inputs, disclosed). Funding is structurally absent on spot and modelled nowhere — never reported as realized.

## Limitations

- TA-Lib EMA/STOCHF/ADX/CCI/RSI/MFI/MACD internals live in their library outside the pinned file — pinned by call with explicit periods (defaults 14/12-26-9 disclosed where the file passes none), not re-derived; exact reproduction inherits that module's seeding and rolling semantics alongside the file-local NaN-false wiring, under the disclosed 100-bar floor.
- The −50% stop is a catastrophe backstop — round-trips close overwhelmingly via the repair exit or the single 1% rung. This record repairs nothing: the effective behaviour is fully explicit and complete, and any livelier schedule would be a different, unpinned rule no reviewer may invent.
- No trailing, no breakeven, no time exit, no short leg, no effective cooldown — all explicitly absent, never to be added by repair.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close convention; this record makes no claim about any live-order behaviour.
- 1m decision cadence implies ~1440 evaluations per day; this is a data-availability statement (the pinned spot feed lists `1m`), never a latency or throughput claim.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/SmoothScalp.py
- https://github.com/freqtrade/freqtrade-strategies
