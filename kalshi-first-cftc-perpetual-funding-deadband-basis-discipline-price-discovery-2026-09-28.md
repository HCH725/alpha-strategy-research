---
schema: strategy-research-record-v1
title: "Kalshi first CFTC-regulated perpetual futures funding deadband: 73.0 percent exactly-zero 8-hour funding intervals, onshore index-centred basis against an offshore persistent discount, and a pre-registered price-discovery test (SSRN 7098201)"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - market-design
  - price-discovery
  - ssrn
status: research-only
confidence: medium
source_as_of: 2026-07-11
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7098201"
  - "https://doi.org/10.2139/ssrn.7098201"
  - "https://ssrn.com/abstract=7098201"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Reference count: the SSRN landing page read on 2026-09-28 prints the heading '0 References', while the pinned 11-page PDF ends with a printed reference list of 14 entries counted entry by entry - unreconciled (the same SSRN landing-versus-PDF pattern appears elsewhere in this repository)."
  - "Reconstruction accuracy: the abstract states that Bybit realized funding was reconstructed from its public premium index 'to within 0.1bp', while section 3.2 and Table C1 report 0.10bp for BTC but 0.13bp (0.134 printed) for ETH - the abstract's single 0.1bp figure does not cover ETH - unreconciled."
  - "Sign of the active tail: section 4.1 states that the pooled nonzero distribution concentrates between -1 and -3bp with 76.4 percent of nonzero prints negative, while section 4.3 states that 'from late June onward the nonzero prints are persistently small and positive, between 1 and 2.5bp' - no subperiod table is printed anywhere to reconcile the pooled negative shoulder with the recent positive run - unreconciled."
  - "Pre-registration date arithmetic: section 7 conditions execution on 'eight weeks of joint order book data' accumulated from a collection start of 11 July 2026 (section 1 and Appendix A), which is 5 September 2026, but fixes execution 'on or after 12 September 2026' - the eight-week interval and the stated date do not close - unreconciled."
---

# Kalshi First CFTC-Regulated Perpetual Futures: Funding Deadband, Basis Discipline and a Pre-Registered Price-Discovery Test

## Provenance

- Source type: SSRN working paper (single-author, independent researcher). Read in full on 2026-09-28.
- Canonical source identity: DOI `10.2139/ssrn.7098201`. Landing https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7098201.
- Title exactly as printed on the PDF title block and the landing heading: "The Perpetual That Rarely Pays: Funding Deadbands and Basis Discipline in the First CFTC-Regulated Perpetual Futures Market".
- Author, exactly as printed: Boon Chuan Lim. Landing affiliation line: "Independent Researcher". PDF title block adds "Independent Researcher, Singapore" and the contact line `boonchuan@singapore.to`, ORCID `0009-0005-8477-9393`. Sole author; no co-authors.
- Version and dates, unreconciled by the source: landing "Posted: 28 Jul 2026"; landing "Date Written: July 11, 2026"; suggested-citation line dated "(July 11, 2026)"; PDF header "This version: 11 July 2026. First look and pre-registered analysis plan."; PDF metadata `/CreationDate D:20260711070923Z` (11 July 2026 07:09:23 UTC), `/Creator LibreOffice 24.2`, `/Author Un-named`.
- Landing metadata read 2026-09-28: "11 Pages"; license line "The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission."; heading "0 References"; heading "0 Citations"; paper statistics DOWNLOADS 44, ABSTRACT VIEWS 165; no journal, no issue, and no peer-review statement anywhere on the landing page, so peer-review/publication status is `not stated in source`. The PDF itself prints no "has not been peer reviewed" banner either.
- PDF pinned for this record: 300,650 bytes, 11 pages, SHA-256 `4eeadfc22e955c3a431de030575be8d95f78f86e57d5380ee0e24b20d39e9b0c`, retrieved 2026-09-28 through the landing page's "Open PDF in Browser" `Delivery.cfm` link (a stable non-expiring link, not a presigned or session-bound object; no expiry URL is stored in this record), text-extracted page by page with pypdf to 35,702 characters / 475 lines and all 11 pages read, covering the abstract, sections 1-8, Table 1, Table 2, Figure 1 and Figure 2 captions, Appendices A, B and C, Table C1, the disclosure block and the 14-entry reference list.
- Embedded declarations: JEL `G13, G14, G18, G23`; keywords "perpetual futures; funding rate; market design; deadband; CFTC; price discovery; cryptocurrency"; an AI disclosure stating the author used Anthropic Claude for code development, analysis-pipeline construction and manuscript drafting/editing with the author taking responsibility for all claims; "No funding was received for this work"; "The author declares no competing interests"; "Data and code sufficient to reproduce all tables and figures are available from the author" - i.e. no public repository, no replication-package DOI (data gap).
- Sample period: funding observations from the first funding event at 20:00 UTC on 3 June 2026 through 04:00 UTC on 11 July 2026 (113 eight-hour intervals per launch contract, 37.33 days, section 3.1 and Table 2); order-book collection began 11 July 2026 (section 1, Appendix A).
- Universe: 16 Kalshi perpetual contracts listed at the freeze - BCH, BTC, DOGE, DOT, ETH, HBAR, HYPE, LINK, LTC, NEAR, SHIB, SOL, SUI, XLM, XRP, ZEC (section 2.1) - of which 13 have funding observations (DOT, HBAR, XLM had none at the freeze); matched offshore comparator is 13 Bybit linear perpetuals plus BTCUSDT and ETHUSDT one-minute premium-index klines.
- Transaction-cost treatment: see Execution assumptions. A whole-document word scan of the pinned PDF finds zero occurrences of "transaction cost", "slippage", "backtest", "Sharpe", "turnover", "capacity", "borrow", "latency", "fill", "participation", "market impact", "liquidity", "pnl" or "net of cost"; all 7 occurrences of "commission" are the Commodity Futures Trading Commission, and all 6 occurrences of "fee" are the substring inside "feed". The paper proposes no trading rule, so it contains no cost model at all - every cost/fill/capacity field below is `data gap`, never zero.
- Regulatory primary source verified by us: `https://www.cftc.gov/filings/documents/2026/orgdcmkexbtxperporder26601.pdf` returned HTTP 200 with 179,109 bytes on 2026-09-28, and `https://www.cftc.gov/PressRoom/PressReleases/9240-26` returned HTTP 200 - both consistent with the paper's citation of CFTC Release 9240-26 of 29 May 2026.
- Pre-write source-identity dedup (2026-09-28, hidden-inclusive `rg -uuu` over the entire checkout including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` at 1,088,787 bytes): zero hits for `7098201`, `The Perpetual That Rarely Pays`, `KXBTCPERP`, `KXETHPERP`, `KalshiEX`, `external-api.kalshi.com`, `CF Benchmarks`, `funding deadband`, `Kalshi Klear`, `orgdcmkexbtxperp` and `0009-0005-8477-9393`; positive control `novy-marx` returned hits in the same session; `git log --oneline -20` used only as a convenience glance; Wiki Brain `kb_search` (read-only) returned only the adjacent pages listed under Related Wiki records.

## Economic mechanism

### Source-reported

The instrument's disciplining object is the funding rate, and the source argues the Kalshi design is "a different machine" from the offshore standard (sections 1 and 2.3). Kalshi computes funding as a pure time-weighted average of 480 one-minute premiums (perpetual price minus an externally administered CF Benchmarks reference index) over each eight-hour period, clamps the result to +/-2%, and - the design feature this paper is built around - snaps any absolute rate below 0.01% to exactly zero so that no payment is made. There is no interest-rate baseline component, unlike the dominant offshore formula F = P + clamp(I - P, +/-0.05%) with I = 0.01% per eight hours. The source calls the resulting zero band a "deadband" and stresses it is a stated rule, not an inference (section 2.3).

The paper documents three facts (sections 4 and 6): (1) 73.0 percent of 1,226 funding observations across 13 contracts are exactly zero; (2) the deadband alone does not produce that frequency - applying Kalshi's rule counterfactually to Bybit's own premium index over the identical window gives a zero share of 0.0 percent, because the offshore BTC perpetual traded at a persistent discount (mean one-minute premium -4.7bp, never positive across five weeks) while Kalshi's perpetual sat inside the one-basis-point band in 64.6 percent of windows; (3) offshore realized funding looks compressed (mean absolute 0.38bp on BTC) only because a negative premium and a positively clamped adjustment term nearly cancel, a decomposition validated by reconstructing realized funding to 0.10bp (BTC) and 0.13bp (ETH) mean absolute error.

The source deliberately leaves its interpretive question open (section 5). Under H-tight, a transparent, second-by-second, independently audited external reference index makes arbitrage cheap, so deviations are corrected before an eight-hour TWAP can leave the band - regulation plus an external benchmark delivers superior index tracking. Under H-anchor, the venue is young and thin, market makers quote around the benchmark, the perpetual price is the index plus a spread by construction, and the venue therefore contributes little independent price information for funding to discipline. The two are observationally equivalent at funding frequency and separate only at higher frequency, which is what the section 7 pre-registration tests.

### Research interpretation

Hypothesized mechanisms, stated in falsifiable form:

- H1 (funding-carry viability on a deadband venue): because the funding transfer is censored at +/-1bp per eight hours and fires in only about one quarter of intervals, a passive funding-carry position on the onshore regulated perpetual earns a funding transfer in roughly 27 percent of intervals and pays one in a negative-print regime; the expected gross carry per interval is therefore far smaller than the same rule on a venue with no deadband. Component roles: regime = venue funding design (deadband on/off, interest component present/absent); signal = sign and escape of the eight-hour TWAP premium relative to the +/-1bp band; transfer = realized funding paid or received at the funding instant; risk/exit = none specified by the source. This is a ported hypothesis about market design, not a source-claimed strategy.
- H2 (onshore satellite versus independent price contributor): under H-anchor the regulated onshore perpetual's mid-quote follows the offshore complex and the spot index with a lag and an information share indistinguishable from zero, so any lead-lag, information-share or microstructure alpha on this venue fails by construction; under H-tight the contribution is small but nonzero. The source pre-registers the discriminating test rather than reporting it.
- H3 (basis location, research-proposed): the same asset and the same five weeks show an offshore perpetual pinned about -4.7bp below its premium index and an onshore perpetual pinned inside +/-1bp of an external audited index, so the cross-venue basis/funding differential between a regulated onshore and an offshore perpetual is a distinct relative-value object from any single-venue funding carry. The source does not propose or test this trade.

No component is assumed to add alpha; F4, F6, F7 and F14 are required before any of the three hypotheses is retained.

## Signal

The source proposes **no trading signal, no entry, no exit and no sizing rule**. Its testable objects are market states, not orders. Everything below is source-reported unless labeled `research-proposed` or `research-defined`.

- Signal object 1, funding-rule state (fully specified by the source): every eight hours, take the 480 one-minute premiums of perpetual price minus reference index, average them, clamp to +/-2%, then set the rate to exactly zero if the absolute value is below 0.01% (sections 2.3 and 4.1). Formation timestamp: the funding instant; funding accrues at 12:00 AM, 8:00 AM and 4:00 PM Eastern Time = 04:00, 12:00 and 20:00 UTC under daylight saving and 05:13:21 UTC after the November shift, versus 00/08/16 UTC year-round offshore (Table 1). Availability: the rate is published after the interval closes; the source reports the full history is served in one response per ticker.
- Signal object 2, premium / basis (fully specified as a measurement, not a rule): eight-hour TWAP of the one-minute premium; report whether it lies inside the +/-1bp band and its sign. Kalshi centres inside the band in 64.6 percent of BTC windows; Bybit's mean premium is -4.7bp with maximum -0.07bp (sections 4.2 and 4.3, Table C1 footnote).
- Signal object 3, information share (pre-registered, not executed): Hasbrouck upper and lower bounds across covariance factorization orderings plus Gonzalo-Granger component shares on one-second mid-quotes for BTC and ETH across Kalshi, Bybit and the constituent regulated spot venues of the reference index, estimated daily with block-bootstrap confidence bands; robustness at 5- and 10-second sampling and event-time estimation; lead-lag confirmation by the lagged Hayashi-Yoshida cross-covariance estimator of Hoffmann, Rosenbaum and Yoshida (2013) (section 7). Execution fixed at "on or after 12 September 2026" - see the frontmatter contradictions.
- Registered auxiliary tests (section 5 and section 7): onshore-lead incidence at 1-60s horizons; attribution of deadband exits to index volatility versus onshore order flow (volume-differenced); cross-sectional zero share on venue activity with listing-age controls; reconstruction of Kalshi's TWAP from collected mid-quotes and the index, confirming realized prints equal "clamp then snap" (section 4.4); rolling-window version of the counterfactual.
- Position sizing, holding period, re-entry, stop, take-profit, order type: `not stated in source` - they do not exist in the source. The signal layer of this record is therefore `underspecified` as a strategy and fully specified only as a market measurement.
- Research-proposed operationalization used solely by the falsification plan: a static funding-carry that is funded only when the published rate is nonzero, entered at the funding instant and held to the next funding instant, with side taken to receive a positive printed rate. Any threshold, fee ladder, horizon or acceptance cutoff appearing in the Falsification plan is `research-defined` or `research-proposed`, never source-reported.

## Required data

- Instrument: Kalshi perpetual futures (linear, USD-margined, 0.0001 BTC per contract for BTC - about USD 6 of notional at sample-period prices - quoted in decimal dollars to four places), plus the matched Bybit linear perpetuals.
- Venue: Kalshi designated contract market, clearing through Kalshi Klear (a CFTC-regulated DCO); comparator venue Bybit; reference index CF Benchmarks real-time indices, for BTC the Bitcoin Real-Time Index (BRTI) aggregating regulated spot venues and updating every second.
- Market type / timeframe: crypto perpetual futures, eight-hour funding grid, one-minute premium candles, two-second order-book polls, five-second market-state polls, 24/7 trading.
- Fields: funding history (rate per interval per ticker); full two-sided order books; price, bid, ask, open interest, notional open interest; cumulative volume fields (differenced to recover interval volume, Appendix B); one-minute premium-index klines; realized eight-hour funding on the comparator; the reference-index series; contract specifications, leverage tiers and liquidation mark price from the API.
- Point-in-time / availability: Kalshi data from public unauthenticated REST endpoints under `external-api.kalshi.com/trade-api/v2/margin/`, which the API documentation described as unreleased at the access date (Appendix A); exchange documentation archived at archive.ph dated 2026-07-11 (source's own references, not independently read by us); Bybit from public v5 endpoints `funding/history` and `premium-index-price-kline`.
- Timestamp: one NTP-disciplined host for all receipt timestamps (Appendix A); Eastern-Time funding grid with a daylight-saving shift against a UTC offshore grid; out-of-order and duplicate handling is described only for the Bybit premium series (duplicates dropped, no interpolation, windows with fewer than 240 of 480 candles excluded - one window at the sample start).
- Missing data: funding pauses whenever the CF Benchmarks feed is unavailable, so funding observations can be missing not at random; the source reports no pause count (data gap). Three listed contracts have no observations at all. Missed market-state snapshots are interval-flagged and field resets are detected as negative differences (Appendix B), with validation deferred.
- Cost data: no cost, fee, spread, borrow, impact or participation dataset is used by the source (data gap, not zero); the only execution-relevant figures printed are a quoted spread of roughly 2bp at the touch and open interest of 693,877 BTC contracts = USD 4.45 million notional at the 11 July 2026 snapshot (section 6).

## Execution assumptions

Source-reported:

- The source executes no trades. There is no signal-to-order timing, order type, fill model, latency assumption, participation cap, leverage rule, borrow assumption, margin financing model, tax treatment or capacity analysis anywhere in the pinned PDF (full-document word scan recorded in Provenance). All of these are `data gap`.
- Contract mechanics that any replication would inherit (section 2.2 and Table 1): leverage is capped, varies by asset and position size, and is exposed per size tier through the API together with a liquidation mark price; margin is isolated in retail applications and portfolio-based via the API; settlement cycles run at 12:00 PM and 4:00 PM ET through Kalshi Klear; funding pauses if the reference feed fails; the venue exposes no public trades feed.
- Liquidity: quoted spread roughly 2bp at the touch and BTC open interest USD 4.45 million notional at the 11 July 2026 snapshot (section 6); quoted and volume-differenced effective spreads, depth at 10/25/50bp and open-interest growth are registered, not executed (data gap).
- Offshore formula used for the counterfactual, source-reported: F = P + clamp(I - P, +/-0.05%) with I = 0.01% per eight hours (Bybit funding methodology documentation, accessed 11 July 2026), verified against realized prints to 0.098bp (BTC) and 0.134bp (ETH) mean absolute error (Table C1).

Research-proposed (our operationalization, not source-reported):

- The static funding-carry used in F4 and F13, its entry at the funding instant, and the requirement to be flat whenever the published rate is zero.
- Every fee/spread ladder, depth threshold, information-share cutoff, zero-share drift tolerance and placebo percentile used in the Falsification plan; all are `research-defined`.

## Evidence

### Source-reported

Every figure below is a third-party claim from the pinned PDF, with its table/section provenance. None has been reproduced by us.

1. Funding mechanism (Table 1 and section 2.3): Kalshi uses a CF Benchmarks externally administered 1-second index, a TWAP of 480 x 1-minute premiums, no interest component, a 0.01%/8h zero threshold, a +/-2%/8h cap, funding at 04/12/20 UTC (05/13/21 UTC in standard time), 0.0001 BTC contract size, Kalshi Klear clearing, no public trades feed. Bybit uses its own premium index from impact bid/ask versus the underlying index, an average of one-minute premiums over 8h, a 0.01%/8h interest term added through a clamped adjustment, no zero threshold, an instrument-specific clamp, funding at 00/08/16 UTC, quantity in BTC with a 0.001 minimum, internal clearing, and a public trades feed.
2. Headline deadband fact (Table 2 pooled row and Figure 2 caption): 1,226 observations, zero share 0.730, mean absolute nonzero rate 1.88bp, first observation 2026-06-03; Figure 2 prints n = 1,226 with 895 zero prints; 253 of the 331 nonzero prints (76.4 percent) are negative (section 4.1).
3. Cross-section of zero shares (Table 2): KXBTCPERP 0.646 (N=113, mean absolute nonzero 1.65bp), KXETHPERP 0.770 (113, 1.84), KXSOLPERP 0.929 (113, 2.63), KXXRPPERP 0.566 (113, 2.14), KXHYPEPERP 0.643 (98, 2.06), KXBCHPERP 0.621 (95, 2.70), KXDOGEPERP 0.905 (95, 1.56), KXKSHIBPERP 0.547 (95, 1.76), KXLINKPERP 0.990 (97, 1.45), KXLTCPERP 0.674 (95, 1.35), KXSUIPERP 0.653 (95, 1.51), KXNEARPERP 0.808 (52, 1.42), KXZECPERP 0.808 (52, 1.67).
4. Offshore realized funding (Table 2): Bybit BTCUSDT 113 observations, zero share 0.000, mean absolute rate 0.38bp; ETHUSDT 113, 0.000, 0.39bp; the 13 matched symbols pooled 1,469 observations, zero share 0.000, mean absolute 0.38-2.34bp by symbol.
5. Counterfactual rule swap (Table 2 and section 4.2): Kalshi's rule applied to Bybit's own premium index gives zero share 0.000 for both BTC (N=113, mean absolute 4.72bp) and ETH (113, 4.88bp); on Bybit's native 00/08/16 UTC grid the window-average premium falls inside the one-basis-point band in 0 of 115 windows for both symbols (Appendix C sample).
6. Premium sign structure (sections 4.3 and 4.2, Table C1 footnote): Bybit BTC one-minute premium mean -4.7bp with maximum -0.07bp and range [-12.78, -0.07]bp, i.e. never positive over five weeks; ETH mean -4.9bp (Table C1 footnote: -4.88bp) with range [-35.70, +11.84]bp. Kalshi's BTC perpetual sits inside the one-basis-point band in 64.6 percent of windows; its two largest BTC excursions are +9.85bp at 04:00 UTC on 5 June and -7.94bp at 12:00 UTC on 18 June, then +2.46bp on 3 July, +2.15bp on 26 June and +2.04bp on 18 June, with nonzero prints from late June onward "between 1 and 2.5bp" and positive.
7. Decomposition validation (Appendix C, Table C1, 115 windows): reconstructing Bybit realized funding from its public premium index under the stated formula gives MAE 0.098bp (BTC) and 0.134bp (ETH), versus 4.960/4.995bp for a pure-premium model and 3.960/3.995bp for premium plus 0.01%; correlation between realized rates and window-average premiums is 0.911 (BTC) and 0.922 (ETH).
8. Listing waves and scale (sections 2.1 and 6): approval 29 May 2026; funding activated for BTC, ETH, SOL, XRP on 3 June, HYPE 8 June, a six-contract wave (BCH, DOGE, SHIB, LINK, LTC, SUI) 9 June, NEAR and ZEC 24 June, DOT/HBAR/XLM with no completed funding period at the freeze; 16 contracts listed; BTC open interest 693,877 contracts = USD 4.45 million notional, quoted spread roughly 2bp at the touch; press reports put cumulative perpetual volume above USD 16 billion by 9 July 2026 (Reuters, 2026); an industry estimate puts global perpetual volume above USD 90 trillion in 2025 versus roughly USD 28 trillion in 2023 (section 1, with no entry in the reference list).
9. Regulatory provenance (section 2.1 and references): CFTC order of approval to KalshiEX, LLC on 29 May 2026 under CEA section 5c(c)(4) and Commission Regulation 40.3, Release 9240-26, together with a Policy Statement Concerning the Listing of Perpetual Contracts; a same-day staff interpretive letter and no-action position under Regulation 30.1 for perpetual contracts treated as foreign futures, Release 9241-26 (Coinbase Financial Markets, Inc.).
10. Pre-registration (section 7): Hasbrouck information-share bounds plus Gonzalo-Granger component shares on one-second mid-quotes for BTC and ETH across Kalshi, Bybit and the constituent regulated spot venues (used individually, with the benchmark labelled a reference process), estimated daily with block-bootstrap confidence bands; robustness at 5s, 10s and event time; lead-lag confirmation via Hoffmann, Rosenbaum and Yoshida (2013); auxiliary tests of onshore-lead incidence, deadband-exit attribution, and cross-sectional zero share on activity with listing-age controls; freeze date, venue set, sampling frequency and both estimators fixed in advance, with a stated commitment that "a finding of zero onshore price discovery contribution will be reported with the same prominence as its converse".
11. What is explicitly registered rather than executed: block-bootstrap intervals for the zero shares (section 4.1); the section 4.4 rule-verification test; all microstructure descriptives including effective spread, depth and open-interest growth (section 6); the volume-recovery validation (Appendix B); the rolling-window counterfactual (section 4.2); the entire section 7 price-discovery analysis.

### Independently reproduced

- Performance figures: `not independently reproduced`. The source reports no return, Sharpe, drawdown or PnL of any kind, so there is nothing of that class to reproduce.
- What we did verify ourselves on 2026-09-28 (research-computed arithmetic on source-reported inputs and independent provenance checks, not a reproduction of the study):
  - Re-downloaded the pinned PDF and hashed it: 300,650 bytes, 11 pages, SHA-256 `4eeadfc22e955c3a431de030575be8d95f78f86e57d5380ee0e24b20d39e9b0c`; extracted 35,702 characters and read all 11 pages.
  - Table 2 per-contract observation counts sum to 1,226 (113+113+113+113+98+95+95+95+97+95+95+52+52), matching the stated pooled N.
  - The observation-count-weighted mean of the 13 printed zero shares is 0.73003, matching the printed pooled 0.730 and the Figure 2 caption 895/1,226 = 0.73002.
  - 1,226 - 895 = 331 nonzero prints and 253/331 = 0.76435, matching the printed 76.4 percent.
  - 20:00 UTC 3 June to 04:00 UTC 11 July 2026 spans 37.33 days = 112 intervals, or 113 when both endpoints are counted, consistent with the printed N = 113 per launch contract.
  - Section 6 arithmetic: 693,877 contracts x 0.0001 BTC = 69.3877 BTC, and USD 4.45 million / 69.3877 implies about USD 64,132 per BTC, which reproduces the "roughly six dollars of notional" contract statement (0.0001 x 64,132 = USD 6.41).
  - The paper's reference list contains 14 entries counted entry by entry, against the landing heading "0 References".
  - A whole-document word scan reproduces the cost-treatment conclusion recorded in Provenance (zero hits for transaction cost, slippage, backtest, Sharpe, turnover, capacity, borrow, latency, fill, participation, market impact, liquidity, pnl).
  - The cited CFTC order URL and press release both return HTTP 200.
  - Scope: none of the above validates the paper's empirical claims about premium distributions, zero shares or price discovery; only the internal arithmetic and the provenance were checked.

### Negative evidence

1. The source proposes no trading rule at all: zero occurrences in the pinned PDF of transaction cost, slippage, backtest, Sharpe, turnover, capacity, borrow, latency, fill, participation, market impact, liquidity or PnL, and the only two occurrences of "strategy" are the phrase "identification strategy" in the AI disclosure - so there is no source-reported cost model, return or risk metric anywhere (data gap, not zero).
2. Funding is transferred in only 27.0 percent of intervals: 73.0 percent of 1,226 prints are exactly zero, so a passive on-venue funding-carry receives or pays in roughly one interval in four (Table 2, Figure 2).
3. Conditional on activation the transfer is marginal: mean absolute nonzero rate 1.88bp per eight hours, "barely above the 1bp threshold" in the source's own words (section 4.1), with the mass of the distribution clipped by the band.
4. The active tail is one-sided and possibly non-stationary: 253 of 331 nonzero prints (76.4 percent) are negative over the pooled sample (section 4.1), while section 4.3 states late-June prints are persistently small and positive - see the frontmatter contradictions; no subperiod table exists to adjudicate the sign.
5. The cross-section of zero shares spans 54.7 percent (SHIB) to 99.0 percent (LINK) with SOL at 92.9 percent and DOGE at 90.5 percent (Table 2), and the source itself warns this cross-section is confounded by listing age (sections 4.1, 5 and 6).
6. The deadband is not the cause of the zeros: applying Kalshi's rule to Bybit's own premium index yields 0.0 percent zeros in 113 windows on Kalshi's clock and 0 of 115 windows on Bybit's clock (section 4.2) - so the near-zero onshore premium is a venue property, and the finding does not transfer to any venue whose premium trades away from its index.
7. The interpretive question is left unresolved by the source: H-tight and H-anchor are explicitly "observationally equivalent at funding frequency" (section 5), and the discriminating test is pre-registered for execution on or after 12 September 2026, i.e. it does not exist as of this record.
8. If H-anchor survives, the onshore venue contributes approximately nothing to price discovery (sections 1, 5 and 7), which by construction eliminates lead-lag, information-share and microstructure alpha on this venue.
9. No statistical inference is reported for the headline fact: there are no t-statistics, p-values, confidence intervals or standard errors for the 73.0 percent zero share or for any cross-sectional comparison; block-bootstrap intervals are explicitly deferred to the registered analysis (section 4.1).
10. The section 4.4 verification that realized prints equal the disclosed "clamp then snap" rule is registered, not executed - the paper's central mechanism is asserted from documentation and not yet checked against collected mid-quotes.
11. The exchange-side price series entering the one-minute premium candles (trade, mark or midpoint) is explicitly "not fully specified in the public documentation" (section 2.3) - `underspecified`.
12. Funding pauses when the CF Benchmarks feed is unavailable (section 2.3), so observations can be missing not at random; no pause count is reported (data gap).
13. Kalshi exposes no public trades feed, so volume is recoverable only by differencing cumulative fields, and the Appendix B validation is deferred to the registered version (data gap).
14. Sample length: five weeks of funding (3 June - 11 July 2026) covering the venue's first six weeks of life, with no out-of-sample period, no second venue-regime and no completed order-book sample - regime stability is untested.
15. The offshore comparator is a single venue (Bybit) over the same five weeks; the persistent -4.7bp discount is attributed by the source to a possible drawdown-regime carry channel that "the funding data alone do not identify" (section 4.3).
16. Offshore realized funding of mean absolute 0.38bp is an artifact of near-cancellation between a negative premium and a positively clamped adjustment term (section 4.3, Table C1); the source's own warning is that small realized offshore funding is not evidence of a tight basis - this invalidates the most common shortcut in funding-carry comparisons.
17. Venue scale is tiny: BTC open interest USD 4.45 million notional and roughly 2bp quoted spread at the touch (section 6); capacity for any on-venue strategy is unassessed and evidently sub-scale (data gap).
18. The three headline market-scale claims are partly secondary: cumulative volume above USD 16 billion is attributed to Reuters (9 July 2026), and the USD 90 trillion / USD 28 trillion global perpetual-volume figures are "industry estimates" with no corresponding entry in the 14-item reference list.
19. Pre-registration date arithmetic does not close: eight weeks from the 11 July 2026 collection start is 5 September 2026, not "on or after 12 September 2026" (section 7 versus section 1 and Appendix A).
20. Reproducibility: "Data and code sufficient to reproduce all tables and figures are available from the author" - there is no public repository, no replication-package DOI and no committed dataset (data gap).
21. Source quality: single independent researcher, AI-assisted (Anthropic Claude) code, pipeline and drafting, no peer-review statement, no journal or issue, no funding, no competing interests, 0 citations and 44 downloads at read time (SSRN landing, 2026-09-28), and an SSRN landing that prints "0 References" against 14 printed references.
22. The paper's own interpretive framing licenses no directional trade: either H-tight or H-anchor being true is described by the source as "informative for design" (section 5), not as an edge.
23. No third-party replication, commentary or citation of this paper was identified in a repository and Wiki Brain search on 2026-09-28; absence is not evidence that no negative result exists elsewhere.

## Falsification plan

Every threshold below is `research-defined` (our acceptance/failure cutoffs); every operational substitution not in the source is `research-proposed`.

- F1 Headline reproduction gate (`research-proposed` pull): re-fetch the Kalshi funding history for 2026-06-03 to 2026-07-11 from `external-api.kalshi.com/trade-api/v2/margin/` and recompute the pooled zero share. Fail if the observation count is not 1,226 or the zero share differs from 73.0 percent by more than 1.5 percentage points (`research-defined`). Action: record a reproduction failure and stop downstream consideration.
- F2 Extended-sample stability: extend the funding history to at least 26 weeks spanning the registered analysis window. Fail if the pooled zero share moves by more than 10 percentage points from 73.0 percent (`research-defined`). Action: treat deadband activation as a launch-phase artifact rather than a stable venue property.
- F3 Multi-venue counterfactual: re-run the Kalshi rule on the premium series of at least three offshore venues (Bybit plus two of Binance, OKX, Deribit) over the identical window. Fail if any venue produces a zero share above 10 percent (`research-defined`). Action: weaken the source's "venue property, not rule property" conclusion.
- F4 Funding-carry economics ladder (`research-proposed` static carry, funded only on nonzero prints): compute gross funding harvested per interval and annualized, then apply taker-fee-and-spread ladders of 0/1/2/5 bps per side (`research-defined`). Fail if annualized net funding yield is not positive at 2 bps per side. Action: reject funding carry on this venue as unviable.
- F5 Active-tail sign stability: over at least 26 weeks, recompute the share of nonzero prints that are negative (source reports 76.4 percent). Fail if that share falls below 50 percent (`research-defined`). Action: treat the sign of the active tail as regime-dependent and refuse to fix a carry direction from this sample.
- F6 Price-discovery adjudication (executes the source's own section 7 pre-registration): Hasbrouck bounds plus Gonzalo-Granger shares at 1s on Kalshi/Bybit/constituent spot venues with block-bootstrap bands. Fail the satellite claim if Kalshi's lower-bound information share is strictly positive with a bootstrap interval excluding zero on at least 60 percent of days (`research-defined`). Action: if the satellite reading survives, block any lead-lag or information-share alpha on this venue.
- F7 Onshore-lead incidence: count Kalshi mid leading the index and the offshore complex at 1-60s horizons. Fail H-anchor if onshore-lead incidence exceeds 1 percent of sampled seconds with a bootstrap interval excluding the exchangeable null (`research-defined`). Action: reclassify the venue as independently informative and re-open the alpha question.
- F8 Rule verification (source-registered section 4.4): reconstruct the eight-hour TWAP premium from collected mid-quotes and the reference index and compare with realized prints under clamp-then-snap. Fail if more than 5 percent of intervals disagree by more than 0.5bp (`research-defined`). Action: treat the disclosed rule as not the operative rule and re-audit every headline number.
- F9 Feed-failure audit: count funding intervals in which the CF Benchmarks feed was unavailable and funding therefore paused. Fail if paused intervals exceed 5 percent of the sample (`research-defined`). Action: restate the zero share net of pauses, since a pause also prints no payment.
- F10 Cross-sectional activity test (source-registered): regress contract-level zero share on venue activity with listing-age controls. Fail the "activity loosens the anchor" prediction if the activity coefficient is not negative with |t| >= 1.96 (`research-defined`). Action: drop activity as an explanation of the cross-section.
- F11 Venue-scale and capacity gate: measure quoted spread and depth at 10/25/50bp in dollar notional. Fail if the median quoted spread exceeds 5bp or depth at 25bp is below USD 250,000 notional (`research-defined`). Action: mark any on-venue carry capacity-sub-scale regardless of its funding economics.
- F12 Second-comparator decomposition check: repeat the realized-funding reconstruction on Binance and OKX premium series. Fail if the stated-formula mean absolute error exceeds 1bp on either venue (`research-defined`). Action: treat the "small realized offshore funding is not a tight basis" warning as Bybit-specific.
- F13 Frozen forward test: from 2026-10-01, run the `research-proposed` static carry forward for 12 months with no retuning. Fail if cumulative net funding at 2 bps per side is not positive. Action: reject the carry hypothesis outright.
- F14 Variance-matched deadband placebo: simulate one-minute premiums as white noise calibrated to Kalshi's observed premium variance, pass them through the disclosed rule (8h TWAP, +/-2% clamp, 0.01% snap), and build a 1,000-draw distribution of zero shares. Fail the index-tracking interpretation if 73.0 percent falls inside the central 95 percent of that null (`research-defined`), i.e. the zero share is explained by variance alone. Action: attribute the deadband frequency to dispersion rather than to basis discipline.

## Crypto portability

`direct`. The evidence is itself crypto: BTC, ETH, SOL, XRP and eleven other crypto perpetual futures on a US regulated venue, with an offshore crypto perpetual as the comparator. Portability risks that remain open even inside this direct setting:

- spot versus perpetual: the reference index aggregates regulated spot venues while the traded object is a linear USD-margined perpetual; the source does not state whether account eligibility, position limits or US-person restrictions bind (data gap).
- funding: the mechanism itself - an 8-hour transfer censored at +/-1bp with no interest baseline, versus an offshore formula whose interest term and clamped adjustment nearly cancel.
- 24/7 session structure and candle boundaries: an Eastern-Time funding grid that shifts by one hour each November against a UTC offshore grid; the shift and the four-hour stagger are identification, but they also mean funding timestamps do not align across venues.
- venue fragmentation: Kalshi, Bybit and the constituent regulated spot venues of the CF Benchmarks index; the benchmark is an aggregation of constituent prices and "not an independent trading venue" (section 7).
- liquidity: BTC open interest USD 4.45 million notional and roughly 2bp quoted spread at the touch at the sample freeze; depth and effective spread are registered, not measured.
- mark / index price: funding and settlement both anchor to CF Benchmarks BRTI rather than to a venue mark or last price, and funding pauses if that feed fails.
- contract specification: 0.0001 BTC per contract, leverage tiers exposed per size tier, isolated margin in retail and portfolio margin via API, settlement twice daily through Kalshi Klear.
- custody, venue and regulatory risk: a CFTC-designated contract market and DCO are a different failure surface from an offshore venue, and the source provides no account-eligibility or withdrawal analysis (data gap).

Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: the entire strategy layer - entry, exit, holding period, sizing, order type, fill model, latency, fee/spread model, borrow, leverage rule, capacity and tax treatment - because the source proposes no strategy.
- `data gap`: no public code or dataset (author-on-request only); no replication-package DOI; no pause counts for the reference-feed failure mode; no validated volume series; no depth, effective-spread or open-interest-growth results; no block-bootstrap intervals; no t-statistics or confidence intervals anywhere; peer-review and publication status not stated.
- `not independently reproduced`: every empirical claim about premium distributions, zero shares, the counterfactual and the decomposition; only internal arithmetic, file hashes, a word scan and two HTTP checks were performed by us.
- `unproven`: both H-tight and H-anchor, and any implication either has for a tradable edge, until the pre-registered section 7 analysis is executed and reported.
- Internal inconsistencies: four, listed in frontmatter, all unreconciled by the source.
- Source quality: a first-look, single-author, AI-assisted SSRN working paper with no peer review, no journal, 0 citations and 44 downloads at read time, whose central verification tests are deliberately deferred.
- Sample risk: five weeks, one venue in its first six weeks of life, one offshore comparator, one asset class configuration - external validity is minimal.
- Incremental value of this capture is the falsification story for funding-carry and price-discovery hypotheses on a newly regulated venue (deadband censoring, counterfactual rule swap, the near-cancellation decomposition that invalidates naive offshore funding comparisons, and a pre-registered information-share adjudication), not a tradable signal.
- Dedup: canonical source identity is unique in this repository; mechanism-adjacent records are listed below and differ in source identity and in at least one of mechanism, signal construction, universe/market type or horizon.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no strategy family, no Qlib or other backtest run of our own, no Paper, Testnet or Live activity, no candidate-pool entry, no Hermes Wiki Brain write, and no Kanban task. The only local actions taken by this run were downloading and reading the pinned SSRN PDF, hashing it, scanning its text, recomputing its printed arithmetic and checking the cited CFTC URLs. The source itself contains no implementation - only an exchange data collector described in Appendix A.

## Adoption boundary

Presence of this record in the staging repository means only normalized research material. It does not mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed any full-backtest validation of ours; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. The source reports no returns, so nothing here is a performance claim. Crypto portability is `direct` and is not authorization to trade. Any adoption, implementation or approval decision must be a separate, explicit, reviewed step based on this record plus current sources.

## Related Wiki records

Repository records (same broad family, different source identity and mechanism):

- [[hyperliquid-cex-cross-venue-funding-spread-carry-2026-09-03]] - Tony Lau, SSRN 6993978, a static short-Hyperliquid / long-CEX funding-spread carry with significance tests; different source, and the mechanism is a cross-venue funding-rate differential between two offshore venues rather than an onshore deadband design plus a price-discovery adjudication.
- [[crypto-funding-rate-feedback-regime-capital-stability-band-2026-09-12]] - a theoretical funding feedback rule with a capital-dependent stability band evidenced on 200 Binance perpetuals; different source, equilibrium-theory mechanism, and offshore venue set.
- [[crypto-perpetual-spot-cross-venue-lead-lag-vecm-2026-09-01]] - cross-venue lead-lag/price-discovery between perpetual and spot; adjacent to this record's pre-registered information-share test but a different source, different venue pair and executed rather than pre-registered.
- [[btc-perp-single-venue-funding-carry-taker-fee-falsification-2026-09-14]] - single-venue funding carry with a taker-fee falsification on an offshore venue without a deadband; different source and different funding design.
- [[crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]] - Kalshi as a venue but prediction markets, not perpetual futures; different instrument class and mechanism.
- [[bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01]] - same author (Boon Chuan Lim, SSRN 6592830) but a different paper and a materially different mechanism: US spot-ETF net-flow drift.
- [[hyperliquid-wallet-cross-venue-anticipatory-flow-binance-btc-perp-2026-09-15]] - same author (Research Square DOI 10.21203/rs.3.rs-10147582/v1) but a different paper and a materially different mechanism: wallet-level cross-venue informed flow.

Hermes Wiki Brain pages (verified read-only via `kb_search` on 2026-09-28):

- [[quant/crypto-funding-rate-feedback-regime-capital-stability-band-2026-09-12]]
- [[quant/crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]
- [[quant/hyperliquid-cex-cross-venue-funding-spread-carry-2026-09-03]]
- [[quant/crypto-perpetual-linear-inverse-quanto-convexity-bjork-identity-falsification-2026-09-13]]
- [[quant/crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12]]
- [[quant/crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]]

No Wiki Brain page exists for this source identity; the pages above are adjacent (funding design, cross-venue carry, price discovery, Kalshi) and were not used to fill any field in this record.

## Sources

- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7098201 - SSRN landing page, read in a browser session on 2026-09-28 after the Cloudflare interstitial cleared: title, sole author "Boon Chuan Lim / Independent Researcher", "11 Pages", "Posted: 28 Jul 2026", "Date Written: July 11, 2026", suggested citation dated July 11 2026, license "All rights reserved. No reuse allowed without permission.", heading "0 References", heading "0 Citations", DOWNLOADS 44, ABSTRACT VIEWS 165, no journal/issue and no peer-review statement.
- https://doi.org/10.2139/ssrn.7098201 - canonical DOI printed in the suggested citation.
- Pinned full text: the SSRN `Delivery.cfm` PDF link exposed by the landing page's "Open PDF in Browser" button, retrieved 2026-09-28, 300,650 bytes, 11 pages, SHA-256 `4eeadfc22e955c3a431de030575be8d95f78f86e57d5380ee0e24b20d39e9b0c`; all 11 pages read including the abstract, sections 1-8, Table 1, Table 2, Figure 1-2 captions, Appendices A-C, Table C1, the disclosure block and the reference list. No presigned or session-bound URL is stored in this record.
- https://www.cftc.gov/filings/documents/2026/orgdcmkexbtxperporder26601.pdf - CFTC order of approval cited by the source; independently confirmed reachable (HTTP 200, 179,109 bytes) on 2026-09-28, not read for this record.
- https://www.cftc.gov/PressRoom/PressReleases/9240-26 - CFTC release cited by the source; independently confirmed reachable (HTTP 200) on 2026-09-28, not read for this record.

Literature and documentation cited inside the source (recorded only as the source's own references, not independently read for this record): Ackerer, Hugonnier and Jermann (2025); Alexander, Choi, Park and Sohn (2020); Bybit funding methodology documentation (accessed 11 July 2026); CFTC (2026) Release 9240-26; CFTC staff (2026) Release 9241-26; Gonzalo and Granger (1995); Hasbrouck (1995); Hayashi and Yoshida (2005); Hoffmann, Rosenbaum and Yoshida (2013); He, Manela, Ross and von Wachter (2024); Kalshi contract-specification and funding help articles (archived at archive.ph 2026-07-11); Makarov and Schoar (2020); Reuters (9 July 2026); Shiller (1993).
