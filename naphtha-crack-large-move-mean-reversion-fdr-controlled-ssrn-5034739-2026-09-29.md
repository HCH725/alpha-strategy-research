---
schema: strategy-research-record-v1
title: "Naphtha Crack Large-Move Mean Reversion with FDR-Controlled Threshold Backtests (SSRN 5034739)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - commodity
  - energy
  - mean-reversion
  - pairs-trading
  - otc
  - statistical-arbitrage
  - multiple-testing
status: research-only
confidence: medium
source_as_of: 2025-05-19
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5034739"
  - "https://doi.org/10.2139/ssrn.5034739"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "C1 dates: SSRN landing 'Posted: 27 Nov 2024 / Last revised: 19 May 2025' and 'Date Written: November 26, 2024' against PDF /CreationDate D:20250511062754Z and /ModDate D:20250519225646+02'00', plus a second SSRN version 5032815 (37 pages, posted 25 Nov 2024) versus 5034739 (43 pages, posted 27 Nov 2024); no journal, issue or acceptance statement anywhere in the source."
  - "C2 ADF: section 3.2 states 'We cannot reject the null hypothesis for all three standardisation methods' while Table 1 prints aDF statistics -10.70 / -30.14 / -22.86 / -34.16 (which reject a unit root at conventional levels) and the same paragraph concludes 'The stationarity of the series justifies the use of the k-fold cross-validation procedure'."
  - "C3 EWMA smoothing: sections 3.2 and Appendix B fix the EWMA alpha at 0.2, while Tables 2, A.3, A.4 and E.5 print rows labelled 'EWMA alpha' containing both 0.15 and 0.2."
  - "C4 selection set: section 5.3 states three criteria (win rate > 50%, positive net profit, share of successful cross-validations >= 80%); applying them to the printed Appendix A.3/A.4 rows yields 10 qualifying strategy ids (A.3: 3,4,15,16,19,23; A.4: 9,13,14,21) but Table 2 prints only 7 (ids 3,4,19,23,9,13,21) and no further exclusion rule is stated."
  - "C5 combinatorics: section 5.3 says 'We run cross-validations for 24 combinations of performance measure, scaling type, and entry strategy' = 2 x 3 x 2 = 12; 24 requires the EWMA alpha factor that the sentence omits."
  - "C6 rounding: section 5.3 prints '$0.19/bbl net profit per trade' as the 12-strategy Profit-per-Trade average; research-computed from the printed Appendix A.4 column = 0.19546, which rounds to 0.20."
  - "C7 dispersion: section 5.3 states stop-loss/take-profit 'decreases the standard deviation of the average win rates across the selected strategies (from 8% to 6%)'; research-computed from the printed win rates = 7.78 pp without stop-loss/take-profit and 4.29 pp (population) / 4.63 pp (sample) with them."
  - "C8 Sharpe justification: section 5.1 withholds the Sharpe ratio because 'the downside is strictly capped' by the stop-loss and take-profit, but section 5.3 and Appendix E conclude 'The no-stop-loss and no-take-profit strategy remains the best performing combination', i.e. the selected best strategies have uncapped downside."
  - "C9 reference count: the pinned PDF reference list contains 32 year-bearing entries counted entry by entry, while the SSRN landing page displays '33 References'."
---

# Naphtha Crack Large-Move Mean Reversion with FDR-Controlled Threshold Backtests

## Provenance

- **Primary source:** Briac Turquet (ETH Zurich, D-MTEC), Pierre Bajgrowicz (Axpo Solutions AG) and Olivier Scaillet (University of Geneva, Geneva Finance Research Institute, Swiss Finance Institute), *"Mean Reversion Trading on the Naphtha Crack"*, SSRN working paper.
- **Stable URL / identity:** `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5034739` - DOI `https://doi.org/10.2139/ssrn.5034739`.
- **Author block verified:** the three affiliations printed on PDF page 2 (ETH Zurich D-MTEC; Axpo Solutions AG; University of Geneva / GFRI / SFI) match the SSRN landing author lines exactly; the PDF prints `turquet18.briac@gmail.com`, `pierre.bajgrowicz@gmail.com`, `olivier.scaillet@unige.ch`; no ORCID is printed in either place.
- **Version / dates (all source-reported, unreconciled - see C1):** SSRN landing `43 Pages`, `Posted: 27 Nov 2024`, `Last revised: 19 May 2025`, `Date Written: November 26, 2024`, `There are 2 versions of this paper` (the other version is `abstract_id=5032815`, 37 pages, posted 25 Nov 2024); pinned PDF `/CreationDate D:20250511062754Z`, `/ModDate D:20250519225646+02'00'`, `/Author "Olivier Scaillet"`, `/Title "Main copy"`, `/Creator Preview`, `/Producer "macOS Version 14.7.5 (Build 23H527) Quartz PDFContext"`.
- **Publication status:** SSRN working paper. No journal name, volume, issue, DOI other than the SSRN DOI, or acceptance statement appears in the source, so publication status is `not stated in source`. The acknowledgements do thank "the Editor and the referee for constructive criticism and numerous suggestions which have led to substantial improvements over the previous version", which implies a journal review process without identifying a journal.
- **Landing metrics (read in a browser session 2026-09-29):** 417 downloads, 1,394 abstract views, 0 citations, 33 References, licence `All rights reserved. No reuse allowed without permission.`, JEL `G13, G14, G15, G17, G18`. Because of that licence this record normalises and cites short printed values only; no substantial source text is reproduced.
- **Pinned primary text:** the PDF was obtained through the landing page's own `Download This Paper` / `Open PDF in Browser` delivery link (`papers.ssrn.com/sol3/Delivery.cfm/5034739.pdf?abstractid=5034739&mirid=1`) with no expiring or presigned token stored in this record: **2,518,214 bytes, 43 pages, SHA-256 `e1bbd9550c0dd53c08fd8b81ac4cc84fc09fd14f884cae3470556383d231e758`**. pypdf 6.16.2 extraction produced 95,889 characters / 1,506 lines (151 NUL artefacts stripped, 96,751 clean bytes) read end to end: title block and abstract, Sections 1-6, equations (1)-(9), Figures 1-6 and their captions, Table 1 (p. 12), Table 2 (p. 25), Section 3.3 fee structure (p. 13), Section 5.1-5.5, Appendix A Tables A.3 (p. 29) and A.4 (p. 30), Appendices B, C, D, Appendix E with Tables E.5/E.6 (p. 38) and E.7 (p. 39), the 32-entry reference list (pp. 39-42) and the SFI back cover.
- **Sample / data as-of:** daily end-of-day settlement prices `15/05/2014 to 14/02/2024` obtained from ICE for the European naphtha crack *Naphtha CIF NWE Cargoes (Platts) vs Brent 1st Line Future* (section 3.2); data start 2014 because that is when naphtha swaps started clearing on the exchange.
- **Repository deduplication (hidden-inclusive, before writing):** `rg -uuu -i` over the entire checkout (including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` at 1,088,787 bytes) for `5034739`, `5032815`, `naphtha`, `Turquet`, `Bajgrowicz`, `Scaillet`, `CIF NWE` returned exactly one file, `crypto-index-volatility-timing-regime-conditional-alpha-fire-70080-2026-09-27.md`, and its single hit is an unrelated reference-list line citing "Scaillet et al. (2020)"; `naphtha` has 0 hits in `coverage_manifest.csv`; positive control `novy-marx` returned 30 files before this write and 31 after, the +1 being this record's own citation of the control term. `git log --oneline -20` was used only as a convenience glance, not as the dedup mechanism. The identity scan was re-run after the final `git pull` and returns exactly one file: this record.
- **Four-axis material-distinction statement vs the nearest existing repository records:** (1) `crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12.md` - different source, different instrument (3:2:1 RBOB/HO/WTI refinery margin versus the two-leg European naphtha-Brent OTC crack), different signal construction (deseasonalised OU with a stop-lockout state machine versus non-parametric Stanton drift estimation plus an absolute-standardised-move threshold grid); (2) `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md` - different source and mechanism (Johansen cointegration on crush spreads); (3) `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23.md` - different source, different market (day-ahead power) and different horizon; (4) `commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02.md` - different source, graph-learning signal on exchange-traded calendar spreads; (5) `commodity-seasonal-dvr-ssa-rlssa-benchmark-null-2026-09-14.md` - different source and a seasonality (not large-move) mechanism. Universe/market type, signal construction and material data dependency (ICE/Platts OTC settlement series) all differ from every adjacent record.
- **Boundaries observed:** no Wiki Brain write, no Kanban task, no backtest run, no market data downloaded, no dependency installed; `not independently reproduced` is stated verbatim below; hard cap 1 record this run.

## Economic mechanism

### Source-reported

The naphtha crack is the difference between an OTC-traded petroleum product outright (Platts daily assessment for *Naphtha CIF NWE Cargoes*) and an electronically traded crude outright (ICE *Brent 1st Line Swap Future*); the contract is cash settled monthly on the average of that difference (section 3.1). The paper argues the two legs sit in structurally different market structures: Brent futures are electronic (about 97% of daily volume in H1 2024), traded by a wide participant set including algorithmic and high-frequency traders, with prompt-month volume of about 111 million bbl per day in H1 2024, while naphtha swaps transact almost entirely through brokers as block trades (more than 99% of daily traded volume over the first six months of 2024) among a smaller pool of physical players (oil majors, trading houses, refiners, terminal operators), with prompt-month volume of about 1.4 million bbl per day in H1 2024 (section 3.1, PDF p. 10). Retail investors are stated to be absent from naphtha because of registration, clearing and broker-approval barriers.

The paper's stated mechanism is a temporary Law-of-One-Price deviation between the fast electronic leg and the slow broker-mediated leg: naphtha prices "need more time to adjust" because they transact through brokers connecting a smaller number of actors, so a Brent move is not fully mirrored in naphtha at the 19:30 London settlement snapshot, while naphtha liquidity peaks during the Platts Market-On-Close assessment ending at 16:30 London (sections 3.3 and 5.5). Two further source-stated causes are (i) low naphtha liquidity alone, where a large trade slips beyond fair value and reverts within about a day, and (ii) naphtha being traded as a spread to gasoline or propane, so sharp moves in those markets temporarily displace the crack (section 5.5).

Empirically the source reports a non-parametrically estimated drift of the standardised daily crack change that becomes increasingly negative/positive (i.e. reversion strengthens) in a non-linear fashion once the absolute daily move passes roughly `$1/bbl`, with an inflexion point whose exact location depends on the standardisation method and the sign of the move (section 4.2, Figure 4), and a diffusion term that rises with the size of the move (section 4.3). Monte Carlo simulations over 10,000 paths seeded above a `$1.6/bbl` threshold show that "most of the reversion takes place on the first day" and that holding beyond day one reduces profits for two of the three standardisation methods (section 4.4, Figure 6).

### Research interpretation

The falsifiable hypothesis is **microstructure lag mean reversion in a two-leg commodity spread**: a large one-day move in the spread is partly an artefact of asymmetric execution speed and liquidity between an electronic leg and a broker/assessment leg, so the spread should revert toward its recent equilibrium within a few sessions, and the reversion magnitude should exceed round-trip trading costs.

Component roles (single strategy, no regime filter claimed by the source):

```text
Signal input:   daily crack change standardised by a volatility measure
                (20-day rolling sd, 60-day rolling sd, or 1-day-ahead GARCH(1,1)),
                EWMA-smoothed and re-scaled to the raw scale
Threshold:      absolute standardised move above a calibrated level ($0.8-$2.0/bbl grid)
Entry:          immediate (same day) or delayed (one session later), reverting direction
Exit:           fixed holding period 1-5 sessions, or stop-loss at -$1.5/bbl,
                or take-profit at +$3/bbl (both optional and ablated by the source)
Risk/sizing:    not specified by the source for the main backtest
                (Appendix E alone assumes a fixed 100-lot position for drawdown work)
```

Research interpretation of why it may fail: the effect is only observable at a settlement snapshot that is itself an administered assessment (Platts MOC) rather than a tradable quote, the selected strategies trade 1-4 times per year, and the paper's own universe average and randomly entered benchmarks lose money after costs. Any of these can erase the reported edge without the mechanism being false, which is why the falsification plan below separates mechanism tests from execution tests.

## Signal

Everything in this section is source-reported unless explicitly marked `research-proposed` or `research-computed`.

- **Formation timestamp:** daily end-of-day settlement of the crack series; naphtha swaps settle at 19:30 London time to match Brent futures settlement (section 3.2). Platts MOC assessment ends at 16:30 London (section 3.3). Timezone is stated as London throughout; no point-in-time/availability lag is modelled beyond that.
- **Raw change:** `DeltaRaw_t = C_t - C_{t-1}` with `C` the crack price in $/bbl, equation (1) (section 3.2).
- **Standardisation:** `Delta_t = DeltaRaw_t / Vol(R_t) * std(R_t) / std(S_{t-1})`, equation (2), with `Vol` one of (i) 20-day rolling historical standard deviation, (ii) 60-day rolling historical standard deviation, (iii) one-day-ahead GARCH(1,1) forecast (Bollerslev 1986); `S_{t-1}` uses only data through `t-1` "so as to avoid any look-ahead bias". An EWMA smoothing of the volatility series is applied with alpha fixed at 0.2 in sections 3.2 and Appendix B, but Tables 2/A.3/A.4/E.5 print both 0.15 and 0.2 (contradiction C3).
- **Roll rule:** the series transitions to the next-month contract **5 exchange business days ahead of expiry** (prompt month from the start of the month to 5 business days before expiry, second-month contract over the last 5 days), explicitly to avoid expiry squeeze noise and to avoid rolling an open position across contract months (section 3.2).
- **Warm-up:** `L = 200` days are discarded to initialise the GARCH(1,1) model (section 5.1, equation (8)-(9)).
- **Entry - immediate (source):** enter a reverting position on the day the standardised daily change exceeds a calibrated threshold; 6 of the 7 selected strategies use this entry (Table 2).
- **Entry - delayed (source):** wait one session after the trigger, then enter the reverting position.
- **Exit (source):** hold for a calibrated number of sessions; grid = 1-5 sessions for immediate entry and 1-4 sessions for delayed entry, chosen so no position is ever rolled across contract months (section 5.2).
- **Risk exits (source):** stop-loss if an open position exceeds a `$1.5/bbl` loss and take-profit if it exceeds a `$3/bbl` gain (section 5.1); Appendix E additionally ablates static versus volatility-dependent (dynamic) versions with stop-loss ranges `[-1.5,-0.5]` (tight) and `[-2,-1]` (relaxed) and take-profit range `[2.5,3.5]`.
- **Threshold grid (source):** `$0.8` to `$2.0` in `$0.1` steps = 13 values; 13 x 5 = 65 combinations for immediate entry and 13 x 4 = 52 for delayed entry (section 5.2; arithmetic re-checked).
- **Selection layer (source):** for each combination of performance measure x standardisation x entry type x EWMA alpha (2 x 3 x 2 x 2 = 24 variants, arithmetic re-checked), threshold and holding period are chosen on the 80% calibration fold using (i) a one-sided z-test of mean return > 0 at `alpha = 0.05` and (ii) Benjamini-Hochberg False Discovery Rate control set at **10%** under a block-dependence assumption, following Bajgrowicz and Scaillet (2012); the surviving combination with the best value of the chosen performance measure is then evaluated on the 20% validation fold.
- **Performance measures (source):** `Phi_total` = sum of raw daily crack changes while in position, equation (8); `Phi_per_trade` = that total divided by the number of trades, equation (9). Both are computed on **raw** price changes even though signals use standardised changes; results are annualised as total profit per year in $/bbl. The Sharpe ratio is explicitly **not** used (section 5.1: "we do not use volatility-dependent performance measures such as the Sharpe ratio since the downside is strictly capped" - see contradiction C8).
- **Validation design (source):** 5-fold cross-validation, 80% calibration / 20% validation, motivated by the claimed stationarity of standardised deltas and the short horizon; no position may be initiated during the 5 sessions preceding a fold boundary (section 5.1). This is random-fold cross-validation on a time series, **not** walk-forward; `walk-forward`, `holdout` and `placebo` return 0 occurrences in the pinned text.
- **Position sizing:** **underspecified.** The main backtest reports profit in $/bbl with no position size, capital base or return-on-capital denominator; Appendix E alone assumes "a unique size for the positions of 100 lots (i.e., 100,000 barrels)" and a starting capital equal to a multiple of a ~$100,000 1-day 95% VaR.
- **Re-entry rules:** not stated beyond the fixed holding period and the fold-boundary exclusion; `underspecified`.

## Required data

- **Instrument:** European naphtha crack = *Naphtha CIF NWE Cargoes (Platts) minus Brent 1st Line Future*, cash-settled monthly contract cleared on ICE, quoted in $/bbl (section 3.1).
- **Universe:** a single instrument, no screen, no reconstitution; the paper notes ICE daily history begins in 2014 because that is when naphtha swaps began clearing, and that pre-2014 data "could probably be obtained from brokers" but would need cleaning because reporting was not then mandatory (section 3.2).
- **Venue / data vendor:** ICE historical daily end-of-day settlement prices, plus the Platts daily assessment price for the naphtha leg; both are licensed commercial data.
- **Timeframe / fields:** daily close-to-close crack price in $/bbl, 15/05/2014-14/02/2024; no OHLCV, no order book, no trades, no funding, no open interest, no borrow.
- **Point-in-time:** settlement timestamps stated as 19:30 London for naphtha swaps and aligned Brent settlement; no revision/availability lag treatment is described for the Platts assessment, and no staleness or missing-data rule is stated (`data gap`).
- **Missing data:** no null/stale/suspended handling is described anywhere in the pinned text (`data gap`).
- **Fees/spread/borrow needs:** a fee model is supplied by the source (see Execution assumptions); borrow, funding and leverage data are not used (0 modelled occurrences).

## Execution assumptions

Cost determination was made from a Methods-level read of sections 3.3, 5.1, 5.2, 5.4 and Appendix E plus a whole-document term census of the pinned text.

- **Source modelled costs (section 3.3, PDF p. 13):** bid-ask on the naphtha crack "typically ranges between `$0.05/bbl` and `$0.10/bbl` during most of the day"; typical broker fee `$0.01/bbl` one-way; ICE clearing fee for this contract `$0.001/bbl` one-way; "we assume total one-way transaction costs of `$0.10/bbl` when evaluating trading strategies"; "in case a stop-loss is triggered, we add an additional `$0.20/bbl` for extra slippage"; negligible fixed costs such as exchange subscription fees. Figure 6's caption quotes round-trip trading costs of `$0.20/bbl`, which reconciles with 2 x $0.10 (arithmetic re-checked).
- **Order type / fill model:** **not stated in source.** The paper describes when prices are observed but never states market versus limit orders, signal-to-order delay, same-bar versus next-bar execution, partial fills, latency, participation caps or venue choice; all of these are `data gap`, never zero.
- **Terminal census (pinned text):** `transaction cost` 11, `bid-ask` 3, `slippage` 3, `clearing fee` 3, `broker fee` 1, `liquidity` 16, `drawdown` 15, `stop-loss` 55, `take-profit` 30, `win rate` 21, `false discovery rate` 3, `cross-validation` 16, `out-of-sample` 2, `sharpe ratio` 1; while `turnover`, `market impact`, `leverage`, `funding`, `latency`, `fill`, `walk-forward`, `holdout`, `placebo` and `deflated` all return **0**. The 6 hits for `margin` are "refinery margins" / "marginally" and the 1 hit for `capacity` is "storage capacity", so financial margin, leverage and trading capacity stay `data gap`; the 2 hits for `commission` are the titles "The European Commission" / "Commission Delegated Regulation", so commission-as-fee is 0 modelled occurrences.
- **Access friction not priced:** registration, clearing-entity approval and broker onboarding are described as a "significant barrier to entry" with retail investors absent (section 3.1); onboarding, inventory and financing costs of maintaining broker access are not modelled.
- **Research interpretation of the cost assumption:** `$0.10/bbl` one-way exceeds the half-spread midpoint plus fees (0.05-0.10 full spread -> 0.025-0.05 one-way, + 0.011 fees = 0.036-0.061; midpoint 0.086 - research-computed), so the published assumption is conservative rather than optimistic, but its decomposition is never printed and no cost ladder is reported (`research-proposed` in F7).
- **Capacity:** no participation, market-impact or capacity analysis exists. Research-computed scale check: Appendix E's 100,000 bbl position is about 7.1% of the stated 1.4 million bbl prompt-month naphtha daily volume (research-computed, H1 2024 volumes).

## Evidence

### Source-reported

All figures below are third-party claims from Turquet, Bajgrowicz and Scaillet (`SSRN 5034739`, pinned PDF 43 pages, SHA-256 `e1bbd955...3d231e758`), with table/section provenance. None has been independently reproduced.

- **Descriptive statistics (Table 1, PDF p. 12):** raw daily delta mean `-0.001` $/bbl, standardised means `0.002 / 0.000 / 0.000`, standard deviation `0.58` $/bbl in all four columns, min `-3.90 / -2.60 / -3.50 / -2.58`, max `5.72 / 5.00 / 4.23 / 3.59`, skewness `0.13 / 0.08 / -0.23 / -0.11`, kurtosis `10.14 / 3.91 / 3.11 / 1.24`, aDF `-10.70 / -30.14 / -22.86 / -34.16` (columns: raw, 20-day sd, 60-day sd, GARCH(1,1)).
- **Estimation results (sections 4.1-4.3, Figures 3-4):** Gaussian kernel density with bandwidth chosen by 10-fold cross-validation; drift estimated with the 3rd-order Stanton (1997) Taylor expansion, equation (5); diffusion estimated with the 1st-order Variance-based approximation, equation (6), chosen after 10-year simulations showed the 2nd-order Expectation-based variant produced unrealistic extrema around +/-`$15/bbl` versus +/-`$4/bbl` observed; reversion strength rises non-linearly past about `$1/bbl`.
- **Monte Carlo (section 4.4, Figures 5-6):** 10,000 iterations, 5 simulated sessions, seed threshold `+/- $1.6/bbl`, de-standardisation via OLS plus a Johnson S_U residual model; "Most of the reversion takes place on the first day for all three standardisation methods. Holding the position beyond the first day decreases profits for two out the three standardisation methods"; Figure 6's red reference line marks `$0.20/bbl` trading costs.
- **Headline strategy results - the 7 selected strategies (Table 2, PDF p. 25, validation with stop-loss and take-profit):** average net profit per trade `$0.25 / $0.36 / $0.73 / $0.74 / $0.78 / $0.78 / $0.68` $/bbl; average yearly total net profit `$1.03 / $0.68 / $0.54 / $0.60 / $0.75 / $0.81 / $0.67` $/bbl; average win rate `56.7% / 65.6% / 61.9% / 63.3% / 62.5% / 62.5% / 52.1%`; average yearly trades `3.5 / 2.0 / 3.6 / 3.5 / 1.8 / 1.7 / 1.1`; share of successful cross-validations `100% / 100% / 80% / 80% / 100% / 100% / 80%`; calibration average thresholds `1.45 / 1.57 / 1.45 / 1.45 / 1.90 / 1.94 / 1.88` $/bbl and average holding periods `4.0 / 4.3 / 4.3 / 4.3 / 4.2 / 4.4 / 5.0` sessions; calibration average multiple-testing p-values `0.00078 / 0.00542 / 0.00032 / 0.00053 / 0.00090 / 0.00084 / 0.00073`; entry type `Immediate / Delayed / Immediate / Immediate / Immediate / Immediate / Immediate` (6 of 7 immediate).
- **Conclusion restatement (section 6, PDF p. 28):** the selected strategies "generate on average an out-of-sample net profit per trade of `$0.62/bbl`, a yearly total net profit of `$0.73/bbl`, and a win rate of more than 60%", with calibration thresholds "between `$1.4/bbl` and `$2/bbl`" and "The optimal holding period is 4 days".
- **Prose ranges (section 5.3, PDF p. 23-24):** validation net profit per trade `$0.25`-`$0.78`/bbl, yearly total net profit `$0.54`-`$1.03`/bbl, win rate `52.1%`-`65.6%`; selected thresholds' medians `$1.45`-`$1.70`/bbl (total profit) and `$1.95`-`$2.00`/bbl (profit per trade); trades per year `1.1`-`1.8` (profit-per-trade) and `2`-`3.6` (total profit); "the immediate entry strategy is superior to the delayed entry, as 6 out of the 7 selected strategies use the former".
- **Whole-universe averages (section 5.3, PDF p. 26):** averaging all 24 tested strategies gives, under the total-profit measure, `$0.26/bbl` net profit per trade, `$0.45/bbl` yearly net total profit and `53.9%` win rate; under the profit-per-trade measure, `$0.19/bbl`, `$0.23/bbl` and `43.6%` (see contradiction C6).
- **Stop-loss/take-profit effect (section 5.3, PDF p. 24):** using them "decreases the standard deviation of the average win rates across the selected strategies (from 8% to 6%) and increases the win rate on average (from 57% to 61%)" (see contradiction C7); Appendix E Table E.6 (PDF p. 38) reports average absolute differences to the fixed stop-loss/take-profit reference of `-0.03` to `+0.12` $/bbl net profit per trade and `-0.18` to `+0.30` $/bbl yearly total net profit across the 6 stop-loss/take-profit configurations, with "The no-stop-loss and no-take-profit strategy remains the best performing combination".
- **Benchmarks (section 5.4, PDF p. 26):** two dummy strategies (random-entry reversion and random-entry buy-and-hold), 3 trades/year, holding 1-5 sessions drawn at random, 10,000 runs per validation sample; average net profit per trade `-$0.22/bbl` (reversion) and `-$0.18/bbl` (buy and hold) with stop-loss/take-profit, and `-$0.25/bbl` and `-$0.20/bbl` without them; the source also states the reversion benchmark stays negative "even if ignoring the transaction costs" while buy-and-hold is "close to 0 but only when ignoring transaction costs".
- **Drawdown study (Appendix E, Table E.7, PDF p. 39):** share of validation P&L paths hitting the 10%/20% drawdown limits at starting capital of 3x/10x/20x a ~`$100,000` VaR: tight stop-loss `91.4% / 82.8% / 82.8% / 48.3% / 55.2% / 3.5%`, relaxed stop-loss `91.4% / 82.8% / 82.8% / 34.5% / 41.4% / 0.00%`.
- **Negative result already inside the source (Appendix A, Tables A.3-A.4, PDF pp. 29-30):** among the 12 total-profit variants, validation yearly net profit with stop-loss/take-profit ranges from `-$0.73` to `+$1.54`/bbl with 4 variants at or below `$0.13`; among the 12 profit-per-trade variants it ranges from `-$0.37` to `+$0.81`/bbl with 4 variants negative and validation win rates down to `0%` (id 18, 20% successful cross-validations).
- **Seasonality null (Appendix D, Figure D.10):** a non-parametric nonstationary test finds no seasonality in standardised price changes, because "the horizontal line at 1 is contained in the 95% bootstrap confidence interval for the yearly average".
- **Mechanism evidence (section 5.5):** the three stated causes (venue/participant asymmetry, low naphtha liquidity, spread-to-gasoline/propane cross-effects) are argued qualitatively; no decomposition, event study or regression isolates them, and the paper's own future-research list proposes decomposing the signal into its naphtha and Brent components.

### Independently reproduced

`not independently reproduced`

Arithmetic self-check only (no empirical re-run, no data, no code): a script re-derived every prose aggregate from the numbers printed in the source's own tables and exited 0. It confirmed the Table 2 means `$0.6171 -> $0.62`, `$0.7257 -> $0.73` and win rate `60.657% -> ">60%"`; the prose ranges `$0.25-$0.78`, `$0.54-$1.03`, `52.1%-65.6%`; the whole-universe means `0.2567 -> 0.26`, `0.4483 -> 0.45`, `53.9167 -> 53.9`, `0.2342 -> 0.23`, `43.6083 -> 43.6`; the grid arithmetic `13 thresholds`, `13x5=65`, `13x4=52`, `2x3x2x2=24`; and the cost arithmetic `2 x 0.10 = 0.20` against Figure 6. It also produced four findings that do **not** reconcile: the printed `$0.19` against the computed `0.19546`; the stated selection criteria yielding 10 qualifying strategy ids against the 7 printed in Table 2 (missing ids 14, 15, 16); the printed win-rate standard deviation "6%" against the computed `4.29`/`4.63` points; and the EWMA alpha prose/table clash.

### Negative evidence

1. Only 7 of the 24 tested strategy variants survive the source's own selection; the other 17 are discarded, and Appendix A shows several with negative validation outcomes (Table A.3 id 8 yearly `-$0.73`/bbl, id 24 `-$0.34`/bbl; Table A.4 id 18 `-$0.37`/bbl with a `0%` validation win rate and only 20% successful cross-validations).
2. Averaging the entire 24-strategy universe - the source's own robustness argument - yields only `$0.26`/`$0.45` per trade/yearly under the total-profit measure and `$0.19`/`$0.23` under the profit-per-trade measure, with a `43.6%` win rate, i.e. below a coin flip (section 5.3).
3. Trade frequency is extremely low: validation averages `1.1`-`3.6` trades per year (calibration `0.97`-`4.57`). Research-computed, a 20% fold of roughly 9.75 years of daily observations is about 490 sessions, so each reported win rate rests on only about 2-7 trades (assumption: ~250 observations/year).
4. No Sharpe ratio, volatility, return-on-capital or CAGR is reported anywhere; the Sharpe is explicitly excluded (section 5.1), and profits are stated only in $/bbl, so the economic magnitude cannot be compared with any capital base (`data gap`).
5. The Sharpe exclusion is justified by "the downside is strictly capped" via stop-loss/take-profit, yet the source's best configuration removes both (contradiction C8) - the stated risk argument does not hold for the strategies actually selected.
6. Validation is 5-fold random cross-validation on a time series, not walk-forward; `walk-forward`, `holdout` and `placebo` have 0 occurrences, and the only leakage guard is a 5-session no-entry window around fold boundaries.
7. Multiple-testing control (BH FDR at 10%) is applied only inside each calibration fold; the outer selection across 24 variants, 2 performance measures and the win-rate/share-of-successful-folds criteria has no multiplicity correction, and `deflated` / `Benjamini-Hochberg` beyond the calibration step is not applied to the reported 7.
8. The stated selection criteria (win rate > 50%, positive net profit, >= 80% successful cross-validations) applied to the printed Appendix tables identify 10 strategies, not the 7 reported (contradiction C4); the reported set is therefore not reproducible from the stated rule.
9. The stationarity claim that licenses the whole cross-validation design is internally contradictory: the prose says the unit-root null cannot be rejected while Table 1 prints aDF statistics between `-10.70` and `-34.16` (contradiction C2).
10. The whole-universe profit-per-trade average is printed as `$0.19` but computes to `0.19546` (contradiction C6), and the win-rate dispersion claim "8% to 6%" computes to `7.78 -> 4.29/4.63` points (contradiction C7).
11. Both dummy benchmarks lose money after costs (`-$0.22` and `-$0.18`/bbl per trade), and the source concedes the reversion benchmark stays negative even before costs while buy-and-hold is only near zero before costs - so the benchmark set is weak and the comparison mainly shows that random entries lose, not that the selected rules beat an alternative alpha.
12. Costs are positive but flat: `$0.10/bbl` one-way is assumed with no decomposition, no ladder, no sensitivity to the reported `$0.05-$0.10` bid-ask range and no turnover figure (`turnover` 0 occurrences), so cost robustness is untested.
13. Entry prices are observed at a settlement snapshot (Platts MOC 16:30, settlement 19:30 London) that is an administered assessment rather than an executable quote; no fill, slippage-realisation or quote-availability test connects the signal to a tradeable price (`fill` and `latency` 0 occurrences).
14. Single instrument, single 10-year window (15/05/2014-14/02/2024) covering the 2020 COVID demand collapse and the 2022 Ukraine/Russia product-import ban, both of which the paper itself describes as volatility bursts - no subperiod or regime breakdown of strategy performance is reported.
15. Data is licensed commercial material (ICE settlement history plus Platts assessments) with no code, no artefact and no replication package; `code availability`/`replication` statements are absent (`data gap`).
16. Access to the instrument itself is gated: block trades are >99% of naphtha volume, retail is absent, and broker/clearing registration is described as a significant barrier - these fixed and relational costs are not modelled.
17. Position size, capital base and leverage are not specified for the main backtest; the only sizing in the paper (100 lots in Appendix E) implies about 7.1% of the stated prompt-month naphtha daily volume (research-computed), and no capacity or market-impact analysis exists.
18. Stop-loss and take-profit reduce profits in the main analysis and the source's best strategies omit them entirely, so the reported edge depends on holding an unhedged position for up to 5 sessions with no defined risk budget.
19. The mechanism section offers three candidate causes but never tests them: there is no decomposition of the signal into its naphtha and Brent legs, no event study around MOC/settlement timing, and no control for gasoline/propane moves - the causal story remains a conjecture (the paper lists this as future work).
20. Zero citations on the SSRN landing (read 2026-09-29); the working paper has no identified journal despite an acknowledgement thanking an editor and a referee (publication status `not stated in source`).
21. Nine unreconciled internal inconsistencies are recorded in the frontmatter `contradictions` block (C1-C9), covering dates, the ADF statement, EWMA alpha, the selection set, combinatorics, two rounding/dispersion errors, the Sharpe justification and the reference count - collectively they weaken confidence in the printed tables.
22. The paper never reports the number of trades entering each validation fold, so win rates and per-trade averages cannot be assessed for sampling error; no confidence interval, t-statistic or binomial test accompanies any reported win rate.
23. Benchmark holding periods and entry points are drawn at random from the validation set rather than matched to the selected strategies' calendar positions, so the benchmark comparison is not conditioned on the same market episodes (matching is `research-proposed` in F10).
24. No out-of-sample period exists after the data end of 14/02/2024; every reported number is in-sample relative to today, and the source's own "out-of-sample" wording refers only to cross-validation folds.

## Falsification plan

Thresholds, tolerances and acceptance cutoffs below are **research-defined falsification thresholds** (not source-reported). Each gate has a pre-declared failure rule and a stated action on failure.

- **F1 - printed-value reproduction.** Re-derive Table 1, Table 2, Tables A.3/A.4, E.5/E.6/E.7 from the pinned PDF's own numbers. *Fail if* any aggregate differs from the paper's prose by more than `0.01 $/bbl` or `0.1 pp` (research-defined). *Action:* the record stays `contested: true` and no performance claim may be quoted without the discrepancy.
- **F2 - selection-rule reproducibility.** Re-implement the stated criteria (win rate > 50%, positive net profit, >= 80% successful cross-validations) over the 24 printed variants. *Fail if* no deterministic rule reproduces exactly the 7 ids in Table 2 (currently the stated rule yields 10). *Action:* treat the headline 7-strategy result as unreproducible and rely only on whole-universe averages.
- **F3 - stationarity/ADF reconciliation.** Re-run the ADF (no constant, no trend) on all three standardised series and reconcile with Table 1's `-10.70 / -30.14 / -22.86 / -34.16` and with the prose claim. *Fail if* the printed statistics and the printed statement cannot both hold. *Action:* withdraw the stationarity-based justification for random-fold cross-validation and move to F5 only.
- **F4 - point-in-time / leakage audit.** Verify equation (2) uses only `t-1` history, that the `L = 200` warm-up is excluded, that no position opens within 5 sessions of a fold boundary, and that the Platts assessment used at `t` was publicly available before the trade decision. *Fail if* any signal input post-dates its decision timestamp. *Action:* re-run with a conservative one-session publication lag; if the edge vanishes, mark the strategy falsified.
- **F5 - walk-forward replacement (replaces random folds).** Rolling-origin evaluation: train/calibrate on the trailing 80%, test on the next 20% without ever mixing time order, repeated across the full sample. *Fail if* mean validation net profit per trade `<= 0 $/bbl`, or fewer than `50%` of folds are positive (research-defined). *Action:* report as no robust edge.
- **F6 - multiplicity across the whole family.** Apply Benjamini-Hochberg at `q < 0.10` (research-defined) to the full family of 24 variants x 13 thresholds x 4/5 holding periods x 3 standardisations, not just inside calibration. *Fail if* fewer than 2 of the 7 reported strategies survive the family-wide correction. *Action:* retain only the surviving strategies, if any.
- **F7 - cost ladder.** Re-run at one-way costs of `0 / 0.05 / 0.10 / 0.15 / 0.20 $/bbl` plus the `+$0.20/bbl` stop-loss slippage, sourced from an independent broker/exchange fee schedule. *Fail if* net profit per trade `<= 0` at the published `0.10 $/bbl` one-way assumption. *Action:* move to gross-only, unvalidated status.
- **F8 - executable-price gate.** Re-price entries and exits against an executable quote (or at minimum the next session's settlement) rather than the same-session settlement snapshot. *Fail if* the mean net profit per trade drops by more than `50%` of its published value (research-defined) or turns non-positive. *Action:* mechanism may survive, strategy claim does not.
- **F9 - statistical power gate.** Count trades per evaluation window; attach an exact binomial 95% interval to each win rate. *Fail if* any selected strategy has fewer than `30` trades in evaluation (research-defined) or its win-rate interval contains `50%`. *Action:* classify the result as underpowered rather than confirmed; with the source's 1-4 trades/year this gate is expected to fail on current data.
- **F10 - matched placebo.** For each selected strategy, generate `10,000` random-entry strategies matched on trade count, holding-period distribution and calendar window (research-proposed). *Fail if* the selected strategy's net profit per trade does not exceed the placebo distribution's `95th` percentile (research-defined). *Action:* treat the edge as indistinguishable from random timing.
- **F11 - risk-rule ablation.** Compare no stop-loss/take-profit versus static (`-$1.5`/`+$3`) versus the dynamic ranges in Appendix E, on the same folds. *Fail if* the sign of the mean net profit flips between configurations (research-defined). *Action:* report the strategy as risk-rule dependent and unusable without an explicit risk budget.
- **F12 - mechanism test.** Decompose the triggering move into its naphtha and Brent legs and test whether reversion is concentrated in the slow leg around the 16:30 MOC / 19:30 settlement gap, with gasoline/propane moves as controls. *Fail if* the reversion is not attributable to the lagged leg (research-defined). *Action:* reject the stated microstructure mechanism even if the P&L survives.
- **F13 - cross-instrument replication.** Repeat the full protocol on 2 of 3 further OTC/assessment-settled energy spreads (research-proposed: fuel oil crack, East-West naphtha, propane-naphtha). *Fail if* fewer than 2 of 3 replicate a positive net profit per trade at the published cost. *Action:* treat the naphtha result as instrument-specific.
- **F14 - frozen forward window.** No retuning: apply the published thresholds/holding periods unchanged to data from `2025-01-01` onward (the source's data end 14/02/2024 leaves a gap). *Fail if* net profit per trade `<= 0` over at least `2` years of new data (research-defined). *Action:* falsified prospectively; do not re-tune to rescue it.

**No-retuning rule:** parameters frozen at the values printed in Table 2 (thresholds, holding periods, standardisation, EWMA alpha, entry type) before F5-F14 are run; any gate failure must be reported as a failure, not converted into a new calibration search.

## Crypto portability

**`adapted`** - and only the abstract mechanism transports.

What ports (research interpretation): the idea that a large move in a two-leg relative-value instrument can be an artefact of asymmetric execution speed and liquidity between a fast venue and a slow one, so the spread mean-reverts within sessions. Crypto has structurally analogous pairs - a slow or fragmented venue against a fast one, spot against perpetual, or a thin altcoin leg against a BTC/ETH anchor - where cross-venue latency and depth differences are measurable from public feeds.

What does not port as stated:

- The signal is defined on an **administered assessment** (Platts MOC) and an OTC broker market with monthly cash settlement; crypto has no equivalent assessment-fix dependency, and no analogue of the 16:30 MOC / 19:30 London settlement gap exists.
- The instrument is a **cleared futures/forward spread** with expiry rolls (5 business days before expiry); crypto perps have funding rather than expiry, and the roll rule, margin grid and liquidation mechanics are all different.
- Costs: `$0.10/bbl` one-way plus `+$0.20/bbl` stop-loss slippage is a broker/clearing fee structure; crypto taker/maker fees, spread and impact must be re-derived from venue schedules.
- Access: the source's barrier is broker/clearing onboarding; crypto's barrier is venue fragmentation, custody, and 24/7 session structure instead.
- Data: ICE settlement history and Platts assessments are licensed; crypto equivalents (trades, books, funding, mark/index) are public but have different timestamp, candle-boundary and clock-synchronisation requirements.
- Market microstructure: `>99%` block trades and an absent retail segment define the naphtha order flow; crypto perp order books are continuous and retail-heavy.

No source-reported crypto evidence exists in this record (`the word crypto does not appear in the pinned text`); crypto performance is `unproven`. Crypto portability is not authorisation to trade.

## Limitations

- `underspecified`: position sizing, capital base, re-entry rules, order type, fill model, signal-to-order delay, latency, participation and capacity.
- `data gap`: ICE/Platts data are licensed with no replication artefact, no code availability statement and no missing-data or staleness rules.
- `not independently reproduced`: all performance figures are third-party claims; our own work was arithmetic on the printed tables only.
- `unproven`: no post-2024-02-14 evidence, no second instrument, no second market regime, no capacity study.
- Nine unreconciled contradictions (C1-C9) in the frontmatter, including two that affect the validity of the evaluation design itself (C2 stationarity, C4 selection set).
- Very low trade frequency means the reported win rates and per-trade averages have unknown sampling error; no interval or t-statistic accompanies them.
- The reported unit of profit ($/bbl) is not a return, so the results cannot be compared with any benchmark Sharpe, CAGR or drawdown.
- Publication status is `not stated in source`; the acknowledgement of an editor and a referee implies review without identifying a venue, and the SSRN landing shows 0 citations.
- Single-author-supplied fee schedule and single-vendor data: no independent second source for the cost model or the price series.
- Scope: this record captures a research hypothesis. It does not assert that the strategy works, that it survives costs in our hands, or that it can be executed at all from our infrastructure.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no signal generator, no data ingestion for ICE/Platts series, no backtest, no Qlib run, no paper, testnet or live configuration. The only artefact produced by this run is this record plus an arithmetic self-check script over the pinned PDF's printed tables. No Qlib full-backtest validation, Paper, Testnet or Live verification has occurred and none is implied.

## Adoption boundary

`status: research-only` | `adoption: not-approved` | `approval_scope: research-only`.

The presence of this record in the repository means only that normalised research material was pushed to the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; or approved for live trading. Paper, Testnet and Live remain future gated stages and are not connected.

## Related Wiki records

Read-only Wiki Brain resolution for this run: `quant/strategy-research-record-spec-v2.md` returns file-not-found, so the run failed closed onto the canonical `quant/strategy-research-record-spec-v1.md` (10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`). A read-only `kb_search` for `naphtha` returned **0 pages**, so no Wiki link to a naphtha record exists and none is fabricated here. A read-only `kb_search` for `crack spread mean reversion commodity energy` returned three verified adjacent pages:

- `[[quant/crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12]]` - same broad family (refining-margin mean reversion) but a different source, instrument (3:2:1 RBOB/HO/WTI) and signal construction (deseasonalised OU plus stop-lockout).
- `[[quant/cwt-wavelet-bandpass-mean-reversion-hmm-stress-overlay-2026-09-12]]` - wavelet/HMM mean-reversion overlay on commodity futures; different mechanism and data dependency.
- `[[quant/commodity-seasonal-dvr-ssa-rlssa-benchmark-null-2026-09-14]]` - seasonality rather than large-move reversion; useful as a sibling null result under transaction costs.

Adjacent repository records (not verified as Wiki pages, listed by filename only): `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md`, `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23.md`, `commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02.md`.

## Sources

1. Briac Turquet, Pierre Bajgrowicz, Olivier Scaillet. *"Mean Reversion Trading on the Naphtha Crack."* SSRN working paper, abstract_id `5034739`, DOI `10.2139/ssrn.5034739`. Landing: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5034739` (read in a browser session 2026-09-29: 43 pages, posted 27 Nov 2024, last revised 19 May 2025, 417 downloads, 1,394 abstract views, 0 citations, 33 References, licence "All rights reserved. No reuse allowed without permission.").
2. Pinned PDF read end to end for this record: 2,518,214 bytes, 43 pages, SHA-256 `e1bbd9550c0dd53c08fd8b81ac4cc84fc09fd14f884cae3470556383d231e758`, obtained from the landing page's own delivery link, extracted with pypdf 6.16.2 to 95,889 characters / 1,506 lines.
3. Second SSRN version of the same work (not separately read): `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5032815`, 37 pages, posted 25 Nov 2024.
4. Works cited inside the source and used above only as the source's own citations (not independently read for this record): Gatev, Goetzmann and Rouwenhorst (2006); Bajgrowicz and Scaillet (2012); Benjamini and Hochberg (1995); Stanton (1997); Prigent, Renault and Scaillet (2001); Bollerslev (1986); Lubnau and Todorova (2015); Mahringer and Prokopczuk (2015); Chen, Smetanina and Wu (2022); Glasserman (2003); Johnson (1949); Fan and Zhang (2024).
