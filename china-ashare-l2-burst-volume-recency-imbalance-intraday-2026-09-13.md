---
schema: strategy-research-record-v1
title: "China A-Share Level-2 Burst Volume Imbalance, Order Recency, and Aggressive Trade Imbalance: Microsecond-Grid Clustering and Short-Horizon Order-Flow Momentum"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - china-ashare
  - market-microstructure
  - level-2
  - order-flow
  - burst-volume
  - aggressive-trade-imbalance
  - order-recency
  - csi500
  - intraday-alpha
  - execution-timing
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "Xuhui Liu, 'intraday_alpha_1m: A minimal, end-to-end high-frequency alpha research pipeline on China A-share Level-2 (order-book tick) data', GitHub repository, commit 2625a7ea2a15e5e32145b9488256b3bf28e3e7f0, September 13, 2026. https://github.com/liu-xuhui/intraday_alpha_1m"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# China A-Share Level-2 Burst Volume Imbalance, Order Recency, and Aggressive Trade Imbalance: Microsecond-Grid Clustering and Short-Horizon Order-Flow Momentum

## Provenance

- **Author:** Xuhui Liu (GitHub: `liu-xuhui`)
- **Repository:** https://github.com/liu-xuhui/intraday_alpha_1m
- **Full Commit SHA:** `2625a7ea2a15e5e32145b9488256b3bf28e3e7f0`
- **Commit Date:** 2026-09-13T06:01:02Z (`source-reported`)
- **Primary Source Files Inspected:**
  - `README.md` (33,722 bytes: detailed pipeline architecture, timing proofs, empirical tables, and microstructure analysis)
  - `src/build_burst_volume_factors.py` (Implementation of 10 ms order burst detection and trailing window imbalance)
  - `src/build_ati_factors.py` (Implementation of trade-level aggressive buy/sell volume and count imbalance)
  - `src/build_order_recency_factors.py` (Implementation of order arrival recency/age imbalance)
  - `src/build_targets.py` (Canonical forward 1-minute mid-price return target construction with as-of-next quote alignment)
  - `src/eval_ic.py` & `src/plot_ic.py` (Cross-sectional Pearson IC, Spearman Rank IC, ICIR, and t-statistic evaluation)
  - `src/validate_orderid_assumption.py` (Empirical proof of Shenzhen order ID reset/unreliability, justifying timestamp-based clustering)
  - `results/ic_summary.txt` (Authoritative tabulated cross-sectional metrics across 11 factor specifications)
  - `data/csi500_wind_codes_20260820.txt` (Fixed 500-constituent universe specification)
  - `data/data_reference.txt` (Exchange-specific schema guide for SSE and SZSE Level-2 parquet streams)
  - `data/download_summary_20260820_20260828.txt` (Audit log of 132M rows across 21 parquet partitions)
- **Primary Data Source:** Hugging Face dataset `venvoo/china-a-share-l2-level2-limit-order-book-tick-data`, pinned revision `0121dd0a60756d74efb23bf19a2876af3565ee3b` (`source-reported`).
- **License & Hygiene:** Repository code is published under the MIT License (`source-reported`). Underlying Hugging Face data archive is restricted to `research-use-only` (`source-reported`). The repository commits only code, configuration, schema references, and aggregated statistical summaries; no raw order book rows, proprietary account identifiers, credentials, or client secrets are committed (`source-reported`).
- **Deduplication Check:** Grep search across the entire `alpha-strategy-research` repository confirmed zero existing records citing repository `liu-xuhui/intraday_alpha_1m` or commit `2625a7ea2a15e5e32145b9488256b3bf28e3e7f0`. Adjacent record `china-ashare-l3-eaten-order-age-imbalance-execution-timing-falsification-2026-09-13.md` (BreevoZ / Zhou, commit `ca2e72fa`) analyzes SZSE Level-3 matching engine sequence number arithmetic (`ApplSeqNum % 10^12`) and passive quote consumption age (`eat_age_imb`). The current record investigates Level-2 order book streams, top-of-book quotes, 10 ms grid clustering (`burst_volume_imbalance`), arrival recency, and trade aggression across a fixed 500-stock cross-section with 1-minute forward horizons.

## Economic mechanism

### Source-reported

1. **Information Content of the Order Process:**
   Limit order book tick data exposes the underlying process generating prices: individual order submissions, cancellations, and aggressive executions with exchange-stamped sequencing. At short horizons (seconds to minutes), this order flow carries transient private information and liquidity demand that has not yet been fully absorbed into prevailing quote prices.
2. **Aggressive Spread-Crossing as Directed Pressure (ATI):**
   When market participants submit aggressive orders that cross the prevailing bid-ask spread (`bs_flag` in trades), they pay the spread cost to obtain immediate execution. A sustained predominance of aggressive buy executions over aggressive sell executions over trailing windows ($W \in [30\text{s}, 90\text{s}]$) reflects urgent directional liquidity demand, exerting positive upward pressure on subsequent mid-prices.
3. **Microsecond-Grid Algorithmic Clustering (Burst Volume):**
   Exchange feeds enforce a 10 ms timestamp quantization grid (`time % 10 == 0`). When institutional participants slice large parent orders via execution algorithms (TWAP/VWAP/POV engines) or when multiple high-frequency trading (HFT) algorithms react simultaneously to an identical market event, child orders land on the exact same stock, side, and 10 ms timestamp slot. While isolated single orders represent retail noise or uncoordinated flow, simultaneous multi-order bursts ($\ge 2$ orders per 10 ms slot) represent machine-driven institutional intent. Measuring the volume imbalance restricted strictly to these burst clusters filters out background noise.
4. **Order Arrival Recency as Freshness of Intent:**
   The elapsed time since the most recent order submission on the bid versus the ask side measures the relative freshness of directional conviction. A recent buy submission coupled with an absent or stale sell submission indicates that active market participants are revising quotes upward or replenishing the bid side.

### Research interpretation

The core economic hypothesis is that sub-minute order flow imbalances exhibit short-horizon directional persistence (order flow momentum) over a 1-minute forward horizon. However, evaluating this mechanism against institutional market reality yields critical constraints:
1. **The Fast Half-Life of Order-Flow Information:**
   Empirical predictability decays steeply as lookback extends beyond 8–30 seconds. Order flow imbalance reflects temporary order book depletion and immediate queue replenishment. As the lookback window expands to 60s or 90s, stale flow dilutes the signal, collapsing cross-sectional IC toward zero.
2. **Structural Execution Infeasibility as a Standalone Cash Strategy:**
   In China A-shares, statutory rules impose a strict T+1 settlement constraint (long equity positions purchased at time $t$ cannot be sold until $t+1$), making standalone intraday directional round-trip trading illegal without pre-existing inventory. Furthermore, transaction frictions (stamp duty of 5 bps on sales, exchange/clearing fees of ~1.1 bps, broker commissions of ~1.5 bps, plus bid-ask spread crossing of 5–15 bps on CSI 500 midcaps) total 15–25 bps roundtrip. A 1-minute forward IC of +0.0156 yields an expected gross edge of only 1–3 bps, ensuring that any attempt to trade this signal as a high-turnover directional cash strategy will be submerged by transaction costs.
3. **Economic Utility Restricted to Sunk-Cost Execution Timing:**
   Because the predictive edge is positive and genuine at short horizons (+0.0156 IC), its valid institutional application is not alpha capture, but execution cost reduction. A broker or quantitative fund executing an existing multi-hour parent order (e.g., VWAP/TWAP) can tilt child-order pacing according to the burst volume or ATI signal, speeding up execution when favorable imbalance appears and pausing when adverse imbalance is detected, capturing basis points of price improvement without incurring incremental turnover.

## Signal

### Signal Construction & Formulas

All factors are evaluated on a cross-sectional universe of $N = 500$ stocks across 1-minute prediction boundaries $t$ (`source-reported`).

#### 1. Aggressive Trade Imbalance (ATI)
- **Source Stream:** `trades.parquet` (`逐笔成交.parquet`), filtering for aggressive execution records where `bs_flag in ('B', 'S')` (`source-reported`).
- **Lookback Window:** Strict half-open trailing window $\tau \in [t - W, t)$, with $W \in \{30, 60, 90\}$ seconds (`source-reported`).
- **Count Imbalance (`ati_count`):**
  $$ATI_{\text{count}, i, t, W} = \frac{N^B_{i, t, W} - N^S_{i, t, W}}{N^B_{i, t, W} + N^S_{i, t, W}}$$
  where $N^B$ and $N^S$ are the count of aggressive buy and sell trades in $[t-W, t)$. If $N^B + N^S = 0$, the factor is set to `NaN` (`source-reported`).
- **Volume Imbalance (`ati_volume`):**
  $$ATI_{\text{volume}, i, t, W} = \frac{V^B_{i, t, W} - V^S_{i, t, W}}{V^B_{i, t, W} + V^S_{i, t, W}}$$
  where $V^B$ and $V^S$ are total executed shares across aggressive buy and sell trades in $[t-W, t)$. If $V^B + V^S = 0$, the factor is set to `NaN` (`source-reported`).

#### 2. Burst Volume Imbalance
- **Source Stream:** `orders.parquet` (`逐笔委托.parquet`), filtering out cancellations (`order_type != 'D'`) and retaining submissions with `order_code in ('B', 'S')` (`source-reported`).
- **Burst Detection Rule:** Group orders by `(wind_code, order_code, exact timestamp)`. A cluster is classified as a burst if the order count within the exact 10 ms timestamp satisfies $N^s_{i, \tau} \ge 2$ (`MIN_BURST_ORDERS = 2`) (`source-reported`).
- **Lookback Window:** Trailing window $\tau \in [t - W, t)$, with $W \in \{8, 15, 30\}$ seconds (`source-reported`).
- **Burst Volume Summation:**
  $$BV^B_{i, t, W} = \sum_{\tau \in [t-W, t)} \mathbb{1}\{N^B_{i, \tau} \ge 2\} \sum_{j \in \text{Cluster}(i, B, \tau)} \text{Volume}_j$$
  $$BV^S_{i, t, W} = \sum_{\tau \in [t-W, t)} \mathbb{1}\{N^S_{i, \tau} \ge 2\} \sum_{j \in \text{Cluster}(i, S, \tau)} \text{Volume}_j$$
- **Burst Volume Imbalance:**
  $$\text{BurstVolumeImbalance}_{i, t, W} = \frac{BV^B_{i, t, W} - BV^S_{i, t, W}}{BV^B_{i, t, W} + BV^S_{i, t, W}}$$
  If $BV^B + BV^S = 0$, the factor is set to `NaN` (`source-reported`).

#### 3. Order Recency Imbalance
- **Source Stream:** `orders.parquet` (`order_type != 'D'`, `order_code in ('B', 'S')`) (`source-reported`).
- **Lookback Window:** $W \in \{15, 30\}$ seconds (`source-reported`).
- **Side Age Definition:**
  $$Age^B_{i, t, W} = \begin{cases} t - \max\{\tau \in [t-W, t) : \text{buy submission}\} & \text{if any buy exists in } [t-W, t) \\ W & \text{otherwise} \end{cases}$$
  $$Age^S_{i, t, W} = \begin{cases} t - \max\{\tau \in [t-W, t) : \text{sell submission}\} & \text{if any sell exists in } [t-W, t) \\ W & \text{otherwise} \end{cases}$$
- **Recency Imbalance:**
  $$\text{RecencyImbalance}_{i, t, W} = \frac{Age^S_{i, t, W} - Age^B_{i, t, W}}{Age^S_{i, t, W} + Age^B_{i, t, W}}$$
  If both sides are silent, $Age^B = Age^S = W$, yielding exactly $0.0$ (`source-reported`).

### Timing & Information-Leakage Boundary

- **Factor Information Set:** Strictly pre-$t$: $\tau \in [t - W, t)$. Any event stamped exactly at $t$ is strictly excluded (`event_time < t`) (`source-reported`).
- **Target Information Set:** Starts at the earliest valid quote with timestamp $\tau^\star \ge t$ (`source-reported`).
- **Lookahead Insulation:** The factor lookback interval $[t-W, t)$ and the forward return interval $[\tau^\star, \tau^\star + 1\text{m}]$ are disjoint by construction (`source-reported`).
- **Incomplete History Truncation:** At the session open (09:30:00), trailing history does not exist; any prediction timestamp $t$ where $t - W < \text{09:30:00}$ is assigned `NaN` across all stocks (`source-reported`).

### Strategy Operational Rules

- **Execution Universe:** Fixed CSI 500 index constituents (500 stocks) (`source-reported`).
- **Prediction Grid:** 1-minute fixed timestamps from 09:30:00 to 09:58:00 within the 09:30–10:00 opening half-hour window (29 timestamps per day, 203 total timestamps over 7 days) (`source-reported`).
- **Forward Horizon:** 1 minute ($h = 1\text{m}$) (`source-reported`).
- **Execution Fill Model:** Primary source evaluates signal predictive power via mid-price forward returns without modeling fills; for institutional execution overlay, passive quote participation at prevailing bid/ask is `research-proposed`.
- **Trading Thresholds / Cutoffs:** Not specified by primary source (evaluated linearly via correlation); long top quintile ($Q5$) / short bottom quintile ($Q1$) cross-sectional allocation is `research-proposed`.
- **Rebalancing Cadence:** 1 minute (`source-reported`).

## Required data

- **Universe:** 500 fixed CSI 500 constituent stocks as of 2026-08-20 (280 Shanghai `.SH` and 220 Shenzhen `.SZ` tickers) (`source-reported`).
- **Time Window:** 09:30:00.000 to 10:00:00.000 Asia/Shanghai (morning continuous auction opening half-hour) across 7 trading days: 2026-08-20 to 2026-08-28 (`source-reported`).
- **Market Data Streams:**
  1. **Quotes (`行情.parquet`):** 10-level order book snapshots every ~3 seconds (median gap 3,000 ms). Required fields: `wind_code`, `date`, `time`, `bid_px1`, `ask_px1`. Scaled prices ($price = \text{raw} / 10000$) (`source-reported`).
  2. **Orders (`逐笔委托.parquet`):** Tick-by-tick order submissions. Required fields: `wind_code`, `date`, `time`, `order_code` (`B`/`S`), `order_type`, `volume` (`source-reported`).
  3. **Trades (`逐笔成交.parquet`):** Tick-by-tick trade executions. Required fields: `wind_code`, `date`, `time`, `bs_flag` (`B`/`S` aggressor side), `volume`, `trade_code` (`source-reported`).
- **Timestamp Precision & Alignment:** Raw time field is an integer `HHMMSSmmm` (e.g. `93000000` for 09:30:00.000, padded to 9 digits). Timestamp resolution is exactly 10 ms (`time % 10 == 0`). No millisecond rounding is permitted (`source-reported`).
- **Exchange Asymmetry Handling:**
  - **Shanghai (SH):** New orders have `order_type == 'A'`; cancellations appear in the order stream with `order_type == 'D'`. Cancellations are explicitly filtered out (`order_type != 'D'`) (`source-reported`).
  - **Shenzhen (SZ):** New orders have `order_type in ('0', '1', '2', 'U')`; cancellations appear in the **trade** stream with `trade_code == 'C'`. Cancellations in the trade stream are filtered out via `bs_flag in ('B', 'S')` (`source-reported`).
- **Missing Data & Filtering:**
  - Stocks missing from a day's stream (e.g. suspended stock `002155.SZ` on 2026-08-20 to 2026-08-26) produce `NaN` entries (`source-reported`).
  - Stale quote filter: `MAX_QUOTE_DELAY_SECONDS = 5`. If the earliest quote at or after $t$ arrives $>5$ seconds late, mid-price is marked `NaN` (`source-reported`).
  - Zero-activity lookback: if $BV^B + BV^S = 0$ or $V^B + V^S = 0$, factor is set to `NaN` (`source-reported`).

## Execution assumptions

- **Source-Reported Execution Assumptions:**
  - The source explicitly notes that **no trading costs, slippage, fill model, or portfolio construction are modeled**; the analysis is conducted as a pure econometric information-coefficient evaluation on mid-price returns (`source-reported`).
- **Research-Proposed Execution Model (Execution Timing Overlay):**
  - **Order Type:** Passive limit orders posting at the best bid (for parent buy orders) or best ask (for parent sell orders), avoiding taker fee and half-spread crossing (`research-proposed`).
  - **Signal Role:** Alpha overlay modulating the participation rate of a parent TWAP/VWAP execution schedule. When `burst_volume_imbalance_8s > +0.20`, increase buy child order participation by 50%; when `burst_volume_imbalance_8s < -0.20`, pause child order submissions (`research-proposed`).
  - **Frictions:** For standalone trading, stamp duty is 5 bps on sells, broker/clearing fees are 2.6 bps roundtrip, and spread crossing is 5–15 bps, resulting in total roundtrip friction of 15–25 bps (`research-proposed`). Under an execution timing overlay, stamp duty and baseline commissions are sunk costs of the parent order; the marginal cost is only the non-execution / adverse selection cost of uncompleted child orders (`research-proposed`).

## Evidence

### Source-reported

Empirical results across 203 prediction timestamps (7 trading days $\times$ 29 minutes) over the fixed 500-stock CSI 500 universe (`source-reported`, `results/ic_summary.txt`):

| Factor Variant | Lookback ($W$) | $N_{\text{IC}}$ | Mean IC | Std IC | ICIR | Naive $t$-stat | % IC $>0$ | Mean Rank IC | Avg Stocks |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ati_volume_30s` | 30s | 196 | **+0.0156** | 0.0826 | **+0.189** | **+2.65** | 60.2% | +0.0078 | 479.6 |
| `burst_volume_imbalance_8s` | 8s | 196 | **+0.0156** | 0.1264 | +0.123 | +1.73 | 56.1% | **+0.0182** | 366.6 |
| `burst_volume_imbalance_15s` | 15s | 196 | +0.0123 | 0.1234 | +0.100 | +1.40 | 54.6% | +0.0142 | 419.2 |
| `ati_count_30s` | 30s | 196 | +0.0089 | 0.0821 | +0.109 | +1.52 | 59.7% | +0.0003 | 479.6 |
| `order_recency_imbalance_30s` | 30s | 196 | +0.0069 | 0.0761 | +0.090 | +1.26 | 56.6% | +0.0086 | 479.8 |
| `order_recency_imbalance_15s` | 15s | 196 | +0.0068 | 0.0761 | +0.090 | +1.26 | 56.6% | +0.0085 | 479.8 |
| `burst_volume_imbalance_30s` | 30s | 196 | +0.0029 | 0.1072 | +0.028 | +0.39 | 55.1% | +0.0025 | 457.5 |
| `ati_volume_90s` | 90s | 189 | +0.0020 | 0.1068 | +0.019 | +0.26 | 49.2% | -0.0061 | 462.6 |
| `ati_volume_60s` | 60s | 196 | +0.0019 | 0.1013 | +0.018 | +0.26 | 52.0% | -0.0076 | 479.8 |
| `ati_count_90s` | 90s | 189 | +0.0002 | 0.1026 | +0.002 | +0.03 | 51.3% | -0.0090 | 462.6 |
| `ati_count_60s` | 60s | 196 | -0.0003 | 0.1001 | -0.003 | -0.05 | 51.5% | -0.0111 | 479.8 |

Key empirical observations documented by the author (`source-reported`):
1. **Consistency of Directional Sign:** All meaningful factor variants exhibit positive mean IC; buy-side pressure predicts positive forward 1-minute mid-price returns.
2. **Steep Decay with Lookback Window:**
   - For ATI volume: IC drops from +0.0156 at 30s to +0.0019 at 60s and +0.0020 at 90s.
   - For Burst Volume: IC drops from +0.0156 at 8s to +0.0123 at 15s and +0.0029 at 30s.
   - Half-life of order-flow information is on the order of seconds.
3. **Information Orthogonality (ATI vs Burst Volume):**
   - While `ati_volume_30s` achieves higher linear ICIR (+0.189 vs +0.123), its Rank IC is lower (+0.0078 vs +0.0182), indicating its predictability is driven by extreme tail volume imbalances.
   - `burst_volume_imbalance_8s` achieves the highest Rank IC (+0.0182) across the cross-section despite evaluating fewer stocks (366.6 vs 479.6).
   - The mean per-minute cross-sectional rank correlation between `ati_volume_30s` and `burst_volume_imbalance_8s` is only **0.19**, indicating that aggressive spread-crossing and algorithmic arrival clustering capture distinct microstructure dynamics.
4. **Order Recency Stability:** Recency imbalance exhibits the lowest standard deviation (0.0761) and positive IC in 56.6% of minutes, but lower mean IC (+0.0069).

### Independently reproduced

- `not independently reproduced` across the full raw Level-2 parquet dataset (requires ~1 TB download of gated Hugging Face archive `venvoo/china-a-share-l2-level2-limit-order-book-tick-data`).
- Independent code audit conducted on commit `2625a7ea2a15e5e32145b9488256b3bf28e3e7f0`: verified calculation logic, prefix sum algorithms, disjoint interval boundaries, DuckDB queries, and alignment contracts.

### Negative evidence

1. **Failure of Naive Statistical Significance:**
   Only one factor variant (`ati_volume_30s`) achieves a naive $t$-statistic exceeding 2.0 ($t = 2.65$). However, minute-level cross-sectional ICs within the same trading session exhibit strong intraday auto-correlation and cross-sectional dependence. On an effective degrees-of-freedom or Newey-West adjusted basis, none of the factors achieve formal statistical significance ($p < 0.01$) over the 7-day sample.
2. **Signal Disappearance Beyond 30 Seconds:**
   For lookback windows of 60s and 90s, ATI volume IC collapses to +0.0019 ($t = 0.26$) and count IC collapses to -0.0003 ($t = -0.05$). The signal is completely evanescent and cannot support holding periods beyond 1–2 minutes.
3. **Sparsity Penalty of Burst Filtering:**
   Because `burst_volume_imbalance_8s` requires $\ge 2$ orders on the exact same 10 ms timestamp, 26.5% of stock-minute observations have zero bursts on both sides, reducing the effective cross-sectional breadth from 480 to 367 stocks.
4. **Economic Submergence by Frictions:**
   Even at an optimistic IC of +0.016, the expected return of a long-short quintile portfolio is ~2 bps per minute, while roundtrip trading friction in China A-shares exceeds 15 bps. Standalone directional implementation is guaranteed to generate negative net returns.

## Falsification plan

To disconfirm the validity of Level-2 order-flow clustering and aggressive trade imbalance:

1. **Lookahead / Timestamp Leakage Audit:**
   - *Test:* Introduce a deliberate 1-second execution delay between the factor calculation time $t$ and target entry $\tau^\star$ ($[\tau^\star + 1\text{s}, \tau^\star + 61\text{s}]$).
   - *Failure Metric:* If the mean IC drops by $>80\%$ or turns negative under a 1-second delay, the empirical result is falsified as an artifact of exchange latency and quote arrival lookahead.
   - *Decision Rule:* `research-defined falsification threshold`: Mean IC must remain $\ge +0.005$ under a 1-second execution delay.
2. **Placebo / Scrambled Grid Permutation Test:**
   - *Test:* Permute the 10 ms timestamps of order arrivals within each 1-minute interval, destroying the simultaneous clustering ($\ge 2$ orders per slot) while preserving total order volume.
   - *Failure Metric:* If the placebo burst volume imbalance yields an IC comparable to or higher than the true factor, the hypothesis that "10 ms grid clustering identifies institutional algorithmic coordination" is rejected.
   - *Decision Rule:* `research-defined falsification threshold`: True burst volume IC must exceed the 95th percentile of 500 scrambled placebo runs ($p < 0.05$).
3. **Out-of-Sample Window & Regime Generalization:**
   - *Test:* Extend evaluation across the full trading day (10:00–11:30 and 13:00–15:00) and across an out-of-sample period of at least 60 trading days.
   - *Failure Metric:* If afternoon IC drops to zero or turns negative, the effect is falsified as a morning-auction opening liquidity quirk rather than a pervasive microstructure property.
   - *Decision Rule:* `research-defined falsification threshold`: Out-of-sample session-wide mean IC must satisfy $\text{IC} \ge +0.008$ with $\text{ICIR} \ge 0.10$.
4. **Sunk-Cost Child Order Execution Trial:**
   - *Test:* In a simulated or paper parent order execution engine, compare standard TWAP execution against a Signal-Tilted TWAP that conditions child slice timing on `burst_volume_imbalance_8s`.
   - *Failure Metric:* If signal-tilted execution fails to achieve at least 1.0 bp of slippage reduction relative to standard TWAP, the hypothesis of execution utility is rejected.
   - *Decision Rule:* `research-defined falsification threshold`: Net slippage improvement must exceed 1.0 bp with $t$-stat $> 2.0$.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven` (`research interpretation`). The primary source tests China A-share equity Level-2 order books; no crypto market empirical evidence is provided.
- **Microstructure Differences:**
  1. **Clock & Timestamp Discretization:** Traditional equity exchanges (SSE/SZSE) batch feed dispatches onto 10 ms grids, enabling cluster-based burst detection. Centralized crypto exchanges (Binance, OKX, Bybit) provide websocket feeds with millisecond or microsecond trade/order timestamps, but without a uniform 10 ms matching engine clock. Burst detection must be adapted to sliding time bins (e.g. 5–20 ms windows).
  2. **Order Stream Availability:** Most crypto exchanges publish top-of-book (BBO), trade streams, and depth snapshots, but do not provide raw order submission/cancellation streams equivalent to China Level-2 `逐笔委托` unless using private institutional feeds. Therefore, `burst_volume_imbalance` cannot be directly computed on public crypto feeds without full tick-by-tick order placement logging.
  3. **Continuous Trading & Shorting:** Unlike China A-shares (T+1, no intraday shorting for retail, high stamp tax), crypto perpetual markets operate 24/7 with continuous two-way trading, leverage, and low taker fees (1.5–4 bps VIP tier). However, aggressive trade imbalance (CVD / trade imbalance) at sub-minute horizons is heavily traded by HFT market makers, creating intense latency competition.
- **Portability Boundary:** Porting this strategy to crypto requires adapting the burst definition to high-resolution websocket trade flow and funding/spread dynamics, and remains entirely unproven.

## Limitations

- **Short Sample Period:** The empirical study spans only 7 consecutive trading days (2026-08-20 to 2026-08-28) and 203 prediction timestamps (`source-reported`).
- **Restricted Session Window:** Analysis is confined to the opening 30 minutes (09:30–10:00 Asia/Shanghai), which exhibits the highest volatility and retail/institutional participation of the day; results cannot be generalized to midday or afternoon sessions (`source-reported`).
- **No Transaction Costs or Execution Simulation:** The primary study evaluates purely statistical cross-sectional correlations ($IC$) against mid-price returns. No spread costs, taker fees, market impact, or latency delays are modeled (`source-reported`).
- **Absence of Factor Neutralization:** Factors are evaluated in raw form without industry, size, or beta neutralization (`source-reported`). Part of the observed IC may reflect transient sector momentum or market-wide opening beta.
- **Gated Raw Data:** The underlying Hugging Face dataset is access-gated and restricted to academic/research use (`source-reported`).

## Implementation status

- `not-implemented`: No implementation exists in our local research or production stack (`nautilus-quant-system`).
- This record captures external market microstructure research only. No PyBroker, NautilusTrader, Paper, Testnet, or Live code has been authored, scheduled, or approved.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- **Boundary Declaration:** This research record serves as an upstream empirical capture for ChatGPT Research Intake Review and Hermes Wiki Brain ingestion. It does not authorize trading, paper testing, or capital commitment. The signal cannot be traded directionally in cash equities due to T+1 and friction constraints, and its potential utility is strictly confined to future institutional execution algorithm research.

## Related Wiki records

- `china-ashare-l3-eaten-order-age-imbalance-execution-timing-falsification-2026-09-13.md` (SZSE Level-3 matching engine sequence number arithmetic, resting quote age, and execution timing)
- `china-ashare-limit-up-momentum-unfillable-execution-falsification-2026-09-13.md` (Falsification of China A-share limit-up momentum due to unfillable queues)
- `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md` (Self-exciting point process modeling of order flow imbalance)
- `binance-crypto-perpetual-order-flow-sign-entropy-falsification-2026-09-13.md` (High-frequency order flow sign entropy and taker cost walls)

## Sources

- **Primary Source Repository:** Xuhui Liu, `intraday_alpha_1m: A minimal, end-to-end high-frequency alpha research pipeline on China A-share Level-2 (order-book tick) data`, GitHub repository, commit `2625a7ea2a15e5e32145b9488256b3bf28e3e7f0`, pushed September 13, 2026. URL: https://github.com/liu-xuhui/intraday_alpha_1m
- **Primary Data Archive:** `venvoo/china-a-share-l2-level2-limit-order-book-tick-data`, Hugging Face dataset, pinned revision `0121dd0a60756d74efb23bf19a2876af3565ee3b`. URL: https://huggingface.co/datasets/venvoo/china-a-share-l2-level2-limit-order-book-tick-data
- **License:** MIT License, copyright (c) 2026 Xuhui Liu.
