---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "RSI confirmed oscillator-pivot breakout BTC-USDT spot 1d long-flat — independent derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-12-11
sources:
  - https://www.tradingview.com/script/25eSqem2-RSI-Pivot-Breaks/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RSI confirmed oscillator-pivot breakout — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary source read directly:** TradingView open-source *indicator* **RSI Pivot Breaks**, author **Uncle_the_shooter**, published **2025-12-11**, stable script ID **25eSqem2**; public first-party URL https://www.tradingview.com/script/25eSqem2-RSI-Pivot-Breaks/ , accessed 2026-10-28. The page describes (a) RSI or smoothed-RSI pivot highs/lows, (b) left/right confirmation delay, (c) bullish RSI breakout above the latest pivot high, (d) bearish breakdown below the latest pivot low, and (e) optional RSI zone filters and OB/OS alerts. It does **not** provide a complete executable trading strategy or full Pine source bytes in the accessible page text. No Pine revision hash, native defaults, tie handling, or author trade/fill/cost claims are verified.

**Explicit independent derived strategy — NOT source-native/lossless Pine:** Retain only the oscillator-pivot breakout/breakdown concept. Researcher independently specifies RSI14 Wilder on close, strict unique 3-left/3-right oscillator pivots, newest-level state/consumption, long/flat trade mapping, UTC daily Binance BTC-USDT spot, 0.001 BTC single-unit size, 10,000 USDT cash, 100-bar warmup, same-completed-row-close synthetic MARKET fills, 0.1% hypothetical fee per filled side, and exact pending/ledger semantics. RSI-MA smoothing, pivot-zone filters, OB/OS-cross trades, shorting, divergence and chart visuals are disabled. These researcher choices can materially change original indicator events. The derivative is assessed only against its own frozen rules.

**Frozen derived identity:** `TV:25eSqem2|Uncle_the_shooter|published-2025-12-11|independent-derived-v1-2026-10-28|RSI14-Wilder-close|strict-pivot-3L3R|latest-confirmed|break-high-long-break-low-flat|BTC-USDT-spot-UTC-1d|Q0.001|completed-close-MARKET|fee0.001`. Stable publication ID/date identify lineage; the identity does **not** pretend that unavailable original Pine bytes are immutable.

**Dedup:** GitHub Connector inspected main at `92ad3faef455ea4fd2b9610342b26d77d5640f75` and again at `68d853c00291e8935affcb0d8d1f8efa801aebef` after unrelated PR #562 merged. Searches for `25eSqem2`, `Uncle_the_shooter` and the exact title found no main record; open research PR searches for the ID and RSI pivot breakout returned none. The existing `rsi-divergence-pivot-oscillator-reversal-two-sided-btcusdt-4h-2026-10-12.md` combines **price** and RSI pivots for divergence and extreme-zone conditions; it does not buy a breakout of the last confirmed **RSI oscillator pivot high** and exit on the RSI pivot-low breakdown. This is a materially distinct signal topology, not a lookback-only variant.

## Economic mechanism

### Source-reported

The author describes breaking confirmed oscillator resistance (RSI pivot high) as bullish momentum acceleration and breaking confirmed oscillator support (RSI pivot low) as bearish momentum. The pivot's right-hand confirmation introduces an unavoidable delay. The source supplies no independently reproduced trade economics or performance.

### Research interpretation

A long-only momentum experiment enters after a newly confirmed RSI pivot high is broken and exits when the most recently confirmed RSI pivot low breaks. Consuming levels avoids repeated entries on the same breakout. No stop means exposure can persist indefinitely; no profitability is presumed.

## Signal

Let `T[t]` be the actual UTC daily candle OPEN timestamp, `C[t]` its actual CLOSE, and `R[t]` Wilder RSI14. All signal arithmetic uses finite unrounded double-precision values and the exact strict/weak inequalities below.

1. **RSI:** For `t>=1`, `d[t]=C[t]-C[t-1]`, `g[t]=max(d[t],0)`, `l[t]=max(-d[t],0)`. Seed at `t=14` with arithmetic means `G[14]=sum(g[1..14])/14`, `L[14]=sum(l[1..14])/14`. Thereafter `G[t]=(13*G[t-1]+g[t])/14`, `L[t]=(13*L[t-1]+l[t])/14`. If both zero, `R=50`; if L=0<G, `R=100`; if G=0<L, `R=0`; otherwise `R=100-100/(1+G/L)`. Undefined before index14. No alternative RSI seed, future fitting, price smoothing, or rounding.
2. **Strict 3/3 pivots:** At completed bar `t`, a center `j=t-3` is confirmed pivot HIGH iff `R[j]` is strictly greater than each of `R[j-3],R[j-2],R[j-1],R[j+1],R[j+2],R[j+3]`; LOW iff strictly less than each. All seven must be defined. A tied extreme yields no pivot. Center j cannot be known before completion of t=j+3. Retain only the newest confirmed HIGH level H and newest confirmed LOW level L; same-side new pivot overwrites any old level.
3. **Event order/availability:** On completed t, evaluate using only H/L registered **by t-1**. `up[t] = H exists && R[t-1]<=H && R[t]>H`; `down[t] = L exists && R[t-1]>=L && R[t]<L`. Equality at current t is not a breakout. Any up/down event consumes/disarms its side's level **even if no trade can be placed**. Only after event evaluation, register pivots newly confirmed at t for use starting **t+1**; new levels supersede consumed old levels. An absent/consumed level cannot trigger again until a newly confirmed pivot arrives.
4. **Orders and priority:** If confirmed LONG and `down[t]`, emit one MARKET SELL for the full confirmed 0.001 BTC; ignore `up[t]` as a trade. Else if confirmed FLAT, `up[t]`, and modeled cash is sufficient, emit one MARKET BUY for 0.001 BTC. While a BUY or SELL is pending, evaluate/consume signal levels but emit no additional order. No same-bar exit/re-entry. If cash is insufficient, consume the breakout but remain FLAT; wait for a **new pivot and new crossing**, never enter late from a stale event. A down event while flat or up event while long has no order effect.
5. **Explicitly disabled:** short/reverse, stop loss, take profit, trailing, time exit, partial exit, DCA/safety orders, pyramiding, concurrency, rebalancing, compounding, other pairs, leverage/margin, MA RSI, OB/OS standalone triggers, pivot-zone filters, and forced end-of-sample liquidation. There is no additional cooldown beyond pending-order and same-bar restrictions.

## Required data

One Binance `binance` spot `BTC-USDT` UTC `1d` OHLCV series. Require finite positive O/H/L/C, H>=max(O,C), L<=min(O,C), finite volume>=0, strictly increasing unique opening timestamps exactly **86400 seconds** apart. All bars must be fully completed before decision; missing, malformed, partial, duplicate, out-of-order, gapped, NaN or nonfinite candles **invalidate the entire run**, not interpolated, dropped, compressed or forward-filled. No external, cross-asset, intrabar, higher-timeframe, funding or order-book input.

Warmup: 100 contiguous completed daily bars indices 0..99, starting FLAT with unset pivots. Compute RSI/pivot state during warmup but never order; first eligible completed decision index100. Backtest start must include these 100 rows **in the controller's visible decision window**, not rely on the data provider's pre-start buffer being visible. No historical position inference or future data.

Causality clock: REST `T[t]` is **opening** timestamp; the candle's close is available no earlier than `D[t]=T[t]+86400`. The derivative's effective decision and synthetic fill clock are D[t], while the engine stores T[t] internally. A completed-row close is a historical idealization, not a claim of a real market order executable at that exact close after data arrival. No repainting, negative shift, future extrema, partial HTF bar, or whole-sample preprocessing.

## Execution assumptions

**Actual pinned path inspected via GitHub Connector this cycle:** Hummingbot distribution package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Direct reads: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` supports `1d`; `binance_spot_candles.py::_parse_rest_candles` reads REST open timestamp and OHLCV; `strategy_v2/backtesting/backtesting_data_provider.py` obtains historical candles and contains a missing-price fallback; `backtesting_engine_base.py` processes rows/actions and nets positions through `BacktestPositionHold`; `executor_simulator_base.py` converts float values to Decimal; `executors_simulator/order_executor_simulator.py` performs MARKET first-row actual-close fills; `executors/order_executor/data_types.py` defines `OrderExecutorConfig`. Prior independent Auditor review in merged Alpha PR **#414** reports wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148` and 902/902 Python-file source identity. **Not rehashed this cycle**; if that prior mapping cannot be independently relied on, Gate 5 is unproven.

**Controller/executor:** A future minimal strategy-specific ControllerV2/backtesting controller (not implemented here) computes causal completed-bar RSI/pivot features and emits `CreateExecutorAction` containing `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`. The inspected `BacktestingEngineBase.simulate_execution` calls controller actions on each processed row and dispatches `OrderExecutorSimulator.simulate`, which selects the **first supplied row's actual close**, sets `filled_amount_quote=float(config.amount)*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and `CloseType.POSITION_HOLD`. `BacktestPositionHold.add_executor/_process_order` nets opposite BUY/SELL base amounts and computes gross realized quote PnL; fees are separate. No maker, next-open, intrabar, multi-asset or futures path is claimed. Missing close invalidates the run: never accept `BacktestingDataProvider.get_price_by_type` fallback `Decimal("1")`. Validate full data continuity **before** `prepare_market_data.dropna` can silently compress gaps.

**State, fills, and cash authority:** Initial unborrowed **10,000 USDT** cash, zero BTC. Controller has `FLAT/PENDING_BUY/LONG/PENDING_SELL` states and a persistent confirmed-executor-ID ledger independent of the default one-hour-pruned terminated-executor view and delayed `positions_held`. Submission only enters PENDING; only a unique, confirmed `POSITION_HOLD` executor with finite positive actual close, positive filled quote and matching side/ID confirms BUY or SELL. Pending prevents duplicate actions; unconfirmed, missing, duplicate, partial or ambiguous fills **abort** (do not invent fills). The engine may surface the fill to the controller on a later row and flush the hold later; wait for its documented ledger updates, reconcile after flush and on the last row. Position classification comes from the persistent confirmed-fill ledger, not `hold.is_closed` exact-zero or a stale `positions_held` view.

**Explicit float/Decimal and reconciliation policy:** The pinned simulator computes quote and fee with binary float; `ExecutorSimulation` calls `Decimal(float)`, and `BacktestPositionHold` derives base via `filled_amount_quote/Decimal(str(fill_close))`. Tiny nonzero base/fee residues are expected. The **engine-returned** `filled_amount_quote` and `cum_fees_quote` are the sole cash/fee authority, not a second exact-Decimal Q*price ledger. After each confirmed BUY, debit their **sum**; after SELL, credit their **difference**. Preorder affordability uses `cash>=Decimal("0.001")*Decimal(str(C[t]))*Decimal("1.001")`; if postfill cash falls below `-0.00000001 USDT`, abort. After the hold's delayed flush, require `abs(hold.net_amount_base - expected_confirmed_inventory) <= 0.000000001 BTC`, where expected inventory is 0 or 0.001 BTC from confirmed order IDs, and per fill `abs(engine_fee - Decimal("0.001")*engine_filled_quote)<=0.00000001 USDT`. These are **researcher-frozen numerical acceptance bounds**, not exchange precision claims. Dust within bounds is ignored **only for controller FLAT/LONG classification**; raw hold/fee values remain in economics, never rounded away or overwritten. Any larger mismatch, NaN, negative/unknown fill or unsupported partial fill aborts. Realized net PnL = engine hold **gross** realized quote PnL minus accumulated engine fees, without subtracting fees twice. Final open exposure is marked with the actual last close; do not fabricate a terminal SELL.

**Costs and permissions:** `trade_cost=0.001` per filled side is a **hypothetical 0.1% research fee**, not a verified Binance tier. Historical model has no modeled spread, impact, latency or slippage, not real-world zero slippage. Spot funding and futures margin are **inapplicable**, not asserted zero realized perpetual funding. Exchange lot/tick/min-notional constraints and live partial fills are not proven. No leverage, borrowing or shorting. HB_READY means this bounded synthetic path is expressible, not that a dedicated controller or Qlib executable artifact exists.

## Evidence

### Source-reported

TradingView first-party RSI Pivot Breaks page, Uncle_the_shooter, 2025-12-11: RSI/MA RSI pivots, left/right delayed confirmation, oscillator pivot-high break bullish and pivot-low break bearish, optional filters/OB-OS signals. No source performance or native trade economics reproduced.

### Independently reproduced

**Not independently reproduced.** No TradingView event replication, Qlib/Hummingbot strategy backtest, wheel byte rehash, trade fills, or profitability calculation was performed. Primary page and pinned source paths were read; prior independent wheel mapping #414 is explicitly cited as prior evidence.

### Negative evidence

- Complete original Pine source/defaults and native execution semantics unavailable in public page text. The independently specified RSI/pivot/order rules are **not** claimed to be original code.
- Main at initial SHA `92ad3faef455ea4fd2b9610342b26d77d5640f75`: 408 root strategy Markdown records, README count408. Main advanced during this cycle via independently merged FMZ PR #562 to `68d853c00291e8935affcb0d8d1f8efa801aebef`: 409 root records, README count408 immediately after merge; the new FMZ record's frontmatter is PASS. This is a **recent webhook bookkeeping lag**, not evidence of a non-PASS strategy. This Scout never edits README. Equal counts alone would not prove all 409 PASS; no all-record re-audit is claimed.
- No exact source-ID/author duplicate on main or open research PR; RSI-price divergence and price-pivot families are materially different.

## Falsification plan

Before mass Qlib screening, check RSI seed/flat prices, strict pivot ties, j+3 availability, t+1 level activation, stale/consumed levels, simultaneous new pivot/event priority, flat/down and long/up no-ops, warmup first eligible t100, cash insufficiency, pending full-fill reconciliation, last-row flush and open position. Run prefix-only signal checks against longer data prefixes (no future influence), then representative Qlib/Hummingbot event-level validation only if a new execution primitive is required. Reconcile real pinned simulator quote/fee/hold against the explicit bounds. Any mismatch invalidates the version, never becomes a survivor claim.

## Crypto portability

This record freezes one Binance BTC-USDT **spot 1d** long-flat model. Other assets, frames, perpetual margin/funding, multi-asset, BO/SO 6/6/6 and leverage 3x/5x are **optional downstream derived experiments**, not HB_READY prerequisites.

## Limitations

Source indicator's full Pine/defaults are not verified; this is not source-native. No protective stop/time exit can mean prolonged drawdown. Synthetic completed-close MARKET is optimistic and not live executable liquidity. Hypothetical fee and unmodeled slippage, real precision, latency, rejects/partial fills are limitations. No profitability, Qlib parity, HB Certified, Survivor or trading authorization.

## Implementation status

**not-implemented**. No controller, Qlib executable, backtest, deployment, container or workflow modification. If formally selected, use existing `IMPLEMENTATION_NEEDED` engineering route, not a new admission flag or registry.

## Adoption boundary

**research-only / not-approved / approval_scope: research-only**. No Paper, Testnet, Live, trading, cron or n8n authorization.

## Related Wiki records

None created or modified.

## Sources

- TradingView first-party publication: https://www.tradingview.com/script/25eSqem2-RSI-Pivot-Breaks/
- Hummingbot pinned source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Previously independently audited distribution mapping: https://github.com/HCH725/alpha-strategy-research/pull/414
