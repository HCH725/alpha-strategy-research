---
schema: strategy-research-record-v1
title: Equity-Index Tail Flush Reversion at or below -7 Percent under Date-Level Counting, Disjoint Depth Bands and Familywise Correction (SSRN 7363482)
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - equity-indices
  - short-horizon-reversal
  - liquidity-provision
  - event-study
  - multiple-testing
  - negative-evidence
  - crypto-perpetuals
status: research-only
confidence: medium
source_as_of: 2026-08-30
sources:
  - "SSRN abstract_id 7363482, DOI 10.2139/ssrn.7363482; landing page read 2026-09-27 at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7363482"
  - "SSRN PDF retrieved 2026-09-27 through the landing-page 'Open PDF in Browser' link https://papers.ssrn.com/sol3/Delivery.cfm/7363482.pdf?abstractid=7363482&mirid=1&type=2 (redirect to download.ssrn.com/2026/8/28/7363482.pdf); 501052 bytes, 22 pages, SHA-256 33955a1110235ded8f83d4409385b33ac326d568e61b3140e2c61b673da97494"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Author name is printed two ways: the SSRN landing page author line and suggested citation read 'Alexandr Dashyan, Independent Researcher', while the PDF title block reads 'Aleksandr Dashyan, Independent Researcher, Yerevan, Armenia' with correspondence alikdashyan1@gmail.com. Both spellings are recorded unreconciled."
  - "Rights statement conflicts: the SSRN landing page displays a Creative Commons badge stating 'This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License', while the PDF front matter states 'Copyright 2026 Aleksandr Dashyan. All rights reserved. This paper is circulated for discussion and comment only; it may not be reproduced, distributed, quoted at length, or used, in whole or in part, without the author's prior written permission.' This record therefore normalises only claims, printed values and section references."
  - "Reference count conflicts: the SSRN landing page shows a '0 References' section heading, while the PDF reference list contains 24 numbered entries [1] to [24]. The landing '0 Citations' heading is consistent with the absence of citations."
  - "Version identity is printed four ways with no version number: SSRN 'Date Written: July 01, 2026', SSRN suggested citation dated 'July 01, 2026', PDF cover 'Working paper. Preliminary. Comments welcome. This version: August 2026', and SSRN 'Posted: 30 Aug 2026'. Recorded unreconciled."
---

# Equity-Index Tail Flush Reversion at or below -7 Percent under Date-Level Counting, Disjoint Depth Bands and Familywise Correction (SSRN 7363482)

## Provenance

**Paper identity.** Dashyan, Alexandr (SSRN author line) / Dashyan, Aleksandr (PDF title block), *The Tail Is the Only Signal: Flush Reversion in Equity Indices and Crypto Perpetual Futures*, with the PDF subtitle *Why pooled event studies overstate short horizon reversal, and what survives when they are corrected*. SSRN abstract_id `7363482`, DOI `10.2139/ssrn.7363482`. Landing page read 2026-09-27: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7363482 (22 Pages; Posted: 30 Aug 2026; Date Written: July 01, 2026; author `Alexandr Dashyan`, Independent Researcher; CC BY-NC-ND 4.0 badge; `0 References`, `0 Citations`; Paper statistics at read time: 80 DOWNLOADS, 162 ABSTRACT VIEWS).

**Pinned primary text.** The full 22-page PDF was retrieved 2026-09-27 through the landing-page delivery link (`https://papers.ssrn.com/sol3/Delivery.cfm/7363482.pdf?abstractid=7363482&mirid=1&type=2`, which redirects to a presigned `download.ssrn.com/2026/8/28/7363482.pdf` object), saved as 501052 bytes / 22 pages, SHA-256 `33955a1110235ded8f83d4409385b33ac326d568e61b3140e2c61b673da97494`, and text-extracted page by page with pypdf 6.16.2 (48782 characters, every page read end to end). Every quantitative field in this record was taken from that pinned text, not from any secondary summary.

**Status, dates, identifiers.** PDF front matter: `Working paper. Preliminary. Comments welcome. This version: August 2026.` JEL classification G14, G12, G11, C12, C58. Keywords: short horizon reversal, event study, cross sectional dependence, liquidity provision, multiple testing, familywise error, stationary bootstrap, cryptocurrency perpetual futures, liquidation cascades, negative results. Author affiliation block: Independent Researcher, Yerevan, Armenia; correspondence `alikdashyan1@gmail.com`. The landing page carries no journal, no issue and no peer-review statement, so peer-review status is `not stated in source`; publication status is SSRN working-paper preprint only.

**AI disclosure (source-reported).** The PDF's Author Contributions and Use of AI Tools section states that research questions, design, hypotheses, methodological choices and interpretation are the author's own; all software implementation (event-study harness, bootstrap and familywise corrections, placebo and decomposition tests, account simulator, adversarial verification harness, figures) was written in Python with Claude (Anthropic) as a coding assistant under the author's direction; the verification process that found the block-bootstrap miscalibration, the nested-threshold problem and the missing multiplicity control was itself run as a multi-agent process using the same tool; Claude is a software tool and not an author; the author is solely responsible for content, claims and errors.

**Data and code provenance (source-reported, Data and Code Availability section).** Equity analysis described as fully reproducible: daily open and close series from a "public vendor chart API" (vendor unnamed) for four indices and 28 single names, plus the 13-week Treasury bill series; a single deterministic script with a fixed random seed is said to produce every equity number, table and figure, and a second script produces the Section 4 calibration evidence. Scripts, the numeric ledger and the verification transcripts are `available from the author on reasonable request` subject to third-party data terms, so there is no public repository and no immutable commit - code availability is `not stated in source` beyond on-request. The Section 7 crypto results are explicitly `cited from a dated internal record of the research program rather than recomputed for this paper`, with only the bracket-geometry retest surviving in the repository.

**Discovery provenance.** Search-engine and aggregator results (including an Exa listing and an alphainacademia.com recap) were used only to locate the SSRN identity; no rule, number or claim in this record comes from them.

## Economic mechanism

### Source-reported

- The paper frames buying after a large single-day decline as one of the oldest short-horizon ideas: prices have moved a long way in a few hours, someone was probably forced to sell, and the counterparty is paid to supply liquidity when it is scarcest (Section 1).
- The mechanism the source favours is liquidity provision rather than behavioural error, anchored in Lehmann (1990), Jegadeesh (1990), Lo and MacKinlay (1990), Grossman and Miller (1988), Campbell Grossman and Wang (1993), Nagel (2012) "Evaporating liquidity", Hendershott and Menkveld (2014), and Hameed Kang and Viswanathan (2010), who show liquidity withdrawing specifically after negative market returns and intensifying when funding is tight (Section 2).
- The paper's own headline contribution is methodological, not economic: pooled event studies overstate short-horizon reversal because large declines cluster on the same calendar dates, so instrument-day pooling counts one market-wide shock many times. Three further corrections are applied - disjoint rather than nested depth thresholds, a familywise max-statistic correction across the tested depths, and a calibrated bootstrap that refuses block configurations with fewer than 20 blocks (Sections 3 and 4).
- For crypto perpetual futures the source argues the two events are not the same event: a perpetual-futures decline mechanically triggers automatic liquidation by an engine that does not care about price, so the cascade is not a temporary imbalance awaiting an intermediary (Section 8), citing Cheng, Deng, Wang and Yu (2021) for daily forced liquidations of 3.51 percent of outstanding long open interest and 1.89 percent of short on positions averaging roughly sixty times leverage, plus Brunnermeier and Pedersen (2009).

### Research interpretation

- **Hypothesis (falsifiable form):** an extreme, market-wide, single-session equity-index decline (close-to-close at or below -7 percent) creates a transient liquidity-provision concession that is paid back in the following session, and the payoff is concentrated in the regular session rather than in the overnight gap, so it is capturable by a participant who buys the next open.
- **Role of each component (hybrid structure):**
  - Regime / trigger: a crude price-only tail event - daily close-to-close return at or below -7 percent on any of four US indices (no volatility, volume, positioning or news filter; deliberately crude by design).
  - Entry: flush close (primary design) or next session open (implementable variant).
  - Exit: the next session close, one-session holding period.
  - Risk / sizing: capital split equally across that date's signals, capped at 20 percent per position and ninety five percent in aggregate; idle capital earns the 13-week Treasury bill rate; unlevered; flat 20 bp round-trip cost.
  - Evidence discipline (part of the tested object, not alpha): date-level observations, disjoint depth bands, familywise max-statistic correction across bands, episode clustering at 60 days.
- The record treats the counting protocol as a **replication requirement**, not as alpha: if a replication pools instrument-days or uses nested cuts, it is testing a different object.
- No claim is made that the mechanism is established. The source's own summary is that the surviving effect is real but economically negligible, and that the transportable result is the counting correction.

## Signal

All rules below are `source-reported` unless explicitly marked `research-proposed`.

- **Formation timestamp:** a flush is defined on the daily close-to-close return of each of the four indices; the event is knowable at the close of day `t` (Sections 3). Timezone and session convention are `not stated in source`; US equity regular sessions are implied by the references to "the closing print", "the opening print" and "the next session" (`data gap`).
- **Lookback:** none. The event uses only day `t` close versus day `t-1` close. Warm-up: none stated. A separate robustness check (Section 6) standardises severity using the prior 250 days only, explicitly so that no future information enters.
- **Event definition:** daily close-to-close return at or below a threshold. Three thresholds are tested at 3, 5 and 7 percent and are treated as **disjoint bands**, not nested cuts: band 1 = declines between -3 and -5 percent, band 2 = between -5 and -7 percent, band 3 = at or below -7 percent (Section 3, called "the single most consequential design choice in the paper").
- **Long entry:** buy the flush close (primary design) and sell the next close, with a 20 basis point round-trip cost (Section 3). Implementable variant: buy the next open instead of the flush close (Sections 5 and 9).
- **Short entry:** none. The design is long-only; no short leg, no borrow (`zero occurrences` of "borrow" and "short sale" in the pinned text).
- **Exit:** sell at the next session close; single-session holding period; no stop, no take-profit, no re-entry rule inside the event, no overlapping-position handling beyond the equal-split-and-cap sizing (`research-proposed` for anything finer).
- **Parameters:** thresholds `-3/-5/-7 percent` (fixed, chosen ex ante as a deliberately crude test); band construction disjoint; episode clustering window `60 days`; per-position cap `20 percent`; aggregate cap `ninety five percent`; round-trip cost `20 bp`; bootstrap `ten thousand` resamples on date-level observations; block bootstrap refused when fewer than 20 blocks; familywise max-statistic correction across the three bands (all `source-reported`).
- **Instrument choice:** `underspecified`. The source trades "the indices" through an unnamed instrument; no ETF, future, index fund or total-return vehicle is named anywhere in the 22 pages (`data gap`). Choosing a tradable proxy (index ETF or equity index future) is `research-proposed`.
- **Order type / timing of the equity orders:** `not stated in source` for the close entry (`data gap`); the next-open variant implies a market-on-open execution, which is `research-proposed` wording for the source's "waits for the market to open and buys there".
- **Sizing logic (source-reported):** on a flush date, capital is spread equally across that date's signals, capped at 20 percent per position and ninety five percent in aggregate; on every other day the account earns the Treasury bill rate; the account simulation walks the entire fixed calendar rather than only event dates, so the annualisation window cannot be chosen by the signal and idle capital is not free (Section 3).

## Required data

- **Instruments:** four US indices with daily open and close prices - S&P 500 from 1950, Nasdaq Composite from 1971, Russell 2000 from 1987, Dow Jones Industrial Average from 1992 - plus a panel of 28 large-capitalisation single names (individual names `not stated in source`, `data gap`) (Section 3).
- **Calendar:** the union of index trading days, a fixed calendar of 19,276 sessions from 1950-01-04 to 2026-08-17, a span of 76.6 years (Section 3).
- **Risk-free / idle cash:** the 13-week Treasury bill series, used both to accrue idle cash and to compute excess returns (Section 3).
- **Venue / vendor:** a "public vendor chart API" (`Section 3` and Data and Code Availability); the vendor, symbol names, split and dividend adjustment policy, and any revision or back-adjustment practice are `not stated in source` (`data gap`).
- **Return type:** price series, not total-return series - the source states this understats reversion by one day of dividend, "an amount too small to change any conclusion" (Section 6).
- **Timeframe:** daily bars; intraday decomposition uses the opening print versus the close of the next session (Section 5, Figure 6). Timezone, DST handling, halts and early closes: `not stated in source` (`data gap`).
- **Point-in-time:** no point-in-time or revision-audit statement exists in the source (`data gap`). The one explicitly point-in-time construction is the 250-day trailing standardisation in Section 6.
- **Missing data:** `not stated in source`. Survivorship is acknowledged only for the single-name panel - delisted securities are `not retrievable from the data source used here` (Section 6).
- **Crypto side (Section 7):** twenty US dollar margined perpetual contracts on an unnamed major venue; one-minute prices against fixed brackets; sample 2021 to 2026; 87,870 events (a pooled instrument-day count, without the counting correction applied to the equity panels); a native liquidation feed exists only from 2026-06-03, giving an honest native span of about 63 days with roughly 16 flush clusters, with every earlier event identified from price and volume.

## Execution assumptions

- **Signal-to-order timing:** flush known at the day-`t` close; entry at that close (primary) or at the next open (implementable variant) (`source-reported`).
- **Order type:** `not stated in source` for equity entries (`data gap`). The only order-type discussion in the paper is on the crypto side, where a price-improved limit entry is shown to be adverse selection in a falling market and replacing it with a market order moves the baseline from -21.7 percent to +17.6 percent at an unchanged win rate (Section 7, `source-reported`).
- **Fill model, partial fills, queue, latency:** `not stated in source`; word scan of the pinned PDF returns `zero occurrences` of "latency" and a single "fill" occurrence that describes crypto limit-order selection, so every one of these is `data gap`, never zero.
- **Fees:** one flat `20 bp round trip` (`source-reported`, Sections 3 and 9 and the Table 3 caption, "unlevered, twenty basis points round trip, twenty percent per position, idle cash earning the Treasury bill rate"). Commission, exchange, regulatory and clearing fees are not itemised; the word "commission" has `zero occurrences` (`data gap`).
- **Spread, slippage, market impact:** `data gap`. The pinned text has `zero occurrences` of "slippage", "bid-ask" and "market impact"; all three occurrences of "spread" are prose ("capital is spread equally", "a few percent spread across", "spread over a recovery window") and are not cost terms.
- **Capacity:** discussed qualitatively only - the source calls it "a capacity and frequency constraint, not a quality constraint" that "cannot be relieved by leverage without reintroducing exactly the tail risk the strategy is trying to harvest" (Section 9). There is no ADV, participation or dollar-volume model (`data gap`).
- **Leverage / margin:** account is `unlevered` (`source-reported`); leverage appears only as the source's own rejection of it and in crypto background prose.
- **Borrow / shorting:** not applicable - long-only design, no short leg (`source-reported`).
- **Funding:** no funding leg in the equity account; funding appears only as liquidity-condition background and as crypto liquidation-cascade mechanics (`not applicable` to the equity signal, `data gap` for any crypto port).
- **Cash / financing:** idle capital accrues the 13-week Treasury bill rate (`source-reported`).
- **Rebalance / holding:** one session, no rebalance, no compounding decision beyond the account walk (`source-reported`).
- **Failure handling, halted sessions, gap risk:** `not stated in source` (`data gap`); the source itself warns that reported drawdowns are small because the strategy is almost never exposed, so they describe the account rather than the risk of the trade (Section 9).

## Evidence

### Source-reported

All figures below are third-party claims from the pinned PDF, marked `source-reported`, none independently verified. Provenance is given as the printed table or section. Rounding-level restatements in the abstract are noted where they differ from the body.

- **Table 1 (pooled versus date-level statistics, disjoint bands):** Indices -3% to -5%: 535 events, 322 dates, pooled t 0.22, date-level t 0.61, uncorrected bootstrap p 0.271. Indices -5% to -7%: 88 / 55, 0.73 / 0.40, p 0.327. Indices at or below -7%: 50 / 25, pooled t 5.55, date-level t 3.38, uncorrected p 0.0005. Singles -3% to -5%: 11,556 / 5,231, 0.87 / 1.11, p 0.138. Singles -5% to -7%: 2,545 / 1,580, 1.97 / 1.21, p 0.117. Singles at or below -7%: 1,361 / 791, pooled t 6.76, date-level t 1.68, uncorrected p 0.045. Table 1 caption states the index tail band's 0.0005 becomes 0.0058 familywise and no other band survives.
- **Table 2 (index panel, 1950 to 2026, disjoint bands):** -3% to -5%: 535 events, 322 dates, 65 episodes, mean next session +0.089%, date t 0.61, episode t 0.54, familywise p 0.631. -5% to -7%: 88 / 55 / 22, +0.243%, 0.40, -0.04, 0.733. At or below -7%: 50 / 25 / 10, **+3.075%**, date t 3.38, episode t 3.89, **familywise p 0.0058**, bootstrap interval 1.335 to 4.835 percent (Section 5), with 72 percent of those dates followed by a positive session (Table 3 prints the day win rate as 72.0%).
- **Abstract restatement (rounding-consistent):** mean next session 3.08 percent, familywise p 0.006, bootstrap interval 1.34 to 4.84 percent, 50 events on 25 dates clustering into 10 episodes since 1950.
- **Placebo horizon (Section 5, Figure 3):** in the tail band the next session returns 3.075 percent while each of the following nine averages 0.013 percent, against an unconditional daily mean of about 0.03 percent - a ratio of 234 to one; in the shallowest band the same ratio is 0.8, i.e. the next session is slightly worse than the placebo days.
- **Robustness - excluding 2008 and 2020 (Section 5):** 20 events on 13 dates in 8 episodes, mean 3.009 percent, date-level t 2.15, episode-level t 3.47, bootstrap p 0.0095. A wider exclusion (1997, 1998, 2000-2002, 2008, 2009, 2011, 2020, 2022) leaves only 3 dates, mean 1.064 percent, bootstrap p 0.402, which the source reports as a bound rather than a test.
- **Gap versus session decomposition (Section 5, Figure 6):** overnight gap contributes 0.510 percent and the regular session 2.567 percent, so 83 percent of the move occurs after the opening print; the two printed components sum to 3.077 against the stated 3.075 percent mean (rounding). Buying the next open instead of the flush close costs 23 percent of the per-active-day return (1.349 percent falling to 1.032 percent) but almost nothing compounded (4.26 percent a year falling to 4.16 percent).
- **Bootstrap calibration evidence (Section 4):** against genuine independent nulls at the sample sizes used, a stationary bootstrap with mean block 10 rejects a true null 13.3 percent of the time at 22 observations and 10.6 percent at 58, against a nominal 5 percent; the independent bootstrap that replaced it rejects at 6.5 and 5.6 percent. First-order autocorrelation of the date-level series is 0.062, -0.137 and -0.112 from shallowest band to tail; median gap between consecutive events is 10, 24 and 14 days by band while the largest gaps run to more than ten years. The source states its own first pass produced a p value roughly two orders of magnitude too small.
- **Standardised-threshold check (Section 6):** at 3 trailing standard deviations both panels are flat (date-level t 0.42 indices, 0.78 singles); at 4 the single names turn negative (-0.80 against 0.69); at 6 the index panel returns 2.784 percent with date-level t 4.29 while the single-name panel returns -0.618 percent with t -1.78 and wins on only 37.5 percent of its dates.
- **Single-name panel (Sections 4 and 6):** 1,361 declines at or below -7 percent collapse to 791 distinct dates; pooled t 6.76 becomes date-level 1.68 (uncorrected p 0.045). The source calls this a failed replication in the better-powered sample and notes the familywise correction was computed for the index panel and is quoted for singles as an expectation, not a measured result.
- **Table 3 (account cards over all 19,276 sessions, unlevered, 20 bp round trip, 20 percent per position, idle cash at the bill rate):** band -3% to -5%: 322 active days, capital time 0.555%, day win rate 49.7%, mean per active day -0.050%, CAGR +3.53%, maxDD 13.2%, Sharpe -0.14. Band -5% to -7%: 55, 0.091%, 54.5%, +0.056%, +3.84%, 5.5%, 0.02. Band at or below -7%: 25, **0.052%**, 72.0%, **+1.349%**, **CAGR +4.26%**, maxDD 2.7%, **Sharpe 0.31**. Treasury bills: +3.82%, 0.0% drawdown. S&P 500 price only 1950-2026: +8.33%, maxDD 56.8%, Sharpe 0.35. S&P 500 total return 1988-2026: +11.53%, maxDD 55.3%, Sharpe 0.54. Table 3 caption adds that counting active days instead of capital time would overstate exposure by a factor of about three.
- **Economics (abstract and Section 9):** an account trading the surviving tail signal deploys 0.05 percent of its capital time (Table 3: 0.052 percent) and beats Treasury bills by 0.44 points a year; the source's own words are "a real effect that cannot carry a portfolio" and "a Treasury bill account with an overlay that fires once every seven and a half years".
- **Crypto perpetual results (Section 7, cited from an earlier dated internal record of the same research program):** twenty USD-margined perpetuals, one-minute prices against fixed brackets, 2021 to 2026, 87,870 pooled events. Edge net of market beta is negative in every regime - -0.118 bull, -0.100 bear, -0.087 range-bound - and the estimated probability that the de-beta edge is positive rounds to zero in every year (to be read as below one percent, not an exact zero). Realised win rate 47.9 percent, which the source says sits below the geometry's breakeven (the breakeven value itself is `not printed` for this baseline, `data gap`; a breakeven near 49.8 percent is printed for the directional checks). A machine-learning meta labeler trained on the full state snapshot with purged walk-forward validation reaches out-of-sample AUC 0.493 to 0.506; the most confident trades win 51.4 percent against an average of 54.4 percent, and no confidence bucket reaches 60 percent.
- **Crypto escape hatches closed (Section 7):** inverting the rule loses too (directional win rates 48.6 and 48.4 percent against breakeven near 49.8 percent); changing bracket geometry leaves net return per trade identical at -0.09 percent across three take-profit / stop-loss configurations; the single large improvement was execution - a price-improved limit entry was adverse selection and replacing it with a market order moved the baseline from -21.7 percent to +17.6 percent at an unchanged win rate.
- **Landing-page statistics at read time 2026-09-27:** 80 downloads, 162 abstract views, 0 citations, 0 references heading (versus 24 references in the PDF; see frontmatter contradictions).

### Independently reproduced

not independently reproduced

No rerun of the event study, bootstrap, familywise correction or account simulation was performed in this run. The source's own scripts are only `available from the author on reasonable request`, no public repository or commit exists, and the vendor is unnamed, so an independent reproduction would require first recovering the exact data pipeline.

### Negative evidence

Source-reported unless marked otherwise; numbered contiguously.

1. **Single-name panel fails (Table 1, Section 4):** pooled t 6.76 falls to date-level 1.68, uncorrected p 0.045, and does not survive familywise correction, in the sample with far more distinct dates (791 versus 25) - a failed replication in the better-powered sample.
2. **Shallower index bands are empty (Table 2):** +0.089 percent with familywise p 0.631, and +0.243 percent with familywise p 0.733.
3. **Nesting artifact (Section 4):** under conventional nested cuts the tail contaminates every shallower threshold and three correlated views of one result present as three confirmations; under disjoint bands the shallow date-level statistics are 0.61 and 0.40, "nothing at all".
4. **Multiplicity cost (Table 1 caption, Table 2):** the index tail's uncorrected p 0.0005 becomes familywise 0.0058, and no other band survives.
5. **The natural dependent-data tool is miscalibrated here (Section 4):** stationary bootstrap with mean block 10 rejects a true null 13.3 percent at n=22 and 10.6 percent at n=58 against a 5 percent nominal; the source's own first pass manufactured a p value about two orders of magnitude too small.
6. **Extreme rarity and concentration (Table 2, Section 5):** 25 dates in 10 episodes across 76 years, roughly one episode every 7.5 years; the confidence interval 1.335 to 4.835 percent is wide.
7. **Crisis-year fragility (Section 5):** excluding 2008 and 2020 leaves 20 events on 13 dates (mean 3.009 percent, p 0.0095), but a wider exclusion leaves only 3 dates (mean 1.064 percent, p 0.402); the source also reports, from an earlier analysis in the same program, that the per-event edge is flat across ex-ante volatility regimes, so what depends on crisis years is the significance of the pooled result, not the effect.
8. **Placebo horizon shows the effect is one session only (Section 5):** the following nine sessions average 0.013 percent each, below the unconditional mean - supportive of the tail claim, but it also means there is no recovery window to trade, and in the shallow band the next session underperforms its own placebo days (ratio 0.8).
9. **Economics are the binding constraint (Table 3, Section 9):** tail CAGR +4.26 percent versus bills +3.82 percent, Sharpe 0.31, capital time 0.052 percent, deployable about 25 times in 76 years; the shallowest band returns +3.53 percent with Sharpe -0.14, below cash outright.
10. **Opportunity cost versus simply owning equity (Table 3):** S&P 500 price-only +8.33 percent (Sharpe 0.35) and total return +11.53 percent (Sharpe 0.54) at 100 percent capital time versus the tail band's 0.052 percent capital time; the source states neither equity row is an alternative at equal risk.
11. **Crypto perpetuals are negative in every regime (Section 7):** de-beta edge -0.118 bull, -0.100 bear, -0.087 range-bound, with the probability of a positive edge below one percent in every year of the six-year sample.
12. **Crypto predictive models find nothing (Section 7):** win rate 47.9 percent below the geometry's breakeven; meta-labeler purged walk-forward AUC 0.493 to 0.506; no confidence bucket at or above 60 percent (51.4 percent for the most confident trades against a 54.4 percent average).
13. **Inversion fails as well (Section 7):** continuation win rates 48.6 and 48.4 percent against breakeven near 49.8 percent - described as a coin flip paying fees in both directions rather than a sign-flipped signal.
14. **Bracket geometry does not matter (Section 7):** net return per trade identical at -0.09 percent across three take-profit / stop-loss configurations.
15. **Execution dominates prediction on the crypto side (Section 7):** price-improved limit entries were adverse selection; a market order moved the baseline from -21.7 percent to +17.6 percent at an unchanged win rate - a finding about order types, not reversion.
16. **Crypto event identification is weak (Sections 7 and 10):** pre-2026 events are identified from price and volume because no native liquidation feed existed before 2026-06-03 (about 63 native days, roughly 16 flush clusters); the 87,870 count is a pooled instrument-day count to which the paper's own counting correction has not been applied.
17. **Sample asymmetry across asset classes (Section 10):** 76.6 years of equities against 6 years of crypto, so the crypto null is a strong statement about a short period rather than a weak statement about a long one.
18. **Single-name survivorship bias (Sections 6 and 10):** the panel contains names that still trade today; delisted securities are not retrievable from the data source used, so the direction of the bias is toward finding reversion, making the reported null more likely conservative than generous - and it is a structural argument, not a measurement.
19. **Price rather than total-return series (Section 6):** understates realised reversion by one day of dividend.
20. **Standardised thresholds widen the asymmetry instead of dissolving it (Section 6):** at 4 trailing standard deviations single names are negative (-0.80 against index 0.69) and at 6 they are -0.618 percent with t -1.78 and a 37.5 percent win rate.
21. **No independent reproduction is possible from public artefacts (Data and Code Availability):** scripts are on request only, and for the crypto half only the bracket-geometry retest survives, so those figures are "reported results with a documented provenance rather than independently reproducible artifacts".
22. **Cost model is one flat number (Sections 3 and 9 plus word scan of the pinned text):** only a 20 bp round trip; `zero occurrences` of slippage, bid-ask, market impact, commission, latency, turnover and borrow; the single "capacity" occurrence is a qualitative sentence with no ADV, participation or dollar-volume model.
23. **Design breadth is deliberately narrow (Section 10):** a single crude event definition and a one-session horizon, chosen to avoid specification search, which leaves open whether a more carefully constructed signal would do better - and equally leaves the reported result exposed to being an artefact of that one cut.
24. **Exposure statistics describe the account, not the trade (Section 9):** drawdowns are small because the strategy is almost never exposed; "a single tail event that failed to revert would move them substantially".
25. **The source's own bottom line (abstract, Section 11):** "a good idea that mostly does not work", "a real effect that cannot carry a portfolio", and for crypto perpetuals "nothing at all".

None identified beyond the reviewed source for replications by third parties; absence is not evidence of no negative result - the landing page shows 0 citations at read time 2026-09-27, so no external replication of this specific paper exists in the cited record.

## Falsification plan

All thresholds below are `research-defined falsification thresholds`, not source-reported. Data for all tests: the pinned PDF (SHA-256 `33955a1110235ded8f83d4409385b33ac326d568e61b3140e2c61b673da97494`), the source's deterministic equity script if and only if the author releases it, and an independently sourced daily OHLC calendar for the four indices. Forward collection window starts `2026-10-01` (`research-proposed` date). Action on failure for every test: the record stays `research-only` and no production candidate-pool entry is proposed.

- **F1 - Frozen forward replication.** Collect every future close-to-close decline at or below -7 percent on the four indices from 2026-10-01 onward, entry at the next open, all rules frozen. Failure rule: the forward mean next-session return is at or below `0.0 percent`, or fewer than `3` new tail dates exist by 2031-12-31 (under-identification - the record then cannot be upgraded on forward evidence).
- **F2 - Counting reproduction gate.** Rebuild Table 1 and Table 2 date-level statistics on the same calendar. Failure rule: any headline cell differs from the pinned PDF by more than `0.10` in t-statistic or `0.10` percentage points in mean next-session return.
- **F3 - Cost ladder.** Re-run the account at round-trip costs `{20, 50, 100, 200}` bp, adding an explicit spread and market-impact model for the chosen tradable proxy. Failure rule: the tail band's excess over bills (`0.44` pp) is erased at `100` bp, or its Sharpe falls below `0`.
- **F4 - Implementable-entry gate.** Execute the next-open variant with market-on-open orders. Failure rule: reproduced mean per active day below `1.032` percent, or account CAGR at or below the `3.82` percent bill CAGR.
- **F5 - Placebo-horizon replication.** Compare the next session with the mean of sessions t+2 to t+10. Failure rule: next-session mean is not larger than the placebo mean (ratio at or below `1.0`), which would collapse the effect into general post-crash drift.
- **F6 - Depth sensitivity with multiplicity.** Re-run thresholds `{6, 7, 8}` percent and standardised `{4, 5, 6}` trailing-SD cuts under the familywise max-statistic correction. Failure rule: familywise p at or above `0.05` at both neighbouring cuts, i.e. the effect exists only at exactly -7 percent.
- **F7 - Episode-level inference.** Re-run inference on the 10 episodes and perform leave-one-episode-out. Failure rule: episode-level t below `2.0`, or any single episode's removal drives the mean to `0` or below.
- **F8 - Crisis-year leave-out.** Remove the three largest crisis years in the sample. Failure rule: surviving mean below `1.0` percent or bootstrap p at or above `0.05` (the source's own wider exclusion already prints 1.064 percent with p 0.402, so this test is expected to be decisive).
- **F9 - Cross-market extension.** Apply the identical protocol to four additional indices (`research-proposed` universes: STOXX 600, Nikkei 225, CSI 300, Hang Seng). Failure rule: fewer than `2` of `4` show a positive tail-band mean with familywise p below `0.05`.
- **F10 - Total-return and point-in-time rebuild.** Rebuild on total-return index series and an audited point-in-time calendar. Failure rule: tail mean falls below `2.5` percent or changes sign.
- **F11 - Data-vendor audit.** Identify vendor and symbols, then compare against a second independent vendor. Failure rule: price differences exceeding `0.10` percent on more than `1.0` percent of sessions, or any calendar mismatch after 1950.
- **F12 - Multiplicity over this record's own search.** Apply Benjamini-Hochberg at `q < 0.10` across `{3 bands x 4 entry variants x 3 universes x 2 vendors}`. Failure rule: no cell survives.
- **F13 - Crypto port test.** Replicate the source's crypto analogue with date-level counting correction and native liquidation data where available. Failure rule for this record's portability claim: a positive crypto tail-band edge with familywise p below `0.05`, which would contradict the source-reported uniform crypto null and force this record's crypto section to be revised.
- **F14 - Reproducibility gate.** Obtain the author's scripts and ledger. Failure rule: the four equity tables and Table 3 cannot be reproduced within `0.05` percentage points in means and `0.10` in t-statistics.

## Crypto portability

`unproven`

This is a portability judgement against a source that tested crypto itself and found nothing, so the label is `unproven` with source-reported evidence pointing against a port - a stronger statement than merely untested:

- The source's own crypto test (Section 7) reports the edge net of market beta negative in every regime and every year of a six-year sample, win rate below breakeven, meta-labeler AUC at a coin flip, and no escape through inversion, bracket geometry or confidence bucketting. Any crypto implementation of "flush reversion" must therefore start from a null, not from the equity result.
- **Session structure.** The equity signal is defined on a closing print and an opening print with an overnight gap decomposition (0.510 percent gap versus 2.567 percent session). Crypto trades 24/7 and has no close or open, so "next session" must be re-specified (funding-settlement epochs, daily 00:00 UTC candles, or venue-specific marks) - `research-proposed`, and it changes the label being tested.
- **Mechanism.** In perpetuals a large decline mechanically triggers automatic liquidation by an engine that does not care about price (Section 8), so the cascade is not a temporary imbalance awaiting an intermediary; the source explicitly predicts no payment for supplying liquidity in that setting and observes it.
- **Index proxies.** There is no 76-year crypto index history and no four-instrument cross-section of comparable depth; a BTC or top-cap index proxy would face survivorship, listing and reconstitution issues the source never models.
- **Funding, mark and margin.** Any hedged or levered crypto expression adds funding, mark/index divergence, margin and liquidation/ADL rules - none of which appear in the source (`data gap`).
- **Venue fragmentation and data.** The source's crypto venue is unnamed and its pre-2026 events are price/volume inferred; crypto candle boundaries, timezone conventions and native liquidation feeds differ by venue.
- Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: the tradable instrument behind each index (ETF, future or fund), equity order type and execution timestamp, timezone and DST convention, handling of halts and early closes, missing-data policy, and the identity of the 28 single names.
- `data gap`: named data vendor, split/dividend adjustment and revision practice, point-in-time audit, exchange/commission/regulatory fees, spread, slippage, market impact, latency, partial fills, participation/ADV capacity, and any funding or borrow treatment.
- `not stated in source`: peer-review or journal status, public code or data location (scripts are on request only), statistical inference beyond the printed bootstrap and familywise procedure, and the breakeven win rate for the crypto baseline geometry.
- `not independently reproduced`: every performance figure in this record; no rerun was possible without the author's scripts and vendor identity.
- Source-internal restatements that differ only by rounding are recorded rather than silently normalised: abstract familywise p `0.006` versus Table 2 `0.0058`; abstract capital time `0.05 percent` versus Table 3 `0.052 percent`; abstract bootstrap interval `1.34 to 4.84` versus Section 5 `1.335 to 4.835`; gap plus session `0.510 + 2.567 = 3.077` versus the stated `3.075` percent mean. Four substantive contradictions (author spelling, licence, reference count, version dates) are listed in the frontmatter and are not reconciled.
- Identification: single-name survivorship bias, price-only series, and crypto events inferred from price and volume before 2026-06-03 all remain open.
- Statistical: 25 dates in 10 episodes is a small effective sample; the source concedes that no procedure can manufacture independent evidence that history did not supply, and that a reader concluding only "something happens after -7 percent index declines and its size is poorly determined" is reading it correctly.
- Publication-bias and selection concerns: the paper reports its own failed first pass (anti-conservative bootstrap, nested thresholds, missing multiplicity control) rather than the flattering version, which is a positive disclosure practice, but the surviving result is still one selected tail cut out of several tested depths, panels and asset classes.
- Capacity: treated qualitatively only; the honest exposure unit (0.052 percent capital time) shows the effect cannot carry a portfolio, and leverage is explicitly rejected by the source as re-importing the tail risk being harvested.
- This record captures a narrow research hypothesis plus a large body of decisive negative evidence; it does not assert that the mechanism is absent, only that the source's own evidence supports one rare, small, hard-to-deploy equity effect and nothing in crypto perpetuals.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack. No Qlib full backtest, no NautilusTrader change, no Paper, Testnet or Live run, and no production card has been produced. The record exists only as normalized research material in the public staging pool.

## Adoption boundary

Presence of this record in this repository does not mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

Verified pages returned by `kb_search` at write time (no page is fabricated):

- [[quant/fourier-residue-sign-magnitude-equity-reversal-decomposition-2026-09-04]] - nearest equity-reversal neighbour, but a different source identity (Portnaya, arXiv:2606.29591) and a different mechanism (Fourier-residue / Fejer-sum decomposition of autocorrelation) versus this record's rare tail-event study with counting corrections.
- [[quant/illiquidity-at-risk-realized-amihud-mem-jump-tail-contagion-2026-09-02]] - shares the illiquidity-versus-tail theme, different mechanism (tail-risk forecasting from realised Amihud MEM-jump) and different source identity.
- [[quant/crypto-perp-crowded-flush-reversal-microstructure-2026-09-12]] - same "flush reversal" vocabulary, different market (Binance perpetuals at 5-minute horizon), different mechanism (microstructure cascade) and different source identity (Harshit Kumar GitHub).
- [[quant/crypto-4h-downside-semideviation-cascade-reversion-btc-confirmation-2026-09-12]] - crypto cascade reversion with a confirmation filter; different universe, horizon, mechanism and source identity.
- [[quant/crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12]] - crypto factor-residual mean reversion under turnover and execution costs; different mechanism, market and source identity.

Adjacent repository records located by the `flush` / `crash` / `reversal` / `Dashyan` scans and explicitly not duplicates of this source identity: `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md` (Harshit Kumar, GitHub commit `4526669f73ac46a86d05c8028a96236c7fa228cb`), `crypto-open-interest-crash-rebound-flow-gap-2026-09-03.md` (arXiv 2608.12841, AQuA agents), `crypto-perpetual-liquidation-cascade-overshoot-reversal-2026-08-31.md` (arXiv 2608.03616 and 2024/2025 cascade papers), `crypto-perp-llm-signal-backtest-to-live-gap-anatomy-2026-09-27.md` (the same author's other paper, SSRN 7353678), `fourier-residue-sign-magnitude-equity-reversal-decomposition-2026-09-04.md` (arXiv 2606.29591) and `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31.md`. Four-axis distinction: mechanism (rare market-wide tail-day liquidity concession repaid in one session, under date-level counting, disjoint bands and familywise correction), signal construction (crude close-to-close at-or-below -7 percent trigger, next-close or next-open entry, one-session hold, equal-split 20/95 percent caps), universe/market type (four US equity indices plus 28 single names, daily, 1950-2026), and material data dependency (an unnamed public vendor chart API and a 13-week T-bill series feeding both the trigger and the idle-cash account) all differ from each of those records, and every source identity differs - in particular SSRN `7363482` appears nowhere else in this repository, while the same author's SSRN `7353678` record studies an LLM signal's backtest-to-live gap rather than an equity event study.

## Sources

- Dashyan, Alexandr (SSRN author line) / Dashyan, Aleksandr (PDF title block), *The Tail Is the Only Signal: Flush Reversion in Equity Indices and Crypto Perpetual Futures*. SSRN abstract 7363482, DOI 10.2139/ssrn.7363482. Landing page read 2026-09-27: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7363482 (22 Pages, Posted 30 Aug 2026, Date Written July 01, 2026, Independent Researcher, CC BY-NC-ND 4.0 badge, `0 References`, `0 Citations`, 80 downloads / 162 abstract views at read time).
- Same paper, pinned PDF retrieved 2026-09-27 through https://papers.ssrn.com/sol3/Delivery.cfm/7363482.pdf?abstractid=7363482&mirid=1&type=2 (presigned object `download.ssrn.com/2026/8/28/7363482.pdf`), 501052 bytes, 22 pages, SHA-256 `33955a1110235ded8f83d4409385b33ac326d568e61b3140e2c61b673da97494`. All quantitative claims in this record trace to the printed Tables 1-3, Figures 1-6 and Sections 1-11 of that PDF.
- Works cited by the source and named in this record only as its stated background (not used for any performance claim): Lehmann (1990); Jegadeesh (1990); Lo and MacKinlay (1990); Grossman and Miller (1988); Campbell, Grossman and Wang (1993); Nagel (2012); Hameed, Kang and Viswanathan (2010); Hendershott and Menkveld (2014); Avramov, Chordia and Goyal (2006); Da, Liu and Schaumburg (2014); Kolari and Pynnonen (2010); Mitchell and Stafford (2000); White (2000); Romano and Wolf (2005); Harvey, Liu and Zhu (2016); Bailey and Lopez de Prado (2014); Politis and Romano (1994); Brunnermeier and Pedersen (2009); Makarov and Schoar (2020); Cheng, Deng, Wang and Yu (2021).
- Companion working papers listed by the source in its own reference list (`[7] Dashyan, A. (2026a)` *Short-horizon directional non-predictability in cryptocurrency perpetual futures*, `[8] Dashyan, A. (2026b)` *Adversarial backtest verification: catching overfitting, beta, collinearity, and look-ahead in a live trading-research program*, `[9] Dashyan, A. (2026c)` *Risk control as the durable edge*, `[10] Dashyan, A. (2026d)` *A real edge that loses: anatomy of a backtest-to-live gap in cryptocurrency perpetual futures*, i.e. SSRN 7353678) are `not stated in source` as retrievable public texts beyond 2026d; none of their results is used in this record.
