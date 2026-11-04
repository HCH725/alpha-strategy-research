---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Pivot Point SuperTrend flip long-flat on BTCUSDT 1d bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Pivot%20Point%20SuperTrend%20(Indie)/Pivot%20Point%20SuperTrend%20(Indie).pinescript4
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Pivot%20Point%20SuperTrend%20(Indie)/README.md
  - https://www.tradingview.com/script/L0AIiLvH-Pivot-Point-Supertrend/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pivot Point SuperTrend flip — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`64f0494a84273138b2e6a0f15821b18ba1616056`** (`Add 60 community MIT/MPL indicators from TakeProfit with guides`, author PavMedd, 2026-10-08T20:41:02Z, verified via GitHub API this cycle), file **`indicators/Pivot Point SuperTrend (Indie)/Pivot Point SuperTrend (Indie).pinescript4`**, blob `7695765e57d6da49d3412d755c58c7b1b727af43`, **3,290 bytes / 139 lines**, `study("Pivot Point SuperTrend", overlay = true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle are byte-identical (second download `cmp`-matched); `git hash-object` of the working copy reproduces the API blob SHA exactly. The header carries `// © LonesomeTheBlue` and the Mozilla Public License 2.0 notice. The pinned port guide (`indicators/Pivot Point SuperTrend (Indie)/README.md`, 21,928 bytes, fetched at the pinned ref this cycle) confirms the original is LonesomeTheBlue's Pivot Point Supertrend (Pine Script v4), the Indie port keeps the 2:1 weighted center, RMA-based ATR bands and trailing state machine, and records the 7-parameter default table plus the live TradingView original URL, which returned HTTP 200 this cycle (public, accessible — cited, not copied).

**Order-affecting logic read verbatim (the alert block governs; the study ships no orders):** inputs pinned at defaults `prd = 2` (Pivot Point Period, 1–50), `Factor = 3` (ATR Factor, ≥1, step 0.1), `Pd = 10` (ATR Period, ≥1); `showpivot = false`, `showlabel = true`, `showcl = false`, `showsr = false` (all display-only). Confirmed pivots: `ph = pivothigh(prd, prd)`, `pl = pivotlow(prd, prd)` — Pine confirms each pivot `prd` bars after its extremum bar and registers the value on the confirmation bar (never backdated, never revised after confirmation). Center (updated only on confirmation bars): `var float center = na`; `lastpp = ph ? ph : pl ? pl : na`; `if lastpp: center := na(center) ? lastpp : (center * 2 + lastpp) / 3`. Bands (Pine v4 `atr()` is RMA-based): `Up = center - (Factor * atr(Pd))`, `Dn = center + (Factor * atr(Pd))`. Trailing state: `TUp := close[1] > TUp[1] ? max(Up, TUp[1]) : Up`; `TDown := close[1] < TDown[1] ? min(Dn, TDown[1]) : Dn`. Trend (long-condition priority, seeded long): `Trend := close > TDown[1] ? 1 : close < TUp[1] ? -1 : nz(Trend[1], 1)`; `Trailingsl = Trend == 1 ? TUp : TDown`. Coded events: `bsignal = Trend == 1 and Trend[1] == -1`; `ssignal = Trend == -1 and Trend[1] == 1` (the Buy/Sell `alertcondition(` legs; a third `alertcondition(change(Trend))` mirrors the same transition and adds no new event).

**Pine-block census (139-line fence):** 1 `study(`; 0 `strategy.*` of any kind; 7 `input(`; 1 `pivothigh(`; 1 `pivotlow(`; 1 `atr(` (RMA); 3 `alertcondition(` (Buy / Sell / Trend-Changed, one event family); 4 `plotshape(` (H/L pivot markers with `offset = -prd`, Buy/Sell labels — display); 0 `request.*`; 0 `volume`. Support/resistance registers (`support := pl ? pl : support[1]`, `resistance := ph ? ph : resistance[1]`, circle plots with `offset = -prd`), the center-line plot, the H/L markers and the label shapes are display-only and read by no signal line.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is a display/alert indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly seven: (1) long-only pin with the short side explicitly disabled (Sell-flip events exit LONG to FLAT and never open SHORT, disclosed); (2) fixed **0.01 BTC** spot sizing (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above verified 5-USDT min-notional and 0.00001 min-qty); (3) all risk legs (SL/TP/trailing/time) explicitly disabled — flip-exit-only risk, disclosed; (4) 100-bar warmup with pre-warmup bars flat (10× the longest used length 10, plus pivot-confirmation/center-seed margin); (5) display drop (H/L markers, S/R circles, center-line plot, Buy/Sell labels — the `Trend` state they visualize is kept); (6) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (7) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim).

**Immutable derivative identity:** `GH:Indie-script-64f0494|ppsupertrend_prd2-factor3-atr10_confirmed-pivot-center_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup100|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@66f87afe` (548 root strategy records, READMEs excluded; this file is the 549th). Case-insensitive content search for `pivothigh`/`pivotlow` hits only other strategies' language-function mentions (Kaufman pivot breakout, LuxAlgo sweep, RSI-divergence, camarilla, salaryman-dow, traderlodge-pivot3 — all different machines, none a Pivot Point SuperTrend record); `LonesomeTheBlue`, `lastpp`, `L0AIiLvH` return zero records. No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors: different center construction vs all eight `supertrend` records and the open #63 SSL/supertrend-flip lane (every one anchors on hl2/median-price bands — here the baseline is a confirmed-pivot weighted center that moves only on pivot-confirmation bars, with an explicit prd-bar confirmation lag); different system vs `pivot-point-breakout-kaufman` (Perry Kaufman pivot breakout — no ATR trailing state, no flip machine); different math vs `turtle-system-2-55d`/`donchian-20-10` breakout records (Donchian highest/lowest rails — no pivot registration, no ATR bands); different trigger vs `ut-bot-atr-trailing-stop-flip` (plain ATR stop flip on price extremes — no pivot center at all). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Pivot Point SuperTrend (per its header, code, and the port guide): a trend-following indicator that anchors its baseline to confirmed pivot highs/lows rather than raw price — a weighted center line (2:1 smoothing) updates only when a new pivot confirms, ATR bands around that center form trailing upper/lower rails, and Buy/Sell markers print exactly on trend-validation flips. The author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool breakout machines that chase Donchian-rail touches (turtle-system-2, donchian-20-10) and unlike pool median-band flippers that trail hl2 (the eight supertrend records, UT Bot), this machine trails a baseline that stands still most bars and jumps only when a pivot confirms — the bet, as derived, is purely that this stepped pivot-center-plus-ATR-rail flip alternation ports arithmetically to BTCUSDT spot daily bars, with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Source series: `O/H/L/C[t]` are the venue bars. No volume read exists in this rule.
- R3 — Confirmed pivots (source formulas, pinned): `ph[t] = pivothigh(2, 2)` evaluated at the confirmation close (extremum bar `t-2`, value registered at bar `t` — Pine confirmation-timing, never backdated); `pl[t] = pivotlow(2, 2)` mirrors. A bar with no confirmation carries na on both legs.
- R4 — Center (source formula, pinned): `lastpp[t] = ph[t] ? ph[t] : pl[t] ? pl[t] : na` (pivot-high priority on the rare same-bar double confirmation, disclosed); `center[t] = lastpp[t] and na(center[t-1]) ? lastpp[t] : lastpp[t] ? (center[t-1]*2 + lastpp[t])/3 : center[t-1]` (moves only on confirmation bars, else frozen).
- R5 — Bands and trailing rails (source formulas, pinned): `atr[t] = RMA-ATR(10)` on venue bars (seeded per language semantics); `Up[t] = center[t] - 3*atr[t]`; `Dn[t] = center[t] + 3*atr[t]`; `TUp[t] = C[t-1] > TUp[t-1] ? max(Up[t], TUp[t-1]) : Up[t]`; `TDown[t] = C[t-1] < TDown[t-1] ? min(Dn[t], TDown[t-1]) : Dn[t]`.
- R6 — Trend (source formula, pinned): `Trend[t] = C[t] > TDown[t-1] ? 1 : C[t] < TUp[t-1] ? -1 : Trend[t-1]` (long-leg priority on the degenerate both-true bar — strict cross of one rail implies distance from the other on live tape, disclosed; recursion seeded `nz(Trend[1], 1)`, i.e. long-biased seed).
- R7 — Events (source formulas, pinned): `Buy[t] = Trend[t]==1 and Trend[t-1]==-1`; `Sell[t] = Trend[t]==-1 and Trend[t-1]==1` (mutually exclusive by construction — at most one fires per bar; the `change(Trend)` alert mirrors the same transition and adds no event).
- R8 — Position (promoted machine, adaptation 1): `LONG`/`FLAT` single-unit book. If FLAT and `Buy[t]` (post-warmup) → request LONG at the next open. If LONG and `Sell[t]` → exit the whole book at the next open. Short-side events while FLAT are explicit holds (short side disabled). A prevailing `Trend == 1` with no fresh post-warmup `Buy` never enters (entry needs the flip, disclosed).
- R9 — Risk legs (adaptation 3, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R10 — Position state: one 0.01-BTC spot unit max, long or flat, never short. Safety orders: explicitly none. No pyramiding: while LONG no new Buy can add (entry needs FLAT, R8) — pinned absence, not invented.
- R11 — Warmup and gaps: flat until 100 completed `1d` bars (10× the longest used length 10, plus pivot-confirmation/center/RMA seed margin). Trend recursion runs from bar 1 so post-warmup state is deterministic. Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold.
- R12 — Invariant identifier: `GH:Indie-script-64f0494|ppsupertrend_prd2-factor3-atr10_confirmed-pivot-center_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup100|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (validity), `high`/`low` (pivot registration, validity), `close` (pivot confirmation input, ATR input, rail comparisons, validity). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used. Pivot values act at their confirmation close (R3) — evaluating them at the extremum bar would be future leakage and is explicitly not this rule.
- Warmup: flat until 100 completed bars (structural). No repainting (confirmed pivots never revise; center/rails/Trend read closed-bar values; Trend recursion is append-only with the source's own `nz(Trend[1], 1)` seed), no negative shift, no future reference, no full-sample normalization. Every live input is frozen at the decision close — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03 — the 11-04 bar was still forming at cycle time — above the cycle-verified Binance spot BTCUSDT `NOTIONAL minNotional 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (local checkout `2dbc844` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle); `hummingbot/strategy_v2/controllers/controller_base.py` (`determine_executor_actions`), `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py` (over spot feeds) and `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. Pivot-confirmation/weighted-center/ATR rails are a plain precomputable signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned 139-line fence ships every adopted headline fact quoted in Provenance: the `input(2/3/10)` defaults and the four display-flag defaults, the `pivothigh(prd, prd)` / `pivotlow(prd, prd)` legs, the `lastpp` selector, the `var`-seeded 2:1 weighted center update gated on `if lastpp`, the RMA `atr(Pd)` bands, the `max`/`min` trailing-rail recursion on previous-close conditions, the long-priority `Trend` expression with `nz(Trend[1], 1)` seed, the `Trailingsl` selector, the `bsignal`/`ssignal` conjunctions, the three `alertcondition(` legs, and the `study(` (not strategy) declaration. It ships zero orders, zero sizing, zero exits, zero performance figures — none adopted; all trading semantics are researcher pins disclosed above. The pinned port guide additionally reports the 1:1 logic port (confirmed pivots, weighted center, RMA ATR, trailing state, Buy/Sell markers), the MPL-2.0 license, and the full 7-parameter default table — cited as source-reported port evidence, not as Hermes reproduction. The linked TradingView original page is live (HTTP 200 this cycle).

### Independently reproduced

Not independently reproduced. No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. No executable probe ran in this unattended cycle; logic assertions above are static readings of the pinned fence, fenced in Negative evidence where implementations may differ.

### Negative evidence

1. Confirmation-timing fence: pivot values act at their confirmation close (extremum + 2 bars). An implementation backdating evaluation to the extremum bar reads two bars of future and prints a different, unpinned (and leaking) event set — flagged as an implementation obligation, never strategy behavior.
2. Same-bar double-confirmation fence: `lastpp` takes `ph` when both confirm on one bar (Pine ternary priority); an implementation taking `pl` (or averaging) prints a different, unpinned event set on those rare bars.
3. Seed/transient fence: `center` is na until the first pivot confirms, RMA-ATR is in seed transient, and `nz(Trend[1], 1)` seeds long — the 100-bar warmup absorbs all three; shorter warmups print different early event sets and are unpinned. Post-warmup prevailing-`Trend == 1` without a fresh `Buy` never enters (R8) — flagged as an implementation obligation.
4. Equality/FP silence fenced: strict inequalities decide every rail comparison — exact rail touches are holds; floating-point RMA comparisons may disagree across implementations on degenerate flat input — fenced as an implementation obligation; live tape carries no constant stretches so no live event turns on it.
5. Display-leg fence: H/L markers, S/R circles, center-line plot and Buy/Sell labels (including their `-prd` drawing offsets) are adopted nowhere — an implementation trading marker positions prints a different, unpinned event set.
6. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
7. Derivation boundary fenced: the only non-source behavior is the seven declared adaptations (long-only pin, fixed sizing, disabled risk, 100-bar warmup, display drop, 0.1% cost overlay, next-open fills); the pivot legs, weighted center, ATR bands, trailing rails, inequalities, priority, seed, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `pivothigh/low(2,2)` confirmation timing / 2:1 weighted center / `3×RMA-ATR(10)` bands / trailing-rail recursion / long-priority flip / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 100-bar warmup are frozen.

- F1 — Center relevance: an hl2-center twin (same Factor/Pd, same rest) must not improve net expectancy; fail ⇒ the pivot-confirmed center is decoration on a plain SuperTrend.
- F2 — Factor relevance: a `Factor = 1` twin (same rest) must not improve net expectancy; fail ⇒ the 3-ATR rail width is decoration on flip churn.
- F3 — Confirmation relevance: a `prd = 5` twin (same rest) must not improve net expectancy; fail ⇒ the 2-bar confirmation timing carries no information.
- F4 — Warmup relevance: a 200-bar-warmup twin must print the identical post-200 event set; fail ⇒ seed transients leak past the declared warmup.
- F5 — ATR-period relevance: a `Pd = 20` twin (same rest) must not improve net expectancy; fail ⇒ the 10-bar RMA window is decoration on generic volatility rails.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — the only venue-specific reads are OHLC). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- The source is a TradingView alert indicator under MPL-2.0 (cited, not copied); every trading semantic (long-only pin, flip exits, venue, sizing, warmup, no-box risk, next-open fills, cost overlay) is a researcher adaptation disclosed in Provenance — the derived event set must not be cited as the author's output or as lossless reproduction.
- Single-venue, single-pair, single-timeframe spot claim only; funding/OI/cross-venue/macro regimes are out of scope by construction, and the 0.1%/side overlay is a research cost model, never realized economics.
- Pivot-confirmation timing, seed behavior and degenerate-input FP behavior are implementation-defined (Negative evidence 1–4); bit-exact cross-implementation match on pathological input is not claimed.
- Warmup (100) is a researcher margin over the longest used length 10; shorter warmups print different early event sets and are unpinned.
- No profitability, Sharpe, drawdown, or capacity claim is made anywhere; PASS is pinned-engine expressibility only.

## Implementation status

`not-implemented` — no dedicated Qlib/Hummingbot executable recipe or deployment artifact exists for this record. This status describes artifacts only and does not revoke HB_READY PASS or permit downstream refusal. If formally selected for execution with no reproducible recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same pipeline without redoing HB_READY).

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`. This record authorizes no live, Paper, Testnet, or real-capital action of any kind.

## Related Wiki records

None.

## Sources

- https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Pivot%20Point%20SuperTrend%20(Indie)/Pivot%20Point%20SuperTrend%20(Indie).pinescript4 (canonical pinned source; commit `64f0494a84273138b2e6a0f15821b18ba1616056`, blob `7695765e57d6da49d3412d755c58c7b1b727af43`, 3,290 bytes / 139 lines, sha256 `e151d26eae059e42617c8d9729a4845b8d158b459f04e65552bfa73fa319d1e4`)
- https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Pivot%20Point%20SuperTrend%20(Indie)/README.md (port guide: LonesomeTheBlue Pine v4 original, 1:1 logic port, 7-parameter default table, MPL-2.0)
- https://www.tradingview.com/script/L0AIiLvH-Pivot-Point-Supertrend/ (upstream original page; HTTP 200 verified this cycle, cited not copied)
- Binance spot `BTCUSDT` exchange filters and `1d` klines fetched live this cycle (NOTIONAL minNotional 5.0, LOT_SIZE 0.00001/0.00001, PRICE_FILTER tickSize 0.01; last completed daily close 77,453.86 on 2026-11-03)
