---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView Bufi adaptive-threshold RSI(2) 28-bar time-exit long-flat on BTCUSDT 1d
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-09-17
sources:
  - https://www.tradingview.com/script/zDP76aFT-TASC-2024-10-Adaptive-Oscillator-Threshold/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView Bufi adaptive-threshold RSI(2) 28-bar time-exit long-flat on BTCUSDT 1d

## Provenance

Primary source identity verified end to end (page fetched live and Pine read this cycle, 2026-11-03):

- TradingView strategy `TASC 2024.10 Adaptive Oscillator Threshold` by publisher `PineCodersTASC`, stable URL `https://www.tradingview.com/script/zDP76aFT-TASC-2024-10-Adaptive-Oscillator-Threshold/` (script ID part `PUB;dc82a28cbf634b559af5eb44f92a1eb8`, `script_type: strategy`). Page fetched live this cycle (451,132 bytes, HTTP 200); `<title>` pins `TASC 2024.10 Adaptive Oscillator Threshold — Strategy by PineCodersTASC — TradingView`. Page markers confirm `OPEN-SOURCE SCRIPT` with `PineCodersTASC` authorship and a Sep-17-2024 publication stamp (record `source_as_of` is that stamp, never a fetch date).
- Full Pine source read verbatim this cycle through the page's `Source code` tab (Pine v5 `//@version=5`, header `TASC Issue: October 2024 / Article: Overbought/Oversold Oscillators: Useless Or Just Misused / Article By: Francesco P. Bufi / Provided By: PineCoders`; page marker `61 lines`; MPL-2.0 `© PineCodersTASC`). Pinned declaration: `strategy(title, stitle, false, default_qty_type=strategy.percent_of_equity, default_qty_value=10, slippage=5)` — no `pyramiding`, no `process_orders_on_close`, no `calc_on_every_tick`, no commission arguments anywhere (order census over the captured text this cycle: 2 `strategy.entry` — both id `long`, side `strategy.long`, one inside the `Traditional` branch and one inside the `BAT` branch — 2 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.close_all`, 0 `request.*`, 0 `security(`). Pine defaults therefore apply: single position, close-decided calculation, next-bar-open market fills.
- Pinned inputs (frozen defaults): `sys = "BAT"` (`Traditional`/`BAT` options), `rsiLen = 2`, `buyLevel = 14`, `adapLen = 8`, `adapK = 6.0`, `exitBars = 28`, `DSL = 1600.0` (dollar stop-loss).
- Idea lineage (context only, no numbers adopted): Francesco P. Bufi, "Overbought/Oversold Oscillators: Useless Or Just Misused", TASC October 2024 Traders' Tips. The page text states the buy threshold should rise with trend direction (linear-regression slope) and fall as price-to-mean distance (standard deviation) grows. The code, not the prose, governs every formula below.
- Licence and rights: this record cites and normalizes the rule (short phrases and definitional recurrence only) and reproduces no extended prose, figures, or performance numbers. The page's `Strategy report` tab was never opened; no author backtest number is adopted anywhere in this record.

**Closed-PR lineage (read before review):** same-source PR #224 (`research/hermes-bufi-adaptive-threshold-20261015-1755`) was closed `NOT_LOSSLESS` on three Gate-5 evidence blockers only — (A) no identified controller/executor/connector or verifiable engine path for decision-to-fill and the 28-bar exit count, (B) no defined funding/fee/slippage model, (C) no quantity-precision/minimums/margin accounting for its 3x/5x posture — while its Gates 1–4 (Pine formulas, long-flat direction, 28-bar time exit with DSL=0, single-long re-entry) were confirmed against the source. This file is a new, independently re-verified record on the same source (not an edit of the closed PR, not a paraphrase of its text): the Pine was re-read line by line this cycle, and Gate 5 is rebuilt below with pinned engine paths re-verified this cycle plus explicit cost/minimums/1x-margin facts. Same construction, because the source is identical — disclosed, never presented as a new mechanism.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the source's BAT-threshold RSI(2) construction ported to BTCUSDT 1d with fixed sizing and close-evaluated fills — not a lossless reproduction of the author's SPY-tester setup. Researcher-declared adaptations are exactly seven: (1) single-asset BTCUSDT Binance USDT-M perpetual venue (the source ships no venue pin; daily grid is source-native); (2) `sys = "BAT"` pinned — a source-provided default option, and the `Traditional` fixed-level branch is dead code under the pin (disclosed, never deleted from the source); (3) `DSL = 0` — the source's dollar stop (1600 SPY-tester dollars under 10%-of-equity sizing) does not survive the sizing port, so it is disabled rather than re-denominated, and no replacement stop is invented (the 28-bar time exit is the sole risk path — disclosed); (4) fixed 0.01 BTC 1x isolated sizing replacing the author's 10%-of-equity sizing (the source `slippage = 5` ticks and 10% equity are SPY-tester economics, never ported); (5) completed-bar-close decision with same-bar-close market fills (declared conversion of the author's next-bar-open fills — the close-evaluated conversion class already used by admitted pool records); (6) structural 100-completed-bar warmup (the source ships none — first fully defined BAT decision needs bars 0..8; the margin absorbs RMA seeding); (7) display drop (plots/fills only). The RSI(2) oscillator, BAT formula, 14/8/6.0 constants, strict `<` entry gate, 28-bar exit count, long-only book, and no-bracket-beyond-time-exit stance are source-faithful. This record is therefore never evidence that the author's script passes.

Pre-write dedup (2026-11-03): working-tree base is current `main@59a780bd` (536 root strategy records). Case-insensitive content searches for `zDP76aFT`, `dc82a28c`, `AdapThrs`, `adapK`, `adapLen`, `Adaptive Oscillator Threshold`, `buyLevel` return zero same-source/same-construction hits (the only `Bufi` hits are cousin-list prose mentions of closed #224 inside three unrelated October records — fencing, never a rule). No pool record computes an oscillator threshold as `buyLevel × adapK × clamp(linreg-slope / stdev)`: Connors-RSI records use fixed RSI(2)/(3) levels, `drm-dynamic-rsi` adapts the RSI *length* via correlation with fixed 70/30 levels (different signal object), TTM-squeeze records use stdev ratios for squeeze state (different construction). All 17 open `research/*` PRs enumerated by number/title/branch (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725) — none is this script, publisher, article, or construction. Five-axis distinction: no pool record and no open PR conditions entries on RSI(2) crossing under a threshold that scales with the clamped ratio of 8-bar regression slope to 8-bar dispersion, exited only by a 28-bar count.

## Economic mechanism

### Source-reported

A fixed oscillator level misfires because the same RSI print means different things in trends versus chop; scaling the buy level with trend direction (regression slope) while damping it by dispersion (standard deviation) keeps the bar high when price is stretched and lowers it when a pullback inside an up-drift is actually buyable. (Author's framing fenced to equities; never adopted as a crypto claim.)

### Research interpretation

Adaptive-threshold dip hold, long-only, daily cadence. Unlike fixed-level RSI records there is no constant oversold line anywhere — the trigger `thrs = 84 × BAT(close, 8)` breathes between −42 and +42, and because RSI(2) lives in [0, 100], entries can only print while the 8-bar drift tilts up (BAT > 0); down-drift bars are structural holds, not near-misses. Unlike oscillator-cross records there is no cross event and no exit leg tied to the oscillator at all — once in, the RSI line is never read again; the position simply ages out after 28 bars. Unlike bracket records there is no stop/target/trailing artifact: risk is the time exit alone. The bet, as derived, is purely that Bufi's slope-over-dispersion threshold ports arithmetically to BTCUSDT daily bars — with the economics of that port fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; close-evaluated market fills; long-flat — any other window, grid, sizing, or fill is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Oscillator: `osc[i] = RSI(2)[i]` on close (Pine `ta.rsi`: Wilder RMA of up-moves over RMA of absolute moves, RMA seeded per Pine convention; seeding transient absorbed by the R11 warmup, never interpolated around).
- R3 — BAT (source formula, pinned): `sd[i] = stdev(close, 8)[i]`; `lr[i] = linreg(close, 8, 0)[i]` (fitted value at the current bar); `slope[i] = (lr[i] − close[i−8]) / 9`; `BAT[i] = clamp(slope[i] / sd[i], −0.5, +0.5)`. First fully defined at bar index 8.
- R4 — Threshold: `thrs[i] = 14 × 6.0 × BAT[i] = 84 × BAT[i]`, hence `thrs ∈ [−42, +42]` by construction.
- R5 — Entry gate (strict inequality, pinned; equality holds): flat and `osc[i] < thrs[i]` → market long entry. `thrs ≤ 0` (down-drift) and `sd = 0` (flat-8, BAT na) stretches never fire — explicit holds, not missing rules.
- R6 — Orders (pinned; `Traditional` branch dead under the BAT pin): `strategy.entry("long", strategy.long)` while flat; a same-bar re-fire while holding is a Pine no-op under default `pyramiding = 0` (pinned, never an add).
- R7 — Time exit (pinned count, source-faithful): `nBar = bar_index − entry_bar_index` from the actual fill event; holding and `nBar ≥ 28` (`exitBars = 28`, first disjunct `exitBars > 0` always true) → `strategy.close("long", "exit")` — full flat, no partials. Distinct decisions fill on distinct bar closes, so no same-bar dual-fire exists to sequence.
- R8 — Risk legs (pinned absences, not invented): `DSL = 0` disables the source dollar-stop leg (adaptation 3 — the `immediately = true` intrabar path is structurally idle); no take-profit, no trailing, no second exit, no cooldown — explicitly none, matching the shipped code (zero `strategy.exit`).
- R9 — Position state: at most one long at any time; no adds, no partials, no pyramiding, no DCA — explicitly none. After any time exit the next qualifying bar may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none, not invented).
- R10 — Warmup and gaps: flat until 100 completed `1d` bars (structural need is bars 0..8; the margin absorbs RMA seeding per the admitted precedent chain). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat.
- R11 — Invariant identifier: `TV:pinecoderstasc-zDP76aFT|BAT84_rsi2_thr28DSL0|longOnly|independent-derived-v1|BinanceFutures:BTC-USDT:1d|LONG-FLAT|closeeval-MARKET|fee0.0005|lev1x|size0.01|warmup100|2026-11-03` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (RSI, stdev, linreg, threshold arithmetic, fill prices). No `high`, no `low`, no volume, no funding/OI/mark-index read gates any order, no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one threshold evaluation per completed daily-bar close; fills land at that bar's close. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: flat until 100 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing statistic; boundaries are constants).

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual, 1x isolated, fixed 0.01 BTC per entry, no adds, no compounding. The short side is explicitly disabled (source has no short leg under any input combination — both entries are `strategy.long`).
- Order timing (declared close-evaluated conversion; the author ships next-bar-open fills): completed-bar-close decision with same-bar-close market fills for entries and the 28-bar time exit — the same lane primitive admitted records in `main` use. No maker-touch, queue, or intrabar-path-dependent fill is claimed. R5's strict inequality plus R9's single-position pin leave no ambiguous same-bar fill order.
- Sizing/capital/costs (blocker-B/C answers, all fixed this cycle): fixed 0.01 BTC per entry (≈765.2 USDT at the cycle's public ticker print 76,522.0 — above the cycle-verified Binance USDT-M BTCUSDT `MIN_NOTIONAL 50`, `LOT_SIZE minQty/stepSize 0.001/0.001`, `MARKET_LOT_SIZE minQty 0.001`; 0.01 is an exact multiple of the step). Explicit research cost overlay: 0.05% taker fee per filled side; modeled funding = sum of realized BTCUSDT-perp settlements (00:00/08:00/16:00 UTC, realized period rate on full notional, sign as settled) while a position is open — a defined, reproducible research model, never hypothetical zero funding and never realized/canonical funding; slippage unmodeled by declaration (the source's 5-tick SPY slippage does not port). Any run missing settlement inputs is void, never zero-filled. The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Margin/liquidation (1x posture): fixed-size 1x isolated single-position with no compounding and no abort rule — no liquidation path exists inside a −100% move short of total loss; no margin-call/forced-close event can pre-empt the 28-bar exit (disclosed). Fills are never conditional on equity, funding, or buying power.
- Concurrency: at most one position at any time (`pyramiding = 0` pinned); re-entry after a time exit is explicitly allowed on the next qualifying bar; no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.
- Pinned-engine path (re-verified against local checkout `2dbc844` this cycle, `VERSION=2.17.0`; remote `origin` is `HCH725/hummingbot`, and pinned source `8b0e067e80ab62f10846d518dcb5a8218527ddb3` verified an ancestor of this checkout via `merge-base --is-ancestor`): `data_feed/candles_feed/binance_perpetual_candles/constants.py:24` maps `1d → 86400`; `strategy_v2/backtesting/backtesting_engine_base.py:282-287` iterates completed rows, calls `controller.determine_executor_actions()` (`strategy/strategy_v2_base.py:747`, `models/executor_actions.py:17 CreateExecutorAction`), and feeds `processed_features.loc[i:max_ts]` (window from the decision row) into `simulate_executor`; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:22-24,56` fills MARKET at the first window row's timestamp at that row's `close`. Hence a completed-bar-t decision fills at `close[t]` — the coded timing. The BAT/RSI/threshold arithmetic, the 28-bar count from the recorded fill event, and the flat/hold branches are deterministic controller logic over completed klines; no external feed is required. A strategy-specific, not-yet-implemented `DirectionalTradingControllerBase` child must compute exactly R2–R9; the generic executor does not calculate the strategy. Admitted time-exit lane precedent in `main` (`turn-of-month-4day-hold`, `caporale-plastun-strategy2-nextday`) shows bar-count exits on this engine class; sibling PASS records are path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The script page and header ship every adopted headline fact quoted in Provenance: the Bufi article lineage, the slope-proportional / dispersion-damped threshold doctrine, the RSI demonstration vehicle, the BAT-system default, next-bar-open fills, the 28-bar exit, the dollar stop, long-only sizing, and the 5-tick slippage. It ships zero adopted performance numbers for this record: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from the page, header, or reference engine is adopted anywhere — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Logic checks executed during this scout cycle (this cycle's own Python, synthetic inputs only — no real-market replay, no profitability figure):

- Threshold-range proof: `thrs = 84 × clamp(·, ±0.5)` ⇒ `thrs ∈ [−42, +42]`; RSI(2) ∈ [0, 100] ⇒ entries structurally require BAT > 0 (up-drift tilt).
- Synthetic 8-close windows: steady rise → BAT +0.3395 → thrs +28.51 (entry-eligible zone); steady fall → BAT −0.3395 → thrs −28.51 (never fires — RSI(2) ≥ 0); flat-8 → `sd = 0` → BAT na → explicit hold.
- Order census on the captured source text: 2 `strategy.entry` (both long — Traditional + BAT branches), 2 `strategy.close` (time exit + DSL leg, latter dead under the DSL=0 pin), 0 `strategy.exit`, 0 `strategy.order`, 0 `strategy.close_all`, 0 `request.*`/`security(` — matches the line-by-line read.

### Negative evidence

1. Fill-conversion fenced: derived close-evaluated fills differ from the author's next-bar-open fills by up to one full `1d` bar on every entry and exit — slow-threshold regimes give back more than the author's tester would show. This is the coded trade, disclosed, not a tunable parameter here.
2. DSL-removal fenced: the source's 1600-dollar stop is disabled, not re-denominated — deep adverse excursions ride the full 28 bars by construction. The time exit is the sole risk path, disclosed.
3. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from the script page, header, or reference engine is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
4. Derivation boundary fenced: the only non-author behavior is the seven declared adaptations (venue, BAT pin, DSL off, fixed sizing, close-evaluated fills, 100-bar warmup, display drop); the RSI(2) oscillator, BAT formula, 14/8/6.0 constants, strict entry gate, 28-bar count, long-only book, and no-bracket-beyond-time-exit stance are source-faithful. This record is therefore never evidence that the author's script passes.
5. Prior-art fenced: same-source PR #224 closed `NOT_LOSSLESS` on Gate-5 evidence (A/B/C above); this record's Gate 5 is rebuilt, not referenced — the closed branch is lineage, never evidence.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `RSI(2)` / `buyLevel 14` / `adapLen 8` / `adapK 6.0` / `exitBars 28` / `DSL 0` / BAT branch / strict `<` / long-flat / close-evaluated fills / fixed 0.01 BTC 1x / BTCUSDT `1d` are frozen.

- F1 — Threshold relevance: a fixed-level twin (`thrs = 14` always, same grid/entries/exit/fills) must not improve net expectancy; fail ⇒ the slope-over-dispersion adaptivity adds nothing over classic RSI(2)<14.
- F2 — Oscillator relevance: a slope-only twin (enter whenever BAT > 0, same exit/fills) must not improve net expectancy; fail ⇒ RSI(2) is fee-burning decoration on a drift filter.
- F3 — Exit relevance: an opposite-gate twin (exit when `osc ≥ thrs` instead of the 28-bar count, same entries/fills) must not improve net expectancy; fail ⇒ the fixed-bar exit destroys more expectancy than it saves in avoided overstays.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-signal days costs more in missed drift than it saves in avoided chop.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual (decision grid completed `1d` bar closes; fills at those closes; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; weekends trade continuously — no equity-calendar port artifact). Extension to other house-universe assets, timeframes, windows, levels, coefficients, or grids would be a different, unpinned claim.

## Limitations

- Single-asset port: the author's evidence is SPY/equity tester context; BTCUSDT 1d BAT-threshold behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Conversion lag: close-evaluated fills deviate from the author's next-bar-open execution on every entry and exit — the derived event set is its own object, never the author's tester output.
- DSL removal: disabling the source dollar stop removes the only intra-trade loss cut — the 28-bar ride is a pinned artifact of the sizing port, not a market claim.
- RSI seeding: Pine RMA seeding transient is absorbed by the 100-bar warmup; an implementation using a different seed must still hold pre-warmup bars flat — flagged as an implementation obligation, not strategy behavior.
- Flat-stretch holds: 8-bar zero-dispersion stretches print na thresholds and hold — fenced by construction, never traded around.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- TradingView OPEN-SOURCE STRATEGY by PineCodersTASC (script ID `zDP76aFT`, `PUB;dc82a28cbf634b559af5eb44f92a1eb8`), page fetched and Pine read live 2026-11-03: https://www.tradingview.com/script/zDP76aFT-TASC-2024-10-Adaptive-Oscillator-Threshold/
- Idea lineage (context only, no numbers adopted): Francesco P. Bufi, "Overbought/Oversold Oscillators: Useless Or Just Misused", TASC October 2024 Traders' Tips.
- Closed-PR lineage (methodology only, never evidence): HCH725/alpha-strategy-research#224 (same source; closed `NOT_LOSSLESS` on Gate-5 A/B/C evidence gaps).
