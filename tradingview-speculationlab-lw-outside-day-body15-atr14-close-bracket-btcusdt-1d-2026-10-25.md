---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "SpeculationLab LW Outside Day — body-filtered bearish outside-bar long, ATR close bracket (independent BTC-USDT spot 1d derivative)"
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-25
sources:
  - https://www.tradingview.com/script/X4ulJUXd/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SpeculationLab LW Outside Day — independently specified close-bracket spot long

## Provenance

**Primary TradingView source:** [LW Outside Day Strategy [SpeculationLab]](https://www.tradingview.com/script/X4ulJUXd/) by **SpeculationLab**, published **2025-10-11**, public open-source TradingView **strategy**, stable script ID **X4ulJUXd**, descriptive primary page inspected **2026-10-25**. Its public description says an outside bar has current high above previous high AND current low below previous low; it filters for a sufficiently large candle body; a close **below the previous low** is its **buy** setup, whereas a close above the previous high is its sell setup. The author describes optional previous-extreme, ATR and fixed-pip stop modes; opposite-swing, risk/reward (default 2:1) and following-open exit modes; a 10%-of-equity default position risk, 0.1% commission and 2 ticks of slippage. The text specifies confirmed bars. Full executable Pine, exact body-size threshold, exact ATR smoothing and precise original order/fill priority were not independently retrievable. Do **not** claim source-native or lossless reproduction.

**Researcher-defined independent derivative:** The following complete executable rule is **not the author's backtest**. We retain the author's distinctive bearish outside-bar **long** trigger but independently freeze a 1.5-times-prior-body filter (author threshold unavailable), Binance BTC-USDT spot 1d, long/flat only (short disabled), Wilder ATR(14), 1.5 ATR initial stop distance and 2R target, both triggered **only by completed closes**, fixed 0.001 BTC, one unit maximum, no pyramiding/DCA, 30-bar warmup, modeled same-close MARKET fills, 10,000 USDT starting quote cash and explicit research fees. This replaces the author's configurable intrabar/following-open exit modes, 10%-equity sizing and 2-tick slippage assumption. Those changes materially alter trade events; the source's original strategy does **not** inherit this derivative's proposed HB_READY status.

**Frozen identity:** TV:X4ulJUXd:SpeculationLab:public-asof-20261025:derived-v1:outsidebar-strict:bearclose-below-prevlow:body-ge-1p5-prev:WilderATR14:stop1p5ATR:target3ATR:close-only:longflat:BTC-USDT:Binance-spot:1d:MARKET-close:0p001BTC. A later change to the public page is not incorporated without a separately versioned record.

**Dedup:** Checked main SHA 815d33dbbfd3d1209310acb252e07401c71602a0 (331 root-level strategy records, README counter 331) and current open research/* PRs (#353, #350, #331, #304, #251, #92, #89, #63, #49, #48). GitHub code search and PR search for exact script ID X4ulJUXd returned no match. Nearby main records have different mechanisms: the wick-reversal hammer/shooting-star record uses 15-bar price context, wick geometry and higher-low confirmation; the inside-bar failure-fade record requires an inside bar and one-sided failed breakout; the 1-3-1 reversal record uses a red anchor plus three green bars. None requires **both** strict outside-bar extremes, a below-previous-low close, the 1.5x body gate and a frozen close-only ATR bracket. This is not a parameter-only duplicate.

## Economic mechanism

The author's outside-day setup interprets a full-range expansion closing below the preceding low as a potential long reversal despite the bearish close. The derivative tests whether that event, filtered by a larger candle body, subsequently reverts enough to reach a fixed ATR-derived profit threshold before a close-based loss threshold. This is a research hypothesis, **not** an established profitable pattern. Because the buy occurs after a bearish close and the stop is checked only at later closes, large adverse intrabar and gap moves remain unprotected.

## Signal — frozen executable specification (Gate 1)

**Data and market:** one Binance BTC-USDT spot 1d UTC OHLCV candle sequence. All OHLC must be finite, positive and internally consistent; volume must be finite and nonnegative. No indicators from other assets, lower timeframes, external feeds or future bars. Zero-based bar index t; all predicates are evaluated only after bar t has fully closed. Strict comparisons unless explicitly marked otherwise.

**Outside-bar source feature, evaluated at completed t >= 1:**

    outside[t] = (high[t] > high[t-1]) AND (low[t] < low[t-1])
    bearishClose[t] = close[t] < low[t-1]

**Derived body filter (not source-authored numeric value):**

    body[t] = abs(close[t] - open[t])
    bodyGate[t] = (body[t] > 0) AND (body[t] >= 1.5 * body[t-1])

The preceding body's zero value does not trigger division by zero: a positive current body passes that component; the full outside/close tests must still pass. An equal 1.5 ratio passes, while equality to the preceding high/low or close-to-low does not. No bullish/green-bar requirement is added: the author explicitly describes the buy as a close **below** the prior low.

**Wilder ATR(14), defined without library ambiguity:**

    TR[t] = max(high[t]-low[t], abs(high[t]-close[t-1]), abs(low[t]-close[t-1])) for t>=1
    ATR14[14] = (TR[1]+...+TR[14])/14
    ATR14[t] = (13*ATR14[t-1]+TR[t])/14 for t>14

No ATR exists before t=14; invalid/nonpositive ATR fails closed. No adjusted candles, alternate RMA seed, exponential 2/(n+1) convention, full-sample fitting, ML or repainting.

**Warmup:** consume and validate first 30 complete candles t=0..29 without any orders; start FLAT, no inherited inventory or standing orders. First possible entry is completed bar t=30. No artificial prehistory or indicator backfill.

**Entry:** When FLAT, not in-flight, and t>=30, if outside[t] AND bearishClose[t] AND bodyGate[t] AND ATR14[t]>0, request one BUY for exactly 0.001 BTC at that completed bar's modeled MARKET-close fill. Freeze the **actual simulated fill price** P and entry-bar ATR A (not a future ATR). On confirmed fill only, set stop=P-1.5*A and target=P+3*A (2:1 reward/risk); reject a nonpositive stop or nonfinite threshold. If no fill, remain FLAT and discard the signal, with no pending order.

**Exit:** While LONG, on each subsequent fully completed bar t>entry_bar, evaluate (in this order) (1) close[t] <= frozen stop, (2) otherwise close[t] >= frozen target; on either, request a single full 0.001 BTC MARKET SELL at that bar's modeled close. The same completed close cannot meet both bounds because target>stop. A stop/target breach by intrabar high/low **alone** never triggers an order. The author's opposite outside-bar sell signal is **not** used as a separate exit; original previous-swing, fixed-pip and following-open modes are disabled. If neither condition holds, carry LONG without time limit or trailing update.

**State and precedence (Gate 4):** FLAT / BUY_IN_FLIGHT / LONG / SELL_IN_FLIGHT. The state changes to LONG or FLAT only on the corresponding confirmed fill. Exactly one order can be in flight; do not emit a second order or a same-bar reversal. Exit processing has priority over new entry; an exit bar is ineligible for re-entry even if its pattern meets entry. After a confirmed exit, a new entry requires a **fresh** later completed bar satisfying the full predicate (zero extra cooldown). Any qualifying outside-bar during LONG is ignored and not queued. Rejected/cancelled/failed orders clear in-flight state without phantom exposure; require a fresh future entry or exit decision. No partial closes, pyramiding, BO/SO, DCA, shared capital, concurrent instruments, short, borrowing, leverage, compounding, stop order, limit/maker order, intrabar order or forced terminal liquidation. An open terminal position is marked at the last observed close, not synthetically sold.

## Causal data and time (Gate 6)

Binance kline timestamps are **candle open** times T[t]. Require contiguous, strictly increasing UTC daily opens separated by 86400 seconds; a complete bar t is available for a decision only at E[t]=T[t]+86400 seconds. A feature/decision for t uses no bar >t and never treats an incomplete current daily bar as complete. The prior-bar extrema/body are t-1; ATR14 uses only t and earlier. Both order event and simulated same-close fill are labeled by effective decision time E[t] even though the pinned engine's internal candle row timestamp remains T[t]. This is a **historical simulator convention**, not an assertion that a live order sent after close can fill retroactively at that same close. If a bar is missing, duplicated, out of order, incomplete, invalid or not actually available by E[t], fail closed/abort that segment; never interpolate, forward-fill, substitute a price or shift to an unverified next-open path.

## Pinned Hummingbot model and execution (Gate 5)

**Exact pinned baseline:** Hummingbot package 20260920; VERSION dev-2.17.0; HCH725/hummingbot immutable commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3. Read directly through the connected GitHub app this cycle: hummingbot/VERSION; hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py (1d interval and /api/v3/klines); binance_spot_candles.py (UTC open-time and OHLCV REST parsing); hummingbot/strategy_v2/backtesting/backtesting_engine_base.py (completed row update, determine_executor_actions/CreateExecutorAction dispatch, BacktestPositionHold BUY/SELL netting, average price and fee accumulation); hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py (ExecutionStrategy.MARKET fills first supplied row at that row's **close**, with filled_amount_quote and cum_fees_quote, then POSITION_HOLD); and hummingbot/strategy_v2/executors/order_executor/data_types.py (OrderExecutorConfig and MARKET). Accepted Alpha PR #414 reports independent 902/902 wheel/source byte identity and 33-assert representative primitive validation; **that prior verification is cited, not repeated or rehashed this cycle**. Merely seeing a controller or MARKET enum is not used as evidence of other execution paths.

**Bounded controller mapping (not yet implemented):** A dedicated strategy controller may compute the declared finished-bar features and FLAT/LONG state, then submit CreateExecutorAction(OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY or SELL, amount=Decimal("0.001"), execution_strategy=MARKET, price=None, leverage=1)). The controller must reconcile the confirmed OrderExecutor POSITION_HOLD fill and its own in-flight state, not equate a requested action with a filled position. SELL is allowed only against the full previously filled spot long; BacktestPositionHold nets opposite orders and computes gross matched PnL. A controller must not assume the pruned terminated-executor view equals current inventory. The pinned simulator's first-row-close fill is the **only** execution primitive claimed here; no unsupported intrabar stop, next-open, maker or real spread model is needed by this derivative.

**Frozen research accounting:** initial 10,000 USDT quote cash and zero BTC; one unit 0.001 BTC maximum. On BUY at positive valid P, require available quote cash >= 0.001*P*(1+0.001); debit notional plus fee and credit exactly 0.001 BTC only on confirmed full fill. On SELL, require that confirmed inventory; debit 0.001 BTC and credit notional minus fee. Fixed trade_cost=0.001 of filled quote notional **per side** (0.1%) is an explicit **research assumption**, not independently verified realized Binance fees. BacktestPositionHold's realized PnL is gross; deduct both-side cum_fees_quote exactly once for net realized PnL, with cash and marked inventory tracked separately. If order cannot be filled in full, cash is insufficient, or price/fee is missing or invalid, fail closed rather than invent a partial fill or price. Spot has no perpetual funding leg; funding is **not applicable to this spot derivative**, not a zero-funding futures assertion. No borrow interest or margin applies. No additional slippage is modeled; unlike the author's 2-tick source backtest assumption, this model **omits** spread, latency, market impact and tick/lot/min-notional checks. It must never claim actual fills, exchange fees or real-world executable returns.

## Six-gate evidence summary

1. **Deterministic:** frozen source feature, exact body ratio, ATR seed/recurrence, thresholds, warmup and action precedence; no training/model/parameter search.
2. **Direction:** Binance BTC-USDT spot BUY-to-long and SELL-to-flat only; no short/futures/margin permission assumed.
3. **Entry/exit/risk:** outside-bar bearish-close long, frozen ATR close-only stop and target, full sell, no other exits or hidden executor stop defaults.
4. **Position:** exactly one 0.001 BTC unit, explicit fill-dependent four-state machine, no adds/DCA/concurrency, no same-bar re-entry, fresh-bar requalification.
5. **Pinned engine:** exact package/version/commit, spot 1d kline path, MARKET-close OrderExecutor, BacktestPositionHold netting and fixed research fee ledger inspected; prior accepted package/primitive verification separately identified. Intrabar/next-open/live economic support is **not** claimed.
6. **Causality:** 30 complete-bar warmup, prior-bar extremes, point-in-time ATR, effective-time mapping, contiguous-data fail-closed rule, no future inputs.

All six are **proposed** for independent Hermes Auditor source-fact and engine-capability review; the Scout's PASS frontmatter is not a self-issued merge approval.

## Evidence and limitations

**Source-reported:** the author's outside-bar and below-previous-low long setup, above-previous-high sell setup, optional stop/target/following-open variants, default 2R, equity-risk sizing and example commission/slippage, as published on TradingView. These are descriptions, **not** a reproduced Pine backtest.

**Independently reproduced:** none for the **strategy**. Only read-only GitHub code-path inspection occurred in this Scout cycle. No TradingView/Pine execution, strategy-specific Hummingbot run, Qlib backtest, event-level parity, profitability metric or real exchange fill was generated. Package/source wheel correspondence and representative primitive tests were reported by the independent reviewer on accepted PR #414, not newly executed here.

**Negative evidence:** full Pine and exact author body-filter threshold were not accessible, so 1.5x is a transparent **researcher-defined** value. The close-only ATR bracket is not the author's native intrabar stop/target, and no original 2-tick slippage is modeled. Same-close fills are a simulator accounting convention that may exaggerate edge. A bearish outside-bar buy may lose sharply, particularly when close-only stop exits are delayed. Actual exchange fees, precision, partial fills, latency and slippage are not validated.

**Falsification plan:** when separately authorized downstream, first reproduce this derivative's pattern/ATR/entry/exit timestamps and exact close-fill ledger in a representative Hummingbot run and a Qlib counterpart; reconcile every BUY/SELL, position size, fill price, entry-frozen ATR stop/target, effective timestamp and both-side fees. Validate any newly required execution primitive once before mass Qlib screening. Disagreement or missing prices must not be hidden by final ROI matching. No such execution is authorized by this record.

## Crypto portability

BTC-USDT Binance spot daily is a **specific bounded research instantiation**, not a universal market/timeframe ban. Futures, shorting, other pairs, 1h/4h, DCA or intrabar exits would be separately specified derivatives and require their own pinned-engine compatibility evidence.

## Implementation status

not-implemented. This record does not supply an executable controller, Qlib recipe, parity run, container change or deployment. HB_READY research admission does not imply executable materialization or profitability.

## Adoption boundary

status: research-only; implementation_status: not-implemented; adoption: not-approved; approval_scope: research-only. Independent Hermes Auditor GitHub Webhook Review alone may remediate source facts, exact-head PASS merge, or NOT_LOSSLESS close. Scout does not merge, approve, close or update README.

## Related Wiki records

None asserted; no private research or Survivor status imported.

## Sources

- TradingView primary: https://www.tradingview.com/script/X4ulJUXd/ (SpeculationLab, published 2025-10-11, inspected 2026-10-25).
- Pinned engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Pinned MARKET simulator: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- Pinned backtesting/position netting: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- Prior accepted independent engine/package evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
