---
schema: strategy-research-record-v1
title: "Day-ahead BESS arbitrage scheduled from a multidimensional probabilistic profit ensemble with a loss-probability stopping rule (MS-ave)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - electricity
  - day-ahead-market
  - battery-energy-storage
  - probabilistic-forecasting
  - ensemble-forecasting
  - multidimensional-forecasting
  - risk-threshold-stopping-rule
  - germany
  - spain
status: research-only
confidence: medium
source_as_of: 2026-06-20
sources:
  - "Tomasz Weron, Katarzyna Maciejowska, 'From electricity prices to profits: multidimensional probabilistic forecasting for BESS trading', arXiv:2608.26122v1 [q-fin.ST], submitted 20 June 2026. https://arxiv.org/abs/2608.26122"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Source-internal provenance metadata is unreconciled: the identifier block is arXiv:2608.26122 (2026-08) while the dateline, the submission-history entry and the arXiv API <published> field all say 20 June 2026 (v1, 14:36:04 UTC), the served PDF carries /CreationDate and /ModDate D:20260828 and the arXiv API <updated> field reads 2026-09-30T04:25:57Z although the submission history lists no v2; the submission-history size (356 KB) also does not equal the served PDF size (891,772 bytes) and the source does not say whether that figure reports source or PDF. No explanation is stated in the source."
  - "The Section 5.3 / Section 6 claim that MS-ave 'generates profits that exceed those of ARX-s by 2.5%-5.5%' reproduces only under an oracle-relative percentage-point reading (Table 4: 85.49 - 83.03 = 2.46 pp; Table 5: 66.97 - 61.43 = 5.54 pp). Under the natural reading of the same words as a relative gain over ARX-s it would be 2.96% (Germany) and 9.02% (Spain), and the prose does not say which baseline (ARX or ARX-s) or which unit is intended. Both readings are retained; neither is silently preferred."
---

# Day-ahead BESS arbitrage scheduled from a multidimensional probabilistic profit ensemble with a loss-probability stopping rule (MS-ave)

## Provenance

- **Primary source:** Tomasz Weron and Katarzyna Maciejowska, *"From electricity prices to profits: multidimensional probabilistic forecasting for BESS trading"*, `arXiv:2608.26122v1 [q-fin.ST]` (primary Statistical Finance; cross-list Applications, `stat.AP`).
- **Stable URL:** https://arxiv.org/abs/2608.26122 · **arXiv-issued DataCite DOI:** https://doi.org/10.48550/arXiv.2608.26122 · **PDF:** https://arxiv.org/pdf/2608.26122v1.
- **Authors, exactly as the source states:** Tomasz Weron (Department of Applied Mathematics, Wrocław University of Science and Technology, Poland; corresponding author; `tomasz.weron@pwr.edu.pl`) and Katarzyna Maciejowska (Department of Operations Research and Business Intelligence, Wrocław University of Science and Technology, Poland; `katarzyna.maciejowska@pwr.edu.pl`). The abs page exposes exactly two author links; the PDF title block and the PDF `/Author` metadata carry the same two names in the same order.
- **Version / date:** dateline `[Submitted on 20 Jun 2026]`; submission history `From: Katarzyna Maciejowska [view email] [v1] Sat, 20 Jun 2026 14:36:04 UTC (356 KB)`; only v1 exists. The PDF page-1 footer prints `arXiv:2608.26122v1 [q-fin.ST] 20 Jun 2026`. The arXiv API returns `<published>2026-06-20T14:36:04Z` and `<updated>2026-09-30T04:25:57Z`. **The 2608 (2026-08) identifier block against a 20 June 2026 submission, the 2026-08-28 PDF generation stamp, the 2026-09-30 API update with no v2, and the 356 KB vs 891,772-byte size mismatch are unreconciled** and are recorded as a source-internal provenance contradiction, not repaired here.
- **Publication status:** **preprint only.** The abs page has **no Comments field, no Journal reference, no publisher DOI** (cell probes: 0 hits each); the only DOI is the arXiv/DataCite identifier. **No peer-review statement** appears anywhere in the source. Licence: **CC BY 4.0** (abs-page licence link `creativecommons.org/licenses/by/4.0` and PDF `/License`).
- **Primary-source checksum (performed 2026-09-30):**
  - PDF `https://arxiv.org/pdf/2608.26122v1` → HTTP 200, **891,772 bytes**, sha256 `919d484347c39cc360ba4977da724704476a0da2d7aac01b8a19620908664c72`, PDF metadata `/Title` = printed title, `/Author` = `Tomasz Weron; Katarzyna Maciejowska`, `/License` = CC BY 4.0, `/DOI` = `https://doi.org/10.48550/arXiv.2608.26122`, `/arXivID` = `https://arxiv.org/abs/2608.26122v1`, `/CreationDate` = `/ModDate` = `D:20260828000055+00'00'`, Creator `arXiv GenPDF (tex2pdf:4af3385)`, Producer `pikepdf 8.15.1`. Extracted with **pypdf 6.16.2 → 26 pages, 68,560 characters, 1,029 lines, read end to end**: Abstract, Sections 1–6, Equations (1)–(17), Tables 1–5 (every cell), Figures 1–6 captions, the AI-use / CRediT / competing-interest / acknowledgments declarations, and the 28-item reference list.
  - abs page `https://arxiv.org/abs/2608.26122` → **41,117 bytes**, sha256 `78b433951380ed553918642745cbaeccb26c3c2593fe05058e4f63c07c1e6928` (source for dateline, authors, subjects, licence, DOI, submission history).
  - `https://arxiv.org/html/2608.26122v1` → **HTTP 404**, no LaTeXML full text exists, so the pinned PDF is the only full text.
  - arXiv API `id_list=2608.26122` read for `published` / `updated`.
- **Declarations and funding, exactly as printed:** generative-AI declaration (ChatGPT and DeepL used to improve language, authors take responsibility); CRediT (Weron: Conceptualization, Investigation, Software, Visualization, Writing – review & editing; Maciejowska: Conceptualization, Funding acquisition, Investigation, Methodology, Writing – original draft, Writing – review & editing); "no known competing financial interests"; funding `National Science Center (NCN), Poland, grant SONATA BIS no. 2019/34/E/HS4/00060`.
- **Data as-of (source-reported):** day-ahead prices, TSO load forecasts and TSO renewable-generation forecasts for **1 January 2021 – 31 December 2024**, hourly; **2021 used purely for model calibration, 2022–2024 the three-year validation period** (Section 2). Electricity data "freely available at transparency.entsoe.eu"; coal (API2) and natural gas (TTF) futures from Investing.com.
- **Source-identity deduplication (whole repository, before writing, 2026-09-30):** `rg -uuu` across **all 2,660 `*.md` files (hidden-inclusive: `.git`, `.mimo-worktrees`, `.agents`, `.hermes`) plus `coverage_manifest.csv` (5,808 lines)** for the fixed strings `2608.26122`, `Tomasz Weron`, `From electricity prices to profits`, `multidimensional probabilistic forecasting`, `MS-ave`, `Maciejowska & Nitka`, `Arbitrage in short-term electricity`, `2604.19580` → **0 matching files for every probe**; the manifest alone also returns 0 for `2608.26122` and `Maciejowska`. The loose token `Maciejowska` returns **exactly one file**, `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md`, where it is only an in-paper citation ("Maciejowska et al., 2026") inside another paper's reference apparatus — not this source identity. Positive control `novy-marx` returns **53 files** in the same session, so the index is live. `git log --oneline -20` was inspected as a convenience glance only and does **not** by itself satisfy dedup; `git pull origin main` at run start returned `Already up to date` at `14e4fd2`.
- **Four-axis material distinction vs the existing electricity records** (all different source identities; the mechanism, signal construction and material data dependency differ in every pair):
  - vs `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md` (Lipiecki, Kourentzes & Weron, arXiv:2609.23223 — note **Rafal Weron is a different person from Tomasz Weron; no shared author here**): mechanism = temporal-hierarchy *point*-forecast reconciliation of prices/spreads vs **joint 24-hour ensemble whose members are pushed through the profit function**; signal = reconciled spread rule vs **ensemble-median argmax over 276 charge/discharge pairs gated by a loss-probability threshold**; data dependency = hierarchy only vs **TSO load/RES forecasts plus day-(t−2) coal and gas futures**.
  - vs `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23.md` (GitHub `CodingxFaisal/power-spread-trader`): mechanism = z-score fade of cross-border day-ahead spreads (a position trade across borders) vs same-day single-asset storage scheduling; universe = 7 cross-border products vs two single national day-ahead auctions; horizon = multi-hour position vs one charge/discharge cycle inside a delivery day.
  - vs `eex-peak-baseload-forward-spread-risk-premium-matrix-har-rcv-2026-09-24.md` (Kloster & Benth, arXiv:2606.05991): mechanism = variance/skewness-priced **forward risk premium in traded futures** vs **physical intraday arbitrage of a battery**; universe = EEX monthly peak/baseload futures vs day-ahead spot hours; signal = matrix-HAR realized-covariance premium regression vs probabilistic profit ensemble.
  - vs `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22.md` (Yu & Bunn, arXiv:2609.23598): universe/market stage = 15-minute **continuous intraday** orderbook vs **day-ahead auction** hours; target = buy/sell price trajectory forecast accuracy with **no trading simulation** vs an explicitly simulated BESS profit/ VaR / trade-frequency evaluation; method = side-specific cross-attention network vs random-split ensemble of ARX errors.
- **Wiki Brain (read-only, this run):** `kb_read quant/strategy-research-record-spec-v2.md` → **file does not exist**, so the run **failed closed onto v1**, canonical `quant/strategy-research-record-spec-v1.md`, **10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`**. `kb_search "day-ahead electricity price forecasting battery arbitrage"` → 0 pages; `kb_search "electricity"` → 4 pages, none on this mechanism. **No stable Wiki Brain page covers this record, so no Wiki link is asserted.** No Wiki page was written.
- **Boundaries of this run:** no Wiki Brain write, no Kanban, no backtest, no market-data download, no dependency install, no third-party code executed, no candidate-pool or downstream write; coordinator and other scouts' untracked files were neither staged nor cleaned.

## Economic mechanism

### Source-reported

The authors' stated thesis is a **forecast-quality → decision-quality channel**, not a return premium:

1. Point forecasts of day-ahead prices are insufficient for a storage operator because the decision depends on the **whole daily price curve**, so the joint (24-hour) distribution must be represented (Sections 1, 3).
2. The **Multiple Split (MS)** method (Maciejowska & Nitka, 2026) randomly splits data into estimation and calibration subsets, repeats the split `N` times, and builds an ensemble `point prediction + calibration residual` whose residuals preserve the **within-day correlation structure**, so the ensemble is inherently multidimensional without an explicit inter-hour dependency model (Sections 3.5, 3.5.1).
3. The paper's contribution is **forecast averaging across estimation windows of different lengths inside MS** (`MS-ave`), with a new algorithm that keeps the calibration window common across windows so the averaged ensembles stay comparable (Section 3.5.1, Fig. 4, Table 1).
4. Applying the **profit function directly to each ensemble member** yields a probabilistic forecast of daily BESS profit; that distribution supports (a) the choice of charging and discharging hours and (b) a decision to abstain when the probability of a loss is too high (Sections 1, 3, 4.1.3).
5. Claimed economic effect: with **non-zero operating cost**, abstaining limits losses and better-calibrated profit forecasts produce higher profit *and* lower downside risk (Sections 5.3, 6). The source explicitly frames this as "decision-relevant quantities" evaluation rather than a new alpha family.

Named benchmark mechanisms it is compared against: In-Sample error ensemble (IS), Historical Simulation (HS), Quantile Regression Machine (QRM), their `-ave` variants, a fixed-hour Naïve rule, a point-forecast ARX rule (with and without a stop), and a perfect-foresight Oracle.

### Research interpretation

Falsifiable form of the hypothesis: **the cross-hour dependence of day-ahead price errors is decision-relevant**, i.e. a strategy that (i) preserves the empirical joint distribution of the 24 hourly errors and (ii) acts on the *distribution* of the derived profit (select the pair with the highest ensemble median, then abstain when `prob(loss) ≥ q`) earns more and loses less in the tail than the same ARX backbone used as a point forecast, **once a per-MWh operating cost makes bad days negative**.

Component roles (hybrid; ablation is required before any component is credited with alpha):

```text
Regime / backbone:  per-hour ARX with weekday dummies, lags {1,2,3,7},
                    previous-day min/max, TSO load and RES forecasts,
                    coal (API2) and gas (TTF) at t-2; refit daily on 364 days
Signal:             multidimensional ensemble of the 24-hour price vector
                    (MS / MS-ave random splits with window averaging)
Decision:           argmax over 276 pairs (h_ch < h_dis) of the ensemble
                    MEDIAN of forecast profit
Risk gate (stopping rule): abstain for the day when prob(pi_hat < 0) >= q
Risk/exit:           one charge + one discharge inside the delivery day,
                    then flat; no intraday re-dispatch, no stop-loss
Cost layer:          fixed variable operating cost Cost in {0, 40} EUR/MWh
```

The **alpha-bearing candidate is the decision layer (joint-distribution profit forecast + loss-probability gate)**, not the ARX backbone (both sides share it) and not the cost or sizing rules (risk management, not alpha). The source's own evidence says the gate only pays once costs are non-zero, so the hypothesis is explicitly **cost-conditional**.

## Signal

All items below are **source-reported** unless tagged.

- **Formation timestamp:** computations are performed **at 11:00 a.m. on the day before delivery**, with the information set restricted to data available by then; day-ahead bids for all 24 hours are submitted "around noon on the day preceding delivery" (Section 3). Timezone / clock convention: **not stated in source** → `data gap`.
- **Lookback:** rolling **364-day** estimation sample, parameters re-estimated for **each day `t` separately** (Section 3.1). Lag structure of Eq. (1): seven weekday dummies; AR lags `p ∈ {1,2,3,7}`; previous-day minimum and maximum DA price; exogenous forecasted load `L` and renewable generation `RES` (hourly, TSO-provided); coal `C` and gas `G` **at `t−2`**, daily. Endpoints / warm-up / missing-value handling: **not stated in source** → `data gap`.
- **Ensemble construction (all source-reported, Sections 3.2–3.6, Table 1):**
  - `IS`: 364 in-sample errors; estimation 364 / calibration 364 / ensemble 364.
  - `HS`: calibration window = last **182** observations; estimation window ≤ 182; ensemble 182. `HS-ave` estimation windows 42, 56, 178, 182.
  - `QRM`: quantile regression of the 99 percentiles `τ = 0.01…0.99` on the point forecast, hour-specific coefficients, post-sorted for monotonicity; **cross-hour independence assumed**, empirical application uses the bi-hourly distribution → ensemble `99²`; estimation 182 / calibration 182; `QRM-ave` windows 42, 56, 178, 182.
  - `MS`: random disjoint split of the sample, repeated `N` times; calibration size 182; ensemble `182 · N`.
  - `MS-ave`: samples `|S1|=84, |S2|=112, |S3|=357, |S4|=364` → estimation sets `42, 70, 315, 322`, **common calibration set of 42**, ensemble `42 · N`; one iteration yields `T1/2 = 42` predictions.
  - `N` (number of random splits) is used symbolically throughout and **no numeric value is printed** → `data gap` (the MS/MS-ave ensembles are not reproducible from the text alone).
- **Long entry (buy to charge):** hour `h_ch` selected to maximize the chosen criterion over the **276 admissible pairs** `h_ch < h_dis` (research-checked `C(24,2) = 276`); for probabilistic strategies the criterion is the **highest median of the ensemble profit distribution** (Section 4.1.3).
- **Short entry:** none. The strategy is a physical long-storage round trip (charge then discharge); it never short-sells.
- **Exit:** discharge at `h_dis` the same delivery day, then flat. No stop-loss, no take-profit, no overnight carry.
- **Holding period:** intraday only — one cycle per delivery day; no position crosses a day boundary.
- **Re-entry:** a fresh decision every day at 11:00 a.m. The day may be skipped entirely (abstain).
- **Stopping rule (source-reported, Eq. 16):** trade only if `prob(π̂_t < 0) < q`; otherwise daily profit is set to 0. `q` is swept over `0.1 … 0.9` plus `q = 1` (unconditional). The source equates this to the rule `Q_q(π̂_t) < 0` of Maciejowska & Nitka (2026) and says a risk-averse manager might use `q = 0.3`, a risk-neutral one something near `q = 0.5`.
- **Reported `q*` (source-reported, Tables 4–5):** `q*` is "the optimal risk threshold **that maximizes profits** (for strategies incorporating a stopping rule)" evaluated **on the evaluation window itself** — a point the source states plainly. MS-ave: `q*` 0.4 → 0.3 (Germany) and 0.6 → 0.4 (Spain) when the cost moves 0 → 40 EUR/MWh; in the zero-cost setup the most profitable `q*` sits around 0.5.
- **Position sizing:** **fixed 1 MWh usable energy, C-rate 1** (can be fully charged or discharged within one hour → 1 MW). No sizing rule, no vol targeting, no capital allocation → any such rule would be `research-proposed`.
- **Benchmarks (source-reported, Sections 4.1.1–4.1.4):** Naïve (charge 04:00, discharge 20:00); `ARX` (point-forecast argmax, no stop); `ARX-s` (stop when `π̂_t < 0`); `Oracle` (perfect foresight: chooses hours *and* refrains when realized profit would be negative).
- **Specification status:** the decision rules are **fully specified except** for `η`, `N`, the exact base over which `Cost` is charged, the timezone, and the `q*` selection protocol's out-of-sample treatment — so the strategy is **partially underspecified** for independent reconstruction from the text alone.

## Required data

- **Instruments / universe:** hourly **day-ahead** electricity of the **German** bidding zone and the **Spanish** market; 24 hourly products per day (treated as distinct products, not a time series — Section 3).
- **Venue / market type:** day-ahead spot auction (EPEX-style national DA markets, sourced via ENTSO-E Transparency Platform); **no futures, no options, no intraday, no balancing** in the evaluated strategy (the source lists intraday/balancing extension as future work).
- **Timeframe:** hourly bars; daily decision at 11:00 a.m. D-1; four full calendar years 2021–2024 (calibration 2021; validation 2022–2024).
- **Fields (all source-reported):** DA price `DA_t,h` (hourly); TSO-forecast load `L_t,h`; TSO-forecast renewable generation `RES_t,h` (solar + wind onshore/offshore combined); daily coal API2 and gas TTF futures `C_{t-2}`, `G_{t-2}`; derived previous-day min/max price; weekday dummies.
- **Point-in-time / availability:** the source restricts the information set to 11:00 a.m. D-1 but **does not state TSO-forecast vintages, revisions, or restatement handling**, nor any ENTSO-E revision handling → `data gap`. Investing.com coal/gas vintages and licensing → `data gap`.
- **Timestamp / timezone:** "hourly resolution" only; **timezone, clock source, DST handling and out-of-order records are not stated** → `data gap`.
- **Missing data:** imputation / suspension / stale-value handling **not stated** → `data gap`; imputation is forbidden by our spec unless the source justifies it.
- **Cost / fee fields:** variable operating cost `Cost ∈ {0, 40} EUR/MWh` (Section 5.3, Eq. 14); German 2024 grid fees quoted as 4 ct/kWh (energy-intensive industry), 9 ct/kWh (other commercial), 11 ct/kWh (households) = 40 / 90 / 110 EUR/MWh (Section 4) — research-checked `ct/kWh × 10 = EUR/MWh`. Nothing else: no maker/taker fees, no bid-ask, no imbalance charge, no imbalance settlement, no balancing-market fee, no ancillary-revenue field, no degradation curve.

## Execution assumptions

Determined at **Methods level** (Sections 3, 4, 4.1, 4.2, 5.3; Eqs. 14–17), not from the abstract.

- **Signal-to-order timing:** decision computed 11:00 a.m. D-1; submitted in the day-ahead auction around noon; **cleared at the day-ahead clearing price** for both charge and discharge (price-taking, full fill).
- **Order type / fill model:** a day-ahead auction schedule for a 1 MW / 1 MWh asset. **No limit order, no queue, no partial fill, no rejection, no imbalance penalty** is modelled (`limit order 0`, `market order 0`, `fill 0` occurrences in the pinned text) → these are `data gap`, **never read as zero**.
- **Fees:** only the grid/distribution-style `Cost` (40 EUR/MWh) is modelled, and the source itself calls it "the **transaction costs** of BESS" (`transaction cost` appears exactly **once**, Section 5.3). Whether the charge is applied to energy purchased, energy cycled, or both, and whether any revenue-side fee applies, **is not restated** → underspecified.
- **Round-trip efficiency:** `η` enters Eq. (14) as `π_t = (1 − η)·DA_{t,hdis} − (1 + η)·DA_{t,hch} − Cost` and is described as "the round-trip efficiency of charging and discharging"; **no numeric value is printed anywhere** (3 occurrences of `η`, none numeric) → `data gap`; absolute profit levels are therefore irreproducible from the text.
- **Spread:** the three `spread` occurrences in the source all mean the **within-day price spread** (or the intraday-vs-day-ahead spread), i.e. the thing being harvested. **No bid-ask / transaction spread is modelled** (`bid-ask 0`).
- **Slippage / impact / latency:** `slippage 0`, `market impact 0`, `latency 0` occurrences → `data gap`, not zero. The asset is 1 MWh and price-taking, so impact is arguably immaterial, but the source never says so.
- **Funding / borrow / leverage / liquidation / margin:** `funding 0` as a cost (the single `funding` hit is the CRediT phrase "Funding acquisition"), `borrow 0`, `leverage 0`, `liquidation 0` → not applicable to a physical battery and not modelled.
- **Capacity / turnover / participation:** `turnover 0`, `maker 0`, `taker 0`; `capacity 5` occurrences are **physical** BESS/RES capacity only → no trading-capacity or participation-cap model; any capacity claim beyond 1 MWh is `research-proposed`.
- **Multi-cycle / degradation / ancillary:** explicitly **excluded** and listed as future work (Section 6: "battery degradation, multi-cycle operation and participation in multiple electricity markets").
- **Oracle leakage:** the Oracle row is a **perfect-foresight upper bound**, clearly labelled; it must never be read as an achievable result.
- **`q*` leakage:** because `q*` is selected by maximising profit on the evaluation window (Tables 4–5), the reported profits embed an **ex-post-selected risk threshold** → recorded under Negative evidence and gated in the Falsification plan.

## Evidence

### Source-reported

Everything in this subsection is third-party (Weron & Maciejowska, 2026) and **has not been independently reproduced**. Every figure carries its Table / Section location; asset class is **European day-ahead electricity (Germany, Spain), not crypto**.

**Forecast accuracy of prices — Table 2** (PICP at nominal 95%; Kupiec column = share of hours where the null of correct coverage is not rejected; CRPS⁹⁹, CRPS²⁰, Energy Score; validation 2022–2024):

| Market | Method | PICP95% | Kupiec | CRPS99 | CRPS20 | ES |
|---|---|---|---|---|---|---|
| Germany | IS | 92.64 | 8.33 | 18.666 | 8.514 | 18.473 |
| Germany | HS | 94.45 | 95.83 | 17.800 | 8.102 | 17.639 |
| Germany | QRM | 93.43 | 45.83 | 17.217 | 7.694 | 17.063 |
| Germany | MS | 95.43 | 91.67 | 18.313 | 7.986 | 18.142 |
| Germany | HS-ave | 94.44 | 91.67 | 16.742 | 7.756 | 16.591 |
| Germany | QRM-ave | 93.55 | 45.83 | **16.231** | 7.399 | **16.085** |
| Germany | MS-ave | 94.29 | 91.67 | 16.421 | **6.999** | 16.268 |
| Spain | IS | 93.28 | 25.00 | 12.848 | 5.562 | 12.714 |
| Spain | HS | 94.92 | 100.00 | 12.929 | 5.407 | 12.807 |
| Spain | QRM | 93.52 | 37.50 | 12.837 | 5.447 | 12.719 |
| Spain | MS | 95.51 | 91.67 | 12.705 | 5.358 | 12.585 |
| Spain | HS-ave | 94.74 | 100.00 | 12.179 | 5.207 | 12.065 |
| Spain | QRM-ave | 93.79 | 54.17 | 12.054 | 5.203 | 11.943 |
| Spain | MS-ave | 94.18 | 75.00 | **12.016** | **5.030** | **11.902** |

Section 5.1 claims: MS-ave attains the **lowest CRPS overall, beaten only by QRM-ave on CRPS99 in Germany** (verified against the table); forecast averaging cuts CRPS99 by **5.4%–10.3%** and CRPS20 by **3.7%–12.4%** (research-recomputed 5.42–10.33 and 3.70–12.36 across the six HS/QRM/MS pairs); IS confirms correct coverage in only 8.3%–25% of hours; MS rejects nothing in 91.7% of hours.

**Forecast accuracy of BESS profits — Table 3** (left panel = fixed schedule charge 04:00 / discharge 20:00; right panel = average over all 276 admissible pairs):

| Market | Method | PICP h4-20 | CRPS99 | CRPS20 | PICP all | CRPS99 | CRPS20 |
|---|---|---|---|---|---|---|---|
| Germany | IS | 91.06 | 19.805 | 9.211 | 91.55 | 15.673 | 7.165 |
| Germany | HS | 93.70 | 20.269 | 9.239 | 93.81 | 15.668 | 7.108 |
| Germany | QRM | 96.62 | 19.963 | 9.088 | 97.56 | 16.456 | 8.177 |
| Germany | MS | 94.80 | 19.533 | 8.766 | 95.21 | 15.351 | 6.690 |
| Germany | HS-ave | 92.88 | 20.240 | 9.672 | 93.63 | 15.486 | 7.311 |
| Germany | QRM-ave | 96.44 | 19.438 | 8.969 | 97.26 | 16.084 | 8.063 |
| Germany | MS-ave | 94.71 | **18.617** | **8.176** | 94.70 | **14.321** | **6.248** |
| Spain | IS | 93.98 | 13.694 | 5.905 | 92.71 | 10.921 | 4.664 |
| Spain | HS | 94.07 | 13.523 | 5.797 | 94.26 | 11.133 | 4.652 |
| Spain | QRM | 97.63 | 13.803 | 6.159 | 98.42 | 11.917 | 5.670 |
| Spain | MS | 96.17 | 13.588 | 5.801 | 95.65 | 10.817 | 4.516 |
| Spain | HS-ave | 94.07 | 13.534 | 5.705 | 94.30 | 11.216 | 4.732 |
| Spain | QRM-ave | 97.63 | 13.541 | 5.916 | 98.10 | 11.736 | 5.502 |
| Spain | MS-ave | 95.53 | **12.973** | **5.459** | 94.95 | **10.588** | **4.396** |

Section 5.2 reading: IS profit intervals are too narrow (91.06%–93.98% coverage); QRM's cross-hour independence over-covers (96.44%–98.42%); MS/MS-ave sit closest to nominal while keeping the residual dependence structure.

**Economic evaluation — Table 4 (Germany) and Table 5 (Spain).** `Profit` is the three-year total for a 1 MWh battery; for every strategy except Oracle it is printed **as a percentage of the Oracle total**; `VaR5%` is the 5% quantile of the daily profit distribution **computed only on days when trading occurred**; `Trade` = share of days traded.

| Strategy | DE q* (cost 0) | DE trade | DE profit | DE VaR5% | DE q* (40) | DE trade | DE profit | DE VaR5% |
|---|---|---|---|---|---|---|---|---|
| Oracle | – | 99.91 | **107280.27 EUR** | 22.51 | – | 80.38 | **66054.60 EUR** | 4.72 |
| Naïve | – | 100.0 | 49.92 | −13.63 | – | 100.0 | 14.71 | −53.63 |
| ARX | – | 100.0 | 90.35 | 12.10 | – | 100.0 | 80.37 | −27.90 |
| ARX-s | – | 99.91 | 90.36 | 12.47 | – | 91.88 | 83.03 | −21.77 |
| IS | 0.5 | 99.91 | 90.04 | 11.61 | 0.3 | 82.39 | 83.76 | −16.47 |
| HS | 0.7 | 100.0 | 87.86 | 10.65 | 0.3 | 81.02 | 80.09 | −18.68 |
| QRM | 0.6 | 100.0 | 88.27 | 10.43 | 0.5 | 87.32 | 80.10 | −20.50 |
| MS | 0.5 | 99.91 | 90.24 | 11.87 | 0.3 | 79.65 | 84.28 | −15.11 |
| HS-ave | 0.3 | 99.18 | 88.37 | 10.63 | 0.3 | 80.93 | 81.39 | −18.92 |
| QRM-ave | 0.5 | 99.82 | 88.58 | 11.88 | 0.4 | 80.02 | 81.02 | −18.09 |
| MS-ave | 0.4 | 99.54 | **90.88** | **12.98** | 0.3 | 81.20 | **85.49** | **−13.82** |

| Strategy | ES q* (cost 0) | ES trade | ES profit | ES VaR5% | ES q* (40) | ES trade | ES profit | ES VaR5% |
|---|---|---|---|---|---|---|---|---|
| Oracle | – | 99.18 | **61476.70 EUR** | 12.60 | – | 57.48 | **24693.73 EUR** | 2.40 |
| Naïve | – | 100.0 | 10.97 | −51.05 | – | 100.0 | **−150.21** | −91.05 |
| ARX | – | 100.0 | 87.47 | 3.59 | – | 100.0 | 40.24 | −36.41 |
| ARX-s | – | 99.45 | 87.56 | 4.83 | – | 74.73 | 61.43 | −27.88 |
| IS | 0.5 | 99.36 | 86.63 | 3.61 | 0.3 | 56.11 | 64.05 | −21.34 |
| HS | 0.4 | 98.81 | 84.38 | 2.88 | 0.3 | 54.84 | 63.30 | −21.23 |
| QRM | 0.6 | 99.91 | 84.68 | 2.08 | 0.4 | 55.20 | 63.47 | −20.62 |
| MS | 0.5 | 99.36 | 86.97 | 4.80 | 0.4 | 62.96 | 63.44 | −23.32 |
| HS-ave | 0.4 | 98.81 | 83.39 | 0.32 | 0.4 | 62.86 | 59.97 | −23.84 |
| QRM-ave | 0.6 | 99.91 | 84.65 | −0.37 | 0.4 | 56.11 | 61.60 | −22.16 |
| MS-ave | 0.6 | 99.91 | **86.73** | **2.88** | 0.4 | 62.86 | **66.97** | **−21.42** |

Section 5.3 / 6 headline claims, each with its arithmetic status:

- Oracle trades **>99%** of days at zero cost (99.91% DE, 99.18% ES); Spanish Oracle profit is **42.7% lower** than German (research-recomputed 42.70%).
- At 40 EUR/MWh the Oracle trades **80.4% / 57.5%** of days and profits fall **38.4% (DE) / 59.8% (ES)** (research-recomputed 80.38, 57.48, 38.43, 59.83).
- Naïve earns only **49.9% (DE) / 11.0% (ES)** of Oracle at zero cost (research-recomputed 49.92 / 10.97) and **loses** at 40 EUR/MWh in Spain (**−150.21%** of Oracle).
- Point-forecast strategies reach "close to or exceeding 90%" of Oracle (DE zero-cost ARX 90.35, ARX-s 90.36).
- Probabilistic strategies trade **79.7%–87.3% (DE)** and **54.8%–63.0% (ES)** of days at 40 EUR/MWh vs ARX-s at **91.88% / 74.73%** (research-recomputed bands 79.65–87.32 and 54.84–62.96).
- **MS-ave beats ARX-s by "2.5%–5.5%"** and improves `VaR5%` from **−21.77 → −13.82 (DE)** and **−27.88 → −21.42 (ES)** (all four VaR cells verbatim). The 2.5–5.5 range reproduces **only** as oracle-relative percentage points (2.46 / 5.54); as a relative gain it is 2.96% / 9.02% — recorded as an internal contradiction above.
- `q*` moves 0.4 → 0.3 (DE) and 0.6 → 0.4 (ES) for MS-ave when cost is introduced; the profit curve in `q` is concave with a local maximum at `q ∈ [0.3, 0.4]` when Cost = 40 (Figs. 5–6).
- Ranking: MS-ave/MS generate the highest profits for all `q` except 0.1 in Germany; in Spain MS-ave/MS lead for `q > 0.3`; IS is third.
- No **return, Sharpe, CAGR, drawdown or win-rate figure exists anywhere in the source** (`sharpe 0`, `cagr 0`, `drawdown 0`, `win rate 0` occurrences), so there is **no gross-vs-net-of-cost performance claim to preserve** — only profit totals, profit-as-%-of-Oracle, trade frequency and `VaR5%`.

### Independently reproduced

`not independently reproduced`

Arithmetic-only cross-checks of the *printed* values were run (55 checks, 0 failures, exit 0) against the pinned PDF and abs page; they verify **internal consistency of the source's own tables and prose**, not the data, model, or profitability: PDF/abs byte counts and sha256; author/title/subject/licence/DOI/absence of Comments and journal-ref; API `published`; all Table 2/3/4/5 row literals; `C(24,2)=276`; `ct/kWh → EUR/MWh`; the 42.7 / 38.4 / 59.8 / 49.9 / 11.0 / 79.7–87.3 / 54.8–63.0 / 91.88 / 74.73 claims; the CRPS reduction bands 5.4–10.3 and 3.7–12.4; the 2.46 / 5.54 pp decomposition behind "2.5%–5.5%"; and the four `VaR5%` cells. **No market data was downloaded and no forecasting or trading code was executed.**

### Negative evidence

1. **No statistical inference in the source:** `p-value 0`, `confidence interval 0`, `bootstrap 0`, `monte carlo 0`, `walk-forward 0` occurrences in the pinned text — every reported number is an untested point estimate on one 3-year, 2-market window.
2. **The claimed advantage exists only with non-zero operating cost.** Section 5.3 states that at zero cost "strategies based on probabilistic forecasts do not exhibit clear advantages over their point forecast counterparts"; in **Spain at zero cost ARX-s (87.56) beats MS-ave (86.73)**, and in Germany MS-ave's edge over ARX-s is 0.52 pp (90.88 vs 90.36).
3. **`q*` is tuned on the evaluation window itself** ("the optimal risk threshold that maximizes profits", Section 5.3) — reported profits therefore embed an in-sample-selected decision parameter; no nested or forward selection is used.
4. **Profits are reported relative to a perfect-foresight Oracle**; absolute EUR totals are printed **only for the Oracle row**, so strategy-level absolute P&L, Sharpe, and capital efficiency are `data gap` (research-computed illustration only: 85.49% × 66,054.60 ≈ 56,470 EUR over three years for German MS-ave at 40 EUR/MWh — **research-computed from two printed cells, not a source figure**).
5. **Cost sensitivity is extreme and sign-flipping:** at 40 EUR/MWh the Spanish Naïve rule loses 150.21% of the Oracle total, Spanish ARX falls from 87.47 to 40.24, and Oracle frequency drops to 57.48% — small changes in the single modelled cost parameter move outcomes by tens of percent.
6. **A cost parameter calibrated on German grid fees is applied to Spain** (both markets are run at 0 and 40 EUR/MWh) with no Spanish distribution-fee discussion → universality of the 40 EUR/MWh figure is untested.
7. **Cross-hour dependence is the only clearly identified driver.** QRM's independence assumption over-covers profit intervals (96.44%–98.42%) and its strategy profit at 40 EUR/MWh sits near the bottom of the probabilistic set in Germany (80.10, with only HS at 80.09 lower) — consistent with dependence mattering, but it says nothing about MS-ave vs a *strong* point-forecast baseline.
8. **Backbone is deliberately weak and shared:** the source says ARX was chosen for "computational efficiency, interpretability" and lists ML/deep-learning point forecasts as future work, so the comparison isolates the probabilistic layer but leaves the point layer unimproved.
9. **Calibration is imperfect:** MS-ave PICP95 for prices is 94.29% (DE) and 94.18% (ES), below the nominal 95%, and the Kupiec null is not rejected in only **75.00% of hours in Spain** for MS-ave against 91.67% in Germany (Table 2); Table 3 prints **no Kupiec test at all for the profit forecasts**, so their formal coverage is untested.
10. **Sample:** one battery (1 MWh, C-rate 1), one cycle per day, two markets, 2022–2024 validation only, 2021 burned on calibration; the window spans the 2022 energy-crisis regime, and no regime breakdown is reported.
11. **Scope exclusions acknowledged by the source:** no degradation, no multi-cycle, day-ahead only (no intraday, balancing, or ancillary revenue) — Section 6 lists all of these as future work.
12. **`VaR5%` is computed only on days actually traded**, so strategies with different trade frequencies are compared on different conditioning sets.
13. **`η` (round-trip efficiency) and `N` (number of random splits) are never given numerically**, so neither the profit level nor the ensembles are reproducible from the text.
14. **No code, repository, or data-availability statement** (`github 0`, `repository 0`, `code availability 0`, `data availability 0`); only the ENTSO-E and Investing.com data pointers.
15. **Point-in-time risk unaddressed:** TSO-forecast vintages/revisions and ENTSO-E revisions are not discussed, so a replication can silently differ in inputs.
16. **Multiple-comparison exposure:** 7 methods × 2 markets × 2 cost levels × 9 `q` values are inspected with no correction, and the headline "best" row is selected after the fact.
17. **Publication status:** preprint with no journal reference and no peer-review statement; unreconciled provenance metadata (see `contradictions`).
18. **No capacity, liquidity or participation analysis** at any scale (physical capacity mentions only).
19. **Absence caveat:** none identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

Each threshold below is **research-defined (a falsification threshold chosen by this scout, not by the source)** unless explicitly quoted from the source. **No-retuning rule:** once a gate is run, the ARX specification, the window lengths (364 / 182 / 84 / 112 / 357 / 364, calibration 42), the four `-ave` window sets, the 1 MWh / C-rate-1 asset, the 276-pair action set, the profit function, the cost grid, and every threshold below are frozen; a failed gate may not be rescued by re-tuning any of them.

1. **F1 — Printed-value reproduction (source-reported numbers).** Re-derive every Table 2/3/4/5 cell and every Section 5.1/5.3/6 claim from the pinned text within ±0.01 pp (profits) and ±0.001 (CRPS/ES). *Status: current arithmetic pass (55 checks, 0 failures); must still be re-run against an independent copy of the PDF.* **Action on failure:** stop; treat the record as unverified.
2. **F2 — Provenance-integrity gate.** Reconcile the identifier/month/size/timestamp anomaly (2608 block vs 20 Jun 2026, 356 KB vs 891,772 bytes, API `updated` 2026-09-30 with no v2) with the arXiv record or the authors. *Status: **currently failing (unresolved)**.* **Action on failure:** keep `contested: true`; do not advance the record beyond research-only.
3. **F3 — Parameter-completeness gate.** The source (or author code) must state `η` and `N` exactly. *Status: **currently failing (both unstated)**.* **Action on failure:** treat absolute profit levels as `data gap`; no adoption; request the replication package.
4. **F4 — Ex-ante risk-threshold gate.** Fix `q` using data no later than 2022 (e.g. `q = 0.3`, matching the source's own risk-averse illustration) and re-run 2023–2024 untouched. *Failure rule:* MS-ave ≤ ARX-s in **either** market → the abstention channel is dead. **Action on failure:** drop the stopping rule from the hypothesis and re-test the median-argmax alone.
5. **F5 — Point-forecast superiority gate (the core claim).** Under Cost = 40 EUR/MWh with all parameters frozen, MS-ave must beat ARX-s in **both** markets. *Failure rule:* advantage ≤ 0 percentage points of Oracle in either market. **Action on failure:** record the claim as falsified; keep only the forecasting record.
6. **F6 — Cost-ladder gate.** Re-run at Cost ∈ {0, 10, 20, 40, 60} EUR/MWh. *Failure rule (research-defined):* MS-ave's advantage over ARX-s is positive at fewer than **3 of 5** cost levels in either market, i.e. the result is an artefact of the single 40 EUR/MWh setting. **Action on failure:** treat the effect as cost-tuned, not mechanism-driven.
7. **F7 — Cost-completeness ladder.** Add research-proposed frictions the source omits: imbalance/balancing penalties, day-ahead bid-ask/curtailment, degradation (per-cycle), and revenue-side fees, each at 0 / 5 / 10 / 20 EUR/MWh. *Failure rule:* MS-ave's advantage ≤ 0 under any "realistic" middle setting. **Action on failure:** mark non-tradable under realistic costs.
8. **F8 — Frozen forward window.** Extend the identical pipeline past 2024 (2025 data, no re-selection of `q`, no re-selection of methods). *Failure rule:* MS-ave < ARX-s in either market over the new window. **Action on failure:** treat the 2022–2024 result as regime-bound (energy-crisis sample).
9. **F9 — Third-market replication.** Repeat on a third day-ahead market (e.g. France or the Netherlands). *Failure rule (research-defined):* fewer than **2 of 3** markets show a positive frozen MS-ave-vs-ARX-s gap at Cost = 40. **Action on failure:** restrict the claim to the two paper markets.
10. **F10 — Calibration gate (price forecasts, Table 2).** PICP95 must sit within **±1.5 pp** of 95% and the Kupiec non-rejection share must be **≥80%** of hours in each market. *Status: PICP passes (MS-ave 94.29 DE, 94.18 ES); **Kupiec passes in Germany (91.67%) but fails in Spain (75.00%)**. For the profit forecasts (Table 3) the source prints PICP only — MS-ave 94.71 / 94.70 (DE) and 95.53 / 94.95 (ES), all within ±1.5 pp — and **no Kupiec test**, so that half of the gate is `data gap`.* **Action on failure:** recalibration is forbidden under the no-retuning rule — record as a failed gate and demote the calibration claim.
11. **F11 — Distribution-accuracy ablation.** MS-ave must hold the **lowest CRPS99 of all seven methods in both markets**. *Status: **currently failing in Germany** (QRM-ave 16.231 < MS-ave 16.421), already disclosed by the source; MS-ave does hold the lowest CRPS20 and (in Spain) ES.* **Action on failure:** narrow the accuracy claim to tail-focused CRPS and Spain-wide ES.
12. **F12 — Cross-hour-dependence placebo.** Compare (a) MS-ave, (b) the same ensemble with the 24 residual vectors shuffled hour-wise across days (destroying within-day dependence), (c) QRM (explicit independence), (d) a time-shuffled-calendar placebo. *Failure rule:* if (a) does not beat (b) on frozen profit and `VaR5%`, the gain is generic ensemble smoothing, not dependence information. **Action on failure:** reject the dependence mechanism.
13. **F13 — Economic-significance floor.** MS-ave's frozen advantage over ARX-s must be **≥1 percentage point of the Oracle total in each market** over ≥3 years (research-defined). *Current status: DE 2.46 pp, ES 5.54 pp — passes only before F2–F4 are cleared.* **Action on failure:** treat the effect as economically immaterial even if statistically consistent.
14. **F14 — Multiple-testing honesty gate.** Recompute the "best method" ranking under a family-wise correction across methods × markets × cost × `q`. *Failure rule:* MS-ave is no longer top-ranked in ≥1 market after correction. **Action on failure:** report the ranking as exploratory only.

Overall action on failure of any gate: the record stays `research-only` / `not-implemented` / `not-approved`; negative evidence is appended here; nothing is promoted.

## Crypto portability

**adapted** — the source demonstrates the mechanism only in European day-ahead electricity and contains **no crypto evidence** (`crypto 0`, `bitcoin 0`, `ethereum 0`, `perpetual 0`, `binance 0`, `usdt 0` occurrences). This is a **ported hypothesis**, not crypto empirical evidence.

- **What ports:** the decision logic — build a *joint* distribution over the session's price vector, push it through a P&L function, act on the median, and abstain when `prob(loss) ≥ q`. The analogous crypto object would be a round-trip of an inventory-carrying position inside a session, where `Cost` maps to taker fees + spread + slippage + funding paid over the window and `η` maps to the round-trip friction factor.
- **What does not port directly:** a physical 1 MWh battery with C-rate 1 and one cycle per day; ENTSO-E / TSO load-and-renewable features; coal and gas futures as exogenous drivers; the day-ahead auction gate (crypto has no single daily clearing auction).
- **Crypto-specific risks:** 24/7 sessions and candle-boundary conventions (no auction close), venue fragmentation and per-venue settlement, funding as a path-dependent carry cost (absent from the source entirely), mark/index vs last-price divergence, far higher data-vintage and contract-survivorship risk, and thin or absent grid-fee analogues so the single modelled cost term would have to be rebuilt from scratch.
- **Economic viability in crypto: `unproven`.** No crypto run of this mechanism exists in our stack; portability must not be read as authorization to trade.

## Limitations

- `underspecified`: numeric `η`; numeric `N`; timezone/DST and hourly boundary convention; the exact base over which `Cost` is charged and whether any revenue-side fee applies; TSO-forecast vintages and ENTSO-E revision handling; missing-data treatment; `q*` selection protocol beyond "maximizes profits".
- `data gap`: absolute strategy P&L in EUR (only Oracle totals printed); Sharpe / CAGR / drawdown / win rate / turnover / capacity (all absent from the source); bid-ask, slippage, impact, latency, fill, imbalance, degradation, financing, borrow (absent, not zero); code and data-availability statements.
- `not independently reproduced`: all source-reported numbers; only internal arithmetic consistency was checked.
- `unproven`: crypto portability; generalization beyond two markets, one battery size and the 2022–2024 regime; superiority over a strengthened point-forecast backbone.
- Identification: the design isolates the probabilistic decision layer against a *shared* ARX backbone (a clean ablation), but `q*` is selected ex-post, seven methods are compared without correction, and the headline claim is written in an ambiguous unit (recorded as a contradiction).
- Source quality: unrefereed preprint, no journal reference, unreconciled provenance metadata; funding and AI-use declarations present.
- Publication-bias concern: the paper reports its own proposed method's win; the one place it loses (German CRPS99 vs QRM-ave) is disclosed but the abstract's "generally outperforms … PICP, CRPS and ES" is broader than the tables support for PICP in Germany (MS 95.43 is closer to nominal than MS-ave 94.29).
- Incremental-write rule: a future run must **update** this record rather than create a sibling if the same source identity is re-encountered; a new record requires a materially different mechanism, signal construction, universe, horizon, or material data dependency.

## Implementation status

`not-implemented`. Nothing from this record has been implemented in our research stack: **no code written, no ENTSO-E or Investing.com data downloaded, no forecast fitted, no backtest run, no Paper / Testnet / Live activity, no Qlib full backtest, no production card, no candidate-pool entry.** The 55 arithmetic checks are provenance/consistency assertions on the pinned PDF and abs page only. Implementation authorization is a separate, explicitly reviewed decision.

## Adoption boundary

This record is **research material only**. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`, and `contested: true` with the two contradictions above. No wording, table count, or gate count in this record promotes it.

## Related Wiki records

No stable Hermes Wiki Brain page was found for this mechanism in this run (`kb_search "day-ahead electricity price forecasting battery arbitrage"` → 0 results; `kb_search "electricity"` → 4 results, none on storage arbitrage or probabilistic profit forecasting). **No Wiki link is asserted.**

Materially related records **in this repository** (different source identities; see the four-axis distinction in Provenance):

- `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md`
- `european-cross-border-day-ahead-power-spread-mean-reversion-2026-09-23.md`
- `eex-peak-baseload-forward-spread-risk-premium-matrix-har-rcv-2026-09-24.md`
- `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22.md`

## Sources

1. Tomasz Weron, Katarzyna Maciejowska. "From electricity prices to profits: multidimensional probabilistic forecasting for BESS trading." arXiv preprint `arXiv:2608.26122v1 [q-fin.ST]`, submitted 20 June 2026. Stable URL: https://arxiv.org/abs/2608.26122 · DOI: https://doi.org/10.48550/arXiv.2608.26122 · Full text read for this record: https://arxiv.org/pdf/2608.26122v1 (891,772 bytes, sha256 `919d484347c39cc360ba4977da724704476a0da2d7aac01b8a19620908664c72`, 26 pages, 68,560 characters read end to end) · abs page https://arxiv.org/abs/2608.26122 (41,117 bytes, sha256 `78b433951380ed553918642745cbaeccb26c3c2593fe05058e4f63c07c1e6928`) · Licence CC BY 4.0. All quantitative claims above trace to Tables 1–5, Eqs. (1)–(17) and Sections 2–6 of that pinned v1 and are labelled source-reported.
2. arXiv API record `id_list=2608.26122` (read 2026-09-30) for `<published>2026-06-20T14:36:04Z` and `<updated>2026-09-30T04:25:57Z`.
3. Data vendors named by source 1 (used by it, not by us; **not** independently fetched): ENTSO-E Transparency Platform (https://transparency.entsoe.eu) and Investing.com (coal API2, gas TTF).
4. Works cited *inside* source 1 (attributed to its literature review, not independently read): Maciejowska & Nitka (2026), *Operations Research and Decisions* 36 — origin of the Multiple Split method; Hirsch & Ziel (2026), arXiv:2604.19580; Hubicka, Marcjasz & Weron (2019), *IEEE Trans. Sustainable Energy* 10, 321–323; Serafin, Uniejewski & Weron (2019), *Energies* 12, 256; Nowotarski & Weron (2018); Marcjasz, Uniejewski & Weron (2020); Lago, Marcjasz, De Schutter & Weron (2021); Kath & Ziel (2021); Barber et al. (2021); Lei et al. (2018); Gneiting et al. (2007, 2008); Kupiec (1995); Koenker & Hallock (2001); Liu et al. (2017); Janczura & Wójcik (2022); Billé et al. (2023); Marcjasz et al. (2018, 2023); Maciejowska (2022); Maciejowska, Serafin & Uniejewski (2024); Uniejewski & Maciejowska (2022); Uniejewski & Weron (2021); Pinson (2013); Kumbartzky et al. (2017); IEA (2026); EIA (2023).
