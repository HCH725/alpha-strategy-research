---
schema: strategy-research-record-v1
title: "Causal kNN Predictive Flow Feature Matching and Information Coefficient Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - machine-learning
  - knn
  - falsification
  - negative-result
  - lookahead-audit
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - "https://github.com/darangworks/causal-knn-crypto-strategy (commit 21b3a98c4cca73c97508f9b1b907fcda15424a0a, 2026-09-12)"
  - "https://www.tradingview.com/script/qaaxkW1P-AI-Predictive-Flow-Zeiierman/ (Zeiierman AI Predictive Flow indicator, 2023-2024)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Causal kNN Predictive Flow Feature Matching and Information Coefficient Falsification

## Provenance

- **Primary research repository:** https://github.com/darangworks/causal-knn-crypto-strategy
- **Full commit SHA:** `21b3a98c4cca73c97508f9b1b907fcda15424a0a` (latest commit "Reorganize files into src/ validation/ tests/", 2026-09-12T13:17:41Z)
- **Primary documentation:** `REPORT.md` (v1.2 frozen data revision, 2026-09-12)
- **Core strategy backtest script:** `src/diagnostic_v11_4h_notrail.py`
- **Validation modules:** `validation/diagnostic_v13_walkforward.py`, `validation/diagnostic_v14_kfold.py`, `validation/diagnostic_v15_crossasset.py`, `src/run_local_baseline.py`
- **Verification suite:** `tests/test_causal_knn_corrected.py` (7/7 causal mechanics tests passed), `accounting/sympy_proof.py` (symbolic equivalence proof)
- **Primary author:** Mohammad Darang (2026)
- **Original indicator source:** Zeiierman, "AI Predictive Flow" (TradingView public script: `https://www.tradingview.com/script/qaaxkW1P-AI-Predictive-Flow-Zeiierman/`, CC BY-NC-SA 4.0)
- **Data snapshot and manifests:** `data/MANIFEST.md` with SHA-256 hashes for BTC-USD (4H, 1H), ETH-USD (4H), SOL-USD (4H) covering 2024-09-13 to 2026-09-12

## Economic mechanism

### Source-reported

The original Zeiierman TradingView indicator posits that financial asset time series contain recurrent multi-dimensional price action and momentum patterns. By computing a 4-feature state vector at each bar (1-bar log return, 5-bar momentum, centered RSI, and EMA spread) across a pattern window of 10 bars, and storing these historical patterns in memory, the system uses a k-Nearest Neighbors (kNN) algorithm under Euclidean distance to retrieve the `k` closest historical analog patterns. The subsequent price movements following those historical analogs are weighted by inverse distance to project an expected price change (predictive flow), smoothed by an exponential moving average to produce an oscillating trading signal.

However, Darang's source-reported forensic audit identifies two critical lookahead and data leakage defects in the original indicator when evaluated as an algorithmic trading strategy:
1. **Backward Target Definition:** In Pine Script, the label variable was defined as `y := math.log(base) - math.log(base[ahead])`. Because the indexing operator `[ahead]` references past bars in Pine Script syntax rather than future bars, this calculated past return over `ahead` bars rather than forward return.
2. **Memory Self-Contamination:** The current bar's feature vector was appended to the training memory buffer before executing the nearest-neighbor query, causing the query pattern to match against itself as its own nearest neighbor with zero distance.

Darang's causal reconstruction corrects both issues: training memory updates are strictly delayed by `ahead` bars (`train_end = i - AHEAD`), labels are forward log returns `math.log(close[i] / close[train_end])`, feature components are volatility-normalized by ATR and clipped to `[-5.0, 5.0]`, and memory is managed via a bounded circular ring buffer.

### Research interpretation

Non-parametric pattern-matching techniques such as kNN operate under the manifold hypothesis: that market microstructure states reside on a low-dimensional manifold embedded within technical feature space. Under this hypothesis, recurrence in feature space implies recurrence in conditional forward return distributions.

In liquid cryptocurrency spot markets, this hypothesis fails empirically once causal discipline is enforced. Specifically:
1. **Feature Space Noise and Dimensionality:** A 40-dimensional feature vector (4 features over 10 consecutive bars) creates extreme sparsity in a small memory buffer (80 historical patterns). In Euclidean space, the distance between genuine analogs and random noise patterns converges, leading to arbitrary neighbor selection.
2. **Information Coefficient Decoupling:** The causal kNN output exhibits a negative unconditional Information Coefficient (Pearson IC −0.02800, Spearman IC −0.02912) and an inverted quintile profile (Q5 lowest, Q1 highest forward return).
3. **Regime Gating vs. Model Edge:** Any positive full-sample return observed in naive backtests is driven not by kNN pattern prediction, but by macro trend and volatility regime filters (50 EMA higher timeframe trend alignment, Bollinger Band width expansion, ADX thresholding, and volume breakout confirmation) that capture right-tail crypto drift during bull regimes.

## Signal

### Signal formation timestamp

The signal is formed at the close of 4-hour bar `i`. Trade entry is executed at the open of bar `i+1` (`next-bar Open execution`).

### Feature extraction and normalization

At bar `t`, four technical features are extracted:
- Normalized volatility denominator: `vn = max(ATR[14] / Close[t], 1e-6)`
- `f1 = (log(Close[t] / Close[t-1])) / vn` (volatility-normalized 1-bar log return)
- `f2 = (Close[t] - Close[t-5]) / ATR[14]` (volatility-normalized 5-bar momentum)
- `f3 = (RSI[14] - 50.0) / 50.0` (centered RSI oscillator, bounded `[-1.0, 1.0]`)
- `f4 = (EMA[10] - EMA[30]) / ATR[14]` (normalized moving average convergence spread)
- Feature clipping: All feature values are clipped to `[-5.0, 5.0]` to eliminate non-stationary outlier contamination.

A pattern vector at bar `t` concatenates the 4 features across lookback window `PATTERN_LEN = 10` bars (total 40 dimensions):
`X_vec(t) = [f1[t-9:t], f2[t-9:t], f3[t-9:t], f4[t-9:t]]`

### Bounded causal memory buffer and delayed labels

- Prediction horizon: `AHEAD = 2` bars (source-reported).
- Label delay: At bar `i`, the observation available for training has endpoint `te = i - AHEAD`.
- Training label: `Y = log(Close[i] / Close[te])` (causally observed forward return from `te` to `i`).
- Training pattern: `X_vec(te)` extracted over `[te - PATTERN_LEN + 1 : te + 1]`.
- Circular ring buffer: Memory capacity `MEMORY_SIZE = 80` historical vectors. Oldest vectors overwritten when capacity is reached.
- Query pattern: `X_vec(i)` extracted over `[i - PATTERN_LEN + 1 : i + 1]`.
- Minimum warm-up: At least `K_NEIGHBORS = 5` valid historical vectors must populate memory before inference begins (`req = max(350, PATTERN_LEN + AHEAD + 50, HTF_EMA_LEN * 4 + 50)` bars total warm-up).

### Nearest-neighbor inference

- Distance metric: Euclidean distance `d_j = ||X_j - query||_2` for all stored patterns `j = 1, ..., min(count, MEMORY_SIZE)`.
- K selection: `K_NEIGHBORS = 5` smallest distances.
- Weighting: Normalized inverse-distance weighting (IDW):
  `w_j = 1.0 / (d_j + 1e-6)`
  `pred_raw = sum(w_j * Y_j) / sum(w_j)`
- Signal smoothing: Exponential moving average with period `PRED_SMOOTH = 4` (`alpha = 2.0 / (4 + 1) = 0.4`):
  `pred_ema[i] = alpha * pred_raw[i] + (1 - alpha) * pred_ema[i-1]`

### Multi-component regime confirmation filters

The strategy combines the kNN oscillator with four confirmation filters:
1. **Prediction score threshold:** Normalized score `sc = pred_ema / (ATR_PCT / 100.0)`. Long requires `sc >= MIN_PRED_ATR = 0.20`; short requires `sc <= -MIN_PRED_ATR = -0.20`.
2. **Higher timeframe (HTF) trend filter:** 50-period EMA (`HTF_EMA_LEN = 50`) on 4H close (`HTF_TIMEFRAME = "4h"`), lagged by 1 bar. Long requires `Close[i] > HTF_EMA[i]`; Short requires `Close[i] < HTF_EMA[i]`.
3. **Volatility expansion filter:** `ATR_PCT[i] >= MIN_ATR_PCT = 0.25%` AND Bollinger Band width `BB_WIDTH_PCT[i] >= MIN_BB_WIDTH_PCT = 1.0%` (`BB_LEN = 20`, `BB_MULT = 2.0`).
4. **Volume expansion filter:** Bar volume must exceed 1.1x the 20-period volume SMA (`VOLUME_LEN = 20`, `VOLUME_MULT = 1.1`).
5. **Trend strength filter:** Wilder ADX(14) >= `MIN_ADX = 18.0`.

### Long entry trigger

Execute long at `Open[i+1]` if at bar `i`:
- `sc >= 0.20`
- `Close[i] > HTF_EMA[i]`
- Volatility filter active (`ATR_PCT >= 0.25` and `BB_WIDTH_PCT >= 1.0`)
- Volume filter active (`Volume > 1.1 * VOL_SMA`)
- ADX filter active (`ADX >= 18.0`)
- Current position `pos <= 0`

### Short entry trigger

Execute short at `Open[i+1]` if at bar `i`:
- `sc <= -0.20`
- `Close[i] < HTF_EMA[i]`
- Volatility filter active
- Volume filter active
- ADX filter active
- Current position `pos >= 0`

### Exit rules

- **Initial stop loss:** Fixed ATR multiple at entry: `ep - STOP_ATR * ATR` for long, `ep + STOP_ATR * ATR` for short (`STOP_ATR = 2.0`).
- **Take profit target:** Fixed ATR multiple at entry: `ep + TP_ATR * ATR` for long, `ep - TP_ATR * ATR` for short (`TP_ATR = 3.5`).
- **Intrabar stop/TP evaluation:** Evaluated intrabar against `High[i]` and `Low[i]`; opening gaps past stop/TP filled at `Open[i]`.
- **Opposing signal reversal:** If a valid pending signal opposes the active position, the existing position is closed at `Open[i+1]` before opening the reverse position.
- **Trailing stop:** Disabled in the primary tested configuration (`TRAIL_ATR = 999.0`).
- **Maximum holding period:** `research-proposed`: 20 bars (80 hours) time-based exit to prevent capital lockup if price remains bounded between TP and SL.

### Sizing and parameters

| Parameter | Value | Classification |
|-----------|-------|----------------|
| `TIMEFRAME` | 4h | Source-reported |
| `PATTERN_LEN` | 10 bars | Source-reported |
| `MEMORY_SIZE` | 80 patterns | Source-reported |
| `K_NEIGHBORS` | 5 neighbors | Source-reported |
| `AHEAD` | 2 bars | Source-reported |
| `PRED_SMOOTH` | 4 periods | Source-reported |
| `MIN_PRED_ATR` | 0.20 | Source-reported |
| `HTF_EMA_LEN` | 50 periods | Source-reported |
| `ATR_LEN` | 14 periods | Source-reported |
| `MIN_ATR_PCT` | 0.25% | Source-reported |
| `BB_LEN` | 20 periods | Source-reported |
| `BB_MULT` | 2.0 | Source-reported |
| `MIN_BB_WIDTH_PCT` | 1.0% | Source-reported |
| `VOLUME_LEN` | 20 periods | Source-reported |
| `VOLUME_MULT` | 1.1 | Source-reported |
| `ADX_LEN` | 14 periods | Source-reported |
| `MIN_ADX` | 18.0 | Source-reported |
| `STOP_ATR` | 2.0 | Source-reported |
| `TP_ATR` | 3.5 | Source-reported |
| `TRAIL_ATR` | 999.0 (disabled) | Source-reported |
| `INITIAL_CAPITAL` | $100,000.00 | Source-reported |
| `POSITION_PCT` | 10% of equity per trade | Source-reported |
| `COMMISSION` | 5 bps (0.0005) per side | Source-reported |
| `SLIPPAGE` | 2 bps (0.0002) per side | Source-reported |
| Max holding timeout | 20 bars (80h) | `research-proposed` |
| Perp funding adjustment | Dynamic 8h rate deduction | `research-proposed` |
| Symmetrical spot shorting borrow cost | 5 bps annual borrow fee | `research-proposed` |

## Required data

- **Instruments:** Spot pairs BTC-USD, ETH-USD, SOL-USD.
- **Venue:** Spot crypto feeds (historical snapshots sourced from Yahoo Finance via `yfinance`, frozen with SHA-256 manifests).
- **Timeframe:** 4-hour (4H) primary aggregation; 1-hour (1H) for benchmark baseline.
- **Fields:** `Open`, `High`, `Low`, `Close`, `Volume`.
- **Point-in-time protections:** Strict index monotonic ordering, timezone fixed to UTC, assertion against duplicate timestamps. Features and labels strictly partitioned using causal indexing (`te = i - AHEAD`).
- **Missing-data handling:** Missing volume or indicator warm-up values handled via forward fill or explicit clipping; division-by-zero guards (`max(..., 1e-6)`) enforced.

## Execution assumptions

- **Execution timing:** Signal computed at bar Close; orders executed at next-bar Open (`i+1`).
- **Fill model:** Slippage modeled symmetrically as `Open * (1 + slip)` for long entry / short exit, and `Open * (1 - slip)` for short entry / long exit.
- **Trading fees:** Commission set to 5 bps (0.05%) per order; slippage set to 2 bps (0.02%) per fill (7 bps total friction per one-way trade).
- **Intrabar stops:** Evaluated on bar High/Low; gap openings past stop/take-profit are filled at bar Open.
- **Borrow / Shorting assumption:** Primary source assumed unconstrained symmetrical shorting feasibility on spot crypto assets without dedicated borrow availability or borrow cost modeling. `research-proposed`: In live spot execution, physical spot shorting requires margin lending pools with variable borrow interest rates; alternatively, execution must be routed to perpetual futures contracts with funding rate settlement.
- **Capacity / Impact:** Deploys 10% equity per trade on $100,000 initial capital ($10,000 nominal trade size). Market impact is assumed negligible for this nominal size on major pairs (BTC, ETH, SOL), but would degrade on low-liquidity altcoins.

## Evidence

### Source-reported

All metrics below are drawn directly from the frozen v1.2 datasets and reported across `REPORT.md` and associated result outputs in `darangworks/causal-knn-crypto-strategy` (commit `21b3a98c4cca73c97508f9b1b907fcda15424a0a`).

#### 1. Full-Sample Backtest (BTC-USD 4H, 2024-09-13 to 2026-09-12, 4,333 bars)

| Scenario | Trades | Gross PnL | Net PnL | Win Rate | Profit Factor |
|----------|:------:|:---------:|:-------:|:--------:|:-------------:|
| Zero Cost | 132 | +$4,656.89 | +$4,656.89 | 38.64% | 1.230 |
| Commission Only (5 bps) | 132 | +$4,590.95 | +$3,287.76 | 38.64% | 1.157 |
| Slippage Only (2 bps) | 131 | +$3,860.71 | +$3,342.28 | 38.17% | 1.163 |
| **Full Cost (5 bps comm + 2 bps slip)** | **131** | **+$3,803.16** | **+$2,000.38** | **38.17%** | **1.095** |

- Hourly equity curve Sharpe ratio: Noted by the author as computed on hourly equity curve increments with 10% capital exposure, yielding non-comparable Sharpe values relative to fully-invested benchmarks.

#### 2. Information Coefficient and Quintile Structure (BTC 4H, N = 3,977)

- **Pearson IC:** −0.02800
- **Spearman Rank IC:** −0.02912
- **Directional Accuracy:** 48.63%
- **Autocorrelation (ACF) block length:** 140 bars

Quintile breakdown of model prediction vs. forward return:
| Quintile | Mean Forward Return |
|:--------:|:-------------------:|
| Q1 (Lowest prediction) | +0.0475% |
| Q2 | −0.0134% |
| Q3 | +0.0325% |
| Q4 | −0.0474% |
| Q5 (Highest prediction) | −0.0325% |
| **Q5 − Q1 Spread** | **−0.0800%** |

- **Rank correlation between quintile rank and forward return:** **−0.800** (inverted non-monotonic profile).

#### 3. Walk-Forward Analysis (Single 50/50 Split, BTC 4H)

| Partition | Sample Window | Trades | Net PnL | Return % | Win Rate | Profit Factor | Spearman IC | Directional Acc |
|-----------|---------------|:------:|:-------:|:--------:|:--------:|:-------------:|:-----------:|:---------------:|
| In-Sample (IS) | First 50% | 58 | **−$3,573.68** | −3.57% | 27.59% | 0.682 | −0.05078 (N=1,810) | — |
| Out-of-Sample (OOS) | Second 50% | 57 | **+$4,733.23** | +4.73% | 45.61% | 1.564 | +0.00034 (N=1,811) | 49.75% |

- Engine output diagnosis: `[WARN] IS negative AND OOS positive → possible luck`. The absence of predictive IC (+0.00034) demonstrates that positive OOS PnL reflects regime-specific drift rather than predictive generalization.

#### 4. Chronological Consistency Windows (6 Non-Overlapping Windows, BTC 4H)

Each window re-initializes an empty kNN memory buffer to assess temporal stability:

| Window | Date Range | Trades | Gross PnL | Net PnL | Win Rate | Profit Factor | Spearman IC |
|:------:|------------|:------:|:---------:|:-------:|:--------:|:-------------:|:-----------:|
| 1 | 2024-09-13 → 2025-01-11 | 13 | −$322.00 | −$505.00 | 30.77% | 0.803 | −0.004 |
| 2 | 2025-01-11 → 2025-05-11 | 11 | −$1,867.00 | −$2,019.00 | 18.18% | 0.162 | −0.080 |
| 3 | 2025-05-11 → 2025-09-08 | 10 | +$188.00 | +$48.00 | 40.00% | 1.043 | +0.055 |
| 4 | 2025-09-09 → 2026-01-13 | 14 | −$1,400.00 | −$1,594.00 | 14.29% | 0.470 | +0.028 |
| 5 | 2026-01-13 → 2026-05-14 | 16 | +$204.00 | −$22.00 | 37.50% | 0.991 | −0.068 |
| 6 | 2026-05-14 → 2026-09-12 | 9 | +$1,423.00 | +$1,295.00 | 55.56% | 2.559 | +0.010 |
| **Total** | | **73** | **−$1,774.00** | **−$2,796.00** | — | — | — |

- Positive windows: 2/6 (33.3%).
- Mean net per window: −$466.01, standard deviation $1,204.00, standard error $491.53.
- **t-statistic:** **−0.948** (Verdict: WEAK).

#### 5. Cross-Asset Robustness Check (6 Windows per Asset)

| Asset | Positive Windows | Trades | Total Gross | Total Net | Mean Net/Window | t-statistic | Verdict |
|-------|:----------------:|:------:|:-----------:|:---------:|:---------------:|:-----------:|:-------:|
| BTC-USD | 2/6 | 73 | −$1,774.00 | −$2,796.00 | −$466.01 | −0.948 | WEAK |
| ETH-USD | 3/6 | 75 | +$222.00 | −$834.00 | −$139.00 | −0.381 | WEAK |
| SOL-USD | 2/6 | 82 | −$3,050.00 | −$4,192.00 | −$698.67 | −1.995 | WEAK |

- Overall multi-asset verdict: `[FAIL] No asset shows consistent edge`.

#### 6. Baseline 1H Resolution Performance (BTC-USD 1H, 17,318 bars)

| Metric | Baseline 1H Value |
|--------|------------------:|
| Trades | 628 |
| Net PnL | **−$8,805.86** |
| Net Return | **−8.81%** |
| Profit Factor | 0.776 |
| Win Rate | 32.01% |
| Max Drawdown | −10.44% |
| Sharpe Ratio | −1.64 |

### Independently reproduced

Not independently reproduced. This evaluation is based on source analysis of the public reproduction codebase, frozen manifests, unit tests, and empirical logs published by Mohammad Darang (commit `21b3a98c4cca73c97508f9b1b907fcda15424a0a`).

### Negative evidence

The empirical evidence systematically disconfirms the hypothesis that causal kNN technical pattern matching yields economic alpha in crypto markets:
1. **Unconditional Information Coefficient Failure:** The model displays negative linear correlation (Pearson IC −0.028) and negative monotonic rank correlation (Spearman IC −0.029) with subsequent 2-bar forward returns across 3,977 bars.
2. **Inverted Quintile Monotonicity:** High-conviction bullish predictions (Q5) produce negative forward drift (−0.0325%), while bearish predictions (Q1) produce positive forward drift (+0.0475%), yielding an inverted rank correlation of −0.800.
3. **Temporal Inconsistency:** Across 6 chronological testing windows on BTC 4H, 4 out of 6 windows generate net losses, yielding aggregate losses of −$2,796 and a negative t-statistic of −0.948.
4. **Cross-Asset Fragility:** When applied to ETH-USD and SOL-USD under identical parameters, the strategy yields net losses across all assets (ETH: −$834; SOL: −$4,192; t-stats −0.381 and −1.995 respectively).
5. **Timeframe Breakdown:** Shifting from 4H to 1H execution escalates trading turnover (628 trades) and expands net drawdowns to −8.81% (Sharpe −1.64, PF 0.776).
6. **Ablation Insight:** Pre-freeze ablation studies indicated that disabling the 50 EMA higher timeframe trend filter collapsed gross returns by ~93% (from +$5,537 to +$376), confirming that any apparent profitability stems from trend filtering rather than kNN analog matching.

## Falsification plan

To falsify the negative-result conclusion or establish conditions where kNN pattern matching could be redeemed, the following pre-registered validation gates must be satisfied:

1. **Causal Leakage and Synthetic Oracle Test:**
   - Run the 7-test unit suite (`tests/test_causal_knn_corrected.py`). Under a driftless geometric Brownian motion synthetic series, the strategy must generate zero statistical edge (Sharpe within ±0.15 of zero, IC within 95% binomial null bounds; `research-defined falsification threshold`). If synthetic data generates positive Sharpe, code leakage is established.
2. **Information Coefficient Monotonicity Gate:**
   - Over an out-of-sample test window of at least 2,000 non-overlapping bars, the kNN prediction must demonstrate a positive Spearman rank IC exceeding +0.03 with a t-statistic > 2.0 (`research-defined falsification threshold`), and the top quintile (Q5) forward return must exceed the bottom quintile (Q1).
3. **Chronological Consistency Window Hurdle:**
   - Across at least 6 non-overlapping out-of-sample chronological windows, at least 4 out of 6 windows must produce positive net PnL after full transaction costs, and the cross-window t-statistic must exceed +1.96 (`research-defined falsification threshold`).
4. **Cross-Asset Generalization Gate:**
   - The strategy must achieve positive net expectation and positive Sharpe on at least two liquid altcoin markets (e.g., ETH and SOL) without asset-specific retuning (`research-defined falsification threshold`).
5. **Cost and Slippage Hurdle:**
   - Net profitability must withstand a fee stress test of 10 bps taker commission and 5 bps slippage (15 bps one-way, 30 bps round-trip; `research-defined falsification threshold`). If net PnL collapses below zero under 10 bps one-way friction, the strategy is deemed non-executable.
6. **Signal Component Ablation Test:**
   - Remove the 50 EMA trend filter, Bollinger Band width gate, and ADX indicator. If the isolated kNN signal cannot produce positive excess returns or positive IC independently (`research-defined falsification threshold`), the claim that kNN pattern matching possesses alpha is falsified.

## Crypto portability

- **Portability classification:** `adapted` / `unproven`
- **Portability rationale:** The primary research evaluated crypto spot data (BTC-USD, ETH-USD, SOL-USD from Yahoo Finance). However, porting the system to institutional crypto execution requires adapting to perpetual futures:
  - **Symmetrical Shorting vs. Borrow Friction:** The backtest assumed costless symmetrical short execution on spot. In actual crypto spot markets, shorting requires margin borrowing, introducing borrow interest and collateral liquidation risk.
  - **Perpetual Funding Drag:** In perpetual futures, shorting during strong bull regimes (which coincide with the strategy's profitable periods) incurs substantial negative funding payments, further eroding the narrow gross profit margin.
  - **Liquidation and Mark Price Dynamics:** Intrabar ATR stop losses are vulnerable to wick cascades and exchange-specific mark/index price divergences during high-volatility liquidation events.

## Limitations

- `underspecified`: The primary implementation does not define a maximum holding period timeout; positions rely solely on ATR stops, take profits, or opposite signal reversals.
- `not independently reproduced`: Research claims and logs originate from Mohammad Darang's repository and have not yet been reconstructed inside NautilusTrader or PyBroker.
- `unproven`: All empirical statistical tests confirm the absence of robust predictive edge under the tested causal specification.
- **Multiple Testing Bias:** Approximately 15 exploratory configurations were investigated during the author's preliminary research before fixing the reported parameters.
- **Sample Coverage:** The 2-year frozen dataset (September 2024 to September 2026) covers predominantly ascending market conditions and lacks a sustained multi-year bear market cycle.

## Implementation status

`not-implemented`

No implementation in NautilusTrader, PyBroker, paper trading, testnet, or live trading has been executed.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This document serves as a source-traceable negative result research capture and forensic lookahead-audit reference. It does not constitute a trading recommendation, validated alpha strategy, or authorization for live execution.

## Related Wiki records

- `machine-learning-knn_ohlcv-2026-08-31.md`
- `retrieval-augmented-llm-expert-switching-portfolio-management-2026-09-03.md`
- `crypto-cross-sectional-return-rank-mlp-decay-portfolio-2026-09-03.md`

## Sources

- **Primary Research Codebase:** Mohammad Darang, *Causal Reconstruction and Validation Study of Zeiierman's AI Predictive Flow Indicator as a Trading Strategy*, GitHub repository: https://github.com/darangworks/causal-knn-crypto-strategy (Commit SHA: `21b3a98c4cca73c97508f9b1b907fcda15424a0a`, as-of 2026-09-12).
- **Original Public Script:** Zeiierman, *AI Predictive Flow*, TradingView script URL: https://www.tradingview.com/script/qaaxkW1P-AI-Predictive-Flow-Zeiierman/ (published under CC BY-NC-SA 4.0).
- **Frozen Data Repository:** `darangworks/causal-knn-crypto-strategy/data/MANIFEST.md` (SHA-256 verified snapshots for BTC-USD, ETH-USD, and SOL-USD, 2024-09-13 to 2026-09-12).
