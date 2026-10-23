---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven VWAP32-distance EMA96-regime RSI-gated pullback long-flat on ETHUSDT 15m bars
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-23
sources:
  - https://github.com/judder659/Forven/blob/81d40ebc2ca065d949f0343491b2a9cdade8b581/forven/strategies/builtin/vwap_pullback_eth_15m.py
  - https://github.com/judder659/Forven
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven VWAP32-distance EMA96-regime RSI-gated pullback long-flat on ETHUSDT 15m bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project; the same repository that supplied the fifty admitted Forven records, including the `forven-vwap-pullback-distance` sibling that pins the bare VWAP-distance cousin file).
- Pinned commit SHA: `81d40ebc2ca065d949f0343491b2a9cdade8b581` (committed `2026-10-23T17:51:51Z`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Exact file path: `forven/strategies/builtin/vwap_pullback_eth_15m.py`.
- GitHub blob SHA at the pinned commit: `c384b9b99888c0ebe3d585d680f23dfa3d04ce05`, size 6827 bytes.
- Byte-identity check: the file downloaded via the raw artifact URL at the pinned commit is 6827 bytes, 188 lines, SHA-256 `702c2b07911e1bb795f6201fdf548257ed8d3a490993c8cc6f26b2ba65506eba`, and `git hash-object` reproduces the GitHub blob (`c384b9b9…4ce05`) — the entire file was retrieved and inspected.
- Registration: the file defines class `Eth15mVWAPPullbackStrategy(BaseStrategy)` with `TYPE_NAME = "vwap_pullback_eth_15m"` and an explicitly EMPTY roster `STRATEGIES: list[...] = []` — no venue row ships anywhere, so the market spelling below is a disclosed researcher choice, never a source claim. Identity here is class plus file path plus `TYPE_NAME`, all unique.
- The file's own words (quoted for gate evidence, never extended): `default_params` returns exactly `{ "_asset": "ETH", "timeframe": "15m", "vwap_period": 32, "distance_pct": 0.015, "ema_regime": 96, "slope_bars": 8, "rsi_period": 14, "rsi_entry": 35, "rsi_exit": 60, "leverage": 1.0 }`; `data_requirements()` declares `timeframe "15m"` with `min_bars = max(warmup + 100, 500)` (= 500 under defaults); the guard is `warmup = max(vwap_period, ema_regime, rsi_period, slope_bars) + 2` (= 98) returning the explicit no-signal `Signal` below it, plus a second explicit no-signal `Signal` when any of `vwap`/`ema_regime`/`rsi` is NaN; entry is `distance_to_vwap >= distance_pct AND trend_ok (close > ema_regime) AND ema_rising (ema_regime > ema_regime.shift(slope_bars)) AND rsi < rsi_entry`; exit is `close >= vwap OR rsi > rsi_exit OR close < ema_regime`; every return hardcodes `direction="long"`; the vectorized twin returns the same four-leg AND / three-leg OR over the shared `_indicator_frame` with `.fillna(False)`; `describe()` states "Buys when price trades at least 1.50% below rolling VWAP(32) while price stays above a rising EMA(96) and RSI(14) is below 35. Exits back at VWAP, on RSI recovery above 60, or when price loses the regime EMA." No performance phrase of any kind ships anywhere in the 188 lines.
- RSI definition pinned in-file-chain (actually read): the file imports `rsi as compute_rsi` from `forven/strategies/indicators`, whose lazy facade resolves to `forven/scanner.py` `def rsi(series, period=14)` — Wilder's RSI, quoted verbatim: `gain = delta.clip(lower=0).ewm(alpha=1.0/n, adjust=False, min_periods=n).mean()`, `loss = (-delta.clip(upper=0)).ewm(alpha=1.0/n, adjust=False, min_periods=n).mean()`, `rs = gain / loss.clip(lower=1e-9)`, `return 100 - (100/(1+rs))` — pure `diff`/`ewm` of past closes only, causal by construction, no future reference.
- Base-class semantics pinned at the same commit (actually read): `forven/strategies/base.py` (12238 bytes, blob `27508a2a6b8c546e21adefdb97fc0144fabf881b` — byte-identical to the blob pinned by five admitted Forven siblings) defines `Signal` with `entry_signal: bool = False` and `exit_signal: bool = False` defaults and `direction: str = "long"` default. The file's explicit `direction="long"` on every return needs no default reading.
- Full-file token census (verified over the 188 lines this cycle): `def generate_signal` exactly once plus `def generate_signals` exactly once (the per-bar path and the vectorized twin — no third path); 0 `short` (no short leg, no short identifier anywhere); 0 `open` (the decision bar's own open is never read); `volume` exactly 3 (the `_rolling_vwap` typical-price weighting only); 0 `funding` / 0 `mark_price`; 0 `request` / 0 `security`; 0 `resample` / 0 `informative`; 0 `hyperopt`; 0 `trailing` / 0 `stoploss`; 0 `pyramid` / 0 `position_` / 0 `cooldown` / 0 `max_open_trades` (the position pin below is a predeclared researcher rule, never a file semantic); `timeframe` only inside `default_params`/`data_requirements` (the `15m` pin below is source-declared, never invented). The single `leverage` token is the `"leverage": 1.0` defaults entry — a spot-consistent hint explicitly adopted as unleveraged (see Execution assumptions).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of any live Forven deployment. The source pins the 15m frame, the VWAP32/distance/EMA96/slope/RSI14 35/60 legs with all strictness, the 98-bar guard, the NaN neutral guards, the long-only stance, and the no-stop posture — but ships an empty roster (no venue spelling), no fill-timing flag, and no position-sizing rule. Researcher-declared adaptations are exactly four: (1) research market `ETHUSDT` spot (the defaults name bare `"ETH"`; venue spelling is disclosed, never a source claim); (2) completed-bar decisions at effective time `timestamp + 900s` with MARKET fills at the creation row's close on the cited pinned-engine path — i.e. the execution row after the decision bar, disclosed, never presented as the Forven engine's own timing and never equated with the file's diagnostic `price` field; (3) single-unit `0.01` ETH position pin with controller-memory state machine plus a 200-bar researcher warmup floor (covers the source's own 98-bar guard plus the twin/per-bar agreement transient with margin; see Required data); (4) the pinned research cost model below (fee 0.001/side post-hoc, slippage 0, funding not applicable on spot, no exchange lot/tick quantization in-path) replacing the absent source economics, with the file's `"leverage": 1.0` hint explicitly adopted as unleveraged. This record is therefore never evidence that the original source strategy itself passes.

Pre-write dedup (2026-10-24): working-tree filename/content search for `vwap_pullback_eth_15m`, `Eth15mVWAPPullbackStrategy`, and `TYPE_NAME = "vwap_pullback_eth_15m"` returns zero strategy records citing this source file — the admitted `forven-vwap-pullback-distance` record cites `vwap_pullback.py` (a different file: bare rolling-20 VWAP, distance > 2%, single reclaim exit, no regime/RSI/slope legs). No open `research/*` PR (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI oversold-recross, #331 AdxSmas SMA3/6-cross, #350 ClucMay72018 BB-discount, #353 Heracles Keltner-Donchian band-ratio) trades a VWAP-distance pullback. No closed `research/*` PR ever carried this source file. Not a duplicate, paraphrase, or trivial parameter variant: a four-leg regime/RSI-gated pullback entry with a triple-OR exit from this immutable file is fenced against every VWAP-geometry pool-mate in Negative evidence 6–8.

## Economic mechanism

### Source-reported

The source claims only what its code and `describe()` print: buy the bar that sits at least 1.5% below its trailing 32-bar volume-weighted mean while holding above a rising 96-bar exponential regime line with RSI(14) washed below 35 — a pullback inside an intact uptrend; stand back to flat when price reclaims VWAP, when RSI recovers above 60, or when price loses the regime line. Rolling VWAP uses trailing volume only (`volume.rolling(32)`, zero-volume windows resolve to NA → neutral, never fabricated). No stop, no target, no trailing, no time exit, no sizing, no cost basis ships anywhere — this record adopts no source-reported performance (see Evidence).

### Research interpretation

Uptrend-pullback timer, long-only, state-gated, no veto beyond its own four legs. The 32-bar VWAP is a fast volume-weighted mean with no volatility normalization; the 96-bar EMA plus its 8-bar rising slope is the slow regime lock; RSI35 is the washout gauge. Entries need all four at once — a deep-enough discount that still respects the regime — so vertical ramps (no discount) and regime breaks (lock lost) both sit out. The triple-OR exit is deliberately hair-trigger: any one of reclaim, momentum recovery, or regime loss ends the trade, so most entries become quick reclaim-or-reject round trips rather than holds. Unlike the pool's bare-distance sibling (one 2% leg in, one reclaim leg out — fires on any air-pocket dip with no trend lock), flat here can also mean "discount without regime" or "regime without washout", never just "no discount". The failure mode is plain: in a grinding bleed the regime lock dies and entries stop only after the damage; in chop around VWAP the hair-trigger exit prints repeated enter-then-exit round trips with no cooldown.

## Signal

Exact rule as pinned (any other VWAP length, distance, regime length, slope window, RSI length, threshold, frame, fill, book, or risk posture is a different, unpinned rule). `vwap_t` is the trailing 32-bar typical-price/volume mean; `ema_t` the 96-bar close EMA; `rsi_t` Wilder RSI(14):

```text
vwap_t   = sum(typ_p * vol)_{t-32..t-1...t} / sum(vol)   // trailing 32, causal
ema_t    = ewm(span=96, adjust=False) of close           // causal
rsi_t    = Wilder RMA RSI(14) of close                   // causal, min_periods=14
ready    = positional index >= 97                        // source guard: len(df) >= 98
entry_t  = ((vwap_t - close_t)/vwap_t >= 0.015) AND (close_t > ema_t)
           AND (ema_t > ema_{t-8}) AND (rsi_t < 35) AND ready AND band-defined
exit_t   = (close_t >= vwap_t) OR (rsi_t > 60) OR (close_t < ema_t)   // no ready gate in twin
```

- Trade events: `entry_signal` on a four-leg pullback bar, `direction` long-only; `exit_signal` on any reclaim/recovery/regime-loss bar. A flat book enters one full unit (`0.01` ETH) on an entry bar; a long book exits the full unit on the first exit-leg bar.
- Exact boundaries (pinned semantics): entry distance is non-strict (`>=` 1.5%); `trend_ok`/`ema_rising` strict (`>`, 8-bar shift); entry RSI strict (`< 35`); exit reclaim non-strict (`>= vwap`), exit RSI strict (`> 60`), exit regime-loss strict (`< ema`). A bar 1.499% under VWAP fires no entry; RSI exactly 35 fires no entry; RSI exactly 60 fires no exit; touches hold the prior state — disclosed, not smoothed.
- Mutual-exclusion proof (no tie-break pin required): entry implies `close_t <= 0.985·vwap_t < vwap_t` (positive-price tape; zero-volume windows are neutral, never evaluated), contradicting exit leg 1 (`close >= vwap`); entry implies `rsi_t < 35`, contradicting leg 2 (`rsi > 60`); entry implies `close_t > ema_t`, contradicting leg 3 (`close < ema`). Jointly unsatisfiable on every evaluable bar. Empirically confirmed this cycle: the real rule's twin evaluated over a 700-bar synthetic `15m` grid prints zero co-print bars. The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and every return hardcodes `direction="long"` — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit): the triple-OR leg is the sole position-ending path. Stop loss, take profit, ROI ladder, trailing-stop order, and time limit are absent in source and recorded as explicitly disabled, never defaulted — adverse excursions have no capital guardrail besides the three exit legs (disclosed principal risk). No exit leg reads net profit, fees, or funding — costs change only the performance report, never whether an exit fires (disclosed).
- Position rule (predeclared researcher pin): single-unit (`0.01` ETH fixed base quantity), at most one open position; a positioned book treats further entry-leg bars as hold-no-ops — no pyramiding, no averaging; a flat book treats exit-leg bars as no-ops; re-entry re-arms on any qualifying pullback bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule. No `position_size` / `position_avg_price` / open-trade reference exists in the file, so no position-aware state conditions any signal.
- Determinism note for the reviewer: the rule reads only completed-bar `close`/`high`/`low` (VWAP construction) and `volume` (VWAP weighting only) with fixed non-positive offsets (trailing windows, one 8-bar shift, RSI diff/ewm — no forward reference); the decision bar's own `open` is never read (census zero). No funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. `compatible_regimes` is absent from this file (no such property — nothing to fence); the `STRATEGIES` roster is an empty list, not a rule.

## Required data

- Completed `15m` bars of ETHUSDT spot: `close`/`high`/`low` (VWAP/EMA/RSI construction), `volume` (VWAP weighting only). No `open` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `15m` (source-declared: `default_params["timeframe"]` and `data_requirements()` both pin `15m`; the rule is pure bar-count logic so the pin rides the file itself — no novel-interval confirmation burden attaches).
- Availability mapping (pinned-engine support, not assumed): Binance spot REST kline row `timestamp` is the bar OPEN time (`binance_spot_candles.py` `_parse_rest_candles`, `row[0]`, same pinned engine commit below); the decision effective time for bar `t` is `timestamp_t + 900s` (the bar's close time — exact for contiguous fixed-interval klines). At that instant every input bar `≤ t` is complete: signals read no future, and the controller acts on the next execution row. Contiguity rule (deterministic data rule, disclosed): a bar whose `timestamp` does not equal the previous bar's `timestamp + 900s` (a gap) carries no decision and no fill — the book holds its prior state across the gap; prices are never fabricated, missing bars are never interpolated.
- Warmup (researcher pin, disclosed): 200 completed `15m` bars held flat. Covers the source's own 98-bar guard plus the per-bar/twin early transient (the twin's `close < ema` leg is defined from bar 0 while the per-bar path holds neutral — both paths agree exactly from bar 98 on complete data, verified 602/602 this cycle) plus EWM burn-in margin with room to spare. The file's `data_requirements` `min_bars = 500` is a dataset-size ask (warmup + 100, floored at 500), fenced as distinct from the 200-bar flat-trading floor — neither is presented as the other's semantics. Coded behaviour underneath: trailing windows print NaN until seeded and the file's explicit `isna` guards plus the twin's `.fillna(False)` collapse every undecided per-bar row to neutral — no entry leg can fire early (verified: zero twin entries before bar 98). No repainting, no negative shift, no future bars/extrema, no full-sample normalization. One evaluation per completed bar.

## Execution assumptions

- Research market: ETHUSDT spot, unleveraged (researcher choice on venue spelling — the defaults name bare `"ETH"` and the roster is empty; the file's own `"leverage": 1.0` hint is explicitly adopted as unleveraged; no source-market equivalence is claimed).
- Pinned-engine path (verified this cycle against immutable source, not assumed): Hummingbot package `20260920`, VERSION `dev-2.17.0`, engine commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`HCH725/hummingbot`): spot connector `binance` + `BinanceSpotCandles` feed (`interval` passed straight to the venue; `"15m"` is a member of the pinned `INTERVALS` map) + `OrderExecutor` MARKET + `BacktestPositionHold` netting. `backtesting_resolution` is pinned to `"15m"` — execution candles coincide one-for-one with decision bars, so the `prepare_market_data` backward-merge of `15m` features onto `15m` execution candles aligns row-for-row and no finer-tick early read is possible. MARKET executors fill at the creation row's close (`order_executor_simulator.py`: `fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close` at that row, `POSITION_HOLD` termination) — the execution row on which the controller acts, i.e. one `15m` step after the decision bar's completion at its effective close time, causally available. No maker-touch, queue, or intrabar-path-dependent fill.
- Controller state machine (derived, fully specified — no engine default is relied on for decisions): once per execution row, the controller evaluates the source predicates for the just-completed bar only; flat+entry creates one MARKET BUY for `Q = 0.01` ETH and records long(Q); long+exit creates one MARKET SELL for `Q` and records flat; long+entry is a hold-no-op; flat+exit is a no-op. Exit sizing comes from the controller's own ledger, never from engine timing. Engine `positions_held`/`executors_info` timing (including the one-row hold-conversion lag inside `update_state` and the 3600s terminated-executor view window, `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 3600`) never gates a decision — the design is window-independent by construction, which is exactly what the `15m` (900s) spacing requires. A strategy-specific controller artifact itself is downstream `IMPLEMENTATION_NEEDED` work, never an admission leg; what is demonstrated here is that every required primitive exists on the cited path.
- Sizing/capital/costs (pinned research cost model — defined here, never punted downstream): fee `0.001`/side passed as the engine `trade_cost` and accumulated per fill as `cum_fees_quote` (order sim `cum_fees_quote = trade_cost × quote`); slippage `0.0` pinned (fills land exactly on the engine close); funding not applicable (spot has no funding leg; the file reads no funding — census zero); precision: the cited path applies no quantity or price rounding (`amount × close` floats, no lot/tick step in-path) and the configured quantity is `Q = 0.01` ETH. The simulator explicitly converts `config.amount` to binary float before multiplying by the close, and `ExecutorSimulation` converts the resulting float quote amounts to `Decimal`; binary floating-point rounding dust (observed `0.063000000000000000444…` on a `0.063` fee this cycle) is therefore possible. Exact decimal representability is not claimed. As specified above, controller-memory flat/long state, not the engine hold `is_closed` flag, governs decisions. Trade economics identity: `net = Σ realized_gross − Σ cum_fees_quote`, both primitives produced by the cited path (`BacktestPositionHold.add_executor` accumulates both; `get_position_summary` reports them separately). Explicitly fenced: the engine `net_pnl_quote` summary field is gross-only (it does not deduct hold fees) and `update_state total_pnl` excludes closed holds — neither label is used here as fee-inclusive equity or closed-trade cash; economics come only from the stated identity. No hypothetical zero funding is reported as realized funding — there is no funding on spot to report.
- Leverage/margin/liquidation: none exists on the specified path — spot, unleveraged, no margin account, no liquidation branch, no forced-close state. The file's `1.0` leverage hint is adopted as-is and no perps/isolated-margin accounting is admitted.
- Concurrency: at most one position at any time; single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (188 lines: the `_rolling_vwap` helper, the `default_params`/`data_requirements`/`describe` pins, the lockstep `generate_signal`/`generate_signals` twins over the shared `_indicator_frame`, the `TYPE_NAME`/empty-roster registration, and the ten-key defaults). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Representative engine-primitive validation executed this cycle (2026-10-24, fresh python3.14 venv with pandas/pydantic): the REAL `OrderExecutorSimulator` class, the REAL `ExecutorSimulation` class, the REAL `BacktestPositionHold` class (AST-extracted from the pinned files, unmodified), the REAL `forven.base` module (whole file: `Signal`, `BaseStrategy`), and the REAL strategy file (whole file — only the `indicators.rsi` import is satisfied by a local pure function implementing the pinned `scanner.rsi` Wilder-RMA text verbatim) — hummingbot enum/config/carrier names carried by minimal stand-ins (`TradeType`, `CloseType`, `RunnableStatus`, `ExecutionStrategy`, `ExecutorInfo` with the real `.side`-via-`custom_info` property, `PositionSummary`, `OrderExecutorConfig`), no behavioural stubbing. 641 asserts, all passing:

- V0 file+class facts (7 asserts): `TYPE_NAME`, all ten defaults incl. `timeframe 15m` / `leverage 1.0`, 98-bar guard arithmetic, `data_requirements` 500-bar/`15m` pin, plus the three REAL hummingbot class loads (`OrderExecutorSimulator`, `ExecutorSimulation`, `BacktestPositionHold`).
- V1 MARKET-fill primitive (7 asserts): BUY `0.01` base fills at the creation row's close, `POSITION_HOLD`, `filled_quote = amount × close` exact, `cum_fees = trade_cost × quote` exact, engine `net_pnl_quote` stays `0` (gross-only label, as fenced), executor-info wiring carries fill/fees/side.
- V2 hold-netting primitive (4 asserts): BUY `0.01 @ 3000` then SELL `0.01 @ 3300` at cost `0.001`/side → `net_base` exactly `0`, gross `3.0`, `cum_fees 0.063000000000000000444…` (float dust, as fenced), `net = gross − fees` — the stated economics identity on engine primitives.
- V3 causality/exclusion/loop (616 asserts): twin predicates evaluated on every truncated prefix `df[:k+1]` equal the full-frame evaluation at `k` for all 700 bars (no future read by construction); per-bar/twin agreement 602/602 from bar 98; the early transient is exactly this: 94 twin-exit bars before bar 98 with zero twin entries — all below the 200-bar floor, never traded; zero entry/exit co-print bars; contiguity predicate holds on the synthetic `15m` grid; `t_end = ts + 900s` mapping asserted; the end-to-end derived-controller loop (floor 200, decide-completed-bar → create-next-row → fill-creation-close) executes a full round trip with every fill exactly its creation-row close and positive fee accumulation.
- V4 code-evidence asserts (7 asserts): `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 3600` literal present; MARKET-first-candle comment present; `fill_timestamp`-first-row line present; `POSITION_HOLD` termination present; `"15m"` in `INTERVALS` present; `row[0]` open-time parse present; `merge_asof` backward merge present. Not a performance backtest, not a deployment — a primitive capability check, exactly the once-per-new-requirement validation the contract calls for.

### Negative evidence

1. Early transient fenced: the twin's `close < ema` exit leg is defined from bar 0 (EWMA seeds immediately) while the per-bar path holds explicit neutral below 98 bars and on NaN — 94 twin-exit bars print before bar 98 with zero twin entries. The 200-bar researcher floor holds all of them flat — disclosed, not repaired. Per-bar and twin agree 602/602 from bar 98 on complete data; the floor covers the transient with margin.
2. Exact-touch rule fenced: entry distance non-strict (`>=` 1.5%) with strict regime/slope/RSI legs; exit reclaim non-strict (`>= vwap`) with strict RSI/regime legs. Touches hold the prior state except the two documented non-strict legs — disclosed, not smoothed.
3. Zero-volume quarantine fenced: `volume_sum.replace(0.0, pd.NA)` resolves dead-volume windows to NA → NaN → explicit neutral. No fill, no interpolation, no fabricated VWAP — disclosed.
4. Diagnostic quarantine fenced: `confidence` (distance/threshold ratio on entry bars else 0.0), `price=round(curr_close, 4)`, and the `indicators` dict are envelope decoration read by zero order-gating comparisons; `describe()` is prose, not a rule; the `STRATEGIES` roster is an empty list — adopting any venue row would be researcher invention, never claimed here.
5. Variant menus fenced: `parameter_space()` (vwap 24–40, distance 1.25–1.75%, regime 72–144, slope 4–8, rsi_entry 35–45, rsi_exit 50–60) is a tuning grid read by zero signal lines — this record freezes the ten canonical defaults as written; adopting any grid point would change trade events and is never claimed here.
6. Pool bare-distance sibling fenced: `forven-vwap-pullback-distance-long-flat-btcusdt-1h-2026-10-19` (`vwap_pullback.py`: bare rolling-20 VWAP, distance > 2%, single reclaim exit, no regime/RSI/slope legs, `1h`) differs on every leg count, all three lengths, both thresholds, frame, asset, and immutable source — a 1.5%-discount bar with RSI 40 fires nothing there while firing here (given regime), and a 2%-discount bar with RSI 70 fires there while firing nothing here; not a re-tuning (changing any leg here would be a different, unpinned rule).
7. Pool VWAP-geometry cousins fenced: `forven-vwap-rolling-cross` (cross, not distance), `forven-vwap-pullback-eth-15m` (this record — no other), and the pool's RSI-washout systems (single-oscillator recrosses with no VWAP/regime construction) each trade a different construction — none evaluates a four-leg VWAP-distance/regime/RSI pullback with a triple-OR exit.
8. Pool RSI/threshold cousins fenced: `forven-rsi-boundary-rejection`, `forven-connors-rsi-oversold-recross`, open PR #304 Forven CCI oversold-recross — single-oscillator threshold systems with no VWAP, no regime EMA, no slope leg — different normalized signals, different files.
9. Engine-label fences (answers to known review findings, pre-declared so no repair is ever needed): fee-inclusive cash is never claimed from `net_pnl_quote`; closed-trade equity is never claimed from `update_state total_pnl`; availability is never claimed from open-time labels without the `+900s` mapping; fills are never claimed intrabar or on the decision bar itself (creation-row close is one `15m` step later, stated); the 3600s terminated view is never relied on for position state; `backtesting_resolution` is fixed to `15m` with a once-per-decision-bar event rule, so no finer-tick early read is possible.
10. Derivation boundary fenced: the only non-source-native behaviours are the ETHUSDT-spot venue-spelling pin, the effective-time MARKET creation-row-close fills, the single-unit/controller-memory/warmup pin, the pinned cost model with leverage adopted as unleveraged, and the `+900s`/gap data rule — all predeclared above. The `15m` frame, the 32/96/8/14 lengths, the 1.5%/35/60 thresholds with all strictness, the guards, the long-only stance, and the no-stop posture are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: VWAP32 / 1.5% distance / EMA96 / 8-bar slope / RSI14 35/60 legs with pinned strictness / long-only / no-stop posture / single-unit `0.01` ETH / `15m` ETHUSDT spot / effective-time creation-row-close fills are frozen.

- F1 — Regime-gate relevance: removing the EMA96 regime lock and slope legs (bare VWAP-distance + RSI35 entry, same triple exit, same posture) must not improve net expectancy; fail ⇒ the regime construction adds nothing over the pool's bare-distance sibling and the record is a label variant of one.
- F2 — Exit-leg relevance: replacing the triple-OR exit with a VWAP-reclaim-only exit (same four-leg entry) must not improve net expectancy; fail ⇒ the RSI-recovery and regime-loss legs add nothing over a single reclaim.
- F3 — Threshold relevance: replacing the 1.5% distance with the sibling's 2% threshold (same gates, same posture) must not reproduce-or-beat net expectancy; fail ⇒ the threshold choice adds nothing over the admitted bare-distance rule.

## Crypto portability

ETHUSDT spot `15m` is the research pin (defaults name bare `"ETH"` with `15m`; roster is empty). Long-only with full-unit open/close expresses unchanged on a spot venue with no naked shorting and no leverage. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. Volume weighting uses the venue's own `15m` bar volume, no cross-venue print. Spot has no funding leg, so the funding portability question does not arise; fees/slippage ride the pinned research model, never a venue schedule claim.

## Limitations

- Hair-trigger exits by construction: the triple-OR leg fires on most trend bars, so entries typically become one-bar reclaim-or-reject round trips — disclosed exit profile, not a hold strategy.
- Chop whipsaw: alternating discount and reclaim bars print repeated enter-then-exit round trips with no cooldown and no structural filter — disclosed chop profile.
- Crash-through blindness: a bar that gaps from a discount straight through the regime EMA exits via the regime-loss leg with no stop order to front-run it, disclosed.
- No risk leg: no stop loss, take profit, ROI rung, trailing-stop order, or time limit exists in source — recorded as explicitly disabled; adverse excursions have no capital guardrail besides the three exit legs.
- Downtrend blindness: declines are watched from flat with no short participation — the zero-`short` posture is a stance choice with a return cost in sustained downtrends, disclosed.
- Single-market scope: derived pin is ETHUSDT spot `15m` only; portability to other symbols/timeframes is untested and claimed nowhere in this record.
- Research overlay dependence: fills, sizing, and costs follow the derived pins and the stated economics identity — not the source engine's own semantics, and not the engine summary labels fenced above.
- No trailing, no breakeven, no short leg, no cooldown — all explicitly absent, never to be added by repair.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/81d40ebc2ca065d949f0343491b2a9cdade8b581/forven/strategies/builtin/vwap_pullback_eth_15m.py
- https://github.com/judder659/Forven
