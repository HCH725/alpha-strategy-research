---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven SuperTrend Wilder-band flip long-flat on BTCUSDT 1h bars
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-21
sources:
  - https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/supertrend.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven SuperTrend Wilder-band flip long-flat on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-roc`, `forven-ema-cross-adx-regime`, `forven-dema-cross`, `forven-tema-cross`, `forven-hma-cross`, `forven-macd-cross-adx-regime`, `forven-ppo-zero-gated-cross`, `forven-donchian-regime-breakout`, `forven-keltner-adx-gated-breakout`, `forven-parabolic-sar-cross`, `forven-rsi-boundary-rejection`, and forty further Forven-sibling records on `main`).
- Pinned commit SHA: `0a8b07fd02ac6864c0102fec08b6ae7ebfa32875` (committed `2026-10-21T13:26:22Z`; verified as the repository HEAD via `git ls-remote` and via the GitHub commits API during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/supertrend.py`.
- GitHub blob SHA at the pinned commit: `9cd80b4057299acad92a52c9fbee6752c37c20e7`, size 2970 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2970 bytes, 74 lines, SHA-256 `b20e5bcde7d1f679a3d79ec9d5b5e2c48ce273d2d47b21e542e1f6756f138ab2`, identical to the GitHub blob (`git hash-object` reproduces `9cd80b40…37c20e7`); a second independent fetch this cycle is byte-identical — the entire file was retrieved and inspected.
- Registration: the file defines class `SuperTrendStrategy(BaseStrategy)` (the only class in the file), `TYPE_NAME = "supertrend"` (line 5), `STRATEGY_CLASS = SuperTrendStrategy` (line 73), and the single-leg `STRATEGIES = [("TOMB-SUPERTREND", SuperTrendStrategy, {"_asset": "BTC"})]` roster pin (line 74). No pool record cites this source file (see pre-write dedup below).
- The file's own words (quoted for gate evidence, never extended): module docstring `SuperTrend strategy.` (line 1); `describe()` returns `Buys when price crosses above SuperTrend ({atr_period}, {multiplier}), sells when crosses below.` (line 23); `default_params` returns exactly `{ "atr_period": 10, "multiplier": 3.0, "leverage": 3.0 }` (line 16); `compatible_regimes` returns `{"TREND_UP", "TREND_DOWN"}` (lines 17–19, metadata never read by the signal path — both decision methods take only `df` plus `self.params`); `parameter_space()` returns `{ "atr_period": (10, 20, 5), "multiplier": (2.0, 4.0, 0.5) }` (lines 70–71, a documented search surface only — this record pins the defaults and runs no search). The vectorized twin `generate_signals()` (lines 25–51) is declared `the SINGLE source of entry/exit logic`: it resolves `compute_indicator(df, {"id": "st", "kind": "supertrend", "params": {"length": p.get("atr_period", 10), "mult": p.get("multiplier", 3.0)}})` (lines 42–46), reads `direction = out["st_dir"]` (line 47), lags once `prev_dir = direction.shift(1)` (line 48), and prints `entry = (prev_dir < 0) & (direction > 0)` / `exit_ = (prev_dir > 0) & (direction < 0)` with `.fillna(False)` (lines 49–51). The scalar `generate_signal()` (lines 53–68) calls that same twin (line 62) and returns `Signal(entry_signal=bool(entries.iloc[-1]), exit_signal=bool(exits.iloc[-1]), price=round(curr_close, 4), direction="long", confidence=1.0, indicators={"atr": ...})` (lines 64–67) — one shared algorithm, no twin-consistency question. The file's own parity NOTE (lines 33–37) documents that a previous basic-band-cross body (`close > hl2 + mult*ATR`, which sits above the bar's own high and can essentially never trigger) was non-functional and replaced by this final-band state machine. No performance phrase of any kind ships anywhere in the 74 lines — this record adopts no source-reported performance (see Evidence).
- Same-pin lineage for the two out-of-file calls (both resolved by name at the same commit, both read end to end this cycle): `forven/strategies/indicators.py` (blob `fdda8b77429e133372482e25cdff8ea31bd59b2a`, 35784 bytes, 884 lines, SHA-256 `0841cf6e…1ffc0c`, byte-identity verified via `git hash-object`) defines `_f_supertrend` (line 464): Wilder-RMA ATR (`_atr_wilder` = `_rma(_true_range(df), n)` with `_rma` = `ewm(alpha=1/n, adjust=False, min_periods=n)`, lines 157–161), `hl2 = (high + low) / 2`, basic bands `hl2 ± mult*ATR`, and a strictly causal forward loop (`for k in range(n)`, referencing only `k` and `k-1`): bands seeded from the prior bar with fallback to the current basic band while ATR is still NaN, `direction` seeded `-1.0` on bar 0 / NaN bands, then `direction[k] = -1.0 if close[k] < final_lower[k] else 1.0` when previously bullish else `1.0 if close[k] > final_upper[k] else -1.0`, emitting `{st, st_dir, st_upper, st_lower}` with `compute_indicator` dispatching `kind: "supertrend"` to exactly this function (line 696–698). `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`, 12238 bytes, 361 lines — byte-identical to the blob already pinned by the admitted ROC sibling) defines the `Signal` dataclass (`entry_signal` / `exit_signal` default False, `direction` default `"long"`, lines 66–80); the file's single `direction="long"` literal (line 66) therefore survives untouched on every bar.
- Full-file token census (verified by search over the 74 lines this cycle): `direction=` occurs exactly once (the `"long"` literal — no short leg exists); 0 `short` anywhere; the 2 `sell` hits are the prose word inside the `describe()` string and the docstring intent quote (lines 23, 29 — no order-gating synonym); 0 `stop` / 0 `limit` / 0 `profit` / 0 `loss` / 0 `trail` / 0 `qty` (no order arguments, no live risk legs of any kind); 0 `fee` / 0 `slippage` / 0 `commission` (no economics beyond the `leverage: 3.0` default, replaced below — see Execution assumptions); 0 `volume` / 0 `funding` / 0 `mark_price` / 0 `request` / 0 `security` / 0 `timeframe` in any line, and 0 `open`-series reads anywhere (the rule reads `df["close"]` once at line 56 for the price echo; `high`/`low` enter only inside the same-pin `_f_supertrend` quoted above — the 3 `high`/`low` substring hits in this file are the prose words "below" (lines 23, 30) and "own high" (line 35)); 0 `pyramid` / 0 `position_size` / 0 `position_avg` / 0 `opentrades` / 0 `openprofit` / 0 `cooldown` (no position-aware state conditions any signal); 0 `resample` / 0 `informative` / 0 `ffill` / 0 `interpolate` / 0 `ewm` / 0 `rolling(` (no lookback helper of its own — the single `.shift(1)` at line 48 is the only lag operator); 0 `hyperopt` (the lone `Parameter` hit is the `parameter_space` def line itself — optimizer metadata, never read by any predicate); 0 negative `shift(-` / 0 `len(`. The 4 `cross` substring hits are the prose words "crosses above/below" (lines 23, 29–30) plus the NOTE's "basic-band cross" (line 33). The scalar path additionally imports the public `atr` facade (line 54, a lazy pure df→Series helper) for the display-only `indicators` dict — no gating line reads it.
- Param fence: the gating path reads only keys present in `default_params` (`atr_period` via `p[...]`/`p.get`, `multiplier` via `p.get`); `leverage` is never read by any signal line (engine-config metadata only). Treating any other key as live, or exercising any `parameter_space` range, would be a different, unpinned rule.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the Forven engine. The source pins the TOMB-SUPERTREND BTC roster leg, the 10/3.0 literals, the Wilder-RMA final-band construction, the flip-edge entry/exit conjunctions, the single shared twin algorithm, and the long-only stance — but ships no venue spelling, no timeframe, no fill-timing flag, no position-sizing rule, no risk leg of any kind, and no entry/exit evaluation ordering beyond its own conjunctions. Researcher-declared adaptations are exactly five: (1) research market/timeframe `BTCUSDT` spot `1h` (the file names no timeframe and no venue spelling; the roster pins `_asset BTC`; the `1h` frame follows the admitted Forven `1h` siblings — frame/venue pin disclosed, never a source claim); (2) completed-bar decisions with same-bar-close market fills (the file returns `price=round(curr_close, 4)` — the decision bar's own close); (3) single-unit/no-add/no-cooldown position pin plus a 60-bar researcher warmup floor (covers the 10-bar RMA seed, the band-loop seeding, and the one-step shift chain with margin); (4) risk explicitly closed out as signal-only exits with every price-level/time leg disabled (the file ships none — recorded as explicitly disabled, never as defaults to be assumed); the file's bare `leverage: 3.0` default is replaced by unleveraged 1x spot exposure with no margin concept; (5) the explicit fixed research cost model below replaces the absent source economics. Every literal, the flip-edge pair, the shared-twin wiring, and the long-only stance are untouched.

Pre-write dedup (2026-10-21): working-tree filename/content search for `TOMB-SUPERTREND`, `builtin/supertrend`, `_f_supertrend`, and `st_dir` returns zero strategy records citing this source file. The pool's only `supertrend` mechanisms are the two Alorse TradingView-sourced records (Supertrend+RSI: Wilder ST(10,3.0) gated by an RSI50 upward-cross with an RSI72 exit leg; StochRSI+Supertrend: ST(11,2) gated by StochRSI K/D oversold cross plus EMA200 — both carry oscillator/trend legs this record never evaluates) and open `research/*` PR #63 (TradingView `VLRj2sG9` SuperTrend STRATEGY: SMA-of-True-Range ATR variant, Multiplier 8.5, `1d` frame — a different smoothing variant, a different band width, a different frame, and an independent source lineage). No closed `research/*` PR (#354 Average, #355 FAdxSma, #356 FMZ-QFL, #357 SmoothOperator, #358 TechnicalExample, #359 FSample) ever carried this source file. Open `research/*` PRs #48 (Larry Williams streak), #49 (Gaussian StochRSI), #89 (Chandelier Exit), #92 (SSL channel), #251 (Swift 2YMA), #304 (Forven CCI oversold-recross), #331 (AdxSmas SMA-cross), #350 (ClucMay72018 BB-discount), #353 (Heracles Keltner-Donchian ratio) trade none of this file's Wilder-final-band flip legs. Not a duplicate, paraphrase, or trivial parameter variant: a pure Wilder-RMA final-band direction-flip edge pair with signal-only exits is a different normalized signal from any RSI/StochRSI-gated, SMA-ATR-variant, or wide-band construction — changing the ATR variant, either literal, the edge-vs-state form, or any leg would each be a different, unpinned rule, and none is admitted here.

## Economic mechanism

### Source-reported

The source claims no behavioural channel beyond its code: ride the bullish SuperTrend regime by buying the bar the final-band direction flips from −1 to +1, and abandon the long the bar it flips back from +1 to −1, on a Wilder-RMA ATR(10) with a 3.0 hl2 envelope. It ships no sample, window, trade count, sizing, fee, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Research interpretation

Pure volatility-band trend rider, long-only, exited by regime failure alone. Unlike single-threshold dip buyers that fire on one oscillator print, entries fire only on the transition bar of a recursive band state machine — a run of consecutive bullish-direction bars enters once on the flip bar and holds silently after, so chop inside the envelope prints nothing. Unlike stop/trailing exits, the position exits only through the reverse flip: there is deliberately no price stop, no target, and no time leg, so a trend that flips late exits late by construction — disclosed, never repaired into a livelier risk ladder. Unlike the pool's SuperTrend cousins, no RSI/StochRSI/EMA leg gates either side: the band state alone opens and closes every round-trip.

## Signal

Exact rule as pinned (any other ATR variant, period, multiplier, source series, strictness, edge-vs-state form, risk leg, fill, frame, book, or leg is a different, unpinned rule). `dir` below is the same-pin `st_dir` series:

```text
tr[t]         = max(high[t]-low[t], |high[t]-close[t-1]|, |low[t]-close[t-1]|)
atr[t]        = RMA(tr, 10)[t]              // ewm(alpha=1/10, adjust=False, min_periods=10); first 9 prints NaN
hl2[t]        = (high[t] + low[t]) / 2
basicU[t]     = hl2[t] + 3.0 * atr[t]
basicL[t]     = hl2[t] - 3.0 * atr[t]
finalU[t]     = basicU[t]                                          if t==0 or isnan(basicU[t])
              = basicU[t]                                          if basicU[t] < finalU[t-1] or close[t-1] > finalU[t-1]
              = finalU[t-1]                                        otherwise
finalL[t]     = basicL[t]                                          if t==0 or isnan(basicL[t])
              = basicL[t]                                          if basicL[t] > finalL[t-1] or close[t-1] < finalL[t-1]
              = finalL[t-1]                                        otherwise
dir[t]        = -1.0                                               if t==0 or isnan(basicU[t]) or isnan(basicL[t])
              = (-1.0 if close[t] < finalL[t] else 1.0)            if dir[t-1] == 1.0
              = (1.0 if close[t] > finalU[t] else -1.0)            otherwise
entry = (dir[t-1] < 0) & (dir[t] > 0)      // enter_long = 1 (flip-up edge only)
exit_ = (dir[t-1] > 0) & (dir[t] < 0)      // exit_long = 1 (flip-down edge only)
guard = NaN prints map to False via .fillna(False); no other seed handling exists
risk  = no take-profit leg; no stop-loss leg; no trailing leg; no time-exit leg — all explicitly disabled
```

- Exact boundaries (pinned semantics): strict `<` / `>` throughout the direction recursion and both flip conjunctions — a close exactly on a final band holds the prior direction (no flip print on equality); the flip tests compare direction states (`±1.0`), never prices, so band-touch equality never synthesizes an edge — disclosed, not smoothed.
- Trade events: `enter_long=1` on flip-up edge bars only, `direction` long-only; `exit_long=1` on flip-down edge bars only. Both legs are EDGE prints (each fires on the transition bar alone — a held regime reprints nothing); either edge can recur across regimes with no one-shot latch in code.
- Mutual-exclusion proof (no tie-break pin required): the entry demands `dir[t-1] < 0 AND dir[t] > 0` while the exit demands `dir[t-1] > 0 AND dir[t] < 0` — jointly unsatisfiable on one bar for any real `dir[t-1]` (and NaN maps both legs to False). No single bar satisfies both legs; the reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and the sole `direction=` literal is `"long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the flip-down signal exit is the sole position-ending path. Stop loss, take profit, trailing stop, and time limit are absent in source and recorded as explicitly disabled — not as defaults to be assumed, and never to be added by repair. `confidence` (constant `1.0`) and the `indicators` echo (`atr` display value) are diagnostic — neither conditions any order line.
- Position rule (predeclared researcher pin): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no position-aware token ships anywhere); a flat book treats exit bars as no-ops; re-entry re-arms on the next flip-up edge after any exit (no cooldown specified — explicitly none, not invented). No DCA/Safety Orders exist in this admission version (see Execution assumptions). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`high`/`low` for TR/hl2, `close` for the recursion and the price echo) with a fixed non-negative one-step lag (no forward reference) — no volume/funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, `ffill`, ewm-seeding outside the disclosed RMA(10), or stop/limit order argument anywhere in the gating path.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low`/`close` for the True-Range/hl2/band/dir paths. No `open` read in the file's own lines, no `volume`, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher pin — the file names no timeframe; the pin follows the admitted Forven `1h` siblings, disclosed, never a source claim). One evaluation per completed bar; every window reads the decision bar and its causal past only (`.shift(1)`); fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher floor, disclosed): the record-rule floor holds 60 one-hour bars flat (~2.5 days). Covers the 10-bar RMA seed (`min_periods=10`), the band-loop NaN seeding, and the one-step shift chain with margin. Coded behaviour underneath: pre-seed NaN bands force `direction = -1.0` and `.fillna(False)` maps NaN flip tests to no-print — so no entry can print before the bands exist; no `fillna`/`ffill` smears seeds forward. No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance **spot**, 1x unleveraged (researcher choice of the `TOMB-SUPERTREND` roster leg — the source roster pins `_asset BTC`; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). Spot is chosen deliberately: no funding, margin, or liquidation concept exists on this path, so no carry term can be silently zeroed (see costs).
- Venue path (specified, read-verified this cycle — not precedent-cited): the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via a `DirectionalTradingControllerBase` controller (`hummingbot/strategy_v2/controllers/directional_trading_controller_base.py`, read-verified in the version-matching 2.17.0 tree) driving one `PositionExecutorConfig` per round-trip (`hummingbot/strategy_v2/executors/position_executor/data_types.py`, read-verified): BUY side, full single-unit amount, `open_order_type = MARKET`, and `TripleBarrierConfig` with `stop_loss = None`, `take_profit = None`, `time_limit = None`, `trailing_stop = None` (all four verified `Optional`, `None`-disabled in code). Entry economics follow `PositionExecutorSimulator.simulate` (same tree, `hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py`, read-verified): a market-open executor enters at its window-first candle's `close` — i.e. the decision candle's own close — accrues close-to-close returns thereafter, and books `2 * trade_cost * filled_amount_quote` in `cum_fees_quote`. Signal exits follow `BacktestingEngineBase.handle_stop_action` (same tree, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, read-verified): the controller's `StopExecutorAction` on the flip-down bar terminates the executor as `EARLY_STOP` at the action timestamp with realized PnL booked — no TP/SL/trailing/time leg participates. No maker-touch, queue, or intrabar-path-dependent fill: the only legs are bar-close-evaluated market entry/exit orders, and entry/exit co-prints are arithmetically impossible (see Signal), so no same-tick open-then-stop ordering exists to verify.
- Decision/availability timestamps (specified): the engine iterates one tick per completed-candle row (`processed_features` loop in the same `BacktestingEngineBase`, read-verified) and the controller's `determine_executor_actions()` runs per tick — so the decision timestamp is the completed `1h` candle's close time, every input (RMA-ATR(10), band loop, one-step shift) is available at that close, and the fill timestamp is that same candle's close. Candle supply rides `CandlesConfig`/`HistoricalCandlesConfig` through `BacktestingDataProvider` (same tree, read-verified; its `info`-endpoint trading-rule/candle fetch needs no credentials), and the `binance` spot connector ships in the version-matching tree (`hummingbot/connector/exchange/binance`). This paragraph is capability evidence read from the specified path this cycle — not a backtest run, not per-candidate parity (reusing verified primitives requires none), and no sibling admission is cited as evidence.
- Sizing/capital/costs (explicit fixed research model — nothing deferred): the source ships no sizing, capital, fee, margin, or funding concept. Fills are market/taker by construction, so `trade_cost = 0.001` per side, pinned to the Binance spot regular-user taker rate `0.100%` (Binance public spot fee schedule, `binance.com/en/fee/trading`, read this cycle); a round-trip books `2 * 0.001 * filled_quote`, exactly the simulator's `cum_fees_quote` formula. Slippage is modeled `0` — the simulator fills exactly at candle close by construction; that is a disclosed modeling assumption, never a market-microstructure claim. Precision/min-notional ride the connector's live trading rules fetched credential-free at run time with the baseline §8 preflight (no invented tick/lot values appear anywhere in this record). FUNDING: no funding leg exists on the declared spot path — nothing is modeled, nothing is zero-filled, nothing is reported as realized; any perpetual/funding/margin/DCA application is a separately declared downstream derivative and is NOT part of this admission version (the single-unit/no-add pin above already excludes it, so no house-overlay conflict can arise inside this record).
- Price-level risk basis: not applicable — no ROI rung, stop, target, trailing, or time leg exists; all economics are close-to-close market fills under the fixed cost model above. No reviewer repair may invent one.
- Concurrency: at most one position per market at any time; the flip-up edge opens the full unit on a flat book; the flip-down edge closes it in full; re-entry after an exit needs only the next flip-up edge (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (74 lines: the module docstring, `TYPE_NAME`, the 10/3.0/3.0 `default_params`, the regime metadata, the `describe()` sentence, the shared-twin `generate_signals` with the `st`-spec/`st_dir`/shift/flip pair, the scalar `generate_signal` with the `round(curr_close, 4)` price echo and the `"long"` literal, the `parameter_space` metadata, and the `TOMB-SUPERTREND` roster pin), plus the same-pin `_f_supertrend` Wilder-final-band machine and `Signal` dataclass quoted above. It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: pre-seed NaN bands force `direction = -1.0` with `.fillna(False)` mapping NaN flip tests to no-print — no entry can print before the bands exist; no `fillna`/`ffill` smears seeds forward. The 60-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no length guard and no `startup_candle_count`, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: strict `<`/`>` fires no flip on a close exactly on a final band (prior direction holds); flip tests compare `±1.0` states, never prices — disclosed, not smoothed.
3. Co-print arithmetic fenced (impossible, proved — not pinned): entry demands `dir[t-1] < 0 AND dir[t] > 0`, exit demands `dir[t-1] > 0 AND dir[t] < 0` — jointly unsatisfiable on one bar, NaN maps both to False. No bar prints both legs; no ordering invented.
4. Initial-direction fence: the loop seeds `direction = -1.0`, so the record starts bearish-assumed — the first entry anywhere requires a genuine up-flip, never a seed artifact; a market that never flips up never opens — disclosed, not repaired.
5. ATR-variant fence (the material cousin distinction): this record's ATR is Wilder-RMA (`ewm(alpha=1/10, adjust=False, min_periods=10)`); open PR #63's TradingView source smooths True Range with a plain SMA and multiplies by 8.5 on `1d`. Different smoothing, different width, different frame, independent source lineage — substituting any of those numbers here would be a different, unpinned rule no reviewer may invent.
6. Cousin records fenced as different constructions (none trades a pure Wilder-final-band flip-edge pair with signal-only exits on `1h`): the two admitted Alorse SuperTrend records each add legs this record never evaluates (RSI50 upward-cross plus RSI72 exit; StochRSI K/D oversold cross plus EMA200 on ST(11,2)); the pool's flip-state, cross-average, and oscillator siblings evaluate no SuperTrend band at all. Not a threshold re-tuning of any of them: moving either literal, changing the ATR variant, converting an edge to a state, adding any exit/risk leg, or changing the frame would each be a different, unpinned rule — none is admitted here.
7. Metadata fenced: `compatible_regimes`, `parameter_space`, `confidence = 1.0`, the `indicators` echo, and the `leverage: 3.0` default are never read by any gating line — no reviewer repair may promote any of them into a leg, and no optimizer range is exercised by this record.
8. Sibling-file fence: every other `forven/strategies/builtin/*.py` file is a separate pin — its constants, legs, exits, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the five declared adaptations (BTCUSDT-spot-`1h` market choice, same-bar-close fills, single-unit/no-add/no-cooldown position pin with 60-bar warmup floor, explicitly-disabled risk legs with 1x unleveraged exposure, fixed `trade_cost = 0.001` research cost model) — all predeclared above. The 10/3.0 literals, the Wilder-final-band machine, the shared-twin wiring, the flip-edge pair, the `round(curr_close, 4)` price echo, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Wilder-RMA ATR(10) / hl2 / Multiplier 3.0 / final-band recursion / flip-up-edge entry and flip-down-edge exit / signal-only risk profile / single-unit long-only / `1h` BTCUSDT spot / same-bar-close fills / `trade_cost = 0.001` are frozen.

- F1 — Flip-edge relevance: entering on every bullish-direction bar (state-holding instead of edge-triggered, first qualifying bar per regime takes the trade, same exit/risk) must not improve net expectancy; fail ⇒ the flip trigger is decorative and the system is a pure regime holder.
- F2 — Reverse-flip exit relevance: holding each entry for a fixed research horizon instead of the bearish-flip close (same entry, same costs) must not improve net expectancy; fail ⇒ the band-failure exit adds nothing over timed holding.
- F3 — Final-band relevance: replacing the final-band state machine with the file's own documented prior body (basic-band cross `close > hl2 + mult*ATR` for entry and its mirror for exit, same literals, same risk) must not improve net expectancy; fail ⇒ the trailing-band recursion adds nothing over the basic envelope. (Expectation, stated upfront: the basic variant essentially never triggers — the file's own NOTE says so — so F3 should pass trivially; it exists to pin the construction choice, not to discover alpha.)

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on any spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Only the `high`/`low`/`close` candle fields are read (venue definition differences move only oscillator inputs, disclosed). No funding, margin, or liquidation concept exists on this path by construction.

## Limitations

- The RMA seeding (`min_periods=10`), pandas `shift`/`fillna` semantics, and the band-loop fallback arithmetic live in libraries outside the pinned file — pinned by call with the file's literal arguments alongside the same-pin `_f_supertrend` body quoted above, not re-derived; exact reproduction inherits those libraries' seeding under the disclosed 60-bar floor.
- A position in a market whose direction never flips down is held indefinitely with no price stop, no target, and no time exit; a market that whipsaws across the bands flip-trades every crossing with the full unit. There is no decay, chop, trend-loss, or further exit beyond the reverse flip — disclosed, not repaired.
- The file declares no order-type plumbing at all — fills are wholly under the derived same-bar-close market convention mapped to the specified `PositionExecutor`/`StopExecutorAction` path above; this record makes no claim about any live-order behaviour.
- Engine evidence in this record is version-matching code-read verification of the specified controller/executor/simulator path, not a backtest run; representative or per-candidate run evidence belongs to downstream research stages, never to admission.
- No signal exit beyond the reverse flip, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/supertrend.py
- https://github.com/judder659/Forven
