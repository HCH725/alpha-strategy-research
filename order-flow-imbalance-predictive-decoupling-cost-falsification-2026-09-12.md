---
schema: strategy-research-record-v1
title: "Order Flow Imbalance Contemporaneous-to-Predictive Decoupling and Microstructure Taker Cost Falsification"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - microstructure
  - order-flow-imbalance
  - limit-order-book
  - price-impact
  - falsification
  - latency-decay
  - high-frequency-trading
status: research-only
confidence: high
source_as_of: 2026-09-07
sources:
  - "https://github.com/Tejas356/limit_order_book_engine (commit a2270d70256f292b7d5d11df30a61fd1d6374ba9, September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Order Flow Imbalance Contemporaneous-to-Predictive Decoupling and Microstructure Taker Cost Falsification

## Provenance

- **Primary Source Codebase:** Tejas Mungale (`Tejas356`), *limit_order_book_engine: Limit order book reconstruction in C++ validated message-by-message against an independent oracle, with an order flow imbalance study that separates price impact from prediction*.
- **Canonical Source Identity:** GitHub repository `Tejas356/limit_order_book_engine` at immutable commit `a2270d70256f292b7d5d11df30a61fd1d6374ba9`, dated 2026-09-07 17:30:42 +0100.
- **Repository URL:** [https://github.com/Tejas356/limit_order_book_engine](https://github.com/Tejas356/limit_order_book_engine)
- **Primary Research Files in Repository:**
  - `README.md` — Architectural specification, headline findings, and core empirical results.
  - `SPEC.md` — Full fourteen-step research plan, design principles, mathematical derivations, and falsification criteria.
  - `NOTES.md` — 1,292-line empirical log containing complete twenty-cell regression tables, depth-scaling quintiles, latency decay measurements, and cost reality checks.
  - `src/ofi.cpp` — Analytical OFI increment ($e_n$) formulation and accumulation engine following Cont, Kukanov and Stoikov (2014).
  - `src/features.cpp` — Book feature extraction (mid-price, microprice with opposite-size weighting, spread in ticks, queue imbalance, depth imbalance).
  - `src/regression.cpp` — Numerically stable two-pass OLS regression and Spearman rank correlation with exact tie handling.
  - `analysis/analyse.py` & `analysis/validate_regressions.py` — Python verification scripts cross-checking C++ outputs against `statsmodels` and `scipy` to machine epsilon ($10^{-12}$ to $10^{-16}$).
- **Empirical Dataset:** NASDAQ LOBSTER Level-10 order book and message data for 2012-06-21 (09:30:00 to 16:00:00 EST, 34,200 to 57,600 seconds after midnight), covering INTC (624,040 messages) and GOOG (147,916 messages).
- **Repository Deduplication Audit:** Checked all existing markdown records in `alpha-strategy-research`. Zero prior records cite `Tejas356`, `limit_order_book_engine`, commit `a2270d7`, or this specific empirical decoupling between contemporaneous impact and forward predictability. Related microstructure records (`hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md`, `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31.md`, `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`) evaluate Hawkes point-process self-excitation or crypto CVD divergences; none address the contemporaneous-to-predictive collapse, queue-imbalance baseline dominance, or taker half-spread falsification boundary documented here.

## Economic mechanism

### Source-reported

The primary research investigates the economic validity of Order Flow Imbalance (OFI) as a predictive alpha signal across two distinct market regimes (the tick-constrained, liquid equity INTC and the wide-spread, low-message-rate equity GOOG):

1. **The Price Impact Tautology vs. Forward Return Prediction:**
   - Cont, Kukanov and Stoikov (CKS, 2014) established that regressing the mid-price change over an interval on the OFI over the *same* interval ($\Delta P_k = \alpha + \beta \cdot OFI_k + \epsilon_k$) yields a high $R^2$ (exceeding 0.60 to 0.68).
   - *Source finding:* This relationship is a **price impact description**, not an alpha forecast. Aggressive market orders and touch revisions are the physical mechanism by which price moves within an interval; regressing price change on contemporaneous flow is close to tautological at short horizons. When testing the required trading condition—regressing the *next* interval's price change on *this* interval's OFI ($\Delta P_{k+1} = \alpha + \beta \cdot OFI_k + \epsilon_k$)—predictive $R^2$ collapses by **10x to 2,898x** (falling to $< 0.049$ across all horizons, and $< 0.005$ for all clock horizons).
2. **Static Queue Imbalance Baseline Dominance:**
   - *Source finding:* On liquid, tick-constrained equities (INTC), a simple one-line static Queue Imbalance ($QI = \frac{q^b - q^a}{q^b + q^a}$) beats the dynamic four-term OFI signal at **every single horizon** by a factor of 1.5x to 2.5x in predictive Information Coefficient (IC).
3. **Decisive Cost Reality Check (Falsification of Taker Alpha):**
   - *Source finding:* When comparing expected gain per trade ($\approx IC \times \sigma(\Delta P)$) against the half-spread required to take liquidity, the maximum edge-to-cost ratio across the entire twenty-cell grid is **0.31** (INTC event-1000 at 0.310 and INTC 30s at 0.297; GOOG event-1000 at 0.227; sub-second horizons at 0.011 to 0.039). Not a single cell comes within a factor of three of paying the half-spread alone. Standalone directional taker trading on OFI is economically falsified.

### Research interpretation

This research exposes a foundational methodological trap prevalent in quantitative trading literature and retail alpha generation:

- **The Microstructure `.shift()` Illusion:** Presenting contemporaneous price impact ($R^2 \approx 0.65$) as predictive alpha is structurally identical to a look-ahead leak via a misplaced `.shift()` in backtesting. Contemporaneous OFI answers "how did the market move when flow arrived?", whereas an executable trading strategy requires "where will the mid-price move after I observe the flow?". Because the price impact of liquidity-demanding orders is absorbed immediately at the touch, the residual information diffusing into the next interval is negligible ($R^2 < 0.05$).
- **Dynamic Flow vs. Static Queue State:** OFI differences consecutive top-of-book states to measure net incoming volume. However, in tick-constrained books where the spread is almost permanently one tick, the relative size of resting queues at the touch ($QI$) summarizes the balance of pending supply and demand far more effectively than incremental flow increments.
- **Latency Asymmetry as a Fraction of Holding Period:** High-frequency alpha signals decay not because latency exists in the abstract, but because latency represents a substantial fraction of the trade holding period. At a 465ms holding period (event-50), 100ms of delay consumes >20% of the trade duration, extinguishing 84% of the signal's predictive IC.
- **Taker vs. Maker Asymmetry:** The economic viability of OFI resides exclusively in passive liquidity provision (market making), where the participant *earns* the spread to absorb flow and uses OFI to shade quotes against adverse selection, rather than active liquidity taking, where crossing the spread imposes an insurmountable arithmetic penalty.

## Signal

### Analytical Formulation of Order Flow Imbalance (OFI)

#### Increment Definition
For each book update $n$, let $(P^b_n, q^b_n)$ denote the best bid price and size, and $(P^a_n, q^a_n)$ denote the best ask price and size `[source-reported]`:

$$e_n = \mathbb{I}_{\{P^b_n \ge P^b_{n-1}\}} \cdot q^b_n - \mathbb{I}_{\{P^b_n \le P^b_{n-1}\}} \cdot q^b_{n-1} - \mathbb{I}_{\{P^a_n \le P^a_{n-1}\}} \cdot q^a_n + \mathbb{I}_{\{P^a_n \ge P^a_{n-1}\}} \cdot q^a_{n-1}$$

Component logic `[source-reported]`:
- **Bid Price Improves ($P^b_n > P^b_{n-1}$):** Only $+q^b_n$ fires (fresh aggressive bid demand enters the touch; old size was outbid, not canceled).
- **Bid Price Falls ($P^b_n < P^b_{n-1}$):** Only $-q^b_{n-1}$ fires (demand that was resting at the touch is fully consumed or canceled).
- **Bid Price Unchanged ($P^b_n = P^b_{n-1}$):** Both indicators fire, differencing to $q^b_n - q^b_{n-1}$ (net size change).
- **Ask Side:** Mirrors the bid side with inverted signs (size on the ask represents selling supply).
- **Initialization & Boundaries:** The first book update primes the state and contributes zero flow ($e_1 = 0$). At interval boundaries, accumulator reset preserves the reference state to avoid discarding boundary updates `[source-reported]`.

#### Interval Aggregation
The interval signal aggregates individual increments over interval $k$ `[source-reported]`:

$$OFI_k = \sum_{n \in \mathcal{I}_k} e_n$$

Two sampling paradigms are evaluated `[source-reported]`:
1. **Clock-Time Sampling:** Intervals of fixed physical duration: 100ms, 500ms, 1s, 5s, 10s, 30s, 60s.
2. **Event-Time Sampling:** Intervals of fixed book update counts: 50, 200, 1000 updates.

### Baseline Benchmark: Queue Imbalance (QI)

Top-of-book static imbalance evaluated at interval boundaries `[source-reported]`:

$$QI_k = \frac{q^b_k - q^a_k}{q^b_k + q^a_k} \in [-1, 1]$$

Depth-weighted imbalance across 5 levels `[source-reported]`:

$$DI_k = \frac{\sum_{i=1}^5 q^b_{i,k} - \sum_{i=1}^5 q^a_{i,k}}{\sum_{i=1}^5 q^b_{i,k} + \sum_{i=1}^5 q^a_{i,k}}$$

### Directional Taker Strategy (Falsified Target Strategy)

#### Formation Timestamp
- Signal evaluated at the close of interval $k$ ($t_{close,k}$) `[source-reported]`.

#### Entry Trigger
- Long when $OFI_k > 0$ (or $QI_k > 0$ for the baseline) `[source-reported]`.
- Short when $OFI_k < 0$ (or $QI_k < 0$ for the baseline) `[source-reported]`.

#### Execution Timing & Fill Model
- Executed via aggressive market orders taking liquidity at prevailing touch prices ($P^a$ for long, $P^b$ for short) `[source-reported]`.
- Signal-to-order execution delay modeled across five latency points: $0\,\mu\text{s}$, $100\,\mu\text{s}$, $1\,\text{ms}$, $10\,\text{ms}$, $100\,\text{ms}$ `[source-reported]`.

#### Exit & Holding Period
- Position closed via market order after holding period equal to the interval duration (median duration for event-time sampling) `[source-reported]`.

## Required data

- **Instruments:** US equity common stocks (INTC and GOOG) `[source-reported]`.
- **Venue:** NASDAQ (single-venue reconstructed limit order book from LOBSTER data) `[source-reported]`.
- **Market Type:** Centralized cash equities `[source-reported]`.
- **Timeframe:** Full trading session (09:30:00 to 16:00:00 EST, 2012-06-21) `[source-reported]`.
- **Data Granularity & Schema:**
  - Message feed: Timestamp (integer nanoseconds since midnight), event type (1=New, 2=Partial Cancel, 3=Delete, 4=Visible Execution, 5=Hidden Execution, 6=Cross, 7=Halt), unique Order ID, size (shares), price (dollars $\times 10,000$, integer ticks), direction ($+1$ for Buy, $-1$ for Sell) `[source-reported]`.
  - Ground truth reference: LOBSTER 10-level order book snapshots $(P^a_i, q^a_i, P^b_i, q^b_i)_{i=1}^{10}$ at every event `[source-reported]`.
- **Cleaning & Message Handling Conventions:**
  - Pre-open resting orders: Window starts at 09:30:00 with pre-existing orders; book seeded from row 0 of oracle `[source-reported]`.
  - Type 4 direction convention: Direction indicates the side of the *resting limit order*, not the incoming aggressor (a Type 4 with direction $= 1$ represents an aggressive sell consuming a resting buy) `[source-reported]`.
  - Type 5 hidden executions: Trades execute without modifying the visible limit order book `[source-reported]`.
  - Types 6 (cross/auction) and 7 (halts): Explicitly filtered from touch calculations `[source-reported]`.
  - Timestamps: Converted to integer nanoseconds using pure integer scaling; floating-point conversions (`double`) strictly prohibited to avoid precision truncation and timestamp inversion `[source-reported]`.

## Execution assumptions

- **Order Type:** Aggressive market orders crossing the touch (demanding liquidity) `[source-reported]`.
- **Transaction Costs:**
  - Half-spread cost paid on both entry and exit: $\approx 0.51$ ticks on INTC; $\approx 14.0$ ticks on GOOG `[source-reported]`.
  - Exchange taker fees: Omitted from baseline calculations; in 2012, NASDAQ taker fee was $\approx \$0.0030$ per share, which further worsens the cost hurdle `[source-reported]`.
- **Fill Assumption:** Immediate 100% fill at the touch upon order arrival (no partial fills or queue delays modeled) `[source-reported]`.
- **Latency Specification:** Evaluated at $0\,\mu\text{s}$, $100\,\mu\text{s}$, $1\,\text{ms}$, $10\,\text{ms}$, $100\,\text{ms}$ timestamp delays relative to signal generation timestamp `[source-reported]`.
- **Capacity & Sizing:** Assumed zero market impact of the strategy itself (infinitesimal taker sizing) `[source-reported]`.

## Evidence

### Source-reported

All quantitative figures trace directly to Tejas Mungale's repository (`Tejas356/limit_order_book_engine`, commit `a2270d70256f292b7d5d11df30a61fd1d6374ba9`, `README.md`, `SPEC.md`, `NOTES.md`):

#### 1. Contemporaneous Price Impact Regression ($\Delta P_k = \alpha + \beta \cdot OFI_k + \epsilon_k$)
Evaluates price change over interval $k$ against OFI over interval $k$ (price in ticks, $\beta$ in ticks per 1,000 shares):

| Ticker | Sampling Scheme | Sample Size ($n$) | $\beta$ / 1k shares | $t$-statistic | $R^2$ |
|---|---|---:|---:|---:|---:|
| **INTC** | Clock 100ms | 77,206 | 0.0191 | 290.5 | **0.5222** |
| INTC | Clock 500ms | 36,126 | 0.0193 | 202.5 | 0.5320 |
| INTC | Clock 1s | 21,527 | 0.0191 | 161.9 | 0.5492 |
| INTC | Clock 5s | 4,680 | 0.0186 | 84.1 | 0.6020 |
| INTC | Clock 10s | 2,340 | 0.0190 | 65.1 | **0.6444** |
| INTC | Clock 30s | 780 | 0.0195 | 40.9 | **0.6830** |
| INTC | Clock 60s | 390 | 0.0199 | 28.8 | **0.6808** |
| INTC | Event 50 | 12,481 | 0.0157 | 70.3 | 0.2834 |
| INTC | Event 200 | 3,121 | 0.0186 | 57.2 | 0.5124 |
| INTC | Event 1000 | 625 | 0.0188 | 33.6 | 0.6438 |
| **GOOG** | Clock 100ms | 36,669 | 9.27 | 77.5 | 0.1407 |
| GOOG | Clock 1s | 16,110 | 8.82 | 58.7 | 0.1760 |
| GOOG | Clock 10s | 2,336 | 5.64 | 21.2 | 0.1614 |
| GOOG | Clock 60s | 390 | 3.79 | 6.7 | 0.1040 |
| GOOG | Event 50 | 2,959 | — | — | 0.2490 |
| GOOG | Event 200 | 740 | 9.58 | 18.4 | 0.3150 |

- *Verification of Structural Scaling with Depth (INTC):* When intervals are bucketed into depth quintiles (mean depth rising from 39,978 shares in Q1 to 117,807 shares in Q5), $\beta$ drops monotonically by a factor of 3.7 (from $0.0437$ to $0.0118$ per 1k shares, all $t > 25$), exactly verifying Cont-Kukanov-Stoikov's structural law of liquidity scaling.

#### 2. The Contemporaneous vs. Predictive Collapse
Contrasts contemporaneous impact ($R^2_{contemp}$) with predictive regression ($\Delta P_{k+1} = \alpha + \beta \cdot OFI_k + \epsilon_k$, $R^2_{pred}$):

| Horizon / Scheme | Contemp $R^2$ | Predictive $R^2$ | Collapse Ratio |
|---|---:|---:|---:|
| **INTC 100ms** | 0.5222 | 0.00127 | **411x** |
| **INTC 1s** | 0.5492 | 0.00197 | **278x** |
| **INTC 10s** | 0.6444 | 0.00447 | **144x** |
| **INTC 60s** | 0.6808 | 0.00023 | **2,898x** |
| **INTC 50 ev** | 0.2834 | 0.02252 | **13x** |
| **INTC 200 ev** | 0.5124 | 0.04931 | **10x** |
| **INTC 1000 ev** | 0.6438 | 0.02016 | **32x** |
| **GOOG 100ms** | 0.1407 | 0.00210 | **67x** |
| **GOOG 1s** | 0.1760 | 0.00162 | **109x** |
| **GOOG 10s** | 0.1614 | 0.00065 | **248x** |
| **GOOG 50 ev** | 0.2490 | 0.02341 | **11x** |
| **GOOG 200 ev** | 0.3150 | 0.00688 | **46x** |

#### 3. Baseline Dominance: Queue Imbalance vs. OFI on INTC
Predictive Information Coefficient (Spearman rank correlation) against forward return:

| Horizon | IC(OFI) | IC(Queue Imbalance) | IC(Depth Imbalance 5L) | Superior Signal |
|---|---:|---:|---:|---|
| **100ms** | 0.0456 | **0.1094** | 0.0644 | Queue Imbalance (2.4x) |
| **1s** | 0.0829 | **0.1687** | 0.1045 | Queue Imbalance (2.0x) |
| **5s** | 0.1458 | **0.2536** | 0.1698 | Queue Imbalance (1.7x) |
| **10s** | 0.1365 | **0.2540** | 0.1794 | Queue Imbalance (1.9x) |
| **50 ev** | 0.2025 | **0.3744** | 0.2261 | Queue Imbalance (1.8x) |
| **200 ev** | 0.3038 | **0.4482** | 0.3028 | Queue Imbalance (1.5x) |

*Null standard error ($1/\sqrt{n-3}$):* $0.0036$ at 100ms, $0.018$ at event-200; the gap separating Queue Imbalance from OFI is statistically decisive (many standard deviations).

#### 4. Latency Decay Curve (INTC Predictive IC vs Artificial Delay)

| Horizon | Median Hold | $0\,\mu\text{s}$ | $100\,\mu\text{s}$ | $1\,\text{ms}$ | $10\,\text{ms}$ | $100\,\text{ms}$ | Retained at 100ms |
|---|---:|---:|---:|---:|---:|---:|---:|
| **100ms** | 100ms | 0.0685 | 0.0685 | 0.0687 | 0.0620 | 0.0254 | **37%** |
| **500ms** | 500ms | 0.0550 | 0.0550 | 0.0552 | 0.0524 | 0.0517 | 94% |
| **1s** | 1.0s | 0.0859 | 0.0859 | 0.0854 | 0.0814 | 0.0744 | 87% |
| **10s** | 10.0s | 0.1376 | 0.1376 | 0.1376 | 0.1383 | 0.1337 | 97% |
| **60s** | 60.0s | 0.0153 | 0.0153 | 0.0153 | 0.0153 | 0.0147 | 96% |
| **50 ev** | 465ms | 0.2701 | 0.2637 | 0.2289 | 0.0878 | 0.0420 | **16%** |
| **200 ev** | 3.8s | 0.3013 | 0.2901 | 0.2455 | 0.1450 | 0.1019 | **34%** |
| **1000 ev** | 31.6s | 0.1416 | 0.1435 | 0.1412 | 0.1312 | 0.1143 | 81% |

#### 5. Cost Reality Check (Expected Edge vs. Half-Spread)
Expected gain per trade $\approx IC \times \sigma(\Delta P)$ ticks versus half-spread:

| Ticker & Horizon | Predictive IC | $\sigma(\Delta P)$ (ticks) | Expected Edge (ticks) | Half-Spread (ticks) | **Edge / Cost Ratio** |
|---|---:|---:|---:|---:|---:|
| **INTC 100ms** | 0.0456 | 0.125 | 0.0057 | 0.510 | **0.011** |
| **INTC 1s** | 0.0829 | 0.237 | 0.0196 | 0.507 | **0.039** |
| **INTC 10s** | 0.1365 | 0.688 | 0.0938 | 0.507 | **0.185** |
| **INTC 30s** | 0.1202 | 1.251 | 0.1503 | 0.506 | **0.297** |
| **INTC 50 ev** | 0.2025 | 0.262 | 0.0531 | 0.617 | **0.086** |
| **INTC 200 ev** | 0.3038 | 0.554 | 0.1684 | 0.619 | **0.272** |
| **INTC 1000 ev** | 0.1462 | 1.328 | 0.1941 | 0.626 | **0.310** |
| **GOOG 1s** | 0.0504 | — | 0.2510 | 13.83 | **0.018** |
| **GOOG 30s** | 0.0855 | — | 1.6910 | 13.48 | **0.125** |
| **GOOG 50 ev** | 0.1876 | — | 1.8092 | 14.86 | **0.122** |
| **GOOG 1000 ev** | -0.0735 | — | 3.3005 | 14.53 | **0.227** |

*Decisive Empirical Verdict:* Across all 20 cells in the experimental grid, the maximum edge-to-cost ratio is **0.310**. Not a single horizon comes within a factor of three of paying the half-spread alone `[source-reported]`.

### Independently reproduced

`Not independently reproduced.` All statistical results, regression coefficients, IC decays, and cost checks represent primary empirical research published by Tejas Mungale in GitHub repository `Tejas356/limit_order_book_engine` (commit `a2270d70256f292b7d5d11df30a61fd1d6374ba9`). No internal reproduction on our own execution stack has been conducted.

### Negative evidence

- **Decisive Falsification of Standalone OFI Taker Alpha:** Predictive $R^2$ is between 10x and 2,898x weaker than contemporaneous impact. In no case does predictive power exceed 0.049.
- **Microstructure Spread Inversion:** The half-spread exceeds expected directional profit by at least 3.2x (and up to 90x at sub-second horizons). Factoring in exchange taker fees ($\approx \$0.0030$/share) and adverse selection widens the loss further.
- **Queue Imbalance Dominance:** The static top-of-book queue ratio $QI$ delivers 1.5x to 2.5x higher predictive IC than the dynamic four-term OFI accumulator on liquid instruments.
- **Latency Vulnerability:** The fastest horizons where OFI exhibits nominal IC ($IC \approx 0.30$ at event-200) decay by 66% to 84% under 100ms latency, proving that the signal decays fastest exactly where it is nominally largest.
- **Cross-Sectional Thin-Book Noise:** On wide, low-volume assets (GOOG), OFI predictive regressions exhibit severe instability and noise across long horizons ($IC = -0.0735$ at event-1000).

## Falsification plan

To further test whether the rejection of OFI taker alpha holds under modern market microstructure or can be rescued under alternative formulations, the following empirical tests are proposed:

1. **Multi-Day Out-of-Sample Modern Microstructure Audit (research-proposed):**
   - *Test:* Reconstruct the full Level-3 order book on SPY, QQQ, and NVDA using modern OPRA/NASDAQ ITCH data across 60 consecutive trading sessions `[research-proposed]`.
   - *Decision Rule:* If the maximum edge-to-cost ratio $\frac{IC \times \sigma(\Delta P)}{half\_spread}$ across all clock and event horizons remains $< 0.50$ net of exchange taker fees, the rejection of OFI as a directional taker alpha is confirmed across modern electronic equity markets `[research-defined falsification threshold]`.
2. **Passive Quoting Adverse Selection Offset Test (research-proposed):**
   - *Test:* Implement a simulated market maker that quotes passively at the touch, shifting quote mid-points by $\gamma \cdot OFI_k$ and tracking fill rates via a calibrated queue position model `[research-proposed]`.
   - *Decision Rule:* If incorporating $OFI_k$ reduces adverse selection markout losses by $\ge 15\%$ without reducing filled spread capture by $> 10\%$, confirm that OFI functions exclusively as a defensive quoting signal rather than an offensive taker alpha `[research-defined falsification threshold]`.
3. **Non-Linear Multi-Level OFI Interaction Test (research-proposed):**
   - *Test:* Evaluate whether a vector OFI across 5 depth levels combined with queue imbalance non-linearly via Gradient Boosted Trees (LightGBM) can improve predictive $R^2$ beyond $0.15$ `[research-proposed]`.
   - *Decision Rule:* If non-linear multi-level combinations fail to achieve out-of-sample predictive $R^2 \ge 0.10$ and net positive Sharpe after crossing spread, confirm that depth expansion does not overturn taker unviability `[research-defined falsification threshold]`.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`
- **Research Interpretation:** The findings originate from US equities (NASDAQ 2012 LOBSTER data) and represent a ported hypothesis that must not be treated as empirical crypto evidence without explicit verification on cryptocurrency order books.
- **Cryptocurrency Derivative (Perpetual Futures) Considerations:**
  - *Continuous Trading & Fee Structure:* Crypto perpetual markets (e.g., Binance, Bybit) feature maker rebates (or low maker fees, e.g., 0.01%–0.02%) vs higher taker fees (0.04%–0.05%). Because the taker fee in crypto perpetuals is frequently 2 to 5 times larger than the bid-ask half-spread on liquid pairs (BTCUSDT, ETHUSDT), directional taker strategies face an even more severe cost hurdle than in US equities.
  - *Level-2 vs Level-3 Book Reconstruction:* Crypto exchanges generally publish aggregated Level-2 order book diffs (e.g., Binance `@depth@100ms`) rather than individual message-by-message order additions and cancellations (Level-3 ITCH). The CKS analytical formulation must be approximated from periodic depth snapshots, introducing aggregation blur and synthetic discretization error.
  - *Funding Rate and Basis Feedback:* Crypto perpetual order flow is heavily influenced by 8-hour funding payments. In periods of extreme funding dislocations, taker flow becomes one-sided and predatory, altering the balance between inventory risk and adverse selection.
  - *Sub-Second Latency Sensitivity:* Decentralized and centralized crypto matching engines experience substantial API network jitter (cloud REST/WebSocket latencies spanning 20ms to 200ms). As demonstrated in Step 12, an 84% decay in predictive IC occurs within 100ms, making retail or non-colocated crypto trading on OFI unviable.

## Limitations

- **Single-Session Historical Sample:** Evaluated on a single trading day (2012-06-21). While covering 771,956 messages across two tickers, multi-day regime stability across high-volatility macro event days cannot be asserted.
- **Single-Venue Book:** NASDAQ order book only; does not incorporate consolidated National Best Bid and Offer (NBBO) across fragmented execution venues (Direct Edge, BATS, NYSE).
- **Absence of Queue Position Model:** Does not model queue priority or passive execution fill probabilities, precluding direct testing of market-making profitability.
- **Omission of Fee Schedules:** Taker fees and liquidity rebates are excluded from the baseline cost calculation, though their inclusion strictly reinforces the negative conclusion.
- **Single-Path Analysis:** Confidence intervals on Information Coefficients are derived from analytical null standard errors ($1/\sqrt{n-3}$) rather than block bootstrap resampling.

## Implementation status

`not-implemented`. No implementation in our research stack (PyBroker, NautilusTrader, or live execution engines) has been conducted.

## Adoption boundary

This record is research material only. Presence in this repository does not indicate:
- Strategy profitability;
- Validated alpha;
- Approval for implementation;
- Approval for paper trading, testnet, or live trading.

## Related Wiki records

- `[[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]]` — Evaluates multi-level OFI trade-arrival intensity via Hawkes self-exciting processes; complements this record's focus on price impact decoupling.
- `[[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]]` — Parallel empirical falsification of parametric surface residual alpha and characterization of market-maker adverse selection boundaries.
- `[[quant/crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]` — Precedent for rigorous empirical falsification of popular quantitative trading heuristics after real-world execution frictions.
- `[[quant/clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03.md]]` — Evaluates unsupervised clustering of order flow imbalance states across depth levels.
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md]]` — Microstructure falsification of cumulative volume delta and retail order flow signals on crypto perpetuals.

## Sources

1. **Primary Codebase & Empirical Research:** Tejas Mungale (`Tejas356`). *limit_order_book_engine: Limit order book reconstruction in C++ validated message-by-message against an independent oracle, with an order flow imbalance study that separates price impact from prediction*, GitHub repository `Tejas356/limit_order_book_engine`, commit `a2270d70256f292b7d5d11df30a61fd1d6374ba9`, dated 2026-09-07 17:30:42 +0100. URL: [https://github.com/Tejas356/limit_order_book_engine](https://github.com/Tejas356/limit_order_book_engine).
2. **Primary Literature Reference:** Rama Cont, Arseniy Kukanov, and Sasha Stoikov (2014), *The Price Impact of Order Book Events*, Journal of Financial Econometrics, 12(1): 47–88. DOI: [10.1093/jjfinec/nbt003](https://doi.org/10.1093/jjfinec/nbt003).
3. **Data Source & Oracle:** LOBSTER (Limit Order Book Reconstruction System), NASDAQ Level-10 sample datasets for INTC and GOOG (2012-06-21). Reference: Rainer Huang and Tomasz Polak (2011), *LOBSTER: Limit Order Book Reconstruction System*, SSRN Electronic Journal. DOI: [10.2139/ssrn.1977201](https://doi.org/10.2139/ssrn.1977201).
4. **Microprice Formulation Reference:** Sasha Stoikov (2018), *The Micro-Price: A High Frequency Estimator of Future Prices*, Quantitative Finance, 18(12): 1959–1966. DOI: [10.1080/14697688.2018.1489139](https://doi.org/10.1080/14697688.2018.1489139).
