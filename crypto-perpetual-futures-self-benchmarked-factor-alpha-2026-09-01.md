---
schema: strategy-research-record-v1
title: Crypto Perpetual Futures Self-Benchmarked Factor Investing and Aggressor Flow Alpha
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - factor-investing
  - self-benchmarking
  - market-neutral
  - aggressor-flow
status: research-only
confidence: medium
source_as_of: 2026
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7301919
  - https://doi.org/10.2139/ssrn.7301919
  - https://www.researchgate.net/publication/393245464_Every_Asset_Its_Own_Benchmark_Market-Neutral_Alpha_in_Perpetual_Futures
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Futures Self-Benchmarked Factor Investing and Aggressor Flow Alpha

## Provenance

Primary source: Dhanya MD, "Every Asset Its Own Benchmark: Market-Neutral Alpha in Perpetual Futures," SSRN working paper, posted/updated January 2026. SSRN Abstract ID: 7301919, DOI: https://doi.org/10.2139/ssrn.7301919. ResearchGate persistent URL: https://www.researchgate.net/publication/393245464_Every_Asset_Its_Own_Benchmark_Market-Neutral_Alpha_in_Perpetual_Futures.

The paper investigates factor investing across a panel of 112 cryptocurrency perpetual contracts over a 363-week test window. It challenges the standard equity-style cross-sectional peer-ranking approach, proposing self-benchmarking (ranking each contract against its own trailing history) and pre-standardization to eliminate cross-sectional scale heterogeneity. It also evaluates an aggressor-side information factor derived from venue-native taker trade imbalance.

Exact factor construction parameter lookback windows, portfolio quantile cutoffs, and execution timestamps not explicitly published in the public abstract/summary remain **underspecified**.

## Economic mechanism

### Source-reported

In traditional equities, cross-sectional factor investing relies on ranking assets against one another under the structural anchor of shared accounting standards, industry classifications, and cash flow fundamentals. In contrast, cryptocurrency perpetual futures exhibit extreme scale heterogeneity, non-stationary volatility regimes, and no common fundamental anchor.

The author argues that directly sorting unadjusted factor values across heterogeneous crypto assets introduces scale distortion. By ranking each perpetual contract against its own trailing history ("self-benchmarking"), or by standardizing each asset against its own history prior to cross-sectional ranking, factor signals become comparable across the cross-section. The author reports that self-benchmarking outperforms peer-relative ranking in 9 out of 11 factor cases. In addition, the paper introduces a factor leveraging exchange-native aggressor-side information (taker buy vs sell volume), which captures signed order-flow pressure that is directly published by crypto exchanges.

### Research interpretation

The falsifiable hypothesis is that **scale heterogeneity and idiosyncratic volatility dispersion distort raw cross-sectional factor rankings in crypto perpetual futures**. 

When factor metrics (momentum, volatility, basis, turnover, or order flow) are compared raw across assets, the resulting long and short portfolios become disproportionately loaded on structural outliers (e.g. ultra-high-volatility small-cap perpetuals) rather than genuine relative mispricings.

Standardizing factor exposures through a time-series z-score or rolling empirical percentile for each individual contract (self-benchmarking) rescales each asset's factor signal onto a uniform scale:

$$\tilde{F}_{i,t} = \frac{F_{i,t} - \mu_i(L)}{\sigma_i(L)}$$

where $\mu_i(L)$ and $\sigma_i(L)$ are the rolling mean and standard deviation of factor $F$ for asset $i$ over trailing lookback $L$.

Cross-sectional ranking on $\tilde{F}_{i,t}$ generates a balanced market-neutral portfolio that captures asset-level regime shifts while neutralizing persistent cross-sectional scale biases. Aggressor-side order flow acts as a directional confirmation filter reflecting informed taker demand.

## Signal

Normalized source-faithful signal framework:

1. **Universe Formation**: At each weekly rebalance date $t$, select the eligible panel of liquid perpetual futures contracts (source uses $N = 112$).
2. **Factor Computation**: Compute raw factor values $F_{i,t}^k$ for each factor $k \in \{1, \dots, 10\}$ (e.g. momentum, reversal, basis, volatility, liquidity, turnover) and for the venue-native aggressor flow factor $F_{i,t}^{\text{aggressor}}$.
3. **Self-Benchmarking / Time-Series Standardization**:
   - For each asset $i$ and factor $k$, calculate the trailing rolling mean $\mu_{i,t}^k$ and trailing volatility $\sigma_{i,t}^k$ over lookback window $L$.
   - Compute standardized factor score $Z_{i,t}^k = \frac{F_{i,t}^k - \mu_{i,t}^k}{\sigma_{i,t}^k}$ (or historical trailing percentile rank).
4. **Cross-Sectional Factor Combination & Sorting**:
   - Aggregate standardized scores into a multi-factor composite score $S_{i,t} = \sum_k w_k Z_{i,t}^k + w_{\text{aggr}} Z_{i,t}^{\text{aggressor}}$.
   - Rank-order all assets by composite score $S_{i,t}$.
5. **Portfolio Allocation**:
   - Long the top quantile (highest standardized scores) and short the bottom quantile (lowest standardized scores) with dollar-neutral weights.
6. **Rebalancing**: Re-form portfolio weekly.

Exact parameter specifications for lookback $L$, multi-factor weights $w_k$, quantile threshold (quintile vs decile), and trade execution timestamp are **underspecified** in public summaries and must not be invented.

## Required data

- Point-in-time universe of cryptocurrency perpetual futures contracts with complete listing, delisting, and tick/contract specifications.
- Daily/weekly OHLCV prices, volume, and open interest.
- Taker buy/sell volume (aggressor-side order flow) per contract.
- Perpetual funding rates, 8-hour settlement timestamps, and mark/index price feeds.
- Venue margin rules, collateral haircuts, and maintenance margin tiers across all 112 contracts.

## Execution assumptions

- Market-neutral long/short execution on centralized perpetual futures exchanges (e.g. Binance, OKX, Bybit).
- Next-bar rebalancing at weekly boundary after signal calculation to prevent look-ahead bias.
- Explicit modeling of:
  - Taker and maker fee tiers (e.g. 2–5 bps taker fee per leg).
  - Bid-ask spread and market impact on smaller/mid-cap perpetuals.
  - Net funding rate payment/receipt across the long and short baskets.
  - Leverage limits and dynamic margin collateral allocation.
  - Liquidation avoidance buffers during market-wide deleveraging spikes.

## Evidence

### Source-reported

- Evaluated across 112 perpetual contracts over a 363-week panel.
- Self-benchmarking (ranking each contract against its own trailing history) outperforms peer-ranking in **9 out of 11 factor cases**.
- Mean annualized Sharpe ratio increased from **1.01** (traditional peer-ranking) to **1.45** (self-benchmarking).
- Pre-standardizing assets against their own trailing history before cross-sectional sorting recovers **41% of the performance gap**, identifying scale heterogeneity as the primary driver.
- Annualized alpha of **27%** when regressed on market, size, and momentum factors, with market beta indistinguishable from zero.
- During the 2022 market downturn (-82% for broad crypto market), the strategy returned **+9%** with a maximum drawdown of **8%**.
- Reported robust under walk-forward selection, held-out universe testing, transaction-cost stresses, and deflated Sharpe ratio corrections.

All figures above are **source-reported** by Dhanya MD (2026) and have not been independently verified.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed primary source.

Absence of reported negative evidence is not evidence of absence. Potential real-world failure modes include:
- Persistent negative funding drag if long baskets systematically cluster in high-positive-funding contracts while short baskets cluster in negative-funding contracts.
- Severe turnover-induced transaction cost drag on weekly rebalances across 112 contracts under higher taker fee schedules.
- Execution slippage on lower-liquidity perpetuals during volatile liquidation cascades.

## Falsification plan

The hypothesis should be weakened or rejected if an independent point-in-time backtest demonstrates:

1. Self-benchmarking does not yield a statistically significant Sharpe ratio improvement ($t < 2.0$) over raw cross-sectional ranking across an out-of-sample perpetual dataset.
2. The Sharpe advantage disappears after accounting for realistic taker fees (e.g., 4 bps taker fee) and actual realized funding rate payments.
3. The aggressor-side flow factor exhibits fast alpha decay that cannot be monetized at weekly rebalance frequencies.
4. Performance is fragile to small variations in lookback window $L$ or universe selection thresholds.
5. The 2022 drawdown resistance fails when tested on an expanded or alternative venue dataset.

## Crypto portability

**Direct**, as the research is natively formulated and tested on cryptocurrency perpetual futures.

Key operational considerations:
- Funding rate divergence between long and short legs must be tracked in real time.
- Venue-specific contract specifications (linear USDT-margined vs inverse coin-margined) require consistent normalization.
- 24/7 continuous trading requires a fixed UTC rebalance timestamp convention.

## Limitations

- **Not independently reproduced.**
- **Working-paper status:** SSRN working paper posted/updated January 2026.
- **underspecified:** Exact lookback length $L$, factor selection weights $w_k$, and quantile cutoffs are not fully detailed in available public text.
- **execution gap:** Net funding rate drag across long/short legs was not isolated separately from gross capital gains in public summaries.
- **exchange risk:** Centralized exchange counterparty and margin haircut risks are unmodeled in standard factor backtests.

## Implementation status

No implementation in PyBroker, NautilusTrader, the strategy registry, Paper, Testnet, Demo, or Live trading has been created or modified.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material in the Alpha Strategy Pool only. It is not evidence of validated alpha, not an implementation task, and not approval for Paper, Testnet, Demo, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain record was queried, created, or modified in this Scout cycle.

Related Alpha Strategy Pool artifacts:
- `crypto-cross-sectional-factor-momentum-anomaly-portfolios-2026-08-31.md` — cross-sectional factor momentum anomaly portfolios.
- `crypto-world-order-flow-cross-sectional-quintile-weekly-2026-08-31.md` — weekly order flow cross-sectional anomaly.
- `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` — perpetual funding rate time-series carry.

## Sources

1. Dhanya MD, “Every Asset Its Own Benchmark: Market-Neutral Alpha in Perpetual Futures,” SSRN working paper, January 2026. SSRN Abstract: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7301919
2. DOI / SSRN persistent identifier: https://doi.org/10.2139/ssrn.7301919
3. ResearchGate publication entry: https://www.researchgate.net/publication/393245464_Every_Asset_Its_Own_Benchmark_Market-Neutral_Alpha_in_Perpetual_Futures
