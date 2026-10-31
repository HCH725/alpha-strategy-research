---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FMZ Super-Scalper dual-RSI ATR-band dip two-sided on BTCUSDT 5m bars
created: 2026-10-31
updated: 2026-10-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-24
sources:
  - https://www.fmz.com/strategy/365373
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Super-Scalper-5-Min-15-Min.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Super-Scalper dual-RSI ATR-band dip — independent BTC-USDT 5m two-sided derivative

## Provenance

**Canonical page (fetched live over HTTPS this cycle, HTTP 200, 713,921 bytes, no login):** FMZ public strategy **365373**, *Super Scalper - 5 Min 15 Min*, author nickname **ChaoZhang**, https://www.fmz.com/strategy/365373 . The served page carries the strategy prose (RSI plus ATR Bands, 5- and 15-minute frames, 1:2R backtest note, EMA-65/21 golden-cross trend confirmation), the `/*backtest*/` stanza (`start: 2022-04-23 00:00:00`, `end: 2022-05-22 23:59:00`, `period: 5m`, `basePeriod: 1m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]` — quoted verbatim, never normalized), and the executable Pine identifiers verified by token census this cycle (`RSILong` ×2, `strategy.entry` ×2, `atr_slen` ×3, `GoldenLong` ×2, `Futures_Binance` ×2, `BTC_USDT` ×2).

**Immutable mirror actually executed against (primary code source):** repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository HEAD via `git ls-remote` this cycle — the same head pin as the merged PowerZone, 1-3-1, Dual-Thrust and MA-ribbon-MACD admissions), exact file path `Super-Scalper-5-Min-15-Min.md` (3770 bytes, 128 lines; GitHub contents-API blob SHA `0110dafba2407efbdad8c854587322b2fdf63cc8`, size 3770 — byte-identical to the fetched file: local `git hash-object` reproduces `0110dafb…f63cc8`, SHA-256 `a7c41e38d8c5e79a0f30627de8179f3e688a2a507b788386d16c9189df5f0a24`). The mirror prints `> Name` = the strategy title, `> Author` = `ChaoZhang`, `> Detail` = the canonical page URL, `> Last Modified` = `2022-05-24 16:20:58` (date part adopted as `source_as_of`), the strategy description, the arguments table (ATR Period 14, ATR Multi 1, smoothing WMA, Fast EMA 21, Slow EMA 65, Fast RSI 25, Slow RSI 100), and the complete `//@version=5` Pine block (mirror lines 39–120). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Order-affecting lines read verbatim (code governs everywhere it conflicts with prose):** `atrlen = input.int(14, "ATR Period")`; `mult = input.float(1, "ATR Multi", step=0.1)`; `smoothing = input.string(title="ATR Smoothing", defval="WMA", options=["RMA", "SMA", "EMA", "WMA"])`; `atr_slen = ma_function(ta.tr(true), atrlen)` (WMA branch at the pinned default); `upper_band = atr_slen * mult + close`; `lower_band = close - atr_slen * mult`; `shortSMA = ta.ema(close, 21)`; `longSMA = ta.ema(close, 65)`; `rsi1 = ta.rsi(close, 25)`; `rsi2 = ta.rsi(close, 100)`; `RSILong = rsi1 > rsi2`; `RSIShort = rsi1 < rsi2`; `longCondition = open < lower_band`; `shortCondition = open > upper_band`; entries `if (longCondition)` → `strategy.entry("long", strategy.long, when = RSILong)` and `if (shortCondition)` → `strategy.entry("short", strategy.short, when = RSIShort)`.

**Text census over the pinned file:** 1 `strategy(` (title `Super Scalper - 5 Min 15 Min`, `overlay=true`, no sizing/timing/cost/pyramiding argument ships anywhere); 2 `strategy.entry` (`"long"`/`strategy.long`, `"short"`/`strategy.short`, both `when=`-gated, no `qty=`/`limit=`/`stop=` qualifiers); 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order`; 0 `pyramiding` / 0 `process_orders_on_close` / 0 `commission` / 0 `slippage` / 0 `calc_on`; 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `volume`; 4 `plotshape` (buy/sell/golden labels — render-only); 2 `ta.crossover` (golden-cross pair — plotted only, never read by any order line); 5 `input.int` + 1 `input.float` + 1 `input.string` (all defaults pinned above). Dead/display-only code fenced: the `stopLoss`/`takeProfit` locals assigned inside both `if` blocks are never passed to any order call (no `strategy.exit` exists — reversal is the sole exit path, disclosed); the EMA-21/65 golden-cross pair feeds only `plotshape` labels (no order-gating line reads them); the standalone `atr = ta.atr(atrlen)` feeds only the dead stop/take locals. Display/plot branches cannot change any order condition.

**Prose-vs-code conflicts (code governs, disclosed):** (a) the prose advertises 1:2R testing and stop-loss/take-profit discipline, but the pinned code submits no stop or limit leg of any kind — the risk posture is reversal-only, never presented as bracketed; (b) the prose advertises EMA-65/21 golden-cross trend confirmation, but the cross pair is plot-only — the only trend gate in any order line is the RSI25-vs-RSI100 comparison, never the EMA cross; (c) the prose names both 5- and 15-minute frames, but the backtest stanza pins `period: 5m` — this derivative pins 5m only, and any 15m execution is a different, unpinned claim.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly six: (1) market/frame pin Binance **BTCUSDT 5m** (the stanza itself backtests `Futures_Binance BTC_USDT` at `period: 5m` — market and decision frame are both source-native; `basePeriod: 1m` is FMZ execution plumbing, not a second signal frame); (2) completed-bar decisions with next-bar-open MARKET fills for entries and reversals (the source ships no execution-timing argument — Pine market-order default timing class; this record claims no source fills, same conversion class as the merged PowerZone and 1-3-1 records); (3) an adopted 120-bar warmup with pre-warmup bars flat by record rule (covers the RSI100 seed with margin); (4) house sizing/capital/costs replacing the sourceless stub (fixed 0.01 BTC, 10,000 USDT cash admission, 0.1%/side researcher fee; Isolated 1×; fees plus modeled funding, no hypothetical zero funding claimed); (5) the Pine-default single-position behavior pinned as an explicit single-unit gate (a signal bar arriving while positioned on the same side is a no-op; an opposite signal closes-and-reverses in one step at the same fill — predeclared researcher rule, never a Pine-manual claim); (6) display/plot/dead-local branches dropped with zero decision function. The WMA-TR14 ATR bands, the RSI25/RSI100 trend gate, the open-penetration triggers, the two-sided stance, and the reversal-only exit posture are source-native and unmodified.

**Immutable derivative identity:** `FMZ:365373|ChaoZhang-v5|dualRSI25-100-ATRband1.0-dip|independent-derived-v1|BinanceFutures:BTC-USDT:5m|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.001|cash10000|lev1x-isolated|reversal-only|warmup120|2026-10-31`. Changing any formula, threshold, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Dip-bought trend-continuation scalper, both directions. The ATR band (`close ± WMA(TR,14)`) sketches the bar's own noise envelope; an open printing outside it marks a micro-displacement. The dual-RSI comparison (`RSI25` vs `RSI100`) votes the slower trend: only dips taken while the fast RSI rides above the slow RSI (uptrend), only rallies faded while it rides below (downtrend). The entry is not the displacement alone and not the RSI stance alone, but their conjunction — a with-trend micro-dip. The source ships no stop, no target, no time exit of any kind; an open position simply waits for the opposite conjunction to reverse it. The prose ships no quantified performance of any kind — only qualitative "works better in 5 and 15 Mins" remarks, adopted here as thesis prose, never as evidence.

### Research interpretation

With-trend dip machine with a volatility-normalized trigger, event-driven, two-sided, effectively always-in-market after warmup. Unlike unconditional fade records (connors-rsi2, lehmann-weekly, three-down-three-up — fades armed by streaks or oscillator extremes with no trend vote), nothing fires against the RSI100 trend: the band penetration is the trigger, the RSI comparison is the permission, and neither leg can act alone. Unlike single-RSI threshold records (rsi-dip, cumulative-rsi — fixed oversold/overbought rails), there is no fixed RSI level anywhere: the gate is a moving RSI-vs-RSI cross-state, so the permission adapts to the volatility regime rather than to an absolute number. Unlike stop/target bracket records (the merged PowerZone 1.5R/1.0R family — pattern-anchored risk boxes with hard caps), winners can run and losers have no guardrail before the opposite conjunction — the record's principal risk, disclosed, never upgraded. The short leg is the exact mirror (no separate short thesis). The edge, if any, lives in the documented scalper intuition that micro-displacements against a slow uptrend tend to snap back before the trend vote flips — a bet on minutes-scale with-trend snap-back, not on any level, streak, calendar effect, volume flow, or second timeframe.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 5-minute bars `t = 0, 1, ...` with real Binance BTC-USDT futures `O[t], H[t], L[t], C[t]` (volume not read). A bar with missing/nonfinite/non-positive prices, or with `H < max(O,C)` / `L < min(O,C)`, is invalid; never interpolate. All inputs pinned at source defaults: `ATR = 14`, `MULT = 1.0`, `SMOOTH = WMA`, `RSIF = 25`, `RSIS = 100` (any other values are a different, unpinned rule).

- **True range `TR[t]`:** `max(H[t] − L[t], |H[t] − C[t−1]|, |L[t] − C[t−1]|)` (Pine `ta.tr(true)` semantics; `TR[0]` uses the bar's own range only, never a fabricated prior close).
- **ATR scale `A[t]`:** WMA of `TR` over 14 bars (pinned `ma_function` WMA branch; undefined before 14 valid bars).
- **Bands:** `UB[t] = C[t] + A[t]`; `LB[t] = C[t] − A[t]` (`A[t] ≥ 0` always — TR is non-negative and WMA weights are positive — so `LB[t] ≤ C[t] ≤ UB[t]` by construction).
- **Trend vote:** `RL[t] = (RSI25[t] > RSI100[t])`; `RS[t] = (RSI25[t] < RSI100[t])` (RSI100 undefined before 100 valid bars → both false; exact RSI equality → both false, flat hold).
- **Long entry `EL[t]`:** `(O[t] < LB[t]) AND RL[t]`, evaluated on the completed bar. **Short entry `ES[t]`:** `(O[t] > UB[t]) AND RS[t]`.
- **Mutual exclusivity (proven, no invented priority):** `EL[t]` needs `RSI25 > RSI100` while `ES[t]` needs `RSI25 < RSI100` (RSI equality fires neither); `EL[t]` needs `O[t] < LB[t] ≤ C[t]` while `ES[t]` needs `O[t] > UB[t] ≥ C[t]` (band-equality fires neither). No bar can print both entries — verified by 20,000-tape exclusivity fuzz plus four analytic cases in scratch this cycle: `SELF-CHECK OK`. A signal bar arriving while positioned on the same side is discarded unseen (explicitly no queue, no add).
- **Exits:** the first opposite entry reverses the full unit in one step (close plus opposite entry at the same next-bar-open fill); there is no flatten-without-reverse leg, no stop-loss, no take-profit, no trailing, no time exit (the source ships no `strategy.exit`/`strategy.close` — carried over exactly, disclosed in Provenance, never upgraded into a source claim).

**Direction (Gate 2):** BUY-to-open / SELL-to-close on the long leg; SELL-to-open / BUY-to-close on the short leg. The short leg requires margin-short permission, realistic on the pinned perpetual venue (same two-sided posture as the merged PowerZone record). No hedge, no cross-market trade.

**Risk (Gate 3, explicit):** reversal-only book. No stop-loss, no take-profit, no trailing, no time stop, no breakeven move, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default. An end-of-sample open position is marked at the last real valid close, not closed with an invented fill.

**State (Gate 4):** `FLAT`, `BUY_PENDING`, `LONG`, `SELL_PENDING`, `SHORT`, `COVER_PENDING`. Initialize `FLAT` after 120 valid completed bars. Entries fire only from confirmed `FLAT` (long/short) or as one-step reversals from the opposite confirmed state; a missing/failed/unconfirmed fill **halts** this research run, never synthesizes inventory. While `LONG`, further `EL` bars are no-ops and `ES` reverses; symmetrically while `SHORT`. A pending order prohibits additional actions. **No DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no pyramiding, no concurrency, no compounding. No cooldown is specified (explicitly none, not invented) — re-entry needs a fresh conjunction print.

## Required data / Gate 6 causality

**Warmup:** minimum 120 contiguous completed 5m bars before the first actionable bar; covers the RSI100 seed (structural first-signal bar index 100) plus margin over the EMA65/WMA14 seeds. No warmup-bar trades; initial state starts from the actual first historical bar, not from full-sample fitted statistics.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `binance_perpetual_candles.py` parses futures Kline row[0] timestamp with rows[1..5] OHLCV at the bounded commit; the 5m interval is a carried `INTERVALS` entry in `candles_base.py`). A bar's OHLCV becomes available no earlier than `T[t] + 300s`. All decisions are computed on completed bars only; fills are effective at the next bar's open. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting, `security()` call, or same-bar intrabar touch is used — every input reads bars `t` (completed) and backward only. The next-open fill is a **research-model convention** in the Pine market-order timing class, not a real-world claim of zero-latency capture. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (verified an ancestor of the local checkout `2dbc844` this cycle). Bytes read at the pin this cycle: `hummingbot/VERSION` file reads `2.17.0` (the `dev-2.17.0` policy VERSION label); `binance_perpetual_candles.py` parses Binance futures Kline open-time and OHLCV (row[0] timestamp, rows[1..5] OHLCV); `candles_base.py` `INTERVALS` carries the `"5m": 300` entry; `backtesting_engine_base.py` chains `run_backtesting` → `simulate_execution` with the `trade_cost = 0.0002` default. Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT perpetual venue, one 5m OHLCV stream (source stanza backtests `Futures_Binance BTC_USDT` at `period: 5m`). No funding or perpetual margin/mark/index read appears anywhere in the gating path (pure OHLC shape-plus-RSI logic). No order-book decision, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must calculate the exact WMA-TR14 bands, the RSI25/RSI100 vote, and the open-penetration conjunctions with time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries/reversals use `OrderExecutorConfig` with `side = BUY/SELL`, `position_action = OPEN/CLOSE`, `amount = Decimal("0.01")` (the fixed initial and only unit size), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated; no liquidation-relevant leverage claim). MARKET entries fill at the next bar's **open** per the pinned research-model convention (Pine market-order timing class). Do not infer a position from the order request; the controller must use confirmed executor/hold state with a persistent ledger. No entry executes if its required future bar is absent.
- **Fees and accounting:** pin an explicit hypothetical 0.1% fee per filled side (researcher assumption, not a source fact and not a verified Binance tier); no slippage/spread modeled, **not** evidence of zero real slippage. Funding is **flagged, never zeroed**: two-sided 5m holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held span carries modeled funding — modeled economics are not realized/canonical funding (same funding language as the merged PowerZone two-sided record). Never treat engine PnL outputs as fee-inclusive net equity without reconstructing from the actual fill ledger plus recorded fees. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Package/commit binding disclosure:** `setup.py` version labels vs the `20260920` policy package label are not re-mapped here — `20260920` is retained as the policy package **label only**, and Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with no novel execution primitive (no trailing/intrabar/maker leg is introduced). Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 3770-byte file ships the complete construction: the `5m`/`Futures_Binance`/`BTC_USDT` stanza, the seven pinned input defaults, the WMA-TR14 band arithmetic, the RSI25/RSI100 vote, the open-penetration triggers, both `when=`-gated `strategy.entry` legs, and the ChaoZhang credit. It ships no sample statistics, trade count, fee basis, win rate, or performance figure of any kind — no source-reported performance is adopted or restated.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifact this run is a researcher self-check of the entry conjunctions plus entry-leg mutual exclusivity on synthetic bars (dip-in-uptrend fires long-only, rally-in-downtrend fires short-only, RSI-equality and inside-band print nothing, 20,000-tape exclusivity fuzz), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

### Negative evidence and deduplication

At the pre-write snapshot `main@4a44578b`, the root Git tree contained **472** strategy Markdown records. Exact-identity working-tree searches for `365373`, `super-scalper`, `SuperScalper`, `RSILong`, `rsi1 > rsi2`, `atr_slen` return **zero** records using this source, author, file, or dual-RSI/ATR-band construction. Twelve open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646) were inspected by title and source — none uses this file or a dual-RSI band-dip mechanism. Pool cousins fenced as different mechanisms on five axes: `freqtrade-cofibit-stochf-ema-rail-adx-gated` (STOCHF-5/3 cross plus EMA5(high/low) rails plus ADX14 gate with hyperopt 25/75 thresholds, 4-rung ROI ladder with −25% stop — different oscillators, different rails, different gate, different exit class); `forven-atr-breakout-channel` (SMA(TR,14)×2.0 bands around the *prior* close, close-breakout entry, long-flat, 1h — different smoother, different multiplier, different anchor, different trigger, different direction set, no RSI vote); `fmz-434330-ttm-scalper` (TTM Squeeze lattice, long-flat, 1d — different construction, different exits); single-RSI threshold records (`cumulative-rsi`, `connors-rsi2` — fixed oversold/overbought rails, no RSI-vs-RSI vote, no band trigger); `eterna-keltner-20-10-2p0-pullback` (Keltner pullback-reclaim, different bands, different trigger). No pool record conjoins an RSI25-vs-RSI100 cross-state trend vote with a WMA-TR14 close-anchored band open-penetration trigger and a reversal-only two-sided book on 5m bars. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen dual-RSI band-dip book against (a) a band-only baseline (open-penetration entries without the RSI vote — same book, grid, fills), (b) an RSI-only baseline (entries on the RSI25/RSI100 cross-state without any band penetration — same book, grid, fills), and (c) a 15m-horizon twin (identical construction on 15m bars with a 130-bar adopted warmup — the source's own second frame); check event rate, vote-suppression rate, and sensitivity to the 120-bar warmup. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 5m** only. Stated plainly: the 5m frame prints up to 288 decisions per day and positions reverse on every opposite conjunction — whipsaw stretches flip the book at the worst prints of each swing, disclosed. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The 5m frame, venue, sizing, costs, leverage, warmup, next-open MARKET fills, and reversal-only resolution are researcher pins, never attributed to the source. The prose's 1:2R/stop-loss/take-profit discipline and EMA golden-cross confirmation are dead/plot-only at the coded defaults (adopted as coded, disclosed). The sourceless sizing stub is replaced, never ported. Adverse moves have no guardrail before the opposite conjunction, by the carried-over source design — the record's principal risk. A position whose opposite conjunction never prints is held indefinitely with no time exit. Framework readings (single-position book, Pine market-order timing class) are conventional pins, never file literals. Funding/mark/liquidation are flagged unmodeled, never zero. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page: https://www.fmz.com/strategy/365373 (author `ChaoZhang`; fetched live 2026-10-31, 713,921 bytes, HTTP 200, no login)
- Primary code: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/Super-Scalper-5-Min-15-Min.md (commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, verified repository HEAD this cycle; blob `0110dafba2407efbdad8c854587322b2fdf63cc8`, 3770 bytes / 128 lines, byte-identical via `git hash-object`, SHA-256 `a7c41e38d8c5e79a0f30627de8179f3e688a2a507b788386d16c9189df5f0a24`)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Reversal-only precedent: https://github.com/HCH725/alpha-strategy-research/pull/590 (1-3-1 family; sibling evidence only, never proof of this candidate)
