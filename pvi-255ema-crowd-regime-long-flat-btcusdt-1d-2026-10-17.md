---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: PVI 255EMA crowd-money regime long-flat on BTCUSDT 1d bars
created: 2026-10-17
updated: 2026-10-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-17
sources:
  - https://www.incrediblecharts.com/indicators/positive_volume_index.php
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PVI 255EMA crowd-money regime long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (Incredible Charts indicator page fetched in full during this cycle, 2026-10-17, ~27KB HTML, full-text extracted on the runner):

- Incredible Charts (Colin Twiggs), `Positive Volume Index` — canonical URL: https://www.incrediblecharts.com/indicators/positive_volume_index.php. Lineage stated on-page: the Positive Volume Index was introduced in *Stock Market Logic* by Norman Fosback and is often used in conjunction with the Negative Volume Index to identify bull and bear markets. Assumption stated on-page: the uninformed crowd dominates trading on active days (NVI assumes smart money dominates quiet days). Filter stated on-page: Positive Volume Index highlights days when volume is up on the previous day; Negative Volume Index highlights days when volume is down.
- Pinned signal (verbatim in sense): "Fosback maintains that there is a 67% probability of a bear market when Positive Volume Index is below its 1 year moving average. The probability drops to 21% when PVI is above the moving average." And: "Positive Volume Index crossing to below its one year moving average confirms the approach of a bear market." The worked example applies the gauge to a single name (Procter & Gamble) with a 9-day exponential moving average (fast MA) and a 255-day exponential moving average (slow MA): fast crosses below slow is the Bear signal `[-]`; fast crosses back above slow ends the bear signal `[+]`. Smoothing characterised on-page: "Indicator smoothing (the fast MA) eliminates several whipsaws from the Positive Volume Index."
- Pinned setup: "The default setting for the exponential moving average is 255 days."
- Pinned formula (verbatim in sense): "Take yesterday's Positive Volume Index. If today's volume is greater than yesterday, add: { ( Close [today] − Close [yesterday] ) / Close [yesterday] } × PVI [yesterday]. Otherwise, add zero." The gate is a strict increase (equality adds zero — unchanged).
- Licence and rights: this record cites and normalizes the rule (short phrases and formulas only) and reproduces no chart, figure, or extended prose.
- A second corroborating page (Fidelity Learning Center PVI guide) was attempted this cycle and refused machine access (bot-wall Access Denied) — disclosed here; zero facts in this record are sourced from it.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the Fosback crowd-money PVI-vs-255EMA bull/bear gauge ported to one crypto asset as a long-flat system — not a lossless reproduction of the source's equity-market timing practice. Researcher-declared adaptations are exactly seven: (1) direction pin long-only — the source's bear leg maps to flat, never short (rationale: the bull leg is the gauge's reliable half at 79% implied odds, mirroring reviewer-accepted long-flat precedent; see Execution assumptions); (2) single-asset BTCUSDT Binance tape (the page itself demonstrates single-name application on Procter & Gamble, so single-name use is source-demonstrated; the crypto-asset port itself remains a declared adaptation); (3) state-hold evaluation each completed close with orders only on target change (event-identical to the page's cross semantics, pinned to remove any cross-vs-hold ambiguity); (4) next-open market fills on the `1d` grid (the source is cadence-silent; daily closes are the declared port); (5) fixed 100%-equity single position at 1× with no leverage (the source ships no sizing); (6) no stop, no target, no trailing, no time exit (the source ships no risk leg anywhere — exits are regime-driven only, source-faithful absence); (7) a declared seed/warmup convention (PVI seeded at 1000; EMA-255 α=2/256 seeded with the SMA of the first 255 PVI values; first decision at the close that completes the seed window — the publisher pins the 255 length but no seeding arithmetic, so the arithmetic is disclosed researcher specification, never presented as a source fact; cross events are seed-scale-invariant in any case — see Signal). The strict-increase volume gate, the multiplicative percentage-change update, the 255-day EMA length, and the above/below regime semantics are source-faithful.

Pre-write dedup (2026-10-17): working-tree case-insensitive searches for `\bpvi\b`, `positive.volume`, `positive_volume`, `fosback`, `dysart`, and `crowd.money` return no Positive Volume Index record — the sole `\bPVI\b` hit pool-wide is the NVI record's own fenced disclaimer adopting no PVI leg; `positive volume` hits elsewhere are generic prose (`ease-of-movement` degenerate-arithmetic note, `gervais-kaniel-mingelgrin` volume-guard note), never the index; the sole `incrediblecharts` hit outside this record is the Wilder volatility-stops record citing that publisher's different `volatility_stops.php` page. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided), #251 (Swift 2-year MA multiplier zone-state long-flat) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `nvi-255ema-regime-long-flat-btcusdt-1d-2026-10-12.md` cumulates percentage price change exclusively on decreased-volume bars (the exact bars PVI discards) as a smart-money gauge with 96%/53% asymmetry — this record is its disjoint mirror; `pvo-signal-cross-volume-momentum-two-sided-btcusdt-1d` trades the Percentage Volume Oscillator's double-EMA spread state (a bounded volume-rate oscillator, no cumulative crowd line, no 255-length anything); `obv-ema-crossover-trend-two-sided-btcusdt-1d` and `pvt-ema-crossover-trend-two-sided-btcusdt-1d` cumulate signed/scaled flow on every bar (down-volume moves count — moves neither Dysart/Fosback index reads selectively); `cmf-velocity-zero-cross-ema200-bracket-two-sided-btcusdt-1d` and `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h` read Money-Flow/Accumulation-Distribution placement inside each bar's range, never an increased-volume-only filter. Five-axis distinction: no pool record and no open PR cumulates percentage price change exclusively on increased-volume bars from a 1000 seed against its own 255-day EMA for a multi-month crowd-money regime.

## Economic mechanism

### Source-reported

Crowd-footprinting mirror of NVI: uninformed participants dominate active (high-volume) days, so cumulating price change only on increased-volume days isolates the crowd-driven drift ("Positive Volume Index highlights days when volume is up on the previous day"). The 255-day EMA of that line is the year-scale bull/bear partition: below it the bear probability is 67%, above it the bear probability drops to 21% (79% bull-implied) — the asymmetry is the source's own finding, carried verbatim. Crossing below the one-year average confirms the approach of a bear market; crossing back above ends the bear signal.

### Research interpretation

Year-scale crowd-drift regime port: the increased-volume filter throws away every quiet bar (each contributes exactly zero) and the 255-day EMA low-passes what remains, so the derived system can only be long while crowd-driven advances persist at the year scale and sits flat through everything else — whipsaw bleed inside choppy regimes is structurally converted into flat time rather than stop-outs, because there is no stop to hit and no cross to chase mid-regime. Unlike every pool volume record (OBV/PVT/PVO/CMF/Chaikin/MFI), which read all-bar flow or intrabar placement, this rule is blind to quiet bars by construction; unlike the NVI sibling it is blind to the exact bars NVI reads — the two gauges partition the tape into disjoint subsets, so a vertical low-volume melt-up prints a flat PVI while NVI climbs, and a vertical high-volume blow-off prints the reverse. Unlike moving-average trend records it smooths a cumulative volume-filtered line rather than price itself. The bet, as derived, is purely on increased-volume drift persistence at the ~year scale, never on a level, band, oscillator zone, calendar date, or funding print.

## Signal

Exact rule as pinned (1000 seed / strict-increase gate / multiplicative update / EMA-255 / state-hold — any other value is a different, unpinned rule):

- Series (pinned): let `C_t`, `V_t` be the close and printed bar volume of completed `1d` bar `t` (`t = 1` is the first available bar). `PVI_1 = 1000` (declared convention — immaterial by scale-invariance below). For `t ≥ 2`: `PVI_t = PVI_{t-1} × (1 + (C_t − C_{t-1}) / C_{t-1})` if `V_t > V_{t-1}` (strictly), else `PVI_t = PVI_{t-1}` (volume decrease or equality contributes nothing — the page's " Otherwise, add zero"). Volume units are immaterial: only the strict inequality of consecutive venue prints is read, so base- versus quote-denominated feeds give identical events. Division is safe: crypto closes are strictly positive, and no other divisor exists.
- Seed scale-invariance (arithmetic fact, not a source claim): the update is linear in the seed, and the EMA below is linear in the series, so seed and EMA scale together and every cross event is seed-invariant. The 1000 seed is convention only.
- Regime line (declared arithmetic, pinned): `EMA_t` is the 255-period exponential moving average of the PVI series with `α = 2/(255+1)`, seeded with the simple mean of `PVI_1 … PVI_255`. `EMA_t` is undefined before `t = 255`; no decision may reference it there.
- Position target (pinned, strict): evaluated at the close of each completed `1d` bar `t ≥ 255`: `PVI_t > EMA_t` → long; `PVI_t ≤ EMA_t` → flat (equality pinned to flat — measure-zero on live tape, no tie semantics beyond this). The bear side of the source gauge is explicitly disabled, not underspecified.
- Orders (pinned): at most one order event per bar, placed for the next `1d` open after the decision bar: flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials, no second decision inside the fill bar for any reason including large adverse excursion. Entry and exit can never co-fire: the target is a single state per bar.
- Risk legs (pinned absence, not invented): the source ships no stop/target/trailing/time-exit concept anywhere — the sole position-closing path is the next regime bar mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no time exit; a year-scale adverse drift is ridden or sat out in full by construction.
- Direction: long-flat (derived pin). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` closes and printed bar volumes of BTCUSDT only: two scalars per bar (`C_t`, `V_t`). No `open` (except as fill price), no `high`, no `low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, breadth, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: completed daily bar. One evaluation per close; fills land on the next daily bar's open. All inputs are completed-bar prints — no provisional close or unfinished volume is ever used. Bar volume is final at bar close on the venue tape.
- Warmup: 255 completed `1d` bars before the first decision (the EMA seed window must exist in full). Bars 1–254 are flat by record rule; the first decidable close is bar 255 and its fill lands on bar 256's open. No signal before the seed window completes may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (bar membership is the venue's own daily grid — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; the page demonstrates single-name application on Procter & Gamble — no cross-venue equivalence claimed). The venue's daily volume print replaces the page's share-volume concept one for one — both are completed-bar venue totals, never modelled intraday.
- Order timing (declared port; the source is cadence-silent): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are regime-change market entry/close-all orders, and at most one order exists per bar — there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (the source ships no sizing). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-flat form holds genuine flat spells between a non-positive regime and the next positive one, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat spell needs only the next long-regime close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The page ships the full construction adopted here: the Fosback lineage, the crowd-on-active-days assumption, the strict-increase gate with the multiplicative percentage-change update and add-zero otherwise, the 255-day exponential default, the above/below bull/bear partition with the 67%/21% asymmetry, the cross-below-confirms-bear / cross-above-ends-bear execution semantics, and the single-name worked example. It ships zero adopted performance numbers for this record: the 67%/21% figures describe Fosback's equity-market odds, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Crowd-gauge reliability caveat, carried: PVI tracks the uninformed crowd by the source's own assumption, and Fosback's own stats rank it below NVI (79%/67% versus 96%/53%). This record is a deliberate single-asset port of the weaker sibling — it is never evidence that PVI times BTCUSDT well.
2. Smoothing alternative fenced: the page's own chart smooths with a 9-day fast EMA to "eliminate several whipsaws". That 9EMA-vs-255EMA cross reading is a different, unpinned rule — none is admitted here; this record pins the headline raw-PVI-vs-one-year-average rule to which the 67%/21% stats attach.
3. Whipsaw admission, carried: the smoothing note exists precisely because the raw gauge whipsaws. The derived system converts those episodes into flat churn and late re-entries, disclosed, not filtered.
4. Asymmetric-direction pin, fenced: the gauge is two-sided — long-flat is a researcher choice; the disabled 67%-bear leg is stronger than NVI's disabled 53% leg, so more gauge economics are discarded here than in the sibling record. Two-sided economics would differ by construction.
5. No hidden risk layer: the source ships no stop/target/trailing concept — the sole position-closing path is the next regime bar. The absence of any stop is source-faithful absence, disclosed, not a tunable parameter here.
6. Fully exposed inside the long regime: once long, the system rides the entire adverse excursion with no guardrail — a −50% drawdown inside an above-EMA regime is held to the last bar by construction. This is the coded trade, disclosed, not a tunable parameter here.
7. Seed-arithmetic boundary, fenced: the publisher pins no seed value — the 1000 seed is declared researcher convention, and cross events are provably seed-invariant under the multiplicative update. An additive percentage-point update (the sibling NVI arithmetic) would be a different, unpinned rule — none is admitted here.
8. Strict-gate boundary, pinned: volume equality adds zero via the strict "greater than yesterday" gate; a `≥`-gated variant would be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source behavior is the seven declared adaptations (long-only pin, single asset, state-hold evaluation, daily next-open grid, fixed sizing, warmup/seed convention, house costs); strict-increase gate, multiplicative update, EMA-255 length, and above/below semantics are source-faithful. This record is therefore never evidence that the source's equity-market timing passes anything.
10. The 1000-seed / strict-increase / multiplicative-update / EMA-255 / state-hold / single-position long-flat / signal-only-exit stance is pinned, not removed: shortening the signal length, adopting the 9-day fast smoothing, substituting a simple average, drawing PVI trendlines, adding a stop/target/filter/cooldown, re-enabling the short leg, trading intrabar, or sizing partially instead of 100% equity would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1000 seed / strict-increase gate / multiplicative update / EMA-255 / state-hold / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Smoothing-scale relevance: adopting the page's own 9-day fast-EMA smoothing (9EMA-vs-255EMA crosses, same closes) must not improve net expectancy; fail ⇒ the raw-line rule carries no advantage over the page's smoothed reading.
- F2 — Filter relevance: replacing the increased-volume-only update with an every-bar percentage-change cumulation (the discarded quiet-tape leg) must not improve net expectancy; fail ⇒ the volume gate does no work and the record is a slow trend-follower in disguise.
- F3 — Direction-pin relevance: enabling the symmetric short leg (bear-regime short instead of flat, cost-loaded) must not improve risk-adjusted expectancy; fail ⇒ the long-only pin discards the gauge's better-compensated half — or the short leg's funding load dominates.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` closes; close-plus-volume arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market prints volume on every daily bar (bar membership is the venue's own daily grid — deterministic on any continuously traded tape). Extension to other house-universe assets, other signal lengths, the 9EMA-smoothed reading, or a combined PVI+NVI record would each be a different, unpinned claim.

## Limitations

- Researcher direction pin: the gauge is two-sided — long-flat is a researcher choice; the disabled bear leg is the page's 67% half, stronger than the sibling record's discarded half. Two-sided economics would differ by construction.
- Single-asset port: the source's odds are broad-market timing (plus one single-name chart example); single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Crowd-tracking caveat: by the source's own assumption PVI follows uninformed flow, so the long regime can mark crowd tops as faithfully as crowd trends — disclosed as the record's principal economic risk.
- No price stop, no intra-regime exit: adverse excursion inside the long regime has no guardrail; the next decision is one bar away but the regime itself can persist for years. This is the source-faithful posture, disclosed as a principal risk.
- EMA lag: structural lag under a 255-day average is inherent — regime turns print months after price turns by construction.
- Unused cost silence: the source reports no cost accounting; derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Warmup cost: the first 254 bars are flat by record rule, so any textbook regime completing inside the seed window is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Incredible Charts (Colin Twiggs), Positive Volume Index (Fosback lineage, crowd-on-active-days assumption, strict-increase multiplicative formula, 255-day EMA default, cross-below-confirms-bear / cross-above-ends-bear semantics, 67%/21% asymmetry, single-name example; fetched full page 2026-10-17): https://www.incrediblecharts.com/indicators/positive_volume_index.php
