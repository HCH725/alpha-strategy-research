---
schema: strategy-research-record-v1
title: Equity Cross-Regime Bayesian Optimization XGBoost-TabNet Hybrid Statistical Arbitrage
created: 2026-09-02T07:30:00Z
updated: 2026-09-02T07:30:00Z
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-long-short
  - machine-learning
  - tabular-deep-learning
  - bayesian-optimization
  - regime-switching
status: research-only
confidence: medium
source_as_of: 2026-08-28T00:00:00Z
sources:
  - "Le Grice, J. (2026). Tabular Deep Learning for Algorithmic Trading: Cross-Regime Bayesian Optimisation for Equity Signal Generation. arXiv:2608.27076 [cs.CE, q-fin.TR, q-fin.PM]. https://arxiv.org/abs/2608.27076"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Equity Cross-Regime Bayesian Optimization XGBoost-TabNet Hybrid Statistical Arbitrage

## Provenance

- Canonical source identity: arXiv:2608.27076 (`https://arxiv.org/abs/2608.27076`, `https://arxiv.org/html/2608.27076v1`).
- Author: Joshua Le Grice.
- Primary paper title: *Tabular Deep Learning for Algorithmic Trading: Cross-Regime Bayesian Optimisation for Equity Signal Generation*.
- License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Data sample span: 11 years (2014–2024 for training, regime validation, and Bayesian hyperparameter optimization; strictly held-out full calendar year 2025 for out-of-sample testing).
- Universe: Approximately 300 large-cap US equities (S&P 500 constituents with complete historical records).

## Economic mechanism

### Source-reported
Algorithmic equity forecasting models frequently suffer from regime instability: hyperparameters tuned on a specific market phase (e.g., low-volatility bull runs) overfit local distributions and experience severe out-of-sample degradation when macroeconomic or volatility regimes shift. Furthermore, cross-sectional stock-day tabular data contains heterogeneous combinations of continuous technical price metrics, discrete fundamental balance-sheet variables, and alternative sentiment indicators. While gradient-boosted decision trees (XGBoost) capture hard axis-aligned feature splits, tabular deep learning architectures (TabNet) utilize sequential attention to select salient features soft-sparsely per sample. Combining XGBoost and TabNet via cross-sectional rank aggregation leverages complementary inductive biases, while cross-regime Bayesian hyperparameter optimization explicitly enforces parameter stability across statistically distinct market environments.

### Research interpretation
The strategy is a market-neutral cross-sectional equity long/short alpha strategy. It addresses two primary failure modes of quantitative ML alpha:
1. **Regime Overfitting**: Standard validation optimizes mean loss across an aggregate historical sample, which is dominated by the longest-duration regime. The cross-regime Bayesian objective penalizes configurations with high variance across regime-partitioned validation subsets.
2. **Model Class Monoculture**: GBDT models and attention-based neural networks make uncorrelated ranking errors. Rank-aggregating their predictions cancels out idiosyncratic model noise, increasing the Signal-to-Noise Ratio (SNR) of top and bottom decile selections.

## Signal

1. **Universe & Sampling**:
   - Cross-section of ~300 large-cap US equities.
   - Daily observation frequency with point-in-time constituent alignment.

2. **Feature Space (Multi-Source Tabular Vector)**:
   - **Technical Price/Volume**: Multi-period momentum (5d, 21d, 63d, 252d), ATR volatility, RSI, MACD, Bollinger band widths, volume acceleration, liquidity ratios.
   - **Fundamental Ratios**: Price-to-earnings, enterprise value to EBITDA, return on equity, debt-to-equity, earnings surprises.
   - **Alternative Data**: News sentiment polarity, Google Trends search attention volume shocks, aggregate social sentiment disagreement.

3. **Cross-Regime Partitioning**:
   - Training history (2014–2024) is partitioned into 3 statistically distinct market regimes using K-Means and Kolmogorov-Smirnov distribution shifts over macro indicators (VIX, 10Y Treasury yield changes, index drawdowns).

4. **Cross-Regime Bayesian Hyperparameter Optimization**:
   - Uses Gaussian Process Expected Improvement (GP-EI) Bayesian optimization.
   - The optimization objective targets trading performance (mean Sharpe ratio across all 3 regimes minus a cross-regime dispersion penalty) rather than pure cross-entropy or MSE loss.

5. **Model Architectures**:
   - **Model 1 (XGBoost)**: Gradient-boosted decision trees with depth, shrinkage, sub-sample, and regularization tuned under the cross-regime objective.
   - **Model 2 (TabNet)**: Sparse-attention tabular neural network with sequential decision steps, masking coefficients, and sparsity regularization.

6. **Signal Aggregation & Portfolio Formation**:
   - On each day $t$ after market close:
     - Generate predicted forward 1-day return scores $\hat{y}_{i,t}^{\text{XGB}}$ and $\hat{y}_{i,t}^{\text{TabNet}}$ for each stock $i$.
     - Convert raw prediction scores into normalized cross-sectional percentile ranks: $r_{i,t}^{\text{XGB}} = \text{Rank}(\hat{y}_{i,t}^{\text{XGB}}) / N_t$, $r_{i,t}^{\text{TabNet}} = \text{Rank}(\hat{y}_{i,t}^{\text{TabNet}}) / N_t$.
     - Compute Hybrid ensemble rank: $r_{i,t}^{\text{Hybrid}} = \frac{1}{2}(r_{i,t}^{\text{XGB}} + r_{i,t}^{\text{TabNet}})$.
   - **Long Portfolio**: Top decile ($r_{i,t}^{\text{Hybrid}} \ge 0.90$), equal-weighted or volatility-weighted.
   - **Short Portfolio**: Bottom decile ($r_{i,t}^{\text{Hybrid}} \le 0.10$), equal-weighted or volatility-weighted.
   - Rebalanced daily at $t+1$ market open.

## Required data

- **Universe**: US large-cap equities (~300 names from S&P 500 universe).
- **Price/Volume Data**: Daily OHLCV, corporate action adjusted prices, shares outstanding.
- **Fundamental Data**: Point-in-time quarterly earnings, balance sheet items, filing dates.
- **Alternative Data**: Daily aggregated financial news sentiment scores, web search interest volume indices.
- **Macro/Regime Data**: CBOE VIX, US 10-Year Treasury yields, broad market index returns (SPY).
- **Point-in-Time Integrity**: Fundamental data lagged to actual filing publication dates; alternative sentiment collected strictly before market close.

## Execution assumptions

- **Rebalance Cadence**: Daily rebalancing at market open ($t+1$ open) following signal calculation on $t$ close.
- **Order Types**: Market-on-Open (MOO) or VWAP over the first 15 minutes of the trading session.
- **Transaction Costs & Slippage**: Source evaluates model sensitivity under simulated friction levels; headline baseline includes standard broker commission and borrow fee estimates for large-cap constituents.
- **Shorting / Borrow**: Large-cap universe ensures continuous borrow availability with general collateral (GC) borrow rates.
- **Gross Leverage**: Dollar-neutral long/short (100% long, 100% short, 200% gross exposure).

## Evidence

### Source-reported
- **Evaluation Period**: Held-out 2025 calendar year out-of-sample (OOS) testing.
- **Headline Performance (Hybrid XGBoost + TabNet Ensemble)**:
  - Annualized Return: **51.26%**
  - Sharpe Ratio: **2.44**
  - CAPM Alpha: **0.423** (annualized alpha $42.3\%$, statistically significant with $p = 0.011$).
  - CAPM Beta: **Near-zero** (confirming return is driven by cross-sectional stock selection, not market beta).
- **Quarterly Consistency**: Signal precision remained strictly above the random baseline across all 4 quarters of the 2025 out-of-sample period.
- **Comparison Against Single Architectures**:
  - Standalone Tabular Deep Learning architectures (TabNet, FT-Transformer, SAINT) did not consistently beat tuned XGBoost individually.
  - The Hybrid ensemble outperformed all individual model classes (XGBoost alone, TabNet alone, LightGBM, Random Forest, Linear baseline) across return, Sharpe, and maximum drawdown.
- **Robustness & Noise Stress Testing**:
  - Under Gaussian noise injection into input feature vectors, portfolio performance exhibited graceful degradation up to a well-defined critical threshold before collapsing, demonstrating robust margin boundaries.
- **SHAP Feature Attribution**:
  - Technical and fundamental features accounted for the vast majority of predictive attribution.
  - Alternative data (news sentiment, search attention) contributed approximately 10–12% of total SHAP attribution, with asymmetrical impact providing significantly stronger signal on the short side (detecting deteriorating sentiment / negative shocks) than on the long side.

### Independently reproduced
- Not independently reproduced.

### Negative evidence
- Individual standalone Tabular Deep Learning architectures without ensemble aggregation failed to outperform standard gradient-boosted trees (XGBoost), confirming prior findings (Grinsztajn et al., 2022) that deep tabular models alone offer no automatic advantage over GBDT on financial tabular panels.
- Alternative data provided minimal incremental alpha on long-only signals; its predictive contribution was almost entirely confined to the short leg.
- Computational tuning overhead for cross-regime Bayesian optimization of TabNet is substantial (hours of GPU training vs. minutes for GBDT).

## Falsification plan

1. **Transaction Cost Degradation Curve**: Test net Sharpe ratio under progressive round-trip transaction costs (5 bps, 10 bps, 15 bps, 20 bps) to determine the turnover breakeven threshold.
2. **Alternative Universe Test**: Apply the exact cross-regime Bayesian pipeline to mid-cap and small-cap US equities (Russell 2000) where borrow costs and market impact are significantly higher.
3. **Regime Transition Stress Test**: Simulate high-stress regime transitions (e.g., March 2020 COVID shock, 2022 rate hike drawdown) to verify whether the cross-regime tuned objective prevents catastrophic drawdowns.
4. **Shuffled Rank / Placebo Test**: Randomly permute the TabNet rankings prior to aggregation with XGBoost to verify whether TabNet contributes genuine complementary orthogonal signal or merely acts as a variance regularizer.

## Crypto portability

- **Portability status**: Adapted / unproven.
- **Portability rationale**:
  - Cross-sectional ranking of top 100 liquid crypto tokens (perpetual futures on Binance/Bybit/OKX) using XGBoost + TabNet is directly implementable.
  - Crypto market regimes (e.g., high-vol meme rally, low-vol liquidity drought, liquidation cascades) are more frequent and abrupt than equity regimes, making cross-regime Bayesian hyperparameter tuning potentially highly relevant.
  - Key crypto differences:
    - Fundamental accounting features (P/E, ROE, debt) do not exist for most crypto assets; on-chain metrics (active addresses, TVL, DEX volume, token unlocks) must substitute.
    - Alternative sentiment data (Twitter/X, Telegram sentiment, funding rates, open interest skew) plays a much larger role in crypto price formation than in large-cap US equities.
    - Funding rate drag on perpetual short legs can significantly alter long/short net carry.

## Limitations

- **Universe Restriction**: Tested only on ~300 large-cap US equities with high liquidity.
- **Look-Ahead Sensitivity in Sentiment**: Relies on clean timestamp alignment for alternative sentiment sources.
- **Computational Intensity**: Multi-regime Bayesian optimization over neural architectures requires substantial compute resources.
- **Execution Slippage**: Assumes frictionless opening auction fills; live market impact for daily rebalancing across 60 positions (top/bottom deciles) could degrade net alpha.

## Implementation status

- Not implemented in local research stack (`not-implemented`).
- No NautilusTrader or PyBroker execution actors configured.

## Adoption boundary

- Research-only capture.
- Not approved for paper, testnet, or live trading execution.

## Related Wiki records

- `[[quant/attention-factors-statistical-arbitrage-residual-portfolios-2026-09-02]]`
- `[[quant/crypto-cross-sectional-elastic-net-ctrend-2026-08-31]]`
- `[[quant/crypto-cross-sectional-factor-zoo-iterative-alpha-compression-2026-09-01]]`
- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]`

## Sources

- Le Grice, J. (2026). *Tabular Deep Learning for Algorithmic Trading: Cross-Regime Bayesian Optimisation for Equity Signal Generation*. arXiv preprint arXiv:2608.27076 [cs.CE, q-fin.TR, q-fin.PM]. https://arxiv.org/abs/2608.27076
