---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "trade_lexx MACD Sniper negative/positive histogram three-run deceleration — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-29
sources:
  - https://www.tradingview.com/script/ZtEWSrDj-macd-sniper-trade-lexx/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# trade_lexx MACD Sniper histogram three-run deceleration — independent research derivative v1

## Provenance

**First-party source:** trade_lexx, *MACD Sniper [trade_lexx]*, public TradingView **open-source indicator** (not an executable strategy), script identity **ZtEWSrDj**, originally published **2025-03-10**, last page-listed revision **2025-07-29**, primary URL https://www.tradingview.com/script/ZtEWSrDj-macd-sniper-trade-lexx/ . Public first-party page read **2026-10-29**. Its accessible description states: (a) a BUY histogram signal when the MACD histogram is below zero and starts increasing after a user-set minimum run of falling columns; (b) a SELL histogram signal when the histogram is above zero and starts decreasing after a minimum run of rising columns; (c) optional minimum bars between signals and wait-for-opposite-signal mode; (d) distinct MA crossover and combined modes; and (e) optional RSI, MFI, Stochastic, Supertrend filters in later revisions. The complete original Pine bytes, original defaults, precise zero/equality semantics and a hash of the July 2025 source revision were **not retrieved**. This record is NOT an assertion of source-native Pine equivalence.

**Independently defined derivative:** Select **histogram-only** mode; conventional EMA MACD(12,26,9) with SMA seeds; exactly **three consecutive strict histogram declines** before a negative-zone bullish turn, or three consecutive strict rises before a positive-zone bearish turn; no RSI/MFI/Stochastic/Supertrend, MA-cross or combined signal; wait-for-opposite-position-state enabled; no separate signal cooldown; Binance BTC-USDT **spot 1h UTC**, long/flat, fixed 0.001 BTC, 120 complete-bar warmup, one-bar-delayed **observed next completed close** historical MARKET fill, hypothetical 0.1% quote-notional fee per side, no price stops or targets. All lengths, histogram tie handling, state, timing, sizing, fees, venue and disabled optional features are **researcher choices**, not original-source facts. The author supplies the histogram exhaustion mechanism, not this exact executable specification.

**Immutable derivative identity:** `TradingView:ZtEWSrDj:trade_lexx:published20250310:updated20250729|independent-derived-v1-20261029|BINANCE:BTC-USDT:SPOT:UTC1h|EMA12-26-SIGNAL9-SMA-seeds|negative-HIST-3-strict-down-then-up=BUY|positive-HIST-3-strict-up-then-down=SELL|LONG-FLAT|warmup120|Q0.001BTC|initial10000USDT|signal-complete-t-to-next-complete-close-t+1|fee0.001-per-filled-side`. Changes to any signal, timing, size, exit or accounting parameter constitute a different derivative; the TradingView ID identifies lineage, not immutable original Pine bytes.

**Pre-write dedup:** GitHub connector main SHA `fc09fde6ed46970c21e291a1874ff6ea44ae1597` has a complete, nontruncated tree with **428** root strategy Markdown files (430 root Markdown files minus README.md and README.zh-TW.md); README count **428**. Eight distributed sampled strategy frontmatters carry `hb_ready_status: PASS`; this is not a full 428-file audit. GitHub default-branch searches for `ZtEWSrDj` and `MACD Sniper` found no matching record; all ten open `research/*` PR bodies were inspected for this source/author and none matched, and an all-state PR search for the script ID returned none. The admitted trade_lexx RSI-smoothed Bollinger record uses a **different TradingView script and RSI/Bollinger signal**. The closest MACD records use histogram **zero crossings**, MACD/RSI event confluence, or Bollinger %B with MACD sign; none uses the source's **strict three-column pre-turn negative/positive histogram run** as the entire long-entry/exit state. Do not count this as a novel generic MACD family; novelty is the specified run-length exhaustion event and its exact source lineage.

## Economic mechanism

The source proposes histogram deceleration while still below zero as a bullish exhaustion cue and histogram deceleration above zero as a bearish exhaustion cue. The derivative tests whether **a strict three-decline / three-rise run followed by a single opposite histogram slope** is useful for one long-only spot position. It can enter while MACD momentum remains negative and exit while it remains positive. No historical profit, source backtest, or independent replication is claimed.

## Signal

1. **Inputs and time:** One contiguous chronological stream of actual completed Binance BTC-USDT spot 1h candles, indexed t=0,1,...; UTC open timestamp T[t], completed availability E[t]=T[t]+3600 seconds. Require unique T, exactly 3600-second increments, finite positive O/H/L/C, L<=min(O,C)<=max(O,C)<=H, finite nonnegative V. Reject gaps, duplicates, incomplete candles, synthetic/forward-filled OHLCV and missing real prices; abort the segment instead of inventing a bar. Features are float64 with deterministic sequential arithmetic; modeled order ledger uses Decimal.
2. **EMA12 and EMA26 on completed close:** For n in {12,26}, `EMA_n[n-1]=mean(C[0..n-1])`, and for t>=n `EMA_n[t]=(2/(n+1))*C[t]+(1-2/(n+1))*EMA_n[t-1]`. EMA undefined before its seed. `MACD[t]=EMA12[t]-EMA26[t]` first defined at t=25.
3. **MACD signal9:** `SIG[33]=mean(MACD[25..33])`; for t>=34, `SIG[t]=(2/10)*MACD[t]+(8/10)*SIG[t-1]`. `HIST[t]=MACD[t]-SIG[t]` first defined at t=33. These seeds, lengths and numeric comparisons are independent-derivative pins, not claims of byte-identical Pine/TA-Lib initialization.
4. **Strict bullish turn:** `B[t] = (HIST[t]<0) AND (HIST[t-4]>HIST[t-3]>HIST[t-2]>HIST[t-1]) AND (HIST[t]>HIST[t-1])`. Thus exactly three **strict declines** ending at t-1, followed by a strict upward turn on t while still negative. No equality, zero crossing, MACD line crossover, RSI or volume filter qualifies.
5. **Strict bearish turn:** `S[t] = (HIST[t]>0) AND (HIST[t-4]<HIST[t-3]<HIST[t-2]<HIST[t-1]) AND (HIST[t]<HIST[t-1])`. Thus three **strict rises** followed by a strict downward turn while still positive. B and S cannot co-occur because their histogram signs are mutually exclusive. On equality or missing history, both are false.
6. **Warmup and causality:** t=0..119 are **120 complete-bar warmup only**; earliest decision t=120, earliest fill E[121]. No pre-warmup signals are carried. Every predicate on t reads only completed closes <=t. No full-sample fitting, lookahead, negative-shift future reference, higher-timeframe partial bar or repainting. All event clocks use E[t], not the exchange candle-open T[t].
7. **Decision priority and state:** Initially FLAT with zero BTC and 10,000 USDT research cash. When FLAT, no pending order and B[t], queue BUY; when LONG, no pending order and S[t], queue SELL of all confirmed BTC. Otherwise HOLD. EXIT-before-ENTRY priority is explicit (though B and S are disjoint); a fill bar never generates another decision. Wait-for-opposite-signal behavior is enforced by FLAT/LONG state, not by an invented extra filter. A new strict B event after a completed exit may re-enter; no carryover or re-arming from an earlier event.
8. **Historical fill:** A completed signal at E[t] queues exactly one MARKET action for bar t+1. A minimal future candidate-specific controller would dispatch the stored action on row t+1; the pinned simulator uses the **actual observed C[t+1]** as its historical MARKET fill, with economic effective time **E[t+1]**, not T[t+1]. The row's open-time index must not be misrepresented as the fill's information availability. No decision on t uses C[t+1]. Ignore any new signal on the fill row; earliest later decision is t+2. No bar t+1 means no fill; no invented price, open or terminal liquidation.
9. **Exposure and risk:** One full-fill Q=Decimal("0.001") BTC long maximum; FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT. No shorts, borrow, margin, leverage, pyramiding, simultaneous positions, DCA, Safety Orders, partial profit-taking, rebalancing, reverse-on-same-bar, independent cooldown, session guard, fixed SL, TP, trailing, break-even, time exit or forced liquidation. These are deliberately **disabled**, not hidden engine defaults. The long may remain open indefinitely if S never occurs. If a pending order is rejected, partially filled, duplicated, stale, unaffordable or not reconciled, abort research rather than fabricate a confirmed position.
10. **Research cash and fees:** Use Q=0.001 BTC, initial cash=10,000 USDT, fee f=Decimal("0.001") on each actually modeled full BUY/SELL notional. BUY requires cash>=Q*P*(1+f), debits that amount and credits Q BTC; SELL requires confirmed Q inventory, debits Q BTC and credits Q*P*(1-f). Matched net PnL = Q*(P_sell-P_buy)-f*Q*(P_buy+P_sell). Track cash, BTC, pending side, last fill row, entry price and accumulated fees. At tape end, mark an unclosed long at the final actual completed close as **unrealized**, not a phantom SELL. Real historical Binance fee tier, spread, impact, partial fills, precision/min-notional and order acceptance are **unverified**, not asserted to be zero. This is spot without perpetual funding; no fabricated realized zero-funding observation.

## Required data

Only one actual Binance BTC-USDT spot UTC 1h OHLCV feed, with at least 120 complete consecutive warmup bars and one subsequent real candle for each simulated fill. No non-OHLCV features, ML, multi-asset synchronization, cross-timeframe interpolation, maker/limit/intrabar fills or funding series. Every run must validate real close and the chronological candle schedule before feeding the engine; an absent candle is not a valid fill. Other pairs/timeframes or futures economics are **not** implicitly supported by this derivative.

## Execution assumptions — pinned Hummingbot Gate 5

**Pinned source inspected through the connected GitHub app on 2026-10-29:** `HCH725/hummingbot` immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label **20260920**, repository `hummingbot/VERSION` **dev-2.17.0**. Prior merged Alpha PR **#414** is existing independent package/source byte-equivalence and representative primitive evidence; this Scout did **not** rerun its wheel checks or execute candidate backtests.

- **Actual candle path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly supports `1h`. `binance_spot_candles.py` parses Binance Kline row[0] as open timestamp and rows[1..5] as O/H/L/C/V. `BacktestingDataProvider` initializes the declared `binance_BTC-USDT_1h` candle feed. Validate real contiguous rows before `prepare_market_data` merges/drops feature rows; no silent gap repair.
- **Actual controller/executor path:** `BacktestingEngineBase.run_backtesting` loads controller/config/feed and `simulate_execution` iterates rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction(OrderExecutorConfig)` to `simulate_executor`. The required MACD run-state controller is **not implemented** and is not claimed to be a shipped Hummingbot controller; it would use the already demonstrated one-row delayed decision/state primitive only.
- **Actual MARKET model:** `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1)` uses the pinned `OrderExecutorSimulator.simulate`, which fills MARKET at the **first supplied row's observed close**; `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. Explicitly dispatch the stored t decision only at row t+1; do not use row t+1 close to generate that decision. This is an idealized historical **next-completed-close** model, NOT evidence of a realizable live close-price market order.
- **Actual position and cost path:** `BacktestPositionHold.add_executor` nets BUY/SELL quantities, tracks gross realized matched PnL and separately accumulates `cum_fees_quote`. Research net PnL must subtract modeled fees; reconcile complete executor ledger, base inventory and fee-inclusive quote cash on each confirmed fill (tolerance <=1e-9 BTC and <=1e-6 USDT for float/Decimal conversion). Keep complete terminated-executor/position-hold history; do not rely on a pruned one-hour view. Abort any unexplained ledger mismatch.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` may return `Decimal("1")` for a missing pair; **never** use this fallback as a market price. Require actual positive C[t+1] before a fill and actual final close for marking. Binance trading-rule initialization and quantization hooks do not prove historical tick/lot/min-notional, fee tier, live liquidity or order acceptance. No intrabar, next-open, maker, leverage, perpetual funding, shared-capital or unverified price path is claimed. Simulated `trade_cost=0.001` is a declared hypothetical research fee, not a measured Binance fee.
- **Gate 5 conclusion:** The **bounded** one-pair spot OHLCV, prior-decision/next-completed-close MARKET full-fill and fee/position-hold accounting primitives are directly supported by pinned source and previously independently validated in #414. A new strategy-specific controller and representative Qlib/Hummingbot event-level parity are downstream engineering prerequisites before mass screening on an unverified execution path, not evidence of a current candidate backtest.

## Evidence

**Source-reported:** the public TradingView page reports negative histogram turning up after a configurable falling-column run, symmetric positive histogram turning down after a rising run, optional signal separation and opposite-signal mode. It also describes alternate MA cross/combined modes and optional filters, all **disabled** here. No original source code, default histogram count, author fee model or performance has been independently verified.

**Independently reproduced:** **None.** No TradingView Pine execution, Qlib/Hummingbot candidate replay, trade-event parity, actual historical fills, returns, OOS, Survivor or HB Certified result. This Scout inspected pinned engine source and reused #414 primitive evidence only.

**Negative evidence:** Original Pine source bytes and revision hash unavailable; EMA seeds, run count, exact histogram edge semantics, disabled optional filters, BTC-USDT venue, timing, position, costs and state are explicitly independent research choices. A missing actual price, bad timestamp, unknown fill or unverified material engine primitive fails closed. No profit or live-execution claims.

### Six-gate Scout proposal — independent Auditor decision required

1. **Determinism:** SMA-seeded EMA12/26, signal9, histogram strict three-run reversal with all equality/initialization choices, fixed market/frame/warmup.
2. **Direction:** Binance BTC-USDT unleveraged spot LONG/FLAT only; original sell signal becomes long liquidation, not a short.
3. **Entries/exits/risk:** exact B/S conditions and opposite exit; no SL/TP/trailing/time exits or hidden defaults.
4. **Position/state:** fixed 0.001 BTC, cash and fee ledger, single pending order, no DCA/pyramiding/concurrency, no same-fill-row reentry, no extra cooldown.
5. **Pinned engine:** directly inspected Binance 1h candle parser, real MARKET close-fill simulator, controller action dispatch, fee and POSITION_HOLD accounting, and missing-price fallback guard at pinned commit; source/wheel correspondence evidence is reused, not newly asserted.
6. **Point-in-time:** 120 complete-bar warmup, only <=t completed-bar features, t decision at E[t] and modeled t+1 close fill effective at E[t+1]; no future leak or false open-time fill.

`hb_ready_status: PASS` is the **Scout's research-only submission** and **NOT** an independently audited or merged finding.

## Falsification plan

If separately authorized downstream, compare (a) strict three-decline/three-rise histogram reversal versus (b) simple one-bar histogram slope reversal and (c) MACD line/signal crosses, each as **separate derivatives**, with fixed IS/OOS and research costs. Audit SMA/EMA seeds, zero/equality, three-run counting, no-signal flat periods, indefinite long holds, pending and fill-row suppression, fee-inclusive cash/PnL, final unrealized inventory, actual candle gaps, timestamp availability, fallback price rejection and exact executor ledger. Require representative Qlib/Hummingbot event-level capability parity before broad screening of any newly used execution path.

## Crypto portability

This identity is **BTC-USDT spot 1h only**. Other symbols, 1d/4h, futures 3x/5x, BO/SO 6/6/6 and shared capital are optional **separately declared downstream campaigns**, never HB_READY entry gates. DCA changes events and must be a separately labeled derivative.

## Limitations and adoption boundary

This is an indicator-inspired independent strategy, not an original Pine backtest or source-native reconstruction. A three-run histogram turn can be late, noisy or absent for long periods; no stop caps drawdown. The historical MARKET close-fill is an idealization, not guaranteed live execution; fee tier, slippage, precision, exchange order acceptance, real funding, strategy-specific controller implementation and profitability are unverified. **Research only**: no implementation, adoption, trading or deployment authorization. Independent Hermes Auditor GitHub Webhook Review alone decides exact-head PASS merge or NOT_LOSSLESS close; this Scout must not merge, approve, alter main or update README.
