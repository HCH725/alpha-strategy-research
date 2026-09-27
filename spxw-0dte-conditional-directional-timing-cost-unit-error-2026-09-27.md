---
schema: strategy-research-record-v1
title: SPXW 0DTE Conditional Directional Timing of Seven Multi-Leg Structures, with a Self-Reported Transaction-Cost Unit-Scale Error That Reverses the Net Conclusions
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - 0dte
  - spxw
  - volatility-risk-premium
  - conditional-timing
  - logistic-classifier
  - negative-evidence
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-08-26
sources:
  - "SSRN abstract_id 4641356, DOI 10.2139/ssrn.4641356; landing page read 2026-09-27 at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4641356"
  - "GitHub replication package https://github.com/vilkovgr/0dte-strategies pinned at full commit 85a447c4c155b60143a51c0496641e0f0b892321 (commit date 2026-08-26T20:20:47Z)"
  - "https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/KNOWN-ISSUES.md"
  - "https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/docs/paper/paper-annotated.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Headline conditional numbers are stated three mutually incompatible ways inside one pinned commit: docs/paper/paper-annotated.md line 946 and line 867 print put-ratio expanding gross SR 1.18 / net 0.93, KNOWN-ISSUES.md prints the same cell as moving +0.93 -> -0.75 after the cost fix, and the shipped output/tables/0dte_conditional_oos.tex prints gross 0.77 / net -0.70 for that row. All three are recorded unreconciled."
  - "KNOWN-ISSUES.md states the top-three basket moves from +0.82 to -0.82 after the cost correction, but the shipped output/tables/0dte_conditional_oos_investment.tex still prints net SR 0.82 (gross 1.12), and that file is NOT among the twelve files touched by the pinned cost-fix commit. The -0.82 value does not appear in any shipped table at the pinned commit."
  - "OOS end date is printed four inconsistent ways: SSRN abstract and paper-annotated.md line 774 say 'February 2, 2026', the tab:cond_oos and tab:cond_oos_investment captions say 'through 01/2026', the unconditional table tab:0dte_stratret2024_2026 says '01/2024 to February 2, 2026', and README.md says sample '09/2016 - 01/2026'."
  - "Paper prose at line 593 describes tab:tail_risk_diag ES_1% as 'roughly 0.58-1.58% of underlying' while the shipped 0dte_tail_risk_diagnostics.tex column spans 0.7680-1.6448."
  - "Observation counts differ across shipped tables for the same OOS protocol: 0dte_conditional_oos.tex uses N = 682 / 681 while `0dte_conditional_oos_investment.tex` uses Days = 1060 / 1061; the source does not explain the gap."
  - "SSRN landing page shows a '0 Citations' section heading while its Paper statistics block shows '3 Citations' and 24 References."
---

# SPXW 0DTE Conditional Directional Timing of Seven Multi-Leg Structures, with a Self-Reported Transaction-Cost Unit-Scale Error That Reverses the Net Conclusions

## Provenance

**Paper identity (two titles recorded, unreconciled).**

- SSRN landing page, read 2026-09-27: heading title `0DTE Trading Rules`; author `Grigory Vilkov`, single author, `Frankfurt School of Finance & Management`; `Date Written: December 6, 2023`; `Posted: 1 Dec 2023`; `Last revised: 18 Mar 2026`; `44 Pages`; `JEL Classification: G11, G12, G13, G17`; `Suggested Citation: Vilkov, Grigory, 0DTE Trading Rules (December 6, 2023)`; DOI `10.2139/ssrn.4641356`; abstract URL `https://ssrn.com/abstract=4641356`.
- License line on the landing page: `The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission.` Only printed values, section references and normalized rule descriptions are reproduced here; no source text is copied wholesale.
- Landing-page statistics read 2026-09-27: `DOWNLOADS 7,829`, `ABSTRACT VIEWS 22,823`, `24 References`, Paper statistics `3 Citations`, but the references/citations section headings show `24 References` and `0 Citations`. Both citation readings are recorded, unreconciled.
- The GitHub package README gives the full title `0DTE Trading Rules: Tail Risk, Implementation, and Tactical Timing` and a BibTeX entry `author = {Vilkov, Grigory}, year = {2026}, note = {Working paper, Frankfurt School of Finance & Management}`. The short SSRN title and the long README title are both recorded and are not reconciled.
- Keywords printed on the landing page: `0DTE, ultra-short options, variance risk premium, volatility trading, option strategies, option trading`.

**SSRN PDF status: data gap.** The SSRN PDF for abstract 4641356 was not retrieved in this run (the delivery path resolves to a Cloudflare `Data_Integrity_Notice.cfm?abid=4641356` interstitial and the landing page sits behind a Cloudflare managed challenge on plain HTTP clients). Therefore every page-level claim below is taken from the pinned GitHub text of the paper, not from the SSRN PDF: SSRN-version page count beyond the landing-page `44 Pages`, SSRN-version pagination, and SSRN-version section numbering are `data gap`. The GitHub commit (2026-08-26) postdates SSRN `Last revised: 18 Mar 2026`, so the two versions may differ; the relationship between them is `underspecified`.

**Primary source pinned for this record: GitHub replication package.**

- Repository: `https://github.com/vilkovgr/0dte-strategies`
- Full commit SHA: `85a447c4c155b60143a51c0496641e0f0b892321`
- Commit author/committer: `Grigory Vilkov <vilkov@vilkov.net>`, date `2026-08-26T20:20:47Z`; commit message begins `Fix transaction-cost unit-scale error in bid-ask half-spread`.
- Repository metadata read 2026-09-27 via the GitHub API: created `2026-04-09T00:17:01Z`, `pushed_at 2026-08-26T20:20:57Z` (so the pinned commit was the repository head at read time), default branch `main`, license `MIT` for code; README states the derived data panels are `for academic replication only` and that raw Cboe bar files are proprietary and not redistributed.
- Files pinned and re-hashed locally at read time (bytes / SHA-256):
  - `README.md` - 9,866 / `bdfbd7973191e83cff9127d905d93ca983a4cbddb789a05db534524c6b68122a`
  - `KNOWN-ISSUES.md` - 5,944 / `e1141b5b9aec78ca27c7106fb46351b847c14c612a72ffab21e6386ff79b96d8`
  - `docs/paper/paper-annotated.md` - 77,391 bytes, 1,110 lines / `9c691a913f0907790e95af6e83c2a9c23ad32b50512042b2cccd65df6930cd30`
  - `output/tables/0dte_conditional_oos.tex` - 1,575 / `ac4274a4c9b9990019178b1a7e1f39ef64f3f26a88bdb69b2567c7da67aee7bd`
  - `output/tables/0dte_conditional_oos_investment.tex` - 1,313 / `1a9f61ae5a3046e46b2a42ef53e795e6c462822f391803114057a9b4c96fce97`
  - `output/tables/0dte_implementable_pnl.tex` - 956 / `0ca889829916a91ebdbc9ad12f5929698d3f0bb0e83a0a2945e959087092b556`
  - `output/tables/0dte_tail_risk_diagnostics.tex` - 714 / `b384f1bfbbd529979758fcdf719715a0466234930ad8e971baf6c9c8c2c47cae`
- The pinned cost-fix commit touches exactly twelve paths: `KNOWN-ISSUES.md`, `README.md`, `code/analysis/compute_conditional_oos_protocol.py`, `code/analysis/compute_implementable_pnl.py`, `code/analysis/compute_tail_risk_diagnostics.py`, `code/analysis/cost_units.py`, `data/conditional_oos_protocol_summary.csv`, `output/tables/0dte_conditional_oos.tex`, `output/tables/0dte_implementable_pnl.tex`, `output/tables/0dte_tail_risk_diagnostics.tex`, `tests/reference/tables/0dte_implementable_pnl.tex`, `tests/reference/tables/0dte_tail_risk_diagnostics.tex`. `output/tables/0dte_conditional_oos_investment.tex` is NOT among them.

**Sample and universe (as printed).**

- README.md: `S&P 500 SPXW 0DTE options, September 2016 - January 2026`.
- paper-annotated.md Data section: `Cboe 30-minute option bars with NBBO quotes and sizes, OHLC prices, trade volume, and underlying levels, focusing on SPX Weeklys (root SPXW)`, `European and cash settled against the SPX close at 16:00 ET`, `The sample runs from 09/2016 to 01/2026`; underlying and realized moments from `ThetaData one-minute bars (SPX and VIX)` and ThetaData daily closes; risk-free rate `1-month Treasury bill from FRED`.
- Daily-expiration history as printed: three weekly expiries from late August 2016; two additional weekdays added 2022-04-18 and 2022-05-11.
- The SSRN abstract states the window as `09/2016 to February 2, 2026`. The four inconsistent end dates are listed in `contradictions` above; the exact sample end is a `data gap`.

**Publication / review status.**

- SSRN landing page carries no journal, no issue, and no peer-review statement at read time, so peer-review status is `not stated in source`.
- paper-annotated.md Acknowledgments states the author `used OpenAI Codex with the GPT-5.4 model during manuscript preparation` and that the tool was used partly for `formatting for Financial Analysts Journal`; this is a stated formatting target only, and no submission or acceptance is stated in source.
- Code license MIT; SSRN text `All rights reserved. No reuse allowed without permission.`

**Pre-write source-identity dedup (hidden-inclusive, this run).** `rg -uuu` across the whole repository (3,443 indexed paths, including `.mimo-worktrees/`, `.agents/`, `.hermes/`, `.git/`) returned zero file hits for every one of these identity patterns: `4641356`, `10.2139/ssrn.4641356`, `0DTE Trading Rules`, `Tail Risk, Implementation, and Tactical Timing`, `gex.live`, `victoryg739`, `vilkovgr`, `0dte-strategies`, `conditional_oos_protocol`. `coverage_manifest.csv` (1,088,787 bytes) returned zero hits for `4641356` and for `Grigory Vilkov`. Case-insensitive `vilkov` produced one unrelated hit only: the citation `Buss and Vilkov (2012)` inside `ml-conditional-asymmetric-beta-market-neutral-minvar-hedging-2026-09-25.md`. Adjacent-term scans: `0DTE` matched 23 files and `SPXW` matched 6 files, all of them different source identities (see Related Wiki records). `git log --oneline -20` was used as a convenience glance only and does not satisfy the dedup contract.

## Economic mechanism

### Source-reported

- The paper's own framing (paper-annotated.md Conclusion): a positive 0DTE variance risk premium exists, but `at same-day horizons its economic magnitude is small and difficult to monetize after realistic frictions`; net PNL distributions are `wide, state-dependent, and dominated by tail risk rather than by stable mean carry`; ex-post strategy PNL loads `more on directional and skewness realizations than on realized variance alone`.
- The traded objects are seven unhedged multi-leg templates held to expiration. Source states `All strategies in this paper are unhedged and held to expiration. Their PNL is therefore driven by entry cost and by the realized underlying move from entry to close.` (paper-annotated.md, Conditional Signals section).
- The conditional claim is explicitly narrow: `a narrow set of transparent, auditable signals can improve timing for selected strategy families under disciplined real-time rules`, and the source's own baseline view is that `short-horizon directional predictability in the index is economically weak` (footnote in the Conditional Signals section).
- Stated appropriate use: `a small tactical overlay with explicit turnover control, tail-risk budgeting, and ongoing out-of-sample monitoring, not as a standing core allocation`.
- Stated limitations of scope: `We study SPXW 0DTE positions held to the close, without dynamic intraday hedging and without a causal market-impact design. Our conditioning variables are restricted to information available by 10:00 ET.`
- The most unusual source-reported fact is not a mechanism at all but a self-disclosed defect: the official replication package reports that a transaction-cost unit-scale error had charged the bid-ask half-spread at `1/100 of its true size (about 0.022 bp instead of 2.2 bp)` and that the correction `reverses the sign of the net-of-cost conclusions: no strategy or basket retains a positive net Sharpe ratio` (README.md correction banner and KNOWN-ISSUES.md, both at the pinned commit).

### Research interpretation

- Hypothesized mechanism, falsifiable form: within a single expiration day, the sign of the net PNL of a fixed 0DTE structure is partly predictable from information available at 10:00 ET, because same-day implied-state and lagged realized-state variables proxy the directional/skewness asymmetry that the source's own regressions identify as the dominant PNL driver. This is a directional-classification hypothesis, not a variance-harvesting hypothesis: the classifier never forecasts magnitude, only the sign of `pnl_net`.
- Component roles (per README hybrid structure convention):
  - Regime: none in the benchmark specification. The VIX/0DTE-implied-variance tercile filter exists in the paper but is explicitly `identified ex post (full-sample terciles)`, so it is look-ahead and is not part of the tradable benchmark.
  - Primary signal: per-strategy L2-regularized logistic regression estimating `Pr(pnl_net > 0)` at 10:00 ET from pre-10:00 features, mapped to a full-size direction by `w = sign(p_hat - 0.5)`.
  - Confirmation filter: none.
  - Risk / exit: no stop and no hedge; time exit only, at 16:00 ET expiry. Tail control is delegated to post-hoc ES/drawdown reporting, not to an in-trade rule.
- Mechanism-critical dependency, flagged because it is the record's central negative evidence: the training label is `y = 1{pnl_net > 0}` where `pnl_net` is net of the half-spread plus 0.5 bp cost. The cost model is therefore inside the target, not merely inside the evaluation. KNOWN-ISSUES.md states this explicitly: `Correcting the cost relabels the training data, so the classifier learns a different - and weaker - signal.` A cost bug in this design corrupts both the reported performance and the fitted signal.
- No claim is made that each component contributes alpha; an ablation of features versus lagged-PNL autoregression versus cost-inside-label is not run by the source and would be required to separate them.

## Signal

All items below are source-reported unless explicitly labeled `research-proposed`.

- **Formation timestamp / tradability.** Signal formed at `10:00 ET` on each expiration day, using `only variables observed by 10:00 ET`; the position is entered at that same 10:00 ET reference. Timezone is stated as ET; daylight-saving handling and clock source are `not stated in source`.
- **Universe of traded objects.** Seven structures: `Strangle/Straddle`, `Iron Butterfly/Condor`, `Risk Reversal`, `Bull Call Spread`, `Bear Put Spread`, `Call Ratio Spread`, `Put Ratio Spread` (row labels in the pinned `.tex` tables; panel list A-G in `fig:strat-ret-ts`).
- **Moneyness construction.** The observed 0DTE cross-section is interpolated at each entry time over a moneyness grid `M in {0.98, 0.981, ..., 1.02}` (within +/-2% of ATM), run within option type, then aggregated into strategy legs. For the conditional exercise, exactly one near-ATM configuration per strategy is kept: candidates satisfy `max_l |M_l - 1| <= 0.01`, and the selected configuration is the one with the highest trading-day coverage; all selected configurations lie within +/-0.5% of ATM. The coverage-maximizing selection is an in-sample selection rule (selection on day coverage, not on returns); whether it leaks outcome information is `underspecified`.
- **Entry.** Long/short direction is set by `w = sign(p_hat - 0.5)`, giving `w in {-1, +1}`; realized trading return is `r = w * y_net`. What `w = -1` physically means for each multi-leg template (sell the structure, take the mirror trade, or stand aside) is `not stated in source`; contract counts, order type and tie handling at exactly `p_hat = 0.5` are `not stated in source`.
- **Holding period and exit.** Entered at 10:00 ET, held to expiry at `16:00 ET` (European, cash-settled against the SPX close). No stop, no take-profit, no dynamic intraday hedge, no re-entry rule stated. Alternative entry times examined as separate unconditional exhibits: `16:00 ET on the previous day`, `13:00 ET`, `15:00 ET`.
- **Model and window.** Separate model per strategy, no cross-strategy pooling; L2-regularized logistic; predictors standardized within the training window; estimation at each OOS date uses data through `t-1` only; window rules are expanding and 252-trading-day rolling with a `252 trading-day minimum` burn-in; with that burn-in, `OOS forecasts begin in April 2019`.
- **Feature set (benchmark).** `10:00 ET implied-state variables (IV_t, IS_t, slope_up_t, slope_dn_t)`, where `IV_t` is the VIX-methodology integrated implied variance from 10:00 ET to 16:00 ET on SPXW 0DTE options; `one-day-lagged realized SPX moments`; and lagged strategy-PNL terms `(P^(1), mean P^(5), sigma_P^(5))`. Richer `Baseline / Flow / GEX / Liquidity` stacks are examined only in separate model-zoo exercises, where GEX variables are `flow/exposure proxies based on traded volume, open interest, and leg Greeks rather than a dealer-inventory reconstruction`.
- **Target and cost inside the label.** `y_net = reth_und - c` with `c = (1/2) * spread + 0.5 bp`; binary label written by the paper as `y_{s,t} = 1{PNL^net_{s,t} > 0}` and by KNOWN-ISSUES.md as `y = 1{pnl_net > 0}`; designs compared are (A) return target with `w = sign(y_hat)`, (B1) hard map `w = sign(p_hat - 0.5)`, (B2) soft map `w = 2*p_hat - 1`. The benchmark strategy-level tables use (B1).
- **Position sizing.** No sizing rule is source-reported: all reported PNL is per unit of underlying, `relative to underlying price * 100%`. Notional, capital, leverage, margin, per-day contract caps and the treatment of overlapping positions are `not stated in source`; any sizing rule applied downstream would be `research-proposed`.
- **Reproducibility verdict.** The signal is reconstructable in structure but not in every operational detail: order type, fill reference, sizing, the meaning of `w = -1` per template, and DST/timezone conventions are `underspecified`.

## Required data

- **Instrument / universe:** S&P 500 SPX Weeklys, root `SPXW`, same-expiry 0DTE contracts on weekday expirations; European, cash-settled against the SPX close at 16:00 ET.
- **Venue / market type:** Cboe listed equity-index options (traditional asset, not crypto).
- **Timeframe / fields:** Cboe 30-minute option bars with NBBO quotes and sizes, OHLC, trade volume, underlying levels; ThetaData one-minute SPX and VIX bars; ThetaData daily closes; FRED 1-month Treasury bill for the risk-free rate.
- **Derived fields:** VIX-methodology implied variance and implied semivariance to expiry at each intraday bar-end; `slope_up` / `slope_dn` volatility-surface slope proxies; lagged realized moments; lagged strategy-PNL terms; option-level `bas` (bid-ask half-spread as a fraction of spot), `mid`, `tv`, `reth_und` and `reth` (payoff-minus-mid in percent of spot); Greeks and open interest for the model-zoo feature groups.
- **Point-in-time:** the paper states the slope panel is point-in-time (`slopes.parquet # Volatility surface slopes (point-in-time, intraday)`) and that conditional features are `no-look-ahead`; the one clearly ex-post object is the VIX-regime tercile filter, which the source labels as ex post itself. Train/test boundary: training through `t-1`, OOS from April 2019.
- **Timestamp / timezone:** ET intraday bar-ends; precision, DST handling and out-of-order treatment are `not stated in source`.
- **Missing data:** `not stated in source` for the raw ingest; the README states the shipped derived panels contain all interpolated variables needed to run every exhibit.
- **Data availability constraint (material):** raw Cboe bar files are proprietary and not redistributed; the derived panels ship via Git LFS, and KNOWN-ISSUES.md states `The repository's LFS budget is currently exceeded, so LFS objects can be neither fetched nor updated`, and that `data/conditional_oos_protocol_predictions.parquet` is `Stale`. An independent rerun of the tables is therefore blocked at the pinned commit.

## Execution assumptions

Cost determination is from a Methods-level read of paper-annotated.md sections `Data, Implementation, and Variable Construction`, `Implementability: Execution Costs, Turnover, and Capital Usage`, `Tail Risk and Capital at Risk`, `Strict Out-of-Sample Trading Protocol`, `OOS Portfolio Implementation`, plus the `tab:cond_oos` / `tab:cond_oos_investment` captions, the `README.md` correction banner and the full `KNOWN-ISSUES.md`, plus a word scan of the pinned 1,110-line paper text.

**Source-reported cost model (three layers at entry).**

1. `mid benchmark` - marking at mid, no friction.
2. `bid/ask execution` - each strategy leg pays `half of the observed option bid-ask spread`.
3. `bid/ask plus an additional 0.5 bp slippage-and-fee charge (in underlying-relative PNL units)`.

The conditional tables use `c = (1/2) * spread + 0.5 bp` subtracted `regardless of direction`. Turnover is reported as a `gross entry premium proxy (in basis points of underlying), computed as absolute strategy premium plus half-spread cost` - that is a one-way premium proxy, not a round-trip traded-value turnover and not an ADV participation measure.

**Word-scan evidence for what the pinned paper text does and does not model.** Occurrences in `docs/paper/paper-annotated.md` (1,110 lines): `half-spread` 9, `slippage` 3 (all three referring to the same fixed 0.5 bp charge), `Sharpe` 7, `open interest` 4, `capacity` 2 (both prose: `drawdown capacity` and `higher-capacity nonlinear models`, neither a capacity model). Zero occurrences: `market impact`, `latency`, `ADV`, `exchange fee`, `SEC fee`, `TAF`, `clearing`, `partial fill`, `queue`, `participation`, `maker`, `funding`.

Therefore, and never as zero: per-contract exchange/SEC/TAF/clearing fees `data gap`; latency and signal-to-order delay `data gap`; order type and fill model beyond the mid/bid-ask reference `data gap`; partial fills, queue position and order rejection `data gap`; market impact and participation/ADV capacity `data gap`; borrow, margin and financing `data gap` (structures are unlevered per-unit-of-underlying payoffs, but no margin rule is stated); liquidation `not applicable as stated` (European cash-settled index options, no liquidation engine described) with margin-call treatment `data gap`. The source explicitly concedes `without dynamic intraday hedging and without a causal market-impact design`.

**The cost defect (source-reported, decisive).**

- KNOWN-ISSUES.md, section `2026-08 - Transaction-cost unit-scale error (FIXED in code; paper being revised)`: the panel stores `bas`, `mid`, `tv` as a fraction of spot and `reth_und`, `reth` as percent of spot; the cost code combined them directly, so `The bid-ask half-spread was therefore charged at 1/100 of its true size - about 0.022 bp instead of 2.2 bp - while the fixed 0.5 bp fee was correctly scaled`; the same pattern `appeared in the conditional protocol, so the conditional tables inherited it`.
- Independent confirmations listed by the source: `reth_und == 100 * (payoff - mid)` holds exactly; `bas * spot` implies a mean dollar spread of about $1.33 (plausible for SPXW 0DTE) whereas reading `bas` as percent implies $0.013, below the minimum tick; `option_strats_uncond_analysis.py` already multiplied `bas`/`mid`/`tv` by 100, so the codebase was internally inconsistent.
- Reported by `the team at gex.live, who reproduced the shipped implementable_pnl table to four decimal places on all seven structures before diagnosing the unit inconsistency`.
- A second, earlier defect: section `2026-05 - Sign error in transaction costs on short days (FIXED)` - `dir_pnl_net = sign * pnl_net` added costs instead of subtracting them when `sign = -1`; reported by `Victor Yoong (victoryg739)` in `issue #1`; acknowledged in a footnote to `tab:cond_oos`.
- A third, related scale error in the same review: `turnover_proxy` mixed `mid` (fraction) with `half_spread_cost`, and the column labeled `Turnover (bps)` was actually in percent; both fixed.
- Regression guard added: `code/analysis/cost_units.py` provides `assert_percent_of_spot_scale()`, called by all three cost paths.
- Scope note on the model zoo: `compute_conditional_model_zoo.py`, `derive_binary_decision_summary.py`, and the `anchor_zoo` path of `compute_conditional_oos_investment_ts.py` use a flat `--net-cost 0.005` (0.5 bp) that `excludes the bid-ask half-spread entirely`; because the half-spread averages about 2.2 bp, those `net` figures `understate realistic cost by roughly 5x and should be read as an upper bound`. This is a documented modeling choice, not the unit bug - but it means model-zoo `net` numbers are not comparable with the main `B/A+0.5bp` numbers.

**Artifact state declared by the source.** Refreshed: analysis code, `output/tables/*`, `tests/reference/tables/*`, `data/conditional_oos_protocol_summary.csv`. Stale: `data/conditional_oos_protocol_predictions.parquet` and the Git LFS data panels. In progress: `the paper PDF and the AI-context documents under docs/`. Note that `output/tables/0dte_conditional_oos_investment.tex` is not in the pinned commit's touched-file list despite the blanket `output/tables/*` wording - see `contradictions`.

## Evidence

### Source-reported

Every figure below is source-reported, third-party, and has not been reproduced by us. Each carries the pinned file and row/column identity.

**Unconditional implementable PNL at 10:00 ET** - `output/tables/0dte_implementable_pnl.tex` @ `85a447c`, means in % of underlying, `Obs` column as printed:

| Structure | Mean Mid | Mean B/A | Mean B/A+0.5bp | SR Mid | SR B/A+0.5bp | Turnover (bps) | ES_1% | Mean/ES_1% | Obs |
|---|---|---|---|---|---|---|---|---|---|
| Strangle/Straddle | -0.0059 | -0.0165 | -0.0215 | -0.27 | -0.97 | 24.097 | 1.6092 | -0.013 | 953 |
| Iron Butterfly/Condor | -0.0073 | -0.0324 | -0.0374 | -0.56 | -2.67 | 31.012 | 0.7865 | -0.048 | 953 |
| Risk Reversal | 0.0157 | 0.0074 | 0.0024 | 0.65 | 0.10 | 2.667 | 1.6448 | 0.001 | 953 |
| Bull Call Spread | -0.0101 | -0.0418 | -0.0468 | -0.35 | -1.59 | 79.114 | 1.0673 | -0.044 | 953 |
| Call Ratio Spread | -0.0140 | -0.0494 | -0.0544 | -0.55 | -2.11 | 74.949 | 1.3273 | -0.041 | 953 |
| Bear Put Spread | 0.0138 | -0.0159 | -0.0209 | 0.48 | -0.73 | 62.903 | 0.9221 | -0.023 | 952 |
| Put Ratio Spread | 0.0251 | -0.0092 | -0.0142 | 1.06 | -0.61 | 57.397 | 0.7680 | -0.018 | 952 |

Cross-check: KNOWN-ISSUES.md's `Turnover` claim that entry turnover goes `from an apparent 0.24 bp to a true 24 bp for a two-leg strangle` matches the printed `24.097` for Strangle/Straddle.

**Cost-fix before/after on the shipped 2024-05-01 panel** - `KNOWN-ISSUES.md` table, source-reported, not independently reproduced: Put Ratio Spread `+1.06 / +0.84 -> -0.61`; Risk Reversal `+0.65 / +0.44 -> +0.10`; Bear Put Spread `+0.48 / +0.30 -> -0.73`; Strangle/Straddle `-0.27 / -0.51 -> -0.97`; Iron Butterfly/Condor `-0.56 / -0.96 -> -2.67` (SR mid / SR net before / SR net after). Source conclusion: `No structure retains a materially positive net Sharpe ratio.` The after-column matches `0dte_implementable_pnl.tex` exactly for all five rows.

**Tail diagnostics** - `output/tables/0dte_tail_risk_diagnostics.tex` @ `85a447c`, daily net PNL in % of underlying under B/A+0.5bp: ES_1% spans `0.7680` (Put Ratio) to `1.6448` (Risk Reversal); Max DD spans `7.946` (Risk Reversal) to `52.124` (Call Ratio); Worst day spans `-0.9560` (Put Ratio) to `-2.8356` (Risk Reversal); Worst 5-Day spans `-2.9267` to `-7.7681`; Loss Prob spans `48.7` (Iron) to `69.9` (Strangle/Straddle) percent; Skewness ranges `-1.00` (Iron) to `+2.71` (Risk Reversal); `Obs` 952-953.

**Conditional OOS protocol, strategy level** - `output/tables/0dte_conditional_oos.tex` @ `85a447c`, logistic benchmark, representative moneyness, `w = sign(p_hat - 0.5)`, OOS April 2019 onward. Selected rows (Hit Rate %, Brier, Calib. Slope, Mean Gross bps, SR Gross, Mean Net bps, SR Net, N):

- Put Ratio Spread, Expanding: `65.1, 0.221, 1.01, 1.556, 0.77, -1.405, -0.70, 681`
- Put Ratio Spread, Rolling: `65.2, 0.223, 0.70, 1.862, 0.93, -1.100, -0.55, 681`
- Strangle/Straddle, Expanding: `68.5, 0.214, 0.18, 1.014, 0.33, -0.889, -0.29, 682`
- Strangle/Straddle, Rolling: `68.5, 0.214, 0.19, 2.126, 0.69, 0.222, 0.07, 682`
- Iron Butterfly/Condor, Expanding: `65.4, 0.220, 0.74, 0.353, 0.65, -3.162, -4.13, 682`
- Risk Reversal, Expanding: `67.9, 0.221, 0.30, 2.012, 0.48, 0.108, 0.03, 682`
- Call Ratio Spread, Expanding: `59.2, 0.250, 0.17, -1.410, -0.60, -4.218, -1.69, 682`
- Bull Call Spread, Expanding: `60.1, 0.241, 0.32, 0.736, 0.56, -1.391, -1.04, 682`
- Bear Put Spread, Expanding: `64.6, 0.231, 0.10, 0.100, 0.07, -2.137, -1.52, 681`

Net SR is positive in only two of the fourteen printed rows, and neither exceeds `+0.07`: `Strangle/Straddle Rolling` (`+0.07`) and `Risk Reversal Expanding` (`+0.03`).

**Conditional OOS portfolio implementation** - `output/tables/0dte_conditional_oos_investment.tex` @ `85a447c`, 252-day rolling window: `Equal-weight basket (Top 3 by Mean PNL)` and `(Top 3 by SR)` both print `Mean Gross 1.875 bps, SR Gross 1.12, Mean Net 1.361 bps, SR Net 0.82, Hit 68.5, Long Share 42.5, ES_1% -122.18 bps, Worst Day -207.64 bps, Max DD -530.56 bps, Days 1061`; `Equal-weight basket (All)` prints `0.740, 0.81, 0.224, 0.25`; the best single row, Put Ratio Spread, prints `1.975, 0.96, 1.455, 0.71, 64.2, 31.2, -153.23, -354.21, -574.46, 1060`. This file is not in the cost-fix commit's touched list - see `contradictions`.

**Paper prose that disagrees with the shipped tables** - `docs/paper/paper-annotated.md` @ `85a447c`: line 946 `put ratio spreads reach a gross SR of 1.18 (0.93 net) in Table [tab:cond_oos]`; line 947 `the top-three basket reaches a gross SR of 1.12 (0.82 net)`; line 867 `gross SR of 1.18 (0.93 net) in the expanding specification`; line 868 `Strangle/straddle structures remain positive (SR gross 0.56, net 0.39)`; line 869 `Iron butterfly/condor structures show a positive gross SR of 0.77 but turn negative after costs (-0.20)`; line 593 ES_1% `roughly 0.58-1.58% of underlying`. None of these prose values except the basket `1.12 / 0.82` matches the shipped `.tex` tables at the same commit.

**Inference robustness (drivers regressions only).** Section `Inference Robustness: Date Clustering and Multiple Testing` reports pooled regressions with combo fixed effects, date-clustered standard errors and `Benjamini-Hochberg FDR control (BenjaminiHochberg1995)` following `HarveyLiuZhu2015`; the source states `the strongest directional-skew links remain after clustering and BH adjustment, while many weaker coefficients lose support`. This BH adjustment applies to the PNL-driver regressions, not to the conditional timing tables.

**Regime filter.** Section `A Simple State Filter at 10:00 ET: VIX Regimes (Ex-Post Cutoffs)` sorts days by `full-sample terciles of the 10:00 ET 0DTE implied-variance measure`; the source concedes `Regime thresholds are therefore identified ex post (full-sample terciles), while the state variable itself is observed ex ante at entry`. Reported direction: downside-oriented structures earn higher mean PNL in high-VIX states, call spreads better in low-VIX states, with `statistical strength remains limited for most strategies in this static design`.

### Independently reproduced

not independently reproduced

### Negative evidence

1. The source itself reports that its cost model was wrong by a factor of 100 on the bid-ask half-spread, and that the fix `reverses the sign of the net-of-cost conclusions` (README.md banner, KNOWN-ISSUES.md).
2. After the documented fix, `No structure retains a materially positive net Sharpe ratio` on the shipped unconditional panel (KNOWN-ISSUES.md); the shipped `0dte_implementable_pnl.tex` confirms: only Risk Reversal stays positive under B/A+0.5bp, at `+0.10`.
3. Only two of the fourteen conditional rows in `0dte_conditional_oos.tex` have positive net SR, `+0.07` (Strangle/Straddle, Rolling) and `+0.03` (Risk Reversal, Expanding); the other twelve range from `-0.29` to `-4.13`.
4. The headline conditional numbers are stated three incompatible ways for the same cell (gross 1.18 / net 0.93 in prose, +0.93 -> -0.75 in KNOWN-ISSUES, gross 0.77 / net -0.70 in the shipped table).
5. The claimed basket reversal `+0.82 -> -0.82` (KNOWN-ISSUES) is not present in any shipped table; the shipped investment table still prints `+0.82`, and that file was not touched by the cost-fix commit.
6. Calibration slopes in `0dte_conditional_oos.tex` range `0.10` to `1.01`; a calibrated probability model should have slope near 1, so most rows are severely under-confident or mis-scaled, and hit rates of `58.1-68.5` % coexist with Brier scores of `0.211-0.251` against a base rate that the table never prints.
7. Hit rate is a weak diagnostic here: Strangle/Straddle has the tied-highest printed hit rate (`68.5`) while its expanding net SR is `-0.29`.
8. The training label embeds the cost, so any cost correction changes the fitted signal; the source states that rescaling cost only at evaluation `will get a more favorable number than the one reported here`.
9. Model-zoo and `anchor_zoo` `net` figures exclude the half-spread entirely and therefore understate realistic cost by roughly 5x (KNOWN-ISSUES scope note), so any model-zoo comparison in the source is an upper bound.
10. The shipped `conditional_oos_protocol_predictions.parquet` is stale and the Git LFS data panels cannot be fetched because the LFS budget is exceeded, so no independent rerun is possible at the pinned commit.
11. A second, earlier cost bug added costs on short days instead of subtracting them (2026-05 section), meaning the table history contains at least two independent cost defects found by outside parties.
12. A third scale defect affected the reported turnover column, which was labeled `bps` while printing percent.
13. All three cost defects were found by external replicators (`gex.live` for the half-spread unit-scale error and the `turnover_proxy` scale error, `victoryg739` for the short-day sign error), not by the repository's own tests - despite `tests/test_replication.py` running byte-parity checks against `tests/reference/tables/`, a reference set produced by the same pipeline and therefore incapable of detecting a wrong-but-consistent cost model.
14. Observation counts are inconsistent across the two conditional tables for the same stated protocol (`682/681` versus `1060/1061`).
15. The OOS end date is printed four different ways across the abstract, prose, captions and README.
16. Tail risk dominates mean: ES_1% of `0.7680` to `1.6448` % of underlying against mean B/A+0.5bp PNL between `-0.0544` and `+0.0024` % of underlying; `Mean/ES_1%` is negative for six of seven structures in `0dte_implementable_pnl.tex` and only `+0.001` for the seventh.
17. Worst-day outcomes of `-0.9560` to `-2.8356` % of underlying and Max DD up to `52.124` % of underlying, with loss probabilities `48.7-69.9` %.
18. `Bull Call Spread` shows the largest turnover proxy (`79.114` bps) with a negative SR at every cost layer - turnover with no edge.
19. The source's own statement that `short-horizon directional predictability in the index is economically weak` undercuts the economic story for a sign-prediction target.
20. No significance test, t-statistic, p-value, confidence interval or multiple-testing control is attached to any conditional OOS Sharpe in the shipped tables; BH adjustment appears only for the drivers regressions.
21. The representative-moneyness configuration is chosen by maximum day coverage, an in-sample selection whose leakage properties are not analyzed.
22. The VIX regime filter uses full-sample terciles, which is look-ahead by the source's own admission.
23. No capacity, latency, market-impact, partial-fill, exchange-fee, SEC-fee, TAF, clearing, borrow, margin or financing model exists anywhere in the pinned paper text (word-scan counts above); every one of those fields is `data gap`, never zero.
24. The paper concedes `without dynamic intraday hedging and without a causal market-impact design`, and that live use should be `a small tactical overlay` only.
25. The meaning of `w = -1` for each multi-leg template, the order type, the fill reference and any sizing rule are `not stated in source`, so the printed Sharpe ratios cannot be mapped to an executable book without assumptions.
26. The SSRN PDF could not be retrieved, so the SSRN-version text cannot be checked against the GitHub text; the two versions have different dates (2026-03-18 versus 2026-08-26) and may differ.
27. SSRN landing-page citation counts are internally inconsistent (`0 Citations` heading versus `3 Citations` in paper statistics).

## Falsification plan

All thresholds below are `research-defined falsification thresholds`, not source-reported. Data for all tests: the pinned package at commit `85a447c4c155b60143a51c0496641e0f0b892321`, plus a frozen forward window starting `2026-10-01` (`research-proposed` date). Action on failure for every test: the record stays `research-only` and no production candidate-pool entry is proposed.

- **F1 - Frozen forward replication.** Re-run the conditional protocol on data from 2026-10-01 forward only, with all rules frozen. Failure rule: forward net SR below `0.30` over at least 12 months, or a forward net SR whose 95% block-bootstrap interval includes zero.
- **F2 - Decisive cost adjudication (+0.82 versus -0.82).** Rebuild `pnl_net`, the binary label and the investment table from the corrected cost path and adjudicate the basket net SR. Failure rule: the reproduced basket net SR is negative, or differs from either printed value (`+0.82`, `-0.82`) by more than `0.10`.
- **F3 - Cost ladder.** Re-evaluate all seven structures under half-spread multipliers `{0, 1, 2, 3, 5}` and fixed add-ons `{0, 0.5, 1, 2, 5}` bp. Failure rule: any structure's net SR falls below zero at the source's own stated average half-spread (`2.2 bp`), or net SR erodes by more than `50%` between the 0 and 1 rungs.
- **F4 - Missing-cost completion.** Add per-contract exchange, SEC, TAF and clearing fees, one round-trip per trade, using published Cboe/SEC/TAF schedules as of the trade date. Failure rule: the additional friction removes the positive net SR of the only surviving structure (Risk Reversal, `+0.10`).
- **F5 - Label-rebuild consistency.** Rebuild `y = 1{pnl_net > 0}` under each cost rung and measure label agreement with the shipped labels. Failure rule: agreement below `90%`, which would confirm that reported performance is inseparable from the cost model.
- **F6 - Leakage audit.** Verify point-in-time construction of `slopes`, `future_moments_*`, the representative-moneyness selection and the rolling/expanding standardization. Failure rule: any feature that uses information after 10:00 ET of day `t`, or any selection step that uses returns rather than coverage.
- **F7 - Ex-post regime removal.** Replace the full-sample tercile VIX filter with expanding-window terciles. Failure rule: the reported regime ordering (downside structures better in high-VIX) reverses or becomes insignificant.
- **F8 - Holdout selection control.** Re-run the coverage-maximizing representative-moneyness choice inside each training window only. Failure rule: performance drops by more than `50%` versus the printed full-sample choice.
- **F9 - Placebo / shuffled-label test.** Circular-shift or sign-shuffle the labels 1,000 times and re-run the full protocol. Failure rule: observed net SR does not exceed the 95th percentile of the placebo distribution.
- **F10 - Competing-explanation baseline.** Compare against (a) always-long-the-structure, (b) always-short, (c) a no-skill 50/50 coin rule, (d) an AR(1) on lagged strategy PNL alone. Failure rule: the logistic benchmark fails to beat the best simple baseline by at least `0.10` net SR.
- **F11 - Ablation of the hybrid.** Ablate (i) implied-state features, (ii) lagged realized features, (iii) lagged PNL terms, (iv) cost-inside-label (replace the label with `1{pnl_gross > 0}`). Failure rule: removing any single group changes net SR by more than `0.30`, or the cost-inside-label ablation alone explains the gross-net gap.
- **F12 - Inference and multiplicity.** Attach Newey-West or date-clustered inference to every conditional Sharpe and apply Benjamini-Hochberg at `q < 0.10` across the 7 structures x 2 windows x all examined target designs. Failure rule: no row survives.
- **F13 - Regime / subperiod stability.** Split the OOS window into three contiguous subperiods and repeat the pre-2022 versus post-2022 daily-expiry expansion split. Failure rule: net SR sign is unstable across subperiods for every structure.
- **F14 - Reproducibility gate.** With LFS restored, reproduce all four shipped tables from source. Failure rule: any headline cell differs from the pinned `.tex` by more than `0.01` in Sharpe or `0.5` bps in mean PNL.

## Crypto portability

`adapted`

The source contains zero crypto evidence: the sample is Cboe SPXW equity-index options, European and cash-settled, traded only on weekday sessions 09:25-16:00 ET. Porting this hypothesis to crypto would be a ported hypothesis, not crypto empirical evidence. Specific obstacles:

- **No 0DTE equivalent with comparable structure.** Crypto options on Deribit/Bybit/Binance are mostly 0-1-2-7-14-30-60-90 day expiries with far thinner same-day liquidity, so the `10:00 ET to 16:00 ET` same-expiry horizon does not have a clean counterpart; daily 0DTE BTC/ETH contracts exist but with far smaller open interest and wider spreads.
- **Session structure.** 24/7 trading means there is no 16:00 settlement boundary; the `held to expiry against the index close` payoff must be replaced by a funding-settlement or mark-price convention, which changes the label `y = 1{pnl_net > 0}` fundamentally.
- **Cost regime.** The record's central lesson is that the half-spread was mis-scaled by 100x in index options with a ~$1.33 mean dollar spread. Crypto perp/option spreads are wider, venue-specific, and regime-dependent, so a `2.2 bp` average assumption cannot be carried over at all.
- **Derivatives type.** The traded object is listed multi-leg option structures; crypto requires single-venue option chains or cash-settified equivalents, with different exercise style (American versus European varies by venue), contract multipliers and index definitions.
- **Mark / index price, funding, liquidation.** Crypto adds mark-index divergence, funding on any hedging perpetual leg, liquidation and ADL rules, and venue fragmentation - none of which appear in the source.
- **Timestamps.** ET intraday bar boundaries, DST and the 09:25 open do not align with crypto candle boundaries; point-in-time reconstruction must be re-specified.
- Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: order type, fill model, sizing, leverage/margin, the operational meaning of `w = -1` per template, re-entry, DST/timezone conventions, and the base rate behind the reported hit rates.
- `data gap`: per-contract exchange/SEC/TAF/clearing fees, latency, market impact, participation/ADV capacity, partial fills, queue position, borrow/financing, and every SSRN-PDF-level detail (page count beyond the landing-page `44 Pages`, pagination, section numbering of the SSRN version).
- `not stated in source`: peer-review/journal status, code and data availability statement inside the paper text, and any statistical inference attached to the conditional OOS Sharpe ratios.
- `not independently reproduced`: every performance figure in this record. No rerun was possible because the Git LFS panels cannot be fetched at the pinned commit.
- Source-internal contradictions (six listed in the frontmatter) are recorded, not reconciled; a downstream reviewer must pick a canonical table before quoting any conditional number.
- Sample-end ambiguity (four printed dates) means the exact OOS window is a `data gap`.
- Publication-bias and selection concerns: the representative-moneyness choice, the reported two-window comparison and the absence of multiplicity control over the conditional table family.
- Capacity: no analysis exists; the largest printed turnover proxy (`79.114` bps for Bull Call Spread) is a premium proxy, not traded value, so real capacity is unknown.
- This record captures a research hypothesis plus decisive negative evidence; it does not assert that the mechanism is absent, only that the source's own net conclusions are not currently usable.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack. No Qlib full backtest, no NautilusTrader change, no Paper, Testnet or Live run, and no production card has been produced. The record exists only as normalized research material in the public staging pool.

## Adoption boundary

Presence of this record in this repository does not mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

Verified pages returned by `kb_search` at write time (no page is fabricated):

- [[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]] - nearest neighbour: same SPXW 0DTE underlying, but a different source identity (Wysocki, arXiv:2608.24786) and a different mechanism (cross-sectional learning-to-rank over the option surface to harvest the variance risk premium) versus this record's per-strategy time-series binary direction timing plus cost-defect negative evidence.
- [[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12]] - VRP falsification, but crypto variance-swap estimators, different market and different source identity.
- [[quant/single-name-equity-earnings-iv-crush-bid-ask-falsification-2026-09-13]] - shares the quoted-spread-versus-modelled-cost theme in equity options, different universe, horizon and source identity.
- [[quant/crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13]] - options-implied conditioning for short-horizon prediction, crypto DVOL, different mechanism and source identity.

Adjacent repository records that were located by the `0DTE` / `SPXW` scans and are explicitly not duplicates of this source identity: `spxw-0dte-vrp-learning-to-rank-2026-09-01.md`, `morning-vvix-1000-est-variance-asset-conditional-long-short-ssrn-6212458-2026-09-26.md` (the closest mechanism neighbour - a 10:00 ET conditioning rule, but on variance-asset instruments under a different SSRN source), `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12.md`, `option-funding-basis-year-end-boundary-wedge-spx-rut-box-implied-2026-09-22.md`. Four-axis distinction: mechanism (per-strategy logistic sign timing of fixed 0DTE structures), signal construction (`w = sign(p_hat - 0.5)` on 10:00 ET implied-state plus lagged-PNL features), universe/market type (Cboe SPXW listed index options), and material data dependency (NBBO half-spread feeding both the cost and the training label) all differ from each of the four records above, and every source identity differs.

## Sources

- Vilkov, Grigory. `0DTE Trading Rules`. SSRN abstract 4641356, DOI 10.2139/ssrn.4641356. Landing page read 2026-09-27: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4641356 (title `0DTE Trading Rules`, Posted 1 Dec 2023, Last revised 18 Mar 2026, 44 Pages, Date Written December 6, 2023, JEL G11/G12/G13/G17, `All rights reserved. No reuse allowed without permission.`).
- `vilkovgr/0dte-strategies` replication package, pinned at full commit `85a447c4c155b60143a51c0496641e0f0b892321` (2026-08-26T20:20:47Z, MIT code license): https://github.com/vilkovgr/0dte-strategies/tree/85a447c4c155b60143a51c0496641e0f0b892321
- Same commit, `README.md`: https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/README.md
- Same commit, `KNOWN-ISSUES.md`: https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/KNOWN-ISSUES.md
- Same commit, `docs/paper/paper-annotated.md`: https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/docs/paper/paper-annotated.md
- Same commit, `output/tables/0dte_implementable_pnl.tex`: https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/output/tables/0dte_implementable_pnl.tex
- Same commit, `output/tables/0dte_tail_risk_diagnostics.tex`: https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/output/tables/0dte_tail_risk_diagnostics.tex
- Same commit, `output/tables/0dte_conditional_oos.tex`: https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/output/tables/0dte_conditional_oos.tex
- Same commit, `output/tables/0dte_conditional_oos_investment.tex`: https://github.com/vilkovgr/0dte-strategies/blob/85a447c4c155b60143a51c0496641e0f0b892321/output/tables/0dte_conditional_oos_investment.tex
- External defect reports cited by the source: `gex.live` (2026-08 cost unit-scale error) and Victor Yoong `https://github.com/victoryg739` issue `https://github.com/vilkovgr/0dte-strategies/issues/1` (2026-05 short-day cost sign error).
