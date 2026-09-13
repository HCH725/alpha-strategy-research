---
schema: strategy-research-record-v1
title: "NASDAQ Level 3 Order Book Imbalance and Microstructure Alpha Leakage Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - microstructure
  - order-book-imbalance
  - high-frequency
  - falsification
  - negative-result
  - leakage-audit
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "https://github.com/Jack-Fletcher-Projects/microstructure-alpha (commit d0cd0e7f6cbd4ef12fca818d19cfa9a43103c398, 2026-09-11)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# NASDAQ Level 3 Order Book Imbalance and Microstructure Alpha Leakage Falsification

## Provenance

- **Primary Source Codebase:** `Jack-Fletcher-Projects/microstructure-alpha` (*Order book features from raw NASDAQ L3 data, and a validation framework measuring how much of a backtested edge is leakage*), authored by Jack Fletcher (`source-reported`).
- **Canonical Source Identity:** GitHub repository `https://github.com/Jack-Fletcher-Projects/microstructure-alpha` at immutable commit SHA `d0cd0e7f6cbd4ef12fca818d19cfa9a43103c398` (committed 2026-09-11 14:00:04 UTC) (`source-reported`).
- **Primary Source Documentation:** `README.md` (9,078 bytes) in `Jack-Fletcher-Projects/microstructure-alpha`, detailing empirical validation tables, leakage inflation mechanics, Benjamini-Hochberg block-bootstrap screening, and lookahead testing (`source-reported`).
- **Source Modules Directly Inspected:**
  - `alpha/features.py` (LOBSTER L3 raw message and book loading, order-flow feature calculations, lookahead-free clock grid alignment, causal VPIN, forward return labeling) (`source-reported`).
  - `alpha/validation.py` (Purged walk-forward cross-validation with embargo, effective sample size calculation, circular block bootstrap null, Benjamini-Hochberg step-up FDR control, rank-based AUC score) (`source-reported`).
  - `alpha/model.py` (Fixed XGBoost gradient boosted tree configuration with regularized tree depth) (`source-reported`).
  - `scripts/run_study.py` (End-to-end study runner reproducing leakage inflation and univariate screening across 1s, 5s, 10s, 30s, and 60s horizons) (`source-reported`).
  - `tests/test_alpha.py` (14 unit tests including bit-identical session truncation lookahead verification, resting-side execution sign inversion, and FDR step-up properties) (`source-reported`).
- **Dataset Evaluated:** Raw NASDAQ Level 3 limit order book data reconstructed via LOBSTER for Amazon (`AMZN`) on 2012-06-21, regular trading session 09:30:00 to 16:00:00 EST (34,200 to 57,600 seconds after midnight), covering 10 levels of visible bids and asks (`source-reported`).
- **Deduplication Audit:** A comprehensive repository-wide audit confirms zero pre-existing records citing `Jack-Fletcher-Projects`, Jack Fletcher, or commit `d0cd0e7f6cbd4ef12fca818d19cfa9a43103c398`. Prior microstructure records in this repository evaluate distinct authors, datasets, and methods:
  - `us-equity-microstructure-ensemble-lightgbm-fdr-falsification-2026-09-13.md` (Breeganzo, commit `c5ad8357e7a8`) evaluates a 50-stock cross-sectional daily panel.
  - `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Mungale, commit `6bfa0995166f`) evaluates C++ LOBSTER data for INTC and GOOG on CKS OFI vs static queue imbalance.
  - `binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13.md` evaluates crypto perpetual 100 ms `bookTicker` flow on BTCUSDT.
  - `causal-knn-predictive-flow-leakage-falsification-2026-09-13.md` (Darang, commit `21b3a98c4cca`) evaluates kNN pattern matching on 4H crypto candles.
  - Jack Fletcher's work provides an independent, rigorous econometric study directly measuring and falsifying overlapping-label leakage across a 1s to 60s horizon ladder on high-frequency NASDAQ Level 3 data.

## Economic mechanism

### Source-reported

1. **Microstructure Pressure Signals:** At sub-second to ultra-short horizons, resting limit order book imbalance (OBI) and trade flow imbalance (TFI) reflect immediate imbalances between liquidity provision and liquidity consumption. When top-of-book bids exceed asks ($q^b_1 > q^a_1$), liquidity takers consume resting asks faster than bids, pushing the microprice $((P^a_1 q^b_1 + P^b_1 q^a_1) / (q^a_1 + q^b_1))$ toward the ask and predicting an immediate upward quote revision. Similarly, buyer-initiated trades (inferred from executions against resting sells) deplete available depth, driving market makers to shade quotes upward.
2. **Label Overlap Leakage in Naive ML:** In high-frequency machine learning studies sampled on a 1-second grid with forward prediction horizons $h \in \{5, 10, 30, 60\}$ seconds, adjacent labels share $(h - 1) / h$ fraction of their constituent price increments. When standard shuffled $k$-fold cross-validation is applied, near-duplicate observations of the test labels are randomly placed into the training set. This creates severe lookahead contamination that inflates apparent out-of-sample predictability (AUC rising from 0.6264 at 1s to 0.8300 at 60s).
3. **Honest Microstructural Decay:** When causal temporal separation is strictly enforced using purged walk-forward splits with an embargo buffer ($2 \times h$), the apparent predictive edge collapses as horizon lengthens (falling from 0.6127 at 1s to 0.4981 at 60s). The information contained in top-of-book imbalance and signed trade flow is fully incorporated into prices within 30 seconds (where OBI AUC decays to 0.502 and microprice deviation decays to 0.496).

### Research interpretation

1. **Mechanical Friction vs. Economic Alpha:** The genuine 1-second edge (univariate AUC 0.5842 for `obi_1` and 0.5882 for `tfi_5s`) represents mechanical queue depletion and short-term quote updating rather than persistent economic alpha. In equity markets, algorithmic liquidity providers adjust quotes within hundreds of milliseconds.
2. **The Spread Hurdle:** The median bid-ask spread in the source sample is approximately 13 cents on AMZN ($P \approx \$220$, or $\sim 5.9$ bps). A 1-second directional edge of AUC $\approx 0.588$ sits entirely inside the bid-ask spread. Aggressive market orders that cross the spread suffer an immediate negative hurdle equal to half the spread, rendering directional taker strategies unprofitable net of costs.
3. **Adverse Selection in Passive Execution:** While passive limit orders could theoretically capture the spread, they face severe adverse selection: limit orders fill preferentially when informed traders trade through the queue, causing adverse post-fill price drift.

## Signal

### Signal formation and causal grid alignment

- **Sampling Grid:** Regular 1.0-second clock grid ($step = 1.0$ s) spanning $t \in [34200, 57600]$ seconds after midnight (`source-reported`).
- **Causal Indexing:** At grid time $t$, book and message states are resolved strictly at or before $t$ via `idx = np.searchsorted(t_msg, grid, side="right") - 1` (`source-reported`).
- **Feature Pipeline:** 15 normalized microstructure features computed from Level 3 order book snapshots and signed trade messages (`source-reported`):
  1. `obi_1`: Level-1 Order Book Imbalance: $(q^b_1 - q^a_1) / (q^b_1 + q^a_1)$.
  2. `obi_5`: Level-5 Cumulative Order Book Imbalance: $(\sum_{i=1}^5 q^b_i - \sum_{i=1}^5 q^a_i) / (\sum_{i=1}^5 q^b_i + \sum_{i=1}^5 q^a_i)$.
  3. `obi_10`: Level-10 Cumulative Order Book Imbalance: $(\sum_{i=1}^{10} q^b_i - \sum_{i=1}^{10} q^a_i) / (\sum_{i=1}^{10} q^b_i + \sum_{i=1}^{10} q^a_i)$.
  4. `microprice_dev`: Microprice deviation from midprice: $(P_{micro} - P_{mid}) / P_{mid}$, where $P_{micro} = (P^a_1 q^b_1 + P^b_1 q^a_1) / (q^a_1 + q^b_1)$.
  5. `spread_rel`: Relative bid-ask spread: $(P^a_1 - P^b_1) / P_{mid}$.
  6. `depth_ratio`: Log ratio of cumulative 5-level depth: $\log((q^b_{1..5} + 1.0) / (q^a_{1..5} + 1.0))$.
  7. `tfi_5s`: Trade Flow Imbalance over trailing 5 seconds: $\sum_{t-5}^t \text{signed\_size} / \sum_{t-5}^t \text{size}$ (zero when no trades occurred).
  8. `tfi_30s`: Trade Flow Imbalance over trailing 30 seconds: $\sum_{t-30}^t \text{signed\_size} / \sum_{t-30}^t \text{size}$.
  9. `trade_rate_30s`: Trailing trade frequency: total trades in trailing 30s divided by 30.0.
  10. `vpin`: Volume-Synchronized Probability of Toxicity, calibrated strictly on initial 1800s warmup ($V_{bucket} = \sum_{w} \text{size} / 50.0$), rolling mean across 50 completed volume buckets mapped to clock grid without forward leakage.
  11. `rv_30s`: Realized volatility: rolling standard deviation of 1-second log returns over trailing 30 seconds.
  12. `ret_ac1`: First-order serial autocorrelation of 1-second log returns over trailing 60 seconds (min periods 30).
  13. `ret_1s`: Trailing 1-second log midprice return: $\log(P_{mid, t} / P_{mid, t-1})$.
  14. `ret_5s`: Trailing 5-second log midprice return: $\log(P_{mid, t} / P_{mid, t-5})$.
  15. `ret_30s`: Trailing 30-second log midprice return: $\log(P_{mid, t} / P_{mid, t-30})$.
- **Trade Signing Rule:** In LOBSTER, message event type 4 or 5 indicates execution against a resting order. Because LOBSTER's `direction` field records the side of the *resting* order, execution sign is inverted (`sign = +1` if resting sell `direction == -1`; `sign = -1` if resting buy `direction == 1`), eliminating the need for heuristic tick or Lee-Ready rules (`source-reported`).
- **Forward Outcome Labels:**
  - Forward log return: $\Delta p_{t, h} = \log(P_{mid, t+h}) - \log(P_{mid, t})$ for $h \in \{1, 5, 10, 30, 60\}$ seconds (`source-reported`).
  - Binary direction label: $y_{t, h} = \text{sign}(\Delta p_{t, h}) \in \{-1, +1\}$ (rows with zero return dropped) (`source-reported`).
- **Machine Learning Architecture:**
  - Model: Fixed XGBoost gradient boosted tree (`XGBClassifier`) (`source-reported`).
  - Hyperparameters: `n_estimators=200`, `max_depth=4`, `learning_rate=0.05`, `subsample=0.8`, `colsample_bytree=0.8`, `reg_lambda=1.0`, `min_child_weight=10`, `eval_metric="logloss"` (`source-reported`). No horizon-specific hyperparameter tuning is conducted, preventing post-hoc selection bias.

### Operational rules and execution triggers

The primary source evaluates econometric directional predictability (AUC) rather than executing simulated trades. To make the hypothesis operational for quantitative validation, the following rules are defined:
- **Directional Entry Trigger:** `research-proposed`:
  - Long Entry: At grid time $t$, execute Buy at $t + \delta$ if predicted probability $\hat{P}(\text{up}) \ge 0.55$.
  - Short Entry: At grid time $t$, execute Sell Short at $t + \delta$ if predicted probability $\hat{P}(\text{up}) \le 0.45$.
  - Neutral / No Trade: If $0.45 < \hat{P}(\text{up}) < 0.55$, no order is dispatched.
- **Execution Timing Delay:** `research-proposed`: $\delta = 50$ ms execution latency buffer from grid timestamp $t$.
- **Exit Trigger:** `research-proposed`:
  - Time-based Exit: Unconditionally close position at $t + h$ seconds ($h = 1$s or $h = 5$s depending on the targeted horizon).
  - Stop-Loss / Take-Profit: `research-proposed`: Optional protective stop at $1.5 \times \text{spread}$.
- **Position Sizing:** `research-proposed`: Fixed fraction of equity or fixed share size (e.g. 100 shares), strictly un-leveraged.

## Required data

- **Instrument:** Single-stock US equity: Amazon.com Inc. (`AMZN`) (`source-reported`).
- **Venue:** NASDAQ National Market System (`source-reported`).
- **Market Type:** Cash equity spot (`source-reported`).
- **Sample Window:** 2012-06-21, 09:30:00 to 16:00:00 EST (6.5 continuous trading hours, 34,200 to 57,600 seconds) (`source-reported`).
- **Data Feed:** LOBSTER Level 3 limit order book message feed and orderbook state feed (`source-reported`).
  - `message_10.csv`: Timestamp (seconds with decimal precision), Event Type (1: New Order, 2: Partial Cancel, 3: Delete, 4: Visible Exec, 5: Hidden Exec), Order ID, Size (shares), Price (in 1/10000 USD), Direction (-1: Sell/Ask, +1: Buy/Bid).
  - `orderbook_10.csv`: 40 columns containing Ask Price 1..10, Ask Size 1..10, Bid Price 1..10, Bid Size 1..10.
- **Data Filtering & Cleaning:**
  - Absent book levels padded with $\pm 9999999999$ masked as `np.nan` before depth aggregation (`source-reported`).
  - Warmup period: First 1,800 seconds ($t \le 36000$) reserved for VPIN volume bucket calibration; VPIN feature is `np.nan` during warmup (`source-reported`).
- **Point-in-Time Discipline:**
  - Feature timestamp $t$ uses binary search (`side="right"` minus 1) to guarantee that only events strictly occurring at or before $t$ enter the feature vector (`source-reported`).
  - Session truncation invariance verified: Truncating the dataset at 60% of the session produces bit-identical feature values on the overlapping prefix (`source-reported`, verified in `test_features_do_not_use_future_data`).

## Execution assumptions

- **Source-Reported Execution Context:**
  - The source does **not** assume a commercial trading execution engine; performance is evaluated purely via directional discrimination (out-of-sample AUC) predicting midprice direction (`source-reported`).
  - The author explicitly states: *"AUC measures directional accuracy, not profit. The 1-second edge sits well inside a 13-cent median spread, so it is not by itself tradeable — capturing it would require queue position and passive fills, which this data cannot model."* (`source-reported`).
- **Research-Proposed Execution Model:**
  - Fill Model: Midpoint or top-of-book execution. For aggressive taker orders: Buy fills at Ask ($P^a_1$), Sell fills at Bid ($P^b_1$) (`research-proposed`).
  - Transaction Costs: NASDAQ maker-taker fee schedule: taker fee $30$ cents per 100 shares ($\sim 1.36$ bps on $\$220$ stock), maker rebate $20$ cents per 100 shares, plus SEC/FINRA regulatory fees (`research-proposed`).
  - Bid-Ask Spread Drag: Median spread of 13 cents ($\sim 5.9$ bps). A round-trip aggressive trade incurs $\sim 14.5$ bps in total friction (spread + taker fees) (`research-proposed`).
  - Latency: Minimum 50 ms to 100 ms network and matching engine colocation latency (`research-proposed`).
  - Slippage and Queue Degradation: In aggressive execution, queue exhaustion at Level 1 requires walking the book; in passive execution, non-execution and adverse selection must be accounted for (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures below are cited directly from Jack Fletcher (`Jack-Fletcher-Projects/microstructure-alpha`, commit `d0cd0e7f6cbd4ef12fca818d19cfa9a43103c398`, `README.md` and `scripts/run_study.py`):

#### 1. Cross-Validation Leakage and Horizon Decay Ladder

Comparison between naive shuffled 5-fold cross-validation and purged walk-forward cross-validation (5 splits, test fold preceded by purge window of $h$ steps and embargo buffer of $2 \times h$ steps):

| Forward Horizon | Shuffled $k$-Fold AUC | Purged Walk-Forward AUC | Leakage Inflation | Total Rows | Effective Sample Size ($n_{eff}$) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **1s** | 0.6264 | **0.6127** | +0.0137 | 6,370 | 6,370 |
| **5s** | 0.7257 | **0.5729** | +0.1528 | 14,860 | 2,972 |
| **10s** | 0.7567 | **0.5382** | +0.2185 | 18,171 | 1,817 |
| **30s** | 0.8160 | **0.5144** | +0.3016 | 20,749 | 692 |
| **60s** | 0.8300 | **0.4981** | +0.3319 | 21,007 | 350 |

- **Empirical Finding:** Shuffled $k$-fold cross-validation shows an artificial increase in AUC from 0.6264 to 0.8300 as horizon expands from 1s to 60s. Purged walk-forward CV shows the opposite, truthful decay: AUC collapses from 0.6127 at 1s to 0.4981 (random coin flip) at 60s.
- **Leakage Quantum:** At 60 seconds, label overlap creates +0.3319 of spurious AUC inflation.

#### 2. Univariate Feature Screening at 1-Second Horizon (9 of 15 Features Survive)

Tested against a circular block bootstrap null (block size $\max(60, 3h)$, 1,500 resamples) with Benjamini-Hochberg false discovery rate control at $\alpha = 0.05$:

| Feature | Univariate AUC | $p$-value (Block Bootstrap) | $p$-value Adjusted (BH-FDR) | Significant ($\alpha=0.05$) |
|:---|:---:|:---:|:---:|:---:|
| `tfi_5s` | 0.5882 | 0.0000 | 0.0000 | **Yes** |
| `obi_1` | 0.5842 | 0.0000 | 0.0000 | **Yes** |
| `microprice_dev` | 0.5781 | 0.0000 | 0.0000 | **Yes** |
| `tfi_30s` | 0.5778 | 0.0000 | 0.0000 | **Yes** |
| `ret_30s` | 0.5582 | 0.0000 | 0.0000 | **Yes** |
| `ret_5s` | 0.5578 | 0.0000 | 0.0000 | **Yes** |
| `ret_1s` | 0.5356 | 0.0000 | 0.0000 | **Yes** |
| `obi_5` | 0.5244 | 0.0010 | 0.0020 | **Yes** |
| `depth_ratio` | 0.5244 | 0.0010 | 0.0020 | **Yes** |
| `ret_ac1` | 0.5064 | 0.4690 | 0.6620 | No |
| `obi_10` | 0.4937 | 0.4930 | 0.6620 | No |
| `spread_rel` | 0.4952 | 0.5510 | 0.6620 | No |
| `vpin` | 0.4952 | 0.5730 | 0.6620 | No |
| `trade_rate_30s` | 0.4965 | 0.7040 | 0.7540 | No |
| `rv_30s` | 0.5017 | 0.8410 | 0.8410 | No |

#### 3. Univariate Feature Screening at 30-Second Horizon (1 of 15 Features Survives)

| Feature | Univariate AUC | $p$-value (Block Bootstrap) | $p$-value Adjusted (BH-FDR) | Significant ($\alpha=0.05$) |
|:---|:---:|:---:|:---:|:---:|
| `tfi_5s` | 0.5428 | 0.0000 | 0.0000 | **Yes** |
| `ret_30s` | 0.4705 | 0.0510 | 0.3850 | No |
| `ret_1s` | 0.5060 | 0.1220 | 0.6100 | No |
| `tfi_30s` | 0.5169 | 0.2510 | 0.9430 | No |
| *(11 other features)* | ~0.493 to 0.504 | > 0.4000 | > 0.9000 | No |

### Independently reproduced

- `not independently reproduced`.
- The study's codebase and 14 unit tests were inspected directly from GitHub clone snapshot `d0cd0e7f6cbd4ef12fca818d19cfa9a43103c398`. All empirical figures and regression tables reflect the primary findings reported by Jack Fletcher.

### Negative evidence

1. **Falsification of Multi-Second Predictability:** Naive ML claims that microstructure features predict 30-second to 60-second forward returns (AUC $\sim 0.816 - 0.830$) are completely falsified. Under causal purged walk-forward cross-validation, predictive discrimination at 60s decays to 0.4981, confirming that published high-AUC results at multi-second horizons are artifacts of label overlap leakage.
2. **Order Book Imbalance Half-Life Decay:** Level-1 Order Book Imbalance (`obi_1`) and Microprice Deviation (`microprice_dev`), which are highly significant at 1 second (AUC 0.5842 and 0.5781, $p < 0.0001$), decay to complete unpredictability by 30 seconds (AUC 0.502 and 0.496).
3. **Data Snooping via Multiple Testing:** At the 30-second horizon, trailing return `ret_30s` exhibits a raw $p$-value of 0.0510, which naive reporting would highlight as a near-significant finding; however, after Benjamini-Hochberg FDR adjustment across the 15-feature panel, the adjusted $p$-value rises to 0.3850, properly classifying it as statistical noise.
4. **Untradeability Under Taker Friction:** The 1-second directional edge (AUC 0.6127 for ensemble, 0.5882 for top feature) operates entirely within the 13-cent median spread ($\sim 5.9$ bps), failing to cover round-trip taker fees and spread crossing costs.

## Falsification plan

To falsify the source's findings or evaluate whether any microstructural edge can be extracted commercially, the following operational tests are defined:

1. **Label Overlap Permutation Test:**
   - *Protocol:* On any new microstructure dataset, train the XGBoost classifier under (a) standard shuffled $k$-fold CV and (b) PurgedWalkForward ($h$ purge steps, $2h$ embargo steps).
   - *Falsification Cutoff:* `research-defined falsification threshold`: If the difference $\text{AUC}_{\text{shuffled}} - \text{AUC}_{\text{purged}} > 0.10$ at $h \ge 10$s, the candidate strategy's claimed performance is declared invalid and rejected due to label leakage.
2. **Spread Hurdle Directional Taker Test:**
   - *Protocol:* Simulate aggressive taker execution at $t + 50$ ms when $\hat{P}(\text{up}) \ge 0.55$, paying the prevailing Ask and exiting at $t + h$ at the prevailing Bid.
   - *Falsification Cutoff:* `research-defined falsification threshold`: If the net strategy Sharpe ratio is $\le 0.0$ and cumulative net PnL is negative across all probability thresholds $\theta \in [0.51, 0.70]$, directional taker execution is falsified.
3. **Passive Queue Execution Adverse Selection Test:**
   - *Protocol:* Simulate passive limit orders placed at Bid/Ask at $t$, modeling strict FIFO queue placement based on observed depth. Evaluate post-fill 5-second mark-to-market return.
   - *Falsification Cutoff:* `research-defined falsification threshold`: If post-fill forward return conditional on passive fill is negative (indicating adverse selection dominates the bid-ask rebate), the passive market-making adaptation is falsified.
4. **Multiple-Testing FDR Horizon Sweep:**
   - *Protocol:* Screen the 15-feature panel against circular block bootstrap null (1,500 resamples) at horizons $h \in \{1, 5, 10, 30, 60\}$ seconds with Benjamini-Hochberg FDR control at $q = 0.05$.
   - *Falsification Cutoff:* `research-defined falsification threshold`: If zero features survive at $h \ge 10$ seconds, any claim of medium-horizon microstructure predictability in that asset is rejected.

## Crypto portability

- **Portability Classification:** `adapted / unproven` (`source-reported` findings are exclusively on US equity NASDAQ Level 3 data).
- **Crypto Market Structural Differences:**
  1. **Trade Sign Oracle:** In LOBSTER equities, trades identify the resting order direction explicitly (`direction = -1` for resting sell). In cryptocurrency exchanges (e.g. Binance, Bybit, OKX), trade streams do not use LOBSTER event codes. Instead, trade aggressor side must be inferred from exchange-specific fields: on Binance, `isBuyerMaker == True` indicates the buyer was the passive maker (so the trade was seller-initiated/taker sell), while `isBuyerMaker == False` indicates buyer-initiated/taker buy.
  2. **Book Depth Availability:** NASDAQ L3 messages allow complete order-by-order book reconstruction up to 10 levels. In crypto, public WebSocket feeds offer Level 2 aggregated order book snapshots/deltas (e.g. Binance `depth@100ms` or `bookTicker`) rather than full Level 3 ITCH market-by-order feeds.
  3. **Fee Hurdle & Taker Economics:** Binance VIP0 spot fees (10 bps taker / 10 bps maker) or VIP0 perpetual fees (5 bps taker / 2 bps maker) represent a substantial friction relative to high-frequency price changes. An AUC of 0.61 at 1 second cannot overcome a 10 bps round-trip taker fee.
  4. **Continuous 24/7 Liquidity:** Unlike NASDAQ's 09:30–16:00 session, crypto markets trade 24/7 without opening/closing auctions, but experience periodic volatility bursts and funding rate settlement dislocations (every 8 hours or 1 hour).
  5. **Portability Verdict:** The econometric validation methodology (purging, embargo, block bootstrap, effective sample size, and Benjamini-Hochberg FDR control) ports directly and identically to cryptocurrency tick research; however, the predictive signal itself remains unproven and likely uneconomic under retail fee tiers.

## Limitations

1. **Single-Stock, Single-Session Sample:** Sourced from 6.5 hours of Amazon (`AMZN`) on June 21, 2012. While the 1-second results align with theoretical market microstructure literature, single-day data cannot establish cross-sectional or multi-regime generalization (`source-reported`).
2. **Small Effective Sample Size at Longer Horizons:** Due to label autocorrelation and overlap, 21,007 rows at a 60-second horizon represent only 350 independent observations, leading to wide confidence intervals (`source-reported`).
3. **Absence of Transaction Cost Engine:** The primary study evaluates purely statistical discrimination (AUC) rather than economic profitability after fees, spread, and queue latency (`source-reported`).
4. **Truncated Level-10 Depth:** LOBSTER message feeds track events affecting the top 10 levels only; deeper liquidity replenishments and hidden iceberg orders beneath Level 10 are unobserved (`source-reported`).
5. **Modified Within-Day VPIN:** Standard VPIN spans several trading days with 50 volume buckets per day. On a single intraday session, the warmup window (1,800s) produces a localized within-day proxy rather than multi-day institutional flow toxicity (`source-reported`).

## Implementation status

- `not-implemented`.
- No implementation has been created in PyBroker, NautilusTrader, paper trading, testnet, or live trading environments. This record is a public research capture and methodological falsification analysis.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record represents an upstream research capture documenting methodological lookahead leakage in high-frequency microstructure modeling. It does not constitute an approved strategy, trading authorization, or validation for execution.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical purged walk-forward cross-validation, combinatorial purged cross-validation (CPCV), and embargo mechanics.
- `[[quant/us-equity-microstructure-ensemble-lightgbm-fdr-falsification-2026-09-13]]` — Breeganzo's 50-ticker US equity microstructure ensemble demonstrating failure of individual tickers under Benjamini-Hochberg FDR correction.
- `[[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]]` — Mungale's NASDAQ LOBSTER study demonstrating contemporaneous-to-predictive decoupling and taker spread hurdles.
- `[[quant/crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31]]` — Standalone VPIN metric evaluation in crypto microstructure.
- `[[quant/binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13]]` — Order flow imbalance horizon decay and queue depletion on Binance perpetuals.

## Sources

1. **Primary Research Repository:** Jack Fletcher (2026), *Order book features from raw NASDAQ L3 data, and a validation framework measuring how much of a backtested edge is leakage*, public GitHub repository `Jack-Fletcher-Projects/microstructure-alpha`.
   - Repository URL: `https://github.com/Jack-Fletcher-Projects/microstructure-alpha`
   - Canonical Commit SHA: `d0cd0e7f6cbd4ef12fca818d19cfa9a43103c398` (Committed 2026-09-11 14:00:04 UTC).
   - Core Artifacts Inspected:
     - `README.md` (empirical tables, leakage inflation proof, BH-FDR results)
     - `alpha/features.py` (LOBSTER parser, feature extraction, causal VPIN, forward labels)
     - `alpha/validation.py` (PurgedWalkForward, effective_sample_size, block_bootstrap_null, benjamini_hochberg, auc_score)
     - `alpha/model.py` (fixed XGBoost configuration)
     - `scripts/run_study.py` (study orchestration and figure reproduction)
     - `tests/test_alpha.py` (14 unit tests including truncation invariance)
2. **Foundational Academic References Cited in Source:**
   - David Easley, Marcos M. López de Prado, and Maureen O'Hara (2012), *Flow Toxicity and Liquidity in a High-Frequency World*, The Review of Financial Studies, 25(5), pp. 1457–1493. DOI: [10.1093/rfs/hhs053](https://doi.org/10.1093/rfs/hhs053).
   - Marcos López de Prado (2018), *Advances in Financial Machine Learning*, John Wiley & Sons, Inc. ISBN: 978-1-119-48208-6.
   - Yoav Benjamini and Yosef Hochberg (1995), *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*, Journal of the Royal Statistical Society: Series B (Methodological), 57(1), pp. 289–300. DOI: [10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x).
   - Dimitris N. Politis and Joseph P. Romano (1994), *The Stationary Bootstrap*, Journal of the American Statistical Association, 89(428), pp. 1303–1313. DOI: [10.1080/01621459.1994.10476870](https://doi.org/10.1080/01621459.1994.10476870).
