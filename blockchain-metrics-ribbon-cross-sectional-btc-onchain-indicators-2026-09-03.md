---
schema: strategy-research-record-v1
title: "Blockchain Metrics Ribbon: Cross-Sectional On-Chain Indicator Suite for Bitcoin Trading"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-03
sources:
  - "King, J.C., Dale, R., Amigó, J.M. (2024). 'Blockchain Metrics and Indicators in Cryptocurrency Trading.' Solitons & Fractals, 178, 114305. DOI: 10.1016/j.chaos.2023.114305. arXiv:2403.00770v1. https://arxiv.org/abs/2403.00770"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Blockchain Metrics Ribbon: Cross-Sectional On-Chain Indicator Suite for Bitcoin Trading

## Provenance

- **Paper:** King, J.C., Dale, R., Amigó, J.M. (2024). "Blockchain Metrics and Indicators in Cryptocurrency Trading." *Solitons & Fractals*, 178, 114305.
- **DOI:** https://doi.org/10.1016/j.chaos.2023.114305
- **arXiv:** 2403.00770v1 [q-fin.ST], submitted 11 Feb 2024.
- **GitHub:** https://github.com/JuanCarlosKing/BlockchainIndicatorsSimulations (Python code for simulations)
- **Data source:** Quandl/Nasdaq BCHAIN dataset (21 blockchain metrics, daily, 2009–2022)
- **Sample period:** August 16, 2010 – December 31, 2022 (Bitcoin daily closing price)
- **Asset:** Bitcoin (BTC/USD)

## Economic mechanism

### Source-reported

The authors hypothesize that blockchain network metrics (hash rate, mining difficulty, cost per transaction, wallet users, transaction counts, etc.) contain predictive information about Bitcoin price that is not fully captured by price data alone. By extending the "Hash Ribbon" concept — a moving-average crossover technique originally applied to hash rate — to 21 blockchain metrics, they construct "blockchain ribbons" that generate long and short trading signals. The authors further derive "adjusted" variants (AdCPTRA, AdMWNUS, AdNTRAT, AdBLCHS) for monotonic metrics by applying time derivatives or linear regression normalization. The economic rationale is that mining-side data reflects network health, miner profitability, and adoption dynamics that precede or accompany price movements.

### Research interpretation

The hypothesized mechanism is a **supply-side and adoption-side information premium**: blockchain metrics encode information about miner economics (cost per transaction, difficulty, hash rate), network adoption (wallet users, transaction counts), and infrastructure growth (blockchain size) that is publicly available but not instantly impounded into price. The ribbon technique (SMA-30 vs SMA-60 crossover) extracts trend changes in these metrics as trading signals. The key falsifiable claim is that blockchain metric ribbons generate statistically superior long signals compared to price-only technical indicators, and that the Adjusted CPTRA (AdCPTRA) indicator provides additional alpha in both long and short directions.

The signal construction is:
- **Regime/Filter:** None specified (raw ribbon crossover signals).
- **Primary signal:** SMA-30 crosses SMA-60 of a given blockchain metric → long (cross from below) or short (cross from above).
- **Enhanced signal (AdCPTRA):** Normalize CPTRA SMA-30 by regression-derived max/min bounds → long when AdCPTRA < 0.3, short when AdCPTRA > 0.6.
- **Confirmation:** None required (signal-only).
- **Risk/exit:** 1:1 risk-reward with 30% stop-loss and 30% target (for standard ribbons); 10% for adjusted ribbon variants.

## Signal

### Standard Blockchain Ribbons

- **Formation timestamp:** Daily, end-of-day (closing price and daily blockchain metric values).
- **Lookback:** SMA-30 (short period) and SMA-60 (long period) of each blockchain metric.
- **Long entry:** SMA-30 crosses above SMA-60 of the metric.
- **Short entry:** SMA-30 crosses below SMA-60 of the metric.
- **Exit:** Next crossover signal (reverse position).
- **Holding period:** Variable (depends on time between crossovers).
- **Parameters:** Fixed SMA-30 and SMA-60 windows; 30% stop-loss and 30% target for standard ribbons; 10% for adjusted variants.

### Adjusted CPTRA (AdCPTRA)

- **Construction:** AdCPTRA(t) = (SMA-30(t) − MinLR(t)) / (MaxLR(t) − MinLR(t)), where MaxLR and MinLR are linear regression lines through historical CPTRA monotonic maxima and minima.
- **Long entry:** AdCPTRA < 0.3 (ribbon SMA-10 crosses above SMA-20 of AdCPTRA).
- **Short entry:** AdCPTRA > 0.6 (ribbon SMA-10 crosses below SMA-20 of AdCPTRA).
- **Exit:** Next crossover or threshold breach.

### Adjusted MWNUS, NTRAT, BLCHS

- **Construction:** Time derivative of the metric, smoothed with SMA-10 and SMA-20.
- **Signal:** Crossover of smoothed derivative lines.
- **Parameters:** 10% stop-loss and 10% target.

### Position sizing

Underspecified in the source. The simulations assume equal position sizing per trade with no explicit sizing rule.

## Required data

- **Instrument:** Bitcoin (BTC/USD).
- **Venue:** Not specified (data from Quandl/Nasdaq BCHAIN dataset, aggregated from blockchain network).
- **Market type:** Spot Bitcoin.
- **Timeframe:** Daily bars.
- **Fields:** 21 blockchain metrics including: Hash Rate (HRATE), Mining Difficulty (DIFF), Cost Per Transaction (CPTRA), My Wallet Number of Users (MWNUS), Total Number of Transactions (NTRAT), Blockchain Size (BLCHS), Miners Revenue (MIREV), Market Capitalization (MKTCP), Addresses Used (NADDU), Total Transaction Fees USD (TRFUS), Estimated Transaction Volume USD (ETRVU), and others. See Table 1 in the paper for full list.
- **Point-in-time:** Daily blockchain metrics from Quandl, published daily.
- **Timestamp:** Daily, no explicit timezone stated (assumed UTC or data-vendor default).
- **Missing-data:** Not explicitly addressed. The paper uses continuous daily data from 2010–2022.
- **Funding/fee/spread:** Trading fees assumed at ~1% for crypto markets. No spread or slippage modeled.

## Execution assumptions

- **Signal-to-order timing:** Next-day execution at opening price (assumed, not explicitly stated).
- **Order type:** Market order.
- **Fill model:** Assume immediate full fill at opening price.
- **Fees:** ~1% trading fee per round trip (assumed for crypto markets).
- **Spread:** Not modeled.
- **Slippage:** Not modeled.
- **Leverage:** Not specified (assumed unleveraged).
- **Position limits:** None specified.
- **Failure handling:** Not addressed.

## Evidence

### Source-reported

All figures below are from King, Dale & Amigó (2024), backtested on Bitcoin daily data August 2010 – December 2022:

**Standard ribbons (long + short combined, Table 2):**
- Top 4 metrics outperforming Bitcoin buy-and-hold: NADDU (Strategy Total Profit 5819%), CPTRA (4117%), TRFUS (3416%), TRFEE (2899%).
- MKPRU (buy-and-hold): 2665%.
- 1:1 risk-reward strategy with 30% stop-loss/target.

**Long-only operations (Table 3):**
- Overall winning trade rate: 58.13%.
- DIFF: 78.57% winning trades (14 trades, 11 winners) but low signal frequency.
- CPTRA: 65.22% winning trades, Strategy Total Profit 4467%.
- NADDU: 57.81% winning trades, Strategy Total Profit 4905%.
- HRATE (Hash Ribbon): 57.14% winning trades, Strategy Total Profit 1099%.

**Short-only operations (Table 4):**
- Overall winning trade rate: 42.75% (no statistical advantage).
- Only MKTCP has positive Total Profit (76%).
- All other metrics show negative Total Profit on shorts.

**Adjusted CPTRA (AdCPTRA, Table 5):**
- Long: 71.88% winning trades (32 trades, 23 winners), Strategy Total Profit 1740%.
- Short: 66.67% winning trades (6 trades, 4 winners), Strategy Total Profit 96%.
- AdCPTRA outperforms raw CPTRA on both long and short signals.

**Adjusted variants (Table 6):**
- AdMWNUS long: 56.41% winning trades, Total Profit 469%.
- AdNTRAT long: 56.03% winning trades, Total Profit 438%.
- AdBLCHS long: 56.06% winning trades, Total Profit 124%.

**ML prediction (Table 7):**
- LSTM with percentage-normalized blockchain metrics: MASE 0.74 (test), 0.63 (train) — best performing model.
- Random Forest with raw data shows severe overfitting (RMSE test 12229 vs train 1478).

**Functional dependency (Chatterjee ξ, Table 1):**
- MWNUS: ξ = 0.987 (highest)
- NTRAT: ξ = 0.986
- DIFF: ξ = 0.976
- MKTCP: ξ = 0.973
- HRATE: ξ = 0.902

Source reports these results have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Short signals are unprofitable:** Across all standard blockchain ribbons, short operations show negative Trade Profit and Total Profit. The only exception is MKTCP with marginally positive 76%. The authors acknowledge that blockchain indicators are not effective for short signals.
- **Monotonic metrics cannot form ribbons:** MWNUS, NTRAT, and BLCHS are monotonic functions of time/price, so their raw ribbon lines never cross. The derivative-based adjustment partially addresses this but introduces additional parameter sensitivity.
- **Low signal frequency for top metrics:** DIFF has the highest long winning rate (78.57%) but only 14 trades over 12+ years, raising concerns about statistical significance.
- **Overfitting risk in ML models:** Random Forest with raw blockchain metrics shows severe overfitting (test RMSE 8× train RMSE). Only percentage-normalized inputs reduce this.
- **Regime sensitivity:** The paper tests the 2017–2022 period separately and confirms long signals remain profitable, but the profit margin is "much smaller."
- None identified beyond the above in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Walk-forward / out-of-sample test:** Re-run ribbon signals on Bitcoin data from 2023–2026 using the exact same parameters (SMA-30/60, AdCPTRA thresholds 0.3/0.6). If winning trade rate drops below 50% or Total Profit turns negative on long signals, the alpha claim is weakened.
2. **Parameter sensitivity:** Vary SMA periods (e.g., 20/40, 40/80) and AdCPTRA thresholds (0.2/0.7, 0.4/0.5). If performance is highly sensitive to exact parameter choices, the signal is likely overfit.
3. **Transaction cost stress:** Re-run with realistic taker fees (0.04–0.10% per side for major exchanges) plus estimated spread. The source assumes ~1% fees, which may be conservative for modern exchanges.
4. **Multi-asset replication:** Test the same blockchain metric ribbon approach on Ethereum (if equivalent on-chain metrics are available) to check cross-asset portability.
5. **Comparison baseline:** Compare against a simple buy-and-hold strategy and a standard moving-average crossover on price alone. If blockchain metrics do not outperform these baselines after costs, the information premium is not material.
6. **Metric significance:** Test whether AdCPTRA remains the dominant variable when combined with other on-chain indicators (e.g., MVRV, SOPR, exchange flows) in a multivariate framework.

## Crypto portability

- **Direct** for Bitcoin (the source tests exclusively on BTC).
- **Adapted** for other L1 blockchains: The ribbon methodology (SMA crossover of on-chain metrics) can be applied to Ethereum, Solana, or other chains with public blockchain data, but the specific metrics (hash rate, mining difficulty, cost per transaction) are Bitcoin-specific. Other chains would require chain-specific metric selection.
- **Spot vs perpetual:** The source tests on spot Bitcoin. Applying to perpetual futures would add funding rate dynamics and leverage effects not modeled.
- **24/7 trading:** The source uses daily bars, which aligns with 24/7 crypto markets.
- **Venue fragmentation:** Not addressed. The source uses aggregated daily data.
- **Liquidity:** Not explicitly modeled. The 30% stop-loss/target assumes sufficient liquidity for large moves.

## Limitations

- **Short signals are unprofitable:** The most significant limitation — blockchain metric ribbons provide no statistical advantage for short positions.
- **Low signal frequency:** Top-performing metrics (DIFF, AdCPTRA) generate very few trades (6–32 over 12+ years), making statistical inference fragile.
- **No slippage or spread modeling:** The source assumes ~1% fees but does not model spread or slippage, which can be significant for Bitcoin.
- **Data source quality:** The Quandl/Nasdaq BCHAIN dataset may have gaps or revisions not addressed by the authors.
- **No walk-forward validation:** The paper uses a single in-sample period (2010–2022) with no out-of-sample holdout.
- **Monotonic metric handling:** The derivative-based adjustment for MWNUS, NTRAT, BLCHS introduces additional smoothing parameters (SMA-10/20) without sensitivity analysis.
- **Publication bias:** Published in a physics/complexity journal (Solitons & Fractals), not a finance journal; the financial methodology may lack the rigor of finance-specific peer review.
- **Bitcoin-only:** No cross-asset validation beyond Bitcoin.

## Implementation status

- **Source-reported:** Python simulation code available at https://github.com/JuanCarlosKing/BlockchainIndicatorsSimulations
- **Our implementation:** not-implemented
- **Paper/Backtest:** Source-reported backtest on Bitcoin 2010–2022 with ribbon signals and ML prediction.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** constitute strategy adoption, approval for implementation, or authorization for Paper, Testnet, or Live trading. The source-reported results have not been independently reproduced. The short-signal unprofitability and low trade frequency are significant limitations for practical deployment.

## Related Wiki records

- [[bitcoin-hash-ribbon-miner-capitulation-2026-08-31]] — The original Hash Ribbon indicator (hash rate SMA-30/60 crossover) from LookIntoBitcoin. This paper extends the ribbon concept to 21 blockchain metrics and introduces enhanced variants (AdCPTRA, AdMWNUS, AdNTRAT, AdBLCHS). Materially distinct in scope and mechanism.
- [[bitcoin-onchain-miner-position-index-mpi-outflow-exhaustion-2026-09-01]] — Related on-chain miner metric, but MPI uses exchange flow data rather than mining network metrics.
- [[crypto-open-interest-crash-rebound-flow-gap-2026-09-03]] — Different on-chain signal class (open interest + flow gap vs. mining metrics).

## Sources

1. King, J.C., Dale, R., Amigó, J.M. (2024). "Blockchain Metrics and Indicators in Cryptocurrency Trading." *Solitons & Fractals*, 178, 114305. DOI: 10.1016/j.chaos.2023.114305. arXiv:2403.00770v1. https://arxiv.org/abs/2403.00770
2. GitHub repository: https://github.com/JuanCarlosKing/BlockchainIndicatorsSimulations
3. Quandl/Nasdaq BCHAIN dataset: https://data.nasdaq.com/data/BCHAIN-Block-Chain/
