---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Force Index 100 zero-state trend two-sided on BTCUSDT 1d bars
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
  - https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/force-index
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Force Index 100 zero-state trend two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (StockCharts ChartSchool page fetched in full during this cycle, 2026-10-12; the page advertises a Markdown edition for agent consumption at the same path plus `.md`, and both the HTML and publisher `.md` twin were retrieved — the `.md` fetch is the publisher's own machine-readable form, not a scrape artifact):

- StockCharts ChartSchool, `Force Index` — canonical URL: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/force-index (Markdown twin at the same path plus `.md`). Lineage stated on-page: developed by Alexander Elder, introduced in his classic book *Trading for a Living*. The page's three-elements doctrine is quoted in sense: direction, extent, and volume combine into one oscillator that fluctuates in positive and negative territory as the balance of power shifts.
- Pinned computation (§Calculating the Force Index, verbatim in sense): `Force Index(1) = {Close (current period) − Close (prior period)} × Volume`; `Force Index(13) = 13-period EMA of Force Index(1)`. The multi-period form is pinned as an exponential moving average of the 1-period values with no alternate smoothing: "a 13-period Force Index is a 13-period EMA of the 1-period Force Index values for the last 13 periods." The three value factors are pinned: sign follows the close-vs-prior-close direction, extent scales with the size of the move, and volume multiplies commitment ("A big move on big volume produces high Force Index values").
- Pinned trend semantics (§Trend Identification and §The Bottom Line, verbatim in sense): "the 100-day Force Index can be used to determine the medium- or long-term trend"; "The bulls have the edge when the 100-day Force Index is positive. The bears have the edge when the 100-day Force Index is negative." The 13-day form is fenced by the page itself as short-term and jagged ("captures short-term fluctuations and is more sensitive"), while the 100-day form "crosses the zero line fewer times" — the length choice here follows the page's own trend-determination recommendation, never a researcher optimisation.
- State-hold pin (§Suggested Scans): the publisher's own scans hold the regime as a level, not a cross — `Daily FORCE(100) > 0` establishes the uptrend side, `Daily FORCE(100) < 0` the downtrend side — confirming positions turn on and persist with the zero-state, event-identical to the state rule below. The volume-data note is carried: "daily volume data is incomplete during the trading day. When running scans with volume-based indicators like the Force Index, base the scan on the 'Last Market Close'" — this record therefore evaluates completed bars only.
- Fenced on purpose: the divergence section (requires subjective swing identification plus page-mandated external confirmation), the 22-day-EMA/2-day-Force-Index correction system (explicitly discretionary — "two schools of thought" on when to act — and labelled "aggressive ... best suited for active traders"), and the CCI-gated scan legs (a second indicator with its own thresholds). None is adopted; the record is the zero-state trend leg only.
- Licence and rights: this record cites and normalizes the rule (short phrases and formulas only) and reproduces no chart, table, figure, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — Elder/ChartSchool's 100-period Force Index zero-state trend gauge ported to one crypto asset as a two-sided daily system — not a lossless reproduction of Elder's discretionary stock practice. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance tape (the page is equity-charted; crypto portability is a researcher carry, disclosed — the page's own scan universe is US stocks, never crypto); (2) state-hold evaluation each completed close with orders only on target change (event-identical to the publisher's `FORCE(100) > 0 / < 0` scan-level semantics, pinned to remove any cross-vs-hold ambiguity); (3) next-open market fills on the `1d` grid (the source is cadence-silent beyond "Last Market Close"; daily closes are the declared port); (4) fixed 100%-equity single position at 1× with no leverage (the source ships no sizing); (5) no stop, no target, no trailing, no time exit (the source ships no risk leg for the zero-state trend use anywhere — exits are regime-driven only, source-faithful absence); (6) a declared EMA-seed/warmup convention (the publisher pins EMA smoothing but no seeding arithmetic, so the arithmetic is disclosed researcher specification, never presented as a source fact). The Force(1) formula, the EMA-only smoothing form, the 100 length, and the positive-bulls/negative-bears edge semantics are source-faithful.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `force.index`, `force(100)`, `force(13)`, `elder`, and `balance of power` return zero strategy records computing this indicator — the sole `force index` hits pool-wide are the elder-impulse record's own dedup paragraph (which records that `\bforce index\b` returned zero hits) and this sentence. That record trades EMA-slope-plus-MACD-histogram impulse states, never a volume-multiplied price-change EMA. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md` cumulates signed volume with no price-extent factor (a flat drift on equal closes still moves OBV; it never moves Force); `pvt-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-11.md` cumulates volume-scaled returns (division by price, every bar counts including unchanged-volume bars); `cmf-velocity-zero-cross-ema200-bracket-two-sided-btcusdt-1d-2026-10-10.md` and `chaikin-oscillator-ad-zero-cross-momentum-divergence-two-sided-btcusdt-4h-2026-10-12.md` read intrabar close-location placement, never close-to-close change; `elder-ray-123reversal-combo-two-sided-btcusdt-1h-2026-10-09.md` reads High-EMA/Low-EMA Bull/Bear Power, a range-vs-average construction with no volume factor at all. Five-axis distinction: no pool record and no open PR trades the sign-state of an EMA of close-change-times-volume.

## Economic mechanism

### Source-reported

Commitment-weighted pressure: Elder's three elements — direction (who won the close), extent (by how far), and volume (how committed the winners were) — multiply into one number per bar, and the 100-period EMA low-passes those prints into a medium/long-term balance-of-power gauge. Positive Territory means buyers committed harder over the window; negative means sellers did. The page's own trend doctrine is symmetric: bulls have the edge above zero, bears below — there is no long-only fence anywhere in the trend sections.

### Research interpretation

Slow commitment-regime port: the 100-bar EMA of change-times-volume can only flip on sustained, committed drift — a single high-volume spike against the regime barely dents a 100-period average, while weeks of grinding signed pressure accumulate into a flip. Unlike OBV/PVT (unbounded every-bar cumulations with no decay — ancient history never fades), the EMA forgets exponentially, so the derived system is a recency-weighted pressure regime, not a lifetime ledger. Unlike moving-average trend records it smooths a volume-weighted change series rather than price itself, so a low-volume melt-up and a high-volume grind print opposite Force readings for similar price paths. The bet, as derived, is purely on the persistence of commitment-weighted drift at the ~quarter scale, never on a level, band, oscillator zone, calendar date, or funding print.

## Signal

Exact rule as pinned (Force(1) product form / EMA-only smoothing / length 100 / zero-state hold — any other value is a different, unpinned rule):

- Series (pinned): let `C_t` be the close and `V_t` the venue-native base-asset printed volume of completed `1d` bar `t` (`t = 1` is the first available bar). `F_t = (C_t − C_{t-1}) × V_t` for `t ≥ 2`. No division exists anywhere in this construction, so no divide-by-zero path exists; crypto closes are strictly positive regardless.
- Regime line (length pinned, arithmetic declared): `FI_t` is the 100-period exponential moving average of `F` with `α = 2/(100+1)`, seeded with the simple mean of `F_2 … F_101`. `FI_t` is undefined before `t = 101`; no decision may reference it there. Volume denomination is pinned to the venue's native base-asset print so the series is exactly reproducible; only the zero-state is traded.
- Position target (pinned, strict): evaluated at the close of each completed `1d` bar `t ≥ 101`: `FI_t > 0` → long; `FI_t < 0` → short; `FI_t == 0` → flat (measure-zero on live tape, pinned for determinism — no tie semantics beyond this). Both directions are source-faithful; no leg is disabled.
- Orders (pinned): at most one order event per bar, placed for the next `1d` open after the decision bar: target long buys/holds 100% equity long; target short sells/holds 100% equity short; target flat closes all. A target change closes the old side and opens the new side at the same next open. Unchanged target places nothing. No intrabar evaluation, no intrabar orders, no adds, no partials, no second decision inside the fill bar for any reason including large adverse excursion. Entry and exit can never co-fire beyond the single atomic flip: the target is one state per bar.
- Risk legs (pinned absence, not invented): the source ships no stop/target/trailing/time-exit concept for the zero-state trend use anywhere — the sole position-changing path is the next regime bar mapping to a different target. The derived posture is explicitly no stop, no target, no trailing, no time exit; a quarter-scale adverse drift is ridden in full by construction.
- Direction: two-sided long/short with a measure-zero flat tie-state (derived pin matching the page's symmetric bulls/bears edge doctrine). The research market is the Binance perpetual under the house overlay with both permissions genuinely used.

## Required data

- Completed `1d` closes and venue-native base-asset printed bar volumes of BTCUSDT only: two scalars per bar (`C_t`, `V_t`). No `open` (except as fill price), no `high`, no `low`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, breadth, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind. The divergence swings, the 22-day EMA trend filter, and the CCI scan legs are fenced — none is computed.
- Single decision grid: completed daily bar. One evaluation per close; fills land on the next daily bar's open. All inputs are completed-bar prints — no provisional close or unfinished volume is ever used, per the page's own "Last Market Close" volume note. Bar volume is final at bar close on the venue tape.
- Warmup: 101 completed `1d` bars before the first decision (100 one-period Force values must exist to form the EMA seed). Bars 1–101 are flat by record rule; the first decidable close is bar 101 and its fill lands on bar 102's open. No signal before the seed window completes may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (bar membership is the venue's own daily grid — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared single-asset port; no cross-venue equivalence claimed). The venue's daily base-volume print replaces the page's share-volume concept one for one — both are completed-bar venue totals, never modelled intraday.
- Order timing (declared port; the source is cadence-silent beyond completed-bar evaluation): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are regime-change market entries/flips/close-all orders, and at most one order exists per bar — there is no same-bar dual-fire to sequence.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept beyond the venue's own short permission), no compounding concept beyond equity — declared derivative (the source ships no sizing). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the short leg accrues genuine funding economics and neither leg is modelled funding-free). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position (long or short) at any time; a flip needs only the next opposite-regime close (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The page ships the full construction adopted here: the Force(1) product formula, the EMA-only multi-period form, the default-13 vs trend-100 length doctrine with the 100-day medium/long-term trend recommendation, the positive-bulls/negative-bears edge partition, the scan-level state-hold semantics (`FORCE(100) > 0 / < 0`), and the completed-bar volume note. It ships zero adopted performance numbers for this record: the PFE/Home Depot/BB/TXN charts are illustration, never a return claim — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-charted gauge, fenced: every worked example is a US stock (PFE table, Home Depot, Best Buy, Texas Instruments) and the scans filter `[type = stock] AND [country = US]`. The single-asset crypto port is a researcher carry justified only by arithmetic portability (closes and volumes print on any tape), never by source evidence — this record is never evidence that Force times BTCUSDT well.
2. Whipsaw admission, carried: the page concedes the 13-day form is "more volatile and jagged" with frequent zero-line crossings; the 100-day form crosses "fewer times" but still whipsaws around zero in directionless tape ("If the index whipsaws around zero it signals that neither side has control" per the secondary literature the page's doctrine is consistent with). The derived system converts those episodes into flip churn, disclosed, not filtered.
3. Standalone-use caveat, carried: "As with all indicators, traders should use the Force Index in conjunction with other indicators and analysis techniques." This record is a standalone specification for admission purposes, never a recommendation.
4. No hidden risk layer: the source ships no stop/target/trailing concept for the trend use — the sole position-changing path is the next regime bar. The absence of any stop is source-faithful absence, disclosed, not a tunable parameter here.
5. Fully exposed inside the regime: once positioned, the system rides the entire adverse excursion with no guardrail — a −50% move inside a still-positive FI(100) is held to the last bar by construction. This is the coded trade, disclosed, not a tunable parameter here.
6. Seed-arithmetic boundary, fenced: the publisher pins EMA smoothing but no seeding arithmetic — the SMA-of-first-100 seed is declared researcher specification. Alternative seedings (first-value seed, Wilder smoothing, SMA-100 signal instead of EMA-100) would be different, unpinned rules; early-regime history shifts slightly under reseeding while the Force(1) path itself is seed-exact.
7. Length boundary fenced: the 13-day (short-term), 39-day (medium illustration), 2-day (correction timing), and 22-day EMA (correction trend filter) forms are all real page content and each would be a different, unpinned rule — none is admitted here. Only the 100-day trend form is specified.
8. Derivation boundary fenced: the only non-source behavior is the six declared adaptations (single asset, state-hold evaluation, daily next-open grid, fixed sizing, warmup/seed convention, house costs); product formula, EMA-only smoothing, length 100, and positive/negative edge semantics are source-faithful. This record is therefore never evidence that Elder's discretionary stock practice passes anything.
9. The Force(1) product / EMA-100 / zero-state / single-position two-sided / signal-only-exit stance is pinned, not removed: adding the CCI pullback legs, the divergence confirmation, a stop/target/filter/cooldown, trading intrabar, disabling the short leg, or sizing partially instead of 100% equity would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: Force(1) product / EMA-100 / zero-state hold / next-open fills / single-position two-sided / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Length relevance: replacing the pinned EMA-100 with EMA-13 (the page's own short-term form) must not improve net expectancy; fail ⇒ the quarter-scale partition carries no advantage over the sensitive form and the record is noise-trading in disguise.
- F2 — Volume-factor relevance: replacing the change-times-volume product with a pure close-change EMA-100 (the volume factor deleted) must not improve net expectancy; fail ⇒ Elder's volume-commitment element does no work and the record is a slow momentum follower in disguise.
- F3 — Symmetry relevance: disabling the short leg (bear-regime flat instead of short, cost-loaded comparison) must not improve risk-adjusted expectancy; fail ⇒ the two-sided pin carries dead weight — or the short leg's funding load dominates.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` closes; close-plus-base-volume arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change provided the same base-volume denomination is pinned. Funding accrues genuinely on the short leg under the house overlay (no zero-funding claim); no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market prints volume on every daily bar (bar membership is the venue's own daily grid — deterministic on any continuously traded tape). Extension to other house-universe assets, other smoothing lengths, the divergence/correction systems, or the CCI scan legs would each be a different, unpinned claim.

## Limitations

- Single-asset port: the source's evidence is equity-charted illustration; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- No price stop, no intra-regime exit: adverse excursion inside the regime has no guardrail; the next decision is one bar away but the regime itself can persist for months. This is the source-faithful posture, disclosed as the record's principal risk.
- EMA lag: a 100-period average turns quarters after price turns by construction — entries and flips print late by design.
- Zero-region churn: a flat market oscillating around FI = 0 produces repeated flips with no trend to capture; disclosed, not filtered.
- Standalone-use caveat: the publisher advises conjunction with other analysis; this record is standalone for admission purposes, never a recommendation.
- Unused cost silence: the source reports no cost accounting; derived evaluation must carry the full house cost load including short-leg funding, and this record reports no net performance of any kind.
- Warmup cost: the first 101 bars are flat by record rule, so any textbook regime completing inside the seed window is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- StockCharts ChartSchool, Force Index (Elder lineage, Force(1) product formula, EMA smoothing doctrine, 100-day trend-determination rule with positive-bulls/negative-bears partition, scan-level state semantics, completed-bar volume note; fetched full HTML plus publisher `.md` twin 2026-10-12): https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/force-index
