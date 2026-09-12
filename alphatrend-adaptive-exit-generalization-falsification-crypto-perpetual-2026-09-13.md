---
schema: strategy-research-record-v1
title: "AlphaTrend Adaptive Exit Generalization Limits and Cost Falsification in Crypto Perpetuals"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - alphatrend
  - trend-following
  - adaptive-exits
  - machine-learning
  - negative-result
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "https://github.com/wizcap/alphatrend-generalization-study (commit 9d604eb6ffc0e1392692e90d0a0e61b611ed51c8, 2026-09-11)"
  - "wizcap, 'Generalization Limits of Adaptive AlphaTrend Exit Models in Cryptocurrency Futures', Research Preprint v1.0.0, 2026-09-11. URL: https://github.com/wizcap/alphatrend-generalization-study/blob/main/paper/manuscript.md"
  - "KivancOzbilgic, 'AlphaTrend Strategy', TradingView open-source Pine script (Mozilla Public License 2.0), retrieved 2026-09-11. URL: https://www.tradingview.com/script/3wdQu7P3-AlphaTrend-Strategy/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AlphaTrend Adaptive Exit Generalization Limits and Cost Falsification in Crypto Perpetuals

## Provenance

- **Primary Repository:** `https://github.com/wizcap/alphatrend-generalization-study`
- **Full Commit SHA:** `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (main branch as of September 11, 2026)
- **Primary Research Manuscript:** wizcap (NEATTRADE project), *"Generalization Limits of Adaptive AlphaTrend Exit Models in Cryptocurrency Futures"*, Research Preprint version 1.0.0, dated September 11, 2026. File path: `paper/manuscript.md`.
- **Underlying Rule-Based Strategy:** KivancOzbilgic, *"AlphaTrend Strategy"*, TradingView open-source Pine strategy v5 under Mozilla Public License 2.0. Canonical URL: [https://www.tradingview.com/script/3wdQu7P3-AlphaTrend-Strategy/](https://www.tradingview.com/script/3wdQu7P3-AlphaTrend-Strategy/). Pinned script SHA-256: `0e9f04404ca0e414a6509ae3db278906efb661742dfa10112790e022b8e4e40d`.
- **License Status:** Repository research code under Mozilla Public License 2.0 (`LICENSE`, `NOTICE.md`). Manuscript and research figures under Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Direct Primary Source Inspection:** Full inspection of repository source files and frozen experimental artifacts:
  - AlphaTrend indicator implementation: `neattrade/alphatrend.py`
  - Exit policy execution engine and model specifications: `neattrade/generalize_v15.py`
  - Feature extraction and causal checkpoint logic: `neattrade/repair_v12.py`
  - Native multi-timeframe indicators and volatility scaling: `neattrade/indicators_v11.py`
  - Pinned protocol specification: `evidence/study015/study015_method.md`
  - Comprehensive empirical results and contrast intervals: `evidence/study015/report.json`
  - Computational audit and verification record: `evidence/study015/verification.json`
  - Public verification suite: `PUBLIC_MANIFEST.json` (355 checksummed raw market data archives, 704 newly fitted model files, 64 cached reference models, and 720 asset account replays).
- **Repository Deduplication Audit:** Full text regex search across all existing records in `alpha-strategy-research` confirmed zero prior records citing `alphatrend-generalization-study`, `wizcap`, `study015`, or `KivancOzbilgic`. Adjacent trend-following and crypto perpetual records (`crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12.md`, `crypto-residual-momentum-market-beta-neutralization-2026-09-11.md`) examine Supertrend/Williams %R indicators and cross-sectional beta-neutral momentum; none address supervised adaptive exit interventions on AlphaTrend trend-following states under walk-forward circular-block bootstrap validation.

## Economic mechanism

### Source-reported

Trend-following strategies such as AlphaTrend exploit persistent directional momentum in liquid assets by using dynamic bands based on Average True Range (ATR) and Money Flow Index (MFI) to capture trend continuation while trailing stops behind favorable price action. However, in cryptocurrency perpetual futures markets, standard trend-following systems suffer substantial drawdowns during choppy, mean-reverting, or volatile consolidation regimes, and incur continuous negative funding carry when market positioning is crowded. The author investigates whether a supervised machine learning model evaluating active trades at a single fixed checkpoint (24 hours after entry) can forecast the incremental continuation payoff of holding the trade to its natural AlphaTrend exit versus terminating the position early. The author tests whether reducing model complexity, adding robust label preprocessing, aggregating predictions across historical training horizons, enforcing unanimous agreement, or transferring models across assets can improve generalization and eliminate overfitting.

### Research interpretation

The strategy decomposes into a two-component hybrid architecture:
1. **Regime & Entry Engine (Rule-Based Base Signal):** The standard AlphaTrend indicator (14-period ATR multiplier 1.0, combined with 14-period MFI momentum threshold at 50) triggers long-only trend-following entries upon positive line crossovers.
2. **Supervised Adaptive Exit Gate (ML Policy Intervention):** At exactly $T_{\text{entry}} + 24\text{h}$, an empirical classifier or regressor evaluates the position's real-time state (distance from AlphaTrend line, trend slope, RSI, normalized ATR, taker buy-volume fraction, volatility, cumulative unrealized PnL, and giveback from maximum favorable excursion). It predicts the continuation payoff:
   $$y = R_{\text{natural}} - R_{\text{early}}$$
   where $R_{\text{natural}}$ is the net return of letting the position exit naturally via the next AlphaTrend sell crossunder, and $R_{\text{early}}$ is the net return of closing immediately at the 24-hour mark. If the predicted continuation payoff $\hat{y} < 0$, the position is terminated early to truncate trailing losses.

The economic hypothesis being tested is whether post-entry path dynamics contain learnable, transferable information about trend exhaustion that persists across market regimes. The empirical finding of the primary study is a rigorous negative result: across 704 walk-forward models and 40 multiplicity-adjusted circular block bootstrap intervals, no supervised exit model demonstrated statistically robust out-of-sample generalization over unmanaged AlphaTrend.

## Signal

### Formation timestamp

- Base execution clock: 15-minute intervals.
- Strategy decision intervals: 2-hour (2h) and 4-hour (4h) candle closes (`source-reported`).
- Decisions occur strictly at candle close timestamps; execution occurs with an explicit 15-minute delay (1 bar delay at the subsequent 15-minute open) for baseline, and 30 minutes for delay stress (`source-reported`).
- Timezone: UTC.

### Lookback

- AlphaTrend indicator: 14-period ATR (using Simple Moving Average of True Range, SMA(TR)) and 14-period Money Flow Index (MFI).
- Volatility normalizer: 42-period rolling standard deviation of log returns.
- Supervised exit training cohorts: Monthly walk-forward updating with a 7-day label maturity embargo (only trades whose natural exits fully resolved strictly before month-start minus 7 days are eligible for training). Evaluated training windows: expanding history, trailing 730 days (2 years), and trailing 365 days (1 year).

### Entry

- **LONG entry:** Triggered when the AlphaTrend line crosses above its 2-bar lagged value (`ta.crossover(AlphaTrend, AlphaTrend[2])` on the native 2h or 4h timeframe).
- **Position Sizing:** Long-or-flat portfolio rule. The target notional/equity fraction is determined by volatility-scaled sizing:
  $$\text{target\_fraction} = \text{state} \times \min\left(0.5, \frac{0.20}{\max(\text{risk\_vol}, 0.10)}\right)$$
  ensuring maximum notional exposure does not exceed 0.5x account equity (`source-reported`).
- **Shorting:** Disabled; strategy is evaluated strictly long-or-flat (`source-reported`).

### Exit

- **Natural AlphaTrend Exit:** Triggers when the AlphaTrend line crosses below its 2-bar lagged value (`ta.crossunder(AlphaTrend, AlphaTrend[2])`). Natural exits take absolute precedence over coincident checkpoint evaluations (`source-reported`).
- **Supervised Early Exit Checkpoint:** Evaluated exactly once per trade at $t = t_{\text{entry}} + 96$ fifteen-minute bars (exactly 24 hours elapsed):
  - Model computes predicted continuation payoff $\hat{y} = \hat{R}_{\text{natural}} - \hat{R}_{\text{early}}$.
  - If $\hat{y} < 0$, position exits to flat (0) on the subsequent 15-minute bar.
  - Policy variants evaluated:
    - `current`: 18-feature HistGradientBoosting (HGB) on expanding history; exit if $\hat{y} < 0$.
    - `compact8`: 8 reduced features, compact HGB (`max_depth=2, max_leaf_nodes=3, l2=50`); exit if $\hat{y} < 0$.
    - `robust8`: 8 features, compact HGB with training targets winsorized at 2.5%/97.5% quantiles and sample weights proportional to $1/\sqrt{n_{\text{group}}}$; exit if $\hat{y} < 0$.
    - `temporal_mean`: Arithmetic average of 3 robust8 heads (expanding, 730-day, 365-day history); exit if $\text{mean}(\hat{y}) < 0$.
    - `temporal_guard`: Same 3 robust8 heads; exits ONLY if all three heads strictly agree on early exit ($\max(\hat{y}_i) < 0$).
    - `ridge8`: 8 features with Ridge regression ($\alpha = 50$); exit if $\hat{y} < 0$.
    - `transfer_current`, `transfer_compact`, `transfer_robust`: Models trained solely on the opposite asset (BTC evaluated by model trained on ETH; ETH evaluated by model trained on BTC).
- **Terminal Window Exit:** At the conclusion of each 6-month accounting half-year, all open positions are force-closed at the terminal open (`source-reported`).

### Holding period

- Variable holding period governed by AlphaTrend trend duration, subject to a potential early exit at 24 hours. If not exited early at 24 hours, the trade remains open until the natural AlphaTrend sell crossover or 6-month terminal window close.

### Parameters

| Parameter | Value | Status |
|---|---|---|
| AlphaTrend Common Period | 14 | Source-reported |
| AlphaTrend Multiplier | 1.0 | Source-reported |
| AlphaTrend ATR Formulation | SMA(TR) (14-period SMA of True Range) | Source-reported |
| AlphaTrend Momentum Gate | MFI(14) $\ge 50$ (Money Flow Index on typical price HLC3) | Source-reported |
| Checkpoint Latency Window | Exactly 24 hours (96 bars on 15m clock) | Source-reported |
| Maximum Leverage Cap | 0.5x notional / equity | Source-reported |
| Target Volatility Sizing | $0.20 / \max(\text{risk\_vol}, 0.10)$ | Source-reported |
| Baseline Execution Friction | 7.0 bps per side (taker fee + slippage) | Source-reported |
| Stress Execution Friction | 14.0 bps per side | Source-reported |
| Baseline Execution Delay | 15 minutes (1 bar delay) | Source-reported |
| Stress Execution Delay | 30 minutes (2 bar delay) | Source-reported |
| Minimum Training Cohort Size | 20 matured non-left-censored exit labels | Source-reported |
| Label Embargo Window | 7 days prior to monthly boundary | Source-reported |
| Compact HGB Parameters | `learning_rate=0.03, max_iter=100, max_depth=2, max_leaves=3, min_leaf=20, l2=50` | Source-reported |
| Ridge Alpha Regularization | 50.0 (Cholesky solver) | Source-reported |
| Winsorization Percentiles | 2.5th and 97.5th percentiles (linear interpolation) | Source-reported |
| Group Weight Formula | $w_i \propto 1 / \sqrt{n_{\text{group}}}$ for symbol $\times$ half-year groups | Source-reported |
| Multi-Asset Universe | BTCUSDT, ETHUSDT USD-M Perpetual Futures | Source-reported |
| Falsification Bootstrap Draws | 100,000 paired circular blocks (widths 7 and 28 days, seed 1015) | Source-reported |
| Falsification Tail Adjustment | Bonferroni-style tail percentile: $\alpha = 0.025 / 40$ | Source-reported |
| Production Selection Status | Null (no model selected for live deployment) | Source-reported |
| Multi-Asset Scaling Buffer | 5 bps minimum target change threshold to avoid micro-churn | Research-proposed |
| Unresolved Label Fill | 0.0 imputed continuation payoff if right-censored at evaluation | Research-proposed |

## Required data

- **Instruments:** Binance BTCUSDT and ETHUSDT USD-Margined Perpetual Futures.
- **Venues:** Binance USD-M Futures (public historical data archives).
- **Timeframe:** 15-minute base clock, aggregated to 2-hour and 4-hour evaluation bars.
- **Fields:**
  - 15-minute OHLCV candles.
  - Taker buy volume (used to calculate `taker_fraction = (buy_volume / total_volume - 0.5) * 4`).
  - Mark-price candles (for exact 8-hour funding rate fee settlement).
  - Continuous historical funding rates.
- **Missing Data Handling:** Verified repairs applied to missing coarse exchange archives; full UTC grid enforced across both assets.
- **Point-in-Time Integrity:**
  - Label maturity strictly enforces that natural trade outcomes are known before the training cutoff ($t - 7\text{d}$).
  - All features extracted at the 24-hour checkpoint use prices and indicators strictly prior to the checkpoint timestamp.
  - Cross-asset transfer strictly removes the target asset before computing quantiles, group weights, and standard scalers.

## Execution assumptions

- **Signal-to-Order Timing:** Decisions occur on bar close; orders execute on the subsequent 15-minute bar open (15-minute execution delay).
- **Fill Model:** Immediate fill at the delayed bar open price.
- **Transaction Costs (Baseline):** 7.0 basis points (0.07%) on each traded side (representing Binance retail taker fee + conservative market impact/slippage).
- **Transaction Costs (Stress):** 14.0 basis points per side (doubled cost stress).
- **Execution Delay Stress:** 30 minutes (2 bars on the 15-minute grid) with baseline 7 bps fee.
- **Funding Cash Flows:** Actual historical 8-hour funding payments settled on open positions using mark prices at funding timestamps.
- **Portfolio Construction:** Equal-capital allocation between BTC and ETH sleeves, rebalanced and closed every 6 months.

## Evidence

### Source-reported

All empirical figures below are extracted directly from `report.json`, `asset_results.csv`, `verification.json`, and Table 1 / Table 2 of the research manuscript (`wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8`).

#### 1. Baseline Friction (7 bps / 15m delay) Across Development (2024–2025) and Recent (Jan–Aug 2026) Periods

| Timeframe | Policy | 2024–2025 Dev Return (%) | Dev Max DD (%) | Dev Sharpe | 2026 Recent Return (%) | Recent Max DD (%) | Recent Sharpe |
|---|---|---:|---:|---:|---:|---:|---:|
| 2h | Alpha (Unmanaged) | 23.27% | 16.09% | 0.89 | 4.26% | 10.62% | 0.55 |
| 2h | Current (18-feat HGB) | 13.07% | 12.70% | 0.67 | 5.80% | 7.87% | 0.82 |
| 2h | Compact8 | 2.38% | 14.23% | 0.17 | 6.94% | 7.66% | 0.91 |
| 2h | Robust8 | 4.08% | 13.70% | 0.24 | 7.51% | 7.17% | 0.98 |
| 2h | Temporal Mean | 5.54% | 15.01% | 0.30 | 6.87% | 6.69% | 0.94 |
| 2h | Temporal Guard | 11.57% | 14.80% | 0.54 | 5.99% | 7.46% | 0.79 |
| 2h | Ridge8 | 28.73% | 14.67% | 1.11 | 4.43% | 8.98% | 0.60 |
| 2h | Transfer Current | 10.12% | 15.76% | 0.49 | 4.53% | 7.91% | 0.67 |
| 2h | Transfer Compact | 26.94% | 16.14% | 1.01 | 5.60% | 8.58% | 0.75 |
| 2h | Transfer Robust | 26.02% | 15.84% | 1.00 | 4.94% | 9.15% | 0.67 |
| 4h | Alpha (Unmanaged) | 26.11% | 14.12% | 0.96 | -4.96% | 16.82% | -0.56 |
| 4h | Current (18-feat HGB) | 38.13% | 9.15% | 1.48 | -3.02% | 11.02% | -0.44 |
| 4h | Compact8 | 21.31% | 11.60% | 0.88 | -5.91% | 17.64% | -0.76 |
| 4h | Robust8 | 17.63% | 11.13% | 0.76 | -4.41% | 16.33% | -0.63 |
| 4h | Temporal Mean | 13.89% | 12.68% | 0.62 | -2.09% | 14.30% | -0.25 |
| 4h | Temporal Guard | 13.01% | 12.68% | 0.57 | -4.53% | 16.43% | -0.56 |
| 4h | Ridge8 | 8.64% | 15.56% | 0.45 | -3.24% | 14.33% | -0.38 |
| 4h | Transfer Current | 26.75% | 11.53% | 1.05 | -4.96% | 16.82% | -0.73 |
| 4h | Transfer Compact | 20.33% | 13.71% | 0.80 | -2.11% | 14.32% | -0.24 |
| 4h | Transfer Robust | 22.17% | 13.71% | 0.85 | -3.67% | 15.69% | -0.49 |

#### 2. Cost Stress Grid (Doubled Friction D2/R2 vs 30-min Delay D30/R30)

| Timeframe | Policy | Dev Double Cost (14 bps) | Recent Double Cost (14 bps) | Dev 30m Delay | Recent 30m Delay |
|---|---|---:|---:|---:|---:|
| 2h | Alpha | 16.59% | 2.08% | 22.73% | 3.86% |
| 2h | Current | 7.10% | 3.62% | 13.79% | 5.45% |
| 2h | Compact8 | -2.95% | 4.73% | 1.07% | 6.57% |
| 2h | Robust8 | -1.33% | 5.29% | 3.03% | 7.64% |
| 2h | Temporal Mean | 0.01% | 4.68% | 5.12% | 7.13% |
| 2h | Temporal Guard | 5.72% | 3.80% | 11.65% | 6.10% |
| 2h | Ridge8 | 21.85% | 2.27% | 27.40% | 4.55% |
| 4h | Alpha | 22.18% | -6.22% | 26.41% | -4.10% |
| 4h | Current | 33.97% | -4.26% | 38.96% | -1.52% |
| 4h | Compact8 | 17.67% | -7.13% | 21.67% | -5.03% |
| 4h | Robust8 | 14.12% | -5.63% | 17.61% | -2.97% |
| 4h | Temporal Mean | 10.50% | -3.36% | 14.16% | -1.58% |
| 4h | Temporal Guard | 9.59% | -5.76% | 13.20% | -3.00% |
| 4h | Ridge8 | 5.48% | -4.52% | 8.65% | -2.26% |

#### 3. Paired Contrasts and Multiplicity-Adjusted Circular Block Bootstrap Intervals (100,000 draws, tail $\alpha = 0.025/40$)

- **Total Declared Contrasts:** 20 paired contrasts across 2 block widths (7-day and 28-day blocks) = 40 adjusted intervals.
- **Wholly Positive Intervals:** Exactly **0 out of 40** intervals lie entirely above zero (`source-reported`).
- **Intervals Containing Zero:** 39 out of 40 intervals span zero, indicating no statistically significant out-of-sample edge.
- **Significant Negative Interval:** Exactly one contrast excludes zero under 28-day blocks: `4h_temporal_guard vs 4h_current` with point estimate -0.2007 in log-wealth excess, 7-day interval `[-0.4648, 0.0126]`, and 28-day interval `[-0.4077, -0.0403]`, indicating that the conservative temporal guard significantly harmed returns relative to the incumbent model.

### Independently reproduced

`not independently reproduced`. All metrics and empirical distributions reflect primary research reported in `wizcap/alphatrend-generalization-study` commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8`.

### Negative evidence

1. **Failure of Simpler Models to Generalize Across Regimes:**
   - Reducing from 18 features to 8 features (`Compact8`) collapsed 2h development return from 13.07% to 2.38% and 4h return from 38.13% to 21.31%.
   - While `Compact8` and `Robust8` exhibited slightly better performance in the truncated 2026 period (+6.94% and +7.51% vs +5.80%), the trade-off was accompanied by severe development degradation and failed bootstrap tests.
2. **Ridge Regression Period Inversion:**
   - At 2h, `Ridge8` appeared to outperform during the 2024–2025 development window (28.73% vs 13.07% for `Current`), but immediately lagged during the 2026 forward window (4.43% vs 5.80%), and collapsed at 4h (8.64% vs 38.13% for `Current`).
3. **Temporal Aggregation Degrades Development Edge:**
   - Enforcing unanimous agreement among three lookback horizons (`Temporal Guard`) at 4h reduced net return by over 25 percentage points (13.01% vs 38.13% for `Current`), and resulted in a statistically significant negative log-wealth difference under 28-day blocks.
4. **Apparent Cross-Asset Transfer is an Artifact of Near-Zero Interventions:**
   - At 2h, `Transfer Compact` delivered 26.94% development return, but direct action auditing revealed it intervened at only 10 out of 161 checkpoints (exiting only 6.2% of trades). Its high return simply reflected unmanaged AlphaTrend rather than learned cross-asset intelligence.
   - At 4h, multiple monthly transfer heads collapsed into trivial constant-tree predictions due to insufficient sample support ($< 40$ observations).
5. **Author's Production Disposition:**
   - The primary research study explicitly concluded with:
     ```json
     "production_selection": null
     ```
     rejecting all 10 candidate exit configurations for live execution or production deployment.

## Falsification plan

1. **Multiplicity-Adjusted Circular Block Bootstrap Superiority:**
   - *Test:* Run 100,000 paired circular block bootstrap resamples of log-wealth differences across 7-day and 28-day blocks between candidate ML exit policies and the unmanaged AlphaTrend baseline.
   - *Research-defined falsification threshold:* If the lower bound of the Bonferroni-adjusted 95% confidence interval ($\alpha = 0.025 / 40$) fails to exceed 0.0, the hypothesis that supervised adaptive exits provide statistically robust generalization over rule-based AlphaTrend is falsified.
2. **Transaction Cost Drag & Break-Even Boundary:**
   - *Test:* Increase one-way taker friction from 7 bps to 14 bps and introduce a 30-minute execution lag.
   - *Research-defined falsification threshold:* If doubling transaction friction drives net 2-year development portfolio return negative (as observed in `Compact8` at -2.95% and `Robust8` at -1.33%), the strategy is falsified as commercially non-viable under realistic exchange taker fees.
3. **Random-Exit Placebo Benchmark:**
   - *Test:* Replace ML-predicted early exit decisions with a synthetic Bernoulli process matching the empirical early-exit frequency (~20–25%) while retaining AlphaTrend entries.
   - *Research-defined falsification threshold:* If the Sharpe ratio or net return of the ML-guided strategy does not exceed the random-exit placebo at a 95% bootstrap confidence level ($p > 0.05$), the hypothesis of predictive exit skill is rejected.
4. **Permutation Test on Post-Entry State Features:**
   - *Test:* Randomly permute the 8 post-entry state features (`alpha_distance`, `rsi14`, `taker_fraction`, `pnl_atr`, etc.) across checkpoint timestamps prior to model training.
   - *Research-defined falsification threshold:* If models trained on permuted features produce comparable out-of-sample continuation payoffs or loss-repair ratios to models trained on true features, the economic validity of the post-entry state space is refuted.

## Crypto portability

**direct**

- The strategy and research framework were natively designed, calibrated, and evaluated on crypto perpetual futures: Binance BTCUSDT and ETHUSDT USD-M contracts.
- **Crypto-Specific Structural Factors:**
  - **Perpetual Funding Rate Settlement:** Funding rates are charged every 8 hours based on mark price. The primary research codebase explicitly integrates continuous historical funding cash flows from official Binance archives (`funding_settlements`).
  - **24/7 Continuous Execution:** The strategy operates on a unified 15-minute UTC clock, eliminating equity-market overnight gap artifacts.
  - **Taker Fee & Slippage Sensitivity:** Crypto perpetual taker fees (typically 4–5 bps for VIP0/retail plus 2–3 bps spread/slippage) create severe turnover drag; the study proves that strategies intervening too frequently (e.g. `Compact8` turnover) suffer catastrophic degradation when friction is increased to 14 bps.

## Limitations

- **Restricted Asset Universe:** Evaluated exclusively on two top-tier cryptocurrency assets (BTC and ETH); cross-sectional dynamics across long-tail altcoins remain untested.
- **Sample Size Constraints:** Low frequency of completed trend-following episodes (only 158 resolved checkpoints at 2h and 93 at 4h during the 2024–2025 development period) limits statistical power and leads to constant-tree model collapses in single-asset transfer configurations.
- **Lookback Exposure:** The evaluation period (2024–2026) had been previously inspected during preliminary research phases; the study represents a frozen computational audit rather than a pristine, unseen holdout.
- **Long-Only Restriction:** The evaluated implementation operates exclusively long-or-flat, omitting the short-side performance dynamics of AlphaTrend.
- **Artificial Half-Year Boundaries:** Sleeves are liquidated and reset every 6 months to match experimental accounting windows, introducing periodic rebalancing frictions not present in continuous trading accounts.

## Implementation status

`not-implemented`

No implementation exists in our PyBroker or NautilusTrader research stacks. Not backtested in our environment, not paper-traded, not testnet-deployed, not authorized for live trading.

## Adoption boundary

`research-only`, `not-approved`

A record being present in this repository does NOT mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- `[[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]` — Trend-following cost-gate falsification and turnover degradation on crypto perpetuals.
- `[[quant/crypto-residual-momentum-market-beta-neutralization-2026-09-11]]` — Time-series and cross-sectional momentum behavior on crypto perpetuals.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Walk-forward label maturity, purging, and embargo protocols for non-stationary financial time series.
- `[[quant/statistical-arbitrage-methodology-degradation-ladder-falsification-2026-09-12]]` — Methodology degradation ladder and multi-horizon falsification.

## Sources

1. wizcap. *"Generalization Limits of Adaptive AlphaTrend Exit Models in Cryptocurrency Futures"*, Research Preprint v1.0.0 (September 11, 2026). GitHub repository `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8`. Full text manuscript: `paper/manuscript.md`.
2. KivancOzbilgic. *"AlphaTrend Strategy"*, TradingView open-source Pine strategy v5 (Mozilla Public License 2.0). URL: [https://www.tradingview.com/script/3wdQu7P3-AlphaTrend-Strategy/](https://www.tradingview.com/script/3wdQu7P3-AlphaTrend-Strategy/). SHA-256: `0e9f04404ca0e414a6509ae3db278906efb661742dfa10112790e022b8e4e40d`. Preserved in `references/alphatrend/original_strategy.pine` and `references/alphatrend/provenance.json`.
3. Source file `evidence/study015/report.json` in `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (full empirical return tables, drawdowns, Sharpe ratios, and 40 circular block bootstrap intervals).
4. Source file `evidence/study015/verification.json` in `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (computational audit results verifying 303 passed tests, 704 refit models, and 720 asset account replays).
5. Source file `evidence/study015/study015_method.md` in `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (pre-declared experimental design, cohort maturity rules, and policy specifications).
6. Source file `neattrade/alphatrend.py` in `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (Python implementation of AlphaTrend indicator and cross-state logic).
7. Source file `neattrade/generalize_v15.py` in `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (HistGradientBoosting, Ridge, and temporal ensemble exit policy engine).
8. Source file `neattrade/repair_v12.py` in `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (24-hour causal checkpoint feature extraction and label definitions).
9. Source file `neattrade/indicators_v11.py` in `wizcap/alphatrend-generalization-study`, commit `9d604eb6ffc0e1392692e90d0a0e61b611ed51c8` (native candle indicator definitions and volatility sizing functions).
