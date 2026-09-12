---
schema: strategy-research-record-v1
title: "Market-Neutral Crypto Statistical Arbitrage via Signed Graph SPONGE Clustering on PCA-Residualized Returns: Turnover-Cost Falsification, Capital Insolvency, and Execution Controls"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - statistical-arbitrage
  - sponge-clustering
  - signed-graph
  - pca-residualization
  - mean-reversion
  - survivorship-bias
  - execution-costs
  - capital-accounting
status: research-only
confidence: high
source_as_of: 2026-09-10
sources:
  - "https://github.com/Aroesler1/Crypto-Stat-Arb/tree/b56cbcd40e6a72cc3c09444fc8bea3df11212c99"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Market-Neutral Crypto Statistical Arbitrage via Signed Graph SPONGE Clustering on PCA-Residualized Returns: Turnover-Cost Falsification, Capital Insolvency, and Execution Controls

## Provenance

- **Author / Research Repository:** `Aroesler1`, *Market-neutral crypto stat-arb research + backtest: build signed k-NN correlation graphs, remove market mode via PCA, cluster tokens (SPONGE/BNC/signed spectral), and trade mean-reversion signals in walk-forward OOS with cost/turnover controls* (`Aroesler1/Crypto-Stat-Arb`).
- **Repository URL:** [https://github.com/Aroesler1/Crypto-Stat-Arb](https://github.com/Aroesler1/Crypto-Stat-Arb)
- **Immutable Commit SHA:** `b56cbcd40e6a72cc3c09444fc8bea3df11212c99` (September 10, 2026).
- **Inspected Primary Source Files:**
  - Core findings & revision summary: [`README.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/README.md)
  - Walk-forward backtest report & phase results: [`stat_arb/reporting/FINAL_REPORT.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/FINAL_REPORT.md)
  - Capital accounting audit & insolvency findings: [`docs/accounting_audit.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/accounting_audit.md)
  - Historical perpetual listing & funding availability audit: [`docs/availability_review_2026.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/availability_review_2026.md)
  - Signed graph clustering literature & implementation review: [`docs/signed_clustering_2026.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/signed_clustering_2026.md)
  - Cluster deviation signal construction: [`stat_arb/signals/cluster_deviation.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/signals/cluster_deviation.py)
  - Z-score mean reversion signal construction: [`stat_arb/signals/zscore_strategy.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/signals/zscore_strategy.py)
  - Market mode PCA extraction & residualization: [`stat_arb/pca/market_mode.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/pca/market_mode.py)
  - SPONGE generalized eigenproblem algorithm: [`stat_arb/clustering/sponge.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/clustering/sponge.py)
  - Core backtest engine & execution rules: [`stat_arb/backtest/engine.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/backtest/engine.py)
  - Transaction cost modeling & sensitivity: [`stat_arb/backtest/costs.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/backtest/costs.py)
  - Turnover limits & band controls: [`stat_arb/portfolio/turnover.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/portfolio/turnover.py)
  - Grid results for execution experiments: [`stat_arb/reporting/phase3/execution_experiments.csv`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/phase3/execution_experiments.csv)
  - Multi-year bracket capital accounting summary: [`stat_arb/reporting/brackets/accounting_summary.csv`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/brackets/accounting_summary.csv)
- **Source As-Of Date:** 2026-09-10 (`b56cbcd40e6a72cc3c09444fc8bea3df11212c99`).
- **Data Universe & Sample Period:**
  - 10-year multi-bracket point-in-time universe: 2016-01-01 to 2025-06-30 (3,469 calendar days) reconstructed from CoinMarketCap historical snapshots, tracking survivorship and dead-token delistings across 4 ETH-relative market cap brackets ($B0$–$B3$).
  - Walk-forward out-of-sample execution window: 2024-05-30 to 2025-05-28 (365 calendar days).
- **Verification Integrity & Deduplication Audit:** All mathematical formulations, code modules, parameter thresholds, and empirical metrics were audited directly from the primary codebase. A full scan of `alpha-strategy-research` confirmed zero matching records for `Aroesler1` or `Crypto-Stat-Arb`. Adjacent statistical arbitrage records in the repository (`graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md` based on Korniejczuk et al. 2024, arXiv:2406.10695) evaluate S&P 500 US equities with an ML soft-voting ensemble, without addressing crypto token cross-sections, PCA market-mode residualization on ragged crypto panels, Point-in-Time CMC dead-token modeling, simple-capital accounting audits, or turnover-limiting execution bands.

## Economic mechanism

### Source-reported

Cryptocurrency prices exhibit high cross-sectional correlation driven by a dominant common market mode (Bitcoin and Ethereum macro beta, PC1). Classical statistical arbitrage applied to raw crypto prices suffers because apparent pair or cluster divergences are frequently artifacts of differential beta exposure rather than genuine idiosyncratic mispricing.

To isolate true relative-value mispricings:
1. **PCA Market-Mode Residualization:** The first principal component (PC1) is extracted via rolling PCA and subtracted from asset returns, yielding residual return series $x_{i,t}$ that reflect purely idiosyncratic movements orthogonal to market beta.
2. **Signed Graph Topology:** Unlike equities where sector boundaries are formal and static, crypto sub-sectors (e.g., Layer 1s, DeFi, AI tokens, meme coins) are fluid and time-varying. Furthermore, tokens exhibit both co-movement (positive edges) and substitution/competition dynamics (negative edges). Constructing a signed k-nearest-neighbor ($k$-NN) correlation graph preserves both edge signs.
3. **SPONGE Generalized Eigenproblem Clustering:** The Signed Positive Over Negative Generalized Eigenproblem (SPONGE; Cucuringu et al., AISTATS 2019) partitions the signed graph by minimizing negative edges within clusters while simultaneously minimizing positive edges between clusters via the generalized Laplacian pencil $(L^+ + \tau^- D^-) v = \lambda (L^- + \tau^+ D^+) v$. This identifies cohesive latent peer groups without imposing rigid manual categorizations.
4. **Within-Cluster Mean Reversion:** Assets within a SPONGE cluster share structural economic linkages. When an individual token's cumulative return temporarily diverges from its peer cluster composite return, liquidity rebalancing and arbitrage pressure drive the spread back toward zero.
5. **Execution Cost Falsification & Friction Controls:** Under daily rebalancing, within-cluster mean-reversion alpha is entirely consumed by taker fees (50 bps) and high turnover (15%–23%/day). However, because cluster mean-reversion signals decay over multi-day horizons, introducing a 2% no-trade band and extending the rebalancing interval to 3 days reduces turnover by $2.8\times$ (from 15.0% to 5.3%/day) while preserving ~97% of gross Sharpe.
6. **Capital Accounting & Survivorship Falsification:** Historical stat-arb studies frequently multiply portfolio weights by log returns, generating an arithmetic artifact where a short position in a token collapsing 99% yields a fictitious score of $+4.605$ instead of $+0.99$. When re-evaluated with a strict capital accounting ledger that enforces nonpositive equity stops on a point-in-time universe with dead tokens, small-cap crypto stat-arb is proven completely insolvent due to illiquid quote spikes and market crashes.

### Research interpretation

This repository provides an institutional-grade falsification and execution reality check on crypto statistical arbitrage. It establishes five structural insights:
- **Gross Alpha vs. Net Dissipation:** Co-movement and mean reversion within signed graph clusters exist strongly in gross terms (gross Sharpe ratios of 2.7–4.2 across all 16 walk-forward configurations), but naive daily rebalancing converts gross edge into deep net losses under realistic exchange taker fees.
- **Turnover Management as Alpha Prerequisite:** Statistical arbitrage alpha in crypto cannot be harvested through high-frequency turnover; it requires execution dampening (no-trade tolerance bands and multi-day rebalance cadences) to prevent cost drag from exceeding signal decay.
- **The Log-Score Arithmetic Trap:** Log-return backtests in long/short stat-arb are fundamentally invalid. Symmetrical log returns treat a $+100\%$ move ($+0.693$) and a $-50\%$ move ($-0.693$) identically, severely flattering short legs and hiding real-world margin liquidation.
- **Survivorship Bias Mirage:** Testing stat arb on surviving token snapshots produces high backtest returns that vanish when point-in-time dead tokens are included.
- **Cross-Sectional Thinness:** Large-cap crypto tokens ($B1$, 1%–10% of ETH) rarely contain enough simultaneous constituents (averaging only 23.9 tokens, clearing the 30-token clustering floor in only 20 of 114 months) to support robust statistical clustering.

## Signal

The deterministic trading signal pipeline is specified in `stat_arb/pca/market_mode.py`, `stat_arb/clustering/sponge.py`, `stat_arb/signals/cluster_deviation.py`, and `stat_arb/portfolio/turnover.py`:

- **Signal Formation & Causal Timing Discipline (`source-reported`):**
  - All signals are formed using data strictly through day $t-1$.
  - Decisions are executed at day $t$ close (or day $t+1$ open).
  - Positions held going into day $t+1$ earn returns at $t+1$.
- **Step 1: Rolling PCA Market-Mode Residualization (`source-reported`):**
  - Standardized returns over a rolling 365-day training window ($X_{t-365:t-1}$, minimum 180 periods) are decomposed via PCA:
    $$X = U \Sigma V^T$$
  - The first principal component (PC1 loading $v_1$) represents the crypto market mode.
  - Residual returns $x_{i,t}$ are computed out-of-sample by projecting day $t-1$ returns onto the orthogonal complement:
    $$x_{t-1} = X_{t-1} - (X_{t-1} v_1) v_1^T$$
  - PCA fit handles ragged panels by dropping only all-NaN rows and zero-filling staggered listing gaps (`source-reported`).
- **Step 2: Signed k-NN Correlation Graph Construction (`source-reported`):**
  - Pairwise Pearson correlation matrix $C$ is computed over rolling 60 days of residual returns.
  - Symmetrized $k$-nearest-neighbor graph ($k=10$ edges per node) is constructed:
    $$A_{ij} = \frac{1}{2} (C_{ij} \cdot \mathbb{I}_{\{j \in \text{kNN}(i)\}} + C_{ji} \cdot \mathbb{I}_{\{i \in \text{kNN}(j)\}}), \quad A_{ii} = 0$$
  - Retained edge weights preserve continuous signed correlation values $A_{ij} \in [-1, +1]$.
- **Step 3: SPONGE Graph Clustering (`source-reported`):**
  - Split signed adjacency into positive and negative layers:
    $$A^+ = \max(0, A), \quad A^- = \max(0, -A)$$
  - Degree matrices: $D^+ = \text{diag}(A^+ \mathbf{1})$, $D^- = \text{diag}(A^- \mathbf{1})$.
  - Laplacians: $L^+ = D^+ - A^+$, $L^- = D^- - A^-$.
  - Regularized SPONGE matrices:
    $$M_1 = L^+ + \tau^- D^-, \quad M_2 = L^- + \tau^+ D^+ + 10^{-6} I$$
    with regularizers $\tau^+ = \tau^- = 1.0$.
  - Solve generalized eigenproblem $M_1 v = \lambda M_2 v$ for the smallest $k$ generalized eigenvalues.
  - Form row-normalized spectral embedding $U \in \mathbb{R}^{n \times k}$ and apply $k$-means clustering (with fixed seed `random_state=42`, $n_{\text{init}}=10$) to partition assets into $k=3$ clusters.
- **Step 4: Cluster Deviation Z-Score Signal (`source-reported`):**
  - For each cluster $c \in \{1, \dots, k\}$, compute the composite return:
    $$R_{c, t-1} = \frac{1}{|c|} \sum_{i \in c} r_{i, t-1}$$
  - Compute each token's deviation from its cluster composite:
    $$d_{i, t-1} = r_{i, t-1} - R_{c, t-1}$$
  - Compute rolling 20-day cumulative deviation:
    $$S_{i, t-1} = \sum_{j=0}^{19} d_{i, t-1-j}$$
  - Standardize into a rolling 60-day z-score ($L=60$, minimum 20 days):
    $$z_{i, t-1} = \frac{S_{i, t-1} - \text{mean}_{60}(S_i)}{\text{std}_{60}(S_i) + 10^{-8}}$$
- **Step 5: Target Weight Generation & Neutralization (`source-reported`):**
  - Entry thresholds:
    - Long entry trigger: $z_{i, t-1} < -2.0$ (token has underperformed cluster composite).
    - Short entry trigger: $z_{i, t-1} > +2.0$ (token has outperformed cluster composite).
  - Un-normalized weights:
    $$w_i = \begin{cases} +1.0 / n_{\text{long}}, & z_{i, t-1} < -2.0 \\ -1.0 / n_{\text{short}}, & z_{i, t-1} > +2.0 \\ 0.0, & \text{otherwise} \end{cases}$$
  - **Cluster Neutralization (`source-reported`):** De-mean weights within each cluster across traded tokens only ($w_i \leftarrow w_i - \bar{w}_{\text{cluster}}$). Untraded names remain strictly zero.
  - **Dollar Neutralization (`source-reported`):** De-mean across all traded tokens in the portfolio ($w_i \leftarrow w_i - \bar{w}_{\text{portfolio}}$) to enforce $\sum w_i = 0$.
- **Step 6: Cost-Aware Turnover & Rebalancing Controls (`source-reported`):**
  - **No-Trade Band:** $w_{\text{band}} = 0.02$ (2%). If $|w_{i, \text{target}} - w_{i, \text{prev}}| < 0.02$, retain previous holding $w_{i, \text{prev}}$.
  - **Trade Cadence:** Rebalance executed only every $3\text{rd}$ day; holdings drift passively with price changes on non-rebalance days.
  - **Daily Turnover Cap:** Aggregate two-sided weight turnover $\sum |w_{i, t} - w_{i, t-1}|$ is capped at $15\%$/day (`source-reported`).

## Required data

- **Instrument & Reference Asset (`source-reported`):**
  - Altcoin tokens traded on centralized spot and perpetual exchanges.
  - Ethereum (ETH) is used as the numeraire/reference asset for market-cap bracket partitioning and excess returns. ETH is never traded in the stat-arb portfolio.
- **Market-Cap Brackets (`source-reported`):**
  - Partitioned monthly by market cap ratio relative to ETH ($r = \text{mcap} / \text{mcap}_{\text{ETH}}$):
    - **$B0$ (Mega):** $r \ge 10\%$ (avg 4.6 members; unclusterable, $<30$ tokens).
    - **$B1$ (Large):** $1\% \le r < 10\%$ (avg 23.9 members; clears 30 members on only 20 of 114 months).
    - **$B2$ (Mid):** $0.1\% \le r < 1\%$ (avg 122.8 members; 114/114 months clusterable).
    - **$B3$ (Small):** $0.01\% \le r < 0.1\%$ (avg 387.6 members; 114/114 months clusterable).
  - Minimum clusterable universe threshold: 30 tokens.
- **Asset Exclusions (`source-reported`):**
  - Stablecoins, wrapped, staked, and bridged tokens are excluded (316 CoinMarketCap IDs).
  - Micro-caps below $0.01\%$ of ETH are excluded due to decimal rounding artifacts.
- **Timeframe & Fields (`source-reported`):** Daily close prices, daily volume, market cap, and funding rates.
- **Sample Periods (`source-reported`):**
  - Full Point-in-Time Panel: 2016-01-01 to 2025-06-30 (10 calendar years, 3,469 days).
  - Phase 1–3 Walk-Forward OOS Window: 2024-05-30 to 2025-05-28 (365 days).
- **Point-in-Time Discipline (`source-reported`):** Point-in-time monthly CoinMarketCap ranks, preserving delisted and dead tokens.
- **Missing Data Handling (`research-proposed`):** Drop rows where all tokens are missing; zero-fill ragged panel gaps during PCA training; freeze holdings if a single token's price is missing on non-rebalance days.

## Execution assumptions

- **Execution Timing (`source-reported`):** Rebalancing executed at daily close ($t-1$ close data generates $t$ close execution; position earns $t+1$ return).
- **Transaction Costs (`source-reported`):**
  - Modeled across parameter grid: $10, 25, 50, 100, 200\text{ bps}$ per side.
  - Standard baseline: $50\text{ bps}$ per side ($100\text{ bps}$ round-trip taker fee).
  - VIP taker tier: $25\text{ bps}$ per side ($50\text{ bps}$ round-trip).
- **Turnover Limits (`source-reported`):**
  - Phase 3 optimal configuration: $2\%$ no-trade weight band, $3$-day rebalance cadence, resulting in realized turnover of $5.32\%$/day.
- **Capital Accounting & Solvency Model (`source-reported`):**
  - Tracks discrete cash, dollar holdings, executed trades, and deducted fees.
  - Longs and leveraged shorts drift with simple price returns.
  - Portfolio stops trading immediately upon terminal equity $\le 0$ (insolvency). No loss clipping, synthetic resets, or capital injections are permitted.
- **Financing & Borrow Carry (`source-reported`):**
  - Uniform daily carry knob (`carry_bps_daily`) tested in backtest engine.
  - Empirical Binance USD-M funding rate panel merged to evaluate perpetual short funding payments.
- **Market Liquidity Filter (`source-reported`):** Minimum daily trading volume floor of $\$50,000$/day per token.

## Evidence

### Source-reported

All figures trace directly to `stat_arb/reporting/FINAL_REPORT.md`, `stat_arb/reporting/phase3/execution_experiments.csv`, and `stat_arb/reporting/brackets/accounting_summary.csv` in `Aroesler1/Crypto-Stat-Arb` (commit `b56cbcd40e6a72cc3c09444fc8bea3df11212c99`):

#### 1. Phase 3 Cost-Aware Execution Grid (Walk-Forward OOS, 2024-05-30 to 2025-05-28)
Evaluated on SPONGE $k=3$ Cluster Deviation strategy across no-trade bands and rebalancing frequencies:

| Weight Band | Rebalance Freq | Gross Sharpe | Net Sharpe @ 25 bps | Net Sharpe @ 50 bps | Daily Turnover | Break-Even Fee | DSR (12-trial pool) |
|---|---|---:|---:|---:|---:|---:|---:|
| **2% (0.02)** | **3 days** | **2.9628** | **2.6328** | **2.3019** | **5.32%** | **225.1 bps** | **0.9553** |
| 0% (none) | 3 days | 2.9874 | 2.4364 | 1.8827 | 5.32% | 135.3 bps | 0.9036 |
| 5% (0.05) | 3 days | 2.2011 | 1.9771 | 1.7532 | 5.22% | 247.6 bps | 0.8668 |
| 0% (none) | 5 days | 2.4834 | 2.0991 | 1.7112 | 3.17% | 160.6 bps | 0.8606 |
| 0% (none) | 2 days | 2.9703 | 2.3342 | 1.6935 | 7.46% | 115.7 bps | 0.8573 |
| 2% (0.02) | 1 day | 2.9996 | 2.3025 | 1.6054 | 14.96% | 107.9 bps | 0.8321 |
| 5% (0.05) | 5 days | 1.7375 | 1.5831 | 1.4282 | 3.07% | 279.8 bps | 0.7828 |
| 5% (0.05) | 1 day | 2.2680 | 1.8389 | 1.4097 | 14.81% | 132.3 bps | 0.7787 |
| 2% (0.02) | 2 days | 2.1396 | 1.7501 | 1.3589 | 7.44% | 136.2 bps | 0.7596 |
| 2% (0.02) | 5 days | 1.8074 | 1.5724 | 1.3360 | 3.15% | 190.9 bps | 0.7561 |
| 0% (none) | 1 day (baseline) | 3.0572 | 2.0275 | 0.9978 | 14.96% | 74.7 bps | 0.6387 |
| 5% (0.05) | 2 days | 1.4053 | 1.1304 | 0.8549 | 7.30% | 127.4 bps | 0.5819 |

#### 2. Phase 1 & 2 Daily Rebalancing Breakdown
- **Phase 1 Baseline (SPONGE $k=3$, Z-Score MR, $H=5, L=60$):**
  - Gross Sharpe: **1.67**
  - Net Sharpe @ 50 bps: **-2.16**
  - Break-even cost: **21.0 bps**
  - Probabilistic Sharpe Ratio (PSR): **0.02** | Deflated Sharpe Ratio (DSR): **0.00**
  - Average daily turnover: **23%** | Max drawdown: **-27.7%**
- **Phase 2 Sweep (16 configurations):**
  - Best gross config (SPONGE $k=6$, Z-Score): Gross Sharpe **4.22**, Net Sharpe @ 50 bps **-1.21**, DSR **0.00**.
  - Best net config (Cluster Deviation, SPONGE $k=3$): Gross Sharpe **3.10**, Net Sharpe @ 50 bps **0.01**, Break-even **50.3 bps**, DSR **0.09** (indistinguishable from noise among 16 trials).

#### 3. 10-Year Multi-Bracket Capital Accounting & Insolvency Audit (2016–2025, 3,288 Days)
Evaluated with simple capital ledger tracking cash and holdings at 50 bps taker costs:

| Bracket | Arm | Historical Log-Score Sharpe | Corrected Net Sharpe @ 50 bps | Missing-Return Exposure Share | Status / Failure Date | Terminal Equity |
|---|---|---:|---:|---:|---|---:|
| $B1$ Large | baseline | +0.3952 | **+0.0781** | 0.0118% | Completed 3,288 days | Positive |
| $B1$ Large | EWMA | -0.0324 | **+0.4277** | 0.0000% | Completed 3,288 days | Positive |
| $B2$ Mid | baseline | -0.2379 | **+0.5389** | 4.8271% | Completed 3,288 days | Positive |
| $B2$ Mid | EWMA | +0.4358 | **-0.2320** | 2.1964% | Completed 3,288 days | Positive |
| $B3$ Small | baseline | -0.4234 | **Insolvent** | N/A | **Failed 2017-12-08** (Virtacoin spike) | **-0.0447** |
| $B3$ Small | EWMA | +1.4524 | **Insolvent** | N/A | **Failed 2020-03-14** (COVID crash) | **-0.4937** |

#### 4. Historical Perpetual Contract Availability Audit (10-Year Screen)
- Statically matched $B3$ member-days: **363,090**.
- Member-days passing dated prior-day funding identity screen: **105,193 (28.9716%)**.
- Average membership drops from 104.67 to 30.32 supported tokens.
- Zero altcoin perpetual funding support existed in the 2016–2019 sample window.

### Independently reproduced

Not independently reproduced. All metrics represent third-party empirical findings directly verified from the code and data outputs of `Aroesler1/Crypto-Stat-Arb`. No independent simulation in our internal execution engine has been performed.

### Negative evidence

The primary repository explicitly details and proves multiple fundamental failure modes:
1. **Turnover Dissipation under Daily Rebalancing:** In the Phase 2 walk-forward test, all 16 configurations generated strong gross Sharpe (1.5 to 4.22), but zero configurations survived 50 bps taker fees under daily rebalancing (DSR $\le 0.09$).
2. **The Log-Score Arithmetic Illusion:** A short position on a collapsing token yields an unconstrained positive log return ($\ln(1/0.01) = +4.605$), whereas real cash equity gain is capped at $+0.99$. Conversely, an illiquid quote spike destroys short capital. In the $B3$ small-cap bracket, the historical +1.452 log-score Sharpe masked total insolvency (equity $-0.494$).
3. **Virtacoin Single-Quote Bankruptcy:** On 2017-12-08, a single illiquid micro-cap (Virtacoin, VTA) rose from $\$0.000002$ to $\$0.000065$ on under $\$900$ of daily volume, instantly wiping out the entire $B3$ baseline book.
4. **COVID-19 Drawdown Contagion:** On 2020-03-12 to 2020-03-14, cross-sectional correlation collapsed into a single macro plunge (median token down ~38% in a day), rendering the $B3$ EWMA book insolvent.
5. **Perpetual Data Unavailability Pre-2020:** Over 71% of historical altcoin member-days lack dated perpetual derivatives support, invalidating multi-year historical backtests that assume perpetual short availability before 2020.

## Falsification plan

- **Test 1: Turnover Cost Dissipation Gate (`research-defined falsification threshold`):**
  - *Data & Protocol:* Evaluate the SPONGE $k=3$ Cluster Deviation strategy across out-of-sample forward slices with exchange fees shifted from 25 bps to 50 bps and 75 bps.
  - *Metric & Threshold:* If net annualized Sharpe ratio drops below $0.50$ under 50 bps taker fees when using the 2% no-trade band and 3-day rebalancing cadence, reject the claim that multi-day execution dampening rescues crypto stat-arb from fee drag.
- **Test 2: Point-in-Time Dead Token & Delisting Stress Test (`research-defined falsification threshold`):**
  - *Data & Protocol:* Evaluate the strategy on a point-in-time universe containing all historical delistings and dead tokens without look-ahead filtering.
  - *Metric & Threshold:* If account equity breaches zero (insolvency) or drawdowns exceed $-35\%$ due to single-name illiquid quote spikes, reject the investability of altcoin statistical arbitrage.
- **Test 3: Synthetic Random Cluster Placebo Test (`research-defined falsification threshold`):**
  - *Data & Protocol:* Replace the SPONGE signed graph clustering step with 500 randomized cluster assignments (holding cluster size distributions and rebalancing cadence identical).
  - *Metric & Threshold:* If the SPONGE clustering portfolio does not outperform the 95th percentile of randomized cluster portfolios ($p > 0.05$ on net Sharpe), falsify the hypothesis that signed Laplacian topology provides genuine structural grouping alpha over random partitioning.
- **Test 4: Perpetual Funding Drag Wedge Test (`research-defined falsification threshold`):**
  - *Data & Protocol:* Merge tick-by-tick or 8-hour actual historical funding rate settlements for every short leg in the portfolio.
  - *Metric & Threshold:* If net cumulative PnL drops by more than $5.0\%$ annualized due to negative funding carry (paying funding on short positions during speculative bull regimes), reject the market-neutral funding viability hypothesis.

## Crypto portability

- **Portability Status (`source-reported`):** Direct.
- **Native Domain:** The strategy, data pipeline, and empirical falsification experiments were conceived and conducted natively on cryptocurrency token panels (spot CoinMarketCap archives and Binance USD-M perpetual futures).
- **Spot vs. Perpetual Dynamics:** The strategy requires symmetric shorting. In spot markets, borrowing altcoins is constrained by centralized lending desks, high borrow fees (often 20%–100% APR), and recall risk. On perpetual futures, shorting is synthetically embedded, but funding rates fluctuate dynamically and can impose severe cash-flow drags during market rallies.
- **24/7 Session Partitioning:** Continuous trading means daily candle boundaries (00:00 UTC) are arbitrary; intrabar volatility spikes can trigger liquidation before daily close rebalancing occurs.
- **Exchange Fragmentation:** Cross-venue liquidity fragmentation means a token may show apparent statistical mispricing on one exchange while trading at fair value on another; executing across fragmented order books introduces adverse execution slippage.

## Limitations

- **Small-Cap Insolvency Risk (`source-reported`):** Lower-tier altcoin brackets ($B3$, $<0.1\%$ ETH market cap) are fundamentally uninvestable due to micro-volume price manipulation and delisting risk.
- **Short Common OOS Window (`source-reported`):** The Phase 3 execution experiments (showing Net Sharpe 2.30) were evaluated on a 1-year out-of-sample window (2024-05-30 to 2025-05-28). While DSR (0.955) adjusts for the 12-cell parameter grid, it does not compensate for single-regime macroeconomic market conditions.
- **Large-Cap Cluster Starvation (`source-reported`):** The $B1$ bracket rarely contains $\ge 30$ tokens, meaning the most liquid, shortable altcoins cannot be reliably partitioned into statistical clusters.
- **Missing Historical Derivatives (`source-reported`):** Pre-2020 historical backtests cannot be executed on perpetual futures because the derivatives infrastructure did not exist for most altcoins.
- **Execution Assumption Simplification:** Backtest assumes immediate fills at daily close without modeling market depth impact for portfolio capital exceeding $\$100,000$.

## Implementation status

- `not-implemented`: No implementation of the SPONGE signed Laplacian solver, PCA market-mode residualizer, cluster deviation state machine, or no-trade band portfolio controller exists in `alpha-strategy-research`, `nautilus-quant-system`, PyBroker, or NautilusTrader.
- This record serves strictly as an auditable, normalized research capture and empirical falsification reference.

## Adoption boundary

- `research-only`: Capturing this research does not authorize trading or system implementation.
- `not-approved`: Not approved for live trading, testnet deployment, or paper trading.
- Research capture does not imply that statistical arbitrage alpha is investable; the primary evidence demonstrates severe structural hurdles (turnover dissipation, small-cap insolvency, and survivorship bias).

## Related Wiki records

- `crypto-cross-sectional-stat-arb-funding-binding-cost-negative-2026-09-09.md`: Cross-sectional crypto perpetual stat arb proving funding rate is the binding cost that eliminates alpha.
- `graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md`: SPONGE signed graph clustering on US equities (S&P 500) with ML ensemble quality filtering.
- `crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12.md`: Empirical falsification of retail crypto patterns via driftless random walk controls.
- `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md`: Multi-venue crypto funding carry turnover dissipation under realistic trading costs.
- `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md`: Classical Johansen and Ornstein-Uhlenbeck statistical arbitrage ablation and multiple testing.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`: Core Hermes Wiki Brain methodology on causal validation, purging, and embargoing.

## Sources

1. **Primary Source Code Repository:**
   - Author: `Aroesler1`
   - Repository: `https://github.com/Aroesler1/Crypto-Stat-Arb`
   - Commit: `b56cbcd40e6a72cc3c09444fc8bea3df11212c99`
   - Date: 2026-09-10
   - Primary Paths:
     - `README.md`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/README.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/README.md)
     - `stat_arb/reporting/FINAL_REPORT.md`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/FINAL_REPORT.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/FINAL_REPORT.md)
     - `docs/accounting_audit.md`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/accounting_audit.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/accounting_audit.md)
     - `docs/availability_review_2026.md`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/availability_review_2026.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/availability_review_2026.md)
     - `docs/signed_clustering_2026.md`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/signed_clustering_2026.md`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/docs/signed_clustering_2026.md)
     - `stat_arb/signals/cluster_deviation.py`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/signals/cluster_deviation.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/signals/cluster_deviation.py)
     - `stat_arb/pca/market_mode.py`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/pca/market_mode.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/pca/market_mode.py)
     - `stat_arb/clustering/sponge.py`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/clustering/sponge.py`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/clustering/sponge.py)
     - `stat_arb/reporting/phase3/execution_experiments.csv`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/phase3/execution_experiments.csv`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/phase3/execution_experiments.csv)
     - `stat_arb/reporting/brackets/accounting_summary.csv`: [`https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/brackets/accounting_summary.csv`](https://github.com/Aroesler1/Crypto-Stat-Arb/blob/b56cbcd40e6a72cc3c09444fc8bea3df11212c99/stat_arb/reporting/brackets/accounting_summary.csv)
2. **Foundational Methodological Literature:**
   - Mihai Cucuringu, Peter Davies, Aldo Glielmo, and Hemant Tyagi. "SPONGE: A Generalized Eigenproblem for Clustering Signed Networks." In *Proceedings of the 22nd International Conference on Artificial Intelligence and Statistics (AISTATS 2019)*, PMLR 89:1088–1098. arXiv preprint `arXiv:1904.08575`.
   - David H. Bailey and Marcos López de Prado. "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality." *Journal of Portfolio Management* 40, no. 5 (2014): 94–107. DOI: [10.3905/jpm.2014.40.5.094](https://doi.org/10.3905/jpm.2014.40.5.094).
   - Marco Avellaneda and Jeong-Hyun Lee. "Statistical arbitrage in the US equities market." *Quantitative Finance* 10, no. 7 (2010): 761–782. DOI: [10.1080/14697680903124632](https://doi.org/10.1080/14697680903124632).
