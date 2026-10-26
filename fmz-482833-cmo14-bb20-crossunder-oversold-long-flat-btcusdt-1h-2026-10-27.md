---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FMZ 482833 CMO-BB dual-gate lower-band crossunder, independent BTC-USDT spot 1h long-flat derivative
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-27
sources:
  - https://www.fmz.com/strategy/482833
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CMO(14) / Bollinger(20, 2.0) dual-gate crossunder — independent research derivative

## Provenance

**Primary publication (read 2026-10-27):** FMZ strategy **482833**, *基于动量振荡与布林带的高级量化策略系统 / Advanced Momentum Oscillator and Bollinger Bands Quantitative Strategy System* (page tags `SMA,stdev,CMO,BB`): https://www.fmz.com/strategy/482833. The page HTML (729,409 bytes, fetched 2026-10-27) embeds the complete Pine v5 block (1,864 chars, `/*backtest ... */` header through the `strategy.close("Short")` block). Frozen source facts: `strategy("Chande Momentum Oscillator + Bollinger Bands Strategy", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=10)`; `bbLength=20`, `bbStdDev=2.0`, `basis=ta.sma(close,20)`, `upper/lower=basis±2.0*ta.stdev(close,20)`; `cmoLength=14`, `cmoOverbought=50`, `cmoOversold=-50`, `cmo=ta.cmo(close,14)`; long entry = `ta.crossunder(close, lower) and cmo < cmoOversold` via `strategy.entry("Long", strategy.long)`; short entry = `ta.crossover(close, upper) and cmo > cmoOverbought` via `strategy.entry("Short", strategy.short)`; long exit = `ta.crossover(close, basis) or cmo > cmoOverbought` via `strategy.close("Long")`; short exit = `ta.crossunder(close, basis) or cmo < cmoOversold` via `strategy.close("Short")`. Text census over the pinned code block: 2 `strategy.entry` / 0 `strategy.exit` / 2 `strategy.close` / 0 `strategy.order` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `commission` / 0 `request.*` / 0 `security(` / 0 `volume` / 0 `time(` / 5 `input.*` (all defaults pinned above) / `ta.*` only `sma/stdev/cmo/crossover/crossunder`. The author's demo header (`2d`, `Binance`, `ETH_USDT`, 2024-02-21→2025-02-18) is provenance only, not a binding window. The page JSON embeds the handle `ianzeng123`, but authorship is not independently confirmed, so this record identifies the source by FMZ ID + title + URL only. No license statement was found on the page and none is claimed. No source-native trade equivalence or independently reproduced performance is claimed.

**Independently derived, NOT source-native:** Retain the source's **Bollinger(20, 2.0) bands**, **Pine v5 `ta.cmo(close,14)` semantic**, **±50 CMO gates**, **lower-band crossunder + oversold dual entry**, and **basis-reclaim-or-overbought exit** for the long side. Independently freeze **Binance BTC-USDT spot 1h**, **LONG/FLAT** (source SHORT leg disabled), **0.001 BTC** fixed size, **10,000 USDT** unborrowed initial cash, **100-bar** warmup, **MARKET same-completed-close entry and exit on subsequent bars**, assumed 0.1%-per-filled-side research fees, and explicit failed-fill/data behavior. Source short trades, percent-of-equity sizing, and the 2d ETH demo window are excluded. These researcher choices **materially change trade events and economics**; do not attribute them to the page author or call this a lossless port.

**Frozen identity:** `FMZ:482833:CMO-BB-dual-gate | independent-derived-v1:2026-10-27 | Binance BTC-USDT spot 1h | BB(20,2.0) | LONG iff crossunder(close,lower) and finite-CMO(14)<-50 | exit iff crossover(close,basis) or finite-CMO(14)>+50 | subsequent-bars only | Q=0.001 BTC | MARKET same-completed-close model | fee=0.001 per side`. Any change to lookback, multiplier, CMO length, threshold, direction, exit timing, cost, size, market or order state is a different revision.

**Dedup snapshot:** `main@ef5e870e54d21c669d3dc2dff59b241d13951733` has 367 root strategy Markdown records and README static count 367. Code-search for `482833` and PR search for the FMZ URL returned no match. Ten open `research/*` PRs were inspected for source and rule identity; none uses this FMZ URL or a CMO-plus-Bollinger rule. The nearest admitted CMO records are materially different on at least three axes each: `tradingview-edgetools-cmo9-oversold-time5` uses CMO(9, sum-of-deltas formulation) crossunder(-50) with a 5-bar time exit and no Bollinger gate; `chande-momentum-80-cross-reversal` uses CMO(9) ±80 two-sided reversal with no bands; `vidya-cmo-adaptive-slope-trend` uses VIDYA plus CMO slope, not band-crossunder gating; pure-Bollinger records (`bollinger-band-breakout-long-midline-exit`, `forven-bb-squeeze-breakout`) have no CMO gate and enter on breakouts, not oversold lower-band crossunders. The count match is not represented as an independent 367-file PASS-status audit.

## Economic mechanism

**Source-reported:** a close that crosses under the lower Bollinger Band while the Chande Momentum Oscillator reads below −50 marks a jointly oversold washout; the position is held until price reclaims the Bollinger basis or momentum flips above +50, combining price-channel and momentum-reversal confirmation.

**Research interpretation (hypothesis only):** a completed hourly close printing a fresh lower-band crossunder with deeply negative 14-bar momentum may indicate short-horizon selling exhaustion, with the basis reclaim or momentum flip as the fully specified exit. This is a testable hypothesis, not a return, profitability, source-backtest, Survivor, or Qlib-parity claim. Close-triggered exits can realize substantially worse prices than their threshold during gaps, and this derivative has no stop/target beyond the two signal exits.

## Signal and fully pinned state

**Market/data:** one real Binance spot `BTC-USDT` `1h` OHLCV series; no synthetic/Heikin-Ashi candles, higher timeframe, multi-market data, fitted model, news, order book or funding feed. Let `T[t]` be the Binance **opening** Unix timestamp of bar `t`; bar `t` is usable only after `T[t]+3600 seconds`. All bar timestamps must be exact consecutive 3600-second increments; every O/H/L/C must be finite and positive, `H>=max(O,C)`, `L<=min(O,C)`, volume finite and nonnegative. Missing, duplicated, malformed or incomplete bars **abort the research run**, not forward-fill, drop, or substitute a price.

**Pinned indicator semantics (Pine v5 built-ins, defaults frozen):** `basis[t]=mean(close[t-19..t])`; `sd[t]=sqrt(mean((close-mean)^2))` over the same 20 closes (population form, Pine `ta.stdev` default `biased=true`); `upper[t]=basis[t]+2.0*sd[t]`; `lower[t]=basis[t]-2.0*sd[t]`. `mom[i]=close[i]-close[i-1]`; `up=RMA(max(mom,0),14)`, `dn=RMA(-min(mom,0),14)` with `RMA` the Pine `ta.rma` Wilder smoother seeded by the first 14 values; `cmo[t]=100*(up-dn)/(up+dn)`, or undefined (`na`) when fewer than 15 closes exist or `up+dn==0`. `crossover(a,b)` is true iff `a[t-1]<=b[t-1] and a[t]>b[t]`; `crossunder(a,b)` is true iff `a[t-1]>=b[t-1] and a[t]<b[t]` (prior-bar equality counts as crossed, per Pine built-ins). Any non-finite indicator value forces its predicate false; `na` never enters or exits.

**Warmup/initial state:** require **100 consecutive fully completed valid hourly bars** (first decidable signal needs 21 bars: 20 for bands plus one prior band for the cross; 100 leaves ample RMA-convergence margin), start with `FLAT`, no orders, no position, 10,000 USDT cash and no inferred earlier trade.

**Entry:** on each fully completed bar `t` after warmup, with state FLAT and no pending order, compute bands over closes `t-19..t` and `cmo[t]` as above. BUY if and only if `crossunder(close[t], lower[t]) and isfinite(cmo[t]) and cmo[t] < -50` (strict on both current-bar comparisons, per source `<`). A flat/degenerate 20-bar window (`sd[t]==0`) can never satisfy `close[t]<lower[t]`; an undefined CMO never satisfies the gate (both verified). Issue one MARKET BUY of exactly `Q=Decimal("0.001") BTC` at the same row's observed completed `close[t]` under the pinned **historical simulator convention**. Require `cash >= Q*close[t]*(1+f)`, `f=0.001`; otherwise stay flat. On **confirmed full fill**, record `entryPrice=close[t]` and `LONG`, cash minus `Q*entryPrice*(1+f)`. Do not infer a fill from an order intent. A missing/failed/partial fill, invalid price or undefined fee aborts this bounded research run instead of inventing a trade or retry rule.

**Exit priority:** on each **subsequent** fully completed bar after a confirmed BUY, SELL the entire confirmed Q at that bar's actual completed close if `crossover(close[t], basis[t]) or (isfinite(cmo[t]) and cmo[t] > 50)` (strict on both comparisons, per source `>`/`or`). Both arms trigger the identical full-size SELL, so no priority ordering is needed; entry and exit predicates are mutually exclusive on one close (`close<lower<=basis` contradicts `close>basis`, and `cmo<-50` contradicts `cmo>+50` — verified analytically and over 4,000 fuzz bars with zero co-triggers). No same-entry-bar exit, stop/limit resting order, next-open price assumption, time exit, trailing stop, or fill at the threshold. A full confirmed SELL credits `Q*close[t]*(1-f)` and returns to FLAT. An unresolved SELL or partial fill aborts; no fabricated flat book.

**At most one position.** Opposite (short-side) source signals are disabled in this derivative and never exit or block a LONG; while LONG, new long signals are ignored (source default `pyramiding=0` admits no same-direction add). No pyramiding, averaging, BO/SO/DCA, concurrent positions, cooldown, short, leverage, borrowing, compounding, stop/target, time exit, discretionary override or hidden controller risk default. On the last sample bar, mark any still-open BTC to the **actual last observed close**; do not fabricate a terminal liquidation. All signals are ignored while an order is pending.

## Required data and causality

Exactly one contiguous Binance BTC-USDT **spot 1h** historical OHLCV feed and the opening timestamp of each candle. Bands, RMA-based CMO and cross predicates use only already completed candles; no value is available before its bar's close. At decision time `T[t]+3600`, only `t` and earlier bars are consulted. There are no future extrema, lookahead, negative shifts, incomplete HTF bars, repainting (no `calc_on_every_tick` in source: exactly one evaluation per completed bar), fitted parameters or full-sample normalizations. Any exchange-open timestamp must be mapped to its **completion** time in the model's causal event interpretation.

## Execution assumptions — actual pinned GitHub source inspected

**Baseline:** Hummingbot package **`20260920`**, VERSION **`dev-2.17.0`**, source **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. Prior Alpha PR **#414/#417** documents package/source correspondence and the 1h spot close-MARKET path, reused by sibling admissions **#483** and **#491** for the same market and fill model; no installed wheel/hash or image digest was reverified in this Scout cycle.

- **Real feed and clock:** pinned BinanceSpotCandles `INTERVALS` includes `1h`; `_parse_rest_candles` maps Binance REST `row[0]` to candle **opening timestamp** and `row[1..5]` to real OHLCV. BB(20) SMA/stdev and CMO(14) RMA arithmetic are deterministic researcher-side computations over these existing closes, not a second feed, model inference, or unsupported exchange session API.
- **Real engine and order path:** `BacktestingEngineBase.simulate_execution` iterates prepared historical rows, `update_state(row)` then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction` to `simulate_executor`. `OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A strategy-specific controller is **not yet implemented**; this is a source-demonstrated existing capability path, not a claim of an already runnable strategy.
- **Actual historical fill path:** `OrderExecutorSimulator.simulate` uses the first supplied row's timestamp for MARKET fill, its **actual close** for price, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*Q*close`, and `CloseType.POSITION_HOLD`. `BacktestPositionHold` nets opposite BUY/SELL filled quantities, computes weighted entry and **gross** realized/unrealized quote PnL, and separately accumulates quote fees. The controller must reconcile confirmed fills, not use its action submission as a position update. `terminated_executors_window=None` (or complete persistent confirmed-fill ledger) is required for visibility beyond the default 3600-second terminated-executor window.
- **Fill timestamp distinction:** the simulator labels the row by **opening** timestamp but uses its close. This record's completed-close event/fill **effective economic time** is therefore **open+3600s**; treating the opening label as the instant the close was knowable is a causality error. Same-row close MARKET is an **idealized backtest fill**, not a claim of a live executable post-close order at that exact historic price.
- **Explicit bounded cost model:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% per-filled-side** quote fee, not a verified Binance tariff. Gross matched PnL `Q*(Psell-Pbuy)` is reduced by `0.001*Q*(Pbuy+Psell)` for net matched PnL. Independent 10,000-USDT cash affordability and fee ledger prevent free borrowed spot capital; the engine's position PnL must not be misreported as fee-inclusive. Simulated MARKET close implies **zero modeled slippage only**; observed exchange spread, slippage, fees, partial fills, latency, min notional and actual precision are **unverified**, never silently claimed zero or live-compatible. Spot has **no perpetual funding obligation**; this is not a fabricated zero USDT-M funding observation. No stop/target/time-exit economics exist in this derivative by explicit design (source `strategy.exit` count is 0), not by omission.
- **Failure fences:** `prepare_market_data` may `dropna`; validate the original contiguous candle sequence **before** engine feature dropping. `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` when price is missing; this fallback is **forbidden** as an order price. Abort on absent actual close, broken time sequence, non-finite indicator inputs, or non-full MARKET fill. No maker queue, intrabar stop, next-open fill, cross-market shared capital, leverage/margin, external price or funding model is required by **this derivative**.

## Six-gate assessment (proposal for independent audit)

1. **Deterministic:** BB(20, 2.0) SMA/population-stdev, Pine-`ta.cmo(close,14)` RMA formula, Pine cross boundary semantics, ±50 gates, 100-bar warmup, fixed fees/size, complete state, no fitted model.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; source SHORT leg explicitly disabled, no leverage/borrow.
3. **Entry/exit/risk:** one dual-gate lower-band crossunder BUY; subsequent-bar basis-reclaim-or-overbought SELL; single-position gate; stop/target/trailing/time exits explicitly disabled per source census (0 `strategy.exit`), no invented risk rule.
4. **Position/re-entry:** one full-size confirmed 0.001 BTC unit, one pending order, re-entry only after confirmed FLAT, no DCA/concurrency/pyramiding, no same-bar entry/exit, abort on unsupported failed/partial fills.
5. **Pinned model:** inspected-then-reused 1h Binance spot parser, controller/action loop, MARKET close-fill simulator, POSITION_HOLD net/fee ledger and assumed trade_cost; indicators are close-arithmetic, spot-only, no intrabar path, no invented funding/price or live-fill claim.
6. **Point-in-time:** bands, CMO and crosses available only at bar close, later decisions only after their 1h close, no incomplete candles/future leakage; historical simulator's raw open-time labels explicitly mapped to close-effective times.

## Evidence, limits and next steps

**Source-reported:** FMZ 482833 title/tags, Pine v5, BB(20, 2.0), CMO(14) ±50, lower-band-crossunder-plus-oversold long entry, upper-band-crossover-plus-overbought short entry, basis-or-momentum-flip closes, percent-of-equity sizing, and the 2d Binance ETH_USDT demo header. **Researcher-defined:** every derivative setting, spot/long-flat/fill/fee/cash/warmup/failure detail above. **Independently reproduced:** none; no Pine replay, backtest, Hummingbot/Qlib event-level parity, performance, OOS, Survivor, HB Certified, Paper/Testnet/Live or deployed controller. The six gates assess bounded pinned-engine **expressibility**, not a profitable or already implemented strategy. Before mass Qlib screening, validate any new execution primitive once with representative Hummingbot/Qlib event-level evidence; existing verified close-MARKET primitive may be reused, and final survivor certification requires strategy-specific HB parity.

**Falsification plan (not executed):** compare CMO(14)/±50 versus predeclared alternates on strictly IS data; check equality boundaries (prior-bar equality crossing, strict current-bar gates), a signal on the last sample bar, flat-window silence with `sd==0`, undefined-CMO silence on 0/0 windows, cash shortage, missing-bar abort, stop-gap irrelevance (no stop exists), full-fill confirmations, single-unit re-entry after FLAT, and close-effective timestamp mapping. No profitability or source parity is inferred from a source description.

**Source:** https://www.fmz.com/strategy/482833
**Pinned engine evidence:** https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
**Prior package/source audit:** https://github.com/HCH725/alpha-strategy-research/pull/414
