---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 442621 New-highs decay-counter long-flat BTC-USDT spot 1d independent derivative"
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
source_as_of: 2024-02-23
sources:
  - https://www.fmz.com/strategy/442621
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The porter prose describes 20-day highest/lowest PRICE extremes (\"最高价高于过去20天的最高价\"), long AND short trading (\"进行做多或做空操作\"/\"长短头交替\"), a start-date trading gate (\"设定了开始交易的时间\"), and momentum indicators (\"动量指标\"). The pinned code computes highs from CLOSE (ta.highest(close,20)), pins allowShort=false so both short legs are unreachable, leaves the startDate input permanently unread behind the constant inTradeWindow=true, and calls only ta.highest/ta.lowest. The code governs everywhere; no prose sentence enters any gate."
---

# New-Highs Decay Counter — close-refresh event latch with time-decay exit, long-flat research derivative

## Provenance

**First-party FMZ source:** strategy `442621`《反转动量破窗策略》(Reversal Momentum Breakout Strategy), porter `ChaoZhang`, page `Created: 2024-02-23 12:11:32` (adopted as `source_as_of`). Inspected **2026-10-27** via the stable public page (HTTP 200, 785,874 bytes, prose plus argument table fully visible without login; the code block renders truncated behind a "Login to view full source" gate) with the full executable payload read verbatim from the immutable public mirror `fmzquant/strategies@7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified commit via Contents API this run), path `反转动量破窗策略Reversal-Momentum-Breakout-Strategy.md`, blob `d6e67b10026fd275901c67c37c801192d6f1fd60`, 9,518 bytes on the page vs 9,373 bytes payload file (`wc -c` + `git hash-object` agree with the API `sha`/`size`). The `> Detail` block contains exactly `https://www.fmz.com/strategy/442621`. No source-native, author-identical or author-performance reproduction is claimed.

**Verified source-code facts (mirror bytes, Pine v5):** `strategy("New Highs and Lows Momentum Strategy", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100)` — no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no commission/sizing argument ships anywhere (Pine v5 defaults govern the source backtest: single evaluation per completed bar, next-bar fills, pyramiding 0). `window = input.int(20)` / `decay = input.int(5)` / `startDate = input(timestamp("1 Jan 2023"))` (dead — never referenced again) / `allowShort = input.bool(false)` (all four frozen at defaults). `var int highDecayCounter = 0` / `var bool isHighPeriod = false` plus the low-leg mirror pair. `inTradeWindow = true` constant. `window_high = ta.highest(close, window)`; `window_low = ta.lowest(low, window)`. High block verbatim: refresh predicate `window_high > ta.highest(close, window)[1]` sets `highDecayCounter := decay` and `isHighPeriod := true`; otherwise decrement while positive, else `isHighPeriod := false`. Low block is the exact mirror on `low`. Execution block verbatim: `if inTradeWindow` → `isHighPeriod and highDecayCounter == decay` ⇒ `strategy.entry("Long", strategy.long)`; `isHighPeriod and highDecayCounter == 0` ⇒ `strategy.close("Long")`; both short legs additionally gated by `allowShort` (false at defaults — unreachable). Plots only. Text census over the payload: 1 `strategy(` declaration / 2 `strategy.entry` (1 reachable at defaults) / 2 `strategy.close` (1 reachable) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `request.*`/`security(` / 0 `volume` / 0 `barstate`/`timeframe(`/`time(` / `ta.*` set exactly `{highest, lowest}`. Backtest stanza prints `start: 2023-02-16 00:00:00`, `end: 2024-02-22 00:00:00`, `period: 1d`, `basePeriod: 1h`, `Futures_Binance BTC_USDT` — quoted as printed, never adopted as research economics (the 1-year window is explicitly not adopted).

**Refresh-predicate equivalence (verified by proof, not sampling):** `ta.highest(close,20)[t] > ta.highest(close,20)[t-1]` holds iff `close[t] > max(close[t-20..t-1])` — strict on both legs. It is NOT equivalent to `close[t] > close[t-20]`; the latter misreading is fenced and never used.

**Explicit independent derivative, NOT lossless source reproduction:** The researcher chooses Binance BTC-USDT **spot 1d**, LONG/FLAT only (at pinned `allowShort=false` the long-only posture is source-code behavior; only the venue leg moves futures to spot), fixed 0.001 BTC on 10,000 USDT research cash (source sizes 100% equity — replaced and disclosed), completed-close signal to next completed-close historical MARKET fill (Pine-native next-bar-open timing is explicitly replaced, per house convention), hypothetical 0.1% fee per filled side, defaults 20 / 5 / false pinned, the close-refresh event plus 5-bar decay exit pinned as the sole traded rule, and a 22-bar warmup holding FLAT. These choices materially change trade events and economics and are researcher-authored.

**Frozen derived identity:** `FMZ:442621|2024-02-23|new-highs-decay-v1|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:UTC1d|window-20|decay-5|allowShort-false|close-refresh-event|decay-zero-exit|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup-t22`. A change to any decision-critical rule defines a new derivative, not a silent update to this identity.

## Economic mechanism

### Source-reported

The porter prose states the method tracks 20-day highest/lowest prices to locate reversal points, arms a 5-day monitoring period on each new extreme, trades long and short inside those windows, and warns of directional-market losses, large drawdowns, overfitting and parameter sensitivity, listing stop-loss optimization only as future work. No sample metric, table, figure, or performance number of any kind ships anywhere in the payload or the ported prose — this record adopts no source-reported performance.

### Research interpretation

A trailing-new-high ratchet with a time-decay leash, not a level breakout: there is no band to cross — entry fires on the single bar whose close strictly exceeds all 19 prior closes plus the 20th-back close (a refresh event), and the position then survives only while refreshes keep arriving; five consecutive non-refresh closes later the counter hits zero and the full position is exited on a pure timer with no price level involved. Unlike Donchian/channel records the exit has no price rail at all; unlike confirmation-count records (2-of-3 majority, streak chains) the counter here measures silence since the last event rather than clustering of events. The prose "reversal" framing is not adopted — the code buys fresh strength and holds it on a leash; whether that fades or follows through is an empirical question, never a claimed edge. No performance assertion is made.

## Signal

1. **Inputs and clock:** one contiguous, chronological real Binance BTC-USDT spot **1d** OHLCV sequence indexed t=0,1,...; each opening timestamp T[t] must be UTC day-aligned and T[t+1]-T[t]=86400 seconds. Require finite O,H,L,C>0, H>=max(O,C), L<=min(O,C), H>=L, and finite V>=0 for every row. Abort on gaps, duplicates, missing prices, malformed bars, unavailable last candle or out-of-order timestamps. No interpolation, synthetic price, full-sample fitting or partial candles. Bar t's completed values become available only at E[t]=T[t]+86400, not at T[t].
2. **Refresh event (verbatim):** for t>=20 with all twenty-one closes C[t-20..t] finite positive, `newHigh[t] = (C[t] > max(C[t-20..t-1]))` with strict `>` on the event leg (equality never refreshes). Bars t<20 print no event (Pine `ta.highest` returns na — unavailable history reads as false downstream, never fabricated). Close-only arithmetic; no price smoothing anywhere.
3. **Latch state (verbatim):** `counter` starts 0 with `armed=false`. On a trigger bar (`newHigh[t]` true): `counter:=5`, `armed:=true`. On a non-trigger bar with `counter>0`: `counter-=1` (armed stays true). On a non-trigger bar with `counter==0`: `armed:=false`. The low-leg latch (`window_low`, `lowDecayCounter`, `isLowPeriod`) is order-unreachable at pinned `allowShort=false` and is excluded from the specified signal — compute-and-ignore at most, never signal-read.
4. **Warmup/entry:** start FLAT, zero BTC and 10,000 USDT. No trading for t=0..21; first possible completed-bar decision is **t=22** (structural minimum is t=20 for `highest[1]`; 22 adds predeclared researcher margin and is part of the frozen identity). Indicators may be computed earlier but must never backfill a position before t=22.
5. **BUY scheduling:** if FLAT, no pending order, t>=22, and t is strictly later than any prior exit-fill bar, a trigger event `newHigh[t]` true stores exactly one BUY instruction from the t signal (level-triggered on the refresh event, matching the source `if (isHighPeriod and counter == decay)` with pyramiding 0 — refires while LONG are language no-ops). Dispatch at row t+1 only; idealized historical MARKET full fill uses **observed** Close[t+1] with economic effective time E[t+1]. Never use any t+1 values to decide the t entry. If t+1 is absent, no fill. Require actual positive close and cash >=Q*price*(1+f), Q=Decimal("0.001") BTC and f=Decimal("0.001"); otherwise abort the research segment rather than invent a fill.
6. **No bracket:** there is no stop/target/trailing/time exit in this derivative, matching the source payload's census-verified complete absence of any risk leg and its prose admission that stop-loss is future work. Absence here is an explicit disclosed choice, not a hidden default.
7. **Exit and priority:** while LONG and no pending order, at each later completed bar u (never on the BUY fill bar — exits evaluate only in confirmed LONG state), `armed[u] and counter[u]==0` true schedules a full SELL at row u+1 with idealized MARKET fill at its actual observed close effective E[u+1]; all other bars mean HOLD. Entry events (`counter==5`) and exit events (`counter==0`) are mutually exclusive on every bar by construction, so no same-bar ordering assumption exists. No same-bar roundtrip.
8. **Order and re-entry state:** one position and at most one pending order. Pending bars ignore all signals. A confirmed full SELL returns to FLAT, records its fill bar and clears state; any later completed bar with `newHigh` true may re-enter, with no cooldown and no DCA. Rejected/partial/duplicate/ambiguous BUY or SELL fills, missing price, or insufficient actual data abort the research segment, not silently mutate inventory. A last-row signal without a subsequent observed candle is unfilled; at sample end mark open inventory only at last actual completed close, separately from realized PnL, with no fabricated forced liquidation.
9. **Explicitly disabled:** short/borrow (both short legs unreachable at pinned `allowShort=false`), futures/perpetuals, margin/leverage/funding, pyramiding (Pine v5 default 0 pinned: no same-direction adds while positioned), DCA/safety orders, concurrent markets/shared capital, partial exits, dynamic sizing/compounding (source 100%-equity sizing explicitly replaced), maker/limit/next-open orders, intrabar stops, trailing, time exit, ROI ladders, the dead `startDate` input, the constant `inTradeWindow`, the low-leg latch, source futures/next-bar-open timing, and all `plot` display plumbing. No simultaneous or hedged positions.

## Required data

One real Binance BTC-USDT spot 1d OHLCV feed; the specified signal reads close only (H/L/V feed continuity validation only; low never signal-read in this derivative, volume never read anywhere). No external symbols, order book, futures funding, non-OHLCV data, secondary timeframes, fitting or future extrema. Validate candle continuity and all observed fill prices **before** the pinned engine's feature merge/dropna. Decisions occur at E[t], fills at E[t+1] in the idealized historical model, regardless of the native feed's opening timestamp. All refresh/latch reads use only <=t completed bars. Non-positive prices abort.

## Execution assumptions

**Pinned GitHub-inspected benchmark (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Immutable raw-file inspection this run of `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993 bytes; INTERVALS declares `1h` and `1d`), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913 bytes; MARKET path fills at the row's actual close with `filled_amount_quote`/`cum_fees_quote` accumulation, returns `CloseType.POSITION_HOLD`), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (39,071 bytes; `BacktestPositionHold`, `simulate_execution` calling `controller.determine_executor_actions()` with `CreateExecutorAction`), and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (8,823 bytes; line 140 `get_price_by_type` missing-price fallback). Prior Alpha PR #414 reports independent package/source correspondence; no wheel/image digest rehash in this run.

- **Actual feed:** pinned BinanceSpotCandles declares `1d`; Binance REST row[0] is **opening timestamp**, row[1..5] supplies real OHLCV. No synthetic candles, inferred fill prices, or silent forward filling. `BacktestingEngineBase.prepare_market_data` can merge features and drop missing rows; a pre-engine strict continuity/validity check is mandatory.
- **Actual action path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction`. A future minimal candidate-specific controller (not yet implemented) must preserve t's latch/pending state, delay dispatch to t+1, and issue `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`; no API name alone is asserted to implement this strategy.
- **Actual bounded fill:** MARKET dispatch on t+1 yields an idealized **t+1 close** fill at that row's actual close, not the source backtester's next-bar-open fill and not an achievable live post-close market price. Native fill row timestamp is an **opening** timestamp; economic effective fill time must be normalized to E[t+1], never reported as T[t+1].
- **Position and fee ledger:** pinned `BacktestPositionHold` nets opposite BUY/SELL base quantities and reports gross realized PnL while fees accumulate separately. Maintain a persistent confirmed-fill ledger (`terminated_executors_window=None` or equivalent) and explicit research cash/inventory: BUY cash `-=Q*Pb*(1+f)`, SELL cash `+=Q*Ps*(1-f)`, net realized round-trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. The fee `f=0.001` is a **hypothetical 0.1% quote-notional fee per filled side**, not a verified Binance fee tier. Engine float-ledger internals are not asserted equal to research-side Decimal bookkeeping; any fill/ledger ambiguity aborts the segment instead of being rounded into a fill. Never call gross engine PnL net. Spot funding is **not applicable**, not fabricated zero perpetual funding.
- **Pure-research precision model (no exchange-spec gating):** this derivative adopts a pure-research fixed-quantity Decimal model unconstrained by exchange specifications — there is deliberately no trading-rules snapshot, no minimum-quantity/step-size/minimum-notional gate, and no precision/validity precondition on fills. Live minimum order size, quantity steps, minimum notionals, and fee tiers are explicitly out of scope and unasserted; fills are idealized historical close fills, never claimed as exchange-acceptable orders.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on a missing price; explicitly **forbid** that fallback. Reject absent/nonpositive observed closes, partial fills and ambiguous position accounting rather than inventing economics. Simulator's idealized full fill does not prove real spread, slippage, liquidity, dynamic fee or latency. The future controller, real execution and package binary are **not** independently validated; this record claims only the bounded pinned historical close-fill primitive.

## Evidence

### Source-reported

FMZ 442621 (porter ChaoZhang, page Created 2024-02-23; Pine v5 `New Highs and Lows Momentum Strategy`): 20-bar close-refresh event, 5-bar decay counter, long entry on refresh with full exit on counter-zero, short legs pinned unreachable by `allowShort=false`, no risk leg (prose lists stop-loss as future work), Futures_Binance BTC_USDT 1d backtest stanza (2023-02-16 → 2024-02-22, basePeriod 1h). No original backtest result is adopted.

### Independently reproduced

**None for strategy events, profits or outcomes.** No Pine parity run, candidate-specific Hummingbot run, Qlib backtest, event-level parity, actual fills, installed package hash, OOS, Survivor or HB Certified claim. Only the **page prose/argument table and the existing pinned source-code engine/data/executor/fee paths** were directly inspected via the stable FMZ URL and immutable raw files at the pinned commit. Alpha PR #414 is prior correspondence evidence, not a claim of re-execution this cycle.

### Negative evidence

Source futures market, February-2023→February-2024 window, and next-bar-open fill timing are **explicitly replaced**, not source-native rules. The porter prose price-extreme sentence (prior high/low), long/short alternation sentence, start-date-gate sentence, and momentum-indicator sentence are fenced as unreliable and never gate an order. The `startDate` input, `inTradeWindow` constant, low-leg latch, and all `plot` plumbing never gate a reachable order. Idealized close fills and assumed fees do not prove exchange execution. No realistic live fills or funding are asserted.

**Six-gate proposal, pending independent Hermes Auditor:**
1. Determinism: strict close-refresh inequality plus counter latch with verbatim inputs 20/5/false, equivalence proof, mutual-exclusion of entry/exit events, t=22 warmup, single-unit no-op refires.
2. Direction: Binance BTC-USDT spot LONG/FLAT; both short legs unreachable at pinned defaults.
3. Entry/exit/risk: refresh-event entry, decay-zero full exit, disclosed absence of any risk leg.
4. State: fixed 0.001 BTC, one pending order/position, research cash and fee ledger, no DCA/concurrency, fresh event after exit, abort on ambiguous fills.
5. Pinned model: directly inspected actual 1d feed, controller/action, MARKET close fill, POSITION_HOLD and fee paths; pure-research precision model with no exchange-spec gating; no unsupported next-bar/intrabar/funding assumption.
6. Causality: refresh needs t>=20, trading from t=22, t completed signal -> t+1 completed-close economic fill, no future bars, opening timestamp never misrepresented as close availability.

**Dedup snapshot:** at `main=1144413`, 388 root Markdown files = 386 strategy records + 2 READMEs, matching README pool count 386 (existing records were **not** exhaustively re-audited for PASS frontmatter; count equality is not represented as a full admission census). Repo-wide `grep -ril` over root `*.md` returned zero signal-use for `442621`, `new-highs-and-lows`, `decay-counter`, `decay counter`, `highDecay`, `new highs`, `monitoring period`, `paulcpk`, `MACDCrossoverWithTrend`, `jQohKDR0`, `long-leg-doji`; GitHub issue search over open PRs returned 0 hits for `442621` and 0 for `decay`; all ten open `research/*` PR heads/titles were checked for source identity with no match. Nearest pool neighbors are materially different constructions: `donchian-20-10-breakout` (Forven S01509 — high/low price-band breakout with opposite-band exit and a date window, 1h); `forven-naked-donchian-20` (prior high/low band cross with a low-band exit, 1d); `fmz-482890-quantile-band-trigger-confirm` (bar counts used for confirmation, not decay); `inside-bar-failure-fade-time-exit` (pattern entry with time exit, not a refresh event). No pool record enters on a close-refresh event with a priceless decay-counter exit.

## Falsification plan

With separate authorization, materialize only a minimal candidate-specific controller, validate the strict t/t+1 clock and actual close inputs, refresh strictness (equality never refreshes; `close[t] > close[t-20]` alone never suffices), latch transitions (trigger→5, silent decrement, zero-bar exit, next-bar disarm), warmup flatness through t=21, post-exit re-entry, fail-closed invalid fills and fee-net position accounting. Before large-scale Qlib screening on a newly unverified execution path, obtain representative Hummingbot/Qlib event-level parity for signals, fills, fees and states. Separately assess fee-net IS/OOS performance; no such test is run by this Scout.

## Crypto portability

BTC-USDT spot 1d is researcher-selected (the executable stanza itself trades BTC_USDT at `period: 1d`, so the frame and coin are source-native; only the venue leg moves from futures to spot). Any futures, 3x/5x, DCA BO/SO 6/6/6, other coin or execution model is downstream optional research requiring a separately specified derivative and verified execution/cost/funding path. No implied transfer of results.

## Limitations

No Pine parity run; source-native equivalence unverified beyond byte-level rule transcription plus the refresh-equivalence proof. Derived spot venue, long-flat posture, next-close fill, fixed quantity, warmup, and hypothetical fees materially differ from the source backtest. Trend-persistence regimes can hold the position through long drawdowns with no stop; silent chop produces repeated 5-bar roundtrips. Idealized close fills and assumed fees do not prove exchange execution. No installed package rehash, strategy backtest, Qlib parity, profitability or live authorization. Thin-volume regimes are untested.

## Implementation status

`not-implemented`: research specification only. No controller, Qlib recipe, trading deployment, backtest, container, n8n or cron changes.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, not self-approved. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns README bookkeeping after an accepted merge. Scout does not approve, merge, close or write main.

## Related Wiki records

None created or modified.

## Sources

- https://www.fmz.com/strategy/442621 — ChaoZhang reversal-momentum breakout Pine v5, page Created 2024-02-23; live page inspected 2026-10-27 (785,874 bytes), full code read via immutable mirror.
- https://github.com/fmzquant/strategies/blob/master/%E5%8F%8D%E8%BD%AC%E5%8A%A8%E9%87%8F%E7%A0%B4%E7%AA%97%E7%AD%96%E7%95%A5Reversal-Momentum-Breakout-Strategy.md — immutable mirror at commit 7853bb2bf262c4567ac238d3552d97f0e50cb801, blob d6e67b10026fd275901c67c37c801192d6f1fd60, inspected 2026-10-27.
- https://raw.githubusercontent.com/HCH725/hummingbot/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source (feed constants, order executor simulator, backtesting engine base, data provider), inspected through immutable raw files 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier package/source correspondence evidence; not re-run here.
