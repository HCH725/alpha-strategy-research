---
schema: strategy-research-record-v1
title: Crypto Cross-Sectional Fundamental Network and Sentiment Factor-Mimicking Dynamic Sorting
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - factor-mimicking
  - on-chain
  - sentiment
  - hashrate
  - active-users
  - fundamental
status: research-only
confidence: medium
source_as_of: 2026
sources:
  - https://doi.org/10.1016/j.intfin.2026.102285
  - https://www.sciencedirect.com/science/article/abs/pii/S1062940826000085
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Sectional Fundamental Network and Sentiment Factor-Mimicking Dynamic Sorting

## Provenance

Primary source: Massimo Guidolin and Serena Ionta, "Predictive sorting of cryptocurrencies based on fundamentals and sentiment", *Journal of International Financial Markets, Institutions and Money*, Volume 107, Article 102285 (2026). DOI: https://doi.org/10.1016/j.intfin.2026.102285.

The study investigates return predictability across a cross-section of 40 cryptocurrencies by constructing weekly factor-mimicking portfolios (FMPs) for non-tradable fundamental metrics (blockchain network active users and computing hashrate) and market sentiment (Google Trends search volume). It implements an out-of-sample portfolio sorting framework ranking assets by realized predictability scores and certainty equivalent returns.

## Economic mechanism

### Source-reported

Guidolin and Ionta (2026) show that cryptocurrency returns are not purely erratic or speculative, but are reliably predictable out-of-sample through the combination of blockchain-specific fundamental variables and investor sentiment. 

Because on-chain network metrics and search sentiment are non-tradable, the authors construct factor-mimicking portfolios (FMPs) that project non-tradable series onto a set of basis asset returns. The authors report that network activity (active users), computing intensity (hashrate), and sentiment (Google search trends) all exhibit significant out-of-sample predictive power across the 40-cryptocurrency panel. Furthermore, dynamically ranking assets by their realized predictability scores yields long-short portfolio spreads with certainty equivalent returns well above the risk-free rate, confirming the joint economic relevance of fundamental utility and behavioral attention.

### Research interpretation

The falsifiable hypothesis is that **cryptocurrency cross-sectional price dynamics are driven by a dual-engine interaction between structural network adoption (fundamentals) and retail attention flow (sentiment), which can be harvested via dynamic predictability sorting**:

1. **Fundamental Value Anchor**: Long-term blockchain adoption expands according to Metcalfe utility ($\text{Active Users}$) and computational security investment ($\text{Hashrate}$). Accelerating network fundamentals signal expanding fundamental value.
2. **Behavioral Attention Transmission**: Retail investor attention (proxied by Google Trends search intensity) acts as the transmission mechanism that drives speculative capital inflows and price discovery.
3. **Synergistic Predictability**: Assets exhibiting strong fundamental growth coupled with positive sentiment momentum experience sustained upward drift. Dynamically sorting assets based on recursive out-of-sample predictive performance ($R^2$ / Certainty Equivalent Return) allocates capital to the most responsive factor exposures while penalizing decaying networks.

## Signal

Normalized source-faithful signal and portfolio sorting architecture:

1. **Universe Formation**: Panel of liquid cryptocurrencies with verifiable on-chain data and Google search indices ($N = 40$).
2. **Weekly Predictor Extraction**:
   - **Network Activity ($N_{i,t}$)**: Percentage change in weekly active user wallet addresses:
     $$N_{i,t} = \ln(\text{ActiveAddresses}_{i,t}) - \ln(\text{ActiveAddresses}_{i,t-1})$$
   - **Computing Intensity ($H_{i,t}$)**: Percentage change in network mining hashrate (or staking security equivalent):
     $$H_{i,t} = \ln(\text{Hashrate}_{i,t}) - \ln(\text{Hashrate}_{i,t-1})$$
   - **Investor Sentiment ($S_{i,t}$)**: Normalized Google Trends search query volume for token $i$:
     $$S_{i,t} = \frac{\text{SearchVolume}_{i,t} - \mu_{i,t}(52)}{\sigma_{i,t}(52)}$$
3. **Factor-Mimicking Portfolio (FMP) Projection**:
   - For each non-tradable series $X_t \in \{N_t, H_t, S_t\}$, estimate projection weights $w_X$ by regressing $X_t$ on a set of base cryptocurrency returns $R_t$:
     $$X_t = \alpha + w_X^\top R_t + \epsilon_t$$
   - The tradable mimicking factor return is:
     $$F_t^X = w_X^\top R_t$$
4. **Recursive Out-of-Sample Predictability Scoring**:
   - Estimate rolling predictive regressions for each asset $i$:
     $$R_{i,t+1} = \alpha_i + \beta_i^N F_t^N + \beta_i^H F_t^H + \beta_i^S F_t^S + e_{i,t+1}$$
   - Calculate rolling out-of-sample predictability metric (Certainty Equivalent Return $CER_{i,t}$ or out-of-sample $R_{OOS,i,t}^2$).
5. **Portfolio Sorting & Allocation**:
   - Sort the 40 cryptocurrencies into quantiles (e.g. quintiles $Q_1$ to $Q_5$) based on predictability scores.
   - Long the top quantile (highest predictability / positive forecast) and short the bottom quantile (lowest predictability / negative forecast) with dollar-neutral weights.
6. **Rebalancing Frequency**: Weekly at fixed UTC boundary.

Exact FMP base asset weights and quantile selection cutoffs not detailed in the public article abstract remain **underspecified**.

## Required data

- **On-Chain Fundamental Data**: Weekly active wallet addresses and network hashrate across 40 layer-1 / layer-2 blockchains (Glassnode, CoinMetrics, or direct RPC node indexers).
- **Search Sentiment Data**: Weekly Google Trends search volume index per cryptocurrency name and ticker.
- **Market Data**: Weekly OHLCV prices, volume, and market capitalization across the 40-asset universe.
- **Risk-Free Rate**: 3-month US Treasury bill rate or USDC lending rate for Certainty Equivalent Return benchmarks.

## Execution assumptions

- Weekly rebalance execution on centralized spot / perpetual exchanges (e.g. Binance, OKX, Coinbase).
- Next-bar execution at weekly close (Sunday 23:59:59 UTC / Monday 00:00:00 UTC) to eliminate look-ahead bias.
- Explicit modeling of:
  - Taker and maker transaction fees (e.g., 2–5 bps per leg).
  - Bid-ask spread and liquidity constraints on mid-tier altcoins in the 40-token panel.
  - Short-borrow fees or perpetual funding rates on short basket positions.

## Evidence

### Source-reported

- Evaluated across a cross-section of 40 cryptocurrencies using weekly out-of-sample forecasting and portfolio sorting.
- All three factor-mimicking portfolios (network activity, computing intensity, sentiment) demonstrate statistically significant out-of-sample return predictability.
- Long-short portfolios formed on predictability sorting achieve Certainty Equivalent (CE) returns well in excess of the risk-free rate, delivering superior risk-adjusted returns relative to passive buy-and-hold benchmarks.
- Combining both fundamental (on-chain) and behavioral (sentiment) predictors yields higher stability and economic performance than single-predictor models.

All empirical performance claims above are **source-reported** by Guidolin and Ionta (2026) and have not been independently verified.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed primary source.

Absence of reported negative evidence is not evidence of absence. Potential real-world failure modes include:
- Computing intensity (hashrate) is strictly defined for Proof-of-Work blockchains; applying hashrate to Proof-of-Stake or DAG architectures requires structural proxy substitutions that may introduce noise.
- Google Trends data suffers from revisions, language bias, and ticker symbol collisions (e.g., common English words).
- Factor-mimicking portfolio weights estimated over historical rolling windows may suffer from estimation error and high turnover costs during regime shifts.

## Falsification plan

The hypothesis should be weakened or rejected if an independent point-in-time backtest demonstrates:

1. Factor-mimicking portfolios fail to achieve positive out-of-sample $R_{OOS}^2$ across an expanded panel of 100+ cryptocurrencies from 2024 to 2026.
2. The Certainty Equivalent return spread between top and bottom quintiles drops below the risk-free rate after applying realistic round-trip trading fees (10 bps) and perpetual funding drag.
3. Replacing Google Trends with alternative sentiment proxies (Twitter/X volume, LunarCrush) completely erodes factor significance, indicating overfitting to Google search artifacts.
4. An ablation test removing hashrate shows that PoS-adapted models underperform simple user-growth + momentum benchmarks.

## Crypto portability

**Direct**, as the methodology is natively constructed and tested on cryptocurrency spot markets using blockchain-specific on-chain metrics and crypto search queries.

Key operational considerations:
- Staking participation rate and validator count should be evaluated as PoS equivalents for PoW hashrate.
- Data availability latency for on-chain metrics must be accounted for by enforcing a strict 1-day ingestion lag before weekly rebalance.

## Limitations

- **Not independently reproduced.**
- **Peer-reviewed journal status:** Published in *Journal of International Financial Markets, Institutions and Money*, Vol. 107 (2026), Article 102285.
- **underspecified:** Exact FMP projection regression asset universe and specific CER utility parameters ($\gamma$ risk aversion coefficient) are not fully listed in public summaries.
- **PoW vs PoS heterogeneity:** Hashrate is native only to PoW networks; universe composition requires careful handling of non-PoW assets.

## Implementation status

No implementation in our research stack has been completed.

## Adoption boundary

Research material only.

A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- `[[quant/crypto-cross-sectional-onchain-user-activity-growth-2026-08-31]]`
- `[[quant/crypto-cross-sectional-abnormal-investor-attention-momentum-2026-08-31]]`
- `[[quant/crypto-cross-sectional-sentiment-risk-beta-premium-2026-09-01]]`

## Sources

- Massimo Guidolin and Serena Ionta, "Predictive sorting of cryptocurrencies based on fundamentals and sentiment", *Journal of International Financial Markets, Institutions and Money*, Volume 107, Article 102285 (2026). DOI: https://doi.org/10.1016/j.intfin.2026.102285.
- ScienceDirect Article Link: https://www.sciencedirect.com/science/article/abs/pii/S1062940826000085.
