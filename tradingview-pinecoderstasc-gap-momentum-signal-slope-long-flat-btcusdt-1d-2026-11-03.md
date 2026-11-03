---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView PineCodersTASC Gap Momentum signal-slope long-flat on BTCUSDT 1d
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-03
sources:
  - https://www.tradingview.com/script/52wKLj6P-TASC-2024-01-Gap-Momentum-System/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView PineCodersTASC Gap Momentum signal-slope long-flat on BTCUSDT 1d

## Provenance

Primary source identity verified end to end (page fetched live and Pine read this cycle, 2026-11-03):

- TradingView strategy `TASC 2024.01 Gap Momentum System` by publisher `PineCodersTASC`, stable URL `https://www.tradingview.com/script/52wKLj6P-TASC-2024-01-Gap-Momentum-System/` (script ID part `PUB;34e22727a1be4a3ebf62de0e3413e9d9`). Page fetched live this cycle (562,929 bytes, HTTP 200); `<title>` pins `TASC 2024.01 Gap Momentum System — Strategy by PineCodersTASC — TradingView`. Page markers confirm `OPEN-SOURCE` script with `PineCodersTASC` authorship; page-embedded strategy inputs pin `Period: 40`, `Signal Period: 20`, `Long Only: true` as defaults.
- Full Pine source read verbatim (47 lines, Pine v5 `//@version=5`, header `TASC Issue: January 2024 - Vol. 42, Issue 1 / Article: Gap Momentum Indicator / Article By: Perry J. Kaufman / Provided By: PineCoders`). Pinned declaration: `strategy(title, stitle, false)` — no `pyramiding`, no `process_orders_on_close`, no commission/sizing arguments anywhere (order census this cycle: 2 `strategy.entry` — one `long`, one `short` inside the `longOnly=false` branch — 1 `strategy.close_all`, 0 `strategy.exit`, 0 `strategy.order`, 0 `request.*`, 0 `security(`). Pine defaults therefore apply: next-bar-open market fills, calculation on bar close.
- Pinned inputs (frozen defaults): `period = 40`, `signalPeriod = 20`, `longOnly = true`.
- Idea lineage (context only, no numbers adopted): Perry J. Kaufman, "Gap Momentum", Traders' Tips, TASC January 2024 edition (Vol. 42, Issue 1). The page text states the system is long-only with two rules — enter long when the signal line moves higher, exit when it moves lower — and describes Gap Momentum as an OBV-style cumulative construction on opening gaps (`today's open minus yesterday's close`). The code, not the prose, governs every formula below.
- Licence and rights: this record cites and normalizes the rule (short phrases and definitional recurrence only) and reproduces no extended prose, figures, or performance numbers.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the source's gap-ratio signal-slope construction ported to BTCUSDT 1d with fixed sizing and next-bar-open fills — not a lossless reproduction of the author's chart setup. Researcher-declared adaptations are exactly five: (1) single-asset BTCUSDT Binance USDT-M perpetual venue (the source ships no venue pin); (2) pinned `1d` decision grid (the source speaks of "N days" and publishes on a daily chart; the daily bar grid is the researcher-chosen executable grid, disclosed); (3) fixed 0.01 BTC 1× isolated sizing with explicit 0.05% taker fee per side plus realized funding while long (the source `strategy()` ships no quantity or commission); (4) structural 61-completed-bar warmup (the source ships none — first fully defined signal-slope decision needs bars 0..60); (5) continuous calendar-day grid including weekends (equity daily bars skip weekends/holidays; the 24/7 tape has no skipped days). The gap definition, 40/20 windows, `gapsDn == 0 → 1.0` fence, SMA signal, strict-inequality slope gates, `opentrades` single-position gate, `longOnly = true` short-leg disablement, next-bar-open fills, and no-bracket stance are source-faithful. This record is therefore never evidence that the author's script passes.

Pre-write dedup (2026-11-03): working-tree base is current `main@59a780bd` (536 root strategy records). Case-insensitive content searches for `gapRatio`, `gapUp`, `gapDn`, `Gap Momentum`, `52wKLj6P`, and `PUB;34e22727a1be4a3ebf62de0e3413e9d9` return zero same-source/same-construction hits. `Kaufman` hits are only fenced non-signal mentions in unrelated records (`pivot-point-breakout-kaufman` swing-pivot breakout, KAMA efficiency-ratio adaptive average) — different mechanisms, no gap arithmetic. All 16 open `research/*` PRs enumerated by number (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708) — none is this script, publisher, article, or construction. Nearest pool records differ in signal object: `roc-sign-state-long-flat` (30-bar price ROC sign, no gaps, no ratio, no dual window) and `coppock-curve-zero-state-long-flat` (double ROC smoothing against a zero level, no opening-gap input). Five-axis distinction: no pool record and no open PR conditions exposure on a 40-bar positive/negative opening-gap sum ratio smoothed by a 20-bar SMA and traded on the slope of that signal line.

## Economic mechanism

### Source-reported

Opening gaps carry the overnight information impulse; cumulating them OBV-style — the ratio of summed positive gaps to summed negative gaps over the trailing window, smoothed — separates persistent directional gap pressure from day-to-day noise, so a rising smoothed ratio means upside gap momentum worth holding and a falling one means the impulse has faded. (Author's framing fenced to equities; never adopted as a crypto claim.)

### Research interpretation

Gap-impulse slope hold, long-only, daily cadence. Unlike price-level momentum records there is no close-price ROC, moving-average cross, or band anywhere — the only price reads are each bar's `open` and the prior bar's `close`. Unlike oscillator records there is no fixed level, zero line, or overbought/oversold threshold — the trigger is purely the slope (`signal > signal[1]` vs `signal < signal[1]`) of a smoothed gap-pressure ratio, with exact ties holding. Unlike bracket records there is no stop/target artifact at all: risk is the signal-slope exit to flat, nothing else. The bet, as derived, is purely that the equity opening-gap pressure construction ports arithmetically to BTCUSDT daily boundary gaps — with the economic meaning of those gaps fenced off as a limitation, and no tuning inside this record.

## Signal

Exact rule as pinned (daily decision on completed `1d` bars; next-bar-open market fills; long-flat — any other window, grid, sizing, or fill is a different, unpinned rule):

- R1 — Measure grid: completed `1d` bars of BTCUSDT only. Continuous calendar days (weekends included); no session template, no holiday skip.
- R2 — Per-bar gap: `gap[i] = open[i] − close[i−1]` (needs `i ≥ 1`). Per-bar components: `gapUp[i] = max(gap[i], 0)`, `gapDn[i] = max(−gap[i], 0)`. (Pine `float gapUp = 0.0` re-initializes each bar and the `switch` adds the current bar's signed part — verified against the 47-line source.)
- R3 — Window sums: `gapsUp[i] = Σ gapUp[j]`, `gapsDn[i] = Σ gapDn[j]`, `j = i−39..i`, requiring `i ≥ 40` (40 fully defined per-bar components).
- R4 — Gap ratio: `gapRatio[i] = 1.0` iff `gapsDn[i] == 0`, else `100.0 × gapsUp[i] / gapsDn[i]` (source-ternary fence, pinned).
- R5 — Signal line: `signal[i] = SMA(gapRatio, 20)[i] = (1/20) Σ gapRatio[k]`, `k = i−19..i`, requiring `i ≥ 59`.
- R6 — Slope gates (strict inequalities, pinned; exact equality holds the current state): long trigger `signal[i] > signal[i−1]`; flat trigger `signal[i] < signal[i−1]`.
- R7 — Orders (pinned, `longOnly = true` so the short branch is dead code): flat (`strategy.opentrades <= 0`) and long trigger → market `strategy.entry('long')` filled at the next bar's open; long (`strategy.opentrades > 0`) and flat trigger → `strategy.close_all()` filled at the next bar's open; unchanged slope places nothing. The `strategy.entry('short')` line exists only inside the `else` of `if longOnly` and never fires under the pinned default — the short side is explicitly disabled, not omitted.
- R8 — Risk legs (pinned absence, not invented): no take-profit, no stop-loss, no trailing, no time exit, no cooldown — explicitly none, matching the shipped code (zero `strategy.exit`). The sole closing path is the signal-slope exit to flat.
- R9 — Position state: at most one long at any time (Pine default pyramiding plus the explicit `opentrades` gate; no adds, no partials, no pyramiding, no DCA — explicitly none). After any flat exit the next long-trigger bar may re-enter on schedule (re-entry explicitly allowed; no cooldown — explicitly none). Distinct decisions fill on distinct bar opens, so no same-bar dual-fire exists to sequence.
- R10 — Warmup and gaps: flat until 61 completed `1d` bars (first decision needs `signal[60]` and `signal[59]`, both fully defined). Any platform partial-window behavior before bar 61 is fenced by forced flat and never trades. Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat.
- R11 — Invariant identifier: `TV:pinecoderstasc-52wKLj6P|gap40_sma20_slope|longOnly|independent-derived-v1|BinanceFutures:BTC-USDT:1d|LONG-FLAT|nextbar-MARKET|fee0.0005|lev1x|size0.01|warmup61|2026-11-03` (any constant, window, direction, sizing, fill, or cost change is a different derivative).

## Required data

- Completed `1d` bars of BTCUSDT only: `open` (gap minuend), `close` (gap subtrahend via `close[1]`, ratio/SMA arithmetic, and the `signal[1]` slope reference). No `high`, no `low`, no volume, no funding/OI/mark-index read gates any order, no sentiment/macro/on-chain/cross-venue state.
- Single decision grid: one slope evaluation per completed daily bar close; fills land on the next bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: flat until 61 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every sum is a trailing 40-bar window; the signal is a trailing 20-bar average; the boundary is the slope comparison itself).

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual, 1× isolated, fixed 0.01 BTC per entry, no adds, no compounding. Long-only — the short permission is explicitly unused, so no margin-short modeling is required.
- Order timing (source-native; the source ships next-bar-open fills via Pine defaults): completed-bar-close decision with next-bar-open market fills — the same convention as the admitted `bali-cakici-whitelaw-2011-max-lottery-avoidance` record, which states it outright as compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. One slope evaluation per bar close yields at most one order per bar open, so there is no ambiguous same-bar fill order.
- Pinned-engine path: connector `binance_perpetual`, market `BTCUSDT`, `1d` candles feed, decision timestamp = completed daily bar close, availability timestamp = same close (all inputs are that bar's finalized `open`/`close` history), fill = next bar open MARKET via the directional-controller market-close path. No multi-asset synchronization, no shared capital, no multi-timeframe alignment, no external feed, no leverage/margin accounting beyond a single fixed-size 1× long. The independent auditor must re-verify the `1d` feed and next-open market-close path line-level at the exact head; if either cannot be established, this record must not merge.
- Sizing/capital/costs: fixed 0.01 BTC per entry. Explicit research cost overlay: 0.05% taker fee per side; realized funding accrues while long, flat days carry none — no hypothetical zero funding is claimed anywhere (the source's zero-commission default does not port to crypto). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position at any time; re-entry after a slope exit is explicitly allowed with no cooldown. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.

## Evidence

### Source-reported

The script page and code comments ship every adopted headline fact quoted in Provenance: the Kaufman/TASC lineage, the long-only two-rule framing (enter when the signal line moves higher, exit when it moves lower), the three calculation steps (40-bar positive/negative gap sums, ratio, 20-bar moving average), and the `40` / `20` / `Long Only: true` defaults. The page ships zero adopted performance numbers for this record: no return, win rate, drawdown, trade count, or per-trade figure from the page or reference engine is adopted anywhere — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Logic checks executed during this scout cycle (this cycle's own Python, synthetic inputs only — no real-market replay, no profitability figure):

- Warmup index proof: `gap` needs `i ≥ 1`; 40-bar sums need `i ≥ 40`; 20-bar SMA needs `i ≥ 59`; slope needs `signal` plus `signal[1]` → first decision bar index 60, i.e. flat until 61 completed bars — exact match to R10.
- Ratio arithmetic on a synthetic 100-gap tape: bar-39 window `up = 5.600`, `dn = 3.200` → `ratio = 175.0000`; 20-ratio SMA at first full bar `signal = 175.0000` — matches the pinned formulas.
- Degenerate fence: all-nonnegative 40-gap window gives `gapsDn = 0` → `gapRatio = 1.0` exactly as coded (crypto `1d` tape never exercises this over 40 days, disclosed).
- Order census on the fetched 47-line source: 2 `strategy.entry` (live `long` + dead `short` under pinned `longOnly`), 1 `strategy.close_all`, 0 `strategy.exit`, 0 `strategy.order`, 0 `request.*`, 0 `security(`, 0 `pyramiding`, 0 `process_orders_on_close`, 2 `math.sum`, 1 `ta.sma` — matches the line-by-line read.

### Negative evidence

1. Gap-meaning port fenced: equity opening gaps are overnight informational jumps across a closed session; BTCUSDT `1d` boundary gaps are continuous-tape microstructure (prior close to next open across an arbitrary UTC boundary, weekends included). The arithmetic ports exactly; the economic meaning does not — no informational-gap claim is made here.
2. Calendar port fenced: the source's "N days" are equity trading days; this record's days are continuous calendar days. Weekend trend moves are traded here, never skipped — the derived event set is its own object, never the author's tester output.
3. Number silence fenced: no return, Sharpe, win rate, drawdown, trade count, or per-trade figure from any source is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
4. Fully exposed between flips: once long, any adverse excursion of any size is ridden until the signal slope turns down — there is no guardrail by construction, disclosed.
5. Derivation boundary fenced: the only non-source behavior is the five declared adaptations (venue, `1d` grid, fixed sizing plus costs, 61-bar warmup, continuous calendar); the gap definition, windows, degenerate fence, SMA signal, strict slope gates, single-position gate, long-only disablement, next-open fills, and no-bracket stance are source-faithful. This record is therefore never evidence that the author's script passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `40` / `20` / gap-minus-prior-close / sum-ratio / SMA-slope / strict inequalities / `longOnly` / single position / next-bar-open fills / fixed 0.01 BTC 1× long-flat / BTCUSDT `1d` / continuous calendar / 61-bar warmup are frozen.

- F1 — Gap-input relevance: an SMA-slope twin on close-price ROC (same 40/20 windows and slope gates, no `open`, no gaps) must not improve net expectancy; fail ⇒ the opening-gap input adds nothing over plain price momentum.
- F2 — Ratio relevance: a smoothed net-gap twin (40-bar mean of signed gaps smoothed by 20-bar SMA, same slope gates) must not improve net expectancy; fail ⇒ the positive/negative-ratio normalization is fee-burning decoration over signed gap drift.
- F3 — Slope relevance: a level twin (long iff `gapRatio > signal`, flat otherwise — same windows, no slope comparison) must not improve net expectancy; fail ⇒ trading the slope destroys more expectancy than holding the level state.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out falling-slope stretches costs more in missed drift than it saves in avoided slides.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual (decision grid completed `1d` bar closes; fills at next-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; a spot-only deployment expresses the identical long-flat event set — pinned, not approximated — since no short leg exists). Extension to other house-universe assets, timeframes, windows, or grids would be a different, unpinned claim.

## Limitations

- Single-asset port: the author's evidence is equity daily gaps; BTCUSDT boundary-gap behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Boundary-gap thinness: on a continuous tape most daily `open − close[1]` gaps are tiny microstructure prints, so the 40-bar ratio can sit in long indecisive stretches with frequent slope flips — the resulting turnover is the coded trade, disclosed.
- Slope-lag exits: the SMA(20) slope turns after the ratio turns, so exits structurally lag pressure peaks — disclosed, not tunable here.
- UTC-boundary dependence: `1d` bar boundaries are venue-day conventions; a different day-boundary convention would print different gaps and a different event set — flagged as an implementation obligation to pin the venue's `1d` close convention, not strategy behavior.
- No guardrail: fully exposed between slope flips by construction (see Negative evidence 4).

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- TradingView strategy by PineCodersTASC (script ID part `PUB;34e22727a1be4a3ebf62de0e3413e9d9`), fetched and read live 2026-11-03: https://www.tradingview.com/script/52wKLj6P-TASC-2024-01-Gap-Momentum-System/
- Idea lineage (context only, no numbers adopted): Perry J. Kaufman, "Gap Momentum Indicator — Taking A Page From The On-Balance Volume", TASC January 2024 (Vol. 42, Issue 1).
