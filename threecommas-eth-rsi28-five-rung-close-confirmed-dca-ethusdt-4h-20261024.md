---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "3Commas ETH RSI(14)<28 five-rung close-confirmed DCA — explicitly derived Binance spot research model v1"
created: 2026-10-24
updated: 2026-10-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - rsi
  - dca
status: research-only
confidence: medium
source_as_of: 2026-10-24
sources:
  - https://www.tradingview.com/script/i90KnZdf-ETH-RSI-Strategy-3Commas/
  - https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# 3Commas ETH RSI(14)<28 five-rung close-confirmed DCA — derived spot v1

## Provenance

- **Primary source:** TradingView public open-source strategy **ETH RSI Strategy [3Commas]**, publisher/author **3Commas**, published **2026-06-28**; script ID **i90KnZdf**; public description inspected **2026-10-24 Asia/Taipei**. Stable source identity: https://www.tradingview.com/script/i90KnZdf-ETH-RSI-Strategy-3Commas/. The public page describes all five rung deviations, scaling, entry/exit rules, order sizes, source instrument, fees, and slippage. Its embedded Pine source pane was **not** retrieved as raw Pine; no claim of byte-for-byte Pine reproduction or an immutable Pine revision is made. This record freezes **derived rule revision v1**, not a mutable author's Pine binary.
- **Original/source-native disclosure:** BYBIT:ETHUSDT.P perpetual, 4h, RSI(14) < 28 when flat; $500 base; five orders at base-fill-relative -2%, -5%, -9.5%, -16%, -25%; order notionals $900, $1,620, $2,916, approximately $5,249, $9,448 (1.8x scale); take profit on close >= weighted-average entry * 1.03; no stop, trailing or short. Source reports $100,000 starting capital, 0.06% commission, three ticks slippage. The author's source-reported results are **not reproduced**.
- **This is a separately identified, non-lossless derivative.** Researcher changes, all frozen here: (D1) BYBIT perpetual -> **Binance ETH-USDT spot**, unlevered, no funding instrument; (D2) source close-triggered market/optional-limit execution -> **only MARKET fills at the NEXT 4h candle CLOSE** after a completed-bar decision, never same-bar or limit/intrabar fills; (D3) if multiple rung thresholds qualify, execute only the lowest-index unfilled rung on the next bar and reevaluate remaining rungs on later completed bars; (D4) explicit single-pending-order state, one bar after fill for ledger confirmation, take-profit-over-add priority, and no same-bar reentry; (D5) exact arithmetic $500 * 1.8^k, not the source's rounded display notionals; (D6) fixed source-stated **0.06% per-side modeled trade cost**, but no invented three-tick slippage, no actual exchange-fee claim, and no source-equivalent net-return claim; (D7) Wilder RSI seed/NaN, strict data validation and deterministic quantization specified below. No other signal filter, optimization, or risk overlay is admitted.
- The immutable **research identity** is TradingView script ID i90KnZdf + source-as-of 2026-10-24 + these complete derived-v1 rules + pinned engine commit. Different rung geometry, fee treatment, timing, symbol, execution mode or priority is a different strategy version. No historical survivor or backtest status is imported.

## Economic mechanism

### Source-reported

Mean-reversion accumulation after a deeply oversold 4h RSI state, with a fixed finite martingale-style five-step downside ladder anchored to the original base fill and a 3% gross-price rebound target above the changing volume-weighted cost. The finite number of orders bounds **additional purchases**, not downside loss: after the last order ETH can keep declining indefinitely. This is not a stop-loss strategy.

### Research interpretation

Test the same distinctive RSI<28 / five fixed-base-deviation / 1.8x-size / average-cost-TP mechanism under a deliberately slower, completed-candle-only **spot** execution model. The derivative trades fewer/farther-from-trigger fills than source Pine and cannot inherit its economics, alerts, or reported performance.

## Signal

**Fixed input and indicator.** Exactly one Binance spot ETH-USDT 4h OHLCV series, sorted ascending, no missing or duplicated intervals. Let C[t] be the positive finite completed close. Compute Wilder RSI on close with length 14: gains=max(C[t]-C[t-1],0), losses=max(C[t-1]-C[t],0); initial 14-change means seed gain/loss at the 15th close, subsequent averages via (13*previous+current)/14; RSI=100-100/(1+avgGain/avgLoss), with zero-loss positive-gain -> 100, zero-gain positive-loss -> 0, both zero -> 50. Do not evaluate entry until the first seeded RSI; NaN never triggers.

**Logical bar timing.** Binance candle timestamps label bar *open*. A completed 4h bar t becomes usable at its close time open_timestamp[t]+14,400 seconds. A condition evaluated on that completed close at t creates a pending market action for the **close of t+1**. No signal can fill on t, at t+1 open, or at an intrabar high/low. The pinned simulator indexes its row by the candle timestamp but uses that row's close for MARKET fills; interpret fill availability as the corresponding candle close, not its opening timestamp. Reject any report that labels the close fill as known at bar open.

**State:** FLAT, PENDING_BASE, LONG(k, base_price, total_qty, gross_cost), PENDING_ADD(k), PENDING_EXIT, where k is the count of already filled safety orders, 0..5. Only one order may be pending or filled per candle; one active deal on one pair, no overlap. No short, hedge, leverage, rebalancing, time exit, cooldown beyond pending-fill confirmation, or extra DCA.

1. When FLAT and RSI14[t] < 28, queue one base BUY of $500 notional for next candle close. RSI<28 is a **level**, not a crossover; if no position, repeated below-28 bars are eligible after the previous deal fully settles.
2. At the scheduled close, use the actual positive finite close as simulated MARKET fill price. Compute base quantity = floor_to_Binance_lot_step(500 / fill_price). The actual spent quote is quantity * fill_price, at most $500. Store **actual** base fill price, not signal close or assumed limit price. Confirm the fill in the native executor/position-hold ledger before the next decision. If quantity violates min-notional/lot rules, the research run fails closed; never fabricate a fill.
3. While LONG, at completed close t, compute the gross weighted-average entry from **confirmed filled quantities and their actual close-fill prices**. If C[t] >= 1.03 * avg_entry, queue one full-position MARKET SELL for next candle close. This TP has **priority** over all adds, including if an add threshold also holds.
4. Otherwise find the smallest unfilled rung j in 1..5 with C[t] <= base_price * (1-d[j]), where d=[0.02,0.05,0.095,0.16,0.25]. Queue exactly **one** add BUY for the next close with quote notional $500*1.8^j (j=1..5 gives $900,$1620,$2916,$5248.80,$9447.84). A deep gap does **not** create simultaneous fills or fill multiple levels at the same price; remaining rungs are reconsidered at subsequent closes. Rungs cannot be skipped, reused or filled twice.
5. No entry, add or exit is decided from a candle whose preceding pending fill has not yet been reconciled. On the candle that executes a pending order, do **not** create a second order. At the next tick the simulator books the previous fill into the position hold; then reevaluate from newly completed data. An unfilled/invalid order is a hard data/execution error, not a silent success.
6. On a pending exit, SELL exactly the confirmed net held ETH amount, already a sum of lot-step-quantized buys. The native ledger must net to zero; otherwise fail closed rather than treating residual dust as flat. Set FLAT only after ledger confirmation; the next later completed bar can start a new deal if RSI<28. There is no automatic reversal or immediate close-and-reopen on the same bar.
7. When all five adds are used, hold without further adds until the delayed 3% gross TP; no stop, margin liquidation, forced close, session/date filter or end-of-sample fictitious liquidation. At end of history, report open exposure and unrealized PnL separately; do not fabricate an exit or a closed trade.

**Precedence:** pending-order settlement > TP > next eligible rung > (if flat) new base > hold. Decisions require a finite positive close, valid RSI, valid market rules and continuous 4h timestamps; otherwise fail closed. No future highs/lows, next-bar prices, higher timeframe, external series, interpolation or lookahead are consulted when choosing a signal.

## Required data

- Native Hummingbot Binance **spot** ETH-USDT 4h candles, valid OHLCV and 14-change warmup; only completed **close** is a decision input. OHLCV high/low are not execution triggers. No other instrument or cross-asset synchronization.
- Binance spot trading rules from the native connector for min size/notional, base-amount increment and price/quantity precision. If unavailable, fail; never invent a constant step size, fee tier or a fill.
- A native executor ledger carrying each actual simulator close fill, filled quote, quantity, timestamp and fee; and the aggregate position hold carrying net ETH, average entry and realized/unrealized gross PnL. Do not replace absent rows or prices with the data-provider's possible fallback price.

## Execution assumptions

**Gate-5 pinned first-party engine evidence, inspected via connected GitHub at immutable commit:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (2026-09-20); `hummingbot/VERSION=dev-2.17.0`, matching policy package `20260920`. This is static code-path evidence, **not a claim that a strategy controller has been implemented or that a backtest ran**.

- `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py` supplies Binance spot `ETH-USDT` symbol normalization and native candles; `.../binance_spot_candles/constants.py` explicitly includes `4h`; `candles_base.py` maps `4h` to 14,400s. `backtesting_data_provider.py` retrieves historical candles and Binance trading rules. The source's BYBIT perpetual/funding/slippage execution is **not** claimed supported by this spot derivative.
- `strategy_v2/backtesting/backtesting_engine_base.py` `run_backtesting(controller_config,start,end,backtesting_resolution='4h',trade_cost=0.0006)` initializes provider/controller, iterates timestamped rows, calls `determine_executor_actions()`, routes `CreateExecutorAction(OrderExecutorConfig)` to `OrderExecutorSimulator`, and accumulates `POSITION_HOLD` executions. `prepare_market_data()` exposes completed OHLCV row closes and feature rows; the proposed controller must **lag decisions one full candle** and must never read the next row's price for the current decision.
- `strategy_v2/executors/order_executor/data_types.py` has `OrderExecutorConfig` with `ExecutionStrategy.MARKET`, `TradeType.BUY/SELL`, amount and spot-compatible leverage=1. The native `order_executor_simulator.py` executes MARKET on its first supplied row at **that row's CLOSE**, records `filled_amount_quote`, `current_position_average_price` and `cum_fees_quote = trade_cost * filled_quote`, then terminates as `POSITION_HOLD`. No maker/limit/intrabar/next-open fill is asserted.
- `BacktestPositionHold._process_order` nets sequential buys and a full sell, updates quantity and weighted-average cost, and tracks gross realized/unrealized PnL. `add_executor` also accumulates fees. Its `summarize_results` can expose gross realized PnL and cumulative fees separately; **do not call its raw position-hold gross PnL fee-net**, and do not treat the built-in per-tick PnL series as audited fee-net equity. For a research report explicitly compute modeled fee-net realized = gross realized - sum(all entry and exit `cum_fees_quote`), and report open gross unrealized and accumulated fees separately. The native `trade_cost=0.0006` is a **fixed hypothetical per-side cost** copied from source's stated 0.06%, **not** verified actual Binance fees. No slippage is simulated on this MARKET close path; the author's three-tick source slippage is intentionally **not reproduced**, never replaced by an invented realized value. Venue spread, liquidity, market impact and fee currency are not verified; no realistic net profitability claim is permitted.
- Spot ETH-USDT has no perpetual funding or margin liquidation; **not applicable to the declared spot instrument**, not a statement that BYBIT perpetual funding was zero. No futures leverage, margin, cross-asset capital or liquidation path is invoked. Fixed $100,000 research cash is larger than the $20,632.64 maximum requested gross order notionals; if a future input price, precision, quote-balance or fee makes an order infeasible, abort instead of assuming credit or free fills.
- The proposed *strategy-specific* controller and state machine are **not implemented**. Their expressibility is bounded by the inspected native controller action, MARKET executor and position-hold code; a new data primitive, backtester change or live execution is neither requested nor assumed. Any engine discrepancy discovered by independent review invalidates this provisional PASS and blocks merge.

## Evidence

### Source-reported

TradingView script i90KnZdf, 3Commas, 2026-06-28: RSI14 on 4h <28; five fixed-from-base rung deviations -2/-5/-9.5/-16/-25%; 1.8x rung sizing; 3% gross average-entry TP; no SL/trailing/short; BYBIT perpetual, 0.06% fee, three ticks slippage; initial $100k. The page also reports 93 trades, +5.79% net profit and 3.83% max drawdown. **These are unverified author claims, not independently reproduced and not transferable to this derivative.**

### Independently reproduced

**None.** No Qlib/Hummingbot run, fill replay, price download, performance statistic, strategy-specific controller or event-level parity has been executed or claimed. First-party engine **source inspection** above is static expressibility evidence, not a performance reproduction.

### Negative evidence

- TradingView public HTML exposes the strategy description, not a raw retrievable Pine revision; exact Pine order-of-operations, historical bar simulator fills, alert JSON and any unmentioned defaults are **not certified**. This record is **derived**, never source-native.
- Perpetual venue, source three-tick slippage, source market/limit option and source same-bar-close timing are **not** reproduced. No real Binance spot fee tier, realized fills, funding, latency or order-book liquidity is asserted.
- Native position-hold accounting exposes gross PnL and fee totals; treating gross as net or relying on a possibly incomplete per-tick equity series would be incorrect. Fee-net reporting requires the explicit separate ledger subtraction above.
- No observed live/testnet/backtest data and no guarantee of fill availability or market rules at any requested historical timestamp. All missing inputs must fail closed.

## HB_READY six-gate assessment (proposed PASS, independent Auditor required)

1. **Deterministic signals — PASS proposed.** Wilder RSI(14) with explicit seed/zero rules, strict <28, finite fixed rung list, fixed 1.8x sizes, strict 3% TP, single action priority, explicit price rounding and no fitted model.
2. **Direction — PASS proposed.** Binance ETH-USDT spot BUY/add then full SELL, long/flat only, short disabled, leverage 1.
3. **Entry/exit/risk — PASS proposed.** Complete base/add/TP conditions, no SL/trailing/time stop/reversal; five adds cap incremental exposure, **not losses**.
4. **Position/DCA/concurrency — PASS proposed.** Exactly one deal, one pending order per candle, five distinct one-shot rungs, explicit fill confirmation, TP priority, no simultaneous actions, no same-bar reentry.
5. **Pinned engine/model — PASS proposed only for this bounded derivative.** Native `binance` spot 4h feed, `OrderExecutorConfig` MARKET at candle close, `BacktestPositionHold` weighted net position, explicit fixed fee and separate fee-net calculation, no unsupported source perpetual/limit/slippage claims. Requires independent source-code verification of the exact pinned path; not a proof of historical liquidity or backtest success.
6. **Causality — PASS proposed.** All decision inputs available only at 4h close; action delayed to following 4h close, RSI warmup 15 closes, no future extrema/HTF lookahead, fail on data gaps, timestamp availability distinguished from bar-open label.

**PASS is research admission only.** It is not profitability, Hummingbot strategy implementation, Qlib parity, Survivor, HB Certified, Paper/Testnet/Live approval. Any failed gate in independent Auditor review must result in `HB_READY: NOT_LOSSLESS` and close this Scout PR, not a relabeled or exempt main admission.

## Falsification plan

1. Audit the six source-derived distinctions against the current public TradingView page and independently inspect the pinned engine paths. If the source identity or a material engine path cannot be substantiated, reject.
2. In a separately authorized later engineering validation (not this Scout), replay synthetic contiguous 4h candles with RSI entering <28, then verify next-close base, five sequential rung fills (including a gap below multiple thresholds), average-cost updates and next-close TP; verify no same-bar orders.
3. Check priority when TP and a rung are simultaneously eligible, no reentry while pending, and full quantity netting after sell. Abort on insufficient precision, missing close, gap, zero price or absent trading rules.
4. Compare native executor/hold gross PnL, total recorded fees and explicitly reconstructed fee-net realized PnL; do not promote an unverified equity series as net. Verify logical close timestamps are not mislabeled as bar-open availability.
5. Only after representative Qlib/Hummingbot event-level parity for the exact execution/data path may this derivative enter any mass Qlib screening; do not transfer the author's TradingView results.

## Crypto portability

This version is **ETH-USDT Binance spot 4h only by explicit research choice**, not an eligibility restriction on other pairs or timeframes. Source's BYBIT perpetual and any 3x/5x futures DCA campaign require separate modeled funding, margin, fill, cost and event evidence; they are **not** this strategy. House BO/SO 6/6/6 is neither applied nor required for HB_READY.

## Limitations

- Martingale ladder can retain a large underwater position with no stop; finite allocation is not a maximum-loss bound.
- Candle-close market fills are a pinned **simulator convention**, not evidence that a real exchange fills at that historical close. Source's 3-tick slippage and actual market fees are unknown under this derivative; reported returns must not be equated.
- Strict validation and one-action-per-bar sequencing deliberately change the source's trade events; source-native equivalence and TradingView statistics are not claimed.
- No implemented controller or actual run exists; admission expresses the **bounded native engine path**, and independent review may still reject any semantic incompatibility.

## Implementation status

`not-implemented` / `research-only` / `adoption: not-approved` / `approval_scope: research-only`. Exactly one proposed root-level record; no engine, workflow, runtime or main-branch changes.
