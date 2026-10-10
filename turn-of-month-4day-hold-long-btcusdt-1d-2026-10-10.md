---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Turn-of-the-month 4-day calendar hold long on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-10
sources:
  - https://quantpedia.com/strategies/turn-of-the-month-in-equity-indexes/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Turn-of-the-month 4-day calendar hold long on BTCUSDT 1d bars

## Provenance

Primary source read end to end (public Quantpedia strategy page rendered in full and verified 2026-10-10):

- Quantpedia, `Turn of the Month in Equity Indexes`: https://quantpedia.com/strategies/turn-of-the-month-in-equity-indexes/ (canonical URL as pinned; page metadata: equities, 1 traded instrument, daily rebalancing, anomaly-validity confidence Strong, transaction costs Not Reported).
- Pinned window definition (verbatim in sense, page description section): "The beginning of the turn-of-the-month period is defined as the last trading day of the month and ending with the third trading day of the following month." Four sessions: days (−1, +3) in the page's Table 3 notation, where −1 is the last trading day of the month and +1..+3 are the first three trading days of the new month.
- Pinned academic lineage (page-cited, bibliographic): Lakonishok and Smidt (1988) — "on average, the four days at the turn-of-the-month account for all of the positive returns to the DJIA over the period of 1897-1986"; McConnell and Xu, `Equity Returns at the Turn of the Month` (SSRN 917884, backtest window 1926–2005) — "virtually all of the excess market return is accrued during the four-day turn-of-the-month period, and investors received little or no reward for bearing the market risk over the other 16 trading days of the month." The L&S and McConnell/Xu papers themselves were not independently fetched (paywalled/SSRN-gated at fetch time); every pinned literal above comes from the public Quantpedia page, which reprints the McConnell/Xu abstract verbatim.
- Pinned executable timing (verbatim in sense, page "Simple trading strategy" section): "Buy SPY ETF 1 day (some papers say 4 days) before the end of the month and sell the 3rd trading day of the new month at the close."
- Pinned robustness note (verbatim in sense, page tail): Table 3 panel A.1, annotated large-cap specification — "a 0.15% mean daily return on days −1 through +3 versus 0.01% on other days (difference 0.15%, t=7.81); the same seasonal pattern is also present in small-cap and high- and low-price portfolios and outside year-end/quarter-end settings."
- Page-shipped caution adopted as negative evidence (verbatim in sense): "caution is needed if one implements this strategy as calendar effects tend to vanish or rotate to different days in a month."
- Page metadata adopted as cost boundary: "Transaction costs: Not Reported" — no cost assumption of any kind is carried from the source.
- Licence and rights: a public strategy-summary page — this record cites and normalizes the rule (short phrases and the (−1,+3) day notation only) and reproduces no figures, code, backtest tables, or extended prose. The cited papers are referenced bibliographically only.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the page's (−1,+3) four-session turn-of-the-month hold ported to a single crypto asset on calendar days with close-based fills — not a lossless reproduction of the page's SPY/CRSP equity backtest. Researcher-declared adaptations are exactly five: (1) calendar-day mapping of the trading-day window (the 24/7 crypto tape has no market holidays, so every calendar day is a trading day and the L&S (−1,+3) window maps 1:1 onto calendar days — last calendar day of month M plus first three calendar days of month M+1 — principled port, not an arbitrary choice among calendars; see Signal); (2) single-asset BTCUSDT Binance perpetual (the DJIA/CRSP/SPY equity universe and every equity-level performance claim are fenced off, never carried — see Negative evidence 1); (3) entry pinned to the page's headline "1 day before the end of the month" (the parenthetical "some papers say 4 days" variant is fenced, never carried — see Negative evidence 5); (4) fixed 100%-equity single-position sizing with no leverage (the page ships no sizing rule — see Limitations); (5) an adopted 5-bar warmup flat by record rule plus house fees/funding treatment (the page reports no costs — see Execution assumptions). The (−1,+3) four-session window, the buy-before/sell-at-close timing, the long-only posture (the page's example buys SPY and holds nothing outside the window — flat, never short), the unconditional calendar trigger (no return conditioning, no filter), and the no-stop time-exit stance are source-faithful.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `turn.of.the.month`, `mcconnell`, `lakonishok`, `ariel`, `ogden`, `quantpedia`, `third trading day`, `last trading day` return zero strategy records — a new family in this pool. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md` holds the six-month May–October seasonal span; `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` holds a weekly Monday session; `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds a full calendar month only when the trailing 12-month return sign is positive (return-conditioned). Five-axis distinction: no pool record and no open PR holds only the four-session month-turn window (last day of month plus first three days of the next month) on an unconditional calendar trigger with no return, indicator, or seasonal-span conditioning.

## Economic mechanism

### Source-reported

Month-end cash-flow and rebalancing pressure: investors receive compensation, dividends, and interest at month-ends and pension/retail flows are reinvested into equities (Ogden 1990 payment-regularity hypothesis as summarized on the page; the page notes McConnell/Xu tests reject the narrow payment version and quote "This persistent peculiarity in equity returns remains a puzzle in search of an answer"). Month-end is additionally a natural rebalancing point for retail and professional portfolio models. The effect is not risk compensation (no higher standard deviation on turn-of-month days), not small-cap/low-price confined, not year-end or quarter-end confined, and is found in 30 non-US markets. Corroboration cited on the page: Reschenhofer (frequency-domain test confirms within-month S&P 500 patterns), Dzhabarov/Ziemba (seasonal anomalies including ToM persist in 1993–2009 futures data), Grimbrether/Swinkels/van Vliet (Halloween and ToM are the two strongest calendar effects, others diminish to zero), Carcano/Tornero ("the turn-of-the-month effect in S&P 500 futures contracts is the only calendar effect that is statistically and economically significant and persistent over time" — page-quoted).

### Research interpretation

Pure calendar drift-capture with maximum time out of market, long-only. Unlike return-conditioned monthly systems (TSMOM) there is no formation leg and no losing-signal concept: the position exists if and only if the calendar says so. Unlike seasonal-span holds (Sell-in-May, six months exposed) the exposure is four sessions per month (~13% of time), so the strategy is flat through the vast majority of tape including whole crises that fall outside the window — and equally unprotected against a crash landing inside the window. Unlike weekly calendar holds (Monday Drift) the trigger is the month boundary, a structurally different payroll/rebalancing clock. The bet, as derived, is purely that the documented month-turn drift ports to BTCUSDT calendar days, never on a level, band, oscillator, volume, return-sign, or funding anchor.

## Signal

Exact rule as pinned (window = last calendar day of month M plus first three calendar days of month M+1; entry at the close before the window; exit at the window's last close — any other window is a different, unpinned rule):

- Calendar convention (pinned): bar dates are UTC calendar dates of completed `1d` bars. Because the venue trades 24/7 with no holidays, every calendar day is a trading day, so the source (−1,+3) trading-day window maps 1:1 onto calendar days with no holiday-shift rule needed — disclosed derivation, no hidden calendar table.
- Window definition (pinned): for each month boundary, `D0` = last calendar day of month M; `D1`, `D2`, `D3` = first, second, third calendar days of month M+1. The holding window is the four sessions of D0..D3.
- Entry long (pinned timing, close-based): at the close of the completed `1d` bar dated D0−1 (the second-to-last calendar day of month M — the page's "1 day before the end of the month"), if flat (always true outside windows by construction), buy 100% equity at that close (same-bar-close fill). Entry predicate from the bar's own date alone: tomorrow is the last day of the month.
- Exit (pinned timing, close-based): at the close of the completed `1d` bar dated D3 (the page's "sell the 3rd trading day of the new month at the close"), close the full position at that close. Exit predicate: a position is open and today is the third calendar day of the month. Because entries happen only on D0−1 bars and windows never overlap, an open position on a 3rd-of-month close is always the matching window position — no pairing ambiguity, disclosed, not missing.
- Separation guarantee (pinned, structural): the entry bar (D0−1) and the exit bar (D3) are always distinct bars with four sessions between them, so no bar ever carries both an entry and an exit — no same-bar dual-fire exists to sequence.
- Risk legs (pinned posture): no stop, no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing path is the D3 close. The absence of any stop is the source's posture (the page ships a time-hold only), disclosed, not invented.
- Direction: long-only (derived pin matching the source example, which buys SPY and is flat — never short — outside the window). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (fills) and bar UTC calendar date (window predicates). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: completed daily bar, one evaluation per bar. Entry fills land on the D0−1 bar's own close; the exit lands on the D3 bar's own close. All inputs are completed-bar values — no provisional intrabar value is ever used.
- Warmup: 5 completed `1d` bars flat by record rule (window predicates need only the bar's own UTC date, so the guard is conventional, not structural — mirrors the standing small-guard record-rule precedent). No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (month membership is the UTC calendar date of each daily bar — deterministic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the page's SPY/CRSP equity universe; no cross-venue equivalence claimed).
- Order timing (declared port of the page's buy-before/sell-at-close timing): completed-bar decision with same-bar-close fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are one market entry per month boundary and one close-all per window — at most one order exists on any bar, so there is no same-bar dual-fire whose ordering could change economics.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (the page ships no sizing rule). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-only form is flat ~24–27 days per month between windows, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; month-turn windows are disjoint by calendar construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any D3 exit the next D0−1 entry fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The page ships the full construction adopted here: the (−1,+3) four-session window definition (last trading day through third trading day of the next month), the buy-1-day-before / sell-3rd-day-at-close executable timing, the long-flat posture (in equities only during the window, out otherwise), the Table 3 panel A.1 robustness read (0.15% mean daily return on days −1..+3 versus 0.01% on other days, difference 0.15%, t=7.81, large-cap specification; pattern also present in small-cap, high/low-price, non-year-end and non-quarter-end cuts), and the multi-paper corroboration chain (L&S 1988; McConnell/Xu 1926–2005; Reschenhofer; Dzhabarov/Ziemba; Halloween-interaction study; Carcano/Tornero futures persistence). It ships zero adopted performance numbers for this record: the page's indicative 7.2% p.a. / 6.9% vol / −20.79% drawdown / 1.04 Sharpe figures describe the Quantpedia-computed equity (−1,+3) segment, never a BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every return number, t-statistic, and persistence claim on the page (L&S DJIA 1897–1986, CRSP 1926–2005, SPY-segment indicatives) belongs to US (and cited non-US) equities — none transfers to BTCUSDT crypto, whose month-end payroll/rebalancing microstructure differs arbitrarily, and none is adopted.
2. Vanish/rotate caution adopted as-is: the page warns "calendar effects tend to vanish or rotate to different days in a month" — this record adds no regime guard and claims no persistence of any kind.
3. Cost silence fenced: page metadata states transaction costs Not Reported — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
4. Fully exposed inside the window: once entered, the position rides the entire adverse excursion with no guardrail — a −20% four-session crash is held to the D3 close by construction. This is the coded trade, disclosed, not a tunable parameter here.
5. Entry-timing variant fenced: the page notes "(some papers say 4 days) before the end of the month" — the 4-day-early entry is never carried; "1 day before" is the pinned headline rule (researcher pin among stated variants, predeclared — never presented as the sole paper convention).
6. Loose-summary sentence fenced: the page's informal line that prices rise "during the last four days and the first three days of each month" (seven sessions) contradicts its own precise (−1,+3) four-session definition and Table 3 — the 7-day reading is fenced, never carried; the precise definition governs.
7. Derivation boundary fenced: the only non-page behavior is the five declared adaptations (calendar-day mapping, single asset, 1-day-before pin, fixed sizing, warmup + house costs); the four-session window, the buy-before/sell-at-close timing, the unconditional calendar trigger, the long-flat posture, and the no-stop stance are source-faithful. This record is therefore never evidence that the page's equity strategy passes.
8. The (−1,+3)-calendar-day / D0−1-close entry / D3-close exit / unconditional-trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close stance is pinned, not removed: widening the window, adding the 4-day-early entry, adding a filter/return-gate/stop/target/cooldown, re-enabling a short leg, trading partial size, or holding past D3 would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 4-calendar-day window / D0−1-close entry / D3-close exit / unconditional trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Window-length relevance: replacing the pinned 4-session window with the fenced 7-session loose reading (last four plus first three calendar days) must not improve net expectancy; fail ⇒ the precise (−1,+3) boundary carries no advantage over the looser calendar span.
- F2 — Entry-timing relevance: replacing the pinned D0−1-close entry with a D0-close entry (capturing only D1..D3) must not improve net expectancy; fail ⇒ the first window session adds nothing over the truncated hold.
- F3 — Selectivity relevance: replacing the pinned window-only exposure with buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out the ~26 non-window days costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; bar-date predicates plus close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no holidays for the rule to skip (every calendar day is a trading day — deterministic on any continuously traded tape). Extension to other house-universe assets, windows, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the page's evidence is equities-only across up to 109-year samples; BTCUSDT month-turn behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Microstructure mismatch: the page's hypotheses (month-end payroll receipt, pension reinvestment, institutional rebalancing) are equity-market mechanisms with no established crypto analogue — the port bets on calendar persistence, not on a verified crypto mechanism.
- Entry-variant pin: "1 day before" is the headline rule, not the sole paper convention — the fenced 4-day-early variant would differ by construction.
- Close-confirmation lag: entries fill at the D0−1 close and exits at the D3 close — gap-through moves across window edges are taken at post-move closes, never at the edge.
- Window rigidity: drift arriving on D4+ or starting D0−2 is missed by record rule; a month whose drift rotates per the page's own caution is held anyway — disclosed, not recovered.
- Warmup cost: the first 5 daily bars are flat by record rule, so a month-turn window completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Quantpedia, Turn of the Month in Equity Indexes (window definition, SPY buy/sell timing, Table 3 panel A.1 robustness read, multi-paper corroboration chain, vanish/rotate caution, costs-not-reported metadata; verified live 2026-10-10): https://quantpedia.com/strategies/turn-of-the-month-in-equity-indexes/
- Bibliographic lineage cited by the page (not independently fetched; every pinned literal comes from the page above): Lakonishok, J., Smidt, S. (1988), *Are Seasonal Anomalies Real? A Ninety-Year Perspective*, Review of Financial Studies 1:403–425; McConnell, J. J., Xu, W. (2008), *Equity Returns at the Turn of the Month*, Financial Analysts Journal 64(2); Ariel, R. A. (1987), *A Monthly Effect in Stock Returns*, Journal of Financial Economics 18:161–174; Ogden, J. P. (1990), *Turn-of-Month Evaluations of Liquid Profits and Stock Returns*, Journal of Finance 45.
