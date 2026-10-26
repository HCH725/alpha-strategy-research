---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: felipemiransan price-action 16-bar rolling-extreme pattern bracket, independent BTC-USDT spot 1h long-flat derivative
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-26
sources:
  - https://www.fmz.com/strategy/473937
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Rolling 16-bar extreme / reversal-pattern bracket — independent research derivative

## Provenance

**Primary publication (read 2026-10-26):** FMZ strategy **473937**, *动态支阻价格行为交易系统* (keywords `SR,PA`), public Pine v5 strategy `strategy("Price Action Strategy", overlay=true)` under **Mozilla Public License 2.0, © felipemiransan**: https://www.fmz.com/strategy/473937. The page HTML (725,585 bytes, fetched 2026-10-26) embeds the complete Pine block (4,269 chars, backtest header through `plot(resistance, ...)`). Frozen source facts: `length=16` rolling support `ta.lowest(low, 16)` / resistance `ta.highest(high, 16)`; `sensitivity=0.018`; long entry = (`isHammer()` or `isDoji()` or `isPinBar()`) and `close <= support * 1.018`; short entry = (`isShootingStar()` or `isDoji()` or `isPinBar()`) and `close >= resistance * 0.982`; entries gated by `strategy.opentrades == 0`; exits only via `strategy.exit` with `stop` at ±16% and `limit` at ±9.5% of average price. Text census over the pinned code block: 2 `strategy.entry` / 2 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `commission` / 0 `default_qty_*` / 0 `request.*` / 0 `security(` / 0 `volume` / 0 `time(` / 0 division except constant `/100` scaling. The author's demo header (`1h`, `Futures_Binance`, `BTC_USDT`, 2024-11-26→12-03) is provenance only, not a binding window. No Pine hash, source-native trade equivalence, or independently reproduced performance is claimed.

**Independently derived, NOT source-native:** Retain the source's **16-bar rolling support**, **1.018 entry zone**, **exact Hammer/Doji/PinBar formulas**, **16% stop / 9.5% target bracket**, and **single-position gate**. Independently freeze **Binance BTC-USDT spot 1h**, **LONG/FLAT** (source SHORT leg disabled), **0.001 BTC** fixed size, **10,000 USDT** unborrowed initial cash, **48-bar** warmup, **MARKET same-completed-close entry**, **close-only stop/target checks on subsequent bars instead of intrabar resting stop/limit orders**, no same-bar entry/exit, assumed 0.1%-per-filled-side research fees, and explicit failed-fill/data behavior. Source short trades, intrabar Pine fills, labels/drawings, and the one-week demo window are excluded. These researcher choices **materially change trade events and economics**; do not attribute them to the author or call this a lossless port.

**Frozen identity:** `FMZ:473937:felipemiransan:MPL-2.0 | independent-derived-v1:2026-10-26 | Binance BTC-USDT spot 1h | support=lowest(low,16) | LONG if (Hammer|Doji|PinBar) and close<=support*1.018 | close-stop<=0.84*entry | close-target>=1.095*entry | subsequent-bars only | Q=0.001 BTC | MARKET same-completed-close model | fee=0.001 per side`. Any change to lookback, sensitivity, pattern, threshold, direction, exit timing, cost, size, market or order state is a different revision.

**Dedup snapshot:** `main@578d536d5b94f4d8c8d0171bf3973a87841899aa` has 364 root strategy Markdown records and README static count 364. Code-search for `473937`/`felipemiransan`/`Price Action Strategy` and PR search for the FMZ URL returned no match. Ten open `research/*` PRs were inspected for source and rule identity; none uses this FMZ URL or a rolling-extreme plus candle-pattern bracket. Nearby admitted records are materially different: `forven-engulfing-body-cover-volume` and `dual-ema-engulfing-volume` use engulfing bodies (not hammer/doji/pinbar at rolling extremes), `tradingview-dipalishah94-morning-evening-star-ratio` uses star-pattern ratios, `williams-fractal-ema-band-fixed-rr` uses fractal plus EMA band, `support-resistance-fractal-trailing-breakout` uses fractal breakout plus trailing exits, `forven-pivot-s1-bounce-r1-exit` uses floor pivots, and `fmz-gbs-top-bottom-confirmed-breakout` uses confirmed-level breakout. The count match is not represented as an independent 364-file PASS-status audit.

## Economic mechanism

**Source-reported:** a 16-bar rolling lowest-low support with a 1.8% tolerance band plus a Hammer/Doji/PinBar reversal print marks a potential bounce level; a fixed 16% stop and 9.5% target bracket the risk.

**Research interpretation (hypothesis only):** a completed hourly close inside the tolerance band above a 16-bar extreme, printed with downside-rejection geometry, may indicate short-horizon buying absorption, with an explicit close-triggered stop and target. This is a testable hypothesis, not a return, profitability, source-backtest, Survivor, or Qlib-parity claim. Close-triggered exits can realize substantially worse prices than their threshold during gaps.

## Signal and fully pinned state

**Market/data:** one real Binance spot `BTC-USDT` `1h` OHLCV series; no synthetic/Heikin-Ashi candles, higher timeframe, multi-market data, fitted model, news, order book or funding feed. Let `T[t]` be the Binance **opening** Unix timestamp of bar `t`; bar `t` is usable only after `T[t]+3600 seconds`. All bar timestamps must be exact consecutive 3600-second increments; every O/H/L/C must be finite and positive, `H>=max(O,C)`, `L<=min(O,C)`, volume finite and nonnegative. Missing, duplicated, malformed or incomplete bars **abort the research run**, not forward-fill, drop, or substitute a price.

**Warmup/initial state:** require **48 consecutive fully completed valid hourly bars** (longest source lookback is 16; 48 leaves ample margin), start with `FLAT`, no orders, no position, 10,000 USDT cash and no inferred earlier trade.

**Entry:** on each fully completed bar `t` after warmup, with state FLAT and no pending order, compute `support[t]=lowest(low,16)` over bars `t-15..t` (current completed bar included, final at close) and the exact source pattern predicates (`body=close-open`, `range=high-low`, `lower=open-low`, `upper=high-close`; Hammer: `body>0 and lower>body*2 and upper<body*0.5 and range>0`; Doji: `abs(body)<range*0.1`; PinBar: `(upper>body*2 and lower<body*0.5) or (lower>body*2 and upper<body*0.5)`). BUY if and only if `(Hammer or Doji or PinBar) and close[t] <= support[t]*1.018` (equality enters, per source `<=`). A zero-range bar satisfies no predicate (verified: all-false, no division anywhere). Issue one MARKET BUY of exactly `Q=Decimal("0.001") BTC` at the same row's observed completed `close[t]` under the pinned **historical simulator convention**. Require `cash >= Q*close[t]*(1+f)`, `f=0.001`; otherwise stay flat. On **confirmed full fill**, record `entryPrice=close[t]`, `stop=0.84*entryPrice`, `target=1.095*entryPrice`, cash minus `Q*entryPrice*(1+f)`, and `LONG`. Do not infer a fill from an order intent. A missing/failed/partial fill, invalid price or undefined fee aborts this bounded research run instead of inventing a trade or retry rule.

**Exit priority:** on each **subsequent** fully completed bar after a confirmed BUY, SELL the entire confirmed Q at that bar's actual completed close if (a) `close[t] <= stop` (strictly a **close-triggered** stop, equality exits); otherwise if (b) `close[t] >= target` (close-triggered target, equality exits). `0.84*entry < 1.095*entry` always, so (a) and (b) cannot both trigger at one close (verified over representative closes). No same-entry-bar exit, intrabar bracket, stop/limit resting order, next-open price assumption or fill at the threshold. A full confirmed SELL credits `Q*close[t]*(1-f)` and returns to FLAT. An unresolved SELL or partial fill aborts; no fabricated flat book.

**At most one position.** Opposite (short-side) source signals are disabled in this derivative and never exit or block a LONG; while LONG, new long signals are ignored (source `opentrades==0` gate). No pyramiding, averaging, BO/SO/DCA, concurrent positions, cooldown, short, leverage, borrowing, compounding, trailing stop, time exit, discretionary override or hidden controller risk default. On the last sample bar, mark any still-open BTC to the **actual last observed close**; do not fabricate a terminal liquidation. All signals are ignored while an order is pending.

## Required data and causality

Exactly one contiguous Binance BTC-USDT **spot 1h** historical OHLCV feed and the opening timestamp of each candle. Support extremes and pattern predicates use only already completed candles; no value is available before its bar's close. At decision time `T[t]+3600`, only `t` and earlier bars are consulted. There are no future extrema, pivot confirmations from future bars, lookahead, negative shifts, incomplete HTF bars, repainting (`calc_on_every_tick` unset in source: exactly one evaluation per completed bar), fitted parameters or full-sample normalizations. Any exchange-open timestamp must be mapped to its **completion** time in the model's causal event interpretation.

## Execution assumptions — actual pinned GitHub source inspected

**Baseline:** Hummingbot package **`20260920`**, VERSION **`dev-2.17.0`**, source **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. Prior Alpha PR **#414/#417** documents package/source correspondence and the 1h spot close-MARKET path, reused by sibling admission **#483** for the same market and fill model; no installed wheel/hash or image digest was reverified in this Scout cycle.

- **Real feed and clock:** pinned BinanceSpotCandles `INTERVALS` includes `1h`; `_parse_rest_candles` maps Binance REST `row[0]` to candle **opening timestamp** and `row[1..5]` to real OHLCV. The 16-bar rolling extreme is a deterministic selection over these existing bars, not a second feed or unsupported exchange session API.
- **Real engine and order path:** `BacktestingEngineBase.simulate_execution` iterates prepared historical rows, `update_state(row)` then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction` to `simulate_executor`. `OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A strategy-specific controller is **not yet implemented**; this is a source-demonstrated existing capability path, not a claim of an already runnable strategy.
- **Actual historical fill path:** `OrderExecutorSimulator.simulate` uses the first supplied row's timestamp for MARKET fill, its **actual close** for price, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*Q*close`, and `CloseType.POSITION_HOLD`. `BacktestPositionHold` nets opposite BUY/SELL filled quantities, computes weighted entry and **gross** realized/unrealized quote PnL, and separately accumulates quote fees. The controller must reconcile confirmed fills, not use its action submission as a position update. `terminated_executors_window=None` (or complete persistent confirmed-fill ledger) is required for visibility beyond the default 3600-second terminated-executor window.
- **Fill timestamp distinction:** the simulator labels the row by **opening** timestamp but uses its close. This record's completed-close event/fill **effective economic time** is therefore **open+3600s**; treating the opening label as the instant the close was knowable is a causality error. Same-row close MARKET is an **idealized backtest fill**, not a claim of a live executable post-close order at that exact historic price.
- **Explicit bounded cost model:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% per-filled-side** quote fee, not a verified Binance tariff. Gross matched PnL `Q*(Psell-Pbuy)` is reduced by `0.001*Q*(Pbuy+Psell)` for net matched PnL. Independent 10,000-USDT cash affordability and fee ledger prevent free borrowed spot capital; the engine's position PnL must not be misreported as fee-inclusive. Simulated MARKET close implies **zero modeled slippage only**; observed exchange spread, slippage, fees, partial fills, latency, min notional and actual precision are **unverified**, never silently claimed zero or live-compatible. Spot has **no perpetual funding obligation**; this is not a fabricated zero USDT-M funding observation.
- **Failure fences:** `prepare_market_data` may `dropna`; validate the original contiguous candle sequence **before** engine feature dropping. `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` when price is missing; this fallback is **forbidden** as an order price. Abort on absent actual close, broken time sequence or non-full MARKET fill. No maker queue, intrabar stop, next-open fill, cross-market shared capital, leverage/margin, external price or funding model is required by **this derivative**.

## Six-gate assessment (proposal for independent audit)

1. **Deterministic:** 16-bar rolling support, 1.018 zone, exact Hammer/Doji/PinBar inequalities, 0.84/1.095 close bracket, 48-bar warmup, fixed fees/size, complete state, no fitted model.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; source SHORT leg explicitly disabled, no leverage/borrow.
3. **Entry/exit/risk:** one close-zone pattern BUY, subsequent close-at/below-stop or close-at/above-target SELL; single-position gate; all other risks explicitly disabled, no invented time exit.
4. **Position/re-entry:** one full-size confirmed 0.001 BTC unit, one pending order, re-entry only after confirmed FLAT, no DCA/concurrency/pyramiding, no same-bar entry/exit, abort on unsupported failed/partial fills.
5. **Pinned model:** inspected-then-reused 1h Binance spot parser, controller/action loop, MARKET close-fill simulator, POSITION_HOLD net/fee ledger and assumed trade_cost; spot-only, no intrabar path, no invented funding/price or live-fill claim.
6. **Point-in-time:** extremes and patterns available only at bar close, later decisions only after their 1h close, no incomplete candles/future leakage; historical simulator's raw open-time labels explicitly mapped to close-effective times.

## Evidence, limits and next steps

**Source-reported:** FMZ 473937 title/keywords, MPL-2.0 © felipemiransan, Pine v5, 16-bar extremes, 1.8% sensitivity, four pattern formulas, 16%/9.5% bracket, single-position gate, and the 1h Futures_Binance BTC_USDT demo header. **Researcher-defined:** every derivative setting, spot/long-flat/fill/fee/cash/failure detail above. **Independently reproduced:** none; no Pine replay, backtest, Hummingbot/Qlib event-level parity, performance, OOS, Survivor, HB Certified, Paper/Testnet/Live or deployed controller. The six gates assess bounded pinned-engine **expressibility**, not a profitable or already implemented strategy. Before mass Qlib screening, validate any new execution primitive once with representative Hummingbot/Qlib event-level evidence; existing verified close-MARKET primitive may be reused, and final survivor certification requires strategy-specific HB parity.

**Falsification plan (not executed):** compare sensitivity 1.018 versus predeclared alternates on strictly IS data; check equality boundaries (zone/stop/target), a signal on the last sample bar, zero-range-bar silence, cash shortage, missing-bar abort, a stop gap through 0.84*entry, full-fill confirmations, single-unit re-entry after FLAT, and close-effective timestamp mapping. No profitability or source parity is inferred from a source description.

**Source:** https://www.fmz.com/strategy/473937
**Pinned engine evidence:** https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
**Prior package/source audit:** https://github.com/HCH725/alpha-strategy-research/pull/414
