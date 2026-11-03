---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: LazyBear VFI-VFIMA sign-state long-flat on BTCUSDT 1d bars
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
  - https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/Volume%20Flow%20Indicator/Volume%20Flow%20Indicator.pinescript
  - https://www.tradingview.com/script/MhlDpfdS-Volume-Flow-Indicator-LazyBear/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LazyBear VFI–VFIMA sign-state — independent BTC-USDT spot 1d long-flat derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `Indie-script/indie-script.github.io` commit **`008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`** (2025-04-18, `Initial commit of Indie site`, verified via GitHub API this cycle), file **`indicators/Volume Flow Indicator/Volume Flow Indicator.pinescript`**, blob `4a53b1af20ff4ff9856138377448d6eb1db88dde`, **1,024 bytes / 35 lines**, `study("Volume Flow Indicator [LazyBear]")` — an indicator, not a strategy. Raw bytes re-downloaded this cycle hash to sha256 `65b7a31278b26df0259229bdb9ebda51012911c1c6916db42a04b86c7a1f56cd`, byte-identical to the working copy. Origin: LazyBear's open-source TradingView script `MhlDpfdS` (Markos Katsanos's VFI, an OBV variant; its page states positive readings bullish / negative bearish and 0.2 coef for day trading vs 0.1 intraday — short-literal citation only, page code never re-fetched, no source block reproduced).

**Order-affecting logic read verbatim (code governs; the study ships no orders):** `length = input(130)`, `coef = input(0.2)`, `vcoef = input(2.5)`, `signalLength = input(5)`, `smoothVFI = input(false)`, `showHisto = input(false)`; `typical = hlc3`; `inter = log(typical) - log(typical[1])`; `vinter = stdev(inter, 30)`; `cutoff = coef * vinter * close`; `vave = sma(volume, length)[1]`; `vmax = vave * vcoef`; `vc = min(volume, vmax)`; `mf = typical - typical[1]`; `vcp = +vc iff mf > cutoff, -vc iff mf < -cutoff, else 0`; `vfi = sum(vcp, length) / vave` (unsmoothed — `smoothVFI=false` pins `ma(x,3)=x`); `vfima = ema(vfi, signalLength)`; `d = vfi - vfima`.

**Pine-block census (35-line fence):** 1 `study(`; 0 `strategy.entry` / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` of any kind; 6 `input(` (130 / 0.2 / 2.5 / 5 / false / false — all fenced at defaults); 0 `request.` / 0 `security(` / 0 `timeframe.*` / 0 `barstate.*`; 2 unconditional `plot(` (VFIMA, VFI) plus 1 default-off histogram (`showHisto=false`) and 1 zero-line — all display-only, dropped, disclosed.

**Corroborating same-commit port (not canonical):** sibling `Volume Flow Indicator.indie4` (2,064 bytes, MPL-2.0, same commit) ports the identical constants and semantics (`length 130`, `coef 0.2`, `vcoef 2.5`, `signal_length 5`, `smooth_vfi false`) and names the same TV origin `MhlDpfdS`; the `.indie5` sibling is a 0-byte placeholder. Cited as consistency evidence only — every pinned literal below comes from the `.pinescript` fence.

**Structural facts carried over exactly:** (a) volatility-normalized money-flow gate — each bar's signed volume survives only past a cutoff scaling with 30-bar log-change dispersion times close, chop prints exactly 0; (b) volume-spike cap at 2.5× trailing average before signing; (c) signed accumulation normalized by average volume (unit-free ratio); (d) no MTF, no session/timezone, no intrabar semantics anywhere.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the source is an indicator and ships no entries, exits, sizing, or risk. Researcher-declared adaptations are exactly nine: (1) promotion of the VFI-minus-VFIMA sign state to long-flat entries/exits on completed bars (`d>0` → LONG, `d<0` → FLAT, exact zero holds prior state — disclosed promotion, same strict semantics); (2) long-only pin with the short side explicitly disabled (the construction is signed; the short leg is a deliberate omission, disclosed); (3) fixed **0.01 BTC** spot sizing (≈768.16 USDT at probe last completed close 76,816.00, above verified 5-USDT min-notional and 0.00001 min-qty); (4) all risk legs (SL/TP/trailing/time) explicitly disabled — signal-exit-only risk, disclosed; (5) 300-bar warmup with pre-warmup bars flat (structural scale is the 130-bar volume average plus the 30-bar dispersion window, plus researcher margin); (6) display drop (all plots plus the default-off histogram); (7) explicit **0.1%/side research cost** (Binance spot standard taker), slippage unmodeled (disclosed); (8) close-decided signals filled next-bar-open MARKET (research-model timing convention, never a live-engine claim); (9) once-per-completed-bar evaluation (no confirmed-close flag ships in source, so the bar discipline is a researcher pin, disclosed).

**Immutable derivative identity:** `GH:Indie-script-008ef56|vfi-L130_c0.2_vc2.5_sig5_d-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup300|2026-11-03`. Changing any formula, length, coef, gate, timing, market, risk, cost, sizing, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-03):** working-tree base is current `main@b13f9d1e` (540 root strategy records, READMEs excluded, all `hb_ready_status: PASS` re-verified this cycle). Case-insensitive content searches for `vfima`, `vcoef`, `VFI_LB`, `smoothVFI` return zero hits; `volume flow` returns 9 prose-only hits naming no VFI leg (`dual-thrust`, `fmz-candlesize`, `fmz-multiwave`, `fmz-powerzone`, `fmz-smma17`, `fmz-super-scalper`, `fmz-tbma`, `forven-obv-ema`, `r-breaker` — generic English about unrelated volume behavior). All 17 open `research/*` PRs enumerated by number/title/branch (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725) — none is this file, author, or construction. Five-axis distinction vs nearest pool neighbors: different source file and math vs `pvo-signal-cross` (pure-volume EMA ratio, no cutoff/cap), `klinger-volume-oscillator` (dual-EMA volume force, no money-flow gate), `forven-obv-ema` (unbounded cumulative OBV, no spike cap), `sqzmom-lb` (different LazyBear indicator, squeeze release), and `tradingview-lazybear-ttf-cross-trigger` (same author, different indicator and trigger) — no duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

VFI (Katsanos, via the origin page): an On-Balance-Volume variant with three modifications; positive readings are bullish and negative bearish; the author suggests coef 0.2 for day trading and 0.1 for intraday — the author's reading frame and coef guidance, never adopted as a crypto claim (the 0.1 variant is used only as a falsifier twin in F1).

### Research interpretation

Unlike pool volume oscillators (PVO's pure-volume EMA ratio, Klinger dual-EMA volume force, OBV's unbounded cumulative tape), this machine range-filters flow before accumulating: sub-cutoff chop contributes exactly zero and spikes are capped at 2.5× average, so the sign state reacts to sustained directed flow, not raw prints. Unlike pool price-oscillator sign states (RSI/ROC threshold or zero signs over fixed windows), the state is flow-minus-its-own-EMA5 — structurally a MACD-style line/signal pair computed on capped money-flow rather than price. The bet, as derived, is purely that this chop-gated flow sign ports arithmetically to BTCUSDT spot daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed spot `1d` bars; entries/exits next-bar-open market; long-only single-unit book — any other constant, window, sizing, fill, or cost is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT spot only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Flow gate (source formulas, pinned): `typical[t] = (H+L+C)[t]/3`; `inter[t] = ln(typical[t]) − ln(typical[t−1])`; `vinter[t] = stdev(inter[t−29..t])` (Pine default biased/population `/N` reading — pinned researcher reading, disclosed); `cutoff[t] = 0.2 · vinter[t] · C[t]`; `vave[t] = mean(V[t−130..t−1])` (the `[1]` shift excludes the decision bar — pinned); `vmax[t] = 2.5 · vave[t]`; `mf[t] = typical[t] − typical[t−1]`; `vcp[t] = +min(V[t],vmax[t])` iff `mf[t] > cutoff[t]`, `−min(V[t],vmax[t])` iff `mf[t] < −cutoff[t]`, else `0`.
- R3 — Oscillator and signal (source formulas, pinned): `vfi[t] = Σ vcp[t−129..t] / vave[t]` (unsmoothed — `smoothVFI=false` fence); `vfima[t] = EMA(vfi, 5)` with `α = 1/3`, seeded at the first finite `vfi` (researcher seed pin — the 300-bar warmup absorbs it to `(2/3)^300 ≈ 0`, disclosed); `d[t] = vfi[t] − vfima[t]`.
- R4 — Display drop (adaptation 6): all `plot(` legs and the default-off histogram never enter any predicate.
- R5 — State (promoted predicate, adaptation 1): `LONG[t]` iff `d[t] > 0`; `FLAT[t]` iff `d[t] < 0`; exact zero holds the prior state (flat-tape probe: 200/200 post-warmup holds — verified branch in probe; live window printed 0 occurrences — carried as an explicit rule, not as verified live behavior).
- R6 — Entry/exit timing (adaptation 8): signal-bar-close decision; fills at the next bar's open market. Guards with single-unit book: flat→LONG fills on fresh flips only; LONG→FLAT closes the whole book at the next open; same-side refire is an explicit no-op. After any exit the next qualifying flip may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R7 — Risk legs (adaptation 4, pinned absences, not invented): no stop, no target, no trailing, no time exit — explicitly none, matching the shipped code (zero order calls).
- R8 — Position state: one 0.01-BTC spot unit max, long or flat, never short (short side explicitly disabled — adaptation 2). Safety orders: explicitly none.
- R9 — Warmup and gaps: flat until 300 completed `1d` bars (structural scale is the 130-bar average plus the 30-bar dispersion window; probe shows 0 NaN bars post-warmup). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat. A bar with nonfinite/non-positive OHLC, non-positive `typical` (log domain), `V < 0`, or `H < max(O,C)` / `L < min(O,C)`, is invalid for signals — explicit hold.
- R10 — Invariant identifier: `GH:Indie-script-008ef56|vfi-L130_c0.2_vc2.5_sig5_d-sign_longonly|independent-derived-v1|BinanceSpot:BTC-USDT:1d|LONG-FLAT|0.01BTC|nextopen-MARKET|fee0.001|lev1x-spot|warmup300|2026-11-03` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT spot only: `open` (fills, validity), `high`/`low`/`close` (typical, cutoff, validity), `volume` in base asset (vave/vc/vcp — every use is ratio- or same-unit-capped, so units cancel; no quote-volume conversion exists in this rule). No funding/OI/mark-index read gates on any order (spot has no funding by construction — disclosed exclusion, never a zero-funding fiction), no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one signal evaluation per completed daily-bar close; fills land at the next bar's open. No provisional intrabar value is ever used.
- Warmup: flat until 300 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing recursion; the four constants are frozen inputs). The `[1]` offsets read past-confirmed values — point-in-time clean.

## Execution assumptions

- Research market: BTCUSDT Binance spot, 1x, fixed 0.01 BTC per unit, single-unit book, no compounding. Long side explicitly enabled; short side explicitly disabled. Fills are never conditional on equity or buying power.
- Order timing (declared promotion): signal-bar-close decision; entries and exits fill at the next bar's open market. No maker-touch, queue, or intrabar-path-dependent fill is claimed. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Sizing/capital/costs (all fixed this cycle): fixed 0.01 BTC per unit (≈768.16 USDT at the cycle's last completed close 76,816.00 — above the cycle-verified Binance spot BTCUSDT `MIN_NOTIONAL 5.0`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `PRICE_FILTER tickSize 0.01`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.1% taker fee per filled side; slippage unmodeled by declaration. Spot venue means no funding leg exists — constructive exclusion, never modeled-or-realized funding.
- Concurrency: one single-unit long-flat book; re-entry after any exit is explicitly allowed on the next qualifying flip with no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.
- Pinned-engine path (re-verified against local checkout `2dbc844` this cycle, `hummingbot/VERSION=2.17.0`; pinned source `8b0e067e80ab62f10846d518dcb5a8218527ddb3` verified an ancestor of this checkout via `merge-base --is-ancestor`): `data_feed/candles_feed/binance_spot_candles/constants.py` carries the spot `1d` interval; `strategy_v2/backtesting/backtesting_engine_base.py:run_backtesting` iterates completed rows and calls `controller.determine_executor_actions()` (`strategy_v2/controllers/controller_base.py:465`, verified this cycle) feeding completed-row windows into `simulate_executor`; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` fills MARKET at the first window row (`fill_timestamp = df['timestamp'].iloc[0]` — verified this cycle). Hence a completed-bar-`s` decision fills at the next row's open in the next-open lane — the coded timing. The VFI/dispersion/state arithmetic is deterministic controller logic over completed klines; no external feed is required. A strategy-specific, not-yet-implemented controller child must compute exactly R2–R9; the generic executor does not calculate the strategy. Sibling PASS records are path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 35-line fence ships every adopted headline fact quoted in Provenance: the 130/0.2/2.5/5/false/false inputs, the hlc3/log-change/dispersion/cutoff chain, the shifted volume average with the 2.5× spike cap, the signed accumulation with the chop-zero branch, and the EMA5 signal leg with its difference. It ships zero orders, zero sizing, zero exits, and zero performance figures — none adopted; all of those are researcher pins disclosed above.

### Independently reproduced

No strategy backtest, event-level Qlib/Hummingbot parity, code execution comparison, live order, testnet/paper trade, wheel rehash, deployment, or profitability experiment occurred. Pinned engine file inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the disclosed VFI re-implementation (gated accumulation, spike cap, population-stdev reading, first-finite EMA seed, strict d-sign state, equality hold, next-open fills, 300-bar warmup), run in scratch (never committed):

- Live microstructure (Binance spot 1d klines fetched live this cycle, 2,999 completed bars 2018-08-18→2026-11-02, verified contiguous at 86400s steps with the still-forming current bar excluded by close-time, last completed close 76,816.00): 553 post-warmup events (277 LONG / 276 FLAT) driving 277 books, holds 1–26 bars, 0 equality holds, 0 NaN bars post-warmup (digest `35f9a22bfe523c2e`); two independent runs identical. Signal bars are predicate prints, never trade counts. 0.01 BTC ≈ 768.16 USDT notional at window close.
- Flat-tape branch probe (500 constant bars): 200/200 post-warmup `d == 0` equality holds — the hold-prior rule is verified probe behavior on degenerate input (live tape printed 0 occurrences, disclosed).
- Spike-cap probe: a 100× volume spike with a +20% move is capped at exactly 2.5× trailing average before signing (probe arithmetic, disclosed).
- Logic checks are verification of the coded rule chain only — not a backtest, not parity, not profitability.

### Negative evidence

1. Indicator-promotion fenced: the source ships no orders, so LONG/FLAT semantics, venue, sizing, warmup, and the no-box risk posture are researcher pins — the derived event set is its own object, never the author's output.
2. Dispersion-denominator reading fenced: the probe implements Pine's default biased (`/N`) stdev; a sample-`/N−1` reading would scale the cutoff by √(30/29) ≈ 1.7% and print a different event set — the `/N` reading is pinned in R2, never silently interchangeable.
3. EMA-seed silence fenced: Pine's early-EMA transient is absorbed by the 300-bar warmup (seed weight decays to ~(2/3)^300); an implementation seeding differently must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
4. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
5. Derivation boundary fenced: the only non-source behavior is the nine declared adaptations (d-sign promotion, long-only pin, fixed sizing, disabled risk, 300-bar warmup, display drop, 0.1% cost overlay, next-open fills, once-per-bar evaluation); the gate arithmetic, cap, constants, and input defaults are source-faithful. This record is therefore never evidence that any author strategy passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `length 130` / `coef 0.2` / `vcoef 2.5` / `signalLength 5` / unsmoothed VFI / d-sign state / equality-hold / long-only / no-box exits / next-open fills / fixed 0.01 BTC spot / BTCUSDT `1d` / 300-bar warmup are frozen.

- F1 — Coef relevance: a coef-0.1 twin (the author's named intraday variant, falsifier only — never adopted here) with the same rest must not improve net expectancy; fail ⇒ the 0.2 daily pin carries no edge over the named alternative.
- F2 — Signal relevance: a signalLength-9 twin (same rest) must not improve net expectancy; fail ⇒ the 5-bar signal leg was decoration on the flow accumulation.
- F3 — Direction relevance: a two-sided twin (d<0 → SHORT with mirrored next-open handling, same rest) must not improve net expectancy; fail ⇒ the long-only pin discards the better half of the state.
- F4 — Warmup relevance: a 450-bar-warmup twin must print the identical post-450 event set; fail ⇒ seeding transients leak past the declared warmup.
- F5 — State relevance: a hold-time twin (flat exits delayed one extra bar, same entries) must not improve net expectancy; fail ⇒ the flip-close timing is decoration on the d-sign state.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid completed `1d` bar closes; entries/exits at next opens; volume read in base asset with unit-free ratios — no venue-specific read). The arithmetic ports across spot venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, constants, grids, or unit counts would be a different, unpinned claim.

## Limitations

- Single-asset port: the source is chart-agnostic indicator mathematics with no market evidence of any kind; BTCUSDT 1d sign-state behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No protective risk: the book carries no stop/target/trailing/time leg by declaration; the longest live-probe hold printed 26 bars — adverse excursions resolve only through the sign flip, disclosed as the coded trade.
- Seeding: first-finite-EMA-seed transients are absorbed by the 300-bar warmup; an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Predicate equality: the strict `>`/`<` state with equality-hold is pinned exactly as coded; an implementation forcing equality to either side prints a different event set — flagged, never silently interchangeable.
- Log-domain guard: bars with non-positive `typical` cannot enter the `log` leg and are held by record rule; a venue printing non-positive prices would break R2's premise — flagged as an implementation obligation, not strategy behavior.
- Licence: the canonical `.pinescript` carries an education/author header with no licence grant and the TV origin page marks the script open-source subject to house rules — this record cites short literals only and reproduces no source block; research-only use asserted, no commercial claim.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- Primary implementation + pin: https://github.com/Indie-script/indie-script.github.io/blob/008ef56613e6a5d3ca599e25fb0f70c39f7c2fea/indicators/Volume%20Flow%20Indicator/Volume%20Flow%20Indicator.pinescript (commit `008ef56613e6a5d3ca599e25fb0f70c39f7c2fea`, 2025-04-18; blob `4a53b1af20ff4ff9856138377448d6eb1db88dde`; Pine study, 35 lines / 1,024 bytes; raw sha256 `65b7a31278b26df0259229bdb9ebda51012911c1c6916db42a04b86c7a1f56cd` verified live 2026-11-03; origin LazyBear TV script `MhlDpfdS`, Katsanos VFI — short-literal citation only)
- Same-commit corroborating port (not canonical): `Volume Flow Indicator.indie4` (2,064 bytes, MPL-2.0, identical 130/0.2/2.5/5/false constants, same TV origin named in-file); `.indie5` sibling is a 0-byte placeholder
- Exchange verification (fetched live 2026-11-03): Binance spot `api/v3/exchangeInfo` (BTCUSDT `TRADING`, spot allowed, `tickSize 0.01`, `LOT_SIZE minQty/stepSize 0.00001/0.00001`, `NOTIONAL minNotional 5.0`) plus `api/v3/klines` 1d microstructure probes (2,999 completed contiguous bars 2018-08-18→2026-11-02, last completed close 76,816.00; 553 events → 277 books, holds 1–26, live digest `35f9a22bfe523c2e`; flat-tape 200/200 equality holds; 100× spike capped at 2.5× average)
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 (verified ancestor of local checkout `2dbc844`, `hummingbot/VERSION=2.17.0`, this cycle)
- Same-repo sibling (different mechanism, path evidence only): `github-indie-andean-envelope-dispersion-sign-state-long-flat-btcusdt-1d-2026-11-03.md` on `main`
- Pine reference: v3 `study`/`input`/`iff` causal semantics, trailing-window `stdev`/`sma`/`sum`/`ema`, `[1]` past-confirmed offsets; code-governs over prose throughout
