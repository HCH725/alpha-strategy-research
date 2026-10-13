---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Pre-holiday drift scheduled pre-closure session hold long on BTCUSDT 1d bars
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
  - https://econpapers.repec.org/RePEc:bla:jfinan:v:45:y:1990:i:5:p:1611-26
  - https://www.jstor.org/stable/2328753
  - https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1990.tb03731.x
  - https://www.nyse.com/markets/hours-calendars
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pre-holiday drift scheduled pre-closure session hold long on BTCUSDT 1d bars

## Provenance

Primary source verified live at abstract/bibliographic level (RePEc EconPapers page fetched 2026-10-13, 12,065 bytes, SHA-256 `7a5e36352c80115d5eeed40925519aee7d1701b49943b64a13d3bb8c0d2615cf`):

- Ariel, R. A., `High Stock Returns before Holidays: Existence and Evidence on Possible Causes`, *Journal of Finance* 45(5) (December 1990): 1611–1626. DOI: https://doi.org/10.1111/j.1540-6261.1990.tb03731.x (JSTOR stable: https://www.jstor.org/stable/2328753; RePEc: https://econpapers.repec.org/RePEc:bla:jfinan:v:45:y:1990:i:5:p:1611-26).
- Pinned headline scope (abstract, verbatim in sense): "On the trading day prior to holidays, stocks advance with disproportionate frequency and show high mean returns averaging nine to fourteen times the mean return for the remaining days of the year."
- Pinned concentration (abstract, verbatim in sense): "Over one third of the total return accruing to the market portfolio over the 1963–1982 period was earned on the eight trading days which each year fall before holiday market closings."
- Pinned intraday shape (abstract, verbatim in sense): "Examination of hourly preholiday stock returns reveals high returns throughout the day."
- Pinned out-of-sample check (abstract, verbatim in sense): "Preholiday stock returns in the posttest 1983–1986 period are also examined."
- Access boundary (stated on the fetched RePEc page itself): "Access to full text is restricted to JSTOR subscribers." The Wiley page is Cloudflare-gated and JSTOR requires login, so no table/figure-level mean, t-statistic, or hourly-bin number is pinned here — every exact table-level figure is omitted per policy, never paraphrased from secondary reprints.
- Indexing-level corroboration only (landing-page abstracts, never fetched full text, never adopted as rules): Cadsby/Ratner-line `Holiday Effects and Stock Returns: Further Evidence` (abnormally high pre-holiday returns on NYSE/AMEX/NASDAQ plus U.K./Japanese markets independent of the U.S. effect; no size effect in pre-holiday mean returns); Chong, Hudson & Keasey (2005), `Pre-holiday effects: International evidence on the decline and reversal of a stock market anomaly` (post-publication decline/reversal — carried as negative evidence 2, abstract-level only).
- Holiday-calendar source fetched and verified live 2026-10-13 (109,229 bytes, SHA-256 `79602f7be5a8f1d39c2b1cac4dd02c4c07f18cf9f92d70602834069154719bad`): NYSE `Holidays & Trading Hours` official page (https://www.nyse.com/markets/hours-calendars) — "All NYSE markets observe U.S. holidays as listed below for 2026, 2027, and 2028," with full-closure tables (New Year's Day; Martin Luther King, Jr. Day; Washington's Birthday; Good Friday; Memorial Day; Juneteenth National Independence Day; Independence Day with observed-day shifts; Labor Day; Thanksgiving Day; Christmas Day — nine to ten scheduled full closures per year) plus early-close footnotes (day after Thanksgiving; July 3/Christmas Eve when applicable). The calendar is published years in advance, which is what makes the trigger point-in-time clean.
- Licence and rights: a journal abstract plus an exchange calendar page — this record cites and normalizes the rule (short phrases and the pre-holiday-session notation only) and reproduces no tables, figures, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's pre-holiday-day hold ported to a single crypto asset on completed `1d` bars keyed to the NYSE scheduled-closure calendar — not a lossless reproduction of the paper's CRSP equity backtest. Researcher-declared adaptations are exactly five: (1) close-to-close daily-bar mapping of the paper's pre-holiday trading-day return (P−1 close entry, P close exit, same-bar-close fills — the paper's own close-to-close day construction, not an invented intraday approximation; the hourly-bin shape is fenced, never carried — see Negative evidence 5); (2) single-asset BTCUSDT Binance perpetual (the CRSP equity universe and every equity-level performance claim are fenced off, never carried — see Negative evidence 1); (3) pre-holiday date set taken as the last NYSE trading session before each NYSE-published scheduled full closure (ex-ante known by multi-year publication; one-off mourning closures never qualify — see Signal); (4) fixed 100%-equity single-position sizing with no leverage (the paper ships no sizing rule — see Limitations); (5) an adopted 5-bar warmup flat by record rule plus house fees/funding treatment (the paper reports no costs — see Execution assumptions). The pre-holiday-only scope, the buy-before/sell-at-session-end timing, the long-only posture (the paper documents an upward pre-holiday drift with no short leg — never a short), the unconditional trigger (no return/size/weekday conditioning is traded), and the no-stop time-exit stance are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `preholiday`, `pre.holiday`, `holiday.effect`, `holiday.drift`, `ariel`, `lakonishok`, `cadsby`, `lunar`, `weekend.effect`, `overnight.anomaly` return zero strategy records — a new family in this pool (the only `holiday` prose hits are incidental words in unrelated indicator files). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md` holds the 4-session month-turn window twelve times per year; `santa-claus-rally-yearend-hold-long-btcusdt-1d-2026-10-12.md` holds the single annual December-to-January 7-session window; `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md` holds the six-month seasonal span; `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` holds a weekly weekday session; `january-barometer-conditional-annual-hold-long-btcusdt-1d-2026-10-12.md` holds a full year conditioned on January sign; `fomc-pre-announcement-drift-scheduled-hold-long-btcusdt-1d-2026-10-13.md` holds Fed-scheduled announcement days. Five-axis distinction: no pool record and no open PR holds only the ~9–10 NYSE-scheduled pre-closure sessions per year (P−1-close to P-close) on an external holiday-calendar trigger with no return, indicator, or month/week/year-boundary conditioning.

## Economic mechanism

### Source-reported

Holiday-euphoria anticipation premium: on the single trading session before a market closure, stocks advance with disproportionate frequency and earn mean returns an order of magnitude above ordinary days (9–14x, abstract), concentrating over a third of the 1963–82 market-portfolio total return into eight sessions per year. The paper's hourly examination finds the premium accrues throughout the pre-holiday session rather than in a single edge print, and it subjects the finding to a 1983–86 post-test window (both abstract-pinned; causal attributions and hourly-bin magnitudes live in the paywalled full text and are fenced, never carried).

### Research interpretation

Pure scheduled-event drift-capture with maximum time out of market, long-only. Unlike fixed-calendar holds (ToM/Santa/Monday/January-Barometer) the trigger is an externally published exchange-holiday calendar (~9–10 single sessions per year, ~2–3% of time), so the strategy is flat through essentially the entire tape including whole crises — and equally unprotected against a crash landing on a pre-holiday session. Unlike the FOMC sibling the trigger is a market-closure calendar, not a policy-news calendar, and the held session is the day *before* the closure rather than an announcement day. Unlike return-conditioned monthly systems (TSMOM) there is no formation leg and no losing-signal concept: the position exists if and only if the NYSE calendar says tomorrow the market shuts. Unlike indicator/funding-anchored systems the bet is purely that the documented pre-holiday drift ports to BTCUSDT daily bars, never on a level, band, oscillator, volume, return-sign, or funding anchor. The multi-year advance publication of the closure calendar is what makes the trigger causal: the dates are public before any window opens.

## Signal

Exact rule as pinned (D0 = NYSE scheduled full-closure calendar date (ET); P = calendar date of the last NYSE trading session before D0; entry at the P−1 close; exit at the P close — any other window is a different, unpinned rule):

- Date set (pinned): D0 runs over NYSE scheduled full-market closures as published on the official NYSE holidays page (the nine-to-ten annual U.S. holidays enumerated in Provenance; observed-day shifts as printed, e.g. Friday-observed Independence/Christmas). One-off national-mourning or emergency closures never qualify — the standing scheduled-only precedent. Early-close sessions (day after Thanksgiving, applicable July 3 / Christmas Eve) are trading sessions, never closures: they can serve as P but never as D0.
- Pre-holiday session mapping (pinned): P is the calendar date of the last NYSE trading session strictly before D0 — normally D0−1 (mid-week closures, Good Friday → Thursday, Thanksgiving Thursday → Wednesday); the Friday before a Monday-closure D0 (MLK/Presidents/Memorial/Labor); the Thursday before a Friday-observed D0. Deterministic from the printed calendar; no weekend-shift assumption of our own (the 24/7 tape has no holidays).
- Calendar convention (pinned): bar dates are UTC calendar dates of completed `1d` bars. NYSE dates are ET calendar dates; the mapping uses the ET date printed on the NYSE schedule, evaluated against the UTC bar of the same calendar date — deterministic, no session template.
- Entry long (pinned timing, close-based): at the close of the completed `1d` bar dated P−1 (the calendar day before the pre-holiday session — the paper's buy-before-the-drift timing mapped onto its close-to-close day construction), if flat (always true outside windows by construction), buy 100% equity at that close (same-bar-close fill). Entry predicate from the bar's own date alone: the day after tomorrow is a scheduled NYSE full closure and tomorrow is its last preceding trading session.
- Exit (pinned timing, close-based): at the close of the completed `1d` bar dated P, close the full position at that close. Exit predicate: a position is open and today is the last NYSE trading session before a scheduled full closure. Because entries happen only on P−1 bars and scheduled closures never fall on adjacent calendar days, an open position on a P close is always the matching window position — no pairing ambiguity, disclosed, not missing.
- Separation guarantee (pinned, structural): the entry bar (P−1) and the exit bar (P) are always distinct bars with one session between them, so no bar ever carries both an entry and an exit — no same-bar dual-fire exists to sequence. Consecutive D0 dates never occur in the scheduled annual set, so overlapping windows are structurally impossible.
- Risk legs (pinned posture): no stop, no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing path is the P close. The absence of any stop is the source's posture (the paper ships a session-hold only), disclosed, not invented.
- Direction: long-only (derived pin matching the source, which documents an upward pre-holiday drift with no short leg). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (fills) and bar UTC calendar date (window predicates). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or market-data-feed dependency of any kind.
- One external calendar input, point-in-time clean by construction: the NYSE-published scheduled full-closure dates, published years in advance (2026–2028 on the fetched page) so every year's date set is public before any of that year's windows opens; later calendar additions (e.g. a newly observed holiday) apply only to years whose calendar prints them — never retroactively. No closure reason, statement text, volume, VIX, size-decile, or weekday input enters any rule.
- Single decision grid: completed daily bar, one evaluation per bar. The entry fills on the P−1 bar's own close; the exit lands on the P bar's own close. All inputs are completed-bar values plus the ex-ante-published schedule — no provisional intrabar value, no future reference, no closure outcome is ever used.
- Warmup: 5 completed `1d` bars flat by record rule (window predicates need only the bar's own UTC date plus the pre-published schedule, so the guard is conventional, not structural — mirrors the standing small-guard record-rule precedent). No repainting, no negative shift, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's CRSP equity universe; no cross-venue equivalence claimed).
- Order timing (declared port of the paper's buy-before/sell-at-session-end timing via its close-to-close day construction): completed-bar decision with same-bar-close fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are one market entry per scheduled closure and one close-all per window — at most one order exists on any bar, so there is no same-bar dual-fire whose ordering could change economics. The paper's hourly-bin shape is deliberately not modelled (fenced — see Negative evidence 5).
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — declared derivative (the paper ships no sizing rule). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long-only form is flat ~355 days per year between windows, so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; scheduled-closure windows are disjoint by published-calendar construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any P exit the next P−1 entry fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships the construction adopted here at abstract level: the trading-day-prior-to-holidays scope (nine-to-fourteen-times mean-return multiple), the eight-sessions-per-year concentration (over one third of the 1963–82 market-portfolio total return), the throughout-the-session accrual shape, and the 1983–86 post-test examination. It ships zero adopted performance numbers for this record: every multiple, share, and frequency figure above describes CRSP/U.S. equities, never a BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every multiple, share-of-returns, and frequency figure (9–14x; eight sessions; over one third of 1963–82 return; throughout-the-day shape) belongs to U.S. equities — none transfers to BTCUSDT crypto, whose pre-holiday microstructure (24/7, no halt, no open/close, funding prints inside the window, global non-U.S. participation on U.S. holidays) differs arbitrarily, and none is adopted.
2. Post-publication decay carried as caution: Chong, Hudson & Keasey (2005) document international evidence on the decline and reversal of the pre-holiday anomaly after Ariel (indexing-level only, full text not fetched) — this record adds no persistence guard and claims no post-1986 edge of any kind.
3. Post-test fence: the paper examines 1983–86 pre-holiday returns (abstract-pinned) but the abstract states no direction — no post-test persistence, strengthening, or attenuation claim of any kind is carried.
4. Corroboration fenced, never a rule: the JFQA further-evidence line (NYSE/AMEX/NASDAQ plus U.K./Japanese independence; no size effect in pre-holiday means) is carried only to show the trigger is holiday-specific, not a size/weekday artefact — indexing-level only, never a traded condition.
5. Hourly-bin shape fenced: the throughout-the-day accrual finding is never claimed for the daily port — this record carries only the close-to-close session hold on daily bars.
6. Cost silence fenced: the paper reports no transaction costs — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
7. Fully exposed inside the window: once entered, the position rides the entire adverse excursion with no guardrail — a −20% pre-holiday-session crash is held to the P close by construction. This is the coded trade, disclosed, not a tunable parameter here.
8. Derivation boundary fenced: the only non-paper behavior is the five declared adaptations (close-to-close daily mapping, single asset, published-schedule date set, fixed sizing, warmup + house costs); the pre-holiday-only scope, the buy-before/sell-at-session-end timing, the unconditional trigger, the long-flat posture, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity strategy passes.
9. The scheduled-D0 / P-session / P−1-close entry / P-close exit / unconditional-trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close stance is pinned, not removed: widening the window (e.g. adding the post-holiday session), trading hourly legs, conditioning on size/weekday/past drift, admitting mourning/emergency closures, adding a stop/target/cooldown, re-enabling a short leg, trading partial size, or holding past P would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: scheduled-D0 set / P-session / P−1-close entry / P-close exit / unconditional trigger / single-position long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Window-length relevance: replacing the pinned P-session hold with a two-session hold (P−1-close entry to post-holiday-close exit, adding the session after the closure) must not improve net expectancy; fail ⇒ the post-closure session carries drift the paper's pre-holiday scope does not bind, and the exit pin is doing unacknowledged work.
- F2 — Entry-timing relevance: replacing the pinned P−1-close entry with a post-holiday-only hold (P-close entry to next-close exit, capturing only the session after the closure) must not improve net expectancy; fail ⇒ the pre-holiday session adds nothing over the post-holiday hold.
- F3 — Selectivity relevance: replacing the pinned schedule-only exposure with buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out the ~355 non-pre-holiday days costs more in missed drift than it saves in avoided exposure — or the record's selectivity pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; bar-date predicates plus close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no closures for the rule to skip; NYSE pre-holiday sessions map onto UTC bar dates deterministically (every calendar day is a trading day). Note the structural mismatch, disclosed: the pinned crypto hold spans a full 24-hour UTC day including non-U.S. hours, while the source premium was measured over one U.S. equity session — the port bets on calendar persistence, not on a verified crypto mechanism. Extension to other house-universe assets, windows, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is equities-only across a 1963–86 sample frame; BTCUSDT pre-holiday behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Abstract-level provenance: the paywalled full text was not read end to end (stated access boundary above); every pinned paper fact is abstract-level from the primary publisher record, and all table/figure-level figures are omitted — a reviewer with JSTOR access can verify or tighten the numbers without changing any rule.
- Microstructure mismatch: the source premium accrues over one halt-bounded U.S. equity session; the 24/7 crypto tape has no halt, no open/close, and perverse adjacencies (weekend P−1 bars before Monday-closure windows, funding prints inside the window, global trading through the U.S. closure itself) — the port bets on anticipation-drift persistence, not on a verified crypto mechanism.
- Sample thinness: nine to ten one-session windows per year means even a decade of crypto history yields only ~100 sessions of exposure — statistical power is structurally weak, disclosed, not recovered.
- Close-confirmation lag: the entry fills at the P−1 close and the exit at the P close — gap-through moves across window edges are taken at post-move closes, never at the edge.
- Window rigidity: drift arriving on P−2 or reversing on the post-holiday session is missed or eaten by record rule; a year whose drift fails is held anyway — disclosed, not recovered.
- Warmup cost: the first 5 daily bars are flat by record rule — pinned, not recovered (immaterial at ~10 windows per year, disclosed for completeness).

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Ariel, R. A., *High Stock Returns before Holidays: Existence and Evidence on Possible Causes*, Journal of Finance 45(5) (December 1990): 1611–1626 — pre-holiday-day scope with 9–14x mean-return multiple, eight sessions/year concentration (over one third of 1963–82 market-portfolio return), throughout-the-session accrual, 1983–86 post-test (all abstract-level; table-level figures omitted); RePEc page fetched live 2026-10-13 (12,065 bytes, SHA-256 `7a5e3635…3bb8c0d2`): https://econpapers.repec.org/RePEc:bla:jfinan:v:45:y:1990:i:5:p:1611-26
- DOI landing (bibliographic): https://doi.org/10.1111/j.1540-6261.1990.tb03731.x — https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1990.tb03731.x
- JSTOR stable record (full text restricted to subscribers, per RePEc page): https://www.jstor.org/stable/2328753
- NYSE, *Holidays & Trading Hours* official calendar (scheduled full closures 2026–2028, observed-day shifts, early-close footnotes; fetched live 2026-10-13, 109,229 bytes, SHA-256 `79602f7b…34069154`): https://www.nyse.com/markets/hours-calendars
- Indexing-level corroboration/negative-evidence pointers (landing abstracts only, never fetched, never adopted as rules): `Holiday Effects and Stock Returns: Further Evidence` (JFQA — NYSE/AMEX/NASDAQ plus U.K./Japanese independence, no size effect); Chong, Hudson & Keasey (2005), `Pre-holiday effects: International evidence on the decline and reversal of a stock market anomaly`.
