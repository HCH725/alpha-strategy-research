---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView sachinlanke Adaptive Supertrend EMA-of-Supertrend/SMA crossover — independent BTCUSDT spot 4h long-flat derivative"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - https://www.tradingview.com/script/lSWZVbuz-Adaptive-Supertrend-MA-Crossover-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adaptive Supertrend line versus smoothed Supertrend MA — independent long-flat derivative

## Provenance

- **Primary source:** [Adaptive Supertrend MA Crossover Strategy](https://www.tradingview.com/script/lSWZVbuz-Adaptive-Supertrend-MA-Crossover-Strategy/), TradingView stable script ID **lSWZVbuz**, author **sachinlanke**, publication **2026-09-11** (the author's example is dated through 2026-09-11). Public open-source script listing and author description read **2026-10-25**. The readable page did **not** expose the complete Pine source, an immutable Pine revision, all defaults, or exact fill semantics; the description, **not a byte-verified Pine listing**, is the primary evidence.
- **Verified source-description concepts only:** The author trades a moving-average crossover against a Supertrend line, offers independent Supertrend/MA price-source selectors, an **“EMA of Supertrend”** MA source that first smooths the Supertrend line with an EMA and then applies a selected SMA/EMA/HMA/WMA, long when MA crosses **above** Supertrend and short on the opposite cross, optional reverse-trading mode, and optional SL/TP. The description states the conventional Supertrend basis defaults to HL2; it does **not** establish numeric ATR length/factor, MA lengths, exact recursion/seed, order processing, sizing, or source-native exit behavior.
- **Independent derivative — NOT lossless source reconstruction:** The researcher explicitly chooses the ATR/Supertrend recursion, EMA8-of-Supertrend followed by SMA5, long-only/flat state, opposite-cross **exit rather than short/reversal**, Binance BTC-USDT spot 4h, fixed 0.001 BTC, no SL/TP, a 120-bar warmup, completed-bar close research fills, and the research fee/position ledger. All are **researcher-defined** choices, not purported author defaults or author backtest trades. In particular the **close-based Supertrend flip test**, rather than the author's separately selectable flip source, is this derivative's own fixed decision rule.
- **Immutable derived identity:** `TV-lSWZVbuz | independently-derived-v1-ST14-RMA-HL2-3p0-closeflip-EMA8(ST)-SMA5(EMA8ST)-cross-long-flat | BinanceSpot-BTC-USDT-4h | 2026-10-25`. Changing any indicator formula, source, timing, side, state, market, quantity, cost or execution convention creates a different derivative.
- **Dedup as of 2026-10-25:** Main at `9fde97452b1effa1dd8f73b4359d4be6e3a395c2` contains 316 root strategy records. GitHub default-branch search for exact `lSWZVbuz` returned no matches; open `research/*` PRs were enumerated (10) and none cited this source or the **EMA-of-Supertrend followed by SMA-of-EMA-of-Supertrend versus raw Supertrend** cross. The existing Supertrend flip, Supertrend/RSI, PMax, EMA cross and Chandelier families have different order-trigger constructions. This is not a trivial parameter change to their triggers. This check is not a claim that every one of 316 records was semantically read in full.

## Economic mechanism

**Source-reported:** Compare a moving average to the adaptive Supertrend line; the author's unusual EMA-of-Supertrend input permits the MA to be built from a smoothed version of the same line. The author claims no independently verified cryptocurrency profitability here.

**Research hypothesis:** A delayed smoothing crossover against the raw, step-like Supertrend may detect changes in trend persistence without directly crossing price against an unrelated indicator. It can lag severely and may whipsaw around state flips. This is an untested hypothesis, not a reproduced TradingView result or survivor designation.

## Signal

**Fully frozen researcher-defined derivative (Gates 1–4):** One consecutive, UTC-aligned Binance BTC-USDT spot **4h** OHLCV stream. For bar index `t`, the kline's open timestamp is `T[t]`, with exact spacing **14,400 seconds**. All calculations and signals use **completed bars only** and are first available at `T[t]+14400`. `H[t],L[t],C[t]` are finite positive high, low and close; no other market/data feed is used.

1. **True range / Wilder ATR14.** `TR[0]=H[0]-L[0]`; for `t>=1`, `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`. `ATR[13]=sum(TR[0..13])/14`. For `t>=14`, `ATR[t]=(13*ATR[t-1]+TR[t])/14`. `ATR` is unavailable before index 13. No EMA/SMA substitution for the recursive ATR.
2. **Basic Supertrend bands.** For `t>=13`, `M[t]=(H[t]+L[t])/2`; `BU[t]=M[t]+3.0*ATR[t]`; `BL[t]=M[t]-3.0*ATR[t]`. At `t=13`, set `FU[13]=BU[13]`, `FL[13]=BL[13]`, state `BEAR` and `ST[13]=FU[13]`. This initial BEAR seed is an explicit researcher choice, not a source-default assertion.
3. **Trailing band recursion.** For `t>13`: `FU[t]=BU[t]` if `BU[t]<FU[t-1]` **or** `C[t-1]>FU[t-1]`, else `FU[t]=FU[t-1]`. `FL[t]=BL[t]` if `BL[t]>FL[t-1]` **or** `C[t-1]<FL[t-1]`, else `FL[t]=FL[t-1]`. All comparisons are strict.
4. **Supertrend state/line.** If previous state was `BEAR`, then `C[t]>FU[t]` changes to `BULL` with `ST[t]=FL[t]`; otherwise remain `BEAR` with `ST[t]=FU[t]`. If previous state was `BULL`, then `C[t]<FL[t]` changes to `BEAR` with `ST[t]=FU[t]`; otherwise remain `BULL` with `ST[t]=FL[t]`. Equality retains prior state. No use of future pivots, future bars, lookahead or repainting.
5. **EMA8 of Supertrend, then SMA5.** Seed `E[20]=mean(ST[13..20])` (eight values). For `t>=21`, `E[t]=(2/9)*ST[t]+(7/9)*E[t-1]`. `A[t]=mean(E[t-4..t])` for `t>=24`. Thus `A` is **SMA5 of EMA8 of ST**, not SMA5 of price or an EMA of price. No model fitting or tunable parameters.
6. **Cross signals.** `UP[t]=(A[t-1]<=ST[t-1]) AND (A[t]>ST[t])`. `DOWN[t]=(A[t-1]>=ST[t-1]) AND (A[t]<ST[t])`. These edges are defined for `t>=25` only. Equality at current bar is neither edge. Both cannot fire together.
7. **State and priority.** Initially `FLAT`; **no trade or position** until 120 consecutive fully valid completed 4h bars have been received, including the bar being evaluated. At each later completed bar: `FLAT+UP` creates one MARKET BUY of exactly **0.001 BTC** and changes state to `LONG(0.001)`; `LONG+DOWN` creates one MARKET SELL of the entire 0.001 BTC and changes to `FLAT`; all other cases HOLD. One action maximum per bar; never a same-bar round trip. A new UP edge on a later bar after an exit may re-enter immediately, with **zero cooldown**. No repeated entries while LONG, no exit while FLAT, no simultaneous positions.
8. **Explicit disabled behavior:** short sales, reverse mode, pyramiding, DCA/BO-SO overlays, safety orders, partial sizing, multi-asset concurrency, margin, leverage, stop loss, take profit, trailing stop, time limit, session filter, intrabar order, limit/maker order, compounding and automatic final-bar liquidation are all **OFF**. The sole exit is DOWN; there is no protective stop. If the dataset ends LONG, mark the remaining BTC at last valid close without inventing a SELL.

**Data validity and gap handling:** Every candle must have a 4h UTC open timestamp exactly one interval after its predecessor; finite positive O/H/L/C; `H>=max(O,C)`, `L<=min(O,C)`; finite nonnegative volume. Any missing/invalid candle resets the ATR/ST/EMA/SMA initialization and the **120-consecutive-bar** trading warmup. Suppress new entries and exits until reinitialized; an already-open LONG is carried across the gap without a fabricated fill or a forced exit. Reinitialization repeats the same BEAR seed, which is explicitly part of this derivative. No forward filling, zero-price substitution, future extrema, or use of incomplete candles.

## Required data and point-in-time causality (Gate 6)

Single **Binance spot BTC-USDT 4h** OHLCV feed, with open timestamps. Signal inputs are `H,L,C` of the current and prior **completed** candles; `O,V` are used for validity only. No cross-asset synchronization, external model, funding/mark price, order book, lower-timeframe, multi-timeframe or session/calendar feed. The 120-consecutive-bar floor exceeds the first fully defined cross at index 25, while allowing ATR and smoothing state to stabilize. A signal on bar `t` cannot be evaluated before `T[t]+14400`; any timestamp representing `T[t]` must be normalized to the **bar close effective time** before controller decision and simulator event recording. A bar-close fill is a declared **research-simulation convention**, not an executable live guarantee of obtaining that same observed close after the decision.

## Execution assumptions (Gate 5)

- **Pinned baseline and identity fence:** admission policy Hummingbot package **`20260920`**, `hummingbot/VERSION=dev-2.17.0`; inspected the immutable engine source **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`** through the connected GitHub app on 2026-10-25. These are distinct identifiers. The previously independently admitted `forven-adx-trend-di-cross-long-flat-btcusdt-1d-2026-10-25.md` documents the distribution wheel `hummingbot-20260920-cp312-cp312-macosx_11_0_arm64.whl`, its SHA-256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`, its `VERSION` and a 902/902 Python-file hash match to that engine commit. **This cycle did not independently rehash that wheel**; the binding is inherited reviewed evidence, not an invented equivalence based on the repo's unrelated `setup.py` version string.
- **Actual pinned data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` includes `4h` in `INTERVALS`; `binance_spot_candles.py` requests `/api/v3/klines` and parses row 0 as open timestamp and rows 1–5 as OHLCV. Only a completed 4h bar may feed the decision rule; a strategy-specific controller/preprocessing step must enforce the stated gap, warmup and close-time availability rules.
- **Controller/executor:** `strategy_v2/backtesting/backtesting_engine_base.py` processes feature rows, calls `controller.determine_executor_actions()`, accepts `CreateExecutorAction`, and dispatches `OrderExecutorConfig` to `order_executor_simulator.py`. A dedicated controller is **not implemented**; its entire deterministic rule is the Signal section above. It maintains its **own immediate filled-order FLAT/LONG ledger** rather than trusting the engine's one-row-lagged `positions_held` view or the terminated-executor view window. The intended market/connector/side are `binance` / `BTC-USDT` / BUY or SELL, `ExecutionStrategy.MARKET`, base quantity `0.001`, leverage 1, with `CloseType.POSITION_HOLD` netting.
- **Actual pinned fill path:** `order_executor_simulator.py` for MARKET chooses the first provided row timestamp, uses that row's `close` as full-fill price, computes `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and returns `POSITION_HOLD`. It does **not** establish next-open, real-time order latency, bid/ask spread, maker queues, partial fills or exchange-valid lot/tick precision. The required strategy-specific feed/feature normalization must map the bar-open label to effective `T+14400` and issue exactly one same-close simulated action. `prepare_market_data()` uses backward `merge_asof`, which alone does **not** prove point-in-time availability; the declared normalization/closed-bar gate is mandatory.
- **Research economics:** Fix `trade_cost=0.001` (0.1% of quote notional **per filled side**) and `Q=0.001 BTC`. At BUY price `P_b`, modeled cash outflow is `Q*P_b*(1+0.001)`; at SELL `P_s`, modeled inflow is `Q*P_s*(1-0.001)`. Matched realized net PnL = gross sell-minus-buy less both fill fees; an open BTC holding is marked at the last valid close with its paid entry fee retained. `BacktestPositionHold` separates realized gross and accumulated fee fields; `update_state.total_pnl` and executor `net_pnl_quote` must **not** be silently treated as fee-inclusive cash/equity. **Spot funding is not applicable**, not a fabricated zero funding observation. Extra modeled slippage is **0** on this simulator path, which is not a claim of zero actual spread/slippage. Precision/lot/min-notional, real commissions, partial fills and exchange latency are **unverified** and not claimed as live executable.
- **Capability reuse:** The same pinned **single-symbol Binance spot 4h completed-candle MARKET-close / POSITION_HOLD / fee-ledger** primitive is documented in previously admitted TradingView research PRs **#421, #423 and #424** and in the current main BB20 derivative. This strategy introduces a new **deterministic signal formula** but no new execution primitive, portfolio model, funding requirement, data category or market type. That reusable pinned-engine evidence is expressibility evidence, not a strategy-specific backtest or implementation. Any real next-open/intrabar/maker requirement would require a separate representative capability validation before mass screening.

## Six-gate evidence matrix

1. **Deterministic signals:** complete ATR/ST band/state recursion, EMA8 seed/recursion, SMA5, edge equality and all fixed constants in Signal; no fitting or unspecified Pine defaults.
2. **Direction:** spot LONG/FLAT only, source's SHORT and reverse mode explicitly disabled as a derived decision.
3. **Entries/exits/risk:** UP entry, DOWN exit; all other exit/risk mechanisms explicitly disabled; no hidden engine SL/TP defaults.
4. **Position state:** single 0.001 BTC, immediate controller state, no DCA/pyramiding/concurrency/cooldown, one action/bar, no forced terminal close.
5. **Pinned-engine compatibility:** explicit engine commit, reviewed package binding, Binance 4h OHLCV, MARKET OrderExecutor and POSITION_HOLD fill/fee/cost path; no futures funding, maker, intrabar or unsupported data path.
6. **Causality:** completed 4h bars only, close-time normalization, explicit 120-bar warmup, prior/current cross comparisons and no future data.

## Evidence, falsification and limitations

**Source-reported evidence:** The TradingView author's description dated 2026-09-11 describes the **EMA-of-Supertrend as an input to a further MA** and MA/Supertrend crossover, optional inverse mode and SL/TP. It does not disclose the exact parameters used here. The author example is GOLDPETAL futures on 15m, **not** this Binance spot BTC 4h derivative. No author PnL, win rate, Sharpe or backtest statistics are claimed as independently reproduced.

**Independently reproduced for this candidate:** **None.** No strategy-specific Qlib or Hummingbot backtest, event-level parity, live fills or TradingView code-equivalence test was run. Pinned-code inspection and reusable previously reviewed engine-path evidence support the **expressibility claim only**.

**Falsification plan:** Following independent admission and separate downstream authorization, freeze this exact strategy identity, then test whether EMA-of-ST smoothing changes entries versus an ordinary close-EMA/ST cross on predetermined IS/OOS splits. Validate a genuinely new engine primitive once before mass Qlib screening; event-level Qlib/Hummingbot parity is required for a new strategy/execution path. No tuning on OOS and no implied survivor/production approval.

**Limitations:** Public readable source did not expose complete Pine, so the selected numeric lengths, recursion/seed, close-based flip, spot venue, single-side conversion, opposite-cross exit, no-stop posture, 120-bar warmup, same-close fill and fee model are **all independently derived and explicitly disclosed**. A different source-native implementation or real exchange execution may yield different events. There is no protection against large adverse price moves. `hb_ready_status: PASS` is this Scout's **proposed six-gate research admission pending independent Hermes Auditor review**, not a self-approved merge. Implementation remains `not-implemented`; adoption remains `not-approved`; approval scope remains `research-only`. No Qlib/Hummingbot execution, trading, containers, deployment or schedule changes are authorized by this record.

## Sources

- https://www.tradingview.com/script/lSWZVbuz-Adaptive-Supertrend-MA-Crossover-Strategy/ — sachinlanke, 2026-09-11, author description read 2026-10-25.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source inspected through GitHub app, 2026-10-25.
- https://github.com/HCH725/alpha-strategy-research/pull/421 — previously reviewed Binance spot 4h MARKET-close primitive.
- https://github.com/HCH725/alpha-strategy-research/pull/423 — previously reviewed same pinned 4h primitive.
- https://github.com/HCH725/alpha-strategy-research/pull/424 — previously reviewed same pinned 4h primitive.
