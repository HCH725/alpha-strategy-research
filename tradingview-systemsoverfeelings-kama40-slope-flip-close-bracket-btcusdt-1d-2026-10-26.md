---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "SystemsOverFeelings KAMA40 normalized-slope flip with 6%/3% close bracket — independently derived BTC-USDT spot 1d long-flat"
created: 2026-10-26
updated: 2026-10-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-11-29
sources:
  - https://www.tradingview.com/script/P3fyKd3i-KAMA-Flip-strategy/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SystemsOverFeelings KAMA40 normalized-slope flip with 6%/3% close bracket — independently derived BTC-USDT spot 1d long-flat

## Provenance

**Primary TradingView source:** [KAMA Flip strategy](https://www.tradingview.com/script/P3fyKd3i-KAMA-Flip-strategy/) by **SystemsOverFeelings**, publicly published **2025-11-29**, stable script ID **P3fyKd3i**; public description directly inspected **2026-10-26**. TradingView labels the script open-source, but its full Pine code, Pine version, revision hash, execution settings, and parameter defaults were **not retrieved** in this inspection. Do not mistake the open-source label for inspection of its Pine instructions or a frozen source-code hash.

**Source-native facts actually visible:** The author describes a KAMA-based normalized zero-line momentum oscillator: positive denotes upward momentum, negative downward; a flip provides direction. The author describes a full-position fixed-percent stop and target, no scaling or trailing, selectable long/short/both directions, and a personal **BTC daily** configuration of **40 lookback, 6% stop-loss, 3% take-profit**. The public description does not specify the exact oscillator normalization, KAMA seeding, fast/slow constants, order-fill bar, stop/target trigger price, same-bar precedence, fees, or capital. Those are not silently attributed to the original Pine.

**Independent derived strategy, not lossless reproduction:** This research record deliberately selects BTC-USDT **Binance spot 1d LONG/FLAT**, KAMA(40) with explicit ER(40), fast=2/slow=30, SMA40 seed, normalized *KAMA slope* oscillator, strict negative-to-positive sign-flip entry, close-only 6%-stop/3%-target exit, a fixed 0.001 BTC unit, 10,000 USDT cash, completed-bar close-fill simulation, 80-bar warmup, fixed research fees, and exact state/error handling. The oscillator formula, close-only bracket, single-sided direction, market/venue, size, warmup, cost and fill convention are **researcher-authored choices**, not verified source-native code. The source's 40/6%/3% values are explicitly reported by the author as preferred BTC daily settings; their exact Pine implementation is not asserted. Any alternate normalization, default, intrabar bracket or opposite-flip exit would be a **different** strategy.

**Immutable research identity:** `TV:P3fyKd3i | author:SystemsOverFeelings | published:2025-11-29 | derived-spec:v1:2026-10-26 | ER40 fast2 slow30 SMA40 seed | normalized KAMA slope zero flip | BTC-USDT Binance spot 1d long-flat | close-only 6%-SL/3%-TP | 0.001 BTC | 80-bar warmup`. This identity pins the **derived rules**, not the unseen Pine bytes. No TradingView performance is adopted as reproduced.

**Dedup on main SHA `2808ab10d311471a08ba41dab42ba99eb50420b2`:** GitHub connector code search returned no `P3fyKd3i` or `SystemsOverFeelings` source record, and open-PR searches returned no matching source or KAMA PR. Nearest main cousin `kama-efficiency-ratio-adaptive-trend-two-sided-btcusdt-1d-2026-10-11.md` uses **HPotter's different TV source KVMbvcHV**, KAMA21 with 0.666/0.0645 ends and a `close[t-1]` versus `KAMA[t]` **two-sided always-in-position** state, no stop/target. This candidate instead trades the **sign flip of KAMA40's own normalized first difference**, only long/flat, with fixed full-position bracket exits and no automatic short reversal. Distinct source, lookback, signal construction, direction, and exit/state transitions; not a parameter-only duplicate. The open PR list was checked before writing; search index completeness and unseen private code are not claimed.

## Economic mechanism

### Source-reported

A noise-adaptive KAMA trend estimate is converted to a zero-centered momentum signal. Its sign change is intended to identify a direction change; a fixed stop and target bound the trade's modeled price move. The author's public text suggests 40 lookback, 6% stop and 3% target on BTC daily, without publishing independently reproducible results in the material inspected.

### Research interpretation

This **derived** long-only test asks whether a KAMA slope turning positive after a negative regime captures a sustained trend often enough for a 3%-upside versus 6%-downside full-position close-bracket to have positive *net* expectancy. A bracket can exit while the oscillator remains positive; re-entry then requires a new negative-to-positive flip, preventing same-regime repeated buys. Neither profitability nor source-equivalent trade events are assumed.

## Signal

All arithmetic and tie rules below are **derived-spec v1** and frozen, not claims about the unseen Pine.

1. Input is a strictly increasing, contiguous sequence of finite, positive **completed UTC daily** Binance BTC-USDT spot closes `C[t]`, zero-based bar index `t`. Decimal precision is preserved for order/accounting; indicator arithmetic uses deterministic float64 in chronological order without lookahead or whole-sample fitting.
2. Seed `KAMA[39] = mean(C[0], ..., C[39])` exactly. For each `t >= 40`, define `change[t] = abs(C[t] - C[t-40])`, `noise[t] = sum(abs(C[j] - C[j-1]) for j=t-39..t)`, `ER[t] = change[t]/noise[t]` when `noise[t] > 0`, else `ER[t] = 0`. Define `fastSC = 2/(2+1)`, `slowSC = 2/(30+1)`, `SC[t] = (ER[t]*(fastSC-slowSC)+slowSC)^2`; `KAMA[t] = KAMA[t-1] + SC[t]*(C[t]-KAMA[t-1])`. No other smoothing or preprocessing.
3. Derived normalized oscillator: `O[t] = 100*(KAMA[t]-KAMA[t-1])/KAMA[t-1]` for `t >= 40`. Since valid closes and the SMA seed are strictly positive, KAMA remains positive. `sign[t]` is +1 when `O[t] > 0`, -1 when `O[t] < 0`, 0 on exact zero. Zero does not change the last **nonzero** sign. No tolerance/epsilon, interpolation, z-scoring or adaptive threshold.
4. Bars `t=0..79` (the first **80 completed** daily candles) are **no-trade warmup**. Calculate KAMA/O as available and seed `last_nonzero_sign` using `t=40..79`; do not create a historical position. The first eligible decision is completed bar `t=80`. If the sign is positive with no prior observed negative sign, do **not** enter merely because it is positive.
5. At each eligible completed bar, first examine an **already filled LONG** position: let `P` be its actual modeled entry close-fill price, `SL = P*0.94`, `TP = P*1.03`. If `C[t] <= SL`, emit one full SELL at `C[t]` (**STOP**). Else if `C[t] >= TP`, emit one full SELL at `C[t]` (**TARGET**). Equality triggers the relevant exit. The stop check has formal priority, although a single valid close cannot be at both positive-price thresholds. Do **not** execute an oscillator-triggered exit; a sign reversal during LONG is ignored for orders. No intrabar high/low threshold fill or resting stop/limit is represented.
6. If FLAT, emit BUY **only** when the last nonzero oscillator sign **before** the current bar was -1 and the current sign is +1. A zero plateau preserves the last nonzero sign, so negative→zero(s)→positive is a valid single flip. Flat + negative flip is no-op. After any SELL, **do not BUY on that same bar**, even if a positive flip also occurs; only a subsequent genuine negative-to-positive flip may re-enter. Update the sign memory after processing the bar, regardless of action.
7. A fill is one modeled MARKET close-price action, never a signal-time assumption of a real exchange fill. No same-bar round-trip. No signal while data invalid, pending order, or unavailable price; a failed/rejected action leaves the filled ledger unchanged. A skipped BUY is not queued and cannot be filled on a later bar without a fresh valid flip.

**Trade direction and complete risk posture:** Binance BTC-USDT **spot**, LONG or FLAT only; no shorts, borrow, futures, leverage, margin, hedge, multi-market exposure or cross-pair synchronization. No pyramiding, DCA, safety orders, partial exits, scaling, trailing, time exit, volatility stop, opposite-signal exit, compounding, end-of-sample forced liquidation or discretionary override. The fixed 6%/3% close-bracket is the only exit. This is **not** an intrabar stop-loss protection claim.

**State and sizing:** Initial cash **10,000 USDT**, initial inventory zero. BUY one fixed **0.001 BTC** if FLAT and `cash >= 0.001*C[t]*(1+0.001)`; debit actual modeled notional plus fee on successful fill. Otherwise skip with no borrowing or phantom position. SELL the full **actually filled** 0.001 BTC only when LONG; credit sale notional minus fee. Keep a single FLAT/LONG state, oscillator sign memory, one in-flight action flag, entry fill price, filled BTC quantity, quote cash and fee ledger. An unfilled/rejected action does not change exposure. No cooldown beyond the strict fresh-flip rule. Mark any terminal open position using the final *observed* close, reporting unrealized value separately.

## Required data

- Only completed BTC-USDT Binance spot **UTC 1d** OHLCV rows; the derived signal and bracket read `close`, with open-time timestamps and OHLCV integrity used to validate feed completeness. No volume-based signal, multi-timeframe join, external model, order-book, mark/index, funding, on-chain or other data requirement.
- Raw candle open timestamps must increase by exactly **86400 seconds**, with unique bars, no gaps/duplicates/partial last bar. Binance kline `timestamp` is the **bar open** `T[t]`; completed-close decision becomes available only at `E[t]=T[t]+86400 seconds`. Preserve both timestamps; never label a close-based decision as known at `T[t]`.
- Validate raw rows **before** any engine feature join/`dropna`. Any missing candle, non-finite/zero/negative close, invalid chronological order or unavailable fill price invalidates the research segment; fail closed rather than forward-fill, interpolate, fabricate a close, or silently skip an unseen flip. A later restart requires a new contiguous 80-bar warmup with flat state.
- Prefix-only KAMA recurrence, 80-bar warmup and sign memory; no future extrema, negative shifts, repainting, full-sample normalization or incomplete higher-timeframe bars. Close-fill is an explicitly **simulated research convention**; a real order sent at `E[t]` cannot be promised the just-finished `C[t]`.

## Execution assumptions

**Pinned engine:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, source commit `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The VERSION and relevant source files below were **read via the connected GitHub app in this Scout cycle**. Package/wheel-to-commit byte correspondence is **inherited evidence** from the earlier independent PR #414 audit (not independently rehashed in this cycle); the immutable source commit is the inspected model. A newer build cannot silently substitute.

- **Data feed:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` maps `1d`; `binance_spot_candles.py` parses Binance REST kline row[0] as seconds **open time** and row[4] as close. The derived controller must suppress incomplete bars and reject gaps *before* `BacktestingEngineBase.prepare_market_data()`, which uses `get_candles_df`, `merge_asof` where applicable and `dropna`. This is a single supported feed; no extrapolation to other market models.
- **Controller and executor:** A not-yet-implemented dedicated deterministic controller may compute the frozen KAMA40/O state on completed rows. `BacktestingEngineBase.simulate_execution()` iterates rows, updates state, calls `determine_executor_actions()`, and simulates `CreateExecutorAction`. Use `OrderExecutorConfig` with `connector_name=binance`, `trading_pair=BTC-USDT`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`; a SELL reduces an existing spot long rather than opening a short. There is **no** claim that a production controller already exists.
- **Fill and timestamps:** `OrderExecutorSimulator.simulate()` MARKET branch chooses the first supplied candle and fills at its `close`, recording `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*notional`, then `CloseType.POSITION_HOLD`. Its `timestamp` is inherited from candle open time, so downstream research event time must explicitly be `E[t]`, not raw `T[t]`. Bracket checks are controller-side **completed-close** predicates producing MARKET SELL actions; no unsupported intrabar stop/limit executor or assumed threshold-price fill is used.
- **Position and cost:** `BacktestPositionHold._process_order()` nets opposite-side amounts, maintains average entry cost and **gross** realized PnL; `add_executor()` aggregates per-side fees. Net realized quote PnL must subtract both BUY and SELL `cum_fees_quote` from gross. Fixed `trade_cost=0.001` **per filled side** (0.1% of quote notional) is a disclosed, reproducible **research assumption**, not a live Binance fee quote or source-author claim. Track cash debits/credits and inventory separately; the engine's gross PnL alone is not net return. **Spot funding is not applicable**, not a zero-funded perpetual assumption. Simulator does not prove real slippage/spread/latency/partial-fill/precision/lot/min-notional economics: no additional simulated slippage is a limitation, not observed zero. Reject unsupported amounts in any later production adaptation.
- **Ledger ordering:** `update_state()` refreshes executor info and position holds before the current decision; a newly created order is not automatically in the controller's pre-action `positions_held`. Reconcile actual simulated fill/position-hold on the next update and at final flush, and use the in-flight flag to prevent duplicate actions. Set `terminated_executors_window=None` or retain an explicit authoritative fill ledger; the default 3600-second controller view can prune a daily-bar fill before the next decision. Never infer a missing fill from a missing history-window entry.
- **Model boundary:** This is a source-inspected *backtest expressibility* path for one spot pair, close-price MARKET fills and modeled quote fees. It is **not** evidence of real order execution at the just-finished close, real protective stop fills, Qlib parity, Paper/Testnet/Live readiness, or actual exchange fee/precision support.

### Six-gate HB_READY evidence — Scout proposal, not independent approval

1. **Deterministic:** exact ER40/KAMA recurrence, SMA seed, fast2/slow30, normalized-slope formula, zero ties, strict flips, 80-bar warmup, missing-data behavior and no hidden fitted model.
2. **Direction:** explicit spot LONG/FLAT; all short/borrow/reversal paths disabled.
3. **Entry/exit/risk:** fresh -1→+1 oscillator flip BUY; only completed-close <=94% or >=103% of filled entry price SELL; complete priority, disabled opposite exits/trailing/time/intrabar stops and no same-bar round-trip.
4. **Position state:** 0.001 BTC, 10,000 USDT, cash/fee/inventory ledger, one in-flight action, no DCA/pyramiding/concurrency/cooldown, fresh-flip re-entry and failed-fill semantics.
5. **Pinned engine:** inspected exact commit's Binance spot 1d feed, CreateExecutorAction/OrderExecutor MARKET close fill, POSITION_HOLD netting, per-side quote fees and timestamp caveat; model-vs-real economics and package-byte audit inheritance explicitly separated.
6. **Causality:** only completed contiguous prefix data, 80-bar no-trade seed, open-time to close-time correction, no future or partial-bar signal, and explicit same-close simulation convention.

The frontmatter `PASS` is a **proposed** six-gate admission status subject to **independent Hermes Auditor exact-head review**; no Scout self-approval, profit claim or merge authorization follows.

## Evidence

### Source-reported

TradingView `P3fyKd3i`, SystemsOverFeelings, 2025-11-29: public description of normalized zero-line KAMA momentum flip, fixed-percent full exit, no scaling/trailing, selectable direction, and preferred BTC daily 40-lookback/6%-SL/3%-TP. The precise Pine source was not retrieved, and none of the derived mathematical/execution pins is represented as a quotation from it.

### Independently reproduced

**Not independently reproduced.** No TradingView strategy backtest, Qlib/Hummingbot run, event-level parity, net return, Sharpe, drawdown, win rate, or fill statistics were produced. This cycle inspected the pinned Hummingbot *source code* for model compatibility only.

### Negative evidence

No inspected Pine code, no verified original indicator formula, no verified original intrabar stop/target execution, no verified original order-fill timing, no exchange fee/funding schedule, no wheel-byte rehash this cycle, no controller implementation, no representative Qlib/Hummingbot event-level parity and no observed trading fills. These gaps **do not get invented**: they distinguish the independently complete derived model from source-native equivalence and from downstream implementation/trading approval.

## Falsification plan

After a separate approved implementation/capability handoff (not in this Scout cycle), verify one representative sequence of KAMA sign flips, stop/target close exits, cash/fee ledger updates, skipped buys and UTC decision/fill timestamps between Qlib and the pinned Hummingbot model before large-scale Qlib screening on this execution path. Compare net expectancy with a fixed EMA40-slope sign-flip control under identical close-bracket and costs; negative net expectancy or unexplained event divergence falsifies the research hypothesis. No performance test was run here.

## Crypto portability

Only the **derived** BTC-USDT spot 1d model is pinned. Other symbols, timeframes, leveraged perpetuals, funding, DCA BO/SO overlays, or intrabar protective stops are separate research/execution variants requiring their own verified path and declared economic model; none is an HB_READY entry prerequisite.

## Limitations

The author's full Pine is not inspected; this is not lossless original reproduction. Close-only bracket exits can realize worse than -6% or better than +3% on a daily gap and are not protective exchange stop orders. Same-completed-close MARKET fills are a simulator accounting convention unavailable as a guaranteed live fill. Precision, partial fills, slippage, spread and latency are unverified. Fixed costs are hypothetical research assumptions; no profitability or Qlib parity is established.

## Implementation status

`not-implemented`: this Markdown is a reproducible research specification, not a controller, Qlib executable recipe, or deployed trading strategy. A later selected strategy may require minimal strategy-specific implementation and one representative capability/parity check; this does not create a second admission status.

## Adoption boundary

`status: research-only`; `adoption: not-approved`; `approval_scope: research-only`. Only an independent six-gate PASS review may merge the exact reviewed PR head to the PASS-only `main` pool. No backtest, Paper, Testnet, Live, trading authorization, survivor or HB Certified status is implied. Existing signed webhook receiver alone owns README count reconciliation after a verified merge.

## Related Wiki records

None linked or modified. The existing HPotter KAMA21 source record above is a **different** strategy, not a shared strategy identity.

## Sources

- TradingView primary public page: https://www.tradingview.com/script/P3fyKd3i-KAMA-Flip-strategy/ (SystemsOverFeelings, published 2025-11-29, inspected 2026-10-26).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (VERSION, Binance spot candle feed, BacktestingEngineBase, OrderExecutorSimulator, OrderExecutorConfig).
- Repository's live admission policy: `README.md` and `.github/HB_READY_REVIEW.md` at main SHA `2808ab10d311471a08ba41dab42ba99eb50420b2`.
