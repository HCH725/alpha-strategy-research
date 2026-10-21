---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade Bandtastic BB-sigma dip MFI-gated long-flat on BTCUSDT 15m bars
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
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade Bandtastic BB-sigma dip MFI-gated long-flat on BTCUSDT 15m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/freqtrade/freqtrade-strategies (official open-source Freqtrade strategy collection; the lane that already supplied the admitted `freqtrade-combined-binh-cluc`, `freqtrade-emaskippump`, `freqtrade-binhv27`, `freqtrade-hlhb`, `freqtrade-multima`, and `freqtrade-strategy003` records — this record pins ONLY the Bandtastic literals below, and no reviewer repair may substitute a sibling constant).
- Pinned commit SHA: `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `user_data/strategies/Bandtastic.py`.
- GitHub blob SHA at the pinned commit: `f7710c76ae1e4ac7aff90857a647e4c2143baf9f`, size 7310 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 7310 bytes, 163 lines, SHA-256 `15dcb60d49a3681241cd39645f0fe8e6dc247687bf878c2026f37bb1c5790b57`, identical to the GitHub blob (`git hash-object` reproduces `f7710c76…3baf9f`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Bandtastic(IStrategy)` (the only class in the file), `INTERFACE_VERSION = 3`, framework column contract `populate_entry_trend` / `populate_exit_trend` (`enter_long` / `exit_long`, never the old `buy`/`sell` plumbing).
- The file's own words (quoted for gate evidence, never extended): `timeframe = '15m'`; `minimal_roi = { "0": 0.162, "69": 0.097, "229": 0.061, "566": 0 }`; `stoploss = -0.345`; `startup_candle_count = 999`; `trailing_stop = True`, `trailing_stop_positive = 0.01`, `trailing_stop_positive_offset = 0.058`, `trailing_only_offset_is_reached = False`; entry is the two-conjunct AND of `close < bb_lowerband1` (Bollinger window 20, 1 sigma, over `typical_price`) and `volume > 0`; exit is the three-conjunct AND of `mfi > 46`, `close > bb_upperband2` (Bollinger window 20, 2 sigma, over `typical_price`), and `volume > 0`. No `trailing` override beyond the four literals, no `can_short`, no `use_exit_signal` / `exit_profit_only` override, no `order_types` mapping, no `order_time_in_force`, no `position_adjustment` / `max_open_trades` / `cooldown` / `pyramid` / `position_size`, no `leverage`, no `funding`, no `mark_price` ships anywhere — all such execution/position/economic semantics are predeclared researcher pins below, never file semantics. The file ships no sample, window, trade count, or cost basis beyond a hyperopt comment table fenced in Negative evidence.
- Hyperopt scaffolding pinned (all resolved to frozen defaults, all standard): 8 `IntParameter` (`buy_fastema` 1–236 default 211, `buy_slowema` 1–250 default 250, `buy_rsi` 15–70 default 52, `buy_mfi` 15–70 default 30, `sell_fastema`/`sell_slowema` 1–365 defaults 7/6, `sell_rsi` 30–100 default 57, `sell_mfi` 30–100 default 46 — every one `optimize=True, load=True`) and 8 `CategoricalParameter` (`buy_rsi_enabled`/`buy_mfi_enabled`/`buy_ema_enabled` default False, `buy_trigger` default `"bb_lower1"`, `sell_rsi_enabled` default False, `sell_mfi_enabled` default True, `sell_ema_enabled` default False, `sell_trigger` default `"sell-bb_upper2"`). No `buy_params` / `sell_params` dict and no parameter file ships anywhere in the pin — the effective rule is the in-file defaults exactly as coded; any hyperopt-loaded point is a different, unpinned rule no reviewer may substitute. The constants carry hyperopt-fitted origin per the file's own comments (`Optimized With Sharpe Ratio and 1 year data` plus a pasted result table) — frozen here as literals with no training performed in this record and no training cutoff shippable from the file (see Limitations).
- Out-of-file calls pinned (all resolved by name, all standard defaults): `ta.RSI(dataframe)` (TA-Lib default `timeperiod=14` — computed, unread by the frozen rule, fenced); `ta.MFI(dataframe)` (TA-Lib default `timeperiod=14` — the exit's `mfi` read); `ta.EMA(dataframe, timeperiod=period)` over the full 1–365 hyperopt-union bank (computed, unread by the frozen rule — every EMA guard defaults False — fenced); `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=1/2/3/4)` (vendored rolling mean/std over `(high+low+close)/3`; the frozen rule reads ONLY `bb_lowerband1` and `bb_upperband2` — all other band columns dead, fenced). No DB, no network, no `request.*`, no `security()`, no resample/interpolate, no `fillna`/`ffill`/`nan_to_num`, no hyperopt call of any kind at research time.
- Full-file token census (verified over the 163 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 4 `volume` (exactly the two `volume > 0` guards plus their two `# Check that volume is not 0` comments — no other volume read); 0 `cross` (no `crossed_above`/`crossed_below` edge anywhere — both legs are persistent level states, never one-bar edges); 0 `resample` / 0 `informative` / 0 `request` / 0 `security(` (single-frame, no external feed); 4 `trailing` (exactly the four trailing literals); 1 `startup_candle_count` (`999`); 0 `can_short` / 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `process_only_new_candles` / 0 `order_types` / 0 `order_time_in_force` / 0 `leverage` / 0 `funding` / 0 `mark_price` (all such semantics are predeclared researcher pins below); 0 `position_adjust` / 0 `max_open_trades` / 0 `cooldown` / 0 `pyramid` / 0 `position_size`; 16 `Parameter(` (exactly the sixteen frozen hyperopt declarations above); 0 negative `shift(-` (no shift call at all — per-bar state evaluation); 2 `hyperopt` (the two `# Hyperopt Buy/Sell Parameters` header comments only); 1 `enter_long` / 1 `exit_long` / 0 `enter_short` / 0 `exit_short`; 0 `print(`. `numpy as np` / `pandas as pd` / `reduce` are imported; `reduce(` is called only to AND the frozen condition lists — no gate effect beyond conjunction.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source backtest. The file is causal as written (no forward reference, no resample/merge, no repainting primitive, no multi-timeframe feed — no repair site exists). Researcher-declared adaptations are exactly six: (1) research market `BTCUSDT` on Binance USDT-M perpetual via connector `binance_perpetual` (the source names no market; its comments show a spot example config and an altcoin pair list — no source-market equivalence is claimed); (2) completed-bar decisions with same-bar-close MARKET fills (the source ships no order types — Freqtrade market-fill default — and the pinned simulator fills market entries at the entry candle's close, verified below); (3) single-unit/no-add/no-pyramid position pin (`max_executors_per_side = 1`), `cooldown_time = 1` (the controller field requires `gt=0`; one second sits below the 15m decision grid, so re-entry re-arms on the next completed bar — the file's no-cooldown semantics preserved), `leverage = 1` (the executor default; the controller prompt documents 1 as the spot-like setting — no liquidation event can occur, so the full barrier set below covers every close), plus the source-native 999-bar warmup floor with pre-warmup bars flat by record rule; (4) framework-default execution semantics pinned as derived behaviour (`can_short` absent → False, long-only; `use_exit_signal` absent → True, signal exits enabled; `exit_profit_only` absent → False, exits fire even at a loss — disclosed, never presented as file literals); (5) bar-close evaluation of the ROI ladder, the fixed stop, and the trailing stop under the verified per-tick precedence below (the source evaluates risk intrabar; intrabar sequencing is scoped out, never invented); (6) the house cost/capital overlay replaces the absent source economics (taker 0.0005/side, zero added slippage, historical-funding overlay modeled-not-realized; the 6%+6%+6% DCA staging is explicitly a separate downstream experiment, NOT part of this version). Every band window, every sigma, every threshold, the two-conjunct entry, the three-conjunct exit, the four-rung ROI ladder, the stop, and the trailing quadruple are untouched.

Pre-write dedup (2026-10-22): working-tree filename/content search for `Bandtastic`, `bandtastic`, `bb_lowerband1`, `buy_trigger`, and `sell-bb_upper` returns zero strategy records — the only `Bandtastic.py` hit pool-wide is the sibling-file fence inside the admitted HLHB record, and the only shared literal anywhere (`stoploss = -0.345`) is the admitted MultiMa record, fenced as a different construction in Negative evidence. The admitted CombinedBinHAndCluc sibling trades a dual-leg BB-penetration entry on `5m` (never a 1σ-typical dip with an MFI-gated 2σ reclaim exit); the admitted BbandRsi sibling trades RSI14<30 plus sub-band close on `1h` with an RSI-70 exit and no trailing (different legs, frame, and risk stack); the admitted Strategy003 sibling conjoins an eight-leg RSI/Fisher/MFI-washout on `5m` with a SAR exit (different conjunction, opposite MFI side/threshold, no trailing). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian ratio) trades a BB-sigma dip with an MFI-gated band-reclaim exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims no behavioural channel beyond its code: buy the bar printing under the 1σ lower rail of a 20-bar typical-price Bollinger envelope while the tape is alive (`volume > 0`); stand aside to flat on the bar where money flow runs hot (`MFI(14) > 46`) AND price reclaims over the 2σ upper rail of the same envelope. A four-rung time-decaying ROI ladder (16.2% → 9.7% → 6.1% → 0% across 0/69/229/566 minutes) harvests winners, a −34.5% fixed stop backstops catastrophes, and a trailer (arms past +5.8%, trails 1.0% under the peak) rides extended moves. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Research interpretation

Asymmetric-envelope dip buyer, long-only, exited by heated reclaim states. Unlike single-rail BB systems that enter and exit off the same band, the entry stoops to the 1σ lower rail (a soft dislocation, not a tail event) while the exit demands the 2σ upper rail PLUS hot money flow — so a V-bounce that reclaims the midline on cold MFI holds the book, and only a heated march to the far rail closes it. Unlike stop/trailing exits, the signal legs do the discriminating work while the risk stack (decaying ladder, wide stop, small trailer) prices time and tail — disclosed, never repaired into a livelier ladder.

## Signal

Exact rule as pinned (any other period, sigma, threshold, strictness, arm combination, risk rung, fill, frame, book, or leg is a different, unpinned rule). All identifiers below are the program's own at frozen defaults:

```text
typical[t]  = (high[t] + low[t] + close[t]) / 3
mid20[t]    = SMA(typical, 20)[t];  sd20[t] = STDEV(typical, 20)[t]
lower1[t]   = mid20[t] - 1 * sd20[t]          // bb_lowerband1
upper2[t]   = mid20[t] + 2 * sd20[t]          // bb_upperband2
mfi[t]      = MFI(high, low, close, volume, 14)[t]   // TA-Lib default period
entry = (close[t] < lower1[t]) & (volume[t] > 0)                          // enter_long = 1
exit_sig = (mfi[t] > 46) & (close[t] > upper2[t]) & (volume[t] > 0)        // exit_long = 1
risk = time-decaying take-profit minimal_roi {"0": 0.162, "69": 0.097, "229": 0.061, "566": 0};
       fixed stop at -34.5% (stoploss -0.345);
       trailer: arms past +5.8% (offset 0.058), trails 1.0% under the peak (positive 0.01),
       only-offset-reached False (live arming nuance scoped to the bar-close ratchet below);
       no time exit beyond the ladder's final 0 rung — explicitly none, not invented
guard = rolling-window NaN comparisons are false (no seed-smearing call anywhere — see Required data)
```

- Exact boundaries (pinned semantics): strict `<` on the entry band leg and both strict `>` on the exit legs — a close exactly on either rail, or MFI exactly 46, holds flat. `volume > 0` strict (exactly zero fails). The `20` window, the `1`/`2` sigmas, the `14` MFI period, the `46` line, and all four ROI rungs are never tuned here.
- Trade events: `enter_long=1` on any bar printing the entry state, `direction` long-only; `exit_long=1` on any bar printing the heated-reclaim state. Both legs are STATE prints in construction (each persists while its levels hold — close-and-hold-flat); either leg can reprint across consecutive bars (no one-shot latch in code).
- Mutual-exclusion proof (no tie-break pin required): the entry demands `close < mid20 − sd20` (strict) while the exit demands `close > mid20 + 2·sd20` (strict) — jointly unsatisfiable on one bar since `−sd20 ≤ +2·sd20` always (and with `sd20 = 0` both strict legs fire nothing). No single bar satisfies both legs; the reviewer is never asked to invent an ordering. ROI/stop/trailer legs start at zero distance on the entry bar — disclosed, not repaired.
- Direction: long-only. Zero `short` tokens ship anywhere and `can_short` is absent (Freqtrade default False) — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the heated-reclaim signal exit, the four-rung ROI ladder, the −34.5% stop, and the trailer are the complete position-closing set. No breakeven move and no fixed time exit beyond the ladder's terminal 0 rung — explicitly none, not invented. `use_exit_signal` is absent (Freqtrade default True — signal exits enabled as coded) and `exit_profit_only` is absent (default False — exits fire even at a loss); both disclosed as derived behaviour.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market (`max_executors_per_side = 1`); a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging, no DCA — no `position_adjustment`/`max_open_trades` ships anywhere, and the house 6%+6%+6% DCA staging is a separate downstream experiment, never part of this version); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying dip bar after any exit (`cooldown_time = 1`, below the decision grid — the file's no-cooldown semantics preserved). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLCV (`high`/`low`/`close` for typical/BB/MFI, `volume` for the MFI path and both guards) with fixed non-negative window offsets (no forward reference) — no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, `ffill`/`fillna`, hyperopt call, or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `15m` bars of BTCUSDT (Binance USDT-M): `high`/`low`/`close` for the typical-price/BB(20, 1σ/2σ) paths; `high`/`low`/`close`/`volume` for the MFI(14) path; `volume` for both alive-tape guards. No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `15m` (source-native — the file prints `timeframe = '15m'`). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (source-native floor, disclosed): the record-rule floor holds 999 fifteen-minute bars flat (~10.4 days) per the file's own `startup_candle_count = 999`. Covers the 20-bar band seed, the 14-bar RSI/MFI seeds, and the full 1–365 dead EMA bank with margin. Coded behaviour underneath: rolling windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early; the feed additionally pre-buffers `max_records` of history before the run window (verified engine machinery, see Execution assumptions). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Engine source pin (read this cycle, traceable): `HCH725/hummingbot@2dbc844` (fork master HEAD as read 2026-10-22; `hummingbot/VERSION` reads `2.17.0`, matching the README `dev-2.17.0` version contract; `setup.py` package lineage reads `20260922` — two days off the README `20260920` package tag, disclosed in Limitations, never hidden). Every path below was read at that commit; field and class names are quoted verbatim so the reviewer can re-verify by search.
- Controller/executor path (exact, disclosed): a `DirectionalTradingControllerBase` subclass (`hummingbot/strategy_v2/controllers/directional_trading_controller_base.py`) driving `PositionExecutor` (`type: "position_executor"`) on connector `binance_perpetual` (`hummingbot/connector/derivative/binance_perpetual/`), trading pair `BTC-USDT` (venue spelling; `BTCUSDT` is the research spelling — spelling normalization is the only market step, and no source-market equivalence is claimed). Signal candles ride the `binance_perpetual_candles` feed (`hummingbot/data_feed/candles_feed/candles_factory.py` registry) at the single decision interval `15m`; the backtest runs at `backtesting_resolution = "15m"` (`BacktestingEngineBase.run_backtesting`, whose signature also pins the modeled `trade_cost` run input). Decision/availability: the engine ticks per completed resolution-candle row (`prices = close`, `_time = row timestamp`), signal features merge via backward `merge_asof` (point-in-time join — later rows can never leak into earlier decisions), and rows with missing fields drop out (`dropna`) — `prepare_market_data` / `update_state` as read.
- Order timing (derived, disclosed): completed-bar decision with same-bar-close MARKET fills. Market entry is the verified taker path: the directional base defaults `open_order_type = MARKET` ("as is a Taker Controller"), and the market-entry branch of `PositionExecutorSimulator.simulate` fills at `df.loc[start_timestamp, 'close']` — the entry candle's own close (`hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py` as read). No maker-touch, queue, or intrabar-path-dependent fill: entry/exit co-prints are arithmetically impossible (see Signal), leaving no invented engine ordering.
- Risk-leg mapping (exact, disclosed): the file's stop/ROI/trailer ride the simulator's verified triple-barrier machinery — `TripleBarrierConfig.stop_loss = 0.345` (evaluated on the BUY low-touch `low <= entry*(1-sl)`, candle extremes from the same row, no imaginary prints), `take_profit` per the controller-carried rung of the `{0.162, 0.097, 0.061, 0}` age schedule (each evaluated strict-`>` on close-based `net_pnl_pct`), `trailing_stop = {activation_price: 0.058, trailing_delta: 0.01}` (the simulator's trigger-gated cummax ratchet closing as `CloseType.TRAILING_STOP`), `time_limit = None` (no file leg — never binds). Barrier order types stay at their verified MARKET defaults; the open leg is pinned MARKET (taker), overriding the config struct's LIMIT default exactly as the directional taker base does. Same-tick precedence is verified code, not convention: each tick settles natural barrier terminations first (`update_executors_info` inside `update_state`) before controller stop proposals, and simultaneous barrier timestamps break TP → SL → trailing → time-limit by the simulator's ordered comparison; controller signal stops settle as `CloseType.EARLY_STOP` at the decision-tick timestamp (`handle_stop_action` as read).
- Sizing/capital (predeclared researcher pin, reproducible rule): `max_executors_per_side = 1`, `amount = total_amount_quote / price` (the base's verified equal-split formula with one executor), `leverage = 1` (the executor struct default; the controller prompt documents 1 as the spot-like setting — no liquidation event can occur, so the barrier set above covers every close). `total_amount_quote` is the run's declared stage stake (fixed research run input, like start/end); venue minimums and lot/price rounding ride the engine's verified trading-rules machinery (`initialize_trading_rules(binance_perpetual)` plus `quantize_order_amount`/`quantize_order_price` as read) — never deferred vaguely downstream. The house 6%+6%+6% DCA staging is a separate downstream experiment, explicitly NOT part of this version.
- Costs (declared research model, verified machinery): taker `0.0005`/side, zero added slippage — carried by the `trade_cost` run input; the simulator books `2 * trade_cost` on filled quote across the round trip with full `cum_fees_quote` accounting (as read). Perpetual funding has no term anywhere in the backtesting execution path read (engine base, data provider, all four executor simulators) — so funding rides the declared house research overlay (historical funding series; modeled, never realized/canonical, never reported as zero), per the README research/canonical cost separation; final HB economics belong to the downstream Node13 check, never to this admission.
- Concurrency: at most one position per market at any time; the dip entry opens the full unit on a flat book; the heated-reclaim signal, any ROI rung, the stop, or the trailer closes it in full; re-entry after an exit needs only the next qualifying dip bar (`cooldown_time = 1`, below-grid). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (163 lines: the RSI/MFI/BB-bank indicator block, the frozen hyperopt default declarations, the two-conjunct entry, the three-conjunct exit, the `timeframe`/`startup_candle_count`/`minimal_roi`/`stoploss`/trailing literals, and the `Bandtastic(IStrategy)` class pin). The two pasted hyperopt comment tables (`199/40000 … 119.93%` and objective `-127.60220`) ship no pair list, evaluation window, dates, or cost basis — this record claims no source-reported performance and no reproduced performance from them.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: rolling BB/RSI/MFI/EMA windows print NaN until seeded and every strict NaN comparison is false — no leg can fire early; the 999-bar record-rule floor additionally holds every pre-seed bar flat, and the feed pre-buffers history before the run window (verified machinery) — disclosed, not repaired.
2. Exact-touch rule fenced: strict `<`/`>` fires nothing on equality (close exactly on either rail, MFI exactly 46, volume exactly 0 all hold flat) — disclosed, not smoothed.
3. Co-print arithmetic fenced (impossible, proved — not pinned): entry (`close` under the 1σ lower rail) contradicts the exit (`close` over the 2σ upper rail) on every tape including zero-variance. No bar prints both legs; no ordering invented.
4. Zero-variance fenced: flat tape zeroes dispersion (`sd20 = 0`, both rails equal the midline — strict legs fail), freezes MFI near 0/NaN (the `> 46` leg fails), and still prints `volume > 0` harmlessly — the book holds flat, disclosed, not repaired.
5. Dead-code plumbing fenced: `rsi` (RSI(14), all three RSI guards default False), `bb_middleband*`/`bb_upperband1`/`bb_lowerband2-4`, and the entire `EMA_1`…`EMA_365` bank (all EMA guards default False) are computed and never read by any order line; `np`/`pd`/`reduce` beyond the frozen AND-lists are display/conjunction leftovers — this record never conditions on them and no reviewer repair may promote any of them into a leg.
6. Fitted-origin fenced: the sixteen hyperopt declarations and the two pasted result tables mark the constants as search-derived, but the pin ships no training window, dates, pair list, or cost basis — there is no shippable training cutoff, so this record freezes them as literals, performs no training, and admits no retune (any other hyperopt point is a different, unpinned rule).
7. Cousin records fenced as different constructions (none trades a sub-1σ-typical dip with an MFI-gated 2σ-upper reclaim exit on `15m` under a decaying ladder plus wide stop plus trailer): the admitted CombinedBinHAndCluc sibling trades a dual-leg BB-penetration entry on `5m` (penetration-plus-body-guards, never sigma-level states with an MFI heat leg); the admitted BbandRsi sibling trades RSI14<30 plus sub-band close on `1h` with an RSI-70 exit and NO trailing (different legs, frame, risk stack); the admitted Strategy003 sibling conjoins an eight-leg RSI/Fisher/MFI<16 washout on `5m` with a SAR exit (opposite MFI side and threshold, no trailing); the admitted MultiMa sibling shares only the `-0.345` stop literal (4h TEMA-stack trend, trailing disabled); the admitted EMASkipPump sibling trades an EMA-stack dip with a volume veto and no MFI leg. Changing any window, sigma, threshold, strictness, rung, or the trailing quadruple would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: every other `user_data/strategies/*.py` file at the pinned commit is a separate pin — its constants must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six declared adaptations (BTCUSDT-perpetual market choice, same-bar-close MARKET fills, single-unit/`max_executors_per_side=1`/`cooldown_time=1`/`leverage=1` position pin with the 999-bar floor, derived `can_short=False`/`use_exit_signal=True`/`exit_profit_only=False` framework semantics, bar-close risk evaluation under the verified precedence, house sizing/costs with DCA explicitly downstream-only) — all predeclared above. The `15m` frame, the typical-price BB(20, 1σ/2σ) constructions, the MFI(14) read, the two-conjunct entry, the three-conjunct exit, the four-rung ROI ladder, the −34.5% stop, the trailing quadruple, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: two-conjunct entry / all windows-sigmas-periods / three-conjunct exit / four-rung ROI / −34.5% stop / trailing quadruple / single-unit long-only / `15m` BTCUSDT-perpetual / same-bar-close MARKET fills under the verified precedence are frozen.

- F1 — MFI-heat relevance: dropping the `mfi > 46` exit conjunct (pure 2σ-upper-reclaim exit, same entry/risk) must not improve net expectancy; fail ⇒ the money-flow heat leg adds nothing over the bare band reclaim.
- F2 — Entry-softness relevance: hardening the entry rail to the 2σ lower band (same exit/risk) must not improve net expectancy; fail ⇒ the soft 1σ dislocation adds nothing over a tail-only dip.
- F3 — Trailer relevance: disabling the trailer (ROI ladder plus fixed stop plus signal exit only, same entry) must not improve net expectancy; fail ⇒ the trailing leg adds nothing over the fixed risk stack.

## Crypto portability

BTCUSDT Binance perpetual `15m` is the research pin (source names no market; its comments show a spot example and an altcoin list — neither adopted, neither claimed as equivalent). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting (`binance_spot_candles` exists in the same verified feed registry). No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Volume is a native candle field on the venue (`volume_bt` carried through the verified market-data path); no exotic feed is required. Funding is declared nowhere in the source and modeled only downstream by house assumptions (modeled, never realized/canonical, never zero).

## Limitations

- TA-Lib RSI/MFI/EMA and vendored `qtpylib` Bollinger internals live in their libraries outside the pinned file — pinned by call with explicit periods/windows/sigmas (defaults 14 disclosed where the file passes none), not re-derived; exact reproduction inherits those modules' seeding and rolling semantics under the disclosed 999-bar floor.
- The sixteen hyperopt declarations mark the constants as search-derived, but the pin ships no training window, dates, pair list, or cost basis — this record freezes them as literals and performs no training; any retuned point is a different, unpinned rule no reviewer may invent.
- The four-rung ROI ladder rides the controller-carried TP schedule against the simulator's scalar-`take_profit` barrier primitive (strict-`>` on close-based pnl per rung) — the schedule form is the predeclared derivation, never a file literal.
- The file's `trailing_only_offset_is_reached = False` live-arming nuance is scoped to the pinned path's trigger-gated bar-close ratchet (verified code); live intrabar arming behaviour is out of scope and never claimed.
- Engine-reference skew disclosed: the traceable engine source pin reads `hummingbot/VERSION = 2.17.0` (matching the README version contract) but its `setup.py` package lineage reads `20260922`, two days off the README `20260920` package tag — the paths and semantics cited were read at the stated commit and stand on their own; the tag skew is flagged, not hidden.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close MARKET convention on the verified taker path; this record makes no claim about any live-order behaviour.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/Bandtastic.py
- https://github.com/freqtrade/freqtrade-strategies
