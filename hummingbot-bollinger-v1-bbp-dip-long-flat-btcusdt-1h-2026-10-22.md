---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Hummingbot bollinger_v1 BBP-breakdown dip-buy barrier-exit long-flat on BTCUSDT spot 1h
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-20
sources:
  - https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/controllers/directional_trading/bollinger_v1.py
  - https://github.com/HCH725/hummingbot
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hummingbot bollinger_v1 BBP-breakdown dip-buy barrier-exit long-flat on BTCUSDT spot 1h

## Provenance

Immutable source actually read end to end (primary artifact for every rule citation):

- Repository URL: https://github.com/HCH725/hummingbot (open-source Hummingbot trading-bot monorepo; this record sources one shipped directional controller implementation, not paper prose).
- Pinned commit SHA: `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (committed `2026-09-20T12:10:22Z`; this is the same commit the repository admission contract pins as Hummingbot package `20260920` / VERSION `dev-2.17.0`, so source identity and engine identity are verified against one immutable tree).
- Exact file path: `controllers/directional_trading/bollinger_v1.py` (87 lines, 3674 bytes, SHA-256 `d828f373513f300e88fd94c73c158d32367b9cc8f2b9c45ef024e85861741283`, GitHub blob `afa0d77241972276b88a0e287bbc37e38b6988c1` — raw bytes fetched at the pinned commit and hashed this cycle).
- Registration: the file defines `BollingerV1ControllerConfig` (`controller_name = "bollinger_v1"`) and `BollingerV1Controller(DirectionalTradingControllerBase)`. No other strategy class ships in the file.
- The file's own words (quoted for gate evidence, never extended): `bb_length` default `100`, `bb_std` default `2.0`, `bb_long_threshold` default `0.0`, `bb_short_threshold` default `1.0`, `interval` default `"3m"`; `self.max_records = self.config.bb_length`; indicator call `df.ta.bbands(length=100, lower_std=2.0, upper_std=2.0, append=True)` reading column `BBP_100_2.0_2.0`; `long_condition = bbp < bb_long_threshold`; `short_condition = bbp > bb_short_threshold`; `df["signal"] = 0` default with `1` / `-1` legs; `processed_data["signal"] = df["signal"].iloc[-1]`; `processed_data["features"] = df`.
- Base-class risk defaults inherited unchanged (file `hummingbot/strategy_v2/controllers/directional_trading_controller_base.py` at the same pin, blob `b2381bba1001f8a77f60f7d168e7ed53b1f899cc`): `stop_loss` default `0.03`, `take_profit` default `0.02`, `time_limit` default `2700` (seconds), `trailing_stop` default `None`, `take_profit_order_type` default `LIMIT`, `max_executors_per_side` default `2`, `cooldown_time` default `300`, `leverage` default `20` (with the field prompt's own words: `"Set it to 1 for spot trading"`), `connector_name` default `"binance_perpetual"`. The base `stop_actions_proposal()` returns `[]` — the shipped controller defines no signal exit; exits are the triple barrier only.
- Full-file token census over the 87 lines: 1 `bbands` call; 0 `volume`; 0 `open`; 0 `high` / 0 `low` in the gating path (the signal reads the derived `BBP` column on `close` only); 0 `shift`; 0 negative offsets; 0 `resample` / 0 `merge` / 0 `informative`; 0 `request` / 0 `security`; 0 hyperopt `Parameter`; 0 `position_adjustment`; 0 `custom_stoploss`; 0 `leverage` override; 0 `funding` / 0 `mark_price`. The `short_condition` leg exists in source and is explicitly disabled by this derived record (see declaration below) — never silently kept.
- BBP arithmetic verified to the pinned dependency tree (not assumed): image `setup.py` at the same pin requires `TA-Lib>=0.6.4` and `pandas-ta>=0.4.71b`; `pandas_ta` 0.4.71b0 `volatility/bbands.py` takes the `talib.BBANDS(close, length, upper_std, lower_std, SMA)` branch whenever TA-Lib is installed with its default `talib=True`, and names the column `BBP_{length}_{lower}_{upper}`; `percent = (close - lower) / (upper - lower)` with a zero-range guard. TA-Lib `BBANDS` uses an SMA midline with a population (`ddof=0`) rolling deviation and a lookback of `length - 1`, so the first 99 bars of any run print NaN and the NaN comparisons in the signal legs are false. The record pins this TA-Lib-present branch, which the image requirement guarantees; the pandas-`ddof=1` fallback branch is fenced as not taken.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live `bollinger_v1` deployment. Source-native and kept verbatim: the `BBP_100_2.0_2.0` construction, the strict `< 0.0` long leg, the `100`-bar seeding rule, the `0.03` stop, the `0.02` take profit, the disabled trailing, and the absent signal exit. Researcher-declared adaptations are exactly seven: (1) market `BTC-USDT` on `binance` spot (source default is `binance_perpetual`; spot removes funding and liquidation from the event set); (2) long-only — the source `short_condition` leg is explicitly disabled (spot cannot short); (3) decision frame `1h` (source default `3m`; `1h` is an already-admitted frame); (4) `time_limit = 54000` seconds, i.e. 15 decision bars — this preserves the source default's own 2700 s / 180 s = 15-bar horizon at the new frame, because the raw 2700 s default would time-kill every `1h` position inside its first bar; (5) `max_executors_per_side = 1`, `total_amount_quote = 1000` (the config prompt's own example value; the controller default is 100), `leverage = 1` (the config prompt's own spot instruction), `cooldown_time = 3600`, `take_profit_order_type = MARKET` (the simulator settles barriers at bar closes either way — disclosed, never effect-claimed); (6) run-cost pin `trade_cost = 0.001` per side (researcher conservative pin above the engine default `0.0002`; see Execution assumptions for the fee-in-net mapping); (7) completed-bar decisions with decision-bar-close MARKET fills (the shipped controller evaluates per completed bar through the same backtest loop cited below). This record is therefore never evidence that the original `bollinger_v1` deployment itself passes.

Pre-write dedup (2026-10-22): no pool record cites `bollinger_v1.py`, `macd_bb_v1.py`, `supertrend_v1.py`, or any `controllers/directional_trading/*` file; filename/content search for `bollinger_v1`, `BBP_100`, and `bb_long_threshold` returns zero strategy records. No open `research/*` PR (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) touches a Bollinger-%B state, a Hummingbot controller source, or this file. Bollinger cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The shipped controller buys breakdowns: when the close sits below the lower 100-bar 2σ band (`BBP < 0`), the per-bar signal is long; when the close sits above the upper band (`BBP > 1`), the per-bar signal is short. The signal is a persistent per-bar state, not a one-bar edge — every qualifying bar prints it. Position-level exits are the triple barrier only (`-3%` stop, `+2%` take profit, `2700` s time limit at default frame, no trailing, no signal exit in the base class). Sizing is `total_amount_quote / price / max_executors_per_side` per created executor.

### Research interpretation

Mean-reversion dip machine, long-only, single-position. The `BBP < 0` state means the market just closed outside its own 100-bar 2σ envelope to the downside; the derived book buys that close and holds through every subsequent bar until a barrier closes it — there is deliberately no signal exit, so a position opened into a persistent breakdown state is held, not flipped, while the state persists. The economics are bar-symmetric by construction: entry always pays the decision close, the stop triggers on a bar-low breach but settles at that bar's close (it can realize better or worse than `-3%` — disclosed), the take profit triggers on a bar close above the `+2%` net line and settles there, and the time limit closes whatever survives after 15 bars. With at most one executor alive, there is no averaging, no pyramid, and no cross-position state to reconcile.

## Signal

Exact rule as pinned (any other band length, deviation, threshold, strictness, state-vs-edge pairing, barrier, frame, or book is a different, unpinned rule):

```text
BBP[t] = (close[t] - L[t]) / (U[t] - L[t])   // TA-Lib BBANDS(close, 100, 2.0, 2.0, SMA);
                                            // U/L = SMA100(close) +/- 2*population-std100(close);
                                            // NaN for the first 99 bars of a run
entry_state[t] = (BBP[t] < 0.0)              // strict; BBP == 0.0 fires nothing; NaN fires nothing
signal[t]      = +1 when entry_state[t] else 0   // short leg explicitly disabled, never -1
risk           = stop_loss 0.03 / take_profit 0.02 / time_limit 54000 s / trailing None
```

- Trade events: on a completed `1h` bar with `signal == +1` and a flat book (no active executor), create one long `position_executor` at that bar's close; hold every later bar (including further `+1` bars — no pyramiding) until exactly one barrier leg closes the full unit. A flat book on a `signal == 0` bar does nothing.
- Exact boundaries: the entry comparison is strict (`< 0.0`) — a bar printing exactly `BBP == 0.0` opens nothing; equality with the band edge is not a fill. The NaN-seeded prefix (first 99 bars) compares false on every leg. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): entries require no active executor while any barrier exit requires exactly one active executor — the two preconditions are complements, so no tick can both open and close; with at most one executor alive there is no same-tick create/stop race and no ordering assumption is needed. The base class emits no stop actions at all, so early exits by signal are structurally impossible, not merely unlikely.
- Direction: long-only. The source `short_condition` (`BBP > 1.0`) is explicitly disabled in this derived record; the position executor side is always `BUY`; the venue is spot. A two-sided reading would contradict this record.
- Exits and risk (explicit and complete): take-profit leg (first completed bar with `net_pnl_pct > 0.02`, settles at that bar's close), stop-loss leg (first completed bar with `low <= entry * (1 - 0.03)`, settles at that bar's close — better or worse than `-3%` by construction), time-limit leg (`54000` s after the entry tick, settles at the last bar at or before the deadline). No trailing (`None`), no signal exit (the base proposal is empty — explicitly none, not invented), no breakeven move — explicitly none further.
- Position rule (researcher pins, all disclosed): at most one active executor per market (`max_executors_per_side = 1`); a positioned book ignores further entry states (no averaging — independent single-executor sims have no averaging path); a flat book ignores barrier legs trivially; re-entry re-arms on the first tick after the prior executor terminates, requiring only the entry state again (no cooldown beyond the native formula, whose flat-book vacuity is disclosed in Execution assumptions). Pre-seed and pre-signal bars are flat by record rule.
- Determinism note: the rule reads only completed-bar `high`/`low`/`close` (100-bar rolling SMA/deviation, fixed non-negative window, no forward reference); the decision bar's own forming values are never read. No `open` read, no bar `volume` read, no funding/OI/mark-price read, no second pair, no second timeframe, no hyperopt parameter, no fitted value anywhere in the gating path.

## Required data

- Completed `1h` bars of BTC-USDT on `binance` spot: `high`/`low`/`close` only (bands on `close`; stop leg on `low`; take-profit leg on `close`). No `open` read, no `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, or session state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher adaptation of the source `3m` default). One evaluation per completed bar; every window reads the decision bar's causal past only; fills land on the decision bar's own close under the engine mapping below.
- Warmup (source-defined, disclosed): `max_records = bb_length = 100` in the shipped controller; the candles feed additionally pre-fetches `100` bars before run start for seeding; the engine drops NaN-prefix rows before the tick loop, so the first evaluation happens on the first fully-seeded bar and the 99-bar NaN prefix is flat by construction. No repainting, no negative shift, no future bars/extrema, no full-sample normalization, no incomplete-bar reads.

## Execution assumptions

Pinned engine path (all files at commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package `20260920`, VERSION `dev-2.17.0`):

- Controller: a `DirectionalTradingControllerBase` subclass implementing the pinned `bollinger_v1` signal (`signal ∈ {0, +1}`) with config `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `interval = "1h"`, `max_executors_per_side = 1`, `cooldown_time = 3600`, `leverage = 1`, `stop_loss = 0.03`, `take_profit = 0.02`, `time_limit = 54000`, `trailing_stop = None`, `take_profit_order_type = MARKET`, `total_amount_quote = 1000`. The base `triple_barrier_config` property hard-codes `open_order_type = MARKET` and `stop_loss_order_type = MARKET` / `time_limit_order_type = MARKET`, so every fill in this record is a taker fill by base-class construction.
- Connector/venue: `binance` spot. The backtest data provider's supported connector types include `CLOB_SPOT`, and `binance` is not on its excluded-connector list, so the spot candle feed and spot trading-rules paths are the modeled ones. Spot has no funding leg and, at `leverage = 1` long-only, no liquidation leg — there is no funding term to pin and nothing is recorded as realized zero.
- Decision/fill timing (cited, not assumed): the engine tick loop runs `update_state(row i)` then `determine_executor_actions()`, and a created executor is simulated over the window starting at row `i` itself; the position-executor simulator with a MARKET open order starts at that window's first timestamp and sets the entry price to that bar's `close`. Hence a decision on completed bar `i` fills at bar `i`'s own close — causal, because the close is already known at the decision tick. Run pin `backtesting_resolution = "1h"` makes ticks coincide with completed decision bars one-for-one.
- Barrier settlement (cited engine-native semantics, disclosed): take profit fires on the first completed bar whose close implies `net_pnl_pct > 0.02` (i.e. gross about `+2.2%` at the pinned costs — the trigger is measured on the fee-inclusive line); the stop fires on the first completed bar with `low <= entry * 0.97`; the time limit fires at the last bar at or before `entry_tick + 54000 s`; every barrier leg settles at its firing bar's close and the earliest of the candidate bars wins, with deterministic `TAKE_PROFIT` / `STOP_LOSS` / `TIME_LIMIT` precedence in that tie order. No intrabar touch prices are realized — only bar closes settle.
- Costs (pinned, with settlement mapping): `trade_cost = 0.001` per side, passed to `run_backtesting`. The simulator books `-2 * trade_cost` directly inside each executor's `net_pnl_pct` line and reports `cum_fees_quote = 2 * trade_cost * filled_amount_quote` alongside, so the engine's own `net_pnl_quote` is already net of both legs' fees — the record defines strategy net as exactly that engine output and separately reports the engine's `total_fees_quote` for audit. There is no slippage term anywhere in the cited 88-line simulator (verified absence — sim-native zero slippage, disclosed, never a venue claim). There is no amount/price quantization, minimum-notional, or balance check anywhere in either cited simulator path (verified absence), so fills are unconditional at the cited closes; venue tick/lot/minimum/rounding behavior is flagged as having no modeled path and is out of scope for this research-only record — no failure behavior is claimed for it.
- Sizing/capital (native formula, no overlay): each created executor takes `amount = total_amount_quote / MidPrice / max_executors_per_side` = the full `1000` USDT notional at the decision close (the provider's mid price is that tick's `close` by engine construction). No compounding (fixed `1000` per position), no averaging, no DCA executor (the create proposal always builds a `position_executor` config — the DCA/grid/order simulator dispatch is never invoked on this path), no shared portfolio state, single pair. Summary percentages use the pinned `total_amount_quote = 1000` denominator.
- Concurrency and re-entry (native gates, read exactly): creation requires `signal != 0`, zero active same-side executors, and the native cooldown inequality; with `max_executors_per_side = 1` the active-count gate dominates while positioned, and after a close there are no active executors so the cooldown term is vacuously satisfied — this vacuity is a reading of the cited formula, and the record claims no cooldown binding that the formula does not produce. A terminated executor leaves the active set on the next tick's executor-info pass, so the earliest re-entry is the tick after termination, on a fresh entry state. No `StopExecutorAction` is ever emitted on this path (there is no stop proposal to emit one), so `keep_position` routing and the pending-hold queue are never touched — position holds stay empty and the engine's `total_pnl` on this path equals executor realized PnL exactly.
- Interval precedent (disclosed, not assumed): `1h` rides existing pool precedent as a decision frame; this paragraph claims no engine capability — every capability above is cited to the pinned files.

## Evidence

### Source-reported

The file ships the full construction (87 lines: the `BBP_100_2.0_2.0` call, the strict `< 0.0` long leg, the `> 1.0` short leg, the `signal ∈ {0, +1, -1}` state, the `100`-bar seeding rule, the `bollinger_v1` controller name, and the inherited `0.03` / `0.02` / `2700` s / no-trailing barrier defaults). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: the first 99 bars print NaN `BBP` and every strict comparison on NaN is false, so no leg can fire early; the engine's NaN-row drop additionally holds the pre-seed prefix out of the tick loop. The file ships no `startup_candle_count` because the shipped controller seeds via `max_records` instead — quoted mechanism, never filled in from elsewhere.
2. Exact-touch rule fenced: entry is strict (`< 0.0`) — a bar printing exactly `BBP == 0.0` opens nothing; the take-profit comparison is strict (`> 0.02` on the fee-inclusive line) while the stop comparison is inclusive on the breach (`low <= 0.97 * entry`). Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Dead-short-leg fence: the source `short_condition` and the `-1` signal value exist in the file but are explicitly disabled in this derived record (long-only spot). They must never be re-enabled by repair; a two-sided variant would be a different, unpinned rule.
4. No-signal-exit fence: the base `stop_actions_proposal()` is empty in the pinned tree — the absence of a signal exit is a source fact, and holding through adverse `signal == 0` bars until a barrier is the specified behaviour, never a gap to be repaired with an invented exit.
5. Take-profit-order-type fence: the record pins `MARKET`, but the cited simulator settles barriers at bar closes without consulting the take-profit order type — the pin is a cost-assumption alignment (taker), and flipping it to `LIMIT` would not change any modeled event. Disclosed, not effect-claimed.
6. Time-limit rescaling fence: `54000` s is a researcher adaptation preserving the source default's own 15-bar horizon (`2700 / 180`) at the `1h` frame — the raw `2700` s default is not kept, and neither value may be substituted by repair without changing the specified rule.
7. Cousin records fenced as different constructions (none trades a `BBP_100_2.0_2.0 < 0` persistent long state with barrier-only exits): the admitted `bollinger-band-breakout-long-midline-exit` pool-mate trades an upside band breakout with a midline exit (opposite direction, opposite exit); the admitted `sideways-dmi-bollinger-breakout` pool-mate trades a DMI-gated breakout (breakout, not breakdown-dip); the admitted `forven-bb-edge-fade-reclaim` pool-mate trades an edge print plus a reclaim confirmation (two-leg confirmation, never a raw sub-zero state); the admitted `forven-bb-squeeze-breakout` / `forven-bollinger-s00120-rsi-breakout` / `forven-bollinger-s026-trend-breakout` pool-mates trade squeeze or RSI-conjunction variants (different gates, different exits); the admitted `freqtrade-bband-rsi-dip-buy` pool-mate requires an RSI conjunction the pinned file never reads; the admitted `freqtrade-combined-binh-cluc` pool-mate trades a dual-leg penetration with microstructure guards; the admitted `chartart-bollinger-rsi-double-joint-cross` pool-mate trades a joint cross (edge, not state). Not a threshold re-tuning of any of them: moving the band length, the deviation, either threshold, converting the state to an edge, adding any conjunction leg, or changing any barrier, the frame, or the book would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `macd_bb_v1.py` (BBP-plus-MACD conjunction, different signal), `supertrend_v1.py` (ATR-based direction latch, different indicator family), `bollinger_v2.py` / `bollingrid.py` / `dman_v3.py` (separate shipped controllers, separate pins) are different sources — their constants, legs, and configs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the `BTC-USDT` spot market choice, the disabled short leg, the `1h` frame, the `54000` s time limit, `max_executors_per_side = 1`, `total_amount_quote = 1000`, `leverage = 1`, `cooldown_time = 3600`, `take_profit_order_type = MARKET`, the `trade_cost = 0.001` pin, and the decision-bar-close fill reading — all predeclared above. The `BBP_100_2.0_2.0` construction with all its literals and strictness, the persistent-state (not edge) posture, the `0.03` stop, the `0.02` take profit, the disabled trailing, and the absent signal exit are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `BBP_100_2.0_2.0` / strict `< 0.0` state / long-only / `0.03` stop / `0.02` take profit / `54000` s limit / no trailing / no signal exit / single-unit / BTCUSDT spot `1h` / decision-close fills / `trade_cost 0.001` are frozen.

- F1 — Dip-state relevance: replacing the `BBP < 0` entry state with an always-enter-when-flat rule (same barriers, same costs) must not improve net expectancy; fail ⇒ the breakdown state adds nothing over blind barrier harvesting.
- F2 — Barrier relevance: removing the take-profit/stop pair (time-limit-only exits) must not improve net expectancy; fail ⇒ the `0.03` / `0.02` barriers add nothing over the entry state plus the horizon cap.
- F3 — Horizon relevance: removing the time limit (barrier-only exits with no horizon cap) must not improve net expectancy; fail ⇒ the 15-bar horizon adds nothing over indefinite barrier holding.

## Crypto portability

BTC-USDT on `binance` spot `1h` is the research pin (the source names no market — its connector default is a perpetual venue, explicitly adapted away). Long-only with full-unit open/close expresses natively on spot with no naked shorting and no margin calls. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing 100-bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding does not exist on the specified spot path.

## Limitations

- The `1h` frame rides existing admission precedent — no novel-interval confirmation burden is claimed or attached to this record (see Execution assumptions for the cited, frame-independent path).
- A position opened into a persistent breakdown state is held through every non-barrier bar by design; a market that keeps printing `BBP < 0` without touching a barrier is simply held, and re-entry after any close needs only the next `+1` bar — there is no chop filter, decay, trend-loss, or signal-based early exit. Disclosed, not repaired.
- The take-profit trigger is measured on the fee-inclusive line, so at the pinned costs it requires about `+2.2%` gross; the stop settles at the breach bar's close, so it can realize better or worse than `-3%` across gaps and intrabar reversals. Both are engine-native settlement semantics — disclosed, not adjusted.
- `BBP` internals (SMA seeding, population-deviation arithmetic, TA-Lib lookback) live in the pinned `TA-Lib>=0.6.4` / `pandas-ta>=0.4.71b` branch cited above alongside the 100-bar floor; exact reproduction inherits those libraries' arithmetic, not a re-derivation. The pandas-`ddof=1` fallback branch would print microscopically different bands and is fenced as not taken.
- The native cooldown formula is vacuously satisfied whenever the book is flat under `max_executors_per_side = 1`; the record claims no cooldown binding beyond the cited formula. No DCA, no grid, no order-executor, no maker, no trailing, no short leg, no signal exit — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/controllers/directional_trading/bollinger_v1.py
- https://github.com/HCH725/hummingbot
