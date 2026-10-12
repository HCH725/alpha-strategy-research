---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: January Barometer conditional annual hold long on BTCUSDT 1d bars
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
  - https://www.stocktradersalmanac.com/Alert/20220106.aspx
  - https://en.wikipedia.org/wiki/January_barometer
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# January Barometer conditional annual hold long on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (both fetched and verified live 2026-10-12):

- Stock Trader's Almanac (official creator site), Jeffrey A. Hirsch & Christopher Mistal, `Yale Hirsch's Incredible January Barometer: Only 13 Major Errors in 84 Years`, 2022-01-06: https://www.stocktradersalmanac.com/Alert/20220106.aspx — pinned rule definition (verbatim in sense): "This indicator adheres to propensity that as the S&P 500 goes in January, so goes the year." Trigger construction: "it is the whole-month gain or loss of the S&P 500 that triggers our January Barometer." Origin lineage: "Devised by Yale Hirsch in 1972." Track record as printed: "the January Barometer (JB) has registered 12 major errors since 1950 for an 83.3% accuracy ratio", with "Including the eight flat years yields a .722 batting average." Timing colour: "every February or sooner if January starts off poorly our January Barometer gets raked over the coals" — adopted only as confirmation that February is the action month, never as a rule. Mechanism colour only: the Twentieth ("Lame Duck") Amendment / new-Congress / State-of-the-Union January cluster — never a rule input.
- Wikipedia, `January barometer` (page last edited 2026-05-02, fetched 2026-10-12): https://en.wikipedia.org/wiki/January_barometer — pinned corroboration (verbatim in sense): 'The January barometer ("As goes January, so goes the year") is the hypothesis that stock market performance in January (particularly in the U.S.) predicts its performance for the rest of the year.' Origin lineage: "The January barometer was first mentioned by Yale Hirsch in 1972." Regime-split statistics as printed: "From 1950 till 1984 both positive and negative prediction had a certainty of about 70% for positive outcomes and 90% for negative ones respectively with 75% in total. Between 1985 and 2010, however, the negative predictive power had been reduced to 50%, or in other words, no predictive power at all." Adopted as caution, never as rules.
- Licence and rights: public summary/reference pages — this record cites and normalizes the rule (short phrases and the January-sign notation only) and reproduces no figures, code, backtest tables, or extended prose. A second official-site page (Almanac knowledge article on the January Barometer) returned only a login gate on fetch and ships zero pinned literals here — disclosed, not silently used.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the Almanac's January-sign forecast ported to a single crypto asset as a long-only conditional annual hold — not a lossless reproduction of the Almanac's S&P 500 equity finding. The source ships a directional forecast for both signs (up-January predicts an up year, down-January predicts a down year) but ships no order, no sizing, and no short-side mechanics. Researcher-declared adaptations are exactly five: (1) calendar-month mapping onto the 24/7 tape (the crypto market has no trading-day calendar, so January/February/December membership is the UTC calendar date of each completed `1d` bar — principled port, not a choice among calendars; see Signal); (2) long-or-flat posture (up-January years hold long February–December; down-or-flat January years stay flat all year — the down-January forecast is fenced as source-reported prediction, never traded as a short leg, because neither source specifies short mechanics; see Negative evidence 2); (3) single-asset BTCUSDT Binance perpetual (the S&P 500 universe and every equity-level accuracy figure are fenced off, never carried); (4) fixed 100%-equity single-position sizing with no leverage (neither source ships a sizing rule); (5) next-open February entry plus adopted 35-bar warmup flat plus house fees/funding treatment (neither source reports costs or fill convention — see Execution assumptions). The whole-month January gain/loss trigger, the February action timing, the hold-through-December exit, and the no-stop stance are source-faithful.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `january`, `barometer`, `as january goes`, `as goes january`, `first-five`, `first five`, `early warning`, `febru` return zero strategy records — a new family in this pool. `hirsch` matches only `santa-claus-rally-yearend-hold-long-btcusdt-1d-2026-10-12.md`, which cites Hirsch for the December/January 7-session SCR window — a different mechanism, window, and trigger (see below). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md` holds an unconditional six-month seasonal span; `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md` holds a 4-session window at every month boundary (twelve windows per year, unconditional); `santa-claus-rally-yearend-hold-long-btcusdt-1d-2026-10-12.md` holds the single unconditional 7-session year-end window; `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds a full calendar month conditioned on the trailing 12-month return sign (monthly re-evaluation); `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` holds a weekly Monday session. Five-axis distinction: no pool record and no open PR conditions a single annual February–December hold on the sign of January's own whole-month return — one evaluation per year, return-conditioned, eleven-month maximum exposure.

## Economic mechanism

### Source-reported

January information-cluster thesis: the Almanac page attributes January's prognostic power to the month's concentration of regime-setting events (new Congresses convene, State of the Union, annual budgets, cash inflows, portfolio adjustments, strategist positioning) rooted in the 1933 Twentieth Amendment calendar — "Switch these events to any other month and chances are the January Barometer would become a memory." The page concedes the error cluster honestly: of the 12 major errors, nine occurred since 2001 (2001 rate cuts/9/11, 2003 Iraq anticipation, 2009 bear-market end, 2010/2014 Fed intervention, 2016 bear-market slide, 2018 Q4 collapse, 2020–2021 Covid) — adopted as regime caution, never as filters. Wikipedia adds the negative-side decay (1985–2010 negative predictions no better than a coin flip) — adopted as the reason the short side is never traded here. The First Five Days "Early Warning" system and the Santa Claus Rally result are named on the page as companion January signals and fenced — neither is a rule here.

### Research interpretation

Conditional annual drift-capture with maximum time out of market, long-or-flat, at most one evaluation and one window per year. Unlike unconditional seasonal holds (Sell-in-May exposes six months every year regardless of January) the exposure is gated: flat-January and down-January years sit out entirely, so the strategy can be flat for a full calendar year by rule. Unlike monthly return-conditioned systems (TSMOM re-evaluates twelve times per year on a 12-month formation leg) there is exactly one formation leg per year — January itself — and the hold spans up to eleven months, a structurally different clock. Unlike the 7-session Santa window (unconditional, ~2% of time) this is the year's slow leg: up to ~92% of a year exposed in a long year. Unlike weekly calendar holds the trigger is the year's first month, not a weekday. The bet, as derived, is purely that January's sign ports to BTCUSDT calendar months as an annual long/flat gate, never on a level, band, oscillator, volume, or funding anchor.

## Signal

Exact rule as pinned (January whole-month sign gates one February–December window per year; entry at the February open after the sign resolves; exit at the December close — any other month, sign convention, or fill is a different, unpinned rule):

- Calendar convention (pinned): bar dates are UTC calendar dates of completed `1d` bars. Because the venue trades 24/7 with no holidays, month membership is the bar's own UTC calendar month with no trading-day-shift rule needed — disclosed derivation, no hidden calendar table. January = all bars dated January 1–31; February 1 is always the day after January 31; December 31 always exists (leap years change nothing — February membership is by date, never by day-count).
- Formation leg (pinned): `R_Jan(year Y)` = sign of (close of the completed `1d` bar dated January 31 of Y minus close of the completed `1d` bar dated December 31 of Y−1). Whole-month gain/loss exactly as the source's trigger ("the whole-month gain or loss ... triggers"). Strictly positive ⇒ long year; zero or negative ⇒ flat year (pinned tie rule: a flat January is a non-signal, matching the source's own "flat years" batting-average treatment — disclosed, not invented; there is no third state).
- Entry long (pinned timing, next-open): at the open of the completed `1d` bar dated February 1 of Y, if `R_Jan(Y) > 0` and flat, buy 100% equity at that open. Entry predicate resolves causally: the January sign is fully known at the January-31 close, one bar before the fill — no same-bar signal/fill ambiguity exists by construction.
- Exit (pinned timing, close-based): at the close of the completed `1d` bar dated December 31 of Y, if a position is open, close the full position at that close. Exit predicate: a position is open and today is December 31. Because entries happen only on February-1 bars and at most one window exists per year, an open position on a December-31 close is always the matching year's position — no pairing ambiguity, disclosed, not missing.
- Separation guarantee (pinned, structural): the entry bar (Feb 1) and the exit bar (Dec 31) are always distinct bars with the February–December span between them, so no bar ever carries both an entry and an exit — no same-bar dual-fire exists to sequence.
- Risk legs (pinned posture): no stop, no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing path is the Dec-31 close. The absence of any stop is the source's posture (both sources describe a hold-the-year propensity, never a stop), disclosed, not invented.
- Direction: long-or-flat (derived pin: the source's up-leg is traded long; the source's down-leg forecast is fenced prediction, never a short order — adaptation (2)). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` bars of BTCUSDT only: `open` (February-1 entry fill), `close` (January formation arithmetic and December-31 exit fill), and bar UTC calendar date (month predicates). No `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: completed daily bar, one evaluation per bar; the formation sign uses only closes on or before the January-31 bar, and the entry fills on the next bar's open. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: 35 completed `1d` bars flat by record rule (covers the prior-year December-31 close plus a full January plus margin, so the first gated February entry can only fire on complete formation data — deterministic guard, disclosed as adaptation (5)). No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (month membership is the UTC calendar date of each daily bar — deterministic). First tradable year is the first calendar year whose prior December-31 close and full January both post-date the warmup.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the Almanac's S&P 500 equity universe; no cross-venue equivalence claimed).
- Order timing (declared port of the February-action timing): formation resolves at the January-31 close with next-open February-1 entry and December-31-close exit, compatible with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — next-open entry plus same-bar-close exit. No maker-touch, queue, or intrabar-path-dependent fill: at most one order exists on any bar (one entry per year, one close-all per long year), so there is no same-bar dual-fire whose ordering could change economics.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (neither source ships a sizing rule). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — a long year holds up to eleven months, so funding treatment is material and must be explicit). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; annual windows are disjoint by calendar construction (one evaluation per year), so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any Dec-31 exit the next Feb-1 entry fires only on a fresh positive January sign (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

Both sources ship the construction adopted here: the whole-month-January gain/loss trigger ("the whole-month gain or loss of the S&P 500 that triggers our January Barometer"), the February action timing, the Yale Hirsch 1972 lineage, and the hold-the-year posture. Track record as printed on the Almanac page: 12 major errors since 1950 for 83.3% accuracy including the error attributions (Vietnam 1966/1968, 1982 bull-market start, 2001, 2003, 2009, 2010/2014, 2016, 2018, 2020–2021), .722 including eight flat years. Wikipedia's regime split: ~75% total 1950–1984 (70% positive / 90% negative) decaying to ~50% negative-side 1985–2010. It ships zero adopted performance numbers for this record: every accuracy figure above describes the S&P 500/equity barometer, never a BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every accuracy figure (83.3%, .722 with flats, 75% 1950–1984, 50% negative-side 1985–2010) belongs to US equities — none transfers to BTCUSDT crypto, whose January microstructure differs arbitrarily, and none is adopted.
2. Down-January leg fenced as prediction, never traded: the source's "as January goes, so goes the year" covers down years, but neither source specifies short mechanics — this record holds flat instead (adaptation (2), disclosed). The decayed negative-side accuracy (coin-flip since 1985) is adopted as supporting caution for exactly this choice.
3. Flat-January tie rule fenced: a zero January return is a flat year by record rule, matching the source's separate flat-year accounting — disclosed convention, never a third position state.
4. Companion signals fenced: the First Five Days Early Warning and the Santa Claus Rally result named on the same page are never inputs here — no five-day or 7-session logic exists in this file.
5. Failure mode fenced: the page's own nine-since-2001 error cluster proves the barometer fails in regime breaks (rate shocks, wars, pandemics, Fed pivots) — a long year rides the entire adverse excursion with no guardrail; a −50% February–December drawdown is held to the Dec-31 close by construction. This is the coded trade, disclosed, not a tunable parameter here.
6. Cost silence fenced: neither source reports transaction costs or funding — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
7. Derivation boundary fenced: the only non-source behavior is the five declared adaptations (calendar-month mapping, long-or-flat posture, single asset, fixed sizing, next-open fill + warmup + house costs); the whole-month January trigger, the February action timing, the hold-through-December exit, and the no-stop stance are source-faithful. This record is therefore never evidence that the Almanac's equity finding passes.
8. The January-sign / Feb-1-open entry / Dec-31-close exit / strict-positive gate / single-position long-flat / `1d` BTCUSDT / 35-bar-warmup stance is pinned, not removed: shifting the formation month, softening the gate to non-negative, entering mid-January, adding a stop/target/cooldown/filter, re-enabling a short leg, trading partial size, or exiting before Dec 31 would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: January-sign gate / Feb-1-open entry / Dec-31-close exit / strict-positive trigger / single-position long-flat / `1d` BTCUSDT / 35-bar warmup are frozen.

- F1 — Gate relevance: replacing the pinned conditional hold with an unconditional February–December hold every year (ignoring the January sign) must not improve net expectancy; fail ⇒ the January gate adds nothing over the seasonal span itself.
- F2 — Entry-timing relevance: replacing the pinned Feb-1-open entry with a Feb-1-close entry (skipping the first session's gap) must not improve net expectancy; fail ⇒ the first February session adds nothing over the truncated hold.
- F3 — Exit-timing relevance: replacing the pinned Dec-31-close exit with a Nov-30-close exit (dropping December) must not improve net expectancy; fail ⇒ the December leg carries no advantage over the eleven-month-truncated hold.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; month predicates plus open/close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no holidays for the rule to skip (month membership is the UTC calendar date of each daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets, formation months, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: both sources' evidence is equities-only across multi-decade samples; BTCUSDT January behavior is unevidenced by either source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Mechanism mismatch: the offered mechanism (congressional calendar, State of the Union, January fund flows) is a US-equity institutional mechanism with no established crypto analogue — the port bets on calendar persistence, not on a verified crypto mechanism.
- Sample thinness: one evaluation per year means even a decade of crypto history yields ~10 gated decisions — statistical power is structurally weak, disclosed, not recovered.
- Open-confirmation lag: the entry fills at the Feb-1 open after the January sign resolves — gap-through moves across the January/February edge are taken at post-move opens, never at the January close.
- Year rigidity: drift arriving entirely within January is missed by record rule (entry waits for February); a year whose trend reverses per the sources' own error precedents is held anyway — disclosed, not recovered.
- Warmup cost: the first 35 daily bars are flat by record rule — pinned, not recovered (immaterial at one evaluation per year, disclosed for completeness).

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Stock Trader's Almanac (official creator site), Jeffrey A. Hirsch & Christopher Mistal, Yale Hirsch's Incredible January Barometer: Only 13 Major Errors in 84 Years (whole-month January S&P 500 gain/loss trigger, "as the S&P 500 goes in January, so goes the year" propensity, Yale Hirsch 1972 devising, 12 major errors since 1950 at 83.3% with .722 including eight flat years, February action timing, companion-signal fencing; 2022-01-06; verified live 2026-10-12): https://www.stocktradersalmanac.com/Alert/20220106.aspx
- Wikipedia, January barometer ("As goes January, so goes the year" hypothesis, Yale Hirsch 1972 first mention, 1950–1984 ~75% total with 70% positive / 90% negative, 1985–2010 negative-side decay to ~50%; verified live 2026-10-12): https://en.wikipedia.org/wiki/January_barometer
- Bibliographic lineage cited by the pages (not independently fetched; every pinned literal comes from the two pages above): Hirsch, Y. (1972), Stock Trader's Almanac (first recording of the January Barometer); Christian Felde, A deep dive into the January Barometer (regime-split statistics as reprinted on Wikipedia).
