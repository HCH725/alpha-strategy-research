---
schema: strategy-research-record-v1
title: "Market Regime Council (MRC): Shapley Credit Assignment in Multi-Agent LLM Crypto Portfolio Management"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - LLM-multi-agent
  - Shapley-value
  - cooperative-game
  - portfolio-management
  - regime-adaptive
  - daily-rebalancing
status: research-only
confidence: medium
source_as_of: 2026-05-23
sources:
  - "Yunhua Pei, Zerui Ge, Jin Zheng, John Cartlidge, 'Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM Decision Systems', arXiv:2605.24490v1 [cs.AI / q-fin.PM], May 23, 2026. DOI: 10.48550/arXiv.2605.24490. https://arxiv.org/abs/2605.24490"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Market Regime Council (MRC): Shapley Credit Assignment in Multi-Agent LLM Crypto Portfolio Management

## Provenance

- **Primary source**: arXiv:2605.24490v1, submitted May 23, 2026
- **Authors**: Yunhua Pei (University of Bristol), Zerui Ge (Independent), Jin Zheng (University of Bristol), John Cartlidge (University of Bristol)
- **URL**: https://arxiv.org/abs/2605.24490
- **Code/demo**: Included in supplementary material (stated in paper; exact repo URL not provided in the preprint)
- **Sample period**: 2023-03-01 to 2025-12-31 (1,037 daily decision periods)
- **Universe**: 13 crypto assets (top L1 blockchain native tokens by market cap as of evaluation period)
- **Seeds**: 5 independent seeds reported as mean ± std

## Economic mechanism

### Source-reported

The authors frame multi-agent portfolio management as an online cooperative game among N=3 specialist LLM agents covering orthogonal information channels: price/technical (A1), on-chain network activity (A2), and macro/sentiment (A3). The system computes exact Shapley values across all 2^N - 1 = 7 coalition outputs (individual + pairwise + grand coalition) to determine agent weights. A Bayesian adaptive mixture stabilizes early-period (cold-start) estimates, regime-dependent multipliers adjust agent authority across bull/volatile/bear conditions, and a five-layer causal trace renders each rebalance auditable.

### Research interpretation

**Hypothesis**: Shapley-based credit assignment provides a principled, axiomatic mechanism for dynamically weighting heterogeneous information channels (price/technical, on-chain, macro) in a cooperative game framework, enabling regime-adaptive multi-agent portfolio construction that outperforms fixed-rule, heuristic, or single-agent approaches.

**Mechanism**: The Shapley value decomposes a portfolio's risk-adjusted return into marginal contributions from each agent and each coalition. When regime conditions shift, the Bayesian mixture transitions from uniform prior (cold-start) to Shapley-derived weights, while regime multipliers amplify agents whose information channels are most relevant in the current regime. This avoids the pitfalls of fixed heuristic weighting or naive online adaptation.

**Components**:
- Regime detector: momentum-to-volatility ratio ξ(t) = tanh(r_30d / σ_30d)
- Exponentially Weighted Protector (EWP): geometric decay with h=252 for cold-start mitigation
- Bayesian adaptive update: α(t) = 1 - exp(-t/λ) with λ=30, transitioning from uniform to Shapley-derived weights
- Selective Winner-Takes-All: dominant agent override when rolling Sharpe exceeds others by factor θ_WTA
- Regime-aware multiplier: agent-specific scalars interpolated across regime conditions
- Risk control overlays: momentum tilt, BTC dominance signal, drawdown protection

## Signal

- **Formation timestamp**: Daily, end-of-day decision period; rebalanced once per trading day
- **Lookback**: 30-day rolling window for regime detection; exponentially weighted historical performance (h=252 days) for Shapley credit computation; Bayesian warm-up over ~110 trading days
- **Entry/exit**: Portfolio weight vector w(t) ∈ W with per-asset concentration limits and bounded cash position; rebalanced daily via council output
- **Holding period**: Daily rebalancing; no explicit holding period constraint
- **Parameters**: λ=30 (Bayesian concentration), h=252 (EWP decay), regime thresholds ξ+ and ξ- (values in Appendix D, not fully specified in main text), θ_WTA (dominance threshold), γ_ρ and γ_μ (Sharpe/mean blend weights in characteristic function)
- **Position sizing**: Long-only with per-asset concentration limits (w_max) and cash bounds (c_max); values in Appendix D

**Underspecified**: Exact values for regime thresholds, w_max, c_max, θ_WTA, γ_ρ/γ_μ are in Appendix D (not fully reproduced in main text). The regime multiplier values per agent per regime are also in Appendix D.

## Required data

- **Universe**: 13 crypto assets (specific list not provided in main text; top L1 blockchain native tokens by market cap)
- **Venue**: Not explicitly stated; dataset described as "multi-modal web3 dataset"
- **Market type**: Spot (portfolio management, no leverage mentioned)
- **Timeframe**: Daily decision period
- **Fields**: Price/technical indicators (candlestick images), on-chain network activity data, macroeconomic/sentiment indicators
- **Data modalities**: Six modality groups across three agent-specific feature bundles (full inventory in Appendix D, Table 4)
- **Timestamp**: Daily; timezone not specified
- **Point-in-time**: Dataset covers 2023-03-01 to 2025-12-31

## Execution assumptions

- **Signal-to-order timing**: End-of-day decision, rebalanced once per trading period
- **Fill model**: Not specified; portfolio weights projected onto constraint set W
- **Transaction costs**: 0 bps in main results; sensitivity analysis at 5 and 10 bps one-way per unit of turnover (Table 8 in Appendix H)
- **Slippage**: Not modeled; no slippage assumption stated
- **Leverage**: Not used; long-only constraint
- **Market/limit order**: Not specified
- **Capacity**: Not assessed; 13-asset universe with daily rebalancing
- **Latency**: LLM inference time reported: 25-458 seconds per full MRC cycle depending on backbone model

## Evidence

### Source-reported

- **Cumulative return**: 440.1% ± 51.4% (5 seeds) over 1,037 trading days
- **Sharpe ratio**: 1.51 ± 0.07 (5 seeds)
- **Maximum drawdown**: 34.1% ± 2.5%
- **Information ratio vs. equal-weight**: 0.47 ± 0.20
- **Benchmark comparisons**: Outperforms BTC buy-and-hold (CR 270.94%, SR 1.23, MDD 32.02%), equal-weight (CR 279.93%, SR 1.14, MDD 42.78%), and all 13 active baselines (LLM and DRL)
- **Transaction cost sensitivity**: At 5 and 10 bps, MRC still exceeds BTC buy-and-hold in cumulative return
- **Regime decomposition**: Positive annualized Sharpe across all three market conditions (bull, volatile, bear); advantage most pronounced in bull, most compressed in bear
- **Ablation**: Gains come from Shapley-weighted integration across coalition outputs rather than any single stage in isolation; debate (Stage 2) consistently reduces Sharpe relative to best individual specialist

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Debate (Stage 2 Socratic cross-examination) consistently reduces Sharpe ratio relative to the best individual specialist. The authors attribute this to the fact that in portfolio construction, divergent views across different data modalities are epistemically valid rather than correctable errors.
- MRC's bear-regime advantage over passive BTC is compressed due to BTC's flight-to-quality role; cash buffer (mean 28% in bear) absorbs downside but caps participation if BTC rallies sharply.
- Multiple backbone models tested show varying parse failure rates (0.19% to 4.53%) and inference times, suggesting deployment depends on model reliability.
- High seed variance in some baselines (e.g., FinMem CR std ±107.6) suggests instability; MRC shows tighter SR variance (±0.07).

## Falsification plan

- **Out-of-sample**: The paper uses a single 1,037-day window without walk-forward or cross-validation; test across additional time periods and market regimes
- **Cost sensitivity**: Test at realistic CEX taker fees (5-20 bps) and spread assumptions; the paper tests 0/5/10 bps but not higher
- **Universe sensitivity**: Test with different asset selections and universe sizes
- **Backbone robustness**: Verify performance holds across different LLM backbones (paper tests Qwen3-VL variants but not GPT-4o or Claude)
- **Ablation of regime detection**: Remove regime-dependent multipliers and test whether Shapley alone is sufficient
- **Parameter perturbation**: Vary λ (Bayesian concentration), h (EWP decay), regime thresholds
- **Capacity/liquidity**: Assess impact of position sizes on execution in less liquid crypto assets
- **Failure threshold**: If MRC fails to beat equal-weight on Sharpe ratio after transaction costs in a walk-forward setting, the hypothesis is weakened

## Crypto portability

**Direct**: The strategy is natively designed and evaluated for crypto markets (13 crypto assets, daily rebalancing, 24/7 regime).

Crypto-specific considerations:
- **24/7 session**: Daily decision periods aligned with crypto's continuous trading; no weekend gap effects
- **Venue fragmentation**: Not addressed; assumes single unified price source
- **Liquidity**: 13 top L1 tokens likely have sufficient daily liquidity for the reported position sizes
- **On-chain data**: A2 (on-chain network activity agent) is a core component; requires reliable on-chain data feeds
- **No leverage**: Long-only constraint simplifies crypto-specific risks (no liquidation, no funding costs)

## Limitations

- **Single sample period**: 1,037 days (2023-03-01 to 2025-12-31) without walk-forward validation or out-of-sample holdout
- **No live/paper trading**: All results are backtest-only
- **0 bps transaction cost**: Main results assume zero costs; realistic costs (5-20 bps taker) may erode performance, especially for high-turnover baselines
- **LLM inference cost**: Full MRC cycle takes 25-458 seconds depending on backbone, which is impractical for intraday or higher-frequency trading
- **Universe unspecified**: Exact 13-asset list not provided in main text
- **Parameter opacity**: Key parameter values (regime thresholds, concentration limits, blend weights) are in Appendix D, not fully reproduced
- **Backbone dependency**: Performance may depend on specific LLM capabilities; code and demo data included but exact repo not provided in preprint
- **No turnover analysis**: Turnover not reported; cost sensitivity assumes fixed 5/10 bps per unit but actual turnover unknown
- **Publication status**: Preprint, not peer-reviewed
- **data gap**: Exact asset list, regime threshold values, and full parameter specifications are in Appendix D which was not fully accessible in the extracted text

## Implementation status

Not implemented. No code execution or validation has been performed. The paper includes code and demo data in supplementary material but exact repository URL was not provided in the preprint.

## Adoption boundary

This record represents normalized research material only. It does not mean:
- The strategy is profitable in live or paper trading
- The Shapley credit assignment mechanism has been validated independently
- The results are robust to realistic transaction costs and slippage
- The strategy has been approved for implementation, paper trading, testnet, or live trading

## Related Wiki records

- [[quant/llm-multi-agent-multi-modal-crypto-portfolio-hierarchical-skill-rebalancing-2026-09-02]] (Luo et al. 2025/2026, arXiv:2501.00826) — different mechanism: hierarchical skill-augmented coordination vs. Shapley credit assignment
- [[quant/multimarket-senseai-multi-agent-llm-regime-adaptive-equity-selection-2026-09-04]] — related multi-agent LLM regime-adaptive approach in equities
- [[quant/tradingmoe-query-key-sparse-expert-routing-llm-trading-2026-09-03]] — related LLM-based multi-agent trading framework

## Sources

1. Yunhua Pei, Zerui Ge, Jin Zheng, John Cartlidge. "Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM Decision Systems." arXiv:2605.24490v1 [cs.AI / q-fin.PM], May 23, 2026. DOI: 10.48550/arXiv.2605.24490. https://arxiv.org/abs/2605.24490
