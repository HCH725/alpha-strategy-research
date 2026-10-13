---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Lunar-phase new-moon regime long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-13
sources:
  - https://www.bus.umich.edu/pdf/mitsui/workshopdocs/ZhengMoonstruck.pdf
  - https://doi.org/10.1016/j.jempfin.2005.06.001
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Lunar-phase new-moon regime long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (PDF fetched and verified live 2026-10-13, 49 pages, 278,579 bytes, SHA-256 `19474a13688124caa0eb2c6f4b117d430ce2f7342dc38ae0582708d9c84c4a2a`):

- Yuan, K., Zheng, L., Zhu, Q., `Are Investors Moonstruck? Lunar Phases and Stock Returns`, University of Michigan working draft (first draft August 2001; this draft September 2002): https://www.bus.umich.edu/pdf/mitsui/workshopdocs/ZhengMoonstruck.pdf.
- Published version (bibliographic): Yuan, Zheng & Zhu, "Are Investors Moonstruck? Lunar Phases and Stock Returns," *Journal of Empirical Finance* 13(1) (January 2006): 1–23. DOI: https://doi.org/10.1016/j.jempfin.2005.06.001 (bibliographic record verified via the ANU research portal entry for the same title/DOI).
- Pinned window definitions (verbatim in sense, §III.A eq. 1): "We define a full moon period as N days before the full moon day + the full moon day + N days after the full moon day (N = 3 or 7). Similarly, we define a new moon period as N days before the new moon day + the new moon day + N days after the new moon day (N = 3 or 7)." The Lunar-dummy regression is `Rt = α + β·Lunardummy + et` with the dummy taking one for a full moon period and zero otherwise (i.e. new moon period days are the zero leg).
- Pinned 15-day partition rule (verbatim in sense, §III.A fn. 10): "In the case of the 15-day window, a new moon period can be less than 15 days since a lunar month may be less than 30 days. In these cases, the new moon period is defined as the remaining days of the lunar month." The full moon period is therefore the fixed 15-day block (full moon day ±7) and the new moon period is every remaining day of the synodic month — the two legs tile the cycle with no gap day and no double-membership day.
- Pinned headline estimates (verbatim in sense, §III.A): "The mean daily return difference between the new moon period and the full moon period is 4.34 basis points for the 15-day window specification and 5.51 basis points for the 7-day window specification. The above numbers translate into annualized return difference of 5.4 percent and 6.9 percent respectively," both significant at the 5% level; the lunar-month return difference (Table II Panel B, 15-day) annualizes to −4.2%, significant at 5% (t-test) and 1% (Wilcoxon). The sinusoidal specification (§III.A eq. 2, cosine with 29.53-day period) gives β = −2.97, significant at the 1% level.
- Pinned data scope (§II, Table I): lunar calendar from the United States Naval Observatory (USNO) table of phase date/time in GMT for 1700–2015 (new/first-quarter/full/last-quarter; mean synodic month 29.53059 days for year 2000); returns are Datastream nominal local-currency daily index returns for 48 MSCI developed/emerging countries; every country sample ends July 31, 2001 (Table I).
- Pinned independence results (§VI, Tables X–XII): the lunar effect survives the January dummy, day-of-week, calendar-month, and holiday controls; survives lunar-holiday checks (including the Jewish-holiday check); and survives the random 30-day-cycle placebo — shifted 30-day cycles starting 11–20 days after the full moon reverse sign, and significance declines as the placebo deviates from the true lunar cycle (Figure 4). Volatility/volume tests (§IV, Table IX) show the spread is not a volatility or trading-volume artifact.
- Licence and rights: a public author-hosted working paper of a published journal article — this record cites and normalizes the rule (short phrases and the window/partition notation only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's 15-day full/new-moon partition ported to a single crypto asset on completed `1d` bars, long during new-moon-period days and flat during full-moon-period days — not a lossless reproduction of the paper's 48-country equity regression. Researcher-declared adaptations are exactly five: (1) the 15-day (N = 7) window is pinned and the 7-day (N = 3) window is fenced, never carried — see Signal; (2) single-asset BTCUSDT Binance perpetual (the 48-country Datastream universe and every equity-level performance claim are fenced off, never carried — see Negative evidence 1); (3) UTC-bar-date anchoring of the paper's GMT phase instants (the paper's own §II premise; phase instants are astronomical and known years in advance, so every bar's regime is known before the bar opens — see Signal); (4) fixed 100%-equity single-position sizing with no leverage (the paper ships no sizing rule — see Limitations); (5) an adopted 5-bar warmup flat by record rule plus house fees/funding treatment (the paper reports no costs — see Execution assumptions). The full/new partition, the long-new/flat-full posture (the paper documents a new-minus-full spread with cash-equivalent zero leg — never a short), the unconditional trigger (no anomaly, size, or volatility conditioning is traded), and the no-stop time-regime stance are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `lunar`, `moonstruck`, `full.moon`, `new.moon`, `ephemeris`, `usno`, `synodic` return zero strategy records (the sole `lunar` hit is the pre-holiday record's own dedup search-terms line, which searched for lunar and found nothing — confirming this is a new family). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in trigger class, and the paper itself proves the distinction: `january-barometer-conditional-annual-hold`, `santa-claus-rally-yearend-hold`, `sell-in-may-seasonal-hold`, `monday-drift-weekly-calendar-hold`, `pre-holiday-drift-scheduled-preclosure-hold`, `turn-of-month-4day-hold`, and `fomc-pre-announcement-drift-scheduled-hold` all use Gregorian-calendar or policy-event triggers, while §VI shows the lunar spread survives January, day-of-week, calendar-month, and holiday controls — i.e. the lunar cycle is orthogonal to every calendar trigger already in the pool. Five-axis distinction: no pool record and no open PR conditions exposure on the 29.53-day synodic phase partition (full moon day ±7 vs. remaining synodic days) from an astronomical ephemeris with no return, indicator, weekday, month, or event-calendar conditioning.

## Economic mechanism

### Source-reported

Mood-misattribution anticipation: psychological and biological literature associates full moon phases with depressed mood; by extension investors value stocks less during full moon periods, so returns accrue lower on full-moon-period days than new-moon-period days (§I). The paper stresses the test is deliberately hard to explain rationally — the lunar cycle has no tangible economic footprint — so any correlation is on its face a mood effect (§I). The spread is not compensation for volatility or volume (§IV), not a January/day-of-week/calendar-month/holiday artifact (§VI), not a lunar-holiday artifact (§VI), and not a generic 30-day-cycle artifact (§VI, Table XII/Figure 4). Country-by-country, all G-7 and all 16 other developed markets show negative full-moon coefficients under the 15-day window (5 significant at 10%, §III.B); emerging markets show larger spreads (7.09bp vs. 3.47bp for G-7, 15-day). Corroborating lineage (fenced, not carried): Dichev & Janes (2003) independently document lower full-moon-period returns, and the follow-up literature re-interprets the spread as enhanced-new-moon rather than depressed-full-moon — both readings agree on the new-minus-full spread this record trades.

### Research interpretation

Pure astronomical-regime drift-capture, long-only, with maximum time out of market on the full-moon leg. Unlike Gregorian calendar holds (ToM/Santa/Monday/January/pre-holiday/FOMC) the trigger is a celestial partition that drifts against every civil calendar (~29.53 days, never aligned to weekdays, months, or policy schedules), so exposure windows precess through all weekdays and seasons — and the paper's §VI is exactly the proof that this trigger is not a relabeling of any of them. Unlike return-conditioned monthly systems (TSMOM) there is no formation leg and no losing-signal concept: the position exists if and only if the ephemeris says the day is a new-moon-period day. Unlike indicator-anchored systems the bet is purely that the documented new-minus-full spread ports to BTCUSDT daily bars, never on a level, band, oscillator, volume, return-sign, or funding anchor. The strategy is deliberately invariant to the depressed-full vs. enhanced-new interpretation dispute: both agree new-moon days out-earn full-moon days, and long-new/flat-full harvests exactly that spread without picking a side. The causality is airtight by construction: phase instants are deterministic astronomy known years before any bar opens.

## Signal

Exact rule as pinned (15-day N = 7 partition; F = UTC calendar date of a full-moon GMT instant; a bar's regime is a pure function of its UTC date plus the ex-ante-known ephemeris — any other window is a different, unpinned rule):

- Partition (pinned, §III.A + fn. 10): full-moon-period days are the 15 UTC dates F−7 … F+7. New-moon-period days are all remaining UTC dates of that synodic month (from F+8 up to the day before the next full-moon period starts; length varies with the true lunation, typically 14–15 days). Every UTC date belongs to exactly one leg — no gap day, no double-membership day, by the paper's own footnote construction.
- Ephemeris convention (pinned, §II): phase instants are GMT dates/times from the USNO-anchored lunar table (mean synodic month 29.53059 days). The record pins UTC bar dates against the UTC calendar date of each GMT instant — deterministic, no session template, no holiday-shift rule (the 24/7 tape has no holidays; the paper's equity-market holiday checks are fenced as specificity evidence only).
- Entry long (pinned timing, close-based): at the close of a completed `1d` bar D dated in the full-moon period whose next calendar day D+1 is a new-moon-period day (i.e. the eve of each new-moon leg — always the F+7 bar), if flat (always true outside new-moon legs by construction), buy 100% equity at that close (same-bar-close fill). Entry predicate from the bar's own date plus tomorrow's ephemeris date alone — both known before the bar opens.
- Exit (pinned timing, close-based): at the close of a completed `1d` bar D dated in the new-moon period whose next calendar day D+1 is a full-moon-period day (i.e. the last new-moon day of each leg), close the full position at that close. Exit predicate: a position is open and tomorrow begins a full-moon period. Because entries happen only on F+7 bars and exits only on the last new-moon day of each lunation, an open position on an exit bar is always the matching leg position — no pairing ambiguity, disclosed, not missing.
- Separation guarantee (pinned, structural): the entry bar (F+7) and the exit bar (last new-moon day) are always distinct bars at least 13 sessions apart, so no bar ever carries both an entry and an exit — no same-bar dual-fire exists to sequence. Lunations never overlap, so overlapping legs are structurally impossible.
- Risk legs (pinned posture): no stop, no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing path is the end-of-new-moon-leg close. The absence of any stop is the source's posture (the paper ships a time-regime only), disclosed, not invented.
- Direction: long-only (derived pin matching the source, which documents a new-minus-full spread against a zero/cash leg — never a short leg). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical regime set.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (fills) and bar UTC calendar date (regime predicates). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or market-data-feed dependency of any kind.
- One external calendar input, point-in-time clean by construction: full/new moon GMT instants from the USNO-anchored lunar table (§II premise; deterministic celestial mechanics predictable years ahead — no release lag, no revision, no publication embargo). No quarter-phase, eclipse, supermoon, volatility, volume, or calendar-anomaly input enters any rule.
- Single decision grid: completed daily bar, one evaluation per bar. The entry fills on the F+7 bar's own close; the exit lands on the last new-moon day's own close. All inputs are completed-bar values plus the ex-ante-known ephemeris — no provisional intrabar value, no future reference, no outcome of any kind is ever used.
- Warmup: 5 completed `1d` bars flat by record rule (regime predicates need only the bar's own UTC date plus the pre-published ephemeris, so the guard is conventional, not structural — mirrors the standing small-guard record-rule precedent). No repainting, no negative shift, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's 48-country equity universe; no cross-asset equivalence claimed).
- Order timing (declared port of the paper's hold-the-new-moon-leg construction): completed-bar decision with same-bar-close fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are one market entry per lunation and one close-all per leg — at most one order exists on any bar, so there is no same-bar dual-fire whose ordering could change economics. The paper's 7-day (N = 3) window is deliberately not modelled (fenced — see Negative evidence 5).
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (the paper ships no sizing rule). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-only form is flat through every ~15-day full-moon leg, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; lunation legs are disjoint by ephemeris construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any leg exit the next F+7 entry fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships the full construction adopted here: the USNO-anchored GMT phase table with the 29.53059-day synodic month (§II), the N = 7 fifteen-day full/new partition with the remainder-days new-moon rule (§III.A + fn. 10), the full-vs-new dummy regression (eq. 1), the long-the-spread posture implicit in the new-minus-full headline (4.34bp/day, 5.4% annualized, 5% significance; lunar-month −4.2% annualized, Table II Panel B), the unconditional trigger (no conditioning variable is ever traded), and the equity-only statistics — 5.51bp/6.9% for the 7-day window, sinusoidal β = −2.97 at 1%, all-G-7-negative country coefficients, larger emerging-market spreads, no volatility/volume explanation (§IV), independence from four calendar anomalies plus lunar holidays plus placebo 30-day cycles (§VI). It ships zero adopted performance numbers for this record: every basis-point, annualized-percent, and significance figure above describes Datastream equity indices through July 2001, never a BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every basis-point, annualized-percent, hit-pattern, and significance figure (4.34bp; 5.4%; 5.51bp/6.9%; −4.2%; β = −2.97; country tables) belongs to pre-August-2001 Datastream country indices — none transfers to BTCUSDT crypto, whose 24/7 microstructure (no open/close, funding prints inside legs, weekend-adjacent boundaries) differs arbitrarily, and none is adopted.
2. Sample-end fence: every country series ends July 31, 2001 (Table I); no post-2001 persistence, decay, or regime claim of any kind is carried — this record adds no out-of-sample guard and claims no persistence.
3. Crypto-lunar anecdote fenced: entertainment overlays (explicitly "not a trading signal"), forum full-moon-bullish anecdotes (contradicting the paper's full-moon-bearish direction), and a review paper reporting mixed backtests with "no robust causal mechanism" are all carried only as proof that no serious crypto-native lunar rule exists to pin — none is adopted, and the contradictory anecdotal direction is never traded.
4. Interpretation dispute adopted as robustness, never as a rule: whether the spread is depressed-full-moon or enhanced-new-moon (follow-up literature) changes nothing here — long-new/flat-full harvests the agreed spread either way, and no leg-attribution claim is made.
5. Seven-day (N = 3) window fenced: the paper's stronger 5.51bp/6.9% construction covers only ±3 days around each phase, leaving unassigned gap days whose treatment the paper never specifies; this record carries only the gapless 15-day partition (4.34bp/5.4%) — the 7-day edge is never claimed for the daily port.
6. Conditioning and placebo evidence fenced as specificity, never as rules: January/day-of-week/calendar-month/holiday dummies, lunar-holiday checks, volatility/volume regressions, and the 30-day-cycle placebo shifts are carried only to show the trigger is lunar-specific, not a generic cycle or calendar hold.
7. Cost silence fenced: the paper reports no transaction costs — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
8. Fully exposed inside the leg: once entered, the position rides the entire adverse excursion with no guardrail — a −20% new-moon-leg crash is held to the leg-end close by construction. This is the coded trade, disclosed, not a tunable parameter here.
9. Derivation boundary fenced: the only non-paper behavior is the five declared adaptations (15-day window pin, single asset, UTC ephemeris anchoring, fixed sizing, warmup + house costs); the full/new partition, the unconditional trigger, the long-new/flat-full posture, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity finding passes.
10. The F±7 partition / F+7-close entry / last-new-day-close exit / unconditional-trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close stance is pinned, not removed: switching to the 7-day window, trading quarter-phase/eclipse/supermoon overlays, conditioning on January/weekday/volatility, adding a stop/target/cooldown, re-enabling a short leg, trading partial size, or holding through full-moon legs would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: F±7 partition / F+7-close entry / last-new-day-close exit / unconditional trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Window-length relevance: replacing the pinned 15-day partition with the paper's own 7-day (N = 3) windows (holding only ±3-day new-moon cores, flat otherwise) must not improve net expectancy; fail ⇒ the gapless-partition pin is doing unacknowledged work and the paper's stronger narrow-window finding does not survive the port.
- F2 — Entry-timing relevance: replacing the pinned F+7-close entry with a first-new-day-close entry (skipping the eve session and capturing only the remaining new-moon days) must not improve net expectancy; fail ⇒ the boundary session adds nothing over the interior-leg hold.
- F3 — Selectivity relevance: replacing the pinned regime exposure with buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out the ~15-day full-moon legs costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; UTC-date predicates plus close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical regime set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no holidays for the rule to skip; GMT phase instants map onto UTC bar dates deterministically (every calendar day is a trading day). Extension to other house-universe assets, windows, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is 48-country-equity-only through July 2001; BTCUSDT new/full-moon behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Microstructure mismatch: the paper's days are equity close-to-close sessions with overnight halts; the 24/7 crypto tape has no halt, no open/close, and perverse adjacencies (funding prints inside legs, weekend boundary bars) — the port bets on spread persistence, not on a verified crypto mechanism.
- Boundary-date convention: the paper anchors on GMT instant dates; the record pins UTC bar dates of the same instants (identical except for sub-day GMT/UTC alignment, immaterial at daily bars) — disclosed, not recovered.
- Sample thinness: roughly 12 lunations per year means a decade of crypto history yields only ~12 full regime cycles per year of exposure halves — statistical power is structurally weak, disclosed, not recovered.
- Close-confirmation lag: the entry fills at the F+7 close and the exit at the last-new-day close — gap-through moves across leg edges are taken at post-move closes, never at the edge.
- Leg rigidity: drift arriving during full-moon legs is missed by record rule, and a leg whose spread fails per the source's own negative lunations is held/flat anyway — disclosed, not recovered.
- Warmup cost: the first 5 daily bars are flat by record rule — pinned, not recovered (immaterial at ~29.5-day legs, disclosed for completeness).
- Ephemeris extension: the paper's USNO table as cited covers 1700–2015; post-2015 phase instants come from the same deterministic astronomical series (phases are computable, not forecasted). Direct USNO site paths were unreachable from this host at write time, so no live USNO URL is claimed — the input is the paper's USNO-anchored table extended by deterministic astronomy, disclosed, not link-dressed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Yuan, K., Zheng, L., Zhu, Q., *Are Investors Moonstruck? Lunar Phases and Stock Returns*, University of Michigan working draft (first draft August 2001; this draft September 2002) — USNO GMT phase table with 29.53059-day synodic month (§II), N = 3/7 full/new window definitions with eq. 1 dummy regression (§III.A), remainder-days new-moon partition rule (fn. 10), headline 4.34bp/5.4% 15-day and 5.51bp/6.9% 7-day spreads at 5% significance plus −4.2% lunar-month spread (Table II), sinusoidal β = −2.97 at 1% (eq. 2), country-by-country results (§III.B), volatility/volume non-explanation (§IV/Table IX), calendar-anomaly/lunar-holiday/placebo-cycle independence (§VI/Tables X–XII, Figure 4), 48-country sample ending July 31, 2001 (Table I); PDF verified live 2026-10-13 (49 pages, 278,579 bytes, SHA-256 `19474a13…8d9c84c4a2a`): https://www.bus.umich.edu/pdf/mitsui/workshopdocs/ZhengMoonstruck.pdf
- Published-version lineage: *Journal of Empirical Finance* 13(1), January 2006, 1–23; DOI: https://doi.org/10.1016/j.jempfin.2005.06.001
- Corroborating lineage (fenced, not carried): Dichev, I. D., Janes, T. D. (2003), lunar-effect corroboration; follow-up international-evidence paper re-interpreting the spread as enhanced-new-moon (bibliographic via ScienceDirect record for the Yuan et al. follow-up)
- Crypto-anecdote fence (none adopted): public entertainment moon-phase/BTC overlay (self-declared not-a-signal), forum full-moon anecdotes, and a mixed-evidence review paper reporting no robust causal mechanism
