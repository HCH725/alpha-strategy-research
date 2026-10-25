---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BullByte Williams R14 EMA20 CHOP12 Volume50 gated recovery - independently derived BTC-USDT spot 5m long-flat
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-28
sources:
  - https://www.tradingview.com/script/TJuVmOfk-Williams-R-Zone-Scalper-v1-0-BullByte/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Williams %R14 recovery with EMA20, CHOP12 and volume50 gates — independent BTC-USDT spot 5m derivative

## Provenance

**First-party source:** BullByte, *Williams R Zone Scalper v1.0[BullByte]*, published **2025-04-28**, TradingView public **open-source strategy**, stable script ID **TJuVmOfk**, Pine Script v6 stated by author: https://www.tradingview.com/script/TJuVmOfk-Williams-R-Zone-Scalper-v1-0-BullByte/ . First-party author description and published input/default table directly inspected **2026-10-26**. The page's complete Pine revision bytes were **not** retrievable through the readable public view. Do not claim a source-native/lossless Pine reproduction or a pinned Pine source hash.

**Author-reported facts:** Williams %R length 14; LONG trigger crosses **above -80**, SHORT trigger crosses **below -20**; optional moving-average trend, Choppiness Index, volume, Bollinger Band Width and Supertrend filters; defaults MA type EMA, length 20; CHOP enabled, length 12, threshold 38.2 (trending below threshold); volume filter enabled, volume SMA length 50; BBW and Supertrend disabled; optional ATR stop/target disabled (if enabled, ATR14, 1.5x SL, 2x TP). The author discusses BTC/USD on 5-minute candles, and reports backtest numbers and a 0.01% commission; those are **author claims only**, not independently reproduced or adopted as this derivative's economics. The prose does not prove the exact Pine boolean expressions, indicator initialization, exits, position handling or fill convention.

**Explicit independent derivative, NOT lossless:** This version independently freezes Binance **BTC-USDT spot 5m**, LONG/FLAT (original SHORT disabled), a strict EMA20 price-above filter, a strict CHOP12 <38.2 filter, volume > SMA50, the source-described W%R14 cross-up entry, and **researcher-defined** exit on W%R cross-down through -20 **or** close <= EMA20, independent of entry filters. It independently defines indicator seeds, 60-bar warmup, completed-close decision/fill convention, cash/size, failed-order state, and all disabled risks. Source-provided optional Supertrend, BBW, ATR stop/target and original short signal are **not enabled**. The source's 5m horizon is retained but symbol/venue and execution semantics are researcher choices. These material choices may change every trade; the source strategy itself is **not** asserted to have passed.

**Frozen derivative identity:** `TV:TJuVmOfk:BullByte:2025-04-28 | independent-derived-v1-WPR14-up-80-EMA20-closegt-CHOP12-lt38p2-volume-gt-SMA50 | exit-WPR-down-20-or-close-le-EMA20 | BinanceSpot:BTC-USDT:5m:LONG-FLAT:Q0p001:close-MARKET:fee0p001 | 2026-10-26`. Any change to filters, exit, timeframe, sizing, fee, timing or risk creates a new derivative identity.

## Economic mechanism

### Source-reported

The author proposes oversold Williams %R recovery with trend, choppiness and participation filters to avoid some range-bound false signals. Five optional filter families and an optional ATR bracket are described; the author's reported returns are **not** evidence of reproducibility or profitability here.

### Research interpretation

A W%R recovery above -80 occurring above a 20-close EMA, with low CHOP and volume above its 50-bar mean, may indicate a higher-participation trend resumption. The independently defined EMA/W%R exit deliberately makes the spot LONG/FLAT version different from the author's two-sided strategy. This is a falsifiable hypothesis, not a performance result.

## Signal

**Clock and input:** exactly one Binance BTC-USDT **spot 5-minute UTC OHLCV** feed. Candle t has opening timestamp `T[t]` in epoch seconds and becomes eligible for calculation/decision **only after** `T[t]+300`. Require strict 300-second consecutiveness, finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, finite `V>=0`, and actual observed `C`; no interpolation, forward fill, synthetic prices or incomplete candle use. Historical initial index is 0; all formulas use only data with index <= t.

**Researcher-pinned mathematics:**

1. `HH14[t]=max(H[t-13..t])`, `LL14[t]=min(L[t-13..t])`, `W[t]=-100*(HH14[t]-C[t])/(HH14[t]-LL14[t])`; invalid if denominator <=0. `WUp80[t]=(W[t-1]<=-80 && W[t]>-80)`. `WDown20[t]=(W[t-1]>=-20 && W[t]<-20)`. Current equality is **not** a crossing.
2. `EMA20[19]=mean(C[0..19])`; for t>=20, `EMA20[t]=(2/21)*C[t]+(19/21)*EMA20[t-1]`. Before t=19 undefined. Price filter `C[t]>EMA20[t]` is strict.
3. For t>=1, `TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1]))`. For t>=12, `S12[t]=sum(TR[t-11..t])`, `R12[t]=max(H[t-11..t])-min(L[t-11..t])`; `CHOP12[t]=100*log10(S12[t]/R12[t])/log10(12)` if S12>0 and R12>0; otherwise invalid. Filter `CHOP12[t]<38.2` is strict. This exact TR/window/initialization is **researcher-defined**, not a claim about the inaccessible Pine implementation.
4. `VSMA50[t]=sum(V[t-49..t])/50`, valid from t=49. Participation filter `V[t]>VSMA50[t]` is strict. Zero/flat volume simply fails the filter; malformed volume invalidates the run.
5. **Warmup:** no decision/order until **60 consecutive fully completed valid 5m candles** are present, and both current and previous W%R and all filters are valid. Initialize `position=FLAT`, `pending=NONE`; no assumed inherited inventory.
6. **Per-completed-bar priority, exactly once:** If `pending` exists, submit no new action until fill/failure is resolved. If confirmed LONG, exit on `WDown20[t] || C[t]<=EMA20[t]` by one SELL for **the confirmed held quantity**; ignore entry conditions on the exit bar. If confirmed FLAT, enter one BUY of exactly `0.001 BTC` only when `WUp80[t] && C[t]>EMA20[t] && CHOP12[t]<38.2 && V[t]>VSMA50[t]` and `cash>=0.001*C[t]*(1+0.001)`. No other entries or exits.
7. **Fill-confirmed state:** BUY action creation sets `pending=BUY` but does not set LONG. On full confirmed fill, debit cash and set LONG; on rejected/failed/unfilled BUY, clear pending and remain FLAT, with no automatic retry absent a **new later WUp80 cross**. SELL action sets `pending=SELL` and retains LONG until confirmed; a failed SELL retains inventory and schedules another SELL at the **next valid completed candle** (not a fabricated same-bar fill), regardless of whether exit predicate persists. No exit-and-reentry on one candle. Re-entry after a confirmed exit requires a fresh later WUp80 cross; cooldown is zero bars otherwise.
8. **Explicitly disabled:** SHORT, perpetual/futures/funding, leverage/borrowing, intrabar/next-open/limit/maker orders, stop-loss, take-profit, trailing stop, time-stop, end-of-sample forced liquidation, ATR bracket, BBW, Supertrend, partial take-profit, pyramiding, BO/SO/DCA, averaging, compounding, multiple simultaneous positions, cross-pair capital sharing, discretionary exits and hidden controller risk defaults. Lack of protective stop is an explicit research risk, not an inferred source fact.
9. **Data failure:** a missing/duplicated/malformed 5m candle or undefined required indicator after warmup aborts the **entire research run as data-incomplete**. Do not quietly bridge gaps, claim continuous returns, invent exit fills or restart from an unverified position. If the sample ends while LONG, leave the position open and mark only at a real last observed valid close; do not insert a SELL.

## Required data

One historical Binance **spot** BTC-USDT 5m OHLCV stream with actual opening timestamps. No order book, funding, mark/index price, news, fitted model, external feature, multi-symbol portfolio, secondary timeframe or future pivot. The original source's dashboard and author backtest summary are **not** inputs.

## Execution assumptions

**Pinned Hummingbot research baseline:** package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The connected GitHub app was used on **2026-10-26** to read the pinned `VERSION`, `binance_spot_candles/constants.py`, `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `strategy_v2/executors/order_executor/data_types.py` and `strategy_v2/backtesting/backtesting_data_provider.py`. Previously independently reviewed package/source correspondence is recorded in Alpha PR **#414** (902/902 Python-file comparison and wheel hash in its evidence); this Scout did **not** rehash the installed package or verify an image digest. That limitation remains explicit.

- **Real data path:** `BinanceSpotCandles` exposes `5m` in `constants.py`; REST candle parser takes exchange `row[0]` as **opening** timestamp and `row[1..5]` as OHLCV. Backtesting provider loads historical candles and the engine merges processed features into OHLCV; `prepare_market_data` calls `dropna`, so the declared **pre-engine** gap/validity check is mandatory rather than trusting dropped rows.
- **Real controller/executor path:** a strategy-specific controller, when later implemented, must evaluate the frozen formulas on completed rows, maintain its own confirmed-fill state and issue `CreateExecutorAction` → `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. The pinned `BacktestingEngineBase.simulate_execution` invokes `update_state(row)`, `controller.determine_executor_actions()`, then `simulate_executor` → `OrderExecutorSimulator.simulate`; `OrderExecutorConfig` accepts these MARKET settings. No dedicated controller exists yet, and API acceptance alone is **not** claimed as implementation.
- **Real fill path and effective time:** pinned `OrderExecutorSimulator` MARKET fills at the **first supplied row's actual close** and computes `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, returning `CloseType.POSITION_HOLD`. Raw row timestamp is candle **open**, not the moment its close became knowable. The declared modeled decision/fill effective clock is **open +300 seconds**, and any implementation that consumes `close[t]` at raw `open[t]` time fails Gate 5/6. This is an **idealized completed-close backtest convention**, not an assertion that live MARKET orders can fill at the historical close.
- **Position and accounting:** pinned `BacktestPositionHold` nets opposite-side filled base amounts, tracks weighted cost and gross realized quote PnL, and accumulates quote fees separately. `terminated_executors_window=None` (or persistent fill-event ledger with equivalent semantics) prevents losing fill confirmations outside the engine's default 3600-second terminated view. A BUY/SELL action does **not** itself change confirmed inventory. `BacktestingDataProvider.get_price_by_type` may default to `Decimal("1")` when a price is missing; that fallback is **forbidden** for this strategy, requiring a real valid close or run failure.
- **Research cash and fees:** start with **10,000 USDT unborrowed cash**, Q=0.001 BTC, at most one open spot long. Pin `run_backtesting(trade_cost=0.001)`, an **assumed 0.1% of quote notional per filled side** (not the author's reported 0.01% or a verified Binance tariff). On BUY cash decreases `Q*Pb*(1+0.001)`; on SELL it increases `Q*Ps*(1-0.001)`. Net matched roundtrip quote PnL is `Q*(Ps-Pb)-0.001*Q*(Pb+Ps)`; do **not** report the engine's gross position PnL as fee-inclusive net equity. Unrealized spot inventory is marked at actual last observed close, not a hypothetical liquidation fill.
- **Explicit model limits:** the simulator's full-size close fills imply idealized **zero modeled slippage**, not observed zero exchange slippage. Real spreads, liquidity, partial fills, fee tiers, price/quantity precision, min notional, latency and actual order execution remain unverified and are not silently represented as realistic. Spot funding is **not applicable** (not fabricated zero perpetual funding). This strategy does not claim any maker, intrabar, next-open or futures capability.

## Evidence

### Source-reported

BullByte's TradingView publication **2025-04-28** directly gives W%R14 crossing -80 for long, EMA20/CHOP12<38.2/volume-SMA50 defaults, optional filter toggles and ATR bracket, short trigger -20, Pine v6 and 5-minute BTC/USD context. No source backtest metric is independently validated or attributed to this derivative.

### Independently reproduced

**Not independently reproduced.** No Pine-vs-derived signal replay, Hummingbot/Qlib strategy run, event-level parity, trading, Paper/Testnet/Live, wheel rehash, deployment, Sharpe/ROI claim or Survivor/HB Certified evidence. This Scout independently inspected the **pinned engine source paths** above to establish a bounded spot 5m completed-close MARKET/POSITION_HOLD research model; that is not strategy performance reproduction.

### Negative evidence

Complete source Pine revision and source-specific boolean/tie/exit details were unavailable. EMA comparator, CHOP arithmetic/seed, volume strictness, exit, spot symbol, cash/fees, clock, fills and state are **researcher-defined**, not silently attributed to BullByte. At pre-write main `546733b14bd488558106a8979dafb7bbdf174241`, root Git tree contained **335** strategy Markdown files and README static count **335**. Count agreement alone is **not** proof that all 335 frontmatters were individually reverified this cycle; two relevant existing records were spot-read as PASS. GitHub code search for `TJuVmOfk`, `BullByte`, and the source title returned no main match, and all ten open `research/*` PR titles/bodies were checked for the source identity. Existing Williams %R records use level-cross, MACD-arm, EMA-reclaim or ADX gating, **not this W%R14 + EMA20 + CHOP12 + volume-SMA50 conjunction with the independently defined exit**. No source or materially identical-rule duplicate was found in that check.

**Six-gate summary (Scout proposal, not independent audit):** (1) exact W%R/EMA/CHOP/volume formulas, seeds, strict comparisons and 60-bar warmup; (2) spot LONG/FLAT, short disabled; (3) complete entry and researcher-defined W%R/EMA exit, all other risk legs explicitly disabled; (4) fixed 0.001 BTC, single confirmed position, no DCA, pending/failure/re-entry/cooldown specified; (5) pinned real Binance spot 5m feed, controller action, MARKET close simulator, POSITION_HOLD ledger, fee and effective-clock model verified by code inspection with explicit economic limitations; (6) 60 completed contiguous candles, no future data or open-time lookahead.

## Falsification plan

Only after independent admission and separate downstream selection: test strict W%R crossings/equality, CHOP zero-range invalidation, volume zero/mean equality, EMA seed, missing/duplicate 5m bars, pending fill/failure and same-bar exit priority. Reconcile representative Hummingbot controller signal/fill events with a comparable Qlib path before any large-scale screening **if this path adds a previously unverified capability**; do not demand candidate-specific parity when reusing a verified primitive. Compare the frozen conjunction against ungated W%R14 on identical IS data/costs; do not tune from OOS.

## Crypto portability

This is one explicitly specified Binance BTC-USDT **spot 5m** derivative. Single-pair scope, 5m interval, OHLCV-only inputs and completed-close convention are **not** admission disqualifiers by category; only actual pinned-engine expressibility governs. Seven-coin 1h/4h/1d, BO/SO 6/6/6, isolated 3x/5x futures are **optional downstream campaigns** and would be new, separately disclosed execution variants rather than silently equivalent source-native fills.

## Limitations

No complete Pine bytes, original revision hash, original order semantics, source parity, profit reproduction, Qlib parity, verified package digest, real precision or live fills. Derived exits and risk-disabled exposure may be hazardous. Same-close MARKET backtest fills are an idealized convention, not guaranteed tradable close prices. If the eventual controller cannot enforce close-effective causality or the stated ledger, this candidate must not be implemented or treated as proven executable without remediation; the independent auditor may reject Gate 5. PASS is only a proposal pending independent review, not a self-certified verdict.

## Implementation status

`not-implemented`: no dedicated Hummingbot controller, Qlib recipe, artifact, test or deployment was created. The record specifies a bounded expressible research strategy, **not** a currently running implementation. Downstream materialization is separate from HB_READY admission.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review alone decides exact-head six-gate PASS merge, source-verifiable remediation or NOT_LOSSLESS close. Scout never merges, approves, closes, trades or edits README.

## Related Wiki records

None asserted; no Wiki changes made.

## Sources

- Primary: BullByte, *Williams R Zone Scalper v1.0[BullByte]*, **2025-04-28**, stable TradingView ID TJuVmOfk: https://www.tradingview.com/script/TJuVmOfk-Williams-R-Zone-Scalper-v1-0-BullByte/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Earlier independent package/source and spot executor evidence: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
