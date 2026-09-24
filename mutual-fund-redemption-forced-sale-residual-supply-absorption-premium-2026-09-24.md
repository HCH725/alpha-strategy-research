---
schema: strategy-research-record-v1
title: "Mutual-Fund Redemption Forced-Sale Residual-Supply Absorption Premium: Shift-Share Flow×Holdings Pressure (ForcedSale / AbsInv) Cross-Sectional Long–Short in US Equities, 2003–2024"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-equity
  - mutual-fund-flows
  - residual-supply
  - liquidity-absorption
  - shift-share
  - fama-macbeth
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-05-29
sources:
  - "Ziyao Wang, 'Residual Supply and the Price of Risk Absorption', arXiv:2605.30672v1 [q-fin.GN; also econ.GN], submitted Fri, 29 May 2026 00:05:09 UTC (74 KB source). https://arxiv.org/abs/2605.30672"
  - "https://doi.org/10.48550/arXiv.2605.30672 (arXiv-issued DataCite DOI, resolves HTTP 200 on 2026-09-24; no publisher DOI)"
  - "https://arxiv.org/html/2605.30672v1 (full text, HTTP 200, 873,386 bytes on 2026-09-24; read directly for this record: §1–§7, Appendices A/B/C, Tables 1–29, Figures 1–4 captions; https://arxiv.org/html/2605.30672v2 -> HTTP 404 confirms v1 is the only version)"
  - "https://arxiv.org/pdf/2605.30672v1 (HTTP 200; 662,641 bytes; last-modified Mon, 01 Jun 2026 00:22:28 GMT; etag \"CM/DloTj5JQDEAI=\")"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Table 9 (no-microcap equal-weighted H–L AbsInv, 1m = 44.09 bp, t=2.85) versus §4.5 text and Appendix Table 26 (same-named no-microcap monthly equal-weighted H–L gross = 47.88 bp, t=3.11): two different values for the same-named monthly spread; the construction difference is not explained anywhere in v1."
  - "Appendix Table 16 permutation-placebo 'true coefficient' for the no-microcap 1m cell (77.26 bp) matches no printed baseline coefficient (Table 5: ForcedSale 65.43, AbsInv 45.81; Table 12: ForcedSale 57.49, AbsInv 38.04); the specification behind the placebo statistic is not stated in v1."
---

# Mutual-Fund Redemption Forced-Sale Residual-Supply Absorption Premium: Shift-Share Flow×Holdings Pressure (ForcedSale / AbsInv) Cross-Sectional Long–Short in US Equities, 2003–2024

## Provenance

- **Primary-source author(s), exactly as source:** **Ziyao Wang (sole author)**. arXiv submission history: `From: Ziyao Wang [view email]`. The v1 HTML title block prints affiliation `Department of Mathematics and Statistics, Texas Tech University`, email `ziywang@ttu.edu`, and an acknowledgement of "Professor Svetlozar T. Rachev and Professor Hongwei Mei of the Department of Mathematics and Statistics at Texas Tech University". No co-authors anywhere in v1.
- **Paper title:** *Residual Supply and the Price of Risk Absorption*.
- **Version / date:** `arXiv:2605.30672v1 [q-fin.GN; also econ.GN]`; landing submission history shows a **single version** `[v1] Fri, 29 May 2026 00:05:09 UTC (74 KB)`; `https://arxiv.org/html/2605.30672v2` → HTTP **404** (tested 2026-09-24). The **rendered date line inside the v1 HTML reads "August 24, 2026"**, which postdates the v1 submission timestamp — recorded here as a **rendering artifact / data gap** (most consistent with a conversion-time `\today` in the LaTeXML render), **not** as evidence of a second version.
- **Publication status:** **preprint only.** Landing `Comments:` empty; `Journal-ref:` empty; no publisher DOI (only the arXiv-issued DataCite DOI `10.48550/arXiv.2605.30672`, HTTP 200). License: **"arXiv.org perpetual non-exclusive license"** (HTML license line; abs-page link `licenses/nonexclusive-distrib/1.0/`). JEL G11, G12, G14, G23; keywords include asset pricing, risk absorption, demand imbalances, mutual fund flows, institutional ownership, slow-moving capital, market clearing.
- **Primary-source inspection for this record:** the arXiv **v1 HTML full text was fetched and read directly** (not a secondary summary). Verified against the primary source: author list, version/date, sample window and universe (§3.1), the full signal construction (§3.2–§3.3, Eqs. 34–37, Fig. 1), data timing and reporting lags (§3.3), regression and portfolio design (§3.5, §4.5), the transaction-cost treatment (§4.5 + Appendix Table 26), every performance number below with its Table/§ anchor, and the scope caveats (§1, §6).
- **Repository deduplication audit (2026-09-24):** ripgrep across the **entire repository** — **2,501 `*.md` files** repo-wide excluding `.git` (936 of them `git`-tracked; includes `.mimo-worktrees/`, `.agents/`, `.hermes/`, and the two untracked `adaptive-perpetual-factor-factory-cross-sectional-fmz-2026-09-15.md` / `option-funding-basis-year-end-boundary-wedge-spx-rut-box-implied-2026-09-22.md`), plus `coverage_manifest.csv` (5,808 lines), plus a repo-wide extraction of **634 unique arXiv IDs already referenced in any `*.md`** — for `2605.30672`, `10.48550/arXiv.2605.30672`, the exact title `Residual Supply and the Price of Risk Absorption`, `Price of Risk Absorption`, `Ziyao Wang`, `ziywang`, `ForcedSale`, `AbsInv`, `ThinBase`, `risk absorber`, `absorption premium`, `absorption pressure`, `market-clearing residual`, `thin investor base`, `predetermined holdings`, `residual supply`, `risk absorption`, `forced sale`, `forced-sale` → **0 hits for every source-identity token of this paper**, and `2605.30672` is not among the 634 already-referenced arXiv IDs (a non-`.md` repo-wide grep for `2605.30672` also returned no files). Generic-word neighbours that DO hit, all different sources: `mutual fund flow`/`flow-induced trading` → 1 file (`beta-times-quantity-noise-trader-flow-factor-pricing-2026-09-07.md`, arXiv `2609.05162` *Quantity, Risk, and Return*); `absorption capacity` → 1 file (`crypto-token-unlock-72h-supply-shock-event-short-2026-09-12.md`); `redemption stress` → 1 file (`usdt-exchange-net-inflow-buy-side-liquidity-drift-1h-2h-2026-09-03.md`); `Texas Tech` → 2 unrelated records; `mutual fund` → 13 files (index-reconstitution drift, short-selling-ban DID, reviving-anomalies, order-flow investor segmentation, etc.).
- **Material-distinctness statement (independent record):** closest existing records differ in **source identity and** in at least one material axis: `beta-times-quantity-noise-trader-flow-factor-pricing-2026-09-07.md` (source arXiv `2609.05162`; mechanism = beta×quantity noise-trader flow *pricing factor*, not a shift-share redemption-pressure signal), `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` (event type = index rebalancing forced flow, scheduled and announced, versus unscheduled open-end redemptions), `order-flow-matched-filter-normalization-investor-segmentation-2026-09-02.md` (signal construction = order-flow matched filter / investor segmentation, not flow×lagged-holdings), `bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01.md` (market and horizon = crypto ETF 1-day drift), `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (anomaly net-return audit, no flow signal), `illiquidity-at-risk-realized-amihud-mem-jump-tail-contagion-2026-09-02.md` (Amihud tail-risk forecasting, not flow-induced residual supply). Axes of material distinction for this record: **mechanism** (costly market-clearing / absorption of redemption-forced residual supply priced by inventory + capital + adjustment wedges), **signal construction** (shift-share `FIT` → `ForcedSale` → decaying `AbsInv`, ρ=0.85, monthly cross-sectional ranks), **universe/market type** (US CRSP common stocks), **horizon/regime** (1–12 months, market-level scarcity states), **material data dependency** (open-end mutual-fund TNA + portfolio holdings + Form 13F).
- **Reproducibility assets:** **no code, data-availability, or replication-package statement appears anywhere in v1** (full-text search for `data availability`, `code availability`, `replication package` → 0 hits; the only GitHub strings are arXiv UI boilerplate "Report GitHub Issue" / "Submit without GitHub"). The mutual-fund holdings/TNA **data vendor is never named** (no WRDS, Morningstar, or similar mention) → both are **data gap**, not inferred to be available.

## Economic mechanism

### Source-reported

The paper asks a market-clearing question rather than a covariance question: when open-end funds redeem and long-horizon natural buyers do not step in at once, some limited-capital "risk absorber" must carry the residual inventory, and it must be compensated. The continuous-time model (§2) fixes the required normalized residual exposure `θ_req = (1/K^A)·diag(P)·[S̄ − D̄(P,X,Z)]` (Eq. 9), imposes absorber equilibrium `θ^A = θ_req` (Eq. 10), and derives the Euler/HJB pricing equation `π_t = ∇_θ c_t − A^{u_t}p_t + ρ p_t + h_t` (Eqs. 26–27) in which expected return = inventory-risk compensation + capital/adjustment wedges. The paper's own summary (§1): "expected return = inventory risk compensation + capital and adjustment wedges". Empirically the chain is: fund flows mapped through **predetermined (lagged) holdings** predict **actual mutual fund selling** → that selling produces **contemporaneous price declines** → **subsequent returns are positive** over one to six months, with the slope **larger when market-wide absorption capacity is tight, investor bases are thin, and trading capacity is low** (Abstract, §1, §4.3–§4.4). The paper positions itself against a pure liquidity story: the pricing object is *the product of residual supply and the marginal cost of absorbing it* (§2.1), and it explicitly distinguishes its contribution from Coval–Stafford (2007), Frazzini–Lamont (2008) and Lou (2012) as showing the reversal is **not uniform** — it is largest exactly where balance sheet, natural demand and trading capacity are scarce (§1).

### Research interpretation

Falsifiable hypothesis H: *US common stocks mechanically exposed to open-end-fund redemptions — negative part of a shift-share of fund flows through lagged portfolio weights, accumulated with decay — earn positive risk-adjusted returns over the following 1–6 months, and the cross-sectional slope increases in a pre-specified market-level absorption-scarcity state.* Component roles:

```text
Regime:     market-level Scarcity composite = aggregate Amihud illiquidity + market
            volatility + mutual-fund redemption stress; low/high month split
            (source-reported; component weights, standardisation and the split
            threshold are NOT stated -> underspecified)
Primary signal: ForcedSale_it = −min(FIT_it / ME_{i,t−1}, 0), with
            FIT_it = Σ_f w_{f,i,t−1}·Flow_{f,t}·TNA_{f,t−1}  (shift-share, lagged weights)
            AbsInv_it = ρ·AbsInv_{i,t−1} + ForcedSale_it, ρ = 0.85 baseline
            entered as within-month cross-sectional ranks (source-reported, Eqs. 34–37)
Confirmation: none as an executable gate — ThinBase / low dollar-volume / scarcity are
            used as sorts and interactions to locate the premium, not as filters
            (source-reported)
Risk / exit: horizon exit only (1/3/6/12-month cumulative returns); no stop, no sizing
            rule, no tie rule, no index-membership rule -> underspecified
```

Research interpretation of what would make H *tradeable* rather than merely *priced*: the effect must survive (i) genuinely point-in-time inputs (the baseline mapping is ex post — §3.3), (ii) a net-of-cost ladder that includes **short-side borrow**, (iii) value-weighted construction, and (iv) an orthogonalisation against ordinary loser reversal (the paper's own main alternative). As recorded below, the source's own evidence is strong on (iv)-as-diagnosed, partial on (i), weak on (iii), and silent on (ii).

## Signal

All items below are **source-reported** unless marked `research-proposed`, `research-defined`, or `underspecified`.

- **Fund flow (Eq. 34, §3.2):** `Flow_{f,t} = [TNA_{f,t} − TNA_{f,t−1}(1+R_{f,t})] / TNA_{f,t−1}` — TNA-based flow with the mechanical return component removed.
- **Flow-induced trading, shift-share (Eq. 35, §3.2):** `FIT_{i,t} = Σ_f w_{f,i,t−1}·Flow_{f,t}·TNA_{f,t−1}` — **predetermined (lagged) portfolio weights** × dollar flow; the paper stresses that lagged rather than contemporaneous weights are "essential" to limit manager information/selection content. Normalised by lagged market equity for ranking.
- **Forced-sale pressure (Eq. 36):** `ForcedSale_{i,t} = −min(FIT_{i,t}/ME_{i,t−1}, 0)` — only the **negative part**, i.e. redemption-induced selling, expressed as a rate of lagged market equity.
- **Inventory proxy (Eq. 37):** `AbsInv_{i,t} = ρ·AbsInv_{i,t−1} + ForcedSale_{i,t}` with **ρ = 0.85 baseline**; robustness grid ρ ∈ {0.50, 0.75, 0.85, 0.90} (Appendix Table 19).
- **Raw scale (§3.2):** 90th/95th percentile of forced selling ≈ **24 / 34 bp of market equity** (full sample) and **29 / 39 bp** (no-microcap), monthly averages.
- **Expected future pressure (§3.2):** fund flows forecast from lagged flows, lagged fund returns, fund size and calendar-month effects with an **expanding window estimated only on prior months**, then mapped through current holdings (`ExpectedSaleNext`). Functional form of the flow model → `underspecified`.
- **Alternative pressure measures (§5.4, Table 15):** `DistressSale` (funds in the bottom tail of the flow distribution — tail definition `underspecified`), residual-redemption sale (flows residualised each month on lagged flows, lagged fund returns, lagged fund size), extreme residual redemption, and `ExpectedSaleNext × ThinBase`.
- **Tradability / formation timestamp (§3.3):** the baseline flow-holdings mapping is explicitly **ex post** and "not automatically a real-time trading signal" (source-reported). The **reported-holdings variant** uses only portfolio reports whose report date is **≥45 days before the flow month and ≤276 days old**; this is the closest thing in the paper to a real-time implementable input. Exact signal-formation calendar date, timezone and publication convention for fund reports → `data gap`.
- **Controls (§3.1):** log market equity, book-to-market, 12-month momentum excluding the most recent month, short-term reversal, market beta, idiosyncratic volatility, turnover, Amihud illiquidity, institutional ownership, ownership breadth, ownership concentration — all **lagged** relative to future returns; continuous variables entered as **within-month ranks**.
- **Cross-sectional test (Eq. 38, §3.5):** `R_{i,t+1:t+h} − R_{f,t+1:t+h} = a_t + b_t·AbsInv_{i,t} + Γ_t′·Controls_{i,t} + ε` for h ∈ {1,3,6,12} months, Newey–West standard errors on the time series of monthly slopes; parallel specs use `ForcedSale` and expected-sale pressure; state dependence via high/low-`Scarcity` slope splits and interactions with `Scarcity`, `ThinBase`, and stock-level illiquidity.
- **Portfolio rule (§3.5, §4.5):** each month stocks are sorted into absorption portfolios on `AbsInv`; **high-minus-low** spreads reported **equal-weighted and value-weighted**, plus CAPM / FF3 / Carhart / FF5+UMD alphas. **The number of sort buckets (deciles? terciles? top/bottom X%), the holding/overlap convention for the 3/6/12-month horizons, tie handling, index-membership changes during the sample, and any position cap are NOT stated anywhere in v1 → `underspecified`** (no `decile`/`quintile` token appears for this sort; only state and size *terciles* are defined).
- **State variables (§3.4, Table 17):** `ThinBase` = "standardized composite" of low institutional ownership, low breadth, high concentration; `Scarcity` = composite of aggregate Amihud illiquidity, market volatility, and mutual-fund redemption stress. **Component weights, standardisation method, and the low/high threshold are not stated → `underspecified`.**
- **Universe / sample (§3.1, Table 3):** CRSP share codes **10 and 11**, **January 2003 – November 2024**; **1,022,728 stock-months / 10,338 PERMNOs** (full); **no-microcap = market equity above the 20th percentile of same-month NYSE ME**, **490,162 stock-months / 5,559 PERMNOs**. Returns **include delisting returns when available**. Descriptives (Table 3): monthly return 96.3 bp (sd 1,795.4) full, 91.8 bp (sd 1,397.2) no-microcap; institutional ownership 0.61 (0.31); forced-sale rank 0.50 (0.29).
- **Reproducibility status:** the *signal arithmetic* is reconstructable from Eqs. 34–37 once fund TNA/returns/holdings are in hand; the *state gates, sort construction and flow-forecast model* are not → the strategy as a whole is **partially reconstructable, materially `underspecified`**.

## Required data

- **Universe:** US common stocks (CRSP share codes 10/11), point-in-time by month, Jan 2003 – Nov 2024; no-microcap screen = ME > 20th pct of same-month NYSE ME (§3.1). Delisting returns used "when available"; handling of stocks entering/leaving the sort universe within a month beyond that → `data gap`.
- **Fund data:** open-end mutual fund **monthly total net assets and net returns** (to build `Flow`) and **portfolio holdings with report dates** (to build `FIT`), at fund×stock×month granularity; first stage uses **168 report months / ~20.5 million manager-stock observations** (Table 4 Panel A). **Vendor is never named** → `data gap`. Fund-level **survivorship, mergers, share-class aggregation and missing-report treatment are never discussed** (0 hits for `survivorship`) → `data gap`.
- **Institutional ownership:** SEC **Form 13F** quarterly — IO = 13F shares/shares outstanding, breadth = log number of owners, HHI, top-holder share (§3.4, Table 17).
- **Characteristics:** Compustat (book-to-market, ROA/profitability/sales-growth look-ahead controls in Appendix Table 24) matched to CRSP; CRSP prices/volumes for Amihud, turnover, beta, idiosyncratic volatility, momentum, reversal; market equity for scaling; risk-free rate subtracted asset-by-asset in the FM spec (Table 18 Panel A note).
- **State data:** aggregate Amihud illiquidity, market volatility (VIX used in the decomposition, Table 20), **NFCI** (Table 20/21), and a mutual-fund redemption-stress series — the construction of the redemption-stress series itself → `data gap`.
- **Point-in-time:** weights are lagged by construction; the reported-holdings variant enforces ≥45-day-old reports and ≤276-day staleness (§3.3); flow forecasts use expanding windows with only prior months (§3.2). Reporting-lag treatment of 13F for `ThinBase` → `data gap`.
- **Missing data:** no imputation is described; no treatment of fund report gaps, suspended stocks, or stale prices is stated → `data gap`.
- **Not required by the source:** order book, trade/ aggressor data, funding, borrow, options, on-chain fields. Short-leg borrow availability/cost is assumed away (see Execution assumptions).

## Execution assumptions

Source-reported:

- **Signal-to-order timing:** the baseline signal is explicitly **ex post** (§3.3) — the paper states the mapping "is not automatically a real-time trading signal". The reported-holdings variant (≥45-day-old reports, ≤276 days) is the only near-real-time construction, so a tradable reading of this signal is structurally **stale by 1.5–9 months of holdings information** (our characterisation of the stated 45/276-day window).
- **Order type / fill model / latency / partial fills / participation cap:** **not stated anywhere in v1** → `data gap` (no market-vs-limit assumption, no fill model, no latency or participation discussion in §3–§5).
- **Costs:** the only explicit cost treatment is Appendix **Table 26** ("Turnover and Transaction-Cost Diagnostics", caption: *"Cost adjustments are illustrative"*) — a **flat one-way cost ladder** on the no-microcap equal-weighted H–L portfolio: gross **47.88 bp/month (t=3.11)**; net **46.54 (3.00) / 43.96 (2.84) / 39.67 (2.56) / 31.08 (2.01)** at **10 / 25 / 50 / 100 bp one-way**; value-weighted net at 25 bp **19.71 (1.23)**; **break-even one-way cost 278.75 bp**; **H–L one-way turnover 17.18%/month (t=24.43)**; value-weighted gross **24.03 (1.50)**. §4.5 restates these as "47.9 gross … 44.0, 39.7, and 31.1 after assumed one-way costs of 25, 50, and 100 basis points".
- **What the cost model does NOT contain (full-text term counts in v1):** `borrow` **0**, `short sell` **0**, `shorting` **0**, `slippage` **0**, `latency` **0**; `bid-ask` **1** occurrence and it is a theory sentence (§2.1), `financing cost` **2** occurrences and both are model notation (Appendix A/B); no spread model, no market-impact model, no locate/availability constraint, no short-side rebate or rebate-of-vote. **Therefore the long–short spreads are gross of short-side financing and borrow, and no cost is inferred to be zero — the source simply does not model those frictions.**
- **Risk metrics:** **no Sharpe, Sortino, or drawdown figure appears anywhere in v1** (`Sharpe` 0 real hits — only the substring in "sharpest"; `drawdown` 0; `Sortino` 0) → `data gap`. Inference is Newey–West t-statistics only.
- **Rebalancing / holding:** portfolios are formed **each month** (§4.5); how 3/6/12-month H–L returns overlap or are re-formed → `underspecified`.
- **Leverage / margin:** not stated; long–short is implicitly dollar-neutral by construction of H–L, gross exposure unstated → `data gap`.
- **Capacity:** the source explicitly limits the claim — §1: the portfolio evidence "serves to locate the premium rather than to propose a large-capacity arbitrage strategy"; §6: the alphas are "diagnostics of a costly market-clearing service rather than evidence of a broad scalable arbitrage factor". No ADV/participation/capacity model is given → `data gap`.

Research assumptions adopted for this record: **none.** No cost, fill, sizing, or entry-timing assumption has been invented here; any reproduction must add them and label them `research-proposed`.

## Evidence

### Source-reported

All figures below are third-party claims from `arXiv:2605.30672v1`, read from the primary source, in **US common-stock equity** (not crypto). Coefficients are **basis points** of future cumulative return per unit of within-month rank (Fama–MacBeth) or portfolio spread; `t` = Newey–West. Table/§ anchors are given for every number.

- **Sample (Table 3, §3.1):** 1,022,728 stock-months / 10,338 PERMNOs full; 490,162 / 5,559 no-microcap; window **Jan 2003 – Nov 2024**.
- **First stage — flows predict actual selling (Table 4 Panel A):** manager–stock two-way (fund × stock, within report month) slope **1.07 (t=30.24)** over 168 report months and 20.5 M manager-stock obs; net FIT rank → ΔMF ownership **52.62 (2.40)**; sale-pressure rank → ΔMF ownership **−114.24 (−4.48)**; buy-pressure rank **−27.23 (−1.39) n.s.**
- **Real-time-ish variant (Table 4 Panel B, no-microcap, 45-day reported-holdings):** ForcedSale rank **50.36 (2.83) / 132.97 (3.44) / 195.29 (3.14) / 321.06 (2.86)** at 1/3/6/12 m.
- **Headline cross-section (Table 5):** ForcedSale rank, **All** = **73.21 (3.33) / 162.52 (3.33) / 225.50 (2.93) / 344.93 (2.35)**; **No microcap** = **65.43 (3.32) / 160.11 (3.97) / 216.50 (3.54) / 342.33 (3.07)**. AbsInv rank, **All** = **68.37 (3.05) / 174.66 (3.09) / 273.82 (2.79) / 337.34 (1.56)**; **No microcap** = **45.81 (2.52) / 135.39 (2.65) / 237.07 (2.63) / 308.55 (1.60)**. (§1 states the headline as "about 65 basis points over the next month and 217 basis points over six months" — matches Table 5 no-microcap ✓.)
- **Industry fixed effects (Table 6, AbsInv):** No microcap **34.50 (2.03) / 97.19 (1.96) / 158.48 (1.83) / 141.48 (0.75)**; All **47.31 (2.31) / 107.39 (2.04) / 143.80 (1.56) / 103.09 (0.52)**.
- **State dependence (Table 7, AbsInv, composite scarcity split):** All — low **43.31 (2.34) / 117.89 (2.60) / 223.40 (3.23) / 290.43 (3.76)** vs high **93.44 (2.28) / 231.43 (2.33) / 323.85 (1.81) / 383.88 (0.95)**; No-microcap — low **29.79 (1.98) / 105.42 (2.45) / 242.63 (3.27) / 340.05 (3.14)** vs high **61.83 (1.91) / 165.37 (1.93) / 231.56 (1.49) / 277.29 (0.79)**.
- **Trading-capacity split conditional on fund ownership (Table 8, no-microcap, above-median lagged MF exposure, top/bottom terciles of 12-month dollar volume):** AbsInv **low volume 96.60 (2.06) / 375.46 (3.79) / 729.63 (5.14)** vs **high volume 4.54 (0.22) / 39.03 (0.74) / 91.77 (0.93)**; ForcedSale low volume **50.95 (1.30) / 268.33 (3.18) / 507.57 (3.86)** vs high volume **24.11 (0.85) / 73.79 (1.06) / 81.14 (0.79)**.
- **Portfolio sorts (Table 9, no-microcap, monthly AbsInv sorts):** EW H–L **44.09 (2.85) / 120.20 (2.75) / 218.41 (2.57) / 333.79 (1.99)**; VW H–L **20.92 (1.29) / 46.17 (1.06) / 74.92 (0.96) / 121.80 (0.96)**; EW high-scarcity **76.21 (2.64) / 195.41 (2.89) / 326.79 (2.46) / 524.75 (1.89)**; VW high-scarcity **28.15 (1.10) / 68.35 (1.03) / 84.53 (0.77) / 112.51 (0.75)**.
- **Factor alphas (Table 10, bp/month, no-microcap):** EW **CAPM 31.28 (1.79), FF3 34.72 (2.19), Carhart 40.21 (2.51), FF5+UMD 24.46 (1.83)**; VW **−8.18 (−0.51), 1.78 (0.14), 5.45 (0.43), 9.81 (0.83)**.
- **Cost / turnover diagnostics (Table 26):** EW gross **47.88 (3.11)**; VW gross **24.03 (1.50)**; one-way turnover **17.18% (24.43)**; EW net **46.54 (3.00) / 43.96 (2.84) / 39.67 (2.56) / 31.08 (2.01)** at 10/25/50/100 bp one-way; VW net at 25 bp **19.71 (1.23)**; **break-even one-way cost 278.75 bp**. Caption: cost adjustments are **illustrative**.
- **Contemporaneous price pressure (Table 11):** no-microcap full period Net FIT **29.76 (3.74)**, ForcedSale **−61.64 (−6.20)**; All full period **42.28 (4.16) / −79.25 (−7.51)**; All low scarcity **26.19 (2.43) / −58.34 (−6.67)**, high scarcity **58.49 (3.52) / −100.32 (−5.07)**; no-microcap low scarcity **23.69 (2.99) / −45.99 (−6.68)**, high scarcity **35.88 (2.56) / −77.41 (−4.05)**.
- **Matched event time (§5.1, Fig. 4):** matched abnormal return **−127 bp at month 0 (t=−12.12)**, **+44 bp at month +1 (t=2.00)**, later months positive but uneven; matching within month, industry group, size, book-to-market, illiquidity, momentum and short-term-reversal bins.
- **After pretrend controls (Table 12):** ForcedSale no-microcap **57.49 (3.12) / 138.62 (3.72) / 169.11 (2.80) / 272.26 (2.35)**; All **63.51 (2.95) / 131.97 (2.73) / 168.23 (2.18) / 242.64 (1.57)**; AbsInv no-microcap **38.04 (2.47) / 104.43 (2.55) / 157.93 (2.06) / 205.07 (1.23)**. Additionally (§5.2 text) after **residualising ForcedSale within month on past returns and the full control set**, the no-microcap 1-month slope is **34 bp (t=2.05)**.
- **Reverse causality (Table 13, forced-sale pressure on past returns):** All **−171.01 (−3.41) / −210.10 (−5.55) / −51.05 (−2.21)**; no-microcap **−65.46 (−1.17) / −324.08 (−6.48) / −162.89 (−5.73)** for past 1/3/12-month returns.
- **13F ownership migration (Table 14, no-microcap):** institutional ownership **−152.54 (−6.91)** at 1 quarter, **−454.95 (−10.18)** at 4 quarters; breadth **−134.23 (−2.75) / −290.97 (−2.76)**; HHI **27.15 (1.96) / 87.09 (2.54)**; top-holder share **30.42 (2.02) / 107.34 (2.69)**; ThinBase **1062.36 (4.61) / 3092.16 (6.04)**.
- **Alternative measures (Table 15, no-microcap):** DistressSale **51.33 (3.00) / 128.33 (3.58) / 180.79 (3.13) / 295.80 (2.76)**; residual-redemption sale **74.08 (3.97) / 180.08 (4.38) / 250.23 (3.91) / 361.80 (3.22)**; extreme residual redemption **55.20 (3.16) / 151.10 (3.92) / 220.41 (3.52) / 333.59 (3.09)**; `ExpectedSaleNext` (out-of-sample expanding window) **106.86 (2.54) / 244.10 (3.07) / 326.65 (3.16) / 408.18 (2.49)**; `ExpectedSaleNext × ThinBase` **137.89 (2.34) / 413.59 (2.54) / 629.51 (2.21) / 829.23 (1.69)**.
- **Permutation placebo (Table 16, 1,000 flow↔holdings remappings):** All — true **87.92 / 155.70 / 180.96 / 208.00** vs 99th-percentile placebo **15.98 / 27.40 / 45.11 / 69.91**, empirical p = 0.001 at all four horizons; No-microcap — true **77.26 / 155.42 / 183.07 / 249.94** vs **18.83 / 27.89 / 44.53 / 69.01**, p = 0.001.
- **Decay robustness (Table 19, no-microcap AbsInv):** ρ=0.50 **46.88 (2.24) / 112.15 (2.29) / 171.18 (2.00) / 227.02 (1.31)**; ρ=0.75 **44.77 (2.39) / 126.47 (2.52) / 210.93 (2.35) / 281.15 (1.50)**; ρ=0.85 **45.81 (2.52) / 135.39 (2.65) / 237.07 (2.63) / 308.55 (1.60)** (equals Table 5 ✓); ρ=0.90 **48.21 (2.65) / 143.59 (2.81) / 261.45 (2.88) / 338.97 (1.76)**.
- **Mechanism double sorts (Table 27, EW no-microcap H–L within high states):** High ThinBase **70.49 (2.61) / 205.31 (2.82) / 350.88 (2.53) / 530.44 (1.89)**; High illiquidity **63.88 (2.44) / 175.42 (2.51) / 296.37 (2.17) / 474.10 (1.72)**; High scarcity **76.21 (2.64) / 195.41 (2.89) / 326.79 (2.46) / 524.75 (1.89)**.
- **Strict panel FE (Table 28, no-microcap, 1-month):** stock + month FE **64.81 (1.79)**; stock + industry-month FE **62.28 (2.21)**.
- **Paper's own bottom line (§6, Abstract):** "a measurable component of residual supply is priced in exactly the states where the theory predicts absorption to be expensive, even as it stops short of tracing the entire market-wide inventory or naming every marginal buyer"; forced-sale pressure "predicts actual fund selling, contemporaneous price declines, and positive returns over the following one to six months."

### Independently reproduced

`not independently reproduced.` This run consisted of: landing-page metadata read; v1 HTML full text fetched and read directly; every quoted number located in its printed table; full-text term counts for cost/risk metrics; and a repository-wide source-identity dedup. **No backtest was re-run, no CRSP / Compustat / mutual-fund / 13F data was obtained, and no formula from the paper was implemented.**

### Negative evidence

Recorded from the primary source plus our own cell counts (marked *our count*); none of this is our reproduction.

1. **Source's own capacity caveat (§1, §6):** the portfolio evidence "serves to locate the premium rather than to propose a large-capacity arbitrage strategy"; the alphas are "diagnostics of a costly market-clearing service rather than evidence of a broad scalable arbitrage factor."
2. **Value-weighted results are weak or null (our count from Tables 9/10/26):** VW H–L 1m **20.92 (t=1.29)**; all four VW factor alphas statistically indistinguishable from zero (CAPM **−8.18, t=−0.51**); VW net at 25 bp **19.71 (t=1.23)**. The premium as printed does not survive value weighting in large/liquid names.
3. **Large-cap sign reversal (our count from Table 25):** within no-microcap NYSE-size terciles, AbsInv slopes for the **Large** tercile are **negative at every horizon** — **−206.05 / −200.16 / −333.17 / −625.18 bp** (t = −1.10 / −1.06 / −0.98 / −1.04) — while **Medium** carries the effect (**−23.16 / 129.02 / 364.22 / 611.96**, t = −0.41 / 1.29 / **2.70 / 2.54**) and **Small** is insignificant (−12.16 / 101.20 / 302.11 / 364.64). §4.5 describes the large tercile as "weak"; the point estimates are in fact the opposite sign (none significant).
4. **Cost model is flat, illustrative, and omits the short side (our term counts):** only a single flat one-way ladder in Appendix Table 26; **0** occurrences of `borrow`, `short sell`, `shorting`, `slippage`, `latency`; **1** `bid-ask` (theory sentence); no spread/impact/locate/financing model for the H–L book; turnover **17.18%/month one-way** with no turnover-aware execution. **No cost is inferred to be zero — the frictions are simply unmodelled.**
5. **Strong pretrend / reversal confound, partially but not fully absorbed (Tables 12/13, §5.2):** forced-sale pressure loads heavily on past returns (no-microcap past-3m **−324.08, t=−6.48**); after residualising the signal itself on past returns and the full control set the 1-month slope falls from **65.43** to **34 bp (t=2.05)** — i.e. roughly half the headline premium is shared with the cross-section of recent losers. The source concedes the design "is not a randomized experiment" and leans on a battery of complementary tests (§6).
6. **The state-dependence story does not decompose (Table 20, source-reported):** continuous interactions of AbsInv with **market illiquidity are negative and significant** (**−12.40, t=−2.43** at 1m; **−49.28, t=−2.31** at 6m), with **VIX ≈ 0** (4.40, t=0.90) and **MF redemption stress ≈ 0/negative** (−1.72, t=−0.50 at 1m); only the *composite* high/low split delivers the headline doubling. The table caption itself says "the mixed signs are why the main text uses the composite scarcity split". A composite whose individual components carry opposite-signed interactions is a fragile gate.
7. **State ordering is split-method-dependent (our count, Table 7 vs Table 21):** with the Table 7 split, high-scarcity > low-scarcity at all four horizons; with the Table 21 **bottom/top-tercile** split (no-microcap, composite scarcity), high > low at 1m (**83.37 vs 39.24**) and 3m (**143.42 vs 120.07**) but **high < low at 6m (169.82 vs 210.90)**. The "premium roughly doubles when capacity is tight" claim is horizon- and split-dependent.
8. **Long-horizon and FE precision decay:** high-scarcity 12m t = **0.95** (All) / **0.79** (no-microcap) (Table 7); industry-FE 6m/12m t = **1.83 / 0.75** (Table 6); AbsInv 12m t = **1.60 / 1.56** (Table 5); matched post-event months after +1 are "positive but uneven" (§5.1).
9. **Buy side is not validated (Table 4, §5.4, Appendix Table 24):** buy-pressure rank → ΔMF ownership **−27.23 (t=−1.39) n.s.**; and when gross buy and sell pressures enter separately "both are associated with weak event-month returns and both predict positive subsequent returns", so the interpretation "rests on the selling side".
10. **Marginal absorber unidentified (§5.3, §6):** quarterly 13F shows forced-sale stocks become harder to place (Table 14) but "do not isolate a single class of marginal buyers"; absorption may run outside 13F.
11. **Real-time tradability gap (§3.3):** baseline mapping is ex post; the reported-holdings variant uses reports 45–276 days old, so the implementable signal is structurally stale; fund-holdings coverage is only "cleanest from" 2003.
12. **Interaction/horse-race fragility (source-reported, Appendix Tables 20, 23):** individual scarcity interactions are "mixed"; saturated specifications combining forced, distress, expected and cumulative pressure deliver "unstable individual coefficients, as one would expect when the pressure variables are highly correlated."
13. **Two unreconciled internal numerics (our count):** (a) Table 9 EW H–L 1m **44.09** vs Table 26 / §4.5 same-named gross **47.88**; (b) Appendix Table 16's placebo "true coefficient" (no-microcap 1m **77.26**) matches no printed baseline (Table 5: 65.43 / 45.81; Table 12: 57.49 / 38.04) and the measured specification is unstated.
14. **No multiplicity or selection adjustment (our count):** the printed grid spans ≥7 pressure measures × 4 horizons × 2 samples × multiple state splits/sizes/FEs plus Appendix Tables 19–29, with **zero** family-wise, FDR, or deflated-Sharpe correction anywhere in v1.
15. **No risk metrics, no peer review, sample ends Nov 2024:** no Sharpe/drawdown/Sortino anywhere; single-author preprint with empty Comments/Journal-ref; no code or data-availability statement; mutual-fund data vendor unstated; fund-level survivorship treatment unstated (0 hits for `survivorship`).

## Falsification plan

Every threshold below is a **`research-defined falsification threshold`** chosen by this Scout; every procedure is **`research-proposed`** unless the source already ran it (noted).

- **F1 — Point-in-time replication (research-proposed):** rebuild `ForcedSale` from **only** holdings reports available at signal time (≥45-day rule) on an independent CRSP + fund-holdings build; **fail if** the no-microcap 1-month slope has **NW t < 2.0** (`research-defined`).
- **F2 — Cost ladder including the short side (research-proposed):** apply 0/10/25/50/100 bp one-way **plus** an explicit borrow/locate fee and an availability screen on the low leg; **fail if** the no-microcap EW H–L is ≤ 0 at **25 bp one-way net of borrow** (`research-defined`), or if annualised net Sharpe < **0.5** (`research-defined`; no source Sharpe exists to compare against).
- **F3 — Capacity / large-cap gate (research-proposed):** require the **value-weighted** net-at-25 bp spread to reach **t ≥ 2.0** (`research-defined`). Pre-registered note: the source's own Table 26 value is **t = 1.23**, so on the source's numbers this gate **already fails** — the strategy must then be declared small/illiquid-capacity only.
- **F4 — Reversal orthogonalisation (research-proposed, benchmarked to source §5.2):** residualise the signal on past 1/3/12-month returns plus the full control set and re-estimate; **fail if** the 1-month slope falls below the source's own residualised **34 bp** or its **t < 2.0** (`research-defined`).
- **F5 — Placebo battery (partly source-run):** the source's 1,000 flow↔holdings remappings gave p = 0.001 (Table 16); add a **1,000-draw within-year date-shuffle** of the signal and require **|z| ≥ 2.0** on the shuffled-vs-true distribution (`research-defined`).
- **F6 — Multiplicity control (research-proposed):** apply Benjamini–Hochberg FDR and/or deflated Sharpe across the full printed grid (measures × horizons × samples × state splits); **fail if** the headline no-microcap ForcedSale 1m and 6m cells do not survive **q < 0.10** (`research-defined`).
- **F7 — Frozen forward test (research-proposed):** freeze the entire pipeline at **November 2024** (sample end) and run it forward on new data with no re-tuning; **fail if** the 1-month no-microcap slope retains **< 50%** of the source's **65.43 bp** (`research-defined`).
- **F8 — Pre-registered state gate ablation (research-proposed):** fix the Scarcity composite weights and the low/high threshold *before* estimation; **fail if** the high-minus-low slope difference is not positive with non-overlapping 95% CIs at **both** 1m and 3m, or if the Table 20-style component interactions keep opposite signs (`research-defined`).
- **F9 — Competing-mechanism horse race (research-proposed):** compare against (i) a plain past-return reversal portfolio, (ii) index-reconstitution forced-flow dates, (iii) sector-level fund-flow rotation; **require ≥ 10 bp/month incremental** EW spread after costs (`research-defined`).
- **F10 — Second-vendor and capacity checks (research-proposed):** rebuild the signal from a second mutual-fund holdings source and require **Spearman ≥ 0.80** of the cross-sectional `ForcedSale` rank (`research-defined`); then re-run F2 under a **≤20% of 21-day dollar-volume participation cap** with an impact model (`research-defined`).

Action on failure: the hypothesis is demoted to "priced-but-not-tradable in our stack" (or "reversal-proxy only") and no production-card or candidate-pool nomination proceeds — adoption is a separate, explicitly reviewed decision in any case.

## Crypto portability

**`unproven`.** The mechanism originates in traditional-asset market structure and the source demonstrates it **only** in US equities; nothing in v1 is crypto evidence.

- **Structural dependency:** the shock generator is **open-end mutual-fund redemption** mapped through **periodic disclosed portfolio holdings**, plus **Form 13F** for the investor-base margin. Crypto has no comparable open-end-fund/13F disclosure complex; the nearest analogue (US spot-ETF creations/redemptions) is already covered by a **different** repository record with a different horizon and mechanism (`bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01.md`).
- **Session structure:** 24/7 trading removes the discrete close/open and T+N disclosure-lag structure on which the reported-holdings timing rule depends; there is no "month-end report" clock.
- **Venue fragmentation / registry:** no single holdings registry; on-chain wallets are transparent but are not fund-redemption-driven residual supply; perp liquidation cascades are a *different* forced-seller channel (see repo liquidation records) and are not modelled here.
- **Funding/borrow/shorting:** perp funding and isolated-margin liquidation dynamics have no analogue in the paper's capital-wedge term; the paper itself models no short-side cost at all.
- **Breadth:** a shift-share over a long-only open-end fund complex over ~5,559 no-microcap names has no crypto equivalent in breadth; a 25-of-N design would be far noisier.

Label: **`unproven` — a ported hypothesis, not crypto empirical evidence.** Any crypto adaptation must be re-derived from a crypto-native forced-seller channel and re-falsified under F1–F10.

## Limitations

- `underspecified`: portfolio sort bucket count and H–L construction; holding/overlap convention for 3/6/12-month spreads; `Scarcity` and `ThinBase` component weights, standardisation and split thresholds; flow-forecast functional form; distress/residual-redemption tail definitions; redemption-stress series construction; tie handling; within-month universe churn; gross exposure/leverage; order type, fill model, latency, participation cap; borrow/short availability and cost; capacity.
- `data gap`: mutual-fund data vendor; fund-level survivorship/merger/share-class treatment; 13F reporting-lag treatment for `ThinBase`; any Sharpe/drawdown/Sortino figure (none exists in v1); code/data availability (none stated); timezone/publication convention for fund report dates.
- `not independently reproduced`: every empirical claim in this record.
- `unproven`: causal separation of "costly absorption" from generic loser reversal beyond the source's own diagnostics; identification of the marginal absorber; scalability beyond EW small/mid names (source's own §1/§6 caveat).
- **Source-internal unreconciled items:** Table 9 (44.09) vs Table 26/§4.5 (47.88) for the same-named spread; Appendix Table 16's placebo "true coefficient" (77.26) matches no printed baseline; rendered date line "August 24, 2026" postdates the v1 submission (29 May 2026).
- **Inference risk (our count):** large printed grid with no multiplicity/selection adjustment; several headline cells rest on composite gates whose components carry opposite-signed interactions (Table 20).
- **Sample:** ends **November 2024**; single-author preprint, not peer reviewed; universe is US equities only.
- Ordinary repeated content does not apply here (this is a new mechanism family for this repository), but the incremental-write threshold was checked: the record is written because it adds a **new signal construction, new data dependency, and new negative-evidence set**, not a reframing of an existing capture.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no signal pipeline, no backtest, no Qlib run, no production card, no Paper/Testnet/Live activity of any kind. This document is a normalized research capture only, and its presence in the repository does not imply any validation stage has begun.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence here does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. No wording, evidence count, confidence value, or negative-result framing in this record promotes it to any later stage; adoption would require a separate explicit review.

## Related Wiki records

Read-only `kb_search` on Hermes Wiki Brain (2026-09-24; queries: "mutual fund flow forced selling liquidity absorption expected returns" → 0 results, "slow-moving capital intermediary flow pressure" → 0 results, "fund flow cross-section stock returns", "liquidity risk premium illiquidity cross-sectional"; **no Wiki write was performed**). **No Hermes Wiki Brain page exists for residual supply, risk absorption, or mutual-fund forced-sale pressure**, so no link is fabricated for the core mechanism. Confirmed-existing related pages:

- [[quant/beta-times-quantity-noise-trader-flow-factor-pricing-2026-09-07]] — flow-based pricing from a *different* source (arXiv `2609.05162`); useful contrast for whether flow's priced channel is beta×quantity rather than redemption-forced inventory.
- [[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]] — the other major *forced-flow* mechanism in the repo (scheduled index rebalancing); key competitor explanation for F9.
- [[quant/order-flow-matched-filter-normalization-investor-segmentation-2026-09-02]] — investor-segmented signal extraction from order flow; alternative way to proxy who is forced to trade.
- [[quant/illiquidity-at-risk-realized-amihud-mem-jump-tail-contagion-2026-09-02]] — Amihud-based liquidity tail forecasting; candidate conditioning variable for the Scarcity gate (F8).
- [[quant/earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13]] — scheduled-jump risk-premium falsification template (decay/gate methodology comparable to F7/F8).

Adjacent repository records that are **not** Wiki links (dedup context only; different source identities): `bitcoin-us-spot-etf-net-flow-next-day-drift-2026-09-01.md`, `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md`, `european-2020-short-selling-ban-liquidity-left-tail-institutional-ownership-did-2026-09-22.md`, `usdt-exchange-net-inflow-buy-side-liquidity-drift-1h-2h-2026-09-03.md`, `crypto-token-unlock-72h-supply-shock-event-short-2026-09-12.md`. No existing record covers arXiv `2605.30672`, open-end-fund redemption-forced `ForcedSale`/`AbsInv`, or a residual-supply absorption premium.

## Sources

- Ziyao Wang, *Residual Supply and the Price of Risk Absorption*, **arXiv:2605.30672v1 [q-fin.GN; also econ.GN]**, submitted 29 May 2026 00:05:09 UTC — https://arxiv.org/abs/2605.30672
- Full text (read directly for this record): https://arxiv.org/html/2605.30672v1 — §§1–7, Appendices A/B/C; Tables 1–29; Figures 1–4 (captions). `https://arxiv.org/html/2605.30672v2` → HTTP 404 (v1 is the only version).
- PDF: https://arxiv.org/pdf/2605.30672v1 (HTTP 200; 662,641 bytes; `last-modified: Mon, 01 Jun 2026 00:22:28 GMT`; `etag "CM/DloTj5JQDEAI="`).
- DOI (arXiv-issued, DataCite): https://doi.org/10.48550/arXiv.2605.30672 (HTTP 200 on 2026-09-24; no publisher DOI, no journal-ref, no comments).
- License: arXiv.org perpetual non-exclusive license (`licenses/nonexclusive-distrib/1.0/`).
- Downstream data named by the paper (not independently re-fetched): CRSP daily/monthly stock data with share codes 10/11 (Jan 2003 – Nov 2024), Compustat characteristics, open-end mutual-fund TNA/returns/holdings (vendor not stated), SEC Form 13F quarterly holdings, Cboe VIX and Chicago Fed NFCI for the state variables.
