---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Alorse Trend EMA-RSI triple-EMA cross green-gated long-flat on BTCUSDT 1h
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-25
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/Tendency%20EMA%20%2B%20RSI.pine
  - https://github.com/Alorse/pinescript-strategies
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse Trend EMA + RSI triple-EMA cross green-gated long-flat — independently derived executable research rule

## Provenance and immutable identity

- Primary GitHub identity: repository `Alorse/pinescript-strategies` (open-source Pine collection; the lane that already supplied the twelve admitted `alorse-*` records — this record pins ONLY the Tendency file's literals below, and no reviewer repair may substitute a sibling constant).
- Exact file path: `strategies/trend/Tendency EMA + RSI.pine`; Pine `//@version=5`; class of artifact is a `strategy()` program titled `Trend EMA + RSI [Alorse]`.
- Pinned commit SHA: `8fb3837ddcd137f1450c3e82d654ff3df24d54d5` (committed `2026-08-25T11:48:57Z`, verified as the repository HEAD via the GitHub commits API during this cycle — record `source_as_of` is that commit date, never a fetch date).
- Byte-identity check: the file fetched from the GitHub contents API at the pinned commit is 2334 bytes, 57 lines, SHA-256 `7d351e0b5bb51f088f721afc5cf9c9b992f075500212d962caff77430dd20136`, identical to the GitHub blob (`git hash-object` reproduces `4b1d17e041dab62010961fe394cef2ba77c70384`, size 2334) — the entire file was retrieved and inspected end to end.
- The file's own words (quoted for gate evidence, never extended): `strategy(... pyramiding=0, ... commission_type=strategy.commission.percent, commission_value=0.1)`; RSI block `len = input.int(14, ...)` / `src = input.source(close, ...)` / `rsi = ta.rsi(src, len)`; averages `len_a = input.int(10, ...)` / `out_a = ta.ema(close, len_a)`, `len_b = input.int(20, ...)` / `out_b = ta.ema(close, len_b)`, `len_c = input.int(100, ...)` / `out_c = ta.ema(close, len_c)`; toggles `showLong = input.bool(true, ...)` / `showShort = input.bool(false, ...)` / `closeAfterXBars = input.bool(true, ...)` / `xBars = input.int(24, ...)`; long rules `entryLong = ta.crossover(out_a, out_b) and out_a > out_c and close > open` and `exitLong = rsi > 70`; short rules `entryShort = ta.crossunder(out_a, out_b) and out_a < out_c and close < open` and `exitShort = rsi < 30`; holding counter `var int nPastBars = 0` with `if strategy.position_size > 0 or strategy.position_size < 0` / `nPastBars := nPastBars + 1` and `if strategy.position_size == 0` / `nPastBars := 0`; time-stop arming `if closeAfterXBars` / `exitLong := nPastBars >= xBars and close > entry_price ? true : exitLong` where `entry_price = ta.valuewhen(bought, open, 0)` and `bought = strategy.opentrades[0] == 1 and strategy.position_size[0] > strategy.position_size[1]`; orders `strategy.entry('Long', strategy.long, when=entryLong and showLong)` / `strategy.close('Long', when=exitLong)` / `strategy.entry('Short', strategy.short, when=entryShort and showShort)` / `strategy.close('Short', when=exitShort)`.
- Full-file token census (verified over the 57 lines this cycle): 2 `strategy.entry` / 2 `strategy.close` / 0 `strategy.exit` (no stop/limit leg of any kind ships anywhere); 0 `stop=` / 0 `limit=`; 0 `request.` / 0 `security(` (single chart timeframe, no external feed); 0 `volume` (no volume read anywhere — the rule is pure OHLC); 0 `high` / 0 `low` (only `open`/`close` are ever read); 1 `ta.crossover` / 1 `ta.crossunder` / 1 `ta.rsi` / 3 `ta.ema`; 3 `input.bool` / 5 `input.int` / 1 `input.source` / 0 `input.float`; 1 `pyramiding` (`0`); 0 `trailing` / 0 `stoploss` / 0 `takeprofit` / 0 `offset` / 0 `fillna` / 0 `ffill` / 0 `highest` / 0 `lowest` / 0 `barstate` / 0 `nz[`; `plot(` calls are display-only. The `entryShort`/`exitShort` legs exist in code but are gated by the default-`false` `showShort` toggle — fenced below, never evaluated.
- **Source-default direction is LONG/FLAT, not a researcher adaptation.** `showLong` defaults `true` and `showShort` defaults `false`, so under every default the short entry/close pair can never fire. This record evaluates only the long legs — that is the file's own default posture, not a disabled-leg adaptation.
- **All researcher-defined differences/choices, declared in advance:** (1) fix Binance BTCUSDT **spot** `1h` candles (the Pine program names no market and no timeframe — chart-selected); (2) same-decision-bar **close-price MARKET fills** for both `strategy.entry` and `strategy.close` legs (Pine market orders fill on the next tick; this normalization is disclosed, never presented as Pine semantics); (3) fix one `0.001 BTC` base-size position, one-position-only (`pyramiding=0` is source-native), no cooldown; (4) pin the Pine `ta.ema` / `ta.rsi` / `ta.crossover` recurrences and seed conventions below exactly; (5) replace the fill-bar-dependent `valuewhen(bought, open, 0)` entry-price capture with the controller ledger's recorded fill close, and count the 24 holding bars from the entry bar in completed-bar units (one-bar-equivalent normalization of Pine's calc-timing counter, disclosed); (6) fix a 150-completed-bar warmup, a declared controller-memory state machine, and the cost/clock model below. No other source-native execution or cost equivalence is claimed.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the single bar where the fast average crosses up through the mid average while already above the slow average and the bar prints green; close the long when the 14-bar RSI overheats above 70, or — once 24 bars have passed since entry — when the close is above the recorded entry price. The short mirror exists in code but is switched off by its own default toggle. No stop-loss, no take-profit, no trailing, no second exit of any kind ships anywhere in the 57 lines.

### Research interpretation

Research hypothesis only: a fast-over-mid EMA cross marks a micro-trend rotation, the slow-EMA level demands the rotation start from an already-elevated tape (no bottom-fishing), and the green-bar conjunct refuses rotations printed on a red bar (intraday distribution). The exit pair is asymmetric patience: overheating banks immediately via RSI, while any other tape must first survive 24 bars and then show any profit at all — chop that never overheats and never shows a 24-bar profit holds the position indefinitely. Unlike pure cross records, the regime level plus the green print gate both legs of the entry; unlike RSI-threshold holders, the in-profit time-stop adds a second, position-aware exit that depends on entry price and holding duration, not on any oscillator. This is a rotation-plus-regime hypothesis with patience exits, not a breakout order or a guaranteed profit mechanism. No return, Sharpe, win-rate, drawdown, or other independently reproduced statistic is asserted.

## Signal — fully specified derived rule

Data are UTC Binance BTCUSDT spot `open, high, low, close` on **completed** `1h` candles. Only `open` and `close` enter any predicate (`high`/`low` are carried for validity checks only; `volume` is never read). Let bar index `t` refer to the current completed candle, with `t-1` the preceding completed candle. All comparisons are strict except where `<=` is written.

Pine v5 standard recurrences pinned exactly (documented Pine semantics, no library version relied upon):

```text
ema(L)[t]   = SMA(close, L) at the L-th observed bar (seed), then
              alpha * close[t] + (1 - alpha) * ema(L)[t-1], alpha = 2 / (L + 1)
A[t]        = ema(10)[t];  B[t] = ema(20)[t];  C[t] = ema(100)[t]
rsi[t]      = Pine ta.rsi(close, 14)[t]   // RMA/Wilder smoothing, na until seeded
cross[t]    = (A[t-1] <= B[t-1]) and (A[t] > B[t])   // exact ta.crossover reduction
entry[t]    = cross[t] and (A[t] > C[t]) and (close[t] > open[t])
rsi_exit[t] = (rsi[t] > 70)
time_exit[t]= LONG and ((t - entry_bar) >= 24) and (close[t] > entry_price)
```

- `na` handling (Pine-native, disclosed): every Pine series is `na` until seeded; every strict/`<=` comparison involving `na` is false, so no leg can fire before the indicators exist. The 150-bar record floor below additionally holds every pre-seed bar flat.
- State transitions are evaluated **once after the bar is complete**, using the state carried *into* the bar:
- `FLAT + entry[t]` -> MARKET BUY exactly `0.001 BTC` at that completed bar's close, then `LONG` with `entry_bar = t`, `entry_price = close[t]`.
- `LONG + (rsi_exit[t] or time_exit[t])` -> MARKET SELL the entire recorded `0.001 BTC` at that bar's close, then `FLAT`.
- Otherwise hold the previous state. A held position never adds, even if a fresh entry edge prints (`pyramiding=0` is source-native). The entry bar **cannot** be its own exit: `t - entry_bar = 0` fails the `>= 24` arm and `rsi_exit` on the entry bar is resolved by the position pin below.
- Co-print priority (possible, resolved by position pin — disclosed, not repaired): an entry bar can simultaneously print `rsi[t] > 70` (hot crossover). No engine ordering is invented: a flat book treats the bar as entry (the exit legs need a position and are no-ops without one — no same-bar round-trip), while a positioned book treats the bar as exit-close (further entry edges are hold-no-ops). While LONG, all three exit arms (RSI level, time-plus-profit, and — vacuously on one bar — any combination) close the full unit at the same bar close, so no exit-exit ordering exists either.
- After an exit, a fresh qualifying entry edge on a later bar may enter immediately; no cooldown (the source ships none — explicitly none, not invented).
- All pre-warmup bars are FLAT. Missing/invalid candles cause **no signal and no fill**, not synthetic price or forced entry. A bar with `close[t] == open[t]` (doji) can never satisfy the green conjunct. On the final data bar, a remaining position is reported as open; no fabricated terminal liquidation.
- Direction is LONG/FLAT only — the file's own default toggle posture (`showShort = false`); the short legs are never evaluated. Reverse-on-signal, hedging, simultaneous positions, pyramiding, averaging, safety orders/DCA, stop loss, take profit, trailing stop, partial exits, stop/limit/maker orders, and further time-based exits beyond the 24-bar arm are all **absent from the source** — explicitly none, not invented.
- The position is deliberately unprotected: a long that never prints RSI above 70 and never shows a 24-bar profit is held indefinitely, including through arbitrarily deep unrealized loss. There is no protective stop anywhere in this specification because there is none in the source.

## Required data, warmup, causality

- One market, one `1h` UTC candle feed: `open` (green-bar conjunct and entry-price ledger) and `close` (all three EMAs, the RSI, both cross/regime comparisons, and every exit). No `volume`, funding, OI, mark/index, L2, cross-asset, calendar, higher/lower timeframe, or other non-OHLCV data is read by any predicate. `high`/`low` enter only the bar-validity check (`high >= low > 0`, `open > 0`, `close > 0`, all finite).
- The slowest seed is the EMA100 SMA-seed at the 100th observed bar; derived warmup is **150 completed bars** and no trade before it (covers the EMA100 seed plus 50 bars of transient margin, the RSI14 seed, and the one-bar crossover lag). The Pine `na`-until-seeded convention independently fences every earlier bar.
- Every signal on bar `t` depends solely on bars `<= t`. A bar is only made available after its `1h` close; neither `open[t]` nor `close[t]` is treated as known before that close. No repainting, lookahead, negative shift, full-sample fitting, future pivot, `request.security`, or partial higher-timeframe candle. The Pine program's chart timeframe is fixed to `1h` by this record's researcher pin — no multi-timeframe alignment is required anywhere.

## Execution assumptions — pinned Hummingbot capability evidence

**Pinned contract:** Hummingbot package `20260920`, `hummingbot/VERSION = dev-2.17.0`, repository `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Read-only inspection of this exact commit (2026-10-25, via the local clone's object store) establishes the following *code-level primitives*, not a strategy-specific live/testnet run:

1. **Data/venue:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `1h` in `INTERVALS`. `binance_spot_candles/binance_spot_candles.py` uses Binance spot klines, passes `interval` to REST (`"interval": self.interval`), parses `row[0]` as candle **open timestamp** (`ensure_timestamp_in_seconds(row[0])`) and parses OHLC plus volume (`row[1..5]`). The research decision clock is explicitly **open_timestamp + 3600 seconds**, the completed `1h` bar's effective availability time; raw Hummingbot candle timestamps remain open-time labels and must not be mistaken for close-time decisions.
2. **Fill:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `OrderExecutorSimulator.simulate`: `ExecutionStrategy.MARKET` fills at the first supplied row (`fill_timestamp = df_filtered['timestamp'].iloc[0]`), uses that row's **close** as `entry_price` (`entry_price = df_filtered.loc[fill_timestamp, 'close']`), records `filled_amount_quote = amount * close`, `cum_fees_quote = trade_cost * filled_amount_quote`, and terminates with `POSITION_HOLD`. The engine's raw `fill_timestamp` is the supplied row's **open-time label**; the declared causal event time for audit/parity is the separately normalized close-effective time `open_timestamp + 3600`. Neither the engine's raw label nor a close-based fill is represented as an actual exchange execution timestamp. This is a **research backtest convention**, not a live guaranteed close fill. Both the entry BUY and every exit SELL (RSI level or time-plus-profit) reuse this single verified MARKET-close path — no LIMIT/STOP/maker/intrabar-touch primitive is required, because every exit is evaluated on completed-bar closes by the controller and submitted as a MARKET action.
3. **Controller and ledger:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` executes `update_state(row)` then `controller.determine_executor_actions()` (method pinned on `controller_base.py:465`), accepts `CreateExecutorAction` with `OrderExecutorConfig`, and uses `BacktestPositionHold` to net executed BUY/SELL base exposure and separately accumulate realized gross PnL and fees ("Buys and sells of the same asset net out automatically. Realized PnL comes from matched buy/sell volume."). The derived controller's own persistent `FLAT/LONG(entry_bar, entry_price, Q)` state and fill ledger (not the engine's bounded terminated-executor view or a delayed `positions_held` snapshot) gate entries, both exits, and the holding-bar count — this replaces Pine's `strategy.opentrades` / `ta.valuewhen(bought, open, 0)` / `var nPastBars` fill-bar machinery with an explicit bar-indexed equivalent, disclosed above. A controller implementing exactly these transitions is **not yet implemented** and is a downstream engineering artifact, not a second HB_READY admission criterion.
4. **Cost/position model:** one `Q=0.001 BTC` BUY/SELL unit on Binance **spot**, no leverage/margin/liquidation/futures funding; funding is **not applicable**, not silently set to a fictitious realized zero-funding stream. The pinned simulator charges `trade_cost` **per side** on each simulated fill's quote notional; the engine run-signature default is `trade_cost=0.0002` (`backtesting_engine_base.py:225`), and this record pins an explicit research fee of `trade_cost=0.001` **per side** applied through that same per-fill path (a declared research assumption — the Pine header's `commission_value=0.1` broker config is fenced as original-backtest config, never as engine evidence). Modeled slippage is `0.0` because this pinned MARKET simulator fills at its close input, **not** a claim of actual zero market slippage. Per completed trade, fee-adjusted research PnL is `realized_gross_quote - sum(cum_fees_quote)`; the executor `net_pnl_quote` alone is not accepted as fee-adjusted cash/equity. The simulator uses binary floats for amount*price, no verified exchange tick/lot rounding, so tiny float residues and real-world precision/slippage discrepancies are limitations, not hidden fills.
5. **Timing constraints:** no next-open, intrabar stop, maker queue, partial fill, shared capital, multi-timeframe, or simultaneous multi-asset semantics are required by this derivative. The single-row MARKET-close primitive is reused for all three event types (entry, RSI exit, time-plus-profit exit), and the `1h` `+3600s` normalization is mandatory before comparing event timestamps. No missing bar's close is invented; a missing `1h` bar blocks that bar's decision/fill while a held position stays open.

These exact engine source paths and restrictions provide **static code-path compatibility evidence** for the defined derived rule. No Qlib/Hummingbot strategy backtest, runtime deployment, trade, or event-level Qlib/HB parity was performed in this Scout cycle. Independent Hermes Auditor must independently verify Gate 5 and all other gates against the pinned code before any merge. Representative engine-path parity remains required before screening if the path is not already validated; PASS is not profitability, Qlib materialization, Survivor, HB Certified or trading authorization.

## Six-gate HB_READY evidence for independent review

1. **Deterministic:** Pine `ta.ema`/`ta.rsi`/`ta.crossover` recurrences pinned with seed conventions, strict cross/regime/green/RSI/time comparisons with explicit equality handling, `na`-until-seeded fencing, disjoint-by-position entry/exit priority, explicit bar offsets and state ledger; all researcher choices pinned above.
2. **Direction:** BTCUSDT Binance spot LONG/FLAT only — the file's own default toggle posture (`showShort=false`), never evaluated, never adapted.
3. **Entry/exit/risk:** entry on the completed cross-plus-regime-plus-green bar; exits on the completed RSI70 bar or the completed 24-bars-and-profitable bar; no protective/partial/other exit exists in source and none is added. No profit-trigger definition beyond the two stated exits is needed because no ROI/stop/trailing leg exists in this derivative.
4. **State:** one fixed `0.001 BTC` unit (`pyramiding=0` source-native), no adds/DCA, no same-bar round-trip possible, co-print resolution by position pin, no cooldown beyond the 24-bar exit arm, deterministic transitions, open-at-end reporting without terminal liquidation.
5. **Engine:** exact Hummingbot package/version/commit, BinanceSpotCandles `1h` feed, controller state (including the holding-bar ledger replacing Pine's fill-bar counter), OrderExecutor MARKET-close fills for all event types, raw/open vs effective/close timestamps, spot accounting, fee/slippage/precision limitations and BacktestPositionHold netting identified by actual immutable code paths; no unverified specialized execution requirement is introduced.
6. **Causality:** 150 completed-bar warmup, point-in-time completed-bar evaluation, no future access, normalized event times and missing-bar fail-closed behavior.

## Evidence and negative evidence

**Primary-source reported:** `Tendency EMA + RSI.pine` at `8fb3837` (57 lines) expressly prints the EMA10/20/100 triple, the RSI14, the long entry conjunction (fast-over-mid cross AND fast-above-slow AND green bar), the RSI70 long exit, the default-on 24-bar in-profit time-stop with its holding counter and entry-price capture, the default-off short mirror, `pyramiding=0`, and the 0.1% commission broker config. The file ships no market, no timeframe, no stop-loss, no take-profit, no trailing, and no performance number of any kind — this record claims no source-reported performance.

**Independently reproduced:** None. Static pinned-engine source read only, as detailed above. The file is research-only, not implemented.

**Dedup (main SHA `44bc03534d5493cfdb3460adb72337ce98a9887b`, 2026-10-25):** working-tree filename/content search for `Tendency`, `Trend EMA + RSI`, `closeAfterXBars`, `nPastBars`, and `valuewhen` returns zero strategy records — no pool record uses a holding-bar counter or a profit-conditioned time exit. The nearest EMA-cross cousins are materially different constructions: `freqtrade-strategy001-ha-ema-cross-long-flat-btcusdt-5m-2026-10-21.md` crosses EMA20/50 with Heikin-Ashi filters and exits on an EMA50/100 cross with an ROI ladder and a −30% stop (`5m`, no RSI, no time-stop); `ema-20-50-cross-btcusdt-1h-2026-10-06.md` is a pure 20/50 cross/crossunder pair with no RSI, no regime level, no risk legs and no time exit; `forven-ema-cross-adx-regime-long-flat-btcusdt-1h-2026-10-19.md` gates a 20/50 cross by ADX regime with a 200-bar EMA (different gate family, different exit). The twelve admitted `alorse-*` siblings trade BB/Aroon, BB Winner, DMI, exceeded-candle, flawless-victory, kodify-BB350, MACD+DMI, MTF-RSI+EMA900, QQE, StochRSI+Supertrend, Supertrend+RSI, and Williams-VixFix mechanics — none crosses a fast/mid EMA pair under a slow-EMA regime with a green-bar conjunct and a holding-bar profit exit. All currently open `research/*` PRs were inspected for the same source and mechanism (#48 Larry Williams 3-EMA channel streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay72018, #353 Heracles) — different mechanisms, indicators, and sources. Not a duplicate, paraphrase, or trivial parameter variant.

**Independent review limitation:** the time-stop fires only on bars that are both 24+ bars past entry and profitable at the close; a position can therefore be held indefinitely through chop that never overheats and never shows a qualifying profit. The Pine fill-timing counter (`nPastBars` from the fill bar, entry price at the fill bar's open) is normalized here to completed-bar units from the decision bar with the fill close — a disclosed one-bar-equivalent convention, not Pine-exact replication. Pine's next-tick market fills are normalized to same-bar closes, which can differ from TradingView's own backtest fills on gapping bars.

**Limitations:** the file's short mirror is deliberately never evaluated — this derivative is long-flat by the source's own default toggles and is never evidence about short-side behavior. The EMA seeding transient is fenced by the 150-bar warmup; a shorter warmup would admit seed-dependent early events. Close-price fills and modeled fees do not reproduce actual venue microstructure; no spot execution/live approval. The exit pair has no loss-cutting leg: a position decaying without RSI heat is held until the wide patience arms release it, and the 24-bar arm additionally demands profitability, so deep drawdowns can be carried. Qlib/Hummingbot event parity and strategy-specific executable artifact remain future, separately authorized work.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA10/20/100 recurrences as written / strict cross-plus-regime-plus-green entry / RSI70 level exit / 24-bar in-profit time exit / single-unit long-only / `1h` BTCUSDT / same-bar-close fills are frozen.

- F1 — Time-stop relevance: the same entry with the 24-bar arm removed (RSI70 exit only, same pins) must not improve net expectancy; fail ⇒ the patience exit adds nothing over the naked overheating exit.
- F2 — Regime relevance: the same cross-plus-green entry with the `A > C` slow-EMA arm removed (same exits, same pins) must not reproduce-or-beat net expectancy; fail ⇒ the slow-EMA regime adds nothing and the record is a label variant of a bare fast/mid cross.
- F3 — Green-bar relevance: the same cross-plus-regime entry with the `close > open` conjunct removed (same exits, same pins) must not reproduce-or-beat net expectancy; fail ⇒ the green print adds nothing over the pure average-cross rotation.

## Crypto portability

Direct for the long leg on either venue type: single-venue BTCUSDT `1h` completed bars with `open` and `close` fields only. No session calendar (crypto trades continuously; the EMA/RMA recursions and the one-bar crossover lag need no session-gap semantics), no corporate actions, no dividends, no funding/OI reads, no cross-venue state. 24/7 continuity means every lookback bar is always the immediately prior print — no weekend-gap discontinuity to normalize. Tick-size rounding follows the venue; no displayed price precision changes any event. The long-only book expresses identically on spot (no margin needed) and on perpetual under a house overlay; it is the same rule on both.

## Implementation status

not-implemented. No dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record; downstream materialization follows the `IMPLEMENTATION_NEEDED` route without revisiting HB_READY admission.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. Any future authorization requires a separate downstream decision outside this repository's admission scope.

## Related Wiki records

None.
