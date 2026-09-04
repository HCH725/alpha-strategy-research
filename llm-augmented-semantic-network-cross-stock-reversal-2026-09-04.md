---
schema: strategy-research-record-v1
title: "Cross-Stock Predictability via LLM-Augmented Semantic Networks: Spurious Linkage Filtering, Gatev Distance Softmax Aggregation, and Cross-Sectional Quintile Reversal (Huang et al. 2026)"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional
  - statistical-arbitrage
  - mean-reversion
  - llm-reasoning
  - semantic-network
  - 10k-filings
  - equity
status: research-only
confidence: medium
source_as_of: 2026-04-28
sources:
  - "Yikuan Huang, Zheqi Fan, Kaiqi Hu, and Yifan Ye, 'Cross-Stock Predictability via LLM-Augmented Semantic Networks', arXiv:2604.19476v2 [q-fin.PM], April 28, 2026. DOI: 10.48550/arXiv.2604.19476. https://arxiv.org/abs/2604.19476"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Stock Predictability via LLM-Augmented Semantic Networks: Spurious Linkage Filtering, Gatev Distance Softmax Aggregation, and Cross-Sectional Quintile Reversal (Huang et al. 2026)

## Provenance

- **Primary Paper:** Yikuan Huang (EMIA & FinTech, The Hong Kong University of Science and Technology / HKUST Guangzhou), Zheqi Fan (EMIA & FinTech, The Hong Kong University of Science and Technology / HKUST Guangzhou), Kaiqi Hu (Rutgers Business School, Rutgers University–New Brunswick), and Yifan Ye (Faculty of Business and Management, Beijing Normal–Hong Kong Baptist University), *"Cross-Stock Predictability via LLM-Augmented Semantic Networks"*, arXiv preprint `arXiv:2604.19476v2 [q-fin.PM, q-fin.GN, q-fin.ST]`, submitted April 28, 2026 (v2 revised April 29, 2026).
- **Canonical Stable URL:** [https://arxiv.org/abs/2604.19476](https://arxiv.org/abs/2604.19476)
- **Digital Object Identifier (DOI):** [10.48550/arXiv.2604.19476](https://doi.org/10.48550/arXiv.2604.19476)
- **Full Text HTML:** [https://arxiv.org/html/2604.19476v2](https://arxiv.org/html/2604.19476v2)
- **Direct Source Verification:** The complete primary source package (including LaTeX manuscripts `P1.tex` through `P6.tex`, `ijcai26.tex`, and `ijcai26.bib`) was directly inspected and audited. Every formula, prompt specification, relation taxonomy weight, and empirical figure in Table 1, Table 2, and Table 3 traces directly to this primary source package without secondary summarization.
- **Audit Confirmation:** A repository-wide audit against recent commits, file names, and Hermes Wiki Brain confirmed zero existing records matching `arXiv:2604.19476`, author `Yikuan Huang` on semantic networks, or the Retrieve-then-Reason cross-stock framework.

## Economic mechanism

### Source-reported

Cross-stock predictability—the empirical regularity where the current returns of economically linked firms forecast the future return of a focal firm—stems from investor inattention and gradual information diffusion across economic networks (Cohen & Frazzini 2008, Menzly & Ozbas 2010). While corporate textual disclosures (SEC Form 10-K) permit constructing large-scale peer networks via dense embedding vectors (e.g., 768-dimensional language model embeddings), unsupervised embedding proximity suffers from a fundamental structural flaw: **spurious correlation**. Embeddings capture topical similarity (e.g., shared discussion of macroeconomic headwinds, regulatory mandates, or pandemic supply chain disruptions) rather than direct operational or economic causality. Unrelated firms discussing similar macro risks appear adjacent in embedding space, yet price divergence between them carries zero mean-reverting information.

Furthermore, inter-firm economic relationships are heterogeneous in their price transmission dynamics:
1. **Competitors:** Direct rivals competing for identical market share exhibit price divergence driven by structural market-share reallocation (one firm winning customers from another). A price divergence between direct competitors reflects fundamental drift rather than temporary inefficiency, making mean-reversion signals across competitors counter-productive.
2. **Supply Chain, Complementary, and Peer Relationships:** Suppliers, customer partners, complementary goods producers, and non-competing industry peers share mutual cost/demand drivers without zero-sum market displacement. Temporary price divergences between these firms reflect delayed information dissemination and over/underreaction, which reliably mean-revert toward historical spread equilibrium.

### Research interpretation

The hypothesized economic mechanism is **cross-sectional relative-value mean reversion over economically constrained pair manifolds**:
1. **Topical vs. Causal Disentanglement:** Textual embeddings act as an effective high-recall filter ($O(NK)$ candidate edges), while zero-temperature LLM semantic classification serves as a high-precision gate. Anonymizing firm disclosures into "Firm A" and "Firm B" forces the LLM to perform contextual structural reasoning rather than memorizing historical ticker betas.
2. **Relation-Aware Pruning:** Setting edge weights for direct rivals to zero ($\omega_{\text{competitor}} = 0$) removes non-reverting structural shifts, while down-weighting substitute goods ($\omega_{\text{substitute}} = 0.5$) mitigates intermediate competitive drift.
3. **Gatev Co-Movement Distance Weighting:** Normalizing pair z-scores via softmax weighting over negative historical sum of squared deviations ($d_{ij} = \sum s_{ij,\tau}^2$) concentrates predictive capital onto pairs with proven co-integration or tight price tracking, suppressing noisy outlier pairs with wide structural variance.

## Signal

### Mathematical formulation (Source-reported)

1. **Normalized Price Definition:**
   For each stock $v_i \in \mathcal{V}$ ($N \approx 500$ S&P 500 constituents) starting from window reference date $t_0$:
   $$P_{i,t} = \prod_{\tau=t_0}^{t} (1 + r_{i,\tau})$$
   where $r_{i,\tau}$ is the split- and dividend-adjusted daily return.

2. **Stage 1: Candidate Graph Generation ($\mathcal{G}_{\text{emb}}$):**
   - For fiscal year $y-1$, compute 768-dimensional document embeddings $\mathbf{h}_i \in \mathbb{R}^{768}$ from annual 10-K filings.
   - Compute pairwise cosine similarity:
     $$\text{sim}(v_i, v_j) = \frac{\mathbf{h}_i^\top \mathbf{h}_j}{\|\mathbf{h}_i\| \|\mathbf{h}_j\|}$$
   - For each stock $v_i$, retain edges to its top-$K$ most similar peers ($K = 5$ default).
   - Construct undirected candidate edge set $\mathcal{E}_{\text{emb}}$ by symmetrization: $(v_i, v_j) \in \mathcal{E}_{\text{emb}}$ if $v_j \in \text{top-}K(v_i)$ or $v_i \in \text{top-}K(v_j)$. Graph edge count scales as $O(NK)$.

3. **Stage 2: LLM-Augmented Edge Classification & Refinement ($\mathcal{G}_{\text{ref}}$):**
   - Query DeepSeek-Chat at temperature $T = 0$ with an anonymized prompt containing:
     - Truncated business description from Item 1 (first $\sim 500$ tokens).
     - Extracted segment- and product-related sentences from Item 1.
     - Extracted competitor-related sentences identified via regex patterns (e.g., surrounding "compete with").
   - Classify relationship into one of six mutually exclusive categories:
     $$\mathcal{R} \in \{\texttt{competitor}, \texttt{supply\_chain}, \texttt{complementary}, \texttt{substitute}, \texttt{peer}, \texttt{unrelated}\}$$
   - Assign relation tradability and weight multiplier $\omega_r$:
     $$(\text{tradable}_r, \omega_r) = \begin{cases} (\text{False}, 0.0) & r = \texttt{competitor} \\ (\text{True}, 0.5) & r = \texttt{substitute} \\ (\text{True}, 1.0) & r \in \{\texttt{supply\_chain}, \texttt{complementary}, \texttt{peer}\} \\ (\text{False}, 0.0) & r = \texttt{unrelated} \end{cases}$$
   - Refined edge set: $\mathcal{E}_{\text{ref}} = \{ (v_i, v_j) \in \mathcal{E}_{\text{emb}} \mid \text{tradable}_{f_{\text{LLM}}(v_i, v_j)} = \text{True} \}$.

4. **Training Phase Spread Parameters:**
   Over the 180-trading-day training window $[t_0, t_1]$:
   - Pairwise normalized price spread:
     $$s_{ij,t} = P_{i,t} - P_{j,t}, \quad t \in [t_0, t_1]$$
   - Historical mean spread:
     $$\mu_{ij} = \frac{1}{t_1 - t_0 + 1} \sum_{t=t_0}^{t_1} s_{ij,t}$$
   - Historical spread standard deviation:
     $$\sigma_{ij} = \sqrt{\frac{1}{t_1 - t_0} \sum_{t=t_0}^{t_1} (s_{ij,t} - \mu_{ij})^2}$$
   - Gatev et al. (2006) sum of squared spread distance:
     $$d_{ij} = \sum_{t=t_0}^{t_1} s_{ij,t}^2$$

5. **Test Phase Pair Z-Scores:**
   Over the 2-month test window $[t_1 + 1, t_2]$:
   $$z_{ij,t} = \frac{s_{ij,t} - \mu_{ij}}{\sigma_{ij}}$$
   where $z_{ij,t} > 0$ indicates $v_i$ is overvalued relative to $v_j$, projecting $v_i$ underperformance and $v_j$ outperformance.

6. **Per-Stock Signal Aggregation:**
   Aggregate pair z-scores to stock-level cross-sectional score $S_{i,t}$:
   $$S_{i,t} = \sum_{(i,j) \in \mathcal{E}_{\text{ref}}} \left( -z_{ij,t} \cdot w_{ij}^{(i)} \right)$$
   with Gatev distance softmax weighting scaled by relation weight $\omega_r$ and node degree $n_i = |\{(i,k) \in \mathcal{E}_{\text{ref}}\}|$:
   $$w_{ij}^{(i)} = \omega_r \cdot n_i \cdot \frac{\exp(-d_{ij})}{\displaystyle\sum_{(i,k) \in \mathcal{E}_{\text{ref}}} \exp(-d_{ik})}$$

7. **Portfolio Sorting:**
   Sort all available stocks cross-sectionally by $S_{i,t}$ into $G = 5$ equal quintiles.
   - Long Group 5 ($Q5$): Top 20% highest scores (projected to appreciate / most oversold).
   - Short Group 1 ($Q1$): Bottom 20% lowest scores (projected to decline / most overbought).
   - Daily rebalanced, equal-weighted within each quintile.

### Operational specifications & parameter classifications

- **Signal Formation Timestamp:**
  - `source-reported`: Calculated at daily market close using daily adjusted close price series; 10-K filings from calendar year $y-1$ applied to rolling windows commencing in year $y$.
  - `research-proposed`: In live operations, compute at 15:45 EST using real-time consolidated market feeds for Market-on-Close (MOC) order placement, or post-close at 16:05 EST for next-day open execution.
- **Lookback Window:**
  - `source-reported`: 180 trading days for spread mean $\mu_{ij}$, variance $\sigma_{ij}^2$, and Gatev distance $d_{ij}$; test window evaluation horizon is 2 calendar months (approx. 42 trading days).
- **Entry Trigger:**
  - `source-reported`: Stock ranks in the top quintile ($Q5$) for long entry or bottom quintile ($Q1$) for short entry upon daily cross-sectional re-ranking.
  - `research-proposed`: Entry gate requiring absolute aggregated score $|S_{i,t}| \ge 0.50$ standard deviations to prevent entering marginal positions with low conviction.
- **Exit Trigger:**
  - `source-reported`: Daily rebalancing reallocation when a stock transitions out of $Q5$ or $Q1$, or natural window rollover after 2 test months.
  - `research-proposed`: Dynamic risk stop: liquidate individual stock pair legs if relative spread widens past $-2.5\times \sigma_{ij}$ from entry, or if portfolio cumulative daily drawdown reaches $2.5\%$.
- **Holding Period:**
  - `source-reported`: Daily rebalancing frequency; test window duration 2 months.
- **Position Sizing:**
  - `source-reported`: Equal weighting within quintiles; dollar-neutral $100\%$ long $Q5$ and $100\%$ short $Q1$.
  - `research-proposed`: Inverse-volatility weighting scaled by stock 30-day realized volatility, capped at a maximum single-stock allocation of $2.0\%$ of total capital and $\le 1.5\%$ of 20-day Average Daily Volume (ADV).
- **Parameters & Hyperparameters:**
  - `source-reported`:
    - Top-$K$ embedding neighbors: $K = 5$.
    - Training window: 180 trading days.
    - Test holding window: 2 calendar months.
    - Quantile groups: $G = 5$.
    - Rebalancing cadence: daily.
    - Relation weight multipliers: $\omega_{\text{competitor}} = 0.0$, $\omega_{\text{substitute}} = 0.5$, $\omega_{\text{supply\_chain}} = 1.0$, $\omega_{\text{complementary}} = 1.0$, $\omega_{\text{peer}} = 1.0$, $\omega_{\text{unrelated}} = 0.0$.
    - LLM: DeepSeek-Chat, temperature $= 0.0$.
    - Textual disclosure truncation: first $\sim 500$ tokens of Item 1.

## Required data

- **Universe:** U.S. common stocks listed in the S&P 500 index (approx. 605 unique CRSP PERMNOs over the sample period, with approx. 497 stocks per year having valid matched 10-K filings).
- **Asset Class / Market Type:** U.S. Equities (Cash Spot).
- **Pricing Fields:** CRSP daily adjusted returns ($r_{i,t}$), adjusted closing prices, and cumulative gross return indices.
- **Corporate Disclosure Data:** Annual SEC Form 10-K filings:
  - Item 1 (Business Description): First $\sim 500$ tokens.
  - Item 1 (Products & Segments): Extracted segment disclosure sentences.
  - Item 1 (Competition): Regex-extracted text snippets surrounding "compete with" and competitor designations.
- **Pre-trained Embeddings:** 768-dimensional dense document embedding vectors derived from firms' annual risk-factor disclosures.
- **Point-in-Time Availability:** 10-K filings for fiscal year $y-1$ are utilized for trading models beginning in calendar year $y$, providing a strict lag to prevent look-ahead bias.
- **Missing Data Handling:**
  - `source-reported`: Stocks lacking valid textual embeddings in year $y-1$ or having missing CRSP return observations across the 180-day training window are excluded from that window's candidate graph.
  - `research-proposed`: If an active stock suffers a trading halt during the 2-month test window, its price is frozen at the last traded price; if delisted, position is closed at the terminal liquidating distribution.

## Execution assumptions

- **Order Timing & Type:**
  - `source-reported`: Underspecified; assumed frictionless execution at CRSP daily closing prices with zero explicit transaction costs, zero commissions, and zero borrow fees.
  - `research-proposed`: Market-on-Close (MOC) orders executed at 16:00 EST. Rebalancing trades execute at closing auction price.
- **Transaction Costs & Friction:**
  - `source-reported`: 0 bps transaction fees and 0 bps slippage evaluated in baseline paper tables.
  - `research-proposed`: Large-cap S&P 500 execution model: 2.5 bps exchange/brokerage fees plus 2.5 bps half-spread crossing cost (5.0 bps per half-turn; 10.0 bps round-trip).
- **Borrow & Shorting:**
  - `source-reported`: Unconstrained short sales assumed for Group 1 ($Q1$) constituents.
  - `research-proposed`: S&P 500 constituents are general collateral (GC); assumed annual borrow fee of 25 bps applied pro-rata to short positions.
- **Execution Capacity:**
  - `source-reported`: Omitted in primary source.
  - `research-proposed`: Based on S&P 500 median constituent ADV ($>\$100\,\text{million}$), estimated institutional capacity is approximately $\$50\,\text{million}$ to $\$100\,\text{million}$ before market impact significantly degrades net alpha.

## Evidence

### Source-reported

All figures below are directly extracted from Huang, Fan, Hu, and Ye (`arXiv:2604.19476v2`, Section 5, Tables 1–3) evaluated over the out-of-sample period January 2011 to December 2019 (2,210 trading days, 9 calendar years):

#### Table 1: Core Component Ablation (Long-Short Portfolio Performance)

| Configuration | Annualized Return ($r^{\text{ann}}$) | Annualized Volatility ($\sigma^{\text{ann}}$) | Sharpe Ratio ($SR$) | Max Drawdown ($MDD$) | Annualized Turnover ($TO^{\text{ann}}$) | Newey-West $t$-stat ($t_{NW}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Semantic Network (Baseline, No LLM) | 4.11% | 5.54% | 0.742 | $-$10.47% | 23.7$\times$ | 2.14 |
| **+ LLM Filtering (Full Proposed)** | **4.67%** | **5.69%** | **0.820** | **$-$7.85%** | **22.0$\times$** | **2.32** |
| No Distance Weighting (Equal Weight) | 5.21% | 6.58% | 0.792 | $-$10.61% | 16.4$\times$ | 2.19 |
| Random Network ($K=5$ Random Graph) | 4.52% | 8.36% | 0.541 | $-$13.15% | 25.3$\times$ | 1.61 |
| SIC Industry Network (2-digit SIC) | 4.60% | 5.80% | 0.792 | $-$9.56% | 23.0$\times$ | 2.32 |

*Source-reported findings:*
- Adding LLM edge filtering yields simultaneous improvements across all key risk dimensions: $+56\,\text{bps}$ annualized return, $+0.078$ Sharpe ratio, and $+262\,\text{bps}$ reduction in maximum drawdown.
- S&P 500 semantic network structure significantly beats random network topology ($SR = 0.820$ vs. $0.541$, $t_{NW} = 2.32$ vs. $1.61$).
- LLM-filtered semantic network outperforms static 2-digit SIC industry networks ($SR = 0.820$ vs. $0.792$, $MDD = -7.85\%$ vs. $-9.56\%$).

#### Table 2: Quintile Portfolio Performance (LLM-Augmented Framework)

| Group | Annualized Return ($r^{\text{ann}}$) | Annualized Volatility ($\sigma^{\text{ann}}$) | Sharpe Ratio ($SR$) |
| :--- | :---: | :---: | :---: |
| Q1 (Short Leg) | 11.77% | 15.50% | 0.759 |
| Q2 | 13.58% | 15.09% | 0.900 |
| Q3 | 13.59% | 15.22% | 0.892 |
| Q4 | 15.88% | 15.67% | 1.013 |
| Q5 (Long Leg) | 16.43% | 16.77% | 0.980 |
| **L$-$S (Q5 $-$ Q1)** | **4.67%** | **5.69%** | **0.820** |

*Source-reported findings:*
- Return sorting across quintiles is strictly monotonic ($11.77\% \to 13.58\% \to 13.59\% \to 15.88\% \to 16.43\%$).
- Alpha generation is distributed across both legs, with long-leg outperformance ($Q5 = 16.43\%$) leading short-leg underperformance ($Q1 = 11.77\%$).

#### Table 3: Parameter Sensitivity Analysis (Long-Short Portfolio)

| Parameter | Value | $r^{\text{ann}}$ | $\sigma^{\text{ann}}$ | $SR$ | $MDD$ | $TO^{\text{ann}}$ | $t_{NW}$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Top-$K$ Neighbors** | $K = 3$ | 4.56% | 5.68% | 0.802 | $-$10.77% | 20.4$\times$ | 2.25 |
| | **$K = 5$ (Default)** | **4.67%** | **5.69%** | **0.820** | **$-$7.85%** | **22.0$\times$** | **2.32** |
| | $K = 10$ | 4.77% | 6.26% | 0.762 | $-$10.38% | 24.4$\times$ | 2.18 |
| | $K = 15$ | 5.02% | 6.57% | 0.763 | $-$7.59% | 25.3$\times$ | 2.20 |
| **Training Window** | 120 days | 5.04% | 5.96% | 0.845 | $-$14.56% | 23.1$\times$ | 2.39 |
| | **180 days (Default)** | **4.67%** | **5.69%** | **0.820** | **$-$7.85%** | **22.0$\times$** | **2.32** |
| | 250 days | 4.11% | 5.63% | 0.730 | $-$10.86% | 21.1$\times$ | 2.01 |
| **Holding Period** | 1 month | 4.22% | 5.97% | 0.707 | $-$11.07% | 25.5$\times$ | 2.01 |
| | **2 months (Default)** | **4.67%** | **5.69%** | **0.820** | **$-$7.85%** | **22.0$\times$** | **2.32** |
| | 3 months | 2.65% | 5.62% | 0.471 | $-$11.26% | 19.2$\times$ | 1.35 |
| | 6 months | 1.63% | 6.01% | 0.271 | $-$13.84% | 15.3$\times$ | 0.78 |
| **Quantile Groups** | **$G = 5$ (Default)** | **4.67%** | **5.69%** | **0.820** | **$-$7.85%** | **22.0$\times$** | **2.32** |
| | $G = 10$ (Deciles) | 5.05% | 7.62% | 0.662 | $-$15.45% | 26.8$\times$ | 1.85 |
| **Rebal. Cadence** | **Daily (Default)** | **4.67%** | **5.69%** | **0.820** | **$-$7.85%** | **22.0$\times$** | **2.32** |
| | Monthly | 2.70% | 5.38% | 0.502 | $-$11.73% | 2.9$\times$ | 1.38 |

*Provenance Gap:* Authors mention in narrative that Fama–French factor regressions confirm positive daily alpha with near-zero factor loadings, but do not provide an explicit numerical regression table. Transaction costs are omitted in the source backtest.

### Independently reproduced

`Not independently reproduced.` All figures, ablation tables, sensitivity sweeps, and prompt designs cited above represent direct extractions from the primary preprint text and LaTeX source files (`arXiv:2604.19476v2`).

### Negative evidence

1. **Turnover Friction Fragility:** The baseline strategy generates $22.0\times$ annualized turnover. At an annualized gross long-short return of $4.67\%$, any transaction cost exceeding $10.6\,\text{bps}$ per one-way turn ($22.0 \times 2 \times 0.00106 \approx 4.66\%$) entirely consumes the gross alpha.
2. **Rapid Signal Decay:** Extending the test holding period beyond 2 months causes severe performance degradation: at 3 months, Sharpe ratio falls to $0.471$ ($t_{NW} = 1.35$, not statistically significant); at 6 months, Sharpe ratio drops to $0.271$ ($t_{NW} = 0.78$).
3. **Rebalancing Frequency Sensitivity:** Moving from daily rebalancing to monthly rebalancing reduces the Sharpe ratio from $0.820$ to $0.502$ ($t_{NW} = 1.38$, insignificant), demonstrating that the alpha relies on high-frequency daily z-score re-alignment rather than long-term buy-and-hold predictability.
4. **Decile Overfitting:** Concentrating the portfolio into deciles ($G = 10$) increases volatility by $+193\,\text{bps}$ (to $7.62\%$), reduces Sharpe ratio to $0.662$, and nearly doubles maximum drawdown (from $-7.85\%$ to $-15.45\%$).

## Falsification plan

To falsify the hypothesis that LLM semantic reasoning produces actionable cross-stock mean-reversion alpha, execute the following operational tests:

1. **Transaction Cost Attrition Test:**
   - *Data & Method:* Backtest the exact daily rebalanced strategy with realistic execution friction: 5.0 bps per half-turn (10 bps round-trip) and 25 bps annual borrow fee on the short leg.
   - *research-defined falsification threshold:* If net-of-cost annualized Sharpe ratio falls below $SR_{\text{net}} < 0.20$ or net annual return falls below $1.5\%$, reject the hypothesis as an unexecutable theoretical artifact driven by turnover drag.
2. **Out-of-Sample Period Extension (2020–2025):**
   - *Data & Method:* Evaluate performance across the post-sample period (January 2020 to December 2025), encompassing the COVID crash, high-inflation regime, and 2023–2025 tech rally.
   - *research-defined falsification threshold:* If the out-of-sample annualized Sharpe ratio is $SR_{\text{OOS}} < 0.35$ or Newey–West $t$-stat $t_{NW} < 1.65$, falsify the temporal stability of 10-K embedding relationships.
3. **Randomized LLM Relation Placebo Test:**
   - *Data & Method:* Permute the LLM-assigned relation labels randomly across candidate edges while preserving label marginal distributions, then re-run edge pruning ($\omega_{\text{random}} = 0$ for randomly assigned competitor edges).
   - *research-defined falsification threshold:* If the true LLM-filtered portfolio does not outperform the empirical 95th percentile of 500 randomized placebo runs ($\Delta SR \le 0$, $p \ge 0.05$), reject the hypothesis that LLM semantic classification provides genuine economic discernment.
4. **Capacity & Microstructure Impact Stress:**
   - *Data & Method:* Apply Almgren–Chriss square-root market impact modeling with participation rates ranging from $1\%$ to $5\%$ ADV across simulated portfolio sizes from $\$10\,\text{million}$ to $\$100\,\text{million}$.
   - *research-defined falsification threshold:* If portfolio capacity drops below $\$15\,\text{million}$ before net alpha reaches zero, classify the strategy as non-institutional.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`
- **Portability Justification & Adaptation Requirements:**
  - *Source Restriction:* The primary source demonstrates the mechanism solely on U.S. equities (S&P 500). Porting this framework to digital assets represents a research interpretation rather than established empirical evidence.
  - *Absence of Mandated Annual Disclosures:* Cryptocurrencies lack mandatory annual regulatory filings (SEC Form 10-K Item 1). Applying this strategy to crypto requires substituting 10-K filings with whitepapers, GitHub documentation repositories, governance forum proposals, or CoinGecko / CoinMarketCap technical descriptions.
  - *Relation Taxonomy Divergence:* Traditional corporate relations (e.g., supplier, customer, substitute) must be adapted to crypto protocol archetypes:
    - Base Layer 1 vs. Layer 2 rollup scaling solutions.
    - Liquidity bridge or wrapped asset dependency.
    - Shared governance tokens, venture backing, or shared ecosystem foundations.
    - Direct DEX / Lending protocol competitors vs. complementary tooling.
  - *Funding Rate and Carrying Cost Drag:* Crypto relative-value pair trades are predominantly executed using perpetual contracts. In volatile regimes, extreme cross-sectional funding rate divergences between long and short legs can rapidly erode the modest gross return margin ($4.67\%$ annualized), imposing carrying cost drag not present in traditional equities.
  - *Execution Boundary:* Without a formal empirical trial on cryptocurrency historical order books, crypto deployment remains completely unproven and strictly prohibited.

## Limitations

1. **Frictionless Backtest Assumption:** The primary paper omits trading commissions, bid-ask spread crossing costs, market impact, and borrow fees. Given the $22.0\times$ annual turnover, net returns will be substantially lower than reported gross returns.
2. **Annual Graph Inflexibility:** 10-K disclosures update only once annually. Inter-firm relationship disruptions occurring mid-year (such as sudden mergers, bankruptcies, or new product launches) remain uncaptured until the subsequent fiscal filing.
3. **LLM Non-Determinism & Version Drift:** Although evaluated at temperature $T = 0$, proprietary LLM API endpoints (such as DeepSeek-Chat) undergo silent backend model updates and weights refactoring, introducing reproducibility drift over multi-year horizons.
4. **Information Loss from Heuristic Truncation:** Truncating Item 1 disclosures to $\sim 500$ tokens to satisfy LLM context budgets may discard crucial revenue segmentation or supplier concentration data.
5. **Universe Selection Survivorship:** The sample is restricted to S&P 500 constituents, introducing a liquidity and market-cap survivorship tilt that may not generalize to broader small-cap or Russell 2000 universes.

## Implementation status

- **Status:** `not-implemented`
- **Repository Context:** No implementation in `nautilus-quant-system`, PyBroker, or NautilusTrader has been executed. No strategy family, backtest campaign, or live execution script exists.
- **Workflow Boundary:** This record represents an upstream research capture exclusively. Implementation in PyBroker or NautilusTrader requires explicit separate review and research authorization.

## Adoption boundary

- **Status:** `research-only`
- **Adoption Scope:** `not-approved`
- **Boundary Declaration:** This research document does not authorize live trading, paper trading, testnet deployment, or production capital allocation. Presence in this repository indicates only that the research idea has been normalized into canonical Wiki Brain format.

## Related Wiki records

- `[[quant/supply-chain-network-augmented-llm-text-embeddings-nale-2026-09-04]]` — Inter-firm production network propagation of LLM text embeddings for equity factor investing (arXiv:2606.29290).
- `[[quant/stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04]]` — Learnable soft-threshold graph attention networks for top-k equity selection (arXiv:2607.19385).
- `[[quant/dynamic-knowledge-graph-community-gated-signal-propagation-2026-09-04]]` — Dynamic knowledge graph community-gated signal propagation for cross-firm return forecasting (arXiv:2607.10932).
- `[[quant/crypto-llm-agent-liquidity-scarcity-range-attention-factor-2026-09-01]]` — Agentic LLM factor discovery in digital asset markets (arXiv:2604.26747).
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Methodological standard for preventing look-ahead leakage and backtest overfitting.

## Sources

1. Yikuan Huang, Zheqi Fan, Kaiqi Hu, and Yifan Ye, *"Cross-Stock Predictability via LLM-Augmented Semantic Networks"*, arXiv preprint `arXiv:2604.19476v2 [q-fin.PM, q-fin.GN, q-fin.ST]`, submitted April 28, 2026 (v2 revised April 29, 2026).
   - Canonical Abstract URL: [https://arxiv.org/abs/2604.19476](https://arxiv.org/abs/2604.19476)
   - Canonical DOI: [10.48550/arXiv.2604.19476](https://doi.org/10.48550/arXiv.2604.19476)
   - Full Text HTML: [https://arxiv.org/html/2604.19476v2](https://arxiv.org/html/2604.19476v2)
   - Full Text PDF: [https://arxiv.org/pdf/2604.19476v2](https://arxiv.org/pdf/2604.19476v2)
   - Source Package Archive: `https://arxiv.org/e-print/2604.19476` (verified primary LaTeX source: `P1.tex`, `P2.tex`, `P3.tex`, `P4.tex`, `P5.tex`, `P6.tex`, `ijcai26.tex`, `ijcai26.bib`)
2. Lauren Cohen and Andrea Frazzini, *"Economic Links and Predictable Returns"*, The Journal of Finance, 63(4):1977–2011, 2008. DOI: [10.1111/j.1540-6261.2008.01379.x](https://doi.org/10.1111/j.1540-6261.2008.01379.x).
3. Evan Gatev, William N. Goetzmann, and K. Geert Rouwenhorst, *"Pairs Trading: Performance of a Relative-Value Arbitrage Rule"*, The Review of Financial Studies, 19(3):797–827, 2006. DOI: [10.1093/rfs/hhj020](https://doi.org/10.1093/rfs/hhj020).
4. K. Yenzer Menzly and Oguzhan Ozbas, *"Market Segmentation and Cross-predictability of Returns"*, The Journal of Finance, 65(4):1555–1580, 2010. DOI: [10.1111/j.1540-6261.2010.01578.x](https://doi.org/10.1111/j.1540-6261.2010.01578.x).
