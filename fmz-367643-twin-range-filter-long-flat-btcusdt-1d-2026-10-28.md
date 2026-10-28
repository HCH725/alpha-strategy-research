---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 367643 Twin Range Filter smoothed range-clamp regime long-flat BTCUSDT 1d independent derivative"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-06-12
sources:
  - https://www.fmz.com/strategy/367643
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Twin-Range-Filter.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Twin Range Filter smoothed range-clamp regime — BTCUSDT spot 1d long-flat derivative

## Provenance

- **Primary source (public FMZ page, read this cycle):** FMZ strategy `367643`, `Twin Range Filter`, porter `Zer3192`, Created 2022-06-04 20:24:49, tag `EMA`. Page fetched this cycle over plain HTTPS: HTTP 200, 733,360 bytes. The full Pine block sits behind FMZ's "Login to view full source" wall, so the verbatim code below is taken from the pinned immutable mirror with byte hashes nailed down.
- **Immutable mirror (byte-verified this cycle):** `fmzquant/strategies@7853bb2bf262c4567ac238d3552d97f0e50cb801`, path `Twin-Range-Filter.md`, blob `031b56424522384510495db0f5adf020dc827d04`, 3,070 bytes, sha256 `01055174706827fd96c7548f5af5c17707b9075ea71e2518d5a799d91b05dde7`, Last Modified 2022-06-12 21:00:10, Detail link back to the FMZ page above. Pine header `// © colinmck`, `//@version=4`. Only rule tokens are normalized and cited here; no image assets are copied.
- **Source declares `study(...)`, NOT `strategy(...)`:** the payload's `study(title="Twin Range Filter", overlay=true)` carries zero trade economics — census over the 56 non-empty code lines: `strategy(` 0, `study(` 1, `strategy.exit` 0, `strategy.close` 0, `strategy.order` 0, `stop=`/`limit=`/`profit=`/`loss=` 0, `pyramiding` 0, `process_orders_on_close` 0, `timeframe` 0, `volume` 0, `input(` 5, `ema(` 2, `nz(` 9. The two trailing `strategy.entry("buy"/"sell")` legs are porter-appended (they cannot compile inside a Pine v4 `study()` at all) and carry no sizing, capital, commission or pyramiding declaration.
- **Researcher-defined derivative v1, NOT source-native:** preserve the exact twin-smoothed-range clamp, recursive filter, counters, strict conditions and regime latch, but trade Binance **BTCUSDT spot** UTC **1d** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, t-signal to t+1 completed-close MARKET fills, and a 300-bar FLAT warmup. This drops the demo venue (`Futures_Binance`, `BTC_USDT`, `period: 4h`, `basePeriod: 15m`, backtest window 2021-05-08→2022-05-07), converts the porter two-sided legs into long-flat, and pins the Pine seed/na conventions below. These choices **materially change** original trade economics.
- **Frozen independent identity:** FMZ:367643|mirror:7853bb2|TRF|derived-v1-20261028|BinanceSpot-BTCUSDT-UTC1d|per27x1.6-per55x2.0-close|clamp-regime-latch|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup300. Any decision-critical alteration creates a new derived version, not a silent update.

## Economic mechanism

### Source-reported

Twin estimates of "smooth average range" (a fast 27/1.6 leg and a slow 55/2.0 leg, each a nested EMA of absolute bar-to-bar change) are averaged into one half-width `smrng`; a recursive clamp `filt` trails price within that width; persistence counters plus a regime latch convert clamp crossings into alternating long/short regime events. No protective stop, target, trailing, or time exit exists anywhere in the payload.

### Research interpretation

This derivative is long only inside a bull regime (entered on the first bull-latch bar after a bear regime) and flat after the first bear-latch bar — a pure clamp-regime state hold on a close-only smoothed range, not a moving-average cross, not a band touch, and not a volatility breakout. The clamp width breathes with realized absolute movement (≈2.6% of price at the median on 1d), so choppy tapes whipsaw the latch while trends ride; the only risk control is the opposite latch, so a grinding decline that never prints a bear latch stays exposed.

## Signal

1. **Input and availability:** one chronological, contiguous sequence of actual Binance BTCUSDT spot UTC **1d** candles indexed t=0,1,... . Native opening time T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite positive O,H,L,C, H>=max(O,C), L<=min(O,C); volume is unused and unchecked. Reject duplicates, gaps, out-of-order bars, missing/zero/nonfinite observed prices or incomplete candles; never interpolate or forward-fill. Completed bar t is available at E[t]=T[t]+86400, not T[t]. Float64 chronological arithmetic, no intermediate rounding. Only the **close** series `x` is consumed by the decision.
2. **Constants (researcher-pinned to payload defaults):** `source=close`, `per1=27`, `mult1=1.6`, `per2=55`, `mult2=2.0` pinned (the payload's five `input()` defaults; the source menu is fenced, not adopted).
3. **Twin smooth range (Pine-v4-faithful, researcher-pinned seed convention):** `smoothrng(x,t,m)`: `wper=t*2-1` (53 / 109); `avrng=ema(abs(x-x[1]),t)`; `smoothrng=ema(avrng,wper)*m`. Pine v4 `ema` is emulated as: seed = SMA of the first L inputs, then `alpha*x+(1-alpha)*prev` with `alpha=2/(L+1)`; the bar-0 `abs(x-x[1])` na is pinned to `0.0` and leading na stretches hold (this seed choice is a disclosed researcher pin where Pine's na-skipping is ambiguous — see Limitations). `smrng1=smoothrng(x,27,1.6)`, `smrng2=smoothrng(x,55,2.0)`, `smrng=(smrng1+smrng2)/2`. First valid `smrng` lands at index 162 (verified in the replay below); earlier bars are indicator seed, never orders.
4. **Recursive clamp (verbatim, `nz` = 0.0):** `filt[0]=x[0]` (series init, not zero). For t>=1: while `smrng[t]` is na, `filt[t]` holds na (Pine na-propagation); once valid, `prev=nz(filt[t-1])` and `filt[t]= (prev if x[t]-r<prev else x[t]-r) if x[t]>prev else (prev if x[t]+r>prev else x[t]+r)` with `r=smrng[t]`. The stale-`prev` hold and the 0.0 restart are Pine-literal, verified against the payload text this cycle.
5. **Persistence counters (verbatim, seed 0.0):** `upward[t]=upward[t-1]+1` if `filt[t]>filt[t-1]`, `0.0` if `<`, else hold; `downward[t]` mirrored. Na-filter bars hold both counters (Pine na-condition falsy).
6. **Conditions (verbatim, strict inequalities, equality holds):** `longCond=(x>f and x>x1 and up>0) or (x>f and x<x1 and up>0)`; `shortCond=(x<f and x<x1 and dn>0) or (x<f and x>x1 and dn>0)` with `f=filt[t]`, `x1=x[t-1]`. Under Pine `and`-over-`or` precedence each simplifies to a side test plus `upward/downward>0` plus `x!=x1`; a doji-equal bar (`x==x1`) fires nothing and holds. The disjunct redundancy is preserved word-for-word, simplification noted, never re-timed.
7. **Regime latch (verbatim, seed 0):** `CondIni[t]=1` if longCond, `-1` else if shortCond, else hold. `long=longCond and CondIni[t-1]==-1`; `short=shortCond and CondIni[t-1]==1`. Long and short can never co-fire (complementary strict side tests); no tie-break is needed. Dead `hband`/`lband`, `plotshape` and `alertcondition` lines are visual-only and excluded; they change no event.
8. **Warmup:** bars 0..299 are FLAT-only seed (slow leg needs 55+109-1=163 bars to its first value; 300 covers the seed transient plus the na-hold/restart with margin). First eligible decision bar is t=300. No extra margin is added beyond the pinned 300.
9. **Entry:** when FLAT with no pending action, t>=300, t strictly later than the last SELL-fill bar, and a `long` latch at t, queue exactly one BUY. Dispatch on row t+1 only, independently of that row's signal, and model a full 0.001 BTC MARKET fill at its **actual observed completed close** C[t+1], effective E[t+1]. No t+1 price or indicator is used to decide at t. If row t+1 does not exist, leave unfilled. Require cash >=Decimal("0.001")*Decimal(str(C[t+1]))*(1+Decimal("0.001")); insufficient funds or ambiguous/missing fill aborts rather than assuming borrowing.
10. **Exit:** when confirmed LONG and no pending action, on the first eligible completed bar u after the BUY-fill bar with a `short` latch at u, queue a full 0.001 BTC SELL for row u+1 at actual observed C[u+1], effective E[u+1]. No stop/target/trailing/time order exists in the payload; all are expressly disabled, not hidden defaults. The opposite latch itself is the sole risk mechanism.
11. **State and priority:** exactly FLAT, BUY_PENDING, LONG, SELL_PENDING; one position and one pending action maximum. The `CondIni` latch makes events strictly alternate L→S→L, so no cooldown is needed. Single unit with no adds (porter legs declare no sizing or pyramiding). On a pending/fill bar ignore new order signals but keep filter/counters/latch updating. On confirmed SELL, return to FLAT using the independent confirmed-fill inventory ledger and record last SELL-fill bar. Re-entry requires FLAT plus a future bull latch. Never BUY and SELL on the same bar. If a fill fails, is partial, duplicated, stale or cannot be reconciled, abort the segment. At sample end, an unfilled pending signal remains unfilled; open inventory is marked only to the last actual completed close and not fictitiously liquidated.
12. **Disabled:** demo venue/timeframe/window, porter two-sided legs as lossless economics, backtest-window cherry-picking, the source menu beyond pinned defaults, short/borrow leg, stops/targets/trailing/time exits, pyramiding, DCA/safety orders, simultaneous markets/shared capital, partial exits, dynamic sizing/compounding, limit/maker fills, intrabar triggers, discretionary overrides, hidden executor risk defaults and forced end-of-sample close.

## Required data

Only one real Binance BTCUSDT spot 1d OHLC feed, no fitted models, external symbols, cross-asset shared capital, funding, order book, non-OHLCV features, second timeframe or future extrema. All decision inputs at t are C[0..t] through the causal EMA/filter/counter/latch chain from bars <=t completed by E[t]. A strict input validity and continuity check must precede the pinned engine's feature merge/dropna; if data cannot satisfy it, fail closed. Native Binance kline timestamp is the **open** time, never the completed-close availability or economic fill time.

## Execution assumptions

**Pinned source-code benchmark inspected at HCH725/hummingbot commit 8b0e067e80ab62f10846d518dcb5a8218527ddb3 on 2026-10-28:** the commit SHA and `hummingbot/VERSION` = **dev-2.17.0** (11 bytes) were verified via pinned raw fetch this round (package label **20260920** unchanged in the live admission contract). Three pinned raw files were byte-verified this round against prior independent review sizes: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993, `1d` declared in INTERVALS), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (8,823). Key lines re-verified: MARKET `entry_price = df_filtered.loc[fill_timestamp, 'close']` (line 56), `CloseType.POSITION_HOLD` (line 70), and the `Decimal("1")` missing-price fallback in `get_price_by_type` (forbidden here).

- **Data:** pinned `BinanceSpotCandles` reads Binance REST `/api/v3/klines` opening timestamp plus actual OHLCV on the **1d** interval. Strict full-bar availability/continuity must be enforced before any feature dropna; a missing price is never substituted.
- **Controller/action path:** `BacktestingEngineBase.simulate_execution` iterates completed rows, calls `update_state(row)`, then `controller.determine_executor_actions()`, simulating CreateExecutorAction. A future minimal candidate-specific controller (not yet materialized) must retain the twin-range/filter/counter/latch values and FLAT/LONG/pending state and send the precommitted t signal on t+1 via OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY or SELL,amount=Decimal("0.001"),position_action=OPEN or CLOSE,execution_strategy=MARKET,price=None,leverage=1). The presence of this API is **not** alone the compatibility proof.
- **Observed fill primitive:** pinned OrderExecutorSimulator MARKET path fills at the first supplied candle with entry price taken from that row's actual close, not a fabricated price, computes float(amount)*entry_price as filled quote and trade_cost*quote as fee, then returns CloseType.POSITION_HOLD. Dispatch at t+1 produces the declared idealized t+1 completed-close fill. It is not an achievable post-close live order guarantee; economic timestamp is E[t+1], even though native row timestamp is T[t+1]. This **adapts** any Pine next-bar assumption into a disclosed completed-close derivative choice, not lossless reproduction.
- **Position and economics:** BacktestPositionHold aggregates BUY/SELL gross exposure and fees separately; native gross realized PnL is not net research PnL. Keep complete confirmed-executor history (terminated_executors_window=None or equivalent) and a separate Decimal research cash/inventory ledger independent of BacktestPositionHold.is_closed. Start cash=10000 USDT, BTC=0; each confirmed BUY: cash -= Q*P*(1+f), inventory +=Q; each confirmed SELL: cash +=Q*P*(1-f), inventory -=Q, with Q=Decimal("0.001") and f=Decimal("0.001"). Net roundtrip realized =Q*(Ps-Pb)-f*Q*(Pb+Ps); record fees separately. This **0.1% quote-notional fee per side is hypothetical**, not a verified Binance fee tier; spot funding is not applicable, not invented perpetual funding=0. No compounding.
- **Float/Decimal precision boundary:** native simulator computes quote in float; BacktestPositionHold re-derives base quantity from Decimal(quote)/price and checks net_amount_base==0 exactly. Opposite equal configured amounts can leave sub-atomic dust; its is_closed flag and positions_held are **not** used as the derivative's authoritative FLAT/LONG or cash ledger. Confirmed OrderExecutorConfig amount and full-fill evidence determine exact research inventory Q; compare engine-derived residual to expected inventory only diagnostically with absolute tolerance 1e-12 BTC and abort if greater. This tolerance is a **researcher-declared diagnostic**, not an engine patch, live lot precision, or silent rounding of an order. Earlier independently reviewed Alpha PRs #519/#529/#530 record bounded synthetic primitive exercises at Q0.001, fee 0.001 and 1e-12 diagnostic tolerance; this record reuses that bounded pure-research primitive. No candidate-specific backtest or new primitive test is claimed here.
- **Pure-research precision contract:** deliberately no exchange lot/tick/min-notional/available-live-balance acceptance gating is claimed. This is an idealized fixed-quantity historical model, not an exchange-acceptable order assertion. Exchange trading rules, liquidity, spread, actual slippage, live fee tiers and real fills are out of scope; they must be independently verified before any deployment. The engine's `get_price_by_type` fallback Decimal("1") on missing prices (re-verified this round) is **forbidden**; missing/nonpositive actual close, ambiguous full-fill, unbounded dust or incomplete fee/position ledger aborts the research segment.

## Evidence

### Source-reported

Pinned mirror payload (read end to end this cycle): five `input()` defaults (close/27/1.6/55/2.0), `smoothrng` nested-EMA definition with `wper=t*2-1`, `rngfilt` recursion with `nz`, `upward`/`downward` counters seeded 0.0, dead `hband`/`lband`, strict `longCond`/`shortCond` disjunctions, `CondIni` latch seeded 0, `long`/`short` edge triggers, `plotshape`/`alertcondition` visuals, and two porter-appended `strategy.entry` legs under a `study()` declaration. Demo header comments pin `Futures_Binance BTC_USDT 4h/15m` and the 2021-05-08→2022-05-07 window — fenced here, never adopted. No sizing, capital, commission, stop, target, pyramiding, or warmup-cause is adopted from the payload.

### Independently reproduced

No strategy backtest, realized market fills, profits, Qlib parity, OOS, Survivor or HB Certified results. This cycle directly inspected the FMZ page (HTTP 200, 733,360 bytes) and the verbatim mirror payload from the immutable pinned commit (size/sha256 pinned above), plus the immutable pinned Hummingbot feed/MARKET/POSITION_HOLD/fallback source paths (SHA, VERSION and three file sizes re-verified this round), and reused prior independent primitive evidence (#519/#529/#530), not a candidate-specific test or installed-binary hash. Prior primitive validation does not imply that an unimplemented dedicated controller already exists.

- **Rule-logic self-check (stdlib only, not a backtest):** the frozen twin-range/filter/counter/latch chain plus the FLAT/LONG state machine were executed over the real-data replay below — all pass: equality bars route to hold; pre-validity bars stay silent crash-free; first valid `smrng` lands exactly at index 162 as derived; identical inputs give identical outputs across two runs (signal-series md5 `355448c5e102edb089ad27bb09c79aba` twice). Both legs provably reachable (55 bull latches and 55 bear latches).
- **Rule computability on real public data (availability check, not a backtest — no PnL, no returns computed):** 2,126 fully completed Binance BTCUSDT spot `1d` bars (2021-01-01 → 2026-10-27; the still-forming 2026-10-28 candle excluded) verified contiguous at exact 86400-second open steps with zero invalid OHLC bars; post-warmup evaluation yields 55 bull-latch bars and 55 bear-latch bars under the frozen rules. Worked latches: LONG 2021-11-08 area bar 311 (C 67525.83, filt 65012.54, smrng 2513.29), SHORT bar 319 (C 60058.87, filt 62566.57, smrng 2507.70). Simulated t+1-close state execution over the same sample fills 55 round trips (median hold 16 bars, max 58) and ends FLAT — no long held at the sample end. The candidate's trade events, Qlib/Hummingbot parity, and net returns have **not** been independently reproduced. No backtest was executed.

### Six-gate proposed PASS — independent Hermes Auditor decides

1. **Determinism:** literal five defaults, literal nested-EMA formula with pinned seed/na convention, Pine-literal clamp/counter/condition/latch recursion, strict-inequality firing with equality-hold, first-decision index and priority.
2. **Direction:** BTCUSDT spot LONG/FLAT; the porter short leg is explicitly converted into the flat exit, never a borrow.
3. **Entry/exit/risk:** bull-latch BUY, bear-latch SELL; no payload stop/target/trailing/time leg exists (0-exit census in a `study()` payload) and all hidden defaults are expressly disabled; the opposite latch is the sole risk mechanism with no loss-cap claim.
4. **Position:** cash10000/Q0.001/fee0.001, single pending and inventory ledger, latch-guaranteed alternation with no cooldown needed, fail-closed fill reconciliation, re-entry only on a future bar while FLAT, no DCA or concurrency.
5. **Pinned compatibility:** actual 1d Binance spot feed, controller/action/next-row MARKET actual close, POSITION_HOLD gross-plus-fees and independently declared Decimal net ledger, pure-research precision/dust boundary; no unsupported next-open, intrabar, MTF, volume, or futures funding claim.
6. **Causality:** t>=300 completed-bar decision on C[0..t] and filter/counter/latch values from bars <=t (max structural lag 162, decision lag 300), t+1 completed-close fill effective E[t+1], opening timestamp not mistaken for completed data, no future leakage or synthetic prices.

### Negative evidence

No backtest, profitability, Qlib parity, OOS, Survivor or live-fill evidence is claimed. The verbatim code comes from the immutable third-party mirror because the FMZ full source sits behind a login wall; the FMZ page itself (title, porter, dates, params table) was read directly this cycle and the mirror's Detail link points back to it, but the auditor decides whether that provenance suffices. The Pine `ema` seed/na pin is a disclosed researcher convention, and the 300-bar warmup (not a payload value) is the fence around it. The opposite latch is bars late by construction and the book has no protective stop — a grinding decline that never prints a bear latch stays exposed. Event rate is moderate (55 trips per ~1,800 post-warmup daily bars). Sibling clamp/channel exposure shapes in the pool are disclosed, not hidden.

**Dedup:** current main at `283b02e` has 405 root strategy Markdown records (README pool count 405, verified: 407 `*.md` minus two READMEs). Full-tree case-sensitive grep for `Twin Range`, `TwinRange`, `smrng`, `rngfilt`, `smoothrng`, `CondIni`, `367643`, `双范围`, `雙範圍` returns zero strategy records; `Range Filter` matches only two prose mentions (an SMA-range-filter sentence and a Range-Filter-window policy sentence), never a strategy; `colinmck` matches only a credit line in the unrelated QQE record; `Zer3192` matches only two FMZ-porter records (ALMA, fibonacci-retracement) — porter repetition, not strategy repetition. All ten open research/* PR titles were checked (#353 Heracles KCD, #350 ClucMay72018, #331 AdxSmas, #304 forven CCI, #251 Swift 2yMA, #92 SSL, #89 Chandelier, #63 SuperTrend flip, #49 Gauss StochRSI, #48 Larry Williams streak); none is Twin-Range/dual-smoothed-range clamp based. Existing root records were not re-audited individually in this Scout; the 405/405 count census plus the merged-base diff shows only reviewed PASS additions and README bookkeeping, with no other strategy changes.

## Falsification plan

With separate authorization only, materialize the minimal candidate-specific controller and test the 162/300-bar seed boundary, the na-hold/`nz`-restart behavior, flat-tape hold behavior, the exact equality-hold boundary routing, state memory through consecutive same-side conditions, re-entry after an exit while still FLAT, first-decision-edge behavior at bars 299/300, pending-bar gate freezes, exact t/t+1 timing, observed prices, quote fees, separate Decimal inventory, float residual tolerance and end-of-sample treatment. Before large-scale Qlib screening of any new execution path, obtain representative event-level Hummingbot/Qlib parity. No such execution, deployment or backtest occurs in this Scout.

## Crypto portability

Native demo venue is Binance-futures 4h BTC_USDT inside a one-year window; this derivative moves only the venue leg to Binance BTCUSDT spot 1d with no leverage or funding. No asset substitution beyond this single declared market is made. Porting the clamp-regime latch to other spot symbols would be a new derived version with its own evidence, not covered by this record.

## Limitations

Verbatim code comes from the immutable public mirror payload (byte-inspected this round: 3,070 bytes with sha256 pinned above) because FMZ gates its full source behind login; no login-wall bypass was performed. The payload carries an MPL-2.0 header line, so only rule tokens are normalized here. The pure-research close/full-fill/fee model is not a real exchange acceptance or executable strategy implementation. The opposite latch is bars late by construction and the book has no protective stop — a grinding decline that never prints a bear latch stays exposed. The Pine seed/na pin and the 300-bar warmup are disclosed researcher choices, not payload values. No performance, survivor, live or Qlib parity claims.

## Implementation status

**implementation_status: not-implemented** — research record only. **status: research-only; adoption: not-approved; approval_scope: research-only.** The proposed PASS is not self-approval: independent Hermes Auditor GitHub Webhook Review alone owns source-fact review, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns post-merge README bookkeeping. This Scout does not approve, merge, close, modify main or change any trading/backtest/cron system.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, Live, Qlib mass screening, or any deployment. Downstream use requires the independent PASS review plus separate implementation and authorization steps outside this record.

## Related Wiki records

None created by this Scout.

## Sources

- https://www.fmz.com/strategy/367643 — FMZ strategy page carrying the title, porter, dates, parameter table and demo header, read 2026-10-28 (HTTP 200).
- https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Twin-Range-Filter.md — immutable mirror carrying the verbatim Pine v4 payload, inspected 2026-10-28 at pinned commit 7853bb2.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine paths inspected via the pinned tree this round (SHA/VERSION plus three file sizes and key lines re-verified).
- https://github.com/HCH725/alpha-strategy-research/pull/519 — prior independent bounded MARKET/POSITION_HOLD synthetic primitive review.
- https://github.com/HCH725/alpha-strategy-research/pull/529 — prior independent bounded pure-research execution and PASS-only census evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/530 — prior independent PASS census evidence.
