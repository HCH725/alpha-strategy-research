---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Stiffness persistence-count breadth state — BTCUSDT spot 1d independent derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-05-03
sources:
  - https://www.tradingview.com/script/MSH4KJ4x-Stiffness-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stiffness persistence-count breadth state — BTCUSDT spot 1d independent derivative

## Provenance

- **Primary TradingView source:** JMOZ1337, *Stiffness Strategy*, script ID **MSH4KJ4x**, published **May 3, 2020**, described on-page as "A strategy for the Stiffness indicator by everget". This Scout opened the live page anonymously on **2026-10-26** and directly verified: title `Stiffness Strategy by JMOZ1337`, `OPEN-SOURCE SCRIPT` badge ("the creator of this script has made it open-source"), publish date May 3 2020, and author JMOZ1337: https://www.tradingview.com/script/MSH4KJ4x-Stiffness-Strategy/. The base indicator is everget's *Stiffness Indicator* (script ID **Ds1akUBu**, original 2018, "Updated Mar 10, 2019"), same formula, no orders.
- **Pine program text captured this cycle** from the page's rendered source panel (`//@version=4`, `strategy("Stiffness Strategy", overlay=false, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_value=0.075)`), sha256 `e8c5c26aa5ce5b5d1ceca84924d0030840fe395d90e83cece27ff0aad5ba827c` (1,707 chars, render-normalised). Frozen source defaults verbatim: `maLength=100`, `stiffLength=60`, `stiffSmooth=3`, `threshold=90`; long leg `long_cond = crossover(stiffness, threshold)` / `strategy.entry("Long", strategy.long, when=long_cond)` and `long_close = stiffness > threshold and falling(stiffness, 1)` / `strategy.close("Long", when=long_close)`. Upstream revision history beyond this capture is not pinned; do not assert byte-lossless upstream equivalence beyond the captured text.

- **Independent reviewer source verification (2026-10-26):** the primary page identifies public script `PUB;kShSUa4MAdhBfvZkM7cWZ2UMON0dWwpH`, published version `1.0`, created/updated `2020-05-03T05:08:28.013129Z`. Its first-party published-source response contains 1,730 characters with CRLF line endings, SHA-256 `c34032e5d1cf4762834188a4658a5a26da56520538a73283843bc22bcc2e5b4f`; replacing CRLF with LF without any other normalization gives 1,692 characters, SHA-256 `1246696d183f43386546f1112b6c75682bbff69943cd7118ee2cb20590285573`. These independently reproducible source hashes are distinct from the Scout-reported render-normalised capture hash above, which the reviewer has not reproduced. The published program uses `sum(close > bound ? 1 : 0, stiffLength)` followed by built-in `ema(sumAbove * 100 / stiffLength, stiffSmooth)`; it does not explicitly implement the derivative’s missing-bound propagation or SMA-of-three EMA initialization. The existing `na`-until-bound, full-count warmup and SMA-seeded recurrence below are frozen independent-derivative conventions, not independently established Pine built-in equivalence. Only the written long-entry/long-exit predicate expressions were source-verified; identical full indicator state or trade events are not claimed. No formula, initialization, parameter, order timing or state rule is changed by this provenance clarification.

- **Frozen independent derivative identity:** `TV:MSH4KJ4x:JMOZ1337:2020-05-03 | independent-derived-v1:2026-10-26 | stiffness-100-60-3-90-long-leg-only | BinanceSpot:BTC-USDT:1d:LONG-FLAT:Q0.001BTC:close-effective-MARKET:trade_cost0.001:161bar-warmup`.
- **Researcher-defined changes, not source facts:** the source is two-sided (it also ships `short_cond`/`short_close` with `strategy.entry("Short", ...)`); this record keeps the source long-entry/long-exit predicate expressions (not a claim of identical full indicator initialization or trade events) and **explicitly disables the entire short leg** (never short, disclosed adaptation). Source percent-of-equity sizing and its `commission_value=0.075` (Pine percent default) are replaced by the frozen house research frame (fixed 0.001 BTC unit, 0.001 per-side modeled cost, spot market, completed-close MARKET fills, 161-bar warmup, exit-before-entry ordering). This record is **not** an admission claim for the author's original two-sided backtest.
- **Rejected sibling mechanisms (disclosed, not proposed):** LazyBear *Kase Peak Oscillator* (full Pine visible, but no entry/exit/state predicate exists — long rule would be invented); everget *Trendscore* (oscillator only, no threshold or exit); NilsXBT *Demand Index Strategy* (predicate degenerate: `di in (0,1]` so `di>0` always true, `di<0` never); LazyBear *Coral Trend* (complete slope-flip rules, but another smoothed-price trend-flip line crowding the taken SuperTrend/HalfTrend/PMax/SSL/UT-Bot/Chandelier/Gann-Hilo cohort — dedup reject).

Pre-write duplicate check against the actual `main` tree at `8afade7` (351 root records), repo-wide grep and all ten open `research/*` PRs: no record or open PR with script ID `MSH4KJ4x`/`Ds1akUBu`, author `JMOZ1337` stiffness, or this derived identity. Case-insensitive `stiffness` hits in `main` are one record only (`rwi-dominant-leg-state-following-…`, same author JMOZ, different RWI-volatility indicator and different arithmetic — not this candidate). The ten open `research/*` PRs (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles KCD) contain no Stiffness rule.

## Economic mechanism

### Source-reported

Breadth-persistence of closes holding above a volatility-shifted mean: when nearly every close of the last 60 bars sits above `sma(close,100) − 0.2·σ₁₀₀`, the market is "stiff" (persistent bid); the strategy buys the upside threshold cross and exits when stiffness rolls over while still elevated. No further economics are stated.

### Research interpretation

This derivative buys a *completed-bar* upside cross of the stiffness gauge through 90 and holds until the gauge falls while still above 90. It trades pure close-price persistence counting with no volume, no ATR stop, no trend gate, and no oscillator normalization — the only memory is the FLAT/LONG position state plus the causal indicator recursion. Because there is no stop, target, or time exit, a decline that never prints a rollover-above-90 leaves the long exposed indefinitely; the only risk control is the rollover exit. Real-kline evidence (below) shows 8 entries over ~7.75 years on BTCUSDT `1d` — a sparse, selective persistence book, not a high-turnover system.

## Signal

Let `C[t]` be a **fully completed** UTC daily close with finite positive OHLC and `H[t]>=max(O[t],C[t])>=min(O[t],C[t])>=L[t]>0`. Independent derivative numeric semantics frozen (Pine built-in initialization equivalence is not claimed): `stdev` is the **population** σ (÷N); `sma` is simple; `crossover(a,b)` ⇔ `a[t]>b AND a[t-1]<=b`; `falling(s,1)` ⇔ `s[t]<s[t-1]`; `ema(x,3)` uses `alpha=2/(3+1)=0.5` seeded with the SMA of its first 3 values (seed-invariance verified: first-value vs SMA seed print identical event sets — see Evidence).

1. `bound[t] = sma(C,100)[t] − 0.2·stdev(C,100)[t]`.
2. `above[t] = (C[t] > bound[t]) ? 1 : 0` — strict `>`; equality counts as NOT above (disclosed); `na` while `bound` is `na`.
3. `cnt[t] = Σ above[t-59 … t]` (integer 0…60).
4. `stiffness[t] = ema(cnt[t]·100/60, 3)`.
5. **Entry predicate `E[t]`:** `stiffness[t] > 90 AND stiffness[t-1] <= 90` (source `crossover(stiffness, threshold)`, threshold frozen at 90).
6. **Exit predicate `X[t]`:** `stiffness[t] > 90 AND stiffness[t] < stiffness[t-1]` (source `stiffness > threshold and falling(stiffness, 1)`).
7. `E[t]` and `X[t]` are **mutually exclusive by construction**: entry requires `stiffness[t-1] <= 90`; exit requires `90 < stiffness[t] < stiffness[t-1]`, hence `stiffness[t-1] > 90`. Proven over 2,830 real-kline decisions with zero joint triggers. On a valid completed bar, process **EXIT before ENTRY** as a standing rule (moot under exclusivity, binding if inputs ever change).
8. Direction and state: only `FLAT` or `LONG(0.001 BTC)`, initially FLAT. If LONG and `X[t]`, issue one full-quantity SELL. Else if FLAT and `E[t]`, issue one BUY. Otherwise hold. Never short; no pyramiding (source ships no `pyramiding` argument — Pine default 0, repeat crosses while LONG are no-ops), scaling, averaging, BO/SO, DCA, reverse orders, hedges, or simultaneous position/executor exposure. Re-entry is allowed on a **future completed bar** with a fresh `E[t]` only after SELL fill confirmation (a dip to `<=90` is mandatory before any fresh cross). No cooldown, no pending limit orders. At most one outstanding MARKET action; never infer a fill from mere order submission.
9. No stop-loss, take-profit, trailing stop, maximum holding period, forced end-of-sample liquidation, equity-based sizing, leverage, margin, funding payment, or session/date restriction. These are **explicitly disabled researcher decisions** (the source declares no `strategy.exit`, no stop, no target, no trailing), not asserted script defaults. Unclosed positions at the predetermined research end remain marked open and must not be represented as realized PnL.

## Required data

- One Binance **spot** market `BTC-USDT`, interval `1d`, UTC day boundary, `open/high/low/close` and original candle-open timestamp. No volume, external security, order book, trades, futures funding, mark/index price, higher/lower timeframe, ML model, shared capital, or portfolio synchronization is used (the rule reads closes only).
- Each exchange candle's timestamp labels its **OPEN**, not its completed-close availability. Define `decision_ts[t] = candle_open_ts[t] + 86400` seconds; use the completed candle only when all its OHLC values are available. Feed prepared engine rows with the effective **completed-close timestamp**, never the original open timestamp for decision or simulated fill. Check monotonicity and exactly contiguous 86400-second UTC daily opens.
- The first **161** fully completed, contiguous, validated bars are warmup-only and cannot trigger orders (SMA/σ valid at index 99, first full 60-bar count at index 158, record-seeded EMA valid at index 160, plus one bar of `prev` reference). No centered windows, future extrema, negative shifts, incomplete daily bar, full-sample preprocessing or repainting.
- A missing, nonfinite, nonpositive or inconsistent OHLC, absent completed close, timestamp gap, or unsorted bar blocks that bar's decisions **and fill**. Do not synthesize candles or substitute a prior price. Resume decisions only after 161 new contiguous valid completed bars; an existing LONG stays open during the gap, with no fictitious stop/exit or fee. A pending unconfirmed order must be reconciled from its real simulated fill ledger before any further action; never invent completion. Such gaps can prolong unprotected exposure.

## Execution assumptions

**Pinned baseline:** Hummingbot package label `20260920`, `hummingbot/VERSION = dev-2.17.0` (re-fetched and read at pinned commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` this cycle — `VERSION` prints `dev-2.17.0`), pinned `HCH725/hummingbot` source commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This Scout directly fetched and read these pinned files at that commit (not an unpinned online API or current main):

- `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` — `_parse_rest_candles` reads REST `row[0]` as the **open timestamp** (`ensure_timestamp_in_seconds(row[0])`) with OHLC values; `.../constants.py` explicitly supports interval `1d` (`INTERVALS` bidict — re-verified this cycle: `1d` present).
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` — `BacktestingEngineBase.simulate_execution` loops row-wise over timestamped prepared rows (`for i, row in processed_features.iterrows()`), calls `controller.determine_executor_actions()`, and routes each `CreateExecutorAction` to the executor simulator with the forward slice **starting at the current row** (`processed_features.loc[i:max_ts]`); `DEFAULT_TERMINATED_EXECUTORS_WINDOW = 60*60` seconds; `BacktestPositionHold` nets same-pair BUY/SELL average-cost ("Buys and sells of the same asset net out automatically"), realized gross PnL and cumulative quote fees.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` — `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, BUY/SELL, base amount 0.001 fills at the **first supplied row's close** (`fill_timestamp = df['timestamp'].iloc[0]`, `entry_price = close at fill_timestamp`), records `filled_amount_quote = amount * close` and `cum_fees_quote = trade_cost * filled_amount_quote`, then reports `CloseType.POSITION_HOLD`. Together with the current-row forward slice, a completed-close signal at `decision_ts` produces a same-effective-timestamp MARKET-close **simulation** on that prepared row. This is the actual pinned close-effective **backtest** primitive, not an exchange close auction or an intrabar fill. The researcher-defined controller would be a strategy-specific `DirectionalTradingController` emitting these actions; **it is not implemented or deployed**.

**Critical fill/position-state setting:** instantiate `BacktestingEngineBase(terminated_executors_window=None)` so the controller can see fill-confirmed executors on subsequent daily decisions. The pinned default is only 3600 seconds and may hide the previous daily fill from `controller.executors_info`; the engine still has an internal stopped ledger. Maintain explicit controller-side fill-confirmed quantity, pending-action suppression, and position cost/fee ledger; never equate `POSITION_HOLD` with a fresh unfilled order or assume an order was filled when submitted. This model convention does **not** establish causal executable live close fills. A future execution path that cannot honor the same effective-timestamp model must be revalidated as a distinct derivative.

**Cost and capital:** research `initial_quote_cash=10000 USDT`, fixed `amount=0.001 BTC`, `trade_cost=0.001` of quote notional **per simulated BUY and SELL fill**, modeled slippage `0` as an expressly artificial simulation assumption. Do not describe this 0.1% as a measured exchange fee or the zero modeled slippage as realized slippage (the source's own `commission_value=0.075` percent default is superseded by this disclosed house frame). Require sufficient simulated cash including modeled BUY fee; if not, no BUY. SELL only confirmed available base quantity. Unleveraged spot has no perpetual-futures funding contract; **no claim of zero realized futures funding** is made. Actual maker/taker schedules, lot/tick rounding, min notional, spread, latency and partial fills are not verified and are not authorized for Paper/Testnet/Live. Model net realized quote PnL as `BacktestPositionHold.realized_pnl_quote - BacktestPositionHold.cum_fees_quote`, **not** the gross-only executor PnL field. No fabricated prices or fills. Float rounding residuals must not create a second position.

The existing independently reviewed **PR #417** documented the same pinned Binance spot `1d` / MARKET first-close / POSITION_HOLD research primitive (reused here with no novel execution primitive); the wheel-to-commit binary hash was **not revalidated in this Scout cycle**. The package label `20260920` is retained as a policy label only; no package-to-commit byte mapping is invented. Gate 5 relies on the directly inspected pinned code path and the existing reviewed evidence, not a claim of fresh wheel-byte identity or an implemented controller. No futures/margin/shared-capital/new data primitive is needed.

## Evidence

### Source-reported

TradingView `MSH4KJ4x`, JMOZ1337, 2020-05-03: open-source strategy on everget's Stiffness gauge; frozen defaults 100/60/3/90; long entry on `crossover(stiffness, 90)`; long close on `stiffness > 90 and falling(stiffness, 1)`; mirror short leg (explicitly disabled in this derivative); no `strategy.exit`, no stop/target/trailing; `initial_capital=10000`, 100%-of-equity sizing, `commission_value=0.075`. No returns, win-rate, or trade-count figures are claimed from the source page.

### Independently reproduced

**Rule-logic self-check (stdlib only, not a backtest):** the frozen `bound/cnt/stiffness/E[t]/X[t]` arithmetic plus the FLAT/LONG state machine were executed over (a) hand-constructed boundary cases — `close == bound` counts as NOT above (strict `>`), `stiffness == 90` triggers neither leg, entry/exit provably disjoint (`prev<=90` vs `prev>90`); and (b) a 2,830-decision walk over real Binance BTCUSDT `1d` klines (2019-01 → 2026-09, every bar validated finite/positive/consistent, day-step contiguity exact with zero gaps): first full-count stiffness at index 158 as predicted, **8 entries / 95 exit-events with zero same-bar co-fires**, **8 strictly alternating round trips ending FLAT**, hold 6/90/326 bars (min/med/max). Exit-events while FLAT are no-ops by state. EMA seed ablation (first-value vs the independently frozen SMA-of-3) prints **identical event sets**. Population-vs-sample σ and seed choices are therefore non-binding on this sample; the frozen record pins its independently declared numeric semantics regardless. **Engine-code inspection only, not a strategy backtest:** pinned Hummingbot commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3` was read file-by-file for the Binance spot `1d` candle parser (open-timestamp rows), the row-wise engine action loop with current-row forward slices, MARKET-first-row-close fill, quote-notional fee accumulator, POSITION_HOLD ledger, `hummingbot/VERSION` and 3600-second vs `None` terminated-executor visibility; `constants.py` `1d` membership re-verified live this cycle. The candidate's trade events, Pine outputs, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Negative evidence

- Pine revision history beyond the captured render text is unpinned; **source-native/lossless equivalence beyond the captured program text is unverified**. The independent derivative is evaluated against its own frozen rules only. Researcher freezes (short-leg disablement, house sizing/cost, spot frame, 161-bar warmup, exit-before-entry) are disclosed above and change events versus the author's two-sided backtest by construction.
- The four rejected siblings above (Kase Peak, Trendscore, Demand Index, Coral) were read at source and killed for missing/degenerate/crowded rules; none validates this candidate.
- No verified live close fill, partial fill, market impact, exchange fee schedule, futures funding or venue order-size permission. None is silently imputed.

## Deduplication

Main at immutable SHA **8afade7** contained **351** root strategy records; README static count **351**. Working-tree filename/content search for `MSH4KJ4x`, `Ds1akUBu`, `JMOZ1337 stiffness`, and `stiffness` returns zero strategy records built on any Stiffness rule (the single `stiffness` hit is passing prose in the JMOZ-authored RWI record, a different indicator and arithmetic). GitHub title search returns no prior Stiffness candidate. Ten open research/* PRs were checked (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend, #89 Chandelier, #92 SSL channel, #251 Swift 2YMA, #304 forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles KCD) — none carries this primary source or a Stiffness rule.

Nearest neighbors are **not equivalent**: `tradingview-blackcat-tii55-34-cross50-long-flat-…` trades a magnitude ratio `100·Σ(close−SMA)/Σ|close−SMA|` crossing 50 — this record trades a **binary persistence count** against a σ-shifted band with a 90 threshold and a falling-while-elevated exit; `%B`/Bollinger-band records trade continuous band position with no counting; `forven-stddev-cross-swing-…` trades a raw σ cross with no band offset, no count, and no breadth threshold; TII/RSI/Stoch/MACD families trade normalized momentum oscillators, not close-above-band breadth. Different source, different signal construction, different exit book: not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

1. Hand-construct completed daily close paths for `close == bound` boundary, `stiffness == 90` boundary, wrong-side persistence (all-below-band stretches), and inconsistent/nonpositive bars. Verify trigger/no-trigger, strict-`>` exclusivity, and exit-before-entry ordering.
2. Ablate the 0.2 σ offset and the 60-bar count window on predeclared IS/OOS partitions and verify the ablation actually changes entry/round-trip event times; do not tune on OOS.
3. Check warmup bars 1–161, missing/invalid OHLC, nonmonotone/gapped timestamps, FLAT/LONG/pending order transitions, fill-ledger persistence across 86400 seconds, and no same-bar re-entry after a SELL.
4. If formally selected downstream, build the minimal strategy-specific controller/recipe and validate **representative event-level Qlib/Hummingbot parity for this execution primitive** before broad Qlib screening if that primitive has not already been independently validated. Compare timestamp, signal, action, confirmed fill, quantity, fee and position-cost state. A model capability failure is an engineering hold, not a retroactive profitability or admission decision. No performance/Sharpe/OOS claim is made here.

## Crypto portability

Only `BTC-USDT` Binance spot `1d` is pinned in this research record. Other assets, timeframes, market types, and the downstream seven-coin × three-timeframe × leverage/DCA research campaign are **separate experiments**, not HB_READY admission requirements or silently equivalent original source behavior. Applying BO/SO overlays or futures economics changes this frozen trade-event/economic model and requires an explicitly declared derivative.

## Limitations

- An upside-cross can print into a top; without SL/TP/time stop this strategy can hold through substantial adverse moves (observed max hold 326 bars), and the source specifies no protection to remove — exposure control is the rollover exit alone.
- Real-kline evidence shows sparse prints (8 entries over ~7.75 years); long flat stretches and regime-dependent signal droughts are expected, not a malfunction. Sparsity is inherent to the frozen source threshold 90, not a tuned choice.
- The 95 exit-events vs 8 round trips: most exit predicates fire while FLAT and are state no-ops; exit predicates alone do not imply position or turnover.
- The simulated completed-close fill is a **backtest convention**, not a live execution guarantee.
- The modeled 0.1%-per-side research cost, zero modeled slippage, fixed base size and absence of futures funding do not prove actual Binance trade economics. A long position can remain exposed during data outages. No Qlib parity, survivor status or trading approval follows from HB_READY.

## Implementation status

`not-implemented`: no candidate-specific controller, Qlib executable artifact, backtest, deployment, Paper/Testnet/Live run or position exists. The pinned Hummingbot MARKET/POSITION_HOLD **capability** is demonstrated; candidate implementation and reproducible replay remain future downstream work, not a second admission gate.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, subject to an **independent Hermes Auditor GitHub Webhook Review** of this exact PR head. Only that reviewer may remediate source-verifiable facts, exact-head merge on six-gate PASS, or close the Scout PR as NOT_LOSSLESS. No autonomous adoption, order placement, Qlib/Hummingbot execution, or README edit.

## Related Wiki records

None created or modified. Future research may link an existing Hermes Wiki Brain record after independent approval; this PR changes only this one root-level strategy record.

## Sources

1. https://www.tradingview.com/script/MSH4KJ4x-Stiffness-Strategy/ — JMOZ1337, *Stiffness Strategy* (strategy on everget's Stiffness indicator), published 2020-05-03; primary signal/order rules, inspected 2026-10-26.
2. https://www.tradingview.com/script/Ds1akUBu-Stiffness-Indicator/ — everget, *Stiffness Indicator*, original 2018; base gauge construction corroboration.
3. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py — pinned MARKET fill and fee path.
4. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py — pinned row loop, current-row forward slice, position/cost ledger and terminated-executor visibility.
5. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py — pinned Binance spot open-timestamp OHLC parser.
6. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py — pinned `1d` interval (membership re-verified live this cycle).
7. https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION — pinned `dev-2.17.0` (content re-verified live this cycle).
8. https://github.com/HCH725/alpha-strategy-research/pull/417 — previously reviewed package/source identity evidence for the same pinned primitive; **not** a fresh binary hash verification.
