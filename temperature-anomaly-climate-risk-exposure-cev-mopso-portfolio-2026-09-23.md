---
schema: strategy-research-record-v1
title: Temperature-Anomaly CRE/CEV Climate-Aware Long-Only MOPSO Equity Portfolio (arXiv 2604.11143)
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-04-13
sources:
  - https://arxiv.org/abs/2604.11143
  - https://arxiv.org/html/2604.11143v1
  - https://doi.org/10.48550/arXiv.2604.11143
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Temperature-Anomaly CRE/CEV Climate-Aware Long-Only MOPSO Equity Portfolio (arXiv 2604.11143)

## Provenance

- **Primary source:** Michele Azzone (corresponding author, Department of Mathematics, Politecnico di Milano), Carlo Bechi (Department of Mathematics, Politecnico di Milano), Gabriele Sbaiz (Department of Economics, Business, Mathematics and Statistics, University of Trieste), "Temperature Anomalies and Climate Physical Risk in Portfolio Construction," `arXiv:2604.11143v1 [q-fin.PM]` (cross-list q-fin.RM per API), submitted **13 Apr 2026, 08:00:49 UTC**, v1 only (no v2 as of read date). Author list copied exactly as the primary source; all three authors verified on the landing page and the v1 HTML (`source-reported`).
- **URLs (stable):** https://arxiv.org/abs/2604.11143 · full text https://arxiv.org/html/2604.11143v1 · DOI https://doi.org/10.48550/arXiv.2604.11143 (arXiv DataCite DOI shown on landing page). License on HTML: CC Zero.
- **Primary-source checksum (performed 2026-09-23 by direct read of the arXiv landing page and the complete v1 HTML, sections §1–§6 + Appendices A–C + Tables 1–10 + Figures 1–12):** (a) authors = the three above, exact order; (b) version/date = v1, 13 Apr 2026; (c) sample periods = temperature data Jan 1940–Apr 2025 (portfolio-selection probability model trained on 1940–2019), return regression 2004–2025, backtest Jan 2020–Apr 2025 with rolling input window starting Jan 2015; (d) universe = MSCI World constituents for the sector regression (sectors present at beginning of 2020 and 2025, banks/financials/insurance excluded) and a stratified **120-stock** MSCI World subsample for optimization (NA 45%/54, Europe 25%/30, Asia 25%/30, Oceania 5%/6, Table 4); (e) transaction-cost treatment = **explicitly not modeled** — §5 states verbatim that "this backtest does not account for transaction costs, bid-ask spreads, and in general rebalancing costs" (all performance figures are therefore gross); (f) core performance numbers = Table 9 (below), each cited to its table; (g) publication status = **arXiv preprint**. The v1 HTML header renders "Journal: European Journal of Operational Research" (manuscript journal metadata), but the arXiv landing page shows **no Journal reference and no non-arXiv DOI** as of 2026-09-23 → peer-review/acceptance status is `not stated in source` and is **not** treated as published.
- **Data sources named by the paper:** monthly mean temperature from Our World in Data (sourced to IPCC, NASA, World Bank); MSCI World constituents/sector returns; firm fundamentals (tangible assets, revenue, continent revenue split).
- **Deduplication audit (pre-write, entire repository, not `git log`):** ripgrep across all `*.md` + `coverage_manifest.csv` for `2604.11143`, `10.48550/arXiv.2604.11143`, exact title "Temperature Anomalies and Climate Physical Risk in Portfolio Construction", `Azzone`, `Climate Risk Exposure`, `Climate Exposure Volatility`, `temperature anomal`, `MOPSO`, `Gabriele Sbaiz` → the only `Azzone` hit is an unrelated citation of **Azzone & Baviera (2021)** synthetic-forwards work in `option-funding-basis-year-end-boundary-wedge-spx-rut-box-implied-2026-09-22.md` (different paper, different mechanism); `Politecnico` hits are other authors' records; every other probe = **0 hits** → source identity genuinely new.

## Economic mechanism

### Source-reported

- Extreme positive temperature anomalies (standardized monthly anomaly Z > 2 against a 1960–1990 continent-month baseline, i.e. ≈ top 2.28% Gaussian tail) are treated as proxies for physical climate events (heatwaves, wildfires, droughts, storms). A panel regression of MSCI World sector excess returns on those anomaly indicators (market-adjusted, HAC/Newey–West SEs, 2004–2025) finds **17 of 23 sectors** significantly affected in at least one continent, with γ almost always negative (§2.4, Table 2); a continent-FE + month-FE panel gives Γ = **−0.003, p = 0.0096** (Eq. 10). Stated economic channel: operational downtime, supply-chain bottlenecks, damage/degradation of temperature-sensitive physical inventories and assets (citing Starr 2000; Zivin & Neidell 2014; Neidell et al. 2021).
- Anomaly probability p(k,t) per continent is modeled as a logistic regression with linear + quadratic time trend (Eq. 3), so the risk input is explicitly **forward-looking and non-stationary** (Table 1 AUROC 0.8380 Europe – 0.9396 Africa; AUPR well above random for all six continents).
- Two portfolio-level metrics are built: **Climate Risk Exposure** CRE(w,t) = Σ αk(w)·p(k,t) (Eq. 13, expected exposure) and **Climate Exposure Volatility** CEV(w,t) = Var(Σ αk·Bk,t) (Eqs. 14–16, includes cross-continent anomaly correlation ρkj), where αk are "climate-normalized" weights combining portfolio weights, firm **asset intensity** AI = tangible assets/revenue (Real Estate ≈10.6, Retailers ≈0.6) and continent revenue shares S(i,k) (§3.1, Eqs. 11–12).
- These enter a **three-objective** optimization (maximize expected return, minimize market variance, minimize CEV) solved by Multi-Objective Particle Swarm Optimization over a long-only, fully invested 120-asset universe (Eqs. 19a–c; no risk-free allocation, no shorting). The Pareto front is then scalarized with convex weights (a,b,c) to pick the traded portfolio (Table 8).

### Research interpretation

- Hypothesized mechanism (falsifiable): **physical-asset-geography risk channel** — firms whose revenues and tangible assets concentrate in regions with rising probability of temperature extremes carry a time-varying, partially diversifiable tail exposure; tilting away from that exposure (a) reduces realized climate-linked return damage and (b) because anomaly events are only moderately correlated across continents (Pearson 0–0.48, §2.2), geographic reweighting can improve the risk profile without necessarily sacrificing return. The α-source claim is a **risk-pricing/tilt** channel, not a directional forecast: the paper's own γ are contemporaneous monthly effects, and its tradable object is a monthly long-only re-optimized portfolio.
- Roles of components: **Regime/risk input:** time-varying continent anomaly probabilities p(k,t) (logistic trend fit). **Risk metric:** CEV (geographic concentration + correlation of exposure). **Primary signal:** the Pareto-front portfolio produced each month from (expected return, variance, CEV). **Confirmation:** sector γ-significance evidence that the climate channel is priced at all. **Execution/exit:** monthly re-optimization on the first business day replaces weights (no separate exit rule in source).
- This is a ported traditional-equity hypothesis; nothing in the source tests crypto. All thresholds/filters below that the source does not state are labeled `research-proposed`; all failure cutoffs are `research-defined`.

## Signal

All of the following is `source-reported` unless marked otherwise.

- **Formation timestamp:** first business day of each month; inputs use (i) trailing 5-year monthly-mean returns, (ii) trailing 5-year daily-return covariance with Ledoit–Wolf shrinkage, (iii) anomaly probabilities updated with the **most recently completed month's** temperature data (§5). Timezone/session convention for "first business day" is `underspecified` in the source.
- **Lookback:** 5-year rolling window for μ and Σ; temperature baseline 1960–1990 for anomaly standardization; probability model trained 1940–2019 for the portfolio-selection use (similar fit to 1940–2025 shown in Figure 2). Endpoints inclusive/exclusive: `not stated in source`.
- **Entry:** at the monthly re-optimization, buy the MOPSO-selected weight vector (long-only, Σw = 1, wi ≥ 0, Eqs. 19b–c). Selection among Pareto portfolios = minimum of a min-max-normalized convex combination of the three objectives with (a,b,c) from Table 8: Balanced (1/3,1/3,1/3), Minimum Risk (0,1/2,1/2), Return-oriented (1/2,1/4,1/4), Variance-oriented (1/4,1/2,1/4), Climate-oriented (1/4,1/4,1/2), Mean-Variance (1/2,1/2,0). Which scalarization is "the" strategy is a **strategy choice among six source-specified variants**; the paper reports all six.
- **Exit / holding period:** hold to month end; weights replaced at next month's first business day (no stop-loss, no take-profit, no overlay in source).
- **Parameters (source-fixed):** anomaly threshold Z = 2; logistic trend β0+β1t+β2t²; 6 continents (Antarctica excluded); N = 120 stocks; MOPSO **Iter = 300, N_rep = 400, N_pop = 500** (chosen in §4.3 after grid over Iter∈{200,300,400}, N_pop∈{200,500,600}, N_rep∈{100,200,400}, averaged over 10 runs); Ledoit–Wolf shrinkage targeting Σ condition number < 1,000; runtime 217.39 s per month.
- **Position sizing:** exactly the optimizer weights; no leverage, no cash, no risk-free leg (source), no per-name cap stated (`underspecified`; any cap such as wi ≤ 10% would be `research-proposed`).
- **Order timing / price / tie handling:** `underspecified` — the source states monthly rebalance then month-end evaluation but gives no order type, execution price, or partial-fill rule. Any concrete rule (e.g., VWAP at the open of the first business day) is `research-proposed`.
- **Reproducibility caveat:** the **exact list of the 120 tickers is not disclosed** (`data gap`); the sector-regression constituent set is likewise described only by selection criteria. A fully independent reconstruction therefore requires a `research-proposed` re-derivation of the stratified sample (mcap × HQ region per Table 4).

## Required data

- **Instrument/universe:** global developed large/mid-cap equities (MSCI World); optimization subset of 120 names stratified by market cap and HQ region (Table 4); sector regression uses MSCI World sector aggregates excluding banks/financials/insurance (`source-reported`).
- **Venue/vendor:** index/constituent and return data vendor for MSCI World is `not stated in source` (`data gap`).
- **Market type:** listed equity spot (no derivatives, no crypto).
- **Timeframe:** monthly anomaly/return series; **daily** returns used for the covariance estimate; monthly rebalance.
- **Fields:** monthly mean temperature per continent (1940–2025); monthly risk-free rate; market index total return; sector total returns (dividends/splits/corporate actions included); firm tangible assets, revenue, revenue-by-continent shares; market caps; HQ country.
- **Point-in-time:** anomaly probability uses only the month preceding the rebalance date (`source-reported`); **publication lag of fundamentals (AI, S_ik) and their vintage is `not stated in source` → point-in-time safety is `data gap`, must be audited before any use.**
- **Timestamp/timezone:** `underspecified` (no timezone or calendar convention given beyond "first business day").
- **Missing data:** firms are required to have "sufficient available data"; imputation rules `not stated in source` (`data gap`).
- **Costs:** maker/taker fees, spread, slippage, borrow: **observed = no, modeled = no, omitted = yes** (explicit source admission, §5).

## Execution assumptions

- **Source-reported:** monthly full re-optimization on the first business day; month-end performance evaluation; long-only, fully invested, no short selling, no risk-free asset (Eqs. 19b–c); Ledoit–Wolf shrinkage on Σ; MOPSO hyperparameters as above; **no transaction costs, no bid-ask spread, no rebalancing cost in the backtest** (explicit §5 statement — performance must be read as gross-of-trading-costs).
- **`not stated in source` / `underspecified`:** order type, fill model, execution price, latency, participation/capacity limits, turnover magnitude, borrow (n/a long-only), partial fills, corporate-action handling inside the backtest window, fee schedule, data-vendor latency.
- **Scout note (`research-proposed`):** a monthly 120-name long-only MOPSO re-solve typically produces non-trivial turnover; with zero modeled costs, net-of-cost viability is untested by the source. Any fill/latency/cost assumption we add later must be labeled `research-proposed`, not attributed to the paper.

## Evidence

### Source-reported

All figures below are third-party, source-reported, read directly from `arXiv:2604.11143v1` HTML on 2026-09-23; **none independently reproduced**.

- **Channel evidence (2004–2025, MSCI World sector aggregates, HAC SEs, market-adjusted):** 17/23 sectors significant at p<0.1 in ≥1 continent; γ negative with one exception. Table 2 examples: Applied Resources–North America **−0.0140 (p=0.001)**, Industrial & Commercial Services–Asia **−0.0139 (p<0.001)**, Mineral Resources–Asia **−0.0148 (p=0.011)**, Food & Beverages–North America **−0.0095 (p=0.006)**; the single positive significant pair is Industrial & Commercial Services–South America **+0.0068 (p=0.058)**. Table 3 (continent + month FE): Chemicals **−0.0062 (0.0014)**, Energy-Fossil Fuels **−0.0089 (0.0399)**, Food & Beverages **−0.0050 (0.0070)**, Real Estate **−0.0055 (0.0121)**, Retailers **−0.0026 (0.0811)**, Telecommunications **−0.0042 (0.0718)**, Transportation **−0.0032 (0.0893)**, and **Software & IT Services +0.0026 (0.0609)** (positive, physical-exposure exception the authors attribute to minimal physical footprint pre-datacenter expansion). Pooled Eq. 10: **Γ = −0.003, p = 0.0096**.
- **Probability model (Table 1):** AUROC Africa 0.9396, Asia 0.9067, North America 0.8947, Oceania 0.8830, South America 0.8754, Europe 0.8380; AUPR 0.8031/0.7312/0.6100/0.3215/0.5227/0.3776 vs random 0.2060/0.2225/0.1429/0.0564/0.1341/0.0943.
- **Anomaly correlations:** all Pearson coefficients positive, range 0–0.48 (§2.2, Figure 3); Fréchet–Hoeffding admissibility verified (§2.3).
- **Backtest, Jan 2020 – Apr 2025, rf assumed 0 for Sharpe/Sortino (Table 9; CAGR / Sharpe / Sortino / MaxDD / r-CRE / r-CEV):**
  - Market-Cap Weights: **15.75% / 1.041 / 1.850 / 14.78% / 0.714 / 10.64%**
  - Equally-Weighted: **17.49% / 1.153 / 1.834 / 16.72% / 0.724 / 10.96%**
  - Min Market Variance: **14.20% / 1.282 / 2.324 / 11.47% / 0.762 / 13.56%**
  - Min CEV: **16.68% / 0.739 / 1.207 / 43.48% / 0.710 / 10.50%**
  - Max Expected Return: **3.32% / 0.320 / 0.674 / 69.37% / 0.695 / 11.87%**
  - Balanced (1/3,1/3,1/3): **33.54% / 1.153 / 2.787 / 31.54% / 0.721 / 10.48%**
  - Minimum Risk (0,1/2,1/2): **14.65% / 1.133 / 1.304 / 17.38% / 0.716 / 11.18%**
  - Return-oriented (1/2,1/4,1/4): **28.43% / 0.920 / 2.077 / 46.10% / 0.727 / 10.51%**
  - Variance-oriented (1/4,1/2,1/4): **30.57% / 1.312 / 3.029 / 20.78% / 0.723 / 10.78%**
  - Climate-oriented (1/4,1/4,1/2): **28.47% / 1.045 / 2.382 / 30.57% / 0.716 / 10.70%**
  - Mean-Variance (1/2,1/2,0): **33.35% / 1.136 / 2.356 / 32.81% / 0.698 / 10.77%**
  - **All of the above are gross of transaction costs, spreads and rebalancing costs (explicit §5 statement).** The authors themselves flag ~30% CAGRs as not net-realistic.
- **CEV dynamics:** CEV trends downward from ~2010 because Bernoulli variance p(1−p) falls once p > 0.5 — i.e., measured "volatility" drops precisely as anomalies become more certain (§3.1 discussion of Figure 5); higher cross-continent correlation materially raises CEV (Figure 6).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Source's own cost admission (§5):** the entire Table 9 is gross; with monthly full re-optimization of 120 names, unspecified turnover means the ~30% CAGR variants have an untested path to net performance. `source-reported`
- **Climate-only optimization fails on risk:** Min CEV Sharpe **0.739** with MaxDD **43.48%** — worse Sharpe than both benchmarks and near-worst drawdown; the paper's climate objective alone is not a viable portfolio rule. `source-reported`
- **Return-oriented scalarization fails:** (1/2,1/4,1/4) MaxDD 46.10%, Sharpe 0.920; Max Expected Return portfolio Sharpe 0.320, MaxDD 69.37%. `source-reported`
- **Min market variance underperforms benchmarks on CAGR** (14.20% vs 15.75%/17.49%) — the risk reduction is not free. `source-reported`
- **CEV metric paradox (source's own explanation):** post-2010 CEV declines while expected anomaly frequency rises (p>0.5 branch of Bernoulli variance) → CEV as a de-risk trigger can move the wrong way exactly in the worst climate regime. `source-reported`
- **Statistical-power/multiplicity:** significance is declared at **p<0.1** across a 23-sector × 6-continent grid (Table 2 reports only significant cells); the source reports **no multiple-testing correction** for §2.4 (`not stated in source`) — `research interpretation`: family-wise/FDR control could materially shrink the 17/23 count.
- **Sample window:** tradable backtest is only **64 months** (Jan 2020–Apr 2025) covering COVID + 2022 energy shock; rolling inputs start 2015; no pre-2020 out-of-sample portfolio test, no deflated-Sharpe/selection-bias adjustment (`data gap`).
- **Selection/survivorship concern (`research interpretation`):** the regression sample conditions on being an MSCI World constituent at the beginning of **both** 2020 and 2025, which still conditions on survival through part of the studied window, despite the source describing the criterion as bias-mitigating. `source-reported` = the criterion and its stated rationale; the critique = research interpretation.
- **Universe truncation:** optimization runs on 120 names (vs ~800 MSCI World) chosen by an undisclosed stratified rule — representativeness and index-proxy fidelity untested (`data gap`).
- **No point-in-time fundamentals audit** for AI/S_ik; zero rf in Sharpe/Sortino inflates headline ratios relative to any positive-rf convention. `data gap` / `source-reported`

## Falsification plan

Each item: data / sample / metric / threshold / action. Thresholds are **`research-defined`**; any rule we invent is **`research-proposed`**. None of these are claimed by the source.

1. **Cost stress (the gating test).** Data: 120-stock monthly weights, one-way cost 5/10/20 bp. Metric: net Sharpe of Variance-oriented (1/4,1/2,1/4) vs net market-cap benchmark, Jan 2020–Apr 2025 + extension. Fail if at **10 bp** net Sharpe ≤ benchmark net Sharpe **−0.10**, or at **20 bp** net Sharpe ≤ **0.50**. Action: reject tradability, keep only as research material. (`research-defined` threshold; cost grid `research-proposed`)
2. **Turnover audit.** Metric: annualized one-way turnover of each Table 8 variant. Fail if annual turnover > **200%** for any "superior" variant (Balanced / Variance-oriented). Action: reclassify headline CAGR as unreachable net. (`research-defined`)
3. **Placebo on the climate channel.** Data: sector-month panel 2004–2025. Metric: distribution of γ under 500 block-shuffled B(k,t) series. Fail if the true |Γ| (−0.003) does not exceed the **95th percentile** of the placebo |Γ| distribution, or if fewer than **8 of the 17** significant sectors stay outside the placebo 90% band. Action: treat the channel as spurious. (`research-defined`)
4. **Multiple-testing control.** Metric: Benjamini–Hochberg FDR at 5% across the full 23×6 sector×continent family. Fail if fewer than **5** sector-continent pairs survive FDR 5% **and** the pooled Γ loses p<0.05. Action: downgrade mechanism confidence to low. (`research-defined`)
5. **Ablation of the CEV objective.** Data: same pipeline with CEV removed (pure mean-variance MOPSO, identical hyperparameters). Fail if removing CEV changes realized r-CEV by <**10%** while Sharpe/MaxDD differences are within ±0.10 — i.e., the climate objective does nothing — or if the climate objective is what *causes* the Min-CEV portfolio's 43% drawdown in every configuration. Action: mechanism is decorative or harmful. (`research-defined`)
6. **Algorithm-vs-objective control.** Run plain convex mean-variance + CEV solver (no PSO, same constraints) and compare. Fail if the Pareto-advantage reported for MOPSO disappears (Sharpe gap < 0.10) — then results are optimizer artifacts, not climate effects. (`research-defined`)
7. **Point-in-time leakage audit (binary).** Verify AI = tangible assets/revenue and S_ik revenue shares at rebalance t use only filings available by t, and that temperature data for month m are used only after m closes. Fail on **any** confirmed look-ahead. Action: invalidate the backtest. (`research-defined`)
8. **Pre-period out-of-sample extension.** Data: extend the portfolio backtest to Jan 2010–Dec 2019 (inputs 2005+). Fail if the Balanced and Variance-oriented variants' Sharpe falls **≤ 0.5** or below the equally-weighted benchmark in that decade. Action: treat 2020–2025 result as regime luck. (`research-defined`)
9. **Probability-model robustness.** Metric: re-fit p(k,t) on NASA/GISS or national agency series instead of Our World in Data; also refit with linear-only trend. Fail if mean AUROC drops below **0.70** for ≥2 continents or anomaly counts diverge >**25%**. Action: CEV input unreliable. (`research-defined`)
10. **CEV-regime sanity check.** Metric: joint path of CEV and realized anomaly frequency. Fail (structural falsification of CEV as a risk trigger) if CEV falls while realized frequency rises over ≥**3 consecutive years** in the test window — the Bernoulli-paradox failure mode the paper itself documents. Action: replace CEV with a monotone exposure metric before any use. (`research-defined`)
11. **Survivorship re-run.** Rebuild the sector panel with point-in-time index membership (entries/exits honored). Fail if pooled Γ sign flips or |Γ| shrinks >**50%**. Action: mechanism evidence collapses. (`research-defined`)
12. **Capacity (low risk, still checked).** 120 large-cap names, long-only, monthly: fail if a ±10% participation cap changes net Sharpe by >**0.15**. Action: capacity-limited. (`research-defined`)

## Crypto portability

**Label: `unproven`** (native crypto direct port does not exist).

- The mechanism is territorial physical-asset exposure: tangible assets, plant/refineries/warehouses, and continent revenue shares. **Native crypto assets have no such exposure channel** — no revenue geography, no asset intensity, no sectoral production to disrupt — so temperature anomalies do not map onto BTC/ETH returns through the source's identified channel. The source contains **zero crypto evidence**.
- The closest (`research-proposed`, untested) adaptations: (a) equity of mining/hosting/infrastructure companies (their own physical footprint and grid/geographic exposure), (b) venue/exchange or stablecoin-reserve **operational** risk by jurisdiction (custody, data-center, regulatory geography), (c) energy-price-mediated effects on miner economics. Each is a new hypothesis, not a port of the paper's result.
- Crypto-specific risks even for those adaptations: spot vs perpetual basis, funding, 24/7 sessions vs monthly "first business day" boundaries, venue fragmentation, index/mark price construction, listing/survivorship of infrastructure names, thin equity-like liquidity in tokens. Any crypto version requires re-deriving every threshold (`research-proposed`) and must not cite this paper as crypto evidence.

## Limitations

- `not independently reproduced` — every performance/statistical figure is source-reported from a single preprint read on 2026-09-23.
- Transaction costs, spreads, slippage, turnover, fees, fill model: **explicitly excluded by the source** (§5) → all returns are gross; no capacity, no latency analysis. `data gap`
- Peer-review status `not stated in source`: HTML carries "Journal: European Journal of Operational Research" manuscript metadata, the landing page carries no journal reference/DOI beyond the arXiv DataCite DOI. `underspecified`
- The 120-ticker list, data vendor, execution price, timezone/calendar convention, fundamentals vintages, and MOPSO random-seed handling: `underspecified` / `data gap`.
- Backtest = 64 months, long-only, rf = 0 in ratios, no deflated Sharpe / multiple-testing correction, significance at p<0.1, exact constituent sample undisclosed.
- CEV's Bernoulli-variance non-monotonicity (documented by the source itself) makes it unsafe as a stand-alone de-risk trigger.
- Confidence `medium` refers to confidence in this research **interpretation** of the source, not to profitability or validation.

## Implementation status

`implementation_status: not-implemented`. No part of this pipeline exists in our research stack: no MOPSO re-solve, no CRE/CEV computation, no backtest, no Qlib run, no Paper/Testnet/Live activity. This record is a normalized research capture only, and does not modify or authorize any runtime.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review · entered Hermes Wiki Brain · entered the production candidate pool · completed Qlib full-backtest validation · became a frozen survivor or leaderboard entry · profitable · validated alpha · approved for implementation, paper trading, testnet, or live trading. The source's own gross-cost, 64-month backtest is the strongest evidence attached, and it is third-party.

## Related Wiki records

No stable Hermes Wiki Brain page for this mechanism was verified in this run, and the Scout does not write to Wiki Brain, so **no Wiki links are asserted** (`data gap`, not fabricated). Adjacent repository records (filenames only, not Wiki pages):

- `climate-attention-global-warming-search-treasury-excess-return-predictor-2026-09-23` — climate-attention theme, but different channel (search attention → Treasury excess returns), different assets, different source.
- `coffee-commodity-weather-stress-lagged-overlay-2026-09-12` — weather stress overlay on a commodity; different mechanism (weather-driven commodity supply), different market.
- `kalshi-temperature-ladder-market-implied-forecast-public-nwp-lead-2026-09-22` — temperature as a **forecast market** input, not an equity-portfolio risk metric.
- `crypto-brown-esg-uncertainty-next-day-downside-liquidity-amplified-2026-09-03` — ESG/uncertainty tilt in crypto; adjacent "ESG/climate in portfolios" family, different mechanism and market.

## Sources

1. Azzone, M., Bechi, C., & Sbaiz, G. (2026). "Temperature Anomalies and Climate Physical Risk in Portfolio Construction." arXiv:2604.11143v1 [q-fin.PM], submitted 13 Apr 2026. https://arxiv.org/abs/2604.11143 · https://arxiv.org/html/2604.11143v1 · DOI 10.48550/arXiv.2604.11143. (Primary source; all `source-reported` claims, tables and figures above trace to §§1–6, Appendices A–C, Tables 1–10, Figures 1–12 of v1, read 2026-09-23.)
2. Supporting data providers named by the primary source (not separately consulted for claims): Our World in Data temperature series (sourced to IPCC/NASA/World Bank); MSCI World index constituent/return data (vendor unspecified in source).
