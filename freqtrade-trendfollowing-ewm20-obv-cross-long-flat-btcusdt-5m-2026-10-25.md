---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade TrendFollowingStrategy EWM20-cross OBV-gated edge long-flat on BTCUSDT 5m bars
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/futures/TrendFollowingStrategy.py
  - https://github.com/freqtrade/freqtrade-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade TrendFollowingStrategy EWM20-cross OBV-gated edge — independently derived executable research rule

## Provenance and immutable identity

- Primary GitHub identity: repository `freqtrade/freqtrade-strategies` (open-source Freqtrade strategy collection); exact file path `user_data/strategies/futures/TrendFollowingStrategy.py`; class `TrendFollowingStrategy(IStrategy)` (the only class in the file); pinned commit SHA `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`, verified as the repository HEAD via the GitHub commits API during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is 2441 bytes, 69 lines, SHA-256 `6b8f3e272acfd4923539120364b9ddceccc17a385117d12a249dc1460ea53c4f`, identical to the GitHub blob (`git hash-object` reproduces `e14f23ddf1a2bdd003f55fa45430492019be39cb`, size 2441 via the contents API at the pinned commit) — the entire file was retrieved and inspected end to end.
- The file's own words (quoted for gate evidence, never extended): `timeframe = "5m"`; indicators are exactly `dataframe['obv'] = ta.OBV(dataframe['close'], dataframe['volume'])` and `dataframe['trend'] = dataframe['close'].ewm(span=20, adjust=False).mean()`; long entry is `(close > trend) & (close.shift(1) <= trend.shift(1)) & (obv > obv.shift(1))`; long exit is `(close < trend) & (close.shift(1) >= trend.shift(1)) & (obv > obv.shift(1))`; mirrored `enter_short`/`exit_short` legs with `(obv < obv.shift(1))` exist in the file; risk block is `minimal_roi = {"0": 0.15, "30": 0.1, "60": 0.05}` (plus a commented-out `{"0": 1}` alternative), `stoploss = -0.265`, and `trailing_stop = True` with `trailing_stop_positive = 0.05` / `trailing_stop_positive_offset = 0.1` / `trailing_only_offset_is_reached = False`.
- Full-file token census (verified by search over the 69 lines this cycle): 1 `INTERFACE_VERSION` (`3`); 0 `startup_candle_count` (no length guard ships); 0 `process_only_new_candles`; 0 `can_short`; 0 `informative_pairs` / 0 `resample` / 0 `merge_informative`; 0 `position_adjustment` / 0 `leverage` / 0 `custom_stoploss` / 0 `protections` / 0 `cooldown`; 0 `volume` guard besides the OBV input; 0 `fee` / 0 `slippage` / 0 `funding` (no economics anywhere). The `from functools import reduce` import is dead code (0 uses). No performance number of any kind ships anywhere.
- **Not source-native / not a lossless Freqtrade reproduction.** The source pins the `5m` frame, the EWM20-cross-plus-OBV-rise entry/exit edges, the four-part risk block above, and both short legs — but ships no venue spelling, no fill-timing flag, no warmup guard, and no position-sizing rule.
- **All researcher-defined differences/choices, declared in advance:** (1) long-only: the file's `enter_short`/`exit_short` legs are explicitly disabled, never evaluated; (2) the file's entire risk block (three-rung ROI ladder, `-0.265` stoploss, active trailing block) is explicitly disabled — the signal-exit leg is the sole position-ending path, so no profit-trigger definition is required anywhere in this record; (3) fix Binance BTCUSDT **spot** `5m` candles (the file names no market); (4) same-decision-bar **close-price MARKET fills** on completed bars, instead of claiming the source engine's fill convention; (5) fix one `0.001 BTC` base-size position, one-position-only, no DCA, no cooldown; (6) pin the EWM20 recurrence and the OBV-gate reduction below exactly (no TA-Lib/pandas version is relied upon); (7) fix a 60-completed-bar warmup, a declared controller-memory state machine, and the cost/clock model below. No other source-native execution or cost equivalence is claimed.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the single bar where close crosses up through its 20-span exponential average while on-balance volume is rising; sell the single bar where close crosses down through the same average while on-balance volume is still rising; mirror for shorts; a three-rung ROI ladder, a fixed `-26.5%` stoploss, and an active trailing stop backstop every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 69 lines.

### Research interpretation

Research hypothesis only: a close crossing its medium exponential average marks a micro-trend rotation, and requiring simultaneously rising on-balance volume filters out rotations printed on distribution (falling/zero volume-flow). Unlike pure price-cross records, the volume-flow gate must confirm both the entry rotation and the exit rotation — the exit fires only on a down-cross that still carries rising volume, so exhausted down-crosses (volume already fading) hold the position. Unlike dual-EMA-of-OBV records, no average of the volume series is ever crossed or level-compared; OBV enters only through its one-bar increment sign. This is a rotation-plus-flow-confirmation hypothesis, not a breakout order or a guaranteed profit mechanism. No return, Sharpe, win-rate, drawdown, or other independently reproduced statistic is asserted.

## Signal — fully specified derived rule

Data are UTC Binance BTCUSDT spot `open, high, low, close, volume` on **completed** `5m` candles. Only `close` and `volume` enter any predicate. Let bar index `t` refer to the current completed candle, with `t-1` the preceding completed candle. All comparisons are strict except where `<=` / `>=` is written; equalities on a strict leg fail. Define:

```text
alpha      = 2 / 21
trend[first] = close[first]
trend[t]     = alpha * close[t] + (1 - alpha) * trend[t-1]      // exact pandas ewm(span=20, adjust=False) recurrence
obv_up[t]    = (close[t] > close[t-1]) and (volume[t] > 0)      // one-bar volume-flow increment sign; see note
entry_edge[t] = (close[t] > trend[t]) and (close[t-1] <= trend[t-1]) and obv_up[t]
exit_edge[t]  = (close[t] < trend[t]) and (close[t-1] >= trend[t-1]) and obv_up[t]
```

- OBV-gate note (exact-equivalence reduction, not an approximation): the source compares OBV *levels* (`obv > obv.shift(1)`), so only the one-bar increment sign ever enters any predicate; the OBV level itself is never compared to anything. Under every OBV construction (TA-Lib included), the increment equals `sign(close[t] - close[t-1]) * volume[t]`; hence `obv[t] > obv[t-1]` holds if and only if `close[t] > close[t-1]` with `volume[t] > 0`. The derived `obv_up[t]` gate is therefore exactly event-equivalent on every bar without pinning any OBV seeding or library version. The first bar has no `t-1` and the gate reads false.
- **Independent review correction — unreachable signal exit (source-verifiable, no rule change):** write `C=close[t]`, `P=close[t-1]`, `E=trend[t-1]`, and `a=2/21`. Because `trend[t]=a*C+(1-a)*E` with `0<a<1`, `C<trend[t]` is equivalent to `C<E`. A down-cross additionally requires `P>=E`, hence `C<E<=P` and therefore `C<P`. But `obv_up[t]` requires `C>P` and positive volume. Thus `exit_edge[t]` is identically false for valid nonnegative-volume candles under the declared recurrence. Conversely, an up-cross implies `C>E>=P`, so its rising-close test is already implied; the OBV gate only excludes zero-volume up-crosses. These are algebraic consequences of the pinned source predicates, not researcher-selected alterations. With the source ROI/stop/trailing legs disabled, the effective declared derivative is FLAT until its first eligible post-warmup entry, then indefinitely LONG (including the final bar); it has no reachable signal exit or subsequent re-entry. Claims above of a volume-confirmed exit rotation must be read subject to this correction. No predicate, risk leg, timing, size or terminal-liquidation rule is changed.
- State transitions are evaluated **once after the bar is complete**, using the state carried *into* the bar:
- `FLAT + entry_edge[t]` -> MARKET BUY exactly `0.001 BTC` at that completed bar's close, then `LONG` with entry bar `t`.
- `LONG + (t > entry_bar) + exit_edge[t]` -> MARKET SELL the entire recorded `0.001 BTC` at that bar's close, then `FLAT`.
- Otherwise hold the previous state. A held position never adds, even if a fresh entry edge prints. The entry bar **cannot** be its own exit (additionally enforced by the `t > entry_bar` arm).
- Entry and exit predicates are **logically disjoint**: entry needs `close[t] > trend[t]`, exit needs `close[t] < trend[t]` — no bar can satisfy both, so no same-bar conflict ordering is ever required. A bar with `close[t] == trend[t]` fires neither leg.
- After an exit, a fresh qualifying entry edge on a later bar may enter immediately; no cooldown (the source ships none — explicitly none, not invented).
- All pre-warmup and pre-first-entry bars are FLAT. Missing/invalid candles cause **no signal and no fill**, not synthetic price or forced entry. A zero-volume bar can never satisfy `obv_up[t]`. On the final data bar, a remaining position is reported as open; no fabricated terminal liquidation.
- Direction is LONG/FLAT only; the file's short legs, reverse-on-signal, hedging, simultaneous positions, pyramiding, averaging, safety orders/DCA, ROI ladder, stop loss, trailing stop, take profit, partial exits, stop/limit/maker orders, and time-based exits are all **disabled by this derived specification**. No hidden executor defaults supply any of them.
- The signal-exit arm is unreachable under the declared recurrence and valid nonnegative-volume inputs, so there are no completed signal-exit trades, winning or losing. There is no profit guarantee and no protective stop; an open position can incur unrealized losses indefinitely.

## Required data, warmup, causality

- One market, one `5m` UTC candle feed: `close` (trend construction and both cross edges) and `volume` (flow-gate increment only). No `open`/`high`/`low` reads, no L2, funding, cross-asset, mark/index, calendar events, higher/lower timeframe, or other non-OHLCV data are read by any signal.
- The EWM20 recurrence needs a seed plus one-bar lookbacks for both edges; derived warmup is **60 completed bars** and no trade before it (covers the EWM seeding transient with margin — the `(1-alpha)^n` seed residue after 60 bars is below `0.004`). The EWM uses the stated recurrence with no alternative smoothing, missing-value substitution, or forward fill.
- Every signal on bar `t` depends solely on bars `<= t`. A bar is only made available after its `5m` close; the close is never treated as known at that bar's open. No repainting, lookahead, negative shift, full-sample fitting, future pivot, or partial higher-timeframe candle.
- Equal closes, equal cross comparisons, zero-volume bars, or a close landing exactly on the trend are not entry/exit events.

## Execution assumptions — pinned Hummingbot capability evidence

**Pinned contract:** Hummingbot package `20260920`, `hummingbot/VERSION = dev-2.17.0`, repository `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Read-only inspection of this exact commit (2026-10-25, via the local clone's object store) establishes the following *code-level primitives*, not a strategy-specific live/testnet run:

1. **Data/venue:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `5m` in `INTERVALS`. `binance_spot_candles/binance_spot_candles.py` uses Binance spot klines, passes `interval` to REST (`"interval": self.interval`), parses `row[0]` as candle **open timestamp** (`ensure_timestamp_in_seconds(row[0])`) and parses OHLC plus volume (`row[1..5]`). The research decision clock is explicitly **open_timestamp + 300 seconds**, the completed `5m` bar's effective availability time; raw Hummingbot candle timestamps remain open-time labels and must not be mistaken for close-time decisions.
2. **Fill:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `OrderExecutorSimulator.simulate`: `ExecutionStrategy.MARKET` fills at the first supplied row (`fill_timestamp = df_filtered['timestamp'].iloc[0]`), uses that row's **close** as `entry_price` (`entry_price = df_filtered.loc[fill_timestamp, 'close']`), records `filled_amount_quote = amount * close`, `cum_fees_quote = trade_cost * filled_amount_quote`, and terminates with `POSITION_HOLD`. The engine's raw `fill_timestamp` is the supplied row's **open-time label**; the declared causal event time for audit/parity is the separately normalized close-effective time `open_timestamp + 300`. Neither the engine's raw label nor a close-based fill is represented as an actual exchange execution timestamp. This is a **research backtest convention**, not a live guaranteed close fill.
3. **Controller and ledger:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` executes `update_state(row)` then `controller.determine_executor_actions()` (method pinned on `controller_base.py:465`), accepts `CreateExecutorAction` with `OrderExecutorConfig`, and uses `BacktestPositionHold` to net executed BUY/SELL base exposure and separately accumulate realized gross PnL and fees ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume."). The derived controller's own persistent `FLAT/LONG(entry_bar, Q)` state and fill ledger (not the engine's bounded terminated-executor view or a delayed `positions_held` snapshot) gate entries/exits. A controller implementing exactly these transitions is **not yet implemented** and is a downstream engineering artifact, not a second HB_READY admission criterion.
4. **Cost/position model:** one `Q=0.001 BTC` BUY/SELL unit on Binance **spot**, no leverage/margin/liquidation/futures funding; funding is **not applicable**, not silently set to a fictitious realized zero-funding stream. Pinned backtest fee is `trade_cost=0.001` **per side**, applied to each simulated fill's quote notional; modeled slippage is `0.0` because this pinned MARKET simulator fills at its close input, **not** a claim of actual zero market slippage. Per completed trade, fee-adjusted research PnL is `realized_gross_quote - sum(cum_fees_quote)`; the executor `net_pnl_quote` alone is not accepted as fee-adjusted cash/equity. The simulator uses binary floats for amount*price, no verified exchange tick/lot rounding, so tiny float residues and real-world precision/slippage discrepancies are limitations, not hidden fills.
5. **Timing constraints:** no next-open, intrabar stop, maker queue, partial fill, shared capital, multi-timeframe, or simultaneous multi-asset semantics are required by this derivative. The single-row MARKET-close primitive is reused, and the `5m` `+300s` normalization is mandatory before comparing event timestamps. No missing bar's close is invented; a missing `5m` bar blocks that bar's decision/fill.

These exact engine source paths and restrictions provide **static code-path compatibility evidence** for the defined derived rule. No Qlib/Hummingbot strategy backtest, runtime deployment, trade, or event-level Qlib/HB parity was performed in this Scout cycle. Independent Hermes Auditor must independently verify Gate 5 and all other gates against the pinned code before any merge. Representative engine-path parity remains required before screening if the path is not already validated; PASS is not profitability, Qlib materialization, Survivor, HB Certified or trading authorization.

## Six-gate HB_READY evidence for independent review

1. **Deterministic:** EWM20 exact recurrence with seed, OBV increment-sign reduction (event-equivalent, library-independent), strict cross edges with explicit equality handling, disjoint entry/exit, explicit bar offsets and state priority; all researcher choices pinned above.
2. **Direction:** BTCUSDT Binance spot LONG/FLAT only; the file's short legs expressly disabled.
3. **Entry/exit/risk:** entry on the completed cross-up-plus-flow bar, exit on the completed cross-down-plus-flow bar, no protective/partial/other exit; disabled behaviours enumerated, including terminal position handling. No profit-trigger definition is needed because no ROI/stop/trailing leg exists in this derivative.
4. **State:** one fixed `0.001 BTC` unit, no adds/DCA, no same-bar conflict possible, entry-bar arm, no cooldown beyond it, deterministic transitions.
5. **Engine:** exact Hummingbot package/version/commit, BinanceSpotCandles `5m` feed, controller state, OrderExecutor MARKET-close fill, raw/open vs effective/close timestamps, spot accounting, fee/slippage/precision limitations and BacktestPositionHold netting identified by actual immutable code paths; no unverified specialized execution requirement is introduced.
6. **Causality:** 60 completed-bar warmup, point-in-time completed-bar evaluation, no future access, normalized event times and missing-bar fail-closed behavior.

## Evidence and negative evidence

**Primary-source reported:** `TrendFollowingStrategy.py` at `f3340ce` (69 lines) expressly prints the `5m` frame, the OBV-plus-EWM20 indicator pair, the long entry conjunction (cross-up AND OBV rising), the long exit conjunction (cross-down AND OBV still rising), the mirrored short legs, and the full risk block (three-rung ROI ladder, `-0.265` stop, active trailing). The file ships no market, no fill timing, no warmup, no sizing, and no performance number of any kind — this record claims no source-reported performance.

**Independently reproduced:** None. Static pinned-engine source read only, as detailed above. The file is research-only, not implemented.

**Dedup (main SHA `4deefd8ed820a3559b1ae0e2ec69da1c63475f82`, 2026-10-25):** working-tree filename/content search for `TrendFollowingStrategy` / `futures/TrendFollowingStrategy` returns zero strategy records citing this source file. Existing `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md` is a different source (FMZ strategy 442252) with a different construction — it crosses two averages *of the OBV series itself* (EMA6-over-EMA24 of cumulative volume-flow) and carries a 3% stop with a two-sided book; it never crosses price against a price average and never uses OBV purely as an increment-sign gate. Existing `ema-20-50-cross-btcusdt-1h-2026-10-06.md` crosses two price averages with no volume read at all. Existing `forven-ema-cross-adx-regime-long-flat-btcusdt-1h-2026-10-19.md` gates a price-EMA cross by ADX regime, not by volume-flow increment. Existing `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h-2026-10-12.md` crosses an oscillator of the CLV-based accumulation line — a different cumulative construction with divergence logic. None combines a price-vs-EWM20 cross edge with a one-bar volume-flow increment gate on both legs at `5m` long-flat with no risk legs. All currently open `research/*` PRs were inspected for the same source and mechanism (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant.

**Independent review limitation:** The frozen exit predicate is mathematically unreachable, not merely rare or conditional on a particular market sample. Consequently a valid run has at most one entry and no completed round trip; no baseline realized per-trade expectancy, win rate or completed-trade comparison is defined. The explanatory volume-confirmation hypothesis above does not establish an independent directional filter on positive-volume up-crosses.

**Limitations:** The file's short legs, ROI ladder, stop, and trailing block are deliberately not carried over — this derivative is long-flat signal-exit only and is never evidence that the original full-risk source passes. EWM seeding transient is fenced by the 60-bar warmup; a shorter warmup would admit seed-dependent early events. Close-price fills and modeled fees do not reproduce actual venue microstructure; no spot execution/live approval. The exit requires still-rising volume, so a position can be held through an exhausted fade that never prints a qualifying down-cross. Qlib/Hummingbot event parity and strategy-specific executable artifact remain future, separately authorized work.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EWM20 recurrence as written / OBV increment-sign gate / strict cross edges / disjoint legs / single-unit long-only / `5m` BTCUSDT / same-bar-close fills are frozen.

Review caveat (no experimental rule change): the frozen baseline has no completed round trips because its exit predicate is unreachable. The following proposed comparisons cannot use a baseline completed-trade net expectancy unless a separately specified future experiment defines an appropriate observable; do not invent a terminal sell or silently change the exit to obtain one. F3 changes the effective exit behavior and is a different strategy version, not evidence that this frozen baseline has executable exits.

- F1 — Flow-gate relevance: entering/exiting on the bare EWM20 cross edges with the `obv_up` conjunction removed (same exit, same pins) must not improve net expectancy; fail ⇒ the volume-flow confirmation adds nothing over the naked cross.
- F2 — Average relevance: replacing the EWM20 recurrence with a simple 20-bar SMA (same edges, gate, and pins) must not reproduce-or-beat net expectancy; fail ⇒ the exponential weighting adds nothing over the arithmetic mean and the record is a label variant of an SMA-cross.
- F3 — Exit-gate relevance: exiting on every cross-down bar regardless of the OBV gate (same entry) must not improve net expectancy; fail ⇒ requiring still-rising volume on the exit adds nothing over the naked opposite cross.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT `5m` completed bars with `close` and `volume` fields only. No session calendar (crypto trades continuously; the EWM recursion and the one-bar lookbacks need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every lookback bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; no displayed price precision changes any event. The long-only book expresses identically on spot (no margin needed) and on perpetual under a house overlay; it is the same rule on both.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.
