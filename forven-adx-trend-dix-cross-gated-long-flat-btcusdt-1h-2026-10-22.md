---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ADX(14) DI-cross strength-gated long-flat on BTCUSDT 1h spot
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/adx_trend.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ADX(14) DI-cross strength-gated long-flat on BTCUSDT 1h spot

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the admitted `forven-adx-trend-pulse-reclaim`, `forven-ema-cross-adx-regime`, `forven-dema-cross`, `forven-tema-cross`, `forven-hma-cross`, `forven-macd-cross-adx-regime`, `forven-ppo-zero-gated-cross`, `forven-parabolic-sar-cross`, `forven-rsi-boundary-rejection`, and dozens of further Forven-sibling records on `main` — this is the first record pinned to this exact file).
- Pinned commit SHA: `e9a6c096f9bcadbd9a033f06ed7dec31dab50de8` (committed `2026-10-16T13:50:18-03:00`; record `source_as_of` is that commit date, never a fetch date). Repository HEAD has since moved (`455a809329f616d3504fd7328864bd402decc932` on 2026-10-22, verified via `git ls-remote` this cycle); this record pins ONLY the immutable commit above, never floating HEAD. Verified this cycle that `forven/strategies/builtin/adx_trend.py` and `forven/strategies/base.py` are byte-identical between the pinned commit and current HEAD, and that the `adx`/`atr` indicator bodies in `forven/scanner.py` are untouched by the HEAD advance (empty diff grep over `def adx`/`def atr` hunks) — so no newer revision diverges from anything cited below.
- Exact file path: `forven/strategies/builtin/adx_trend.py`.
- GitHub blob SHA at the pinned commit: `b92a9291eca8d3ba522f3bf7f1a1427dd0a9a377`, size 3855 bytes.
- Byte-identity check: the file retrieved via `git show` at the pinned commit is 123 lines, 3855 bytes, SHA-256 `d564098c0195f7630fa259b9a00cae885ac5bbf1b78382640bc610d72b2ca4f6`, identical to the GitHub blob (`git hash-object` reproduces `b92a9291…a377`) — the entire file was retrieved and inspected.
- Registration: the file defines class `ADXTrendStrategy(BaseStrategy)` with `TYPE_NAME = "adx_trend"`, plus module aliases `STRATEGY_CLASS = ADXTrendStrategy` and roster entry `("PREBUILT-ADX-TREND", ADXTrendStrategy, {"_asset": "BTC"})`. Identity here is class plus file path plus pin, all unique.
- The file's own words (quoted for gate evidence, never extended): docstring `Entry: ADX > threshold AND +DI crosses above -DI.` / `Exit: ADX drops below threshold OR -DI crosses above +DI.`; `default_params` returns exactly `{ "adx_period": 14, "adx_threshold": 25, "di_period": 14, "leverage": 1.0 }`; `describe()` returns `Enters when ADX(14) > 25 and +DI crosses above -DI. Exits when ADX falls below threshold or -DI crosses above +DI.` (at defaults); guard `min_bars = max(di_period, adx_period) * 2 + 2` (30 at defaults) returning a flat `Signal(entry_signal=False, exit_signal=False, price=0.0, direction="long", confidence=0.0, indicators={})` when `len(df) < min_bars`; entry `entry = adx_strong and plus_cross_up` with `adx_strong = curr_adx > p["adx_threshold"]`, `plus_cross_up = prev_plus_di <= prev_minus_di and curr_plus_di > curr_minus_di`; exit `exit_ = (curr_adx < p["adx_threshold"]) or minus_cross_up` with `minus_cross_up = prev_minus_di <= prev_plus_di and curr_minus_di > curr_plus_di`; both `Signal` constructions carry the literal `direction="long"`.
- Out-of-file calls pinned (resolved by name through the file's own import line `from forven.strategies.indicators import adx, atr`): the `indicators.py` facade (`forven/strategies/indicators.py`, blob `fdda8b77429e133372482e25cdff8ea31bd59b2a`) exposes `adx`/`atr` lazily via its PEP-562 `__getattr__` hook (`_FACADE_NAMES` includes both names), re-exported from their canonical home `forven/scanner.py` (blob `9a1d77b90bf214c03aa230a5f46775aab94748bd`): `adx(df, period=14)` is the Wilder-style construction (`tr` max-of-three, `dm_pos`/`dm_neg`, `ewm(span=period, adjust=False)` smoothing, `di = 100 * ewm / atr.clip(lower=1e-9)`, `dx = 100 * |di_pos - di_neg| / (di_pos + di_neg).clip(lower=1e-9)`, returned as `dx.ewm(span=period, adjust=False).mean()`); `atr(df, period=14)` is `tr.rolling(period).mean()` (first `period - 1` prints NaN — fenced in Required data). No DB, no network, no order-flow enrichment inside either helper (the scan-time `_enrich_scan_frame` wrapper is not on this file's gating path).
- Signal envelope: `forven/strategies/base.py` (blob `27508a2a6b8c546e21adefdb97fc0144fabf881b`) defines the `Signal` dataclass (`entry_signal`/`exit_signal` bools, `price`, `direction` default `"long"`, `confidence`, `indicators`); its `__post_init__` coerces flags via `_normalize_signal_flag` and resolves direction via `_normalize_signal_direction` (an entry must name its side; non-entry bars keep the long-book reading). Both file literals say `direction="long"`, and no short leg ships anywhere — the envelope never invents a short side here.
- Full-file token census (verified over the 123 lines this cycle): 0 `short` (case-insensitive — no short leg, no short identifier anywhere); 0 `volume` (no volume read — the rule reads `high`/`low`/`close` only); 0 `open` (no open-column read); 0 `shift` (the edge uses `iloc[-1]`/`iloc[-2]` positional reads on completed bars, never a negative-shift call); 0 `resample` / 0 `informative` / 0 `request` / 0 `security` (single timeframe, no external feed); 0 `hyperopt` and 0 hyperopt Parameter classes (no `IntParameter`/`DecimalParameter`/`CategoricalParameter`/`BooleanParameter` anywhere — the single `parameter_space()` method is a documented search surface only: `{ "adx_period": (10, 20, 2), "adx_threshold": (20, 35, 5), "di_period": (10, 20, 2) }`; this record pins the defaults and runs no search, disclosed); 0 `funding` / 0 `mark_price` (no economics beyond direction); 1 `leverage` (the `1.0` default — consistent with the spot/leverage-1 pin below, claimed as consistency only); 2 `long` (the two `direction="long"` literals — guard Signal and live Signal). `confidence` (`min(1.0, curr_adx / 50)`) and `atr_14` are reporting-only indicators payload, never gating legs — disclosed, never promoted into the rule.
- `compatible_regimes` (`{"TREND_UP", "TREND_DOWN"}`) and the `PREBUILT-ADX-TREND` roster tuple are metadata, never gating legs.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the ADX(14) > 25 strength gate, the +DI(14)/−DI(14) cross edges, the 30-bar `min_bars` guard, the long-only stance, and the OHLC-only causal construction — but ships no venue spelling, no fill-timing flag, no position-sizing rule, and no TP/SL/trailing/time legs. Researcher-declared adaptations are exactly five: (1) research market `BTCUSDT` spot (the file's `_asset` default is `"BTC"`; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed); (2) completed-1h-bar decisions with same-row-close market fills on a pinned `backtesting_resolution = "1h"` path (derivation disclosed in Execution assumptions with the full label→availability→decision→fill mapping, never presented as the source engine's own timing); (3) single-unit position pin with hold-no-op semantics plus the source-native 30-bar guard adopted verbatim as the warmup rule; (4) all absent risk legs (TP/SL/trailing/time) explicitly disabled via `None` triple-barrier pins (never invented); (5) sizing/costs ride the explicit house overlay with pinned simulator cost (never hypothetical zero funding — the source declares no funding treatment at all). This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-22): working-tree exact-path search for `builtin/adx_trend.py` (dot-anchored, excluding `adx_trend_pulse.py`) returns zero strategy records — no record in the pool cites this source file; class/alias search for `ADXTrendStrategy` / `PREBUILT-ADX-TREND` (comma-anchored, excluding `-PULSE`) returns zero. No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades an ADX±DI-cross rule. ADX cousins in the pool are fenced as different constructions in Negative evidence 7. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: hold long exposure when trend strength is confirmed (ADX(14) above 25) at the moment buying pressure crosses over selling pressure (+DI crosses above −DI); exit when strength fails (ADX falls below 25) or selling pressure crosses back over (−DI crosses above +DI). The file ships no sample, window, trade count, ROI ladder, stop, or cost basis — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Strength-gated cross machine, long-only. Unlike a bare moving-average cross (which fires in chop), the ADX > 25 gate demands that a directional trend actually exists before the ±DI cross can open exposure — and the ADX < 25 leg exits as soon as that trend dissolves, even without an opposite cross. The failure mode is plain: an ADX that oscillates around 25 whipsaws the book (exit-then-re-enter round trips with no cooldown), while a cross that fires just as strength fades holds the unit until the next exit leg — there is no stop, no target, no trailing, and no time exit, all explicitly absent.

## Signal

Exact rule as pinned (any other ADX period, threshold, DI period, edge-vs-state pairing, exit set, frame, or book is a different, unpinned rule). All periods/thresholds are explicit file literals (`14`/`25`/`14`), never library defaults:

```text
up_move[t]   = high[t] - high[t-1]                    // .diff(), causal
down_move[t] = -(low[t] - low[t-1])                   // .diff(), causal
plus_dm[t]   = up_move[t]  if up_move>down_move and up_move>0 else 0
minus_dm[t]  = down_move[t] if down_move>up_move and down_move>0 else 0
atr_w[t]     = atr(df, 14)[t]                         // scanner rolling-14 TR mean
plus_di[t]   = 100 * ewm(plus_dm, span=14)[t]  / atr_w[t]    // RAW division
minus_di[t]  = 100 * ewm(minus_dm, span=14)[t] / atr_w[t]    // RAW division
adx[t]       = adx(df, 14)[t]                         // scanner Wilder-style ADX
adx_strong   = (adx[t] > 25)                          // strict
plus_cross   = (plus_di[t-1] <= minus_di[t-1]) and (plus_di[t] > minus_di[t])
minus_cross  = (minus_di[t-1] <= plus_di[t-1]) and (minus_di[t] < plus_di[t])
entry        = adx_strong and plus_cross              // edge, strict
exit_        = (adx[t] < 25) or minus_cross           // strict threshold OR edge
guard        = len(df) < 30 -> flat Signal (source-native min_bars)
```

- Trade events: `entry` on a bar printing the gated plus-cross (`direction` long-only); `exit_` on a bar printing sub-threshold ADX or the minus-cross. The cross legs are one-bar edges evaluated on the decision bar's own completed prints (positional `iloc[-1]` vs `iloc[-2]`); a book already positioned treats further entry bars as hold-no-ops under the position pin below, and a flat book treats exit bars as no-ops.
- Exact boundaries (pinned semantics): the ADX gate is strict on both sides (`>` for strength, `<` for weakness) — a bar with `adx == 25.0` fires neither ADX leg (exit then only via a minus-cross); both crosses are strict on the decision bar (`>` / `<`) with a non-strict (`<=`) prior-bar lock. All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `plus_di[t] > minus_di[t]` while any cross-exit bar has `minus_di[t] > plus_di[t]` — mutually exclusive on every bar, so entry and cross-exit never co-print; any entry bar has `adx[t] > 25` while any threshold-exit bar has `adx[t] < 25` — likewise mutually exclusive. Entry and exit therefore never co-fire on any bar, degenerate or otherwise. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero short-leg tokens ship anywhere and both `Signal` literals read `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the ADX-sub-threshold/minus-cross exit pair is the COMPLETE position-closing set. No ROI ladder, no stop, no trailing, no time exit ships anywhere — all four are explicitly disabled in the derived execution (triple-barrier `None` pins, see Execution assumptions), not invented, not defaulted-in. No exit leg reads net profit, fees, or funding — fees change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin over the source-native guard): single-unit, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging); a flat book treats exit bars as no-ops; re-entry re-arms on any qualifying gated-cross bar after any exit (no cooldown specified — explicitly none, not invented; the `cooldown_time = 1` engine pin is disclosed-inert in Execution assumptions). Pre-guard bars (fewer than 30 completed 1h bars) are flat by the file's own rule.
- Determinism note for the reviewer: the rule reads only completed-bar `high`/`low`/`close` (first differences, span-14 EWMs with `adjust=False`, one rolling-14 mean, and positional prior/current reads — no forward reference) under completed-bar evaluation; the decision bar's own forming values are never read. No funding/OI/mark-price read, no volume read, no `request.*`, `security()`, session/calendar call, resample, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. `confidence` and `atr_14` never gate.

## Required data

- Completed `1h` bars of BTCUSDT: `high`/`low` (DM construction, TR, ATR) and `close` (TR). No `open` read, no volume read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1h` (researcher choice — the file names no timeframe; the `1h` frame, like the market, is a derivation step, and no source-timeframe equivalence is claimed). One evaluation per completed bar; every window reads the decision bar's causal past only (plus the decision bar's own completed print); fills land on the decision bar's own close under the derived rule below.
- Warmup (source-native, disclosed): 30 completed 1h bars held flat by the file's own `min_bars = max(14, 14) * 2 + 2` guard. Covers the 14-bar rolling-ATR seed (first 13 prints NaN; every strict NaN comparison is false, so no leg can fire early) with margin. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. The engine's `prepare_market_data` trailing `dropna` additionally drops unseeded leading rows (coded behaviour, disclosed, never relied upon as the warmup).

## Execution assumptions

Pinned engine (all line citations verified this cycle against `hummingbot/hummingbot@fac3a7f8c4adfd9f07f462cfaad9e2ed9e8b6467`, committed 2026-09-20 — the `20260920` / `dev-2.17.0` admission baseline):

- Research market: BTCUSDT Binance SPOT (`connector_name = "binance"`, pair `BTC-USDT`, `leverage = 1` — researcher pins overriding the directional-base defaults of `binance_perpetual`/20×). The source default `leverage: 1.0` is consistent with unlevered spot, claimed as consistency only. Spot is a deliberately chosen derived boundary: no perpetual funding exists on this path, so funding is excluded/unmodeled downstream — never reported as realized zero (the source declares no funding treatment at all).
- Signal candles: the researcher controller overrides the base's default-empty `get_candles_config()` with exactly one `CandlesConfig(connector = "binance", trading_pair = "BTC-USDT", interval = "1h", max_records = 500)` (override hook and `CandlesConfig` shape per `controller_base.py` `get_candles_config`/`initialize_candles_feed`; `max_records = 500` prefetches a `500 × 3600 s` pre-start buffer per `backtesting_data_provider.py` `get_candles_feed`, covering the 30-bar guard and the 14-bar ATR seed).
- Execution resolution (the originating-researcher fix for the prior round's Gate 5/6 blockers): `backtesting_resolution = "1h"` is pinned — the `run_backtesting(..., backtesting_resolution: str = "1m", ...)` default is explicitly NOT used (`backtesting_engine_base.py:221-238`). Execution candles are therefore `1h` candles on the same `1h` frame as the signal candles. `prepare_market_data()` backward-merges features onto execution rows (`pd.merge_asof(..., left_on = "timestamp_bt", right_on = "timestamp", direction = "backward")`, `backtesting_engine_base.py:466-468`); with identical `1h`/`1h` label sets the merge is label-identity — each execution row carries exactly its own bar's completed features, never a younger bar's features on an older execution row. No cross-row early-read exists on this pinned path.
- Label→availability→decision→fill mapping (stated as event times, never as label claims): pinned-candle row labels are kline OPEN times — `binance_spot_candles.py:80-85` keeps `row[0]` as the row `timestamp`, and a live Binance `1h` kline check this cycle confirms the layout (`open 13:00:00Z`, `close 13:59:59.999Z`, OHLC inside). A `1h` bar's complete high/low/close is therefore available only at its close (label + 1h − 1ms). Engine rows represent COMPLETED bars: `update_state` prices the row at its completed close (`prices = close_bt`, `_time = timestamp`, `backtesting_engine_base.py:364-367`). The derived strategy's availability time for bar T's signal is bar T's close; the decision event and the fill event both occur AT that availability time on the engine row carrying bar T's completed data; the row's open-time label is an identifier only and is never claimed to be the availability time. This is the explicit, verifiable completed-bar/same-close model — not a bar-label-as-availability claim.
- Cadence (once per decision bar, structurally): `simulate_execution` iterates the prepared frame one row at a time — `update_state(row)` then exactly one `determine_executor_actions()` call per row (`backtesting_engine_base.py:282-284`), i.e. one decision pass per completed `1h` bar on this pinned path. The researcher directional controller (`DirectionalTradingControllerBase` subclass) emits at most one action per pass: `create_actions_proposal` appends at most a single `CreateExecutorAction` (`directional_trading_controller_base.py:167-181`); the record's controller creates iff the row's entry edge is true AND the book is flat (`max_executors_per_side = 1` researcher pin; `can_create_executor` same-side active/cooldown gate per lines 185-195), and its `stop_actions_proposal` override (the base returns none, line 197-201) emits a single `StopExecutorAction(keep_position = False)` iff the row's exit leg is true AND a BUY executor is active. `cooldown_time = 1` (one second) is pinned solely to satisfy the `gt = 0` field constraint — inert against 3600 s row spacing and the single-position gate, disclosed as no material cooldown, never a throttle.
- Entry fill: market-order `PositionExecutor` fills at its slice's first row close — non-limit path sets `start_timestamp` to the slice minimum (`position_executor_simulator.py:14-15`) and `entry_price` to that row's `close` (line 40); the slice handed to the simulator starts at the decision row (`simulate_execution`, `backtesting_engine_base.py:287`). The config `entry_price` passed by the controller is the same row's close (`MidPrice` from `close_bt` per `backtesting_engine_base.py:366` and `get_executor_config`, `directional_trading_controller_base.py:204-219`) — fill price and quoted price coincide at the decision row's close, i.e. the availability-time price. No maker-touch, queue, or intrabar-path-dependent fill.
- Exit fill: the stop is handled at the current row's timestamp (`handle_stop_action(action, row["timestamp"])`, `backtesting_engine_base.py:291`) and booked with that row's close economics — `get_executor_info_at_timestamp` reads the latest simulation row at or before the timestamp (`searchsorted(timestamp, side = "right") - 1`, `executor_simulator_base.py:29-56`), terminating `EARLY_STOP` with realized PnL at that row's close (`handle_stop_action`, `backtesting_engine_base.py:568-599`). Signal exit and entry never co-print (Signal proof), so no same-row create/stop ordering assumption is needed; any exit row closes the full unit flat.
- Disabled barriers (no intrabar scanning ambiguity): the researcher `triple_barrier_config` pins `stop_loss = None, take_profit = None, time_limit = None, trailing_stop = None` (all `Optional` on `DirectionalTradingControllerConfigBase`; `open_order_type = MARKET` taker default retained). The simulator skips every barrier scan when unset (TP `if ... else None` line 19; trailing lines 22-24; stop `if ...` line 60; time-limit fallback line 25-26) — exits occur ONLY via controller stops at row closes. An executor never stopped terminates `TIME_LIMIT` at the frame's final row close (`close_timestamp = min(...)` over the surviving candidate, line 66) with that row's economics — terminal-row behaviour disclosed, not hidden.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept. Sizing rides the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3×/5× research experiment; no safety-order tranche activates under the single-unit/no-add pin, so position events are fully determined by the entry/exit legs and sizing changes no event — never presented as source-native behaviour); the engine `amount = total_amount_quote / price / max_executors_per_side` with the record's `total_amount_quote = 1000` USDT pin and `max_executors_per_side = 1` (directional lines 171-176). Simulator cost is pinned at `trade_cost = 0.001` per side with the native round-trip `2 × trade_cost` model (`position_executor_simulator.py:45, 49`: cumulative returns less `2 * trade_cost`, `cum_fees_quote = 2 * trade_cost * filled`) and continuous float accounting — zero added slippage, disclosed. Precision/min-notional ride the venue trading-rules path (`initialize_trading_rules`, `quantize_order_amount/price` in `backtesting_data_provider.py`); the baseline §4 runtime preflight plus a 10 USDT order floor applies, sub-floor bars are out of scope, and any silent drop of an in-scope order counts as a breach of this record.
- Interval precedent (disclosed, not assumed): `1h` is an already-admitted interval on `main` via the Forven `1h` pool family — no novel-interval confirmation burden attaches to this frame. `1h` is additionally a natively supported candle interval on this pinned path (`INTERVALS` in `binance_spot_candles/constants.py` lists `1h`). Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path above; fees/funding/precision are pinned downstream and hypothetical zero funding is never reported as realized funding.
- Concurrency: at most one position executor active per market at any time; the gated plus-cross opens the full unit on a flat book; the sub-threshold/minus-cross leg closes it in full; re-entry after an exit needs only the next gated-cross bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (123 lines: the inline ±DM/DI arithmetic, the `adx`/`atr` facade imports with explicit periods `14`/`14`, the strict gated-cross entry, the strict threshold-or-cross exit, the 30-bar guard, the `ADXTrendStrategy` class pin with `TYPE_NAME = "adx_trend"`, and the `PREBUILT-ADX-TREND` roster entry). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Leading-window behaviour fenced: the 30-bar `min_bars` guard returns a flat `Signal` before 30 completed bars — no leg can fire early by file rule. Underneath, the rolling-14 ATR prints NaN for its first 13 bars and every strict NaN comparison is false — coded behaviour, disclosed, never repaired. The engine `dropna` additionally sheds unseeded leading rows.
2. Exact-threshold rule fenced: both ADX legs are strict — a bar printing exactly `adx == 25.0` fires neither ADX leg (exit then only via a minus-cross). Strictness preserved throughout — disclosed, not smoothed.
3. Prior-bar lock fenced: both crosses require the non-strict prior lock (`prev_plus <= prev_minus` / `prev_minus <= prev_plus`) with a strict decision-bar cross — equality-chained bars (`plus == minus` on both bars) deterministically fire neither edge. Coded fact, disclosed.
4. Degenerate-bar fence: zero-ATR bars divide by zero through the file's RAW (unclipped) inline division — `x / 0` yields ±inf, `0 / 0` yields NaN under IEEE semantics; NaN comparisons are false (no leg), inf comparisons follow arithmetic deterministically. No exception path, no invented fill-in: degenerate bars resolve through the coded arithmetic exactly as written. (The scanner-side `adx` helper separately clips at `1e-9`; the inline DI deliberately does not — difference disclosed, never harmonized by repair.)
5. Reporting-vs-gating fence: `confidence`, `atr_14`, `compatible_regimes`, and the exit-column-free prose docstring never gate an order — only `entry`/`exit_` booleans drive the controller. `atr(df, 14)` feeds reporting only; the gating ATR is `atr(df, di_period)` inside the DI denominators.
6. Search-surface fence: `parameter_space()` (periods 10–20, threshold 20–35) is an unrunned hyperopt surface — this record pins `14`/`25`/`14` and performs no search. Substituting any searched tuple would be a different, unpinned rule.
7. Cousin records fenced as different constructions (none trades an ADX(14) > 25-gated ±DI(14)-cross edge pair, long-flat, signal-only exits): the admitted `forven-adx-trend-pulse-reclaim` pool-mate trades a four-way EMA21/EMA55-trend × ADX14 ≥ 18 × 4-bar-pullback-touch × EMA21-reclaim conjunction with close-under-EMA21 exits (`builtin/adx_trend_pulse.py` — a market that prints a bare +DI cross at ADX 26 with price far above EMA21 fires an entry here but nothing there); the admitted `forven-ema-cross-adx-regime` pool-mate gates an EMA cross behind an ADX regime (different trigger leg); the admitted `forven-adx-di-cross-strength-gated-two-sided` pool-mate is two-sided on a different source; the admitted `forven-williams-r-adx-gated`, `forven-keltner-adx-gated-breakout`, and `forven-macd-cross-adx-regime` pool-mates gate different primary legs (Williams %R reclaim, Keltner breakout, MACD cross) behind ADX variants. Not a threshold re-tuning of any of them: moving either period, the 25 gate, converting either edge to a state, adding any risk leg, or changing the frame would each be a different, unpinned rule — none is admitted here.
8. Sibling-file fence: `adx_trend_pulse.py`, `ema_cross.py`, `williams_r.py`, `keltner.py`, `macd.py`, and every other file in `builtin/` are separate pins — their constants, legs, exits, frames, and risk pairs must never be substituted into this record.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot market choice, the `1h` frame choice, the pinned `backtesting_resolution = "1h"` with the label→availability→decision→fill mapping, the single-unit/no-add/no-cooldown position pin, the `total_amount_quote = 1000` / `trade_cost = 0.001` / `cooldown_time = 1` / `max_executors_per_side = 1` / barriers-`None` controller pins, and house sizing/costs — all predeclared above. The ADX(14) > 25 gate with all its literals and strictness, the +DI/−DI(14) cross edges, the sub-25/minus-cross exit pair, the 30-bar guard, the causal OHLC-only construction, and the long-only stance are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ADX(14) / 25-gate with pinned strictness / ±DI(14) cross edges / threshold-or-cross exit pair / single-unit long-only / `1h` BTCUSDT spot / same-close fills on the pinned `backtesting_resolution = "1h"` path are frozen.

- F1 — Gate relevance: entering on the plus-cross alone (no ADX > 25 gate; same exits, same costs) must not improve net expectancy; fail ⇒ the strength gate adds nothing over the bare cross.
- F2 — Threshold relevance: replacing the 25 gate with a 20/30 hysteresis band (enter above 30, threshold-exit below 20, same cross legs) must not improve net expectancy; fail ⇒ the coded 25 line adds nothing over its banded twin.
- F3 — Exit-leg relevance: removing the minus-cross exit (threshold-only exits) must not improve net expectancy; fail ⇒ the opposite-cross leg adds nothing over the bare strength-state machine.

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (the file defaults `_asset` to `"BTC"` with no venue). Long-only with full-unit open/close expresses unchanged on a perpetual venue at 1× without naked shorting, but this record specifies spot — no funding leg exists to port. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. High/low/close are native Binance kline fields on both spot and perpetual venues. Funding is declared nowhere in the source and is excluded (not zero-filled) on this path.

## Limitations

- The `1h` frame rides existing admission precedent (Forven `1h` pool family) plus native pinned-path support — no novel-interval confirmation burden attaches to this record (see Execution assumptions).
- A position in a market whose ADX never prints below 25 and never prints a minus-cross is held indefinitely — there is no stop, target, trailing, or time exit by file design (disclosed, not repaired). A market whose ADX oscillates around 25 whipsaws the book across consecutive bars (exit-then-re-enter round trips with no cooldown to damp them — disclosed as the principal friction).
- Facade internals (scanner `adx`/`atr` seeding, EWM initialization, rolling-NaN propagation) live outside the pinned file — pinned by call with explicit period 14 at immutable commit `e9a6c09`, verified untouched by the HEAD advance, never re-derived; exact reproduction inherits that seeding alongside the 30-bar guard.
- The `parameter_space` ranges, `compatible_regimes`, roster tuple, `confidence`, and `atr_14` are metadata/reporting — nothing further to fence.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/e9a6c096f9bcadbd9a033f06ed7dec31dab50de8/forven/strategies/builtin/adx_trend.py
- https://github.com/judder659/Forven
