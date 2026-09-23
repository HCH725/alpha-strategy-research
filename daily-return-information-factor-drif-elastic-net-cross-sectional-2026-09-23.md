---
schema: strategy-research-record-v1
title: "Daily Return Information Factor (DRIF): Elastic-Net Mapping of the Past 21 Daily Returns to Next-Month Cross-Sectional Equity Returns"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - short-horizon-reversal
  - elastic-net
  - factor-zoo
  - us-equity
  - multiverse-analysis
status: research-only
confidence: medium
source_as_of: "2026-05-04"
sources:
  - "Nusret Cakici, Christian Fieberg, Gabor Neszveda, Robert Bianchi, Adam Zaremba, 'A Unified Framework for Anomalies Based on Daily Returns', SSRN abstract 6005614, DOI 10.2139/ssrn.6005614; posted 7 Jan 2026, last revised 4 May 2026; PDF version dated May 4, 2026. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6005614"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Daily Return Information Factor (DRIF): Elastic-Net Mapping of the Past 21 Daily Returns to Next-Month Cross-Sectional Equity Returns

## Provenance

- **Primary source (read in full this run):** Nusret Cakici, Christian Fieberg, Gabor Neszveda, Robert Bianchi, Adam Zaremba, *"A Unified Framework for Anomalies Based on Daily Returns."* SSRN abstract ID **6005614**, DOI **10.2139/ssrn.6005614**. SSRN landing: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6005614 (posted 7 January 2026; last revised 4 May 2026; 59 pages; 122 references as listed on the landing page). PDF delivery URL: https://papers.ssrn.com/sol3/Delivery.cfm/6005614.pdf?abstractid=6005614&mirid=1
- **Author list exactly as the primary PDF title page:** *Nusret Cakici, Christian Fieberg, Gabor Neszveda, Robert Bianchi, Adam Zaremba* (SSRN landing renders the fourth author as "Robert J. Bianchi"). Affiliations on the title page: Fordham University (Cakici); HSB Hochschule Bremen – City University of Applied Sciences (Fieberg); Magyar Nemzeti Bank (Neszveda); Griffith University (Bianchi); MBS School of Business / Poznan University of Economics and Business / Monash University (Zaremba, corresponding author).
- **Pinned version / checksum (measured 2026-09-23):** the PDF was retrieved through a real browser session (SSRN's interstitial cleared), **2,190,537 bytes**, **SHA-256 `8b3660307dd87281bd3467bb47e2d4b1a4c9e91470004ec706e796e4d1ede4e1`**. Embedded metadata: `/Title "Microsoft Word - Paper_20260504a"`, `/Author Adam Zaremba`, `/CreationDate D:20260504172022+02'00'`. Title page states **"This version: May 4, 2026"**, matching the SSRN "last revised" date. All 59 pages were text-extracted and read (Abstract, §1–§6, Tables 1–13, Figures 1–7 captions, References).
- **Sample / universe verified from the primary PDF (§2.1 and the Table 2 caption):** U.S. common stocks on NYSE/Amex/Nasdaq; monthly CRSP + Compustat via WRDS, monthly features from the code of Jensen et al. (2023), daily returns from CRSP Daily Stock Files; **sample January 1927 – December 2024, with the actual testing period beginning January 1937** (first training window = 10 years).
- **Transaction-cost treatment verified from the primary PDF Methods/practical sections (§2 Data and Methods, §4.4 Practical Considerations):** no fee, commission, slippage, spread, borrow, market-impact, or fill model is applied anywhere to the reported portfolio returns; §4.4 instead reports turnover and **breakeven one-way transaction costs**. Full-text scan of the PDF: the only cost-model vocabulary present is the §4.4 breakeven discussion and a $5 price filter "to mitigate bid-ask bounce" (§2.1). Detailed turnover/breakdown tables (Table A3) live in an **Online Appendix that is not part of the 59-page PDF** → marked `data gap` below.
- **Core performance numbers:** all quantitative claims in this record are traced to a named table/section of the pinned PDF above (Table 2, Table 3, Table 4, Table 6, Table 7, Table 8, §4.4 with Table A4/A3 references, §4.5 with Figure 4, §5.1 Table 12, §5.2 Table 13, §5.3). No figure in this record is taken from a secondary summary.
- **Publication status:** SSRN working paper. **No journal acceptance, forthcoming notice, DOI other than the SSRN DOI, or peer-review statement appears anywhere in the PDF or on the landing page** → `not stated in source`. No replication package / code-availability statement appears in the PDF → `not stated in source`.
- **Pre-write deterministic dedup (2026-09-23, ripgrep across ALL `*.md` in this repository, not `git log`):** `Daily Return Information`, `\bDRIF\b`, `6005614`, `Unified Framework for Anomalies`, `Cakici`, `elastic-net`, `Zaremba`, `6468806` (the competing "Reviving Anomalies" candidate) → **zero records carry this source identity**. Adjacent but materially different records were checked and kept distinct: `crypto-cross-sectional-elastic-net-ctrend-2026-08-31` (Fieberg et al. JFQA *trend factor* on crypto — different paper, different signal), `crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31` and `crypto-cross-sectional-extreme-downside-risk-var-2026-09-01` (Bali–Cakici–Whitelaw MAX as an *input* characteristic, not this learned 21-day mapping), `conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04` (Brou–Luger sign/magnitude *market-timing* decomposition), `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31` (single-day reversal in crypto), `crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01` (crypto factor selection). **Genuinely new source identity and new mechanism family for this repository: a single elastic-net signal that spans the whole short-horizon anomaly class.**

## Economic mechanism

### Source-reported

The authors argue that a large class of cross-sectional equity anomalies (short-term reversal, idiosyncratic volatility, MAX/lottery, salience, sign-based measures) all draw on **the same raw material: the sequence of daily returns over the previous month**, but each isolates only one aspect by imposing an ad hoc functional form (§1). They instead estimate the mapping from the full 21-day daily-return vector to next-month returns with an **elastic net**, letting the data assign weights (§2.2–§2.3), producing the scalar signal **DRI** and the long–short factor **DRIF**.

Two information channels are separated (§1, §2.2):

- **Chronological information** — the time-ordered 21 daily returns — linked by the source to short-term reversal, liquidity provision and temporary price pressure (Kaul & Nimalendran 1990; Lo & MacKinlay 1990; Hasbrouck 1991; Chordia et al. 2002; Nagel 2012; Gârleanu & Pedersen 2013).
- **Rank (magnitude) information** — the same 21 returns sorted by size within the month — linked to attention, salience and lottery/skewness preferences (Bali et al. 2011; Barberis & Huang 2008; Bordalo et al. 2012).

The source's own reading of its coefficients (§3.2, Figure 2): the chronological component dominates, with the **largest negative loading on the most recent daily returns** (recent winners subsequently underperform, recent losers outperform) — i.e. short-horizon reversal is the primary channel; the rank component contributes a smaller but significant layer (§3.2, §6).

### Research interpretation

Falsifiable form: **the cross-section of next-month equity returns is predictable from the cross-sectionally demeaned 21-day daily-return path, and the predictability is dominated by the time-ordered (reversal/price-pressure) component, with the rank/salience component adding incrementally.** If the mechanism is friction/liquidity driven, the premium must (a) be larger where trading frictions bind (small, low-priced, illiquid, high-idiosyncratic-volatility stocks) and in high-VIX / high-short-rate states, and (b) decay rapidly when execution is delayed past the most recent days; if it is purely behavioral/attention driven, the rank component should carry comparable weight. Component roles (per README hybrid structure): **no regime filter and no exit/stop logic exist in the source** — Signal = DRI (chronological ⊕ rank), Portfolio = monthly decile long–short. Do not assume each component contributes: the source itself supplies the chronology-vs-rank ablation (Table 3) and an interaction test that adds "virtually no additional power" (§1).

## Signal

All items below are source-reported unless explicitly labeled `research-proposed` / `underspecified`.

- **Formation timestamp:** signal computed at **month end** from the **21 daily returns preceding portfolio formation** (`d = 1` is the most recent trading day; §2.2). Portfolio formation is monthly. Timezone/session convention for CRSP daily closes is `not stated in source`.
- **Cross-sectional demeaning:** in the estimation panel, all daily returns are **demeaned within each calendar day** to remove market-wide moves (§2.2, citing Murray et al. 2024).
- **Lookback:** exactly **21 trading days**, warm-up = the 21-day history plus the first 10-year training window; endpoints not further specified beyond "prior to portfolio formation" (`underspecified`: whether the 21st day may cross a month boundary is not stated).
- **Estimation (§2.3):** elastic net (Zou & Hastie 2005) of next-month excess returns on the two 21-element feature blocks; penalty mix **η = 0.5** (LASSO/ridge) default; **λ selected by repeated 5-fold cross-validation, 5 repetitions = 25 validation folds, minimizing MSE**, then refit on the full training set; **expanding (recursive) training window, first window = 10 years → out-of-sample forecasts start January 1937**; coefficients **re-estimated annually**, using only information available through year *t* to predict year *t+1* ("strictly out-of-sample" per §2.3).
- **Signal value:** `DRI_i,t = R^(chrono)' β̂^(chrono) + R^(rank)' β̂^(rank)` (Eq. 3).
- **Long entry:** buy the **top DRI decile** each month. **Short entry:** sell the **bottom DRI decile** ("High–Low"; Table 2 caption). Baseline weighting **value-weighted**; equal-weighted reported as Panel B of Table 2; deciles (quintiles only inside the multiverse, §4.5).
- **Exit / holding period:** **monthly rebalance**; holding period one month; overlapping positions do not apply (`underspecified`: no explicit stop, no take-profit, no within-month adjustment).
- **Execution timing assumed by the source (§4.4):** "strategies based on daily data implicitly assume trading at the **month-end close immediately after signal formation** — a strong assumption, as investors may not process information and trade instantaneously."
- **Delay robustness (§4.4, Table A4 — figures quoted in §4.4 text):** recomputing DRI with a **skip of the most recent k days (k = 1…10)**: value-weighted spread **1.57% → 0.85% (k=1) → 0.38% (k=3)**; equal-weighted **2.26% → 1.27% (k=1) → 0.77% (k=3)**; "a substantial portion of the premium concentrated in the most recent days", significance weakening at longer lags for value-weighted portfolios.
- **Universe filters (§2.1, Table 2 caption):** U.S. common stocks that are the firm's primary security on its main listing exchange (one WRDS observation per firm-month); non-missing end-of-month price, market equity, one-month-ahead excess return and 21 daily returns; **price > $5 at month end**; **exclude nano-caps below the NYSE 1st percentile of market cap** (Jensen et al. 2023 definition). Cross-section: ~600 stocks early, ~6,000 at peak, **time-series average 2,601**; by count 32% big / 29% small / 39% micro; by cap ~90% big.
- **Parameters:** lookback 21 days, η = 0.5, 10-year first training window, annual refit, 25 CV folds, decile breakpoints, monthly rebalance, $5 and nano-cap filters — all source-fixed. Any additional knob below is `research-proposed`.
- `research-proposed` (not in source): a crypto or liquid-only universe variant, a liquidity/participation cap, any entry threshold, any stop or vol-target overlay, and any choice of venue or rebalance clock other than month-end close.

## Required data

- **Instrument / universe:** U.S. common stocks, NYSE/Amex/Nasdaq, primary listing only; **not crypto** (§2.1).
- **Venue / data vendor:** CRSP (monthly + Daily Stock Files) and Compustat **via WRDS**; monthly characteristic code from Jensen et al. (2023) (`data gap`: exact feature list/code revision not pinned in the paper).
- **Market type / timeframe:** equity cash market, **daily returns aggregated to monthly** portfolios.
- **Fields used:** daily total returns (21-day history), month-end price, market equity, one-month-ahead excess return, plus — for the control/factor tests only — book-to-market, momentum, profitability, asset growth, illiquidity, bid-ask spread, ivol, co-skewness (Table 6 caption) and the FF6 factor returns.
- **Point-in-time / availability:** the source states forecasts use only information available up to the end of year *t* (expanding window, annual refit) and that the first 10 years are training-only, so reported test returns are out-of-sample from 1937 (§2.3). CRSP/Compustat are **proprietary and point-in-time only if re-fetched historically**; delisting returns, share-code changes and NYSE-breakpoint vintage handling are `underspecified` beyond the §2.1 statements.
- **Timestamp / timezone:** `not stated in source` (CRSP daily close convention assumed but never written).
- **Missing data:** imputation forbidden by the source's own sample rule — observations lacking any of the required fields are dropped (§2.1); treatment of halts/partial months `not stated in source`.
- **Funding/fee/spread needs:** none for the signal itself; for tradability the record needs one-way transaction costs, short-borrow availability and fees — **none of which the source models** (`not stated in source`; see Execution assumptions).

## Execution assumptions

- **Signal-to-order:** month-end close, same instant as signal formation (source's own stated "strong assumption", §4.4).
- **Order type / fill model / latency / partial fills:** `not stated in source`.
- **Fees, spread, slippage, market impact:** **no cost model is applied to any reported return.** The source's only cost analysis is the breakeven one-way cost in §4.4: **value-weighted DRIF breakeven ≈ 42 bps per month (36 bps at the 5% level), equal-weighted ≈ 65 bps (57 bps)**, plus long-only top-decile breakevens of **69.3 bps (value-weighted) and 100.5 bps (equal-weighted)**; breakevens are higher for microcaps and "substantially lower" for large caps. The source notes these thresholds **exceed typical institutional estimates reported by Frazzini et al. (2018)** while still implying "a meaningful fraction of the gross return is offset by trading frictions". *Research interpretation (Scout): because no cost deduction appears anywhere in Tables 2/3/7, those headline spreads should be read as **gross** of trading costs — the source itself never writes the word "gross", so this classification is flagged as Scout reading, not a source quote.*
- **Turnover:** **average monthly turnover 92.6% (value-weighted DRIF spread, full sample)**, "among high-turnover strategies" (§4.4, citing Table A3 of the **Online Appendix, which is not contained in the retrieved 59-page PDF → `data gap` for the underlying per-year/per-decile breakdown**).
- **Borrow / shorting:** `not stated in source` — no borrow fee, availability, recall or shorting-constraint model; the source only motivates the short leg via Stambaugh et al. (2012) short-sale-constraint logic (§3.1).
- **Capacity / impact / leverage / margin:** `not stated in source`. The source argues value-weighted results are less small-cap dependent but performs no participation-ratio or impact test.
- **Distinguish source vs Scout:** everything above is what the source assumes or omits; our own cost ladder, liquidity caps and venue choices are `research-proposed` and appear only in the Falsification plan.

## Evidence

### Source-reported

All figures below are gross-of-cost spreads/alphas from the pinned PDF (May 4, 2026 version), U.S. common stocks, Jan 1927–Dec 2024 sample with testing from Jan 1937; Newey–West t-statistics; FF6 = Fama–French (2018) six-factor model.

- **Table 2, Panel A (value-weighted): High–Low = 1.57% per month (t = 10.94), annualized Sharpe 1.23, FF6 alpha 1.60% (t = 9.41).** Component deciles: Low mean −0.28% (t = −1.35), alpha **−0.98%** (t = −8.75); High mean 1.29% (t = 6.59), alpha **0.62%** (t = 5.86) — i.e. both legs contribute, with the larger abnormal return on the short side.
- **Table 2, Panel B (equal-weighted): High–Low = 2.26% per month (t = 16.52), Sharpe 2.39, FF6 alpha 2.10% (t = 15.19).**
- **Table 3 (value-weighted component ablation):** chronological-only High–Low **1.50%** (t = 10.53, Sharpe 1.20, alpha 1.56%) joint estimation / **1.50%** (t = 10.30, Sharpe 1.19, alpha 1.57%) individually estimated; rank-only **0.84%** (t = 4.87, Sharpe 0.56, alpha 0.50%) joint / **0.86%** (t = 4.75, Sharpe 0.56, alpha 0.53%) individual. §3.2 prose rounds these to "exceeding 1.5% … Sharpe around 1.2" and "approximately 0.85% … Sharpe around 0.55".
- **Table 4 (spanning):** the chronological component keeps an alpha of **≈1.4% per month** when regressed on the rank signal, while the rank component's alpha in the reverse regression is negligible; DRI itself retains positive significant alphas against either component → each carries non-overlapping information, hierarchy is chronological-dominant (§3.2).
- **Table 6 (Fama–MacBeth, OLS and WLS):** DRI slope positive and highly significant in univariate and multivariate settings; in the kitchen-sink regression with 15 controls — including salience (ST) and chronological-return-ordering (CRO) variables — **t-statistic still exceeds 9** (§4.2).
- **Table 7 (subperiods, value-weighted spread):** 1937–1959 **1.43%**, 1960–1979 **1.76%**, 1980–1999 **2.17%**, **2000–2024 1.08% (t = 3.16) with FF6 alpha 1.16% (t = 3.70)**; full sample 1.57%. By size for 2000–2024: micro **1.86%**, small **1.60%**, big **0.90%** (full sample: micro 2.99 / small 2.14 / big 1.28).
- **Table 8 (market states):** DRIF strengthens after **high-volatility months (2.07% vs 1.14%)** and in **high short-rate states (1.99% vs 1.26%)**, both significant; this variation is driven by the chronological component, which rises ≈0.8 pp per month in those states, while the rank component is comparatively stable (§4.3–§4.4).
- **§4.5 multiverse (Figure 4, Table 9):** **2,304 DRIF implementations** (10 crossed design choices: universe/price/listing-history/financials-utilities filters × information set × OLS/LASSO/elastic-net × expanding vs 120-month rolling × decile/quintile × equal/value weighting). Mean monthly returns **0.77%–3.58%**, Sharpe **0.76–3.08**, **minimum t-statistic 6.64**, **minimum monthly alpha 0.72%**; the baseline sits *below* the median on mean/t/Sharpe (67th percentile on alpha) → the relation is not a favorable-specification artifact (source's claim).
- **§5.1 Table 12 (spanning of the short-horizon anomaly class):** adding DRIF to FF6 cuts the average absolute alpha of the comparator anomalies from **0.45 to 0.25** and the average absolute t-stat from **2.44 to 1.60**; idiosyncratic-volatility, realized-volatility, MAX and standard short-term-reversal alphas shrink to insignificance, while **industry-adjusted reversal (IA-REV), regret (REG) and relative-loss-aversion (RLA) keep significant intercepts** (explicit source-stated boundary of DRIF).
- **§5.2 Table 13 (sequential factor selection, Swade et al. 2023):** with DRIF available it is **selected immediately after the market**, delivering the largest single-step error reduction (**GRS 3.79 → 3.02**; average |alpha| 0.53% → 0.44%), converging to an eight-factor model (GRS 1.65, average |alpha| 0.16%); selection frequency ≈100% across the 2,304 designs and **99.91% in 10,000 stationary-bootstrap resamples**.
- **§5.3 (Bayesian spike-and-slab SDF, Bryzgalova et al. 2023):** 43 candidates (26 tradable factors, 16 macro variables, DRIF) ⇒ **>8.8 trillion model configurations**; DRIF attains the **highest posterior inclusion probability** across all prior-Sharpe settings, often exceeding market and momentum.
- **Source's own framing:** the 1.57% spread "reflects an upper bound on the strength of the predictive relation rather than directly attainable profit" (§1 and §3.1, citing Patton & Weller 2022).
- **`data gap`:** no net-of-cost return, Sharpe, IC, or deflated Sharpe ratio for DRIF is reported anywhere in the pinned PDF (the deflated-Sharpe literature is cited only in the reference list, Bailey & López de Prado 2014).

### Independently reproduced

not independently reproduced.

### Negative evidence

- **From the source itself:**
  - **Attenuation over time:** the spread falls to 1.08%/month in 2000–2024 and to **0.90%/month for big caps**, versus 1.43–2.17% in earlier decades; the source attributes this to improving liquidity, more arbitrage competition and faster information incorporation (§4.3, Table 7, citing Chordia et al. 2014; McLean & Pontiff 2016).
  - **Execution-delay decay:** skipping just the most recent day cuts the value-weighted spread from 1.57% to **0.85%**, and three days to **0.38%** (§4.4, Table A4) — the premium is concentrated exactly where instant month-end execution is required.
  - **Turnover/cost exposure:** **92.6% monthly turnover** with breakeven one-way costs of 42 bps (VW) / 65 bps (EW); the source concedes a meaningful fraction of gross return is consumed by frictions and cites Novy-Marx & Velikov (2016, 2019) on cost erosion of short-horizon signals (§4.4).
  - **Mechanism boundary:** industry-adjusted reversal, regret and relative-loss-aversion alphas survive FF6+DRIF (§5.1) — DRIF does not subsume within-industry return structure.
  - **Methodological self-risk:** the source explicitly flags that elastic-net/high-dimensional settings can capture idiosyncratic patterns (§4.5, citing Bailey & López de Prado 2014; Kim et al. 2021) and answers with a multiverse, **not** with a deflated-Sharpe correction.
  - **Internal numeric inconsistency (Scout check of the pinned PDF):** the Introduction (p. 3) reports the rank component as "roughly **0.94%** … Sharpe ≈ 0.56", whereas §3.2 prose and Table 3 report **0.84–0.86%** with Sharpe 0.55–0.56. Table values are used in this record.
- **From Scout reading (clearly separated):**
  - Reported performance contains **no transaction-cost, borrow, or impact model at all** — for a >90%-monthly-turnover long–short decile strategy this is the single largest evidence gap.
  - Proprietary WRDS/CRSP dependency and no replication package statement → independent reproduction cost is high.
  - Post-publication / modern-era anomaly decay is a general concern; a related cost-focused study (Chen & Velikov, *JFQA* 58(3), 2023, DOI 10.1017/S0022109022000874) was surfaced during discovery but **its primary source was not opened this run, so no numbers from it are asserted here** — flagged as a required reading for the cost review.
  - Absence of peer review: SSRN working paper with no acceptance statement (`not stated in source`); absence of a negative result elsewhere is not evidence of robustness.

## Falsification plan

Source-defined tests (already in the paper's design): strictly out-of-sample expanding-window annual refit; 2,304-design multiverse with a pre-declared design space (§4.5); controls against FF6, a >150-anomaly factor zoo (generalized alphas, FGX, Feng et al. double-selection LASSO), sequential factor selection, and Bayesian SDF averaging; skip-period delay test (Table A4); chronology-vs-rank ablation (Tables 3–4).

Scout-added operational tests — everything here is `research-proposed` except thresholds explicitly marked `research-defined`:

1. **Net-of-cost ladder (`research-proposed`).** Recompute the value-weighted decile spread after one-way costs of 5 / 10 / 20 / 42 bps at the source's 92.6% monthly turnover. **Failure rule (`research-defined`):** if the net spread is ≤ 0 at the source's own 42 bps breakeven, the *tradability* claim fails (the pricing relation may still hold); action = keep record at `research-only`, block any implementation candidate.
2. **Execution-delay test (`research-proposed`).** Re-run with k = 1, 2, 3 skipped days. **Failure rule (`research-defined`):** if the value-weighted spread with a one-day skip falls below **50% of the 1.57% baseline (i.e. < 0.79%/month)** — source reports 0.85% — treat the result as execution-timing dependent and require same-close capacity evidence before any further work.
3. **Modern-subperiod requirement (`research-defined`).** On 2000–2024 (and a post-2024 holdout once available) the value-weighted spread must stay positive with t ≥ 2.0. Source reports 1.08% (t = 3.16); a holdout reading below t = 2.0 fails the hypothesis for current-regime use.
4. **Chronology-vs-rank ablation (`research-proposed`).** Compare combined vs chronological-only vs rank-only (source's Table 3 structure). **Failure of the "unified framework" claim (`research-defined`):** combined spread ≤ max(component spread) by more than measurement noise (component gap < 0.1%/month) means the framework adds nothing beyond reversal.
5. **Placebo / mechanism test (`research-proposed`).** (a) Randomly permute the within-month ordering of the 21 returns in the *training* features (keeps the rank block intact, destroys chronology): if the out-of-sample spread is unchanged, the source's reversal/price-pressure mechanism claim is rejected; (b) shuffle next-month return labels in training and require out-of-sample t < |2|.
6. **Specification-perturbation (`research-proposed`).** Vary lookback (15/21/63 days), η (0.0/0.5/1.0), rolling-120-month vs expanding refit, decile vs quintile, equal vs value weighting; parameter sensitivity that flips sign is failure (source's own multiverse is the benchmark: min t = 6.64, min alpha 0.72%).
7. **Alternative universe / venue (`research-proposed`).** Restrict to the top-N most liquid names (e.g. by Amihud or dollar volume) with a participation cap; long-only top-decile variant must clear its own breakeven (source: 69.3 bps VW).
8. **Competing explanation (`research-proposed`).** Double-sort DRI against short-term reversal, ivol, MAX and salience with identical breakpoints (source's Table 5/12 design); if DRI's alpha conditional on plain short-term reversal is ≤ 0, the "unified" contribution reduces to documented reversal.
9. **Point-in-time / leakage audit (`research-proposed`).** Rebuild the panel from raw CRSP with delisting returns and NYSE-breakpoint vintages; any 20%+ change in the baseline spread is failure of the data pipeline, not of the hypothesis.
10. **Action on failure:** every failure path leaves the record at `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`; no retuning of frozen parameters is allowed to rescue a failed test.

## Crypto portability

**unproven.** The source demonstrates the mechanism only in U.S. equities and explicitly lists extension to "bonds, commodities, or cryptocurrencies" as **future research** (§6) — there is **no crypto evidence in the source**, so this cannot be `direct`, and nothing has been ported yet, so it is not `adapted`.

Porting risks if a crypto variant is ever attempted (all rules below are `research-proposed`, none from the source):

- **Universe / survivorship:** decile sorts need a broad, point-in-time cross-section with delisted names; crypto listing histories are survivor-biased and concentrated — a 21-day panel over hundreds of microcaps is mostly untradable.
- **Calendar semantics:** the signal is defined on *21 trading days before month end*; crypto trades 24/7 with no session close, so candle boundaries, timezone and "month end" are a free parameter (exchange daily 00:00 UTC vs calendar month) — a material data dependency the source never specifies for crypto.
- **Demeaning step:** cross-sectional daily demeaning requires an index-like breadth measure; on crypto, thin breadth and stablecoin/quote-currency effects make the demeaning base ambiguous.
- **Mechanism fit:** the source's channel is temporary price pressure / liquidity provision with short-sale constraints; crypto perps have cheap native shorting but **funding payments, liquidation cascades and 8-hourly settlement** interact with a monthly long–short reversal in ways the source never models (spot vs perpetual, funding, mark/index basis, venue fragmentation).
- **Frequency/clock:** monthly rebalance vs crypto's intraday regime rotation; adjacent repo records already document crypto last-day reversal, OI/funding regimes and factor-zoo effects — a port must be tested against those, not assumed.
- Any crypto claim of the form "DRIF works on crypto" would be a **different mechanism record** requiring its own primary source.

## Limitations

- `data gap`: **no net-of-cost performance anywhere** — all headline numbers are gross; breakeven analysis (§4.4) substitutes for a cost model; turnover table (A3) sits in an Online Appendix **not included in the retrieved PDF**.
- `data gap`: no deflated Sharpe / multiple-testing correction for DRIF itself; no IC/ICIR reported (portfolio sorts only).
- `data gap`: no replication package, code, seed for CV partitions, or exact feature-list pin (Jensen et al. 2023 code referenced but not versioned).
- `data gap`: no borrow/short-cost, no capacity/impact, no fill/latency model; order type and timezone `not stated in source`.
- `underspecified`: whether the 21-day window may cross month boundaries; delisting-return and corporate-action handling; behavior around halts and partial months.
- `underspecified`: publication status — SSRN working paper, no journal/peer-review statement in source.
- Internal inconsistency: rank-component spread stated as ≈0.94% in the Introduction vs 0.84–0.86% in §3.2/Table 3 (Table values used here).
- Regime risk: strong attenuation post-2000 (1.08%) and in big caps (0.90%); premium concentrated in the last 1–3 days (skip test) — implementation-sensitive by construction.
- Source's own caveat: spreads are an **upper bound, not attainable profit** (Patton & Weller 2022); mechanism-boundary evidence: industry-adjusted reversals survive DRIF.
- `not independently reproduced`; proprietary CRSP/WRDS data dependency; single-study evidence (no external replication found in this run's search).

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no signal code, no CRSP/WRDS ingestion, no backtest, no Qlib run, no Paper/Testnet/Live activity of any kind. The record is a normalized research capture of a public working paper only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No evidence count, table count, Sharpe ratio, or multiverse result in this record promotes it.

## Related Wiki records

No stable Hermes Wiki Brain page is verified for any related record this run, so only the schema page is linked as a Wiki link:

- `[[quant/strategy-research-record-spec-v1]]` — authoritative schema specification (read this run).

Adjacent records already in this repository (checked for dedup; **different source identities and different mechanisms** — plain filenames, not Wiki links):

- `crypto-cross-sectional-elastic-net-ctrend-2026-08-31.md` — Fieberg et al. (JFQA 2025) *trend factor* for crypto; elastic-net method overlap only.
- `crypto-cross-sectional-max-daily-return-lottery-momentum-2026-08-31.md` / `crypto-cross-sectional-extreme-downside-risk-var-2026-09-01.md` — MAX/lottery characteristic family that DRIF claims to subsume (equity source vs crypto ports).
- `crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31.md` — single-day reversal analogue in crypto.
- `conditioning-sign-on-magnitude-return-decomposition-csm-2026-09-04.md` — sign/magnitude return decomposition for equity-premium timing (different target variable).
- `crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01.md` — crypto factor-zoo compression; methodologically adjacent to §5.2 sequential selection.
- `anomaly-pre-release-drift-predicted-signal-decile-portfolios-2026-09-23.md` and `china-ashare-factor-library-overfitting-audit-amihud-illiquidity-falsification-2026-09-13.md` — anomaly-cost and anomaly-multiplicity audits that frame the same skepticism DRIF must survive.

## Sources

1. Nusret Cakici, Christian Fieberg, Gabor Neszveda, Robert Bianchi, Adam Zaremba. *"A Unified Framework for Anomalies Based on Daily Returns."* SSRN Working Paper **abstract_id=6005614**, DOI **10.2139/ssrn.6005614**; posted 7 January 2026, last revised 4 May 2026; document version "May 4, 2026"; 59 pages. Landing: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6005614 — **read in full (all 59 pages: Abstract, §1–§6, Tables 1–13, figure captions, References) on 2026-09-23**; retrieved PDF SHA-256 `8b3660307dd87281bd3467bb47e2d4b1a4c9e91470004ec706e796e4d1ede4e1`, 2,190,537 bytes. PDF: https://papers.ssrn.com/sol3/Delivery.cfm/6005614.pdf?abstractid=6005614&mirid=1
2. Every quantitative claim in this record traces to that pinned PDF at a named location: **Table 2** (baseline deciles, VW/EW spreads, Sharpe, FF6 alphas), **Table 3** (chronological vs rank ablation), **Table 4** (spanning), **Table 6** (Fama–MacBeth controls), **Table 7** (subperiods and size), **Table 8** (market states), **§4.4 with Table A3/A4 references** (turnover, breakeven costs, skip-period decay), **§4.5 / Figure 4 / Table 9** (2,304-design multiverse), **§5.1 / Table 12** (spanning of short-horizon anomalies), **§5.2 / Table 13** (sequential factor selection), **§5.3** (Bayesian SDF), **§6** (conclusion, crypto listed as future work), **§2.1–§2.3** (data, signal, estimation).
3. Discovery aids only (no figure or rule in this record is taken from them): Alpha Architect / Larry Swedroe summary, CXO Advisory summary, QuantifiedStrategies summary, SSRN landing-page metadata.
