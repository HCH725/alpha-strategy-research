---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "dgtrd Elder-Ray negative Bear Power recovery in rising EMA13 — independent BTC-USDT spot 1d long-flat derivative"
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
source_as_of: 2026-10-27
sources:
  - https://www.tradingview.com/script/fadiBynQ-Bull-vs-Bear-Power-by-DGT/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# dgtrd Elder-Ray negative Bear Power recovery in rising EMA13 — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary first-party source:** dgtrd (DGT), *Bull vs Bear Power by DGT*, public TradingView open-source **indicator** with stable script ID **fadiBynQ**, published **2020-08-03**, directly inspected **2026-10-27**: https://www.tradingview.com/script/fadiBynQ-Bull-vs-Bear-Power-by-DGT/ . The page documents Bull Power = High − EMA13(Close), Bear Power = Low − EMA13(Close), an upward EMA13 slope and negative-but-rising Bear Power as the **two mandatory** Elder-Ray long conditions. Higher Bull Power peaks and bullish divergence are explicitly optional filters. The page also describes optional CDMI, smoothing and visualization; those are **not** mandatory long conditions. The accessible page mentions a Pine v6 upgrade in release notes but does not expose complete current Pine bytes, an immutable code revision or source-native executable order rules. Do not attribute any research-defined order to the author's indicator.

**Independent executable derivative v1, NOT lossless/source-native Pine:** researcher fixes BTC-USDT Binance spot UTC 1d, EMA seeding, the exact entry edge, a separately designed exit, sizing, warmup, completed-close/next-close simulation, cash/fee accounting and disabled behaviors. The author's optional divergence, Bull Power peak comparison, CDMI, smoothing, short and adding-to-position guidance are **disabled**, not silently treated as source-native omissions. No original author performance or trade equivalence is claimed.

**Immutable derivative identity:** `TV:fadiBynQ | dgtrd | published:2020-08-03 | page-as-of:2026-10-27 | independent-derivative:v1:2026-10-27 | Binance BTC-USDT spot UTC 1d | EMA13 SMA-seeded | Bear=Low-EMA | fresh negative-rising Bear + rising EMA entry | Bear>=0 OR EMA non-rising exit | one 0.001 BTC long | t signal -> t+1 close-model fill | fee 0.001 per filled side | 50-bar warmup`.

**Dedup on main SHA `aa2c50d42794858bdf2c332bd79aa1a24920528c`:** README 380; root-level strategy Markdown records 380 (tree not truncated). Exact TradingView script ID `fadiBynQ` absent in main code search and all-state PR search; ten open research PR descriptions were inspected, none this source or these rules. Nearest existing family `forven-elder-ray-bull-power-cross-long-flat-btcusdt-1h-2026-10-17.md` enters on **Bull Power (High−EMA13) crossing above zero**, exits when Bull Power falls below zero or EMA declines. This derivative enters on **negative but rising Bear Power (Low−EMA13)** with an EMA trend gate and exits on Bear Power recovering to nonnegative or EMA trend failing; its triggering candle sets, high-versus-low dependency and exit sets differ materially, not a trivial parameter change. Existing Elder-Impulse and 123/Elder combos also have distinct multi-leg mechanisms. No claim of exhaustive frontmatter re-audit from numerical equality.

## Economic mechanism

### Source-reported

Elder-Ray compares the day's extremes with the 13-period EMA consensus. Negative Bear Power that becomes less negative while the EMA rises indicates a potential pullback recovery inside an upward trend. The primary page identifies these two conditions as mandatory long-side conditions; divergence and recent Bull Power peak confirmation are optional.

### Research interpretation

The derivative tests whether a *new* recovery in sellers' inability to push lows far below rising consensus can identify a long entry, and exits when that recovery reaches/non-crosses the EMA from below or the EMA trend fails. This exit is **researcher-designed**, not attributed to dgtrd or Elder. No positive expectancy is asserted.

## Signal

All indexed bars are contiguous **completed** UTC 1d Binance spot candles. `t` is the zero-based bar index; `O[t],H[t],L[t],C[t],V[t]` are finite actual OHLCV values. Reject any nonpositive price, H<L, C outside [L,H], missing or duplicated bar, non-finite value, or absent modeled fill close. Computation is chronological float64 with no future inputs or full-sample fitting.

1. **EMA13(Close):** `E[12]=sum(C[0..12])/13`. For `t>=13`, `E[t]=E[t-1]+(2/14)*(C[t]-E[t-1])`. `Bear[t]=L[t]-E[t]` for `t>=12`; `Bull[t]=H[t]-E[t]` is optional diagnostic only and never gates orders. No alternate EMA seed or smoothing.
2. **Source-inspired mandatory long conditions:** `R[t]=(E[t]>E[t-1]) AND (Bear[t]<0) AND (Bear[t]>Bear[t-1])` for `t>=13`, strict comparisons; equality is false. No divergence, CDMI, Bull Power top, stochastic, other indicator, optimization or Heikin-Ashi.
3. **Researcher-defined entry edge:** after exactly **50 fully completed bars of no-trade warmup** (`t=0..49`), begin FLAT. At `t>=50`, while FLAT and no pending action, schedule one BUY only if `R[t]=true AND R[t-1]=false`. A gate already true at warmup boundary does not create a synthetic entry. If insufficient quote cash or invalid price/size, fail closed and do not queue a retroactive fill.
4. **Researcher-defined exit:** while LONG and no pending action, schedule one full SELL if `Bear[t]>=0 OR E[t]<=E[t-1]`. If both, label Bear recovery primary; if only EMA fails, label trend failure. Bear Power ceasing to rise while remaining negative is **not** itself an exit. No protective stop, take profit, trailing, time stop or forced terminal liquidation. A flat exit is a no-op.
5. **Priority/state:** SELL decision has priority if LONG; BUY only if FLAT. At most one action pending; no simultaneous BUY and SELL, no intra-bar re-entry. Signals update every completed bar even while LONG or pending, so a later BUY requires a **new** false-to-true R edge after exit. No discretionary cooldown, except the engine's necessary fill reconciliation: a bar used to fill a pending order cannot itself issue another action; resume evaluating for new actions at the first subsequent fully reconciled bar. Rejected actions are not queued or retried without a fresh qualifying edge.
6. **Direction/position:** spot LONG/FLAT only, fixed **0.001 BTC** per entry, full liquidation of actual filled base quantity on exit. Initial modeled quote cash **10000 USDT**, zero BTC; no reinvestment or compounding. Cash debit on BUY is `0.001*fill_close*(1+0.001)`; cash credit on SELL is `filled_qty*fill_close*(1-0.001)`. Insufficient cash skips the order. Gross realized quote PnL is separate from both side fees; mark residual BTC at last observed completed close for unrealized quote PnL. No leverage, short, borrow, futures, funding, margin, multi-asset capital, DCA, safety orders, pyramiding, partial exits, averaging, or hidden stop/target defaults.

## Required data

Exactly one historical Binance **BTC-USDT spot UTC 1d** OHLCV feed; the decision inputs are completed high/low/close and historical continuity. No lower/multi-timeframe, cross-asset, order-book, mark/index, open interest, funding, news or fitted-model dependency. Binance REST kline `row[0]` is the **opening** timestamp `T[t]`; the earliest availability of H/L/C for this bar is `A[t]=T[t]+86400 seconds`. Enforce strictly consecutive daily opening timestamps and no partial current bar. A new segment rewarms from FLAT; never interpolate missing candles or silently drop data with `dropna`.

## Execution assumptions

**Pinned source inspection (connected GitHub app):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION=dev-2.17.0`; admission package label `20260920`. Package-to-commit wheel hash equivalence was **not rechecked** this cycle. This is a strategy-specific controller specification, **not** a claim that an executable controller already exists.

- **Feed:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` contains the 1d interval; `binance_spot_candles.py::_parse_rest_candles` reads `row[0]` timestamp and `row[1..5]` OHLCV. Before `BacktestingEngineBase.prepare_market_data()`, validate all requested historical candles, continuity, and close availability; the engine's `merge_asof/dropna` does not establish integrity.
- **Controller:** a future minimal strategy-specific controller computes prefix-only EMA/Bear/R and queued `t` decisions. `BacktestingEngineBase.simulate_execution()` calls `update_state(row)`, then `determine_executor_actions()`, then routes `CreateExecutorAction(OrderExecutorConfig)` through `simulate_executor()`. At engine row `t+1`, issue only the previously stored completed-bar `t` action, never a decision derived from `t+1` prices.
- **Executor:** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1,position_action=OPEN/CLOSE)`. Pinned `OrderExecutorSimulator` MARKET fills on the **first supplied row at its actual close**, with `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. An exit SELL reduces an existing spot long; it does not create a naked short. `trade_cost=0.001` per filled side is an explicit **hypothetical** research fee, not an exchange-observed Binance fee.
- **Timestamp:** the raw simulator fill timestamp is the `t+1` candle **open** label, while the modeled price is its **close**. Store research effective fill availability as `A[t+1]`, never pretend the next close was known at `T[t+1]`. This is a **historical next-completed-close full-fill convention**, not a claim that a live market order can guarantee the close price. No intrabar, maker, stop-fill, latency, spread, slippage or partial-fill path is asserted.
- **Accounting:** pinned `BacktestPositionHold._process_order` nets opposite-side filled base quantities, tracks weighted entry and **gross** realized PnL, and `add_executor` accumulates fees separately. Reconcile the complete executor ledger to explicit cash/BTC inventory and net PnL, preserving stopped POSITION_HOLD executors and final flush; do not let terminated-executor view pruning erase exposure. `BacktestingDataProvider.get_price_by_type` may default to `Decimal("1")` when price is missing; this fallback is **forbidden**: prevalidate actual prices and abort rather than fabricate.
- **Boundaries:** this pinned spot-only model has **no perpetual funding obligation**, not a modeled zero-funded futures position. Exchange min-notional, base precision, actual fee tier, liquidity, slippage and partial fills are **not** established by the simulator. Reject unverified production execution claims; no Hummingbot/Qlib parity or installed package rehash performed.

**Six gates (proposed, independent review required):** (1) exact EMA seed, Bear formula, strict rising edge, warmup, validation; (2) spot LONG/FLAT only; (3) defined entry, full exit, disabled risk behavior; (4) single fixed position, pending/fill/cash state, no DCA/concurrency, fresh-edge re-entry; (5) pinned Binance 1d feed, controller/action route, MARKET next-row close model, POSITION_HOLD netting, fee ledger and timestamp limitations inspected; (6) only completed prefix data, 50-bar warmup, decision at A[t], historical modeled fill effective A[t+1], no future input or missing-price invention. PASS is a Scout proposal only.

## Evidence

### Source-reported

dgtrd TradingView script `fadiBynQ`, published 2020-08-03, page inspected 2026-10-27: EMA13 consensus; Bear Power low minus EMA13; mandatory rising EMA and negative-but-rising Bear Power for basic long interpretation; optional divergence/Bull Power top filters; CDMI and smoothing are optional indicator features. No source-native order event timing, source exit, fee or backtest result is imported.

### Independently reproduced

**None.** No source-Pine replay, candidate backtest, Qlib/Hummingbot event-level parity, economic performance, real fills or HB certification. Pinned Hummingbot source-path inspection is compatibility evidence, not independently reproduced trades.

### Negative evidence

Complete current Pine bytes and revision hash not available through inspected primary page. All entry edge, exit, market, amount, fee, warmup and execution semantics beyond the documented indicator conditions are independent researcher choices. Next-close historical full fill is not real executable pricing; no protective stop exists; no exchange precision, wheel hash or actual cost proof. No profitable-return or Survivor claim.

## Falsification plan

On separately authorized implementation, run representative event-level Hummingbot/Qlib parity for this strategy path before mass screening: compare EMA/Bear/R transitions, entry-edge and exit events, stored decision availability, t+1 close-effective fill timestamps, size, fees, cash/BTC inventory and terminal positions. Reject the hypothesis if its net outcomes are unstable or if actual execution cannot reproduce the declared timing; never treat historical same-close prices as guaranteed live fills. No test or trade is authorized by this record.

## Crypto portability

Only Binance BTC-USDT spot UTC 1d is asserted for this immutable derivative. Other symbols, horizons, perpetuals, leverage and optional BO/SO overlays are **downstream experiments**, not HB_READY admission filters; any change to signals/position events is a newly disclosed derivative and any new engine primitive requires representative capability validation.

## Limitations

Indicator-inspired, **not** source-native Pine. The optional Elder divergence and DMI features are disabled; exit is researcher-authored. Historical MARKET full fills at the next completed close ignore spread/slippage and cannot be represented as live post-close execution. No bounded stop loss, Qlib parity, real costs or profit evidence.

## Implementation status

`not-implemented`: no dedicated controller, Qlib recipe, deployment or backtest artifact. A selected candidate requires minimal strategy-specific materialization, not another admission registry.

## Adoption boundary

`research-only / not-approved / research-only`. Independent Hermes Auditor GitHub Webhook Review owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README reconciliation. Scout makes no main/README changes, self-review, merge, trading or environment edits.

## Related Wiki records

None created. Compare admitted Forven Bull Power zero-cross, Elder-Impulse dual slope and 123/Elder combo only as distinct relatives.

## Sources

- Primary: https://www.tradingview.com/script/fadiBynQ-Bull-vs-Bear-Power-by-DGT/
- Pinned engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Current admission policy: https://github.com/HCH725/alpha-strategy-research/blob/aa2c50d42794858bdf2c332bd79aa1a24920528c/.github/HB_READY_REVIEW.md
