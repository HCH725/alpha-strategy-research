---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Coinrule SMA9/50 RSI55 crossover long-flat on BTC-USDT spot 1h — independent execution derivative
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
source_as_of: 2020-12-29
sources:
  - https://www.tradingview.com/script/U8616A9S-Maximized-Moving-Average-Crossing-by-Coinrule/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Maximized%20Moving%20Average%20Crossing%20(by%20Coinrule).pine
  - https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coinrule SMA9/50 RSI55 crossover — independently defined BTC-USDT spot 1h execution derivative

## Provenance

- **Primary publication:** Coinrule, *Maximized Moving Average Crossing (by Coinrule)*, public OPEN-SOURCE SCRIPT, TradingView stable script ID `U8616A9S`, published **2020-12-29**: https://www.tradingview.com/script/U8616A9S-Maximized-Moving-Average-Crossing-by-Coinrule/ . The first-party page was inspected 2026-10-30. It explicitly says **BUY** when MA9 crosses above MA50 while RSI >55, **SELL** when MA9 crosses below MA50; it describes 1h as preferred, one position at a time, 30%-capital sizing and a 0.1% trading fee. The page does not itself expose the complete Pine bytes to this read.
- **Secondary source-code witness, not an independently verified byte-identical TradingView revision:** public `hasnocool/tradingview-pine-scripts` mirror, pinned commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, exact file `Maximized Moving Average Crossing (by Coinrule).pine`, Git blob `a0c8b31b1f49f99ef0dfa9e07bc141ac0b109382`. Connector read its 43-line Pine v4 excerpt. Its actual order logic matches the first-party page: `sma(close,9)` vs `sma(close,50)`, `rsi(close,14)>55`, crossover BUY, crossunder CLOSE, date-window gate, no shorts or price brackets. Its header says Author: Coinrule but a copyright comment names `relevantLeader16058`; the attribution mismatch is preserved as a provenance limitation, **not** used to claim a verified original Pine revision.
- **Distinct independently specified derivative, not source-native/lossless Pine replication.** The published SMA9/50 crossover and RSI>55 entry and reverse-cross exit are retained; researcher pins Binance BTC-USDT spot UTC 1h, Wilder RSI seed/ties, 100-bar warmup, fixed 0.001 BTC and 10,000 USDT, a complete pending-order state machine, and a historical **next completed candle CLOSE** MARKET simulation instead of the original Pine broker-emulator timing (the mirrored `strategy()` has no `process_orders_on_close`). Source's 30%-of-equity sizing is intentionally **replaced**, so economics and possible later capital-dependent events can differ. No original performance equivalence is claimed.
- **Frozen identity:** `TV:U8616A9S:Coinrule:2020-12-29 | mirror:69969ae:a0c8b31 | independent-execution-derivative-v1:2026-10-30 | binance-spot:BTC-USDT:UTC1h | SMA(close,9/50):RSI14-Wilder:entry>55 | crossup-buy:crossdown-sell | long-flat:0.001BTC:10000USDT | decision-closed-t:fill-closed-t+1:MARKET | 0.001-research-fee-per-side | warmup100 | no-DCA:no-short:no-bracket`. Any rule, timestamp, execution, sizing or fee change is a different derivative.

## Economic mechanism

An SMA9-above-SMA50 crossover is the event, but the contemporaneous RSI14>55 gate vetoes weak-momentum crosses; the reverse SMA cross closes exposure regardless of RSI. This is not the already admitted Coinrule *Maximized Scalping On Trend* (source `XAiEh7nb`), which buys a **price crossunder SMA9** inside an SMA50>SMA100 regime and exits on RSI70/30. It also differs materially from the admitted `golden-cross-sma-regime-gated-long-btcusdt-1h-2026-10-08.md`, whose 9/50 cross requires **SMA100>SMA50**, not RSI>55, and from the two-sided SMA100/150 RSI-regime record. This candidate's momentum-gated fast/medium cross changes which trades exist; it is not a mere parameter tweak.

## Signal — deterministic, closed-candle specification (Gate 1)

- Input: strictly time-ordered, contiguous, **fully closed** Binance BTC-USDT spot UTC 1h OHLCV bars; decisions use only CLOSE and UTC time. SMA9[t]=mean(C[t-8:t]), SMA50[t]=mean(C[t-49:t]), with inclusive endpoints. No EMA substitution.
- RSI14 is the standard Wilder close-delta oscillator: gain=max(C[t]-C[t-1],0), loss=max(C[t-1]-C[t],0); first average gain/loss are the arithmetic means of the first 14 completed deltas, then RMA14 recursion `avg[t]=(13*avg[t-1]+current)/14`; RSI=100-100/(1+avgGain/avgLoss). Researcher-pinned zero cases: loss=0 and gain>0 =>100; gain=loss=0 =>50; gain=0 and loss>0 =>0. These initialization/tie conventions are explicit derivative choices where exact live Pine source bytes are not proven.
- Strict crossover UP at completed bar t iff SMA9[t-1]<=SMA50[t-1] AND SMA9[t]>SMA50[t]. Strict crossover DOWN iff SMA9[t-1]>=SMA50[t-1] AND SMA9[t]<SMA50[t]. A current equality does not cross; previous equality followed by strict separation does. NaN/undefined never signals.
- BUY signal iff FLAT and UP and RSI14[t]>55 and the **bar-open UTC time** is in [2020-01-01 00:00, 2112-01-01 23:59]. SELL signal iff LONG and DOWN and the same date gate. These reproduce the page's decisive signal structure; the explicit UTC timezone, seed and evaluation state are researcher-frozen. RSI equality 55 blocks BUY. DOWN has no RSI gate.
- Warmup **100 consecutive completed 1h bars**, chosen conservatively by researcher. Before that, emit neither entry nor exit. The 50-bar SMA and prior-bar cross are fully defined by then; no incomplete, future, lookahead or full-sample inputs are permitted. No parameter optimization or training step.

## Direction, exits, risk and state (Gates 2–4)

- **LONG / FLAT only** on Binance spot. No short, reversal-to-short, borrowed inventory, leverage, futures, funding, multi-pair exposure, pyramiding, DCA, safety order, partial exit, trailing, take-profit, price stop, intrabar stop, time exit or forced end-of-sample liquidation. The only ordinary exit is the reverse SMA9/SMA50 crossover. This deliberately has unbounded adverse-price excursion before an exit event.
- Position size: exactly **0.001 BTC** per successful BUY; starting unborrowed cash **10,000 USDT**, one position maximum. No compounding, size increase or rebalancing. A SELL closes the entire held 0.001 BTC; never sell while FLAT.
- Four exclusive states: FLAT, PENDING_BUY, LONG, PENDING_SELL. At completed bar t, first execute any pending action created at completed t-1 using the **actual historical C[t]** and then evaluate t's completed-bar signal for a possible action on t+1. The same bar may complete a previous fill and create a *new pending* opposite signal, but it may never fill both. Ignore all fresh entry signals while LONG or pending; ignore exits while FLAT or pending. No cooldown; re-entry needs a new strict UP crossover after returning FLAT.
- If an eligible signal occurs on the last available complete bar, its pending order expires **unfilled** at dataset end. Missing/nonpositive/nonfinite price, missing/gapped candle, mismatched time index, invalid trading rules or unavailable fee inputs are **hard validation failures**: halt/reject that research replay; do not fabricate a price, shift the fill to an arbitrary later row or silently drop rows. Insufficient quote cash or venue size/notional failure cancels the pending BUY without retry, returning FLAT; subsequent entry requires a fresh crossover. No discretionary remediation of missed signals.
- At fill, verify `quantize_order_amount("binance","BTC-USDT",Decimal("0.001"))` equals 0.001 BTC and that applicable historical research min-size/min-notional assumptions are declared; if not, block the fill instead of silently resizing. No exchange-lot or actual Binance fee-tier compliance is claimed before verification.

## Required data and point-in-time causality (Gate 6)

- Only one 1h BTC-USDT candle feed; no cross-asset alignment, higher/lower timeframe, external data, order-book, OI, mark/index price or full-sample normalization. Binance spot REST Kline `row[0]` is the **bar OPEN timestamp**, not its completed-bar availability time. For each bar with open epoch T, CLOSE becomes available only at T+3600 seconds. Record decision availability `T+3600`; the pending action from this bar can be filled only on the following fully completed bar's CLOSE (availability `T+7200`).
- The pinned backtesting engine internally indexes rows by the source bar-open epoch. This raw index is **not** asserted to be a true fill/decision availability timestamp. A strategy-specific controller must delay signal t by one complete row before emitting the MARKET action, and exported event evidence must explicitly map raw candle-open labels to close availability times. Never report raw `timestamp_bt` as an actual fill time. The simulated next-close price is a historical model, not a guarantee of a live closing-price order.
- Validate 3600-second cadence, uniqueness, UTC alignment and complete historical bars **before** the engine's backward `merge_asof` and `dropna`; a missing row must not make the simulator accidentally fill at a later valid bar. No repainting or future bar extrema.

## Execution assumptions — inspected pinned Hummingbot path (Gate 5)

- **Pin:** HCH725/hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`; its `hummingbot/VERSION` read `dev-2.17.0`, matching the repository's mandated package label `20260920`. Prior independent Alpha PR #414 documents package/source matching; this Scout did **not** independently rehash installed wheel bytes. This is bounded source-level capability evidence, not deployment proof.
- **Data:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lists `1h`; `binance_spot_candles.py` parses Binance Kline open timestamp and OHLCV. `BacktestingDataProvider` loads historical candles and exposes trading rules, amount quantization and candle dataframe. `BacktestingEngineBase.run_backtesting(...,backtesting_resolution="1h",trade_cost=0.001)` initializes a controller, feeds bars, merges causal features, and dispatches `CreateExecutorAction` to `OrderExecutorSimulator`.
- **Actual executor semantics verified in pinned source:** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1)`; `OrderExecutorSimulator.simulate()` fills MARKET at the **first supplied row's actual `close`**, records `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, then returns `POSITION_HOLD`. `BacktestingEngineBase.update_state()` precedes `determine_executor_actions()` each row; the proposed controller therefore emits only the **previous bar's pending action** to obtain the intended next-completed-bar-close fill. The generic engine does not calculate SMA/RSI or supply this controller automatically.
- **Position/cost model:** `BacktestPositionHold` nets BUY and SELL fills, maintains average cost, gross realized/unrealized PnL and cumulative fees; it does not by itself prove a cash-constrained spot account. The research controller/replay must reconcile actual simulated BUY/SELL quantities and fill prices to a separate minimal cash ledger: BUY cash delta `-0.001*C_fill*(1+0.001)`, SELL cash delta `+0.001*C_fill*(1-0.001)`; while LONG, equity=cash+0.001*last_valid_close; while FLAT, equity=cash. Halt on disagreement or missing prices. This is an accounting specification for a future implementation, **not** an assertion that such a controller/ledger already exists.
- **Costs:** `trade_cost=0.001` is a **hypothetical 0.1% per filled side**, matching the source's stated research commission but **not** a verified live Binance fee. The MARKET simulator has no actual order-book spread, queue, partial-fill or market-impact model; historical close fills are explicitly synthetic, not real execution or a claim of zero realized slippage. Spot has no perpetual funding contract; no fictional zero perpetual-funding data are inserted. No margin, liquidation or leveraged economics are used.
- **Unsupported paths not required:** no next-open, maker queue, intrabar bracket, short borrow, funding, cross-asset capital, lower-timeframe sampling or multi-timeframe synchronization. No generic API/executor name is used as evidence for those paths. Dedicated implementation and representative event-level Qlib/Hummingbot parity remain downstream engineering work, not HB_READY profit/implementation admission gates.

## Dedup and evidence

- Pre-write main snapshot `42708a5c90d9cdfd9d20732becfc128183d0b5ee` (2026-10-30): untruncated recursive tree contains **454** root strategy Markdown files, matching README **454**. Distributed frontmatter checks were PASS; **not** an exhaustive 454-file status audit. GitHub code search for stable TV ID `U8616A9S` returned zero. All 11 then-open PRs were inspected for source/title overlap: none used Coinrule or this URL. Nearest same-author and same-MA families above differ in trade-event construction and/or exit.
- **Source-reported:** first-party page states the 9/50+RSI55 entry, reverse-cross exit, 30%-capital/one-position/0.1% fee and 1h preference. No independent return, win rate, Sharpe or Survivor result is claimed.
- **Independently reproduced:** no backtest, no fill trace, no Qlib parity, no profitability or execution deployment. Only source-code/path inspection and a deterministic derivative specification.
- **Negative evidence:** mirrored Pine declaration has no `process_orders_on_close`; thus this derivative's next-completed-close model is **not** Pine default next-open equivalence. The mirror copyright name differs from the first-party page's publisher; exact source-code provenance is not overstated. A crossover alone without RSI>55 is not the same mechanism. A fee input is not proof of actual paid fees.

## Falsification plan

Keep the frozen derivative unchanged in baseline research. Compare, in later independently authorized screening, (F1) entry with RSI gate removed versus the frozen RSI>55 gate, (F2) SMA9/50 cross alone versus cross with RSI gate, and (F3) reverse-cross exits versus a separately declared fixed-horizon exit. These are **separate experimental derivatives**, not silent changes to this PASS record. Require one representative event-level Qlib/Hummingbot parity check before mass screening any new execution path.

## Limitations

No protective stop means severe adverse excursions can persist until a reverse cross. SMA crossover signals can whipsaw in sideways markets. Synthetic next-completed-close MARKET fills can differ materially from source Pine next-open orders and actual exchange fills; time-index normalization, min-notional, cash/fee reconciliation and a controller remain unimplemented. No performance, profitability, Qlib parity, Survivor, Paper/Testnet/Live or production readiness is asserted.

## Implementation status and adoption boundary

`implementation_status: not-implemented`; `status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. This is a six-gate **Scout PASS claim for independent Hermes Auditor review**, not an auditor verdict. No Qlib/Hummingbot run, trading, deployment, status migration or README edit occurred.

## Related Wiki records

None.

## Sources

- TradingView first-party publication: https://www.tradingview.com/script/U8616A9S-Maximized-Moving-Average-Crossing-by-Coinrule/ (Coinrule, 2020-12-29; read 2026-10-30).
- Public Pine mirror: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Maximized%20Moving%20Average%20Crossing%20(by%20Coinrule).pine (secondary code witness, blob a0c8b31b1f49f99ef0dfa9e07bc141ac0b109382).
- Pinned engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting (BacktestingEngineBase, BacktestingDataProvider, OrderExecutorSimulator, BacktestPositionHold); Binance Spot candle feed and OrderExecutorConfig at same commit.
- Prior independent package/path review: https://github.com/HCH725/alpha-strategy-research/pull/414 (not re-executed in this cycle).
