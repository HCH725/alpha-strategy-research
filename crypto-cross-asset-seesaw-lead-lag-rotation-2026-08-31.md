---
schema: strategy-research-record-v1
title: Crypto Cross-Asset Seesaw Lead-Lag Rotation
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-asset
  - lead-lag
  - seesaw-effect
  - cross-predictability
  - lasso-selection
status: research-only
confidence: high
source_as_of: 2023-09
sources:
  - https://doi.org/10.1016/j.jempfin.2023.101428
  - https://doi.org/10.1093/rfs/hhl035
  - https://doi.org/10.1111/j.2517-6161.1996.tb02080.x
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Cross-Asset Seesaw Lead-Lag Rotation

## Provenance

Primary source: Yuecheng Jia, Yangru Wu, Shu Yan, and Yuzheng Liu, “A seesaw effect in the cryptocurrency market: Understanding the return cross predictability of cryptocurrencies,” *Journal of Empirical Finance* 74 (2023), article 101428. DOI: https://doi.org/10.1016/j.jempfin.2023.101428.

The authors investigate cross-asset return predictability across dozens of cryptocurrencies from major global spot exchanges (Binance, Bitfinex, Bittrex, Poloniex) covering 2017 through 2022.

Foundational and related literature:
- Kewei Hou, “Industry Information Diffusion and the Lead-Lag Effect in Stock Returns,” *The Review of Financial Studies* 20(4), 1113–1138 (2007). DOI: https://doi.org/10.1093/rfs/hhl035.
- Robert Tibshirani, “Regression Shrinkage and Selection via the Lasso,” *Journal of the Royal Statistical Society: Series B (Methodological)* 58(1), 267–288 (1996). DOI: https://doi.org/10.1111/j.2517-6161.1996.tb02080.x.
- Dirk G. Baur, Thomas Dimpfl, and Konstantin Kuck, “Bitcoin, gold and the US dollar–A replication and extension,” *Finance Research Letters* 25, 103–110 (2018). DOI: https://doi.org/10.1016/j.frl.2017.10.012.

## Economic mechanism

### Source-reported

In traditional equity markets, large firms lead small firms with a positive coefficient due to gradual information diffusion (Hou, 2007). Jia, Wu, Yan, and Liu (2023) uncover a contrary, asymmetric dynamic in the cryptocurrency market termed the **"seesaw effect"**:
1. Large-market-capitalization cryptocurrencies (e.g. BTC, ETH, XRP) exhibit strong, statistically significant **negative lead-lag cross-predictability** on the returns of smaller altcoins.
2. In contrast, small-cap cryptocurrencies exhibit negligible predictive power over large-cap returns.
3. The authors propose a behavioral and structural liquidity-reallocation mechanism:
   - When large coins experience sudden positive demand and price surges, limited investor attention and speculative capital are rapidly drawn out of altcoins and concentrated into the large coins, causing altcoin liquidity drain and short-term underperformance.
   - Subsequently, after large-coin momentum consolidates, profits and liquidity rotate outward into smaller altcoins ("altcoin season" spillover).
4. Using high-dimensional machine learning (LASSO penalization), the authors extract sparse predictive lead-lag coefficients across assets that generate significant out-of-sample trading alpha.

### Research interpretation

The hypothesized mechanism is attention-constrained capital rotation and market-liquidity reallocation:
1. Retail and speculative capital in crypto is finite and highly mobile.
2. Large-cap upward surges trigger FOMO attention spikes, prompting traders to liquidate altcoin holdings to chase BTC/ETH breakouts, creating a temporary negative price drag on altcoins.
3. Conversely, sharp pullbacks or consolidation in large-cap coins prompt capital reallocation back into higher-beta altcoins.
4. Conditioning altcoin long/short allocations on trailing large-cap returns (or fitting regularized multi-asset VAR models with LASSO) captures this predictable lead-lag liquidity cycle.

## Signal

1. **Asset classification**:
   - Divide active crypto universe into **Leader assets** ($L$, top 3–5 market-cap coins: BTC, ETH, SOL/XRP) and **Target altcoin universe** ($S$, liquid altcoins ranked 10–100 by market cap and ADV).
2. **Estimation window & LASSO cross-predictability**:
   - For each target asset $i \in S$, estimate trailing regularized predictive regression over window $T = 60\text{ to }90\text{ days}$:
     $$R_{i,t} = \mu_i + \sum_{k=1}^P \phi_{i,k} R_{i,t-k} + \sum_{j \in L} \sum_{k=1}^P \beta_{i,j,k} R_{j,t-k} + \epsilon_{i,t}$$
   - Solve via LASSO $\ell_1$-penalization to identify non-zero predictive lag coefficients:
     $$\min_{\{\phi, \beta\}} \sum_{t} \left( R_{i,t} - \hat{R}_{i,t} \right)^2 + \lambda \left( \sum_k |\phi_{i,k}| + \sum_{j,k} |\beta_{i,j,k}| \right)$$
   - Optimal tuning parameter $\lambda$ chosen via rolling cross-validation / BIC.
3. **Simplified heuristic seesaw signal**:
   - Compute trailing 1-to-3 day leader return spread $\bar{R}_{L,t} = \frac{1}{|L|}\sum_{j \in L} R_{j,t}^{(1\text{d})}$.
   - For each target altcoin $i$, expected next-day return is inversely proportional to leader return shock:
     $$\hat{s}_{i,t} = -\text{sign}(\bar{R}_{L,t}) \cdot |R_{i,t}^{(1\text{d})} - \bar{R}_{L,t}|$$
4. **Portfolio construction & ranking**:
   - Rank altcoins by predicted return $\hat{R}_{i,t+1}$ into quintiles or tertiles.
   - **Long basket**: Top quintile of predicted altcoins (assets expected to benefit from capital rotation).
   - **Short basket**: Bottom quintile of predicted altcoins (assets suffering from liquidity drainage).
   - Hedge market directional beta using a short/long position in BTC/ETH perpetual futures.
5. **Rebalancing cadence**:
   - Daily (24-hour holding horizon) or 3-day holding horizon.
6. **Specification status**: **fully specified** for LASSO objective function and cross-lag structure; **underspecified** regarding intra-day execution timing and penalty tuning speed.

## Required data

- Daily OHLCV series for top 100 cryptocurrencies across major spot and perpetual exchanges.
- Market capitalization and daily volume series for dynamic Leader vs Altcoin universe segmentation.
- UTC daily candle alignment (00:00:00 UTC).
- Historical listing/delisting data.

## Execution assumptions

- Signal calculated at day $t$ close (00:00 UTC); orders executed at open of day $t+1$.
- Taker fee modeling (5–8 bps) and bid-ask spread slippage accounted for in net return estimation.
- Market-neutral hedging via BTC/ETH perpetual contracts.
- Short leg execution requires active perpetual futures contracts or spot margin borrowing.

## Evidence

### Source-reported

Jia, Wu, Yan, and Liu (2023) report:
- Large coins negatively predict the next-day returns of small coins with statistical significance across multiple independent exchanges (Binance, Bitfinex, Bittrex, Poloniex).
- Out-of-sample LASSO-based trading strategies generate annualized returns of **30% to 65%** with annualized Sharpe ratios ranging from **1.5 to 2.4** across the 2018–2022 sample period.
- Net profitability survives 10 bps transaction costs per trade.
- Sub-sample analyses confirm that the seesaw effect is strongest during periods of high market attention and retail trading activity.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Strategy performance degrades during structural liquidity crashes (e.g. March 2020 or Nov 2022) when all crypto correlations spike toward 1.0, temporarily overriding cross-sectional lead-lag dispersion.
- Daily rebalancing across a basket of 20–40 altcoins creates continuous turnover drag that requires maker-rebate or low-fee tier structures.
- Potential decay: As institutional algorithmic market makers deploy cross-asset arbitrage bots, lead-lag latency in price discovery shrinks from daily horizons to intraday/sub-second horizons.

## Falsification plan

The seesaw lead-lag hypothesis should be rejected or considered unviable if:
1. Out-of-sample evaluation (2023–2026 data) demonstrates that the cross-predictive coefficients $\beta_{i,j,k}$ collapse to zero ($t < 1.96$) or flip positive.
2. The LASSO long-short portfolio generates net Sharpe $< 0.3$ after deducting realistic execution costs (7 bps taker fee + 3 bps spread).
3. The predictive alpha is subsumed entirely by simple 1-day time-series reversal of the altcoins themselves (ablation against pure individual reversal).
4. Testing at higher execution latency (> 1 hour post-close) degrades PnL to zero, indicating signal decay.

## Crypto portability

**Direct**, as the empirical framework was developed and evaluated natively on cryptocurrency spot exchanges.

Portability adaptations for perpetual futures:
- Perpetual contracts provide high liquidity and low slippage for simultaneous altcoin long/short baskets and BTC/ETH hedge execution.
- Funding rate divergence between leader contracts and altcoins must be incorporated into net holding cost calculations.

## Limitations

- **not independently reproduced**: requires replication in a systematic backtesting engine.
- **turnover friction**: daily portfolio updates generate continuous rebalancing costs.
- **correlation regime shifts**: during broad market panic sell-offs, cross-asset dispersion collapses as all tokens plunge together.
- **underspecified execution**: exact execution time window and order routing dynamics are omitted in the academic text.

## Implementation status

No implementation in PyBroker, NautilusTrader, or any internal research/backtesting pipeline has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is research material only. It does not represent a validated production strategy, an execution authorization, or approval for Paper, Testnet, or Live trading.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

- `[[crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]`
- `[[crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31]]`
- `[[crypto-cross-sectional-idiosyncratic-skewness-2026-08-31]]`

## Sources

1. Yuecheng Jia, Yangru Wu, Shu Yan, and Yuzheng Liu, “A seesaw effect in the cryptocurrency market: Understanding the return cross predictability of cryptocurrencies,” *Journal of Empirical Finance* 74, 101428 (2023). DOI: https://doi.org/10.1016/j.jempfin.2023.101428
2. Kewei Hou, “Industry Information Diffusion and the Lead-Lag Effect in Stock Returns,” *The Review of Financial Studies* 20(4), 1113–1138 (2007). DOI: https://doi.org/10.1093/rfs/hhl035
3. Robert Tibshirani, “Regression Shrinkage and Selection via the Lasso,” *Journal of the Royal Statistical Society: Series B (Methodological)* 58(1), 267–288 (1996). DOI: https://doi.org/10.1111/j.2517-6161.1996.tb02080.x
4. Dirk G. Baur, Thomas Dimpfl, and Konstantin Kuck, “Bitcoin, gold and the US dollar–A replication and extension,” *Finance Research Letters* 25, 103–110 (2018). DOI: https://doi.org/10.1016/j.frl.2017.10.012
