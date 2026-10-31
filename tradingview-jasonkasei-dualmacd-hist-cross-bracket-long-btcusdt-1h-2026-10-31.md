---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Jasonkasei Dual MACD histogram cross plus second-MACD slope, close-trigger bracket — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-31
updated: 2026-10-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-05-29
sources:
  - https://www.tradingview.com/script/fiGbHMjI/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dual-MACD histogram zero-cross with second-MACD momentum confirmation — independent close-bracket long-flat derivative

## Provenance

**TradingView primary source read 2026-10-31:** Jasonkasei, *Dual MACD Strategy [Js.k]*, published **2025-05-29**, stable script ID **fiGbHMjI**, public TradingView open-source strategy: https://www.tradingview.com/script/fiGbHMjI/ . The accessible first-party description states: LONG when MACD1 histogram crosses upward through zero while MACD2 histogram is positive and rising; SHORT when MACD1 histogram crosses downward through zero while MACD2 histogram is negative and falling. It describes a 1% stop and 1.5% target relative to entry, 10%-equity risk/sizing language, a BTCUSDT 1h example, a reported 0.04% commission and two-tick slippage. These are **author statements**, not independently reproduced backtest results, actual exchange fees or verified fill behavior. The full Pine source bytes and original two MACD parameter triples, order flags, pyramiding and execution details were **not** accessible in the fetched page; no unspecified Pine behavior is attributed to the author.

**EXPLICIT INDEPENDENT DERIVATIVE, NOT SOURCE-NATIVE PINE EQUIVALENCE.** The following are deliberate researcher definitions: MACD1=(12,26,9) and MACD2=(5,35,5), both close-based EMA; Binance BTC-USDT unleveraged spot **1h**, LONG/FLAT only (the author's short ENTRY is disabled and its mirror trigger repurposed as an additional long EXIT); fixed 0.001 BTC size replacing ambiguous 10%-equity sizing; initial 10,000 USDT cash; completed-bar-close historical MARKET fill; **close-only** 1% stop and 1.5% target thresholds replacing any unverified intrabar Pine bracket execution; 200-bar contiguous warmup; modeled fee 0.001 per filled side; and all state/priority/cost rules below. No claim is made that the author's original stop, take profit, order fills, MACD settings or reported statistics are reproduced.

**Frozen derivative identity:** `TV:fiGbHMjI:Jasonkasei:published-2025-05-29 | derived-v1:2026-10-31 | BinanceSpot:BTC-USDT:UTC1h | MACD1(12,26,9),MACD2(5,35,5):hist1-up0-cross AND hist2-positive-rising | LONG/FLAT:0.001BTC | exit close<=entry*0.99 OR close>=entry*1.015 OR mirrored-dualMACD-bear-trigger | same-completed-close-MARKET | 200-contiguous-bar-warmup | modeled-fee=0.001/side`. Any alteration is a **different** derivative, not a silent revision.

**Pre-write dedup at main SHA `66e8d28c7799fcdb4448c769a2b4d13d7077fb61`:** complete untruncated root Git tree = 477 strategy Markdown files, README static count = 477. GitHub code search for `fiGbHMjI` and `Jasonkasei` returned no root record; all 12 open PRs were inspected by head/title/body and the exact-source open PR search returned none. Nearest MACD families differ materially: `macd-signal-cross-reversal` trades **one** MACD line/signal crossover, not a first-histogram zero cross gated by a **second** histogram's polarity and slope; `elder-impulse-dual-slope` conjoins EMA13 slope with one MACD-histogram slope, without dual MACDs or zero-cross gate; `hummingbot-macdbb` uses Bollinger-band position and MACD histogram, not two independently parameterized MACDs. This is not a mere parameter retune of the same conjunction. No full 477-file PASS frontmatter re-audit is claimed from count equality.

## Economic mechanism

**Source-reported:** first MACD histogram zero-cross provides a discrete momentum transition; a second independently parameterized histogram must already agree in sign and continue moving in that direction. Source describes symmetric short logic and 1%/1.5% price risk legs.

**Research interpretation:** the independently defined long-only strategy buys only a synchronized bullish zero-cross with an already strengthening slower MACD confirmation; it exits on the first completed-close downside threshold, upside threshold or mirrored dual-MACD bearish turn. This may underperform, gap far beyond its close stop, or remain long indefinitely; no edge, Sharpe, return or trade count is asserted.

## Signal — exact deterministic rules

Use consecutive **completed** Binance BTC-USDT spot UTC **1h** candles with finite positive closes `C[t]`, exchange-open timestamp `T[t]` and strictly `T[t]-T[t-1]=3600` seconds. Only closes feed the indicators. Index t starts at zero at the first valid candle of a contiguous run.

1. For any period N, define `EMA_N(C)[0]=C[0]`; thereafter `EMA_N(C)[t]=(2/(N+1))*C[t]+(1-2/(N+1))*EMA_N(C)[t-1]`. Seed every MACD signal EMA at zero on the first observation because both price EMAs start at C[0].
2. `M1[t]=EMA12(C)[t]-EMA26(C)[t]`; `S1[t]=EMA9(M1)[t]`; `H1[t]=M1[t]-S1[t]`.
3. `M2[t]=EMA5(C)[t]-EMA35(C)[t]`; `S2[t]=EMA5(M2)[t]`; `H2[t]=M2[t]-S2[t]`. These are **researcher-selected** period triples; the source does not publish verified values in the accessible description.
4. Bullish entry predicate `B[t]=(H1[t-1]<=0 AND H1[t]>0) AND (H2[t]>0 AND H2[t]>H2[t-1])`. Both AND legs must be true on the **same completed bar**. Equality on H1[t] or H2[t] does not enter; equality on H1[t-1] allows the upward zero-cross.
5. Bearish liquidation predicate `R[t]=(H1[t-1]>=0 AND H1[t]<0) AND (H2[t]<0 AND H2[t]<H2[t-1])`. This mirrors the author's SHORT **signal** but is an explicitly researcher-designed LONG **exit**, not an author-described long exit.
6. If FLAT, not pending and eligible after warmup, submit BUY exactly when B[t] is true. If LONG at the start of the bar with confirmed entry fill price `P_entry`, submit a full SELL when **any** of the following is true: (a) `C[t]<=0.99*P_entry` (close-only loss threshold), (b) `C[t]>=1.015*P_entry` (close-only gain threshold), (c) R[t]. Diagnostic priority when more than one exit reason is true: (a) then (b) then (c); **only one SELL** is submitted. These are close-triggered market exits, **not** resting stop/limit orders, intrabar barriers, guaranteed 1% maximum loss or 1.5% execution profit.
7. EXIT is evaluated only for a position already LONG at bar start. No exit on entry bar; no entry on an exit bar; no same-bar reversal or re-entry. If no trigger, HOLD. No other exit, trailing, time expiry, margin liquidation, forced end-of-sample SELL or discretionary action. Shorts, leverage, pyramiding, partial exits, DCA, safety orders and simultaneous strategies are disabled.
8. **Warmup:** first **200 consecutive fully closed** bars always FLAT with no orders. Earliest decision at t=200 using H1[t-1], H2[t-1], H1[t], H2[t] after all seeded EMAs are finite. If timestamp order/continuity, data completeness, price positivity or finiteness fails, **never fabricate a bar or price**. Suspend decisions until a fresh 200-bar contiguous run is obtained; if a long already exists, preserve it and do not pretend a synthetic exit or zero-risk flat state. Report such exposure as unresolved data-risk. No lookahead, repaint, negative shift, unfinished candle or fitted model is used.

## Position, orders and capital state

- One unborrowed Binance `BTC-USDT` spot position: `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT`, transitions only after **confirmed filled** MARKET order. Max position = 0.001 BTC, no short borrowing, max one pending order, no stacking, no DCA, no other pair, no shared-capital concurrency. Store `P_entry` from the **actual modeled BUY fill** (never the signal threshold or next candle's assumed price).
- Starting modeled cash = 10,000 USDT; require `cash >= 0.001*observed_fill_close*(1+0.001)` before BUY. Reject an order that cannot be afforded, without inventing credit or a price. Do not submit another order while pending. If a BUY fails, remain FLAT and require a later fresh B[t] cross; if SELL fails, remain LONG with liquidation intent latched and retry at a later valid completed close until confirmed filled. No same-bar retry. Once a SELL fills, allow only a **subsequent** bar's fresh B[t] cross; no fixed cooldown.
- End-of-sample open BTC is marked using the last real observed close; no fictitious terminal exit fill. All missing-price, connector-rule and insufficient-balance cases fail closed rather than using provider fallback values.

## Required data, causality and clock

- Pinned Binance spot candle feed accepts `1h`; `binance_spot_candles.py::_parse_rest_candles` maps Binance kline row[0] to the **open** timestamp, row[1..5] to OHLCV. A 1h close C[t] becomes known only at **effective economic time `D[t]=T[t]+3600` seconds**, not at raw T[t]. Decisions and historical idealized fills in this derivative occur at D[t]. When reporting results from the pinned backtester, **relabel effective decision/fill times to T+3600** and never present the raw opening timestamp as a real close-available time. Enforce continuity and validity **before** the engine's `dropna` and `merge_asof`; otherwise missing bars could silently compress history.
- Pinned engine's same-row-close MARKET convention is an **idealized historical price fill**: an order sent after close is **not** guaranteed to obtain that closing price on a live venue. This is a bounded research model, not proof of executable exchange close-price fills. No future bar is used in signal selection; the close fill is a declared backtest convention and the clock correction is mandatory.
- No high/low intrabar barrier, L2 book, tick-level maker/limit, external feed, multi-timeframe synchronization, funding-rate series, mark price, open interest, leverage or cross-pair exposure is required by this derivative.

## Execution assumptions — pinned Hummingbot Gate 5

**GitHub connector code inspected on 2026-10-31:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; `hummingbot/VERSION=dev-2.17.0`, admission package `20260920`. Exact pinned paths:
- `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` supports `1h`; `binance_spot_candles.py` provides the open-time OHLCV mapping.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `BacktestingEngineBase` obtains candle frames, merges features, iterates `update_state` then `determine_executor_actions`, dispatches `OrderExecutorConfig` to `OrderExecutorSimulator`; `BacktestPositionHold` nets BUY/SELL quantities, computes gross realized/unrealized PnL and accumulates fees separately. `prepare_market_data` sets timestamp from `timestamp_bt` (open timestamp), so the D[t] economic-clock correction above is **required**.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: `ExecutionStrategy.MARKET` fills at the first actual prepared row's `close` and timestamp, `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. Use a proposed strategy-specific ControllerV2 action path with BUY and SELL `OrderExecutorConfig` `ExecutionStrategy.MARKET`, connector `binance`, pair `BTC-USDT`, amount `Decimal("0.001")`, leverage 1. No unverified stop/limit executor or live order path is claimed. This controller is **not implemented**.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` may return `Decimal("1")` for an absent price lookup; **explicitly reject** that fallback rather than treating it as real data. Set `terminated_executors_window=None` or maintain independent confirmed-fill state so hourly order fills are not lost to the default one-hour controller view.
- Prior admitted research PRs **#414** and **#417** document this same bounded spot MARKET-close primitive and earlier package/commit binding. They are precedent/evidence, **not** a new candidate simulation or guarantee that arbitrary execution semantics work.

**Research economics (not factual venue costs):** choose `trade_cost=0.001` per filled side, **explicitly researcher-modeled 0.1% quote notional**, not the source's claimed 0.04% or a verified Binance account fee. For Q=0.001 BTC: BUY cash change `-Q*P_buy*(1+f)`; SELL cash change `+Q*P_sell*(1-f)`; gross matched PnL `Q*(P_sell-P_buy)`; net matched PnL subtract `f*Q*P_buy+f*Q*P_sell`. Report both gross and net; the engine's `total_pnl` time series does **not** by itself include all fee deductions. Model has **no additional slippage/spread/latency input**; do not describe this as measured zero slippage. Spot unleveraged means **no perpetual funding contract exists** for this derivative, not that perpetual funding is zero. Venue minimum notional, lot precision, actual taker fee, partial fills and live liquidity are unverified; a real deployment would require separate evidence and authorization.

## Six-gate Scout evidence (for independent Hermes Auditor)

1. **Determinism:** exact dual EMA-MACD formulas, first-close seed, two frozen parameter triples, strict cross and slope comparisons, 200-bar warmup, exit priority, data invalidation.
2. **Direction:** BTC-USDT Binance unleveraged spot LONG/FLAT only; author short leg expressly disabled and mirrored trigger repurposed as a disclosed long exit.
3. **Entry/exit/risk:** one dual-histogram AND entry; close-only 1% loss, 1.5% gain, or bearish mirror liquidation; no hidden stops, targets, trailing, intrabar or time orders.
4. **State:** fixed 0.001 BTC, 10,000 USDT initial cash, confirmed-fill pending transitions, no DCA, no concurrency, no same-bar re-entry, explicit failure handling and next-bar rearm.
5. **Pinned compatibility:** code-read HCH725/hummingbot `8b0e067`, Binance SpotCandles 1h, ControllerV2/OrderExecutor MARKET-close, position hold gross/fee ledger, no funding contract, mandatory close-time correction and rejection of missing-price fallback. This is model-compatibility evidence, **not** actual live fills or a strategy-specific backtest.
6. **Point-in-time:** 200 fully closed contiguous hourly bars; t and t-1 only; effective time open+3600, no forward references, no intrabar stops or incomplete bar consumption.

**PASS is a Scout admission proposal only**; independent exact-head Hermes Auditor decides PASS, source-verifiable remediation or NOT_LOSSLESS closure. It is not an implementation, profitability result, reproduced TradingView trade sequence, Qlib parity, Survivor/HB Certified result or Paper/Testnet/Live approval. A new execution primitive would need one representative Qlib/Hummingbot event-level validation before large-scale Qlib screening; do not add another admission flag.

## Evidence, limitations and falsification

- First-party public description directly confirms dual-histogram directional conjunction, stop/target percentages and reported source backtest setup. Full Pine code, native parameter triples, native fill flags and precise source risk-sizing behavior are **not verified**; those differences are openly researcher-designed and never silently inferred.
- Main strategy count 477 equals README 477 at captured main SHA, not a 477-file individual status audit. No identical TradingView ID in main or 12 open PRs; nearest dual-slope/MACD records use materially different signal structures.
- No actual Hummingbot/Qlib strategy backtest, economic parity, fee/slippage measurement, live price/fill, forward test or performance metric was produced. A close-only stop may incur **more than 1% loss** on a gap or long drawdown between completed bars. If data continuity fails while LONG, the exposure remains open and the research must flag it.
- A later authorized test can falsify whether adding the second MACD's slope/polarity improves the first histogram's bare zero-cross, or whether the close-only bracket dominates the mirrored-MACD exit. Any parameter or risk change must be a separately identified derivative, never an invisible revision.

## Implementation status

not-implemented. No controller, Qlib code, backtest, container, deployment, trading, cron, workflow or README modification is part of this Scout. If later admitted and selected, missing executable materialization is `IMPLEMENTATION_NEEDED` under the existing pipeline, not a second HB_READY gate.

## Adoption boundary

Research-only; adoption not approved; approval scope research-only. Independent Hermes Auditor GitHub Webhook Review alone owns exact-head six-gate review, permitted source-fact remediation, PASS merge or NOT_LOSSLESS close. Scout stops after verified open PR and does not approve, merge, close or update README.

## Sources

- https://www.tradingview.com/script/fiGbHMjI/ — Jasonkasei, *Dual MACD Strategy [Js.k]*, public TradingView publication 2025-05-29; directly read 2026-10-31.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot engine.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier bounded package/primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/417 — earlier bounded TradingView close-MARKET research path.
