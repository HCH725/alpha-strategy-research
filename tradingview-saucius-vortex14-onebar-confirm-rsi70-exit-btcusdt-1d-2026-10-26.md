---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "saucius Vortex14 one-bar high confirmation and RSI14-70 exit — independent BTCUSDT spot long-flat derivative"
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2020-12-22
sources:
  - https://www.tradingview.com/script/ELam0FmE/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# saucius Vortex14 one-bar close/high confirmation + RSI14 crossunder-70 exit — independent derivative

## Provenance

**Public primary source:** saucius, *Vortex and RSI ts 2020*, TradingView public open-source strategy, published **2020-12-22**, stable script ID **ELam0FmE**, source page checked **2026-10-26**: https://www.tradingview.com/script/ELam0FmE/ . The directly accessible first-party description states **long-only**, entry when positive Vortex crosses above negative Vortex plus a "second test" of a close above the prior high, and exit when RSI crosses **below 70**, or negative Vortex crosses above positive Vortex with a close below the prior low. It mentions fixed money management but does not expose its exact value in the accessible prose. The complete Pine revision, parameter defaults, source execution timing, stop/target settings, and precise meaning/timing of the second test were **not** recovered. Open-source page labeling is not evidence that its complete code was read.

**This is an explicitly independent researcher-defined executable derivative, NOT source-native/lossless Pine.** The researcher freezes the standard Vortex(14), Wilder RSI(14), a **one-completed-bar** post-cross confirmation window, fixed spot BTC-USDT daily bars, a bounded same-processed-row-close MARKET backtest convention, 0.001 BTC unit size, 10,000 USDT starting cash, a fixed hypothetical 0.1% fee per filled side, warmup and state handling below. The original may use other lengths, a different second-test latch, different money management or order timing. These are declared choices, **not attributed to saucius**. Short, stop-loss, take-profit, trailing, time exit, DCA and all other unstated behaviors are disabled in this derivative; no performance or source-equivalence is asserted.

**Immutable identity:** `TV:ELam0FmE|saucius:2020-12-22|derived-v1-VI14-bull-cross-arm1-close>priorHigh-RSI14-Wilder-crossunder70-or-VI14-bear-arm1-close<priorLow|BinanceSpot:BTC-USDT:1d|long-flat:0.001BTC|same-row-close-synthetic:fee0.001|2026-10-26`. Any change to thresholds, confirmation duration, RSI/Vortex variant, market, execution, fee or state logic is a separately disclosed revision.

**Dedup, current main:** GitHub connector main SHA `9c2c720b1e52de0abf64cfffa212e3052f8780ec` (349 root-level strategy Markdown files, README count 349); exact TradingView ID `ELam0FmE` absent in default-branch code search. No open `research/*` PR or open PR search matched the ID, author/rule pairing or this two-stage mechanism. Related main mechanisms are NantzOS Vortex14+SMA50 **immediate** cross entry, Vortex spread-EMA threshold, and standalone RSI reversals; this strategy instead **arms on a Vortex cross, confirms against the preceding cross bar's high/low on the immediately following completed bar, and exits by either RSI70 crossunder or confirmed bearish Vortex**. This changes trade-event topology, not just a parameter. Other open research PRs concern distinct mechanisms.

## Economic mechanism

### Source-reported

Vortex dominance crossover proposes a direction, with a separate price-strength test to avoid unconfirmed flips; a downward RSI70 crossing is an overbought-momentum decay exit, with a symmetric bearish Vortex/price weakness alternative. The source's public description supplies no verified profitability, win rate, transaction cost or event-level data.

### Research interpretation

Freeze a strictly one-bar confirmation rather than an unbounded "second test" to make causality and signal lifetime reproducible. The two exit routes compete: an RSI70 downward cross exits immediately on its completed bar, while a bearish Vortex cross requires the next completed bar to close below the bearish-cross bar's low. This is a research interpretation, not a claim about the inaccessible Pine logic.

## Signal

**Gate 1: formulas and deterministic comparisons.** Index strictly consecutive, completed UTC daily Binance spot bars `t=0,1,...` with `O[t],H[t],L[t],C[t],V[t]`. For `t>=1`: `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`; `VMplus[t]=abs(H[t]-L[t-1])`; `VMminus[t]=abs(L[t]-H[t-1])`. For `t>=14`, `VIplus[t]=sum(VMplus[t-13..t])/sum(TR[t-13..t])`, and `VIminus[t]` analogously. If the denominator is not finite and strictly positive, indicators are undefined and the bar is ineligible. Bull cross at `t`: `VIplus[t]>VIminus[t]` AND `VIplus[t-1]<=VIminus[t-1]`. Bear cross: `VIminus[t]>VIplus[t]` AND `VIminus[t-1]<=VIplus[t-1]`. Strict equality never confirms a new crossing.

**RSI14 variant:** `delta[t]=C[t]-C[t-1]`; gain=`max(delta,0)`, loss=`max(-delta,0)`. Seed average gain and average loss at `t=14` with arithmetic means of `t=1..14` gains/losses. Thereafter each Wilder RMA is `(13*previous + current)/14`. RSI = `100-100/(1+avgGain/avgLoss)`; when loss=0 and gain>0, RSI=100; gain=0 and loss>0 gives RSI=0; both zero gives RSI=50. RSI bearish exit cross is `RSI[t]<70 && RSI[t-1]>=70`. No other oscillator smoothing or signal filter.

**Gate 2 and Gate 3: LONG/FLAT only, no shorts.** Start FLAT. If FLAT and unarmed at eligible completed bar `t`, a bull Vortex cross sets `entry_arm=(t,H[t])`, **without buying yet**. On exactly the next completed bar `t+1`, buy 0.001 BTC iff `C[t+1]>H[t]` and the cash guard succeeds; otherwise discard the arm. A crossing on any earlier bar cannot be carried forward. While LONG, an RSI14 crossunder 70 causes an immediate synthetic completed-row-close SELL, taking priority over any bearish Vortex arm. Otherwise a bear Vortex cross at `t` sets `exit_arm=(t,L[t])` without selling. On exactly `t+1`, SELL iff `C[t+1]<L[t]`; if RSI crosses under 70 on that same bar, SELL by RSI first, with exactly one SELL action. Failed price confirmation discards the arm. If both are absent, hold. No fixed stop, take-profit, trailing, forced time exit, reversal, or end-of-sample liquidation; the final open position remains open and can only be marked at a genuinely observed valid price.

**Gate 4: complete state.** `FLAT, ENTRY_ARMED, PENDING_BUY, LONG, EXIT_ARMED, PENDING_SELL` are mutually exclusive. Process a matured arm before any new cross; while any arm or pending order exists, ignore new arm requests. An RSI exit while EXIT_ARMED overrides the arm. A confirmed fill (not order submission) advances PENDING_BUY to LONG or PENDING_SELL to FLAT. Rejected/failed/unfilled actions do not create phantom holdings: reconcile the executor outcome; failed BUY returns FLAT, failed SELL retains LONG, both clear the stale arm, and no order is automatically retried. No re-entry on the same bar as a SELL, and subsequent entry requires a fresh bull cross on a later completed bar. Exactly one spot position, maximum 0.001 BTC, no pyramiding, safety orders, DCA, cooldown beyond fresh-cross/re-entry rules, compounding, shared capital, or simultaneous strategies.

## Required data

**Gate 6:** one Binance `BTC-USDT` spot `1d` OHLCV stream. Bar `t` has an **opening** timestamp `T[t]` at UTC midnight and is decision-available only at `T[t]+86400s` once finalized. Require **80 consecutive valid completed bars** before first decision; this exceeds RSI seeding, Vortex prior-high/low dependence and previous-cross requirements. Require `T[t]-T[t-1]=86400s`, finite strictly positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, `H>=L`, finite nonnegative V, and complete bar-close availability. Any gap, duplicate, non-monotonic, malformed or incomplete bar **invalidates that research run**; never drop/forward-fill/interpolate gaps or fabricate a price. No `request.security`, incomplete higher-timeframe candle, repainting, hindsight pivot, negative shift, lookahead join, cross-asset data, fitting or ML preprocessing. The next-bar confirmation reads only that bar once complete; no advance knowledge of its close is used at the prior cross bar.

## Execution assumptions

**Gate 5: bounded pinned Hummingbot engine, not live execution.** Admission baseline is Hummingbot package label **20260920**, VERSION **dev-2.17.0**, source pin `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle inspected the pin's `hummingbot/VERSION`, `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py`, `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` through the GitHub app. Package-to-commit **binary digest was not independently revalidated**; previously independently reviewed same-path evidence is in alpha PR #417. If that binding cannot be substantiated, the independent auditor must fail Gate 5 rather than presume it.

- **Data/controller:** BinanceSpotCandles REST parser uses kline `row[0]` as bar-**open** timestamp and `row[1..5]` for O/H/L/C/V. A strategy-specific, not-yet-implemented controller computes the above Vortex/RSI and arm state on completed daily bars only. `BacktestingEngineBase.simulate_execution` updates row state, invokes `determine_executor_actions`, and sends `CreateExecutorAction` to the executor simulator. `prepare_market_data` has a backward as-of join/dropna, which is **not** a proof of bar-completion or gap safety: the strict continuity and close-availability preflight above is required.
- **Executor/fill:** `OrderExecutorConfig` for `connector_name=binance`, `trading_pair=BTC-USDT`, `ExecutionStrategy.MARKET`, `TradeType.BUY/SELL`, `PositionAction.OPEN/CLOSE`, `amount=Decimal("0.001")`, `leverage=1` and `price=None`. The inspected `OrderExecutorSimulator.simulate` fills MARKET in full at the **first supplied processed row's close**, marks `CloseType.POSITION_HOLD`, and computes quote notional/fees from that close. **This is a synthetic completed-row-close research fill**, not evidence a real order submitted after candle close can fill at the observed close. No maker, intrabar touch, next-open, partial fill or actual exchange order is assumed. The engine retains the bar-**open** label internally: report the derivative's economic decision/fill availability as `T[t]+86400s`, never `T[t]`; a controller or report that uses the raw open label as decision time violates Gate 5/6.
- **Position/fee ledger:** `BacktestPositionHold` in the pinned engine nets filled equal-base BUY/SELL, tracks weighted entry, gross realized quote PnL and `cum_fees_quote` separately. Use persistent fill-confirmed position state and `terminated_executors_window=None` (or a verified equivalent), rather than relying on the default one-hour terminated-executor view for daily events. No synthetic trade is created when an action fails. Reject any missing/nonpositive actual observed close: `BacktestingDataProvider.get_price_by_type` can return a fallback `Decimal("1")`; **never** treat that fallback as a BTC trade price.
- **Research cash and costs:** initial unborrowed cash `10,000 USDT`. A BUY requires `cash >= 0.001*C[t]*(1+0.001)`, then modeled cash decreases by that amount. A SELL increases cash by `0.001*C[t]*(1-0.001)`. Pin `run_backtesting(trade_cost=0.001)` as a **hypothetical 0.1% fee on each filled side**; for entry `Pb` and exit `Ps`, net quote realized PnL is `0.001*(Ps-Pb) - 0.001*0.001*(Pb+Ps)`. Do not mistake gross native PnL for net-of-fee equity or subtract fees twice. The simulator does not add separate slippage/spread/market impact; **not** a claim of zero real costs. Spot borrowing/leverage/futures funding are **inapplicable**, not assumed zero funding for a perpetual. Real commissions, precision, lot size, minimum notional, liquidity, partial fills and production latency are unverified and not claimed.

**Capability boundary:** the inspected and previously reviewed single-market spot daily OHLCV → controller → MARKET first-row-close → POSITION_HOLD/fee ledger is the only claimed research path. This record neither relies on nor asserts a new intrabar, multi-timeframe, maker, futures or cross-asset path. A future executable controller must demonstrate its close-effective timestamps and arm transitions; if the pinned engine cannot enforce them, Gate 5 fails. The above is a bounded **expressibility precheck**, subject to independent Hermes Auditor review, not a backtest or implementation.

## Evidence

### Source-reported

The TradingView page identifies the 2020-12-22 author/title, long-only Vortex bullish cross + higher-than-prior-high confirmation, RSI70 downward-cross exit, and bearish Vortex cross + lower-than-prior-low exit. No numeric backtest claim is carried forward.

### Independently reproduced

**None.** No TradingView Pine source revision was reconstructed, no source-native trade series reproduced, no Hummingbot/Qlib backtest run, and no candidate event-level parity or profitability result obtained. Pinned generic engine code paths were inspected through GitHub, with package digest limitation disclosed. The record proposes six-gate PASS for this **derived** specification only; the independent reviewer owns the actual admission decision.

### Negative evidence

Accessible source prose does not specify Vortex/RSI lengths, whether the second test is immediate or delayed, order fills, sizing, exact money management, stops or transaction costs. The researcher independently fixed these, and does not present them as original author facts. No support is claimed for real after-close fills at the just-observed close, exact exchange fees, realized slippage, next-open or intrabar stop fills. Any unavailable candle or price blocks the run instead of using a fabricated value.

## Falsification plan

Before downstream Qlib mass screening, independently calculate both Vortex components and RSI14 from a frozen contiguous BTC-USDT daily sample; check bull/bear tie crossings, RSI70 ties, one-bar confirmation expiration, simultaneous RSI/armed-exit precedence, unaffordable BUY, rejected action, duplicate executor visibility, and terminal open position. On the **existing** verified execution path, check one representative Qlib/Hummingbot event ledger for correct signal time, close-availability time, BUY/SELL ordering, 0.001 BTC size, synthetic price, gross/net fees and position state; a **new** execution primitive requires separate representative capability validation before mass screening. Do not infer profitability from HB_READY; freeze IS/OOS and research cost assumptions downstream. No testing or trading was executed by Scout.

## Crypto portability

This independent derivative explicitly selects Binance BTC-USDT spot 1d. Other assets/timeframes, 6/6/6 DCA, 3x/5x isolated futures and multi-asset portfolios are **optional separate downstream experiments**, not admission gates and not silently source-native. Any change in trade events requires its own declared derivative and compatible economic model.

## Limitations

The original Pine bytes, strategy property defaults and precise "second test" implementation remain unverified. A one-bar confirmation can differ materially from the original. No protective stop; gap invalidation may interrupt evaluation while a position is held. The close-effective MARKET model is synthetic and is not a realizable live-fill promise. The pinned package/source digest and production trading economics remain unverified. PASS is neither Qlib parity, survivor qualification, profitability nor trading authorization.

## Implementation status

`not-implemented`: no strategy-specific controller, Qlib executable recipe, replay or deployment artifact created. Implementation materialization, if separately authorized, is downstream engineering work and not a new HB_READY gate.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. No merge, self-approval, Paper/Testnet/Live order, Qlib/Hummingbot run, container change or cron change. Independent Hermes Auditor GitHub Webhook Review decides exact-head PASS merge or NOT_LOSSLESS close.

## Related Wiki records

- TradingView first-party source: https://www.tradingview.com/script/ELam0FmE/
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting
- Prior independently reviewed generic spot MARKET/POSITION_HOLD capability: https://github.com/HCH725/alpha-strategy-research/pull/417
