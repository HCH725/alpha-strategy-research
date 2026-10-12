---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Santa Claus Rally year-end 7-session calendar hold long on BTCUSDT 1d bars
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
  - https://www.stocktradersalmanac.com/Alert/20160105.aspx
  - https://en.wikipedia.org/wiki/Santa_Claus_rally
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Santa Claus Rally year-end 7-session calendar hold long on BTCUSDT 1d bars

## Provenance

Primary sources read end to end (both fetched and verified live 2026-10-12):

- Stock Trader's Almanac (official creator site), Jeffrey A. Hirsch & Christopher Mistal, `Santa Claus Rally Official Results & Free Lunch Update: Santa is a No Show`, 2016-01-05: https://www.stocktradersalmanac.com/Alert/20160105.aspx — pinned window definition (verbatim in sense): "As defined in the Stock Trader's Almanac, the Santa Claus Rally (SCR) is the propensity for the S&P 500 to rally the last five trading days of December and the first two of January an average of 1.4% since 1950." The page further states the miss-base-rate context adopted as caution: "Including this year, Santa has failed to pay Wall Street a visit in just 15 years since 1950" and that "The lack of a rally can be a preliminary indicator of tough times to come. This was certainly the case in 2008 and 2000. A 4.0% decline in 2000 foreshadowed the bursting of the tech bubble and a 2.5% loss in 2008 preceded the second worst bear market in history."
- Wikipedia, `Santa Claus rally` (page last edited 2025-12-25, fetched 2026-10-12): https://en.wikipedia.org/wiki/Santa_Claus_rally — pinned corroboration (verbatim in sense): "A Santa Claus rally is a calendar effect that involves a rise in stock prices during the last 5 trading days in December and the first 2 trading days in the following January." Origin lineage: "The Santa Claus rally was first recorded by Yale Hirsch in his Stock Trader's Almanac in 1972." Statistics reprinted from the 2019 Almanac: the market "has risen 1.3% on average during the 7 trading days in the period since both 1950 and 1969" and "stock prices have historically risen 76% of the time" over those 7 trading days. Hypotheses listed as unsettled: January-effect front-running, light holiday volume, tax-loss-harvest slowdown, holiday absence of short sellers — adopted only as mechanism colour, never as rules.
- Licence and rights: public summary/reference pages — this record cites and normalizes the rule (short phrases and the 5+2 session notation only) and reproduces no figures, code, backtest tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the Almanac's December/January 7-session window ported to a single crypto asset on calendar days with close-based fills — not a lossless reproduction of the Almanac's S&P 500 equity finding. Researcher-declared adaptations are exactly four: (1) calendar-day mapping of the trading-day window (the 24/7 crypto tape has no market holidays, so every calendar day is a trading day and the 5+2 window maps 1:1 onto Dec 27–31 plus Jan 1–2 — principled port, not an arbitrary choice among calendars; see Signal); (2) single-asset BTCUSDT Binance perpetual (the S&P 500 universe and every equity-level performance claim are fenced off, never carried — see Negative evidence 1); (3) fixed 100%-equity single-position sizing with no leverage (neither source ships a sizing rule — see Limitations); (4) an adopted 5-bar warmup flat by record rule plus house fees/funding treatment (neither source reports costs — see Execution assumptions). The 7-session window, the buy-before/sell-at-window-end timing, the long-only posture (the source describes a rally to be ridden, never a short), the unconditional calendar trigger (no return conditioning, no filter), and the no-stop time-exit stance are source-faithful.

Pre-write dedup (2026-10-12): working-tree case-insensitive searches for `santa`, `hirsch`, `santaclaus`, `christmas.*rally`, `december.*january.*seven`, `first two.*january`, `last five.*december` return zero strategy records — a new family in this pool. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md` holds the 4-session month-turn window at every month boundary (twelve windows per year); `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md` holds the six-month May–October seasonal span; `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` holds a weekly Monday session; `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds a full calendar month only when the trailing 12-month return sign is positive (return-conditioned). Five-axis distinction: no pool record and no open PR holds only the single annual December-to-January 7-session window (last five days of December plus first two days of January) on an unconditional calendar trigger with no return, indicator, or seasonal-span conditioning.

## Economic mechanism

### Source-reported

Year-end/holiday market microstructure: the Almanac page ties the window to the year-end cluster (the SCR sits inside the "Free Lunch" year-end/tax-loss-selling/January-Effect complex on STA pages 110–114) and treats a missing rally as a forward caution flag (2000/2008 precedents quoted above). Wikipedia lists the commonly offered hypotheses with the explicit caveat "There is no generally accepted explanation for the phenomenon": anticipation of the January effect, lighter holiday volume easing upward moves, slowing tax-loss harvesting that had depressed early-December prices, and holiday absence of pessimistic/short participants. The Dow corollary (better forward performance after failed-Santa years) is reported on the page and fenced — it is never a rule here.

### Research interpretation

Pure calendar drift-capture with maximum time out of market, long-only, one window per year. Unlike monthly turn-of-month (twelve 4-session holds) the exposure is seven sessions per year (~2% of time), so the strategy is flat through essentially the entire tape including whole crises — and equally unprotected against a crash landing inside the window. Unlike seasonal-span holds (Sell-in-May, six months exposed) there is no regime thesis beyond the documented year-end drift. Unlike return-conditioned monthly systems (TSMOM) there is no formation leg and no losing-signal concept: the position exists if and only if the calendar says so. Unlike weekly calendar holds (Monday Drift) the trigger is the single year boundary, a structurally different holiday/payroll/rebalancing clock. The bet, as derived, is purely that the documented year-end drift ports to BTCUSDT calendar days, never on a level, band, oscillator, volume, return-sign, or funding anchor.

## Signal

Exact rule as pinned (window = last five calendar days of December plus first two calendar days of January; entry at the close before the window; exit at the window's last close — any other window is a different, unpinned rule):

- Calendar convention (pinned): bar dates are UTC calendar dates of completed `1d` bars. Because the venue trades 24/7 with no holidays, every calendar day is a trading day, so the source 5+2 trading-day window maps 1:1 onto calendar days with no holiday-shift rule needed — disclosed derivation, no hidden calendar table.
- Window definition (pinned): `W1`..`W5` = December 27, 28, 29, 30, 31; `W6`, `W7` = January 1, 2 of the following year. The holding window is these seven sessions.
- Entry long (pinned timing, close-based): at the close of the completed `1d` bar dated December 26 (the day before the window), if flat (always true outside windows by construction), buy 100% equity at that close (same-bar-close fill). Entry predicate from the bar's own date alone: tomorrow is December 27.
- Exit (pinned timing, close-based): at the close of the completed `1d` bar dated January 2 (the window's last session), close the full position at that close. Exit predicate: a position is open and today is January 2. Because entries happen only on December-26 bars and windows never overlap, an open position on a January-2 close is always the matching window position — no pairing ambiguity, disclosed, not missing.
- Separation guarantee (pinned, structural): the entry bar (Dec 26) and the exit bar (Jan 2) are always distinct bars with seven sessions between them, so no bar ever carries both an entry and an exit — no same-bar dual-fire exists to sequence.
- Risk legs (pinned posture): no stop, no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing path is the Jan-2 close. The absence of any stop is the source's posture (both sources describe a hold-through-the-window drift, never a stop), disclosed, not invented.
- Direction: long-only (derived pin matching the source, which describes a rally to be long, never a short leg). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (fills) and bar UTC calendar date (window predicates). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: completed daily bar, one evaluation per bar. The entry fills on the Dec-26 bar's own close; the exit lands on the Jan-2 bar's own close. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: 5 completed `1d` bars flat by record rule (window predicates need only the bar's own UTC date, so the guard is conventional, not structural — mirrors the standing small-guard record-rule precedent). No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (month/day membership is the UTC calendar date of each daily bar — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the Almanac's S&P 500 equity universe; no cross-venue equivalence claimed).
- Order timing (declared port of the buy-before/sell-at-window-end timing): completed-bar decision with same-bar-close fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are one market entry per year and one close-all per window — at most one order exists on any bar, so there is no same-bar dual-fire whose ordering could change economics.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (neither source ships a sizing rule). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-only form is flat ~358 days per year between windows, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; year-end windows are disjoint by calendar construction (one per year), so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any Jan-2 exit the next Dec-26 entry fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

Both sources ship the construction adopted here: the 5+2 seven-session window (last five trading days of December plus first two of January), the first-recording lineage (Yale Hirsch, Stock Trader's Almanac, 1972), the long-hold posture through the window, and the equity-only statistics — Almanac page: 1.4% average since 1950; Wikipedia reprint of the 2019 Almanac: 1.3% average since both 1950 and 1969 with a 76% historical hit rate over the 7 trading days. It ships zero adopted performance numbers for this record: every return/average/hit-rate figure above describes the S&P 500/equity window, never a BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every average-return, hit-rate, and persistence figure (1.4% since 1950; 1.3% since 1950/1969; 76% of the time; 15 misses since 1950) belongs to US equities — none transfers to BTCUSDT crypto, whose year-end microstructure differs arbitrarily, and none is adopted.
2. Miss-as-caution adopted as-is, never as a rule: the Almanac page warns a missing rally "can be a preliminary indicator of tough times to come" (2000 −4.0% / 2008 −2.5% precedents) — this record adds no conditional logic, no skip-after-miss filter, and claims no forward predictive power of any kind.
3. Failure mode fenced: the Wikipedia page reports a 2024–2025 "reverse Santa Claus rally" (S&P 500 selling off through the Christmas-to-New-Year business days, described as a historic first; page-flagged as needing citation) — adopted as proof the window can fail outright, never as a contrasting rule.
4. Cost silence fenced: neither source reports transaction costs — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
5. Fully exposed inside the window: once entered, the position rides the entire adverse excursion with no guardrail — a −20% seven-session crash is held to the Jan-2 close by construction. This is the coded trade, disclosed, not a tunable parameter here.
6. Dow corollary fenced: the page-reported better forward Dow years after failed Santas is never carried — no post-window conditional holding exists here.
7. Derivation boundary fenced: the only non-source behavior is the four declared adaptations (calendar-day mapping, single asset, fixed sizing, warmup + house costs); the 7-session window, the buy-before/sell-at-window-end timing, the unconditional calendar trigger, the long-flat posture, and the no-stop stance are source-faithful. This record is therefore never evidence that the Almanac's equity finding passes.
8. The 5+2-calendar-day / Dec-26-close entry / Jan-2-close exit / unconditional-trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close stance is pinned, not removed: widening the window, adding a filter/return-gate/stop/target/cooldown, re-enabling a short leg, trading partial size, or holding past Jan 2 would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 7-session window / Dec-26-close entry / Jan-2-close exit / unconditional trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Window-length relevance: replacing the pinned 7-session window with a December-only hold (Dec-26-close entry to Dec-31-close exit, dropping the January leg) must not improve net expectancy; fail ⇒ the two January sessions carry no advantage over the December-only span.
- F2 — Entry-timing relevance: replacing the pinned Dec-26-close entry with a Dec-27-close entry (capturing only six of the seven sessions) must not improve net expectancy; fail ⇒ the first window session adds nothing over the truncated hold.
- F3 — Selectivity relevance: replacing the pinned window-only exposure with December buy-and-hold over the same sample (Dec-1-close entry to Dec-31-close exit each year) must not improve net expectancy; fail ⇒ sitting out the ~24 non-window December days costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; bar-date predicates plus close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no holidays for the rule to skip (every calendar day is a trading day — deterministic on any continuously traded tape). Extension to other house-universe assets, windows, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: both sources' evidence is equities-only across up to 75-year samples; BTCUSDT year-end behavior is unevidenced by either source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Microstructure mismatch: the offered hypotheses (January-effect front-running, holiday-thin volume, tax-loss-harvest rhythm, holiday absence of shorts) are equity-market mechanisms with no established crypto analogue — the port bets on calendar persistence, not on a verified crypto mechanism.
- Sample thinness: one 7-session window per year means even a decade of crypto history yields only ~70 sessions of exposure — statistical power is structurally weak, disclosed, not recovered.
- Close-confirmation lag: the entry fills at the Dec-26 close and the exit at the Jan-2 close — gap-through moves across window edges are taken at post-move closes, never at the edge.
- Window rigidity: drift arriving before Dec 27 or after Jan 2 is missed by record rule; a year whose drift rotates or reverses per the sources' own miss precedents is held anyway — disclosed, not recovered.
- Warmup cost: the first 5 daily bars are flat by record rule — pinned, not recovered (immaterial at one window per year, disclosed for completeness).

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Stock Trader's Almanac (official creator site), Jeffrey A. Hirsch & Christopher Mistal, Santa Claus Rally Official Results & Free Lunch Update: Santa is a No Show (window definition as the Almanac's SCR: last five trading days of December plus first two of January, 1.4% average since 1950; miss-base-rate and 2000/2008 caution; 2016-01-05; verified live 2026-10-12): https://www.stocktradersalmanac.com/Alert/20160105.aspx
- Wikipedia, Santa Claus rally (7-session window corroboration, Yale Hirsch 1972 origin, 2019 Almanac 1.3% average since 1950/1969 with 76% hit rate, unsettled hypotheses, reverse-rally failure mode; verified live 2026-10-12): https://en.wikipedia.org/wiki/Santa_Claus_rally
- Bibliographic lineage cited by the pages (not independently fetched; every pinned literal comes from the two pages above): Hirsch, Y. (1972), Stock Trader's Almanac (first recording of the SCR); Stock Trader's Almanac 2016, pp. 110–114 (Free Lunch / January Effect / SCR complex); Stock Trader's Almanac 2019 (window statistics as reprinted on Wikipedia).
