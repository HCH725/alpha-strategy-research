---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Indie Ripster EMA-clouds triple-state long-flat on BTCUSDT 1d bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Ripster%20EMA%20Clouds/Ripster%20EMA%20Clouds.pinescript4
  - https://indie-script.github.io/indicators/Ripster%20EMA%20Clouds/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ripster EMA-clouds triple-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`64f0494a84273138b2e6a0f15821b18ba1616056`** (2026-10-08, `Add 60 community MIT/MPL indicators from TakeProfit with guides`, verified via GitHub API this cycle), file **`indicators/Ripster EMA Clouds/Ripster EMA Clouds.pinescript4`**, blob `a50d6df4fdac44e3d6df8d04e64e9d9b99b9880e`, **5,594 bytes / 215 lines**, `study("Ripster EMA Clouds", overlay=true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `c3bdba3a4577b24f6833be730d9a96438cbd7fef62aac4e6b6e596adb05d21c7`, byte-identical to the working copy (blob base64 decoded and `cmp`-matched). Origin: ripster47's free TradingView community script Ripster EMA Clouds (the port guide confirms ripster47 authorship, MPL-2.0 license, five short/long MA pairs with greenish fill when short MA is above-or-equal and reddish when below).

**Order-affecting logic read verbatim (code governs; the study ships no orders):** `matype = input("EMA", options=["EMA","SMA"])`; ten lengths `8/9/5/12/34/50/72/89/180/200`; `src = input(hl2)`; `ma_offset = input(0)`; `f_ma(malen)` selects `ema(src,malen)` at the default; `htf_ma1..10 = f_ma(ma_len1..10)` (same-TF despite the `htf_` names — the commented `res` input never ships, no `security(` exists); `mashort1..5/malong1..5` alias the ten legs; cloud colors `mashort >= malong ? green-ish : red-ish` on all five pairs (exact equality prints green); `ema1/ema2/ema3 = input(true)`, `ema4/ema5 = input(false)`; `showLine = input(false)`; `showlong/showshort = input(false)`; `emacloudleading = input(0)`.

**Pine-block census (215-line fence):** 1 `study(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 22 live `input(` (matype / ten lengths / hl2 / offset 0 / showlong / showshort / showLine / ema1–ema5 / leading 0; four more `input(` lines are comments); 0 `security(`; 0 `request.*`; 0 `volume`; 12 `plot(` legs (display-only, dropped, disclosed); 5 `fill(` (display-only, dropped, disclosed); 0 `alertcondition(`.

**Structural facts carried over exactly:** (a) five short/long MA pairs on one source, never a cross of two different indicator families; (b) per-cloud ordinal state — each predicate compares a short leg with its own long leg (`>=`, equality bullish); (c) default-enabled triple is clouds 1–3 only (`8/9`, `5/12`, `34/50`; clouds 4–5 ship disabled); (d) no MTF at the default, no session/timezone, no intrabar semantics, no volume read anywhere (every predicate is `hl2`-derived); (e) zero offsets (`ma_offset=0`, `emacloudleading=0`) so no displacement.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the default-enabled triple-cloud conjunction to long-flat entries/exits on completed bars (`C1 AND C2 AND C3` → LONG, anything else → FLAT, disclosed promotion); (2) long-only pin with the short side explicitly disabled (the construction is signed; the all-bearish leg is a deliberate omission, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at probe last completed close 76,816.00, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 250-bar warmup with pre-warmup bars flat (structural scale is 50 bars — longest enabled EMA seed-full at bar 50 — plus researcher transient margin); (6) display drop (all twelve plot legs, all five fills, line/rise-fall coloring, both disabled clouds, both alarm flags); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (no confirmed-close flag ships in source, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-64f0494|ripster-emaclouds_8-9_5-12_34-50_triple-AND_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup250|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@94f45da4` (544 root strategy records on base `main`, READMEs excluded; this file is the 545th). Case-insensitive content searches for `ripster`, `emacloudleading`, `cloudcolour` return zero hits anywhere on base `main`; the filename neighbors below were surfaced by generic cloud search and are distinguished on five axes. No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number/branch — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors: different source file and math vs `ema-cloud-7-20-trend` (FMZ 363835 close-vs-EMA 7/20 alignment, two-sided — close against averages, not average-against-average triple); `fmz-dual-ema-cloud-donchian-stop-breakout` (dual cloud plus Donchian stop on 1m, two-sided — a Donchian dependency absent here); `hull-ema-crossover-reversal` (HMA(5)-vs-EMA(5) single cross — Hull math, one pair, not three); `fmz-hull-pac-linreg-swing` (Hull+PAC+linreg confluence — different family); `ema-20-50-cross` (single 20/50 cross event — one pair, different lengths/source) — no duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Ripster EMA Clouds (via ripster47, per the port guide): five short/long moving-average pairs on one source with colored fills between them to visualize trend strength and direction — greenish when the short leg sits above-or-equal, reddish when below — so multiple trend scales are visible at a glance. The author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool cross machines (single fast/slow penetration events that fire on one crossing) and unlike pool level machines (close-vs-average alignment that requires price to sit outside a band), this machine watches *three* average-vs-average orderings at once and trades only their conjunction — the trigger is whether the 8/9, 5/12, and 34/50 EMA pairs all agree short-over-long on `hl2`, not whether price sits above any average or whether any single pair crossed this bar. Unlike pool slope machines (one line against its own past), no self-displacement exists here — every comparison is contemporaneous between two live legs. The bet, as derived, is purely that this triple-scale agreement ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series (pinned): `hl2[t] = (high[t]+low[t])/2` (the source default; a close-sourced twin is a different, unpinned rule).
- R3 — EMA legs (source formulas, pinned): `E8[t]=ema(hl2,8)`, `E9[t]=ema(hl2,9)`, `E5[t]=ema(hl2,5)`, `E12[t]=ema(hl2,12)`, `E34[t]=ema(hl2,34)`, `E50[t]=ema(hl2,50)` (Pine-built-in trailing EMA reading — na until each leg's first full window under the SMA-seed reading; seeds absorbed by warmup, disclosed researcher reading).
- R4 — Cloud states (source predicates, pinned): `C1[t]` iff `E8[t] >= E9[t]`; `C2[t]` iff `E5[t] >= E12[t]`; `C3[t]` iff `E34[t] >= E50[t]` (exact equality is green/bullish in source and carried as bullish, never bearish — pinned source-faithful reading, disclosed).
- R5 — Display drop (adaptation 6): all twelve `plot(` legs, all five `fill(`, rise/fall line coloring, disabled clouds 4–5, and both alarm flags never enter any predicate.
- R6 — State (promoted predicate, adaptation 1): `LONG[t]` iff `C1[t] AND C2[t] AND C3[t]`; `FLAT[t]` otherwise (covers any-bearish, na seeds — carried as an explicit rule, not as verified live behavior).
- R7 — Entry/exit timing (adaptation 8): signal-bar-close decision; fills at the next bar's open market. Guards with single-unit book: flat→LONG fills on fresh flips only; LONG→FLAT closes the whole book at the next open; same-side refire is an explicit no-op. After any exit the next qualifying flip may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R8 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R9 — Position state: one 0.01-BTC spot unit max, long or flat, never short (short side explicitly disabled — adaptation 2). Safety orders: explicitly none.
- R10 — Warmup and gaps: flat until 250 completed `1d` bars (structural scale is 50 bars — longest enabled EMA seed-full at bar 50 — plus researcher transient margin; probe shows first-eligible LONG behavior from the first post-warmup stretch with 0 na remnants post-warmup). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold (volume never read: no volume-validity leg exists in this rule).
- R11 — Invariant identifier: `GH:Indie-script-64f0494|ripster-emaclouds_8-9_5-12_34-50_triple-AND_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup250|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (fills, validity), `high`/`low` (hl2 source and validity), `close` (validity only — no predicate reads `close`). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 250 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing recursion; all live inputs are frozen). All three predicates compare contemporaneous confirmed legs — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (raw `hummingbot/VERSION` at `8b0e067e` reads `dev-2.17.0`, verified live this cycle); `8b0e067e` is a verified ancestor of the local checkout `2dbc844`; `hummingbot/strategy_v2/controllers/controller_base.py:465` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/` (`BacktestingDataProvider` over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. No new execution primitive, no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned 215-line fence ships every adopted headline fact quoted in Provenance: the EMA/SMA switch, the ten lengths, the `hl2` source, the zero offsets, the `ema1–ema5` enable flags, the `>=` cloud-color predicates with equality on the bullish side, and the twelve display plots plus five fills. It ships zero orders, zero sizing, zero exits, and zero performance figures — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the disclosed EMA re-implementation (8/9, 5/12, 34/50 windows on hl2, triple-AND state, equality-bullish, na seeds, LONG-iff-all-agree state, next-open fills, 250-bar warmup), run in scratch (never committed):

- Live microstructure (Binance spot 1d klines fetched live this cycle, 3,365 completed bars 2017-08-17→2026-11-02, verified contiguous at 86400s steps with the still-forming current bar excluded by close-time, last completed close 76,816.00): 1,097 LONG / 2,018 FLAT post-warmup bars driving 58 books, holds 1–87 bars, 0 na bars post-warmup, 0 nonfinite closes (digest `d78031597774f588`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 768.16 USDT notional at window close.
- Flat-tape branch probe (400 constant bars): 0/150 post-warmup LONG — see Negative evidence 3 for the honest FP-dust mechanism; carried as implementation-defined degenerate behavior, never a strategy claim.
- Predicate-necessity probes: monotonic +0.1%/bar tape goes LONG from the first post-warmup bar (150/150); monotonic-down tape sits all-bearish → 0 LONG under the long-only pin; ±1 alternating tape prints 75/150 LONG — the triple conjunction does not absorb tight chop the way single-line smoothers do (disclosed decoration boundary, carried into F1).
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. Cloud-subset fenced: only default-enabled clouds 1–3 govern the book; clouds 4–5 (`72/89`, `180/200`) ship disabled and stay disabled — an implementation enabling them prints a different event set, flagged as an implementation obligation, never silently interchangeable.
3. Equality/FP silence fenced: exact `short == long` prints green/bullish in source; on mathematically constant input the Python probe prints FLAT because `E34` rounds to `99.99999999999997` against `100.0` — degenerate-constant behavior is floating-point-implementation-defined (Pine's own rounding may differ) and is fenced as an implementation obligation, never a strategy claim; live tape carries no constant stretches so no live event turns on it.
4. EMA-seeding silence fenced: na→available ramp transients (longest seed-full from bar index 49) are absorbed by the 250-bar warmup; an implementation seeding EMAs differently must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
5. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
6. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (triple-AND promotion, long-only pin, fixed sizing, disabled risk, 250-bar warmup, display drop, 0.1% cost overlay, next-open fills, once-per-bar evaluation); the EMA math, lengths, source, constants, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `8/9 + 5/12 + 34/50` windows / `hl2` source / triple-AND / LONG-iff-all-agree / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 250-bar warmup are frozen.

- F1 — Conjunction relevance: a single-cloud-1 twin (8/9 only, same rest) must not improve net expectancy; fail ⇒ the triple conjunction is decoration on the fastest pair (the alternating-tape 75/150 LONG probe is the standing falsifier baseline).
- F2 — Direction relevance: a two-sided twin (all-bearish → SHORT with mirrored next-open handling, same rest) must not improve net expectancy; fail ⇒ the long-only pin discards the better half of the state.
- F3 — Source relevance: a close-sourced twin (same six lengths on `close`, same rest) must not improve net expectancy; fail ⇒ the `hl2` pin carries no edge over closes.
- F4 — Warmup relevance: a 400-bar-warmup twin must print the identical post-400 event set; fail ⇒ seeding transients leak past the declared warmup.
- F5 — State relevance: a hold-time twin (flat exits delayed one extra bar, same entries) must not improve net expectancy; fail ⇒ the flip-close timing is decoration on the triple state.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The source is a TradingView display indicator; every trading semantic (state promotion, venue, sizing, warmup, no-box risk, next-open fills, cost overlay, bar discipline) is a researcher adaptation disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- EMA seeding and degenerate-constant FP behavior are implementation-defined (Negative evidence 3–4); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (250) is a researcher margin over the 50-bar structural scale; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Ripster%20EMA%20Clouds/Ripster%20EMA%20Clouds.pinescript4 (canonical pinned source; commit `64f0494a84273138b2e6a0f15821b18ba1616056`, blob `a50d6df4fdac44e3d6df8d04e64e9d9b99b9880e`, 5,594 bytes / 215 lines, sha256 `c3bdba3a4577b24f6833be730d9a96438cbd7fef62aac4e6b6e596adb05d21c7`)
- https://indie-script.github.io/indicators/Ripster%20EMA%20Clouds/ (port guide: ripster47 original, MPL-2.0, five-pair construction, above-or-equal green rule)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (NOTIONAL minNotional 5.0, LOT_SIZE 0.00001/0.00001, PRICE_FILTER tickSize 0.01; 3,365 contiguous completed bars 2017-08-17→2026-11-02, last close 76,816.00)
