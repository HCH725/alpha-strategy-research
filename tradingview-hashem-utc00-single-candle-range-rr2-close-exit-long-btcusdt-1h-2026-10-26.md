---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: hashem-trader UTC 00 candle range close-breakout and 2R close-bracket, independent BTC-USDT spot 1h long-flat derivative
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
source_as_of: 2025-10-31
sources:
  - https://www.tradingview.com/script/YJjFy8kD-Candle-Breakout-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# UTC single-candle opening range / 2R close exit — independent research derivative

## Provenance

**Primary publication (read 2026-10-26):** hashem-trader, *Candle Breakout Strategy*, public open-source TradingView strategy, **2025-10-31**, **v1.0 / Pine v5** as explicitly described, stable script ID **YJjFy8kD**: https://www.tradingview.com/script/YJjFy8kD-Candle-Breakout-Strategy/. The first-party page says a user-selected UTC target candle supplies a single high/low range; later closes above its high signal long, below its low signal short; a stop is the opposite range boundary, take-profit is entry plus/minus risk times configurable reward:risk, and the range disarms after an entry until the next target time. It says only one position at once and notes the source example uses 100%-of-equity sizing. The complete Pine source bytes and Pine strategy order-processing settings were **not accessible in the text view**. No Pine hash, source-native trade equivalence, or independently reproduced performance is claimed.

**Independently derived, NOT source-native:** Retain the source's **single UTC-target-candle high/low**, **close-above-range long breakout**, **opposite-boundary risk reference**, **2R target**, and **one-entry-attempt-per-range** mechanism. Independently freeze **Binance BTC-USDT spot 1h**, target **00:00 UTC**, **LONG/FLAT** (source SHORT disabled), **0.001 BTC** fixed size, **10,000 USDT** unborrowed initial cash, **48-bar** warmup, **close-only stop and target checks instead of intrabar/resting stop/TP orders**, next target-candle time exit, no same-bar entry/exit, assumed 0.1%-per-filled-side research fees, and explicit failed-fill/data behavior. Source alerts, chart drawings, 100%-equity sizing, short trades, and any intrabar Pine fills are excluded. These researcher choices **materially change trade events and economics**; do not attribute them to the author or call this a lossless port.

**Frozen identity:** `TV:YJjFy8kD:hashem-trader:2025-10-31:v1.0 | independent-derived-v1:2026-10-26 | Binance BTC-USDT spot UTC1h | anchor=00:00 UTC completed candle | LONG if later close>anchor high | close-stop<=anchor low | close-target>=entry+2*(entry-anchor low) | next-anchor close flatten | one attempt/day | Q=0.001 BTC | MARKET same-completed-close model | fee=0.001 per side`. Any change to anchor clock, threshold, direction, exit timing, cost, size, market or order state is a different revision.

**Dedup snapshot:** `main@ba047d234ac6bf9edce661d4c1fb01df5c1abc3c` has 358 root strategy Markdown records and README static count 358. Connected GitHub code search for `YJjFy8kD` and PR search for the exact ID/author returned no match. Ten open `research/*` PRs were inspected for source and rule identity; none uses this TradingView URL or same UTC single-candle range with close-based 2R/time exits. Nearby admitted `forven-orb-4bar-trailing-breakout` uses a rolling **prior four-bar** high/low, `holmberg-orb-normal-tail-breakout` uses **day-open percent thresholds** and day-end liquidation, and Donchian records use rolling multi-bar channels; none is this **one fixed 00:00 UTC candle, one attempt, opposite-boundary 2R** mechanism. The count match is not represented as an independent 358-file PASS-status audit.

## Economic mechanism

**Research hypothesis only:** a completed UTC midnight-hour candle establishes a fixed daily volatility range. A later confirmed close above its high may indicate persistent intraday buying, with an explicit lower-range close exit, 2R profit exit and next-anchor reset. This is a testable hypothesis, not a return, profitability, source-backtest, Survivor, or Qlib-parity claim. Close-triggered exits can realize substantially worse prices than their threshold during gaps.

## Signal and fully pinned state

**Market/data:** one real Binance spot `BTC-USDT` UTC `1h` OHLCV series; no synthetic/Heikin-Ashi candles, higher timeframe, multi-market data, fitted model, news, order book or funding feed. Let `T[t]` be the Binance **opening** Unix timestamp of bar `t`; bar `t` is usable only after `T[t]+3600 seconds`. All bar timestamps must be exact consecutive 3600-second increments, UTC-aligned; every O/H/L/C must be finite and positive, `H>=max(O,C)`, `L<=min(O,C)`, volume finite and nonnegative. Missing, duplicated, malformed or incomplete bars **abort the research run**, not forward-fill, drop, or substitute a price.

**Warmup/initial state:** require **48 consecutive fully completed valid hourly bars**, start with `FLAT`, no orders, no position, 10,000 USDT cash and no inferred earlier trade. Wait until the **first subsequently completed** bar with opening UTC hour `00`, minute `00`; its actual `H` and `L` become `rangeHigh[D]` and `rangeLow[D]` for UTC date `D`. They are frozen only at **01:00 UTC**, after that candle closes; that target bar is never an entry bar. Reject `rangeHigh<=rangeLow` for that day's setup (remain flat/unarmed); do not fabricate a range.

**Daily arming:** at each valid 00:00-open target candle's **01:00 close**, freeze the new day's high/low and reset that UTC day's entry-attempt counter to zero. If a prior position is still open, the same completed target bar **forces its full close first**, then arms the new day's range only after confirmed SELL. There is no entry on a target candle and no same-bar re-entry. On each other completed UTC-day bar opening at 01:00..23:00, a flat armed state with zero entry attempts may buy if and only if `close[t] > rangeHigh[D]` (strict; equality no trade). This is the **first eligible level observation**, not an inferred intrabar high breakout or a required crossover from below. Consume the day's sole entry attempt on the BUY signal, even if a fill is rejected. A flat day with no signal expires at the next target; no carryover entry intent.

**Entry:** issue one MARKET BUY of exactly `Q=Decimal("0.001") BTC` at the same row's observed completed `close[t]` under the pinned **historical simulator convention**. Require `cash >= Q*close[t]*(1+f)`, `f=0.001`; otherwise stay flat and mark the day's attempt consumed. On **confirmed full fill**, record `entryPrice=close[t]`, `R=entryPrice-rangeLow[D]>0`, `target=entryPrice+2*R`, `stop=rangeLow[D]`, cash minus `Q*entryPrice*(1+f)`, and `LONG`. Do not infer a fill from an order intent. A missing/failed/partial fill, invalid price or undefined fee aborts this bounded research run instead of inventing a trade or retry rule.

**Exit priority:** on each **subsequent** fully completed bar after a confirmed BUY, SELL the entire confirmed Q at that bar's actual completed close if (a) the bar is the next day's 00:00-open target candle (mandatory time exit, highest priority); otherwise if (b) `close[t] <= stop` (strictly a **close-triggered** stop, equality exits); otherwise if (c) `close[t] >= target` (close-triggered 2R target, equality exits). Stop and target are separated by `R>0`, so cannot both trigger at one close. No same-entry-bar exit, intrabar bracket, stop/limit resting order, next-open price assumption or fill at the threshold. A full confirmed SELL credits `Q*close[t]*(1-f)`, returns to FLAT, and **does not** rearm the already-consumed day. An unresolved SELL or partial fill aborts; no fabricated flat book.

**At most one BUY attempt per UTC date.** The next 00:00 target refreshes the range; after a confirmed forced SELL on that target candle, a new day can take its first entry on a later completed candle only. On the last sample bar, mark any still-open BTC to the **actual last observed close**; do not fabricate a terminal liquidation. All signals are ignored while an order is pending. No pyramiding, averaging, BO/SO/DCA, concurrent positions, same-day re-entry, cooldown beyond the daily attempt latch, short, leverage, borrowing, compounding, trailing stop, discretionary override or hidden controller risk default. If there is no completed target candle after warmup, there is no trade.

## Required data and causality

Exactly one contiguous Binance BTC-USDT **spot 1h** historical OHLCV feed and the opening timestamp of each candle. UTC calendar arithmetic and range state use only already completed candles; the anchor high/low are not available until the anchor candle finishes. At decision time `T[t]+3600`, only `t` and earlier bars are consulted. There are no future extrema, pivot confirmations from future bars, lookahead, negative shifts, incomplete HTF bars, repainting, fitted parameters or full-sample normalizations. Any exchange-open timestamp must be mapped to its **completion** time in the model's causal event interpretation.

## Execution assumptions — actual pinned GitHub source inspected

**Baseline:** Hummingbot package **`20260920`**, VERSION **`dev-2.17.0`**, source **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. The connected GitHub app directly read this commit's `hummingbot/VERSION`, `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py`, `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`, `strategy_v2/executors/order_executor/data_types.py`, and `strategy_v2/backtesting/backtesting_data_provider.py` on 2026-10-26. Prior Alpha PR **#414/#417** documents package/source correspondence; no installed wheel/hash or image digest was reverified in this Scout cycle.

- **Real feed and clock:** pinned BinanceSpotCandles `INTERVALS` includes `1h`; `_parse_rest_candles` maps Binance REST `row[0]` to candle **opening timestamp** and `row[1..5]` to real OHLCV. The researcher-defined `00:00 UTC` anchor is a deterministic selection over these existing bars, not a second feed or unsupported exchange session API.
- **Real engine and order path:** `BacktestingEngineBase.simulate_execution` iterates prepared historical rows, `update_state(row)` then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction` to `simulate_executor`. `OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A strategy-specific controller is **not yet implemented**; this is a source-demonstrated existing capability path, not a claim of an already runnable strategy.
- **Actual historical fill path:** `OrderExecutorSimulator.simulate` uses the first supplied row's timestamp for MARKET fill, its **actual close** for price, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*Q*close`, and `CloseType.POSITION_HOLD`. `BacktestPositionHold` nets opposite BUY/SELL filled quantities, computes weighted entry and **gross** realized/unrealized quote PnL, and separately accumulates quote fees. The controller must reconcile confirmed fills, not use its action submission as a position update. `terminated_executors_window=None` (or complete persistent confirmed-fill ledger) is required for visibility beyond the default 3600-second terminated-executor window.
- **Fill timestamp distinction:** the simulator labels the row by **opening** timestamp but uses its close. This record's completed-close event/fill **effective economic time** is therefore **open+3600s**; treating the opening label as the instant the close was knowable is a causality error. Same-row close MARKET is an **idealized backtest fill**, not a claim of a live executable post-close order at that exact historic price.
- **Explicit bounded cost model:** `run_backtesting(trade_cost=0.001)` is a **hypothetical 0.1% per-filled-side** quote fee, not a verified Binance tariff. Gross matched PnL `Q*(Psell-Pbuy)` is reduced by `0.001*Q*(Pbuy+Psell)` for net matched PnL. Independent 10,000-USDT cash affordability and fee ledger prevent free borrowed spot capital; the engine's position PnL must not be misreported as fee-inclusive. Simulated MARKET close implies **zero modeled slippage only**; observed exchange spread, slippage, fees, partial fills, latency, min notional and actual precision are **unverified**, never silently claimed zero or live-compatible. Spot has **no perpetual funding obligation**; this is not a fabricated zero USDT-M funding observation.
- **Failure fences:** `prepare_market_data` may `dropna`; validate the original contiguous candle sequence **before** engine feature dropping. `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")` when price is missing; this fallback is **forbidden** as an order price. Abort on absent actual close, broken time sequence or non-full MARKET fill. No maker queue, intrabar stop, next-open fill, cross-market shared capital, leverage/margin, external price or funding model is required by **this derivative**.

## Six-gate assessment (proposal for independent audit)

1. **Deterministic:** UTC 00:00 one-candle frozen H/L, strict later close breakout, close stop/2R/time exit, 48-bar warmup, fixed fees/size, complete state, no fitted model.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; original SHORT path explicitly disabled, no leverage/borrow.
3. **Entry/exit/risk:** one daily close-above-high BUY, subsequent close-at/below-low or close-at/above-2R SELL, mandatory next-anchor close exit; all other risks explicitly disabled.
4. **Position/re-entry:** one full-size confirmed 0.001 BTC unit, one attempt per UTC day, one pending order, no DCA/concurrency/pyramiding, no same-bar re-entry, abort on unsupported failed/partial fills.
5. **Pinned model:** inspected actual 1h Binance spot parser, controller/action loop, MARKET close-fill simulator, POSITION_HOLD net/fee ledger and assumed trade_cost; spot-only, no intrabar path, no invented funding/price or live-fill claim.
6. **Point-in-time:** anchor available only at 01:00 UTC, later decisions only after their 1h close, no incomplete candles/future leakage; historical simulator's raw open-time labels explicitly mapped to close-effective times.

## Evidence, limits and next steps

**Source-reported:** TradingView author/date/v1.0/Pine v5, UTC selected candle, breakout at later close, opposite-range stop, configurable RR target, one active position, one-shot range, and source example equity sizing. **Researcher-defined:** every derivative setting, clock/exit/fill/fee/cash/failure detail above. **Independently reproduced:** none; no original Pine source replay, backtest, Hummingbot/Qlib event-level parity, performance, OOS, Survivor, HB Certified, Paper/Testnet/Live or deployed controller. The six gates assess bounded pinned-engine **expressibility**, not a profitable or already implemented strategy. Before mass Qlib screening, validate any new execution primitive once with representative Hummingbot/Qlib event-level evidence; existing verified close-MARKET primitive may be reused, and final survivor certification requires strategy-specific HB parity.

**Falsification plan (not executed):** compare UTC 00 anchor versus alternate predeclared anchors on strictly IS data; check equality boundaries, a breakout on the last 23:00-open candle, forced next-target exit, a zero-width anchor, cash shortage, missing 00:00 bar, a stop gap, full-fill confirmations, one attempt/day, and close-effective timestamp mapping. No profitability or source parity is inferred from a source description.

**Source:** https://www.tradingview.com/script/YJjFy8kD-Candle-Breakout-Strategy/
**Pinned engine evidence:** https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
**Prior package/source audit:** https://github.com/HCH725/alpha-strategy-research/pull/414
