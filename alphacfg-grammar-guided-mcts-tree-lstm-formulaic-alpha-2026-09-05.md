---
schema: strategy-research-record-v1
title: "AlphaCFG: Grammar-Guided Learning and Tree-Structured Search for Formulaic Alpha Discovery"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - formulaic-alpha
  - context-free-grammar
  - mcts
  - tree-lstm
  - cross-sectional-equity
  - symbolic-regression
status: research-only
confidence: medium
source_as_of: 2026-01-29
sources:
  - "Han Yang, Dong Hao, Zhuohan Wang, Qi Shi, Xingtong Li, 'Alpha Discovery via Grammar-Guided Learning and Search', arXiv:2601.22119v1 [q-fin.CP, cs.AI, cs.LG], January 2026. DOI: 10.48550/arXiv.2601.22119. https://arxiv.org/abs/2601.22119"
  - "HanYang544/AlphaCFG GitHub repository (commit f6be57914d54d10e0ccabd5d14e147f756b36fa8), https://github.com/HanYang544/AlphaCFG"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaCFG: Grammar-Guided Learning and Tree-Structured Search for Formulaic Alpha Discovery

## Provenance

- **Primary Academic Paper:** Han Yang, Dong Hao, Zhuohan Wang, Qi Shi, and Xingtong Li, *"Alpha Discovery via Grammar-Guided Learning and Search"*, arXiv preprint `arXiv:2601.22119v1 [q-fin.CP, cs.AI, cs.LG]`, submitted 2026-01-29 UTC.
- **Canonical DOI:** [10.48550/arXiv.2601.22119](https://doi.org/10.48550/arXiv.2601.22119).
- **Traceable Paper URLs:**
  - Abstract: [https://arxiv.org/abs/2601.22119](https://arxiv.org/abs/2601.22119)
  - Full Text HTML: [https://arxiv.org/html/2601.22119v1](https://arxiv.org/html/2601.22119v1)
  - Full Text PDF: [https://arxiv.org/pdf/2601.22119](https://arxiv.org/pdf/2601.22119)
- **Primary Open-Source Implementation:**
  - Repository: [https://github.com/HanYang544/AlphaCFG](https://github.com/HanYang544/AlphaCFG)
  - Immutable Commit SHA: `f6be57914d54d10e0ccabd5d14e147f756b36fa8`
  - Key Modules: `alphacfg/grammar/specs.py`, `alphacfg/mcts_core.py`, `alphacfg/network_backends/tree_lstm.py`, `alphacfg/grammar/tree_similarity.py`, `alphacfg/strategy_/strategy.py`.
- **Authors & Affiliations:**
  - Han Yang, Dong Hao, Xingtong Li: School of Computer Science and Engineering, University of Electronic Science and Technology of China (UESTC), Chengdu, China.
  - Zhuohan Wang: Department of Informatics, King's College London, London, United Kingdom.
  - Qi Shi: School of Electronics and Computer Science, University of Southampton, Southampton, United Kingdom.
- **Pre-Write Deduplication Audit:**
  - A comprehensive repository-wide search on 2026-09-05 confirmed zero prior records referencing `2601.22119`, `AlphaCFG`, `Han Yang`, `Dong Hao`, `Zhuohan Wang`, or `Qi Shi`.
  - Adjacent factor discovery records in the repository (`alphalogics-market-logic-multi-agent-factor-generation-2026-09-05.md`, `agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04.md`, `alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03.md`, `alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03.md`, `quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05.md`) evaluate multi-agent prompt negotiation, test-harness sandboxing, LLM reasoning with GRPO, or genetic institutional price-volume correlation.
  - AlphaCFG is structurally and mathematically distinct: it formulates formulaic alpha mining as a formal **Tree-Structured Linguistic Markov Decision Process (TSL-MDP)** governed by a length-bounded context-free grammar ($\alpha$-Sem-$k$), solved via neural Monte Carlo Tree Search (MCTS) with an adaptive branching PUCT rule and a dual-head Tree-LSTM that directly eliminates operator-commutative isomorphic expression redundancy.

## Economic mechanism

### Source-reported

The authors argue that quantitative trading alpha discovery faces a trilemma among heuristic intuition, black-box machine learning, and formulaic symbolic search:
1. **Heuristic/Expert Factors:** Financial ratios (e.g., Fama-French book-to-market, Carhart 12-month momentum) provide clear behavioral intuition but scale poorly and decay rapidly once crowded and arbitraged by market participants.
2. **Black-Box Machine Learning:** Deep recurrent nets, gradient boosted trees, and temporal transformers capture non-linear market interactions but suffer from severe overfitting to financial noise, opaque attribution, and unpredictable regime shifts.
3. **Formulaic Alpha Discovery:** Symbolic expressions (e.g., WorldQuant Alpha101, GTJA 191) provide transparent, human-readable trading rules. However, existing automated symbolic mining frameworks (genetic programming such as `gplearn`, or reinforcement learning such as AlphaGen and AlphaQCM) suffer from two core systemic flaws:
   - *Lack of Linguistic Characterization:* Prior methods treat formula search as an unconstrained traversal over an infinite, unstructured symbol space $\Sigma^*$. In the absence of formal grammar, exploration generates vast numbers of syntactically invalid expressions, ill-formed operator arities, and economically nonsensical combinations (e.g., computing moving averages of constants or correlating non-time-varying parameters).
   - *Semantic & Isomorphic Redundancy:* Linear sequence representations (such as Reverse Polish Notation, RPN) treat syntactically distinct token sequences that encode identical mathematical semantics as independent states (e.g., $x + y \equiv y + x$, or $\text{Cov}(x, y, t) \equiv \text{Cov}(y, x, t)$). This causes search algorithms to repeatedly evaluate isomorphic factors, wasting exploration budget.

To solve this, AlphaCFG formalizes alpha discovery as a language generation problem over nested context-free grammars:
$$\mathcal{L}_{\text{sem}}^{\le K} \subset \mathcal{L}_{\text{sem}} \subset \mathcal{L}_{\text{syn}} \subset \Sigma^*$$

1. **Syntactically Valid Grammar ($\alpha$-Syn):** Enforces prefix notation and strict operator-arity constraints over nonterminal $\mathsf{Expr}$, generating only parseable, well-formed Abstract Syntax Representations (ASR).
2. **Semantically Interpretable Grammar ($\alpha$-Sem):** Integrates financial domain constraints directly into the production rules:
   - Rolling and paired-rolling operators require positive integer constants as window operands ($\mathsf{Num} \in \{20, 30, 40\}$).
   - Expressions cannot consist purely of constants and arithmetic operators (non-triviality).
   - Paired-rolling operators ($\text{Cov}, \text{Corr}$) must operate on two distinct time-varying market features.
3. **Length-Bounded Grammar ($\alpha$-Sem-$k$):** Enforces an additive length counter $k \le K$ with rule-specific length increments $\Delta k \in \{0, 1, 2, 3\}$, reducing the search space from an infinite exponential language to a bounded, tractable combinatorial tree.
4. **Tree-Structured Linguistic MDP (TSL-MDP):** Casts factor derivation as sequential expansion of the leftmost nonterminal symbol in an ASR.
5. **Syntax-Aware Neural MCTS:**
   - Guided by a dual-head **Tree-LSTM encoder** that aggregates child node hidden states: standard $N$-ary Tree-LSTM for asymmetric/ordered operations (e.g., division, subtraction, time shifts) and Child-Sum Tree-LSTM for symmetric/commutative operations (e.g., addition, multiplication, covariance, correlation). This guarantees identical latent embeddings for isomorphic factor trees.
   - An adaptive PUCT selection rule modulates exploration via $\sqrt{b / b_{\text{ref}}}$, compensating for irregular branching across tree depths.
   - A diversity-aware value target penalizes structural similarity against existing factors in the alpha pool using maximum common subtree matching ($\text{sim}(f_j, \mathcal{F})$).

### Research interpretation

AlphaCFG functions as an explicit **inductive bias and structural regularizer** for symbolic alpha mining:
- In financial machine learning, unconstrained symbolic search spaces suffer from the curse of dimensionality, where the number of noise-fitting formulas dwarfs genuine economic anomalies. By encoding syntactic arity, dimensional consistency, and time-series validity into the CFG production rules, AlphaCFG eliminates vast swaths of financially illiterate formulas before evaluation.
- The dual-head Tree-LSTM architecture establishes **topological equivariance** over abstract syntax trees. Traditional sequential RL models (e.g., AlphaGen using LSTM over RPN tokens) treat $\text{Add}(\text{close}, \text{open})$ and $\text{Add}(\text{open}, \text{close})$ as distinct trajectories requiring independent exploratory samples. AlphaCFG collapses these isomorphic paths onto a single representation, dramatically improving sample efficiency.
- The diversity penalty in the MCTS reward target ($z_t = (1 - \text{sim}(f_j, \mathcal{F})) \cdot \max(\text{IC}_{\mathcal{F}}, 0)$) prevents factor crowding within the linear combination pool. Rather than discovering multiple superficial variations of the same short-term price momentum factor, the framework is compelled to search for orthogonal mechanisms—such as volume-price covariance, normalized volatility of illiquidity, and cross-sectional price-range rank interactions.

## Signal

### Grammar Formalism & Production Rules

The core bounded semantic grammar $\alpha$-Sem-$k$ is defined by the quadruple $G = (\mathcal{N}', \mathcal{T}', \mathcal{P}', \mathcal{S})$ [source-reported]:
- **Start Symbol:** $\mathcal{S} = \mathsf{Expr}$ (encoded as root nonterminal `Q` in code).
- **Nonterminals:** $\mathcal{N}' = \{\mathsf{Expr}, \mathsf{Num}, \mathsf{Constant}\}$ [source-reported].
- **Terminals ($\mathcal{T}'$):**
  - **Raw Features ($|\mathcal{F}| = 6$):** $\{\text{open}, \text{high}, \text{low}, \text{close}, \text{volume}, \text{vwap}\}$ [source-reported, Table 4].
  - **Constants ($|\mathcal{C}| = 6$):** $\{-0.1, -0.05, -0.01, 0.01, 0.05, 0.1\}$ [source-reported, Table 5].
  - **Rolling Windows ($|\mathcal{N}| = 3$):** $\{20, 30, 40\}$ [source-reported, Table 5].
  - **Unary Operators ($|U| = 4$):** $\{\text{Abs}(x), \text{Sign}(x), \text{Log}(x), \text{CSRank}(x)\}$ [source-reported, Table 6].
  - **Symmetric Binary Operators ($|B| = 4$):** $\{\text{Add}(x,y), \text{Mul}(x,y), \text{Greater}(x,y), \text{Less}(x,y)\}$ [source-reported, Table 6].
  - **Asymmetric Binary Operators ($|B_{\text{asym}}| = 3$):** $\{\text{Div}(x,y), \text{Pow}(x,y), \text{Sub}(x,y)\}$ [source-reported, Table 6].
  - **Rolling Operators ($|R| = 15$):** $\{\text{Ref}, \text{Skew}, \text{Kurt}, \text{Mean}, \text{Sum}, \text{Std}, \text{Var}, \text{Max}, \text{Min}, \text{Med}, \text{Mad}, \text{Delta}, \text{WMA}, \text{EMA}, \text{Rank}\}$ [source-reported, Table 6].
  - **Paired-Rolling Operators ($|R_{\text{pair}}| = 2$):** $\{\text{Cov}(x,y,t), \text{Corr}(x,y,t)\}$ [source-reported, Table 6].

- **Length Increments $\Delta k$ per Production Rule [source-reported, Table 7]:**
  - $\mathsf{Expr} \to \mathsf{Feature}$: $\Delta k = 0$
  - $\mathsf{Num} \to 20 \mid 30 \mid 40$: $\Delta k = 0$
  - $\mathsf{Constant} \to -0.01 \mid \dots$: $\Delta k = 0$
  - $\mathsf{Expr} \to \mathsf{UnaryOp}(\mathsf{Expr})$: $\Delta k = 1$
  - $\mathsf{Expr} \to \mathsf{BinaryOp}(\mathsf{Expr}, \mathsf{Expr})$: $\Delta k = 2$
  - $\mathsf{Expr} \to \mathsf{BinaryOp}(\mathsf{Expr}, \mathsf{Constant})$: $\Delta k = 2$
  - $\mathsf{Expr} \to \mathsf{BinaryOp\_Asym}(\mathsf{Constant}, \mathsf{Expr})$: $\Delta k = 2$
  - $\mathsf{Expr} \to \mathsf{RollingOp}(\mathsf{Expr}, \mathsf{Num})$: $\Delta k = 2$
  - $\mathsf{Expr} \to \mathsf{PairedRollingOp}(\mathsf{Expr}, \mathsf{Expr}, \mathsf{Num})$: $\Delta k = 3$

### Neural MCTS & Value Optimization

- **PUCT Action Selection Rule:**
  $$a^* = \arg\max_{a} \left( Q(s, a) + c_{\text{puct}} \sqrt{\frac{b}{b_{\text{ref}}}} P(s, a) \frac{\sqrt{\sum_b N(s, b)}}{1 + N(s, a)} \right)$$
  where $c_{\text{puct}} = 1.0$, $b_{\text{ref}} = 40$ (maximum branching constant), $b$ is the number of valid production rules at current node $s$, and $P(s,a)$ is predicted by the policy head [source-reported, Section 4.2 & Appendix H.1].
- **MCTS Simulation Hyperparameters:** 64 simulations per state, 8 parallel workers, evaluation batch size = 2 [source-reported, Appendix H.1].
- **Tree-LSTM Architecture:** Embedding dimension = 128, hidden size = 128, dropout = 0.1. Policy head: 2-layer MLP ($128 \to 64 \to 128$) with Softmax. Value head: 2-layer MLP ($128 \to 64 \to 64 \to 1$) with ReLU [source-reported, Appendix H.2].
- **Training Hyperparameters:** Adam optimizer, learning rate $= 10^{-4}$, batch size $= 64$, replay buffer $= 20,000$, 100 factor trajectories per iteration, 100 training iterations, early stopping after 20% iterations without validation IC improvement [source-reported, Appendix H.3].
- **Linear Combination Model:**
  $$y_t = \sum_{i=1}^{n} w_i f_i(X), \quad \min_{w} \frac{1}{T} \sum_{t=1}^{T} \left( r_t^{(20)} - y_t \right)^2$$
  where $r_t^{(20)} = \frac{\text{Ref}(\text{close}, -20)}{\text{close}} - 1$ is the forward 20-trading-day return [source-reported, Section 2 & Appendix B.1].
- **Diversity Penalty Formulation:**
  $$z_t = (1 - \text{sim}(f_j, \mathcal{F})) \cdot \max(\text{IC}_{\mathcal{F}}, 0), \quad \text{sim}(T_1, T_2) = \frac{|\text{MaxCommonSubtree}(T_1, T_2)|}{\max(N(T_1), N(T_2))}$$
  [source-reported, Section 4.3 & Appendix G].

### Top Discovered Alphas (Empirical Examples)

Table 9 in the primary source details the top 10 discovered alpha expressions and their linear combination weights on CSI 300 constituents:

| Rank | Alpha Factor Expression | Weight ($w_i$) | Economic / Microstructure Interpretation |
| :--- | :--- | :--- | :--- |
| 1 | $\text{Mean}(\text{Corr}(\text{Sum}(\text{open}, 40), (\text{high} - \text{volume}), 20), 20)$ | -0.00889 | Multi-window correlation between cumulative price level and high-volume price spread [source-reported]. |
| 2 | $\text{volume}$ | -0.01278 | Negative volume factor: high turnover predicts lower subsequent returns (liquidity premium / retail overtrading) [source-reported]. |
| 3 | $\text{Std}(\text{close}, 40)$ | +0.01778 | Long-term price volatility expansion factor [source-reported]. |
| 4 | $\text{Pow}(\text{Med}(\text{Cov}(\text{high}, \text{low}, 30), 30), 0.1)$ | +0.01411 | Compressed non-linear median high-low co-movement (intraday range dispersion) [source-reported]. |
| 5 | $\text{Delta}(\text{Log}(|\text{Min}(\text{high}, 30) / 0.01|), 30)$ | -0.01649 | 30-day rate of change in log minimum resistance level [source-reported]. |
| 6 | $\text{Cov}((-0.1 - \text{Sum}(\text{close}, 40)), \text{volume}, 20) + \text{low}$ | -0.01649 | Asymmetric volume-price cumulative flow divergence combined with trailing support [source-reported]. |
| 7 | $0.01 \cdot \text{Greater}(-0.1 / \text{Corr}(\text{high}, \text{close}, 30), \text{volume})$ | -0.00823 | High-close correlation thresholding against volume spikes [source-reported]. |
| 8 | $\text{Log}(|\text{Std}((0.05 - \text{volume}), 40)|)$ | +0.01224 | Temporal variability of inverse trading volume; measures variability of illiquidity under stress [source-reported]. |
| 9 | $\text{Greater}(-0.01, \text{Log}(|\text{Log}(|\text{low}|)|))$ | -0.04616 | Extreme low-price boundary gating filter [source-reported]. |
| 10 | $\text{Cov}(\text{volume}, \text{vwap}, 40)$ | -0.01412 | 40-day co-movement of trading volume and VWAP; negative weight captures institutional distribution exhaustion and price reversal [source-reported]. |

### Operational Trading Rules (Top-K / Drop-N Execution)

- **Signal Formation Timestamp:** Formed daily at market close using daily OHLCV bars [source-reported].
- **Prediction Target Horizon:** 20-trading-day forward return ($h = 20$) [source-reported, Appendix I.1].
- **Universe Cross-Sectional Ranking:** Constituents are ranked in descending order by the linear combination score $y_t = \sum w_i f_i(X_t)$ [source-reported].
- **Portfolio Construction (Top-K / Drop-N Strategy):**
  - Target portfolio size: $K = 60$ stocks [source-reported, Appendix I.3].
  - Daily turnover constraint: Maximum of $n = 5$ stocks swapped per day ($n_{\text{swap}} = 5$) [source-reported, Appendix I.3].
  - Long Entry Rule: Select the highest-ranked stocks not currently held to fill empty slots up to $K = 60$. If the portfolio is full, candidate stocks are eligible to swap into the portfolio only if their score exceeds the score of the lowest-ranked sellable holding [source-reported, `TopKSwapNStrategy` in `alphacfg/strategy_/strategy.py`].
  - Sell / Drop Rule: Rank held stocks by score. Eligible sellable stocks (held $\ge 1$ day) with the lowest scores are sold to accommodate newly qualified top candidates, capped at $n = 5$ swaps per day [source-reported].
- **Position Sizing:** Equal-weighting across all held stocks ($1/60 \approx 1.67\%$ per position) [source-reported].
- **Holding Period:** Minimum holding period of 1 trading day (`min_hold_days = 1`); effective average holding period is governed by the 20-day return horizon and the 5-stock daily turnover ceiling [source-reported].
- **Execution Fill Model:** Next-day market-on-open or market-on-close execution simulated via Qlib `trade_exchange` [`research-proposed` standard fill model].

## Required data

- **Instruments:** Equities; CSI 300 index constituents (China A-share) and S&P 500 index constituents (U.S.) [source-reported].
- **Data Providers:**
  - China A-shares: Qlib binary format (`cn_data_rolling`) updated via AKShare `stock_zh_a_daily` (originating from Sina Finance daily market feeds) [source-reported, repository `README.md`].
  - U.S. equities: Qlib binary format (`us_data`) via Qlib official US daily sample download pipeline [source-reported, repository `README.md`].
- **Timeframe:** Daily OHLCV bars [source-reported].
- **Input Fields:** 6 raw daily fields: `open`, `high`, `low`, `close`, `volume`, `vwap` (where `vwap = amount / volume`) [source-reported, Table 4].
- **Temporal Partitions [source-reported, Appendix I.1]:**
  - **In-Sample Training Period:** 2010-01-01 to 2017-12-31 (8 years).
  - **Validation Period:** 2018-01-01 to 2019-12-31 (2 years, strictly reserved for hyperparameter tuning, pool sizing, and early stopping).
  - **Excluded Period (COVID-19 Gap):** Calendar year 2020 (2020-01-01 to 2020-12-31) was deliberately excluded by design to prevent distortions caused by abnormal structural pandemic volatility [source-reported, Appendix I.1].
  - **Out-of-Sample Test Period:** 2021-01-01 to 2024-12-31 (4 years held-out evaluation).
- **Point-in-Time & Leakage Protection:**
  - Strict temporal boundaries between train, validation, and test splits.
  - Forward 20-day returns $R_t^{(20)}$ are used strictly as target variables during training/reward calculation and never as feature inputs.
  - Operators use strictly backward-looking trailing windows ($\tau \le 40$ trading days) [source-reported].

## Execution assumptions

- **Transaction Costs & Fees:**
  - Simulated via Qlib backtest engine using standard institutional rate schedules:
    - China A-share: Buy commission 0.03% (3 bps); Sell commission + Chinese stamp duty 0.13% (13 bps) [`research-proposed` standard Qlib setup].
    - U.S. equities: Buy commission 0.00% (0 bps); Sell commission 0.05% (5 bps) [`research-proposed` standard Qlib setup].
- **Execution Fill Model:** Qlib standard daily bar execution; orders matched at next-bar Open or Close price assuming full fill without partial cancellation [source-reported / `research-proposed`].
- **Slippage Model:** 0 bps explicitly modeled in baseline paper backtest; slippage stress testing is [`research-proposed`].
- **Turnover Control:** Explicitly constrained by the `TopKSwapNStrategy` parameter $n = 5$ swaps per day out of 60 positions, enforcing a maximum daily portfolio turnover of $2 \times (5 / 60) \approx 16.67\%$ [source-reported].
- **Shorting / Borrowing:** Long-only portfolio consisting of equal-weighted top 60 ranked constituents; no short borrowing required [source-reported].
- **Capacity / ADV Cap:** Not explicitly stated in primary paper; 1.0% of constituent 20-day average daily volume (ADV) [`research-proposed`].

## Evidence

### Source-reported

All quantitative figures below are transcribed directly from Table 2 and Table 3 of Yang et al. (arXiv:2601.22119v1), evaluated across 5 random seeds (reported as mean and standard deviation in parentheses) on the held-out out-of-sample test period (2021-01-01 to 2024-12-31):

#### 1. Out-of-Sample Performance Comparison (2021.01–2024.12, Table 2)

**CSI 300 Constituents (China A-Shares):**

| Method Family | Method | Rank IC | IC | Rank ICIR | ICIR | Sharpe Ratio | Max Drawdown |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ML-Based** | XGBoost | 0.0288 (0.0000) | 0.0326 (0.0000) | 0.2895 (0.0000) | 0.2818 (0.0000) | 0.2853 (0.0000) | -0.2777 (0.0000) |
| | LightGBM | 0.0539 (0.0029) | 0.0296 (0.0014) | 0.3963 (0.0247) | 0.2649 (0.0395) | 0.2680 (0.0666) | -0.3271 (0.0177) |
| | LSTM | 0.0128 (0.0260) | 0.0127 (0.0136) | 0.0896 (0.2064) | 0.1041 (0.1060) | 0.1268 (0.0425) | -0.3542 (0.0240) |
| | TCN | 0.0303 (0.0236) | 0.0085 (0.0133) | 0.2726 (0.1855) | 0.0871 (0.1557) | 0.0908 (0.0754) | -0.2988 (0.0191) |
| | ALSTM | 0.0138 (0.0076) | 0.0105 (0.0067) | 0.1194 (0.0540) | 0.0950 (0.0550) | 0.1372 (0.1113) | -0.3475 (0.0501) |
| | Transformer | 0.0423 (0.0133) | 0.0248 (0.0132) | 0.3759 (0.0697) | 0.2457 (0.0971) | 0.1699 (0.1105) | -0.3365 (0.0377) |
| **Symbolic/RL** | gplearn | 0.0706 (0.0119) | 0.0440 (0.0139) | 0.4695 (0.1164) | 0.3478 (0.1397) | 0.2062 (0.2346) | -0.3854 (0.0324) |
| | AlphaQCM | 0.0811 (0.0046) | 0.0525 (0.0048) | 0.5334 (0.0296) | 0.3874 (0.0121) | 0.4363 (0.0610) | -0.3605 (0.0339) |
| | RPN+PPO (AlphaGen) | 0.0837 (0.0070) | 0.0477 (0.0086) | 0.5724 (0.0343) | 0.3531 (0.0574) | 0.4978 (0.1478) | -0.3497 (0.0423) |
| **Ablation** | RPN+MCTS | 0.0710 (0.0031) | 0.0500 (0.0026) | 0.5577 (0.0292) | 0.4285 (0.0293) | 0.5639 (0.1050) | -0.3201 (0.0613) |
| | $\alpha$-Syn+MCTS | 0.0745 (0.0052) | 0.0487 (0.0036) | 0.5125 (0.0467) | 0.3974 (0.0367) | 0.4852 (0.1320) | -0.3475 (0.0414) |
| | $\alpha$-Sem+MCTS | 0.0770 (0.0044) | 0.0512 (0.0015) | 0.5593 (0.0340) | 0.4369 (0.0301) | 0.5801 (0.1169) | -0.3039 (0.0206) |
| **Proposed** | **$\alpha$-Sem-$k$+MCTS (AlphaCFG)** | **0.0865 (0.0060)** | **0.0577 (0.0029)** | **0.6036 (0.0537)** | **0.4505 (0.0249)** | **0.6459 (0.0612)** | **-0.2963 (0.0289)** |

**S&P 500 Constituents (U.S. Equities):**

| Method Family | Method | Rank IC | IC | Rank ICIR | ICIR | Sharpe Ratio | Max Drawdown |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ML-Based** | XGBoost | 0.0140 (0.0000) | 0.0104 (0.0000) | 0.1535 (0.0000) | 0.1456 (0.0000) | 0.5883 (0.0000) | -0.2543 (0.0000) |
| | LightGBM | 0.0078 (0.0021) | 0.0220 (0.0032) | 0.0860 (0.0269) | 0.2072 (0.0229) | 0.5852 (0.0547) | -0.2047 (0.0128) |
| | LSTM | 0.0131 (0.0077) | 0.0219 (0.0040) | 0.1157 (0.0786) | 0.1847 (0.0419) | 0.5601 (0.0546) | -0.2345 (0.0142) |
| | TCN | 0.0198 (0.0040) | 0.0166 (0.0020) | 0.1358 (0.0190) | 0.1340 (0.0133) | 0.4973 (0.0271) | -0.2396 (0.0175) |
| | ALSTM | 0.0202 (0.0028) | 0.0268 (0.0039) | 0.1569 (0.0344) | 0.1993 (0.0391) | 0.4441 (0.0397) | -0.2418 (0.0109) |
| | Transformer | 0.0106 (0.0049) | 0.0185 (0.0036) | 0.0828 (0.0433) | 0.1806 (0.0361) | 0.5979 (0.1163) | -0.2512 (0.0070) |
| **Symbolic/RL** | gplearn | 0.0130 (0.0122) | 0.0322 (0.0110) | 0.0812 (0.0643) | 0.1877 (0.0437) | 0.8241 (0.1814) | -0.2456 (0.0434) |
| | AlphaQCM | 0.0178 (0.0055) | 0.0384 (0.0056) | 0.1149 (0.0381) | 0.2527 (0.0336) | **1.0566 (0.0756)** | -0.2105 (0.0273) |
| | RPN+PPO (AlphaGen) | 0.0149 (0.0055) | 0.0342 (0.0050) | 0.1045 (0.0364) | 0.2420 (0.0296) | 0.8271 (0.1421) | -0.2559 (0.0242) |
| **Ablation** | RPN+MCTS | 0.0309 (0.0054) | 0.0385 (0.0031) | 0.2447 (0.0234) | 0.3308 (0.0344) | 0.7992 (0.0854) | -0.1957 (0.0140) |
| | $\alpha$-Syn+MCTS | 0.0111 (0.0017) | 0.0272 (0.0047) | 0.0913 (0.0087) | 0.2335 (0.0356) | 0.8046 (0.0322) | -0.2286 (0.0186) |
| | $\alpha$-Sem+MCTS | 0.0265 (0.0011) | 0.0413 (0.0030) | 0.2075 (0.0108) | 0.3360 (0.0162) | 0.8315 (0.0855) | -0.2243 (0.0225) |
| **Proposed** | **$\alpha$-Sem-$k$+MCTS (AlphaCFG)** | **0.0354 (0.0026)** | **0.0457 (0.0034)** | **0.2958 (0.0154)** | **0.4099 (0.0230)** | 0.8473 (0.0483) | **-0.1942 (0.0126)** |

#### 2. Classical Alpha Factor Refinement Results (Table 3)

The authors evaluate the mask-completion capability of the $\alpha$-Sem-$k$+MCTS framework by taking classic factors whose out-of-sample IC had decayed near zero, masking trailing operators, and optimizing single-factor IC:

- **GTJA 191 Factor Refinements (Evaluated on CSI 300 Test Set):**
  - Factor 1: `open / Ref(close, 1) - 1` (Original IC = 0.00185) $\to$ Improved: `open / 0.1 - Cov(volume, high, 20)` (**IC = 0.04279**, $+2,213\%$ improvement).
  - Factor 2: `Mean(close, 6) - close` (Original IC = 0.00482) $\to$ Improved: `Mean(Cov(vwap, volume, 20) / (-0.01), 20) / 0.05` (**IC = 0.04262**, $+784\%$ improvement).
  - Factor 3: `close - Ref(close, 5)` (Original IC = 0.00495) $\to$ Improved: `close - Greater(-0.1, Cov(volume, |vwap|, 30))` (**IC = 0.03872**, $+682\%$ improvement).
- **Alpha101 Factor Refinements (Evaluated on S&P 500 Test Set):**
  - Alpha #1: `-Corr(open, volume, 10)` (Original IC = 0.00271) $\to$ Improved: `Corr(open, Log(|open|), 40) * CSRank(high)` (**IC = 0.02934**, $+983\%$ improvement).
  - Alpha #2: `-Rank(CSRank(low), 9)` (Original IC = 0.01031) $\to$ Improved: `Rank(CSRank(CSRank(Sign(vwap))), 30) * CSRank(high)` (**IC = 0.02944**, $+186\%$ improvement).
  - Alpha #3: `Pow(high * low, 0.5) - vwap` (Original IC = 0.00112) $\to$ Improved: `Pow(CSRank(|open|) * open, CSRank(close)) - vwap` (**IC = 0.03126**, $+2,691\%$ improvement).

### Independently reproduced

`Not independently reproduced.` All quantitative tables and metrics above are source-reported extractions directly transcribed and verified from Yang et al. (arXiv:2601.22119v1) and its open-source repository `HanYang544/AlphaCFG` at commit `f6be57914d54d10e0ccabd5d14e147f756b36fa8`.

### Negative evidence

- **Structural Failure of Unbounded Grammar Search:** In the ablation study (Table 2), removing the length-bounding constraint ($\alpha$-Sem+MCTS vs. $\alpha$-Sem-$k$+MCTS) causes Rank IC to drop from 0.0865 to 0.0770 on CSI 300, and from 0.0354 to 0.0265 on S&P 500. Without strict depth/length bounds, MCTS generates overly deep, complex formulas that overfit training noise and suffer from out-of-sample performance degradation.
- **RPN Sequence Representation Degradation:** Comparing RPN+MCTS against $\alpha$-Sem-$k$+MCTS demonstrates that linear sequence representations underperform tree grammar representations across both markets (Rank IC: 0.0710 vs 0.0865 on CSI 300; 0.0309 vs 0.0354 on S&P 500), confirming that linear token encoding wastes exploration budget on isomorphic formulas.
- **Extreme Cross-Market Informational Attenuation:** Rank IC drops from 0.0865 on CSI 300 to 0.0354 on S&P 500 (a $59.1\%$ decay). This reflects the high informational efficiency and institutional crowding in U.S. large-cap equities, indicating that formulaic alpha signals discovered on price-volume data alone face strong margin compression in mature liquid markets.
- **Intentional Omission of COVID-19 Period (2020):** The authors intentionally omitted the entire calendar year 2020 from train, validation, and test datasets. The strategy's performance during macro crisis regimes, flash crashes, or sudden volatility spikes remains untested and unproven.
- **Absence of Slippage and Execution Latency Modeling:** The reported Sharpe ratios (0.6459 on CSI 300, 0.8473 on S&P 500) assume zero slippage and instantaneous next-bar execution. For daily rebalancing across 60 constituents, real-world execution frictions (e.g., bid-ask spread crossing, market impact on rebalancing days) could substantially diminish net profitability.

## Falsification plan

To falsify the claim that AlphaCFG discovers genuine predictive alpha rather than fitting in-sample data noise:

1. **Permuted Grammar / Inverted Arity Ablation:**
   - *Test:* Replace the $\alpha$-Sem-$k$ grammar with an inverted grammar where operator arities are permuted or financial semantic constraints are inverted (e.g., forcing rolling window parameters to take time-varying prices while features take static integers).
   - *Metric:* Out-of-sample Rank IC and Sharpe ratio on 2021–2024 test data.
   - *Research-defined falsification threshold:* If factors mined under the inverted grammar achieve Rank IC $\ge 80\%$ of the canonical AlphaCFG baseline, the hypothesis that formal financial grammar provides genuine discovery regularisation is falsified.
2. **Stress Test on Excluded 2020 COVID-19 Period:**
   - *Test:* Run the frozen top-10 discovered alpha pool (Table 9) through the omitted 2020 calendar year (2020-01-01 to 2020-12-31) without retraining or parameter modification.
   - *Metric:* Maximum Drawdown and Calmar ratio during 2020.
   - *Research-defined falsification threshold:* A Maximum Drawdown exceeding $-35.0\%$ or a negative annualized Sharpe ratio over 2020 falsifies the strategy's tail-risk robustness across volatile macro regimes.
3. **Execution Slippage & Bid-Ask Spread Degradation Test:**
   - *Test:* Apply incremental round-trip execution slippage penalties: 2 bps, 5 bps, 10 bps, and 15 bps per traded share in the Top-60/Drop-5 backtest.
   - *Metric:* Net Annualized Return and Sharpe Ratio.
   - *Research-defined falsification threshold:* If net Sharpe drops below $0.20$ or net annualized alpha turns negative at 5 bps round-trip slippage, the strategy is deemed unviable for institutional production.
4. **Isomorphic Tree Representation Ablation (Tree-LSTM vs. Token Sequence):**
   - *Test:* Replace the dual-head Tree-LSTM with a standard sequential Transformer or LSTM encoder while holding the MCTS search budget fixed at 64 simulations.
   - *Metric:* Sample efficiency (iterations required to reach validation IC $\ge 0.05$) and unique non-isomorphic factor yield.
   - *Research-defined falsification threshold:* If the sequential encoder discovers equivalent or higher validation IC within the same simulation budget, the claim that Tree-LSTM isomorphic reduction is necessary for efficient factor discovery is falsified.
5. **Action Following Falsification:** Invalidate automated MCTS factor discovery; reject alpha pool for portfolio implementation; isolate individual valid mathematical primitives for classical manual econometric screening.

## Crypto portability

**Portability Status:** `Adapted / Unproven`.

The primary source evaluates AlphaCFG exclusively on equity universes (CSI 300 and S&P 500). Porting AlphaCFG to cryptocurrency markets is a research adaptation and must be considered unproven until empirically validated in crypto environments. Critical structural divergences include:

- **24/7 Continuous Trading & Candle Boundary Ambiguity:** Equities exhibit clear daily opening and closing auctions that define session boundaries. Crypto trades continuously 24/7. Applying daily aggregation (e.g., 00:00 UTC cutoff) creates arbitrary boundaries that can distort rolling operators ($\text{Ref}$, $\text{Delta}$, $\text{WMA}$) and volume-price covariance metrics.
- **Perpetual Futures Funding Rate Drag:** In crypto perpetual futures, the dominant cost-of-carry is the 8-hour funding rate. The primary AlphaCFG model optimizes purely for 20-day price return ($R_t^{(20)}$) without accounting for cumulative funding yield or basis divergence. High-momentum long tokens frequently trade at elevated positive funding rates, eroding net returns.
- **Extreme Cross-Sectional Beta Co-Movement:** Altcoin cross-sections exhibit high correlation with Bitcoin ($\beta_{\text{BTC}} > 0.8$ for most liquid tokens). A Top-60 long-only ranking strategy in crypto would effectively function as an unhedged high-beta market proxy, suffering catastrophic drawdowns during systematic crypto market sell-offs unless explicit cross-sectional market-neutralization (e.g., dollar-neutral long/short or beta-hedging via BTC/ETH perpetuals) is applied.
- **Venue Fragmentation & VWAP Quality:** In equity markets, consolidated tape data provides reliable volume and VWAP. Crypto spot and perpetual liquidity is fragmented across Binance, OKX, Bybit, Coinbase, and decentralized exchanges. Divergent exchange prints introduce artificial noise into rolling covariance ($\text{Cov}(\text{volume}, \text{vwap}, 40)$).
- **Adapted Crypto Universe & Parameterization [`research-proposed`]:**
  - Universe: Top 50 liquid perpetual contracts on Binance/OKX with trailing 30-day ADV $> \$25\text{M}$.
  - Target Horizon: 5-day to 10-day forward returns (adjusted for faster crypto alpha decay).
  - Target Formulation: Dollar-neutral long top quintile / short bottom quintile with 8-hour funding rate deduction.

## Limitations

- **Omission of Crisis Period (2020 Gap):** Complete exclusion of the year 2020 removes the primary modern stress-test regime from the empirical evaluation, creating an untested survivorship window across market dislocations.
- **Zero Slippage Assumption in Published Results:** The reported backtest metrics assume frictionless execution, which overstates profitability for multi-factor daily rebalanced portfolios.
- **High Computational Training Overhead:** Executing 64 MCTS simulations per action step with dual-head Tree-LSTM inference over 20,000 replay states requires significant GPU compute (CUDA 12.8 / PyTorch 2.8 / DGL 1.1.3), limiting real-time retraining frequency.
- **Linear Combination Simplicity:** Alpha factors are combined using a static linear regression model. Non-linear factor interactions or regime-switching dynamics are not captured by the downstream portfolio layer.
- **Underspecified Transaction Cost Breakdown in Paper Body:** While Table 2 reports net performance, the precise commission, stamp duty, and borrow assumptions are not detailed in the paper text, requiring provenance recovery from Qlib codebase conventions.

## Implementation status

`not-implemented`. This record represents an external research capture. No code has been integrated into `nautilus-quant-system`, PyBroker, or NautilusTrader. No trading strategy family has been instantiated, and no paper, testnet, or live trading has been authorized.

## Adoption boundary

- **Status:** `research-only`
- **Implementation Status:** `not-implemented`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This document is a research hypothesis capture and does not constitute approval for live execution, capital allocation, or strategy adoption. Any future adoption must undergo formal isolated validation in PyBroker (Loop B) followed by event-driven historical backtesting in NautilusTrader.

## Related Wiki records

- `[[quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05]]` — Market logic-driven multi-agent system compiling intermediate financial hypotheses into DSL factor constraints.
- `[[quant/alphacrafter-harness-multi-agent-cross-sectional-equity-alpha-2026-09-03]]` — Multi-agent cross-sectional equity alpha generation with test harness validation.
- `[[quant/agonalpha-prompt-economy-adversarial-review-agentic-alpha-discovery-2026-09-04]]` — Adversarial multi-agent prompt economy for alpha factor search.
- `[[quant/alphar1-context-aware-alpha-screening-llm-reasoning-grpo-2026-09-03]]` — LLM reasoning with GRPO reinforcement learning for alpha factor screening.
- `[[quant/quantaalpha-institutional-price-volume-correlation-intraday-momentum-2026-09-05]]` — Evolutionary factor mining with institutional price-volume correlation.
- `[[quant/cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03]]` — Econometric selection of Alpha191 factors using double-selection LASSO.
- `[[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]]` — Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery.

## Sources

1. Han Yang, Dong Hao, Zhuohan Wang, Qi Shi, and Xingtong Li, *"Alpha Discovery via Grammar-Guided Learning and Search"*, arXiv preprint `arXiv:2601.22119v1 [q-fin.CP, cs.AI, cs.LG]`, submitted January 29, 2026.
   - Abstract: [https://arxiv.org/abs/2601.22119](https://arxiv.org/abs/2601.22119)
   - Full Text HTML: [https://arxiv.org/html/2601.22119v1](https://arxiv.org/html/2601.22119v1)
   - Full Text PDF: [https://arxiv.org/pdf/2601.22119](https://arxiv.org/pdf/2601.22119)
   - Canonical DOI: [10.48550/arXiv.2601.22119](https://doi.org/10.48550/arXiv.2601.22119)
2. Han Yang et al., *AlphaCFG: Unified Framework for Grammar-Guided Alpha-Factor Discovery*, GitHub repository: [https://github.com/HanYang544/AlphaCFG](https://github.com/HanYang544/AlphaCFG).
   - Immutable Commit SHA: `f6be57914d54d10e0ccabd5d14e147f756b36fa8`
   - Key Reference Files: `alphacfg/grammar/specs.py`, `alphacfg/mcts_core.py`, `alphacfg/network_backends/tree_lstm.py`, `alphacfg/strategy_/strategy.py`.
3. S. Yu, H. Xue, X. Ao, F. Pan, J. He, D. Tu, and Q. He, "Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning (AlphaGen)", *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 2023.
4. Z. Zhu and K. Zhu, "AlphaQCM: Alpha Discovery in Finance with Distributional Reinforcement Learning", *Forty-second International Conference on Machine Learning (ICML)*, 2025.
5. Z. Kakushadze, "101 Formulaic Alphas", *Wilmott*, 2016.
6. Guotai Junan Securities, "Alpha 191 Factors", 2025.
7. X. Yang, W. Liu, D. Zhou, J. Bian, and T. Liu, "Qlib: An AI-oriented Quantitative Investment Platform", *arXiv:2009.11189*, 2020.
8. K. S. Tai, R. Socher, and C. D. Manning, "Improved Semantic Representations from Tree-Structured Long Short-Term Memory Networks", *arXiv:1503.00075*, 2015.
9. D. Silver et al., "Mastering the Game of Go without Human Knowledge", *Nature*, 550(7676):354–359, 2017.
