---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Indie Kivanc MavilimW WMA-cascade slope-sign-state long-flat on BTCUSDT 1d bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/MavilimW%20(Fibonacci%20WMA%20Cascade)/MavilimW%20(Fibonacci%20WMA%20Cascade).pinescript4
  - https://www.tradingview.com/script/IAssyObN-MavilimW/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MavilimW WMA-cascade slope-sign-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`64f0494a84273138b2e6a0f15821b18ba1616056`** (2026-10-08, `Add 60 community MIT/MPL indicators from TakeProfit with guides`, verified via GitHub API this cycle), file **`indicators/MavilimW (Fibonacci WMA Cascade)/MavilimW (Fibonacci WMA Cascade).pinescript4`**, blob `cd2b0809cce890c75c7ab4267694ba553610994e`, **1,105 bytes / 73 lines**, `study("MavilimW", overlay=true)` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `46c366f7eba4828af21aaf5c69ae0cc2eef0e3dea9bc7bc625d825f606784443`, byte-identical to the working copy. Origin: Kivanc Ozbilgic's open-source TradingView script `IAssyObN` (MavilimW; the origin page returned HTTP 200 this cycle — short-literal citation only, page code never re-fetched, no source block reproduced; its description confirms the two Blue/Red trend colors, sensitivity via the first two parameters, the previous-version toggle, and the automatic Fibonacci-series construction).

**Order-affecting logic read verbatim (code governs; the study ships no orders):** `mavilimold = input(false)`; `fmal = input(3)`; `smal = input(5)`; auto-derived lengths `tmal = fmal+smal` (8), `Fmal = smal+tmal` (13), `Ftmal = tmal+Fmal` (21), `Smal = Fmal+Ftmal` (34); six-deep WMA cascade `M1 = wma(close, fmal)`, `M2 = wma(M1, smal)`, `M3 = wma(M2, tmal)`, `M4 = wma(M3, Fmal)`, `M5 = wma(M4, Ftmal)`, `MAVW = wma(M5, Smal)`; slope coloring `col1 = MAVW > MAVW[1]` (blue), `col3 = MAVW < MAVW[1]` (red), else yellow (flat); three `alertcondition(` edge alarms (`crossover(MAVW, MAVW[1])` BUY, `crossunder(MAVW, MAVW[1])` SELL, `cross(MAVW, MAVW[1])` color alarm) — alarms only, never orders.

**Pine-block census (73-line fence):** 1 `study(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 3 `input(` (false / 3 / 5 — all fenced at defaults); 0 `request.` / 0 `security(` / 0 `timeframe.*` / 0 `barstate.*`; 2 `plot(` legs (MAVW line plus the `mavilimold`-gated old-version leg, fenced off at `false`) — all display-only, dropped, disclosed; 3 `alertcondition(` alarms — display/alarm-only, dropped, disclosed.

**Structural facts carried over exactly:** (a) Fibonacci WMA cascade — six nested `wma` smoothings with auto-derived lengths 3→5→8→13→21→34, so the published line is a deeply smoothed close derivative, never raw price; (b) slope-sign coloring — the state is the strict one-bar comparison `MAVW > MAVW[1]` / `<`, with exact equality printing the third (yellow) color; (c) previous-version leg exists only behind the `mavilimold` toggle fenced at `false` — never evaluated, disclosed; (d) no MTF, no session/timezone, no intrabar semantics, no volume read anywhere (every predicate is close-derived).

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the slope-sign state to long-flat entries/exits on completed bars (`MAVW > MAVW[1]` → LONG, anything else — slope-down red, yellow flat equality, na seeds — → FLAT, disclosed promotion; the level state, not the edge alarms, governs so the book is always defined); (2) long-only pin with the short side explicitly disabled (the construction is signed; the red-slope leg is a deliberate omission, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at probe last completed close 76,816.00, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 120-bar warmup with pre-warmup bars flat (structural scale is 78 bars — 2+4+7+12+20+33 bar ramp across the six cascade stages — plus researcher margin); (6) display drop (both plot legs, the three colors except as the predicate, the three alarms, and the fenced old-version leg); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (no confirmed-close flag ships in source, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-64f0494|mavilimw-wma3-5-8-13-21-34_slope-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup120|2026-11-04`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@57395399` (542 root strategy records, READMEs excluded). Case-insensitive content searches for `mavilim`, `MAVW`, `MavilimW`, `Fibonacci WMA` return zero hits; no open `research/*` PR is this file, author construction, or signal (17 open PRs enumerated by number/title/branch — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding). Five-axis distinction vs nearest pool neighbors: different source file and math vs `super-guppy-ema-stack` (EMA-stack alignment, no WMA cascade, no slope-sign state), `hull-ema-crossover-reversal` (single HMA-vs-EMA cross, not a six-deep cascade), `fmz-tema7-single-level-trend` (TEMA level, different smoother), `alphatrend-mfi-atr-trailing-reversal` (same Kivanc authorship, different AlphaTrend MFI+ATR construction), and `pmax-profit-maximizer-ma-cross-flip` (same Kivanc authorship, different MA+ATR-band construction) — no duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

MavilimW (via Kivanc Ozbilgic, after @mavilim0732): smoothed weighted-moving-average combinations of Fibonacci numbers plot a slow support/resistance line for longer-term trading and confirmation — blue for uptrend, red for downtrend; raising the first two parameters desensitizes the line toward support/resistance use, lowering them sensitizes buy/sell color flips. The author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool cross machines (HMA/EMA/TEMA crosses that fire on line-over-line penetration) and unlike pool stack machines (Guppy/ribbon alignment that requires several lines to agree), this machine watches a *single* deeply smoothed line and trades only its own one-bar slope sign — the trigger is whether the 84-bar-deep Fibonacci WMA cascade ticked up on the just-completed bar, not whether price sits above any average or whether fast/slow lines crossed. Unlike pool oscillator states (RSI/CCI/Stoch recrosses of fixed thresholds), there is no threshold at all — the predicate is purely ordinal. The bet, as derived, is purely that this cascade-slope sign ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Cascade (source formulas, pinned): `fmal=3`, `smal=5`, `tmal=8`, `Fmal=13`, `Ftmal=21`, `Smal=34`; `M1[t]=wma(close,3)`, `M2[t]=wma(M1,5)`, `M3[t]=wma(M2,8)`, `M4[t]=wma(M3,13)`, `M5[t]=wma(M4,21)`, `MAVW[t]=wma(M5,34)` (Pine-built-in trailing-WMA reading — na until each stage's full length; seeds absorbed by warmup, disclosed researcher reading).
- R3 — Slope-sign state (source predicate, pinned): `UP[t]` iff `MAVW[t] > MAVW[t-1]` (the blue leg); `DOWN[t]` iff `MAVW[t] < MAVW[t-1]` (the red leg); exact equality is the yellow leg — carried as FLAT, never LONG (pinned conservatism, disclosed).
- R4 — Display/alarm drop (adaptation 6): both `plot(` legs, the three colors except as the R3 predicate, the `mavilimold=false` old-version leg, and all three `alertcondition(` alarms never enter any predicate.
- R5 — State (promoted predicate, adaptation 1): `LONG[t]` iff `UP[t]`; `FLAT[t]` otherwise (covers red slope, yellow equality, and na seeds — flat-tape probe: 180/180 post-warmup flats hold FLAT; live window printed 0 na post-warmup — carried as an explicit rule, not as verified live behavior).
- R6 — Entry/exit timing (adaptation 8): signal-bar-close decision; fills at the next bar's open market. Guards with single-unit book: flat→LONG fills on fresh flips only; LONG→FLAT closes the whole book at the next open; same-side refire is an explicit no-op. After any exit the next qualifying flip may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R7 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R8 — Position state: one 0.01-BTC spot unit max, long or flat, never short (short side explicitly disabled — adaptation 2). Safety orders: explicitly none.
- R9 — Warmup and gaps: flat until 120 completed `1d` bars (structural scale is 78 bars — cascade ramp — plus researcher margin; probe shows first eligible LONG at the first post-warmup bar on monotonic-up tape and 0 na remnants post-warmup). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC is invalid for signals — explicit hold (volume never read: no volume-validity leg exists in this rule).
- R10 — Invariant identifier: `GH:Indie-script-64f0494|mavilimw-wma3-5-8-13-21-34_slope-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup120|2026-11-04` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (fills, validity), `high`/`low`/`close` (validity; cascade reads `close` only). No volume read exists in this rule; no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 120 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing recursion; the three inputs are frozen). The `[1]` offsets read past-confirmed values — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 — above the cycle-verified Binance spot BTCUSDT `MIN_NOTIONAL 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Pinned-engine path (bounded model, inspected this cycle — capability check, not implementation): Hummingbot package `20260920` / `VERSION dev-2.17.0` per the README pin; GitHub tree `HCH725/hummingbot@8b0e067e` verified live this cycle (commit resolves; raw `hummingbot/VERSION` reads `dev-2.17.0`), and verified as an ancestor of the local checkout `2dbc844`; `strategy_v2/controllers/controller_base.py:465` (`determine_executor_actions`), `strategy_v2/backtesting/` (`BacktestingDataProvider` over `CandlesFactory` spot feeds) and `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` all present — the single-TF spot-1d close-decided / next-open-market path is the same bounded route prior PASS records use. No new execution primitive, no new data requirement, no representative-capability validation owed.

## Evidence

### Source-reported

The pinned 73-line fence ships every adopted headline fact quoted in Provenance: the false/3/5 inputs, the auto-derived 8/13/21/34 Fibonacci lengths, the six-deep WMA cascade, the strict slope-sign coloring with the yellow equality leg, and the fenced old-version toggle. It ships zero orders, zero sizing, zero exits, and zero performance figures — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the disclosed cascade re-implementation (auto-derived lengths, six-stage WMA ramp, slope-sign state, yellow-equality FLAT, na seeds, LONG-iff-slope-up state, next-open fills, 120-bar warmup), run in scratch (never committed):

- Live microstructure (Binance spot 1d klines fetched live this cycle, 3,365 completed bars 2017-08-17→2026-11-02, verified contiguous at 86400s steps with the still-forming current bar excluded by close-time, last completed close 76,816.00): 1,788 LONG / 1,457 FLAT post-warmup bars driving 34 books, holds 13–204 bars, 0 na bars post-warmup, 0 nonfinite closes, 0 negative volumes (digest `5f1b79039cde643a`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 768.16 USDT notional at window close.
- Flat-tape branch probe (300 constant bars): 180/180 post-warmup flats hold FLAT — the yellow-equality rule is verified probe behavior on degenerate input (live tape printed slope equality only on flats, disclosed).
- Slope-necessity probes: monotonic +0.1%/bar tape goes LONG from the first post-warmup bar; ±1 alternating tape still prints 90 LONG bars post-warmup — the 78-bar cascade integrates fast alternation into slow drift, so unlike a 2-bar gate this state provably *can* sit LONG through chop (disclosed decoration boundary, carried into F3); monotonic-down tape sits slope-down → 0 LONG under the long-only pin.
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. Alarm-vs-state fenced: the source's BUY/SELL `alertcondition(` edges fire on slope flips; this record governs the book by the *level* slope state instead (always defined, position-state complete) — the edge alarms are dropped, never silently substituted for entries.
3. Yellow-equality silence fenced: exact `MAVW == MAVW[1]` prints the third color; carrying it as FLAT is the pinned conservative reading — an implementation promoting equality to carry-LONG prints a different event set, flagged as an implementation obligation, never silently interchangeable.
4. WMA-seeding silence fenced: na→available ramp transients across the six stages (full availability from bar index 78) are absorbed by the 120-bar warmup; an implementation seeding WMAs differently must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
5. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
6. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (slope-sign promotion, long-only pin, fixed sizing, disabled risk, 120-bar warmup, display/alarm drop, 0.1% cost overlay, next-open fills, once-per-bar evaluation); the cascade math, lengths, constants, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `fmal 3 / smal 5` / auto-derived 8/13/21/34 cascade / strict slope-sign / LONG-iff-slope-up / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 120-bar warmup are frozen.

- F1 — Length relevance: a `(5, 8)`-seed twin (same rest, auto-derived 13/21/34/55 cascade) must not improve net expectancy; fail ⇒ the (3, 5) sensitivity pin carries no edge over a slower cascade.
- F2 — Direction relevance: a two-sided twin (red-slope → SHORT with mirrored next-open handling, same rest) must not improve net expectancy; fail ⇒ the long-only pin discards the better half of the state.
- F3 — Cascade-necessity relevance: a cascade-dropped twin (LONG iff raw `close > close[1]`, same rest) must not improve net expectancy; fail ⇒ the six-deep smoother was decoration on the close-momentum sign (the alternating-tape 90-LONG probe is the standing falsifier baseline).
- F4 — Warmup relevance: a 200-bar-warmup twin must print the identical post-200 event set; fail ⇒ seeding transients leak past the declared warmup.
- F5 — State relevance: a hold-time twin (flat exits delayed one extra bar, same entries) must not improve net expectancy; fail ⇒ the flip-close timing is decoration on the slope-sign state.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no volume read — no venue-specific read at all). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- Single-asset port: the source is chart-agnostic indicator mathematics with no market evidence of any kind; BTCUSDT 1d cascade-slope behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No protective risk: the book carries no stop/target/trailing/time leg by declaration; the longest live-probe hold printed 204 bars — adverse excursions resolve only through the slope flip, disclosed as the coded trade.
- Seeding: six-stage WMA ramp transients (full availability from bar index 78) are absorbed by the 120-bar warmup; an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Predicate strictness: the strict `>` slope with the yellow-equality-else-flat state is pinned exactly as coded; an implementation admitting equality as LONG prints a different event set — flagged, never silently interchangeable.
- Down-slope omission: sustained red-slope stretches (the monotonic-down probe's steady state) are deliberately unexploited by the long-only pin — disclosed opportunity cost, not hidden behavior.
- Chop exposure: the alternating-tape probe prints 90 LONG bars — the deep cascade can sit LONG through fast chop while it integrates drift; this is disclosed probe behavior, not a filtered regime.
- Licence: the canonical `.pinescript4` header credits the Twitter author and the porter with no explicit licence grant in-file; the landing commit message describes the batch as community MIT/MPL additions — this record cites short literals only and reproduces no source block; research-only use asserted, no commercial claim.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- Primary implementation + pin: https://github.com/Indie-script/indie-script.github.io/blob/64f0494a84273138b2e6a0f15821b18ba1616056/indicators/MavilimW%20(Fibonacci%20WMA%20Cascade)/MavilimW%20(Fibonacci%20WMA%20Cascade).pinescript4 (commit `64f0494a84273138b2e6a0f15821b18ba1616056`, 2026-10-08; blob `cd2b0809cce890c75c7ab4267694ba553610994e`; Pine v4 study, 73 lines / 1,105 bytes; raw sha256 `46c366f7eba4828af21aaf5c69ae0cc2eef0e3dea9bc7bc625d825f606784443` verified live 2026-11-04; origin Kivanc Ozbilgic TV script `IAssyObN` — short-literal citation only)
- Same-pin context, existence only (not canonical, contents unread except the two rejected screenings): 40 `.pinescript*` files at the same commit; `Squeeze Momentum.pinescript` and `Volume Flow Indicator.pinescript` already ported on `main`, `Ultimate MA - MultiTF.pinescript` MTF-rejected in a prior cycle, `Andean Oscillator.pinescript5` same family as an existing record — none read, none adopted
- Exchange verification (fetched live 2026-11-04): Binance spot `api/v3/exchangeInfo` (BTCUSDT `TRADING`, spot allowed, `tickSize 0.01`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `NOTIONAL minNotional 5.0`) plus `api/v3/klines` 1d microstructure probes (3,365 completed contiguous bars 2017-08-17→2026-11-02, last completed close 76,816.00; 1,788 LONG / 1,457 FLAT bars → 34 books, holds 13–204, live digest `5f1b79039cde643a`; flat-tape 180/180 equality-holds; alternating-tape 90 LONG; monotonic-down 0 LONG)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (commit resolves live; raw `hummingbot/VERSION` reads `dev-2.17.0`; verified ancestor of local checkout `2dbc844`, `strategy_v2/controllers/controller_base.py:465`, `strategy_v2/backtesting/` provider + `executors_simulator/order_executor_simulator.py` all present, this cycle)
- Same-repo siblings (different mechanism, path evidence only): `github-indie-weis-wave-sign-state-long-flat-btcusdt-1d-2026-11-03.md`, `github-indie-vfi-vfima-sign-state-long-flat-btcusdt-1d-2026-11-03.md`, `github-indie-andean-envelope-dispersion-sign-state-long-flat-btcusdt-1d-2026-11-03.md` on `main`
- Pine reference: v4 `study`/`input` causal semantics, `[1]` past-confirmed offsets, `crossover`/`crossunder` edge-alarm semantics; code-governs over prose throughout
