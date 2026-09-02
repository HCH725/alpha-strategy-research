---
schema: strategy-research-record-v1
title: "Small-Cap Alpha-Beta Separation and Uncertainty-Aware Portfolio Allocation: Integrating Multimodal LLM News Sentiment, Macroeconomic Indicators, and Technical Signals"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - small-cap
  - large-language-models
  - financial-news-sentiment
  - macroeconomic-regimes
  - uncertainty-quantification
  - portfolio-optimization
  - risk-parity
  - lead-lag
status: research-only
confidence: medium
source_as_of: 2026-08-12
sources:
  - "Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, and Arman Khaledian, 'Large Language Model-Driven Small-Capitalization Trading: Integrating Financial News Sentiment, Macroeconomic Indicators, and Technical Signals', arXiv:2608.12283v1 [q-fin.PM, cs.AI, cs.LG], August 12, 2026. https://arxiv.org/abs/2608.12283. DOI: https://doi.org/10.48550/arXiv.2608.12283"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Small-Cap Alpha-Beta Separation and Uncertainty-Aware Portfolio Allocation: Integrating Multimodal LLM News Sentiment, Macroeconomic Indicators, and Technical Signals

## Provenance

- Canonical Source: arXiv:2608.12283v1 [q-fin.PM, cs.AI, cs.LG], submitted August 12, 2026.
- Authors: Alireza Kargarzadeh (Tailstate Intelligence Ltd.), Nariman Khaledian (Independent Researcher), Navid Parvini (Zanista AI Ltd.), Arman Khaledian (Zanista AI Ltd.).
- DOI: https://doi.org/10.48550/arXiv.2608.12283
- Stable Source URLs:
  - Abstract: https://arxiv.org/abs/2608.12283
  - HTML Full Text: https://arxiv.org/html/2608.12283v1
  - PDF: https://arxiv.org/pdf/2608.12283
- Dataset & Sample:
  - Asset Universe: Russell 2000 small-capitalization equities traded in US markets.
  - Daily OHLCV Data: October 2, 2023 through December 31, 2025.
  - Scored Financial News Feed: October 1, 2023 through December 31, 2025.
  - Exogenous Macro-Indicator Panel: 58 series (50 Yahoo Finance daily market series spanning 11 GICS sector ETFs, index futures, rates, commodities, crypto; and 8 FRED macroeconomic releases: GDP, inflation, unemployment, capacity utilization, consumer confidence, housing starts, building permits, and federal funds rate) spanning January 1, 2022 through January 1, 2026.
  - Partitioning Protocol: In-sample model training, feature standardization, and early stopping strictly restricted to the period ending December 31, 2024. Out-of-sample evaluation conducted across the entire 2025 calendar year (252 trading days). A strict embargo of at least $H$ trading days is enforced between training, validation, and test splits to eliminate forward overlap leakage.

## Economic mechanism

### Source-reported

Small-capitalization equities are subject to structural informational frictions: they receive sparse analyst coverage, exhibit lower liquidity, and react with noticeable friction to macroeconomic developments compared to large-cap equities. The authors propose three foundational mechanisms:

1. **Information Propagation and Lead-Lag Asymmetry**: Liquid macro-beta indicators and sector benchmarks reprice instantly upon macroeconomic releases. Small-cap equities reprice with a measurable lag. By decomposing trading triggers into a "pure-beta" leg (macro indicator fires before the small-cap stock itself reacts) and a "pure-alpha" leg (small-cap stock exhibits an extreme abnormal move not explained by macro indicators), researchers can isolate lead-lag spillover from idiosyncratic earnings and news drift. Requiring both channels to fire simultaneously ("beta intersection") discards the asymmetric timing advantage that creates the trading opportunity.
2. **De-biasing and Contextual News Processing**: Standard financial sentiment lexicons miss negation, linguistic nuance, and entity attribution. LLMs (evaluated across GPT-4o mini, FinBERT, Mistral-7B, and Llama-3-8B) capture contextual polarity. To convert raw LLM scores into tradable signals without overfitting, scores are subjected to entity-prior correction, shrinkage toward group medians, embedding-space deduplication, and centroid representative selection.
3. **Uncertainty-Aware Portfolio Construction**: Traditional machine learning strategies predict conditional expected returns $\\hat{\\mu}_t$ and either plug them into static sample covariance matrices or apply heuristic position sizing. In contrast, this pipeline jointly predicts the conditional return vector $\\hat{\\mu}_t$ and the conditional covariance matrix $\\hat{\\Sigma}_t$, decomposing total predictive uncertainty into:
   - **Aleatoric uncertainty** ($\\hat{\\Sigma}^A_t$): inherent market noise, modeled via the covariance output head under a Multivariate Normal or heavy-tailed Multivariate Student-$t$ negative log-likelihood loss;
   - **Epistemic uncertainty** ($\\hat{\\Sigma}^E_t$): model parameter and specification uncertainty, quantified via Monte Carlo dropout over $M$ stochastic forward passes.
   The combined predictive covariance $\\hat{\\Sigma}_t = \\hat{\\Sigma}^A_t + \\hat{\\Sigma}^E_t$ is injected directly into the quadratic risk terms of constrained portfolio allocators (Mean-Variance, Black-Litterman, Bayesian Black-Litterman, Risk Parity, and Hierarchical Risk Parity).

### Research interpretation

The proposed alpha mechanism represents a hybrid multi-layer quantitative system:
- **Regime Selection Layer**: Filters the cross-section into distinct behavioral cohorts (pure-alpha vs. pure-beta). Pure-beta captures institutional order flow rebalancing and macroeconomic repricing cascades that diffuse gradually across the Russell 2000. Pure-alpha captures under-the-radar firm-specific corporate developments.
- **Multimodal Prediction Layer**: Blends 30-day trailing technical features with LLM-derived sentiment embeddings using 1D convolutional encoders, explicitly capturing nonlinear cross-asset interactions.
- **Dynamic Risk-Aware Allocation Layer**: By penalizing names with elevated epistemic or aleatoric uncertainty, the portfolio allocator tilts away from hallucinated LLM sentiment signals or regime transitions where the model lacks confidence, naturally controlling tail risk and turnover.

## Signal

### Signal formation timestamp
- Signal generated on decision day $t$ after market close using trailing 30-day technical indicators, daily sentiment scores up to day $t$, and the most recently available public macro indicator values.
- Rebalancing executed at day $t+1$ market open; positions held for $H \\in \\{1, 2, 3, 5, 10, 20, 40, 60\\}$ trading days.

### Stock-selection triggers
For each asset $i$ on day $t$:
1. **Stock-side Trigger ($S_S$)**: Fires when the stock's own return $z$-score satisfies:
   $$|Z_{i,t}| \\ge 2.0$$
   Direction is $\\text{sign}(Z_{i,t})$.
2. **Macro-indicator Trigger ($S_I$)**: Evaluated over 58 exogenous indicators. Trailing beta $\\beta_{i,j}$ with respect to indicator $j$ is estimated over rolling 120 trading days (daily series) or 240 trading days (macro series). An indicator-side trigger fires if the indicator's return exceeds 2 standard deviations and the tail co-movement condition is satisfied.
3. **Regime Definitions**:
   - **Pure Alpha**: $S_S \\setminus S_I$ (stock-side fires, but indicator-side does not fire).
   - **Pure Beta**: $S_I \\setminus S_S$ (indicator-side fires, but stock-side has not fired yet).
   - **Beta Intersection**: $S_S \\cap S_I$ (both stock-side and indicator-side triggers fire simultaneously).
   - A stock qualifies for the live execution mask only if it has an active BUY signal under the selected regime leg. If no stocks qualify on a rebalance date, the allocation defaults to 100% risk-free cash.

### News sentiment processing
1. **Scoring**: News articles scored into calibrated class probabilities $p_{\\tau,i} = (p^-_{\\tau,i}, p^0_{\\tau,i}, p^+_{\\tau,i})$, yielding raw directional score:
   $$s^{raw}_{\\tau,i} = p^+_{\\tau,i} - p^-_{\\tau,i}$$
2. **Entity Prior & Shrinkage**: Corrected for named-versus-masked entity bias $\\delta_i$. Trailing median sentiment $\\tilde{m}_{\\tau,i}$ is shrunk toward group median $m_{\\tau,g}$ with shrinkage intensity:
   $$w_{\\tau,i} = \\frac{n_{\\tau,i}}{n_{\\tau,i} + \\kappa_{\\text{shrink}}}, \\quad \\kappa_{\\text{shrink}} = 20.0$$
3. **Deduplication**: Cosine distance in embedding space $d(\\tau, \\tau') = 1 - e_{\\tau,i}^\\top e_{\\tau',i} \\le 1 - \\eta$. Stories within distance threshold are clustered, and cluster centroid representatives are selected.
4. **Aggregation**: Daily normalized score $\\bar{s}_{i,d}$ averaged over $K_{i,d}$ representative stories in the trailing 30-day window.

### Multimodal network architecture & uncertainty decomposition
- **Inputs**: Trailing $T = 30$ trading days of daily technical features (10 price/volume indicators: close-to-close log return, open-to-close, overnight return, adjusted return, high-low range, 20-day rolling volatility, 20-day rolling return, relative volume, MACD, RSI) and news sentiment features (mean normalized sentiment, log article count).
- **Encoder**: 1D Convolutional Neural Network (32 channels, kernel size 3) per branch, followed by a shared 64-dimensional hidden layer. Dropout rate 0.20 applied throughout.
- **Output Heads**: Emits conditional mean log-return $\\hat{\\mu}_t \\in \\mathbb{R}^N$ and low-rank parameterized aleatoric covariance $\\hat{\\Sigma}^A_t \\in \\mathbb{R}^{N \\times N}$.
- **Loss Function**: Trained with Multivariate Normal NLL ($\\mathcal{L}_G$) or Multivariate Student-$t$ NLL ($\\mathcal{L}_t$ with degrees of freedom $\\nu$).
- **Epistemic Covariance**: Estimated via $M$ stochastic Monte Carlo dropout passes during inference:
   $$\\hat{\\Sigma}^E_t = \\frac{1}{M} \\sum_{m=1}^M (\\hat{\\mu}_t^{(m)} - \\bar{\\mu}_t)(\\hat{\\mu}_t^{(m)} - \\bar{\\mu}_t)^\\top$$
- **Moment Conversion**: Log-return moments converted to arithmetic moments:
   $$\\mu_{i,t} = \\exp\\left(\\hat{\\mu}_{i,t} + \\frac{1}{2}\\hat{\\Sigma}_{ii,t}\\right) - 1$$
   $$\\Sigma_{ij,t} = \\exp\\left(\\hat{\\mu}_{i,t} + \\hat{\\mu}_{j,t} + \\frac{1}{2}\\hat{\\Sigma}_{ii,t} + \\frac{1}{2}\\hat{\\Sigma}_{jj,t}\\right) \\times \\left(\\exp(\\hat{\\Sigma}_{ij,t}) - 1\\right)$$

### Portfolio allocation rules
- **Mean-Variance Optimization (MVO)**:
   $$\\max_{w} \\left( \\mu_t^\\top w - \\frac{\\delta}{2} w^\\top \\Sigma_t w \\right), \\quad \\text{s.t. } w^\\top \\mathbf{1} = 1, \\; 0 \\le w_i \\le 0.40, \\; \\delta = 2.5$$
- **Risk Parity (RP)**: Allocates capital such that each asset contributes equally to total portfolio risk under $\\Sigma_t$.
- **Hierarchical Risk Parity (HRP)**: Tree-clustering on correlation distance $d_{ij} = \\sqrt{\\frac{1 - \\rho_{ij}}{2}}$, quasi-diagonalization, and recursive bisection inverse-variance sizing.

## Required data

- **Universe**: US small-cap equities constituent in the Russell 2000 index.
- **Price Data**: Adjusted daily Open, High, Low, Close, Volume (OHLCV) spanning October 2023 through December 2025.
- **News Data**: Timestamped public financial news headlines and articles scored with LLM backends (GPT-4o mini, FinBERT, Mistral-7B, Llama-3-8B).
- **Macroeconomic Indicators (58 series)**:
  - 50 daily market series from Yahoo Finance (11 GICS sector ETFs, major US and global equity indices, VIX, Treasury yields, energy, metals, agriculture, crypto).
  - 8 macroeconomic releases from FRED: real GDP, CPI inflation, civilian unemployment rate, industrial capacity utilization, consumer sentiment index, housing starts, building permits, effective federal funds rate.
- **Point-in-Time Discipline**: FRED macroeconomic releases forward-filled strictly after public release timestamps. News articles timestamped strictly prior to market close.

## Execution assumptions

- **Execution Timing**: Signals calculated at post-close of day $t$; rebalance executed at market open on day $t+1$.
- **Holding Period**: Fixed rebalance cadence of $H$ trading days ($H \\in \\{1, 2, 3, 5, 10, 20, 40, 60\\}$). Weights drift naturally with daily returns between rebalances.
- **Transaction Costs**: Explicitly evaluated across 0 bps, 10 bps, 25 bps, 50 bps, and 100 bps per unit of portfolio turnover. Primary reported stress benchmarks apply 50 bps and 100 bps.
- **Financing & Position Limits**: Long-only ($w_i \\ge 0$), fully invested ($\\sum w_i = 1$), per-asset maximum cap $w_i \\le 40\\%$. Unallocated capital placed in risk-free cash.

## Evidence

### Source-reported

All figures below are cited directly from Kargarzadeh et al. (arXiv:2608.12283v1, August 12, 2026), evaluated out-of-sample across calendar year 2025:

1. **Selection Regime & Horizon Performance under 100 bps Costs (Table 19)**:
   - **$H = 5$ days**: Pure alpha achieved Sharpe **1.01** (Annualized Return **89.0%**, Cumulative Net **70.0%**), whereas Pure beta produced Sharpe **-0.79** (Ann. Return -42.0%) and Beta intersection produced Sharpe **-1.34** (Ann. Return -40.7%).
   - **$H = 10$ days**: Pure alpha achieved Sharpe **1.11** (Annualized Return **49.6%**, Cumulative Net **43.8%**), compared to Pure beta Sharpe **-0.60** (Ann. Return -22.2%) and Beta intersection Sharpe **-0.83** (Ann. Return -22.6%).
   - **$H = 40$ days**: Pure beta achieved Sharpe **2.05** (Annualized Return **74.7%**), strongly dominating Pure alpha Sharpe **0.62** (Ann. Return 14.6%) and Beta intersection Sharpe **0.15** (Ann. Return 6.4%).
   - **$H = 60$ days**: Pure alpha achieved Sharpe **1.87** (Ann. Return 57.0%), Pure beta achieved Sharpe **1.48** (Ann. Return 41.8%), and Beta intersection reached Sharpe **0.69** (Ann. Return 23.9%).
   - **$H = 1$ day**: High turnover swamped returns at 100 bps (Pure alpha Sharpe -1.28, Pure beta -2.15). However, at 0 bps and 10 bps, pure beta was dominant due to immediate 1-day macro-beta spillovers.

2. **Best Conservative Allocations under 50 bps and 100 bps Costs (Table 21 & Section 5.1)**:
   - Pure beta with GPT-4o mini, Student-$t$ distribution, $H = 40$ days, and Risk Parity reached **Sharpe 2.33** at 100 bps.
   - Pure beta with FinBERT, Gaussian distribution, $H = 40$ days, and Hierarchical Risk Parity (HRP) achieved Net Return **78.4%**, Annualized Return **79.8%**, Sharpe **2.15**, and Maximum Drawdown **-18.5%** at 50 bps.
   - Pure alpha with Mistral-7B, Gaussian distribution, $H = 60$ days, and HRP achieved Net Return **50.3%**, Annualized Return **61.6%**, Sharpe **2.05**, and Maximum Drawdown **-15.5%** at 50 bps.
   - Pure alpha with Mistral-7B, Student-$t$ distribution, $H = 60$ days, and Equal Weight achieved Net Return **45.6%**, Annualized Return **56.9%**, Sharpe **1.96**, and Maximum Drawdown **-15.2%** at 50 bps.
   - In contrast, Beta intersection with Mistral-7B, Gaussian, $H = 60$ days, and Equal Weight achieved only Sharpe **0.76** (Net 15.6%, Ann 26.2%, Max DD -17.7%) at 50 bps.

3. **Allocator Comparison**:
   - Risk Parity (RP) and Hierarchical Risk Parity (HRP) consistently delivered higher risk-adjusted returns and lower drawdowns than unconstrained Mean-Variance Optimization (MVO), as MVO over-concentrated into assets with noisy predicted means.

### Independently reproduced

Not independently reproduced. The empirical metrics trace exclusively to the authors' published paper, tables, and experimental logs.

### Negative evidence

- **Short-Horizon Friction Fragility ($H \\le 3$ days)**: At 50 bps and 100 bps costs, daily rebalancing ($H = 1, 2, 3$) resulted in catastrophic negative Sharpe ratios (down to -2.44) and annualized losses exceeding -100%, proving that small-cap bid-ask bounce and market impact completely erase high-frequency sentiment alpha.
- **Beta Intersection Failure**: Requiring both stock-side and macro-indicator triggers to fire simultaneously consistently produced the lowest returns and Sharpe ratios across nearly all horizons, confirming that symmetric filtering destroys the lead-lag timing edge.
- **MVO Estimation Instability**: Unconstrained mean-variance optimization generated higher turnover and deeper drawdowns (e.g., Max DD -21.9% at $H=20$) compared to HRP and Risk Parity.

## Falsification plan

1. **Lead-Lag Shuffled Macro Placebo Test**: Randomly permute the timestamps of the 58 macro indicators while preserving small-cap stock return series. If the pure-beta strategy retains positive out-of-sample Sharpe at $H = 40$ days, the hypothesized macroeconomic information spillover mechanism is falsified.
2. **Sentiment Shuffled Label Test**: Randomly shuffle news sentiment embeddings across tickers on each date. If the multimodal model's Sharpe ratio does not collapse significantly toward baseline technical-only models, the incremental predictive contribution of LLM news sentiment is disproven.
3. **Execution Delay Test**: Introduce a 1-day execution lag (executing on day $t+2$ instead of $t+1$). If pure-alpha Sharpe at $H=5$ degrades by more than 50%, the alpha is confirmed to be ultra-short-lived and vulnerable to real-world operational delays.
4. **Liquidity & Capacity Frontier Stress**: Restrict the universe to the lowest-decile liquidity stocks in the Russell 2000 and simulate 150 bps market impact. If cumulative net return turns negative across all horizons, the strategy lacks institutional capacity.

## Crypto portability

Portability status: **adapted / unproven**.

The source paper exclusively tests US small-cap equities and FRED/Yahoo macro indicators. Porting this mechanism to cryptocurrency requires specific adaptations:

1. **Universe Adaptation**: The concept of "small-cap" translates to mid-to-low cap altcoins (e.g., market caps between $50M and $500M) vs. mega-caps (BTC, ETH, SOL).
2. **Macro-Beta Panel Adaptation**: The 58 macro indicators must be replaced with crypto-native liquidity and leverage drivers: BTC dominance, USDT/USDC stablecoin net minting, Binance aggregated funding rates, Deribit 25-delta skew, and Korean exchange (Upbit) retail volume premiums.
3. **News Sentiment Ingestion**: Crypto news is dominated by continuous social feeds (Crypto Twitter/X, Telegram announcements, governance forum proposals) with severe spam and bot pollution, requiring aggressive deduplication and anti-sybil clustering before LLM sentiment scoring.
4. **24/7 Continuous Trading & Funding Risk**: Unlike equity markets with discrete daily closes and market-on-open auctions, crypto trades 24/7. Altcoin perpetuals carry substantial funding rate divergence during market run-ups, which can erode long-horizon ($H = 40$ days) returns unless funding arbitrage hedging is integrated.

## Limitations

- **Knowledge Cutoff & In-Sample Boundary**: LLMs trained with fixed historical weights may embed look-ahead exposure if evaluated on historical news prior to their training cutoff (though the authors used October 2023 cutoff models on 2025 data).
- **Small-Cap Microstructure & Slippage**: Russell 2000 stocks suffer from wide bid-ask spreads and limited depth during market opens; assuming 50–100 bps fixed slippage may underestimate true market impact for portfolios exceeding $10M AUM.
- **Survivorship & Delisting Filtering**: Point-in-time constituent adjustments of the Russell 2000 must be handled rigorously to avoid survivorship bias in small-cap historical pools.
- **Absence of Open-Source Code Repository**: While model equations and hyperparameters are fully specified, no immutable GitHub commit with executable training pipelines is provided by the authors.

## Implementation status

not-implemented. This research record documents an empirical academic study. No implementation in NautilusTrader, PyBroker, or live production environments has been undertaken.

## Adoption boundary

research-only / not-approved. This record is strictly for research interpretation and hypothesis tracking. It is not approved for live trading, testnet, paper execution, or capital commitment.

## Related Wiki records

- [[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]]
- [[quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]]
- [[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]]
- [[quant/portfolio-covariance-and-shrinkage-2026-08-28]]
- [[quant/volatility-targeting-risk-parity-constrained-2026-08-28]]
- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]

## Sources

- Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, and Arman Khaledian, "Large Language Model-Driven Small-Capitalization Trading: Integrating Financial News Sentiment, Macroeconomic Indicators, and Technical Signals", arXiv preprint arXiv:2608.12283v1 [q-fin.PM, cs.AI, cs.LG], submitted August 12, 2026. Available at: https://arxiv.org/abs/2608.12283; HTML: https://arxiv.org/html/2608.12283v1; PDF: https://arxiv.org/pdf/2608.12283. DOI: https://doi.org/10.48550/arXiv.2608.12283.
- Tetlock, P. C. (2007), 'Giving content to investor sentiment: The role of media in the stock market', Journal of Finance, 62(3), 1139–1168.
- Lopez-Lira, A. and Tang, Y. (2026), 'Can ChatGPT forecast stock price movements? Return predictability and large language models', Journal of Financial Economics.
- De Prado, M. L. (2018), Advances in Financial Machine Learning, John Wiley & Sons.
