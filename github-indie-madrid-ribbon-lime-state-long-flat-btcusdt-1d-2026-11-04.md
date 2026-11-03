---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Indie Madrid ribbon fastest-leg LIME-state long-flat on BTCUSDT 1d bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Madrid%20Moving%20Average%20Ribbon/Madrid%20Moving%20Average%20Ribbon.pinescript4
  - https://indie-script.github.io/indicators/Madrid%20Moving%20Average%20Ribbon/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Madrid ribbon fastest-leg LIME-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`64f0494a84273138b2e6a0f15821b18ba1616056`** (2026-10-08, `Add 60 community MIT/MPL indicators from TakeProfit with guides`, verified via GitHub API this cycle), file **`indicators/Madrid Moving Average Ribbon/Madrid Moving Average Ribbon.pinescript4`**, blob `865cf22a7db5838b44cb820fe95d386ead73fd55`, **9,455 bytes / 327 lines**, `study("Madrid Moving Average Ribbon", shorttitle="Madrid Ribbon", overlay=true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `9290acc4bb2ec4ea55001b7903d0174788a21f9e32e91d5f9ef3c9a48f4075c8`, byte-identical to the working copy (second download `cmp`-matched). Origin: Madrid's TradingView community script Madrid Moving Average Ribbon (the port guide confirms Madrid authorship, MPL-2.0 license, 18 moving averages in periods 5–90 with dynamic coloring against a 100-period reference).

**Order-affecting logic read verbatim (code governs; the study ships no orders):** `src = close`; eighteen legs `ma05..ma90` in steps of 5 plus unplotted reference `ma100`, `i_exp = input(true, "Expnential MA")` selecting `ema(src, N)` at the default (SMA twin unpinned); color helper `maColor(_ma, _maRef)` with `diffMA = change(_ma)` and `macol = diffMA>=0 and _ma>_maRef ? LIME : diffMA<0 and _ma>_maRef ? MAROON : diffMA<=0 and _ma<_maRef ? RUBI : diffMA>=0 and _ma<_maRef ? GREEN : GRAY`; all eighteen `plot(` legs call `maColor(maXX, ma100)`; `ma05`/`ma90` drawn `linewidth=3` for emphasis. Author header semantics, quoted: `Lime : Uptrend. Long trading` / `Green : Reentry (buy the dip) or downtrend reversal warning` / `Red : Downtrend. Short trading` / `Maroon : Short Reentry (sell the peak) or uptrend reversal warning`.

**Pine-block census (327-line fence):** 1 `study(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 2 live `input(` (`i_exp` exponential switch plus one decorative title separator); 0 `security(`; 0 `request.*`; 0 `volume`; 18 `plot(` legs (seventeen dropped, disclosed); 0 `alertcondition(`.

**MMARB answer (prior-screening rebuttal, fenced):** the author header references a companion MMARB bar study "to best determine if this is a reentry point or a trend reversal" — that companion is **not** in the pinned file and is never adopted here. A prior Scout pre-filter rejected Madrid as "missing MMARB leg"; this record answers that rejection by construction: the promoted rule uses only the fastest leg's LIME predicate (`Lime : Uptrend. Long trading`, quoted above) and never uses reentry/reversal distinctions, so no MMARB input exists anywhere in the rule. Reproducing the author's full discretionary trading system would need MMARB and stays out of scope (fenced in Negative evidence 5, never claimed).

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the fastest-leg LIME print to long-flat entries/exits on completed bars (`LIME[ma05]` → LONG, anything else → FLAT, disclosed promotion); (2) long-only pin with the short side explicitly disabled (RED/MAROON legs are deliberate omissions, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at the cycle's last completed close 76,816.00, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 250-bar warmup with pre-warmup bars flat (structural scale is 100 bars — MA100 reference seed-full at bar 100 — plus researcher transient margin); (6) display drop (all seventeen non-fastest plot legs, line widths, all non-LIME colors, SMA twin, MMARB references); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (no confirmed-close flag ships in source, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-64f0494|madrid-ribbon_ema5-lime-vs-ema100_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup250|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@d6e00c6a` (545 root strategy records on base `main`, READMEs excluded; this file is the 546th). Case-insensitive content search for `madrid` returns exactly one hit anywhere on base `main` — the Hull-Suite record's screening note quoting its own prior rejection (`Madrid ribbon (missing MMARB leg, rejected in a prior cycle)`), a mention, not a record; zero dedicated Madrid records exist by filename or content. No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number/branch — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors: different source file and math vs `eterna-ema-ribbon-9-21-55` (three-leg 9/21/55 aligned-stack momentum, two-sided, ETHUSDT 4h — stack alignment, not slope-vs-reference color); `fmz-483047-ma-ribbon-macd` (ribbon plus MACD dual-cross dependency absent here, ETHUSDT 1h); `joat-atr-velocity-ribbon` (ATR velocity onset plus volume impulse absent here, 1h); `oberon-rsi4-macd3bar-sma-ribbon` (RSI/MACD confluence family, 1h); `ema-cloud-7-20-trend` (close-vs-average conjunctions, no reference-level color machine) — no duplicate, paraphrase, or trivial parameter variant. Same-commit screenings rejected before writing: OTT support-line cross (identical VAR(2)/1.4% ratchet math already ported on `main`, rejected as already-ported); Scalping PullBack Tool (hand-drawn mini-trendline entries, Heikin-Ashi option, sub-15min scalping intent — discretionary, rejected as non-deterministic); EWO Pro and TonyUX EMA Scalper (no Pine original pinned at this commit — `.indie5` only — rejected as provenance-insufficient).

## Economic mechanism

### Source-reported

Madrid Moving Average Ribbon (via Madrid, per the port guide): eighteen moving averages (periods 5–90) colored dynamically by direction and position relative to a 100-period reference — lime when a leg is rising and above the reference, maroon when falling but above, red when falling below, green when rising below — giving a fast visual read of trend direction and possible reversals. The author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool stack machines (several averages must line up in price order) and unlike pool cross machines (one penetration event fires on a single crossing bar), this machine watches *one* leg's signed state — whether the fastest EMA is flat-or-rising *and* above the slow reference — and holds that verdict as a regime, not an event: there is no cross to catch, only a color to keep. Unlike pool slope machines (one line against its own past), the verdict is two-dimensional — slope *and* level against MA100 — so a rising leg below the reference (GREEN) and a falling leg above it (MAROON) both print FLAT here. The bet, as derived, is purely that this fastest-leg lime regime ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series (pinned): `C[t] = close[t]` (the source `src = close`; an hl2/ohlc4-sourced twin is a different, unpinned rule).
- R3 — EMA legs (source formulas, pinned): `E5[t]=ema(C,5)`, `E100[t]=ema(C,100)` (Pine-built-in trailing EMAs at the default `i_exp=true`; SMA twin unpinned; seeds absorbed by warmup, disclosed researcher reading).
- R4 — LIME predicate (source color rule, pinned): `dE5[t] = E5[t]-E5[t-1]` (Pine `change`); `LIME[t]` iff `dE5[t] >= 0 AND E5[t] > E100[t]` (flat slope counts bullish via `>=`; exact level equality `E5 == E100` is NOT lime via strict `>` — pinned source-faithful boundaries, disclosed; na seeds print not-lime).
- R5 — Display drop (adaptation 6): the other seventeen legs, all line widths, MAROON/RED/GREEN/GRAY prints, the SMA switch, and every MMARB reference never enter any predicate.
- R6 — State (promoted predicate, adaptation 1): `LONG[t]` iff `LIME[t]`; `FLAT[t]` otherwise (covers MAROON/RED/GREEN prints and na seeds — carried as an explicit rule, not as verified live behavior).
- R7 — Entry/exit timing (adaptation 8): signal-bar-close decision; fills at the next bar's open market. Guards with single-unit book: flat→LONG fills on fresh flips only; LONG→FLAT closes the whole book at the next open; same-side refire is an explicit no-op. After any exit the next qualifying flip may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R8 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R9 — Position state: one 0.01-BTC spot unit max, long or flat, never short (short side explicitly disabled — adaptation 2). Safety orders: explicitly none.
- R10 — Warmup and gaps: flat until 250 completed `1d` bars (structural scale is 100 bars — MA100 reference seed-full at bar 100 — plus researcher transient margin). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold (volume never read: no volume-validity leg exists in this rule).
- R11 — Invariant identifier: `GH:Indie-script-64f0494|madrid-ribbon_ema5-lime-vs-ema100_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup250|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (fills, validity), `close` (signal source and validity), `high`/`low` (validity only — no predicate reads them). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 250 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (both legs are trailing recursions; all live inputs are frozen). The predicate compares a contemporaneous slope and level — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 on 2026-11-02 — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (the `dev-2.17.0` blob verified live this cycle at ancestor `8b0e067e`; local checkout `2dbc844` carries a later `aeacec9` working-tree bump to `2.17.0`, disclosed — engine-path semantics for this route unchanged); `8b0e067e` is a verified ancestor of `2dbc844`; `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/` (`BacktestingDataProvider` over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. No new execution primitive, no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned 327-line fence ships every adopted headline fact quoted in Provenance: the `src = close` assignment, the eighteen 5–90 legs plus MA100 reference, the default-true exponential switch, the `>=`/`>` LIME boundary inside `maColor`, all legs colored against `ma100`, the `Lime : Uptrend. Long trading` header verdict, and the eighteen display plots. It ships zero orders, zero sizing, zero exits, the MMARB companion study, and zero performance figures — none adopted; all trading semantics are researcher pins disclosed above.

### Independently reproduced

Not independently reproduced. No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. No executable probe ran in this unattended cycle; logic assertions above are static readings of the pinned fence, fenced as Negative evidence 3–4 where implementations may differ.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. Single-leg-subset fenced: only the fastest leg's LIME print governs the book; the other seventeen legs ship live in source and stay dropped — an implementation governing on unanimity or any other leg prints a different event set, flagged as an implementation obligation, never silently interchangeable.
3. Equality/FP silence fenced: flat-slope-above-reference prints lime in source while exact level equality does not; on mathematically constant input, floating-point EMA implementations may disagree at the `>` boundary — degenerate-constant behavior is implementation-defined (Pine's own rounding may differ) and is fenced as an implementation obligation, never a strategy claim; live tape carries no constant stretches so no live event turns on it.
4. EMA-seeding silence fenced: na→available ramp transients (reference seed-full from bar index 99) are absorbed by the 250-bar warmup; an implementation seeding EMAs differently must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
5. MMARB boundary fenced: the author's reentry-vs-reversal disambiguation needs the unpinned MMARB companion and is never used here — GREEN/MAROON ambiguity collapses to FLAT by rule, so the companion's absence changes no event in this derivative; any record claiming author-system fidelity without MMARB is a different, unpinned claim.
6. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
7. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (fastest-LIME promotion, long-only pin, fixed sizing, disabled risk, 250-bar warmup, display drop, 0.1% cost overlay, next-open fills, once-per-bar evaluation); the EMA math, lengths, source, constants, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `ema(C,5)` / `ema(C,100)` / `change>=0 AND E5>E100` / LONG-iff-LIME / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 250-bar warmup are frozen.

- F1 — Single-leg relevance: an all-18-unanimity twin (every leg LIME, same rest) must not improve net expectancy; fail ⇒ the fastest-leg promotion is decoration on ribbon agreement.
- F2 — Direction relevance: a two-sided twin (RED print → SHORT with mirrored next-open handling, same rest) must not improve net expectancy; fail ⇒ the long-only pin discards the better half of the state.
- F3 — Source relevance: an SMA twin (same lengths on SMA, same rest) must not improve net expectancy; fail ⇒ the exponential pin carries no edge over simple averages.
- F4 — Warmup relevance: a 400-bar-warmup twin must print the identical post-400 event set; fail ⇒ seeding transients leak past the declared warmup.
- F5 — State relevance: a hold-time twin (flat exits delayed one extra bar, same entries) must not improve net expectancy; fail ⇒ the flip-close timing is decoration on the lime regime.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The source is a TradingView display indicator; every trading semantic (state promotion, venue, sizing, warmup, no-box risk, next-open fills, cost overlay, bar discipline) is a researcher adaptation disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- EMA seeding and degenerate-constant FP behavior are implementation-defined (Negative evidence 3–4); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (250) is a researcher margin over the 100-bar structural scale; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Madrid%20Moving%20Average%20Ribbon/Madrid%20Moving%20Average%20Ribbon.pinescript4 (canonical pinned source; commit `64f0494a84273138b2e6a0f15821b18ba1616056`, blob `865cf22a7db5838b44cb820fe95d386ead73fd55`, 9,455 bytes / 327 lines, sha256 `9290acc4bb2ec4ea55001b7903d0174788a21f9e32e91d5f9ef3c9a48f4075c8`)
- https://indie-script.github.io/indicators/Madrid%20Moving%20Average%20Ribbon/ (port guide: Madrid original, MPL-2.0, eighteen-leg construction, lime-means-rising-and-above-reference rule)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (NOTIONAL minNotional 5.0, LOT_SIZE 0.00001/0.00001, PRICE_FILTER tickSize 0.01; last completed daily close 76,816.00 on 2026-11-02)
