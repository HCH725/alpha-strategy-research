---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "growbharat2005 EMA9/20 bullish cross above EMA200 with price/EMA20 recross exit — BTCUSDT spot 1h independent derivative"
created: 2026-10-31
updated: 2026-10-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-31
sources:
  - https://www.tradingview.com/script/fURZdvM1-Long-Only-EMA-Strategy-9-20-with-200-EMA-Filter/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EMA9/20 bullish cross above EMA200, close/EMA20 bearish recross exit (independent derivative)

## Provenance

- **Primary source:** growbharat2005, *Long Only EMA Strategy (9/20 with 200 EMA Filter)*, public TradingView strategy, published **2025-12-03**, stable script ID **fURZdvM1**: https://www.tradingview.com/script/fURZdvM1-Long-Only-EMA-Strategy-9-20-with-200-EMA-Filter/ . First-party description inspected 2026-10-31. The publication is marked open source, but its full Pine bytes and immutable revision hash were **not** retrieved; no lossless Pine/event equivalence is claimed.
- **Source-native facts verified from first-party description:** EMA(close,9) crosses **above** EMA(close,20), while close is **above** EMA(close,200), to enter **long only**; an open long exits when **close crosses below** EMA(close,20). The author describes no short, and presents risk management extensions such as stop-loss/take-profit as future optional additions rather than current specified rules. The source suggests various chart timeframes but does not pin a particular market, Pine fill convention, EMA seeding, quantity, fee or re-entry ledger in its public prose.
- **Explicit independent derivative:** This record selects Binance BTC-USDT **spot 1h**, SMA-seeded recursive EMAs, 220-bar warmup, a fixed 0.001 BTC long, next-**completed-bar-close** MARKET simulation, a 10,000 USDT cash ledger and hypothetical 0.1% per-side quote fee. It specifies no protective stop/target, no DCA, and full-fill-only re-entry. These are **researcher-designed** timing, preprocessing, execution, position and accounting choices; they are not asserted to be native TradingView defaults.
- **Immutable research identity:** `TV:fURZdvM1|growbharat2005|2025-12-03|independent-derived-v1-20261031|BinanceSpot-BTC-USDT-UTC1h|EMA9-20-crossup+close>EMA200|close-crossunder-EMA20-exit|SMAseed|warmup220|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|no-SL-TP-DCA`. Immutable identity is the declared rule/version fixed by this record and eventual PR head, **not** an inaccessible Pine source revision hash.

## Economic mechanism

The source proposes a short/medium EMA bullish-cross onset gated by the longer EMA200 regime, then exits on price losing the EMA20. This is a falsifiable trend-continuation hypothesis, not a demonstrated profit premium. Research interpretation: EMA200 suppresses countertrend crossovers; the close/EMA20 exit can respond before a reverse EMA9/20 cross. No historical profitability, Survivor status, source-native parity or actual execution is claimed.

## Signal

Use a single chronological sequence of **actual, completed** Binance BTC-USDT spot UTC 1h candles, indexed `t=0,1,...` with opening timestamp `T[t]` and availability time `E[t]=T[t]+3600 seconds`. Only actual finite positive close prices are admitted; full OHLCV validity is checked before any feature merge or dropna.

1. Researcher-defined EMA seeding (not attributed to Pine): for `n in {9,20,200}`, `EMA_n[n-1]=mean(close[0..n-1])`; `EMA_n[t]=(2/(n+1))*close[t]+(1-2/(n+1))*EMA_n[t-1]` for `t>=n`. Undefined before `n-1`. Arithmetic: deterministic IEEE float64 with fixed chronological order, no training, optimization, dynamic lengths or missing-value imputation.
2. `BULL_CROSS[t]=(EMA9[t-1]<=EMA20[t-1]) AND (EMA9[t]>EMA20[t])`; equality on the current bar is not a cross. `REGIME[t]=(close[t]>EMA200[t])`. **BUY signal** only when `BULL_CROSS[t] AND REGIME[t]`, research state FLAT, no pending order and `t>=220`.
3. `EXIT_CROSS[t]=(close[t-1]>=EMA20[t-1]) AND (close[t]<EMA20[t])`. **SELL signal** only when LONG, no pending order, `t>=220`, and `EXIT_CROSS[t]`. A price that is merely below EMA20 without a fresh cross does **not** generate an exit; EMA9/20 bearish cross alone does **not** exit. Falling below EMA200 alone does **not** exit.
4. On completed signal bar `s`, queue one BUY or SELL. No fill is booked on `s`. At completed bar `b=s+1`, dispatch exactly one MARKET `OrderExecutorConfig` with the actual **bar `b` close**; economic fill time is `E[b]`. This is a deliberate historical next-close model, **not** TradingView next-open, source-native execution, a guaranteed live fill, or a protective intrabar order. If no real successor candle exists, the pending signal remains unfilled.
5. **State priority:** At any bar, process prior pending confirmed fill first; do not evaluate a new entry/exit on that fill bar. While LONG, only SELL is eligible; while FLAT, only BUY is eligible. The source-defined exit event is independent of the entry event; if both predicates are true, current state determines which is eligible. After a confirmed SELL fill, re-entry requires a **new** eligible bullish EMA cross on a strictly later bar; no automatic re-entry from persistent `EMA9>EMA20`.
6. **Explicitly disabled:** short/borrow, opposite-side reversal, pyramiding, scaling, DCA/safety orders, SL, TP, trailing, break-even, time/session exit, funding, margin/leverage/liquidation, cross-market allocation, cooldown, same-bar round trip, end-of-data forced liquidation, and all hidden executor defaults. The absence of SL/TP is a deliberate risk exposure, not a claim of bounded losses.

## Required data and causality

- One Binance spot BTC-USDT **1h** OHLCV series, no additional market or higher-timeframe dependency. Require strictly increasing hourly opening timestamps with no duplicates/gaps, finite positive O/H/L/C, `high>=max(open,close)`, `low<=min(open,close)`, finite nonnegative volume, and actual completed candle availability. Reject gaps, stale/unclosed bars, invalid prices or missing fill bars; do not forward-fill or synthesize candles.
- Warmup: **220 fully completed bars** `t=0..219` with no orders; first decision at `t=220`. EMA200 is seeded at `t=199`, both previous/current cross operands are defined before the first decision. All indicators and decisions use current/prior **completed** bars; no future extrema, negative shifts, repainting, full-sample fitting or lookahead.
- `prepare_market_data` in the pinned engine uses `merge_asof(direction="backward")` and `dropna`; the research path must validate raw timestamp continuity **before** this processing and reject unexpected dropped/misaligned bars. The decision series must not read bar `t` before `E[t]`. Raw Binance timestamps are **open**, not decision/fill availability times.

## Execution assumptions — pinned Hummingbot capability

- **Exact pin inspected via GitHub connector 2026-10-31:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION=dev-2.17.0`, policy package `20260920`. Source inspected: `binance_spot_candles/binance_spot_candles.py` and `constants.py`, `backtesting_engine_base.py`, `backtesting_data_provider.py`, `order_executor_simulator.py`, `order_executor/data_types.py`, `executor_simulator_base.py`. The package/wheel-to-source correspondence is **reused** from independent Alpha PR #414 evidence, not rehashed here. Independently reviewed bounded MARKET/POSITION_HOLD primitive evidence: Alpha PR #519 (`HB_READY: PASS`, exact-head review) and #532; this is not a candidate-specific executable implementation.
- **Data:** pinned `BinanceSpotCandles` uses `/api/v3/klines` with `1h` supported; REST parser maps `row[0]` to the candle **opening** timestamp. `connector_name="binance"`, `trading_pair="BTC-USDT"`; no unverified non-OHLCV/MTF path.
- **Controller/executor:** a future minimal controller must maintain this record's FLAT/LONG/PENDING and confirmed-fill cash/inventory state, and emit `CreateExecutorAction(OrderExecutorConfig)` on `s+1`, not `s`: `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. `BacktestingEngineBase.simulate_execution` calls `update_state(row)` then controller actions then `simulate_executor(config, processed_features.loc[i:max_ts], trade_cost)`; `OrderExecutorSimulator` MARKET uses **first supplied actual row close** and row timestamp, `amount_quote=float(Q)*close`, `cum_fees_quote=trade_cost*amount_quote`, `CloseType.POSITION_HOLD`. Thus next-row dispatch provides the declared **idealized next-completed-close** fill path. The engine timestamp is the opening timestamp; the controller/ledger must record economic availability/fill at `E[b]`, never `T[b]`.
- **Research cost/cash model (declared derivative):** initial `cash=Decimal("10000") USDT`, `BTC=Decimal("0")`, fixed `Q=Decimal("0.001") BTC`, `f=Decimal("0.001")` quote-notional fee **each side**, `trade_cost=0.001`. On confirmed full BUY at actual close `P_b`: require `cash>=Q*P_b*(1+f)`, then `cash-=Q*P_b*(1+f)`, `BTC+=Q`. On confirmed full SELL at actual close `P_s`: `cash+=Q*P_s*(1-f)`, `BTC-=Q`. Net closed PnL = `Q*(P_s-P_b)-f*Q*(P_s+P_b)`; open inventory marked only at the final **actual** close. No compounding or short cash. Fee 0.1% is a **hypothetical reproducible research assumption, NOT verified Binance tier**. Additional slippage is idealized as zero and explicitly **not** a real spread/liquidity or guaranteed fill claim. Spot funding is inapplicable; no perpetual funding is silently set to zero.
- **Engine limitations/fail closed:** native MARKET fill quote and `BacktestPositionHold` use float-to-Decimal conversion and may leave tiny position dust; native `positions_held` may lag and gross-only PnL is not this net cash ledger. Use independent confirmed-fill Decimal state, require `ExecutorSimulation` filled quote/fee/termination evidence, preserve full terminated history (`terminated_executors_window=None` or equivalent), and reconcile base to `Q` within `1e-12 BTC` and quote/fees within `1e-8 USDT` diagnostic tolerances. Reject partial/duplicate/failed/stale/unmatched fills, missing/invalid prices, cash deficits or precision disagreement; never fabricate a fill or rely on `BacktestingDataProvider.get_price_by_type` missing-price `Decimal("1")` fallback. Actual lot/tick/min-notional, venue fees, liquidity and live acceptance are **not** claimed.
- This is a **research-only model-consistent bounded historical capability**, not proof of a deployed controller, exchange fill, actual fee tier, profitability, Qlib parity, HB Certified or Paper/Testnet/Live authorization. New execution primitives require representative validation before mass Qlib screening.

## Evidence and independent review checklist

**Source-reported:** the author's 2025-12-03 description explicitly supplies EMA9/20 cross-up, close>EMA200 filter, close crossunder EMA20 exit and long-only side. No independently reproduced TradingView backtest numbers are included. **Independently reproduced performance:** none. **Historical survivor:** none.

**Six Gate assertions for independent Hermes Auditor (proposed PASS, not self-certification):**

1. Deterministic three EMA formulas/seed/thresholds and 220-bar warmup; no missing researcher-defined model or preprocessing.
2. Binance BTC-USDT spot LONG/FLAT, no shorts or borrow.
3. Full fresh-cross BUY and price/EMA20 crossunder SELL, no unspoken stops/targets/trailing or hidden risk exits.
4. Fixed Q/cash, one pending/position, confirmed-fill-only transition, fresh-cross re-entry, DCA/pyramiding/cooldown disabled.
5. Exact pinned spot candle/controller/MARKET/POSITION_HOLD next-completed-close path, hypothetical explicit fee and Decimal net ledger, fail-closed prices/precision; prior independently reviewed bounded primitive #519/#532 reused, not merely an API-name assertion.
6. Actual bar availability `E[t]=T[t]+3600`, next completed-close fill `E[t+1]`, raw continuity validation before merge/dropna, no future data or same-bar fill.

**Dedup 2026-10-31:** GitHub main SHA `e45fceea51174ad52ceb9ffa56fe1f2e77f3c71c`; root tree contains 480 Markdown strategy records vs README count 480. Searches for `fURZdvM1`, `growbharat2005`, and exact 9/20/200 EMA combination found no same-source record. All 13 open PRs checked, including three `research/chatgpt-tradingview-*`; none use this source or the same EMA9/20 cross-up + EMA200 regime + **price**/EMA20 crossunder exit. The admitted EMA20/50 simple cross and other EMA trend/filter families use materially different trigger and/or exit mechanics. Five dispersed existing main frontmatters were checked as PASS; this is **not** a full 480-record status census.

## Falsification and limitations

Downstream (not run here): verify indicator prefix invariance when future bars are changed; exact entry/exit event tape, warmup and pending timing; compare engine MARKET fill quotes/fees with independent ledger, then perform representative Qlib/Hummingbot event-level parity before large-scale Qlib screening. Compare EMA9/20 without EMA200 gate and price/EMA20 exit against reverse EMA9/20 exit only as **separate** hypotheses, not retroactive edits to this frozen identity. No claimed profit, source Pine equivalence, actual exchange execution, or authorization to trade.
