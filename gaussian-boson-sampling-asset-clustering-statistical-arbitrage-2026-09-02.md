---
schema: strategy-research-record-v1
title: "Gaussian Boson Sampling for Asset Clustering in Statistical Arbitrage Portfolios: Photonic Quantum Heuristics for Correlation Clustering"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - quantum-computing
  - gaussian-boson-sampling
  - correlation-clustering
  - mean-reversion
  - equities
  - portfolio-construction
status: research-only
confidence: medium
source_as_of: 2026-07-21
sources:
  - "Dayne Marcus Lopena, Daniel Buguks, Zhenghao Li, Ewan Mer, Shana H. Winston, Shang Yu, Mihai Cucuringu, Del Rajan, Philip Intallura, and Raj B. Patel, 'Gaussian Boson Sampling for Asset Clustering in Statistical Arbitrage Portfolios', arXiv:2607.19279v1 [quant-ph, q-fin.CP, q-fin.ST, q-fin.TR], July 21, 2026. DOI: 10.48550/arXiv.2607.19279. Stable URL: https://arxiv.org/abs/2607.19279. Full text: https://arxiv.org/html/2607.19279v1. Code and Data: https://doi.org/10.5281/zenodo.18890167"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gaussian Boson Sampling for Asset Clustering in Statistical Arbitrage Portfolios: Photonic Quantum Heuristics for Correlation Clustering

## Provenance

- **Primary Source:** Dayne Marcus Lopena, Daniel Buguks, Zhenghao Li, Ewan Mer, Shana H. Winston, Shang Yu, Mihai Cucuringu, Del Rajan, Philip Intallura, and Raj B. Patel, *"Gaussian Boson Sampling for Asset Clustering in Statistical Arbitrage Portfolios"*, arXiv preprint `arXiv:2607.19279v1 [quant-ph, q-fin.CP, q-fin.ST, q-fin.TR]`, submitted July 21, 2026.
- **Canonical DOI:** [10.48550/arXiv.2607.19279](https://doi.org/10.48550/arXiv.2607.19279)
- **Traceable Source URL:** `https://arxiv.org/abs/2607.19279` / HTML full text: `https://arxiv.org/html/2607.19279v1`
- **Replication Data and Code Repository:** [10.5281/zenodo.18890167](https://doi.org/10.5281/zenodo.18890167)
- **Institutional Context:** Academic collaboration including researchers affiliated with the University of Oxford, Imperial College London, Post-Quantum, and HSBC Bank Plc.

## Economic mechanism

### Source-reported

In classical statistical arbitrage (StatArb), assets are grouped based on historical co-movement, under the premise that price divergences among strongly correlated peers represent temporary dislocations that will mean-revert. Identifying optimal clusters from empirical correlation matrices is a Max-Agree Correlation Clustering Problem (MACCP), which is NP-hard. Classical spectral methods (e.g., Spectral clustering and SPONGE) rely on eigendecompositions constrained by $\mathcal{O}(N^3)$ computational scaling and require pre-specifying a fixed or heuristically estimated number of clusters $K$.

Gaussian Boson Sampling (GBS) is a photonic quantum computing paradigm wherein single-mode squeezed vacuum states pass through a linear interferometer of beamsplitters and phase shifters. The output photon detection statistics are governed by the hafnian (or Torontonian under threshold detection) of submatrices of the graph adjacency matrix. Because the hafnian enumerates weighted perfect matchings, GBS naturally exhibits an intrinsic probabilistic bias toward sampling dense subgraphs. When residual correlation matrices of stock returns are mapped to GBS-compatible non-negative adjacency matrices, GBS acts as a physical combinatorial heuristic that samples cohesive asset communities without requiring a pre-specified target cluster count $K$. The source authors introduce two quantum clustering algorithms—an adapted GBS Boost and a novel agglomerative GBS Roots—and hypothesize that sampling-derived community partitions isolate structural market idiosyncrasies more effectively than deterministic classical spectral methods, especially during turbulent, volatile market regimes.

### Research interpretation

The underlying alpha hypothesis is cross-sectional equity mean reversion within quantum-discovered dynamic correlation subgraphs:

1. **Topological Co-movement Filtering:** Stock returns share common market factor exposure. Once market beta is stripped via single-factor regression, residual return correlations reflect genuine idiosyncratic linkages (industry supply chains, business model overlaps, common institutional ownership).
2. **Dense Subgraph Partitioning as Arbitrage Enclosure:** If a cluster exhibits high intra-cluster correlation, idiosyncratic pricing shocks to individual members should revert toward the cluster cross-sectional mean. Traditional clustering forces rigid geometric or spectral partitions that often suffer from spectral noise and rigid cluster count assumptions. GBS organically extracts heavy-tailed dense communities, discovering flexible, transient correlation structures that classical eigendecomposition misses.
3. **Displacement as Loss Regularization:** In physical photonic devices with photon transmission loss $l_r$, uncompensated loss degrades sampling toward thermal noise. The authors demonstrate that injecting coherent light via Displaced GBS (DGBS) preserves the mean photon number $\bar{n}$, which acts as an implicit regularizer preventing over-clustering into trivial two-asset pairs while maintaining high diversification.

## Signal

The trading signal operates as a multi-step pipeline combining factor neutralization, quantum graph clustering, and cross-sectional mean reversion:

- **Formation Timestamp / Cadence:** Calculated at daily market close on a rolling basis. Operational window shifts forward by $l = 3$ trading days at each rebalance.
- **Factor Neutralization & Lookback:**
  - Market beta estimation window: 60 trading days ($w_{\text{beta}} = 60$).
  - For each stock $i$, compute daily return $R_{t,i} = \frac{P_{t,i} + D_{t,i}}{P_{t-1,i}} - 1$.
  - Estimate CAPM market beta $\beta_i = \frac{\text{Cov}(R_i, R_{\text{mkt}})}{\text{Var}(R_{\text{mkt}})}$.
  - Compute market residual returns (MRR): $R_{t,i}^{\text{res}} = R_{t,i} - \beta_i R_{\text{mkt},t}$.
  - Residual correlation lookback window: 5 trading days ($w = 5$) to construct the $N \times N$ correlation matrix $\mathcal{C}$ of residual returns.
- **Graph Adjacency Construction:**
  - Zero the diagonal: $\mathcal{A} = \mathcal{C} - \mathbf{I}_N$.
  - Apply threshold function dropping negative correlations: $\mathcal{A}_{ij} \mapsto \max(0, \mathcal{A}_{ij})$ to ensure non-negativity (preventing negative-correlation sampling bias in the hafnian while preserving density utility).
- **Quantum Graph Clustering (GBS Roots):**
  - Rescale adjacency matrix $\mathbf{B} = c \mathcal{A}$ via Takagi-Autonne decomposition $\mathbf{B} = \mathbf{U} \mathbf{\Lambda} \mathbf{U}^T$ with singular values $\lambda_k \in [0, 1)$ and squeezing parameters $r_k = \tanh^{-1}(c \lambda_k)$.
  - Set target mean photon number $\bar{n} = \sqrt{\dim(\mathcal{A})}$.
  - Draw batch of $H = \mathcal{O}(N \log N)$ threshold detection samples using Strawberry Fields / Walrus.
  - Calculate Weighted Density (WD) for each sample: $\text{WD}(\mathcal{C}) = \frac{\sum_{i,j \in \mathcal{C}} \mathcal{A}_{ij}}{|\mathcal{C}|(|\mathcal{C}| - 1)}$.
  - Initiate greedy multi-packing: Take sample $q_1$ with highest WD. Sequentially evaluate remaining samples $q_j$; if $q_j \cap \mathcal{U} = \emptyset$ and merging increases total WD, merge into disjoint union $\mathcal{U}$.
  - Form cluster $C = \mathcal{U}$, remove constituent nodes from graph $\mathcal{G} \setminus \mathcal{U}$, shrink $\mathcal{A}$, update $\bar{n}$, and repeat until graph cannot be further partitioned. No target cluster count $K$ is prescribed.
- **Signal Generation (Previous Winner / Previous Loser):**
  - Within each cluster $j$ containing $j_n$ stocks, calculate cluster mean return over the 5-day formation window: $\bar{R}_{t,j} = \frac{1}{j_n} \sum_{i=1}^{j_n} R_{t,i}$.
  - Compute stock deviation $\Delta_{t,j_i} = R_{t,j_i} - \bar{R}_{t,j}$.
  - Classification rule (threshold $p = 0$):
    - Previous Winner (PW): $\Delta_{t,j_i} > 0 \implies$ Short signal.
    - Previous Loser (PL): $\Delta_{t,j_i} < 0 \implies$ Long signal.
- **Position Sizing & Weighting:**
  - Zero-cost, dollar-neutral portfolio per cluster constrained to unit dollar capital ($1.00 long, $1.00 short).
  - Capital allocated uniformly across legs: if cluster has $m$ PWs and $n$ PLs, each short position receives weight $-1/m$ and each long position receives weight $+1/n$.
- **Exit & Rebalance Rules:**
  - Scheduled holding period: $l = 3$ trading days. Portfolio liquidated and rebalanced at day $t + 3$.
  - Early exit / Stop-win threshold: $q = 0.02$ (2.0% cumulative portfolio return). If cumulative portfolio return breaches $q = 0.02$ prior to the end of the 3-day holding period, early liquidation is triggered immediately, locking in profits and shifting the operational window forward by 3 days.

## Required data

- **Instruments:** U.S. large-cap equities (constituents of S&P 500 index).
- **Universe:** 100 S&P 500 stocks in the primary lossless benchmark, selected via stratified sampling across 11 GICS sectors (Energy, Materials, Industrials, Consumer Discretionary, Consumer Staples, Healthcare, Financials, Information Technology, Communication Services, Utilities, Real Estate) based on previous year's performance. Also evaluated on 12-, 20-, 30-, and 50-stock subsets in scaling studies.
- **Market Type:** Cash equity spot (long and short borrowing).
- **Timeframe:** Daily close prices and dividend distributions.
- **Fields:** Dividend-adjusted close prices ($P_{t,i}$, $D_{t,i}$), market benchmark return ($R_{\text{mkt},t}$ from Fama-French 3-factor market factor), Standard Industrial Classification (SIC) codes for sector mapping.
- **Data Vendors:** Wharton Research Data Services (WRDS), Center for Research in Security Prices (CRSP), Kenneth French Data Library.
- **Simulation Hardware / Software:** Strawberry Fields quantum simulation API (`sf.apps.sample.sample`), The Walrus library for Torontonian calculation.

## Execution assumptions

- **Order Timing:** Execution at market close (or next-open unmodeled) following signal calculation.
- **Order Types:** Market on close / limit at mid assumed.
- **Transaction Costs & Slippage:** **Zero transaction costs and zero price impact assumed in source backtests.** The paper explicitly states in Section IV: *"A key assumption, for simplicity, in our simulations is that the trades executed do not incur price impact and there are zero transaction costs."*
- **Short Borrow:** Unconstrained short selling assumed with zero borrow fees and perfect locate availability.
- **Rebalancing Frequency:** Every 3 trading days ($l = 3$), or earlier upon triggering the $q = 0.02$ stop-win threshold.

## Evidence

### Source-reported

All performance statistics below are reported directly from Lopena et al. (arXiv:2607.19279v1, July 2026), evaluated over the volatile one-year 2020 sample period for a 100-stock lossless universe ($l_r = 0$), comparing quantum heuristics against classical spectral benchmarks:

**Table 1: Financial Performance (Lossless 100-Stock Universe, Year 2020, ~20 runs for quantum methods, ~100 runs for classical methods):**
- **GBS Roots (Novel Quantum Heuristic):**
  - Total Return (TR): $0.236 \pm 0.031$ (23.6% annual return)
  - Annualized Sharpe Ratio (ShR): $2.248 \pm 0.293$
  - Sortino Ratio (SoR): $3.708 \pm 0.673$
- **GBS Boost (Adapted Quantum Heuristic):**
  - Total Return (TR): $0.239 \pm 0.035$ (23.9% annual return)
  - Annualized Sharpe Ratio (ShR): $2.050 \pm 0.190$
  - Sortino Ratio (SoR): $3.188 \pm 0.521$
- **SPONGE (Top Classical Benchmark):**
  - Total Return (TR): $0.214 \pm 0.064$ (21.4% annual return)
  - Annualized Sharpe Ratio (ShR): $2.242 \pm 0.669$
  - Sortino Ratio (SoR): $3.737 \pm 1.282$
- **Spectral Clustering (Classical Benchmark):**
  - Total Return (TR): $0.200 \pm 0.051$ (20.0% annual return)
  - Annualized Sharpe Ratio (ShR): $2.035 \pm 0.512$
  - Sortino Ratio (SoR): $3.389 \pm 0.931$
- **QIC-GBS (Quantum-Inspired Classical GBS Benchmark):**
  - Total Return (TR): $0.195 \pm 0.099$ (19.5% annual return)
  - Annualized Sharpe Ratio (ShR): $1.781 \pm 0.893$
  - Sortino Ratio (SoR): $3.089 \pm 1.696$

**Statistical Validation & Graph Metrics:**
- **Welch's Two-Tailed t-test:** GBS Roots exhibits a statistically significant advantage in total return over SPONGE at the 5% significance level ($p = 0.023$). Mean Sharpe ratios are statistically indistinguishable ($p = 0.949$), but GBS Roots achieves this risk-adjusted performance with less than half the cross-run standard deviation ($\pm 0.293$ vs. $\pm 0.669$), reflecting greater run-to-run consistency.
- **Table 2: Cluster Properties (Best Partition by Total Return):**
  - GBS Roots: Weighted Density (WD) = $0.199 \pm 0.118$, Jaccard similarity ($J$) = $0.163 \pm 0.024$, Cluster Value ($V$) = $3.945$.
  - GBS Boost: WD = $0.176 \pm 0.129$, $J = 0.164 \pm 0.029$, $V = 17.031$.
  - SPONGE: WD = $0.336 \pm 0.015$, $J = 0.321 \pm 0.042$, $V = 2.752$.
  - Spectral: WD = $0.111 \pm 0.023$, $J = 0.344 \pm 0.055$, $V = 2.756$.
  - QIC-GBS: WD = $0.262 \pm 0.173$, $J = 0.154 \pm 0.025$, $V = 8.151$.
- **Photon Loss & Displacement Results (50-Stock Universe):** Without displacement, GBS returns degrade below classical benchmarks at photon loss rates $l_r > 60\%$, approaching a random clustering baseline. Incorporating coherent displacement (DGBS) stabilizes detected photon counts and performance: at loss $l_r \le 40\%$, GBS methods outperform SPONGE in 85% of cases.
- **Regime Evaluation:** GBS methods delivered strong positive returns during high-volatility crashes (2008 and 2020), demonstrating positive correlation between quantum portfolio Sharpe and market VIX. Conversely, GBS methods underperformed in the low-volatility bull market of 2017, where mean-reversion dislocations were scarce.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Zero Transaction Costs:** The reported Sharpe ratios ($> 2.0$) and total returns ($\sim 23.6\%$) do not incorporate transaction costs, bid-ask spread, exchange fees, or short borrow fees. Because the portfolio rebalances every 3 days (approx. 84 rebalances per year), turnover is high. In practice, trading frictions on 100 equity names across 84 annual rebalances will substantially erode gross returns.
- **Degradation in Stable Regimes:** In low-volatility, unidirectional trending environments (such as 2017), GBS methods underperformed static equal-weighted benchmarks, as persistent trends break the zero-mean residual assumption.
- **Jaccard Instability:** GBS methods exhibit low inter-window Jaccard similarity ($J \approx 0.16$ vs. $J \approx 0.32\text{--}0.34$ for classical methods), indicating rapid turnover in cluster membership between consecutive 3-day windows.
- **Hardware Limitations:** Simulating threshold detection GBS on classical hardware scales exponentially with detected photons ($\mathcal{O}(N^3 2^N)$ for exact hafnian, constrained by bounding $\bar{n} = \sqrt{N}$), limiting practical universe size to $\le 100$ assets without physical photonic hardware.

## Falsification plan

1. **Transaction Cost & Slippage Haircut:** Re-simulate the 2020 backtest incorporating realistic institutional equity transaction costs (5 bps to 15 bps per trade, plus borrow fees on the short leg). If net Sharpe drops below 0.75 or net cumulative return falls below SPONGE/Spectral benchmarks, the economic superiority of quantum clustering over classical spectral methods is falsified.
2. **Ablation of GBS vs. Classical Greedy Clustering:** Benchmark GBS Roots against a purely classical greedy agglomerative algorithm that searches for maximal weighted density on the same thresholded adjacency matrix. If classical heuristic search matches or exceeds GBS Roots returns, the empirical quantum advantage is disconfirmed.
3. **Out-of-Sample Rolling Test (2021–2025):** Evaluate the GBS Roots strategy across multi-year out-of-sample data including the 2021 speculative bull market, the 2022 rate-hike bear market, and 2023–2024 tech-dominated rally. If the strategy suffers prolonged drawdowns ($> 25\%$) or negative annualized returns, the regime robustness claim is falsified.
4. **Permutation / Shuffled Adjacency Test:** Shuffle the stock labels in the correlation matrix before GBS sampling. If shuffled partitions yield returns within 1.0 standard error of un-shuffled GBS Roots, the signal is driven by random portfolio construction artifacts rather than genuine topological structure.
5. **Failure Threshold:** If net annualized Sharpe over a 5-year rolling window is $< 0.50$ after costs, the strategy is rejected for quantitative research progression.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Mechanism Mapping:** The core thesis—clustering co-moving assets via non-negative residual correlations and trading cross-sectional mean reversion—theoretically applies to crypto perpetual markets (e.g., top 50–100 altcoins vs. BTC/ETH market factor).
- **Crypto-Specific Obstacles:**
  - **Dominant Market Factor:** In crypto, the first principal component (Bitcoin beta) accounts for 70–85% of total variance (compared to 30–50% in equities). Stripping BTC/ETH beta leaves thin idiosyncratic residual variance, increasing correlation noise.
  - **Funding Rate Friction:** Holding short and long perpetual positions over multi-day horizons incurs 8-hour funding payments. Cluster imbalances where altcoins have high positive funding rates could wipe out mean-reversion profits.
  - **24/7 Continuous Trading:** Unlike equity daily sessions, crypto trades continuously; 3-day discrete windows may suffer from continuous intraday liquidation cascades and lead-lag dynamics.
  - **Survivorship & Listing Churn:** The altcoin universe experiences rapid token obsolescence, delistings, and illiquid order books, violating the stationary universe assumption.

## Limitations

- **Source Backtest Omits Friction:** Zero fees, zero slippage, and unconstrained borrow availability represent a critical provenance gap for real-world viability.
- **Quantum Hardware Dependency:** Current execution relied on classical simulation via the Strawberry Fields API (bounded to $\bar{n} = 10$). Scaling to 500+ assets requires physical photonic quantum processing units (QPUs), which currently suffer from high optical loss and phase drift.
- **Short Lookback Window:** A 5-day correlation lookback window ($w = 5$) is noisy and susceptible to high estimation variance, which may explain the low Jaccard similarity across windows.
- **Not Independently Reproduced:** All reported metrics are third-party empirical findings from Lopena et al. (arXiv:2607.19279v1).

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

## Adoption boundary

Research-only. This document represents a theoretical and computational research capture. It does not authorize capital deployment, paper trading, or live execution.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/cross-sectional-equity-statistical-arbitrage]]`

## Sources

- Dayne Marcus Lopena, Daniel Buguks, Zhenghao Li, Ewan Mer, Shana H. Winston, Shang Yu, Mihai Cucuringu, Del Rajan, Philip Intallura, and Raj B. Patel, *"Gaussian Boson Sampling for Asset Clustering in Statistical Arbitrage Portfolios"*, arXiv preprint `arXiv:2607.19279v1 [quant-ph, q-fin.CP, q-fin.ST, q-fin.TR]`, submitted July 21, 2026. DOI: [10.48550/arXiv.2607.19279](https://doi.org/10.48550/arXiv.2607.19279). URL: `https://arxiv.org/abs/2607.19279`.
- Replication Code & Data: Lopena, D. M., & Buguks, D. (2026). *Zenodo Archive*. DOI: [10.5281/zenodo.18890167](https://doi.org/10.5281/zenodo.18890167).
