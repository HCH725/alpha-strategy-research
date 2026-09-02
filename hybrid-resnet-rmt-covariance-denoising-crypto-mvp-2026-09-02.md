---
schema: strategy-research-record-v1
title: "Hybrid ResNet-RMT Covariance Denoising for Cryptocurrency Minimum Variance Portfolios"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - portfolio-optimization
  - covariance-estimation
  - random-matrix-theory
  - deep-learning
  - minimum-variance
  - regime-robust
status: research-only
confidence: medium
source_as_of: 2025-12-26
sources:
  - "Andrés García-Medina, 'Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications', arXiv:2510.19130v2 [q-fin.CP], December 26 2025. https://arxiv.org/abs/2510.19130. DOI: 10.1142/S0129183127500458"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hybrid ResNet-RMT Covariance Denoising for Cryptocurrency Minimum Variance Portfolios

## Provenance

- Paper: arXiv:2510.19130v2 [q-fin.CP], submitted October 21, 2025; revised December 26, 2025.
- Author: Andrés García-Medina, Faculty of Sciences, Autonomous University of Baja California, Ensenada, Mexico.
- Published in: International Journal of Theoretical and Applied Finance (related DOI: 10.1142/S0129183127500458).
- Stable source URLs:
  - https://arxiv.org/abs/2510.19130
  - https://arxiv.org/pdf/2510.19130
- Code/data: Not explicitly linked in the paper; author email provided (acedo@biomemakers.com references a different paper). The ResNet architecture is described in detail in Section 3.2 but no public repository is cited.
- Primary crypto sample: 89 major non-stablecoins by market cap, daily returns from 2020-08-02 to 2025-07-31 (n=1825 observations). Data sourced via yfinance API.
- Training/testing split: Training period ends 2021-11-09 (Bitcoin peak); testing period begins 2021-11-09 through 2025-05-05 (walk-forward).

## Economic mechanism

### Source-reported

The paper argues that empirical covariance matrices estimated from short, noisy, and non-Gaussian financial time series are notoriously unstable. Cryptocurrency returns exhibit heavy tails, abrupt jumps, asymmetry, and complex dynamics that push traditional statistical methods to their limits. The covariance structure of cryptocurrency markets follows approximate power-law scaling (fitted slope α ≈ 0.2), which motivates a power-law covariance model for characterizing collective market dynamics.

The proposed hybrid estimator integrates Random Matrix Theory (RMT) with deep Residual Neural Networks (ResNets):
- RMT component: regularizes the eigenvalue spectrum in high-dimensional noisy settings via nonlinear shrinkage (Ledoit-Péché formula).
- ResNet component: learns data-driven corrections that recover latent structural dependencies encoded in the eigenvectors.

The key insight is that RMT-based Rotationally Invariant Estimators (RIEs) retain sample eigenvectors, which may fail to capture important structural properties of the population covariance matrix due to top eigenvector inconsistency. The hybrid approach explicitly exploits eigenvector information via ResNet while using RMT for eigenvalue estimation.

### Research interpretation

The hypothesized mechanism is that covariance denoising—particularly eigenvector correction via deep learning—improves portfolio risk allocation by better capturing the hierarchical and multiscale interaction structure of cryptocurrency markets. The minimum variance portfolio (MVP+) is used as the allocation strategy, where accurate covariance estimation directly controls portfolio volatility across different market regimes.

Components:
- Covariance estimation: hybrid RMT eigenvalue shrinkage + ResNet eigenvector correction
- Portfolio construction: Minimum Variance Portfolio with no short-selling (MVP+)
- Rebalancing: periodic (182-day rolling windows)

## Signal

### Formation timestamp

- Covariance matrix computed from daily returns over in-sample window (N=182 trading days).
- Portfolio weights computed at each rebalancing date; weights are applied to next-period returns.
- Timezone: data timestamps follow market close (daily frequency).
- Formation is end-of-day; execution assumed next-day open.

### Lookback

- In-sample window: 182 trading days (approximately 9 months).
- Extended training dataset for ResNet: in-sample period plus approximately one additional preceding year (282 days).
- Training data: bull market period ending 2021-11-09.

### Entry

- Long-only minimum variance portfolio weights computed from denoised covariance matrix.
- Weights solved via quadratic programming (QP) with constraint w ≥ 0 and 1⊤w = 1.
- No directional signal; allocation is risk-minimizing.

### Exit

- Portfolio held until next rebalancing date (182-day horizon).
- No stop-loss or take-profit rules.
- Rebalancing occurs at fixed intervals; turnover measures weight changes.

### Holding period

- Maximum and expected holding period: 182 trading days (until next rebalancing).
- Walk-forward analysis: 7 rebalancing points from 2021-11-09 to 2025-05-05.

### Parameters

- In-sample window: 182 days (fixed).
- ResNet architecture: 10 residual blocks, each with CNN layers (64 filters, 3×3 kernel), ReLU activation, skip connections with r=2.
- Training: Adam optimizer, learning rate 10⁻³, MSE loss, batch size 16, 10 epochs, 100 training samples with 20% validation.
- Power-law model parameter: α = 1.5 (simulation); empirical α ≈ 0.2.
- Hierarchical clustering: Average Linkage Clustering Analysis (ALCA) for two-step estimators.
- All parameters are fixed or specified by the method; no hyperparameter tuning reported.

## Required data

- Instrument: 89 major non-stablecoins by market cap (excluding stablecoins, leveraged tokens, and pegged-base pairs).
- Universe: top 400 cryptocurrencies by market cap, filtered to remove coins with >1% missing values, top 10% most volatile excluded, stablecoins excluded (21 coins).
- Venue: Data sourced via yfinance API (likely aggregated from multiple exchanges).
- Market type: Spot prices (daily close).
- Timeframe: Daily returns.
- Fields: Daily close prices (log returns computed).
- Point-in-time: Universe selected based on market cap at time of analysis; survivorship bias possible.
- Timestamp: Daily frequency; timezone not specified (likely UTC or exchange-local).
- Missing-data: Forward-fill imputation for remaining gaps after 1% threshold filtering.
- Funding/fee/spread: Not modeled; transaction costs not included in portfolio performance.

## Execution assumptions

- Signal-to-order timing: End-of-day signal, assumed next-day execution.
- Order type: Market orders (implicit in MVP+ framework).
- Fill model: Perfect fill assumed.
- Fees: Not included in reported results.
- Slippage: Not included in reported results.
- Spread: Not included in reported results.
- Impact: Not modeled.
- Leverage: None (long-only, fully invested).
- Shorting: Not permitted (MVP+ constraint).
- Funding: Not applicable for spot positions.
- Capacity: Not explicitly addressed; universe of 89 coins with daily rebalancing suggests moderate capacity.
- Partial fills/failures: Not addressed.

Source-reported assumptions: The paper does not include transaction costs, slippage, or spread in the walk-forward analysis. The reported cumulative returns are therefore gross of trading costs.

## Evidence

### Source-reported

Walk-forward portfolio performance (MVP+ strategy, 2021-11-09 to 2025-05-05, 7 rebalancing points):

| Estimator | Cumulative Return | Annual Return | Annual Volatility | Sharpe Ratio | Max Drawdown | Turnover |
|-----------|------------------|---------------|-------------------|--------------|--------------|----------|
| Uniform (U) | 0.25 | -33.00% | 66.52% | -0.5 | -84.56% | 0 |
| Naive | 0.88 | -3.66% | 39.10% | -0.09 | -65.63% | 1.02 |
| RMT (Ledoit-Péché) | 0.71 | -9.24% | 43.75% | -0.21 | -73.35% | 1.13 |
| ResNet (ΞCNN) | 1.54 | 13.19% | 46.79% | 0.28 | -63.74% | 1.3 |
| Hybrid (ΞH) | 1.40 | 10.17% | 54.44% | 0.19 | -76.43% | 0 |
| ALCA | 1.09 | 2.46% | 40.71% | 0.06 | -66.24% | 1 |
| Two-step RMT (Ξ2S(LP)) | 0.75 | -7.78% | 43.99% | -0.18 | -73.75% | 1.22 |
| **Two-step CNN (Ξ2S(CNN))** | **1.74** | **17.14%** | **46.60%** | **0.37** | **-63.63%** | **1.34** |
| Two-step Hybrid (Ξ2S(H)) | 1.40 | 10.17% | 54.44% | 0.19 | -76.43% | 0 |

Best performer: Ξ2S(CNN) (two-step CNN-based estimator) achieves highest cumulative return (1.74), highest Sharpe ratio (0.37), and lowest maximum drawdown (-63.63%) among all covariance estimators.

Monte Carlo simulation results (p=100, n=200, 1000 realizations):
- Block-diagonal model: Ξ2S(CNN) best on Frobenius loss; Ξ2S(H) best on minimum-variance loss.
- Nested hierarchical model: ΞCNN best on Frobenius loss; ΞH best on minimum-variance loss.
- Power-law model: No estimator significantly outperforms naive on Frobenius loss; Ξ2S(H) best on minimum-variance loss.

Key finding: As covariance model complexity increases (hierarchical or power-law), hybrid estimators increasingly outperform traditional methods in terms of portfolio risk control (minimum-variance loss).

Cryptocurrency covariance structure: Empirical eigenvalue spectrum displays approximate power-law decay with coefficient α ≈ 0.2, consistent with nested hierarchical and power-law covariance models.

Individual asset comparison (buy & hold, walk-forward):
- Several individual cryptocurrencies outperform all covariance-based portfolio strategies.
- GT-USD: cumulative return 2.90, Sharpe 0.67, max drawdown -62.41%.
- LEO-USD: cumulative return 2.64, Sharpe 0.61, max drawdown -55.67%.

Source reports these results; they have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper notes that covariance estimation primarily affects the orientation of risk (through eigenvector and factor loading modifications) rather than overall volatility level, due to strong market-wide factor dominance in crypto returns.
- Individual buy-and-hold strategies on select cryptocurrencies (e.g., GT-USD, LEO-USD) outperform all covariance-based portfolio strategies, suggesting that asset selection may be more important than covariance estimation quality.
- The hybrid ΞH estimator largely mirrors Bitcoin behavior, reflecting strong alignment with the dominant market mode.
- Transaction costs, slippage, and spread are not included; with turnover of 1.34 for the best estimator, real-world performance would be lower.
- Training on bull market data and testing on bear market is deliberately challenging but still represents a single regime transition; generalization to other regime shifts is untested.
- Survivorship bias: universe selection based on market cap at time of analysis may exclude coins that subsequently failed.

## Falsification plan

1. **Out-of-sample extension**: Test on period beyond 2025-05-05 with fresh data; require Sharpe ratio > 0.1 and maximum drawdown < -70% to maintain hypothesis.
2. **Transaction cost stress**: Add realistic fees (10-20 bps round-trip), slippage (0.5-1% of AUM per trade), and spread; require Sharpe ratio > 0 after costs to maintain hypothesis.
3. **Parameter perturbation**: Vary in-sample window (90, 182, 270 days); require consistent positive Sharpe across windows.
4. **Universe sensitivity**: Test on top-50, top-100, and top-150 coins by market cap; require that best estimator remains ResNet-based or hybrid.
5. **Regime breakdown**: Separate bull (2020-2021), bear (2022), and recovery (2023-2025) subperiods; identify which regimes drive the performance.
6. **Baseline comparison**: Compare against equal-weight portfolio and BTC-only holding; if covariance-based approach underperforms on risk-adjusted basis, hypothesis is weakened.
7. **Capacity limits**: Test with position sizing constraints (max 10% per coin); if performance degrades materially, hypothesis is weakened.
8. **Failure metric**: If Ξ2S(CNN) Sharpe ratio < 0 after transaction costs across full sample, reject the practical alpha hypothesis.

## Crypto portability

**Direct** — the paper is specifically designed for and tested on cryptocurrency markets.

Crypto-specific considerations:
- Universe: 89 non-stablecoin cryptocurrencies from yfinance; actual Binance perpetual/spot universe may differ.
- Market type: Spot daily returns; perpetual futures would introduce funding rate dynamics not modeled.
- 24/7 trading: Daily close timestamps may differ across exchanges; paper uses yfinance aggregation.
- Liquidity: Top 89 coins by market cap are generally liquid, but rebalancing across 89 positions may face slippage on smaller names.
- Survivorship: Universe selected at analysis time; coins that delisted or failed before the study period are excluded.
- Funding: Not applicable for spot; would be relevant for perpetual futures adaptation.
- Exchange fragmentation: yfinance aggregates from multiple venues; actual execution on a single venue may differ.
- Timestamp alignment: Daily close prices may not align across exchanges; paper does not address this.

## Limitations

- **No transaction costs**: Reported returns are gross of fees, slippage, and spread. With turnover of 1.34, costs would materially reduce performance.
- **Survivorship bias**: Universe selected based on market cap at time of analysis; coins that failed or delisted are excluded.
- **Single regime transition**: Training on bull market, testing on bear market is one specific transition; generalization to other regime changes is untested.
- **No code available**: The paper describes the ResNet architecture in detail but does not provide a public repository for replication.
- **Asset selection not integrated**: Individual cryptocurrencies outperform the portfolio strategy, suggesting that covariance estimation quality alone may not be sufficient for alpha generation.
- **Limited universe**: 89 coins is a subset of the broader crypto universe; results may not generalize to smaller, less liquid assets.
- **Walk-forward frequency**: 182-day rebalancing is infrequent; more frequent rebalancing might capture regime changes better but increase costs.
- **Power-law model novelty**: The proposed power-law covariance model is presented for the first time; its theoretical properties and optimality guarantees are not yet established.
- **Market-wide factor dominance**: Crypto returns are dominated by a single market factor, limiting the diversification benefit of covariance-based allocation.

## Implementation status

Not implemented. No code repository is publicly available. The ResNet architecture is described in detail (Section 3.2, Figure 1) but would need to be implemented from scratch. The minimum variance portfolio optimization via quadratic programming is standard and readily implementable.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

The reported Sharpe ratio of 0.37 is source-reported and does not account for transaction costs. Practical viability is uncertain without cost-adjusted validation.

## Related Wiki records

No directly related records found in the repository. Adjacent concepts:
- [[crypto-cross-sectional-volatility-managed-momentum-2026-08-31]] (different mechanism: cross-sectional momentum vs. covariance denoising)
- [[wasserstein-distributional-risk-bounds-covariance-free-portfolio-2026-09-02]] (different approach to portfolio risk management)

## Sources

- Andrés García-Medina, "Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications", arXiv:2510.19130v2 [q-fin.CP], December 26, 2025. https://arxiv.org/abs/2510.19130. DOI: 10.1142/S0129183127500458.
- Submission history: v1 October 21, 2025; v2 December 26, 2025.
- Subjects: Computational Finance (q-fin.CP).
- Code/data: Not publicly available as of source date.
