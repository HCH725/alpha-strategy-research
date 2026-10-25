---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: girishmanuja Williams %R140 armed MACD24/52/9 histogram turn SMA7-gated independent BTC-USDT spot 1d long-flat derivative
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
source_as_of: 2024-08-27
sources:
  - https://www.tradingview.com/script/975ByLQ5-Scalping-with-Williams-R-MACD-and-SMA-1m/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Williams %R140 armed MACD histogram turn with SMA7 gate — independent BTC-USDT spot 1d derivative

## Provenance

**Primary public TradingView source:** *Scalping with Williams %R, MACD, and SMA (1m)* by **girishmanuja**, published **2024-08-27**, stable script ID **975ByLQ5**: https://www.tradingview.com/script/975ByLQ5-Scalping-with-Williams-R-MACD-and-SMA-1m/ . The first-party description was directly read on **2026-10-25**. The page labels the script open-source but did **not** expose the complete Pine code in the accessible text. No original Pine revision hash, precise author initialization, order timing, or source backtest has been verified.

**Facts directly reported by the author:** the original is intended for **1-minute** trading; Williams %R length **140**; MACD fast **24**, slow **52**, signal **9**; SMA length **7**. A Williams %R cross upward through **-94** activates a buy condition, a cross upward through **-40** deactivates it; a buy is considered while the buy condition is active, Williams %R is above -94, price is above SMA7, and the MACD histogram turns positive following a negative bar. A long exits when the MACD histogram turns negative and is below its previous bar. The source also describes a **short/sell** arm (-6, -60) and short trades; those are **not** implemented here. These are source-description facts, not a claim to have reproduced the inaccessible Pine implementation.

**Explicit independent derivative, NOT source-native/lossless:** this record changes the original **1-minute** horizon to **BTC-USDT Binance spot 1d UTC**; disables the original short leg; pins EMA initialization, precise strict crossover/equality behavior, arming/deactivation precedence, state reset after entry/exit, a 200-completed-bar warmup, completed-close decision and modeled same-row MARKET close fill, fixed 0.001 BTC sizing, 10,000 USDT initial unborrowed cash, a 0.1% per-side *assumed research* fee, invalid-data handling, and all otherwise unspecified exit/risk behavior. The original description does not prove these researcher choices. This is a new fully specified derivative with different trade events and economics, **not** a parameter-tuned copy or an adaptation secretly attributed to girishmanuja.

**Immutable derivative identity:** `TV:975ByLQ5 | girishmanuja:2024-08-27 | independent-derived-v1-WPR140-arm-94-disarm-40-MACD-EMA24-52-9-hist-turn-SMA7 | BinanceSpot:BTC-USDT:1d:LONG-FLAT:0.001BTC:close-MARKET | 2026-10-25`. Any change to timeframe, arming logic, oscillator, fee, fill, sizing, entry/exit or state creates a different research identity.

## Economic mechanism

**Source-reported:** the author combines an oversold Williams %R recovery with a MACD histogram transition and SMA price trend filter to seek long momentum after a pullback. The author also describes a separate short side, not used in this derivative.

**Research interpretation (unproven):** an armed oversold recovery that is not already above the -40 deactivation threshold, followed by a fresh negative-to-positive MACD histogram transition above SMA7, might capture a limited rebound. An opposite histogram sign transition closes exposure. The daily timeframe and all fills/costs are researcher choices. No return, Sharpe, win rate, or survivor status is asserted.

## Signal

**Input and clock:** exactly one Binance **spot** BTC-USDT UTC **1d** candle stream, `(open_time,O,H,L,C,V)`, strictly contiguous 86400-second opening timestamps. `open_time` is the exchange candle-open Unix timestamp; a completed candle becomes available only at `open_time+86400`. Compute and act only after that completion. Require finite positive O/H/L/C, H >= max(O,C), L <= min(O,C), finite nonnegative V, and valid strictly increasing timestamps. No forward fill, synthetic open/close, higher-timeframe peeking, or missing-price substitution.

**Researcher-pinned indicator mathematics:**

1. `HH140[t] = max(H[t-139..t])`; `LL140[t] = min(L[t-139..t])`. For `HH140>LL140`, `W[t] = -100*(HH140[t]-C[t])/(HH140[t]-LL140[t])`. If the denominator is zero, the indicator is invalid and the data-gap rule below applies. No future highs/lows.
2. `SMA7[t] = (C[t]+...+C[t-6])/7`.
3. For `n=24,52`, `E_n[n-1] = mean(C[0..n-1])`; for `t>=n`, `E_n[t] = (2/(n+1))*C[t] + (1-2/(n+1))*E_n[t-1]`. Earlier values undefined. `M[t]=E24[t]-E52[t]` exists from index 51. The 9-bar EMA signal `G[59]=mean(M[51..59])`, then `G[t]=0.2*M[t]+0.8*G[t-1]` for t>=60. `Hist[t]=M[t]-G[t]`. These seeds are **researcher-defined**, not asserted as the inaccessible Pine's internal initialization.
4. Cross-up of Williams %R through a level `L`: `W[t-1]<=L && W[t]>L`. Thus `ARM[t]` is cross-up through **-94**, and `DISARM[t]` is cross-up through **-40**. Current equality does not count as a cross. `HistUp[t] = Hist[t-1]<0 && Hist[t]>0`; `HistDown[t] = Hist[t-1]>=0 && Hist[t]<0 && Hist[t]<Hist[t-1]`. Zero histogram at the current bar does not trigger. The `HistDown` extra comparison explicitly preserves the author's “below previous histogram bar” description.
5. Maintain `position in {FLAT,LONG}` and `buy_armed in {false,true}`; initialize `FLAT,false`. After **200 contiguous valid fully completed bars**, on each bar t apply the following priority **exactly once**:
   - If `LONG`: if `HistDown[t]`, model one full `SELL` of 0.001 BTC, set `FLAT,false`; otherwise HOLD. Ignore new arm signals while LONG. Never exit and re-enter on the same bar.
   - If `FLAT`: first apply `ARM[t]` to set `buy_armed=true`; next apply `DISARM[t]` to set `buy_armed=false` (**disarm wins** on a single large W%R jump); then if `buy_armed && W[t]>-94 && C[t]>SMA7[t] && HistUp[t]`, place one `BUY` of 0.001 BTC **only if affordable**, set `LONG,false`. If unaffordable, skip that signal and clear `buy_armed` until a fresh ARM. Otherwise remain FLAT and preserve the armed flag until DISARM or entry. No implicit expiry. On an exit, re-arming requires a **later** fresh -94 cross; no same-bar reversal.
   - The short-side -6/-60 signals are deliberately disabled and never place an order. No partial-fill retry or speculative state transition is inferred from an absent fill.
6. **Explicitly disabled:** short selling, futures/perpetuals, leverage, borrowing, maker/limit/next-open/intrabar execution, stop-loss, take-profit, trailing stop, timed exit, forced end-of-data liquidation, pyramiding, BO/SO/DCA, averaging, compounding, concurrent positions, cross-pair capital sharing, discretionary exits, or any hidden Hummingbot default risk order. No stop is a deliberate research risk.
7. **Invalid/missing candles:** stop the run as **data-incomplete** if any candle is missing, duplicated, malformed, out-of-order, or any required indicator is undefined after warmup. Do not fabricate a fill, silently drop a row, or sell an existing LONG at an invented price. A restarted independent run must establish 200 new contiguous valid completed bars and a fresh FLAT state; a historical gap cannot be bridged with a fabricated holding return. A pending position makes the interrupted run non-claimable.

## Required data

One real Binance BTC-USDT **spot** 1d OHLCV feed and its UTC opening timestamps. At time t, all indicators use only candles `0..t`. No order book, ML model, funding, mark/index price, cross-asset input, multi-timeframe alignment, pivot confirmation, or future extrema. Source's 1-minute market is **not** claimed to have been reproduced; this 1d variant is explicitly independent.

## Execution assumptions — actual pinned Hummingbot model

**Pinned research engine:** Hummingbot policy package **20260920**, VERSION **dev-2.17.0**, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Previous independently merged [Alpha PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414) records a 902/902 wheel/source Python-file match and wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`; this Scout did **not** rehash the installed wheel. In this cycle the following real source paths were directly inspected at the pinned commit, not inferred from a feature list:

- **Feed/data:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly maps `1d`; `binance_spot_candles.py::_parse_rest_candles` maps Binance open timestamp `row[0]` and OHLCV `row[1..5]`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::prepare_market_data` exposes `open_bt/high_bt/low_bt/close_bt/volume_bt` plus unsuffixed fields. Its `dropna` is **not** proof of data continuity; the derivative requires a pre-engine continuity/validity check so that missing bars cannot be hidden.
- **Controller/executor:** the pinned `BacktestingEngineBase.simulate_execution` iterates processed rows, invokes `update_state(row)` then `controller.determine_executor_actions()` and routes `CreateExecutorAction` to `OrderExecutorSimulator`. The pinned `OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A dedicated strategy controller/recipe is **not yet implemented**. Controller memory must use fill-confirmed position/arm state, not infer immediate flatness from lagged ledger snapshots.
- **Real fill and clock semantics:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` MARKET execution selects the **first supplied row**, uses that row's `close` as `entry_price`, records `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, and returns `CloseType.POSITION_HOLD`. The engine's raw timestamp is the candle **opening label**; the economic decision and modeled fill effective time are **opening label + 86400 seconds**. This is the simulator's same-close convention, **not** a claim of executable live post-close market fills. Do not relabel a next-open fill as same-close or fabricate missing prices.
- **Position and costs:** `BacktestPositionHold._process_order` nets opposite-side base quantities and realizes **gross** quote PnL; executor fees are accumulated separately. Use `Q=0.001 BTC`, starting unborrowed cash `10000 USDT`, no other positions, and an **assumed research fee** `trade_cost=0.001` of filled quote on **each** buy/sell. A BUY is affordable only if `cash >= Q*C[t]*(1+0.001)`. On BUY debit `Q*C[t]*(1+0.001)`; on SELL credit `Q*C[t]*(1-0.001)`. `net_roundtrip_pnl = Q*(sell_close-buy_close)-0.001*Q*(buy_close+sell_close)`. While LONG, mark cash plus `Q*last_valid_close` without inventing a hypothetical sell; an open position is **not** automatically liquidated at the end. Spot funding is **not applicable**, not a zero-perpetual-funding assumption.
- **Boundaries:** simulator MARKET fills are full-quantity, single-close synthetic fills. Real exchange fee tiers, spreads, latency, slippage, depth, partial fills, lot/tick minimums and production precision are **not verified**. No CEX slippage path is inferred from unrelated Gateway-only `slippage_pct` fields. No live cost/fill guarantee or HB Certified status is claimed. The bounded spot 1d controller/executor/candle/position path is a previously reviewed primitive, not a claim that this particular strategy has been backtested.

## HB_READY six-gate evidence — Scout proposal, not independent verdict

1. **Determinism:** full Williams %R140, SMA7, seeded EMA24/52/9 MACD histogram formula, exact strict crossings, arm/disarm precedence, 200-bar warmup and fail-closed data rules.
2. **Direction:** one Binance BTC-USDT spot LONG/FLAT position; original short side explicitly disabled as a derivative.
3. **Entry/exit/risk:** armed oversold recovery + positive histogram turn + SMA7 price filter enters; negative histogram turn exits; all stop/target/trailing/time behaviors explicitly disabled.
4. **Position/re-entry:** one fixed 0.001 BTC unit, 10,000 USDT cash affordability, no DCA/BO/SO/pyramiding/concurrency, full exit and later fresh re-arm only, zero cooldown.
5. **Pinned real Hummingbot path:** package/source binding evidence, inspected 1d Binance spot feed, real controller/OrderExecutor MARKET close fill, netted position ledger, fee and timestamp normalization; explicit noncanonical execution/cost limitations.
6. **Causality:** 200 completed contiguous daily candles, only present/past observations, previous-bar sign and level crossing, UTC close-effective timing, no lookahead or gap substitution.

## Evidence

### Source-reported

The 2024-08-27 TradingView publication by girishmanuja specifies Williams %R140 thresholds -94/-40 for the long arm, MACD24/52/9 histogram sign transition, SMA7 price filter, and a long histogram-negative exit. It also describes a 1-minute timeframe and short rules; the 1d LONG/FLAT derivative intentionally does **not** claim original event parity. No source performance table or source trading cost is adopted.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, original Pine code comparison, live order, testnet/paper trade, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation.

### Negative evidence and deduplication

At initial and pre-write GitHub snapshots `main@0257cd6eb25bab85ab1ab1dcb301c67ea8bcbc1e`, the root Git tree contained **325** strategy Markdown records, matching README's static **325** count; count agreement is **not** a substitute for independently checking every existing record's PASS frontmatter. GitHub code search for `975ByLQ5` and PR searches for the same ID/author returned no matches. Ten open `research/*` PRs were inspected for source overlap and none used this script or materially identical W%R-arm + MACD-histogram + SMA7 mechanism. Existing `williams-r-level-cross-mean-reversion-long-btcusdt-1d-2026-10-09.md` uses Julien_Exe's distinct W%R14 -80/-20 unarmed level-cross mechanism without MACD/SMA; existing Forven Williams+ADX is a separate source and filter. This derivative adds a **stateful W%R140 arm/disarm plus MACD24/52/9 histogram sign-transition gate and SMA7**, a materially different mechanism, not a trivial length/threshold variation.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen arm/disarm + histogram gate to a pure W%R140 level-cross baseline and to a no-arm histogram/SMA7 baseline on identical contiguous BTC-USDT 1d data with the same declared costs. Check missed-arm and gap events and the sensitivity to researcher-defined disarm priority. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance spot 1d** only. The original author described a 1-minute strategy; daily adaptation may materially change event frequency and behavior. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

Complete Pine code/version was not readable; author-side signal persistence, tie ordering, EMA initialization, order-fill semantics and risk defaults cannot be verified losslessly. All such decisions are independently frozen above, never attributed to the source. The daily horizon and disabled short leg materially change the original. Same-bar-close simulated fills are not achievable live-price guarantees. Real spread/slippage/fees/precision are unverified. A no-stop long may have unbounded holding time and substantial drawdown. Package/source binding cites an earlier independent review rather than a fresh wheel hash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- TradingView primary: girishmanuja, *Scalping with Williams %R, MACD, and SMA (1m)*, 2024-08-27, https://www.tradingview.com/script/975ByLQ5-Scalping-with-Williams-R-MACD-and-SMA-1m/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
