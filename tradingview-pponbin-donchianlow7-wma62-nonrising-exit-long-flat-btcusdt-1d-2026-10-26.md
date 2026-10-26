---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: PPonBIN Donchian-low 7 / WMA62 crossover with nonrising-WMA exit, independent BTC-USDT spot 1d long-flat derivative
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
source_as_of: 2025-06-08
sources:
  - https://www.tradingview.com/script/nns2oNG1-Donchian-x-WMA-Crossover-2025-Only-Adjustable-TP-Real-OHLC/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PPonBIN Donchian-low / WMA cross — independently derived BTC-USDT spot long-flat strategy

## Provenance

**Primary TradingView source:** PPonBIN, *Donchian x WMA Crossover (2025 Only, Adjustable TP, Real OHLC)*, published **2025-06-08**, stable public script ID **nns2oNG1**, directly inspected **2026-10-26**: https://www.tradingview.com/script/nns2oNG1-Donchian-x-WMA-Crossover-2025-Only-Adjustable-TP-Real-OHLC/ . The first-party public description states a LONG entry on `ta.crossover(ta.lowest(low, 7), ta.wma(close, 62))`; a cross-down exit when that WMA is not rising; an optional 1% take-profit; a 2025-only calendar restriction; real rather than Heikin-Ashi OHLC; 100% equity sizing, no pyramiding and an initial AUD 1,000 account. The source is presented as an open-source script, but the complete Pine source bytes and revision-specific TradingView order settings were **not** retrieved; this is not a source-native trade-reproduction claim.

**Explicit independent derivative, NOT lossless source Pine:** This candidate retains the source-described **Donchian-low 7 crossing WMA62** entry and **cross-down with nonrising WMA** exit, but deliberately changes the author's ASX/2025/equity-funded configuration to **Binance BTC-USDT spot, UTC 1d, all available dates, LONG/FLAT, 0.001 BTC fixed quantity, 10,000 USDT initial unborrowed cash**. It **disables** the source's optional take-profit and calendar cutoff, defines strict crossover equality, a 100-bar warmup, a completed-close historical MARKET simulation, hypothetical 0.1% per-side cost, exit-first confirmed-fill order state, and no stops or other orders. Each is a researcher-authored alteration, not a fact about the original Pine defaults. Removing TP/calendar and changing the market can materially change trades; the source's performance is not transferred or claimed.

**Immutable candidate identity:** `TV:nns2oNG1:PPonBIN:2025-06-08 | derived-v1:2026-10-26 | L7=min(low,t-6..t), WMA62=weighted-close | CROSSUP ENTER, CROSSDOWN AND WMA_NONRISING EXIT | Binance:BTC-USDT:spot:UTC1d:LONG-FLAT:0.001BTC | historical-completed-close-MARKET | fee=0.001`. A change to signals, warmup, market, timing, cost, order state, TP, or date filter is a different research revision.

**Dedup checked on immutable main `a7f8a584bbe02ba7b6851b0d8e043285dada2978`:** 356 root-level strategy Markdown records; README static counter 356. GitHub code searches for `nns2oNG1` and `PPonBIN` returned no main match; all 11 open `research/*` PR source summaries and titles were checked and none references this URL or rule. The closest main families (Donchian 20/10 raw-price breakout, Eterna Donchian 20/1 midline, Forven Donchian regimes, and WMA/OTT or WMA/trend-confluence strategies) use raw extrema, regime flips, or price/MA crossings. This candidate specifically compares the **rolling seven-low series itself** to a **62-bar linearly weighted close**, with a **nonrising-WMA exit gate**. That event mechanism is not a mere length variant of a price/Donchian breakout or price/WMA cross. No exact or materially identical record was found; count agreement alone is not claimed as a full historical frontmatter audit.

## Economic mechanism

**Source-described hypothesis:** A recent-low channel crossing above a weighted price trend line marks a trend recovery; its downward recross while WMA momentum is flat/negative ends the trade. **Derived BTC hypothesis (unverified):** a strengthening seven-day low relative to the 62-day weighted close may select persistent trend recoveries rather than raw new-high breakouts. Exit requires both the downside cross and a nonrising WMA, so losses can be substantial while that conjunction is absent. No profitability, original-source parity, or Hummingbot/Qlib backtest result is asserted.

## Signal

**Single-market data:** real Binance spot `BTC-USDT`, UTC `1d` consecutive historical OHLCV candles. Bar `t` has exchange **open timestamp** `T[t]` and only becomes completed/decision-eligible at `T[t]+86400` seconds. Require `T[t]-T[t-1]=86400`, finite positive O/H/L/C, `H>=max(O,C)`, `L<=min(O,C)`, finite `V>=0`. Never use Heikin-Ashi/synthetic values, forward-filled or future candles. Any missing/duplicate/invalid/incomplete required bar **aborts the research run** before engine `dropna`; no invented price.

**Frozen arithmetic:** for `t>=6`, `L7[t]=min(L[t-6],...,L[t])`, **including** the completed current bar. For `t>=61`, `WMA62[t] = (sum(k=0..61, (62-k)*C[t-k])) / 1953` (newest close weight 62; oldest weight 1; 1953=62*63/2). No smoothing beyond this WMA, no future bar, no indicator fit or normalization. All calculations use the unrounded source OHLCV values; exchange precision is not invented.

**Entry event:** `crossUp[t] := (L7[t-1] <= WMA62[t-1]) AND (L7[t] > WMA62[t])`. The equality on the previous bar is permitted; the current inequality is strict.

**Exit event:** `crossDown[t] := (L7[t-1] >= WMA62[t-1]) AND (L7[t] < WMA62[t])`; `nonRising[t] := WMA62[t] <= WMA62[t-1]`; `EXIT[t] := crossDown[t] AND nonRising[t]`. Nonrising includes equality, as a researcher-defined interpretation of the source's "not rising." There is **no** unconditional exit on price below WMA, no stop, no TP and no end-of-year forced sale. Do not treat `L7` as `close` or `highest`.

**Warmup and causality:** first 100 **consecutive fully completed valid UTC daily candles** are required; the first eligible decision is index 99 (zero-based), where both current and previous WMA62 are already defined. Begin FLAT, zero BTC, 10,000 USDT, no inferred prehistory position and no pending order. Evaluate exactly once after each completed bar, using only `t` and earlier data. No incomplete bar, future extrema, lookahead, negative shift, repainting, or full-sample fit.

**Deterministic state machine and order precedence:**
1. States `FLAT`, `LONG`, or `ORDER_PENDING` with side and prior confirmed holdings recorded. At most one order exists. Reconcile **confirmed** simulated executor fill/failed status before any new action. Order intent alone never changes position or cash; unresolved/partial fill aborts as outside the bounded model, rather than assuming a price or quantity.
2. When confirmed LONG, if a prior exit SELL failed, retry a SELL of the **entire confirmed BTC quantity** on the next valid completed bar regardless of whether the original exit condition persists. Otherwise if `EXIT[t]` is true, issue exactly one SELL. A LONG ignores all new entry signals. SELL has precedence over any entry; no same-bar re-entry.
3. When confirmed FLAT with no pending order and `crossUp[t]` true, require cash `>= 0.001*C[t]*(1+0.001)`, then issue exactly one BUY of 0.001 BTC. If insufficient cash, remain FLAT and **do not** carry a pending entry; only a fresh later crossUp can enter. A failed BUY leaves FLAT, with no retry except a fresh later crossUp. No intrabar retries.
4. A full confirmed BUY deducts `Q*Pbuy*(1+f)` from cash and sets LONG; a full confirmed SELL credits `Q*Psell*(1-f)` and sets FLAT, where `Q=0.001 BTC`, `f=0.001`, and `P` is the observed historical completed close. A failed SELL leaves LONG and sets the retry flag. No fractional position, pyramiding, safety order, averaging, cooldown, simultaneous exposure, compounding, dynamic sizing, or partial TP.
5. If no event, HOLD. On the final observed bar, value a remaining LONG at the **actual last completed close**, with no fabricated terminal sale. No stop-loss, take-profit, trailing, time exit, date restriction, SHORT, leverage, futures, funding, margin, maker, limit, next-open, intrabar order, cross-market dependency, or hidden controller default.

## Required data

Exactly one spot BTC-USDT real OHLCV `1d` stream, including the **low** over the last seven completed bars and **close** over the last 63 completed bars for current and previous WMA. No multi-timeframe feed, external fundamentals, order book, funding, mark-price, ML model, or future value. Single-pair/1d/OHLCV are deliberate derivative choices, **not** HB_READY eligibility restrictions.

## Execution assumptions — pinned Hummingbot source directly read this cycle

**Baseline:** Hummingbot package `20260920`, VERSION `dev-2.17.0`; pinned source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. This cycle read the pinned source through the GitHub app; earlier Alpha PR #414/#417 contain package/source mapping evidence. The wheel-to-source binary hash was **not** independently rechecked this cycle, and no installed runtime was inspected.

**Data path:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly maps `1d`; `binance_spot_candles.py::_parse_rest_candles` maps exchange row[0] open timestamp and row[1..5] OHLCV. The candidate requires **real** Binance spot prices, not Heikin-Ashi conversion or a synthetic TradingView feed.

**Engine/control path:** `strategy_v2/backtesting/backtesting_engine_base.py::run_backtesting` → `simulate_execution` calls `prepare_market_data`, `update_state(row)`, then `controller.determine_executor_actions()` and `simulate_executor`. `strategy_v2/executors/order_executor/data_types.py::OrderExecutorConfig` exposes `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `position_action=OPEN/CLOSE`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A **strategy-specific controller is not implemented**; this is a source-verified model path, not a claim that a runnable strategy already exists.

**Fill path:** `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py::simulate` uses the **first supplied historical row's actual close** for a MARKET fill, `filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*notional`, `CloseType.POSITION_HOLD`. The `BacktestPositionHold` class in `backtesting_engine_base.py` matches opposite BUY/SELL fills, keeps weighted average cost, **gross** realized/unrealized PnL and **separate** fees. Independent unborrowed cash checks above prevent synthetic borrowing; do **not** equate gross `realized_pnl_quote` to net returns. Net matched PnL is `Q*(Psell-Pbuy)-f*Q*(Pbuy+Psell)`.

**Timestamp/fill boundary:** The source feed labels a candle at **open time** `T`, but its close is only knowable at `T+86400`. The bounded historical simulator's same-row MARKET-at-close convention must be **economically labeled at completion `T+86400`** and is explicitly an idealized **backtest convention**; a real post-close order cannot be promised that historical close price. A strategy-specific controller must not execute based on an incomplete candle or use `T` as an executable signal timestamp. No live/next-open/maker/intrabar fill compatibility is claimed.

**Fees and negative evidence:** `run_backtesting(trade_cost=0.001)` is a **research assumption**, 0.1% quote notional on both sides, **not** measured Binance commissions. Real fees, spread, slippage, latency, min notional, quantity precision, partial fills and actual fill prices are unverified; they are **not** silently assumed to be realized zero. Spot funding is **not applicable**, not a fabricated zero perpetual funding observation. `prepare_market_data` calls `dropna`, so independently prevalidate candle continuity; `BacktestingDataProvider.get_price_by_type` can fall back to `Decimal("1")`, which this strategy **must never** use as an order price. Abort if observed price is missing. The engine's default terminated-executor view lasts **3600 simulated seconds**; require `terminated_executors_window=None` or an equivalent complete confirmed-fill ledger to avoid losing cross-day order state. The controller must reconcile actual filled status, not equate action creation to a fill.

## Evidence / six-gate review matrix

1. **Gate 1 — deterministic:** fully pinned inclusive seven-low, linearly weighted 62-close formula and denominator, cross inequalities, WMA slope equality, one-pass bar clock, warmup, order priority and failure states. The choices are labeled derived where the full Pine cannot be inspected.
2. **Gate 2 — direction:** real Binance spot LONG/FLAT; SHORT and leverage explicitly disabled.
3. **Gate 3 — entries/exits/risk:** entry is low7 cross above WMA62; exit requires low7 cross below AND WMA nonrising; optional source TP, calendar exit, all other stops/targets/trailing/time limits and hidden defaults explicitly disabled.
4. **Gate 4 — position/reentry:** fixed 0.001 BTC, one position/order, independent cash budget, no DCA/BO/SO/pyramiding, no cooldown, confirmed-fill-only transitions, SELL retry, BUY failure behavior, no same-bar reentry.
5. **Gate 5 — real pinned model:** inspected `1d` Binance spot feed/parser, backtesting controller/executor dispatch, MARKET historical-close fill, POSITION_HOLD inventory/cost accounting and explicit fee parameter. Unverified exchange execution/precision/slippage is excluded from this bounded historical claim; missing-price fallbacks prohibited.
6. **Gate 6 — causality:** only contiguous completed `t` and earlier candles, 100-bar warmup, strict UTC daily availability at `T+86400`, no future data, and explicit simulation-versus-live fill timing.

**Source-reported:** PPonBIN's public description supplies the Donchian-low/WMA crossover idea, seven/62 inputs, cross-down with WMA not rising, optional 1% TP and calendar-2025 behavior. No source backtest numbers are reproduced.

**Independently reproduced:** The listed **pinned Hummingbot source-code paths were inspected**, but **no Pine byte-level reproduction, strategy backtest, Qlib/Hummingbot event-level parity, fee-tier validation, Sharpe/ROI/survivor status or executable-controller test** was performed. A future implementation must validate the declared controller and bounded fill/accounting semantics; a new unverified engine capability requires one representative event-level parity test before mass screening. Independent Hermes Auditor may reject any unsupported material assumption.

## Falsification plan

After independent admission and formal downstream selection, test equality on previous/current cross bars, WMA flat versus rising, simultaneous opposite state, long without a stop, 100th-bar warmup, seven-low inclusive indexing, WMA62 weight orientation, missing/duplicate UTC day, missing price fallback, last-bar open position, insufficient quote cash, failed BUY and failed/retried SELL, confirmed fill lag, fee separation, and exchange-open timestamp versus completed-bar economic timestamp. Validate a genuinely new execution primitive once at representative Qlib/Hummingbot event level before large-scale screening; profitability and OOS are separate from HB_READY.

## Limitations and adoption boundary

This **independent BTC spot derivative** is not the author's ASX/2025/TP/equity-sized Pine strategy. The original Pine bytes and native fill conventions are unavailable. The 2025-only restriction and optional TP are intentionally removed, and a fixed 0.001 BTC size is substituted. No deployed controller, paper/testnet/live authorization, actual fees/slippage/partial-fill support, backtest results, Qlib parity, or survivor certification is claimed. Same-completed-close historical fill is a model assumption, not executable live pricing. The exit-only risk regime can retain a losing position for long periods.

**status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only.** `hb_ready_status: PASS` is the Scout's evidence-backed **admission proposal**, pending independent Hermes Auditor GitHub Webhook Review. Only that independent reviewer may remediate verifiable source facts, accept the exact-head PASS merge or close as NOT_LOSSLESS. No README change, merge, deployment or trading action is authorized by this record.

## Sources

- PPonBIN, *Donchian x WMA Crossover (2025 Only, Adjustable TP, Real OHLC)*, TradingView script ID `nns2oNG1`, **2025-06-08**: https://www.tradingview.com/script/nns2oNG1-Donchian-x-WMA-Crossover-2025-Only-Adjustable-TP-Real-OHLC/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Earlier independent package/source mapping: https://github.com/HCH725/alpha-strategy-research/pull/414 and https://github.com/HCH725/alpha-strategy-research/pull/417
