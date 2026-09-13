---
schema: strategy-research-record-v1
title: "Point-in-Time Supply Chain Lead-Lag Information Diffusion: Customer Pressure Momentum, Hermitian MetaCluster Meta-Flow, ClusterRank Local Laggers, and Directional Reverse Placebo Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - cross-sectional
  - lead-lag
  - supply-chain
  - network-momentum
  - hermitian-clustering
  - information-diffusion
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "nicjia, 'supply-chain-lead-lag: Quantitative strategy exploiting lead-lag return predictability across supply chain networks', GitHub repository, commit 1cd62fdf5e4100bab9605ec7eb808f38369b5b02 (September 13, 2026), https://github.com/nicjia/supply-chain-lead-lag"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Point-in-Time Supply Chain Lead-Lag Information Diffusion: Customer Pressure Momentum, Hermitian MetaCluster Meta-Flow, ClusterRank Local Laggers, and Directional Reverse Placebo Falsification

## Provenance

- **Primary Source Repository:** `nicjia/supply-chain-lead-lag`, public GitHub repository: `https://github.com/nicjia/supply-chain-lead-lag`.
- **Immutable Commit SHA:** `1cd62fdf5e4100bab9605ec7eb808f38369b5b02` (committed September 13, 2026).
- **Exact Primary Source Paths Examined:**
  - `README.md`: System architecture, pipeline stages, rebalance specifications, and CLI commands.
  - `docs/FRAMEWORK.md`: Research questions (RQ1–RQ7), causal hypothesis, and falsification criteria.
  - `docs/IMPLEMENTATION_SPEC.md`: Mathematical specifications for strategy families, network matrices, and clustering algorithms.
  - `docs/EXPECTED_OUTPUTS.md`: Output file contracts and regression table specifications.
  - `supply_chain_leadlag/matrix.py`: Pairwise edge scoring (`tstat_diff`, `beta_diff`, `cross_corr`, `regression_r2`, `granger`, `levy`), lead-lag matrix $C$, skew matrix $S = C - C^\top$, and hybrid matrix construction.
  - `supply_chain_leadlag/backtest.py`: Rolling point-in-time (PIT) backtesting engine, edge filtering, supplier pressure signal generation, and long-short quantile weighting.
  - `supply_chain_leadlag/strategy_families.py`: Strategy family interface for `supplier_pressure`, `globalrank`, `metacluster`, and `clusterrank`.
  - `supply_chain_leadlag/metacluster_strategy.py`: Inter-cluster directed flow matrix $F_{ab}$ and leading-to-lagging cluster trading engine.
  - `supply_chain_leadlag/clusterrank_strategy.py`: Intra-cluster local leadingness ranking $\ell_i^{(c)}$ and laggers-only long-short execution.
  - `supply_chain_leadlag/clustering_methods.py`: Sector, supply community, symmetric spectral, Hermitian spectral, and signed clustering algorithms.
  - `supply_chain_leadlag/signals.py`: Lagged linear signal computation, Frobenius matrix distance, and portfolio metrics.
  - `results/final_research/report/final_report.md`: Complete empirical research report with 155-rebalance backtest results, panel regressions, hybrid alpha sweeps, and strategy correlations.
  - `results/final_research/config_used.yaml`: Parameter configuration frozen for the 155-rebalance empirical run.
  - `results/final_research/run_metadata.json`: Machine, runtime, dataset, and git commit metadata (`a1deef529fe2f98c5ba81457ac942759cb81a8a0`).
  - `tests/test_strategy_families.py`: Unit and regression test specifications verifying supplier-only trading, zero-sum weights, and pre-blended hybrid matrices.
- **Data Scope & Universe:** US equity universe comprising 5,461 return assets (`data/returns_with_gvkey.parquet`) and 17,153 point-in-time supply-chain edge observations (`data/merged_edges.csv`) between 1,198 unique customer firms and 1,857 unique supplier firms. Sample covers 15 years (2010-01-04 through 2024-12-31, 3,774 trading days) evaluated across 155 monthly rebalances (`BME` frequency).
- **Repository Deduplication:** Checked against all existing records in `alpha-strategy-research`. Zero prior records analyze `nicjia/supply-chain-lead-lag`. Existing lead-lag records (`equity-lead-lag-clustering-minirocket-dtw-rowsum-momentum-2026-09-02.md`, `commodity-futures-network-momentum-lead-lag-graph-learning-2026-09-02.md`, `crypto-cross-sectional-lead-lag-rotation-hyperliquid-perps-2026-09-13.md`) focus on statistical MiniRocket/DTW clustering without supply networks, commodity futures learning, or Hyperliquid perps. An NLP record (`supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04.md`) propagates FinBERT embeddings over a static text graph. None evaluate point-in-time customer-pressure returns, Hermitian meta-clustering, ClusterRank laggers, or directional reverse placebos.

---

## Economic mechanism

### Source-reported

1. **Slow Information Diffusion Along Supply Chains:** The primary economic thesis posits that value-relevant economic shocks originate at major customer firms and propagate with a lag to their economically dependent suppliers. Because complex customer-supplier relationships require high analytical processing effort and retail/institutional attention is disproportionately allocated to high-profile consumer-facing companies, supplier equity prices incorporate customer demand and earnings signals with a friction-induced delay (typically 1 to 2 trading days).
2. **Directional Economic Asymmetry ($Customer \to Supplier$ vs $Supplier \to Customer$):** The revenue-dependence edge is inherently directional:
   $$w_{j \to i, t} = \frac{\text{sales from supplier } i \text{ to customer } j}{\text{total sales of supplier } i}$$
   A customer firm $j$ representing 20% of supplier $i$'s total sales creates an asymmetric cash-flow exposure. A return shock to customer $j$ directly impacts supplier $i$'s future order volume, whereas a return shock to supplier $i$ typically has a negligible impact on customer $j$'s overall procurement or valuation.
3. **Higher-Order Network Aggregation & Meta-Flows:** Pairwise return-based lead-lag estimates between single stock pairs are notoriously noisy. By aggregating pairwise links into higher-order network structures—such as directed inter-cluster flow between industrial sectors (`metacluster`) or local leadership hierarchies within signed spectral partitions (`clusterrank`)—the signal filters idiosyncratic noise while preserving macro-structural information diffusion.
4. **Structural Priors for Return Networks:** Return-based lead-lag matrices ($C^{data}$) are unstable over time due to sample covariance noise. Blending return-derived lead-lag matrices with structural supply-chain adjacency matrices ($C^{supply}$) via a convex combination ($C^{hybrid} = \alpha C^{data} + (1-\alpha) C^{supply}$) tests whether structural economic links stabilize eigenspace drift and improve out-of-sample risk-adjusted returns.

### Research interpretation

1. **Behavioral Inattention vs. Fundamental Lead-Lag:** The customer momentum effect is primarily an inattention anomaly rather than a risk premium. As market efficiency has increased over the 2010–2024 sample, daily customer-to-supplier predictability has compressed, requiring faster execution and tighter sector neutralization to avoid factor confounding.
2. **Confounding by Industry and Macro Factors:** A critical challenge in supply-chain lead-lag research is distinguishing true idiosyncratic supply-chain diffusion from industry-wide momentum or common market factor shocks. If customer and supplier belong to adjacent industries undergoing simultaneous cyclical re-ratings, pooled OLS regressions will show apparent lead-lag predictability that is actually driven by factor auto-correlation.
3. **Severe Drawdown Risk in Network Equities:** The empirical results reveal massive historical drawdowns (-71.06% for supplier pressure) across the 2010–2024 period, reflecting severe liquidation crises (e.g., March 2020 COVID shock, 2022 rate hike cycle) where small-cap suppliers experience severe liquidity evaporation. Unhedged customer-supplier momentum cannot be traded without explicit volatility targeting and drawdown containment.

---

## Signal

### Formation timestamp

- **Rebalance Cadence:** Monthly on Business Month End (`rebalance_freq: BME`, `max_rebalances: 155`). Evaluated across 155 historical rebalance dates from 2010 to 2024 (`source-reported`).
- **Matrix Estimation Timing:** At each rebalance date $T$, the lead-lag matrix $C$ is computed using historical trailing returns up to date $T$ and point-in-time supply-chain edges with `filing_date <= T` (`source-reported`).
- **Daily Signal Generation Timing:** For daily-updating strategies (`supplier_pressure`, `metacluster`, `clusterrank`), signals are evaluated on each day $d$ using closed daily returns $r_d$ (`source-reported`).
- **Tradability & Execution Timestamp:** Weights computed from day $d$ returns are applied on day $d+1$ (`apply_next_day: true`), strictly avoiding same-day lookahead bias (`source-reported`). Orders execute at day $d+1$ market open or VWAP (`research-proposed`).

### Lookback windows

- **Lead-Lag Matrix Lookback ($W_{matrix}$):** 504 trading days (~2 calendar years) of daily returns (`lookback_rows: 504`, `source-reported`).
- **Prediction Horizon ($h$):** 1 trading day (`horizon: 1`, `source-reported`).
- **Minimum Pairwise Observations:** 80 overlapping trading days (`min_obs: 80`, `source-reported`).
- **Edge Expiry Horizon:** 550 calendar days from SEC filing date (`edge_expiry_days: 550`, `source-reported`).
- **Quantile Truncation / Winsorization:** Two-tailed return winsorization at 0.1% quantile (`winsor_q: 0.001`, `source-reported`).

### Strategy families & entry/exit rules

#### 1. Supplier Pressure Strategy (`supplier_pressure`)

- **Pairwise Lead-Lag Asymmetry Matrix $C$:**
  For each customer-supplier pair $(j, i)$ where edge weight $w_{ji} > 0$:
  - Estimate forward regression: $r_i(t+1) = \alpha_{fwd} + \beta_{fwd} r_j(t) + \epsilon$ with $t$-statistic $t_{fwd}$.
  - Estimate reverse regression: $r_j(t+1) = \alpha_{rev} + \beta_{rev} r_i(t) + \epsilon$ with $t$-statistic $t_{rev}$.
  - Compute directed score:
    $$C_{ji} = w_{ji} \cdot (t_{fwd} - t_{rev})$$
    (using `score: tstat_diff`, `source-reported`).
- **Daily Customer Pressure Signal:**
  On day $d$, given vector of cross-sectional returns $r_d$:
  $$s_d = C^\top r_d$$
  where $s_d(i) = \sum_j C_{ji} r_j(d)$ measures aggregate customer return pressure on supplier $i$ (`source-reported`).
- **Traded Universe:** Traded assets are restricted strictly to suppliers ($\text{columns of } C$); customers receive weight 0.0 (`source-reported`).
- **Portfolio Construction:**
  - Rank eligible suppliers by $s_d$.
  - Long top quantile $q = 0.20$ suppliers with weight $+1 / K$.
  - Short bottom quantile $q = 0.20$ suppliers with weight $-1 / K$, where $K = \lfloor |Suppliers| \cdot q \rfloor$.
  - Weights sum to zero ($\sum w_i = 0$), forming a dollar-neutral portfolio (`source-reported`).
- **Holding Period:** Rebalanced daily at day $d+1$ (`source-reported`).

#### 2. GlobalRank Strategy (`globalrank`)

- **Skew Matrix Construction:** At rebalance date $T$, form skew matrix:
  $$S = C - C^\top$$
- **Hermitian Spectral Ranking:** Construct Hermitian matrix $H = i S$. Compute leading eigenvector $v_1$ of $H$. Node scores correspond to the magnitude/phase embedding of $v_1$ (`globalrank_method: spectral`, `source-reported`).
- **Portfolio Construction:** Long top $q = 0.20$ nodes by score, short bottom $q = 0.20$ nodes.
- **Holding Period:** Held statically across the monthly rebalance cycle (no daily return rebalancing, `source-reported`).

#### 3. MetaCluster Strategy (`metacluster`)

- **Cluster Partition:** Assign firms to GICS sectors (`clustering_method: sector`, 11 sectors, `source-reported`).
- **Inter-Cluster Meta-Flow Matrix:**
  $$F_{ab} = \frac{1}{|C_a||C_b|} \sum_{i \in C_a, j \in C_b} (C_{ij} - C_{ji})$$
- **Edge Selection:** Filter pairs $(a, b)$ with positive directed meta-flow ($F_{ab} > 0$); select top 10% strongest edges (`top_frac: 0.10`, `source-reported`).
- **Signal & Trading:** For each active meta-flow edge $a \to b$, calculate leading sector return $R_{a, d} = \frac{1}{|C_a|} \sum_{i \in C_a} r_{i, d}$. Trade lagging sector $b$ on day $d+1$ with sign of $R_{a, d}$ (`source-reported`).

#### 4. ClusterRank Strategy (`clusterrank`)

- **Signed Spectral Clustering:** Partition firms dynamically using positive and negative parts of $S = C - C^\top$ (`clustering_method: signed`, `source-reported`).
- **Local Skew & Leadingness:** Inside cluster $c$, compute local skew $S^{(c)} = C^{(c)} - (C^{(c)})^\top$ and local leadingness $\ell_i^{(c)} = \sum_{j \in c} S_{ij}^{(c)}$ (`source-reported`).
- **Signal Formation:** Identify local leaders (top quantile $q$) and local laggers (bottom quantile $q$). Signal is local leader average return:
  $$Signal_{c, d} = \frac{1}{|Leaders_c|} \sum_{i \in Leaders_c} r_{i, d}$$
- **Laggers-Only Trading:** Trade laggers only: long top laggers, short bottom laggers conditioned on $Signal_{c, d}$ (`source-reported`).

### Parameters

| Parameter | Value | Source Status | Rationale / Description |
| :--- | :--- | :--- | :--- |
| `rebalance_freq` | `BME` (Monthly) | `source-reported` | Business Month End matrix re-estimation cadence. |
| `lookback_rows` | 504 trading days | `source-reported` | Trailing return window for estimating $C$ (~2 years). |
| `horizon` | 1 trading day | `source-reported` | Forward lag for customer-to-supplier prediction. |
| `edge_score` | `tstat_diff` | `source-reported` | Asymmetric t-statistic difference $t_{fwd} - t_{rev}$ weighted by $w_{ji}$. |
| `winsor_q` | 0.001 (0.1%) | `source-reported` | Two-tailed winsorization of daily return outliers. |
| `min_obs` | 80 trading days | `source-reported` | Minimum pairwise overlapping return observations required to populate an edge. |
| `edge_expiry_days`| 550 calendar days | `source-reported` | Maximum shelf-life of an SEC supply-chain relationship filing. |
| `q` | 0.20 (20%) | `source-reported` | Top and bottom quantile for long-short basket selection. |
| `apply_next_day` | `true` | `source-reported` | Causal execution: weights calculated from $t$ returns apply to $t+1$ returns. |
| `hybrid_alpha` | Grid: [0.0, 0.25, 0.5, 0.75, 1.0] | `source-reported` | Blending factor between data-driven $C^{data}$ and structural $C^{supply}$. |
| `metacluster_top_frac` | 0.10 (10%) | `source-reported` | Proportion of top positive directed meta-flow edges retained. |
| `n_clusters` | 10 | `source-reported` | Target cluster count for network clustering algorithms. |
| `commission_bps` | 0.0 bps | `source-reported` | Zero baseline cost assumption in reported research runs (`provenance gap`). |
| `slippage_bps` | 0.0 bps | `source-reported` | Zero slippage assumption in reported research runs (`provenance gap`). |
| `borrow_bps_annual`| 0.0 bps | `source-reported` | Zero short borrow cost assumption in reported research runs (`provenance gap`). |
| Execution benchmark | VWAP / Open | `research-proposed` | Realistic execution fill benchmark for day $d+1$ rebalances. |
| Minimum ADTV | $5,000,000 | `research-proposed` | Liquidity filter to prevent small-cap supplier execution bottlenecks. |

---

## Required data

- **Asset Universe:** US equity universe covering 5,461 equity assets identified by Compustat GVKEY (`returns_with_gvkey.parquet`, `source-reported`).
- **Market Type:** US cash equities (common stock, `source-reported`).
- **Return Data:** Daily close-to-close total returns from 2010-01-04 to 2024-12-31 (3,774 trading days, `source-reported`).
- **Supply-Chain Network Data:** 17,153 point-in-time customer-supplier relationships (`merged_edges.csv`) linking 1,198 unique customers and 1,857 unique suppliers (`source-reported`). Includes `customer_gvkey`, `supplier_gvkey`, revenue weight `weight_wji`, and SEC disclosure filing date `filing_date` (`source-reported`).
- **Industry Classifications:** GICS sector maps (`sector_map.csv`, `firm_classification_map.csv`) mapping GVKEYs to 11 macro sectors (`source-reported`).
- **Point-in-Time Discipline:** Edges filtered strictly by `filing_date <= T` with a 550-day rolling expiration window. No forward-looking Compustat customer revisions are permitted (`source-reported`).
- **Missing Data Handling:** Pairs with fewer than 80 overlapping returns are omitted from matrix estimation. Missing asset returns on day $d$ are imputed as 0.0 for signal dot-product purposes (`source-reported`).

---

## Execution assumptions

### Source-reported

- **Signal-to-Order Timing:** Next-day execution (`apply_next_day: true`). Signals formed at day $d$ market close earn returns over day $d+1$.
- **Portfolio Dollar Neutrality:** Long weights sum to $+1.0$, short weights sum to $-1.0$; gross leverage is 2.0.
- **Transaction Costs & Fees:** The reported 155-rebalance backtest results assume 0.0 bps commissions, 0.0 bps slippage, and 0.0 bps short borrow financing (`Table 13: gross_sharpe == net_sharpe`). The author explicitly highlights this provenance gap: *"avg_turnover is NaN and total_cost_bps is 0 — gross Sharpe equals net Sharpe. Populate turnover/cost assumptions before submission."*

### Research-proposed

- **Execution Venue & Order Routing:** MOC (Market-On-Close) or TWAP over the opening 30 minutes on US exchanges (`research-proposed`).
- **Realistic Commission & Exchange Fees:** 5.0 bps per leg (10.0 bps round-trip) for US institutional equity execution (`research-proposed`).
- **Market Impact & Slippage:** Model slippage as a function of daily volume: $\text{slippage} = 5.0\text{ bps} + 10.0\text{ bps} \times \sqrt{\text{Order Size} / \text{ADTV}}$ (`research-proposed`).
- **Short Borrow Availability & Cost:** Small-cap suppliers often carry elevated short interest. Assume general collateral (GC) borrow rate of 50 bps annualized for large-cap suppliers, and 300 to 500 bps annualized for hard-to-borrow small-cap suppliers (`research-proposed`).
- **Liquidity Floor:** Exclude supplier firms with 20-day Average Daily Traded Volume (ADTV) below $5,000,000 (`research-proposed`).

---

## Evidence

### Source-reported

All quantitative performance figures below trace directly to the official research report `results/final_research/report/final_report.md` in repository `nicjia/supply-chain-lead-lag` (commit `1cd62fdf5e4100bab9605ec7eb808f38369b5b02`, generated May 25, 2026, over the 2010-01-04 to 2024-12-31 sample with 155 BME rebalances):

#### 1. Strategy Family Backtest Performance (155 Rebalances, 2010–2024)

| Strategy Family | Clustering Method | Edge Score | Ann. Return | Ann. Vol | Sharpe | Max Drawdown | Traded Universe |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`supplier_pressure`** | `signed` (bookkeeping) | `tstat_diff` | **11.14%** (0.111417) | 21.38% (0.213785) | **0.52** (0.521166) | **-71.06%** (-0.710557) | Suppliers only ($s=C^\top r$) |
| **`clusterrank`** | `signed` (network) | `tstat_diff` | **5.33%** (0.053263) | 14.55% (0.145470) | **0.37** (0.366141) | **-48.35%** (-0.483454) | Laggers only within clusters |
| **`metacluster`** | `sector` (GICS) | `tstat_diff` | **11.35%** (0.113467) | 34.56% (0.345592) | **0.33** (0.328328) | **-56.75%** (-0.567501) | Lagging sectors via meta-flow |
| **`globalrank`** | `signed` (network) | `tstat_diff` | **2.03%** (0.020282) | 19.25% (0.192481) | **0.11** (0.105370) | **-64.31%** (-0.643095) | Full network spectral rank |

#### 2. Strategy Family Cross-Correlation & Diversification (Daily Returns)

| Family | `supplier_pressure` | `metacluster` | `clusterrank` | `globalrank` |
| :--- | :--- | :--- | :--- | :--- |
| `supplier_pressure` | 1.000 | **0.008** | **-0.042** | **0.093** |
| `metacluster` | **0.008** | 1.000 | **0.025** | **0.022** |
| `clusterrank` | **-0.042** | **0.025** | 1.000 | **-0.059** |
| `globalrank` | **0.093** | **0.022** | **-0.059** | 1.000 |

- **Orthogonality:** `supplier_pressure` and `metacluster` exhibit near-zero return correlation (**0.008**), indicating distinct underlying drivers (idiosyncratic supplier demand vs. sector-level macro rotation).
- **Portfolio Ensembles:**
  - 50/50 `supplier_pressure` + `metacluster`: **Sharpe 0.55** (vs. 0.52 for supplier pressure alone and 0.33 for metacluster alone).
  - Equal-weighted 4-family portfolio: **Sharpe 0.62** (in-sample exploratory, not OOS-validated).

#### 3. Hybrid Structural Matrix Sweep ($C^{hybrid} = \alpha C^{data} + (1-\alpha) C^{supply}$)

| Strategy Family | Hybrid $\alpha$ | Ann. Return | Ann. Vol | Sharpe Ratio | Max Drawdown |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `supplier_pressure` | $\alpha = 0.00$ (pure supply graph) | 11.45% | 22.47% | **0.51** (0.509641) | **-58.07%** |
| `supplier_pressure` | $\alpha = 0.25$ | 10.35% | 22.62% | **0.46** (0.457567) | -66.11% |
| `supplier_pressure` | $\alpha = 0.50$ | 7.52% | 22.06% | **0.34** (0.340869) | -76.17% |
| `supplier_pressure` | $\alpha = 0.75$ | 8.18% | 21.22% | **0.39** (0.385671) | -73.60% |
| `supplier_pressure` | $\alpha = 1.00$ (pure return data) | 11.14% | 21.38% | **0.52** (0.521166) | **-71.06%** |
| `globalrank` | $\alpha = 0.00$ | -2.64% | 21.37% | **-0.12** (-0.123328) | -69.84% |
| `globalrank` | $\alpha = 0.75$ | 8.33% | 19.72% | **0.42** (0.422398) | -44.08% |
| `globalrank` | $\alpha = 1.00$ | -6.75% | 16.87% | **-0.40** (-0.400271) | -82.33% |
| `metacluster` | $\alpha = 0.00$ | 14.99% | 54.41% | **0.28** (0.275460) | -98.12% |
| `metacluster` | $\alpha = 1.00$ | 9.71% | 50.97% | **0.19** (0.190465) | -98.88% |
| `clusterrank` | $\alpha = 0.75$ | 2.69% | 10.90% | **0.25** (0.246663) | -26.44% |
| `clusterrank` | $\alpha = 1.00$ | 2.37% | 13.24% | **0.18** (0.178922) | -38.43% |

*Key finding:* For `supplier_pressure`, pure structural supply links ($\alpha=0$) achieve almost identical Sharpe (**0.51** vs. **0.52**) with a significantly lower maximum drawdown (**-58.07%** vs. **-71.06%**), demonstrating that return-based estimation noise degrades tail risk without generating incremental Sharpe. For `globalrank`, hybrid blending ($\alpha=0.75$) rescues an otherwise failing strategy (-0.40 Sharpe $\to$ +0.42 Sharpe).

#### 4. Forward vs. Reverse Placebo Panel Regressions

- **Forward Customer $\to$ Supplier ($r_{supp}(t+h) \sim r_{cust}(t)$):**
  - Horizon $h=1$: $\beta = 0.041264, t = 7.907$ ($N=633,674$, 460 entities, pooled OLS).
  - Horizon $h=2$: $\beta = 0.038797, t = 7.435$ ($N=633,599$, 460 entities).
  - Horizon $h=3$: $\beta = -0.012025, t = -2.304$ (mean reversion).
  - Horizon $h=4$: $\beta = -0.004167, t = -0.798$.
  - Horizon $h=5$: $\beta = 0.000701, t = 0.134$.
- **Reverse Supplier $\to$ Customer Placebo ($r_{cust}(t+h) \sim r_{supp}(t)$):**
  - Horizon $h=1$: $\beta = 0.008175, t = 2.549$ ($N=633,563$, 460 entities).
  - Horizon $h=2$: $\beta = 0.008087, t = 2.521$ ($N=633,375$, 460 entities).
  - Horizon $h=5$: $\beta = -0.008932, t = -2.782$ ($N=632,809$, 460 entities).

### Independently reproduced

- `not independently reproduced`

### Negative evidence

1. **Failure of Reverse Placebo Under Pooled OLS:** The author explicitly flags that reverse predictability (supplier return predicting customer return) is statistically significant at $h=1$ ($t=2.55$) and $h=2$ ($t=2.52$). If information diffusion were strictly unidirectional ($Customer \to Supplier$), reverse horizons should be indistinguishable from zero. This demonstrates that pooled OLS is confounded by common industry and market shocks that simultaneously affect both customer and supplier.
2. **Catastrophic Tail Risk:** All strategy families suffer extreme drawdowns over the 15-year sample: -71.06% for supplier pressure, -56.75% for metacluster, -64.31% for globalrank, and -48.35% for clusterrank. The strategy experiences prolonged multi-year stagnation (e.g., 2015–2019) and acute liquidation during market crashes.
3. **Turnover & Cost Sensitivity Provenance Gap:** The reported baseline backtest assumes 0.0 bps transaction fees and 0.0 bps borrow costs. Because the `supplier_pressure` strategy rebalances 20% long and 20% short daily across hundreds of suppliers, daily turnover is substantial. If turnover is 20% daily (approx. 5,000% annualized), transaction costs of 5 to 10 bps per trade would completely eliminate the 11.14% annualized gross return, rendering the strategy unprofitable in practice.
4. **Structural Degradation in Complex Network Partitioning:** Direction-blind community clustering (`supply_community`, `symmetric_spectral`) frequently resulted in degenerate partitions with zero traded positions, while static GlobalRank failed completely ($\text{Sharpe} = 0.11$, and $\text{Sharpe} = -0.40$ under pure data).

---

## Falsification plan

### Test 1: Panel Fixed Effects & Clustered Standard Errors (Confounding Audit)

- **Test Specification:** Re-estimate panel regressions of $r_{supp}(t+h)$ on customer pressure with two-way fixed effects (firm fixed effects and trading-day time fixed effects) using `linearmodels.PanelOLS`, clustering standard errors by both firm entity and date.
- **Decision Rule:**
  - Forward Customer $\to$ Supplier $t$-statistic at $h=1$ must satisfy $t > 2.50$ (`research-defined falsification threshold`).
  - Reverse Supplier $\to$ Customer placebo $t$-statistic at $h=1$ and $h=2$ must collapse to $|t| < 1.65$ (`research-defined falsification threshold`).
- **Action upon Failure:** If the reverse placebo remains statistically significant ($|t| \ge 1.96$) after time and firm fixed effects, or if the forward coefficient collapses to $|t| < 1.96$, reject the customer-to-supplier information diffusion hypothesis as an artifact of common factor co-movement.

### Test 2: Net-of-Cost Hurdle & Turnover Drag Falsification

- **Test Specification:** Compute exact daily portfolio turnover $\tau_d = \frac{1}{2} \sum_i |w_{i, d} - w_{i, d-1}|$. Evaluate net Sharpe under realistic institutional frictions: 5 bps commission, 5 bps slippage, and 100 bps annualized borrow cost on short positions.
- **Decision Rule:** Net annualized Sharpe ratio must remain $\ge 0.30$ (`research-defined falsification threshold`), and net annualized return must remain positive ($\text{CAGR}_{net} > 0.0\%$, `research-defined falsification threshold`).
- **Action upon Failure:** If net Sharpe $< 0.0$, reject daily rebalanced customer pressure as an unexecutable theoretical anomaly; mandate migration to multi-day holding periods (3-day or 5-day TWAP) or execution only on large customer earnings shocks.

### Test 3: Network Topology Randomization (Permutation Placebo)

- **Test Specification:** Randomly rewire the 17,153 point-in-time supply-chain edges while preserving each node's in-degree and out-degree distribution (degree-preserving bipartite shuffle). Re-run the rolling 155-rebalance `supplier_pressure` backtest 500 times.
- **Decision Rule:** The true empirical Sharpe ratio (0.52) must exceed the 99th percentile of the randomized network distribution ($p < 0.01$, `research-defined falsification threshold`).
- **Action upon Failure:** If randomized supply networks generate comparable Sharpe ratios, falsify the economic link hypothesis; conclude that apparent performance is driven by generic cross-sectional size or volatility tilts.

### Test 4: Subperiod & Regime Stability Split

- **Test Specification:** Partition the 2010–2024 sample into two equal 7.5-year subperiods: Pre-modern (2010-01-04 to 2017-06-30) and Modern (2017-07-01 to 2024-12-31).
- **Decision Rule:** Both subperiods must exhibit positive gross Sharpe ($\text{Sharpe} \ge 0.25$, `research-defined falsification threshold`).
- **Action upon Failure:** If modern subperiod Sharpe drops below 0.10, classify the anomaly as decayed due to institutional algorithmic arbitrage.

---

## Crypto portability

- **Portability Status:** `unproven` (research interpretation).
- **Economic Disconnect:** The primary mechanism relies on mandatory legal disclosures of business customers under SEC Regulation S-K Item 101 (requiring public disclosure of customers representing $\ge 10\%$ of consolidated revenue). Decentralized crypto assets have no equivalent corporate customer disclosure framework.
- **Adapted Hypotheses for Crypto Ecosystems (`research-proposed`):**
  1. *Protocol Revenue & Layer-1 / Layer-2 Fee Diffusion:* Major decentralized applications (e.g., Uniswap, Aave) generate fee volume that directly pays gas/settlement fees to underlying base chains (Ethereum, Solana). A surge in application user volume or token return could lead underlying layer-1 token returns.
  2. *DeFi Liquidity & Lending Hubs:* Protocols sharing deep liquidity pools or lending markets (e.g., liquid staking tokens Lido/RocketPool and collateral platforms Maker/Ethena) exhibit structural flow interdependencies that could be modeled as a synthetic directed network.
  3. *On-Chain Token Transfer Directed Graphs:* Large transaction flows between smart contracts or entity clusters (e.g., market maker deposit addresses to DEX liquidity pools) could replace SEC revenue weights with verifiable on-chain volume weights.
- **Key Crypto Portability Risks:**
  - *24/7 Trading & Instantaneous Information Propagation:* Crypto markets trade continuously without overnight closes. Information diffusion between correlated tokens occurs within seconds or minutes via algorithmic arbitrageurs, eliminating the 1-day lag observed in slow equity filings.
  - *Perpetual Funding Carry:* Holding short positions in high-beta altcoin "suppliers" incurs severe funding rate penalties during bull regimes.
  - *Severe Fragmentation & Mark-Price Basis:* Crypto perpetuals across Binance, Bybit, and Hyperliquid exhibit exchange-specific basis dislocations that can invalidate network signals.

---

## Limitations

1. **Unmodeled Trading Costs (Major Provenance Gap):** The primary empirical results reported in `report/final_report.md` assume 0 bps commissions, 0 bps slippage, and 0 bps short borrow financing. Daily long-short rebalancing across hundreds of small/mid-cap suppliers creates high turnover that is highly susceptible to cost drag.
2. **Reverse Directional Spillover:** Significant reverse placebo statistics ($t \approx 2.5$) indicate that pooled OLS cannot rule out common industry or factor co-movement as a confounder.
3. **Severe Maximum Drawdown:** -71.06% drawdown in the primary `supplier_pressure` sleeve represents unacceptable capital impairment without overlay risk controls or volatility targeting.
4. **Episodic Meta-Flow Alpha:** The `metacluster` strategy exhibits extreme return concentration during the 2020–2022 macro cycle, followed by severe stagnation.
5. **Compustat SEC Filing Latency:** While the codebase correctly enforces `filing_date <= T`, annual customer disclosures occur with a 60- to 90-day lag post fiscal year-end, meaning network edges represent stale historical relationships.

---

## Implementation status

- `not-implemented` in our production or research engine.
- No NautilusTrader strategy, PyBroker experiment, paper trading, testnet, or live trading execution has been performed.

---

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves solely as normalized upstream quantitative research captured for ChatGPT Research Intake Review and Hermes Wiki Brain ingestion. It does not constitute authorization to trade or implement in live capital environments.

---

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04]]`
- `[[quant/equity-lead-lag-clustering-minirocket-dtw-rowsum-momentum-2026-09-02.md]]`
- `[[quant/commodity-futures-network-momentum-lead-lag-graph-learning-2026-09-02]]`

---

## Sources

1. **Primary Source Codebase & Empirical Report:**
   - Author: `nicjia`
   - Repository: `https://github.com/nicjia/supply-chain-lead-lag`
   - Immutable Commit: `1cd62fdf5e4100bab9605ec7eb808f38369b5b02`
   - Frozen Run Artifacts:
     - `results/final_research/report/final_report.md` (Empirical report covering 155 BME rebalances, 2010–2024, 3,774 trading days)
     - `results/final_research/config_used.yaml` (Run configuration)
     - `results/final_research/run_metadata.json` (Run metadata, commit `a1deef529fe2f98c5ba81457ac942759cb81a8a0`, executed May 25, 2026)
     - `docs/FRAMEWORK.md` (Research hypotheses RQ1–RQ7)
     - `docs/IMPLEMENTATION_SPEC.md` (Mathematical specification)
     - Core Modules: `supply_chain_leadlag/matrix.py`, `supply_chain_leadlag/backtest.py`, `supply_chain_leadlag/strategy_families.py`, `supply_chain_leadlag/metacluster_strategy.py`, `supply_chain_leadlag/clusterrank_strategy.py`, `supply_chain_leadlag/clustering_methods.py`.
