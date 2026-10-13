---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: FOMC pre-announcement drift scheduled-day hold long on BTCUSDT 1d bars
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
  - https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf
  - https://www.newyorkfed.org/research/staff_reports/sr512.html
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1923197
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FOMC pre-announcement drift scheduled-day hold long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (PDF fetched and verified live 2026-10-13, 1,177,349 bytes, SHA-256 `c7cb0f335c60cb9fc305189935fb7c51e98fa8461c2b33efd51eb5a5c3f2e34b`):

- Lucca, D. O., Moench, E., `The Pre-FOMC Announcement Drift`, Federal Reserve Bank of New York Staff Report No. 512 (September 2011; revised August 2013): https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf (landing page: https://www.newyorkfed.org/research/staff_reports/sr512.html; SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1923197).
- Published version (bibliographic, official NY Fed landing page): Lucca & Moench, "The Pre-FOMC Announcement Drift," *Journal of Finance* 70(1) (February 2015): 329–371.
- Pinned scope (verbatim in sense, §1): "Only the occurrence of scheduled meetings is known to investors in advance, and because we study returns ahead of monetary policy news we exclusively consider these meetings in this paper." Scheduled meetings run eight times per year since 1981 (§1). Unscheduled meetings are enumerated and excluded (§2: April 18 1994, October 15 1998, January 3 2001, September 17 2001, January 21 2008, October 7 2008, plus liquidity-facility statements and 24 statement-less intermeeting calls).
- Pinned headline window (verbatim in sense, §2): post-1994 evidence rests on "the 24-hour period from 2 pm on the day before a scheduled FOMC announcement until 2 pm on the day of a scheduled FOMC announcement, or about fifteen minutes before the announcement release time," which "by construction" contains no meeting outcome.
- Pinned executable (verbatim in sense, §3.1/Table 2): "The simple strategy that consists in buying the SPX at 2 pm the day before a scheduled FOMC announcement, selling fifteen minutes before the announcement and holding cash on all other days would have earned a large annualized Sharpe ratio of 1.14." Headline estimates: 49bp mean 24-hour pre-FOMC excess return (t > 4.5, Huber-White); 3.89% annualized in-window versus 0.88% on all other days, i.e. about 80% of annual realized excess stock returns since 1994 earned in the pre-FOMC window; 98 of 131 pre-FOMC returns positive (Table 3); post-announcement (2pm-to-close) mean return zero.
- Pinned daily-bar variant adopted here (verbatim in sense, §3.1/Table 2 col 4): close-to-close FOMC-day excess-return differential "somewhat lower at about 33 basis points," still highly significant with annualized Sharpe 0.84, accounting for "more than half of realized excess stock returns (2.7% compared to 2.08% on all other days)."
- Pinned supporting facts: pre-1994 window is the meeting day itself with 20bp mean 1980–1993 (§3.2/Table 4); no reversal on surrounding days (§3.3/Table 5); pre-FOMC dummy survives White (2000) reality-check over nine other macro releases (p < 0.02%, §3.4); no drift in Treasuries/fed-funds/Eurodollar futures (§3.7/Table 8) and none ahead of nine other macro releases (§3.7/Table 7); blackout week with no policy communication precedes each meeting (§1); leakage explanation rejected (§4.2).
- Licence and rights: a public central-bank staff report — this record cites and normalizes the rule (short phrases and the scheduled-day notation only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's close-to-close FOMC-day hold ported to a single crypto asset on completed `1d` bars — not a lossless reproduction of the paper's SPX intraday backtest. Researcher-declared adaptations are exactly five: (1) daily-bar mapping of the paper's 2pm-to-2pm window onto the paper's own published close-to-close FOMC-day variant (D−1 close entry, D0 close exit — the paper's Table 2 col 4 construction, not an invented intraday approximation; the 24-hour 2pm intraday variant is fenced, never carried — see Negative evidence 5); (2) single-asset BTCUSDT Binance perpetual (the SPX/CRSP universe and every equity-level performance claim are fenced off, never carried — see Negative evidence 1); (3) scheduled-date set taken as the Federal Reserve's published scheduled-meeting calendar (ex-ante known by the paper's own §1 premise; unscheduled/emergency meetings never qualify — see Signal); (4) fixed 100%-equity single-position sizing with no leverage (the paper ships no sizing rule — see Limitations); (5) an adopted 5-bar warmup flat by record rule plus house fees/funding treatment (the paper reports no costs — see Execution assumptions). The scheduled-only scope, the buy-before/sell-at-window-end timing, the long-only posture (the paper documents an upward anticipation drift with cash held otherwise — never a short), the unconditional trigger (no VIX/slope/past-return conditioning is traded), and the no-stop time-exit stance are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `fomc`, `lucca`, `moench`, `federal.open.market`, `pre.announcement`, `pre.fomc`, `scheduled.meeting`, `blackout` return zero strategy records — a new family in this pool (the only `reversal`-class hits are generic prose in unrelated indicator files, and the TSMOM record's Jegadeesh-Titman (1993) citation is a holding-construction reference, not a strategy). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md` and `santa-claus-rally-yearend-hold-long-btcusdt-1d-2026-10-12.md` hold fixed month/year-boundary calendar windows; `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` holds a weekly weekday session; `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds a full month conditioned on trailing-return sign. Five-axis distinction: no pool record and no open PR holds only the eight-per-year Fed-scheduled announcement days (D−1-close to D0-close) on an event-calendar trigger with no return, indicator, or month/week/year-boundary conditioning.

## Economic mechanism

### Source-reported

Anticipation premium ahead of scheduled monetary-policy news that standard asset pricing cannot easily explain: large positive mean returns accrue while realized volatility, implied volatility (VIX), and trading volume are all *low* (§3.5), then volatility and volume jump at the release while the post-announcement mean return is zero — the disconnect between when returns are earned and when news arrives is the paper's central puzzle (§4.1). Candidate explanations tested and rejected or left incomplete: systematic-risk compensation (contradicted by the timing/volatility pattern and by the absence of drift in rate-sensitive fixed income, §4.1), good-news/secular-easing stories (§4.2), information leakage (rejected on sign-consistency, correlation, and cross-asset grounds, §4.2), volatility-feedback/liquidity innovations (explain at most a fraction; dummy stays 32–36bp and significant, §4.2). The drift is equity-specific (no Treasuries/futures drift, §3.7), macro-release-specific (no drift before nine other U.S. releases, §3.7), and international (29–52bp across five European indices, §3.6). Conditioning correlates (low yield-curve slope, high VIX, high past pre-FOMC returns, §3.8) are explanatory regressions, never traded rules.

### Research interpretation

Pure scheduled-event drift-capture with maximum time out of market, long-only. Unlike fixed-calendar holds (ToM/Santa/Monday) the trigger is an externally published policy-event calendar (~8 days/year exposure, ~2% of time), so the strategy is flat through essentially the entire tape including whole crises — and equally unprotected against a crash landing on an FOMC day. Unlike return-conditioned monthly systems (TSMOM) there is no formation leg and no losing-signal concept: the position exists if and only if the Fed schedule says so. Unlike indicator/funding-anchored systems the bet is purely that the documented pre-announcement anticipation drift ports to BTCUSDT daily bars, never on a level, band, oscillator, volume, return-sign, or funding anchor. The blackout-week premise (§1) is what makes the trigger causal: the dates are public before the window opens.

## Signal

Exact rule as pinned (D0 = scheduled FOMC announcement calendar date (ET); entry at the D0−1 close; exit at the D0 close — any other window is a different, unpinned rule):

- Date set (pinned): D0 runs over scheduled FOMC announcement dates as published by the Federal Reserve (the paper's §1 premise is that only scheduled meetings are known in advance; unscheduled/emergency/intermeeting actions never qualify — the §2 exclusion list is the standing precedent). Each D0 is a single ET calendar date; two-day meetings contribute their announcement day only.
- Calendar convention (pinned): bar dates are UTC calendar dates of completed `1d` bars. Announcement dates are ET calendar dates; the mapping uses the ET date printed on the Fed schedule, evaluated against the UTC bar whose calendar date contains the announcement — deterministic, no session template, no holiday-shift rule (the 24/7 tape has no holidays).
- Entry long (pinned timing, close-based): at the close of the completed `1d` bar dated D0−1 (the calendar day before the announcement — the paper's "buying the SPX at 2 pm the day before" mapped onto its own close-to-close variant), if flat (always true outside windows by construction), buy 100% equity at that close (same-bar-close fill). Entry predicate from the bar's own date alone: tomorrow is a scheduled FOMC announcement date.
- Exit (pinned timing, close-based): at the close of the completed `1d` bar dated D0, close the full position at that close. Exit predicate: a position is open and today is a scheduled FOMC announcement date. Because entries happen only on D0−1 bars and scheduled meetings are weeks apart, an open position on a D0 close is always the matching window position — no pairing ambiguity, disclosed, not missing.
- Separation guarantee (pinned, structural): the entry bar (D0−1) and the exit bar (D0) are always distinct bars with one session between them, so no bar ever carries both an entry and an exit — no same-bar dual-fire exists to sequence. Consecutive D0 dates never occur in the published schedule, so overlapping windows are structurally impossible.
- Risk legs (pinned posture): no stop, no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing path is the D0 close. The absence of any stop is the source's posture (the paper ships a time-hold only), disclosed, not invented.
- Direction: long-only (derived pin matching the source, which documents an upward anticipation drift with cash held otherwise — never a short leg). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (fills) and bar UTC calendar date (window predicates). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or market-data-feed dependency of any kind.
- One external calendar input, point-in-time clean by construction: the Federal Reserve's published scheduled-FOMC-announcement dates, known to investors in advance per the paper's §1 premise (the schedule for a year is public before any of that year's windows opens). No release-time, statement-text, decision-outcome, surprise, VIX, yield-curve, or volume input enters any rule.
- Single decision grid: completed daily bar, one evaluation per bar. The entry fills on the D0−1 bar's own close; the exit lands on the D0 bar's own close. All inputs are completed-bar values plus the ex-ante-published schedule — no provisional intrabar value, no future reference, no announcement outcome is ever used.
- Warmup: 5 completed `1d` bars flat by record rule (window predicates need only the bar's own UTC date plus the pre-published schedule, so the guard is conventional, not structural — mirrors the standing small-guard record-rule precedent). No repainting, no negative shift, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's SPX universe; no cross-venue equivalence claimed).
- Order timing (declared port of the paper's buy-before/sell-at-window-end timing via its close-to-close variant): completed-bar decision with same-bar-close fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are one market entry per scheduled meeting and one close-all per window — at most one order exists on any bar, so there is no same-bar dual-fire whose ordering could change economics. The paper's 2pm/2:15pm intraday legs are deliberately not modelled (fenced — see Negative evidence 5).
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (the paper ships no sizing rule). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-only form is flat ~357 days per year between windows, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; scheduled-meeting windows are disjoint by published-schedule construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any D0 exit the next D0−1 entry fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships the full construction adopted here: the scheduled-meetings-only scope (§1, eight per year since 1981), the buy-before/sell-before-announcement executable timing (§3.1, Sharpe 1.14 for the 24-hour variant), the long-with-cash-otherwise posture, the close-to-close FOMC-day variant adopted by this record (differential ~33bp, Sharpe 0.84, more than half of realized excess returns — Table 2 col 4), the unconditional trigger (drift is earned ahead of the announcement regardless of the eventual decision; surprises average to zero, §3.1), and the equity-only statistics — 49bp mean 24-hour drift (t > 4.5), 3.89%/yr in-window vs 0.88% outside (~80% share), 98/131 positive windows, 20bp 1980–1993 pre-1994, no reversals, zero post-announcement mean. It ships zero adopted performance numbers for this record: every basis-point, share, and Sharpe figure above describes SPX/equity windows, never a BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every basis-point, share-of-returns, hit-rate, and Sharpe figure (49bp; 3.89% vs 0.88%; ~80%; 1.14; 98/131; 33bp/0.84 close-to-close; 20bp pre-1994) belongs to SPX/U.S. (and cited international) equities — none transfers to BTCUSDT crypto, whose FOMC-day microstructure (24/7, no open/close, funding, weekend-adjacent meetings) differs arbitrarily, and none is adopted.
2. Sample-end fence: the paper's intraday sample ends March 2011 (131 meetings, Sep 1994–Mar 2011); no post-2011 persistence, decay, or regime claim of any kind is carried — this record adds no out-of-sample guard and claims no persistence.
3. Conditioning regressions fenced: yield-curve slope, VIX level, and past-pre-FOMC-average (MA8) predict drift variation (§3.8) but are never traded here — the trigger stays unconditional per the paper's headline strategy; adding any of them would be a different, unpinned rule.
4. Announcement-conditional response fenced: Bernanke-Kuttner-style surprise responses average to zero in-sample (§3.1) — this record holds no position into the outcome by construction (D0-close exit) and claims nothing about conditional announcement effects.
5. Intraday 2pm variant fenced: the paper's headline 49bp/1.14-Sharpe construction needs 2pm–2pm timestamped fills; this record carries only the paper's own close-to-close variant (33bp/0.84) on daily bars — the intraday timing edge is never claimed for the daily port.
6. Non-findings adopted as specificity, never as rules: no drift in Treasuries/rate futures (§3.7/Table 8), none before nine other macro releases (§3.7/Table 7), leakage rejected (§4.2) — carried only to show the trigger is FOMC-specific, not a generic event-day hold.
7. Cost silence fenced: the paper reports no transaction costs — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
8. Fully exposed inside the window: once entered, the position rides the entire adverse excursion with no guardrail — a −20% FOMC-day crash is held to the D0 close by construction. This is the coded trade, disclosed, not a tunable parameter here.
9. Derivation boundary fenced: the only non-paper behavior is the five declared adaptations (close-to-close daily mapping, single asset, published-schedule date set, fixed sizing, warmup + house costs); the scheduled-only scope, the buy-before/sell-at-window-end timing, the unconditional trigger, the long-flat posture, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity strategy passes.
10. The scheduled-D0 / D0−1-close entry / D0-close exit / unconditional-trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close stance is pinned, not removed: widening the window (e.g. adding D0+1), trading the intraday 2pm legs, conditioning on VIX/slope/past drift, admitting unscheduled meetings, adding a stop/target/cooldown, re-enabling a short leg, trading partial size, or holding past D0 would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: scheduled-D0 set / D0−1-close entry / D0-close exit / unconditional trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Window-length relevance: replacing the pinned D0-day hold with a two-day hold (D0−1-close entry to D0+1-close exit, adding the post-announcement session the paper finds averages zero) must not improve net expectancy; fail ⇒ the paper's zero-post-announcement finding does not bind the crypto port and the exit pin is doing unacknowledged work.
- F2 — Entry-timing relevance: replacing the pinned D0−1-close entry with a D0-open-proxy entry (the D0 bar's own first traded price — capturing only the announcement-day leg) must not improve net expectancy; fail ⇒ the overnight/pre-day session adds nothing over the announcement-day-only hold.
- F3 — Selectivity relevance: replacing the pinned schedule-only exposure with buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out the ~357 non-FOMC days costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; bar-date predicates plus close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no holidays for the rule to skip; FOMC announcement dates map onto UTC bar dates deterministically (every calendar day is a trading day). Extension to other house-universe assets, windows, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is SPX/equity-only across up to 51-year samples; BTCUSDT FOMC-day behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Microstructure mismatch: the paper's window is an equity-market-hours phenomenon (2pm-to-2pm around a 2:15pm ET release with an overnight halt); the 24/7 crypto tape has no halt, no open/close, and perverse adjacencies (weekend D0−1 bars, funding prints inside the window) — the port bets on anticipation-drift persistence, not on a verified crypto mechanism.
- Release-time drift: since April 2011 release times vary (12:30pm–2pm, §1); the daily-bar port is invariant to this (D0-close exit always follows the release), but it also always *includes* post-release hours the paper finds average zero — disclosed, not recovered.
- Sample thinness: eight one-day windows per year means even a decade of crypto history yields only ~80 sessions of exposure — statistical power is structurally weak, disclosed, not recovered.
- Close-confirmation lag: the entry fills at the D0−1 close and the exit at the D0 close — gap-through moves across window edges are taken at post-move closes, never at the edge.
- Window rigidity: drift arriving on D0−2 or reversing on D0+1 is missed or eaten by record rule; a meeting whose drift fails per the source's own 33 negative windows is held anyway — disclosed, not recovered.
- Warmup cost: the first 5 daily bars are flat by record rule — pinned, not recovered (immaterial at eight windows per year, disclosed for completeness).

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Lucca, D. O., Moench, E., *The Pre-FOMC Announcement Drift*, Federal Reserve Bank of New York Staff Report No. 512 (September 2011; revised August 2013) — 24-hour 2pm-to-2pm window definition (§2), scheduled-meetings-only scope with unscheduled exclusions (§1–§2), headline 49bp / ~80% / Sharpe 1.14 and close-to-close 33bp / Sharpe 0.84 variant (Table 2, §3.1), 98/131 positivity (Table 3), pre-1994 20bp (§3.2/Table 4), no reversals (§3.3/Table 5), reality-check (§3.4), international evidence (§3.6/Table 6), macro/fixed-income non-findings (§3.7/Tables 7–8), conditioning correlates (§3.8), rejected explanations (§4); PDF verified live 2026-10-13 (1,177,349 bytes, SHA-256 `c7cb0f33…5a5c3f2e`): https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf
- Official landing page (published-version lineage: *Journal of Finance* 70(1), February 2015, 329–371; verified live 2026-10-13): https://www.newyorkfed.org/research/staff_reports/sr512.html
- SSRN record (verified live 2026-10-13): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1923197
