---
schema: strategy-research-record-v1
title: "Binance Perpetual Order Flow Imbalance: Microsecond-to-Second Horizon Decay, Static Queue Imbalance Dominance, and Retail Taker Cost Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - market-microstructure
  - order-flow-imbalance
  - limit-order-book
  - queue-imbalance
  - high-frequency-trading
  - price-impact
  - falsification
  - negative-evidence
  - transaction-costs
status: research-only
confidence: high
source_as_of: 2026-08-26
sources:
  - "https://github.com/armaansg/orderbook-microstructure/tree/dbb79885153bd16d1f736c10b71eb1bd26c5034d"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/README.md"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/docs/results.md"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/config/corpus.yaml"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/src/obmicro/features/ofi.py"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/src/obmicro/features/bars.py"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/src/obmicro/eval/dataset.py"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/src/obmicro/eval/regress.py"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/src/obmicro/eval/moments.py"
  - "https://github.com/armaansg/orderbook-microstructure/blob/dbb79885153bd16d1f736c10b71eb1bd26c5034d/src/obmicro/eval/run.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance Perpetual Order Flow Imbalance: Microsecond-to-Second Horizon Decay, Static Queue Imbalance Dominance, and Retail Taker Cost Falsification

## Provenance

- **Primary Source Repository:** `armaansg/orderbook-microstructure` (*obmicro: Reproducible study of order flow imbalance as a predictor of short-horizon returns, on 30 days of Binance BTCUSDT bookTicker data. 100 ms bars, Newey-West HAC regressions, out-of-sample split on whole days with an embargo*), authored by Armaan Goraya (`armaansg`) (`source-reported`).
- **Canonical Source Identity:** GitHub repository `https://github.com/armaansg/orderbook-microstructure` at immutable commit SHA `dbb79885153bd16d1f736c10b71eb1bd26c5034d` (committed 2026-08-26 18:31:47 UTC; empirical results report generated 2026-08-17 19:13 UTC) (`source-reported`).
- **Foundational Econometric Reference:** Cont, R., Kukanov, A., & Stoikov, S. (2014), *The Price Impact of Order Book Events*, Journal of Econometrics, 178(2), 314–325 (`source-reported`).
- **Primary Source Files Directly Inspected:**
  - `README.md`: Architectural specification detailing bounded memory streaming, transition boundary stitching across Arrow blocks, timestamp discipline (`event_time` vs `transaction_time`), and execution costs (`source-reported`).
  - `docs/results.md`: Complete tabular summary of in-sample and out-of-sample OLS regressions, Newey-West HAC t-statistics, information coefficients, and hit rates across 4 prediction horizons and 5 model configurations (`source-reported`).
  - `config/corpus.yaml`: Pinned corpus specification defining instrument (`BTCUSDT`), market (`futures/um`), feed (`bookTicker`), resolution (`100 ms`), date bounds (2024-03-01 to 2024-03-30), and pre-registered quality gates (`source-reported`).
  - `src/obmicro/features/ofi.py`: Canonical 6-case event-level Cont-Kukanov-Stoikov OFI implementation, arithmetic mid-price, crossed-size microprice, and static queue imbalance (`source-reported`).
  - `src/obmicro/features/bars.py`: Zero-extraction streaming accumulator aggregating raw `bookTicker` diffs into 100 ms uniform clock bars, stitching boundary transitions, tracking latency histograms, and forward-filling empty quote buckets (`source-reported`).
  - `src/obmicro/eval/dataset.py`: Multi-horizon forward return target generation, depth-normalized OFI scaling ($OFI / depth\_mean$), within-day-only lag shifting, quality gate filtering, and time-ordered train/embargo/test dataset splitting (`source-reported`).
  - `src/obmicro/eval/regress.py`: OLS estimation, Newey-West HAC lag selection ($1.5 \times horizon$), out-of-sample $R^2$ benchmarked to training mean, and baseline comparison harness (`source-reported`).
  - `src/obmicro/eval/moments.py`: Streaming sufficient statistics accumulator computing cross-product matrices $(X'X, X'y, y'y)$ and Bartlett kernel HAC covariances per calendar day without cross-day leakage (`source-reported`).
  - `src/obmicro/eval/run.py`: Automated markdown report generation pipeline and baseline verdict logic (`source-reported`).
  - `tests/test_ofi.py` and `tests/test_eval.py`: Unit test suites verifying sign correctness, reflection antisymmetry, and day-seam leakage protections (`source-reported`).
- **Deduplication Audit:** A comprehensive audit across all strategy records in this repository confirms zero pre-existing records citing `armaansg`, `orderbook-microstructure`, or the Binance `bookTicker` historical archive corpus. Related records in the repository evaluate distinct asset classes or methodologies: `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` evaluates Tejas Mungale's NASDAQ equity LOBSTER study (INTC/GOOG); `crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13.md` evaluates Anupam Patil's 1-to-15 minute online-SGD models on Coinbase spot (`BTC-USD`); `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md` evaluates Rattandeep Singh's bivariate self-exciting point processes; and `yushingtoncity/binance-orderflow-microstructure` evaluates order flow sign entropy. Armaan Goraya's study provides an independent, rigorously bounded out-of-sample empirical investigation of canonical Cont-Kukanov-Stoikov top-of-book OFI on Binance USD-M futures at 100 ms to 5 s horizons, providing an explicit falsification of dynamic OFI dominance against static queue imbalance at horizons $\ge 500$ ms and proving that the predictive effect is an order of magnitude smaller than the retail taker fee barrier.

## Economic mechanism

### Source-reported

1. **Order Book Event Price Impact (Cont-Kukanov-Stoikov 2014):**
   In limit order book markets, price movements are driven by the accumulation of order book events at the best quotes. The Order Flow Imbalance (OFI) metric measures the net volume consumed or supplied at the top of the book across consecutive states. When demand exceeds supply ($OFI > 0$), aggressive buying exhausts existing ask depth and new limit bids arrive at higher prices, mechanically inducing an upward shift in the mid-price. Conversely, net selling ($OFI < 0$) exhausts bids and lowers the ask, driving the mid-price downward (`source-reported`).
2. **Elasticity and Depth Normalization:**
   Raw OFI measured in base currency units (e.g., BTC contracts) is not stationary across time or volatility regimes because a given volume shock moves a thin order book substantially further than a deep, highly liquid book. Dividing aggregated OFI by the mean prevailing top-of-book depth ($depth\_mean = q^b + q^a$) transforms the regressor into a dimensionless queue elasticity measure, making impact coefficients comparable across days (`source-reported`).
3. **Horizon-Dependent Predictive Decay:**
   The source tests whether top-of-book OFI acts as a leading predictor of forward price changes over horizons from 100 ms to 5 s. While order flow imbalance exhibits massive statistical significance contemporaneously and at ultra-short horizons (100 ms), its marginal predictive power decays rapidly as the observation window lengthens (`source-reported`).
4. **The Baseline Falsification Question (OFI vs Static Queue Imbalance):**
   A critical scientific question posed by the source is whether dynamic OFI—which requires continuous, message-by-message event tracking—provides superior out-of-sample explanatory power compared to cost-free, static top-of-book queue imbalance ($qimb = (q^b - q^a)/(q^b + q^a)$). The empirical study demonstrates that at ultra-short horizons (100 ms), OFI achieves higher out-of-sample $R^2$ ($0.03274$ vs $0.02819$). However, at every longer horizon tested ($500\text{ ms}, 1\text{ s}, 5\text{ s}$), static queue imbalance decisively outperforms OFI (e.g., at 1 s, $qimb$ $R^2_{OOS} = 0.05414$ vs $OFI$ $R^2_{OOS} = 0.01717$). The dynamic history of order book transitions adds negligible marginal information over a simple snapshot of the prevailing queue state once the horizon exceeds 500 ms (`source-reported`).

### Research interpretation

- **Transient Liquidity Exhaustion vs Permanent Information:**
  The rapid decay of OFI's predictive advantage past 100 ms highlights the microstructural difference between instantaneous liquidity depletion and fundamental price discovery. At 100 ms, OFI measures the immediate mechanical residue of incoming market orders sweeping resting liquidity. By 500 ms to 1 s, automated market-making algorithms have already responded to the event by replenishing the depleted side or widening spreads, resetting the local supply-demand balance. The remaining predictable drift is driven primarily by the persistent structural skew of resting limit liquidity (queue imbalance) rather than the historical trajectory of how that liquidity arrived.
- **Microstructural Adverse Selection & The Taker Fee Wall:**
  At 1 s, a 1-standard-deviation shock in depth-scaled OFI predicts a mid-price move of $+0.1623$ basis points ($0.001623\%$). Standard exchange taker fees on Binance USD-M futures range from $2.0$ to $5.0$ bps per side ($4.0$ to $10.0$ bps round-trip) for VIP0/retail accounts, and average half-spreads on BTCUSDT fluctuate between $0.5$ and $1.0$ bps. Because the total gross predictive drift ($~0.16$ bps) is more than $25\times$ smaller than round-trip taker friction, trading OFI as an aggressive taker directional alpha is mathematically unviable. The signal carries practical value only as a passive execution filter—enabling market makers and TWAP execution algorithms to shade quotes, adjust queue priority, or pause aggressive buying when order flow turns adverse.

## Signal

### Mathematical Formulation

- **Event-Level OFI Contribution:**
  For two consecutive top-of-book states $n-1 \to n$, the event contribution $e_n$ is defined across six mutually exclusive conditions (`source-reported`):
  $$e_n = \mathbf{1}_{\{P_n^b \ge P_{n-1}^b\}} q_n^b - \mathbf{1}_{\{P_n^b \le P_{n-1}^b\}} q_{n-1}^b - \mathbf{1}_{\{P_n^a \le P_{n-1}^a\}} q_n^a + \mathbf{1}_{\{P_n^a \ge P_{n-1}^a\}} q_{n-1}^a$$
  - Bid price increases ($P_n^b > P_{n-1}^b$): $+q_n^b$ (positive / buy pressure).
  - Bid price decreases ($P_n^b < P_{n-1}^b$): $-q_{n-1}^b$ (negative / sell pressure).
  - Bid price unchanged ($P_n^b = P_{n-1}^b$): $+ (q_n^b - q_{n-1}^b)$ (size delta).
  - Ask price decreases ($P_n^a < P_{n-1}^a$): $-q_n^a$ (negative / sell pressure).
  - Ask price increases ($P_n^a > P_{n-1}^a$): $+q_{n-1}^a$ (positive / buy pressure).
  - Ask price unchanged ($P_n^a = P_{n-1}^a$): $- (q_n^a - q_{n-1}^a)$ (size delta).
- **100 ms Bar Aggregation:**
  Within each fixed clock-time bucket $t$ of width $\Delta t = 100\text{ ms}$, total OFI is the sum of event contributions (`source-reported`):
  $$OFI_t = \sum_{k \in \text{bucket } t} e_k$$
  Boundary transitions spanning consecutive Arrow streaming blocks are explicitly stitched to eliminate boundary truncation bias (`source-reported`).
- **Depth-Scaled Regressor:**
  $$OFI_{scaled, t} = \frac{OFI_t}{depth\_mean_t}$$
  where $depth\_mean_t = \frac{1}{N_t} \sum_{k \in \text{bucket } t} (q_k^b + q_k^a)$ is the time-weighted average combined top-of-book depth (`source-reported`).
- **Static Queue Imbalance Regressor:**
  $$qimb_k = \frac{q_k^b - q_k^a}{q_k^b + q_k^a} \in [-1, 1], \quad qimb\_mean_t = \frac{1}{N_t} \sum_{k \in \text{bucket } t} qimb_k$$
  Evaluates to 0 if the top of the book is empty (`source-reported`).
- **Control Regressors:**
  - Lagged return: $ret\_lag1_t = \ln(mid\_last_t / mid\_last_{t-1}) \times 10^4$ (in basis points) (`source-reported`).
  - Lagged OFI: $ofi\_lag1_t = OFI_{t-1}$ (`source-reported`).
  - Relative spread: $spread\_bps_t = (spread\_mean_t / mid\_last_t) \times 10^4$ (in basis points) (`source-reported`).
- **Forward Return Prediction Target:**
  $$fwd_{h, t} = \ln\left(\frac{mid\_last_{t+h}}{mid\_last_t}\right) \times 10^4 \quad (\text{bps})$$
  evaluated across four horizons: $h \in \{1, 5, 10, 50\}$ bars, corresponding to $100\text{ ms}$, $500\text{ ms}$, $1\text{ s}$, and $5\text{ s}$ (`source-reported`).
- **Regression Models Evaluated:**
  1. `ofi`: $fwd_{h, t} = \alpha + \beta \cdot OFI_{scaled, t} + \epsilon_t$ (`source-reported`).
  2. `qimb`: $fwd_{h, t} = \alpha + \beta \cdot qimb\_mean_t + \epsilon_t$ (`source-reported`).
  3. `ret_lag`: $fwd_{h, t} = \alpha + \beta \cdot ret\_lag1_t + \epsilon_t$ (`source-reported`).
  4. `ofi_qimb`: $fwd_{h, t} = \alpha + \beta_1 \cdot OFI_{scaled, t} + \beta_2 \cdot qimb\_mean_t + \epsilon_t$ (`source-reported`).
  5. `full`: $fwd_{h, t} = \alpha + \beta_1 \cdot OFI_{scaled, t} + \beta_2 \cdot qimb\_mean_t + \beta_3 \cdot ret\_lag1_t + \beta_4 \cdot spread\_bps_t + \beta_5 \cdot ofi\_lag1_t + \epsilon_t$ (`source-reported`).

### Execution & Operational Signal Mapping

- **Formation Timestamp:** Close of each 100 ms clock bucket, strictly indexed by exchange `event_time` (`source-reported`).
- **Trading Signal Mapping (`research-proposed`):**
  - Continuous predicted drift: $\hat{y}_t = \mathbf{x}_t \hat{\boldsymbol{\beta}}$.
  - Directional Entry Threshold: Enter long if $\hat{y}_t > +\theta$; enter short if $\hat{y}_t < -\theta$, where $\theta = 0.25\text{ bps}$ (`research-proposed`).
  - Order Execution: Resting passive limit order at prevailing mid-price or top-of-book post-only order; taker market orders are strictly prohibited by fee economics (`research-proposed`).
  - Holding Horizon: Fixed time exit after $h = 10$ bars (1 second) or upon sign reversal of $\hat{y}_{t+k}$ (`research-proposed`).
  - Position Sizing: Fixed unit risk or linear sizing proportional to $\min(|\hat{y}_t| / \theta, 1.0)$ (`research-proposed`).

## Required data

- **Instrument / Symbol:** `BTCUSDT` linear perpetual futures (`source-reported`).
- **Venue:** Binance Futures USDⓈ-M (`source-reported`).
- **Market Type:** Centralized exchange linear perpetual swap (`futures/um`) (`source-reported`).
- **Data Product:** Binance historical archive `bookTicker` daily compressed CSV files (`data.binance.vision`) (`source-reported`).
- **Data Fields:**
  - `best_bid_price` (float64)
  - `best_bid_qty` (float64)
  - `best_ask_price` (float64)
  - `best_ask_qty` (float64)
  - `transaction_time` (int64, epoch ms)
  - `event_time` (int64, epoch ms)
  - `update_id` (int64) (`source-reported`).
- **Timeframe & Resolution:** 100 ms uniform clock-time bars ($864,000$ buckets per 24-hour UTC calendar day) (`source-reported`).
- **Causality & Data Hygiene Guarantees:**
  - `event_time` is used exclusively for bar bucketing; mixing with `transaction_time` leaks cross-network latency (`source-reported`).
  - Forward returns are shifted strictly within each calendar day; returns never span across day seams, eliminating boundary splice distortion (`source-reported`).
  - Empty buckets (buckets with zero order book events, ~3% of all buckets) have $OFI = 0$ and forward-filled quotes; they are explicitly purged from regression rows to prevent artificial $(0,0)$ inflation of $R^2$ (`source-reported`).
  - Pre-registered Quality Gates: Days are rejected prior to fitting if coverage $< 90\%$, crossed books $> 1000$, non-monotonic update IDs occur, or mean latency $> 1000\text{ ms}$ (`source-reported`).
  - Train/Test Split: 18 calendar days train, 1-day embargo (2024-03-21), 8 calendar days test (`source-reported`).

## Execution assumptions

- **Econometric vs Tradable Nature:** The primary source investigates econometric mid-price predictability rather than executing simulated order fills (`source-reported`).
- **Execution Cost Barrier:**
  - Binance USD-M VIP0 standard taker fee: $0.05\%$ ($5.0$ bps) per side ($10.0$ bps round-trip); reduced VIP0 with BNB deduction: $0.045\%$ per side ($9.0$ bps round-trip) (`source-reported` / `research-proposed`).
  - Institutional VIP9 taker fee: $0.017\%$ ($1.7$ bps) per side ($3.4$ bps round-trip) (`research-proposed`).
  - Typical BTCUSDT top-of-book spread: $0.5$ to $1.5$ bps (`spread_bps` mean $\approx 1.0$ bp) (`source-reported`).
  - Half-spread cost to cross the book: $\approx 0.5$ bps (`research-proposed`).
- **Fill Delay:** Typical exchange feed latency on Binance `bookTicker` is observed at $7$ to $11\text{ ms}$ (median), with p99 at $22\text{ ms}$ (`source-reported`). A 100 ms execution loop operates comfortably within the latency envelope for collocated or low-latency cloud nodes (`research-proposed`).
- **Passive Limit Queue Reality:** Capturing the $0.16$ bp drift via passive maker orders requires queuing at the best bid/ask; however, adverse selection dictates that limit orders are disproportionately filled when toxic adverse flow sweeps the queue (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below trace directly to `docs/results.md` generated by `obmicro.eval.run` from 27 qualifying days in March 2024 (21,117,280 total fitted/scored bars; 14,727,553 train bars; 6,389,727 test bars) (`source-reported`).

#### 1. Out-of-Sample Empirical Regression Table (March 2024 Panel)

Features are z-scored using training set moments only. $\beta$ represents the forward move in basis points per one standard deviation of the regressor. $t(\text{HAC})$ uses Newey-West standard errors with Bartlett kernel lags scaled to $1.5 \times horizon$ (1 to 75 lags) to account for overlapping return autocorrelation. $R^2_{OOS}$ is evaluated against the training mean (`source-reported`).

| Horizon | Model | $\beta$ (OFI) | $t$ (HAC) | $R^2$ In-Sample | $R^2$ OOS | IC OOS | Hit Rate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **100 ms** | `ofi` | +0.0682 | +337.8 | 0.03201 | **0.03274** | 0.1820 | 0.771 |
| 100 ms | `qimb` | +0.0635 | +675.0 | 0.02779 | 0.02819 | 0.1824 | 0.863 |
| 100 ms | `ret_lag` | +0.0382 | +36.5 | 0.01006 | 0.01215 | 0.1106 | 0.663 |
| 100 ms | `ofi_qimb` | +0.0517 | +246.6 | 0.04369 | 0.04730 | 0.2226 | 0.879 |
| 100 ms | `full` | +0.0601 | +58.2 | 0.04445 | 0.04767 | 0.2239 | 0.881 |
| **500 ms** | `ofi` | +0.1374 | +258.9 | 0.02097 | 0.02389 | 0.1547 | 0.658 |
| 500 ms | `qimb` | +0.1788 | +461.7 | 0.03548 | **0.05178** | 0.2333 | 0.779 |
| 500 ms | `ret_lag` | +0.0768 | +46.8 | 0.00655 | 0.00702 | 0.0838 | 0.577 |
| 500 ms | `ofi_qimb` | +0.0825 | +155.3 | 0.04199 | 0.05960 | 0.2469 | 0.784 |
| 500 ms | `full` | +0.1001 | +73.1 | 0.04269 | 0.06064 | 0.2490 | 0.786 |
| **1 s** | `ofi` | +0.1623 | +198.1 | 0.01370 | 0.01717 | 0.1310 | 0.612 |
| 1 s | `qimb` | +0.2414 | +338.9 | 0.03031 | **0.05414** | 0.2345 | 0.731 |
| 1 s | `ret_lag` | +0.0900 | +43.7 | 0.00422 | 0.00477 | 0.0692 | 0.550 |
| 1 s | `ofi_qimb` | +0.0844 | +103.0 | 0.03350 | 0.05765 | 0.2409 | 0.734 |
| 1 s | `full` | +0.1058 | +60.3 | 0.03412 | 0.05854 | 0.2427 | 0.735 |
| **5 s** | `ofi` | +0.1870 | +89.6 | 0.00328 | 0.00515 | 0.0724 | 0.544 |
| 5 s | `qimb` | +0.3440 | +132.9 | 0.01111 | **0.02439** | 0.1562 | 0.607 |
| 5 s | `ret_lag` | +0.0940 | +23.9 | 0.00083 | 0.00140 | 0.0389 | 0.518 |
| 5 s | `ofi_qimb` | +0.0689 | +32.3 | 0.01150 | 0.02482 | 0.1576 | 0.607 |
| 5 s | `full` | +0.1069 | +31.6 | 0.01265 | 0.02507 | 0.1584 | 0.607 |

#### 2. Head-to-Head Baseline Comparison (Single-Regressor OOS $R^2$)

| Horizon | Best Single Regressor | Best $R^2_{OOS}$ | `ofi` $R^2_{OOS}$ | Empirical Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **100 ms** | `ofi` | **0.03274** | 0.03274 | **OFI wins** |
| **500 ms** | `qimb` | **0.05178** | 0.02389 | **`qimb` wins** ($+117\%$ higher $R^2$) |
| **1 s** | `qimb` | **0.05414** | 0.01717 | **`qimb` wins** ($+215\%$ higher $R^2$) |
| **5 s** | `qimb` | **0.02439** | 0.00515 | **`qimb` wins** ($+374\%$ higher $R^2$) |

#### 3. Data Quality Gate Exclusions

Three days were automatically excluded by pre-registered data-quality gates (`source-reported`):
- `2024-03-08`: Excluded due to coverage $= 0.8687 < 0.90$ and severe feed latency spike ($mean\_latency = 15,507\text{ ms} > 1,000\text{ ms}$) (`source-reported`).
- `2024-03-09`: Excluded due to coverage $= 0.8597 < 0.90$ (`source-reported`).
- `2024-03-30`: Excluded due to coverage $= 0.8718 < 0.90$ (`source-reported`).

### Independently reproduced

- Not independently reproduced. All metrics and tabular regressions represent primary research outputs reported by Armaan Goraya in repository `armaansg/orderbook-microstructure` (commit `dbb79885153bd16d1f736c10b71eb1bd26c5034d`).

### Negative evidence

1. **Decisive Loss to Static Queue Imbalance at $h \ge 500$ ms:**
   At all horizons exceeding 100 ms, static queue imbalance ($qimb$) substantially beats dynamic order flow imbalance ($OFI$). At the 1-second horizon, $qimb$ delivers an out-of-sample $R^2$ of $0.05414$ versus $0.01717$ for $OFI$. Because queue imbalance requires only the current top-of-book snapshot and no historical event sequence, it represents a more parsimonious and econometrically powerful explanatory variable (`source-reported`).
2. **Economic Non-Tradability for Directional Takers:**
   At 1 second, a one-standard-deviation increase in depth-scaled OFI predicts only $+0.1623$ bps of price movement. Comparing this $+0.16$ bp gross drift against the minimum round-trip taker cost of $4.0$ to $10.0$ bps (plus half-spread of $0.5$ bps) proves that OFI cannot generate positive net returns as a standalone taker strategy (`source-reported` / `research-proposed`).
3. **Rapid Predictive Half-Life Decay:**
   Between 100 ms and 5 s, the out-of-sample $R^2$ of OFI collapses from $0.03274$ to $0.00515$ (an $84.3\%$ decline), and its information coefficient drops from $0.1820$ to $0.0724$. Any execution delay exceeding a few hundred milliseconds eliminates the bulk of the signal's predictive content (`source-reported`).

## Falsification plan

1. **Taker Net Expectancy Stress Test:**
   - *Test:* Construct an aggressive market-order backtest triggered when predicted 1-second drift $\hat{y}_t > \theta$ under realistic taker fees ($2.0\text{ bps}$ maker / $5.0\text{ bps}$ taker) and effective half-spreads.
   - *Decision Rule:* If simulated net expectancy is negative across all tested thresholds $\theta \in [0.1, 2.0]\text{ bps}$ (`research-defined falsification threshold`), confirm the formal falsification of standalone directional OFI taker trading.
2. **Multi-Asset Altcoin Persistence Test:**
   - *Test:* Evaluate the identical 100 ms CKS OFI versus queue imbalance regression on high-beta altcoin perpetuals (`ETHUSDT`, `SOLUSDT`, `DOGEUSDT`) across 30-day panels.
   - *Decision Rule:* If static queue imbalance fails to outperform OFI at 1 s on $> 50\%$ of tested altcoin assets (`research-defined falsification threshold`), reject the hypothesis that queue imbalance dominance is universal across crypto perpetuals.
3. **Out-of-Sample Regime Shift Test:**
   - *Test:* Replay the regression models on modern 2026 Binance L2 tick data (or Coinbase `level2_batch`).
   - *Decision Rule:* If out-of-sample $R^2_{OOS}$ at 100 ms falls below $0.010$ or $t(\text{HAC})$ falls below $10.0$ (`research-defined falsification threshold`), conclude that algorithmic quote recycling has degraded the 100 ms OFI price impact mechanism.
4. **Passive Maker Adverse Selection Audit:**
   - *Test:* Simulate passive limit orders placed at the mid-price conditioned on positive OFI ($OFI_{scaled} > 1.0$), tracking post-fill markouts at 1 s, 5 s, and 30 s.
   - *Decision Rule:* If passive fills incur negative post-fill markouts ($< -0.5\text{ bps}$) over $\ge 65\%$ of fills (`research-defined falsification threshold`), reject the use of OFI as a passive maker shading filter due to insurmountable adverse selection.

## Crypto portability

- **Portability Classification:** `direct` (`source-reported`).
- **Rationale:** The primary source investigates Binance USD-M futures `BTCUSDT` perpetual contracts directly, utilizing Binance's historical public `bookTicker` dataset.
- **Portability Specifics & Microstructure Considerations:**
  - *Data Feed Discontinuation:* Binance permanently discontinued the public historical `bookTicker` daily archive after 2024-04-30. Implementing this signal in production requires continuous recording of live WebSocket feeds (`wss://fstream.binance.com/ws/btcusdt@bookTicker`) or reconstructing top-of-book dynamics from real-time depth diffs (`@depth` / `@depthUpdate`) (`source-reported`).
  - *24/7 Continuous Trading:* Unlike equity markets with opening and closing auctions, crypto perpetual order books run continuously. However, cross-day seams in historical files must still be handled with strict purge and embargo protocols to prevent synthetic boundary artifacts (`source-reported`).
  - *Perpetual Funding Rate Neutrality:* Because the signal horizon is ultra-short ($100\text{ ms}$ to $5\text{ s}$), funding rate accrual (which occurs every 8 hours) has negligible direct impact on per-trade returns, though extreme funding regimes may alter the baseline bid-ask queue asymmetry (`research-proposed`).

## Limitations

- **Top-of-Book Restriction:** The study is restricted to Level 1 best bid and best ask quotes (`bookTicker`). It does not incorporate deep Level 2 order book updates (Levels 2–20), iceberg orders, or hidden liquidity.
- **Fixed Calendar Window:** The empirical corpus spans a single month (March 2024, 27 qualifying days). While it encompasses $> 21$ million observations, it does not capture multi-year structural regime shifts, prolonged low-volatility bear markets, or exchange liquidity crises.
- **Archive Discontinuation:** The Binance historical archive for `bookTicker` ended in April 2024, meaning exact historical out-of-sample extensions past this date cannot use the identical static archive product and must transition to recorded WebSocket streams.
- **Econometric vs P&L Gap:** High statistical t-statistics ($t > 300$) in OLS regressions do not equal trading profits; the magnitude of the signal is completely dominated by the bid-ask spread and exchange trading fees.

## Implementation status

- Frontmatter: `implementation_status: not-implemented`
- The strategy logic and econometric models are fully implemented and verified in Armaan Goraya's upstream repository `armaansg/orderbook-microstructure`.
- No NautilusTrader, PyBroker, paper trading, testnet, or live trading implementation exists in the current system.

## Adoption boundary

- Frontmatter: `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
- This record serves strictly as a quantitative research capture and falsification benchmark for order flow imbalance and queue imbalance dynamics.
- It does not authorize strategy adoption, automated signal generation, paper trading, testnet execution, or capital deployment.

## Related Wiki records

- `[[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]]` — Evaluates Tejas Mungale's NASDAQ equity LOBSTER study demonstrating contemporaneous-to-predictive decoupling and taker cost barriers.
- `[[quant/crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13]]` — Evaluates Anupam Patil's online-SGD microstructure models on Coinbase spot (`BTC-USD`), showing failure to clear retail taker fees.
- `[[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]]` — Evaluates Rattandeep Singh's bivariate Hawkes self-exciting point process on Binance BTCUSDT.
- `[[quant/clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03]]` — Evaluates unsupervised clustering of order flow imbalance states across depth levels.
- `[[quant/crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]` — Evaluates multi-level order flow imbalance forecasting on crypto perpetuals.

## Sources

- **Primary Research Codebase:** Armaan Goraya (`armaansg`), *obmicro: Reproducible study of order flow imbalance as a predictor of short-horizon returns, on 30 days of Binance BTCUSDT bookTicker data. 100 ms bars, Newey-West HAC regressions, out-of-sample split on whole days with an embargo*, GitHub repository `https://github.com/armaansg/orderbook-microstructure` at commit SHA `dbb79885153bd16d1f736c10b71eb1bd26c5034d` (committed 2026-08-26 18:31:47 UTC) (`source-reported`).
- **Research Results Monograph:** `docs/results.md` in `armaansg/orderbook-microstructure` (generated 2026-08-17 19:13 UTC by `obmicro.eval.run`) (`source-reported`).
- **Corpus & Quality Protocol:** `config/corpus.yaml` in `armaansg/orderbook-microstructure` (`source-reported`).
- **Feature Engineering Implementations:** `src/obmicro/features/ofi.py` and `src/obmicro/features/bars.py` in `armaansg/orderbook-microstructure` (`source-reported`).
- **Econometric Estimation & Dataset Harness:** `src/obmicro/eval/dataset.py`, `src/obmicro/eval/regress.py`, `src/obmicro/eval/moments.py`, and `src/obmicro/eval/run.py` in `armaansg/orderbook-microstructure` (`source-reported`).
- **Correctness & Leakage Test Suites:** `tests/test_ofi.py` and `tests/test_eval.py` in `armaansg/orderbook-microstructure` (`source-reported`).
- **Foundational Microstructure Literature:** Cont, R., Kukanov, A., & Stoikov, S. (2014), *The Price Impact of Order Book Events*, Journal of Econometrics, 178(2), 314–325. DOI: [10.1016/j.jeconom.2013.07.005](https://doi.org/10.1016/j.jeconom.2013.07.005) (`source-reported`).
