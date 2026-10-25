---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Tr0sT Holy Grail ADX28-gated WMA11-straddle trigger-bar breakout independent BTC-USDT spot 1d long-flat derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2018-07-24
sources:
  - https://www.tradingview.com/script/emQdbShi-Linda-Raschke-s-Holy-Grail/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Tr0sT Holy Grail ADX28-gated WMA11-straddle trigger-bar breakout — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Primary public TradingView source:** *Linda Raschke's Holy Grail* — **Strategy by Tr0sT**, published **2018-05-25**, updated **2018-07-24**, stable script ID **emQdbShi**: https://www.tradingview.com/script/emQdbShi-Linda-Raschke-s-Holy-Grail/ . The page was directly read in a real browser session on **2026-10-25** (page live, `OPEN-SOURCE SCRIPT`, ~150-line `//@version=3` Pine block fully visible in the `Source code` tab). Page tags: ADX, Exponential Moving Average (EMA), raschke, stoploss, strategy, takeprofit. The author's own description line: `[a]nother script based on Linda Raschke's strategy with the same name from her book about swing trading` — lineage to Raschke/Connors *Street Smarts* is the author's attribution, not an independent verification of the book text by this Scout.

**Facts directly read from the author's Pine code (long side only; short side mirrored in source and disabled here):** `adxlen=18`, `adxMin=28`, `useAdx=true`, `maLength=11`, trend source default `"wma"` (options ema/sma/rma/wma), `highPeriod=34`. The ADX block is a custom `dirmov`/`adx` pair built on Wilder `rma` smoothing with `dilen=adxlen`. A long stop order is armed only when **all** hold: `adx>28`, `low<curMA`, `high>curMA`, `curMA>curMA[17]`, `curMA>curMA[34]`, and `highest(high,34)>high`; the order is `strategy.order("Long", strategy.long, stop=high)` with `strategy.exit` limit `highest(high,34)` and stop `f_lowest(low, barssince(low>=curMA))`. Pending orders are cancelled when `adx<=28` or `high<curMA`. No original Pine revision hash, no author backtest window, and no source performance table were found on the page.

**Explicit independent derivative, NOT source-native/lossless:** this record pins the source-default WMA11/ADX18/28/34 construction and the straddle-plus-slope arming logic, but changes the intrabar stop-entry into a completed-close decision with a modeled same-row MARKET close fill, drops the intrabar limit/stop take-profit/stop-loss legs (the pinned MARKET-only path cannot model them — see Execution assumptions), replaces position exits with the source's own close-evaluated cancel condition (`adx<=28` or `high<MA`), disables the mirrored short leg, and pins BTC-USDT Binance spot 1d, fixed 0.001 BTC sizing, 10,000 USDT cash, a 0.1% per-side *assumed research* fee, a 200-completed-bar warmup, and fail-closed data handling. The source trades any symbol/timeframe with 100%-of-equity sizing and a 0.07 commission parameter; none of that is carried over. This is a new fully specified derivative with different trade events and economics, **not** a parameter-tuned copy or an adaptation secretly attributed to Tr0sT.

**Immutable derivative identity:** `TV:emQdbShi | Tr0sT:2018-07-24 | independent-derived-v1-ADX18gt28-WMA11-straddle-slope17-34-HH34filter-nextbar-triggerH | BinanceSpot:BTC-USDT:1d:LONG-FLAT:0.001BTC:close-MARKET | 2026-10-25`. Any change to timeframe, lengths, thresholds, trigger/cancel semantics, fee, fill, sizing, or exit creates a different research identity.

## Economic mechanism

### Source-reported

The author claims only book lineage (Raschke swing-trading pullback continuation): wait for ADX-confirmed trend strength, let price straddle a short average with a rising slope, then buy the break of the setup bar's high with a highest-high target and a lowest-since-touch stop. No behavioural channel, no performance number, and no market-selection claim appear on the page.

### Research interpretation

Trend-continuation participation with a pullback-timing filter, long-only, state-holding. ADX18 above 28 requires measurable trend strength so range chop cannot arm entries; the WMA11 straddle (`low<MA<high`) requires sellers to have actually pressed price into the average; the dual-slope condition (`MA>MA[17]` and `MA>MA[34]`) requires the average itself to be rising on two horizons so entries do not trigger under a flat or rolling average; the 34-bar-high filter requires headroom above the current high. The trigger-bar breakout times the entry to trend resumption; the ADX/price cancel pair surrenders the unit when strength fades or price slips fully under the average. No return, Sharpe, win rate, or survivor status is asserted.

## Signal

**Input and clock:** exactly one Binance **spot** BTC-USDT UTC **1d** candle stream, `(open_time,O,H,L,C,V)`, strictly contiguous 86400-second opening timestamps. `open_time` is the exchange candle-open Unix timestamp; a completed candle becomes available only at `open_time+86400`. Compute and act only after that completion. Require finite positive O/H/L/C, H >= max(O,C), L <= min(O,C), finite nonnegative V, and valid strictly increasing timestamps. No forward fill, synthetic open/close, higher-timeframe peeking, or missing-price substitution.

**Researcher-pinned indicator mathematics (source-default lengths, Pine-rma-equivalent seeding):**

1. `W[t] = sum_{k=0..10} (11-k)*C[t-k] / 66` (WMA11, weights sum 66). Undefined for `t<10`.
2. For `t>=1`: `TR[t]=max(H[t]-L[t],|H[t]-C[t-1]|,|L[t]-C[t-1]|)`; `up[t]=H[t]-H[t-1]`; `dn[t]=L[t-1]-L[t]`; `pDM[t]=up[t]` if `up[t]>dn[t] and up[t]>0` else `0`; `mDM[t]=dn[t]` if `dn[t]>up[t] and dn[t]>0` else `0`. This mirrors the source `dirmov` block exactly, including strict comparisons.
3. Wilder-RMA with Pine-equivalent seeding (**researcher-defined**, matching Pine `rma` semantics where the first smoothed value is the simple mean): for any series `x` first defined at index `a` with length `n=18`, `R[a+17]=mean(x[a..a+17])`, then `R[t]=(x[t]+17*R[t-1])/18` for `t>a+17`. Apply to `TR` (gives `ATR`), `pDM` (gives `P`), `mDM` (gives `M`), each first defined at `t=18`.
4. `pDI[t]=100*P[t]/ATR[t]`; `mDI[t]=100*M[t]/ATR[t]`. If `ATR[t]==0` the data-gap rule below applies (no division by zero, no invented value).
5. `r[t]=|pDI[t]-mDI[t]| / ((pDI[t]+mDI[t])==0 ? 1 : (pDI[t]+mDI[t]))` — the `sum==0?1:sum` guard is the source's own line, yielding `r=0` on a zero-sum bar.
6. `ADX[t]=100*RMA18(r)` (first defined at `t=35`). `HH34[t]=max(H[t-33..t])` for `t>=33`.
7. `Setup(t) = ADX[t]>28 && L[t]<W[t] && H[t]>W[t] && W[t]>W[t-17] && W[t]>W[t-34] && HH34[t]>H[t]`. `Cancel(t) = ADX[t]<=28 || H[t]<W[t]`. `Setup(t)` implies `not Cancel(t)` by construction (strict `H[t]>W[t]` contradicts `H[t]<W[t]`; `ADX[t]>28` contradicts `ADX[t]<=28`) — no same-bar cancel/arm conflict is possible.
8. Maintain `position in {FLAT,LONG}` and pending trigger `P in {none} ∪ price`; initialize `FLAT,none`. After **200 contiguous valid fully completed bars**, on each bar `t` apply **exactly once**:
   - If `LONG`: if `Cancel(t)`, model one full `SELL` of 0.001 BTC, set `FLAT,none`; otherwise HOLD. Ignore setups and triggers while LONG. Never exit and re-enter on the same bar.
   - If `FLAT`: first, if `Cancel(t)`, set `P=none`. Else, if `Setup(t)`, set `P=H[t]` (a setup bar arms but **never fills on itself** — fills begin on the next completed bar at the earliest; a later setup bar overwrites `P` with its own high). Else, if `P` was set on an **earlier** bar and `H[t]>=P`, place one `BUY` of 0.001 BTC **only if affordable**, set `LONG,none`. If unaffordable, skip that signal and set `P=none`. Otherwise remain FLAT and preserve `P`. Pending triggers never expire by time — they end only by fill, cancel, overwrite, or exit — because the source specifies no validity window (a multi-bar window would be a different, unpinned rule).
9. **Explicitly disabled:** the mirrored short leg; the source's intrabar `strategy.exit` limit (`highest(high,34)`) and stop (`f_lowest` since touch) legs; trailing stops; take-profit targets; timed exits; forced end-of-data liquidation; pyramiding; BO/SO/DCA; averaging; compounding; concurrent positions; cross-pair capital sharing; maker/limit/next-open/intrabar execution; discretionary exits; the source's 100%-of-equity sizing and 0.07 commission parameter; or any hidden Hummingbot default risk order. No stop is a deliberate research risk.
10. **Invalid/missing candles:** stop the run as **data-incomplete** if any candle is missing, duplicated, malformed, out-of-order, non-finite, or any required indicator is undefined after warmup. Do not fabricate a fill, silently drop a row, reset position state mid-run, or sell an existing LONG at an invented price. A pending position makes the interrupted run non-claimable. A restarted independent run must establish 200 new contiguous valid completed bars and a fresh FLAT/none state; a historical gap cannot be bridged with a fabricated holding return.

## Required data

One real Binance BTC-USDT **spot** 1d OHLCV feed and its UTC opening timestamps. At time t, all indicators use only candles `0..t`. Volume is validity-checked but never signal-forming (no formula reads V). No order book, ML model, funding, mark/index price, cross-asset input, multi-timeframe alignment, or future extrema. The source's any-symbol/any-timeframe prose is **not** claimed to have been reproduced; this 1d BTC-USDT variant is explicitly independent.

## Execution assumptions — actual pinned Hummingbot model

**Pinned research engine:** Hummingbot policy package **20260920**, VERSION **dev-2.17.0**, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Previously merged [Alpha PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414) records a 902/902 wheel/source Python-file match and wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`; this Scout did **not** rehash the installed wheel. In this cycle the following real source paths were directly read at the pinned commit via the local checkout (`8b0e067` verified present by `git cat-file` and confirmed ancestor of the working tree), not inferred from a feature list:

- **Feed/data:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly maps `1d` in `INTERVALS`; `binance_spot_candles.py::_parse_rest_candles` maps Binance open timestamp `row[0]` and OHLCV `row[1..5]`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::prepare_market_data` exposes `open_bt/high_bt/low_bt/close_bt/volume_bt` plus unsuffixed fields with a `dropna`; its `dropna` is **not** proof of data continuity — the derivative requires a pre-engine continuity/validity check so that missing bars cannot be hidden.
- **Controller/executor:** the pinned `BacktestingEngineBase.simulate_execution` iterates processed rows, invokes `update_state(row)` then `controller.determine_executor_actions()` and routes `CreateExecutorAction` to `OrderExecutorSimulator`. The pinned `OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A dedicated strategy controller/recipe is **not yet implemented**.
- **Real fill and clock semantics:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` MARKET execution fills at the **first supplied row**, uses that row's `close` as `entry_price`, records `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, and returns `CloseType.POSITION_HOLD`. The engine's raw timestamp is the candle **opening label**; the economic decision and modeled fill effective time are **opening label + 86400 seconds**. This is the simulator's same-close convention, **not** a claim of executable live post-close market fills. The source's intrabar stop-entry (`stop=high`) and limit/stop exit legs are **not** modeled — their omission is the central disclosed execution adaptation. Do not relabel a stop/limit fill as same-close MARKET or fabricate missing prices.
- **Position and costs:** `BacktestPositionHold` (defined in `backtesting_engine_base.py`) nets opposite-side base quantities and realizes **gross** quote PnL; executor fees are accumulated separately. Use `Q=0.001 BTC`, starting unborrowed cash `10000 USDT`, no other positions, and an **assumed research fee** `trade_cost=0.001` of filled quote on **each** buy/sell. A BUY is affordable only if `cash >= Q*C[t]*(1+0.001)`. On BUY debit `Q*C[t]*(1+0.001)`; on SELL credit `Q*C[t]*(1-0.001)`. `net_roundtrip_pnl = Q*(sell_close-buy_close)-0.001*Q*(buy_close+sell_close)`. While LONG, mark cash plus `Q*last_valid_close` without inventing a hypothetical sell; an open position is **not** automatically liquidated at the end. Spot funding is **not applicable**, not a zero-perpetual-funding assumption.
- **Boundaries:** simulator MARKET fills are full-quantity, single-close synthetic fills. Real exchange fee tiers, spreads, latency, slippage, depth, partial fills, lot/tick minimums and production precision are **not verified**. No CEX slippage path is inferred from unrelated Gateway-only `slippage_pct` fields. No live cost/fill guarantee or HB Certified status is claimed. The bounded spot 1d controller/executor/candle/position path reuses previously reviewed primitives (no stop/limit/trailing/next-open/intrabar leg is introduced), not a claim that this particular strategy has been backtested.

## Evidence

### Source-reported

The 2018-05-25 (updated 2018-07-24) TradingView publication by Tr0sT (`emQdbShi`) pins ADX length 18 with threshold 28, WMA length 11 as default trend source, 34-bar highest-high filter and dual average-slope gates, a stop-entry at the setup bar's high, limit/stop exit legs, and pending-order cancellation on `adx<=28` or `high<MA`. It describes both long and short sides; this derivative implements the long side only. No source performance table, trade count, date range, or trading cost is adopted.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, Pine-code execution comparison, live order, testnet/paper trade, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation.

### Negative evidence and deduplication

At the pre-write snapshot `main@c35e1f75b043a7e3597fea99b44b7ac8da13884c`, the root Git tree contained **326** strategy Markdown records, matching README's static **326** count; count agreement is **not** a substitute for independently checking every existing record's PASS frontmatter. Working-tree search for `emQdbShi`, `uzair`, and `holy.grail` returns no record using this script identity or setup name (the sole same-author hit is `ehlers-cyber-cycle-signal-self-cross-loss-escape-two-sided-btcusdt-1d-2026-10-15.md`, built on Tr0sT's different `yrCo4RtN` Ehlers-cycle script — different source, indicator, and mechanism). A same-day namesake page (*Holy Grail by Linda Bradford Raschke* by `uzair2join`, script ID `ptU0vveI`) returned TradingView `Publication not found` when opened in the same browser session and is therefore **not** used. Ten open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) were inspected for source overlap; none uses this script or an ADX28/WMA11-straddle/trigger-breakout mechanism (the nearest, #331 AdxSmas, is an ADX-gated SMA3/6 cross — different construction). Pool ADX cousins are fenced as different mechanisms: `adx-di-cross-strength-gated-two-sided` fires on a ±DI cross (cross, not straddle-breakout); `forven-adx-trend-di-cross` and `freqtrade-adx-momentum-di-gated` are DI-cross systems; `forven-adx-trend-pulse-reclaim` is a four-way EMA55-trend × ADX≥18 × 4-bar-touch × EMA21-reclaim-cross system with a close-under-EMA/ADX-gate exit pair (this record: ADX>28 straddle with dual WMA-slope gates, next-bar trigger-high breakout entry, pure ADX/price-cancel exit, no reclaim cross, no slow-EMA regime — different entry, exit, thresholds, and source). This is a materially different signal construction, not a trivial length/threshold variation.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen straddle-plus-slope trigger rule against (a) a slope-gates-off baseline (straddle + ADX gate only) and (b) a trigger-off baseline (enter at next close after any setup bar) on identical contiguous BTC-USDT 1d data with the same declared costs; check missed-trigger and gap-interruption event rates and sensitivity to the `HH34>high` headroom filter. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance spot 1d** only. The source describes a swing-trading setup for any trending symbol/timeframe; daily crypto adaptation with target/stop legs removed may materially change event frequency, holding time, and drawdown behavior. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

Pine `rma` seeding, EMA/SMA/RMA/WMA initialization, and order-fill semantics inside the inaccessible backtester are pinned here by researcher rule, never attributed to the source. The source's intrabar stop-entry and limit/stop take-profit/stop-loss legs are deliberately not modeled; the replacement close-based exit (the source's own cancel pair) holds positions through adverse intrabar moves the original legs would have cut — drawdown and whipsaw profiles differ materially. The trigger-high breakout may fill far above the setup close on gapping bars. Pending triggers never expire by time, so a stale trigger can fire long after the setup bar. A no-stop long held until regime invalidation may have unbounded holding time and substantial drawdown. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- TradingView primary: Tr0sT, *Linda Raschke's Holy Grail*, 2018-05-25 (updated 2018-07-24), https://www.tradingview.com/script/emQdbShi-Linda-Raschke-s-Holy-Grail/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
