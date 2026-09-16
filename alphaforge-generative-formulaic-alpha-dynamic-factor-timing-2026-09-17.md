---
schema: strategy-research-record-v1
title: "AlphaForge Generative Formulaic Alpha Mining and Dynamic Factor Timing"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-06-27
sources:
  - https://arxiv.org/abs/2406.18394
  - https://github.com/DulyHao/AlphaForge
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaForge Generative Formulaic Alpha Mining and Dynamic Factor Timing

## Provenance

- **Primary Source:** Hao Shi, Cuicui Luo, Weili Song, Xinting Zhang, Xiang Ao, *"AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors"*, arXiv preprint `arXiv:2406.18394v1 [cs.CE]`, submitted June 27, 2024 (accepted at AAAI 2025).
- **Canonical arXiv URL:** https://arxiv.org/abs/2406.18394
- **Official Open-Source Repository:** https://github.com/DulyHao/AlphaForge
- **Immutable Commit SHA:** `d0cfc27df23c60f271bc885fd43027b86b787746`
- **Primary Code Paths:** `train_AFF.py`, `combine_AFF.py`, `gan/network/generater.py`, `gan/network/predictor.py`, `gan/network/masker.py`
- **Institutional Affiliations:** University of Chinese Academy of Sciences (School of Computer Science & Technology; International College); Renaissance Era Investment Management Co., Ltd; University of Nottingham; Institute of Computing Technology, Chinese Academy of Sciences.
- **Deduplication Audit:** A comprehensive search of the repository confirmed no existing record for canonical arXiv `2406.18394` or the `DulyHao/AlphaForge` repository. While the name "AlphaForge" appeared in comparative baseline tables in two later factor-discovery records (`alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05.md` and `alphalogics-market-logic-multi-agent-factor-generation-2026-09-05.md`), no prior record captures the generative-predictive formulaic mining framework, its surrogate scoring mechanism, or its dynamic factor-timing and OLS combination methodology.

## Economic mechanism

### Source-reported

Financial time-series data suffers from low signal-to-noise ratios and continuous factor decay: widely known hand-crafted factors lose predictive power due to crowding, while market regimes and style rotations cyclically invert factor efficacy. Traditional formulaic alpha discovery methods (genetic programming, tree mutation) explore factor spaces inefficiently. Recent reinforcement learning methods discover synergistic factor pools, but bind them into fixed linear combinations with static weights. Because individual alpha factors experience cyclical drawdowns and periodic sign reversals, static factor combinations inevitably suffer when previously winning factors reverse.

AlphaForge addresses this via a two-stage decoupled architecture:
1. **Generative-Predictive Alpha Mining:** A Deep Convolutional GAN (DCGAN) generator proposes symbolic alpha expressions represented in Reverse Polish Notation (RPN), guided by a differentiable 2D-CNN surrogate predictor that approximates the non-differentiable Information Coefficient (IC) fitness function. A sequence-rule masker and Gumbel-Softmax enforce syntactic validity while allowing gradient backpropagation. A diversity loss penalizes mutual correlation among generated factors, forcing the generator to mine orthogonal factor primitives into a persistent "Factor Zoo".
2. **Dynamic Factor Timing & Combination:** Rather than fixing factor weights, the system leverages factor momentum (Ehsani & Linnainmaa, 2022). At each trading day, the framework evaluates the recent out-of-sample performance of all factors in the Factor Zoo, filters out decaying or unstable factors, selects an optimal subset of top performers, and solves for dynamic Ordinary Least Squares (OLS) weights to forge a daily composite "Mega-Alpha" signal.

### Research interpretation

The core falsifiable thesis decomposes into two distinct mechanisms:
- **Factor Momentum & Dynamic Selection:** Individual formulaic signals (e.g., cross-sectional correlations of volume and price ranges) are not stationary across market cycles. Filtering factors based on recent trailing Rank IC and Rank ICIR selects factors currently aligned with prevailing market liquidity and volatility regimes, mitigating factor drawdown.
- **Adaptive Cross-Sectional Ridge/OLS Synthesis:** Dynamically re-estimating linear combination weights on recent historical cross-sections automatically down-weights or flips the sign of mean-reverting factors and prevents obsolete signals from contaminating the final cross-sectional rank.

Component roles in the hybrid architecture:
- **Search Engine:** DCGAN generator mapping Gaussian latent noise to discrete RPN formula tokens.
- **Fitness Surrogate:** 2D-CNN regression network predicting fitness scores to provide gradient guidance through sparse symbolic search spaces.
- **Diversity Regularizer:** Pairwise return correlation penalty ensuring low inter-factor collinearity within the Factor Zoo.
- **Factor Timing Filter:** Rolling window Rank IC / Rank ICIR thresholding identifying active alpha drivers.
- **Linear Synthesizer:** OLS regression computing dynamic factor combination weights for daily Mega-Alpha formation.
- **Turnover Damper:** Maximum 5-stock daily replacement constraint on top-50 equal-weighted portfolio holdings.

## Signal

### Symbolic Representation & Grammar

Alphas are formalized as expression trees linearized into Reverse Polish Notation (RPN), represented as a one-hot matrix $x \in \{0, 1\}^{D \times S}$, where maximum formula length $S = 20$ and $D$ is the operator/operand vocabulary size.
- **Operands:** Normalized daily features: `open_`, `high`, `low`, `close`, `volume`, `vwap`, plus numerical constants.
- **Unary Operators:** `Abs(x)`, `Log(x)`, `Inv(x)`, `S_log1p(x)`, `CSRank(x)`.
- **Binary Operators:** `+`, `-`, `*`, `/`, `Greater(x, y)`, `Less(x, y)`, `Power(x, y)`.
- **Time-Series Operators:** Parameterized over lookback window $t \in [1, 50]$ days:
  - Rolling moments: `Mean(x, t)`, `Med(x, t)`, `Sum(x, t)`, `Std(x, t)`, `Var(x, t)`, `Max(x, t)`, `Min(x, t)`, `Mad(x, t)`.
  - Trend/Difference: `Delta(x, t)`, `WMA(x, t)`, `EMA(x, t)`, `Pctchange(x, t)`.
  - Higher moments / Risk: `Skew(x, t)`, `Kurt(x, t)`, `IR(x, t)`, `Min_Max_diff(x, t)`.
  - Bivariate cross-features: `Cov(x, y, t)`, `Corr(x, y, t)`.

### Target Optimization Variable

During factor mining, the forward return target is:
$$y_t = \frac{\text{Ref}(\text{VWAP}, -21)}{\text{Ref}(\text{VWAP}, -1)} - 1$$
representing the return of buying at the volume-weighted average price (VWAP) on the day following signal arrival and holding for 20 trading days.

### Factor Zoo Ingestion Criteria

A generated formula $f$ enters the Factor Zoo $\mathcal{Z}$ (size $N = 100$) if and only if:
1. $\text{IC}(f) > 0.03$ (3% Pearson correlation with forward return).
2. $\text{ICIR}(f) > 0.1$ (stability requirement).
3. Maximum pairwise return correlation with any existing factor in $\mathcal{Z}$ satisfies $\max_{g \in \mathcal{Z}} |\text{corr}(\text{ret}_f, \text{ret}_g)| \le 0.50$ (or $0.70$ in `train_AFF.py`).
4. Valid data ratio: finite value ratio $> 0.80$ and unique value ratio $> 0.01$ across cross-sections.

### Dynamic Combination & Daily Mega-Alpha

On each evaluation day $t$:
1. **Lookback Shift:** Trailing metrics are computed strictly over historical window $[0, t - 21]$ (shift of 21 days), preventing lookahead bias from the 20-day forward return target.
2. **Performance Ranking:** For each factor $k \in \mathcal{Z}$, compute trailing mean Rank IC ($\text{ric}_k$) and Rank ICIR ($\text{ricir}_k$). Sort factors descending by $|\text{ricir}_k|$.
3. **Active Selection Gate:** Filter factors satisfying:
   $$\text{ric}_k > 0.02 \quad \text{AND} \quad \text{ricir}_k > 0.20$$
   If no factor meets this criterion, select the top-1 factor by absolute Rank ICIR.
4. **Top-$K$ Slicing:** Select the top $K$ passing factors (source default: $K = 10$).
5. **Dynamic Weight Estimation:** Extract historical factor cross-sections $X \in \mathbb{R}^{M \times (K+1)}$ (including a constant intercept column) and forward returns $Y \in \mathbb{R}^{M \times 1}$ over $[0, t - 21]$. Solve the linear system via least squares:
   $$\hat{\beta}_t = (X^T X)^{-1} X^T Y$$
6. **Mega-Alpha Formation:** Compute out-of-sample cross-sectional score for asset $i$ on day $t$:
   $$\text{MegaAlpha}_{t, i} = \sum_{k=1}^K \hat{\beta}_{t, k} \cdot f_k(X_{t, i}) + \hat{\beta}_{t, 0}$$

## Required data

- **Universe:** China A-share equities: CSI300 (large-cap) and CSI500 (mid/small-cap) constituent stock pools.
- **Venue:** Shanghai and Shenzhen Stock Exchanges (SSE / SZSE).
- **Timeframe:** Daily trading bars (aggregated from official exchange session close).
- **Required Price/Volume Fields:** `open`, `high`, `low`, `close`, `volume`, `vwap`.
- **Target Field:** Daily VWAP forward return 20-day horizon: $\text{Ref}(\text{VWAP}, -21)/\text{Ref}(\text{VWAP}, -1) - 1$.
- **Point-in-Time Availability:** Signals generated strictly after daily close; trade execution mapped to next trading day VWAP. The 21-day backward shift in dynamic combination prevents overlapping target label leakage.
- **Missing Data Handling:** Non-finite values imputed to zero or masked; expression evaluations with $<80\%$ valid cross-sectional points or $<1\%$ unique values are discarded with fitness set to 0.

## Execution assumptions

- **Signal-to-Order Timing:** Signals calculated at daily market close $t$; execution executed on day $t+1$.
- **Fill Benchmark:** Volume-Weighted Average Price (VWAP) across day $t+1$.
- **Portfolio Construction:** Daily top-50 stocks by Mega-Alpha score held in equal weights ($2\%$ per name).
- **Turnover Management:** Hard execution constraint permitting a maximum replacement of 5 stocks per day ($10\%$ maximum daily portfolio turnover) to suppress transaction drag.
- **Transaction Costs & Slippage:** The paper's simulated trading tracks account net value within Qlib. Explicit fee levels are omitted in paper prose; standard Qlib A-share execution assumes $0.15\%$ ($15$ bps) round-trip commission and stamp duty (`research-proposed` standard replication baseline).
- **Shorting / Leverage:** Long-only portfolio (no short selling permitted due to Chinese mainland short-selling constraints); $1.0\times$ gross leverage.

## Evidence

### Source-reported

All figures below are directly cited from Shi et al. (2024), Table 1 and Table 2 (mean across 5 random seeds, standard deviations in parentheses):

#### 1. Out-of-Sample Predictive Metrics (5-Year Walk-Forward 2018–2022)

- **CSI300 Universe:**
  - **GP Baseline:** $\text{IC} = 1.29\% \pm 0.44\%$, $\text{Rank IC} = 2.72\% \pm 0.58\%$, $\text{ICIR} = 0.072 \pm 0.026$, $\text{Rank ICIR} = 0.140 \pm 0.033$.
  - **RL Baseline (Yu et al., 2023):** $\text{IC} = 2.09\% \pm 0.26\%$, $\text{Rank IC} = 2.72\% \pm 0.42\%$, $\text{ICIR} = 0.141 \pm 0.021$, $\text{Rank ICIR} = 0.167 \pm 0.027$.
  - **AlphaForge (Full Model):** $\text{IC} = 4.40\% \pm 0.56\%$, $\text{Rank IC} = 5.89\% \pm 0.69\%$, $\text{ICIR} = 0.368 \pm 0.041$, $\text{Rank ICIR} = 0.454 \pm 0.060$.

- **CSI500 Universe:**
  - **GP Baseline:** $\text{IC} = 0.37\% \pm 0.76\%$, $\text{Rank IC} = 2.34\% \pm 1.07\%$, $\text{ICIR} = 0.024 \pm 0.046$, $\text{Rank ICIR} = 0.124 \pm 0.058$.
  - **RL Baseline:** $\text{IC} = 1.91\% \pm 0.49\%$, $\text{Rank IC} = 4.03\% \pm 0.62\%$, $\text{ICIR} = 0.152 \pm 0.042$, $\text{Rank ICIR} = 0.286 \pm 0.056$.
  - **AlphaForge (Full Model):** $\text{IC} = 2.84\% \pm 0.58\%$, $\text{Rank IC} = 5.57\% \pm 0.58\%$, $\text{ICIR} = 0.212 \pm 0.043$, $\text{Rank ICIR} = 0.386 \pm 0.042$.

#### 2. Ablation Study: Generative Mining vs. Dynamic Timing (Table 2)

- **CSI300 Static Combination (AlphaForge Mining + RL Static Combination):**
  - $\text{IC} = 2.43\% \pm 0.57\%$, $\text{Rank IC} = 3.67\% \pm 0.46\%$, $\text{ICIR} = 0.144 \pm 0.036$, $\text{Rank ICIR} = 0.204 \pm 0.029$.
  - Comparing Static ($2.43\%$ IC) vs. RL baseline ($2.09\%$ IC) confirms that generative-predictive mining alone improves factor generation over RL.
  - Comparing Dynamic ($4.40\%$ IC) vs. Static ($2.43\%$ IC) demonstrates that dynamic factor timing provides a $+1.97\%$ absolute IC uplift ($+81\%$ relative gain).

- **CSI500 Static Combination:**
  - $\text{IC} = 2.05\% \pm 0.29\%$, $\text{Rank IC} = 4.48\% \pm 0.46\%$, $\text{ICIR} = 0.180 \pm 0.040$, $\text{Rank ICIR} = 0.336 \pm 0.056$.
  - Dynamic combination ($2.84\%$ IC, $5.57\%$ Rank IC) similarly outperforms Static ($2.05\%$ IC, $4.48\%$ Rank IC).

#### 3. Factor Pool Sensitivity (Figure 3)

Varying the maximum pool size across $K \in \{1, 10, 20, 50, 100\}$ reveals a distinct non-monotonic concavity: peak performance occurs at $K = 10$, while expanding the pool to $50$ or $100$ leads to degraded performance due to inclusion of noisy or correlated factors.

#### 4. Simulated Trading Performance (Figure 4)

In Qlib simulated trading on CSI300 (top-50 equal-weighted, 5-stock daily change limit, 2018–2022), AlphaForge achieved the highest cumulative net asset value across all evaluated methods, outperforming RL, GP, and buy-and-hold index benchmarks over the 5-year evaluation window.

### Independently reproduced

Not independently reproduced. The official codebase at commit `d0cfc27df23c60f271bc885fd43027b86b787746` was cloned and audited for consistency with paper claims; execution of the full 5-year GPU retraining workflow has not been executed in our local environment.

### Negative evidence

- **Diminishing Returns of Zoo Expansion:** Increasing the active combination pool beyond 10 factors degrades both IC and ICIR, showing that large factor libraries introduce collinearity and estimation noise unless strictly regularized.
- **Underperformance of Static Ensembles:** Static factor weights lose more than $40\%$ of the predictive Information Coefficient compared to dynamic weights, demonstrating that formulaic alphas in equity markets suffer from rapid non-stationarity.
- **Asymmetric Execution Friction:** The primary evaluation restricts portfolios to long-only top-50 holdings; performance of an unconstrained long-short dollar-neutral implementation subject to short-borrow fees in A-shares remains unexamined.
- **Absence of Crypto Empirical Testing:** Zero empirical evidence is provided for cryptocurrency markets in the cited source.

## Falsification plan

To falsify the claim that AlphaForge's generative-predictive mining and dynamic factor timing produce genuine, robust predictive alpha:

1. **Walk-Forward Holdout Evaluation:** Test on post-2022 Chinese equity data (2023–2026) and US equities (S&P 500, Russell 2000). 
   - *Research-defined falsification threshold:* Reject the hypothesis if out-of-sample 20-day forward Rank IC drops below $0.015$ or Rank ICIR falls below $0.15$.
2. **Factor Momentum vs. Random Selection Ablation:** Compare AlphaForge's dynamic Rank IC/Rank ICIR selection against:
   - (a) Uniform random selection of 10 factors from the Factor Zoo;
   - (b) Inverse-momentum selection (choosing the lowest trailing Rank ICIR factors);
   - (c) Static equal-weighted average of all 100 Zoo factors.
   - *Research-defined falsification threshold:* Reject the dynamic factor-timing hypothesis if the active selection gate does not outperform the equal-weighted 100-factor static baseline by at least $+0.50\%$ Rank IC out-of-sample.
3. **Execution Cost Stress Test:** Subject the top-50 portfolio with 5-stock daily turnover constraint to realistic fee grids:
   - Apply $5$, $10$, $15$, and $25$ bps one-way transaction costs plus $5$ bps execution slippage.
   - *Research-defined falsification threshold:* Reject tradability if net annualized Sharpe ratio drops below $0.50$ at $15$ bps one-way friction.
4. **Target Leakage / Shift Verification:** Remove the 21-day evaluation shift in `combine_AFF.py`. If reported performance collapses or explodes, audit for implicit target lookahead in rolling metrics.
5. **Universe Transfer & Placebo Test:** Permute stock identifiers across the cross-section (scrambled cross-sectional placebo). The resulting Rank IC must be strictly zero.

## Crypto portability

**Status:** `adapted/unproven`

The primary paper conducts research strictly on Chinese equities (CSI300 and CSI500). Porting AlphaForge to cryptocurrency markets represents a research interpretation and faces substantial structural adaptations:

- **Trading Session & Candle Boundaries:** Equities observe distinct market open/close and auction-derived VWAP. Crypto trades 24/7/365 across fragmented venues (Binance, OKX, Bybit, Hyperliquid). Adapting the 20-day horizon ($y_t$) requires fixing standardized UTC midnight candle boundaries and volume-weighted execution windows.
- **Perpetual Funding Rate Drag:** In equity spot markets, holding positions for 20 days incurs only opportunity costs. In crypto perpetual swaps, maintaining a multi-week position exposes the trader to cumulative funding payments that can easily exceed $10\%–30\%$ annualized. The forward target return must be explicitly adjusted:
  $$y_t^{\text{crypto}} = \frac{\text{Ref}(\text{VWAP}, -21)}{\text{Ref}(\text{VWAP}, -1)} - 1 - \sum_{\tau=1}^{20} \text{FundingRate}_\tau \quad (\text{research-proposed})$$
- **Universe Breadth & Liquidity Dispersion:** CSI300 offers 300 highly liquid equities with comparable capitalization. The crypto perpetual universe exhibits severe Pareto skew: BTC and ETH dominate volume, while small-cap altcoins suffer high taker fees, thin order books, and severe market impact. An adapted crypto universe should be restricted to the top 30–50 perpetual contracts by 30-day average dollar volume (`research-proposed`).
- **Two-Sided Long/Short Implementation:** Unlike A-shares, crypto perpetuals support frictionless shorting. A dollar-neutral long/short portfolio (top quintile long, bottom quintile short) is naturally implementable, but short positions are vulnerable to sudden liquidation short-squeezes.

## Limitations

- **Omission of Explicit Fee Assumptions in Paper Prose:** The primary manuscript presents cumulative net value graphs without documenting the exact basis-point transaction fee or slippage model used in the Qlib simulation environment (`provenance gap`).
- **Sparse Factor Zoo Entry:** The hard correlation threshold ($\text{corr} \le 0.50$) causes factor admission to become exponentially difficult as the zoo grows, which may leave later candidate slots unfilled or sensitive to generation order.
- **Linear Combination Simplicity:** Dynamic weights are estimated via unregularized OLS (`torch.linalg.lstsq`), which can become unstable when selected factors exhibit transient multicollinearity. Ridge or Lasso regularization would provide greater numerical stability (`research-proposed`).
- **Non-Crypto Origin:** Entirely unproven in digital asset markets.
- **Implementation Status:** Not implemented in our production or backtesting stack.

## Implementation status

`not-implemented`

No implementation of AlphaForge's generative-predictive factor mining pipeline or dynamic factor timing has been integrated into `nautilus-quant-system`, PyBroker, NautilusTrader, paper trading, or live execution. This record serves strictly as a normalized research capture.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

A record being present in this repository does not indicate that the strategy is profitable, validated, or approved for implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05]]` — Comparative formulaic alpha generation framework citing AlphaForge as a baseline benchmark.
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05.md]]` — Multi-agent market logic factor generation benchmarked against AlphaForge.
- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — Grammar-guided formulaic alpha mining using MCTS and Tree-LSTM.
- `[[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]` — Surrogate-guided factor mining in semantic plan spaces.

## Sources

1. **Primary Paper:** Hao Shi, Cuicui Luo, Weili Song, Xinting Zhang, Xiang Ao. *"AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors"*. arXiv preprint `arXiv:2406.18394v1 [cs.CE]`, June 27, 2024. https://arxiv.org/abs/2406.18394
2. **Official Code Repository:** Hao Shi et al. *"AlphaForge Framework Implementation"*, GitHub repository: https://github.com/DulyHao/AlphaForge, commit `d0cfc27df23c60f271bc885fd43027b86b787746`.
3. **Foundational Factor Momentum:** Sina Ehsani, Juhani T. Linnainmaa. *"Factor Momentum and the Momentum Factor"*. The Journal of Finance, 77(3), 1877–1919, 2022. https://doi.org/10.1111/jofi.13131
4. **Baseline Synergistic RL:** Shuo Yu, Hongyan Xue, Xiang Ao, Feiyang Pan, Jia He, Dandan Tu, Qing He. *"Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning"*. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '23), 5476–5486, 2023. https://doi.org/10.1145/3580305.3599831
