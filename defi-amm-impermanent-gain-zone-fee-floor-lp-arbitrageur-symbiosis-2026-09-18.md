---
schema: strategy-research-record-v1
title: "AMM Impermanent Gain Zone: Fee-Floor Bounds for LP-Arbitrageur Symbiotic Profitability in Constant-Product DEX"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - cpmm
  - impermanent-gain
  - fee-optimization
  - lp-profitability
  - uniswap-v2
  - balancer
status: research-only
confidence: high
source_as_of: 2026-04-30
sources:
  - "Ignat Melnikov, Roman Vlasov, Vladimir Gorgadze, Andrey Seoev, Yury Yanovich. 'From Impermanent Loss to Sustainable Gain: Quantifying Profitability Zones for Liquidity Providers on DEX.' arXiv:2604.28014v1 [cs.DC], April 30, 2026. CC BY 4.0. https://arxiv.org/abs/2604.28014"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AMM Impermanent Gain Zone: Fee-Floor Bounds for LP-Arbitrageur Symbiotic Profitability in Constant-Product DEX

## Provenance

- **Source**: arXiv:2604.28014v1 [cs.DC], April 30, 2026
- **Authors**: Ignat Melnikov (Skolkovo Institute of Science and Technology), Roman Vlasov (Moscow Institute of Physics and Technology), Vladimir Gorgadze (MIPT / IDEAS Center), Andrey Seoev (MEV-X), Yury Yanovich (Skolkovo Institute of Science and Technology)
- **License**: CC BY 4.0
- **URL**: https://arxiv.org/abs/2604.28014
- **PDF**: https://arxiv.org/pdf/2604.28014

## Economic mechanism

### Source-reported

The paper reframes the LP-arbitrageur relationship in constant-product AMMs (Uniswap V2, Balancer) from adversarial to symbiotic. The core insight: the same arbitrage trades that cause Impermanent Loss (IL) for individual LPs also generate the swap fees that compensate them. When the price discrepancy between the DEX and an external reference market (typically a CEX) is sufficiently small, the fees earned from the arbitrage trade exceed the IL caused by the price realignment — creating an "Impermanent Gain" (IG) zone where both arbitrageurs and LPs profit simultaneously.

The paper derives closed-form analytical boundaries for the IG zone in Uniswap V2, a probabilistic framework for estimating how many blocks an LP stays in the IG zone (modeling external price dynamics as Geometric Brownian Motion), and a lower bound on pool fees required to achieve a target probability of remaining profitable. Experimental validation on Polygon (MATIC) demonstrates that even minimal fees (0.03%) regularize arbitrage and stabilize LP returns near zero IL, while zero-fee pools generate 50% more arbitrage activity but expose LPs to IL up to −20 MATIC.

### Research interpretation

This is a DeFi-specific alpha mechanism: in constant-product AMMs, there exists a deterministic zone of price discrepancy where LP positions are net profitable relative to a hold benchmark, bounded by the pool's fee structure and invariant curve. The mechanism is structural — it arises from the mathematical properties of the constant-product formula and fee accrual — rather than behavioral. For a trading strategy, the implication is that LPs who can control their entry price ratio (by timing deposits relative to CEX-DEX price divergence) and who set appropriate fee tiers can systematically harvest the IG zone. The framework also provides a principled fee-selection tool: protocols can set fees as a function of observed volatility to maintain LP profitability with a target confidence level.

## Signal

- **Formation timestamp**: The IG zone boundaries are computed from observable pool parameters (fee tier ϕ₁, ϕ₂, invariant curve) and the current CEX-DEX price ratio. Signal is continuously observable on-chain.
- **Lookback**: Not applicable — the IG zone is a structural property of the AMM, not a time-series signal. The probabilistic IL framework uses GBM calibration from historical volatility (lookback not specified in source).
- **Long entry (LP deposit)**: Deposit liquidity into a constant-product pool when the CEX-DEX price ratio falls within the analytically derived IG zone boundaries. For Uniswap V2 with fee ϕ, the IG zone is defined by the closed-form threshold swap size Δx_max^u (Equation 1 in source) — trades smaller than this threshold generate net impermanent gain for LPs.
- **Short entry**: Not applicable — LP positions are long both assets by construction.
- **Exit**: Withdraw liquidity when the CEX-DEX price ratio exits the IG zone (enters the IL zone), or when the probabilistic framework indicates the LP has exceeded the target number of blocks in the IG zone.
- **Holding period**: Continuous — LP positions earn fees as long as they remain deployed. The probabilistic framework estimates expected blocks until IL.
- **Parameters**: Fee tiers ϕ₁, ϕ₂ (pool-specific, e.g., 0.01%, 0.03%, 0.05%, 0.3%, 1%); volatility σ (for GBM calibration); target IL probability (research-proposed); time horizon T (research-proposed).
- **Position-sizing logic**: Underspecified in source — the paper derives zone boundaries and fee floors but does not prescribe optimal LP position sizing.
- **Multi-timeframe dependencies**: The IG zone is timeframe-independent (structural), but the probabilistic IL timing depends on the chosen observation frequency (block-by-block).
- **Fully specified?**: The IG zone boundaries for Uniswap V2 are fully specified in closed form. The probabilistic IL framework requires GBM calibration (volatility estimate), which is not fully specified in the source.

## Required data

- **Instrument**: Any token pair listed on a constant-product AMM (Uniswap V2, Balancer).
- **Venue**: DEX (Uniswap V2, Balancer) + external reference price (CEX spot or oracle).
- **Market type**: On-chain spot DEX.
- **Timeframe**: Block-level (Ethereum/Polygon block time).
- **Fields**: Pool reserves (x, y), pool marginal price p_dex, external reference price p_cex, fee tier ϕ, LP share value.
- **Point-in-time**: Prices are observable on-chain in real time; no look-ahead issues for zone computation.
- **Timestamp**: Block number / timestamp from the chain.
- **Missing-data**: If CEX price is unavailable or stale, the IG zone computation may be inaccurate. Source does not address oracle latency.
- **Funding/fee/spread**: Gas costs for deposit/withdrawal/rebalancing; swap fees (the LP's income); slippage on large trades. The paper models these conceptually but does not provide a precise quantitative model for gas costs or slippage in the core analysis.

## Execution assumptions

- **Signal-to-order timing**: LP deposit/withdrawal transactions are submitted to the mempool and included in the next block. Timing is block-by-block.
- **Next-bar vs same-bar execution**: On-chain execution is block-by-block; the IG zone is evaluated at each block's state.
- **Market / limit order**: LP deposit is a smart contract interaction (not a traditional order).
- **Fill model**: Deterministic — on-chain transactions are included if gas price is sufficient.
- **Fees**: Gas costs (Ethereum/Polygon); swap fees (ϕ₁, ϕ₂) are the LP's income source.
- **Spread**: Not applicable for LP positions (LPs are the spread provider).
- **Slippage**: LP deposits/withdrawals incur slippage proportional to position size relative to pool reserves. Source does not provide a precise slippage model.
- **Impact / capacity**: LP returns are inversely related to position size relative to pool TVL. The paper does not address capacity constraints.
- **Funding**: Not applicable for spot DEX LP positions.
- **Leverage / margin**: Not applicable.
- **Borrow / shorting**: Not applicable.
- **Latency**: Block inclusion latency (Ethereum ~12s, Polygon ~2s).
- **Partial fills / failures**: On-chain transactions can fail (revert) if conditions change between submission and inclusion.

## Evidence

### Source-reported

- Closed-form IG zone boundaries derived for Uniswap V2 constant-product AMM (Equation 1 in source).
- Probabilistic IL framework: upper bound on one-block probability of IL using GBM price dynamics.
- Fee optimization insight: lower bound on pool fee required to maintain target LP profitability probability.
- On-chain experimental validation on Polygon (MATIC): private pools with whitelisted arbitrageur demonstrated that 0.03% fees stabilize LP returns near zero IL, while zero-fee pools expose LPs to IL up to −20 MATIC but generate 50% more arbitrage volume.
- The framework is validated theoretically and experimentally on Uniswap V2 and Balancer.
- No specific Sharpe, CAGR, or backtest performance numbers are reported — the paper is a theoretical framework with experimental validation, not a backtested trading strategy.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that zero-fee pools, despite higher arbitrage volume, expose LPs to significant IL. This suggests the IG zone is fragile without adequate fee structures.
- The experimental validation is limited to MATIC on Polygon — generalizability to other tokens and chains is not established.
- The GBM assumption for price dynamics may not hold in crypto markets (fat tails, volatility clustering, jumps).
- The paper does not address MEV extraction by sophisticated actors who may front-run LP deposits/withdrawals.

## Falsification plan

- **Required sample**: Reproduce the IG zone computation on a diverse set of Uniswap V2 / Balancer pools across multiple tokens and chains.
- **Relevant regimes**: Test during high-volatility periods (e.g., March 2020, May 2021, November 2022) when CEX-DEX price discrepancies are large and the IG zone may shrink or disappear.
- **Baseline / control**: Compare LP returns in the IG zone vs. outside the IG zone vs. a simple hold strategy.
- **Ablation tests**: (1) Remove the fee structure (zero-fee) to isolate the pure IL effect; (2) Vary the fee tier (0.01% to 1%) to map the fee-profitability frontier; (3) Test with different pool sizes (small vs. large TVL).
- **Cost sensitivity**: Include gas costs, slippage, and MEV costs in the profitability calculation. The paper's experimental validation uses Polygon (low gas), but Ethereum mainnet gas costs could dominate.
- **Out-of-sample requirement**: Test on pools and time periods not used in the paper's calibration.
- **Failure metric or threshold**: If LP returns in the "IG zone" are negative after accounting for gas, slippage, and MEV, the framework fails.
- **What action follows failure**: The IG zone boundaries would need to be recalibrated or the framework would be limited to low-gas environments.

## Crypto portability

direct

The paper is inherently crypto-native — it studies constant-product AMMs (Uniswap V2, Balancer) on EVM-compatible chains. The experimental validation is on Polygon (MATIC). The framework is directly applicable to any constant-product AMM on any EVM chain.

Crypto-specific considerations:
- Gas costs vary dramatically across chains (Ethereum mainnet vs. L2s vs. alternative L1s). The IG zone profitability is highly gas-sensitive.
- MEV extraction by sophisticated actors can erode LP returns even within the theoretical IG zone.
- Oracle latency for p_cex may introduce stale-price risk.
- Pool TVL and trade size affect slippage, which is not fully modeled in the core framework.
- The paper does not address concentrated liquidity AMMs (Uniswap V3), where the IG zone dynamics would be materially different.

## Limitations

- The IG zone framework is derived for constant-product AMMs only (Uniswap V2, Balancer). Extension to concentrated liquidity (Uniswap V3) or other AMM designs is not provided.
- The GBM assumption for price dynamics is a simplification; crypto prices exhibit fat tails, volatility clustering, and jumps that may cause the probabilistic IL bounds to be inaccurate.
- Transaction costs (gas, slippage, MEV) are discussed conceptually but not integrated into the core profitability model. The experimental validation uses Polygon (low gas), which may not generalize.
- The experimental validation is limited to MATIC on Polygon with a whitelisted arbitrageur — a controlled setting that may not reflect real-world adversarial conditions.
- Position-sizing logic is not prescribed — the paper derives zone boundaries but not optimal LP capital allocation.
- The paper does not address the dynamic problem of when to enter/exit LP positions as a function of time-varying volatility and price discrepancy.
- The fee optimization insight is a lower bound, not an optimal fee — actual optimal fees may be higher.
- data gap: The paper does not specify the exact sample period, number of blocks, or statistical significance of the on-chain experimental results.
- data gap: The paper does not quantify the impact of MEV (sandwich attacks, frontrunning) on LP profitability within the IG zone.

## Implementation status

No implementation in our research stack. The paper provides closed-form expressions that could be implemented as a pool-selection or fee-optimization tool, but no backtest or live deployment has been conducted by us.

## Adoption boundary

This record is research material only. A record being present in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The IG zone framework is a theoretical contribution to LP risk assessment, not a validated trading strategy.

## Related Wiki records

- [[defi-amm-jump-diffusion-lvr-decomposition-optimal-block-time-2026-09-08]] — Related AMM LP research focused on LVR decomposition and optimal block time under jump-diffusion prices. The IG zone paper is complementary: it addresses when LPs can profit from arbitrage, while the LVR paper addresses how much LPs lose to arbitrageurs.
- [[crypto-uniswap-v3-just-in-time-jit-liquidity-provision-price-impact-2026-09-01]] — JIT liquidity provision research; the IG zone framework applies to passive LP positions, not JIT strategies.
- [[defi-amm-amortizing-perpetual-options-lvr-hedge-2026-09-01]] — Related DeFi LP research on hedging impermanent loss.

## Sources

1. Ignat Melnikov, Roman Vlasov, Vladimir Gorgadze, Andrey Seoev, Yury Yanovich. "From Impermanent Loss to Sustainable Gain: Quantifying Profitability Zones for Liquidity Providers on DEX." arXiv:2604.28014v1 [cs.DC], April 30, 2026. CC BY 4.0. https://arxiv.org/abs/2604.28014
