---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView ChartArt NR7 plus Inside Day SMA20 bullish-candle exit — independent BTCUSDT 1d derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-25
sources:
  - https://www.tradingview.com/script/Dln4aFaM-Narrow-Range-Inside-Day-Long-Only-Strategy-by-ChartArt/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ChartArt NR7 + Inside Day / SMA20 bullish-candle exit — independently derived executable research rule

## Provenance and immutable identity

- Primary TradingView identity: `Dln4aFaM`, **Narrow Range + Inside Day, Long Only Strategy (by ChartArt)**; author **ChartArt**; public publication date **2016-10-16**; primary source URL in frontmatter; page inspected **2026-10-25**.
- Immutable candidate identity: `TV-Dln4aFaM | derived-nr7id-sma20-green-exit | BTCUSDT-spot-1d | v1 | 2026-10-25`. Freeze this combination; a changed SMA, signal, exit, market, time convention or fill model is a different derivative.
- **Not source-native / not a lossless Pine reproduction.** The publicly readable TradingView *author description* (not the full Pine body) expressly describes: a daily NR7 candle narrower than each of six preceding candles, strict inside-day high/low containment, a bullish candle, positive SMA slope, long-only entry, and a later bullish-candle exit. It does **not** expose a reliably readable Pine implementation or a definite SMA period, exchange, sizing, order-fill timing, transaction costs, cooldown, pyramiding or protective orders. No assertion is made about inaccessible Pine defaults or original backtest performance.
- **All researcher-defined differences/choices, declared in advance:** (1) fix SMA to simple 20-day close SMA, with strict one-bar rising slope; (2) fix Binance BTCUSDT **spot** daily UTC candles (24/7 rather than equity trading sessions); (3) interpret the author's conjunction as a close-confirmed setup-bar entry, with a later bullish close exit, and pin strict comparisons and tie rules below; (4) choose same-decision-bar **close-price MARKET fills** on a completed daily bar, instead of claiming the original Pine fill convention; (5) fix one `0.001 BTC` base-size position, one-position-only, no DCA or re-entry delay; (6) explicitly disable protective stop/target/trailing/time exits (not a claim that original Pine disabled them); (7) fix 25-completed-bar warmup, a declared controller-memory state machine, and the cost/clock model below. No other source-native execution or cost equivalence is claimed.

## Economic mechanism

Research hypothesis only: an unusually narrow daily range *inside* the prior day signals compression; the green setup candle and positive SMA20 slope select upward-biased compressions. Unlike breakout-following NR7 variants, the derived rule buys the **completed setup bar itself**, then liquidates on the **first later green day**; this is a short-hold conditional candle-state hypothesis, not a breakout order or a guaranteed profit mechanism. No return, Sharpe, win-rate, drawdown, or other independently reproduced statistic is asserted.

## Signal — fully specified derived rule

Data are UTC daily Binance BTCUSDT spot `open, high, low, close` on **completed** candles. Let bar index `t` refer to the current completed daily candle, with `t-1` the preceding completed daily candle. All comparisons are strict; equalities fail. Define:

```text
range[t] = high[t] - low[t]
sma20[t] = sum(close[t-19], ..., close[t]) / 20
nr7[t] = all(range[t] < range[t-k] for k = 1..6)
inside[t] = high[t] < high[t-1] and low[t] > low[t-1]
green[t] = close[t] > open[t]
slope_up[t] = sma20[t] > sma20[t-1]
entry_setup[t] = nr7[t] and inside[t] and green[t] and slope_up[t]
exit_signal[t] = green[t]
```

State transitions are evaluated **once after the bar is complete**, using the state carried *into* the bar:

- `FLAT + entry_setup[t]` -> MARKET BUY exactly `0.001 BTC` at that completed bar's close, then `LONG` with entry bar `t`.
- `LONG + (t > entry_bar) + exit_signal[t]` -> MARKET SELL the entire recorded `0.001 BTC` at that bar's close, then `FLAT`.
- Otherwise hold the previous state. A held position never adds, even if a fresh NR7 setup occurs. The entry bar **cannot** be its own exit; exit is evaluated only from the next completed day onward. If a green exit and new entry setup coincide while already LONG, **exit wins and no same-bar re-entry**. After an exit, a fresh qualifying setup on a later bar may enter immediately; no other cooldown.
- All pre-warmup and pre-first-entry bars are FLAT. Missing/invalid candles cause **no signal and no fill**, not synthetic price or forced entry. On the final data bar, a remaining position is reported as open; no fabricated terminal liquidation.
- Direction is LONG/FLAT only; naked shorts, reverse-on-signal, hedging, simultaneous positions, pyramiding, averaging, safety orders/DCA, TP, SL, trailing, partial exits, stop/limit/maker orders, and time-based exits are all **disabled by this derived specification**. No hidden executor defaults supply any of them.
- The bullish-candle exit can occur at a loss. There is no profit guarantee and no protective stop. The next-day minimum hold follows the author's word **“next time ... in any of the next trading days”** but the precise order-time semantics are this researcher's disclosed close-fill derivative, not verified original Pine.

## Required data, warmup, causality

- One market, one daily UTC candle feed: `open` (bullish-body test), `high/low` (range/inside test), `close` (SMA and MARKET close-fill). No volume, L2, funding, cross-asset, mark/index, calendar events, lower/higher timeframe or non-OHLCV data are read by any signal.
- SMA20 slope needs `sma20[t-1]`, hence **21** completed closes; NR7 needs seven completed daily ranges. Derived warmup is **25 completed bars** and no trade before it. SMA20 uses an ordinary unweighted arithmetic average with no alternative smoothing, missing-value substitution or forward fill.
- Every signal on bar `t` depends solely on bars `<= t`. A bar is only made available after its UTC daily close; the close is never treated as known at that bar's open. No repainting, lookahead/security call, negative shift, full-sample fitting, future pivot, or partial higher-timeframe candle.
- Equal ranges, equal inside highs/lows, doji candles, or a flat SMA20 slope are not entry events. A doji while LONG is not an exit event.

## Execution assumptions — pinned Hummingbot capability evidence

**Pinned contract:** Hummingbot package `20260920`, `hummingbot/VERSION = dev-2.17.0`, repository `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Read-only inspection of this exact commit (2026-10-25) establishes the following *code-level primitives*, not a strategy-specific live/testnet run:

1. **Data/venue:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `1d` in `INTERVALS`. `binance_spot_candles/binance_spot_candles.py` uses Binance spot klines, passes `interval` to REST, parses `row[0]` as candle **open timestamp**, and parses OHLC. The research decision clock is explicitly **open_timestamp + 86400 seconds**, the completed daily bar's effective availability time; raw Hummingbot candle timestamps remain open-time labels and must not be mistaken for close-time decisions.
2. **Fill:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `OrderExecutorSimulator.simulate`: `ExecutionStrategy.MARKET` fills at the first supplied row, uses that row's **close** as `entry_price`, records `filled_amount_quote = amount * close`, `cum_fees_quote = trade_cost * filled_amount_quote`, and terminates with `POSITION_HOLD`. The engine's raw `fill_timestamp` is the supplied row's **open-time label**; the declared causal event time for audit/parity is the separately normalized close-effective time `open_timestamp + 86400`. Neither the engine's raw label nor a close-based fill is represented as an actual exchange execution timestamp. This is a **research backtest convention**, not a live guaranteed close fill.
3. **Controller and ledger:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` executes `update_state(row)` then `controller.determine_executor_actions()`, accepts `CreateExecutorAction` with `OrderExecutorConfig`, and uses `BacktestPositionHold` to net executed BUY/SELL base exposure and separately accumulate realized gross PnL and fees. The derived controller's own persistent `FLAT/LONG(entry_bar, Q)` state and fill ledger (not the engine's bounded terminated-executor view or a delayed `positions_held` snapshot) gate entries/exits. A controller implementing exactly these transitions is **not yet implemented** and is a downstream engineering artifact, not a second HB_READY admission criterion.
4. **Cost/position model:** one `Q=0.001 BTC` BUY/SELL unit on Binance **spot**, no leverage/margin/liquidation/futures funding; funding is **not applicable**, not silently set to a fictitious realized zero-funding stream. Pinned backtest fee is `trade_cost=0.001` **per side**, applied to each simulated fill's quote notional; modeled slippage is `0.0` because this pinned MARKET simulator fills at its close input, **not** a claim of actual zero market slippage. Per completed trade, fee-adjusted research PnL is `realized_gross_quote - sum(cum_fees_quote)`; the executor `net_pnl_quote` alone is not accepted as fee-adjusted cash/equity. The simulator uses binary floats for amount*price, no verified exchange tick/lot rounding, so tiny float residues and real-world precision/slippage discrepancies are limitations, not hidden fills.
5. **Timing constraints:** no next-open, intrabar stop, maker queue, partial fill, shared capital, multi-timeframe, or simultaneous multi-asset semantics are required by this derivative. The single-row MARKET-close primitive is reused, and the daily `+86400s` normalization is mandatory before comparing event timestamps. No missing bar's close is invented; a missing daily bar blocks that bar's decision/fill.

These exact engine source paths and restrictions provide **static code-path compatibility evidence** for the defined derived rule. No Qlib/Hummingbot strategy backtest, runtime deployment, trade, or event-level Qlib/HB parity was performed in this Scout cycle. Independent Hermes Auditor must independently verify Gate 5 and all other gates against the pinned code before any merge. Representative engine-path parity remains required before screening if the path is not already validated; PASS is not profitability, Qlib materialization, Survivor, HB Certified or trading authorization.

## Six-gate HB_READY evidence for independent review

1. **Deterministic:** four strict setup predicates, SMA20 simple arithmetic, seven-range comparison, explicit bar offsets and state priority; all researcher choices pinned above.
2. **Direction:** BTCUSDT Binance spot LONG/FLAT only; shorts expressly disabled.
3. **Entry/exit/risk:** entry on the completed setup day, first **later** green-day close exit, no protective/partial/other exit; disabled behaviors enumerated, including terminal position handling.
4. **State:** one fixed `0.001 BTC` unit, no adds/DCA, no same-bar re-entry, no cooldown beyond entry-bar minimum hold, deterministic conflict priority.
5. **Engine:** exact Hummingbot package/version/commit, BinanceSpotCandles daily feed, controller state, OrderExecutor MARKET-close fill, raw/open vs effective/close timestamps, spot accounting, fee/slippage/precision limitations and BacktestPositionHold netting identified by actual immutable code paths; no unverified specialized execution requirement is introduced.
6. **Causality:** 25 completed-bar warmup, point-in-time completed-bar evaluation, no future access, normalized event times and missing-bar fail-closed behavior.

## Evidence and negative evidence

**Primary-source reported:** TradingView `Dln4aFaM` (ChartArt, 2016-10-16) explicitly describes the NR7 + inside-day + green-candle + rising-SMA entry conjunction and a subsequent green-candle close. Its page says the SMA period can be changed but does not expose the specific default in accessible text. This record chooses 20 as an **independent researcher parameter**, never attributes 20 to the author. No Pine source, backtest statistic or original fill economics is claimed to have been recovered.

**Independently reproduced:** None. Static pinned-engine source read only, as detailed above. The file is research-only, not implemented.

**Dedup (main SHA `1ed0390dd18f71fbf44b19b3df4ce9abc283c59d`, 2026-10-25):** GitHub repository code search found no `Dln4aFaM` or `NR7ID` source identity; GitHub PR search returned no matching PR. Existing `nr7-price-breakout-long-btcusdt-1d-2026-10-10.md` instead enters **the day after** an NR7 setup on a channel breakout and exits on 10-day expiry/ATR stop; it does **not** require strict inside-day containment, green setup day and rising SMA, and does **not** exit on the first subsequent green candle. Existing `forven-inside-bar-breakout-continuation-long-flat-btcusdt-1h-2026-10-17.md` requires a later confirmed breakout, not a same-day NR7+SMA compression entry. Existing `inside-bar-failure-fade-time-exit-two-sided-btcusdt-1d-2026-10-13.md` fades failed probes with a three-bar clock. These are materially distinct signal/exit mechanisms, not a threshold-only clone. All currently open `research/*` PR titles/branches were inspected for the same source and mechanism.

**Limitations:** No accessible full Pine source for lossless attribution; SMA20, order timing, venue, quantity, risk omissions, state and costs are independently designed and disclosed. Close-price fills and modeled fees do not reproduce actual venue microstructure; no spot execution/live approval. The strategy can hold losing positions indefinitely during a succession of non-green days. Qlib/Hummingbot event parity and strategy-specific executable artifact remain future, separately authorized work.
