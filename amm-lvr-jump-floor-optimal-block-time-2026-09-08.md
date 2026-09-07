---
schema: strategy-research-record-v1
title: "AMM LP Loss-Versus-Rebalancing Jump Floor and Optimal Block Time under Jump-Diffusion"
created: 2026-09-08
updated: 2026-09-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - lvr
  - jump-diffusion
  - liquidity-provision
  - block-time
  - adverse-selection
status: research-only
confidence: high
source_as_of: 2026-08-31
sources:
  - "Nils Bundi, 'Optimal Block Time for AMM Liquidity Providers under Jump-Diffusion Prices', arXiv:2608.30321v1 [q-fin.MF], August 31 2026. https://arxiv.org/abs/2608.30321"
  - "Extended version accepted at MARBLE 2026; to be published by Springer Nature in Mathematical Research for Blockchain Economy (Lecture Notes in Operations Research)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AMM LP Loss-Versus-Rebalancing Jump Floor and Optimal Block Time under Jump-Diffusion

## Provenance

- Paper: arXiv:2608.30321v1 [q-fin.MF], submitted August 31, 2026.
- Author: Nils Bundi (ORCID 0000-0003-3576-3289), Zurich University of Applied Sciences (ZHAW), School of Engineering, Winterthur, Switzerland.
- Subjects: Mathematical Finance (q-fin.MF); Probability (math.PR); Trading and Market Microstructure (q-fin.TR).
- Publication status: Extended version of a paper accepted at MARBLE 2026 (Lecture Notes in Operations Research, Springer). Adds full proofs (Appendix A) and supporting illustrations (Appendix B).
- Replication: All results are closed-form or evaluated by standard quadrature; no external code repository provided.
- Data: Binance ETH/USDT 5-minute closes, January 2020–June 2026 (2,373 days). Jump parameters (λ, δ) estimated via Lee-Mykland jump-detection test at the 1% level, with jump sizes corrected for diffusive component. Diffusion volatility σ estimated by bipower variation from continuous-part realized variance.

## Economic mechanism

### Source-reported

The paper extends the Loss-Versus-Rebalancing (LVR) framework of Milionis et al. (2025) from a geometric Brownian motion (GBM) reference price to a jump-diffusion reference price. Under GBM, the LVR rate is σ²V/8 and is independent of block time; with fees and discrete block arrivals, shorter blocks reduce LVR by reducing the probability of a profitable arbitrage block. The prevailing industry intuition—"shorten blocks to reduce LVR"—follows from this.

Under jump-diffusion, Bundi shows the LVR rate decomposes additively into:

1. A **diffusion channel**: σ²V/8 · F(γ/(σ√Δt)), governed by block time Δt, which vanishes as Δt→0.
2. A **jump channel**: λV · G(γ; m, δ²), which carries **no Δt dependence** and forms an irreducible floor ℓ(Δt) ≥ λVG > 0 that no block-time reduction can eliminate.

The jump channel arises because price jumps produce instantaneous, Δt-independent gaps in the no-arbitrage band. Faster blocks clear each gap sooner but do not make it smaller; the LP absorbs the concavity loss regardless of block cadence.

At Ethereum's 12-second slot: total LVR rate is 471 bp/yr, jump floor is 125 bp/yr (only ~27% of LP loss is schedule-addressable). At Solana's 400ms slot: the jump channel already dominates (43% diffusion share). The floor is approached as √Δt (Corollary 1).

When netting LVR against per-block consensus cost, the LP-side optimal block time is **invariant in pool size and all jump parameters** (λ, m, δ): jumps shift the welfare level but not the planner's marginal tradeoff. Only volatility (σ), fee tier (γ), and consensus cost (c) set the optimum. At calibrated parameters: ∆t_opt ≈ 8.4 seconds.

### Research interpretation

The core falsifiable hypothesis is that AMM LP adverse selection loss has two separable components: one addressable by protocol-level block-time design (diffusion channel) and one that is an irreducible floor set by the jump intensity and size distribution of the underlying price process (jump channel). This implies:

- Sub-second block times (as pursued by Solana and Ethereum L2s) primarily suppress only the diffusion channel; the jump channel remains untouched.
- LP yield strategies on AMMs cannot fully eliminate adverse selection by relying on faster settlement alone.
- Fee tier design (γ/δ ratio) is the lever against jump-LVR, not block time.
- The optimal block time for LP welfare is a chain-level property (set by σ, γ, c), not a pool-level property (independent of TVL V and jump parameters).

This is a ported hypothesis from mathematical finance to DeFi: the LVR framework and jump-diffusion model are standard in quantitative finance, but the additive decomposition and the irreducible floor result are novel contributions to the AMM/DeFi literature.

## Signal

### Formation timestamp
The signal is structural/protocol-level, not a trade-by-trade alpha signal. The LVR rate and optimal block time are properties of the AMM design and the price process, formed continuously and observable from chain state and external price feeds.

### Lookback
Jump parameters (λ, δ) are estimated from historical 5-minute closes over the full sample (Jan 2020–Jun 2026). σ is estimated by bipower variation from the same sample. These are regime-dependent and would need periodic re-estimation in live deployment.

### Entry (research-proposed)
For an LP evaluating whether to provide liquidity on a specific AMM pool:
- Compute or estimate the jump intensity (λ) and jump size distribution (δ) of the reference asset.
- Compute the diffusion volatility (σ) from realized variance.
- Evaluate the LVR rate ℓ(Δt) using Theorem 2 (equation 12): diffusion contribution F(κ) + jump floor G(γ; m, δ²).
- Compare ℓ(Δt) against expected fee income and impermanent-gain scenarios.
- The LP should not expect block-time reductions alone to eliminate jump-LVR.

### Exit (research-proposed)
The paper does not specify entry/exit rules for LP positions; the LVR rate is a continuous cost rate. LP exit decisions would depend on comparing accumulated LVR against fee income over the holding period.

### Holding period
Continuous; the LVR rate is a per-unit-time cost that applies regardless of LP position duration.

### Parameters (source-reported unless noted)

| Parameter | Value | Source |
|-----------|-------|--------|
| σ (diffusion volatility) | 0.8156 | Calibrated from ETH/USDT 5-min closes (Jan 2020–Jun 2026) |
| λ (jump intensity) | 283.3/yr | Lee-Mykland jump detection at 1% level |
| m (mean log jump) | 0 | Symmetric jumps; sample ĉm = −0.0012, 99% CI contains zero |
| δ (std of log jump) | 0.0192 | Lee-Mykland jump detection |
| γ (swap fee) | 0.0005 (5 bps) | Uniswap 0.05% tier |
| V (pool TVL) | $1,000,000 | Modeling choice |
| c (consensus cost per block per $1M TVL) | 260 × 10⁻⁵ USD/block | Derived from Ethereum gross issuance (~$1.7B/yr), V_ETH ≈ $208B, staking ratio ~30% |

### Position sizing
Not specified by the source. The LVR analysis applies per unit of LP capital; absolute sizing depends on TVL and pool depth.

### Multi-timeframe dependencies
Not applicable; the analysis operates at the protocol/block-time timescale.

### Fully specified vs. underspecified
The mathematical framework (Theorems 1–4, Lemmas 1–2, Proposition 1, Corollary 1) is fully specified for CPMM under Merton jump-dusion with symmetric jumps. The calibration to ETH/USDT is specific and reproducible. Operational LP decisions (entry timing, range selection, hedging) are underspecified by the paper.

## Required data

- **Instrument**: ETH/USDT on Uniswap (CPMM, full-range).
- **Venue**: Uniswap (on-chain); external reference price from Binance.
- **Market type**: On-chain spot AMM pool.
- **Timeframe**: 5-minute closes for parameter estimation; block-level for LVR evaluation.
- **Fields**: OHLCV (for jump detection and σ estimation); pool reserves (x, y) and marginal price P; external reference price S.
- **Point-in-time**: All parameters estimated from realized historical data; no look-ahead bias in the calibration.
- **Timestamp**: ETH block timestamps; Binance candle timestamps (UTC).
- **Missing-data**: Not addressed; assumes continuous price observation between blocks.
- **Funding/fee/spread**: Proportional swap fee γ; no explicit funding rate modeling (applicable to spot AMM, not perpetuals).

## Execution assumptions

- **Signal-to-order timing**: Not applicable; the paper analyzes LP loss, not active trading.
- **Fill model**: Full arbitrageur execution at block arrival when |log(S/P)| > γ; no partial fills.
- **Fees**: Proportional fee γ deducted from arbitrageur profits; LPs receive fee income.
- **Slippage**: CPMM constant-product invariant handles slippage implicitly through pool price movement.
- **Impact**: LVR itself is the adverse-selection cost; market impact of LP deposits/withdrawals is not modeled.
- **Leverage/margin**: Not applicable; LP positions are unleveraged.
- **Latency**: Arbitrageur observes external price continuously; trades only at block inclusion.
- **Funding**: Not applicable (spot AMM).
- **Per-block consensus cost**: Modeled as c/Δt (resource cost per pool proportional to TVL/Vchain).
- **What source omits**: LP deposit/withdrawal gas costs; LP capital opportunity cost; MEV redistribution dynamics; concentrated liquidity (CLMM) effects; oracle freshness beyond block time; multi-pool arbitrage dynamics.

## Evidence

### Source-reported

Source-reported results (calibrated to ETH/USDT, Jan 2020–Jun 2026):

| Metric | Value | Condition |
|--------|-------|-----------|
| Diffusion ceiling σ²V/8 | 832 bp/yr | Δt→∞ |
| Jump floor λVG | 125 bp/yr | Δt→0 |
| Total LVR ℓ(12s) | 471 bp/yr | Ethereum L1, 12s slot |
| Total LVR ℓ(2s) | 312 bp/yr | Base/OP L2 |
| Total LVR ℓ(400ms) | 221 bp/yr | Solana |
| Total LVR ℓ(250ms) | 203 bp/yr | Arbitrum |
| Total LVR ℓ(50ms) | 162 bp/yr | App-chain |
| Diffusion share at 12s | 73% | Baseline |
| Diffusion share at 400ms | 43% | Baseline |
| Diffusion share at 50ms | 23% | Baseline |
| Fee discount on jump term | 4.1% | Ψ(γ/δ) = 0.959 at γ/δ = 0.0260 |
| Optimal block time | 8.4s | Baseline c = 260 × 10⁻⁵ |
| Remainder envelope at 12s | [−0.653, +0.849] bp/yr | Proposition 1 |

Sensitivity (Table 3 in source, at Δt = 12s):

| σ \ λ | 71/yr | 283/yr | 1133/yr | 4533/yr |
|-------|-------|--------|---------|---------|
| 0.30 | 55 (43%) | 148 (16%) | 524 (4%) | 2027 (1%) |
| 0.816 | 377 (92%) | 471 (73%) | 847 (41%) | 2349 (15%) |
| 1.50 | 1625 (98%) | 1719 (93%) | 2095 (76%) | 3597 (44%) |

Optimal block time sensitivity:

| c (×10⁻⁵ USD/block) | Δt_opt (s) |
|----------------------|------------|
| 500 | 15.4 |
| 260 | 8.4 |
| 90 | 3.4 |
| 30 | 1.4 |
| 2 | 0.20 |

Volatility sensitivity: σ ∈ {0.30, 0.815, 1.50} → Δt_opt ∈ {62.3, 8.4, 2.5}s.

These results have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

The paper notes several important limitations that function as implicit negative constraints:
- The analysis is for CPMM (full-range Uniswap V2 style); concentrated liquidity AMMs (Uniswap V3) may have different LVR dynamics within active tick ranges, though Milionis et al. (2025, Remark 1) state the LVR construct applies within active tick ranges.
- The calibration uses ETH/USDT specifically; jump parameters are regime-dependent and differ across assets and time periods.
- The LVR rate is only one input to block-time welfare; MEV redistribution, oracle freshness, finality, and decentralization are not included in the LP-side optimum.
- The paper does not model LP hedging strategies that could offset jump-LVR.

## Falsification plan

1. **Empirical LVR measurement**: Implement LVR computation on historical Uniswap V2 ETH/USDT pool data and compare against the theoretical decomposition. Required: on-chain pool state + external price feeds. Failure: if measured LVR does not match the additive decomposition within the stated bounds.

2. **Jump parameter regime stability**: Re-estimate (λ, δ) across sub-periods (e.g., yearly) and check whether the jump floor is stable or regime-dependent. Failure: if the jump floor varies by more than 2× across sub-periods, the static calibration is unreliable for forward-looking LP decisions.

3. **CLMM extension**: Test whether the additive decomposition holds for concentrated liquidity AMMs (Uniswap V3). Failure: if concentrated liquidity introduces interaction terms between diffusion and jump channels that violate additivity.

4. **Cross-asset validation**: Apply the framework to BTC/USDT and other major crypto pairs with different jump characteristics. Failure: if the optimal block time varies substantially across assets on the same chain, the chain-level invariance claim breaks down.

5. **Fee tier sensitivity**: Test across Uniswap fee tiers (0.01%, 0.05%, 0.3%, 1%) to verify the U-shaped ∂∆t_opt/∂γ relationship. Failure: if the optimal block time does not exhibit the predicted U-shape, the fee-LVR interaction model is incorrect.

6. **Out-of-sample holdout**: Hold out the most recent 6 months and re-estimate; compare predicted vs. realized LVR rates. Research-defined falsification threshold: if out-of-sample LVR deviation exceeds 20% of the in-sample estimate, the model requires recalibration.

## Crypto portability

**Direct**. The paper is explicitly developed for crypto AMMs (Uniswap CPMM, Ethereum, Solana) and calibrated to ETH/USDT on Binance/Uniswap. The entire analysis operates in the crypto-native context of on-chain AMMs.

Crypto-specific considerations:
- **Spot vs. perpetual**: The analysis is for spot AMM pools; perpetual swap funding rates are a separate cost channel not addressed.
- **24/7 session structure**: The model assumes continuous price observation; 24/7 trading is natural for on-chain AMMs.
- **Venue fragmentation**: The analysis assumes a single external reference price; in practice, fragmented venue prices could affect jump detection.
- **Liquidity**: The CPMM analysis assumes full-range liquidity; concentrated liquidity within active tick ranges may have different LVR dynamics.
- **On-chain constraints**: Block time, gas costs, and MEV are protocol-level design choices; the paper provides a framework for evaluating one dimension (LP-side LVR) of this multi-dimensional design space.
- **Timestamp/candle boundaries**: Jump detection relies on 5-minute candle data; higher-frequency data might reveal different jump dynamics.

## Limitations

- **CPMM only**: The full analysis is for constant-product market makers; concentrated liquidity (CLMM/Uniswap V3) and other CFMM designs require separate treatment, though the LVR construct is stated to apply within active tick ranges.
- **Single asset calibration**: Results are calibrated to ETH/USDT only; generalizability to other crypto pairs requires re-estimation of (σ, λ, δ).
- **Regime dependence**: Jump parameters are estimated over a specific historical period; they may not be stable forward-looking, especially across different market regimes (bull/bear/crisis).
- **LVR-only objective**: The planner's optimum considers only LP-side LVR and consensus cost; a full social-welfare treatment including MEV, finality, oracle freshness, and decentralization could yield different optima.
- **Not independently reproduced**: All results are theoretical; no empirical validation of the decomposition against realized LVR is provided in the paper.
- **Continuous price observation assumed**: The model assumes the arbitrageur can observe the external reference price continuously between blocks; in practice, oracle latency and data availability may differ.
- **No LP hedging**: The analysis assumes LPs do not hedge their adverse-selection exposure; hedging strategies could alter the effective LVR.
- **Symmetry assumption**: The exact floor result (Theorem 3) requires symmetric jump distributions; asymmetric jumps (m ≠ 0) weaken the bound (Proposition 1 covers the general case).
- **data gap**: The paper does not provide the raw Binance data or the exact jump-detection output; replication requires independent data acquisition and processing.

## Implementation status

Not implemented. No implementation in our research stack (NautilusTrader, PyBroker, or any other system) has been completed. The paper provides closed-form results and numerical illustrations; no trading strategy or LP management system is proposed or implemented.

## Adoption boundary

This record is research material only. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The paper's insights about jump-LVR floors and optimal block time are relevant for protocol design and LP strategy evaluation, but they do not constitute a tradeable alpha signal. The actionable implication for our research is that AMM LP strategies cannot fully eliminate adverse selection through block-time optimization alone; fee tier design and jump-aware LP management are the relevant levers.

## Related Wiki records

- `[[quant/ml-optimized-tau-reset-clmm-liquidity-provision-2026-09-06]]` — Different mechanism (CLMM tau-reset optimization vs. CPMM block-time LVR decomposition), but both address AMM LP loss.
- `[[quant/crypto-clmm-path-dependent-liquidity-provision-win-score-early-exit-2026-09-02]]` — CLMM-specific LP management; this record addresses the CPMM block-time dimension.
- `[[quant/defi-prediction-market-uniform-loss-amm-lvr-dynamic-liquidity-2026-09-02]]` — Prediction market AMM; different market type but shares the LVR adverse-selection framing.
- `[[quant/strategy-research-record-spec-v1]]` — Canonical specification.

## Sources

1. Nils Bundi, "Optimal Block Time for AMM Liquidity Providers under Jump-Diffusion Prices", arXiv:2608.30321v1 [q-fin.MF], August 31, 2026. https://arxiv.org/abs/2608.30321. Extended version accepted at MARBLE 2026; to be published by Springer Nature in Mathematical Research for Blockchain Economy (Lecture Notes in Operations Research).
