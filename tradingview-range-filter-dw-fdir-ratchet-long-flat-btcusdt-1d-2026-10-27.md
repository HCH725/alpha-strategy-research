---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "TradingView Range Filter DW fdir ratchet long-flat BTC-USDT spot 1d independent derivative"
created: 2026-10-27
updated: 2026-10-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - tradingview
  - source-backed
status: research-only
confidence: medium
source_as_of: 2020-11-01
sources:
  - https://www.tradingview.com/script/lut7sBgG-Range-Filter-DW/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Range Filter [DW] — Average-Change double-EMA dead-zone ratchet fdir long-flat research derivative

## Provenance

**First-party TradingView source:** `Range Filter [DW]` by DonovanWall, script ID **`lut7sBgG`**, Pine **v4** `study` (indicator, 195 lines), published **2018-10-30**, migrated to v4 **2020-02-17**, rebuilt with array functions plus external trend output **2020-11-01**, tagged Editors' Picks / OPEN-SOURCE SCRIPT. Source code read verbatim in-page **2026-10-27** (header, all four Pine functions, all inputs, definitions, direction block, all outputs). No source-native, backtest-identical or author-performance reproduction is claimed.

**Verified source-code facts:** `Cond_EMA(x,cond,n)` samples every bar when `cond` is true and updates `ema+=(x-ema)*(2/(n+1))`, seeded with the first sampled value. `rng_size` with scale `Average Change` returns `qty*AC` where `AC=Cond_EMA(abs(x-x[1]),1,n)`. `rng_filt` Type 1 steps a persistent `rfilt` seeded with the first bar's `(h+l)/2`: `h-r>prev` sets `h-r`, `l+r<prev` sets `l+r`, otherwise it holds. `fdir` is `var 0.0`, set to `1` when `filt>filt[1]`, `-1` when `filt<filt[1]`, otherwise held. The external trend output `plot(fdir,display=display.none)` is documented by the author as `1` bullish / `-1` bearish. The file contains no `strategy.*` order, no stop/limit/trailing/time-exit, and no short-leg block.

**Explicit independent derivative, NOT lossless source reproduction:** The researcher freezes Type 1 / Close / 2.618 / Average Change / 14 / smooth-true / 27 / average-off, maps `fdir=+1` to BUY and `fdir=-1` to flat exit on Binance BTC-USDT **spot UTC 1d**, fixed 0.001 BTC, 10,000 USDT initial research cash, completed-close signal to next completed-close historical MARKET fill, and hypothetical 0.1% fee per filled side. The source demo chart (EURUSD 1h) is provenance only. These choices materially define trade events and are researcher-authored.

**Frozen derived identity:** `TV:lut7sBgG|DonovanWall|2020-11-01|independent-v1:2026-10-27|BinanceSpot:BTC-USDT:UTC1d|Type1-Close-2p618-AC14-smooth27-avoff|fdir-flip|t-signal-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-per-side|warmup-t60`. A change to any decision-critical rule defines a new derivative, not a silent update to this identity.

## Economic mechanism

### Source-reported

The author filters minor price action by gating moves against a smoothed average range (inspired by the QQE volatility filter but applied directly to price rather than to smoothed RSI), then plots the bands that would trigger the next filter movement. No realized return is adopted.

### Research interpretation

This independent derivative tests a self-stepping dead-zone trend state: the filter line only moves when price escapes it by more than the current double-smoothed range, and the traded signal is the line's own step direction (`fdir`), not a price-vs-band cross. Entries therefore require a range-normalized breakout of the filter's dead zone, and exits are the symmetric breakdown. No performance assertion is made.

## Signal

1. **Inputs and clock:** one contiguous, chronological real Binance BTC-USDT spot **UTC 1d** OHLCV sequence indexed t=0,1,...; each opening timestamp T[t] must be UTC midnight-aligned and T[t+1]-T[t]=86400 seconds. Require finite O,H,L,C>0, H>=max(O,C), L<=min(O,C), H>=L, and finite V>=0 for every row. Volume is validated for bar integrity but is **not** a signal input. Abort on gaps, duplicates, missing prices, negative volume, malformed bars, unavailable last candle or out-of-order timestamps. No interpolation, synthetic price, full-sample fitting or partial candles. Bar t's completed values become available only at E[t]=T[t]+86400, not at T[t].
2. **EMA closed form (researcher-specified):** `EMA_n` uses `alpha=2/(n+1)`, seeded with the first valid sampled value, float64, no intermediate rounding. This pins the Pine `Cond_EMA`-with-true-condition semantics explicitly rather than inheriting any library default.
3. **Range recursion:** `x[t]=close[t]` (Close movement source, so `(h+l)/2=close`). `AC[t]=EMA_14(|close[t]-close[t-1]|)`, first valid t=1. `r_raw[t]=2.618*AC[t]`. `r[t]=EMA_27(r_raw)`, seeded with the first valid `r_raw`. Any non-finite input invalidates bar t and aborts the research segment rather than fabricating a value.
4. **Filter recursion (Type 1):** `filt` seeds with `close[0]`. For each later completed bar: if `close[t]-r[t]>filt[t-1]` then `filt[t]=close[t]-r[t]`; else if `close[t]+r[t]<filt[t-1]` then `filt[t]=close[t]+r[t]`; else `filt[t]=filt[t-1]`. Strict inequalities: equality holds the line. A non-finite `r[t]` makes both comparisons false, so the line holds (Pine na semantics); a persistently non-finite range aborts the segment.
5. **Direction state:** `fdir` seeds `0.0`. `filt[t]>filt[t-1]` sets `+1`; `filt[t]<filt[t-1]` sets `-1`; otherwise the prior `fdir` is held, including the initial `0.0`. Bands `filt+/-r`, bar colors and fills are display-only and never traded.
6. **Warmup/entry:** start FLAT, zero BTC and 10,000 USDT. No trading for t=0..59; first possible completed-bar decision is **t=60** (EMA27 seed weight `(25/27)^60` is about 1%, so seed influence is negligible; EMA14 is long converged).
7. **BUY scheduling:** if FLAT, no pending order, t>=60, and t is strictly later than any prior exit-fill bar, an entry event is `fdir[t]==+1` with `fdir[t-1]!=+1` (strict flip; the initial `0.0` never equals `+1`). Store exactly one BUY instruction from the completed t signal. Dispatch at row t+1 only; idealized historical MARKET full fill uses **observed** Close[t+1] with economic effective time E[t+1]. Never use any t+1 values to decide the t entry. If t+1 is absent, no fill. Require actual positive close, valid size/rules and cash >=Q*price*(1+f), Q=Decimal("0.001") BTC and f=Decimal("0.001"); otherwise abort the research segment rather than invent a fill.
8. **No bracket:** there is no stop/target/trailing/time exit in this derivative, matching the source file's complete absence of any risk leg. The fdir breakdown exit below is the sole risk leg. Absence here is an explicit disclosed choice, not a hidden default.
9. **Exit and priority:** while LONG and no pending order, at each later completed bar u (never on the BUY fill bar), `fdir[u]==-1` schedules a full SELL at row u+1 with idealized MARKET fill at its actual observed close effective E[u+1]; otherwise HOLD. Entry requires FLAT and exit requires LONG, so no same-bar ordering assumption exists. No same-bar roundtrip.
10. **Order and re-entry state:** one position and at most one pending order. A confirmed full SELL returns to FLAT, records its fill bar and clears state; any later completed bar with a fresh `+1` flip may re-enter, with no cooldown and no DCA. Rejected/partial/duplicate/ambiguous BUY or SELL fills, missing price, or insufficient actual data abort the research segment, not silently mutate inventory. A last-row signal without a subsequent observed candle is unfilled; at sample end mark open inventory only at last actual completed close, separately from realized PnL, with no fabricated forced liquidation.
11. **Explicitly disabled:** short/borrow, futures/perpetuals, margin/leverage/funding, pyramiding, DCA/safety orders, concurrent markets/shared capital, partial exits, dynamic sizing/compounding, maker/limit/next-open orders, intrabar stops, trailing, time exit, Type 2 stepping, Wicks movement source, all non-Average-Change scales, filter-change averaging, and hidden executor defaults. No simultaneous or hedged positions.

## Required data

One real Binance BTC-USDT spot 1d OHLCV feed; close is the only signal input and volume is unused beyond bar-integrity validation. No external symbols, order book, futures funding, non-OHLCV data, secondary timeframes, fitting or future extrema. Validate candle continuity and all observed fill prices **before** the pinned engine's feature merge/dropna. Decisions occur at E[t], fills at E[t+1] in the idealized historical model, regardless of the native feed's opening timestamp. All recursion uses only <=t completed data. Non-finite range or missing candles aborts.

## Execution assumptions

**Pinned GitHub-inspected benchmark (2026-10-27):** `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`, package label `20260920`, `hummingbot/VERSION=dev-2.17.0`. Immutable raw-file inspection this run of `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (INTERVALS declares `1d`), `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (MARKET path fills at the row's actual close with `filled_amount_quote`/`cum_fees_quote` and returns `CloseType.POSITION_HOLD`), and `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (`get_price_by_type` missing-price fallback). Prior Alpha PR #414 reports independent package/source correspondence; no wheel/image digest rehash in this run.

- **Actual feed:** pinned BinanceSpotCandles declares `1d`; Binance REST row[0] is **opening timestamp**, row[1..5] supplies real OHLCV. No synthetic candles, inferred fill prices, or silent forward filling. `BacktestingEngineBase.prepare_market_data` can merge features and drop missing rows; a pre-engine strict continuity/validity check is mandatory.
- **Actual action path:** `BacktestingEngineBase.simulate_execution` calls `update_state(row)`, then `controller.determine_executor_actions()`, and simulates `CreateExecutorAction`. A future minimal candidate-specific controller (not yet implemented) must preserve t's fdir/flip/pending state, delay dispatch to t+1, and issue `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),position_action=OPEN/CLOSE,execution_strategy=MARKET,price=None,leverage=1)`; no API name alone is asserted to implement this strategy.
- **Actual bounded fill:** MARKET dispatch on t+1 yields an idealized **t+1 close** fill at that row's actual close, not an achievable live post-close market price. Native fill row timestamp is an **opening** timestamp; economic effective fill time must be normalized to E[t+1], never reported as T[t+1].
- **Position and fee ledger:** pinned `BacktestPositionHold` nets opposite BUY/SELL base quantities and reports gross realized PnL while fees accumulate separately. Maintain a persistent confirmed-fill ledger (`terminated_executors_window=None` or equivalent) and explicit research cash/inventory: BUY cash `-=Q*Pb*(1+f)`, SELL cash `+=Q*Ps*(1-f)`, net realized round-trip `Q*(Ps-Pb)-f*Q*(Pb+Ps)`. The fee `f=0.001` is a **hypothetical 0.1% quote-notional fee per filled side**, not a verified Binance fee tier. Engine float-ledger internals are not asserted equal to research-side Decimal bookkeeping; any fill/ledger ambiguity aborts the segment instead of being rounded into a fill. Never call gross engine PnL net. Spot funding is **not applicable**, not fabricated zero perpetual funding.
- **Fail-closed boundaries:** `BacktestingDataProvider.get_price_by_type` can return `Decimal("1")` on a missing price; explicitly **forbid** that fallback. Reject absent/nonpositive observed closes, negative or non-finite volume, invalid trading rules, unsupported precision/min-notional, partial fills and ambiguous position accounting rather than inventing economics. Simulator's idealized full fill does not prove real spread, slippage, liquidity, live minimum order/precision, dynamic fee or latency. The future controller, real execution and package binary are **not** independently validated; this record claims only the bounded pinned historical close-fill primitive.

## Evidence

### Source-reported

DonovanWall Range Filter [DW] (2018-10-30/2020-02-17/2020-11-01): Average-Change range `2.618*EMA14(|Δprice|)` smoothed by EMA27, Type-1 dead-zone ratchet filter line, held `fdir` state with author-documented `1` bullish / `-1` bearish external output, bands/bars/colors display-only. No original backtest result is adopted.

### Independently reproduced

**None for strategy events, profits or outcomes.** No TradingView parity run, candidate-specific Hummingbot run, Qlib backtest, event-level parity, actual fills, installed package hash, OOS, Survivor or HB Certified claim. Only the **existing pinned source-code engine/data/executor/fee paths** were directly inspected via immutable raw files at the pinned commit. Alpha PR #414 is prior correspondence evidence, not a claim of re-execution this cycle.

### Negative evidence

The source is an indicator study, so the order mapping (flip-BUY, breakdown-exit, long-flat, size, fees, t+1 fills, t=60 warmup) is **researcher-authored**, not author主張. The demo chart symbol/timeframe, Type 2 stepping, Wicks source, alternate scales and change-averaging are **explicitly not adopted**. Idealized close fills and assumed fees do not prove exchange execution. No realistic live fills or funding are asserted.

**Six-gate proposal, pending independent Hermes Auditor:**
1. Determinism: closed-form EMA seeds, AC/range/filter/fdir recursions, strict-inequality attribution, t=60 warmup.
2. Direction: Binance BTC-USDT spot LONG/FLAT; no short leg exists in source or derivative.
3. Entry/exit/risk: fdir `+1`-flip entry, `-1` full exit as sole disclosed risk leg, disclosed absence of any bracket.
4. State: fixed 0.001 BTC, one pending order/position, cash and fees, no DCA/concurrency, fresh flip after exit, abort on ambiguous fills.
5. Pinned model: directly inspected actual 1d feed, controller/action, MARKET close fill, POSITION_HOLD and fee paths; no unsupported intrabar/funding assumption.
6. Causality: 60 completed-bar warmup, t completed signal -> t+1 completed-close economic fill, no future bars, opening timestamp never misrepresented as close availability.

**Dedup snapshot:** at `main=4853ba14c096d16cddc95026237698866f81afee`, README static pool count and root Markdown strategy count were both **384** (excluding two READMEs). Repo-wide `grep -ril` over root `*.md` returned zero for `lut7sBgG`, `DonovanWall`, `rng_filt`, `Average Change`, `Movement Source`, `fdir`; `2.618` matched only `qqe-fast-slow-cross-two-sided-btcusdt-1d-2026-10-10.md` (a QQE Fast parameter, different mechanism); `Range Filter` prose matched only two unrelated cards (a mean-reversion card title fragment and a crawler-context mention). All ten open `research/*` PR titles were checked for source identity with no match. Nearest pool neighbors (`SuperTrend` flip, PMax-style ATR bands, Chandelier exits) are ATR/true-range bands with price-cross flips; this candidate uses a double-EMA Average-Change dead-zone self-stepping line whose own step direction is the signal, with no high/low, no true range and no RSI. Existing 384 strategies were **not** exhaustively re-audited for PASS frontmatter; count equality is not represented as a full admission census.

## Falsification plan

With separate authorization, materialize only a minimal candidate-specific controller, validate the strict t/t+1 clock and actual close inputs, EMA seed/first-valid-bar behavior, equality cases (`close-r==filt` holds, `filt==filt[1]` holds fdir, initial `0.0` never trades), non-finite-range hold/abort, post-exit re-entry, fail-closed invalid fills and fee-net position accounting. Before large-scale Qlib screening on a newly unverified execution path, obtain representative Hummingbot/Qlib event-level parity for signals, fills, fees and states. Separately assess fee-net IS/OOS performance; no such test is run by this Scout.

## Crypto portability

BTC-USDT spot 1d is researcher-selected, not an author-validated outcome or admission whitelist. Any futures, 3x/5x, DCA BO/SO 6/6/6, other coin or execution model is downstream optional research requiring a separately specified derivative and verified execution/cost/funding path. No implied transfer of results.

## Limitations

No TradingView parity run; source-native equivalence unverified. Derived order mapping, next-close fill, fixed quantity and hypothetical fees materially differ from the source study, which defines no orders. Idealized close fills and assumed fees do not prove exchange execution. No installed package rehash, strategy backtest, Qlib parity, profitability or live authorization. Registry-frozen inputs only; any input change is a new derivative.

## Implementation status

`not-implemented`: research specification only. No controller, Qlib recipe, trading deployment, backtest, container, n8n or cron changes.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is **Scout-proposed**, not self-approved. Independent Hermes Auditor GitHub Webhook Review owns source-fact remediation, exact-head PASS merge or NOT_LOSSLESS close. The existing signed webhook receiver alone owns README bookkeeping after an accepted merge. Scout does not approve, merge, close or write main.

## Related Wiki records

None created or modified.

## Sources

- https://www.tradingview.com/script/lut7sBgG-Range-Filter-DW/ — DonovanWall, first-party public Pine v4 study source, 2018-10-30/2020-02-17/2020-11-01; source code inspected 2026-10-27.
- https://raw.githubusercontent.com/HCH725/hummingbot/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — immutable pinned engine source (feed constants, order executor simulator, backtesting data provider), inspected through immutable raw files 2026-10-27.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — earlier package/source correspondence evidence; not re-run here.
