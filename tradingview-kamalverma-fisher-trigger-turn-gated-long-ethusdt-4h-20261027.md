---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "kamalverma1207 Fisher trigger-turn with +1 entry/exit gates, ETH-USDT spot 4h long-flat — independent derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-08-04
sources:
  - https://www.tradingview.com/script/oVoigpVw-Fisher-Crossover-Strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fisher trigger-turn, gated at +1 — independent executable research derivative

## Provenance

**TradingView first-party source:** kamalverma1207, *Fisher Crossover Strategy*, stable script ID `oVoigpVw`, public open-source strategy page and release notes dated **2025-08-04**, inspected **2026-10-27**: https://www.tradingview.com/script/oVoigpVw-Fisher-Crossover-Strategy/ . The page says Fisher is compared with its one-bar-lagged Trigger, a long is entered on Fisher crossing **above** Trigger while Fisher is **below 1**, and the long is exited on Fisher crossing **below** Trigger while Fisher is **above 1**. The author describes one trade at a time, candle-close confirmation and INR 20,000 fixed-cash orders. The generic opening paragraph also discusses unfiltered crosses; the **release notes' gated rules** are the source description selected here.

**Source limitations:** The accessible public page text does **not** expose the full Pine bytes, code revision/hash, indicator lookback, price normalization, recursive initialization, exact order-fill convention, fee model, or broker settings. The page's open-source badge is **not** proof that those details were retrieved. No source-native or lossless Pine reconstruction is claimed. No source-reported performance number is independently reproduced.

**Explicitly independent derived strategy:** This record adopts only the publicly stated *Fisher-versus-previous-Fisher turn plus level-1 gates* as an inspiration, then **researcher-defines** every missing decision-critical component: Ehlers-style trailing-HL2 normalization, length 10, 0.33/0.67 and 0.5 recursive coefficients, zero-range rejection, finite seed, exact cross/tie predicates, ETH-USDT spot UTC 4h, 100-bar warmup, delayed next-completed-close historical fills, fixed 0.01 ETH, 10,000 USDT modeled cash, 0.1%/side modeled fee, pending-order and retry state, and explicit absence of SL/TP/DCA. INR 20,000 sizing is **not** carried over; source order timing, fees, and Pine implementation are **not** asserted to match. These choices materially alter signals, trade timing, and economics, so this derivative must never be cited as proof that the author's original strategy is HB_READY.

**Immutable research identity:** `TV:oVoigpVw|kamalverma1207|2025-08-04|independent-v1:2026-10-27|BinanceSpot:ETH-USDT:UTC4h|HL2-10-Ehlers-style-Fisher-recursion-0.33/0.67-0.5|Fisher-vs-Fisher-lag1-turn|BUY-cross-up-and-Fisher<1|SELL-cross-down-and-Fisher>1|warmup100|signal-t-to-close-t+1|0.01ETH|cash10000USDT|fee0.001`. Any change in source lineage, formula, gates, venue, execution clock, state or cost defines a new derivative.

**Dedup:** Connected GitHub `main` snapshot `e287ed4d893e5bdbc6b5b53ec2aaba059bc5510c` (2026-10-27), untruncated recursive tree: 378 root-level strategy Markdown records; README count 378. Exact source ID `oVoigpVw` and author `kamalverma1207` were absent from main code search and open PR search; ten open `research/*` PRs were inspected for source/rules. Closest admitted records: `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` uses a **zero-sign latched, two-sided** Fisher reversal, not the derivative's **lagged-Fisher turn plus asymmetric +1 entry/exit gates, long-flat**; `combo-123-reversal-fisher-transform-two-sided-btcusdt-4h-2026-10-15.md` requires **123-candle/stochastic agreement** and is two-sided; `tradingview-blackcat-inverse-fisher-rsi5-wma9-threshold-long-flat-btcusdt-1d-2026-10-26.md` applies **inverse** Fisher to RSI, not Fisher of HL2. The Fisher-zero record mentions a trigger-cross as a *falsification idea*, not an admitted strategy with this source and level-1 gated exits. No duplicate URL or materially identical admitted/open rules found. Count equality alone is not a census of every historical PASS frontmatter.

## Economic mechanism

**Source-described hypothesis:** A Fisher upswing relative to its own one-bar lag, while the transformed oscillator remains below +1, is a possible bullish reversal; a downswing above +1 signals a later rollover. This may generate few exits and can hold a loss indefinitely; the page's generic advice to use risk management is not an executable stop rule.

**Derived hypothesis:** The same asymmetrically gated turn events on a pinned, deterministic HL2 Fisher oscillator can be researched as a long-only ETH spot regime with no hidden filters. The transform's exact numerical implementation and market transfer are independent research choices, not recovered source Pine facts.

## Signal — fully pinned independent definition

- **Market/data:** one real Binance **spot** `ETH-USDT` 4h OHLCV series, UTC-aligned, sorted by strictly increasing **open** timestamps `T[t]`, exactly 14,400 seconds apart. Require actual finite positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, nonnegative finite volume, unique rows and actual close price. Reject missing/gapped/duplicate/synthetic/forward-filled data; no substituted trade price. Only `H,L` drive the indicator; `C` is used as the modeled fill price.
- **Price:** `P[t]=(H[t]+L[t])/2`. At each completed t >= 9, `lo[t]=min(P[t-9..t])`, `hi[t]=max(P[t-9..t])`. If `hi[t]==lo[t]`, invalidate the research series rather than divide by zero or invent a fallback.
- **Deterministic initialization:** At t=9, set `V[8]=0`, `F[8]=0` as **research-defined** seeds. For every t>=9, `r[t]=(P[t]-lo[t])/(hi[t]-lo[t])`; `V[t]=0.66*(r[t]-0.5)+0.67*V[t-1]`; `W[t]=min(0.999,max(-0.999,V[t]))`; `F[t]=0.5*ln((1+W[t])/(1-W[t]))+0.5*F[t-1]`. Natural log, double precision indicators, unrounded comparisons. This is an explicitly chosen Ehlers-style formula; **not** verified as the author's original Pine implementation.
- **Trigger:** `G[t]=F[t-1]` for t>=10. Exact Pine-like strict cross semantics are **pinned**: `crossUp[t] := F[t]>F[t-1] AND F[t-1]<=F[t-2]`; `crossDown[t] := F[t]<F[t-1] AND F[t-1]>=F[t-2]`. The trigger is a lag, not a moving average. Equality alone does not create a cross.
- **Entry signal:** `crossUp[t] AND F[t]<1.0`. Only while confirmed FLAT, with no pending order, and only after warmup. `F[t]==1.0` fails the strict entry gate.
- **Exit signal:** `crossDown[t] AND F[t]>1.0`. Only while confirmed LONG, with no pending order, and only after warmup. `F[t]==1.0` fails the strict exit gate. If Fisher never makes a downward turn above 1, no exit occurs; loss exposure is unbounded absent a stop.
- **Priority:** evaluate a pending SELL before any BUY; no simultaneous opposing orders or same-bar exit/re-entry. Cross events occurring in an ineligible position/state are ignored rather than queued indefinitely. No initial synthetic entry from a pre-warmup cross.
- **Warmup:** 100 consecutive fully completed 4h bars, indices 0..99, with recursion calculated from t=9. First eligible signal is t=99; first possible modeled fill is t=100. Need >=101 valid consecutive bars for a completed entry. No full-sample extrema, future-bar data, `security` lookahead, fitting, repainting, or incomplete candle.

## Position, risk, and re-entry state

- Start with 10,000 modeled USDT, 0 ETH, FLAT, no pending order. A signal at completed t queues exactly **one** MARKET BUY or SELL for the **next** completed candle t+1. Do not execute a new order on the same bar as its signal.
- Fixed BUY amount `Decimal("0.01")` ETH, contingent on modeled available USDT >= `Q*C[t+1]*(1+0.001)` at the actual next completed close and valid exchange minimum/precision constraints. SELL liquidates the entire confirmed 0.01 ETH (or actual filled balance). No negative spot inventory or borrowing.
- State transitions: `FLAT -> BUY_PENDING -> LONG` only on confirmed full BUY fill; `LONG -> SELL_PENDING -> FLAT` only on confirmed full SELL fill. On rejected/unfilled BUY: clear pending, stay FLAT and require a **fresh** future eligible cross. On rejected/unfilled SELL: remain LONG and retry one MARKET SELL at each subsequent valid completed close until confirmed full fill, without duplicate simultaneous orders.
- A bar executing a pending order is **not** also eligible to initiate a new order; signal events on that fill bar are ignored. After a SELL fill, a new BUY requires a future fresh cross, not a still-true level. If t is the last available bar, any queued action has no fill; cancel the unexecuted pending action and mark held inventory at the last actual close for reporting only, not a synthetic liquidation.
- Historical engine assumes full single-row MARKET fills. If partial fills, fee currency conversion, actual tick/lot/min-notional precision, missing prices, cash shortfall, or ambiguous execution cannot be represented, invalidate/hold the research run instead of manufacturing full fills or zero costs. One market, one position and at most one pending order; no pyramiding, BO/SO/DCA, averaging, cooldown beyond fresh-cross/no-fill-bar-entry, concurrent positions, shared capital, leverage or compounding.
- **Disabled:** SHORT, futures, margin, funding, limit/maker/intrabar/next-open fills, SL, TP, trailing, time-based exit, opposite-signal close without the +1 gate, discretionary exits, partial TP, price-based emergency stop, unannounced controller defaults, and end-of-sample forced liquidation. No stop is an explicit risk limitation.

## Execution assumptions — pinned Hummingbot evidence

**Engine baseline:** Repository contract pins Hummingbot package `20260920`, VERSION `dev-2.17.0`. Connected GitHub inspection of `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` on 2026-10-27 directly read `hummingbot/VERSION` = `dev-2.17.0`; the package/commit byte-equivalence is reported by prior independently reviewed Alpha PR #414 (902/902 wheel bytes), **not rehashed in this Scout cycle**. No later engine version is presumed.

**Actual bounded engine path (not an API-name assumption):**
1. `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` declares the Binance spot `4h` interval; `binance_spot_candles.py::_parse_rest_candles` maps Binance row[0] to **open timestamp** and row[1..5] to OHLCV. The historical feed is `binance` / `ETH-USDT` / `4h`, not a synthetic 4h aggregation or futures mark feed.
2. A **future, not-yet-implemented** minimal ControllerV2/backtesting controller computes the above Fisher series only from completed rows, stores signal t, and on the next completed row emits `CreateExecutorAction(OrderExecutorConfig(connector_name="binance", trading_pair="ETH-USDT", side=BUY/SELL, amount=Decimal("0.01"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1))` with controller-memory pending/fill/cash state. This record does not assert an already-existing strategy-specific controller.
3. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution` calls `determine_executor_actions()`, `simulate_executor()`, and `update_executors_info()`; `order_executor_simulator.py::simulate` selects the first supplied row for MARKET and uses its **actual close** as `entry_price`, calculates `filled_amount_quote=Q*close` and `cum_fees_quote=trade_cost*Q*close`, then reports `CloseType.POSITION_HOLD`. `BacktestPositionHold::_process_order` nets opposite-side base quantity, records weighted average entry, gross realized PnL and separate quote fees. The historical simulator is **not** a live exchange execution guarantee.
4. **Causal timestamp fence:** `T[t]` is candle **OPEN** timestamp. Signal t is knowable only at `D[t]=T[t]+14400` (UTC seconds) after completion. Its delayed MARKET action executes on t+1 row's **actual close**, economically timestamped `D[t+1]`, **never** at the raw `T[t+1]` or before the future close was known. The engine's row timestamp remains open time internally; reporting must remap the modeled decision/fill economic clock, not falsely claim an intrabar fill. This is an idealized historical next-close convention, not a claim of real-world executable next-close liquidity.
5. **Fees and cash:** research-only `trade_cost=0.001` per side on actual simulated quote notional, not a verified Binance account fee tier. Confirmed BUY debits `Q*P_buy*(1+0.001)`; confirmed SELL credits `Q*P_sell*(1-0.001)`. A completed round trip's modeled net quote PnL is `Q*(P_sell-P_buy)-0.001*Q*(P_sell+P_buy)`. `BacktestPositionHold.realized_pnl_quote` is **gross** and `cum_fees_quote` must be deducted separately. Spot perpetual funding is **inapplicable**, not realized zero. Spread, slippage, latency, precision and partial fills are not independently measured and are not silently set to realistic zero.
6. **Known engine traps:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on missing price; explicitly reject that fallback. `BacktestingEngineBase.prepare_market_data` drops NaN rows; validate continuity before any filtering. Default terminated-executor retention can prune old fills; set `terminated_executors_window=None` or preserve the verified fill ledger. Enforce full-fill and spot cash state in the future minimal controller; the simulator's `position_action` field alone does not prove cash constraints.

**Compatibility scope:** Verified for this **bounded single-pair Binance spot 4h, completed-row MARKET close-fill, quote-fee and position-hold accounting model**, subject to the stated controller implementation and data-validation obligations. No proof of source-native Pine parity, live fills, multi-asset portfolio behavior, futures economics, or Qlib strategy-specific parity. No Qlib/Hummingbot backtest was run.

## Evidence, negative evidence, and falsification

- **Gate 1 — deterministic:** pinned 10-bar HL2 min/max, 0.33/0.67 recurrence, 0.5 Fisher recursion, clamp, seed, double precision, trigger lag, strict crossing/threshold/tie logic; no fitted model.
- **Gate 2 — direction:** Binance spot LONG/FLAT only; short, borrowing, leverage and derivatives disabled.
- **Gate 3 — entries/exits/risk:** separate below-1 upward Fisher-turn entry and above-1 downward Fisher-turn exit, delayed historical MARKET close fills; SL/TP/trailing/time exits explicitly absent, unbounded adverse exposure disclosed.
- **Gate 4 — state:** exact fixed quantity/cash/fee, single position and pending action, full-fill confirmation, failure/retry rules, fresh-cross re-entry, no DCA/pyramiding/concurrency.
- **Gate 5 — real pinned model:** package/version/source pin; Binance 4h OHLCV parser; actual backtesting controller action loop, MARKET close fill, quote-fee and POSITION_HOLD accounting paths read; spot funding inapplicable; no fabricated missing prices, live fill or precision claim.
- **Gate 6 — causality:** 100 completed-bar warmup, no future extrema, signal at D[t] and modeled fill at D[t+1], with explicit raw-open-timestamp hazard and continuity rejection.

**Independent audit is required.** Frontmatter PASS is a **Scout proposal**, not self-approval, implemented software, historical profitability, Survivor status, Qlib parity, Paper/Testnet/Live authorization, or proof of the original author's Pine strategy. A future executable path must undergo representative Qlib/Hummingbot event-level parity before large-scale Qlib screening if it introduces a previously unverified primitive.

**Negative evidence:** No retrieved original Pine bytes or hash; no claim that the original Fisher formula equals this derivative; no source proof of source-native order timing/fees or INR-to-USDT equivalence; no guaranteed stop or forced profit; no fabricated source/backtest performance. The published source's threshold-1 turn gates distinguish this from the already admitted Fisher zero-sign and 123/Fisher-combo systems.

**Falsification plan (downstream only, not executed here):** freeze the above identity and compare the gated turn rule against (a) ungated Fisher/lag cross, (b) zero-sign Fisher regime, and (c) randomized turn timing, all with the same declared execution/cost model and OOS isolation. These are future distinct research hypotheses, not hidden changes to this admitted candidate.
