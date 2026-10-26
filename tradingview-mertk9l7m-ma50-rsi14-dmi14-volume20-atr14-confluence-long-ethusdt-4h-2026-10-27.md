---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "mertk9l7m five-filter MA50/RSI/DMI/volume/ATR confluence with five independent exits — ETH-USDT spot 4h long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-09-07
sources:
  - https://www.tradingview.com/script/i5cYs2nw/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# mertk9l7m MA50/RSI/DMI/volume/ATR confluence — independent ETH-USDT spot 4h long-flat derivative

## Provenance

**Primary source:** mertk9l7m, *MS - Crypto RSI-Based Trading Strategy*, public TradingView open-source script **i5cYs2nw**, published **2025-09-07**, first-party description inspected **2026-10-27**: https://www.tradingview.com/script/i5cYs2nw/ . The description explicitly states **all-of-five BUY**: price above MA50 with 5% buffer; RSI between 50 and 70; +DI > -DI; volume 1.5 times its moving average; ATR below its average. It states **any-of-five SELL**: price below MA50 with 5% buffer; RSI < 45; -DI crosses above +DI; volume below 0.5 times its average; ATR above its average. The page labels the script open-source, but complete Pine bytes, revision hash, original exact indicator seeds/lengths, order flags, exchange/fill model, and backtest metrics were **not retrieved**. No claim is made about unseen Pine logic.

**Explicit independent executable derivative v1 — not source-native or lossless.** Researcher-chosen: Binance ETH-USDT **spot UTC 4h**, LONG/FLAT; SMA50 of close; Wilder RSI14, Wilder DMI14 and ATR14; 20-bar arithmetic means of volume and ATR; strict thresholds and a false-to-true entry edge; 100 completed bars warmup; SELL predicates used as full LONG exits (rather than an inferred source short); fixed 0.01 ETH; completed-bar t decision to t+1 **historical modeled close** MARKET fill; 0.1% hypothetical per-side fee; no stop/target/DCA. Interpret “5% buffer” as C > 1.05*SMA50 for BUY and C < 0.95*SMA50 for SELL; interpret “between 50 and 70” strictly and volume 1.5x as a strict greater-than. These interpretations, data horizon, indicator lengths and order behavior are researcher-defined and can change trade events. Original Pine equivalence is **not** asserted.

**Immutable derivative identity:** TradingView:i5cYs2nw | mertk9l7m | publication:2025-09-07 | derivative-v1:2026-10-27 | Binance ETH-USDT spot UTC4h | SMA50(C) buffered 1.05/0.95 | WilderRSI14 50<RSI<70 / exit RSI<45 | WilderDMI14 +DI>-DI / bearish DI cross | V>SMA20(V)*1.5 / exit V<SMA20(V)*0.5 | WilderATR14<SMA20(ATR14) / exit ATR14>SMA20(ATR14) | first-all-five-true entry edge | next-completed-bar modeled CLOSE fills | fixed 0.01 ETH | warmup100 | modeled fee 0.001/side. A change to any parameter, edge, fill timing, market, sizing, or exit creates a new derivative.

**Dedup:** Current main at `ac0b447a7f593bf0e5d6e6032189ba0508177294` contains 376 root-level strategy Markdown records; connected GitHub default-branch searches for `i5cYs2nw` and `mertk9l7m` returned no match, and open research/* PRs and open PR searches showed no matching source. Nearby RSI/DMI/volume records use different trigger/exit mechanisms; this candidate's **simultaneous buffered-MA, RSI-band, DI-direction, high-volume and low-ATR conjunction with five independent sell exits** is material, not a trivial RSI length variant. Do not duplicate it on parameter tweaks.

## Economic mechanism

### Source-reported

The author describes buying an uptrend with momentum in a bounded RSI zone, positive directional movement, elevated participation and below-average volatility; any loss of trend, momentum, DI control, participation or low-volatility regime signals selling. The first-party page does not provide independently validated returns or executable Pine details.

### Research interpretation

This derivative tests whether the five-way entry confluence followed by an asymmetric five-way **OR exit** offers a distinct regime-conditioned return distribution after modeled fees. It does **not** claim that the source's sell conditions were actually implemented as long exits, or that the source's original market and execution semantics are reproduced.

## Signal

All rules here define the **researcher-authored derivative**, not hidden source facts. Use finite chronological ETH-USDT spot UTC 4h OHLCV with strictly positive O/H/L/C, V>=0, L<=min(O,C)<=max(O,C)<=H, exact opening timestamps `T[t+1]-T[t]=14400` seconds, no gaps/duplicates/incomplete last candle. Reject invalid segments, never interpolate or manufacture prices. Compute indicators sequentially in float64 without rounding comparisons; fill/cash/fee ledger uses Decimal.

1. **SMA50(C):** arithmetic mean of completed closes C[t-49..t], defined for t>=49. **SMA20(V):** mean V[t-19..t], defined for t>=19. Current t is included only after t is completed. If SMA20(V)=0, no entry (volume condition cannot pass).
2. **Wilder RSI14(C):** for t>=1, delta=C[t]-C[t-1], gain=max(delta,0), loss=max(-delta,0). Seed average gain/loss at t=14 as the arithmetic means of t=1..14 differences; thereafter each is (13*previous+current)/14. RSI=100-100/(1+avgGain/avgLoss) when avgLoss>0; RSI=100 if only gain>0, 0 if only loss>0, 50 if both zero. No RSI values before t=14.
3. **Wilder DMI14 and ATR14:** for t>=1, TR=max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1])); up=H[t]-H[t-1], down=L[t-1]-L[t]; +DM=up if up>down and up>0 else 0; -DM=down if down>up and down>0 else 0. Seed smoothed TR, +DM and -DM at t=14 as the sums over t=1..14. For t>14 update each smoothed sum S[t]=S[t-1]-S[t-1]/14+raw[t]. Define +DI=100*smoothed(+DM)/smoothed(TR), -DI analogously, and ATR14=smoothed(TR)/14. Require smoothed TR>0; otherwise indicators invalid and segment aborts. Ties in up/down give both DM=0. ADX is **not** used.
4. **SMA20(ATR14):** mean of 20 valid ATR14 values t-19..t, first valid t=33. All signals require non-NaN positive ATR14 and its SMA. No fitted parameter or future reference.
5. Define entry conjunction B[t] = (C[t] > 1.05*SMA50[t]) AND (50<RSI14[t]<70) AND (+DI14[t]>-DI14[t]) AND (V[t]>1.5*SMA20(V)[t]) AND (ATR14[t]<SMA20(ATR14)[t]). All comparisons strict. Define **new confluence** E[t]=B[t] AND NOT B[t-1]. Researcher-defined edge suppresses repeated BUY while a condition remains true. t=0..99 are warmup NO-TRADE; t=100 is the first eligible decision and B[99] is used for its edge.
6. When FLAT, no pending order, and t strictly after last exit-fill bar, E[t] schedules exactly one full BUY for next completed bar t+1; do not use t+1 inputs in the decision. The pinned historical OrderExecutor MARKET simulation fills 0.01 ETH at the **observed C[t+1]**; the economic fill is effective no earlier than `T[t+1]+14400`, even though the engine indexes the row by opening timestamp. If no next full bar or actual close exists, do not fill. Abort on invalid/partial/rejected fill, failed trading-rule validation or insufficient modeled cash; never use synthetic fallback prices.
7. While LONG with no pending order, after the entry-fill bar, define five exits at each completed t: (a) C[t]<0.95*SMA50[t]; (b) RSI14[t]<45; (c) -DI[t]>+DI[t] AND -DI[t-1]<=+DI[t-1]; (d) V[t]<0.5*SMA20(V)[t]; (e) ATR14[t]>SMA20(ATR14)[t]. If **any** is true, schedule one full SELL at actual observed C[t+1] in the historical MARKET simulator. Store all reasons in order (a,b,c,d,e) for diagnosis; one SELL only. No intrabar stop/target, no guaranteed exit price and no same-bar exit on the entry-fill bar. If the final bar emits an exit without a next full bar, leave inventory marked but not fictitiously sold.
8. After confirmed full SELL fill set FLAT, reset pending, remember exit-fill bar; no BUY on that same bar. A later completed t>exit_fill_bar requires a **fresh E[t]**. Ignore entry edges while LONG/pending and ignore repeated exit signals while pending. Never queue them. One pair, one full-sized long, at most one pending order, no short, borrow, leverage, hedging, pyramiding, partial fills, Safety Orders, DCA, rebalancing, time exit, stop loss, take profit, trailing stop, external override, cooldown timer or concurrent position. Unbounded downside to zero is a disclosed risk; no hidden protective stop.
9. Initial cash Decimal("10000") USDT and zero ETH. Fixed filled quantity Q=Decimal("0.01") ETH. Fee f=Decimal("0.001") of fill notional on **each** side; BUY cash -= Q*P*(1+f), inventory += Q; SELL cash += Q*P*(1-f), inventory -= Q. Full-fill round-trip net PnL = Q*(sellP-buyP)-f*Q*(buyP+sellP). Reject cash deficit or amount/min-notional/precision conflicts rather than assuming exchange acceptance. At sample end mark unsold ETH at last actual completed close and report unrealized value separately, no fabricated liquidation/fee. Segment restart resets state and requires full warmup. No compounding, funding, margin or interest: spot has no perpetual funding leg; no imaginary zero-funding observations.

## Required data

Only one real Binance ETH-USDT **spot 4h** historical OHLCV feed, validated as complete and ordered with original exchange candle **open** timestamps; exact 4h UTC boundaries and next close-availability timestamps are mandatory. Indicator calculations consume only <=t completed bars. No order book, non-OHLCV feed, multiple markets, higher-timeframe synchronization or intrabar event reconstruction. A valid historical close is required for every modeled fill. Missing data, invalid precision or an unavailable fill price are blockers, not zero-valued inputs or guessed values.

## Execution assumptions

**Pinned Hummingbot source directly read using connected GitHub app on 2026-10-27:** `HCH725/hummingbot` commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, repository `hummingbot/VERSION` = **dev-2.17.0**; existing admission package label **20260920**. The historical package/source byte mapping was reported in separately reviewed Alpha PR #414; this run did **not** independently rehash an installed package or run a backtest.

- **Real data/market path:** pinned `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `4h`; `binance_spot_candles.py::_parse_rest_candles` maps actual Binance row[0] to candle **open** timestamp and row[1..5] to O/H/L/C/V. `BacktestingDataProvider.initialize_candles_feed` and `get_candles_df` support a `binance_ETH-USDT_4h` feed. No claim that this run downloaded any ETH candles.
- **Controller/executor path:** pinned `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution="4h",trade_cost=0.001)` uses controller-provided candles and trading rules. `simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`. A **future minimal candidate-specific controller** must calculate the stated predicates/state and delay actions by one completed bar; none has been written. A generic executor name alone does not implement this strategy.
- **Actual simulator primitive:** `OrderExecutorConfig(connector_name="binance",trading_pair="ETH-USDT",side=BUY/SELL,amount=Decimal("0.01"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. In pinned `order_executor_simulator.py`, MARKET fills on first supplied row at that row's actual `close`; `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. This is an **idealized full-fill historical close model**, not a real post-close executable market price, next-open execution, or guaranteed order acceptance.
- **Timestamp and leakage boundary:** engine row `timestamp` is Binance **opening** time and `update_state(row)` can see its close; therefore a candidate controller must **only dispatch stored prior t signal on row t+1**, never derive the decision from t+1 close. Record the modeled fill's **effective availability** as t+1 close, not the engine's raw row timestamp. Validate full contiguous candles and features **before** `prepare_market_data`'s backward `merge_asof`/dropna to prevent silent missing-bar removal. No same-row re-entry.
- **Ledger/cost path:** pinned `BacktestPositionHold._process_order` nets opposite base quantities and records gross matched realized PnL; `add_executor` separately tracks fees. Reconcile net realized PnL, cash and final marked inventory from the complete full-fill ledger; do not call gross PnL fee-net. Preserve all terminated executor evidence across 4h bars. `BacktestingDataProvider.get_price_by_type` can default to Decimal("1") on missing price; **forbid that fallback**, validate actual candle close before action, abort otherwise. Connector quantization/trading rules must be checked; exchange min-notional, live slippage, partial fills, spread and real fee tier are **not proven**.
- **Gate 5 scope:** pinned reusable capability covers one Binance spot 4h OHLCV feed, deterministic controller actions, full MARKET historical close fills, fees and position netting. This derivative requires no unverified intrabar, multi-asset, perpetual, non-OHLCV or live execution path. Missing candidate controller is implementation work, not evidence that its code exists. A new execution primitive requires representative validation before mass Qlib screening.

## Evidence

### Source-reported

TradingView publication **2025-09-07** specifies the five BUY predicates and five alternative SELL predicates cited in Provenance. No claimed source win rate, Sharpe, return, stop-loss, commission, fill timing or specific market was reproduced.

### Independently reproduced

**None.** No TradingView Pine replay, Hummingbot/Qlib strategy run, event-level parity, installed-package hash, profitability, OOS, Survivor or HB Certified result. Direct pinned-source **capability inspection only**.

### Negative evidence

Complete original Pine/revision and precise indicator defaults were not retrievable. Researcher pins of RSI/DMI/ATR/volume lengths, MA buffer direction, strict ties, long-exit interpretation, edge, next-bar close fills, market, quantity and fees are **not** source-native. Original short behavior, original stops, Pine fill rules and original performance cannot be inferred. Historical MARKET close full fills ignore actual slippage, spread, latency and partial fills.

### Six-gate HB_READY proposal (requires independent Hermes Auditor)

1. **Deterministic:** SMA50, RSI14 Wilder seed, DMI14 Wilder TR/DM seed, ATR14 and its SMA20, volume SMA20, strict thresholds, confluence rising edge and warmup pinned.
2. **Direction:** ETH-USDT Binance spot LONG/FLAT; source sell predicates mapped explicitly to LONG exits; short/borrow disabled.
3. **Entry/exit/risk:** exact all-of-five entry and any-of-five exit with bearish-DI cross definition; no SL/TP/trailing/time exit; loss risk disclosed.
4. **Position/state:** Q=0.01 ETH, cash/fee ledger, full-fill pending order, one position, no DCA/pyramiding/concurrency/cooldown, fresh-edge re-entry.
5. **Pinned engine:** inspected 20260920/dev-2.17.0 source commit, actual Binance 4h feed, controller/action path, MARKET historical close simulator, fee/POSITION_HOLD netting, missing-price and timestamp limitations.
6. **Causality:** 100 completed-bar warmup; signal t from <=t, modeled fill t+1 close only after its availability; no future bars, uncompleted candles or early open-timestamp claims.

`hb_ready_status: PASS` is the **Scout's review proposal**, not self-approval; independent exact-head Auditor decides admission.

## Falsification plan

On separately authorized implementation, test indicator seeds/ties, MA 1.05/0.95 interpretations, DI crossover strictness, first all-of-five edge, repeated-predicate suppression, five-way exit priority, next-completed-bar fill availability, cash/fees and position netting, data gaps, zero volume, missing-price guard, rejected/partial fill abort, last-bar pending orders and final mark. Demonstrate one representative Hummingbot/Qlib event-level parity of the strategy/execution path before large-scale Qlib screening **if** that path introduces an unverified primitive. A failed capability or unexplained event/cost discrepancy blocks downstream use; it does not license invented fills. No backtest is run by Scout.

## Crypto portability

ETH-USDT spot UTC 4h is a research-only derivative choice, not source-proven profitability or an admission whitelist. Other coins, timeframes, futures 3x/5x, BO6/SO6/SO6 or intrabar stops are separately declared execution experiments, never silently overlaid as source-native.

## Limitations

Original Pine source revision and trade-processing defaults are unavailable; this is an explicitly independent derived strategy. Fee 0.1% is a hypothetical model assumption, not an asserted Binance tier; no realized funding is claimed. Historical next-close full fills are idealized and not a promise of real tradability. No implementation, Qlib parity, survivor qualification, HB certification or trading authorization.

## Implementation status

**not-implemented.** No dedicated candidate controller, Qlib executable recipe, backtest or deployed system is created here. Future selected research may require minimal strategy-specific materialization without a second admission registry.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** Hermes Auditor GitHub Webhook Review alone handles source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. Existing signed GitHub webhook receiver alone handles post-merge README count. Scout does not merge/approve/close, modify main, backtest, trade or change schedules.

## Related Wiki records

None created or modified. No private Wiki or private user data is included.

## Sources

- mertk9l7m, *MS - Crypto RSI-Based Trading Strategy*, TradingView public script i5cYs2nw, published 2025-09-07, inspected 2026-10-27: https://www.tradingview.com/script/i5cYs2nw/
- Pinned Hummingbot commit: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Pinned Binance spot candles: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py
- Pinned backtesting engine: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Pinned order simulator: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
