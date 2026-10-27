---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 434330 TTM-scalper close-lattice latch long-flat BTC-USDT spot 1d independent derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-12-05
sources:
  - https://www.fmz.com/strategy/434330
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The page ZH/EN porter prose describes a rising structure as a sell signal and a falling structure as a buy signal (dot/marker semantics), but the pinned code maps the rising-lattice state to switch 1 / green / pos +1 / Long entry and the falling-lattice state to Short entry. The code governs everywhere; the prose paraphrase is fenced as unreliable and no prose sentence enters any gate."
---

# TTM Scalper — three-close reversal lattice with persistent latch, long-flat research derivative

## Provenance

**First-party FMZ source:** strategy `434330`《基于价格反转的TTM银隼震荡策略》(TTM Falcon Oscillator Reversal Strategy Based on Price Reversion), porter `ChaoZhang`, page `Last Modified` **2023-12-05 15:07:10** (adopted as `source_as_of`). The Pine block credits `Copyright by HPotter v2.0 10/01/2018` and describes itself as a close approximation of John Carter's Scalper Buys and Sells (`Mastering the Trade` — lineage only; no rule is taken from the book). Inspected **2026-10-27** via the stable public page (HTTP 200, 713,433 landing bytes, no login) with the full executable payload read verbatim, cross-checked against the immutable mirror file `基于价格反转的TTM银隼震荡策略TTM-Falcon-Oscillator-Reversal-Strategy-Based-on-Price-Reversion.md` (10,337 bytes, FMZ id `434330` in its `> Detail` block). No source-native, HPotter-identical or author-performance reproduction is claimed.

**Verified source-code facts (live payload = mirror bytes on every gate-critical line):** `//@version=2`; `strategy(title="TTM scalper indicator", overlay = true)` — no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no commission/sizing argument ships anywhere (Pine v2 defaults govern the source backtest: single evaluation per completed bar, next-bar fills, pyramiding 0). `reverse = input(false, title="Trade reverse")`. `triggerSell = (close[1]<close) AND (close[2]<close[1] OR close[3]<close[1])`; `triggerBuy` is the exact mirror (`>` in all three places). `buySellSwitch` latches 1 on triggerSell / 0 on triggerBuy / holds otherwise (`nz` init 0). `clr_s` latches 1 on a fresh triggerSell state / 0 on a fresh triggerBuy state / holds otherwise (`nz` init 0, so the seed color is red). `clr` is red iff `clr_s==0` else green. `pos` is +1 iff green, −1 iff red (the `nz(pos[1],0)` fallback is unreachable — `clr` is always exactly one of the two). `possig = pos` at the pinned `reverse=false` (the `reverse=true` inversion path is disclosed-as-disabled code, never the admitted rule). `if (possig == 1) strategy.entry("Long", strategy.long)`; `if (possig == -1) strategy.entry("Short", strategy.short)`. `barcolor`/`plot(SBS,...)` are display only and never order-read. Text census over the payload: 2 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `crossover`/`crossunder` / 0 `request.*`/`security(` / 0 indicator calls of any kind (no sma/ema/stdev/rsi/highest/lowest/linreg — pure close comparisons plus the latch) / 0 `volume` / 0 `open`. Backtest stanza prints `start: 2022-11-28 00:00:00`, `end: 2023-12-04 00:00:00`, `period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT` — quoted as printed, never adopted as research economics.

**Explicit independent derivative, NOT lossless source reproduction:** The researcher chooses Binance BTC-USDT **spot 1d**, LONG/FLAT only (the source short leg becomes the signal exit, never a short position), fixed 0.001 BTC on 10,000 USDT research cash, completed-close signal to next completed-close historical MARKET fill (substituting for the source backtester's next-bar fill), hypothetical 0.1% fee per filled side, `reverse=false` pinned, and a 10-bar warmup holding FLAT (the source seed state is short-leaning — `clr_s=0 → red → pos=-1` from bar 0 — and its bar-0 short is never traded here). These choices materially change trade events and economics and are researcher-authored.

**Frozen derived identity:** `FMZ:434330|2023-12-05|HPotter-TTM-scalper-v2|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:UTC1d|close-lattice-3bar|switch-clr-pos-latch|reverse-false|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup-t10`. A change to any decision-critical rule defines a new derivative, not a silent update to this identity.

## Economic mechanism

### Source-reported

The script header states the method is a close approximation of Carter's Scalper Buys and Sells and warns the squares are not real-time but print once the third bar confirms a reversal. No sample, metric, table, figure, or performance number of any kind ships anywhere in the payload or the ported prose — this record adopts no source-reported performance.

### Research interpretation

A two-leg close-comparison lattice driving a persistent one-bit latch: the rising lattice (today above yesterday, yesterday above at least one of the two closes before it) sets the latch long; the falling mirror sets it short; anything else holds the prior state, so chop produces no new orders by construction. Unlike streak-count records the comparison is bar-to-offset (up to 3 bars back), never candle-to-candle chains; unlike band/channel records there is no average, no dispersion, and no level anywhere — the entire signal is six strict close inequalities plus recursion. The latch is the whole risk control: there is no stop, target, or timer, so drawdowns end only on the opposite lattice print. No performance assertion is made.

## Signal

1. **Inputs and clock:** one contiguous, chronological real Binance BTC-USDT spot **1d** OHLCV sequence indexed t=0,1,...; each opening timestamp T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite O,H,L,C>0, H>=max(O,C), L<=min(O,C), H>=L, and finite V>=0 for every row (O/H/L/V are continuity-validated but never signal-read — the rules below read close only). Abort on gaps, duplicates, missing prices, malformed bars, unavailable last candle or out-of-order timestamps. No interpolation, synthetic price, full-sample fitting or partial candles. Bar t's completed values become available only at E[t]=T[t]+86400, not at T[t].
2. **Reversal lattice (verbatim, strict):** for t>=3 with all four closes finite positive, `triggerSell[t] = (C[t-1]<C[t]) AND (C[t-2]<C[t-1] OR C[t-3]<C[t-1])`; `triggerBuy[t] = (C[t-1]>C[t]) AND (C[t-2]>C[t-1] OR C[t-3]>C[t-1])`. Equality on any leg makes that leg false; both triggers can never fire on the same bar (they require opposite strict sides of C[t-1] vs C[t]). Bars t<3 print no trigger (unavailable history reads as false, never fabricated).
3. **Latch (verbatim recursion, Pine `nz`=0):** `switch[t] = triggerSell?1 : triggerBuy?0 : switch[t-1]`, `switch[-1]=0`. `clr_s[t] = (triggerSell AND switch[t-1]==0)?1 : ((triggerBuy AND switch[t-1]==1)?0 : clr_s[t-1])`, `clr_s[-1]=0`. `clr[t]` is red iff `clr_s[t]==0`, else green. `pos[t] = +1` iff green, `−1` iff red (the `nz(pos[1],0)` seed is unreachable — fenced, never traded on). `possig[t] = pos[t]` at pinned `reverse=false`. Float-free integer/boolean arithmetic; no rounding anywhere.
4. **Seed fence:** the source seed state is short-leaning (`clr_s=0 → red → pos=-1` until the first rising-lattice bar). This derivative holds FLAT through the warmup regardless of seed, so the seed never opens anything.
5. **Warmup/entry:** start FLAT, zero BTC and 10,000 USDT. No trading for t=0..9; first possible completed-bar decision is **t=10** (structural minimum is t=3 for `close[3]`; 10 covers the lattice seed plus latch-seed margin as a predeclared researcher choice). Indicators may be computed earlier but must never backfill a position before t=10.
6. **BUY scheduling:** if FLAT, no pending order, t>=10, and t is strictly later than any prior exit-fill bar, an entry event is `possig` transitioning to `+1` from a non-+1 state at completed bar t. Store exactly one BUY instruction from the t signal. Dispatch at row t+1 only; idealized historical MARKET full fill uses **observed** Close[t+1] with economic effective time E[t+1]. Never use any t+1 values to decide the t entry. If t+1 is absent, no fill. Require actual positive close and cash >=Q*price*(1+f), Q=Decimal("0.001") BTC and f=Decimal("0.001"); otherwise abort the research segment rather than invent a fill.
7. **No bracket:** there is no stop/target/trailing/time exit in this derivative, matching the source payload's census-verified complete absence of any risk leg. Absence here is an explicit disclosed choice, not a hidden default.
8. **Exit and priority:** while LONG and no pending order, at each later completed bar u (never on the BUY fill bar — exits evaluate only in confirmed LONG state), `possig` transitioning to `−1` from a non-(−1) state schedules a full SELL at row u+1 with idealized MARKET fill at its actual observed close effective E[u+1]; latch-hold bars mean HOLD. The single latch value makes entry and exit mutually exclusive on every bar, so no same-bar ordering assumption exists. No same-bar roundtrip.
9. **Order and re-entry state:** one position and at most one pending order. A confirmed full SELL returns to FLAT, records its fill bar and clears state; any later completed bar with a fresh transition to `+1` may re-enter, with no cooldown and no DCA. Pending bars ignore all signals. Rejected/partial/duplicate/ambiguous BUY or SELL fills, missing price, or insufficient actual data abort the research segment, not silently mutate inventory. A last-row signal without a subsequent observed candle is unfilled; at sample end mark open inventory only at last actual completed close, separately from realized PnL, with no fabricated forced liquidation.
10. **Explicitly disabled:** short/borrow, futures/perpetuals, margin/leverage/funding, pyramiding (Pine v2 default 0 pinned: no same-direction adds while positioned; the source opposite-direction entry reverses, which this derivative expresses as the signal exit, never a reversal add), DCA/safety orders, concurrent markets/shared capital, partial exits, dynamic sizing/compounding, maker/limit/next-open orders, intrabar stops, trailing, time exit, the `reverse=true` inversion path, source futures/next-bar timing, and `barcolor`/`plot(SBS)` display plumbing. No simultaneous or hedged positions.

## Required data

One real Binance BTC-USDT spot 1d OHLCV feed; only close is signal-read (O/H/L/V feed continuity validation only). No external symbols, order book, futures funding, non-OHLCV data, secondary timeframes, fitting or future extrema. Validate candle continuity and all observed fill prices **before** the pinned engine's feature merge/dropna. Decisions occur at E[t], fills at E[t+1] in the idealized historical model, regardless of the native feed's opening timestamp. All lattice/latch reads use only <=t completed closes. Non-positive prices abort.

## Execution assumptions

**Pinned GitHub-inspected benchmark (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Immutable raw-file inspection this run of `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993 bytes; INTERVALS declares `1h` and `1d`), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913 bytes; MARKET path fills at the row's actual close with `filled_amount_quote`/`cum_fees_quote` accumulation, returns `CloseType.POSITION_HOLD`), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (39,071 bytes; `BacktestPositionHold`, `simulate_execution` calling `controller.determine_executor_actions()` with `CreateExecutorAction`), and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (8,823 bytes; line 140 `get_price_by_type` missing-price fallback). Prior Alpha PR #414 reports independent package/source correspondence; no wheel/image digest rehash in this run.

- **Actual feed:** pinned BinanceSpotCandles declares `1d`; Binance REST row[0] is **opening timestamp**, row[1..5] supplies real OHLCV. No synthetic candles, inferred fill prices, or silent forward filling. `BacktestingEngineBase.prepare_market_data` can merge features and drop missing rows; a pre-engine strict continuity/validity check is mandatory.
- **Actual action path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction`. A future minimal candidate-specific controller (not yet implemented) must preserve t's latch/pending state, delay dispatch to t+1, and issue `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`; no API name alone is asserted to implement this strategy.
- **Actual bounded fill:** MARKET dispatch on t+1 yields an idealized **t+1 close** fill at that row's actual close, not the source backtester's next-bar fill and not an achievable live post-close market price. Native fill row timestamp is an **opening** timestamp; economic effective fill time must be normalized to E[t+1], never reported as T[t+1].
- **Position and fee ledger:** pinned `BacktestPositionHold` nets opposite BUY/SELL base quantities and reports gross realized PnL while fees accumulate separately. Maintain a persistent confirmed-fill ledger (`terminated_executors_window=None` or equivalent) and explicit research cash/inventory: BUY cash `-=Q*Pb*(1+f)`, SELL cash `+=Q*Ps*(1-f)`, net realized round-trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. The fee `f=0.001` is a **hypothetical 0.1% quote-notional fee per filled side**, not a verified Binance fee tier. Engine float-ledger internals are not asserted equal to research-side Decimal bookkeeping; any fill/ledger ambiguity aborts the segment instead of being rounded into a fill. Never call gross engine PnL net. Spot funding is **not applicable**, not fabricated zero perpetual funding.
- **Pure-research precision model (no exchange-spec gating):** this derivative adopts a pure-research fixed-quantity Decimal model unconstrained by exchange specifications — there is deliberately no trading-rules snapshot, no minimum-quantity/step-size/minimum-notional gate, and no precision/validity precondition on fills. Live minimum order size, quantity steps, minimum notionals, and fee tiers are explicitly out of scope and unasserted; fills are idealized historical close fills, never claimed as exchange-acceptable orders.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on a missing price; explicitly **forbid** that fallback. Reject absent/nonpositive observed closes, partial fills and ambiguous position accounting rather than inventing economics. Simulator's idealized full fill does not prove real spread, slippage, liquidity, dynamic fee or latency. The future controller, real execution and package binary are **not** independently validated; this record claims only the bounded pinned historical close-fill primitive.

## Evidence

### Source-reported

FMZ 434330 (porter ChaoZhang, 2023-12-05; HPotter v2.0 2018-10-01 header): three-close reversal lattice, persistent switch/color/position latch with flat-unreachable seed, `reverse=false` pin, Long entry on `possig==1` and Short entry on `possig==-1`, no risk leg, display-only `barcolor`/`SBS` plot, Futures_Binance BTC_USDT 1d backtest stanza (2022-11-28 → 2023-12-04). No original backtest result is adopted.

### Independently reproduced

**None for strategy events, profits or outcomes.** No Pine parity run, candidate-specific Hummingbot run, Qlib backtest, event-level parity, actual fills, installed package hash, OOS, Survivor or HB Certified claim. Only the **page HTML payload and the existing pinned source-code engine/data/executor/fee paths** were directly inspected via the stable FMZ URL and immutable raw files at the pinned commit. Alpha PR #414 is prior correspondence evidence, not a claim of re-execution this cycle.

### Negative evidence

Source futures market, short leg, seed short-lean, and next-bar fill timing are **explicitly replaced**, not source-native rules. The porter prose inverts the trigger-to-side mapping (dot semantics, not trade legs); the code governs. The `reverse=true` inversion, `SBS` dot coordinates, `barcolor`, and `plot` never gate an order. Idealized close fills and assumed fees do not prove exchange execution. No realistic live fills or funding are asserted.

**Six-gate proposal, pending independent Hermes Auditor:**
1. Determinism: six strict close inequalities, verbatim latch recursion with `nz`=0 seeds, mutual-exclusion proof, t=10 warmup, transition-only events.
2. Direction: Binance BTC-USDT spot LONG/FLAT; the source short leg survives only as the signal exit.
3. Entry/exit/risk: fresh `+1` transition schedules entry, fresh `−1` transition schedules full exit, disclosed absence of any risk leg.
4. State: fixed 0.001 BTC, one pending order/position, research cash and fee ledger, no DCA/concurrency, fresh event after exit, abort on ambiguous fills.
5. Pinned model: directly inspected actual 1d feed, controller/action, MARKET close fill, POSITION_HOLD and fee paths; pure-research precision model with no exchange-spec gating; no unsupported next-bar/intrabar/funding assumption.
6. Causality: lattice needs t>=3, trading from t=10, t completed signal -> t+1 completed-close economic fill, no future bars, opening timestamp never misrepresented as close availability.

**Dedup snapshot:** at `main=4853ba1`, 386 root Markdown files = 384 strategy records + 2 READMEs, matching README pool count 384 (existing records were **not** exhaustively re-audited for PASS frontmatter; count equality is not represented as a full admission census). Repo-wide `grep -rilE` over root `*.md` returned zero signal-use for `434330`, `buySellSwitch`, `clr_s`, `SBS`, `triggerBuy`, `hpotter`, `falcon`; `ttm`/`scalper`/`Carter` hits are prose/family mentions inside other records' dedup paragraphs (Forven TTM-squeeze, SQZMOM-LB squeeze-release, Eterna confluence) or unrelated text, never this lattice. Nearest pool neighbors are materially different constructions: `forven-ttm-squeeze-momentum-release-long-flat` (1h, BB-inside-KC release AND-gated with rising linreg oscillator, momentum-flip exit — no close lattice, no latch); `sqzmom-lb-squeeze-release-ema100-two-sided` (1d two-sided, squeeze-transition + EMA100 + trailing-100-extreme gates + any-tick closes — none of which exists here); `1-3-1-red-green-candle-reversal` (1h long-only, red-plus-three-rising-greens color sequence with red-low stop and fixed 1R limit — pattern plus bracket, no latch, no transition exit); `three-down-three-up-consec-close` (strict chain counting, no offset lattice, no latch); `combo-123-reversal-fisher-transform` (123-pattern AND Fisher agreement with a flat leg). All ten open `research/*` PR titles/bodies were checked for source identity with no match.

## Falsification plan

With separate authorization, materialize only a minimal candidate-specific controller, validate the strict t/t+1 clock and actual close inputs, lattice strictness (equality legs fire nothing), latch seeds (`switch`/`clr_s` init 0, seed short-lean, unreachable `pos` fallback), mutual exclusion (no bar fires both triggers), post-exit re-entry, fail-closed invalid fills and fee-net position accounting. Before large-scale Qlib screening on a newly unverified execution path, obtain representative Hummingbot/Qlib event-level parity for signals, fills, fees and states. Separately assess fee-net IS/OOS performance; no such test is run by this Scout.

## Crypto portability

BTC-USDT spot 1d is researcher-selected (the executable stanza itself backtests BTC_USDT at `period: 1d`, so the frame is source-native; only the venue leg moves from futures to spot). Any futures, 3x/5x, DCA BO/SO 6/6/6, other coin or execution model is downstream optional research requiring a separately specified derivative and verified execution/cost/funding path. No implied transfer of results.

## Limitations

No Pine parity run; source-native equivalence unverified. Derived spot venue, long-flat posture, next-close fill, fixed quantity, warmup, and hypothetical fees materially differ from the source backtest. The always-±1 latch means the book is either long or flat-needing-re-entry with no neutral rest state beyond warmup and post-exit bars. Idealized close fills and assumed fees do not prove exchange execution. No installed package rehash, strategy backtest, Qlib parity, profitability or live authorization. Thin-volume regimes are untested.

## Implementation status

`not-implemented`: research specification only. No controller, Qlib recipe, trading deployment, backtest, container, n8n or cron changes.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, not self-approved. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns README bookkeeping after an accepted merge. Scout does not approve, merge, close or write main.

## Related Wiki records

None created or modified.

## Sources

- https://www.fmz.com/strategy/434330 — ChaoZhang-ported HPotter TTM scalper Pine v2, page Last Modified 2023-12-05; live payload inspected 2026-10-27.
- https://raw.githubusercontent.com/HCH725/hummingbot/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source (feed constants, order executor simulator, backtesting engine base, data provider), inspected through immutable raw files 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier package/source correspondence evidence; not re-run here.
