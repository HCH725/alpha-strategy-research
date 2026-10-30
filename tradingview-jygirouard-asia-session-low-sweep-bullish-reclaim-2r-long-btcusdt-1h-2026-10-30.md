---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "jygirouard Asia-session low sweep and bullish close reclaim with 2R close exits — independent BTC-USDT spot 1h derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/6fqUkyaO-ICT-Liquidity-Sweep-Asia-London-1-Trade-per-High-Low/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# UTC Asia-session low sweep / bullish reclaim / 2R close exit — independent research derivative

## Provenance

**TradingView primary source:** jygirouard, *ICT Liquidity Sweep Asia/London 1 Trade per High & Low*, **2025-10-22**, author's **strategy version 1.3**, public open-source strategy, stable script ID **6fqUkyaO**. First-party page directly inspected **2026-10-30**: https://www.tradingview.com/script/6fqUkyaO-ICT-Liquidity-Sweep-Asia-London-1-Trade-per-High-Low/ . The public description specifies Asia **20:00–23:59 America/New_York**, London **02:00–05:00 America/New_York**, session high/low sweeps, opposite-direction confirmation candles, at most one trade per high/low per session, stop beyond sweep wick, and configurable target **2:1 reward/risk by default**. It describes both long and short setups and recommends 1–15-minute charts. Full original Pine source bytes, precise sweep-to-confirmation state, and original fill/commission settings were not retrieved. No source-native, lossless Pine parity, original statistics, or original strategy PASS is claimed.

**Explicitly independent derived executable strategy, NOT source-native.** Retain only the economic concept of **a sweep below a completed session low followed by a bullish close reclaim**, the **one low-side trade per session** constraint, a **stop below the sweep wick**, and the source-described **2R** target. Researcher changes, all order-material: (a) Binance BTC-USDT **spot UTC 1h**, not original NY-clock 1–15m sessions; (b) define one fixed UTC **00:00–03:59 Asia proxy**, not the author's DST-aware NY Asia/London windows, and allow entry only from 04:00 through 11:59 UTC; (c) a single completed candle must sweep/reclaim and be bullish, instead of asserting the source's unspecified multi-candle confirmation semantics; (d) disable short/high sweeps, London leg and all other entries; (e) freeze one 0.001-BTC long position and a one-trade-per-UTC-day latch; (f) define a gap-safe stop from the entry fill, a 2R target, **completed-close-only** risk checks and 24-bar timeout, with next-completed-close historical MARKET fills instead of source-native resting/intrabar stops; (g) fix initial cash, warmup, costs, data validity, priority and re-entry. Every modification can change original trade events and economics.

**Frozen identity:** `TV:6fqUkyaO:jygirouard:2025-10-22:v1.3|independent-utc-asia-low-sweep-reclaim-2R-v1:2026-10-30|BinanceSpot:BTC-USDT:UTC1h|AsiaProxy00-03UTC|eligible04-11UTC|L<AsiaLow:C>AsiaLow:C>O|Q0.001BTC:cash10000USDT|signal-t:MARKET-close-t+1|stop=min(0.999*setupLow,0.99*fillClose):target=fillClose+2R|close-only:timeout24|one-buy-attempt-UTC-day|warmup72|fee0.001/side`. Changing any clock, source rule, state, fill or economic assumption is a distinct derivative revision.

**Main and duplicate snapshot:** GitHub `main@16c6179b6c40793ab03653bcca4a75ebafd0e981` has a nontruncated tree of **463** root-level strategy Markdown records, equal to README's **463**; 14 distributed records were independently sampled and each had `hb_ready_status: PASS` (not an exhaustive 463-file status audit). GitHub code search and open-PR search for stable ID `6fqUkyaO` returned no matches; 12 open research PRs were enumerated. The nearest mechanisms are (1) the existing FMZ Turtle Soup, which fades a **rolling 20-bar Donchian** false break, with unrelated 2.5ATR bracket/add state; (2) the hashem-trader UTC **single 00:00 candle HIGH breakout** with opposite-boundary 2R exit; and (3) the PuestoGlobal **triangle-boundary** failed breakdown with pivot construction and timeout. This derivative instead sweeps and **reclaims the completed four-hour UTC session LOW**, only once per UTC day, with a bullish-candle requirement and a fill-anchored 2R close-exit. It is neither the same TradingView source nor a trivial parameter change.

## Economic mechanism

### Source-reported
The author's ICT-inspired hypothesis is that price briefly sweeps a session's liquidity high/low and reverses, enabling a contrarian entry after candle confirmation. The author describes 2:1 reward/risk and a wick-based stop. These are the source's *conceptual* rules, not evidence of the derivative's profitability.

### Research interpretation
A completed four-hour UTC opening range may supply a public reference low. A later hourly candle that trades below it but **closes back above it with positive body** could mark an unsuccessful downside liquidity sweep. The derivative tests whether that failure subsequently reverts upward enough to compensate for its defined stop, delay and costs. No historical win rate, Survivor status, Qlib parity, or return claim is made.

## Signal

**Gate 1, exact input and comparisons.** One genuine contiguous Binance BTC-USDT Spot **1h** OHLCV series indexed `t=0,1,...` with Unix UTC **bar-open** timestamp `T[t]`, divisible by 3600 and exactly `T[t]-T[t-1]=3600`. `O,H,L,C` finite positive, `L<=min(O,C)<=max(O,C)<=H`, base volume `V` finite and nonnegative. The bar is decision-available **only at E[t]=T[t]+3600**, not at its open label. Missing, duplicate, partial, misaligned, nonconsecutive or invalid bars **abort the research run**; no forward fill, imputed zero, fabricated price, or silent `dropna` recovery. The sample must begin with 72 consecutive completed warmup bars, initially FLAT, zero BTC, 10,000 USDT cash, no pending order and no inherited exposure. The first 72 bars are observation only. The first eligible session is a UTC day whose four anchor bars are complete **after** the warmup.

**Fixed UTC Asia-proxy session (researcher choice):** For each UTC calendar day D, take precisely the **four completed** candles with opening UTC hours 00, 01, 02 and 03. After the 03:00 candle closes at **04:00 UTC**, freeze `AsiaLow[D]=min(L[00],L[01],L[02],L[03])` and `AsiaHigh[D]=max(H[00],H[01],H[02],H[03])`; only the low is used for this long-only derivative. If any anchor candle is absent or malformed, abort; the range cannot be constructed from partial candles. No NY timezone conversion, DST handling, London session, previous-day range, rolling Donchian, future pivot or lower-timeframe intrabar data is used.

**Entry setup:** Only a fully completed hourly bar `t` with opening UTC hour **04,05,06,07,08,09,10 or 11** of day D may signal, and only after that day's AsiaLow has been frozen. Define `sweep[t]=(L[t]<AsiaLow[D])`; `reclaim[t]=(C[t]>AsiaLow[D])`; `bullish[t]=(C[t]>O[t])`. All comparisons are **strict**; equality never qualifies. `entry[t]=sweep[t] AND reclaim[t] AND bullish[t]`, while FLAT, no pending order and `usedLow[D]=false`. The low, close and body of **the same fully completed candle** constitute this derivative's confirmation; this is not attributed to the source author's exact Pine logic. On the first qualifying signal set `usedLow[D]=true` immediately and queue one BUY for the next completed bar. The latch resets to false at the next UTC date, but cannot override an existing LONG or pending order. No later same-day retry, including after a failed fill. Unused setups expire after the 11:00-open candle's 12:00 close. No entry on the 00–03 anchor candles.

**Gate 6, causality:** A decision at E[t] uses only known candles through t and a session range frozen at 04:00. BUY cannot fill at E[t] or any earlier timestamp; its historical fill uses the *actual* next completed candle t+1 close, effective time E[t+1]. The signal is latched and the controller emits the order on t+1, rather than leaking `C[t+1]` into the t decision. No future extrema, negative shifts, fitted model, incomplete higher-frame candle or lookahead. A 1h sweep is known only after its complete close; this is **not** a stop-order fill at the wick.

## Required data

Only one real Binance BTC-USDT Spot 1h candle feed: open timestamp, open, high, low, close and base volume. The session reference is derived deterministically from those same candles and UTC timestamps. No real liquidation/stop-run observation is claimed; the wick sweep is an OHLCV proxy. No order book, non-OHLCV flow, second asset, multi-timeframe `request.security`, futures mark/index price, funding or leverage input. Validate all candle continuity and close availability **before** the pinned engine's feature merge/dropna path.

## Execution assumptions

**Gates 2–4, side, position, orders and priority.** LONG/FLAT only on BTC-USDT unleveraged spot, fixed `Q=0.001 BTC`, initial quote cash `10,000 USDT`. States `FLAT`, `BUY_PENDING`, `LONG`, `SELL_PENDING`; exactly one active position and at most one pending order. No short/borrow, simultaneous positions, pyramiding, DCA/safety orders, partial entries/exits, equity compounding, rebalancing, trailing/breakeven stop, intrabar stop/limit/maker order, source NY time-window/other-session trades, or re-entry on a SELL fill bar. No forced end-of-sample liquidation. No hidden controller defaults are assumed.

1. At E[t] when FLAT and entry[t], consume that UTC day's low-sweep attempt and queue a single BUY Q. If t+1 does not exist, do not fabricate a fill; mark the terminal attempt unresolved and fail the completed-trade evaluation. Other signals are ignored while pending.
2. At E[t+1], issue the latched MARKET BUY through the pinned historical OrderExecutor path at **real observed C[t+1] = P**. Require `P>0`, validated row and `cash >= Q*P*(1+f)` with fixed hypothetical `f=0.001` per filled side. Full fill debits quote cash by `Q*P*(1+f)`, records one LONG(Q), and freezes `stop=min(0.999*L[t], 0.99*P)`, `R=P-stop>0`, `target=P+2*R`, `fill_index=t+1`. The `0.999` wick offset and `0.99*P` gap guard are **researcher-defined**, not source defaults; the latter guarantees the stop is below the actual historical fill even if the next candle gaps below the original sweep wick. If the simulator cannot corroborate an actual full fill, fees, or spot cash sufficiency, **abort**; no synthetic partial fills, wallet credit or hidden financing.
3. From the **next** completed bar j>=t+2 while LONG, test **close only**: if `C[j]<=stop`, queue SELL Q (priority 1); else if `C[j]>=target`, queue SELL Q (priority 2); else if `j-fill_index>=24`, queue SELL Q (priority 3, 24 fully completed post-fill bars); otherwise hold. Equality triggers the risk exits; a price gap can produce a much worse next-close sale than the threshold. The bracket levels are frozen at fill, never recalculated. No same-bar stop/TP execution or historical assumption about whether high or low happened first.
4. SELL signal at E[j] queues a MARKET SELL Q at the **next completed** j+1 close, E[j+1]. Full fill credits quote cash `Q*C[j+1]*(1-f)`, realizes `Q*(C[j+1]-P)` gross minus both filled-side quote fees, and returns FLAT. No new entry on j+1 even if an unrelated entry predicate is true. If the SELL is missing, partial, rejected or unaccounted, abort; do not silently flatten.
5. While LONG or pending, ignore all fresh sweeps. A later UTC day can arm a fresh entry only once FLAT and after its complete 00–03 anchor, with `usedLow[D]=false`. If a position remains at the predetermined sample end, mark it to the actual final completed close with realized/unrealized PnL and accrued entry fees; do not invent a terminal sale, closing fee or realized funding. If an exit order is pending at sample end, record it unresolved and do not claim a completed round trip.

**Gate 5, pinned Hummingbot path (static code evidence inspected this cycle):** package `20260920`, `hummingbot/VERSION=dev-2.17.0`, immutable source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Connected GitHub source readback: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists **1h**; `binance_spot_candles.py` REST parser reads `row[0]` as Binance **open timestamp** and `row[1..5]` as actual OHLCV. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` `prepare_market_data` exposes `open_bt/high_bt/low_bt/close_bt/volume_bt` and backward-merges features; `simulate_execution` iterates historical rows, `update_state` sets `close_bt`, then `controller.determine_executor_actions()` processes `CreateExecutorAction`. `hummingbot/strategy_v2/executors/order_executor/data_types.py` `OrderExecutorConfig` supports connector/pair, side, amount, `ExecutionStrategy.MARKET`, `leverage=1`. `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET on the first provided candle at its **actual close**, with `filled_amount_quote=Q*close` and `cum_fees_quote=trade_cost*filled_amount_quote`. `BacktestPositionHold` nets base BUY/SELL, tracks matched realized gross quote PnL, remaining base exposure and cumulative fees. Raw simulator `fill_timestamp` is the candle's **open-time label**; the research **effective/causal** event time is open+3600 seconds. Controller must latch the setup on t and issue BUY on the t+1 completed row, and likewise delay exit; an unshifted t-order would not implement this record. Validate real `close_bt` before each order and reject any generic missing-price fallback. A separate strategy-specific cash sufficiency ledger is required; the MARKET simulator does **not** prove wallet enforcement.

**Economic boundary:** fixed `trade_cost=0.001` per filled side (0.1% quote notional) is a **research hypothesis**, not a verified account fee, exchange slippage, spread, market impact or execution guarantee. Simulator assumes idealized full close-price MARKET fills; real Binance tick/lot/min-notional filters, latency, liquidity and partial fills are unverified. Spot has **no perpetual funding or margin settlement**; funding is **not applicable**, not a measured zero funding stream. No futures mark price, leverage, shared capital or unverified maker/intrabar execution primitive is required. The prior independently reviewed Alpha PR #414 documents source-to-package correspondence for package 20260920; this Scout **did not rehash the installed package or run the engine**, and the independent auditor must confirm the mapping and controller timing before an exact-head PASS merge. This is a **bounded static engine capability argument**, not an implementation or execution test.

## Evidence

### Source-reported
The cited first-party TradingView page by jygirouard (2025-10-22, version 1.3) directly states NY-clock Asia/London windows, sweep of high/low, opposite-color confirmation, one trade per sweep type per session, beyond-wick stop and configurable 2:1 RR default. No source-native fills, Pine revision hash or original performance statistics are asserted.

### Independently reproduced
**None.** No strategy, TradingView, Qlib or Hummingbot backtest or event-level parity run was performed. The pinned source-code inspection above is a capability argument for independent audit only. `hb_ready_status: PASS` is this Scout's **provisional six-gate admission claim**, not an independent auditor decision.

### Negative evidence
This derivative deliberately drops the author's NY session clocks, London session, short/high sweeps and potential separate confirmation bar. Its 1h wick sweep is not proof of actual stop orders or liquidations; its next-completed-close fills are not achievable historical close auctions; its close-only risk and 24-bar timeout materially differ from a live beyond-wick resting stop. If source-native equivalence or actual execution precision is required, this record does **not** supply it.

## Falsification plan

Only after separate implementation and downstream authorization: freeze the exact candle tape and validate 72-bar warmup, UTC four-candle range freeze, strict low sweep/reclaim/body tests, daily consumed latch, one-bar delayed orders, fill-anchored gap-safe stop and 2R target, 24-bar timeout, priority, fee/cash ledger, and open-end marking. Compare the same frozen events against a representative Qlib/Hummingbot replay **before mass screening if this execution/data capability has not already been validated**. Test against a same-session random-entry control and a Donchian false-break control with identical costs, then evaluate IS/OOS without retuning on OOS. No such experiment was performed here.

## Crypto portability

Only BTC-USDT Binance Spot UTC 1h is pinned. The seven-coin campaign, 1h/4h/1d research frames, BO/SO 6/6/6 and 3x/5x futures leverage are **optional downstream experiments**, not admission conditions. Any materially different market, time anchor, execution, DCA or risk overlay must be explicitly derived and revalidated.

## Limitations

Public TradingView prose is sufficiently specific to support the **session-sweep/reclaim/2R inspiration**, but does not expose full Pine bytes; every unverified decision-critical choice is explicitly **researcher-defined**, not silently attributed to the author. No profitable-return, historical Survivor, Qlib parity, production-ready controller, actual fee or live-tradability claim. Static engine inspection is not a run. A 1h close-only exit can realize worse than stop; a BTC-USDT spot model cannot be treated as USDT-M futures without separately validating funding/margin/fill economics.

## Implementation status

not-implemented — no controller code, Qlib recipe, engine run or deployment artifact created. This is research admission, not executable materialization; downstream implementation is a separate engineering step, not a second HB_READY gate.

## Adoption boundary

research-only; implementation_status not-implemented; adoption not-approved; approval_scope research-only. No Paper, Testnet, Live, real order, or automatic strategy deployment is authorized.

## Related Wiki records

No new Wiki record. Nearest mechanisms: existing Turtle Soup Donchian false-break fade, hashem-trader UTC 00 single-candle HIGH breakout, and PuestoGlobal triangle downside trap; all differ in reference construction and event/state rules.

## Sources

- TradingView first party: https://www.tradingview.com/script/6fqUkyaO-ICT-Liquidity-Sweep-Asia-London-1-Trade-per-High-Low/ (jygirouard, 2025-10-22, strategy v1.3, inspected 2026-10-30).
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (VERSION, Binance Spot 1h feed, backtesting engine, OrderExecutor simulator/config).
- Prior package/source correspondence evidence (not rehashed in this cycle): https://github.com/HCH725/alpha-strategy-research/pull/414 .
