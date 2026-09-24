---
schema: strategy-research-record-v1
title: "Malaysia Official Shariah List Inclusion: Matched [0,10] and [0,20] Trading-Day Drift After the Securities Commission Release (Permission / Constrained-Demand Event)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - event-driven
  - equity-event-study
  - constrained-demand
  - shariah-screening
  - institutional-flow
  - emerging-market
status: research-only
confidence: medium
source_as_of: 2026-08-12
sources:
  - "https://arxiv.org/abs/2608.12634 (arXiv:2608.12634v1 [q-fin.ST], only version [v1] Wed, 12 Aug 2026 22:49:26 UTC 781 KB, submitter Abdulrahman Qadi)"
  - "https://arxiv.org/html/2608.12634v1 (pinned v1 HTML full text, 681,681 bytes fetched and read end to end 2026-09-25)"
  - "https://doi.org/10.48550/arXiv.2608.12634 (DataCite, HTTP 302 -> https://arxiv.org/abs/2608.12634, checked 2026-09-25)"
  - "https://www.sc.com.my/development/icm/icm-publications/list-of-shariah-compliant-securities (official SC Malaysia list-of-shariah-compliant-securities archive; URL read from the reference anchor inside the pinned v1 HTML, not invented)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Malaysia Official Shariah List Inclusion: Matched [0,10] and [0,20] Trading-Day Drift After the Securities Commission Release (Permission / Constrained-Demand Event)

## Provenance

**Primary source identity.** arXiv preprint `arXiv:2608.12634v1`, title *The Price of Permission: Classification Uncertainty in Constrained Capital Markets*, landing page `https://arxiv.org/abs/2608.12634`, pinned full text `https://arxiv.org/html/2608.12634v1`. Submission history shows **exactly one version: [v1] Wed, 12 Aug 2026 22:49:26 UTC (781 KB)**, submitter Abdulrahman Qadi; no v2 as of 2026-09-25. `Comments: 67 pages, 20 figures, 27 tables`; **no `Journal-ref`, no publisher `DOI` beyond the arXiv-issued one and no peer-review statement anywhere in the landing page or body -> preprint only**. Primary subject `q-fin.ST`. **License: `arXiv.org perpetual non-exclusive license`** (printed in the v1 HTML header) — this is *not* a Creative Commons licence, so the text is cited and normalized here rather than reproduced. DataCite DOI `10.48550/arXiv.2608.12634` resolves **HTTP 302 -> `https://arxiv.org/abs/2608.12634`** (final 200, checked 2026-09-25). `source_as_of: 2026-08-12` is the pinned v1 submission date; the empirical sample as-of runs **January 1999 – December 2024 (Route A, US)** and **November 2013 – November 2025 (Route B, Malaysia)**.

**Text actually read.** The pinned v1 HTML (681,681 bytes, converted to 153,638 characters / 2,442 lines) was fetched and read end to end on 2026-09-25: Sections 1–9, the three declarations, References, and Internet Appendices A (roadmap), B (Route A) and C (Route B), including main Tables 1–19 and the appendix table notes.

**Authors (exactly as printed on the title block).** Abdulrahman Qadi (corresponding author, `abdulrahman.qadi.24@ucl.ac.uk`), Akash Sharma, Francesca Medda — all three listed under **Institute of Finance and Technology, University College London, Gower Street, London WC1E 6BT**; no per-author affiliation markers beyond that single block, so per-author institute mapping beyond "all three carry the UCL IFT block" is `data gap`.

**Declarations (verbatim scope).** Competing interests: none known. Funding: none. Generative-AI use: Claude (Anthropic) and Codex (OpenAI) used **"solely assist with LaTeX debugging"**, with authors taking responsibility for all formulas, empirical claims and manuscript content. Data availability: a replication package **"will include"** programs, dictionary, merge-key documentation, parser logs and synthetic inputs; **CRSP, Compustat, WRDS, LSEG Workspace and index-provider inputs are proprietary and cannot be redistributed**; the SC Malaysia PDFs are public.

**Deduplication (deterministic source-identity search, 2026-09-25).** Whole-repository ripgrep across **all 2,524 `*.md` files including hidden trees** (`.mimo-worktrees`, `.agents`, `.hermes`) **plus `coverage_manifest.csv` (5,808 lines)** for `2608.12634`, `The Price of Permission`, `Price of Permission`, `Abdulrahman Qadi`, `Qadi`, `Akash Sharma`, `Francesca Medda`, `Medda`, `permitted investor mass`, `classification uncertainty`, `permission premium`, `Securities Commission`, `Securities Commission Malaysia`, `Shariah`/`sharia`/`Islamic`, `AAOIFI`, `DJIM` — **every exact-identity pattern returned 0 hits** (case-insensitive included). Family-level neighbours found and cleared: `index inclusion` (3 files) resolves to `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md`; `constrained investor` (6 files) resolves to the analyst-coverage spillover record and `crypto-cross-sectional-betting-against-beta-2026-08-31.md`.

**Four-axis distinction (mechanism / signal construction / universe / horizon / data dependency).** (1) vs `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13`: that record studies **benchmark-index forced flow** on announcement-to-effective dates in US large caps; this record studies **mandate-permission (religious-eligibility) demand** at a single dated regulator release, with the flow channel unproven. (2) vs `buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13`: firm-initiated repurchase disclosure vs **regulator-issued eligibility labels**. (3) vs `crypto-brown-esg-uncertainty-next-day-downside-liquidity-amplified-2026-09-03`: continuous **ESG score uncertainty** in crypto vs a **binary, rule-book-defined permission** event in listed equities. (4) Mechanism here = *classification change -> permitted-investor-set change -> rebalancing -> possible price pressure* (each arrow conditional), universe = **Bursa Malaysia securities on official SC lists**, horizon = **10/20 trading days post-release**, data dependency = **public SC PDFs + Compustat Global listing history** — no axis overlaps any existing record. No second record from this source exists.

## Economic mechanism

### Source-reported

The authors' chain is explicit and deliberately conditional: `classification change -> change in the permitted investor set -> portfolio rebalancing -> potential price pressure`, with each arrow requiring that the affected rule govern economically relevant capital, that the event not be fully anticipated, and that permitted investors be marginal and able to trade — so **"a formal label change can therefore leave prices unchanged."** The formal object is *permitted investor mass* `m_i = omega_U + omega' e_i` (unconstrained capital mass plus the capital masses governed by each Shariah policy type) in a transparent mean-variance benchmark where required expected returns decline as `m_i` expands. *Classification uncertainty* has two stated dimensions: **cross-standard disagreement over the current eligible set** (DISC) and **dynamic boundary risk** (distance to the nearest binding screen threshold). The paper states plainly that it **"does not claim that these measures already constitute a profitable trading strategy"** and that **"the paper does not estimate the profitability of acting on this information."**

Two empirical routes are reported. **Route A (US, monitoring and boundary test):** 1999–2024 CRSP–Compustat panel of **13,188 securities / 1,342,606 security-months**, share codes 10/11 on NYSE/AMEX/NASDAQ, seven *researcher-emulated* rulebooks (AAOIFI, DJIM, S&P, FTSE/Yasaar, MSCI main, MSCI M-Series, SC Malaysia), accounting data lagged six months, plus a September 2023 DJIM/S&P methodology-shock event study. **Route B (Malaysia, the central price evidence):** **25 official semi-annual Securities Commission Malaysia lists, November 2013 – November 2025**, parsed from the official PDFs, day 0 = first security-specific trading day on or after the PDF release date printed on the cover.

### Research interpretation

Hypothesized mechanism (falsifiable form): in a market where **one public authority issues a single recognized binary eligibility list**, an inclusion event changes the feasible set of a mandate-governed capital pool, and — conditional on the name being already listed, tradable enough to absorb the flow, and not fully anticipated — produces a **positive drift over the following ~10–20 trading days**. This is a *constrained-participation / forced-rebalancing* mechanism (the Merton 1987 investor-recognition and Heinkel et al. 2001 segmentation lineage the source itself cites), not an information-diffusion or earnings mechanism.

Component roles (source-reported unless marked):
- **Regime / filter:** pre-event average share turnover over `[−30,−1]` must be at or above the cross-sectional bottom-quartile cutoff (printed floor **0.000296**), *and* the security must have traded before the preceding review (continuously-listed requirement). Source-reported as a *sample definition* built exclusively from pre-event data.
- **Primary signal:** official SC Malaysia list inclusion (stock code in `M_ell` but not `M_{ell-1}`), dated by the PDF release date. Source-reported.
- **Confirmation filter:** none specified by the source (same-SIC matching is a *robustness* design, not a signal filter).
- **Exit / risk logic:** not specified by the source; `[0,10]` and `[0,20]` are **event-study measurement windows**, not printed holding rules. The tradable reading of them is **research-proposed** below.
- No source claim assigns alpha to any component separately; ablation is left to falsification.

## Signal

**Source-reported (event-study construction, not a trading rule).**
- Event definition: inclusion/exclusion/continuous-compliance computed at the **official stock-code level before Compustat linkage**; day `d = 0` is the first security-specific trading day on or after release date `a_ell`.
- Abnormal return: market-adjusted `AR_i,d = r_i,d − r_m,d^MYS` with `r_m,d^MYS` the **equal-weighted Compustat Global Malaysia daily return** in the analysis universe; `CAR` = sum over the window; `diffCAR` = treated CAR minus the mean CAR of its three matched controls.
- Matching: **three nearest controls** from continuously compliant securities of the same list date, standardized (within treated + date-specific candidate pool) Euclidean distance on **log market cap, pre-event return, volatility, turnover, Amihud illiquidity**, **no caliper, with replacement, greedy** (not globally optimal); balance reported in Table 13 (largest standardized difference **0.150**, log dollar volume; all matching variables < 0.09).
- Sample ladder (Table 7): 859 official inclusion transitions -> 598 linked to a Compustat Global security -> 595 with a valid release-date CAR -> 582 matched -> **410 continuously listed** -> **295 continuously listed + above the turnover floor** (the primary sample; 257 of 367 exclusions survive the same floor).
- Primary outcome: **matched `diffCAR[0,10]`** for the 295 inclusions; `[0,20]` secondary; inference = clustering by SC list date (**24 non-baseline clusters**) plus **wild-cluster bootstrap p-values with 999 restricted Rademacher replications**.
- Full-sample caveat the source prints: `Q^turn_0.25` is the bottom-quartile cutoff **"in the full matched event universe before treatment-specific filtering"**, i.e. computed over the whole 2013–2025 event universe rather than recursively from past releases.

**Underspecified in the source (must not be read as reproducible):** entry price and time of day (the SC PDF has a date but **no publication time-of-day**, so "enter on day 0" is not pinned), position sizing, weighting, holding-period mechanics, re-entry, shorting, any stop, and whether `[0,10]` counts trading days from the release-day close or the next open. Route B tail treatment (winsorization/outlier rules) is **not stated** — the four winsorization statements in the pinned text all belong to Route A and the Fama–MacBeth tables.

**Research-proposed tradable skeleton (NOT source-reported).** Long-only, equal-weight: buy at the **first print strictly after the release date is observable** (conservative choice: **day-1 open**, `research-proposed`), one position per included name, exit at the close of trading day **10** (variant: day **20**), no leverage, participation capped at **20% ADV** (`research-defined`), cost ladder as in F3. This skeleton exists only so the falsification plan has something concrete to attack; the source neither prints nor endorses it.

## Required data

- **Event source (public):** SC Malaysia *List of Shariah-Compliant Securities*, semi-annual PDFs 2013–2025 (25 list dates + printed release dates) — `https://www.sc.com.my/development/icm/icm-publications/list-of-shariah-compliant-securities`.
- **Universe / linkage:** Bursa Malaysia official stock codes; **Compustat Global** security master and first observed trading date (to identify "continuously listed"); listing-history lookback before each review.
- **Market fields:** daily close-to-close returns, volume, shares outstanding, price level; equal-weighted Malaysian market return (Compustat Global Malaysia); pre-event log market cap, return, volatility, turnover, **Amihud illiquidity** over `[−30,−1]` and `[−250,−30]`-style windows where used.
- **Point-in-time / availability:** release date must be read from the PDF cover (day 0 = first trading day on or after it); membership state must be reconstructed from consecutive lists; **time-of-day of publication is unavailable (`data gap`)**.
- **Optional mechanism data:** LSEG Workspace dated holder snapshots (treated 55,180 holder rows; controls 178,058 rows), Malaysia Shariah ETF NAV/shares/holdings — **proprietary, non-redistributable**.
- **Missing-data behavior as printed:** parser recovered **633 of 653** codes on the November 2013 PDF (pagination/column-break artefact; re-anchoring on May 2014 leaves estimates unchanged); 859 -> 598 linkage loss drops unlinked/first-observed names; events are dropped when the security has < 40 baseline trading days, price < $1 equivalent, or no trade within five calendar days of the event day (Route A filters; Route B relies on the CAR-validity and matching stages).

## Execution assumptions

**The source contains no execution or cost model.** Pinned-v1 word-boundary scan (our scan, 2026-09-25): `transaction cost(s)` **2** hits, both prose (a monitoring sentence in §3 and the §8 list of things a tradable strategy *would* need) — no fee, spread, borrow or impact model anywhere; `bid-ask` **0**, `slippage` **0**, `latency` **0**, `fill` **0**, `fee` **0**, `borrow` **0**, `short sell` **0**, `market impact` **0**, `Sharpe` **0** (the single case-insensitive hit is the word *sharper*), `drawdown` **0**; `commission` **14** hits are all the institution *Securities Commission* (brokerage commission model: none); `leverage` **6** hits are book-leverage controls/screen ratios; `spread` **1** hit is dispersion of eligibility rates across standards; `turnover` **53** hits are the matching variable, the pre-event screen and benchmark turnover, not portfolio turnover; `capacity` **20** hits are ETF channel capacity and prose; `participation` **4** hits are investor-participation prose; `ADV` **1** hit inside an appendix demand-pressure scaling. **Everything missing is `data gap`, never zero.**

Also unstated: signal-to-order timing, order type, fill model, partial fills, latency, borrow/short availability (there is no printed short leg anyway), leverage/margin, dividends/withholdings, **Malaysia-specific statutory levies**, capacity, and per-side vs round-trip reading of any future cost assumption (`underspecified`). A traded-strategy P&L, turnover, Sharpe and drawdown **do not exist in the source**: this is an event study, not a backtest.

## Evidence

### Source-reported

All figures below are read from the pinned v1 and are third-party claims (source-reported, none reproduced by us). All are **gross of any cost**.

- **Table 14 specification ladder** (matched `diffCAR`, percentage points, `p_date` / `p_wild`): all matched inclusions **N=582** → **0.784** `[0,10]` (0.163 / 0.163), **1.436*** `[0,20]` (0.072 / 0.083); continuously listed **N=410** → **0.896** (0.127 / 0.134), **1.458*** (0.053 / 0.064); **continuously listed + turnover floor N=295** → **1.759\*\*\*** `[0,10]` (**0.008 / 0.017**), **2.252\*\*** `[0,20]` (**0.018 / 0.035**); complete-fundamentals **N=262** unadjusted 2.154 (0.003 / 0.009) and 2.753 (0.005 / 0.012), with relative fundamentals 2.154 (0.001 / 0.006) and 2.753 (0.003 / 0.017) — the source states the larger complete-case level is **sample composition, not the added controls**. Turnover floor printed as **0.000296**; wild p-values use **999 restricted Rademacher replications**.
- **Table 15 event-window profile (N=295; estimate, cluster SE, `p_date`, `p_wild`):** `[−20,−1]` −0.816 (0.987; 0.409 / 0.451); `[−10,−1]` −0.475 (0.440; 0.281 / 0.298); `[−5,−1]` −0.037 (0.340; 0.914 / 0.909); `[0,1]` **−0.233** (0.278; 0.404 / 0.461); `[0,3]` 0.844\*\* (0.395; 0.032 / 0.068); `[0,5]` 1.017\* (0.524; 0.053 / 0.082); `[0,10]` **1.759\*\*\*** (0.660; 0.008 / 0.017); `[0,20]` **2.252\*\*** (0.954; 0.018 / 0.035). Prose: the response is **not immediate**, accumulating mainly after day 3.
- **Table 12 raw market-adjusted CARs:** Inclusion **N=595**: `[−10,−1]` −0.85%, `[0,3]` −0.32%, `[0,5]` 0.00%, `[0,10]` **+1.14%**; Exclusion **N=375**: `[0,10]` −0.62%; Continuous compliant **N=12,024**: `[0,10]` −0.28%.
- **Table 13 matching balance (treated vs control, standardized difference):** log market cap 19.122 / 19.125 (−0.002); pre-event return 0.001 / 0.001 (−0.004); volatility 0.036 / 0.034 (0.084); turnover 0.0066 / 0.0058 (0.065); Amihud 7.99e−06 / 5.25e−06 (0.085); log dollar volume 12.992 / 12.689 (**0.150**, the largest).
- **Table 16 screen sensitivity (`[0,10]` mean, `p_date`, `p_wild`):** turnover quartile N=307 → 1.84% (0.004 / 0.014); tercile N=273 → 1.62% (0.022 / 0.038); median N=205 → 2.53% (0.003 / 0.009); **market-cap** quartile N=307 → 0.87% (0.173 / 0.174); market-cap median N=205 → 0.60% (0.471 / 0.493).
- **Table 17 turnover slopes** (`p_wild` in parentheses): inclusion indicator **2.007\*\*** (0.051) `[0,10]`, **1.768\*** (0.089) `[0,20]`; exclusion turnover slope **−3.543\*\*\*** (0.010) / −3.365\*\* (0.083); **inclusion turnover slope 0.086 (0.925) / −0.027 (0.979)**. Source prose: the earlier positive inclusion-by-turnover interaction came from the negative exclusion slope and "cannot be interpreted as the inclusion effect rising with turnover."
- **Influence / repeats:** leave-one-list-date-out `[0,10]` ranges **1.29 – 1.98 pp** and `[0,20]` **1.78 – 2.55 pp** (Figure 6); **295 events over 237 distinct securities (44 repeats; our count ≈ 12.3 events per release across 24 clusters)**; two-way date-security clustering `p_wild` 0.008 / 0.015; first-inclusion-only **N=237** → 1.69 / 2.41 (both significant under list-date wild cluster); strict same-date same-SIC **N=266** → **0.87 / 1.48, imprecise**.
- **Table 19 mid-review timing placebo (fixed matched sets shifted three calendar months earlier):** `[0,10]` 0.841 (SE 1.151; 0.465 / 0.473), `[0,20]` 0.895 (1.181; 0.449 / 0.466), `[0,1]` 0.222, `[0,3]` 0.243, `[0,5]` 0.988 — all insignificant.
- **Ownership / channel diagnostics (Table 18, treated change vs control change, difference, `p_wild`):** Shariah-sensitive portfolio **+0.022 vs +0.000, diff 0.021 (0.360)**; broad mandate-constrained +0.017 vs −0.036, diff 0.053 (0.282); global passive placebo −0.002 vs −0.001, diff −0.001 (0.832). Appendix channel test: predicted constrained-pressure proxy predicts ownership change (`p_wild` 0.037) but its **CAR coefficient is negative and insignificant**; ETF capacity/creations do not explain CARs.
- **Route A monitoring (Table 8, logit, z in parentheses, N=300,000, two-way security/month clustering, year FE):** implemented disagreement **1.1609\*\*\*** (39.75); proximity risk **3.2384\*\*\*** (30.61); log market cap −0.0557\*\*\* (−8.48); Internet-Appendix IDIT-only-proxy rebuild gives 1.0687 and 3.1006.
- **Route A Fama–MacBeth (Table 9, standardized slopes, Newey–West 12 lags):** eligibility share baseline **0.0013\*\*\*** (t 4.13) → +quality **0.0005 (1.62)** → +quality+screens **−0.0001 (−0.35)**; implemented disagreement 0.0015\*\*\* (4.47) → 0.0010\*\*\* (2.76) → 0.0007\*\* (2.54). IDIT-only: eligibility −0.0005 (t −1.94), disagreement 0.0006 (2.42).
- **Route A September 2023 shock (Table 10, market-model CAR, winsorized 1/99, HC3 t):** announcement **Aug 4 2023**, unmatched newly-both **0.750\*\*** (2.31) `[0,1]`, **1.210\*\*\*** (2.63) `[0,3]`, 1.013\* (1.79) `[0,5]`, 1.310\* (1.85) `[0,10]`; **matched vs still-ineligible 0.368 (0.89), 0.643 (1.09), 0.818 (1.04), 1.249 (1.37) — all insignificant**; matched vs continuously eligible −0.612 (−1.04), −0.069, 0.418, 1.367. Pro-forma **Sep 1 2023** matched vs still-ineligible −0.662, −0.920, **−1.669\*\* (−2.24)** `[0,5]`, −0.355.
- **Route A placebos (Table 11, matched newly-both vs still-ineligible, `[0,3]` / `[0,5]`):** 2019 0.615 / −0.376; **2020 2.088\*\*\* (2.62) / 0.202**; 2021 −0.123 / −0.273; **2022 −1.895\*\*\* (−3.53) / −2.670\*\*\* (−3.99)**; 2024 −0.647 / −0.292.
- **Sample size anchors:** Route A 13,188 securities / 1,342,606 security-months (1999–2024), seven emulated rulebooks; Route B 25 semi-annual lists (Nov 2013 – Nov 2025), 859/661 official inclusion/exclusion transitions.
- **Our arithmetic on printed cells (our count, not a source number):** 1.759 pp over 10 trading days ≈ **0.176 pp per trading day gross**, unannualized; 295 events over 24 clusters ≈ **12.3 eligible names per release**. No annualized return, Sharpe, drawdown or win rate is stated anywhere in the source.

### Independently reproduced

not independently reproduced.

### Negative evidence

1. **No cost, fill, borrow, capacity, turnover or P&L model exists** (scan above); the effect is gross and un-costed, and the source itself lists "implementation lags, transaction costs, and investable capacity" among the requirements a tradable strategy would need (§8).
2. **The joint pre-event test rejects:** a list-date-clustered joint Wald test of the **20 daily pre-event coefficients** rejects equality to zero (**p = 0.006**), driven by isolated days −17 and −11; the source says it "cannot be ignored" and that it "limits a clean parallel-trends or causal interpretation."
3. **Significance is conditional on the turnover-qualified sample.** The 410-event continuously listed sample — the natural baseline — is **not significant** at `[0,10]` (0.896, p_wild 0.134); the source states "the stronger inference emerges at the turnover-screen step, not merely from removing new listings."
4. **No dose-response with liquidity:** the inclusion turnover slope is 0.086 (p_wild 0.925) and −0.027 (p_wild 0.979); market-cap screens do **not** reproduce the result (0.87 %, p_wild 0.174; 0.60 %, p_wild 0.493).
5. **Strict industry matching weakens it:** same-date same-SIC N=266 → 0.87 / 1.48, imprecise.
6. **The mechanism's first stage is unproven:** treated-minus-control Shariah-sensitive ownership change 0.021 pp with **p_wild 0.360**; broad-constrained 0.053 (0.282); pressure proxies enter with signs inconsistent with simple buying pressure; ETF capacity does not explain CARs; the paper states it identifies **neither a security-level demand instrument nor a unique marginal buyer**.
7. **US evidence fails the same hypothesis:** equal-weighted permission premium vanishes with controls (−0.0001, t −0.35), the September 2023 DJIM/S&P shock has **no significant matched repricing**, and the 2019/2020/2021/2022/2024 placebo distribution is unstable (2020 strongly positive, 2022 strongly negative) — "the price evidence is too fragile to support an unconditional inclusion-premium interpretation."
8. **One-sided and not immediate:** exclusions are not persistently negative under release-date timing (−0.62 % `[0,10]`, not robust), so there is no printed hedge leg; `[0,1]` is **negative and insignificant (−0.233)**, so any same-day/next-day entry assumption is unsupported by the printed profile.
9. **Small-cluster inference:** only **24 non-baseline list-date clusters**, 999 wild replications, 44 repeat securities; 27 tables and many windows are printed with **zero multiplicity control** (`Benjamini`/`Bonferroni`/`multiple testing`/`false discovery`/`deflated` all 0 hits) and **zero point-in-time/look-ahead language** (`point-in-time`/`look-ahead`/`walk-forward` all 0 hits).
10. **The printed liquidity floor is full-sample:** `Q^turn_0.25` is computed "in the full matched event universe before treatment-specific filtering" — a retrospective cutoff a live rule could not have known without recomputing it per release.
11. **External validity is a single recognized local market.** The paper's own conclusion: official permission has price content "in a recognized local market among sufficiently tradable securities; formal eligibility alone is insufficient" — the US route shows the label alone does not reprice.
12. **Source quality / reproducibility:** preprint-only (no peer review stated); replication package promised in future tense; CRSP/Compustat/WRDS/LSEG inputs non-redistributable; parser shortfall on the earliest PDF; generative-AI use declared (LaTeX only); `arXiv.org perpetual non-exclusive` licence rather than CC.
13. **No ex-ante strategy is claimed by the authors** — an explicit statement, not our inference.

## Falsification plan

Every threshold below is **research-defined**; every operational rule not printed by the source is **research-proposed**. Each test names data, sample/regime, metric, decision rule and the action on failure.

- **F1 - Point-in-time, forward releases** (`research-proposed` rule, `research-defined` threshold). Rebuild the floor **recursively from prior releases only**, freeze the filter (continuously listed + turnover >= prior-cross-section Q25) before each review, and trade SC releases from **Nov 2025 forward for >= 8 releases (>= 16 independent list-date/security clusters)**. Threshold: mean `diffCAR[0,10]` >= **0.9 pp** with one-sided wild-cluster **p < 0.05**, and positive in >= 6 of 8 releases. **Action on failure:** the printed effect is partly full-sample-threshold look-ahead; close the tradable reading.
- **F2 - Pretrend repair** (`research-proposed`). Re-match with entropy balancing / calipers until the **joint `[−20,−1]` Wald test has p > 0.10**, then re-estimate `[0,10]`. Threshold: effect >= **1.0 pp** with `p_wild < 0.05` **while** the pre-trend test passes. **Action on failure:** classify the pattern as anticipation/drift contamination rather than post-release repricing.
- **F3 - Cost ladder with local levies** (`research-proposed` cost lines, `research-defined` thresholds). Re-book the long-only window at **0 / 5 / 10 / 20 / 30 bp per side**, plus a variant that adds Malaysia-specific statutory/brokerage charges (rate to be researched at implementation time; **the source states no rate**), at **20% ADV** and **10% ADV** participation. Threshold: net > 0 at 10 bp and >= **0.5 pp** at `[0,10]` with no sign flip before 30 bp. **Action on failure:** no investable claim; the record stays a documentation/event finding.
- **F4 - Full placebo-date battery** (`research-defined`). 1,000 pseudo-release dates drawn from non-review months, matched on weekday, month and trailing volatility, each with the same matching machinery. Threshold: the observed `[0,10]` exceeds the **95th percentile of the placebo mean-|diffCAR| distribution** and placebo means lie within **±0.3 pp** of zero. **Action on failure:** the window is calendar-structured noise.
- **F5 - Benchmark and weighting robustness** (`research-proposed`). Re-estimate with (a) a `[−250,−30]` market-model benchmark, (b) value-weighted treated portfolios, (c) same-SIC-only controls. Threshold: all three keep `[0,10]` >= **0.8 pp** with `p < 0.05`. **Action on failure:** the drift is a small-cap/value-weight or benchmark artefact.
- **F6 - Short-leg test** (`research-defined`). Short the 257 floor-qualified **exclusions** over `[0,10]`/`[0,20]`. Threshold: `diffCAR <= −0.5 pp` with `p < 0.05`. **Action on failure:** withdraw every long-short framing; the hypothesis is explicitly long-only and one-sided.
- **F7 - Second-jurisdiction transport** (`research-defined`). Replicate the identical pipeline on **>= 2 additional published, dated official/authoritative Islamic-eligibility or constrained-universe classifications** outside Malaysia. Threshold: same-signed `[0,10]` >= **0.5 pp** with `p < 0.05` in at least 1 of 2 after **Benjamini-Hochberg q < 0.10**. **Action on failure:** the mechanism does not transport; treat it as a Malaysia-institutions result only.
- **F8 - Capacity / participation audit** (`research-defined`). Cap at 10% ADV and require >= 80% of signal weight to sit above MYR-equivalent **5 million** daily dollar volume (research-defined floor). Threshold: the `[0,10]` estimate shrinks by **< 50%** relative to the printed 1.759 pp. **Action on failure:** effect is concentrated in untradable small names; capacity unknown, implementation withdrawn.
- **F9 - Mechanism first stage** (`research-defined`). With an independent dated ownership dataset, require treated-minus-control mandate-sensitive ownership change >= **0.05 pp** with `p_wild < 0.05` (the printed estimate is 0.021 with p 0.360). **Action on failure:** keep the price pattern but downgrade the mechanism to "channel undetermined"; do not attribute it to constrained demand.
- **F10 - Multiplicity audit** (`research-defined`). Apply Benjamini-Hochberg at **q = 0.10** across every printed window x specification x screen combination (Tables 12–19 and appendix), counting the three ladder steps as three looks. **Action on failure:** if the `[0,10]`/`[0,20]` results do not survive, record the finding as exploratory and lower `confidence` to `low`.

## Crypto portability

`unproven`.

There is no crypto equivalent of a **public authority issuing a single dated binary eligibility list** for a recognized mandate-governed capital pool, and no evidence in the source that the mechanism operates outside listed equities. Specific breaks: the day-0 = "first trading day on or after the PDF release date" convention assumes exchange sessions and a business-day document clock, versus **24/7** crypto sessions and continuous listing; there is no analogue of **Compustat listing history** for "continuously listed", no Amihud/turnover floor calibrated to crypto liquidity, and no treatment of **perpetual funding, mark/index price, liquidation, borrow/short availability or venue fragmentation** — none of which the source models even for equities. Nearest analogues (index/ETF additions, exchange listing events, collateral-eligibility changes) are different mechanisms and would need their own records. Portability is a **ported hypothesis**, not crypto empirical evidence.

## Limitations

- `underspecified`: entry price/time-of-day, sizing, weighting, exit mechanics, shorting, any cost line, Route B tail treatment.
- `data gap`: publication time-of-day of the SC PDF; per-author affiliation mapping; mandate-capital weights (the structural `m_i` is never estimated — the source says so); official-provider decisions (Route A uses *emulated* rulebooks).
- `not independently reproduced`: every number in Evidence/Source-reported.
- `unproven`: the constrained-buyer channel (Table 18 and channel diagnostics are imprecise); causality (pretrend joint test rejects); ex-ante profitability (explicitly not claimed by the authors).
- Small-cluster, single-market, single-authority inference (24 clusters, 25 releases); effect concentrated after day 3 with a negative insignificant `[0,1]`.
- Significance depends on a retrospectively computed turnover floor; market-cap screens fail; same-industry matching fails precision.
- Preprint-only, non-CC licence, future-tense replication package, proprietary non-redistributable inputs, declared generative-AI use.
- Incremental-write check: no prior Shariah/Islamic-eligibility record exists in this repository (0 hits), and the four-axis distinction above shows the mechanism, universe and data dependency all differ from the existing forced-flow records.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack: no event parser, no matching replication, no portfolio, no backtest, no Qlib run, and no Paper/Testnet/Live activity of any kind. The only executed work this run was source verification (landing page, pinned HTML, DOI resolution, repository-wide dedup, Wiki Brain read-only spec resolution and read-only linkage search).

## Adoption boundary

A record being present here does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. This is research material only, and the source itself states that no profitable pre-reclassification strategy has been established.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — authoritative record specification (read via `kb_read`; `v2` does not exist, sha256 `4561578a…ff6fcaa7`).
- `[[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]]` — adjacent forced-flow/event-drift family; **different mechanism (benchmark-index mandate vs religious-eligibility mandate), universe (US large caps vs Bursa Malaysia) and signal dates (announcement/effective vs regulator release)**.
- `[[quant/buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13]]` — adjacent event-study family; **firm-initiated disclosure vs regulator-issued permission labels**.

Wiki Brain `kb_search` (read-only) for `Shariah screening Islamic equity eligibility`, `constrained investor demand segmentation index inclusion forced flow`, and `mandate constrained feasible universe exclusionary screening prices` each returned **0 results**, so no further page is asserted; no page was fabricated and **no Wiki Brain write was performed**.

## Sources

1. Abdulrahman Qadi, Akash Sharma, Francesca Medda, *"The Price of Permission: Classification Uncertainty in Constrained Capital Markets"*, `arXiv:2608.12634v1 [q-fin.ST]`, submitted Wed, 12 Aug 2026 22:49:26 UTC (781 KB), 67 pages / 20 figures / 27 tables, arXiv.org perpetual non-exclusive licence, preprint only (no Journal-ref, no publisher DOI, no peer-review statement). https://arxiv.org/abs/2608.12634
2. Pinned v1 full text read end to end on 2026-09-25: https://arxiv.org/html/2608.12634v1 (681,681 bytes) — all figures cited above carry Table/Section anchors into this text.
3. DataCite DOI `10.48550/arXiv.2608.12634` → HTTP 302 → https://arxiv.org/abs/2608.12634 (checked 2026-09-25). https://doi.org/10.48550/arXiv.2608.12634
4. Securities Commission Malaysia, *List of Shariah-Compliant Securities, Semi-Annual Releases, 2013–2025* [dataset], cited by §4.3 of the source; archive URL read from the pinned v1 reference anchor: https://www.sc.com.my/development/icm/icm-publications/list-of-shariah-compliant-securities
