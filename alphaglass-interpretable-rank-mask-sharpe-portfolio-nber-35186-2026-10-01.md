---
schema: strategy-research-record-v1
title: "AlphaGlass Interpretable Rank-and-Mask Sharpe-Optimal Characteristic Portfolio (NBER Working Paper 35186)"
created: 2026-10-01
updated: 2026-10-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-05-11
sources:
  - https://www.nber.org/papers/w35186
  - https://www.nber.org/system/files/working_papers/w35186/w35186.pdf
  - https://doi.org/10.3386/w35186
  - https://doi.org/10.2139/ssrn.6691958
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Appendix F prose (Section 4.1 follow-on) states the AlphaGlass out-of-sample Sharpe ratio of 0.43 is 'slightly lower than the SR of 0.54 for the full sample that includes small stocks', but Table 2 Panel B reports the full-sample out-of-sample 10-1 Sharpe ratio as 0.47 and 0.54 is the Table 2 Panel A in-sample figure; the immediately following sentence about the neural net and EBM uses out-of-sample baselines (0.34 and 0.30), so the two readings are not internally consistent."
---

# AlphaGlass Interpretable Rank-and-Mask Sharpe-Optimal Characteristic Portfolio

## Provenance

Primary pinned source (the only source of every number in this record):

- NBER Working Paper **35186**, title **"AlphaGlass: Interpretable Characteristic-Based Portfolio Choice"**, DOI **10.3386/w35186**, NBER issue date **May 2026** (landing `citation_publication_date` 2026/05/11).
- Author block, page-1 title block order exactly as printed: **Sebastian Bell; Ali Kakhbod; Martin Lettau; Abdolreza Nazemi**. Cover affiliations: Karlsruhe Institute of Technology School of Economics and Management (Bell); University of California, Berkeley Haas School of Business (Kakhbod); University of California, Berkeley Haas School of Business and CEPR and also NBER (Lettau); Karlsruhe Institute of Technology (Nazemi).
- JEL classification as printed on the abstract page: C14, C45, G10, G11, G12.
- Publication status from the pinned PDF cover: "NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications." Cover also prints "The authors have nothing to disclose." and a copyright notice (2026, all rights reserved; short sections not exceeding two paragraphs may be quoted with credit), so this record cites and normalizes rather than reproduces. Crossref record for 10.3386/w35186: `type` report, publisher National Bureau of Economic Research, `created` 2026-05-11, `published` 2026-05, `container-title` empty (no journal), `relation` empty, `is-referenced-by-count` 0, indexed 2026-09-19. **Working paper, not peer reviewed, no journal reference.**
- Pinned artefacts fetched 2026-10-01 over HTTPS:
  - PDF `https://www.nber.org/system/files/working_papers/w35186/w35186.pdf` -> HTTP 200, **764622 bytes**, SHA-256 `9e42ccad387791f7af0b7a6d0ae9f739681d8cfc208a5897abf82d3b39360830`, `%PDF-1.6`, **97 pages** by pypdf 6.16.2, PDF dictionary `/CreationDate D:20260504045615Z` and `/ModDate D:20260505215511-04'00'`, producer xdvipdfmx (20250410). Extracted text layer **221312 characters / 251122 bytes / 5535 lines**, SHA-256 `14805ef9368cb28cbb020fb2b6107cb064beb1392351b3e222b29514c8adf6c3`, read end to end: cover, abstract, Sections 1 to 9, Equations (1) to (27), Tables 1 to 7 with every printed cell, Figures 1 to 10 with captions, the full reference list, and Appendices A (A.1 to A.4), B, C, D, E, F, G, H, I, J, K (K.1, K.2).
  - Landing `https://www.nber.org/papers/w35186` -> HTTP 200, **87881 bytes**, used only for `citation_title`, the four `citation_author` values, `citation_doi`, `citation_publication_date 2026/05/11`, `citation_technical_report_number w35186` and `citation_pdf_url`. The landing carries no revision-date row.
  - Crossref `https://api.crossref.org/works/10.3386/w35186` -> HTTP 200, 1788 bytes.
- Secondary identity surface (dedup aid, **not** a number source): DOI **10.2139/ssrn.6691958**, same four authors. Crossref `https://api.crossref.org/works/10.2139/ssrn.6691958` -> HTTP 200, 31652 bytes: `type` posted-content, `group-title` SSRN, publisher Elsevier BV, `created` 2026-05-02, `posted` 2026, `reference-count` 112, `is-referenced-by-count` 0. The SSRN HTML landing itself returned **HTTP 403 ("Content Blocked")** on 2026-10-01, so the SSRN PDF was never fetched and **equivalence between the SSRN and NBER PDF byte streams was not verified (data gap)**; every empirical field in this record comes from the NBER PDF only.
- No code, repository, seed, or data-availability statement exists in the pinned PDF (`github` 0, `source code` 0, `code avail` 0 occurrences in the pinned text layer).
- Pre-write source-identity dedup (2026-10-01): ripgrep across **all `*.md` files in the whole checkout including hidden trees** (`.mimo-worktrees/`, `.agents/`, `.hermes/`) plus `coverage_manifest.csv` for `AlphaGlass`, `10.3386/w35186`, `w35186`, `Interpretable Characteristic-Based Portfolio`, `Abdolreza Nazemi`, `rank-and-mask` -> **0 files**; a positive control on `novy-marx` returned hits, confirming the search space was live. `git log --oneline -20` was read only as a convenience glance and does not satisfy dedup. `git pull origin main` returned `Already up to date` before research.

## Economic mechanism

### Source-reported

The source's claim is a **construction claim, not a new premium**: the return spread it reports is produced by a learned score over pre-existing firm characteristics, and the paper's own thesis is that optimizing the investor's objective end-to-end inside an interpretable class generalizes better than predict-then-sort.

- **Signal layer.** A Generalized Additive Model with sparse pairwise interactions maps 91 cross-sectionally ranked characteristics to one score: `s(l,t) = beta0 + sum_i theta_i * f_i(x_i) + sum_{i>j} gamma_ij * f_ij(x_i, x_j)` (Eq. 7/8). Each `f_i` and `f_ij` is a small feed-forward net (main effect: 1 input, one hidden layer of 20 units, 1 output, ReLU; interaction: 2 inputs, two hidden layers of 20 units each, 1 output, ReLU), so every portfolio decision decomposes exactly into term-level contributions.
- **Portfolio layer.** The score is converted to weights by a differentiable **rank-and-mask** layer: pairwise logistic comparisons `S(l,l',t) = sigmoid((s_l - s_l')/tau_s)` give a soft rank `rank = 1 + sum_{l' != l} S`; with `k_t = floor(n_t / M)` and `M = 10`, soft masks `mH = sigmoid((rank - rank_{n-k+1})/tau_m)` and `mL = sigmoid((rank_k - rank)/tau_m)` select the top and bottom decile, each leg is normalized to sum to one, and `wHL = wH - wL`.
- **Objective layer.** Steps (2) to (6) are solved jointly by minimizing `L = -SR(fHL)` plus L1 gates on main effects and interactions (Eq. 9). The source explicitly contrasts this with the three-step pipeline that minimises MSE of predicted returns and only afterwards evaluates a Sharpe ratio (Section 2, Eq. 1 versus Eqs. 2 to 6).
- **Stated economic drivers (Section 4.4, Figure 6).** Monotonically decreasing `herf` (industry sales concentration), monotonically increasing `pchsale_pchxsga` (sales growth less SG&A growth), monotonically increasing and convex `mom12m` (12-month momentum excluding the most recent month), monotonically decreasing `chempia` (industry-adjusted employee change); plus one dominant interaction, `acc x hire` (working-capital accruals conditioned on employee growth), whose conditional surface is positive only when accruals are low.
- **Stated theory.** Theorem 1 soft-hard equivalence (soft weights are exponentially close to the hard sort under a positive signal margin, and the two Sharpe ratios coincide as temperature goes to zero); Theorem 2 argmax-consistency of the sample Sharpe ratio within the AlphaGlass class; Theorem 3 an oracle inequality for the out-of-sample Sharpe ratio in terms of blocked Rademacher complexity, `b/T` and a beta-mixing concentration term; Theorem 4 that, given a risk-free asset and mean-variance preferences, the optimal portfolio rule is a Sharpe-ratio maximizer.

### Research interpretation

Falsifiable restatement (research interpretation, not a source claim): **the cross-sectional long-short decile spread on an end-to-end Sharpe-optimized, sparse-interpretable characteristic score should survive out-of-sample, survive costs, and beat the same architecture trained on MSE return prediction.** The proposed mechanism class is cross-sectional mispricing plus limits-to-arbitrage harvested through nonlinear characteristic interactions and volatility-aware ranking, executed as a monthly dollar-neutral 10-1 sort. Roles: **rank-and-mask layer** = tradability/portfolio-formation component (not alpha by itself); **additive score with sparse interactions** = signal; **Sharpe-ratio loss** = objective that substitutes for a separate risk model. This is a ported US cash-equity hypothesis; it is **unproven** outside the source's own sample and is **not** crypto empirical evidence.

## Signal

- **Formation timestamp.** Cross-section formed monthly at time `t`; characteristics are lagged relative to returns so that returns in month `t` match monthly characteristics at the end of month `t-1`, quarterly data by the end of `t-5`, and the most recent annual data by the end of `t-7` (Section 3, source-reported). Timezone, calendar convention, and the exact signal-to-order delay are **not stated in source** (data gap).
- **Tradability.** Weights `w(l,t)` are functions of the signals at `t` and returns are `f(t+1)` (Section 2, Eqs. 3 to 5). Appendix A.4 states the trading decision is made once per rebalancing date using the information set available at that date, all names are ranked and weighted simultaneously, and realized portfolio return is evaluated from the weighted aggregation of next-period returns. Whether fills occur at the month-`t` close, the next session open, or a monthly VWAP is **underspecified** (data gap).
- **Lookback.** Each of the 91 characteristics carries its own lookback, defined in Appendix B (Table B.1) and inherited from Green et al. (2017) / Gu et al. (2020); for example `mom12m` is the past year excluding the most recent month (source-reported). Endpoints and warm-up rules for the panel are not further specified; the panel is cross-sectionally ranked to `[0,1]` each month (Section 3).
- **Long entry.** Top soft-ranked decile, `k_t = floor(n_t/10)` names, weight `wH_l = mL-normalized soft mask / sum`, so the long leg sums to 1 (source-reported, Section 2.2).
- **Short entry.** Bottom soft-ranked decile, weight `wL` likewise normalized to sum to 1; `wHL = wH - wL` gives a dollar-neutral book with gross exposure 2 (source-reported; footnote 6 states "fixed gross exposure, preserving dollar neutrality").
- **Exit / holding period / re-entry.** Monthly re-formation: the 10-1 portfolio is recomputed at every month `t` and held for one month (source-reported from the monthly sort in Sections 2 and 3). No stop, no take-profit, no time-based exit, no re-entry rule exists in the source; **absence is source-reported, not a Scout choice**.
- **Position sizing.** Equal-weight-within-leg in the hard evaluation the tables describe ("ten equal-weighted portfolios", Table 2/3/E.1/F.1/G.1 notes); training uses the soft-normalized weights above. An Appendix E alternative (demean scores, divide by the cross-sectional L1 norm, unit gross exposure) is reported separately.
- **Parameters (source-reported).** `M = 10` deciles; `k_t = floor(n_t/M)`; main-effect subnet width 20, interaction subnets two layers of width 20; ReLU; three-stage training (main effects, then screened interactions, then joint fine-tuning at a lower learning rate); L1 gate penalties `lambda_main`, `lambda_inter`; heredity-constrained FAST interaction screening keeping the top `K` pairs (Lou et al., 2013); tolerance-`rho` pruning path on the validation loss; early-stopping threshold tuned on validation; mini-batches built from complete months.
- **Parameters NOT printed in source (underspecified / data gap).** The numeric values of `tau_rank`, `tau_mask` used during training, `lambda_main`, `lambda_inter`, `K`, `rho`, learning rates, epoch caps, early-stopping tolerance, and batch-month count are never printed. Figure 1 uses `tau_rank = 0.1` and `tau_mask = 0.5` **for an illustrative 200-stock toy example only** and must not be read as the fitted training values.
- **Reproducibility verdict.** The rule is **partially specified**: architecture, objective, portfolio formation and lag conventions are reconstructible; fitted hyperparameters, weights, code and the baseline calendar split boundaries are not.

## Required data

- **Instrument / universe.** Monthly US common-equity returns from **CRSP**, restricted to the three major US exchanges **NYSE, NASDAQ, AMEX** (Section 3, source-reported). Observations with unavailable return or market-cap data are removed, yielding **1,656,664 observations** over **January 2000 to December 2021**. No CRSP share-code filter, no exchange screen beyond the three venues, and no liquidity/price screen are stated (**data gap**).
- **Fields.** 91 firm characteristics from **Green et al. (2017) as provided by Gu et al. (2020)**, merged from CRSP and Compustat, cross-sectionally ranked to `[0,1]` each month (Section 3 and Appendix B, source-reported). `compustat` appears once and `crsp` five times in the pinned text layer; no alternative data, no text data, no order-book data.
- **Market type / venue / timeframe.** Cash equities, monthly bars, US three-exchange trading; no derivatives, no futures, no options, no crypto.
- **Point-in-time.** Only the stated publication lags (monthly `t-1`, quarterly `t-5`, annual `t-7`) are given. The phrases `point-in-time`, `look-ahead`, `survivorship` and `delisting` occur **0** times in the pinned text layer; delisting returns, corporate-action handling, and revision handling are **not stated in source** (data gap).
- **Timestamp.** Monthly CRSP period convention; timezone, clock source and out-of-order handling are **not stated in source** (data gap).
- **Missing data.** Rows lacking return or market-cap are dropped; any other missing-value treatment (median fill, winsorization, clipping) is **not stated in source** (data gap).
- **Funding / fee / spread needs.** Not addressed anywhere in the source (see the census in Execution assumptions): **data gap**, must never be read as zero.

## Execution assumptions

Cost/friction treatment was determined at Methods level from Sections 2, 3, 4.1 to 4.5, 6, 8.1, 9, Appendix A.4 ("execution protocol of a cross-sectional equity strategy"), Appendices D, E, F, G, J, all seven table captions, all ten figure captions, and a whole-document case-insensitive substring census of the pinned 251122-byte / 5535-line text layer (references and appendices included):

- `transaction cost` **0**, `trading cost` **0**, `slippage` **0**, `commission` **0**, `market impact` **0**, `latency` **0**, `order type` **0**, `limit order` **0**, `market order` **0**, `maker` **0**, `taker` **0**, `participation` **0**, `fill` **0**, `net of cost` **0**, `net-of-cost` **0**, `after cost` **0**, `gross of` **0**, `backtest` **0**, `win rate` **0**, `funding` **0**, `short sale` **0**, `short-sell` **0**, `short sell` **0**, `point-in-time` **0**, `look-ahead` **0**, `survivorship` **0**, `delisting` **0**, `share code` **0**, `github` **0**, `source code` **0**, `limitation` **0**.
- Non-cost hits that must not be misread: `bid-ask` **2** (one reference-list title, Amihud and Mendelson 1989; one Appendix B characteristic, `baspread Bid-ask spread`); `fee` **1** and `fees` **0** (the single hit is inside the word "feed-forward"); `borrow` **1** (the phrase "secured borrowing" in the Section 5.1 interpretation, not short-book borrow); `turnover` **3** (all three inside Appendix B variable definitions: `chatoia` asset turnover, `std_turn` share turnover, `turn` share turnover - **no strategy turnover is reported**); `execution` **1** (Appendix A.4 protocol sentence); `rebalanc` **1** (same sentence); `gross exposure` **2** (footnote 6 and Appendix E); `cost` **12** (overhead costs, "computationally costly", training cost, "zero-cost portfolio" in the theory, and one reference title); `spread` **11** (portfolio/return spreads and `baspread`); `capacity` **6** (model capacity, debt capacity, capacity-constrained portfolios); `leverage` **14** and `margin` **16** (leverage characteristics, theory leverage, "marginal", and the `pchgm_pchsale` gross-margin characteristic); `liquidity` **10** (liquidity characteristics and the Appendix C category).
- **Conclusion of the census: every trading-friction field is a data gap and must never be read as a modeled zero.** The source models no cost, no spread, no borrow, no funding and no fill, so every printed mean, standard deviation and Sharpe ratio is **gross of all trading frictions**, and the paper carries no gross-versus-net label anywhere (`gross of` 0).
- Signal-to-order timing: once per monthly rebalance date (Appendix A.4). Order type, fill model, latency, fees, spread, slippage, impact, participation cap, leverage/margin, borrow availability and partial-fill handling: **not stated in source** (data gap). The short leg is assumed implementable with no shortability or locate discussion (`short sale` 0).
- Capacity: **not stated in source** (data gap). Statistical treatment of the reported Sharpe ratios: `newey` **0**, `bootstrap` **0**, `t-stat` **0**, `p-value` **0**, `significant` **1** (only for the Figure 10 cross-sectional regression), `confidence interval` **2** (only for regression bands) - no inference is attached to any portfolio Sharpe.
- Multiplicity: `benjamini` **0**, `bonferroni` **0**, `multiplicity` **0**, `deflated` **0**, `walk-forward` **0**.
- Scout-added operational choices, all **research-proposed** and not source-reported: cost ladder values in F3/F4, turnover cap in F5, HAC lag in F10, BH `q` in F11, placebo tolerance in F12, temperature/K grids in F13, the frozen forward window in F14, and every failure cutoff in the falsification plan (all **research-defined falsification thresholds**).

## Evidence

### Source-reported

All figures below are **source-reported**, taken from the pinned NBER PDF at the stated table/figure/section, US cash equities, monthly, gross of all costs, and **not independently reproduced**.

Headline (Section 4.1 and Table 2, AlphaGlass, 10-1 decile portfolio):

- **Table 2 Panel A (in-sample, training + validation)**: mean **1.87**, S.D. **3.44**, SR **0.54**.
- **Table 2 Panel B (out-of-sample, test sample)**: mean **1.10**, S.D. **2.35**, SR **0.47**. Section 4.1 text: "The monthly Sharpe ratio of the high/low portfolio is 0.47 (1.62 p.a.)". The source does not print the annualization formula; `0.47 * sqrt(12) = 1.63` (research-computed), consistent with rounding.
- **Table 2 Panel B decile SRs (columns 1 to 10)**: 0.08, 0.15, 0.25, 0.22, 0.21, 0.23, 0.24, 0.22, 0.23, 0.24.

Benchmarks (Table 3, same MSE-loss predict-then-sort pipeline):

- **RF out-of-sample 10-1**: mean 0.62, S.D. 4.33, SR **0.14** (in-sample SR 0.75).
- **Neural net out-of-sample 10-1**: mean 0.90, S.D. 2.67, SR **0.34** (in-sample SR 0.67).
- **EBM out-of-sample 10-1**: mean 1.35, S.D. 4.52, SR **0.30** (in-sample SR 0.78).

Robustness tables:

- **Table 1** (value-weighted univariate characteristic sorts): best in-sample SR 0.30 (`pchcurrat`); the text names only `chcsho` (0.235) and `pchsale_pchrect` (0.196) as holding up out of sample, printed as 0.24 and 0.20 in Panel B; `mvel1` falls to 0.00.
- **Table 4** out-of-sample SR by size quintile (Small, 2, 3, 4, Big): AlphaGlass **0.31 / 0.40 / 0.33 / 0.25 / 0.27**; RF 0.28 / -0.01 / 0.05 / 0.10 / 0.01; NN 0.32 / 0.19 / 0.11 / -0.01 / 0.02; EBM 0.46 / 0.11 / 0.18 / -0.02 / 0.04.
- **Table F.1** (bottom size quintile excluded, out-of-sample): AlphaGlass 10-1 mean 0.98, S.D. 2.29, SR **0.43**; RF 0.01; NN 0.12; EBM 0.13.
- **Table G.1** (15-year train 1/2000-12/2014, 2-year validation 1/2015-12/2016, 5-year test 1/2017-12/2021): out-of-sample 10-1 mean 1.24, S.D. 2.55, SR **0.49**; in-sample SR 0.59 (Section 4.1 text: "0.49").
- **Table 6** maximized mean-variance utility (x100), out-of-sample: gamma=1 AlphaGlass **1.12**, EBM 0.99, NN 0.86, RF 0.53 (in-sample 1.81 / 7.88 / 3.51 / 8.56); gamma=3 AlphaGlass **1.23**, EBM 0.87, NN 0.79, RF 0.34 (in-sample 1.43 / 6.70 / 3.21 / 7.48).
- **Table D.1** Sharpe-optimal combination of characteristic-sorted long-short portfolios, out-of-sample SR for k = 3, 5, 10, 45, 91: **0.060 / 0.123 / 0.002 / 0.032 / 0.062** against in-sample 0.341 / 0.460 / 0.520 / 0.800 / 1.089.
- **Table E.1** alternative full-cross-section (demean + L1) objective: out-of-sample 10-1 SR **0.352** (in-sample 1.218).
- **Table J.1** drawdown-penalized objective (lambda_DD = 100): out-of-sample SR AlphaGlass **0.302**, RF 0.143, NN 0.338, EBM 0.299; the drawdown term is near zero only for AlphaGlass (0.003).

Interpretability numbers:

- **Figure 3** mean absolute scores: `herf` **1.78**, `pchsale_pchxsga` **1.54**, `mom12m` and `chempia` both around **0.86**; the `acc x hire` interaction is the only interaction in the top 15.
- **Figure 5** leave-one-term-out: removing `maxret` or `mom12m` lowers the out-of-sample SR from **0.47 to 0.41**.
- **Section 4.4**: estimated signals have mean **0.74**, standard deviation **6.06**, interquartile range **(-4.38, 4.98)**.
- **Figure 10** regressions inside the legs: `hire` on `acc` in portfolio 1 coefficient **0.54 (t = 11.4)**, in portfolio 10 **-0.38 (t = -3.3)**.
- **Section 5.1** directional mean scores: long leg led by `herf` **S+ = 2.42**; short leg led by `sin` **|S-| = 5.60**, then `pchsale_pchxsga` **2.57**, `divi` **2.01**, `realestate` **1.55**, `herf` **1.04**.

Simulation (Section 8, Table 7; not market data): 100 replications, n = 500 assets, p = 6 characteristics, common correlation 0.25, `mu_sig = 0.018`, `log sigma^2 = (-4.6) + 2.5*u2 + 1.2*(u3-0.5)^2`, training lengths T = 120 and 240 months, evaluation on an independent 1000-month population sample:

- **Panel A oracles** (annualized SR): weighting **2.995 (0.116) / 2.982 (0.118)**, ranking **2.388 (0.107) / 2.368 (0.120)**, mean **2.047 (0.123) / 2.021 (0.105)** for T = 120 / 240.
- **Panel B**: AlphaGlass **1.774 (0.340) / 1.970 (0.226)**, EBM 1.568 / 1.755, Neural net 1.449 / 1.557, Random Forest 1.411 / 1.438.
- **Panel C** fraction of ranking-oracle SR: AlphaGlass **0.743 / 0.834**, EBM 0.658 / 0.742, RF 0.591 / 0.608, NN 0.607 / 0.659.
- **Panel D** fraction of mean-oracle SR: AlphaGlass **0.867 / 0.977**, EBM 0.767 / 0.869, RF 0.689 / 0.711, NN 0.709 / 0.771.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **No cost model of any kind.** The Methods-level census returns `transaction cost` 0, `trading cost` 0, `slippage` 0, `commission` 0, `market impact` 0, `bid ask` 0 - every reported return and Sharpe ratio is gross with no gross/net label.
2. **No strategy turnover is reported.** The only `turnover` hits (3) are Appendix B characteristic names; cost feasibility of a book that re-forms monthly and re-sorts 91 characteristics is therefore unknown.
3. **No borrow, shortability or locate analysis.** `short sale` 0, `short-sell` 0, and the single `borrow` hit is the phrase "secured borrowing" in prose; the short leg of a 10-1 sort over the whole NYSE/NASDAQ/AMEX panel is assumed free and available.
4. **No statistical inference on any portfolio Sharpe ratio.** `newey` 0, `bootstrap` 0, `t-stat` 0, `p-value` 0; the only inferential statistics in the paper are the Figure 10 cross-sectional regression t-statistics (11.4 and -3.3).
5. **No multiple-testing control** across 91 characteristics, a screened interaction space and four objective variants: `benjamini` 0, `bonferroni` 0, `multiplicity` 0, `deflated` 0.
6. **No walk-forward or rolling refit.** `walk-forward` 0; footnote 7 notes Gu et al. (2020) refit every 12 months and states the results are "not directly comparable", so the headline is one fixed 10/2/10 split.
7. **The baseline calendar boundaries of the 10-year / 2-year / 10-year split are never printed.** Only the alternative split dates (Appendix G: 1/2000-12/2014, 1/2015-12/2016, 1/2017-12/2021) are given; the main split windows are a **data gap**.
8. **Internal inconsistency (contested).** Appendix F prose benchmarks the 0.43 out-of-sample SR against "0.54 for the full sample", but Table 2 Panel B's full-sample out-of-sample SR is 0.47 and 0.54 is the in-sample Panel A value, while the parallel neural-net/EBM sentence uses out-of-sample baselines.
9. **Sample ends December 2021** - `1,656,664` observations stop at 2021-12; nothing from 2022 onward exists in the pinned source.
10. **Preprint only.** NBER working paper, explicitly not peer reviewed, `container-title` empty in Crossref, `is-referenced-by-count` 0 as of 2026-09-19; no journal, acceptance or forthcoming string anywhere in the PDF.
11. **No code, no seed, no data release**: `github` 0, `source code` 0, `code avail` 0; fitted hyperparameters (`lambda_main`, `lambda_inter`, `K`, `rho`, training `tau_rank`/`tau_mask`, learning rates, epochs) are never printed, so the reported model cannot be rebuilt from the paper.
12. **Objective variants degrade.** The drawdown-penalized fit falls to out-of-sample SR 0.302, below the neural net's 0.34 (Table J.1), and the full-cross-section objective falls to 0.352 (Table E.1); the headline 0.47 is the best of four objectives, which is selection across variants with no correction.
13. **The comparison confounds objective with architecture.** AlphaGlass uses a Sharpe-ratio loss while RF, NN and EBM all use MSE (Section 4), so the reported gain is partly an objective-function comparison; the interpretable EBM under MSE already reaches 0.30.
14. **The strongest simple benchmark collapses out of sample.** Table D.1's Sharpe-optimal combination of characteristic sorts goes from in-sample SR 1.089 (k = 91) to out-of-sample 0.062, direct in-source evidence that in-sample Sharpe fitting in this panel does not generalize.
15. **Inputs themselves decay.** Table 1 shows the best univariate characteristic SR falling from 0.30 in-sample to 0.08 out-of-sample for `pchcurrat`, 0.26 to 0.10 for `pchquick`, and 0.22 to 0.00 for size (`mvel1`).
16. **The headline is not a large-cap result.** Table 4 shows AlphaGlass's big-quintile SR at 0.27 versus 0.47 headline, and every benchmark's non-smallest-quintile factor sits near zero.
17. **No universe hygiene is documented.** `share code` 0, `survivorship` 0, `delisting` 0, `point-in-time` 0, `look-ahead` 0 - delisting returns, corporate actions, and any share-code or exchange screen beyond "three major US exchanges" are unstated.
18. **No capacity or liquidity constraint.** `market impact` 0, `participation` 0; `baspread` and `zerotrade` exist only as model inputs, never as execution filters.
19. **Risk-free rate source for the "excess return" input is not stated** (`risk-free rate` appears once, inside the Section K theory, not in the data section).
20. **The simulation is deliberately favorable.** Section 8's DGP is designed so the Sharpe-optimal score depends on both mean and characteristic-dependent volatility, contains no market frictions, and reports only annualized Sharpe ratios - it is not market evidence.
21. **No robustness to market or venue.** `crypto` 0, `bitcoin` 0, `ethereum` 0, `perpetual` 0, `futures` 0, `etf` 0 - nothing about any market other than US monthly cash equities.
22. **No limitations section and no threats-to-validity discussion**: the word `limitation` appears 0 times in the pinned text layer.

## Falsification plan

All thresholds below are **research-defined falsification thresholds** and all operational choices are **research-proposed**; none is source-reported. Each gate has a Fail condition and an Action.

- **F1 Printed-value reproduction.** Data: CRSP + the 91 Gu et al. (2020) characteristics. Fail if the Table 2 Panel B out-of-sample 10-1 Sharpe ratio cannot be reproduced to within +/- 0.01. Action: treat the record's numbers as unusable and downgrade to a reproducibility-gap note.
- **F2 Baseline split reproduction.** Fail if a faithful 10-year / 2-year / 10-year split over January 2000 to December 2021 yields an out-of-sample 10-1 SR below 0.35. Action: mark the headline as non-reproducible in our stack.
- **F3 One-way cost ladder.** Fail if the out-of-sample 10-1 SR is non-positive at 20 bps one-way, or below 0.15 at 50 bps one-way (research-proposed ladder: 0 / 5 / 10 / 20 / 50 bps applied to a research-proposed monthly turnover estimate). Action: reclassify as a cost-insensitive artifact, not an alpha candidate.
- **F4 Two-way cost plus borrow gate.** Fail if SR < 0.10 under 30 bps one-way on both legs plus a research-proposed 100 bps per month borrow fee on the short leg. Action: reject the short-leg component and re-test long-only, or drop.
- **F5 Turnover gate.** Fail if monthly one-way turnover of the 10-1 book exceeds 100% (research-defined). Action: re-specify with an explicit turnover penalty inside the loss and re-run the one-way cost ladder gate.
- **F6 Untouched forward window.** Freeze every fitted choice and evaluate 2022-01 through 2026-12. Fail if the forward 10-1 SR < 0.20. Action: mark the effect as sample-bound.
- **F7 Rolling-refit stability.** Fail if a 12-month rolling refit flips the sign of the 10-1 mean in more than one third of the years. Action: mark the rule unstable to refit timing.
- **F8 Objective ablation.** Train AlphaGlass with MSE loss and train EBM with the Sharpe-ratio loss. Fail if the AlphaGlass-minus-strongest-baseline SR gap falls below 0.05 (research-defined). Action: attribute the reported gain to the objective, not to the rank-and-mask interpretability claim.
- **F9 Size / liquidity split.** Fail if the out-of-sample SR in the top size quintile is below 0.15. Action: restrict the claim to small/mid caps and record the capacity ceiling.
- **F10 Inference gate.** Fail if a Newey-West t-statistic with 12 lags (research-proposed) on the monthly 10-1 return is below 2.0. Action: report as statistically unconfirmed.
- **F11 Multiplicity gate.** Apply Benjamini-Hochberg at q < 0.10 (research-proposed) across all four objectives, three split variants, size splits and the univariate panel. Fail if the headline specification is not in the surviving set. Action: mark as selection-contaminated.
- **F12 Placebo gate.** Permute the cross-sectional characteristic-to-return mapping within each month. Fail if the placebo SR reaches 50% or more of the reported 0.47 (research-defined). Action: reject the mechanism reading and keep only a null result.
- **F13 Hyperparameter-sensitivity gate.** Vary `tau_rank` in {0.05, 0.1, 0.5, 1.0} and interaction budget `K` in {10, 25, 50} (research-proposed grid, all else frozen). Fail if the resulting out-of-sample SR range spans 0.20 or more. Action: mark the result as hyperparameter-fragile and require a pre-registered grid.
- **F14 Frozen forward cohort.** From 2026-10-01, run a frozen configuration for at least 36 months with no re-tuning. Fail if the cumulative mean is non-positive or the SR < 0.30. Action: close the candidate as falsified.

**Global no-retuning rule.** Every gate above freezes the 91-characteristic panel, the Green/Gu lag conventions (monthly t-1, quarterly t-5, annual t-7), the `[0,1]` cross-sectional rank transform, `M = 10`, the leg-sum-one normalization, the monthly re-formation, the additive-plus-sparse-interaction architecture, subnet widths 20/20/20, the three-stage training order, the FAST heredity screen, the L1 gates, the `-SR` loss, the 10/2/10 split and the CRSP three-exchange universe. Any deviation restarts the gate rather than rescuing it.

## Crypto portability

**adapted, performance unproven.**

The pinned text layer contains `crypto` 0, `bitcoin` 0, `ethereum` 0, `perpetual` 0, `futures` 0, `etf` 0 occurrences: the source demonstrates nothing outside US monthly cash equities. Porting notes (research interpretation):

- **Mechanism maps only partially.** A cross-sectional monthly rank-and-mask long-short layer is mechanically transposable to a crypto top-N spot or perpetual panel, but 91 of the inputs are CRSP/Compustat accounting fields (accruals, SG&A growth, employee change, book equity) with **no crypto analogue**; only the price/volume/liquidity subset (`mom12m`, `mom6m`, `turn`, `dolvol`, `baspread`, `retvol`, `maxret`) ports.
- **24/7 sessions** break the monthly CRSP bar, the t-1/t-5/t-7 lag convention and the "one decision per rebalancing date" assumption; timestamp and candle-boundary conventions must be redefined.
- **Funding, mark/index price, liquidation and ADL** are entirely absent from the source and are first-order in perpetuals - all are **data gaps** to be modeled, not inherited.
- **Venue fragmentation and survivorship** (delistings, rug pulls, exchange failures) are unstated in the source and are the dominant new bias when porting.
- **Borrow** for the short leg is unstated in the source and differs sharply between marginable majors and long-tail alts.

Crypto portability is not authorization to trade.

## Limitations

- **underspecified**: fitted hyperparameters, baseline split calendar boundaries, execution timing, order type, fill model, risk-free rate source, universe share-code screen, missing-data treatment beyond dropping rows lacking return or market cap.
- **data gap**: all transaction-cost, spread, slippage, commission, borrow, funding, capacity and latency fields; turnover; statistical inference on Sharpe ratios; delisting and survivorship handling; any post-2021 evidence; SSRN-versus-NBER version equivalence (SSRN landing returned HTTP 403 on 2026-10-01 and its PDF was not fetched).
- **not independently reproduced**: every performance number in this record is source-reported.
- **unproven**: the out-of-sample 0.47 monthly Sharpe is a single-split, gross-of-cost, no-inference result on a sample ending 2021-12 from a non-peer-reviewed working paper; nothing here establishes that it persists after costs, after 2022, or in any other market.
- **selection**: four objective variants, three split variants and size splits are reported; the headline is the maximum of that family with no correction (see F11).
- **incremental-write threshold / dedup**: this is a new source identity and a materially distinct mechanism (end-to-end portfolio-objective optimization through a differentiable rank-and-mask layer) relative to existing records, not a reframing of one; no existing record covers DOI 10.3386/w35186.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no AlphaGlass training run, no reconstruction of the 91-characteristic panel, no portfolio simulation, no Qlib backtest, no Paper/Testnet/Live stage. The only work performed for this record was source retrieval, primary-source reading, deterministic dedup, and normalization.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the repository means only that normalized research material entered the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not strategy adoption, implementation authorization, or permission to run Paper/Testnet/Live.

## Related Wiki records

- [[quant/equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02]] - also cross-sectional US equity ML ranking; different architecture and different signal construction (dependence-graph ranking rather than Sharpe-optimized additive rank-and-mask).
- [[quant/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05]] - US equities ML ensemble signal-quality filtering; different source, different mechanism (graph clustering plus ensemble quality gating).
- [[quant/size-enhanced-left-side-momentum-resga-expected-shortfall-2026-09-04]] - cross-sectional equity factor interaction; different source and different signal (size x left-side momentum), listed because size and momentum are two of AlphaGlass's leading terms.

Pre-write Wiki Brain searches (read-only, `kb_search`) were run for "interpretable machine learning portfolio construction Sharpe ratio characteristic", "explainable boosting machine glass box equity return prediction" (0 results), "differentiable sorting rank mask portfolio weights" (0 results) and "cross-sectional equity anomaly machine learning factor timing"; only the three verified paths above were returned, and no Wiki Brain page was written.

## Sources

- https://www.nber.org/papers/w35186 (NBER landing page; title, four authors, DOI, issue date May 2026, technical report number, PDF URL; fetched 2026-10-01, HTTP 200, 87881 bytes)
- https://www.nber.org/system/files/working_papers/w35186/w35186.pdf (pinned primary PDF; 764622 bytes, SHA-256 9e42ccad387791f7af0b7a6d0ae9f739681d8cfc208a5897abf82d3b39360830, 97 pages, read end to end; fetched 2026-10-01, HTTP 200)
- https://doi.org/10.3386/w35186 (Crossref record for the NBER working paper: type report, publisher NBER, created 2026-05-11, no container-title, no relation)
- https://doi.org/10.2139/ssrn.6691958 (secondary identity surface for dedup; Crossref posted-content in group SSRN, publisher Elsevier BV, created 2026-05-02, reference-count 112, same four authors; SSRN HTML landing returned HTTP 403 on 2026-10-01 and its PDF was not pinned)
