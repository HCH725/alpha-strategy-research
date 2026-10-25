---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: melkani log-weighted five-MA relative-strength sign cross - independent BTC-USDT spot 1d long-flat derivative
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
source_as_of: 2024-12-29
sources:
  - https://www.tradingview.com/script/QSirInj3-Relative-Strength/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# melkani log-weighted five-MA relative-strength sign cross — independent BTC-USDT spot daily derivative

## Provenance

**Primary public source:** TradingView script **QSirInj3**, *Relative Strength*, author **melkani**, first published **2024-12-23**, updated **2024-12-29** (release note: "Strategy to Indicator"); public description inspected **2026-10-26**: https://www.tradingview.com/script/QSirInj3-Relative-Strength/ . The current page calls the work open-source and retains historical strategy/backtesting prose, but the 2024-12-29 change means it must **not** be represented as a verified current executable Pine strategy. The complete Pine source bytes, code revision/hash and actual default inputs are not accessible in the inspected readable page. No source-native, lossless, or original-Pine HB_READY claim is made.

**Source-reported facts only:** the author describes a custom strength function measuring percentage deviations from short EMA and longer SMA references over periods **8, 34, 20, 50, 200**, combining them by logarithmic weights that emphasize shorter periods. The description associates positive/negative strength transitions with buy/sell and optionally displays BTC, ETH and equity-index comparisons. It does not publish the exact five component assignments, logarithm formula, EMA seed, threshold equality, execution clock, actual trading side, fill/cost model, sizing or position/risk defaults in the readable text.

**Independently specified derivative (not attributed to original Pine):** researcher chooses EMA8 and EMA34, SMA20/SMA50/SMA200, a precise logarithmic weighting, BTC-USDT Binance **spot 1d UTC**, single-market close-only inputs, zero-cross LONG/FLAT signals, **next completed daily close** MARKET fills, 0.001 BTC per trade, 0.1% modeled fee each side, finite warmup, explicit order/position state and no protective stop or short. The source's optional cross-market visual comparisons and backtest date filter are **disabled**, not assumed necessary to the core price-strength mechanism. All choices are research-designed and may materially alter source trade events.

**Frozen derivative identity:** `TV:QSirInj3:melkani:published-2024-12-23:updated-2024-12-29 | independent-derived-v1 | EMA8/34 seeded in trailing-250; SMA20/50/200; w(n)=ln(1+200/n); score=weighted-percent-deviation | zero-sign-cross LONG/FLAT | signal-at-UTC-daily-close; MARKET-fill-next-UTC-daily-close | BinanceSpot:BTC-USDT:1d:0.001BTC:cash10000USDT:fee0.001/side | 2026-10-26`. Altering any formula, lookback, seed, fill clock, sizing, market, costs or state is a different derivative.

**Dedup at main `b885c7ee7e752ebb347ee3abe1f9793a2de23359`:** the untruncated recursive Git tree contained **339** root-level strategy Markdown records; README static count **339**. GitHub main code search found no `QSirInj3`, and GitHub PR search found no `QSirInj3` or titled `Relative Strength` PR. Ten open `research/*` PR titles were checked: none concerned this source or the five-reference log-weighted price-deviation sign transition. The nearest generic moving-average/crossover records trade individual MA rails/crosses, not a logarithmically weighted five-MA **normalized deviation aggregate**. This is a distinct signal construction, not a trivial length change. Numeric agreement alone is not an independent re-audit of all 339 prior PASS frontmatters.

## Economic mechanism

### Source-reported

An aggregate of percentage distances from multiple trend baselines attempts to measure the underlying instrument's directional strength across horizons. The author describes positive/negative transitions as trading signals; no independently reproduced performance is available.

### Research interpretation

A weighted consensus of deviations from two fast exponential and three simple trend anchors seeks persistent multi-horizon trend strength. A turn from nonpositive to positive opens a single long; a turn from nonnegative to negative exits. Log weights deliberately favor shorter baselines, making the composite different from a simple SMA/EMA cross. Sideways choppiness and fee drag can invalidate the hypothesis.

## Signal

**Data:** one real, consecutive Binance BTC-USDT spot **UTC 1d** OHLCV stream. Each row's exchange timestamp `T[t]` is its UTC **opening** time; its OHLCV and signal become available only after **`T[t]+86400` seconds**. Validate consecutive exactly-86400-second opens, finite strictly positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, and finite nonnegative volume. A missing, duplicate, incomplete or malformed row aborts the research run; never fabricate/forward-fill a price or silently skip rows.

**Fully specified rolling EMA construction:** For each completed bar `t` with 250 consecutive valid closes `C[t-249..t]`, recompute EMA8 and EMA34 on **that exact trailing 250-close window**. For EMA of length `n in {8,34}`, seed at window position `n-1` with the arithmetic mean of the window's first `n` closes; for each later window position `j`, `EMA_n[j] = (2/(n+1))*C[j] + (1-2/(n+1))*EMA_n[j-1]`. The final EMA is the value at `t`. This fixed-window re-seeding is a deliberate researcher choice, not a claim about the original script or an infinite-history EMA. SMA20, SMA50 and SMA200 are arithmetic means of the final 20, 50 and 200 closes ending at `t`. No external symbol, intraday sample, fit, volatility normalization, ML model, shifted future bar or additional filter.

**Score:** for `n in {8,20,34,50,200}`, assign `M_8=EMA8, M_34=EMA34, M_20=SMA20, M_50=SMA50, M_200=SMA200`. Define `d_n[t] = 100*(C[t]-M_n[t])/M_n[t]`, `w_n = ln(1+200/n)` (natural log), and `S[t] = sum_n(w_n*d_n[t])/sum_n(w_n)`. All five denominators must be finite and strictly positive; otherwise fail the run, never substitute a previous score or zero. There is no rounding before comparison.

**Warmup:** first permitted signal decision is at completed bar index `t=250` (zero-based), requiring **251 consecutive validated candles**, so both `S[t-1]` and `S[t]` each have a full independent trailing-250 window. Initialize at the start of the tape with 10,000 USDT cash, 0 BTC, no prior position and no pending order. No inference of a pre-warmup holding.

**Decision conditions (strict):** `Enter[t] = (S[t-1] <= 0 AND S[t] > 0)`; `Exit[t] = (S[t-1] >= 0 AND S[t] < 0)`. Exactly zero does not itself trigger an order. Entry is eligible only while confirmed FLAT; exit only while confirmed LONG. On a decision at the **completed close of t**, schedule exactly one corresponding MARKET action for the **next completed daily close, t+1**; the next bar's price is **not known or used at t**. At t+1, process the scheduled action before any new signal: submit a BUY or SELL, model a fill at **observed C[t+1]**, and ignore t+1's score for a new decision. Resume score-cross evaluation no earlier than completed t+2. This deliberately delayed-close execution is an independent research convention, **not** original Pine order timing or a claim that a live market order can fill at the closing print.

**State and order priority:** `FLAT -> pending BUY -> confirmed LONG -> pending SELL -> FLAT`. One unresolved order at a time; no entry during LONG, no reversal/short, no exit-and-reentry on one bar. A BUY is 0.001 BTC only when confirmed free cash covers `0.001*C[t+1]*(1+0.001)`; otherwise reject that signal and remain FLAT, with no automatic retry until a **new later cross**. A SELL is exactly the confirmed held base quantity; do not treat order submission as a fill. MARKET backtest path models immediate full fills; any missing fill/partial fill or inconsistent position reconciliation is a **run failure**, not a fabricated completion. A failed SELL retains LONG and is retried on the next completed valid daily bar until resolved, without evaluating new entries. A rejected BUY clears pending and requires a new later cross. No separate cooldown beyond waiting for a new cross after a confirmed exit. Cash/position is never inferred from a signal alone.

**Explicitly disabled:** SHORT, leverage, margin, perpetual funding, DCA/BO/SO, pyramiding, partial profit-taking, shared multi-asset capital, discretionary trading, stop-loss, take-profit, trailing stop, fixed holding time, intrabar triggers, maker/limit/next-open orders, compounding, forced end-of-sample liquidation, source's optional cross-market comparison plots, hidden Hummingbot risk defaults and any source-claimed backtest date window. An open position at the sample end is marked only at the actual last valid observed close; no imaginary exit fill. **No protective stop exists.**

## Required data

One 1d Binance **spot** BTC-USDT historical OHLCV feed with genuine exchange opening timestamps and 251 fully completed contiguous daily bars before the first decision. Only close enters the composite; O/H/L/V validate row integrity. No order book, futures mark/funding, external indices, other coin feed, cross-asset synchronization, higher/lower timeframe, fitted model or future price. The first observed tape date, OHLCV bytes, UTC calendar and cost parameters must be frozen in downstream replay metadata; a changed data snapshot is not an identical replay.

## Execution assumptions

**Pinned benchmark:** repository contract Hummingbot package **20260920**, `hummingbot/VERSION=dev-2.17.0`, source **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Read-only GitHub source inspection this cycle verified the VERSION file and the following exact paths on that commit: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (1d supported), `.../binance_spot_candles/binance_spot_candles.py` (REST kline row[0] open timestamp; row[1..5] OHLCV), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`, `.../executors_simulator/order_executor_simulator.py`, `.../backtesting_data_provider.py`, and `hummingbot/strategy_v2/executors/order_executor/data_types.py`. Earlier independent Alpha PR **#414** reports **902/902 wheel byte-identity verification** and 33-assert representative engine validation; that package/source hash was **not independently rerun this cycle**. No dedicated strategy controller exists yet.

**Actual bounded engine path:** `BacktestingEngineBase.simulate_execution` updates a controller from processed historical rows, takes `CreateExecutorAction` and dispatches `OrderExecutorConfig` to `OrderExecutorSimulator`. For `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `amount=Decimal("0.001")`, `leverage=1`, `price=None`, the MARKET simulator fills the **first supplied historical row's actual close**, sets quote notional `Q*close`, books `trade_cost*notional` quote fees and yields `POSITION_HOLD`. `BacktestPositionHold` nets opposite-side base quantity, tracks weighted average entry and aggregates gross realized PnL and fees separately. This is the **spot, full-fill, idealized completed-close** research subset only; neither API availability nor an executor name alone is asserted as compatibility.

**Mandatory causal clock fence:** raw Binance candle timestamps and the engine's simulated executor timestamps are **bar opens**, even though the engine consumes that row's close. The declared strategy evaluates `S[t]` only at **`T[t]+86400`** and places the resulting action on row `t+1`, whose effective model fill time is **`T[t+1]+86400`**. Any controller/Replay must enforce the one-bar signal shift and record/compare these **effective close times**; interpreting raw open-time engine events as real-time decisions or pretending a live market fill occurred at the historical close would violate Gates 5/6. This is an idealized historical research model, not an execution-ready controller.

**Fees and accounting:** explicitly run with `trade_cost=0.001` per fully filled side (**research assumption** of 0.1% of quote notional, not a verified Binance fee schedule). Starting unborrowed cash 10,000 USDT; on confirmed BUY at observed `P`, cash decreases by `Q*P*(1+0.001)`; on confirmed SELL, cash increases by `Q*P*(1-0.001)`. Net round-trip cash PnL = `Q*(Psell-Pbuy)-0.001*Q*(Pbuy+Psell)`; the engine's gross position PnL and separately recorded fees must not be conflated. Open inventory equity = cash plus held BTC times an **observed** valid close. No perpetual funding leg on spot (**not applicable**, not fabricated zero futures funding); no borrow interest or leverage. MARKET simulator has no separate spread/slippage/latency/partial-fill realism; zero simulated slippage is **not** evidence of zero real slippage. Real exchange fee tier, tick/step/min-notional constraints and live fills remain unverified and cannot be claimed.

**Failure safeguards:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` when missing: **forbid this fallback** and abort on missing real prices. `prepare_market_data` drops NaN rows: validate all consecutive raw candles **before** invoking it, never let gaps disappear. Specify `terminated_executors_window=None` or a persistent full-run confirmed-fill ledger so a prior fill cannot disappear from controller memory; update position state only from actual confirmed `POSITION_HOLD` executor results, not action intent. If the later materialization cannot implement these exact safeguards and shifted clock, hold that execution path for engineering proof rather than asserting it was tested.

## Evidence

### Source-reported

melkani's TradingView page QSirInj3 (published 2024-12-23; updated 2024-12-29) describes the five lookbacks, mixed EMA/SMA normalized strength, logarithmic weighting and positive/negative buy/sell transitions. Its update note explicitly says "Strategy to Indicator". No performance claim is independently reproduced.

### Independently reproduced

**No strategy backtest or trade-event reproduction was performed.** This Scout directly inspected the named immutable Hummingbot GitHub source files for actual spot 1d data parsing, MARKET close fill, quote fee, position holding, controller action loop and timestamp caveat. Prior package-byte verification is cited as earlier independent evidence, not freshly repeated. The exact derived composite and next-completed-close order convention are research specifications, not tested implementations.

### Negative evidence

Readable TradingView source omits complete Pine bytes and exact weighting/EMA seed/side/fill settings; the derived choices are fully disclosed rather than misrepresented as author defaults. The 2024-12-29 indicator conversion prevents a claim that the latest page is a verified executable strategy. Missing actual prices, incomplete daily bars, an uncorrected open-time event clock, untracked fees, partial fills or unverified futures/maker paths are **not** covered by this proposal. README 339/root 339 agreement does not prove each preexisting PASS record was re-audited this cycle.

**Six-gate Scout proposal (independent Auditor decides):** (1) five explicit MA algorithms, 250-window seed, logarithmic weights, exact cross/equality/priority; (2) BTC-USDT spot LONG/FLAT, SHORT disabled; (3) sign-exit and every disabled risk leg declared; (4) single 0.001 BTC position, no DCA/concurrency, scheduled action, fill/failure/re-entry state; (5) immutable pinned 1d spot feed, controller action, MARKET/POSITION_HOLD/cost path and explicit effective-clock/economic limitations; (6) 251 completed-bar warmup, backward-only rolling indicators, prior-bar signal executed no earlier than next completed close, no future leakage.

## Falsification plan

After independent admission and separate downstream selection, test hand-computed 251-bar score/equality cases, moving 250-window EMA seed, zero-price/data-gap aborts, next-bar action timing, ignored pending-bar signals, rejected BUY, failed SELL retry, full-fill reconciliation, cash/fee/equity and raw-open vs effective-close timestamps. Compare representative Hummingbot/Qlib event-level parity **before mass screening if this execution path introduces an unverified primitive**; otherwise reuse previously verified engine capabilities. Only later research/OOS assesses profitability, not this HB_READY admission.

## Crypto portability

Frozen derivative is **only** Binance BTC-USDT spot 1d. Single-pair, 1d, OHLCV and completed-close are research choices, **not** reinstated policy bans. Seven-coin/three-timeframe, BO/SO 6/6/6, 3x/5x futures and funding are optional downstream experiments; any material change is a separately disclosed execution derivative with its own engine/economic evidence.

## Limitations

No full Pine hash or source-native parity; exact source defaults unavailable; explicit 2024-12-29 indicator conversion; no freshly repeated package wheel digest; no strategy controller, replay, Hummingbot/Qlib backtest, realized fees/slippage, exchange precision/min-notional verification or live-close fill guarantee. The absence of a protective stop exposes the strategy to substantial drawdown. A future execution implementation must satisfy the declared causal clock, full-fill and cash/fee ledger constraints; otherwise it is an engineering hold, not proof of executable deployment. PASS is a **Scout-proposed bounded model compatibility status**, pending independent Auditor review, not profitability or trading authorization.

## Implementation status

**not-implemented**: no dedicated controller, Qlib executable recipe, tests, trading environment or deployment was created. Later materialization is separate from the six-gate admission status.

## Adoption boundary

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** Only independent Hermes Auditor GitHub Webhook Review may remediate source-verifiable facts, merge an exact-head six-gate PASS or close a NOT_LOSSLESS Scout PR. Scout does not approve, merge, close, edit README, run backtests or trade.

## Related Wiki records

None asserted; no Wiki modifications.

## Sources

- Primary: melkani, *Relative Strength*, TradingView QSirInj3, published 2024-12-23, updated 2024-12-29: https://www.tradingview.com/script/QSirInj3-Relative-Strength/
- Pinned engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Earlier independent pinned wheel/source and representative engine validation: https://github.com/HCH725/alpha-strategy-research/pull/414
- Current admission contract: https://github.com/HCH725/alpha-strategy-research/blob/b885c7ee7e752ebb347ee3abe1f9793a2de23359/.github/HB_READY_REVIEW.md
