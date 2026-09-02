---
schema: strategy-research-record-v1
title: "KellyBoost: Growth-Optimal Portfolio Construction with Multi-Output Gradient-Boosted Decision Trees, Exact Log-Growth Hessian Rectification, and Leave-One-Out Ensembling"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - kelly-criterion
  - gradient-boosting
  - xgboost
  - decision-focused-learning
  - end-to-end-allocation
  - leave-one-out-ensemble
status: research-only
confidence: high
source_as_of: 2026-08-24
sources:
  - "Jiayu Li, 'KellyBoost: Growth-Optimal Portfolio Construction with Gradient-Boosted Trees', arXiv preprint arXiv:2608.23393v1 [q-fin.PM, cs.LG], August 24, 2026. DOI: 10.48550/arXiv.2608.23393. Stable URL: https://arxiv.org/abs/2608.23393"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# KellyBoost: Growth-Optimal Portfolio Construction with Multi-Output Gradient-Boosted Decision Trees, Exact Log-Growth Hessian Rectification, and Leave-One-Out Ensembling

## Provenance

- **Primary Source:** Jiayu Li, *"KellyBoost: Growth-Optimal Portfolio Construction with Gradient-Boosted Trees"*, arXiv preprint `arXiv:2608.23393v1 [q-fin.PM, cs.LG]`, submitted August 24, 2026. DOI: [10.48550/arXiv.2608.23393](https://doi.org/10.48550/arXiv.2608.23393). Stable URL: [https://arxiv.org/abs/2608.23393](https://arxiv.org/abs/2608.23393).
- **Primary Subject Areas:** Portfolio Management (`q-fin.PM`), Machine Learning (`cs.LG`).
- **Research Scope:** Portfolio construction is fundamentally a decision problem, yet the predominant machine learning paradigm in quantitative asset management decomposes it into a two-stage "predict-then-optimize" pipeline: models are first trained to forecast conditional returns under statistical losses (e.g., mean squared error), and these forecasts are subsequently fed into a quadratic or mean-variance optimizer with a separately estimated covariance matrix. This introduces well-documented failure modes: forecast errors are disproportionately amplified in the directions the optimizer exploits, return forecasts are notoriously noisy, and the two stages optimize fundamentally mismatched objectives. While neural networks have been applied to end-to-end portfolio learning (mapping features directly to asset weights), gradient-boosted decision trees (GBDTs)—the established standard for tabular financial data—have historically been excluded because tree ensembles cannot be trained via gradient backpropagation. Jiayu Li resolves this limitation by constructing KellyBoost: an exact, end-to-end multi-output GBDT formulation that directly optimizes the Kelly growth criterion using closed-form gradients and exact diagonal Hessians under saddle-free Newton rectification.

## Economic mechanism

### Source-reported

1. **Direct Conditional Growth Optimality vs. Proxy Regression:** Classical growth-optimal portfolio theory (Kelly 1956, Breiman 1961) maximizes the expected logarithmic wealth growth $\mathbb{E}[\log(1 + w^\top y)]$. Classical implementations either condition on no information (unconditional Kelly) or rely on static rolling windows. KellyBoost represents the conditional version: a non-parametric tree estimator $w(x) = \text{softmax}(z(x))$ mapping an arbitrary macroeconomic and market state vector $x \in \mathbb{R}^d$ directly to the growth-optimal allocation on the simplex $\Delta^{K-1}$.
2. **Elimination of the Optimization Seam:** By defining the training loss directly as the negative log growth rate $\ell(z, y) = -\log(1 + \text{softmax}(z)^\top y)$, there is no intermediate return forecast, no rolling covariance matrix inversion, and no surrogate proxy. The tuning metric, split search criterion, and evaluation metric are identical.
3. **Margin-Sensitive Compounding vs. Argmax Classification:** Practitioners attempting to allocate via tree classifiers often train on an argmax label ("index of the best-performing asset") using cross-entropy. Cross-entropy discards the entire margin structure of financial returns: a month won by 20 basis points is penalized identically to a month won by 2,000 basis points. In contrast, the Kelly gradient incorporates the realized portfolio return $S = w^\top y$ and the compounding denominator $1/(1+S)$, scaling updates inversely with portfolio wealth growth.
4. **Vector-Leaf Joint Partitioning:** Asset allocation is inherently a joint relative decision ("growth stocks vs. gold"). KellyBoost utilizes multi-output trees with vector leaves (`multi_strategy = "multi_output_tree"`), where scalar splits partition the feature space once for all $K$ assets simultaneously based on joint gain. This imposes an inductive bias where macro regimes (e.g., yield curve inversions, volatility spikes) trigger unified reallocation across the entire portfolio rather than requiring $K$ independent noisy trees.
5. **Split-Tie Instability and Accidental Shrinkage:** Boosted trees exhibit chaotic sensitivity to training samples: dropping a single row (0.02% of data) flips near-tied split boundaries and moves live portfolio weights by multiple percentage points. Furthermore, faithfully optimizing an unconstrained conditional Kelly objective concentrates aggressively on historical winners. In low-signal monthly regimes, two-stage predict-then-optimize pipelines outperform unregularized end-to-end Kelly models because near-zero return forecasts act as accidental shrinkage toward uniform diversification.

### Research interpretation

The falsifiable thesis is that **training multi-output GBDTs directly on the exact logarithmic growth loss improves realized out-of-sample log growth over argmax classification surrogates while systematically reducing portfolio turnover, but requires explicit structural shrinkage or fractional Kelly dampening to prevent destructive over-concentration caused by estimation error**:
- The decision-focused loss preserves the economic magnitude of asset outperformance, avoiding the churn of categorical classifiers.
- Second-order optimization with exact Hessian preconditioning accelerates in-sample convergence by more than $3\times$ relative to constant-curvature boosting, but out-of-sample deployment demands explicit regularization (risk aversion $\gamma > 1$ or shrinkage) rather than relying on accidental pipeline artifacts.

## Signal

### 1. Mathematical Formulation and Action Space

Let $x_t \in \mathbb{R}^d$ denote the market and macroeconomic feature vector observed at decision date $t$, and $y_t \in \mathbb{R}^K$ denote the vector of realized holding-period simple returns over $[t, t+h]$ across $K$ asset legs.
A multi-output gradient-boosted tree model outputs a raw score vector $z(x_t) = (z_1(x_t), \dots, z_K(x_t))^\top \in \mathbb{R}^K$.
The portfolio weight vector $w_t = \sigma(z(x_t)) \in \Delta^{K-1}$ is generated via the softmax transformation:
$$\sigma_k(z) = \frac{\exp(z_k)}{\sum_{j=1}^K \exp(z_j)}, \quad k \in \{1, \dots, K\}$$
The portfolio is long-only and fully invested by construction ($\sum_{k=1}^K w_{t,k} = 1, w_{t,k} \ge 0$). Inclusion of an explicit cash leg ensures full investment is non-restrictive.

### 2. Loss Function and Exact Derivatives

The realized holding-period portfolio return is $S_t = w_t^\top y_t = \sum_{k=1}^K \sigma_k(z) y_{t,k}$.
The per-row training loss is the negative log growth rate:
$$\ell(z, y) = -\log(1 + S_t) = -\log\left(1 + \sum_{k=1}^K \sigma_k(z) y_{t,k}\right)$$
Using the Jacobian identities $\frac{\partial \sigma_k}{\partial z_j} = \sigma_k(\delta_{kj} - \sigma_j)$ and $a_k = \frac{\partial S}{\partial z_k} = \sigma_k(y_k - S)$, the exact gradient $g_k = \frac{\partial \ell}{\partial z_k}$ is:
$$g_k = \frac{\sigma_k (S - y_k)}{1 + S}$$
Asset $k$'s logit is driven upward when its return exceeds the portfolio return ($y_k > S$), scaled by its current allocated probability $\sigma_k$ and inversely proportional to wealth accumulation $1+S$.

The exact diagonal second derivative $h_k = \frac{\partial^2 \ell}{\partial z_k^2}$ is derived in closed form:
$$h_k = g_k (1 - 2\sigma_k) + g_k^2$$
Because $\ell(z, y)$ is non-convex in the raw logits $z$, the true diagonal curvature $h_k$ can be negative (especially for assets currently outperforming the portfolio when $\sigma_k < 0.5$). Tree leaf optimization requires positive curvature denominators; KellyBoost applies saddle-free Newton rectification:
$$\tilde{h}_k = |h_k| = |g_k(1 - 2\sigma_k) + g_k^2|$$
Rectification modifies step size while mathematically guaranteeing strict descent along the local gradient linearization: $\sum_k g_k v_k = -\sum_k \frac{g_k^2}{|h_k| + \lambda} < 0$.

### 3. Full Hessian and CRRA Extension

The exact full $K \times K$ Hessian matrix has closed form:
$$H_{jk} = \frac{\partial^2 \ell}{\partial z_j \partial z_k} = \frac{a_j a_k}{(1+S)^2} + \frac{1}{1+S} \left[ S \sigma_j \sigma_k - \sigma_j a_k - \sigma_k a_j - \delta_{jk} \sigma_k (y_k - S) \right]$$
The objective extends to the Constant Relative Risk Aversion (CRRA) family $\phi_\gamma(S) = \frac{(1+S)^{1-\gamma} - 1}{\gamma - 1}$:
$$g_k = \phi_\gamma'(S) a_k, \quad h_k = \phi_\gamma''(S) a_k^2 + g_k (1 - 2\sigma_k)$$
where $\gamma \to 1$ continuously recovers the logarithmic Kelly objective, and $\gamma > 1$ serves as an integrated risk-aversion dial (fractional Kelly).

### 4. Vector-Leaf Boosting and Leave-One-Out Deployment

- **Tree Architecture:** Multi-output binary decision trees with vector-valued leaves. For a leaf $j$ containing sample indices $I_j$, the coordinate-wise Newton update is:
  $$v_{jk} = -\frac{\sum_{i \in I_j} g_{ik}}{\sum_{i \in I_j} \tilde{h}_{ik} + \lambda}$$
  Split selection scans candidate features across all outputs jointly, maximizing gain:
  $$\text{Gain} = \frac{1}{2} \sum_{k=1}^K \left[ \frac{G_{L,k}^2}{H_{L,k} + \lambda} + \frac{G_{R,k}^2}{H_{R,k} + \lambda} - \frac{G_{P,k}^2}{H_{P,k} + \lambda} \right] - \gamma_{\text{split}}$$
- **Leave-One-Out Ensemble ($K_{\text{ens}} = 4$):** To neutralize chaotic split-point flips, the live allocation is the average of $K_{\text{ens}} = 4$ models, where each member $s \in \{1, \dots, 4\}$ is trained on the full dataset minus a single interior row drawn deterministically from seed $s$, preserving hyperparameter capacity while decorrelating split ties.

## Required data

- **Universe (8 Asset Legs):**
  1. Growth Equity: Vanguard Growth Index Fund (`VIGRX`)
  2. Value Equity: Vanguard Value Index Fund (`VIVAX`)
  3. Long-Term Treasuries: Vanguard Long-Term Treasury Fund (`VUSTX`)
  4. International Equity: Vanguard Total International Stock Index Fund (`VGTSX`)
  5. Energy Equity: Vanguard Energy Fund (`VGENX`)
  6. Gold: COMEX Gold Futures continuous (`GC=F`)
  7. Silver: COMEX Silver Futures continuous (`SI=F`)
  8. Cash Leg: 13-week Treasury Bill discount yield (`^IRX`), with 20-day accrual yield $\frac{\text{yield}}{100} \times \frac{20}{252}$ known at decision time.
- **Context Feature Series (30 Exogenous Series):** S&P 500, VIX, 4 Treasury yields/spreads, copper, natural gas, corn, wheat, soybeans, US Dollar Index, Russell 2000, Nasdaq, emerging market equities, REITs, investment-grade credit, high-yield credit, TIPS, CBOE SKEW, and JPY.
- **Feature Generation:** 7,871 candidate columns constructed from backward-looking transforms (rolling returns, drawdowns, MA ratios, $z$-scores, realized volatility, skewness, kurtosis, Hurst exponent, and Dempster interval quantiles over 1, 3, 6, 12, 24-month windows).
- **Timeframe & Resolution:** Daily closes; 20-trading-day rebalancing cycle ($h = 20$ trading days $\approx 1$ month); history spanning 2003-02 to 2026-07.
- **Point-in-Time Discipline:** Same-day closes; strictly backward-looking; futures series forward-filled onto the NYSE trading calendar; no macro releases requiring publication revisions.

## Execution assumptions

- **Decision Frequency:** Rebalanced every 21 trading days on an end-anchored decision grid (anchored at the most recent available bar and counted backwards to prevent stale decisions).
- **Order Execution:** Market-on-close rebalancing into mutual fund / ETF / futures legs.
- **Transaction Cost Modeling:** One-way proportional fee schedules evaluated across 0 bps, 5 bps, 10 bps, and 20 bps.
- **Shorting & Leverage:** None; constrained strictly to the unit simplex $\Delta^{K-1}$ ($w_k \ge 0, \sum w_k = 1$).

## Evidence

### Source-reported

All figures below are directly cited from Jiayu Li (arXiv:2608.23393v1, August 2026), evaluated over a 23-year backtest with a strictly separated development segment (2003-02 to 2012-12, single-row purged walk-forward with 19-day purge and 60-day embargo) and an untouched evaluation segment (2013-01 to 2026-07, 13.6 years):

1. **$2 \times 2$ Controlled Loss-Effect Comparison (Primary Metric: Mean Log Growth per 20-day decision $\overline{\log G} \times 100$):**
   - *Gradient-Boosted Trees (Growth Loss vs. Argmax Cross-Entropy Surrogate):*
     - Searched Features (7,871-column pool): KellyBoost achieves **$0.47$** vs. Multiclass Surrogate **$0.35$** (**$+0.12$** per decision).
     - Hand-Built Features (174 columns): KellyBoost achieves **$0.39$** vs. Multiclass Surrogate **$0.32$** (**$+0.07$** per decision).
   - *Multi-Layer Perceptron (MLP under identical architecture):*
     - Searched Features: Kelly loss achieves **$0.56$** vs. Cross-Entropy **$0.20$** (**$+0.36$** per decision).
     - Hand-Built Features: Kelly loss achieves **$0.67$** vs. Cross-Entropy **$0.49$** (**$+0.18$** per decision).
   - *Statistical Significance:* The growth objective wins **4 out of 4 cells** in both learner classes and both feature pipelines. Paired per-decision difference across the 4 cells ranges from **$+0.07$ to $+0.37$** per decision. The pooled paired difference is **$+0.18$** with moving-block bootstrap $\Pr(\Delta > 0) = \mathbf{0.89}$ (stable between $0.84\text{--}0.96$ across block lengths of 1 to 12 decisions).
2. **Transaction Cost Widening Effect:**
   - In all four cells, the growth objective trades significantly less than the argmax surrogate:
     - Searched Trees: **$7.9\times$** annualized turnover (KellyBoost) vs. **$13.1\times$** (Surrogate).
     - Hand-Built Trees: **$4.8\times$** vs. **$10.8\times$**.
     - Searched MLPs: **$11.8\times$** vs. **$16.8\times$**.
     - Hand-Built MLPs: **$15.4\times$** vs. **$16.0\times$**.
   - Due to lower turnover, imposing transaction costs widens the pooled advantage over the surrogate:
     - Gross (0 bps): $+0.18$ ($\Pr(\Delta > 0) = 0.89$)
     - 5 bps: $+0.20$ ($\Pr(\Delta > 0) = 0.91$)
     - 10 bps: $+0.22$ ($\Pr(\Delta > 0) = 0.93$)
     - 20 bps: **$+0.25$** per decision ($\Pr(\Delta > 0) = \mathbf{0.95}$).
3. **Curvature Optimization vs. Deployment Inversion (Ablation Table 5):**
   - On the development segment protocol at identical hyperparameters, the exact rectified Hessian $|\tilde{h}_k|$ scores **$+4.19$** vs. constant Hessian (gradient-only boosting) **$+1.43$** ($\times 100$), confirming that exact curvature is over $2.9\times$ more effective at optimizing the training objective.
   - However, upon out-of-sample deployment, the ranking inverts: the constant Hessian's undersized steps leave the softmax closer to uniform diversification, outperforming faithfully optimized full-Kelly.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **End-to-End Over-Concentration Failure:** Faithfully optimizing the conditional full-Kelly objective leads to aggressive portfolio concentration (the deployed committee mean maximum leg weight is **$0.70$**). As a result, KellyBoost suffered sharp drawdowns during 2014–2018 and early 2026, trailing the traditional two-stage "predict-then-optimize" pipeline out of sample.
- **Accidental Shrinkage Dominance:** The classic two-stage pipeline (LightGBM predicting returns with MSE loss $\to$ quadratic Kelly QP with sample covariance) produces near-zero expected return forecasts due to low $R^2$ in monthly asset returns. Fed with near-zero forecasts, the QP optimizer holds a diversified book. This accidental shrinkage outperforms unconstrained end-to-end Kelly learners out of sample.
- **Feature Search Overfitting:** Expanding the candidate pool to 7,871 features doubled development selection scores for all methods, but failed to improve deployed performance for end-to-end models (both MLPs' searched feature sets deployed worse than their hand-built feature baselines).

## Falsification plan

1. **Transaction Cost Degradation Test:** Evaluate KellyBoost under realistic execution slippage and fees ranging from 5 bps to 50 bps. If annualized turnover exceeds $12\times$ or if net geometric growth falls below a naive $1/N$ equal-weight benchmark, the hypothesis that decision-focused loss minimizes trading churn is falsified.
2. **Explicit Shrinkage / Fractional Kelly Ablation:** Train KellyBoost with the CRRA parameter $\gamma \in \{2, 3, 5, 10\}$ and compare against unconstrained $\gamma = 1$. If fractional Kelly dampening fails to reduce maximum drawdown by at least $25\%$ while matching or exceeding the two-stage pipeline's Sharpe ratio, the failure is structural to decision-focused trees rather than full-Kelly risk preferences.
3. **Sub-Period Stress Analysis:** Split the 2013–2026 evaluation window into distinct macroeconomic regimes (2013–2019 low-vol growth, 2020 COVID shock, 2022 inflation/rate tightening, 2023–2026 AI expansion). If KellyBoost generates negative excess returns over cash in more than two out of four regimes, the multi-output conditioning is falsified as unstable.
4. **Rejection Threshold:** Reject the model if paired bootstrap probability $\Pr(\Delta > 0)$ against the multiclass surrogate drops below $0.80$ under 10 bps transaction costs, or if annualized maximum drawdown exceeds $35\%$.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Cross-Sectional Spot & Perpetual Baskets:** The multi-output GBDT architecture can be applied to allocate across major liquid crypto assets (BTC, ETH, SOL, BNB, AVAX, LINK, SUI) plus a USD stablecoin leg (USDT/USDC).
- **Compounding Frequency & Horizon Adjustment:** The 20-day monthly rebalance horizon in traditional equities must be adapted to a faster cadence (e.g., 8-hour funding cycles or 3-day holding periods) in crypto due to accelerated regime transitions.
- **Asymmetric Drawdown Risk in Crypto:** The logarithmic loss $-\log(1+w^\top y)$ approaches $+\infty$ as $w^\top y \to -1$. In crypto, flash crashes and token liquidations can easily produce $-50\%$ to $-90\%$ single-asset drawdowns. Softmax long-only weights do not eliminate bankruptcy risk if a leg approaches zero; an explicit safety barrier $\epsilon_{\text{cash}} \ge 0.10$ or fractional Kelly tuning ($\gamma \ge 3$) is mandatory.
- **Execution Frictions:** Funding rate carry on perpetual futures and exchange taker fees ($2\text{--}5$ bps) will erode performance if turnover exceeds $10\times$ annually.

## Limitations

- **Simplex-Only Action Space:** The formulation is restricted to long-only, fully invested allocations; short selling and dynamic borrowing leverage are not incorporated into the softmax parameterization.
- **High Sensitivity to Estimation Error:** As demonstrated in the paper's negative results, unconstrained full-Kelly optimization amplifies estimation error, requiring manual tuning of the risk-aversion parameter $\gamma$ or artificial regularizers.
- **Scaling Bottleneck in Large Universes:** Softmax parameterization over hundreds of assets ($K > 100$) dilutes individual logits ($O(1/K)$), requiring hierarchical or grouped tree structures.
- **Look-Ahead Peek in Original Paper Design:** The paper authors disclose that the evaluation segment was examined once before introducing the automated feature search; however, this disclosure strengthens the negative finding that feature search did not repair out-of-sample concentration.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/fractional-kelly-2026-08-28]]`
- `[[quant/expected-shortfall-and-risk-of-ruin-2026-08-28]]`
- `[[quant/dynamic-portfolio-optimization-cvar-stochastic-control-hjb-2026-09-02]]`
- `[[quant/wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02]]`
- `[[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]`

## Sources

1. Jiayu Li, *"KellyBoost: Growth-Optimal Portfolio Construction with Gradient-Boosted Trees"*, arXiv preprint `arXiv:2608.23393v1 [q-fin.PM, cs.LG]`, August 24, 2026. DOI: [10.48550/arXiv.2608.23393](https://doi.org/10.48550/arXiv.2608.23393). Stable URL: [https://arxiv.org/abs/2608.23393](https://arxiv.org/abs/2608.23393).
2. John L. Kelly, *"A New Interpretation of Information Rate"*, *Bell System Technical Journal*, 35(4):917–926, 1956.
3. Leo Breiman, *"Optimal Gambling Systems for Favorable Games"*, *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability*, 1:65–78, 1961.
4. Adam N. Elmachtoub and Paul Grigas, *"Smart 'Predict, then Optimize'"*, *Management Science*, 68(1):9–26, 2022.
