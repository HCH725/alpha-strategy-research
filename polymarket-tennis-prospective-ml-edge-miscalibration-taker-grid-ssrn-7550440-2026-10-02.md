---
schema: strategy-research-record-v1
title: "Prospective Model-Edge vs Price Test on Polymarket Tennis: Calibration Decomposition, Mid-Controlled Edge, and a Non-Detecting Executable Taker Grid"
created: 2026-10-02
updated: 2026-10-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - polymarket
  - market-efficiency
  - calibration
  - executable-taker-grid
  - sports-forecasting
  - negative-results
status: research-only
confidence: medium
source_as_of: 2026-10-02
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7550440"
  - "https://doi.org/10.2139/ssrn.7550440"
  - "https://api.crossref.org/works/10.2139/ssrn.7550440"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Prospective Model-Edge vs Price Test on Polymarket Tennis: Calibration Decomposition, Mid-Controlled Edge, and a Non-Detecting Executable Taker Grid

## Provenance

Primary source identity (read from the primary source itself, not from a summary):

- Author: **Dmitrii Yushkov** (single author, exactly as printed on the manuscript title page and on the SSRN landing author row). Affiliation as printed: New Economic School and HSE University, Moscow on the title page; New Economic School (NES); National Research University - Higher School of Economics (HSE University) on the landing page. The author e-mail line on the manuscript title page is deliberately not reproduced here.
- Title (exact): "Model Edge or Model Miscalibration? A Prospective Test on Polymarket Tennis".
- Venue and identifiers: SSRN preprint, abstract id 7550440, DOI `10.2139/ssrn.7550440`. Crossref record type `posted-content`, group-title `SSRN`, publisher Elsevier BV, `container-title` empty, `reference-count` 0, Crossref created `2026-10-02T11:39:26Z`. DOI resolves by redirect to `https://www.ssrn.com/abstract=7550440` (a plain HTTP client receives HTTP 403 from the Cloudflare edge on both the DOI target and the landing page; see fetch route below).
- Dates (all three, as printed): manuscript `Date Written: October 01, 2026`; landing `34 Pages Posted: 2 Oct 2026`; Crossref created 2026-10-02. Suggested citation line on the landing gives `October 01, 2026`.
- Publication status: **SSRN working paper / preprint**. No journal reference, no container title, no acceptance or peer-review statement appears on the landing page or in the Crossref record - peer-review status is therefore `not stated in source` (data gap), not "peer reviewed".
- Licence (landing `License Information` row, verbatim): "The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission." This record therefore cites and normalizes the idea and the printed numbers with section/table provenance; it reproduces no extended passage.
- Landing metadata also printed: keywords "prediction markets, probability calibration, forecast evaluation, sport forecasting, market efficiency, machine learning forecasting"; JEL C52, C53, G14, L83; SSRN section "Capital Markets: Market Efficiency"; 0 References, 0 Citations; DOWNLOADS 2, ABSTRACT VIEWS 6 at fetch time; Declaration of Interest states no position was taken on any market analysed and no capital was deployed (all returns counterfactual under the accounting of Section 4.5); no funding; a generative-AI disclosure (Claude / Claude Code, April-September 2026) covering drafting and analysis code, with design and conclusions claimed as the author's own.
- Primary-source artefacts pinned on 2026-10-02: SSRN `Delivery.cfm` PDF linked from that landing page, **349,803 bytes, SHA-256 `90569c6009c5422dd9b538730d09298fa439bf64904d910885b02f43ad0018ef`**, `%PDF-1.5`, **34 pages** by pypdf (matching the landing "34 Pages"), PDF metadata `/Creator LaTeX with hyperref`, `/Producer xdvipdfmx (20220710)`, `/CreationDate D:20261001204657-00'00'`. Extracted text layer **138,785 characters / 140,261 bytes / 1,631 lines, SHA-256 `fb899e7211250f098275b117131c284709096ce5e84158ab39a427757a21b21d`**, whitespace-normalized 138,772 characters with SHA-256 `348b25ca3d3c1a86dafa576237f9a8e5f25f798029d70f97354baf6f34090d13`.
- Fetch route (provenance for the above): the landing page was opened in a real browser session to clear the Cloudflare challenge, the PDF was then fetched with that session's clearance, and no session-bound URL is stored in this record. The plain-HTTP failure mode (HTTP 403, challenge page) is recorded because it explains why a naive client cannot reproduce the fetch.
- Reading coverage: the 34-page PDF text was read end to end - title page and abstract, Highlights, Sections 1, 2, 2.1, 2.2, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 5.1, 5.2, 5.3, 5.4, 5.5, 6, the References list, and Tables 1 to 7 and Figures 1 to 5 with their captions. The landing page was read for author rows, page count, dates, licence, declarations, JEL, keywords, section assignment and paper statistics.

Sample, universe and cost treatment (all determined at Methods level, not from the abstract):

- **Sample period:** order-book history 27 April 2026 to 13 June 2026 (collector window); the two-27 April gap is uncovered and there is an outage of roughly 29 hours on 13-14 May (Section 3.3). Market history of 6,458 markets over 27 April to 13 June 2026 (Section 1 / Table 1).
- **Universe:** Polymarket tennis event contracts, tracked side fixed at deployment and independent of price (Section 3.1); populations are deliberately non-nested and are printed in Table 1: order-book history 6,458, resolved catalog 5,874, calibration sample 5,498 (5,485 after removing walkovers and retirements), shadow log V1 3,231 / V2 2,756 / V3 2,059 entries over 2,749 and 2,054 distinct markets, matched V2 1,921 and matched V3 1,925.
- **Venue and market type:** order-driven central limit order book settled on-chain (Sections 1 and 3.2), explicitly contrasted with a quote-driven bookmaker book; the venue's separate US exchange runs a different uniform schedule and is not the venue studied (Section 3.2, footnote 1).
- **Transaction cost / fee treatment, read from Section 3.2 and Section 4.5:** the venue charges a **sports taker fee proportional to p(1-p) on the notional, taker only, with makers charged nothing and rebated**; the schedule "launched at a rate of 0.03 in March 2026 and was raised to 0.05 in July 2026"; the sample "lies entirely inside the 0.03 regime"; the tradability grid was first computed at 0.05 and rerun at 0.03, both reported side by side in Section 4.5. **Gross returns are the primary quantity** ("what does not pay before costs does not pay after them"). No closed-form fee equation is printed - the exact functional constants are `underspecified` in source, only the prose proportionality and the two rates are stated. The fee rules are documented by deployment-date rule and the public catalog "carries no fee field of any kind", so the fee-free control is absent and this is recorded as a limitation in Section 6. Settlement and gas on-chain, capital tied up between entry and resolution, and any slippage past the top of book are **explicitly outside the accounting** (Section 4.5), as are depth/capacity in the grid itself: entry is "the quoted ask taken without reference to size" and depth and order-size columns are "not loaded by the accounting script at all" (Section 6). The sample was **paper-traded only** - no capital was deployed (Section 6 and the Declaration of Interest).
- **Slippage / spread / fill:** the executable ask and the executable bid are used for entry and terminal payoff in Section 4.5; measurement sections (4.1, 4.3, 4.4) use the mid and are explicitly "not net of the spread and are not meant to be" (Section 3.2). Fill at top of book is assumed with no queue position, no partial fills and no price impact (Section 6). Gas, capacity and depth: `data gap` beyond the one depth-notional bound quoted for the maker branch (approximately USD 492k per month, Section 4.5).

Pre-write identity and dedup evidence (all run against the whole checkout before writing):

- Repository state at run start: `git pull origin main` returned `Updating ac2bd23..cb2c0bf` fast-forward with one new file from another scout (`tradingview-kangaroo-tail-structure-liquidity-sweep-rejection-2026-10-02.md`); `git log --oneline -20` was read as a convenience glance only. The working tree contained only other scouts'/coordinator untracked artefacts; nothing was staged, cleaned or imported, and this record is the only staged path.
- Hidden-inclusive identity scan over **3,992 files** (whole checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv` at 1,088,787 bytes) for `7550440`, `Yushkov`, `dyushkov`, `Model Edge or Model Miscalibration`, `Polymarket tennis`, `Spiegelhalter`, `shadow log`, `ECE10`, `Kovalchik`, `tennis`: **0 files each**. Positive control `novy-marx`: 73 files. Loose probes: `beat-the-market` matched 1 unrelated SPY intraday record; `pre-start price` matched 1 unrelated League of Legends pregame record whose primary source is arXiv:2609.08060.
- Schema resolution: the canonical Wiki Brain specification `quant/strategy-research-record-spec-v2.md` does not exist (filesystem search for `quant/strategy-research-record-spec-v*.md` returns only v1), so the run **failed closed onto `quant/strategy-research-record-spec-v1.md`** (10,289 bytes) and read it in full before writing. Zero Wiki Brain pages were written or modified; Wiki access this run was read-only existence checks of the five vault paths linked below.
- Five-axis distinction (mechanism / signal construction / universe / horizon-regime / material data dependency) against the nearest repository records, each differing in source identity and in at least one further axis: `crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01.md` (arXiv:2605.02287 + SSRN 5227845 + Columbia WP - account-level skill/luck and information-leakage scoring, not a model-versus-price tradability test); `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md` (GitHub `elraffaello123-art/quant-research` commit `511fab83791a81a96ff64b3e5dadc1636cc5b698` - Wang-transform lambda on Kalshi hourly mids); `crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01.md` (arXiv:2606.19517 - cross-venue binary pricing against option-implied fair value); `league-of-legends-pregame-paired-comparison-polymarket-parity-2026-09-22.md` (arXiv:2609.08060 - paired-comparison esports model parity); `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md` and `crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01.md` (different sport/asset, different signal). No record in this repository previously captured tennis, bookmaker-consensus comparison, prospective shadow logging, Spiegelhalter testing or an executable event-contract taker grid.

## Economic mechanism

### Source-reported

The paper does not propose a new premium; it separates two explanations that produce the same observable object, the model's signed disagreement with the current price ("edge"):

1. **Genuine edge that the market has not yet absorbed** versus **model miscalibration**, which generates disagreement mechanically in whatever direction the model's scale is wrong (Abstract, Sections 1 and 5.1). The two are told apart by conditioning on the current price: specification B/D of Section 3.1 regresses the pre-start price on the current mid plus the model probability, and the mid-controlled coefficient on edge is algebraically the specification-B model coefficient (an identity the author confirms numerically across all ten version-by-horizon fits).
2. **A specification trap:** regressing an outcome on the edge alone (specification C) returns a coefficient that is negative and appears to strengthen toward the start; the source attributes this to omitted-variable bias because the edge contains the negative of the price it is regressed against, and derives `beta_C = beta_B_model + beta_D_mid * delta` with `delta = Cov(p, e)/Var(e) < 0` whenever `Cov(p, p_hat) < Var(p)` (Sections 3.1 and 4.4).
3. **Venue economics:** on a quote-driven bookmaker book the operator sets the spread and the informed taker benefits from a stale line; on an order-driven CLOB with a taker fee "the same trade pays for the privilege", which is stated to remove the structural taker advantage that bad-model profit arguments rely on (Sections 1, 3.2 and 2.2, after Hubacek and Sir 2023).
4. **Why the market is hard to beat (frame, not measurement):** a Glosten-Milgrom adverse-selection reading - residual inefficiency tends to be about the size of the cost of taking it - plus convergent external evidence that on this venue arbitrage opportunities have a median life of a few seconds and executability rather than detection is binding (Section 5.3, citing Yang, Cheng and Zou 2026 and Vedova 2026). The microstructural mechanism itself is deferred to a companion paper "in preparation" - `data gap`.
5. **Calibration versus discrimination:** calibration is necessary but not sufficient; a monotone recalibration cannot reorder forecasts, so a binding discrimination deficit is unfixable by a calibrator (Sections 4.2 and 5.1, after Walsh and Joshi 2024).

### Research interpretation

Falsifiable hypothesis as we normalize it (this is our phrasing of the claim the source tests, not the source's own sentence):

```text
Regime / precondition: a calibrated event-contract CLOB whose sports books are
  fee-bearing and order-driven (no market maker of last resort).
Primary signal (source-reported): the ensemble probability p_hat written before
  the match, versus the executable quotes of the two outcome tokens.
Hypothesis (source-reported result, restated as a hypothesis): once the current
  mid is controlled for, the model's incremental content about the future price
  is small and confined to roughly the day before the match, and is concentrated
  on markets whose book has not formed; the hold-to-resolution taker return on
  the same information does not separate from zero even gross of fees.
Failure of the hypothesis (research-defined): any horizon-by-edge cell whose
  fee-net return interval clears zero after multiplicity control, or a challenger
  model whose paired AUC is not below the market's on a matched sample.
```

Component roles (each labeled by origin): **Regime:** book-formed versus wrapper quotes - the source measures this with the spread at the read (0.05 and 0.10 cuts) and treats the split as descriptive because spread is an outcome of attention, not a randomized condition (Section 4.3). **Primary signal (source-reported):** `e_A = p_hat - ask_A`, `e_B = bid_A - p_hat`, buy side A if `e_A > 0`, buy side B if `e_B > 0`, otherwise do not trade; "the spread itself is the threshold" (Section 4.5). Note the printed left-hand side of `e_B` reads `bid_A` in the PDF text layer; the economically coherent reading is a bid on the complement side, and the notation as printed is `underspecified` on that one symbol - flagged rather than silently repaired. **Confirmation filter:** none beyond the executable-spread threshold; there is no liquidity, tier or volume filter in the grid (the tier cut is explicitly declined in Section 4.5). **Risk / exit:** none - terminal accounting, entered once, held to resolution, flat sizing, no early exit, no hedge, no sizing rule (Sections 3.1 and 6).

Do not assume every component contributes alpha; the source itself reports that the apparent predictive content lives in unformed books, which it reads as out-predicting a placeholder rather than a market (Section 5.1).

## Signal

Source-reported construction (all of the following are printed in Sections 3.1, 3.4, 3.5 and 4.5):

- **Signal formation timestamp:** the ensemble probability is the scanner's first logged pass over a market, written at a **median of 20.2 hours before scheduled start (interquartile range 15.6-34.6 hours)**, fixed once and never re-estimated. Immunity to look-ahead comes from a live shadow log written before resolution (Section 3.5), with a measured median gap of 68 seconds between the quote the model saw and the probability it wrote (Section 4.2). Probability orientation was verified against the outcome field on all 152,204 prediction rows (Section 4.2).
- **Horizon grids (two, deliberately different):** regression horizons `H = {T-24h, T-12h, T-6h, T-2h, T-30m}`; tradability grid horizons `G = {T-30h, T-24h, T-12h, T-6h, T-2h}` - the horizon set of the execution study it reruns. The source names the grid whenever a number from one is set beside a number from the other; this record preserves that separation.
- **Reference prices:** `p_pre` = last mid observed no later than fifteen minutes before scheduled start (hours-to-start >= 0.25); `T0` = last mid at hours-to-start >= 0; mids at the H horizons. Anchors 0 / 0.25 / 0.5 hours leave ECE at 0.0088 / 0.0097 / 0.0090.
- **Model family (source-reported):** V1-V3 are live XGBoost ensembles; V2 and V3 are the reported live versions. V4 is an offline clean-rebuild control (CatBoost, causal replay, strictly ordered temporal splits: train <= 2023-12, validation 2024, lockbox-A <= 2026-04-22, PM-era lockbox-B >= 2026-04-27), a control rather than a trading model. Feature families are named only as "ratings, form, surface, rest, and match context" (Section 5.4) - the full feature list, hyperparameters and ensembling weights are `not stated in source`.
- **Entry:** buy the side whose executable ask the model prices below, i.e. enter at the ask of the side actually bought; a negative disagreement with the tracked side becomes a purchase of the complement at its own quoted ask, not a short (Section 4.5).
- **Exit / holding period:** none; held to resolution (terminal). No re-entry rule is specified because no exit exists.
- **Position sizing:** flat, equal units; returns are aggregate `sum(payoff - entry - fee) / sum(entry)` with intervals from **1,000 bootstrap replications resampling (payoff, stake) pairs**. No leverage, no bankroll rule.
- **Stratification (analysis only, not a tradable rule):** terciles are cut on the realized executable edge within each version-by-horizon cell **over executed trades only**, so `e > 0` holds by construction and the terciles separate marginal from large executable edges, not winners from losers. Because the cut is realized (ex-post) it is **not forward-implementable as stated** - an ex-ante edge threshold would be `research-proposed`, and this record proposes none.
- **Timing caveat (source-reported):** at T-30h and part of T-24h the forecast does not yet exist, so those two columns are "an upper bound on what was available rather than a backtest" (Section 4.5); the corresponding restriction for the regressions (826 markets whose first scan precedes the horizon) raises rather than collapses the day-out coefficient.
- **Fully specified / underspecified verdict:** the tradable rule (side selection by executable edge, ask entry, hold to resolution, flat sizing, taker fee schedule by regime) is source-specified; the fee formula constants, the ensemble internals, the tercile cut's forward analogue, and the `bid_A` notation for `e_B` are `underspecified` and marked above.

## Required data

- Instrument / universe: Polymarket tennis binary outcome tokens (tracked side plus arithmetic complement), one row per market; 6,458 markets observed 27 Apr - 13 Jun 2026, of which 5,498 resolved tracked-side observations carry a valid mid.
- Venue: Polymarket public **Gamma and CLOB endpoints** (Section 6, data and code availability) - order-book snapshot pivot of 1.7M rows, current-state market catalog, resolution outcomes.
- Market type: on-chain settled event contracts (binary, 0-1 price scale); not spot, perps or options. Market type is `event contract / prediction market`.
- Timeframe: horizon mids at T-30h / T-24h / T-12h / T-6h / T-2h / T-30m before scheduled start; T0 and p_pre anchors as above; timestamps are the collector's own scans (timezone convention `data gap` - the source does not state a timezone for scheduled tennis start times or scan stamps).
- Fields used: two-sided bid/ask and mid per outcome token, spread, resolution outcome, model first-scan probability, tournament Elo rating (live-read), tour/level/surface labels (empty for 65.2% of records), depth (only in a separate pass - not in the accounting script).
- External reference data: Jeff Sackmann's open tennis databases (CC BY-NC-SA 4.0), public ESPN result feeds, TennisExplorer listings for Challenger and qualifying events; bookmaker closing lines (Bet365, market-best, cross-book average, Betfair Exchange) used only in Section 4.6 and only on the 4% of markets they cover; Pinnacle closing odds exist for 2026 but stop being populated on 13-14 January, so the intersection with the sample is empty.
- Point-in-time: the shadow log is the point-in-time artifact (timestamped before resolution); the catalog is a current-state table rewritten on every scan and is **contaminated for retrospective feature reads** - the catalog rating equals the final scan in 94.9% of markets, a median of six distinct rating values per market, and an as-of audit shows the change between consecutive appearances loads on the later match at about +25 rating points (p < 1e-16) (Section 3.5).
- Missing data: 2-27 April uncovered; a ~29-hour outage on 13-14 May; 42 logged markets resolve with no pre-start observation; 3,577 resolved markets carry no model prediction (the model priced roughly a third of the resolved population, self-selected); walkover/retirement filter is applied only where the source says so (N = 5,485 subset). Imputation: none stated.
- Funding / fee / spread needs: venue taker fee schedule by deployment date (0.03 in sample, 0.05 from July 2026), maker rebate (makers charged nothing), executable bid and ask per side. Gas/settlement, capital carry, depth-based slippage: observed = no, modeled = no, omitted = yes, explicitly (Section 4.5).

## Execution assumptions

Source assumptions (all source-reported):

- Signal-to-order timing: the executable edge is read at the horizon quote; entry is the ask of the purchased side at that horizon, taken without reference to size; no latency model is given (`data gap`).
- Order type: marketable taker order against the resting ask (grid), plus an idealized maker branch (post at the mid, fee zero) that the source itself calls "deliberately generous".
- Fill model: assumed fill at the top of book, no queue position, no partial fills, no price impact (Section 6); every grid figure is a per-unit quantity.
- Fees: taker fee proportional to p(1-p) on notional at rate 0.03 (sample) and 0.05 (later regime); makers free and rebated. Fee schedule by deployment date, no per-market fee field available.
- Spread: paid on entry via the executable ask and on the terminal leg via the executable bid; measurement sections are mid-based and not net of spread.
- Slippage / impact / capacity: past-the-top-of-book slippage is outside accounting; capacity is not modelled in the grid; a depth-notional bound of about USD 492k per month appears only for the maker branch and assumes sweeping the entire visible book with guaranteed fills.
- Leverage / margin / borrow: none - long-only purchase of an outcome token held to resolution, no shorting (the complement purchase substitutes for a short), no leverage.
- Latency / partial fills / failures: not modelled (`data gap`).
- Deployment status: paper / counterfactual only - no position was taken and no capital was deployed during the study window.

Scout-added assumptions: **none**. This record proposes no entry threshold, stop, sizing rule, universe filter or capacity cap; every operational value above is either printed in the source or marked `data gap` / `research-proposed` where noted.

## Evidence

### Source-reported

All figures below are third-party claims from the primary source, each tagged with its Section / Table / Figure so the row and column identity is recoverable. They have not been independently reproduced.

Calibration and discrimination (Sections 4.1, 4.2, Table 2, Table 3, Table 4, Table 5):

- Market at the T0 anchor: **ECE10 = 0.0088 over N = 5,498**, Spiegelhalter **Z = -0.27 (p = 0.79)**, at 0.63 of a 1,000-draw parametric null floor (6.8th percentile). By horizon (Table 3): T-30h Z = +2.41 (p = 0.016, n = 1,425), T-24h **Z = +3.00 (p = 0.0027, n = 1,611)**, T-12h +1.17 (p = 0.243), T-6h +0.17, T-2h -0.10, T-30m -0.02, T0 -0.27; the T-24h statistic is carried by one price bin (66 markets quoted 0.10-0.20 supply 38.3% of the numerator on 4.1% of the sample; removal leaves Z = +1.98, p = 0.047). T-24h subgroups: Challenger Z = +2.97 (p = 0.0030, n = 444), ATP +2.24 (p = 0.025, n = 727), hard courts +2.23 (p = 0.026, n = 101); under Bonferroni at 0.05/16 = 0.003125 only Challenger survives.
- Baselines (Section 4.1): constant 0.5 forecast log-loss 0.693 against the market's 0.574; honest first-scan Elo logistic AUC 0.675 against the market's 0.734 on the common 1,540 matches, paired difference **+0.059 (95% CI [+0.040, +0.078])**; reading the rating from the resolved catalog instead inflates that AUC to 0.784 (+0.11) and would falsely appear to beat the market.
- Live ensembles on their matched sets (Section 4.2): first-scan **ECE10 0.1315 (V2) and 0.1219 (V3)** against the market's 0.0230 / 0.0227 on the same sets, each model at **5.1-5.6x its own noise floor** (percentile 100) while the market sits at 0.78 of its floor; Spiegelhalter **Z = 16.7 (V2)** and **15.2 (V3)**. In-sample Platt scaling (an oracle bound) gives slope 0.393 with ECE 0.0258 (V2) and 0.391 with ECE 0.0182 (V3) but leaves AUC unchanged to three decimals. **First-scan AUC 0.638 (V2) / 0.627 (V3) against the market's 0.738 / 0.739** on those matched samples; the honest Elo baseline (0.675) also ranks above the models, paired gap elo-minus-model +0.048 (95% CI [+0.023, +0.073]) on the 1,540 shared matches.
- Book-quality read (Section 4.2, Table 4): at the moment the model writes, the median spread is 0.55 and the widest bin's mid is uninformative (AUC 0.506, 689 of 1,297 markets in that bin for V2); with a real book (spread <= 0.02) the market reads AUC 0.719 / 0.723 and the paired model-minus-market difference is negative in all six real-book cells, excluding zero in four of them. Re-reading the market at each market's own first-scan timestamp (median lag 68 seconds) changes the market's AUC by -0.009 with an interval covering zero - "the market's advantage over the model is not an advantage of timing".
- Clean rebuild control (Section 4.2, Table 5): V4 reaches **ECE10 0.0277 at 0.84 of its own floor** on the PM-era lockbox (Z = +1.87, p = 0.062), i.e. calibrated, and a beta calibrator only moves it to 0.0228 - "data hygiene rather than post-hoc scaling". On the **486 shared matches** (345 under the strict exact-date/full-name join): V4 ECE10 0.0398 (0.88 floor) versus market 0.0590 (1.27 floor), neither rejected (Z = +0.86 p = 0.39; Z = -0.12 p = 0.90); **AUC 0.670 versus the market's 0.735, paired difference -0.065 (95% CI [-0.104, -0.027])**, strict join -0.082 [-0.131, -0.032], at T-6h -0.057 [-0.093, -0.020]; Brier 0.229 versus 0.209. At the anchor 482 of 486 markets are quoted inside a spread of 0.05, so the comparison is against real prices.

Horse race and specification diagnostic (Sections 4.3, 4.4, Table 6):

- Specification-B mid coefficients are flat at one across horizons: **V2 1.009, 1.010, 0.999, 0.998, 1.001; V3 1.032, 1.009, 0.998, 0.997, 1.001** (T-24h to T-30m).
- Model partial r-squared of the pre-start price: **6.44% (V2) / 9.90% (V3) at T-24h, 2.10% / 0.79% at T-12h, 0.81% / 0.19% at T-6h, 0.26% / 0.03% at T-2h, 0.40% / 0.19% at T-30m**, with market-only R-squared rising from 0.767 to 0.988 over the same span (Table 6, n = 1,045-1,994 per cell).
- Book-quality split at T-24h: tight stratum (spread <= 0.05, n = 610 / 611) contributes **0.13% for V2 (beta +0.0099, SE 0.0114, t 0.87, p 0.38)** and **1.7% for V3 (beta +0.0386, SE 0.0119, t 3.26, p 0.001)**; wrapper stratum (n = 437 / 434) 14.2% and 18.1%, with the coefficient itself falling from +0.124 to +0.010 (V2) and +0.160 to +0.039 (V3). The honest Elo control accounts for **36.3% in the wrapper stratum (beta +0.590, SE 0.038, n = 418)** and 0.10% in the tight stratum - a rating with no learned component beats both ensembles exactly where the quote is a wrapper. Tight-stratum market coefficients are 0.992 / 0.972.
- Restricting to the 826 markets whose first scan precedes the horizon raises the day-out coefficient to +0.184 (V3) and +0.127 (V2) with partial r-squared 11.9% / 6.0%.
- Sign diagnostic (Section 4.4): the mid-controlled edge coefficient is positive and decaying (V2 +0.124 -> +0.007; V3 +0.160 -> +0.005), while the uncontrolled specification C gives **V3 -0.077 at T-24h to -0.341 at T-30m**; recovered delta runs -0.144 / -0.230 (T-24h) to -0.346 (T-30m), and the decomposition reproduces at T-24h for V2 as 0.124 + 1.009 x (-0.144) = -0.021 against the observed -0.021 (p = 0.51).
- V4 at T-24h: pooled contribution 14.6% (n = 183), 24.1% where the book is wide (n = 80, beta +0.609, SE 0.123, t 4.94) and 5.6% where tight (n = 103, beta +0.173); this tight-stratum coefficient is the one in the paper that fails clustering (p = 0.017 homoskedastic, 0.079 player, 0.110 tournament, 0.109 two-way on 15 tournament clusters) and is expressly not read as a residual contribution.

Tradability grid (Section 4.5, Table 7 - thirty cells, terminal accounting at the executable ask and bid):

- **No cell has a gross ROI with a lower confidence bound above zero.** Largest positive point estimate **+6.02% (95% CI [-1.1, +13.1], n = 557, V3, T-12h, low tercile)**; worst **-10.01% (95% CI [-19.7, -0.5], V3, T-12h, high tercile)** - one of thirty cells is significantly negative gross, before any fee. Mean entry falls from about 0.53 (low tercile) to about 0.41 (high tercile).
- Fee illustration (Section 4.5 prose, not tabulated): at **0.05** eight cells are significantly negative with ROI range **[-12.7, +4.2]**; at **0.03** (the rate the sample bore) five cells and range **[-11.6, +4.9]**; the three cells that drop out had upper bounds -1.03, -0.47 and -0.17. Median cost per cell falls from 2.06 to 1.24 points (ratio 1.667 = 0.05/0.03).
- Gradient: gross ROI declines from low to high tercile in **9 of 10** horizon groups (strict low-mid-high monotonicity holds in 5 of 10 and is expressly not claimed); the same direction holds on absolute profit per unit in the same 9 of 10 groups. Interval half-widths: about 7pp at n about 557, about 13pp at the sparsest cells (n about 215).
- Maker branch: **flip-maker +0.3% to +2.1% with intervals above zero in 9 of 10 cells**; held-maker intervals cross zero; capacity bound about USD 492k per month; the source states maker viability is unresolvable without fill and order-flow data and claims no tradable edge on either branch.
- Withdrawn positive (recorded by the source, Section 4.5): a day-out long-shot fade rule (buy the 10-20% bin at T-24h, enter at the ask, hold to resolution) returned **+71.5% gross on 66 markets**, and was withdrawn because those 66 markets are the ones carrying 38% of the statistic the rule exploits; split by window halves it gives **-25.1% (n = 34, [-84.5, +44.9])** and **+174.2% (n = 32, [+68.1, +285.2])**, and no bin deviates significantly in the first half.
- Bookmaker cross-check (Section 4.6): on the 220-market slice (4.0% of the sample) the T0 mid regresses on the de-vigged closing probability with correlation 0.991-0.995 and R-squared 0.98-0.99; Betfair slope 0.997 +/- 0.007; in the outcome horse race the book's coefficient is positive and significant (t +2.38 to +2.76, partial r-squared 2.5-3.7%) while the market's is not, and the market's AUC sits below the book's by 0.009-0.010; the cross-book average out-ranks V2 by 0.058 and V3 by 0.036 at n = 201.

### Independently reproduced

not independently reproduced

Arithmetic identities checked only (no data, no model, no return recomputation): 2,039 - 76 = 1,963 and 1,963 - 42 = 1,921; 2,042 - 75 = 1,967 and 1,967 - 42 = 1,925; 2,749 - 710 = 2,039; 2,054 - 12 = 2,042; 5,498 - 1,921 = 3,577; 1,921 / 5,498 = 0.349 ("roughly a third"); 0.05/0.03 = 1.667 and 2.06/1.24 = 1.661 (rounding level); 0.05/16 = 0.003125 (the printed Bonferroni bar); 0.124 + 1.009 x (-0.144) = -0.0213 against the printed -0.021; (0.171 - 0.136)/0.171 = 20.5% against the printed 21% and (0.170 - 0.143)/0.170 = 15.9% against the printed 16%; 486 - 345 = 141 rows excluded by the strict join; 6,458 - 5,874 and 5,874 - 5,498 are not differences, because the source states the three populations are not nested. One figure does not reproduce from printed rounded inputs: the source's "roughly 30.6% larger |ROI|" from mean entries 0.53 versus 0.41 gives 29.3% - consistent only with unrounded mean entries, recorded as a rounding-level gap rather than a contradiction.

### Negative evidence

1. Source's own headline: **zero of thirty** horizon-by-edge cells return a gross ROI whose interval clears zero, before fees and after paying the executable spread (Section 4.5, Table 7).
2. The single significantly negative gross cell (-10.01%, [-19.7, -0.5]) shows the bad-model route losing at zero cost; fees only deepen it (5 cells negative at the sample's 0.03 tariff, 8 at 0.05).
3. The information that does exist does not convert: partial r-squared below 1% from T-6h onward, and it is concentrated in markets whose book is a wrapper rather than a price (Section 4.3).
4. Discrimination deficit: the live ensembles rank below the market (0.638 / 0.627 vs 0.738 / 0.739) and even below their own rating input; the clean rebuild is calibrated and still ranks below the market (-0.065, interval excluding zero) - a deficit a calibrator provably cannot repair (Section 4.2).
5. Specification trap: the negative edge coefficient a naive regression reports is omitted-variable bias, and the sign/trend invert when the mid is controlled for (Sections 3.1, 4.4, 5.2) - a cheap diagnostic that cuts against a whole class of "edge versus market price" claims.
6. The only large positive number in the record (+71.5% gross, 66 markets) was withdrawn by the source and fails its own half-split (-25.1% / +174.2%).
7. Power: intervals of +/-7 to +/-13 percentage points mean a true +5% edge would not be distinguishable from zero in most cells - the source's own claim is non-detection, not absence (Sections 4.5 and 6).
8. Maker branch: the only cells with intervals above zero rest on an unobserved fill; adverse selection versus a resting quote cannot be separated without fill and order-flow data, and the capacity bound assumes sweeping the whole visible book (Sections 4.5, 5.3, 6).
9. External convergent negative evidence cited by the source: bookmaker consensus already beat eleven statistical and rating models (Kovalchik 2016); tennis ML accuracy plateaus near 70-75% and the market is not reliably beaten (Wilkens 2021); on Polymarket NBA the surviving arbitrage opportunities have median life of a few seconds with executability binding (Yang, Cheng and Zou 2026); on prediction markets what separates winners from losers is execution rather than information (Vedova 2026); the theoretical bad-model profit route of Hubacek and Sir (2023) is argued to lose its premises on a fee-bearing CLOB.
10. Evidence pointing the other way, kept explicit: Clegg and Cartlidge (2025) report positive returns on high-intransitivity tennis matchups against Pinnacle (subset-level, walk-forward, with calibration); the source does not refute it and argues its own horse race plus grid is the tradability stress test such claims need. Clinton and Huang (2025) and others report Polymarket political markets as noisy/inefficient, in tension with the calibration headline - the source resolves this as a domain and metric difference (Section 2.1) and does not test it.
11. On the bookmaker slice the source's own data cut against the middle link of its literature chain: the market's AUC is below the book's by 0.009-0.010, where Reichenbach and Walther (2025) report Polymarket slightly outperforming bookmaker odds (Section 4.6, n = 220, 4% of the sample).
12. Selection and scope limits: one sport, one season, one venue, one surface transition; the model priced only about a third of resolved markets, self-selected by its own modelability; the joined V4 sample is lower-tour heavy; tour/level/surface fields empty for 65.2% of the catalog.
13. Data-integrity incidents inside the source itself: catalog rating leakage (94.9% of catalogs equal the final scan; +25 points on the later match at p < 1e-16), a withdrawn earlier claim that the mid "under-weights its own future mid", a withdrawn Roland Garros-versus-rest contrast, three upstream artefacts not preserved in the archive (the original match-selection routine, the live training tables, V3's shadow_log file), and a live-pipeline defect where eight V3 markets emit last-scan probabilities between 1.45 and 1.83.
14. No multiplicity correction anywhere (thirty grid cells plus ten horizon regressions); the source argues the uncorrected bias is conservative because it favours spurious positives and it reports none.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** (Scout-chosen, not source-reported) unless the text says `source-reported`. Each gate states data, sample/regime, metric, threshold and action. The hypothesis under test is the source's negative claim: *no collectable pre-match ML taker edge on a calibrated event-contract CLOB*.

- **F1 - Printed-value reproduction.** Data: SSRN PDF 90569c6009c5422dd9b538730d09298fa439bf64904d910885b02f43ad0018ef. Threshold: all thirty Table 7 cells (n, entry, ROI, CI), ECE10 0.0088 / 0.1315 / 0.1219, AUC 0.638 / 0.627 / 0.738 / 0.739 / 0.670 / 0.735, partial r-squared row of Table 6, and Z = -0.27 / +3.00 / 16.7 / 15.2 are re-extracted from the pinned PDF text. Action: any mismatch = stop, mark the record contested.
- **F2 - Sample-window and data-availability go/no-go.** Data: Polymarket Gamma/CLOB public history. Threshold: reconstructable order-book history covering the declared window with both sides quoted and resolutions available for >= 95% of tracked markets; per-market fee field absent is accepted as a known gap. Action: if the public history cannot be rebuilt for the window, mark `data gap` and halt before any return computation.
- **F3 - Prospective shadow-protocol replication (source-reported design, research-defined size).** Data: a new frozen window starting 2026-10-02, predictions logged to an append-only timestamped log before resolution. Threshold: >= 1,000 resolved tracked-side observations with a valid mid. Action: below n = 1,000, do not compute the grid; extend the window instead.
- **F4 - Market calibration gate (source-reported metric).** Threshold: market ECE10 ratio to its own simulated floor <= 1.2 and Spiegelhalter p > 0.05 at the T0 anchor on the new window. Action: if the market is not calibrated, the source's premise fails and the hypothesis must be re-stated before testing tradability.
- **F5 - Executable taker grid, multiplicity-controlled.** Data: same grid construction as Section 4.5 (horizons G, executable-edge terciles, ask entry, hold to resolution, aggregate ROI, 1,000 (payoff, stake) bootstrap draws) but with an ex-ante edge threshold instead of an ex-post tercile (`research-proposed`: threshold fixed at the mid-spread). Threshold (research-defined): **any cell with fee-net ROI whose 95% interval lower bound > 0 after Benjamini-Hochberg at q = 0.10 across all cells falsifies the non-detection claim**. Action: if a cell clears, the record flips to `contested: true` and the edge goes to an independent replication lane before any implementation talk.
- **F6 - Discrimination gate.** Data: matched market-versus-challenger-model sample. Threshold (research-defined): paired model-minus-market AUC difference whose 95% interval includes 0 or is positive, at n >= 400. Action: that outcome refutes "the binding deficit is discrimination" and requires re-reading the source's Section 4.2 chain.
- **F7 - Calibration-over-accuracy check.** Threshold (research-defined): a challenger model with ECE10 ratio to its own floor <= 1.2 **and** AUC within 0.01 of the market's on the same matches. Action: if both hold, the source's claim that a calibrated model still loses on ranking no longer generalizes; re-open.
- **F8 - Omitted-variable-bias sign diagnostic (source-reported, cheap).** Fit specification C and specification D on the same sample. Threshold: sign and trend must invert (C negative and strengthening, D positive and decaying), and the identity `beta_C = beta_B_model + beta_D_mid * delta` must reproduce to 0.001. Action: if it does not reproduce, the source's C4 diagnostic is wrong and any negative edge coefficient in our own work cannot be dismissed as OVB.
- **F9 - As-of leakage audit (source-reported method).** For every feature stored in a rewritten table, regress the between-appearance change on the earlier and the later match result. Threshold (research-defined): the later-match loading must not exceed the earlier one at p < 1e-6. Action: on failure, discard the affected feature read and re-run from timestamped logs only.
- **F10 - Book-formation stratification.** Data: spread at the read. Threshold (research-defined): in the tight stratum (spread <= 0.05) the model's partial r-squared of the pre-start price must be >= 5% with the coefficient significant under tournament-clustered errors before any absorption claim is made. Action: below that, the day-out fit is classified as wrapper-stratum artifact, as the source itself does.
- **F11 - Maker-branch admissibility.** Threshold: maker claims require fill and order-flow data with adverse-selection measured; absent that, `data gap` and no maker claim. Action: keep the maker branch out of every downstream summary.
- **F12 - Capacity and depth gate.** Threshold (research-defined): executable notional within 20% of visible top-of-book depth at every entry, and a monthly capacity ceiling computed from depth, not from a full-book sweep. Action: if capacity cannot be bounded, report returns strictly as per-unit quantities, as the source does.
- **F13 - Cost ladder.** Fees at 0 / 0.03 / 0.05 taker tariffs plus hypothetical additional costs of 0 / 1 / 2 / 5 / 10 bps per side, with gas and capital carry added. Threshold (research-defined): the claim of non-detection must hold at every ladder point (no cell clears zero). Action: any ladder point where a cell clears zero after F5's multiplicity control falsifies the non-detection claim.
- **F14 - Frozen forward window.** Data: 2026-10-02 onward for at least 12 months on the same venue. Threshold (research-defined): F5 and F6 evaluated once at the end of the window with no re-tuning. Action: report the single pre-declared verdict; a failed gate at that point flips `contested` to true, a passed gate keeps the record research-only but upgrades confidence only after independent reproduction.

**Global no-retuning rule (applies to every gate):** freeze the first-scan-as-forecast convention, the p_pre and T0 anchors, the horizons H and G, the executable-edge side-selection rule, the terminal flat-sizing accounting, the 1,000-replicate (payoff, stake) bootstrap, the fee tariffs 0.03 and 0.05, the wrapper/tight spread cuts at 0.02 / 0.05 / 0.10, the Platt-scaling-invariance control, and every F1-F14 threshold above. Any change to these mid-stream resets the exercise to a new, separately declared study.

## Crypto portability

**direct** - with an explicit boundary on what "direct" covers.

The venue is crypto-native and the execution mechanics are demonstrated there by the source itself: an on-chain settled central limit order book, outcome tokens bought at an executable ask and held to resolution, a taker fee schedule, maker rebates, settlement and gas treated as on-chain costs, and market-side data taken from public Gamma and CLOB endpoints. Nothing in the venue, fee, spread, settlement or data path needs to be ported for the mechanism to be re-tested on Polymarket.

What is **not** direct: the predictive input. The signal is a tennis win-probability ensemble built on public match records; the underlying is a sport, not a crypto price. Porting the *hypothesis* ("a pre-event model's disagreement with a calibrated CLOB mid does not survive the executable spread and a taker fee") to BTC/ETH event contracts or to crypto-price markets would be a **research-proposed adaptation**, is `unproven` here, and is not evidence from this record - the source explicitly states its result is about one feature family and one sport (Sections 5.4, 6).

Crypto-specific risks the source covers or exposes: 24/7 venue versus nominal tennis start times (the source anchors short of start precisely because scheduled starts slip); catalogue/deployment-driven fee grandfathering with no per-market fee field (a point-in-time hazard on any fee-bearing crypto venue); maker-branch fills unobservable without order-flow data; venue capacity modelled only by a full-book-sweep bound. Crypto-specific items the source does **not** cover and which remain `data gap`: spot-versus-perpetual differences, funding, cross-venue fragmentation for event contracts, custody/withdrawal risk, and listing/delisting churn of the sports catalogue. The venue's separate US exchange runs a different uniform fee schedule and is outside the study.

## Limitations

- `not independently reproduced` - every number above is source-reported; only arithmetic identities were checked.
- One venue, one sport, one season, one surface transition (late April to mid-June 2026); seasonal, tier and venue effects are confounded in a sample of this shape.
- One model family; a model using a genuinely different information set (intransitivity, injury/travel intelligence, in-play state) is untested and not answered by this paper.
- `underspecified`: the exact fee formula (prose proportionality plus two rates, no equation), the ensemble feature list/hyperparameters, the timezone convention for scheduled start and scan stamps, and the printed `e_B = bid_A - p_hat` symbol choice.
- `data gap`: no per-market fee field on the public catalog (so no fee-free control); replication package "available from the author on request" and promised for a public repository on publication - no public code or data repository exists at capture time; the companion microstructure paper is "in preparation"; depth, queue, partial fills and latency are not in the accounting; peer-review status not stated.
- Capacity is not modelled in the grid; every return is a per-unit quantity assuming a top-of-book fill.
- Paper trading only - no capital deployed, all returns counterfactual.
- Terminal flat accounting only: early exit, hedging and any edge- or price-responsive sizing are untested, and a negative result for hold-to-resolution flat staking does not extend to them.
- Power: the grid cannot separate a true +5% edge from zero in most cells; the correct reading is non-detection.
- No multiplicity correction on thirty cells or ten horizon regressions (bias direction argued to be conservative for a negative claim).
- Self-selected model coverage (about one third of resolved markets), non-nested population counts, reconstructed matched samples after upstream artefacts were lost, a disclosed live-pipeline defect (8 V3 markets with probabilities 1.45-1.83 on last scan), and one file (V3 shadow_log) absent from the working tree and archives.
- Withdrawn results are recorded rather than deleted (the +71.5% rule, the Roland Garros contrast, the earlier "under-weights its own future mid" claim), which is good practice but means headline numbers moved between drafts - treat any earlier circulated version as stale.
- Publication-bias relevance: this is a negative-result preprint on SSRN with 0 references registered in Crossref and near-zero reads at capture time; it has not been cited or replicated anywhere we could find.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack. No shadow log, no Polymarket collector, no ensemble, no tercile or threshold grid, no fee ladder and no falsification gate has been run by us. No Qlib full backtest, no Paper, no Testnet and no Live verification of any kind has occurred. The source itself is counterfactual/paper only - no capital was deployed during its study window.

## Adoption boundary

Frontmatter stays `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`, `contested: false`, `confidence: medium` (confidence in the research interpretation, not in profitability). This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. The source's own conclusion is negative - "No taker strategy earns a gross return significantly above zero" - and nothing here may be worded as an endorsed edge, a validated strategy or an approval to trade.

## Related Wiki records

- [[quant/prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02]]
- [[quant/prediction-market-llm-confidence-weighted-value-bet-2026-09-04]]
- [[quant/kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13]]
- [[quant/polymarket-favorite-longshot-bias-crypto-politics-2026-09-14]]
- [[quant/crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01]]

All five vault paths were existence-checked on disk as real files before linking; no Wiki page was written or modified by this run. Repository-side neighbours distinguished in Provenance: the layered informed-trading skill-score record, the Kalshi Wang-transform executable-spread falsification record, the Polymarket-versus-Binance binary threshold record, the League of Legends pregame parity record, and the Polymarket favourite-longshot record.

## Sources

- Dmitrii Yushkov, "Model Edge or Model Miscalibration? A Prospective Test on Polymarket Tennis", SSRN abstract id 7550440, 34 pages, Date Written October 01, 2026, posted 2 Oct 2026. Landing page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7550440 (read 2026-10-02).
- DOI: https://doi.org/10.2139/ssrn.7550440 (Crossref posted-content, group-title SSRN, publisher Elsevier BV, created 2026-10-02T11:39:26Z; API record read 2026-10-02 at https://api.crossref.org/works/10.2139/ssrn.7550440).
- Primary PDF, fetched from the SSRN `Delivery.cfm` endpoint linked by that landing page through a browser-cleared session on 2026-10-02: 349,803 bytes, SHA-256 90569c6009c5422dd9b538730d09298fa439bf64904d910885b02f43ad0018ef, 34 pages. Every quantitative claim in this record cites its Section, Table or Figure inside that PDF.
- Venue fee documentation cited inside the source (not consulted directly by us): Polymarket Help Center, "Trading Fees" and "Maker Rebates Program", help.polymarket.com, accessed July 2026 (source footnote 1).
