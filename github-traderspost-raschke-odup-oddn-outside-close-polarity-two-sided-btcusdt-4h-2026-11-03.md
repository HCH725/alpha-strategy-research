---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradersPost Raschke ODUP/ODDN outside-bar close-polarity two-sided on BTCUSDT 4h bars
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-07-23
sources:
  - https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/raschke-patterns.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ODUP/ODDN outside-bar close-polarity + avg-price 2%/4% box — independent BTC-USDT 4h derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `TradersPost/pinescript-agents` commit **`ebc382f88b6103fcda2569fe666a38b00fe714c5`** (2026-07-23 — still the repo HEAD, verified live this cycle via `git ls-remote`), file **`projects/raschke-patterns.pine`**, blob `b6d473b8b7f6bfb3538471f5a786cd3c228778db` (contents API at the pinned ref, size 27536), **27,536 bytes / 506 lines**, Pine v6, `indicator("Raschke Patterns", ...)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `92287b6fde409d57539878b07a5b615b0d926abf9b4cfcb0ca17ae720a8f08ce`, byte-identical to the admitted 80-20 and Turtle-Soup siblings ported from this same file. Permalink above. This is the same file the admitted 80-20 sibling (merged) and Turtle-Soup sibling (merged) were ported from; both records explicitly fenced the ODUP/ODDN family OUT, so none of its predicates is pinned there.

**Order-affecting logic read verbatim (code governs):** `outside = high > high[1] and low < low[1]` (line 218); `odUp = enOD and outside and close > open` (line 219); `odDown = enOD and outside and close < open` (line 220); gate default `enOD = input.bool(true, "Outside Up/Down (ODUP/ODDN)", ...)`; the two legs join the shared marker ORs `sigBull = ... or odUp or ...` / `sigBear = ... or odDown or ...` (lines 293–294, display triggers, never orders — disclosed); markers `plotshape(showMarkers and odUp, "ODUP", shape.triangleup, location.belowbar, ...)` / mirrored `odDown` (lines 350/365); per-pattern log calls `logEvt(odUp, "Outside Up (ODUP)")` / `logEvt(odDown, "Outside Down (ODDN)")` (lines 499–500). Strict inequalities throughout — equality on any leg fires nothing. Body size, wick split, ATR multiple, volume and trend play no role in these two legs — disclosed.

**Pine-block census (this cycle, over the pinned bytes):** 1 `indicator(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 real `strategy.order` (1 `{{strategy.order.alert_message}}` template placeholder only); 0 `request.*` / 0 `security(` / 0 `input.session` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` — all recorded as absent, never filled in; `timeframe.period` ×2 appears only inside alert/log display strings, never in signal math (disclosed); per-bar `alert()` uses `alert.freq_once_per_bar_close` (close-decided intent, disclosed); Pine Logs writes are gated on `barstate.isconfirmed` (disclosed); 6 `alertcondition` entries are dropdown/pick-list conveniences only (disclosed). The file's own header warns "detections use the bar's CLOSE; on the live (forming) bar a signal can appear/disappear until the bar closes" and states "All patterns use the chart timeframe" (chart-agnostic, no market pinned) — the once-per-completed-bar researcher pin below is the direct answer (disclosed). `ta.atr` / `ta.ema` / `ta.dmi` are computed for OTHER families' legs only (lines 135–137) and are never read by any OD-gating line — dropped, disclosed (same fencing class as the WorldQuant siblings' unread legs). All markers/plotcandle/boxes/lines/legend/table/recolor/display-only inputs are dropped, disclosed. The other eight pattern families in the file (Turtle Soup, TS+1, 80-20, Inside Bar, FIB, NR4/NR7, Bar Gap Reversal, Holy Grail) are explicitly fenced OUT — none of their predicates, state, or parameters is pinned here (disclosed). No LICENSE file ships in the repo — short-literal citation only, no source block reproduced.

**Structural facts carried over exactly:** (a) two-bar range-engulf predicates with strict inequalities (`H>H[1]`, `L<L[1]`); (b) close-vs-open polarity only (`C>O` bull, `C<O` bear — no close-vs-prior-extreme level, no body-size gate, no ATR multiple); (c) source-declared polarity (up-bar long leg, down-bar short leg); (d) flat-only promotion (the indicator ships no position concept; single-position no-add is a researcher pin — disclosed); (e) the doji edge (`C==O`) is an explicit neither-fire hold. No MTF, no session/timezone, no gap dependence anywhere in the ported legs (the file's session-sensitive gap leg is fenced out, disclosed).

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the two source ODUP/ODDN setup predicates to two-sided entries on confirmed bars (disclosed promotion, same strict semantics and polarity); (2) latched avg-price −2%/+4% box with reversal-dominate stop-first resolution (fully researcher-designed risk/state — the source has no exits; the 2%/4% geometry reuses the admitted 80-20/Turtle-Soup house box so OD attribution isolates the signal, disclosed); (3) fixed **0.01 BTC** sizing (≈770.7 USDT at probe close 77,068.8, above verified 50-USDT min-notional and 0.001 min-qty; 10,000 USDT cash; Isolated 1×); (4) 100-bar warmup with pre-warmup bars flat (structural minimum is 1 prior bar for the `[1]` reference, plus a 99-bar researcher margin matching the admitted sibling chain); (5) display drop (markers, candles, boxes, lines, legend, table, alerts, logs); (6) constant fence (outside-strict/close-polarity/two-sided/box-on — any other predicate value is a different unpinned rule); (7) explicit **0.05%/side research cost**, slippage unmodeled (disclosed); (8) close-decided entries filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (the source's close-decided intent preserved; the intrabar-instability warning is answered by pin, disclosed).

**Co-fire impossibility proof:** bull needs `C>O` and bear needs `C<O` on the same bar — jointly impossible. Both-legs firing is provably unreachable; the flat tie-hold branch (doji `C==O`, verified on tape) is coded defensively only (disclosed).

**Immutable derivative identity:** `GH:TradersPost-ebc382f|raschke-ODUP-ODDN_outside-strict_closepolarity|independent-derived-v1|BinanceFutures:BTC-USDT:4h|TWO-SIDED|0.01BTC|nextopen-MARKET|SL2-TP4-avgpx-latched|fee0.0005|cash10000|lev1x-isolated|reversal-dominate-stopfirst-noop|warmup100|2026-11-03`. Changing any predicate, polarity, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Range-expansion reversal setups: a bar that engulfs the prior bar's full range and closes with polarity is marked ODUP (up) / ODDN (down). The file ships no performance figure, no trade rule, no market thesis — none adopted.

### Research interpretation

Unlike pool hammer/shooting-star records (fixed single-bar shapes, long-only) and pool engulfing records (body-overlap predicates), this machine keys off **full-range engulf plus close polarity**: both extremes must print outside the prior bar's extremes (strict), and the close alone decides the leg — no body-size, wick, volume or trend gate. Unlike the admitted 80-20 sibling (open/close location within the bar's own range plus a 1.5× ATR width gate — a climax object) and the admitted Turtle-Soup sibling (swept 20-bar extreme plus reversal close with a 4-bar freshness gate — a level-sweep object), this trigger reads only the last two bars and carries no lookback window, no ATR, no level memory of any kind — the purest two-bar event in the Raschke file. Unlike pool outside-day SpeculationLab (downside close below the prior low plus a 1.5× body-expansion gate, long-only 1d spot with a 3-bar time exit — a close-location object), this machine fires on EITHER polarity with no location or size gate, trades two-sided on 4h futures, and exits only through the researcher 2%/4% box or an opposite setup — direction, frame, venue, gates and exits all differ (see Negative evidence). Live-window rate is 48 post-warmup predicate bars per 1,499 4h bars (22 bull-leg / 26 bear-leg), driving 106 opens / 106 closes (30 SL / 18 TP / 58 reversals) — the fade-and-reverse character (over half of closes are opposite-setup reversals) is structural, not tuned.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 4-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]`/`O[t]` for polarity, `H[t]`/`L[t]` for engulf/box-touch legs. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals. All predicates are source-default literals at `enOD=true`; every other family toggle is pinned off.

- **Predicates (actionable only t ≥ 100, at bar `t`'s close, Pine-faithful):** `bull[t] = (H[t]>H[t-1]) and (L[t]<L[t-1]) and (C[t]>O[t])`; `bear[t] = (H[t]>H[t-1]) and (L[t]<L[t-1]) and (C[t]<O[t])`. Pre-warmup bars flat by record rule; every na/degenerate/doji bar is an explicit neither-fire hold. Strict inequalities match source exactly (equality never fires).
- **Latched box (researcher-designed, fixed at fill-average `A`, never moved):** long `SL=A×0.98`, `TP=A×1.04`; short mirrored `SL=A×1.02`, `TP=A×0.96`.
- **Resolution (explicit researcher pin):** entries fill next-bar-open MARKET; each held bar `v` (fill bar +1 onward) evaluates at its close in code order — opposite setup first (reversal dominates: close old and open new at the same next open; tie bars defensively hold per the impossibility proof), else SL-touch, else TP-touch (`H/L` vs latched levels); SL+TP co-fire is one flat close (stop wins). Single position, no adds: same-side refire is a no-op (verified on tape).

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous valid completed 4h bars; covers the single `[1]`-offset prior-bar reference plus a 99-bar researcher margin matching the admitted sibling chain (the ported legs read no ATR/EMA/DMI, so no seeder convergence is needed — disclosed). No warmup-bar trades; pre-warmup flat by record rule.

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `4h` is a carried `INTERVALS` entry `14400` — byte-verified at the pin this cycle; forming bar dropped by `closeTime`, completed-only probe verified live this cycle: 1,499 bars 2026-02-26→2026-11-02). Bars become available no earlier than `T[t]+14400s`. All decisions use completed bars only (researcher once-per-bar pin answering the source's forming-bar instability warning); fills at next-bar open; SL/TP legs are close-decided against completed-bar `H/L` with next-open fills (research-model convention, disclosed). No incomplete bar, future extremum, repainted graphic, MTF call, session template, gap state, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` line 221, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py` line 747, `class OrderExecutorSimulator` byte-present in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` line 9, `INTERVALS "4h": 14400` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py` line 20). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 4h OHLCV stream (single-feed design — no MTF, no session, no second symbol, no gap feed). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the two-bar strict-engulf plus close-polarity predicates and the avg-price 2%/4% latch with the reversal-dominate stop-first no-op state pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes `position_action = CLOSE` (SL, TP, and reversal legs all close-then-act per the pin), `amount = Decimal("0.01")` (≈770.7 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the record timing pin. No fill executes if its required future bar is absent. Exit evaluation starts at `fill+1`, so every exit decision acts on a fill confirmed at least one full bar earlier (admitted ledger-lag discipline). Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-size 1× single-position with no compounding and no abort rule (disclosed).
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin; slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 4h holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided box legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 506-line fence ships the complete ODUP/ODDN construction: the two-bar strict-engulf formula, the close-vs-open polarity legs with `enOD=true` default, the shared marker-OR joins, the triangle markers, the per-pattern log calls, the close-decided alert/log intent, and the forming-bar instability warning — plus the explicit fence that the other eight families are separate toggles. It ships no performance figure of any kind — none adopted. It ships no order, sizing, or risk of any kind — the box is 100% researcher design (disclosed).

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/latch/state pipeline (Pine-faithful engulf split, strict polarity, avg-price latch, code-order reversal-dominate stop-first no-op resolution, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS, double-run identical):** MICRO-BULL tape prints 1 post-warmup bull leg driving 1 open / 1 TP close ending flat (digest `c03f8b8453`); MICRO-BEAR tape prints 1 bear leg driving 1 open / 1 TP close ending flat (digest `0e12249f89`); MICRO-SL tape prints 1 bull leg driving 1 open / 1 SL close ending flat (digest `efc007542f`); MICRO-REV tape prints 1 bull + 1 bear leg driving 2 opens / 1 reversal close + 1 TP close ending flat with the reversal dominating a simultaneous SL-touch bar (digest `bc3880cac0`); MICRO-TIE tape prints an outside doji (`C==O`) driving 0 opens ending flat (digest `b74753435a`).

**Live-exchange microstructure probes (this cycle, futures 4h klines, 1,499 completed bars 2026-02-26→2026-11-02, forming bar dropped by closeTime, last close 77,068.8):** 22 post-warmup bull and 26 post-warmup bear predicate bars drive 106 state-machine opens / 106 closes (30 SL-touch / 18 TP-touch / 58 reversals) ending FLAT (signal digest `1d8255c955`); first fire at bar 188 (warmup sane); sub-window bars 300–999 print 48 opens / 47 closes (15 SL / 5 TP / 27 reversals) ending SHORT-HELD at the honest cut with no invented fill (digest `6f7efd6759`). 0.01 BTC ≈ 770.7 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

At the pre-write snapshot `main@86c5d23e`, the root Git tree contained **526** strategy Markdown records (528 files minus two READMEs). Exact-identity working-tree searches for `odup` / `oddn` / `outside up` / `outside down` return **only** the two admitted siblings' fence lists (`github-traderspost-80-20-...`, `github-traderspost-turtle-soup-...`), both of which explicitly fence ODUP/ODDN OUT as unclaimed — zero records embody this rule. The nearest outside-bar neighbour `tradingview-speculationlab-outside-day-downclose-bodyfade-time3-long-btcusdt-1d-2026-10-30.md` is five-axis distinct: different source (TradingView X4ulJUXd vs TradersPost GitHub pin), different signal construction (close-below-prior-low location plus 1.5× body-expansion gate vs pure close-vs-open polarity with no gate — its long trigger would map to this record's SHORT leg on shared bars), different direction (long-flat vs two-sided), different frame/venue (1d spot vs 4h futures), different exits (3-bar time exit vs 2%/4% box with reversals). The admitted same-file siblings are different mechanisms (80-20 climax locations with ATR gate; Turtle-Soup 20-bar sweep levels with freshness gate — both carry window/level memory this trigger has none of). Sixteen open `research/*` PRs were inspected by per-PR title/head — no collision (nearest open lanes are Alpha57-VWAP, EMA-stack-RSI, OneTrend, dual-MACD, volume-dip, supertrend, Heracles, ClucMay, AdxSmas, CCI, 2yMA, SSL, Chandelier, Gaussian, Larry-Williams — none an outside-bar machine). Closed-PR scan surfaces the two same-file siblings' research PRs (#701 Turtle-Soup, #704 80-20, both merged-lineage) and the SpeculationLab research PR (#624, distinct as above) — no ODUP/ODDN member. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen ODUP/ODDN box book against (a) no-box twins (pure setup-to-opposite-setup reversal — isolating the percent box), (b) house 1%/2% and 3%/6% box twins (isolating the 2R choice shared with the siblings; researcher variation), (c) sibling-pattern cross-checks (80-20-only and Turtle-Soup-only legs on the same window — isolating what the gateless two-bar trigger adds beyond its windowed cousins; researcher variation — never attributed to source), and (d) warmup sensitivity (100 vs 200). Check event rate, SL/TP/reversal attribution, hold-time distribution, and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 4h** only — a researcher frame pin on a chart-agnostic indicator, no port claimed. Stated plainly: the machine needs completed-bar OHLC plus the 100-bar admission warmup (single-prior-bar bound); the entries are gateless two-bar outside closes with a live-window rate of ~48 predicates per 1,499 4h bars; the exits are a researcher-latched 2%/4% avg-price box with reversal dominance; 4h slippage plus funding apply to every held span. The ported legs carry no session, calendar, or gap dependence (the file's session-sensitive gap leg is fenced out, disclosed), so 24/7 crypto continuous trading introduces no anchor or session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The two-sided promotion, next-open fills, 2%/4% box, reversal dominance, stop-wins-tie, same-side no-op, fill+1 evaluation, 100 warmup, 0.01 BTC 1× sizing, 0.05% research fee, and all display/family drops are researcher pins, never attributed to the source. The `ta.atr`/`ta.ema`/`ta.dmi` lines execute in the source every bar for other families but are unread by either OD leg — fenced out, never ported. The forming-bar instability warning is answered by the once-per-completed-bar pin with disclosed whipsaw risk. The page ships no LICENSE (short-literal citation only, research-only use asserted, no commercial claim). No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/raschke-patterns.pine (commit `ebc382f88b6103fcda2569fe666a38b00fe714c5`, 2026-07-23, still HEAD verified live 2026-11-03; blob `b6d473b8b7f6bfb3538471f5a786cd3c228778db`; Pine v6, 506 lines / 27,536 bytes; raw sha256 `92287b6fde409d57539878b07a5b615b0d926abf9b4cfcb0ca17ae720a8f08ce` verified live 2026-11-03; OD legs lines 218–220, `enOD` default-true, shared ORs lines 293–294; no LICENSE — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `TRADING`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 4h microstructure probes (1,499 completed bars 2026-02-26→2026-11-02, forming bar dropped by closeTime, 48 predicates → 106 opens / 106 closes; tape digests `c03f8b8453`/`0e12249f89`/`efc007542f`/`bc3880cac0`/`b74753435a`, signal digest `1d8255c955`, sub-window digest `6f7efd6759`, first fire bar 188), fetched live 2026-11-03
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Same-file admitted siblings (different mechanisms, OD explicitly fenced out): `github-traderspost-80-20-wide-bar-fade-two-sided-btcusdt-4h-2026-11-02.md`; `github-traderspost-turtle-soup-sweep-fade-two-sided-btcusdt-4h-2026-11-02.md`
- Nearest outside-bar lineage (different construction/direction/frame/venue/exits): `tradingview-speculationlab-outside-day-downclose-bodyfade-time3-long-btcusdt-1d-2026-10-30.md` (research PR #624)
