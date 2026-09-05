---
schema: strategy-research-record-v1
title: "AlphaSchema: Structured Trading-Semantic Plan Space Exploration and Surrogate-Guided Evolution for Automated Alpha Mining"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - alpha-mining
  - llm-agents
  - semantic-plans
  - surrogate-optimization
  - lightgbm
  - cross-sectional-equity
  - csi300
status: research-only
confidence: medium
source_as_of: "2026-07-29"
sources:
  - "Jingyang Yi, Jian Yang, Yifei Jin, Yuqi Li, and Jian Li, 'AlphaSchema: Exploring the Space of Trading Semantics for LLM-Based Alpha Mining', arXiv preprint arXiv:2607.26642v1 [cs.AI], July 29, 2026. https://arxiv.org/abs/2607.26642"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaSchema: Structured Trading-Semantic Plan Space Exploration and Surrogate-Guided Evolution for Automated Alpha Mining

## Provenance

- **Title:** AlphaSchema: Exploring the Space of Trading Semantics for LLM-Based Alpha Mining
- **Authors:** Jingyang Yi (1), Jian Yang (1), Yifei Jin (1), Yuqi Li (2, 3), and Jian Li (4)
- **Affiliations:** (1) X-Tech, Xtech-PandaAI-Waton Joint Lab; (2) Monash University; (3) PandaAI; (4) Institute for Interdisciplinary Information Sciences (IIIS), Tsinghua University
- **Preprint Identifier:** arXiv:2607.26642v1 [cs.AI], submitted July 29, 2026 (`source-reported`)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2607.26642](https://doi.org/10.48550/arXiv.2607.26642) (`source-reported`)
- **Canonical Abstract URL:** [https://arxiv.org/abs/2607.26642](https://arxiv.org/abs/2607.26642)
- **Canonical Full-Text HTML URL:** [https://arxiv.org/html/2607.26642v1](https://arxiv.org/html/2607.26642v1)
- **Canonical PDF URL:** [https://arxiv.org/pdf/2607.26642](https://arxiv.org/pdf/2607.26642)
- **Subject Classification:** Artificial Intelligence (`cs.AI`) (`source-reported`)
- **Primary Source Inspection:** Audited directly from the complete 24-page primary preprint manuscript of `arXiv:2607.26642v1`, including the formal semantic grammar formulation (Section 2 & 3, Appendix C), closed-loop surrogate optimization loop (Section 3), empirical backtests on CSI300 and CSI500 (Section 4 & Appendix B), component-level ablation studies (Section 5, Table 6), surrogate predictability proofs and experiments (Appendix E, Table 7), and backend model robustness audits across seven distinct LLM engines (Table 8).
- **Pre-Write Deduplication & Identity Verification:** An exhaustive scan across the repository confirmed that `arXiv:2607.26642` has zero existing strategy records in `alpha-strategy-research`. The framework was referenced only in passing as an inspiration for an LLM sensitivity test in a multi-market equity selection record (`multimarket-senseai-multi-agent-llm-regime-adaptive-equity-selection-2026-09-04.md`). Existing agentic factor-mining records in this repository explore evolutionary program generation (`quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md`), market logic prompting (`alphalogics-market-logic-multi-agent-factor-generation-2026-09-05.md`), or MCTS trajectory evolution (`navigating-the-alpha-jungle-mcts-2026-09-02.md`). None represent candidate factors as a 5-dimensional structured semantic tuple $(e, c, Q, d, o)$ decoupled from code realization, nor do they maintain an explicit offline tabular surrogate model (LightGBM) over discrete semantic schema features to guide exploration, exploitation, and mutation budgets.

## Economic mechanism

### Source-reported

Automated alpha mining has transitioned from symbolic formulaic search (genetic programming, operator trees) to Large Language Model (LLM) agents. However, conventional LLM-based agent systems couple hypothesis generation, search-space navigation, and code-level realization inside the LLM agent itself. Consequently, the candidate search space is shaped implicitly by stochastic prompts, memory traces, and model-specific proposal biases, making exploration difficult to measure, coverage hard to control, and search trajectories challenging to reproduce or optimize systematically.

To solve this coupling, **AlphaSchema** decouples *what to search* (trading semantics) from *how to implement it* (executable code):
1. **Trading-Semantic Abstraction:** Candidate factors are represented as structured plans before code realization, spanning five explicit functional dimensions:
   - **Event ($e$):** The primary market phenomenon or signal-generating event (e.g., breakout, volume expansion, volatility compression, effort-result divergence) (`source-reported`).
   - **Context ($c$):** The conditioning market state or reference benchmark (e.g., VWAP distance, moving average distance, volatility regime, cross-sectional quantile) (`source-reported`).
   - **Qualities ($Q$):** Zero to three validation or filtering constraints (e.g., event cooldown filter, volume confirmation, multi-window range-efficiency alignment, outlier filter) (`source-reported`).
   - **Direction ($d$):** The hypothesized directional relationship with future returns (continuation, reversal, or range oscillation) (`source-reported`).
   - **Output ($o$):** The mathematical formulation of the tradable signal (continuous score, event decay, cross-sectional rank, bounded continuous transformation) (`source-reported`).
2. **Surrogate-Guided Navigation:** Realized factor evaluations provide supervision over the discrete semantic space. By training a LightGBM surrogate reward model over structured schema features, the system learns reusable priors about which economic mechanisms produce persistent alpha before generating code (`source-reported`).
3. **Adaptive Quota Search:** A multi-armed exploration schedule balances global structural exploration (favoring rare event-context pairings), surrogate exploitation (selecting top-predicted plans), and local mutation (perturbing single schema fields of high-reward parents) (`source-reported`).

### Research interpretation

The economic foundation of AlphaSchema rests on **hypothesis-first factor engineering and variance reduction across stochastic code realizations**:
1. **Semantic Separation from Implementation Noise:** In traditional formulaic mining, two identical economic ideas (e.g., volume-confirmed price breakout above 20-day high) can take hundreds of syntactically distinct mathematical forms with different operators, smoothing windows, and scalings. Conversely, LLMs often invent mathematically complex formulas that lack any coherent economic intuition. By forcing the search algorithm to navigate a bounded, economically grounded semantic vocabulary ($\sim 7.0 \times 10^8$ potential valid combinations), the search space is constrained to interpretable market mechanisms (`research-proposed`).
2. **Feature-Level Pooling of Noisy Code Feedback:** A single code realization of a semantic plan is a noisy sample of that plan's latent quality due to LLM operator choices and finite-sample backtest noise. However, because individual schema components (events, contexts, qualities) recur across thousands of plans, an offline gradient-boosted decision tree surrogate pools these noisy observations at the feature level, identifying which structural components (such as multi-window efficiency alignment and event cooldowns) consistently enhance risk-adjusted returns (`research-proposed`).
3. **Overfitting Risks in Combiner Layer:** Although individual semantic factors are screened for look-ahead leakage and low cross-correlation ($\le 0.70$), combining 120–150 factors using a 500-tree LightGBM model on daily equity data creates severe risk of backtest overfitting and hyperparameter tuning bias. The reported Information Ratios ($> 1.0$) and Annualized Excess Returns ($> 11\%$) must be treated as upper-bound laboratory figures subject to decay under live execution slippage and regime transitions (`research-proposed`).

## Signal

### Mathematical Specification of the Semantic Space

A candidate trading plan $p \in \mathcal{P}$ is formally defined as a 5-tuple:
$$p = (e, c, Q, d, o) \in \mathcal{V}_E \times \mathcal{V}_C \times \mathcal{Q}_{\text{set}} \times \mathcal{V}_D \times \mathcal{V}_O \quad \text{(`source-reported`)}$$
where:
- $\mathcal{V}_E$ is the Event vocabulary ($|\mathcal{V}_E| = 40$) (`source-reported`).
- $\mathcal{V}_C$ is the Context vocabulary ($|\mathcal{V}_C| = 40$) (`source-reported`).
- $\mathcal{Q}_{\text{set}} = \bigcup_{k=0}^3 \{ Q \subseteq \mathcal{V}_Q \mid |Q| = k \}$ represents admissible quality sets containing 0 to 3 constraints from $|\mathcal{V}_Q| = 50$ items (`source-reported`).
- $\mathcal{V}_D$ is the Direction vocabulary ($|\mathcal{V}_D| = 3$: continuation, reversal, range oscillation) (`source-reported`).
- $\mathcal{V}_O$ is the Output vocabulary ($|\mathcal{V}_O| = 7$: continuous score, event decay, cross-sectional rank, bounded continuous, persistent condition, etc.) (`source-reported`).

Total discrete price-volume search space size:
$$|\mathcal{P}| = 40 \times 40 \times \left( \sum_{k=0}^3 \binom{50}{k} \right) \times 3 \times 7 = 1600 \times (1 + 50 + 1225 + 19600) \times 21 = 701,433,600 \text{ unique plans} \quad \text{(`source-reported`)}$$

### Realization & Evaluation Reward Function

Each selected plan $p$ is translated by a code agent (default: DeepSeek-V4-Flash) into two executable realizations: a fast time-scale factor $f_{p,\text{fast}}$ and a slow time-scale factor $f_{p,\text{slow}}$ (`source-reported`).
For each realization $f_{p,s}$ ($s \in \{\text{fast}, \text{slow}\}$), the search reward is computed as:
$$r_{p,s} = \alpha \cdot \text{RankIC}(f_{p,s}) + \beta \cdot \text{Corr}(f_{p,s}, L_1 f_{p,s}) - \lambda \cdot |\text{RankIC}(f_{p,s}) - \text{RankIC}(L_1 f_{p,s})| \quad \text{(`source-reported`)}$$
where:
- $\text{RankIC}(f)$ is the Spearman rank correlation between factor score and 5-day forward return label (`source-reported`).
- $\text{Corr}(f, L_1 f)$ measures autocorrelation / temporal stability of the signal (penalizing hyper-turnover) (`source-reported`).
- $|\text{RankIC}(f) - \text{RankIC}(L_1 f)|$ measures lag sensitivity (penalizing signals that vanish upon 1-day execution delay) (`source-reported`).
- Parameter coefficients: $\alpha = 10$, $\beta = 1$, $\lambda = 2$ (`source-reported`).
- Overall plan reward: $r(p) = \max_{s \in \{\text{fast}, \text{slow}\}} r_{p,s}$ (`source-reported`).
- If an implementation fails validation checks (syntax, division by zero, look-ahead leakage) after one repair attempt, it receives $r(p) = 0.0$ as a feasibility penalty (`source-reported`).

### Adaptive Quota Search Mechanism

Each search round evaluates a batch of $B = 16$ plans across 80 rounds ($T=80$, total 1,280 evaluated plans) (`source-reported`):
1. **Cold Start (Rounds 1–10):** 100% of batch allocated to structural exploration ($\rho_t = 1.0$) (`source-reported`).
2. **Post-Cold Start (Rounds 11–80):** Exploration quota decays exponentially:
   $$\rho_t = \rho_{\min} + (\rho_{\max} - \rho_{\min}) e^{-n_t / \tau} \quad \text{(`source-reported`)}$$
   The remaining budget $(1 - \rho_t)$ is divided equally between surrogate-guided exploitation and local mutation (`source-reported`).
3. **Selection Operators:**
   - **Structural Exploration:** Ranks sampled candidates by coverage novelty:
     $$\nu(p) = \frac{1}{\sqrt{N_E(e) + 1}} + \frac{1}{\sqrt{N_C(c) + 1}} + \frac{2}{\sqrt{N_{EC}(e,c) + 1}} \quad \text{(`source-reported`)}$$
   - **Surrogate Exploitation:** Evaluates 10,000 sampled plans using the LightGBM surrogate model trained on all accumulated buffer entries, selecting top $\hat{r}_t(p)$ plans (`source-reported`).
   - **Local Mutation:** Takes top-performing parent plans and applies single-field mutations with empirical probabilities: replace quality (0.22), replace context (0.16), replace output (0.16), add quality (0.14), drop quality (0.12), replace direction (0.12), replace event (0.08) (`source-reported`).

### Downstream Trading Strategy Architecture

- **Factor Pool Selection:** Greedy reward-ranked filtering enforcing pairwise correlation constraint:
  $$\max_{g \in \mathcal{S}} |\text{Corr}(f, g)| \le \gamma = 0.70 \quad \text{(`source-reported`)}$$
  Yields a 120-factor OHLCV pool, or 150 factors when augmented with 30 fundamental schema factors (`source-reported`).
- **Ensemble Ranker:** LightGBM regressor (500 boosting trees, learning rate tuned on validation set, early stopping = 50 rounds) mapping cross-sectional factor vector $\mathbf{x}_{i,t} \in \mathbb{R}^K$ to forward 5-day return score $\hat{y}_{i,t}$ (`source-reported`).
- **Portfolio Construction:** Qlib `TopkDropoutStrategy` with `topk = 50`, `n_drop = 5` (`source-reported`):
  - Equal weighting across top 50 ranked stocks (`source-reported`).
  - Daily rebalancing: holdings falling outside the top tier are replaced, with at most 5 stocks replaced per day to minimize portfolio turnover (`source-reported`).
  - Execution price: Open price of trading day $t+1$ (`deal_price = open`) (`source-reported`).
  - Limit-up/limit-down protection: Excludes purchases of stocks reaching $+9.5\%$ price limit (`source-reported`).

## Required data

- **Universe:** China A-Share CSI300 index constituents (primary benchmark: `SH000300`), with secondary validation on CSI500 (`SH000905`) (`source-reported`).
- **Sample Period:**
  - In-Sample Training: January 1, 2016 to December 31, 2020 (5 years) (`source-reported`).
  - Validation: January 1, 2021 to December 31, 2022 (2 years) (`source-reported`).
  - Out-of-Sample Test: January 1, 2023 to December 31, 2025 (3 years) (`source-reported`).
- **Timeframe:** Daily bars (`1d` frequency) (`source-reported`).
- **Required OHLCV Fields:** Open, High, Low, Close, Volume, VWAP (`source-reported`).
- **Fundamental Fields (+Fundamental setting):** Financial statement indicators, earnings surprises, valuation ratios (`source-reported`).
- **Point-in-Time Integrity:** Signals formed at close of day $t$; orders executed at open of day $t+1$; strict look-ahead leakage screening applied before backtesting (`source-reported`).
- **Missing Data Handling:** Suspended stocks, illiquid trading halts, and non-trading days filtered out; rank normalization applied cross-sectionally daily (`source-reported`).

## Execution assumptions

- **Execution Timing:** Market orders executed at the open price of day $t+1$ (`deal_price = open`) (`source-reported`).
- **Transaction Costs & Slippage:**
  - Buy commission & slippage: $0.05\%$ ($5\text{ bps}$) (`source-reported`).
  - Sell commission, stamp duty & slippage: $0.15\%$ ($15\text{ bps}$) (`source-reported`).
  - Total round-trip transaction friction: $\sim 0.20\%$ ($20\text{ bps}$), subject to a minimum fee of 5 currency units per trade (`source-reported`).
- **Turnover Control:** Constrained by `n_drop = 5` limit, capping maximum daily portfolio turnover at $10\%$ ($5/50$) of portfolio equity under normal conditions (`source-reported`).
- **Shorting / Borrow Restrictions:** Long-only portfolio equity allocation; China A-share short-selling restrictions respected (no naked shorting) (`source-reported`).
- **Capacity & Participation:** CSI300 constituents represent large-cap institutional equities ($> \$1\text{B}$ market cap); capacity is substantial ($> \$50\text{M}$ AUM) before market impact degrades 5-day holding periods (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below are transcribed directly from Yi et al. (`arXiv:2607.26642v1`, July 29, 2026), evaluated over the held-out test window (January 1, 2023 to December 31, 2025) on CSI300:

#### 1. Main Comparative Results on CSI300 (Table 1)

| Category | Model / Method | Fund. Schema | IC | ICIR | Rank IC | Rank ICIR | Information Ratio (IR) | Annualized Excess Return (AER %) | Max Drawdown (MDD %) ↓ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ML Predictor** | MLP | ✗ | 0.0236 | 0.1408 | 0.0389 | 0.2471 | 0.5901 | 5.16% | 11.47% |
| **ML Predictor** | XGBoost | ✗ | 0.0284 | 0.2024 | 0.0373 | 0.2699 | 0.3556 | 2.55% | 10.30% |
| **Deep Sequence** | Transformer | ✗ | 0.0289 | 0.1561 | 0.0507 | 0.2775 | 0.6929 | 6.14% | 12.03% |
| **Deep Sequence** | GRU | ✗ | 0.0310 | 0.1782 | 0.0565 | 0.3242 | 0.4609 | 3.73% | 13.21% |
| **Deep Sequence** | LSTM | ✗ | 0.0380 | 0.2269 | **0.0587** | **0.3521** | 0.6317 | 5.14% | 11.51% |
| **Factor Library** | Alpha158 | ✗ | 0.0347 | 0.2081 | 0.0504 | 0.3009 | 0.5474 | 4.36% | 15.87% |
| **Factor Library** | Alpha360 | ✗ | 0.0231 | 0.1710 | 0.0292 | 0.2100 | 0.4024 | 2.99% | **8.86%** |
| **Agentic Mining** | RD-Agent (NeurIPS '26) | ✗ | 0.0242 | 0.1494 | 0.0504 | 0.3094 | 0.9861 | 6.81% | 15.57% |
| **Agentic Mining** | QuantaAlpha (arXiv '26) | ✗ | 0.0208 | 0.1619 | 0.0380 | 0.2934 | 0.6726 | 5.57% | 14.18% |
| **Proposed** | **AlphaSchema (OHLCV, 120)** | ✗ | **0.0382** | **0.2374** | 0.0498 | 0.2912 | 0.7624 | 8.53% | 18.63% |
| **Proposed** | **AlphaSchema (+Fund., 150)**| ✓ | 0.0380 | 0.2365 | 0.0487 | 0.2857 | **1.0877** | **11.94%** | 15.43% |

- **Key Performance Takeaways:**
  - AlphaSchema (OHLCV) achieves the highest linear correlation metrics among all methods: IC = 0.0382 and ICIR = 0.2374 (`source-reported`).
  - AlphaSchema (+Fund.) achieves the highest benchmark-relative risk-adjusted portfolio return: IR = 1.0877, AER = +11.94% net of transaction costs, outperforming RD-Agent (0.9861 IR, 6.81% AER) and QuantaAlpha (0.6726 IR, 5.57% AER) (`source-reported`).
  - Factor decay analysis (Figure 8) reveals that AlphaSchema factor pool outperformed Alpha158 on 466 of 467 valid test-period rolling dates, maintaining a mean rolling Rank IC advantage of +0.0149 (`source-reported`).

#### 2. Component Ablation on 100 Schema Plans (Table 6)

| Variant | Removed Field | Validity Rate | Mean \|Rank IC\| | Relative Retained (%) | Mean Reward |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **AlphaSchema (Full)** | None | 100/100 (100%) | **0.0185** | **100.0%** | **4.174** |
| w/o Event | Event ($e$) | 93/100 (93%) | 0.0147 | 78.9% | 2.199 |
| w/o Context | Context ($c$) | 94/100 (94%) | 0.0131 | 69.4% | 2.249 |
| w/o Qualities | Qualities ($Q$) | 95/100 (95%) | 0.0134 | 72.9% | 2.483 |
| w/o Direction | Direction ($d$) | 88/100 (88%) | 0.0134 | 71.7% | 2.219 |
| w/o Output | Output ($o$) | 96/100 (96%) | 0.0141 | 75.1% | 2.310 |

- **Ablation Interpretation:** Removing any semantic dimension results in a 21.1% to 30.6% drop in absolute Rank IC, proving that all five dimensions supply essential, complementary market structure (`source-reported`).

#### 3. LLM Code Backend Robustness (Table 8)

| Backend Model | Pass@1 Rate | Repair Needed | Final Valid | Mean \|Rank IC\| | Mean Rank IC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **GPT-5.4** | 97/100 | 2 | 99/100 | 0.0116 | 0.0040 |
| **GPT-5.4-mini** | 81/100 | 10 | 91/100 | 0.0129 | 0.0073 |
| **Kimi-K2.7-Code** | 82/100 | 10 | 92/100 | 0.0138 | 0.0075 |
| **Claude Opus 4.6** | 94/100 | 3 | 97/100 | 0.0157 | 0.0113 |
| **DeepSeek-V4-Flash** | 63/100 | 30 | 93/100 | **0.0168** | **0.0121** |
| **Qwen3.6-Flash** | 49/100 | 40 | 89/100 | 0.0161 | 0.0115 |
| **GLM-5.2** | 75/100 | 22 | 97/100 | 0.0145 | 0.0109 |

- **Model Invariance:** While Pass@1 code execution ranges from 49% (Qwen3.6-Flash) to 97% (GPT-5.4), the mean absolute Rank IC of realized factors across all seven LLMs remains tightly clustered between 0.0116 and 0.0168. This confirms that factor alpha is primarily governed by the semantic schema plan rather than the specific LLM generating the code (`source-reported`).

#### 4. Concrete Exemplar Factor Performance (Appendix D, Table 3)

- **Semantic Plan:** Effort-result breakout rank ($e$) + reference distance rank ($c$) + event cooldown filter ($Q$) + continuation ($d$) + event decay memory ($o$) (`source-reported`).
- **5-Day Open-to-Open Forward Rank IC:**
  - Training (2016–2021): Rank IC = 0.0462 (`source-reported`).
  - Validation (2022): Rank IC = 0.0483 (`source-reported`).
  - Test (2023–2025): Rank IC = 0.0474 (`source-reported`).

### Independently reproduced

`Not independently reproduced.` The proprietary prompt templates, full schema JSON repositories, and LightGBM surrogate weights have not been evaluated in our internal research pipeline.

### Negative evidence

1. **Drawdown Inflation on Pure OHLCV:** AlphaSchema (OHLCV) suffered a Maximum Drawdown of $18.63\%$, which is higher than Alpha360 ($8.86\%$), XGBoost ($10.30\%$), MLP ($11.47\%$), LSTM ($11.51\%$), and QuantaAlpha ($14.18\%$). This demonstrates that pure price-volume factor pools discovered by semantic search can experience severe correlated drawdown phases during market regime shifts (`source-reported`).
2. **First-Pass Code Generation Failure on Open-Source Models:** When using smaller open-source models, Pass@1 failure rates are high (37% for DeepSeek-V4-Flash, 51% for Qwen3.6-Flash), requiring heavy automated repair loops to reach valid execution. In a production pipeline without sophisticated repair guards, realization failure rates will severely hinder factor discovery (`source-reported`).
3. **Diminishing Returns of Repeated Realization:** Generating multiple code realizations for the same semantic plan exhibits steep diminishing returns: top-20% recall per realization collapses from 0.462 ($k=1$) to 0.156 ($k=5$) (Table 5), confirming that spending compute on repeated LLM rollouts is budget-inefficient compared to exploring new semantic schemas (`source-reported`).

## Falsification plan

To falsify the claim that structured semantic plan exploration discovers robust, out-of-sample alpha factors:

1. **Surrogate Model Disablement Test (`research-defined falsification threshold`):**
   - *Test:* Replace the LightGBM surrogate reward model with: (a) Uniform random plan selection, and (b) Shuffled-reward surrogate control (as in Appendix E).
   - *Threshold / Decision Rule:* If the factor pool generated by surrogate-guided exploitation does not achieve an Information Ratio at least 25% higher than the uniform random baseline over a 2-year out-of-sample window, the hypothesis that schema-level reward learning accelerates alpha discovery is falsified.
2. **Transaction Cost Degradation Stress Test (`research-defined falsification threshold`):**
   - *Test:* Escalate round-trip transaction costs from 20 bps to 35 bps and 50 bps, and increase rebalance frequency from Top50/Drop5 to daily full turnover.
   - *Threshold / Decision Rule:* If net Annualized Excess Return drops below 2.0% or Information Ratio drops below 0.30 under 35 bps round-trip friction, the factor pool is falsified as an unexecutable theoretical construct destroyed by market microstructure frictions.
3. **Cross-Universe Portability Test (`research-defined falsification threshold`):**
   - *Test:* Deploy the 120 CSI300-mined factors directly onto US Equities (S&P 500 / Russell 1000) without retraining individual factor formulas.
   - *Threshold / Decision Rule:* If mean out-of-sample Rank IC on US large-cap equities is not statistically distinguishable from zero ($t$-statistic $< 2.0$), the discovered semantics represent China-specific retail microstructure anomalies rather than universal asset-pricing mechanisms.
4. **Permutation & Data Snooping Audit (`research-defined falsification threshold`):**
   - *Test:* Evaluate the final factor pool against White's Reality Check and Hansen's Superior Predictive Ability (SPA) test, accounting for the 1,280 in-sample plan evaluations.
   - *Threshold / Decision Rule:* If the $p$-value for superior performance exceeds 0.05 after adjusting for data mining across the 700M schema space, the strategy is rejected as backtest selection bias.

## Crypto portability

- **Portability Status:** `adapted` / `unproven` (`research interpretation`). The primary research demonstrated AlphaSchema strictly on Chinese A-share equity markets (CSI300 and CSI500). Porting to cryptocurrency markets is unproven and represents research hypothesis adaptation.
- **Portability Risks & Structural Discrepancies:**
  - **Absence of Centralized Daily Close/Open Auction:** China A-shares feature synchronized 09:30 open and 15:00 close call auctions, allowing clean `deal_price = open` assumptions with known liquidity. Cryptocurrencies trade 24/7/365 across decentralized, fragmented order books with no universal open/close auction (`research-proposed`).
  - **Perpetual Funding Rate Drift:** In crypto perpetual futures, long positions held over multi-day horizons are subject to 8-hour funding rates. In strong bull regimes, funding payments can exceed 20–50% annualized, rapidly eroding the 8.5%–11.9% excess return reported in equities (`research-proposed`).
  - **Cross-Sectional Universe Size & Breadth:** CSI300 provides 300 highly liquid equities for cross-sectional ranking. In crypto, liquid perpetual futures with dependable historical data and uniform tick rules rarely exceed 50–100 tokens, severely reducing cross-sectional rank dispersion and increasing idiosyncratic token risk (`research-proposed`).
  - **Extreme Volatility & Fat Tails:** Microstructure events such as "effort-result breakout" and "volatility compression" behave drastically differently during cascading liquidation cascades in crypto than in regulated equity markets with $\pm 10\%$ price limit bands (`research-proposed`).

## Limitations

1. **Reliance on Downstream Non-Linear Combiner:** The headline results rely on a LightGBM ranker combining 120–150 factors. This obscures the standalone efficacy of individual factors and risks multi-factor collinearity and overfitting.
2. **Underspecified Parameter Calibration:** While schema plans decouple logic from code, individual LLM realizations choose window lengths, clipping thresholds, and decay half-lives non-deterministically, introducing unquantified implementation variance.
3. **Execution Latency in Real-Time Systems:** Generating LLM code and validating leakage during live trading is computationally unviable; AlphaSchema is strictly an offline factor mining paradigm, requiring pre-compiled factors for live production.
4. **Survivorship & Point-in-Time Bias Risk:** While Qlib filters handle historical index constituents, cross-sectional ranking across historical data requires meticulous point-in-time constituent lists to avoid survivorship bias.

## Implementation status

- `not-implemented`. This record represents an upstream research capture and evaluation. No implementation in NautilusTrader, PyBroker, paper trading, testnet, or live production has been authorized or conducted.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record serves exclusively as normalized upstream research intelligence for Hermes Loop A hypothesis generation. It is not approved for live trading, testnet deployment, paper execution, or production implementation.

## Related Wiki records

- `[[quant/quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05]]` — QuantaAlpha evolutionary framework for LLM-driven alpha mining on China A-shares (Han et al. 2026).
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — Market logic multi-agent factor generation and hypothesis-constrained factor exploration.
- `[[quant/llm-verifier-guided-strategy-genome-evolution-evoquant-2026-09-04]]` — LLM verifier-guided strategy genome evolution and code-level mutation trees.
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery.
- `[[quant/gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]` — Multi-metric gated anti-overfitting objective for evolutionary parameter selection.

## Sources

1. **Primary Research Paper:**
   - Jingyang Yi, Jian Yang, Yifei Jin, Yuqi Li, and Jian Li, *"AlphaSchema: Exploring the Space of Trading Semantics for LLM-Based Alpha Mining"*, arXiv preprint `arXiv:2607.26642v1 [cs.AI]`, submitted July 29, 2026.
   - Canonical URL: [https://arxiv.org/abs/2607.26642](https://arxiv.org/abs/2607.26642)
   - DOI: [10.48550/arXiv.2607.26642](https://doi.org/10.48550/arXiv.2607.26642)
   - HTML Full-Text: [https://arxiv.org/html/2607.26642v1](https://arxiv.org/html/2607.26642v1)
   - Primary PDF: [https://arxiv.org/pdf/2607.26642](https://arxiv.org/pdf/2607.26642)
2. **Directly Benchmarked Literature & Predecessors in Primary Source:**
   - Xiao Yang, Weiqing Liu, Dong Zhou, Jiang Bian, and Tie-Yan Liu, *"Qlib: An AI-oriented quantitative investment platform"*, arXiv preprint `arXiv:2009.11189`, 2020. URL: [https://arxiv.org/abs/2009.11189](https://arxiv.org/abs/2009.11189).
   - Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu, *"LightGBM: A highly efficient gradient boosting decision tree"*, *Advances in Neural Information Processing Systems* 30 (NeurIPS 2017).
   - Zura Kakushadze, *"101 Formulaic Alphas"*, *Wilmott*, 2016(84):72–81, 2016. DOI: `10.1002/wilm.10558`.
   - Yuante Li, Xingxuan Yang, Xinyi Yang, Xiao Yang, Weiqing Liu, and Jiang Bian, *"R&D-Agent-Quant: A multi-agent framework for data-centric factors and model joint optimization"*, *Advances in Neural Information Processing Systems* 38 (NeurIPS 2026).
   - Jiarui Han et al., *"QuantaAlpha: An evolutionary framework for LLM-driven alpha mining"*, arXiv preprint `arXiv:2602.07085`, 2026. URL: [https://arxiv.org/abs/2602.07085](https://arxiv.org/abs/2602.07085).
   - Zepu Tang et al., *"AlphaAgent: LLM-driven alpha mining with regularized exploration to counteract alpha decay"*, in *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining* (KDD 2025), pp. 2813–2822, 2025. DOI: `10.1145/3690624.3709325`.
