---
schema: strategy-research-record-v1
title: "KSE Sentinel: Rule-Based Trend-Continuation on a 30-Symbol Pakistan Stock Exchange Universe with a Deflated-Sharpe Multiple-Testing Floor, an Independent ~2000-2020 Archive Claim, and a 60-Day Live Forward-Paper Program (SSRN 7093159, companion 7102818)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - trend-following
  - time-series-momentum
  - frontier-markets
  - pakistan-stock-exchange
  - rule-based
  - backtest-overfitting
  - deflated-sharpe-ratio
  - walk-forward-validation
  - live-forward-test
  - single-venue
  - withheld-parameters
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-07-28
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7093159"
  - "https://doi.org/10.2139/ssrn.7093159"
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7102818"
  - "https://doi.org/10.2139/ssrn.7102818"
  - "https://www.linkedin.com/posts/abbas-ertiza_algorithmictrading-quantfinance-psx-share-7479859295233167361-nr_u/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The same paper is posted twice on SSRN one day apart under two distinct abstract IDs and DOIs - 7093159 (14 pages, 'Posted: 28 Jul 2026', PDF /CreationDate D:20260710185728+08'00', filed under 'Capital Markets: Asset Pricing & Valuation' and 'Capital Markets: Market Efficiency', DOWNLOADS 53 / ABSTRACT VIEWS 143 at read time) and 7102818 (13 pages, 'Posted: 29 Jul 2026', PDF /CreationDate D:20260712092232+08'00', filed under 'Macroeconomics: Production & Investment' and 'Operations Research', DOWNLOADS 74 / ABSTRACT VIEWS 161 at read time). Both landings print 'Date Written: July 07, 2026' and the identical abstract, and both carry the control 'There are 2 versions of this paper' even though they are two separate submissions rather than one versioned submission. Page counts differ by one. A normalised sentence-level diff of the two pinned PDFs shows only hyphenation, line-wrap and spacing differences plus 'yFinance' to 'yfinance' and 'primary data vendor (Yahoo Finance)' to 'primary data vendor', with no numeric or claim difference found. Which posting is authoritative is not stated and is not reconciled here."
  - "Section 6.3 states that the paper reports 'a statistically corrected assessment of how much of that Sharpe ratio survives once the number of prior strategy variants considered is accounted for', but the section then prints the result as the literal unfilled placeholder 'The resulting Deflated Sharpe Ratio figure is [to be confirmed from run_fresh_dsr_analysis.py output]'. The headline multiple-testing correction the paper is organised around is therefore absent from both pinned PDFs, unreconciled."
  - "Section 5.4 states that performance against an equal-weight buy-and-hold benchmark over the same window and universe 'is reported', but the pinned 14-page PDF contains only two tables - the Section 5.1 headline table and the Section 5.5 sizing comparison - and no benchmark figure appears anywhere in the text. The claimed benchmark comparison is not present in the document, unreconciled."
  - "The abstract states that the paper reports 'results from an ongoing 60-day live forward-paper validation program initiated July 2026', but Section 7 reports only program design, persistence of scan decisions and two operational incidents; no forward return, win rate, Sharpe, trade count or drawdown for the live window is printed. The promised forward results are absent, unreconciled."
  - "The paper's single cost number is phrased two ways: the abstract says 'net of realistic transaction costs (commission, slippage, and spread totalling 22.5 basis points per leg)' while Section 3.4 says 'All reported returns are net of an assumed 22.5 basis points in round-trip trading costs per leg'. 'Per leg' (one-way) and 'round-trip' (both legs) differ by a factor of two, and the abstract drops the word 'assumed' that Section 3.4 uses. Unreconciled."
  - "Both SSRN landing abstracts and both PDF abstracts open ' present KSE Sentinel, a fully rule-based ...' - the sentence subject (presumably 'We') is missing on every surface, in both pinned PDFs, and the same defect is reproduced verbatim in the SSRN abstract text of both postings."
  - "Both SSRN landings print the headings '0 References' and '0 Citations' while the pinned PDF reference list prints six entries (Jegadeesh and Titman 1993; Moskowitz, Ooi and Pedersen 2012; Hurst, Ooi and Pedersen 2017; Bailey and Lopez de Prado 2014; Bailey, Borwein, Lopez de Prado and Zhu 2014; Securities and Exchange Commission of Pakistan 2025)."
  - "The sizing-comparison section is labelled '.5 Sizing Sensitivity: 3% vs. 5% Risk Per Trade' - the leading '5' of '5.5' is missing - in both pinned PDFs, immediately after Section 5.4."
  - "In the pinned 14-page PDF the identical six-item 'Suggested full citations' block is printed twice, on page 4 and again on page 5; the companion 13-page posting carries the same duplicated block."
  - "Section 6.3 defines the Deflated Sharpe Ratio trial count as N = 4, explicitly 'the 1%/3%/4%/5% sizing candidates', but the paper prints results only for the 3% and 5% tiers (Sections 5.1 and 5.5). The 1% and 4% cells are never reported, so the trial set used for the correction is only partly visible; the source also names at least five further prior experiments (a 5.5% sizing variant, an earlier stricter entry rule, an RSI-oversold gate, and two 'trap-immune' signal variants) that are excluded from N because they were 'abandoned before producing a comparable Sharpe figure'."
  - "The secondary source reached through the paper's own printed testing link states that the system 'was subjected to extensive backtesting against 20 years of historical PSX data', while the paper's primary window is 2021-2026 and its independent archive is described as '~2000-2020' - roughly 27 calendar years of combined coverage. The two statements about backtest depth are not reconciled."
  - "The paper never states the direction of the trades it takes - no long-only or long-and-short statement appears in Sections 3 to 5 - while the secondary source reached through the paper's own printed testing link states that 'retail script is embded in system, but currently disabled due to SECP regulation against shorting the market', implying a short side that the paper does not describe. Direction handling is unreconciled."
  - "The author's affiliation is printed two ways: the PDF title block and closing block read 'Analyst, Developer & Author' with 'Singapore /Seoul/ Karachi' (and 'Seoul/ Singapore / Karachi' at the end), while both SSRN author lines read 'Independent'. No ORCID and no email address is printed on either surface, and SSRN's contact control was deliberately not expanded."
  - "The abstract reports 'maximum drawdown of 2.91% in local currency terms' (positive sign) while the Section 5.1 headline table prints 'Maximum drawdown | -2.91%'; the sign convention differs between abstract and table, unreconciled."
---

# KSE Sentinel: Rule-Based Trend-Continuation on a 30-Symbol Pakistan Stock Exchange Universe with a Deflated-Sharpe Multiple-Testing Floor, an Independent ~2000-2020 Archive Claim, and a 60-Day Live Forward-Paper Program (SSRN 7093159, companion 7102818)

## Provenance

- **Primary source.** SSRN preprint, `abstract_id=7093159`, DOI [`10.2139/ssrn.7093159`](https://doi.org/10.2139/ssrn.7093159). Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7093159>.
- **Companion posting of the same work (also pinned, see below).** SSRN `abstract_id=7102818`, DOI [`10.2139/ssrn.7102818`](https://doi.org/10.2139/ssrn.7102818). Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7102818>.
- **Exact title.** PDF title block (p.1): `KSE Sentinel: A Rule-Based Trend-Continuation Strategy for the Pakistan Stock Exchange (PSX)`, with subtitle `Design, Statistical Validation, and Live Forward Testing`, followed by `Working Paper`. Both SSRN landing titles carry the identical main title.
- **Author (recorded exactly as each surface prints it; the surfaces disagree on affiliation).** PDF title block (p.1): `Ertiza Abbas`, `Analyst, Developer & Author`, `Singapore /Seoul/ Karachi`, `July 2026`. PDF closing block (p.14): `Ertiza Abbas`, `Analyst, Developer, Author, Seoul/ Singapore / Karachi`, `July 2026`. Both SSRN author lines: **Ertiza Abbas**, `Independent`. PDF metadata `/Author` reads `abbas ertiza`. Single author, no co-authors printed; no ORCID; no email printed on either surface.
- **Dates (printed six-plus ways; not reconciled).** PDF cover (p.1): `July 2026`. Landing: `Date Written: July 07, 2026`; `Posted: 28 Jul 2026` (7093159). Suggested citation: `(July 07, 2026)`. PDF metadata `/CreationDate D:20260710185728+08'00'` (2026-07-10 18:57:28 +08'00'). Companion posting: `Posted: 29 Jul 2026`, `/CreationDate D:20260712092232+08'00'` (2026-07-12 09:22:32 +08'00'). Two further in-text time anchors: the canonical backtest run id `backtest_20260707_063609` (Section 5) and the live program `initiated July 6, 2026` (Section 7.1). Both PDFs were produced by `Microsoft Word for Microsoft 365` (the PDF `/Creator` and `/Producer` fields print the vendor string with a registered-trademark glyph; it is rendered here without that glyph so this record stays ASCII-only).
- **Publication / review status.** SSRN working paper (the PDF cover prints `Working Paper`). Both landings carry no journal, no issue and no peer-review statement, and the PDFs print no peer-review banner, so peer-review status is `not stated in source`. Landing headings read `0 References` / `0 Citations` (see contradictions). Paper statistics at read time: 7093159 `DOWNLOADS 52` rising to `53`, `ABSTRACT VIEWS 143`; 7102818 `DOWNLOADS 74`, `ABSTRACT VIEWS 161`.
- **Licence (restrictive).** Both landings state `The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.` Because redistribution is restricted, this record normalises only short printed values, table cells and section references and reproduces no extended passages.
- **Landings read in a browser session on 2026-09-29** after the Cloudflare interstitial cleared (one read each): page counts, post dates, `Date Written`, `There are 2 versions of this paper` (the control cross-links 7093159 and 7102818), the full abstract, the Keywords block, the licence line, the paper statistics, and the `Open PDF in Browser` delivery links.
- **Pinned PDFs (primary and companion), retrieved 2026-09-29** through each landing's `Open PDF in Browser` delivery link - stable non-expiring delivery links with **no presigned or session-bound URL stored anywhere in this record**:
  - **Primary (7093159):** `https://papers.ssrn.com/sol3/Delivery.cfm/7093159.pdf?abstractid=7093159&mirid=1` - **287,604 bytes, 14 pages, SHA-256 `cc9e7d63b36fc8521ff4281c6dcafb4dabe9bfd569d20bf0527d3d9a8644d719`**, `%PDF-1.7`; text extracted with `pypdf 6.16.2` to **24,783 characters**, all 14 pages read, including Sections 1-10, Sections 2.1-2.4, Sections 3.1-3.4, Sections 4.1-4.4, Sections 5.1-5.5, Sections 6.1-6.4, Sections 7.1-7.3, the six-entry reference list read entry by entry, and the printed testing link on p.2.
  - **Companion (7102818):** `https://papers.ssrn.com/sol3/Delivery.cfm/7102818.pdf?abstractid=7102818&mirid=1` - **296,570 bytes, 13 pages, SHA-256 `c4ff62868c11e0559545bc31daf658e7380e398747c9486320628f406a52ebbb`**, `%PDF-1.7`; `pypdf 6.16.2` extraction to **24,904 characters**; compared against the primary with a normalised sentence-level diff (only hyphenation / line-wrap / spacing differences plus the `yFinance` and `(Yahoo Finance)` wording changes noted above; **no numeric or claim difference found**).
- **Tables are raster images, not text (method note).** In the pinned primary PDF the Section 5.1 headline table (page 8, XObject `/Image53`, 790 x 567, `/FlateDecode`, `/DeviceRGB`, 8 bpc) and the Section 5.5 sizing table (page 9, XObject `/Image56`, 757 x 310, same encoding) carry no text layer, so ordinary text extraction returns blank space under those headings. Both image streams were pulled from the pinned PDF's page resource dictionaries, re-encoded losslessly to PNG and transcribed by direct visual reading on 2026-09-29. Pages 1-7 and 10-14 contain no images. Every headline figure below tagged `(Table 5.1)` or `(Table 5.5)` comes from that transcription and is cross-checked against the abstract and conclusion text where the same figure also appears in the text layer.
- **Secondary source printed inside the PDF.** Page 2 prints `For Strategy and API link for testing click here https://shorturl.at/n9GTR`. That link shortener resolves on redirect to the public LinkedIn post <https://www.linkedin.com/posts/abbas-ertiza_algorithmictrading-quantfinance-psx-share-7479859295233167361-nr_u/>, titled `PSX Algorithmic Trading System Launched`, read 2026-09-29 without login: the post body and its hashtags are visible, while reactions and comments are login-walled. The post's displayed timestamp is a relative `2 months` with an `edited` marker (research-computed heuristic decode of LinkedIn activity id `7479859295233167361` via `(id >> 22) + 1104537600000` gives 2026-07-06 UTC, consistent with the paper's stated live-program start - **this decode is research-computed, not source-reported**). The shortener is not a stable identifier, and its destination is a social-media announcement rather than a code, data or replication artefact.
- **Deterministic pre-write source-identity dedup** (hidden-inclusive `rg -uuu` over the whole checkout, including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` at 1,088,787 bytes): `7093159`, `10.2139/ssrn.7093159`, `7102818`, `10.2139/ssrn.7102818`, `KSE Sentinel`, `Ertiza`, `abbas-ertiza`, `linkedin.com/posts/abbas`, `Pakistan Stock Exchange`, `backtest_20260707_063609`, `run_fresh_dsr_analysis`, `shorturl.at/n9GTR`, `Rule-Based Trend-Continuation`, `Trend-Continuation Strategy for the Pakistan`, `KSE100`, `kse100`, `frontier markets` - **all zero hits outside this file**. Generic-adjacent tokens were scanned and reported honestly: `Deflated Sharpe Ratio` hits 75 files, `walk-forward validation` 126 files, `y[Ff]inance` 93 files, `forward-paper` 4 files, `trend-continuation` 5 files (all unrelated phrasings), `Pakistan` hits exactly 2 files, both of them recording Pakistani **author affiliations** (Lahore / LUMS) on non-Pakistani markets, and `PSX` hits exactly 1 file as a substring coincidence inside unrelated fund-ticker text. Positive control `novy-marx` returned **14 files** in the same session. `coverage_manifest.csv` (last written 2026-08-31, therefore stale) returns 0 for every new token. `git log --oneline -20` was used as a convenience glance only and does not satisfy dedup.
- **Four-axis distinction against adjacent repository records** (source identity and mechanism differ in every pair; no existing record in this repository has the Pakistan Stock Exchange as its primary universe):
  - `long-only-us-equity-ath-trend-following-vol-sizing-atr-ratchet-turnover-control-ssrn-5084316-2026-09-27.md` (SSRN `5084316`): different source; that rule enters **at new all-time highs above its own moving average** on liquid US large caps with ATR-ratchet exits and an explicit turnover control, whereas this rule is a **short-EMA two-candle continuation entry with regime-conditional exit strictness** on a 30-name frontier-equity universe. Different market type (US large-cap equity vs Pakistan frontier equity), different signal construction (ATH-level breakout vs candle-close relative to a short EMA), different material data dependency (survivorship-controlled CRSP-style panel vs yFinance daily bars on a version-controlled in-house 30-symbol list).
  - `us-equity-long-only-trend-above-own-sma-cash-retreat-nvidia-concentration-attribution-ssrn-7073258-*.md` (SSRN `7073258`): different source; there the mechanism is a **cash-retreat throttle on a volatility-conditioned momentum-concentration book** whose return component is attributed to a single name; here there is no cash sleeve and no concentration attribution, and the paper reports no single-name attribution for the canonical 3% book (the one name it does isolate, NPL at +74.64%, belongs to the 5% variant and is explicitly flagged as unrepresentative).
  - `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` and `tradingview-close-only-donchian-50-trend-following-2026-09-18.md`: both are **Donchian channel breakout** entry families; this source never references Donchian or channel breakouts, and its entry is a candle-close/short-EMA condition. Different source, different signal construction, different universe (crypto perpetuals vs PSX equities).
  - `futures-trend-following-autocorrelation-drift-decomposition-2026-09-02.md`: different source, different mechanism (return autocorrelation / drift decomposition used as the explanatory object), different market (exchange-traded futures), and it is a study of where trend returns come from rather than an implemented rule.
  - `retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-*.md`: different source; that record stacks oscillator, volume and calendar gates as a retail signal family under falsification, while this source deliberately stacks **no** indicator beyond a short EMA and a regime label, and claims its rule was specified from discretion before being tested rather than mined.
  - `opening-range-breakout-pre-registered-225-cell-futures-cost-falsification-*.md`: different source, different mechanism (opening-range breakout), different market (futures), different evidentiary posture (a 225-cell pre-registered cost falsification vs a single canonical backtest run id).

## Economic mechanism

### Source-reported

The paper is explicit that it does **not** claim a new return-predictability mechanism. Section 1 states that the underlying phenomenon - trend continuation / time-series momentum - is `well documented across asset classes and decades` and that the contribution is `applied and methodological` instead. The source's stated rationale, in its own framing:

1. **Mechanism family.** Trend continuation in the spirit of Jegadeesh and Titman (1993) for cross-sectional momentum and Moskowitz, Ooi and Pedersen (2012) for time-series momentum, which the paper cites as showing that past 12-month returns positively predict future returns across 58 futures instruments and that the effect persists about a year before partially reversing. Hurst, Ooi and Pedersen (2017) is cited for persistence across roughly a century, 67 markets and four asset classes, with annualised gross returns of 18.0 percent, about half the volatility of equities, and net returns positive in every decade.
2. **Payoff signature.** The paper expects - and reports - positive skew: `a small number of very large winning trades contributing disproportionately to total profit`, framed as the textbook signature of trend following (many small losses, few large gains), consistent with behavioural anchoring / herding and with non-profit-seeking participants.
3. **Claimed methodological novelty - construction order.** The stated differentiator is that the entry/exit logic was derived `first from an experienced discretionary trader's codified judgment, and only then tested against historical data`, so `the rules were not searched for; they were specified and then evaluated`. The paper concedes this `does not make the strategy immune to overfitting risk` but argues it is a more defensible starting point than a data-mined rule.
4. **Claimed methodological novelty - multiple-testing honesty.** The Deflated Sharpe Ratio (Bailey and Lopez de Prado 2014) is used to correct for the number of prior strategy trials and for non-normality, with the trial count disclosed as `an honest floor, not an exhaustive count`.
5. **Claimed methodological novelty - a live forward test.** Section 7 presents an ongoing 60-day live forward-paper program as a genuine differentiator from backward-only evidence, and discloses two operational incidents caught during live operation.
6. **Claimed methodological novelty - currency honesty.** The paper reports local-currency and USD-converted returns side by side because the divergence is `a real, first-order finding for any foreign institutional allocator`.
7. **Regulatory framing.** SECP's 2025 Concept Paper on regulating algorithmic trading in Pakistan is cited as the environment the operational controls are built toward (registration, audit trails, senior oversight, kill-switch capability, phased institutional-first access).

### Research interpretation

Component roles normalised so each can be ablated later. Everything marked `[withheld]` is explicitly withheld by the source (Section 4: `exact calibrated parameters, precise entry/exit trigger logic, and full source code are withheld here`); everything marked `[research-proposed]` carries the label `research-proposed` because it is not specified by the source at all.

```text
Regime:            a separately-identified "prevailing trend regime" (a "master
                   trend regime") that must be identified before an entry is
                   allowed; identification rule, lookback and timeframe
                   [withheld]
Primary signal:    two consecutive same-direction candle closes on the
                   trend-correct side of a short-period exponential moving
                   average; EMA period, candle timeframe and the definition of
                   "trend-correct side" [withheld]
Confirmation:      none stated beyond the two-candle condition
Exit:              exit strictness is conditional on whether the master trend
                   regime has flipped since entry - winners and losers are
                   managed differently depending on whether the trend context
                   that justified the entry is still intact; the actual
                   take-profit / stop / time-exit values [withheld]
Position sizing:   tiered risk-based framework, conservative / moderate /
                   balanced / growth tiers, roughly 1-5% risk per trade,
                   applied against a fractional-share-aware per-symbol lot
                   resolver reflecting the April 2024 PSX one-share lot reform;
                   canonical reported tier 3%, comparison tier 5%, and the DSR
                   trial set is 1% / 3% / 4% / 5% (the 1% and 4% cells are
                   never printed)
Portfolio risk:    correlation-based position gating - new entries blocked when
                   the candidate would have rho >= 0.70 with an already-open
                   position, computed from live synced price data; plus
                   sector / symbol concentration limits at tenant config level
Direction:         not stated anywhere in the paper [data gap]; the secondary
                   source says the retail script is disabled for shorting under
                   SECP regulation
Data / cadence:    daily OHLCV from yFinance, PSX trading sessions, rebalance
                   implied per scan; no intraday component is described
Benchmark:         claimed as an equal-weight buy-and-hold over the same window
                   and universe, but no benchmark number is printed [data gap]
```

Interpretation in falsifiable form: the hypothesis is that on a frontier-equity daily panel, short-horizon price continuation conditioned on a slower trend state produces a positively skewed trade-level distribution whose mean win is roughly four times its mean loss, such that a sub-40 percent hit rate still yields a profit factor materially above 1 after a fixed 22.5 bp cost assumption. That is a **risk-management-plus-trend hypothesis**, not a forecast of direction; the paper itself says the alpha claim rests on payoff shape (cut losses, let winners run) rather than on hit rate. The economic channel the source offers for why trends persist at all is behavioural (anchoring, herding) plus non-profit-seeking flow - it presents no microstructural or informational channel, and it does not test any.

## Signal

- **Signal formation timestamp / tradability.** Formed on completed daily candles for PSX-listed symbols. The paper does not state the session timezone, the candle boundary convention, or whether a signal formed on day T is traded at day T close or day T+1 open. `data gap` / `underspecified`.
- **Lookback.** A `short-period exponential moving average` and a `separately-identified prevailing trend regime`. Neither period, nor the regime's lookback, nor whether endpoints are inclusive, nor any warm-up rule is printed. `underspecified` (deliberately withheld under Section 4).
- **Long entry.** `two consecutive same-direction candles closing on the trend-correct side of a short-period exponential moving average`, conditioned on the prevailing trend regime - as stated in the abstract and restated in Section 4.1 as a `trend-continuation signal derived from short-horizon candle-close direction relative to a short-period exponential moving average, conditioned on a separately-identified prevailing trend regime`. Exact price reference for the fill, order timing and tie handling: `not stated in source`.
- **Short entry.** The paper does not state whether it shorts at all. The secondary source reached through the paper's own printed link says the retail script is `currently disabled due to SECP regulation against shorting the market`, which implies a short capability exists in the system but is switched off for retail. `data gap`, unreconciled (see contradictions).
- **Exit.** `Exit logic strictness is conditional on whether the master trend regime has flipped since entry - winners and losers are managed differently depending on whether the broader trend context that justified the entry remains intact.` Actual stop, target, trailing and timeout values: `underspecified` (withheld).
- **Holding period.** `not stated in source`. Trade count alone implies roughly 0.8 trades per PSX trading day across the 30-symbol book over the 2021-2026 window (research-computed: 1,009 trades / ~1,260 trading days), but no holding-period distribution, no maximum hold and no overlap rule is printed.
- **Re-entry rules.** `not stated in source`.
- **Parameters.** Sizing tiers (1 / 3 / 4 / 5 percent risk per trade used as the DSR trial set; canonical 3 percent; comparison 5 percent), correlation gate `rho >= 0.70`, lot-size resolver reflecting the April 2024 one-share lot reform, tenant-level sector and symbol concentration limits. Entry and exit parameters: `underspecified`.
- **Position sizing logic.** Risk-per-trade percentage applied against a fractional-share-aware, per-symbol lot-size resolver. The paper documents that the sizing tier is **not** a free multiplier: the 5% variant produced 602 trades against 1,009 at 3% because larger positions interact with portfolio-level risk controls and block entries (Section 5.5).
- **Multi-timeframe dependencies.** A master trend regime governing exit strictness, plus the candle-level entry condition. The timeframe of the master regime is `not stated in source`.
- **Fully specified or underspecified?** **Underspecified, by design.** Section 4 states that exact calibrated parameters, precise entry/exit trigger logic and full source code `are withheld here`, and that the section describes the `mechanism class and validation discipline` rather than `a replication recipe`. The strategy therefore **cannot be independently reconstructed from the source**, and no parameter in this record may be treated as source-reported beyond those explicitly printed above.

## Required data

- **Instrument.** Common shares listed on the Pakistan Stock Exchange, traded in PKR, one-share lot standard since the April 2024 reform. No derivatives, no short instrument identified.
- **Universe.** 30 symbols `spanning PSX's major sectors (commercial banks, oil & gas exploration/marketing, fertilizer, power generation, cement)`, defined and version-controlled in the author's codebase file `bulk_sync_universe.py` (the file itself is not published in the source). The full ticker list is **not printed** - `data gap`. Known membership events the source discloses: `ENGRO` formally delisted effective 2025-01-14 after a Scheme of Arrangement into Dawood Hercules, renamed `ENGROH`, which `is not currently available through the strategy's primary data vendor (Yahoo Finance) under any ticker suffix attempted` (disclosed as a `known, understood, immaterial-scale data gap`); and the KSE-100 removal of `UNITY` as of 2026-04-01 cited as an example of routine index-composition churn that universe management must handle.
- **Venue.** Pakistan Stock Exchange, single venue.
- **Timeframe.** Daily bars.
- **Fields.** OHLCV only. No funding, no mark/index/basis, no trades or aggressor side, no order book, no open interest, no options surface, no on-chain, no sentiment field is used or described.
- **Point-in-time.** Primary window 2021-2026 pulled from `yFinance daily OHLCV data`. Independent out-of-sample window `~2000-2020` from `a separate PSX historical archive` - the archive's identity, provider, version and point-in-time rules are `not stated in source` (`data gap`), so survivorship and restatement bias cannot be quantified. The source does not describe any delisting or renaming adjustment beyond the ENGRO note.
- **Timestamp / timezone.** `not stated in source`. No clock, precision, alignment or out-of-order handling rule is printed.
- **Missing data.** Only the ENGRO/ENGROH vendor gap is disclosed. No null, stale, suspended, partial-bar or bad-print policy is stated - `underspecified`. Imputation policy: `not stated in source`.
- **Currency.** PKR-denominated returns are primary; USD-converted returns are also reported. The FX rate source, conversion convention (daily vs period-average vs period-end) and timing are `not stated in source` (`data gap`), which matters because the USD and PKR CAGRs differ by 10.43 percentage points (research-computed from Table 5.1: 7.47% vs -2.96%).
- **Cost inputs.** A single assumed figure of 22.5 basis points combining commission, slippage and spread; see Execution assumptions. No per-name, per-size or regime-dependent cost field is used.

## Execution assumptions

- **Source-reported cost.** `All reported returns are net of an assumed 22.5 basis points in round-trip trading costs per leg (commission, slippage, and spread combined)` (Section 3.4). The abstract phrases the same number as `22.5 basis points per leg` and omits `assumed`. The one-way-versus-round-trip reading is a factor-of-two ambiguity and is recorded as a contradiction; this record does **not** resolve it in either direction.
- **Cost is assumed, not measured.** A whole-document term scan of both pinned PDFs (identical counts in each) gives: `slippage` 2, `spread` 2, `commission` 5, `cost` 4, `costs` 3, `capacity` 5, and **zero occurrences** of `market impact`, `impact`, `participation`, `latency`, `limit order`, `market order`, `fill`, `execution`, `maker`, `taker`, `order book`, `turnover`, `bid`, `ask`, `fee`, `fees`, `leverage`, `margin`, `borrow`, `liquidation`, `funding`, `shorting` and `advance`. Both `slippage` hits and both `spread` hits sit inside the two 22.5 bp sentences (abstract and Section 3.4); of the five `commission` hits, two are inside those same sentences and three are the string `Securities and Exchange Commission of Pakistan`, each inside one of the three printed copies of that reference entry (the `Suggested full citations` block printed on page 4 and again on page 5, plus the page 14 `References` list). The four `cost` hits are the abstract, the Section 3.4 heading, the Section 3.4 body, and the Section 5.5 phrase `the identical universe, signal logic, and cost assumptions`. The token `short` appears exactly 5 times - twice in `short-period` (abstract and Section 4.1), once in `short-horizon` (Section 4.1), once inside the printed `https://shorturl.at/n9GTR` link, and once inside a quotation from the cited trend-following literature (`position themselves short after the initial market decline`) - so the paper never states its own trade direction. No commission schedule, no observed spread series, no slippage measurement, no market-impact model, no participation cap and no cost-sensitivity ladder exist anywhere in either PDF. Every cost field other than that one assumed number is a `data gap`, **never zero**.
- **Order type, fill model, signal-to-order delay, same-bar vs next-bar execution.** `not stated in source`.
- **Latency / partial fills / failures.** `not stated in source`.
- **Leverage / margin.** `not stated in source`. The paper describes equity share positions sized through a per-symbol lot resolver and never mentions margin, leverage or financing; leverage therefore stays a `data gap` and must not be inferred as 1x either.
- **Borrow / shorting.** `not stated in source` in the paper; the secondary source states retail shorting is disabled under SECP regulation (unreconciled).
- **Capacity (source-reported, methodology not shown).** `an estimated ~PKR 500M hard capacity ceiling, with a practical operating range closer to ~PKR 100M at the recommended 4% sizing tier` (Section 8). How the ceiling was derived - ADV, participation, impact model - is `not stated in source` (`data gap`).
- **Funding / borrow cost.** The instrument described is equity shares on the PSX, so no perpetual-style funding term applies; securities-lending or short-borrow cost is `not stated in source` (and the existence of a short side is itself unreconciled).
- **Independent stance.** Everything in this section other than the 22.5 bp number, the capacity figures and the sizing tiers is a source omission, not a Scout assumption. No fill, latency, impact or leverage assumption has been supplied by this record.

## Evidence

### Source-reported

Every figure below is third-party, source-reported, and has not been reproduced by us. Provenance is given per figure.

**Table 5.1 `Headline Statistics` (p.8 of the pinned primary PDF; transcribed from the page's embedded raster table because the table has no text layer):**

| Metric | Value (as printed) |
| --- | --- |
| Total trades | 1,009 |
| Universe | ~30 symbols |
| Sample window | ~5 years (2021-2026) |
| Win rate | 39.15% |
| Profit factor | 2.51 |
| CAGR (PKR) | 7.47% |
| CAGR (USD-converted) | -2.96% |
| Sharpe ratio | 2.08 |
| Maximum drawdown | -2.91% |
| Monte Carlo significance (sign-permutation) | p = 0.0 |

**Table 5.5 sizing comparison (p.9 of the pinned primary PDF; same raster-table method):**

| Metric | 3% Risk (canonical) | 5% Risk |
| --- | --- | --- |
| Total trades | 1,009 | 602 |
| Win rate | 39.15% | 39.37% |
| Sharpe ratio | 2.08 | 2.09 |
| CAGR (PKR) | 7.47% | 5.53% |
| Maximum drawdown | -2.91% | -2.68% |

**Abstract (p.1 of both pinned PDFs, identical to both landing abstracts):** 1,009 trades; ~five-year window 2021-2026; net of commission, slippage and spread totalling 22.5 basis points per leg; 39.15% win rate; profit factor 2.51; annualised Sharpe ratio 2.08; maximum drawdown 2.91% in local currency terms; positively skewed returns with average win size approximately 3.9 times average loss size; multiple-testing handled with the Deflated Sharpe Ratio of Bailey and Lopez de Prado (2014) with the trial count disclosed as a floor; out-of-sample validation against an independent ~2000-2020 PSX historical archive; an ongoing 60-day live forward-paper validation program initiated July 2026 including real operational incidents; PKR returns positive while USD-converted returns are negative over the sample.

**Section 5.2:** `A sub-40% win rate alongside a strongly positive profit factor` is presented as the textbook trend-following signature; `Average-win-to-average-loss ratio is approximately 3.9x`.

**Section 5.5 prose:** the 5% variant produced `substantially fewer trades (602 vs. 1,009)` than the 3% variant despite identical entry/exit signal logic, `and, counterintuitively, a lower CAGR despite larger position sizing`, with win rate and Sharpe `essentially unchanged`; the stated explanation is that larger positions interact with portfolio-level risk controls and block entries. Best single symbol in the 5% run: `NPL, returning 74.64% over the sample window on an isolated, independently-capitalized basis`, explicitly `not representative of portfolio-level performance, which is properly reported as the 5.53% CAGR figure`.

**Section 6.1:** `Sign-permutation methodology yields p = 0.0`, with the source's own caveat that this tests whether the observed win/loss sequence could arise from a random reordering `not whether the strategy's rules themselves were free from data-snooping in their original construction`. The permutation count is `not stated in source`.

**Section 6.2:** walk-forward validation of the adaptive sizing methodology shows out-of-sample Sharpe `held in both folds tested`, with the source's own caveat `Two folds is suggestive, not definitive proof of robustness`.

**Section 6.3:** DSR trial count `N=4 (the 1%/3%/4%/5% sizing candidates)`, `a documented floor, not an exhaustive count`; explicitly excluded prior experiments are `a 5.5% sizing variant, an earlier stricter entry rule, an RSI-oversold gate, two "trap-immune" signal variants`. **The resulting DSR figure is printed as the unfilled placeholder `[to be confirmed from run_fresh_dsr_analysis.py output]`.**

**Section 6.4:** testing against the separate ~2000-2020 PSX historical archive is described as `a genuinely distinct data source` and `a stronger form of out-of-sample evidence than a simple time-split on a single data source`. **No number, metric, sample size or result of that test is printed anywhere in the source** - `data gap`.

**Section 7:** 60-day live forward-paper validation program, `initiated July 6, 2026`, running `once per trading day`; every scan decision (executed, blocked, ignored, held, closed) persisted to a dedicated live signal tracking table with entry-to-outcome linkage. Reported operational incidents: (a) a tenant risk configuration row missing for the first two days, causing conservative fallback sizing instead of the intended tier, caught and corrected with the discontinuity documented; (b) a timestamp-precision ID collision between two same-microsecond events caught live on Day 3, contained by existing error handling and fixed at root cause the same day. Section 7.3 states a 60-day window `is not by itself sufficient to draw strong statistical conclusions` and that its value is as an infrastructure test `not as a standalone performance claim`. **No forward performance figure is printed** - `data gap`.

**Section 8:** capacity `~PKR 500M hard capacity ceiling`, `practical operating range closer to ~PKR 100M at the recommended 4% sizing tier`; operational controls listed as rate limiting, CORS hardening, collision-safe identifier generation, authentication/RBAC and a planned kill-switch aligned with SECP direction.

**Section 9 (source's own limitations):** currency risk (PKR positive, USD negative); data gaps (ENGRO/ENGROH and vendor coverage); sample size and multiple testing with N=4 as an honest floor; frontier-market liquidity and capacity; a regulatory environment still at Concept Paper stage; a deterministic rule set that is `not infallible`.

**Section 10:** restates `39.15% win rate, profit factor of 2.51, and Sharpe ratio of 2.08`.

**Secondary source (LinkedIn post reached through the paper's own printed testing link):** announces the launch of the forward-testing phase for `a proprietary, end-to-end intelligent decision support and automated trading system specifically engineered for the Pakistan Stock Exchange (PSX - KSE100)`; describes three pillars (Scanning, Selection, Execution) with `zero manual intervention`; states the system `was subjected to extensive backtesting against 20 years of historical PSX data, yielding highly promising and robust results` (no figure given); states `white paper is available, the system is built for institutes, Brokers, and Banks. although retail script is embded in system, but currently disabled due to SECP regulation against shorting the market.` Post shows 3 reactions at read time. Treat as a promotional claim, not evidence.

### Independently reproduced

`Not independently reproduced.`

We performed provenance verification and one internal arithmetic consistency check only, both of which are ours and neither of which reproduces any empirical result:

- **Arithmetic identity check (research-computed).** From the printed win rate 39.15% and printed profit factor 2.51, the implied average-win / average-loss ratio is `2.51 x (1 - 0.3915) / 0.3915 = 3.9012`, which matches the paper's printed `approximately 3.9x`. The printed PKR CAGR 7.47% against printed max drawdown 2.91% implies a Calmar ratio of 2.567 (not printed by the source; research-computed for scale only). 1,009 trades over roughly 1,260 PSX trading days implies about 0.80 trades per day across the 30-symbol book (research-computed). None of these checks validates the underlying trades, the data, the cost assumption or the Sharpe ratio.
- **Provenance checks (research-computed).** Both pinned PDFs hashed and page-count verified; both landing metadata blocks read directly; the two postings compared by normalised sentence-level diff as described under Provenance; the Section 5.1 and 5.5 tables recovered from the pages' embedded raster images and transcribed.

No backtest was re-run, no PSX data was downloaded, no trade sequence was reconstructed, and the withheld parameters prevent reconstruction in any case.

### Negative evidence

1. **The headline multiple-testing correction does not exist in the source.** The paper is organised around the Deflated Sharpe Ratio, yet Section 6.3 prints only the placeholder `[to be confirmed from run_fresh_dsr_analysis.py output]`. The number a reader would need to judge whether the Sharpe survives selection is absent.
2. **The trial count is openly a floor.** N = 4 covers only the sizing candidates, and the source names at least five further abandoned experiments (5.5% sizing variant, stricter entry rule, RSI-oversold gate, two `trap-immune` variants) plus the disclosed possibility of unlisted iteration. A DSR computed at N = 4 is an upper bound on the correction, not the correction.
3. **The USD result is negative.** Table 5.1 prints CAGR (USD-converted) of **-2.96%** against PKR 7.47% - a 10.43 pp divergence (research-computed). For any allocator not already long PKR, the strategy lost money in hard currency over its own sample window. The source itself calls this `a real, first-order finding`.
4. **The claimed benchmark comparison is missing.** Section 5.4 says an equal-weight buy-and-hold comparison `is reported`, but no benchmark number exists in the pinned PDF. Whether the strategy beats passive exposure over the same 30 names is therefore untested in the document - the single most basic alpha check is absent.
5. **The claimed independent-archive validation has no result.** Section 6.4 asserts a genuinely distinct ~2000-2020 out-of-sample test but prints nothing about it - no Sharpe, no CAGR, no sample size. `data gap`, and it is one of the paper's three headline validation claims.
6. **The claimed live forward results have no result.** The abstract promises forward-test results from the 60-day program; Section 7 delivers program design and two bug reports only. `data gap`.
7. **The forward window is admittedly underpowered**, in the source's own words: `A 60-day window, even fully clean, is not by itself sufficient to draw strong statistical conclusions.`
8. **The sign-permutation p-value is a floor and answers a narrower question than it appears to.** `p = 0.0` is a printed zero rather than a stated permutation count, and the source states outright that it does not test whether the rules were free of data-snooping.
9. **Only two walk-forward folds**, self-described as `suggestive, not definitive proof of robustness`.
10. **The rule set is deliberately withheld**, so the strategy cannot be reconstructed, audited for look-ahead, or replicated from the source. This is the source's own stated design choice, and it is the single largest obstacle to treating any number above as evidence.
11. **Sizing is non-monotone.** Raising risk per trade from 3% to 5% cut the trade count by 40.3% (research-computed from 1,009 to 602) and lowered CAGR by 1.94 pp (7.47% to 5.53%), because portfolio-level controls block entries. The reported edge is therefore a joint product of the signal and a risk engine, and the paper's own ablation shows the risk engine is not a free multiplier.
12. **Two of the four DSR sizing candidates (1% and 4%) are never reported**, so the visible performance surface is a subset of the searched surface.
13. **Single venue, single country, single frontier market, 30 symbols, one vendor.** All results are PKR cash equities on the PSX from yFinance daily bars; the ticker list, the universe file and the vendor's corporate-action handling are not published.
14. **Universe handling has a known hole and visible churn.** ENGRO/ENGROH is a disclosed vendor coverage gap; UNITY's 2026-04-01 KSE-100 removal shows membership changes mid-sample. Point-in-time universe construction rules are unstated, so survivorship bias cannot be bounded.
15. **Capacity is sub-scale by the source's own numbers** - roughly PKR 100M practical against a PKR 500M hard ceiling at the recommended 4% sizing tier, with no derivation shown and no USD equivalent computed here because the source supplies no FX rate and this record will not import an outside one.
16. **Regulatory constraint on the short side.** SECP's algorithmic-trading framework is still only a Concept Paper, and the secondary source states retail shorting is currently disabled - so the tradable configuration may differ materially from the tested one, and the paper never says which side it trades.
17. **No code, no data, no run artefact.** The canonical backtest is identified only by an internal run id (`backtest_20260707_063609`) that cannot be resolved from the source; the printed `Strategy and API link for testing` is a link shortener resolving to a social-media post rather than a replication package; the referenced `bulk_sync_universe.py`, `run_fresh_dsr_analysis.py` and independent archive are not published.
18. **The mechanism claim is explicitly not novel.** The source states outright that it proposes no new return-predictability mechanism and that trend continuation is well documented; the entire evidentiary weight rests on one five-year in-house backtest of a withheld rule.
19. **Source quality.** Single-author, non-peer-reviewed SSRN working paper with zero citations, low download and view counts, an unfilled placeholder in its central statistical section, duplicated citation blocks, a broken section label, an abstract missing its subject, and the same paper posted twice under two IDs on consecutive days - all documented as contradictions above.
20. **Licence restricts reuse** (`All rights reserved. No reuse allowed without permission.`), limiting independent redistribution of the artefact even if parameters were released.
21. **No cost sensitivity anywhere.** A single assumed 22.5 bp figure carries the entire net-of-cost claim, and the source prints no trade frequency per symbol, no holding period and no turnover, so the annual drag of any other cost assumption cannot be computed from the document at all - which is exactly why the cost-ladder gate F7 below exists.
22. **No placebo, no shuffled-label test, no competing-explanation control** (e.g., against a passive index or a simple buy-and-hold of the same names) is reported.

## Falsification plan

All thresholds, sample sizes, ladders and acceptance cutoffs below are labelled `research-proposed` when they are operationalizations (ladders, caps, windows) and `research-defined falsification threshold` when they are acceptance cutoffs. None of them is specified by the source; the source publishes no falsification plan of its own.

- **F1 - Rule-release gate (reconstructability).** Require the exact EMA period, the master-regime definition, the entry and exit trigger values, the fill convention and the `backtest_20260707_063609` artefact to be published. **Fail** if parameters remain withheld. **Action:** treat the strategy as non-reconstructable, keep `research-only`, never promote to implementation.
- **F2 - Printed-value reproduction gate.** On an independently assembled 2021-2026 daily PSX panel for the 30-symbol universe, require reproduction of 1,009 trades (within +/- 5%), win rate 39.15% (+/- 0.50 pp), profit factor 2.51 (+/- 0.10), PKR CAGR 7.47% (+/- 1.00 pp) and max drawdown 2.91% (+/- 0.50 pp) under the source's own 22.5 bp assumption. **Fail** on any miss. **Action:** record a failed replication as primary negative evidence.
- **F3 - DSR completion gate.** Require the paper's own Section 6.3 placeholder to be filled at N = 4 and to exceed 1.00. **Fail** if the figure stays unfilled or is below 1.00. **Action:** the multiple-testing claim is then unsupported and the record's status stays `research-only`.
- **F4 - True-trial-count gate.** Enumerate every prior strategy variant (source-disclosed minimum: N = 4 sizing candidates plus the 5.5% variant, stricter entry rule, RSI-oversold gate and two `trap-immune` variants = at least 9) and recompute DSR at that N. **Fail** if DSR < 1.00 at the true N. **Action:** classify the reported Sharpe as consistent with selection noise.
- **F5 - Currency gate.** Recompute returns with a documented PKR/USD series (source and convention to be fixed in advance). **Fail** if USD CAGR <= 0. **Action:** the strategy is a PKR-currency story rather than an alpha story and must not be proposed to a USD allocator. *Pre-declared expectation: as printed (-2.96%) this gate already fails.*
- **F6 - Passive-benchmark gate.** Equal-weight buy-and-hold of the same 30 symbols over the same window under the same 22.5 bp assumption. **Fail** if the strategy does not beat it on both CAGR and Sharpe. **Action:** no demonstrated alpha beyond passive exposure.
- **F7 - Cost-ladder gate (research-proposed ladder centred on the source's single assumption).** Round-trip cost at 0 / 11.25 / 22.5 / 45 / 90 bp. **Fail** if PKR CAGR turns non-positive at 45 bp, or if max drawdown exceeds 2x the printed 2.91% at 45 bp. **Action:** the result is a cost assumption, not an edge.
- **F8 - Walk-forward gate.** At least 10 contiguous folds (research-defined), OOS Sharpe > 0 in at least 7 folds, pooled OOS Sharpe >= 1.00. **Fail** on any condition unmet (the source currently has 2 folds). **Action:** robustness claim downgraded to unproven.
- **F9 - Independent-archive gate.** Require the ~2000-2020 archive result to be printed with sample size, Sharpe and CAGR, and to show OOS Sharpe >= 1.00 on data disjoint from development. **Fail** if no number is published or if OOS Sharpe < 1.00. **Action:** the paper's second headline validation claim is void.
- **F10 - Forward-test gate.** Complete a live forward-paper window of at least 252 trading days (research-proposed extension of the source's 60-day program) with the decision log preserved. **Fail** if realized Sharpe < 1.00, if USD CAGR < 0, or if any of the two source-disclosed incident classes (missing risk config, identifier collision) recurs after its stated fix. **Action:** deployment claims unsupported; stop the forward program and re-derive the rule.
- **F11 - Direction ablation.** Run long-only and long+short variants of the identical rule (research-proposed) to adjudicate the paper's silence on direction against the secondary source's SECP shorting note. **Fail** if the long-only variant retains less than 50% of PKR CAGR (or, conversely, if the long-only variant is where all of the edge sits, in which case the long+short headline is misattributed). **Action:** restate the headline under the surviving configuration only.
- **F12 - Universe / survivorship audit.** Rebuild the panel point-in-time from a vendor carrying delisted names (ENGRO restored as ENGROH where applicable) with pre-declared membership rules. **Fail** if trade count moves by more than 10% or PKR CAGR by more than 1.5 pp from the printed values. **Action:** the result is driven by universe construction.
- **F13 - Capacity gate (research-proposed, since the source gives no derivation).** Cap participation at 20% of 20-day ADV (research-proposed) up to PKR 100M and require net CAGR to remain positive after the F7 cost ladder at 45 bp. **Fail** if net CAGR <= 0 under the cap. **Action:** capacity-limited and unsuitable for the institutional audience the source targets.
- **F14 - Placebo gate.** 1,000 draws (research-defined) of date-permuted / label-shuffled entries on the same 30-symbol panel with identical sizing and cost model. **Fail** if the observed PKR CAGR does not exceed the 95th percentile of the placebo distribution. **Action:** the reported edge is consistent with random entries under this sizing and cost stack.
- **Action-on-failure map (research-defined).** No gate may be rescued by retuning: if a gate fails, the failure is recorded in this record's Negative evidence and the status remains `research-only`. Any parameter change after a failure starts a new trial count that must be added to F4's N. Zero of F1-F14 has been executed by this record.

## Crypto portability

`adapted` - the mechanism family is price-only and in principle transportable, but **the source demonstrates zero crypto evidence**, so every crypto number would be a ported hypothesis rather than crypto empirical evidence, and crypto performance is `unproven`.

- **What ports cleanly.** The signal uses only completed OHLCV candles and a moving-average/trend-regime condition; it needs no exchange-specific field, no order book, no funding series and no on-chain data, so the *construction* can be re-specified on any continuous price series.
- **What does not port as stated.**
  - **Session structure.** PSX trades a single daytime session on business days; crypto perpetuals trade 24/7 with no session close, so `two consecutive candles` means something different under a daily bar convention, and the paper's unstated timezone/candle-boundary convention has to be redefined.
  - **Funding and leverage.** The source models neither. A perpetual leg carries periodic funding and liquidation mechanics that can dominate a multi-day holding period at the sizing tiers described (1-5% risk per trade) - an entirely new cost and risk term the source never contemplates.
  - **Venue fragmentation and instrument choice.** One venue, one currency, one cash market in the source; crypto would require choosing spot vs perpetual, one venue vs many, and dealing with mark/index price vs last price.
  - **Currency.** PKR/USD divergence is a first-order driver of the source's own headline (10.43 pp, research-computed). In crypto the base currency is USD/stablecoin-denominated, so that specific effect disappears while being replaced by stablecoin/depeg and venue-withdrawal risk.
  - **Universe churn.** PSX delistings are slow and disclosed (ENGRO); crypto listing and delisting churn is far faster, which makes the source's unstated point-in-time universe rules a much larger bias in crypto.
  - **Contract and lot rules.** The source's sizing is built around the April 2024 PSX one-share lot reform; crypto tick sizes, lot sizes, minimum notional and contract multipliers differ per symbol and per venue.
  - **Shorting regime.** The source's retail shorting is reportedly blocked by local regulation; crypto perps permit both directions but add bankruptcy/ADL and exchange-counterparty risk that the source's cash-equity framing does not address.
  - **Capacity.** The source's own ceiling is ~PKR 100M practical against ~PKR 500M hard; no USD equivalent is computed here because the source supplies no FX rate. Crypto capacity regimes span many orders of magnitude and would need an entirely different analysis.
- **Porting requirement.** Any crypto test must re-derive candle conventions, add a funding and liquidation cost model, fix a point-in-time universe with delisting history, and re-run F1-F14 under the F7 cost ladder. None of that has been done.

## Limitations

- `underspecified`: the entry/exit parameters, the EMA period, the master trend regime's definition and timeframe, the fill and order timing, the holding period, the trade direction, the 30-symbol ticker list, the point-in-time universe rules, the FX conversion convention, the permutation count behind `p = 0.0`, the capacity derivation, and the independent archive's identity are all either deliberately withheld or never stated.
- `data gap`: no commission schedule, no measured spread, no slippage model, no market impact, no participation cap, no latency, no fill model, no leverage or margin model, no borrow cost - the single 22.5 bp assumption is the entire cost model, and it is labelled `assumed` by the source itself.
- `data gap`: the equal-weight buy-and-hold benchmark claimed in Section 5.4 is not printed; the ~2000-2020 archive result claimed in Section 6.4 is not printed; the live forward result promised in the abstract is not printed.
- `not independently reproduced`: every performance, statistical and capacity figure in this record is third-party source-reported. Only provenance hashing, a two-PDF text diff, raster-table transcription and one arithmetic identity check were performed by this record.
- `unproven`: crypto portability, and any claim that the rule would survive a cost ladder above 22.5 bp, a point-in-time universe, or a genuine out-of-sample window.
- **Source-quality limits.** Single-author, non-peer-reviewed working paper; zero citations; an unfilled placeholder in the central statistical section; the same work posted twice under two SSRN IDs on consecutive days with different page counts and different subject classifications; a printed testing link that resolves through a shortener to a social-media post rather than a replication package; restrictive licence.
- **Interpretation confidence split.** Provenance, evidence extraction and the identification of contradictions in this record are high-confidence (all surfaces were read directly and hashed). Confidence in the *signal* interpretation is materially lower because the rule is withheld by design - which is why `confidence: medium` at record level with `underspecified` at signal level, rather than any higher reading.
- **Scope limit.** This record normalises a frontier-equity rule for research purposes. It contains no backtest, no downloaded PSX data, no Wiki Brain write, no Kanban task and no Paper/Testnet/Live action.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack. No PSX data has been pulled, no rule has been coded, no backtest has been run, no production card has been created, and no Qlib full backtest, Paper, Testnet or Live stage has been reached or attempted. The source's own implementation (a proprietary multi-tenant system with a live forward-paper program) is the author's, is not published, and is not ours.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not strategy adoption, implementation authorization, or permission to run Paper/Testnet/Live. No wording, evidence count, confidence value or schedule behaviour in this record promotes it.

## Related Wiki records

Read-only `kb_search` on `trend following time-series momentum falsification` returned 10 adjacent pages; the following are linked as retrieval hooks for future synthesis and contradiction checks only (no Wiki page was written by this run):

- [[quant/alphatrend-adaptive-exit-generalization-falsification-crypto-perpetual-2026-09-13]]
- [[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]
- [[quant/crypto-trend-atlas-causal-multi-speed-perpetual-portfolio-2026-09-12]]
- [[quant/futures-quad-trend-carry-skew-vov-composite-2026-09-11]]
- [[quant/futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]]
- [[quant/crypto-perpetual-regime-aligned-right-tail-trend-cost-hurdle-2026-09-13]]
- [[quant/bitget-perpetual-shuffled-null-falsification-cross-sectional-momentum-2026-09-13]]

No pre-existing Wiki record covers the Pakistan Stock Exchange or any frontier-equity universe; no Wiki page matching this source identity was found.

## Sources

1. Ertiza Abbas, *KSE Sentinel: A Rule-Based Trend-Continuation Strategy for the Pakistan Stock Exchange (PSX) - Design, Statistical Validation, and Live Forward Testing*, SSRN working paper, `abstract_id=7093159`, Date Written July 07, 2026, Posted 28 Jul 2026, 14 pages. Landing: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7093159> - DOI: <https://doi.org/10.2139/ssrn.7093159>. Pinned PDF (read 2026-09-29): `https://papers.ssrn.com/sol3/Delivery.cfm/7093159.pdf?abstractid=7093159&mirid=1`, 287,604 bytes, 14 pages, SHA-256 `cc9e7d63b36fc8521ff4281c6dcafb4dabe9bfd569d20bf0527d3d9a8644d719`.
2. Ertiza Abbas, same title, SSRN `abstract_id=7102818`, Date Written July 07, 2026, Posted 29 Jul 2026, 13 pages (companion posting of the same work). Landing: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7102818> - DOI: <https://doi.org/10.2139/ssrn.7102818>. Pinned PDF (read 2026-09-29): `https://papers.ssrn.com/sol3/Delivery.cfm/7102818.pdf?abstractid=7102818&mirid=1`, 296,570 bytes, 13 pages, SHA-256 `c4ff62868c11e0559545bc31daf658e7380e398747c9486320628f406a52ebbb`.
3. Ertiza Abbas, `PSX Algorithmic Trading System Launched`, LinkedIn post, reached by resolving the link shortener printed on p.2 of source 1; read 2026-09-29 without login (post body public, reactions and comments login-walled): <https://www.linkedin.com/posts/abbas-ertiza_algorithmictrading-quantfinance-psx-share-7479859295233167361-nr_u/>.
4. As printed in source 1, p.2: `https://shorturl.at/n9GTR` - a link shortener, recorded as printed for traceability; not a stable identifier.
5. Works **cited by** source 1 and used by it for framing only (not read by this record, so any claim resting on them is `data gap`): Jegadeesh and Titman (1993), *Returns to Buying Winners and Selling Losers*, Journal of Finance 48(1), 65-91; Moskowitz, Ooi and Pedersen (2012), *Time Series Momentum*, Journal of Financial Economics 104(2), 228-250; Hurst, Ooi and Pedersen (2017), *A Century of Evidence on Trend-Following Investing*, Journal of Portfolio Management 44(1), 15-29; Bailey and Lopez de Prado (2014), *The Deflated Sharpe Ratio*, Journal of Portfolio Management 40(5), 94-107; Bailey, Borwein, Lopez de Prado and Zhu (2014), *Pseudo-Mathematics and Financial Charlatanism*, Notices of the AMS 61(5), 458-471; Securities and Exchange Commission of Pakistan (2025), *Concept Paper: Regulating Algorithmic Trading in Pakistan*, May 2025.
