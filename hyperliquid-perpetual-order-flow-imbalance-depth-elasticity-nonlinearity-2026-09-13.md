---
schema: strategy-research-record-v1
title: "Hyperliquid Perpetual Order Flow Imbalance: Cross-Market Replication, Quote-Frequency Degradation, Concave Nonlinearity, and Depth Elasticity"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - order-flow-imbalance
  - ofi
  - price-impact
  - market-microstructure
  - limit-order-book
  - hyperliquid
  - crypto-perpetuals
  - market-depth-elasticity
  - trade-imbalance
  - us-equities
  - white-hc0
status: research-only
confidence: medium
source_as_of: 2026-08-11
sources:
  - "https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/tree/2af7b405dc1656bbaf5f4c3df4da5f91986c525c"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hyperliquid Perpetual Order Flow Imbalance: Cross-Market Replication, Quote-Frequency Degradation, Concave Nonlinearity, and Depth Elasticity

## Provenance

- **Authors:** Yashar Ezzatpour (Sharif University of Technology, ID `404209214`) and Ata Akbarizad Ahangari (Sharif University of Technology, ID `403209313`) (`AHBAR-software-TM`).
- **Academic Framework:** Course project report for *Financial Machine Learning* (Spring 2026), titled *"The Price Impact of Order Book Events: Replication across Crypto Perpetual and Equity Markets"*, extending the foundational econometric framework of Rama Cont, Arseniy Kukanov, and Sasha Stoikov (2014, *Journal of Financial Econometrics*, DOI: `10.1093/jjfinec/nbt003`).
- **Repository URL:** [https://github.com/AHBAR-software-TM/price-impact-of-order-book-events](https://github.com/AHBAR-software-TM/price-impact-of-order-book-events)
- **Full Immutable Commit SHA:** `2af7b405dc1656bbaf5f4c3df4da5f91986c525c`
- **Canonical Tree URL:** [https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/tree/2af7b405dc1656bbaf5f4c3df4da5f91986c525c](https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/tree/2af7b405dc1656bbaf5f4c3df4da5f91986c525c)
- **Commit Date:** 2026-08-11T02:03:28+03:30
- **Primary Source Files Examined:**
  - `Full Report.pdf` (27-page comprehensive academic project report detailing theoretical derivations, data hygiene protocols, 17 empirical regression tables, 14 analytical figures, and cross-market comparisons) (`source-reported`).
  - `price_impact_order_book_events.ipynb` (executable master Jupyter notebook containing raw L2 top-of-book ingestion, event-level OFI construction, 10-second binning, White HC0 OLS regressions, non-linear quadratic impact tests, depth elasticity regressions, trade imbalance comparisons, and market synthesis plots) (`source-reported`).
  - `README.md` (project documentation, mathematical methodology, repository structure, and executive summary) (`source-reported`).
- **Primary Source Verification:** Directly inspected all 15 cells and executed tabular/visual outputs of `price_impact_order_book_events.ipynb` as well as all 27 pages of `Full Report.pdf`. Every metric, regression $R^2$, $t$-statistic, $\beta$ coefficient, $\gamma_Q$ non-linear coefficient, depth elasticity $\lambda$, price-volume exponent $H$, and sample count traces directly to these primary documents.
- **Repository Deduplication:** Audited all existing markdown records in `alpha-strategy-research`. Zero prior records cite `AHBAR-software-TM`, Yashar Ezzatpour, Ata Akbarizad Ahangari, or this commit. Prior order-flow records in the repository evaluate different domains: `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Tejas Mungale / `Tejas356`) analyzes single-equity INTC NASDAQ ITCH 40-level books and predictive decoupling; `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md` (Rattandeep Singh / `Rattandeep0500`) investigates bivariate Hawkes self-excitation on Binance BTCUSDT; `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31.md` explores multi-level OFI on crypto spot. The current research provides an independent, broad-scope empirical replication across five Hyperliquid decentralized perpetual futures contracts (BTC, ETH, SOL, HYPE, DOGE; 720 half-hour regressions across 3 monthly regimes) and two U.S. equities (AAPL, AMZN; 26 half-hour regressions), uncovering four distinct empirical findings: (1) quote-sampling frequency collapse in July ($12\text{--}18 \to 1.8$ quotes/bin) degrades $R^2$ by roughly half; (2) crypto perpetuals exhibit recurrent concave non-linearity ($\gamma_Q < 0$ in $89\%\text{--}98\%$ of half-hours); (3) market depth elasticity $\lambda$ diverges across crypto assets (SOL $\lambda=1.19$, HYPE $\lambda=1.32$, but BTC $\lambda=-0.60$); and (4) aggressive trade imbalance retains substantial incremental explanatory power over OFI in crypto perpetuals unlike in traditional equities.

## Economic mechanism

### Source-reported

1. **Top-of-Book Demand/Supply State vs. Executed Trades:**
   Traditional microstructure models evaluate price impact through executed transactions. Cont, Kukanov, and Stoikov (2014) demonstrated that short-horizon mid-price movements are driven by net changes in supply and demand at the best bid and ask (Order Flow Imbalance, OFI), which integrates limit order insertions, cancellations, and market orders. Price moves occur when displayed queue sizes at the top of the book are exhausted or when new quotes establish a tighter spread.
2. **Generalization to Decentralized Perpetual Futures:**
   Hyperliquid operates a fully on-chain central limit order book (CLOB) with deterministic order matching. Because top-of-book quotes (best bid, best ask, bid size, ask size) and aggressor trades are transparently broadcast, the OFI mechanism should operate similarly to traditional equity exchanges: positive OFI represents net buying pressure (increasing bid queues or depleting ask queues), pushing the mid-price upward.
3. **Cross-Market Structural Distinctions:**
   - *Sampling Granularity & Microstructure Compression:* In continuous equity markets (NBBO), quote update rates reach hundreds per 10-second interval (343 for AAPL, 793 for AMZN). In Hyperliquid perpetuals, public API capture densities are substantially lower ($12\text{--}18$ quotes per 10-second bin in May/June 2026, falling to $\sim 1.8$ in July 2026). When sampling frequency falls, multiple intermediate order-book events occur between captured snapshots and are mechanically compressed, injecting measurement noise and reducing empirical explanatory power ($R^2$).
   - *Nonlinear Price Impact:* In equities, the relationship between OFI and price change is largely linear, with quadratic terms yielding negligible explanatory gains ($65\% \to 68\%$). In crypto perpetuals, large order flows face diminishing price impact per unit of imbalance (concavity, $\gamma_Q < 0$), driven by reactive algorithmic replenishment from high-frequency market makers and liquidity clustering outside the best quote.
   - *Market Depth Scaling:* The theoretical benchmark predicts that price impact slope $\beta_i$ is inversely proportional to average top-of-book depth $\bar{D}_i$ ($\beta_i \propto 1/\bar{D}_i$, elasticity $\lambda = 1$). In crypto perpetuals, depth elasticity is highly asset-specific: liquid altcoins (SOL, HYPE, DOGE) conform to the inverse scaling law, while BTC exhibits an anomalous positive correlation between impact and depth across sampled dates.
   - *Information Content of Aggressive Trades:* In equities, OFI substantially subsumes Trade Imbalance ($TI$). In crypto perpetuals, while OFI remains the stronger standalone predictor, $TI$ retains independent statistical significance in $44\%\text{--}77\%$ of half-hour windows, reflecting the unique informational role of aggressive liquidations and market orders in perpetual derivatives.

### Research interpretation

From a quantitative trading and strategy development perspective, the findings delineate clear boundaries between contemporaneous market-making inventory control and directional alpha:
- **Contemporaneous Price Impact vs. Directional Forecasting:** The empirical relationship $\Delta P_k = \alpha + \beta \cdot \text{OFI}_k$ is contemporaneous: $\text{OFI}_k$ is accumulated over the exact same 10-second interval as $\Delta P_k$. While this confirms the mechanical and structural link between queue dynamics and price revision, it does not prove that past OFI ($\text{OFI}_{k-1}$) predicts future price changes ($\Delta P_k$) net of taker fees.
- **Component Roles in a Microstructure Strategy Architecture (`research-proposed`):**
  - *Regime Gate:* Quote-Sampling Frequency Monitor. Require $\ge 5$ quote updates per 10-second bin; suspend execution when feed capture drops below 2 updates/bin (as observed in the July regime) to avoid trading on compressed, stale book states (`research-proposed`).
  - *Primary Signal:* Lagged Multi-Interval OFI Momentum / Mean-Reversion. Compute standardized $\text{OFI}_k / \bar{D}_k$; enter in the direction of persistent imbalance only if predicted return exceeds round-trip taker fees (Hyperliquid taker fee: 2.5–3.5 bps) (`research-proposed`).
  - *Nonlinear Threshold Filter:* Apply a concave adjustment $\beta_Q \text{OFI} + \gamma_Q \text{OFI}|\text{OFI}|$ to down-weight extreme OFI spikes that reflect temporary liquidity vacuums prone to rapid mean reversion (`research-proposed`).
  - *Depth-Adaptive Sizing:* Scale position sizes inversely with estimated local depth $\bar{D}_i^\lambda$ using asset-specific elasticity ($\lambda_{\text{SOL}} \approx 1.19$, $\lambda_{\text{HYPE}} \approx 1.32$) (`research-proposed`).
  - *Confirmation Filter:* Trade Imbalance ($TI$) Alignment. Require directional concordance between top-of-book OFI and aggressive taker trade flow ($TI_k \cdot \text{OFI}_k > 0$) (`research-proposed`).

## Signal

### Formation Timestamp

- **Observation Cadence:** Continuous order-book event stream aggregated into uniform 10-second discrete clock-time bins ($\Delta t = 10\text{ s}$) (`source-reported`).
- **Regression Estimation Window:** 30-minute rolling blocks (up to 180 ten-second bins per regression; minimum 120 valid observations required) (`source-reported`).
- **Clock Source & Alignment:** UTC timestamps (`source-reported`). Data gaps $> 15\text{ seconds}$ trigger a new segment boundary; the first quote following a gap is never compared against the pre-gap quote, preventing artificial OFI spikes (`source-reported`).
- **Trading Execution Timestamp:** Next-bar open fill at $t_k$ following signal finalization at $t_{k-1}$ (`research-proposed`).

### Lookback Windows

- **Crypto Perpetuals Sample Dates:** 2026-05-01, 2026-06-01, and 2026-07-01 (three non-consecutive first-of-month 24-hour UTC sessions) (`source-reported`).
- **Equity Sample Session:** One regular U.S. trading session (09:30–16:00 EST, 6.5 hours) (`source-reported`).
- **Discrete Aggregation Interval ($\Delta t$):** 10 seconds (`source-reported`).
- **Parameter Estimation Block ($i$):** 30 minutes (180 bins) (`source-reported`).
- **Trade-Time Horizon ($L$):** $L \in \{2, 5, 10\}$ consecutive executed transactions for trade-time robustness regressions (`source-reported`).

### Exact Mathematical Definitions

1. **Event-Level Order Flow Imbalance ($e_n$):**
   For event $n$ with best bid price $P_n^B$, best bid size $q_n^B$, best ask price $P_n^A$, and best ask size $q_n^A$:
   $$e_n = I_{\{P_n^B \ge P_{n-1}^B\}} q_n^B - I_{\{P_n^B \le P_{n-1}^B\}} q_{n-1}^B - I_{\{P_n^A \le P_{n-1}^A\}} q_n^A + I_{\{P_n^A \ge P_{n-1}^A\}} q_{n-1}^A \quad (\text{source-reported})$$
   where $I_{\{\cdot\}}$ is the indicator function. This explicitly captures five discrete micro-events:
   - *Bid Price Increase ($P_n^B > P_{n-1}^B$):* $e_n = +q_n^B$ (new higher bid established).
   - *Bid Size Increase at Same Price ($P_n^B = P_{n-1}^B$):* $e_n = q_n^B - q_{n-1}^B$ (resting bid added).
   - *Bid Size Decrease at Same Price ($P_n^B = P_{n-1}^B$):* $e_n = q_n^B - q_{n-1}^B < 0$ (resting bid canceled or filled).
   - *Ask Price Decrease ($P_n^A < P_{n-1}^A$):* $e_n = -q_n^A$ (new lower ask established).
   - *Ask Size Increase at Same Price ($P_n^A = P_{n-1}^A$):* $e_n = -(q_n^A - q_{n-1}^A)$ (resting ask added).

2. **10-Second Aggregated Order Flow Imbalance ($\text{OFI}_k$):**
   $$\text{OFI}_k = \sum_{n=N(t_{k-1})+1}^{N(t_k)} e_n \quad (\text{source-reported})$$

3. **Mid-Price Change in Ticks ($\Delta P_k$):**
   $$\Delta P_k = \frac{P_k^{\text{mid}} - P_{k-1}^{\text{mid}}}{\text{TickSize}} \quad (\text{source-reported})$$
   where $P_k^{\text{mid}} = \frac{1}{2}(P_k^B + P_k^A)$ is the mid-price at the close of 10-second bin $k$.

4. **Linear Price Impact Regression:**
   $$\Delta P_k = \alpha_i + \beta_i \cdot \text{OFI}_k + \epsilon_k \quad (\text{source-reported})$$
   estimated separately for each 30-minute block $i$ via OLS with White HC0 heteroskedasticity-consistent standard errors (`source-reported`).

5. **Nonlinear Quadratic Price Impact Regression:**
   $$\Delta P_k = \alpha_{Q,i} + \beta_{Q,i} \cdot \text{OFI}_k + \gamma_{Q,i} \cdot \text{OFI}_k |\text{OFI}_k| + \epsilon_{Q,k} \quad (\text{source-reported})$$
   where $\gamma_{Q,i} < 0$ indicates concave price impact (diminishing marginal price change per unit OFI).

6. **Price Impact vs. Average Market Depth Log-Log Regression:**
   $$\log(\beta_i) = \alpha_{L,i} - \lambda \log(\bar{D}_i) + \epsilon_{L,i} \quad (\text{source-reported})$$
   where $\bar{D}_i = \frac{1}{K} \sum_{k=1}^K \frac{q_k^B + q_k^A}{2}$ is the average top-of-book depth in half-hour $i$, estimated using Newey-West HAC standard errors across blocks with $\beta_i > 0$ (`source-reported`).

7. **Trade Imbalance ($TI_k$) and Total Volume ($\text{VOL}_k$):**
   $$TI_k = \sum_{m \in \text{bin } k} \text{signed\_trade\_amount}_m = \text{BuyVolume}_k - \text{SellVolume}_k \quad (\text{source-reported})$$
   $$\text{VOL}_k = \sum_{m \in \text{bin } k} \text{trade\_amount}_m = \text{BuyVolume}_k + \text{SellVolume}_k \quad (\text{source-reported})$$
   Joint regression:
   $$\Delta P_k = \alpha_i + \beta_{\text{OFI},i} \cdot \text{OFI}_k + \beta_{TI,i} \cdot TI_k + \epsilon_k \quad (\text{source-reported})$$

8. **Price-Volume Scaling Exponent ($H$):**
   $$\log |\Delta P_k| = \log c + H \log(\text{VOL}_k) + \nu_k \quad (\text{source-reported})$$
   evaluating whether the empirical relation matches the theoretical square-root law ($H = 0.5$).

### Operational Trading Parameters (`research-proposed`)

While the primary source is an empirical econometric study, operationalizing the mechanism into a falsifiable trading strategy requires defining explicit trading rules:
- **Z-Score Normalization:** Standardized OFI $z_k = (\text{OFI}_k - \mu_{k,180}) / \sigma_{k,180}$ computed over a rolling 180-bin (30-minute) window (`research-proposed`).
- **Long Entry Trigger:** $z_k > +2.0$ AND $TI_k > 0$ AND quote count per bin $\ge 5$ (`research-proposed`).
- **Short Entry Trigger:** $z_k < -2.0$ AND $TI_k < 0$ AND quote count per bin $\ge 5$ (`research-proposed`).
- **Exit Trigger:** $z_k$ crosses 0.0 OR after a fixed holding period of 6 bins (60 seconds) (`research-proposed`).
- **Stop Loss:** Adverse mid-price movement exceeding $3 \times \text{TickSize}$ or $1.5 \times \text{Spread}_k$ (`research-proposed`).
- **Position Sizing:** Inversely proportional to current top-of-book depth $\bar{D}_k$ capped at $1.0\%$ of available book depth (`research-proposed`).

## Required data

- **Instruments & Asset Universe:**
  - *Crypto Perpetuals:* Five Hyperliquid perpetual futures contracts: BTC-USD, ETH-USD, SOL-USD, HYPE-USD, DOGE-USD (`source-reported`).
  - *Equities:* Two U.S. large-cap equities: AAPL, AMZN (`source-reported`).
- **Venues:**
  - Hyperliquid decentralized perpetual futures exchange (data collected and distributed by Tardis.dev) (`source-reported`).
  - U.S. National Best Bid and Offer (NBBO) quote stream (`source-reported`).
- **Market Type:** Central limit order book (CLOB) perpetual futures and equity cash equities (`source-reported`).
- **Tick Sizes:**
  - BTC: $1.0$ USD (`source-reported`).
  - ETH: $0.1$ USD (`source-reported`).
  - SOL: $0.001$ USD (`source-reported`).
  - HYPE: $0.001$ USD (`source-reported`).
  - DOGE: $0.00001$ USD ($10^{-5}$) (`source-reported`).
  - AAPL & AMZN: $0.01$ USD (`source-reported`).
- **Raw Quote Fields Required:**
  - Timestamp (UTC nanoseconds or microsecond integer) (`source-reported`).
  - Best bid price ($P^B$) and best bid size ($q^B$) (`source-reported`).
  - Best ask price ($P^A$) and best ask size ($q^A$) (`source-reported`).
- **Raw Trade Fields Required (Crypto):**
  - Timestamp (UTC) (`source-reported`).
  - Trade execution price (`source-reported`).
  - Trade execution amount / quantity (`source-reported`).
  - Taker side (`buy` vs. `sell`) (`source-reported`).
- **Point-in-Time & Hygiene Rules:**
  - Strict chronological sorting by timestamp (`source-reported`).
  - Exclusion of invalid, non-positive prices and sizes (`source-reported`).
  - Exclusion of locked ($P^B = P^A$) or crossed ($P^B > P^A$) quotes (removed 2,569 rows for AAPL, 7,161 rows for AMZN) (`source-reported`).
  - Gaps $> 15\text{ s}$ trigger segment resets; no cross-gap OFI calculation (`source-reported`).
  - Deduction of time-of-day integer strings for equities (`hhmmss + nanoseconds`) bounded strictly within regular trading hours (09:30:00 to 16:00:00 EST) (`source-reported`).

## Execution assumptions

- **Model Formulation vs. Tradability:** The source authors estimate an econometric model of price formation, not an execution algorithm (`source-reported`).
- **Order Type:** Passive limit orders at top of book or aggressive taker orders (`research-proposed`).
- **Fill Timing:** Same-bar execution in source regressions (contemporaneous price impact). In a tradable implementation, orders execute at the next-bar open ($t_{k+1}$) with minimum 50–100 ms network latency to Hyperliquid validators (`research-proposed`).
- **Transaction Costs & Fees:**
  - Hyperliquid standard VIP0 taker fee: 2.5–3.5 bps ($0.00025\text{--}0.00035$); maker fee: -0.2 bps (rebate) or 0.0 bps (`research-proposed`).
  - Bid-ask spread: Crypto perpetual average spreads range from $1.0\text{--}2.5$ ticks; equity spreads average 1.0 tick ($0.01$) (`source-reported`).
- **Slippage & Capacity:** Market orders incur instantaneous slippage characterized by $\beta_i \cdot \text{TradeSize}$. Maximum order capacity is constrained by resting top-of-book depth $\bar{D}_k$ (`research-proposed`).
- **Margin & Funding:** Hyperliquid perpetual positions require USDC collateral with margin leverage up to 20x–50x. 8-hour funding payments apply to open perpetual positions (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below trace directly to `Full Report.pdf` (Tables 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17) and executed cells in `price_impact_order_book_events.ipynb` (commit `2af7b405dc1656bbaf5f4c3df4da5f91986c525c`):

#### 1. Sample Size and Descriptive Statistics (Table 4 & Table 6)

| Asset / Symbol | Market | Quote Rows | Trade Rows | 10s Bins | Tick Size | Mean Quotes/Bin | Trade Bin Coverage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BTC** | Hyperliquid Perp | 319,880 | 1,571,845 | 25,920 | 1.0 | 12.34 | 100.0% |
| **ETH** | Hyperliquid Perp | 313,954 | 503,020 | 25,918 | 0.1 | 12.11 | 98.9% |
| **SOL** | Hyperliquid Perp | 267,759 | 340,689 | 25,918 | 0.001 | 10.33 | 94.9% |
| **HYPE** | Hyperliquid Perp | 294,821 | 1,398,875 | 25,919 | 0.001 | 11.37 | 100.0% |
| **DOGE** | Hyperliquid Perp | 233,859 | 66,303 | 25,853 | 0.00001 | 9.05 | 63.9% |
| **AAPL** | U.S. Equity NBBO | 803,356 | N/A | 2,340 | 0.01 | 343.3 | N/A |
| **AMZN** | U.S. Equity NBBO | 1,855,226 | N/A | 2,340 | 0.01 | 792.8 | N/A |

#### 2. Quote Frequency Collapse and Explanatory Power by Date (Table 5)

| Asset | May Quotes/Bin | June Quotes/Bin | July Quotes/Bin | May Mean $R^2$ | June Mean $R^2$ | July Mean $R^2$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BTC** | 17.59 | 17.58 | **1.86** | 0.508 (50.8%) | 0.457 (45.7%) | **0.311 (31.1%)** |
| **ETH** | 16.91 | 17.58 | **1.86** | 0.586 (58.6%) | 0.609 (60.9%) | **0.343 (34.3%)** |
| **SOL** | 13.54 | 15.60 | **1.86** | 0.542 (54.2%) | 0.525 (52.5%) | **0.294 (29.4%)** |
| **HYPE** | 13.91 | 18.35 | **1.86** | 0.419 (41.9%) | 0.414 (41.4%) | **0.245 (24.5%)** |
| **DOGE** | 12.36 | 12.92 | **1.82** | 0.550 (55.0%) | 0.558 (55.8%) | **0.248 (24.8%)** |

#### 3. Half-Hour Linear OFI Regression Results (Table 7 & Table 14)

| Asset | Total Regressions | Mean $R^2$ | Median $R^2$ | $\beta > 0$ Pct | Significant $\beta$ ($p < 0.05$) | Mean $t(\beta)$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BTC** | 144 | 0.425 (42.52%) | 0.437 (43.65%) | 100.0% | 100.0% | 8.90 |
| **ETH** | 144 | 0.513 (51.27%) | 0.549 (54.94%) | 100.0% | 100.0% | 10.46 |
| **SOL** | 144 | 0.454 (45.38%) | 0.478 (47.76%) | 100.0% | 100.0% | 10.26 |
| **HYPE** | 144 | 0.359 (35.92%) | 0.369 (36.89%) | 100.0% | 97.9% | 6.99 |
| **DOGE** | 144 | 0.452 (45.19%) | 0.491 (49.10%) | 100.0% | 100.0% | 9.83 |
| **Crypto Pooled** | **720** | **0.4406 (44.06%)** | — | **100.0%** | **99.58%** | — |
| **AAPL** | 13 | 0.553 (55.28%) | 0.583 (58.22%) | 100.0% | 92.3% | — |
| **AMZN** | 13 | 0.740 (74.01%) | 0.801 (80.01%) | 100.0% | 92.3% | — |
| **Equity Pooled** | **26** | **0.6464 (64.64%)** | — | **100.0%** | **92.31%** | — |

#### 4. Nonlinear Impact Tests ($\text{OFI} \times |\text{OFI}|$, Table 8 & Table 15)

| Asset | Mean $R^2$ Gain (pp) | Median $R^2$ Gain (pp) | Significant $\gamma_Q$ ($p < 0.05$) | $\gamma_Q < 0$ (Concave) | $\gamma_Q < 0$ and Sig |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BTC** | +3.14 | +2.52 | 74.3% | 97.2% | 74.3% |
| **ETH** | +2.34 | +1.54 | 55.6% | 89.6% | 54.9% |
| **SOL** | +2.28 | +1.18 | 50.0% | 95.8% | 49.3% |
| **HYPE** | **+7.69** | **+6.42** | **84.0%** | **97.9%** | **84.0%** |
| **DOGE** | +4.03 | +1.44 | 55.6% | 88.9% | 55.6% |
| **AAPL** | +8.01 | +1.13 | 38.5% | 53.8% | — |
| **AMZN** | +5.38 | +1.67 | 53.8% | 92.3% | — |

*Key finding:* In crypto perpetuals, $\gamma_Q$ is negative in $88.9\%\text{--}97.9\%$ of half-hours, demonstrating strong concave price impact (diminishing price impact for larger order imbalances).

#### 5. Price Impact vs. Market Depth Elasticity ($\lambda$, Table 10 & Table 16)

| Asset | Pooled $\hat{\lambda}$ | Log-Log $R^2$ | $\text{Corr}(\beta, \text{Depth})$ | $p$-value ($H_0: \lambda = 1$) |
| :--- | :--- | :--- | :--- | :--- |
| **BTC** | **-0.601** | 0.045 | +0.171 | 0.000 (rejection, wrong sign) |
| **ETH** | 0.215 | 0.026 | -0.129 | 0.000 (rejection, weak inverse) |
| **SOL** | **1.186** | 0.167 | -0.365 | **0.484 (consistent with $\lambda=1$)** |
| **HYPE** | **1.322** | 0.522 | -0.161 | **0.131 (consistent with $\lambda=1$)** |
| **DOGE** | 0.604 | 0.479 | -0.521 | 0.000 |
| **AAPL** | 2.032 | 0.241 | -0.516 | 0.205 (consistent with $\lambda=1$) |
| **AMZN** | 2.832 | 0.765 | -0.927 | 0.016 (super-elastic) |

#### 6. OFI vs. Trade Imbalance ($TI$) in Crypto Perpetuals (Table 11)

| Asset | OFI Standalone $R^2$ | $TI$ Standalone $R^2$ | Joint Model $R^2$ | OFI Sig in Joint | $TI$ Sig in Joint |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BTC** | 0.425 | 0.131 | 0.505 | 100.0% | **75.0%** |
| **ETH** | 0.513 | 0.076 | 0.555 | 100.0% | **53.5%** |
| **SOL** | 0.454 | 0.069 | 0.491 | 100.0% | **44.4%** |
| **HYPE** | 0.359 | 0.189 | 0.439 | 96.5% | **77.1%** |
| **DOGE** | 0.452 | 0.048 | 0.474 | 99.3% | **45.8%** |

*Key finding:* OFI has 3x to 9x greater standalone explanatory power than trade imbalance across all five assets. However, $TI$ remains significant in $44.4\%\text{--}77.1\%$ of crypto half-hours, far higher than the $\sim 31\%$ reported in the original 50-stock equity paper.

#### 7. Price-Volume Scaling Exponent $H$ (Table 12)

| Asset | Mean Exponent $\hat{H}$ | $|\text{OFI}|$ Standalone $R^2$ | $\text{VOL}^H$ Standalone $R^2$ | Joint Model $R^2$ | $|\text{OFI}|$ Sig | $\text{VOL}^H$ Sig |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BTC** | 0.149 | 0.237 | 0.156 | 0.343 | 94.4% | 98.6% |
| **ETH** | 0.111 | 0.319 | 0.136 | 0.395 | 97.2% | 86.1% |
| **SOL** | 0.091 | 0.232 | 0.080 | 0.286 | 91.0% | 75.7% |
| **HYPE** | 0.201 | 0.148 | 0.138 | 0.237 | 72.2% | 81.9% |
| **DOGE** | 0.063 | 0.245 | 0.051 | 0.275 | 84.7% | 34.7% |

*Key finding:* The estimated exponent $H$ ranges between $0.063$ and $0.201$, decisively rejecting the theoretical $H = 0.5$ square-root law.

### Independently reproduced

Not independently reproduced. All figures and tables represent third-party empirical findings reported by Yashar Ezzatpour and Ata Akbarizad Ahangari (`AHBAR-software-TM`) in GitHub commit `2af7b405dc1656bbaf5f4c3df4da5f91986c525c`.

### Negative evidence

1. **Severe Quote Sampling Degradation in Crypto:** Sparser quote sampling in July 2026 ($\sim 1.8$ quotes/10s bin) cut the empirical explanatory power ($R^2$) by roughly half compared to May/June ($12\text{--}18$ quotes/bin) across all five crypto perpetuals (e.g. ETH $R^2$ collapsed from $60.9\%$ to $34.3\%$, SOL from $52.5\%$ to $29.4\%$). Top-of-book OFI cannot accurately account for price revisions when intermediate book state changes are compressed into coarse snapshots (`source-reported`).
2. **Breakdown of Inverse Depth Scaling in BTC Perpetuals:** The theoretical inverse scaling law between price impact and resting depth ($\lambda = 1$) fails completely in BTC ($\lambda = -0.601, p < 0.001$), where higher recorded depth coincides with higher, not lower, price impact slope $\beta$ (`source-reported`).
3. **Heavy-Tailed Residual Kurtosis:** Regression residuals exhibit extreme excess kurtosis across all crypto assets (median $3.16\text{--}6.77$, max $150.55$ for SOL, $112.63$ for BTC), demonstrating that White HC0 standard errors and Gaussian $t$-statistics may overstate significance due to extreme tail events (`source-reported`).
4. **Failure of Square-Root Volume Law:** The estimated power-law exponent $H \in [0.063, 0.201]$ fails to support the widely cited square-root impact law ($H = 0.5$) in crypto perpetuals (`source-reported`).
5. **Intraday Market-Close Breakdown in Equities:** In both AAPL and AMZN, OFI explanatory power collapsed in the final 30 minutes of trading (AAPL $R^2$ dropped to $0.012$ with $\beta$ becoming statistically insignificant; AMZN $R^2$ dropped from $>0.75$ to $0.174$), indicating that market-on-close auction flows decouple prices from continuous quote dynamics (`source-reported`).

## Falsification plan

1. **Predictive Decoupling Test (Lagged OFI vs. Taker Costs):**
   - *Test:* Regress 1-bin forward price change $\Delta P_{k+1}$ on current $\text{OFI}_k$.
   - *Failure Rule:* Forward predictive $R^2 < 0.005$ (0.5%) or the implied gross return fails to exceed a 5.0 bps round-trip taker hurdle ($2 \times 2.5\text{ bps}$) (`research-defined falsification threshold`).
   - *Action:* Conclude that contemporaneous OFI reflects instantaneous market clearing rather than tradable directional alpha for takers.
2. **Sampling Frequency Stress Test:**
   - *Test:* Artificially downsample high-frequency quote streams to 30s, 60s, and 300s bins.
   - *Failure Rule:* If regression $R^2$ drops below $0.15$ or estimated $\beta$ standard errors expand by $>300\%$ (`research-defined falsification threshold`).
   - *Action:* Enforce a strict minimum quote-density gate on live data feeds before enabling microstructure execution.
3. **Out-of-Sample Parameter Stability Test:**
   - *Test:* Evaluate the predictive performance of rolling 30-minute estimated $\hat{\beta}_i$ out-of-sample over subsequent 2-hour holdout periods across high-volatility regime shifts.
   - *Failure Rule:* Realized out-of-sample prediction error exceeds the historical naive drift variance by $>10\%$ (`research-defined falsification threshold`).
   - *Action:* Reject the assumption of locally stationary price impact coefficients in crypto perpetuals.
4. **Ablation of Trade Imbalance Information:**
   - *Test:* Compare an OFI-only execution quoting model against an OFI + $TI$ dual-signal model.
   - *Failure Rule:* If removing $TI$ produces a statistically significant drop in net PnL or Sharpe ratio ($p < 0.01$) (`research-defined falsification threshold`).
   - *Action:* Reject pure top-of-book OFI as an adequate summary of crypto perpetual order flow; mandate inclusion of executed aggressor trade direction.

## Crypto portability

- **Portability Classification:** `direct` for contemporaneous price impact in centralized/decentralized perpetual order books; `adapted/unproven` for directional alpha strategies (`research-proposed`).
- **Primary Demonstration:** The cited research was conducted directly on cryptocurrency perpetuals on Hyperliquid (BTC, ETH, SOL, HYPE, DOGE), proving that the core OFI relationship ($\beta > 0$ in $100\%$ of half-hours, mean $R^2 \approx 44\%$) generalizes directly from equity markets to decentralized perpetual futures (`source-reported`).
- **Crypto-Specific Portability Nuances:**
  - *Perpetual Funding Rate Dynamics:* Divergence between perpetual mark price and spot index price induces funding arbitrage flows. When funding is heavily positive, continuous passive ask replenishment suppresses upward price impact, while aggressive liquidations create non-linear concave impact jumps (`research-proposed`).
  - *24/7 Session vs. Equity Auction Closes:* Crypto perpetuals lack market-on-close auctions. However, exchange settlement resets (e.g. 00:00 UTC) and funding payment timestamps (every 8 hours or hourly) induce localized volatility spikes and quote replenishment delays (`research-proposed`).
  - *Single-Venue Decentralized CLOB vs. Consolidated NBBO:* Unlike U.S. equities where NBBO aggregates multiple competing exchanges, Hyperliquid is a single execution venue. This eliminates inter-exchange routing latency but makes data feeds vulnerable to node-level quote sampling throttles (as observed in the July 2026 data drop) (`source-reported`).

## Limitations

- **Contemporaneous vs. Forward Predictive Gap:** The study demonstrates contemporaneous price impact ($\text{OFI}_k$ aligned with $\Delta P_k$). It does not demonstrate that past OFI predicts future returns net of taker fees (`source-reported`).
- **Short Sample Window:** Crypto evaluation is restricted to three single-day snapshots (May 1, June 1, July 1 2026), and equities to a single undated trading session. While containing millions of quote events, multi-month and multi-year regime shifts remain unstudied (`source-reported`).
- **Sampling Density Distortion:** Public API quote streaming on Hyperliquid experienced an 85% drop in observation density during the July 2026 capture, introducing substantial heterogeneity into the pooled depth-elasticity regressions (`source-reported`).
- **Underspecified Trade Execution Model:** The source does not model limit order queuing priority, cancel-to-fill ratios, or adverse selection incurred by passive liquidity providers attempting to capture OFI spread (`source-reported`).

## Implementation status

`not-implemented`.

This research record represents an external public research capture from GitHub repository `AHBAR-software-TM/price-impact-of-order-book-events`. No strategy implementation, automated trading logic, or backtesting harness has been created in PyBroker, NautilusTrader, paper trading, testnet, or live environments.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

Presence in this repository does not indicate that the strategy is profitable, approved for production, or cleared for live/testnet/paper deployment. It serves exclusively as normalized empirical research material for downstream hypothesis synthesis.

## Related Wiki records

- `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Tejas356: NASDAQ ITCH 40-level book OFI, contemporaneous impact vs predictive decoupling, and fee barrier falsification in INTC)
- `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md` (Rattandeep0500: Bivariate Hawkes self-excitation and multi-level CKS OFI on Binance BTCUSDT)
- `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31.md` (Cont-Kukanov-Stoikov multi-level OFI on crypto spot)
- `passive-market-impact-optimal-execution-mlofi-2026-09-02.md` (Multi-level OFI for passive market impact in execution algorithms)
- `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` (Falsification of retail cumulative volume delta and order flow indicators)

## Sources

1. Yashar Ezzatpour and Ata Akbarizad Ahangari (`AHBAR-software-TM`). *"The Price Impact of Order Book Events: Replication across Crypto Perpetual and Equity Markets"*, Academic Project Report for *Financial Machine Learning* (Spring 2026), Sharif University of Technology. Full text available in repository as `Full Report.pdf`.
   - Repository URL: [https://github.com/AHBAR-software-TM/price-impact-of-order-book-events](https://github.com/AHBAR-software-TM/price-impact-of-order-book-events)
   - Canonical Tree URL: [https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/tree/2af7b405dc1656bbaf5f4c3df4da5f91986c525c](https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/tree/2af7b405dc1656bbaf5f4c3df4da5f91986c525c)
   - Full Report PDF: [`Full Report.pdf`](https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/blob/2af7b405dc1656bbaf5f4c3df4da5f91986c525c/Full%20Report.pdf)
   - Master Replication Notebook: [`price_impact_order_book_events.ipynb`](https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/blob/2af7b405dc1656bbaf5f4c3df4da5f91986c525c/price_impact_order_book_events.ipynb)
   - Project README: [`README.md`](https://github.com/AHBAR-software-TM/price-impact-of-order-book-events/blob/2af7b405dc1656bbaf5f4c3df4da5f91986c525c/README.md)
2. Rama Cont, Arseniy Kukanov, and Sasha Stoikov. *"The Price Impact of Order Book Events"*. *Journal of Financial Econometrics*, 12(1):47–88, 2014. DOI: [10.1093/jjfinec/nbt003](https://doi.org/10.1093/jjfinec/nbt003).
