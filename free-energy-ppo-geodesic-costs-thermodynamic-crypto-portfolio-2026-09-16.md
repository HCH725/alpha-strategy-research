---
schema: strategy-research-record-v1
title: Free-Energy PPO with Geodesic Transaction Costs for Cryptocurrency Portfolio Management
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - portfolio-management
  - reinforcement-learning
  - thermodynamic
  - regime-switching
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - "https://doi.org/10.20944/preprints202603.1644.v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Free-Energy PPO with Geodesic Transaction Costs for Cryptocurrency Portfolio Management

## Provenance

- **Source URL:** https://doi.org/10.20944/preprints202603.1644.v1
- **Full text:** https://www.preprints.org/manuscript/202603.1644/v1
- **Author:** Ntebogang Dinah Moroke
- **Title:** Deep Reinforcement Learning for Cryptocurrency Portfolio Management: A Free-Energy PPO Framework with Geodesic Transaction Costs and Thermodynamic Efficiency Bounds
- **Status:** Preprint (not peer-reviewed)
- **Submitted:** 2026-03-19; Posted: 2026-03-20
- **DOI:** 10.20944/preprints202603.1644.v1
- **Part of:** WOW-E-W quadrilogy (Paper 3 of 4)
- **Sample period (evaluation):** January 2022 to March 2026
- **Full sample (training + evaluation):** January 2017 to March 2026

## Economic mechanism

### Source-reported

The paper argues that all prior portfolio RL implementations treat transaction costs as a fixed proportional fee, ignoring that execution costs vary with the market's distributional state. The central claim is that the execution cost of a portfolio rebalancing is the geodesic distance between pre- and post-trade distributional states on the Fisher information manifold of a Markov-switching GARCH (MS-GARCH) volatility model. When the manifold is flat (GARCH parameter space has zero curvature), this reduces to the Euclidean norm (flat proportional fee); when curved (during high-volatility, fragmented-liquidity regimes), geodesic slippage exceeds the flat-fee approximation by an economically significant margin.

The framework derives a thermodynamic Carnot bound on portfolio efficiency (η ≤ 1 − H_turb / H_calm), where H_turb and H_calm are the maximum-entropy values of the turbulent and calm regime distributions. This establishes that active management has a fundamental thermodynamic efficiency limit determined by the entropy differential between regimes. Assets with large entropy gaps (e.g., ETH) have more "headroom" for active management; assets near boiling-point (BTC, where both regimes are near maximum entropy) have an efficiency bound approaching zero.

The agent uses a topological circuit breaker that activates when three simultaneous failures occur: GRU viscosity blackout (high-resistance state), negative Ricci scalar (Fisher manifold diverging / liquidity fragmentation), and Betti-0 exceedance (order book has fragmented into disconnected islands). The joint condition requires all three simultaneous failures, producing a lower false-positive rate than any individual criterion.

### Research interpretation

This is a regime-conditioned, cost-aware portfolio RL approach with two core innovations:

1. **State-dependent transaction costs:** Replace flat proportional fees with geodesic slippage on the Fisher information manifold of a calibrated volatility model. The economic mechanism is that rebalancing during periods of high curvature (fragmented liquidity, regime transitions) incurs higher true execution costs than during calm, stable regimes. This is falsifiable: if geodesic slippage does not predict actual fill quality better than a flat fee, the cost model provides no advantage.

2. **Thermodynamic efficiency bound:** The Carnot bound provides a falsifiable upper limit on achievable Sharpe per unit of Wasserstein dissipation. If realized efficiency consistently exceeds the bound, the bound is invalid; if the Spearman ordering of realized efficiency across assets does not match the predicted ordering from regime entropy values, the thermodynamic interpretation fails.

The regime-switching component uses a maximum-entropy Markov-switching GARCH model (MS-GARCH-MaxEnt) with Hamilton filter regime inference. The 11-dimensional observation vector combines regime probabilities and parameters from Paper 1 of the quadrilogy, GRU viscosity-filtered velocity and gate states from Paper 2, and Riemannian geometry features (Fisher curvature, Ricci scalar, Betti numbers, Wasserstein dissipation, topological alarm) from Paper 2.5.

## Signal

- **Formation timestamp:** End-of-day (daily rebalancing). The paper uses daily bars; the signal is formed after the close and executed at the next open (research-proposed timing).
- **Lookback window:** Expanding-window maximum likelihood for MS-GARCH-MaxEnt parameter estimation; 60-day rolling window for Fisher information matrix estimation via score-gradient outer product. GRU viscosity filter uses a sequence lookback (length not specified in the extracted text).
- **Entry / exit:** The PPO agent outputs a discrete action ∈ {short, neutral, long} for each of five assets (BTC, ETH, XRP, LTC, BCH), with equal weighting across assets. A topological circuit breaker constrains the agent to neutral when the joint fragmentation condition fires. Position sizing is discrete and equal-weight (not continuous); this is a limitation acknowledged by the author.
- **Holding period:** Daily rebalancing cadence.
- **Parameters:** The PPO uses two hidden layers of 128 units each with ReLU activation (separate actor and critic networks). Entropy bonus coefficient annealed linearly from 0.01 to 0.001 over training episodes. KL divergence early-stopping at 1.5× threshold. GAE for advantage estimation. 10 PPO epochs per update. Circuit breaker thresholds set at 90th percentile of GRU update gate and Betti-0 count during turbulent-regime periods (research-proposed thresholds for circuit breaker; the 0.5 Hamilton filter threshold is standard).
- **Position sizing:** Equal-weight across all five assets; discrete long/neutral/short (not continuous allocation). This is a significant simplification acknowledged in the limitations.
- **Signal is partially underspecified:** The exact MS-GARCH-MaxEnt training protocol, GRU architecture details, and Fisher information computation are deferred to Papers 1, 2, and 2.5 of the quadrilogy. Full reconstruction of the 11-dimensional observation vector requires reading all four papers.

## Required data

- **Instruments:** BTC, ETH, XRP, LTC, BCH (five cryptocurrency assets)
- **Venue:** Not specified (likely spot markets from a major exchange; the paper references Binance fee tiers in context of the quarter-hour effect paper but does not specify the exact data source for this study)
- **Market type:** Cryptocurrency spot (daily rebalancing)
- **Timeframe:** Daily bars
- **Fields:** OHLCV; Level-2 order book data (for Betti number computation via Vietoris-Rips persistent homology); regime probabilities and parameters from upstream MS-GARCH-MaxEnt model
- **Point-in-time:** Expanding-window maximum likelihood; data through March 2026
- **Timestamp:** Daily resolution; timezone not specified
- **Missing data:** Not explicitly addressed

## Execution assumptions

- **Signal-to-order timing:** End-of-day signal, next-day execution (research-proposed; not explicitly specified)
- **Order type:** Market order (research-proposed; the paper does not specify limit orders or queue position)
- **Fill model:** Assumed instant fill at close/open price (research-proposed)
- **Fees:** The framework models fees via geodesic slippage S* on the Fisher information manifold. The flat-fee baseline uses a constant 0.2% fee. The geodesic model derives state-dependent costs from the MS-GARCH parameter path curvature (source-reported)
- **Slippage:** Geodesic slippage S* replaces the flat proportional fee assumption. This is the Riemannian arc length on the Fisher information manifold, computed from score-gradient outer products over a 60-day rolling window (source-reported)
- **Impact / capacity:** Not modeled (the paper acknowledges market impact is non-linear and left for future work)
- **Leverage / margin:** Not specified (research-proposed neutral)
- **Latency:** Not modeled (daily rebalancing frequency)
- **Liquidation:** Not applicable for spot (the framework does not model perpetual futures or margin)

## Evidence

### Source-reported

All results from Table 3, evaluation window January 2022 to March 2026:

- **Sharpe ratio:** Geometric-cost PPO achieves highest Sharpe for all five assets. Bootstrap test rejects equal Sharpe between geometric-cost and flat-fee PPO at p < 0.05 for ETH, LTC, XRP, and BCH. Bitcoin does not meet the threshold (consistent with the near-zero Carnot bound).
- **Carnot efficiency ordering:** ETH > LTC > XRP > BCH > BTC. Spearman ρ = 0.94 (p = 0.017, n = 5) between realized η and turbulent half-life τ_1/2 from Paper 1.
- **Turnover reduction:** 78% (BTC) to 83% (ETH) relative to Greedy Signal; 56% (BTC) to 62% (ETH) relative to flat-fee PPO. Wilcoxon signed-rank p < 0.001 for all five assets.
- **Thermodynamic friction points (c*):** ETH ~1.8% [95% CI: 1.6, 2.1]; LTC ~1.4% [1.2, 1.6]; XRP ~1.2% [1.0, 1.4]; BCH ~1.0% [0.8, 1.2]; BTC ~0.6% [0.5, 0.8]. Kruskal-Wallis H = 9.21, p < 0.001.
- **Circuit breaker MDD reduction:** 28% to 38% Maximum Drawdown reduction (bootstrap tested).
- **Ablation:** Every component of the 11-dimensional observation vector contributes a statistically significant performance gain (Diebold-Mariano p < 0.05 for at least 4 of 5 assets per component). Fisher metric and turbulent-regime probability contribute the largest individual improvements.
- **Efficiency bounds:** Realized efficiencies range from 31% (BTC) to 74% (ETH) of their respective Carnot bounds.

Note: The paper reports bootstrap CIs but does not report exact Sharpe ratio point values in the extracted text (the exact numbers appear in Table 3 which was not fully extracted). The bootstrap test p-values are reported for each asset. This is a data gap for precise Sharpe values.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Bitcoin's geometric-cost PPO does not significantly outperform flat-fee PPO (p-value does not meet threshold), consistent with the thermodynamic prediction that BTC's near-zero entropy gap makes the geometric cost advantage minimal.
- The paper acknowledges that in prolonged low-volatility periods, Carnot efficiency decreases as regime differences compress, and performance would be expected to be lower.
- The paper is a preprint (not peer-reviewed). The WOW-E-W quadrilogy is self-referential (the four papers cite each other extensively), which raises concerns about independent validation.

## Falsification plan

1. **Carnot bound validity:** If the Spearman correlation between realized η and turbulent half-life τ_1/2 is not significant across a larger sample of assets, the thermodynamic interpretation fails. **Threshold (research-defined):** Spearman ρ < 0.50 across ≥ 20 assets. **Action:** Abandon thermodynamic framing.
2. **Geodesic vs. flat-fee superiority:** If geometric-cost PPO does not significantly outperform flat-fee PPO on Sharpe across the majority of assets in an expanded sample, the geodesic cost model provides no incremental value. **Threshold (research-defined):** Win rate < 60% of assets. **Action:** Revert to flat-fee model.
3. **Turnover reduction persistence:** If the 56–83% turnover reduction does not hold in forward-looking deployment (paper trading or live), the cost model may be overfit to the training data geometry. **Action:** Run 90-day paper trading with real order book data and compare turnover.
4. **Circuit breaker false-positive rate:** If the joint topological circuit breaker triggers too frequently in calm markets (false positive rate > 10% of trading days), it will erode returns by forcing unnecessary neutral positions. **Action:** Adjust thresholds or relax the triple-failure condition.
5. **Out-of-sample decay:** Re-run the full pipeline on a held-out period (e.g., April 2026 – September 2026) with no retraining. **Threshold (research-defined):** Sharpe ratio degradation > 50% vs. in-sample.

## Crypto portability

- **Direct:** The paper is designed for and tested on cryptocurrency spot markets (BTC, ETH, XRP, LTC, BCH). It is directly applicable to crypto spot.
- **Perpetual adaptation:** The framework currently models spot only. Porting to perpetual futures would require adding funding rate costs, mark/index price divergence, and liquidation risk to the reward function. The geodesic cost model would need recalibration for perp-specific execution characteristics.
- **Crypto-specific risks:** Venue fragmentation (Level-2 order book data is venue-specific); 24/7 markets (daily bar aggregation convention needs definition); exchange-specific fee structures (the friction point analysis is fee-level-dependent); survivorship and delisting of smaller assets.

## Limitations

- **Preprint (not peer-reviewed):** The paper is posted on Preprints.org and has not undergone peer review. The WOW-E-W quadrilogy is self-referential with extensive cross-citation among the four papers.
- **Small universe:** Only five cryptocurrency assets are evaluated. Generalizability to the broader crypto market (hundreds of liquid perpetuals and spot pairs) is untested.
- **Daily rebalancing only:** Intraday extension is deferred. The smooth manifold assumption underlying the geodesic formula may fail during flash crashes at higher frequencies.
- **Discrete position sizing:** The agent outputs long/neutral/short with equal weighting, not continuous allocation. This is a significant simplification that may leave alpha on the table.
- **No Level-3 / impact modeling:** Market impact is assumed linear in rebalanced fraction; real impact is non-linear, especially for larger trades relative to ADV.
- **Parameter uncertainty not modeled:** The MS-GARCH-MaxEnt parameter path is assumed observed without error. Sampling variance propagates into Fisher metric and geodesic slippage but is not integrated over.
- **Training data overlap with evaluation:** The evaluation window (January 2022 – March 2026) overlaps with the later portion of the full sample (January 2017 – March 2026). The paper does not clearly state whether the evaluation window is fully held-out or whether any training data bleeds into it. This is a potential leakage concern.
- **Exact Sharpe values not reported in extracted text:** Table 3 contains the exact Sharpe point estimates, but they were not fully captured in the extraction. The bootstrap p-values and CIs are reported.
- **Not independently reproduced.**
- **Data gap:** Exact data source (exchange, tick vs. bar, timezone) not specified in the extracted text.

## Implementation status

Not implemented. This is a research capture only. No code repository was identified. The author references a separate pipeline (Papers 1, 2, 2.5) that must be implemented to reproduce the full framework. The PPO training protocol is specified in Algorithm 1 but depends on the upstream components from the other three papers.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

The preprint status and self-referential quadrilogy structure require independent validation before any operational consideration.

## Related Wiki records

- [[crypto-quarter-hour-algorithmic-order-flow-predictability-2026-09-14]] (related: regime-aware execution cost modeling in crypto)
- [[crypto-perpetual-alpha-four-cell-regime-falsification-2026-09-13]] (related: regime classification in crypto markets)
- [[alphazerobeta-recurrent-ppo-market-neutral-portfolio-2026-09-02]] (related: PPO-based portfolio RL with different reward formulation)

## Sources

- Moroke, N.D. (2026). Deep Reinforcement Learning for Cryptocurrency Portfolio Management: A Free-Energy PPO Framework with Geodesic Transaction Costs and Thermodynamic Efficiency Bounds. *Preprints.org*, 202603.1644.v1. DOI: 10.20944/preprints202603.1644.v1. URL: https://doi.org/10.20944/preprints202603.1644.v1
