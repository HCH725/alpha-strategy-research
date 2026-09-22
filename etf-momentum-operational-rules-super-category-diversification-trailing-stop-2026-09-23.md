---
schema: strategy-research-record-v1
title: US ETF cross-sectional momentum rescued by an operational layer — entry filter, super-category diversification and dynamic trailing-stop/MA exits (SSRN 7379989)
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - etf
  - momentum
  - tactical-asset-allocation
  - stop-loss
  - portfolio-diversification
  - regime-dependence
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-08-31
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7379989"
  - "https://doi.org/10.2139/ssrn.7379989"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# US ETF Cross-Sectional Momentum under Simple Operational Rules (Entry Filter + Super-Category Diversification + Dynamic Exits)

## Provenance

**Primary source (pinned version, read in full this run):**
Nicolás Magner, Aliro Joel Sanhueza, *"Momentum Strategies in ETFs under Simple Operational Rules: Economic Value and Conditional Predictability"*, Available at SSRN: `abstract_id=7379989`, DOI `10.2139/ssrn.7379989`.

- **Complete author list exactly as source (SSRN abstract page and PDF):** Nicolás Magner — Universidad Diego Portales; Aliro Joel Sanhueza — Universidad Diego Portales. No other authors, no acknowledgements of additional contributors on the abstract page.
- **Version/date:** SSRN abstract page (read 2026-09-23): 28 pages, **Posted: 31 Aug 2026**, no "Last revised" field and no "Date Written" field displayed → version-history / date-written `not stated in source`. Record `source_as_of` = 2026-08-31 (SSRN posting date). Sample end (2026-05-15) is recorded separately under Required data.
- **Sample period / universe (§3.1):** **2001-08-31 → 2026-05-15, T = 1,289 weeks (24.7 years)**; universe = **3,215 U.S.-listed investable ETFs** after four operational-viability filters; leveraged and inverse products (77 ETFs across seven Refinitiv Trading–Leveraged/Inverse/Miscellaneous categories) excluded.
- **Primary-source checksum (performed 2026-09-23):** SSRN abstract page opened directly in a browser session after the Cloudflare check, then the 28-page PDF downloaded through the same cleared session (local file 784,136 bytes, **SHA-256 `4a5d3cce67b2c64d4715c7e1cee218498b8c04a6b80bbce549ad15e50fb1e136`**) and read end-to-end: §1–§5, §6.1, **Tables 1–5** (Panels A–D of Tables 2, 3 and 4), References (46 entries). Every quantitative field below is anchored to that pinned PDF by Table/Section.
- **Transaction-cost treatment (read from §3.1 Methodology, not from the abstract):** every purchase and every sale pays **20 basis points per side**, embedded in the return series *before* evaluation ("in the return rather than as an ex-post adjustment", §1; `0.002 · ωi,t` on the traded capital, §3.2), stated to be "representative of retail brokers and effective spreads in liquid markets" (§3.1). Idle cash earns the 3-month T-bill (FRED DTB3) and **incurs no entry/exit cost** (footnote 4). Passive benchmarks are charged **zero** transaction costs for their initial purchase and annual rebalancings (§3.1). **Spread is not separately modelled** (folded into the flat 20 bp) → `data gap`; **market impact, borrow, short-selling, funding and latency are not modelled** (long-only design, no shorting) → `not stated in source`.
- **Publication / peer-review status:** SSRN preprint; every PDF page carries "This preprint research paper has not been peer reviewed", and the abstract page states "it offers immediate access but has not been peer reviewed" → **peer-review status: preprint, not peer-reviewed (source-stated)**; no journal reference, no non-SSRN DOI.
- **Rights:** SSRN license notice reads "The copyright holder has granted SSRN a license. All rights reserved. **No reuse allowed without permission.**" → this record cites and normalizes the rules and short figures only; no wholesale copying.
- **Code/data availability:** no repository, supplement link or data-share statement appears on the abstract page or in the PDF; the full 144-rule frontier, the frequency matrix and the conditional-Sharpe table are repeatedly deferred to "supplementary material" that is **not contained in the 28-page PDF** → `data gap`.

**Whole-repository source-identity dedup (performed before writing, 2026-09-23):** ripgrep across **all 876 `*.md` records plus `coverage_manifest.csv`** for `7379989`, `10.2139/ssrn.7379989`, `Momentum Strategies in ETFs`, `Simple Operational Rules`, `Magner`, `Sanhueza`, `Diego Portales`, `3,215`, `super-category`, `mandatory diversification` → **zero source-identity hits** (the only matches for the generic terms `Jobson` were three unrelated records: `finatom-head-free-token-generation-etf-allocation-dapo-grpo-2026-09-04.md`, `path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03.md`, `intraday-overreaction-momentum-finbert-emotion-classifier-2026-09-05.md`, which merely name the same test statistic). Mechanism neighbours were checked and are materially distinct: `simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11.md` (arXiv 2609.07946, convex Markowitz/vol-target allocation over 3 assets, different source and construction), `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (funding carry factor, different asset class and signal), plus Chinese-language FMZ ETF entries in `coverage_manifest.csv` still flagged `needs_semantic_review`. Material distinction from every neighbour: **source identity** (DOI 10.2139/ssrn.7379989, unique), **universe** (3,215 U.S. listed ETFs vs. single-name/crypto/futures), **signal construction** (C₂∩C₆ technical entry filter + multi-horizon cross-sectional momentum score + mandatory super-category caps + SP/ST/TSL/TP exit stack), **horizon/regime** (weekly Friday decisions, biweekly entries, 25-year tactical allocation, VIX>25 conditioning). Not a reframing of an existing record.

## Economic mechanism

### Source-reported

The authors' thesis is explicitly anti-signal: "pure momentum over a broad ETF universe creates no value", and the value comes from "the operational management layer that surrounds it" (Abstract, §5). Mechanisms they invoke: (a) the momentum anomaly is robust for stocks and asset classes but does not survive the translation to the ETF vehicle on narrow samples (§1, §2, citing Tse 2015, Andreu et al. 2013, Zaremba–Andreu 2018, Vanstone et al. 2021, Wang–Wu 2024); (b) an entry filter (golden cross ∩ 52-week breakout) removes non-trend regimes before capital is committed (§4.1); (c) mandatory super-category diversification prevents the momentum score from concentrating eight slots on the same underlying factor (SPY/IVV/VOO example, §3.1), converting idiosyncratic dispersion into breadth; (d) dynamic exits (7% trailing stop or SMA200 overlay, plus native MA50/death-cross exits) truncate the left tail, which is where the entire measured advantage sits (§4.2); (e) the surviving fragility is the volatility regime, not the business cycle — cross-category correlations converge to one under systemic stress so diversification "stops working" (§4.3, framed through the Adaptive Markets Hypothesis, Lo 2004/2017).

### Research interpretation

Falsifiable decomposition (our framing): the reported Sharpe gain from −0.17…+0.22 to >1.3 is **risk management plus breadth, not predictive ranking** — the ranking layer's own contribution must be isolated by ablation before any claim of momentum alpha. Component roles (roles source-reported; the ablation attribution is our research reading and is not established by the source):

```text
Regime / entry filter:  C2 ∩ C6 = golden cross (MA50 > MA200) AND 52-week-high breakout,
                         evaluated at each Friday close (chosen ex post from 63 subsets)
Primary ranking signal: multi-horizon cross-sectional momentum score
                         0.35·rank(r26) + 0.35·rank(r13) + 0.20·rank(dMA30) + 0.10·rank(r4)
Confirmation / breadth:  N = 8 slots × 12.5%, eleven super-categories with per-category caps,
                         unfilled slots earn 3-month T-bill
Risk / exit:            native SP (halve position when price < MA50, reversible) and
                         ST (full exit on death cross) + dynamic SL/TP layer
                         (frontier: TSL07 7% trailing stop, or MA_SMA200_OV with TP100)
Cadence:                entries every other Friday, exit monitoring every Friday
```

Do not read the composite as eight independent alpha sources: per README rule 8, stops, sizing caps and cadence are **risk management, not alpha**, and the paper's own numbers say the CAGR gain over SPY is statistically insignificant (Table 3 Panel C).

## Signal

All of the following is `source-reported` with anchors; nothing below is Scout-operationalized unless explicitly labelled.

- **Formation timestamp / tradability (§3.1):** daily dividend- and split-adjusted prices aggregated to **weekly Friday closes**; every decision uses Friday-t closes or earlier (footnote 1, "without look-ahead"). Exits (SP/ST/SL/TP) are evaluated **every Friday**; a position breaching an exit during the week is liquidated **that same Friday**. Entries into free slots are rebalanced **every other Friday**. Whether intraweek breaches are detected on daily bars or only at Friday close is not fully specified → `underspecified` (the text says "if a position breaks its exit criteria during the week, the rule liquidates it that same Friday", implying daily monitoring; the monitoring frequency itself is not stated as a formal rule).
- **Universe filter M(i,t), four viability conditions (footnote 2):** (i) ≥ 52 weeks of continuous history; (ii) 13-week rolling median of daily volume > USD 100,000; (iii) ≥ 90% non-null closes in the 252-day rolling window; (iv) exclusion of leveraged (2×/3×) and inverse products (77 ETFs, seven Refinitiv categories).
- **Entry filter (Table 1 Panel A):** six candidate conditions C1 price>MA50; C2 MA50>MA200 (golden cross); C3 MA50 10-week slope>0; C4 MA200 10-week slope>0; C5 higher highs and higher lows over 13 weeks; C6 P_t > max P over the prior 252 days (52-week breakout). **Adopted specification: C₂ ∩ C₆**, chosen **ex post** from the 2⁶−1 = 63 non-empty subset ablation (§4.1); the source explicitly defends the choice as "the conservative end of the informationally equivalent band" because all subsets collapse into only two Sharpe outcomes (0.881 without C₅, 0.945 with C₅).
- **Ranking score (Eq. 1, §3.1):** `score = 0.35·rank^cs(r26) + 0.35·rank^cs(r13) + 0.20·rank^cs(dMA30) + 0.10·rank^cs(r4)`, where `rank^cs` ∈ [0,1] is the cross-sectional percentile on date t, `r26/r13/r4` are 26/13/4-week returns and `dMA30` is the normalized distance to the 30-week rolling average. Candidates are scanned in descending score and fill empty slots up to N = 8.
- **Slot weights and cash:** 12.5% gross per filled slot; unfilled capital stays in cash earning the weekly 3-month T-bill (FRED DTB3); cash pays no costs.
- **Mandatory diversification (§3.1, Table 5):** eleven Refinitiv-aggregated super-categories with caps — US_LARGE_CAP 2, US_MID_SMALL 1, US_SECTORAL 2, INTL_DM_EQUITY 1, EM_EQUITY 1, GOV_BONDS 1, CORP_BONDS 1, MONEY_MARKET 1, COMMODITIES 1, REITS 1, OTHER 1 (caps sum to 13 > 8). A candidate whose category is already full is rejected during the score scan; with all eight slots filled the portfolio necessarily spans ≥ 4 distinct super-categories.
- **Native technical exits (§3.1):** **SP** — partial exit reducing the position to 50% when price leaves the zone above the 50-day MA (C1 breaks); reversible to 100% at no cost if price reclaims MA50. **ST** — full liquidation when the golden cross inverts (death cross, C2 breaks); permanent for that position, ST takes priority over SP; the ETF may re-enter later if it again passes the entry filter.
- **Dynamic exit family (Table 1 Panel B, §3.2):** 23 stop-loss configurations in five families — F1 fixed SL% {5,7,10,15,20}% from entry price; F2 trailing SL% {7,10,15,20}% from the running maximum (TSL07 = 7% trailing); F3 rolling weekly low over N ∈ {10,20,40} weeks; F4 Chandelier `max price − M·ATR^W_14`, M ∈ {2,3,4}; F5 dynamic MA {EMA5W, SMA50, SMA100, SMA200} as *overlay* (coexists with SP/ST) or *replace*. Take-profits {TP30, TP50, TP60, TP100, TP200} at β ∈ {30,50,60,100,200}% above entry, immediate full exit. Grid = 23×6 + 5 + 1 = **144 combinations** (§3.2).
- **Implementability screen (§3.2, source-defined):** only rules with **SlotChg/yr ≤ 20** (bilateral slot changes per year) are retained; 70 of 144 rules exceed it and are discarded despite nominally higher Sharpe (ATR2 1.42 at 40 slots/yr; EMA5W 1.39 at 51 slots/yr).
- **Reported frontier rule (Table 3 Panel A):** **TSL07** (C₂∩C₆ entry + ranking + caps + 7% trailing stop + native SP/ST) and **MA_SMA200_OV_TP100** are the two leaders.
- **Parameters source:** every threshold above (MA windows, 52-week breakout, score weights 0.35/0.35/0.20/0.10, N=8, caps, SL/TP grid, ≤20 SlotChg/yr) is `source-reported`; the specific adoption of C₂∩C₆ and TSL07 as "the" strategy is an **in-sample (ex post) selection reported by the source**, not an out-of-sample result. No Scout-added operational rule exists in this record.
- **Fully specified?** Almost: score, filters, caps, exits and cadence are reconstructible. Unspecified: intraweek monitoring frequency formalization, delisted-ETF handling in the universe, how ties in the score scan are broken, and the numerical frequency-matrix/conditional-Sharpe tables (supplementary) → `underspecified` / `data gap`.

## Required data

- **Instruments:** 3,215 U.S.-listed ETFs (equity, sector, fixed income, commodity, REIT, money-market, "other"), long-only; 77 leveraged/inverse ETFs excluded by rule.
- **Venue / vendor:** Refinitiv DataStream daily prices adjusted for dividends and splits, plus the Refinitiv sector (Morningstar-style) classification and leveraged/inverse product markers (§3.1). Replication with a different vendor is an open item (not stated as possible by the source) → `data gap`.
- **Timeframe / session:** daily series aggregated to Friday weekly closes; U.S. equity session; sample 2001-08-31 → 2026-05-15 (T = 1,289 weeks).
- **Macro fields (FRED, daily → weekly Friday, Table 1 Panel C):** VIXCLS (>25 threshold, active 17.8% of weeks), USREC (NBER recession, 7.4%), T10Y3M (<1pp, 36.3%), BAA10Y (> historical 75th percentile, 30.3%); cash yield DTB3.
- **Point-in-time / look-ahead:** decisions use Friday-t closes or earlier only (footnote 1); warm-up series may extend into the 1990s and are used only for MA/rolling-high computation (footnote 3). **Survivorship / delisted-ETF treatment is not stated** → `data gap` (the four filters condition on ≥52 weeks of history but the source never says whether delisted ETFs remain in the panel after listing ends).
- **Missing data:** ≥90% non-null closes in the 252-day window is the only stated rule; no imputation is described.

## Execution assumptions

- **Order type / fill model:** not stated as market vs limit; the design implies execution at the Friday close used for the signal (entries and exits both dated Friday) → same-bar close execution, `source-reported by construction`, latency `not stated in source`.
- **Fees / spread / slippage:** **20 bp per side, embedded pre-trade** on every purchase and sale (§3.1, §3.2); flat, described as covering retail broker commission and effective spread; cash trades cost zero; benchmarks costed at zero. Slippage as a separate distribution, spread as a separate series, partial fills, order-queue position and market impact → `not stated in source` (impact/capacity: only an operational proxy via SlotChg/yr ≤ 20 and an implied cost toll of ~0.7–0.9 pp/yr for TSL07 and ~0.5–0.6 pp/yr for MA_SMA200_OV_TP100, §4.2 Panel C discussion).
- **Leverage / margin:** none — eight 12.5% slots sum to 100%; no margin use.
- **Shorting / borrow:** none (long-only; exits are liquidations to cash) → borrow cost `not applicable`.
- **Funding / liquidation:** `not applicable` (spot ETF, no derivatives).
- **Capacity:** not modelled beyond the ≤20 SlotChg/yr implementability screen; AUM/volume-participation caps `not stated in source`.
- **Benchmark cost asymmetry:** active rule pays 20 bp/side, benchmarks pay zero (§3.1) — conservative for the active rule, but it also means benchmark-relative deltas mix a cost difference with a signal difference (`research interpretation`).

## Evidence

### Source-reported

All figures are `source-reported`, net of the embedded 20 bp/side, rf = 3%/yr, annualized by √52 (§3.1), from the pinned PDF (SHA-256 `4a5d3cce…1e136`):

- **Pure-momentum baseline, Tse (2015) replication on the full universe (Table 3 Panel D):** cross-sectional top-8 momentum, no filters/caps/SL-TP — 1-month **Sharpe +0.215 / CAGR 6.51% / MaxDD −69.52%**; 3-month **−0.008 / 2.87% / −76.75%**; 6-month **−0.043 / 2.32% / −75.76%**; 12-month **−0.167 / 0.39% / −81.88%** (SlotChg/yr 35.7–35.9). **SPY buy-and-hold reference: Sharpe +0.459 / CAGR 9.81% / MaxDD −54.44%.** All four gaps vs TSL07 significant at p<0.001 (JK–Memmel). Abstract/conclusion restate the range as Sharpe −0.17…+0.22 with drawdowns 69%–82%.
- **Entry-filter ablation (Table 2):** the 63 subsets collapse to two outcomes — with C₅ **Sharpe 0.9450** (CAGR 11.98%, MaxDD −14.07%), without C₅ **Sharpe 0.8810** (CAGR 11.56%, MaxDD −13.81%, CVaR₉₅ 2.80%, SlotChg/yr 8.1); **within-grid differences are insignificant on every metric (p = 0.16–0.90, Table 2 Panel C)**; five of six conditions are informationally redundant (pairwise Jaccard > 0.99 on the filtered universe). C₂∩C₆ vs SPY: **ΔSharpe +0.408 (p=0.01)**, **ΔCAGR +1.75pp (p=0.58, not significant)**, **ΔMaxDD +40.6pp (p<0.001)**, **ΔCVaR₉₅ −2.86pp (p<0.001)**.
- **Implementable frontier (Table 3 Panel A):** **TSL07 Sharpe 1.336 (CI95 [1.26, 1.41]) / CAGR 13.26% / MaxDD −6.98% / CVaR₉₅ 1.83% / Ω 1.99 / skew +1.22 / SlotChg 16.8 / Cash 19.0% / Z vs SPY +4.46 (p<0.001)**; TSL07_TP50 1.336; TSL07_TP100 1.329; TSL07_TP30 1.327 (MaxDD −7.91%); **MA_SMA200_OV_TP100 1.320 / CAGR 14.84% / MaxDD −11.04% / SlotChg 12.5**; MA_SMA200_OV 1.291; MA_SMA200_OV_TP60 1.277. Take-profit on top of the trailing stop is redundant (variants indistinguishable to the third decimal, §4.2.1).
- **Paired tests (Table 3 Panels B–C):** TSL07 vs BASELINE (no SL/TP control) **ΔSharpe +0.299 (p=0.01)**, ΔCAGR +0.34 (p=0.83), ΔMaxDD +7.10pp (p=0.02), ΔCVaR₉₅ −1.02pp (p<0.001). TSL07 vs SPY B&H **ΔSharpe +0.812 (p<0.001), ΔCAGR +3.45 (p=0.31 — not significant), ΔMaxDD +47.46pp (p<0.001), ΔCVaR₉₅ −3.83pp (p<0.001)**; vs VTI+EFA 50/50 **+0.885 (p<0.001)** with ΔCAGR +4.69 (p=0.17); vs 60/40 SPY+AGG **+0.744 (p<0.001)**; vs IEF **+1.171 (p<0.001)**. TSL07 vs MA_SMA200_OV_TP100: ΔSharpe +0.016 (p=0.51, indistinguishable); both beat BASELINE at p<0.01.
- **Regime conditioning (Table 4 Panels A–D, §4.3):** weekly-regression intercepts α are positive and significant for all five rules (**BASELINE +0.288, TSL07 +0.320, MA_SMA200_OV_TP100 +0.348 pp/week**); the **only significant regime coefficient is β₁(VIX>25): −0.621 (BASELINE), −0.457 (TSL07), −0.524 (MA_SMA200_OV_TP100), −0.500 (TSL10), −0.585 (ATR4)**; NBER, TERM_LOW and CREDIT_HIGH are insignificant in every panel. TSL07 therefore goes from +0.32 pp/week in normal weeks to ≈ −0.14 pp/week when VIX>25 (§4.3). Same signs/magnitudes in both balanced subperiods (2001-08→2013-12, n=643; 2014-01→2026-05, n=646) and across **519 rolling 260-week windows where β₁(VIX>25) is significant in 80–92% of windows** while the other three indicators sit near the 5% chance level.
- **Conditional Sharpe (§4.3 text; table itself is supplementary):** five rules **1.27–1.66 unconditionally**, collapsing to **−0.83 (TSL07) … −1.20 (ATR4) when VIX>25 (17.8% of weeks)**; ≈0 in NBER weeks; 1.5–2.0 in TERM_LOW and CREDIT_HIGH weeks.
- **Operational toll (§4.2):** ≈0.7–0.9 pp/yr (TSL07) and 0.5–0.6 pp/yr (MA_SMA200_OV_TP100) of cumulative 20 bp costs vs CAGR deltas of +3.5pp (vs SPY, n.s.) to +11.6pp (vs IEF, p<0.001).
- **Cost/regime robustness claim (§5):** "from the monthly rebalancing onward, no active rule beats passive investing" — the underlying 5-rules × 6-frequencies = 30-simulation matrix numbers are **not in the PDF** → `data gap`.

### Independently reproduced

not independently reproduced

### Negative evidence

- **The source's own baseline is the strongest counter-evidence:** textbook cross-sectional ETF momentum (1/3/6/12-month lookbacks) is below passive on every lookback, with 69%–82% drawdowns (Table 3 Panel D) — the "alpha" claim lives or dies on the management layer, not on momentum.
- **No absolute-return alpha vs equity:** ΔCAGR vs SPY is +3.45pp with **p = 0.31** (Table 3 Panel C); the paper's economic contribution is entirely left-tail truncation. A risk-managed equity/60-40 alternative is the relevant control, not raw momentum.
- **Structural regime failure (source-stated, §4.3, §5):** VIX>25 reverses the strategy (conditional Sharpe −0.83…−1.20), is significant in 80–92% of rolling windows, and the paper concedes "there is no internal hedge against that risk" — the diversification layer fails precisely in 2002/2008/2011/2020/2022 when the eleven super-categories converge.
- **Frequency fragility (source-stated, §5):** monthly-or-slower rebalancing removes the advantage entirely — the reported edge requires reviewing the portfolio every 1–2 weeks.
- **Selection is in-sample:** C₂∩C₆ was picked ex post from 63 subsets and the dominant exits from 144 combinations **on the same 1,289-week sample**; JK–Memmel tests are computed on that same sample. No train/test split, no holdout, no Deflated Sharpe or multiple-testing correction is reported → `data gap` and the single biggest interpretive risk (`research interpretation`).
- **Internally unreconciled baseline level:** Table 2 prints C₂∩C₆ with no SL/TP at **Sharpe 0.8810**, while Table 3 Panel B's Δ implies a BASELINE near **1.04** (1.336 − 0.299) under what §3.2 describes as identical assumptions; the BASELINE level itself is never printed → `data gap` / apparent internal inconsistency, left unrepaired here.
- **Cost sensitivity:** 20 bp/side is an assumption, not a measurement; the source concedes that "under higher effective retail costs, the marginal rules would become unviable" (§5). Slippage, spread and impact are not separately observed.
- **Discarded higher-Sharpe rules:** 70 of 144 combinations show higher Sharpe (ATR2 1.42) but fail the ≤20 SlotChg/yr screen — the frontier is shaped by an operational constraint, so reported Sharpe is conditional on that screen (§4.2).
- **Prior-literature nulls (as cited by the source):** Tse (2015), Andreu et al. (2013), Zaremba–Andreu (2018), Vanstone et al. (2021), Wang–Wu (2024) find weak/insignificant ETF momentum; Kaminski–Lo (2014) shows stop-loss value is conditional on underlying momentum dynamics.
- **Universe/coverage:** U.S.-only ETF supply, Refinitiv classification dependency, unstated survivorship handling, preprint status, no code/data release, supplementary tables unavailable → all recorded above as `data gap`.

## Falsification plan

Every threshold below is `research-defined`; every procedure not present in the source is `research-proposed`. Data: the same Refinitiv-equivalently-sourced ETF daily panel plus FRED series; metrics net of 20 bp/side unless stated.

1. **Frozen forward test (research-proposed / research-defined):** freeze the exact published spec (C₂∩C₆ + score weights 0.35/0.35/0.20/0.10 + caps + TSL07 + SP/ST + biweekly entries/weekly exits) with no re-tuning and run it out-of-sample from 2026-05-16 for ≥ 12 months. **Fail if** forward Sharpe ≤ 0.459 (the SPY B&H reference, Table 3 Panel D) → the operational-layer thesis is falsified for the forward window; action: reject adoption candidacy and archive.
2. **Holdout re-selection audit (research-proposed / research-defined):** confine selection of the entry subset and exit rule to a training window ending 2013-12, evaluate 2014-01→2026-05 untouched. **Fail if** the holdout Sharpe of the selected rule falls below 1.0 **or** below the holdout Sharpe of a randomly drawn rule from the 144-grid → the headline is selection artifact; action: reclassify as unproven.
3. **Ranking-vs-risk-management ablation (research-proposed):** compare (a) full spec, (b) same cadence/caps/exits with **random slot selection** instead of the momentum score, (c) score ranking with **no caps**, (d) score ranking with **no SL/TP**, (e) passive 60/40. **Fail the "momentum alpha" reading if** (a) − (b) is insignificant (JK–Memmel p ≥ 0.05) while (a) beats (e) → value is pure risk management, not signal; action: relabel hypothesis accordingly.
4. **Cost stress (research-defined):** re-run at 10/20/40/60 bp per side. **Fail if** at 40 bp TSL07 Sharpe ≤ SPY's 0.459 → not robust to realistic higher-cost retail execution; action: reject.
5. **Frequency degradation (research-defined):** replicate the source's 6-frequency matrix. **Fail the source's claim if** monthly rebalancing still beats passive at p<0.05 (source claims it does not) — either outcome is diagnostic; action: record confirmation or contradiction against §5.
6. **VIX>25 hedge ablation (research-proposed / research-defined):** add a pre-declared tail overlay (e.g., static put/crash-spread or VIX-futures hedge funded at a fixed budget) and measure net Sharpe. **Fail if** no overlay at ≤ 1.5%/yr cost lifts the VIX>25 conditional Sharpe above −0.5 → the strategy remains uninvestable through stress; action: hold at research-only.
7. **Independent-vendor replication (research-proposed):** rebuild the panel from a non-Refinitiv source including **delisted ETFs** (survivorship audit). **Fail if** MaxDD improvement vs passive shrinks below 20pp (from the reported ~47pp) or Sharpe drops below 1.0 → vendor/survivorship artifact; action: reject.
8. **Placebo entry filter (research-proposed / research-defined):** replace C₂∩C₆ with a randomly phased trend filter matched on time-in-market. **Fail if** the real filter does not beat the placebo family's 95th percentile on MaxDD → the "entry timing" contribution is placebo; action: drop the filter layer from any future spec.
9. **Multiple-testing honesty (research-defined):** compute a Deflated Sharpe Ratio over the full 63+144 search. **Fail if** DSR < 95% for TSL07 → treat 1.336 as in-sample overfit; action: reject adoption candidacy.
10. **Cross-vehicle portability (research-defined):** re-run on a non-U.S. ETF universe (e.g., European/Asian listings). **Fail if** no subsample beats its local passive benchmark after costs → the effect is U.S.-specific; action: restrict scope or reject.

## Crypto portability

**unproven.**

The source contains **zero crypto evidence**: a single market type (U.S.-listed spot ETFs), a fixed Friday session, T-bill cash, Refinitiv super-category classification, and a long-only no-borrow design. Nothing about perpetual funding, liquidation cascades, 24/7 candle boundaries, venue fragmentation or index/mark-price mechanics is tested or even discussed.

- The *architecture* (trend entry filter + multi-horizon score + category/sleeve caps + trailing stop + asymmetric cadence) is mechanically portable in principle, but porting it requires rebuilding the "super-category" notion for crypto sectors, redefining Friday closes for 24/7 data, and re-deriving the trailing stop on per-venue candles — that is a **different signal construction**, not a parameter change.
- Crypto-specific unmodelled risks: perpetual funding payments (can dominate a 20 bp/side cost model), liquidation/leverage feedback, index-vs-last-price divergence, exchange delistings/survivorship worse than in ETFs, and venue-level spread/impact well above 20 bp on small caps.
- Cross-asset evidence is not transferable: the source itself shows the effect is regime-fragile in a VIX>25 world; crypto's equivalent stress episodes (funding squeezes, cascade liquidations) are untested.
- **This record must not be cited as crypto evidence.** Any crypto version is a ported hypothesis requiring its own primary source and validation (`research-proposed`).

## Limitations

- `not independently reproduced` — every performance number is `source-reported` from a single preprint backtest.
- `preprint, not peer-reviewed` (source-stated on every page).
- `data gap`: supplementary tables (full 144-rule frontier, frequency matrix, conditional-Sharpe table) not present in the delivered PDF; BASELINE level not printed (Table 2's 0.881 vs Δ-implied ≈1.04 unreconciled); no code/data release; survivorship/delist handling unstated; version/date-written unstated.
- `underspecified`: intraweek exit-monitoring frequency formalization, score-tie handling, capacity/impact.
- In-sample ex-post selection of both the entry filter (63 subsets) and the dominant exit (144 combinations) with no holdout or multiple-testing correction (`research interpretation` of the source's procedure).
- Sample/regime: 2001–2026 U.S. only; cost model is a flat assumed 20 bp/side; benchmarks costed at zero; rf fixed at 3%/yr.
- Publication-bias and single-author-team-research risk: a 25-year in-sample tactical backtest with an operational screen chosen by the authors.
- Incremental-write check: this is a new family (ETF-vehicle momentum with an explicit operational-management layer and regime-conditioned falsification) — no prior record shares its source identity or its composite construction.

## Implementation status

`implementation_status: not-implemented`. No implementation exists in our research stack: no prototype, no backtest, no Qlib run, no Paper/Testnet/Live connection. This document is a normalized research capture of an external preprint only. Nothing in this record should be read as having been executed, validated or even re-implemented by us.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. Adoption would require a separate, explicit review based on this record plus current sources.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — the authoritative strategy-research record specification this record was normalized against (read from Wiki Brain this run; sha256 `4561578a…fcaa7`; no v2 spec exists).

Repository neighbours (filenames only — no stable Wiki Brain pages are known for them, so no Wiki links are asserted): `simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11.md`, `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md`, `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md`, `functionally-generated-portfolio-diversity-entropy-smallcap-stochastic-cost-2026-09-22.md`. Each differs in source identity and mechanism.

## Sources

1. Nicolás Magner and Aliro Joel Sanhueza, "Momentum Strategies in ETFs under Simple Operational Rules: Economic Value and Conditional Predictability", SSRN preprint, `abstract_id=7379989`, DOI `10.2139/ssrn.7379989`, 28 pp, Posted 31 Aug 2026, Universidad Diego Portales; license "No reuse allowed without permission". Landing page and full PDF read 2026-09-23; local PDF SHA-256 `4a5d3cce67b2c64d4715c7e1cee218498b8c04a6b80bbce549ad15e50fb1e136`. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7379989
2. (Referenced *inside* source 1, not read independently this run — claims attributed to source 1's summary of them): Tse (2015), *North American Journal of Economics and Finance* 33:134–148; Andreu, Swinkels & Tjong-A-Tjoe (2013), *FMP* 27(2):127–148; Kaminski & Lo (2014), *Journal of Financial Markets* 18:234–254; Zaremba & Andreu (2018); Vanstone et al. (2021); Wang & Wu (2024); Jegadeesh & Titman (1993); Moskowitz, Ooi & Pedersen (2012); Asness, Moskowitz & Pedersen (2013); Lo (2004, 2017); Faber (2007); Antonacci (2014).
