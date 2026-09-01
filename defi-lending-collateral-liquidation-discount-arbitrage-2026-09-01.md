---
schema: strategy-research-record-v1
title: DeFi Collateral Liquidation Discount Arbitrage in Protocols for Loanable Funds
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - lending
  - liquidation
  - collateral-discount
  - mev
  - arbitrage
status: research-only
confidence: high
source_as_of: 2021-11
sources:
  - https://doi.org/10.1145/3487552.3487813
  - https://arxiv.org/abs/2106.06389
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeFi Collateral Liquidation Discount Arbitrage in Protocols for Loanable Funds

## Provenance

- **Primary peer-reviewed source:** Kaihua Qin, Liyi Zhou, Pablo Gamito, Philipp Jovanovic, and Arthur Gervais, "An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities", *Proceedings of the 21st ACM Internet Measurement Conference (IMC '21)*, November 2021, Pages 336–350. DOI: https://doi.org/10.1145/3487552.3487813.
- **Preprint / working version:** arXiv preprint arXiv:2106.06389 (June 2021). URL: https://arxiv.org/abs/2106.06389.
- **Empirical scope:** Historical on-chain data across the four major Ethereum DeFi lending protocols—Aave (v1/v2), Compound (v2), MakerDAO, and dYdX—representing over 85% of the total loanable funds market during the study period.
- **Core dataset:** Comprehensive liquidation event logs, oracle updates, and smart contract execution traces from protocol genesis through 2021.

## Economic mechanism

### Source-reported

Qin et al. (2021) investigate the structural mechanisms and empirical profitability of collateral liquidations in decentralized lending protocols (protocols for loanable funds / PLFs).

DeFi lending platforms rely on over-collateralization to maintain protocol solvency without traditional identity or credit underwriting. When the market value of a borrower's pledged collateral relative to their outstanding debt drops below a specified liquidation threshold (i.e. Health Factor $HF < 1.0$), the position becomes undercollateralized and eligible for liquidation.

The authors categorize liquidation architectures into two principal models:
1. **Fixed-Spread Liquidations (Compound, Aave, dYdX):**
   External liquidators are permitted to repay a fraction of the borrower's debt (governed by the protocol's *close factor*, e.g., 50% of outstanding debt) in exchange for seizing an equivalent value of collateral plus a fixed liquidation bonus discount $B$ (typically 5% to 10% below current oracle price).
2. **Auction-Based Liquidations (MakerDAO):**
   Collateral is sold through on-chain collateral auctions (Dutch or English auction formats) where liquidators bid debt tokens (e.g. DAI) to claim collateral lots over an extended multi-block auction window.

Liquidators systematically combine flash loans with decentralized exchange (DEX) swaps to execute atomic, riskless liquidations:
- Flash-borrow the required debt asset $D$ (e.g. USDC, DAI).
- Call `liquidateBorrow()` on the lending pool, repaying debt $D$ and receiving seized collateral $C$ at bonus discount $B$.
- Instantly swap collateral $C$ back to debt asset $D$ on an AMM (e.g. Uniswap/SushiSwap).
- Repay the flash loan $D + \text{FlashLoanFee}$ and retain the remaining surplus as profit $\pi$, all within a single Ethereum transaction.

### Research interpretation

This is an event-driven, structural arbitrage strategy exploiting protocol-mandated liquidation discounts and automated MEV execution.

The predictive alpha vector is not time-series directional forecasting; rather, it is:
1. **Collateral Health Monitoring / Liquidation Triggering:** Pre-calculating pending price oracle updates (e.g., Chainlink or DEX TWAP price pushes in the mempool) to identify borrower positions that will transition from $HF \ge 1.0$ to $HF < 1.0$ within the upcoming block.
2. **Atomic Discount Extraction:** Capturing the fixed bonus spread ($B \approx 5\% - 10\%$) while hedging or eliminating inventory holding risk via flash loans and instantaneous AMM execution.
3. **Execution Edge:** Submitting atomic bundles via private builder auctions (e.g. Flashbots) to secure priority execution right after the oracle price update transaction.

## Signal

Normalized source-backed rule:

1. **Position Health Evaluation**:
   For each active borrower account $j$ in lending pool $k$, calculate the point-in-time Health Factor:
   $$HF_j = \frac{\sum_{i \in \text{Collateral}} C_{i, j} \cdot P_i \cdot LT_i}{\sum_{m \in \text{Debt}} D_{m, j} \cdot P_m}$$
   where $C_{i, j}$ is deposited collateral amount, $P_i$ is oracle price, $LT_i$ is the liquidation threshold for asset $i$, and $D_{m, j}$ is borrowed debt.

2. **Trigger Condition**:
   A liquidation signal triggers whenever $HF_j < 1.0$.

3. **Repayment & Seizure Sizing**:
   - Compute the maximum allowed debt repayment amount:
     $$d_{\text{repay}}^* = \min\left(D_{\text{target}}, \text{CloseFactor} \times D_{\text{total}, j}\right)$$
   - Calculate the nominal collateral amount seized including liquidation bonus $B$:
     $$c_{\text{seize}} = \frac{d_{\text{repay}}^* \cdot P_{\text{debt}} \cdot (1 + B)}{P_{\text{collateral}}}$$

4. **Profitability Simulation & Net Spread**:
   Simulate the full atomic flash-swap execution:
   $$\pi_{\text{net}} = \text{AMM\_SwapOut}(c_{\text{seize}} \to \text{DebtAsset}) - d_{\text{repay}}^* - \text{FlashFee} - \text{GasCost} - \text{BuilderTip}$$
   Execute only if $\pi_{\text{net}} > \text{MinProfitThreshold} > 0$.

Underspecified / implementation gaps from source:
- Dynamic adjustment of builder bribe percentage in high-congestion gas wars.
- Multi-token collateral liquidation sequencing when a borrower holds multiple collateral and debt assets simultaneously.

## Required data

- Full on-chain state of active lending protocol contracts (Aave, Compound, MakerDAO, Spark, Morpho).
- Chainlink / Pyth / DEX oracle price feeds and pending oracle update transactions in the mempool.
- Real-time AMM pool reserve states and depth across all relevant collateral-debt swap pairs.
- Gas price, EIP-1559 base fee, and Flashbots / MEV-Boost RPC endpoints.

## Execution assumptions

- Execution must be atomic within a single smart contract call. If price slippage on the AMM or gas costs render $\pi_{\text{net}} \le 0$, the contract must revert immediately.
- Flash loan availability for the required debt asset with deterministic fee schedule (e.g., 0.05% on Balancer or 0.09% on Aave).
- Private transaction routing via MEV block builders to prevent public frontrunning and avoid paying reverted gas fees.

## Evidence

### Source-reported

- Qin et al. (2021) analyzed over 85% of the total loanable funds market on Ethereum (Aave v1/v2, Compound v2, MakerDAO, dYdX).
- Fixed-spread protocols (Compound, Aave) were found to provide highly consistent positive gross margins for liquidators due to guaranteed liquidation bonuses ($5\%$ to $10\%$), but resulted in excessive collateral seizure from borrowers.
- In contrast, the authors documented that auction-based designs (such as MakerDAO) suffered significant operational instability during market crashes: they identified **641 unprofitable liquidations** on MakerDAO that resulted in a collective loss of **467.44K USD** for liquidators, driven by collateral price declines during multi-block auction execution windows.
- Liquidator competition concentrated heavily into priority gas auctions (PGAs) and builder bribes, transferring substantial portions of gross liquidation rewards to miners/validators.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Market efficiency and builder co-location: Modern DeFi liquidations are intensely contested by specialized MEV searchers. In liquid pairs (e.g. WETH/USDC), searchers routinely bid >95% of the net liquidation bonus to block builders.
- AMM liquidity depth constraints: In severe market-wide drawdowns, DEX liquidity depth for illiquid collateral assets dries up or experiences extreme slippage, causing the AMM swap output to fall below the flash loan repayment amount and leading to failed/unprofitable liquidations.
- Protocol bad debt risk: If collateral price drops faster than oracles update or liquidators can execute, positions become underwater ($HF \ll 1.0$ where collateral value $<$ debt), causing liquidations to cease and leaving protocol bad debt.

## Falsification plan

1. Historical replay backtesting: Extract historical borrower health factor trajectories across Aave and Compound on Ethereum, Arbitrum, and Base (2022–2026).
2. Slippage & Flash Loan Simulation: Simulate exact DEX pool routing and flash loan fees for each liquidation event.
3. Competitive margin evaluation: Measure the net searcher residual margin after subtracting historical top-of-block builder tips.
4. Falsification criteria: Reject the standalone alpha thesis if net searcher margin after builder bribes and gas costs is non-positive or if capital returns fail to exceed the risk-free rate over a 60-day out-of-sample evaluation period.

## Crypto portability

direct

Natively designed for decentralized finance lending protocols and EVM smart contracts. Directly applicable across all EVM-compatible lending markets (Aave v3 on Ethereum/Arbitrum/Optimism/Base/Polygon, Compound v3, Spark, Morpho) and non-EVM lending protocols (e.g. Kamino / MarginFi on Solana, Suilend on Sui) with appropriate protocol-specific liquidation interfaces.

## Limitations

- Pure MEV competition: Residual searcher profit margins are heavily compressed by competitive builder bidding.
- MEV builder latency: Success depends on ultra-low latency infrastructure and direct builder connectivity.
- Oracle update frontrunning / backrunning precision: Requires millisecond-level mempool parsing to position liquidation transactions immediately after oracle price updates.
- Research-only status; not a standard time-series asset-pricing strategy and cannot be evaluated using traditional OHLCV backtesters without EVM execution state simulators.

## Implementation status

Research-only. No PyBroker, NautilusTrader, paper, testnet, or live trading implementation has been completed.

## Adoption boundary

This record is staging-layer research material only. It does not constitute an implementation directive or approval for paper, testnet, or live deployment.

## Related Wiki records

- `crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31`
- `dex-cyclic-arbitrage-constant-product-amm-2026-09-01`

## Sources

1. Qin, Kaihua; Zhou, Liyi; Gamito, Pablo; Jovanovic, Philipp; Gervais, Arthur. "An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities." *Proceedings of the 21st ACM Internet Measurement Conference (IMC '21)*, November 2021, pp. 336–350. DOI: https://doi.org/10.1145/3487552.3487813
2. Qin, Kaihua; Zhou, Liyi; Gamito, Pablo; Jovanovic, Philipp; Gervais, Arthur. "An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities." *arXiv preprint arXiv:2106.06389* (2021). URL: https://arxiv.org/abs/2106.06389
