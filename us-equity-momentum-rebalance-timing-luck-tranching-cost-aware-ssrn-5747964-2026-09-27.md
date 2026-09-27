---
schema: strategy-research-record-v1
title: "Rebalance Timing Luck and Cost-Aware Portfolio Tranching in a Concentrated US Equity Momentum Rotation (SSRN 5747964, 'The Tranching Dilemma')"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5747964 (SSRN landing, opened and read in a browser session on 2026-09-27 after the Cloudflare interstitial cleared)"
  - "https://doi.org/10.2139/ssrn.5747964"
  - "https://concretumgroup.com/wp-content/uploads/2026/02/The-Tranching-Dilemma.pdf (authors' own public PDF copy, 1,254,826 bytes, 16 pages, SHA-256 b202ace1fccee25639082abff00bd8fce4d02607ffbcc87e126b7d5cf75de440, downloaded and read 2026-09-27)"
  - "https://concretumgroup.com/the-tranching-dilemma-a-cost-aware-approach-to-mitigate-rebalance-timing-luck-in-factor-portfolios/ (authors' landing page, discovery aid only)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Author affiliation differs by surface: SSRN landing prints both Carlo Zarattini and Alberto Pagani under 'Concretum Group'; PDF p.1 prints both under 'Concretum Research, Viale Carlo Cattaneo 1, 6900 Lugano, Switzerland' with emails carlo@concretumgroup.com and alberto@concretumgroup.com. Unreconciled."
  - "Title rendering differs by surface: SSRN landing heading and suggested citation read 'The Tranching Dilemma.A Cost-Aware Approach to Mitigate Rebalance Timing Luck in Factor Portfolios' (no space after the period); the PDF title block reads 'The Tranching Dilemma' on one line and 'A Cost-Aware Approach to Mitigate Rebalance Timing Luck in Factor Portfolios' on the next with no separating period; the SSRN page <title> tag wraps the subtitle in <b> </b><i>. All renderings preserved."
  - "Four date expressions: PDF p.1 prints 'First Version: November 14, 2025' and 'This Version: November 14, 2025'; PDF metadata CreationDate and ModDate are D:20251114095627+01'00'; SSRN landing prints 'Posted: 17 Nov 2025', 'Last revised: 14 Nov 2025' and 'Date Written: November 14, 2025'; the suggested citation is dated November 14, 2025. A posting date later than the last-revision date is internally odd. Unreconciled."
  - "Reference count conflicts: the SSRN landing displays '0 References' while the pinned PDF's reference list on p.16 carries 8 entries (Blitz et al. 2010; Da et al. 2014; Gray and Vogel 2016; Hoffstein et al. 2020; Hoffstein et al. 2019; Jegadeesh and Titman 1993; Kissell 2020; Zarattini et al. 2025). Unreconciled."
  - "Section 3 prose states that 'only two reaching marginal significance at the 5% level' for strategy alphas, but no row of Table 1 has an alpha pVal below 0.05 (the minimum printed pVal is 0.051, trading day 6; the next is 0.054, trading day 9). The prose claim and the printed table disagree. Unreconciled."
  - "Table 1 prints an identical CAGR of 18.01% for trading day 6 and trading day 9 while marking trading day 9 as the best and trading day 0 as the worst, so the best-schedule identity is ambiguous at the printed precision. Unreconciled."
---

# Rebalance Timing Luck and Cost-Aware Portfolio Tranching in a Concentrated US Equity Momentum Rotation (SSRN 5747964)

## Provenance

- **Primary source (paper):** SSRN working paper abstract `5747964`, DOI `https://doi.org/10.2139/ssrn.5747964`, landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5747964`.
- **Complete author list exactly as printed on PDF p.1:** `Carlo Zarattini` (superscript 1) and `Alberto Pagani` (superscript 2). No third author, no editor, no mentor line. Affiliation printed on PDF p.1: `Concretum Research, Viale Carlo Cattaneo 1, 6900 Lugano, Switzerland`; emails `carlo@concretumgroup.com`, `alberto@concretumgroup.com`; social handle `@ConcretumR`. The SSRN landing instead lists each author under `Concretum Group` (see frontmatter contradiction 1).
- **Title (three renderings, preserved unreconciled):** PDF title block `The Tranching Dilemma` / `A Cost-Aware Approach to Mitigate Rebalance Timing Luck in Factor Portfolios`; SSRN landing heading `The Tranching Dilemma.A Cost-Aware Approach to Mitigate Rebalance Timing Luck in Factor Portfolios`.
- **Version / date (primary-source checksum):** PDF p.1 `First Version: November 14, 2025` and `This Version: November 14, 2025`; PDF metadata `/CreationDate` and `/ModDate` = `D:20251114095627+01'00'`, `/Producer` = `MiKTeX pdfTeX-1.40.25`, `/Creator` = `LaTeX with hyperref`; SSRN landing `Posted: 17 Nov 2025`, `Last revised: 14 Nov 2025`, `Date Written: November 14, 2025`.
- **Landing statistics read in the browser session on 2026-09-27:** `16 Pages`, `DOWNLOADS 1,005`, `ABSTRACT VIEWS 2,568` (2,569 on a second read minutes later), `0 References`, `0 Citations`.
- **Licence / rights:** the landing states `The copyright holder has granted SSRN a license.` and `All rights reserved. No reuse allowed without permission.` No journal, no issue, and no peer-review statement appears on the landing or in the PDF, so **publication status is: SSRN working paper, peer-review status not stated in source**.
- **PDF used for every body claim:** the authors' own public copy at `https://concretumgroup.com/wp-content/uploads/2026/02/The-Tranching-Dilemma.pdf`, **1,254,826 bytes, 16 pages, SHA-256 `b202ace1fccee25639082abff00bd8fce4d02607ffbcc87e126b7d5cf75de440`**, downloaded 2026-09-27 and text-extracted page by page with `pypdf` to 29,288 characters across all 16 pages (`===== PAGE n =====` markers retained in the scratch extraction). Its byte length is **identical to the `Content-Length: 1254826` reported by SSRN's own `Delivery.cfm` delivery link for abstract `5747964`** on 2026-09-27; an SSRN-side SHA-256 was **not** computed because the SSRN delivery is issued as a short-lived presigned URL that was deliberately **not** reproduced or stored anywhere in this record, so byte-identity is asserted on length only and is `underspecified` beyond that.
- **Retrieval path:** the SSRN landing returned a Cloudflare interstitial to a plain `curl` (HTTP 403), so the landing was read in a browser session after the challenge cleared; the SSRN PDF delivery link was confirmed to return HTTP 200 / `application/pdf` / `Content-Length 1254826` from that session, and the text actually normalized here comes from the byte-length-matched authors' copy above.
- **Pre-write deterministic source-identity dedup (2026-09-27, before any file was created):** `rg -uuu` across the whole repository including `.mimo-worktrees/`, `.agents/`, `.hermes/`, `coverage_manifest.csv` (5,808 lines) and `_review_payload.json` for `5747964`, `Tranching`, `tranching`, `Rebalance Timing Luck` (case-sensitive) returned **0 hits**; `rebalance timing luck` (lowercase) returned exactly **1 hit**, inside `long-only-us-equity-ath-trend-following-vol-sizing-atr-ratchet-turnover-control-ssrn-5084316-2026-09-27.md` F12, where it is only a Scout-authored falsification threshold, not a source identity. `Hoffstein` returned 25 hits, all inside crypto momentum records citing Drogen, Hoffstein and Otte (SSRN 4322637), a different source. No repository record carries this DOI, this title, or this mechanism. `git log --oneline -20` was inspected as a convenience glance only.

## Economic mechanism

### Source-reported

The paper's object is **rebalance timing luck (RTL)**, defined by the authors (quoting Hoffstein et al. 2020) as the "potential performance dispersion between two identically managed strategies with different rebalance schedules". The authors argue, following Blitz et al. (2010) and Hoffstein et al. (2019, 2020), that:

- rebalance-date choice is an **uncompensated and non-mean-reverting** source of performance dispersion ("random but permanent artifacts", Hoffstein et al. 2019 as quoted on p.8);
- **portfolio tranching** - splitting the portfolio into N sub-portfolios (tranches) that trade independently on staggered, evenly spaced rebalance schedules - reduces RTL roughly by a factor of 1/N while leaving average CAGR and annual turnover essentially unchanged, at the cost of a linearly increasing number of trades (each tranche holds `1/(M x N)` weight, M = max holdings per tranche = 20);
- because tranching multiplies the number of smaller trades, its **net** benefit is AUM-dependent once commissions and market impact are charged: small accounts are hurt by minimum-commission thresholds, large accounts are helped by splitting chunky rebalances.

The dual objective stated in Section 1 (p.2) is to demonstrate the magnitude of RTL on a concentrated momentum case study and to offer a framework for choosing the degree of tranching. The paper explicitly states on p.4 that "the objective of this paper is not to propose a ready-to-trade investment strategy, but rather to present a realistic case study illustrating how the effects of rebalance timing luck can be analyzed and potentially addressed."

### Research interpretation

Falsifiable decomposition of what is being claimed, with each component's role named:

- **Predictive signal (the only candidate alpha):** a concentrated cross-sectional equity momentum rotation - liquidity filter, 2-12 month skip-month momentum, then an information-discreteness momentum-quality tiebreak. Hypothesized channels: trend continuation in individual names plus a reduction of momentum crashes when cumulative returns are built from many small gains rather than a few jumps (frog-in-the-pan quality, Da et al. 2014).
- **Implementation-timing risk (explicitly NOT alpha):** the same book rebalanced on different days of the month produces a CAGR spread that the source measures at 348 bp. This is dispersion around an expected return, not a return predictor; the paper says so directly ("tranching is not intended to enhance performance", p.9).
- **Variance-reduction overlay:** staggered tranching converts a single unlucky schedule into an average over schedules. Its value is a reduction of outcome dispersion, bought with more (but smaller) trades.
- **Friction layer as the binding constraint:** the optimal number of tranches is set by the interaction of a fixed minimum commission with I-Star market impact across AUM scales, i.e. an execution-cost mechanism, not an information mechanism.

Roles, in the hybrid structure required by the contract:

```text
Primary signal:  2-12 MOM top-100 of the 1000 most liquid Russell 3000 names
Selection filter: information-discreteness momentum quality, top 20, equal weight 5%
Calendar layer:   one monthly rebalance on trading day d of the month (20 variants)
Overlay:          split the book into N tranches on evenly spaced days (N = 1,2,4,5,10,20)
Risk / exit:      none - no stop, no drawdown control, full turnover to the new book
Cost model:       IB commission + SEC-doubled sells + I-Star impact, normalized to a reference AUM
```

Ablation of these components is not performed by the source; whether the timing layer matters independently of the signal is `research-proposed` territory (see F3).

## Signal

All operational rules below are **source-reported** (Section 2 pp.3-4, Section 3 p.5, Section 4 pp.8-13 of the pinned PDF) unless explicitly tagged.

- **Universe / formation:** Russell 3000 universe **including historical constituents**, from Norgate Data, prices adjusted for splits, corporate actions and dividends (p.3).
- **Lookback / selection pipeline (p.3):**
  1. liquidity filter: keep the **1000 most liquid** stocks, where liquidity is the **rolling 252-day median dollar volume** (footnote 1);
  2. momentum screen: rank the subset by past yearly return **ignoring the most recent month** (`2-12 MOM`), keep the **top 100**;
  3. momentum-quality selection: compute `ID = sgn(2-12 MOM) x [%neg - %pos]` over the formation period (percentage of positive and negative days; `sgn = +1` if `2-12 MOM > 0`, else `-1`), keep the **20 lowest ID** values (highest momentum quality, Da et al. 2014).
- **Signal formation timestamp / tradability:** "All signals, and consequently the amount of shares to buy or sell, are computed at the close of day t and executed at the close of day t + 1" (p.4). Timezone, session close definition and holiday handling: **not stated in source**.
- **Rebalance calendar (Section 3, p.5):** 20 variants of the same monthly schedule - variant `d` rebalances at the close of the `d`-th trading day of each month (`d = 0` first trading day ... `d = 19` twentieth), using signals from the last day of the previous month; if a month has fewer than `n` trading days, the **last available trading day** is used so that every month has exactly one rebalance event.
- **Tranching schedules (Section 4, Table 2, p.8):** for a 20-trading-day month, evenly spaced tranches give `N = 1 -> 20 schedules`, `2 -> 10`, `4 -> 5`, `5 -> 4`, `10 -> 2`, `20 -> 1`, **42 schedules in total**, all of which the authors simulate.
- **Entry / holding / re-entry:** at each scheduled rebalance the portfolio holds the 20 selected names at **5% each**; holdings remain unchanged until the next rebalance; "no interim adjustments are allowed" (p.3). No stop, no take-profit, no time exit other than the next rebalance.
- **Position sizing:** equal weight `5%` per name; under tranching, each position weight becomes `1/(M x N)` with `M = 20` (p.10).
- **Delisting handling (p.4):** on delisting the notional moves to cash and is **not logged as a transaction and does not count toward turnover**; the portfolio then holds fewer than 20 positions plus residual cash.
- **Cash:** positive and negative cash balances earn / are charged the **Kenneth French risk-free rate** (footnote 4 gives the negative-cash financing example). Fractional shares are allowed (p.4).
- **RTL metric (Section 4, p.9):** `RTL = CAGR(best schedule) - CAGR(worst schedule)` within a tranching configuration, evaluated at the end of the full simulation.
- **Objective function (Eq. 2, p.11):** `U(N) = CAGR(N) - RTL(N)` where `CAGR(N)` is the **average** long-term CAGR across all schedules at N tranches and `RTL(N)` is the best-minus-worst dispersion, both evaluated **net of fees** for the cost analysis.
- **Fully specified / underspecified:** the selection pipeline, calendars, sizing and RTL metric are reconstructable from the PDF. The **net-of-fee numeric grid** behind Figure 3 (`CAGR(N)`, `RTL(N)`, `U(N)` for each N and each reference AUM) is **never printed**, so the decisive cost-aware conclusion is `underspecified` from the paper alone; the I-Star ADV input definition is `underspecified`; the constant `Rf 2.45%` used in two Sharpe column headers is `not stated in source`.

## Required data

- **Instrument / universe:** US-listed common stocks in the Russell 3000 **with historical constituents** (survivorship handling: the source states the dataset "includes historical index constituents, thereby eliminating survivorship bias", p.3).
- **Vendor:** Norgate Data, 1991-2024, split / corporate-action / dividend adjusted (p.3). A second independent vendor is not used.
- **Market type:** cash equities, long-only rotation (long-only is implied by the selection and 5% weighting description; the words "long-only" are applied in the PDF only to Hoffstein's indices, so for the case-study book this is `not stated in source` beyond the mechanics).
- **Timeframe:** daily bars; monthly rebalance events; signals at close of day t, execution at close of day t+1.
- **Fields required:** daily adjusted OHLC (or at least close), daily dollar volume for the rolling 252-day median liquidity filter, positive/negative-day counts for the ID quality metric, index membership history, delisting dates and codes, dividends for adjusted-price construction, Kenneth French `Mkt-RF` and risk-free series.
- **Point-in-time:** index constituents must be point-in-time (historical constituents); no other availability lag is discussed.
- **Timestamp / timezone:** **not stated in source** (daily close convention only).
- **Missing data:** **not stated in source** (no stale-price, halt, or missing-bar policy).
- **Funding / fee data needs:** IB commission schedule ($0.0035/share, $0.35 minimum, doubled on sells), Kissell (2020) I-Star parameters, and a reference AUM grid ($25K, $100K, $1M, $10M, $100M). Spread, quoted depth, borrow and exchange fees are **not** inputs of the paper's model.

## Execution assumptions

**Source-reported (Section 2 p.4, Section 4 pp.11-12):**

- Signal-to-order timing: computed at close of day t, executed at **close of day t+1** (next-session execution, at the close).
- Order type: **not stated in source** (only "executed at ... close").
- Commissions: Interactive Brokers standard tier **$0.0035 per share, $0.35 minimum per trade**, and "these values are doubled for sell transactions to account for SEC clearing fees".
- Market impact: **I-Star**, parameters "calibrated by Kissell (2020) for the overall U.S. equity market": **a1 = 708, a2 = 0.55, a3 = 0.71**.
- Cost normalization (Eq. 3): `tcosts_norm_t = AUM_(t-1) x tcosts_t(AUM_ref) / AUM_ref`, i.e. costs are always computed at a fixed reference AUM and rescaled, so that cost drag does not mechanically grow as the book compounds.
- Reference AUMs: **$25K, $100K, $1M, $10M, $100M**.
- Leverage / margin: unlevered book with a cash account; negative cash is financed at the risk-free rate (footnote 4).
- Shorting / borrow: none - no short leg exists, so borrow is not applicable.
- Fractional shares allowed; **integer-share and lot-size constraints are therefore not modeled**.
- Gross tables (Table 1, Table 3) explicitly "assume no transaction costs" (Table 1 caption, p.6).

**Data gaps (never treated as zero):** a word scan of the full 16-page pinned text finds **zero occurrences** of `spread`, `slippage`, `latency`, `fill`, `borrow`, `ADV` (as a cost input), `participation`, `order type`, `timezone` and `bid`. Partial fills, queue position, exchange/marketplace fees, market-on-open vs close imbalance, closing-auction impact, latency and any participation cap are therefore `data gap` / `underspecified`, **not** unmodeled-by-inference-as-zero. The source itself concedes on p.13 that "our execution assumptions may not reflect actual institutional practices (such as splitting trades across multiple sessions)".

## Evidence

### Source-reported

Every figure below is `source-reported`, traces to the pinned PDF, and has **not** been independently reproduced. Market for all of them: US listed common stocks, Russell 3000 historical constituents, Jan 2 1991 - Nov 15 2024 (Table 1 / Table 3 captions), **gross of transaction costs unless stated**.

**Base strategy, 20 rebalance-day variants (Table 1, p.6; prose Section 3 p.7):**

- Analysis period printed in the caption: **January 2, 1991 to November 15, 2024**; "Results incorporate interest paid or received and assume no transaction costs"; alpha and beta come from regressing strategy excess returns on `Mkt-RF` from Kenneth French's library.
- **CAGR range: 14.53% (trading day 0, marked worst) to 18.01% (trading day 9, marked best; trading day 6 also prints 18.01)**; Section 3 states the gap is **348 basis points**, the abstract says "almost 350 basis points".
- Full CAGR vector by trading day 0..19: `14.53, 16.37, 16.60, 16.10, 16.91, 17.83, 18.01, 17.09, 17.09, 18.01, 17.40, 17.63, 16.02, 15.30, 15.42, 16.66, 17.38, 17.55, 17.58, 15.08`.
- Max drawdown across the 20 variants: **-69.31% (day 1) to -74.85% (day 19)**.
- Sharpe: **0.61 to 0.72** with `Rf 0%`, **0.53 to 0.63** with `Rf 2.45%` (the construction of the constant 2.45% is `not stated in source`).
- Average trades per year: **338.52 to 340.73** (Section 3: "roughly 340 executed trades per year"). Annual turnover: **1,051.81% to 1,072.44%** (Section 3: "around 1,060%").
- Beta **1.24 to 1.26**; alpha **3.07% (day 0) to 6.09% (day 6)** with alpha p-values **0.051 to 0.334**; Section 3 prose nevertheless claims "only two reaching marginal significance at the 5% level" (frontmatter contradiction 5). Footnote 5 asserts that "Proprietary research shows that the strategy can be adjusted to achieve statistically significant alphas in a more consistent way" - that evidence is withheld, `data gap`.
- Terminal wealth (Section 3, p.7): an initial $1 grows to **$99** in the least favourable run and **$272** in the most favourable run, "a difference of almost threefold".
- The source states that no rebalance threshold is imposed, so micro-rebalancing trades are deliberately included so that "rebalance timing luck is not affected by anything beyond the variation in rebalancing days".

**Tranching schedules (Table 2, p.8):** `N=1 -> 20`, `N=2 -> 10`, `N=4 -> 5`, `N=5 -> 4`, `N=10 -> 2`, `N=20 -> 1` possible schedules; **42 in total**, all simulated; RTL is the best-minus-worst CAGR within a configuration.

**Tranching results (Table 3, p.9), gross, means across all schedules of that configuration:**

| Tranches | Mean CAGR (%) | RTL (%) | Sharpe (Rf 2.45%) | Avg trades / year | Annual turnover (%) |
|---|---|---|---|---|---|
| 1 | 16.73 | 3.48 | 0.59 | 339.58 | 1060.41 |
| 2 | 16.81 | 2.05 | 0.60 | 679.16 | 1060.38 |
| 4 | 16.84 | 1.01 | 0.60 | 1357.48 | 1059.98 |
| 5 | 16.84 | 0.63 | 0.60 | 1696.48 | 1059.80 |
| 10 | 16.84 | 0.07 | 0.60 | 3391.53 | 1059.49 |
| 20 | 16.83 | 0.00 | 0.60 | 6748.10 | 1056.20 |

Caption provenance: "Values represent the mean of key metrics ... across all possible tranching schedules. The analysis period spans from January 2, 1991, to November 15, 2024." Prose (p.9-10): mean CAGR is materially unchanged, RTL "is consistently reduced", annual turnover "remains virtually unchanged" (Blitz et al. 2010), trades scale linearly with N, and "our results seem to confirm the findings of Hoffstein et al. (2019), who conclude that tranching reduces RTL by a factor of 1/N" (Figure 2, p.10, plots RTL and trades against N with a dotted 1/N reference line).

**Cost-aware layer (Section 4 pp.11-13, Eq. 2-3, Figure 3 p.13):** net-of-fee `U(N) = CAGR(N) - RTL(N)` evaluated at reference AUMs $25K / $100K / $1M / $10M / $100M with IB commissions and I-Star impact as specified above. Reported conclusions, all qualitative because **no numeric utility table is printed**:

- **$25K: optimal N = 2**; beyond that "the performance decay due to transaction costs begins to offset the benefits", because tranching produces more, smaller trades that hit minimum-commission thresholds.
- **$100K: optimal N = 5**, "with diminishing benefits thereafter".
- **$1M to $100M: benefits of tranching increase monotonically** with N.
- **$100M: U(1) is negative**, i.e. net-of-fee CAGR of a single-tranche book is lower than the RTL dispersion itself.
- Source framing (p.13): "larger portfolios are severely harmed by 'chunky' rebalancing practices", the utility functions are "strictly specific to our strategy", more holdings would make the $25K decay worse, and a low-turnover strategy would be dominated by trading costs rather than RTL.

**Conclusion (Section 5 p.14):** RTL "can be documented at intra-month resolution, with dispersion reaching almost 350 basis points"; tranching confirms prior literature on turnover and 1/N decay; retail investors "would benefit most from accepting a relatively high exposure to RTL"; institutions designing factor products "can successfully embrace tranching"; further research should seek "alternative momentum definitions capable of generating more stable rankings over time".

**Scout arithmetic self-check (arithmetic only, not a reproduction - the backtest was not re-run):** means of the 20 printed Table 1 rows give CAGR **16.728%**, turnover **1060.41%**, trades **339.58**, Sharpe(Rf 2.45%) **0.592**, exactly matching the N=1 row of Table 3; `1.1453^33.833 = 98.5` and `1.1801^33.833 = 271.2` reproduce the printed $99 / $272 terminal wealth and a 2.75x ratio; `18.01 - 14.53 = 3.48` reproduces the printed 348 bp RTL; trades scale to `2.00x / 4.00x / 5.00x / 9.99x / 19.87x` the single-tranche base for N = 2/4/5/10/20; RTL x N = `3.48, 4.10, 4.04, 3.15, 0.70, 0.00` shows decay **faster** than 1/N at N >= 10. Script exit 0, FAILS: 0.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **No demonstrated alpha in the primary evidence:** the best printed alpha p-value in Table 1 is 0.051, i.e. no rebalance-day schedule reaches the conventional 5% level, and the paper's own prose claiming two significant alphas conflicts with its own table.
2. **Alpha regressions are single-factor only** (strategy excess return on `Mkt-RF`), so the 3.07-6.09% "alpha" is unadjusted for size, value, or any momentum benchmark; beta is 1.24-1.26, so most of the return is market exposure.
3. **Drawdowns of -69% to -75%** gross; the strategy has no stop, no volatility targeting and no drawdown control of any kind.
4. **Turnover ~1,060% per year and ~340 trades per year**, deliberately including micro-rebalancing that a real manager might skip - an execution burden that is itself a risk, and the reason the friction layer dominates.
5. **Tranching produces no alpha by construction** - the source states it plainly: it reduces dispersion, not expected return (p.9).
6. **RTL at N = 10 and N = 20 collapses partly by construction:** RTL is the best-minus-worst range over the *available* schedules, and the number of available schedules falls from 20 (N=1) to 1 (N=20). At N=20 there is only one schedule, so `RTL = 0.00` is guaranteed arithmetically, not empirically; at N=10 only two schedules (even/odd days) are compared. The apparent faster-than-1/N decay measured by the Scout (`RTL x N = 0.70` at N=10) is therefore confounded with schedule-count shrinkage.
7. **The decisive cost layer is not numerically published:** Figure 3 shows utility curves but the paper prints no `CAGR(N)`, `RTL(N)` or `U(N)` values per reference AUM, so the optimal-N conclusions ($25K -> 2, $100K -> 5) cannot be checked from the paper alone (`underspecified`).
8. **I-Star inputs are underspecified:** the impact model needs an ADV and a participation/volatility input, but the paper never states which series feeds I-Star; footnote 1 defines liquidity as rolling 252-day median dollar volume, and whether that is the I-Star ADV input is not stated.
9. **The cost-normalization formula (Eq. 3) is itself a modelling choice** that removes AUM drift from the cost drag; conclusions are conditional on it and no sensitivity to it is reported.
10. **Costs are calibrated from external defaults**, not from this backtest's own fills: aggregate-market Kissell (2020) parameters and a published IB commission schedule, with no slippage, spread, latency or fill model at all.
11. **Single strategy, single sample, no holdout:** one concentrated momentum portfolio, one market, 1991-2024; there is no out-of-sample period, no second universe, and no walk-forward anything.
12. **No statistical inference on RTL itself:** no confidence interval, standard error or test is reported for any RTL number or for the difference between RTL(N) values; a 348 bp range is a full-sample range statistic that is upward-biased by construction (max minus min of 20 noisy outcomes).
13. **No multiplicity control:** 20 schedules x 6 tranching configurations x several metrics, with best/worst selection highlighted, and no adjustment; the "best" schedule (day 9) and "worst" (day 0) are order statistics.
14. **Withheld evidence:** footnote 5's "proprietary research" claim of consistent statistical significance is unverifiable (`data gap`).
15. **Delisting handling understates turnover:** on delisting, notional moves to cash without logging a transaction or counting toward turnover, so reported turnover excludes a real trading event.
16. **Fractional shares are allowed**, which suppresses the minimum-lot rounding friction that would matter most for the retail AUM conclusions the paper draws - i.e. the $25K cost drag is likely understated, while minimum commissions push the other way.
17. **Institutional execution is explicitly admitted to be unrealistic:** "our execution assumptions may not reflect actual institutional practices (such as splitting trades across multiple sessions)" (p.13), yet the $1M-$100M monotonic-benefit conclusion rests on exactly those assumptions.
18. **Schedule-spacing is approximate:** Table 2 assumes "a month contains approximately 20 trading days" while real months are adjusted to the last available trading day, so tranches are not exactly evenly spaced in months with fewer trading days.
19. **Best-schedule identity is ambiguous at printed precision** (18.01% for both day 6 and day 9, best marked on day 9).
20. **Constant `Rf 2.45%` Sharpe convention is undefined** in the source, and the risk-free series is otherwise taken from Kenneth French's time-varying library.
21. **No data or code availability statement anywhere in the 16 pages**; the dataset is a commercial vendor (Norgate), so full reproduction requires paid data and undisclosed code.
22. **Literature dependence:** the 1/N decay and the "permanent artifact" property are imported from Hoffstein et al. (2019, 2020) and Blitz et al. (2010); this paper's own evidence for them is one strategy and a schedule-count-confounded range statistic.
23. **The utility function is acknowledged by the authors as strategy-specific:** "these utility functions are strictly specific to our strategy" (p.13) - a direct limit on generalizing the optimal tranching counts.
24. **Publication and review status:** SSRN working paper with no peer-review statement, `0 References` / `0 Citations` shown on the landing at read time, and an all-rights-reserved licence that prevents redistribution of the PDF itself.

None of the above was found to contradict the *direction* of the tranching claim inside the reviewed source; absence of a contrary finding in this one paper is not evidence that no negative result exists.

## Falsification plan

All thresholds and decision rules below are `research-defined` (Scout-authored); the procedures they test are `source-reported` unless marked `research-proposed`.

- **F1 - Frozen forward replication (`research-defined`).** From **2026-10-01**, rebuild the 20 rebalance-day variants point-in-time for 24 months using current index constituents and the published pipeline. **Failure:** the forward CAGR range across schedules is `<= 0` or differs from the in-sample scale (348 bp per 33.8 years, i.e. an order-of-magnitude annualized equivalent) by more than 50%. **Action:** record RTL as a sample-specific artefact.
- **F2 - Table 1 / Table 3 reproduction gate (`research-defined`).** Reproduce the N=1 row: mean CAGR **16.73%**, RTL **3.48 pp**, turnover **1060.41%**, trades **339.58**, Sharpe **0.59**. **Failure:** any of `|mean CAGR - 16.73| > 0.50 pp`, `|RTL - 3.48| > 0.50 pp`, `|turnover - 1060| > 100 pp`. **Action:** treat all source numbers as unreproducible.
- **F3 - Schedule-count artifact test, decisive (`research-defined`).** Recompute `RTL(N)` with a **fixed schedule count** for every N (draw the same number of schedules, e.g. 20, from the N-tranche family with wrap-around / phase randomization `research-proposed`) instead of ranging only over the schedules that happen to exist for that N (20, 10, 5, 4, 2, 1 for N = 1, 2, 4, 5, 10, 20). **Failure:** the 1/N-shaped decay does not survive (RTL(10) and RTL(20) no longer collapse), or the fitted decay exponent moves from ~1 to `< 0.5`. **Action:** relabel the tranching benefit as partly a range-over-fewer-schedules artefact.
- **F4 - Cost-ladder adjudication of the optimal-N claim (`research-defined`).** Re-run `U(N)` under an all-in cost ladder of **0 / 25 / 50 / 100 bp per round turn** plus IB commission, at reference AUMs $25K / $100K / $1M / $10M / $100M. **Failure:** the claimed optima (`$25K -> 2`, `$100K -> 5`, monotone increasing for >= $1M, `U(1) < 0` at $100M) shift by more than **+/- 1 tranche** at any AUM under either the 25 bp or 50 bp ladder. **Action:** mark the optimal-tranching framework as cost-model dependent.
- **F5 - Net-number recovery gate (`research-defined`).** Obtain the numeric `CAGR(N)`, `RTL(N)`, `U(N)` grid behind Figure 3 (authors or re-implementation) and match it to within **0.25 pp**. **Failure:** the grid cannot be produced or does not match. **Action:** keep Figure-3 conclusions permanently `underspecified`.
- **F6 - Alpha significance under multiplicity (`research-defined`).** Apply Benjamini-Hochberg at `q < 0.10` across the 20 schedule alphas (and across the 42 simulated schedule-configurations of Table 2 as a second family). **Failure:** no schedule survives, which the printed p-values (min 0.051) already predict. **Action:** the base momentum book is treated as carrying **no demonstrated alpha**, and the record is cited only for its implementation-timing claim.
- **F7 - Rebalance-band ablation (`research-proposed` stop-loss on turnover).** Add a minimum rebalance band (e.g. skip trades moving a position by `< 0.5%` of NAV) that the source deliberately omits. **Failure:** RTL changes by `> 0.5 pp` or turnover falls by `> 30%` while CAGR is stable. **Action:** the published RTL magnitude is conditional on micro-trade inclusion.
- **F8 - Turnover and capacity audit (`research-defined`).** Convert the reported ~1,060% annual turnover into ADV participation for the 20-name book at each reference AUM. **Failure:** required participation exceeds **10% of ADV** at any AUM above $1M. **Action:** capacity claims restricted to below the breaching AUM.
- **F9 - Point-in-time universe rebuild (`research-defined`).** Rebuild with a second point-in-time Russell 3000 constituent history and explicit delisting codes. **Failure:** mean CAGR or RTL shifts by `> 1.0 pp` / `> 0.5 pp`. **Action:** survivorship or constituent-history sensitivity recorded as a material limitation.
- **F10 - Independent-vendor rebuild (`research-defined`).** Re-run on a non-Norgate daily source. **Failure:** RTL differs by `> 0.5 pp` or the identity of the best/worst schedule changes. **Action:** vendor-dependent result.
- **F11 - Subperiod stability (`research-defined`).** Split 1991-2024 into 1991-2005 / 2006-2015 / 2016-2024 and recompute RTL per subperiod. **Failure:** max/min subperiod RTL ratio `> 2x` or any subperiod RTL `< 0.5 pp`. **Action:** RTL reported as regime-dependent rather than structural.
- **F12 - Placebo / circular-shift test (`research-defined`).** Randomly reassign which trading day is labelled the rebalance day (1,000 circular shifts of the schedule labels `research-proposed`) and compare observed RTL to the placebo distribution. **Failure:** observed RTL is below the **95th percentile** of the placebo. **Action:** reject the claim that the measured range is schedule-specific.
- **F13 - Alternative-momentum robustness (`research-defined`)**, using the source's own closing call for "more stable" definitions: repeat with 11-1 skip-month momentum, volatility-scaled momentum and residual momentum under the identical calendar layer. **Failure:** RTL scales so tightly with turnover that `RTL(N) x turnover(N)` is constant (pure cost artefact) or the sign of the tranching benefit flips at $100K. **Action:** restrict the framework to high-turnover books.
- **F14 - Crypto port test (`research-defined`).** Port only the calendar/RTL layer to a daily crypto top-20 rotation on a 24/7 clock with monthly schedules defined on UTC month boundaries `research-proposed`. **Failure:** RTL is indistinguishable from zero (`< 0.5 pp`) or does not decay with N. **Action:** conclude the mechanism is specific to calendar-driven, session-closed markets and revise the Crypto portability section.

## Crypto portability

**unproven.**

The evidence base is US listed cash equities on a session-closed daily calendar with a monthly rebalance ritual; the source tests no crypto market and makes no crypto claim. Portability considerations:

- the RTL mechanism depends on discrete, shared calendar rebalance events - crypto trades 24/7, so "the 5th trading day of the month" has no natural analogue and any UTC-month-boundary choice is a `research-proposed` convention;
- the signal needs a point-in-time large-cap index (Russell 3000 equivalent) with survivorship-free membership; crypto equivalents (market-cap top-N) are survivorship-prone and reconstitute continuously;
- futures/perpetual variants would add funding, mark price, liquidation and contract-roll mechanics that the source never models;
- venue fragmentation, candle-boundary differences (exchange-local vs UTC), and spot-vs-perpetual basis would each perturb a `close of day t -> close of day t+1` execution convention;
- the friction layer (IB commission + SEC clearing + I-Star) is entirely non-transportable; crypto taker/maker fees, spreads and impact would need a fresh cost model, which is exactly where this paper's conclusions are most fragile.

Nothing in this record is crypto empirical evidence.

## Limitations

- `underspecified`: the numeric net-of-fee utility grid behind Figure 3; the I-Star ADV/participation input; the constant `Rf 2.45%` Sharpe convention; order type, session close definition, timezone, holiday and missing-data policy.
- `data gap`: spread, slippage, latency, fill model, partial fills, exchange fees, participation caps, integer-share constraints, turnover in dollar/ADV terms, borrow (not applicable - long-only), and any code or data release.
- `not stated in source`: whether the case-study book is formally long-only; how delisting proceeds are reinvested relative to the next scheduled rebalance beyond the cash-account treatment; the derivation of the "almost 350 bp" claim's uncertainty.
- `not independently reproduced`: every performance figure in this record. The only checks performed were (a) full reading of all 16 pinned pages, (b) internal arithmetic consistency of Table 1 vs Table 3 and of the printed terminal wealth, (c) a whole-repository source-identity dedup.
- Interpretation limits: this record captures an **implementation-timing / portfolio-construction** hypothesis plus the momentum construction it is measured on. The source explicitly disclaims being a ready-to-trade strategy proposal; the momentum book itself shows no alpha significant at 5% in its own Table 1.
- Source quality: SSRN working paper, all-rights-reserved licence, no peer-review statement, zero references and zero citations shown on the landing at read time, commercial data dependency, no public code.
- Publication-bias / selection: best-minus-worst range statistics across 20 schedules are upward-biased order statistics; no multiplicity control is applied anywhere in the source.

## Implementation status

`implementation_status: not-implemented`.

No part of this record has been implemented in our research stack: no backtest was re-run, no ledger was consulted, no test suite was executed, no Qlib (or any other) validation occurred, and no Paper, Testnet or Live workflow was touched. This run performed only primary-source reading (SSRN landing in a browser, pinned PDF text extraction), an arithmetic self-check of printed table values, and a deterministic repository dedup search. This capture does not modify any engine, does not create a strategy family, and does not authorize execution.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed any full backtest; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No record may promote itself by wording, evidence count, confidence or schedule behaviour; any adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Wiki Brain was queried read-only on 2026-09-27 (`kb_search`; **no Wiki write was performed**). Queries `rebalance timing luck portfolio tranching` and `rebalance schedule dispersion smart beta factor rotation equal weight` and `I-Star market impact transaction cost model capacity` returned **0 pages**, so no page exists for this mechanism; the following **verified existing** pages were returned by adjacent queries and are linked as retrieval hooks, not as endorsements:

- [[quant/two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]] - adjacent cross-sectional stock-ranking deployment record; different mechanism (regime-trust gating vs. calendar-timing dispersion).
- [[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]] - adjacent search-aware / deflated-evaluation record; relevant to the multiple-comparison structure of choosing among 20 schedules.

Repository records that are **not** Wiki links (dedup context; distinct source identities):

- `long-only-us-equity-ath-trend-following-vol-sizing-atr-ratchet-turnover-control-ssrn-5084316-2026-09-27.md` - same first two authors and it is cited inside this PDF as `Zarattini et al. (2025)`, but a **different paper and mechanism** (daily all-time-high time-series trend following with ATR ratchet stops vs. monthly cross-sectional momentum rotation plus rebalance-timing dispersion); its F12 even uses "rebalance timing luck" only as a Scout-authored threshold.
- `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` - shares first author Zarattini (SSRN 4824172), half-hour SPY intraday rule; distinct horizon and universe.
- `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` - shares authors Zarattini/Pagani (SSRN 5209907), crypto Donchian rotation; distinct asset class and channel.
- `pure-momentum-wild-bootstrap-drift-significance-filter-us-equities-2026-09-26.md` - US equity pure momentum, but the axis is statistical significance filtering of the signal, not the rebalance calendar.
- `industry-trend-keltner-donchian-fallback-wfa-falsification-arxiv-2412.14361-2026-09-23.md` - shares first author (SSRN 4857230 baseline), industry-level trend; distinct mechanism.

Four-axis distinction (source identity + mechanism, material for every pair): this record's source is SSRN `5747964` with a **rebalance-calendar dispersion / staggered-tranching** mechanism on a **monthly concentrated equity momentum** book; the five records above differ in source identity and in at least one of mechanism, signal construction, universe/market type, horizon/regime, or material data dependency.

## Sources

1. Carlo Zarattini, Alberto Pagani. "The Tranching Dilemma. A Cost-Aware Approach to Mitigate Rebalance Timing Luck in Factor Portfolios." SSRN abstract `5747964`, DOI `https://doi.org/10.2139/ssrn.5747964`, landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5747964` (read in a browser session 2026-09-27: `16 Pages`, Posted 17 Nov 2025, Last revised 14 Nov 2025, Date Written November 14, 2025, 1,005 downloads, 2,568-2,569 abstract views, 0 References, 0 Citations, all-rights-reserved licence, no journal and no peer-review statement). Primary source for author list, dates, abstract, licence, landing statistics.
2. Pinned PDF actually read: `https://concretumgroup.com/wp-content/uploads/2026/02/The-Tranching-Dilemma.pdf` - authors' own public copy, **1,254,826 bytes, 16 pages, SHA-256 `b202ace1fccee25639082abff00bd8fce4d02607ffbcc87e126b7d5cf75de440`**, retrieved 2026-09-27, byte length identical to the `Content-Length: 1254826` served by SSRN's own `Delivery.cfm` link for abstract 5747964 in the same session (SSRN-side hash not computed; the presigned delivery URL was deliberately not stored). Text extracted page by page with `pypdf` to 29,288 characters across all 16 pages; source for Section 1-5, Eq. 1-3, Table 1/2/3, Figure 1/2/3 captions, footnotes 1-5, references and author biography.
3. `https://concretumgroup.com/the-tranching-dilemma-a-cost-aware-approach-to-mitigate-rebalance-timing-luck-in-factor-portfolios/` - authors' landing page (discovery aid only; no empirical claim in this record is taken from it).
