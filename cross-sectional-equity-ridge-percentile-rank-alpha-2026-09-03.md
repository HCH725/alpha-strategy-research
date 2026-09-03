---
schema: strategy-research-record-v1
title: "Cross-Sectional Regularized Linear Equity Alpha via Out-of-Sample Percentile Ranking"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - cross-sectional
  - machine-learning
  - ridge-regression
  - information-coefficient
  - walk-forward
  - tree-ensembles
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-02
sources:
  - "https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/tree/38f38fd8530826442b001b301130004dcb461785"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Regularized Linear Equity Alpha via Out-of-Sample Percentile Ranking

## Provenance

- **Primary Source:** Divyansh Gupta, *Cross-Sectional Machine Learning Alpha Strategy*, public GitHub repository `Divyansh-Gupta01/cross-sectional-ml-alpha`.
- **Repository URL:** `https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha`
- **Immutable Commit SHA:** `38f38fd8530826442b001b301130004dcb461785` (committed 2026-09-02T15:21:22Z).
- **Exact File Paths:**
  - Data ingestion and liquidity audit: [`src/data_pipeline.py`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/src/data_pipeline.py)
  - Feature engineering and cross-sectional ranking: [`src/features.py`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/src/features.py)
  - Model pipelines and walk-forward training: [`src/models.py`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/src/models.py)
  - Portfolio backtest and execution engine: [`src/backtest.py`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/src/backtest.py)
  - Statistical metrics and permutation testing: [`src/metrics.py`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/src/metrics.py)
  - Validation reports and trade logs:
    - [`outputs/reports/backtest_summary.csv`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/outputs/reports/backtest_summary.csv)
    - [`outputs/reports/overall_ic_summary.csv`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/outputs/reports/overall_ic_summary.csv)
    - [`outputs/reports/fold_ic_breakdown.csv`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/outputs/reports/fold_ic_breakdown.csv)
    - [`outputs/reports/fold_backtest_breakdown.csv`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/outputs/reports/fold_backtest_breakdown.csv)
    - [`outputs/reports/feature_importance.csv`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/outputs/reports/feature_importance.csv)
    - [`outputs/reports/trade_log_headline.csv`](https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha/blob/38f38fd8530826442b001b301130004dcb461785/outputs/reports/trade_log_headline.csv)
- **Source As-Of:** 2026-09-02.
- **Deduplication Audit:** Repository-wide audit confirms zero existing records for `Divyansh-Gupta01`, `cross-sectional-ml-alpha`, or this specific 462-equity walk-forward regularized linear ranking implementation. Existing cross-sectional records in this repository (`cross-sectional-crypto-momentum-2026-08-31.md`, `cross-market-alpha191-double-selection-lasso-2026-09-02.md`, `lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02.md`, `strata-selective-state-space-intraday-raw-bars-cross-sectional-ranking-2026-09-02.md`) address fundamentally distinct universes, mathematical architectures, or asset classes.

## Economic mechanism

### Source-reported

1. **Cross-Sectional Breadth vs. Small-Sample Noise:** Time-series machine learning models trained on small universes (e.g., 20 assets) frequently suffer from small-sample overfitting, yielding out-of-sample Information Coefficients (IC) near zero and failing against random selection baselines. Expanding the cross-sectional universe to liquid S&P 500 equities provides statistical power ($>10^6$ observation rows across 462 tickers) to separate relative value and short-to-medium-term momentum from macroeconomic noise.
2. **Linear Regularization vs. Tree Ensemble Failure in Cross-Sectional Ranking:** Decision tree ensembles (Random Forest and Gradient Boosted Trees) split greedily on the features providing the largest variance reduction. When presented with a mix of stock-specific cross-sectional ranks and market-wide macro indicators (e.g., benchmark volatility and distance from 200-day SMA), tree models allocate $>89\%$ of split importance to market-wide variables. Because market-wide variables are identical across all stocks on any given day, tree models fail to differentiate cross-sectional relative performance, resulting in negative out-of-sample rank ICs. In contrast, an L2-regularized linear model (Ridge Regression) distributes weights smoothly across standardized percentile rank features, preventing macro regime variables from drowning out relative ranking signals.

### Research interpretation

This is an equity cross-sectional factor-selection and relative-value alpha model operating on an intermediate holding horizon (20 trading days).

The core falsifiable hypothesis is: **In a broad, liquid equity universe, cross-sectional percentile normalization of multi-horizon momentum, price-to-moving-average distance, volatility, and volume dynamics provides persistent relative-ranking alpha when estimated via an L2-regularized linear model that penalizes coefficient concentration, whereas nonlinear tree ensembles overfit to market-wide regime covariates and destroy cross-sectional predictive ranking.**

Key mechanism characteristics:
- **Momentum Persistence & Volatility Scaling:** Intermediate price trends (20d, 60d return ranks) combined with inverse volatility weighting capture risk-adjusted momentum continuation.
- **Mean Reversion in Extremes:** Normalized distance from 20-day and 50-day moving averages (`rank_dist_sma20`, `rank_dist_sma50`) and 20-day z-scores act as short-term mean-reversion counterweights.
- **Failure Mode Demarcation:** The model captures relative equity outperformance, but because it executes as a long-only cash portfolio, it inherits broad market beta risk (maximum drawdown of -42.86% during broad equity downturns).

## Signal

The strategy uses an expanding-window walk-forward pipeline to predict forward 20-trading-day returns and construct a daily top-ranked long portfolio.

### 1. Feature Construction Pipeline (Daily at Day $T$ Close)

For each active stock $i$ on trading day $T$, raw technical indicators are calculated from daily OHLCV bars:
- **Multi-Horizon Returns:** 
  $$\text{return\_kd}_{i,T} = \frac{\text{Close}_{i,T} - \text{Close}_{i,T-k}}{\text{Close}_{i,T-k}}, \quad k \in \{5, 10, 20, 60\}$$
- **Moving Average Distance & Z-Score:**
  $$\text{dist\_smaK}_{i,T} = \frac{\text{Close}_{i,T}}{\text{SMA}_K(\text{Close}_{i,T})} - 1, \quad K \in \{20, 50, 200\}$$
  $$\text{zscore\_20d}_{i,T} = \frac{\text{Close}_{i,T} - \text{SMA}_{20}(\text{Close}_{i,T})}{\sigma_{20}(\text{Close}_{i,T}) + 10^{-8}}$$
- **Momentum & Volatility Indicators:**
  - 14-day exponential Wilder RSI (`rsi_14d`).
  - Annualized 20-day and 60-day realized volatility: $\sigma_w \times \sqrt{252}$, $w \in \{20, 60\}$.
  - 14-day Average True Range as a percentage of price: $\text{ATR\%}_{i,T} = \frac{\text{ATR}_{14}(\text{High}, \text{Low}, \text{Close})_{i,T}}{\text{Close}_{i,T}} \times 100$.
- **Volume Dynamics:**
  - 20-day relative volume: $\text{rel\_volume\_20d}_{i,T} = \frac{\text{Volume}_{i,T}}{\text{SMA}_{20}(\text{Volume}_{i,T}) + 10^{-6}}$.
  - 20-day normalized On-Balance Volume (OBV) momentum:
    $$\text{obv\_momentum\_20d}_{i,T} = \frac{\text{OBV}_{i,T} - \text{OBV}_{i,T-20}}{\sum_{j=0}^{19} \text{Volume}_{i,T-j} + 10^{-6}}$$
- **Macro Market Features (from SPY benchmark):**
  - SPY 5d, 20d, 60d returns (`market_return_5d`, `market_return_20d`, `market_return_60d`).
  - SPY 20d realized volatility (`market_volatility_20d`).
  - SPY distance from 200d SMA (`market_dist_sma200`).
- **Cross-Sectional Percentile Normalization:**
  On each date $T$, all stock-level features are converted to cross-sectional percentile ranks across the active universe:
  $$\text{rank\_feat}_{i,T} = \frac{\text{Rank}(\text{feat}_{i,T})}{\max_j \text{Rank}(\text{feat}_{j,T})} \in (0.0, 1.0]$$
- **Sector-Relative & Interaction Features:**
  - Sector-relative 20d return: $\text{sector\_rel\_return\_20d}_{i,T} = \text{return\_20d}_{i,T} - \frac{1}{|S_i|} \sum_{j \in S_i} \text{return\_20d}_{j,T}$, then percentile-ranked across the entire active universe (`rank_sector_rel_return_20d`).
  - Momentum-volatility interaction: $\text{interaction\_mom\_x\_vol}_{i,T} = \text{rank\_return\_20d}_{i,T} \times (1.0 - \text{rank\_volatility\_20d}_{i,T})$.
  - Reversal-volume interaction: $\text{interaction\_rev\_x\_vol}_{i,T} = \text{rank\_zscore\_20d}_{i,T} \times \text{rank\_rel\_volume\_20d}_{i,T}$.

Total active feature vector contains 22 variables (14 stock percentile ranks, 5 market macro variables, 1 sector-relative rank, and 2 interaction terms).

### 2. Labeling & Target Return

- **Signal Timestamp:** Computed at Day $T$ close using data strictly available through Day $T$.
- **Execution Timestamp:** Trade entered at Day $T+1$ open.
- **Exit Timestamp:** Trade closed at Day $T+21$ close.
- **Continuous Target Return:**
  $$y_{i,T} = \frac{\text{Close}_{i,T+21} - \text{Open}_{i,T+1}}{\text{Open}_{i,T+1}}$$

### 3. Model Architecture & Training Protocol

- **Model:** Scikit-learn Pipeline with `StandardScaler` followed by L2-regularized `Ridge` regression.
- **Hyperparameter Optimization:** `RidgeCV` with candidate $\alpha \in \{0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0\}$.
- **Walk-Forward Validation:** 5 expanding chronological folds spanning 1,791 out-of-sample trading days (October 2017 – November 2024).
- **Purging & Embargo:** 10-trading-day embargo between training split and out-of-sample test split to prevent leakage from overlapping rolling window features. No future data shuffling.

### 4. Portfolio Construction & Order Logic

- **Selection Timing:** At Day $T$ close, predict $\hat{y}_{i,T}$ for all active stocks. Rank candidates by descending $\hat{y}_{i,T}$.
- **Eligible Candidates:** Exclude assets currently held in the portfolio.
- **Daily Quota:** Select top $N = 3$ unheld candidates.
- **Position Allocation:** Allocate up to $10\%$ of current total capital per position ($10$ maximum concurrent open positions). Minimum allocation threshold: $\$1,000$.
- **Order Execution:** Submit market-on-open buy orders for execution at Day $T+1$ open.
- **Holding Period & Exit:** Positions are held for exactly 20 trading days (`days_held >= 20`) and liquidated at market close on Day $T+21$.

## Required data

- **Universe:** Liquid constituents of the S&P 500 index evaluated from 2015-01-01 to 2024-12-31.
  - Initial pool: 503 S&P 500 company listings + SPY ETF benchmark.
  - Liquidity Filter: Median Average Daily Dollar Volume ($\text{ADV} = \text{Close} \times \text{Volume}$) $\ge \$10,000,000$.
  - Historical Completeness: Minimum $90\%$ valid trading days over the 10-year period ($2,263$ out of $2,515$ days).
  - Final Clean Universe: 462 stocks (1,059,416 total feature rows). Exactly 41 tickers dropped due to recent IPO/spin-off history (e.g., ABNB, COIN, CRWD, DASH, DDOG, DELL) or low ADV (ECHO), fully logged in `data/processed/dropped_tickers_log.csv`.
- **Benchmark:** SPY (SPDR S&P 500 ETF Trust) daily OHLCV.
- **Timeframe:** Daily OHLCV bars.
- **Fields Required:** `Open`, `High`, `Low`, `Close`, `Volume`.
- **Corporate Actions:** Prices adjusted for splits; volume unadjusted.
- **Missing Data Handling:** Strict dropping of tickers failing 90% history threshold; zero imputation of missing prices. Any non-positive price print ($P \le 0$) triggers ticker exclusion.

## Execution assumptions

### Source-reported

- **Order Types:** Market-on-Open (MOO) for entries at Day $T+1$ open; Market-on-Close (MOC) for exits at Day $T+21$ close.
- **Transaction Costs & Slippage:**
  - Commission fee: 5 bps per side ($0.05\%$).
  - Execution slippage: 5 bps per side ($0.05\%$).
  - Total friction: 10 bps per side, equivalent to 20 bps ($0.20\%$) completed round-trip friction.
- **Capital & Leverage:**
  - Base capital: $\$100,000.00$.
  - No leverage ($1.0\times$ long-only cash account).
  - Minimum trade allocation: $\$1,000.00$.
  - Maximum concurrent positions: 10 positions (10% capital ceiling per asset).
- **Shorting / Borrow:** None (long-only).
- **Cash Management:** Uninvested cash remains idle (0% risk-free interest assumed).

### Research interpretation

- **Realistic Liquidity:** The 462 equities all have median daily dollar volume $\ge \$10\text{M}$, so 10% positions ($\sim \$10,000\text{--}\$30,000$) represent $<0.1\%$ of daily volume, making 5 bps slippage conservative and realistic.
- **Auction Execution:** Entering at Open and exiting at Close aligns with official NYSE/Nasdaq opening and closing crosses, minimizing intraday timing discretion.
- **Survivorship Bias Consideration:** S&P 500 constituents were selected based on recent membership rather than point-in-time index composition, introducing mild survivorship bias.

## Evidence

### Source-reported

All metrics below are reported directly from Divyansh Gupta (`Divyansh-Gupta01/cross-sectional-ml-alpha`, commit `38f38fd8530826442b001b301130004dcb461785`, files `outputs/reports/overall_ic_summary.csv`, `outputs/reports/fold_ic_breakdown.csv`, `outputs/reports/backtest_summary.csv`, `outputs/reports/fold_backtest_breakdown.csv`, and `outputs/reports/trade_log_headline.csv`):

#### 1. Daily Information Coefficient (Spearman Rank IC across 1,791 Out-of-Sample Trading Days)

$$\text{IC}_t = \text{Corr}_{\text{Spearman}}(\hat{y}_{i,t}, y_{i,t})$$

| Model | Mean Daily IC | IC Std | Annualized ICIR | t-statistic | p-value | Permutation p-value (500 runs) | Positive IC % |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ridge Regression (Headline)** | **+0.0294** | **0.1979** | **2.361** | **6.295** | **< 0.00001** | **0.000** | **53.8%** |
| Random Forest (Classifier) | -0.0046 | 0.1661 | -0.438 | -1.167 | 0.24329 | 0.236 | 50.2% |
| HistGradientBoosting (Regressor) | -0.0099 | 0.1766 | -0.891 | -2.376 | 0.01761 | 0.016 | 44.7% |

#### 2. Fold-by-Fold Ridge IC Consistency

| Fold | Test Period | Ridge Mean IC | Ridge ICIR | n Trading Days |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 2017-10-17 to 2019-03-21 | +0.0108 | 0.97 | 358 |
| 2 | 2019-03-22 to 2020-08-20 | +0.0350 | 2.77 | 358 |
| 3 | 2020-08-21 to 2022-01-21 | +0.0492 | 3.79 | 358 |
| 4 | 2022-01-24 to 2023-06-27 | +0.0515 | 3.46 | 358 |
| 5 | 2023-06-28 to 2024-11-27 | +0.0008 | 0.08 | 359 |

#### 3. Portfolio Backtest Summary (2017–2024, Net of 20 bps Round-Trip Costs)

| Strategy / Benchmark | CAGR | Sharpe Ratio | Sortino Ratio | Ann. Vol | Max Drawdown | Profit Factor | Daily Win Rate | Ending Capital ($100k Base) | Total Trades |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ridge Regression (Headline)** | **17.11%** | **0.667** | **0.057** | **30.85%** | **-42.86%** | **1.127** | **53.7%** | **$307,348.44** | **890** |
| SPY Buy-and-Hold Benchmark | 12.73% | 0.717 | 0.055 | 19.33% | -34.10% | 1.147 | 55.1% | $234,403.26 | N/A |
| HistGradientBoosting | 18.63% | 0.662 | 0.058 | 35.09% | -48.79% | 1.128 | 54.1% | $336,852.45 | 890 |
| Random Forest Classifier | 10.90% | 0.551 | 0.044 | 24.06% | -33.48% | 1.115 | 53.1% | $208,675.43 | 890 |
| Random Control Baseline (100 Seeds) | 9.73% $\pm$ 3.31% (Max: 16.52%) | 0.543 $\pm$ 0.142 (Max: 0.836) | 0.682 $\pm$ 0.181 | — | -38.78% $\pm$ 4.09% | — | — | $186,410.12$ (Mean) | — |

*Statistical significance note:* Ridge CAGR ($17.11\%$) exceeds the 100th percentile of the 100-seed random portfolio distribution (maximum random CAGR was $16.52\%$). Ridge Sharpe ($0.667$) ranks in the 79th percentile of random allocations.

#### 4. Fold-by-Fold Portfolio Performance Breakdown

| Fold | Period | Ridge CAGR | Ridge Sharpe | Ridge Max DD | SPY CAGR | SPY Sharpe | SPY Max DD | Outperformance |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 2017-10-17 to 2019-03-21 | 8.56% | 0.477 | -28.18% | 7.93% | 0.571 | -20.18% | +0.63% |
| 2 | 2019-03-22 to 2020-08-20 | 38.07% | 1.025 | -35.52% | 14.45% | 0.622 | -34.10% | +23.62% |
| 3 | 2020-08-21 to 2022-01-21 | 7.86% | 0.434 | -23.70% | 19.64% | 1.292 | -9.80% | -11.78% |
| 4 | 2022-01-24 to 2023-06-27 | 13.73% | 0.533 | -27.71% | -0.59% | 0.082 | -22.75% | **+14.32% (Bear Mkt Alpha)** |
| 5 | 2023-06-28 to 2024-11-27 | 20.35% | 0.855 | -19.21% | 24.87% | 1.888 | -10.29% | -4.52% |

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Failure of Nonlinear Tree Models for Cross-Sectional Ranking:**
   - Both Random Forest (mean IC $-0.0046$, $t = -1.167$, $p = 0.243$) and HistGradientBoosting (mean IC $-0.0099$, $t = -2.376$, $p = 0.0176$) produce statistically insignificant or significantly negative out-of-sample Spearman rank ICs.
   - Analysis of split feature importances (`outputs/reports/feature_importance.csv`) reveals that Random Forest concentrates $89.1\%$ of its total split importance on 5 market-wide macro indicators:
     - `market_volatility_20d`: $22.91\%$
     - `market_dist_sma200`: $21.84\%$
     - `market_return_60d`: $19.58\%$
     - `market_return_20d`: $13.98\%$
     - `market_return_5d`: $10.80\%$
   - Individual stock cross-sectional ranks receive trivial importance ($<1.2\%$ each, e.g., `rank_dist_sma200` $1.18\%$, `rank_return_60d` $1.04\%$). Because market features are invariant across stocks on any given day, tree models fail to differentiate cross-sectional relative performance.
2. **Substantial Beta Drawdown Exposure:**
   - Ridge strategy suffered a maximum drawdown of $-42.86\%$, which is deeper than the SPY benchmark's $-34.10\%$. Because the portfolio holds long-only equities without cash hedging or short overlays, it absorbs market beta shocks.
3. **Decay of IC in Fold 5:**
   - In Fold 5 (2023-06-28 to 2024-11-27), Ridge daily IC collapsed to $+0.0008$ (ICIR $0.08$), indicating that the signal experienced severe alpha decay or was dominated by mega-cap market concentration (e.g., "Magnificent Seven" rally) where cross-sectional rank dispersion was compressed.
4. **Survivorship Bias in Constituent Pool:**
   - As disclosed by the author, selecting 2024 S&P 500 constituents introduces survivorship bias into 2015–2020 training and backtests by excluding companies that were removed from the index due to bankruptcy or acquisition.

## Falsification plan

1. **Survivorship-Free Point-in-Time Universe Audit:** Re-run the data ingestion and 5-fold walk-forward pipeline using historical point-in-time S&P 500 constituent lists (e.g., CRSP or Compustat survivorship-free data) where historical membership dynamically updates on rebalancing dates. **Falsification threshold:** If mean daily IC falls below $+0.010$ or annualized ICIR falls below $1.0$ ($t < 2.0$), reject the strategy as an artifact of survivorship bias.
2. **Macro Feature Ablation Test:** Train Ridge and Random Forest models strictly on the 14 cross-sectional percentile rank features, removing all 5 SPY macro features (`market_*`). **Falsification threshold:** If Random Forest fails to achieve a positive rank IC ($IC \le 0$) even after removing macro confounding features, reject the hypothesis that macro feature domination is the sole driver of tree ensemble failure in cross-sectional ranking.
3. **Transaction Cost Stress Test:** Increase completed round-trip trading friction from 20 bps ($5+5$ bps per side) to 40 bps ($10+10$) and 60 bps ($15+15$). **Falsification threshold:** If net CAGR drops below the SPY benchmark ($12.73\%$) at $30\text{ bps}$ round-trip costs, classify the strategy as a cost-fragile turnover artifact.
4. **Execution Timing Delay Test:** Shift execution from Day $T+1$ Open to Day $T+1$ VWAP or Day $T+1$ Close (testing a 1-day execution lag). **Falsification threshold:** If 1-day execution delay erodes more than $50\%$ of the out-of-sample IC, reject the execution robustness of the signal.
5. **Cross-Sectional Shuffled Null Control:** On each date $T$, randomly permute predicted scores across tickers while maintaining identical portfolio position-sizing and holding rules. **Falsification threshold:** If the unshuffled Ridge strategy cannot beat the 95th percentile of 500 shuffled trials on CAGR and Sharpe, reject skill over random selection.

## Crypto portability

- **Portability:** `adapted` / `unproven`
- **Porting Rationale:** The core concept of cross-sectional ranking on multi-horizon momentum, moving average distances, and volume dynamics can be mathematically ported to liquid cryptocurrency perpetual futures (e.g., top 50–100 altcoin perps by open interest and volume on Binance/OKX/Hyperliquid).
- **Crypto-Specific Frictions & Obstacles:**
  1. *Perpetual Funding Rate Drag:* Holding a multi-week ($20\text{-day}$) long basket in crypto perpetuals incurs continuous 8-hour funding rates. In bull regimes, funding costs typically average $10\%\text{--}30\%$ APR, severely penalizing cash-equity-style holding periods.
  2. *Absence of Fixed Market Open/Close Crosses:* Crypto trades continuously 24/7 without opening/closing auctions. Slippage on volatile altcoins can easily exceed 20–50 bps during liquidity dislocations.
  3. *Extreme Cross-Asset Correlation:* During market-wide liquidations, cross-sectional dispersion collapses as BTC beta dominates $>80\%$ of altcoin return variance, degrading relative-value rankings.
  4. *Rapid Universe Churn & Delistings:* Crypto tokens experience high attrition, listing obsolescence, and sudden liquidity dry-ups far exceeding S&P 500 constituent replacement.

## Limitations

- **Survivorship Bias:** The universe is constructed from modern (2024) S&P 500 constituents rather than true point-in-time historical constituent records.
- **Unhedged Equity Beta:** The portfolio is 100% long-only equities, causing deep drawdowns ($-42.86\%$) during macroeconomic bear markets.
- **High Turnover / Position Drag:** Holding 10 slots with 20-day holding periods generates 890 trades over 7 years, incurring substantial cumulative transaction costs ($\sim 178\%$ in gross friction).
- **Alpha Decay in Later Period:** Fold 5 (2023–2024) showed an IC of only $+0.0008$, suggesting potential decay or regime sensitivity during periods of high index concentration.
- **Not Independently Reproduced.**

## Implementation status

No implementation has been conducted in PyBroker, NautilusTrader, paper trading, testnet, or live trading environments. This document represents an upstream research capture of Divyansh Gupta's public repository code and reports.

## Adoption boundary

- `status: research-only`
- `implementation_status: not-implemented`
- `adoption: not-approved`
- `approval_scope: research-only`

This document is a research capture for intake review. It does not authorize capital allocation, live deployment, strategy pipeline integration, or execution on any account.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Framework for purging, embargo, and walk-forward validation protocols.
- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]` — Modeling fee, slippage, and execution delay hurdles on gross factor returns.
- `[[quant/phase10-universe-lifecycle-survivorship-2026-08-28]]` — Point-in-time universe construction and survivorship bias mitigation.
- `[[cross-sectional-crypto-momentum-2026-08-31]]` — Cross-sectional momentum dynamics in crypto assets.
- `[[lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]]` — Cross-sectional reversal and sector relative value models.

## Sources

1. Divyansh Gupta (2026), *Cross-Sectional Machine Learning Alpha Strategy*, public GitHub repository `Divyansh-Gupta01/cross-sectional-ml-alpha`.
   - Repository URL: `https://github.com/Divyansh-Gupta01/cross-sectional-ml-alpha`
   - Full Commit SHA: `38f38fd8530826442b001b301130004dcb461785`
   - As-of Date: 2026-09-02.
2. Marco Lopez de Prado (2018), *Advances in Financial Machine Learning*, John Wiley & Sons (reference for triple-barrier labeling and walk-forward embargo protocols).
3. Andrew W. Lo and A. Craig MacKinlay (1990), *When Are Contrarian Profits Due to Stock Market Overreaction?*, The Review of Financial Studies, 3(2), 175–205 (cross-sectional lead-lag and interaction foundations).
