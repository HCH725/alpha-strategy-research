---
schema: strategy-research-record-v1
title: Cointegration-Screened Crypto Perpetual Pairs Trading with Kalman-Filter Dynamic Hedge Ratios and Cross-Asset Falsification
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - pairs-trading
  - statistical-arbitrage
  - kalman-filter
  - cointegration
  - crypto-perpetuals
  - cross-asset
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-06
sources:
  - "https://github.com/kolyamkl/crypto-statarb/tree/560730eee89bff30eb548432da76a197fcd5dc25"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cointegration-Screened Crypto Perpetual Pairs Trading with Kalman-Filter Dynamic Hedge Ratios and Cross-Asset Falsification

## Provenance

- **Primary Repository:** GitHub repository `kolyamkl/crypto-statarb`
- **Canonical Source Identity:** GitHub repository `kolyamkl/crypto-statarb` at immutable commit `560730eee89bff30eb548432da76a197fcd5dc25`.
- **Commit Date / As-Of:** 2026-09-06 20:51:44 UTC (`feat(M10): equity replication — the three-hypothesis verdicts`).
- **Author:** Mykola "Kolya" Maklakov (`kolyamkl`).
- **Primary Source Code & Report Paths Inspected Directly:**
  - `README.md`: End-to-end methodology summary, headline in-sample vs. out-of-sample results, automated walk-forward performance, robustness diagnostics, and equity cross-asset comparison.
  - `SPEC.md`: Detailed research protocol, milestone definitions (M1 to M10), look-ahead guards, and accounting invariants.
  - `DECISIONS.md`: Methodology decision log (22,480 characters) tracking non-obvious choices: 2024-12-31 train/test split, log-price Engle–Granger screening, Kalman filter formulation, innovation spread dynamics, funding event joins, degenerate hedge guards, and equity replication design.
  - `config.yaml`: Authoritative parameter configuration for Binance USDT-M perpetual futures (data, pairs, signals, backtest, validation, robustness).
  - `config_equities.yaml`: Authoritative parameter configuration for the pre-registered US equities replication.
  - `src/pairs/cointegration.py`: Engle–Granger two-step cointegration screening across both regression directions using MacKinnon critical values; AR(1) half-life estimation.
  - `src/pairs/kalman.py`: One-sided causal Kalman filter estimating dynamic time-varying state vector `[alpha_t, beta_t]` with OLS warm-up on burn-in window.
  - `src/signals/spread.py`: Causal innovation spread construction (`spread_t = y_t - (alpha_{t-1} + beta_{t-1} * x_t)`) and rolling window z-score normalization.
  - `src/signals/rules.py`: State-machine signal generator (`enter_z`, `exit_z`, `stop_z`), negative-beta entry cancellation guard, and post-flat re-arm guard.
  - `src/backtest/engine.py`: Single-pair vectorised arithmetic backtest engine enforcing next-bar open execution, frozen entry beta, and unit gross capital.
  - `src/backtest/funding.py`: Exact timestamp-matching join for historical 8-hour funding events from Binance premium-index data.
  - `reports/m2_pair_screen.md`: Full 91-pair Engle–Granger cointegration ranked screening table on training data (2021-01-01 to 2024-12-31).
  - `reports/m4_backtest.md`: Initial M4 training backtest results highlighting the Kalman whitening / self-arbitrage problem.
  - `reports/m5_validation.md`: 72-configuration parameter grid search on training data and 15-fold rolling quarterly walk-forward out-of-sample evaluation.
  - `reports/m6_metrics.md`: Definitive performance metrics table covering train, untouched test, walk-forward, per-pair breakdowns, and buy-and-hold benchmarks.
  - `reports/m7_robustness.md`: Post-hoc stress tables evaluating cost sensitivity, parameter sensitivity, leave-one-pair-out attribution, market regime slices, and rolling cointegration stability.
  - `reports/m7_failure_analysis.md`: Detailed qualitative and quantitative autopsy of seven empirical failure modes and structural limitations.
  - `reports/m10_crossasset.md`: Pre-registered replication report evaluating 24 US large-cap equities (276 pairs) across three formal hypotheses (prevalence, stability, profitability).
- **Source Quality:** High-rigor open-source quantitative research study featuring complete look-ahead unit test coverage (58 tests with mutate-the-future assertions), strict data-snooping controls, deterministic SQLite/Postgres data pipelines, explicit transaction friction decomposition, and unsparing empirical falsification reporting.

## Economic mechanism

### Source-reported

The author formulates the pairs trading hypothesis around pairwise statistical cointegration and dynamic equilibrium tracking in cryptocurrency perpetual futures:
1. **Pairwise Cointegration vs. Correlation:** High return correlation (0.44 to 0.85 among crypto majors) does not imply a bound on price spread divergence. Cointegration establishes that a linear combination of log prices forms a stationary process with mean-reverting residuals, providing an economic anchor for statistical arbitrage.
2. **Adaptive Equilibrium via Dynamic Hedge Ratios:** Fixed OLS hedge ratios assume stationary relationship parameters over multi-year horizons, which fails during structural crypto market regime shifts. A one-sided Kalman filter models the hedge ratio `beta_t` as a random walk, adapting to slow baseline drift without leaking future information.
3. **Trading Transitory Innovation Dislocations:** The traded object is the Kalman filter prediction error (innovation) — today's log price of asset y minus the expected price conditional on today's log price of asset x evaluated using yesterday's filtered state `[alpha_{t-1}, beta_{t-1}]`. Because the Kalman state absorbs slow structural trends, the innovation isolates high-frequency microstructural supply-demand imbalances that revert in hours rather than months.
4. **Frictional Realism:** Edge in crypto statistical arbitrage is constrained by taker fees (5 bps VIP0 on Binance), bid-ask spread crossing and slippage (2 bps), and perpetual funding payments. The strategy explicitly incorporates these friction channels into the signal design and backtest accounting.

### Research interpretation

This research provides a benchmark empirical falsification of naive pairs trading in cryptocurrency markets:
1. **The Kalman Whitening Dilemma (Self-Arbitrage):** A well-calibrated Kalman filter produces white noise innovations by mathematical construction. When the state noise parameter is set to standard responsive levels (`delta = 1e-5`), the filter rapidly absorbs mean-reverting deviations into `alpha_t` and `beta_t`, leaving an innovation series with near-zero predictable autocorrelation. Slowing the filter 100-fold (`delta = 1e-7`) leaves tradeable mean reversion in the residual, but this parameter tuning occupies an extremely narrow empirical band discovered through training search.
2. **Human Selection Bias vs. Algorithmic Pipeline:** While the curated 3-pair book achieved +4.00% net return in the untouched test window, a fully automated pipeline executing quarterly re-screening and re-tuning on a rolling 2-year window lost -30.16% out-of-sample over 3.5 years. The apparent edge did not reside in the automated statistical engine, but in the author's subjective human selection of economically plausible pairs (alt-L1 substitutes) and a post-hoc relaxation of half-life constraints.
3. **Pseudo-Market Neutrality and Sector Factor Beta:** Although each pair is dollar-hedged return-neutral at trade entry, portfolio PnL is strongly conditioned on aggregate crypto market drift: netting +11.52% in trailing BTC-up regimes and losing -7.15% in trailing BTC-down regimes. In crypto markets, altcoin pairwise mean reversion holds when the broader sector grinds upward, but breaks down completely during collective market-wide liquidations.
4. **Episodic Cointegration as a Structural Obstacle:** Rolling 1-year Engle–Granger tests reveal that cointegration is not a persistent asset-pair property, but an episodic phenomenon holding in only 5% to 11% of rolling annual windows. Long-window screens capture historical averaging artifacts rather than stable stationary relations.

## Signal

### Universe Selection & Cointegration Screen (Source-Reported)

1. **Eligible Symbol Universe:**
   14 liquid USDT-margined perpetual futures on Binance: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `AVAXUSDT`, `NEARUSDT`, `ADAUSDT`, `DOTUSDT`, `ATOMUSDT`, `LINKUSDT`, `LTCUSDT`, `BCHUSDT`, `DOGEUSDT`, `ARBUSDT`, `OPUSDT`. Total pairwise combinations: 14 * 13 / 2 = 91 pairs.
2. **Screening Sample Window:**
   Training data only, strictly up to 2024-12-31 (34,343 hourly bars per continuous symbol).
3. **Engle–Granger Cointegration Gate:**
   - Evaluated on log perpetual close prices: y_t = ln(P_{y,t}), x_t = ln(P_{x,t}).
   - Tested symmetrically in both regression directions (y ~ x and x ~ y) using `statsmodels.tsa.stattools.coint`.
   - Screened on the **worse (maximum) p-value** of the two directions using MacKinnon asymptotic critical values:
     eg_p_max = max(p_{y ~ x}, p_{x ~ y}) < 0.05
4. **Half-Life Tradeability Filter:**
   - Residual mean reversion speed estimated via an AR(1) specification on OLS residuals:
     Delta e_t = -lambda * e_{t-1} + epsilon_t
     half-life = -ln(2) / ln(1 - lambda)
   - Pre-registered tradeability bounds: 24 <= half-life <= 720 hourly bars (1 to 30 calendar days). Fast mean reversion (<24h) cannot overcome 1-hour bar execution frictions; slow mean reversion (>30d) locks up capital and weakens the stat-arb premise.
5. **Screening Outcome:**
   Only 1 out of 91 pairs passed both gates strictly on training data: `AVAXUSDT ~ NEARUSDT` (p = 0.0021, half-life 663h / 27.6d, OLS beta = 0.856, return correlation 0.64).
6. **Curated Trading Book (Source-Reported):**
   To achieve minimum portfolio diversification, the author documented a post-hoc relaxation of the upper half-life bound from 30d to ~70d, approving a 3-pair book:
   - Pair 1: `AVAXUSDT ~ NEARUSDT` (p = 0.0021, half-life 663h / ~27.6d, beta = 0.856, clean pass)
   - Pair 2: `ADAUSDT ~ DOTUSDT` (p = 0.0486, half-life 1220h / ~50.8d, beta = 0.806, relaxed half-life)
   - Pair 3: `ADAUSDT ~ LTCUSDT` (p = 0.0240, half-life 1580h / ~65.8d, beta = 1.170, relaxed half-life)

### Dynamic Hedge Ratio & Kalman Filter (Source-Reported)

1. **State-Space Formulation:**
   - Observation equation:
     y_t = [1, x_t] * [alpha_t, beta_t]^T + e_t, where e_t ~ N(0, R)
   - State transition equation (random walk):
     alpha_t = alpha_{t-1} + w_{alpha,t}
     beta_t = beta_{t-1} + w_{beta,t}
     where w_t ~ N(0, Q)
2. **Noise Covariance Calibration (Chan Single-Knob Parameterization):**
   - State noise covariance:
     Q = (delta / (1 - delta)) * I_2
   - Observation noise variance R: Initialized from OLS residual variance on the burn-in window: R = s_OLS^2.
   - Burn-in warm-up: 720 hourly bars (30 days) seeded by OLS on the initial window. Burn-in bars receive no filtered estimate and are strictly untradeable.
   - Parameter grid search: delta in {1.0e-5, 1.0e-7, 1.0e-8}. Promoted frozen parameter on training data: delta = 1.0e-7.
3. **Causality & Look-Ahead Protection:**
   The filter is strictly one-sided (no Kalman smoothing). Filtered state at time t uses observations up to and including t only. Unit tests assert causality by mutating future observations and verifying bit-identical prior state outputs.

### Innovation Spread Construction & Normalization (Source-Reported)

1. **Causal Innovation Calculation:**
   The traded spread is defined as the 1-step-ahead Kalman prediction error using the **lagged** state vector known at bar t-1:
   spread_t = y_t - (alpha_{t-1} + beta_{t-1} * x_t)
   *Rationale:* Using state filtered at t would absorb bar t price move into alpha_t and beta_t, shrinking the very dislocation targeted for trading.
2. **Rolling Z-Score Normalization:**
   mu_t = (1 / W) * sum_{i=0}^{W-1} spread_{t-i}
   sigma_t = sqrt((1 / (W - 1)) * sum_{i=0}^{W-1} (spread_{t-i} - mu_t)^2)
   z_t = (spread_t - mu_t) / sigma_t
   - Rolling window W = 720 hourly bars (30 days), selected via training grid search from {720, 1440}.
   - Full window required (`min_periods = 720`); initial warm-up bars evaluate to NaN.

### Trade Entry, Exit, and Risk Rules (Source-Reported)

1. **Position State Machine:**
   Position s_t in {+1, -1, 0} in units of the spread (where +1 = long y, short beta*x; -1 = short y, long beta*x; 0 = flat):
   - **Long Entry (s_t = +1):** Triggered when z_t <= -entry_z (spread is cheap).
   - **Short Entry (s_t = -1):** Triggered when z_t >= +entry_z (spread is rich).
   - **Promoted Parameter:** entry_z = 2.5 (grid search across {1.5, 2.0, 2.5}).
2. **Degenerate Hedge Guard (`cancel_entries_without_positive_beta`):**
   If the lagged Kalman hedge ratio at the entry decision bar satisfies beta_{t-1} <= 0, the entire trade episode is cancelled (s_t = 0). A non-positive beta implies a long-long synthetic asset rather than a market-neutral pair. Mid-trade beta fluctuations do not abort established positions.
3. **Mean-Reversion Take-Profit Exit:**
   - Active long positions (s_{t-1} = +1) exit to flat (s_t = 0) when z_t >= -exit_z.
   - Active short positions (s_{t-1} = -1) exit to flat (s_t = 0) when z_t <= +exit_z.
   - **Promoted Parameter:** exit_z = 0.5 (grid search across {0.0, 0.5}). Exiting at 0.5 captures the majority of mean reversion while avoiding prolonged holding periods around the mean.
4. **Structural Dislocation Stop-Loss Exit:**
   - Any active position exits immediately to flat (s_t = 0) when |z_t| >= stop_z.
   - **Promoted Parameter:** stop_z = 4.0 (grid search across {3.0, 4.0}). Divergence beyond 4 standard deviations signals that cointegration has broken down.
5. **Re-Arm Guard:**
   Following any transition to flat (whether via mean reversion exit or stop-loss), new entries are blocked until |z_t| returns strictly inside the entry threshold band (|z_t| < entry_z = 2.5). Without this guard, a position stopped out at z = 4.1 would immediately re-enter on the next bar if z remained above 2.5, continually re-buying an accelerating structural breakout.

### Position Sizing and Portfolio Construction (Source-Reported)

1. **Per-Pair Unit Gross Capital Allocation:**
   When active, each pair deploys unit gross capital (1.0), allocated return-neutral across legs:
   w_{y,t} = s_t / (1 + beta_entry)
   w_{x,t} = -s_t * beta_entry / (1 + beta_entry)
   where |w_{y,t}| + |w_{x,t}| = 1.0 (for beta > 0).
2. **Frozen Beta at Entry:**
   The hedge ratio beta_entry is locked at the trade entry fill bar and remains constant throughout the holding episode. Dynamic bar-by-bar rebalancing is eliminated to prevent churn turnover costs.
3. **Equal-Weighted Portfolio Book:**
   Total portfolio capital (1.0) is divided equally across the active book pairs. Unallocated capital earns zero interest.

## Required data

- **Asset Universe:** 14 Binance USDT-margined perpetual futures (`BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `AVAXUSDT`, `NEARUSDT`, `ADAUSDT`, `DOTUSDT`, `ATOMUSDT`, `LINKUSDT`, `LTCUSDT`, `BCHUSDT`, `DOGEUSDT`, `ARBUSDT`, `OPUSDT`).
- **Data Vendor / Exchange:** Binance USD(S)-M Futures REST API (`/fapi/v1/klines`, `/fapi/v1/fundingRate`, `/fapi/v1/premiumIndex`).
- **Timeframe & Bar Aggregation:** 1-hour OHLCV klines. Candle boundaries aligned to top-of-hour UTC (`00:00`, `01:00`, etc.).
- **Price Fields:** Perpetual close price (P_{y,t}, P_{x,t}) for signal generation and mark-to-market; perpetual open price of next bar (P_{t+1}^open) for execution fills.
- **Funding Data:** Historical 8-hour funding rates (`fundingRate`, `fundingTime`). Joined by exact event timestamp (stored in PostgreSQL/SQLite `funding` table); never approximated by an idealized 8-hour grid.
- **Point-in-Time Discipline:** Ingestion strictly drops the currently forming bar whose close time exceeds the run timestamp. Lookback windows operate strictly on historical closed candles.
- **Data Continuity:** Zero interior gaps observed across 646,101 hourly bars (2021-01-01 to 2026-07-10). Newer listings (`OPUSDT` listed 2022-06, `ARBUSDT` listed 2023-03) start at their recorded onboarding dates without backfilling.

## Execution assumptions

- **Execution Model (Source-Reported):** Next-bar open fill (`desired.shift(1)`). Signal decided at the close of bar t; order filled at the open of bar t+1. In 24/7 perpetual futures, P_{t+1}^open approx P_t^close to within microstructure noise.
- **Taker Fee (Source-Reported):** 5.0 bps (0.05%) per leg per side (Binance VIP0 standard taker schedule).
- **Slippage Model (Source-Reported):** 2.0 bps per leg per fill applied to all entries and exits.
- **Round-Trip Friction per Leg (Source-Reported):** 2 * (5.0 + 2.0) = 14.0 bps. For a two-leg unit pair, total round-trip friction is approximately 28 bps weighted across legs (~14 bps of total deployed pair capital).
- **Funding Fee Treatment (Source-Reported):** Exact funding debit/credit applied when holding a position across a funding timestamp:
  funding_pnl_t = -sum_{i in {y, x}} w_{i,t} * funding_rate_{i,t}
- **Margin & Leverage (Source-Reported):** 1x leverage assumed on unit capital. Intrabar liquidation, margin calls, and maintenance margin constraints are not modeled.
- **Borrow / Shorting Friction (Source-Reported):** No external borrow fee; short perpetual exposure is sustained entirely through negative/positive funding cash flows.
- **Accounting Framework (Source-Reported):** Arithmetic PnL on constant unit capital (no geometric compounding):
  net_pnl = gross_pnl - fees - slippage + funding
  Drawdowns represent cumulative sums of per-bar arithmetic returns from peak equity.
- **Execution Fill Model for Research Stack (`research-proposed`):** When porting to NautilusTrader, execution should evaluate both taker limit orders with crossing prices and passive maker quotes (`PostOnly`) inside the bid-ask spread to test whether the strategy survives under maker rebate tiers.

## Evidence

### Source-reported

All metrics and statistics below trace directly to the primary research repository `kolyamkl/crypto-statarb` (commit `560730eee89bff30eb548432da76a197fcd5dc25`), evaluated across `reports/m4_backtest.md`, `reports/m5_validation.md`, `reports/m6_metrics.md`, `reports/m7_robustness.md`, and `reports/m10_crossasset.md`.

#### 1. Curated 3-Pair Book: Static Train/Test Split Performance

- **Configuration:** delta = 1.0e-7, W = 720 bars, entry_z = 2.5, exit_z = 0.5, stop_z = 4.0.
- **Training Window:** 2021-01-01 to 2024-12-31 (34,343 hourly bars / 4.0 years).
- **Test Window (Untouched):** 2025-01-01 to 2026-07-10 (13,363 hourly bars / ~1.5 years).

| Series / Asset | Net PnL | Gross PnL | Costs | Sharpe | Sortino | Max DD | Hit Rate | Avg Hold | Turnover/Yr | Exposure |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Strategy — Train (Tuned)** | **+30.81%** | +41.18% | 10.90% | **+0.59** | +0.80 | -18.73% | 60% | 85h | 39.7x | 46% |
| **Strategy — Test (Untouched)** | **+4.00%** | +7.91% | 4.15% | **+0.27** | +0.38 | -16.90% | 60% | 98h | 38.9x | 51% |
| **Strategy — Walk-Forward OOS** | **-30.16%** | — | — | **-0.69** | -0.88 | -47.06% | — | — | — | — |
| `BTCUSDT` Buy-and-Hold (Train) | +173.38% | +173.38% | 0.00% | +0.73 | +1.02 | -125.87% | — | — | — | 100% |
| `BTCUSDT` Buy-and-Hold (Test) | -22.90% | -22.90% | 0.00% | -0.33 | -0.46 | -69.35% | — | — | — | 100% |
| `ETHUSDT` Buy-and-Hold (Train) | +206.17% | +206.17% | 0.00% | +0.68 | +0.95 | -145.04% | — | — | — | 100% |
| `ETHUSDT` Buy-and-Hold (Test) | -25.10% | -25.10% | 0.00% | -0.24 | -0.33 | -102.02% | — | — | — | 100% |

#### 2. Per-Pair Breakdown in Untouched Test Window (2025-01-01 to 2026-07-10)

| Pair (y ~ x) | Net PnL | Gross PnL | Costs | Sharpe | Sortino | Max DD | Hit Rate | Avg Hold | Turnover/Yr | Exposure |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `AVAXUSDT ~ NEARUSDT` | +3.85% | +8.43% | 4.62% | +0.16 | +0.22 | -24.25% | 65% | 91h | 43.3x | 23% |
| `ADAUSDT ~ DOTUSDT` | -4.32% | -0.83% | 4.06% | -0.20 | -0.27 | -20.56% | 59% | 124h | 38.0x | 27% |
| `ADAUSDT ~ LTCUSDT` | +12.46% | +16.13% | 3.78% | +0.50 | +0.71 | -14.52% | 56% | 79h | 35.4x | 16% |

#### 3. Fully-Automated Walk-Forward Validation (2023-01-01 to 2026-07-10)

- Re-screens 91 pairs and re-tunes 72-config grid quarterly on rolling 17,520-bar (2y) windows; trades next 2,160 bars (1 quarter) untouched.
- 15 total quarterly folds: 12 traded, 3 held 100% cash (no pairs passed cointegration and trade-count floors in 2025-Q1, 2025-Q2, 2025-Q3).
- Stitched out-of-sample result: **Net -30.16%, Sharpe -0.69, Sortino -0.88, Max DD -47.06% over 24,427 bars**.
- Worst quarterly fold: 2024-09-22 (`DOGEUSDT ~ NEARUSDT`), netting -15.12% (Sharpe -2.24) due to shorting DOGE during the November 2024 meme rally.

#### 4. Pre-Registered US Equities Replication (M10 Cross-Asset Study)

- Evaluated on 24 US large caps (276 pairs, daily bars 2021–2026, identical train/test split, mechanical top-3 rule: `MA~V`, `MA~AVGO`, `MA~NVDA`).
- **Prevalence (H1):** 13/276 pairs passed (4.7%) vs. crypto's 1/91 (1.1%), but ~13.8 passes were expected by chance; neither market beats its multiple-testing base rate.
- **Stability (H2):** Refuted. Rolling 1-year cointegration pass rates were 0% to 4% for equities vs. 5% to 11% for crypto. Cointegration was more episodic in equities.
- **Profitability (H3):** Equities test net was +13.7% (Sharpe +1.02, max DD -6.0%), but Spearman rank correlation between train and test Sharpe was -0.30; 97% of configs were positive OOS (broad equity market tailwind); the only economically sound pair (`MA~V`) lost -3.7% while tech momentum pairs printed; SPY buy-and-hold beat the equity book risk-adjusted (+1.11 vs +1.02). Automated walk-forward earned +3.3% (Sharpe +0.12).

### Independently reproduced

`not independently reproduced`. All metrics, equity series, and diagnostic tables represent primary research outputs reported by Mykola Maklakov in GitHub repository `kolyamkl/crypto-statarb` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). No internal simulation has been run in our stack.

### Negative evidence

The primary source explicitly details seven empirical failure modes and diagnostic stresses:
1. **Kalman Filter Self-Arbitrage / Whitening:** In the initial M4 backtest with standard responsive state noise (delta = 1.0e-5), the portfolio lost -36.54% net (gross -1.49%, fees 25.43%, slippage 10.17%, funding +0.55%). The adaptive state absorbed the mean-reverting dislocation into `alpha_t` and `beta_t`, producing near-white innovation residuals with no predictive edge.
2. **Automated Pipeline Collapse:** Replacing human pair curation with automated quarterly re-screening produced -30.16% cumulative losses out-of-sample, demonstrating that the algorithmic pipeline cannot generate sustainable statistical arbitrage without human intervention.
3. **Extreme Single-Pair Concentration:** In leave-one-pair-out testing on the untouched test window:
   - Excluding `ADAUSDT ~ LTCUSDT`: Test net PnL collapses from +4.00% to **-0.24%** (Sharpe -0.01).
   - Excluding `ADAUSDT ~ DOTUSDT`: Test net PnL doubles to **+8.15%** (Sharpe +0.46).
   - Excluding `AVAXUSDT ~ NEARUSDT`: Test net PnL is **+4.07%** (Sharpe +0.23).
   The entire positive out-of-sample performance was generated by a single pair (`ADA/LTC`) during a single quarter (Q1-2025).
4. **Severe Fee & Friction Fragility:** Post-hoc cost stress testing reveals that the strategy edge completely dissolves under modest fee increases:
   - 0.5x costs: Net PnL +6.07%, Sharpe +0.42
   - 1.0x costs (baseline): Net PnL +4.00%, Sharpe +0.27
   - **2.0x costs: Net PnL -0.16%, Sharpe -0.01 (Edge Dies)**
   - 3.0x costs: Net PnL -4.31%, Sharpe -0.30
   At ~39x annual portfolio turnover and ~14 bps capital cost per round trip, transaction frictions consume ~4% to 5% of portfolio equity annually, roughly matching the entire gross edge.
5. **Parameter Tuning Ineffectiveness:** Spearman rank correlation between in-sample training Sharpe and out-of-sample test Sharpe across all 72 grid configurations was **+0.10** (statistically indistinguishable from zero). The single best-performing test config (Sharpe +0.85) had a negative Sharpe on training data.
6. **Failure of Sector Factor Market-Neutrality:** In regime slicing based on trailing 30-day BTC returns:
   - BTC Trending Up: Net PnL **+11.52%**, Sharpe **+2.14** (5,909 bars)
   - BTC Trending Down: Net PnL **-7.15%**, Sharpe **-0.85** (6,734 bars)
   - High Volatility: Net PnL +3.59%, Sharpe +0.46 (6,321 bars)
   - Low Volatility: Net PnL +0.77%, Sharpe +0.13 (6,322 bars)
   The book suffers severe losses during market downturns because altcoin cointegration breaks during market-wide sell-offs.
7. **Episodic Cointegration Decoherence:** Rolling 1-year Engle–Granger tests show that the book pairs pass the 5% significance threshold in only 5% to 11% of rolling windows across 2022–2026:
   - `ADAUSDT ~ DOTUSDT`: 11% of windows pass
   - `ADAUSDT ~ LTCUSDT`: 9% of windows pass
   - `AVAXUSDT ~ NEARUSDT`: 5% of windows pass

## Falsification plan

1. **Maker Order Rebate and Spread Crossing Friction Audit:**
   - *Test:* Re-run the backtest across the untouched test window replacing taker execution (5 bps taker + 2 bps slippage) with passive maker quotes inside the spread (+1 bps maker rebate or 0 bps fee, 0 bps slippage), and alternatively with punitive taker market orders (7 bps taker + 5 bps slippage).
   - `research-defined falsification threshold`: If the strategy cannot achieve a net Sharpe >= 1.0 under passive maker execution, or if net return degrades to less than -5.0% under a 2-bps increase in slippage, reject the hypothesis that bilateral crypto perpetual pairs trading is commercially viable under standard VIP0 exchange fee tiers.
2. **Orthogonalized Crypto Sector Beta Neutralization:**
   - *Test:* Regress each pair synthetic spread returns against rolling 30-day BTC and ETH returns, and enter trades only when the residual spread is orthogonal to the crypto market factor (|beta_{spread, BTC}| < 0.15).
   - `research-defined falsification threshold`: If market-orthogonalized spread trading reduces the test-window Sharpe below 0.00 or yields a negative return in BTC-up regimes, reject the hypothesis that the strategy extracts idiosyncratic pairwise mean reversion and accept that historical profits were merely disguised long crypto market beta.
3. **Cross-Exchange Execution on Hyperliquid L1:**
   - *Test:* Re-run the pair screening and backtest on 1-hour OHLCV and 1-hour funding data from Hyperliquid DEX perpetuals (2023 to 2026).
   - `research-defined falsification threshold`: If zero pairs pass the Engle–Granger screen (p < 0.05) or if net PnL across matching pairs is negative on Hyperliquid data, reject exchange-invariant cointegration and classify the findings as Binance-specific order book or funding artifacts.
4. **Random Pair Permutation Placebo Test:**
   - *Test:* Construct 1,000 synthetic pseudo-pairs by randomly pairing non-cointegrated tokens from the Binance perp universe and running the identical Kalman filter and z-score trading rules.
   - `research-defined falsification threshold`: If the curated book test Sharpe (+0.27) falls below the 80th percentile of the randomized pseudo-pair distribution, reject the claim that Engle–Granger cointegration screening provides statistically significant predictive value over random pairing.
5. **Walk-Forward In-Sample Ranking Falsification:**
   - *Test:* Measure the rank correlation between in-sample Sharpe and out-of-sample Sharpe on an expanded 20-pair universe across 20 quarterly walk-forward folds.
   - `research-defined falsification threshold`: If the mean Spearman rank correlation across folds remains < 0.15, falsify the assumption that historical backtest optimization carries actionable predictive information for crypto pairs trading parameter selection.

## Crypto portability

- **Portability Status:** `direct`.
- **Natively Researched Asset Class:** Cryptocurrency USDT-margined perpetual futures on Binance. The primary study was constructed, backtested, and diagnosed directly on crypto perpetual contracts.
- **Cross-Asset Replication:** The author pre-registered and executed an identical replication pipeline on US cash equities (`M10`), demonstrating that the failure of automated cointegration screening to deliver sustainable out-of-sample alpha is an invariant cross-asset market reality.
- **Crypto-Specific Market Frictions:**
  1. *Perpetual Funding Rate Dynamics:* Unlike cash equities with fixed borrow fees, perpetual swaps transfer funding every 8 hours (Binance) or 1 hour (Hyperliquid). In a hedged pair, funding can act as an unpredictable drag if one leg incurs persistent positive funding while the short leg does not offset it. Empirical evidence from M4 indicates funding net impact was mild (+0.53% over 4 years on a hedged book), but during stress periods (e.g., FTX collapse in November 2022), funding interval spikes (e.g., SOLUSDT funding every 2 hours) introduce severe tail risk.
  2. *24/7 Continuous Trading & Execution Discontinuity:* Crypto markets trade continuously without opening/closing auctions. Next-bar open execution closely matches prior close, but weekend liquidity dry-ups and sudden liquidation cascades can cause extreme slippage exceeding the assumed 2 bps.
  3. *Exchange-Level De-Peg and Insolvency Risk:* Pairs trading across altcoins assumes that collateral and quoting currencies maintain stable parity. Holding large bilateral perp positions introduces platform exposure to Binance cross-margin liquidation algorithms and auto-deleveraging (ADL) events during extreme volatility.

## Limitations

- **Complete Dependence on Human Curation:** The automated walk-forward pipeline generated a disastrous -30.16% return; the positive +4.00% test result was entirely dependent on human pair selection and post-hoc relaxation of screening rules.
- **Extreme Single-Pair Concentration:** Over 100% of out-of-sample profits stemmed from `ADA/LTC` in Q1-2025; removing this single pair leaves the strategy net negative (-0.24%).
- **Fee Death Threshold at 2x Costs:** At taker fees of 5 bps and slippage of 2 bps, the strategy pays 4% to 5% of capital per year in frictions; doubling fees turns the net return negative (-0.16%), making the edge commercially unviable without maker rebate status.
- **Failure of Dollar Neutrality During Market Sell-Offs:** The strategy lost -7.15% during BTC-down regimes, proving that bilateral dollar hedging does not protect against market-wide crypto liquidity crashes.
- **Episodic Cointegration:** Cointegration holds in only 5% to 11% of rolling 1-year windows, violating the fundamental premise of a stationary equilibrium.
- **Absence of Intrabar Stop-Loss Modeling:** 1-hour bar backtests cannot detect intrabar 3-sigma flash crashes, understating realized maximum drawdowns.
- **Survivorship Bias:** The universe was selected from currently active Binance perpetual symbols; delisted tokens were not tracked in historical screens.
- **Not Independently Reproduced:** All performance figures reflect third-party author backtests and empirical diagnostics.

## Implementation status

`not-implemented`. This document represents a research capture and empirical falsification analysis. No code from `crypto-statarb` has been integrated into `nautilus-quant-system`, PyBroker, or NautilusTrader, and no live, paper, or testnet execution is authorized.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- The presence of this record in the repository serves as definitive negative research and falsification evidence regarding classical bilateral cointegration pairs trading on crypto perpetuals. It does not authorize strategy implementation or live capital deployment.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (canonical strategy research specification)
- `[[quant/crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]` (crypto cross-sectional reversal and liquidity filters)
- `[[quant/partial-information-regime-filtering-ddpg-ornstein-uhlenbeck-pairs-trading-2026-09-05]]` (regime-filtering continuous-time pairs trading)
- `[[quant/path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03]]` (path signature lead-lag pair trading)
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` (crypto microstructure signal falsification)
- `[[quant/simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11]]` (dynamic multi-asset portfolio optimization)

## Sources

1. **Primary Research Repository:** Mykola Maklakov (`kolyamkl`). *"crypto-statarb: A cross-asset statistical-arbitrage research study — crypto perpetual futures, then a pre-registered replication on US equities"*, GitHub repository `kolyamkl/crypto-statarb`, commit `560730eee89bff30eb548432da76a197fcd5dc25`, dated 2026-09-06 20:51:44 UTC. URL: [https://github.com/kolyamkl/crypto-statarb](https://github.com/kolyamkl/crypto-statarb).
2. **Project Specification & Methodology Protocol:** `SPEC.md` and `DECISIONS.md` in `kolyamkl/crypto-statarb` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). Documenting Engle–Granger cointegration screening on log prices, half-life bounds [24, 720] hours, one-sided causal Kalman filtering, lagged state innovation spread, next-bar open fill execution, Binance VIP0 taker fee (5.0 bps) + slippage (2.0 bps), and exact funding joins.
3. **M2 Cointegration Screening Table:** `reports/m2_pair_screen.md` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). Screening 91 pairs across 14 Binance perp symbols on 2021-01-01 to 2024-12-31 data: `AVAXUSDT ~ NEARUSDT` (p=0.0021, HL 663h / 27.6d, OLS beta=0.856), `ADAUSDT ~ LTCUSDT` (p=0.0240, HL 1580h / 65.8d, OLS beta=1.170), `ADAUSDT ~ DOTUSDT` (p=0.0486, HL 1220h / 50.8d, OLS beta=0.806).
4. **M4 Initial Training Backtest & Whitening Diagnosis:** `reports/m4_backtest.md` and `reports/m4_backtest_notes.md` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). Fast filter delta=1.0e-5 backtest: Portfolio gross -1.49%, fees 25.43%, slippage 10.17%, funding +0.55%, net -36.54%.
5. **M5 Validation Grid & Walk-Forward:** `reports/m5_validation.md` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). 72-config grid tuning on training data: promoted config `ParamSet(delta=1e-07, zscore_window_bars=720, entry_z=2.5, exit_z=0.5, stop_z=4.0)` delivering train net +30.81%, Sharpe +0.59, 234 trades. 15-fold rolling quarterly walk-forward delivering stitched OOS net -30.16%, Sharpe -0.69.
6. **M6 Comprehensive Metrics & Benchmarks:** `reports/m6_metrics.md` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). Untouched test window (2025-01-01 to 2026-07-10): Strategy net +4.00%, gross +7.91%, costs 4.15%, Sharpe +0.27, Sortino +0.38, max DD -16.90%, hit rate 60%, avg hold 98h, turnover 38.9x/yr, exposure 51%. Benchmark BTCUSDT: -22.90%, Sharpe -0.33, max DD -69.35%. Benchmark ETHUSDT: -25.10%, Sharpe -0.24, max DD -102.02%. Per-pair test results: AVAX~NEAR (+3.85%, SR +0.16), ADA~DOT (-4.32%, SR -0.20), ADA~LTC (+12.46%, SR +0.50).
7. **M7 Robustness & Stress Testing:** `reports/m7_robustness.md` and `reports/m7_failure_analysis.md` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). Fee stress (0.5x: +6.07% / SR +0.42; 1x: +4.00% / SR +0.27; 2x: -0.16% / SR -0.01; 3x: -4.31% / SR -0.30). Grid Spearman train-test rank correlation: +0.10. Leave-one-pair-out: without ADA/LTC net PnL is -0.24%. Market regime slices: BTC-up net +11.52% / SR +2.14 vs. BTC-down net -7.15% / SR -0.85. Rolling 1-year Engle–Granger pass rates: 5% to 11%.
8. **M10 US Equities Cross-Asset Replication:** `M10_PLAN.md` and `reports/m10_crossasset.md` (commit `560730eee89bff30eb548432da76a197fcd5dc25`). 24 large-cap equities (276 pairs): 13/276 passed screen (4.7%); rolling 1y EG pass rates 0% to 4%; test net +13.7%, Sharpe +1.02, max DD -6.0%; grid rank correlation -0.30; automated walk-forward +3.3%, Sharpe +0.12.
