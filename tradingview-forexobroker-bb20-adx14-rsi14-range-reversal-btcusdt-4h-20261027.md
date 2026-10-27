---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: forexobroker BB20 ADX14 RSI14 range-reversal BTCUSDT spot 4h long-flat independent derivative
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-27
sources:
  - https://www.tradingview.com/script/N3ItY18G-Vortex-Reversal-Engine-forexobroker/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# forexobroker Bollinger–ADX range reversal — independent BTC-USDT spot 4h long-flat derivative

## Provenance

**Primary public TradingView identity:** forexobroker, *Vortex Reversal Engine [forexobroker]*, open-source TradingView strategy, stable script ID `N3ItY18G`, https://www.tradingview.com/script/N3ItY18G-Vortex-Reversal-Engine-forexobroker/ . First-party description read 2026-10-27. The page displays **Apr 9** without an unambiguous year; the publication year is **not asserted**. Neither the complete Pine revision nor original input-default list was accessible as text in this research read. Despite its name, the publicly described mechanism is **Bollinger/ADX/RSI mean reversion**, not a Vortex VI+/VI− indicator.

**Source-reported, not inferred:** one-position-at-a-time; ADX below configurable 30; lower-Bollinger-band touch in a 5-bar lookback for long (upper-band touch for short); recently oversold RSI with rising RSI for long (reverse for short); close still below BB basis for long; bullish candle closing above its midpoint; barstate.isconfirmed; default single-exit target +1.0 ATR and stop −3.5 ATR; optional partial TP1/TP2, trailing, session filter and cooldown. The source explicitly describes BB basis as SMA20 and an extreme at two standard deviations. It does **not** disclose in the readable page a reproducible RSI-recent lookback, exact ADX/ATR/RSI lengths and seed conventions, order timing/quantity, complete cooldown/session defaults, fee/funding, or precise Pine exit-order behavior. Do not attribute the following chosen values to the author.

**Declared independent derivative v1, NOT source-native/lossless Pine:** select **Binance BTC-USDT spot 4h, long/flat only**; pin BB20 population standard deviation ×2, Wilder RSI14/ADX14/ATR14, RSI lookback of five *preceding* completed bars, 5-bar BB-touch window including the signal bar, fixed 0.001 BTC size, no source short, no sessions/cooldown/partial TP/trailing, close-confirmed (rather than intrabar resting) ATR target/stop, and the state/timing/cost/validation rules below. The re-arm rule is an additional disclosed researcher restriction. All changes are part of this **separate strategy**, not evidence that the source's Pine strategy is expressible unchanged.

**Immutable research identity:** `TV-N3ItY18G-forexobroker | derived-v1-BB20x2-pop-ADX14lt30-RSI14-prior5lt30-recovery-candle | BTC-USDT-binance-spot-4h | close-bracket-ATR14-1p0-3p5 | 2026-10-27`. Changing any component changes the derivative identity.

**Pre-write dedup:** main SHA `aa2c50d42794858bdf2c332bd79aa1a24920528c`, 380 root-level strategy Markdown records; README static count 380. GitHub main search for `N3ItY18G` and `forexobroker` and PR search for `N3ItY18G` returned no match; ten open `research/*` PRs were examined by title and source, none uses this URL or rule. Nearby families are materially different: `sideways-dmi-bollinger-breakout-long-btcusdt-4h-2026-10-07.md` requires a *lower-band upward price crossover* with DMI spread <20 and exits on an *upper-band downward crossover*; `forven-bollinger-s00120-rsi-breakout-long-flat-bnbusdt-1h-2026-10-17.md` buys an *upper-band breakout* under RSI oversold; `chartart-bollinger-rsi-double-joint-cross-two-sided-btcusdt-1d-2026-10-15.md` requires simultaneous RSI50 and lower/upper-band joint crosses. This candidate instead requires a **recent lower-band touch + ADX low-trend regime + RSI recovering + bullish midpoint candle**, then frozen ATR bracket exits; not a trivial parameter variant.

## Economic mechanism

The first-party hypothesis is range-bound mean reversion after a lower-band extreme and confirmed momentum recovery. ADX vetoes trending conditions; RSI and candle shape seek an initial rebound while price remains below the mean. The deliberately asymmetric +1 ATR target / −3.5 ATR stop is a payoff design, **not** proof of positive expectancy. No TradingView backtest or win-rate figure is independently reproduced or claimed.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 4h OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 14400 seconds apart, and no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars or price fallback.

**BB20:** for `t>=19`, `basis[t]=sum(C[t-19..t])/20`; `sigma[t]=sqrt(sum((C[i]-basis[t])^2 for i=t-19..t)/20)` (population divisor 20); `lower[t]=basis[t]-2*sigma[t]`; `upper[t]=basis[t]+2*sigma[t]`. No shifted bands or fitted inputs.

**Wilder RSI14:** for `t>=1`, `d=C[t]-C[t-1]`, `g=max(d,0)`, `l=max(-d,0)`. At `t=14` seed average gain/loss with the arithmetic mean of `d[1..14]`; for `t>14`, `avgG=(13*avgG_prev+g)/14` and likewise `avgL`. `RSI=100*avgG/(avgG+avgL)`; if both averages are zero RSI=50; if only loss is zero RSI=100; if only gain zero RSI=0.

**Wilder ATR14 / DMI14 / ADX14:** for `t>=1`, `TR=max(H-L,abs(H-Cprev),abs(L-Cprev))`, `up=H-Hprev`, `down=Lprev-L`, `+DM=up if up>down and up>0 else 0`, `-DM=down if down>up and down>0 else 0`. At `t=14` seed `ATR14`, `RMA(+DM,14)`, `RMA(-DM,14)` with means over bars 1..14, then Wilder recurrence `(13*previous+current)/14`. `DIplus=100*RMA(+DM)/ATR`, `DIminus=100*RMA(-DM)/ATR`, `DX=100*abs(DIplus-DIminus)/(DIplus+DIminus)`. If `ATR=0` or the DI denominator is zero, DX=0 and both DI=0. First `ADX14` at `t=27` is arithmetic mean `DX[14..27]`; later ADX uses Wilder recurrence. All divisions and outputs must remain finite; no hidden library seed.

**Completed-bar long entry predicate `E[t]`** (all true, strict comparisons unless shown):
1. `ADX14[t] < 30`.
2. `any(L[i] <= lower[i] for i=t-4..t)` (5 complete bars; band at each bar i, no look-ahead).
3. `min(RSI14[t-5..t-1]) < 30` and `RSI14[t] > RSI14[t-1]` (researcher-fixed definition of the source's unspecified recent oversold recovery).
4. `C[t] < basis[t]`.
5. `C[t] > O[t]` and `C[t] > (H[t]+L[t])/2`.
6. `t>=100`, every required feature valid, no pending order, FLAT and re-arm state true.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory or cross-market trade. The original short-side description is intentionally **disabled**.

**Frozen bracket (Gate 3):** upon confirmed BUY at observed `entry_close=C[t]`, freeze `atr_entry=ATR14[t]` and `tp=entry_close+1.0*atr_entry`, `sl=entry_close-3.5*atr_entry`. Require `atr_entry>0`, finite, and `sl>0`; otherwise no entry. Starting at the **next completed bar** after entry, while LONG, request full SELL if `C[t]>=tp` (target) or `C[t]<=sl` (stop). If neither, hold. TP and SL cannot both trigger on the same close. **Both are close-confirmed MARKET research exits, not intrabar touches or resting protective stop/limit orders.** No RSI/ADX/BB signal exit, trailing, time stop, partial exit, averaging, forced end-of-data liquidation or silent executor triple-barrier default.

**State (Gate 4):** `FLAT_DISARMED`, `FLAT_ARMED`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT_ARMED` after 100 valid completed bars **only if E without the state clause was false on the immediately prior completed bar**; otherwise wait for a false bar to arm. A BUY request transitions to `BUY_PENDING`, freezes candidate entry-bar ATR; only a confirmed MARKET POSITION_HOLD fill at that same completed close transitions to LONG and freezes entry price/levels. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored. SELL request transitions to SELL_PENDING; only confirmed filled SELL of the complete 0.001 BTC returns to FLAT_DISARMED. Once flat, require at least one **subsequent** completed bar with the non-state entry predicate false to re-arm; a later true predicate may buy. No same-bar SELL+BUY, pyramiding, DCA/SO, concurrency, rebalancing, compounding, session restriction, source optional cooldown or other trade. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous completed 4h bars before the first actionable bar; RSI prior-five, BB touch-five and ADX seeds are covered. No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Require enough historical pre-start candles to compute this before the first eligible decision; `prepare_market_data` itself may drop NaNs and must not be relied upon to silently repair gaps.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0]); a bar's OHLC and derived indicators become available no earlier than `T[t]+14400s`. All decisions and the synthetic model fill are effective at that **completed-bar close**. The backtest engine's backward `merge_asof` operates on raw open-time indices, so a strategy-specific controller must gate features by close availability and not mistake open-time index `T[t]` for the decision time. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting or same-bar intrabar touch is used. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (`hummingbot/VERSION` blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb` read this cycle). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** `BinanceSpotCandles` at `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` (blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`) parses Binance `/api/v3/klines` open-time and OHLCV; `constants.py` supports `4h`. Connector `binance`, pair `BTC-USDT`, one spot 4h stream. No funding or perpetual margin/mark/index, no order-book/volume-dependent decision, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.update_processed_data` → `prepare_market_data` → per-row `update_state` → `determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`; pinned `backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`. A **strategy-specific, not-yet-implemented** controller must calculate the exact indicators/state and perform time gating. The generic executor does not calculate the strategy.
- **Orders:** `OrderExecutorConfig` from `hummingbot/strategy_v2/executors/order_executor/data_types.py` (blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`), `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.001")`, `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. MARKET `OrderExecutorSimulator` (blob `3b4e82e91896db9074295ca2a8a087dde2499eab`) fills fully at first provided row's **close** and ends `CloseType.POSITION_HOLD`; not a live or intrabar stop fill. On confirmed fills, `BacktestPositionHold` nets base amounts, tracks weighted entry, realized gross PnL and fees. Do not infer a position from the order request; controller must use confirmed executor/hold state, with a persistent ledger or `terminated_executors_window=None` rather than relying on the default 3600s view for 4h bars.
- **Fees and accounting:** pin `trade_cost=0.0002` per filled BUY and SELL, exactly the simulator's `cum_fees_quote=trade_cost*amount*observed_close`. This is **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. For one round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. The pinned engine's `summarize_results.net_pnl_quote` for POSITION_HOLD can reflect **gross** matched PnL while reporting fees separately; its `pnl_timeseries` also does **not** guarantee a complete fee-inclusive cumulative equity series after flat transitions. **Never** call either output fee-inclusive net equity without reconstructing from actual fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Price integrity:** validate every observed finite positive `close_bt` before order creation; `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` for a missing pair and must **never** supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Six-gate evidence and limits

1. **Determinism:** all indicators, seeds, strict thresholds, five-bar windows, state priority and size are fixed above; no optimization, ML or undisclosed Pine defaults.
2. **Direction:** BTC-USDT spot long/flat, short explicitly off.
3. **Entry/exit/risk:** full predicate and close-only frozen ATR bracket; all optional behaviors explicitly disabled.
4. **State:** one position, confirmed-fill transitions, no DCA/pyramiding, re-arm and pending rules explicit.
5. **Pinned expressibility:** exact Hummingbot commit, 4h Binance feed, custom controller route, MARKET close simulator, POSITION_HOLD accounting, explicit fee and unsupported-realism boundaries; no intrabar order semantics claimed.
6. **Causality:** 100 complete-bar warmup, strict continuity, prior-only RSI lookback, close availability `T+14400`, no future signals, close-model disclosure.

**Limits:** source Pine source-code bytes and author input defaults not recovered; the researcher-chosen RSI/ADX/ATR variants, 5-bar RSI history, direction, entry state, execution convention, exit handling, size, cost and market are **not** source-native facts. No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.
