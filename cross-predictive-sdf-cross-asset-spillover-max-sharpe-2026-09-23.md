---
schema: strategy-research-record-v1
title: Cross-Predictive Stochastic Discount Factor with Cross-Asset Spillovers (Max-Sharpe Equity Strategy)
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - cross-sectional
  - cross-predictability
  - lead-lag
  - stochastic-discount-factor
  - max-sharpe
  - ridge-regularization
status: research-only
confidence: medium
source_as_of: 2026-02-24
sources:
  - "Doron Avramov and Xin He, 'Stochastic Discount Factors with Cross-Asset Spillovers', arXiv:2602.20856v1 [q-fin.CP], submitted 24 Feb 2026. https://arxiv.org/abs/2602.20856"
  - "https://arxiv.org/html/2602.20856v1 (full text read directly for this record, 2026-09-23)"
  - "https://doi.org/10.48550/arXiv.2602.20856"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Predictive Stochastic Discount Factor with Cross-Asset Spillovers (Max-Sharpe Equity Strategy)

## Provenance

- **Primary source:** Doron Avramov (Reichman University (IDC), Herzliya, Israel) and Xin He (University of Science and Technology of China), *"Stochastic Discount Factors with Cross-Asset Spillovers"*, arXiv preprint **arXiv:2602.20856v1 [q-fin.CP]**, submitted **24 February 2026** (landing-page version stamp read 2026-09-23: `arXiv:2602.20856v1 [q-fin.CP] 24 Feb 2026`). Paper states both authors contributed equally; research support acknowledged from Inquire Europe.
- Abstract: https://arxiv.org/abs/2602.20856
- Full text (HTML v1): https://arxiv.org/html/2602.20856v1 — opened and read directly for this record on 2026-09-23 (§1 Introduction, §2 Econometric Framework incl. §2.1 Trading Strategy and §2.2 Zero-Cost and Leverage Constraints, §3 Estimation incl. §3.1–§3.2, §4 Data incl. §4.1–§4.3, §5 Results incl. §5.1–§5.4, §6 Conclusion, Tables 1–9, Figure 1, Appendices A–F).
- Canonical DOI: https://doi.org/10.48550/arXiv.2602.20856
- **Publication status:** arXiv preprint, v1 only; the landing page carries **no journal reference and no DOI other than the arXiv DOI**; peer-review status is `not stated in source` (do not read as either reviewed or unreviewed).
- **Version/date integrity:** all empirical claims below are taken from the single pinned version v1 (24 Feb 2026). The HTML render carries an in-document date line of "August 24, 2026", which is a rendering artifact of the HTML build; the authoritative submission stamp is 24 Feb 2026.
- **Primary-source checksum performed:** author list, version/date, sample period, universe, cost treatment, core performance numbers and publication status were each verified against the primary full text listed above; fields that could not be verified are marked `data gap` / `underspecified` / `not stated in source` in the relevant section. No secondary summary, snippet or aggregator was used to fill any rule or number.
- **Deduplication search (2026-09-23, whole repository, not just `git log -20`):** ripgrep across all **866** existing `*.md` records **and** `coverage_manifest.csv` for `2602.20856`, the exact title `Stochastic Discount Factors with Cross-Asset Spillovers`, `Avramov`, `cross-predictive`, `cross-prediction`, `Stochastic Discount Factor`, `principal portfolio`, `connection matrix`, `Jensen et al. (2023)` → **zero records for this source identity**; only one adjacent cross-predictability record exists (crypto seesaw lead-lag, different source and different mechanism — see *Related Wiki records*).

## Economic mechanism

### Source-reported

The authors propose a unified framework that links firm-level predictive signals, cross-asset spillovers, and the stochastic discount factor (SDF):

1. **Signal aggregation vector Λ** assigns weights to M firm-level characteristics; **connection (spillover) matrix Ψ** encodes how asset *i*'s signals forecast asset *j*'s returns (diagonal = self-prediction, off-diagonal = cross-prediction). Portfolio weights are `ω_t' = Λ' S_t' Ψ` (Eq. 1), with cross-sectionally standardized signals (`S_t` columns mean 0, sd 1).
2. Λ and Ψ are **jointly estimated by maximizing the squared Sharpe ratio**, implemented as Britten-Jones (1999)-style regressions with a shared ridge penalty λ chosen by **five-fold cross-validation** (§3.2, Eqs. 21–25, Appendices D–E). Expected-return maximization (MR, SVD of the managed-portfolio matrix Π, §3.1) is retained only as a benchmark.
3. The realized return of the max-Sharpe strategy is proportional to an SDF — a single factor that prices the cross-section (Eq. 10; Hansen–Jagannathan / Cochrane / Back). The paper notes its Sharpe-maximizing strategy "excludes alpha, by construction, consistent with the SDF interpretation" (§2.1 remark 6).
4. **Economic channels claimed:** staggered information diffusion, peer/industry/supply-chain links, and correlated institutional trading produce lead–lag cross-predictability; empirically the average **absolute off-diagonal Ψ entry exceeds the average absolute diagonal entry** (toy example: 0.0805 vs 0.0068, Table 2 Panel A), i.e. cross-asset linkages carry more information than self-predictive signals.
5. Diebold–Yılmaz (2014)-style row/column aggregation of Ψ shows **large, low-turnover firms are net transmitters** of predictive signal and smaller, high-turnover, value/profitable/low-investment firms are net receivers (§5.4, Table 9). Highest-|λ| signals cluster in investment, value and profitability themes; return-based signals (momentum, short-term reversal, seasonality) get persistently low weights (§5.3, Table 8).
6. Post-2000 attenuation is attributed by the authors to wider anomaly adoption, higher liquidity and passive-ETF growth, mirroring Green et al. (2017) (§1, §5.2.4).

### Research interpretation

Falsifiable hypothesis: **cross-sectional characteristics contain cross-asset lead–lag content that adds out-of-sample risk-adjusted performance beyond self-predictive SDF estimation**, and this increment survives cost stress and factor spanning.

Component roles (Scout-normalized):

```text
Regime: none — the framework is unconditional by design (Hansen–Richard unconditional optimization; §1)
Primary signal: monthly cross-sectionally standardized characteristic matrix S_t (138 signals)
Signal aggregation: ridge-estimated Λ (weights on characteristics)
Cross-asset layer: ridge-estimated Ψ (off-diagonal lead-lag spillovers); self-prediction benchmark = Ψ diagonal only
Portfolio construction: zero-cost projection Θ (Eq. 11–12) + rescale to total leverage 2
Risk/exit: none specified beyond monthly re-estimation (no stop, no drawdown rule in source)
```

Ablation requirement: any performance gain that survives zeroing the off-diagonals of Ψ would falsify the *spillover* mechanism and re-attribute the result to signal aggregation alone.

## Signal

- **Formation timestamp:** monthly frequency. Signals are observed at time *t* and returns realized at *s > t* (§2, Eq. 2 defines managed-portfolio returns with `s > t`). The exact calendar formation/rebalance day, session convention and timezone are `underspecified` in the source (CRSP monthly data; no intraday timing exists in this design).
- **Lookback / estimation window:** rolling **120 months** (10 years) of the most recent observations, re-estimated **every month** (§4: "Out-of-sample evaluation begins in February 1973, with estimation windows based on rolling samples of the most recent 120 monthly observations"). Endpoint inclusion convention `underspecified`. Warm-up: 1963-01 → 1973-01 estimation history before the first OOS month.
- **Signal construction:** each of the M = 138 characteristics is standardized to mean 0 / sd 1 (§4.1). Weights: `ω_t' = Λ' S_t' Ψ` (Eq. 1), then zero-cost projection `ω_t' = Λ' S_t' Θ`, `Θ = I_N − (1/N)A` (Eq. 11–12), then **rescaled so total portfolio leverage = 2** (§2.2).
- **Estimation:** alternating ridge regressions for Λ (Eq. 22) and Φ = vec(Ψ') (Eq. 25), unit-norm constraints Λ'Λ = 1, Φ'Φ = 1 (Eq. 4), shared ridge parameter λ selected by **five-fold cross-validation, re-selected over time** (§3.2, Appendix E). A robustness variant `MS BiSort fixed` uses fixed **λ = 1**, "the most frequently selected value" (§5.2.4).
- **Long entry / short entry:** long the assets with positive ω and short those with negative ω across the test-asset universe; the construction is dollar-neutral by the zero-cost constraint with gross leverage 2 (long ≈ 1, short ≈ 1). Ties / simultaneous signals: not addressed in source → `not stated in source`.
- **Exit / holding period / re-entry:** monthly portfolio re-formation implies a one-month holding period with full re-estimation each month; no stop, take-profit, or overlay rule exists in the source. Any threshold, filter, or stop beyond this is **research-proposed** (none added here).
- **Parameters:** M = 138 signals (of the original 153 in Jensen et al. (2023), 15 that begin after 1963 are excluded); N = 138 (univariate spread-portfolio universe) or N = 544 (bivariate size×signal universe); toy example M = 5, N = 9 (3×3 ME×BM sorts) with characteristics ME, BM, OP, INV, MOM. λ is **CV-tuned (fixed vs tuned explicitly distinguished)**; λ = 1 fixed variant is a robustness check, not the headline.
- **Benchmarks defined by the source:** MS Self (Ψ restricted to diagonal), MR (expected-return max), Principal Portfolios PP-ME/PP-BM/PP-MOM/PP-EW (Kelly et al. 2023), and FF factor benchmarks.
- **Reproducibility of the rule:** the mathematical rule is fully specified; the operational trading layer (rebalance day, order handling, universe tradability of *portfolio sorts* — see *Execution assumptions*) is **underspecified**.

## Required data

- **Instrument / universe:** US common stocks (CRSP) aggregated into **portfolio-level test assets**, not individual tradable instruments:
  - Universe A: **138 univariate spread portfolios** — monthly tercile sorts per signal, high-minus-low, value-weighted with market-equity weights winsorized at the **80th percentile of NYSE capitalization** (§4.2).
  - Universe B: **544 bivariate portfolios** — size (big/small) × signal (high/low; medium dropped; only high/low retained), 136 signals × 4 = 544 (`ami_126d` dropped for missing 2023 returns) (§4.3).
  - Stock filters: `excntry = "USA"`, `shrcd ∈ {10,11}`, `exchcd ∈ {1,2,3}`, non-missing `ret_exc` and `ret_exc_lead1m` (§4.1).
- **Venue / market type:** US equity exchanges (CRSP); monthly cash equities. No derivatives, no crypto, no futures.
- **Data vendors / fields:** CRSP monthly returns; Compustat accounting variables; IBES analyst coverage/earnings forecasts; **Jensen et al. (2023) "Global Stock Returns and Characteristics"** contributed dataset via WRDS (13 themes: Accruals, Debt Issuance, Investment, Leverage, Low Risk, Momentum, Profit Growth, Profitability, Quality, Seasonality, Size, Short-Term Reversal, Value).
- **Point-in-time:** Compustat quarterly/annual statements assumed publicly available **four months after fiscal period end** (§4). WRDS contributed-data vintage/revision handling for the Jensen et al. signals is `underspecified` (no vintage/revision rule stated).
- **Timestamp:** monthly bar, calendar months; intraday timestamps not applicable. Exact alignment of signal month to return month beyond "s > t" is `underspecified`.
- **Sample:** full sample **January 1963 – December 2023**; **out-of-sample February 1973 – December 2023** (PP comparison subsample: OOS February 1973 – December 2019, Table 4). VIX-regime panels use **January 1990 – December 2023** (Panels C–D of Table 3).
- **Auxiliary series:** Baker–Wurgler investor sentiment `SENT` (July 1965 – December 2023, Wurgler's website), CBOE VIX (1990–2023); evaluation factors: FF5, UMD, REV, LIQ (Pastor–Stambaugh), PEAD/FIN (Daniel et al. 2020, available before December 2018), R_IA/R_ROE (Hou et al. 2015), MGMT/PERF (Stambaugh–Yuan 2017, available before December 2016), plus a fourteen-factor aggregate (Table 6 caption).
- **Missing data:** imputation rules beyond the stated filters are `not stated in source`.
- **Funding/fee/spread fields:** not requested by the source's evaluation design → `data gap` (see *Execution assumptions*).

## Execution assumptions

- **Signal-to-order timing:** monthly; weights formed on month-*t* signals applied to subsequent returns (`s > t`). Same-bar vs next-bar convention at the monthly boundary and the exact execution date are `underspecified`.
- **Portfolio form:** dollar-neutral long-short, **gross leverage fixed at 2** (§2.2) — the standard factor-portfolio convention.
- **Order type / fill model / latency / partial fills:** `not stated in source`.
- **Fees, commission, spread, slippage, market impact:** **`not stated in source`.** A full read of §2 (Trading Strategy, Zero-Cost and Leverage Constraints), §3 (Estimation), §4 (Data) and §5 (Results, Tables 1–9, Figure 1) located **no transaction-cost, turnover-cost, bid-ask, slippage or fill-model analysis** for the strategy; bid-ask spread and turnover appear only as *characteristics* in the Table 9 connectedness regressions, not as costs. Per the contract this is recorded as a data gap — it is **not** to be read as "modeled", and equally not asserted as a tested-unmodeled result.
- **Critical terminology warning:** the paper's **"zero-cost" means self-financing (long proceeds fund shorts; net investment 0) with leverage rescaled to 2** — Table 1's `Cost` column literally reads `Zero Cost` / `Not Zero Cost`. It is **not** a statement about trading-cost adjustment, and it does **not** mean results are net of costs.
- **Turnover / rebalancing intensity:** the strategy re-estimates Λ, Ψ and λ **every month**; the resulting position turnover is `data gap` (never reported — Table 4/5 `Sum`/`ASum` columns are gross leverage, not turnover).
- **Borrow / shorting / capacity:** shorting of the short legs is assumed by the factor-portfolio construction; borrow availability, locate, and fees `not stated in source`; capacity/liquidity limits `not stated in source`.
- **Gross vs net status of all reported numbers:** **not stated explicitly; no cost line exists anywhere in the reported tables → treat every performance figure below as gross-of-trading-costs and cost-adjusted performance as `data gap`.**

## Evidence

### Source-reported

All figures below trace to Avramov & He, arXiv:2602.20856v1 (pinned version) with the stated Table/Figure/Section provenance, market/universe and sample window. **All are source-reported and have not been independently reproduced.** Unless noted, they are the zero-cost, leverage-2 (MS/MR) constructions and are gross of trading costs (cost treatment `not stated in source`).

**Toy example (Table 1; N = 9 ME×BM portfolios, M = 5 characteristics; OOS February 1973 – December 2023; monthly μ %, σ %, annualized SR; `Cost` column = zero-cost flag, not trading cost):**

| Strategy | μ | σ | SR | Cost column |
|---|---|---|---|---|
| MR Cross (unconstrained) | 5.56 | 61.9 | 0.31 | Not Zero Cost |
| MS Cross (unconstrained) | 2.36 | 9.78 | 0.84 | Not Zero Cost |
| MS Self (unconstrained) | 1.31 | 7.57 | 0.60 | Not Zero Cost |
| MR Cross ZC | 0.49 | 3.22 | 0.53 | Zero Cost |
| MS Cross ZC | 0.50 | 1.43 | 1.22 | Zero Cost |

Certainty equivalent (γ = 2): **16.84% per year** for cross-prediction, **8.00 pp higher** than self-prediction (§5.1 prose).

**Main performance — Table 3 (zero-cost, leverage 2; monthly μ %, σ %, annualized SR):**

- Panel A, spread portfolios, **1973:02–2023:12**: MR 0.42 / 3.23 / 0.45; **MS 0.29 / 0.45 / 2.21**. Sentiment split (Baker–Wurgler median): MS SR **2.19** (SENT high) vs **2.22** (SENT low); MR μ 0.73 (high) vs 0.11 (low).
- Panel B, bi-sort portfolios, **1973:01–2023:12**: MR 0.45 / 3.02 / 0.52; **MS 0.26 / 0.27 / 3.32**. SENT high **3.58**, SENT low **3.08** (MS).
- Panel C, spread portfolios, **1990:01–2023:12** (VIX median split): MS 0.24 / 0.43 / **1.92** (VIX high 2.02, VIX low 1.98); MR 0.33 / 3.83 / 0.30 (high) vs 0.07 (low).
- Panel D, bi-sort portfolios, 1990:01–2023:12: **MS 0.24 / 0.29 / 2.90** (VIX high 2.89); MR SR 0.42 full panel.

**Principal-portfolio comparison — Table 4 (OOS February 1973 – December 2019, PP replication sample 1963–2019):**

- Panel A (unconstrained): PP-ME SR 0.51, PP-BM 0.60, PP-MOM 0.48, PP-EW μ 2.83% SR 0.56 (ASum 1.35); MR μ 135.14% SR 0.52 (ASum 537.70); MS μ 68.65% SR 2.22 (ASum 438.01).
- Panel B (zero-cost, leverage 2): MR 0.46 / 3.10 / 0.51; **MS 0.30 / 0.45 / 2.33**, gross leverage ASum = 2.00 for both.

**Cross- vs self-prediction — Table 5 (OOS February 1973 – December 2023):**

- Panel A spread portfolios: MS Self SR **1.42** (μ 6.76, σ 16.54, ASum 30.93); MS Cross SR **2.08** (unconstrained, ASum 438.46); **MS Cross ZC SR 2.21** (μ 0.29, σ 0.45, ASum 2.00).
- Panel B bi-sort portfolios: MS Self SR **2.06** (ASum 99.05); MS Cross SR **3.00** (unconstrained, ASum 2154.07); **MS Cross ZC SR 3.32** (μ 0.26, σ 0.27, ASum 2.00).
- Headline deltas (source framing): cross beats self by **+0.79 SR** (spread) and **> +1.26 SR** (bi-sort) under the constrained implementations (§1).

**Factor spanning — Table 6 (monthly alphas %, Newey–West t, Bartlett kernel, L = 4(T/100)^(2/9); zero-cost leverage-2 MS):**

- Panel A (spread): FF5 **α 0.29, t = 13.29**; FF5+UMD+REV+LIQ **0.26, t = 11.54**; Stambaugh–Yuan **0.28, t = 10.20**; Daniel et al. **0.29, t = 11.09**; fourteen-factor **0.26, t = 8.04**. Loadings: Market β −0.01 (t = −2.56), SMB 0.01 (t = 1.78), others insignificant in FF5.
- Panel B (bi-sort): fourteen-factor **α 0.25, t = 11.36**. (Factor availability caps: PEAD/FIN to Dec 2018; MGMT/PERF to Dec 2016 — Table 6 caption.)

**Time-series evolution — Table 7 + Figure 1 (annualized SR):**

| Period | MS Spread | MS BiSort | MKT-RF | SMB | HML | RMW | CMA | UMD |
|---|---|---|---|---|---|---|---|---|
| 1973–2023 | 2.21 | 3.32 | 0.45 | 0.21 | 0.33 | 0.45 | 0.50 | 0.45 |
| 1973–1999 | 2.84 | 4.98 | 0.48 | 0.16 | 0.47 | 0.36 | 0.58 | 0.96 |
| 2000–2023 | 1.58 | 2.21 | 0.41 | 0.27 | 0.20 | 0.54 | 0.43 | 0.09 |

Figure 1 (ten-year trailing SR, first point January 1983): MS BiSort reaches **4–7** before 2000, MS Spread ≈ **4**; by end-2023 both moderate to **≈ 1.2** (§5.2.4; §1 also reports five-year trailing ≈ 1.2 by end-2023). MS BiSort fixed (λ = 1) prints higher trailing SR than CV-tuned MS BiSort (§5.2.4).

**Signal importance — Table 8 Panel A (time-series average |Λ|, spread universe):** `aliq_at` (liquidity of book assets, Investment theme) **0.139**; `div12m_me` (dividend yield, Value) **0.126**; `at_me` (assets-to-market, Value) **0.125**; `be_gr1a` (change in common equity, Investment) **0.125**. §5.3: return-based signals (momentum, short-term reversal, seasonality) receive persistently low weights.

**Ψ structure — Table 2 Panel A (toy, last rolling window Dec 2003 – Nov 2023):** |diag(Ψ)| avg **0.0068** vs |off-diag(Ψ)| avg **0.0805**; Λ = ME 0.21, BM −0.34, OP 0.29, INV 0.53, MOM 0.69.

**Network — Table 9 / §5.4:** in the bivariate universe, big stocks lead small (NET size coefficient −0.15, robust to −0.19 controlling BM/OP/INV/MOM); controlling five trading frictions reverses the size sign (flagged by the authors as warranting further investigation); low-volume, high-turnover, low-beta stocks are net transmitters (§5.4).

### Independently reproduced

not independently reproduced

### Negative evidence

- **Post-2000 attenuation is in the source itself:** MS Spread SR falls 2.84 → 1.58 and MS BiSort 4.98 → 2.21 (Table 7); ten-year trailing SR decays from 4–7 to ≈ 1.2 by end-2023 (Figure 1); momentum UMD over the same split falls 0.96 → 0.09 (Table 7), i.e. the paper's own regime context says the underlying predictability pool is shrinking (§1 cites Green et al. 2017).
- **No cost analysis whatsoever:** no transaction-cost, turnover, spread, slippage or fill evidence exists in §2–§5 (see *Execution assumptions*). With monthly full re-estimation of a 138- or 544-asset long-short book, cost sensitivity is untested — `data gap`, and a prime falsification target.
- **The baseline is already strong:** MS Self alone delivers SR 1.42 / 2.06 (Table 5). The *increment attributable to the spillover mechanism* is the +0.6 to +1.3 SR delta, not the headline 2.21 / 3.32 — headline numbers alone do not evidence cross-asset spillover alpha.
- **Unconstrained variants are unimplementable as reported:** ASum (gross leverage) 438.01 (MS, Table 4 Panel A), 438.46 / 2154.07 (MS Cross, Table 5), MR μ 135.14% per month with σ 895.59% — only the zero-cost, leverage-2 versions are economically meaningful; MR ZC barely beats noise (SR 0.45–0.53).
- **Zero-cost constraint reduces expected profitability** by the authors' own Appendix C derivation (§2.2).
- **High-dimensional estimation risk:** Ψ has N² parameters (544² = 295,936 in the bi-sort universe) estimated from 120 monthly observations with a single ridge λ; the paper's defense is CV shrinkage and MS BiSort fixed (λ = 1) performing *better*, which equally suggests sensitivity to the regularization choice (§5.2.4, Appendix E). Overfitting risk is acknowledged only indirectly.
- **Test assets are not directly tradable instruments:** both universes are value-weighted factor-mimicking portfolio sorts (tercile spreads and size×signal cells) built from the full CRSP cross-section — implementability for an outside trader requires replicating the sorts, which reintroduces the unstated cost/shorting layer.
- **Regime splits are median splits** of SENT and VIX (Table 3 caption) — in-sample partition points, not pre-declared deployable regime rules.
- **Publication status:** preprint without journal reference; publication-bias and novelty-decay concerns apply (see also the repository's adjacent alpha-decay literature). Peer-review status `not stated in source`.
- **Point-in-time integrity of the WRDS contributed Jensen et al. dataset is not documented in the source** — vintage/revision leakage risk is `underspecified`.

## Falsification plan

Every threshold below is **research-defined** and every operational choice below is **research-proposed** — none is source-reported.

1. **Direct replication of the OOS protocol** (data: CRSP/Compustat + Jensen et al. signals via WRDS; sample: rolling 120-month windows, monthly re-estimation, OOS 1973:02–2023:12). *Metric:* annualized SR of MS Spread. *Fail rule:* OOS SR < 1.00 vs source 2.21 (`research-defined`). *Action:* reject the record as unreproducible; do not advance.
2. **Cost stress** (research-proposed): apply 5 / 10 / 20 bps per side to measured one-month turnover of the leverage-2 book. *Fail rule:* net SR ≤ market SR + 0.10 (`research-defined`) at 10 bps, or net monthly alpha ≤ 0 at 20 bps. *Action:* mechanism not tradable as reported.
3. **Turnover measurement** (research-proposed): report average monthly one-way turnover; *fail rule:* turnover > 100% per month persistently (`research-defined`) without a documented cost model. *Action:* flag as cost-infeasible pending execution study.
4. **Spillover ablation** (core mechanism test): re-estimate with off-diagonal Ψ blocked (= self-prediction) and compare paired OOS SR. *Fail rule:* ΔSR(cross − self) < 0.30 (`research-defined`, source reports +0.79/+1.26). *Action:* attribute any remaining performance to signal aggregation, not cross-asset spillovers; downgrade mechanism claim.
5. **Label-permutation placebo** (research-proposed): randomly re-map asset identities in Ψ each window (or block-shuffle the cross-section) and re-run 500 times. *Fail rule:* median placebo SR ≥ 50% of the true SR (`research-defined`). *Action:* conclude results are estimation artifact.
6. **λ-robustness** (research-proposed): compare CV-selected λ against fixed λ ∈ {0.1, 1, 10}. *Fail rule:* OOS SR swings > 30% across this grid (`research-defined`). *Action:* conclude regularization-driven overfit.
7. **Subperiod / regime honesty test:** OOS 2000–2023 only. *Fail rule:* SR < 1.00 (`research-defined`; source reports 1.58 / 2.21). *Action:* record as regime-dependent, not deployable on full-sample strength.
8. **Factor-spanning replication:** fourteen-factor regression on the replicated strategy. *Fail rule:* α ≤ 0.10%/month or |t| < 2 (`research-defined`; source reports 0.25–0.26% with t = 8.04–11.36). *Action:* performance is exposure to existing factors, reject incremental-alpha claim.
9. **Alternative-universe test** (research-proposed): run the identical estimator on (a) individual NYSE-common stocks and (b) a liquidity-restricted half-sample. *Fail rule:* SR drop > 50% vs portfolio-sort universe (`research-defined`). *Action:* conclude result depends on portfolio aggregation/sort construction.
10. **Point-in-time / leakage audit:** verify Jensen et al. signal availability respects the stated 4-month accounting lag and WRDS vintage; *fail rule:* any signal entering the window before its stated availability (`research-defined`, binary). *Action:* stop — invalid evidence.
11. **Capacity test** (research-proposed): restrict long legs to the top NYSE median-cap decile. *Fail rule:* SR drop > 50% or net (10 bps) SR ≤ 0.5 (`research-defined`). *Action:* capacity-constrained, research-only.
12. **Ablation of the sentiment/VIX splits:** re-run subperiod tests with pre-declared rolling (not full-sample median) thresholds. *Fail rule:* regime SRs disagree in sign with the median-split results (`research-defined`). *Action:* treat §5.2 regime claims as partition artifacts.

## Crypto portability

**unproven.**

- The source contains **zero crypto evidence**: US equities, monthly CRSP, 1963–2023, portfolio sorts only.
- Mechanism portability is plausible but untested: cross-asset lead–lag / information-diffusion spillovers do exist in crypto (the repository's adjacent crypto seesaw record documents a large-coin → altcoin lead-lag structure), yet the direction and sign there are attention-driven and *negative*, unlike the equity diffusion channel assumed here. Any crypto version is a **research-proposed new hypothesis**, not a port.
- Concrete portability gaps: the 138 Jensen et al. accounting/analyst signals have no direct crypto analogue (no book equity, no IBES); the cross-sectional universe of liquid crypto pairs is far smaller than 138–544 test assets (N² estimation burden worsens); 24/7 candle boundaries vs monthly equity months; venue fragmentation and per-venue survivorship; funding, mark/index basis and borrow for the short leg on perpetuals; stablecoin/quote-currency effects; custody/withdrawal and venue risk; listing and delisting bias.
- Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: rebalance-day/timezone convention, ties handling, WRDS signal vintage/revision policy, endpoint inclusion in the 120-month window, λ selection grid details beyond 5-fold CV.
- `data gap`: transaction costs, turnover, spread, slippage, impact, fill model, borrow/short availability, latency, capacity — none appears anywhere in the reviewed primary-source sections; gross-vs-net status of all performance figures is therefore also a `data gap`.
- `not independently reproduced`: every quantitative claim in this record is source-reported from arXiv:2602.20856v1.
- Source-quality: single preprint version, no journal reference, no public replication package cited in the text (no repository/commit exists to pin) → implementation provenance is the paper text alone.
- Identification: test assets are constructed sorts; performance can reflect sort construction, winsorization (80th pct NYSE ME) and value-weighting choices as much as a tradable signal.
- Statistical: Newey–West t-stats address autocorrelation in *factor-spanning regressions*, not the estimation error of a recursively re-estimated 295,936-parameter Ψ; the SRs themselves carry no reported confidence intervals (`data gap`).
- Regime/publication: full-sample SR 2.21/3.32 is dominated by the 1970s–1990s; recent five-year trailing SR ≈ 1.2 (source-reported) is the more honest current-state number.
- Deduplication update rule: this is a new family (cross-predictive SDF / spillover-matrix max-Sharpe construction) — no existing record to update was found repository-wide.

## Implementation status

`implementation_status: not-implemented`.

Nothing in our research stack has been built for this record: no WRDS/CRSP replication, no Ψ/Λ estimator, no portfolio-sort reconstruction, no Qlib full backtest, no production card, no Paper, Testnet or Live run. This document is a normalized research capture of a preprint only. Implementation authorization is a separate, gated decision.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool (`/results/_handoff/candidates.json`); completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. No record may promote itself by wording, evidence count, confidence, or schedule behavior.

## Related Wiki records

Adjacent repository records (read for context; none shares this source identity or this mechanism):

- `crypto-cross-asset-seesaw-lead-lag-rotation-2026-08-31.md` — crypto cross-asset return cross-predictability (Jia, Wu, Yan & Liu 2023, *J. Empirical Finance*): same *cross-predictability* topic family, different market, different mechanism (attention/liquidity seesaw, negative sign), different source identity.
- `nystrom-attention-cross-sectional-stock-transformer-low-rank-2026-09-11.md`, `cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03.md`, `cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03.md` — neighboring cross-sectional/regularized equity signal records with different estimators and hypotheses.

No verified Hermes Wiki Brain page for this source identity is known to this Scout; no Wiki link is asserted (Wiki Brain was not written — Scouts are forbidden to write there).

## Sources

1. Doron Avramov and Xin He. "Stochastic Discount Factors with Cross-Asset Spillovers." arXiv:2602.20856v1 [q-fin.CP], submitted 24 February 2026. Abstract: https://arxiv.org/abs/2602.20856 — DOI: https://doi.org/10.48550/arXiv.2602.20856
2. Full text (HTML v1, read directly 2026-09-23): https://arxiv.org/html/2602.20856v1 — §2.1 Trading Strategy (Eqs. 1–10), §2.2 Zero-Cost and Leverage Constraints (Eqs. 11–12), §3.1–§3.2 Estimation (Eqs. 13–25), §4 Data (§4.1–§4.3), §5 Results (§5.1–§5.4), Tables 1–9, Figure 1, Appendices A–F.
3. Underlying data/signal source named by the paper: Jensen, Kelly, and Pedersen, "A Replication Datasheet: 153 Global return predictors" (Jensen et al. 2023) — Global Stock Returns and Characteristics dataset, WRDS Contributed Data Forms (cited by the primary source; not independently opened for this record).
4. Benchmark/evaluation inputs named by the primary source: Baker and Wurgler (2006) sentiment index (Wurgler data page), CBOE VIX historical data, FF5/UMD/REV/LIQ/PEAD/FIN/R_IA/R_ROE/MGMT/PERF factor series as listed in the Table 6 caption.
