---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "mcward302 VWAP SD20 upper-band breakout / VWAP cross exit — independent BTC-USDT spot 1h long-flat derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tradingview
status: research-only
confidence: medium
source_as_of: 2025-10-26
sources:
  - https://www.tradingview.com/script/1PK2hhF7-VWAP-Band-Cross-Strategy-v6/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# mcward302 session-VWAP SD20 upper breakout with VWAP midline exit — independent BTC-USDT spot 1h derivative

## Provenance

**First-party public TradingView page, read 2026-10-30:** mcward302, *VWAP & Band Cross Strategy v6*, published **2025-10-26**, stable script ID **1PK2hhF7**, URL https://www.tradingview.com/script/1PK2hhF7-VWAP-Band-Cross-Strategy-v6/ . The publication calls the script open-source and describes (a) a VWAP computed from user-selected price, default close; (b) upper/lower bands using price standard deviation over 20 periods by default with multiplier 2.0; (c) six alternative entry modes including price crossing **above the upper band** for long breakout; (d) configurable cross exits using VWAP/bands; (e) optional RSI/SMMA/MACD, day/time and daily-profit/trade-count filters, and tick/ATR/EOD exit modes. The accessible first-party page did **not** expose complete Pine source bytes, actual selected defaults for entry/exit modes, session anchor, precise standard-deviation estimator, source strategy order-processing flags, fills, fees, sizing or a source revision hash. These are **not** claimed as source-native facts.

**Explicit independent derived executable strategy v1, not a lossless Pine reproduction:** Choose exactly one of the author's disclosed entry families (long upper-band breakout) and one disclosed exit family (cross below VWAP), disable all other selectable entry/exit modes and optional filters, and specify all previously unverified implementation choices below. In particular, **researcher-defined**, not source-confirmed: Binance BTC-USDT spot UTC 1h, daily UTC-reset close-volume VWAP, population SD20 of closes, upper band VWAP+2*SD20, precise cross comparisons, 120-bar warmup, completed-bar decisions with next-completed-bar-close historical MARKET fills, one fixed 0.001 BTC unit, one-position state, hypothetical 0.1% fee each side, and no protective stops. Selecting the author's available cross modes does **not** prove they are simultaneously selected by default in Pine. All these decisions can change source trade events and belong to this independently identified derivative.

**Immutable derivative identity:** TradingView:1PK2hhF7 | mcward302 | publication:2025-10-26 | independent-derivative-v1:2026-10-30 | Binance:BTC-USDT:spot:UTC1h | UTC daily close-volume VWAP | population close-SD20 *2 upper rail | upper cross LONG, VWAP downcross FULL EXIT | t completed signal -> t+1 completed-close simulated MARKET fill | warmup 120 | Q=0.001 BTC | no stop/target/DCA | fee model 0.001 per side. Any rule, reset clock, market, timing, position, or fee-model change changes this frozen derivative identity.

**Dedup at main SHA 42708a5c90d9cdfd9d20732becfc128183d0b5ee:** GitHub Connector code search on current main found no script ID 1PK2hhF7. Open research/* PRs were enumerated; searches for 1PK2hhF7, mcward302, and VWAP band breakout found no open match. Closest admitted records: Eterna VWAP Bounce (session VWAP **fixed percentage** rails, wick-touch **reclaim** with EMA50 regime, VWAP center exit, two-sided), Garman-Klass adaptive VWMA (rolling VWMA center, OHLC-volatility-adaptive band width and **lower-band** exit), and Forven rolling-VWAP centerline cross (no dispersion rail). This derivative instead trades an **upper-band volatility breakout** of a **session-reset VWAP + rolling close SD20**, exits at the VWAP center, and has no EMA or Garman-Klass regime. It is not a mere parameter variation of those normalized rules.

## Economic mechanism

### Source-reported

The author offers both mean-reversion and trend-following VWAP/band crossing modes. An upper-band long cross is described as a trend-following breakout; a VWAP cross is an available exit mode. No independently verified performance numbers or claim of source default selection are adopted.

### Research interpretation

Test whether an hourly close newly exceeding the session's volume-weighted mean by two recent standard deviations signals persistent upward price displacement, and hold until the close crosses back below the session VWAP. Unlike a lower-band bounce, this enters **away from** the mean after expansion. No expected return, Sharpe, win rate or survivor status is asserted.

## Signal

Complete **researcher-authored derivative** rules, not a representation of unretrieved Pine bytes:

1. Use one chronological Binance BTC-USDT spot UTC 1h candle series, with real finite O/H/L/C>0, V>=0, L<=min(O,C)<=max(O,C)<=H, UTC-aligned opening timestamps T[t] spaced exactly 3600 seconds with no duplicates/gaps. Use completed candles only. An incomplete latest candle is never a decision. Any missing, invalid, zero-session-volume, synthetic or interpolated required value aborts the affected research segment; never invent a price or carry a prior VWAP across an invalid day.
2. For each completed bar t, identify UTC date D[t]=floor(T[t]/86400). Define A[t]=all bars i in the **same UTC date** with i<=t. Session VWAP W[t]=sum(C[i]*V[i] for i in A[t])/sum(V[i] for i in A[t]); the denominator must be >0. At UTC midnight start a fresh accumulator. Current bar is included **only after it completes**. This daily anchor and close source are derivative choices.
3. For t>=19, M20[t]=mean(C[t-19..t]); SD20[t]=sqrt(sum((C[i]-M20[t])^2 for i=t-19..t)/20), **population** standard deviation with divisor 20, not 19. U[t]=W[t]+2*SD20[t]; optional diagnostic lower rail LBand[t]=W[t]-2*SD20[t] does not trigger any order. Float64 indicator computation without intermediate rounding. No fitted or future statistics.
4. Long entry edge E[t]=(C[t-1]<=U[t-1]) AND (C[t]>U[t]), with both U values valid. Equality on the previous bar is allowed; equality on the current bar fails. A UTC-day boundary may legitimately change W/U and create a cross; this is **explicit derivative behavior**, not a source claim. First eligible signal t>=120 after **120 fully completed historical bars** t=0..119 used for warmup; no trading in warmup.
5. While FLAT, with no pending action and t later than the last exit-fill bar, a valid E[t] schedules one BUY of Q=Decimal("0.001") BTC at the next complete bar t+1 **actual observed close C[t+1]** in the pinned historical MARKET simulator. The decision at t must never read any t+1 value. If no t+1 full bar exists, leave the signal unfilled. Require sufficient cash, real price and valid amount/precision/trading rules; reject/abort on unsupported fills, rather than fabricate one.
6. Once a full BUY fills at bar f=t+1, set LONG, entry price C[f], Q=0.001 BTC, and one pending-order slot cleared. No exit may be decided on that fill bar; first exit decision is on completed bar u>f. While LONG, full exit edge X[u]=(C[u-1]>=W[u-1]) AND (C[u]<W[u]), using valid session VWAP for both bars; a UTC reset is permitted to participate in this cross. A valid X[u] schedules one full-quantity SELL at **the actual completed close C[u+1]** of the next full bar. Exit signals while FLAT are no-ops; entry signals while LONG or pending are ignored, never queued.
7. On full SELL fill, return to FLAT and record exit-fill bar. No same-fill-bar re-entry. Re-entry requires a **fresh** E[t] on a later completed bar; no separate time cooldown. At most one long position and one pending full-fill order, no pyramiding, DCA, safety orders, partial close, scale-in, cross-pair concurrency or shared portfolio capital. If the simulator produces a partial, duplicate, rejected, ambiguous or missing fill, abort rather than silently changing position state.
8. **Only exit is VWAP downcross.** Stop loss, take profit, trailing, time stop, opposite short entry, EOD close, daily PnL locks, daily trade limits, RSI/SMMA/MACD filters, session/day-of-week entry filters, discretionary overrides and all other source-configurable options are **disabled**. Positions may persist overnight and across multiple UTC VWAP resets. No hidden Hummingbot risk default is invoked.
9. End-of-sample: discard an unfillable pending signal; leave any still-long inventory open and separately mark it at the last real completed close. Do not invent a terminal liquidation, sell fee, realized PnL or future candle. Restarted segments begin FLAT with fresh warmup.

**Cash and cost ledger:** initial modeled cash Decimal("10000") USDT, BTC=0, spot leverage=1, no compounding. For each confirmed BUY at P, require cash>=Q*P*(1+f), then cash-=Q*P*(1+f), inventory+=Q; for SELL at S, inventory-=Q, cash+=Q*S*(1-f), with f=Decimal("0.001") per filled side. Net matched round-trip PnL=Q*(S-P)-f*Q*(P+S); fees separately logged, never label gross Hummingbot position PnL net. This 0.1% is an **explicit hypothetical research fee**, not an actual Binance tier, source commission, slippage or live cost. Funding is **not applicable** to unleveraged spot, not a fabricated zero-funding observation.

## Required data

One real, gap-free Binance BTC-USDT spot 1h OHLCV feed, UTC opening timestamps, and completed-bar availability times T[t]+3600. The session VWAP needs the date boundary and each day's actual volume; SD20 uses the trailing 20 complete closes, including prior UTC dates. At a first-hour bar after UTC midnight, W[t] is only that completed bar's volume-weighted close. No second timeframe, non-OHLCV data, order book, funding, cross-asset sync, fitted model or future extrema. Missing session volume/price fails closed. A signal at t is available **after** T[t]+3600; a modeled t+1 close fill is economically effective **after** T[t+1]+3600, never at the t+1 opening timestamp.

## Execution assumptions

**Pinned Hummingbot source inspected directly via connected GitHub app 2026-10-30:** repository HCH725/hummingbot, immutable commit **8b0e067e80ab62f10846d518dcb5a8218527ddb3**, package label **20260920**, file hummingbot/VERSION = **dev-2.17.0**. Prior independently reviewed Alpha PR #414 reports package/source byte-mapping evidence; this Scout did not rehash an installed wheel or execute a backtest.

- **Data:** hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py includes interval "1h"; binance_spot_candles.py maps Binance REST kline row[0] to opening timestamp, row[1..5] to O/H/L/C/V. BacktestingDataProvider can supply binance_BTC-USDT_1h. Before feature merge, validate real contiguous candles and timestamps: prepare_market_data's merge/dropna must not silently erase invalid rows or generate fake observations.
- **Controller path:** BacktestingEngineBase.run_backtesting accepts a controller, start/end, resolution and trade_cost; simulate_execution iterates rows, calls update_state(row), then controller.determine_executor_actions(), dispatching CreateExecutorAction with OrderExecutorConfig. A **minimal candidate-specific controller remains to be implemented** and must carry only completed t indicators/position state into row t+1 action; do not claim any existing generic controller implements this derivative.
- **Fill path:** OrderExecutorConfig connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1. In executors_simulator/order_executor_simulator.py, MARKET selects first supplied candle, uses its **actual close** as fill price, sets filled_amount_quote=Q*close and cum_fees_quote=trade_cost*notional, then closes as POSITION_HOLD. It is an idealized full-fill **historical close-price simulation**, not a claim that a post-close real market order can fill at that close. The native row timestamp is the candle **open** timestamp; the derivative's effective modeled fill time is the **close availability**, and any report must correct that semantic distinction.
- **Position/cost:** BacktestPositionHold._process_order nets opposing BUY/SELL base amounts and computes **gross** matched realized PnL; add_executor separately accumulates fees. Reconcile cash, inventory, net PnL and fees against the full executor ledger; retain terminated-executor history (terminated_executors_window=None) and final-tick flush. Reject unverified price/size precision and order validity; do not assume real exchange min-notional, liquidity, spread, partial fills, slippage or fee tier are modeled.
- **Fail closed:** BacktestingDataProvider.get_price_by_type has a Decimal("1") fallback on missing price. **Never use that fallback as a trade price**: require actual observed C and a valid feed for each action or abort. No leverage, margin, funding, liquidation, maker, next-open, intrabar stop or multi-asset engine primitive is needed for this bounded spot derivative.

**Gate 5 scope:** Verified reusable pinned-engine primitives cover one spot 1h feed, per-row controller actions, MARKET historical close fills, fee ledger and net position accounting. The dedicated signal controller, installed package identity and any future Qlib parity are not independently tested in this cycle. No claim of live execution equivalence.

## Evidence

### Source-reported

First-party TradingView publication (2025-10-26) describes selectable VWAP/band crossing modes, including upper-band long breakout, VWAP cross exits, close-price VWAP input, SD20 with 2.0 multiplier, and optional risk/time/indicator filters. It does **not** establish the derived combination as the source default or publish independently reproduced economics.

### Independently reproduced

**Not independently reproduced.** No Pine code byte-for-byte verification, Hummingbot/Qlib strategy replay, backtest, profit statistic, event-level parity, installed-wheel rehash, OOS or HB Certified result was performed. Pinned source code capability inspection is not strategy-performance reproduction.

### Negative evidence

Unavailable complete Pine bytes, source default mode selection, session anchoring, standard-deviation implementation, Pine order-fill flags and exact source economics prevent a source-native/lossless claim. This is intentionally a different independent derivative. Historical MARKET close fills may differ from live fills; spot real precision, slippage, fee tiers and latency are unverified. A VWAP exit may leave inventory exposed indefinitely in a persistent trend or across sessions.

### Six-gate HB_READY Scout proposal — independent Auditor owns decision

1. **Deterministic:** UTC daily close-volume VWAP, population SD20, exact 2x upper band, strict crossover boundaries, fixed 120-bar warmup, no fitted parameters.
2. **Direction:** one Binance BTC-USDT spot LONG/FLAT position; short/borrow explicitly disabled.
3. **Entry/exit/risk:** upper-band upward cross entry; VWAP downward cross full exit; all alternative risk/exits/filters explicitly disabled.
4. **Position/state:** fixed 0.001 BTC, one pending action, no DCA/pyramiding/concurrency, fresh cross after exit, no same-fill-bar re-entry, explicit cash/fee ledger.
5. **Pinned engine:** inspected exact 20260920/dev-2.17.0 commit for Binance spot 1h candles, controller/action, MARKET close-fill, timestamp limitation, POSITION_HOLD and fee netting; missing price and unverified real fill paths fail closed.
6. **Causality:** 120 complete warmup bars, t completed decision -> t+1 completed close modeled fill, no future candle in signals, explicit UTC reset and end-of-sample handling.

The frontmatter PASS is a **Scout research proposal only**, not independent auditor approval, profitability, Qlib parity or trading authorization.

## Falsification plan

If separately selected for downstream materialization, implement the smallest candidate-specific indicator/controller and compare hand-worked UTC midnight VWAP resets, SD20 population denominator, exact upper/VWAP crosses (including ties and reset crossings), warmup, one-order state, t+1 close timing, fees, partial/rejected-fill aborts and end-of-sample open inventory. Representative Hummingbot/Qlib event-level parity is required before broad screening of a newly unverified execution path. Failure of the declared event sequence or negative fee-net performance falsifies the respective engineering/alpha hypothesis. No tests run here.

## Crypto portability

BTC-USDT spot 1h is a declared research scope, not a market/timeframe admission whitelist. Other assets, 1d/4h, futures leverage, BO/SO/SO DCA, partial exits or different fill conventions are separate derived experiments requiring new causality/economics evidence, never silently inherited from this PASS proposal.

## Limitations

The primary page is an author description, not independently retrievable Pine bytes; this record must never be represented as source-native or a faithful TradingView backtest. The session anchor, selected modes and fill timing are disclosed research choices. No protective stop, so drawdowns are unbounded by a nominal stop threshold. Fees are hypothetical; live fill realism, Qlib implementation, OOS and Survivor certification are unverified.

## Implementation status

**not-implemented.** No candidate-specific controller, Qlib executable recipe, backtest, trading bot or deployment exists. Any future engineering handoff is separate from HB_READY admission and must use the existing pipeline, not a new admission registry.

## Adoption boundary

**status: research-only; adoption: not-approved; approval_scope: research-only.** Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. Only the existing signed webhook receiver may update the README count after an accepted merge. Scout does not approve, merge, close, deploy or trade.

## Related Wiki records

None created or modified.

## Sources

- mcward302, *VWAP & Band Cross Strategy v6*, first-party TradingView page, 2025-10-26, script 1PK2hhF7: https://www.tradingview.com/script/1PK2hhF7-VWAP-Band-Cross-Strategy-v6/
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior engine capability evidence (not this strategy's replay): https://github.com/HCH725/alpha-strategy-research/pull/414
- Canonical review contract: https://github.com/HCH725/alpha-strategy-research/blob/42708a5c90d9cdfd9d20732becfc128183d0b5ee/.github/HB_READY_REVIEW.md
