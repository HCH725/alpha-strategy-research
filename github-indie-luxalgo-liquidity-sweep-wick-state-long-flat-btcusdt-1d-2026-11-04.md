---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: LuxAlgo liquidity-sweep wick-state long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-08
sources:
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Liquidity%20Sweeps/Liquidity%20Sweeps.pinescript5
  - https://indie-script.github.io/indicators/Liquidity%20Sweeps/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Liquidity-sweep wick-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`64f0494a84273138b2e6a0f15821b18ba1616056`** (2026-10-08, `Add 60 community MIT/MPL indicators from TakeProfit with guides`, verified via GitHub API this cycle), file **`indicators/Liquidity Sweeps/Liquidity Sweeps.pinescript5`**, blob `085e3ec5cba464b0c48fcc41757d1e1eba560cfa`, **5,797 bytes / 160 lines**, `indicator('Liquidity Sweeps [LuxAlgo]', ..., overlay=true)` — an indicator, not a strategy. Header license: CC BY-NC-SA 4.0, © LuxAlgo. Raw bytes re-downloaded this cycle are byte-identical (second download `cmp`-matched); `git hash-object` of the working copy reproduces the API blob SHA exactly. Port guide confirms LuxAlgo authorship, Pine Script v5 original, default option `Only Wicks`, and 1:1 logic port of swing pivots, wick sweeps, outbreaks/retests and extending sweep boxes.

**Order-affecting logic read verbatim (code governs; the study ships no orders):** swing pivots `ph = ta.pivothigh(len, len)` / `pl = ta.pivotlow(len, len)` at default `len = input.int(5, 'Swings')`, registered on confirmation bars as `piv.new(ph, n - len, ...)` (level price fixed, located five bars back); mode flags `oW = opt == 'Only Wicks'` (default true), `oO`, `WO`. At default mode the outbreak/retest legs are dead code (`if not oW` false, `tak` unsettable). Wick sweep of a live high pivot: `high > prc and close < prc` (first touch only via `wic` flag, draws bear box); mitigation of a high pivot: `close > prc`. Mirrored for lows: sweep on `low < prc and close > prc` (bull box); mitigation on `close < prc`. Stale/removal bound `n - bix > 2000 or mit or tak`. Sweep boxes extend right (`extend`, `maxB = 300`) until the close leaves them — display only.

**Pine-block census (160-line fence):** 1 `indicator(`; 0 `strategy.*` of any kind; 10 `input(` (length, option, six colors, extend, max-bars); 0 `security(`; 0 `request.*`; 0 `volume`; 2 `ta.pivot`; 4 drawing new-calls (`line.new`/`box.new`, incl. the display-only `lnDot` dotted mark drawn to `bar_index + 3`, never a signal); 0 `alertcondition(`.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is a display indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of first-touch bullish wick sweeps to long-flat entries/exits on completed bars (disclosed promotion); (2) long-only pin with the short side explicitly disabled (bearish sweeps while flat are deliberate omissions, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at the cycle's last completed close 76,816.00 on 2026-11-02, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 250-bar warmup with pre-warmup bars flat (structural scale is 11 bars — 5+5 pivot formation plus confirmation — plus researcher transient/array-depth margin); (6) display drop (sweep boxes, pivot lines, dotted marks, extend/maxB machinery, all colors, the outbreak/retest option branches); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation with an explicit same-bar bull+bear conflict precedence and no re-anchor while LONG (researcher pins, disclosed).

**Immutable derivative identity:** `GH:Indie-script-64f0494|luxalgo-liqsweep_len5-wick-only_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup250|2026-11-04`. Changing any formula, length, mode, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@5f5e2819` (546 root strategy records, READMEs excluded; this file is the 547th). Case-insensitive content search for `luxalgo` returns exactly one hit anywhere on base `main` — an unrelated endpoint-envelope record's passing mention, zero dedicated LuxAlgo records and zero liquidity-sweep-indicator records by filename or content. No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors, all sweep-flavored: different source file/math/mode vs `tradingview-pridarasx-turtle-soup-onebar-confirm-long-flat-btcusdt-1d` (Pridarasx page, no pinned Pine; fixed 20-bar rolling extremes, not len-5/5 fractal pivots; entry only on the *next* bar's confirmation break, never the sweep bar; 0.001 BTC close-market fills; 30-bar warmup — extreme definition, trigger timing, and fills all differ); different data dependency/market/risk vs `tradingview-heatsweep-volumeprofile-sweep-poc-bracket-two-sided-btcusdt-1h` (100-bar volume profile with POC, heat ≥ 0.25 and rvol > 1.0 gates, ATR brackets, two-sided futures 1h — volume-profile machine, not a pivot-wick machine; this rule reads no volume); different geometry vs `wick-reversal-hammer-shooting-star-long-flat-btcusdt-1d` (single-candle wick/body proportion rule with no reference level at all). No duplicate, paraphrase, or trivial parameter variant. Same-commit screenings rejected before writing: 2-Period RSI Strategy, RSI LacQuanTeu Pub, Classic SlingShot, Band Trend, Median Algorithm, Trend Impulse Channels, Ultra Trend Alerts, Pivot Ribbon BLC, Trendlines with Breaks, UFF, VD binary pro 3 (no Pine original pinned at this commit — `.indie5` only — rejected as provenance-insufficient, same fence as prior-cycle EWO/TonyUX); Market Facilitation Index Squat Bars (same fence); Optimized Trend Tracker (identical OTT support-line ratchet math already ported on `main`, rejected as already-ported); Volume Orderbook (POC/profile dependency needs representative capability validation not owed by this run — left for a future cycle, never silently simplified).

## Economic mechanism

### Source-reported

Liquidity Sweeps [LuxAlgo] (per the port guide): swing highs and lows that are swept by a wick, broken or retested, drawn as boxes — a wick pierces the level and the candle closes back (sweep), a close crosses the level (outbreak), or price retests a broken level. The author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool level machines that fade fixed rolling extremes (turtle-soup's 20-bar Donchian band) and unlike pool profile machines that gate on volume concentration (heatsweep's POC/heat/rvol stack), this machine watches *confirmed fractal structure* — len-5/5 swing pivots that only exist after a five-bar confirmation delay — and trades the *first* wick-through-and-close-back as the event, with the swept level itself as the invalidation line: a close through the anchor kills the trade the same way it kills the pivot in source. Unlike pool cross machines there is no penetration event to catch late; unlike pool slope/state machines there is no regime to hold — there is only a sweep to enter on and a mitigation to exit on. The bet, as derived, is purely that this fractal-sweep-then-mitigate alternation ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series (pinned): `O/H/L/C[t]` (the source reads bar OHLC only; a heikin-ashi-sourced twin is a different, unpinned rule). No volume read exists in this rule.
- R3 — Pivot registration (source formulas, pinned): `PH[t] = ta.pivothigh(5,5)`, `PL[t] = ta.pivotlow(5,5)` evaluated on completed bar `t` (non-na on confirmation bars only); newly confirmed pivots register before evaluation on the same bar with price `P` and location `t-5`, mirroring source order (register-then-test). Pre-registration bars are never tested against a pivot — a sweep that completes before its pivot confirms is missed by rule, source-faithfully (fenced in Negative evidence 3).
- R4 — Live set (source state, pinned): a registered pivot is live iff not mitigated and `t - bix <= 2000` (source stale bound); `brk`/`tak` are unsettable at the pinned default mode and never consulted.
- R5 — Bullish sweep event (source wick rule, pinned): for a live low pivot with `wic = false`, event iff `L[t] < P AND C[t] > P` (strict both sides; equality on either side is neither sweep nor mitigation — pinned source-faithful boundary, disclosed); firing sets `wic := true` (first touch only — a second pierce of the same pivot is an explicit no-op).
- R6 — Bearish sweep event (source wick rule, pinned): for a live high pivot with `wic = false`, event iff `H[t] > P AND C[t] < P`; firing sets `wic := true`.
- R7 — Mitigation (source rule, pinned): a live low pivot dies when `C[t] < P`; a live high pivot dies when `C[t] > P`. Sweep and mitigation are mutually exclusive on one bar by construction (opposite close requirements) — no same-bar conflict exists inside either test.
- R8 — State (promoted machine, adaptation 1): `LONG`/`FLAT` single-unit book anchored to the swept pivot price `S`. If FLAT and a bullish sweep event fires → request LONG at the next open anchored at `S = P`. If LONG → exit the whole book at the next open when either (a) `C[t] < S` (anchor mitigated, source rule R7), or (b) a bearish sweep event fires on any live high pivot. Bearish sweeps while FLAT are explicit holds (short side disabled — adaptation 2). A fresh bullish sweep while LONG is an explicit no-op (no re-anchor, no add — pinned absence of pyramiding, not invented).
- R9 — Same-bar conflict precedence (adaptation 9, researcher pin): a bar firing both a bullish sweep (while LONG) and an exit trigger resolves exit-first at the next open, and that bar's bullish event may NOT re-enter on the same signal (re-entry waits for a fresh later bullish sweep). A bar firing both while FLAT enters LONG (bearish half ignored — short side disabled). Any other precedence is a different, unpinned rule.
- R10 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R11 — Position state: one 0.01-BTC spot unit max, long or flat, never short. Safety orders: explicitly none.
- R12 — Warmup and gaps: flat until 250 completed `1d` bars (structural scale is 11 bars — pivot formation plus confirmation — plus researcher transient/array-depth margin). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold.
- R13 — Invariant identifier: `GH:Indie-script-64f0494|luxalgo-liqsweep_len5-wick-only_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup250|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (fills, validity), `high`/`low` (sweep tests, validity), `close` (sweep tests, mitigation, validity). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close, with pivot registration preceding evaluation on the same bar (R3); fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 250 completed bars (structural). No repainting (`ta.pivot*` confirms with fixed delay; registered levels never move; `wic`/`mit` flags are append-only state), no negative shift, no future reference (the display-only `lnDot` future-draw to `bar_index + 3` is dropped with the display, never a signal), no full-sample normalization. Every live input is frozen at the decision close — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 on 2026-11-02 — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (the `dev-2.17.0` blob verified live this cycle at ancestor `8b0e067e` of local checkout `2dbc844`); `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/` (`backtesting_data_provider.py` over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. Pivot-array state is a plain precomputable signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned 160-line fence ships every adopted headline fact quoted in Provenance: the `len = input.int(5, 'Swings')` default, the three-way `options` input defaulting to `Only Wicks`, `ta.pivothigh(len, len)` / `ta.pivotlow(len, len)` registration at `n - len`, the strict wick inequalities for both sides, the close-through mitigation rules, the `wic` first-touch flag, the 2000-bar stale bound, and the `indicator(` (not strategy) declaration with `max_lines_count = max_boxes_count = 500`. It ships zero orders, zero sizing, zero exits, zero performance figures — none adopted; all trading semantics are researcher pins disclosed above. The pinned port guide additionally reports an independent drawing-level check of the Indie port against a re-implementation on 2,473 BTC 30-minute TradingView candles (15 Aug – 5 Oct 2026): the 55 newest sweeps matched on bar, direction and both price levels (55 of 55) at the default option — cited as source-reported port evidence, not as Hermes reproduction.

### Independently reproduced

Not independently reproduced. No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. No executable probe ran in this unattended cycle; logic assertions above are static readings of the pinned fence, fenced as Negative evidence 3–4 where implementations may differ.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, anchor-exit choice, conflict precedence, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. First-touch-subset fenced: only each pivot's first wick sweep governs; repeat pierces of the same pivot ship live in source display and stay dropped as signals — an implementation trading every touch prints a different event set, flagged as an implementation obligation, never silently interchangeable.
3. Confirmation-timing silence fenced: sweeps completing before their pivot's five-bar confirmation are untestable in source (pivot not yet registered) and stay missed here; an implementation back-testing unconfirmed pivots prints a different, non-source-faithful event set — flagged as an implementation obligation, not strategy behavior.
4. Equality/FP silence fenced: strict inequalities decide everything — exact level touches neither sweep nor mitigate; on degenerate flat input, floating-point pivot comparisons may disagree across implementations — fenced as an implementation obligation, never a strategy claim; live tape carries no constant stretches so no live event turns on it.
5. Outbreak/retest boundary fenced: the `Only Outbreaks & Retest` and combined branches are never used here — any record using `brk`/`tak` transitions is a different, unpinned claim; the companion display machinery (`extend`, `maxB`, boxes, pivot lines, future-drawn dotted marks) changes no event in this derivative.
6. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
7. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (wick promotion, long-only pin, fixed sizing, disabled risk, 250-bar warmup, display drop, 0.1% cost overlay, next-open fills, bar discipline with conflict precedence); the pivot math, lengths, inequalities, mode default, stale bound, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ta.pivot(5,5)` / first-touch wick-only sweeps / strict inequalities / anchor-mitigation-or-opposing-sweep exits / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 250-bar warmup are frozen.

- F1 — Structure relevance: a fixed-20-bar-extreme twin (same sweep/exit handling on rolling 20-bar highs/lows) must not improve net expectancy; fail ⇒ the fractal-pivot structure is decoration on generic extreme-sweeps.
- F2 — First-touch relevance: an every-touch twin (repeat pierces re-arm entries with the same rest) must not improve net expectancy; fail ⇒ the `wic` once-flag discards the better half of the flow.
- F3 — Exit relevance: a mitigation-only twin (anchor-break exits only, opposing sweeps ignored, same rest) must not improve net expectancy; fail ⇒ the opposing-sweep exit is decoration on anchor invalidation.
- F4 — Warmup relevance: a 400-bar-warmup twin must print the identical post-400 event set; fail ⇒ pivot-registration transients leak past the declared warmup.
- F5 — Conflict relevance: an exit-and-reenter twin (same-bar bull+bear resolves to flip rather than exit-and-wait, same rest) must not improve net expectancy; fail ⇒ the conflict precedence is decoration on sweep churn.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The source is a TradingView display indicator (CC BY-NC-SA 4.0, © LuxAlgo — cited, not copied); every trading semantic (sweep promotion, anchor exits, venue, sizing, warmup, no-box risk, next-open fills, cost overlay, conflict precedence) is a researcher adaptation disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- Pivot-confirmation timing and degenerate-input FP behavior are implementation-defined (Negative evidence 3–4); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (250) is a researcher margin over the 11-bar structural scale; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Liquidity%20Sweeps/Liquidity%20Sweeps.pinescript5 (canonical pinned source; commit `64f0494a84273138b2e6a0f15821b18ba1616056`, blob `085e3ec5cba464b0c48fcc41757d1e1eba560cfa`, 5,797 bytes / 160 lines, sha256 `466daad041cafc87ee0540219a889377872bb405fdf003bd8a25f35ab6c137f7`)
- https://indie-script.github.io/indicators/Liquidity%20Sweeps/ (port guide: LuxAlgo original, Pine v5, CC BY-NC-SA 4.0, wick-sweep/break/retest construction, default `Only Wicks`, 55/55 drawing-level port check)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (NOTIONAL minNotional 5.0, LOT_SIZE 0.00001/0.00001, PRICE_FILTER tickSize 0.01; last completed daily close 76,816.00 on 2026-11-02)
