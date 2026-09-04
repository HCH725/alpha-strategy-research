---
schema: strategy-research-record-v1
title: FinATOM Head-Free Token Generation for Multi-Step Return Forecasting and Constrained ETF Portfolio Allocation
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - language-models
  - token-generation
  - portfolio-allocation
  - mean-variance
  - dapo
  - grpo
  - etf
  - multimodal
status: research-only
confidence: medium
source_as_of: "2026-08-10"
sources:
  - "Xu Ouyang and Moontae Lee, 'FinATOM: Financial Numerical Prediction and Allocation as Token Generation', arXiv:2608.09880v1 [cs.LG, q-fin.PM], August 10, 2026. https://arxiv.org/abs/2608.09880"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FinATOM: Head-Free Token Generation for Multi-Step Return Forecasting and Constrained ETF Portfolio Allocation

## Provenance

- **Primary Source:** Xu Ouyang and Moontae Lee (Department of Computer Science, University of Illinois Chicago), *"FinATOM: Financial Numerical Prediction and Allocation as Token Generation"*, arXiv preprint `arXiv:2608.09880v1 [cs.LG, q-fin.PM]`, submitted August 10, 2026.
- **Canonical Abstract URL:** https://arxiv.org/abs/2608.09880
- **Canonical HTML URL:** https://arxiv.org/html/2608.09880v1
- **Canonical PDF URL:** https://arxiv.org/pdf/2608.09880v1
- **DOI:** `10.48550/arXiv.2608.09880`
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Data Evaluation Windows:**
  - **Five-ETF Dynamic Allocation Dataset:** Daily observations across five liquid US exchange-traded funds (GLD, SPY, TLT, UUP, XLE) from January 2018 to October 2025. Evaluated across three expanding chronological walk-forward periods:
    1. *2023 Test Window:* Train 2018–2022, test calendar year 2023 (249 trading days).
    2. *2024 Test Window:* Train 2019–2023, test calendar year 2024 (251 trading days).
    3. *2025 Test Window:* Train 2020–2024, test January to October 2025 (209 trading days).
    4. *Pooled Benchmark:* Concatenation of all three test windows comprising 709 test trading days.
  - **FinTexTS Stock Forecasting Dataset:** 100 large-cap US equities from 2019 to 2023 paired with ~1,000,000 news articles and SEC filings organized across four textual tiers (macro, sector, peer, target company). Training on pre-2022 data, validation on 2022, and testing across 239 trading sessions through December 19, 2023.
- **Pre-Write Deduplication Audit:**
  - Repository-wide and Hermes Wiki Brain inspections on 2026-09-04 confirmed zero matches for `2608.09880`, `FinATOM`, `Ouyang`, or `Moontae Lee`.
  - Distinct from `strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02.md` (arXiv:2608.28060): STRATA replaces attention with continuous-time Mamba state-space layers over raw 5-minute limit-order-book bars without tokenization, grammar scaffolds, or policy-gradient optimization.
  - Distinct from `retrieval-augmented-llm-expert-switching-portfolio-management-2026-09-03.md` (arXiv:2608.28252): RAG expert switching retrieves macro text chunks to dynamically route capital across external pre-trained forecasting experts; it does not generate portfolio weights via direct vocabulary token emission.
  - Distinct from `brag-wasserstein-barycenter-adversarial-irl-control-barrier-function-2026-09-04.md` (arXiv:2608.15770): BRaG aggregates multiple expert policies via sliced Wasserstein barycenters and enforces hard quadratic-program control barrier functions, whereas FinATOM uses a single language model backbone emitting ordered discrete tokens supervised by a causal mean-variance teacher and refined by DAPO-augmented GRPO.

## Economic mechanism

### Source-reported

Financial machine learning systems traditionally separate textual and quantitative reasoning by attaching task-specific regression, ranking, or policy heads to deep representation models (e.g. PatchTST, Time-LLM, MASTER). This head-based paradigm exhibits three structural weaknesses:
1. **Contract Fragmentation:** Each downstream task requires distinct parameterizations, loss functions, and heuristic projection layers to enforce domain constraints.
2. **Loss-Metric Misalignment:** Standard regression heads minimize mean squared error (MSE) or token cross-entropy, which fail to penalize excessive portfolio turnover or optimize risk-adjusted returns (Sharpe ratio, drawdown).
3. **Loss of Generation Auditability:** Direct continuous vector outputs lack an inspectable, token-level decision trace that can be supervised with ordinal priors or improved via group-relative reinforcement learning.

FinATOM addresses these shortcomings by formulating financial prediction and allocation as **constrained autoregressive token generation** through the native language model vocabulary, eliminating auxiliary heads entirely:
- **Head-Free Architecture:** A single causal language model (Llama 3.2 1B with LoRA adapters) maps serialized market time series, covariance matrices, and macro news into structured token sequences. Valid numerical values are discrete learned vocabulary items scored by the tied input-output embedding projection.
- **Causal Teacher Supervised Pretraining:** In portfolio allocation, the model is trained via supervised fine-tuning (SFT) to imitate a backward-looking mean-variance optimization teacher incorporating turnover penalties and $1/N$ shrinkage. The teacher utilizes strictly historical data ($t-19$ to $t$) and path-dependent anchor states, ensuring zero look-ahead leakage.
- **DAPO-Augmented GRPO Risk Alignment:** To transcend the limitations of the historical covariance estimate without succumbing to policy collapse, a Group Relative Policy Optimization (GRPO) stage samples legal allocation sequences and optimizes forward 21-day realized Sharpe ratio while penalizing deviation from the causal anchor in raw action space.

### Research interpretation

The economic foundation of FinATOM rests on **regularized reinforcement learning over a causal financial manifold**:
1. **Anchored Manifold Initialization:** Pure reinforcement learning applied to financial markets suffers from low signal-to-noise ratios and explosive gradient variance, frequently resulting in policy collapse or severe drawdown exploration traps. By initializing the language model via SFT on a well-behaved causal mean-variance anchor, FinATOM forces the policy into an economically grounded subspace that respects budget constraints ($\sum w_i = 1$) and diversification bounds ($w_i \le 0.50$).
2. **Forward Information Synthesis via Policy Gradients:** Backward-looking covariance matrices ($\Sigma_t$) are notoriously lagging estimators of future risk during macro transitions. While the SFT teacher cannot parse unstructured news or foresee structural breaks, the DAPO-augmented GRPO reward function evaluates realized forward returns ($t+1$ to $t+21$). This allows the language model to learn associative relationships between macro news headlines (e.g. inflation prints, central bank commentary) and forward asset volatility, adjusting portfolio weights dynamically before trailing covariance catches up.
3. **Trust-Region Anchoring:** The inclusion of an explicit action-space penalty ($-8 \cdot \frac{1}{2}\|\boldsymbol{z}_t^g - \boldsymbol{w}_t^{\mathrm{A}}\|_1$) prevents the policy from drifting into overfitted regime-specific gambles. The model is rewarded for improving risk-adjusted returns only within a bounded neighborhood of the causal teacher.

## Signal

FinATOM formalizes two distinct token-native decision interfaces sharing the same underlying backbone:

### 1. Dynamic ETF Portfolio Allocation Interface

#### State Space & Context Construction ($x_t$)
At each decision date $t$, the context window combines:
- **Trailing Return Table ($R_t \in \mathbb{R}^{20 \times 5}$):** Strictly historical daily close-to-close returns in integer basis points across five liquid ETFs ordered as:
  $$\text{Universe} = [\text{GLD}, \text{SPY}, \text{TLT}, \text{UUP}, \text{XLE}]$$
- **Risk & Covariance Statistics:** Annualized trailing volatility per asset and the full $5 \times 5$ empirical return-correlation matrix computed over the 20-day window.
- **Path-Dependent State:** Previous quantized causal anchor allocation vector $\boldsymbol{w}_{t-1}^{\mathrm{A}} \in [0, 1]^5$.
- **Macro-Financial News Block:** Approximately 100-word daily summary synthesized from major news outlets (Bloomberg, Reuters, CNBC via NewsAPI) using DeepSeek-V4, covering monetary policy, inflation, labor markets, GDP growth, energy, and geopolitical developments.

#### Causal Mean–Variance Teacher Optimization
The continuous teacher solves a convex quadratic program at date $t$:
$$\widetilde{\boldsymbol{w}}_t = \arg\min_{\boldsymbol{w} \in \mathcal{W}} \left[ \sqrt{252 \, \boldsymbol{w}^\top \Sigma_t \boldsymbol{w}} - 0.05 (252 \mu_t)^\top \boldsymbol{w} + 0.05 \cdot \frac{1}{2} \|\boldsymbol{w} - \boldsymbol{w}_{t-1}^{\mathrm{A}}\|_1 \right]$$
subject to the feasible polytope:
$$\mathcal{W} = \left\{ \boldsymbol{w} \in \mathbb{R}^5 \;\middle|\; \boldsymbol{w} \ge 0, \; \boldsymbol{1}^\top \boldsymbol{w} = 1, \; w_i \le 0.50 \; \forall i \right\}$$
*(Note: on the initial sample date, the turnover term is omitted).*

To stabilize out-of-sample estimation, the solution is shrunk toward equal weight ($1/N$) and quantized:
$$\overline{\boldsymbol{w}}_t = 0.85 \, \widetilde{\boldsymbol{w}}_t + 0.15 \, \frac{\boldsymbol{1}}{5}$$
$$\boldsymbol{a}_t^{\mathrm{A}} = Q_{50, 1000}(1000 \, \overline{\boldsymbol{w}}_t)$$
where $Q_{50, 1000}$ performs largest-remainder apportionment over a 50-unit discrete grid enforcing a total budget of 1000 units ($\sum a_i = 1000$) with a minimum floor of 50 units per asset ($a_i \ge 50$). The normalized state passed forward is $\boldsymbol{w}_t^{\mathrm{A}} = \boldsymbol{a}_t^{\mathrm{A}} / 1000$.

#### SFT Output Grammar & Ordinal Loss
The target answer sequence follows the deterministic scaffold:
$$\texttt{<GLD><250><SPY><200><TLT><200><UUP><200><XLE><150>}$$
Across all answer positions, standard sequence cross-entropy $\mathcal{L}_{\mathrm{tok}}$ is applied. At each of the five value slots $j \in \{1, \dots, 5\}$, an additional Gaussian ordinal cross-entropy loss is imposed over the 21 grid values $\{0, 50, \dots, 1000\}$:
$$q_{jk} \propto \exp\left( -\frac{(k - k_j^*)^2}{2(0.8)^2} \right), \quad k \in \{0, 1, \dots, 20\}$$
$$\mathcal{L}_{\mathrm{SFT}} = \mathcal{L}_{\mathrm{tok}} + \sum_{j=1}^5 \mathrm{CE}(q_j, p_j)$$

#### DAPO-Augmented GRPO Policy Optimization
The policy stage samples $G = 8$ candidate allocation sequences per prompt at temperature $T = 1.0$. For raw discrete token action $\boldsymbol{z}_t^g = \boldsymbol{a}_t^g / 1000$, deployed weights are strictly normalized:
$$\boldsymbol{w}_t^g = \frac{\boldsymbol{z}_t^g}{\boldsymbol{1}^\top \boldsymbol{z}_t^g}$$
The policy reward evaluates realized 21-day forward portfolio Sharpe ratio net of anchor deviation:
$$R_t^g = \operatorname{Sh}(\boldsymbol{w}_t^g; \, t+1:t+21) - 8 \cdot \frac{1}{2} \|\boldsymbol{z}_t^g - \boldsymbol{w}_t^{\mathrm{A}}\|_1$$
*(Any grammar or parsing failure receives a heavy penalty $R_t^g = -5$).*

Group-relative advantages normalize rewards against the empirical group mean $\overline{R}_t$ and standard deviation $s_t$:
$$A_t^g = \frac{R_t^g - \overline{R}_t}{\max(s_t, 0.65)}$$
*(Advantage is zeroed for degenerate groups with near-identical rewards).*

Updates follow a token-level clipped surrogate objective with decoupled asymmetric bounds $[0.80, 1.28]$:
$$\mathcal{L}_{\mathrm{pol}} = -\frac{1}{M} \sum_{g=1}^G \sum_{\ell=1}^L m_{g\ell} \min\left( \rho_{t\ell}^g A_t^g, \, \operatorname{clip}(\rho_{t\ell}^g, 0.80, 1.28) A_t^g \right)$$
where $\rho_{t\ell}^g = \pi_\theta(y_{t,\ell}^g \mid x_t, y_{t,<\ell}^g) / \pi_{\mathrm{old}}(y_{t,\ell}^g \mid x_t, y_{t,<\ell}^g)$ and $m_{g\ell}$ masks active answer tokens. Training executes 3 passes per prompt with behavior-KL early stopping at threshold $0.03$, setting reference-KL to zero.

#### Inference & Execution Decoding
At deployment, the model performs deterministic expectation decoding:
$$\widehat{a}_j = \sum_{k=0}^{20} p_{jk} v_k, \quad v_k = 50 \cdot k$$
Final portfolio weights normalize the expectation vector to the unit simplex:
$$\boldsymbol{w}_t = \frac{\widehat{\boldsymbol{a}}}{\boldsymbol{1}^\top \widehat{\boldsymbol{a}}}$$
*(Fallback: if all probabilities collapse to near-zero, equal weight $\boldsymbol{1}/5$ is deployed).*

---

### 2. Multi-Step Autoregressive Stock Forecasting Interface

#### State Space & Context Construction
For each equity $i$ in a 100-stock universe, the prompt contains:
- 64 trading sessions of close-to-close returns, opening gaps, and high-low ranges in integer basis points.
- Trailing 20-day volatility $\sigma_{t,20}$, multi-horizon return momentum, and 52-week drawdown.
- Same-day market and sector benchmarks.
- Four tiers of news text (macro, sector, related peer, target firm) and five SEC 10-K/10-Q filing summaries.

#### Standardized Horizon Targets
For forward horizons $h \in \{1, 2, 3\}$, returns are volatility-standardized:
$$r_{t,h} = \frac{P_{t+h}}{P_{t+h-1}} - 1, \quad z_{t,h} = \operatorname{clip}\left( \frac{r_{t,h}}{\sigma_{t,20}}, -8, 8 \right)$$
Forty-one train-only quantile bins $\{b_0, \dots, b_{40}\}$ partition standardized returns, with bin centers $c_k = \mathbb{E}[z \mid b=k]$.

#### Grammar & Autoregressive Decoding
The token scaffold is fixed:
$$\texttt{<|forecast_start|><D1><b12><D2><b19><D3><b07><|forecast_end|>}$$
Decoding is strictly autoregressive: the D1 argmax bucket token is sampled and appended before evaluating D2, which in turn conditions D3. Continuous scores are recovered via conditional expectation:
$$\widehat{z}_{t,h} = \sum_{k=0}^{40} p_{t,h,k} c_k$$
Scores are rescaled by $\sigma_{t,20}$ and compounded into a 3-day expected return score. Equities are ranked cross-sectionally, and the top 20 are equally weighted with 3-day holding periods.

#### Policy Optimization Reward
A one-epoch policy stage updates bucket positions using $G=4$ samples under a composite reward:
$$R = 0.40 R_{\mathrm{step}} + 0.25 R_{\mathrm{path}} + 0.05 R_{\mathrm{dir}} + 0.25 R_{\mathrm{rank}} + 0.05 R_{\mathrm{top20}}$$
with clipped token-PPO and KL coefficient $0.02$ against cached SFT action probabilities.

## Required data

- **Asset Universe:**
  - *ETF Allocation:* Five US-listed ETFs covering broad macro asset classes: GLD (Gold bullion), SPY (S&P 500 equity), TLT (20+ Year Treasury bonds), UUP (US Dollar Index Bullish), and XLE (Energy sector equity).
  - *Stock Forecasting:* 100 large-cap US equities from the FinTexTS benchmark.
- **Price & Microstructure Data:** Daily OHLCV bars, close-to-close returns, overnight opening price gaps, and intraday high-low volatility ranges.
- **Statistical Features:** Trailing 20-day sample covariance matrix $\Sigma_t \in \mathbb{R}^{5 \times 5}$, sample mean vector $\mu_t \in \mathbb{R}^5$, 20-day annualized volatility per asset $\sigma_{t,20}$, and trailing 52-week peak drawdown.
- **Textual Data Feeds:**
  - Macroeconomic news articles retrieved daily via NewsAPI across major financial publishers (Bloomberg, Reuters, CNBC, WSJ).
  - SEC regulatory disclosure summaries (Form 10-K annual reports and Form 10-Q quarterly reports).
- **Point-in-Time Availability:**
  - All price features, covariance matrices, and news summaries are stamped strictly at or before market close of decision date $t$.
  - Forward returns ($t+1$ to $t+21$) enter solely as external reward scalars during offline policy optimization; they are excluded from the model's visible context.
- **Missing Data & Degeneracy Rules:**
  - If news text is missing for a date, the text block is omitted while preserving the tabular structure.
  - If model output fails grammar verification during inference, an explicit fallback to equal weights ($\boldsymbol{1}/5$) is executed.

## Execution assumptions

- **Execution Timing:** Next-day market open or close rebalancing ($t \to t+1$ trade execution).
- **Rebalance Cadence:** Daily rebalancing for the 5-ETF allocation portfolio; 3-day periodic rebalancing for the 100-stock top-20 basket.
- **Transaction Costs & Slippage:**
  - Modeled linear transaction cost of 5 basis points ($c = 0.0005$) per unit of one-way turnover:
    $$C_t = 0.0005 \cdot \frac{1}{2} \|\boldsymbol{w}_t - \boldsymbol{w}_{t-1}\|_1$$
  - Break-even cost analysis: the pooled annual gross return advantage of the policy over SFT ($\approx 0.49$ percentage points) versus excess one-way turnover ($0.056\% \times 252 \approx 14.1\%$ annualized) implies a break-even cost of roughly **340 basis points** per unit turnover, far exceeding institutional ETF execution costs (typically $< 1\text{ bp}$).
- **Leverage & Portfolio Bounds:** Long-only simplex ($\boldsymbol{w}_t \ge 0$, $\sum_{i=1}^5 w_{t,i} = 1$). Maximum single-asset concentration is capped at $50\%$ ($w_{t,i} \le 0.50$). Zero borrowing, zero shorting, zero leverage.
- **Market Impact:** Omitted in the source paper due to immense liquidity in GLD, SPY, TLT, UUP, and XLE (daily secondary market turnover exceeds billions of dollars).

## Evidence

### Source-reported

All figures trace directly to Ouyang & Lee (*arXiv:2608.09880v1*, August 10, 2026), Section 5, Tables 2–5, and Supplementary Material Q7–Q12:

#### 1. Chronological Walk-Forward ETF Allocation (Table 2 & Table 3)
Evaluated across three expanding walk-forward periods (252 trading days/year annualization, zero risk-free rate):

| Period / Year | Strategy / Model | Annualized Return | Annualized Volatility | Sharpe Ratio | Max Drawdown | Daily Turnover |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **2023** (249 days) | FinATOM SFT | 7.18% | 5.03% | 1.404 | -2.81% | 1.316% |
| | **FinATOM Policy** | **7.11%** | **4.98%** | **1.404** | **-2.78%** | **1.271%** |
| | Causal Teacher Target | 7.92% | 5.03% | 1.542 | -2.83% | — |
| | Equal Weight ($1/N$) | 6.55% | 7.47% | 0.886 | -5.28% | — |
| **2024** (251 days) | FinATOM SFT | 7.35% | 5.00% | 1.445 | -4.72% | — |
| | **FinATOM Policy** | **7.88%** | **4.93%** | **1.564** | **-4.72%** | — |
| | Causal Teacher Target | 7.06% | 4.93% | 1.407 | -4.69% | — |
| | Equal Weight ($1/N$) | 9.59% | 6.87% | 1.367 | -4.88% | — |
| **2025** (209 days) | FinATOM SFT | 10.46% | 6.91% | 1.474 | -6.28% | — |
| | **FinATOM Policy** | **11.76%** | **6.87%** | **1.653** | **-6.04%** | — |
| | Causal Teacher Target | 11.58% | 6.61% | 1.691 | -5.21% | — |
| | Equal Weight ($1/N$) | 15.72% | 10.03% | 1.506 | -7.99% | — |
| **Pooled** (709 days) | FinATOM SFT | — | — | 1.428 (Gross) / 1.394 (Net) | — | 1.481% |
| | **FinATOM Policy** | — | — | **1.529 (Gross) / 1.494 (Net)** | — | **1.537%** |
| | Causal Teacher Target | — | — | 1.540 (Gross) | — | — |
| | Equal Weight ($1/N$) | — | — | 1.245 (Gross) | — | — |

*Key Empirical Findings:*
- Policy optimization raises pooled gross Sharpe by **+0.101** (1.428 to 1.529) and net Sharpe by **+0.100** (1.394 to 1.494) under 5-bp transaction costs.
- Daily one-way turnover rises by only **0.056 percentage points** (1.481% to 1.537%), demonstrating that the policy improves the return-risk tradeoff rather than churning volume.
- In 2024, the policy exceeds its own causal teacher's Sharpe ratio (**1.564 vs. 1.407**), demonstrating that outcome-based RL discovers valuable macro adjustments beyond backward-looking sample covariance.

#### 2. Input-Modality Ablation (Table 4)
Evaluating the relative contributions of text and price time series across the three test periods:

| Input Modality | 2023 Sharpe | 2024 Sharpe | 2025 Sharpe | 3-Year Mean Sharpe |
| :--- | :---: | :---: | :---: | :---: |
| News Only | 1.377 | 1.459 | 1.473 | 1.436 |
| Time Series Only | 1.408 | 1.565 | 1.463 | 1.479 |
| **News + Time Series** | **1.404** | **1.564** | **1.653** | **1.540** |

*Key Empirical Findings:*
- Time-series context provides the most stable standalone foundation, nearly tying the multimodal arm in 2023 (1.408 vs. 1.404) and 2024 (1.565 vs. 1.564).
- Macro news provides strong regime-dependent alpha in 2025, lifting Sharpe by **+0.190** over time-series alone (1.653 vs. 1.463).

#### 3. FinTexTS 100-Stock Top-20 Cross-Sectional Ranking (Table 5)
Evaluated over 239 test trading days through December 19, 2023:

| System / Model Architecture | Cumulative Return | Sharpe Ratio |
| :--- | :---: | :---: |
| FinTexTS Published Baseline (Lee et al. 2026) | 53.98% | 2.67 |
| FinATOM SFT (Head-Free Llama 3.2 1B) | 73.52% | 2.68 |
| **FinATOM Policy (One-Epoch Token-PPO)** | **73.72%** | **2.69** |

*Key Empirical Findings:*
- The head-free token interface achieves 73.52% return and 2.68 Sharpe on SFT alone.
- Policy optimization provides an incremental gain (+0.20 pp cumulative return, +0.01 Sharpe), confirming that supervised token initialization carries the primary ranking signal and RL acts as a conservative fine-tuning operator.

### Independently reproduced

`Not independently reproduced.` (Scouted research capture from public arXiv preprint).

### Negative evidence

1. **Teacher Dominance in Stagnant/Trending Regimes:** The learned policy trails its causal teacher in 2023 (1.404 vs. 1.542) and in 2025 (1.653 vs. 1.691). Across all 709 pooled days, the policy's gross Sharpe of 1.529 slightly lags the teacher's 1.540, proving that outcome-based RL does not uniformly dominate classical mean-variance optimization.
2. **Failure of Policy Learning in 2023:** In 2023, the policy stage fails to improve upon SFT at three decimals of Sharpe (both 1.404), with behavior-KL early stopping terminating updates early due to low directional reward signal.
3. **Raw Return Underperformance vs. 1/N Benchmark:** Equal weighting earns substantially higher raw annualized returns than FinATOM in 2024 (9.59% vs. 7.88%) and 2025 (15.72% vs. 11.76%). FinATOM's Sharpe advantage derives primarily from aggressive volatility suppression (4.93% vs. 6.87% in 2024; 6.87% vs. 10.03% in 2025) rather than raw profit maximization.
4. **Modality Redundancy in Normal Regimes:** Adding news summaries produces zero gain in 2023 (news+TS Sharpe 1.404 vs. TS-only 1.408) and 2024 (1.564 vs. 1.565). The multimodal thesis relies exclusively on the 2025 regime.
5. **Statistical Significance Gap:** The paper evaluates only a single training seed per setting across three chronological splits. No formal statistical significance (e.g. Jobson-Korkie or Ledoit-Wolf p-values) is documented.
6. **Look-Ahead & Cutoff Contamination Risks:** Llama 3.2's pretraining data cutoff (December 2023) overlaps the 2023 ETF test period and the entire FinTexTS stock dataset. Furthermore, daily news blocks were summarized using DeepSeek-V4 (released mid-2026), creating a potential channel for parametric hindsight leakage into historical summaries.

## Falsification plan

To disconfirm the FinATOM alpha hypothesis, execute the following operational stress tests:
1. **Multi-Seed Stability Audit:** Retrain the SFT and DAPO-augmented GRPO pipeline across 10 random seeds on the identical 2018–2025 ETF splits. If the standard deviation of pooled net Sharpe exceeds 0.08, or if the paired Sharpe difference test against SFT (Memmel-corrected Jobson-Korkie) yields $p > 0.10$, the claim of systematic RL improvement is falsified as seed noise.
2. **Strictly Pre-Dated News Summarization:** Replace DeepSeek-V4 news summaries with summaries generated by an open-weights model whose pretraining cutoff strictly predates 2023 (e.g. Llama-2-7B or Mistral-7B frozen as of 2023). If the 2025 multimodal Sharpe advantage (+0.190) disappears or collapses to $< 0.05$, the reported news alpha is falsified as hindsight contamination.
3. **Closed-Loop Deployment Test:** Remove the teacher-in-the-loop assumption at inference time. Instead of feeding the causal teacher's previous anchor $\boldsymbol{w}_{t-1}^{\mathrm{A}}$ into the prompt at date $t$, feed the model's own previously generated allocation $\boldsymbol{w}_{t-1}^{\mathrm{model}}$. If compounding autoregressive errors cause portfolio volatility to expand by $> 25\%$ or net Sharpe to drop below 1.20, the production feasibility of the system is falsified.
4. **Anchor Ablation Sweep:** Vary the anchor consistency penalty coefficient $\lambda \in \{0, 2, 4, 8, 16\}$. If setting $\lambda = 0$ results in policy divergence or negative Sharpe, it proves that the model possesses no autonomous alpha discovery capability and relies entirely on teacher tethering.
5. **Post-2025 True Out-of-Sample Evaluation:** Evaluate the frozen model checkpoint on unseen daily data from November 2025 through late 2026. If the net Sharpe ratio falls below the naive equal-weight ($1/N$) benchmark, the policy is rejected.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Structural Differences & Adaptation Requirements:**
  - *24/7 Continuous Trading:* Traditional US equities trade on 252 discrete sessions with distinct market opens, closes, and weekend halts. Crypto operates 24/7/365. Implementing FinATOM in crypto requires redefining daily boundaries (e.g. 00:00 UTC cutoff) and adjusting annualization factors from $\sqrt{252}$ to $\sqrt{365}$.
  - *Crypto Universe Construction:* The 5-asset macro ETF universe (GLD, SPY, TLT, UUP, XLE) represents fundamentally distinct economic drivers (commodities, equities, sovereign debt, fiat currency, energy). Constructing an analogous 5-asset crypto universe is challenging due to high cross-asset beta. A plausible basket (e.g. BTC, ETH, SOL, BNB, and a yield-bearing stablecoin sUSDe/USD0) exhibits far higher intra-market correlation and joint tail contagion during liquidity crunches.
  - *Funding Rate & Basis Carry:* Unlike spot ETFs, crypto capital primarily resides in perpetual futures. Holding long positions in bullish regimes incurs substantial funding payments (often 10–30% annualized). The causal mean-variance teacher must incorporate dynamic 8-hour funding rates directly into the optimization objective, penalizing crowded high-funding long exposures.
  - *News Quality & Latency:* Macro news feeds (Bloomberg/Reuters) have muted explanatory power for idiosyncratic crypto tokens compared to crypto-native catalysts (protocol governance, token unlock schedules, on-chain liquidity migrations, exchange listings, MEV exploit alerts). Sourcing and verifying point-in-time crypto news without look-ahead bias is significantly more difficult.
  - *Execution Costs & Slippage:* While large-cap ETFs trade at tight $< 1\text{ bp}$ bid-ask spreads, crypto perpetuals charge 2 to 5 bps taker fees plus dynamic slippage during liquidation cascades. The 5-bp linear cost assumption in FinATOM is realistic for Binance/Bybit VIP tiers, but break-even tolerances will be tighter for smaller tokens.

## Limitations

- **Single Seed Uncertainty:** All published empirical gains stem from a single training run per period; statistical significance cannot be confirmed without seed replicates.
- **Teacher Dependency at Deployment:** The test pipeline retains the causal mean-variance optimizer in the loop at inference time to supply $\boldsymbol{w}_{t-1}^{\mathrm{A}}$ to the prompt. A fully autonomous, closed-loop deployment where the model conditions exclusively on its own generated historical allocations remains untested.
- **Pretraining Contamination Window:** Llama 3.2 was pretrained on data through December 2023, overlapping the 2023 ETF test period and the entire FinTexTS stock dataset.
- **Summarizer Hindsight Risk:** DeepSeek-V4 was trained well after the historical dates of the news articles it summarized.
- **Incremental RL Contribution:** In stock forecasting, token policy optimization increases Sharpe by only +0.01 (2.68 to 2.69); in ETF allocation, RL fails to add value in 2023. The framework's success is overwhelmingly driven by the supervised initialization on the causal teacher.
- **Asset Universe Breadth:** The allocation framework is evaluated on only five assets; performance on large-scale universes ($N > 50$) under combinatorial token length explosion is unverified.

## Implementation status

- `not-implemented`.
- No prototype or production implementation exists in NautilusTrader, PyBroker, or internal trading engines.
- This record represents a research capture and methodological normalization only.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Capturing this research record does not authorize paper trading, backtest integration, testnet execution, or live capital allocation. Any future implementation requires explicit research review, multi-seed replication, closed-loop verification, and rigorous transaction-cost stress testing.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]]
- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
- [[quant/backtest-overfitting-pbo-cscv-2026-08-27]]
- [[quant/sharpe-deflated-multiple-testing-2026-08-27]]
- [[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]
- [[quant/questrader-self-supervised-auxiliary-task-discovery-rl-trading-2026-09-02]]
- [[quant/strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02]]
- [[quant/brag-wasserstein-barycenter-adversarial-irl-control-barrier-function-2026-09-04]]

## Sources

1. Xu Ouyang and Moontae Lee, *"FinATOM: Financial Numerical Prediction and Allocation as Token Generation"*, arXiv preprint `arXiv:2608.09880v1 [cs.LG, q-fin.PM]`, submitted August 10, 2026. Stable URL: https://arxiv.org/abs/2608.09880. Full-text HTML: https://arxiv.org/html/2608.09880v1. DOI: `10.48550/arXiv.2608.09880`.
2. Harry Markowitz, *"Portfolio Selection"*, The Journal of Finance, Vol. 7, No. 1, pp. 77–91, 1952. DOI: `10.2307/2975974`.
3. Victor DeMiguel, Lorenzo Garlappi, and Raman Uppal, *"Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?"*, The Review of Financial Studies, Vol. 22, No. 5, pp. 1915–1953, 2009. DOI: `10.1093/rfs/hhm075`.
4. Zhihong Shao et al., *"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"*, arXiv preprint `arXiv:2402.03300`, 2024.
5. Qisheng Yu et al., *"DAPO: An Open-Source LLM Reinforcement Learning System at Scale"*, arXiv preprint `arXiv:2503.14476`, 2025.
6. Junwoo Lee et al., *"FinTexTS: Financial Text-Paired Time-Series Dataset via Semantic-Based and Multi-Level Pairing"*, Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26), pp. 1–12, 2026. DOI: `10.1145/3770855.3817468`.
7. Meta AI, *"Llama 3.2 Model Card"*, Meta Platforms, Inc., 2024.
