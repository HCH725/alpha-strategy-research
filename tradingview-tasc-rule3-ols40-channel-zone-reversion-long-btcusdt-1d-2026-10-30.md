---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "PineCodersTASC Rule 3 OLS40 residual-extreme channel-zone reversion BTC spot 1d long-flat — independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/nTdxANi4-TASC-2025-05-Trading-The-Channel/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TASC 2025.05 Rule 3 — OLS40 residual-extreme channel-zone reversion (BTC-USDT spot 1d independent derivative)

## Provenance

**Primary TradingView source:** PineCodersTASC, *TASC 2025.05 Trading The Channel*, published 2025-04-17, stable public script ID `nTdxANi4`, publicly labeled open-source, first-party description inspected 2026-10-30: https://www.tradingview.com/script/nTdxANi4-TASC-2025-05-Trading-The-Channel/ . This page attributes the concepts to Perry J. Kaufman's May 2025 TASC article; the article and original Pine bytes were not independently verified. No immutable Pine source hash or version is available from this inspection.

**Source-native statements verifiable on that page:** the script offers three different rule sets. Rule 3 ("Trade within the channel") enters a long near the channel low and a short near the channel high, with optional slope-direction filter. The linear-regression channel is based on maximal historical distances from the fitted regression line to observed prices. The period default is 40, regression source default close, channel range source default close, zone-width default 20% of channel range, optional trend filter default OFF, optional percent stop default OFF, and default auto sizing applies to equities/futures (Manual is needed for other symbol types). No default commission or slippage is provided. These statements are **not** proof of the uninspected Pine implementation or its order timing.

**Independently derived strategy, NOT a source-native/lossless reproduction:** this record selects only Rule 3, specifies an exact trailing-40 OLS plus signed maximum-residual channel and strict zone-entry comparisons, converts the source's upper-zone short/reversal concept into a full long exit, disables shorting and trend filter, selects BTC-USDT Binance spot daily data and manual fixed-unit sizing, adds a 60-completed-bar warmup, explicit position/cash state, next-completed-close historical MARKET fills and declared hypothetical research costs. These researcher-defined rules can change original trade events; no Pine parity is claimed.

**Immutable derived identity:** TradingView `nTdxANi4` / publication 2025-04-17 / source Rule 3 / independent derived spec v1 frozen 2026-10-30 / OLS40-close residual-extreme channel / lower-20%-zone cross entry and upper-20%-zone level exit / Binance BTC-USDT Spot UTC 1d / long-flat / next-completed-close historical full-fill / 0.001 BTC. Later source edits do not alter this frozen specification.

**Dedup on main `9278fdb1ed674da94e65e1b3c5b3541d22cb41fa`:** 460 root-level records, README 460, and 11 open research PRs inspected. The sole `nTdxANi4` record in main is `tradingview-tasc-linreg40-slope-sign-long-flat-btcusdt-1d-2026-10-25.md`, which selects **Rule 1** (regression-slope sign flips; no channel-zone events). This Rule 3 mechanism is materially different, not a parameter variant. `linreg-channel-band-touch-two-sided-btcusdt-1d-2026-10-12.md` uses a 100-bar residual-sigma channel, slope/EMA50 gates, two-sided touch/reject and midline exits; `forven-linreg-channel-breakout-long-flat-btcusdt-1h-2026-10-17.md` uses a 50-bar +2-sigma breakout and midline exit. Neither uses Rule 3's residual-extreme 40-bar **20%-of-range zones** with lower-zone entry and upper-zone full exit. No open research PR references this TradingView ID or these normalized rules. Independent Auditor must recheck dedup at review time.

## Economic mechanism

### Source-reported

Kaufman's channel-zone rule treats price near a fitted channel's lower extreme as a potential mean-reversion long and price near its upper extreme as a potential short/reversal. The source provides no verified profitability, crypto market or transaction-cost evidence.

### Research interpretation

Long-only channel-zone reversion: enter on a fresh move into the bottom fifth of the trailing regression residual-extreme envelope; exit when price reaches the top fifth. Unlike Rule 1, slope sign does not gate trades; unlike a breakout, price moves **into** the lower zone to enter. No statistical claim of mean reversion or positive expectancy is made.

## Signal

**All arithmetic and comparisons below are researcher-frozen; none are asserted as recovered Pine code.** Let `C[t]` be finite, positive, completed daily close; indexes increase chronologically, starting at 0.

1. At each `t >= 39`, use `C[t-39],...,C[t]` and `j=0,...,39`. Compute `m[t] = sum((j-19.5)*C[t-39+j] for j=0..39)/5330` (OLS slope, because `sum((j-19.5)^2)=5330`), `a[t] = mean(C[t-39..t]) - 19.5*m[t]`, `L[j,t] = a[t]+j*m[t]`, `R[j,t] = C[t-39+j]-L[j,t]`.
2. `rmax[t]=max(R[0..39,t])`; `rmin[t]=min(R[0..39,t])`; `lower[t]=L[39,t]+rmin[t]`; `upper[t]=L[39,t]+rmax[t]`; `W[t]=upper[t]-lower[t]`. With `W[t] <= 0` or any nonfinite input, no signal; malformed input aborts the research run. This is a **signed residual-extreme** channel, not standard-deviation bands, Donchian high/low, or future-known extrema.
3. `low_zone[t]=lower[t]+0.20*W[t]`; `high_zone[t]=upper[t]-0.20*W[t]`. Zone boundaries are inclusive on the inside.
4. **BUY event** at completed bar `t` iff `t>=60`, state FLAT, `W[t-1]>0`, `W[t]>0`, `C[t-1]>low_zone[t-1]` and `C[t]<=low_zone[t]`. This is a fresh cross **into** the bottom zone, not a standing low-zone level. Changing regression boundaries can cause a zone crossing without an identical raw-price change; this is deliberate and causal.
5. **SELL event** at completed bar `t` iff `t>=60`, state LONG, `W[t]>0`, and `C[t]>=high_zone[t]`. This is a **level** test, not an edge test: a still-upper-zone close on a later eligible bar can exit a position entered earlier. It closes the full filled long. If both zone tests could appear in raw features, position state makes only one side eligible; the strict `W>0` also separates low and high zones.
6. Before bar 60 (the first 60 completed candles, indexes 0..59), observe indicators but emit no orders and hold FLAT. First eligible decision is bar index 60, using completed prior-zone bar 59. There is no hindsight seeding, entry from an already-low zone, signal on incomplete data or forced end-of-sample liquidation.

## Required data

Single Binance `BTC-USDT` spot 1d OHLCV feed. Only historical completed **close** and the UTC candle-open timestamp affect signals; O/H/L/V are checked for integrity. Require consecutive UTC open timestamps separated by 86400 seconds, finite positive O/H/L/C, `low<=open,close<=high`, `low<=high`, finite nonnegative volume, and at least 61 completed candles. Reject duplicate/gapped/nonmonotonic rows, unfinished final candle, missing or invalid prices and nonfinite regression values; do not interpolate, forward-fill or substitute a synthetic close. Validate raw rows **before** `prepare_market_data()` can drop NaNs or merge features.

A Binance candle's stored `timestamp=T[t]` is its **OPEN** time, not when its close becomes known. Decision availability is `E[t]=T[t]+86400` UTC. All regression and zone computations for `t` use only the 40-bar prefix through completed bar `t`; prior-zone comparisons use a separately completed 40-bar prefix through `t-1`. No higher-timeframe incomplete data, future bar, repainting, fitted full-sample artifact or external feed.

## Execution assumptions

**Pinned Hummingbot engine:** package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout directly read at this commit `hummingbot/VERSION`, `data_feed/candles_feed/binance_spot_candles/constants.py` and `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `backtesting_data_provider.py`, `executors_simulator/order_executor_simulator.py`, and `executors/order_executor/data_types.py`. The accepted Alpha PR #414 is prior representative package/source primitive evidence; this cycle did not rehash a wheel or run a candidate backtest.

- **Real pinned data/model path:** `BinanceSpotCandles.INTERVALS` includes `1d`; the REST Kline parser stores the actual opening timestamp and O/H/L/C/V. `BacktestingDataProvider` loads historical candles and `BacktestingEngineBase.prepare_market_data()` exposes `close_bt`/`close` after row assembly. A **future strategy-specific** controller, not present today, must prevalidate completeness/gaps and implement the exact OLS40 zones before sending any actions.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution()` updates the processed row, invokes `controller.determine_executor_actions()` and dispatches `CreateExecutorAction` to `simulate_executor()`. `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY or SELL, amount=Decimal("0.001"), execution_strategy=MARKET, price=None, leverage=1, position_action=OPEN or CLOSE)`. SELL reduces the recorded spot base inventory, never opens a short. The pinned `OrderExecutorSimulator` MARKET branch fills at the **actual first supplied row close**, records `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`. `BacktestPositionHold` nets BUY/SELL quantities, tracks gross realized PnL and fees separately; its gross realized PnL must **not** be mislabeled fee-net equity.
- **Causal modeled fills:** decide after completed `t` at `E[t]`; store at most one pending action and dispatch it on the `t+1` processed row. Model a retrospective full MARKET fill at the **observed `C[t+1]`**, with economic fill availability `E[t+1]`, even though engine row index is the candle-open `T[t+1]`. Do not use `C[t+1]` in the earlier `t` signal. No other action is emitted on the fill row; the next eligible decision is `t+2`. A pending action without a completed next bar is canceled unfilled. This is a bounded **idealized historical next-completed-close** convention, not an assertion that a live order can execute at a past close or that close equals next open.
- **Position/state:** initial cash 10000 USDT, base 0 BTC, fixed `Q=Decimal("0.001")` BTC. Exactly one long unit maximum, no pyramiding, DCA, safety orders, compounding, partial exits, shared capital, simultaneous markets, margin, borrow, leverage, cooldown (other than mandatory fill-row suppression), discretionary stop, stop-loss, take-profit, trailing exit, timed exit, overnight/session filter or forced terminal close. State FLAT/LONG plus at most one pending BUY/SELL; filled exposure changes only after verified simulator full fill. Flat SELL/long BUY are no-ops. Failed BUY does not create phantom long or delayed fill; a **new** lower-zone crossing is required. After SELL a new lower-zone cross can re-enter.
- **Explicit hypothetical cost/cash ledger:** research fee `f=Decimal("0.001")` (0.1% of filled notional **per side**), passed as `trade_cost=0.001` to the pinned simulator. BUY requires `cash>=Q*P*(1+f)`; then `cash-=Q*P*(1+f)`, `base+=Q`. SELL requires `base==Q`; then `cash+=Q*P*(1-f)`, `base=0`. Quote fee-net round trip = `Q*(P_sell-P_buy)-f*Q*(P_buy+P_sell)`; open equity = cash + base*last_valid_close. Do not double-count fees already deducted by this separate ledger. Missing price, impossible inventory or negative cash => fail closed. Research fee is **not** a verified exchange tier; modeled zero spread/slippage and full fill are explicit historical idealizations, **not** observed zeros. Real lot/tick precision, min-notional, live order acceptance, partial fills, liquidity and actual fees are **unverified** and no live exchange-valid order claim is made. Spot has no perpetual funding/margin/liquidation leg; no fictitious futures funding is introduced. `BacktestingDataProvider.get_price_by_type` has a fallback `Decimal("1")`; this derivative **forbids** its use as a missing trade price.
- **Fail-closed boundary:** no short/maker/limit/intrabar/multi-asset/next-open execution primitive is required. This record asserts compatibility only with the bounded pinned historical MARKET-close research model, not real trading economics or an implemented controller.

## Evidence

### Source-reported

TradingView first-party description: Rule 3 near-low long/near-high short, period 40, close regression/range sources, 20% zone width, optional slope filter disabled, optional stop disabled, default auto sizing unsuitable for crypto without Manual, and no specified commission/slippage. No source-reported performance number is adopted.

### Independently reproduced

None. No original Pine event stream, strategy-specific controller, backtest, profitability, Qlib/Hummingbot event parity, OOS or Survivor status was independently reproduced. The pinned engine **source capability** paths were read directly; accepted PR #414 is prior representative evidence, not a candidate-specific execution result.

### Negative evidence

Pine bytes/revision, original zone tie handling, channel residual arithmetic, original short/long reversal timing and source execution economics remain unverified. The exact OLS40 residual-max/min channel, fresh lower-zone cross, upper-zone level exit, BTC spot long-flat stance, fixed 0.001 BTC, warmup, fill clock and hypothetical fees are explicitly independent derived decisions. Real exchange order acceptance and fees are not verified. Rule 1 in main shares source identity but not signal mechanism; the regression band-touch and breakout records use materially different events.

## Six-gate Scout assessment (proposal, not independent audit)

1. **Deterministic:** frozen OLS40 regression, signed residual-extreme envelope, inclusive 20% zones, strict prior-bar crossing, width/NaN handling and explicit 60-bar warmup.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; source's short side intentionally disabled.
3. **Entries/exits/risk:** fresh lower-zone entry, upper-zone level full exit; no other order or protective behavior.
4. **State:** one filled 0.001 BTC unit, cash/fee ledger, one pending, no DCA/pyramiding/concurrency, fill-row suppression and fresh-cross re-entry.
5. **Pinned engine:** actual 1d spot feed, controller-action/MARKET simulator, close-price fill, position-hold netting and hypothetical quote-fee ledger examined at exact pinned commit; no unsupported execution path is asserted.
6. **Causality:** completed UTC daily bars, explicit open-vs-close availability, two independent trailing prefixes, `t` decision to `t+1` historical close fill, no future decision input or hidden next-open assumption.

The `hb_ready_status: PASS` field is **this Scout's proposed research-only six-gate admission** for the declared independent derivative, not independent Hermes Auditor approval, source-native equivalence, profitability, Qlib parity, HB Certified Survivor or live authorization.

## Falsification plan

Not run. Future adversarial cases: flat 40-bar window; ties at either zone boundary; lower-zone cross caused by moving channel; gap/missing price; 60-bar warmup boundary; upper-zone exit immediately after BUY fill; cash insufficiency; pending action on last bar; duplicate timestamp; fee-net equity versus gross `BacktestPositionHold` PnL; long signal while already long; rejection of future/repaint data. If a new engine primitive is needed, perform representative Qlib/Hummingbot event-level validation before mass Qlib screening; this record does not run it.

## Crypto portability

The source did not pin BTC or 1d. This derivative's single spot pair and daily frame are research selections, not universal HB_READY restrictions. Other assets/frames, shorts, original auto sizing, futures leverage/funding, 6/6/6 DCA, slope filter or different zone width require a separately declared derived version and capability check; none is silently source-native.

## Limitations

No Pine-byte parity, independent returns, real order-book fills, exchange lot/tick/min-notional validation or observed fee tier. A no-stop mean-reversion long can hold through prolonged declines. A moving residual-extreme envelope can generate entries due to zone movement. Idealized historical next-completed-close execution is not live executable at the same close. A future strategy-specific controller is necessary before Qlib/Hummingbot research execution; this record does not create one.

## Implementation status

`not-implemented`. No deployed controller, Qlib executable recipe, testnet/live system or new admission layer is created.

## Adoption boundary

`research-only`, `not-approved`, `approval_scope: research-only`. Only the independent Hermes Auditor GitHub Webhook Review may source-remediate, exact-head PASS merge or NOT_LOSSLESS close this PR. The existing signed GitHub webhook receiver alone reconciles README count after an accepted merge.

## Related Wiki records

None required. No new registry, folder or secondary qualification flag.

## Sources

- TradingView primary: https://www.tradingview.com/script/nTdxANi4-TASC-2025-05-Trading-The-Channel/ — PineCodersTASC, 2025-04-17, source Rule 3 and defaults; inspected 2026-10-30.
- Pinned engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — package 20260920, VERSION dev-2.17.0.
- Prior representative capability review: https://github.com/HCH725/alpha-strategy-research/pull/414 — referenced only; no new wheel validation claimed.
