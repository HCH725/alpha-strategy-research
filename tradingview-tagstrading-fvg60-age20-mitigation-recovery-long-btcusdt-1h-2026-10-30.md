---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TagsTrading bullish FVG 60% mitigation-to-zone-recovery — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-09-28
sources:
  - https://www.tradingview.com/script/PjH7wg3n/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bullish FVG 60%-mitigation-to-zone-recovery — independently specified derivative

## Provenance

**Primary source, directly read 2026-10-30:** TagsTrading, *Order Block Volumatic FVG Strategy*, TradingView public open-source script, published **2025-09-28**, stable script identity **PjH7wg3n**, https://www.tradingview.com/script/PjH7wg3n/ . The author describes FVG-zone mitigation percentage, age gating, optional close-versus-high/low mitigation, most-recent qualifying zone priority, directional confirmation, LTF-volume/Bull-Bear-share filters, fixed-percent stop and profit-activated trailing stop. The author suggests 60–80% mitigation and 20–30-bar minimum age as **starting presets, not fixed source defaults**. The page identifies Pine v6 and credits BigBeluga's original Volumatic FVG indicator (CC BY-NC-SA 4.0). No complete Pine source bytes or exact source revision hash were retrievable through the publicly rendered page; this record reproduces no copyrighted source code and makes **no source-native or lossless equivalence claim**.

**Immutable derivative identity:** `TV:PjH7wg3n:TagsTrading:2025-09-28 | independent-bull-FVG-60pct-age20-recovery-v1:2026-10-30 | BinanceSpot:BTC-USDT:UTC1h | three-bar-upgap | min-age20:max-age120 | prior-close-cross60 | exit-zone-upper-or-lower | 160bar-warmup | Q0.001BTC:cash10000USDT | completed-t-signal:next-completed-t+1-MARKET-close | fee0.001-per-side`. Changing any formula, market, window, execution, fee or state rule creates a different derivative.

**Full source-versus-derivative boundary:** Source-native *ideas* used are FVG-zone mitigation, an age filter, optional close-only measurement, most-recent-zone selection and no pyramiding. The **researcher independently defines** the three-bar bullish gap formula, 60% depth threshold, 20–120-bar age window, strict fresh-cross trigger, invalidation/consumption, zone-boundary close exits, spot long-only market, fixed quantity/cash, 160-bar warmup, delayed completed-close idealized fills, hypothetical fee and full state machine. The source's LTF volume split, box volume and Bull/Bear-share gates, short leg, optional directional-candle gate, original fixed-percent stop, triggered trailing stop, and unknown original order/timing semantics are **explicitly disabled/replaced**; these changes materially alter trade events. This is an independent FVG-retest experiment, **not** a claim that the TagsTrading original itself passes HB_READY.

**Pre-write dedup:** Current `main@734741223d54586a4eef77367c32d9cb16c2947c` nontruncated Git tree has **461** root strategy Markdown records and README count **461**; 14 spread-across-tree frontmatters were checked as PASS, not an all-461 status audit. GitHub code and PR searches for `PjH7wg3n`, `TagsTrading`, `volumatic`, and FVG mitigation found no matching admitted/open research rule. Eleven open research PRs were inspected. Nearest admitted `fair-value-gap-breakout-long-btcusdt-1h-2026-10-10.md` uses an FMZ-source two-bar range-gap **breakout** with prior-close confirmation and opposite-gap flattening, **not** an aged bullish zone's 60%-deep **retest** followed by zone-boundary recovery/failure. `tradingview-cnagda3-onebar-gap-profit-gated-opposite-exit-long-flat-btcusdt-1h-2026-10-28.md` uses a one-bar gap/profit-gated opposite exit, not an age-filtered FVG mitigation. No trivial parameter variant or source duplicate is proposed.

## Economic mechanism

### Source-reported

The author treats FVG boxes as potential price-imbalance zones, tests the percentage of price re-entry (mitigation) into a box, and optionally filters by age, volume and direction. The source also describes intrabar and lower-timeframe volume dependencies that this derivative does **not** reproduce.

### Research interpretation

A sufficiently old bullish three-bar imbalance that is retested deeply on a completed close may rebound toward its upper boundary; a completed close at/below the lower boundary instead falsifies the recovery. This is a testable *hypothesis*, not observed order flow, institutional activity, profitability or source-native performance.

## Signal — deterministic formula and state (Gates 1–4, 6)

1. **Data:** Binance BTC-USDT **spot**, strictly consecutive UTC-aligned **1h completed** OHLCV bars indexed `t=0,1,...`. For each bar require finite positive O/H/L/C, `L<=min(O,C)<=max(O,C)<=H`, finite base volume >=0 and strictly consecutive 3600-second open timestamps. Only OHLC is decision-relevant. Missing, duplicate, unfinished, zero-price or corrupt bars abort; no interpolation, invented candle, or substitute fill price.
2. **Zone creation:** At each completed `t>=2`, if `L[t] > H[t-2]` strictly, append one bullish zone `Z=(born=t, lower=H[t-2], upper=L[t], depth=upper-lower>0, threshold=upper-0.60*depth, used=false, invalid=false)`. No bearish zones, OB inference, volume split or additional FVG conditions. Equal prices never form a gap. Creation uses only information available at the completed bar.
3. **Zone lifetime:** At each later completed bar `u>born`, invalidate a not-yet-used zone when `C[u]<=lower` or `u-born>120`. Invalidation is permanent; a close above `upper` does **not** invalidate an unmitigated zone. Keep zones in formation order; prune invalidated/expired zones without future reads. Zones younger than 20 bars are ineligible but remain trackable. A zone may have been touched before age 20 and later become eligible only on a *new* qualifying threshold crossing.
4. **Entry candidate:** On a completed decision bar `u>=160`, while FLAT and with no pending action, consider only unused/noninvalid zones with `20<=u-born<=120`. A zone qualifies iff `C[u-1] > threshold` and `lower < C[u] <= threshold` (strict fresh crossing into >=60% mitigation, close remains above lower bound). No bullish-body confirmation. If multiple qualify, select the zone with the greatest `born` (most recent; ties impossible since at most one new bullish zone per bar). Record its immutable `lower/upper`, mark `used=true` immediately, queue exactly one BUY for bar `u+1`. No second entry is queued on the same bar.
5. **Warmup:** Bars `0..159` are indicator/zone-state-only, **flat with no trades**. Zones formed during warmup can qualify after index 159 if their age is still within 20..120. First legal decision is `u=160`; no whole-sample calibration, no negative shift, no right-pivot or lookahead.
6. **Entry fill:** On the next **completed** bar `u+1`, at its effective close time, issue a historical simulator MARKET BUY for `Q=Decimal("0.001")` BTC at that bar's **actual validated close**. Starting cash is `Decimal("10000")` USDT, BTC 0. Research fee `f=Decimal("0.001")` of executed quote per side. Only a confirmed **full** fill with `cash>=Q*price*(1+f)` debits quote plus fee, credits Q BTC and sets LONG with frozen selected zone bounds. Insufficient cash consumes the signal and remains FLAT; missing price, unexpected partial fill, rejection, or ledger disagreement **aborts**, never manufactures a fill. The BUY fill bar cannot generate another signal.
7. **Exit decision:** While LONG, on each completed bar `v` **strictly after the BUY fill bar**, if `C[v]>=frozen_upper` (zone recovery), or `C[v]<=frozen_lower` (zone failure), queue a full-Q MARKET SELL for next completed bar `v+1`. These are **close-triggered signal exits**, not resting exchange stop/limit orders. `upper>lower` makes both triggers mutually exclusive. A zone expiring or being invalidated after entry does not alter frozen exit levels. No other exit is allowed.
8. **Exit fill:** At the next completed bar's real close, confirmed full SELL debits Q BTC, credits `Q*price*(1-f)` USDT, returns FLAT, clears the frozen zone and pending action. The SELL fill bar generates no entry. Only a fresh eligible zone-cross on a *later* completed decision bar may re-enter. An already-used zone can never re-enter.
9. **Priority and disabled behaviors:** States `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT`. Pending fills are processed before zone maintenance; all bars still update zone formation/invalidation causally, but pending/fill bars cannot issue fresh decisions. At most one position and one pending order, no adds/pyramiding, DCA, safety orders, shorts, borrow, leverage, margin, shared-capital cross-pair trades, cooldown beyond fill-bar suppression, intrabar triggers, maker/limit execution, TP/SL/trailing/time-based exits or discretionary overrides. No hidden Hummingbot defaults are adopted.
10. **Terminal behavior and arithmetic:** If the next completed fill bar does not exist, report pending unfilled action without invented liquidation. If LONG at end, mark remaining Q BTC at the last real completed close **separately** from realized PnL. Compare unrounded binary64 OHLC-derived thresholds; use 28-digit Decimal for Q, cash, fees and ledger. No parameter optimization or performance claim.

## Required data and causality

The only input is the actual Binance Spot BTC-USDT 1h OHLCV feed; volume is validated for feed integrity but **not** a trading filter. A Binance REST candle timestamp `T[t]` is its **open** epoch seconds; OHLC values become completed only at `E[t]=T[t]+3600`. Zone creation, age, invalidation and entry/exit decisions are effective at `E[t]`, never at `T[t]`. The next-completed-bar fill convention is effective at `E[t+1]` and uses only the actual historical `C[t+1]` as a retrospective fill price; it is **not** an executable live promise to know or trade at that close. Feature joins use raw open-labeled `T[t]`, and the controller must delay action until the designated next row. No LTF, HTF, external flow, model fitting, future pivots, incomplete bars or cross-market synchronization is required.

## Pinned Hummingbot engine, fill and accounting evidence — Gate 5

**Exact reviewed source pin:** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; `hummingbot/VERSION` is `dev-2.17.0`; repository's fixed research package is `20260920`. This cycle **directly read the immutable GitHub source files** listed below. Previously merged Alpha PR #414 reports 902/902 package-to-source Python-file identity; **this cycle did not rehash the package/wheel**, so independent Auditor must confirm the package mapping before accepting the Gate-5 claim.

- **Spot data:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly supports `1h`. `binance_spot_candles.py::_parse_rest_candles` reads open timestamp from REST `row[0]` and O/H/L/C/base volume from `row[1..5]`. `strategy_v2/backtesting/backtesting_data_provider.py::get_candles_feed` loads historical candles, and `get_candles_df` trims to the run window. Preflight >=160 actual contiguous completed bars plus any active-zone state, not merely configured `max_records`; reject incomplete warmup/gaps.
- **Feature and decision:** `strategy_v2/backtesting/backtesting_engine_base.py::prepare_market_data` backward `merge_asof` joins features on raw open-labeled timestamps and exposes actual `close_bt`; `simulate_execution` updates each row, then calls `controller.determine_executor_actions()`. A dedicated future controller, **not yet implemented**, must retain the *previous completed bar* signal and dispatch only on the specified next completed row; no `t+1` value is used to decide at `t`.
- **Order and fill:** `executors/order_executor/data_types.py::OrderExecutorConfig` permits `ExecutionStrategy.MARKET`, `price=None`, positive amount, leverage=1. Dispatch `CreateExecutorAction(OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1))` on the selected fill row. `backtesting_engine_base.py::simulate_executor` routes this to `executors_simulator/order_executor_simulator.py`, whose MARKET path takes the **first supplied historical row's actual close**, computes full `filled_amount_quote=Q*C`, fee `trade_cost*filled_amount_quote`, and terminates as `POSITION_HOLD`. Raw engine fill timestamp remains open-labeled; research effective close timestamp is `E[t+1]`. This is a pinned **idealized historical full-fill** model, not proof of actual exchange execution.
- **Position and cost ledger:** `BacktestPositionHold` (inside `backtesting_engine_base.py`) nets BUY/SELL matched base, records average entry, realized/unrealized gross PnL, and separately accumulates `cum_fees_quote`. Maintain a separate Decimal spot cash/BTC ledger from **confirmed** executor fills, reconcile full quantity and per-side hypothetical `trade_cost=0.001`, and calculate realized net `Q*(P_sell-P_buy)-f*Q*(P_buy+P_sell)`. Do not treat gross PnL as fee-inclusive. No perpetual funding, futures margin or liquidation is modeled because this declared strategy is **unlevered spot**; this is not a claim of observed zero futures funding.
- **Fail closed and economic limits:** `BacktestingDataProvider.get_price_by_type` can default to `Decimal("1")` for absent prices; explicitly forbid that fallback for any fill or mark. Require actual finite historical close, sufficient research cash, full fill, consistent executor/ledger totals, and no missing bars. The simulator does **not** verify actual Binance minimum notional, lot precision, dynamic fee tier, partial fills, slippage, depth, latency or order acceptance. These remain unverified live economics, never claimed as reproduced. No other data/executor capability is required by this **independently derived** close-only spot path.

## Evidence and six-gate assessment

### Source-reported

The 2025-09-28 public TradingView description reports FVG mitigation-based entry, age filtering, most-recent-box preference, optional candle confirmation, lower-TF volume-share filters, and fixed-percent/trailing risk legs. It suggests 60–80% mitigation and 20–30-bar age as **examples**. It does not provide a reproducible native Pine revision or independent performance numbers in the retrievable public text.

### Independently reproduced

**None.** No Pine equivalence test, Qlib/Hummingbot backtest, event-level parity, Survivor assessment, historical return, or real fill has been performed.

### Negative evidence

- Native Pine bytes, exact original FVG algorithm, native thresholds, lower-TF volume aggregation, original SL/trailing order semantics and original performance are **not verified**. This independent derivative does not purport to reproduce them.
- The derived close-only zone-failure exit can execute one completed bar later at a price far below `lower`; it is **not** a guaranteed stop at the boundary. An aged zone may never recover; drawdowns may be substantial.
- Full historical MARKET fills and 0.1% per-side fees are explicit **hypothetical research conventions**, not observed Binance executions or live trading authorization.
- A record with `hb_ready_status: PASS` is a **Scout six-gate eligibility assertion awaiting independent Hermes Auditor review**, not independently certified source facts, profitability, Qlib parity or downstream adoption.

**Gate map:** G1 = exact gap/zone/depth/age/cross/state formulas; G2 = Binance spot long/flat, short disabled; G3 = recovery/failure close exits and explicit disabled risks; G4 = one Q0.001 BTC position, no DCA, consumed zones, pending/cooldown/re-entry defined; G5 = pinned 1h feed + controller + MARKET close simulator + separate spot ledger and modeled fees with explicit missing-price guard; G6 = 160-bar warmup, completed-time availability, one-full-bar delayed fill, no future leakage. **Auditor focus:** exact source/derivative boundary, gap-zone event identity vs admitted breakout, cross/age and used-zone state, open-time versus effective-close timestamps, package/source correspondence, and executor fee/position accounting. Any unsupported assumption is a merge blocker; no reviewer invention to force PASS.

## Falsification plan

With this derivative's exact rules frozen, test whether deep age-filtered mitigation followed by boundary recovery improves *net* expectancy versus (a) otherwise identical no-age gate, (b) 30% rather than 60% depth, and (c) a simple 20-bar breakout. These are **future separate experiments**, not admitted alternate rules or claimed results. First establish representative Hummingbot/Qlib event-level capability parity before any large-scale Qlib screening of a new execution path.

## Crypto portability

BTC-USDT Binance Spot UTC 1h is the only admitted research scope for this version. Other symbols, perpetuals, timeframes, real volume/flow filtering, intrabar stop/trailing, LTF split and leverage would require separately specified and verified execution/data paths. The derivative has no cross-asset synchronization or portfolio optimizer.

## Limitations

No complete original Pine bytes; explicitly derived, not lossless. Historical fill-price idealization, fee assumption, possible late gap-failure exits, no risk cap beyond close-triggered zone failure, and unverified live precision/fees/slippage are material. This document is research-only and not a deployment recipe.

## Implementation status

Not implemented. No dedicated Hummingbot controller, Qlib executable recipe, backtest, container change or trading run was created. PASS admission alone does not establish Qlib materialization or parity; any selected implementation must follow the existing downstream engineering and independent-review workflow.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. No Paper/Testnet/Live authorization. House DCA/leveraged capital overlays are separate derived experiments, not prerequisites for HB_READY and not silently part of this strategy.

## Sources

- TagsTrading, *Order Block Volumatic FVG Strategy*, TradingView public open-source Pine v6 description, 2025-09-28: https://www.tradingview.com/script/PjH7wg3n/
- Fixed engine source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
