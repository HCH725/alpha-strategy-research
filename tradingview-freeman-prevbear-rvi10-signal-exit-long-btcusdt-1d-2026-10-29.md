---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "03.freeman previous-bear candle entry with RVI10 signal-level exit — independent BTC-USDT spot long-flat derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2019-12-05
sources:
  - https://www.tradingview.com/script/5t8W2H4T-Expert-studio-strategy-1-GBPUSD/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Previous bearish candle / RVI signal-level exit — independent long-flat derivative

## Provenance

**Primary source (directly read 2026-10-29):** TradingView public open-source *Expert studio strategy 1 - GBPUSD*, **03.freeman**, **2019-12-05**, immutable public script identifier **5t8W2H4T**, https://www.tradingview.com/script/5t8W2H4T-Expert-studio-strategy-1-GBPUSD/ . Public page states: long entry when the **previous candle is bearish**; long exit when **RVI > its signal line**; short entry when previous candle is bullish; short exit when RVI < its signal; no take-profit or stop-loss. Author describes GBPUSD 1d, 0.1 fixed lots, €1,000 starting balance, and using the current candle **open** instead of close. These are the only claimed source-native decision facts.

**Source revision limitation:** the public page labels the script open-source but the full executable Pine bytes, Pine language version, RVI implementation, signal smoothing length, precedence, sizing defaults and revision hash were **not retrieved**. The visible prose is a dated first-party description, not proof of exact source-native Pine equivalence. No claimed Pine default is inferred from common indicator settings.

**Independent derived strategy, NOT source-native reconstruction:** preserve the source-described previous-bear-candle long-entry concept, RVI-greater-than-signal long-exit predicate and no-stop/no-target posture. Researcher-defined alterations: (a) define a particular **Relative Vigor Index** formula and 10-period smoothing plus a 4-point weighted signal; (b) disable shorts; (c) port GBPUSD 1d to Binance BTC-USDT spot 1d; (d) delay signal evaluation to a fully completed prior bar and simulate a MARKET fill at the current completed bar's close, rather than source's stated current open; (e) choose 0.001 BTC, 10,000 USDT cash, 0.1% per-side hypothetical fees, 60-bar warmup and explicit state/priority/gap conventions. The RVI here is **Relative Vigor**, not the similarly abbreviated Relative Volatility Index. These choices are the researcher's design, not recovered source facts.

**Immutable derivative identity:** `TV:5t8W2H4T|03.freeman:2019-12-05|independent-derived-v1-previous-bear-long-RVI10-4bar-signal-gt-exit|BinanceSpot:BTC-USDT:1d|0.001BTC|prior-complete-signal-next-complete-close-MARKET|fee0.001|2026-10-29`. Changing any formula, timing, market, risk, cost or direction creates a different derivative.

## Economic mechanism

The research hypothesis is to buy after a bearish daily candle, then exit when the researcher's RVI momentum measure exceeds its weighted signal line. This is a contrarian entry followed by a vigor-confirmed exit, **not** a claim that the source's unknown RVI defaults were recovered. The exit is a **level/state predicate** `RVI > signal`, not an RVI crossover; while LONG it can trigger on any later eligible bar. A sequence of bearish candles while already LONG never pyramids. There is no asserted profitability.

## Signal

**Gate 1 — exact researcher-pinned arithmetic.** Index completed UTC daily bars by `t=0,1,...`. Use real, unadjusted Binance BTC-USDT spot `O[t],H[t],L[t],C[t],V[t]`. Define `D[t]=C[t]-O[t]` and `R[t]=H[t]-L[t]`. All prices must be finite, positive, `H>=max(O,C)`, `L<=min(O,C)`; `R>=0`; volume finite and nonnegative. Reject incomplete/malformed bars; never interpolate.

1. For `t>=3`, `weightedD[t]=(D[t]+2*D[t-1]+2*D[t-2]+D[t-3])/6` and `weightedR[t]=(R[t]+2*R[t-1]+2*R[t-2]+R[t-3])/6`.
2. For `t>=12`, `RVI10[t]=sum(weightedD[t-9..t])/sum(weightedR[t-9..t])`. This is exactly the ratio of the two **10-point arithmetic means**; no EMA, Wilder smoothing or relative-volatility calculation. If the denominator is zero/nonfinite, RVI is undefined and no order can be generated.
3. For `t>=15`, `RVI_signal[t]=(RVI10[t]+2*RVI10[t-1]+2*RVI10[t-2]+RVI10[t-3])/6`. All four values must be finite and available; equality does **not** meet the exit predicate.
4. On simulator bar `t` **only after its close**, use the already-completed **previous** bar `t-1` for signal predicates. `bearPrev = C[t-1] < O[t-1]`. `exitPrev = RVI10[t-1] > RVI_signal[t-1]`. A doji is not bearish. No current-bar `t` signal indicator may influence the action; `C[t]` is solely the modeled fill price and cash check.
5. If confirmed FLAT and not pending, `bearPrev` creates one BUY of 0.001 BTC at the simulated `C[t]` only if the 60-bar continuity/warmup and affordability checks pass. The RVI exit predicate is **not** an entry veto: a flat state ignores it.
6. If confirmed LONG and not pending, `exitPrev` creates one SELL of the confirmed 0.001 BTC at simulated `C[t]`. The bearish-candle entry predicate is **not** consulted while LONG. An exit takes priority over any new entry; never reverse or re-enter on the same bar.
7. There is no fixed SL/TP, trailing stop, time exit, reverse short, hedge, discretionary override, safety order, averaging, scale-out or end-of-sample forced liquidation. An unclosed final position remains open and is marked at the last **observed valid** price only, without a fabricated SELL.

**Gate 2:** LONG/FLAT on Binance BTC-USDT **spot**, leverage 1, no short or futures. **Gate 3:** complete bearish-prior-candle entry, strict RVI-above-signal exit and intentionally absent protective orders as specified above.

## Position, risk and state

**Gate 4:** starting research cash `10,000 USDT`, initial inventory `0 BTC`, fixed single-unit order quantity `Decimal("0.001") BTC`, maximum one open position and one pending action. State is `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT` **only after an observed filled executor**, not on signal submission. Reject unaffordable BUY if `cash < 0.001*C[t]*(1+0.001)`; no negative spot cash, leverage, fractional extra unit, compounding or partial-position trading. If no valid positive close exists, no order. Failed/unfilled actions must not create phantom inventory; maintain pending state until a documented fill or failure is reconciled, with no automatic retry. A failed BUY returns to FLAT only after explicit failure; a failed SELL retains LONG and waits for a new exit predicate. No explicit cooldown after a confirmed exit beyond the no-same-bar-reentry rule; a later bar can enter if the **new** previous-bear condition is met. Pyramiding, DCA, simultaneous strategies and safety orders are disabled.

The fixed size is a backtest design, not an assertion of exchange lot/min-notional viability. Unprotected exposure may suffer large drawdown. The strategy does not guarantee a positive result or enforce real exchange precision.

## Required data and causality

**Gate 6:** require at least **60 consecutive fully completed** UTC 1d OHLCV bars before the first signal/fill; this exceeds the 16-bar RVI signal minimum and includes the one-bar lag. A Binance daily bar with opening timestamp `T[t]` is not complete before `T[t]+86400 seconds`. The source predicate at `t-1` is known before `t` completes; the modeled fill at `C[t]` is assigned **effective time** `T[t]+86400`, never the raw Binance Kline **opening** label `T[t]`. A completed-close MARKET simulator fill is a bounded historical modeling convention, **not** a claim that a live order can execute at a known historical close. No future prices, higher-timeframe partial bars, repainting pivots, full-sample fitted values, negative shifts, hindsight optimization or imputed candles.

Every bar must have a strictly consecutive UTC daily timestamp and valid OHLCV. On a missing/invalid/out-of-sequence bar, generate no new signal or fill, clear the prior comparator, reset the 60-bar contiguous warmup, and **retain** any confirmed existing spot position; do not synthesize an exit. After continuity is restored, resume exit decisions only after a fresh warmup. The controller must never use the current bar's still-forming close to construct a signal.

## Execution assumptions

**Gate 5 — actual inspected pinned engine path (not a generic API assertion):** admission package `20260920`, Hummingbot VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle directly read that commit's VERSION, Binance Spot candle feed/constants, `BacktestingEngineBase`, `BacktestingDataProvider`, `OrderExecutorSimulator`, `OrderExecutorConfig`, and `ControllerBase` through GitHub. Prior independently reviewed same-path build evidence is in merged Alpha PR #414; the wheel bytes were **not** independently rehashed in this cycle. No claim is made about a different engine build.

- **Market/data:** `BinanceSpotCandles` uses `/api/v3/klines` and exposes `1d`, with timestamp and O/H/L/C/V parsed from actual Binance Kline fields. Pin `connector_name="binance"`, `trading_pair="BTC-USDT"`, one 1d feed, no secondary timeframe, cross-asset join, funding, mark price or order-book requirement.
- **Controller:** a strategy-specific `ControllerBase` implementation (not yet written) computes the above exact RVI and prior-bar signal on completed candles. `BacktestingEngineBase.run_backtesting` updates processed data and `simulate_execution` iterates rows, calls `update_state` then `determine_executor_actions`, dispatching `CreateExecutorAction` with `OrderExecutorConfig(side=BUY/SELL, position_action=OPEN/CLOSE, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. The generic executor does **not** compute RVI or implement this controller automatically.
- **Fill/clock:** inspected `OrderExecutorSimulator.simulate` sets MARKET fill timestamp to the **first supplied row** and fill price to that row's **close**; `CloseType.POSITION_HOLD` is emitted on fill. Here row `t` uses only signal inputs from `t-1`, and the simulator's fill `C[t]` is effective only at `T[t]+86400`. The engine's raw `timestamp_bt` and backward `merge_asof` are bar-**open** labels; interpreting them as completed-bar decision or fill times would be future leakage. An implementation failing to normalize effective close times is **not** compliant.
- **Fill-confirmed position:** inspected `BacktestPositionHold` in `backtesting_engine_base.py` nets opposite BUY/SELL base fills, tracks weighted entry cost, gross realized PnL and `cum_fees_quote`. The default terminated-executor controller visibility is only 3600 seconds; use `BacktestingEngineBase(terminated_executors_window=None)` or a durable equivalent plus a controller-side pending/fill ledger. `positions_held` can lag an executor's fill by a controller tick; no duplicate BUY/SELL while a prior MARKET fill is pending reconciliation. Never infer a fill from action creation alone.
- **Cash/fees:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% fee on each filled side**, charged in quote currency by the inspected simulator as `trade_cost * amount * fill_close`. For buy price `Pb`, sell `Ps` and `Q=0.001`, modeled net realized quote PnL = `Q*(Ps-Pb) - 0.001*Q*(Pb+Ps)`; quote cash is decremented by buy notional plus fee and credited by sell notional minus fee. The position hold's gross PnL and fee accumulator are separate, so a gross PnL series is **not** fee-inclusive net equity. This fee is **not** the source's, user's or Binance account's realized tariff.
- **No fabricated economics:** spot has no perpetual funding payment; this is **not** a claim of zero perpetual funding. The inspected MARKET simulator does not independently reproduce order-book spread, impact, slippage, latency, partial fills or exchange minimums. Those remain unverified real costs and execution constraints, not assumed real-world zeros. `BacktestingDataProvider.get_price_by_type` falls back to `Decimal("1")` when price is missing: this fallback must be explicitly rejected for BTC price/cash/fill accounting. Use actual positive finite `C[t]` only. Maintain Decimal ledger quantities and reconcile any simulator float roundoff; no fabricated prices.

**Capability boundary:** a single spot daily candle feed and MARKET completed-close fill model with a position-hold ledger is supported by the pinned inspected path. The source's **next/current open** forex execution, exact original Pine RVI, real fills and exchange-level economic parity are **not** claimed. This derivative is not a source-native equivalence assertion.

## Evidence

### Source-reported

03.freeman, 2019-12-05, TradingView `5t8W2H4T`: previous bearish candle long entry; RVI above signal line long exit; bullish candle short entry; RVI below signal short exit; no TP or SL; original GBPUSD 1d and open-based timing. No source performance metrics adopted.

### Independently reproduced

**No independent performance or Pine parity reproduced.** This cycle read the public TradingView description and the pinned GitHub Hummingbot source, but ran no Qlib/Hummingbot backtest, no market replay, and no strategy controller. Six-gate PASS is the Scout's **proposed research admission assessment**, subject to the independent Hermes Auditor; it is not an auditor verdict, Survivor designation, economic performance claim or trading approval.

### Negative evidence

Exact source Pine revision/indicator defaults and its original open-fill equivalence are unavailable. Actual Binance fee, lot/tick constraints, real partial fills, package wheel byte identity this cycle, and future implementation correctness remain unverified. Any controller that accidentally reads bar `t` RVI while claiming to decide at `t` open, treats raw bar-open labels as close timestamps, silently uses a missing-price fallback, or double counts position holds fails the stated Gate 5/6 contract.

**Six-gate summary:** (1) pinned weighted Relative Vigor RVI10 and signal, prior-bar bearish predicate; (2) spot LONG/FLAT, shorts disabled; (3) exact entry/exit and deliberately disabled stops/targets; (4) fixed one-unit, fill-confirmed pending state, no DCA/pyramiding; (5) inspected pinned spot daily candle → custom controller → MARKET OrderExecutor → POSITION_HOLD and quote-fee ledger with price/time guards; (6) 60 contiguous completed bars, one-bar lag and no future-data use.

## Dedup and falsification plan

At pre-write `main` SHA `a28a0f59d88b2257ed7ddfc95acb52b7b2f15d5d`, 419 root-level strategy Markdown records matched README's 419. Main code search and open `research/*` PR search found no script ID `5t8W2H4T`, author 03.freeman or this prior-bear-candle + RVI-level-exit identity. Closest families are `rvi-swma-cross-ema-stack-atr-stop-target-two-sided-btcusdt-1h-2026-10-11.md` (RVI *cross* with EMA and ATR bracket), `inertia-smoothed-rvi-50-latch-two-sided-btcusdt-1h-2026-10-15.md` (Relative **Volatility** Index 50-state), and `tradingview-botnet101-bearish-wick-prior7high-exit-long-btcusdt-1d-2026-10-26.md` (wick threshold and price breakout exit). None is this prior bearish **whole-candle** entry plus strict Relative Vigor **level** exit with no MA/ATR/price-breakout filter.

Future tests (not performed): compare hand-calculated RVI and strict exit on frozen consecutive bars; test doji, equality, zero denominator, missing bar and cash guard; reconcile fill effective timestamps, BUY/SELL side, position netting and each fee against the pinned simulator. Only after representative Hummingbot/Qlib event-level execution-path parity may this strategy path enter mass Qlib screening. This is **not** a new admission gate or a requirement for each candidate to rerun generic primitive validation.

## Limitations and adoption boundary

This is an independent derived hypothesis, not a faithful reproduction of the GBPUSD Pine source. It has **no stop-loss** and may hold a large losing position until RVI exceeds its signal. A completed-close MARKET simulator is a bounded research abstraction. No positive return, real trading viability, Qlib parity, OOS result, Survivor/HB Certified status, Paper/Testnet/Live authorization or deployment is asserted. Optional campaign coins/timeframes, DCA BO/SO 6/6/6 and futures leverage are not entry requirements and are not part of this derivative.

**Implementation status:** `not-implemented`. **Adoption:** `not-approved`. **Approval scope:** `research-only`. Independent Hermes Auditor GitHub Webhook Review alone owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS closure. This Scout does not approve, merge or alter `main`.

## Sources

- TradingView primary source: https://www.tradingview.com/script/5t8W2H4T-Expert-studio-strategy-1-GBPUSD/ (03.freeman; 2019-12-05; first-party page read 2026-10-29).
- Pinned Hummingbot engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting (VERSION `dev-2.17.0`; source directly inspected this cycle).
- Prior independently merged pinned-engine capability evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 (not proof of this derivative's signals or performance).
