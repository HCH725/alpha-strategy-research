---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Indie InSilico Hull-Suite self-slope-state long-flat on BTCUSDT 1d bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Hull%20Suite%20by%20InSilico%20-%20Indie%20Edition/Hull%20Suite%20by%20InSilico%20-%20Indie%20Edition.pinescript4
  - https://indie-script.github.io/indicators/Hull%20Suite%20by%20InSilico%20-%20Indie%20Edition/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hull-Suite self-slope-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`64f0494a84273138b2e6a0f15821b18ba1616056`** (2026-10-08, `Add 60 community MIT/MPL indicators from TakeProfit with guides`, verified via GitHub API this cycle), file **`indicators/Hull Suite by InSilico - Indie Edition/Hull Suite by InSilico - Indie Edition.pinescript4`**, blob `612880fb053eba3139c18c301c8651610f22c46c`, **2,262 bytes / 103 lines**, `study("Hull Suite by InSilico", overlay=true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `6471dbf892b9447a197064c762be0fec49234f1789dcc1d458adc4db53f2d0b7`, byte-identical to the working copy (blob base64 decoded and `cmp`-matched). Origin: InSilico's free TradingView community script Hull Suite (public guides confirm the InSilico authorship, the HMA/EHMA/THMA switch, the 55 default length, and the MHULL-vs-SHULL color rule; the TV search page returned bot-wall 403 this cycle — short-literal citation only, page code never re-fetched, no source block reproduced).

**Order-affecting logic read verbatim (code governs; the study ships no orders):** `src = input(close)`; `modeSwitch = input("Hma", options=["Hma","Thma","Ehma"])`; `length = input(55)`; `lengthMult = input(1.0)`; `useHtf = input(false)`; `htf = input("240", type=input.resolution)`; `HMA(_src,_length) => wma(2*wma(_src,_length/2)-wma(_src,_length), round(sqrt(_length)))`; `Mode(...)` selects the HMA branch at the default; `_hull = Mode(modeSwitch, src, int(length*lengthMult))`; `HULL = useHtf ? security(syminfo.ticker, htf, _hull) : _hull`; `MHULL = HULL[0]`; `SHULL = HULL[2]`; color `HULL > HULL[2] ? green : red` (exact equality prints red); two `alertcondition(` edges (`crossover(MHULL,SHULL)` trending-up, `crossover(SHULL,MHULL)` trending-down) — alarms only, never orders.

**Pinned arithmetic at defaults (no invention):** `int(55*1.0)=55`; Pine v4 integer division `55/2=27`; `round(sqrt(55))=round(7.416)=7`; hence the evaluated line is exactly `HMA(close,55) = wma(2*wma(close,27)-wma(close,55),7)`. The `security(` expression is fenced behind `useHtf=false` and no derived predicate reads any higher-timeframe value — any implementation enabling HTF prints a different, unpinned event set.

**Pine-block census (103-line fence):** 1 `study(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 11 `input(` (close / "Hma" / 55 / 1.0 / false / "240" / true / false / true / 1 / 40 — all fenced at defaults); 1 `security(` (fenced off, disclosed); 0 `request.*`; 0 `volume`; 2 `plot(` legs (MHULL plus the `visualSwitch`-gated SHULL leg — display-only, dropped, disclosed); 1 `fill(`; 1 `barcolor(` (fenced at `candleCol=false`, disclosed); 2 `alertcondition(` alarms — display/alarm-only, dropped, disclosed.

**Structural facts carried over exactly:** (a) single-HMA construction — one Hull line, never a cross of two different averages; (b) self-displacement slope state — the predicate compares the line with its own value two bars earlier (`HULL[t]` vs `HULL[t-2]`), with exact equality on the red/down side; (c) no MTF at the default, no session/timezone, no intrabar semantics, no volume read anywhere (every predicate is close-derived); (d) on closed bars the color is fixed (public guides note only the still-open bar can flip intrabar — absorbed by the once-per-completed-bar researcher pin).

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the self-slope state to long-flat entries/exits on completed bars (`HULL[t] > HULL[t-2]` → LONG, anything else — red slope, exact equality, na seeds — → FLAT, disclosed promotion; the level state, not the edge alarms, governs so the book is always defined); (2) long-only pin with the short side explicitly disabled (the construction is signed; the red-slope leg is a deliberate omission, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at probe last completed close 76,816.00, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 120-bar warmup with pre-warmup bars flat (structural scale is 63 bars — inner windows full at bar 55, outer 7-bar smoother full at bar 61, SHULL displacement to bar 63 — plus researcher margin); (6) display drop (both plot legs, the fill, the fenced candle coloring, thickness/transparency, both alarms, the fenced HTF leg); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (no confirmed-close flag ships in source, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-64f0494|hullsuite-hma55_self-slope-2bar_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup120|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@f99565d2` (543 root strategy records on base `main`, READMEs excluded; this file is the 544th). Case-insensitive content searches for `insilico`, `MHULL`, `SHULL`, `Hull Suite` return zero hits anywhere on base `main`; the two Hull-family neighbors below were surfaced by filename search and are distinguished on five axes. No open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number/branch — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors: different source file and math vs `hull-ema-crossover-reversal` (contemporaneous HMA(5)-vs-EMA(5) cross, two-sided reversal — two different averages crossing, not one line against its own past; lengths 5 vs 55); `fmz-hull-pac-linreg-swing` (Hull+PAC+linreg confluence on 1m, two-sided); `ema-cloud-7-20-trend` (close-vs-fast plus fast-vs-slow alignment conjunctions, 0 crossover calls); `flying-dragon-offset-ma-band-trend` (close versus 6-bar-lagged HMA(35) level band system); `ehma-range-band-breakout` (custom exponential-Hull recursion with symmetric ±2% envelope inequalities, no displacement state) — no duplicate, paraphrase, or trivial parameter variant. Same-commit screenings rejected before writing: OTT support-line cross (identical VAR(2)/1.4% ratchet math already ported on `main` as `freqtrade-fott-ott-var-cross-adx60-state-exit`, rejected here as already-ported), cRSI (fractional `rsi[4.5]` offset semantics un-pinnable, rejected in a prior cycle), Madrid ribbon (missing MMARB leg, rejected in a prior cycle).

## Economic mechanism

### Source-reported

Hull Suite (via InSilico, per the ported guide): three Hull-based smoothers (HMA/EHMA/THMA) in one tool; the band is the Hull line drawn against its own value two bars earlier; green when the current value is higher, red when lower — a trend-identification and pullback-filtering aid, with 55 suggested for swing entries and 180–200 for floating support/resistance. The author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool cross machines (HMA-vs-EMA, triple-EMA conjunctions that fire on line-over-line penetration) and unlike pool stack machines (Guppy/ribbon alignment that requires several lines to agree), this machine watches a *single* low-lag Hull line and trades only its own two-bar slope sign — the trigger is whether HMA(55) sits above where it stood two bars ago, not whether price sits above any average or whether fast/slow lines crossed. Unlike pool band machines (EHMA ±2% envelopes, offset Dragon bands), there is no envelope at all — the predicate is purely ordinal on one line's past. The bet, as derived, is purely that this self-slope sign ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Hull line (source formulas, pinned): `L=55`, `H=27` (`55/2` under v4 integer division), `R=7` (`round(sqrt(55))`); `W1[t]=wma(close,27)`, `W2[t]=wma(close,55)`, `D[t]=2*W1[t]-W2[t]`, `HULL[t]=wma(D,7)` (Pine-built-in trailing-WMA reading — na until each stage's full window; seeds absorbed by warmup, disclosed researcher reading).
- R3 — Self-slope state (source predicate, pinned): `UP[t]` iff `HULL[t] > HULL[t-2]` (the green leg); otherwise the red leg — exact equality is red in source and carried as FLAT, never LONG (pinned source-faithful conservatism, disclosed).
- R4 — Display/alarm drop (adaptation 6): both `plot(` legs, the `fill(`, the fenced `barcolor(`, thickness/transparency, the `useHtf=false` HTF leg, and both `alertcondition(` alarms never enter any predicate.
- R5 — State (promoted predicate, adaptation 1): `LONG[t]` iff `UP[t]`; `FLAT[t]` otherwise (covers red slope, exact equality, and na seeds — flat-tape probe: 180/180 post-warmup flats hold FLAT; live window printed 0 na post-warmup — carried as an explicit rule, not as verified live behavior).
- R6 — Entry/exit timing (adaptation 8): signal-bar-close decision; fills at the next bar's open market. Guards with single-unit book: flat→LONG fills on fresh flips only; LONG→FLAT closes the whole book at the next open; same-side refire is an explicit no-op. After any exit the next qualifying flip may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R7 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R8 — Position state: one 0.01-BTC spot unit max, long or flat, never short (short side explicitly disabled — adaptation 2). Safety orders: explicitly none.
- R9 — Warmup and gaps: flat until 120 completed `1d` bars (structural scale is 63 bars — inner windows full at bar 55, outer smoother at bar 61, SHULL displacement at bar 63 — plus researcher margin; probe shows first-eligible LONG on monotonic-up tape from the first post-warmup bar and 0 na remnants post-warmup). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold (volume never read: no volume-validity leg exists in this rule).
- R10 — Invariant identifier: `GH:Indie-script-64f0494|hullsuite-hma55_self-slope-2bar_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup120|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (fills, validity), `high`/`low`/`close` (validity; Hull reads `close` only). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 120 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing recursion; all eleven inputs are frozen). The `[2]` offset reads a past-confirmed value — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 — above the cycle-verified Binance spot BTCUSDT `MIN_NOTIONAL 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin (raw `hummingbot/VERSION` at `8b0e067e` reads `dev-2.17.0`, verified live this cycle); GitHub tree `HCH725/hummingbot@8b0e067e` verified live this cycle (commit resolves; verified ancestor of the local checkout `2dbc844`); `strategy_v2/controllers/controller_base.py:465` (`determine_executor_actions`), `strategy_v2/backtesting/` (`BacktestingDataProvider` over `CandlesFactory` spot feeds) and `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. No new execution primitive, no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned 103-line fence ships every adopted headline fact quoted in Provenance: the close/"Hma"/55/1.0/false inputs, the HMA/EHMA/THMA branch definitions, the `int(length*lengthMult)` effective length, the `useHtf`-gated HTF leg, the MHULL/SHULL two-bar displacement, the strict green-vs-red coloring with equality on red, and the two trend alarms. It ships zero orders, zero sizing, zero exits, and zero performance figures — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the disclosed HMA re-implementation (55/27/7 windows, self-slope state, equality-FLAT, na seeds, LONG-iff-slope-up state, next-open fills, 120-bar warmup), run in scratch (never committed):

- Live microstructure (Binance spot 1d klines fetched live this cycle, 3,365 completed bars 2017-08-17→2026-11-02, verified contiguous at 86400s steps with the still-forming current bar excluded by close-time, last completed close 76,816.00): 1,688 LONG / 1,557 FLAT post-warmup bars driving 76 books, holds 1–80 bars, 0 na bars post-warmup, 0 nonfinite closes (digest `2be069dacae21aa9`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 768.16 USDT notional at window close.
- Flat-tape branch probe (300 constant bars): 180/180 post-warmup flats hold FLAT — the equality-red rule is verified probe behavior on degenerate input.
- Slope-necessity probes: monotonic +0.1%/bar tape goes LONG from the first post-warmup bar; ±1 alternating tape prints 0 LONG bars post-warmup — the HMA(55) smoother absorbs micro-alternation, so unlike faster gates this state provably sits out tight chop (disclosed decoration boundary, carried into F3); monotonic-down tape sits slope-down → 0 LONG under the long-only pin.
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. Alarm-vs-state fenced: the source's trending-up/down `alertcondition(` edges fire on MHULL/SHULL crosses; this record governs the book by the *level* slope state instead (always defined, position-state complete) — the edge alarms are dropped, never silently substituted for entries.
3. Equality-red silence fenced: exact `HULL == HULL[2]` prints red; carrying it as FLAT is the source-faithful reading — an implementation promoting equality to carry-LONG prints a different event set, flagged as an implementation obligation, never silently interchangeable.
4. WMA-seeding silence fenced: na→available ramp transients (full availability from bar index 62) are absorbed by the 120-bar warmup; an implementation seeding WMAs differently must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
5. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
6. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (self-slope promotion, long-only pin, fixed sizing, disabled risk, 120-bar warmup, display/alarm drop, 0.1% cost overlay, next-open fills, once-per-bar evaluation); the HMA math, lengths, constants, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `HMA(55)` / `27-55-7` windows / strict two-bar self-slope / LONG-iff-slope-up / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 120-bar warmup are frozen.

- F1 — Length relevance: a length-89 twin (same rest, `44-89-9` windows) must not improve net expectancy; fail ⇒ the 55 swing-entry pin carries no edge over a slower Hull.
- F2 — Direction relevance: a two-sided twin (red-slope → SHORT with mirrored next-open handling, same rest) must not improve net expectancy; fail ⇒ the long-only pin discards the better half of the state.
- F3 — Smoother-necessity relevance: a Hull-dropped twin (LONG iff raw `close > close[2]`, same rest) must not improve net expectancy; fail ⇒ the HMA smoother was decoration on the two-bar close-momentum sign (the alternating-tape 0-LONG probe is the standing falsifier baseline).
- F4 — Warmup relevance: a 200-bar-warmup twin must print the identical post-200 event set; fail ⇒ seeding transients leak past the declared warmup.
- F5 — State relevance: a hold-time twin (flat exits delayed one extra bar, same entries) must not improve net expectancy; fail ⇒ the flip-close timing is decoration on the self-slope state.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — no venue-specific read at all). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- Single-asset port: the source is chart-agnostic indicator mathematics with no market evidence of any kind; BTCUSDT 1d self-slope behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No protective risk: the book carries no stop/target/trailing/time leg by declaration; the longest live-probe hold printed 80 bars — adverse excursions resolve only through the slope flip, disclosed as the coded trade.
- Seeding: nested-WMA ramp transients (full availability from bar index 62) are absorbed by the 120-bar warmup; an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Predicate strictness: the strict `>` slope with the equality-red-else-flat state is pinned exactly as coded; an implementation admitting equality as LONG prints a different event set — flagged, never silently interchangeable.
- Down-slope omission: sustained red-slope stretches (the monotonic-down probe's steady state) are deliberately unexploited by the long-only pin — disclosed opportunity cost, not hidden behavior.
- Chop exposure: the live window's shortest holds printed 1 bar — the state can flip on consecutive bars in sideways tape while slowerchop (alternating ±1) is absorbed; this is disclosed probe behavior, not a filtered regime.
- Licence: the canonical `.pinescript4` file carries no in-file licence grant naming this reuse; this record cites short literals only and reproduces no source block; research-only use asserted, no commercial claim.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- Primary implementation + pin: https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/Hull%20Suite%20by%20InSilico%20-%20Indie%20Edition/Hull%20Suite%20by%20InSilico%20-%20Indie%20Edition.pinescript4 (commit `64f0494a84273138b2e6a0f15821b18ba1616056`, 2026-10-08; blob `612880fb053eba3139c18c301c8651610f22c46c`; Pine v4 study, 103 lines / 2,262 bytes; raw sha256 `6471dbf892b9447a197064c762be0fec49234f1789dcc1d458adc4db53f2d0b7` verified live 2026-11-04; origin InSilico TV script — short-literal citation only)
- Same-pin context, existence only (not canonical, contents unadopted): other `.pinescript*` files at the same commit, including the screened-and-rejected OTT support-line port (same math as a `main` record), cRSI (fractional-offset semantics), and Madrid ribbon (missing leg) — none read for adoption, none adopted
- Exchange verification (fetched live 2026-11-04): Binance spot `api/v3/exchangeInfo` (BTCUSDT `TRADING`, spot allowed, `tickSize 0.01`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `NOTIONAL minNotional 5.0`) plus `api/v3/klines` 1d microstructure probes (3,365 completed contiguous bars 2017-08-17→2026-11-02, last completed close 76,816.00; 1,688 LONG / 1,557 FLAT bars → 76 books, holds 1–80, live digest `2be069dacae21aa9`; flat-tape 180/180 equality-holds; alternating-tape 0 LONG; monotonic-down 0 LONG)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (commit resolves live; raw `hummingbot/VERSION` reads `dev-2.17.0`; verified ancestor of local checkout `2dbc844`, `strategy_v2/controllers/controller_base.py:465`, `strategy_v2/backtesting/` provider + `executors_simulator/order_executor_simulator.py` all present, this cycle)
- Same-repo siblings (different mechanism, path evidence only): `github-indie-mavilimw-slope-sign-state-long-flat-btcusdt-1d-2026-11-04.md`, `github-indie-weis-wave-sign-state-long-flat-btcusdt-1d-2026-11-03.md`, `github-indie-vfi-vfima-sign-state-long-flat-btcusdt-1d-2026-11-03.md` on `main`
- Pine reference: v4 `study`/`input` causal semantics, `[2]` past-confirmed offsets, v4 integer division (`55/2=27`), `crossover` edge-alarm semantics; code-governs over prose throughout
