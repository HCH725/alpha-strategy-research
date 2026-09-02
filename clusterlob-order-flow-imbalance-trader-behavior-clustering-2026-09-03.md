---
schema: strategy-research-record-v1
title: "ClusterLOB: Unsupervised Order Clustering and Cluster-Specific Order Flow Imbalance for Intraday Return Forecasting"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - limit-order-book
  - order-flow-imbalance
  - unsupervised-learning
  - clustering
  - k-means-plus-plus
  - high-frequency-trading
  - intraday-alpha
  - tick-size-heterogeneity
status: research-only
confidence: high
source_as_of: 2025-04-28
sources:
  - "Yichi Zhang, Mihai Cucuringu, Alexander Y. Shestopaloff, and Stefan Zohren, 'ClusterLOB: Enhancing Trading Strategies by Clustering Orders in Limit Order Books', arXiv:2504.20349v1 [q-fin.TR], April 28, 2025. DOI: https://doi.org/10.48550/arXiv.2504.20349. Full text HTML: https://arxiv.org/html/2504.20349v1, PDF: https://arxiv.org/pdf/2504.20349."
  - "YichiZhang-Oxford/ClusterLOB repository on GitHub, commit SHA 80806211e18442995312e49942a2dfffe82e7ee6, files cluster_lob.py, main.py, metric.py, small_tick_stocks/test_top_FRNB_A.csv, medium_tick_stocks/test_top_FRNB_A.csv, large_tick_stocks/test_top_FRNB_A.csv. URL: https://github.com/YichiZhang-Oxford/ClusterLOB/tree/80806211e18442995312e49942a2dfffe82e7ee6"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ClusterLOB: Unsupervised Order Clustering and Cluster-Specific Order Flow Imbalance for Intraday Return Forecasting

## Provenance

- **Canonical Academic Source:** Yichi Zhang, Mihai Cucuringu, Alexander Y. Shestopaloff, and Stefan Zohren, *"ClusterLOB: Enhancing Trading Strategies by Clustering Orders in Limit Order Books"*, arXiv preprint `arXiv:2504.20349v1 [q-fin.TR]`, submitted April 28, 2025; published in *Quantitative Finance* (2026).
- **Institutional Affiliations:** Department of Statistics and Oxford-Man Institute of Quantitative Finance, University of Oxford, UK.
- **Digital Object Identifier (DOI):** [https://doi.org/10.48550/arXiv.2504.20349](https://doi.org/10.48550/arXiv.2504.20349)
- **Stable Academic URLs:**
  - Abstract: [https://arxiv.org/abs/2504.20349](https://arxiv.org/abs/2504.20349)
  - Full-text HTML: [https://arxiv.org/html/2504.20349v1](https://arxiv.org/html/2504.20349v1)
  - PDF: [https://arxiv.org/pdf/2504.20349](https://arxiv.org/pdf/2504.20349)
- **Immutable Code Repository:** GitHub repository `https://github.com/YichiZhang-Oxford/ClusterLOB`
- **Immutable Commit SHA:** `80806211e18442995312e49942a2dfffe82e7ee6`
- **Core Implementation Files:**
  - `cluster_lob.py`: feature engineering ($V, T^m, T^1, T', SBS, OBS$), forward-rolling normalization, and order flow imbalance calculation;
  - `main.py`: cross-sectional pipeline, base initialization, and bucket aggregation;
  - `metric.py`: evaluation metrics and portfolio backtest harness;
  - `small_tick_stocks/test_top_FRNB_A.csv`, `medium_tick_stocks/test_top_FRNB_A.csv`, `large_tick_stocks/test_top_FRNB_A.csv`: frozen empirical test result tables.
- **Dataset & Sample Partition:**
  - Source: LOBSTER (reconstructed NASDAQ Level 3 Market-by-Order ITCH data);
  - Universe: 15 liquid NASDAQ equities across 6 sectors for the full calendar year 2021 (252 trading days);
  - Partitioning:
    - **In-Sample (TRAIN):** January 1, 2021 to June 30, 2021 (126 trading days);
    - **Out-of-Sample (TEST):** July 1, 2021 to December 31, 2021 (126 trading days).

## Economic mechanism

### Source-reported

1. **Heterogeneous Market Participant Behavior in LOBs:** In modern electronic limit order books (LOBs), market orders and limit orders are submitted by diverse participants pursuing conflicting objectives:
   - **Directional participants ($\phi_1$):** Execute informed or urgent directional trades with high market impact. Their activity generates strong contemporaneous price movement (high correlation with $CONR$), but the price adjustment is largely absorbed within the current observation bucket, followed by partial mean reversion, leaving weak forward predictability.
   - **Opportunistic participants ($\phi_2$):** Tactically time order submissions based on short-term predictive signals and ephemeral liquidity imbalances. Their trades do not immediately disrupt the market but exhibit strong correlation with forward returns ($FRNB$ and $FREB$), reflecting anticipatory intraday alpha.
   - **Market-making participants ($\phi_3$):** Provide continuous two-sided liquidity and manage inventory risk. Their order flow shows minimal correlation with both contemporaneous and forward price changes, reflecting passive quote maintenance and queue replenishment.
2. **De-noising Order Flow Imbalance (OFI):** Classical OFI aggregates all order arrivals, cancellations, and executions across all market participants. Because market-maker inventory rebalancing and uninformative quote churning constitute the vast majority of message traffic, raw unclustered OFI is heavily diluted by microstructure noise. Segmenting order flow into behavioral clusters unmasks the high-signal opportunistic flow.
3. **Tick-Size Heterogeneity:** The structural role of order flow varies across tick-size regimes:
   - In *small-tick* stocks (wide bid-ask spreads in terms of ticks, $\bar{s} \ge \pi$), spread crossing is costly; opportunistic traders time order entry carefully, and count-based imbalances isolate their execution timing.
   - In *large-tick* stocks (tight spreads, $\bar{s} \lesssim 1.5\pi$), depth queues are deep; opportunistic traders queue strategically, making count-based signals highly effective.
   - In *medium-tick* stocks, directional size-based imbalances dominate forward predictability due to persistent price impact across intermediate tick spreads.

### Research interpretation

- **Unsupervised Information Filtration without Proprietary IDs:** Traditional participant segmentation relies on proprietary broker data or regulatory investor tags (e.g., Korean exchange regulatory tags). ClusterLOB proves that an unsupervised geometric clustering algorithm ($K\text{-means++}$) operating purely on publicly reconstructible Level 3 order attributes (queue dwell time, arrival interval, same- and opposite-side depth) can effectively disentangle informed from noise traders.
- **Convexity and Queue State Dependency:** Features $T^m$ (time since mid-price move), $T^1$ (queue inception age), and $T'$ (time since last price update) capture order book inertia and replenishment velocity. Orders submitted immediately after a mid-price change reflect different information content than orders joining stale queues.
- **Ported Hypothesis Boundary:** The empirical findings are demonstrated exclusively on US equity NASDAQ Market-by-Order data. Transferring this mechanism to cryptocurrency spot or perpetual futures markets constitutes an adapted, unproven research interpretation.

## Signal

### Feature engineering per order event
For every incoming market event $x = (p_x, q_x, t_x)$ on each trading day, six time-dependent features are extracted:
1. **Available Volume ($V$):** Available depth at order price $p_x$ at arrival timestamp $t_x$:
   $$V(p_x, t_x) = \sum_{j=1}^{10} v(p_j, t_x) \cdot \mathbb{I}(p_j = p_x)$$
2. **Mid-Price Elapsed Time ($T^m$):** Time elapsed between current order timestamp $t_x$ and the timestamp $t_m$ of the last mid-price change:
   $$T^m(t_x) = t_x - t_m$$
3. **First Price Occurrence Elapsed Time ($T^1$):** Time elapsed since the first order $x_1$ arrived at price $p_x$ on the same side:
   $$T^1(t_x) = t_x - t_{x_1}$$
4. **Previous Depth Update Elapsed Time ($T'$):** Time elapsed since the immediately preceding order $x'$ arrived at price $p_x$ on the same side:
   $$T'(t_x) = t_x - t_{x'}$$
5. **Same Book Side Depth ($SBS$):** Cumulative available depth on the same side of the book from the best price up to $p_x$:
   $$SBS(p_x, t_x) = \sum_{p \le p_x \text{ (bid)} \text{ or } p \ge p_x \text{ (ask)}} v(p, t_x)$$
6. **Opposite Book Side Depth ($OBS$):** Cumulative available depth on the opposite side of the book from the opposite best price up to the symmetric price $p'_x = 2m(t_x) - p_x$:
   $$OBS(p_x, t_x) = \sum_{p \ge p'_x \text{ (ask for buy)} \text{ or } p \le p'_x \text{ (bid for sell)}} v(p, t_x)$$

### Causal forward-rolling normalization
To eliminate cross-stock scale discrepancies without look-ahead bias, each feature $f_i$ is standardized dynamically over a causal sliding window of the preceding $w = 100$ orders:
$$\mathcal{N}(f_i(p, t)) = \frac{f_i(p, t) - \text{MA}_{100}(f_i(p, t))}{\text{STD}_{100}(f_i(p, t))}$$

### Clustering and role identification
1. **Model:** $K\text{-means++}$ with $K = 3$ clusters trained on the normalized 6-D feature vectors of the training sample.
2. **Cluster Alignment:** To guarantee uniform semantic meaning across stocks, cluster centroids are initialized using a base initialization algorithm, and cluster identities are mapped to standardized roles via mode estimation of correlations:
   - $\phi_1$ (Directional): Cluster exhibiting the highest correlation with contemporaneous return $CONR(\Delta_j, T)$;
   - $\phi_2$ (Opportunistic): Cluster exhibiting the highest correlation with future end-bucket return $FREB(\Delta_j, T)$;
   - $\phi_3$ (Market-Making): Remaining cluster showing low correlation with both $CONR$ and $FREB$, characterized by high values of $SBS, OBS, T^1, T'$.
   - $\phi_*$: Benchmark scenario without clustering (all orders pooled).

### Order Flow Imbalance (OFI) construction
The trading day (09:30 to 16:00 EST) is partitioned into $J = 13$ discrete 30-minute buckets $\Delta_j$ ($j = 1, \dots, 13$).
Within each bucket $\Delta_j$, order flow imbalances are computed for each cluster $\phi_k$:
- **Size-based OFI ($OFI^S$):**
  $$OFI^S(\phi_k, \Delta_j, T) = \sum_{i \in \Delta_j, \, c_i = \phi_k} \text{Direction}_i \cdot \text{BestSize}_i \cdot \text{SignEvent}_i$$
  where $\text{Direction}_i \in \{+1 \text{ (buy)}, -1 \text{ (sell)}\}$, $\text{BestSize}_i$ is order size if placed at or improving the best bid/ask ($0$ otherwise), and $\text{SignEvent}_i \in \{+1 \text{ for Add/Trade}, -1 \text{ for Cancel}\}$.
- **Count-based OFI ($OFI^C$):**
  $$OFI^C(\phi_k, \Delta_j, T) = \sum_{i \in \Delta_j, \, c_i = \phi_k} \text{Direction}_i \cdot \mathbb{I}(\text{BestSize}_i > 0) \cdot \text{SignEvent}_i$$

### Trading rule and sizing
1. **Decision Timestamp:** Formed at the boundary of each 30-minute bucket $\Delta_j$ using data strictly within $(t_{j-1}, t_j]$.
2. **Forecast Target:** Future Return for Next Bucket ($FRNB$):
   $$FRNB(\Delta_j, T) = \frac{m(t_{j+1}) - m(t_j)}{m(t_j)}$$
3. **Optimal Signal Selection (determined in TRAIN):**
   - **Small-tick stocks:** Opportunistic Count OFI, $s_{n, \Delta_j} = \text{sign}\left(OFI^C(\phi_2, \Delta_j, T)\right)$
   - **Medium-tick stocks:** Directional Size OFI, $s_{n, \Delta_j} = \text{sign}\left(OFI^S(\phi_1, \Delta_j, T)\right)$
   - **Large-tick stocks:** Opportunistic Count OFI, $s_{n, \Delta_j} = \text{sign}\left(OFI^C(\phi_2, \Delta_j, T)\right)$
4. **Position Sizing:** Equal-weighted across stocks within each tick-size group on each trading day:
   $$PNL(\Delta_j, T) = \frac{1}{N} \sum_{n=1}^N s_{n, \Delta_j} \cdot FRNB_n(\Delta_j, T)$$
   The daily aggregate PnL is rescaled to an annualized target volatility $\sigma_{\text{tgt}} = 0.15$ (15%):
   $$\widehat{PNL}_t = PNL_t \cdot \frac{\sigma_{\text{tgt}}}{\sigma_{PNL}}$$

## Required data

- **Universe:** 15 liquid US common stocks listed on NASDAQ across 6 sectors:
  - *Small-tick group ($\bar{s} \ge \$0.01$):* CHTR, GOOG, GS, IBM, MCD, NVDA (6 stocks);
  - *Medium-tick group ($1.5\pi \lesssim \bar{s} \lesssim \pi$):* AAPL, ABBV, PM (3 stocks);
  - *Large-tick group ($\bar{s} \lesssim 1.5\pi$):* CMCSA, CSCO, INTC, MSFT, KO, VZ (6 stocks).
- **Venue:** NASDAQ National Market System.
- **Market Type:** Cash equity (spot).
- **Timeframe:** Event-by-event Level 3 Market-by-Order message stream, aggregated to 30-minute intervals (13 buckets per day, 09:30 to 16:00 EST).
- **Fields:**
  - Order message fields: `Time` (nanoseconds past midnight), `EventType` (1: Add, 2: Cancel partial, 3: Cancel full, 4: Trade visible, 5: Trade hidden), `OrderID`, `Size`, `Price`, `Direction` ($+1$ Buy, $-1$ Sell);
  - LOB depth fields: Top 10 levels of prices and quantities (`AskPrice1–10`, `AskSize1–10`, `BidPrice1–10`, `BidSize1–10`).
- **Point-in-Time & Availability:** Strictly causal; rolling z-score uses trailing $w = 100$ orders. Trades and signals execute at bucket close boundary $t_j$.
- **Data Filtering & Missing Data:** Auction orders (EventType 6) and trading halt indicators (EventType 7) are removed. Weekends, market holidays, and incomplete trading sessions are omitted.

## Execution assumptions

- **Execution Timing:** Trades execute at the end of each 30-minute bucket $\Delta_j$, capturing the mid-price return to the end of bucket $\Delta_{j+1}$.
- **Fill Model:** Mid-price execution assumed in the source paper's academic backtest harness.
- **Transaction Costs & Spread:** The source reports **gross returns** without subtracting transaction costs, exchange taker fees, or bid-ask crossing costs.
- **Turnover:** 13 rebalances per trading day (every 30 minutes between 09:30 and 16:00 EST).
- **Leverage & Volatility Target:** Portfolio positions are scaled to hit a 15% annualized volatility target ($\sigma_{\text{tgt}} = 0.15$). Unconstrained borrowing is implicitly assumed for long and short positions.

## Evidence

### Source-reported

All metrics below are reported directly by Yichi Zhang, Mihai Cucuringu, Alexander Y. Shestopaloff, and Stefan Zohren (arXiv:2504.20349v1, Quantitative Finance 2026, Table 2 and frozen repository CSVs) on the out-of-sample test dataset (July 1, 2021 to December 31, 2021; 126 trading days, annualized volatility target $\sigma_{\text{tgt}} = 0.15$):

#### Out-of-Sample Test Results for Next-Bucket Return (FRNB, All Events)

| Asset Group | Strategy / Model | Ann. Return ($\mathbb{E}[\text{Ret}]$) | Sharpe Ratio | Sortino Ratio | Calmar Ratio | Max Drawdown | Hit Rate |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Small-Tick** | **ClusterLOB: $OFI^C(\phi_2)$ (Opportunistic)** | **+20.1%** ($0.201$) | **1.340** | **2.226** | **2.831** | **-7.1%** ($-0.071$) | **56.9%** |
| Small-Tick | Benchmark: $OFI^S(\phi_*)$ (No cluster, size) | +8.9% ($0.089$) | 0.593 | 0.773 | 0.798 | -11.2% ($-0.112$) | 53.4% |
| Small-Tick | Benchmark: $OFI^C(\phi_*)$ (No cluster, count) | -11.7% ($-0.117$) | -0.779 | -1.505 | -0.675 | -17.3% ($-0.173$) | 41.4% |
| **Medium-Tick** | **ClusterLOB: $OFI^S(\phi_1)$ (Directional)** | **+18.7%** ($0.187$) | **1.248** | **2.125** | **1.733** | **-10.8%** ($-0.108$) | **51.7%** |
| Medium-Tick | Benchmark: $OFI^S(\phi_*)$ (No cluster, size) | -7.0% ($-0.070$) | -0.467 | -0.897 | -0.543 | -12.9% ($-0.129$) | 46.6% |
| Medium-Tick | Benchmark: $OFI^C(\phi_*)$ (No cluster, count) | -8.9% ($-0.089$) | -0.593 | -0.964 | -0.555 | -16.1% ($-0.161$) | 45.7% |
| **Large-Tick** | **ClusterLOB: $OFI^C(\phi_2)$ (Opportunistic)** | **+23.2%** ($0.232$) | **1.548** | **2.344** | **3.869** | **-6.0%** ($-0.060$) | **55.2%** |
| Large-Tick | Benchmark: $OFI^S(\phi_*)$ (No cluster, size) | -0.2% ($-0.002$) | -0.013 | -0.021 | -0.014 | -13.2% ($-0.132$) | 49.1% |
| Large-Tick | Benchmark: $OFI^C(\phi_*)$ (No cluster, count) | +14.1% ($0.141$) | 0.940 | 1.734 | 2.482 | -5.7% ($-0.057$) | 50.9% |

- **Single-Stock PnL per Trade (PPT) on Small-Tick Test (Figure 6):**
  - Opportunistic cluster $\phi_2$: $\text{PPT} = 0.66$, Sharpe $1.34$;
  - Unclustered size benchmark $OFI^S(\phi_*)$: $\text{PPT} = 0.30$, Sharpe $0.60$;
  - Unclustered count benchmark $OFI^C(\phi_*)$: $\text{PPT} = -0.39$, Sharpe $-0.78$.
- **End-of-Day Return (FREB) Horizon Performance (Table 3 in source):**
  - Small-tick: $\phi_2$ opportunistic achieves Sharpe $0.230$, PPT $0.11$ (vs unclustered benchmarks with Sharpe $< -2.35$);
  - Medium-tick: $\phi_1$ directional achieves Sharpe $0.531$ (vs unclustered benchmarks with Sharpe $< -1.1$);
  - Large-tick: $\phi_2$ opportunistic achieves Sharpe $0.438$ (vs unclustered benchmarks with Sharpe $< 0.1$).

### Independently reproduced

`not independently reproduced`

### Negative evidence

1. **Failure of Event-Type OFI Decomposition:** Decomposing order flow into granular event types (Add events $L$, Cancel events $D$, and Trade events $M$) fails to improve out-of-sample forward-looking price impact over aggregate cluster OFI (Appendix A, confirming findings of Sitaru et al., 2023). Segmenting by participant behavior is effective; segmenting by order action is redundant.
2. **Catastrophic Failure of Raw Unclustered Order Counts:** Naive count-based OFI ($OFI^C(\phi_*)$) produces negative Sharpe ratios across small-tick ($-0.779$) and medium-tick ($-0.593$) stocks, suffering drawdowns of $-17.3\%$ and $-16.1\%$. Without behavioral clustering, high-frequency quote flickering and rapid cancellations by market makers completely invert or destroy count-based predictive signals.
3. **Horizon Decay (FREB vs FRNB):** Strategy performance collapses when expanding the holding horizon from 30 minutes ($FRNB$, Sharpe $1.25$ to $1.55$) to the end of the trading day ($FREB$, Sharpe $0.23$ to $0.53$). Order flow imbalance signals are fundamentally fast-decaying microstructure alphas.
4. **Frictional Vulnerability:** The source paper does not subtract transaction costs or bid-ask spreads. At 13 trades per stock per day, a round-trip trading friction of merely 2 bps per rebalance would impose an annual cost hurdle of approximately:
   $$13 \text{ trades/day} \times 252 \text{ days} \times 2 \text{ bps} \times \text{turnover fraction} \approx 65\% \times \text{turnover}$$
   which would severely impair or erase the headline gross returns ($18.7\%$ to $23.2\%$).

## Falsification plan

1. **Placebo Cluster Assignment Test:**
   - *Procedure:* Randomly permute the cluster assignments $\phi \in \{\phi_1, \phi_2, \phi_3\}$ across orders within each day while preserving marginal cluster frequencies.
   - *Falsification Rule:* If the randomized opportunistic cluster $OFI^C(\phi_{\text{placebo}})$ achieves a Sharpe ratio within $20\%$ of the empirical ClusterLOB Sharpe ($SR \ge 1.07$), reject the hypothesis that the 6 time-dependent features isolate informed participant behavior, and attribute performance to spurious data partitioning.
2. **Transaction Cost & Taker Fee Hurdle Test:**
   - *Procedure:* Re-evaluate the strategy under realistic taker fees (e.g., $1$ bp, $2$ bps, and $5$ bps per side) and bid-ask half-spread crossing costs across the 15 NASDAQ equities.
   - *Falsification Rule:* If net Sharpe ratio drops below $0.0$ at a conservative friction of $1.5$ bps per leg, classify the strategy as a theoretical microstructure artefact incapable of surviving execution frictions.
3. **Temporal Centroid Drift & Out-of-Sample Cluster Stability Test:**
   - *Procedure:* Evaluate whether cluster centroids learned on H1 2021 remain stable in subsequent years (2022–2025). Re-cluster on a rolling 6-month basis versus static H1 2021 centroids.
   - *Falsification Rule:* If the cosine similarity of the opportunistic cluster centroid $\phi_2$ drops below $0.70$, or if the out-of-sample Sharpe drops below $0.30$ under rolling re-clustering, falsify the structural stability of the learned behavioral classes.
4. **Tick-Size Inversion Stress Test:**
   - *Procedure:* Force the small-tick configuration ($OFI^C(\phi_2)$) onto medium-tick stocks, and the medium-tick configuration ($OFI^S(\phi_1)$) onto large-tick stocks.
   - *Falsification Rule:* If cross-tick parameter transfers yield equal or superior Sharpe ratios, falsify the authors' claim that tick-size market microstructure dictates distinct optimal signal constructions.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`
- **Microstructure and Data Discrepancies:**
  - *Data Access (Level 3 vs Level 2):* NASDAQ provides full Market-by-Order ITCH feeds with unique `OrderID` tags, allowing deterministic tracking of order inception ($T^1$) and depth modifications ($T'$). Major cryptocurrency exchanges (Binance, OKX, Bybit) broadcast aggregated Level 2 price-depth snapshots and diffs via WebSockets. Reconstructing $T^1$ and $T'$ in crypto requires proprietary Level 3 binary feeds or exchange colocation.
  - *Session Structure:* Crypto operates 24/7 without opening/closing auctions, requiring continuous rolling bucket windows rather than 13 fixed intraday intervals.
  - *Fee Structures:* Taker fees on major crypto perpetual venues range from $2$ to $5$ bps (VIP0/retail), which would consume the entire alpha budget under 30-minute rebalancing cadence. A crypto adaptation would require passive maker execution, introducing adverse selection.
  - *Tick Size Heterogeneity:* Unlike US equities with a rigid $\$0.01$ tick size, crypto perpetuals feature dynamic and highly disparate tick sizes (e.g., $\$0.10$ on BTC vs $\$0.00001$ on memecoins), which drastically shifts queue dynamics and order-count informativeness.

## Limitations

- **Gross Mid-Price Evaluation:** The source paper does not account for execution costs, commissions, or bid-ask crossing slippage.
- **Narrow Sample Horizon:** Evaluated on a single calendar year (2021), a predominantly bull/high-volatility regime for US equities.
- **Universe Limitation:** Tested on only 15 large-cap NASDAQ stocks; performance across small-cap or illiquid equities is unknown.
- **Static Cluster Architecture:** $K\text{-means++}$ with $K = 3$ is trained once on the first 6 months and held static, ignoring dynamic shifts in algorithmic execution styles.
- **Compute Burden:** Calculating rolling 100-order moving averages and depth traversals across millions of MBO events per day requires substantial compute infrastructure (e.g., 72-core Xeon with 500GB RAM in the authors' setup).

## Implementation status

- `not-implemented`. No implementation has been created in NautilusTrader, PyBroker, or any live execution harness. This document serves strictly as an upstream research capture.

## Adoption boundary

- `research-only`, `not-approved`. Capturing this strategy research does not authorize implementation, paper trading, testnet, or live deployment.

## Related Wiki records

- `[[order-flow-matched-filter-normalization-investor-segmentation-2026-09-02]]`
- `[[order-flow-two-layer-hawkes-core-reaction-rough-impact-2026-09-02]]`
- `[[crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`
- `[[temporal-kolmogorov-arnold-networks-high-frequency-lob-alpha-decay-2026-09-02]]`

## Sources

1. Yichi Zhang, Mihai Cucuringu, Alexander Y. Shestopaloff, and Stefan Zohren, *"ClusterLOB: Enhancing Trading Strategies by Clustering Orders in Limit Order Books"*, arXiv preprint `arXiv:2504.20349v1 [q-fin.TR]`, April 28, 2025; published in *Quantitative Finance* (2026). DOI: [https://doi.org/10.48550/arXiv.2504.20349](https://doi.org/10.48550/arXiv.2504.20349). Stable URL: [https://arxiv.org/abs/2504.20349](https://arxiv.org/abs/2504.20349). Full-text HTML: [https://arxiv.org/html/2504.20349v1](https://arxiv.org/html/2504.20349v1).
2. GitHub Repository: `https://github.com/YichiZhang-Oxford/ClusterLOB`, full commit SHA `80806211e18442995312e49942a2dfffe82e7ee6`. Files: `cluster_lob.py`, `main.py`, `metric.py`, `small_tick_stocks/test_top_FRNB_A.csv`, `medium_tick_stocks/test_top_FRNB_A.csv`, `large_tick_stocks/test_top_FRNB_A.csv`.
