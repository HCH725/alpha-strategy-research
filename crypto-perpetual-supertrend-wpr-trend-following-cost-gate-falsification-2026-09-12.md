---
schema: strategy-research-record-v1
title: "Crypto Perpetual Multi-Timeframe Trend Following: Supertrend, Williams %R, Cost-per-R Friction Gate, and Statistical Ceiling Falsification on Delta Exchange India"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - trend-following
  - supertrend
  - williams-r
  - adx
  - cost-per-r-gate
  - transaction-costs
  - negative-result
  - falsification
  - effective-sample-size
  - multi-timeframe
status: research-only
confidence: high
source_as_of: 2026-09-10
sources:
  - "GitHub repository: yesterdaysrebel/deltabt (commit 8fd85a4b0c2db41cee49c6151aceb186fb78dc3f, docs/strategy.md, deltabt/config.py, deltabt/costs.py, out/htrend/arms.csv, out/hwpr/decision.json, out/summary_parity.json, out/universe_neff.json, published September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Multi-Timeframe Trend Following: Supertrend, Williams %R, Cost-per-R Friction Gate, and Statistical Ceiling Falsification on Delta Exchange India

## Provenance

- **Repository**: `https://github.com/yesterdaysrebel/deltabt`
- **Full Commit SHA**: `8fd85a4b0c2db41cee49c6151aceb186fb78dc3f` (with upstream research PR #51 merge commit `48ef1805a88fa2fc33243b7922396ad8bfd50de2`)
- **Author**: Irfan Paraniya (`yesterdaysrebel`)
- **Publication / Last Commit Date**: 2026-09-07 to 2026-09-10
- **License**: MIT License
- **Exact File Paths**:
  - `README.md`: Overview of the pre-registered negative-result research program, statistical detection ceiling, and six cataloged methodology errors (`source-reported`).
  - `deltabt/config.py`: Configuration dataclasses, Delta Exchange India constants, WPR band-traverse latch rules, and `StrategyParams` specification (`source-reported`).
  - `deltabt/costs.py`: Delta Exchange India cost model, 18% Indian GST multiplier, maker/taker fee schedules, integer contract rounding, snapshot funding logic, and basis-point slippage model (`source-reported`).
  - `deltabt/engine.py`: Event-driven backtesting execution loop with mark-price stop triggers and next-bar evaluation (`source-reported`).
  - `deltabt/indicators.py`: Numba-accelerated, window-invariant Supertrend, DMI, ADX, Williams %R, ATR, and RMA implementations (`source-reported`).
  - `deltabt/research/run_hwpr.py`: Frozen experiment driver for H-WPR-1 (Williams %R pullback overlay) (`source-reported`).
  - `deltabt/research/run_htrend.py`: Frozen experiment driver for H-TREND-1 (multi-timeframe trend alignment ablation) (`source-reported`).
  - `deltabt/research/stats.py`: Time-series-aware inference, Politis-Romano stationary block bootstrap, participation ratio, trade design effect, and cluster-adjusted t-statistics (`source-reported`).
  - `docs/strategy.md`: Frozen specification for H-WPR-1 Variant A, timeframe inversion rationale, and leg-extreme truncation bounds (`source-reported`).
  - `docs/v5_stopping_rule.md`: Pre-registered stopping rule and statistical resolution power boundaries (`source-reported`).
  - `out/summary_parity.json`: Exact output from Pine script parity run across BTCUSD, ETHUSD, SOLUSD, and XRPUSD (`source-reported`).
  - `out/universe_neff.json`: Cross-sectional return correlation, participation ratio ($PR$), and design effect ($DEFF$) output for the 4 majors (`source-reported`).
  - `out/htrend/arms.csv` & `out/htrend/decision.json`: Tabular metrics and formal `NO SIGNAL` verdict across all four trend ablation arms (`source-reported`).
  - `out/hwpr/decision.json`: Formal `NO ECONOMIC EDGE` verdict for the Williams %R pullback family (`source-reported`).
  - `out/walkforward.csv`: Out-of-sample rolling walk-forward fold evaluations (`source-reported`).
- **Primary Source Data Span**: 2024-01-23 to 2026-08-11 (1,331,315 1-minute OHLCV candles, matching mark-price series, and 1-hour funding rates on Delta Exchange India for BTCUSD, ETHUSD, SOLUSD, and XRPUSD) (`source-reported`).

## Economic mechanism

### Source-reported

The underlying retail strategy posits a multi-timeframe directional momentum and mean-reversion pullback hypothesis on cryptocurrency perpetual futures:
1. **Regime and Directional Alignment**: A higher-timeframe trend filter (e.g., 5-minute or 1-hour) establishes directional bias using the Supertrend indicator (ATR-based volatility band) confirmed by the Average Directional Index (ADX) and Directional Movement Index (+DI / -DI). When price resides above the Supertrend line and ADX reflects strong trend strength ($\text{ADX} \ge 25$ with $+\text{DI} > -\text{DI}$), directional momentum is hypothesized to persist.
2. **Intrabar / Lower-Timeframe Pullback Entry**: Rather than buying market highs, the strategy seeks short-term oversold conditions within the macro uptrend using Williams %R (e.g., WPR(140) crossing or rising from below -80), attempting to capture institutional trend continuation at discounted local prices.
3. **Volatility-Scaled Risk / Reward**: Exits are anchored to the structural Supertrend band or trailing swing extreme, setting a take-profit target at a fixed 2.0R reward-to-risk ratio.

### Research interpretation

This repository represents an exhaustive empirical and econometric falsification study of indicator-based retail trend-following systems on cryptocurrency perpetual futures. The primary contribution of the research program is demonstrating that the apparent profitability of popular Pine Script indicator combinations (Supertrend + ADX + Williams %R) collapses under rigorous friction modeling, cross-asset correlation accounting, and multiple-testing corrections:

1. **The Cost-per-R Friction Barrier**: The foundational economic breakdown occurs at the transaction-cost boundary. On lower timeframes (1-minute and 5-minute), ATR-derived stop-loss distances ($R$) are physically compressed into 8 to 22 basis points. However, exchange taker fees (5.0 bps nominal $\times$ 1.18 GST = 5.9 bps per side $\rightarrow$ 11.8 bps round-trip on Delta Exchange India) combined with realistic execution slippage (2.0 bps per leg $\rightarrow$ 4.0 bps round-trip) impose a fixed round-trip cost hurdle of 15.8 bps. As a result, friction consumes 0.40R to 1.82R per trade. This mechanical friction moves the required break-even win rate for a 2.0R target from the theoretical 33.3% to over 53.3%, destroying gross edge before any signal evaluates.
2. **Mutual Exclusion Construction Flaw**: In the original TradingView Pine script implementation, the long entry requires the full trend stack (Supertrend bullish, ADX rising) *and* WPR(140) < -80. Empirical inspection reveals that conditioned on a verified uptrend stack, the probability of WPR(140) falling below -80 is $P(\text{WPR} < -80) = 0.00003$, with a median WPR of -9.9. The oversold condition and the trend-following condition are near-mutually exclusive by construction, generating only 11 trades across 4 instruments in 2.5 years.
3. **Statistical Sample Size Illusion**: On higher timeframes (4-hour to 1-day) where stop distance $R$ widens and cost-per-R falls to acceptable levels (0.026R), trade frequency collapses. Because crypto majors (BTC, ETH, SOL, XRP) share a mean pairwise return correlation of $\bar{\rho} = 0.733$ and the first principal component (PC1) explains 80.09% of total variance, the 4 assets represent only $PR = 1.52$ independent degrees of freedom. At trade level, simultaneous position overlap is 91.6%, creating a design effect of $DEFF = 2.22$. A nominal sample of 137 trades across 4 majors contains only 62 effective independent observations ($N_{\text{eff}} = 62$).
4. **The Detection Ceiling**: Testing 72 parameter configurations across correlated time-series creates an effective number of multiple trials $M_{\text{eff}} \approx 37 \text{ to } 149$. Clearing statistical significance after multiple testing requires a t-statistic $t \ge 3.2$. However, since $t = \text{Sharpe} \times \sqrt{T}$, a legitimate Sharpe 1.0 strategy over a 2.55-year history can produce a maximum t-statistic of only $1.0 \times \sqrt{2.55} = 1.60$. Hence, the statistical bar sits above the empirical ceiling.

## Signal

The research documents two primary implementations: the as-written Pine script (`parity` mode) and the pre-registered corrected research architecture (`corrected` mode).

### 1. Pine Script Parity Architecture (`mode = parity`)

- **Formation & Execution**: Evaluated on closed 1-minute bars; order placed on next bar.
- **Long Entry Conditions** (all must be True simultaneously) (`source-reported`):
  1. `close > supertrend` (where Supertrend ATR period = 10, multiplier factor = 2.0).
  2. `direction < 0` (Pine script convention for bullish Supertrend).
  3. `ADX >= 25` (computed with DI period = 14, ADX smoothing = 14).
  4. `+DI > -DI`.
  5. `Williams %R(140) < -80.0` (evaluated on current closed bar).
  6. `Williams %R(140) > Williams %R[1]` (rising %R).
- **Short Entry Conditions**: Exact mirror opposite (`source-reported`).
- **Stop-Loss**: Level of the Supertrend line at entry bar (`source-reported`).
- **Take-Profit**: Entry $\pm 2.0 \times |\text{entry} - \text{stop}|$ (`reward_risk = 2.0`) (`source-reported`).
- **Defects identified in source audit**: Level-triggered signals with zero cooldown produce immediate re-entries on consecutive bars; position sizing has no leverage cap; WPR condition is near-mutually exclusive with the trend filter (`source-reported`).

### 2. Pre-Registered Corrected Architecture (`mode = corrected`, H-WPR-1 and H-TREND-1)

- **Grid Resolution**: Primary signal evaluated on 5-minute closed bars; trend confirmation evaluated on 1-minute closed bars (or primary on 1m with 5m confirmation in earlier research arms) (`source-reported`).
- **Lookback Windows**:
  - Supertrend: ATR period = 10, multiplier factor = 2.0 (`source-reported`).
  - DMI / ADX: DI length = 14, Wilder smoothing period = 28 (`source-reported`).
  - Williams %R: Lookback length = 140 bars (in H-WPR-1) or omitted (in H-TREND-1) (`source-reported`).
  - Warmup requirement: $N_{\text{warmup}} \ge \text{di\_length} + 2 \times \text{adx\_smoothing} = 70$ bars (`source-reported`).
- **Long Entry Conditions (H-WPR-1 Variant A)** (`source-reported`):
  1. Primary bar (5m): Bullish Supertrend (`direction < 0`).
  2. Primary bar (5m): $\text{ADX} \ge 25$ and $+\text{DI} > -\text{DI}$.
  3. Primary bar (5m): $\text{WPR}(140) > -80.0$ and $\text{WPR}_t > \text{WPR}_{t-1}$ (rising out of oversold zone).
  4. Confirmation bar (1m): Bullish Supertrend (`direction < 0`).
  5. Confirmation bar (1m): $\text{ADX} \ge 25$ and $+\text{DI} > -\text{DI}$.
  6. Edge Trigger & Cooldown: Must be a fresh trigger (`edge_trigger = True`); cooldown of $\ge 10$ bars flat before re-arming (`cooldown_bars = 10`) (`source-reported`).
  7. **Cost-per-R Gate**: Expected round-trip fee + slippage must not exceed 15% of stop distance $R$ (`max_cost_per_r = 0.15`) (`source-reported`).
- **Short Entry Conditions**: Exact symmetrical mirror (`source-reported`).
- **Structural Stop-Loss**:
  $$\text{Stop}_{\text{long}} = \min(\text{lowest low since Supertrend flipped bullish}, \text{Supertrend})$$
  $$\text{Stop}_{\text{short}} = \max(\text{highest high since Supertrend flipped bearish}, \text{Supertrend})$$
  Floored by minimum distance: $\ge 0.5 \times \text{ATR}(10)$ and $\ge 10$ ticks; capped at maximum 5% distance from entry (`source-reported`).
- **Take-Profit Target**: $\text{Entry} \pm 2.0 \times |\text{entry} - \text{stop}|$ (`reward_risk = 2.0`) (`source-reported`).
- **Exits & Precedence** (`source-reported`):
  1. *Resting Stop / Target*: Checked against high/low of incoming bar (evaluated pessimistically: if both hit in same bar, stop takes precedence).
  2. *Adverse Trend Flip*: If Supertrend flips direction before stop/target hit (`exit_on_trend_flip = True`).
  3. *Maximum Holding Time*: 240 bars (`max_hold_bars = 240`).

### Operational parameters classification

| Parameter | Value | Provenance Classification | Notes |
|:---|:---|:---|:---|
| `base_minutes` | 1m or 5m | source-reported | Primary candle timeframe |
| `confirm_minutes` | 5m or 1m | source-reported | Confirmation candle timeframe |
| `st_atr_period` | 10 | source-reported | Supertrend ATR lookback |
| `st_factor` | 2.0 (swept 2.0 to 12.0) | source-reported | Supertrend ATR multiplier |
| `di_length` | 14 | source-reported | DMI period |
| `adx_smoothing` | 28 (14 in Pine parity) | source-reported | Wilder smoothing of DX |
| `adx_threshold` | 25.0 | source-reported | Minimum trend strength filter |
| `wpr_length` | 140 (swept 14 to 140) | source-reported | Williams %R lookback period |
| `wpr_fire_long` | -80.0 | source-reported | Oversold recovery trigger |
| `reward_risk` | 2.0 (2.0R) | source-reported | Take-profit multiple |
| `max_cost_per_r` | 0.15 (15% of R) | source-reported | Friction rejection gate |
| `risk_percent` | 0.5% equity | source-reported | Risk budget per trade |
| `max_leverage` | 3.0x | source-reported | Maximum allowable leverage |
| `cooldown_bars` | 10 bars | source-reported | Re-entry suppression window |
| `max_hold_bars` | 240 bars | source-reported | Time-based exit limit |
| `GST_MULTIPLIER` | 1.18 (+18%) | source-reported | Indian Goods & Services Tax on fees |
| `slippage_bps` | 2.0 bps per leg (4.0 bps RT) | source-reported | Modelled execution slippage |
| Fill execution | Next-bar open fill | research-proposed | Standard causal event loop assumption |
| Benchmark comparison | Exposure-matched random entry | source-reported | 2,000 simulated random control paths |
| Detection threshold | $t \ge 3.2$ | source-reported | Multi-testing corrected significance |

## Required data

- **Instruments**: Cryptocurrency perpetual futures on Delta Exchange India (`BTCUSD`, `ETHUSD`, `SOLUSD`, `XRPUSD`).
- **Timeframe & Candles**:
  - 1-minute OHLCV candles (`timestamp`, `open`, `high`, `low`, `close`, `volume`).
  - Primary data set: 1,331,315 1m bars from 2024-01-23 to 2026-08-11 (`source-reported`).
- **Order Book & Mark Price Series**:
  - Independent 1-minute mark price series (`SERIES_MARK = "MARK:"`).
  - Essential because Delta Exchange India triggers stop-loss orders against mark price rather than last-traded price (LTP) (`source-reported`).
- **Historical Funding Rates**:
  - 1-hour funding rate snapshots (`SERIES_FUNDING = "FUNDING:"`).
  - Delta Exchange settles funding on snapshot schedules (every 4 or 8 hours depending on instrument), not continuous pro-rata (`source-reported`).
- **Data Hygiene and Quality Filters** (`source-reported`):
  - *Synthetic Bar Filter*: Delta Exchange forward-fills illiquid periods with zero-volume synthetic bars. Any symbol where synthetic bars exceed 5% of history (`MAX_SYNTHETIC_RATIO = 0.05`) is disqualified.
  - *Halt Detection*: Runs of identical $O=H=L=C$ bars with zero volume lasting $\ge 20$ bars (`HALT_MIN_RUN_BARS = 20`) are classified as maintenance halts. Stop triggers are suppressed during halts.
  - *History Length*: Minimum 180 usable days (`MIN_USABLE_DAYS = 180`).

## Execution assumptions

- **Exchange Venue**: Delta Exchange India (`https://api.india.delta.exchange`) (`source-reported`).
- **Fee Structure**:
  - Base maker/taker commission on crypto perpetuals: 0.02% / 0.05% (`source-reported`).
  - Statutory 18% Indian GST applied to all fees: effective taker fee = $0.05\% \times 1.18 = 0.059\%$ per leg ($0.118\%$ round-trip) (`source-reported`).
- **Execution Slippage**: Modeled at 2.0 basis points per leg (4.0 bps round-trip notional), deliberately specified in basis points rather than ticks to avoid cross-symbol pricing artifacts (`source-reported`).
- **Total Round-Trip Friction**:
  $$\text{Friction}_{\text{round-trip}} = 2 \times 0.059\% + 2 \times 0.02\% = 0.158\% \quad (15.8 \text{ bps})$$
- **Contract Quantisation**: Order sizes are constrained to integer contracts (`contract_value`). For high-notional contracts (e.g., SOLUSD where 1 contract $\approx \$76$ notional), integer truncation materially restricts sizing on small accounts (`source-reported`).
- **Margin & Leverage**: Position sizing dynamically scaled by stop distance, subject to a hard leverage cap of $3.0\times$ (`max_leverage = 3.0`) and minimum stop floor of 10 ticks (`source-reported`).

## Evidence

### Source-reported

All quantitative figures below trace directly to official research outputs in repository `yesterdaysrebel/deltabt` (commit `8fd85a4b0c2db41cee49c6151aceb186fb78dc3f`), specifically `out/summary_parity.json`, `out/htrend/arms.csv`, `out/htrend/decision.json`, `out/hwpr/decision.json`, `out/universe_neff.json`, and `README.md`:

#### 1. Pine Script Parity Reproduction (1m Candles, 2024-01-23 to 2026-08-11)

The exact TradingView Pine script logic was executed across 1,331,315 bars per symbol:

| Symbol | Trades | Win Rate | Expectancy $E[R]$ | 95% Bootstrap CI | Total PnL ($) | Max Drawdown | Avg Cost / R | Median $R$ (bps) | Total Fees ($) |
|:---|---:|---:|---:|:---|---:|---:|---:|---:|---:|
| `BTCUSD` | 5 | 40.0% | -2.312R | [-6.530, +0.773] | -$575.92 | 6.51% | 2.67R | 9.7 bps | $625.67 |
| `ETHUSD` | 3 | 66.7% | +0.008R | [-1.813, +1.122] | +$0.55 | 0.91% | 1.40R | 11.5 bps | $150.98 |
| `SOLUSD` | 2 | 50.0% | -0.703R | [-2.259, +0.852] | -$70.75 | 1.56% | 1.51R | 10.7 bps | $119.48 |
| `XRPUSD` | 1 | 100.0% | +1.139R | [+1.139, +1.139] | +$56.93 | 0.34% | 1.37R | 11.5 bps | $44.45 |
| **Combined** | **11** | **45.5%** | **-0.967R** | **Uninterpretable** | **-$589.19** | **6.51%** | **1.74R** | **10.9 bps** | **$940.58** |

*Finding*: The parity check confirmed that the published TradingView strategy produced only 11 trades in 2.5 years (effectively zero, matching the original Pine tester result) due to the structural mutual exclusion of the trend stack and WPR oversold conditions.

#### 2. Timeframe vs Stop Distance Scaling and Cost Drag

Evaluating the strategy across candle timeframes with ST(10, 3.0) and cost-per-R gating:

| Base Timeframe | Trades | Win Rate | Expectancy $E[R]$ | 95% Bootstrap CI | Cost / $R$ | Median $R$ (bps) | Break-even Win Rate |
|:---|---:|---:|---:|:---|---:|---:|---:|
| **1m** | 56 | 28.6% | -0.243R | [-0.479, +0.021] | 0.123R | 122 bps | 36.1% |
| **5m** | 367 | 34.6% | -0.077R | [-0.182, +0.031] | 0.118R | 131 bps | 35.9% |
| **15m** | 401 | 32.4% | -0.078R | [-0.181, +0.027] | 0.107R | 143 bps | 35.6% |
| **1h** | 180 | 31.1% | -0.049R | [-0.213, +0.134] | 0.077R | 218 bps | 34.9% |

*Finding*: On 1m bars without filtering, Supertrend(10, 2.0) stop distance is 8.7 bps, yielding a cost-to-R ratio of 1.82R (cost exceeds planned risk by 82%). Even at factor 12.0, cost is 0.38R. When the timeframe is widened to 1h to dilute costs, win rates sit at the 33.3% random break-even level, and every 95% confidence interval straddles zero.

#### 3. Pre-Registered H-TREND-1 Trend Alignment Ablation

Evaluated over locked Train (60%) and Validation (20%) windows across the 4 majors:

| Arm Description | Split | Trades | Eff. $N$ | Win % | Gross $E[R]$ | Total Cost | Net $E[R]$ | $t_{\text{gross}}$ | $t_{\text{net}}$ | Verdict |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|:---|
| **Arm A**: 5m regime + 1m ST + 1m ADX/DI | Train | 4,439 | 2,493.1 | 34.5% | +0.0577R | 0.4028R | -0.3452R | +2.114 | -9.08 | **NO SIGNAL** |
| **Arm A**: 5m regime + 1m ST + 1m ADX/DI | Valid | 1,530 | 608.6 | 31.0% | **-0.0431R** | 0.4198R | -0.4629R | **-0.768** | -6.08 | (Validation gross $\le 0$) |
| **Arm B**: 5m regime only | Train | 9,209 | 5,886.4 | 23.4% | +0.0177R | 5.0391R | -5.0214R | +0.952 | -14.48 | **NO SIGNAL** |
| **Arm B**: 5m regime only | Valid | 294 | 139.2 | 15.6% | -0.2245R | 4.9017R | -5.1262R | -1.746 | -5.78 | Gross negative |
| **Arm C**: 5m regime + 1m ST | Train | 6,073 | 3,272.5 | 33.6% | +0.0339R | 0.5154R | -0.4815R | +1.344 | -13.00 | **NO SIGNAL** |
| **Arm C**: 5m regime + 1m ST | Valid | 2,737 | 979.8 | 31.4% | -0.0124R | 0.6400R | -0.6524R | -0.281 | -9.84 | Gross negative |
| **Arm D**: 5m regime + 1m ADX/DI | Train | 5,487 | 5,014.5 | 31.8% | +0.0443R | 1.8044R | -1.7601R | +2.312 | -8.38 | **NO SIGNAL** |
| **Arm D**: 5m regime + 1m ADX/DI | Valid | 2,236 | 1,487.4 | 25.5% | -0.0689R | 3.4326R | -3.5015R | -1.917 | -6.47 | Gross negative |

#### 4. Pre-Registered H-WPR-1 Williams %R Pullback Experiment

- **Train Split**: 4,356 trades, effective $N = 2,671.5$, win rate 33.98%, gross expectancy $+0.0317\text{R}$ ($t_{\text{gross}} = 1.198$), fees $0.2856\text{R}$, slippage $0.0968\text{R}$, net expectancy $-0.3510\text{R}$ ($t_{\text{net}} = -9.569$).
- **Validation Split**: 1,504 trades, effective $N = 668.1$, win rate 30.72%, gross expectancy **$-0.0505\text{R}$** ($t_{\text{gross}} = -0.944$), net expectancy $-0.4583\text{R}$ ($t_{\text{net}} = -6.477$).
- **Official Program Verdict**: **`NO ECONOMIC EDGE`** (gross expectancy is negative on validation; transaction costs exceed gross expectancy by 12x in training).

#### 5. Cross-Asset Correlation and Statistical Detection Ceiling

- **Eigenvalue Decomposition of 4 Majors** (`out/universe_neff.json`):
  - Common sample: 853.7 days (2024-01-23 to 2026-08-11).
  - Mean pairwise correlation: $\bar{\rho} = 0.7326$.
  - First Principal Component (PC1): explains **80.09%** of variance.
  - Participation Ratio: $PR = 1.523$ effective instruments.
  - Trade-level design effect: $DEFF = 2.22$ (mean cross-trade correlation 0.434; simultaneous position hold 91.6%).
  - Effective swing sample size: 137 nominal 4h trades $\rightarrow$ **62 effective independent observations**.
- **Overlapping Window Serial Correlation Inflation**:
  - Naive OLS overlapping panel t-statistic: $+4.54$.
  - Driscoll-Kraay robust panel t-statistic: $+0.59$.
  - Cluster-adjusted discrete trade t-statistic: $+0.57$.
  - Inflation factor: Naive t is inflated **7.7x to 11x** by overlapping serial correlation.
- **Random Entry Benchmark Comparison**:
  - 2,000 exposure-matched random-entry simulations on BTCUSD (matched on trade count, holding period, and transaction fees).
  - Random long-only entries: earned **$+0.0997\text{R}$**.
  - Supertrend strategy entries: earned **$+0.0933\text{R}$**.
  - Trend-following system underperformed passive random market drift by $0.0064\text{R}$.
- **Multiple Testing Eigenspectrum & Detection Ceiling**:
  - 72-cell grid PnL correlation matrix has mean correlation 0.63, collapsing to $M_{\text{eff}} \approx 37 \text{ to } 149$ independent trials.
  - Bonferroni / Sidak multiple-testing significance hurdle: **$t \ge 3.2$**.
  - Maximum t-statistic achievable by a true Sharpe 1.0 strategy over 2.55 years:
    $$t_{\max} = 1.0 \times \sqrt{2.55} = 1.60$$
  - Minimum detectable Sharpe ratio at 80% power: **$\text{Sharpe} \ge 2.53$**.
- **Non-Gaussian Null Bootstrap**:
  - Empirical trade return distribution exhibits skewness of **14.3** and kurtosis of **272**.
  - Stationary bootstrap of demeaned null: $P(|t| > 1.96) = 14.0\%$ (vs. 5.0% theoretical Gaussian), invalidating unadjusted t-tests.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The entirety of this study constitutes conclusive negative empirical evidence against retail indicator-based crypto trend following:
1. **Gross edge is zero or negative out-of-sample**: Across all four trend ablation arms and the Williams %R pullback family, out-of-sample validation gross expectancies are uniformly negative ($-0.0124\text{R}$ to $-0.2245\text{R}$).
2. **Transaction costs are fatal on intraday bars**: Round-trip transaction costs on Delta Exchange India (15.8 bps taker) consume 40% to 182% of the planned stop distance $R$ on 1m and 5m bars, guaranteeing capital depletion even under positive gross expectancy.
3. **Williams %R actively destroys performance**: Adding WPR(140) to the 15m trend system reduced trade count from 401 to 57 (-86%) while degrading net expectancy from $-0.078\text{R}$ to $-0.212\text{R}$.
4. **Apparent in-sample edge is passive drift**: The Supertrend system underperformed a matched random-entry null on BTCUSD ($+0.0933\text{R}$ vs $+0.0997\text{R}$).
5. **Look-ahead bug forensic demonstration**: The codebase documents that an uncorrected same-bar look-ahead bug previously manufactured a spurious $+0.482\text{R}$ edge ($t=32$) before correction.

## Falsification plan

The following falsification protocols establish explicit empirical hurdles required for any counter-claim that indicator trend-following carries genuine alpha on crypto perpetuals:

1. **Exchange Fee / Maker Execution Stress Test**:
   - *Protocol*: Model execution under pure maker fee schedules (e.g., Binance VIP tiers at 1.0 bps maker or zero maker on select pairs) with a verified limit order fill model.
   - *Falsification threshold*: If net expectancy remains below $+0.05\text{R}$ or gross expectancy remains negative on out-of-sample validation periods, confirming that fee reduction alone cannot convert a zero-signal system into positive alpha (`research-defined falsification threshold`).
2. **Effective Degrees of Freedom Stress ($N_{\text{eff}}$)**:
   - *Protocol*: Evaluate the strategy on an expanded universe of 50 altcoin perpetuals, calculating the empirical correlation matrix and participation ratio $PR$.
   - *Falsification threshold*: If $PR / K < 0.20$ (indicating that altcoin returns remain dominated by a single market factor) and cluster-adjusted $t$-statistic fails to clear $t \ge 3.2$ (`research-defined falsification threshold`).
3. **Random Entry Null Superiority**:
   - *Protocol*: Generate 5,000 exposure-matched random entry iterations across the exact trading timestamps and durations.
   - *Falsification threshold*: If the strategy's gross return fails to exceed the 95th percentile of the random entry null distribution ($p > 0.05$) (`research-defined falsification threshold`).
4. **Structural Stop-Loss Window Invariance Audit**:
   - *Protocol*: Recompute the structural Supertrend stop across varying historical buffer windows ($W \in [500, 3000]$ bars).
   - *Falsification threshold*: If stop-loss distance fluctuates by $> 20\%$ due to truncation of unconfirmed Supertrend flip legs (`research-defined falsification threshold`).

## Crypto portability

**Direct** (tested natively on cryptocurrency perpetual futures).

The research was conceptualized, implemented, and executed directly on real cryptocurrency perpetual futures contracts on Delta Exchange India (`BTCUSD`, `ETHUSD`, `SOLUSD`, `XRPUSD`):
- **Continuous 24/7 Liquidity**: Tested on over 1.33 million consecutive 1-minute bars without market close auction interruptions.
- **Microstructure Idiosyncrasies Modeled**:
  - *Mark-Price Stop Triggers*: Stops triggered on mark price, eliminating stop-hunting slippage artifacts seen in LTP-only backtests.
  - *Funding Cashflows*: Snapshot funding payments incorporated based on instrument-specific 4-hour and 8-hour settlement intervals.
  - *Synthetic Bar Contamination*: Forward-filled zero-volume candles explicitly flagged and filtered.
  - *Jurisdictional Taxation*: Indian Goods & Services Tax (18% GST) directly applied to trading fees.
- **Portability to Other Crypto Venues (Binance, Bybit, Hyperliquid)**:
  - *Adapted / Unproven*: While Delta Exchange charges 5.9 bps taker fees with GST, venues like Binance or Bybit charge 4.0 to 5.0 bps taker without GST, and Hyperliquid offers lower taker fees. However, because gross expectancy was negative on validation ($-0.0431\text{R}$), lowering fees merely slows the rate of drawdown rather than creating alpha.

## Limitations

- **Complete Absence of Alpha**: The primary strategy family exhibits zero positive gross expectancy out-of-sample; it is a textbook retail overfitting artifact.
- **Severe Multiple-Testing Degradation**: Sweeping 72 parameter configurations over 2.5 years of crypto history inflates false discoveries; no configuration clears the required $t \ge 3.2$ hurdle.
- **Cross-Asset Redundancy**: Testing across BTC, ETH, SOL, and XRP provides only 1.5 effective independent instruments due to extreme cross-asset correlation ($\bar{\rho} = 0.733$).
- **Lack of Sub-Minute Execution Data**: Ambiguous bars (where both stop and target fall inside a single 1-minute candle) cannot be definitively resolved without tick-level order book history; pessimistic resolution was enforced.
- **Absence of Limit Order Fill Dynamics**: The backtest models market taker orders; simulating maker limit orders requires queue position modeling that was not available in historical 1-minute data.

## Implementation status

not-implemented

This document represents external research normalization of an open-source empirical falsification repository. No strategy implementation in NautilusTrader, PyBroker, paper trading, testnet, or live trading has been performed.

## Adoption boundary

This record is research material only. It does not constitute:
- Evidence of live profitability (it is an explicit negative result and falsification capture)
- Validated alpha ready for capital allocation
- Approval for NautilusTrader or PyBroker production implementation
- Authorization for paper trading, testnet execution, or live deployment

Any future quant research attempting to deploy Supertrend, ADX, or Williams %R indicator combinations on cryptocurrency perpetuals must first demonstrate that the proposed system clears the Cost-per-R gate ($\text{cost} \le 0.15R$) and surpasses the Driscoll-Kraay cluster-adjusted multiple-testing ceiling ($t \ge 3.2$).

## Related Wiki records

- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]` — empirical falsification of retail three-gate indicator combinations.
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` — forensic audit and falsification of retail order-flow CVD and funding patterns.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — canonical validation rules for preventing serial correlation and look-ahead leakage.
- `[[quant/crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12]]` — empirical walk-forward validation and friction modeling on Binance perpetual futures.
- `[[quant/statistical-arbitrage-methodology-degradation-ladder-falsification-2026-09-12]]` — methodology breakdown and forensic accounting of statistical arbitrage edge decay.

## Sources

1. **Primary Codebase Repository**: Irfan Paraniya (`yesterdaysrebel`), *deltabt: Backtesting and pre-registered strategy research for Delta Exchange India perpetual futures*, public GitHub repository `yesterdaysrebel/deltabt`, commit `8fd85a4b0c2db41cee49c6151aceb186fb78dc3f` (with upstream research PR #51 merge commit `48ef1805a88fa2fc33243b7922396ad8bfd50de2`), published September 2026. Stable URL: `https://github.com/yesterdaysrebel/deltabt`.
2. **Strategy Specification Document**: `docs/strategy.md` in repository `yesterdaysrebel/deltabt`, commit `8fd85a4b0c2db41cee49c6151aceb186fb78dc3f`.
3. **Stopping Rule & Power Calculations**: `docs/v5_stopping_rule.md` and `docs/v3_stopping_rule.md` in repository `yesterdaysrebel/deltabt`.
4. **Cost Model & Tax Specifications**: `deltabt/costs.py` and `deltabt/config.py` in repository `yesterdaysrebel/deltabt`.
5. **Statistical Methodology & Inference**: `deltabt/research/stats.py` in repository `yesterdaysrebel/deltabt`.
6. **Empirical Results Files**:
   - `out/summary_parity.json` (Pine script parity backtest output across BTCUSD, ETHUSD, SOLUSD, XRPUSD).
   - `out/universe_neff.json` (Eigenvalue decomposition, participation ratio, and design effect calculations).
   - `out/htrend/arms.csv` & `out/htrend/decision.json` (Tabular results and official `NO SIGNAL` verdict for H-TREND-1).
   - `out/hwpr/decision.json` & `out/wpr_curve.csv` (Official `NO ECONOMIC EDGE` verdict and WPR parameter curve).
   - `out/walkforward.csv` (Walk-forward out-of-sample rolling fold results).
7. **Exchange API Source**: Delta Exchange India public API specification (`https://api.india.delta.exchange`).
8. **Methodology & Data As-Of Date**: 2026-09-10.
