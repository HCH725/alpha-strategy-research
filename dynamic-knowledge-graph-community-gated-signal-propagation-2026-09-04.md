---
schema: strategy-research-record-v1
title: "LLM-Enhanced Dynamic Knowledge Graphs with Community-Gated Signal Propagation (Zhang 2026)"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - knowledge-graph
  - llm
  - signal-propagation
  - cross-sectional
  - network-alpha
status: research-only
confidence: medium
source_as_of: 2026-07-12
sources:
  - "Lin Zhang, 'LLM-Enhanced Dynamic Financial Knowledge Graphs for Cross-Entity Signal Propagation and Alpha Discovery', arXiv:2607.10932v1 [stat.AP], July 12 2026. https://arxiv.org/abs/2607.10932"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM-Enhanced Dynamic Knowledge Graphs with Community-Gated Signal Propagation

## Provenance

- **Paper Title:** LLM-Enhanced Dynamic Financial Knowledge Graphs for Cross-Entity Signal Propagation and Alpha Discovery
- **Author:** Lin Zhang (Department of Statistics and Data Science, Southern University of Science and Technology, Shenzhen, Guangdong, China; contact: `zhangl2023@mail.sustech.edu.cn`).
- **Identifier:** arXiv:2607.10932v1 [stat.AP], submitted July 12, 2026.
- **DOI:** [10.48550/arXiv.2607.10932](https://doi.org/10.48550/arXiv.2607.10932)
- **Traceable URLs:**
  - Abstract & PDF: https://arxiv.org/abs/2607.10932
  - Full HTML Source: https://arxiv.org/html/2607.10932v1
- **Code Repository:** Public replication repository stated by author as available at [https://github.com/sustech-quant/dynamic-kg-propagation](https://github.com/sustech-quant/dynamic-kg-propagation) (primary text provides formal algorithmic specifications and calibrated simulation code).
- **Universe & Sample Period:** Evaluated on two experimental environments over $T = 750$ trading days:
  1. Stylized synthetic equity market ($N = 300$ firms, $T = 750$, 20 Monte Carlo replications).
  2. Calibrated Russell-1000 equity market ($N = 1,000$ firms, $T = 750$, 10 Monte Carlo replications) with parameters matched to Russell-1000 empirical moments (firm size, volatility, edge density, degree distributions).
- **Source Data As-Of:** July 12, 2026.

## Economic mechanism

### Source-reported

Financial markets process firm-specific disclosures with structural delays. While direct disclosures (such as 10-K/10-Q filings, earnings announcements, or press releases) are incorporated into the disclosing firm's own stock price relatively quickly, the indirect economic implications for economically linked peer entities (suppliers, customers, competitors, technology partners, or shared CapEx ecosystem constituents) diffuse much more slowly. 

Traditional quantitative approaches suffer from two key limitations:
1. **Static relationship graphs:** Conventional supply-chain or industry graphs (e.g., standard GICS or static FactSet supply-chain links) fail to capture temporal rewiring, emerging commercial partnerships, or transient operational dependencies.
2. **Homogeneous signal diffusion:** Unconstrained network diffusion models (e.g., standard PageRank or uniform heat diffusion) assume information spills across all edges equally, leading to rapid signal attenuation and dilution across noisy cross-industry ties.

The author proposes an LLM-enhanced dynamic knowledge graph (KG) framework that couples:
- **LLM-extracted structured event tuples:** Extracting directional economic shocks $e_{i,t} = (z, m, h, n, c)$ spanning 8 distinct corporate dimensions (demand, capex, pricing, inventory, supply constraint, guidance, regulatory, management) from unstructured text, calculating net firm-level innovation shocks relative to prior market expectations.
- **Dynamic graph evolution:** Continuous temporal graph updating refreshed every $\Delta\tau = 21$ trading days with edge persistence $\alpha = 0.9$ and edge survival probability $p = 0.85$, reflecting real-world corporate contract rewiring.
- **Community-gated propagation:** Applying Louvain modularity clustering on the dynamic graph to establish economic cluster boundaries, gating signal propagation such that intra-community edges propagate signals with full transmission ($\lambda_{\text{in}} = 1.0$), while inter-community edges are heavily damped ($\lambda_{\text{out}} = 0.3$).

Economically, investors within the same tightly coupled economic cluster (e.g., specialized semiconductor supply chains or cloud AI capex ecosystems) share analyst coverage, institutional investor bases, and direct cash-flow dependencies, enabling coherent signal transmission. Cross-community boundaries act as information friction barriers where signal dissipation and noise dominate.

### Research interpretation

The hypothesized alpha channel is **delayed cross-entity information diffusion along dynamically resolved economic networks**:
1. **Inattention friction:** Financial analysts and market participants focus attention primarily on primary disclosing firms. When a firm releases a major unexpected capex revision or inventory constraint shock, market prices reflect direct impacts first, but secondary impacts on connected upstream suppliers, specialized customers, and direct product competitors require multi-step financial modeling that market consensus delays by several days to weeks.
2. **Network modularity as an information container:** Dense communities in financial knowledge graphs represent coherent economic sub-economies. Intra-community links convey high-signal-to-noise cash-flow spillovers. Damping cross-community links prevents diffusion from collapsing into an uninformative macro or sector-wide average.
3. **Pure spillover alpha (excluding direct innovation):** By explicitly setting the direct step $k = 0$ coefficient to zero ($\tilde{s}_t = \sum_{k=1}^K \gamma^k P_t^k s_t$), the factor isolates the pure indirect spillover effect, eliminating overlap with conventional single-stock momentum or earnings-surprise drift.

## Signal

### Mathematical formulation (Source-reported)

1. **Structured Event Extraction & Innovation Signal:**
   Text documents $D_{i,t}$ (filings, transcripts, news) are parsed into event tuples:
   $$e_{i,t} = (z, m, h, n, c)$$
   where:
   - $z \in \{\text{demand, capex, pricing, inventory, supply constraint, guidance, regulatory, management}\}$
   - $m \in \mathbb{R}$ (signed magnitude/sentiment score)
   - $h \in \{\text{immediate, short, medium, long}\}$ (forward horizon)
   - $n \in [0, 1]$ (novelty relative to historical corpus $\mathcal{F}_{t-1}$)
   - $c \in [0, 1]$ (extraction confidence)

   The scalar innovation signal $s_{i,t}$ is computed as:
   $$s_{i,t} = \Delta\text{State}_{i,t} + \eta_{i,t}$$
   $$\Delta\text{State}_{i,t} = \text{State}_{i,t} - \mathbb{E}[\text{State}_{i,t} \mid \mathcal{F}_{t-1}]$$
   where noise $\eta_{i,t} \sim \mathcal{N}(0, \sigma_\eta^2)$.

2. **Dynamic Knowledge Graph Representation:**
   The economic network is a time-varying directed weighted graph $G_t = (V, E_t, W_t)$ across typed relationships $\rho \in \{\text{Supplier}, \text{Customer}, \text{Competitor}, \text{Technology}, \text{CapExExposure}, \text{Industry}\}$.
   - Graph refresh cadence: $\Delta\tau = 21$ trading days.
   - Dynamic weight evolution:
     $$w_{ij,t} = \alpha w_{ij,t-1} + (1-\alpha)\hat{w}_{ij,t}^{\text{obs}}$$
     where baseline $\alpha = 0.9$, edge survival probability $p_{\text{surv}} = 0.85$.
   - Transition matrix: $P_t = D_t^{-1} W_t$, where $D_{ii,t} = \sum_j w_{ij,t}$.

3. **Community Partitioning:**
   At each graph refresh date $t$, Louvain modularity maximization partitions the extracted adjacency matrix $\widehat{W}_t$ into $K_t$ non-overlapping communities $C_t = \{C_{1,t}, \dots, C_{K_t,t}\}$.

4. **Community-Gated Propagation Operator:**
   The propagated signal for firm $j$ at time $t$ is:
   $$\tilde{s}_{j,t} = \sum_{i=1}^N w_{ij,t} \cdot \phi(C_{i,t}, C_{j,t}) \cdot s_{i,t}$$
   where the community gating kernel is:
   $$\phi(C_{i,t}, C_{j,t}) = \begin{cases} \lambda_{\text{in}} & \text{if } C_{i,t} = C_{j,t} \\ \lambda_{\text{out}} & \text{if } C_{i,t} \neq C_{j,t} \end{cases}$$
   Source baseline parameters: $\lambda_{\text{in}} = 1.0$, $\lambda_{\text{out}} = 0.3$.
   Multi-hop diffusion uses damped propagation with $K = 2$ hops and decay parameter $\gamma = 0.35$, explicitly excluding the direct $k = 0$ innovation term.

5. **Derived Factors:**
   - **Community Information Surprise (CIS):**
     $$\text{CIS}_{k,t} = \sum_{i \in C_{k,t}} \omega_{i,t} \Delta\text{State}_{i,t}, \quad \omega_{i,t} = \frac{\text{MktCap}_{i,t}}{\sum_{m \in C_{k,t}} \text{MktCap}_{m,t}}$$
   - **Propagated Information Surprise (PIS):**
     $$\text{PIS}_{j,t} = \sum_{k=1}^{K_t} \text{Exposure}_{j,k,t} \times \text{CIS}_{k,t}, \quad \text{Exposure}_{j,k,t} = \frac{\sum_{i \in C_{k,t}} w_{ij,t}}{\sum_{m=1}^N w_{mj,t}}$$

### Operational Specifications

- **Formation Timestamp:** Daily, calculated at close of trading day $t$ using text events released up to market close on date $t$.
- **Execution Delay:** `research-proposed` Market order execution at the market open of day $t+1$ ($T_{\text{exec}} = t+1\text{ Open}$), allowing overnight compute for LLM tuple extraction and graph diffusion.
- **Lookback & Refresh:** 
  - Dynamic graph adjacency matrix updated every $\Delta\tau = 21$ trading days (monthly).
  - AR(1) edge persistence: $\alpha = 0.9$ with $p_{\text{surv}} = 0.85$.
  - Daily innovation signals aggregated over the trailing 1 to 5 days.
- **Cross-Sectional Portfolio Construction:**
  - Rank universe cross-sectionally by community-propagated signal $\tilde{s}_{j,t}$ (or $\text{PIS}_{j,t}$).
  - Long top quintile (Q5, highest positive incoming spillover surprise).
  - Short bottom quintile (Q1, highest negative incoming spillover surprise).
  - Equal weighting within quintiles (dollar-neutral long/short).
- **Rebalance Cadence:** Evaluated at 10-day rebalancing frequency in primary text; factor decay shows persistence through 20 trading days ($h = 20$).

## Required data

- **Universe:** US Equities ($N = 300$ to $1,000$ liquid stocks; calibrated to Russell-1000 constituents).
- **Market Data:**
  - Daily Open, High, Low, Close, Volume (OHLCV).
  - Daily market capitalization for CIS weight calculation ($\omega_{i,t}$).
  - Adjusted returns for forward return horizon evaluation ($h = 1, 5, 10, 20$ days).
- **Textual & Unstructured Data:**
  - Regulatory filings (SEC 10-K, 10-Q, 8-K).
  - Earnings call transcripts and corporate press releases.
  - Timestamp precision: Exact filing/release publication timestamp with strict point-in-time enforcement (events published after 16:00 EST enter at $t+1$).
- **Relationship Knowledge Graph:**
  - Initialized from supply-chain filings, customer-supplier disclosures, segment competitor disclosures, and patent/technology co-classifications.
  - Dynamically updated via LLM entity-relationship extraction every 21 trading days.
- **Missing Data Handling:** `research-proposed` Firms with missing event disclosures receive zero direct innovation ($s_{i,t} = 0$), but continue to receive propagated peer signals through existing graph edges if connected. Firms with zero graph degree receive zero propagated signal and are placed in the neutral quintile (Q3).

## Execution assumptions

- **Execution Timing:** `research-proposed` Orders generated at day $t$ market close; executed at market open on trading day $t+1$ ($T+1$ Open).
- **Order Type:** `research-proposed` MOC (Market-On-Close) or MOO (Market-On-Open) market orders to ensure complete fillability across the liquid quintile basket.
- **Transaction Costs & Slippage (Source-reported):**
  - Gross performance evaluated at 0 bps.
  - Net performance explicitly evaluated at:
    - 5 bps round-trip transaction costs.
    - 10 bps round-trip transaction costs.
- **Fill Model:** `research-proposed` Linear volume participation assumption capped at $\le 1.0\%$ of Average Daily Volume (ADV) to avoid severe market impact.
- **Borrow & Shorting:** Dollar-neutral long/short quintile portfolio requires borrow availability for Q1 constituents; borrow fee assumed at baseline general collateral rate (50 bps annualized) in equity large-caps (`research-proposed`).
- **Margin & Leverage:** 1x gross leverage (100% long / 100% short, net zero dollar exposure).

## Evidence

### Source-reported

The primary paper evaluates five nested model specifications across both Stylized ($N = 300$) and Calibrated Russell-1000 ($N = 1,000$) environments over $T = 750$ trading days:
- **M1:** Raw sentiment score ($m_{i,t}$)
- **M2:** Direct innovation shock ($\Delta\text{State}_{i,t}$)
- **M3:** Static-KG damped propagation ($\tilde{s}_t^{\text{static}}$, $K=2, \gamma=0.35$)
- **M4:** Dynamic-KG damped propagation ($\tilde{s}_t^{\text{dynamic}}$)
- **M5:** Community-aware dynamic KG propagation ($\tilde{s}_{j,t}$ with Louvain gating $\lambda_{\text{in}} = 1.0, \lambda_{\text{out}} = 0.3$)

#### 1. Stylized Market Environment ($N = 300, T = 750, 20$ Replications)

- **Rank Information Coefficient ($h = 5$ days, Table 1):**
  - M1 (Sentiment): Rank IC = 0.0086, ICIR = 0.149, $t$-statistic = 1.73
  - M2 (Direct Innovation): Rank IC = 0.0126, ICIR = 0.219, $t$-statistic = 2.53
  - M3 (Static-KG): Rank IC = 0.0133, ICIR = 0.234, $t$-statistic = 2.70
  - M4 (Dynamic-KG): Rank IC = 0.0156, ICIR = 0.273, $t$-statistic = 3.15
  - M5 (Community-aware M5): Rank IC = **0.0161**, ICIR = **0.282**, $t$-statistic = **3.26**

- **Fama-MacBeth Cross-Sectional Pricing Regressions (Table 2):**
  - M1: Sentiment $\beta_1 = 0.009$ ($t = 0.82$, insignificant)
  - M2: Direct Innovation $\beta_1 = 0.027$ ($t = 2.41, p < 0.05$, 65% rejection rate)
  - M3: Propagated $\beta_2 = 0.013$ ($t = 1.14$, insignificant, 25% rejection rate)
  - M4: Propagated $\beta_2 = 0.038$ ($t = 3.28, p < 0.01$, 85% rejection rate)
  - M5: Propagated $\beta_2 = \mathbf{0.043}$ ($t = \mathbf{3.72}, p < \mathbf{0.01}$, 90% rejection rate)

- **Quintile Long/Short Portfolio Performance (10-Day Rebalancing, Table 3):**
  - M1: Gross Return = 1.1%, Vol = 4.6%, Gross Sharpe = 0.24, Max DD = 6.8%, Turnover = 2.41; Net Sharpe (5 bps) = -0.49, Net Sharpe (10 bps) = -1.22
  - M2: Gross Return = 2.2%, Vol = 4.3%, Gross Sharpe = 0.52, Max DD = 5.4%, Turnover = 2.40; Net Sharpe (5 bps) = -0.19, Net Sharpe (10 bps) = -0.91
  - M3: Gross Return = 2.1%, Vol = 4.3%, Gross Sharpe = 0.48, Max DD = 5.8%, Turnover = 2.38; Net Sharpe (5 bps) = -0.27, Net Sharpe (10 bps) = -0.99
  - M4: Gross Return = 3.2%, Vol = 4.2%, Gross Sharpe = 0.76, Max DD = 4.5%, Turnover = 2.39; Net Sharpe (5 bps) = 0.02, Net Sharpe (10 bps) = -0.71
  - M5: Gross Return = **3.5%**, Vol = **4.2%**, Gross Sharpe = **0.83**, Max DD = **4.2%**, Turnover = **2.39**; Net Sharpe (5 bps) = **0.10**, Net Sharpe (10 bps) = **-0.62**

- **Mechanism Validation Regression (Equation 12):**
  $$R_{j,t,t+h} = \alpha_j + \lambda_{\text{in}}\tilde{s}_{j,t}^{\text{in}} + \lambda_{\text{out}}\tilde{s}_{j,t}^{\text{out}} + \epsilon_{j,t}$$
  - Feasible extracted graph: $\hat{\lambda}_{\text{in}} = 8.8\text{ bps}$ ($t = 4.8$), $\hat{\lambda}_{\text{out}} = -0.2\text{ bps}$ ($t = -0.2$), difference $t\text{-stat} = 5.7$ ($p < 0.001$). Intra-community transmission accounts for virtually all predictive alpha.

#### 2. Calibrated Russell-1000 Environment ($N = 1,000, T = 750, 10$ Replications)

- **Rank Information Coefficient ($h = 5$ days, Table 5):**
  - M1: Rank IC = 0.0054, ICIR = 0.173
  - M2: Rank IC = 0.0074, ICIR = 0.234
  - M3: Rank IC = 0.0083, ICIR = 0.262
  - M4: Rank IC = 0.0093, ICIR = 0.297
  - M5: Rank IC = **0.0096**, ICIR = **0.304**, $t$-statistic = **3.51**
  - Multi-horizon decay (M5): $h=1 \rightarrow \text{IC}=0.0051$; $h=5 \rightarrow \text{IC}=0.0096$; $h=10 \rightarrow \text{IC}=0.0081$; $h=20 \rightarrow \text{IC}=0.0057$. Signal peaks around day 5 and persists through day 20.

- **Fama-MacBeth Pricing Regressions (Table 6):**
  - M5: Propagated $\beta_2 = \mathbf{0.023}$ ($t = \mathbf{2.91}, p < 0.01$, 80% rejection rate).

- **Quintile Long/Short Portfolio Performance (10-Day Rebalancing, Table 7):**
  - M5: Gross Return = **2.9%**, Vol = **2.5%**, Gross Sharpe = **1.16**, Max DD = **2.8%**, Two-sided Turnover = **2.33**; Net Sharpe (5 bps) = **-0.03**, Net Sharpe (10 bps) = **-1.22**.

- **Mechanism Validation Regression (Table 8):**
  - Feasible graph: $\hat{\lambda}_{\text{in}} = 5.4\text{ bps}$ ($t = 3.8$), $\hat{\lambda}_{\text{out}} = 0.8\text{ bps}$ ($t = 0.9$), difference $t\text{-stat} = 3.6$ ($p < 0.01$).

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Sensitivity to Transaction Costs:** As explicitly demonstrated in Tables 3 and 7 of the source paper, a standalone 10-day rebalanced long/short quintile strategy suffers severe turnover ($2.33$ to $2.39$ two-sided turns per period). At 5 bps round-trip transaction costs, the net Sharpe ratio drops to near-zero ($+0.10$ in stylized, $-0.03$ in Russell-1000); at 10 bps costs, net Sharpe collapses deeply into negative territory ($-0.62$ to $-1.22$). The raw standalone factor is not viable as an unconstrained rapid-turnover trading strategy without turnover-reduction overlays or incorporation into an existing multi-factor optimizer.
- **Static KG Insufficiency:** Static knowledge graphs (M3) fail to achieve statistical significance in Fama-MacBeth regressions ($t = 1.14$, only 25% rejection rate), confirming that static supply-chain maps without temporal rewiring produce weak, stale signals.
- **Dilution across Sparser Graphs:** In the calibrated 1,000-stock market where edge density is lower (0.015 vs 0.04), individual factor IC drops from 0.0161 to 0.0096, demonstrating dependence on graph completeness.

## Falsification plan

The following empirical tests are defined to disconfirm the proposed alpha mechanism:

1. **Intra- vs. Inter-Community Transmission Contrast:**
   - *Test:* Run regression Equation 12 on historical equity data.
   - *Decision Rule:* If $\hat{\lambda}_{\text{in}} - \hat{\lambda}_{\text{out}} \le 0$ or the difference $t$-statistic is $< 2.0$, falsify the community-gating hypothesis.
2. **Network Scrambling (Placebo Permutation Test):**
   - *Test:* Randomly rewire the edges of $W_t$ while preserving the empirical degree distribution, then recalculate community-propagated signals $\tilde{s}_{j,t}$.
   - *Decision Rule:* `research-defined falsification threshold` If the scrambled network achieves $\ge 70\%$ of the empirical Rank IC, falsify the specific economic knowledge graph topology.
3. **Point-in-Time Event Lag Audit:**
   - *Test:* Impose an artificial 24-hour publication lag on all corporate disclosures.
   - *Decision Rule:* `research-defined falsification threshold` If 5-day forward Rank IC drops by more than 60%, the reported returns may stem from look-ahead leakage in timestamping.
4. **Turnover-Constrained Multi-Factor Integration:**
   - *Test:* Evaluate the signal as an alpha tilt within a risk-model-constrained quadratic optimizer with turnover penalty ($\lambda_{\text{tc}} = 10\text{ bps}$).
   - *Decision Rule:* `research-defined falsification threshold` If the incremental information ratio (IR) over a standard Fama-French 5-factor + momentum benchmark is $\le 0.20$, reject standalone adoption.

## Crypto portability

**Adapted**

The core mechanism—delayed cross-entity signal propagation across network communities—theoretically ports to cryptocurrency and decentralized finance ecosystems, which exhibit intense narrative coupling, shared token treasuries, and protocol dependencies. However, direct porting is subject to substantial structural shifts:

- **Ecosystem Knowledge Graph (`research-proposed`):** Instead of corporate customer/supplier filings, the crypto dynamic knowledge graph must be constructed from:
  1. On-chain composability graphs (e.g., liquidity pools, yield vaults, collateral dependencies between protocols).
  2. Ecosystem co-investments and venture backing clusters (e.g., shared foundation grants, venture portfolios).
  3. Shared infrastructure dependencies (e.g., shared L1/L2 settlement layers, shared oracle dependencies).
- **24/7 Continuous Signal Propagation:** Unlike equity markets with daily closes and earnings calendar cadences, crypto disclosures and on-chain governance votes occur 24/7/365. Refreshing graphs monthly ($\Delta\tau = 21\text{ days}$) would be too slow; crypto graphs require dynamic weekly or on-chain event-triggered updates.
- **Fragmentation & Perpetual Futures:** Cross-sectional ranking must be applied across liquid perpetual futures contracts (e.g., top 100 Binance/Bybit perps) with funding-rate cost adjustments.
- **Status:** Unproven in crypto markets. No empirical crypto evidence is presented in the paper; all crypto adaptations remain exploratory research interpretations.

## Limitations

- **Simulated Backtest Architecture:** The primary paper's results are derived from stylized and Russell-1000 calibrated multi-agent simulation environments rather than an uninterrupted 20-year live execution tape.
- **Heavy Transaction Cost Drag:** High factor turnover ($>2.3$ two-sided turns per 10-day period) completely erodes gross Sharpe ratios at standard retail and institutional cost levels (5 to 10 bps).
- **LLM Extraction Compute Overhead:** Extracting structured event tuples $e_{i,t} = (z, m, h, n, c)$ across thousands of corporate filings and daily transcripts requires substantial LLM inference throughput and is susceptible to prompt drift and model hallucination.
- **Graph Incompleteness:** Private commercial relationships, informal partnerships, and unannounced customer arrangements are omitted from public filings, leading to edge sparsity.
- **No Independent Physical Replication:** The strategy has not been independently reproduced in our local research stack.

## Implementation status

`not-implemented`

No code, data pipelines, LLM parsers, or network propagation operators have been implemented in our research or execution infrastructure. The strategy exists solely as a normalized research record.

## Adoption boundary

This record is research material only. It does not imply:
- Validated or profitable alpha in our operational universe.
- Approval for portfolio inclusion, PyBroker testing, Nautilus validation, or paper/testnet/live trading.
- Exemption from rigorous turnover-reduction overlays and point-in-time leakage audits.

## Related Wiki records

- `[[quant/dynamic-graph-structural-alpha-2026-09-04]]` (Structural tails and network rewiring in corporate disclosure networks)
- `[[quant/event-driven-llm-sentiment-alpha-2026-09-04]]` (Event-aware LLM sentiment factor extractions)
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` (Cross-validation and information leakage protections)

## Sources

1. Lin Zhang, "LLM-Enhanced Dynamic Financial Knowledge Graphs for Cross-Entity Signal Propagation and Alpha Discovery", arXiv:2607.10932v1 [stat.AP], July 12, 2026. Available at: [https://arxiv.org/abs/2607.10932](https://arxiv.org/abs/2607.10932).
2. SUSTech Quant Group, Dynamic Knowledge Graph Propagation Replication Repository: [https://github.com/sustech-quant/dynamic-kg-propagation](https://github.com/sustech-quant/dynamic-kg-propagation).
