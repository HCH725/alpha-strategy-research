---
schema: strategy-research-record-v1
title: "A Symmetric Trend Veto Is Two Different Objects: Short- and Long-Side Asymmetry of a +/-3 Percent Trailing 24 Hour Index Entry Veto over 1,698,988 Barrier Outcomes on Twenty Cryptocurrency Perpetuals (SSRN 7418978)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - entry-filter
  - exposure-control
  - trailing-return-veto
  - barrier-options
  - day-clustered-bootstrap
  - negative-result
status: research-only
confidence: medium
source_as_of: 2026-09-07
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7418978"
  - "https://doi.org/10.2139/ssrn.7418978"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "SSRN landing author line prints 'Alexandr Dashyan' (Independent Researcher) while the PDF title block prints 'Aleksandr Dashyan, Independent Researcher, Yerevan, Armenia' with ORCID 0009-0009-5118-5184 and correspondence alikdashyan1@gmail.com; both spellings preserved exactly as printed, not reconciled."
  - "Landing shows a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0) licence badge while PDF p.1 states 'Copyright 2026 Aleksandr Dashyan. All rights reserved.' and forbids reproduction, distribution or quotation at length without prior written permission; licence conflict unreconciled, so this record normalises only short printed values, table cells and section references."
  - "SSRN landing prints headings '0 References' and '0 Citations' while the PDF reference list carries 17 entries (12 methodological works plus Dashyan 2026a-2026e); unreconciled, same apparatus defect as the sibling SSRN records in this repository."
  - "Five unreconciled date expressions: PDF cover 'Working paper. Preliminary. Comments welcome. This version: September 2026.'; landing 'Date Written: August 25, 2026'; landing 'Posted: 7 Sep 2026'; suggested citation '(August 25, 2026)'; PDF metadata /CreationDate D:20260905233910+04'00' (2026-09-05 23:39:10 +04'00')."
  - "Section 3.4 states 'Section 6.3 shows that the two indices agree on the veto decision 96 to 99 percent' and Section 9 states the index choice is 'validated in Section 6.3', but printed Section 6.3 is 'The trailing window is not special either' and the index-agreement material is printed as Section 6.7 'Does the study index measure the live gate'; internal cross-reference error, unreconciled."
  - "Section 8 prints a long-veto blocked set of 136 candidates at 33.82 percent win rate with a mean net of -0.5996 percent per candidate, but under this paper's own stated net geometry (+2.00 percent win / -2.00 percent loss) that win rate implies -0.6472 percent (implied win rate for the printed mean is 35.01 percent); the matching short cell reproduces exactly (35.35 percent implies -0.5860 against the printed -0.5859). Section 8 does not restate which geometry the cited internal record used, so the discrepancy is unreconciled."
  - "The identical live-cell day-clustered one-sided probability is printed as 0.974 (abstract and Table 2), 0.973 (Table 3 live row and Table 4 at the 3.0 percent threshold) and 0.975 (Table 5 at the 24 hour window) for the short veto, and as 0.386 (abstract and Table 2), 0.384 (Table 3), 0.383 (Table 4) and 0.385 (Table 5) for the long veto; the resample count differs by table (10,000 vs 20,000) but that is never stated as the cause, unreconciled."
  - "Table 1 prints 167,663 brackets for 'Short, blocked, trailing at or above plus 3 percent' and 167,664 for 'Long, allowed, trailing at or above plus 3 percent' although both cells are defined by the identical condition on the identical hour set, while the mirror pair prints 146,458 for both sides; a plausible reading is side-specific drops of the 362 open ends, but the source never says so, unreconciled."
  - "Section 3.2 states 'Of 1,700,000 candidate brackets, 99.979 percent resolve and 362 open ends are dropped, leaving 1,698,988 resolved brackets', but 1,700,000 x 0.99979 - 362 = 1,699,281, not 1,698,988; the components close only as rounding (1,698,988 + 362 = 1,699,350), unreconciled."
---

# A Symmetric Trend Veto Is Two Different Objects: Short- and Long-Side Asymmetry of a +/-3 Percent Trailing 24 Hour Index Entry Veto over 1,698,988 Barrier Outcomes on Twenty Cryptocurrency Perpetuals (SSRN 7418978)

## Provenance

- **Primary source.** SSRN preprint, `abstract_id=7418978`, DOI [`10.2139/ssrn.7418978`](https://doi.org/10.2139/ssrn.7418978). Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7418978>.
- **Exact titles.** PDF title block (p.1): `A Symmetric Trend Veto Is Two Different Objects: 5.7 Years of Barrier Outcomes on Twenty Cryptocurrency Perpetuals`, with subtitle `The short side and long side of a symmetric plus or minus 3 percent trailing return filter are not the same object, and the asymmetry is not a barrier geometry artifact`. Landing title: identical main title.
- **Author (recorded exactly as each surface prints it; the surfaces disagree).** SSRN author line: **Alexandr Dashyan**, `Independent Researcher`. PDF title block: **Aleksandr Dashyan**, `Independent Researcher, Yerevan, Armenia`, `ORCID: 0009-0009-5118-5184`, correspondence `alikdashyan1@gmail.com`. The `Alexandr` / `Aleksandr` difference is a source-level discrepancy and is not reconciled here. Single author, no co-authors printed.
- **Dates (printed five ways; not reconciled).** PDF cover (p.1): `Working paper. Preliminary. Comments welcome. This version: September 2026.` Landing: `Date Written: August 25, 2026`; `Posted: 7 Sep 2026`; suggested citation `(August 25, 2026)`. PDF metadata `/CreationDate D:20260905233910+04'00'`, `/Creator Microsoft® Word 2024`, `/Producer Microsoft® Word 2024`, `/Author python-docx` (the `/Author` field literally reads `python-docx`, a generation artefact rather than a name, recorded as printed).
- **Publication / review status.** SSRN working paper; the landing carries no journal, no issue and no peer-review statement and the PDF prints no peer-review banner, so peer-review status is `not stated in source`. Landing headings read `0 References` / `0 Citations`; paper statistics at read time: `DOWNLOADS 30`, `ABSTRACT VIEWS 89`.
- **Licence (conflicting, unreconciled).** Landing shows a `Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International` badge; PDF p.1 states `Copyright 2026 Aleksandr Dashyan. All rights reserved.` with an explicit no-reproduction / no-quotation-at-length clause. Because the two surfaces conflict, this record normalises only short printed values, table cells and section references and reproduces no extended passages.
- **Landing read in a browser session on 2026-09-29** after the Cloudflare interstitial cleared (single read): `25 Pages`, `Posted: 7 Sep 2026`, `Date Written: August 25, 2026`, the full abstract, the Keywords block, the Declaration of Interest / Funder Statement (`no interest, that is my personal research with my personal funds`), and the `Open PDF in Browser` delivery link.
- **Pinned PDF.** Retrieved 2026-09-29 through the landing's `Open PDF in Browser` delivery object (`https://papers.ssrn.com/sol3/Delivery.cfm/7418978.pdf?abstractid=7418978&mirid=1&type=2`, a stable non-expiring delivery link with **no presigned or session-bound URL stored anywhere in this record**), **697,629 bytes, 25 pages, SHA-256 `b07711713ff83b5f4f145466b5ecfb42dc42680eeb35d7dd188da51f400182da`**, text extracted with `pypdf 6.16.2` to **54,379 characters / 736 lines**, all 25 pages read including sections 1-10, Sections 3.1-3.5, Sections 6.1-6.7, Tables 1-5, the captions of Figures 1-7, the `Author Contributions and Use of AI Tools` block, the `Data and Code Availability` block, and the reference list read entry by entry (**17 entries**: 12 methodological works and Dashyan 2026a-2026e). JEL printed on p.1: `G11, G14, G12, C12, C58`. Keywords printed on p.1: `trend following, time series momentum, exposure control, stop loss filters, barrier options, cryptocurrency perpetual futures, win rate, base rate, day clustered bootstrap, negative results, asymmetry`.
- **AI / authorship disclosure (source-reported, PDF `Author Contributions and Use of AI Tools`).** The author states he designed the study and made every modelling and inferential decision; large language model assistants were used as instruments under his direction in three roles - writing and executing the analysis code from his specifications, adversarial red-teaming of his own claims (which produced the barrier geometry control, the de-overlapped independence check and the base-rate correction), and drafting prose from his outline. The block states `Claude is a tool, not an author`, and reports two safeguards: every number pinned to a results ledger naming its script, and the resolved bracket table regenerated from raw bars and confirmed identical field by field.
- **Companion works, now identified with identifiers (PDF reference list, first record in this repository to pin them).** Dashyan (2026a) *Short-horizon directional non-predictability in cryptocurrency perpetual futures: a multi-method negative result under adversarial verification*, DOI `10.2139/ssrn.7306538`; Dashyan (2026b) *Adversarial backtest verification: catching overfitting, beta, collinearity, and look-ahead in a live trading-research program*, DOI `10.2139/ssrn.7338919`; Dashyan (2026c) *Risk control as the durable edge: loss filtering, profit-armed ratchets, and market-neutral carry when direction fails*, DOI `10.2139/ssrn.7345542`; Dashyan (2026d) *A real edge that loses: anatomy of a backtest-to-live gap in cryptocurrency perpetual futures*, DOI `10.2139/ssrn.7353678`; Dashyan (2026e) *The tail is the only signal: flush reversion in equity indices and crypto perpetual futures*, DOI `10.2139/ssrn.7363482`. The latter three already exist as repository records (`crypto-perp-risk-control-...-ssrn-7345542-2026-09-28.md`, `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md`, `equity-index-tail-flush-reversion-disjoint-band-familywise-2026-09-27.md`); **7306538 and 7338919 are still uncaptured and are deferred to a future run.**
- **Deterministic pre-write source-identity dedup** (hidden-inclusive `rg -uuu` over the whole checkout, including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` at 1,088,787 bytes): `7418978`, `10.2139/ssrn.7418978`, `A Symmetric Trend Veto`, `Barrier Outcomes on Twenty Cryptocurrency`, `trend veto`, `0009-0009-5118-5184`, `7306538`, `7338919` - **all zero hits outside this file**. Author tokens `alikdashyan1` hit exactly two existing files and `Dashyan` hits exactly three existing files, all of them the sibling records named above. Concept tokens were also scanned: `no new short`, `against an extended move`, `already rallied`, `after a rally` all zero; `entry veto` hits one unrelated record; `veto` hits 31 files of which the only crypto-perpetual neighbours are an OI/premium-divergence veto filter and the sibling 7345542 entry filter (different signal, see below). Positive control `novy-marx` returned **16 files** in the same session. `coverage_manifest.csv` (last written 2026-08-31, therefore stale) returns 0 for every new token. `git log --oneline -20` was used as a convenience glance only and does not satisfy dedup.
- **Four-axis distinction against adjacent repository records** (source identity and mechanism differ in every pair):
  - `crypto-perp-risk-control-loss-filter-profit-armed-ratchet-market-neutral-funding-carry-ssrn-7345542-2026-09-28.md` (SSRN `7345542`, same author): mechanism there is a **one-hour per-coin Bollinger extreme entry filter (`R4`)** measured on a single month of one LLM book, plus an account-level ratchet and a funding-carry sleeve. Mechanism here is a **market-wide chained-index trailing 24 hour return veto measured unconditionally over 5.7 years on 1.7 million bracket outcomes**, with no sizing, no capital and no signal feed. Different source, different signal construction (index trailing return vs per-coin band position), different horizon/regime (2021-2026 unconditional vs June 2026 selected book), different material data dependency (constructed cross-sectional index vs LLM feature snapshot).
  - `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` (SSRN `7353678`, same author): different source, different mechanism (anatomy of one directional signal's deployment gap); this paper cites it only for the fact that the deployed book lost money live.
  - `equity-index-tail-flush-reversion-disjoint-band-familywise-2026-09-27.md` (SSRN `7363482`, same author): different source, different mechanism (tail-event reversion), different market for its main claim.
  - `tradingview-binance-perpetual-oi-premium-divergence-veto-filter-2026-09-19.md`: shares only the word `veto`; there the veto is an open-interest / premium divergence condition on a single coin, here it is a trailing return of a cross-sectional index applied to entry timing on every coin.
  - `crypto-perpetual-volume-spike-momentum-liquidity-inversion-trailing-exit-falsification-2026-09-13.md` and `crypto-risk-managed-tsmom-crash-state-de-risking-drawdown-control-2026-09-14.md`: trailing rules there govern **exits** of a momentum book; here the trailing return governs **entry refusal** and the paper's own claim is explicitly direction selection, not profitability.

## Economic mechanism

### Source-reported

The paper's premise is exposure control, not prediction. A leveraged directional book that trades both sides of a market carries a symmetric trailing return veto: block a new short when a market-wide index's trailing 24 hour return sits at or above **+3 percent**, and block a new long when it sits at or below **-3 percent** - same threshold, same window, both sides. The paper asks whether the two halves deserve the same treatment and reports that they do not.

Source-stated rationale and framing:

1. **Short side - refusing to chase a rally.** Shorting into an extended rally is described as the worst short state there is; the veto removes exactly that state. The stated justification is that the vetoed subset is *worse than average for that side*, not that it loses money (almost every state loses money at this geometry because of the fee).
2. **Long side - the mirror was carried on faith.** The long half of the same rule is measured to block a subset indistinguishable from average, with the wrong sign at the live horizon, so the source concludes it is exposure control at best on one side and inertia on the other.
3. **Literature positioning (source-reported).** The veto is framed as a short-horizon relative of time series momentum (Moskowitz, Ooi and Pedersen 2012; Hurst, Ooi and Pedersen 2017) run in reverse - `Time series momentum says follow the move; a symmetric veto says do not fade it` - and as a small concrete instance of the documented asymmetry of trend/momentum exposure (Daniel and Moskowitz 2016 on momentum crashes concentrated in recoveries from declines; Ilmanen 2011 chapters 13 and 20 on built-in crash asymmetry of carry and trend).
4. **Methodological premise.** A barrier-race win rate has a base rate set by the barrier distances (47.5 percent here, not 50), so every comparison is made **within a side against that side's own base rate**; overlapping hourly entries are handled by a day-clustered bootstrap rather than binomial intervals.
5. **Explicit non-claim.** The paper states it makes no trading recommendation, reports no ROI, drawdown or Sharpe because it sequences no capital, and that `no state at this geometry is profitable after fees`.

### Research interpretation

Component roles normalised so each can be ablated later:

```text
Regime / entry gate:  refusal to open a NEW position when a market-wide chained
                      equal-weight index's trailing return (default 24h) crosses
                      +/-3 percent; blocks entries only, never closes positions
Primary signal:       NONE - the study is unconditional and selects no direction
                      (every hour, every coin, both sides, no signal selection)
Oracle / outcome:     single take-profit / stop-loss bracket resolved by first
                      touch on 15-minute bars, flat 0.10 percent round-trip fee
Risk / exit:          bracket stop at -1.9 percent gross / target at +2.1 percent
                      gross, 30-day cap, no time exits, no sizing, no compounding
```

Falsifiable mechanism hypotheses (Scout interpretation, not source wording):

- **(a) Adverse selection of shorts into rallies.** A short opened after the market has already rallied 3 percent or more is on average worse than a short opened elsewhere, because it fades a move with remaining momentum; refusing it therefore removes losers rather than winners. Predicted signature: negative blocked-minus-allowed win-rate gap for shorts, stable sign across years, thresholds and windows, surviving a barrier-geometry control.
- **(b) The mirror claim should fail.** A long opened after a 3 percent sell-off is *not* systematically worse than other longs in this universe, because the universe's down-drift already makes longs uniformly bad. Predicted signature: long blocked-minus-allowed gap near zero with unstable sign at the live horizon.
- **(c) Exposure control versus trade selection are separable.** Even if the veto carries little per-trade information, it can still prevent a leveraged book from taking many correlated positions into a single move. Predicted signature: a large drawdown reduction on correlated-selloff days with a small per-trade win-rate gap - which is what Section 8 of the source reports for its own live book.
- **(d) Horizon specificity.** The reported asymmetry is a property of the 24 hour horizon the live gate runs on; the source itself reports the long side turning negative at 12, 48 and 168 hours, so the clean two-object split is horizon-conditional.

No component is assumed to contribute alpha; ablation and the failure rules are in the Falsification plan.

## Signal

All items below are source-reported unless explicitly marked `research-proposed` or `data gap`. The study is **not a sequenced strategy**: it resolves an outcome oracle, so several strategy fields are structurally absent rather than omitted.

### Market-wide index and the veto state (Sections 3.4, 6.7)

- **Formation timestamp.** The veto reads a market-wide index and its trailing 24 hour return at each **hourly** entry timestamp. Entries are hourly (brackets open at the close of the 15-minute bar ending on the hour), so the veto state is evaluated at that hour. Whether the trailing window is inclusive of the entry bar, and the exact timezone/clock of the index series, are `data gap` (no timezone is printed anywhere in the paper).
- **Study index (source-reported).** A **chained equal-weight index**: at each 15-minute step take the cross-sectional mean of the simple returns of the coins present at both ends of the step, then compound. Stated rationale: no window-start dependence and no listing discontinuity, and identical to the live formula on a fixed coin set over 24 hours.
- **Live-gate index (source-reported, for contrast).** The live book normalised each coin to its first price in a rolling window and averaged the levels - described as a sound equal-weight index over a fixed **109 day** window with a constant coin set, but degenerating over 5.7 years because newly listed coins enter at level one against incumbents at two or three (a listing discontinuity) and because the normalisation weight becomes cumulative appreciation since 2021 (turning an equal-weight index into a momentum-weighted one).
- **Index agreement (source-reported, Section 6.7).** Over the **2,688** scan overlap where both can be computed: trailing-24h-return correlation **0.964**, mean absolute difference **0.49 pp**, bias **+0.014 pp**; veto-decision agreement **96.9 / 96.4 percent** (long / short) at +/-3 percent and **98.6 / 99.3 percent** at +/-5 percent; running the live formula on the study's own bars gives 96.9 percent against 96.8 percent for the chained index, so residual disagreement is attributed to price data (live frame scan-time snapshots vs official bar closes, per-coin median difference **0.09 to 0.28 percent**), with **84 percent** of disagreements within one percentage point of the threshold.
- **Measurement noise finding (source-reported, Sections 6.7 and 9).** Standard deviation of the difference between the two indices is **0.76 percentage points**, and **about 25 percent** of scans sit in the 2-4 percent band where the +/-3 percent decision is partly a coin flip - so the hard threshold behaves closer to a soft weighting than to the rule it is written as.

### The veto rule (Sections 1, 5)

- **Short veto (source-reported).** Block a **new short** when the index trailing 24 hour return is **>= +3 percent**. Fires on **19.74 percent** of short candidate hours (research-computed from the printed 167,663 blocked of 849,494 per-side hours).
- **Long veto (source-reported).** Block a **new long** when the trailing return is **<= -3 percent**. Source prints it as firing on **17.2 percent** of long candidate hours; research-computed 146,458 / 849,494 = **17.24 percent** (reproduces).
- **Semantics.** The veto **refuses entries only**; it never closes an open position, has no expiry, no re-entry rule and no interaction with sizing - all `data gap`.
- **Thresholds are not fitted (source-reported, Section 6.2).** `+3 percent` is the threshold `the trading system was built with`, so the single-cut test is described as pre-registered rather than fished; a six-threshold sweep (2.0 / 2.5 / 3.0 / 3.5 / 4.0 / 5.0 percent) and a four-window sweep (12 / 24 / 48 / 168 hours) are reported as robustness, with an explicit familywise rotation-null correction.

### The outcome oracle (Sections 3.2, 3.3)

- **Bracket geometry (source-reported).** Take profit **+2.1 percent gross**, stop **-1.9 percent gross**; after the **0.10 percent round-trip fee** the net outcomes are exactly **+2.00 percent** on a win and **-2.00 percent** on a loss, which makes the profit-and-loss breakeven win rate **50.00 percent** while the zero-drift first-passage base rate is `1.9 / (2.1 + 1.9)` = **47.5 percent** (reproduced: 47.5).
- **Resolution (source-reported).** 15-minute high/low bars, pessimistic: a single bar spanning both barriers scores as the stop. Entry is the close of the 15-minute bar ending on the hour and the barrier walk begins on the **next** bar, so no part of the entry bar resolves the trade it opened. **No time exits**; a position runs to a barrier or the **30-day cap**; an entry touching no barrier within 30 days is an open end and is **dropped** from every statistic.
- **Counts (source-reported).** `Of 1,700,000 candidate brackets, 99.979 percent resolve and 362 open ends are dropped, leaving 1,698,988 resolved brackets over 2,070 trading days from 2 January 2021 to 2 September 2026.` Research-computed: 1,698,988 + 362 = 1,699,350 and 1,698,988 / 1,699,350 = **99.9787 percent**; 2021-01-02 to 2026-09-02 inclusive = **2,070 calendar days** (crypto trades 24/7, so calendar = trading days here) and **5.665 years** (the printed `5.7 years`). The printed `1,700,000` candidate figure does not close with the other two printed components (contradiction #9).
- **What is deliberately absent (source-reported).** No position sizing, no capital, no compounding, no concurrency, therefore **no return on investment, no drawdown and no Sharpe ratio**; the reported units are win rates and per-trade net outcomes only.
- **By-side base rates (source-reported, Section 3.3).** Pooled **47.5 percent**; **45.67 percent** for longs and **49.37 percent** for shorts (the alternative-coin universe drifted down over 2021-2026, so shorting was structurally the better side).

### Statistics (Section 3.5)

- Day-clustered bootstrap resampling whole trading days: **10,000** resamples for a single cell, **20,000** for the vetoed-versus-allowed contrast. All Table 2 inference uses whole-day resampling because hourly entries overlap.
- The source's own admission: day clustering does not close the overlap (about **one third** of brackets resolve on a later calendar day than they open; longest hold **13 days**), so intervals `should be read as, if anything, a little too tight`.
- The de-overlapped variant lets a coin re-enter only after its prior trade resolves, cutting the sample to **329,514** brackets.

### Research-proposed operationalisation (NOT in the source)

- Sequencing these brackets into a tradeable book - one position per coin, a candidate generator, sizing, re-entry after a vetoed hour, and a rule for which of the many overlapping hourly candidates to take - is **`research-proposed`**. The source explicitly does not sequence a book, and this record must not be read as a strategy specification.
- The **cost ladder** in the Falsification plan, the **cross-venue index** variant, and the **frozen forward window** are all `research-defined` / `research-proposed`; the source specifies none of them.

## Required data

- **Instruments / universe:** twenty Binance USD-margined perpetual futures, `a real traded set with real listing dates`, panel growing from **13 coins in early 2021 to all 20 by 2025**. The ticker list is `listed in full in the analysis scripts` and is **not printed in the paper** (`data gap`); the only coin named anywhere in the text is **FIL** (Section 6.4, the least supportive leave-one-out drop).
- **Venue / market type:** Binance perpetual futures only (single venue); cash-settled with a funding mechanism, but **funding is never used as an input or an outcome** in this study (`funding` occurs once in the whole PDF, in the instrument definition).
- **Fields:** 15-minute open, high, low and close bars per coin (the Data and Code Availability block states the price data comes from `a public exchange endpoint requiring no key`); per-coin listing dates; the cross-sectional index construction. No order book, depth, trades/aggressor, open interest, options surface, borrow or funding field is used (`not stated in source` as requirements).
- **Timeframe / resolution:** 15-minute bars for index steps and barrier resolution; hourly entry stamps; trailing windows of 12 / 24 / 48 / 168 hours.
- **Point-in-time / look-ahead:** entry is fixed at the close of the 15-minute bar ending on the hour with the barrier walk starting on the next bar, which is a stated look-ahead guard for *resolution*. Whether the veto's trailing window includes the entry bar, and any publication/availability lag for the index, are `data gap`.
- **Timestamps / timezone:** `data gap` - no timezone, clock source, alignment or out-of-order handling is printed for any series; the only time anchor given is the date range and the 15-minute/ hourly cadence.
- **Missing data:** `data gap` - no null/stale/suspended/partial-bar policy is stated; coins enter at listing dates and the chained index handles the discontinuity but `cannot add history that does not exist`; no imputation is described (and none should be assumed).
- **Survivorship:** the source asserts the set is not survivorship-filtered because listing dates are real, but the universe is `fixed by that program` (20 coins traded during 2026) and the paper does not report delisted coins or coins the live program never traded (`data gap`).

## Execution assumptions

### Cost model (Methods-level determination)

The cost and fill treatment was read from Sections 3.2, 3.3, 7, 9, the Abstract and the `Data and Code Availability` block, plus a whole-document term scan of the extracted 54,379-character text:

- **The only friction modelled is a flat `0.10 percent round trip fee`**, folded into the bracket so that a win nets +2.00 percent and a loss nets -2.00 percent. The source states the gross geometry is `fair` and that the 2.5-point gap between the 47.5 percent base rate and the 50 percent breakeven `is precisely the 0.10 percent fee`.
- **Term scan counts (zero means absent, never zero-cost):** `slippage` 0, `bid-ask` 0, `market impact` 0, `latency` 0, `limit order` 0, `market order` 0, `commission` 0, `maker` 0, `taker` 0, `order book` 0, `capacity` 0, `turnover` 0, `liquidat*` 0, `borrow` 0. `spread` occurs once and only in the phrase `spread as a trend` (not a cost); `margin` occurs only in `marginal` / `by a small margin`; `fill` occurs only in `filled point` (figure legend); `leverage` occurs twice as description of the motivating book (`A leveraged directional book`), with no margin, maintenance-margin or liquidation model anywhere.
- Therefore **spread, slippage, market impact, participation, order type, fill model, latency, leverage/margin, liquidation, borrow, funding as a cost line, and capacity are all `data gap` - never to be read as 0.**
- **Sharpe / ROI / drawdown:** explicitly **not reported by design** (`this paper reports no Sharpe ratio because it sequences no capital`). The two drawdown numbers that do appear belong to the cited live book in Section 8, not to this study.

### Timing, fills and sizing (source-reported)

- **Signal-to-order:** entries stamp at the close of the 15-minute bar ending on the hour; barrier walk starts next bar. Market vs limit order, partial fills, slippage on the bracket and latency are `data gap`.
- **Pessimistic resolver:** a bar spanning both barriers scores as a stop - a conservative fill convention stated by the source.
- **Sizing / leverage:** none - no capital, no sizing, no concurrency by construction.
- **Open ends:** dropped (362 of ~1.7 million), with the source's stated reason that counting them as scratch wins `would break the breakeven arithmetic`.

### Section 8 live-book figures (cited, not re-run)

The 109-day selected-book numbers are `cited from the program's dated internal record and the companion papers (Dashyan, 2026c, 2026d) and were not re-run for this paper`. Live geometry, sizing and cost detail behind those numbers are `data gap` in this paper (and the long cell does not reconcile - contradiction #6).

## Evidence

### Source-reported

Every figure below is a third-party claim from the pinned PDF, **not** independently reproduced, with table/section provenance given so a reviewer can locate it in the 25-page version.

- **Setting (Sections 3.1-3.5).** 20 Binance perpetuals with real listing dates (13 -> 20 coins); 1,698,988 resolved brackets over 2,070 days, 2021-01-02 to 2026-09-02; bracket TP +2.1 / SL -1.9 gross, net +/-2.00 percent after the 0.10 percent round-trip fee; unconditional design, both sides, every hour, no signal selection.
- **Table 1 - vetoed, allowed and deep cells (day-clustered 95 percent CI, 10,000 resamples).** Long blocked (<= -3 percent) n = **146,458**, realWR **45.90 percent** [44.16, 47.63], net per trade **-0.1641 percent**; Short blocked (>= +3 percent) n = **167,663**, **47.97 percent** [46.43, 49.56], **-0.0813 percent**; Short allowed (<= -3 percent cell) n = **146,458**, **49.05 percent** [47.33, 50.79], **-0.0380 percent**; Long allowed (>= +3 percent cell) n = **167,664**, **46.86 percent** [45.31, 48.40], **-0.1254 percent**; Long deep (<= -5 percent) n = **66,622**, **45.84 percent** [43.60, 48.20], **-0.1664 percent**; Short deep (>= +5 percent) n = **76,627**, **48.32 percent** [46.36, 50.45], **-0.0673 percent**. Base rates printed: long **45.67 percent**, short **49.37 percent**, breakeven **50.00 percent**.
- **Table 2 - the central contrast (day-clustered, 20,000 resamples).** Short veto: vetoed **47.97** vs allowed **49.71 percent** -> **-1.74 pp**, 95 percent CI **[-3.52, +0.01]**, one-sided P(below zero) **0.974**. Long veto: vetoed **45.90** vs allowed **45.62 percent** -> **+0.28 pp**, CI **[-1.64, +2.20]**, **P 0.386**. The program's stated kill convention is a one-sided probability of **0.95**, which the short veto clears `though its two-sided interval ... just touches zero`.
- **Figure 2 / Section 5 - era stability.** Short veto holds its sign in **5 of 6** calendar years with mean difference **-1.87 pp** (only 2021 flips); long veto holds in **2 of 6** with mean **+0.31 pp**.
- **Section 7 - shape of the sides.** Long win rate ranges **44.4 to 47.3 percent** across all twelve trailing-return buckets and never approaches breakeven; short line is highest where the market has fallen a little (**-4 to -1 percent**, crossing breakeven) and the **only** trailing states with a positive net short outcome anywhere in 5.7 years are those mild-weakness buckets, at **+0.004 to +0.022 percent** per trade, which the live veto already allows; shorting into a rally of +3 percent and up is `the worst short state there is`.
- **Table 3 - barrier-geometry control.** Live (target 2.1 / stop 1.9) base **47.52 percent**, short **-1.74 pp / 0.973**, long **+0.28 pp / 0.384**; symmetric +/-2.0 base **49.96**, short **-1.67 / 0.969**, long **+0.30 / 0.378**; symmetric +/-3.0 base **49.99**, short **-2.00 / 0.975**, long **+0.35 / 0.377**; symmetric +/-4.0 base **49.99**, short **-2.53 / 0.990**, long **+0.01 / 0.489**. Short era sign test stays **5 of 6** at every geometry.
- **Table 4 - threshold sweep.** Short contrast negative at every threshold: **-1.60 / 0.972** (2.0), **-1.60 / 0.967** (2.5), **-1.74 / 0.973** (3.0 live), **-1.45 / 0.940** (3.5), **-1.34 / 0.911** (4.0), **-1.15 / 0.848** (5.0). Long contrast **-0.29 / 0.621**, **-0.14 / 0.555**, **+0.28 / 0.383**, **+0.36 / 0.364**, **+0.65 / 0.279**, **+0.19 / 0.443** - no stable sign. **Familywise rotation-null probability for the best of the six short cuts: 0.124** (long side 0.56), so the short veto does not become individually significant by searching thresholds.
- **Table 5 - trailing-window sweep.** Short: **-2.91 pp / 0.999** (12h), **-1.74 / 0.975** (24h live), **-3.15 / 1.000** (48h), **-2.47 / 0.997** (168h). Long: **-1.80 / 0.968**, **+0.28 / 0.385**, **-1.48 / 0.942**, **-1.69 / 0.963** - the source concedes the live gate applies its long veto `at the one trailing horizon where that veto carries the least information`.
- **Section 6.4 - leave-one-coin-out.** Short contrast stays negative for all twenty removals, **-1.87 to -1.62 pp** (least supportive: removing FIL); long stays **+0.18 to +0.46 pp**.
- **Section 6.5 - difference in differences.** Short contrast **-1.74**, long **+0.28**, difference **-2.02 pp**, day-clustered interval **[-4.35, +0.26]**, one-sided probability **0.958**; a linear slope of win rate on trailing return is not significant on either side (the short effect is concentrated in the vetoed rally tail).
- **Section 6.6 - deep cells, recent window, de-overlap.** Deep cells as in Table 1; September 2024 - September 2026 alone: blocked longs **47.01** vs long base **46.20 percent**, blocked shorts **47.55** vs short base **48.89 percent**; de-overlapped sample **329,514** brackets: blocked longs **47.14**, blocked shorts **48.11**, short contrast falls to **-0.27 pp** with interval **[-1.74, +1.22]** and one-sided P **0.633** (below the 0.95 convention), long contrast **+1.01 pp** at P **0.104**.
- **Section 8 - cited live book (109-day window).** Short veto blocked **99** short candidates at mean net **-0.5859 percent** and win rate **35.35 percent**; long veto blocked **136** at **-0.5996 percent** and **33.82 percent**; rotation null validates only the short side at fixed threshold (**P 0.002**) with the long mirror on 7 blocked holdout candidates at **P 0.2625**; day-level probabilities **0.42** and **0.72**. On **20 August 2026** the raw selection rule fired **88 short candidates in one day against a typical 15**; running the deployed book with the short veto rather than without it cut maximum drawdown from **about 71 percent to about 9 percent** (~62 points) and kept it from losing **about 44 percent**. A threshold grid of **66 cells** on those 109 days yields **no cell** clearing the program's significance bar. The companion paper (7353678) is cited for the fact that the deployed book **lost money in live trading**: `The short veto did not make that book profitable. It made it survivable.`
- **Publication context.** SSRN working paper, sole independent researcher, LLM-assisted analysis with author responsibility, no peer review, `0 Citations`, 30 downloads at read time.

### Independently reproduced

`Not independently reproduced.`

What was done instead is limited to provenance and internal-consistency checking of the pinned PDF, which is **not** replication of any empirical result:

- Byte length (697,629), page count (25), SHA-256 (`b0771171...182da`) and text size (54,379 characters / 736 lines) recomputed locally from the pinned file; section/table/figure inventory re-derived (sections 1-10, Tables 1-5, Figures 1-7, 17 reference entries).
- All six Table 1 `net per trade` cells re-derived from their own printed win rates under the printed net geometry (+2.00 / -2.00): -0.1640 vs -0.1641, -0.0812 vs -0.0813, -0.0380 vs -0.0380, -0.1256 vs -0.1254, -0.1664 vs -0.1664, -0.0672 vs -0.0673 (max deviation 0.0002 pp - rounding only).
- Central contrasts re-derived: 47.97 - 49.71 = **-1.74 pp**; 45.90 - 45.62 = **+0.28 pp**; difference-in-differences = **-2.02 pp**.
- Base-rate arithmetic re-derived: 1.9 / (2.1 + 1.9) = **47.5 percent**; 2.1 - 0.1 = **2.00** and -1.9 - 0.1 = **-2.00**; fee-free breakeven 47.5 percent against fee-inclusive breakeven **50.00 percent**.
- Sample arithmetic re-derived: 1,698,988 + 362 = **1,699,350**, resolving rate **99.9787 percent** (printed 99.979); 2021-01-02 -> 2026-09-02 inclusive = **2,070 days** (printed 2,070 trading days) = **5.665 years** (printed 5.7); long-veto fire rate 146,458 / 849,494 = **17.24 percent** (printed 17.2).
- Section 8 short cell re-derived from its printed win rate (35.35 -> -0.5860 against printed -0.5859) while the long cell **fails** to re-derive (33.82 -> -0.6472 against printed -0.5996), which is contradiction #6.
- Whole-document cost-term scan counts re-computed from the extracted text (all zero counts listed under Execution assumptions).

No trading rule was re-run, no market data were re-downloaded, no bootstrap was re-estimated, and no performance or statistical result was reproduced.

### Negative evidence

1. The source's own headline non-claim: `no state at this geometry is profitable after fees` - the study establishes which side of a filter carries information, not that anything makes money.
2. The long veto has the **wrong sign** at the live horizon: +0.28 pp with one-sided P 0.386, correct sign in only 2 of 6 years.
3. Long entries lose in **every** trailing state, 44.4 to 47.3 percent against a 50 percent breakeven; removing the long veto buys `candidate frequency, not edge`.
4. The short contrast's two-sided interval **[-3.52, +0.01] touches zero** - the source itself calls it `supported but marginal, not proven`.
5. **Familywise correction kills individual significance**: across the six-threshold family the rotation-null probability of the best short cut is **0.124**, i.e. a search over these correlated cuts reproduces the sign about 12 percent of the time; the source states it would `rather say so than dress it up`.
6. **The de-overlapped sample breaks the bar**: on 329,514 non-overlapping brackets the short contrast falls to **-0.27 pp at P 0.633**, well below the program's 0.95 convention, so `a good part of the short contrast's apparent significance on the full sample was coming from the shared price paths of overlapping entries`.
7. The robustness cuts are **not independent tests**: thresholds nest inside one another, windows are autocorrelated, leave-one-out panels share 19 of 20 coins, geometries re-price the same paths; only the six calendar years are near-disjoint, and there the short sign is right in 5 of 6 = binomial **0.109**.
8. The clean two-object split is **horizon-conditional**: at 12, 48 and 168 hours the long veto turns negative (-1.5 to -1.8 pp), so the asymmetry reported is specifically the one at the 24 hour horizon the live gate runs on.
9. The study is **unconditional while the live book was conditional**; the source states the unconditional study `cannot speak to the selected book's profitability`, and the Section 8 numbers are cited from an internal record, not re-run.
10. The deployed book that used this veto **lost money in live trading** (cited from companion 7353678); the veto made it survivable, not profitable.
11. On the live 109-day window, **no cell in a grid of 66 thresholds** clears the program's significance bar - `a plateau, not a cliff`.
12. **No economic performance measure exists**: no ROI, no drawdown, no Sharpe, no capital path, by construction; therefore there is nothing here that can be compared to a benchmark.
13. **Cost model is a single flat 0.10 percent round-trip fee**; spread, slippage, impact, latency, order type, fill, margin and liquidation are all absent (`data gap`, term scan zeros) even though the motivating book is leveraged.
14. **Universe is not printed**: only FIL is named, the 20 tickers live in unpublished scripts, so the study cannot be reconstructed from the paper alone; single venue, single asset class of correlated crypto alternatives.
15. **Index construction is itself noisy**: 0.76 pp standard deviation of disagreement between the study index and the live gate index, about 25 percent of scans inside the 2-4 percent band where a hard +/-3 percent decision is partly a coin flip - the implemented rule is softer than the written rule.
16. **Panel and survivorship limits**: the universe is fixed by the 2026 live programme, the panel grows 13 -> 20 coins, early years are thinner, and delisted/never-traded coins are not reported.
17. **Intervals are admittedly too tight**: day clustering does not close the overlap (~1/3 of brackets cross days, longest hold 13 days) - `the intervals should be read as, if anything, a little too tight` (source's own words).
18. **No public code, no data artefact, no archive DOI**: the Data and Code Availability block describes five to seven deterministic scripts and a results ledger but gives **no URL, repository or identifier**, and the coin list is `in the analysis scripts`.
19. **Source quality**: sole-author SSRN working paper, no peer review, 0 citations / 30 downloads at read time, LLM-written analysis code and LLM-assisted prose (disclosed), licence conflict between landing and PDF.
20. **Editorial precision problems** (contradictions #5-#9): a cross-reference error in Sections 3.4 and 9, a Section 8 long-cell that does not reconcile with its own printed win rate, a one-count cell mismatch, a non-closing candidate-count sentence, and three different printings of the same bootstrap probability.
21. **The value claim is deliberately modest**: the source says a veto can be worth keeping even when `the trades it blocks would have lost less than the ones it keeps`, which means the headline is about information content, not about profit per blocked trade - any later framing of this record as a profitable strategy would misstate the source.
22. Adjacent contrary evidence already in this repository: `crypto-perp-risk-control-...-ssrn-7345542-2026-09-28.md` (same author: filters are wrong four times out of five), `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` (same author: a signal that passes a permutation test still lost money in deployment), `crypto-risk-managed-tsmom-crash-state-de-risking-drawdown-control-2026-09-14.md` and `hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12.md` (time-series-momentum risk overlays), `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13.md` (retail-cost falsification on the same venue).

## Falsification plan

Every threshold below is **research-defined** (a Scout-chosen failure rule), not a number from the source; every rule the source does specify is marked source-reported. All tests are research-proposed until executed. **No gate may be rescued by retuning.**

- **F1 - printed-cell reproduction gate (research-defined).** Rebuild the bracket table from 15-minute Binance bars and require all six Table 1 cells, both Table 2 contrasts and the base rates to match the printed values within **0.01 pp**, and the resolved-bracket count within **0.1 percent** of 1,698,988. **Fail** on any larger deviation; action: treat the study as non-reproducible and stop.
- **F2 - de-overlapped significance gate (research-defined).** On the 329,514-style de-overlapped sample (one open trade per coin), require the short blocked-minus-allowed contrast to be negative **and** its day-clustered one-sided probability **>= 0.95**. **Fail** if either misses (the source prints -0.27 pp at 0.633, so this gate is expected to fail as printed - the honest reading is that the effect is exposure-level, not trade-level); action: block any trade-selection claim.
- **F3 - familywise multiplicity gate (research-defined).** Apply Benjamini-Hochberg at **q < 0.10** over the full searched family actually exercised (6 thresholds x 4 windows x 4 geometries x 2 sides = 192 cells) plus the rotation null. **Fail** if the short veto does not survive; action: record the result as a sign-stability observation only.
- **F4 - cross-venue replication gate (research-defined).** Rebuild the chained index and the +/-3 percent / 24 hour veto on at least two further venues (e.g. OKX, Bybit) over the same 2021-2026 window and require the short contrast to keep its sign with **>= 50 percent** of the Binance magnitude in **2 of 3** venues. **Fail** otherwise; action: mark the effect venue-specific.
- **F5 - geometry-control gate (research-defined).** Re-resolve at symmetric +/-2.0, +/-3.0 and +/-4.0 percent barriers (source-reported control) and require the short contrast to stay negative with one-sided probability **>= 0.95** at all three and the base rate to return to 50.00 +/- 0.10 percent. **Fail** if the sign flips or the base rate does not recover; action: attribute the result to barrier geometry.
- **F6 - threshold and window sign-stability gate (research-defined).** Require the short contrast negative at **>= 5 of 6** thresholds (2.0-5.0 percent) and at **>= 3 of 4** windows (12/24/48/168 h), and the long contrast to have no stable sign at the live window. **Fail** if the short sign is confined to the live cell; action: declare the threshold fitted despite the source's pre-registration claim.
- **F7 - index-measurement-noise gate (research-defined).** Inject index noise matching the reported 0.76 pp standard deviation of disagreement (and separately run the live-formula index) and require the short contrast to move by **<= 30 percent** of its printed magnitude. **Fail** beyond that; action: mark the veto as a soft weighting whose threshold is not an operational parameter.
- **F8 - survivorship and listing audit (research-defined).** Rebuild the panel with Binance-delisted perpetuals included where data exist and re-run. **Fail** if the short contrast changes sign or its magnitude falls below **50 percent** of printed; action: mark the result survivorship-dependent.
- **F9 - frozen forward test (research-defined).** Freeze the source's rule verbatim (chained equal-weight index, trailing 24h, +/-3 percent, entry refusal only) and evaluate from **2026-10-01** for 6 months. **Fail** if the forward short contrast is non-negative or its one-sided probability is **< 0.90**; action: retire the mechanism as sample-bound.
- **F10 - tradable-sequencing and cost-ladder gate (`research-proposed`).** Sequence the veto on an independently specified directional candidate generator (one position per coin, next-bar entry, explicit sizing) and run a cost ladder of **0 / 1 / 2 / 5 / 10 / 20 bp per side** plus a half-spread. **Fail** the deployability claim if the vetoed book does not beat the unvetted book on net Sharpe at **5 bp per side**, or if its max drawdown is not reduced by **>= 25 percent**; action: keep the record as measurement only, no candidate-pool entry.
- **F11 - exposure-control gate (research-defined).** On a pre-declared set of correlated-selloff episodes (BTC 24h return <= -5 percent with >= 60 percent of the universe down), require the short veto to cut episode-level max drawdown by **>= 30 percent** while changing mean trade P&L by no more than **0.20 pp**. **Fail** if the drawdown reduction is smaller or the P&L cost is larger; action: the source's own claim (it made the book survivable rather than profitable) collapses in both directions.
- **F12 - long-side removal ablation (research-defined).** Remove the long veto entirely and re-run the oracle book. **Fail** the source's `candidate frequency, not edge` interpretation if any risk metric worsens by **> 10 percent**; action: the long side carries content the paper denies it, and the two-object claim must be rewritten.
- **F13 - placebo rotation gate (research-defined).** 1,000 time-rotations of the veto series preserving rate and serial structure (the source's own rotation null, extended to all cells). **Fail** if the observed short contrast is beaten by **< 5 percent** of rotations on the de-overlapped sample; action: if it is beaten by 5-15 percent (as the source's 0.124 suggests), report only sign stability, never significance.
- **F14 - paper-integrity gate (research-defined).** Reconcile the nine frontmatter contradictions with the source (Section 8 long cell, cross-references, cell counts, candidate-count arithmetic, duplicate bootstrap probabilities). **Fail** if any remains unexplained after a source re-read; action: keep `contested: true`, keep the record research-only, and do not promote it into a candidate pool regardless of F1-F13 outcomes.

Action on any failure: the record stays `research-only` and must not advance to a production candidate; no parameter may be retuned to rescue a failed gate.

## Crypto portability

**direct.**

The evidence is itself crypto: Binance USD-margined perpetual futures, 20 coins, 15-minute and hourly data, 2021-01-02 to 2026-09-02. Nothing has to be ported across asset classes.

Residual portability risks even inside this `direct` setting:

- **Single venue / single asset class.** Everything is Binance crypto alternatives; whether the same asymmetry appears in equity index futures or FX is explicitly `unknown` in the source's own limitations section.
- **Index definition.** The veto reads a cross-sectional index of the traded coins, so its value depends on index membership, weighting and listing rules; on other venues or with different constituents the veto state changes (the source's own live-vs-study index comparison already shows 96-97 percent agreement, not identity).
- **Mark vs index price.** The source uses official bar closes; live gates often use mark or index prices with different snapshots (the paper attributes its residual index disagreement to exactly this), so the threshold crossing time can shift.
- **Leverage and liquidation.** The motivating book is leveraged, but no margin, maintenance-margin or liquidation model exists anywhere in the paper - on perpetuals the veto's exposure-control value is entangled with liquidation risk that is `data gap`.
- **Funding.** Funding is never modelled as cost or income; a book that actually holds positions across funding settlements inherits an 8-hour cash flow this study does not price.
- **24/7 session and candle boundaries.** Hourly entries, 15-minute resolution and no time exits assume continuous trading; maintenance windows, index-price dislocations and gap-throughs at the stop are `data gap`.
- **Listing and delisting churn.** The panel grows 13 -> 20 with real listing dates; crypto perps delist actively, and delisted names are not reported.
- **Capacity / crowding.** A widely copied "do not short into a rally" filter changes the very state it measures; capacity and impact are unmodelled (term scan: zero occurrences).

## Limitations

- `underspecified`: the 20-ticker universe; the exact alignment of the trailing window to the entry bar; the timezone/clock of every series; order type, fill timing, latency and partial-fill handling; the geometric/sizing conventions behind the Section 8 live cells; the code repository, scripts and results ledger (described but never linked).
- `data gap`: spread, slippage, market impact, participation, margin/liquidation, borrow, funding as a cost line, capacity, missing-data policy, delisted-coin history, and any availability lag for the index.
- `not independently reproduced`: every empirical number in this record is source-reported; only printed arithmetic, counts and term scans were re-derived locally.
- `unproven`: transfer of the veto to any other book, venue or asset class; any claim of profitability; the exposure-control benefit outside the single cited 20 August 2026 episode and the 109-day internal record.
- Source-quality limits: SSRN working paper, sole independent researcher, no peer review, no citations, no code or data artefact, licence conflict, LLM-assisted code and prose (fully disclosed by the author), and an internally inconsistent editorial apparatus (nine contradictions recorded above).
- Sample and design limits: one universe, one primary geometry, one asset class; the effect is small and marginal in any single test; the de-overlapped sample removes most of the apparent significance; the intervals are admittedly a little tight; the robustness cuts re-slice one sample.
- Interpretation limit: this record captures a **measurement of an entry filter**, not a strategy. The source explicitly makes no trading recommendation and reports no capital-path metric; reading this record as an alpha strategy would contradict the source. What is captured for research is the falsifiable hypothesis that the two sides of a symmetric trailing-return veto are not the same object.

## Implementation status

`implementation_status: not-implemented`.

No part of this record has been implemented in our research stack. No Binance data were downloaded for this study, no bracket resolver, bootstrap or veto backtest was run, no NautilusTrader / Qlib / Paper / Testnet / Live workflow was touched, and no empirical result was reproduced. What exists locally is only: the pinned PDF, its extracted text, a cost-term word scan and an arithmetic re-derivation of printed cells - all provenance checks.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository means only that a normalised, source-traceable research capture exists. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed any full backtest; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; or approved for live trading. The source's own conclusion - that no state at this geometry is profitable after fees and that the short veto is exposure control rather than a predictor of individual trades - is part of this record and is not overridden by it.

## Related Wiki records

Read-only `kb_search` on the run date, three queries:

1. `trailing return veto entry filter exposure control cryptocurrency perpetual` -> **0 hits**.
2. `stop loss trailing stop momentum crash risk control` -> **6 hits**, all generic-adjacent and none sharing this mechanism: [[quant/ou-first-passage-time-bands-fdr-stability-portfolio-stat-arb-2026-09-12]], [[quant/futures-quad-trend-carry-skew-vov-composite-2026-09-11]], [[quant/crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]], [[quant/dtw-ocp-clustering-pairs-trading-regime-falsification-2026-09-13]], [[quant/frozen-timesfm-hybrid-bilinear-gated-random-forest-residual-2026-09-12]], [[quant/alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]] - returned by the query and verified to exist, but linked only as retrieval hooks, **not** as same-mechanism relatives.
3. `Dashyan backtest-to-live gap risk control durable edge funding carry` -> **0 hits**, so no Wiki page exists for this paper or for any of its five companions; none is fabricated here.

Adjacent **repository** records (not Wiki pages) a future reviewer should read together with this one: `crypto-perp-risk-control-loss-filter-profit-armed-ratchet-market-neutral-funding-carry-ssrn-7345542-2026-09-28.md` (SSRN 7345542, same author, the closest mechanism neighbour), `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` (SSRN 7353678, same author, source of the live-loss fact cited in Section 8), `equity-index-tail-flush-reversion-disjoint-band-familywise-2026-09-27.md` (SSRN 7363482, same author), `tradingview-binance-perpetual-oi-premium-divergence-veto-filter-2026-09-19.md`, `crypto-risk-managed-tsmom-crash-state-de-risking-drawdown-control-2026-09-14.md`, `hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12.md`, `crypto-perpetual-volume-spike-momentum-liquidity-inversion-trailing-exit-falsification-2026-09-13.md`.

## Sources

- Dashyan, A. (2026). *A Symmetric Trend Veto Is Two Different Objects: 5.7 Years of Barrier Outcomes on Twenty Cryptocurrency Perpetuals*. SSRN working paper. Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7418978>; DOI: <https://doi.org/10.2139/ssrn.7418978>. PDF title block: `Aleksandr Dashyan` / `Independent Researcher, Yerevan, Armenia` / `ORCID: 0009-0009-5118-5184` / `alikdashyan1@gmail.com`; landing author line: `Alexandr Dashyan` / `Independent Researcher`. `Date Written: August 25, 2026`; `Posted: 7 Sep 2026`; suggested citation `(August 25, 2026)`; PDF cover `This version: September 2026`; PDF metadata `CreationDate D:20260905233910+04'00'`, `/Creator Microsoft® Word 2024`, `/Producer Microsoft® Word 2024`, `/Author python-docx`. 25 pages. Landing read 2026-09-29 in a browser session after the Cloudflare interstitial cleared, showing `25 Pages`, `0 References`, `0 Citations`, `DOWNLOADS 30`, `ABSTRACT VIEWS 89`, `Open PDF in Browser`, licence `Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International`, and the declaration `no interest, that is my personal research with my personal funds`. Pinned PDF retrieved 2026-09-29 via the landing's `Open PDF in Browser` delivery link, 697,629 bytes, SHA-256 `b07711713ff83b5f4f145466b5ecfb42dc42680eeb35d7dd188da51f400182da`, text extracted with `pypdf 6.16.2` to 54,379 characters, all 25 pages read; no presigned or session-bound URL retained.
- Companion works cited by the source **with identifiers in its own reference list** (Dashyan 2026a-2026e): `10.2139/ssrn.7306538` (*Short-horizon directional non-predictability in cryptocurrency perpetual futures*), `10.2139/ssrn.7338919` (*Adversarial backtest verification*), `10.2139/ssrn.7345542` (*Risk control as the durable edge*), `10.2139/ssrn.7353678` (*A real edge that loses*), `10.2139/ssrn.7363482` (*The tail is the only signal*). The last three are already captured in this repository; the first two are not.
- Methodological references used by the source for its own tests (the 12 non- Dashyan entries, listed as the source lists them): Arnott/Harvey/Markowitz (2019); Bailey/Borwein/Lopez de Prado/Zhu (2014); Bailey & Lopez de Prado (2014); Daniel & Moskowitz (2016); Harvey/Liu/Zhu (2016); Hurst/Ooi/Pedersen (2017); Ilmanen (2011); Lo & MacKinlay (1990); Makarov & Schoar (2020); Moskowitz/Ooi/Pedersen (2012); Politis & Romano (1994); White (2000).
