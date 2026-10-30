---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "ChainAssetsCapital OFTS sell-delta absorption and price-stall long-flat — independently defined BTC-USDT spot 1h research derivative"
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
  - https://www.tradingview.com/script/XG9gPHAe-Order-Flow-Trading-System-v6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# OFTS negative-delta absorption at stalled price — independent research derivative

## Provenance and immutable identity

**Primary source:** ChainAssetsCapital, *Order Flow Trading System v6* (TradingView public open-source Pine v6 **indicator**, stable script ID `XG9gPHAe`), https://www.tradingview.com/script/XG9gPHAe-Order-Flow-Trading-System-v6/ ; directly inspected **2026-10-30**. The displayed listing date is **Feb 27** without an unambiguous year in the retrieved page; the author's embedded documentation labels itself **Version 1.0 | 2025**. These are separate date/version facts, not a claim of a verified immutable Pine revision. The full original Pine bytes and its exact execution semantics were not retrieved.

**Source-reported facts only:** the author explicitly uses candle close-location as an OHLCV **proxy** for directional delta (not real aggressor volume), defines buy absorption as unusually **negative** delta accompanied by a small price change, publishes a default **1.5** absorption delta multiplier and **0.1%** price epsilon, and describes score-reversal, volatile-divergence and illiquid-regime exits for the much broader original indicator. It also contains OBI, CVD, microprice, Kelly sizing, adaptive weights and theoretical market-making quotes. **None** of the source's complete composite-score, learning, quoting, or automated-trading semantics is claimed to be reproduced here.

**Independent derivative only, NOT source-native/lossless:** the researcher takes the first-party close-location delta and negative-delta price-stall absorption concept, retains the source-reported 1.5 and 0.1% values, and independently fixes the **previous-20 absolute-delta baseline**, strict event edges, LONG/FLAT order mapping, BTC-USDT spot 1h, 100-bar warmup, 24-bar time exit, 3% completed-close reference stop, positive-delta absorption exit, fixed 0.001 BTC / 10,000 USDT, next-completed-close idealized historical MARKET fills and hypothetical 0.1% fee. These are researcher decisions that can materially alter every trade event. No original-source strategy return, source-event equivalence, Qlib parity or Survivor claim is made.

**Frozen derivative identity:** `TV:XG9gPHAe:ChainAssetsCapital:OFTS-doc-v1.0-2025:asof20261030 | independent-sell-delta-stall-v1:20261030 | BinanceSpot:BTC-USDT:UTC1h | delta-close-location:prior20-mean-absolute:1.5-strict | abs-close-change<=0.1pct | fresh-buy-absorption LONG | opposite-sell-absorption/close-3pct/age24 exit | 100bar-warmup | Q0.001BTC:cash10000USDT | completed-t-decision:next-completed-t+1-MARKET-close | fee0.001-per-side`. Any altered signal, fill, risk, fee or market is a new version.

**Dedup before write:** Connected GitHub `main@e352ea3d3e6070d19fcdd488b1916219b5ffa503` has a nontruncated tree of **462** root-level strategy Markdown records and README static count **462**. Nine distributed frontmatters independently read are PASS; this is **not** all-462 verification. GitHub main searches for `XG9gPHAe`, `ChainAssetsCapital` found none, and same-source/open `research/*` PR searches found none. Nearest admitted mechanisms differ materially: `tradingview-phenlabs-close-location-delta-z9-ema50-200-long-btcusdt-1h-2026-10-30.md` buys **positive delta Z-anomalies** with EMA and high-volume gates; `tradingview-ennoid-volume-block-impact-decay95-crosszero-long-flat-btcusdt-1h-2026-10-30.md` trades a **decayed signed volume-block score**; `fmz-446538-vector-candle-choch-count-long-flat-btcusdt-1h-2026-10-27.md` counts **high-volume colored candle events**. This candidate instead buys **negative estimated delta despite near-flat price** and exits on opposing absorption / time / adverse close. The absorption-vs-momentum mechanism is not a trivial parameter variant.

## Economic mechanism

**Research hypothesis only:** unusually negative *estimated* bar delta without meaningful price displacement may indicate sell pressure being absorbed; a long position is opened only on the first new qualifying event. The opposite imbalance, adverse close or a finite holding horizon closes it. This is a falsifiable hypothesis, not observed institutional order flow or independently reproduced performance.

## Signal, execution and state machine — Gates 1/2/3/4/6

1. **Data/market:** Real Binance `BTC-USDT` spot UTC `1h` OHLCV; LONG/FLAT only, no short or futures. For candle index `t`, exchange `T[t]` is **open** epoch seconds, and the bar is complete/available at `E[t]=T[t]+3600`. Require strictly consecutive UTC-aligned 3600-second opens, finite positive O/H/L/C, `L<=min(O,C)<=max(O,C)<=H`, finite base volume `V>=0`. Missing/gapped/invalid or incomplete bars abort; no forward fill, fabricated prices or partial candles.
2. **Researcher-pinned delta proxy:** If `H[t]>L[t]`, `q[t]=(C[t]-L[t])/(H[t]-L[t])` and `D[t]=V[t]*(2*q[t]-1)`. For `H[t]==L[t]`, define `D[t]=0`. This is a close-location **OHLCV proxy** and must not be mislabeled real Binance taker-flow, Level 2 imbalance or a trade footprint.
3. **Prior-only baseline:** For `t>=20`, `A[t]=sum(abs(D[t-i]),i=1..20)/20` using **20 previous completed bars only**. If `A[t]<=0`, both absorption events are false. This window, absolute-value choice and zero handling are researcher-defined; the source does not fix them.
4. **Stall gate and exact inequalities:** `Stall[t]=(abs(C[t]/C[t-1]-1)<=0.001)` (inclusive **0.1%** absolute close-to-previous-close movement). `BuyAbs[t]=(A[t]>0 AND D[t]<-1.5*A[t] AND Stall[t])`. `SellAbs[t]=(A[t]>0 AND D[t]>1.5*A[t] AND Stall[t])`. Delta comparisons are **strict**; equality at the delta threshold fails. `BuyAbs` means source-style **buyers absorbing negative/sell pressure**, not a positive-delta buy spike. The opposite `SellAbs` is the source-style positive-delta absorption counterpart. No EMA/OBI/CVD/volume-profile/ML input.
5. **Warmup:** Compute all D and A from index 0. Require at least **100 consecutive fully completed valid hourly bars** (indices 0..99) before decisions. First eligible decision index `t=100`; `BuyAbs[t-1]` must be available. Start FLAT, BTC 0, cash `Decimal("10000")` USDT, no inherited/pending orders.
6. **Entry:** At completed `E[t]`, if `FLAT` and no pending order, queue BUY iff `BuyAbs[t]` is true and `BuyAbs[t-1]` is false. A persistent event is not a repeated entry. Evaluate only the current completed candle and its past; no future, repaint, intrabar or score-learning signal.
7. **BUY fill:** At the **following completed bar** `E[t+1]`, dispatch one historical MARKET BUY for `Q=Decimal("0.001")` BTC, `f=Decimal("0.001")` fee per side, using that row's **actual valid close `C[t+1]`** as the pinned idealized simulator fill. Cash must cover `Q*C[t+1]*(1+f)`; otherwise consume signal and remain FLAT. Only a confirmed full fill sets LONG, entry index `e=t+1`, entry price `P=C[e]`, and frozen completed-close stop reference `Stop=0.97*P`. Missing price, partial/rejected fill, or inconsistent accounting **aborts** rather than fabricates a trade.
8. **Exit priority:** Starting only at the **next** completed bar `u>e`, while LONG and no pending exit, evaluate in order: (a) `C[u]<=Stop` (3% **completed-close reference**, not intrabar stop order); (b) `SellAbs[u]` (opposite positive-delta price-stall absorption); (c) `u-e>=24` (24 completed hourly bars after fill). First true predicate fixes one exit reason and queues one full-Q SELL at the **next completed bar** `E[u+1]` at its actual `C[u+1]`. No intrabar bracket, stop-price execution, trailing or source-native composite-score exit. Loss may exceed 3% because execution is delayed.
9. **Position, pending, re-entry:** States `FLAT`, `BUY_PENDING`, `LONG(Q)`, `SELL_PENDING`. One spot position and at most one pending executor; no concurrent strategies or shared capital. On confirmed full SELL, debit Q BTC and credit `Q*C_sell*(1-f)` USDT, return FLAT. Ignore all signals while LONG/pending and on entry/exit fill bars; a new entry requires a **fresh BuyAbs false-to-true event on a later bar after SELL confirmation**. No DCA, safety orders, pyramiding, compounding, scale-outs, rebalancing, cooldown beyond fill-bar exclusion, leverage, margin, shorts, maker/limit orders, discretionary exits, or hidden executor defaults.
10. **End of history and precision:** A pending next-bar fill without an actual complete next bar stays explicitly **unfilled**; held inventory is marked to the last **actual completed close** without inventing liquidation. Use chronological float64 for D/A comparisons and Decimal 28-digit cash, Q and fee arithmetic; never round before comparisons. Fees are deducted separately on confirmed fills. No training, refitting, optimization or future data.

## Pinned Hummingbot capability and economics — Gate 5

- **Pin:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, connected-GitHub source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle directly fetched that commit's `hummingbot/VERSION` and immutable code paths below. Previously merged Alpha PR **#414** reports a **902/902 Python-file wheel/source correspondence**, but the wheel was **not rehashed this cycle**; independent Auditor must verify the package mapping. No later engine features are assumed.
- **Actual feed:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `1h`; `binance_spot_candles.py::_parse_rest_candles` maps REST row[0] to open timestamp, row[1..5] to O/H/L/C/base volume. `strategy_v2/backtesting/backtesting_data_provider.py::get_candles_feed` retrieves historical buffers and may reuse cached feeds, while `get_candles_df` trims to the run window. A future controller must preflight the **actual** 100+ contiguous completed warmup rows before trimming; configured max_records alone is not proof. `prepare_market_data` uses backward `merge_asof`, copies raw open timestamps and drops NA; validate continuity **before** this drop, join features on open-labeled `T[t]`, and treat the decision as effective only at completed `E[t]`.
- **Controller and MARKET executor:** `strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution` iterates rows, calls `update_state` then `controller.determine_executor_actions()`, and `simulate_executor` routes `OrderExecutorConfig` to `executors_simulator/order_executor_simulator.py`. A **dedicated future controller, not yet implemented**, must store the signal at t and emit its `CreateExecutorAction` only on row t+1. `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)` is the intended historical path; its validator allows MARKET with no limit price. The pinned simulator fills MARKET on the **first supplied row** at that row's **actual close**, sets filled quote and `cum_fees_quote=trade_cost*filled_quote`, and terminates `POSITION_HOLD`. This is a retrospective **full-fill close-price simulation**, NOT a live exchange execution guarantee or a same-open fill. Dispatch is delayed one row, and effective fill availability is E[t+1], despite raw timestamp T[t+1].
- **Ledger/costs:** `BacktestPositionHold::_process_order` nets matched BUY/SELL base and tracks gross realized/unrealized PnL; `cum_fees_quote` is separate. Maintain/reconcile a Decimal cash/BTC ledger against **confirmed** full executor fills. Set `trade_cost=0.001` per executed side (hypothetical research fee, not observed Binance tier). Modeled completed round-trip net = `Q*(P_sell-P_buy)-0.001*Q*(P_buy+P_sell)`; never mistake gross PnL for fee-net equity. Unlevered **spot** has no perpetual funding or futures liquidation path; do not label hypothetical zero funding as realized funding. Real exchange min-notional, tick/lot precision, partial fills, depth, slippage, latency and fee tier are **unverified**; they are not claimed by this idealized historical strategy.
- **Fail closed:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` for missing price. **Forbid that fallback** for fills/marks; require the observed close and reject incomplete data, partial fills, ledger mismatch or unverified execution paths. No MTF, non-OHLCV input, cross-market capital, maker, intrabar, next-open or real-time flow dependency is used. Revalidate any new primitive once before mass screening.

## Six-gate evidence and independent review focus

1. **G1:** exact close-location delta, zero-range rule, prior-20 absolute-delta mean, strict 1.5 comparison, inclusive 0.1% price stall, fresh event and numerical handling.
2. **G2:** Binance BTC-USDT spot LONG/FLAT; short disabled.
3. **G3:** first negative-delta stall entry; adverse close, opposite positive-delta stall and 24-bar exit in explicit priority; no hidden stops/TP.
4. **G4:** fixed 0.001 BTC, 10,000 USDT, one active/pending position, full fills, no DCA/adds and explicit re-entry.
5. **G5:** fixed package/commit, real Binance spot 1h feed, controller/executor/market-close simulator, timestamps, fees and separate cash/position accounting; no live-fidelity claim.
6. **G6:** completed-bar E[t] signal, following-completed-close E[t+1] fill, previous-only baseline and 100-bar warmup; no future leak.

**Auditor must independently confirm** first-party source/date/version facts, derivative-vs-source-native boundaries, material dedup distinction from PhenLabs/ennoiD/volume-climax families, source-package mapping, open-label/effective-close semantics, warmup availability, fill confirmation, fee ledger and all economic limitations. This is a Scout **PASS claim awaiting independent review**, NOT an independently audited PASS, profitability claim, Qlib parity, or Paper/Testnet/Live authorization. No backtest, trading, container or workflow action was performed.
