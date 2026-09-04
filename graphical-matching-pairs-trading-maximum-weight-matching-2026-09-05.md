---
schema: strategy-research-record-v1
title: "Graphical Matching Pairs Trading: Covariance Mitigation via Maximum Weight Matching on Cointegration Graphs"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - cointegration
  - graph-theory
  - maximum-weight-matching
  - portfolio-variance-reduction
  - equities
status: research-only
confidence: high
source_as_of: 2024-03-12
sources:
  - "Khizar Qureshi and Tauhid Zaman, 'Pairs Trading Using a Novel Graphical Matching Approach', arXiv:2403.07998v1 [stat.AP], March 12, 2024. https://arxiv.org/abs/2403.07998"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Graphical Matching Pairs Trading: Covariance Mitigation via Maximum Weight Matching on Cointegration Graphs

## Provenance

- **Primary Academic Source:** Khizar Qureshi (Massachusetts Institute of Technology, Department of Electrical Engineering and Computer Science, Cambridge, MA, USA; `kqureshi@mit.edu`) and Tauhid Zaman (Yale School of Management, Yale University, New Haven, CT, USA; `tauhid.zaman@yale.edu`), *"Pairs Trading Using a Novel Graphical Matching Approach"*, arXiv preprint `arXiv:2403.07998v1 [stat.AP]`, submitted March 12, 2024.
  - Canonical arXiv Abstract: [https://arxiv.org/abs/2403.07998](https://arxiv.org/abs/2403.07998)
  - Canonical DOI: [https://doi.org/10.48550/arXiv.2403.07998](https://doi.org/10.48550/arXiv.2403.07998)
  - Full-Text HTML: [https://arxiv.org/html/2403.07998v1](https://arxiv.org/html/2403.07998v1)
  - Primary LaTeX Package: `https://arxiv.org/src/2403.07998` (audited directly from unpacked source files `pairs_or.tex` and empirical tables).
- **Code Reference in Paper:** The primary text cites an associated GitHub repository `https://github.com/kai-trading-bot/pair/` (accessed April 30, 2023 in the paper). Independent live verification via HTTP inspection returns 404 (repository missing or made private). All mathematical specifications, graph formulations, signal equations, and empirical tables were audited and verified directly from the authors' primary LaTeX source.
- **Pre-Write Deduplication & Identity Verification:** An exhaustive scan across all 370+ markdown strategy captures in `alpha-strategy-research` confirmed zero existing records matching `2403.07998`, `Khizar Qureshi`, `Tauhid Zaman`, `maximum weight matching`, or `graphical matching`. Existing pairs trading records in the repository focus on deep reinforcement learning execution overlays (`crypto-drl-execution-overlay-multi-pair-trading-2026-09-01`), factor-augmented volatility models (`crypto-factor-augmented-volatility-pairs-trading-2026-09-01`), copula dependence (`crypto-pairs-trading-copula-cointegration-2026-08-31`), and path signature decomposition (`path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03`). None of the existing records address the shared-asset covariance distortion in multi-pair portfolios or utilize Edmonds' maximum weight matching algorithms to structurally eliminate portfolio variance.

## Economic mechanism

### Source-reported

1. **The Shared-Asset Covariance Problem in Multi-Pair Portfolios:** Traditional pairs trading strategies select candidate asset pairs by testing for cointegration (e.g., Engle-Granger or single-lag Augmented Dickey-Fuller) and forming a portfolio from the pairs exhibiting the smallest p-values or most negative t-statistics. In large equity universes (such as the S&P 500 with $N=500$ stocks and 124,750 potential pairs), top cointegrated pairs heavily cluster around a small set of common "hub" stocks. For example, stock 1 may appear simultaneously in pair $(1, 2)$ and pair $(1, 3)$. When distinct pairs share a common asset, their spread returns exhibit a strictly positive covariance ($\Cov(r_{at}, r_{bt}) > 0$). In empirical S&P 500 data (January 2021 to August 2023), selecting the top 250 pairs based purely on ADF p-values yields a median of $m_2 = 1,748$ pairs of pairs that share an asset, with individual stocks appearing in up to 15 (and at times exceeding 100) pairs simultaneously. Random graph theory ($G(n, p)$ Erdos-Renyi) predicts only 249.5 shared-asset pairs of pairs, proving that statistical cointegration clusters severely around specific assets.
2. **Analytical Proof of Covariance Inflation:** The authors establish analytical formulas for the mean, variance, and cross-pair covariance of returns:
   - For cointegrated pairs sharing stock 1, Theorem 3.2 proves that the cross-pair covariance is:
     $$\Cov(r^a_t, r^b_t) = \left(e^{\sigma_1^2} - 1\right) \mathbb{E}[r_{at}] \mathbb{E}[r_{bt}]$$
     Since cointegrated pairs have positive expected return ($\mathbb{E}[r_t] > 0$), this covariance is strictly positive.
   - For non-cointegrated pairs sharing stock 1, Theorem 3.4 proves that even though their individual expected return is zero ($\mathbb{E}[r_t] = 0$), the cross-pair covariance is strictly positive due to the correlated noise shock $\sigma_1^2$.
   - In a portfolio of $n_1$ cointegrated pairs and $n_2$ non-cointegrated pairs with $m_1$ shared cointegrated pairs and $m_2$ shared non-cointegrated pairs, the total portfolio variance is:
     $$\Var(R_t) = n_1 \nu_1 + n_2 \nu_2 + 2 m_1 \kappa_1 + 2 m_2 \kappa_2$$
     In the baseline cointegration-ranked portfolio, the covariance terms ($2 m_2 \kappa_2$) account for approximately 50% of the entire portfolio variance.
3. **Graph-Theoretic Matching Solution:** To eliminate the covariance drag, the authors formulate pair selection as a Maximum Weight Matching (MWM) on a complete weighted pairs graph $G=(V, E)$, where vertices $V$ are assets, edges $E$ are all potential pairs, and edge weights are the negative ADF t-statistics ($w_{ij} = -t_{ij}^{\text{ADF}}$). A matching is a subgraph where each vertex has degree at most 1 (each asset is included in at most one pair). Solving for the maximum weight matching via Edmonds' blossom algorithm maximizes the aggregate cointegration strength across the portfolio while strictly enforcing $m_1 = 0$ and $m_2 = 0$. This halves portfolio variance and limits single-stock idiosyncratic risk to exactly 1 pair by construction.

### Research interpretation

1. **Structural Idiosyncratic Firewall:** In traditional relative-value and statistical arbitrage, multi-pair portfolios frequently suffer from hidden concentration risk: when an idiosyncratic shock (such as a regulatory action, accounting restatement, or management crisis) hits a central hub stock, every pair containing that stock diverges simultaneously, causing multi-leg drawdowns and margin liquidation cascades. Maximum weight matching serves as an ex-ante structural firewall that decorrelates pair spreads at the asset level.
2. **Outlier-Robust Quantile Normalization (Q-Score):** The standard z-score normalization standardizes residual spreads by the sample standard deviation, which is vulnerable to volatility clustering and single outlier spikes. The proposed Q-score normalizes residuals by the interquartile range ($\text{IQR} = \tau_{75} - \tau_{25}$) and discretizes positions via integer rounding ($[|q_{at}|]$). This dynamically establishes an inner dead-band ($[|q_{at}|] = 0$ for $|q_{at}| < 0.5$) while scaling capital into larger deviations without requiring heuristic multiplier tuning.
3. **Turnover Reduction and Cost Feasibility:** By preventing the portfolio from continuously flipping positions across dozens of redundant pairs tied to the same volatile stocks, the matching approach reduces portfolio turnover by approximately 66% (median turnover 1/3 of the baseline), allowing the strategy to preserve positive net returns after transaction costs where the naive cointegration baseline is rendered unprofitable.

## Signal

The strategy consists of a two-stage pipeline: (1) monthly portfolio graph construction and maximum weight matching pair selection, and (2) daily pair spread estimation, outlier-robust signal generation, and integer position sizing.

### 1. Portfolio Construction via Maximum Weight Matching (`source-reported`)

At the beginning of each calendar month:
1. **Universe & Historical Lookback:** Select the universe of $N$ eligible stocks (S&P 500, $N \approx 500$; `source-reported`). Use a sliding historical lookback window of 2 years (504 trading days; `source-reported`).
2. **Pair Regression & Cointegration Estimation:** For every candidate pair $a = (i, j)$ among the $N(N-1)/2$ possible combinations:
   - Estimate the OLS log-price cointegration relationship:
     $$\log(p_{jt}) = \mu_a + \beta_a \log(p_{it}) + \epsilon_{at} \quad (\text{source-reported})$$
   - Extract the residual spread time series $\epsilon_{at}$ and its estimated variance $\sigma_a^2$ (`source-reported`).
   - Run a single-lag Augmented Dickey-Fuller (ADF) stationarity test on the residual spread $\epsilon_{at}$ to obtain the test statistic $t_a^{\text{ADF}}$ and its corresponding p-value (`source-reported`).
3. **Pairs Graph Representation:**
   - Construct a complete undirected graph $G = (V, E)$, where the vertex set $V$ represents the $N$ stocks, and the edge set $E$ contains an edge for every stock pair $(i, j)$ (`source-reported`).
   - Assign edge weights $w_{ij}$ equal to the negative of the ADF t-statistic:
     $$w_{ij} = -t_{ij}^{\text{ADF}} \quad (\text{source-reported})$$
     Since more negative t-statistics indicate stronger rejection of the unit root (stronger cointegration), larger positive edge weights correspond to superior pair candidates (`source-reported`).
4. **Maximum Weight Matching Optimization:**
   - Solve for the maximum weight matching $M^* \subset E$ on the pairs graph:
     $$\max_{M \subseteq E} \sum_{e \in M} w_e \quad \text{subject to} \quad \text{deg}_M(v) \leq 1 \quad \forall v \in V \quad (\text{source-reported})$$
   - The optimization is solved using Edmonds' blossom algorithm / primal-dual matching method, with polynomial time complexity $O(V^2 E)$ (Edmonds 1965, Galil 1986; `source-reported`).
   - The resulting matching portfolio $M^*$ contains at most $\lfloor N/2 \rfloor$ pairs (up to 250 pairs for $N=500$), where no two pairs share any common stock (`source-reported`).

### 2. Daily Trading Signals & Execution Logic (`source-reported`)

During the active month, each selected pair $a = (i, j) \in M^*$ is traded daily:
1. **Daily Residual Update:** On each trading day $t$, re-estimate the log-price regression over the sliding 2-year window leading up to date $t$:
   $$\log(p_{jt}) = \mu_a + \beta_a \log(p_{it}) + \epsilon_{at} \quad (\text{source-reported})$$
   Obtain the latest residual $\epsilon_{at}$ (`source-reported`).

2. **Signal Model A: Winsorized Z-Score ($S^z_{at}$; `source-reported`):**
   - Compute standardized z-score: $z_{at} = \epsilon_{at} / \sigma_a$ (`source-reported`).
   - Winsorize $z_{at}$ at the interval $[-3.0, +3.0]$ to truncate extreme outliers (`source-reported`).
   - Signal generation with trading threshold $k = 2.0$ (`source-reported`):
     $$S_{at}^z = \mathbbm{1}_{\{\epsilon_{at} \leq -k \sigma_a\}} - \mathbbm{1}_{\{\epsilon_{at} \geq k \sigma_a\}} \quad (\text{source-reported})$$
   - Asset execution rules:
     - $S_{at}^z = +1$ (spread undervalued; stock $j$ cheap relative to stock $i$): Buy $\$1$ of stock $j$, short $\$ \beta_a$ of stock $i$ (`source-reported`).
     - $S_{at}^z = -1$ (spread overvalued; stock $j$ expensive relative to stock $i$): Buy $\$ \beta_a$ of stock $i$, short $\$1$ of stock $j$ (`source-reported`).
     - $S_{at}^z = 0$: Close existing positions or remain flat (`source-reported`).

3. **Signal Model B: Outlier-Robust Quantile Q-Score ($S^q_{at}$; `source-reported`):**
   - Let $\tau_k(\epsilon_{at})$ be the $k$-th percentile of historical regression residuals over the 2-year window (`source-reported`).
   - Calculate the Q-score:
     $$q_{at} = \frac{\epsilon_{at} - \tau_{50}(\epsilon_{at})}{\tau_{75}(\epsilon_{at}) - \tau_{25}(\epsilon_{at})} \quad (\text{source-reported})$$
     where the numerator subtracts the median spread and the denominator is the interquartile range ($\text{IQR}$) (`source-reported`).
   - Compute the integer-rounded directional signal and position weight:
     $$S_{at}^q = \left( -\mathbbm{1}_{\{q_{at} \leq 0\}} + \mathbbm{1}_{\{q_{at} \geq 0\}} \right) [|q_{at}|] \quad (\text{source-reported})$$
     where $[|q_{at}|]$ denotes rounding $|q_{at}|$ to the nearest integer (`source-reported`).
   - Operational behavior:
     - If $|q_{at}| < 0.5$, $[|q_{at}|] = 0$: no position is taken (natural dead-band; `source-reported`).
     - If $q_{at} \leq -0.5$: buy $\$[|q_{at}|]$ of stock $j$, short $\$([|q_{at}|] \cdot \beta_a)$ of stock $i$ (`source-reported`).
     - If $q_{at} \geq 0.5$: buy $\$([|q_{at}|] \cdot \beta_a)$ of stock $i$, short $\$[|q_{at}|]$ of stock $j$ (`source-reported`).
     - Larger deviations receive integer weight scaling ($1\times, 2\times, 3\times$) proportional to dislocation severity (`source-reported`).

4. **Execution Timing & Portfolio Weighting:**
   - In theoretical derivations, unit capital is allocated to each pair (`source-reported`).
   - In simulation, daily returns are aggregated across active pairs (`source-reported`).
   - Signal-to-order execution lag: Daily close mark (`source-reported`). A 1-bar execution delay (entry on next-day open/VWAP) is `research-proposed`.

## Required data

- **Universe:** S&P 500 constituent common equities (`source-reported`).
- **Venue:** US Equity National Market System (NYSE, NASDAQ; `source-reported`).
- **Market Type:** Cash equity (spot; `source-reported`).
- **Timeframe:** Daily closing bars (`source-reported`).
- **Price Fields:** Daily closing prices adjusted for corporate actions, cash dividends, and stock splits (`source-reported`).
- **Data Period in Primary Study:** January 2010 to August 2023 for moment parameter estimation; January 2017 to May 2023 for out-of-sample trading simulations (`source-reported`).
- **History Requirement:** Minimum 2 years (504 consecutive trading days) of daily adjusted close prices for regression estimation and ADF cointegration testing (`source-reported`).
- **Point-in-Time Considerations:** Survivorship bias handling in historical index constituents is not explicitly detailed in the source (`provenance gap`).

## Execution assumptions

- **Order Timing & Type:** Daily evaluations based on closing prices; orders assumed executed at the closing price on day $t$ (`source-reported`). Next-day market-on-open (MOO) or VWAP execution is `research-proposed`.
- **Fill Model:** Frictionless instantaneous fill at closing price assumed in primary simulation (`source-reported`).
- **Transaction Cost Model:** Annual transaction cost modeled at 1.0% per stock, converted into a daily fee of $1\% / 252 = 0.00397\%$ per trading day deducted from daily pair returns whenever positions are held (`source-reported`).
  - *Provenance Note:* This fee structure acts as a flat holding-cost proxy rather than a per-trade ticket commission or bid-ask spread crossing cost (`provenance gap`). A realistic per-trade slippage model of 5 to 10 bps per side is `research-proposed`.
- **Short Borrow & Financing:** Frictionless short borrowing assumed; borrow fees, rebate rates, and hard-to-borrow constraints are omitted in the source (`provenance gap`).
- **Leverage & Capital Allocation:** Capital allocated proportionally based on regression hedge ratio $\beta_a$ (`source-reported`). Cash interest and margin leverage requirements are omitted (`provenance gap`).
- **Capacity & Participation:** Large-cap S&P 500 equities imply high dollar capacity, but formal market impact models are omitted in the source (`provenance gap`).

## Evidence

### Source-reported

All quantitative metrics and empirical findings below are transcribed directly from the primary LaTeX source of Qureshi & Zaman (2024, arXiv:2403.07998v1), covering S&P 500 equities from January 2017 to May 2023:

#### 1. Theoretical Parameter Estimation & Variance Decomposition (Table 1; `source-reported`)
Using daily log-price data from 2010 to 2023 and monthly 250-pair universes from January 2021 to August 2023:
- Median daily log-price return mean: $\mu_1 = 0.0005$ (`source-reported`).
- Median daily log-price return standard deviation: $\sigma_1 = 0.0180$ (`source-reported`).
- Median spread residual standard deviation: $\sigma = 0.0711$ (`source-reported`).
- Signal threshold: $k = 2.0$ (`source-reported`).
- Modeled pair portfolio composition: $n_1 = 1$ cointegrated pair, $n_2 = 249$ non-cointegrated pairs (`source-reported`).
- Cointegrated shared pairs: $m_1 = 0$ for both Baseline and Matching (`source-reported`).
- Non-cointegrated shared pairs: $m_2 = 1,748$ for Baseline vs. $m_2 = 0$ for Matching (`source-reported`).
- **Theoretical Annualized Sharpe Ratio:**
  - Baseline Portfolio: **0.50** (`source-reported`).
  - Matching Portfolio: **1.18** (`source-reported`).
  - The shared-asset covariance term ($2 m_2 \kappa_2$) accounts for 50% of the total variance in the Baseline portfolio (`source-reported`).

#### 2. Gross Performance Comparison (Table 2; `source-reported`)
Performance across four strategies—Matching Q-score (MQ), Matching Z-score (MZ), Baseline Q-score (BQ), Baseline Z-score (BZ)—benchmarked against the S&P 500 (January 2017 – May 2023):

| Strategy | Gross Sharpe Ratio | Gross Sortino Ratio | Gross Cumulative Return (%) | Gross Annualized Return (%) | Min Single Day Return (%) | Max Single Day Return (%) | Skew | Max Drawdown (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **MQ (Matching Q-score)** | **1.23** | **1.78** | **73.65%** | **8.40%** | **-3.81%** | **4.20%** | **1.12** | **-7.99%** |
| **MZ (Matching Z-score)** | **1.23** | **1.69** | **74.87%** | **8.42%** | **-4.16%** | **4.13%** | **0.83** | **-8.30%** |
| **BQ (Baseline Q-score)** | 0.34 | 0.44 | 17.96% | 2.49% | -3.93% | 3.49% | -0.28 | -6.94% |
| **BZ (Baseline Z-score)** | 0.48 | 0.67 | 38.30% | 5.13% | -4.63% | 4.99% | 0.04 | -8.48% |
| **S&P 500 Benchmark** | 0.59 | 0.70 | 88.25% | 10.79% | -10.94% | 9.06% | -0.55 | -19.49% |

#### 3. Net Performance Comparison (Table 3; `source-reported`)
Factoring in daily transaction costs of $1\% / 252 = 0.00397\%$ per day active:

| Strategy | Net Sharpe Ratio | Net Sortino Ratio | Net Cumulative Return (%) | Net Annualized Return (%) | Min Single Day Return (%) | Max Single Day Return (%) | Skew | Max Drawdown (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **MQ (Matching Q-score)** | **1.12** | **1.63** | **64.73%** | **7.64%** | **-3.82%** | **4.18%** | **1.12** | **-8.00%** |
| **MZ (Matching Z-score)** | **1.12** | **1.55** | **66.34%** | **7.25%** | **-4.17%** | **4.13%** | **0.82** | **-8.30%** |
| **BQ (Baseline Q-score)** | -0.49 | -0.64 | -26.15% | -4.11% | -4.01% | 4.90% | -0.31 | -6.90% |
| **BZ (Baseline Z-score)** | -0.13 | -0.18 | -13.40% | -1.65% | -4.67% | 3.44% | 0.03 | -8.40% |
| **S&P 500 Benchmark** | 0.59 | 0.70 | 88.25% | 10.79% | -10.94% | 9.06% | -0.55 | -19.49% |

#### 4. Strategy Correlation Matrix & Market Tail Protection (Table 4; `source-reported`)
- Correlation with S&P 500: MQ has $-0.27$, MZ has $-0.25$, BQ has $-0.17$, BZ has $-0.14$ (`source-reported`).
- During major market crashes, the matching strategy exhibited negative correlation and strong positive returns:
  - **March 2020 (COVID-19 Crash):** S&P 500 returned $-35\%$, while Matching approach returned $+15\%$ (`source-reported`).
  - **Full Year 2022 (Bear Market):** S&P 500 returned $-18\%$, while Matching approach returned $+10\%$ (`source-reported`).
- Correlation between MQ and MZ: $0.91$ (`source-reported`).
- Correlation between Matching and Baseline: $0.50$ (MQ vs. BQ) and $0.37$ (MZ vs. BZ), confirming that graph matching selects fundamentally distinct asset subsets (`source-reported`).

#### 5. Ex-Ante Structural Metrics (`source-reported`)
- **Turnover:** The Matching method exhibits a median monthly asset turnover approximately one-third as large as the Baseline method (`source-reported`).
- **Concentration:** Baseline portfolio concentration (maximum appearances of any single stock across pairs) averages 10.2 and exceeds 100 during certain regimes; Matching concentration is strictly 1.0 by definition (`source-reported`).
- **Retention (Jaccard Index):** Matching portfolio consistently exhibits lower retention between monthly updates, confirming higher portfolio diversity and reduced exposure to stale pairs (`source-reported`).

### Independently reproduced

`not independently reproduced`.
Mathematical derivations, loss equations, graph matching formulations, and empirical tables were inspected directly from the primary LaTeX source of `arXiv:2403.07998v1`, but the strategy has not been executed within our internal research environment.

### Negative evidence

1. **Transaction Cost Destruction of Baseline:** In the absence of graphical matching, the standard cointegration selection pipeline collapses under realistic trading costs. Baseline net annualized returns are negative ($-4.11\%$ for BQ, $-1.65\%$ for BZ) with negative net Sharpe ratios ($-0.49$ and $-0.13$), demonstrating that high turnover in overlapping pairs destroys alpha.
2. **Simplified Cost Modeling Risk:** The primary study models transaction costs as a continuous daily holding drag ($0.00397\%$/day) rather than a per-trade ticket fee, exchange commission, and bid-ask spread crossing cost. For high-frequency intraday rebalancing or illiquid stocks, per-trade turnover costs could be significantly more penalizing than a static 1% annual fee.
3. **Suboptimal Pair Pruning by MWM:** Maximum Weight Matching maximizes total aggregate edge weight across the graph. Consequently, a highly cointegrated pair with an exceptional t-statistic (e.g., $w_{1,2} = 10$) may be rejected if matching stock 1 with stock 3 ($w_{1,3} = 6$) and stock 2 with stock 4 ($w_{2,4} = 6$) yields a higher combined weight ($12 > 10$). This structural property occasionally forces the exclusion of the single strongest individual pair.
4. **Survivorship Bias in S&P 500 Snapshot:** The paper evaluates S&P 500 constituents from 2017 to 2023. If index membership is back-filled using a static constituent list, survivorship bias could artificially inflate pair cointegration stability.

## Falsification plan

1. **Per-Trade Fee & Bid-Ask Spread Attrition Stress Test:**
   Replace the paper's 1% annual holding cost proxy with realistic per-trade transaction costs: 5 bps, 10 bps, and 20 bps per traded dollar on every entry, exit, and rebalance action, combined with a 2 bps half-spread.
   - `research-defined falsification threshold`: If the net annualized Sharpe ratio of the Matching Q-score strategy drops below 0.50 under a conservative 10 bps per-side execution cost, the strategy is falsified as an economically viable standalone equity statistical arbitrage strategy.

2. **Next-Day Open / VWAP Execution Lag Audit:**
   The primary paper assumes orders are filled at the same day's closing price as signal formation. Implement an explicit 1-bar execution delay: calculate signals at date $t$ market close, and execute orders at date $t+1$ market-on-open (MOO) or 30-minute VWAP.
   - `research-defined falsification threshold`: If the out-of-sample net Sharpe ratio degrades by more than 40% when executing at next-day open versus same-day close, the apparent performance is falsified as look-ahead bias from simultaneous close execution.

3. **Multiple Hypothesis Testing & Cointegration Stability Test:**
   Audit the raw ADF p-values of the candidate universe using the Benjamini-Hochberg False Discovery Rate (FDR) control and Romano-Wolf stepdown procedure at $\alpha = 0.05$.
   - `research-defined falsification threshold`: If fewer than 5% of the selected matching pairs maintain statistically significant cointegration under Benjamini-Hochberg FDR correction, the foundational assumption of persistent cointegrated spreads ($n_1 \ge 1$) is falsified, indicating the strategy is harvesting short-term mean reversion rather than true cointegration.

4. **Greedy Matching vs. Edmonds Blossom Ablation:**
   Compare the exact Edmonds blossom Maximum Weight Matching against a computationally trivial greedy matching heuristic: sort all pairs descending by ADF t-statistic, and greedily select pairs whose constituent assets have not yet been selected.
   - `research-defined falsification threshold`: If the greedy heuristic achieves a net Sharpe ratio within $\pm 0.05$ of the Edmonds blossom algorithm, the requirement for complex maximum weight matching optimization is falsified as an unnecessary complexity over simple greedy deduplication.

5. **Cross-Sectional Shuffled Placebo Test:**
   At each monthly rebalancing, randomly permute the stock return series across assets before computing pairwise regressions and ADF tests, destroying true inter-asset cointegration while preserving individual asset return distributions.
   - `research-defined falsification threshold`: If the matched portfolio constructed on shuffled placebo data yields an out-of-sample Sharpe ratio exceeding 0.40, the matching strategy is falsified as fitting spurious statistical noise.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`. The primary paper evaluates exclusively US equities (S&P 500) from 2017 to 2023. The application of graphical maximum weight matching to cryptocurrency pairs is an unproven research interpretation.
- **Crypto Market Microstructure Adaptations:**
  - *Universe Selection & Graph Dimensions:* On major perpetual exchanges (Binance, Bybit, OKX), the liquid perpetual universe consists of 80 to 150 instruments with sufficient depth. This corresponds to an undirected pairs graph with $V \approx 100$ nodes and $E \approx 4,950$ edges. Edmonds' blossom algorithm solves this in under 50 milliseconds, making graphical matching computationally feasible at hourly or 4-hour intervals rather than monthly.
  - *Continuous 24/7 Trading & Spread Horizons:* Crypto markets do not have discrete daily market closes. Stationarity in crypto pairs typically manifests at intraday frequencies (1-hour to 4-hour half-lives) rather than multi-week horizons. The regression and ADF lookback should be adapted from 2 years of daily bars to 30 to 60 days of 1-hour bars (`research-proposed`).
  - *Perpetual Funding Rate Divergence Penalty:* In crypto perpetual futures, long and short legs are subject to 8-hour funding payments. If two assets are cointegrated in price but exhibit persistent funding rate divergence, funding bleed can rapidly exceed the statistical arbitrage spread. The edge weight in the pairs graph must be modified to incorporate a funding differential penalty:
    $$w_{ij}^{\text{crypto}} = -t_{ij}^{\text{ADF}} - \lambda_{\text{funding}} \cdot \frac{|\overline{\text{Funding}}_i - \overline{\text{Funding}}_j|}{\sigma_{\text{funding}}} \quad (\text{research-proposed})$$
    where $\lambda_{\text{funding}}$ is a research-proposed tuning penalty.
  - *Extreme Single-Asset Concentration Mitigation:* In crypto, altcoin tokens frequently experience sudden liquidation cascades, token de-peggings, or exploit events. Because the matching method enforces a maximum node degree of 1, an exploit on a single token affects at most one pair, preventing contagion across the broader crypto statarb book.

## Limitations

- `not independently reproduced`: Primary results are transcribed directly from Qureshi & Zaman (2024); independent empirical reproduction in our quantitative backtesting stack has not been performed.
- `simplified transaction cost model`: The primary paper uses a flat 1% annual fee proxy ($0.00397\%$/day) instead of realistic per-trade maker/taker fees, order slippage, and bid-ask spread crossing costs.
- `look-ahead execution risk`: Positions evaluated at the daily close and assumed filled at the closing price create potential execution friction in live trading.
- `official code repository 404`: The authors' cited GitHub repository (`https://github.com/kai-trading-bot/pair/`) returns HTTP 404, requiring independent re-implementation of the blossom graph pipeline.
- `unproven in crypto`: Transferability to 24/7 crypto perpetual futures with funding rates, exchange counterparty risk, and liquidation volatility remains unverified empirically.

## Implementation status

- `not-implemented`: This research capture does not modify `nautilus-quant-system`, create PyBroker/Nautilus strategy families, or authorize paper, testnet, or live trading.
- All mathematical formulas, network matching formulations, and empirical tables reflect direct extraction from the primary LaTeX source of Qureshi & Zaman (`arXiv:2403.07998v1`, 2024).

## Adoption boundary

- `status`: `research-only`
- `adoption`: `not-approved`
- `approval_scope`: `research-only`
- Research capture is strictly separated from trading authorization. This strategy record is staged exclusively for ChatGPT Research Intake Review and downstream hypothesis generation; it is not approved for execution, capital allocation, or paper trading.

## Related Wiki records

- `[[quant/crypto-drl-execution-overlay-multi-pair-trading-2026-09-01]]`
- `[[quant/crypto-factor-augmented-volatility-pairs-trading-2026-09-01]]`
- `[[quant/crypto-pairs-trading-copula-cointegration-2026-08-31]]`
- `[[quant/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05]]`
- `[[quant/moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05]]`
- `[[quant/end-to-end-statistical-arbitrage-autoencoder-policy-2026-09-05]]`
- `[[quant/strategy-research-record-spec-v1]]`

## Sources

1. **Khizar Qureshi and Tauhid Zaman**, *"Pairs Trading Using a Novel Graphical Matching Approach"*, arXiv preprint `arXiv:2403.07998v1 [stat.AP]`, March 12, 2024.
   - Canonical URL: [https://arxiv.org/abs/2403.07998](https://arxiv.org/abs/2403.07998)
   - DOI: [https://doi.org/10.48550/arXiv.2403.07998](https://doi.org/10.48550/arXiv.2403.07998)
   - Full-Text HTML: [https://arxiv.org/html/2403.07998v1](https://arxiv.org/html/2403.07998v1)
2. **Jack Edmonds**, *"Paths, Trees, and Flowers"*, *Canadian Journal of Mathematics*, Vol. 17, pp. 449–467, 1965. [https://doi.org/10.4153/CJM-1965-045-4](https://doi.org/10.4153/CJM-1965-045-4)
3. **Zvi Galil**, *"Efficient Algorithms for Finding Maximum Matching in Graphs"*, *ACM Computing Surveys*, Vol. 18, No. 1, pp. 23–38, 1986. [https://doi.org/10.1145/6462.6464](https://doi.org/10.1145/6462.6464)
4. **Evan Gatev, William N. Goetzmann, and K. Geert Rouwenhorst**, *"Pairs Trading: Performance of a Relative-Value Arbitrage Rule"*, *The Review of Financial Studies*, Vol. 19, No. 3, pp. 797–827, 2006. [https://doi.org/10.1093/rfs/hhj020](https://doi.org/10.1093/rfs/hhj020)
5. **Marco Avellaneda and Jeong-Hyun Lee**, *"Statistical Arbitrage in the US Equities Market"*, *Quantitative Finance*, Vol. 10, No. 7, pp. 761–782, 2010. [https://doi.org/10.1080/14697680903124632](https://doi.org/10.1080/14697680903124632)
6. **Walter Enders**, *"Applied Econometric Time Series"*, John Wiley & Sons, 2004.
7. **Binh Do and Robert Faff**, *"Are Pairs Trading Profits Robust to Trading Costs?"*, *Journal of Financial Research*, Vol. 35, No. 2, pp. 261–287, 2012. [https://doi.org/10.1111/j.1475-6803.2012.01316.x](https://doi.org/10.1111/j.1475-6803.2012.01316.x)
