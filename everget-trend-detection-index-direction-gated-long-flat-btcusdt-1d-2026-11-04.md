---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: everget Trend Detection Index direction-gated long-flat on BTCUSDT 1d bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-04
sources:
  - https://github.com/everget/tradingview-pinescript-indicators/blob/master/oscillators/trend_detection_index.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# everget Trend Detection Index direction-gated long-flat on BTCUSDT 1d bars

## Provenance

**Primary source (fetched live over HTTPS this cycle, byte-identical):** file `oscillators/trend_detection_index.pine` in public repository `https://github.com/everget/tradingview-pinescript-indicators`, pinned at repo HEAD `8385cc421888bbf31f36407195796bc0eabafb19` (verified via `git ls-remote` this cycle). File commit `7f20cfa04e8d` dated `2023-11-04T18:54:29Z` (sole commit touching that path per the GitHub commits API this cycle; date part adopted as `source_as_of`). Pinned blob SHA `8555ed52649a7b9212f6141ffd8753c6266a4a67` (681 bytes per the GitHub contents API at the pinned ref), SHA-256 `9f4a2a1a1ba38b52ac57c0edc610a5111f83d95194ef11a1a3abd281bbfc80a1` (recomputed locally this cycle from the raw fetch; double-fetch identical). Header reads `Copyright (c) 2018-present, Alex Orekhov (everget)` under `GPL-3.0` (free-software grant, quoted as printed). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Order-affecting logic (full 681-byte `study()` file, zero `strategy.*` calls anywhere — the indicator→machine reading below is the predeclared derivation, never a source claim):** inputs `length = input(title="Length", type=integer, minval=1, defval=20)` and `src = input(title="Source", type=source, defval=close)`; `momentum = change(src, length)`; `tdi = abs(sum(momentum, length)) - (sum(abs(momentum), length * 2) - sum(abs(momentum), length))`; `direction = sum(momentum, length)`; `plot(tdi, ...)` / `plot(direction, ...)`; `hline(0, title="Zero Level", linestyle=dotted)`. Code census this cycle: 1 `study(` / 0 `strategy(` / 0 `strategy.entry` / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=` / `limit=` / target / trailing / time-exit inputs or calls / 0 `request.*` / 0 `timeframe.*` / 0 `volume` / 0 `open` / 0 `high` / 0 `low` in any order-gating line (the rule reads `close` only) / exactly 2 `input(` (length, source — no date-window, no mode switch, no threshold input). Pine `change(src, L)` is `src[t] - src[t-L]`; `sum(x, N)` is the trailing N-bar sum including the current bar — both causal on completed bars.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source ships a market-agnostic `study()` indicator with two plots and a zero line and no order, sizing, timing, market, or cost leg of any kind. Researcher-declared adaptations are exactly five: (1) market pin **BTCUSDT Binance spot 1d** (the indicator names no market — venue/frame pin disclosed, never presented as a source claim; spot is the minimal realistic venue because the derived machine is long-flat and never needs margin-short permission); (2) indicator→executable long-flat machine: `LONG[t] = (TDI[t] > 0) and (D[t] > 0)` holds long, everything else is flat — completed-bar decision with **next-bar-open market** fills (predeclared per the merged Decycler lane precedent, which reads an everget `study()` file the same way); (3) `length = 20` and `src = close` pinned at the file defaults (any other value is a different, unpinned rule); (4) adopted **60-bar warmup** with pre-warmup bars flat by record rule (structural minimum — first finite print at the 60th completed bar, verified index 59 this cycle); (5) house sizing/costs replacing the absent source economics (fixed 0.01 BTC, 0.1%/side taker; spot means no funding leg exists — constructive exclusion, never zero-claimed). The `mom` / `TDI` / `D` arithmetic, the strict `> 0` pair against the plotted zero line, and the no-stop/no-target posture are source-pinned or predeclared; no short leg is invented.

**Immutable derivative identity:** `everget:TDI-direction-gated|length20_close|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-04`. Changing any length, source, threshold, direction, timing, market, risk, cost, sizing, or book state creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@dbdfe22e` (556 root strategy records, READMEs excluded; this file is the 557th). Case-insensitive filename search for `trend-detection` / `trend-detection-index` / `steckler` / `trend_detection_index` returns zero records. Content search for `Trend Detection Index` (exact indicator title), `trend_detection_index.pine`, `8555ed52` (pinned blob), and `Steckler` returns zero records embodying this rule. The four pool `\bTDI\b` hits are all the **Traders Dynamic Index** (RSI+BB+MA volatility-band machine — different indicator, different author, different arithmetic; fenced in Negative evidence 1). No open `research/*` PR is this file, author, construction, or signal (17 open PRs enumerated by number — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — titles contain no trend-detection / steckler / everget-TDI hit). Five-axis distinction vs nearest pool neighbours: different object vs VHF/PFE/RWI/Choppiness/KAMA-ER (all single-window *ratios* against a tuned threshold — this record *subtracts* two adjacent-window absolute-momentum sums with a fixed structural zero); different trigger vs TASC-linreg40-slope-sign (single-OLS slope *sign* — this record gates on a *net-minus-prior-gross* level plus a direction sum); different mapping vs Decycler fast-slow *cross* (two filtered lines crossing each other — this record crosses nothing but the plotted zero). No duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Net-displacement-vs-prior-churn trend detection. The file's construction is self-describing: per-bar momentum `mom[t] = C[t] - C[t-20]`; trailing direction sum `D[t] = Σ mom` over the last 20 bars; gross churn over the last 40 `|mom|` prints minus gross churn over the last 20 leaves the *prior* adjacent window's churn; `TDI = |D| - priorGross`. `|D|` is the net displacement magnitude of the recent window (triangle-inequality-capped by its own gross); subtracting the prior window's gross asks whether the recent net move *exceeds everything the prior window churned through*. The plotted `hline(0)` is the construction's own reference: positive TDI means net beat prior churn, negative means it did not. The file ships no market, direction, entry, exit, stop, target, or performance claim of any kind.

### Research interpretation

Adjacent-window absolute-momentum subtraction with a direction gate, long-flat. Write `D[t] = Σ_{k=0..19} mom[t-k]` (equivalently `20·(SMA20[t] − SMA20[t-20])`) and `TDI[t] = |D[t]| − Σ_{k=20..39} |mom[t-k]|`. `TDI[t] > 0` means the last 20 bars' net drift magnitude beat the *entire* absolute churn of the 20 bars before them — a burst that dwarfs its own baseline; `D[t] > 0` signs that burst upward. Unlike VHF (highest-high/lowest-low range *ratio* with a tuned 0.4-style level), PFE (fractal-efficiency *ratio* with ±50 bands), RWI (high/low excursion *ratio* with 1.0/0.5 bands), or KAMA-ER (net-over-gross *ratio* driving an adaptive average), this rule never divides and never tunes a band: it *subtracts* absolute sums and holds against the file's own structural zero. Unlike Decycler (fast filtered line *crossing* a slow filtered line), this rule crosses nothing against itself: zero is the sole reference, and the direction sum is the only companion. The failure mode is plain: the 20-bar net needs a sustained push to beat a churning baseline, so entries arrive late into bursts and the flat leg rides out every chop below zero — disclosed, not upgraded.

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; entries/exits next-bar-open market; long-flat single-unit book — any other length, source, threshold, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days; no session template, no holiday skip.
- R2 — Source series: `C[t]` is the sole signal input via `mom[t] = C[t] − C[t-20]`. `O[t]`/`H[t]`/`L[t]` are never read by any order-gating line (fills price at opens; notionals reference closes for cost sizing only). No volume, no funding/OI/mark-index read gates on any order; no sentiment/macro/on-chain/cross-venue state.
- R3 — Composite (file math, frozen at defaults): `D[t] = Σ_{k=0..19} mom[t-k]`; `TDI[t] = |D[t]| − (Σ_{k=0..39} |mom[t-k]| − Σ_{k=0..19} |mom[t-k]|)`, finite only when all 60 closes `C[t-59..t]` are finite (first possible at the 60th completed bar — verified index 59 this cycle). `length = 20`, `src = close` frozen; any other pair is unpinned.
- R4 — Events (strict inequalities against the plotted zero, pinned): `Long[t] = (TDI[t] > 0) and (D[t] > 0)`; everything else (either leg `== 0`, either leg NaN, or any false combination) is flat-hold — explicit hold, no event. At most one fill decision per bar by construction.
- R5 — Position (derived machine, predeclared): `LONG`/`FLAT` single-unit book. If FLAT and `Long[t]` (post-warmup) → buy at the next open. If LONG and not `Long[t]` → close the whole book at the next open. While LONG, true `Long[t]` bars are no-ops; while FLAT, false bars are no-ops.
- R6 — Risk legs (file absence, not invented): stop-loss, take-profit, trailing, and time exit are all explicitly disabled — the 681-byte file ships none, and no prose ships any. The `not-Long` close is the sole exit path.
- R7 — Position state (single deterministic path — no reset, no re-warmup): one 0.01-BTC unit max, long or flat. Safety orders: explicitly none. No pyramiding: while LONG no new entry can add (entry needs FLAT). No cooldown: after any close, a fresh `Long` signal may re-enter at the next signal. Fills are unconditional. Invalid bars (non-positive/non-finite close) force `mom` NaN → hold (no signal, no close). Missing-bar stretches freeze evaluation at the prior target — book and ledger retained across the freeze; evaluation resumes on the next valid bar with no warmup repetition, never backfilled, never forced flat.
- R8 — Warmup: flat until 60 completed `1d` bars (structural minimum — index 59 is the first finite `TDI`/`D` print, verified this cycle; finite 60-bar memory ⇒ any warmup ≥ 60 prints the identical post-warmup event set, fenced).
- R9 — Invariant identifier: `everget:TDI-direction-gated|length20_close|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001-nofunding|spot1x|nostop-notarget|warmup60|2026-11-04` (any length, source, threshold, direction, sizing, fill, risk, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (the sole series the formula reads; `open` is never an order-gating input — fills price at opens; notionals reference closes for cost sizing only). No `high`, no `low`, no `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (no multi-timeframe call, no `request.*`, no cross-sectional ranking — one asset, one frame; the 60-close window reads trailing completed closes of the same series, never a second feed).
- Warmup: 60 completed `1d` bars flat by record rule — structural minimum is the 60th completed bar (60 finite closes for the first `TDI`/`D` pair; verified index 59 this cycle). Pre-warmup and any NaN-signal bars are flat/hold by record rule; missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (sums read completed closes including the decision bar only), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled (the derived machine never sells short). Fills are never conditional on equity or buying power.
- Order timing (declared derivation): completed-bar decision with next-bar-open market fills for entries and whole-book closes — the same verified execution primitive as the merged Decycler and PSY12 lane records (single-frame completed-bar decision, next-open market fill, no protective stop/limit legs anywhere in the derived machine, hence no same-bar TP/SL ordering ambiguity; each bar's outcome is a single deterministic event: hold, open-long, or close-flat). This record claims no other fill convention: no same-bar-close print, no maker-touch, no intrabar-path-dependent fill.
- Pinned engine path (verified at the pin this cycle): Hummingbot package label `20260920`, VERSION `dev-2.17.0` (local checkout `2dbc844fadb9d863b3ab0af1b8ab100472102e42` carries `hummingbot/VERSION` file `2.17.0`, verified live this cycle; `8b0e067e80ab62f10846d518dcb5a8218527ddb3` is an ancestor of the local checkout, verified via `merge-base --is-ancestor` this cycle; code paths verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py:221`, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py:747`, `class OrderExecutorSimulator` in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:9`, `INTERVALS "1d" = "1d"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py:24`). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the trailing-60 `TDI`/`D` pair and the long/flat state pin via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy. The 60-close precomputable sum pair plus zero-gated state machine is a plain signal series, not a new execution primitive; no new data requirement, no representative-capability validation owed.
- Stop/limit modeling: none — the derived spec carries zero stop/limit/trailing/time orders by record rule. No hidden Hummingbot stop-order defaults are relied upon, and with no stop/limit legs there is no same-bar TP/SL ordering ambiguity.
- Sizing/capital/costs: the file ships no economics (no capital, sizing, fee, or slippage line of any kind — recorded as absent, never as evidence). Explicit house overlay: single-unit frame, 0.1% taker fee per filled side, slippage unmodeled by declaration. Exchange facts re-verified live this cycle via `api/v3/exchangeInfo`: `BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 (`NOTIONAL`). The fixed 0.01 BTC (≈774.54 USDT at the cycle's last completed close 77,453.86 on 2026-11-03, above the 5.0 min-notional and an exact multiple of the 0.00001 step). Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: at most one single-asset engine position at any time; a `not-Long` signal closes it (re-entry earliest next signal). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (file fetched live this cycle at the pinned ref, 681 bytes, blob `8555ed52`, file commit `7f20cfa04e8d` dated 2023-11-04): the `study("Trend Detection Index", shorttitle="TDI")` declaration; the `length = 20` / `src = close` defaults; the `momentum = change(src, length)` line; the `tdi = abs(sum(momentum, length)) - (sum(abs(momentum), length * 2) - sum(abs(momentum), length))` line; the `direction = sum(momentum, length)` line; the `hline(0, title="Zero Level")` reference; the GPL-3.0 licence header and Alex Orekhov copyright. This record claims no source-reported performance number of any kind — no return, win rate, trade count, or backtest figure is carried into the derived specification — and no reproduced performance exists.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/composite/state pipeline (impl-faithful trailing-60 `TDI`/`D` sums, 60-bar warmup, next-open single-unit long-flat machine), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic, double-run identical):** TAPE-A (dead-constant 170-bar tape) prints post-gate all-flat (0 entries / 0 exits, ending FLAT) — zero momentum yields `TDI = 0`, `D = 0`, hold, as pinned; TAPE-B (sustained +1%/day 170-bar uptrend tape) prints post-gate one-entry long-hold (1 entry / 0 exits, ending LONG) — sustained net drift beats prior churn with positive direction, as pinned; TAPE-C (sustained −1%/day 170-bar downtrend tape) prints post-gate all-flat (0 entries / 0 exits, ending FLAT) — negative direction never fires the long gate, as pinned.

**Live-exchange microstructure probes (this cycle, Binance spot 1d klines, 3,366 completed bars 2017-08-17→2026-11-03, last close 77,453.86):** 800 post-warmup long-signal bars drive 38 entries / 38 exits ending FLAT (holds median 21 bars, max 48 — non-degenerate, non-buy-and-hold). Two independent runs produce identical digests (signal-series digest `70276fd5`). Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Acronym fence, admitted plainly: pool `tdi-pac-strength-tiered-alert-reversal` trades the **Traders Dynamic Index** (RSI-13 + 2/7-bar SMA pair inside a 34-bar 1.6185-sigma band plus a 5-bar SMMA price-action channel — a band-channel conjunction object). This record trades the **Trend Detection Index** (adjacent-window absolute-momentum subtraction with a direction sum — a subtraction object reading closes only). Shared `TDI` letters are not shared signal; the two files share no author, no formula, no input, and no event.
2. Equality fence: `TDI == 0` or `D == 0` emits no event (strict `> 0` pair pinned — the constant tape exercises the exact-zero hold path). An implementation using `>=` prints a different, unpinned event set.
3. NaN fence: any non-finite `mom` print (non-positive/non-finite close) or pre-60th-bar evaluation holds with no signal and no close. Interpolating, seeding, or backfilling is a different, unpinned rule.
4. Derivation-boundary fence: the source file contains zero order calls, so the FLAT→LONG / LONG→FLAT next-open machine is the predeclared derivation, never a source claim; this record is therefore never evidence that everget endorses any executable posture. A reviewer must not substitute a same-bar-close, stop-carrying, or two-sided variant into this record.
5. Single-print-twin fence: no twin is admitted — any per-bar (unsmoothed) `mom`-sign variant, any `TDI`-only (direction-gate-dropped) variant, any banded-threshold (`±ε`) variant, any other length, source, frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.
6. Overlap fences, admitted plainly: pool `vhf`/`pfe`/`rwi`/`choppiness`/`kama-er` all trade single-window *ratios* against tuned *bands* (ratio-band objects — this record subtracts absolute sums with a structural zero, no division, no band); `tasc-linreg40-slope-sign` trades a single-OLS slope *sign* (a slope object — this record gates a *level* (`TDI`) plus a *sum* (`D`)); `ehlers-decycler` trades a fast-line *cross* of a slow line (a cross object — this record crosses nothing but zero). Shared "trend/efficiency/momentum" vocabulary is not shared signal.
7. Warmup-identity fence: finite 60-bar memory ⇒ any warmup ≥ 60 prints the identical post-warmup event set; the adopted 60 is the structural minimum. A shorter warmup (< 60) prints a different, unpinned early event set.
8. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
9. Page-drift fence: this record follows the file content as fetched 2026-11-04 at repo HEAD `8385cc42` (file commit `7f20cfa04e8d`). If the file is ever edited, this record does not move with it.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `length 20` / `close` source / adjacent-window subtraction / strict `TDI > 0 ∧ D > 0` pair / long-flat book / no-stop-no-target posture / `1d` BTCUSDT spot / next-open fills / 0.01 BTC / 0.1% costs / 60-bar warmup are frozen.

- F1 — Horizon relevance: an L=10 twin (same subtraction, grid, fills, `20 → 10` horizon only) must not improve net expectancy; fail ⇒ the 20-bar horizon adds nothing over a faster read, and the record is a horizon label rather than a horizon edge.
- F2 — Direction-gate relevance: a TDI-only twin (long while `TDI > 0` regardless of `D` sign — same rest) must not improve net expectancy; fail ⇒ the direction gate adds nothing over the churn-beat leg alone, and the record is a gate label rather than a signed-burst edge.
- F3 — Zero-vs-band relevance: a band twin (long while `TDI > +0.5·median40(|mom|)` with the same direction gate — same rest) must not improve net expectancy; fail ⇒ the structural zero adds nothing over a churn-scaled band, and the record is a trigger label rather than a zero edge.
- F4 — Warmup relevance: a 120-bar-warmup twin must print the identical post-120 event set (finite 60-bar memory ⇒ structural identity is expected); fail ⇒ seed or ramp transients leak past the declared warmup.

## Crypto portability

Pinned to BTCUSDT Binance spot under the house overlay (declared port of a venue-free close-only formula). The rule reads completed daily closes only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (equity-calendar effects are non-issues on crypto — disclosed, not modeled). The composite is unit-free in differences-of-closes (a subtraction of absolute sums), so unlike absolute-price thresholds the rule ports across venues without re-scaling — yet 20-bar net-vs-prior-churn on crypto microstructure (24/7 closes, stablecoin-quoted prints, volatility-regime shifts the source never traded) fires at a cadence the source never measured (38 round-trips across 3,306 post-warmup bars here), disclosed without re-tuning. The rule is long-flat, so a spot deployment expresses the full machine with no short permission — a two-sided or perpetual variant would be a different, unpinned claim (this record's gate-5 evidence is the spot path only). No warmup history beyond 60 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Late-burst book: the live window prints 38 round-trips across 3,306 post-warmup bars (average hold ≈ 21 bars) with only `not-Long` closes as exits — the record's principal risk is entering bursts after the push is mature and riding chop below zero with no guardrail, by the derived design.
- Whipsaw by design: a `TDI` oscillating across zero with positive `D` prints full open/close cycles at the worst prints of each flicker; the zero line offers no band or hysteresis against it, by the prescribed design.
- Single-venue port residual: venue-free close arithmetic vs Binance spot execution (prints, fees, open-definition across 24/7 sessions, margin mechanics beyond the house model) is unclaimed, disclosed.
- Next-open latency idealization: indicator plots confirm on bar close while fills land on the next open; any live gap between the decision close print and the realized next-open fill differs by construction — disclosed, research-only.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the file presents a reusable indicator as a research object, not a vetted trading system — this record is research-only and claims no live suitability.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary file + pin: https://github.com/everget/tradingview-pinescript-indicators/blob/master/oscillators/trend_detection_index.pine (repo `everget/tradingview-pinescript-indicators`, HEAD `8385cc421888bbf31f36407195796bc0eabafb19` verified live 2026-11-04; file commit `7f20cfa04e8d` dated 2023-11-04; 681 bytes, blob `8555ed52649a7b9212f6141ffd8753c6266a4a67`, SHA-256 `9f4a2a1a1ba38b52ac57c0edc610a5111f83d95194ef11a1a3abd281bbfc80a1`; `length = 20` / `src = close` defaults, `momentum = change(src, length)` / `tdi = abs(sum(momentum, length)) - (sum(abs(momentum), length * 2) - sum(abs(momentum), length))` / `direction = sum(momentum, length)` / `hline(0)`; `study()` with zero `strategy.*` calls — © Alex Orekhov, GPL-3.0)
- Lane precedent (different mechanism, unmerged-proof never claimed): `ehlers-decycler-oscillator-cross-long-flat-btcusdt-1d-2026-10-16.md` (everget `study()`→long-flat derivation pattern)
- Nearest pool lineages (different mechanisms, unmerged-proof never claimed): `tdi-pac-strength-tiered-alert-reversal-two-sided-btcusdt-2h-2026-10-15.md` (Traders Dynamic Index — different indicator); `vhf-trend-phase-threshold-latch-reversal-two-sided-btcusdt-1d-2026-10-15.md`; `pfe-polarized-fractal-efficiency-hysteresis-two-sided-btcusdt-1d-2026-10-15.md`; `tradingview-tasc-linreg40-slope-sign-long-flat-btcusdt-1d-2026-10-26.md`
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty/step 0.00001/0.00001, min-notional 5.0 via `NOTIONAL`) plus `api/v3/klines` 1d probes (3,366 completed bars 2017-08-17→2026-11-03, 800 long-signal / 2,506 flat-signal post-warmup → 38 entries / 38 exits, signal digest `70276fd5` double-run identical), fetched live 2026-11-04
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
