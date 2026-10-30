---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FMZ PowerZone 5-bar anchor-breakout 1.5R/1.0R bracket two-sided on ETHUSDT 1d bars
created: 2026-10-31
updated: 2026-10-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-03-31
sources:
  - https://www.fmz.com/strategy/488909
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/PowerZone交易策略-PowerZone-Trading-Strategy.md
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ PowerZone anchor-breakout bracket — independent ETH-USDT 1d two-sided derivative

## Provenance

**Canonical page (fetched live over HTTPS this cycle, HTTP 200, 749,619 bytes, no login):** FMZ public strategy **488909**, *PowerZone交易策略-PowerZone-Trading-Strategy*, porter nickname **ianzeng123**, https://www.fmz.com/strategy/488909 . The served page carries the ZH/EN prose (anchor-plus-five-consecutive rule, 1.5×/1.0× bracket, two-sided posture), the `/*backtest*/` stanza (`start: 2024-03-31 00:00:00`, `end: 2025-03-29 08:00:00`, `period: 1d`, `basePeriod: 1d`, `exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]` — quoted verbatim, never normalized), and a 12-line / 303-byte Pine preview ending at `//@version=6` (SHA-256 `e3a532924c487f8b410bc338a2bad2a3b9ca1af2ab8fbfd20ae8d3c28e8648d2`) behind the page's login overlay for the remainder. The page's meta keywords (`RSI,EMA,TP,SL,PZ`) name indicators the executable code never calls — recorded as prose only, never as signal.

**Immutable mirror actually executed against (primary code source):** repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified as the repository HEAD via `git ls-remote` this cycle — the same head pin as the merged 1-3-1, Dual-Thrust, soldiers/crows and further FMZ admissions), exact file path `PowerZone交易策略-PowerZone-Trading-Strategy.md` (9278 bytes, 242 lines; GitHub contents-API blob SHA `430d034a505b5a16ad8e228dedab91ccb1d10d11`, size 9278 — byte-identical to the fetched file: local `git hash-object` reproduces `430d034a…10d11`, SHA-256 `45decc307ea5ea1f4a237da193f00f3c1b172664ceb20da412e8663f4941acb0`). The mirror prints `> Name` = the strategy title, `> Author` = `ianzeng123` (mirror porter; the Pine block itself credits `// © tradingbauhaus` under MPL-2.0), `> Detail` = the canonical page URL, `> Last Modified` = `2025-03-31 17:34:35` (date part adopted as `source_as_of`), the `[trans]` ZH/EN prose matching the canonical page, and the complete executable `//@version=6` Pine block (lines 142–208). This dual page-plus-mirror sourcing is the same path as the merged 1-3-1 (FMZ 430364) and MA-ribbon-MACD (FMZ 483047) admissions. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Order-affecting lines read verbatim (code governs everywhere it conflicts with prose):** `periods = input.int(5, ...)`; `threshold = input.float(0.0, ...)`; `usewicks = input.bool(false, ...)`; `tp_factor = input.float(1.5, ...)`; `sl_factor = input.float(1.0, ...)`; `ob_period = periods + 1` (= 6); `absmove = math.abs((close[ob_period] - close[1]) / close[ob_period]) * 100`; `relmove = absmove >= threshold`; bull `bullishPZ = close[ob_period] < open[ob_period]`, `upcandles` counting `close[i+1] > open[i+1]` for `i = 0 to periods-1`, `PZ_bull = bullishPZ and upcandles == periods and relmove`, box `PZ_bull_high = open[ob_period]` / `PZ_bull_low = low[ob_period]` (the `usewicks` true-branches never execute at the pinned default); bear mirror with `close[ob_period] > open[ob_period]`, `downcandles`, `PZ_bear_high = high[ob_period]` / `PZ_bear_low = open[ob_period]`; entries `if PZ_bull and close > PZ_bull_high and strategy.position_size == 0` → `strategy.entry("BullPZ", strategy.long)` + `strategy.exit("BullExit", "BullPZ", limit=bull_tp, stop=bull_sl)` with `bull_tp := close + (PZ_bull_high - PZ_bull_low) * tp_factor`, `bull_sl := PZ_bull_low - (PZ_bull_high - PZ_bull_low) * sl_factor`; bear mirror (`close < PZ_bear_low`, `strategy.short`, `bear_tp := close - R*1.5`, `bear_sl := high + R*1.0`).

**Text census over the pinned code block:** 1 `strategy(` (title `PowerZone Trading Strategy`, `overlay=true`, `default_qty_type = strategy.percent_of_equity, default_qty_value = 100` sizing stub — no capital, cost, timing or pyramiding argument ships anywhere); 2 `strategy.entry` (`"BullPZ"`/`strategy.long`, `"BearPZ"`/`strategy.short`, no `qty=`/`limit=`/`stop=`/`when=` qualifiers, both flat-gated); 2 `strategy.exit` (`"BullExit"`/`"BearExit"`, `limit=` + `stop=`, no trailing qualifier); 0 `strategy.close` / 0 `strategy.order` / 0 `strategy.risk` / 0 `strategy.cancel`; 0 `ta.*` / 0 indicator calls of any kind (pure OHLC shape logic — the page-keyword RSI/EMA appear nowhere in code); 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `volume` / 0 `nz(`; 0 `pyramiding` / 0 `process_orders_on_close` / 0 `commission` / 0 `slippage` / 0 `initial_capital` / 0 `calc_on_every_tick`. Display/alert/panel blocks (`plot(`, `alertcondition(`, info-panel `label.new`, `showdocu` doc label, color-scheme inputs) are render-only and cannot change any order condition.

**Prose-vs-code conflicts (code governs, disclosed):** (a) the ZH/EN prose claims the move gate defaults to 2%, but the pinned code default is `threshold = 0.0`, so `relmove` is identically true — the move gate is vacuous in this derivative, never presented as a live filter; (b) the prose says the five bars show an "uptrend", but the code tests bar color (`close > open`), not rising closes — color governs; (c) the prose's "breakout" wording is exact in code (`close > PZ_bull_high` / `close < PZ_bear_low` on the pattern-completing bar).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly seven: (1) market/frame pin Binance **ETHUSDT 1d** (the stanza itself backtests `Futures_Binance ETH_USDT` at `period: 1d` — market and decision frame are both source-native; `basePeriod: 1d` is FMZ execution plumbing, not a second signal frame); (2) completed-bar decisions with same-bar-close MARKET entries (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills next-bar-open; this record claims no source fills, same conversion class as merged Alpha PRs #590/#592/#594/#596/#602 and the 1-3-1 record); (3) an adopted 10-bar warmup with pre-warmup bars flat by record rule (covers the `[6]` seed with margin); (4) house sizing/capital/costs replacing the percent-of-equity stub (fixed 0.1 ETH, 10,000 USDT cash admission, 0.1%/side researcher fee; Isolated 1×; fees plus historical funding, no hypothetical zero funding claimed); (5) the resting stop+limit OCO pair resolved post-hoc by first-touch against completed-bar high/low with the pinned stop-first same-bar rule (same bracket class as the merged 1-3-1 record); (6) the Pine-default no-pyramiding behavior pinned as an explicit single-position gate (entries only when confirmed FLAT — coded `position_size == 0` on both legs); (7) display/alert/panel/doc branches dropped with zero decision function. The 5-consecutive color count, the opposite-color anchor, the anchor-open breakout trigger, the open-to-extreme risk box, the 1.5R/1.0R arithmetic, the flat-only gate, the two-sided stance, and the bracket-only exit posture are source-native and unmodified.

**Immutable derivative identity:** `FMZ:488909|tradingbauhaus-v6|5bar-anchor-breakout-15R-10R|independent-derived-v1|BinanceFutures:ETH-USDT:1d|TWO-SIDED|0.1ETH|samebar-close-MARKET|fee0.001|cash10000|lev1x-isolated|stop-first-bracket|warmup10|2026-10-31`. Changing any formula, threshold, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Exhaustion-anchored II-shaped continuation bet, both directions. A lone opposite-color bar prints the local wash; five subsequent same-color bars confirm the new tape has held without a single counter-print; the entry is not the pattern itself but the close's break back past the anchor bar's open — i.e. the market must first prove it can trade through the wash bar's origin. The risk box is the anchor bar's own body-to-wick span (`open→low` bull, `high→open` bear): stop one full box beyond the extreme, target one-and-a-half boxes from entry. The prose ships no quantified performance of any kind — only qualitative "captures strong moves" remarks, adopted here as thesis prose, never as evidence.

### Research interpretation

Breakout-of-origin machine with an asymmetric bracket, event-driven, two-sided, flat between trades. Unlike every streak-fade record in the pool it never buys the wash itself and never buys continuation alone: five same-color bars without the opposite anchor fire nothing, and the full six-bar shape without the breakout print fires nothing. Unlike oscillator-gated dip buys there is no level, no smoothing, no band: the signal is pure open/close color plus one extreme anchor plus one price-level trigger. Unlike trailing trend records the stop is pattern-anchored (never ratchets) and the target is a hard 1.5R cap — winners can never run, losers always pay up to the full box-plus distance. The short leg is the exact mirror (no separate short thesis). The edge, if any, lives in the documented tape intuition that a wash origin retaken after five uncontested bars tends to see at least 1.5 risk-units of follow-through before failing — a bet on days-scale post-wash drift, not on any trend, level, indicator, calendar effect, volume flow, or second timeframe.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 1-day bars `t = 0, 1, ...` with real Binance ETH-USDT futures `O[t], H[t], L[t], C[t]` (volume not read). A bar with missing/nonfinite/non-positive prices, or with `H < max(O,C)` / `L < min(O,C)`, is invalid; never interpolate. All inputs pinned at source defaults: `P = 5`, `OB = 6`, `TH = 0.0`, `TPF = 1.5`, `SLF = 1.0` (any other values are a different, unpinned rule).

- **Bull pattern `PB[t]`:** `C[t-6] < O[t-6]` AND `C[t-j] > O[t-j]` for all `j = 1..5` AND `|C[t-6] − C[t-1]| / C[t-6] × 100 ≥ 0.0` (identically true at the pinned default — fenced, never hidden). Risk box `RB[t] = O[t-6] − L[t-6]`.
- **Bull entry `EB[t]`:** `PB[t]` AND `C[t] > O[t-6]`, evaluated on the completed bar, flat-gated. Limit `LTP[t] = C[t] + 1.5 × RB[t]`; stop `LST[t] = L[t-6] − 1.0 × RB[t]` (both frozen at entry, never recomputed).
- **Bear pattern `PS[t]`:** `C[t-6] > O[t-6]` AND `C[t-j] < O[t-j]` for all `j = 1..5` AND the vacuous move gate. Risk box `RS[t] = H[t-6] − O[t-6]`.
- **Bear entry `ES[t]`:** `PS[t]` AND `C[t] < O[t-6]`, flat-gated. Limit `STP[t] = C[t] − 1.5 × RS[t]`; stop `STS[t] = H[t-6] + 1.0 × RS[t]`.
- **Mutual exclusivity (proven, no invented priority):** `EB[t]` needs `C[t-6] < O[t-6]` while `ES[t]` needs `C[t-6] > O[t-6]` (anchor equality fires neither); `EB[t]` needs `C[t] > O[t-6]` while `ES[t]` needs `C[t] < O[t-6]` (trigger equality fires neither). No bar can print both entries. A signal bar arriving while positioned is discarded unseen (coded flat gate, explicitly no queue, no add).

**Direction (Gate 2):** BUY-to-open / SELL-to-close on the bull leg; SELL-to-open / BUY-to-close on the bear leg. The short leg requires margin-short permission, realistic on the pinned perpetual venue (same two-sided posture as the merged Dual-Thrust record). No hedge, no cross-market trade.

**Risk (Gate 3, explicit):** each position's sole closer is its resting OCO pair (`limit` + `stop`, no trailing qualifier anywhere in source). Post-hoc resolution per completed bar after the entry bar: if the bar's range touches neither level, hold; if it touches exactly one, close there; if it touches **both**, the **stop fills first** (pinned stop-first same-bar rule, same bracket class as the merged 1-3-1 record). No profit trigger beyond the 1.5R limit, no breakeven move, no partial exit, no time stop, no averaging, no forced end-of-data liquidation, no silent executor default. An end-of-sample open position is marked at the last real valid close, not closed with an invented fill.

**State (Gate 4):** `FLAT`, `BUY_PENDING`, `LONG`, `SELL_PENDING`, `SHORT`, `COVER_PENDING`. Initialize `FLAT` after 10 valid completed bars. Entries fire only from confirmed `FLAT`; a missing/failed/unconfirmed fill **halts** this research run, never synthesizes inventory. While `LONG`/`SHORT`, all entry predicates are ignored and the opposite pattern resolves nothing (no reversal — the opposite entry needs `FLAT`). A pending order prohibits additional actions. **No DCA/safety orders (explicitly disabled — the downstream 6%+6%+6% house overlay is not active in this admission and never silently overrides single-unit semantics)**, no pyramiding, no concurrency, no compounding. No cooldown is specified (explicitly none, not invented) — re-entry needs a fresh six-bar breakout print, which cannot persist true across bars by construction.

## Required data / Gate 6 causality

**Warmup:** minimum 10 contiguous completed 1d bars before the first actionable bar; covers the `[6]` seed plus margin over the structural 7-bar minimum. No warmup-bar trades; initial state starts from the actual first historical bar, not from full-sample fitted statistics.

Binance Kline `timestamp` is the **bar-open** `T[t]` (pinned `BinanceSpotCandles._parse_rest_candles` reads row[0] at the bounded commit; the perpetual venue streams the same open-time Kline layout). A bar's OHLCV becomes available no earlier than `T[t] + 86400s`. All decisions and fills are effective at completed-bar closes. No incomplete bar, higher-timeframe partial, future extremum, negative shift, repainting, `security()` call, or same-bar intrabar touch is used — every lag call reads bars `t-1` through `t-6`, strictly backward. The simulator's same-row-close fill is a **synthetic completed-bar convention**, not a real-world claim that a post-close order could capture the just-observed historical close. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (verified an ancestor of the local checkout `2dbc844` this cycle). Bytes read at the pin this cycle: `hummingbot/VERSION` content `dev-2.17.0`; `binance_spot_candles.py` parses Binance `/api/v3/klines` open-time and OHLCV (row[0] timestamp, rows[1..5] OHLCV); `constants.py` `INTERVALS` carries the `"1d"` entry; `backtesting_engine_base.py` chains `run_backtesting` → `simulate_execution` with the `trade_cost = 0.0002` default. Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative engine validation for this source/package path; this Scout **did not independently rehash** the wheel or run a backtest. A different deployed package must be revalidated.

- **Market/feed:** Binance ETH-USDT perpetual venue, one 1d OHLCV stream. No funding or perpetual margin/mark/index read appears anywhere in the gating path (pure OHLC shape logic). No order-book decision, no multi-market or mixed-timeframe synchronization.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must calculate the exact six-bar anchor/breakout predicates and perform time gating. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries use `OrderExecutorConfig` with `side = BUY/SELL`, `position_action = OPEN/CLOSE`, `amount = Decimal("0.1")` (the fixed initial and only unit size, same denomination class as merged Alpha PR #590-family 0.1 ETH), `connector_name = "binance"`, `trading_pair = "ETH-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated; no liquidation-relevant leverage claim). MARKET entries fill at the signal row's **close** per the simulator's synthetic completed-bar convention. The resting stop+limit OCO pair is armed from the bar after entry and resolved post-hoc by first-touch against completed-bar high/low with the pinned stop-first same-bar rule (same bracket class as the merged 1-3-1 record) — explicitly a research-model convention, never a claim the pinned engine queues live stop/limit legs. Do not infer a position from the order request; the controller must use confirmed executor/hold state with a persistent ledger. No exit executes if its required future bar is absent.
- **Fees and accounting:** pin an explicit hypothetical 0.1% fee per filled side (researcher assumption, not a source fact and not a verified Binance tier); no slippage/spread modeled, **not** evidence of zero real slippage. Funding is **flagged, never zeroed**: perpetual funding/mark/liquidation cash flows are unmodeled in this research convention — modeled economics are not realized/canonical funding (same funding language as the merged Dual-Thrust two-sided record). Never treat engine PnL outputs as fee-inclusive net equity without reconstructing from the actual fill ledger plus recorded fees. Trading precision/min-notional/partial fills/market impact/actual exchange fee tier remain unverified, so this is not an execution or profitability approval.
- **Package/commit binding disclosure:** `setup.py` version labels vs the `20260920` policy package label are not re-mapped here — `20260920` is retained as the policy package **label only**, and Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET same-close primitive with no novel execution primitive (no trailing/next-open/intrabar leg is introduced). Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 9278-byte file ships the complete construction: the `1d`/`Futures_Binance`/`ETH_USDT` stanza, the five pinned input defaults, the `ob_period = periods + 1` anchor offset, the `absmove`/`relmove` gate, the `upcandles`/`downcandles` five-bar color loops, the anchor-open/extreme risk boxes, the breakout triggers, the flat gates, both `strategy.entry` legs, both `strategy.exit` limit+stop legs, and the MPL-2.0/`tradingbauhaus` credit. It ships no sample statistics, trade count, fee basis, win rate, or performance figure of any kind — no source-reported performance is adopted or restated.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifact this run is a researcher self-check of the pattern/trigger/bracket arithmetic plus entry-leg mutual exclusivity on synthetic bars (bull/bear arithmetic, silence on 4-green, 20,000-tape exclusivity fuzz), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

### Negative evidence and deduplication

At the pre-write snapshot `main@37a86c4b`, the root Git tree contained **471** strategy Markdown records. Exact-identity working-tree searches for `powerzone`, `488909`, `upcandles`, `PZ_bull`, `PZ_bear` return **zero** records using this source (the sole `downcandles` substring hit is the DeMarker record's `SignalCooldownCandles` cooldown field — an unrelated StockSharp throttle, fenced here). Twelve open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646) were inspected by title and source — none uses this file or an anchor-breakout bracket mechanism. Pool cousins fenced as different mechanisms on five axes: `1-3-1-red-green-candle-reversal` (1-red + 3 *rising* greens, long-only, symmetric 1R off the red *low*, no breakout trigger, BTC 1h — different count, different trigger, different box, different symmetry, different direction set); `three-white-soldiers-black-crows-flip` (TA-Lib body/shadow/adaptive-average quality filters, contra-pattern flip-only always-in-market book with **no** stop/target, BTC 1d — different construction, different exit class); `three-down-three-up-consec-close` (3-close-count fade long-only with count exit, no anchor, no box, no bracket); `fmz-482589`-family count rules (different counts, long-only, no breakout/bracket). No pool record conjoins a 5-consecutive color run off an opposite-color anchor with a breakout-of-anchor-open trigger and an asymmetric 1.5R/1.0R resting bracket, two-sided. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen 5-bar anchor-breakout bracket against (a) a no-breakout baseline (entry on pattern completion without the anchor-open trigger) and (b) a symmetric-1R baseline (same entries, 1.0R limit) on identical contiguous ETH-USDT 1d data with the same declared costs; check event rate, breakout-suppression rate, and sensitivity to the 10-bar warmup. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **ETH-USDT Binance futures 1d** only. Stated plainly: the 1d frame prints at most one decision per day and holding times stretch across weeks; six-bar setups are rare and most bars print nothing. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The 1d frame, venue, sizing, costs, leverage, warmup, same-close MARKET entries, and post-hoc bracket resolution are researcher pins, never attributed to the source. The prose's 2% move gate is dead at the coded `0.0` default (adopted as coded, disclosed). The `percent_of_equity` sizing stub is replaced, never ported. Adverse moves pay the full box-plus distance with no cut; winners are capped at 1.5R with no runner. A position whose bracket never touches is held indefinitely with no time exit. Framework defaults (`pyramiding = 0`, Pine next-bar-open timing) are conventional readings replaced by explicit pins, never file literals. Funding/mark/liquidation are flagged unmodeled, never zero. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary page: https://www.fmz.com/strategy/488909 (porter `ianzeng123`, page `Last Modified` role unverified; fetched live 2026-10-31, 749,619 bytes, HTTP 200, no login)
- Primary code: https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/PowerZone交易策略-PowerZone-Trading-Strategy.md (commit `7853bb2bf262c4567ac238d3552d97f0e50cb801`, verified repository HEAD this cycle; blob `430d034a505b5a16ad8e228dedab91ccb1d10d11`, 9278 bytes / 242 lines, byte-identical via `git hash-object`, SHA-256 `45decc307ea5ea1f4a237da193f00f3c1b172664ceb20da412e8663f4941acb0`)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Bracket-resolution precedent: https://github.com/HCH725/alpha-strategy-research/pull/590 (1-3-1 family; sibling evidence only, never proof of this candidate)
