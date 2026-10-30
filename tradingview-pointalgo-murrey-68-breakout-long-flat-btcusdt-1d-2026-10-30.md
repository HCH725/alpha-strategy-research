---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "pointalgo Murrey Math 6/8-breakout 4/8-exit BTC spot 1d long-flat — independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-30
sources:
  - https://www.tradingview.com/script/zYJ7XXTa-Murrey-Math-pointalgo/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# pointalgo Murrey Math octave-grid breakout — BTC spot daily independent research derivative

## Provenance

- **TradingView primary:** pointalgo, *Murrey Math [pointalgo]*, publicly listed open-source indicator, stable TradingView script ID **zYJ7XXTa**: https://www.tradingview.com/script/zYJ7XXTa-Murrey-Math-pointalgo/ . First-party landing page fetched live **2026-10-30** (HTTP 200, 307653 bytes) and carries the `OPEN-SOURCE SCRIPT` badge. The accessible page did not expose immutable Pine source bytes, a revision number, the default `Geometric Frame Size` value, or native strategy fill/fee settings; this record does **not** assert Pine equivalence.
- **Source-native facts verified in the first-party description:** highest high and lowest low over a user-defined `Geometric Frame Size`; that range divided into 8 equal price intervals (`0/8` to `8/8`); level semantics `0/8 & 8/8` major support & resistance (frame extremes), `4/8` central equilibrium/median, `2/8 & 6/8` pivot zones, `1/8 & 7/8` weak stall levels, `3/8 & 5/8` trading range levels; breakout signals on **closes**: bullish when price closes above `4/8`, `6/8`, or `8/8`, bearish when price closes below `4/8`, `2/8`, or `0/8`, with arrows/labels on the breaking bar.
- **Explicit independent derivative, and ONLY this derivative is proposed for HB_READY:** researcher fixes Geometric Frame Size to trailing **64** completed daily bars (the page exposes no default number; 64 is a disclosed researcher choice, corroborated only as reasonable by an independent Murrey script default, not copied as a source fact), BTC-USDT Binance spot UTC 1d, LONG/FLAT (the source is an indicator with both bullish and bearish breakout marks; no source short/reversal leg is adopted), entry on a fresh close-above-`6/8` cross, exit on a close-below-`4/8` level, 100 completed-bar warmup, fixed 0.001 BTC and 10000 USDT cash, next **completed** daily close historical MARKET fills, modeled 0.1% per-side quote fee, no stop/target/DCA. Frame length, market, size, fee, warmup, fill timing and tie rules are **researcher-designed**, not source-native. These alter possible trade events and risk. No original indicator performance or source-native event equivalence is claimed. Murrey's square-number octave anchoring used by other scripts is intentionally not adopted; this derivative uses only the trailing-range octave method described on the cited page.
- **Immutable research identity:** `TV:zYJ7XXTa|pointalgo|derived-murrey68-breakout-48exit-long-flat-v1-20261030|BinanceSpot:BTC-USDT:UTC1d|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|frame64|warmup100|no-DCA-stop`.
- **Dedup, 2026-10-30:** `main` SHA `c9453ed0e44939265d8cd5635dfa395f40a2c808`, 458 root strategy records / README 458; working-tree searches for `murrey`, `murray math`, `octave`, `8/8`, `zYJ7XXTa` and GitHub PR search for the source ID, author and title found no same-source candidate. All 11 open research PRs inspected for source identity. Closest pool neighbors use different signal objects: Camarilla R1/S1 rail-cross derives levels from the prior day HLC pivot formula (not a trailing-64-bar octave grid); the Fibonacci 0.618 record reclaims a swing-anchored retracement (not a fixed 1/8 grid cross); the Donchian cohort trades edge-channel extremes with no interior `6/8`/`4/8` level pair; the Kaufman pivot breakout crosses a confirmed-pivot price level (not an octave fraction). This derivative's trailing-octave `6/8`-cross entry with `4/8`-level exit is not a paraphrase or mere parameter variant of those mechanisms.

## Economic mechanism

### Source-reported
Price tends to respect, stall at, and break through the 1/8th octave grid derived from the recent range; closes beyond pivot levels (`2/8`, `6/8`) and the `4/8` equilibrium mark momentum regime change, while `3/8`–`5/8` contains range trading. This is a qualitative hypothesis, not independently validated profitability.

### Research interpretation
Test whether a daily close breaking above the upper pivot line of a trailing 64-day octave grid predicts continued BTC price appreciation until price closes back below the grid midpoint. The derivative deliberately adopts only the `6/8`-up / `4/8`-down pair of the source's wider breakout family; its results would not measure the full indicator or any other level pair.

## Signal

- Input: strictly chronological, **completed** UTC Binance Spot BTC-USDT `1d` candles indexed `t=0,1,...`; use raw `high[t]`, `low[t]`, `close[t]`. Reject missing/duplicate/gapped daily bars, nonfinite/nonpositive prices, or any candle with `high < max(open,close)`, `low > min(open,close)`, `low > high`, or negative/nonfinite volume. Reject/abort invalid research segment; never synthesize prices, forward-fill signals, or silently skip a broken bar.
- **Researcher-defined trailing octave grid:** at the **close** of bar `t>=63`, `HH[t]=max(high[t-63..t])`, `LL[t]=min(low[t-63..t])`. Require finite `HH[t]`, `LL[t]` with `HH[t] > LL[t]` strictly; a zero-range frame (`HH==LL`) or any nonfinite frame input invalidates the segment (fail closed, never divide by zero). `octave[t]=(HH[t]-LL[t])/8`; `L6[t]=LL[t]+6*octave[t]`; `L4[t]=LL[t]+4*octave[t]`. The grid is recomputed every bar from completed bars only and is time-varying; no Gann square-number anchoring, no backdating, no repainting of confirmed levels.
- **Entry:** at a permitted decision close `t>=100`, when FLAT, no pending order, `close[t] > L6[t]` and `close[t-1] <= L6[t-1]` (fresh close-above-`6/8` cross against contemporaneous same-bar levels), queue exactly one BUY for the next bar. Equality never crosses. No entry from a pre-warmup above-level state without a new cross.
- **Exit:** at a permitted decision close `t>=100`, when LONG, no pending order, and `close[t] < L4[t]` (close-below-`4/8` level against the contemporaneous frame), queue one full-position SELL. The `4/8` **level** (rather than only the cross) is a disclosed researcher-designed catch-up: a breakdown occurring on a fill bar is observed at the next eligible decision, not silently lost. A close exactly on a level never triggers. EXIT has priority over ENTRY if an impossible/malformed state would co-trigger; invalid state aborts. One bar gapping across several levels still produces at most one queued action because entry requires FLAT and exit requires LONG.
- **Warmup:** bars `0..99` update frame history and levels but cannot queue or fill orders. First eligible decision is the completed close of `t=100`. The frame itself needs 64 bars; 100 bars is a deliberately conservative fixed research warmup, not an original indicator default.
- **State:** FLAT, BUY_PENDING, LONG, SELL_PENDING; exactly one position and one pending order at most. A queued action on `t` attempts one historical fill at `t+1` completed close; process that fill first and do **not** generate a new order on the fill bar `t+1`, though its frame/level state still updates. Earliest next decision is `t+2`. On BUY fill enter LONG; on SELL fill become FLAT. No re-entry unless a fresh `6/8` cross occurs after flat, no repeated entry while LONG, no pyramiding, simultaneous positions, short, hedge, borrowing, DCA, safety orders, partial exits, dynamic sizing, independent cooldown or forced end-of-sample liquidation. An unfilled end-of-sample pending order remains unfilled and is reported as such.
- **Risk and disabled behavior:** no protective stop-loss, take-profit, trailing stop, time exit, automatic liquidation, session filter or discretionary override. The `4/8` close-below level is the only signal exit. Loss and indefinite holding are possible; no hidden executor SL/TP defaults.

## Required data

Single Binance Spot `BTC-USDT` UTC daily OHLCV candle series, validated for completeness and chronological availability. Frame extremes and octave levels derive from validated high/low/close only. Only completed-bar levels and price for the fixed-fee cash ledger are decision-critical. No funding, order book, open interest, cross-market synchronization, alternate timeframe, or private feed is required. Historical MARKET fill prices must be actual validated next-bar close data, never the backtesting provider's missing-price fallback.

## Execution assumptions — demonstrated bounded pinned-engine research path

- **Pinned engine:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The pinned `hummingbot/VERSION`, Binance spot candles `constants.py` and `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `backtesting_data_provider.py`, `executors_simulator/order_executor_simulator.py` and `executors/order_executor/data_types.py` were directly read at this pinned commit this cycle. Prior independently reviewed representative primitive is Alpha PR #414; no wheel rehash or candidate-specific backtest was run.
- **Real data path:** `BinanceSpotCandles.INTERVALS` includes `1d`; Binance REST `/api/v3/klines` parser takes the actual Kline opening timestamp and O/H/L/C/V. A candle's stored `timestamp=T[t]` is **open time**; its `high/low/close` are decision-available only after `T[t]+86400 seconds` for a complete UTC day. The candidate's own controller must reject incomplete last bars, gaps and invalid prices **before** engine preparation/dropna; no missing-price `Decimal("1")` fallback.
- **Controller/executor path:** `BacktestingEngineBase.simulate_execution` prepares rows and advances `update_state(row)` then controller `determine_executor_actions()`, dispatching `CreateExecutorAction` via `simulate_executor`. The future dedicated controller (NOT yet implemented) will implement the explicit 64-bar octave state and one-bar pending action. `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1,position_action=OPEN/CLOSE)`. SELL size equals the recorded base inventory. `OrderExecutorSimulator.simulate` for MARKET fills on the first supplied row at its actual `close`, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`; `BacktestPositionHold` nets buy/sell and tracks gross realized PnL separately from fees. No limit/maker/intrabar fill or unverified cross-asset path is required.
- **Exact causal fill mapping:** decide at `T[t]+86400` using data through completed bar `t`; dispatch the stored order only on the `t+1` row, and model a retrospective full fill at actual `C[t+1]`, effective `T[t+1]+86400`. The row's opening timestamp is not misrepresented as fill availability. Do not use `C[t+1]` or levels recomputed on `t+1` to decide at `t`; the `t+1` frame state may update but does not create another action on the fill bar. This is an **idealized historical next-completed-close** convention, not live close-order timing or a live close-order guarantee. No claim equates any close with any neighboring open.
- **Exact modeled cash/inventory ledger:** initial cash `10000 USDT`, BTC inventory 0, fixed `Q=Decimal("0.001")`, hypothetical quote fee rate `f=Decimal("0.001")` per executed side. On BUY at actual close `P`, require `cash >= Q*P*(1+f)`; otherwise consume BUY intent without a fill, stay FLAT, require a new `6/8` cross. Successful BUY: `cash -= Q*P*(1+f)`, `base += Q`. SELL requires `base==Q`; successful SELL: `cash += Q*P*(1-f)`, `base=0`. Invalid inventory or nonfinite/absent price aborts, not a fabricated fill. Round-trip fee-net quote PnL `Q*(Pexit-Pentry)-f*Q*(Pentry+Pexit)`. Controller ledger uses `Decimal` on original validated close strings, not native gross PnL as fee-net equity. On each full-fill-only modeled action pass `trade_cost=0.001` to pinned simulator; do not double-subtract fees.
- **Research economics boundary:** this is a **fixed idealized full-fill** historical Spot model. Research fee 0.1% per side is a declared hypothetical input, NOT verified Binance fee tier. Zero **modeled** spread/slippage is an explicit idealization, not an observed zero. Exchange-specific lot/tick rounding, min-notional, historical order acceptance, latency, partial fills, liquidity and live fee tier are not verified or claimed compatible. Do not call `quantize_order_amount` or assert real exchange-valid orders from this model. Spot has no perpetual funding/margin/liquidation leg; do not fabricate futures funding observations. PASS only concerns this precisely bounded historical model; actual trading would require separate validation and authorization.
- **Fail closed:** reject invalid candles, zero-range frames, insufficient warmup, missing next close, price fallbacks and contradictory pending/position states. No paper/testnet/live order path, trading, Qlib run or Hummingbot run is authorized by this record.

## Evidence

### Source-reported
First-party TradingView description, pointalgo, stable ID zYJ7XXTa: HH/LL over user-defined Geometric Frame Size, 8 equal 0/8–8/8 intervals, stated level semantics (extremes, 4/8 equilibrium, 2/8 & 6/8 pivots, weak stalls, trading range), and close-based breakout marks (bullish above 4/8, 6/8, 8/8; bearish below 4/8, 2/8, 0/8). It provides no independently verified performance and no accessible immutable Pine bytes, default frame length, or execution economics.

### Independently reproduced
Not independently reproduced. No Pine trade sequence, candidate-specific Hummingbot execution, Qlib parity, profitability, OOS or Survivor status was reproduced. The pinned Hummingbot **source capability** paths were directly inspected at the pinned commit; existing independently accepted primitive evidence #414 is referenced without claiming the derivative controller exists.

### Negative evidence
TradingView Pine bytes, native default frame length and native order timing were not obtained. This derivative's fixed 64-bar frame, spot-only direction, `6/8`-cross entry, `4/8`-level catch-up exit, sizing, fill clock, fee, warmup and disabled behaviors are explicitly researcher choices. Main and open PR dedup found no same TradingView script ID or materially identical trailing-octave grid strategy. Real exchange precision, fees, fill quality and partial executions are unverified.

## Six-gate assessment — Scout proposal, not independent audit

1. **Determinism:** trailing-64 HH/LL frame, strict `HH>LL`, 1/8 octave grid, strict-inequality `6/8` cross entry and `4/8` level exit, equality veto, 100-bar warmup, no fitted parameters.
2. **Direction:** BTC-USDT Binance Spot LONG/FLAT; bearish-breakout short leg disabled, no borrow/leverage.
3. **Entry/exit/risk:** fresh `6/8`-cross entry, `4/8`-level full exit with fill-bar catch-up, all protective/alternative exits explicitly disabled.
4. **Position:** one fixed 0.001 BTC position, 10000 USDT ledger, one pending, fill-bar no-action, no DCA/pyramiding/cooldown, new cross needed for re-entry.
5. **Pinned engine:** actual 1d Binance spot candles, pinned controller/action/MARKET close-fill/POSITION_HOLD and quote-fee model verified from source this cycle; bounded hypothetical full-fill research accounting only, not exchange-valid orders.
6. **Causality:** frame and levels use completed bars only (`t-63..t` available at `T[t]+86400`), warmup precedes decisions, open timestamps corrected to close availability, `t` signal → `t+1` completed-close modeled fill, no future-data decision leakage, no close/open equality claim.

`hb_ready_status: PASS` is a **Scout research admission proposal** for this independent derivative only; independent Hermes Auditor decides exact-head PASS, source-verifiable remediation or NOT_LOSSLESS. It is not proof of source-native equivalence, profitability, Qlib parity, implementation, HB Certified survivor or live readiness.

## Falsification plan

Not executed: adversarial tests for zero-range frames, ties on `L6`/`L4`, single-bar gaps across multiple octave levels, frame-boundary warmup, breakdown on BUY fill bar and `4/8` catch-up exit, insufficient cash, fees, missing next close and sample-end pending order. A later representative Qlib↔Hummingbot event-level primitive parity check is required before mass screening if this path is not already covered by validated evidence; candidate-specific performance research is separate.

## Crypto portability

BTC-USDT spot 1d is an independent study selection, not an HB_READY whitelist. Applying this structure to other coins/timeframes, other frame lengths or level pairs, house BO/SO 6/6/6, futures leverage, or new fill conventions requires separately declared research assumptions and capability checks; it is not silently the original TradingView indicator.

## Limitations

No original Pine source bytes, revision number, default frame length or source order-processing details were retrieved. The fixed 64-bar frame and close-fill/catch-up semantics can materially differ from the TradingView indicator. No protective stop or forced liquidation; long drawdowns and indefinite holding are possible. The hypothetical 0.1% fee and idealized full-fill/zero-modeled-slippage Spot ledger are not exchange-realistic order acceptance or canonical realized costs. No controller implementation, candidate-specific event parity, backtest, reproduced returns or deployment exists.

## Implementation status

`not-implemented`: no strategy-specific controller, Qlib recipe or executable deployment. HB_READY research admission is not implementation approval.

## Adoption boundary

`research-only`, `not-approved`; no Paper/Testnet/Live, capital authorization or Qlib/Hummingbot run. Only independent Hermes Auditor GitHub Webhook Review may remediate/review/merge or close; only the existing signed GitHub webhook receiver performs post-merge README count bookkeeping.

## Related Wiki records

None required; no separate registry or research artifact was created.

## Sources

- TradingView primary: https://www.tradingview.com/script/zYJ7XXTa-Murrey-Math-pointalgo/ — pointalgo, *Murrey Math [pointalgo]*, open-source indicator; public description inspected 2026-10-30.
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed execution primitive: https://github.com/HCH725/alpha-strategy-research/pull/414
