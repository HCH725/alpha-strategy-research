---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: HyperTrend orientation flip long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-18
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/HyperTrend%20%5BLuxAlgo%5D.pine
  - https://www.tradingview.com/script/Bcufg8oX-HyperTrend-LuxAlgo/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# HyperTrend orientation flip — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical code (fetched live over HTTPS this cycle, immutable pin):** `hasnocool/tradingview-pine-scripts` commit **`69969aeaf271b2f7b5a7632a1bde43069a0cbe26`** (HEAD, committer hasnocool, 2024-09-18T10:39:02Z, verified via GitHub API this cycle), file **`HyperTrend [LuxAlgo].pine`**, blob `118578aacb18e1fbc4a193e0a04d22dfa3dfd4f6`, **3,869 bytes / 164 lines** (mirror scrape framing plus the 85-line numbered Pine block per the file's own `Expand (85 lines)` marker), `indicator("HyperTrend [LuxAlgo]", overlay = true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle are byte-identical (second download `cmp`-matched); `git hash-object` of the working copy reproduces the API blob SHA exactly. The header carries `// © LuxAlgo` and the Attribution-NonCommercial-ShareAlike 4.0 International notice (cited, not copied — same license posture as the already-merged LuxAlgo sweep record `github-indie-luxalgo-liquidity-sweep-wick-state-long-flat-btcusdt-1d-2026-11-04.md`).

**Upstream authorship (cited, not copied):** the file's own header names Script Name `HyperTrend [LuxAlgo]`, Author `LuxAlgo`, with the author's summary (a real-time estimate of an underlying linear trend; support/resistance extremities built from that estimate). The live TradingView original page `https://www.tradingview.com/script/Bcufg8oX-HyperTrend-LuxAlgo/` returned HTTP 200 this cycle, names LuxAlgo as author, marks the script open-source, publishes the three numeric defaults (Multiplicative Factor 5, Slope 14, Width % 80), states the direction convention (average sloping upward = uptrend, downward = downtrend), and states the average has no lookahead bias — all cited as source-reported prose, never adopted as crypto claims.

**Order-affecting logic read verbatim (the orientation state governs; the indicator ships no orders):** inputs pinned at defaults `mult = 5` (Multiplicative Factor), `slope = 14` (Slope), `width = 80 % → 0.8` (Width, display-only — it feeds only the plotted extremities, never `avg`/`os`/`hold`); the five Style inputs (two colors, `area` Gradient/Solid option, two area colors) are display-only. Seeds: `var float avg = close` (first-bar close), `var hold = 0.`, `var os = 1.` (long-biased seed, same seed posture as the merged Pivot Point SuperTrend record's `nz(Trend[1], 1)`). Threshold: `atr = nz(ta.atr(200)) * mult`, i.e. 5× the RMA-based ATR(200) (`ta.atr` is RMA-based per the v5 reference; `nz` maps the pre-200-bar `na` to 0). Average step: `avg := |close - avg| > atr ? mean(close, avg) : avg + os * (hold / mult / slope)` (Pine statement order: this line executes before the `os` reassignment, so it reads the pre-update `os`/`hold`, i.e. prior-bar values — fenced in Negative evidence 1). Orientation: `os := math.sign(avg - avg[1])` ∈ {1, −1, 0} (`math.sign(0) = 0` — fenced in Negative evidence 2). Hold: `hold := os != os[1] ? atr : hold` (re-armed to the full 5× threshold on every orientation flip). Extremities (display-only): `upper := avg + width * hold`, `lower := avg - width * hold`. Flip visualization (the indicator's own trend-change event): the average plot prints `na` exactly on bars where `os != os[1]`.

**Pine-block census (whole-file fence):** 1 `indicator(`; 0 `strategy.*` of any kind; 8 `input.*` (3 numeric + 5 style); 0 `alertcondition(`; 0 `plotshape(`; 3 `plot(`; 2 `fill(`; 0 `request.*` / `security(`; 0 `cross*(` / `ta.cross`; 0 `ema(`/`ta.ema`/`ta.rsi`/`rsi(`; 1 `ta.atr(`; 1 `nz(`; 1 `math.sign`; 0 `pivothigh`/`pivotlow`; 0 `barstate`; 0 volume reads. Arithmetic corollary (not a new rule): on a flip bar `hold` is re-armed to 5×ATR(200), so the subsequent drift step `hold/mult/slope` equals ATR(200)/14 per bar — the `mult` cancels out of the drift by construction.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is a display indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly seven: (1) long-only pin with the short side explicitly disabled (down-flip events exit LONG to FLAT and never open SHORT, disclosed); (2) fixed **0.01 BTC** spot sizing (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above verified 5-USDT min-notional and 0.00001 min-qty); (3) all risk legs (SL/TP/trailing/time) explicitly disabled — flip-exit-only risk, disclosed; (4) 2000-bar warmup with pre-warmup bars flat (10× the longest used length 200; RMA seed residual after 2000 bars is (199/200)^2000 ≈ e^−10 < 1e−4, fenced); (5) display drop (upper/lower extremities, average plot styling, both fills, all colors, the `area` option — and the `width` input, which feeds only the dropped extremities); (6) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (7) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim).

**Immutable derivative identity:** `TV:LuxAlgo-Bcufg8oX|mirror-69969aea|hypertrend_mult5-slope14-atr200_orientation-flip_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup2000|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@10937128` (549 root strategy records, READMEs excluded; this file is the 550th). Case-insensitive content search for `hypertrend` and `Bcufg8oX` returns zero records; `hasnocool` hits are only other strategies' mirror-provenance citations (sell-in-may, DMI-swings, fisher, IK-grid — all different machines, none a HyperTrend record); `LuxAlgo` hits only the merged liquidity-sweep record (wick-sweep/break/retest event machine, different construction). No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors: different trigger and center vs all eight `supertrend` records and the open #63 supertrend-flip lane (every one anchors hl2/median-price bands with max/min trailing rails — here there is no hl2, no band, and no rail cross; the signal is the sign of the stepped average's own bar-to-bar change); different machine vs `ut-bot-atr-trailing-stop-flip` (plain ATR stop flip on price extremes — no average, no orientation state); different math and exits vs `tradingview-systemsoverfeelings-kama40-slope-flip-close-bracket` (Kaufman efficiency-ratio-adaptive KAMA(2/30/40) with a −6%/+3% SL/TP close-bracket box — here the average is ATR-threshold-gated jump-or-drift with a 5×RMA-ATR(200) gate, and exits are flip-only with no box); different system vs `github-indie-luxalgo-liquidity-sweep-wick-state` (wick-sweep/break/retest events — no average at all); different rails vs `turtle-system-2-55d`/`donchian-20-10` (highest/lowest breakout rails — this rule reads no highest/lowest); different construction vs `schaff-trend-cycle-band-edge` (bounded oscillator band edges) and vs `tradingview-coral-trend-pullback-adx` (six-stage EMA ribbon pullback entries). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

HyperTrend (per its header, code, and the live TradingView page): a real-time estimate of an underlying linear trend — a channel average that jumps toward price (blends to the mean) when price deviates beyond a 5×ATR tolerance and otherwise drifts linearly along the prevailing orientation; orientation flips re-arm the channel width. An average sloping upward indicates an uptrend, downward a downtrend (the author's display frame, never adopted as a crypto claim). The author further suggests channel extremities as support/resistance and wick contacts as reversal/retracement cues — discretionary chart-reading usage that this record does NOT adopt (fenced in Negative evidence 6).

### Research interpretation

Unlike pool breakout machines that chase Donchian-rail touches (turtle-system-2, donchian-20-10), unlike pool median-band flippers that trail hl2 (the eight supertrend records, UT Bot), and unlike the pooled KAMA40 slope-flipper (efficiency-ratio-adaptive smoothing with boxed exits), this machine follows the orientation of an average that stands still in structure most bars — blending only on tolerance breaks and otherwise creeping at ATR/14 per bar — flipping LONG/FLAT solely on the sign change of that average's own bar-to-bar step. The bet, as derived, is purely that this tolerance-gated orientation alternation ports arithmetically to BTCUSDT spot daily bars, with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series: `O/H/L/C[t]` are the venue bars (H/L/C feed the ATR and the average; O is validity only). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- R3 — ATR threshold (source formula, pinned): `A[t] = 5 × RMA-ATR(200)[t]` on venue bars (`ta.atr` is RMA-based; `nz` maps pre-200-bar `na` to 0 — warmup absorbs the zero-gate transient, fenced).
- R4 — Average step (source formula, pinned, prior-bar state read): `avg` seeded at the first bar's close. For `t ≥ 1`: `avg[t] = |C[t] − avg[t−1]| > A[t] ? mean(C[t], avg[t−1]) : avg[t−1] + os[t−1] × (hold[t−1]/5/14)` (the step reads pre-update orientation/hold per Pine statement order, fenced; the drift leg equals ATR(200)/14 per bar whenever `hold` was freshly re-armed).
- R5 — Orientation (source formula, pinned): `os[t] = sign(avg[t] − avg[t−1])` ∈ {1, −1, 0}, seeded `os = 1` (long-biased seed, disclosed). Exact-flat equality yields 0 (Pine `math.sign(0) = 0`, fenced) — never interpolated, never carried from a nonzero sign.
- R6 — Hold re-arm (source formula, pinned): `hold` seeded 0; `hold[t] = os[t] ≠ os[t−1] ? A[t] : hold[t−1]` (re-armed to the full 5× threshold on every orientation flip, including flips involving 0).
- R7 — Events (promoted machine, adaptation 1): `Buy[t] = os[t]==1 and os[t−1]==−1`; `Sell[t] = os[t]==−1 and os[t−1]==1` (mutually exclusive by construction — at most one fires per bar; any bar involving `os == 0` emits no event and holds position, disclosed).
- R8 — Position (promoted machine, adaptation 1): `LONG`/`FLAT` single-unit book. If FLAT and `Buy[t]` (post-warmup) → request LONG at the next open. If LONG and `Sell[t]` → exit the whole book at the next open. Short-side events while FLAT are explicit holds (short side disabled). A prevailing `os == 1` with no fresh post-warmup `Buy` never enters (entry needs the flip, disclosed).
- R9 — Risk legs (adaptation 3, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls, zero `alertcondition(` legs).
- R10 — Position state: one 0.01-BTC spot unit max, long or flat, never short. Safety orders: explicitly none. No pyramiding: while LONG no new Buy can add (entry needs FLAT, R8) — pinned absence, not invented.
- R11 — Warmup and gaps: flat until 2000 completed `1d` bars (10× the longest used length 200; RMA seed residual below 1e−4 thereafter). All three recursions (`avg`, `os`, `hold`) run from bar 1 so post-warmup state is deterministic. Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold.
- R12 — Invariant identifier: `TV:LuxAlgo-Bcufg8oX|mirror-69969aea|hypertrend_mult5-slope14-atr200_orientation-flip_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup2000|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `high`/`low`/`close` (ATR input, jump-gate input, step comparisons, validity), `open` (validity only). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used. Every live input is frozen at the decision close — point-in-time clean.
- Warmup: flat until 2000 completed bars (structural). No repainting (all three recursions read closed-bar values only and are append-only; the author's page independently claims no lookahead bias — cited, not relied upon), no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03 — the 11-04 bar was still forming at cycle time — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle); `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. The tolerance-gated average plus orientation sign is a plain precomputable signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned file ships every adopted headline fact quoted in Provenance: the `input.float(5/14/80%)` defaults and the five Style inputs, the `var`-seeded `avg`/`hold`/`os` registers, the `nz(ta.atr(200)) * mult` threshold, the jump-vs-drift `avg` ternary with its strict `>` gate, the `math.sign(avg − avg[1])` orientation, the flip-re-armed `hold`, the display-only extremities, the flip-breaking average plot, and the `indicator(` (not strategy) declaration. It ships zero orders, zero sizing, zero exits, zero performance figures — none adopted; all trading semantics are researcher pins disclosed above. The live TradingView page additionally reports LuxAlgo authorship, open-source status, the same three numeric defaults, the upward = uptrend / downward = downtrend convention, and the no-lookahead-bias claim — cited as source-reported page evidence, not as Hermes reproduction.

### Independently reproduced

Not independently reproduced. No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. No executable probe ran in this unattended cycle; logic assertions above are static readings of the pinned fence, fenced in Negative evidence where implementations may differ.

### Negative evidence

1. Statement-order fence: the `avg` step executes before the `os` reassignment, so the drift leg reads the pre-update (prior-bar) `os`/`hold`. An implementation stepping `avg` with the already-updated orientation prints a different, unpinned event set — flagged as an implementation obligation, never strategy behavior.
2. Zero-sign fence: `math.sign` of an exactly-flat average step is 0, which is neither long nor short and emits no event; position holds through 0-bars. An implementation carrying the last nonzero sign across 0-bars, or treating 0 as a flip leg, prints a different, unpinned event set.
3. Seed/transient fence: `avg` starts at the first bar's close, `hold` at 0, `os` at 1, and `nz(ta.atr(200))` is 0 until 200 bars, so early bars blend on nearly every bar with a 0-drift leg — the 2000-bar warmup absorbs all four; shorter warmups print different early event sets and are unpinned. Post-warmup prevailing-`os == 1` without a fresh `Buy` never enters (R8) — flagged as an implementation obligation.
4. Equality/FP silence fenced: the jump gate is a strict `>` — an exact `|C − avg| == A` touch takes the drift branch; floating-point RMA comparisons may disagree across implementations on degenerate flat input — fenced as an implementation obligation; live tape carries no constant stretches so no live event turns on it.
5. Display-leg fence: upper/lower extremities, the `width` input feeding them, all three plots, both fills, all colors and the `area` option are adopted nowhere — an implementation trading extremity touches prints a different, unpinned event set.
6. Discretionary-usage fence: the author's extremity-as-S/R and wick-contact reversal prose is chart-reading guidance with no coded event and is adopted nowhere — flagged as out of scope, never strategy behavior.
7. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
8. Derivation boundary fenced: the only non-source behavior is the seven declared adaptations (long-only pin, fixed sizing, disabled risk, 2000-bar warmup, display drop, 0.1% cost overlay, next-open fills); the threshold, average step, orientation, hold re-arm, inequalities, seeds, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.
9. Mirror-vs-page drift fence: the code freeze is the mirror blob `118578aa…`; the TradingView page is cited for authorship, defaults, and prose claims only. If the page's current code ever differs from the blob, this record follows the blob.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `5×RMA-ATR(200)` gate / jump-blend-vs-drift average / `sign(avg − avg[1])` orientation / flip-re-armed hold / strict gates / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 2000-bar warmup are frozen.

- F1 — Gate relevance: a `mult = 1` twin (same rest) must not improve net expectancy; fail ⇒ the 5× tolerance gate is decoration on drift churn.
- F2 — Slope relevance: a `slope = 30` twin (same rest) must not improve net expectancy; fail ⇒ the ATR/14 drift rate carries no information.
- F3 — ATR-length relevance: an `atr(100)` twin (same rest) must not improve net expectancy; fail ⇒ the 200-bar RMA window is decoration on generic volatility gating.
- F4 — Warmup relevance: a 2400-bar-warmup twin must print the identical post-2400 event set; fail ⇒ seed transients leak past the declared warmup.
- F5 — Orientation relevance: an hl2-band twin (same gate widths, SuperTrend-style rails, same rest) must not improve net expectancy; fail ⇒ the stepped-average orientation is decoration on a plain band flipper.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The source is a TradingView indicator under CC BY-NC-SA 4.0, © LuxAlgo (cited, not copied; short literals only); every trading semantic (long-only pin, flip exits, venue, sizing, warmup, no-box risk, next-open fills, cost overlay) is a researcher adaptation disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- Statement order, zero-sign handling, seed behavior and degenerate-input FP behavior are implementation-defined (Negative evidence 1–4); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (2000) is a researcher margin at 10× the longest used length 200; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/HyperTrend%20%5BLuxAlgo%5D.pine (canonical pinned code; commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, blob `118578aacb18e1fbc4a193e0a04d22dfa3dfd4f6`, 3,869 bytes / 164 lines with an 85-line Pine block, sha256 `f0f071265a8178b2219ec1c912973df53afda2d6a6b9bc4376a2bab9acdeb6cc`)
- https://www.tradingview.com/script/Bcufg8oX-HyperTrend-LuxAlgo/ (upstream original page; HTTP 200 verified this cycle; LuxAlgo authorship, open-source status, mult 5 / slope 14 / width 80% defaults, slope-direction convention, no-lookahead-bias claim — cited not copied)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (NOTIONAL minNotional 5.0, LOT_SIZE 0.00001/0.00001, PRICE_FILTER tickSize 0.01; last completed daily close 77,453.86 on 2026-11-03)
