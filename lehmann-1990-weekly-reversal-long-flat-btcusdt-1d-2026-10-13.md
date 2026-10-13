---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Lehmann 1990 one-week reversal weekly long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1990-02-01
sources:
  - http://econpapers.repec.org/RePEc:tpr:qjecon:v:105:y:1990:i:1:p:1-28
  - https://nber.org/papers/w2533
  - https://academic.oup.com/qje/article-lookup/doi/10.2307/2937816
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Lehmann 1990 one-week reversal weekly long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end at the bibliographic and abstract level (RePEc/EconPapers record, NBER working-paper page, and OUP article page fetched and read 2026-10-13):

- Lehmann, Bruce N., `Fads, Martingales, and Market Efficiency` — The Quarterly Journal of Economics, vol. 105, issue 1, 1–28, February 1990. JSTOR stable `10.2307/2937816`; RePEc handle `RePEc:tpr:qjecon:v:105:y:1990:i:1:p:1-28`. Canonical record: http://econpapers.repec.org/RePEc:tpr:qjecon:v:105:y:1990:i:1:p:1-28 with predecessor NBER Working Paper 2533 (1988): https://nber.org/papers/w2533 and publisher lookup https://academic.oup.com/qje/article-lookup/doi/10.2307/2937816.
- Pinned headline spec (publisher Abstract, read verbatim on the RePEc mirror): systematic changes in fundamental valuation over intervals like a week `should not occur in efficient markets`, and the evidence shows that the `"winners" and "losers" one week experience sizeable return reversals the next week in a way that reflects apparent arbitrage profits which persist after corrections for bid-ask spreads and plausible transactions costs.` The paper's interpretation is fenced with the quote: `This probably reflects inefficiency in the market for liquidity around large price changes.` Sample window and table/figure-level numbers are not stated in the Abstract and are omitted by rule rather than reconstructed.
- Pinned strategy construction (OUP article page, read verbatim): `study the profits of costless (i.e., zero net investment) portfolios which give negative weight to recent winners and positive weight to recent losers.` The short-run martingale benchmark is fenced with the quote: `The short-run martingale model predicts that these costless portfolios should tend to earn zero profits.` The zero-net-investment cross-sectional portfolio is fenced, never ported (see Derived-record declaration).
- Access boundary (disclosed, not worked around): the complete published text sits behind the publisher paywall and was NOT read; every source-reported fact below carries Abstract/excerpt provenance, and all table/figure/section-level claims are omitted by rule rather than reconstructed.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's one-week winner/loser reversal leg ported to one crypto asset as a long-or-flat weekly contrarian hold — not a lossless reproduction of the paper's zero-cost equity-portfolio study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance perpetual (the winner/loser cross-section, the zero-net-investment construction, and every portfolio-level profit claim are fenced off, never carried — see Negative evidence 1); (2) formation fixed to one ISO-calendar-week (Monday–Sunday UTC) close-to-close simple return sign (the paper's weekly grid and one-week reversal horizon are source-native; the plain-close definition with no distributions is the declared port — BTC pays none); (3) long-flat direction mapping (long exactly when the formation week is negative; the paper's negative-weight-winners/positive-weight-losers heuristic maps to the loser leg only — the winner-short leg is fenced and the short permission is simply unused — see Signal); (4) weekly decision grid on completed `1d` closes with next-open fills (the paper is a portfolio-profit study and ships no executable fill convention, so the causal port is declared, never implied); (5) an adopted two-full-ISO-week warmup flat by record rule plus house fees/funding treatment replacing the paper's spread-and-cost-corrected abnormal-profit accounting; (6) fixed 100%-equity single-position sizing with no leverage (the paper sizes zero-cost portfolios, never a single-asset book). The 1-week formation, the 1-week holding period, the sign inversion (the negative-weight-to-winners leg, nothing else), the weekly update, and the no-stop/no-target/no-trailing posture (signal-roll exits only) are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `lehmann`, `fads.martingales`, `one-week reversal`, `1-week reversal`, `weekly reversal`, `winner.loser`, `winners.and.losers` return zero strategy records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `jegadeesh-1990-monthly-reversal-long-flat-btcusdt-1d-2026-10-13.md` inverts the sign of a completed calendar-MONTH return and holds a month — a twelve-times-slower formation on a different paper with a different identification (first-order monthly autocorrelation, not weekly liquidity); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` conditions its monthly hold on the sign of the trailing 12-month cumulative return with the SAME-direction mapping (long when positive) — a momentum leg, opposite sign logic and fifty-two times the formation of this record; `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` is a pure weekday-seasonal hold with no price-conditioned leg at all; the indicator mean-reversion family (`etf-3day-reversion`, `connors-rsi2`, `cumulative-rsi`, `ibs-mean-reversion`, `catching-the-bottom-rsi-dip`, `oversold-rsi`, `three-down-three-up`, `turtle-soup-donchian-fade`, `inside-bar-failure-fade`) forms on 1–5-bar oscillator, pattern-failure, or streak constructions, never on a calendar-week total-return sign. Five-axis distinction: no pool record and no open PR holds next ISO week long-or-flat on the inverted sign of the completed ISO-week return.

## Economic mechanism

### Source-reported

Short-horizon liquidity-driven reversal, not trend riding: over intervals like a week there should be no systematic change in fundamental valuation in an efficient market, yet last week's winners and losers systematically reverse the next week — with the apparent arbitrage surviving spread and transaction-cost corrections — which the paper attributes to inefficiency in the market for liquidity around large price changes (Abstract — mechanism framing fenced to the paper's equity sample, never adopted as a crypto claim here). The monetization is a zero-net-investment portfolio giving negative weight to recent winners and positive weight to recent losers (OUP construction sentence — cross-sectional form, fenced, never adopted here).

### Research interpretation

Weekly contrarian-regime port: the sign of one completed ISO week admits only post-decline weeks as exposure permission, while the once-a-week update makes intra-week overtrading structurally impossible — the strategy can be a whole week early or late but can never chase inside the holding week. Unlike return-sign momentum (TSMOM) the mapping is inverted by construction: red formation week means exposure, green means cash. Unlike the monthly reversal sibling (Jegadeesh record) the formation is seven daily closes, not a calendar month, and the re-decision fires fifty-two times a year — the bet is on liquidity snap-back around large weekly moves, not on monthly autocorrelation. Unlike oscillator/pattern mean-reversion there is no threshold, band, streak count, or failure shape: one weekly sign, re-decided weekly, held until the next Sunday re-maps it. The bet, as derived, is purely on the paper's one-week reversal leg surviving the port to BTCUSDT at weekly cadence, never on a level, band, oscillator, volume, weekday-seasonal, or funding anchor.

## Signal

Exact rule as pinned (1-ISO-week formation, strict sign inversion, weekly grid — any other value is a different, unpinned rule):

- Week definition (pinned): ISO-calendar weeks, Monday 00:00 through Sunday 23:59 UTC; week membership is the UTC calendar date of each `1d` bar — deterministic on the 24/7 tape (Binance daily bars are UTC-dated). No week-numbering scheme is read; only consecutive Sunday closes matter.
- Decision bar: the `1d` bar dated Sunday of ISO week W (the last completed daily bar of the week).
- Formation (pinned): `R_W = C_W / C_{W-1} − 1` (simple close-to-close return, closes only — `C_W` is the Sunday close of week W, `C_{W-1}` the Sunday close of the immediately preceding week; no log/simple choice left open, no dividend or distribution adjustment exists for BTC).
- Position target for ISO week W+1 (pinned, inverted sign): `R_W < 0` → long; `R_W >= 0` → flat (the equality leg is pinned to flat — measure-zero on live tape, no tie semantics beyond this; the inversion is the paper's negative-weight-to-winners leg, not a researcher pin).
- Orders (pinned): at most one order event per week, placed for the first `1d` open of week W+1 present on the tape (next-open fill after the decision bar — the declared causal port; the paper ships no fill convention): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-week evaluation, no intra-week orders, no adds, no partials, no second decision inside week W+1 for any reason including large adverse excursion.
- Missing-bar rule (pinned edge case, not invented later): if the decision-Sunday close or its prior-Sunday base is absent from the `1d` tape, no re-decision occurs that week — the prior week's target persists and no order is placed.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next Sunday signal mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-week exit; a week-long adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the paper's heuristic is winner-short/loser-long across the cross-section; the winner leg is fenced and the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` closes of BTCUSDT only: two Sunday closes per decision (no `open` except as fill price, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: ISO week. One evaluation per week on the Sunday daily bar; fills land on the next daily bar's open (first open of the new week present on the tape). All formation inputs are completed-bar closes — no provisional Sunday value is ever used.
- Warmup: two full ISO weeks of `1d` bars before the first decision (both Sunday closes must exist). Bars before the first decidable Sunday close are flat by record rule; no signal before the Monday open following the second Sunday close may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's weekly portfolio grid): Sunday completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per week, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's abnormal-profit accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports spread-and-cost-corrected abnormal profits in a 1980s equity cost regime, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long weeks carry realized funding, flat weeks carry none, and the form holds genuine flat weeks so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat week needs only the next negative Sunday sign (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The Abstract ships every adopted construction fact: the no-fundamental-change-in-a-week identification logic, the `"winners" and "losers" one week experience sizeable return reversals the next week` leg (the 1-week formation/holding grid with the inverted-sign mapping), the persistence `after corrections for bid-ask spreads and plausible transactions costs`, and the liquidity-around-large-moves interpretation — plus the OUP construction sentence (`negative weight to recent winners and positive weight to recent losers`) that pins the inversion direction. It ships zero adopted performance numbers for this record: the paper's arbitrage-profit results describe its equity winner/loser portfolios, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every tradable result (zero-cost winner/loser portfolios, martingale-benchmark tests, liquidity interpretation) belongs to a cross-sectional equity study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Full-text boundary: the complete paper (methods, tables, figures, robustness, sample window) sits behind the publisher paywall and was not read; abstract-plus-excerpt provenance is disclosed as this record's principal evidence ceiling — any table-level dispute is decided against this record, never patched by inference.
3. No crypto sample anywhere: no equity-week evidence speaks to BTCUSDT behavior; single-asset crypto weekly reversal is unevidenced by the source and may differ arbitrarily. Weekly-sign reversal can underperform a roaring one-way bull tape for months by construction (flat through every green week).
4. Bid-ask-bounce headwind: part of any observed short-horizon reversal mechanically reflects bid-ask bounce in transaction prices (Roll-style microstructure); the paper corrects for spreads and still finds profits in its 1980s equity tape, but the bounce-vs-information split on a 24/7 crypto tape with a different microstructure is unevidenced here — the record trades the bare weekly sign with no bounce decomposition, disclosed, not recovered.
5. Lead-lag attribution headwind: the subsequent literature attributes much of weekly contrarian profit to cross-stock lead-lag autocorrelations rather than own-stock overreaction (Lo–MacKinlay-style decomposition); a single-asset port owns no cross-section to harvest, so if the effect is mostly lead-lag, this record's leg is structurally the wrong slice — disclosed, not hedged.
6. Opposing-leg admission: the weekly grid is fifty-two re-decisions a year against the monthly sibling's twelve — turnover and cost load are structurally heavier, and a red-week/green-month conflict is resolved unconditionally in favor of the weekly leg here, disclosed, not hedged.
7. Bare-sign simplification: the paper's portfolios weight winners and losers across the cross-section; this record trades the bare single-asset formation-week sign. Any conditioning or weighting information in the paper's construction is discarded by declared derivation, not silently carried.
8. Weekend-structure gap: the paper's weeks are equity trading weeks; crypto ISO weeks price weekends continuously — weekend jumps land inside the formation week here by construction, and any weekend-vs-weekday reversal split is unmodeled, disclosed, not patched.
9. Weekly latency: the grid can only react at Sunday close; a mid-week reversal is ridden (or missed) to Sunday by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 1-ISO-week formation / strict `<0`-long-else-flat / Sunday decision / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Formation-length relevance: replacing the pinned 1-week formation with a 2-week formation sign (same inversion, same grid) must not improve net expectancy; fail ⇒ the paper's first-order weekly leg carries no advantage over the slower neighbor.
- F2 — No-skip relevance: ending the 1-week formation one week before the decision bar (skip-latest-week variant) must not improve net expectancy; fail ⇒ the paper's no-skip week-end timing adds nothing over the skipped convention.
- F3 — Direction-twin relevance: the momentum-signed twin on the identical grid (long iff `R_W >= 0`, flat otherwise) must not outperform the pinned contrarian mapping; fail ⇒ the one-week reversal leg does not survive the port and the record's inversion is doing negative work.
- F4 — Full-size relevance: replacing fixed 100%-equity sizing with fixed 50%-equity sizing must not improve risk-adjusted expectancy; fail ⇒ the declared size pin is doing unacknowledged work — or the record's size choice is arbitrary leverage in disguise.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid ISO-week on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market prices weekends inside the ISO week by construction (week membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets or lookbacks would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across individual equities; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Bare-sign simplification: the paper weights winner/loser portfolios; this record trades the bare formation-week sign. Any weighting information in the paper's construction is discarded by declared derivation, not silently carried.
- Cash without yield: flat weeks earn nothing here while neither paper leg accrues cash yield either — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper is a portfolio-profit study with no fill convention; this record fills next open. On gapping Sunday/Monday boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-week exit: adverse excursion inside the holding week has no guardrail; the next decision is days away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Weekly latency and turnover: the grid re-decides fifty-two times a year; in choppy tape the record can flip exposure weekly and pay the full house cost load on every flip — pinned, not smoothed.
- Warmup cost: the first two ISO weeks are flat by record rule, so any textbook reversal completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Lehmann, Bruce N., Fads, Martingales, and Market Efficiency (The Quarterly Journal of Economics, vol. 105(1), 1–28, February 1990 — RePEc/EconPapers canonical record with full publisher Abstract, verified 2026-10-13; full text behind publisher paywall, not accessed): http://econpapers.repec.org/RePEc:tpr:qjecon:v:105:y:1990:i:1:p:1-28
- NBER Working Paper 2533 predecessor page (bibliographic cross-check, DOI 10.3386/w2533): https://nber.org/papers/w2533
- OUP article lookup (source identity and heuristic-strategy construction sentence): https://academic.oup.com/qje/article-lookup/doi/10.2307/2937816
