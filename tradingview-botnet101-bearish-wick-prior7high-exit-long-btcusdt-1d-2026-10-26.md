---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Botnet101 bearish lower-wick rejection with prior-seven-high close exit — BTCUSDT spot 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-01-24
sources:
  - https://www.tradingview.com/script/Kz4wRzup-Bearish-Wick-Reversal/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Botnet101 bearish lower-wick rejection with prior-seven-high close exit — BTCUSDT spot 1d independent derivative

## Provenance

- **Primary TradingView source:** Botnet101, *Bearish Wick Reversal*, published **2025-01-24**, public/open-source TradingView **strategy** ID **Kz4wRzup**, inspected as of **2026-10-26**: https://www.tradingview.com/script/Kz4wRzup-Bearish-Wick-Reversal/. The publicly retrievable author description, not a verified Pine source revision, is the source of the source-reported facts below. The full Pine text, its version, and its immutable code hash were **not retrieved**; do not assert lossless Pine equivalence, original TradingView fills, or original backtest metrics.
- **Frozen independent derivative identity:** `TV:Kz4wRzup:Botnet101:2025-01-24 | independent-derived-v1:2026-10-26 | bearish-close<open and (low-close)/close*100<=-1.0 | exit-close>max(prior-7-highs) | EMA-filter-disabled, date-filter-disabled | BinanceSpot:BTC-USDT:1d:LONG-FLAT:Q0.001BTC:close-effective-MARKET:trade_cost0.001:20bar-warmup`.
- **Source-native descriptive facts:** bearish candle (`close < open`) with extended downside wick; author describes the wick as `(low - close)/close * 100`, with default threshold **−1%**; an optional **EMA200** trend filter; an author-configurable time window; sell when `close > _highest[1]`, explained by the author as the **highest high of the previous seven bars**. The source describes a long-entry and sell-exit strategy. No verified source-native stop, target, DCA, short entry, exact order clock, or cost model was recovered.
- **Researcher-defined changes, not source facts:** this separately identified strategy fixes the strict/equality comparator at `<= −1.0`, turns OFF the optional EMA and time-window filters, chooses Binance BTC-USDT spot on UTC `1d`, enforces LONG/FLAT and one 0.001 BTC unit, sets 20 contiguous completed-bar warmup, gives exits priority on simultaneous predicates, simulates completed-close MARKET fills, freezes a research-only 0.001 per-side notional cost, explicitly disables all other orders and defines data-failure and re-entry semantics. These changes may alter source-native trade events. This record is **not** an admission claim for the author's original Pine program.

Pre-write duplicate check against the actual `main` tree at `5b4caf1fd2e4518bbfe788cbd18547d1f8b9a60a`, GitHub code search and the ten open `research/*` PRs: no record or open PR with TradingView script ID `Kz4wRzup`, the Botnet101 bearish-wick/previous-seven-high rule pair, or this immutable derived identity. Existing `wick-reversal-hammer-shooting-star-long-flat-btcusdt-1d-2026-10-16.md` instead uses a **prior-bar half-range hammer**, a **15-bar ±5% momentum context** and a **current shooting-star** exit. Existing `tradingview-pridarasx-turtle-soup-onebar-confirm-long-flat-btcusdt-1d-2026-10-25.md` instead uses a prior-20-bar low sweep and a next-bar confirmation. The proposed **same-bar close-relative −1% lower wick entry / prior-seven-high close breakout exit** is materially different, not a trivial parameter variant. The existing `ibs-mean-reversion-short-ethusdt-1h-2026-10-06.md` mentions author Botnet101 but uses a distinct IBS rule and TradingView source.

## Economic mechanism

### Source-reported

A bearish bar that rejects a downside excursion by a sufficiently long lower wick may indicate capitulation or absorption. The author's exit waits for a closing-price breakout above the highest high of the previous seven bars as a bullish confirmation. The author notes that prolonged bearish trends can create false reversal signals; the optional EMA200 filter is intended to restrict trades by trend. These are hypotheses, not demonstrated profits.

### Research interpretation

This derivative buys a *large downside rejection during a still-bearish candle*, then holds until a **seven-prior-bar high close breakout**. It is neither a moving-average crossover nor a generic hammer plus shooting-star reversal. A continued decline may leave the long position exposed indefinitely because no protective price or time stop is defined.

## Signal

Let `O[t], H[t], L[t], C[t]` be a **fully completed** UTC daily OHLC bar with positive finite `C[t]` and `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]>0`. Require seven strictly prior completed highs and at least twenty contiguous completed bars before trading.

1. `wick_pct[t] = 100 * (L[t] - C[t]) / C[t]`. **Entry predicate:** `C[t] < O[t] AND wick_pct[t] <= -1.0`. This negative sign follows the author's displayed low-minus-close convention. `−1.0` and the inclusive comparator are frozen researcher choices informed by the source's stated default threshold; do not silently substitute the usual `(min(O,C)-L)/(H-L)` hammer formula.
2. `prior7_high[t] = max(H[t-7], H[t-6], ..., H[t-1])`. **Exit predicate:** `C[t] > prior7_high[t]` (strict greater-than; today's high is **excluded**). A current-bar high breakout without a closing-price breakout is not an exit.
3. On a valid completed bar, process **EXIT before ENTRY**. If LONG and exit predicate true, issue one full-quantity SELL and suppress BUY for that bar. If FLAT and exit predicate true, take no action even if the entry predicate also holds. Otherwise, if FLAT and entry predicate true, issue one BUY. If neither eligible predicate holds, retain current position. If a predicate is exactly on a threshold, use the explicit `<=` entry / `>` exit operators, with no floating tolerance.
4. Direction and state: only `FLAT` or `LONG(0.001 BTC)`, initially FLAT. Never short; no pyramiding, scaling, averaging, BO/SO, DCA, reverse orders, hedges, or simultaneous position/executor exposure. An entry predicate while LONG is a no-op; an exit while FLAT is a no-op. Re-entry is allowed on a **future completed bar** with a fresh eligible entry predicate only after SELL fill confirmation. No cooldown, no pending limit orders. At most one outstanding MARKET action; never infer a fill from mere order submission.
5. No stop-loss, take-profit, trailing stop, maximum holding period, forced end-of-sample liquidation, equity-based sizing, leverage, margin, funding payment, or session/date restriction. These are **explicitly disabled researcher decisions**, not asserted Pine defaults. Unclosed positions at the predetermined research end remain marked open and must not be represented as realized PnL.

The optional author EMA200 filter is **disabled**, not assumed to be ON by default; there is no EMA calculation in this derived decision path. The source's configurable time-window gate is **disabled**. No inferred original risk or execution settings are imported.

## Required data

- One Binance **spot** market `BTC-USDT`, interval `1d`, UTC day boundary, `open/high/low/close` and original candle-open timestamp. No volume, external security, order book, trades, futures funding, mark/index price, higher/lower timeframe, ML model, shared capital, or portfolio synchronization is used.
- Each exchange candle's timestamp labels its **OPEN**, not its completed-close availability. Define `decision_ts[t] = candle_open_ts[t] + 86400` seconds; use the completed candle only when all its OHLC values are available. Feed prepared engine rows with the effective **completed-close timestamp**, never the original open timestamp for decision or simulated fill. Check monotonicity and exactly contiguous 86400-second UTC daily opens.
- The first **20** fully completed, contiguous, validated bars are warmup-only and cannot trigger orders. Seven prior highs are structurally necessary, and 20 is the independently declared conservative warmup. No centered windows, future extrema, negative shifts, incomplete daily bar, full-sample preprocessing or repainting.
- A missing, nonfinite, nonpositive or inconsistent OHLC, absent completed close, timestamp gap, or unsorted bar blocks that bar's decision **and fill**. Do not synthesize candles or substitute a prior price. Resume decisions only after 20 new contiguous valid completed bars; an existing LONG stays open during the gap, with no fictitious stop/exit or fee. A pending unconfirmed order must be reconciled from its real simulated fill ledger before any further action; never invent completion. Such gaps can prolong unprotected exposure.

## Execution assumptions

**Pinned baseline:** Hummingbot package label `20260920`, `hummingbot/VERSION = dev-2.17.0`, pinned `HCH725/hummingbot` source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout inspected these pinned GitHub files, not an unpinned online API or current main:

- `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` — Binance spot klines parse REST row[0] as **open timestamp**, with OHLC values; `.../constants.py` explicitly supports interval `1d`.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` — `BacktestingEngineBase` loops over timestamped prepared rows, updates state, dispatches `CreateExecutorAction`, simulates executor on that row's forward slice, and maintains `BacktestPositionHold` average-cost, realized gross PnL and cumulative quote fees.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` — `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, BUY/SELL, base amount 0.001 fills at the **first supplied row's close**, records `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, then reports `CloseType.POSITION_HOLD`. This is the actual pinned close-effective **backtest** primitive, not an exchange close auction, a next-open fill or an intrabar stop. The researcher-defined controller would be a strategy-specific `DirectionalTradingController` emitting these actions; **it is not implemented or deployed**.

**Critical fill/position-state setting:** instantiate `BacktestingEngineBase(terminated_executors_window=None)` so the controller can see fill-confirmed executors on subsequent daily decisions. The pinned default is only 3600 seconds and may hide the previous daily fill from `controller.executors_info`; the engine still has an internal stopped ledger. Maintain explicit controller-side fill-confirmed quantity, pending-action suppression, and position cost/fee ledger; never equate `POSITION_HOLD` with a fresh unfilled order or assume an order was filled when submitted. A completed-close signal at `decision_ts` produces a same-effective-timestamp MARKET-close **simulation** on that prepared row; this model convention does **not** establish causal executable live close fills. A future execution path that cannot honor the same effective-timestamp model must be revalidated as a distinct derivative.

**Cost and capital:** research `initial_quote_cash=10000 USDT`, fixed `amount=0.001 BTC`, `trade_cost=0.001` of quote notional **per simulated BUY and SELL fill**, modeled slippage `0` as an expressly artificial simulation assumption. Do not describe this 0.1% as a measured exchange fee or the zero modeled slippage as realized slippage. Require sufficient simulated cash including modeled BUY fee; if not, no BUY. SELL only confirmed available base quantity. Unleveraged spot has no perpetual-futures funding contract; **no claim of zero realized futures funding** is made. Actual maker/taker schedules, lot/tick rounding, min notional, spread, latency and partial fills are not verified and are not authorized for Paper/Testnet/Live. Model net realized quote PnL as `BacktestPositionHold.realized_pnl_quote - BacktestPositionHold.cum_fees_quote`, **not** the gross-only executor PnL field. No fabricated prices or fills. Float rounding residuals must not create a second position.

The existing independently reviewed **PR #414** documented a wheel/source mapping for this pinned source family; the wheel-to-commit binary hash was **not revalidated in this Scout cycle**. Gate 5 relies on the directly inspected pinned code path and the existing reviewed evidence, not a claim of fresh wheel-byte identity or an implemented controller. No futures/margin/shared-capital/new data primitive is needed.

## Evidence

### Source-reported

TradingView `Kz4wRzup`, Botnet101, 2025-01-24: bearish candle; downside wick `(low-close)/close*100` with stated −1% default; optional EMA200; optional time window; close above the **previous seven highs** as the sell signal. The author provides no independently reproduced performance evidence here. Public page calls the script open-source, but full Pine code/version bytes were not retrieved.

### Independently reproduced

**Engine-code inspection only, not a strategy backtest:** pinned Hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` was read via GitHub connector for the Binance spot `1d` candle parser, row-wise engine action loop, MARKET-first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, `hummingbot/VERSION` and 3600-second vs `None` terminated-executor visibility. The candidate's trade events, TradingView Pine outputs, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

- No full Pine revision or Pine default-order/commission setting is available from the retrieved source page; **source-native/lossless equivalence is unverified**. The independent derivative is evaluated against its own frozen rules only.
- Prior admitted wick-reversal family uses a prior-bar half-range hammer, 15-bar momentum context and shooting-star exit, **not** this −1% close-relative wick and prior-seven-high exit.
- No verified intrabar stop, live close fill, partial fill, market impact, exchange fee schedule, futures funding or venue order-size permission. None is silently imputed.

## Falsification plan

1. Hand-construct completed daily OHLC cases for wick_pct at −0.99%, exactly −1.00%, −1.01%, bullish/neutral candles, and simultaneous entry/exit predicates. Verify strict prior-seven-high exclusion of today's high and strict `C>prior7_high` (equality is not exit).
2. Check warmup bars 1–20, missing close, nonmonotone/gapped timestamps, FLAT/LONG/pending order transitions, fill-ledger persistence across 86400 seconds, and no same-bar re-entry after a SELL.
3. If formally selected downstream, build the minimal strategy-specific controller/recipe and validate **representative event-level Qlib/Hummingbot parity for this execution primitive** before broad Qlib screening if that primitive has not already been independently validated. Compare timestamp, signal, action, confirmed fill, quantity, fee and position-cost state. A model capability failure is an engineering hold, not a retroactive profitability or admission decision. No performance/Sharpe/OOS claim is made here.

## Crypto portability

Only `BTC-USDT` Binance spot `1d` is pinned in this research record. Other assets, timeframes, market types, and the downstream seven-coin × three-timeframe × leverage/DCA research campaign are **separate experiments**, not HB_READY admission requirements or silently equivalent original source behavior. Applying BO/SO overlays or futures economics changes this frozen trade-event/economic model and requires an explicitly declared derivative.

## Limitations

- A lower wick can recur throughout a crash; without SL/TP/time stop this strategy can hold through substantial adverse moves.
- The author's optional EMA200 and time-window filter are deliberately OFF. This can change entries materially versus an original Pine configuration.
- Exact source Pine revision, source-native fill clock, original sizing/cost settings and profitability are unknown. The simulated completed-close fill is a **backtest convention**, not a live execution guarantee.
- The modeled 0.1%-per-side research cost, zero modeled slippage, fixed base size and absence of futures funding do not prove actual Binance trade economics. A long position can remain exposed during data outages. No Qlib parity, survivor status or trading approval follows from HB_READY.

## Implementation status

`not-implemented`: no candidate-specific controller, Qlib executable artifact, backtest, deployment, Paper/Testnet/Live run or position exists. The pinned Hummingbot MARKET/POSITION_HOLD **capability** is demonstrated; candidate implementation and reproducible replay remain future downstream work, not a second admission gate.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, subject to an **independent Hermes Auditor GitHub Webhook Review** of this exact PR head. Only that reviewer may remediate source-verifiable facts, exact-head merge on six-gate PASS, or close the Scout PR as NOT_LOSSLESS. No autonomous adoption, order placement, Qlib/Hummingbot execution, or README edit.

## Related Wiki records

None created or modified. Future research may link an existing Hermes Wiki Brain record after independent approval; this PR changes only this one root-level strategy record.

## Sources

1. https://www.tradingview.com/script/Kz4wRzup-Bearish-Wick-Reversal/ — Botnet101, *Bearish Wick Reversal*, published 2025-01-24; primary descriptive strategy rules, inspected 2026-10-26.
2. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py — pinned MARKET fill and fee path.
3. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py — pinned row loop, position/cost ledger and terminated-executor visibility.
4. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py — pinned Binance spot open-timestamp OHLC parser.
5. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py — pinned `1d` interval.
6. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION — pinned `dev-2.17.0`.
7. https://github.com/HCH725/alpha-strategy-research/pull/414 — previously reviewed package/source identity evidence; **not** a fresh binary hash verification.
