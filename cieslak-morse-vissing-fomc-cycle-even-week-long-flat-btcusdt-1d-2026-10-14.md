---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Cieslak-Morse-Vissing-Jorgensen FOMC-cycle even-week hold long-flat on BTCUSDT 1d bars
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
  - https://stern.nyu.edu/sites/default/files/assets/documents/cycle_paper_cieslak_morse_vissingjorgensen.pdf
  - https://doi.org/10.1111/jofi.12818
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cieslak-Morse-Vissing-Jorgensen FOMC-cycle even-week hold long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (PDF fetched and verified live 2026-10-14, 859,710 bytes, SHA-256 `c45108b8ab390585452585ed7a8a31484f7defe5928c05c1ac67bc1a278a88`, 70 pages):

- Cieslak, A., Morse, A., Vissing-Jorgensen, A., `Stock Returns over the FOMC Cycle` (first draft April 23, 2014; current draft October 2, 2015; Cieslak — Duke University; Morse — UC Berkeley and NBER; Vissing-Jorgensen — UC Berkeley, NBER and CEPR): https://stern.nyu.edu/sites/default/files/assets/documents/cycle_paper_cieslak_morse_vissingjorgensen.pdf
- Published version (bibliographic, Crossref metadata verified 2026-10-14): Cieslak, Morse & Vissing-Jorgensen, "Stock Returns over the FOMC Cycle," *Journal of Finance* 74(5) (October 2019): 2201–2248, doi:10.1111/jofi.12818.
- Pinned scope (verbatim in sense, §1–§2a): the FOMC cycle starts on the day before a scheduled FOMC announcement day and resets at each of the eight scheduled meetings per year; date 0 is the day of a scheduled FOMC meeting (two-day meetings contribute the second, announcement day); the event-time graph omits weekends and sets return to zero on holidays, so the day axis is trading-day event time.
- Pinned bins (verbatim in sense, §2a/Figure 1): week −1 = days −6 to −2; week 0 = days −1 to 3; week 1 = days 4 to 8; week 2 = days 9 to 13; week 3 = days 14 to 18; week 4 = days 19 to 23; week 5 = days 24 to 28; week 6 = days 29 to 33; days 34+ are dropped (3 days in the 20-year sample, footnote 5).
- Pinned headline estimates (verbatim in sense, §2a–§2b, 160 scheduled meetings 1994–2013, Ken French daily data): 5-day cumulative excess returns average 0.57% (week 0), 0.30% (week 2), 0.42% (week 4), 0.61% (week 6), against ~0% (week −1), −0.17% (week 1), −0.17% (week 3), −0.12% (week 5); daily regression +13.6bp/day in week 0 and +10bp/day in weeks 2/4/6 versus odd weeks, both significant at 1% (Table 1); the entire 20-year equity premium was earned in even weeks.
- Pinned executable (verbatim in sense, §2f/Table 3): "Strategy B" holds stocks in weeks 0, 2, 4, 6 only and stays out in odd weeks — "an easily implementable strategy since FOMC calendars are announced well in advance of a given FOMC cycle and since it could be implemented with very low transactions costs using an existing ETF"; Table 3 rows — A (buy-hold) 8.47/19.99/0.42, B (even-weeks-only) 11.58/13.92/0.83, week-0-only 4.76/9.06/0.53, week-2-only 2.44/6.78/0.36, week-4-only 3.02/6.69/0.45, week-6-only 0.93/1.57/0.59, C (odd-weeks-only) −2.67/15.04/−0.18, D (long-even/short-odd) 14.24/21.78/0.65; verdict: "the most attractive is to simply stay out of the stock market in odd weeks in FOMC cycle time" (Sharpe 0.8, twice the market).
- Pinned supporting facts: bi-weekly pattern robust across 1994–2000/2001–2007/2008–2013 subperiods (Figure 2) and international — EM earns +19bp/day in week 0 and +18bp/day in weeks 2/4/6 with odd weeks at −6.5bp/day (Table 2/Figure 3); VIX-implied premium rises going into even weeks with no realized-volatility pattern (§2e/Figure 4); even-week dummies survive macro-release, reserve-maintenance, day-of-month and day-of-week controls (Table 5); the yearly schedule "is announced ahead of time" (the 2013 schedule was announced in May 2012, §3a); the paper states its bi-weekly finding is novel relative to Lucca-Muench pre-drift (Introduction, footnote 2).
- Licence and rights: a publicly hosted author working draft — this record cites and normalizes the rule (short phrases and the even-week day sets only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's own Strategy B (long even FOMC-cycle weeks, flat odd weeks) ported to a single crypto asset on completed `1d` bars — not a lossless reproduction of the paper's equity backtest. Researcher-declared adaptations are exactly five: (1) weekday-advance event clock with weekend carry — the paper's axis omits weekends, so Monday–Friday UTC bars advance the event-day counter (all weekday bars, including US holidays, per the paper's keep-holidays-on-axis handling) while Saturday/Sunday bars carry Friday's position with no new evaluation, because the paper makes no weekend decisions; (2) single-asset BTCUSDT Binance perpetual (the equity universe and every equity-level performance claim are fenced off, never carried — see Negative evidence 1); (3) scheduled-date set taken as the Federal Reserve's published scheduled-announcement calendar (ex-ante known by the paper's own premise — 2013 schedule out in May 2012; unscheduled/emergency actions never reset the cycle — see Signal); (4) fixed 100%-equity single-position 1× sizing (Strategy B is fully-invested-or-out — source-native sizing, no researcher sizing rule); (5) an adopted 5-bar warmup flat by record rule plus house fees/funding treatment (the paper reports no costs — see Execution assumptions). The scheduled-only scope, the even-week-only exposure, the long-flat posture (the paper's recommended B over short-legged D), the unconditional trigger (no VIX/Board/macro conditioning is traded), and the no-stop week-hold stance are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive searches for `cieslak`, `morse`, `vissing`, `fomc.cycle`, `even.week`, `cycle.week`, `bi.weekly`, `fomc-cycle` return zero strategy records — a new family in this pool (the only `announcement` hit is the Lucca-Moench pre-drift record below, matched on the generic English word). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in window class: `fomc-pre-announcement-drift-scheduled-hold-long-btcusdt-1d-2026-10-13.md` holds one single pre-announcement day per meeting (D−1 close to D0 close); `turn-of-month-4day-hold-long-btcusdt-1d-2026-10-10.md`, `santa-claus-rally-yearend-hold-long-btcusdt-1d-2026-10-12.md`, `sell-in-may-seasonal-hold-long-btcusdt-1d-2026-10-10.md`, `january-barometer-conditional-annual-hold-long-btcusdt-1d-2026-10-12.md` hold fixed month/year-boundary windows; `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md`, `ariel-1987-monthly-half-effect-long-flat-btcusdt-1d-2026-10-14.md`, `lunar-phase-new-moon-regime-long-flat-btcusdt-1d-2026-10-13.md`, `kamstra-kramer-levi-2000-daylight-saving-monday-skip-long-flat-btcusdt-1d-2026-10-14.md`, `pre-holiday-drift-scheduled-preclosure-hold-long-btcusdt-1d-2026-10-13.md` hold weekday/month/moon/DST/holiday grids; `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` and the Hurst-Ooi-Pedersen composite hold on trailing-return signs. Five-axis distinction: no pool record and no open PR holds multi-week even-parity regimes on an event-anchored reset clock (34-day cycle, ~half-time exposure) with no return, indicator, or month/week/year-boundary conditioning.

## Economic mechanism

### Source-reported

Bi-weekly risk premium for news coming from the Federal Reserve: the equity premium accrues in even FOMC-cycle weeks while odd weeks average zero-to-negative, with implied (VIX) volatility elevated going into even weeks but no matching realized-volatility pattern — at least some market participants pay up for protection ahead of even-week news, consistent with a premium, not a statistical accident (§2e). Evidence bundle tying the cycle to the Fed: the irregular FOMC calendar changes across the three robust subperiods; even weeks do not line up with 16,487 Bloomberg macro releases or with corporate earnings (Table 5); fed-funds-market volatility peaks in even weeks; internal Board discount-rate meetings aggregate on a bi-weekly FOMC-cycle rhythm and the cycle is driven by even weeks following Board meetings (Table 7); pre-1994 intermeeting target changes fell disproportionately in even weeks. Ruled out: signalling via open-market operations (per official conversations), premia for public releases/minutes/Beigebooks/statements, speech-frequency alignment, reserve-maintenance-period alignment (Table 5 col 2), leakage as the sole story — systematic informal communication with media/financials is the argued channel (Tables 9–10, §5). Cross-asset: weaker/insignificant for Treasuries (Figure 5), no dollar-exchange-rate tendency; conditioning correlates are explanatory regressions, never traded rules.

### Research interpretation

Event-anchored regime capture with roughly half-time exposure, long-only. Unlike fixed-calendar holds (ToM/Santa/Monday/lunar/DST) the trigger is a published policy-event calendar with an irregular ~6-week reset, so regime boundaries drift across months, weekdays, and holidays by construction — Table 5's day-of-month/day-of-week fixed-effect controls are what make the trigger causal rather than a disguised weekday effect. Unlike the Lucca-Moench pre-drift cousin the exposure is multi-week parity regimes (~4 weeks per cycle) rather than eight single pre-announcement days per year, and unlike return-conditioned monthly systems (TSMOM, HOP composite) there is no formation leg and no losing-signal concept: the position exists if and only if the cycle clock says even week. The bet is purely that the documented bi-weekly Fed-news premium ports to BTCUSDT daily bars, never on a level, band, oscillator, volume, return-sign, or funding anchor.

## Signal

Exact rule as pinned (D0 = scheduled FOMC announcement ET calendar date; two-day meetings contribute the announcement/second day; the cycle resets at each scheduled D0 — unscheduled/emergency/intermeeting actions never reset it, per the paper's 8-per-year scheduled construction and its separate Table 6 treatment of the seven 1994–2013 intermeeting changes):

- Event clock (pinned mapping): event-day `d` advances on Monday–Friday UTC bars only — the paper's axis omits weekends, and holidays stay on-axis, so every weekday bar (including US-holiday weekdays, which print normal crypto bars) advances the counter by one; `d` = weekday bars since the last scheduled D0 with `d(D0 bar) = 0` and the previous weekday bar at `d = −1`. Saturday/Sunday bars carry Friday's position with no evaluation and no orders, because the paper makes no weekend decisions.
- Even set (pinned, trading-day event time, §2a): `E = {−1..3, 9..13, 19..23, 29..33}` — weeks 0, 2, 4, 6. Odd weeks (−1: −6..−2; 1: 4..8; 3: 14..18; 5: 24..28) and days `d ≥ 34` (the paper drops week 7+) are flat by record rule.
- Entry long (pinned timing, close-based): at the close of a weekday bar whose `d ∈ E`, if flat, buy 100% equity at that close (same-bar-close fill). Entry predicate from the bar's own UTC date plus the pre-published schedule alone.
- Exit (pinned timing, close-based): at the close of a weekday bar whose `d ∉ E` (first odd-week bar or `d ≥ 34`), if long, close the full position at that close. Because even/odd partition every weekday bar, an open position on an exit bar is always the matching regime position — no pairing ambiguity, disclosed, not missing.
- Separation guarantee (pinned, structural): the even/odd partition means no bar ever carries both an entry and an exit — no same-bar dual-fire exists to sequence; at most one state-change order exists on any bar. Weekend bars carry no orders by construction.
- Risk legs (pinned posture): no stop, no target, no trailing, no opposite-signal exit (no short side exists to signal against); the sole position-closing path is the first non-even weekday close. The absence of any stop is the source's posture (Strategy B holds full weeks), disclosed, not invented.
- Direction: long-only (derived pin matching the source, whose recommended Strategy B stays out of odd weeks rather than shorting them — Strategy D's short leg is fenced, never carried). The futures venue is still pinned as the research market (house overlay) with the short permission simply unused; a spot-only deployment expresses the identical event set.
- Sizing: fixed 100%-equity single position, 1×, no adds (Strategy B is fully-invested-or-out — source-native sizing, no researcher sizing rule).

## Required data

- Completed `1d` bars of BTCUSDT only: `close` (fills), bar UTC calendar date, and its Monday–Friday versus Saturday/Sunday predicate (clock advance/carry). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, release-time, statement-text, decision-outcome, surprise, VIX, yield-curve, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or market-data-feed dependency of any kind.
- One external calendar input, point-in-time clean by construction: the Federal Reserve's published scheduled-FOMC-announcement dates, known to investors in advance per the paper's §3a premise (the schedule for a year is public before any of that year's cycles opens — 2013 precedent: announced May 2012). No announcement outcome ever enters any rule.
- Single decision grid: completed daily bar, one evaluation per weekday bar at its close; weekend bars carry with no evaluation. All inputs are completed-bar values plus the ex-ante-published schedule — no provisional intrabar value, no future reference, no meeting outcome is ever used.
- Warmup: 5 completed `1d` bars flat by record rule (before the first schedulable cycle is establishable the clock is undefined, so the guard is structural at sample start and conventional thereafter — mirrors the standing small-guard record-rule precedent). No repainting, no negative shift, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's equity universe; no cross-venue equivalence claimed).
- Order timing (declared port of the paper's hold-in-even-weeks Strategy B): completed-bar decision with same-bar-close fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: regime edges are the only order source — at most one state-change order exists on any bar, so there is no same-bar dual-fire whose ordering could change economics. The paper's 2pm/intraday legs are deliberately not modelled (no intraday timing is claimed for the daily port).
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity — source-native (Strategy B fully-in-or-out). Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — the long leg is exposed through weekends it carries and across full even weeks, so it is a genuine funding payer when long). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; even/odd weeks partition the clock by published-schedule construction, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any odd-week exit the next even-week entry fires on schedule (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships the full construction adopted here: the scheduled-meetings-only scope (8 per year, §1–§3a), the even-week day sets in trading-day event time (week 0 = −1..3 through week 6 = 29..33, §2a/Figure 1), the Strategy B executable (long even weeks, flat odd weeks, §2f/Table 3, Sharpe 0.83 versus 0.42 buy-hold, with the paper's own verdict that staying out of odd weeks is the most attractive simple strategy), the long-with-cash-otherwise posture (short-legged Strategy D rejected on Sharpe despite a higher mean), the ex-ante implementability premise (calendars announced well in advance, ETF-implementable at very low transactions costs), the unconditional trigger (no VIX/Board/macro conditioning traded), and the equity-only statistics — 0.57/0.30/0.42/0.61% even-week 5-day means, ~0/−0.17/−0.17/−0.12% odd-week means, +13.6/+10bp/day regression differentials at 1%, Table 3 rows A 8.47/19.99/0.42 · B 11.58/13.92/0.83 · C −2.67/15.04/−0.18 · D 14.24/21.78/0.65, 160 meetings 1994–2013, three robust subperiods, EM +19/+18bp/day even with −6.5bp/day odd. It ships zero adopted performance numbers for this record: every basis-point, share, and Sharpe figure above describes 1994–2013 equities, never a BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Equity-only evidence fenced: every basis-point, regression-coefficient, hit-pattern, and Sharpe figure (0.57/0.30/0.42/0.61%; ~0/−0.17/−0.17/−0.12%; +13.6/+10bp/day; A/B/C/D Table 3 rows; EM +19/+18/−6.5bp/day) belongs to 1994–2013 equities — none transfers to BTCUSDT crypto, whose FOMC-week microstructure (24/7, no open/close, funding, weekend-carried exposure) differs arbitrarily, and none is adopted.
2. Sample-end fence: the paper's return sample ends 2013 (160 meetings, 1994–2013); no post-2013 persistence, decay, or regime claim of any kind is carried — this record adds no out-of-sample guard and claims no persistence.
3. Week-6 thinness fenced: the paper's own Figure 1B shows data points dropping off past week 4, and the week-6-only leg (0.93/1.57/0.59) contributes least to Strategy B — the week-6 leg is carried as pinned Strategy-B definition, never re-optimized or dropped.
4. Days `d ≥ 34` fenced: 3 such days are dropped in the paper; this record pins them flat — disclosed unevidenced region, never traded, never interpolated.
5. Weekend-carry adaptation fenced: the paper has no weekend concept (axis omits weekends); carrying Friday's position through Saturday/Sunday bars is the declared 24/7 mapping, and weekend-session exposure is unevidenced by the source — disclosed, not recovered.
6. Conditioning/mechanism regressions fenced: VIX-predictability (§2e), Board-meeting driver (Table 7), leak evidence (Tables 9–10), reserve-maintenance and macro-release and day-of-month/weekday controls (Table 5), bond/carry cross-asset results (Figure 5) are explanatory, never traded here — adding any of them would be a different, unpinned rule.
7. Cost silence fenced: the paper reports no transaction costs (its "very low transactions costs using an existing ETF" remark is qualitative and is never converted into a number) — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
8. Fully exposed inside even weeks: once entered, the position rides the entire adverse excursion with no guardrail — a −20% even-week crash is held to the week's end by construction. This is the coded trade, disclosed, not a tunable parameter here.
9. Derivation boundary fenced: the only non-paper behaviors are the five declared adaptations (weekday-advance clock with weekend carry, single asset, published-schedule date set, fixed sizing, warmup + house costs); the scheduled-only scope, the even-week-only exposure, the unconditional trigger, the long-flat posture, and the no-stop stance are source-faithful. This record is therefore never evidence that the paper's equity strategy passes.
10. The even-week set / weekday clock / scheduled-only reset / single-position long-flat / `1d` BTCUSDT / same-bar-close stance is pinned, not removed: narrowing to week-0-only, widening to buy-hold, shorting odd weeks, conditioning on VIX/Board/macro days, admitting unscheduled meetings, adding a stop/target/cooldown, trading partial size or leverage, or re-evaluating on weekend bars would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: even-week set / weekday-advance clock / scheduled-only reset / single-position long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Selectivity relevance: replacing the pinned even-week-only hold with buy-and-hold over the same sample must not improve net expectancy; fail ⇒ the paper's A-vs-B selectivity contrast does not bind the crypto port and the even-week pin is doing unacknowledged work.
- F2 — Full-set relevance: replacing the pinned four-leg even set with a week-0-only hold (the Lucca-Moench-overlapping leg) must not improve net expectancy; fail ⇒ weeks 2/4/6 add nothing over the announcement-week leg in crypto and the full-set pin is doing unacknowledged work.
- F3 — Short-leg relevance: adding the paper's Strategy D short leg in odd weeks must not improve risk-adjusted expectancy; fail ⇒ the odd-week short carries risk-adjusted value in crypto and the long-flat pin is doing unacknowledged work.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid completed `1d` bars; weekday predicate plus close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no intraday session template, no cross-venue state. The 24/7 crypto market has no holidays for the clock to skip: every Monday–Friday UTC bar advances the event counter (matching the paper's keep-holidays-on-axis handling) and Saturday/Sunday bars carry Friday's state with no evaluation (matching the paper's weekend omission). FOMC announcement dates map onto UTC bar dates deterministically (every calendar day is a trading day). Extension to other house-universe assets, windows, clocks, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is US (and cited international) equities over 1994–2013; BTCUSDT even-week behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Microstructure mismatch: the paper's bins are equity close-to-close trading-day blocks around a 2pm ET release with weekend halts; the 24/7 crypto tape has no halt, no open/close, and weekend-carried exposure — the D0 bar's close exit always follows the release but also always *includes* post-release hours the paper never isolates, and Saturday/Sunday exposure exists only by the carry mapping — disclosed, not recovered.
- Holiday advance: US-holiday weekday bars advance the clock and trade here, while the paper's holiday bars sit on-axis at zero equity return — a crypto bar that moves on Thanksgiving shifts subsequent bin alignment versus the paper — disclosed, not recovered.
- Sample thinness of the outer leg: week 6 rests on few data points by the paper's own Figure 1B; a decade of crypto history yields on the order of eighty even-week regimes with the week-6 leg sparsest — statistical power is structurally modest, disclosed, not recovered.
- Close-confirmation lag: entries fill at regime-edge weekday closes and exits at the first non-even weekday close — gap-through moves across edges are taken at post-move closes, never at the edge.
- Regime rigidity: odd-week rallies are missed and even-week crashes are held in full by record rule; an FOMC cycle whose premium fails per the paper's own odd/even dispersion is held anyway — disclosed, not recovered.
- Warmup cost: the first 5 daily bars are flat by record rule — pinned, not recovered (immaterial at ~half-time exposure, disclosed for completeness).

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Cieslak, A., Morse, A., Vissing-Jorgensen, A., `Stock Returns over the FOMC Cycle` (working draft, first draft April 23, 2014; current draft October 2, 2015) — cycle definition and reset (§1–§2a), even-week day sets and headline estimates with Figure 1/Table 1, Strategy B/C/D executables with Table 3, subperiod/international/VIX evidence (§2c–§2e, Figure 2–4, Table 2), Fed-tie evidence and ruled-out channels (§3–§5, Tables 5–10); PDF verified live 2026-10-14 (859,710 bytes, SHA-256 `c45108b8ab390585452585ed7a8a31484f7defe5928c05c1ac67bc1a278a88`): https://stern.nyu.edu/sites/default/files/assets/documents/cycle_paper_cieslak_morse_vissingjorgensen.pdf
- Published-version lineage (Crossref metadata verified 2026-10-14): *Journal of Finance* 74(5), October 2019, 2201–2248: https://doi.org/10.1111/jofi.12818
