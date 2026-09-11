---
schema: strategy-research-record-v1
title: "AlphaRJM — Reward-Jump Memory for Stochastic Return-Guided Formulaic Alpha Discovery"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - symbolic-alpha
  - formulaic-alpha
  - reinforcement-learning
  - sde
  - distributional-rl
  - cross-sectional-equity
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - "https://doi.org/10.48550/arXiv.2609.08581"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaRJM — Reward-Jump Memory for Stochastic Return-Guided Formulaic Alpha Discovery

## Provenance

- **Primary source:** Sayan Dhan and Selvaraju Natarajan (Department of Mathematics, Indian Institute of Technology Guwahati, `s.dhan@iitg.ac.in`, `nselvaraju@iitg.ac.in`). *"AlphaRJM: Reward-Jump Memory for Stochastic Return-Guided Alpha Discovery"*, arXiv preprint `arXiv:2609.08581v1 [cs.LG]`, submitted September 8, 2026, announced September 9, 2026.
- **Canonical DOI:** [10.48550/arXiv.2609.08581](https://doi.org/10.48550/arXiv.2609.08581).
- **Traceable URLs:**
  - Abstract: [https://arxiv.org/abs/2609.08581](https://arxiv.org/abs/2609.08581)
  - Full-text HTML: [https://arxiv.org/html/2609.08581v1](https://arxiv.org/html/2609.08581v1)
  - PDF: [https://arxiv.org/pdf/2609.08581v1](https://arxiv.org/pdf/2609.08581v1)
- **Primary Source Verification:** The primary source paper PDF (26 pages) and arXiv HTML full text were directly retrieved and inspected. All empirical metrics, mathematical specifications, architecture dimensions, ablation results, and baseline figures trace directly to Sections 3–4, Appendices B–F, and Tables 1–5 of `arXiv:2609.08581v1`.
- **Deduplication Audit:** Zero prior records in `alpha-strategy-research` cite `arXiv:2609.08581`, Sayan Dhan, or Selvaraju Natarajan. Existing symbolic alpha mining records (`alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05.md` and `alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05.md`) evaluate GFlowNets and MCTS Tree-LSTMs, respectively; neither implements event-driven Reward-Jump Memory across formula episodes nor an action-conditioned continuous-time SDE return critic with distributional Bellman particle learning.

## Economic mechanism

### Source-reported

Formulaic alphas are human-interpretable symbolic mathematical expressions mapping historical price, volume, and financial variables to forward predictive signals. Automating their discovery is challenging because candidate utility is intrinsically pool-dependent: a formula's economic value depends on its marginal contribution to the existing ensemble rather than its standalone correlation. In such environments, informative feedback occurs primarily when a complete formula is evaluated on historical data, introducing two systemic bottlenecks:
1. **Persistent History Loss:** The retained alpha pool records only accepted/retained formulas. When candidates are rejected, replaced, or invalid, this terminal evaluation feedback is discarded. Consequently, the search agent cannot condition future exploration on previous negative or marginal outcomes.
2. **Delayed Return Uncertainty:** At intermediate token construction steps, the downstream payoff of an action is highly uncertain because it depends on the syntax of the formula completed steps later and the pool state against which it will be evaluated.

AlphaRJM resolves these bottlenecks by coupling two mechanisms:
- **Reward-Jump Memory (RJM):** An event-driven latent memory state $H_t \in \mathbb{R}^8$ that remains strictly invariant during token-level construction ($\delta_t = 0$) and undergoes an event-triggered jump $J_t$ only upon terminal formula evaluation ($\delta_t = 1$), driven by the realized ensemble IC increment $\Delta \text{IC}$ and the categorical outcome $o_t \in \{\text{accepted}, \text{replaced}, \text{rejected}, \text{invalid}\}$.
- **Action-Conditioned SDE Return Critic:** An internal stochastic process $dZ_\tau^{t,a} = \kappa_{t,a}(\mu_{t,a} - Z_\tau^{t,a}) d\tau + \sigma_{t,a} dB_\tau$ simulating future discounted search return distributions via particles, enabling uncertainty-aware action scoring during symbolic policy unrolling.

### Research interpretation

The core financial mechanism underlying the discovered alpha expressions is cross-sectional equity predictability driven by behavioral momentum, price-volume divergence, and liquidity normalization:
1. **Ensemble Non-Redundancy:** By rewarding candidates strictly on marginal Information Coefficient ($\Delta \text{IC}$) relative to an equal/ridge-weighted pool of 50 alphas, the framework systematically penalizes redundant momentum or mean-reversion signals and incentivizes orthogonal features.
2. **Search Regimes and Rejection Memory:** Retaining memory of rejected formula trajectories across episodes acts as a soft tabu / exploration bias. The agent avoids repeatedly traversing syntactically distinct but economically redundant operator subtrees that previously led to rejected candidates.
3. **Exploration under Epistemic Search Risk:** The SDE return critic quantifies the variance $\hat{V}_{t,a}$ of future discovery returns. An uncertainty-seeking score bonus ($c_n \sqrt{\hat{V}_{t,a}}$) promotes early structural diversity across operators before annealing into greedy exploitation of high-expected-return formula subtrees.

## Signal

The trading signal generated by AlphaRJM is an ensemble cross-sectional rank/score produced by evaluating the discovered pool of formulaic alphas:

- **Signal Formation Timestamp:** At each daily market close $d$, after market data is finalized (source-reported: China A-share daily close; execution modeled at close-to-close or open-to-close).
- **Alpha Pool Construction:**
  - Up to $K_{\text{pool}} = 50$ symbolic expressions retained in pool $\mathcal{P}$.
  - Grammar vocabulary consists of 62 selectable actions (operators: arithmetic, time-series operators `Ts_Mean`, `Ts_Std`, `Ts_Max`, `Ts_Min`, `Correlation`, etc.; operands: open, high, low, close, volume, vwap, and constant tokens).
  - Maximum token length $L_{\max} = 20$.
  - Beginning-of-expression token (BEG) and padding (PAD) are input-only; separator (SEP) terminates the expression.
  - Length-dependent early-stop probability: $p_{\text{stop},t} = p_{\text{mask}} \frac{\ell_t^{\text{state}}}{L_{\max}}$ with $p_{\text{mask}} = 1.0$.
- **Pool Weighting & Optimization:**
  - The alpha pool $\mathcal{P} = \{\alpha_1, \ldots, \alpha_J\}$ ($J \le 50$) forms an ensemble prediction:
    $$\hat{y}_{i,d} = \sum_{j=1}^J w_j \alpha_j(X_{i,d})$$
  - Ensemble coefficients $w_j$ are jointly optimized on training data via ridge regression / linear combination to maximize weighted ensemble Information Coefficient $Q(\mathcal{P}) = \text{IC}(\hat{y}, y)$.
  - Candidate replacement rule: If pool is full ($J=50$), the candidate and existing members are jointly reweighted. If the candidate receives the smallest absolute weight, it is rejected; otherwise, the lowest-weight existing alpha is evicted and the candidate is marked as replaced.
- **Target Prediction Horizon:**
  - Standard benchmark: $h = 20$ trading days forward return:
    $$y_{i,d}^{(20)} = \frac{C_{i,d+20}}{C_{i,d}} - 1$$
  - Long-horizon benchmark: $h = 42$ trading days forward return:
    $$y_{i,d}^{(42)} = \frac{C_{i,d+42}}{C_{i,d}} - 1$$
- **Downstream Portfolio Selection:**
  - Daily cross-sectional ranking across all valid stocks in the universe.
  - Long selection: Top quintile ($\mathcal{T}_d = \text{top } 20\%$ of stocks by $\hat{y}_{i,d}$).
  - Benchmark accumulation daily return:
    $$R_d = \frac{1}{h} \frac{1}{|\mathcal{T}_d|} \sum_{i \in \mathcal{T}_d} y_{i,d}^{(h)}$$
- **Operational Rules (`research-proposed`):**
  - Cross-sectional dollar-neutral long/short extension: Long top 20%, short bottom 20%, equal-weighted within quantile (`research-proposed`).
  - Rebalance cadence: Daily rolling rebalance with $1/h$ fraction turnover (`research-proposed`).
  - Signal winsorization / clipping: Cross-sectional z-score clipped to $[-3.0, 3.0]$ (`research-proposed`).

## Required data

- **Instruments:** China A-Share listed equities across CSI300, CSI500, CSI800, and CSI1000 indices.
- **Universe Filter:** Historical index constituents. Survivorship-bias free database via Qlib.
- **Venue:** Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE).
- **Market Type:** Spot equity.
- **Timeframe:** Daily bars (OHLCV).
- **Price/Volume Fields:**
  - Daily `open`, `high`, `low`, `close`, `volume`, `vwap`.
  - Target forward returns: `Ref(CLOSE, -h) / CLOSE - 1`.
- **Sample Partitions:**
  - Training period: January 1, 2010 – December 31, 2020 (11 years).
  - Validation period: January 1, 2021 – December 31, 2021 (1 year).
  - Testing period: January 1, 2022 – December 31, 2024 (3 years out-of-sample).
- **Point-in-time / Availability:** Strictly chronological train/val/test split. All formulaic feature evaluations use strictly backward-looking time-series windows (`Ts_*` operators).
- **Missing-data Handling:** Invalid, unlisted, suspended, or zero-volume stock-days are excluded from cross-sectional ranking. Imputation is not used.

## Execution assumptions

- **Execution Timing:** Next-day open execution or same-day close execution (source models return accumulation via rolling $1/h$ forward return).
- **Fill Model:** Perfect execution at closing/opening bar price (`source-reported` in benchmark Qlib accumulation; unmodeled real market friction).
- **Transaction Costs & Slippage:** Omitted in raw IC/RIC and primary cumulative wealth curves (`source-reported` protocol from Qlib/AlphaSAGE benchmark). Explicit fee/slippage modeling is absent in the primary paper.
- **Borrow / Shorting:** The primary paper implements a long-only top-quintile (top 20%) portfolio. Shorting is not required for the reported cumulative wealth curves.
- **Execution Assumptions (`research-proposed`):**
  - Taker fee: 5 bps ($0.05\%$) per side (`research-proposed`).
  - Stamp duty (China equities): 5 bps ($0.05\%$) on sells (`research-proposed`).
  - Slippage: 5 bps ($0.05\%$) linear impact estimate (`research-proposed`).
  - Capacity: Estimated at $10M–$50M AUM for CSI300/CSI500, dropping to <$5M AUM for illiquid CSI1000 tails (`research-proposed`).

## Evidence

### Source-reported

All metrics trace directly to Dhan & Natarajan (arXiv:2609.08581v1, Sections 4.1–4.4, Appendices D–E, Tables 1–5):

#### 1. Primary Benchmark (h = 20 days, Test Period 2022–2024, Mean ± Std over 4 Random Seeds 0–3, Table 1):

| Universe | Model | IC | ICIR | RIC | RICIR |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CSI300** | MLP | 0.030 ± 0.017 | 0.218 ± 0.119 | 0.035 ± 0.024 | 0.269 ± 0.186 |
| | LightGBM | 0.024 ± 0.003 | 0.242 ± 0.028 | 0.020 ± 0.001 | 0.191 ± 0.010 |
| | Neural ODE | 0.037 ± 0.004 | 0.260 ± 0.028 | 0.032 ± 0.006 | 0.214 ± 0.040 |
| | Neural SDE | 0.032 ± 0.005 | 0.239 ± 0.040 | 0.026 ± 0.005 | 0.188 ± 0.035 |
| | AlphaGen | 0.041 ± 0.011 | 0.302 ± 0.080 | **0.046 ± 0.021** | 0.326 ± 0.156 |
| | AlphaQCM | 0.039 ± 0.007 | 0.276 ± 0.051 | 0.043 ± 0.009 | 0.301 ± 0.073 |
| | AlphaSAGE | 0.033 ± 0.016 | 0.246 ± 0.080 | 0.037 ± 0.017 | 0.266 ± 0.088 |
| | **AlphaRJM (Ours)** | **0.042 ± 0.007** | **0.307 ± 0.058** | **0.046 ± 0.003** | **0.331 ± 0.038** |
| **CSI500** | MLP | 0.031 ± 0.011 | 0.269 ± 0.088 | 0.034 ± 0.018 | 0.299 ± 0.162 |
| | LightGBM | 0.027 ± 0.003 | 0.311 ± 0.027 | 0.031 ± 0.007 | 0.364 ± 0.077 |
| | Neural ODE | 0.029 ± 0.002 | 0.239 ± 0.014 | 0.028 ± 0.002 | 0.218 ± 0.018 |
| | Neural SDE | 0.025 ± 0.005 | 0.215 ± 0.030 | 0.024 ± 0.007 | 0.186 ± 0.055 |
| | AlphaGen | 0.036 ± 0.005 | 0.273 ± 0.025 | 0.041 ± 0.007 | 0.339 ± 0.061 |
| | AlphaQCM | 0.035 ± 0.007 | 0.296 ± 0.053 | 0.042 ± 0.012 | 0.360 ± 0.085 |
| | AlphaSAGE | 0.041 ± 0.007 | 0.336 ± 0.039 | **0.059 ± 0.016** | 0.497 ± 0.061 |
| | **AlphaRJM (Ours)** | **0.046 ± 0.014** | **0.379 ± 0.159** | **0.059 ± 0.015** | **0.523 ± 0.173** |
| **CSI800** | MLP | 0.015 ± 0.007 | 0.176 ± 0.082 | 0.018 ± 0.013 | 0.206 ± 0.152 |
| | LightGBM | 0.026 ± 0.003 | 0.305 ± 0.035 | 0.025 ± 0.004 | 0.286 ± 0.045 |
| | Neural ODE | 0.026 ± 0.002 | 0.237 ± 0.024 | 0.024 ± 0.003 | 0.197 ± 0.033 |
| | Neural SDE | 0.028 ± 0.003 | 0.264 ± 0.020 | 0.028 ± 0.003 | 0.239 ± 0.022 |
| | AlphaGen | 0.028 ± 0.004 | 0.258 ± 0.054 | 0.039 ± 0.007 | 0.344 ± 0.088 |
| | AlphaQCM | 0.029 ± 0.017 | 0.260 ± 0.147 | 0.041 ± 0.019 | 0.332 ± 0.150 |
| | AlphaSAGE | 0.025 ± 0.020 | 0.208 ± 0.159 | **0.045 ± 0.015** | **0.396 ± 0.082** |
| | **AlphaRJM (Ours)** | **0.036 ± 0.007** | **0.339 ± 0.027** | 0.043 ± 0.007 | 0.371 ± 0.048 |

#### 2. Long-Horizon Benchmark (h = 42 days, Seed 0, Table 2):

| Universe | Model | IC | RIC |
| :--- | :--- | :--- | :--- |
| **CSI300** | MLP | 0.046 | 0.056 |
| | LightGBM | 0.027 | 0.026 |
| | Neural ODE | 0.014 | 0.014 |
| | Neural SDE | 0.007 | 0.005 |
| | AlphaGen | 0.021 | 0.027 |
| | AlphaQCM | 0.045 | 0.062 |
| | AlphaSAGE | 0.025 | 0.043 |
| | **AlphaRJM (Ours)** | **0.046** | **0.066** |
| **CSI500** | MLP | 0.041 | 0.050 |
| | LightGBM | 0.031 | 0.035 |
| | Neural ODE | 0.028 | 0.033 |
| | Neural SDE | 0.019 | 0.015 |
| | AlphaGen | 0.034 | 0.044 |
| | AlphaQCM | 0.044 | 0.052 |
| | AlphaSAGE | 0.033 | 0.050 |
| | **AlphaRJM (Ours)** | **0.051** | **0.065** |

#### 3. Component Ablation on CSI300 (Seed 0, Table 4):

| Model Variant | IC | ICIR |
| :--- | :--- | :--- |
| **AlphaRJM (Full)** | **0.0480** | **0.3700** |
| w/o SDE Return Critic (replaced by QCM/IQN critic) | 0.0362 | 0.2687 |
| w/o Distributional Loss (removed energy distance $\lambda_{\text{ED}}$) | 0.0453 | 0.3085 |
| w/o Persistent Memory (removed recurrent $H_t$) | 0.0434 | 0.3053 |

#### 4. Large-Universe Generalization on CSI1000 (Seeds 0–1, Mean ± Std, Table 5):

| Method | IC | ICIR | RIC | RICIR |
| :--- | :--- | :--- | :--- | :--- |
| MLP | 0.049 ± 0.004 | 0.464 ± 0.034 | 0.063 ± 0.008 | 0.556 ± 0.076 |
| LightGBM | 0.053 ± 0.000 | 0.556 ± 0.006 | 0.063 ± 0.000 | **0.668 ± 0.027** |
| Neural ODE | 0.054 ± 0.001 | 0.513 ± 0.020 | 0.066 ± 0.002 | 0.585 ± 0.008 |
| Neural SDE | 0.054 ± 0.000 | 0.510 ± 0.000 | 0.063 ± 0.001 | 0.574 ± 0.006 |
| AlphaGen | 0.072 ± 0.010 | 0.513 ± 0.038 | 0.089 ± 0.011 | 0.627 ± 0.035 |
| AlphaQCM | 0.070 ± 0.008 | **0.563 ± 0.002** | 0.078 ± 0.016 | 0.610 ± 0.080 |
| AlphaSAGE | 0.056 ± 0.007 | 0.517 ± 0.032 | 0.068 ± 0.004 | 0.579 ± 0.018 |
| **AlphaRJM (Ours)** | **0.076 ± 0.003** | 0.505 ± 0.003 | **0.102 ± 0.009** | 0.648 ± 0.013 |

### Independently reproduced

Not independently reproduced. All figures and claims are third-party results reported by Dhan & Natarajan (2026, arXiv:2609.08581v1). No internal simulation or code execution has been conducted in our stack.

### Negative evidence

- **Search Budget Cost:** Training requires 10,000 formula evaluations, each calculating rolling cross-sectional correlations over 11 years of daily equity data. Simulating the SDE return critic with Euler–Maruyama particle trajectories adds substantial computational overhead relative to simple genetic programming.
- **Turnover and Market Frictions:** The paper reports raw correlation metrics (IC/RIC) and theoretical wealth accumulation without realistic execution friction, bid-ask spread, or stamp duty. In Chinese equity markets, frequent portfolio turnover can consume substantial alpha.
- **Rank Metric Performance on Broad Universes:** On CSI800, AlphaSAGE achieved higher RIC ($0.045 \pm 0.015$ vs $0.043 \pm 0.007$) and higher RICIR ($0.396 \pm 0.082$ vs $0.371 \pm 0.048$) than AlphaRJM. Similarly, on CSI1000, LightGBM and AlphaQCM achieved higher ICIR / RICIR.

## Falsification plan

To falsify the claim that AlphaRJM produces genuine, durable formulaic alpha superior to existing symbolic methods:

1. **Transaction Cost & Turnover Stress:**
   - *Protocol:* Execute the top-20% portfolio with realistic transaction fees ($0.05\%$ taker fee + $0.05\%$ stamp duty + 5 bps slippage).
   - *Decision Rule (`research-defined falsification threshold`):* If net annualized return degrades by $> 65\%$ or net Sharpe drops below $0.50$, the strategy is falsified as transaction-cost unviable.
2. **True Out-of-Sample Holdout (2025–2026):**
   - *Protocol:* Evaluate the pool discovered on 2010–2020 training data on recent out-of-sample data (2025–2026).
   - *Decision Rule (`research-defined falsification threshold`):* If test RankIC drops below $0.015$ or ICIR drops below $0.15$, the symbolic discovery is falsified as overfit to the 2022–2024 test regime.
3. **Ablation Falsification (Memory vs Random Shuffle):**
   - *Protocol:* Train AlphaRJM with randomly permuted terminal memory jumps $J_t$.
   - *Decision Rule (`research-defined falsification threshold`):* If the randomized memory variant matches or exceeds the true AlphaRJM RankIC within $\pm 0.002$, the hypothesis that event-driven sequential evaluation history guides symbolic discovery is falsified.
4. **Placebo Shuffled-Target Test:**
   - *Protocol:* Train AlphaRJM on cross-sectionally scrambled forward returns.
   - *Decision Rule (`research-defined falsification threshold`):* If the discovered expressions produce positive out-of-sample IC ($> 0.010$), the framework suffers from structural look-ahead leakage.

## Crypto portability

**Portability rating:** `adapted` / `unproven`

The primary paper evaluates Chinese A-share cash equities exclusively. Application to cryptocurrency markets is entirely a research interpretation and has not been demonstrated by the authors:

- **Venue Fragmentation & Data Alignment:** Equities trade on unified synchronous venues (SSE/SZSE) with centralized closing prices. Crypto spot and perpetual markets trade 24/7 across multiple fragmented venues (Binance, OKX, Bybit), requiring strict UTC timestamp normalization and funding rate accounting.
- **Universe Definition & Survivorship:** Crypto tokens exhibit extreme turnover, rapid delistings, and illiquid tails. Applying AlphaRJM to crypto requires a dynamic liquidity-filtered universe (e.g., top 50 perpetual contracts by 30-day median dollar volume) rather than fixed index constituent lists (`research-proposed`).
- **Feature Set Adaptation:** Traditional equity features (`open`, `high`, `low`, `close`, `volume`, `vwap`) must be augmented with crypto-native market microstructure features: perpetual funding rates, open interest changes, liquidation cascades, and basis spreads (`research-proposed`).
- **Execution & Shorting:** In crypto perpetuals, two-sided trading is native and symmetrical, allowing direct implementation of dollar-neutral long/short portfolios, unlike Chinese equities where shorting is heavily restricted.

## Limitations

- **No Transaction Costs Modeled:** All reported empirical metrics are gross of fees, commissions, slippage, and market impact (`source-reported` limitation).
- **CPU Benchmark Scope:** All experiments were run on an Apple Mac mini CPU using Qlib. High-throughput execution across millions of candidate expressions was bounded by a 10,000-episode budget.
- **Univariate Particle SDE:** The SDE critic models discovery return as a scalar linear mean-reverting process with constant diffusion, which may not capture multi-modal or heavy-tailed search return landscapes.
- **Static Alpha Pool Reweighting:** Linear ensemble weighting is recomputed inside the training loop; dynamic regime-adaptive weighting during live execution was not investigated.
- **Traditional Asset Only:** Zero crypto market testing was conducted in the cited source.

## Implementation status

`not-implemented`. No implementation of AlphaRJM, Reward-Jump Memory, or the action-conditioned SDE return critic exists in our research repository, PyBroker, or NautilusTrader stacks.

## Adoption boundary

This record is research material only. Presence in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `[[alphag-opd-reliability-gated-sibling-counterfactuals-symbolic-alpha-2026-09-05]]` — Parallel formulaic alpha discovery using GFlowNets and sibling counterfactual credit assignment.
- `[[alphacfg-grammar-guided-mcts-tree-lstm-formulaic-alpha-2026-09-05]]` — Grammar-guided Monte Carlo Tree Search with dual-head Tree-LSTM for formulaic alpha discovery.
- `[[prism-vq-vector-quantized-discrete-latent-factor-stock-ranking-2026-09-04]]` — Discrete latent factor generation and cross-sectional stock ranking.

## Sources

1. Sayan Dhan and Selvaraju Natarajan. "AlphaRJM: Reward-Jump Memory for Stochastic Return-Guided Alpha Discovery." *arXiv preprint* `arXiv:2609.08581v1 [cs.LG]`, submitted September 8, 2026. DOI: [10.48550/arXiv.2609.08581](https://doi.org/10.48550/arXiv.2609.08581). Full text: [https://arxiv.org/abs/2609.08581](https://arxiv.org/abs/2609.08581).
2. Shuo Yu, Hongyan Xue, Xingweng Ao, Feiran Pan, Jia He, Dongxiao Tu, and Qing He. "Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning (AlphaGen)." *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, pp. 5476–5486, 2023. DOI: [10.1145/3580305.3599831](https://doi.org/10.1145/3580305.3599831).
3. Zhoufan Zhu and Kexin Zhu. "AlphaQCM: Alpha Discovery in Finance with Distributional Reinforcement Learning." *Proceedings of the 42nd International Conference on Machine Learning (ICML)*, 2025. [https://github.com/ZhuZhouFan/AlphaQCM](https://github.com/ZhuZhouFan/AlphaQCM).
4. Berkin Chen, Han Ding, Ning Shen, Ting Guo, Jiawei Huang, Lu Liu, and Meng Zhang. "AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration." *International Conference on Learning Representations (ICLR)*, 2026. [https://github.com/BerkinChen/AlphaSAGE](https://github.com/BerkinChen/AlphaSAGE).
