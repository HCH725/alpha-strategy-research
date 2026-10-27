---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 446538 Vector-candle ChoCH count long-flat BTC-USDT spot 1h independent derivative"
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
source_as_of: 2024-03-29
sources:
  - https://www.fmz.com/strategy/446538
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The page ZH/EN porter prose describes the traded signal as a structure break (close below prior low for red ChoCH / close above prior high for green BOS) combined with a vector candle, but the pinned Pine code assigns those structure-break comparisons only to display-only plot variables (isRedChoCH / isGreenBOS) and the actual order predicates (buyCondition / sellCondition) read solely the 2-of-3 volume-color majority count, ignoring prior high/low entirely. The code governs everywhere; the prose structure-break sentence is fenced as unreliable and no prose sentence enters any gate."
---

# Vector Candle ChoCH Count — volume-climax majority latch, long-flat research derivative

## Provenance

**First-party FMZ source:** strategy `446538`《基于向量蜡烛图的通道突破与自定义ChoCH策略》(Vector-Candle-based Channel Breakout and Custom ChoCH Strategy), porter `ChaoZhang`, page `Created: 2024-03-29 14:45:57` (adopted as `source_as_of`; page shows 58 copies / 1,258 hits / 通用策略). Inspected **2026-10-27** via the stable public page (HTTP 200, prose fully visible without login, Pine block gated behind login showing 264 bytes / 12 lines) with the full executable payload read verbatim from the immutable public mirror `fmzquant/strategies@7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified repo HEAD via API this run), path `基于向量蜡烛图的通道突破与自定义ChoCH策略-Vector-Candle-based-Channel-Breakout-and-Custom-ChoCH-Strategy.md`, blob `b73ca97870b0f7cfcc2302012696fcb7a4e3b4b6`, 9,518 bytes, `> Detail` block containing `https://www.fmz.com/strategy/446538`. No source-native, author-identical or author-performance reproduction is claimed.

**Verified source-code facts (mirror bytes):** `//@version=4`; `strategy("Custom ChoCH and BOS Strategy with Vector Candles", overlay=true)` — no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no commission/sizing argument ships anywhere (Pine v4 defaults govern the source backtest: single evaluation per completed bar, next-bar fills, pyramiding 0). `length = input(10)` / `volMultiplier = input(2.0)` / `confirmationCandles = input(3)` (all three frozen at defaults). `avgVol = sma(volume, length)`. `vectorCandleRed = (close < open) and (volume > avgVol * volMultiplier) ? 1.0 : 0.0`. `vectorCandleGreen = (close > open) and (volume > avgVol * volMultiplier) ? 1.0 : 0.0`. `vectorCandleBlue = (close < open) and (volume > avgVol * 1.5)` / `vectorCandlePurple = (close > open) and (volume > avgVol * 1.5)` — blue/purple are plot-only, never order-read. `isRedChoCH = vectorCandleRed > 0 and (close < low[1])` / `isGreenBOS = vectorCandleGreen > 0 and (close > high[1])` — both feed only `plotshape`, never any order call. `redChoCHConfirmed = (sum(vectorCandleRed, confirmationCandles) >= 2) ? 1.0 : 0.0`; `greenBOSConfirmed = (sum(vectorCandleGreen, confirmationCandles) >= 2) ? 1.0 : 0.0`. `buyCondition = redChoCHConfirmed > 0`; `sellCondition = greenBOSConfirmed > 0`. `if (buyCondition) strategy.entry("Buy", strategy.long)`; `if (sellCondition) strategy.close("Buy")`. Text census over the payload: 1 `strategy.entry` (long only) / 1 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `crossover`/`crossunder`/`ta.cross` / 0 `request.*`/`security(` / 0 `barstate` / 0 `timeframe` / 1 `sma` / 2 `sum` / 0 `pyramiding`. Backtest stanza prints `start: 2024-02-01 00:00:00`, `end: 2024-02-29 23:59:59`, `period: 1h`, `basePeriod: 15m`, `Futures_Binance BTC_USDT` — quoted as printed, never adopted as research economics (the 1-month window is explicitly not adopted).

**Explicit independent derivative, NOT lossless source reproduction:** The researcher chooses Binance BTC-USDT **spot 1h**, LONG/FLAT only (source has no short leg — long entry plus flat exit is source-native posture, venue leg alone moves futures to spot), fixed 0.001 BTC on 10,000 USDT research cash, completed-close signal to next completed-close historical MARKET fill, hypothetical 0.1% fee per filled side, defaults 10 / 2.0 / 3 pinned, the pure volume-color majority count pinned as the sole traded rule with the `close<low[1]` / `close>high[1]` structure breaks fenced as display-only, and a 25-bar warmup holding FLAT. These choices materially change trade events and economics and are researcher-authored.

**Frozen derived identity:** `FMZ:446538|2024-03-29|vector-candle-choch-count-v1|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:UTC1h|avgVol-sma10|volmult-2.0|confirm-3|count-ge2|red-entry-green-exit|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup-t25`. A change to any decision-critical rule defines a new derivative, not a silent update to this identity.

## Economic mechanism

### Source-reported

The porter prose states the method combines vector (volume-amplified) candles with channel breakout and ChoCH/BOS structure recognition to capture breakout moves, confirms signals over a fixed number of confirmation candles to filter noise, opens long on confirmed red ChoCH and closes on confirmed green BOS, and warns the strategy ships no stop-loss and may suffer in choppy markets with frequent false signals. No sample metric, table, figure, or performance number of any kind ships anywhere in the payload or the ported prose — this record adopts no source-reported performance.

### Research interpretation

A volume-climax absorption counter, not a level breakout: each completed bar is colored red only when it closes down on volume above twice its own trailing 10-bar average, green only on the up-close mirror; doji and normal-volume bars are colorless. Entry fires when at least 2 of the last 3 completed bars are red (capitulation clustering — sellers exhausting into falling closes on expanding volume); exit fires on the symmetric 2-of-3 green distribution cluster. Because one bar can carry at most one color, entry and exit are mutually exclusive on every bar by construction, so chop produces holds rather than whipsaw reversals. Unlike band/channel records there is no price level, no average of price, and no dispersion anywhere — the only trailing statistic is a volume mean used strictly as a bar-color multiplier gate. Unlike streak-count records the window is a majority vote (2-of-3), never a consecutive chain. The exit is the mirror count, so holding time ends only on opposite-side distribution clustering; there is no stop, target, or timer. No performance assertion is made.

## Signal

1. **Inputs and clock:** one contiguous, chronological real Binance BTC-USDT spot **1h** OHLCV sequence indexed t=0,1,...; each opening timestamp T[t] must be UTC hour-aligned and T[t+1]-T[t]=3600 seconds. Require finite O,H,L,C>0, H>=max(O,C), L<=min(O,C), H>=L, and finite V>=0 for every row. Abort on gaps, duplicates, missing prices, malformed bars, unavailable last candle or out-of-order timestamps. No interpolation, synthetic price, full-sample fitting or partial candles. Bar t's completed values become available only at E[t]=T[t]+3600, not at T[t].
2. **Volume mean (verbatim):** for t>=9 with all ten volumes V[t-9..t] finite non-negative, `avgVol[t] = (1/10)*SUM(V[t-9..t])`. Bars t<9 print no mean (Pine `sma` returns na — unavailable history reads as false downstream, never fabricated). Float arithmetic on volumes only; no price smoothing anywhere.
3. **Bar colors (verbatim, strict):** for t>=9 with avgVol[t] finite positive, `red[t] = 1` iff `C[t]<O[t] AND V[t]>avgVol[t]*2.0`, else 0; `green[t] = 1` iff `C[t]>O[t] AND V[t]>avgVol[t]*2.0`, else 0. Equality on either leg makes that color 0: doji (`C==O`) is colorless, and volume exactly at 2.0x is colorless (strict `>`). Each bar carries at most one color; blue/purple 1.5x variants and the `close<low[1]` / `close>high[1]` structure comparisons are display-only and never enter any rule below.
4. **Majority count (verbatim):** for t>=2, `redCount[t] = red[t-2]+red[t-1]+red[t]`; `greenCount[t] = green[t-2]+green[t-1]+green[t]` (Pine `sum(x,3)` over completed bars). Entry predicate `entry[t] = (redCount[t]>=2)`; exit predicate `exitP[t] = (greenCount[t]>=2)`. Both predicates can never be true on the same bar (they would require at least 4 colored bars in 3 slots with each bar single-colored — a counting impossibility). Bars t<2 print no predicate.
5. **Warmup/entry:** start FLAT, zero BTC and 10,000 USDT. No trading for t=0..24; first possible completed-bar decision is **t=25** (structural minimum is t=9 for `sma(volume,10)` plus the 3-bar count; 25 adds predeclared researcher margin and is part of the frozen identity). Indicators may be computed earlier but must never backfill a position before t=25.
6. **BUY scheduling:** if FLAT, no pending order, t>=25, and t is strictly later than any prior exit-fill bar, an entry event is `entry[t]` true while FLAT (level-triggered on the confirmed count, matching the source `if (buyCondition)` with pyramiding 0 — refires while LONG are language no-ops). Store exactly one BUY instruction from the t signal. Dispatch at row t+1 only; idealized historical MARKET full fill uses **observed** Close[t+1] with economic effective time E[t+1]. Never use any t+1 values to decide the t entry. If t+1 is absent, no fill. Require actual positive close and cash >=Q*price*(1+f), Q=Decimal("0.001") BTC and f=Decimal("0.001"); otherwise abort the research segment rather than invent a fill.
7. **No bracket:** there is no stop/target/trailing/time exit in this derivative, matching the source payload's census-verified complete absence of any risk leg and its prose admission that no stop-loss ships. Absence here is an explicit disclosed choice, not a hidden default.
8. **Exit and priority:** while LONG and no pending order, at each later completed bar u (never on the BUY fill bar — exits evaluate only in confirmed LONG state), `exitP[u]` true schedules a full SELL at row u+1 with idealized MARKET fill at its actual observed close effective E[u+1]; count-hold bars mean HOLD. Entry and exit predicates are mutually exclusive on every bar (counting proof above), so no same-bar ordering assumption exists. No same-bar roundtrip.
9. **Order and re-entry state:** one position and at most one pending order. A confirmed full SELL returns to FLAT, records its fill bar and clears state; any later completed bar with `entry` true may re-enter, with no cooldown and no DCA. Pending bars ignore all signals. Rejected/partial/duplicate/ambiguous BUY or SELL fills, missing price, or insufficient actual data abort the research segment, not silently mutate inventory. A last-row signal without a subsequent observed candle is unfilled; at sample end mark open inventory only at last actual completed close, separately from realized PnL, with no fabricated forced liquidation.
10. **Explicitly disabled:** short/borrow, futures/perpetuals, margin/leverage/funding, pyramiding (Pine v4 default 0 pinned: no same-direction adds while positioned), DCA/safety orders, concurrent markets/shared capital, partial exits, dynamic sizing/compounding, maker/limit/next-open orders, intrabar stops, trailing, time exit, the blue/purple 1.5x colors, the `isRedChoCH`/`isGreenBOS` structure-break plots, source futures/next-bar timing, and all `plotshape`/`plotchar` display plumbing. No simultaneous or hedged positions.

## Required data

One real Binance BTC-USDT spot 1h OHLCV feed; signal reads close, open, and volume only (H/L feed continuity validation only; prior high/low never signal-read in this derivative). No external symbols, order book, futures funding, non-OHLCV data, secondary timeframes, fitting or future extrema. Validate candle continuity and all observed fill prices **before** the pinned engine's feature merge/dropna. Decisions occur at E[t], fills at E[t+1] in the idealized historical model, regardless of the native feed's opening timestamp. All mean/color/count reads use only <=t completed bars. Non-positive prices abort.

## Execution assumptions

**Pinned GitHub-inspected benchmark (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Immutable raw-file inspection this run of `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993 bytes; INTERVALS declares `1h` and `1d`), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913 bytes; MARKET path fills at the row's actual close with `filled_amount_quote`/`cum_fees_quote` accumulation, returns `CloseType.POSITION_HOLD`), `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` (39,071 bytes; `BacktestPositionHold`, `simulate_execution` calling `controller.determine_executor_actions()` with `CreateExecutorAction`), and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (8,823 bytes; line 140 `get_price_by_type` missing-price fallback). Prior Alpha PR #414 reports independent package/source correspondence; no wheel/image digest rehash in this run.

- **Actual feed:** pinned BinanceSpotCandles declares `1h`; Binance REST row[0] is **opening timestamp**, row[1..5] supplies real OHLCV. No synthetic candles, inferred fill prices, or silent forward filling. `BacktestingEngineBase.prepare_market_data` can merge features and drop missing rows; a pre-engine strict continuity/validity check is mandatory.
- **Actual action path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction`. A future minimal candidate-specific controller (not yet implemented) must preserve t's count/pending state, delay dispatch to t+1, and issue `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`; no API name alone is asserted to implement this strategy.
- **Actual bounded fill:** MARKET dispatch on t+1 yields an idealized **t+1 close** fill at that row's actual close, not the source backtester's next-bar fill and not an achievable live post-close market price. Native fill row timestamp is an **opening** timestamp; economic effective fill time must be normalized to E[t+1], never reported as T[t+1].
- **Position and fee ledger:** pinned `BacktestPositionHold` nets opposite BUY/SELL base quantities and reports gross realized PnL while fees accumulate separately. Maintain a persistent confirmed-fill ledger (`terminated_executors_window=None` or equivalent) and explicit research cash/inventory: BUY cash `-=Q*Pb*(1+f)`, SELL cash `+=Q*Ps*(1-f)`, net realized round-trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. The fee `f=0.001` is a **hypothetical 0.1% quote-notional fee per filled side**, not a verified Binance fee tier. Engine float-ledger internals are not asserted equal to research-side Decimal bookkeeping; any fill/ledger ambiguity aborts the segment instead of being rounded into a fill. Never call gross engine PnL net. Spot funding is **not applicable**, not fabricated zero perpetual funding.
- **Pure-research precision model (no exchange-spec gating):** this derivative adopts a pure-research fixed-quantity Decimal model unconstrained by exchange specifications — there is deliberately no trading-rules snapshot, no minimum-quantity/step-size/minimum-notional gate, and no precision/validity precondition on fills. Live minimum order size, quantity steps, minimum notionals, and fee tiers are explicitly out of scope and unasserted; fills are idealized historical close fills, never claimed as exchange-acceptable orders.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on a missing price; explicitly **forbid** that fallback. Reject absent/nonpositive observed closes, partial fills and ambiguous position accounting rather than inventing economics. Simulator's idealized full fill does not prove real spread, slippage, liquidity, dynamic fee or latency. The future controller, real execution and package binary are **not** independently validated; this record claims only the bounded pinned historical close-fill primitive.

## Evidence

### Source-reported

FMZ 446538 (porter ChaoZhang, 2024-03-29; Pine v4 `Custom ChoCH and BOS Strategy with Vector Candles`): volume mean over 10 bars, 2.0x red/green vector colors (1.5x blue/purple display-only), 3-bar confirmation window with threshold 2, long entry on red majority and flat exit on green majority, no risk leg (prose admits no stop-loss), Futures_Binance BTC_USDT 1h backtest stanza (2024-02-01 → 2024-02-29, basePeriod 15m). No original backtest result is adopted.

### Independently reproduced

**None for strategy events, profits or outcomes.** No Pine parity run, candidate-specific Hummingbot run, Qlib backtest, event-level parity, actual fills, installed package hash, OOS, Survivor or HB Certified claim. Only the **page prose and the existing pinned source-code engine/data/executor/fee paths** were directly inspected via the stable FMZ URL and immutable raw files at the pinned commit. Alpha PR #414 is prior correspondence evidence, not a claim of re-execution this cycle.

### Negative evidence

Source futures market, February-2024 window, and next-bar fill timing are **explicitly replaced**, not source-native rules. The porter prose structure-break sentence (prior high/low) is fenced as display-only and never gates an order. The blue/purple 1.5x colors, `isRedChoCH`/`isGreenBOS` plots, and all `plotshape`/`plotchar` plumbing never gate an order. Idealized close fills and assumed fees do not prove exchange execution. No realistic live fills or funding are asserted.

**Six-gate proposal, pending independent Hermes Auditor:**
1. Determinism: volume mean plus strict color inequalities plus 2-of-3 majority count, verbatim inputs 10/2.0/3, equality-proof legs, mutual-exclusion counting proof, t=25 warmup, level-triggered events with single-unit no-op refires.
2. Direction: Binance BTC-USDT spot LONG/FLAT; no short leg exists anywhere in the payload.
3. Entry/exit/risk: red-majority entry, green-majority full exit, disclosed absence of any risk leg.
4. State: fixed 0.001 BTC, one pending order/position, research cash and fee ledger, no DCA/concurrency, fresh event after exit, abort on ambiguous fills.
5. Pinned model: directly inspected actual 1h feed, controller/action, MARKET close fill, POSITION_HOLD and fee paths; pure-research precision model with no exchange-spec gating; no unsupported next-bar/intrabar/funding assumption.
6. Causality: mean needs t>=9, counts need t>=2, trading from t=25, t completed signal -> t+1 completed-close economic fill, no future bars, opening timestamp never misrepresented as close availability.

**Dedup snapshot:** at `main=830d218`, 387 root Markdown files = 385 strategy records + 2 READMEs, matching README pool count 385 (existing records were **not** exhaustively re-audited for PASS frontmatter; count equality is not represented as a full admission census). Repo-wide `grep -ril` over root `*.md` returned zero signal-use for `446538`, `vector-candle`, `vector candle`, `redchoch`, `greenbos`, `choch`, `change of character`, `break of structure`; all ten open `research/*` PR titles/bodies were checked for source identity with no match. Nearest pool neighbors are materially different constructions: `gervais-kaniel-mingelgrin-high-volume-premium` (volume as a strict 50-bar maximum premium with unconditional direction and a 20-bar timer exit — no color, no count); `forven-atr-volume-breakout` (volume as a breakout-continuation gate, not a down/up-close majority vote); `freqtrade-strategy005-volume-surge-fisher-washout` (5m Fisher washout plus EMA gate, not a pure volume-color count); dip-buy RSI/extreme records (price/oscillator extremes, never volume multiplicity). No pool record counts colored high-volume bars with a symmetric majority exit.

## Falsification plan

With separate authorization, materialize only a minimal candidate-specific controller, validate the strict t/t+1 clock and actual close inputs, color strictness (doji and exactly-2.0x bars color nothing), count window (2-of-3 majority, mutual exclusion on every bar), warmup flatness through t=24, post-exit re-entry, fail-closed invalid fills and fee-net position accounting. Before large-scale Qlib screening on a newly unverified execution path, obtain representative Hummingbot/Qlib event-level parity for signals, fills, fees and states. Separately assess fee-net IS/OOS performance; no such test is run by this Scout.

## Crypto portability

BTC-USDT spot 1h is researcher-selected (the executable stanza itself trades BTC_USDT at `period: 1h`, so the frame and coin are source-native; only the venue leg moves from futures to spot). Any futures, 3x/5x, DCA BO/SO 6/6/6, other coin or execution model is downstream optional research requiring a separately specified derivative and verified execution/cost/funding path. No implied transfer of results.

## Limitations

No Pine parity run; source-native equivalence unverified beyond byte-level rule transcription. Derived spot venue, long-flat posture, next-close fill, fixed quantity, warmup, and hypothetical fees materially differ from the source backtest. The always-counted book means the position is either long or flat-needing-re-entry with no neutral rest state beyond warmup and post-exit bars. Idealized close fills and assumed fees do not prove exchange execution. No installed package rehash, strategy backtest, Qlib parity, profitability or live authorization. Thin-volume regimes are untested.

## Implementation status

`not-implemented`: research specification only. No controller, Qlib recipe, trading deployment, backtest, container, n8n or cron changes.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, not self-approved. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns README bookkeeping after an accepted merge. Scout does not approve, merge, close or write main.

## Related Wiki records

None created or modified.

## Sources

- https://www.fmz.com/strategy/446538 — ChaoZhang vector-candle ChoCH/BOS Pine v4, page Created 2024-03-29; live prose inspected 2026-10-27, full code read via immutable mirror.
- https://github.com/fmzquant/strategies/blob/master/%E5%9F%BA%E4%BA%8E%E5%90%91%E9%87%8F%E8%9C%A1%E7%83%9B%E5%9B%BE%E7%9A%84%E9%80%9A%E9%81%93%E7%AA%81%E7%A0%B4%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89ChoCH%E7%AD%96%E7%95%A5-Vector-Candle-based-Channel-Breakout-and-Custom-ChoCH-Strategy.md — immutable mirror at commit 7853bb2bf262c4567ac238d3552d97f0e50cb801, blob b73ca97870b0f7cfcc2302012696fcb7a4e3b4b6, inspected 2026-10-27.
- https://raw.githubusercontent.com/HCH725/hummingbot/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source (feed constants, order executor simulator, backtesting engine base, data provider), inspected through immutable raw files 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier package/source correspondence evidence; not re-run here.
