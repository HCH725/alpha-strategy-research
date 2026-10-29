---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "SwiftEdge Supertrend10/Keltner20/EMA100 simultaneous breakout, spot long-flat, explicit derivative v1"
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
source_as_of: 2025-05-03
sources:
  - https://www.tradingview.com/script/hkpsp4so-QuantumTrend-SwiftEdge/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SwiftEdge simultaneous Supertrend/Keltner breakout with EMA100 — independently specified long-flat derivative v1

## Provenance

**Primary source:** SwiftEdge, *QuantumTrend SwiftEdge*, TradingView public open-source **indicator** (not a ready-to-trade order strategy), stable script ID `hkpsp4so`, published **2025-05-02**, updated **2025-05-03**; first-party page inspected **2026-10-30**: https://www.tradingview.com/script/hkpsp4so-QuantumTrend-SwiftEdge/ . Its public description explicitly identifies a bullish event as **close above EMA100 + upward Keltner upper-band crossover + Supertrend bearish-to-bullish flip**, with the converse bearish event, and states default sensitivity-3 parameters **Supertrend ATR10 ×3, Keltner EMA20 ±1.5×ATR10, EMA100**. Its adaptive sensitivity (1–5), visual gradient and ATR-based line visibility are additional source features. Full original Pine bytes, revision hash, exact initialization, order execution and strategy risk rules were **not** accessible in this research; no source-native losslessness or original performance reproduction is claimed.

**Independent executable derivative, not a reconstruction of source-native orders:** freeze the six published default indicator numbers as manually fixed constants, **disable adaptive sensitivity** and non-decision visual effects, independently define all Wilder/EMA seeds, Supertrend band recursion and crossing boundaries, and translate the described *bullish* indicator event into a spot LONG entry. The source's *bearish* triple-confluence event is **not** treated as a source-native exit; the researcher explicitly introduces earlier exits on Supertrend bearish flip, Keltner midline down-cross, or a 5% **completed-close** adverse threshold, plus fixed size, next-completed-close historical MARKET fills, fees, pending states and no-DCA. These exits, market/timeframe, timing and 5% risk trigger are **researcher-designed changes**, not facts asserted about the original Pine script. This record evaluates only the derivative's expressibility.

**Frozen identity:** `TV:hkpsp4so|SwiftEdge|public-description-2025-05-03|independent-derivative-v1-20261030|binance-spot-BTC-USDT-UTC1h|ST-WilderATR10x3-initial-down|KC-EMA20-WilderATR10x1.5|EMA100|simultaneous-bullish-flip-upper-cross|exit-close5pct-or-ST-down-or-KCmid-crossdown|t-to-t+1-completed-close-MARKET|Q0.001BTC-cash10000USDT-fee0.001|warmup150|no-DCA`. Changes to any rule, seed, market, exit, timing or cost define a different derivative.

**Dedup snapshot:** GitHub `main` commit `e7e1a8282c161fe424597d0f3557b15994b96c11`, untruncated tree **447** root-level strategy records; README static count **447**. Nineteen distributed frontmatter checks returned PASS (not an exhaustive 447-record status census). GitHub code search for `hkpsp4so` and `QuantumTrend SwiftEdge` found no main record; open research PR search for those identities found none, and the open `research/*` PR titles/sources did not show this mechanism. Existing Keltner/ADX breakout, squeeze/EMA100, and standalone Supertrend records do not use this **same-bar joint Supertrend-flip + Keltner-upper crossover + EMA100** entry event. This is a bounded semantic comparison, not a guarantee of all possible duplicates.

## Economic mechanism

### Source-reported

The source combines trend regime (EMA100), volatility-channel breakout (Keltner), and ATR-based trend-state reversal (Supertrend) to seek confirmed momentum entries. Its published 2025-05-03 default numbers are frozen, but original Pine signal/fill parity is **not** asserted.

### Research interpretation

The hypothesis is that a **single completed candle** simultaneously flipping Supertrend upward and closing through the upper Keltner band above EMA100 marks an unusually decisive regime transition. Researcher-defined exits cut exposure when trend reverses, price falls through Keltner center, or the completed close falls 5% below actual modeled entry fill. This is an untested hypothesis; no Sharpe, ROI, win rate or survivor claim.

## Signal

**Candle index and validation:** t=0,1,... on Binance BTC-USDT spot UTC-aligned **1h** candles. Observed open timestamp T[t] must increase exactly 3600 seconds; E[t]=T[t]+3600 is the earliest completed-candle decision time. Require actual finite positive O,H,L,C, H≥max(O,C), L≤min(O,C), H≥L, finite nonnegative base volume, no duplicate, gap, incomplete, out-of-order or fabricated candle. Abort on a malformed/missing interior bar, indicator nonfinite result or invalid timestamp; no forward fill or synthetic fill prices. Use float64 chronological indicator arithmetic, without interim rounding.

**True range and Wilder ATR10:** TR[0]=H[0]-L[0]; for t≥1, TR[t]=max(H[t]-L[t], abs(H[t]-C[t-1]), abs(L[t]-C[t-1])). ATR10 first valid at t=9 as mean(TR[0..9]); for t≥10, ATR10[t]=(9×ATR10[t-1]+TR[t])/10. Before t=9, ATR and Supertrend are unavailable.

**EMA20 and EMA100:** for n∈{20,100}, EMA_n first valid at t=n-1 as arithmetic mean(C[0..n-1]); later EMA_n[t]=(2/(n+1))×C[t]+(1-2/(n+1))×EMA_n[t-1]. No incomplete-window EMA values or alternate seeding. Keltner center K[t]=EMA20[t]; upper U[t]=K[t]+1.5×ATR10[t]; lower D[t]=K[t]-1.5×ATR10[t]. First valid K/U/D is t=19. This derivative uses Wilder ATR10, not a TR SMA or an unpinned TradingView Keltner variant.

**Supertrend, explicitly researcher-defined:** for t≥9 set midpoint M[t]=(H[t]+L[t])/2, basic upper BU[t]=M[t]+3×ATR10[t], basic lower BL[t]=M[t]-3×ATR10[t]. At t=9, final upper FU[9]=BU[9], final lower FL[9]=BL[9], and direction ST[9]=DOWN (a **researcher-defined** initial condition). For t≥10:
- FU[t]=BU[t] if BU[t]<FU[t-1] OR C[t-1]>FU[t-1]; otherwise FU[t-1].
- FL[t]=BL[t] if BL[t]>FL[t-1] OR C[t-1]<FL[t-1]; otherwise FL[t-1].
- If ST[t-1]=DOWN, ST[t]=UP exactly when C[t]>FU[t], else DOWN.
- If ST[t-1]=UP, ST[t]=DOWN exactly when C[t]<FL[t], else UP.
Equality does not flip. The opposite band is maintained in both states. This fully specifies the derivative; no claim is made that the inaccessible original Pine initializes or updates identically.

**ENTRY[t] on a fully completed candle t≥150:** all conditions must be true **on the same t**, not within a loose lookback: (i) ST[t-1]=DOWN and ST[t]=UP; (ii) C[t-1]≤U[t-1] and C[t]>U[t] (strict Keltner upper close-cross); (iii) C[t]>EMA100[t]; (iv) state FLAT, no pending action. No upper-band intrabar touch, incomplete candle, prior-bar lookahead, volume confirmation or delayed reuse of a stale flip.

**EXIT[t] while LONG, after entry fill bar:** in descending priority (1) completed close C[t]≤0.95×P_entry (researcher 5% adverse trigger, **not** an exchange stop or guaranteed loss cap); (2) ST[t-1]=UP and ST[t]=DOWN; (3) C[t-1]≥K[t-1] and C[t]<K[t] (Keltner center down-cross). One full exit only even if multiple conditions hold. No original bearish triple-confirmation requirement for exit. A fixed profit target, trailing stop, intrabar stop, other exit or forced terminal liquidation is **disabled**.

**Warmup/causality:** first 150 **completed** contiguous bars t=0..149 are indicator-only, initial FLAT, no inherited position. First decision t=150; EMA100 starts t=99 and ATR/ST start t=9, with all recursions running chronologically. Decisions only at E[t], using ≤t completed data. No future extrema, repaint, request.security, ML fit, lookahead, full-sample optimization or next-bar price in signal formation.

## Required data

One historical feed: pinned Hummingbot Binance spot `binance`, pair `BTC-USDT`, interval `1h`, actual contiguous UTC OHLCV. Required fields are open timestamp, O/H/L/C and base volume (volume validates rows but does not filter trades). No multi-asset capital sharing, futures marks/funding, external sentiment, higher-timeframe aggregation or unverified intrabar feed. Every modeled fill must use an **observed** actual close; absent prices are fatal, never defaulted.

## Execution assumptions

**States:** FLAT → PENDING_BUY → LONG → PENDING_SELL → FLAT. Start 10,000 USDT cash and zero BTC. One market, one full position Q=Decimal("0.001") BTC, at most one pending order; no pyramiding, averaging, DCA, safety orders, partial fills, shorts, leverage, margin, funding, compounding, simultaneous exposure, discretionary actions or hidden cooldown. Explicit full-fill reconciliation is required.

- At ENTRY[t] observed at E[t], latch one pending BUY. **Only at the next observed completed bar t+1** submit a historical MARKET BUY to the simulator's actual close C[t+1], economically timestamped E[t+1]. Require cash≥Q×C[t+1]×1.001; otherwise abort. Upon confirmed full fill, cash -=Q×P×1.001, BTC +=Q, freeze P_entry=P. Do not evaluate exits on the BUY fill bar.
- For each later completed t, evaluate EXIT[t]. On trigger, latch one full MARKET SELL for next observed completed t+1; fill at actual C[t+1], economically effective E[t+1]. On confirmed full fill, BTC -=Q, cash +=Q×P×0.999, reconcile realized gross and fees. Ignore any ENTRY on SELL fill bar. Re-entry requires a **new** same-bar triple event on a later completed candle, not a remembered signal or already-UP state.
- A missing next bar at the predetermined sample end means an unfilled pending action, **not** an invented last-close fill. Open LONG remains marked to last **observed** close without forced liquidation. Any missing interior row, failed/partial fill, unresolved fee/quantity, negative cash, or inconsistent position state aborts the run rather than fabricating success.
- Research cost: hypothetical **0.001 quote fee per filled side**, passed as `trade_cost=0.001`. Round-trip quote PnL is Q×(sellPrice-buyPrice)-0.001×Q×(buyPrice+sellPrice). This is **not** a verified Binance fee tier; simulator MARKET fills idealize close, not live executable post-close prices. No modeled spread, impact or slippage is **not** evidence of zero realized costs. Spot has no perpetual funding; no futures funding or liquidation claim.

## Evidence

### Source-reported

SwiftEdge first-party TradingView page (2025-05-02; update 2025-05-03) gives the exact three-component bullish/bearish indicator logic and default ST10×3, KC20×1.5 with ATR10, EMA100; it does not establish the derivative's added exits, execution timing or performance.

### Independently reproduced

**No strategy backtest, trade events, Qlib parity or performance was reproduced in this Scout.** The following is **source inspection of the pinned execution capability**, not execution of a candidate strategy:

1. Pinned identity: `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`; `hummingbot/VERSION` directly read as `dev-2.17.0`; repository contract pins Hummingbot package `20260920`. Prior Alpha PR #414 records package/source correspondence; **this run did not rehash wheel/image bytes**. Auditor must verify that inherited correspondence applies.
2. `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` directly checked: Binance spot `/api/v3/klines` and `1h` interval. `binance_spot_candles.py::_parse_rest_candles` directly checked: row[0] is **open** timestamp, row[1..5] are O/H/L/C/base volume. `backtesting_data_provider.py::get_candles_df` provides the candles; no special native Supertrend/Keltner feed is required.
3. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::simulate_execution` directly checked: per-row `update_state(row)`, `controller.determine_executor_actions()`, then `simulate_executor` on the row slice. A future strategy-specific controller **must latch completed t** and dispatch only at t+1; this Scout does not implement such a controller.
4. `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` directly checked: MARKET chooses **first supplied row** as fill timestamp and **its observed close** as fill price; `filled_amount_quote=amount×close`, `cum_fees_quote=trade_cost×amount_quote`, terminal `CloseType.POSITION_HOLD`. `order_executor/data_types.py` exposes MARKET and BUY/SELL OrderExecutorConfig with spot connector/pair, amount, OPEN/CLOSE, leverage 1. This supports the explicitly delayed **idealized close-price** derivative, not next-open, intrabar or maker fills.
5. `backtesting_engine_base.py::BacktestPositionHold` directly checked: opposing filled BUY/SELL base amounts net, realized gross PnL and fees tracked separately; closing-tick POSITION_HOLD flush exists. Maintain/reconcile a separate cash/base ledger; do **not** mistake gross PnL for fee-net equity. `backtesting_data_provider.py::get_price_by_type` may return `Decimal("1")` on missing prices: never use that fallback for decisions, fills or marks; fail closed on missing actual close.
6. **Timestamp limitation:** raw Binance candle timestamp is bar **open**; simulator's fill event uses that row timestamp. This derivative defines economically effective completed-bar E[t] for each observed close, so controller/event logs must explicitly normalize to E[t] and must not misstate the raw timestamp as a feasible open-time fill. Model is retrospective and not a real-time close execution guarantee. The pinned backtester does not prove real exchange precision/min-notional acceptance, slippage, partial fills, dynamic fee tiers, or live latency; these are **not** asserted as verified.

**Pinned source references:**
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/executors/order_executor/data_types.py
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_data_provider.py

### Negative evidence

Original Pine source bytes/revision and exact source-native Supertrend initialization are unavailable; the researcher's ST recursion and risk exits are explicitly **derived**, not quietly substituted original facts. No independent profitability, original TradingView backtest reproduction, runtime wheel hash, Qlib/Hummingbot event-level parity, or live market acceptance evidence. A failure of the declared pinned historical execution/cost path is **NOT_LOSSLESS**, not an excuse to relabel PASS.

### Six-gate Scout assessment (proposed PASS; independent auditor owns decision)

1. **G1 reproducibility:** pinned source/defaults, exact TR/ATR/EMA/Keltner/ST formulas and seeds, strict same-bar crossing, tie cases and fixed parameters.
2. **G2 direction:** Binance spot LONG/FLAT, short explicitly disabled.
3. **G3 risk/exits:** entry triple-confluence; priority 5% close trigger, ST-down flip, KC-mid down-cross; no hidden exits, no guaranteed stop price.
4. **G4 position:** one 0.001 BTC position, 10k USDT ledger, pending/fill-bar states, fresh-event re-entry, DCA/pyramiding/concurrency disabled.
5. **G5 pinned engine:** inspected Binance spot 1h OHLCV, controller action sequencing, MARKET first-row observed-close fills, POSITION_HOLD/fee ledger, raw timestamp normalization, fail-closed missing price; package/source correspondence inherited from PR #414 and requires auditor confirmation.
6. **G6 causality:** 150-bar completed warmup, t close decisions at E[t], t+1 observed completed-close fills at E[t+1], no lookahead or future data.

## Falsification plan

Without performing a backtest here: test strict upper-band equality, ST initial DOWN and reversal thresholds, simultaneous versus staggered flip/cross, EMA100 equality, missing 1h bars, ATR zero, stop/flip/midline exit priority, pending/fill-bar suppression, cash sufficiency, last-bar pending action and observed-only terminal mark. Independently verify the pinned wheel/source mapping and controller timestamp normalization; validate any newly required Qlib execution primitive with one representative Qlib/Hummingbot event-level parity test **before** mass screening. No strategy-specific parity/performance is claimed at admission.

## Crypto portability

This immutable derivative is BTC-USDT **spot 1h only**, unleveraged. The original indicator is described as usable on other markets/timeframes, but those are **not** part of this tested expressibility claim. Different symbols, intervals, futures funding, margin or risk sizing require a separately frozen version and engine/cost assessment; neither the campaign's seven coins nor its DCA 6/6/6 overlay is an HB_READY prerequisite.

## Limitations

The same-bar triple condition may be rare or never occur on some samples; lack of trades is not a profitable backtest. The 5% threshold is **close-triggered** and executed only at a later completed close, so losses may exceed 5%. Historical MARKET-close prices are an idealized simulator convention. Original Pine fidelity, dynamic sensitivity behavior, source bearish exit, exchange execution quality, funding, Qlib parity and Survivor status are not established. No user/private data or copyrighted Pine code copied.

## Implementation status

`not-implemented`: this is a research record, **not** a controller, runnable Qlib strategy, backtest, execution order or deployment. An admitted PASS may later require minimal strategy-specific implementation without introducing a new admission status.

## Adoption boundary

`research-only`, `adoption: not-approved`, `approval_scope: research-only`. Scout's PASS is a **proposal pending independent Hermes Auditor exact-head review**, not self-approval. Only the independent webhook review may remediate source facts, merge exact-head PASS or close as NOT_LOSSLESS. Existing signed webhook receiver alone owns post-merge README count synchronization. No main modification, Qlib/Hummingbot run, trading, or workflow changes are authorized.

## Related Wiki records

No Wiki record created or modified in this Scout. Related main strategy families: standalone Supertrend, Keltner/ADX breakout, and squeeze/EMA100; none is claimed equivalent to this simultaneous triple-event derivative.

## Sources

- SwiftEdge (2025-05-02; updated 2025-05-03), *QuantumTrend SwiftEdge*, TradingView first-party public indicator: https://www.tradingview.com/script/hkpsp4so-QuantumTrend-SwiftEdge/
- Pinned Hummingbot source commit: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Alpha review contract at candidate base: https://github.com/HCH725/alpha-strategy-research/blob/e7e1a8282c161fe424597d0f3557b15994b96c11/.github/HB_READY_REVIEW.md
