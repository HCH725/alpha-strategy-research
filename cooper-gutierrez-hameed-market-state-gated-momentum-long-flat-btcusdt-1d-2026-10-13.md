---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Cooper-Gutierrez-Hameed 2004 market-state-gated six-month momentum long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2004-06-01
sources:
  - https://doi.org/10.1111/j.1540-6261.2004.00665.x
  - https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2004.00665.x
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=299927
  - https://eccles.utah.edu/news/document/market-states-and-momentum
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cooper-Gutierrez-Hameed 2004 market-state-gated six-month momentum long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref metadata, publisher landing, and university abstract page read 2026-10-13):

- Cooper, Michael J. & Gutierrez, Roberto C. Jr. & Hameed, Allaudeen, `Market States and Momentum` — Journal of Finance, vol. 59, no. 3, 1345–1365 (June 2004). DOI `10.1111/j.1540-6261.2004.00665.x`; SSRN abstract `299927`. Crossref record pins title `Market States and Momentum`, container `The Journal of Finance`, volume `59`, issue `3`, pages `1345-1365`, authors Cooper / Gutierrez / Hameed. (Publisher affiliations: Purdue, Oregon, NUS.)
- Pinned headline spec (publisher/SSRN/university Abstract, read verbatim): `We test overreaction theories of short-run momentum and long-run reversal in the cross section of stock returns. Momentum profits depend on the state of the market, as predicted. From 1929 to 1995, the mean monthly momentum profit following positive market returns is 0.93%, whereas the mean profit following negative market returns is −0.37%. The up-market momentum reverses in the long-run. Our results are robust to the conditioning information in macroeconomic factors. Moreover, we find that macroeconomic factors are unable to explain momentum profits after simple methodological adjustments to take account of microstructure concerns.`
- Pinned construction facts (full-text excerpts, read verbatim): the state clock is the lagged three-year / `36-month` market return (`Average Monthly Profits Following 36-month UP Markets`, Figure 1 `six-month momentum strategy from 1929:01 to 1995:12 following three-year UP markets and three-year DOWN markets`, cumulative event-time `months t + 1 to t + 60`); the momentum leg is a six-month formation (`six-month returns (from t − 5 to t, including month t)`); headline Table I cells `Months 1-6` UP `N 674 / Mean profit 0.93 / (t-statistic) (8.41)` vs DOWN `N 124 / Mean profit -0.37 / (t-statistic) (-0.65)`, `Months 1-12` UP `0.72 (9.43)` vs DOWN `-0.50 (-1.44)`, `Months 13-60` UP `-0.36 (-3.23)` vs DOWN `-0.67 (-3.19)`; CAPM alpha UP `1.12 (9.84)` vs DOWN `0.01 (0.03)`; Fama-French alpha UP `1.28 (10.80)` vs DOWN `0.64 (1.44)`; equality Panel C `(2.26)` raw / `(2.22)` CAPM for the 6/6 leg. The microstructure adjustments are a `$1` price screen and `skipping of the month between the formation period and the holding period`; the recursive out-of-sample finding is that `the lagged return on the market` predicts the momentum-profit time series while the macro multifactor model does not.
- State-sign corroboration (secondary literature summary, disclosed as secondary): the UP/DOWN cut is `UP when the lagged three-year market return is non-negative and DOWN when it is negative`, with U.S. momentum returns `exclusively` following UP markets. This record pins the zero cut from that corroboration plus the primary Abstract's positive/negative phrasing; the exact-zero print is pinned to UP (measure-zero on live tape, disclosed in Signal).
- Access boundary (disclosed, not worked around): the publisher full text sits behind subscription walls; abstract-level facts were verified on the publisher landing and a university page, construction/table facts in full-text excerpts of the identical paper (identical title/authors/journal/vol/pages block verified in-text). No table cell beyond the quoted numbers is cited anywhere in this record.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's 36-month-state-gated six-month momentum winner leg ported to one crypto asset as a monthly-redecided long-or-flat hold — not a lossless reproduction of the paper's cross-sectional decile-spread study. Researcher-declared adaptations are exactly seven: (1) single-asset BTCUSDT Binance perpetual (the CRSP cross-section, the winner-minus-loser zero-cost spread, the overlapping event-time sleeves, and every portfolio-level profit/alpha/t-statistic claim are fenced off, never carried — see Negative evidence 1); (2) self-state proxy: the asset's own trailing 36-calendar-month cumulative simple return replaces the paper's diversified-market (CRSP value-weighted) lagged three-year return — there is no market index on a single-asset tape, so the UP `>= 0` / DOWN `< 0` cut is applied to BTC's own 36-month print (the central declared invention — see Signal and Limitations); (3) formation fixed to the cumulative 6-calendar-month close-to-close simple return over months T−5..T with no skip (the paper's `(from t − 5 to t, including month t)` pin; the paper's skip-a-month and $1-screen microstructure variants are fenced, never read); (4) long-flat direction mapping on the joint gate (UP-state AND positive formation → long, anything else → flat; the paper's short leg and any DOWN-state momentum are fenced — see Signal); (5) sequential non-overlapping 1-calendar-month holding sleeves re-decided every month-end with next-open fills (the paper holds overlapping cohorts in event time; the derived port holds one sleeve per month so single-position state stays explicit — a material event-timing change, declared here, never implied); (6) an adopted thirty-six-full-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's cost-free CRSP accounting; (7) fixed 100%-equity single-position sizing with no leverage (the paper holds equally weighted cross-sectional portfolios, never a single-asset book). The 36-month state window, the zero state cut, the 6-month formation, the same-signed winner mapping, and the no-stop/no-target/no-trailing posture (signal-roll exits only) are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `cooper`, `gutierrez`, `hameed`, `market-state`, `three-year`, `UP-market` return no strategy record in the main tree — the only hits are mechanism-unrelated fragments (the De Bondt-Thaler record's own 36-month contrarian formation, one Heikin-Ashi record's `trend-state` filename token, citation prose in the Liu-Tsyvinski and Heston-Sadka records). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md` trades the same 6-month formation unconditionally on sequential 6-month blocks with no state read anywhere (this record adds the 36-month UP gate, re-decides monthly, and holds one month at a time); `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md` reads a lagged echo formation that deliberately ignores recent months with no regime gate (opposite recency handling, no state cut); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds on the bare 12-month sign with no second condition (single-input rule, twice the formation, no gate); `debondt-thaler-36m-overreaction-long-flat-btcusdt-1d-2026-10-13.md` maps a 36-month read contrarianly on 36-month blocks (inverted mapping, thirty-six times the holding, and its 36-month input is the signal where this record's 36-month input is only the gate); `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` compares a price level against its own 10-month average (a level comparison with no return-sign anywhere); `moreira-muir-volatility-managed-long-only-btcusdt-1d-2026-10-13.md` scales size by inverse variance (a sizing ruler, no formation sign, no state cut); the calendar holds carry no price-conditioned leg at all. Five-axis distinction: no pool record and no open PR conditions a six-month continuation leg on a trailing 36-month state cut with monthly re-decision and one-month sequential holds.

## Economic mechanism

### Source-reported

Overreaction-gated continuation, not unconditional momentum: `Momentum profits depend on the state of the market, as predicted` by overreaction theories — after three-year UP markets the six-month winner-minus-loser leg earns `0.93%` per month (`t 8.41`, CAPM alpha `1.12`), after three-year DOWN markets it earns `-0.37%` (`t -0.65`, CAPM alpha `0.01`), samples `1929 to 1995`; `The up-market momentum reverses in the long-run` (months 13–60 UP `-0.36`, DOWN `-0.67`). Macroeconomic factors (dividend yield, default/term spreads, T-bill) do not capture the asymmetry once microstructure adjustments apply, and the lagged market return — not the macro model — forecasts the momentum-profit time series out of sample. (All mechanism framing fenced to the paper's 1929–1995 equity sample, never adopted as a crypto claim here.)

### Research interpretation

State-gated drift sensor: the 36-month self-state print acts as a slow permission switch that only lets a sustained three-year advance arm the book, while the 6-month formation ending at the same month-end acts as the trigger that fires only when the fresh half-year also points up — both legs must agree at the same close or the next month stays flat, so chop, single-month spikes, and whole DOWN-state stretches print nothing but flat months. Unlike unconditional momentum (JT-6/6) the book can sit out a screaming 6-month rally when the three-year state reads DOWN. Unlike echo momentum (Novy-Marx) the freshest months are fully read — a vertical half-year rally after a long base prints long immediately. Unlike long-horizon reversal (De Bondt-Thaler) the 36-month read is a gate, never the signal, and the mapping is same-signed. Unlike average-regimes (Faber) there is no average anywhere: both inputs are bare cumulative-return signs. The bet, as derived, is purely on the paper's UP-gated winner leg surviving the port to BTCUSDT at monthly cadence with the asset's own print standing in for the market, never on a level, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (36-month self-state cut at zero, 6-month formation including recent months, no skip, strict joint gate, 1-month sequential sleeves — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in calendar month T (month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- State (pinned): `S_T = C_T / C_{T−36} − 1` (simple cumulative close-to-close return; `C_T` is the close of the last completed daily bar dated in month T and `C_{T−36}` the close of the last completed daily bar dated in month T−36; this compounds exactly the 36 calendar-month returns of months T−35..T, i.e. the paper's lagged three-year market return ported to the asset's own print). UP iff `S_T >= 0` (the equality leg is pinned to UP — measure-zero on live tape, no tie semantics beyond this; the paper's DOWN cut `< 0` maps to not-UP here).
- Formation (pinned): `R_T = C_T / C_{T−6} − 1` (simple cumulative close-to-close return over months T−5..T, i.e. the paper's `from t − 5 to t, including month t` pin; no log/simple choice left open, no dividend or distribution adjustment exists for BTC).
- Skip (pinned, not a parameter): none — this record adopts the representative no-skip read; the paper's skip-a-month and $1-screen microstructure variants are fenced, never read.
- Position target for calendar month T+1 (pinned, strict joint gate): (`S_T >= 0` AND `R_T > 0`) → long; anything else → flat (`R_T = 0` pins to flat — measure-zero, no second rule).
- Orders (pinned): at most one order event per month boundary, placed for the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port; the paper forms overlapping event-time cohorts with no executable fill convention, so the sequential next-open fill is declared, never implied): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside month T+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next month-end joint gate mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-month exit; a DOWN-state whipsaw month or a gated-out rally is absorbed exactly as printed by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` closes of BTCUSDT only: two month-end closes per decision (`C_T`, `C_{T−6}`, `C_{T−36}`; no `open` except as fill price, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: calendar months. One evaluation per month on the last completed daily bar of the month; fills land on the next daily bar's open (first open of month T+1). All state and formation inputs are completed-bar closes — no provisional month-end value is ever used.
- Warmup: thirty-six full calendar months of `1d` bars before the first decision (all three month-end closes must exist). Bars before the first decidable month-end are flat by record rule; no signal before the thirty-seventh calendar month's first open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's formation-time cohort starts): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per month boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long months carry realized funding, flat months carry none, and the form holds genuine flat months so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat month needs only the next UP-and-positive joint print (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping cohorts (the paper's overlapping event-time sleeves are replaced by the declared sequential single sleeve — see Limitations). The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: the lagged three-year / 36-month UP-vs-DOWN state clock (Table I title, Figure 1 caption, event-time months t+1..t+60, sample `1929:01 to 1995:12`), the six-month formation read (`from t − 5 to t, including month t`), the UP `0.93 (8.41)` / DOWN `-0.37 (-0.65)` asymmetry with CAPM `1.12 / 0.01` and FF `1.28 / 0.64` alphas and equality t-stats `(2.26)` raw / `(2.22)` CAPM on the 6/6 leg, the long-run reversal legs (13–60 UP `-0.36`, DOWN `-0.67`), the skip-month/$1-screen microstructure adjustments, and the recursive out-of-sample lagged-market-return forecast result. It ships zero adopted performance numbers for this record: the 0.93/−0.37 spreads, every alpha, and every t-statistic describe the paper's equity decile study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every headline result (decile sorts, equal weighting, winner-minus-loser spreads, CAPM/FF spanning, macro-model horse race, the UP `N 674` vs DOWN `N 124` month counts) belongs to a cross-sectional equity study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Full-text access boundary: the publisher full text sits behind subscription restrictions and was not taken from the publisher; abstract-level facts were verified on the publisher landing and a university page, construction/table facts in full-text excerpts of the identical paper, disclosed as this record's evidence ceiling — any table-level dispute beyond the quoted construction facts is decided against this record, never patched by inference.
3. Self-state proxy admission: the paper's state is a diversified equity-market return; this record feeds the asset's own 36-month print into the same cut. State and formation are then functions of one price path — a trending tape arms its own gate — which has no counterpart in the source. Any diversification, breadth, or lead-lag property of a true market state is discarded by declared derivation, not silently carried.
4. No crypto sample anywhere: no 1929–1995 equity evidence speaks to BTCUSDT behavior; single-asset crypto state-gated momentum is unevidenced by the source and may differ arbitrarily — including inverting (later literature reports momentum following DOWN states in China, fenced here as a sample-specificity warning, never evaluated). A gated-out rally or a fully ridden DOWN-state slide are both live possibilities by construction.
5. Cost silence fenced: the paper's spreads are cost-free returns, not net-of-cost tradable P&L — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
6. Overlap admission: the source holds overlapping event-time cohorts while this record holds one sequential sleeve per month — a declared material timing change; any turnover, smoothing, or diversification property of the overlapping construction is discarded, not carried.
7. Bare-sign simplification: the paper ranks break-pointed cross-sections into winner/loser tails; this record trades the bare single-asset joint sign. Any distributional information in the paper's sort is discarded by declared derivation, not silently carried.
8. Transition blindness: later market-dynamics literature notes momentum losses concentrate in state transitions; this record re-reads the gate monthly but holds through any intra-month transition with no exit by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 36-month self-state `>= 0` UP cut / 6-month formation T−5..T / no skip / strict joint gate / month-end decision / next-open fills / single-position sequential long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — State-gate relevance: dropping the pinned 36-month UP gate (unconditional 6-month-sign twin, same monthly grid) must not improve net expectancy; fail ⇒ the paper's state cut carries no advantage over bare momentum on the same tape.
- F2 — Formation relevance: replacing the pinned 6-month formation with the 12-month formation under the identical UP gate (same sign, same grid, TSMOM-style window) must not improve net expectancy; fail ⇒ the six-month trigger carries no advantage over the annual read under the same gate.
- F3 — Direction-twin relevance: the contrarian-signed twin under the identical UP gate (long iff UP-state AND `R_T <= 0`, flat otherwise) must not outperform the pinned same-signed mapping; fail ⇒ the winner leg does not survive the port and the record's sign is doing negative work.
- F4 — DOWN-state asymmetry relevance: trading the formation leg inside DOWN states (long iff DOWN-state AND `R_T > 0`, flat otherwise) must not outperform the pinned flat-in-DOWN posture; fail ⇒ the paper's core UP-only asymmetry inverts on this tape and the gate points the wrong way.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid calendar months on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets, other state windows, or other formation windows would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across individual equities conditioned on a diversified market state; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Self-state proxy: state and formation read one price path, so the gate and the trigger are mechanically correlated; any breadth or diversification in the paper's market state is lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Sequential-holding deviation: the source's overlapping event-time sleeves are replaced by one sequential sleeve per month; turnover smoothing and cohort diversification are lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Bare-sign simplification: the paper buys/sells ranked decile tails; this record trades the bare joint sign. Any distributional information in the paper's sort is discarded by declared derivation, not silently carried.
- Cash without yield: flat months earn nothing here while neither paper leg accrues cash yield either — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper starts cohorts in event time with no fill convention; this record fills next open. On gapping month boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is a month away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Warmup cost: the first thirty-six calendar months are flat by record rule, so any textbook state-plus-formation completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, month-end decision on completed `1d` closes, next-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Cooper, Michael J. & Gutierrez, Roberto C. Jr. & Hameed, Allaudeen (2004). Market States and Momentum. Journal of Finance 59(3), 1345–1365. https://doi.org/10.1111/j.1540-6261.2004.00665.x (Crossref-verified 2026-10-13; publisher landing https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2004.00665.x; SSRN abstract https://papers.ssrn.com/sol3/papers.cfm?abstract_id=299927; university abstract page https://eccles.utah.edu/news/document/market-states-and-momentum)
