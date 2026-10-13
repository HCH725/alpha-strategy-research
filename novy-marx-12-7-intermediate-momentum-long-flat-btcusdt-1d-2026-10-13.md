---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Novy-Marx 2012 intermediate 12-7 momentum monthly long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2012-03-01
sources:
  - https://ideas.repec.org/a/eee/jfinec/v103y2012i3p429-453.html
  - https://doi.org/10.1016/j.jfineco.2011.05.003
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Novy-Marx 2012 intermediate 12-7 momentum monthly long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (RePEc canonical record fetched and read 2026-10-13; full-text methods verified against a text-layer mirror the same day):

- Novy-Marx, Robert, `Is momentum really momentum?` — Journal of Financial Economics, vol. 103, issue 3, 429–453 (2012). DOI `10.1016/j.jfineco.2011.05.003`; RePEc handle `RePEc:eee:jfinec:v:103:y:2012:i:3:p:429-453`. Canonical record: https://ideas.repec.org/a/eee/jfinec/v103y2012i3p429-453.html (`Novy-Marx, Robert, 2012. "Is momentum really momentum?," Journal of Financial Economics, Elsevier, vol. 103(3), pages 429-453`).
- Pinned headline spec (publisher Abstract, read verbatim on the RePEc record): `Momentum is primarily driven by firms' performance 12 to seven months prior to portfolio formation, not by a tendency of rising and falling stocks to keep rising and falling.` / `Strategies based on recent past performance generate positive returns but are less profitable than those based on intermediate horizon past performance, especially among the largest, most liquid stocks.` / `Similar results hold for momentum strategies trading international equity indices, commodities, and currencies.` Sample window adopted at section level only (data §2.1: CRSP universe January 1926–December 2008; strategy sample January 1927–December 2008).
- Pinned construction facts (full-text §§2–2.1, read verbatim): `Momentum strategies are constructed each month by buying winners and selling losers, where these are defined as the upper and lower decile, by NYSE breaks, of cumulative returns over a test period.` / `The n-m strategy is based on portfolios sorted on r[n;m], denoting cumulative returns from n to m months (inclusive) prior to portfolio formation. The n-m strategy and its return series are both denoted MOM[n;m].` / `I fix the holding period at one month to keep the number of strategies under consideration manageable.` The headline test pair is `MOM12;7` (intermediate, months −12 to −7) versus `MOM6;2` (recent, months −6 to −2): `MOM12;7 generates 1.21% per month, while MOM6;2 generates 0.79% per month` (Table 2, value-weighted, portfolio-level claim — fenced, never adopted here). The large-cap illustration (`the top (bottom) quintile of performers over the period 12 to seven months prior to portfolio formation, generated average returns of almost 10% per year from January 1927 through December 2008`) is likewise portfolio-level and fenced.
- Access boundary (stated on the RePEc record, disclosed, not worked around): `Full text for ScienceDirect subscribers only` — the publisher full text was therefore NOT taken from ScienceDirect; section-level methods above were verified in a public text-layer mirror of the same paper (identical title/authors/journal/DOI/abstract block verified in-text). No table, figure, or regression beyond the quoted construction facts and the two fenced headline numbers is cited anywhere in this record.
- Licence and rights: the paper is a published Elsevier journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's intermediate-horizon `MOM12;7` winner leg ported to one crypto asset as a monthly long-or-flat hold — not a lossless reproduction of the paper's cross-sectional decile-spread study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance perpetual (the NYSE-break decile cross-section, the winner-minus-loser spread, the Fama-MacBeth regressions, and every portfolio-level performance claim are fenced off, never carried — see Negative evidence 1); (2) formation fixed to the cumulative 6-calendar-month close-to-close simple return over months T−11..T−6 at a month-T-end decision (the paper's `r12;7` inclusive-cumulative six-month window ported to calendar months — the bare-close definition with no distributions is the declared port, BTC pays none); (3) long-flat direction mapping on the strict formation sign (the paper's long-short spread leg is fenced; the short permission is simply unused — see Signal); (4) calendar-month decision grid on completed `1d` closes with next-open fills (the paper fixes a one-month holding cadence but ships no executable fill convention, so the causal port is declared, never implied); (5) an adopted twelve-full-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's cost-free CRSP accounting; (6) fixed 100%-equity single-position sizing with no leverage (the paper holds value-weighted decile portfolios, never a single-asset book). The 12-to-7 lagged six-month formation, the skipped six most-recent months, the one-month holding, the strict sign rule, the monthly update, and the no-stop/no-target/no-trailing posture (signal-roll exits only) are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `novy-marx`, `novy marx`, `really momentum`, `MOM12`, `r12;7`, `intermediate horizon` return zero strategy records in the main tree. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` conditions its monthly hold on the sign of the trailing 12-month cumulative return ending at the decision month with no skip (that record's own Falsification F2 names the `ending one month before the decision bar` skip as an unpinned variant — a one-month skip, never a six-month echo window); `jegadeesh-1990-monthly-reversal-long-flat-btcusdt-1d-2026-10-13.md` inverts the sign of a 1-month formation (a 1-month reversal leg, opposite mapping and one-sixth the formation of this record); `lehmann-1990-weekly-reversal-long-flat-btcusdt-1d-2026-10-13.md` trades a weekly grid, never a lagged multi-month formation; `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` compares a price level against its own 10-month average — a level comparison with no return-ratio sign and no skipped window anywhere; the calendar holds (`sell-in-may`, `january-barometer`, `monday-drift`, `turn-of-month-4day`, `pre-holiday-drift`, `fomc-pre-announcement-drift`, `lunar-phase-new-moon-regime`) carry no price-conditioned leg at all. Five-axis distinction: no pool record and no open PR holds next month long-or-flat on the sign of a lagged intermediate formation that deliberately ignores the six most recent months.

## Economic mechanism

### Source-reported

Momentum-with-an-echo, not short-run autocorrelation: what predicts next-month returns is not recent rising/falling but performance 12 to seven months prior — `intermediate horizon past performance, measured over the period from 12 to seven months prior, seems to better predict average returns than does recent past performance` (§3 lead, mechanism framing fenced to the paper's 1927–2008 equity sample, never adopted as a crypto claim here). The paper monetizes the pattern as a value-weighted winner-minus-loser spread of 1.21 percent per month for `MOM12;7` versus 0.79 percent for `MOM6;2` (Table 2 — spread-level claim, fenced, never adopted here).

### Research interpretation

Slow-echo trend port: the six-month formation lagged by six months acts as a band-pass filter that only lets drift old enough to have survived half a year of tape trigger exposure, while the monthly hold with no intra-month trading makes whipsaws structurally impossible inside the holding month — the strategy can be six months stale but can never chase last month's candle. Unlike trailing momentum (TSMOM) the freshest half-year of returns is unread by construction: a vertical six-month rally followed by nothing still prints flat if the lagged window is red. Unlike one-month reversal (Jegadeesh) the mapping is same-signed and the window is six times longer and six months older. Unlike moving-average regimes (Faber) there is no average anywhere: the signal is a bare lagged cumulative-return sign. The bet, as derived, is purely on the paper's intermediate-horizon leg surviving the port to BTCUSDT at monthly cadence, never on a level, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (lagged 6-month formation, 6-month skip, strict sign, monthly grid — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in calendar month T (month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- Formation (pinned): `R_T = C_{T−6} / C_{T−12} − 1` (simple cumulative close-to-close return, closes only — `C_{T−6}` is the close of the last completed daily bar dated in month T−6 and `C_{T−12}` the close of the last completed daily bar dated in month T−12; this compounds exactly the six calendar-month returns of months T−11..T−6, i.e. the paper's `r12;7` window relative to holding month T+1; no log/simple choice left open, no dividend or distribution adjustment exists for BTC).
- Skip (pinned, not a parameter): the six most recent completed months T−5..T are never read for any reason — this is the paper's echo logic (the `r6;2`-plus-skip-month exclusion), not a tunable lookback.
- Position target for calendar month T+1 (pinned, strict): `R_T > 0` → long; `R_T <= 0` → flat (the equality leg is pinned to flat — measure-zero on live tape, no tie semantics beyond this; the paper's spread is long-short across deciles and the short leg is fenced by declared adaptation (3)).
- Orders (pinned): at most one order event per month, placed for the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port; the paper ships no fill convention): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside month T+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next month-end signal mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-month exit; a month-long adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` closes of BTCUSDT only: two month-end closes per decision (`C_{T−6}` and `C_{T−12}`; no `open` except as fill price, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: calendar month. One evaluation per month on the last completed daily bar of the month; fills land on the next daily bar's open (first open of the new month). All formation inputs are completed-bar closes — no provisional month-end value is ever used.
- Warmup: twelve full calendar months of `1d` bars before the first decision (both month-end closes must exist). Bars before the first decidable month-end are flat by record rule; no signal before the thirteenth calendar month's first open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's fixed one-month holding cadence): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per month, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long months carry realized funding, flat months carry none, and the form holds genuine flat months so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat month needs only the next positive lagged-formation sign (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: monthly formation of winner-minus-loser decile spreads on cumulative test-period returns (§2.1), the `r[n;m]` inclusive-cumulative notation with the `MOM[n;m]` strategy label (§2.1), the fixed one-month holding period (§2 lead), and the headline 12-to-7-months-prior driver (Abstract). It ships zero adopted performance numbers for this record: the 1.21%/0.79% spreads and the ~10%/year large-cap illustration describe the paper's equity decile study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every headline result (decile sorts, NYSE breaks, value-weighting, Fama-MacBeth regressions, factor spanning tests, the 1.21/0.79 spreads) belongs to a cross-sectional equity study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Full-text access boundary: the publisher full text sits behind a ScienceDirect-subscriber restriction and was not taken from the publisher; section-level methods were verified in a public text-layer mirror of the identical paper, disclosed as this record's evidence ceiling — any table-level dispute beyond the quoted construction facts is decided against this record, never patched by inference.
3. No crypto sample anywhere: no 1927–2008 equity evidence speaks to BTCUSDT behavior; single-asset crypto echo-momentum is unevidenced by the source and may differ arbitrarily. The six-month skip can sit out a roaring one-way bull tape for half a year by construction (flat while the lagged window digests old red months).
4. Cost silence fenced: the paper's spreads are cost-free returns, not net-of-cost tradable P&L — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
5. Recent-leg admission: the same paper documents that recent past performance also generates positive (if smaller) returns — a green last-six-months backdrop paired with a red lagged window is followed unconditionally here (flat), disclosed, not hedged.
6. Bare-sign simplification: the paper sorts break-pointed cross-sections into winner/loser tails; this record trades the bare single-asset formation sign. Any conditioning information in the paper's distributional sort is discarded by declared derivation, not silently carried.
7. Monthly latency doubled by the skip: the grid can only react at month-end to information already six months old; a fresh regime break is missed for half a year by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: lagged 6-month formation T−11..T−6 / 6-month skip / strict `>0`-long-else-flat / month-end decision / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Skip relevance: replacing the pinned lagged formation with the trailing 6-month formation over months T−5..T (same sign, same grid, no skip) must not improve net expectancy; fail ⇒ the paper's echo/skip logic carries no advantage over fresh momentum on the same tape.
- F2 — Window-length relevance: replacing the pinned 6-month lagged formation with the trailing 12-month formation (TSMOM-style, same grid) must not improve net expectancy; fail ⇒ the intermediate window carries no advantage over the plain 12-month leg.
- F3 — Direction-twin relevance: the contrarian-signed twin on the identical lagged grid (long iff `R_T <= 0`, flat otherwise) must not outperform the pinned same-signed mapping; fail ⇒ the intermediate-momentum leg does not survive the port and the record's sign is doing negative work.
- F4 — Full-size relevance: replacing fixed 100%-equity sizing with fixed 50%-equity sizing must not improve risk-adjusted expectancy; fail ⇒ the declared size pin is doing unacknowledged work — or the record's size choice is arbitrary leverage in disguise.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid calendar-month on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets or lookbacks would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across individual equities; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Bare-sign simplification: the paper buys/sells break-pointed decile tails; this record trades the bare formation-month sign. Any distributional information in the paper's sort is discarded by declared derivation, not silently carried.
- Cash without yield: flat months earn nothing here while neither paper leg accrues cash yield either — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper fixes a one-month holding cadence with no fill convention; this record fills next open. On gapping month boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is weeks away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Stale-signal latency: the formation window ends six months before the holding month; fresh information is structurally ignored for half a year — pinned, not recovered.
- Warmup cost: the first twelve calendar months are flat by record rule, so any textbook echo completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- https://ideas.repec.org/a/eee/jfinec/v103y2012i3p429-453.html
- https://doi.org/10.1016/j.jfineco.2011.05.003
