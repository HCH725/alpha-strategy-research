---
schema: strategy-research-record-v1
title: "When Alpha Breaks: Two-Level Uncertainty for Safe Deployment of Cross-Sectional Stock Rankers via Strategy-Level Regime-Trust Gating and Position-Level Epistemic Tail-Risk Capping"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-ranking
  - equity-long-short
  - machine-learning
  - lightgbm
  - epistemic-uncertainty
  - deup
  - direct-epistemic-uncertainty-prediction
  - rank-displacement
  - structural-coupling
  - regime-trust-gate
  - abstention
  - selective-prediction
  - tail-risk-guard
  - conformal-prediction
  - walk-forward-optimization
status: research-only
confidence: high
source_as_of: 2026-02-23
sources:
  - "Ursina Sanderink, 'When Alpha Breaks: Two-Level Uncertainty for Safe Deployment of Cross-Sectional Stock Rankers', arXiv:2603.13252v1 [cs.AI, cs.LG, q-fin.PM], February 23, 2026. DOI: 10.48550/arXiv.2603.13252. https://arxiv.org/abs/2603.13252"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# When Alpha Breaks: Two-Level Uncertainty for Safe Deployment of Cross-Sectional Stock Rankers via Strategy-Level Regime-Trust Gating and Position-Level Epistemic Tail-Risk Capping

## Provenance

- **Primary Source:** Ursina Sanderink, *"When Alpha Breaks: Two-Level Uncertainty for Safe Deployment of Cross-Sectional Stock Rankers"*, arXiv preprint `arXiv:2603.13252v1 [cs.AI, cs.LG, q-fin.PM]`, dated February 23, 2026, submitted March 2026.
- **Canonical DOI:** [10.48550/arXiv.2603.13252](https://doi.org/10.48550/arXiv.2603.13252)
- **Stable Abstract URL:** [https://arxiv.org/abs/2603.13252](https://arxiv.org/abs/2603.13252)
- **Full Text HTML:** [https://arxiv.org/html/2603.13252v1](https://arxiv.org/html/2603.13252v1)
- **Primary LaTeX Source Bundle:** Retrieved from official arXiv source bundle [https://arxiv.org/src/2603.13252](https://arxiv.org/src/2603.13252), containing the complete author source manuscript `twoleveluncertainity.tex` (125,415 bytes). All mathematical equations, tabular metrics, and experimental protocols in this record were verified directly against this primary LaTeX source.
- **Referenced Code Repository:** GitHub project repository listed in author footnote: `https://github.com/sinsasanderink/AIStockForecaster-PIT-Safe-Ranking-First-Signals-for-AI-Equities-FMP-Kronos-FinText-TSFM-`. *(Note: Returned HTTP 404 at Scout verification time; empirical evidence and strategy parameters are verified directly from the complete published preprint text and LaTeX manuscript).*
- **Pre-Write Deduplication & Identity Audit:** A repository-wide inspection verified zero matches for `2603.13252`, `Sanderink`, `When Alpha Breaks`, `DEUP`, `rank displacement`, or `structural coupling`. While adjacent records analyze regime shifts in multi-asset or index contexts (e.g. `regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02.md`, `continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md`), this paper investigates an independent, fundamental problem in cross-sectional equity ranking: the geometric coupling between predictive uncertainty and signal strength, and a two-level deployment architecture that uncouples strategy-level abstention from position-level tail capping.

## Economic mechanism

### Source-reported

Cross-sectional machine learning ranking models (such as gradient-boosted decision trees) are commonly deployed as if scalar point predictions were sufficient: the model produces scores, and capital is allocated following the induced ordering. Under non-stationarity, however, financial markets experience regime shifts in which historically effective factor relationships break or invert.

In the author's primary setting (the *AI Stock Forecaster*), a LightGBM ranker trained on U.S. equities achieves strong development performance (20d shadow-portfolio Sharpe 3.12, all-period Sharpe 2.73). However, during the 2024 out-of-sample holdout, an AI thematic rally and rapid sector rotation severely degraded the signal:
1. At 60-day and 90-day horizons, mean RankIC inverted and became negative ($-0.005$ and $-0.021$).
2. At the primary 20-day horizon, mean RankIC collapsed by 86%, falling from $0.072$ in DEV (2016–2023) to $0.010$ in FINAL (2024–2025).

The author demonstrates two critical economic realities:
1. **Market stress proxies fail to detect model failure:** Conventional operational heuristics condition strategy exposure on market volatility or stress proxies (such as VIX percentile, market realized volatility, or cross-sectional dispersion). Empirically, these proxies are uninformative or counterproductive: VIX percentile has an AUROC of only 0.449 overall (0.504 in FINAL, effectively a coin flip), and cross-sectional mean stock volatility reverses sign in the holdout (AUROC 0.460, worse than random). Market stress measures generic participant anxiety, whereas model failure depends on whether the model's specific factor loadings remain aligned with cross-sectional returns. High VIX in 2024 accompanied a strong thematic equity rally where the model failed, while elevated VIX in 2023 occurred during the model's most profitable periods (generating costly false alarms).
2. **The structural coupling of uncertainty and signal strength in ranking:** Direct Epistemic Uncertainty Prediction (DEUP) trains a secondary model to predict rank displacement. However, because extreme cross-sectional ranks have the greatest mechanical room to displace, predicted epistemic uncertainty $\hat{e}$ is strongly and positively coupled with signal magnitude $|\text{score}|$ (median cross-sectional Spearman $\rho = 0.616$ across 1,865 trading dates). Consequently, the standard academic prescription of inverse-uncertainty sizing ($w_i \propto 1/\sqrt{\hat{e}_i + \varepsilon}$) systematically de-levers the portfolio's highest-conviction ideas in the score tails, degrading portfolio Sharpe.
3. **Decoupling strategy-level abstention from position-level risk:** To resolve this structural dilemma, deployment risk must be split into two separate decisions:
   - *Strategy-level regime-trust gate $G(t)$:* A point-in-time (PIT-safe) classifier tracking trailing realized model efficacy that decides whether the strategy should trade or abstain (hold cash).
   - *Position-level tail-risk cap:* Within active trading dates, rather than continuously modulating weights, apply a discrete cap only to the extreme right tail of epistemic uncertainty (top 15%, P85), preserving score-tail convexity across 85% of positions.

### Research interpretation

1. **Information-theoretic failure of market proxies:** Market volatility indicators (like VIX) reflect aggregate index-option hedging demand and macro uncertainty. In contrast, cross-sectional alpha models extract relative-value spreads across idiosyncratic and sector factor loadings. During thematic market regimes (e.g. narrow mega-cap leadership, speculative retail thematic runs, or AI infrastructure rotations), cross-sectional dispersion can expand while single-stock return correlations with past momentum completely decorrelate or invert. Model failure is an internal informational state, not an external macro state.
2. **Geometric barrier of ranking loss:** In return-forecasting regressions, expected return $\hat{y}$ and forecast variance $\sigma^2$ can vary independently. In cross-sectional ranking, rank displacement $| \text{rank}_{\%}(r) - \text{rank}_{\%}(\hat{r}) |$ is mechanically bounded by the position: a median stock (50th percentile) can at most displace 50 percentiles, whereas a top-ranked stock (99th percentile) can displace 99 percentiles. Any model trained to predict ranking error will assign higher predicted error to extreme scores. Multiplicative inverse-sizing penalizes this mechanical tail dispersion, inadvertently destroying the convexity needed for long-short spread generation.
3. **Discrete gating preserves option-like payoff:** Continuous exposure modulation ($w(t) \propto G(t)$ or trailing IC sizing) degrades recovery performance because the model remains throttled during sharp post-drawdown rebounds. Binary abstention ($G(t) \ge 0.2$ vs. cash) acts as a structural circuit breaker: it halts trading during sustained factor breakdowns, then re-enters with full risk budget once realized factor predictability re-emerges.

## Signal

The signal architecture operates in three sequential stages:

### Stage 1: Base Ranker (`source-reported`)
- **Model Architecture:** LightGBM gradient-boosted decision tree regressor.
- **Predictor Features (7 PIT-safe features):**
  1. `mom_1m`: 1-month momentum (trailing 21-day return).
  2. `mom_3m`: 3-month momentum (trailing 63-day return).
  3. `mom_12m`: 12-month momentum (trailing 252-day return).
  4. `vol_20d`: 20-day annualized realized volatility.
  5. `vol_60d`: 60-day annualized realized volatility.
  6. `adv_20d`: 20-day average daily dollar volume ($\frac{1}{20}\sum_{j=1}^{20} \text{Vol}_{t-j} \cdot P_t$).
  7. `cross_sectional_rank`: Stock's percentile rank in today's cross-section.
- **Prediction Target:** Forward benchmark-relative excess total return:
  $$r_{i,t}^{(\tau)} = R_{i,t\rightarrow t+\tau}^{\text{total}} - R_{\text{benchmark},t\rightarrow t+\tau}^{\text{total}}$$
  evaluated at $\tau \in \{20, 60, 90\}$ trading days (primary deployment horizon: $\tau = 20\text{d}$).
- **Walk-Forward Training Protocol:** Expanding window across 109 calendar folds (February 2016 to February 2025). Minimum 90-trading-day embargo between training label maturation and out-of-sample prediction fold; overlapping labels purged.

### Stage 2: Epistemic Uncertainty Quantification via DEUP (`source-reported`)
1. **Rank Displacement Loss Definition:**
   $$\ell_{i,t}^{(\tau)} = \left| \operatorname{rank}_{\%}\left(r_{i,t\rightarrow t+\tau}\right) - \operatorname{rank}_{\%}\left(\text{score}_{i,t}\right) \right| \in [0, 1]$$
   where $\operatorname{rank}_{\%}$ maps cross-sectional values to $[0, 1]$.
2. **Error Predictor $g(x)$:**
   LightGBM regression model predicting expected rank displacement $\mathbb{E}[\ell_{i,t} \mid x_{i,t}]$. Trained on walk-forward out-of-sample residuals (folds 21–109, $N = 161,863$ stock-level predictions).
   - *Hyperparameters:* $n_{\text{estimators}} = 50$, $\text{max\_depth} = 3$, $\text{num\_leaves} = 8$, $\text{min\_child\_samples} = 50$, $\text{learning\_rate} = 0.05$, feature/row subsampling $0.80$.
   - *Features (11 predictors):*
     - Per-prediction: `score`, `abs_score`, `cross_sectional_rank`.
     - Stock-level: `vol_20d`, `vol_60d`, `mom_1m`, `adv_20d`.
     - Market regime: `vix_percentile_252d`, `market_regime_enc`, `market_vol_21d`, `market_return_21d`.
3. **Deployable Point-in-Time Aleatoric Floor $a_{\text{PIT}}(t)$:**
   To prevent hindsight leakage in deployment, the irreducible noise floor is estimated from fully matured historical losses with horizon lag $\tau=20$ and trailing window $W=60$ trading days:
   $$a_{\text{PIT}}(t) = P_{10}\left( \{ \ell_{i,u} : u \in [t - \tau - W, t - \tau] \} \right)$$
   *(Robustness alternative tested: expanding median of matured $P_{10}$, $a_{\text{EXP}}(t)$).*
4. **Deployable Epistemic Uncertainty Signal:**
   $$\hat{e}_{\text{PIT}}(x_{i,t}) = \max\left(0, g(x_{i,t}) - a_{\text{PIT}}(t)\right)$$

### Stage 3: Two-Level Deployment Architecture (`source-reported`)

#### Level 1: Strategy-Level Regime-Trust Gate $G(t)$
- **Matured Health Index Components:**
  1. *Realized Efficacy $H_{\text{real}}(t)$:* EWMA (halflife = 30 trading days, min_periods = 20) of realized daily RankIC values whose forward $\tau$-day returns have fully matured (structural $\tau = 20\text{d}$ lag).
  2. *Feature and Score Drift $H_{\text{drift}}(t)$ (zero lag):*
     $$H_{\text{drift}} = 0.4 \cdot \text{feat\_drift} + 0.3 \cdot \text{score\_drift} + 0.3 \cdot \text{corr\_spike}$$
     where $\text{feat\_drift}$ is mean absolute z-score of key features vs. trailing 252d mean; $\text{score\_drift}$ is Kolmogorov-Smirnov distance of today's scores vs. trailing 60d scores; and $\text{corr\_spike}$ is mean pairwise 20-day return correlation.
  3. *Cross-Expert Disagreement $H_{\text{disagree}}(t)$:* Spearman rank correlation between primary LightGBM ranker and a secondary model (Rank Average 2).
- **Health Score Aggregation:**
  $$H_{\text{raw}}(t) = z_{\text{real}}(t) - 0.3 \cdot z_{\text{drift}}(t) - 0.3 \cdot z_{\text{disagree}}(t)$$
  $$H(t) = \sigma\left(H_{\text{raw}}(t)\right) \in [0, 1]$$
  $$G(t) = \operatorname{clip}\left(\frac{H(t) - 0.3}{0.7 - 0.3}, 0, 1\right)$$
- **Binary Abstention Rule:**
  $$\text{Active}(t) = \mathbb{1}[G(t) \ge 0.20]$$
  If $G(t) < 0.20$, the strategy holds 100% cash (zero market exposure). Threshold $\theta = 0.20$ calibrated on DEV.

#### Level 2: Position-Level Epistemic Tail-Risk Cap
- On active days ($\text{Active}(t) = 1$):
  1. *Volatility Sizing:* Compute volatility-scaled scores:
     $$w_i^{\text{vol}} = s_{i,t} \cdot \min\left(1, \frac{c_{\text{vol}}}{\sqrt{\text{vol\_20d}_i + \varepsilon}}\right)$$
     where $c_{\text{vol}}$ is calibrated on DEV such that median weight $\approx 0.70$.
  2. *Portfolio Selection:* Select top $K=10$ stocks for the long leg and bottom $K=10$ stocks for the short leg based on sized scores. Equal leg capital allocation.
  3. *Epistemic Tail Cap (`source-reported`):*
     For any selected constituent whose deployable epistemic uncertainty exceeds the 85th cross-sectional percentile ($P_{85}(\hat{e}_{\text{PIT},t})$), apply a 30% weight reduction ($\kappa = 0.70$):
     $$w_i = \begin{cases} w_i^{\text{vol}} \cdot 0.70 & \text{if } \hat{e}_{\text{PIT}}(x_{i,t}) > P_{85}(\hat{e}_{\text{PIT},t}) \\ w_i^{\text{vol}} & \text{otherwise} \end{cases}$$
  4. *Residual Rebalance Rule (`research-proposed`):* Weights clipped by the cap may either be held in cash (reducing gross leverage) or redistributed pro-rata across the remaining uncapped 85% of leg names. In the primary paper, cash de-leveraging is maintained.

## Required data

- **Asset Class / Universe (`source-reported`):** U.S. common equities (Polygon ticker type `CS`). Dynamic investable panel of up to 100 AI-exposed names selected via deterministic tradability waterfall:
  - Minimum share price: $P_{i,t} \ge \$5.00$.
  - Minimum liquidity: 20-day Average Daily dollar Volume $\text{ADV}_{i,t} \ge \$1,000,000$.
  - Theme relevance: Exact ticker match against a 100-ticker AI-themed universe list.
  - Size cap: Top 100 constituents by market capitalization. Realized universe size: mean $N_t = 83.9$ (ALL), $81.8$ (DEV), $98.4$ (FINAL).
- **Benchmark (`source-reported`):** Invesco QQQ ETF (`QQQ`).
- **Timeframe & Session (`source-reported`):** Daily close-to-close bars (4:00 PM Eastern Time).
- **Price & Corporate Action Conventions (`source-reported`):** Vendor split-adjusted close prices. Dividends incorporated explicitly into excess return labels using dividends with ex-date in $(t, t+\tau]$.
- **Macro / Market Inputs (`source-reported`):** CBOE Volatility Index (VIX) closing levels for rolling 252-day percentile calculation; benchmark market returns and 21-day realized volatility.
- **Point-in-Time Availability (`source-reported`):**
  - Features use strictly historical data available at close of day $t$.
  - Realized RankIC used in $H_{\text{real}}(t)$ enforces a mandatory structural lag of $\tau = 20$ trading days (no forward return leakage).
  - DEUP training uses walk-forward expanding windows with a 90-day embargo.
- **Missing Data Handling (`source-reported`):**
  - LightGBM handles missing feature values natively.
  - Missing forward returns (pre-IPO or unlisted rows) dropped from training/evaluation (87.2% overall label coverage across sample; 99.95% coverage in 20d evaluation window).
  - DEUP uncertainty features use zero imputation (`fillna(0)`).
  - CRSP-style delisting returns are omitted (`provenance gap explicitly noted`).

## Execution assumptions

- **Rebalance Cadence (`source-reported`):** 20 trading days, evaluated on non-overlapping monthly rebalances (first trading day of each calendar month).
- **Signal-to-Order Timing:**
  - `source-reported`: Evaluated close-to-close using 20-day forward total returns.
  - `research-proposed`: In live deployment, signals computed at 4:00 PM ET close; limit or market-on-open (MOO) orders submitted for execution at $t+1$ market open (9:30 AM ET).
- **Order Types & Execution Model (`research-proposed`):** Liquid U.S. equities ($ADV \ge \$1\text{M}$); market-on-close (MOC) or arrival-price TWAP over first 30 minutes.
- **Transaction Costs & Slippage (`source-reported`):** 10 basis points ($0.10\%$) per rebalance round-trip turnover applied to portfolio P&L.
- **Shorting & Borrowing Assumptions:**
  - `source-reported`: Frictionless shorting assumed on bottom-10 basket; no explicit borrow fee schedule.
  - `research-proposed`: Prime broker borrow fees for AI-themed small/mid-caps typically range from 25 to 150 bps annualized. Institutional implementation requires borrow locate verification.
- **Leverage & Margining (`research-proposed`):** Dollar-neutral long/short ($100\%$ long, $100\%$ short, $2\times$ gross exposure when active; $0\%$ exposure when gated).

## Evidence

### Source-reported

All metrics trace directly to Ursina Sanderink (`arXiv:2603.13252v1`, Tables 1, 4, 5, 8, 10, 11, 12, 13, 14, and manuscript sections):

#### 1. Baseline Performance Without Uncertainty Controls (Table 1)
Evaluated over 109 walk-forward folds (DEV: 2016–2023, 95 months; FINAL: 2024–2025, 14 months; ALL: 109 months):
- **Shadow Portfolio (20d, Monthly Non-Overlapping L/S, Vol-Sized LightGBM, 10 bps Cost):**
  - *Sharpe (ann.):* ALL = 2.734, DEV = 3.121, FINAL = 2.337.
  - *Sortino (ann.):* ALL = 6.058, DEV = 5.410, FINAL = 9.687.
  - *Max Drawdown:* ALL = $-18.1\%$, DEV = $-18.1\%$, FINAL = $-8.7\%$.
  - *Calmar Ratio:* ALL = 6.76, DEV = 6.07, FINAL = 26.2.
  - *Annualized Return (arithmetic):* ALL = 87.0%, DEV = 79.6%, FINAL = 137.3%.
  - *CAGR (geometric):* ALL = 122.4%, DEV = 109.9%, FINAL = 228.8%.
  - *Annualized Volatility:* ALL = 31.8%, DEV = 25.5%, FINAL = 58.7%.
  - *Monthly Hit Rate:* ALL = 82.6%, DEV = 82.1%, FINAL = 85.7%.
  - *Win/Loss Ratio:* ALL = 2.17$\times$, DEV = 2.08$\times$, FINAL = 2.46$\times$.
  - *Best Month / Worst Month:* ALL = $+64.0\% / -17.4\%$.
  - *Mean Turnover / Month:* ALL = 42.7%, DEV = 43.1%, FINAL = 40.4%.
- **Raw LightGBM Signal Quality (RankIC):**
  - *Mean RankIC (20d / 60d / 90d):*
    - ALL: 0.064 / 0.140 / 0.165
    - DEV: 0.072 / 0.160 / 0.192
    - FINAL: 0.010 / $-0.005$ / $-0.021$ *(Note the severe regime inversion at 60d/90d and 86% drop at 20d).*
  - *Median RankIC (20d / 60d / 90d):*
    - ALL: 0.081 / 0.148 / 0.183
    - DEV: 0.091 / 0.167 / 0.206
    - FINAL: 0.017 / $-0.044$ / $-0.052$

#### 2. DEUP Stock-Level Failure Prediction vs. Baselines (Table 4)
Spearman $\rho$ between predictive signals and realized rank displacement:
- $\hat{e}(x)$ (DEUP): 20d ALL = 0.144, **20d FINAL = 0.192**, 90d ALL = 0.146, **90d FINAL = 0.248**.
- $g(x)$ (raw): 20d ALL = 0.192, 20d FINAL = 0.218, 90d ALL = 0.161, 90d FINAL = 0.262.
- `vol_20d`: 20d ALL = 0.047, 20d FINAL = 0.010, 90d ALL = 0.035, 90d FINAL = 0.009.
- `VIX percentile`: 20d ALL = 0.018, 20d FINAL = $-0.022$, 90d ALL = 0.053, 90d FINAL = $-0.020$.
- $|score|$: 20d ALL = 0.096, 20d FINAL = 0.065, 90d ALL = 0.018, 90d FINAL = 0.013.
*(DEUP uncertainty maintains or improves informativeness out of sample, whereas volatility and VIX collapse to zero).*

#### 3. Quintile Monotonicity (Table 8)
Mean realized rank loss by $\hat{e}(x)$ quintile:
- **20d DEV:** Q1 = 0.265, Q2 = 0.267, Q3 = 0.297, Q4 = 0.354, Q5 = 0.400 (Spearman $\rho = 1.0$, Q5/Q1 = 1.51).
- **20d FINAL:** Q1 = 0.253, Q2 = 0.275, Q3 = 0.308, Q4 = 0.366, Q5 = 0.427 (Spearman $\rho = 1.0$, Q5/Q1 = **1.69**).
- **90d DEV:** Q1 = 0.242, Q2 = 0.258, Q3 = 0.285, Q4 = 0.321, Q5 = 0.371 (Spearman $\rho = 1.0$, Q5/Q1 = 1.53).
- **90d FINAL:** Q1 = 0.233, Q2 = 0.305, Q3 = 0.315, Q4 = 0.386, Q5 = 0.437 (Spearman $\rho = 1.0$, Q5/Q1 = **1.88**).

#### 4. Deployment Policy Ablation at 20d (Table 5 & Table 10)
Sharpe ratio ($\times\sqrt{12}$) from non-overlapping monthly returns with 10 bps transaction costs:
- **Ungated Raw (LGB):** ALL Sharpe = 2.730, DEV = 3.107, FINAL = 1.650, Crisis MaxDD = $-7.4\%$.
- **Variant 1 (Gate + Raw):** ALL Sharpe = 1.928, DEV = 2.039, FINAL = $-0.322$, Crisis MaxDD = $-7.4\%$.
- **Variant 2 (Gate + Vol):** ALL Sharpe = 1.886, DEV = 1.971, FINAL = 0.375, Crisis MaxDD = $-8.4\%$.
- **Variant 4 (Gate + Resid-$\hat{e}$):** ALL Sharpe = 1.987, DEV = 2.041, FINAL = 0.953, Crisis MaxDD = $-6.0\%$.
- **Variant 6 (Gate + Vol + $\hat{e}$-Cap, P85, $\kappa=0.70$):**
  - Under deployable PIT-safe $\hat{e}^{\text{PIT}}$ ($W=60$): ALL Sharpe = **1.864 / 1.877**, DEV = **1.915 / 1.928**, FINAL = **0.906 / 0.925**, Crisis MaxDD = **$-6.7\%$**.
  - Under hindsight oracle $\hat{e}^{\text{oracle}}$: ALL Sharpe = 1.864, DEV = 1.915, FINAL = 0.906, Crisis MaxDD = $-6.7\%$ (Table 10).
  *(Identical performance confirms that the percentile cap operates independently of aleatoric floor scale, making it strictly deployable without lookahead).*
- *Alternative P&L Series reported in author text (Section 1 & 6.2):* Gate + Vol alone yielded ALL 0.817, FINAL 0.191; Gate + Vol + $\hat{e}$-Cap achieved ALL 0.884, FINAL 0.316. In both evaluations, Gate + Vol + $\hat{e}$-Cap delivers the highest holdout Sharpe among deployable policies.

#### 5. Regime-Trust Gate Discriminative Performance (Table 11 & Table 12)
- **Target:** Matured $\text{good\_day}(t) = \mathbb{1}[\text{matured\_RankIC}(t) > 0]$ ($N_{\text{ALL}} = 2,218$, $N_{\text{FINAL}} = 284$):
  - $H(t)$ combined: AUROC ALL = **0.721**, FINAL = **0.750**.
  - $G(t)$ gate: AUROC ALL = 0.710, FINAL = 0.743.
  - $H_{\text{real}}$-only: AUROC ALL = 0.715.
  - Market volatility (21d): AUROC ALL = 0.596, FINAL = 0.569.
  - Mean stock volatility: AUROC ALL = 0.590, FINAL = 0.460.
  - VIX percentile: AUROC ALL = 0.449, FINAL = 0.504.
- **Operating Point ($G(t) \ge 0.20$):** Precision = 80.0%, Recall = 64.0%, Abstention Rate = 47.2%. Confusion matrix: 937 TP, 234 FP, 527 FN, 520 TN.
- **Calibration Monotonicity across Buckets (Table 12):**
  - Bucket 0 ($G \in [0, 0.1)$): Mean $G = 0.006$, Mean RankIC = $-0.011$, 51.2% bad days.
  - Bucket 1 ($G \in [0.1, 0.4)$): Mean $G = 0.236$, Mean RankIC = $+0.065$, 34.3% bad days.
  - Bucket 2 ($G \in [0.4, 0.7)$): Mean $G = 0.573$, Mean RankIC = $+0.114$, 22.0% bad days.
  - Bucket 3 ($G \in [0.7, 1.0]$): Mean $G = 0.939$, Mean RankIC = $+0.153$, 11.5% bad days.

#### 6. Multi-Crisis Stress Test Diagnostic (Table 13)
Across 5 stress episodes and 3 calm reference windows (2016–2025), $G(t)$ achieved **7 out of 8 correct verdicts** (87.5%), compared to **5 out of 8** (62.5%) for a 67th-percentile VIX gate:
- COVID recovery 2020: Mean $G = 0.375$, IC = $+0.062$ (both active, correct).
- Meme mania 2021: Mean $G = 0.210$, IC = $-0.040$ ($G(t)$ active at 73% abstention, mild miss; VIX abstained, correct).
- Inflation shock 2022: Mean $G = 0.077$, IC = $-0.024$ (both abstained, correct).
- Late hiking 2023 H2: Mean $G = 0.381$, IC = $+0.034$ ($G(t)$ active, correct; VIX abstained, false alarm).
- AI rotation 2024: Mean $G = 0.123$, IC = $-0.013$ (both abstained, correct).
- Calm 2018: Mean $G = 0.323$, IC = $+0.088$ (both active, correct).
- Calm 2019: Mean $G = 0.566$, IC = $+0.122$ ($G(t)$ active, correct; VIX abstained, false alarm).
- Calm 2023 H1: Mean $G = 0.486$, IC = $+0.104$ ($G(t)$ active, correct; VIX abstained, false alarm).

### Independently reproduced

- Not independently reproduced. All figures and tables cited above represent empirical findings reported by Ursina Sanderink (`arXiv:2603.13252v1`).

### Negative evidence

The primary research documents multiple explicit failure modes and negative results:
1. **Failure of Inverse-Uncertainty Sizing in Ranking:** Multiplicative sizing based on epistemic uncertainty ($w_i \propto 1/\sqrt{\hat{e}_i + \varepsilon}$) degrades portfolio Sharpe relative to simple volatility weighting (Variant 3 UA-Sort Sharpe 0.726 vs. 0.817 for Gate + Vol). Calibrating the uncertainty weight $\lambda$ on DEV produces $\lambda = 0.05$, effectively collapsing the uncertainty adjustment to zero.
2. **Failure of Residualized Uncertainty:** Regressing $\hat{e}$ on $|\text{score}|$ removes linear correlation statistically, but the resulting residualized uncertainty signal introduces excessive noise, causing FINAL Sharpe to turn deeply negative ($-0.450$, author text).
3. **Failure of Continuous Gating:** Sizing exposure continuously by $G(t)$ or trailing RankIC (Kill baseline K4) destroys recovery convexity. K4 Sharpe (0.754) barely matches Gate + Raw (0.758).
4. **Complete Breakdown of Market Volatility Baselines:** VIX percentile is indistinguishable from a random guess (AUROC 0.504 in FINAL). Cross-sectional stock volatility reverses sign (AUROC 0.460), meaning high volatility in 2024 actually correlated with better model performance.
5. **Aggregated Uncertainty Fails as a Regime Indicator:** Aggregating per-stock $\hat{e}$ (median, 90th percentile, IQR) yields AUROC $\approx 0.50$ for predicting regime-level success, confirming that micro uncertainty cannot detect macro model failure.
6. **2021 Meme Mania Gate Leakage:** During the early 2021 retail short-squeeze wave, $G(t)$ averaged 0.210 (narrowly above the 0.20 cutoff) with 73% abstention, but suffered mild negative RankIC ($-0.040$).

## Falsification plan

To falsify the economic mechanism or deployment rules, the following operational empirical tests are specified:

1. **Structural Coupling Absence Test (`research-defined falsification threshold`):**
   - *Test:* Compute the cross-sectional Spearman correlation $\rho_t = \rho_S(\hat{e}_t, |\mathbf{s}_t|)$ across a minimum of 500 walk-forward trading dates on an alternative cross-sectional universe.
   - *Threshold:* If median $\rho_t \le 0.20$ or is statistically non-positive on $>30\%$ of dates, the structural coupling hypothesis is falsified for that asset class, and inverse-uncertainty sizing should be re-tested against tail capping.
2. **Regime-Trust Gate AUROC Out-of-Sample Test (`research-defined falsification threshold`):**
   - *Test:* Evaluate the binary classification AUROC of $G(t)$ on a completely unseen temporal holdout (e.g. 2025–2027) or alternative asset universe (e.g. Russell 1000 or S&P 500).
   - *Threshold:* If $G(t)$ AUROC $\le 0.55$, reject the hypothesis that trailing realized efficacy acts as an effective model health gate.
3. **Holdout Sharpe Superiority Test (`research-defined falsification threshold`):**
   - *Test:* Compare the net-of-cost annualized Sharpe of `Gate + Vol + e-Cap` against `Gate + Vol` across a full market cycle with at least one documented regime failure.
   - *Threshold:* If the Sharpe improvement $\Delta \text{Sharpe} \le +0.05$ or Crisis MaxDD worsens by $>1.0$ percentage point, reject the epistemic tail-risk cap as an effective downside guardrail.
4. **Lead-Lag PIT Embargo Audit:**
   - *Test:* Artificially perturb the structural lag $\tau$ in $H_{\text{real}}(t)$ from $20\text{d}$ to $19\text{d}, 15\text{d}, 10\text{d}$.
   - *Failure Rule:* If gate AUROC drops precipitously when moving from $19\text{d}$ to $20\text{d}$, forward lookahead contamination is present.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Cross-Asset Market Structure Differences:**
  - *Continuous Trading:* Unlike U.S. equities (which close at 4:00 PM ET), crypto perpetual markets trade 24/7/365. Bar boundaries must be standardized (e.g. 00:00 UTC daily closes).
  - *Funding & Basis Frictions:* In crypto perpetuals (Binance, OKX, Bybit, Hyperliquid), holding positions across 20-day horizons incurs continuous 8-hour funding rates. In bull regimes, long legs pay significant carry; in bear cascades, short legs may pay carry.
  - *Universe Definition:* The dynamic top-100 U.S. AI equity universe translates into a top-50 or top-100 liquid perpetual token universe filtered by 24h trading volume ($\ge \$10\text{M}$) and open interest.
  - *Regime Dynamics in Crypto:* Crypto regimes shift rapidly due to cascading liquidations, basis shocks, and regulatory events. A 20-day structural lag in $H_{\text{real}}(t)$ would be too sluggish for crypto; the horizon would need adaptation to $\tau = 1\text{d}$ or $3\text{d}$, with high-frequency order-book and funding-rate drift replacing long-horizon returns.
- **Porting Verdict:** The conceptual architecture (strategy-level health gating + position-level uncertainty tail capping) is directly applicable to crypto cross-sectional factor ranking models, but parameter choices ($20\text{d}$ horizon, $W=60$, $\theta=0.20$) cannot be ported directly without re-calibration. Empirical validity in crypto remains entirely unproven.

## Limitations

1. **Narrow Thematic Universe (`source-reported`):** All evaluations are confined to a single 100-constituent AI-exposed U.S. equity universe. Cross-sectional pairwise correlations in this basket are higher than in broad-market universes (e.g. S&P 500 or Russell 3000), which may amplify score-tail crowding.
2. **Omission of Delisting Returns (`source-reported`):** Securities that delist mid-holding period have their labels dropped rather than penalized with CRSP terminal delisting returns. While rare in this large-cap universe, this represents an empirical provenance gap.
3. **Structural Lag in Regime Gate (`source-reported`):** Because $H_{\text{real}}(t)$ relies on matured forward returns, there is an inherent $\tau$-day (20-day) observation lag. Sudden, sharp regime breaks lasting less than 20 days cannot be anticipated by $H_{\text{real}}$ alone (relying entirely on real-time feature drift $H_{\text{drift}}$).
4. **Execution & Borrow Cost Omission (`research-proposed`):** Backtests apply a flat 10 bps turnover fee but do not model hard-to-borrow fees or short locate availability, which can be non-trivial for small-cap growth names during retail squeeze episodes.
5. **Code Availability Gap:** The GitHub URL cited in the preprint returned HTTP 404 at scout inspection; empirical verification relies exclusively on the published LaTeX manuscript and arXiv preprint.

## Implementation status

- `not-implemented`

No implementation of this two-level uncertainty architecture, the DEUP rank-displacement error predictor, or the $G(t)$ regime-trust gate exists in `nautilus-quant-system`, PyBroker, or NautilusTrader.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is an upstream research capture. Inclusion in this repository does not constitute authorization for deployment, paper trading, testnet, or live trading. Any future implementation or validation requires explicit intake review and formal backtest verification in Loop B (`nautilus-quant-system`).

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Foundational principles of walk-forward embargoing, label purging, and point-in-time safety applied in the base ranker.
- `[[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]` — Cross-sectional ranking models evaluated under market frictions.
- `[[quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]]` — Compares continuous vs. discrete regime-timing mechanisms.
- `[[quant/regime-adaptive-continual-learning-portfolio-management-recap-2026-09-02]]` — Non-stationary market adaptation in portfolio management.
- `[[quant/alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]]` — Market-neutral cross-sectional portfolio construction.

## Sources

1. Ursina Sanderink, *"When Alpha Breaks: Two-Level Uncertainty for Safe Deployment of Cross-Sectional Stock Rankers"*, arXiv preprint `arXiv:2603.13252v1 [cs.AI, cs.LG, q-fin.PM]`, dated February 23, 2026, submitted March 2026.
   - Canonical DOI: [10.48550/arXiv.2603.13252](https://doi.org/10.48550/arXiv.2603.13252)
   - Stable arXiv URL: [https://arxiv.org/abs/2603.13252](https://arxiv.org/abs/2603.13252)
   - Full-text HTML: [https://arxiv.org/html/2603.13252v1](https://arxiv.org/html/2603.13252v1)
   - Full-text PDF: [https://arxiv.org/pdf/2603.13252v1](https://arxiv.org/pdf/2603.13252v1)
   - Primary TeX source bundle: [https://arxiv.org/src/2603.13252](https://arxiv.org/src/2603.13252) (`twoleveluncertainity.tex`)
2. S. Lahlou, M. Jain, H. Neber, G. Ortiz-Jimenez, D. Hjelm, and Y. Bengio, *"DEUP: Direct Epistemic Uncertainty Prediction"*, Transactions on Machine Learning Research (TMLR), 2023.
3. Y. Liu, X. Tao, and Y. Yuan, *"Uncertainty-adjusted sorting for asset pricing with machine learning"*, arXiv preprint `arXiv:2601.00593`, 2026.
4. L. Hentschel, *"Contextual alpha: Emphasizing forecasts where they work best"*, Working Paper, 2025.
5. V. Vovk, A. Gammerman, and G. Shafer, *"Algorithmic Learning in a Random World"*, Springer, 2005.
