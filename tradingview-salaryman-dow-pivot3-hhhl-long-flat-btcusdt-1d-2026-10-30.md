---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Salaryman_G Dow Theory confirmed-pivot HH/HL regime BTC spot 1d long-flat — independent derivative"
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
  - https://www.tradingview.com/script/568IR12F/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Salaryman_G confirmed Dow pivot HH/HL trend — BTC spot daily independent research derivative

## Provenance

- **TradingView primary:** Salaryman_G, *Dow Theory Trend Strategy*, publicly listed open-source strategy, published **2025-03-27**, stable TradingView script ID **568IR12F**: https://www.tradingview.com/script/568IR12F/ . First-party public description read **2026-10-30**. The accessible page did not expose immutable Pine source bytes, a revision number, the default `pivotLookback` value, or native fill/fee settings; this record does **not** assert Pine equivalence.
- **Source-native facts verified in the first-party description:** `ta.pivothigh()` and `ta.pivotlow()` with equal left/right `pivotLookback` confirmation windows; the latest two confirmed pivot highs and lows; UP only when both successive highs and lows rise (HH + HL), DOWN only when both fall (LH + LL); otherwise persist the prior regime. A change to UP triggers a long `strategy.entry`, a change to DOWN triggers a short `strategy.entry`; the original Pine strategy reverses exposure. Right-side pivot confirmation is delayed, not available at the pivot's plotted center.
- **Explicit independent derivative, and ONLY this derivative is proposed for HB_READY:** researcher selects strict-unique pivot length `L=R=3`, deterministic tie rules, BTC-USDT Binance spot UTC 1d, LONG/FLAT (source short/reversal disabled), transition-only long entries, level-based DOWN exit for catch-up after fill-bar suppression, 100 completed-bar warmup, fixed 0.001 BTC and 10000 USDT cash, next **completed** daily close historical MARKET fills, modeled 0.1% per-side quote fee, no stop/target/DCA. Strict pivot ties, default pivot length, exit catch-up, market, size, fee, warmup and execution time are **researcher-designed**, not source-native. These alter possible trade events and risk. No original Pine performance or source-native event equivalence is claimed.
- **Immutable research identity:** `TV:568IR12F|Salaryman_G|published-2025-03-27|derived-strict-pivot3-hhhl-long-flat-v1-20261030|BinanceSpot:BTC-USDT:UTC1d|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|warmup100|no-DCA-stop`.
- **Dedup, 2026-10-30:** `main` SHA `73f94cba24b5b325bff13015c1e777e232531ad6`, 457 root strategy records / README 457; GitHub code search `568IR12F`, `pivotLookback`, `dow theory trendDirection` and PR search for the source ID, author and title found no same-source candidate. All 11 open research PRs inspected for source identity. Existing Kaufman pivot breakout enters on price crossing a confirmed pivot **level**; the FMZ fractal support/resistance strategy trades level breakouts. This derivative instead uses **two consecutive confirmed highs AND two confirmed lows** to latch a regime, with an UP transition entry and DOWN-state exit. Not a paraphrase or mere parameter variant of those breakout mechanisms.

## Economic mechanism

### Source-reported
The author interprets consecutive higher pivot highs and lows as an established uptrend, and consecutive lower pivot highs and lows as a downtrend; persistence through ambiguous structures is intended to reduce false regime flips. This is a qualitative hypothesis, not independently validated profitability.

### Research interpretation
Test whether a fully confirmed rising-pivot structure predicts continued daily BTC price appreciation until the confirmed structure becomes falling. The derivative deliberately excludes the original short leg and original Pine reversal/order defaults; its results would not measure the source strategy's complete two-sided behavior.

## Signal

- Input: strictly chronological, **completed** UTC Binance Spot BTC-USDT `1d` candles indexed `t=0,1,...`; use raw `high[t]`, `low[t]`, `close[t]`. Reject missing/duplicate/gapped daily bars, nonfinite/nonpositive prices, or any candle with `high < max(open,close)`, `low > min(open,close)`, `low > high`, or negative/nonfinite volume. Reject/abort invalid research segment; never synthesize prices, forward-fill signals, or silently skip a broken bar.
- **Researcher-defined strict pivot:** at the **close** of bar `t>=6`, center `k=t-3` becomes a confirmed HIGH pivot iff `high[k] > high[j]` for every other `j` in `[k-3,k+3]`. Confirm a LOW pivot iff `low[k] < low[j]` for all other such `j`. Equality with ANY neighboring bar disqualifies that pivot (tie handling deliberately differs from any unverified Pine implementation). No confirmation is backdated to `k`; it becomes usable only at `t`. A center can qualify as both high and low; apply both updates before regime evaluation.
- Maintain the **two most recently confirmed** pivot highs `Hprev,Hnew` and lows `Lprev,Lnew` by confirmation time, without interpolation or reordering. If fewer than two of either exist, `trend[t]=NEUTRAL(0)` (until enough evidence), unless a prior non-neutral trend already exists. Once four pivots exist: if `Hnew>Hprev && Lnew>Lprev`, `trend[t]=UP(+1)`; else if `Hnew<Hprev && Lnew<Lprev`, `trend[t]=DOWN(-1)`; else `trend[t]=trend[t-1]`. Equality, mixed HH/LL or LH/HL, or no new pivot leaves trend unchanged. Initial trend is 0. No future-bar `lookahead` or plotted-center signal.
- **Entry:** at a permitted decision close `t>=100`, when FLAT, no pending order, `trend[t]=UP` and `trend[t-1]!=UP`, queue exactly one BUY for the next bar. No entry from a pre-warmup UP state without a new transition.
- **Exit:** at a permitted decision close `t>=100`, when LONG, no pending order, and `trend[t]=DOWN`, queue one full-position SELL. The DOWN **level** (rather than only the transition) is a disclosed researcher-designed catch-up: a DOWN transition occurring on a fill bar is observed at the next eligible decision, not silently lost. A neutral regime never exits. EXIT has priority over ENTRY if an impossible/malformed state would co-trigger; invalid state aborts.
- **Warmup:** bars `0..99` update pivot history and trend but cannot queue or fill orders. First eligible decision is the completed close of `t=100`. Confirmation itself needs 7 bars; 100 bars is a deliberately conservative fixed research warmup, not an original Pine default.
- **State:** FLAT, BUY_PENDING, LONG, SELL_PENDING; exactly one position and one pending order at most. A queued action on `t` attempts one historical fill at `t+1` completed close; process that fill first and do **not** generate a new order on the fill bar `t+1`, though its pivot/trend state still updates. Earliest next decision is `t+2`. On BUY fill enter LONG; on SELL fill become FLAT. No re-entry unless a fresh UP transition occurs after flat, no repeated entry while LONG, no pyramiding, simultaneous positions, short, hedge, borrowing, DCA, safety orders, partial exits, dynamic sizing, independent cooldown or forced end-of-sample liquidation. An unfilled end-of-sample pending order remains unfilled and is reported as such.
- **Risk and disabled behavior:** no protective stop-loss, take-profit, trailing stop, time exit, automatic liquidation, session filter or discretionary override. DOWN state is the only signal exit. Loss and indefinite holding are possible; no hidden executor SL/TP defaults.

## Required data

Single Binance Spot `BTC-USDT` UTC daily OHLCV candle series, validated for completeness and chronological availability. Only completed high/low pivots and price for the fixed-fee cash ledger are decision-critical. No funding, order book, open interest, cross-market synchronization, alternate timeframe, repainting ZigZag, or private feed is required. Historical MARKET fill prices must be actual validated next-bar close data, never the backtesting provider's missing-price fallback.

## Execution assumptions — demonstrated bounded pinned-engine research path

- **Pinned engine:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. GitHub Connector directly read `hummingbot/VERSION`, Binance spot candles `constants.py` and `binance_spot_candles.py`, `strategy_v2/backtesting/backtesting_engine_base.py`, `backtesting_data_provider.py`, `executors_simulator/order_executor_simulator.py` and `executors/order_executor/data_types.py` this cycle. Prior independently reviewed representative primitive is Alpha PR #414; no wheel rehash or candidate-specific backtest was run.
- **Real data path:** `BinanceSpotCandles.INTERVALS` includes `1d`; Binance REST `/api/v3/klines` parser takes the actual Kline opening timestamp and O/H/L/C/V. A candle's stored `timestamp=T[t]` is **open time**; its `high/low/close` are decision-available only after `T[t]+86400 seconds` for a complete UTC day. The candidate's own controller must reject incomplete last bars, gaps and invalid prices **before** engine preparation/dropna; no missing-price `Decimal("1")` fallback.
- **Controller/executor path:** `BacktestingEngineBase.simulate_execution` prepares rows and advances `update_state(row)` then controller `determine_executor_actions()`, dispatching `CreateExecutorAction` via `simulate_executor`. The future dedicated controller (NOT yet implemented) will implement the explicit pivot/regime state and one-bar pending action. `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1,position_action=OPEN/CLOSE)`. SELL size equals the recorded base inventory. `OrderExecutorSimulator.simulate` for MARKET fills on the first supplied row at its actual `close`, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`; `BacktestPositionHold` nets buy/sell and tracks gross realized PnL separately from fees. No limit/maker/intrabar fill or unverified cross-asset path is required.
- **Exact causal fill mapping:** decide at `T[t]+86400` using data through completed bar `t`; dispatch the stored order only on the `t+1` row, and model a retrospective full fill at actual `C[t+1]`, effective `T[t+1]+86400`. The row's opening timestamp is not misrepresented as fill availability. Do not use `C[t+1]` or pivots confirmed on `t+1` to decide at `t`; the `t+1` pivot state may update but does not create another action on the fill bar. This is an **idealized historical next-completed-close** convention, not original Pine next-open timing or a live close-order guarantee.
- **Exact modeled cash/inventory ledger:** initial cash `10000 USDT`, BTC inventory 0, fixed `Q=Decimal("0.001")`, hypothetical quote fee rate `f=Decimal("0.001")` per executed side. On BUY at actual close `P`, require `cash >= Q*P*(1+f)`; otherwise consume BUY intent without a fill, stay FLAT, require a new UP transition. Successful BUY: `cash -= Q*P*(1+f)`, `base += Q`. SELL requires `base==Q`; successful SELL: `cash += Q*P*(1-f)`, `base=0`. Invalid inventory or nonfinite/absent price aborts, not a fabricated fill. Round-trip fee-net quote PnL `Q*(Pexit-Pentry)-f*Q*(Pentry+Pexit)`. Controller ledger uses `Decimal` on original validated close strings, not native gross PnL as fee-net equity. On each full-fill-only modeled action pass `trade_cost=0.001` to pinned simulator; do not double-subtract fees.
- **Research economics boundary:** this is a **fixed idealized full-fill** historical Spot model. Research fee 0.1% per side is a declared hypothetical input, NOT verified Binance fee tier. Zero **modeled** spread/slippage is an explicit idealization, not an observed zero. Exchange-specific lot/tick rounding, min-notional, historical order acceptance, latency, partial fills, liquidity and live fee tier are not verified or claimed compatible. Do not call `quantize_order_amount` or assert real exchange-valid orders from this model. Spot has no perpetual funding/margin/liquidation leg; do not fabricate futures funding observations. PASS only concerns this precisely bounded historical model; actual trading would require separate validation and authorization.
- **Fail closed:** reject invalid candles, insufficient warmup, missing next close, price fallbacks and contradictory pending/position states. No paper/testnet/live order path, trading, Qlib run or Hummingbot run is authorized by this record.

## Evidence

### Source-reported
First-party TradingView description, Salaryman_G, 2025-03-27, stable ID 568IR12F: symmetric confirmed pivot high/low detection, two successive HH+HL or LH+LL pairs, persistence in mixed regimes, and two-sided regime-change entries. It provides no independently verified performance and no accessible immutable Pine bytes or default `pivotLookback`/execution economics.

### Independently reproduced
Not independently reproduced. No Pine trade sequence, candidate-specific Hummingbot execution, Qlib parity, profitability, OOS or Survivor status was reproduced. The pinned Hummingbot **source capability** paths were directly inspected; existing independently accepted primitive evidence #414 is referenced without claiming the derivative controller exists.

### Negative evidence
TradingView Pine bytes and native default pivot length/order timing were not obtained. This derivative's strict pivot tie handling, 3/3 confirmation, spot-only direction, DOWN-level catch-up exit, sizing, fill clock, fee, warmup and disabled behaviors are explicitly researcher choices. Main and open PR dedup found no same TradingView script ID or materially identical combined HH+HL / LH+LL regime strategy. Real exchange precision, fees, fill quality and partial executions are unverified.

## Six-gate assessment — Scout proposal, not independent audit

1. **Determinism:** strict 3-left/3-right pivot with equality veto, 2-high/2-low regime state, simultaneous update, persistence, no fitted parameters, 100-bar warmup.
2. **Direction:** BTC-USDT Binance Spot LONG/FLAT; short/reversal/borrow/leverage disabled.
3. **Entry/exit/risk:** fresh UP-transition entry, DOWN-level full exit, all protective/alternative exits explicitly disabled.
4. **Position:** one fixed 0.001 BTC position, 10000 USDT ledger, one pending, fill-bar no-action, no DCA/pyramiding/cooldown, new transition needed for re-entry.
5. **Pinned engine:** actual 1d Binance spot candles, pinned controller/action/MARKET close-fill/POSITION_HOLD and quote-fee model verified from source; bounded hypothetical full-fill research accounting only, not exchange-valid orders.
6. **Causality:** right-side pivots confirmed only at `t=k+3`, no backdating, completed-bar warmup, open timestamps corrected to close availability, `t` signal → `t+1` completed-close modeled fill, no future-data decision leakage.

`hb_ready_status: PASS` is a **Scout research admission proposal** for this independent derivative only; independent Hermes Auditor decides exact-head PASS, source-verifiable remediation or NOT_LOSSLESS. It is not proof of source-native equivalence, profitability, Qlib parity, implementation, HB Certified survivor or live readiness.

## Falsification plan

Not executed: adversarial tests for tied pivot highs/lows, simultaneous high+low pivot, initial missing pivots, mixed HH/LL, regime persistence, pivot confirmation delay, warmup boundary, DOWN transition on BUY fill bar and catch-up exit, price gaps, zero/invalid prices, insufficient cash, fees, missing next close and sample-end pending order. A later representative Qlib↔Hummingbot event-level primitive parity check is required before mass screening if this path is not already covered by validated evidence; candidate-specific performance research is separate.

## Crypto portability

BTC-USDT spot 1d is an independent study selection, not an HB_READY whitelist. Applying this structure to other coins/timeframes, house BO/SO 6/6/6, futures leverage, or new fill conventions requires separately declared research assumptions and capability checks; it is not silently the original TradingView strategy.

## Limitations

No original Pine source bytes, version number, default pivot length or source order-processing details were retrieved. The derived strict 3/3 pivots and close-fill/catch-up semantics can materially differ from TradingView's script. No protective stop or forced liquidation; long drawdowns and indefinite holding are possible. The hypothetical 0.1% fee and idealized full-fill/zero-modeled-slippage Spot ledger are not exchange-realistic order acceptance or canonical realized costs. No controller implementation, candidate-specific event parity, backtest, reproduced returns or deployment exists.

## Implementation status

`not-implemented`: no strategy-specific controller, Qlib recipe or executable deployment. HB_READY research admission is not implementation approval.

## Adoption boundary

`research-only`, `not-approved`; no Paper/Testnet/Live, capital authorization or Qlib/Hummingbot run. Only independent Hermes Auditor GitHub Webhook Review may remediate/review/merge or close; only the existing signed GitHub webhook receiver performs post-merge README count bookkeeping.

## Related Wiki records

None required; no separate registry or research artifact was created.

## Sources

- TradingView primary: https://www.tradingview.com/script/568IR12F/ — Salaryman_G, *Dow Theory Trend Strategy*, published 2025-03-27; public description inspected 2026-10-30.
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed execution primitive: https://github.com/HCH725/alpha-strategy-research/pull/414
