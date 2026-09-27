---
schema: strategy-research-record-v1
title: "Ethereum Demand-Side Fee Flow Deviation and 10-60 Day ETH Return Predictability (SSRN 7003998)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - ethereum
  - on-chain
  - fundamental
  - fee-flow
  - valuation
  - return-predictability
  - regime-break
  - preprint
status: research-only
confidence: medium
source_as_of: 2026-07-18
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7003998"
  - "https://doi.org/10.2139/ssrn.7003998"
  - "SSRN Open PDF in Browser delivery link for abstract_id=7003998 (download.ssrn.com presigned object), pinned locally 2026-09-27"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ethereum Demand-Side Fee Flow Deviation and 10-60 Day ETH Return Predictability (SSRN 7003998)

## Provenance

Page numbers in this record are physical pages of the pinned PDF (1-47 = main text, whose printed folio matches the physical page; 48-55 = Online Appendix, which restarts its own numbering at 1-8). Table and section identifiers are the source's own.

- **Primary source:** SSRN preprint, `abstract_id=7003998`, DOI [`10.2139/ssrn.7003998`](https://doi.org/10.2139/ssrn.7003998). Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7003998>.
- **Exact title.** PDF p.1 title block: `Demand-side fee flows and return predictability on Ethereum`. Landing page heading: `Demand-Side Fee Flows and Return Predictability on Ethereum`. Capitalisation differs only; recorded, not reconciled.
- **Authors, recorded exactly as each surface prints them; the two surfaces disagree on one affiliation and are not reconciled.**
  - PDF p.1 title block, in printed order: **Lucas Dünnes** with superscript `a`, then **Jens Felsenstein-Eckberg** with superscript `*`; affiliation line `aMAJOR KEY Research GmbH, Regensburg`; footnote `*Corresponding author: jens@felsenstein-eckberg.com`.
  - Landing page author headings: **Lucas Dünnes** - `University of Regensburg`; **Jens Felsenstein-Eckberg** - `affiliation not provided to SSRN`.
  - Landing page `Suggested Citation`: `Dünnes, Lucas and Felsenstein-Eckberg, Jens, Demand-Side Fee Flows and Return Predictability on Ethereum (June 26, 2026). Available at SSRN: https://ssrn.com/abstract=7003998 or http://dx.doi.org/10.2139/ssrn.7003998`.
  - Discrepancy: Dünnes's affiliation is `MAJOR KEY Research GmbH, Regensburg` in the PDF versus `University of Regensburg` on the landing page; Felsenstein-Eckberg's affiliation is present only as "not provided to SSRN". PDF metadata `/Author` is `Lucas Dünnes; Jens Felsenstein-Eckberg; ` (trailing separator).
- **Dates (both printed; not reconciled).** Landing page: `Posted: 18 Jul 2026`, `55 Pages`, `Date Written: June 26, 2026`. PDF metadata: `/CreationDate D:20260626165639Z` (2026-06-26), `/ModDate D:20260626185812+02'00'`, `/Creator LaTeX with hyperref`, `/Producer pdfTeX-1.40.27`, `/Title Demand-side fee flows and return predictability on Ethereum`.
- **Publication / peer-review status.** No journal, volume, issue or conference appears on the landing page, and the strings `peer review`, `peer-review`, `under review`, `submitted` and `forthcoming` return **zero** hits in the whole pinned text, while `ssrn` occurs **zero** times outside the reference list (the only occurrence is the Jermann 2023 reference entry). No acknowledgement, funding or conflict-of-interest statement exists (`acknowledg` appears once, only as `We acknowledge that the native-unit construction attenuates...`). Status: **preprint; peer-review, journal, funding and conflict status all `not stated in source`.**
- **Rights (recorded, not interpreted).** The landing page prints `The copyright holder has granted SSRN a license` and `All rights reserved. No reuse allowed without permission.` This record therefore normalises only the source's own claims, printed values, section references and table identifiers, and does not reproduce the source's prose at length.
- **Reference / citation metadata discrepancy (recorded, not repaired).** The landing page prints `0 References` (with an unfetched `Fetch References` button) and `0 Citations`, while the PDF's own main-text reference list (pp.45-47) contains **44** entries counted entry by entry (script-counted), of which **6** are repeated in the Online Appendix reference list (p.55).
- **Landing-page statistics at read time (2026-09-27):** 96 downloads, 220 abstract views, 0 citations. Landing-page keywords `Decentralized Finance, Return Predictability, Protocol Governance, Ethereum`; JEL `G12, G14, C58`.
- **Pinned primary source.** PDF obtained 2026-09-27 through the SSRN `Open PDF in Browser` delivery link (a `download.ssrn.com` presigned object), **909,210 bytes, 55 pages**, SHA-256 `0b8442bd53cf323a1d95f878a1a68b28a4a7a81a7f00043ad684b678da53fd0f`. Text extracted page by page with `pypdf` 6.16.2 to 103,287 characters; all 55 pages carry a text layer and every page was read in full before this record was written. Page count agrees with the landing page's `55 Pages`.
- **Sample window (all printed, mutually consistent).** Full sample `September 15, 2022 (the Merge) through March 17, 2026, yielding 1,280 daily observations` (section 4.1, p.15). Regime partitions (Appendix B, p.44): pre-Dencun `September 15, 2022 to March 12, 2024 (542 daily observations)`; post-Dencun full `March 13, 2024 to March 17, 2026 (735 daily observations)`; **post-Dencun clean RRR (primary analysis sample) `June 11, 2024 to March 17, 2026 (645 daily observations)`**. Control-bearing specifications use `N = 571` (section 5, p.21; Table 7, p.33). Data as-of 2026-03-17; no post-March-2026 data appears.
- **Universe.** Single asset: ETH. Dependent variables are cumulative ETH/USD log returns over k in {10, 20, 30, 45, 60} days, with cumulative ETH/BTC relative log returns as the ETH-specificity check (Table 1 Panel C, p.14).
- **Transaction-cost treatment (Methods-level determination, see Execution assumptions).** There is no cost model: the source models no fee schedule, spread, slippage, impact, turnover, capacity, latency, fill, funding, borrow, leverage, margin or liquidation, and makes exactly one prose assertion about round-trip costs in section 7. Every trading-cost field in this record is `data gap`, never zero.
- **Code / data availability.** No code-availability statement, data-availability statement, replication package, repository URL or `github` string appears anywhere in the pinned text (word scan: `github` 0, `available at` 0; `code` occurs twice, both meaning `encoded in protocol design`). The dataset is the authors' own `Ethereum Valuation Terminal` daily dataset (footnote 3, p.15; `Dünnes, L., 2025. Ethereum: Building a valuation framework for a decentralized blockchain. Master's thesis. University of Regensburg.`) aggregating Etherscan, Beaconcha.in and ultrasound.money. Every availability field is `not stated in source`.
- **Pre-write source-identity dedup (hidden-inclusive, executed 2026-09-27).** `rg -uuu` over all files in the repository, including `.mimo-worktrees`, `.agents` and `.hermes`, for `7003998`, `Demand-Side Fee Flows`, `Demand-side fee flows`, `Felsenstein`, `Dünnes`, `Dunnes`, `Flow Deviation`, `Rolling Reference Rate`, `Ethereum Valuation Terminal` and `MAJOR KEY`: **zero hits for every pattern**. Adjacent-term scans: `fee intensity` - 3 hits, all in `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` where it denotes an L1 transaction-cost weight in a portfolio optimiser, unrelated; `Dencun` - 9 files, all incidental mentions of scheduled protocol upgrades as event risk inside unrelated equity records (`earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13.md`, `single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13.md`, `crypto-cross-sectional-style-investing-transaction-speed-habitat-2026-09-01.md`) with no fee-to-return mechanism. `coverage_manifest.csv` (1,088,787 bytes) contains none of the identity patterns. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup.
- **Four-axis distinction against the nearest existing records (source identity and mechanism differ in every pair).**
  1. Repo record `crypto-cross-sectional-onchain-user-activity-growth-2026-08-31.md` (Liu & Tsyvinski, `Risks and Returns of Cryptocurrency`, DOI `10.1093/rfs/hhaa113`): different source identity; that record is a **cross-sectional adoption-growth factor over many coins** built from active addresses / transaction counts / payment counts, this record is a **single-asset (ETH only) time-series valuation deviation** built from fees scaled by supply and differenced against a trailing median; signal construction (growth of activity levels vs log-ratio to a rolling median), universe (multi-coin cross-section vs one asset), horizon (monthly cross-sectional rebalance vs 10-60 day forward horizons) and material data dependency (address/tx counts vs Etherscan fee aggregates plus a protocol-upgrade regime gate) all differ.
  2. Repo record `bitcoin-onchain-nvt-signal-macro-cycle-2026-08-31.md` (woobull / Glassnode NVT): different source identity and asset; NVT is a **price-reflexive ratio** (market cap / transaction volume) so the numerator contains the price being predicted, whereas Flow Intensity is **entirely price-free** (ETH fees / ETH supply) by construction; NVT-Signal uses an oscillating band, Flow Deviation uses a trailing-median log deviation.
  3. Repo record `ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01.md` (arXiv 2411.06327): different source identity; exchange net-inflow is a **custody/transfer-flow** signal at **1-6 hour** horizons, this is a **protocol-fee throughput** signal at **10-60 day** horizons.
  4. Repo record `ethereum-whale-deposit-asymmetric-sell-signal-long-horizon-edge-2026-09-05.md` (GitHub `zty05070242/whale-signals` at commit `f0972c6...`): different source identity; **whale event study** on deposit/withdrawal counts versus **continuous fee-intensity valuation deviation**; different signal construction, different data dependency (large-holder labels vs fee aggregates).
  5. Repo record `bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01.md`: fund-flow demand signal on a regulated wrapper at next-day horizon, versus a native-protocol throughput signal at multi-week horizon.
- **Scope of this record.** The source is an asset-pricing / return-predictability study; it contributes a signal and an identification argument, not an executable trading rule. The source itself states it should be read as an equilibrium valuation signal `rather than as a trading strategy` (section 7, pp.37-38). Nothing here is independently reproduced.

## Economic mechanism

### Source-reported

The source's question is whether protocol-native, token-denominated economic flows are capitalised into token prices in an environment with no firm, no contracts and no residual cash-flow rights (sections 1 and 7, pp.3-4, 35-37).

Construction, exactly as printed (section 3, pp.7-12):

- `EconFlows_t = F_base_t + F_prio_t + B_t` (eq.1, p.9) - demand-side fees only: execution-layer base fee (burned), execution-layer priority fee, and blob/data-availability fee. Consensus-layer issuance is explicitly excluded as a supply-side parameter and enters only as a control (sections 2.2, 3.1). Pre-Dencun `B_t = 0` mechanically.
- `FI_t = EconFlows_t / S_t` (eq.2, p.9) - Flow Intensity, a dimensionless ratio denominated entirely in ETH, described as `the fraction of the token base "earned" by the protocol through demand-side activity`.
- `FI_t = (1/30) * sum_{j=0}^{29} FI_{t-j}` (eq.4, p.10) - 30-day trailing arithmetic mean, stated to filter gas spikes, airdrop farming and MEV, and set `ex ante as a calendar-month frequency` (OA.2, p.49).
- `RRR^h_t = Median(FI_{t-1}, FI_{t-2}, ..., FI_{t-h})` (eq.5, p.10) - Rolling Reference Rate over `h in {90, 180, 270, 360} days (denoted 3M, 6M, 9M, 12M)`; median rather than mean because fee distributions are heavily right-skewed. Note the window starts at `t-1`, so the benchmark excludes the current day.
- `FD^h_t = ln(FI_t / RRR^h_t)` (eq.6, p.11) - Flow Deviation, the primary signal. Positive = current demand-side activity above its own trailing median.
- `FD momentum: Delta FD^{h,l}_t = FD^h_t - FD^h_{t-l}` (eq.9, p.12), with `l = 14 days` primary and a 6-month variant (Table 1 Panel A, p.14).
- Component signals `FD_EL` and `FD_DA` from execution-layer and blob intensities (eqs.7-8, p.11).

Stated hypothesis: `beta > 0` - when current flows exceed their trailing median, `subsequent returns should be positive as the market corrects toward fundamentals` (section 4.3, p.17). The source's analogy is earnings/cash-flow-to-price ratios and post-earnings-announcement drift (section 7, pp.36-37).

Identification argument (section 4.4, pp.20-21): native-unit measurement breaks the mechanical USD-price-to-fee link; the rolling median dampens price-driven speculation spikes; all right-hand sides are lagged (`FD_t predicts r_{t+1:t+k}`); and the Dencun upgrade (EIP-4844, activated March 13, 2024) is treated as a quasi-exogenous structural break whose timing `was determined by development milestones years before activation and is orthogonal to contemporaneous market prices` (section 2.3, p.7).

The source reports that raw fee levels carry no information: replacing FD with the raw log level of total fees smoothed at 30, 60 or 90 days `produces no predictive power whatsoever (t<0.6 at all horizons)` (OA.2, p.49).

### Research interpretation

Component roles, normalised so each can be ablated independently:

```text
Signal:       FD(h) = ln( 30-day mean(FI) / trailing median(FI, h days) )
              h = 3M is the headline (and the pre-specified primary test is
              FD(3M) -> 45-day forward return, section 4.3 p.17)
Secondary:    FD momentum = FD_t - FD_{t-14d}, evaluated against the 6M reference
Universe:     ETH only; ETH/USD primary dependent variable, ETH/BTC as the
              ETH-specificity check
Horizon:      forward cumulative return over k in {10, 20, 30, 45, 60} days
Regime gate:  primary estimates restricted to post-Dencun clean-RRR dates
              (2024-06-11 onward); a Dencun dummy plus interaction is used on
              the full sample
Control:      native-unit construction (fees in ETH / ETH supply) - no fiat input
Execution:    NONE specified by the source (it is a predictive regression, not a
              trading rule)
```

Hypothesised mechanism: **slow capitalisation of protocol throughput fundamentals** - a flow-to-price mean-reversion / underreaction channel, for which the source offers a descriptive weekly error-correction speed of `alpha = -0.087` implying `a half-life of approximately ln(2)/0.087 = 8 weeks` (section 5.6, p.28), consistent with the 45-60 day peak.

Competing explanations the record must keep alive (the source itself raises all three):

1. **Price-driven fee endogeneity.** Rising prices attract users and raise fees; the source reports `r = 0.21` between FD(3M) and past ETH returns at a 45-day lookback (sections 4.4, 5.8) and finds price Granger-causes fees at daily frequency (p<0.01) and weekly frequency (F=4.63, p=0.033), while fees Granger-cause price only weakly at daily frequency and **not at all** at weekly frequency (F=0.59, p=0.445; section 5.6).
2. **Sample-window artefact of one protocol upgrade.** The entire effect exists only after March 2024; the source concedes it `cannot rule out that the post-Dencun results reflect a one-time structural adaptation rather than a permanent regime` (section 8, p.40).
3. **Selection across the reference-horizon / forecast-horizon grid.** 4 reference horizons x 5 return horizons = 20 in-sample cells, with the source noting the 6-month window was `originally hypothesized` while the 3-month window is the reported winner (section 5.2, p.23; OA.2, p.49).

Ablation is mandatory before believing the mechanism: the decisive test is whether FD beats a circularly shifted fee series, and whether the effect survives when the trailing median is replaced by a trailing mean or by a non-fee activity measure.

## Signal

All parameters below are `source-reported` unless tagged. Where the source prints nothing, the gap is marked; no operational value has been invented.

**Formation timestamp and tradability.** Daily frequency; fee totals are `computed by summing all transaction-level fees within each UTC day` (Appendix A.1, p.41); all market and macro series are `aligned to UTC daily observations` (Table A1 note, p.42). FD is formed at the end of day `t` from FI up to `t` and the trailing median over `t-1 ... t-h`; the dependent variable is `r_{t+1:t+k}` (Table 1 Panel C, p.14). The source states `All predictive Specifications use lagged right-hand-side variables: FD_t predicts r_{t+1:t+k}. This ensures temporal precedence.` (section 4.4, p.20). The exact execution convention (which price on day t+1 the return is measured to, and when a tradable order would be sent) is `not stated in source` -> `data gap`.

**Lookback.** Smoothing: 30-day trailing arithmetic mean (eq.4). Reference: trailing median over h = 90 / 180 / 270 / 360 days (eq.5), excluding the current day. Momentum: l = 14 days (primary) and 6 months (Table 1 Panel A). Warm-up: the clean-RRR primary sample starts 90 days after Dencun precisely so that the 3-month reference window is fully post-Dencun (Appendix B, p.44). Endpoints: the median window is explicitly `FI_{t-1}, ..., FI_{t-h}` (inclusive of `t-h`, exclusive of `t`).

**Entry.** `not stated in source`. The source specifies no direction rule, no threshold, no order type and no trigger; it reports regressions. A rule of the form `be long ETH when FD(3M) > 0` is an obvious reading of the reported sign split (section 5.2) but is **`research-proposed`**, not source-reported.

**Exit / holding period / re-entry.** `not stated in source`. The natural mapping of a k-day forward-return regression is a k-day holding window (k = 10, 20, 30, 45, 60 days), but no exit, stop, rebalance cadence or overlap rule is printed -> `data gap`. Whether overlapping positions are permitted is `not stated in source`.

**Position sizing.** `not stated in source`. The source reports no portfolio construction, no weights, no volatility targeting and no leverage; the strings `portfolio`, `long-short`, `long only` and `Sharpe` return **zero** hits in the pinned text.

**Parameters and their provenance.**
- Source-reported: `30` day smoothing; `h in {90, 180, 270, 360}` days; `l = 14` days and 6 months; `k in {10, 20, 30, 45, 60}` days; `180`-day minimum training window for the expanding OOS exercise; a `60/40` static split as sensitivity; Newey-West HAC bandwidth `floor(1.5 * k)`; `2,000` moving-block bootstrap replications (OA.1); `1,000` random placebo regime dates (section 6); the pre-specified primary test `FD(3M) predicting 45-day forward returns on the post-Dencun clean RRR sample` (section 4.3, p.17).
- `underspecified`: Table 1 describes h as `{3M, 6M, 9M, 12M} (calendar months)` while section 3.3 gives `{90, 180, 270, 360} days`; these are treated as equivalent here but the source never states how a `calendar month` median window is dated.
- `research-proposed`: any entry threshold, any sign rule, any stop, any sizing rule, any re-entry rule, any capacity limit. None of these appear in the source and none are used anywhere in this record except in the falsification plan, where every cutoff is `research-defined`.

## Required data

- **Instrument:** ETH spot price (ETH/USD) plus on-chain fee, burn, issuance and supply series for the Ethereum mainnet. No derivative is required by the source.
- **Universe:** single asset, ETH. No inclusion/exclusion rule, no liquidity filter, no listing-age filter, no survivorship handling - because there is no universe -> `data gap` for anything universe-like.
- **Venue / vendor (Table A1, p.42):** Etherscan (execution-layer base fee, execution-layer priority fee, blob base fee, blob priority fee, circulating supply); Beaconcha.in (consensus-layer issuance, total effective balance, active validators, validator entry/exit queues); ultrasound.money (execution-layer burn); CoinGecko (ETH/USD daily closing price, described as `volume-weighted average`); Alternative.me (Crypto Fear & Greed Index); `Public market data` for BTC/USD, S&P 500, NASDAQ Composite, US Dollar Index and 10-year Treasury yield - **the vendor for those five series is unnamed** -> `underspecified`. Cross-validation: `Each series is cross-validated with at least one independent aggregator` (section 4.1, p.15), with no named second aggregator for every series -> partially `data gap`.
- **Timeframe:** daily bars, UTC day boundaries; weekly and monthly aggregations used in robustness (OA.9). The 24/7 session convention relative to a daily close, and whether the ETH/USD `daily closing price` is taken at 00:00 UTC or at CoinGecko's own snapshot time, are `not stated in source` -> `data gap`.
- **Fields:** total demand-side fees (EL base + EL priority + DA base + DA priority, all in ETH), circulating supply, consensus-layer issuance, EL burn, net issuance, total effective balance / staking ratio, ETH/USD close, BTC/USD close, S&P 500, NASDAQ, DXY, 10-year yield, Crypto Fear & Greed Index; plus constructed FD, Delta FD, FD_EL, FD_DA and forward cumulative returns.
- **Point-in-time:** no publication-lag, revision or availability convention is described for any series -> `data gap`. Because the fee and supply series are protocol-native and append-only this is a lower risk than for macro data, but the five unnamed market/macro series have no point-in-time provenance at all -> `underspecified`.
- **Missing data:** no null, stale, suspended or bad-print handling rule appears anywhere -> `data gap`. Imputation is `not stated in source`. The claim of `1,280 daily observations` over 2022-09-15 to 2026-03-17 implies no missing calendar days, but no completeness check is reported.
- **Funding / fee / spread needs:** protocol fees are the *signal*, not a trading cost. For any tradable reading the source supplies no maker/taker schedule, no spread, no slippage, no impact, no participation, no capacity, no latency, no fill model, no funding, no borrow and no liquidation rule -> **every one of these is `data gap`, never zero.**

## Execution assumptions

- **The source does not present a trading rule.** Section 7 (pp.37-38): the Flow Deviation is to be interpreted `as an equilibrium valuation signal, an analogue to the dividend-price ratio or cash-flow yield ... rather than as a trading strategy: fees are capitalized into token valuations through equilibrium price adjustment, not arbitrage.` Order type, fill model, signal-to-order delay, reference price, partial fills and failure handling are therefore all `not stated in source`.
- **The single cost statement (source-reported, section 7, p.37):** `The predicted magnitudes are economically large, a one-standard-deviation increase in FD(3M) implies roughly 4-8 percentage points of additional 30-45 day return, and comfortably exceed plausible round-trip trading costs, since on-chain execution for institutional-sized positions and centralized-exchange fees are both modest (Park, 2023).` The cited Park (2023) is `The conceptual flaws of decentralized automated market making`, *Management Science* 69 - a paper about AMM design, not an ETH round-trip cost measurement; **no cost rate, fee tier, venue or spread number is printed anywhere in the 55 pages** -> `underspecified`.
- **Scout arithmetic on that sentence (labelled `research interpretation`, not a source claim):** Table 2 (p.22) prints `FD (3M)` standard deviation `0.32`; Table 3 (p.24) prints `beta = 0.282` at 30 days and `0.456` at 45 days. `0.282 * 0.32 = 0.090` and `0.456 * 0.32 = 0.146`, i.e. about **9.0 and 14.6 log-return points**, not 4-8 percentage points. The source repeats the 4-8 pp figure in section 7 (p.37) but never prints the standard deviation it used, so the bridge between its prose magnitude and its printed coefficient/standard-deviation pair is `underspecified`.
- **Word scan of the pinned 55-page text (Methods-level, whole-document):** `transaction cost` / `transaction costs` **2** (one is the literature-review sentence in section 1 about fee mechanisms shaping transaction costs; one is the section 7 paragraph quoted above), `round-trip` **1** (the same sentence), `trading strategy` **1** (the same disclaimer), `slippage` **0**, `bid-ask` **0**, `spread` **1** (meaning the above-trend minus below-trend *return* spread in section 5.2, not a bid-ask spread), `turnover` **0**, `latency` **0**, `fill` **0**, `maker` **0**, `taker` **0**, `market impact` **0**, `commission` **0**, `funding` **0**, `liquidation` **0**, `leverage` **0**, `margin` **3** (all meaning `marginally significant` / `statistical margin`), `borrow` **0**, `backtest` **0**, `Sharpe` **0**, `drawdown` **0**, `CAGR` **0**, `portfolio` **0**, `risk-free` **0**. `capacity` occurs **10** times but every occurrence means protocol **block** capacity, never trading capacity.
  -> fee schedule, spread, slippage, market impact, participation, trading capacity, latency, fill/partial-fill, funding, borrow, leverage, margin and liquidation are all **`data gap`, never zero.**
- **Borrow / shorting.** The reported sign split (`FD(3M) <= 0` days followed by `-4.7%` over 10 days and `-18.0%` over 45 days, section 5.2, p.24) cannot be avoided without a short or a hedge, yet the document contains no short leg, no borrow source, no borrow cost and no perpetual-funding treatment (word scan above) -> `data gap`.
- **Turnover / capacity.** At k = 45 days an implementable reading of the regression would trade roughly 8 times a year plus whatever the sign rule implies; the source never computes turnover, traded notional, ADV participation or capacity -> `data gap`.
- **Leverage / margin / liquidation:** `not stated in source` -> `data gap`.
- **Latency / partial fills / failures:** `not stated in source` -> `data gap`.

## Evidence

### Source-reported

Every figure below is `source-reported`, traced to the pinned PDF (SHA-256 `0b8442bd...3fd0f`) at the table/section/page stated. All evidence is crypto (ETH) evidence; none of it is equity, commodity or traditional-futures evidence. None has been independently reproduced.

**Descriptive statistics - Table 2, p.22 (post-Dencun clean RRR, N = 645)**

| Variable | N | Mean | Std | Min | Median | Max |
|---|---|---|---|---|---|---|
| ETH/USD Price | 645 | 2975.37 | 753.89 | 1514.35 | 2946.74 | 4791.51 |
| Daily ETH Return (%) | 645 | -0.07 | 2.97 | -18.50 | 0.08 | 14.90 |
| Flow Intensity (x10^6) | 645 | 5.67 | 6.29 | 0.51 | 3.17 | 49.90 |
| Smoothed FI (30d, x10^6) | 645 | 5.93 | 4.73 | 0.82 | 3.74 | 18.10 |
| FD (3M) | 645 | 0.08 | 0.32 | -0.75 | 0.04 | 0.87 |
| FD (6M) | 645 | -0.13 | 0.48 | -1.30 | -0.06 | 0.74 |
| Realized Vol (ann.) | 645 | 0.54 | 0.12 | 0.28 | 0.54 | 0.84 |
| Daily BTC Return (%) | 645 | 0.01 | 2.48 | -15.24 | -0.00 | 11.80 |

**Main predictability - Table 3 Panel A, p.24 (overlapping returns, Newey-West HAC bandwidth `floor(1.5k)`, post-Dencun sample)**

| Reference h | k=10 | k=20 | k=30 | k=45 | k=60 |
|---|---|---|---|---|---|
| 3M beta | 0.080*** | 0.171*** | 0.282*** | 0.456*** | 0.458*** |
| 3M t-stat | 2.65 | 3.22 | 3.86 | 3.83 | 2.93 |
| 3M R2 | 5.1% | 10.0% | 15.7% | **22.8%** | 17.1% |
| 3M N | 635 | 625 | 615 | 600 | 585 |
| 6M beta | 0.040 | 0.071 | 0.092 | 0.095 | 0.017 |
| 6M t-stat | 1.62 | 1.31 | 1.01 | 0.68 | 0.11 |
| 6M R2 | 2.9% | 4.0% | 4.0% | 2.5% | 0.1% |
| 9M beta / t | 0.019 (0.69) | 0.025 (0.46) | 0.020 (0.23) | -0.018 (-0.14) | -0.138 (-0.88) |
| 12M beta / t | 0.023 (0.77) | 0.033 (0.53) | 0.032 (0.31) | -0.003 (-0.02) | -0.138 (-0.76) |

Significance stars are the source's: `***/**/*` = 1%/5%/10%.

**Non-overlapping blocks - Table 3 Panel B, p.24:** 20-day blocks `N=32, beta=0.222, t=2.68, R2=19.4%`; 30-day `N=21, beta=0.282, t=2.11, R2=19.0%`; 45-day `N=14, beta=0.487, t=2.43, R2=33.0%`; 60-day `N=10, beta=0.647, t=1.70, R2=26.6%` (the last not starred).

**Sign split - section 5.2, p.24:** days with `FD(3M) > 0` followed by `+2.7%` (10 days) and `+10.7%` (45 days); days with `FD(3M) <= 0` followed by `-4.7%` (10 days) and `-18.0%` (45 days); unconditional spread `+28.7%` at 45 days. No hold-out version of this spread is reported.

**FD momentum - Table 4, p.25 (`Delta FD(14d, 6M)`, post-Dencun):** k=30 `beta=0.158, t=1.54` (not starred); k=45 `beta=0.412, t=3.54***, R2=13.6%`; k=60 `beta=0.589, t=5.07***, R2=20.8%`. The source calls `t = 5.07 at 60 days` `the strongest single result in the analysis` (p.26).

**Regime interaction - Table 5, p.26 and section 5.4:** on the full sample with a Dencun dummy `D_Dencun = 1(t >= March 13, 2024)`:

| Horizon | beta_1 (pre-Dencun) | delta (interaction) | Total post-Dencun |
|---|---|---|---|
| 30 days | -0.105 | 0.252** | 0.147 |
| 45 days | -0.114 | 0.382** | 0.268 |
| 60 days | -0.072 | 0.369** | 0.297 |

Chow test at Dencun (section 5.4, p.26): `F ~ 2.0, p = 0.13` at the 1-day horizon; `F > 25` for multi-day windows (`F ~ 25 at k = 20 days; p < 0.0001`). Regime interaction p-values at the actual Dencun date `p = 0.030-0.047` (section 6, p.34). Execution-layer fees are `99.2%` of Flow Intensity post-Dencun, blob fees `0.8%` (section 5.5, p.27); data-availability fees fell `approximately 72%` after Dencun (section 5.4, p.26).

**Component horse race - Table OA.7, p.54 (post-Dencun, Newey-West):**

| k | univariate beta_EL (R2) | horse-race beta_EL | horse-race beta_DA | R2 |
|---|---|---|---|---|
| 30d | 0.275*** (14.9%) | 0.281*** (4.49) | -0.001 (-0.20) | 15.0% |
| 45d | 0.455*** (22.8%) | 0.511*** (5.08) | -0.007 (-1.56) | 27.2% |
| 60d | 0.455*** (16.7%) | 0.552*** (4.29) | -0.012** (-2.14) | 27.3% |

**Lead-lag and error correction - section 5.6, pp.28-29 and Table OA.6, p.53:** daily Granger, price -> fees `p < 0.01`, fees -> price `p < 0.05` at some lag orders; weekly, price -> fees `F = 4.63, p = 0.033`, fees -> price `F = 0.59, p = 0.445`. Johansen trace: daily `5.15`, weekly `8.86`, 5% critical value `15.49` - the null of no cointegration is **not rejected** in either sample. VECM speed-of-adjustment on the price equation: daily `alpha = -0.0081` (p = 0.064), weekly `alpha = -0.0866` (p = 0.022), giving the source's `half-life ~ 8 weeks`; `N = 645` daily / `N = 93` weekly; 5 lags daily, 3 lags weekly. The source explicitly labels these `descriptive rather than structural`.

**Out-of-sample - Table 6, p.29 (FD(3M) predictor):**

*Panel A, single 60/40 split:* 20d `IS 19.2%, OOS -6.4%, DirAcc 53.4%, rho 0.086 (p=0.1884), N=238`; 30d `25.0%, -4.3%, 48.7%, 0.210 (p=0.0014), N=228`; 45d `22.9%, +3.5%, 68.1%, 0.458 (p<0.0001), N=213`; 60d `9.7%, -4.1%, 61.1%, 0.569 (p<0.0001), N=198`.

*Panel B, expanding window (180-day minimum training, expanded daily):* 30d `N=435, OOS R2 9.0%, DirAcc 67.1%, Pos.Freq 37.7%, Lift 29.4pp, rho 0.406***, Clark-West t 7.73***`; 45d `N=420, 14.4%, 76.4%, 35.5%, 41.0pp, 0.479***, 9.16***`; 60d `N=405, 10.3%, 73.1%, 41.0%, 32.1pp, 0.475***, 9.63***`.

*Panel C, rolling 180-day window (re-estimated daily):* 30d `N=435, OOS R2 3.3%, DirAcc 64.6%, Lift 26.9pp, rho 0.324***, CW t 8.15***`; 45d `N=420, -2.0%, 64.3%, 28.8pp, 0.332***, 7.19***`; 60d `N=405, -19.7%, 54.8%, 13.8pp, 0.252***, 4.01***`.

**Controls - Table 7, p.33 and section 5.8 (N = 571):** column (1) FD(3M) alone `beta 0.452, t 3.81, R2 22.6%`; (2) plus ETH momentum 7d/30d `0.487, t 3.71, R2 23.5%`; (3) plus BTC momentum 7d `0.484, t 3.68, R2 23.7%`; (4) plus annualised realised vol, delta log(tx count), delta log(active addresses) `0.483, t 3.71, R2 25.5%`. No control coefficient is individually significant. Panel B incremental R2 of FD over the full control set: 30d `16.3 -> 19.0`; 45d `22.6 -> 25.5`; 60d `16.6 -> 19.5` (N 571/571/556). Macro variables explain `4.5%` of FD(3M) variation and `18.2%` of Delta FD variation (section 5.8, p.31). Correlation of FD(3M) with past ETH returns: `r ~ 0.12` at 7 days, `r ~ 0.21` at 45 days (sections 4.4, 5.8).

**Placebo on the structural break - section 6, p.34:** against `1,000 randomly assigned regime dates drawn from the full sample`, the actual Dencun interaction t-statistic falls near the `65th-71st percentile`; restricted to a `+/-60-day window around the actual Dencun date`, it falls at `roughly the 51st percentile at all horizons (30, 45, 60 days)`.

**Multiple testing - footnote 4, p.30:** `20 implicit hypothesis tests`; best raw `p = 0.0002` for FD(3M) at k=30d; Bonferroni-adjusted `p = 0.005`; Holm-Bonferroni adjusted `p < 0.013` for all horizons 10-60 days.

**Robustness appendix:**
- OA.1 (p.48), quantile regressions with moving-block bootstrap (block = k, 2,000 replications). k=45d: tau 0.10 `beta 0.398, t 2.37**`; 0.25 `0.586, 3.28***`; 0.50 `0.548, 3.41***`; 0.75 `0.381, 2.39**`; 0.90 `0.223, 1.00` (not significant). k=60d: `0.431 (1.94*)`, `0.586 (2.20**)`, `0.726 (3.00***)`, `0.369 (1.53)`, `0.161 (0.76)`. The source notes i.i.d. quantile inference produces t-stats `3-5 times larger` (e.g. `t = 11.55` at tau=0.10/45d vs bootstrap `2.37`).
- OA.2 (p.49): peak t-stat / peak R2 by reference horizon - `3M (3.87 at 30d) / 22.8% at 45d`, `6M (2.81 at 45d) / 14.2% at 45d`, `9M (2.30 at 45d) / 10.5% at 45d`, `12M (1.95 at 45d) / 8.1% at 45d`, with `Significant horizons` of `10d,20d,30d,45d,60d` / `30d,45d` / `30d,45d` / `30d (marginal)`. Smoothing sweep (EWMA): significant at 5% for spans `7 days (t=3.89)`, `14 days (t=3.63)`, `30 days (t=2.26)`, **not** for `60 days or longer`. Raw log fee level at 30/60/90-day smoothing: `t < 0.6 at all horizons`.
- OA.3 (p.50): Stambaugh (1999) bias correction; `rho = 0.991`, `Corr(u,v) = 0.086`, estimated bias `< 0.005` in absolute value, `beta_OLS = 0.456` vs `beta_adj = 0.456` at 45d; printed `t-stat OLS` / `t-stat adj` of `5.82/5.81, 8.33/8.25, 10.70/10.63, 13.27/13.26, 10.96/11.06` for k = 10/20/30/45/60. Amihud-Hurvich (2004) augmented regression at 45d: `beta = 0.457, t = 3.76`.
- OA.4 (p.51): Hodrick (1992) vs Newey-West t - `10d 2.12 (p=0.034) vs 2.65`, `20d 2.45 (0.014) vs 3.21`, `30d 2.61 (0.009) vs 3.86`, `45d 2.78 (0.006) vs 3.83`, `60d 1.89 (0.059) vs 2.93`; local-to-unity `c = N(rho-1) ~ -5.6`; Campbell-Yogo Bonferroni Q critical `t ~ 2.58` at 1%.
- OA.5 (p.52), ETH/BTC relative returns: `10d 0.042 (2.21**) R2 3.2%`, `20d 0.085 (2.20**) 6.0%`, `30d 0.138 (2.30**) 8.9%`, `45d 0.239 (2.55**) 14.7%`, `60d 0.275 (2.23**) 13.9%`.
- OA.8 (p.54): raw vs macro-orthogonalised p-values - FD(3M) 20d `0.0010 -> 0.0060`, 30d `<0.001 -> 0.0020`, 45d `<0.001 -> <0.001`, 60d `0.0030 -> 0.0010`; Delta FD 45d `0.0004 -> 0.0210`, 60d `<0.0001 -> 0.0002`.
- OA.9 (p.55): weekly `FD(3M)` 6wk `p=0.046, R2 10.7%`, 8wk `p=0.042, R2 11.3%`; weekly `Delta FD(2w,6M)` 8wk `p=0.041, R2 8.5%`; monthly `FD(3M)` 2mo `p=0.017, R2 14.8%`, 1mo `p=0.074`; monthly `Delta FD` 2-3mo `p=0.034-0.037`; `Monthly sample: N = 25`.

**Bootstrap quantile regressions are significant from the 10th through the 75th percentile with the strongest effects in the left tail** (section 6, p.35, referring to OA.1).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. The source explicitly disclaims being a trading strategy: the Flow Deviation is presented as an equilibrium valuation signal `rather than as a trading strategy` (section 7, pp.37-38). No entry rule, direction rule, exit, sizing, rebalance or portfolio construction exists anywhere in the 55 pages; `portfolio`, `Sharpe`, `long-short` and `backtest` all return zero hits.
2. **No transaction-cost model.** The only cost content in the whole document is one prose sentence in section 7 asserting that 4-8 pp magnitudes `comfortably exceed plausible round-trip trading costs` while citing an AMM-design paper (Park, 2023). Word scan: `slippage`, `bid-ask`, `turnover`, `latency`, `fill`, `maker`, `taker`, `market impact`, `commission`, `funding`, `liquidation`, `leverage`, `borrow` = **0 hits each**; `spread` occurs once and means a return spread; `capacity` occurs 10 times but always means protocol block capacity.
3. **Out-of-sample results are horizon- and window-dependent.** Single 60/40 split gives negative OOS R2 at 20d (-6.4%), 30d (-4.3%) and 60d (-4.1%) (Table 6 Panel A); the rolling 180-day window gives **-2.0% at 45d and -19.7% at 60d** (Panel C). Only the expanding window is positive everywhere, and only the expanding-window figure (14.4% at 45d) is quoted in the abstract and conclusion.
4. **Directional accuracy below chance in one headline cell:** single-split 30-day DirAcc `48.7%` (Table 6 Panel A); rolling 60-day `54.8%` with a lift of only `13.8pp` (Panel C).
5. **The lift benchmark is the weaker of the two naive rules.** The source reports `Lift = DirAcc - Pos.Freq` (76.4% - 35.5% = 41.0pp at 45d). Scout arithmetic, `research interpretation`: an always-short rule scores `1 - 0.355 = 64.5%` in the same OOS window, so the lift over the better naive rule is about **11.9pp** (and 4.8pp at 30d, 14.1pp at 60d), not 41.0pp. The source prints only the always-long comparison.
6. **The effect exists in only one regime.** Pre-Dencun coefficients are negative and insignificant at every horizon (Table 5: -0.105 / -0.114 / -0.072), and the 1-day Chow test is not significant (`F ~ 2.0, p = 0.13`).
7. **The structural-break placebo is weak by the source's own numbers.** Against 1,000 random regime dates the actual interaction t sits at only the `65th-71st percentile`; against +/-60-day matched dates it sits at `roughly the 51st percentile` at 30, 45 and 60 days (section 6, p.34) - i.e. indistinguishable from the median placebo date. The source frames this as a power limitation.
8. **No cointegration.** Johansen trace `5.15` (daily) and `8.86` (weekly) against a 5% critical value of `15.49` (Table OA.6), so the ~8-week half-life is explicitly descriptive; the source states the VECM `does not satisfy the Johansen rank condition` (section 8, p.39).
9. **The source's own lead-lag test fails to find fee -> price causality at weekly frequency:** `F = 0.59, p = 0.445` for fees -> price versus `F = 4.63, p = 0.033` for price -> fees (section 5.6), even though the headline claim operates on 45-60 day horizons.
10. **Near-unit-root predictor.** FD(3M) has `AR(1) rho = 0.991` (Table OA.3); the source computes local-to-unity `c = N(rho-1) ~ -5.6` and concedes standard t critical values may be liberal in that range (OA.4). Hodrick t at 60 days is `1.89, p = 0.059` - not significant at 5%.
11. **Selection across a 20-cell grid.** 4 reference horizons x 5 return horizons were estimated, and the source itself says the 6-month window was `originally hypothesized` while the 3-month window is the promoted winner (section 5.2; OA.2). Footnote 4's Bonferroni/Holm correction is applied to the same 20 in-sample cells and does not address the parallel smoothing-span sweep (7/14/30 days work, 60+ do not, OA.2) or the momentum lookback choice.
12. **The primary sample window is defined by the selected horizon:** the clean-RRR sample starts exactly 90 days after Dencun `determined by the reference horizon of the primary signal` (Appendix B, p.44), so sample definition and parameter choice are not independent.
13. **Right-tail predictability is absent.** Quantile coefficients are insignificant at tau = 0.90 at both 45d (`0.223, t=1.00`) and 60d (`0.161, t=0.76`) under block bootstrap (Table OA.1), and the source concedes i.i.d. standard errors would have produced t-stats `3-5 times larger`.
14. **Overlap inflates precision and R2, and the source never adjusts for it.** The 22.8% R2 at k=45 comes from 600 overlapping observations of which Panel B finds only **14** non-overlapping blocks; OOS directional accuracy and Clark-West `t = 9.16` are likewise computed on ~420 overlapping forward returns (about 9 independent 45-day windows). No effective-sample or overlap-adjusted R2 is printed -> `data gap`.
15. **Source-internal contradiction in the reference-horizon table.** Table 3 Panel A prints 6M `t = 1.62/1.31/1.01/0.68/0.11` with `R2 = 2.9/4.0/4.0/2.5/0.1%`, 9M `t = 0.69/0.46/0.23/-0.14/-0.88`, and 12M `t = 0.77/0.53/0.31/-0.02/-0.76` (no star anywhere), while Table OA.2 for the same sample and method reports 6M `peak t = 2.81 at 45d, peak R2 = 14.2% at 45d, significant at 30d and 45d`, 9M `2.30 / 10.5% / significant at 30d,45d`, 12M `1.95 / 8.1% / 30d marginal`. Section 5.2's prose (`significance concentrated at intermediate horizons (30-45 days)`) follows OA.2, not Table 3. These cannot both be correct; recorded unreconciled.
16. **The 9M and 12M rows of Table 3 are near-duplicates:** both print `beta = -0.138` at k=60 and near-identical values at every other k, which is a plausible transcription defect in the source -> `underspecified`.
17. **Source-internal inconsistency in reported t-statistics.** Table 3 Panel A gives Newey-West t of `2.65 / 3.22 / 3.86 / 3.83 / 2.93` for FD(3M), while Table OA.3 prints `t-stat OLS` of `5.82 / 8.33 / 10.70 / 13.27 / 10.96` for the same coefficients without stating which standard errors those are; and Table 3 gives `3.22` at k=20 while Table OA.4 lists the corresponding Newey-West value as `3.21`. Recorded unreconciled.
18. **The source's headline economic magnitude does not follow from its printed coefficient and standard deviation.** `4-8 percentage points` (sections 5.2 and 7) versus `0.282 * 0.32 = 9.0` and `0.456 * 0.32 = 14.6` log-return points from Tables 2 and 3; the standard deviation used for the 4-8 pp claim is never printed -> `underspecified`.
19. **Partially endogenous predictor by the source's own admission:** `r = 0.21` between FD(3M) and 45-day past returns; `The modest correlation with past returns underscores the importance of interpreting FD as a demand-side fundamental measure with a partially endogenous feedback loop` (section 5.8); residual endogeneity is explicitly conceded in section 4.4.
20. **The second fee channel the construction was built to separate carries no positive pricing content:** execution-layer fees are `99.2%` of Flow Intensity, blob fees `0.8%` (section 5.5), and the DA coefficient is *negative and significant* at 60 days (`-0.012, t = -2.14`, Table OA.7).
21. **Effect decay is conceded:** `the signal is stronger in the first post-Dencun year, consistent with gradual learning`, and the source `cannot rule out that the post-Dencun results reflect a one-time structural adaptation rather than a permanent regime` (section 8, p.40).
22. **Small effective samples:** 645 primary daily observations; `N = 14` non-overlapping 45-day blocks; `N = 10` at 60 days; `N = 25` monthly observations (Table OA.9).
23. **The +28.7% sign spread is in-sample only** - computed on the same cells used to select FD(3M) and k = 45 (section 5.2); no hold-out or forward version of the spread is reported.
24. **Provenance-level discrepancy:** Dünnes's affiliation differs between the PDF (`MAJOR KEY Research GmbH, Regensburg`) and the SSRN landing page (`University of Regensburg`); the landing page prints `0 References` and `0 Citations` while the PDF carries a 44-entry main-text reference list.
25. **The data are the authors' own product** (`Ethereum Valuation Terminal`, maintained by the authors; `Dünnes, 2025` master's thesis) with no code, no data-availability statement and no replication package -> none of Tables 2-7 or OA.1-OA.9 can be regenerated from the source alone.
26. **No short leg, borrow, funding, leverage, margin, liquidation or trading-capacity treatment exists anywhere** (word scan), so the bearish half of the signal - `FD(3M) <= 0` followed by `-18.0%` over 45 days - has no specified implementation path and no costed hedge.
27. **Five of the control-series vendors are unnamed** (`Public market data` for BTC/USD, S&P 500, NASDAQ, DXY and the 10-year yield, Table A1) -> point-in-time provenance `underspecified`.
28. **Publication status is unverifiable from the source:** no journal, no peer-review statement, no funding or conflict statement, no acknowledgement, `ssrn` appears nowhere outside the reference list, and the landing page shows `0 Citations` -> preprint with all such fields `not stated in source`.

## Falsification plan

All thresholds below are `research-defined falsification thresholds` chosen by the Scout; all reconstruction parameters not printed by the source are `research-proposed`. Failure action for every test is: **do not advance the hypothesis past research-only, and record the failure in this record.**

1. **F1 - Frozen forward replication.** Implement FD(3M) exactly as printed (30-day mean of daily FI, trailing median over `t-1 ... t-90`, `FD_t` against `r_{t+1:t+45}`) with no re-tuning, and run forward from `2026-10-01` for 24 months. Fail if the expanding-window OOS R2 at 45 days is `<= 0` or directional accuracy is `<= 50%`. (`research-defined`.)
2. **F2 - Table recovery gate.** Rebuild Table 3 Panel A and Table 6 Panel B from public data before any forward claim. Fail if FD(3M) 45-day beta is outside `0.456 +/- 0.03`, R2 outside `22.8% +/- 2.0pp`, or expanding OOS R2 outside `14.4% +/- 3.0pp`. (`research-defined` tolerances; failure means the source's own numbers cannot be recovered, so stop.)
3. **F3 - All-in cost ladder.** Trade the `research-proposed` rule `long ETH while FD(3M) > 0, flat otherwise, k = 45` at per-side costs of `0 / 1 / 2 / 5 / 10 / 20 bp`. Fail if the source-reported `+10.7%` average 45-day above-trend return (section 5.2) loses `> 50%` at `5 bp` or turns negative at `10 bp`. (`research-defined`.)
4. **F4 - Short-leg feasibility gate.** To monetise the `-18.0%` below-trend side, source an ETH short (perpetual or borrow) and charge its all-in carry (funding / borrow fee plus spread). Fail if the charged carry absorbs `> 50%` of the source-reported `-18.0%`, or if no short is continuously available across the sample. (`research-defined`.)
5. **F5 - Full-sample regime placebo, tightened.** Repeat the source's own 1,000-draw random-date placebo and require the actual Dencun interaction t-statistic to exceed the **95th** percentile of the null. Fail if it does not. (`research-defined`: 1,000 draws, 95th percentile; the source reports only 65th-71st.)
6. **F6 - Time-controlled regime placebo, tightened.** With placebo dates restricted to +/-60 days around Dencun, require the actual interaction t to exceed the **90th** percentile at 30, 45 and 60 days. Fail otherwise. (`research-defined`; the source reports roughly the 51st percentile.)
7. **F7 - Overlap-adjusted inference.** Re-estimate the 45-day regression on strictly non-overlapping blocks only and report R2 on the resulting independent observations. Fail if block R2 `< 10%` or the block t-statistic `< 1.96`. (`research-defined`; source prints N = 14, R2 = 33.0%, t = 2.43 - this test is designed to be re-runnable and to expose variance.)
8. **F8 - Alternative-estimator inference.** Re-run FD(3M) at 45 days under the Campbell-Yogo Q-test and a fixed-b (Kiefer-Vogelsang) HAC. Fail if FD(3M) is not significant at 5% under either. (`research-defined`.)
9. **F9 - Circular-shift placebo on the fee series (decisive mechanism test).** Circularly shift the daily Flow Intensity series `1,000` times, rebuilding FD and re-estimating each time. Fail if the observed 45-day beta is below the `95th` percentile of the null. (`research-defined`: 1,000 draws, 95th percentile.)
10. **F10 - Endogeneity partial-out.** Orthogonalise FD(3M) against 7-day and 30-day ETH momentum, BTC return and annualised realised volatility **jointly** (the source orthogonalises against macro only), then re-test. Fail if the residual coefficient is not significant at 5%. (`research-defined`.)
11. **F11 - Specificity test on BTC.** Re-estimate the identical construction on BTC with no re-tuning (same equations, same horizons, same regime logic applied to BTC's own fee history). Fail if the BTC FD(3M) 45-day coefficient is not positive - a positive BTC result would show the effect is a generic fee/activity artifact rather than an Ethereum-specific valuation channel, and a null would show it does not generalise. (`research-defined`.)
12. **F12 - Second-platform replication.** Re-estimate on a second fee-market chain (e.g. an alternative L1 or an L2 with its own EIP-1559-style market) using the same construction. Fail if the sign is not positive. (`research-defined`.)
13. **F13 - Multiplicity control.** Apply Benjamini-Hochberg over the full tested family (4 reference horizons x 5 return horizons x 2 signals (level, momentum) x 2 frequencies (daily, weekly) x the reported subsamples and split schemes). Fail if any surviving claim has `q >= 0.10`. (`research-defined`.)
14. **F14 - Clean-room reproduction gate.** An independent re-implementation must reproduce Table 2 summary statistics, Table 3 beta/R2/N cells, and all three panels of Table 6 within `+/- 10%` relative error, and must resolve the Table 3 versus Table OA.2 contradiction (Negative evidence item 15) by locating which specification each table actually reports. Fail otherwise. (`research-defined`: 10% relative.)

## Crypto portability

**direct.**

The evidence is itself crypto: ETH on the Ethereum mainnet, daily UTC data from 2022-09-15 to 2026-03-17, ETH/USD returns sourced from CoinGecko, with ETH/BTC as the relative-return check. The signal is built entirely from protocol-native quantities (fees in ETH, supply in ETH), so no fiat-denominated input and no traditional-asset result is being re-labelled as crypto evidence. No porting step is required.

`direct` is not a tradability or adoption statement. Residual crypto-specific gaps that remain *inside* this direct setting are `data gap`: no funding / borrow / leverage / margin / liquidation treatment for the short side of the signal; the daily close used for ETH/USD is a CoinGecko `volume-weighted average`, not an executable venue price, and no executable-price reconciliation is given; venue fragmentation for the traded leg is not addressed (single aggregate index price, no book depth); 24/7 UTC candle boundaries are used without a session-convention discussion; custody and withdrawal risk for any implementation is unmodelled; the ETH/BTC leg requires a second asset and possibly a second venue with no execution assumption stated; trading capacity, latency and partial fills are unaddressed.

## Limitations

- `data gap`: any transaction-cost, spread, slippage, impact, participation, trading-capacity, latency, fill, funding, borrow, leverage, margin or liquidation treatment; execution timestamp and order convention; missing-data handling; point-in-time/revision conventions for every series; turnover of any implementable rule; code and data availability.
- `underspecified`: the bridge between the source's `4-8 percentage points` prose magnitude and its printed coefficient/standard-deviation pair; the standard error type behind Table OA.3's `t-stat OLS` column; the vendor of the BTC and macro control series; the exact dating convention of a `calendar month` reference window.
- `not stated in source`: any entry, exit, sizing, rebalance or portfolio rule; any Sharpe, drawdown, CAGR, win-rate or turnover statistic (all zero hits); peer-review status, journal status, funding and conflict statements.
- Source-quality: SSRN preprint, `All rights reserved. No reuse allowed without permission.`, no replication package, dataset is the authors' own product, and multiple internal contradictions (Negative evidence items 15, 16, 17, 24) - so even the `source-reported` figures should be treated as unverified third-party claims.
- Identification: the predictor is admitted to be partially endogenous (r = 0.21 with 45-day past returns), weekly Granger tests find no fee -> price causality, Johansen rejects no-cointegration nowhere, and the regime-break placebo only reaches the 65th-71st (or 51st) percentile of its own null.
- Sample / regime: the whole effect lives in one ~24-month post-Dencun window; the pre-Dencun coefficient is negative; the source concedes possible one-time structural adaptation and reports stronger effects in the first post-Dencun year.
- Statistical power: 645 primary observations, 14 non-overlapping 45-day blocks, 25 monthly observations; overlapping-return inference inflates apparent precision and no effective-sample adjustment is printed.
- Selection / publication bias: the promoted cell is the winner of a 20-cell grid plus a smoothing-span sweep plus a momentum-window choice, and the primary sample start was defined by the winning reference horizon.
- Capacity / execution: unaddressed entirely; the negative half of the signal requires a short ETH leg whose cost and availability are never discussed.
- Reproducibility: `not independently reproduced`; nothing in our stack has regenerated any number in this record.
- Incremental-write check: this record was written only after a hidden-inclusive repo-wide source-identity search returned zero hits for the DOI, exact title, both author names, `Flow Deviation`, `Rolling Reference Rate` and `Ethereum Valuation Terminal`; the nearest existing records differ in source identity and in mechanism (see Provenance, four-axis distinction).

## Implementation status

`not-implemented`. No part of this signal exists in our research stack: no Ethereum fee/supply data pipeline, no Flow Intensity or Flow Deviation estimator, no rolling-reference-rate builder, no predictive regression, no portfolio simulator, no backtest, no Paper, no Testnet, no Live. Nothing in this record implies Qlib full-backtest validation or any survivor status.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

`status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`. No wording, evidence count, confidence value or schedule behaviour in this record promotes it.

## Related Wiki records

Verified Wiki Brain pages (paths returned by `kb_search` on 2026-09-27). Queries that returned **zero** pages, so no page for this exact mechanism is claimed: `ethereum protocol fee intensity flow deviation return predictability valuation` (0), `Ethereum staking liquid staking basis yield protocol` (0), `fee market blockspace MEV layer 2 rollup` (0), `on-chain user activity growth cross-sectional network adoption factor` (0), `crypto on-chain metrics valuation NVT MVRV fundamental` (0 relevant hits).

Adjacent verified pages:

- [[quant/ethereum-whale-deposit-asymmetric-sell-signal-long-horizon-edge-2026-09-05]]
- [[quant/ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01]]
- [[quant/crypto-cross-chain-attention-negative-spillover-capital-reallocation-2026-09-06]]
- [[quant/crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]]
- [[quant/crypto-hourly-bitcoin-walk-forward-cost-aware-execution-2026-09-01]]

Adjacent records in **this repository** (not Wiki links, listed for dedup transparency): `crypto-cross-sectional-onchain-user-activity-growth-2026-08-31.md`, `bitcoin-onchain-nvt-signal-macro-cycle-2026-08-31.md`, `ethereum-exchange-net-inflow-bearish-drift-1h-6h-2026-09-01.md`, `ethereum-exchange-net-inflow-conditioned-call-selling-2026-09-03.md`, `ethereum-whale-deposit-asymmetric-sell-signal-long-horizon-edge-2026-09-05.md`, `bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01.md`, `blockchain-metrics-ribbon-cross-sectional-btc-onchain-indicators-2026-09-03.md`.

## Sources

1. Lucas Dünnes and Jens Felsenstein-Eckberg, `Demand-side fee flows and return predictability on Ethereum`, SSRN preprint, `abstract_id=7003998`, DOI [`10.2139/ssrn.7003998`](https://doi.org/10.2139/ssrn.7003998), `Date Written: June 26, 2026`, `Posted: 18 Jul 2026`, 55 pages. Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7003998>. Rights statement `All rights reserved. No reuse allowed without permission.`; peer-review and journal status `not stated in source`. The affiliation of Lucas Dünnes differs between the PDF (`MAJOR KEY Research GmbH, Regensburg`) and the landing page (`University of Regensburg`) and is recorded unreconciled in Provenance.
2. Pinned PDF (same work, retrieved 2026-09-27 through the SSRN `Open PDF in Browser` delivery link): 909,210 bytes, 55 pages, SHA-256 `0b8442bd53cf323a1d95f878a1a68b28a4a7a81a7f00043ad684b678da53fd0f`; text extracted page by page with `pypdf` 6.16.2 to 103,287 characters and every page read. All table/section/page provenance in this record refers to this file.
3. Dataset named by the primary source as its own dependency, **not** used as independent evidence by this record: `Ethereum Valuation Terminal` daily dataset, footnote 3, p.15, aggregated from Etherscan, Beaconcha.in and ultrasound.money (`Dünnes, L., 2025. Ethereum: Building a valuation framework for a decentralized blockchain. Master's thesis. University of Regensburg.`).
4. Works cited inside the primary source and named here only as the source's own dependencies, **not** used as independent evidence by this record: Park, A., 2023, `The conceptual flaws of decentralized automated market making`, *Management Science* 69, 6731-6751 (the citation attached to the source's only transaction-cost sentence); Liu, Y., Tsyvinski, A. & Wu, X., 2022, `Common risk factors in cryptocurrency`, *Journal of Finance* 77, 1133-1177 (the control-factor construction); Cong, L. W., Li, Y. & Wang, N., 2021, `Tokenomics: Dynamic adoption and valuation`, *Review of Financial Studies* 34, 1105-1155 (the theoretical frame); Campbell, J. Y. & Thompson, S. B., 2008 and Clark, T. E. & West, K. D., 2007 (the OOS R2 and Clark-West statistics reported in Table 6).
