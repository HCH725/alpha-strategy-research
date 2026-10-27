---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Mutanabby_AI ONEUSDT_MR1 5-to-3-bar dip window with 2-bar follow-through and 11xATR close trail — independent BTC-USDT spot 1h derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
  - derived
status: research-only
confidence: medium
source_as_of: 2025-12-11
sources:
  - https://www.tradingview.com/script/8I2576zL-Mutanabby-AI-ONEUSDT-MR1/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Mutanabby_AI windowed decline / prior-high exit with close-only ATR trail — independent BTC-USDT spot 1h derivative

## Provenance

**Primary TradingView source:** Mutanabby_AI, *Mutanabby_AI | ONEUSDT_MR1*, published 2025-12-11, stable public script ID **8I2576zL**, inspected 2026-10-27: https://www.tradingview.com/script/8I2576zL-Mutanabby-AI-ONEUSDT-MR1/ . The public description explicitly reports a LONG-only ONEUSDT 1h strategy: price move from five bars ago to three bars ago in the interval -7% to -5%; last-two-bar move <= 0%; primary exit when current close exceeds prior bar high AND prior bar open <= close nine bars ago; 11x ATR14 trailing stop; equity-based sizing; pyramiding up to four; and source-reported 0.1% commission. The page is marked open-source, but the complete Pine source bytes, source order processing, ATR trailing algorithm, actual sizing formula, Pine version and source revision hash were **not retrieved**. Those details are NOT asserted as source-native facts. Source-reported historical performance is not independently reproduced.

**Explicitly independent derived strategy, NOT source-native or a lossless Pine port.** Researcher alterations are: BTC-USDT Binance Spot 1h instead of ONEUSDT; precise two-window percentage arithmetic; first-activation edge entry; fixed 0.01 BTC quantity and 10,000 USDT initial cash instead of equity-sized/pyramiding source orders; no add-ons; ATR14 Wilder seed and a **close-only** 11xATR ratcheting stop (not an intrabar protective order); completed-candle close simulated MARKET fills; 120-bar warmup; strict entry/exit precedence and flat-state re-entry; and explicit hypothetical fee/cash ledger. The source's 11x ATR *multiplier* and primary exit predicates are preserved as reported, but the trailing-stop implementation is researcher-authored. These choices materially alter trade events and must never be represented as author defaults.

**Immutable research identity:** TV:8I2576zL | Mutanabby_AI | published:2025-12-11 | independently-derived-v1:2026-10-27 | Binance:BTC-USDT:spot:UTC1h | prior-return C[t-3]/C[t-5]-1 in [-7%,-5%] | recent-return C[t]/C[t-2]-1 <=0 | first-edge entry | primary exit C[t]>H[t-1] and O[t-1]<=C[t-9] | Wilder ATR14 close-ratchet 11x | 0.01BTC LONG/FLAT | 120-bar warmup | historical same-completed-close MARKET | fee=0.001/side. A different parameter, signal, state, price, timing or cost assumption creates a new derivative revision.

**Dedup on main SHA 9dad4fa8580f711e09f9dc3dff15cec68e5f17ea (381 root strategy records; README 381):** Connected GitHub code searches for 8I2576zL, Mutanabby and ONEUSDT_MR1 found no matching strategy record; open research/* PRs were enumerated (10 open) and no title/source matches this source or its two disjoint percentage windows with nine-bar-conditioned prior-high exit. Closest families differ: three-down-three-up uses consecutive-close counters; forven momentum-burst uses ATR-normalized percentile/ADX/volume gates; low-high dip uses 20-bar low recovery and 8% target. This source's **bounded lag-5-to-lag-3 decline plus lag-2 nonpositive return, paired with prior-high/lag-9 exit** is a materially distinct mechanism, not a trivial parameter substitution. Code search is not a claim of exhaustive semantic equivalence review of all 381 records.

## Economic mechanism

### Source-reported

The author frames a sharp but bounded older decline plus nonpositive recent two-bar return as potential selling exhaustion and exits when price strength clears the prior bar high subject to a nine-bar reference; an ATR-based trailing stop limits downside. The author reports historical ONEUSDT performance, which is neither audited nor transferred to BTC.

### Research interpretation

This derivative tests whether the **disjoint prior/recent return windows** select post-selloff continuation/exhaustion states differently from consecutive-red-candle or oscillator oversold rules. The exit requires both an upside prior-high close breakout and a nine-bar-relative open filter, while the 11xATR close trail may be very loose. It may have poor drawdown or no trades; no profitability or survivor claim is made.

## Signal

**All following clauses are frozen researcher-defined derivative semantics, not assertions about unseen Pine code.**

1. **Market/data:** Binance BTC-USDT unleveraged spot, consecutive UTC-aligned **1h** OHLCV bars t=0,1,... . Let O[t], H[t], L[t], C[t], V[t] be finite observed values with O,H,L,C>0, L<=min(O,C)<=max(O,C)<=H, V>=0. Binance kline open timestamps T[t] must be strictly increasing by exactly 3600 seconds; reject duplicate, missing, incomplete, nonfinite, zero-priced or malformed bars and abort the affected segment rather than interpolate, forward-fill, fabricate a price or silently drop a bar. All signals are based solely on completed historical candles.
2. **Return windows (researcher interpretation of the source prose):** P[t]=100*(C[t-3]/C[t-5]-1) for t>=5, and R[t]=100*(C[t]/C[t-2]-1) for t>=2, both calculated from unrounded float64 close prices. Condition A[t] iff **-7.0 <= P[t] <= -5.0**, inclusive; condition B[t] iff **R[t] <= 0.0**, inclusive. Define eligible[t]=A[t] AND B[t]. Do not reinterpret P as C[t]/C[t-5], or R as two separate down candles.
3. **Wilder ATR14:** TR[0]=H[0]-L[0]; TR[t]=max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1])) for t>=1. First ATR[13]=mean(TR[0..13]); for t>=14 ATR[t]=(13*ATR[t-1]+TR[t])/14. Require ATR[t]>0 and finite. All recursions are chronological; no revised or future data.
4. **Warmup:** t=0..119 are complete-bar warmup; initial FLAT, no inherited inventory or simulated orders. First eligible decision is t=120. The edge check eligible[t-1] is computed on the same fully valid prefix even during warmup/while LONG. A restart resets state and repeats warmup.
5. **Entry:** if FLAT with no pending order at eligible completed t>=120, ATR[t]>0, eligible[t] true and eligible[t-1] false, issue exactly one MARKET BUY of Q=Decimal("0.01") BTC, provided cash >= Q*C[t]*(1+f), f=Decimal("0.001"). The historical research model fills the entire order at **observed C[t]**, effective no earlier than bar completion E[t]=T[t]+3600 seconds. If balance, precision, notional or actual close data cannot be validated, reject/abort rather than invent an order or alter quantity. No entry is queued after a missed edge.
6. **Trailing stop (researcher-defined close-only 11xATR, not source-native):** after BUY at t=e, initialize trail[e]=C[e]-11*ATR[e], highest_close[e]=C[e]. For each subsequent completed bar t>e while LONG, highest_close[t]=max(highest_close[t-1], C[t]); trail[t]=max(trail[t-1], highest_close[t]-11*ATR[t]). A trailing exit triggers iff C[t]<=trail[t]. This is a **close-evaluated signal**, never an intrabar stop order or a guaranteed stop-price fill. A gap through the trail exits at observed C[t], not at trail[t].
7. **Primary exit:** for a position entered on a prior bar, primary[t] iff **C[t]>H[t-1] AND O[t-1]<=C[t-9]** (strict first comparison; inclusive second). No exit from this predicate before index 9, already covered by warmup. Exit at the completed current close C[t] via one full-quantity MARKET SELL. The author describes this predicate; its completed-bar execution and the single-position policy are derivative choices.
8. **Exit precedence and state:** while LONG from an earlier bar, evaluate trail[t] and primary[t]; if either true, issue one SELL of all filled BTC. If both true, label reason TRAIL before PRIMARY for audit but never double sell. No same-bar entry+exit or reversal; the bar of a SELL is ineligible for BUY. After confirmed full SELL, return FLAT, reset trail/highest_close, and await a **fresh false-to-true eligible edge on a later completed bar**. While LONG, repeated entry conditions are ignored; while FLAT, exit signals are no-ops. At most one pending order, one position and one strategy; partial/unconfirmed fills abort the modeled segment rather than infer position or cash.
9. **Disabled behaviors:** source's up-to-four pyramiding, equity-based sizing and ONEUSDT venue scope are deliberately not ported. Short, borrow, margin, leverage, futures funding, DCA/safety orders, scale-ins, partial take profits, intrabar high/low stop touches, exchange-native stop orders, time exits, arbitrary cooldown, maker queue and discretionary intervention are disabled. No hidden controller defaults.
10. **Terminal bar:** mark remaining BTC inventory at the last *actually observed completed* close; report unrealized gross and fee-adjusted equity separately. Do not fabricate liquidation, next-bar prices, future fees or forced flat close.

**Cash and fee ledger:** start with 10,000 USDT, zero BTC. Full BUY at P debits Q*P + f*Q*P; full SELL credits Q*P - f*Q*P. Use Decimal for order quantities/cash/fees, with float64 only for indicator comparisons; report realized gross PnL, cumulative quote fees, fee-net realized PnL, unrealized PnL and cash/equity separately. Actual exchange fee tier, spread, slippage, funding (not applicable to spot), order-book liquidity, market impact and real trading-rule history are not supplied or silently presumed. No compounding or equity-based position size.

## Required data

One pinned BinanceSpotCandles BTC-USDT **1h** feed, real historical OHLCV and verified complete UTC candle availability. The REST kline row[0] is **open time**, not signal time. Define completed-candle decision and historical model fill effective time E[t]=T[t]+3600 seconds, with all input data available by E[t]. The Hummingbot engine may internally retain T[t] for event indices; normalized audit/event comparisons must distinguish open timestamps from completion-time decisions. Historical same-close execution is an idealized simulator convention, **not** a live-achievable post-close quote. Reject incomplete terminal candles and missing prices; do not use the data provider's Decimal("1") missing-price fallback.

## Execution assumptions

**Pinned model inspected via connected GitHub app 2026-10-27:** Hummingbot package **20260920**, VERSION **dev-2.17.0**, repository commit **HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3**. Relevant immutable files inspected: `hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py`, adjacent `constants.py`, `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`, `backtesting_engine_base.py`, `executors_simulator/order_executor_simulator.py`, `executors/order_executor/data_types.py`, `executors/validation.py`. The pinned 1h Binance spot interval exists; REST parser maps row[0] to open timestamp and row[1..5] to actual OHLCV.

**Bounded supported execution path:** BacktestingDataProvider requests the configured historical 1h candles; BacktestingEngineBase.prepare_market_data() merges features and can drop missing rows, hence the **mandatory pre-validation** of complete/contiguous OHLCV before that step. BacktestingEngineBase.simulate_execution() calls update_state(row), then controller.determine_executor_actions(), and dispatches CreateExecutorAction/OrderExecutorConfig to OrderExecutorSimulator. A minimal **not-yet-implemented strategy-specific controller** must compute the above prefix-only returns, ATR, trail and durable FLAT/LONG/pending state; no existing generic controller is claimed to implement this rule. This is an expressibility proposal, not proof that an executable recipe is already deployed.

For each BUY or SELL, OrderExecutorConfig uses connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.01"), execution_strategy=MARKET, price=None, leverage=1 and explicit OPEN/CLOSE position_action. Pinned OrderExecutorSimulator's MARKET branch fills on the first supplied historical candle at its **observed close**, sets filled_amount_quote=Q*close and cum_fees_quote=trade_cost*Q*close, then terminates as POSITION_HOLD. BacktestPositionHold nets BUY/SELL positions, records gross realized/unrealized PnL and accumulates quote fees **separately**; fee-net performance must subtract them rather than mislabel gross PnL. Maintain durable controller state / position-hold ledger; the one-hour terminated-executor view may expire between candles, so it must not be mistaken for a FLAT position. Reject missing/invalid price and unsupported trading-rule precision/min-notional; do not treat API config acceptance as a fill guarantee.

**Economic/timing limits:** trade_cost=0.001 per filled side is an explicitly hypothetical research cost parameter (the TradingView author reports 0.1% commission; actual Binance tier not verified). No slippage, spread, partial fills, maker queue or market impact is reproduced. BTC-USDT spot has no perpetual funding/margin in this derivative; never invent zero-funding futures economics. Close-only 11xATR trail is a **signal**, not a stop-price order. Pinned source code path was inspected, but installed wheel/source byte identity was **not** revalidated this run. No Hummingbot/Qlib replay, live order, strategy implementation or event-level parity was performed; representative event-level Qlib/Hummingbot path parity remains required before large-scale Qlib screening of a new primitive.

### Six-gate HB_READY assessment — Scout-proposed PASS, independent audit required

1. **Determinism:** explicit two return windows, inclusive thresholds, ATR14 seed/recursion, first-edge predicate, trailing ratchet and equality/priority semantics; no ML, future extrema or hidden data.
2. **Direction:** BTC-USDT spot LONG/FLAT only; source's ONEUSDT market is explicitly changed and short disabled.
3. **Entries/exits/risk:** edge-triggered bounded dip entry; prior-high/nine-bar exit or close-only 11xATR trail; every other exit/stop behavior disabled.
4. **Position/state:** fixed 0.01 BTC, one position, 10,000 USDT ledger, no pyramiding/DCA/concurrency, full-fill pending guard, no same-bar round-trip, fresh-edge re-entry.
5. **Pinned compatibility:** directly inspected Binance Spot 1h OHLCV parser, BacktestingEngineBase tick ordering, OrderExecutor MARKET close-fill, POSITION_HOLD netting and separate quote fees; data/precision and timestamp limitations fail closed.
6. **Causality:** 120 completed-bar warmup, only t and positive historical lags, ATR recursion, prior closes/highs/open, no repainting or incomplete candle; source open timestamp normalized to completed-data availability.

**PASS frontmatter is a Scout candidate proposal, not independent certification.** Hermes Auditor must independently validate source facts, exact head, engine compatibility and all six gates before any merge.

## Evidence

### Source-reported

TradingView public page dated 2025-12-11 supplies the three percentage-window entry predicates, nine-bar-qualified prior-high primary exit, 11xATR14 trailing concept, 1h ONEUSDT scope, up-to-four pyramiding, equity sizing and 0.1% commission. It reports backtest results; those are unverified **source claims only**, not evidence for this BTC derivative.

### Independently reproduced

**None.** No source Pine execution, TradingView strategy tester replication, Qlib/Hummingbot backtest, PnL estimate, Sharpe, drawdown, OOS, Survivor or HB Certified result. The GitHub app was used to inspect the pinned Hummingbot source path only, not to run a controller or recheck installed package hashes.

### Negative evidence

Original Pine bytes/version, precise native last-two-bar expression, native ATR trail algorithm, order-fill convention and true sizing are unavailable. This record does not attribute researcher definitions to the author. No proof of historical live-fill attainability, exact exchange precision/fee tier, source-native event parity, Qlib event parity or actual profitability. The fixed-size BTC port and close-only trail can diverge materially from the author's ONEUSDT strategy.

## Falsification plan

Under separately authorized downstream work, compare the frozen signal against a manually specified prefix-only reference tape: P=-7/-5 boundary ties, R=0 tie, eligible edges across flat/long states, first 120 bars, prior-high strict versus equal, nine-bar open tie, ATR seed, trail ratchet, gap-through trail exit at **close**, dual-exit priority, missing candle, cash shortfall, fee ledger and last-bar open inventory. One representative Qlib/Hummingbot event-level parity test is required for any unverified path before large-scale screening. Failure of event or cost equivalence blocks downstream certification. None of these tests were run in this Scout cycle.

## Crypto portability

The author studied ONEUSDT 1h. This independent research variant selects BTC-USDT spot 1h solely to pin a model-supported market. The seven-coin / 1h-4h-1d campaign, BO/SO 6/6/6 and 3x/5x isolated futures are optional **downstream** experiments, not HB_READY gates. They would materially change this single-position spot derivative and require explicit new execution/cost/causality specifications.

## Limitations

A reported -5% to -7% two-bar move followed by a nonpositive recent two-bar return can represent persistent decline rather than exhaustion; no performance claim follows. The 11xATR trail can allow severe drawdown. Source Pine is uninspected and the entry-window and trail interpretations are deliberately independent. A close-only trailing signal does not protect intrabar. Historical close fills ignore adverse execution and cannot be represented as live market attainable.

## Implementation status

`not-implemented`: no controller, order router, Qlib recipe, backtest artifact or deployment was created. HB_READY research admission, if independently verified, is distinct from engineering materialization and profitability.

## Adoption boundary

`research-only`; `adoption: not-approved`; `approval_scope: research-only`. No Qlib mass screening without required representative path parity, no Paper/Testnet/Live, no capital allocation and no strategy merge without independent exact-head six-gate PASS.

## Related Wiki records

None asserted. The root strategy record is the research artifact; no extra registry, pipeline, service or folder is created.

## Sources

- TradingView primary source (Mutanabby_AI, 2025-12-11): https://www.tradingview.com/script/8I2576zL-Mutanabby-AI-ONEUSDT-MR1/
- Pinned Hummingbot source (immutable): https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting
- Canonical admission contract: https://github.com/HCH725/alpha-strategy-research/blob/9dad4fa8580f711e09f9dc3dff15cec68e5f17ea/.github/HB_READY_REVIEW.md
