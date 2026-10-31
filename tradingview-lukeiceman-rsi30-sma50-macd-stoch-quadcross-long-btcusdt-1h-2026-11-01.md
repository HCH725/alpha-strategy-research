---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "lukeiceman RSI30 + SMA50 + MACD12/26/9 + Stoch14/3/3 simultaneous cross long-flat BTCUSDT spot 1h — independent derivative"
created: 2026-11-01
updated: 2026-11-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2026-11-01
sources:
  - https://www.tradingview.com/script/MZjxZ1uR-Ultimate-Trading-Bot/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Four simultaneous oscillator cross events with SMA50 regime — BTC-USDT spot 1h long-flat independent derivative

## Provenance and immutable strategy identity

- **First-party public TradingView source:** lukeiceman, *Ultimate Trading Bot*, published **2025-02-23**, stable TradingView script ID **MZjxZ1uR**: https://www.tradingview.com/script/MZjxZ1uR-Ultimate-Trading-Bot/ . The first-party public description was directly read **2026-11-01**. TradingView marks the publication open-source, but the complete Pine bytes, exact Pine revision hash, initialization, sizing, order flags and costs were **not** obtained. No source-native/lossless equivalence is claimed.
- **Source-described facts only:** a long entry requires RSI crossing up through 30, close above SMA50, MACD(12,26,9) crossing up through its signal, and stochastic %K crossing above %D **all together**. A long exit requires RSI crossing down through 70, close below SMA50, MACD crossing down through its signal, and stochastic %K crossing below %D **all together**. The source does not establish the stochastic smoothing/length, RSI smoothing seed, fill convention, risk orders, market, timeframe, or position sizing from the visible description. These omissions are **not** silently attributed to the source.
- **Explicit independent derivative (material choices):** This record fixes Binance BTC-USDT unleveraged spot UTC 1h; RSI(14) Wilder seeded from actual closes; SMA50; SMA-seeded EMA(12,26) and EMA9 signal for MACD; stochastic raw14 with SMA3 %K and SMA3 %D; all four fresh edges must coincide on one completed bar; a fixed 0.001 BTC single long; 10,000 USDT initial cash; 100-bar warmup; next-completed-candle-close historical MARKET fill; modeled quote fee 0.1% per side; no SL/TP/DCA/short; and strict state, accounting and invalid-data handling. Every choice in this sentence is researcher-defined and **not** claimed to be the author's original Pine behavior. The source's four simultaneous predicates are preserved as described; no conversion of the four cross events to persistent states.
- **Immutable identity:** TV:MZjxZ1uR|lukeiceman|2025-02-23|independent-derived-v1-20261101|BinanceSpot-BTC-USDT-UTC1h|RSI14-up30+close>SMA50+MACD12-26-9-up+Stoch14-3-3-KupD-samebar|RSI14-down70+close<SMA50+MACDdown+StochKdownD-samebar|warmup100|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|no-DCA-SL-TP.
- **Dedup checked:** the current main GitHub code search for stable ID MZjxZ1uR and author lukeiceman found no record; open research PRs and a separate open-PR ID search found no matching URL or materially identical four-edge rule. Similar individual RSI/MACD/Stoch/MA strategies are not represented as the same four-edge conjunction.

## Falsifiable research hypothesis

A simultaneous oversold RSI recovery, bullish MACD cross, bullish stochastic cross and SMA50-positive regime might identify rare, unusually synchronized upward momentum. The inverse four-part conjunction defines exit. Because all four cross **events** must occur on the same bar, signals may be extremely rare or absent; no threshold is relaxed to manufacture trades. No profitability, historical Survivor, reproduced TradingView result, Qlib parity or live suitability is claimed.

## Signal: fully pinned causal arithmetic

Use one actual, contiguous, chronological Binance spot BTC-USDT **1h** OHLCV series. Candle t opens at UTC exchange timestamp T[t] and becomes available at E[t]=T[t]+3600 seconds. All numeric calculations use float64, chronological order and actual completed bars only; no fitting or parameter search.

1. Validate each raw bar before indicator calculation: strictly hourly increasing unique T; finite positive O/H/L/C, high >= max(open,close), low <= min(open,close), finite nonnegative volume; no missing, synthetic, partial, future or forward-filled bars. Reject an invalid/gapped series, not just a problematic row. Reject unexpected drops or misalignments after the engine's backward-asof feature merge.
2. SMA50[t] is the arithmetic mean of close[t-49..t], defined for t>=49.
3. RSI14 Wilder: delta[t]=close[t]-close[t-1], gain=max(delta,0), loss=max(-delta,0). At t=14 seed avgGain and avgLoss with the arithmetic mean of the first 14 gain/loss observations t=1..14; thereafter avgX[t]=(13*avgX[t-1]+X[t])/14. RSI=100-100/(1+avgGain/avgLoss); if loss=0 and gain>0 use 100; if gain=0 and loss>0 use 0; if both are zero use 50. Undefined before t=14.
4. For EMA n=12,26 on close, seed EMA_n[n-1] with mean(close[0..n-1]); update EMA_n[t]=(2/(n+1))*close[t]+(1-2/(n+1))*EMA_n[t-1]. MACD[t]=EMA12[t]-EMA26[t], defined t>=25. Seed MACD signal EMA9 at t=33 as mean(MACD[25..33]); update recursively with alpha=2/10 for t>=34. No histogram condition.
5. Stoch raw14[t]=100*(close[t]-min(low[t-13..t]))/(max(high[t-13..t])-min(low[t-13..t])), defined t>=13. A zero/nonfinite denominator is invalid: fail closed, do not fabricate a 0/50/100 stochastic. %K[t]=SMA3(raw14)[t], defined t>=15; %D[t]=SMA3(%K)[t], defined t>=17. These are researcher-selected, not claimed Pine defaults.
6. First eligible signal decision is at t=100 after **100 completed warmup candles t=0..99**, and requires both t-1 and t indicator values finite. No trading during warmup. Signal is evaluated at E[t], never at opening timestamp T[t].
7. **BUY event on completed t:** RSI[t-1]<=30 AND RSI[t]>30; close[t]>SMA50[t]; MACD[t-1]<=Signal[t-1] AND MACD[t]>Signal[t]; K[t-1]<=D[t-1] AND K[t]>D[t]. All conjuncts refer to the **same** completed t. Only eligible while FLAT with no pending order.
8. **SELL event on completed t:** RSI[t-1]>=70 AND RSI[t]<70; close[t]<SMA50[t]; MACD[t-1]>=Signal[t-1] AND MACD[t]<Signal[t]; K[t-1]>=D[t-1] AND K[t]<D[t]. All conjuncts refer to the **same** completed t. Only eligible while LONG with no pending order.
9. Cross equality is allowed on the **previous** bar only; equality on current bar is not a cross. A persistent RSI>30, MACD>signal, or K>D is **not** a fresh cross. No substitute exit when any single bearish component fires. If no four-way exit ever occurs, the position remains open through the end of the dataset.
10. At E[s] after a valid signal, queue exactly one side-specific MARKET intent for the **next actual complete candle b=s+1**. On b, consume actual close[b] only once it becomes available at E[b]; emit the MARKET order using the engine's b-row close model. No fill is booked at E[s], no next-open/intrabar fill, no synthesized missing b. Do not evaluate any new signal on fill bar b. If no successor candle exists, pending order remains unfilled and is discarded at end-of-sample.
11. State machine: FLAT -> PENDING_BUY -> LONG only after verified full BUY fill; LONG -> PENDING_SELL -> FLAT only after verified full SELL fill. On failed/partial/duplicate/stale fill, invalid price, fee or insufficient quote balance, **invalidate the research run**, rather than pretending a trade occurred. After SELL, require a new four-way BUY event on a strictly later bar; no immediate re-entry from persistent conditions.
12. Explicitly disabled: shorts, borrow, reversals, multiple positions, pyramiding, DCA/safety orders, trailing, protective stop, take-profit, breakeven, time/session exit, partial exits, cooldown, same-bar round trip, leverage/margin/liquidation, funding, cross-market portfolio allocation, automatic end-of-data liquidation and hidden executor defaults. A missing stop is deliberate unlimited downside exposure within the fixed spot notional, not proof of risk control.

## Execution assumptions and pinned Hummingbot capability (Gate 5)

- **Exact inspected GitHub pin:** HCH725/hummingbot commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, matching policy package **20260920**, VERSION **dev-2.17.0**. Source inspected directly through the GitHub connector on 2026-11-01: hummingbot/strategy_v2/backtesting/backtesting_engine_base.py (simulate_execution, prepare_market_data, simulate_executor); hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py; hummingbot/strategy_v2/executors/order_executor/data_types.py; hummingbot/data_feed/candles_feed/binance_spot_candles/{binance_spot_candles.py,constants.py}. Reuse previously independently reviewed bounded spot MARKET/POSITION_HOLD capability described in existing PASS research records; no new executor path is assumed.
- **Market and feed:** BinanceSpotCandles REST /api/v3/klines, connector_name=binance, trading_pair=BTC-USDT, supported interval 1h, single market and one timeframe. Exchange row[0] timestamp is the **candle open**, not the moment its close is known. Require actual complete candle availability E[t], validated before feature generation; no higher-timeframe, maker, tick, book, futures, or funding path is required.
- **Controller/executor path:** a future minimal strategy-specific controller tracks FLAT/LONG/PENDING and confirmed fills, computes completed-bar features, and emits CreateExecutorAction(OrderExecutorConfig) on b=s+1 with side BUY or SELL, amount Decimal(0.001), position_action OPEN or CLOSE respectively, execution_strategy MARKET, price None and leverage 1. The pinned BacktestingEngineBase iterates row, updates state, calls determine_executor_actions, then passes processed_features.loc[i:max_ts] to simulate_executor. The pinned OrderExecutorSimulator MARKET takes the **first supplied actual row close** and row timestamp, calculates filled_amount_quote=amount*close, cum_fees_quote=trade_cost*filled_amount_quote, and returns POSITION_HOLD. Dispatching only on b therefore yields the specified idealized b-close price; its internal open timestamp must **never** be reported as an economic decision/fill time. The controller/ledger records E[b] after bar completion. This is an idealized historical model, not a live execution guarantee or source-native Pine order fill.
- **Cash/fees:** initial 10,000 USDT cash and 0 BTC; fixed Q=0.001 BTC, no compounding; modeled fee f=0.001 of quote notional **per fill side**, passed as trade_cost=0.001. BUY at actual P requires cash >= Q*P*(1+f), then cash -= Q*P*(1+f), BTC += Q. SELL at actual P requires BTC >= Q, then cash += Q*P*(1-f), BTC -= Q. Closed net PnL = Q*(sell_price-buy_price)-f*Q*(buy_price+sell_price). Mark any remaining BTC at last actual close; do not claim closed PnL for open holdings. Spot funding is inapplicable; no fabricated perpetual funding or borrowing. f=0.1% is a **hypothetical reproducible research cost**, not a verified Binance account fee. The engine's idealized close-price MARKET model does **not** model bid-ask spread, latency, queue, impact or slippage; those limitations must not be disguised as actual zero execution cost.
- **Fail-closed accounting:** native POSITION_HOLD and float-to-Decimal conversion are not independently sufficient as a net spot cash ledger. Require confirmed full-fill event and quote fee for each executor; reconcile BTC to Q within 1e-12 and quote amounts/fees within 1e-8 USDT; retain terminated executor history; reject partial/unfilled/duplicated fills, missing prices, invalid fees or cash deficit. Do not use missing-price fallback values, unverified exchange tick/lot/min-notional rules or gross-only engine PnL as proof of real fills. The research-only model is bounded; exchange acceptance, real fee tier, deployed controller and Hummingbot/Qlib event-level parity remain **unverified downstream**.
- **Point-in-time ordering (Gate 6):** no current candle close may be consumed before E[t]; queue after E[s] and fill after E[s+1]. The engine's internal T timestamp must be shifted to E for economic chronology and event reconciliation, never interpreted as a live fill at T. No future bar enters signal s, no negative shifts, repainting, future extrema, incomplete candles, fitted features, or same-bar signal/fill. A mismatched timestamp, dropped candle or unavailable next-bar price invalidates the run.

## Six-gate evidence submitted for independent Hermes Auditor

1. **Deterministic signals:** all four indicator formulas, seeds, lookbacks, comparisons, conjunction, 100-bar warmup, float64 order and invalid-data policy explicitly fixed; no ML/optimization.
2. **Direction:** only Binance spot LONG/FLAT; shorts disabled.
3. **Entries/exits/risk:** exact four-way simultaneous cross events, no stops/targets/trailing or hidden exits; rare/no-trade possibility disclosed.
4. **Position and re-entry:** Q=0.001 BTC, 10k USDT cash, one pending and one full position, confirmed-fill transitions, no DCA, new-event-only re-entry.
5. **Pinned compatibility:** exact Hummingbot commit and Binance 1h candle/OrderExecutor MARKET close-price/POSITION_HOLD paths inspected, hypothetical per-side fee and separate spot cash ledger declared; no claim of unsupported intrabar/maker/MTF/futures economics.
6. **Causality:** complete 1h bars, E[t] availability, 100-bar warmup, next-completed-close fill with explicit opening-timestamp caveat, no lookahead or fabricated prices.

**Admission scope:** proposed HB_READY PASS for this *independent derived research specification only*. The independent Hermes Auditor must verify this exact PR head and all six gates; this record is neither source-native Pine replication nor a completed executable implementation. No backtest, Qlib parity, profitability, Survivor, Hummingbot certification, Paper/Testnet/Live or adoption approval is asserted.
