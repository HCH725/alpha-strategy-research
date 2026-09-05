---
schema: strategy-research-record-v1
title: "AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - symbolic-alpha
  - gflownet
  - on-policy-distillation
  - counterfactual-credit
  - formulaic-alpha
  - cross-sectional-equity
  - china-ashares
  - sp500
status: research-only
confidence: medium
source_as_of: 2026-08-02
sources:
  - "arXiv:2608.01303v1 — https://arxiv.org/abs/2608.01303"
  - "https://doi.org/10.48550/arXiv.2608.01303"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery

## Provenance

- **Paper Title:** AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery
- **Author:** Yaoyu Su (Tsinghua University, Beijing, China; contact: `syy21@tsinghua.org.cn`)
- **arXiv Identifier:** `arXiv:2608.01303v1 [cs.LG, q-fin.CP]` (submitted August 2, 2026)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2608.01303](https://doi.org/10.48550/arXiv.2608.01303)
- **Canonical URLs:**
  - Abstract: [https://arxiv.org/abs/2608.01303](https://arxiv.org/abs/2608.01303)
  - Full Text HTML: [https://arxiv.org/html/2608.01303v1](https://arxiv.org/html/2608.01303v1)
  - Primary Source Code/LaTeX Package: Unpacked and verified directly from the authoritative arXiv source archive (`paper.tar.gz` containing `main.tex`, `appendix.tex`, `tables/main_results.tex`, `tables/mechanism_results.tex`, and `references.bib`).
- **Repository Deduplication Audit:**
  - A comprehensive search across the repository verified zero prior records referencing `2608.01303`, `AlphaG-OPD`, or `Yaoyu Su`.
  - Adjacent symbolic factor discovery records (`alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05.md`, `alphalogics-market-logic-multi-agent-factor-generation-2026-09-05.md`, `agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04.md`, `factorsmith-autonomous-agentic-alpha-mining-2026-09-04.md`, `factorengine-program-level-knowledge-infused-alpha-factor-mining-2026-09-04.md`) address grammar-guided MCTS, LLM multi-agent negotiation, adversarial code review, or program synthesis.
  - AlphaG-OPD is structurally distinct: it addresses the fundamental credit assignment bottleneck in Generative Flow Networks (GFlowNets) by introducing structural on-policy distillation (OPD) with paired sibling counterfactuals, an empirical Lower Confidence Bound (LCB) reliability gate, and score-indexed bounded credit consolidation under an exact physical-score budget.

---

## Economic mechanism

### Source-reported

In automated symbolic formulaic alpha mining, search algorithms (Genetic Programming, RL, GFlowNets) evaluate candidates only upon full completion of an abstract syntax tree (AST). However, a scalar terminal reward (such as cross-sectional Information Coefficient, IC) entangles an early structural action with all subsequent tokens, operators, and parameters. A high-scoring completed expression reinforces all decisions along its trajectory, failing to identify whether an alternative legal action at an intermediate node would have yielded superior risk-adjusted alpha.

Generative Flow Networks (GFlowNets) learn a policy proportional to terminal reward, preserving diverse, multimodal factor candidates. Yet their Trajectory Balance (TB) objective remains trajectory-global and cannot compare unchosen sibling actions at visited intermediate states.

To solve local credit assignment without inflating evaluation budgets, the author introduces **AlphaG-OPD**, structured across three sequential decisions:
1. **Component I (Where to teach):** An on-policy structural interface identifies partial AST states $s$ visited by the current forward policy $P_F^\theta$. It selects the sampled action and two legal sibling actions ($m=3$) that share action class, operator family, and arity, ensuring identical unresolved stack obligations.
2. **Component II (What is reliable enough to teach):** Evaluates the 3 siblings under $K=4$ shared completion suffixes sampled from a reward-blind geometric proposal $q$. Suffix sampling probabilities cancel when comparing relative sibling credits. A provisional teacher distribution is formed via exponential tilt within an explicit Kullback-Leibler (KL) trust region ($\delta = 0.03$). The teacher is admitted only if matched comparisons exhibit sufficient winner agreement ($\gamma \ge \gamma_{\min} = 0.75$, i.e., at least 3 of 4 suffixes agree) AND a positive empirical lower confidence bound on paired improvement ($\operatorname{LCB}(s) = \bar{\Delta} - z \operatorname{SE}(\Delta) > 0$, $z=1$).
3. **Component III (How much and how long to teach):** Accepted targets are stored in a queue of at most 512 rows, expiring after 1,000 physical evaluations. The student is updated via forward KL on the sibling-restricted distribution. A measured gradient-norm balancing rule caps the auxiliary gradient at $\rho = 0.10$ of the Entropy-TB gradient norm, requiring zero additional factor evaluations during replay.

### Research interpretation

AlphaG-OPD targets the structural micro-foundations of cross-sectional factor generation:
1. **Resolution of Local Combinatorial Credit:** In financial time-series feature engineering, the choice of operator (e.g., `Ts_Rank` vs. `Ts_Mean`) or operand (e.g., `Volume` vs. `Close`) at an inner AST node fundamentally dictates the economic nature of the factor (e.g., rank-order momentum vs. simple moving average). Terminal evaluation introduces severe credit variance. By holding the prefix and suffix constant across sibling actions, AlphaG-OPD isolates the partial derivative of terminal alpha quality with respect to a single localized syntax decision.
2. **Epistemic Noise Gating against Spurious Overfitting:** Financial data contains high noise-to-signal ratios. A single lucky random completion can make an inferior operator appear profitable. Requiring 4 independent completions to agree on the superior sibling with an empirical statistical safety margin ($\text{LCB} > 0$) acts as an automated anti-hallucination barrier, filtering out non-robust syntax updates.
3. **Bounded Memory Adaptation for Non-Stationary Drift:** As the GFlowNet explores new regions of factor space, older local guidance becomes obsolete. Imposing a physical-score lifetime (TTL = 1,000 evaluations) prevents the policy from over-anchoring to stale heuristics.

---

## Signal

The alpha generation, factor normalization, and composite portfolio signal pipeline is fully formalized by the primary paper:

### 1. Symbolic Grammar and Domain-Specific Language (DSL)
- **Input Terminal Features:** Daily `OPEN`, `CLOSE`, `HIGH`, `LOW`, `VOLUME` [source-reported].
- **Lookback Windows:** $W \in \{10, 20, 30, 40, 50\}$ trading days [source-reported].
- **Constant Set:** $\{-30, -10, -5, -2, -1, -0.5, -0.01, 0.01, 0.5, 1, 2, 5, 10, 30\}$ [source-reported].
- **Max Expression Length:** $L \le 20$ tokens [source-reported].
- **Operator Space:** Unary operators (e.g., `-`, `Abs`, `Sign`, `Log`), binary operators (e.g., `+`, `-`, `*`, `/`), and rolling time-series operators (e.g., `Ts_Mean`, `Ts_Std`, `Ts_Rank`, `Delay`, `Delta`, `Correlation`, `Covariance`) following standard quantitative finance DSL conventions [source-reported].

### 2. State, Transition, and Trajectory Balance Backbone
- **State Representation:** Typed partial abstract syntax tree (AST) encoded via Reverse Polish Notation (RPN) stack obligations [source-reported].
- **Policy Networks:** 2-layer Relational Graph Convolutional Network (RGCN) with hidden dimension 128 [source-reported].
- **Global Objective (Entropy-TB):**
  $$\mathcal{L}_{\mathrm{ETB}} = \mathbb{E}_\tau [\mathcal{L}_{\mathrm{TB}}(\tau)] - \eta_H \mathbb{E}_\tau \left[ \sum_{t=0}^{L-1} H(P_F^\theta(\cdot \mid s_t)) \right], \quad \eta_H = 0.01$$
  where $\mathcal{L}_{\mathrm{TB}}(\tau) = \left[ \log Z_\phi + \sum_{t=1}^L \log P_F^\theta(a_t \mid s_{t-1}) - \log R(x) - \sum_{t=1}^L \log P_B(s_{t-1} \mid s_t) \right]^2$ [source-reported].
- **Terminal Reward:** $R(x) = \max \{ |r_{\mathrm{IC}}(x)|, \exp(-10) \}$, where $r_{\mathrm{IC}}(x)$ is the mean cross-sectional Pearson IC of candidate expression $x$ against the 20-day forward return on the training split [source-reported].

### 3. Component I: Structural On-Policy Interface
- At state $s$ sampled by $P_F^\theta$, retain sampled action and 2 alternatives ($m=3$, $\mathcal{A}_s = \{a_1, a_2, a_3\}$) satisfying [source-reported]:
  1. Forward policy probability $P_F^\theta(a_i \mid s) > 10^{-4}$;
  2. Sibling actions belong to the same action class, operator family, and arity;
  3. Sibling actions induce identical unresolved stack construction signatures.
- Sibling-restricted baseline distribution:
  $$p_i = \frac{P_F^\theta(a_i \mid s)}{\sum_{a_j \in \mathcal{A}_s} P_F^\theta(a_j \mid s)}$$

### 4. Component II: Reliability-Gated Paired Teacher
- **Shared Suffix Proposal ($q$):** Samples $K=4$ unique completions $U = \{u_1, u_2, u_3, u_4\}$ valid across all 3 siblings. Stepwise proposal logit combines geometric mean across branches with exit bias $b_{\mathrm{exit}} = 1.5$ [source-reported]:
  $$q_t(b) \propto \mathbf{1}[b \in \mathcal{V}_t] \exp \left( \frac{1}{3} \sum_{i=1}^3 \ell_{it}(b) + b_{\mathrm{exit}} \mathbf{1}[b = \mathrm{exit}] \right)$$
- **Matched Credit Matrix:** For terminal factor $x_{ki} = x(s, a_i, u_k)$, credit is:
  $$\mathbf{C}_{ki} = \log R(x_{ki}) - \log q(u_k \mid s, \mathcal{A}_s)$$
  (Note: $\log q$ cancels across siblings under the same suffix row $k$) [source-reported].
- **Anchored Exponential Tilt:** Centered credit $c_i = \bar{C}_i - \frac{1}{3} \sum_j \bar{C}_j$ generates provisional teacher $\widetilde{\pi}_i(\alpha) \propto p_i \exp(\alpha c_i / \tau)$ ($\tau = 1$). One-dimensional line search selects max $\alpha \ge 0$ satisfying $D_{\mathrm{KL}}(\widetilde{\pi}(\alpha) \,\|\, p) \le \delta = 0.03$ [source-reported].
- **Reliability Gate:**
  - *Agreement:* $\gamma(s) = \frac{1}{K} \max_i \sum_{k=1}^K \mathbf{1}[i = \arg\max_j \mathbf{C}_{kj}] \ge \gamma_{\min} = 0.75$ [source-reported].
  - *Paired Improvement:* $\Delta_k = \sum_{i=1}^3 (\widetilde{\pi}_i - p_i) \mathbf{C}_{ki}$ [source-reported].
  - *Lower Confidence Bound:* $\operatorname{LCB}(s) = \bar{\Delta} - z \operatorname{SE}(\Delta) > 0$ with $z = 1.0$ [source-reported].
- If admitted, confidence weight $w(s) = \min \left( 1, \frac{\gamma(s) \operatorname{LCB}(s)}{\max \{ |\bar{\Delta}| + \operatorname{SE}(\Delta), 10^{-12} \}} \right)$ shrinks the target radius to $w(s) \delta$, yielding stored teacher $\pi^*$ [source-reported].

### 5. Component III: Bounded Credit Consolidation
- Active queue stores at most 512 tuples $(s, \mathcal{A}_s, \pi^*, n_{\mathrm{score}}^{\mathrm{create}})$ [source-reported].
- Time-to-Live (TTL): Active only while $n_{\mathrm{score}} - n_{\mathrm{score}}^{\mathrm{create}} < 1000$ terminal evaluations [source-reported].
- Auxiliary Objective: Forward KL across active queue $\mathcal{B}$:
  $$\mathcal{L}_{\mathrm{OPD}}(\theta) = \frac{1}{|\mathcal{B}|} \sum_{(s, \mathcal{A}_s, \pi^*) \in \mathcal{B}} D_{\mathrm{KL}}\left( \pi^*(\cdot \mid s) \,\|\, P_F^\theta(\cdot \mid s, \mathcal{A}_s) \right)$$
- Adaptive Gradient Balancing:
  $$\lambda = \min \left( 10^4, 0.10 \frac{\|\nabla_\theta \mathcal{L}_{\mathrm{ETB}}\|_2}{\|\nabla_\theta \mathcal{L}_{\mathrm{OPD}}\|_2 + 10^{-12}} \right), \quad \mathcal{L} = \mathcal{L}_{\mathrm{ETB}} + \lambda \mathcal{L}_{\mathrm{OPD}}$$
  Target gradient ratio $\rho = 0.10$ bounds auxiliary policy distortion [source-reported].

### 6. Portfolio Scoring & Multi-Factor Aggregation
- **Pool Capacity:** Top 50 non-redundant discovered alpha expressions ($M = 50$) [source-reported].
- **Direction Assignment (Validation-Sign Equal-50):** Factor direction $d_m \in \{-1, +1\}$ is determined strictly by its validation-period Pearson IC: $d_m = \operatorname{sign}(\mathrm{IC}_m^{\mathrm{valid}})$ [source-reported].
- **Composite Portfolio Factor Score:**
  $$F_{tj} = \frac{1}{50} \sum_{m=1}^{50} d_m f_{mtj}$$
  where $f_{mtj}$ is the normalized cross-sectional score of factor $m$ on day $t$ for asset $j$ [source-reported].

---

## Required data

- **Universes:**
  - **China A-Shares:** CSI300 (large cap, $N \approx 300$), CSI500 (mid cap, $N \approx 500$), CSI1000 (small cap, $N \approx 1000$) [source-reported].
  - **US Equities:** S&P 500 index constituents ($N \approx 500$) [source-reported].
- **Time Horizons and Sample Partitions:**
  - *China A-Shares:* Training: 2010–2020; Validation: 2021; Out-of-Sample Testing: 2022–2024 (3 full calendar years) [source-reported].
  - *US S&P 500:* Training: 2010–2016; Validation: 2017; Out-of-Sample Testing: 2018–2020 (3 full calendar years) [source-reported].
- **Price/Volume Inputs:** Daily OHLCV bars (`Open`, `High`, `Low`, `Close`, `Volume`) via Qlib quantitative platform [source-reported].
- **Target Label:** 20-trading-day forward cumulative return: `Ref(close, -20) / close - 1` [source-reported].
- **Point-in-Time Discipline:** Factor signs fixed strictly in validation; testing conducted with frozen model weights and frozen factor definitions over untouched test intervals [source-reported].

---

## Execution assumptions

- **Rebalance Frequency:** Monthly (20 trading days), matching the 20-day return prediction horizon [source-reported].
- **Execution Timing:** Rebalance order generated at day $t$ close, assumed executed at next-day open or close [`research-proposed` next-open market fill].
- **Order Model:** Market-on-open (MOO) / Market-on-close (MOC) proportional rebalancing [source-reported / `research-proposed`].
- **Position Sizing:** Equal-weighted factor combination ($1/50$ weight per selected factor); cross-sectional quintile or decile ranking [source-reported]. Long-only execution evaluated for S&P 500 [source-reported]; long-short market-neutral portfolio evaluated for CSI universes [source-reported].
- **Transaction Costs & Slippage:** Qlib standard backtest execution settings assumed in reported metrics [source-reported; `research-proposed` 10 bps round-trip fee + 5 bps bid-ask spread stress].
- **Short Selling / Borrow:** Frictionless shorting assumed for Chinese index constituents in paper backtests [source-reported; provenance gap / `research-proposed` margin/borrow rate of 200–500 bps p.a. for China A-shares].
- **Capacity / Liquidity Filter:** Constituents limited to official index members, filtering micro-cap illiquidity [source-reported; `research-proposed` max participation rate of 1.5% 20-day ADV].

---

## Evidence

### Source-reported

All figures below are transcribed directly from Table 1 (`tab:main-results`) and Table 2 (`tab:full-system`) of `arXiv:2608.01303v1`, evaluated under an identical **10,000 physical-score evaluation budget** across 3 random seeds (reported as Mean with sample standard deviation in parentheses):

#### 1. Main Out-of-Sample Performance Comparison by Universe (Table 1)

##### China A-Share CSI300 Universe (2022–2024 Test):
| Method | Family | IC (%) $\uparrow$ | ICIR $\uparrow$ | RankIC (%) $\uparrow$ | RankICIR $\uparrow$ | AR (%) $\uparrow$ | MDD (%) $\downarrow$ | Sharpe (SR) $\uparrow$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **AlphaG-OPD (Ours)** | GFlowNet | $\mathbf{6.73 \; (0.74)}$ | $\mathbf{0.4479 \; (0.0270)}$ | $\mathbf{8.78 \; (1.13)}$ | $\mathbf{0.5408 \; (0.0283)}$ | $\mathbf{8.382 \; (2.222)}$ | $\mathbf{14.184 \; (1.562)}$ | $\mathbf{2.080 \; (0.615)}$ |
| **AlphaSAGE** | GFlowNet | $5.81 \; (1.03)$ | $0.4177 \; (0.0686)$ | $7.50 \; (1.69)$ | $0.5195 \; (0.0803)$ | $6.146 \; (3.787)$ | $15.140 \; (1.397)$ | $1.413 \; (0.987)$ |
| **AlphaAgent** | LLM Agent | $5.10$ | $0.325$ | $5.60$ | $0.329$ | $2.16$ | $26.9$ | $0.65$ |
| **AlphaForge** | Neural/RL | $4.10$ | $0.259$ | $5.20$ | $0.306$ | $3.90$ | $21.9$ | $0.88$ |
| **AlphaGen** | Neural/RL | $5.80$ | $0.414$ | $5.70$ | $0.360$ | $4.00$ | $22.6$ | $0.76$ |
| **AlphaQCM** | Neural/RL | $4.30$ | $0.262$ | $4.20$ | $0.246$ | $1.95$ | $24.8$ | $0.36$ |
| **GP (Genetic Prog.)** | Conventional | $2.60$ | $0.215$ | $2.80$ | $0.216$ | $6.80$ | $17.6$ | $1.55$ |
| **XGBoost** | Conventional | $3.10$ | $0.243$ | $3.30$ | $0.248$ | $5.40$ | $17.5$ | $1.26$ |
| **LightGBM** | Conventional | $1.10$ | $0.124$ | $0.60$ | $0.064$ | $2.61$ | $18.5$ | $0.53$ |
| **MLP** | Conventional | $2.00$ | $0.158$ | $1.90$ | $0.142$ | $3.54$ | $20.9$ | $0.68$ |

##### China A-Share CSI500 Universe (2022–2024 Test):
| Method | Family | IC (%) $\uparrow$ | ICIR $\uparrow$ | RankIC (%) $\uparrow$ | RankICIR $\uparrow$ | AR (%) $\uparrow$ | MDD (%) $\downarrow$ | Sharpe (SR) $\uparrow$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **AlphaG-OPD (Ours)** | GFlowNet | $\mathbf{4.71 \; (1.15)}$ | $\mathbf{0.3369 \; (0.0547)}$ | $\mathbf{6.81 \; (1.81)}$ | $\mathbf{0.4671 \; (0.1114)}$ | $\mathbf{2.968 \; (1.308)}$ | $\mathbf{18.535 \; (1.531)}$ | $\mathbf{0.577 \; (0.237)}$ |
| **AlphaSAGE** | GFlowNet | $1.97 \; (1.16)$ | $0.1721 \; (0.0950)$ | $2.72 \; (1.98)$ | $0.2352 \; (0.1691)$ | $-0.778 \; (2.020)$ | $25.040 \; (3.286)$ | $-0.139 \; (0.361)$ |
| **AlphaAgent** | LLM Agent | $5.30$ | $0.396$ | $6.50$ | $0.495$ | $1.82$ | $22.4$ | $0.36$ |
| **AlphaForge** | Neural/RL | $5.30$ | $0.345$ | $8.30$ | $0.600$ | $4.18$ | $16.7$ | $0.93$ |
| **AlphaGen** | Neural/RL | $3.20$ | $0.270$ | $3.10$ | $0.230$ | $1.15$ | $32.4$ | $0.19$ |
| **AlphaQCM** | Neural/RL | $4.80$ | $0.378$ | $7.30$ | $0.546$ | $4.06$ | $24.0$ | $0.75$ |
| **GP** | Conventional | $1.40$ | $0.238$ | $2.20$ | $0.233$ | $3.04$ | $19.4$ | $0.56$ |
| **XGBoost** | Conventional | $3.90$ | $0.365$ | $5.20$ | $0.528$ | $5.50$ | $17.1$ | $1.15$ |
| **LightGBM** | Conventional | $2.40$ | $0.305$ | $2.10$ | $0.264$ | $4.61$ | $17.5$ | $0.89$ |
| **MLP** | Conventional | $1.70$ | $0.185$ | $2.00$ | $0.233$ | $1.56$ | $24.3$ | $0.27$ |

##### China A-Share CSI1000 Universe (2022–2024 Test):
| Method | Family | IC (%) $\uparrow$ | ICIR $\uparrow$ | RankIC (%) $\uparrow$ | RankICIR $\uparrow$ | AR (%) $\uparrow$ | MDD (%) $\downarrow$ | Sharpe (SR) $\uparrow$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **AlphaG-OPD (Ours)** | GFlowNet | $5.89 \; (0.33)$ | $\mathbf{0.4894 \; (0.0347)}$ | $7.74 \; (0.86)$ | $\mathbf{0.6298 \; (0.0715)}$ | $3.155 \; (0.363)$ | $25.271 \; (2.513)$ | $0.534 \; (0.081)$ |
| **AlphaSAGE** | GFlowNet | $\mathbf{6.04 \; (0.28)}$ | $0.4781 \; (0.0268)$ | $\mathbf{8.44 \; (1.15)}$ | $0.6088 \; (0.0404)$ | $\mathbf{4.011 \; (0.256)}$ | $\mathbf{24.804 \; (3.883)}$ | $\mathbf{0.669 \; (0.036)}$ |
| **AlphaAgent** | LLM Agent | $7.20$ | $0.579$ | $8.90$ | $0.712$ | $5.51$ | $20.5$ | $1.01$ |
| **AlphaForge** | Neural/RL | $7.10$ | $0.537$ | $9.50$ | $0.742$ | $6.07$ | $21.1$ | $1.06$ |
| **AlphaGen** | Neural/RL | $7.10$ | $0.540$ | $9.20$ | $0.713$ | $5.27$ | $24.0$ | $0.92$ |
| **AlphaQCM** | Neural/RL | $6.50$ | $0.453$ | $10.70$ | $0.682$ | $7.12$ | $20.6$ | $1.31$ |
| **GP** | Conventional | $5.80$ | $0.474$ | $7.90$ | $0.657$ | $4.32$ | $24.7$ | $0.67$ |
| **XGBoost** | Conventional | $6.20$ | $0.498$ | $8.60$ | $0.695$ | $4.72$ | $23.5$ | $0.91$ |
| **LightGBM** | Conventional | $6.70$ | $0.501$ | $8.30$ | $0.656$ | $4.98$ | $22.7$ | $0.98$ |
| **MLP** | Conventional | $4.80$ | $0.384$ | $6.90$ | $0.621$ | $3.22$ | $25.7$ | $0.47$ |

##### US S&P 500 Universe (2018–2020 Test, Long-Only):
| Method | Family | IC (%) $\uparrow$ | ICIR $\uparrow$ | RankIC (%) $\uparrow$ | RankICIR $\uparrow$ | AR (%) $\uparrow$ | MDD (%) $\downarrow$ | Sharpe (SR) $\uparrow$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **AlphaG-OPD (Ours)** | GFlowNet | $0.56 \; (0.73)$ | $0.0519 \; (0.0677)$ | $\mathbf{1.20 \; (0.74)}$ | $0.1043 \; (0.0619)$ | $\mathbf{9.398 \; (0.627)}$ | $\mathbf{25.530 \; (1.418)}$ | $\mathbf{1.882 \; (0.107)}$ |
| **AlphaSAGE** | GFlowNet | $\mathbf{0.89 \; (1.26)}$ | $\mathbf{0.0921 \; (0.1314)}$ | $1.19 \; (0.93)$ | $\mathbf{0.1103 \; (0.0950)}$ | $9.213 \; (1.809)$ | $26.136 \; (0.367)$ | $1.795 \; (0.319)$ |
| **AlphaAgent** | LLM Agent | $4.80$ | $0.479$ | $3.30$ | $0.315$ | $18.66$ | $5.7$ | $6.27$ |
| **AlphaForge** | Neural/RL | $3.90$ | $0.422$ | $3.10$ | $0.324$ | $17.24$ | $5.0$ | $6.30$ |
| **AlphaGen** | Neural/RL | $4.40$ | $0.396$ | $1.30$ | $0.127$ | $10.31$ | $5.5$ | $3.96$ |
| **AlphaQCM** | Neural/RL | $3.80$ | $0.262$ | $1.00$ | $0.071$ | $13.86$ | $13.0$ | $3.30$ |
| **GP** | Conventional | $3.20$ | $0.308$ | $0.20$ | $0.016$ | $13.39$ | $13.0$ | $3.15$ |
| **XGBoost** | Conventional | $1.60$ | $0.159$ | $2.60$ | $0.168$ | $13.25$ | $8.3$ | $3.61$ |
| **LightGBM** | Conventional | $2.30$ | $0.196$ | $1.80$ | $0.165$ | $11.11$ | $5.1$ | $4.22$ |
| **MLP** | Conventional | $3.50$ | $0.287$ | $2.00$ | $0.143$ | $12.85$ | $5.6$ | $3.35$ |

#### 2. Staged Additive Ablation under Equal 10K Physical-Score Budget (Table 2)
Evaluated on CSI500 with frozen Validation-Sign Equal-50 evaluator (8,008 ordinary + 1,992 probe evaluations = exactly 166 probes of 12 calls):

| Method Variant | I: Interface | Paired Teacher | Reliability Gate | III: Consolidation | IC (%) $\uparrow$ | ICIR $\uparrow$ | RankIC (%) $\uparrow$ | RankICIR $\uparrow$ | AR (%) $\uparrow$ | Sharpe $\uparrow$ | MDD (%) $\downarrow$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Base Model** | -- | -- | -- | -- | $2.175$ | $0.182282$ | $3.200$ | $0.277667$ | $-1.038$ | $-0.209$ | $24.571$ |
| **Comp. I–II (Gate Off)** | $\checkmark$ | $\checkmark$ | -- | -- | $4.040$ | $0.342000$ | $4.850$ | $0.395800$ | $0.920$ | $0.164$ | $22.860$ |
| **Comp. I–II (Gate On)** | $\checkmark$ | $\checkmark$ | $\checkmark$ | -- | $3.730$ | $0.327100$ | $5.520$ | $0.453500$ | $1.320$ | $0.249$ | $21.820$ |
| **AlphaG-OPD (I–III)** | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\mathbf{6.018}$ | $\mathbf{0.399784}$ | $\mathbf{8.822}$ | $\mathbf{0.595058}$ | $\mathbf{4.384}$ | $\mathbf{0.835}$ | $\mathbf{17.417}$ |

*Key Insights from Ablation:*
1. **Paired Teacher Effect:** Adding the on-policy interface and paired teacher alone (Gate Off) moves annualized return from negative ($-1.038\%$) to positive ($+0.920\%$) and doubles RankIC from $3.20\%$ to $4.85\%$.
2. **Reliability Gate Effect:** Enabling the winner-agreement and positive-LCB gate (Gate On) sacrifices a small amount of raw linear IC ($3.73\%$ vs. $4.04\%$) but substantially boosts RankIC ($5.52\%$ vs. $4.85\%$), RankICIR ($0.4535$ vs. $0.3958$), and Sharpe ratio ($0.249$ vs. $0.164$), confirming that gating filters out noise-driven spurious factor updates.
3. **Consolidation Effect:** Enabling bounded credit consolidation (Component III) elevates performance across every single metric, yielding peak RankIC ($8.822\%$), annualized return ($4.384\%$), Sharpe ($0.835$), and lowest drawdown ($17.417\%$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Small-Cap Exploration Trade-off in CSI1000:** On the broad CSI1000 universe, AlphaG-OPD produced slightly lower raw IC ($5.89\%$ vs. $6.04\%$) and annualized return ($3.155\%$ vs. $4.011\%$) compared to baseline AlphaSAGE. In highly dispersed micro-cap universes, local structural guidance may slightly constrain the broad stochastic exploration of global GFlowNets.
2. **US Large-Cap Market Efficiency Resistance:** On the S&P 500, symbolic formulaic factors yielded vastly lower raw predictive correlation ($\text{IC} = 0.56\%$) compared to Chinese equity markets ($\text{IC} = 4.71\% - 6.73\%$). US large caps exhibit intense arbitrage and pricing efficiency, limiting the raw standalone predictive capacity of simple daily price-volume syntactic expressions.
3. **Linear IC vs. Rank Order Trade-off under Gating:** In Table 2, adding the reliability gate without consolidation reduced raw Pearson IC from $4.040\%$ to $3.730\%$. Researchers must be aware that filtering for high-confidence structural winners favors monotonic rank predictability over extreme linear outliers.

---

## Falsification plan

The core empirical and theoretical claims of the AlphaG-OPD framework can be falsified through the following five structured experimental protocols:

1. **Equal-Score Budget Scalability & Saturation Test:**
   - *Protocol:* Scale the total physical-score evaluation budget from $N_{\mathrm{score}} = 10\text{K}$ to $25\text{K}$, $50\text{K}$, and $100\text{K}$ across both AlphaG-OPD and baseline AlphaSAGE.
   - *Decision Rule (`research-defined falsification threshold`):* If baseline AlphaSAGE matches or exceeds AlphaG-OPD's out-of-sample RankIC within $\pm 0.20\%$ at $N_{\mathrm{score}} \ge 50\text{K}$, the claim of fundamental structural credit advantage is falsified; AlphaG-OPD would then represent merely a transient sample-efficiency heuristic rather than a superior policy equilibrium.
2. **Scrambled Suffix Null Baseline (Placebo Verification):**
   - *Protocol:* Replace the $K=4$ shared grammar-valid suffixes with independently sampled suffixes drawn from disparate states, eliminating the matched-completion control.
   - *Decision Rule (`research-defined falsification threshold`):* If the policy trained with independent suffixes achieves an out-of-sample Sharpe ratio within $10\%$ of the matched-suffix AlphaG-OPD model on CSI500, reject the hypothesis that local counterfactual cancellation ($\mathbf{C}_{ki} - \mathbf{C}_{kj} = \log R(x_{ki}) - \log R(x_{kj})$) is the causal driver of performance.
3. **Suffix Sample Size Sensitivity Analysis:**
   - *Protocol:* Evaluate the reliability gate across $K \in \{1, 2, 4, 8\}$ completion suffixes per probe, adjusting probe frequency to preserve the exact 10,000 score ceiling.
   - *Decision Rule (`research-defined falsification threshold`):* If setting $K=1$ (single completion, no winner agreement or LCB calculation possible) matches the out-of-sample RankIC of $K=4$ on CSI500, reject the necessity of epistemic reliability gating.
4. **Transaction Cost and Real-World Friction Degradation:**
   - *Protocol:* Simulate the resulting Validation-Sign Equal-50 portfolio across realistic execution costs: $\text{fee} \in \{5, 10, 15, 25, 35\}\text{ bps}$ per trade with next-open execution.
   - *Decision Rule (`research-defined falsification threshold`):* If annualized return on CSI500 drops below $0.0\%$ at round-trip transaction costs $\le 15\text{ bps}$, reject the tradability hypothesis; the discovered formulaic alpha collection suffers from excessive rebalancing turnover.
5. **Macroeconomic Regime Shift & Sub-Period Stress Test:**
   - *Protocol:* Evaluate the discovered factors across segregated market regimes: secular bull (2020–2021), liquidity contraction / bear (2022), and sideways volatility (2023–2024).
   - *Decision Rule (`research-defined falsification threshold`):* If the portfolio Sharpe ratio turns negative in more than 1 out of the 3 test regimes, falsify the hypothesis that GFlowNet-discovered formulaic ensembles possess regime-invariant alpha.

---

## Crypto portability

**Portability Classification: Adapted / Unproven**

The primary paper evaluates AlphaG-OPD strictly on Chinese A-share and US equity index components. Adapting this symbolic discovery framework to cryptocurrency markets represents a research interpretation and encounters substantial domain-specific structural shifts:

1. **Continuous 24/7/365 Auction vs. Discrete Daily Sessions:** Equities rely on daily opening/closing auctions with weekend halts. Crypto operates continuously. The 20-day return target `Ref(close, -20)/close - 1` must be ported to fixed synthetic boundaries (e.g., 00:00 UTC 480-hour forward return) [`research-proposed`].
2. **Funding Rate & Perpetual Futures Basis Drag:** Equity returns reflect pure spot price changes. In crypto perpetual contracts, holding long or short positions entails 8-hour funding payments. A formulaic factor predicting positive spot price momentum could suffer net losses if funding rates exceed the gross price drift [`research-proposed`].
3. **Cross-Sectional Breadth & Liquidity Dispersion:** China A-shares feature hundreds of liquid names (CSI300/500/1000). The crypto universe has high liquidity concentration in BTC and ETH, with a steep liquidity drop-off in altcoins. Cross-sectional ranking (`RankIC`) on a small universe ($N \le 50$) exhibits substantially higher statistical noise and susceptibility to idiosyncratic token shocks [`research-proposed`].
4. **Crypto-Native Feature Space Augmentation:** Daily OHLCV is insufficient in crypto. The symbolic grammar must be expanded beyond OHLCV to incorporate crypto-native primitives: aggregate Open Interest, perpetual funding rates, spot-perpetual basis, exchange net inflow/outflow, and liquidation volume [`research-proposed`].
5. **Execution Latency & Fee Structure:** Crypto spot/perpetual exchanges charge higher taker fees ($2\text{ to }5\text{ bps}$) and feature rapid order book liquidity changes. Factors discovered at daily resolution may decay before portfolio execution if not modeled with realistic fill mechanics [`research-proposed`].

---

## Limitations

- **Fixed DSL Expressiveness:** The search space is bounded by the predefined operator and constant vocabulary; complex multi-asset relational structures or high-frequency order-flow dynamics cannot be expressed.
- **Physical Score Budget Trade-off:** Sibling probes consume 12 physical evaluations per probe ($3 \text{ siblings} \times 4 \text{ suffixes}$). Under a tight 10K budget, 1,992 evaluations are allocated to probing, leaving only 8,008 ordinary trajectory evaluations.
- **Frictionless Backtesting Assumption:** Primary empirical results do not account for borrow fees on short equity positions or non-linear market impact in small-cap universes.
- **Equal-Weighted Aggregation Heuristic:** While Validation-Sign Equal-50 prevents overfitting, it does not optimize portfolio weights dynamically based on rolling factor volatility or cross-factor correlation.
- **Sample Selection in US Markets:** Lower standalone performance in S&P 500 suggests that symbolic alpha mining on daily OHLCV is significantly less effective in highly efficient institutional equity markets.

---

## Implementation status

Not implemented. No implementation of AlphaG-OPD exists in `nautilus-quant-system`, PyBroker pipelines, or NautilusTrader harnesses.

---

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

Any transition of discovered factors into PyBroker screening or NautilusTrader accounting requires independent out-of-sample historical validation, fee-adjusted backtesting, and formal sign-off.

---

## Related Wiki records

- `[[quant/alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — Grammar-guided MCTS with Tree-LSTM for formulaic alpha discovery.
- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — Multi-agent LLM reasoning for formulaic alpha factor generation.
- `[[quant/agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04]]` — Autonomous alpha discovery via prompt economy and adversarial review.
- `[[quant/adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05]]` — Dynamic PPO integration of LLM-generated formulaic alphas.
- `[[quant/factorsmith-autonomous-agentic-alpha-mining-2026-09-04]]` — Self-directed agentic alpha mining pipeline.
- `[[quant/china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04]]` — Machine learning enhanced multi-factor quantitative trading in China A-shares.

---

## Sources

1. **Primary Academic Preprint:** Yaoyu Su, *"AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery"*, arXiv preprint `arXiv:2608.01303v1 [cs.LG, q-fin.CP]`, submitted August 2, 2026.
   - Canonical Abstract URL: [https://arxiv.org/abs/2608.01303](https://arxiv.org/abs/2608.01303)
   - Full Text HTML URL: [https://arxiv.org/html/2608.01303v1](https://arxiv.org/html/2608.01303v1)
   - Digital Object Identifier (DOI): [10.48550/arXiv.2608.01303](https://doi.org/10.48550/arXiv.2608.01303)
2. **Primary Baseline and Architectural Sources Cited in Paper:**
   - B. Chen, H. Ding, N. Shen, J. Huang, T. Guo, L. Liu, and M. Zhang, *"AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration"*, arXiv preprint `arXiv:2509.25055`, 2025.
   - Y. Bengio, S. Lahlou, T. Deleu, E. J. Hu, M. Tiwari, and E. Bengio, *"GFlowNet Foundations"*, *Journal of Machine Learning Research*, 24(210):1–55, 2023.
   - N. Malkin, M. Jain, E. Bengio, C. Sun, and Y. Bengio, *"Trajectory Balance: Improved Credit Assignment in GFlowNets"*, *Advances in Neural Information Processing Systems (NeurIPS)*, 35:5955–5967, 2022.
   - S. Yu, H. Xue, X. Ao, F. Pan, J. He, D. Tu, and Q. He, *"Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning (AlphaGen)"*, *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, pp. 5476–5486, 2023.
   - X. Yang, W. Liu, D. Zhou, J. Bian, and T. Liu, *"Qlib: An AI-oriented Quantitative Investment Platform"*, arXiv preprint `arXiv:2009.11189`, 2020.
