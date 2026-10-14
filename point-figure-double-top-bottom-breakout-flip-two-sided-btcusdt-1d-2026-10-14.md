---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Point-Figure double-top breakout double-bottom breakdown flip two-sided on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-14
sources:
  - https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/introduction-to-point-and-figure-charts
  - https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bullish-breakouts
  - https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bearish-breakdowns
  - https://help.stockcharts.com/charts-and-tools/other-charting-tools/p-and-f-charts
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Point-Figure double-top breakout double-bottom breakdown flip two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (ChartSchool GitBook pages plus the Support Center P&F page, fetched over HTTPS during this cycle via text extraction):

- Construction canon: `Introduction to Point & Figure Charts` states the ChartSchool articles are based on the classic 3-box reversal method; gives the exact High-Low Method rules (in an X-Column use the high when another X can be drawn and ignore the low; use the low only when another X cannot be drawn and the low triggers a 3-box reversal; ignore both otherwise — mirror rules for an O-Column); works a full Day-1-to-Day-5 construction example (Day 4: a 3-box reversal adds three X's starting one box above the low of the previous column); documents percentage scaling as fixed-percentage-of-price boxes.
- Buy-signal canon: `P&F Bullish Breakouts` — `The most basic P&F buy signal is a Double Top Breakout, which occurs when an X-Column breaks above the high of the prior X-Column`, with the two X-Columns separated by an O-Column (first X establishes direction, middle O establishes support, third X triggers the higher high).
- Sell-signal canon: `P&F Bearish Breakdowns` — `The most basic P&F sell signal is a Double Bottom Breakdown, which occurs when an O-Column breaks below the low of the prior O-Column`, mirror-separated by an X-Column.
- Platform defaults (Support Center P&F page, Chart Scaling section, verified verbatim): `Percentage scaling ... The default is 1.0 for 1%` and `the Reversal field ... The default value is 3 boxes`. The Traditional box-size table and Dynamic (ATR) scaling are documented on the same page but never adopted here.
- The pages ship zero performance numbers for these patterns (no return, Sharpe, win rate, trade count, table, or figure) — this record claims no source-reported performance and no reproduced performance. The horizontal/vertical-count price objectives are documented measuring techniques for reward sizing, never order triggers here (fenced, see Negative evidence).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of a source trading system, because the source is a charting canon, not a backtest: it ships no order, no sizing, no fill convention, no venue, and no exit rule for these patterns. Researcher-declared adaptations are exactly six: (1) research market/timeframe BTCUSDT completed `1d` bars (the source's equity examples are daily-bar-charted securities — the daily frame is preserved, the venue is ported); (2) percentage 1% boxes with 3-box reversal, numerically equal to the documented platform defaults (Traditional-table and ATR scalings fenced as different, unpinned rules); (3) log-level box arithmetic plus the first-bar seeding rule below (the source defines boxes and reversals in prose with a worked example — the integer-level concretization is the researcher's, fully specified); (4) next-`1d`-open fills on signals evaluated at the completed-bar close (the source declares no execution timing); (5) opposite-signal flip-only book with explicitly no stop/target/trailing/time leg (the source declares no exit — the flip book is the declared assembly, stated here); (6) an adopted 90-bar warmup with pre-warmup bars flat by record rule (the source needs no warmup concept — see Required data for the structural rationale). The High-Low construction rules, the 3-box reversal distance, the verbatim double-top/double-bottom signal definitions, two-sided direction, and the source-reported whipsaw proneness are source-native and unmodified.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `point-figure`, `point & figure`, `point and figure`, `kagi`, `renko`, `three-line`, `line-break`, `pnf`, `double-top`, `double-bottom`, `double top`, `double bottom`, `stockcharts`, and `chartschool` return zero strategy records using any box-column chart construction (the two incidental hits are `trendline-break` in Special K and prose `reclaim` context in Fibonacci — different mechanisms, indicators, and sources). The pool's channel breakouts (Donchian/Darvas/NR7/Keltner/Turtle/Dual Thrust/R-Breaker) are all time-based bars with raw-price levels, never box-filtered columns. Open `research/*` PRs are only #48 (Larry Williams streak long), #49 (Gaussian StochRSI long), #63 (SuperTrend long), #89 (Chandelier long), #92 (SSL two-sided) — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (price-move-only X/O box columns with no time axis, versus every pool record's time-barred indicators, bands, pivots, grids, or calendars), signal construction differs (column-extreme-vs-prior-column-extreme events on 1%/3-box High-Low columns, versus closes-vs-levels on raw bars), exits differ (opposite-pattern flip-only book with explicitly no stop/target/trailing/time leg), source identity differs (StockCharts ChartSchool + Support Center, first of its family in the pool), and direction handling differs (two-sided flip system, always-in-market after the first signal with an explicit pre-first-signal flat state).

## Economic mechanism

### Source-reported

Filtered supply/demand auction (ChartSchool framing): X-Columns are rising-price demand regimes, O-Columns are falling-price supply regimes; insignificant moves are filtered by the box, and only a 3-box counter-move earns a new column. A Double Top Breakout means buyers finally create more demand than the supply that capped the prior X-Column — `break above the prior high shows strength associated with an uptrend`. A Double Bottom Breakdown means the buyers who held the prior O-Column low can no longer absorb supply — `the inability to hold the prior low shows weakness associated with a downtrend`. Wider multi-column patterns mark better-established levels; the double is the most basic and most common signal of the family (page prose; no number attached).

### Research interpretation

Box-filtered regime-break speculation on a single 24/7 instrument. Unlike the pool's bar-close breakout systems (Donchian/Turtle/Dual Thrust/R-Breaker), which fire on raw closes crossing raw levels every bar, this system cannot fire until price has travelled a full 1% box beyond a column extreme that itself survived a 3% adverse filter — slow grinds that never print a higher box are ignored no matter how persistent, while a single vertical day can seed, extend, and break in sequence. Unlike oscillator-cross systems it reads no normalized momentum, no average, no band, no volume, and no calendar — only the integer geometry of filtered columns. Unlike trailing-stop flip systems (UT Bot/Chandelier/SSL/SuperTrend) the state is column-membership, not distance from a moving stop, so flat chop inside the current column prints no event at all. The bet is that a filtered higher-high (lower-low) on the daily auction carries multi-day directional persistence often enough to survive the family's famously common whipsaws (see Negative evidence). The 1%/3-box filter is bought with missed sub-1% inflections and late entries after vertical moves; the flip-instead-of-stop posture is bought with full adverse carry between opposite patterns.

## Signal

Exact rule as pinned (any other box size, reversal amount, scaling, pricing method, or fill timing is a different, unpinned rule):

- Frame: completed BTCUSDT `1d` bars (UTC days) with `H`/`L`/`C`. One evaluation per completed bar, in bar order.
- Box level: `L(p) = floor(ln(p / 1.0) / ln(1.01))` for `p` in USDT — integer 1% percentage boxes. All comparisons below are strict integer-level comparisons, so no boundary-inclusivity case exists.
- State: current column (`none`, `X` with top `Xt`, `O` with bottom `Ob`), plus `lastX` (extreme top of the most recent completed X-column, if any) and `lastO` (extreme bottom of the most recent completed O-column, if any). Columns strictly alternate by construction.
- Seed (researcher concretization, disclosed): `R = L(C)` of the first bar ever processed; state stays `none` until some bar prints `L(H) >= R+1` (open X with bottom `R+1`, top `L(H)`) or `L(Lw) <= R-1` (open O with top `R-1`, bottom `L(Lw)`); `R` never moves before seeding.
- X-column update on bar `(H, Lw)` (source High-Low priority): if `L(H) > Xt` → extend `Xt = L(H)`, ignore the low entirely (even a 3-box low prints nothing — source Day-3 rule); elif `L(Lw) <= Xt-3` → reversal: new O-column with top `Xt-1`, bottom `L(Lw)` (the full traversed length, matching the worked example's three drawn X's generalized); else no change.
- O-column update (mirror): if `L(Lw) < Ob` → extend `Ob = L(Lw)`, ignore the high entirely; elif `L(H) >= Ob+3` → reversal: new X-column with bottom `Ob+1`, top `L(H)`; else no change.
- When a new X-column opens, the finished X-column's extreme (if a prior X existed) becomes `lastX` before further comparison; mirror for `lastO`. The first X (O) column has no prior — it can never fire a signal itself.
- Double Top Breakout (source-native verbatim): on the completed bar where the current X-column's top first satisfies `Xt > lastX` → buy signal. Double Bottom Breakdown (mirror): on the bar where the current O-column's bottom first satisfies `Ob < lastO` → sell signal. At most one firing per column per side (the extreme is monotonic within a column). A reversal bar may legally complete the new column's signal in the same step (e.g. a fresh O-column bottoming below `lastO` on its formation bar) — single outcome per bar, so no ordering ambiguity exists.
- Orders: evaluated at the completed-bar close, executed at the next `1d` open. Buy signal from flat → open long; from short → flip to long in one step at the same open price. Sell signal from flat → open short; from long → flip to short in one step. Same-side repeats ignored (no adds, no partials, no pyramiding). Flat before the first signal by construction; always-in-market after it (the flip-only book has no flat leg).
- Direction: two-sided flip system. Risk legs (declared absences — the source ships none for these patterns): no stop-loss, no take-profit, no trailing, no time exit — the sole position-changing paths are double-top buys and double-bottom sells, exactly as assembled above.

## Required data

- Completed `1d` bars of BTCUSDT: `H`/`L` (column extension and reversal checks), `C` (seeding anchor only; never a comparison input thereafter). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, breadth, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (declared research frame on the source-native daily charting interval; no second subscription exists — the P&F columns are an arithmetic transform of the same daily bars, not a second feed).
- Warmup: the structural need is seeding plus at least one finished X/O cycle plus comparison columns (≥3 columns with both a `lastX` and a `lastO` reference). The adopted warmup is the first 90 completed `1d` bars flat by record rule (predeclared researcher choice — several multiples of the structural need on BTC daily volatility, where 1% boxes turn over in days). No repainting (a completed column extreme never revises — extensions only grow, reversals open new columns), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar; forming bars never gate orders.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (declared port; the source venues are daily-charted equities — no cross-venue equivalence is claimed beyond OHLC arithmetic).
- Order timing (predeclared derivation): completed-bar decision with next-`1d`-open execution for entries and flips, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source declares no execution timing; this record does not claim source fills. No maker-touch, queue, or intrabar-path-dependent fill: with one decision per bar and a single flip outcome per bar, there is no same-bar entry ordering ambiguity.
- Sizing/capital/costs: the source ships no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply here, never presented as source-native behavior.
- Concurrency: at most one single-unit position (long or short) at any time after the first signal; every position-changing event flips in full in one step; no cooldown specified — explicitly none, not invented. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The pages ship the full adopted construction (classic 3-box-reversal basis, the complete High-Low Method rule set with priority and ignore-both cases, the Day-1–Day-5 worked construction example, percentage scaling mechanics, the `1.0 for 1%` box default, the `3 boxes` reversal default, the verbatim double-top and double-bottom signal definitions with their separated-column anatomy, and the bull/bear pattern taxonomies they head). They ship zero performance numbers for these patterns: no return, no Sharpe, no win rate, no profit factor, no trade count, no tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Source-reported whipsaw proneness, admitted plainly: both pattern pages call the double the most common signal in the P&F universe and the most prone to whipsaw and failure, to be used only with wider technical context. This record trades every double mechanically with no wider-context filter — chop oscillating across adjacent column extremes flips the full unit pattern after pattern, disclosed, not smoothed.
2. Price objectives fenced: the horizontal/vertical-count objectives are documented reward-measuring techniques with worked arithmetic, never triggers — adopting any of them as an exit or target would be a different, unpinned rule; none is admitted here.
3. ATR-scaling repaint warning fenced: the source warns Dynamic (ATR) scaling changes the box size as ATR changes so prior signals may disappear. This record pins fixed-percentage boxes precisely to keep every completed column immutable — the ATR variant would be a different, unpinned rule; none is admitted here.
4. Traditional-table alternative fenced: the ChartCraft/Dorsey price-range table is documented on the same support page; adopting it would re-anchor every box and signal — a different, unpinned rule; none is admitted here.
5. No risk layer of any kind, admitted plainly: a trend grinding against the position without ever printing an opposite double is held in full, and a vertical adverse move on the entry bar itself has no guardrail. Adding any stop would be a different, unpinned rule — none is admitted here.
6. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` venue port, the 1%/3-box default pins (numerically equal to documented platform defaults), the log-level arithmetic plus first-bar seeding, next-open fills, the flip-only book with all no-stop/no-target/no-trailing/no-time exclusions, and the adopted 90-bar warmup with record-rule pre-warmup flat — all predeclared above; the High-Low construction rules, the 3-box reversal distance, the verbatim double-top/double-bottom definitions, two-sided direction, and the pre-first-signal flat state are source-native. This record is therefore never evidence that any StockCharts-charted deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: High-Low method / 1% boxes / 3-box reversal / verbatim double definitions / flip-only book / two-sided / `1d` BTCUSDT / next-open fills / 90-bar warmup are frozen.

- F1 — Filter relevance: replacing the 1%/3-box columns with raw daily closes (long on close above the prior 20-bar high, short on close below the prior 20-bar low, same flip-only book, same frame/fills) must not improve net expectancy; fail ⇒ the box filter plus column memory add nothing over a plain daily breakout.
- F2 — Flip relevance: replacing the always-in-market flip book with a flat-after-signal book (each opposite double closes to flat instead of opening the contra unit, re-entering only on the next same-direction double) must not improve net expectancy; fail ⇒ staying perpetually exposed through flips adds nothing over breakout-and-hold episodes.
- F3 — Pricing-method relevance: rebuilding the identical system on the Close Method (one price per bar, same 1%/3-box settings, same signals, same book) must not improve net expectancy; fail ⇒ the High-Low intrabar range information adds nothing over close-only columns.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a daily-equity charting canon). The OHLC arithmetic ports across perpetual venues without structural change; the 24/7 market needs no session approximation (UTC-day bars, fully specified above). Both sides are explicit legs, so a spot-only deployment expresses the long half only while every flip-to-short stays venue-gated (short permission unused, never silently converted) — a spot-only variant would be a different, unpinned claim. No funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Charting canon, not a trading system: the source declares entries only as pattern vocabulary with no exits, economics, or timing — the flip book, fills, sizing, costs, and warmup are the researcher's declared assembly. Backtest economics of any other assembly differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about any StockCharts-charted deployment's performance.
- No source cost declaration of any kind: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Always-in-market exposure: after the first signal the book is never flat by rule, so adverse drift between opposite doubles is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Static 1%/3-box filter: the grid never adapts to volatility regimes, so a volatility expansion prints late signals after vertical moves and a compression prints dense whipsaw columns — fixed-filter behavior is the coded trade, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- ChartSchool P&F construction canon (3-box basis, High-Low Method, worked example, percentage scaling): https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/introduction-to-point-and-figure-charts
- ChartSchool P&F buy-signal canon (Double Top Breakout definition and anatomy): https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bullish-breakouts
- ChartSchool P&F sell-signal canon (Double Bottom Breakdown definition and anatomy): https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bearish-breakdowns
- StockCharts Support Center P&F page (platform defaults: Box Percent `1.0 for 1%`, Reversal `3 boxes`; Traditional table and ATR scaling fenced as not adopted): https://help.stockcharts.com/charts-and-tools/other-charting-tools/p-and-f-charts
