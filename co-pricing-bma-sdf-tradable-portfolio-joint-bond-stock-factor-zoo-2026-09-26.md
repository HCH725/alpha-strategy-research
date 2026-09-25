---
schema: strategy-research-record-v1
title: "Co-Pricing BMA-SDF tradable portfolio — Bayesian model averaging over a 54-factor joint bond/stock zoo (arXiv:2604.04430v1)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arxiv
  - factor-zoo
  - bayesian-model-averaging
  - stochastic-discount-factor
  - corporate-bonds
  - equities
  - cross-sectional
  - portfolio-construction
status: research-only
confidence: high
source_as_of: 2026-09-26
sources:
  - "arXiv:2604.04430v1 [q-fin.PR], 'The Co-Pricing Factor Zoo', Alexander Dickerson, Christian Julliard, Philippe Mueller; submitted Mon, 6 Apr 2026 05:23:01 UTC (1,635 KB); https://arxiv.org/abs/2604.04430 (abs read 2026-09-26)"
  - "https://arxiv.org/html/2604.04430v1 — pinned v1 HTML, 1,099,677 bytes, SHA-256 d6d9b386223830b72be797e83ec25c3b00da99e27b1c94a54c216bfbca55d987 (retrieved 2026-09-25, re-fetched and re-hashed 2026-09-26 with identical hash); full body read for this record"
  - "https://arxiv.org/pdf/2604.04430v1 — pinned v1 PDF, 3,038,880 bytes, SHA-256 2bf6fadbb0cb5618aab7dd1104cf95668204bec587e6074c2809d34c9b5263dd (retrieved 2026-09-25, re-hashed 2026-09-26 with identical hash)"
  - "https://doi.org/10.48550/arXiv.2604.04430 — DataCite DOI, HTTP 302 to abs (checked 2026-09-26)"
  - "https://github.com/Alexander-M-Dickerson/co-pricing-factor-zoo — official replication package; default branch main, tip commit 55663cec28848f8875a112190b5a6cb2a5505772 authored 2026-04-13T03:33:06Z, tree of 307 entries (not truncated) containing _run_full_replication.R, _run_complete_replication.R, ia/_run_ia_full.R, README.md, QUICKSTART.md (verified via GitHub git/trees and commits API 2026-09-26)"
  - "https://raw.githubusercontent.com/Alexander-M-Dickerson/co-pricing-factor-zoo/55663cec28848f8875a112190b5a6cb2a5505772/README.md — replication README (read 2026-09-26); its table states Journal 'Journal of Financial Economics (Forthcoming)' and links SSRN abstract_id=4589786"
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4589786 — SSRN landing cited by the replication README; HTTP 403 to a scripted client (browser user-agent, curl, 2026-09-26) so the SSRN record and journal-acceptance claim were NOT independently verified"
  - "https://openbondassetpricing.com/ — companion data site named in the pinned v1 text and replication README (not fetched this run; bundle contents are a data gap)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal (pinned v1, Table 6 note): TOPγ and TOPλ are listed with the SAME five factor IDs (PEADB, PEAD, CMAs, CRY, MOMBS) in different order, and the note says both 'use the MPRs', yet the two columns report different performance (IS mean 33.77 vs 34.04; OOS mean 20.59 vs 23.41). Section 3.1.2 prose says selection is 'by posterior probability and MPR, respectively'. The exact distinguishing rule that produces different weights from an apparently identical factor set is underspecified in the pinned text."
  - "Provenance-order ambiguity (pinned v1, Table 6): the table header row orders the last benchmarks FF5 | HKM | MKTB | MKTS while the caption prose lists 'benchmark models (FF5, HKM, MKTS, MKTB)'. This record attributes those four columns by the header row order and flags the caption's different listing order rather than silently reconciling it."
---

# Co-Pricing BMA-SDF tradable portfolio (The Co-Pricing Factor Zoo, arXiv:2604.04430v1)

## Provenance

**Primary source.** arXiv:2604.04430**v1**, category `q-fin.PR`, title *The Co-Pricing Factor Zoo*, complete author list exactly as printed: **Alexander Dickerson, Christian Julliard, Philippe Mueller** (three authors; abs page: "by Alexander Dickerson and 2 other authors"). Submission history shows a single version: `[v1] Mon, 6 Apr 2026 05:23:01 UTC (1,635 KB)`; `https://arxiv.org/abs/2604.04430v2` returns HTTP 404 (checked 2026-09-26), so v1 is the sole and latest version as of 2026-09-26. Abs page shows **no Comments field, no journal-ref, no publisher DOI** beyond the arXiv-issued DataCite DOI `10.48550/arXiv.2604.04430` (HTTP 302 → abs, checked 2026-09-26). License line in the pinned HTML: "arXiv.org perpetual non-exclusive license", so the text is cited and normalized here rather than reproduced.

**Pinned snapshots (re-verified this run).** Pinned HTML `https://arxiv.org/html/2604.04430v1` = **1,099,677 bytes, SHA-256 `d6d9b386223830b72be797e83ec25c3b00da99e27b1c94a54c216bfbca55d987`**; pinned PDF `https://arxiv.org/pdf/2604.04430v1` = **3,038,880 bytes, SHA-256 `2bf6fadbb0cb5618aab7dd1104cf95668204bec587e6074c2809d34c9b5263dd`**. Both were first retrieved 2026-09-25 and re-fetched/re-hashed on 2026-09-26 with byte-identical hashes (idempotent pin). The body was read from the stripped text of the pinned HTML, including Sections 1–5, Table 6 note, Figure 3/6/7/10 captions, Appendix A factor list references and the benchmark descriptions in Appendix D.

**Publication / peer-review status.** The first line of the pinned HTML reads "Nikolai Roussanov was the editor for this article", followed by thanks to "an anonymous referee" — a referee-handling statement inside the manuscript. arXiv metadata itself carries **no journal-ref and no journal name**, so publication status is `not stated in source` on the primary arXiv record. The official replication README at pinned commit `55663cec28848f8875a112190b5a6cb2a5505772` states `Journal of Financial Economics (Forthcoming)` and links `SSRN abstract_id=4589786`; the SSRN landing returns **HTTP 403** to a scripted client (browser user-agent, 2026-09-26), so the journal-acceptance claim and the SSRN record were **not independently verified** and remain a source-reported claim from the replication repository only. An earlier version of the paper circulated under the title **"The Corporate Bond Factor Zoo"** (stated in the pinned HTML footer block); that title is used as a dedup pattern below.

**Replication code.** `https://github.com/Alexander-M-Dickerson/co-pricing-factor-zoo`, default branch `main`, tip commit **`55663cec28848f8875a112190b5a6cb2a5505772` (2026-04-13T03:33:06Z)**, tree 307 entries and `truncated: false`, containing `_run_full_replication.R`, `_run_complete_replication.R`, `ia/_run_ia_full.R`, `README.md`, `QUICKSTART.md` (all confirmed by path lookup against the pinned-commit tree API, 2026-09-26). The README claims the two scripts reproduce all main-paper/appendix/Internet-Appendix tables and figures (~65 + ~16 minutes, 50,000 MCMC draws, 24-core desktop) with data from a single public bundle at openbondassetpricing.com. **The Scout did not execute any of this code**; reproducibility of the printed numbers is unverified by us.

**Data as-of.** Sample data end **2022:12** (IS 1986:01–2022:12; OOS 2004:07–2022:12). `source_as_of: 2026-09-26` is the date the primary source was pinned and re-verified.

**Repo-wide dedup (run 2026-09-26, before writing).** A hidden-inclusive scan walked **all 2,548 `*.md` files** in the repository (including `.mimo-worktrees`, `.agents`, `.hermes`) plus `coverage_manifest.csv`, testing 16 source-identity patterns: `2604.04430`, `10.48550/arXiv.2604.04430`, `Co-Pricing Factor Zoo`, `The Corporate Bond Factor Zoo`, `co-pricing-factor-zoo`, `openbondassetpricing`, `Alexander Dickerson`, `Christian Julliard`, `Philippe Mueller`, `BMA-SDF`, `BMA SDF`, `18 quadrillion`, `PEADB`, `Julliard`, `Dickerson`, `Mueller`. **All 16 patterns returned 0 files.** Near-string probes (`Kozak`, `Bryzgalova`) resolve only to unrelated records (`aeap-seads-llm-agentic-…`, `cross-predictive-sdf-…`, `daily-return-information-factor-drif-…`). `git pull origin main` was up to date and `git status --porcelain --untracked-files=no` was clean before research began. No existing record for this source identity was found, so no material-distinction argument is required.

## Economic mechanism

### Source-reported

The authors analyse **18 quadrillion models** (`2^54`) for the joint pricing of corporate bond and stock returns with a hierarchical Bayesian spike-and-slab prior on factor inclusion (continuous spike-and-slab, §2.3), and argue that:

- the **true latent SDF is dense** in the space of observable factors: many individual factors are only noisy proxies for a smaller set of common underlying risks, so selection of a handful of factors is the wrong operation and **aggregation (Bayesian model averaging) is what the data reward** (§1, §3.1.4, §5);
- **equity and non-tradable factors alone suffice** to explain corporate bond risk premia once the bond's **Treasury term-structure component** is accounted for, "rendering the extensive bond factor literature largely redundant for this purpose" (abstract, §3.3); stock factors cannot price that Treasury component, which the source reads as partial segmentation between equity and Treasury markets and commonality between equity markets and credit risk (§3.3, Figure 8/9);
- averaging over models is equivalent to averaging over factors, so the BMA-SDF can be made tradable by weighting the **posterior means of the market prices of risk (MPRs)** of all (tradable) factors rather than by selecting factors (§1, §3.2);
- the resulting tradable strategy delivers a **time-series out-of-sample annualized Sharpe ratio of 1.5 to 1.8 "despite only yearly rebalancing"** over July 2004–December 2022, an evaluation period spanning the Global Financial Crisis and the COVID contraction (abstract, §1, §5);
- the SDF and its conditional mean/volatility are persistent, track the business cycle and heightened-uncertainty episodes, and predict future asset returns (abstract, §3.4).

Source-reported supporting statements (all pinned v1): the ex-post maximum Sharpe ratio of the test assets is **5.4 annualized** (§3.1.1); a factor-inclusion prior set at 60–80% of that maximum implies prior annualized Sharpe ratios of about **1.0 to 4.2** (§3.1.1); Table 1 discussion reports the posterior mean Sharpe contribution of the top-five factors `E[SR_f|data]` ranging **0.78 to 1.46** for 60%–80% priors while their share of squared SDF Sharpe is "quite limited" (§3.1.1).

### Research interpretation

Two separable, falsifiable hypotheses are embedded in one strategy:

1. **Aggregation-over-selection (mechanism):** when the priced-risk space is dense and each observed factor is a noisy proxy, shrinkage-weighted averaging across the whole zoo should beat (a) any sparse model and (b) ex-post selection of a "top" subset, *out of sample*, because selection error grows with zoo size while averaging error shrinks.
2. **Cross-market discipline (mechanism):** jointly pricing bonds and stocks constrains the posterior MPRs with two cross-sections at once, so the bond leg borrows statistical strength from the equity leg (and vice versa); the source's own Treasury-component decomposition is the proposed economic channel linking them.

The tradable object is therefore **a portfolio-construction rule, not a new anomaly**: weights = normalized posterior-mean MPRs over the 40 tradable factors, refreshed annually, volatility-scaled to the equity index. Component roles:

```text
Estimation regime: expanding monthly window, initial 222 months (1986:01–2004:06), re-estimated every year
Aggregation:       Bayesian model averaging (spike-and-slab) over 54 factors -> posterior mean MPRs
Signal/weights:    normalize MPRs of the 40 tradable factors to sum to one
Scaling:           rescale all tradable strategies to the equity-index volatility (research-proposed? no: source-stated, §3.2)
Holding/exit:      hold the resulting 40-factor portfolio for 12 months, then re-estimate and re-weight
```

Note the source explicitly calls the tradable version a **lower bound**, because it excludes the 14 non-tradable factors which themselves command a non-trivial Sharpe (§3.2). Our reading: that framing is untested — excluding non-tradable factors changes both the estimation sample and the weight vector, so the direction of the bias is an open empirical question (see Falsification F6).

## Signal

All items below are **source-reported unless marked otherwise**. Formation/holding cadence is monthly data with a yearly re-estimation cycle.

- **Formation timestamp:** portfolio weights are computed at each yearly estimation date from the expanding monthly sample through the month before the evaluation year; the sample data are monthly (IS 1986:01–2022:12, `T=444`). Publication/availability convention for the underlying vendor data is **not stated in source** (data are retrospective vendor composites; no point-in-time release lag is modelled) → `data gap`.
- **Lookback:** expanding window, **initial window 222 months = 1986:01–2004:06**, then "expanded by twelve months" every year (§3.2). Endpoints: source states the IS period as 1986:01 to 2022:12 inclusive (`T=444`) and the OS period as 2004:07 to 2022:12 inclusive (`T=222`).
- **Weight construction (the signal):** "Portfolio weights for the tradable strategies are constructed by normalizing the posterior means of the MPRs of the SDF representations to sum to one in each specification" (§3.2), **restricted to the 40 tradable factors** because all benchmarks are exclusively tradable. Prior for factor inclusion is Beta(1,1) (prior inclusion probability 50%); prior Sharpe ratio grid = **20%, 40%, 60%, 80% of the ex-post maximum Sharpe ratio of the test assets** (which changes with the expanding window in Panel B; Table 6 note).
- **Scaling:** "all tradable portfolio strategies are normalized to have the same volatility as the equity market index" (§3.2); Figure 7 states "portfolio returns are scaled to have a constant volatility equal to that of the stock market factor (MKTS)". **Gross leverage implied by that rescaling is not reported anywhere in the pinned text** → `data gap`.
- **Entry / direction:** long-short combination of 40 factor portfolios (16 bond + 24 stock tradable factors) at the normalized MPR weights; **no long-only constraint is stated**, and **no borrow/short-feasibility rule is stated** for the 16 corporate-bond factor legs → `data gap` / `underspecified`.
- **Exit / holding period:** weights "are then used to invest in the factors over the next 12 months" and are held constant for the year, then recomputed (Table 6 note; §3.2; Figure 7). Source describes this as "yearly rebalancing" (the only rebalancing statement in the paper).
- **Re-entry:** automatic on the next yearly re-estimation.
- **Parameters:** prior grid {20,40,60,80}% (a **tuned/ex-post grid**, see Negative evidence), Beta(1,1) inclusion prior, 50% prior inclusion probability, top-five definitions for TOPγ/TOPλ (see contradictions in frontmatter), KNS twofold cross-validation re-run at every estimation, RPPCA PCs re-estimated at every estimation, GMM weights for RPPCA/FF5/HKM (Table 6 note).
- **Benchelines in the same table:** TOPγ (top five factors by posterior probability), TOPλ (top five by MPR), KNS (Kozak, Nagel, Zimmermann-style latent-factor SDF, §D), RPPCA (Lettau–Pelger risk-premia PCA), FF5, HKM (He, Kelly, Matai two-factor), MKTB, MKTS, and EW = equally weighted portfolio of all 40 tradable factors (also the IR benchmark).
- **Fully specified?** The **weighting rule and cadence are specified**; the **exact per-period weight vectors, the leverage from vol-scaling, the short/borrow feasibility, the tie/ordering rule behind TOPγ vs TOPλ, and the arithmetic-vs-log convention of the Mean column are underspecified.** A researcher can reconstruct the procedure but not the exact printed portfolio from the paper alone without the replication package.

## Required data

- **Instruments / universe:** U.S. corporate bonds and U.S. equities. Bonds: LBFI/BAML ICE bond-level data merged with **Mergent FISD** for characteristics; sample deliberately begins **1986** because pre-1986 LBFI bonds are 91% investment grade with 67% matrix-priced (non-quote) prices (§1.1). The bond-level data span 37 years = **444 monthly observations**; merged with CRSP equity data the sample covers **75% of total stock-market capitalization of listed firms on average** (§1.1).
- **Test assets (IS):** **123** = **50 bond portfolios + 33 stock portfolios + 40 tradable factors** (§1.3, §3.1.1). Bond portfolios are double-sorts on ratings/credit spreads, size, and similar characteristics; stock portfolios follow standard anomaly constructions (§1.3).
- **Test assets (OS):** **154 bond and stock portfolios (77 each)** built from 14 distinct cross-sections (§1.4), plus **29 Treasury portfolios** with maturities 2–30 years used in the §3.3 Treasury-component analysis.
- **Factor zoo:** **54 factors = 40 tradable (16 bond + 24 stock) + 14 non-tradable**, giving `2^54 ≈ 18 quadrillion` models (§1.2, §3.1); robustness extension to a **grand total of 91 candidate pricing factors** over varying subsamples (§4.4.3). Factor list is Appendix A / Table A.1.
- **Fields:** monthly bond returns in excess of the one-month risk-free rate, duration-adjusted bond returns (source equation (10)), equity returns, factor returns, Treasury portfolio returns, the one-month risk-free rate, and the estimated posterior MPRs.
- **Venue / market type:** U.S. dealer corporate-bond market (via LBFI/ICE pricing, with WRDS TRACE and DFPS TRACE used only as *alternative data sources* in the §4.4.1 robustness) plus CRSP equities. No exchange, no crypto venue.
- **Timeframe:** monthly bars; annual weight cycle; timezone/session convention not stated (monthly data) → not applicable beyond monthly alignment.
- **Point-in-time:** **not modelled.** All inputs are retrospective vendor composites; no publication lag, revision handling, or availability filter is described → `data gap` (also a look-ahead risk for any replication that starts in 1986 using today's vendor files).
- **Missing data:** source applies "standard filters" and merges; exact filter list is in §1.1 but survivorship/backfill handling of the vendor histories is `underspecified`.
- **Funding / fee / spread needs:** the source models **none of them** (see Execution assumptions).

## Execution assumptions

**Transaction-cost determination (Methods-level read, this run).** I read §1 (Data), §2 (Econometric method), §3.2 (Trading the BMA–SDF), §4 and §4.4.1 (robustness incl. alternative bond data), §5, Appendix A and Appendix D, and then ran a case-insensitive substring scan of the entire pinned v1 text. Results:

- `transaction` = **2**, both in §4.4.1 and *both refer to datasets* — "(iv) the transaction-based WRDS TRACE data, and (v) the transaction-based DFPS TRACE data" — **not to costs**;
- `turnover` = 0, `slippage` = 0, `bid-ask`/`bid ask` = 0, `commission` = 0, `transaction cost` = 0, `trading cost` = 0, `fees` = 0, `market impact` = 0, `participation` = 0, `ADV` = 0, `drawdown` = 0, `win rate` = 0, `short selling` = 0, `liquidation` = 0, `latency` = 0, `rebalance` = 0 with `rebalancing` = **2** (both "yearly rebalancing"), `capacity` = **1** (equilibrium "risk-bearing capacity" in §3.1.1, not a trading-capacity model), `friction` = **1** (literature-review sentence "behavioral market frictions in asset pricing", not a model), `cost` = 1 (an accounting-reference title, "implied cost of capital");
- the remaining apparent hits (`fee`, `margin`, `leverage`, `funding`, `fill`, `spread`, `adv`) all resolve to non-cost contexts on inspection: arXiv HTML footer boilerplate, "marginal(ly)", "leverages"/a low-beta factor definition, arXiv "funding support" footer, "fill this gap", and credit/yield-spread *factor definitions*.

**Conclusion: the primary source contains no transaction-cost, slippage, spread, borrow, margin, funding, participation, impact, fill or capacity model of any kind.** Every one of those fields is `data gap` — **never zero** — and **no printed number in this record is net of cost**.

Other execution assumptions:

- **Signal-to-order timing:** weights computed at the yearly estimation date and invested for the following 12 months; same-bar/next-bar convention at monthly granularity is not stated → `underspecified`.
- **Order type / fill model:** not stated → `data gap`.
- **Latency:** not stated → `data gap`.
- **Leverage / margin:** volatility scaling to MKTS implies leverage (or deleveraging) but **gross leverage `sum|w|` is never printed** → `data gap`; financing cost of any levered sleeve is therefore also unmodelled.
- **Borrow / shorting:** the strategy combines 40 factor portfolios including 16 corporate-bond factors, several of which are long-short by construction (e.g. the low-beta factor "holds low-beta assets, leveraged to beta 1, and shorts high-beta assets, de-leveraged"). **Bond short feasibility, stock-loan fees and dealer willingness-to-borrow are never discussed** → `data gap`.
- **Capacity / impact:** not addressed → `data gap`.
- **Source vs Scout:** everything in this section that is not explicitly attributed to the source is a `data gap` or `underspecified`; **no cost, fill, sizing or leverage assumption in this record is Scout-invented** — the falsification thresholds further down are the only research-defined numbers, and they are labelled as such.

## Evidence

### Source-reported

All figures below are transcribed from the pinned v1 HTML **Table 6 ("Trading the BMA-SDF and benchmark models")**, column order taken from the table header row: `BMA-SDF prior Sharpe ratio 20% | 40% | 60% | 80% | TOPγ | TOPλ | KNS | RPPCA | FF5 | HKM | MKTB | MKTS | EW`. **Gross of cost** (no cost model exists). Means annualized in percent; SR and IR annualized; IR benchmark = EW.

**Panel A — In-sample, 1986:01–2022:12 (`T=444`)**

| row | 20% | 40% | 60% | 80% | TOPγ | TOPλ | KNS | RPPCA | FF5 | HKM | MKTB | MKTS | EW |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mean | 31.38 | 38.94 | 43.43 | 45.03 | 33.77 | 34.04 | 40.54 | 39.59 | 12.20 | 8.37 | 10.18 | 8.29 | 19.42 |
| SR | 1.99 | 2.46 | 2.75 | 2.85 | 2.14 | 2.15 | 2.57 | 2.51 | 0.77 | 0.53 | 0.64 | 0.52 | 1.23 |
| IR | 1.73 | 2.28 | 2.52 | 2.59 | 1.94 | 1.90 | 2.33 | 2.18 | 0.02 | 0.34 | −0.47 | 0.29 | – |
| Skew | 0.76 | 0.73 | 0.54 | 0.31 | 0.47 | 0.44 | 0.51 | 0.90 | −0.70 | −0.65 | −0.71 | −0.78 | −0.29 |
| Kurt | 3.55 | 3.08 | 2.47 | 2.00 | 2.53 | 2.54 | 2.98 | 3.07 | 3.41 | 1.91 | 4.68 | 2.22 | 4.63 |

**Panel B — Out-of-sample, 2004:07–2022:12 (`T=222`)**

| row | 20% | 40% | 60% | 80% | TOPγ | TOPλ | KNS | RPPCA | FF5 | HKM | MKTB | MKTS | EW |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mean | 22.72 | 25.73 | 27.17 | 27.90 | 20.59 | 23.41 | 20.36 | 23.01 | 5.90 | 7.12 | 8.22 | 8.71 | 17.15 |
| SR | 1.46 | 1.65 | 1.74 | 1.79 | 1.32 | 1.50 | 1.31 | 1.48 | 0.38 | 0.46 | 0.53 | 0.56 | 1.10 |
| IR | 0.98 | 1.24 | 1.38 | 1.46 | 1.40 | 1.37 | 0.85 | 1.07 | −0.27 | −0.26 | −0.04 | −0.21 | – |
| Skew | 0.30 | 0.04 | −0.10 | −0.13 | −0.62 | 0.17 | −1.19 | −0.60 | −1.59 | −0.37 | −0.93 | −0.54 | −1.06 |
| Kurt | 2.39 | 3.59 | 4.06 | 3.77 | 5.77 | 2.38 | 11.97 | 7.74 | 10.60 | 1.51 | (not transcribed) | (not transcribed) | (not transcribed) |

Provenance for the last row: the stripped-text capture of Table 6 ends mid-row at the HKM kurtosis cell (1.51), so the MKTB/MKTS/EW OS kurtosis cells are deliberately left untranscribed rather than guessed → `data gap` in this record.

**Figure 7 (§3.2, caption + prose, pinned v1).** Out-of-sample cumulative value of investing $1, log scale, with returns "scaled to have a constant volatility equal to that of the stock market factor (MKTS)", initial 222-month estimation window, 12-month constant holds: **$174 for the BMA-SDF at the 80% prior versus $71 for RPPCA**, with the source stating the BMA-SDF slope is higher "in virtually any multi-year sub-period".

**Other source-reported results used above:** OOS Sharpe "**approximately 1.8 (80% shrinkage)**" and "all of the BMA-SDF specifications convincingly outperform" EW (§3.2 prose); abstract/§1/§5 "out-of-sample Sharpe ratio of **1.5 to 1.8**"; IS SR range **1.99 to 2.85** with KNS the closest competitor at **2.57** (§3.2); robustness to five alternative corporate-bond datasets (LBFI/BAML bond-level, firm-level, quotes-only, WRDS TRACE, DFPS TRACE) with BMA-SDF "still emerges as the dominant model across all estimations" (§4.4.1); pricing across **16,383 = 2^14 − 1** OS cross-sections (Figure 5 caption) and a **one-million-draw** resampling of cross-sections from **306 anomalies** over **100 sets of test assets** (§4.4.2). These robustness claims were read as prose; the underlying Internet-Appendix tables were not consulted → they remain source-reported, unverified.

### Independently reproduced

**not independently reproduced.** The Scout executed no replication code, no R pipeline, no backtest and no re-estimation. The pinned snapshots and every table cell above were re-read from the primary source on 2026-09-26, but re-reading a table is not reproduction. The official replication package exists at commit `55663cec28848f8875a112190b5a6cb2a5505772` and was **not run**.

**Our own arithmetic checks on printed cells (independent, but not a reproduction of the results):**

1. **Implied annual volatility from `Mean / SR`** across all 13 columns: Panel A = **15.77%–15.94%**, Panel B = **15.48%–15.61%**. This is internally consistent with the stated "normalized to the same volatility as the equity market index" (§3.2), and it means the SR column is invariant to that scaling while the Mean column and any leverage it implies are not.
2. **Figure 7 identity:** `exp(0.2790 × 222/12) = 174.4` and `exp(0.2301 × 222/12) = 70.6` — i.e. **$174 and $71 are exactly the printed OOS Mean columns compounded continuously over 18.5 years with no drag term**. If the Mean column is an *arithmetic* mean of simple returns, a path with σ ≈ 15.6% would compound geometrically to ≈ **$76** (`exp(ln(1.2790) − 0.5 × 0.156²) × 18.5`) and ≈ **$37** for RPPCA; if the Mean column is a *log* mean, Figure 7 is exact as printed. **Which convention the Mean column uses is not stated → `underspecified`.** This is recorded as a provenance ambiguity, not as a claim that the figure is wrong.

### Negative evidence

1. **Zero cost model.** Every cost/fill/borrow/capacity/slippage field is a data gap (see Execution assumptions). The strategy holds 40 factor portfolios, 16 of them corporate-bond legs in a dealer market the source itself describes via matrix pricing and TRACE alternatives, with yearly re-weighting and volatility-scaled leverage whose size is unreported. All Table 6 numbers are gross.
2. **The weakest BMA specification loses out of sample.** Panel B SR: 20% prior **1.46 < TOPλ 1.50** and **< RPPCA 1.48**. So "all of the BMA-SDF specifications convincingly outperform" (§3.2) does not hold against every baseline at every prior.
3. **Information ratio wins only at one grid point.** OS IR: **0.98 / 1.24 / 1.38 / 1.46** for 20/40/60/80% priors against **TOPγ 1.40** and **TOPλ 1.37**. Only the 80% prior (1.46) exceeds both; 40% (1.24) is below both, and 20% (0.98) is well below. Since the benchmark portfolio for IR is EW, this is the cleanest test of "beating 1/N" and it is grid-point-dependent.
4. **Hyperparameter selection uses ex-post information.** The prior Sharpe grid is set at 20–80% of the **ex-post maximum Sharpe ratio of the test assets (5.4)**, and the source states 80% "tends to yield the best out-of-sample performance" (§3.1.1) — selection on the same out-of-sample period used for evaluation. Panel B re-computes the ex-post maximum within each expanding window, which does not remove the look-ahead in choosing the grid.
5. **TOPγ vs TOPλ is internally underdetermined** (see frontmatter `contradictions`): same five factor IDs, both described as using MPRs, materially different reported performance (OOS mean 20.59 vs 23.41).
6. **Baseline asymmetry.** The EW portfolio of the same 40 factors already delivers OS SR **1.10** with mean 17.15% — the source cites DeMiguel et al. (2009) on how hard 1/N is to beat. The BMA-SDF's best OS margin over EW is **+0.69 SR (1.79 vs 1.10)** and it is computed *after* volatility scaling on both sides; whether that margin survives costs is untested.
7. **Unreported leverage and financing.** Vol-scaling to MKTS on a portfolio of 40 factor strategies implies a gross leverage that is never printed; financing costs, margin and stock-loan/bond-borrow costs are absent from a cost model that does not exist.
8. **Short-leg feasibility unaddressed.** Sixteen tradable factors are bond factors and several zoo factors are long-short by construction (e.g. the Betting-Against-Beta construction described in Appendix A). Corporate-bond shorting, dealer inventory and TRACE liquidity are never analysed.
9. **No point-in-time / survivorship treatment.** The 1986 start is justified on price-quality grounds, not availability grounds; CRSP/FISD/LBFI merges are retrospective. Any replication on today's vendor files inherits backfill risk.
10. **No inference and no multiplicity control.** Table 6 reports point estimates only — no Newey-West t-statistics, no block bootstrap, no Diebold–Mariano tests, no confidence intervals for any SR/IR difference, and no adjustment across 4 priors × 13 columns × 2 panels (104 printed performance cells plus Skew/Kurt).
11. **Single market, single OOS window.** US corporates + US equities, one 222-month OOS window (2004:07–2022:12) covering the GFC and COVID — the source calls it "particularly challenging", which is a regime argument in both directions: it is a stress test, but it is also the only test.
12. **Publication status is unverified.** No journal-ref on arXiv; "JFE (Forthcoming)" exists only in the replication README; SSRN returns 403. Preprint-level provenance unless independently confirmed.
13. **Cross-record contrary evidence (equity side).** `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (Chen & Welch, *What Useful Alphas?*, arXiv:2607.06502v1) reports a luck-adjusted near-null for published equity anomalies in the investable large-cap universe post-2005 — directly relevant because **24 of the 40 tradable legs are equity factors** and because the source's own Table 1 says top factors explain only a limited share of squared SDF Sharpe.
14. **Cross-record contrary evidence (implementation net returns).** `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` and `revaluation-alpha-structural-premium-multifactor-allocation-2026-09-25.md` both emphasise that gross factor spreads shrink materially once costs/short-leg frictions are priced — precedent that gross-of-cost factor portfolios of this type can degrade.
15. **Replication package not executed**, so "code exists" is not evidence that the printed cells regenerate.

## Falsification plan

Every threshold below is **research-defined** (acceptance/failure cutoffs chosen by the Scout) or **research-proposed** (operational rules not specified by the source). None of them is source-reported.

- **F1 — Reproduction gate (research-defined).** Run the pinned replication package at commit `55663cec28848f8875a112190b5a6cb2a5505772` (`_run_full_replication.R`, then `ia/_run_ia_full.R`). **Fail** if any of the 13 Panel B SR cells in Table 6 differs from the printed value by more than **±0.05**, or if the run cannot complete on the documented public data bundle. Action on failure: record the record as non-reproducible and stop downstream use of its numbers.
- **F2 — Point-in-time costed replication (research-defined).** Rebuild the 40-leg portfolio with point-in-time membership and a cost ladder of **0 / 5 / 10 / 20 / 30 bp per leg round-trip**, plus a **10% ADV/participation cap** where data permit (corporate bonds: use TRACE-based depth estimates). **Fail** if net OOS Sharpe falls below the source's own EW benchmark (**1.10**) at **10 bp**, or below **0.50** at **30 bp**.
- **F3 — Prior-selection integrity (research-defined).** Fix the prior Sharpe ratio **ex ante** (either a constant 1.0, or selected solely inside the 1986:01–2004:06 training window) and re-run Panel B. **Fail** if the fixed-prior OOS SR is below **TOPλ's 1.50** — i.e. if the headline result depends on the ex-post grid.
- **F4 — Inference on the headline spread (research-defined).** Monthly differential `BMA80 − EW` and `BMA80 − TOPλ`, Newey–West with lag 12 plus a 1,000-draw moving-block bootstrap (block = 12 months). **Fail** if the 95% interval for either differential includes **zero**.
- **F5 — Multiplicity (research-defined).** Benjamini–Hochberg at `q < 0.10` across all 4 priors × 13 columns × 2 panels of Table 6. **Fail** if fewer than **half** of the BMA cells remain significant against EW.
- **F6 — "Lower bound" ablation (research-defined).** Estimate the tradable weights *and* a variant that keeps the 14 non-tradable factors in the estimation while still holding only the 40 tradable legs. **Fail** (claim of direction) if the constrained-40 version retains **less than 80%** of the full-model OOS SR, which would mean exclusion changes results more than the source's "lower bound" framing implies.
- **F7 — Co-pricing / cross-market ablation (research-defined).** Re-estimate (a) joint, (b) bond-only, (c) stock-only BMA-SDFs with identical priors and windows, then trade all three. **Fail** the joint-discipline mechanism if the joint OOS SR does not exceed the **best single-market** variant by **≥ 0.10 SR**.
- **F8 — Treasury-component mechanism test (research-defined).** Repeat §3.3 with duration-adjusted bond returns and the 29 Treasury portfolios. **Fail** the segmentation mechanism if the *stock-only* SDF prices the Treasury component as well as the joint SDF (OOS `R²_GLS` difference **< 0.02** in absolute terms).
- **F9 — Turnover and breakeven cost (research-defined).** Measure realized annual turnover of the 40-leg portfolio under the yearly re-estimation rule (research-proposed metric: `sum|w_t − w_{t-1}|` on the normalized weights, averaged over the OOS window). **Fail** if the implied breakeven round-trip cost is **< 5 bp**.
- **F10 — Regime breakdown (research-defined).** Split OOS into 2004:07–2009:12, 2010:01–2019:12, 2020:01–2022:12. **Fail** if BMA80's SR is below EW's in **2 of 3** sub-periods (the source's "stable in virtually any multi-year sub-period" claim is directly at stake).
- **F11 — Leverage/financing stress (research-proposed estimate).** Infer gross leverage from the volatility-rescaling ratio implied by `Mean/SR` (≈15.6% target) against the unlevered 40-leg portfolio; charge financing at a stated broker rate on `sum|w|`. **Fail** if net SR drops below EW (**1.10**).
- **F12 — Placebo (research-defined).** 1,000 draws of random 5-of-40 factor subsets with the same normalization and windows. **Fail** if BMA80's OOS SR does not exceed the **95th percentile** of the placebo distribution — a check on whether dense averaging beats random subsetting.
- **F13 — Frozen forward window (research-defined).** Extend the sample past 2022:12 with point-in-time data. Require **≥ 60 additional months** with net OOS SR **≥ 1.0 at 10 bp** and positive median annualized excess return. **Fail** if either condition is unmet.

Failure action for all tests: the hypothesis is downgraded in the intake review; no implementation, paper or testnet stage may proceed on the basis of this record.

## Crypto portability

**adapted** — the *mechanism* (Bayesian aggregation over a dense factor zoo, weights from posterior-mean MPRs, annual re-estimation) is market-agnostic and could in principle be re-estimated on a crypto cross-sectional factor zoo (spot and perpetual returns, funding, basis, carry, on-chain flow factors). **This source contains zero crypto evidence**, so nothing here may be read as crypto validation, and the concrete strategy as printed does not port:

- **Spot vs perpetual vs futures:** the 16 bond legs have no crypto analogue; a crypto version would need entirely new factor definitions and a new test-asset set, so `signal construction` would change materially.
- **Funding / mark price / liquidation:** absent from the source entirely (no cost model at all), yet central to any crypto implementation of long-short factor legs on perpetuals.
- **24/7 sessions and candle boundaries:** source is monthly data with a January-style annual cycle; crypto has no session break, so the "yearly rebalance" calendar and the 12-month hold would need a re-thought cadence (research-proposed).
- **Venue fragmentation / survivorship:** a crypto factor zoo inherits listing churn, exchange delistings and vendor backfill — a look-ahead problem the source does not address anywhere.
- **Liquidity and capacity:** corporate-bond-style liquidity constraints simply do not transfer; crypto factor portfolios face exchange-level depth and concentration limits instead, none of which the source models.
- **Stablecoin / quote-currency effects:** not considered by the source → `data gap`.

Net: porting requires re-specification of factors, costs, cadence and feasibility rules; treat any crypto variant as a new hypothesis, not a transfer of this evidence.

## Limitations

- `underspecified`: TOPγ vs TOPλ distinguishing rule (frontmatter contradiction); Mean column arithmetic-vs-log convention (Figure 7 identity, see our count); implied gross leverage; long/short feasibility of the 16 bond legs; per-period weight vectors; tie/ordering rules; monthly signal-to-order convention.
- `data gap`: every transaction-cost, slippage, spread, borrow, margin, funding, participation, impact, fill, capacity and drawdown field; point-in-time availability and revision handling; data-vendor version/vintage for LBFI/ICE/FISD/CRSP; Internet-Appendix tables (not consulted this run).
- `not independently reproduced`: all Table 6, Figure 7 and robustness numbers; the replication package exists at an immutable commit but was never executed by the Scout.
- `unproven`: that the OOS Sharpe advantage over EW/TOPλ/KNS survives costs, financing, leverage reporting, prior choice fixed ex ante, or a post-2022 window; that the joint (co-pricing) estimation is what drives the result; that the "dense SDF" conclusion implies an implementable edge rather than a pricing fit.
- Identification/selection risk: prior grid chosen with ex-post Sharpe information; 80% prior described as best *out of sample* in the source itself; no inference or multiplicity control over 100+ printed cells.
- Sample/regime: one market (US corporates + US equities), one 222-month OOS window, sample ends 2022:12 — roughly three and a half years of unseen data as of this record.
- Capacity: no capacity analysis at all, despite a 40-leg long-short book including corporate bonds.
- Source-quality: preprint (arXiv, no journal-ref); journal-acceptance claim exists only in the authors' own replication README; SSRN landing unverifiable (403).
- Publication-bias: a single paper's own benchmark table, with no independent replication study found in the reviewed material.

## Implementation status

`implementation_status: not-implemented`.

Nothing from this record has been implemented in our research stack: no Qlib full backtest, no production card, no Paper, Testnet or Live run, no strategy family, no Wiki Brain adoption record. The Scout's activity this run was limited to reading the primary source, hashing pinned snapshots, deduplicating the repository, and writing this research record. The official replication package was located and pinned but **not executed**.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. All performance figures above are **source-reported and gross of any cost**, and no later stage may be implied from this record's existence, its evidence count, or its confidence field.

## Related Wiki records

Three Wiki Brain searches were run on 2026-09-26 before writing: `stochastic discount factor SDF factor zoo Bayesian model averaging` → 0 results; `corporate bond factor zoo` → 0 results; `spike and slab prior factor selection shrinkage cross-sectional asset pricing` → 0 results. **No related Wiki Brain page was found, so no Wiki link is asserted and no page is fabricated.** Canonical schema was resolved by reading `quant/strategy-research-record-spec-v1.md` (`sha256 4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`, 10,289 bytes); `quant/strategy-research-record-spec-v2.md` returned "No such file or directory", so **v1 remains canonical** (fail-closed).

Adjacent repository records examined for the four-axis distinction (all with different source identity *and* materially different mechanism/signal/universe):

- `cross-predictive-sdf-cross-asset-spillover-max-sharpe-2026-09-23.md` (Avramov & He, arXiv:2602.20856v1) — ridge-regularized cross-asset spillover SDF estimated on equities; different source, different mechanism (predictive spillover terms vs spike-and-slab model averaging), different signal (max-Sharpe ridge weights vs posterior-mean MPR normalization), no bond cross-section.
- `daily-return-information-factor-drif-elastic-net-cross-sectional-2026-09-23.md` (Cakici et al., SSRN 6005614) — elastic-net mapping of past 21 daily returns to next-month cross-sectional returns; different source, machine-learning return-prediction signal rather than SDF pricing weights, equity-only universe.
- `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` (Chen & Welch, arXiv:2607.06502v1) — a *critique/null* of published equity anomalies, different source, different mechanism (luck adjustment), and cited above as cross-record contrary evidence rather than a duplicate.
- `revaluation-alpha-structural-premium-multifactor-allocation-2026-09-25.md` (Arnott et al., SSRN 5451754) — valuation-decomposition-based factor allocation across 14 US equity long-short factors; different source, timing/allocation mechanism, equity-only universe.
- `option-implied-tvs-sdf-equity-premium-forecast-sp500-2026-09-24.md` — option-implied SDF/equity-premium forecasting; different source, different mechanism (option-implied tail risk) and different universe.

## Sources

- arXiv abs: https://arxiv.org/abs/2604.04430 (v1, submitted Mon, 6 Apr 2026 05:23:01 UTC; read 2026-09-26; no Comments, no journal-ref).
- arXiv pinned HTML: https://arxiv.org/html/2604.04430v1 — 1,099,677 bytes, SHA-256 `d6d9b386223830b72be797e83ec25c3b00da99e27b1c94a54c216bfbca55d987` (retrieved 2026-09-25, re-verified 2026-09-26). All Table 6 cells, Figure 7 values, §3.2 signal text, §1.1–§1.4 sample/universe text, §4.4.1 data-source robustness and the cost-word scan come from this snapshot.
- arXiv pinned PDF: https://arxiv.org/pdf/2604.04430v1 — 3,038,880 bytes, SHA-256 `2bf6fadbb0cb5618aab7dd1104cf95668204bec587e6074c2809d34c9b5263dd` (retrieved 2026-09-25, re-verified 2026-09-26).
- DOI: https://doi.org/10.48550/arXiv.2604.04430 (HTTP 302 → abs, 2026-09-26).
- Replication repository: https://github.com/Alexander-M-Dickerson/co-pricing-factor-zoo at commit `55663cec28848f8875a112190b5a6cb2a5505772` (2026-04-13T03:33:06Z); tree verified 2026-09-26; README at that commit read 2026-09-26 (source of the "JFE (Forthcoming)" and SSRN 4589786 claims).
- SSRN landing cited by that README: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4589786 — HTTP 403 to a scripted client (2026-09-26); not independently verified.
- Companion data site named in the paper: https://openbondassetpricing.com/ (not fetched this run; bundle contents a data gap).
