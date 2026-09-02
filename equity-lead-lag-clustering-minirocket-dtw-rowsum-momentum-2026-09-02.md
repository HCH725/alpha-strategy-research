---
schema: strategy-research-record-v1
title: "Cross-Sectional Equity Lead-Lag Harvesting via Time-Series Clustering: MiniRocket-KMeans, KShape, and Pairwise DTW Lag Matrix RowSum Partitioning"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - lead-lag
  - time-series-clustering
  - minirocket
  - kshape
  - dtw
  - cross-sectional-momentum
  - crsp
status: research-only
confidence: medium
source_as_of: 2026-08-25
sources:
  - "Ruichen Deng (Nankai University) and Yichi Zhang (University of Oxford), 'Lead-Lag Relationships in Financial Markets: A Comparison of Multiple Clustering Algorithms', arXiv preprint arXiv:2608.24703v1 [q-fin.ST], submitted August 25, 2026. DOI: 10.48550/arXiv.2608.24703. Stable URL: https://arxiv.org/abs/2608.24703. Full text HTML: https://arxiv.org/html/2608.24703v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Equity Lead-Lag Harvesting via Time-Series Clustering: MiniRocket-KMeans, KShape, and Pairwise DTW Lag Matrix RowSum Partitioning

## Provenance

- **Primary Source:** Ruichen Deng and Yichi Zhang, *"Lead-Lag Relationships in Financial Markets: A Comparison of Multiple Clustering Algorithms"*, arXiv preprint `arXiv:2608.24703v1 [q-fin.ST]`, submitted August 25, 2026.
- **Authors & Affiliations:**
  - Ruichen Deng: School of Mathematical Sciences, Nankai University, China (email: `2311274@nankai.edu.cn`).
  - Yichi Zhang: Department of Statistics, University of Oxford, UK (email: `yichi.zhang@stats.ox.ac.uk`).
- **Canonical DOI:** [10.48550/arXiv.2608.24703](https://doi.org/10.48550/arXiv.2608.24703).
- **Traceable Source URLs:**
  - Abstract & Bibliographic record: [https://arxiv.org/abs/2608.24703](https://arxiv.org/abs/2608.24703)
  - Full Text HTML: [https://arxiv.org/html/2608.24703v1](https://arxiv.org/html/2608.24703v1)
- **Data Provenance:** Wharton Research Data Services (WRDS) CRSP Daily Stock Price History:
  - **Dataset 1 (679 Equities):** Daily closing prices from January 3, 2000 to December 31, 2019 (5,211 trading days).
  - **Dataset 2 (1,028 Equities):** Daily closing prices from January 31, 2000 to July 1, 2019 (4,880 trading days).

## Economic mechanism

### Source-reported

In modern equity markets, lead-lag relationships arise naturally due to structural heterogeneity among market participants: varying information acquisition costs, differing speeds of price discovery between large-cap/institutional favorites and small/mid-cap equities, and asynchronous order-flow execution. Traditional methods that estimate lead-lag networks via brute-force pairwise cross-correlation suffer from severe quadratic time complexity ($\mathcal{O}(n^2)$) and high statistical noise in sample correlation estimates.

The authors propose a multi-stage framework:
1. First, partition the broad asset universe into dynamically determined homogeneous clusters using efficient time-series clustering algorithms:
   - **DTW-KMedoids:** Dynamic Time Warping distance with medoid centroids (Zhang et al., 2023a).
   - **KShape:** Shape-Based Distance (SBD) invariant to scaling and phase shifts based on normalized cross-correlation (Paparrizos and Gravano, 2015).
   - **MiniRocket-KMeans:** Deterministic lightweight dilated convolutional kernels extracting Positive Part Value (PPV) features mapped into Euclidean space (Dempster et al., 2021).
   - **Ensemble:** Hard voting consensus clustering requiring pair agreement between DTW-KMedoids and KShape.
2. The optimal number of clusters $K^*$ is dynamically selected in each window by maximizing the average silhouette coefficient.
3. Within each cluster, a Dynamic Time Warping (DTW) alignment matrix is computed between all asset pairs to build an antisymmetric lead-lag matrix $\mathbf{M}$.
4. A RowSum ranking algorithm partitions each cluster into Leaders ($\mathcal{L}$) and Laggers ($\mathcal{G}$).
5. The core economic hypothesis is that the momentum of leading assets forecasts the subsequent returns of lagging assets due to delayed price adjustment (the "Lag strategy"), or alternatively, leading assets maintain persistent directional momentum (the "Lead strategy").

### Research interpretation

The proposed strategy is a **cross-sectional information diffusion / slow-moving order flow arbitrage hypothesis**:

1. **Information Transmission vs. Own-Momentum Dominance:** The theoretical justification for lead-lag extraction is that lagging assets underreact to common factor or industry news that is immediately priced into leading assets. However, the empirical results reveal an important structural divergence:
   - On the 679-asset universe, the **Lead Strategy** (trading the Leaders directly using their own signal) systematically outperforms the **Lag Strategy** across Sharpe ratio (0.866 vs 0.739 for MiniRocket-KMeans) and maximum drawdown ($-63.9\%$ vs $-144.2\%$).
   - This demonstrates that on a moderately sized universe, the detected edge is predominantly driven by **momentum persistence in liquid leaders** rather than profitable delay-harvesting in illiquid laggers.
2. **Clustering-Induced Dimensionality Reduction:** Applying MiniRocket or KShape before lead-lag detection serves as an unsupervised manifold filter. Assets in the same cluster share similar exposure to latent factors. Filtering pairwise DTW to intra-cluster pairs reduces spurious alignments between economically unrelated assets.
3. **Severe Universe Scalability Fragility:** Moving from 679 to 1,028 assets dramatically degrades strategy performance across all algorithms (Sharpe ratios drop from $0.6–0.8$ down to $0.15–0.47$; drawdowns explode past $-400\%$). In the 1,028 universe, the relationship inverts: the Lag strategy outperforms the Lead strategy (e.g., Ensemble lag Sharpe 0.474 vs Ensemble lead 0.251). This structural inversion indicates high sensitivity to marginal, less liquid names and demonstrates that the lead-lag boundaries are non-stationary.

## Signal

### Formation timestamp

- **Observation Schedule:** Daily at the close of trading ($t_{\text{close}} = 16:00$ US Eastern Time).
- **Signal Calculation:** Daily closing prices over a rolling sliding window of fixed length $l = 21$ trading days ($X_{n \times l}$) are gathered.
- **Tradability:** Orders are generated after the daily close $t$ for execution at the market open or next close ($t+1$).

### Lookback & Algorithmic Steps

For an equity matrix $X_{n \times T}$ representing closing prices of $n$ assets over $T$ days:

1. **Sliding Window Extraction:**
   Extract rolling sub-matrices of length $l = 21$ trading days:
   $$X_{n \times l}^{(t)} = [X_1^{(t-l+1:t)}, X_2^{(t-l+1:t)}, \dots, X_n^{(t-l+1:t)}]^{\top}$$

2. **Time-Series Clustering:**
   Inside each 21-day window, partition the $n$ assets into $K^*$ clusters using one of four algorithms:
   - **DTW-KMedoids:** Computes pairwise DTW warping costs:
     $$D_{\text{DTW}}(X_i, X_j) = \min_{\pi} \sum_{(p, q) \in \pi} |X_i[p] - X_j[q]|$$
     Centroids are actual sample time-series (medoids) minimizing sum of DTW distances.
   - **KShape:** Computes Shape-Based Distance (SBD) from normalized cross-correlation (NCC):
     $$\operatorname{SBD}(X, Y) = 1 - \max_{\tau} \frac{(X \star Y)[\tau]}{\|X\|_2 \|Y\|_2}$$
     where $\tau$ is time lag and $\star$ denotes cross-correlation. Cluster centroids are updated iteratively to maximize intra-cluster cross-correlation.
   - **MiniRocket-KMeans:** Applies $K_{\text{kernels}}$ fixed, lightweight random dilated convolution kernels to map each 21-day series $X_i$ to a feature vector in Euclidean space using the Positive Part Value (PPV):
     $$\operatorname{PPV}(C_k(X)) = \frac{1}{l - l_k \cdot d_k + 1} \sum_{t=1}^{l - l_k \cdot d_k + 1} \mathbb{I}\{C_k(X)[t] > 0\}$$
     where $l_k$ is kernel length, $d_k$ is dilation factor, and $\mathbb{I}$ is the indicator function. Standard KMeans is then applied to the resulting PPV representations.
   - **Ensemble:** Applies hard consensus voting: two assets $i$ and $j$ belong to the same cluster if and only if both DTW-KMedoids and KShape assign them to the same cluster ($L_{\text{DTW}}(i) = L_{\text{DTW}}(j) \land L_{\text{KShape}}(i) = L_{\text{KShape}}(j)$).

3. **Optimal Cluster Count Selection ($K^*$):**
   Evaluate candidate cluster counts $K$ by computing the average silhouette coefficient $S$:
   $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad S = \frac{1}{n}\sum_{i=1}^n s(i)$$
   where $a(i)$ is mean intra-cluster distance and $b(i)$ is mean distance to the nearest neighboring cluster. The optimal $K^*$ maximizes $S$.

4. **Pairwise DTW Lead-Lag Matrix Construction:**
   Within each cluster, apply DTW alignment to every asset pair $(i, j)$ to obtain local lag values $\delta_{ij}^k$ across alignment points $k=1, \dots, K$. Aggregate into global lag $\hat{L}_{ij}$ using:
   - **Mode Estimation (`mod`):**
     $$\hat{L}_{ij}^{\text{mod}} = \arg\max_v \operatorname{count}(\delta_{ij}^k = v)$$
   - **Median Estimation (`med`):**
     $$\hat{L}_{ij}^{\text{med}} = \operatorname{median}(\{\delta_{ij}^1, \dots, \delta_{ij}^K\})$$
   Construct the antisymmetric lead-lag matrix $\mathbf{M}$:
   $$\mathbf{M}[i, j] = \hat{L}_{ij} - \hat{L}_{ji}$$

5. **Leader / Lagger Partitioning:**
   Compute the global leading score $S_i$ by row-wise summation:
   $$S_i = \sum_{j} \mathbf{M}[i, j]$$
   Sort assets in descending order of $S_i$. The top $\alpha = 0.25$ fraction of assets with the lowest scores (most leading, representing earliest phase / negative relative lag) form the Leader set $\mathcal{L}$. The remaining $75\%$ form the Lagger set $\mathcal{G}$.

6. **Trading Signal Generation:**
   Compute the exponentially weighted moving average (EWMA) of the equal-weighted excess returns of the Leader set over span $p \in \{1, 3, 5, 7\}$ days:
   $$\text{signal}_t = \operatorname{sign}\left( \frac{1}{|\mathcal{L}|} \sum_{k \in \mathcal{L}} \operatorname{EWMA}(R_k, p) \right)$$
   where $\text{signal}_t \in \{-1, +1\}$.

7. **Target Portfolio Construction & Returns:**
   Two distinct execution branches:
   - **Lead Strategy:** Apply $\text{signal}_t$ to the Leader basket $\mathcal{L}$:
     $$\text{PnL}_t^{\text{lead}} = \text{signal}_t \cdot \left( \frac{1}{|\mathcal{L}|} \sum_{k \in \mathcal{L}} R_k(t + f) \right)$$
   - **Lag Strategy:** Apply $\text{signal}_t$ to the Lagger basket $\mathcal{G}$:
     $$\text{PnL}_t^{\text{lag}} = \text{signal}_t \cdot \left( \frac{1}{|\mathcal{G}|} \sum_{k \in \mathcal{G}} R_k(t + f) \right)$$
   where $f = 1$ is the forward execution horizon.

### Holding Period & Execution Rules

- **Rebalancing Cadence:** Daily sliding window shift ($w = 1$ trading day).
- **Holding Period:** 1 trading day per allocation step.
- **Position Allocation:** Equal-weighted across all active names in $\mathcal{L}$ or $\mathcal{G}$. Long when $\text{signal} = +1$, short when $\text{signal} = -1$.
- **Parameter Specification Gap:** In Algorithm 1 of the source paper, sliding step $w$ and forward step $f$ are written generally without fixed numerical values in the pseudocode header, but the empirical results evaluate daily steps ($w=1, f=1$).

## Required data

- **Instrument:** US Common Equities (CRSP universe).
- **Universe:** 
  - Sub-sample 1: 679 equities with continuous price history from 2000 to 2019.
  - Sub-sample 2: 1,028 equities with continuous price history from 2000 to 2019.
- **Venue:** NYSE, AMEX, NASDAQ (Wharton Research Data Services CRSP database).
- **Timeframe:** Daily frequency (closing prices).
- **Fields:** Daily closing prices $P_i(t)$, daily arithmetic/log returns $R_i(t)$.
- **Point-in-Time & Survivorship:** The sample requires continuous historical presence over the 20-year window (2000–2019), introducing survivorship selection bias.
- **Missing Data:** Null or non-trading days require forward-fill or exclusion; the source assumes complete daily matrices.
- **Frictions Data:** Zero commission, zero slippage, zero borrow rate, and zero bid-ask spread data are accounted for in the source paper.

## Execution assumptions

- **Execution Timing:** Next-day closing price ($t+1$) execution based on day-$t$ closing signals.
- **Order Types:** Modeled as friction-free market-on-close (MOC) or closing auction orders.
- **Transaction Costs:** 0 bps fees, 0 bps slippage, 0 bid-ask spread (frictionless assumption).
- **Shorting & Borrow:** Unconstrained short selling assumed across all 679 or 1,028 equities without borrow fees or locating constraints.
- **Position Sizing:** Equal weight across all constituent stocks in the active basket ($1/|\mathcal{L}|$ or $1/|\mathcal{G}|$).

## Evidence

### Source-reported

All figures, metrics, and parameters below are directly reported by Ruichen Deng and Yichi Zhang (arXiv:2608.24703v1, August 25, 2026, Section 4.4, Tables 2 and 3).

#### 1. Performance on 679 Assets (5,211 Trading Days, Jan 2000 – Dec 2019)

*Source: Table 2 in arXiv:2608.24703v1.*

| Algorithm | Strategy | Sharpe Ratio | Hit Rate | Max Drawdown (%) | Profit Loss Ratio | Annual Return (%) | Annual Volatility (%) | Sharpe P-Value |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DTW_KMedoids_mod** | lag | 0.706 | 0.517 | -122.703 | 1.065 | 5.12% | 7.26% | 0.0 |
| **DTW_KMedoids_med** | lag | 0.793 | 0.521 | -109.148 | 1.063 | 5.83% | 7.35% | 0.0 |
| **KShape_mod** | lag | 0.650 | 0.516 | -133.997 | 1.053 | 4.92% | 7.57% | 0.0 |
| **KShape_med** | lag | 0.579 | 0.514 | -125.684 | 1.049 | 4.42% | 7.63% | 0.0 |
| **MiniRocket_KMeans_mod** | lag | 0.689 | 0.517 | -114.118 | 1.058 | 5.07% | 7.36% | 0.0 |
| **MiniRocket_KMeans_med** | lag | 0.739 | 0.521 | -144.229 | 1.052 | 5.48% | 7.41% | 0.0 |
| **Ensemble_mod** | lag | 0.573 | 0.511 | -135.930 | 1.061 | 4.10% | 7.16% | 0.0 |
| **Ensemble_med** | lag | 0.609 | 0.518 | -132.002 | 1.040 | 4.41% | 7.25% | 0.0 |
| **DTW_KMedoids_mod** | lead | 0.715 | 0.517 | -71.518 | 1.064 | 5.21% | 7.29% | 0.0 |
| **DTW_KMedoids_med** | lead | 0.801 | 0.521 | -70.276 | 1.061 | 5.80% | 7.25% | 0.0 |
| **KShape_mod** | lead | 0.808 | 0.518 | -67.604 | 1.078 | 5.75% | 7.12% | 0.0 |
| **KShape_med** | lead | 0.790 | 0.515 | -69.418 | 1.089 | 5.60% | 7.08% | 0.0 |
| **MiniRocket_KMeans_mod** | lead | 0.769 | 0.521 | -67.066 | 1.058 | 5.54% | 7.20% | 0.0 |
| **MiniRocket_KMeans_med** | **lead** | **0.866** | **0.520** | **-63.908** | **1.079** | **6.21%** | **7.17%** | **0.0** |
| **Ensemble_mod** | lead | 0.643 | 0.515 | -67.094 | 1.060 | 4.65% | 7.24% | 0.0 |
| **Ensemble_med** | lead | 0.679 | 0.519 | -67.879 | 1.050 | 4.89% | 7.20% | 0.0 |

*Key source-reported observations (679 assets):*
- MiniRocket-KMeans with median lag estimation under the **Lead Strategy** achieves the highest Sharpe ratio ($0.866$), highest annual return ($6.21\%$), and smallest maximum drawdown ($-63.908\%$).
- In all clustering algorithms, the Lead strategy significantly outperforms the Lag strategy (lower drawdowns by $\approx 50–75$ percentage points).
- Median lag aggregation (`med`) consistently outperforms mode aggregation (`mod`) across almost all models.

#### 2. Performance on 1,028 Assets (4,880 Trading Days, Jan 2000 – Jul 2019)

*Source: Table 3 in arXiv:2608.24703v1.*

| Algorithm | Strategy | Sharpe Ratio | Hit Rate | Max Drawdown (%) | Profit Loss Ratio | Annual Return (%) | Annual Volatility (%) | Sharpe P-Value |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DTW_KMedoids_mod** | lag | 0.371 | 0.502 | -843.835 | 1.061 | 3.00% | 8.08% | 0.0 |
| **DTW_KMedoids_med** | lag | 0.353 | 0.500 | -400.600 | 1.065 | 2.88% | 8.16% | 0.0 |
| **KShape_mod** | lag | 0.321 | 0.515 | -259.902 | 0.998 | 2.69% | 8.36% | 0.0 |
| **KShape_med** | lag | 0.373 | 0.510 | -142.985 | 1.024 | 3.14% | 8.42% | 0.0 |
| **MiniRocket_KMeans_mod** | lag | 0.405 | 0.510 | -1161.520 | 1.033 | 3.36% | 8.30% | 0.0 |
| **MiniRocket_KMeans_med** | lag | 0.307 | 0.502 | -635.786 | 1.048 | 2.56% | 8.35% | 0.0 |
| **Ensemble_mod** | **lag** | **0.474** | **0.509** | **-751.317** | **1.048** | **3.85%** | **8.13%** | **0.0** |
| **Ensemble_med** | lag | 0.447 | 0.508 | -451.613 | 1.047 | 3.66% | 8.20% | 0.0 |
| **DTW_KMedoids_mod** | lead | 0.156 | 0.505 | -566.770 | 1.008 | 1.32% | 8.52% | 0.0 |
| **DTW_KMedoids_med** | lead | 0.188 | 0.505 | -735.014 | 1.013 | 1.60% | 8.49% | 0.0 |
| **KShape_mod** | lead | 0.189 | 0.507 | -1766.753 | 1.004 | 1.59% | 8.40% | 0.0 |
| **KShape_med** | lead | 0.267 | 0.510 | -1029.415 | 1.008 | 2.24% | 8.38% | 0.0 |
| **MiniRocket_KMeans_mod** | lead | 0.220 | 0.509 | -1071.332 | 1.002 | 1.85% | 8.38% | 0.0 |
| **MiniRocket_KMeans_med** | lead | 0.160 | 0.505 | -629.837 | 1.006 | 1.33% | 8.36% | 0.0 |
| **Ensemble_mod** | lead | 0.251 | 0.509 | -471.088 | 1.008 | 2.13% | 8.48% | 0.0 |
| **Ensemble_med** | lead | 0.227 | 0.505 | -542.783 | 1.017 | 1.92% | 8.46% | 0.0 |

*Key source-reported observations (1,028 assets):*
- Performance collapses when expanding the universe: all Sharpe ratios drop by $50–80\%$ (from $0.7–0.8$ down to $0.15–0.47$).
- Maximum drawdowns explode to catastrophic levels ($-142\%$ to $-1,766\%$), reflecting severe unmitigated equity downside risk.
- Under the larger universe, the Ensemble algorithm demonstrates superior stability, leading the pack with Sharpe $0.474$ (lag strategy).

### Independently reproduced

`Not independently reproduced.` Findings are transcribed directly from Deng & Zhang (arXiv:2608.24703v1).

### Negative evidence

1. **Fatal Sensitivity to Transaction Costs:** The reported gross annualized returns are modest ($1.32\%–6.21\%$) while requiring daily rebalancing across baskets of hundreds of stocks. In reality, US equity trading incurs bid-ask spreads, exchange fees, and borrow fees for short legs. At a conservative friction of $5–10\text{ bps}$ per round trip, daily turnover exceeding $200\%\text{–}400\%$ annually would consume $100–400\text{ bps}$ of performance, rendering net returns negative and destroying all claimed statistical significance.
2. **Universe Scalability Degradation:** The sharp drop in Sharpe ratio when moving from 679 to 1,028 assets (MiniRocket lead dropping from $0.866$ to $0.160$) reveals that expanding the investment universe introduces noisy, illiquid, or non-stationary relationships that corrupt the lead-lag matrix.
3. **Catastrophic Unmitigated Drawdowns:** The recorded maximum drawdowns (ranging from $-63.9\%$ on 679 assets to an astonishing $-1,766\%$ on 1,028 assets) indicate that equal-weighted unhedged long/short portfolios generated by sign-only EWMA suffer severe tail blowups during major market shocks (e.g., 2000–2002 dot-com bust, 2008 GFC).
4. **Hypothesis Contradiction (Lead vs. Lag Inversion):** On 679 assets, trading the Leaders directly outperforms trading the Laggers. On 1,028 assets, trading the Laggers outperforms trading the Leaders. This behavioral inversion indicates that the underlying mechanism is not a persistent economic lead-lag transmission law, but rather an unstable regime- and universe-dependent artifact.
5. **Survivorship Bias:** The requirement of continuous daily closing price availability across the entire 20-year span (January 2000 to December 2019) unconditionally eliminates all bankrupt, acquired, or newly listed firms, introducing extreme survivorship bias.

## Falsification plan

1. **Transaction Cost & Slippage Hurdle Test:**
   - **Protocol:** Re-simulate the 679-asset and 1,028-asset backtests applying an explicit fee, spread, and market impact schedule of $5\text{ bps}$, $10\text{ bps}$, and $20\text{ bps}$ per trade.
   - **Decision Rule:** If the annualized net return of the top-performing configuration (MiniRocket_KMeans_med lead) falls below $0.0\%$ under a $10\text{ bps}$ friction assumption, the hypothesis of tradable economic alpha is falsified.
2. **Subsampling Universe Stability Test:**
   - **Protocol:** Draw 100 random sub-samples of 500 stocks from the 1,028 universe and evaluate the strategy across the 2000–2019 history.
   - **Decision Rule:** If the interquartile range (IQR) of annualized Sharpe ratios crosses zero, or if fewer than $50\%$ of the sub-samples achieve Sharpe $> 0.3$, falsify the claim that time-series clustering identifies stable, robust lead-lag structures.
3. **Time-Shifted Leader Placebo Test:**
   - **Protocol:** Artificially shift the returns of the Leader set $\mathcal{L}$ forward in time by $+3$ to $+10$ days before calculating the EWMA signal, breaking any genuine economic causal lead over the Lagger set $\mathcal{G}$.
   - **Decision Rule:** If the synthetic placebo signal generates a Sharpe ratio within $\pm 0.15$ of the true signal on the Lag strategy, falsify the hypothesis that the DTW RowSum partition extracts genuine temporal causality.
4. **Execution Delay Degradation Test:**
   - **Protocol:** Introduce a 1-day execution latency (generating the signal at close $t$, executing at close $t+2$ instead of $t+1$).
   - **Decision Rule:** If the hit rate decays to $50.0\% \pm 0.2\%$ and Sharpe drops below $0.1$, confirm that the observed relationship is an ultra-short-term statistical artifact with zero execution tolerance.

## Crypto portability

**Adapted / Unproven.** The source paper investigates exclusively US equities (CRSP) from 2000 to 2019 and does not test cryptocurrency assets.

Porting cross-sectional lead-lag clustering to cryptocurrency markets involves substantial structural differences and severe risks:

1. **Absence of Uniform Cash Session Closes:** Crypto trades 24/7/365 without an official NYSE/NASDAQ 16:00 close. A crypto adaptation must impose arbitrary daily snapshot boundaries (e.g., UTC 00:00). Microsecond phase shifts across global liquidity hubs (Binance, Bybit, OKX, Coinbase) mean that daily bar DTW will miss high-frequency cross-venue lead-lag dynamics that operate on milliseconds to minutes.
2. **Extreme Market-Beta & BTC Dominance:** Unlike equities, where 500+ stocks exhibit distinct sector factor structures, the cryptocurrency universe is heavily dominated by Bitcoin (BTC) and Ethereum (ETH). Cross-sectional clustering on 100+ altcoins typically produces a degenerate single cluster dominated by BTC beta, rendering intra-cluster leader/lagger partitions economically trivial.
3. **Perpetual Funding Rate Drag:** In crypto perpetual futures, shorting lagging altcoins or longing leading assets incurs perpetual funding payments that can exceed $20\%–50\%$ annualized during strong trend or crowded market regimes, rapidly erasing any marginal daily return ($1\%–6\%$).
4. **Catastrophic Tail Risk in Altcoins:** Altcoin liquidity drops exponentially outside the top 10 assets. Equal-weighted baskets across hundreds of crypto tokens suffer from frequent rug-pulls, exchange delistings, and severe slippage that would amplify the already extreme equity drawdowns ($-1,766\%$) into total portfolio wipeouts.

## Limitations

- **Zero Transaction Cost Assumption:** The source paper models zero friction, which invalidates the practical viability of a daily rebalanced multi-asset strategy.
- **Survivorship Bias:** Conditioning on 20 years of continuous CRSP price history excludes distressed and bankrupt firms.
- **Catastrophic Drawdown Profile:** Unhedged sign-based EWMA positioning generates unacceptable tail drawdowns exceeding $-60\%$ to $-1,000\%$.
- **Parameter Underspecification:** The exact values of sliding step $w$ and forward step $f$ are omitted in the pseudocode description of Algorithm 1.
- **Inconsistent Economic Mechanism:** The reversal of Lead vs. Lag strategy dominance between 679 and 1,028 assets demonstrates non-stationarity.
- **No Independent Reproduction:** Results rely solely on the reported tables of the preprint.

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been performed.

## Adoption boundary

`research-only`. This capture serves as a normalized research record and comparative benchmark for time-series clustering algorithms. It is not an approved trading strategy, does not guarantee positive net return, and does not authorize deployment in paper, testnet, or live environments.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/cross-sectional-equity-statistical-arbitrage]]`
- `[[quant/lead-lag-information-diffusion-microstructure]]`
- `[[quant/time-series-momentum-deep-learning-changepoint]]`

## Sources

1. Ruichen Deng and Yichi Zhang, *"Lead-Lag Relationships in Financial Markets: A Comparison of Multiple Clustering Algorithms"*, arXiv preprint `arXiv:2608.24703v1 [q-fin.ST]`, submitted August 25, 2026. DOI: [10.48550/arXiv.2608.24703](https://doi.org/10.48550/arXiv.2608.24703). Stable URL: [https://arxiv.org/abs/2608.24703](https://arxiv.org/abs/2608.24703). Full text HTML: [https://arxiv.org/html/2608.24703v1](https://arxiv.org/html/2608.24703v1).
2. Y. Zhang, M. Cucuringu, A. Y. Shestopaloff, and S. Zohren, *"Dynamic time warping for lead-lag relationships in lagged multi-factor models"*, arXiv preprint `arXiv:2309.08800`, 2023.
3. J. Paparrizos and L. Gravano, *"k-Shape: efficient and accurate clustering of time series"*, Proceedings of the 2015 ACM SIGMOD International Conference on Management of Data, pp. 1855–1870, 2015.
4. A. Dempster, D. F. Schmidt, and G. I. Webb, *"MiniRocket: a very fast (almost) deterministic transform for time series classification"*, Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 248–257, 2021.
