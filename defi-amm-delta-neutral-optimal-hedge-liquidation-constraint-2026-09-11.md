---
schema: strategy-research-record-v1
title: "Optimal Hedge Ratio for Delta-Neutral Liquidity Provision under Liquidation Constraints"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - delta-neutral
  - liquidity-provision
  - liquidation-risk
status: research-only
confidence: medium
source_as_of: 2026-03-20
sources:
  - "https://arxiv.org/abs/2603.19716v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Optimal Hedge Ratio for Delta-Neutral Liquidity Provision under Liquidation Constraints

## Provenance

- **Primary source:** Atsushi Hane, "Optimal Hedge Ratio for Delta-Neutral Liquidity Provision under Liquidation Constraints," arXiv preprint arXiv:2603.19716v1 [q-fin.PM], published March 20, 2026. URL: https://arxiv.org/abs/2603.19716
- **Author:** Atsushi Hane (Independent researcher, atsushihane@gmail.com)
- **Version:** v1 (March 20, 2026)
- **Paper length:** 26 pages, 4 figures
- **Data:** Calibrated to on-chain data from SUI/NS pool on Sui blockchain (91 days daily CoinGecko price data); replicated across SOL/RAY, SOL/JUP (Solana), and ETH/ARB (Arbitrum) pairs using 365 days of daily CoinGecko data. Monte Carlo simulation with N = 30,000 paths, T = 90 days.
- **Public-use status:** Open-access arXiv preprint.

## Economic mechanism

### Source-reported

The paper studies the problem of hedging the price exposure of liquidity positions in constant-product AMMs (Uniswap v2 style) when the hedge is funded by collateralized borrowing from a lending protocol. The LP borrows constituent tokens and sells them, creating a short position that offsets the LP's long exposure. The core trade-off is three-way: (1) higher hedge ratios reduce price exposure variance, (2) higher hedge ratios increase borrow costs linearly, and (3) higher hedge ratios raise the loan-to-value (LTV) ratio, increasing the probability of forced liquidation. The paper derives that the unconstrained Sharpe-optimal hedge ratio is near-full hedging (h* ≈ 0.977), but at this level the liquidation probability exceeds 19%, making it impractical. The binding liquidation constraint forces the practical optimum down to h** ≈ 60–65%, where liquidation probability drops to 1.4–2.3%.

### Research interpretation

The mechanism is a **liquidation-constrained variance reduction** strategy for DeFi AMM liquidity provision. The alpha (or rather, the risk-adjusted return improvement) comes from partially hedging the directional price exposure of an LP position through collateralized borrowing, while deliberately under-hedging to maintain a safe LTV buffer against forced liquidation. The interior optimum (rather than full hedging) arises structurally from the interaction between: (a) the linear cost of borrowing, (b) the convex reduction in portfolio variance from hedging, and (c) the non-linear increase in liquidation probability as the hedge ratio approaches 1. The strategy earns LP rewards (fees + farming incentives) as the primary return source, with hedging serving purely as a variance-reduction tool. This is a DeFi-native mechanism with no traditional-finance analogue — it exploits the specific structure of AMM pools combined with lending protocol liquidation mechanics.

## Signal

- **Formation timestamp:** Signal is formed continuously as the LP monitors the current hedge ratio drift from target.
- **Lookback:** Volatilities and correlation estimated from daily log returns (91-day or 365-day calibration window, as reported).
- **Entry:**
  - Deposit collateral C (stablecoin) into a lending protocol at ratio C/V0 ≥ 2.0 (research-proposed minimum; source-tested range C/V0 ∈ [1.2, 5.0]).
  - Borrow fractions of tokens A and B proportional to h** × V0 / 2 (where h** ∈ [0.60, 0.65] is the constrained optimal hedge ratio).
  - Use borrowed tokens + spot-purchased tokens to fund the LP position in a constant-product pool.
  - Initial LTV should be approximately 30% (research-proposed target; source reports initial LTV of 25–33% at optimum across collateral configurations).
- **Exit:**
  - Unwind the LP position and repay the borrow when the LP decides to exit (horizon not specified by source; source uses T = 90 days for simulation).
  - The exit strategy is not explicitly specified beyond the simulation horizon.
- **Holding period:** Source uses T = 90 days for simulation. No specific holding period rule is prescribed.
- **Rebalancing:** Threshold-based rebalancing when either token's effective hedge ratio drifts more than 15 percentage points from target (research-proposed threshold; source shows this achieves Sharpe 1.15 with median rebalance frequency of ~62–85 days). Alternative: claim rewards and repay biweekly (reduces liquidation probability by ≈4pp).
- **Parameters:**
  - h** ∈ [0.60, 0.65]: constrained optimal hedge ratio (source-reported, calibrated to on-chain data).
  - C/V0 ≥ 2.0: collateral-to-LP-value ratio (research-proposed minimum).
  - ℓmax = 0.80: maximum LTV threshold (source-reported, typical DeFi lending protocol value).
  - Rebalancing drift threshold: 15pp (research-proposed).
  - Reward claim frequency: biweekly (research-proposed).
- **Position sizing:** Not explicitly specified. Source assumes the LP's position is small relative to the pool and lending market (price-taker assumption).

## Required data

- **Instrument:** Token pair in a constant-product AMM pool (e.g., SUI/NS, SOL/RAY, SOL/JUP, ETH/ARB).
- **Universe:** Constant-product AMM pools on low-gas blockchains where delta-neutral LP strategies are practically viable (Sui, Solana, Arbitrum tested).
- **Venue:** Uniswap v2-style constant-product AMM + lending protocol on the same chain.
- **Market type:** DeFi spot AMM pool + lending protocol.
- **Timeframe:** Daily price data for calibration (91–365 days); simulation uses daily time steps.
- **Fields:** Token prices (S_A, S_B), borrow rates (r_A, r_B), LP reward rate (R/V0), stablecoin supply rate (r_f), max LTV (ℓmax), collateral ratio (C/V0).
- **Point-in-time:** Calibration uses historical daily CoinGecko price data. Borrow rates and reward rates observed at time of calibration.
- **Timestamp:** Daily price observations. No specific timezone requirement.
- **Missing-data:** Not explicitly addressed.
- **Funding/fee/spread:** Borrow rates r_A and r_B (observed from lending protocol); LP reward rate R/V0 (observed from pool); stablecoin supply rate r_f (observed); one-time borrow fee 0.3% + gas costs included in tx-adjusted results. Spread and market impact assumed negligible (price-taker).

## Execution assumptions

- **Signal-to-order timing:** Not specified. Assumed instantaneous execution at observed prices.
- **Next-bar vs same-bar execution:** Assumed same-bar (daily rebalancing at daily boundary).
- **Market / limit order:** Assumed market orders for borrowing and LP deposit.
- **Fill model:** Assumed full fills at observed prices (price-taker).
- **Fees:** One-time borrow fee of 0.3% of borrowed amount + gas costs. LP trading fees included in R/V0.
- **Spread:** Assumed negligible (price-taker assumption).
- **Slippage:** Not explicitly modeled. Source acknowledges large positions may impact pool prices.
- **Impact / capacity:** Source assumes price-taker (small position relative to pool and lending market). Capacity not quantified.
- **Funding:** Borrow rates r_A and r_B are fixed (simplification; source acknowledges they fluctuate in practice).
- **Leverage / margin:** Leverage arises from the borrow position. Initial LTV at h = 0.60 is approximately 30% (collateral C/V0 = 2.0). Max LTV ℓmax = 0.80.
- **Borrow / shorting:** Borrowing from a lending protocol; tokens are sold to create the short leg.
- **Latency:** Not modeled.
- **Partial fills / failures:** Not modeled.
- **Liquidation penalty:** Modeled as 20% of collateral (aggregates protocol liquidation bonus ~5–10%, market-impact slippage, and opportunity cost). Sensitivity tested at 10% and 30%.

## Evidence

### Source-reported

- Under baseline calibration (SUI/NS, σ_A = 0.922, σ_B = 1.084, ρ = 0.72, R/V0 = 0.54, C/V0 = 2.0, T = 90 days):
  - Optimal hedge ratio h** = 60–65%.
  - Raw Sharpe ratio at h = 0.65: 0.95; at h = 0.60: 0.93.
  - Transaction-cost-adjusted Sharpe at h = 0.60: 0.64.
  - Expected ROE at h = 0.60: +3.32% (over 90 days, including tx costs).
  - Liquidation probability at h = 0.60: 1.4%; at h = 0.65: 2.3%.
  - 5% VaR at h = 0.60: -5.8pp.
- Robustness across four token pairs (SUI/NS, SOL/RAY, SOL/JUP, ETH/ARB): h** ∈ [60%, 65%] across all pairs. Sharpe ranges from 0.54 (ETH/ARB) to 0.95 (SUI/NS).
- Sensitivity to correlation ρ ∈ [0, 0.9]: h** remains 60–70%.
- Sensitivity to volatility scaling ±20%: h** shifts from 50% (high vol) to 70% (low vol).
- Sensitivity to LP reward rate: strategy viable at R/V0 ≥ 20%; h** increases with reward rate (40% at R/V0 = 20% to 70% at R/V0 = 70%).
- Jump-diffusion robustness (Merton model, λ = 4/yr, ρ_J = 0.80): h** unchanged at 65%; Sharpe differs by < 0.02.
- Rebalancing: threshold-based 15pp drift rule achieves Sharpe 1.15 with negligible tx costs.

These results are source-reported backtest/simulation results. They have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- At h = 1.0 (full hedging), Sharpe ratio collapses to -0.03 (raw) and liquidation probability reaches 19.2%, confirming that full hedging is dominated by the constrained interior optimum.
- At R/V0 < 20%, the strategy is unviable at any hedge ratio.
- The paper acknowledges that concentrated-liquidity AMMs (Uniswap v3) are not covered, and the optimal h may differ there.
- The paper acknowledges that stochastic borrow/reward rates, regime-switching volatility dynamics, and large-position market impact are not modeled.

## Falsification plan

- **Out-of-sample test:** Re-calibrate volatilities, correlation, and rates from a rolling 91-day window; simulate forward over the next 90 days. Repeat across multiple non-overlapping periods.
- **Alternative universe:** Test on Uniswap v2 pools on Ethereum mainnet (higher gas, different rate dynamics) and on CEX-based perpetual funding rate carry (structurally different but analogous mechanism).
- **Parameter perturbation:** Vary h** by ±10pp from the calibrated optimum; vary C/V0 from 1.2 to 5.0; vary ℓmax from 0.70 to 0.90. Source reports sensitivity tables for most of these.
- **Cost sensitivity:** Test with realistic DeFi gas costs (not just Sui's ~$0.01), including Ethereum mainnet gas spikes. Include MEV / sandwich attack costs for large LP deposits.
- **Capacity test:** Estimate maximum LP position size before borrow rates shift materially or pool price impact becomes non-negligible.
- **Regime breakdown:** Separate bull vs. bear vs. sideways regimes. Source notes liquidation is driven by rising prices (both tokens rising 60%+ simultaneously); test whether the optimal h shifts materially in persistent bull markets.
- **Failure metric:** If the transaction-cost-adjusted Sharpe at h** drops below 0.30, or liquidation probability at h** exceeds 5%, the strategy is materially weakened.
- **Action on failure:** If falsified, investigate whether the interior optimum is an artifact of the GBM calibration or the 20% liquidation penalty assumption; test with empirical price dynamics and protocol-specific liquidation mechanics.

## Crypto portability

direct

The strategy is inherently crypto-native: it depends on the specific structure of constant-product AMMs, lending protocol liquidation mechanics, and token emission reward schedules. There is no traditional-finance analogue.

**Crypto-specific considerations:**
- Spot vs. perpetual: The strategy operates on spot AMM pools, not perpetuals. Funding rate dynamics are irrelevant here.
- 24/7 session: Continuous monitoring is possible; rebalancing can occur at any time.
- Venue fragmentation: Strategy is chain-specific (tested on Sui, Solana, Arbitrum). Cross-chain portability requires chain-specific calibration of rates and liquidation parameters.
- Liquidity: Price-taker assumption may break for large positions; thin markets for long-tail tokens may increase slippage during liquidation.
- Mark / index price: Not applicable (spot AMM).
- Contract specification: AMM pool invariant (x·y = L²) and lending protocol LTV threshold (ℓmax) are the key structural parameters.
- Timestamp / candle boundaries: Daily price data used for calibration; simulation uses daily time steps.
- MEV risk: LP deposits and rebalancing transactions are vulnerable to sandwich attacks and MEV extraction, which are not modeled.

## Limitations

- **GBM dynamics:** Cryptocurrency prices exhibit heavier tails and jumps than GBM. Jump-diffusion robustness test (Merton model with matched variance) leaves h** unchanged, but regime-switching with persistent volatility shifts is untested.
- **Constant rates:** Borrow and reward rates are assumed fixed. In practice, reward rates decline as pool TVL increases (dilution), and utilization-dependent borrow rates can spike during bull markets. Source acknowledges this is a key limitation.
- **Static analytical framework:** The first-passage-time bound assumes a static hedge held over [0, T]. Rebalancing improves Sharpe, implying the analytical bound is conservative.
- **No concentrated liquidity:** Only full-range constant-product pools are considered. Uniswap v3 concentrated liquidity amplifies both IL and fee income, potentially shifting the optimal h.
- **Simplified liquidation:** Fixed 20% collateral penalty assumed. Actual protocols implement partial liquidation, keeper response lags, and variable bonuses.
- **Price-taker assumption:** Large positions may move borrow rates, dilute LP rewards, or impact pool prices. Capacity not quantified.
- **No empirical validation:** All results are from Monte Carlo simulation calibrated to observed parameters. No historical backtest using actual on-chain execution is provided.
- **Single-author independent research:** Not peer-reviewed. No institutional affiliation.
- **Reward rate sensitivity:** Strategy viability depends critically on LP reward rates (R/V0 ≥ 20% required). DeFi farming rewards are funded by token emissions and tend to decline over time.
- **Data gap:** The paper does not specify the exact CoinGecko pool address, lending protocol, or timestamp of parameter observation for the SUI/NS calibration. Reproducibility depends on re-observing current on-chain parameters.

## Implementation status

not-implemented

No implementation in our research stack (NautilusTrader, PyBroker, or any other system) has been completed. This is a pure research capture.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The strategy targets DeFi AMM liquidity provision, which is outside the current NautilusTrader execution scope. Any future implementation would require DeFi-specific execution infrastructure (wallet management, on-chain transaction signing, lending protocol interaction).

## Related Wiki records

- [[quant/defi-amm-continuous-installment-options-lvr-delta-hedge-2026-09-01]] — Related in that both address AMM LP hedging, but Singh et al. models LVR as a continuous-installment option (pricing framework), whereas Hane optimizes the hedge ratio under liquidation constraints (practical optimization). Different mechanisms, different questions.
- [[quant/defi-amm-amortizing-perpetual-options-lvr-hedge-2026-09-01]] — Related DeFi hedging research; distinct mechanism.
- [[quant/ethena-optimal-execution-delta-neutral-steth-perp-carry-2026-09-02]] — Related delta-neutral strategy; targets stETH/ETH perpetual carry, not AMM LP hedging.
- [[quant/ml-optimized-tau-reset-clmm-liquidity-provision-2026-09-06]] — Related AMM LP research; targets concentrated liquidity (CLMM), not constant-product pools.

## Sources

1. Hane, A. (2026). "Optimal Hedge Ratio for Delta-Neutral Liquidity Provision under Liquidation Constraints." arXiv preprint arXiv:2603.19716v1 [q-fin.PM], published March 20, 2026. URL: https://arxiv.org/abs/2603.19716
2. Adams, H., Zinsmeister, N., Salem, M., Keefer, R., and Robinson, D. (2020). "Uniswap v2 Core." Technical report, Uniswap.
3. Milionis, J., Moallemi, C. C., Roughgarden, T., and Zhang, A. L. (2022). "Automated Market Making and Loss-Versus-Rebalancing." arXiv preprint arXiv:2208.06046.
4. Qin, K., Zhou, L., and Gervais, A. (2022). "Quantifying Blockchain Extractable Value: How Dark is the Forest?" In IEEE S&P.
5. Perez, D., Werner, S. M., Xu, J., and Livshits, B. (2021). "Liquidations: DeFi on a Knife-edge." In Financial Cryptography.
