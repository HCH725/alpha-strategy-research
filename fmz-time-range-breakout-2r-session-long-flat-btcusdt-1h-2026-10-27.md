---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 501678 time-range breakout with opposite-edge stop, 2R target and session-end flatten — BTC-USDT spot 1h long-flat derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - fmz
status: research-only
confidence: medium
source_as_of: 2025-07-16
sources:
  - https://fmz.com/strategy/501678
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ time-range breakout — independent BTC-USDT spot 1h long-flat derivative

## Provenance

**Primary source:** ianzeng123, *Time-Range Breakout Trading Strategy: Automated Momentum Capture System Based on Low Volatility Periods*, public FMZ strategy **501678**, created **2025-07-16**, article text inspected directly **2026-10-27**: https://fmz.com/strategy/501678 . The article explicitly states: range window **19:15–19:30 IST** (highest/lowest recorded); trading session **19:00 IST to 05:30 IST next day**; **long** when price breaks above the range high, **short** when below the range low; long stop at the range low (short stop at the range high); profit target from a customizable risk-reward ratio (**default 2:1**); **one trade per session**; **all positions closed at session end**; variables reset each new session. The article notes breakout trades run on the **15-minute timeframe**. The full Pine source sits behind an FMZ login wall ("Login to view full source") and was **not retrieved**. No claim is made about unseen Pine logic, exact order flags, fill model, or backtest metrics.

**Explicit independent executable derivative v1 — not source-native or lossless.** Researcher-chosen: Binance BTC-USDT **spot UTC 1h**, LONG/FLAT (source short side explicitly disabled: spot has no short leg); range = H/L of the single hourly bar covering the source window; strict close-breakout entry; close-evaluated opposite-edge stop, 2R target and session-end time exit; fixed 0.001 BTC; completed-bar t decision to t+1 **historical modeled close** MARKET fill; 0.1% hypothetical per-side fee; one trade per session; 24-bar warmup. IST (UTC+5:30) maps 19:15–19:30 IST to **13:45–14:00 UTC**, inside the 13:00–14:00 UTC hourly bar; session 19:00 IST–05:30 IST maps to **13:30 UTC–00:00 UTC next day**. Using the full covering bar's H/L, hourly closes instead of 15-minute intrabar breaks, and close-based instead of intrabar stop/target fills are researcher-defined adaptations that can change trade events. Original Pine equivalence is **not** asserted.

**Immutable derivative identity:** FMZ:501678 | ianzeng123 | created:2025-07-16 | derivative-v1:2026-10-27 | Binance BTC-USDT spot UTC1h | range=H/L(d 13:00 UTC bar) | entry C>rangeHigh strict | stop C<rangeLow strict | target fill+2R strict, R=fill-rangeLow | priority stop>target>time | session bars d 14:00–23:00 UTC | time-exit fill at d+1 00:00-bar close | one-trade-per-session | short disabled | fixed 0.001 BTC | warmup24 | modeled fee 0.001/side. A change to any parameter, window mapping, edge, fill timing, market, sizing, or exit creates a new derivative.

**Dedup:** Current main at `d353434dab7e682eaa6d2bd18c770060585cb61d` contains 377 root-level strategy Markdown records; exact searches for `501678`, `time-range breakout`, `19:15-19:30` and `ianzeng123` returned no match, and none of the 10 open research/* PRs (Heracles KCD, ClucMay, AdxSmas, Forven CCI, Swift 2YMA, SSL, Chandelier, SuperTrend, Gauss-StochRSI, Larry-Williams) uses a fixed-clock session window. Nearby breakout records differ materially: dual-thrust (K1/K2 open-range, no clock window, no session flatten), forven-orb-4bar (N-bar trailing), holmberg-orb (normal-tail ORB), nr7 x2 (single-bar narrow range). This candidate's **fixed low-volatility clock window with opposite-edge stop, fixed 2R target, hard session-end flatten and one-trade-per-session reset** is material, not a trivial parameter variant. Do not duplicate it on window tweaks.

## Economic mechanism

### Source-reported

The author describes capturing momentum when the market transitions from a low-volatility consolidation window into higher-activity sessions: a locked range gives objective breakout references, the opposite edge bounds risk, the 2:1 reward ratio systematizes payoff asymmetry, and one-trade-per-session plus session-end flattening prevents overtrading and overnight carry. The article lists unaddressed risks (false breakouts, no regime filter, fixed window, forced session-end closure) without validated performance numbers.

### Research interpretation

This derivative tests whether a fixed-clock low-volatility range Runtime with asymmetric close-based exits (structure stop, 2R target, time flatten) yields a distinct intraday-breakout return distribution after modeled fees. It does **not** claim the source's 15-minute intrabar entries, intrabar stops, short leg, or original market semantics are reproduced.

## Signal

All rules here define the **researcher-authored derivative**, not hidden source facts. Use finite chronological BTC-USDT spot UTC 1h OHLCV with strictly positive O/H/L/C, V>=0, L<=min(O,C)<=max(O,C)<=H, exact opening timestamps `T[t+1]-T[t]=3600` seconds, no gaps/duplicates/incomplete last candle. Reject invalid segments, never interpolate or manufacture prices. Compute in float64 without rounding comparisons; fill/cash/fee ledger uses Decimal.

1. **Session geometry (UTC).** For UTC date d: range bar R(d) opens `d 13:00 UTC` (13:00–14:00, covers source 13:45–14:00 UTC window). Signal bars S(d) open `d 14:00` … `d 23:00 UTC` (10 bars). Permitted fill bars open `d 15:00` … `d+1 00:00 UTC`. RangeHigh(d)=H[R(d)], RangeLow(d)=L[R(d)], locked once R(d) completes.
2. **Session skip.** Skip S(d) entirely (no decisions) when R(d) is missing/invalid or RangeHigh(d)<=RangeLow(d) (zero-width guard). A skipped session sets no traded flag and requires nothing further.
3. **Warmup.** Bars t=0..23 are warmup NO-TRADE (feed-continuity guard). Sessions whose range bar falls in warmup are skipped. First eligible decisions use only completed validated bars.
4. **Entry.** When FLAT, session not traded, no pending order, t strictly after last exit-fill bar, and t in S(d) with d not skipped: breakout B[t] = (C[t] > RangeHigh(d)), strict. If true, schedule exactly one BUY of Q at the actual observed C[t+1], provided t+1 is a permitted fill bar with a valid close; otherwise no order (never fill outside the fill set, never use t+1 inputs in the decision). Do not use t+1 inputs in the decision. Abort on invalid/partial/rejected fill, failed trading-rule validation or insufficient modeled cash; never use synthetic fallback prices.
5. **Risk definition.** On confirmed entry fill at fillP with session range (RH, RL): R = fillP − RL. Target T = fillP + 2R. If R<=0 (filled at/below the stop edge), the stop is deemed immediately breached: schedule one SELL at the next completed-bar actual close after the fill bar (stop-immediate exit), then apply rule 7.
6. **Open-position exits.** While LONG with no pending order, evaluate each completed t after the fill bar with strict comparisons and fixed priority **stop > target > time**: (a) stop: C[t]<RL → SELL next-bar actual close; (b) target: C[t]>T → SELL next-bar actual close; (c) time: t is the `d 23:00 UTC` bar and still LONG → SELL at the `d+1 00:00 UTC` bar actual close (modeled fill effective 01:00 UTC, disclosed lag). Store all simultaneously true reasons in order (a,b,c) for diagnosis; one SELL only, filled only on a valid next bar. No intrabar stop/target, no guaranteed exit price. If the final available bar emits an exit without a next full bar, leave inventory marked but not fictitiously sold.
7. **One-trade-per-session state.** Set traded(d)=true on entry fill. After any exit fill, FLAT with no re-entry for the rest of S(d), even if fresh breakouts print. Ignore entry signals while LONG/pending and ignore repeated exit signals while pending. Never queue them. One pair, one full-sized long, at most one pending order, no short, borrow, leverage, hedging, pyramiding, partial fills, Safety Orders, DCA, rebalancing, cooldown timer or concurrent position. Unbounded downside to zero is a disclosed risk; no hidden protective stop.
8. **Ledger.** Initial cash Decimal("10000") USDT and zero BTC. Fixed filled quantity Q=Decimal("0.001") BTC. Fee f=Decimal("0.001") of fill notional on **each** side; BUY cash -= Q*P*(1+f), inventory += Q; SELL cash += Q*P*(1-f), inventory -= Q. Full-fill round-trip net PnL = Q*(sellP-buyP)-f*Q*(buyP+sellP). Reject cash deficit or amount/min-notional/precision conflicts rather than assuming exchange acceptance. At sample end mark unsold BTC at last actual completed close and report unrealized value separately, no fabricated liquidation/fee. Segment restart resets state and requires full warmup. No compounding, funding, margin or interest: spot has no perpetual funding leg; no imaginary zero-funding observations.

## Required data

Only one real Binance BTC-USDT **spot 1h** historical OHLCV feed, validated as complete and ordered with original exchange candle **open** timestamps; exact 1h UTC boundaries and next close-availability timestamps are mandatory. Range, signal and exit logic consume only <=t completed bars. No order book, non-OHLCV feed, multiple markets, higher-timeframe synchronization or intrabar event reconstruction. A valid historical close is required for every modeled fill. Missing data, invalid precision or an unavailable fill price are blockers, not zero-valued inputs or guessed values.

## Execution assumptions

**Pinned Hummingbot source directly read over HTTPS on 2026-10-27:** `HCH725/hummingbot` commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, repository `hummingbot/VERSION` = **dev-2.17.0**; existing admission package label **20260920**. This run read the three pinned files below in full; it did **not** rehash an installed package or run a backtest.

- **Real data/market path:** pinned `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` bidict includes `1h` (also 15m/30m/4h/1d, unused here). `BacktestingDataProvider.initialize_candles_feed` and `get_candles_df` support a `binance_BTC-USDT_1h` feed. No claim that this run downloaded any BTC candles.
- **Controller/executor path:** pinned `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution="1h",trade_cost=0.001)` loads controller candles at that resolution and iterates rows calling `update_state(row)` then `controller.determine_executor_actions()`, dispatching `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`. A **future minimal candidate-specific controller** must compute the stated session/range/state predicates and delay actions by one completed bar; none has been written. A generic executor name alone does not implement this strategy.
- **Actual simulator primitive (read in full):** `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. In pinned `order_executor_simulator.py`, MARKET fills at the first supplied row's actual `close` (`entry_price=df.close[fill_timestamp]`, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`). This is an **idealized full-fill historical close model**, not a real post-close executable market price, next-open execution, or guaranteed order acceptance. Source intrabar stop-buy entries and intrabar opposite-edge stops are **not** modeled; the derivative's close-based entries/exits exist precisely to stay inside this verified primitive.
- **Timestamp and leakage boundary:** engine row `timestamp` is Binance **opening** time while the row also carries its close; therefore a candidate controller must **only dispatch stored prior t signal on row t+1**, never derive the decision from t+1 close. Record each modeled fill's **effective availability** as t+1 close time (`T[t+1]+3600`), not the engine row timestamp. Validate full contiguous candles and features **before** `prepare_market_data`'s backward merge/dropna to prevent silent missing-bar removal. No same-row re-entry; fills only on permitted fill bars.
- **Ledger/cost path (read in full):** pinned `BacktestPositionHold` (`backtesting_engine_base.py`) nets same-asset buys/sells (`net_amount_base`, average entry, matched realized PnL on reduction, unrealized on remainder) and accumulates `cum_fees_quote` separately. Reconcile net realized PnL, cash and final marked inventory from the complete full-fill ledger; do not call gross PnL fee-net. Connector quantization/trading rules must be checked; exchange min-notional, live slippage, partial fills, spread and real fee tier are **not proven**.
- **Gate 5 scope:** pinned reusable capability covers one Binance spot 1h OHLCV feed, deterministic controller actions, full MARKET historical close fills, fees and position netting. This derivative requires no unverified intrabar, multi-asset, perpetual, non-OHLCV or live execution path. Missing candidate controller is implementation work, not evidence that its code exists. A new execution primitive requires representative validation before mass Qlib screening.

## Evidence

### Source-reported

FMZ strategy 501678 article (ianzheng123, 2025-07-16) specifies the 19:15–19:30 IST range window, 19:00 IST–05:30 IST session, above/below-range long/short entries, opposite-edge stops, default 2:1 risk-reward target, one trade per session, and session-end flattening cited in Provenance. No claimed source win rate, Sharpe, return, commission, fill timing or crypto-market result was reproduced.

### Independently reproduced

**None.** No FMZ replay, Hummingbot/Qlib strategy run, event-level parity, installed-package hash, profitability, OOS, Survivor or HB Certified result. Direct pinned-source **capability inspection only** (three files read in full at the pinned commit).

### Negative evidence

Complete Pine bytes/revision and exact order defaults sit behind the FMZ login wall and were not retrieved; researcher pins of market (BTC-USDT spot), timeframe (1h), UTC window mapping, full-bar range, strict close comparisons, close-based stop/target/time exits, disabled short leg, quantity, fees and warmup are **not** source-native. Source 15-minute intrabar entries/stops, short behavior and original performance cannot be inferred. Historical next-close full fills ignore actual slippage, spread, latency and partial fills; the 00:00-bar time-exit fill lands after the source's session-end definition.

### Six-gate HB_READY proposal (requires independent Hermes Auditor)

1. **Deterministic:** UTC session geometry, full-bar range lock, strict close comparisons, stop>target>time priority, fixed 2R formula, one-trade state machine and warmup pinned.
2. **Direction:** BTC-USDT Binance spot LONG/FLAT; source short leg explicitly disabled with reason (no spot short); no borrow/leverage.
3. **Entry/exit/risk:** exact close-breakout entry and close-evaluated stop/target/time exits with formulas; no SL/TP beyond stated rules; loss-to-zero risk disclosed.
4. **Position/state:** Q=0.001 BTC, cash/fee ledger, full-fill pending order, one position, one trade per session, no DCA/pyramiding/concurrency/cooldown, reset per session.
5. **Pinned engine:** inspected 20260920/dev-2.17.0 source commit in full (spot 1h feed constant, controller/action path, MARKET historical close simulator, fee/POSITION_HOLD netting, timestamp limitations); intrabar modeling explicitly excluded.
6. **Causality:** 24-bar warmup; range locked from completed bar; signal t from <=t, modeled fill t+1 close only after its availability; no future bars, uncompleted candles or early open-timestamp claims.

`hb_ready_status: PASS` is the **Scout's review proposal**, not self-approval; independent exact-head Auditor decides admission.

## Falsification plan

On separately authorized implementation, test UTC/IST mapping, range-bar edge cases (missing bar, zero-width skip), first-breakout-only entry, R<=0 stop-immediate path, stop/target same-bar priority, time-exit fill lag, cash/fees and position netting, data gaps, zero volume, missing-price guard, rejected/partial fill abort, last-bar pending orders, session-boundary fills and final mark. Demonstrate one representative Hummingbot/Qlib event-level parity of the strategy/execution path before large-scale Qlib screening **if** that path introduces an unverified primitive. A failed capability or unexplained event/cost discrepancy blocks downstream use; it does not license invented fills. No backtest is run by Scout.

## Crypto portability

BTC-USDT spot UTC 1h is a research-only derivative choice, not source-proven profitability or an admission whitelist. Other coins, timeframes, futures 3x/5x, BO6/SO6/SO6 or intrabar stops are separately declared execution experiments, never silently overlaid as source-native.

## Limitations

Pine source revision and order defaults are login-walled and unavailable; this is an explicitly independent derived strategy. Fee 0.1% is a hypothetical model assumption, not an asserted Binance tier; no realized funding is claimed. Historical next-close full fills are idealized and not a promise of real tradability; the hourly-bar range is wider than the source 15-minute window and the time-exit fill lags the source session end. No implementation, Qlib parity, survivor qualification, HB certification or trading authorization.

## Implementation status

**not-implemented.** No dedicated candidate controller, Qlib executable recipe, backtest or deployed system is created here. Future selected research may require minimal strategy-specific materialization without a second admission registry.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** Hermes Auditor GitHub Webhook Review alone handles source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. Existing signed GitHub webhook receiver alone handles post-merge README count. Scout does not merge/approve/close, modify main, backtest, trade or change schedules.

## Related Wiki records

None created or modified. No private Wiki or private user data is included.

## Sources

- ianzeng123, *Time-Range Breakout Trading Strategy: Automated Momentum Capture System Based on Low Volatility Periods*, FMZ public strategy 501678, created 2025-07-16, article inspected 2026-10-27: https://fmz.com/strategy/501678
- Pinned Hummingbot commit: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Pinned Binance spot candles: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py
- Pinned backtesting engine: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Pinned order simulator: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
