---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: NantzOS Vortex14 crossover SMA50-confirmed BTCUSDT spot long-flat independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-20
sources:
  - https://www.tradingview.com/script/V3cRaSNH-Vortex-Cross-w-MA-Confirmation/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# NantzOS Vortex14 + SMA50 confirmed cross — BTC-USDT spot long-flat independent derivative

## Provenance

**TradingView primary source:** *Vortex Cross w/MA Confirmation*, author **NantzOS**, published **2023-08-06**, updated **2024-09-20**, open-source strategy, stable script ID **V3cRaSNH**: https://www.tradingview.com/script/V3cRaSNH-Vortex-Cross-w-MA-Confirmation/ . First-party publication and update text inspected **2026-10-26**. Full executable Pine revision bytes and strategy property defaults were **not** retrieved; no claim of source-native/lossless Pine equivalence.

**Verified source-native description only:** Vortex Positive (VIP) crossing **above** Vortex Negative (VIM) while close is **above** a smoothing moving average is a long-entry condition; VIM crossing **above** VIP while close is **below** the smoothing line is a short-entry condition. The author lists selectable smoothing types SMA, EMA, SMMA, WMA and VWMA. The 2024-09-20 note describes an updated script with more MA options. The visible text does **not** establish exact Vortex length, MA length/type/default, Pine bar-order timing, actual source exit behavior, stops, sizing, pyramiding, fees, or exact source calculation code. Those are never silently attributed to the author.

**Explicit researcher-defined executable derivative (NOT the author's full strategy):** choose standard unsmoothed Vortex(14) on high/low/true range; SMA(close,50) for the author's described trend confirmation; disable the source's short side; add a long exit on a bearish Vortex cross **without** the source's short-side MA gate; use BTC-USDT Binance **spot 1d**, fixed **0.001 BTC** unit size, close-effective MARKET simulation, no stop/target/trailing/time exit or DCA, no leverage, and the precise warmup, gap, state and research-fee conventions below. No unspecified source settings are represented as recovered Pine defaults.

**Immutable strategy identity:** `TV-V3cRaSNH-NantzOS | independent-derived-v1-VI14-raw-SMAclose50-bullcross-long-bearcross-exit | BinanceSpot-BTC-USDT-1d | 2026-10-26`. Any change to indicator formulas, direction, sizing, risk, timing, cost, or market is a different derivative.

## Economic mechanism

### Source-reported

The author's hypothesis is trend confirmation: a positive Vortex crossover indicates an emerging upward trend, and price above a moving average filters entries. The public description provides the two-sided crossover-plus-MA concept but no independently verifiable performance figures.

### Research interpretation

This derivative isolates the **raw** Vortex trend-turn entry conditioned on SMA50 and exits when the opposite Vortex crossover invalidates positive directional dominance. The exit deliberately does not require price below SMA50, so a losing/weakening position can flatten before a second filter changes. This is not the same as the source's stated short-entry rule or the repository's EMA-smoothed Vortex-spread threshold system. No positive expectancy is presumed.

## Signal

**Gate 1 — frozen deterministic arithmetic:** one consecutive Binance BTC-USDT spot daily OHLCV stream, with bar index `t` and completed bar `O[t], H[t], L[t], C[t]`. No adjusted or synthetic bars, indicator libraries with hidden smoothing, discretionary drawing, fitting, or future reads.

- `TR[t] = max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1]))`; `VMplus[t] = abs(H[t]-L[t-1])`; `VMminus[t] = abs(L[t]-H[t-1])`. The first bar has no previous bar and all three are undefined.
- For `t >= 14`, `VIplus14[t] = sum(VMplus[t-13..t]) / sum(TR[t-13..t])` and `VIminus14[t] = sum(VMminus[t-13..t]) / sum(TR[t-13..t])`. The 14-bar denominator must be finite and **strictly positive**; otherwise both VI values are undefined. This is the researcher's pinned *unsmoothed* Vortex formula, not a claim about the unseen Pine source.
- `SMA50[t] = sum(C[t-49..t])/50`, with all 50 closes finite and positive. No EMA/SMMA/WMA/VWMA is used in this derivative.
- `bullCross[t] = (VIplus14[t-1] <= VIminus14[t-1]) AND (VIplus14[t] > VIminus14[t])`. `bearCross[t] = (VIminus14[t-1] <= VIplus14[t-1]) AND (VIminus14[t] > VIplus14[t])`. Comparisons require both current and immediately preceding complete, valid values. Equality on the current bar is **not** a cross.
- **Entry** only while FLAT, after warmup, if `bullCross[t] AND C[t] > SMA50[t]`: one BUY of 0.001 BTC. No entry when already LONG or pending.
- **Exit** only while LONG if `bearCross[t]`: one SELL of exactly the filled net 0.001 BTC. The bearish cross exits even if `C[t] >= SMA50[t]`. No reverse SHORT order is ever submitted.
- Exit/close-state processing precedes entry evaluation; a bar that closes a position cannot re-enter. All SL, TP, trailing, time-stop, forced reversal, averaging, stop orders and extra source-unverified rules are explicitly **disabled**. Missing-data bars generate **no** signal, order or artificial fill.

## Required data

**Gate 6 — point-in-time data contract:** UTC Binance BTC-USDT spot **1d** open/high/low/close/volume bars, opening at `T[t]`, available for a complete-close decision no earlier than `T[t] + 86400 seconds`. Require 60 **consecutive valid completed** bars before first decision, covering the 50-close SMA, 14 Vortex movements requiring previous high/low/close, and previous-bar crossover. Validate `O,H,L,C > 0`, finite, `H >= max(O,C)`, `L <= min(O,C)`, nonnegative finite volume, and strictly consecutive UTC daily timestamps. Missing, malformed or nonconsecutive bars suspend new decisions; reset the 60-bar continuity warmup and the previous-crossover comparator. If LONG during a gap, retain confirmed inventory and resume exit evaluation only after a fresh valid warmup, without inventing an exit price or liquidation. End-of-sample LONG remains open and is marked only with an actual observed valid price; no synthetic closing fill. No repainting, forward-filled gaps, higher-timeframe incomplete candles, negative shifts, hindsight extrema, or future leakage.

## Execution assumptions

**Gate 5 — pinned and bounded Hummingbot engine model, not a live execution claim.** Canonical admission label: Hummingbot package **20260920**, VERSION **dev-2.17.0**. Source path inspected through connected GitHub: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION` = `dev-2.17.0`. The package image/build digest has **not** been independently matched byte-for-byte to that commit. Previously reviewed same-path capability evidence exists in repository PR **#417**; that evidence does not certify this strategy or supply a missing package digest. A different deployed package requires a fresh capability check.

- **Market and data:** `BinanceSpotCandles` in `hummingbot/data_feed/candles_feed/binance_spot_candles/` uses Binance `/api/v3/klines`, supports `1d`, and parses timestamp and O/H/L/C/V from actual Kline fields. Use connector `binance`, pair `BTC-USDT`, spot, one 1d feed, no futures, multi-asset joins, funding, mark prices, order-book signals or secondary timeframe. A strategy-specific controller must calculate the formulas above; a generic candle-list or executor label alone does not implement them.
- **Controller and executor route:** `BacktestingEngineBase.run_backtesting` creates the controller and calls `update_processed_data`; `simulate_execution` invokes `update_state`, then `determine_executor_actions`, then `CreateExecutorAction` → `OrderExecutorConfig` with `ExecutionStrategy.MARKET` → `OrderExecutorSimulator.simulate`. BUY `PositionAction.OPEN` and SELL `PositionAction.CLOSE`, amount `Decimal("0.001")`, leverage 1; never a PositionExecutor with hidden stops. The inspected MARKET simulator fills fully at the **first supplied row's close** and returns `CloseType.POSITION_HOLD`; this is the exact research fill convention, **not** proof that a post-close live MARKET order receives the observed close.
- **Causal clock:** Binance Kline timestamps are bar-**open** labels, and `prepare_market_data` performs backward `merge_asof` on those labels. Therefore the controller must withhold the signal until that entire daily bar is completed and interpret/normalize its close-based decision and modeled fill ledger at `T[t]+86400`. A naive feature-as-of-raw-open implementation is **invalid** and must not be used. The engine's same-row-close simulation is expressly a completed-bar research convention; no next-open or intrabar touch-path claim is made. If a controller cannot enforce this effective timestamp, the candidate's execution path is **not** HB_READY until fixed.
- **Position/fill state:** `BacktestPositionHold` nets filled BUY/SELL base quantity and records weighted cost, matched gross realized PnL and accumulated quote fees separately. The controller starts FLAT, has at most one pending action, and changes inventory only on confirmed simulator `POSITION_HOLD` fill, never at order creation. Use `terminated_executors_window=None` or persistent equivalent fill-confirmed state so a daily tick does not lose the prior fill from the default 3600-second terminated view. A rejected/failed/unfilled order leaves the state pending/flat as appropriate, not a phantom position. No pyramiding, safety orders, concurrency, re-entry cooldown or compounding; re-entry requires a **new** bullish cross after a confirmed SELL and on a later bar.
- **Cost/price model:** pin `run_backtesting(trade_cost=0.0002)` as **hypothetical 0.02% quote fee per filled BUY and SELL side** (the inspected OrderExecutorSimulator computes `cum_fees_quote = trade_cost * amount * fill_close`). This is a declared fixed research fee assumption, **not** the actual Binance account tariff; no separate slippage is simulated, **not** a claim of zero real slippage/spread. For a matched 0.001 BTC BUY at `Pb` and SELL at `Ps`, research net quote PnL is `0.001*(Ps-Pb) - 0.0002*0.001*(Pb+Ps)`. Gross position PnL and `pnl_timeseries` are not silently called fee-inclusive net equity. Spot funding is **not applicable**, never fabricated as a futures zero. Enforce valid finite positive observed close price; `BacktestingDataProvider.get_price_by_type` has a fallback `Decimal("1")`, which **must not** be used as an absent BTC price. Exchange lot/tick, min-notional, liquidity, partial fills, realized fees and deployment viability remain unverified and are not HB_READY profit/live assertions.
- **Capability boundary:** This derivative uses the already inspected single-asset spot daily Kline + MARKET same-close simulator + POSITION_HOLD path, not an unverified next-open, maker, intrabar, lower-timeframe or perpetual path. Package-to-commit provenance and physical implementation remain limitations, not concealed proofs.

## Evidence

### Source-reported

NantzOS TradingView V3cRaSNH, published 2023-08-06, updated 2024-09-20: Vortex positive/negative crossover conditioned by close above/below a selectable moving average for long/short opportunities. No source backtest metrics adopted.

### Independently reproduced

**Not independently reproduced.** No Pine-vs-derived signal replay, no Hummingbot or Qlib run, no event-level parity, no Sharpe/return claim. The six-gate *specification and pinned-engine path precheck* is evidence for **proposed** PASS pending independent Hermes Auditor verification, not an independently reproduced performance result.

### Negative evidence

Full Pine source and defaults were unavailable; source-native execution and exits cannot be claimed. The inspected backtest path does not establish live post-close fills, real fees/slippage, exchange precision, or byte-level package digest. An implementation that evaluates today's completed close at today's **open** timestamp, or substitutes the provider's fallback price 1, would violate Gate 5/6.

**Six-gate summary:** (1) explicit raw Vortex14 and SMA50 formulas/strict comparators; (2) spot LONG/FLAT, short disabled; (3) complete entry/bear-cross exit and disabled risk legs; (4) single 0.001 BTC fill-confirmed position, no DCA/concurrency/cooldown; (5) inspected pinned Binance spot 1d → controller → MARKET OrderExecutor → POSITION_HOLD/fee ledger, with timestamp/price limitations; (6) 60-bar contiguous completed warmup and effective-close causal decisions. All source-to-derivative changes are disclosed.

## Falsification plan

Without claiming any result: verify bar-for-bar indicator values on a frozen BTC-USDT daily sample; compare the proposed controller's decision timestamps against completed-bar availability; reconcile every simulated MARKET fill, side, base size, fee and net cost ledger; verify no entry during a gap or while LONG; test equal VI lines, zero true-range and incomplete warmup. After the execution path is representative-event validated, optional Qlib screening can test whether the SMA50 gate improves outcomes versus ungated raw VI14 cross, with IS/OOS frozen and fees reported separately. No Qlib/HB backtest was run in this Scout cycle.

## Crypto portability

One-pair Binance BTC-USDT spot 1d is a **derivative choice**, not an admission whitelist. Other markets/timeframes or a futures short variant require their own source-to-derivative identity and engine/cost evidence. Optional BO/SO 6/6/6 and 3×/5× downstream campaign overlays would change this strategy's fill events and are **not** part of this HB_READY record.

## Limitations

The author may implement different Vortex lengths, smoothing, MA selection, exits or Pine order timing; this record does not imply source-native equivalence. No protective stop means potentially large drawdown. Same-close MARKET fills are a bounded backtest abstraction, not executable price guarantees. Package build digest, realized fees, precision, actual fills, deployment, Qlib parity and economic performance are unverified. Independent Auditor may reject if any six-gate assumption cannot be demonstrated on the pinned model.

## Implementation status

`not-implemented`: no dedicated controller, executable Qlib recipe, backtest artifact or deployed strategy exists from this Scout. PASS is research admission only and never promises implementation.

## Adoption boundary

`research-only`, `adoption: not-approved`, `approval_scope: research-only`. No Paper, Testnet, Live, merge, auto-approval, Hummingbot deployment or Survivor/HB Certified assertion. Independent Hermes Auditor alone decides exact-head six-gate PASS merge or NOT_LOSSLESS closure.

## Related Wiki records

None identified. No Wiki or other repository modified.

## Sources

- Primary TradingView source: https://www.tradingview.com/script/V3cRaSNH-Vortex-Cross-w-MA-Confirmation/ (NantzOS, 2023-08-06; updated 2024-09-20; directly read 2026-10-26).
- Engine inspection: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting (VERSION `dev-2.17.0`, spot candle parser, BacktestingEngineBase, OrderExecutorSimulator, BacktestPositionHold).
- Existing independently reviewed engine primitive: https://github.com/HCH725/alpha-strategy-research/pull/417 (not evidence of this candidate's signal or performance).
