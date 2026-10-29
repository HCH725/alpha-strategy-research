---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TRW_meir triple SuperTrend 10/11/12 RSI7 Fibonacci BB close-exit BTC spot long-flat — independent derivative"
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
  - derived
status: research-only
confidence: medium
source_as_of: 2026-10-29
sources:
  - https://www.tradingview.com/script/jw3P5XtU-Triple-SuperTrend-RSI-Fib-BB/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Triple SuperTrend + RSI7 + Fibonacci BB close-exit — independent long-flat research derivative

## Provenance

**Primary public source:** TradingView open-source **indicator** page *Triple SuperTrend + RSI + Fib BB*, author **TRW_meir**, published **2025-10-13**, stable script identity **jw3P5XtU**, inspected **2026-10-29**: https://www.tradingview.com/script/jw3P5XtU-Triple-SuperTrend-RSI-Fib-BB/ . The page describes a trading strategy, but its listing is an indicator; do not claim its published artifact is a verified executable Pine `strategy()`. Complete Pine bytes and revision hash were **not** available in the public page text. No Pine order execution or original TradingView backtest is independently verified.

**Source-native facts, as described by the author:** three SuperTrend instances with ATR periods/multipliers (10,1.0), (11,2.0), (12,3.0); RSI7 >50 for bullish confirmation and <50 for bearish; Fibonacci Bollinger SMA200 with 2.618 population-standard-deviation-style band concept (exact variance convention is not provided by the page); entry at first simultaneous directional alignment; exit on any SuperTrend color change or Fibonacci band touch. The author describes both long and short setups, no-repainting intent, and one signal per setup. The page does not pin SuperTrend initial-state/ATR variant, RSI seeding, BB touch price, order timing, venue, size, or cost.

**EXPLICIT INDEPENDENT DERIVATIVE; NOT source-native/lossless.** Researcher pins Binance BTC-USDT spot UTC 1h; disables shorts; fixes Wilder ATR/RSI seeds, deterministic SuperTrend band/state recurrence, population BB standard deviation, long-only **completed CLOSE >= upper BB** exit rather than ambiguous high/low band touch; retains exit on *any* SuperTrend bearish change; adds explicit one-setup latch, 250-bar warmup, no intrabar stops, 0.001 BTC size, 10,000 USDT cash, 0.1% hypothetical fee per side, and next-completed-candle-close MARKET simulation. All of these are researcher rules, not alleged source facts. Disabling shorts and replacing band touches/author order execution can materially alter trade events and risk.

**Frozen identity:** `TV:jw3P5XtU:TRW_meir:2025-10-13 | derived-v1:2026-10-29 | BinanceSpot:BTC-USDT:UTC1h | ST(10,1.0)(11,2.0)(12,3.0):WilderTR:RMA-seeded:finalband-recursion | RSI7:Wilder:>50 | BB200:population:upper=2.618sigma | qualified-false-to-true-entry | exit:any-ST-bear-or-close>=upperBB | LONG-FLAT:Q0.001BTC:cash10000USDT | signal-E[t]:fill-next-E[t+1]-MARKET-row-close | fee0.001:W250:no-DCA:no-short`. Any change to this identity is a different derivative.

**Dedup (prewrite, main `a78de72445e8768878421df87bba5a1580fc8a92`):** GitHub code search for exact `jw3P5XtU` and all-state PR searches for the script ID and title returned no result. The nontruncated main tree listed 437 root-level strategy records and README count 437; 18 distributed frontmatter spot checks returned PASS (not an exhaustive independent audit). Open `research/*` PRs were inspected; none references this source. Existing SuperTrend flip/RSI/EMA, Fibonacci retracement, and triple-EMA variants do **not** implement this source's three distinct SuperTrend periods with a first-alignment RSI7 latch and upper Fibonacci-BB alternative exit. Not a trivial parameter retune.

## Economic mechanism
### Source-reported
Three differently reactive trend bands require directional consensus, RSI7 confirms momentum, and the 200-bar Fibonacci BB signals statistical price extension; the author does not provide independently verified expectancy, exchange costs or execution trace.
### Research interpretation
An all-three-bullish regime transition with RSI7>50 may reduce isolated trend-flip noise; the upper-BB close exit takes profit on statistically extended moves. Without a protective stop, a long can sustain severe losses; the exit is **not** a guaranteed stop or live fill.

## Signal

**Gate 1 — deterministic data and preprocessing.** One Binance BTC-USDT Spot UTC `1h` series indexed t=0,1,... by Binance candle **opening** timestamp T[t], with T[t+1]-T[t]=3600 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C), finite V>=0, strictly ordered unique complete candles; reject gaps, duplicates, incomplete bars, forward fills, missing prices, bad precision and synthetic data. Completed bar t is available only at E[t]=T[t]+3600. Compute float64 features in chronological order; no model fitting or external feeds.

**ATR / three derived SuperTrend states:** for each n in {10,11,12}, TR[0]=H[0]-L[0]; for t>=1, TR[t]=max(H[t]-L[t],abs(H[t]-C[t-1]),abs(L[t]-C[t-1])). ATR_n is undefined for t<n-1, ATR_n[n-1]=mean(TR[0..n-1]); for t>=n, ATR_n[t]=((n-1)*ATR_n[t-1]+TR[t])/n. Set M[t]=(H[t]+L[t])/2, raw lower L0[t]=M[t]-mult*ATR_n[t], raw upper U0[t]=M[t]+mult*ATR_n[t], with mult=1,2,3 for n=10,11,12 respectively. At seed t=n-1: final lower Lf=L0, upper Uf=U0, state BULL if C[t]>=M[t], else BEAR (researcher-defined initialization). At t>=n, recursively set Lf[t]=L0[t] if L0[t]>Lf[t-1] OR C[t-1]<Lf[t-1], else Lf[t-1]; Uf[t]=U0[t] if U0[t]<Uf[t-1] OR C[t-1]>Uf[t-1], else Uf[t-1]. If prior state BULL, current state becomes BEAR only when C[t]<Lf[t]; otherwise stays BULL. If prior state BEAR, current state becomes BULL only when C[t]>Uf[t]; otherwise stays BEAR. Equality never flips. This is the **declared derivative's** SuperTrend, not an unverified claim about TradingView `ta.supertrend` internals.

**RSI7:** delta[t]=C[t]-C[t-1], gain=max(delta,0), loss=max(-delta,0). Seed Wilder average gains/losses at t=7 from deltas 1..7; thereafter update G[t]=(6*G[t-1]+gain[t])/7, L similarly. RSI=100-100/(1+G/L); if L=0 and G>0 =>100; G=0 and L>0 =>0; both zero =>50. Undefined t<7.

**Fibonacci BB:** at t>=199, SMA200[t]=mean(C[t-199..t]), sigma[t]=sqrt(mean((C[i]-SMA200[t])^2 over i=t-199..t)), **population** divisor 200, upper[t]=SMA200[t]+2.618*sigma[t]. Includes the current *completed* bar; no forward shift. Only upper band matters to this long-only derivative.

**Entry setup edge:** qualified[t] = (all three states BULL at completed t) AND RSI7[t]>50. Eligible LONG entry at t>=250 only if FLAT, no pending action, qualified[t] true and qualified[t-1] false. The false->true transition is consumed even if entry is impossible; no repeated entry while qualified stays true. Source's "first bar where all conditions align" is implemented as this explicit derived latch.

**Exit:** while LONG and only on a bar strictly after the confirmed entry fill bar, if **any** of the three SuperTrend states is BEAR OR C[t]>=upper[t], queue SELL. Exit checks level-state (not just a new flip) to avoid ignoring a bearish state after entry. If both exit predicates hold, classify as `ST_EXIT` before `BB_EXIT`; only one full SELL. RSI is an entry-only gate. Lower BB, wick-touch, profit target, stop-loss, trailing stop, time exit, and forced terminal sale are **disabled**. No automatic reversal.

## Required data

Only the one complete Binance Spot 1h OHLCV stream, with validated actual closes for every decision, fill and mark. Require 250 uninterrupted completed bars before any signal; first eligible signal t=250, so 200-bar BB, ATR12 and RSI7 have initialized. No order-book, external funding, higher-timeframe, multi-asset or fitted inputs.

## Execution assumptions

**Gates 2–4:** unleveraged Binance Spot BTC-USDT LONG/FLAT; shorts, margin, perpetuals and borrowing disabled. One fixed BUY/SELL of Decimal("0.001") BTC, initial 10,000 USDT, initial zero BTC; single position and single pending action; no DCA, safety orders, pyramiding, compounding, simultaneous orders, partial planned exits, cooldown, extra stops/targets or hedges. State `FLAT -> BUY_PENDING -> LONG -> SELL_PENDING -> FLAT`. Pending actions suppress all fresh signals. Re-entry requires a **new** qualified false->true edge on a later eligible completed bar after full SELL confirmation. Failed, missing, partial, duplicate or precision-invalid fills abort research rather than silently assuming execution; SELL failure retains LONG and latched exit intent and retries only against the next real complete row. No cash shortage allowed; if the BUY's actual quote cost exceeds cash, abort. If no next complete row exists, the pending action remains unfilled; mark any held BTC at last verified close, never fabricate a terminal exit.

**Historical event clock:** detect signal only after completed t at E[t]; latch action; on completed t+1, use pinned Hummingbot OrderExecutor `MARKET` simulator's **first supplied row's actual close C[t+1]** as modeled fill price. Emit controller action on t+1 using only t's latched decision; never emit on signal bar t. Raw Binance and engine row timestamps are **opening** T[t+1]; keep that raw value and separately annotate economic completion/fill-availability E[t+1]=T[t+1]+3600. This is a historical close-price simulator convention, **not** a claim of live achievable fill at the candle close or actual timestamped exchange trade. Entry fill bar cannot trigger exit; exit fill bar cannot trigger entry.

**Hypothetical costs/accounting:** trade_cost=0.001 per filled side of quote notional, not an observed Binance fee; no fabricated funding or spread/slippage measurement. BUY at P requires 0.001*P*(1.001) USDT and adds 0.001 BTC; SELL at S removes 0.001 BTC and credits 0.001*S*(0.999) USDT. Net matched PnL = 0.001*(S-P)-0.001*0.001*(P+S). Reconcile confirmed executor fills and separate fee ledger with quote cash and base inventory; never present gross PnL as net. Spot has no perpetual funding/margin/liquidation leg. Unmodeled market impact, real slippage, latency and partial fills are limitations, **not measured zero**.

## Evidence
### Source-reported
Primary TradingView page directly states three ATR/multiplier pairs, RSI7 threshold, BB200/2.618, first-alignment entries, any-SuperTrend-change or BB-touch exits, both original sides and no-repainting intent. The full original Pine code was not retrieved, so the above deterministic implementation is explicitly derived. No source-reported returns adopted.
### Independently reproduced
**No backtest or Qlib/Hummingbot run performed.** Gate 5 **static pinned-source inspection**, via connected GitHub only: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, `hummingbot/VERSION=dev-2.17.0` (blob `fa1dd206a0e288710d6d68e195d4f030960fc6fb`); package baseline `20260920` per Alpha contract. Wheel/source mapping is previously evidenced in Alpha PR #414, **not independently rehashed in this cycle**; if installed package differs, the engine compatibility claim must be revalidated before use.

- `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` blob `6d505dff42b60b356931df13eeeecd1e28b426f9`: `1h` in Binance Spot interval list, `/api/v3/klines`. `binance_spot_candles.py` blob `5d0c938af574aca5f8dcba5ba28121797eae4dd0`: row[0] opening timestamp, row[1..5] OHLC/base volume. One-stream OHLCV is sufficient, but interval listing alone is **not** execution proof.
- `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` blob `7d1e552dd7ee62df4f83f10950b8d593cd1106e6`: prepared rows call `update_state(row)`, then `controller.determine_executor_actions()`, then `simulate_executor(action.executor_config, processed_features.loc[i:max_ts],trade_cost)`. A strategy-specific ControllerV2 must carry the prior completed-bar signal into the next row, not rely on a generic strategy API name. `BacktestPositionHold` accumulates gross matched PnL and fees separately; `terminated_executors_window=None` or equivalent persistent fill ledger required to prevent losing position history.
- `hummingbot/strategy_v2/executors/order_executor/data_types.py` blob `67715e3d14a1edf636defa95a7bbe5c73b8cff90`: `OrderExecutorConfig` supports connector `binance`, trading pair `BTC-USDT`, BUY/SELL, Decimal amount, OPEN/CLOSE, MARKET and leverage 1. `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` blob `3b4e82e91896db9074295ca2a8a087dde2499eab`: MARKET fills at first supplied **row close**, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*amount*close`, terminates as POSITION_HOLD. These are modeled fills, not actual exchange fills.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` blob `e3d3e087b4da7c0381fac9621d1a04dcb8de81cf`: `get_price_by_type` may return `Decimal("1")` for absent price. This derivative **forbids** that fallback for any fill/mark and aborts if no validated real close is available. Validate actual initialized Binance trading rules (lot size, min notional, precision) before simulation; reject instead of silently changing 0.001 BTC. The pinned engine's `dropna` preparation must not conceal raw data gaps; validate continuity first.
### Negative evidence
No original Pine byte-for-byte comparison, actual fee schedule, real fill/latency, wheel rehash, live stop behavior, Qlib parity or performance reproduction. In particular, author-described band **touch** is not equivalent to the derived completed-close upper-band exit. This is an admission **proposal** pending independent Auditor, not proof of source-native equivalence or live readiness.

## Falsification plan

Independent Auditor must verify first-party publication/date and distinguish author facts from derived choices; recalculate a few synthetic 10/11/12 ATR SuperTrend state transitions, Wilder RSI7 and population BB200 edge cases; inspect exact completed-bar event ordering, fill timestamps, ledger, fees, abort behavior and no future leakage. Before any mass Qlib screening of a new execution path, obtain one representative Hummingbot↔Qlib event-level parity proof. Then use later IS/OOS for profitability, not as an HB_READY entry gate.

## Crypto portability

All indicators use relative price and normalized oscillator geometry, not SPY session calendars; only Binance BTC-USDT spot 1h is claimed here. Porting to other symbols, futures or intervals is a new explicitly pinned research identity, not silently assumed.

## Limitations

No exchange-native stop, target or liquidation protection; next-complete-close exit can be much worse than band or trend-change price. The author's original short side and wick-touch semantics are excluded. Unobserved real trading costs, no live implementation, no independent return estimates, and no verified original Pine revision. No invented zero funding or zero slippage. Historical Survivor/Qlib profitability is not inferred from HB_READY PASS.

## Implementation status

`not-implemented`: strategy-specific controller/ledger is specified but not deployed. Static Gate 5 compatibility is a bounded claim under the pinned source/previous wheel mapping; independent Hermes Auditor owns exact-head admission review. No Hummingbot/Qlib backtest, deployment or trading performed.

## Adoption boundary

`research-only`, `adoption: not-approved`, `approval_scope: research-only`. PASS frontmatter is a Scout six-gate admission claim awaiting independent review, **not** HB Certified, Qlib parity, profitability, or Paper/Testnet/Live authorization.

## Related Wiki records

None asserted; similar SuperTrend/RSI and triple-EMA families on main use materially different state and exit constructions.

## Sources

- TRW_meir, *Triple SuperTrend + RSI + Fib BB*, TradingView public open-source indicator, 2025-10-13, stable ID jw3P5XtU: https://www.tradingview.com/script/jw3P5XtU-Triple-SuperTrend-RSI-Fib-BB/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Alpha contract: `README.md` and `.github/HB_READY_REVIEW.md` on main SHA `a78de72445e8768878421df87bba5a1580fc8a92`.
