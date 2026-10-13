---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Jegadeesh-Titman 1993 6-month 6-month momentum sequential long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1993-03-01
sources:
  - https://ideas.repec.org/a/bla/jfinan/v48y1993i1p65-91.html
  - https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
  - https://www.jstor.org/stable/2328882
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Jegadeesh-Titman 1993 6-month 6-month momentum sequential long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (RePEc canonical record, DOI landing, and JSTOR stable page read 2026-10-13; full-text methods verified against a text-layer copy of the identical JSTOR scan the same day):

- Jegadeesh, Narasimhan & Titman, Sheridan, `Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency` — Journal of Finance, vol. 48, no. 1, 65–91 (March 1993). DOI `10.1111/j.1540-6261.1993.tb04702.x`; RePEc handle `RePEc:bla:jfinan:v:48:y:1993:i:1:p:65-91`; JSTOR stable `http://www.jstor.org/stable/2328882`. Canonical record: https://ideas.repec.org/a/bla/jfinan/v48y1993i1p65-91.html (`Jegadeesh, Narasimhan & Titman, Sheridan, 1993. "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency," Journal of Finance, American Finance Association, vol. 48(1), pages 65-91, March.`).
- Pinned headline spec (publisher/JSTOR Abstract, read verbatim): `This paper documents that strategies which buy stocks that have performed well in the past and sell stocks that have performed poorly in the past generate significant positive returns over 3- to 12-month holding periods.` Sample window adopted at section level only (§II: NYSE and AMEX stocks, 1965 to 1989, CRSP daily returns file compounded to monthly; the 12-month/12-month leg needs 23 months of lags so the first full calendar year examined is 1965).
- Pinned construction facts (§I, read verbatim from the text layer): `The strategies we consider select stocks based on their returns over the past 1, 2, 3, or 4 quarters. We also consider holding periods that vary from 1 to 4 quarters. This gives a total of 16 strategies. In addition, we examine a second set of 16 strategies that skip a week between the portfolio formation period and the holding period.` / `By skipping a week, we avoid some of the bid-ask spread, price pressure, and lagged reaction effects that underlie the evidence documented in Jegadeesh (1990) and Lehmann (1990).` / `To increase the power of our tests, the strategies we examine include portfolios with overlapping holding periods. Therefore, in any given month t, the strategies hold a series of portfolios that are selected in the current month as well as in the previous K - 1 months, where K is the holding period.` / `a strategy that selects stocks on the basis of returns over the past J months and holds them for K months (we will refer to this as a J-month/K-month strategy) is constructed as follows: At the beginning of each month t the securities are ranked in ascending order on the basis of their returns in the past J months.` / `In each month t, the strategy buys the winner portfolio and sells the loser portfolio, holding this position for K months. In addition, the strategy closes out the position initiated in month t - K.` Portfolio-level headline numbers fenced, never adopted here: the most successful zero-cost leg `selects stocks based on their returns over the previous 12 months and then holds the portfolio for 3 months` at `1.31% per month` contiguous and `1.49% per month` with the 1-week lag; `The 6-month formation period produces returns of about 1% per month regardless of the holding period`; the paper then establishes `one specific strategy in detail, the 6-month/6-month strategy that does not skip a week between the portfolio formation period and the holding period` as representative (`The results for this strategy are representative of the results for the other strategies`); the 6-month-formation illustration (`the portfolio formed on the basis of returns realized in the past 6 months generates an average cumulative return of 9.5% over the next 12 months but loses more than half of this return in the following 24 months`) is likewise portfolio-level and fenced.
- Access boundary (disclosed, not worked around): the publisher full text sits behind subscription walls; section-level methods above were verified in a publicly hosted text-layer copy of the identical JSTOR scan (identical title/authors/journal/vol/pages/stable-URL block verified in-text, pp. 65–69 read verbatim). No table cell beyond the quoted headline numbers is cited anywhere in this record.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's representative 6-month/6-month winner leg ported to one crypto asset as a sequential 6-calendar-month long-or-flat hold — not a lossless reproduction of the paper's cross-sectional decile-spread study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance perpetual (the NYSE/AMEX decile cross-section, the winner-minus-loser zero-cost spread, the rebalanced/buy-and-hold accounting, and every portfolio-level performance claim are fenced off, never carried — see Negative evidence 1); (2) formation fixed to the cumulative 6-calendar-month close-to-close simple return over months T−5..T at a block-end decision (the paper's J = 6-month past-return rank input ported to calendar months — the bare-close definition with no distributions is the declared port, BTC pays none); (3) long-flat direction mapping on the strict formation sign (the paper's long-short spread leg is fenced; the short permission is simply unused — see Signal); (4) sequential non-overlapping 6-calendar-month holding blocks on completed `1d` closes with next-open fills (the paper holds K overlapping cohorts with 1/K monthly turnover; the derived port holds one cohort per block so single-position state stays explicit — a material event-timing change, declared here, never implied); (5) an adopted six-full-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's cost-free CRSP accounting; (6) fixed 100%-equity single-position sizing with no leverage (the paper holds equally weighted decile portfolios, never a single-asset book). The 6-month formation, the same-signed winner mapping, the 6-month holding length, the strict sign rule, the no-skip representative pin, and the no-stop/no-target/no-trailing posture (signal-roll exits only) are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `titman`, `jegadeesh-titman`, `buying winners`, `relative strength`, `J-month`, `past J months`, `6-month/6-month` return no strategy record in the main tree — the only hits are citation/prose fragments (the TSMOM record's Jegadeesh-Titman 1993 holding-construction citation scoped as a construction reference, the Novy-Marx record's generic `buying winners and selling losers` construction quote, one PMO record's charting-manual `relative strength order` sentence). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` conditions its monthly hold on the sign of the trailing 12-month cumulative return with a 1-month hold (twice the formation, one-sixth the holding of this record); `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md` holds next month on the sign of a lagged intermediate formation that deliberately ignores the six most recent months (an echo window, opposite recency handling and one-sixth the holding); `jegadeesh-1990-monthly-reversal-long-flat-btcusdt-1d-2026-10-13.md` inverts the sign of a 1-month formation (a 1-month reversal leg, opposite mapping and one-sixth the formation); `lehmann-1990-weekly-reversal-long-flat-btcusdt-1d-2026-10-13.md` trades a weekly grid, never a multi-month formation; `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` compares a price level against its own 10-month average — a level comparison with no return-sign anywhere; the calendar holds carry no price-conditioned leg at all. Five-axis distinction: no pool record and no open PR holds a sequential six-calendar-month block long-or-flat on the same-signed 6-month formation that includes the most recent months.

## Economic mechanism

### Source-reported

Relative-strength continuation over practitioner horizons, not short-run reversal or long-run overreaction: practitioners `base their selections on price movements over the past 3 to 12 months`, and the paper's `analysis of NYSE and AMEX stocks documents significant profits in the 1965 to 1989 sample period for each of the relative strength strategies examined` (§I lead, mechanism framing fenced to the paper's 1965–1989 equity sample, never adopted as a crypto claim here). The paper monetizes the pattern as zero-cost winner-minus-loser spreads of about 1% per month for 6-month-formation legs (Table I — spread-level claim, fenced, never adopted here).

### Research interpretation

Slow-trend continuation port: the 6-month formation ending at the block boundary acts as a two-quarter drift sensor that only lets sustained advances trigger exposure, while the locked 6-month holding block with no intra-block trading makes whipsaws structurally impossible inside the half-year — the strategy can be up to six months stale but can never chase last week's candle or flip on a single red month. Unlike trailing monthly momentum (TSMOM) the holding commitment is six times longer so a one-month pullback cannot exit the position. Unlike intermediate echo momentum (Novy-Marx) the freshest months are fully read by construction: a vertical six-month rally prints long immediately at the next block boundary. Unlike one-month reversal (Jegadeesh 1990) the mapping is same-signed and the window is six times longer. Unlike moving-average regimes (Faber) there is no average anywhere: the signal is a bare 6-month cumulative-return sign. The bet, as derived, is purely on the paper's representative 6/6 winner leg surviving the port to BTCUSDT at half-year cadence, never on a level, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (6-month formation including recent months, no skip, strict sign, 6-month sequential blocks — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in a block-end calendar month T (blocks are consecutive non-overlapping 6-calendar-month groups tiling forward from the first decidable month-end; month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- Formation (pinned): `R_T = C_T / C_{T−6} − 1` (simple cumulative close-to-close return, closes only — `C_T` is the close of the last completed daily bar dated in month T and `C_{T−6}` the close of the last completed daily bar dated in month T−6; this compounds exactly the six calendar-month returns of months T−5..T, i.e. the paper's J = 6-month past-return input with the representative no-skip pin; no log/simple choice left open, no dividend or distribution adjustment exists for BTC).
- Skip (pinned, not a parameter): none — this record adopts the paper's representative 6-month/6-month leg `that does not skip a week`; the paper's second set of 16 skip-a-week variants is fenced, never read.
- Position target for the next block of six calendar months T+1..T+6 (pinned, strict): `R_T > 0` → long; `R_T <= 0` → flat (the equality leg is pinned to flat — measure-zero on live tape, no tie semantics beyond this; the paper's spread is long-short across deciles and the short leg is fenced by declared adaptation (3)).
- Orders (pinned): at most one order event per 6-month block boundary, placed for the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port; the paper rebalances overlapping cohorts at month beginnings with no executable fill convention, so the sequential next-open fill is declared, never implied): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-block evaluation, no intra-block orders, no adds, no partials, no second decision inside months T+1..T+6 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next block-end signal mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-block exit; a half-year adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` closes of BTCUSDT only: two month-end closes per decision (`C_T` and `C_{T−6}`; no `open` except as fill price, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: 6-calendar-month blocks. One evaluation per block on the last completed daily bar of the block-end month; fills land on the next daily bar's open (first open of the new block). All formation inputs are completed-bar closes — no provisional month-end value is ever used.
- Warmup: six full calendar months of `1d` bars before the first decision (both month-end closes must exist). Bars before the first decidable block-end are flat by record rule; no signal before the seventh calendar month's first open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's month-beginning rebalance cadence): block-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per block boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long blocks carry realized funding, flat blocks carry none, and the form holds genuine flat blocks so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat block needs only the next positive block formation sign (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping cohorts (the paper's K overlapping sleeves with 1/K monthly turnover are replaced by the declared sequential single sleeve — see Limitations). The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: the J-by-K quarter grid with 16 contiguous plus 16 skip-a-week legs (§I), the skip-week microstructure rationale (§I), the overlapping-hold construction with month-t ranking on past-J returns and month t−K close-out (§I), the 1965–1989 CRSP-daily-compounded sample (§II), and the representative 6-month/6-month no-skip leg (§II). It ships zero adopted performance numbers for this record: the 1.31%/1.49% 12m/3m spreads, the ~1%-per-month 6-month-formation cells, the 9.5% illustration, and every t-statistic describe the paper's equity decile study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every headline result (decile sorts, equal weighting, winner-minus-loser spreads, factor-spanning and size/beta/calendar splits, the 1.31/1.49 and ~1% cells) belongs to a cross-sectional equity study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Full-text access boundary: the publisher full text sits behind subscription restrictions and was not taken from the publisher; section-level methods were verified in a publicly hosted text-layer copy of the identical JSTOR scan, disclosed as this record's evidence ceiling — any table-level dispute beyond the quoted construction facts is decided against this record, never patched by inference.
3. No crypto sample anywhere: no 1965–1989 equity evidence speaks to BTCUSDT behavior; single-asset crypto 6/6 momentum is unevidenced by the source and may differ arbitrarily. The locked 6-month block can ride a full half-year drawdown with no exit by construction (flat-while-green at block ends is equally possible).
4. Cost silence fenced: the paper's spreads are cost-free returns, not net-of-cost tradable P&L — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
5. Overlap admission: the source holds K overlapping sleeves with monthly 1/K turnover while this record holds one sequential sleeve per block — a declared material timing change; any turnover, smoothing, or diversification property of the overlapping construction is discarded, not carried.
6. Bare-sign simplification: the paper ranks break-pointed cross-sections into winner/loser tails; this record trades the bare single-asset formation sign. Any conditioning information in the paper's distributional sort is discarded by declared derivation, not silently carried.
7. Block latency: the grid can only react at 6-month boundaries to information already baked at the boundary; a fresh regime break is missed for up to half a year by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 6-month formation T−5..T / no skip / strict `>0`-long-else-flat / block-end decision / next-open fills / single-position sequential long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Recency relevance: replacing the pinned recent 6-month formation with the lagged intermediate 6-month formation over months T−11..T−6 (same sign, same block grid, Novy-Marx-style skip) must not improve net expectancy; fail ⇒ the paper's recent-leg inclusion carries no advantage over the echo window on the same tape.
- F2 — Holding-length relevance: replacing the pinned 6-month sequential holding with a 1-month holding on the identical 6-month formation sign (TSMOM-style, same grid phase) must not improve net expectancy; fail ⇒ the half-year commitment carries no advantage over the monthly roll.
- F3 — Direction-twin relevance: the contrarian-signed twin on the identical block grid (long iff `R_T <= 0`, flat otherwise) must not outperform the pinned same-signed mapping; fail ⇒ the relative-strength leg does not survive the port and the record's sign is doing negative work.
- F4 — Full-size relevance: replacing fixed 100%-equity sizing with fixed 50%-equity sizing must not improve risk-adjusted expectancy; fail ⇒ the declared size pin is doing unacknowledged work — or the record's size choice is arbitrary leverage in disguise.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid 6-calendar-month blocks on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets or lookbacks would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across individual equities; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Sequential-holding deviation: the source's overlapping K-sleeve construction with monthly turnover is replaced by one sequential sleeve per block; turnover smoothing and cohort diversification are lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Bare-sign simplification: the paper buys/sells ranked decile tails; this record trades the bare formation-block sign. Any distributional information in the paper's sort is discarded by declared derivation, not silently carried.
- Cash without yield: flat blocks earn nothing here while neither paper leg accrues cash yield either — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper rebalances at month beginnings with no fill convention; this record fills next open. On gapping block boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-block exit: adverse excursion inside the six-month holding block has no guardrail; the next decision is months away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Stale-signal latency: the formation window ends at the block boundary and the position then locks for six months; fresh information is structurally ignored for half a year — pinned, not recovered.
- Warmup cost: the first six calendar months are flat by record rule, so any textbook formation completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- https://ideas.repec.org/a/bla/jfinan/v48y1993i1p65-91.html
- https://doi.org/10.1111/j.1540-6261.1993.tb04702.x
- https://www.jstor.org/stable/2328882
