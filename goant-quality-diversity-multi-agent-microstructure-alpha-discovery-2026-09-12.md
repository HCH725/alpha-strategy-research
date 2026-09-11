---
schema: strategy-research-record-v1
title: "GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - quality-diversity
  - map-elites
  - alpha-discovery
  - symbolic-alpha
  - multi-agent
  - market-microstructure
  - order-book
  - price-volume
  - china-a-shares
status: research-only
confidence: high
source_as_of: 2026-09-09
sources:
  - "Stella Zhao and Tommy Sha, 'GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data', arXiv:2609.08719v2 [cs.AI], submitted September 2026. Stable URLs: https://arxiv.org/abs/2609.08719, https://arxiv.org/html/2609.08719v2, https://arxiv.org/pdf/2609.08719, DOI: 10.48550/arXiv.2609.08719"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data

## Provenance

- **Primary Source:** Stella Zhao (University of Minnesota, `zhao2052@umn.edu`) and Tommy Sha (Stony Brook University, `tianming.sha@stonybrook.edu`), *"GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data"*, arXiv preprint `arXiv:2609.08719v2 [cs.AI]`, submitted September 2026.
  - Abstract URL: [https://arxiv.org/abs/2609.08719](https://arxiv.org/abs/2609.08719)
  - Full-Text HTML: [https://arxiv.org/html/2609.08719v2](https://arxiv.org/html/2609.08719v2)
  - Full-Text PDF: [https://arxiv.org/pdf/2609.08719](https://arxiv.org/pdf/2609.08719)
  - Canonical DOI: [10.48550/arXiv.2609.08719](https://doi.org/10.48550/arXiv.2609.08719)
  - License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Verification Integrity:** The complete full-text HTML and mathematical derivations of `arXiv:2609.08719v2` were directly retrieved and inspected. Every reported equation, behavioral descriptor axis, admission threshold, hyperparameter, ablation table, and out-of-sample retention figure traces directly to the text, Tables 1–4, and Supplementary Appendices A–I of `arXiv:2609.08719v2`. No secondary summaries, search snippets, or synthetic aggregations were used to formulate strategy mechanics or empirical findings.
- **Repository Deduplication Audit:** A comprehensive audit of all records in `alpha-strategy-research` confirmed zero existing records matching `arXiv:2609.08719`, the title, Stella Zhao, Tommy Sha, or the GoAnt Quality-Diversity multi-agent factor search framework. Related formulaic alpha discovery records in the repository (such as `alpharjm-reward-jump-memory-sde-critic-symbolic-alpha-2026-09-11.md` based on Dhan & Natarajan 2026, arXiv:2609.08581) evaluate single-agent token construction with event-driven jump memory and continuous-time SDE return critics on daily equity bars without quality-diversity behavioral archives, multi-agent island roles, or order-book microstructure cost walls. GoAnt constitutes a distinct, independent research capture.

## Economic mechanism

### Source-reported

1. **The Execution Trap and the Reasoning Trap in Automated Alpha Mining:**
   - *The Execution Trap:* As quantitative data granularity shifts from daily price–volume panels to intraday order-book (L2) snapshots, traditional predictive proxies (such as raw RankIC) diverge catastrophically from execution-aware net returns $N(f, C)$ under transaction costs $C$ (spread, slippage, market impact). Unconstrained single-agent optimization collapses into localized sub-optima generating high-frequency trading noise whose gross statistical correlation is entirely wiped out by execution frictions.
   - *The Reasoning Trap:* Off-the-shelf communicative multi-agent LLM systems (e.g., chat-based manager-analyst hierarchies) suffer from consensus bias, context window squeezing, and herd behavior when navigating high-dimensional noisy financial search spaces. Such coordinators repeatedly allocate computational budget to redundant, homogenized factor families.

2. **The GoAnt Tripartite Architecture:**
   To overcome both traps, GoAnt decouples the search into three structural components:
   - **The Mental Map (Adaptive-Capacity MAP-Elites Archive):** A Quality-Diversity (QD) archive defined over a 6-dimensional behavioral feature space $\mathcal{Z}$. The embedding operator $\phi: \mathcal{F} \to \mathcal{Z}$ maps each factor to a label-free execution and structural profile computable strictly without future-return information. Cell centers are initialized at birth at the descriptor position of the founding candidate and frozen forever. Capacity is adaptive: when a valid candidate lies farther than a niche radius ($r = 0.65$) from every existing cell, it founds a new niche. Elitist replacement guarantees that within each cell, an elite $e_{k,t}$ is replaced only if a newly proposed candidate achieves a strictly higher signal quality score $S(f)$.
   - **Worker Ants (Decoupled, Non-Communicating Generators):** Three specialized, non-communicating generator islands that exchange no direct messages and coordinate exclusively through the shared Mental Map:
     - *Explorer Ants:* Perform radical, high-temperature structural mutations on program ASTs to cross behavioral barriers and discover unoccupied niches.
     - *Exploiter Ants:* Execute intensive, localized hill-climbing via Learned Repair on existing niche elites to maximize signal quality within established niches.
     - *Connector Ants:* Perform semantic crossover, recombining subtrees from spatially distant niches on the Mental Map via mutual $k$-nearest-neighbor graph edges ($k=4$).
   - **The Queen Ant (Distilled Compact Dispatcher):** Under a fixed evaluation budget $B = 500$, the orchestration policy assigns candidate generation tasks to the three worker islands. Standard multi-armed bandits (e.g., UCB) over-exploit high-reward niches and stall due to candidate duplication. The Queen Ant is a compact language model (Qwen2.5-Instruct 1.5B) LoRA-distilled from 8 frontier teacher LLMs (GPT-5.6, Claude Opus 4.8, Claude Opus 5, DeepSeek-V4-Pro, Qwen3.7-Max, GLM-5.2, Kimi K2.7-Code, MiniMax-M3) on a 35M-token corpus. It optimizes a global multi-objective reward over standardized coverage $\bar{C}$, quality $\bar{Q}$, and redundancy $\bar{D}$:
     $$\max_\pi J(\pi) = \alpha \bar{C}(A_B) + \beta \bar{Q}(A_B) - \gamma \bar{D}(\tau_B), \quad \alpha, \beta, \gamma \ge 0, \quad \alpha + \beta + \gamma = 1$$

3. **Layered Objective with Deflation-Corrected Signal Quality:**
   To prevent optimization against the noisy, non-convex cost wall during search, GoAnt decouples the objective:
   - Search fitness is a deflated signal-quality score $S(f)$ that penalizes sign instability:
     $$S(f) = t_{\text{dsr}}(f) \cdot \max\left(0, 2\left(p_+(f) - \frac{1}{2}\right)\right)$$
     where $t_{\text{dsr}}(f)$ is the deflated $t$-statistic of the factor's RankIC and $p_+(f)$ is the fraction of days with positive daily IC. When daily IC fluctuates symmetrically around zero ($p_+ \approx 0.5$), $S(f) \to 0$.
   - Turnover and transaction costs are offloaded to descriptor coordinates of the Mental Map.
   - Net return $N(f, C)$ is evaluated strictly as an admission gate and post-hoc out-of-sample validation filter, never as an in-the-loop gradient.

### Research interpretation

- **Structural Decoupling as an Antidote to Overfitting:**
  Greedy direct optimization of net return under transaction costs causes symbolic search algorithms to discover over-parameterized filters that artificially suppress trade frequency during backtest drawdown periods. By mapping turnover and spread into behavioral descriptor coordinates, the algorithm preserves low-turnover, medium-turnover, and high-turnover alphas in separate cells, forcing exploration across the entire behavioral spectrum rather than collapsing to a single degenerate low-turnover factor.
- **Why Connectors Matter Most:**
  Empirical role ablation reveals that removing Connector Ants incurs the largest performance drop ($-8.7$ in PV and $-10.9$ in L2 quality-weighted yield). Simple random mutation (Explorers) finds isolated pockets, but bridging distant behavioral clusters (e.g., combining an order-book depth imbalance subtree with a price-volatility normalization operator) generates genuinely non-linear cross-microstructure alpha.
- **Adaptive Capacity vs. Center Mobility:**
  The authors' $2 \times 2$ factorial proves that allowing cells to be created dynamically (+adaptive capacity) yields large performance gains (+27% to +34% quality-weighted yield), whereas allowing cell centers to move (mean-tracking) actively harms performance ($-13\%$ to $-17\%$) by deforming the coordinate space and dragging existing niches toward recent sample density.

## Signal

The signal generation pipeline produces an ensemble cross-sectional ranking across tradeable assets by combining the non-redundant elites discovered in the Mental Map (`source-reported` framework; specific portfolio combination `research-proposed`):

1. **Search Space and Grammar:**
   - Search space $\mathcal{F}$ consists of symbolic alpha programs formed as abstract syntax trees (ASTs).
   - Operators include time-series rolling operators (`ts_mean`, `ts_std`, `ts_corr`, `ts_rank`, `ts_decay_linear`), cross-sectional operators (`cs_rank`, `cs_zscore`), arithmetic operators (`+`, `-`, `*`, `/`), and conditional logic.
   - Maximum operator-chain depth: $\le 5$ (`source-reported` admission gate).

2. **The 6-Dimensional Behavioral Descriptor Space $\mathcal{Z}$ (`source-reported`):**
   The descriptor operator $\phi(f) = [z_1, z_2, z_3, z_4, z_5, z_6]^\top \in \mathbb{R}^6$ embeds factor $f$ using strictly label-free execution and structural features:
   - $z_1$: Turnover (annualized average fraction of portfolio replaced daily).
   - $z_2$: Mean effective spread (bps, volume-weighted).
   - $z_3$: Operator-chain depth (maximum depth of the AST program tree).
   - $z_4$: Signal autocorrelation (lag-1 auto-correlation of the cross-sectional factor values).
   - $z_5$: Cross-sectional skewness (average cross-sectional third standardized moment).
   - $z_6$: Long/short spread tilt (relative variance of the top decile vs. bottom decile factor exposures).
   *Scaling:* Each descriptor axis is robustly standardized (median and interquartile range) and clipped to $[-3.0, +3.0]$ standard units using scalers fitted strictly on the development split (`source-reported`).

3. **Archive Admission Gates (Table S4, `source-reported`):**
   A proposed candidate factor $f$ is admitted to the Mental Map if and only if it clears all 10 frozen admission gates:
   - *Statistical Gates:*
     - $|\text{RankIC}| \ge 0.01$
     - $|t_{\text{dsr}}| \ge 2.0$ (deflated $t$-statistic of RankIC)
   - *Stability Gates:*
     - Positive-IC period ratio $\ge 0.52$
     - Positive daily-IC fraction $p_+(f) \ge 0.60$
     - In-sample vs. late-sample IC gap $\le 0.02$
   - *Execution Gates:*
     - Mean effective spread $\le 25$ bps
     - Net cumulative return $N(f, C) > 0$
     - Gross-to-net return retention ratio $> 0$
     - Maximum drawdown of net return $> -0.50$ (less severe than 50% drawdown)
   - *Structural Gate:*
     - Operator-chain depth $\le 5$

4. **Niche Allocation and Elite Replacement (`source-reported`):**
   - Candidate joins the nearest existing cell if Euclidean distance $d(z, c_k) \le 0.65$.
   - If $d(z, c_k) > 0.65$ for all existing cells $k$, a new cell is founded with center $c_{\text{new}} = z$.
   - Centers closer than $0.325$ ($0.5 \times 0.65$) are merged to prevent cardinality inflation.
   - Elite replacement: candidate replaces existing elite $e_k$ if and only if $S(f) > S(e_k)$.

5. **Downstream Production Portfolio Construction (`research-proposed`):**
   The source evaluates individual factors and the archive population under an effective-yield protocol. For live quantitative strategy deployment, the following portfolio construction rules are `research-proposed`:
   - *Factor Selection:* Select all surviving elites clearing a qualified quality floor $q^*$ with pairwise Spearman correlation $|\rho(f_i, f_j)| < 0.70$ (`research-proposed`).
   - *Weighting:* Cross-sectional z-scores of selected factors are combined via inverse-variance or equal weighting:
     $$F_{i,t} = \frac{1}{M} \sum_{m=1}^M \text{cs\_zscore}(f_m(X_{i,t}))$$
     (`research-proposed`).
   - *Position Sizing:* Dollar-neutral long/short quintile portfolio: Long top 20% of stocks by $F_{i,t}$, short bottom 20%, equal-weighted within quintiles (`research-proposed`).
   - *Rebalance Cadence:* Daily market close rebalancing with 1-day execution lag (`research-proposed`).

## Required data

- **Universe:** China A-share equity universe (all actively traded non-ST, non-suspended common stocks on Shanghai and Shenzhen stock exchanges, 2023–2026) (`source-reported`).
- **Data Categories (`source-reported`):**
  1. *Price–Volume (PV) Panels:* Daily OHLCV bars, aggregate turnover, and volume-weighted average price (VWAP).
  2. *Order-Book (L2) Snapshots:* Level-2 high-frequency limit order book snapshots, containing 10-level bid/ask prices, queue depths, accumulated trade quantities, and order imbalances.
- **Development vs. Out-of-Sample Split (`source-reported`):**
  - Search / Development Split: Disjoint early sample period (2023 to early 2025) used for factor search, descriptor scaler estimation, and cell creation.
  - Locked Out-of-Sample Split: Strictly disjoint late sample period (late 2025 to 2026) used exclusively for evaluation of locked factor populations without re-selection or re-fitting.
- **Point-in-Time Hygiene:** Scaler parameters (medians, IQR) and candidate evaluation grids are fitted strictly on the development split; zero future-return labels or OOS dates are consulted during descriptor embedding or scaling (`source-reported`).

## Execution assumptions

- **Cost Model & Execution Frictions (`source-reported`):**
  - Category-specific cost model incorporates bid-ask spread, slippage, and market impact following Almgren & Chriss (2001).
  - Effective spread gate: Factors must maintain mean effective spread $\le 25$ bps (`source-reported`).
  - Cost wall: Gross-to-net retention must be strictly positive ($N(f, C) > 0$), and net maximum drawdown must be milder than $-50\%$ (`source-reported`).
- **Signal-to-Order Timing (`research-proposed`):**
  - Daily close evaluation; orders executed at next-day open or TWAP/VWAP over the first 30 minutes of regular trading (`research-proposed`).
- **Short Selling Assumptions (`research-proposed`):**
  - China A-share market operates under short-selling constraints (securities lending restrictions, T+1 trading rules). Long-only top quintile benchmark or index-enhancement portfolio overlay must be adopted unless utilizing CSI 300 / CSI 500 index futures as the short leg (`research-proposed`).

## Evidence

### Source-reported

All empirical figures below trace directly to Zhao & Sha (arXiv:2609.08719v2, Tables 1–4, Tables S1–S4):

1. **Exp 1: The Coordination Spectrum (Table 1, matched 500-evaluation budget, 5 seeds mean):**

| # | Method | Topology | PV Distinct | PV Q-Wtd Yield | PV Best $S(f)$ | PV $|\rho| @ q^*$ | PV Cells | L2 Distinct | L2 Q-Wtd Yield | L2 Best $S(f)$ | L2 $|\rho| @ q^*$ | L2 Cells |
|---|--------|----------|-------------|----------------|----------------|--------------------|----------|-------------|----------------|----------------|--------------------|----------|
| 1 | Single-Agent | greedy | 6 | 5.8 | 5.12 | 0.68 | — | 5 | 4.6 | 4.71 | 0.71 | — |
| 2 | Debate/Vote | static | 15 | 16.3 | 5.81 | 0.52 | — | 13 | 13.9 | 5.34 | 0.56 | — |
| 3a | RD-Agent-Quant | static | 21 | 22.4 | 6.24 | 0.35 | — | 19 | 20.1 | 5.88 | 0.38 | — |
| 3b | TradingAgents | static | 19 | 19.6 | 5.93 | 0.37 | — | 17 | 17.4 | 5.52 | 0.40 | — |
| 3c | AlphaAgent (2025) | static | 23 | 25.1 | 6.41 | 0.39 | — | 20 | 21.6 | 6.02 | 0.41 | — |
| 3d | AlphaGen (2023) | n/a | 20 | 20.8 | 6.08 | 0.35 | — | 18 | 18.5 | 5.71 | 0.37 | — |
| 3e | AutoAlpha (GP) (2020) | n/a | 24 | 26.6 | 6.55 | 0.36 | — | 22 | 24.2 | 6.12 | 0.37 | — |
| 3f | CVT-MAP-Elites (2018) | fixed | 18 | 18.4 | 5.94 | 0.41 | 96 | 17 | 17.2 | 5.76 | 0.43 | 96 |
| 3g | CMA-ME (2020) | fixed | 14 | 13.7 | 5.42 | 0.45 | 96 | 12 | 11.6 | 5.08 | 0.47 | 96 |
| 3h | Random Search | none | 7 | 6.5 | 4.63 | 0.44 | — | 6 | 5.5 | 4.35 | 0.46 | — |
| **4** | **GoAnt (ours)** | **adaptive** | **34** | **41.8 (+57%)** | **7.62** | **0.31** | **118** | **37** | **47.6 (+97%)** | **7.84** | **0.28** | **131** |
| 5 | No-Map Ablation | none | 9 | 8.7 | 7.14 | 0.71 | — | 8 | 7.6 | 7.29 | 0.74 | — |
| 6 | Static Map (frozen) | frozen | 27 | 30.5 | 7.21 | 0.38 | 96 | 26 | 31.2 | 7.32 | 0.39 | 96 |
| 6b | Re-fit Atlas (periodic)| periodic | 29 | 33.7 | 7.06 | 0.36 | 104 | 29 | 34.8 | 7.22 | 0.36 | 109 |
| 6c | Moving-Centre (semi) | semi | 31 | 36.2 | 7.34 | 0.34 | 121 | 31 | 39.4 | 7.58 | 0.33 | 134 |
| 7 | Raw-Net Objective | adaptive | 11 | 9.9 | 4.87 | 0.63 | 115 | 8 | 6.8 | 4.12 | 0.69 | 128 |

2. **Exp 2: $2 \times 2$ Factorial Decomposition of Archive Dynamism (Table 2):**
   - *Row A (GoAnt: frozen centers, new cells allowed):* PV: 118 cells, 41.8 q-wtd; L2: 131 cells, 47.6 q-wtd.
   - *Row B (mean-tracking centers, new cells allowed):* PV: 121 cells, 36.2 q-wtd ($-13\%$); L2: 134 cells, 39.4 q-wtd ($-17\%$).
   - *Row C (frozen centers, new cells forbidden [Static Map]):* PV: 96 cells, 30.5 q-wtd ($-27\%$); L2: 96 cells, 31.2 q-wtd ($-34\%$).
   - *Row D (mean-tracking centers, new cells forbidden):* PV: 96 cells, 28.1 q-wtd ($-33\%$); L2: 96 cells, 28.4 q-wtd ($-40\%$).

3. **Exp 4: Out-Of-Sample Quality Retention on Locked Populations (Table 3):**
   - *Single-Agent:* PV retention = 0.38 ($-41\%$ vs. GoAnt); L2 retention = 0.32 ($-52\%$).
   - *Debate/Vote:* PV retention = 0.47 ($-27\%$); L2 retention = 0.44 ($-34\%$).
   - *Alpha158/360 fixed library:* PV retention = 0.59 ($-8\%$); L2 retention = 0.58 ($-13\%$).
   - *AlphaGen (RL):* PV retention = 0.51 ($-20\%$); L2 retention = 0.48 ($-28\%$).
   - *No-Map:* PV retention = 0.29 ($-55\%$); L2 retention = 0.27 ($-60\%$).
   - *Static Map:* PV retention = 0.61 ($-5\%$); L2 retention = 0.63 ($-6\%$).
   - *GoAnt (ours):* In-sample $q = 7.62 \to$ OOS $q = 4.88$ (retention **0.64**) in PV; In-sample $q = 7.84 \to$ OOS $q = 5.25$ (retention **0.67**) in L2.

4. **Exp 5: Orchestrator Routing Ablation under Identical Atlas (Table 4):**
   - *Round-Robin:* PV q-wtd = 34.9 ($-17\%$), L2 q-wtd = 38.1 ($-20\%$).
   - *EMA-guided:* PV q-wtd = 36.2 ($-13\%$), L2 q-wtd = 39.7 ($-17\%$).
   - *UCB bandit:* PV q-wtd = 38.4 ($-8\%$), L2 q-wtd = 42.0 ($-12\%$).
   - *Mock-Queen (uninformed reasoning ablation):* PV q-wtd = 35.6 ($-15\%$), L2 q-wtd = 39.0 ($-18\%$).
   - *Queen Ant 1.5B (ours):* PV q-wtd = **41.8**, L2 q-wtd = **47.6**.

5. **Decision-Level Audit of the Queen Ant (Table 8 / S2):**
   - Decisions audited: 120 (PV) and 120 (L2).
   - Parse failures: 3 (PV) and 4 (L2). Low-confidence abstentions: 7 (PV) and 9 (L2).
   - Fallback rate: 0.058 (PV) and 0.075 (L2) (well below cap).
   - Agreement with UCB argmax: 0.62 (PV) and 0.59 (L2).
   - Deviation from UCB argmax: 0.38 (PV) and 0.41 (L2) (clears deviation floor, confirming Queen is not a bandit impersonator).

### Independently reproduced

Not independently reproduced. All empirical findings reflect direct extraction from Zhao & Sha (`arXiv:2609.08719v2`, 2026).

### Negative evidence

- **Catastrophic Collapse of Raw Net-Return Optimization (Arm 7):**
  When search admission is directed by raw net return $N(f, C)$ rather than deflated signal quality $S(f)$, yield collapses from 41.8 to 9.9 in PV ($-76\%$) and from 47.6 to 6.8 in L2 ($-86\%$), while pairwise correlation among survivors spikes to $0.63$ and $0.69$. The algorithm overfits the discrete transaction-cost boundary by generating sparse, non-generalizable signals.
- **Greedy Collapse without Mental Map (Arm 5):**
  A flat greedy pool without behavioral niche partitioning produces only 9 distinct factors in PV and 8 in L2, with extreme pairwise correlation ($\rho = 0.71$ to $0.74$) and catastrophic OOS decay (retention drops to $0.29$ in PV and $0.27$ in L2, losing over 70% of in-sample quality).
- **Center Mobility Degrades Quality:**
  Moving centers according to running member means (mean-tracking, Arm B) systematically degrades quality-weighted yield by $13\%$ in PV and $17\%$ in L2 relative to frozen centers at birth, as center drift crowds existing cells and suppresses outlying discoveries.

## Falsification plan

1. **Ablation Falsification of Behavioral Map Decomposition:**
   - *Test:* Replace the 6D behavioral execution descriptor $\mathcal{Z}$ with a purely statistical descriptor (e.g., RankIC, IC IR, skewness) or random projection coordinates.
   - *Metric:* Quality-weighted yield and OOS quality retention on locked test data.
   - *Falsification Condition (`research-defined falsification threshold`):* If the random or statistical coordinate archive achieves $\ge 90\%$ of the quality-weighted yield and OOS retention of GoAnt, falsify the hypothesis that label-free execution profiling is the causal mechanism preserving factor diversity.

2. **Transaction Cost Escalation Stress Test:**
   - *Test:* Progressively increase effective spread from 5 bps to 50 bps and market impact parameter by $3\times$ on L2 order-book factor evaluations.
   - *Metric:* Fraction of discovered factors retaining positive net return ($N(f, C) > 0$).
   - *Falsification Condition (`research-defined falsification threshold`):* If more than 75% of GoAnt's discovered order-book factors deliver negative net returns when effective spread is doubled from 15 bps to 30 bps, the hypothesis of execution-aware robustness is disproven.

3. **Multi-Agent Search Budget Saturation Crossover:**
   - *Test:* Scale evaluation budget $B$ from 500 to 2,500 evaluations.
   - *Metric:* Quality-weighted yield of GoAnt (adaptive capacity) vs. Static Map (fixed capacity CVT-MAP-Elites).
   - *Falsification Condition (`research-defined falsification threshold`):* If a well-sited static map with fixed cardinality catches up to within 5% of GoAnt's yield as budget scales, the advantage of adaptive capacity is a finite-budget artifact rather than an asymptotic structural property.

4. **Shuffled-Microstructure Placebo Test:**
   - *Test:* Permute Level-2 order book depth queues cross-sectionally across assets while preserving marginal distributions.
   - *Metric:* Number of admitted order-book factors.
   - *Falsification Condition (`research-defined falsification threshold`):* If the search discovers $> 5$ admissible order-book factors on permuted L2 data, the admission gates fail to filter out spurious microstructure correlations.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
  The primary source demonstrates the mechanism strictly on China A-share equities (PV panels and L2 order-book snapshots). Application to cryptocurrency perpetual and spot markets is a ported research interpretation.
- **Crypto-Specific Market Microstructure Adaptations (`research-proposed`):**
  1. *Perpetual Funding Rate & Basis Costs:* In crypto perpetual futures, the 8-hour funding rate acts as a persistent carrying cost. The execution cost model $C(f)$ must incorporate cumulative funding payments alongside bid-ask spread and taker fees (`research-proposed`).
  2. *Exchange Fragmentation & Latency Arbitrage:* Unlike centralized equity exchanges with unified matching engines, crypto trades across fragmented venues (Binance, OKX, Bybit). Order-book depth imbalance signals decay within 50–500 ms due to toxic cross-venue flow; L2 factor discovery must evaluate sub-second latency and taker fee tiers (typically 2–5 bps taker) (`research-proposed`).
  3. *Continuous 24/7 Session Structure:* A-shares have distinct morning/afternoon auctions and overnight gaps. Crypto operates continuously; signal autocorrelation and turnover metrics in the 6D descriptor must be calculated on rolling 24-hour windows rather than daily trading sessions (`research-proposed`).
  4. *Extreme Volatility & Liquidations:* Cascading liquidation spirals produce severe non-Gaussian tails. The maximum drawdown gate ($> -0.50$) and spread gate ($\le 25$ bps) must be adjusted for crypto volatility regimes (`research-proposed`).

## Limitations

- **Source Code Availability Gap:** The primary working paper (`arXiv:2609.08719v2`) provides detailed pseudo-code, mathematical specifications, and hyperparameters in Supplementary Appendix H, but does not provide an open-source public code repository link. Exact reproduction requires implementing the AST grammar, MAP-Elites archive, and LoRA distillation pipeline.
- **Fixed Computational Budget:** All experiments evaluate a fixed budget of $B = 500$ evaluations across 5 random seeds (seeds 101–105). As noted by the authors, the trade-off between adaptive capacity and frozen tessellation may shift at higher evaluation budgets ($B \ge 5,000$).
- **Single Market Implementation:** Evaluated strictly on China A-share equities. Cross-market validity across US equities, European equities, and crypto derivatives remains unproven.
- **Absence of Live Execution Audit:** Reported results reflect backtested simulation under an execution cost model (Almgren-Chriss framework with effective spread gate); live capital slippage, queue priority degradation, and exchange fill dynamics have not been audited in production.

## Implementation status

`not-implemented`.
No implementation in our quantitative research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader) has been conducted. This record represents normalized research capture only.

## Adoption boundary

- Status: `research-only`
- Adoption: `not-approved`
- Approval Scope: `research-only`
- This record captures theoretical and empirical research published in `arXiv:2609.08719v2`. Its presence in this repository does not constitute evidence of profitability, validated alpha, or authorization for deployment in paper trading, testnet, or live trading systems.

## Related Wiki records

- `[[quant/alpharjm-formulaic-alpha-discovery-reward-jump-memory-sde-critic-2026-09-08]]` — Formulaic alpha discovery via single-agent reinforcement learning with event-driven jump memory and continuous-time SDE critic.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical methodology for leakage-free validation, cross-validation, and out-of-sample data partitioning.
- `[[quant/crypto-l2-liquidity-state-transitions-order-flow-2026-09-01]]` — Level-2 limit order book microstructure states and order-flow dynamics in perpetual markets.
- `[[quant/deflated-sharpe-ratio-multiple-testing-correction-2026-08-30]]` — Multiple testing corrections and deflated statistics under large evaluation budgets.

## Sources

1. Stella Zhao and Tommy Sha (University of Minnesota & Stony Brook University), *"GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data"*, arXiv preprint `arXiv:2609.08719v2 [cs.AI]`, submitted September 2026.
   - Abstract URL: [https://arxiv.org/abs/2609.08719](https://arxiv.org/abs/2609.08719)
   - Full-Text HTML: [https://arxiv.org/html/2609.08719v2](https://arxiv.org/html/2609.08719v2)
   - Full-Text PDF: [https://arxiv.org/pdf/2609.08719](https://arxiv.org/pdf/2609.08719)
   - Canonical DOI: [10.48550/arXiv.2609.08719](https://doi.org/10.48550/arXiv.2609.08719)
