---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "ennoiD volume-block decayed impact zero-cross — independent BTC-USDT spot 1h long-flat derivative"
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
source_as_of: 2025-03-16
sources:
  - https://www.tradingview.com/script/NMag7dki-Volume-Block-Order-Analyzer/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Volume-block decayed-impact zero-cross — explicitly independent derivative

## Provenance, source facts, and immutable identity

**First-party TradingView source:** ennoiD, *Volume Block Order Analyzer*, public open-source **strategy**, published **2025-03-14**, release notes **2025-03-14/15/16**, stable script ID **NMag7dki**: https://www.tradingview.com/script/NMag7dki-Volume-Block-Order-Analyzer/ . The primary page was read on **2026-10-30**. The author's initial description specifies unusual volume against a recent average, default **2.0×** volume multiplier, bullish/bearish candle direction, a proportional impact score, **0.95** default decay, and cumulative-impact zero-cross entry/exit concepts. Subsequent **2025-03-14 through 2025-03-16** release notes explicitly add/change optional minimum-volume/price-size weighting, thresholds, trailing stops, negation, exhaustion validation and breakout entries. Therefore the page does **not** establish one lossless, unchanging native strategy. Its rendered mathematical Pine blocks are not retrievable as complete source bytes; no original code revision hash or trade-event equivalence is claimed.

**Researcher-designed derivative, NOT source-native:** This record takes only the dated **volume-spike + candle-direction + decayed impact** idea and source-reported **2×** and **0.95** values. It independently defines prior-20-bar mean volume, the signed and capped impulse formula, a zero-threshold two-state signal, fixed spot market/size/cash, 120-bar warmup, one-completed-bar-delayed historical MARKET-close fills, hypothetical per-side fees, full position ledger and no additional exits. The source's unknown exact impact formula, native lookback, changing thresholds, negation, exhaustion/breakout logic, RSI projection, optional trailing stop and all native order semantics are **not** reproduced or attributed to this derivative. These choices can change every trade event. No original or derived profitability, TradingView reproduction, Qlib parity, or Survivor claim.

**Frozen identity:** `TV:NMag7dki:ennoiD:2025-03-14/16 | independent-block-impact-v1:2026-10-30 | BinanceSpot:BTC-USDT:UTC1h | prior20-volume-SMA:V>2x | bullish/bearish-body-signed:min(V/avg/10,1) | impact[t]=0.95*impact[t-1]+impulse[t] | long-cross-zero:flat-at-nonpositive | Q0.001BTC:cash10000USDT | signal-close-t:historical-MARKET-next-completed-close-t+1 | fee0.001-per-side | warmup120`. Any changed parameter, rule, timing, fee, position, or market defines a new version.

**Pre-write dedup:** GitHub `main@9278fdb1ed674da94e65e1b3c5b3541d22cb41fa` nontruncated tree had **460** root-level strategy Markdown records and README count **460**. Ten spread-across-tree frontmatters were checked and were `PASS`; this is **not** an assertion of all-460 frontmatter verification. GitHub code search for `NMag7dki` and PR search (including closed PRs) found **zero** same-source matches; 11 open research PRs were inspected. The closest records, `tradingview-phenlabs-close-location-delta-z9-ema50-200-long-btcusdt-1h-2026-10-30.md` (close-location proxy delta Z anomaly with EMA gate) and `tradingview-szymonsobkowiak-volumeema20-priceema50-bullbar-time5-long-btcusdt-1h-2026-10-29.md` (single volume-EMA impulse with fixed five-bar hold), do **not** maintain a decaying, signed, multi-event block-volume accumulation state that crosses zero. The difference is in the decision-critical indicator and event timing, not merely parameter changes.

## Economic mechanism and scope

**Source-reported:** exceptionally high volume on bullish/bearish candles may indicate directional pressure; exponentially decaying accumulation may represent recent block activity more strongly than old activity. This is an OHLCV **proxy**, not observed institutional block executions, aggressor flow, or exchange order-book data.

**Research hypothesis only:** the first transition of a decayed signed block-volume score from nonpositive to positive may identify a new positive pressure regime. The next transition to nonpositive closes exposure. No verified edge is implied. Without a protective stop or maximum holding time, prolonged adverse price movement is possible.

## Signal and deterministic state machine — Gates 1, 2, 3, 4, 6

1. **Data:** Chronologically sorted, real Binance `BTC-USDT` **spot UTC 1h OHLCV**. For index `t`, `T[t]` is exchange candle **open** epoch seconds; completed bar `t` is available only at `E[t]=T[t]+3600`. Require exact consecutive UTC-aligned 3600-second timestamps, no duplicates/gaps, finite positive O/H/L/C, `L<=min(O,C)<=max(O,C)<=H`, finite base-asset volume `V>=0`. Missing, incomplete or invalid data **abort**; never interpolate, forward-fill, silently drop or synthesize a price.
2. **Prior-20 mean:** For `t>=20`, `A[t]=(V[t-1]+...+V[t-20])/20` (strictly **previous** completed bars, not current-inclusive). If `A[t]<=0`, set impulse `I[t]=0`; no division. Researcher-chosen lookback 20 and prior-only window are **not** source defaults.
3. **Block and impulse:** If `A[t]>0` and `V[t]>2*A[t]` (strict inequality), let `sgn[t]=1` if `C[t]>O[t]`, `-1` if `C[t]<O[t]`, and `0` on equality. Set `I[t]=sgn[t]*min(V[t]/(10*A[t]),1)`. Otherwise `I[t]=0`. This signed capped normalization is **researcher-defined**; the source's actual impact formula is not asserted. The cap bounds a single impulse, not the cumulative score.
4. **Decay state:** Initialize `S[19]=0`. For every `t>=20`, including warmup, compute `S[t]=0.95*S[t-1]+I[t]` in chronological IEEE float64. Never reinitialize after a trade. No rolling refit, future data, or full-sample normalization. Decay alone preserves a nonzero score's sign; a new opposite block is needed to reverse it. Exact zero is nonpositive.
5. **Warmup:** Indices `0..119` (120 consecutive **completed** 1h bars) are indicator-only; no trading, no inherited position. The first eligible signal is index `120`, with `S[t-1]` available. No ML/model fitting, higher/lower timeframe, future pivot, repaint, or intrabar signal.
6. **Entry:** While `FLAT` and no pending action, `BUY_SIGNAL[t] = (S[t-1]<=0 && S[t]>0)` on completed `E[t]`. Queue one BUY for the **next completed bar** `t+1`, not the signal bar. No extra source-native confirmation, session filter, or hidden default.
7. **BUY fill:** At `E[t+1]`, if actual valid `C[t+1]` exists and modeled cash `>=Q*C[t+1]*(1+f)`, issue one historical simulator MARKET BUY, `Q=Decimal("0.001")` BTC, `f=Decimal("0.001")`, at that **actual close**. Only a confirmed full fill debits cash and credits Q BTC and sets `LONG`. Insufficient cash consumes the signal and returns `FLAT`; missing price, unexpected partial fill, rejection or inconsistent ledger aborts instead of inventing execution. The fill bar never also produces a new decision.
8. **Exit:** On each **subsequent completed bar** `u` strictly after the BUY fill index while `LONG` and no pending exit, if `S[u]<=0`, queue one full-Q SELL for the **next completed bar** `u+1`. Exit reason is `nonpositive-decayed-impact` only; the current negative score may have crossed zero earlier during the entry's pending/fill interval, in which case the first eligible post-fill LONG decision exits. On confirmed full historical MARKET SELL at actual `C[u+1]`, debit Q BTC, credit `Q*C[u+1]*(1-f)` USDT and return `FLAT`. Do not generate a new signal on the SELL fill bar.
9. **Priority/re-entry:** States `FLAT`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Pending fill processing takes priority; at most one position and one pending executor. Ignore entry signals while LONG/pending, do not queue stale entries, and require a **fresh** later nonpositive-to-positive crossing after SELL confirmation. No cooldown beyond fill-bar exclusion; no pyramiding, DCA/safety orders, partial fills, compounding, shorts, futures, borrowing, leverage, margin, shared-capital cross-pair execution, SL/TP/trailing, discretionary exits, intrabar/maker/limit orders, or forced liquidation.
10. **End-of-data and arithmetic:** If a next completed fill bar is absent, report pending unfilled action; if LONG at end, mark inventory at the last **real valid completed close** separately from realized PnL, never synthesize liquidation. Use chronological float64 for indicator values and 28-digit Decimal cash/fees/Q. Exact comparisons use unrounded values. No model or parameter optimization.

## Required data and pinned-engine expressibility — Gate 5

**Source pin verified through connected GitHub:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION=dev-2.17.0`; target package **20260920**. This run directly read immutable code paths below. Prior merged Alpha PR **#414** reports package/source 902/902 Python-file correspondence; the wheel itself was **not re-downloaded or rehashed** this run, and package mapping must be confirmed by independent Auditor.

- **Actual feed:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` supports `1h`. `binance_spot_candles.py::_parse_rest_candles` reads REST `row[0]` as **open timestamp** and `row[1..5]` as OHLC/base volume. `strategy_v2/backtesting/backtesting_data_provider.py::get_candles_feed` fetches a historical buffer and may reuse cached feed; `get_candles_df` trims to the backtest range. Preflight an actual 120+ complete contiguous historical warmup, including prior-20 calculation, **before** the run window/feature trimming. Do not treat configured max_records as proof of returned bars.
- **Feature time and controller:** `backtesting_engine_base.py::prepare_market_data` performs backward `merge_asof` from `timestamp_bt` to `features.timestamp` and copies raw open timestamps into engine rows. Features must join on **raw T[t]**, while decisions are independently marked as effective `E[t]` only after that candle completes. `simulate_execution` updates the row then calls `controller.determine_executor_actions()`. A dedicated future strategy controller (NOT yet implemented) must remember t's signal and dispatch only on t+1's designated fill row, never use t+1 data to form t's signal.
- **Order path:** Emit `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1))`. `executors/order_executor/data_types.py` validates positive amount and permits MARKET without limit price. `backtesting_engine_base.py::simulate_executor` routes to `executors_simulator/order_executor_simulator.py`; its MARKET path fills on **first supplied historical row** at that row's **actual close**, sets filled quote, charges `trade_cost*filled_quote`, and terminates `POSITION_HOLD`. The controller must delay dispatch to the preselected t+1 row. Raw fill row is open-labeled; effective historical fill event is `E[t+1]`. This is a **retrospective close-price full-fill simulator convention**, not a claim of executable live market orders at a known close.
- **Ledger and costs:** Pinned `BacktestPositionHold` nets confirmed BUY/SELL base, accumulates gross realized/unrealized PnL and `cum_fees_quote` separately; its `_process_order` uses matched volume and average entry. Reconcile a separate Decimal spot cash/BTC ledger against complete confirmed executor fills and fee totals; do not equate gross `net_pnl_quote` with fee-inclusive net portfolio PnL or infer fills from intended actions. Starting cash 10,000 USDT, BTC 0. Hypothetical `trade_cost=0.001` per executed side; round-trip modeled net `Q*(P_sell-P_buy)-0.001*Q*(P_buy+P_sell)`. This is **not** an observed Binance fee tier. Spot without leverage has **no perpetual funding or liquidation flow** (not a claim of observed zero futures funding). Real exchange min-notional/precision, slippage, depth, latency, partial fills and order acceptance remain **unverified**; none is silently asserted or needed by this explicitly idealized historical path.
- **Fail closed:** `BacktestingDataProvider.get_price_by_type` may return `Decimal("1")` for a missing price. **Forbid this fallback** for any fill/mark. Reject invalid/missing real close, feed gaps, fee/position ledger disagreement, incomplete warmup, unsupported executor actions or unconfirmed fills. No multi-asset, MTF, funding, maker, next-open, intrabar or live engine path is required. Any future change requiring those primitives is a **new** capability check before large-scale screening.

## Six-gate evidence and independent review focus

1. **G1 reproducible:** previous-20 SMA, exact volume comparison, candle sign/doji, capped normalized impulse, 0.95 recursive state and exact zero crossing fully specified.
2. **G2 direction:** unlevered Binance BTC-USDT spot LONG/FLAT; short explicitly disabled.
3. **G3 entry/exit/risk:** fresh positive zero-cross entry, nonpositive-score exit, no hidden SL/TP/trailing/time exit; prolonged adverse holds are a material limitation.
4. **G4 position:** 0.001 BTC, 10,000 USDT, one pending action/position, no DCA/pyramiding, explicit pending/re-entry/last-bar rules.
5. **G5 engine:** pinned Binance spot 1h OHLCV, actual controller/action/MARKET-close/POSITION_HOLD path, modeled per-fill fee and separate cash/position accounting; no assertion of live economic fidelity.
6. **G6 causality:** completed-bar decision `E[t]`, delayed fill `E[t+1]`, previous-only volume baseline, 120-bar warmup, no future bar for decisions or invented price.

**Auditor must independently verify**: source-date/revision and *explicitly derived* lineage rather than native equivalence; whether the decayed block-state mechanism is materially distinct from existing volume strategies; strict previous-20 and zero-cross edges; fill-bar signal suppression; actual cached warmup and open-label/effective-close timestamp separation; pinned package correspondence, executor accounting and all model limitations. This is a Scout **PASS claim for independent review**, not independent certification, profitability, Qlib parity or trading authorization. No backtest, Paper/Testnet/Live trade, container or scheduler change was performed.
