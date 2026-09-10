---
schema: strategy-research-record-v1
title: "DeFi CPMM-Oracle Liquidation Dynamics and Fee-Gated OEV Protection"
created: 2026-09-10
updated: 2026-09-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - liquidation
  - MEV
  - OEV
  - AMM
status: research-only
confidence: medium
source_as_of: "2026-09-10"
sources:
  - "Agathe Sadeghi and Zachary Feinstein, 'Liquidation Dynamics in DeFi and the Role of Transaction Fees', arXiv:2602.12104v1 [q-fin.MF, q-fin.TR], February 2026. https://arxiv.org/abs/2602.12104"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeFi CPMM-Oracle Liquidation Dynamics and Fee-Gated OEV Protection

## Provenance

- **Primary Academic Source:** Agathe Sadeghi and Zachary Feinstein (Stevens Institute of Technology, School of Business), "Liquidation Dynamics in DeFi and the Role of Transaction Fees," arXiv preprint `arXiv:2602.12104v1 [q-fin.MF, q-fin.TR]`, submitted February 12, 2026. DOI: [10.48550/arXiv.2602.12104](https://doi.org/10.48550/arXiv.2602.12104). Full text: https://arxiv.org/abs/2602.12104.
- **Repository URL:** https://arxiv.org/abs/2602.12104
- **Version:** v1 (only version at time of capture)
- **Source type:** Peer-reviewed-quality academic preprint (28 pages, 9 figures); no GitHub repository identified.
- **Subject:** q-fin.MF (Mathematical Finance), q-fin.TR (Trading and Market Microstructure), math.DS (Dynamical Systems)
- **Status:** Working paper / preprint. Not published in a journal at time of capture.

## Economic mechanism

### Source-reported

Sadeghi and Feinstein study the optimal liquidation strategy from the liquidator's profit-maximizing perspective when the lending protocol uses a Constant Product Market Maker (CPMM) — specifically Uniswap v2 — as the on-chain spot oracle for the Health Factor (HF) calculation. They show:

1. **Staged liquidations dominate:** Sequential small liquidations (marginal dx units) are strictly more profitable than a single lump-sum liquidation. This follows from profit subadditivity under the constant-product pricing rule.

2. **Sandwich attack on liquidation events:** A liquidator can sell Δ units of collateral to the CPMM to depress the collateral price, trigger a liquidation cascade, complete liquidations, and repurchase Δ at the lower price. This is an Oracle Extractable Value (OEV) attack.

3. **CPMM fees as a critical security parameter:** When the CPMM charges a transaction fee γ > 0, sandwich attacks have a maximum feasible attack size Δ_max = (A₀ + (1-γ)c) / γ. Beyond this, the attacker faces infinite losses because the repurchase cost diverges. Critically, there exists a threshold fee γ* above which ALL sandwich attacks are unprofitable for any attack size Δ > 0. For realistic parameters (θ=85%, ℓ=5%, CF=80%, κ=50%, A₀=10,000, B₀=28,000,000, b=32,000, c=20.12), the critical threshold is γ* ≈ 0.17%.

### Research interpretation

The economic mechanism is CPMM price impact acting as an endogenous deterrent to OEV manipulation. The constant-product invariant creates quadratic price impact, and when transaction fees are layered on top, the marginal cost of the final repurchase step in a sandwich attack exceeds the marginal profit. This is a market-structure / mechanism-design result rather than a traditional alpha signal. The falsifiable hypothesis is: **on lending protocols using CPMM spot oracles (not TWAP), AMM fee rates above γ* endogenously prevent profitable sandwich-based liquidation manipulation.**

The paper assumes the lending protocol uses the instantaneous CPMM spot price (not TWAP) for HF calculation. This is a simplification; the authors note that production protocols (Aave, Compound) typically use TWAPs or off-chain oracles, which sacrifice responsiveness for robustness.

## Signal

The paper does not propose a direct trading signal for discretionary traders. Instead, it characterizes the structural parameters under which:

- **Liquidator optimal strategy:** Sequential small liquidations until HF recovers to CF (closing factor), followed by one final large liquidation (Algorithm 1 in the paper).
- **Attacker decision boundary:** Whether a sandwich attack on a liquidation event is profitable given pool depth (A₀, B₀), fee rate γ, liquidation bonus ℓ, and position parameters (c, b, θ, CF, κ).
- **Oracle protection threshold:** For given protocol parameters, there exists γ* such that all sandwich attacks are unprofitable when γ ≥ γ*.

The signal is not "go trade this" but rather "this structural relationship holds and can be verified":

- Staged liquidations dominate lump-sum liquidations (Lemma 1, proven).
- For γ = 0: larger sandwich attacks always yield higher profit (Proposition 3).
- For γ > 0: maximum attack size is bounded; beyond γ*, all attacks are unprofitable (Proposition 3, Example 5).

**Signal formation timestamp:** N/A — this is a structural result, not a time-series signal.
**Parameters:** The critical fee threshold γ* depends on pool depth, position size, liquidation parameters, and is computed numerically for each scenario. No single universal number; the paper's Example 5 finds γ* ≈ 0.17% for their specific parameterization.

## Required data

- **Instrument:** DeFi lending protocol collateral/debt pairs (e.g., ETH/USDC on Aave) with CPMM oracle (Uniswap v2 or similar).
- **Universe:** DeFi lending protocols that use on-chain CPMM spot prices as oracles (not TWAP or Chainlink).
- **Venue:** On-chain (Ethereum mainnet, Uniswap v2 / v3, Aave v2 / v3).
- **Timeframe:** Intra-block (single-block optimization).
- **Fields:** AMM reserves (A, B), collateral amount (c), debt amount (b), health factor (HF), liquidation threshold (θ), liquidation bonus (ℓ), closing factor (CF), liquidation fraction (κ), transaction fee (γ).
- **Point-in-time:** On-chain state is deterministic and point-in-time by construction.
- **Timestamp:** Block-level granularity; all actions occur within a single block.
- **Missing-data:** Gas costs are abstracted away (upper bound on attacker profitability). Flash loan costs assumed zero.

## Execution assumptions

- **Signal-to-order timing:** All actions within a single block (sandwich attack + liquidation + repurchase).
- **Fill model:** Deterministic CPMM pricing (constant product invariant).
- **Fees:** CPMM transaction fee γ is the critical parameter; gas costs are ignored.
- **Slippage:** Explicitly modeled through the CPMM price impact curve.
- **Market impact:** Permanent price impact from CPMM trades is the core mechanism.
- **Flash loans:** Assumed available at zero cost (Remark 3).
- **Leverage / margin:** Not applicable (liquidation mechanics, not position construction).
- **Latency:** Block-level; MEV relays assumed.
- **Fill failures:** Not modeled.

The paper explicitly acknowledges these are upper-bound assumptions: gas costs and execution frictions would further compress manipulation incentives in practice (Section 5, Discussion).

## Evidence

### Source-reported

This is a theoretical/analytical paper (dynamic programming + closed-form results + numerical examples). No empirical backtest or live trading results. Key findings:

- **Lemma 1 (proven):** Sequential small liquidations strictly dominate lump-sum liquidations. Profit π_liq = B((1-γ)(1+ℓ)-1)·x_liq / (A + x_liq(1-γ)(1+ℓ)).
- **Proposition 2 (proven):** Maximum feasible sandwich attack size Δ_max = (A₀ + (1-γ)c) / γ for γ > 0; infinite for γ = 0.
- **Proposition 3 (proven):** For γ = 0, limiting attack profit = B₀c/(A₀+c). For γ > 0, limiting attack profit = −∞.
- **Example 5 (numerical):** With A₀=10,000, B₀=28,000,000, γ=0.3%, θ=85%, ℓ=5%, CF=80%, κ=50%, b=32,000, c=20.12: all sandwich attacks are unprofitable for Δ > 0. Critical threshold γ* ≈ 0.17%.
- **Key trade-off:** Higher AMM fees make oracles safer but increase trading costs for legitimate LPs and borrowers.

All results are analytical proofs or numerical examples; no backtest Sharpe/return/drawdown figures.

### Independently reproduced

Not independently reproduced. The results are analytical proofs; reproduction would require re-derivation or numerical verification with the paper's stated parameterizations.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result. The paper does not consider:
- Cross-block strategies (only single-block analysis).
- Gas costs, priority fee competition, or competitive MEV.
- Multi-block TWAP manipulation.
- Liquidity fragmentation across venues.
- Protocol-specific quirks (Aave V3 e-mode, Compound III hooks).

## Falsification plan

1. **Empirical verification of γ*:** For known lending protocols using CPMM spot oracles, compute the empirical γ* from on-chain parameters and verify that sandwich attack profitability transitions from positive to negative around γ*.
2. **On-chain replay:** Replay historical liquidation events on protocols using Uniswap v2/v3 spot oracles; measure actual liquidator profits vs. model predictions.
3. **Parameter sensitivity:** Vary pool depth (A₀, B₀), position size (b, c), and liquidation parameters (θ, ℓ, CF, κ) to verify the model's predictions about when staged vs. lump-sum dominates and when attacks become unprofitable.
4. **Out-of-sample (different AMMs):** Test whether the results generalize beyond CPMM to other AMM types (e.g., Curve StableSwap, concentrated liquidity).
5. **Gas cost inclusion:** Add realistic gas costs and priority fee bidding to determine whether the security margin is larger or smaller than the theoretical model suggests.
6. **Failure metric:** If actual on-chain liquidator profits under sandwich attacks are positive and persistent for γ > γ*, reject the fee-as-protection hypothesis.

## Crypto portability

direct

The paper is entirely about on-chain DeFi mechanics (CPMM, lending protocols, MEV). The analysis is native to crypto and directly applicable to:
- Ethereum mainnet Uniswap v2/v3 oracles
- Any EVM-compatible chain with CPMM-based lending oracle designs
- Cross-chain: results hold wherever the CPMM invariant and fee structure apply

**Crypto-specific risks:**
- Gas cost variability can change the effective γ*.
- MEV searcher competition may prevent any individual liquidator from executing the optimal strategy.
- Flash loan availability and cost vary by protocol/chain.
- Different AMM designs (concentrated liquidity, Curve) may have different security thresholds.
- 24/7 operation means liquidation events can occur at any time.

## Limitations

- **Theoretical only:** No empirical validation, no backtest, no live results.
- **Single-block scope:** Cross-block strategies, TWAP manipulation, and multi-block MEV are not considered.
- **CPMM-specific:** Results assume constant-product AMMs; concentrated liquidity (Uniswap v3), StableSwap, and other AMM designs may have different properties.
- **Gas costs omitted:** The model provides an upper bound on attacker profitability; real-world profitability is likely lower.
- **No competitive dynamics:** Only a single attacker is modeled; competitive MEV bidding among multiple searchers is not considered.
- **Parameter-dependent:** The critical fee threshold γ* varies with pool depth, position size, and protocol parameters; no universal constant.
- **Flash loan assumption:** Zero-cost flash loans are assumed; in practice, flash loan fees or constraints may limit attack feasibility.
- **Not independently reproduced.**

## Implementation status

Not implemented. This is a theoretical analysis providing structural results about DeFi liquidation dynamics and oracle security. No trading strategy or implementation artifact exists in our research stack.

## Adoption boundary

This record is research material only. Its presence does not imply:
- A profitable trading strategy
- Validated alpha
- Approved implementation
- Paper/testnet/live trading authorization

The paper's primary contribution is mechanism-design insight (fees as oracle protection) rather than a directly tradeable signal. It could inform:
- Protocol design decisions (choosing fee rates for oracle security)
- Risk management (understanding liquidation mechanics and MEV exposure)
- Hypothesis generation for DeFi-specific alpha research

## Related Wiki records

- `[[quant/defi-lending-collateral-liquidation-discount-arbitrage-2026-09-01]]` — Different mechanism: collateral discount arbitrage during liquidation vs. optimal liquidation strategy and OEV protection.
- `[[quant/defi-cross-chain-oracle-latency-speculative-liquidation-mev-2026-09-07]]` — Different mechanism: cross-chain oracle latency exploitation vs. single-block CPMM oracle manipulation.

No directly related records share the same source identity.

## Sources

1. Agathe Sadeghi and Zachary Feinstein, "Liquidation Dynamics in DeFi and the Role of Transaction Fees," arXiv preprint `arXiv:2602.12104v1 [q-fin.MF, q-fin.TR]`, February 12, 2026. DOI: [10.48550/arXiv.2602.12104](https://doi.org/10.48550/arXiv.2602.12104). https://arxiv.org/abs/2602.12104.
