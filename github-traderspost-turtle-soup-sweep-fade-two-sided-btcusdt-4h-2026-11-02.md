---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradersPost Raschke Turtle-Soup 20-bar sweep-fade percent-box two-sided on BTCUSDT 4h bars
created: 2026-11-02
updated: 2026-11-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-02
sources:
  - https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/raschke-patterns.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Turtle-Soup / +1 sweep-fade + avg-price 2%/4% box — independent BTC-USDT 4h derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `TradersPost/pinescript-agents` commit **`ebc382f88b6103fcda2569fe666a38b00fe714c5`** (2026-07-23 — still the repo HEAD, verified live this cycle), file **`projects/raschke-patterns.pine`**, blob `b6d473b8b7f6bfb3538471f5a786cd3c228778db`, **27,536 bytes / 506 lines**, Pine v6, `indicator("Raschke Patterns", ...)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `92287b6fde409d57539878b07a5b615b0d926abf9b4cfcb0ca17ae720a8f08ce`, byte-identical to the working copy. Permalink above.

**Order-affecting logic read verbatim (code governs; indicator ships no orders):** prior-window extremes `prior20High = ta.highest(high, 20)[1]` / `prior20Low = ta.lowest(low, 20)[1]` plus one-bar-older `prior20High1 = ta.highest(high, 20)[2]` / `prior20Low1 = ta.lowest(low, 20)[2]`; extreme age `ageHigh = -ta.highestbars(high, 20)[1] + 1` (mirrored low) with fenced defaults `tsLookback = input.int(20)` / `tsRequireOld = input.bool(true)` / `tsMinBarsAgo = input.int(4)`; classic legs `tsBear = enTS and oldHighOK and high > prior20High and close < prior20High` and `tsBull = enTS and oldLowOK and low < prior20Low and close > prior20Low`; delayed legs `tsPlusBear = enTSP and high[1] > prior20High1 and close < prior20High1` and `tsPlusBull = enTSP and low[1] < prior20Low1 and close > prior20Low1` — in-source these arm markers/alerts only (display triggers, never orders — disclosed).

**Pine-block census (506-line fence):** 1 `indicator(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 0 `request.*` / 0 `security(` / 0 `input.session` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` — all recorded as absent, never filled in; `timeframe.period` appears only inside alert/log display strings, never in signal math (disclosed); per-bar `alert()` uses `alert.freq_once_per_bar_close` (close-decided intent, disclosed); Pine Logs writes are gated on `barstate.isconfirmed` (disclosed); 6 `alertcondition` entries are dropdown/pick-list conveniences only (disclosed). The file's own header warns "detections use the bar's CLOSE; on the live (forming) bar a signal can appear/disappear until the bar closes" — the once-per-completed-bar researcher pin below is the direct answer (disclosed). All markers/plotcandle/boxes/lines/legend/table display-only — dropped, disclosed. The other nine pattern families in the file (80-20, Inside Bar, FIB, ODUP/ODDN, NR4/NR7, Bar Gap Reversal, Holy Grail) are explicitly fenced OUT — none of their predicates, state, or parameters is pinned here (disclosed). No LICENSE file ships in the repo — short-literal citation only, no source block reproduced.

**Structural facts carried over exactly:** (a) false-breakout fade of the prior 20-bar extreme with close back through the level; (b) the swept extreme must be at least 4 bars old (classic age gate at source defaults); (c) the +1 legs time the same mechanism one bar later (breakout on prior bar, reversal close now); (d) bull/bear setup polarity is source-declared (fade up vs fade down); (e) no MTF, no session/timezone, no gap dependence, no intrabar semantics anywhere in the ported legs.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the four source setup predicates to two-sided entries on confirmed bars (disclosed promotion, same strict semantics and polarity); (2) latched avg-price −2%/+4% box with entries-dominate stop-first resolution plus a bull+bear same-bar tie-hold (fully researcher-designed risk/state — the source has no exits; disclosed); (3) fixed **0.01 BTC** sizing (≈783.1 USDT at probe close 78,313.0, above verified 50-USDT min-notional and 0.001 min-qty; 10,000 USDT cash; Isolated 1×); (4) 100-bar warmup with pre-warmup bars flat (20 = structural lookback scale, +80 researcher margin for extreme-age convergence); (5) display drop (markers, candles, boxes, lines, legend, table, alerts, logs); (6) constant fence (20/4/0.01/two-sided/box-on — any other value is a different unpinned rule); (7) explicit **0.05%/side research cost**, slippage unmodeled (disclosed); (8) close-decided entries filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (the source's default bar-close calc class is preserved; the intrabar-instability warning is answered by pin, disclosed).

**Immutable derivative identity:** `GH:TradersPost-ebc382f|raschke-TS-TSplus1_L20-age4_fade_SL2-TP4-avgpx-latched|independent-derived-v1|BinanceFutures:BTC-USDT:4h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|entries-dominate-stopfirst-tiehold|warmup100|2026-11-02`. Changing any formula, length, age, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Failed-breakout trap fade (Linda Raschke short-term setups): price pokes just past a recent extreme like a breakout, then snaps back through the level — the breakout was a trap and price often reverses the other way. The +1 variant is the same trap confirmed a bar later (fake breakout one bar, reversal close the next).

### Research interpretation

Unlike pool average-cross siblings (e.g. naked EMA9/21 cross with the same house 2%/4% box — flips on every strict moving-average cross), this machine keys off **price-level** events: a swept 20-bar extreme plus a reversal close, age-gated so fresh extremes never qualify. Unlike pool breakout records (which follow the break), this fades it. The pool contains **zero** Turtle-Soup / Raschke / NR / Holy-Grail records at the pre-write snapshot — this is a fresh signal family, not a parameter variant of anything admitted. Live-window rate is ~208 post-warmup predicate bars per 1,500 4h bars (92 bull-leg / 116 bear-leg), with 30 of 94 closes coming from opposite-setup reversals — the fade-and-reverse character is structural, not tuned.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 4-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` for signals/anchors/closes, `H[t]`/`L[t]` for sweep/box-touch legs, `O[t]` for fills. A bar with missing/nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals. All constants are source-default literals.

- **Rolling extremes (causal, per-bar, Pine-faithful):** `pH[t]=max(H[t-20..t-1])`, `pL[t]=min(L[t-20..t-1])`, `pH1[t]=max(H[t-21..t-2])`, `pL1[t]=min(L[t-21..t-2])`; age of the most-recent extreme inside the prior window (Pine `highestbars/lowestbars` idiom): `ageH[t]=(t-1-mH)+1` where `mH` is the last index attaining the window max (mirrored `ageL`); defined only for `t ≥ 21`.
- **Predicates (actionable only t ≥ 100, at bar `t`'s close):** `bull[t] = (ageL≥4 and L[t]<pL[t] and C[t]>pL[t]) or (L[t-1]<pL1[t] and C[t]>pL1[t])`; `bear[t] = (ageH≥4 and H[t]>pH[t] and C[t]<pH[t]) or (H[t-1]>pH1[t] and C[t]<pH1[t])`. Pre-warmup bars flat by record rule; every na/degenerate bar is an explicit neither-fire hold.
- **Latched box (researcher-designed, fixed at fill-average `A`, never moved):** long `SL=A×0.98`, `TP=A×1.04`; short mirrored `SL=A×1.02`, `TP=A×0.96`.
- **Resolution (explicit researcher pin):** entries fill next-bar-open MARKET; each held bar `v` (fill bar +1 onward) evaluates at its close in code order — opposite setup first (reversal dominates, old box dies; tie bars keep box legs only), else SL-touch, else TP-touch (`H/L` vs latched levels); SL+TP co-fire is one flat close (stop wins). Flat with both legs firing is an explicit neither-fire hold (researcher tie-break — co-fires are constructible on wide-range bars, verified on tape). Single position, no adds: same-side refire is a no-op.

## Required data / Gate 6 causality

**Warmup:** minimum 100 contiguous valid completed 4h bars; covers the 20-bar structural scale plus the [2]-offset older window and an 80-bar researcher margin for extreme-age convergence (rolling windows are defined from bar 1 — the margin renders seeding immaterial post-warmup, disclosed). No warmup-bar trades; pre-warmup flat by record rule.

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `4h` is a carried `INTERVALS` entry `14400` — byte-verified at the pin this cycle; row[0] open-time parsing, 4h-boundary alignment verified live this cycle). Bars become available no earlier than `T[t]+14400s`. All decisions use completed bars only (researcher once-per-bar pin answering the source's own close-warning; `alert.freq_once_per_bar_close` + `isconfirmed` logs show the source's close-decided intent, disclosed); fills at next-bar open; SL/TP legs are close-decided against completed-bar `H/L` with next-open fills (research-model convention, disclosed). No incomplete bar, future extremum, repainted graphic, MTF call, session template, gap state, or same-bar intrabar signal. Single OHLC feed — no second data dependency. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `BacktestingEngineBase.run_backtesting` + `determine_executor_actions` in controller bases, `OrderExecutorSimulator` class byte-present in `backtesting/executors_simulator/order_executor_simulator.py`, `INTERVALS "4h": 14400` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT futures venue, one 4h OHLCV stream (single-feed design — no MTF, no session, no second symbol, no gap feed). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the four sweep-fade predicates with strict age semantics, the new-position avg-price 2%/4% latch, and the entries-dominate stop-first tie-hold state pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes `position_action = CLOSE` (SL, TP, and reversal legs all close-then-act per the pin), `amount = Decimal("0.01")` (≈783.1 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the source timing class. No fill executes if its required future bar is absent. Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-size 1× single-position with no compounding and no abort rule (disclosed).
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin; slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 4h holds routinely span `00:00`/`08:00`/`16:00 UTC` stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided box legs and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 506-line fence ships the complete sweep-fade construction: the 20-bar lookback with the 4-bar age gate at source defaults, the exact classic and +1 predicates with strict inequalities, the Bull/Bear polarity with stated fade expectations, and the close-decided alert/log intent. It ships no orders, no sizing, no exits, and no performance figure of any kind — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/latch/state pipeline (Pine-faithful extremes, strict age gate, avg-price latch, code-order entries-dominate stop-first tie-hold resolution, next-open fills), run in scratch (never committed): `SELF-CHECK OK` — logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS, double-run identical):** MICRO-SL tape prints 2 post-warmup bull legs driving 1 open / 1 SL close ending flat (digest `09ac57bbf3dedbb6`); MICRO-TP tape prints 2 bear legs driving 1 open / 1 TP close ending flat (digest `f493571810b547b9`); MICRO-REV tape prints 2 bull / 2 bear legs driving 2 opens / 1 reversal close ending short-held (digest `e0000e9bbdba202e`); MICRO-TIE tape prints 2 bull / 2 bear legs with a both-legs sweep bar driving 0 opens ending flat (digest `3c3a0a2e11ab9d9e`).

**Live-exchange microstructure probes (this cycle, futures 4h klines, 1,500 completed bars 2026-02-25→2026-11-01, last close 78,313.0):** 92 post-warmup `LE` and 116 post-warmup `SE` predicate bars drive 95 state-machine opens / 94 closes (55 SL-touch / 9 TP-touch, 30 reversals) ending LONG (digest `ece893126b1ca2b3`); sub-window bars 300–999 print 39 `LE` / 50 `SE` driving 39 opens / 38 closes (23 SL / 2 TP / 13 reversals) ending SHORT, same honest cut (digest `eb38bf990aff7de9`). 0.01 BTC ≈ 783.1 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

At the pre-write snapshot `main@c6d540f8`, the root Git tree contained **513** strategy Markdown records (515 files minus two READMEs). Exact-identity working-tree searches for `turtle` / `raschke` / `soup` / `nr4` / `nr7` / `holy-grail` / `holygrail` / `8020` / `odup` / `b6d473b8` return **zero** records. Fifteen open `research/*` PRs were inspected by per-PR title/head — no collision (nearest open lanes are EMA-stack-RSI, OneTrend, dual-MACD, volume-dip, supertrend, Heracles, ClucMay, AdxSmas, CCI, 2yMA, SSL, Chandelier, Gaussian, Larry-Williams — none a sweep-fade). Closed-PR scan surfaces no member of this family. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen sweep-fade box book against (a) no-box twins (pure setup-to-opposite-setup reversal — isolating the percent box), (b) classic-only twins (TS legs without +1 — isolating the delayed leg; researcher variation), (c) 1%/2% and 3%/6% box twins (isolating the 2R choice; researcher variation), and (d) static-level twins keyed off fixed 20-bar extremes without the age gate (isolating the 4-bar freshness rule; researcher variation — never attributed to source). Check event rate, SL/TP/reversal attribution, hold-time distribution, warmup sensitivity (100 vs 200), and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 4h** only. Stated plainly: the machine needs completed-bar OHLC plus the 100-bar admission warmup (lookback-bound); the entries are 20-bar extreme sweep-fades with a live-window rate of ~208 predicate bars per 1,500 4h bars; the exits are a researcher-latched 2%/4% avg-price box with reversal dominance and tie-hold; 4h slippage plus funding apply to every held span. The ported legs carry no session, calendar, or gap dependence (the file's session-sensitive gap leg is fenced out, disclosed), so 24/7 crypto continuous trading introduces no Year-2024-style anchor or session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The indicator→strategy promotion, market/timeframe pin (source is chart-agnostic), sizing, cash, leverage, warmup, display drop, constant fence, 0.05% research fee, close-decided next-open resolution, tie-hold, and once-per-bar evaluation are researcher pins, never attributed to the source. The nine non-ported pattern families (80-20, IB, FIB, OD, NR4/NR7, gaps, HG) are fenced out — enabling any of them creates a different unpinned rule. The repo ships no LICENSE — this record cites short literal lines only and reproduces no source block; research-only use asserted, no commercial claim. Pine rolling-window seeding is adopted explicitly with an 80-bar convergence margin inside the 100 warmup. Entries read completed-bar closes only; SL/TP legs are close-decided against completed-bar H/L with next-open fills (research-model convention, disclosed). Probe windows end holding (LONG full-window, SHORT sub-window) — no invented fills. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/TradersPost/pinescript-agents/blob/ebc382f88b6103fcda2569fe666a38b00fe714c5/projects/raschke-patterns.pine (commit `ebc382f88b6103fcda2569fe666a38b00fe714c5`, 2026-07-23, still HEAD verified live 2026-11-02; blob `b6d473b8b7f6bfb3538471f5a786cd3c228778db`; Pine v6, 506 lines / 27,536 bytes; raw sha256 `92287b6fde409d57539878b07a5b615b0d926abf9b4cfcb0ca17ae720a8f08ce` verified live 2026-11-02; no LICENSE — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `TRADING`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 4h microstructure probes (1,500 completed bars 2026-02-25→2026-11-01, 92 LE / 116 SE → 95 opens / 94 closes, plant digests `09ac57bb`/`f4935718`/`e0000e9b`/`3c3a0a2e`, window digests `ece893126b1ca2b3`/`eb38bf990aff7de9`), fetched live 2026-11-02
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): naked-cross `github-traderspost-ema921-naked-percent-box-two-sided-btcusdt-4h-2026-11-02.md`; Q-Trend-KVO confluence https://github.com/HCH725/alpha-strategy-research/pull/697; dual-Kalman cross `github-indie-kalman-trend-levels-percent-box-two-sided-btcusdt-4h-2026-11-02.md`
- Pine reference: v6 causal rolling windows (`ta.highest/lowest` with `[1]`/`[2]` offsets, `highestbars/lowestbars` age idiom), `alert.freq_once_per_bar_close`, `barstate.isconfirmed` log gating
