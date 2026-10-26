---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FPT Harami full-range containment reversal — BTCUSDT spot 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-12-26
sources:
  - https://www.tradingview.com/script/xYGhNjjy-FPT-Harami/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FPT Harami full-range containment reversal — BTCUSDT spot 1d independent derivative

## Provenance

- **Primary TradingView source:** erendev, *FPT – Harami (Wick Included)*, published **Dec 26, 2025**, public **open-source indicator** ID **xYGhNjjy**, page directly fetched and read as of **2026-10-26** (294,060 bytes HTML): https://www.tradingview.com/script/xYGhNjjy-FPT-Harami/. The page carries the `Open-source script` badge (`rootOpenSource`, "the creator of this script has made it open-source"). The retrievable meta description is the source of the source-reported facts below: "a clean and minimalist candlestick pattern indicator that highlights Harami reversal formations using full candle ranges (wicks included)", following "a strict and objective definition of Harami by requiring the entire range of the second candle (high–low) to be fully contained within the range of the first candle". **Bullish Harami:** first candle bearish, second candle bullish, second candle's high and low completely inside the first candle's range. **Bearish Harami:** the mirror. Design philosophy stated on the page: "No indicators. No filters. No assumptions about trend or volatility." The full Pine text, its revision, and its immutable code hash were **not retrieved**; do not assert lossless Pine equivalence, original indicator outputs, or any backtest metrics.
- **Frozen independent derivative identity:** `TV:xYGhNjjy:erendev:2025-12-26 | independent-derived-v1:2026-10-26 | bullish-range-containment-entry | bearish-range-containment-exit | strict-color-no-trend-filter | BinanceSpot:BTC-USDT:1d:LONG-FLAT:Q0.001BTC:close-effective-MARKET:trade_cost0.001:20bar-warmup`.
- **Source-native descriptive facts:** two-candle Harami detection only — no entries, exits, stops, targets, sizing, warmup, cost model, or order settings are specified anywhere on the source page (it is a visual indicator; its own text states it "does not provide trade signals" and is "for visual analysis only"). Every order-level behavior below is researcher-declared.
- **Researcher-defined changes, not source facts:** this separately identified strategy freezes strict candle colors (bearish := `C<O`, bullish := `C>O`; a doji on either bar satisfies neither predicate), freezes **non-strict** range containment (`H[t]<=H[t-1]` and `L[t]>=L[t-1]`, equality admits — disclosed), keeps the source's no-trend-filter stance (no SMA/EMA trend gate is added), trades only Binance BTC-USDT spot on UTC `1d`, enforces LONG/FLAT with one 0.001 BTC unit, simulates completed-close MARKET fills, exits LONG only on a completed bearish-containment pair, explicitly disables the source short direction, sets 20 contiguous completed-bar warmup, gives exits priority, and defines data-failure and re-entry semantics. This record is **not** an admission claim for the author's original Pine program.
- **Rejected sibling mechanism (disclosed, not proposed):** the Traaaderz *All Candlestick Patterns Strategy* body-containment Harami (`C_HaramiBullish`/`C_HaramiBearish`: child wicks inside the mother *body*, plus `ema(C_Body,14)` Long/SmallBody tests and an SMA50 trend gate — verbatim code verified byte-identical, sha256 `a427adbf…c172a2da`, between the public tv-mirror copy and `https://raw.githubusercontent.com/hasnocool/tradingview-pine-scripts/e031cab2819a7d56fb8bb9d000252f51439986e2/All%20Candlestick%20Patterns%20Strategy.pine`) was evaluated against 1,000 real Binance BTCUSDT `1d` klines and printed **zero** signals in ~2.7 years: on gapless crypto klines the body-containment conjunction reduces to a tick-exact zero-wick requirement that never jointly holds. It is documented here as negative selection evidence only and is not this candidate.

Pre-write duplicate check against the actual `main` tree at `9c2c720b1e52de0abf64cfffa212e3052f8780ec`, repo-wide grep and the ten open `research/*` PRs: no record or open PR with TradingView script ID `xYGhNjjy`, author `erendev`, or this immutable derived identity. Case-insensitive `harami` hits in `main` are passing prose only (`three-white-soldiers-black-crows-flip-two-sided-…` mentions Harami among related patterns; `forven-donchian-regime-breakout-…`, `forven-keltner-adx-gated-…`, `rvi-swma-cross-…` mention `piercing` in passing) — no record is built on any Harami rule. `kdj-golden-cross-…` mentions `three inside` in passing. Closed-PRs sweep (100 most recent, including #469 saucius-vortex, #464 Alpha33, #453 Bandtastic, #448 vnpy-AtrRsi, #443 Gap-Fill, #439 PSY12) returns no Harami-titled candidate. The ten open `research/*` PRs (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2yMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles KCD) contain no Harami rule.

## Economic mechanism

### Source-reported

A two-candle Harami (large directional candle followed by a smaller opposite-color candle whose full high–low range sits inside the first candle's range) is presented as a potential early warning of momentum slowdown or short-term reversal. No economics beyond pattern detection are stated.

### Research interpretation

This derivative buys a *completed* bullish range-containment pair and holds until a *completed* bearish range-containment pair. It trades pure two-candle geometry with no moving average, no oscillator, and no volatility filter — the only memory in the system is the FLAT/LONG position state. Because there is no stop, target, or time exit, a decline that never prints a bearish-containment pair leaves the long exposed indefinitely; the only risk control is the opposite-pattern close exit. Real-kline evidence (below) shows roughly one print per side every two weeks on BTCUSDT `1d` — a sparse, selective reversal book, not a high-turnover system.

## Signal

Let `O[t], H[t], L[t], C[t]` be a **fully completed** UTC daily OHLC bar with positive finite values and `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]>0`. No indicator is computed; the rule reads OHLC only.

1. **Entry predicate `B[t]`** on completed pair `(t-1, t)`: `O[t-1]>C[t-1]` (bearish mother, strict) AND `O[t]<C[t]` (bullish child, strict) AND `H[t]<=H[t-1]` AND `L[t]>=L[t-1]` (full-range containment, non-strict and disclosed: a child high exactly equal to the mother high, or low exactly equal to the mother low, still prints).
2. **Exit predicate `R[t]`** on completed pair `(t-1, t)`: `O[t-1]<C[t-1]` AND `O[t]>C[t]` AND `H[t]<=H[t-1]` AND `L[t]>=L[t-1]`.
3. `B[t]` and `R[t]` are **mutually exclusive by construction**: they require opposite strict colors on *both* bars (`O[t-1]>C[t-1]` vs `O[t-1]<C[t-1]`, and `O[t]<C[t]` vs `O[t]>C[t]`); a doji on either bar satisfies neither. Proven over 980 real-kline decisions with zero joint triggers (see Evidence). On a valid completed bar, process **EXIT before ENTRY** as a standing rule (moot under exclusivity, binding if inputs ever change).
4. Direction and state: only `FLAT` or `LONG(0.001 BTC)`, initially FLAT. If LONG and `R[t]`, issue one full-quantity SELL. Else if FLAT and `B[t]`, issue one BUY. Otherwise hold. Never short; no pyramiding, scaling, averaging, BO/SO, DCA, reverse orders, hedges, or simultaneous position/executor exposure. An entry predicate while LONG is a no-op; an exit while FLAT is a no-op. Re-entry is allowed on a **future completed bar** with a fresh eligible entry predicate only after SELL fill confirmation. No cooldown, no pending limit orders. At most one outstanding MARKET action; never infer a fill from mere order submission.
5. No stop-loss, take-profit, trailing stop, maximum holding period, forced end-of-sample liquidation, equity-based sizing, leverage, margin, funding payment, or session/date restriction. These are **explicitly disabled researcher decisions** (the source specifies no order behavior at all), not asserted script defaults. Unclosed positions at the predetermined research end remain marked open and must not be represented as realized PnL.

## Required data

- One Binance **spot** market `BTC-USDT`, interval `1d`, UTC day boundary, `open/high/low/close` and original candle-open timestamp. No volume, external security, order book, trades, futures funding, mark/index price, higher/lower timeframe, ML model, shared capital, or portfolio synchronization is used.
- Each exchange candle's timestamp labels its **OPEN**, not its completed-close availability. Define `decision_ts[t] = candle_open_ts[t] + 86400` seconds; use the completed candle only when all its OHLC values are available. Feed prepared engine rows with the effective **completed-close timestamp**, never the original open timestamp for decision or simulated fill. Check monotonicity and exactly contiguous 86400-second UTC daily opens.
- The first **20** fully completed, contiguous, validated bars are warmup-only and cannot trigger orders (the pair need is two bars; twenty is the independently declared conservative warmup, same package as the sibling TradingView candle-pattern `1d` derivative). No centered windows, future extrema, negative shifts, incomplete daily bar, full-sample preprocessing or repainting.
- A missing, nonfinite, nonpositive or inconsistent OHLC, absent completed close, timestamp gap, or unsorted bar blocks that bar's pair decisions **and fill**. Do not synthesize candles or substitute a prior price. Resume decisions only after 20 new contiguous valid completed bars; an existing LONG stays open during the gap, with no fictitious stop/exit or fee. A pending unconfirmed order must be reconciled from its real simulated fill ledger before any further action; never invent completion. Such gaps can prolong unprotected exposure.

## Execution assumptions

**Pinned baseline:** Hummingbot package label `20260920`, `hummingbot/VERSION = dev-2.17.0`, pinned `HCH725/hummingbot` source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout directly fetched and read these pinned files at that commit (not an unpinned online API or current main):

- `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` — `_parse_rest_candles` reads REST `row[0]` as the **open timestamp** (`ensure_timestamp_in_seconds(row[0])`) with OHLC values; `.../constants.py` explicitly supports interval `1d` (`INTERVALS` bidict).
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` — `BacktestingEngineBase.simulate_execution` loops row-wise over timestamped prepared rows (`for i, row in processed_features.iterrows()`), calls `controller.determine_executor_actions()`, and routes each `CreateExecutorAction` to the executor simulator with the forward slice **starting at the current row** (`processed_features.loc[i:max_ts]`); `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60*60` seconds; `BacktestPositionHold` nets same-pair BUY/SELL average-cost ("Buys and sells of the same asset net out automatically"), realized gross PnL and cumulative quote fees.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` — `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, BUY/SELL, base amount 0.001 fills at the **first supplied row's close** (`fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close at fill_timestamp`), records `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, then reports `CloseType.POSITION_HOLD`. Together with the current-row forward slice, a completed-close signal at `decision_ts` produces a same-effective-timestamp MARKET-close **simulation** on that prepared row. This is the actual pinned close-effective **backtest** primitive, not an exchange close auction or an intrabar fill. The researcher-defined controller would be a strategy-specific `DirectionalTradingController` emitting these actions; **it is not implemented or deployed**.

**Critical fill/position-state setting:** instantiate `BacktestingEngineBase(terminated_executors_window=None)` so the controller can see fill-confirmed executors on subsequent daily decisions. The pinned default is only 3600 seconds and may hide the previous daily fill from `controller.executors_info`; the engine still has an internal stopped ledger. Maintain explicit controller-side fill-confirmed quantity, pending-action suppression, and position cost/fee ledger; never equate `POSITION_HOLD` with a fresh unfilled order or assume an order was filled when submitted. This model convention does **not** establish causal executable live close fills. A future execution path that cannot honor the same effective-timestamp model must be revalidated as a distinct derivative.

**Cost and capital:** research `initial_quote_cash=10000 USDT`, fixed `amount=0.001 BTC`, `trade_cost=0.001` of quote notional **per simulated BUY and SELL fill**, modeled slippage `0` as an expressly artificial simulation assumption. Do not describe this 0.1% as a measured exchange fee or the zero modeled slippage as realized slippage. Require sufficient simulated cash including modeled BUY fee; if not, no BUY. SELL only confirmed available base quantity. Unleveraged spot has no perpetual-futures funding contract; **no claim of zero realized futures funding** is made. Actual maker/taker schedules, lot/tick rounding, min notional, spread, latency and partial fills are not verified and are not authorized for Paper/Testnet/Live. Model net realized quote PnL as `BacktestPositionHold.realized_pnl_quote - BacktestPositionHold.cum_fees_quote`, **not** the gross-only executor PnL field. No fabricated prices or fills. Float rounding residuals must not create a second position.

The existing independently reviewed **PR #417** documented the same pinned Binance spot `1d` / MARKET first-close / POSITION_HOLD research primitive (reused here with no novel execution primitive); the wheel-to-commit binary hash was **not revalidated in this Scout cycle**. The package label `20260920` is retained as a policy label only; no package-to-commit byte mapping is invented. Gate 5 relies on the directly inspected pinned code path and the existing reviewed evidence, not a claim of fresh wheel-byte identity or an implemented controller. No futures/margin/shared-capital/new data primitive is needed.

## Evidence

### Source-reported

TradingView `xYGhNjjy`, erendev, 2025-12-26: open-source Harami indicator; strict full-range (wicks-included) containment definition; bullish = bearish first + bullish second with second high–low completely inside first range; bearish mirror; no indicators, filters, or trend assumptions. No entries, exits, stops, targets, sizing, warmup, cost, or order settings exist on the source page.

### Independently reproduced

**Rule-logic self-check (stdlib only, not a backtest):** the frozen `B[t]`/`R[t]` inequalities plus the FLAT/LONG state machine were executed over (a) hand-constructed boundary pairs — equality containment admits, doji on either bar blocks both legs, wrong-color pairs never trigger; and (b) a 980-decision walk over 1,000 real Binance BTCUSDT `1d` klines (all bars validated finite/positive/consistent): zero co-fires, **34 BUY / 34 SELL strictly alternating round trips**, ending FLAT. **Engine-code inspection only, not a strategy backtest:** pinned Hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` was read file-by-file for the Binance spot `1d` candle parser (open-timestamp rows), the row-wise engine action loop with current-row forward slices, MARKET-first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, `hummingbot/VERSION` and 3600-second vs `None` terminated-executor visibility. The candidate's trade events, Pine outputs, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

- No full Pine revision or indicator output series is available from the retrieved source page; **source-native/lossless equivalence is unverified**. The independent derivative is evaluated against its own frozen rules only. Researcher freezes (strict colors, non-strict containment) are disclosed above and may change events versus the author's Pine on boundary bars.
- The Traaaderz body-containment Harami variant (byte-pinned code) prints zero signals on ~2.7 years of real BTCUSDT `1d` data and was rejected for that reason; it is not this candidate and does not validate it.
- Closed Scout PR #220 used TA-Lib gap-penetration two-sided flip semantics on perpetual markets — a different source, different arithmetic, different market and position model; it is not this candidate.
- No verified live close fill, partial fill, market impact, exchange fee schedule, futures funding or venue order-size permission. None is silently imputed.

## Deduplication

Main at immutable SHA **9c2c720b1e52de0abf64cfffa212e3052f8780ec** contained **349** root strategy records; README static count **349**. Working-tree filename/content search for `xYGhNjjy`, `erendev`, `fpt-harami`, and `harami` returns zero strategy records built on any Harami rule (only passing prose mentions); GitHub title search for Harami returns no prior candidate, and a 100-PR closed sweep returned no Harami-titled PR. Ten open research/* PRs were checked (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none carries this primary source or a Harami rule.

Nearest neighbors are **not equivalent**: `tradingview-dipalishah94-morning-evening-star-ratio-long-flat-btcusdt-1d-2026-10-26` trades a *three*-candle body-ratio/midpoint-penetration star (35/55/50 arithmetic, no averages, no containment) — this record trades a *two*-candle full-range containment with strict colors and no ratios, thresholds, or averages of any kind; `three-white-soldiers-black-crows-flip-two-sided-btcusdt-1d-2026-10-14` trades TA-Lib three-candle continuation geometry, two-sided; `wick-reversal-hammer-shooting-star-long-flat-btcusdt-1d-2026-10-16` trades single-candle wicks; `dual-ema-engulfing-volume-long-btcusdt-1h-2026-10-07` trades the *inverse* geometry (child larger than mother) gated by EMA stack and volume on `1h`. Different source, different signal construction, different risk book: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

1. Hand-construct completed daily OHLC pairs for containment just outside/at equality on each rail, wrong-color and doji mothers/children, and inconsistent/nonpositive bars. Verify trigger/no-trigger, strict color exclusivity on both bars, and exit-before-entry ordering.
2. Ablate non-strict containment (`<=`/`>=`) against a strict (`<`/`>`) variant on predeclared IS/OOS partitions and verify the ablation actually changes print/round-trip event times; do not tune on OOS.
3. Check warmup bars 1–20, missing/invalid OHLC, nonmonotone/gapped timestamps, FLAT/LONG/pending order transitions, fill-ledger persistence across 86400 seconds, and no same-bar re-entry after a SELL.
4. If formally selected downstream, build the minimal strategy-specific controller/recipe and validate **representative event-level Qlib/Hummingbot parity for this execution primitive** before broad Qlib screening if that primitive has not already been independently validated. Compare timestamp, signal, action, confirmed fill, quantity, fee and position-cost state. A model capability failure is an engineering hold, not a retroactive profitability or admission decision. No performance/Sharpe/OOS claim is made here.

## Crypto portability

Only `BTC-USDT` Binance spot `1d` is pinned in this research record. Other assets, timeframes, market types, and the downstream seven-coin × three-timeframe × leverage/DCA research campaign are **separate experiments**, not HB_READY admission requirements or silently equivalent original source behavior. Applying BO/SO overlays or futures economics changes this frozen trade-event/economic model and requires an explicitly declared derivative.

## Limitations

- A bullish-containment pair can print repeatedly through a crash; without SL/TP/time stop this strategy can hold through substantial adverse moves, and the source specifies no protection to remove — exposure control is the opposite-pattern exit alone.
- Real-kline evidence shows sparse prints (~125 containment pairs, 34 round trips over ~2.7 years); long flat stretches and regime-dependent print droughts are expected, not a malfunction.
- The source is a visual indicator with no order semantics; entries/exits happen at the simulated pair-completion close, which cannot match any original indicator output timing one-to-one.
- Exact source Pine revision, boundary-bar comparator strictness in the author's code, and profitability are unknown. The simulated completed-close fill is a **backtest convention**, not a live execution guarantee.
- The modeled 0.1%-per-side research cost, zero modeled slippage, fixed base size and absence of futures funding do not prove actual Binance trade economics. A long position can remain exposed during data outages. No Qlib parity, survivor status or trading approval follows from HB_READY.

## Implementation status

`not-implemented`: no candidate-specific controller, Qlib executable artifact, backtest, deployment, Paper/Testnet/Live run or position exists. The pinned Hummingbot MARKET/POSITION_HOLD **capability** is demonstrated; candidate implementation and reproducible replay remain future downstream work, not a second admission gate.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, subject to an **independent Hermes Auditor GitHub Webhook Review** of this exact PR head. Only that reviewer may remediate source-verifiable facts, exact-head merge on six-gate PASS, or close the Scout PR as NOT_LOSSLESS. No autonomous adoption, order placement, Qlib/Hummingbot execution, or README edit.

## Related Wiki records

None created or modified. Future research may link an existing Hermes Wiki Brain record after independent approval; this PR changes only this one root-level strategy record.

## Sources

1. https://www.tradingview.com/script/xYGhNjjy-FPT-Harami/ — erendev, *FPT – Harami (Wick Included)*, published 2025-12-26; primary descriptive strategy rules, inspected 2026-10-26.
2. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py — pinned MARKET fill and fee path.
3. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py — pinned row loop, current-row forward slice, position/cost ledger and terminated-executor visibility.
4. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py — pinned Binance spot open-timestamp OHLC parser.
5. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py — pinned `1d` interval.
6. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION — pinned `dev-2.17.0`.
7. https://github.com/HCH725/alpha-strategy-research/pull/417 — previously reviewed package/source identity evidence for the same pinned primitive; **not** a fresh binary hash verification.
