---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Indie Andean bull-bear envelope-dispersion sign-state long-flat on BTCUSDT 1d bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/Andean%20Oscillator/Andean%20Oscillator.pinescript5
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Andean bull-bear envelope-dispersion sign-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`** (2025-04-18, `Initial commit of Indie site`, verified via GitHub API this cycle), file **`indicators/Andean Oscillator/Andean Oscillator.pinescript5`**, blob `2656f52cab18c7d5907522c513ba72d34cf81b46`, **1,670 bytes / 48 lines**, Pine v5, `indicator("Andean Oscillator")` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `7f41fb65b97256f808406ad36cf53afbda1329b353f5416c5f908029faa34f56`, byte-identical to the working copy. Permalink above. File header: `© alexgrover`, CC BY-NC-SA 4.0, original post `Alpaca.markets/learn/andean-oscillator-a-new-technical-indicator-based-on-an-online-algorithm-for-trend-analysis/` — short-literal citation only, no source block reproduced.

**Order-affecting logic read verbatim (code governs; indicator ships no orders):** `length = input(50)`, `sig_length = input(9, 'Signal Length')`; `var alpha = 2/(length+1)` (frozen once at bar 0: `2/51`); `var up1 = 0., var up2 = 0., var dn1 = 0., var dn2 = 0.`; `C = close, O = open`; `up1 := nz(math.max(C, O, up1[1] - (up1[1] - C) * alpha), C)`; `up2 := nz(math.max(C*C, O*O, up2[1] - (up2[1] - C*C) * alpha), C*C)`; `dn1 := nz(math.min(C, O, dn1[1] + (C - dn1[1]) * alpha), C)`; `dn2 := nz(math.min(C*C, O*O, dn2[1] + (C*C - dn2[1]) * alpha), C*C)`; components `bull = math.sqrt(dn2 - dn1*dn1)`, `bear = math.sqrt(up2 - up1*up1)`; `signal = ta.ema(math.max(bull, bear), sig_length)`. Bar-0 seeding is pinned by `nz(na, C)`: `up1/dn1 = C₀`, `up2/dn2 = C₀²` — explicit, never a free choice.

**Pine-block census (48-line fence):** 1 `indicator(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 2 `input(` (50 / 9 — both fenced at defaults); 0 `request.` / 0 `security(` / 0 `timeframe.*` / 0 `barstate.isconfirmed` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` — all recorded as absent, never filled in. All three `plot(` calls (Bullish/Bearish/Signal) are display-only — dropped, disclosed.

**Structural facts carried over exactly:** (a) exponential price envelopes with same-side clamps (`max` up / `min` down) on both price and price-squared with shared `α = 2/51`; (b) bull/bear are envelope dispersions (sqrt of squared-envelope minus squared level-envelope); (c) the `signal` EMA(9) leg is a display smoother, never a trigger — dropped, disclosed; (d) no MTF, no session/timezone, no intrabar/magnifier semantics anywhere.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the bull/bear sign state to long-flat entries/exits on completed bars (`bull>bear` → LONG, `bull<bear` → FLAT, exact equality holds prior state — disclosed promotion, same strict semantics); (2) long-only pin with the short side explicitly disabled (the construction is symmetric; the short leg is a deliberate omission, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at probe last completed close 76,816.00, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 300-bar warmup with pre-warmup bars flat (length-50 structural scale plus researcher margin; seed-convergence verified below); (6) display drop (all plots plus the signal EMA9 leg); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (no `isconfirmed` ships in source, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-008ef56|andean-L50_a2/51_bullbear-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup300|2026-11-03`. Changing any formula, length, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-03):** working-tree base is current `main@2fa2ac55` (539 root strategy records, READMEs excluded). Case-insensitive content searches for `andean`, `alexgrover`, `2656f52`, `andean-oscillator`, `bull-bear dispersion`, `envelope-dispersion`, and `bullish component` return zero same-source/same-construction hits; `bearish component` returns one unrelated record (`tradingview-lukeiceman-rsi30-sma50-macd-stoch-quadcross` — generic English prose about its own RSI/MACD legs, no Andean leg). All 17 open `research/*` PRs enumerated by number/title/branch (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725) — none is this file, author, or construction. Five-axis distinction vs the same-repo Kalman record (`github-indie-kalman-...-2026-11-02.md`, merged): different source file and math (Kalman R/Q recursion vs price/price-squared exponential envelopes), different signal (dual-filter cross vs single bull/bear sign state), different risk (latched 2%/4% box vs explicit no-box signal exits), different market/TF/direction (futures 4h two-sided vs spot 1d long-flat), different warmup basis — no duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

Online trend dispersion: two exponential envelopes track price from above and below on both the level and the squared scale; the gap between each envelope pair (its dispersion) measures how far price has stretched from its own adaptive track. Bull-side dispersion dominating means downside deviation is running hotter than upside deviation — the author's trend-reading frame, never adopted as a crypto claim.

### Research interpretation

Unlike pool oscillator sign-state records (RSI/ROC/CMF threshold or zero signs over fixed lookback windows), this machine has no window, no threshold, and no normalization — the state is a pure sign comparison of two recursively defined dispersions with a single frozen `α`. Unlike the same-repo Kalman sibling (adaptive-gain smoothers whose lengths set noise scaling), the Andean envelopes clamp to each bar's open/close, so the state reacts to range structure, not just close displacement. The bet, as derived, is purely that this clamp-plus-dispersion sign state ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Envelopes (source recursion, pinned): `α = 2/51`; `up1[t] = max(C[t], O[t], (1−α)·up1[t−1] + α·C[t])`; `up2[t] = max(C[t]², O[t]², (1−α)·up2[t−1] + α·C[t]²)`; `dn1/dn2` mirrored with `min`; bar-0 seed `up1/dn1 = C[0]`, `up2/dn2 = C[0]²` (Pine `nz` semantics — pinned).
- R3 — Components (source formulas, pinned): `bull[t] = sqrt(dn2[t] − dn1[t]²)`, `bear[t] = sqrt(up2[t] − up1[t]²)`. For strictly positive prices the radicands are structurally non-negative (squared-envelope Jensen plus same-side clamp, by induction from the bar-0 seed); the float guard below never fired — fenced, never traded around.
- R4 — Display drop (adaptation 6): the `signal = EMA(max(bull,bear), 9)` leg is plot-only and never enters any predicate.
- R5 — State (promoted predicate, adaptation 1): `LONG[t]` iff `bull[t] > bear[t]`; `FLAT[t]` iff `bull[t] < bear[t]`; exact equality holds the prior state (0 occurrences across all probes this cycle — carried as an explicit hold, not as verified behavior).
- R6 — Entry/exit timing (adaptation 8): signal-bar-close decision; fills at the next bar's open market. Guards with single-unit book: flat→LONG fills on fresh flips only; LONG→FLAT closes the whole book at the next open; same-side refire is an explicit no-op. After any exit the next qualifying flip may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R7 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R8 — Position state: one 0.01-BTC spot unit max, long or flat, never short (short side explicitly disabled — adaptation 2). Safety orders: explicitly none.
- R9 — Warmup and gaps: flat until 300 completed `1d` bars (structural scale is the length-50 envelope; pine-seed vs zero-seed event sets verified identical on synthetic and live windows — the 250-bar margin renders seeding immaterial post-warmup, disclosed). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals — explicit hold.
- R10 — Invariant identifier: `GH:Indie-script-008ef56|andean-L50_a2/51_bullbear-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup300|2026-11-03` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (envelope clamp, fills), `high`/`low` (validity checks only — no stop/target touches exist in this rule), `close` (envelopes, components). No volume (no volume read anywhere in the shipped code), no funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 300 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing recursion; the sole constant `α` is frozen at bar 0). The `[1]` offsets read past-confirmed values — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 — above the cycle-verified Binance spot BTCUSDT `MIN_NOTIONAL 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: one single-unit long-flat book; re-entry after any exit is explicitly allowed on the next qualifying flip with no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.
- Pinned-engine path (re-verified against local checkout `2dbc844` this cycle, `hummingbot/VERSION=2.17.0`; pinned source `8b0e067e80ab62f10846d518dcb5a8218527ddb3` verified an ancestor of this checkout via `merge-base --is-ancestor`): `data_feed/candles_feed/binance_spot_candles/constants.py` carries the spot `1d` interval; `strategy_v2/backtesting/backtesting_engine_base.py:run_backtesting` iterates completed rows and calls `controller.determine_executor_actions()` (`strategy_v2/controllers/controller_base.py:465`, verified this cycle) feeding completed-row windows into `simulate_executor`; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET at the first window row (`fill_timestamp = df['timestamp'].iloc[0]` — verified this cycle). Hence a completed-bar-`s` decision fills at the next row's open in the next-open lane — the coded timing. The envelope/dispersion/state arithmetic is deterministic controller logic over completed klines; no external feed is required. A strategy-specific, not-yet-implemented controller child must compute exactly R2–R9; the generic executor does not calculate the strategy. Sibling PASS records are path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 48-line fence ships every adopted headline fact quoted in Provenance: the length-50/signal-9 inputs, the `2/(length+1)` alpha, the four clamped envelope recursions with `nz` seeding, the bull/bear dispersion formulas, and the display-only signal smoother. It ships zero orders, zero sizing, zero exits, and zero performance figures — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the Pine-faithful envelope/dispersion/state pipeline (clamped recursion, `nz` seed, strict sign state, equality hold, next-open fills, 300-bar warmup), run in scratch (never committed):

- Synthetic drift tape (700 bars): 1 post-warmup LONG driving an open book, 0 float-guard fires (digest `37f4eb54b9c01da`); two independent runs identical.
- Synthetic alternating-ramp tape (700 bars): 8 post-warmup events (4 LONG / 4 FLAT), 0 float-guard fires (digest `9047c0dd33d6d221`); two independent runs identical.
- Seed-convergence check: pine-seed vs zero-seed runs produce identical post-warmup event sets on the synthetic tape and on a live 1,000-bar window — the 300-bar warmup renders the bar-0 seed immaterial (disclosed).
- Live microstructure (Binance spot 1d klines fetched live this cycle, 2,999 completed bars 2018-08-18→2026-11-02, verified contiguous at 86400s steps with the still-forming current bar excluded by close-time, last completed close 76,816.00): 72 post-warmup events (36 LONG / 36 FLAT) driving 36 paired books ending FLAT, holds 3–192 bars, 0 float-guard fires, 0 equality holds (digest `01f6c279fba8be7f`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 768.16 USDT notional at window close.
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. Unobserved branch fenced: exact bull==bear equality never printed in any probe window (0 holds); the hold-prior pin is an explicit rule for an unobserved branch — flagged, never silently interchangeable with a forced exit.
3. Radicand silence fenced: non-negativity is argued structurally for positive prices and the float guard fired 0 times across ~4,700 evaluated bars; a venue printing non-positive prices would break R3's premise — flagged as an implementation obligation, not strategy behavior.
4. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
5. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (sign-state promotion, long-only pin, fixed sizing, disabled risk, 300-bar warmup, display drop, 0.1% cost overlay, next-open fills, once-per-bar evaluation); the envelope arithmetic, `α`, seeding, dispersion formulas, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `length 50` / `α 2/51` / clamp structure / `nz` seed / bull-bear sign state / equality-hold / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 300-bar warmup are frozen.

- F1 — Length relevance: length-30 and length-70 twins (same rest) must not improve net expectancy; fail ⇒ the length-50 scale carries no edge over neighboring envelope memories.
- F2 — Smoother relevance: a signal-gated twin (entries only when `max(bull,bear)` sits above its EMA9, same rest) must not improve net expectancy; fail ⇒ the dropped display leg was decision-relevant after all.
- F3 — Direction relevance: a two-sided twin (bear>bull → SHORT with mirrored next-open handling, same rest) must not improve net expectancy; fail ⇒ the long-only pin discards the better half of the state.
- F4 — Warmup relevance: a 450-bar-warmup twin must print the identical post-450 event set; fail ⇒ seeding transients leak past the declared warmup.
- F5 — State relevance: a hold-time twin (flat exits delayed one extra bar, same entries) must not improve net expectancy; fail ⇒ the flip-close timing is decoration on the sign state.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; no venue-specific read). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, windows, lengths, grids, or unit counts would be a different, unpinned claim.

## Limitations

- Single-asset port: the source is chart-agnostic indicator mathematics with no market evidence of any kind; BTCUSDT 1d sign-state behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No protective risk: the book carries no stop/target/trailing/time leg by declaration; the longest live-probe hold printed 192 bars — adverse excursions resolve only through the sign flip, disclosed as the coded trade.
- Seeding: `nz` bar-0 seeding transients are absorbed by the 300-bar warmup (pine-vs-zero-seed event sets verified identical); an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Predicate equality: the strict `>`/`<` state with equality-hold is pinned exactly as coded; an implementation forcing equality to either side prints a different event set — flagged, never silently interchangeable.
- Stale-state holds: post-close retained envelope numbers are inert while flat; the equality branch is unobserved in probes — carried as an explicit hold, not as verified behavior.
- Licence: the file is CC BY-NC-SA 4.0 — this record cites short literal lines only and reproduces no source block; research-only use asserted, no commercial claim.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- Primary implementation + pin: https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/Andean%20Oscillator/Andean%20Oscillator.pinescript5 (commit `008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`, 2025-04-18; blob `2656f52cab18c7d5907522c513ba72d34cf81b46`; Pine v5, 48 lines / 1,670 bytes; raw sha256 `7f41fb65b97256f808406ad36cf53afbda1329b353f5416c5f908029faa34f56` verified live 2026-11-03; CC BY-NC-SA 4.0 © alexgrover — short-literal citation only)
- Exchange verification (fetched live 2026-11-03): Binance spot `api/v3/exchangeInfo` (BTCUSDT `TRADING`, spot allowed, `tickSize 0.01`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `NOTIONAL minNotional 5.0`) plus `api/v3/klines` 1d microstructure probes (2,999 completed contiguous bars 2018-08-18→2026-11-02, last completed close 76,816.00; 72 events → 36 paired books ending FLAT, plant digests `37f4eb54b9c01da`/`9047c0dd33d6d221`, live digest `01f6c279fba8be7f`)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (verified ancestor of local checkout `2dbc844`, `hummingbot/VERSION=2.17.0`, this cycle)
- Same-repo sibling (different mechanism, path evidence only): `github-indie-kalman-trend-levels-percent-box-two-sided-btcusdt-4h-2026-11-02.md` on `main`
- Pine reference: v5 `var`-series causal recursion, `nz` seeding, `math.max/min/sqrt` causal semantics; code-governs over prose throughout
