---
schema: strategy-research-record-v1
title: "Optimal Dynamic Fees for AMMs: Pro-Cyclical Volatility Feedback via Loss-Versus-Rebalancing Stochastic Control"
created: 2026-09-09
updated: 2026-09-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - automated-market-maker
  - constant-product
  - dynamic-fees
  - loss-versus-rebalancing
  - stochastic-control
  - liquidity-provision
status: research-only
confidence: high
source_as_of: 2026-06-19
sources:
  - "Farbod Ghasemlu, 'Optimal Dynamic Fees for Automated Market Makers: A Stochastic Control Approach to Loss-Versus-Rebalancing', arXiv:2606.21769v1 [q-fin.MF, q-fin.TR], June 19, 2026. DOI: 10.48550/arXiv.2606.21769. https://arxiv.org/abs/2606.21769"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Optimal Dynamic Fees for AMMs: Pro-Cyclical Volatility Feedback via Loss-Versus-Rebalancing Stochastic Control

## Provenance

- **Source:** Farbod Ghasemlu, "Optimal Dynamic Fees for Automated Market Makers: A Stochastic Control Approach to Loss-Versus-Rebalancing"
- **arXiv ID:** arXiv:2606.21769v1
- **Subjects:** q-fin.MF (Mathematical Finance), q-fin.TR (Trading and Market Microstructure)
- **Submitted:** June 19, 2026 (v1)
- **DOI:** 10.48550/arXiv.2606.21769
- **URL:** https://arxiv.org/abs/2606.21769
- **Pages:** 18 pages, 3 figures, 1 table
- **Code:** Not publicly released; code reproducing figures and tables available from the author on request.

## Economic mechanism

### Source-reported

The paper models the fee-setting problem of a liquidity provider (LP) in a constant-product AMM (e.g. Uniswap v3/v4 with programmable hooks) as a stochastic control problem. The LP's fee governs two opposing forces: (1) uninformed fee income from noise traders, which is hump-shaped in the fee; and (2) adverse selection losses from arbitrageurs, which decrease in the fee because a higher fee widens the no-arbitrage band. The paper builds on the loss-versus-rebalancing (LVR) framework of Milionis et al. (2022, 2024).

### Research interpretation

The core alpha mechanism is a **pro-cyclical dynamic fee rule** for AMM liquidity provision: the LP should raise the fee when realized volatility increases and lower it when volatility decreases. This is because higher volatility increases both the level of adverse selection and its sensitivity to the fee, making the marginal value of fee protection larger. The optimal fee is a deterministic function of instantaneous variance alone, independent of LP wealth and risk aversion. Under constant volatility, no dynamic adjustment is needed—the best static fee is optimal.

This is an **LP fee optimization strategy**, not a directional trading signal. The alpha accrues to LPs who dynamically adjust their pool fee to minimize adverse selection cost net of uninformed fee revenue, compared to LPs using a fixed fee.

## Signal

### Formation timestamp
Continuous-time model; fee is a function of the filtered instantaneous variance of the external reference price. In practice, the fee would be updated on-chain (e.g. per block or per swap via Uniswap v4 hooks).

### Lookback
The optimal fee f*(v) is a pointwise function of instantaneous variance v_t, not of past observations. In practice, a filtered/estimated variance would be used (e.g. exponential moving average of squared returns).

### Entry / fee rule
The growth-optimal fee solves the first-order condition (Eq. 15 in paper):

```
ν₀ · e^{-αf} · (1 - αf) = -∂_f A(f; v)
```

where:
- ν₀ = base uninformed turnover (calibrated: 8 per unit pool value per year)
- α = semielasticity of uninformed volume to the fee (calibrated: 400, so uninformed peak at 25 bps)
- A(f; v) = adverse selection rate from the LVR band mechanism (Eq. 6 in paper)
- v = instantaneous variance of the reference price

The optimal fee is strictly increasing in v (pro-cyclical, Proposition 3). At the calibrated parameters:
- f* = 26.7 bps at √v = 30% annualized
- f* = 35.5 bps at √v = 60% (long-run mean)
- f* = 47.4 bps at √v = 80%
- f* = f_max = 100 bps near √v = 100%

### Exit / fee adjustment
The fee is continuously adjusted to f*(v_t). Gas costs are handled via an impulse-control dead-band: the fee is reset only when |f_current - f*(v)| exceeds a threshold.

### Holding period
N/A (fee setting is a continuous process, not a position with a holding period).

### Parameters
- λ (block rate): 2.63 × 10⁶ yr⁻¹ (12-second slot, proof-of-stake chain) — research-proposed calibration
- κ (mean-reversion speed of variance): 3.0 — research-proposed calibration
- θ (long-run variance level): 0.36 (√θ = 60% annualized) — research-proposed calibration
- ξ (vol-of-var): 1.30 — research-proposed calibration
- ν₀ (base uninformed turnover): 8 — research-proposed calibration
- α (uninformed fee sensitivity): 400 — research-proposed calibration
- f_max (fee cap): 100 bps — research-proposed calibration

### Position sizing
Not applicable. The strategy is a fee-setting rule for a constant-product AMM position.

## Required data

- **Instrument:** Any crypto asset pair traded on a constant-product AMM (e.g. ETH/USDC on Uniswap).
- **Venue:** Uniswap v4 or compatible AMM with programmable hooks enabling dynamic fee adjustment.
- **Market type:** On-chain spot (constant-product AMM).
- **Timeframe:** Continuous-time model; practical implementation at block-level or swap-level granularity.
- **Fields:** External reference price of the risky asset (for variance estimation); on-chain pool state; uninformed volume estimates.
- **Timestamp:** Real-time; fee should respond to an external, manipulation-resistant volatility signal (not the pool's own price).
- **Missing-data:** Paper assumes continuous observation of instantaneous variance. In practice, variance must be estimated from realized returns, introducing estimation error — data gap.

## Execution assumptions

- **Signal-to-order timing:** The fee is set as a function of the current variance estimate; the fee update is an on-chain transaction.
- **Execution:** The fee applies to all subsequent swaps in the pool until the next update. No order placement decisions by the LP.
- **Fees:** The strategy is itself about fee optimization; the model accounts for the fee's effect on both uninformed revenue and adverse selection.
- **Slippage / spread:** Abstracted through the no-arbitrage band mechanism. The model assumes competitive arbitrageurs correct mispricing.
- **Impact:** Not directly modeled; the LP is a price-taker relative to arbitrageurs and uninformed flow.
- **Funding:** Not applicable (spot AMM, not perpetual).
- **Gas costs:** Handled via impulse-control dead-band. Calibration: for a $10M pool with $9 per update gas cost, a 2 bps dead-band reduces updates to ~95/year with minimal growth loss (~0.9 bps).
- **Capacity:** Paper does not analyze capacity constraints.
- **Fill model:** Not applicable (AMM, not order book).

## Evidence

### Source-reported

From the calibration and simulation study (Section 7, Table 1 of paper):

- Optimal dynamic fee excess growth rate: **37.1 bps/year** over the rebalancing benchmark.
- Best static fee (37 bps): **31.4 bps/year** excess growth. Paired gain of optimal over best static: **5.7 bps/year** (95% paired band [1.5, 25.7] bps).
- Static 30 bps fee: **28.8 bps/year**. Paired gain: **8.3 bps/year** ([0.6, 41.8] bps).
- Volatility-linked heuristic: **35.9 bps/year**. Paired gain: **1.2 bps/year** ([0.5, 5.3] bps).
- Static 55 bps fee: **−139.9 bps/year** (dominated by wide margin).
- At long-run volatility, the frictionless LVR rate is θ/8 = **4.5% per year**; the optimal fee eliminates **93.1%** of this.
- The optimal fee is **100% win rate** against each benchmark by construction (Theorem 1).
- Results evaluated on **6,000** simulated variance paths over **1.5 years** with common random numbers.
- Source reports the optimal fee is weakly dominates every alternative on **each individual path** (paired comparison).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The improvement over the best static fee is **modest in absolute terms** (5.7 bps/year in the calibrated setting), and the paper acknowledges this: "a well-chosen static fee already removes most adverse selection" (Section 7.3).
- The gain accrues mainly in the **tails of the volatility distribution**; at the center of the distribution, the static fee is nearly optimal.
- The model deliberately **abstracts from** inventory management, volatility-stimulation channels, and strategic arbitrageurs who anticipate the fee policy. Baggiani et al. (2025) show a richer model produces a two-regime fee alternating between deterring arbitrage and stimulating noise flow (Section 8).
- The model assumes the LP has a **single fee control** and does not consider range selection (concentrated liquidity) or liquidity depth decisions.
- The calibration uses **illustrative parameters**; the authors state "the qualitative conclusions depend only on the sign properties of Lemma 1 and on α > 0" but the quantitative magnitude of the dynamic gain is parameter-dependent.

## Falsification plan

1. **Out-of-sample simulation:** Re-run the calibration with different volatility parameters (smaller ξ, different θ, different κ) and verify that the dynamic gain remains positive but scales as predicted (wider dispersion → larger gain; narrower → smaller gain). **Failure metric:** Dynamic fee fails to dominate the best static fee on average across paths. **Action:** If dynamic fees do not add value, the strategy reduces to static fee optimization.
2. **Empirical estimation of α:** Estimate the semielasticity α of uninformed volume to the fee from historical AMM data. If α is very large (highly elastic demand), the dynamic gain narrows; if α ≈ 0 (inelastic), the gain widens. **Failure metric:** Estimated α > 1000 would render the dynamic adjustment marginal.
3. **Variance estimation error:** Test the strategy with estimated variance (e.g. exponential moving average of squared returns) rather than instantaneous variance. **Failure metric:** If estimation error causes the strategy to underperform the best static fee, the practical value is negated.
4. **Gas cost sensitivity:** Increase gas costs or decrease pool value and verify the dead-band still captures most of the dynamic gain. **Failure metric:** If gas costs exceed the dynamic gain for small pools, the strategy is only viable for large pools.
5. **Competition:** Introduce competing pools with different fee policies and verify the volatility-driven fee shape survives. **Failure metric:** If competitive pressure eliminates the fee-setting authority, the strategy is not implementable.
6. **Abstraction test:** Compare against the richer Baggiani et al. (2025) two-regime model. **Failure metric:** If the two-regime model materially outperforms the pointwise volatility feedback, the reduced-form model is incomplete.

## Crypto portability

**direct**

The paper is explicitly designed for constant-product AMMs in DeFi. The calibration targets major crypto pairs on proof-of-stake chains (12-second slots). The model directly applies to:
- Uniswap v4 with programmable hooks
- Any constant-product AMM allowing per-swap or per-block fee updates

Crypto-specific considerations:
- The fee should respond to an **external, manipulation-resistant volatility signal** to avoid feedback loops where an adversary manipulates the pool price to induce a favorable fee (Section 8).
- **Gas costs** are an on-chain friction that the paper explicitly addresses via dead-band impulse control.
- The model assumes the **external reference price** is observable and manipulation-resistant; in practice, this requires a TWAP oracle or external price feed.

## Limitations

- **Single-agent model:** The LP sets the fee unilaterally; strategic interactions with arbitrageurs and competing pools are abstracted (Baggiani et al. 2025 provide a more complete equilibrium treatment).
- **No concentrated liquidity:** The model applies to full-range constant-product positions. The concentrated-liquidity extension with range-dependent adverse selection is noted as future work (Section 8).
- **No liquidity depth decision:** The LP's deposit/withdrawal decision is held fixed; the paper does not model how the fee policy affects LP entry/exit.
- **Illustrative calibration:** Parameters are chosen for qualitative demonstration, not calibrated to a specific live pool. Quantitative results (5.7 bps/year dynamic gain) are parameter-dependent.
- **No empirical validation:** All results are from simulation, not live trading or historical replay on real AMM data.
- **Estimation error:** The model assumes instantaneous variance is observable; practical implementation requires filtered estimation, which introduces lag and error.
- **Data gap:** The paper does not provide empirical estimates of the uninformed flow parameters (ν₀, α) from real AMM data; these are calibrated illustratively.
- **No on-chain code:** The numerical experiments use simulated data; code is available only on request.

## Implementation status

Not implemented. The paper provides theoretical results and simulation-based calibration. No on-chain deployment or backtesting against real AMM data is reported.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- Profitable in live AMM liquidity provision
- Validated alpha
- Approved for implementation
- Approved for paper trading, testnet, or live deployment

The dynamic fee rule is a research-proposed optimization for AMM LPs. Its practical value depends on accurate variance estimation, appropriate parameter calibration, and the LP's ability to execute on-chain fee updates within gas constraints.

## Related Wiki records

- [[quant/defi-concentrated-liquidity-stochastic-impulse-control-tail-risk-2026-09-02]] — Related DeFi AMM optimal LP strategy (RL-based rebalancing for concentrated liquidity; different mechanism: rebalancing vs. fee-setting)
- [[quant/defi-concentrated-liquidity-amm-dynamic-fee-staleness-proxy-lvr-compensation-2026-09-02]] — Related dynamic fee strategy for AMMs (staleness-proxy-based, different signal construction: staleness proxy vs. variance feedback)
- [[quant/amm-lvr-jump-floor-optimal-block-time-2026-09-08]] — Related LVR framework (jump-diffusion optimal block-time, different mechanism: block timing vs. fee-setting)
- [[quant/strategy-research-record-spec-v1]] (schema specification)

## Sources

1. Farbod Ghasemlu, "Optimal Dynamic Fees for Automated Market Makers: A Stochastic Control Approach to Loss-Versus-Rebalancing," arXiv:2606.21769v1 [q-fin.MF, q-fin.TR], June 19, 2026.
   - URL: https://arxiv.org/abs/2606.21769
   - DOI: 10.48550/arXiv.2606.21769
2. Public full-text HTML for the same paper: https://arxiv.org/html/2606.21769
