---
schema: strategy-research-record-v1
title: Staged Short-Term Intraday Drawdown Reversal with Machine-Learned Timing Overlay and Trend-Health Gating
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/tree/3194d210a0a4e243825c837ed4791b381831f688"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Staged Short-Term Intraday Drawdown Reversal with Machine-Learned Timing Overlay and Trend-Health Gating

## Provenance

- **Repository:** `https://github.com/randomwalkhan/Short-Term-Reversal-Strategy`
- **Canonical Source Identity:** GitHub repository `randomwalkhan/Short-Term-Reversal-Strategy` at immutable commit `3194d210a0a4e243825c837ed4791b381831f688`.
- **Commit Date / As-Of:** 2026-09-11 13:32:52 UTC (`Update Reversal Alpaca paper 2026-09-11 09:32 ET`).
- **Primary Source Code Paths Inspected Directly:**
  - `README.md`: Official strategy specifications for Reversal 3.5 and 3.3, multi-stage optimization trajectory, live paper dashboard.
  - `RESEARCH_GUARDRAILS.md`: Anti-overfitting criteria, causal mechanism requirements, execution realism checks.
  - `backtest_metrics.py`: Annualized Sharpe calculation using U.S. 10-Year Treasury par yield rate (4.23% as of 2026-03-16).
  - `backtest_reversal_3_1_calls.py`: Core signal construction, maximum intraday drop calculation, rolling historical recovery probability gate, Black–Scholes option mark model.
  - `backtest_reversal_3_3_calls.py`: Reversal 3.3 official backtest runner combining universe selection with walk-forward timing overlay.
  - `backtest_reversal_3_3_timing_overlay_experiment.py`: Feature engineering (SMA, EMA, ATR, DI+/DI-, RSI, rolling MAD), expanding-window Logistic Regression model training, probability scoring.
  - `reversal_universe.py`: Screened universe generation (`qqq_only_filtered` + curated ETF overlays `SOXL`, `UPRO`, `DRAM`), liquidity filters, trailing P/E ceiling guard (`trailing P/E < 140`).
  - `analyze_reversal_2_4_overfitting.py`: Multi-year backtest (2021–2026), half-year subperiod stability analysis, parameter grid sweeps, ticker PnL concentration analysis, placebo test.
  - `reversal_3_3_live.py` & `reversal_3_4_1_alpaca_paper.py`: Production paper-trading loop, option quote staleness checks, trend-health gating, liquidity validation.
  - `results/reversal_3_3/reversal_3_3_summary.csv`: Official 1-year backtest performance metrics.
  - `results/reversal_3_3/reversal_3_3_baseline_comparison.csv`: Direct ablation of timing overlay against raw signal baseline.
  - `results/reversal_2_4_overfit/segment_stability.csv`: Detailed 2021–2026 half-year return and drawdown series.
  - `results/reversal_2_4_overfit/ticker_pnl_concentration.csv`: Constituent ticker attribution across 1,279 trades.
- **Source Quality:** Open-source quantitative research repository featuring documented code, versioned backtests, ablation matrices, automated paper trading, and empirical failure/overfitting diagnostics.

## Economic mechanism

### Source-reported

The strategy exploits short-horizon overreaction following large intraday equity drawdowns. The author stated rationale operates across five layered components:
1. **Intraday Liquidity Holes & Forced Liquidation:** Sharp intraday price drops in liquid large-cap technology stocks often overshoot fair value as market-maker inventory limits are hit, stop-loss orders trigger cascades, and institutional desks execute price-insensitive liquidation programs.
2. **Conditional Historical Recovery Frequency:** Rather than assuming all price drops mean-revert equally, the strategy conditions on asset-specific recent microstructure resilience. By examining the preceding 60 trading days, it measures whether past drawdowns of equal or greater magnitude recovered at least 70% of the drop within the subsequent 5 trading days. Tickers demonstrating high conditional recovery rates (>= 80% with >= 10 historical occurrences) possess persistent buy-the-dip institutional support in the current market environment.
3. **Valuation Knife-Catch Protection:** High-multiple growth equities undergoing fundamental valuation reratings frequently fail to mean-revert. Excluding stocks with extreme trailing price-to-earnings multiples (`trailing P/E >= 140`) filters out falling knives (e.g., AMD, AXON, CSGP, DDOG, FANG, PLTR, TSLA).
4. **Machine-Learned Timing Overlay:** Even when a conditional drawdown signal triggers, entering into a strong directional momentum downtrend causes losses. A walk-forward logistic regression model trained on multi-indicator technical features (trend, volatility, directional movement) generates an out-of-sample probability of successful rebound; trades with p_timing < 0.50 are blocked.
5. **Asymmetric Convexity via Option Contracts:** Purchasing near-the-money call options (~30 DTE) limits capital risk to the premium paid (strictly constrained by a -10% hard stop-loss) while providing convex upside participation during the rapid 1-2 day initial snapback.

### Research interpretation

This setup is a **microstructure overextension and inventory rebalancing strategy augmented by conditional Bayesian state-filtering and options payoff asymmetry**:
1. **Transient Supply-Demand Dislocation:** In mega-cap and liquid tech equities, large intraday drops represent transitory liquidity imbalances rather than instantaneous permanent information arrival. Once aggressive selling pauses, bid-ask spreads compress and inventory rebalancing pushes prices toward the pre-shock level.
2. **Empirical Bounce Probability as a Nonparametric Regime Filter:** The 60-day historical success rate acts as a local regime estimator. When a stock recent order-flow environment readily absorbs sell programs, its empirical bounce rate is high. When macro headwinds or earnings downgrades induce persistent selling drift, the bounce rate drops below 80%, shutting down the signal automatically.
3. **Convex Payoff Framing vs. Theta Decay:** Buying short-dated calls avoids the unbounded downside of longing spot equities with trailing stops. However, the strategy must achieve swift mean reversion within 24-48 hours; otherwise, option implied volatility crush and rapid theta decay quickly erode contract value.
4. **Severe Tail Risk in Sustained Bear Markets (Negative Evidence):** Because the core signal relies on dip-buying, it functions as a liquidity provider. In protracted structural bear markets (such as 2022-H2), mean-reversion fails systematically as downward momentum dominates, leading to severe portfolio drawdowns (-57.03% in 2022-H2). The machine-learned timing overlay and trend-health filter serve as necessary compensatory friction to mitigate this fundamental regime fragility.

## Signal

### Primary Signal Definition

1. **Intraday Maximum Drop Calculation:**
   For each stock on trading day t:
   D_t = (P_{t-1}^close - P_t^low) / P_{t-1}^close
   where P_{t-1}^close is the previous trading day adjusted closing price, and P_t^low is day t intraday low price.
2. **Minimum Drop Gate:**
   D_t > 0.5% (i.e., D_t > 0.005). Signals where the intraday drop is <= 0.5% are discarded.
3. **Signal Drop Dollar Amount:**
   SDA_t = D_t * P_{t-1}^close = P_{t-1}^close - P_t^low
4. **Historical Recovery Success Definition:**
   For any historical day tau in [t - 60, t - 5] (excluding the most recent 5 days to avoid forward-looking window overlap):
   Future High_tau = max_{k=1..5} P_{tau+k}^high
   Recover Ratio_tau = (Future High_tau - P_tau^low) / SDA_tau
   Signal Success_tau = I(Recover Ratio_tau >= 0.70)
5. **Conditional Historical Success Rate & Match Count:**
   Identify historical matching days tau where D_tau >= D_t:
   M_t = sum_{tau=t-60}^{t-5} I(D_tau >= D_t and valid)
   SR_t = (1 / M_t) * sum_{tau=t-60}^{t-5} (I(D_tau >= D_t) * Signal Success_tau) * 100
6. **Primary Signal Acceptance Criteria:**
   SR_t >= 80.0% and M_t >= 10

### Machine-Learned Timing Overlay

- **Feature Pipeline:**
  - Common features: success_rate (SR_t), matched_signals (M_t), current_drop_pct (D_t), rolling_sigma_20d_pct (20-day annualized realized volatility).
  - 5-day technical timing indicators:
    - SMA_5: 5-day simple moving average.
    - EMA_5: 5-day exponential moving average.
    - ATR_5: 5-day average true range.
    - DI+_5, DI-_5: 5-day directional indicators derived from directional movement divided by ATR_5.
    - RSI_5: 5-day relative strength index.
    - MAD_5: 5-day rolling mean absolute deviation of price.
- **Model Architecture & Training:**
  - Standardized scaling via `StandardScaler` with mean imputation (`SimpleImputer(strategy="mean")`).
  - Classifier: `LogisticRegression(max_iter=1000, random_state=42)`.
  - Walk-forward training: Model is fitted using historical candidate signal events prior to trade date t with an expanding window (minimum 250 training signals, minimum class count of 40 events per outcome class).
- **Inference & No-Trade Gate:**
  - Generates out-of-sample probability p_timing in [0, 1].
  - Execution rule: If p_timing < 0.50, block entry (no-trade gate).
  - In Reversal 3.5 live execution, early-entry signals (10:00-12:00 ET) require p_timing >= 0.67, SR_t >= 88%, and M_t >= 30, but are restricted to shadow-only tracking due to live empirical fragility.

### Trend-Health Breakdown Gate (Reversal 3.5 Live Filter)

Blocks trade entry if any of the following 4 trend-breakdown conditions are met:
1. 10-day linear regression slope < -0.25% per day.
2. 10-day lookback total return < -1.50%.
3. Current spot price < 0.995 * SMA_5 (trading >0.5% below 5-day moving average).
4. Lower close streak >= 4 consecutive sessions.

### Option Contract Selection Rules

- **Option Type:** Call options.
- **Expiration Window:** Target approx 30 trading DTE (allowed window: 21 to 40 trading DTE).
- **Moneyness:** Near-ATM calls with absolute moneyness |K / P_close - 1| <= 8%, maximum out-of-the-money allowance <= 5%.
- **Option Liquidity Gate:**
  - Minimum Open Interest: >= 110 contracts.
  - Minimum Daily Volume: >= 20 contracts.
  - Maximum Bid-Ask Spread: <= 14% of mid-price ((Ask - Bid) / Mid <= 0.14).
  - Rejection: If no contract satisfies liquidity constraints, trade is skipped.

### Position Sizing & Staged Exit Ladder

- **Portfolio Allocation:** Maximum 2 concurrent open positions (MAX_OPEN_POSITIONS = 2).
- **Sizing:** Target 50% of available portfolio equity allocated per open position (TARGET_POSITION_WEIGHT = 0.50).
- **Staged Exit Ladder (Reversal 3.3 Backtest):**
  - **Day 1 Exit:** If option gain >= +10%, take profit and exit.
  - **Day 2 Exit:** If option gain >= +15%, take profit and exit.
  - **Stop-Loss:** If option drawdown hits <= -10%, exit immediately (hard stop).
  - **Time Exit:** If neither take-profit nor stop-loss is triggered within 5 business days, exit at market close on Day 5.
- **Staged Exit Ladder (Reversal 3.5 Live Execution):**
  - **Day 1 Exit:** Take-Profit at +15%.
  - **Day 2 Exit:** Take-Profit at +15%.
  - **Stop-Loss:** Hard stop at -10%.
  - **Holding Limit:** 5 business days.

## Required data

- **Universe:** 
  - Base universe: `qqq_only_filtered` (~97 liquid Nasdaq 100 constituent equities).
  - Curated ETF overlay: `SOXL` (Direxion Daily Semiconductor Bull 3X), `UPRO` (ProShares UltraPro S&P 500 3X), and `DRAM` (Memory ETF added in Reversal 3.5).
  - Universe exclusion filters:
    - Minimum market capitalization: > $1B.
    - Minimum share price: > $10.00.
    - Structural exclusions: Warrants, rights, units, preferred shares, ADRs/depositary shares, debt notes, debentures.
    - Fundamental valuation ceiling: Non-ETF equities with `trailing P/E >= 140` are excluded.
- **Fields Required:**
  - Daily equity OHLCV and Adjusted Close.
  - Real-time intraday Low and Current Price during market hours.
  - End-of-day equity options chains (bid, ask, volume, open interest, strike, expiration, implied volatility).
- **Timeframe & Session Alignment:**
  - Daily bar close for signal calculation.
  - Intraday monitoring slots: `manage_0930` (market open review) and standard close execution.
  - Timezone: US Eastern Time (`America/New_York`).
- **Point-in-Time Integrity:**
  - 60-day historical success rate excludes the most recent 5 trading days (t-5 to t-1) to eliminate lookahead bias in forward 5-day high recovery determination.
  - Machine learning timing model is refitted strictly on historical signals realized prior to trade date t.
  - Extended quote staleness guard: Options quotes older than 20 minutes are rejected.

## Execution assumptions

- **Execution Venue:** US equity and equity options exchanges (e.g., via Alpaca Paper API, Interactive Brokers).
- **Order Types & Pricing:**
  - In research backtests: Evaluated using Black–Scholes option mid-price (S, K, tau, sigma_ann_20d, r = 4%).
  - In live paper runner: Executed against live option bid/ask quotes with maximum spread constraint of <= 14%.
- **Fees & Slippage:**
  - Source-reported backtests assume frictionless Black–Scholes fills; live runner operates in paper mode without real exchange clearing fees.
  - `research-proposed`: Real-world options execution requires modeling OCC clearing fees (~$0.02/contract), exchange broker commissions (~$0.65/contract), and conservative half-spread slippage (~5% to 7% of option premium).
- **Capacity Constraint:**
  - Bounded by the open interest and bid-ask depth of individual equity option series. With minimum open interest of 110 and volume of 20, realistic capacity per name is limited to $10,000 to $50,000 in premium before incurring severe market impact.

## Evidence

### Source-reported

All figures below are transcribed directly from primary source backtest summary CSVs, comparison logs, and code files in `randomwalkhan/Short-Term-Reversal-Strategy`:

#### 1. Official Reversal 3.3 Backtest Performance (1-Year Snapshot)
- **Source File:** `results/reversal_3_3/reversal_3_3_summary.csv` and `reversal_3_3_baseline_comparison.csv`.
- **Sample Period:** 2025-04-23 to 2026-04-23 (1 calendar year).
- **Initial Capital:** $10,000.00.
- **Risk-Free Rate:** 4.23% per annum (U.S. 10-Year Treasury par yield rate on 2026-03-16).
- **Results:**
  - Final Equity: $79,084.73
  - Total Return: +690.85%
  - Maximum Drawdown: -26.42%
  - Win Rate: 69.23%
  - Total Trades: 117
  - Annualized Sharpe Ratio: 4.32
- **Ablation vs. Baseline Without Timing Overlay:**
  - Baseline Final Equity: $182,287.24
  - Baseline Total Return: +1,722.87%
  - Baseline Maximum Drawdown: -48.99%
  - Baseline Win Rate: 63.27%
  - Baseline Total Trades: 245
  - Baseline Annualized Sharpe: 4.24
  - **Finding:** Adding the 5-day walk-forward logistic timing overlay reduced trade count by 52.2%, compressed maximum drawdown by 22.57 percentage points (from -48.99% to -26.42%), and elevated win rate by 5.96 percentage points (from 63.27% to 69.23%), confirming its role as an effective risk filter.

#### 2. Universe Selection Controlled Ablation (Reversal 2.3.3)
- **Source File:** `results/reversal_2_3_3_universe_comparison/reversal_2_3_3_universe_comparison.csv`.
- **Sample Period:** 2025-03-17 to 2026-03-16.
- **Rule:** Identical dynamic filter (`matched_signals >= 10`, `success_rate >= 80%`) tested across 5 candidate universes:

| Universe Name | Usable Tickers | Win Rate | Total Return | Max Drawdown | Sharpe (rf=4.23%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `qqq_only_filtered` | 97 | 59.02% | +552.91% | -32.46% | 2.93 |
| `legacy_watchlist_11` | 10 | 54.15% | +81.27% | -31.57% | 1.18 |
| `qqq_spy_filtered` | 501 | 53.53% | +54.38% | -43.24% | 0.91 |
| `spy_only_filtered` | 491 | 52.92% | +36.28% | -43.26% | 0.73 |
| `nasdaq_spy_filtered` | 1,163 | 50.81% | -7.10% | -50.29% | 0.23 |
| `nasdaq_only_filtered` | 830 | 49.59% | -30.21% | -50.51% | -0.15 |

- **Finding:** Reversal edge is strictly concentrated in liquid, high-quality Nasdaq 100 technology names (`qqq_only_filtered`). Broadening the universe into the wider S&P 500 or full Nasdaq composite dilutes the edge into negative performance (-30.21% on Nasdaq only), proving that the phenomenon is not an unconstrained market-wide effect.

#### 3. Factor Refinement Ablation (Reversal 2.4)
- **Source File:** `results/reversal_2_4_article_variants/reversal_article_variants_summary.csv`.
- **Sample Period:** 2025-03-17 to 2026-03-16 on `qqq_only_filtered`:

| Factor Variant | Return | Max Drawdown | Win Rate | Trades | Sharpe |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `Window 60d` (Promoted) | +806.11% | -30.56% | 61.00% | 241 | 3.41 |
| `Original 2.3.3` (Baseline) | +552.91% | -32.46% | 59.02% | 244 | 2.93 |
| `Add Volume` | +364.25% | -37.58% | 57.32% | 239 | 2.44 |
| `Window 126d` | +276.80% | -38.62% | 56.83% | 227 | 2.18 |
| `Window 252d + Recent Weight` | +181.17% | -30.21% | 56.31% | 206 | 1.82 |
| `Kappa / s-score` | +145.58% | -29.95% | 55.61% | 214 | 1.61 |
| `PCA Defactored` | +23.89% | -42.39% | 52.31% | 216 | 0.60 |

#### 4. Minimum Drop Gate Ablation (Reversal 2.5)
- **Source File:** `results/reversal_2_5_min_drop_experiment/reversal_2_5_min_drop_summary.csv`.
- **Sample Period:** 2025-03-17 to 2026-03-16:
  - Drop >0.0% (Baseline): Return +806.11%, Max DD -30.56%, Win Rate 61.00%, Sharpe 3.41
  - Drop >0.5% (Promoted): Return +1,305.60%, Max DD -30.84%, Win Rate 62.08%, Sharpe 3.96
  - Drop >1.0%: Return +594.68%, Max DD -24.79%, Win Rate 60.44%, Sharpe 3.11
  - Drop >2.0%: Return +485.14%, Max DD -22.05%, Win Rate 62.13%, Sharpe 3.20
  - Drop >3.0%: Return +77.61%, Max DD -15.15%, Win Rate 60.00%, Sharpe 1.68
  - Drop >4.0%: Return +3.56%, Max DD -18.19%, Win Rate 52.38%, Sharpe 0.06

#### 5. Multi-Year Subperiod Stability (2021-2026)
- **Source File:** `results/reversal_2_4_overfit/segment_stability.csv`.
- **Full Period Metrics (2021-01-01 to 2026-03-13, 1,279 trades):** Final equity $9,525,897.68, Total return +95,158.98%, Max DD -62.41%, Win rate 56.68%, Average trade return +1.34%.
- **Half-Year Subperiod Breakdown:**
  - `2021-H1`: Return +46.56%, Max DD -39.77%, Win Rate 54.55% (121 trades)
  - `2021-H2`: Return +191.66%, Max DD -27.23%, Win Rate 60.80% (125 trades)
  - `2022-H1`: Return +31.31%, Max DD -29.90%, Win Rate 53.57% (112 trades)
  - `2022-H2`: Return -40.53%, Max DD -57.03%, Win Rate 45.83% (120 trades) **[Severe Failure Regime]**
  - `2023-H1`: Return +236.18%, Max DD -29.46%, Win Rate 62.30% (122 trades)
  - `2023-H2`: Return +66.12%, Max DD -34.35%, Win Rate 55.65% (124 trades)
  - `2024-H1`: Return +59.47%, Max DD -30.17%, Win Rate 55.37% (121 trades)
  - `2024-H2`: Return +57.53%, Max DD -25.59%, Win Rate 56.00% (125 trades)
  - `2025-H1`: Return +140.17%, Max DD -23.20%, Win Rate 58.97% (117 trades)
  - `2025-H2`: Return +380.09%, Max DD -19.96%, Win Rate 64.75% (122 trades)
  - `2026-H1` (to 03-13): Return +15.16%, Max DD -25.48%, Win Rate 55.56% (36 trades)

#### 6. Ticker PnL Concentration
- **Source File:** `results/reversal_2_4_overfit/ticker_pnl_concentration.csv`.
- Across the multi-year backtest, returns exhibit heavy concentration in specific resilient technology and biotech names:
  - `KLAC`: $1,726,932.76 (18.15% of total PnL)
  - `GILD`: $1,110,065.89 (11.67% of total PnL)
  - `INSM`: $1,037,499.68 (10.90% of total PnL)
  - `WDC`: $793,856.90 (8.34% of total PnL)
  - `ORLY`: $699,591.17 (7.35% of total PnL)
  - Top 3 tickers generate 40.72% of cumulative strategy profits; top 5 tickers account for 55.21%.

### Independently reproduced

`not independently reproduced`. All metrics and empirical distributions reflect third-party backtest outputs and live paper recordings from the primary GitHub repository.

### Negative evidence

1. **Catastrophic Regime Vulnerability in 2022-H2:** The empirical half-year stability analysis reveals severe strategy failure during the sustained macroeconomic tech bear market of 2022-H2: total return fell to -40.53%, maximum drawdown expanded to -57.03%, and the trade win rate collapsed to 45.83%. In trending bear regimes, buying intraday dips triggers cascading stop-loss hits as intraday drawdowns continuation rather than mean-revert.
2. **Universe Fragility Outside Nasdaq 100:** When deployed on broader universes (`nasdaq_only_filtered` or `nasdaq_spy_filtered`), returns collapse to negative numbers (-30.21% and -7.10%, respectively, with Sharpe ratios of -0.15 and 0.23). The reversal effect does not generalize to mid/small-cap equities.
3. **Extreme Ticker Concentration Risk:** Over 40% of 5-year cumulative gains stem from just three constituent tickers (`KLAC`, `GILD`, `INSM`), indicating that idiosyncratic single-stock behavior disproportionately drives portfolio performance.
4. **Early-Entry Intraday Failure:** In live paper deployment (documented in README and code), opening positions during the 10:00-12:00 ET intraday window exhibited high failure rates and instability, forcing the author to demote early-entry execution to `shadow-only` tracking in Reversal 3.5.
5. **Execution Friction & Option Spread Drag:** The core backtests assume idealized Black–Scholes option execution at mid-market prices. In live options trading, wide bid-ask spreads (even under the 14% gate) and dealer slippage on market orders can consume a substantial fraction of the +10% to +15% take-profit target.

## Falsification plan

1. **Realistic Spread and Commission Friction Stress Test:**
   - Re-run the official Reversal 3.3 backtest replacing Black–Scholes mid-prices with conservative execution prices: enter at Ask + 0.05 * Spread, exit at Bid - 0.05 * Spread, plus $0.65/contract OCC/broker commission.
   - `research-defined falsification threshold`: If net annualized Sharpe drops below 1.50 or net return erodes by more than 50% relative to mid-price backtest, reject the hypothesis that theoretical option reversal profits survive execution friction.
2. **Macro Bear Market Regime Stress (2022 Replay Audit):**
   - Evaluate the strategy across rolling 6-month windows where the benchmark index (QQQ) suffers a drawdown > 15% and trades below its 200-day moving average.
   - `research-defined falsification threshold`: If the strategy suffers an annualized drawdown > 35% or delivers a negative information ratio against QQQ during bear regimes, reject the claim that the 5-day ML timing overlay and trend-health filter adequately solve downward momentum vulnerability.
3. **Top-Ticker Leave-One-Out (Jackknife) Test:**
   - Sequentially remove the top 3 profit-generating tickers (`KLAC`, `GILD`, `INSM`) from the universe.
   - `research-defined falsification threshold`: If removing these three names reduces the multi-year annualized return by > 40% or lowers the win rate below 52%, reject the hypothesis of a universal Nasdaq 100 reversal anomaly and classify it as an idiosyncratic asset artifact.
4. **Placebo Shuffled Signal Day Permutation Test:**
   - Holding the trading universe and timing model fixed, randomly permute the signal drop days across non-signal days within the same stock trajectories (1,000 Monte Carlo paths).
   - `research-defined falsification threshold`: If more than 5% of placebo permutations (p > 0.05) generate a Sharpe ratio within 1.0 of the empirical strategy Sharpe, reject the predictive validity of the 60-day recovery probability condition.
5. **Holding Period Decay & Premature Exit Sensitivity:**
   - Vary the mandatory time-exit window across 1, 2, 3, 5, 7, and 10 business days.
   - `research-defined falsification threshold`: If the optimal win rate and PnL peak at horizons > 7 days rather than days 1-2, falsify the microstructure overreaction thesis in favor of generic medium-term drift.

## Crypto portability

- **Portability Status:** `adapted / unproven`.
- **Primary Source Asset Class:** U.S. cash equities and equity call options (Nasdaq 100 constituents and leveraged ETFs `SOXL`, `UPRO`, `DRAM`). No cryptocurrency instruments were tested in the primary source repository.
- **Porting Mechanism to Crypto (`research-proposed`):**
  - **Asset Universe:** Top 30 high-liquidity perpetual futures contracts (e.g., on Binance, Bybit, Hyperliquid) with 30-day ADV > $50M.
  - **Payoff Structure:** Unlike equity markets where retail traders buy single-stock options, crypto options (Deribit) are predominantly concentrated in BTC, ETH, and SOL. For altcoins, the strategy must be ported to **linear perpetual futures** using synthetic convex stops:
    - Long perpetual position entered following an intraday drop > 2.5% (adjusted for crypto baseline higher volatility).
    - Rolling 60-day historical bounce gate: Require >= 80% recovery frequency of >= 70% of drop within 3 days.
    - Risk management: Tight hard stop-loss at -3.0% and staged limit take-profits at +3.0% and +5.0%.
- **Crypto-Specific Frictions & Obstacles:**
  1. *Perpetual Funding Drag:* Severe intraday sell-offs in crypto often trigger extreme funding dislocations. If funding rates turn deeply negative during cascades, long positions collect positive funding; however, if the drop is part of an unhedged basis blow-out, holding perpetuals carries basis divergence risk.
  2. *24/7 Session Discontinuity:* Equity markets have distinct 09:30-16:00 ET sessions where opening liquidity holes occur. Crypto trades continuously; signals must be evaluated on fixed 8-hour or 24-hour UTC rolling snapshots (e.g., 00:00 UTC boundaries).
  3. *Cascading Liquidation Severity:* Equity circuit breakers and limit-up/limit-down bands halt panic selling. In crypto, automated liquidation engines and cross-margin liquidations can drive prices down 15% to 30% in minutes without rebounding for weeks. Catching crypto dips without on-chain liquidation metrics (e.g., CVD divergence or Open Interest flush) carries severe bankruptcy risk.
  4. *Absence of Fundamental Multiple Filters:* Equity P/E ratio guards (`trailing P/E < 140`) cannot be ported directly to tokens without cash flows. A crypto adaptation requires substituting valuation guards with on-chain metrics (e.g., Fully Diluted Valuation / Market Cap ratio < 2.0, or token unlock schedule filters).

## Limitations

- **Source-Assumed Mid-Price Execution:** Primary backtests do not deduct real-world option exchange fees or model bid-ask spread crossing, which could materially lower realized returns.
- **Extreme Bear Market Fragility:** Demonstrated heavy losses in 2022-H2 (-40.53% return, -57.03% drawdown), showing that the strategy remains fundamentally vulnerable to sustained macro sell-offs.
- **High Idiosyncratic Concentration:** Over 40% of 5-year profits originate from just three stocks (`KLAC`, `GILD`, `INSM`), indicating potential sample-selection or survivorship bias.
- **Short-DTE Greeks Decay:** Holding 21-40 DTE call options exposes the strategy to rapid theta decay and implied volatility compression if the rebound does not materialize within 48 hours.
- **Option Liquidity Squeezes:** In market-wide sell-offs, options market makers widen spreads significantly; the 14% maximum entry spread gate may block entries during the very dislocated moments where potential alpha is highest.
- **Not Independently Reproduced:** All figures are third-party source-reported.

## Implementation status

`not-implemented`. This record is a research capture and specification only. No code from this repository has been integrated into NautilusTrader, PyBroker, or our production trading engines, and no live, paper, or testnet trading is authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- The presence of this document in the alpha strategy research repository does not constitute an operational recommendation, proof of profitability, or authorization to trade.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (canonical strategy research specification)
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]` (retail signal gating and falsification frameworks)
- `[[quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]]` (retail liquidity-shock timing and contrarian execution)
- `[[quant/crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]` (liquidity-conditioned short-term reversal in crypto)
- `[[quant/leveraged-etf-closing-rebalance-predatory-trading-reversal-2026-09-03]]` (leveraged ETF structural rebalance reversals)

## Sources

1. **Primary Repository:** GitHub repository `randomwalkhan/Short-Term-Reversal-Strategy`, commit `3194d210a0a4e243825c837ed4791b381831f688`, as-of 2026-09-11 13:32:52 UTC. URL: [https://github.com/randomwalkhan/Short-Term-Reversal-Strategy](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy).
2. **Official Backtest Metrics (Reversal 3.3):** `results/reversal_3_3/reversal_3_3_summary.csv` and `results/reversal_3_3/reversal_3_3_baseline_comparison.csv`. Snapshot window: 2025-04-23 to 2026-04-23. Reversal 3.3 official: +690.85% total return, -26.42% max drawdown, 69.23% win rate (117 trades), Sharpe 4.32 (annualized, rf = 4.23% U.S. 10Y Treasury). Baseline without timing overlay: +1,722.87% return, -48.99% max drawdown, 63.27% win rate (245 trades), Sharpe 4.24.
3. **Universe Selection Ablation (Reversal 2.3.3):** `results/reversal_2_3_3_universe_comparison/reversal_2_3_3_universe_comparison.csv`. Sample window: 2025-03-17 to 2026-03-16. `qqq_only_filtered` (+552.91%, DD -32.46%, SR 2.93), `legacy_watchlist_11` (+81.27%, DD -31.57%, SR 1.18), `qqq_spy_filtered` (+54.38%, DD -43.24%, SR 0.91), `spy_only_filtered` (+36.28%, DD -43.26%, SR 0.73), `nasdaq_spy_filtered` (-7.10%, DD -50.29%, SR 0.23), `nasdaq_only_filtered` (-30.21%, DD -50.51%, SR -0.15).
4. **Factor Selection Ablation (Reversal 2.4):** `results/reversal_2_4_article_variants/reversal_article_variants_summary.csv`. `Window 60d` (+806.11%, DD -30.56%, WR 61.00%, SR 3.41), `Original 2.3.3` (+552.91%, DD -32.46%, WR 59.02%, SR 2.93), `Add Volume` (+364.25%, DD -37.58%, WR 57.32%, SR 2.44), `Window 126d` (+276.80%, DD -38.62%, WR 56.83%, SR 2.18), `Window 252d + Recent Weight` (+181.17%, DD -30.21%, WR 56.31%, SR 1.82), `Kappa / s-score` (+145.58%, DD -29.95%, WR 55.61%, SR 1.61), `PCA Defactored` (+23.89%, DD -42.39%, WR 52.31%, SR 0.60).
5. **Minimum Drop Gate Ablation (Reversal 2.5):** `results/reversal_2_5_min_drop_experiment/reversal_2_5_min_drop_summary.csv`. `min_drop_0.5pct` (+1,305.60%, DD -30.84%, WR 62.08%, SR 3.96) vs `baseline_60d` (+806.11%, DD -30.56%, WR 61.00%, SR 3.41).
6. **Multi-Year Robustness & Subperiod Analysis:** `results/reversal_2_4_overfit/segment_stability.csv` and `results/reversal_2_4_overfit/reversal_2_4_overfit_summary.csv`. Full sample (2021-01-01 to 2026-03-13): +95,158.98% return, -62.41% max drawdown, 56.68% win rate, 1,279 trades. Subperiods: 2021-H1 (+46.56%), 2021-H2 (+191.66%), 2022-H1 (+31.31%), 2022-H2 (-40.53%, DD -57.03%), 2023-H1 (+236.18%), 2023-H2 (+66.12%), 2024-H1 (+59.47%), 2024-H2 (+57.53%), 2025-H1 (+140.17%), 2025-H2 (+380.09%), 2026-H1 (+15.16%).
7. **Ticker PnL Attribution:** `results/reversal_2_4_overfit/ticker_pnl_concentration.csv`. Top earners: KLAC (18.15%), GILD (11.67%), INSM (10.90%), WDC (8.34%), ORLY (7.35%). Top 3 account for 40.72% of cumulative PnL.
8. **Signal Logic & Implementation:** Code files `backtest_reversal_3_1_calls.py`, `backtest_reversal_3_3_calls.py`, `backtest_reversal_3_3_timing_overlay_experiment.py`, `reversal_universe.py`, and `reversal_3_3_live.py` (same repository).
