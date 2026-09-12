---
schema: strategy-research-record-v1
title: "AEGIS: Momentum-Gated Hierarchical Volatility-Adjusted Anchor Triad and Recursive Minimax Immunization with Convex Sortino Allocation"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-momentum
  - hierarchical-portfolio-optimization
  - minimax-correlation
  - sortino-optimization
  - tail-risk-immunization
  - equity
status: research-only
confidence: medium
source_as_of: 2026-04-10
sources:
  - "Arya Chakraborty and Randhir Singh, 'Taming the Black Swan: A Momentum-Gated Hierarchical Optimisation Framework for Asymmetric Alpha Generation', arXiv:2604.09060v2 [q-fin.PM], submitted April 10, 2026. DOI: 10.48550/arXiv.2604.09060. https://arxiv.org/abs/2604.09060"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AEGIS: Momentum-Gated Hierarchical Volatility-Adjusted Anchor Triad and Recursive Minimax Immunization with Convex Sortino Allocation

## Provenance

- **Authors:** Arya Chakraborty (Department of Computer Science) and Dr. Randhir Singh (Department of Mathematics), Birla Institute of Technology Mesra, Ranchi, India (`btech10196.23@bitmesra.ac.in`, `aryachakraborty2005@gmail.com`, `randhir.math@gmail.com`).
- **Title:** "Taming the Black Swan: A Momentum-Gated Hierarchical Optimisation Framework for Asymmetric Alpha Generation"
- **Primary Source:** arXiv preprint `arXiv:2604.09060v2 [q-fin.PM]`, submitted April 10, 2026 (v1 submitted April 2026), 18 pages.
- **Canonical DOI:** [10.48550/arXiv.2604.09060](https://doi.org/10.48550/arXiv.2604.09060).
- **Stable URLs:** Abstract: https://arxiv.org/abs/2604.09060; Full text PDF: https://arxiv.org/pdf/2604.09060.pdf.
- **Underlying Code / Data Artifacts:** No public code repository was published by the authors; the complete mathematical formulation and algorithmic architecture are fully detailed in Algorithms 1, 2, and 3 in the paper.
- **Repository Deduplication Audit:** An exhaustive audit across all existing markdown strategy records in `alpha-strategy-research` confirmed zero pre-existing records citing `arXiv:2604.09060`, Arya Chakraborty, Randhir Singh, the AEGIS system, or recursive minimax correlation immunization. Related equity momentum records in the repository (e.g. `size-enhanced-left-side-momentum-resga-expected-shortfall-2026-09-04.md` and `graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05.md`) investigate genetic algorithms with expected shortfall or maximum weight matching for pairs; none formulate a hierarchical sector-VAM anchor triad coupled with recursive minimax pairwise correlation filtering and SLSQP Sortino optimization.

## Economic mechanism

### Source-reported

Traditional cross-sectional momentum (CSM) strategies suffer from the "Winner's Curse" and severe left-tail momentum crashes during abrupt macroeconomic regime shifts. Because conventional CSM ranks assets solely on raw historical price appreciation, it systematically over-allocates to volatile, high-beta assets at the peak of a market cycle. When liquidity shocks occur (such as the 2008 Global Financial Crisis), these crowded winners suffer catastrophic drawdowns (e.g., standard CSM lost -42.58% in 2008). Conversely, static risk parity strategies rely on historical inverse correlations (such as equities versus bonds), which collapse during inflationary macroeconomic tightening cycles (such as 2022, when stocks and bonds fell simultaneously, resulting in a -26.72% loss for risk parity).

The Adaptive Equity Generation and Immunisation System (AEGIS) addresses these systemic vulnerabilities through a three-stage hierarchical pipeline that mathematically decouples offensive alpha generation from localized tail-risk management:

1. **Offensive Core (Anchor Triad via Volatility-Adjusted Momentum):** Rather than chasing unadjusted price returns, the signal generation module groups the universe by GICS sectors, identifies the 12-month cumulative return leader in each sector, and computes an efficiency score $S_i = R_i / \sigma_i$ (cumulative return normalized by annualized realized volatility). Locking the top three efficiency leaders as the "Anchor Triad" ensures exposure to the market's most stable, persistent structural trends while penalizing erratic variance.
2. **Defensive Immunization Layer (Recursive Minimax Correlation Protocol):** Downstream from the anchors, the remaining capital slots ($N-3$, default 47 diversifiers for a 50-asset basket) are filled via a greedy recursive minimax correlation algorithm. A boolean momentum gate first purges all decaying assets ($R_i \le 0$) to avoid the value trap of selecting distressed, uncorrelated assets. The algorithm then iteratively selects the candidate that minimizes the maximum pairwise correlation against existing basket members:
   $$\rho_{\max}(c) = \max_{b \in B} |\text{corr}(r_c, r_b)|, \quad c^* = \arg\min_{c \in P} \rho_{\max}(c)$$
   This enforces mathematical orthogonality across the basket, ensuring that localized sector collapses are contained rather than cascading into structural portfolio drawdowns.
3. **Convex Allocation Engine (SLSQP Sortino Optimization):** Capital weights are determined by solving a non-linear convex optimization problem using Sequential Least Squares Programming (SLSQP). Unlike Markowitz mean-variance optimization, which indiscriminately penalizes upside and downside volatility, the objective function maximizes the annualized Sortino ratio using a degree-2 Lower Partial Moment ($\text{LPM}_2$) hurdle rate of 4.0%. This treats upside volatility as desirable while aggressively penalizing downside variance.

### Research interpretation

The AEGIS architecture represents a structured synthesis of trend filtering, combinatorial graph dispersion, and asymmetric convex portfolio allocation. The recursive minimax correlation selection operates as a greedy approximation to the minimum-coherence sub-matrix problem, forcing portfolio assets to occupy disparate eigenvectors of the empirical return correlation matrix.

By enforcing a positive cumulative return gate ($R_i > 0$) prior to correlation minimization, the model eliminates a pervasive failure mode of pure minimum-variance or minimum-correlation algorithms: inadvertently loading into distressed, falling-knife assets that appear statistically uncorrelated only because they are undergoing idiosyncratic solvency crises.

The rolling 3-month retrospective lookback for SLSQP covariance estimation acts as an automated circuit-breaker: when an asset begins experiencing explosive downside semi-variance, the $\text{LPM}_2$ penalty forces its allocated weight rapidly toward zero before catastrophic ruin is realized.

## Signal

The trading logic is hierarchical and fully specified across three operational modules:

### Module 1: Signal Generation & Anchor Triad Selection (Algorithm 1)
- **Lookback Window ($L_{\text{select}}$):** 12 months (252 trading days) of daily total return (adjusted close) data (`source-reported`).
- **Universe Partitioning:** Ingest universe and partition into unique GICS sectors $S \in \{\text{Technology}, \text{Healthcare}, \text{Financials}, \dots\}$ (`source-reported`).
- **Sector Leader Identification:** For each unique sector $k$, identify the asset with the maximum 12-month cumulative logarithmic/total return:
  $$\text{Leader}_k = \arg\max_{i \in U_k} \left( R_{i, t-L:t} \right) \quad \text{(`source-reported`)}$$
- **VAM Efficiency Scoring:** For each sector leader, compute the annualized realized volatility:
  $$\sigma_k = \sqrt{252} \cdot \text{std}(r_{k, t-L:t}) \quad \text{(`source-reported`)}$$
  Compute the efficiency score:
  $$S_k = \frac{R_{k, t-L:t-1}}{\sigma_k} \quad \text{(`source-reported`)}$$
- **Anchor Selection:** Sort all sector leaders descending by efficiency score $S_k$. The top 3 sector leaders form the Anchor Triad $A = \{a_1, a_2, a_3\}$ (`source-reported`).

### Module 2: Structural Diversification via Recursive Minimax Correlation (Algorithm 2)
- **Momentum Gate:** From candidate pool $U \setminus A$, filter out assets with non-positive cumulative return. Candidate pool:
  $$P = \{ i \in U \setminus A \mid R_i > 0 \} \quad \text{(`source-reported`)}$$
- **Basket Initialization:** Initialize basket $B \leftarrow A$ (`source-reported`).
- **Target Basket Size ($N$):** Default $N = 50$ assets (3 anchors + 47 diversifiers; tested against 25 and 75 in robustness sweep) (`source-reported`).
- **Recursive Greedy Selection:**
  While $|B| < N$:
  1. For each candidate $c \in P$, compute its maximum absolute pairwise Pearson correlation against all current basket members:
     $$\rho_{\max}(c) = \max_{b \in B} |\text{corr}(r_c, r_b)| \quad \text{(`source-reported`)}$$
  2. Select the candidate minimizing this maximum correlation:
     $$c^* = \arg\min_{c \in P} \rho_{\max}(c) \quad \text{(`source-reported`)}$$
  3. Append $c^*$ to $B$, and remove $c^*$ from candidate pool $P$.
  4. Terminate when $|B| = N$ or if $P$ is exhausted.

### Module 3: Weight Allocation via Convex SLSQP Sortino Optimization (Algorithm 3)
- **Allocation Lookback Window ($L_{\text{alloc}}$):** 3 months (63 trading days) of retrospective daily returns (`source-reported`).
- **Optimization Objective:** Maximize the portfolio Sortino ratio with respect to weight vector $w$:
  $$\max_{w} F(w) = \frac{\text{AnnRet}(w) - R_f}{\text{LPM}_2(w) + \epsilon} \quad \text{(`source-reported`)}$$
  where:
  - $\text{DailyPortRet}_t = \sum_{i=1}^N w_i \cdot r_{i,t}$
  - $\text{AnnRet}(w) = \text{Mean}(\text{DailyPortRet}) \times 252$
  - $\text{Downside}_t = \min\left( \text{DailyPortRet}_t - \frac{R_f}{252}, 0 \right)$
  - $\text{LPM}_2(w) = \sqrt{\text{Mean}(\text{Downside}^2)} \times \sqrt{252}$
  - Risk-free hurdle rate: $R_f = 0.04$ (4.0% annualized) (`source-reported`).
  - Stability epsilon: $\epsilon = 10^{-6}$ (`source-reported`).
- **Institutional Portfolio Constraints:**
  - Budget constraint: $\sum_{i=1}^N w_i = 1.0$ (fully invested) (`source-reported`).
  - Long-only constraint: $w_i \ge 0 \quad \forall i$ (short-selling prohibited) (`source-reported`).
  - Diversification cap: $w_i \le 0.05 \quad \forall i$ (maximum 5% single-asset exposure) (`source-reported`).
- **Optimization Solver:** Sequential Least Squares Programming (`scipy.optimize.minimize(method='SLSQP')`) (`source-reported`).
- **Rebalance Cadence:** Rolling monthly rebalance ($t \leftarrow t + 1 \text{ month}$) (`source-reported`). Weights optimized over $[t - L_{\text{alloc}} : t]$ are held fixed out-of-sample over $[t : t+1]$.
- **Execution Timestamp / Order Timing:** Monthly closing prices on the final trading day of month $t$ to form weights, executed at next-day market open/close (`research-proposed` operationalization of source's period return convention).

## Required data

- **Instrument Universe:** U.S. Equities drawn from the aggregated constituent list of five primary indices: S&P 500, S&P MidCap 400, S&P SmallCap 600, NASDAQ-100, and Dow Jones Industrial Average (`source-reported`).
- **Classification Taxonomy:** GICS Sector mapping for all constituent assets (`source-reported`).
- **Price / Return Series:** Daily Adjusted Close prices adjusted for splits, dividends, and distributions, reflecting Total Return (`source-reported`).
- **Survivorship & Delisting Handling:** Historical pricing data for prominent delisted and bankrupted equities (e.g., Lehman Brothers, Enron, Washington Mutual) was manually injected back into the master dataset during their active operational windows to explicitly stress-test against survivorship bias (`source-reported`).
- **Missing Data Treatment:** Outer join on trading dates, forward-filling stale prices to preserve temporal causality, and dropping NaN rows prior to asset listing/IPO or post-delisting (`source-reported`).
- **Point-in-Time Separation:** Signal lookback $[t - L : t]$ strictly ceases prior to test window $[t : t+1]$ (`source-reported`).

## Execution assumptions

- **Rebalancing Frequency:** Monthly (`source-reported`).
- **Order Type:** Market orders at monthly boundary prices (`research-proposed`).
- **Fill Model:** Immediate full execution at monthly interval boundaries (`source-reported`).
- **Transaction Friction:** Flat 10 basis points ($f = 0.0010$) applied to portfolio turnover $\sum |w_{\text{opt}, i} - w_{\text{prev}, i}|$ at every monthly rebalance (`source-reported`).
- **Gross vs Net Realization:** Total gross return of 1950.78% converted to 1657.17% net return across the 2006–2025 period, representing an accumulated friction drag of -15.58% total (<1.0% annual average friction) (`source-reported`).
- **Leverage / Margin:** 1.0x (unlevered long-only, $\sum w_i = 1$, $w_i \ge 0$) (`source-reported`).
- **Borrow / Short Availability:** Not applicable (long-only) (`source-reported`).
- **Capacity / Market Impact Model:** Single-asset 5% cap distributes capital across at least 20 distinct assets; large-cap and mid-cap liquidity ensures high capacity, but explicit non-linear market impact for AUM > $100M was not modeled (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below are directly reported by Arya Chakraborty and Dr. Randhir Singh (arXiv:2604.09060v2, April 10, 2026) over the 20-year walk-forward backtest (January 2006 to December 2025):

#### 1. Aggregate Long-Term Performance (Table III, 2006–2025)
- **Total Gross Return:** 1950.78%
- **Total Net Return (after 10 bps friction):** 1657.17%
- **Compound Annual Growth Rate (CAGR):** 15.41%
- **Total Friction Impact:** -15.58% (average annual friction ~0.78%)
- **Annualized Volatility:** 16.44%
- **Maximum Drawdown:** -28.89% (vs S&P 500 -50.95%, NASDAQ -41.73% in 2008 GFC)
- **Sharpe Ratio:** 0.72 (assuming $R_f = 0.04$)
- **Average Sortino Ratio:** 6.47
- **Outlier-Adjusted Sortino Ratio:** 1.72 (excluding 2013 [Sortino 82.61] and 2017 [Sortino 15.79])
- **Monthly Win Rate:** 68.8% (positive returns in 165 out of 240 months)
- **Profitable Years:** 18 out of 20 years (90.0% win rate)
- **Best Calendar Year (2020):** +53.06% net return
- **Worst Calendar Year (2008):** -20.94% net return
- **Average Monthly Gain:** +1.31%

#### 2. Multi-Horizon CAGR Benchmarking vs Major U.S. Indices (Table IV, Ending 2025)
| Time Horizon | Period | AEGIS Strategy | S&P 500 | NASDAQ-100 | Dow Jones | S&P 400 MidCap | S&P 600 SmallCap |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 1-Year | 2025–2025 | 15.77% | 16.39% | 20.77% | 12.97% | 4.95% | -6.74% |
| 2-Year | 2024–2025 | 20.01% | 19.80% | 23.15% | 12.92% | 7.32% | 3.57% |
| 5-Year | 2021–2025 | 12.93% | 12.76% | 15.07% | 9.45% | 10.07% | 7.72% |
| 10-Year | 2016–2025 | 16.75% | 12.85% | 19.45% | 10.68% | 9.88% | 8.47% |
| 15-Year | 2011–2025 | 18.26% | 11.96% | 18.57% | 9.96% | 11.66% | — |
| 20-Year | 2006–2025 | 15.41% | 8.88% | 15.44% | 7.79% | 9.46% | — |

*Terminal wealth on $10,000 initial allocation (2006–2025):* AEGIS reached $176,302 vs S&P 500 $54,838 (+221% excess wealth) and NASDAQ-100 ~$176,000 (virtual return parity with vastly lower volatility and max drawdown).

#### 3. Crisis Resilience Across Systemic Macro Shocks (Table V)
| Strategy / Model | 2008 Global Financial Crisis | 2022 Macroeconomic Tightening |
| :--- | :---: | :---: |
| **AEGIS Framework** | **-20.94%** | **-5.10%** |
| Standard Momentum (CSM) | -42.58% | +4.99% |
| Risk Parity (Stock/Bond Proxy) | +5.68% | -26.72% |

#### 4. Parameter Robustness Matrix Across Basket Sizes and Allocation Lookbacks (Table VI)
| Allocation Lookback | 22 Diversifiers ($N=25$) | 47 Diversifiers ($N=50$, Primary) | 72 Diversifiers ($N=75$) |
| :--- | :--- | :--- | :--- |
| **3 Months** | CAGR: 12.70%<br>Max DD: -50.56%<br>Avg Vol: 19.15% | **CAGR: 15.41%<br>Max DD: -28.89%<br>Avg Vol: 16.44%** | CAGR: 13.22%<br>Max DD: -38.97%<br>Avg Vol: 15.89% |
| **6 Months** | CAGR: 11.32%<br>Max DD: -51.62%<br>Avg Vol: 19.24% | CAGR: 16.86%<br>Max DD: -30.46%<br>Avg Vol: 25.15% | CAGR: 11.70%<br>Max DD: -34.75%<br>Avg Vol: 16.45% |
| **12 Months** | CAGR: 12.71%<br>Max DD: -52.81%<br>Avg Vol: 16.74% | CAGR: 18.39%<br>Max DD: -37.94%<br>Avg Vol: 23.61% | CAGR: 13.61%<br>Max DD: -40.21%<br>Avg Vol: 16.74% |

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- **Under-diversification Breakdown ($N=25$):** Portfolios constrained to 22 diversifiers suffered catastrophic maximum drawdowns exceeding -50% across all allocation lookback windows (-50.56% to -52.81%), confirming that concentrated baskets cannot withstand localized asset decay when individual members undergo distress.
- **Over-diversification Momentum Drag ($N=75$):** Expanding diversifiers to 72 diluted the offensive momentum premium, capping CAGR at 11.70%–13.61% while still experiencing drawdowns between -34.75% and -40.21%.
- **Allocation Window Rigidity:** A 12-month covariance lookback produced the highest gross CAGR (+18.39%), but increased annualized volatility to 23.61% and maximum drawdown to -37.94%, failing to react promptly to swift market dislocations.
- **No live operational track record:** The reviewed primary paper is an academic simulation; no live trading or independently audited track record was identified.

## Falsification plan

To falsify the core claims that (1) recursive minimax correlation immunization truncates left-tail risk without sacrificing momentum alpha, and (2) SLSQP Sortino optimization provides structural advantage over classical allocation methods:

1. **Minimax Correlation Ablation Test:**
   - *Protocol:* Replace Algorithm 2's recursive minimax correlation selection with: (a) random selection of assets satisfying $R_i > 0$, and (b) selecting the highest cumulative return assets regardless of correlation.
   - *Decision Rule (`research-defined falsification threshold`):* If the naive momentum or random diversifier portfolio matches or improves upon the AEGIS maximum drawdown (within $\pm 3.0$ percentage points) and Sortino ratio (within $\pm 0.15$), reject the hypothesis that recursive correlation minimization provides structural tail-risk protection.
2. **Sortino vs Mean-Variance Optimization Ablation:**
   - *Protocol:* Replace Algorithm 3's Sortino objective with classical Markowitz mean-variance optimization (Sharpe ratio maximization) under identical constraints ($\sum w_i = 1$, $0 \le w_i \le 0.05$).
   - *Decision Rule (`research-defined falsification threshold`):* If classical MVO achieves an equivalent or lower maximum drawdown and higher Calmar ratio over the 2006–2025 period, reject the claim that downside semi-variance penalization is necessary for crisis resilience.
3. **Momentum Gate ($R_i > 0$) Removal Test:**
   - *Protocol:* Remove the boolean momentum gate ($R_i > 0$) in Algorithm 2, allowing distressed negative-momentum assets to enter the correlation minimization pool.
   - *Decision Rule (`research-defined falsification threshold`):* If removing the gate improves risk-adjusted returns or does not cause the portfolio to load into terminal bankruptcy decays, the claim that the gate prevents value traps is disconfirmed.
4. **Transaction Cost and Liquidity Stress Test:**
   - *Protocol:* Scale transaction friction from 10 bps to 25 bps, 50 bps, and 75 bps per turnover unit.
   - *Decision Rule (`research-defined falsification threshold`):* If net CAGR falls below the passive S&P 500 buy-and-hold benchmark (+8.88%) at transaction friction $\le 30 \text{ bps}$, reject the practical implementability of monthly SLSQP rebalancing for institutional execution.
5. **Out-of-Sample / Cross-Market Validation:**
   - *Protocol:* Execute walk-forward backtests on international equities (e.g., STOXX Europe 600, Nikkei 225) and post-2025 out-of-sample data.
   - *Decision Rule (`research-defined falsification threshold`):* If out-of-sample realized Sortino falls below 0.50 or maximum drawdown exceeds -40.0%, falsify the model's regime-agnostic generalizability.

## Crypto portability

- **Portability Status:** `adapted/unproven` (`research interpretation`). The primary source tests exclusively U.S. cash equities; it does not analyze cryptocurrency or digital asset derivatives.
- **Porting Challenges & Required Adaptations:**
  - *Sector Taxonomy Absence:* Crypto lacks standardized GICS sector definitions. Porting requires constructing synthetic sectors based on functional classifications (e.g., Layer-1, Layer-2, DeFi, AI/Compute, Memes, DePIN) or dynamic unsupervised clustering (e.g., spectral or k-means clustering on return correlations) (`research-proposed`).
  - *Extreme Correlation Convergence:* During liquidity panics and liquidation cascades in crypto, cross-token correlations routinely spike to 0.85–0.95 across all sectors. The greedy minimax correlation protocol may find no genuinely orthogonal diversifiers, collapsing the basket into high systemic beta (`research-proposed`).
  - *Time Horizon & Lookback Mismatch:* The 12-month momentum lookback reflects equity business cycles. In crypto's compressed narrative cycles, a 12-month lookback induces severe lag. An adapted framework would require compressing the momentum lookback to 30–60 days and the allocation lookback to 14–30 days (`research-proposed`).
  - *Perpetual Funding Drag:* In crypto perpetual futures, holding a long-only basket of 50 assets incurs perpetual funding payments. During market exuberance, positive funding rates (often 10%–30% annualized) would severely erode long-only momentum carry (`research-proposed`).
  - *Liquidity and Survivorship:* The crypto tail exhibits extreme token attrition and slippage. A strict liquidity filter (e.g., minimum $20M 30-day median daily dollar volume) is mandatory to prevent execution failure on diversifiers (`research-proposed`).

## Limitations

- **Traditional Equities Only (`source-reported`):** The empirical evidence is restricted to U.S. large, mid, and small-cap equities from 2006 to 2025. It does not validate performance in crypto, FX, or commodities.
- **No Public Code Repository (`provenance gap`):** While the mathematical equations and algorithm steps are comprehensively printed, no official GitHub codebase was provided by the authors for bitwise replication.
- **Simplified Transaction Friction:** A fixed 10 bps friction model does not capture non-linear market impact, market-on-close slippage, or bid-ask spread expansion during volatility crises (e.g., October 2008 or March 2020).
- **Execution Timing Underspecification:** The paper does not specify the precise execution timestamp (e.g., market-on-open vs market-on-close) for rolling monthly rebalancing.
- **Unconstrained Solver Sensitivity:** SLSQP non-linear optimization with 50 assets over a 63-day lookback may be sensitive to local minima or matrix ill-conditioning when assets exhibit near-collinearity.

## Implementation status

`not-implemented`. Neither the AEGIS architecture, the VAM efficiency score, the recursive minimax correlation filter, nor the SLSQP Sortino convex allocation engine is implemented in our research repository, PyBroker, or NautilusTrader stacks.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This document represents external academic research capture for conceptual analysis and potential future algorithmic synthesis. It does not constitute strategy approval, validation in our proprietary backtesting infrastructure, or authorization for paper, testnet, or live trading deployment.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — Authoritative strategy-research record specification.
- `size-enhanced-left-side-momentum-resga-expected-shortfall-2026-09-04.md` — Left-side momentum with tail risk control in equity portfolios.
- `graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05.md` — Graph-theoretic methods for eliminating shared-asset covariance in portfolio selection.
- `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md` — Statistical arbitrage on S&P 500 constituents with rigorous multiple testing controls.
- `simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11.md` — Dynamic asset allocation with volatility targeting.
- `nystrom-attention-cross-sectional-stock-transformer-low-rank-2026-09-11.md` — Low-rank representation learning for cross-sectional stock ranking.

## Sources

1. Arya Chakraborty and Dr. Randhir Singh, "Taming the Black Swan: A Momentum-Gated Hierarchical Optimisation Framework for Asymmetric Alpha Generation", arXiv preprint `arXiv:2604.09060v2 [q-fin.PM]`, submitted April 10, 2026.
   - Stable arXiv abstract: https://arxiv.org/abs/2604.09060
   - Full text PDF: https://arxiv.org/pdf/2604.09060.pdf
   - Canonical DOI: [10.48550/arXiv.2604.09060](https://doi.org/10.48550/arXiv.2604.09060)
   - Methodology & Algorithms: Section II (Data Acquisition & Mathematical Framework), Section III (Proposed Model & Algorithms 1, 2, 3).
   - Empirical Performance & Ablations: Section IV (Results & Discussions), Table II (Year-by-Year Performance 2006–2025), Table III (Overall 20-Year Statistics), Table IV (Multi-Horizon CAGR vs Benchmarks), Table V (Crisis Performance 2008 & 2022), Table VI (Parameter Robustness Matrix).
