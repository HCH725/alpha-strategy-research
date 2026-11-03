---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: LazyBear Weis Wave Volume wave-sign-state long-flat on BTCUSDT 1d bars
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-04-18
sources:
  - https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/Weis%20Wave%20Volume/Weis%20Wave%20Volume.pinescript
  - https://www.tradingview.com/script/HFGx4ote-Indicator-Weis-Wave-Volume-LazyBear/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Weis Wave Volume wave-sign-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`** (2025-04-18, `Initial commit of Indie site`, verified via GitHub API this cycle), file **`indicators/Weis Wave Volume/Weis Wave Volume.pinescript`**, blob `5538e1fe69b75a8ff9f5878215a709dacc3fab33`, **919 bytes / 17 lines**, `study("Weis Wave Volume [LazyBear]", shorttitle="WWV_LB")` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `08b82076a6b97ccdd0aa4eddf67dfed44cc0c71e67e454ffc55065ab91fca067`, byte-identical to the working copy. Origin: LazyBear's open-source TradingView script `HFGx4ote` (Weis Wave Volume; the origin page returned HTTP 200 this cycle — short-literal citation only, page code never re-fetched, no source block reproduced).

**Order-affecting logic read verbatim (code governs; the study ships no orders):** `trendDetectionLength = input(2)`, `showDistributionBelowZero = input(false, type=bool)`; `mov = close>close[1] ? 1 : close<close[1] ? -1 : 0`; `trend = (mov != 0) and (mov != mov[1]) ? mov : nz(trend[1])`; `isTrending = rising(close, trendDetectionLength) or falling(close, trendDetectionLength)`; `wave = (trend != nz(wave[1])) and isTrending ? trend : nz(wave[1])`; `vol = wave==wave[1] ? (nz(vol[1])+volume) : volume`; `up = wave == 1 ? vol : 0`; `dn` display split (governed by `showDistributionBelowZero`, display-only).

**Pine-block census (17-line fence):** 1 `study(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 2 `input(` (2 / false — both fenced at defaults); 0 `request.` / 0 `security(` / 0 `timeframe.*` / 0 `barstate.*`; 2 unconditional `plot(` histogram legs (up/dn) — all display-only, dropped, disclosed.

**Same-commit siblings (existence only, not canonical):** `Weis Wave Volume.indie4` (1,936 bytes) and `Weis Wave Volume.indie5` (1,922 bytes) sit beside the `.pinescript` at the same commit. Their contents were not read line-by-line and no literal is adopted from them — every pinned literal below comes from the 919-byte `.pinescript` fence.

**Structural facts carried over exactly:** (a) direction-persistence detector — the running `trend` flips only on a nonzero close-vs-prior-close sign change and otherwise carries; (b) 2-bar persistence gate — a new `wave` is accepted only when `rising(close,2) or falling(close,2)` confirms the move, otherwise the prior wave carries (chop prints no new wave); (c) per-wave volume accumulation that resets to the current bar's volume on every wave flip (accumulation is display-only, never a predicate); (d) no MTF, no session/timezone, no intrabar semantics anywhere.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the wave-sign state to long-flat entries/exits on completed bars (`wave==+1` → LONG, anything else — `-1` or the `0` seed — → FLAT, disclosed promotion); (2) long-only pin with the short side explicitly disabled (the construction is signed; the down-wave leg is a deliberate omission, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at probe last completed close 76,816.00, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 50-bar warmup with pre-warmup bars flat (structural scale is ~3 bars — sign persistence plus the 2-bar gate — plus researcher margin); (6) display drop (both histogram legs and the `showDistributionBelowZero` split, fenced at `false`); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (no confirmed-close flag ships in source, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-008ef56|wwv-tdl2_wave-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup50|2026-11-03`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-03):** working-tree base is current `main@31eb5dfd` (541 root strategy records, READMEs excluded, all `hb_ready_status: PASS` re-verified this cycle). Case-insensitive content searches for `weis`, `wwv_lb`, `trendDetectionLength`, `showDistributionBelowZero`, `HFGx4ote`, `wave==1` return zero hits; the single `isTrending` hit is an unrelated FMZ record's own dedup paragraph naming its own search term, not this construction. `wave` prose hits name unrelated objects (Elliott-wave, FMZ WaveFinder pivots, passing English). All 16 open `research/*` PRs enumerated by number/title/branch (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725) — none is this file, author, or construction. Five-axis distinction vs nearest pool neighbors: different source file and math vs `forven-obv-ema` (unbounded cumulative OBV, no wave reset), `klinger-volume-oscillator` (dual-EMA volume force, no persistence gate), `pvo-signal-cross` (pure-volume EMA ratio, no price-direction state), `github-indie-vfi-vfima-sign-state` (dispersion-gated money-flow sign over 130 bars, no wave reset), and `fmz-432808-wavefinder-vmacd-stochrsi` (different FMZ source and pivot-based construction) — no duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Weis Wave Volume (Weis method via LazyBear): volume is accumulated into directional waves so that each wave's printed size reflects sustained buying/selling pressure rather than per-bar prints; waves restart when price direction persistence breaks and re-confirms — the author's display frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool cumulative-t tape readers (OBV's unbounded sum, Klinger's dual-EMA force, PVO's volume-only ratio, VFI's dispersion-gated 130-bar accumulation), this machine segments the tape into confirmed directional waves and resets accumulation at every flip — the state reacts to *whether price has just proven a 2-bar persistent move*, not to how much volume printed. Unlike pool price-slope states (EMA crosses,Donchian breakouts), the trigger is a discrete sign flip *gated* by persistence, so single-bar wicks and dojis can never start a wave by themselves. The bet, as derived, is purely that this gated wave sign ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Direction persistence (source formulas, pinned): `mov[t] = +1` iff `C[t] > C[t−1]`, `−1` iff `C[t] < C[t−1]`, else `0` (no prior close at the first bar — pinned seed, absorbed by warmup); `trend[t] = mov[t]` iff `mov[t] != 0` and `mov[t] != nz(mov[t−1])`, else `nz(trend[t−1])` (`nz` maps na to 0 — pinned researcher reading of the seed transient, disclosed).
- R3 — Persistence gate and wave (source formulas, pinned): `rising[t] = C[t] > C[t−1] and C[t] > C[t−2]`, `falling[t] = C[t] < C[t−1] and C[t] < C[t−2]` (Pine v3 `rising`/`falling` strict-greater-than-any-prior-bar reading for length 2 — pinned researcher reading, disclosed); `isTrending[t] = rising[t] or falling[t]`; `wave[t] = trend[t]` iff `trend[t] != nz(wave[t−1])` and `isTrending[t]`, else `nz(wave[t−1])`.
- R4 — Display drop (adaptation 6): `vol` accumulation and both `plot(` histogram legs (`up`/`dn`, `showDistributionBelowZero=false` fence) never enter any predicate.
- R5 — State (promoted predicate, adaptation 1): `LONG[t]` iff `wave[t] == +1`; `FLAT[t]` otherwise (covers `−1` and the `0` seed — flat-tape probe: 250/250 post-warmup zeros hold FLAT; live window printed 0 seed occurrences post-warmup — carried as an explicit rule, not as verified live behavior).
- R6 — Entry/exit timing (adaptation 8): signal-bar-close decision; fills at the next bar's open market. Guards with single-unit book: flat→LONG fills on fresh flips only; LONG→FLAT closes the whole book at the next open; same-side refire is an explicit no-op. After any exit the next qualifying flip may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R7 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R8 — Position state: one 0.01-BTC spot unit max, long or flat, never short (short side explicitly disabled — adaptation 2). Safety orders: explicitly none.
- R9 — Warmup and gaps: flat until 50 completed `1d` bars (structural scale is ~3 bars — persistence plus the 2-bar gate; probe shows monotonic-up LONG from bar index 2 and 0 seed remnants post-warmup). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC or `V < 0`, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals — explicit hold.
- R10 — Invariant identifier: `GH:Indie-script-008ef56|wwv-tdl2_wave-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup50|2026-11-03` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (fills, validity), `high`/`low`/`close` (persistence, gate, validity), `volume` in base asset (display-only accumulation — every predicate use is price-derived; no quote-volume conversion exists in this rule). No funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 50 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing recursion; the two inputs are frozen). The `[1]`/`[2]` offsets read past-confirmed values — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 — above the cycle-verified Binance spot BTCUSDT `MIN_NOTIONAL 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: one single-unit long-flat book; re-entry after any exit is explicitly allowed on the next qualifying flip with no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.
- Pinned-engine path (re-verified against local checkout `2dbc844` this cycle, `hummingbot/VERSION=2.17.0`; pinned source `8b0e067e80ab62f10846d518dcb5a8218527ddb3` verified an ancestor of this checkout via `merge-base --is-ancestor`): `data_feed/candles_feed/binance_spot_candles/constants.py` carries the spot `1d` interval; `strategy_v2/backtesting/backtesting_engine_base.py:run_backtesting` iterates completed rows and calls `controller.determine_executor_actions()` (`strategy_v2/controllers/controller_base.py:465`, verified this cycle) feeding completed-row windows into `simulate_executor`; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET at the first window row (`fill_timestamp = df_filtered['timestamp'].iloc[0]` — verified this cycle). Hence a completed-bar-`s` decision fills at the next row's open in the next-open lane — the coded timing. The persistence/gate/wave arithmetic is deterministic controller logic over completed klines; no external feed is required. A strategy-specific, not-yet-implemented controller child must compute exactly R2–R9; the generic executor does not calculate the strategy. Sibling PASS records are path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 17-line fence ships every adopted headline fact quoted in Provenance: the 2/false inputs, the close-vs-prior sign persistence, the `rising`/`falling` 2-bar gate, the gated wave flip with carry, and the per-wave volume accumulation with its reset. It ships zero orders, zero sizing, zero exits, and zero performance figures — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the disclosed wave re-implementation (sign persistence, 2-bar strict gate, `nz` seeds, wave carry, reset accumulation, LONG-iff-+1 state, next-open fills, 50-bar warmup), run in scratch (never committed):

- Live microstructure (Binance spot 1d klines fetched live this cycle, 3,365 completed bars 2017-08-17→2026-11-02, verified contiguous at 86400s steps with the still-forming current bar excluded by close-time, last completed close 76,816.00): 1,741 LONG / 1,574 FLAT post-warmup bars driving 473 books, holds 1–21 bars, 0 seed-zero bars post-warmup, 0 nonfinite closes, 0 negative volumes (digest `84f5682bc213520a`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 768.16 USDT notional at window close.
- Flat-tape branch probe (300 constant bars): 250/250 post-warmup `wave == 0` holds → all FLAT, the `0`-seed rule is verified probe behavior on degenerate input (live tape printed 0 occurrences, disclosed).
- Gate-necessity probes: monotonic +0.1%/bar tape goes LONG from bar index 2; ±1 alternating tape never satisfies the 2-bar gate (0 LONG bars — single-bar flicker provably cannot start a wave); monotonic-down tape sits at `wave == −1` → FLAT under the long-only pin; a 100× volume spike inside an up-wave changes only display accumulation, never the state.
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. Gate-reading fenced: the probe implements Pine v3 `rising`/`falling` as strict greater/less-than over both prior bars; a `>=`/`<=` reading would admit doji touches and print a different event set — the strict reading is pinned in R3, never silently interchangeable.
3. `nz`-seed silence fenced: na→0 seed transients are absorbed by the 50-bar warmup (first LONG on trending tape prints at bar index 2; flat tape never leaves 0); an implementation seeding differently must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
4. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
5. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (wave-sign promotion, long-only pin, fixed sizing, disabled risk, 50-bar warmup, display drop, 0.1% cost overlay, next-open fills, once-per-bar evaluation); the persistence math, gate, constants, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `trendDetectionLength 2` / strict 2-bar gate / wave-carry / LONG-iff-+1 / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 50-bar warmup are frozen.

- F1 — Gate-length relevance: a `trendDetectionLength`-4 twin (same rest) must not improve net expectancy; fail ⇒ the 2-bar persistence pin carries no edge over a slower gate.
- F2 — Direction relevance: a two-sided twin (`wave==-1` → SHORT with mirrored next-open handling, same rest) must not improve net expectancy; fail ⇒ the long-only pin discards the better half of the state.
- F3 — Gate-necessity relevance: a gate-dropped twin (wave follows every persistence flip without the `rising`/`falling` confirmation, same rest) must not improve net expectancy; fail ⇒ the persistence gate was decoration on the sign detector.
- F4 — Warmup relevance: a 150-bar-warmup twin must print the identical post-150 event set; fail ⇒ seeding transients leak past the declared warmup.
- F5 — State relevance: a hold-time twin (flat exits delayed one extra bar, same entries) must not improve net expectancy; fail ⇒ the flip-close timing is decoration on the wave-sign state.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; volume read in base asset for display-only accumulation — no venue-specific read). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- Single-asset port: the source is chart-agnostic indicator mathematics with no market evidence of any kind; BTCUSDT 1d wave-sign behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No protective risk: the book carries no stop/target/trailing/time leg by declaration; the longest live-probe hold printed 21 bars — adverse excursions resolve only through the wave flip, disclosed as the coded trade.
- Seeding: `nz` na→0 transients are absorbed by the 50-bar warmup; an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Predicate strictness: the strict `>`/`<` gate with the `wave==+1`-else-flat state is pinned exactly as coded; an implementation admitting equality touches prints a different event set — flagged, never silently interchangeable.
- Down-wave omission: sustained down-waves (`wave == −1`, the monotonic-down probe's steady state) are deliberately unexploited by the long-only pin — disclosed opportunity cost, not hidden behavior.
- Licence: the canonical `.pinescript` carries an education-purposes header with no licence grant and the TV origin page marks the script open-source subject to house rules — this record cites short literals only and reproduces no source block; research-only use asserted, no commercial claim.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- Primary implementation + pin: https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/Weis%20Wave%20Volume/Weis%20Wave%20Volume.pinescript (commit `008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`, 2025-04-18; blob `5538e1fe69b75a8ff9f5878215a709dacc3fab33`; Pine study, 17 lines / 919 bytes; raw sha256 `08b82076a6b97ccdd0aa4eddf67dfed44cc0c71e67e454ffc55065ab91fca067` verified live 2026-11-03; origin LazyBear TV script `HFGx4ote` — short-literal citation only)
- Same-commit siblings, existence only (not canonical, contents unread): `Weis Wave Volume.indie4` (1,936 bytes), `Weis Wave Volume.indie5` (1,922 bytes)
- Exchange verification (fetched live 2026-11-03): Binance spot `api/v3/exchangeInfo` (BTCUSDT `TRADING`, spot allowed, `tickSize 0.01`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `NOTIONAL minNotional 5.0`) plus `api/v3/klines` 1d microstructure probes (3,365 completed contiguous bars 2017-08-17→2026-11-02, last completed close 76,816.00; 1,741 LONG / 1,574 FLAT bars → 473 books, holds 1–21, live digest `84f5682bc213520a`; flat-tape 250/250 zero-holds; alternating-tape 0 LONG; monotonic-down steady `wave −1`)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (verified ancestor of local checkout `2dbc844`, `hummingbot/VERSION=2.17.0`, this cycle)
- Same-repo siblings (different mechanism, path evidence only): `github-indie-vfi-vfima-sign-state-long-flat-btcusdt-1d-2026-11-03.md`, `github-indie-andean-envelope-dispersion-sign-state-long-flat-btcusdt-1d-2026-11-03.md` on `main`
- Pine reference: v3 `study`/`input` causal semantics, `nz` na→0, strict `rising`/`falling` over trailing bars, `[1]`/`[2]` past-confirmed offsets; code-governs over prose throughout
