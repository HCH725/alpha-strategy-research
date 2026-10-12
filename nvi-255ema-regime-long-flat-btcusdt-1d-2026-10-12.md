---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: NVI 255EMA smart-money regime long-flat on BTCUSDT 1d bars
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-12
sources:
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/negative-volume-index-nvi
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# NVI 255EMA smart-money regime long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (StockCharts ChartSchool page fetched in full during this cycle, 2026-10-12, Markdown edition served by the publisher itself):

- StockCharts ChartSchool, `Negative Volume Index (NVI)` — canonical URL: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/negative-volume-index-nvi (Markdown twin at the same path plus `.md`; the page advertises Markdown editions for agent consumption, so the `.md` fetch is the publisher's own machine-readable form, not a scrape artifact). Lineage stated on-page: Paul Dysart first developed the indicator in the 1930s (original version cumulated Net Advances on decreased-volume periods); Norman Fosback (author of *Stock Market Logic*) adjusted it by substituting the percentage price change for Net Advances; the SharpCharts formula uses this Fosback version.
- Pinned computation (§SharpCharts Calculation, verbatim in sense): (1) Cumulative NVI starts at 1000; (2) add the Percentage Price Change to Cumulative NVI when Volume Decreases; (3) Cumulative NVI is Unchanged when Volume Increases; (4) apply a 255-day EMA for Signals. The spreadsheet note pins the scale: the Price %Change is multiplied by 100, and NVI values are applied each period starting at 1000 — i.e. the Fosback update is additive in percentage points, not multiplicative. The Volume%Change column governs: a negative value routes the price %Change into the NVI column, a positive value routes nothing (a zero volume change is not negative, so equality leaves NVI unchanged — pinned by the same column rule).
- Pinned signal (§Signal, verbatim in sense): "According to Fosback, the odds favor a bull market when NVI is above its 255-day EMA and the odds favor a bear market when NVI is below." Asymmetry disclosed on-page, never smoothed over: "There is a 96% chance of a bull market when NVI is above its 255-day EMA, but only a 53% chance of a bear market when NVI is below its 255-day EMA." The page further warns of "plenty of whipsaws (bad signals)" under the 255-day EMA (1998 and 2001–2002 Dow examples) and of structural lag ("Chartists can expect some lag because moving averages lag and a 255-day EMA is being used").
- Portability licence (§Fine Tuning, verbatim in sense): "Even though NVI was designed with a major stock index in mind, chartists can use NVI with ETFs, stocks or anything that has volume." This sentence — not Hermes — authorises carrying the indicator to any volume-printing tape. The Bottom Line fences the carry: "this indicator was designed for broad market indices and exchange volume. It can be used on stocks and ETFs, but NVI does not always act as expected" and "should not be used on its own."
- Execution semantics (§Suggested Scans): the publisher's own Bullish/Bearish scans fire on signal-line crosses (`[NVI x NVI Signal(255)]` bullish; `[NVI Signal(255) x NVI]` bearish), confirming the regime is evaluated bar by bar against the 255 EMA and positions turn exactly at crosses — the state-hold pin in Signal is event-identical to cross entries/exits.
- No PVI page exists in ChartSchool (the `positive-volume-index-pvi` path returns Page Not Found with NVI/RVOL/RSI/PVO/MFI suggestions) — this record therefore pins NVI only and adopts no Positive Volume Index leg of any kind.
- Licence and rights: this record cites and normalizes the rule (short phrases and formulas only) and reproduces no chart, spreadsheet, figure, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the Fosback/ChartSchool NVI-vs-255EMA bull/bear regime gauge ported to one crypto asset as a long-flat system — not a lossless reproduction of the source's broad-index timing practice. Researcher-declared adaptations are exactly seven: (1) direction pin long-only — the source's bear leg maps to flat, never short (rationale: Fosback's own 53% bear-side asymmetry plus unverifiable historical short funding, mirroring reviewer-accepted long-flat precedent; see Execution assumptions); (2) single-asset BTCUSDT Binance tape under the publisher's own "anything that has volume" licence (the index-breadth/Net-Advances Dysart original and every multi-security claim are fenced, never carried); (3) state-hold evaluation each completed close with orders only on target change (event-identical to the publisher's scan-cross semantics, pinned to remove any cross-vs-hold ambiguity); (4) next-open market fills on the `1d` grid (the source is cadence-silent; daily closes are the declared port); (5) fixed 100%-equity single position at 1× with no leverage (the source ships no sizing); (6) no stop, no target, no trailing, no time exit (the source ships no risk leg anywhere — exits are regime-driven only, source-faithful absence); (7) a declared EMA-seed/warmup convention (seed NVI 1000 at first bar; EMA-255 α=2/256 seeded with the SMA of the first 255 NVI values; first decision at the close that completes the seed window — the publisher pins the 255 length but no seeding arithmetic, so the arithmetic is disclosed researcher specification, never presented as a source fact). The 1000 seed, the additive percentage-point update, the strict-decrease volume gate, the 255-day EMA length, and the above/below regime semantics are source-faithful.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `dysart`, `fosback`, `smart.money`, `255.day`, `255-day`, `255.ema`, and `NVI Signal` return zero strategy records — the sole `\bNVI\b`/`\bPVI\b` hit pool-wide is the PVO record's prose phrase "negative volume-momentum leg" describing its own Percentage Volume Oscillator polarity, never a Dysart/Fosback index. Word-boundary `\bPVI\b` as an indicator returns zero records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `pvo-signal-cross-volume-momentum-two-sided-btcusdt-1d-2026-10-12.md` trades the Percentage Volume Oscillator's double-EMA spread state (a bounded volume-rate oscillator, no cumulative smart-money line, no 255-length anything); `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md` cumulates signed volume on every bar (up-volume moves count — the exact moves NVI discards) against a fast EMA cross; `pvt-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-11.md` cumulates volume-scaled price changes on all bars the same way; `cmf-velocity-zero-cross-ema200-bracket-two-sided-btcusdt-1d-2026-10-10.md` and `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h-2026-10-12.md` read Money-Flow/Accumulation-Distribution placement inside each bar's range, never a decreased-volume-only filter; no pool record discards up-volume price action entirely. Five-axis distinction: no pool record and no open PR cumulates percentage price change exclusively on decreased-volume bars from a 1000 seed against its own 255-day EMA for a multi-year smart-money regime.

## Economic mechanism

### Source-reported

Smart-money footprinting: informed participants transact quietly on low-volume days while uninformed crowd volume dominates high-volume days, so cumulating price change only on decreased-volume days isolates the informed drift ("NVI counts price changes when volume decreases and discounts price changes when volume increases"). The 255-day EMA of that line is the year-scale bull/bear partition: above it the odds "favor a bull market" at 96%, below it they favor a bear market at only 53% — the asymmetry is the source's own finding, carried verbatim.

### Research interpretation

Year-scale informed-drift regime port: the decreased-volume filter throws away most of the tape (every up-volume bar contributes exactly nothing) and the 255-day EMA low-passes what remains, so the derived system can only be long during persistent smart-money accumulation years and sits flat through everything else — whipsaw bleed inside choppy regimes is structurally converted into flat time rather than stop-outs, because there is no stop to hit and no cross to chase mid-regime. Unlike every pool volume record (OBV/PVT/PVO/CMF/Chaikin/MFI), which read all-bar flow or intrabar placement, this rule is blind to the majority of bars by construction; unlike moving-average trend records it smooths a cumulative volume-filtered line rather than price itself, so a vertical low-volume melt-up and a vertical high-volume blow-off print opposite NVI readings for the same price path. The bet, as derived, is purely on decreased-volume drift persistence at the ~year scale, never on a level, band, oscillator zone, calendar date, or funding print.

## Signal

Exact rule as pinned (1000 seed / strict-decrease gate / additive percentage-point update / EMA-255 / state-hold — any other value is a different, unpinned rule):

- Series (pinned, Fosback/SharpCharts version): let `C_t`, `V_t` be the close and printed bar volume of completed `1d` bar `t` (`t = 1` is the first available bar). `NVI_1 = 1000`. For `t ≥ 2`: `NVI_t = NVI_{t-1} + 100 × (C_t − C_{t-1}) / C_{t-1}` if `V_t < V_{t-1}` (strictly), else `NVI_t = NVI_{t-1}` (volume increase or equality contributes nothing — the zero-change case follows the page's Volume%Change column rule, negative-only routing). Volume units are immaterial: only the strict inequality of consecutive venue prints is read, so base- versus quote-denominated feeds give identical events. Division is safe: crypto closes are strictly positive.
- Regime line (declared arithmetic, pinned): `EMA_t` is the 255-period exponential moving average of the NVI series with `α = 2/(255+1)`, seeded with the simple mean of `NVI_1 … NVI_255`. `EMA_t` is undefined before `t = 255`; no decision may reference it there.
- Position target (pinned, strict): evaluated at the close of each completed `1d` bar `t ≥ 255`: `NVI_t > EMA_t` → long; `NVI_t ≤ EMA_t` → flat (equality pinned to flat — measure-zero on live tape, no tie semantics beyond this). The bear/short side of the source gauge is explicitly disabled, not underspecified.
- Orders (pinned): at most one order event per bar, placed for the next `1d` open after the decision bar: flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials, no second decision inside the fill bar for any reason including large adverse excursion. Entry and exit can never co-fire: the target is a single state per bar.
- Risk legs (pinned absence, not invented): the source ships no stop/target/trailing/time-exit concept anywhere — the sole position-closing path is the next regime bar mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no time exit; a year-scale adverse drift is ridden or sat out in full by construction.
- Direction: long-flat (derived pin). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` closes and printed bar volumes of BTCUSDT only: two scalars per bar (`C_t`, `V_t`). No `open` (except as fill price), no `high`, no `low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, breadth, Net Advances, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind. The Dysart Net-Advances original is fenced — only the Fosback percentage-change version is computed.
- Single decision grid: completed daily bar. One evaluation per close; fills land on the next daily bar's open. All inputs are completed-bar prints — no provisional close or unfinished volume is ever used. Bar volume is final at bar close on the venue tape.
- Warmup: 255 completed `1d` bars before the first decision (the EMA seed window must exist in full). Bars 1–254 are flat by record rule; the first decidable close is bar 255 and its fill lands on bar 256's open. No signal before the seed window completes may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (bar membership is the venue's own daily grid — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port under the publisher's "anything that has volume" licence; no cross-venue equivalence claimed). The venue's daily volume print replaces the page's exchange-volume concept one for one — both are completed-bar venue totals, never modelled intraday.
- Order timing (declared port; the source is cadence-silent): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are regime-change market entry/close-all orders, and at most one order exists per bar — there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (the source ships no sizing). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-flat form holds genuine flat spells between a non-positive regime and the next positive one, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat spell needs only the next long-regime close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The page ships the full construction adopted here: the 1000 seed, the add-percentage-change-on-decrease / unchanged-on-increase update, the percentage-points ×100 scale note, the 255-day EMA signal length, the above/below bull/bear partition with the 96%/53% asymmetry, the scan-cross execution semantics, and the "anything that has volume" portability licence. It ships zero adopted performance numbers for this record: the 96%/53% figures describe Fosback's broad-index odds, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Index-designed gauge, fenced: the indicator "was designed for broad market indices and exchange volume" and "does not always act as expected" on single names; the Bottom Line advises against standalone use. This record is a deliberate single-asset port under the page's own licence sentence — it is never evidence that NVI times BTCUSDT well.
2. Whipsaw admission, carried: the source documents "plenty of whipsaws (bad signals)" under the 255 EMA with concrete 1998/2001–2002 episodes. The derived system converts those episodes into flat churn and late re-entries, disclosed, not filtered.
3. Asymmetric short side, fenced by direction pin: the 53% bear leg is the source's own reason the short side is disabled here; long-flat economics differ from two-sided gauge economics by construction.
4. No hidden risk layer: the source ships no stop/target/trailing concept — the sole position-closing path is the next regime bar. The absence of any stop is source-faithful absence, disclosed, not a tunable parameter here.
5. Fully exposed inside the long regime: once long, the system rides the entire adverse excursion with no guardrail — a −50% drawdown inside an above-EMA regime is held to the last bar by construction. This is the coded trade, disclosed, not a tunable parameter here.
6. Seed-arithmetic boundary, fenced: the publisher pins the 255 length but no EMA-seeding arithmetic — the SMA-of-first-255 seed is declared researcher specification. Alternative seedings (first-value seed, Wilder smoothing, SMA-255 signal instead of EMA-255) would be different, unpinned rules; early-regime history shifts slightly under reseeding while the additive NVI path itself is seed-exact.
7. Strict-gate boundary, pinned: volume equality leaves NVI unchanged via the negative-only column rule; a `≤`-gated variant would be a different, unpinned rule — none is admitted here.
8. Derivation boundary fenced: the only non-source behavior is the seven declared adaptations (long-only pin, single asset, state-hold evaluation, daily next-open grid, fixed sizing, warmup/seed convention, house costs); seed 1000, additive update, strict-decrease gate, EMA-255 length, and above/below semantics are source-faithful. This record is therefore never evidence that the source's broad-index timing passes anything.
9. The 1000-seed / strict-decrease / additive-update / EMA-255 / state-hold / single-position long-flat / signal-only-exit stance is pinned, not removed: shortening the signal length, adding the 100-day correction EMA from the Fine Tuning section, drawing NVI trendlines, adding a stop/target/filter/cooldown, re-enabling the short leg, trading intrabar, or sizing partially instead of 100% equity would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1000 seed / strict-decrease gate / additive update / EMA-255 / state-hold / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Signal-length relevance: replacing the pinned EMA-255 with EMA-100 (the page's own correction-scale EMA) must not improve net expectancy; fail ⇒ the year-scale partition carries no advantage over the correction scale.
- F2 — Filter relevance: replacing the decreased-volume-only update with an every-bar percentage-change cumulation (the discarded OBV-style leg) must not improve net expectancy; fail ⇒ the volume gate does no work and the record is a slow trend-follower in disguise.
- F3 — Direction-pin relevance: enabling the symmetric short leg (bear-regime short instead of flat, cost-loaded) must not improve risk-adjusted expectancy; fail ⇒ the long-only pin discards the gauge's better half — or the short leg's funding load dominates.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` closes; close-plus-volume arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market prints volume on every daily bar (bar membership is the venue's own daily grid — deterministic on any continuously traded tape). Extension to other house-universe assets, other signal lengths, or the PVI mirror would each be a different, unpinned claim.

## Limitations

- Researcher direction pin: the gauge is two-sided — long-flat is a researcher choice; two-sided economics would differ by construction, and the disabled leg is the page's weaker (53%) half.
- Single-asset port: the source's evidence is broad-index timing; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No price stop, no intra-regime exit: adverse excursion inside the long regime has no guardrail; the next decision is one bar away but the regime itself can persist for years. This is the source-faithful posture, disclosed as the record's principal risk.
- EMA lag: the page warns of structural lag under a 255-day average — regime turns print months after price turns by construction.
- Standalone-use caveat: the publisher advises against using NVI on its own; this record is a standalone specification for admission purposes, never a recommendation.
- Unused cost silence: the source reports no cost accounting; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 254 bars are flat by record rule, so any textbook regime completing inside the seed window is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockCharts ChartSchool, Negative Volume Index (NVI) (lineage Dysart/Fosback, SharpCharts formula, 255-day EMA signal rule with 96%/53% asymmetry, scans, portability licence; fetched full Markdown edition 2026-10-12): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/negative-volume-index-nvi
