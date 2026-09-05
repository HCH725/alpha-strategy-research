---
schema: strategy-research-record-v1
title: "FinPILOT: Inference-Time MPC Plugin for RL Portfolio Management with XGBoost Price Forecasting"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - model-predictive-control
  - portfolio-management
  - inference-time-optimization
  - xgboost
  - plugin-architecture
status: research-only
confidence: medium
source_as_of: 2026-05-12
sources:
  - "Eun Go, Rohan Deb, Arindam Banerjee, 'Plan Before You Trade: Inference-Time Optimization for RL Trading Agents', arXiv:2605.12653v1 [cs.LG], May 12 2026. https://arxiv.org/abs/2605.12653"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FinPILOT: Inference-Time MPC Plugin for RL Portfolio Management

## Provenance

- **Primary Source:** Eun Go, Rohan Deb, Arindam Banerjee, "Plan Before You Trade: Inference-Time Optimization for RL Trading Agents", arXiv preprint `arXiv:2605.12653v1 [cs.LG]`, submitted May 12, 2026. DOI: `10.48550/arXiv.2605.12653`. Stable URL: `https://arxiv.org/abs/2605.12653`. PDF: `https://arxiv.org/pdf/2605.12653`.
- **Authors:** Eun Go (Siebel School of Computing and Data Science, University of Illinois Urbana-Champaign), Rohan Deb (Siebel School of Computing and Data Science, University of Illinois Urbana-Champaign), Arindam Banerjee (Siebel School of Computing and Data Science, University of Illinois Urbana-Champaign).
- **Publication Status:** Preprint (arXiv), May 2026. Not peer-reviewed at time of recording.
- **Code:** TradeMaster benchmark platform used; paper does not appear to release custom FinPILOT code separately.

## Economic mechanism

### Source-reported

The authors argue that RL trading agents are typically trained and deployed as static policies with no mechanism for using price forecasts at inference time. FinPILOT bridges the gap between supervised forecasting (which produces predictive signals but delegates decision-making to heuristics) and RL (which learns sequential policies but ignores forecasts at deployment). The key structural insight is that in portfolio management, the reward is closed-form: once prices are observed, portfolio return follows deterministically from allocations and price relatives. This eliminates the need for a learned reward model and reduces the "world model" to a price forecaster. At each decision step, the forecaster's predicted price trajectory is used to construct an imagined return objective, and the pre-trained policy is adapted via gradient ascent on this imagined objective before executing one step of the trade.

### Research interpretation

The mechanism is a **plugin inference-time Model Predictive Control (MPC)** framework for portfolio management. The hypothesized alpha channel is:

1. **Forecast-informed re-planning:** A separately trained price forecaster (XGBoost, R² ≈ 0.01) provides H-step price trajectories at each decision step.
2. **Imagined objective optimization:** The pre-trained RL actor is adapted by backpropagating through K noisy imagined rollouts, optimizing a risk-penalized imagined return (mean return minus downside semi-deviation).
3. **Closed-form reward exploitation:** Portfolio reward is deterministic given prices and allocations, so no learned reward model is needed — the forecaster's predicted price relatives directly compute imagined PnL.
4. **One-step execution:** After E gradient update epochs on the imagined objective, only the first resulting action is executed before re-planning (standard MPC receding horizon).

The framework is compatible with any pre-trained actor-critic RL agent (PPO, SAC, A2C, TD3, DDPG evaluated) and requires zero retraining.

## Signal

- **Formation timestamp:** Inference-time adaptation occurs at each daily trading step using the forecaster's H-step ahead price predictions.
- **Lookback:** Forecaster trained on historical data strictly preceding the test window. Per-asset XGBoost models trained on 11 temporal features (open/high/low/close/adjusted-close ratios and 6 moving-average ratios at horizons 5–30 days). H = 50 planning horizon.
- **Entry:** At each step t, observe state s_t, generate K noisy forecast trajectories via forecaster F, run E epochs of gradient ascent on the risk-penalized imagined objective J_t(θ) = mean_return - λ × downside_semi_deviation, then execute the adapted policy's allocation w_t = π_θ(s_t).
- **Exit:** Daily rebalancing. Transaction cost: 0.1% of rebalanced value proportional to weight turnover. Cash earns zero return.
- **Holding period:** Daily (single-day holding, rebalance every step).
- **Parameters:**
  - Planning horizon H = 50 days [source-reported, selected via horizon sensitivity analysis]
  - Risk-aversion coefficient λ ∈ {0.5, 2, 5, 10} [source-reported, grid-searched on validation]
  - Per-step learning rate η ∈ {10⁻², 10⁻³, 10⁻⁴} [source-reported]
  - Gradient update epochs E ∈ {1, 5, 10} [source-reported]
  - Discount γ = 0.99 [source-reported, fixed]
  - Noise particles K > 1 with Gaussian perturbation scaled by per-horizon prediction variance [source-reported]
  - Transaction cost c = 0.1% per rebalanced value [source-reported, TradeMaster convention]

## Required data

- **Instrument:** DJ30 constituents (29 Dow Jones 30 stocks) and 22 FX currency pairs.
- **Universe:** DJ30: 29 stocks from Dow Jones 30 index, 2012–2021 daily prices. FX: 22 currency pairs, 2009–2019 daily rates.
- **Venue:** TradeMaster benchmark platform. DJ30 sourced from Yahoo Finance.
- **Timeframe:** Daily bars.
- **Fields:** Open, high, low, close, adjusted-close prices; 11 derived temporal features per asset per day.
- **Point-in-time:** Standard train/validation/test splits (DJ30: train 2012–2019, val 2020, test 2021; FX: train 2009–2017, val 2018, test 2019). No look-ahead bias in feature construction.
- **Missing-data:** Not explicitly addressed; TradeMaster platform handles data quality.

## Execution assumptions

- **Signal-to-order timing:** Daily rebalancing at close.
- **Fill model:** Perfect fill assumption (TradeMaster benchmark convention).
- **Fees:** 0.1% transaction cost per rebalanced value, proportional to total weight turnover.
- **Slippage:** Not modeled; TradeMaster benchmark does not include slippage.
- **Impact:** Price-taker assumption; portfolio weights do not affect observed prices.
- **Leverage/margin:** Long-only, no shorting, no leverage. Softmax ensures weights sum to 1 and are non-negative.
- **Cash:** Cash earns zero return; acts as risk-free reserve.
- **Latency:** Not modeled; daily frequency assumed sufficient.
- **Capacity:** Not explicitly analyzed; DJ30 is a small-cap universe.
- **Execution model:** MPC adaptation at inference time requires gradient computation at each step; per-step compute cost not reported as a binding constraint.

## Evidence

### Source-reported

All figures below are from Go, Deb, and Banerjee (2026), arXiv:2605.12653v1, evaluated on TradeMaster DJ30 benchmark (test period: 2021). Initial portfolio: $100,000. Transaction cost: 0.1%.

**DJ30 main results (Table 1, noise + λ configuration, 5 seeds):**

| Algorithm | Total Return (%) | Sharpe | Calmar | Sortino | Max DD (%) |
|-----------|-----------------|--------|--------|---------|------------|
| PPO Baseline | 17.74 ± 0.22 | 1.49 ± 0.01 | 2.56 ± 0.02 | 2.13 ± 0.02 | 6.65 ± 0.05 |
| PPO + FinPILOT | 23.46 ± 0.82 | 1.75 ± 0.04 | 2.71 ± 0.32 | 2.80 ± 0.06 | 8.15 ± 0.63 |
| SAC Baseline | 17.78 ± 0.22 | 1.49 ± 0.02 | 2.57 ± 0.07 | 2.13 ± 0.03 | 6.62 ± 0.14 |
| SAC + FinPILOT | 22.21 ± 0.16 | 1.71 ± 0.01 | 2.92 ± 0.02 | 2.66 ± 0.02 | 7.13 ± 0.00 |
| A2C Baseline | 17.87 ± 0.00 | 1.49 ± 0.00 | 2.56 ± 0.01 | 2.13 ± 0.01 | 6.67 ± 0.01 |
| A2C + FinPILOT | 18.44 ± 0.00 | 1.52 ± 0.00 | 2.57 ± 0.01 | 2.22 ± 0.00 | 6.86 ± 0.00 |

**Key observations (source-reported):**
- Stochastic policies (PPO, SAC) benefit more than deterministic ones (TD3, DDPG).
- PPO shows the largest gain: total return 17.74% → 23.46%, Sharpe 1.49 → 1.75.
- Maximum drawdown increases modestly for PPO and SAC despite risk penalty.
- FX generalization: All FinPILOT hyperparameters transferred from DJ30 without retuning; PPO, SAC, A2C, DDPG all improve on FX (Table 3).

**Cheating experiments (Table 2):** Threshold-like behavior — gains nearly indistinguishable between R² = 0.001 and R² = 0.01, with continued improvement at higher R². At R² = 0.8, PPO achieves 123.89% total return and 5.50 Sharpe.

**XGBoost forecaster performance (Table 5):** Mean test R² ≈ 0.01 across price features at H = 50. This is described as "economically meaningful in daily equity markets."

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Maximum drawdown increases for PPO and SAC under FinPILOT relative to baselines (PPO: 6.65% → 8.15%; SAC: 6.62% → 7.13%), despite the downside risk penalty. The authors acknowledge this as a limitation.
- Deterministic policies (TD3, DDPG) show modest, sometimes insignificant improvements that fall within large baseline variance.
- Evaluation limited to two benchmarks (DJ30 and FX daily). No intraday, crypto, or multi-asset-class evaluation.
- Backtested performance does not account for market impact, slippage, latency, or regime shifts in live trading.
- The XGBoost forecaster's R² ≈ 0.01 is extremely low; the economic significance of this signal level in practice (vs. benchmark) is debatable.

## Falsification plan

1. **Out-of-sample validation:** Re-run on independent datasets (e.g., S&P 500, Russell 2000, international equities, crypto perpetuals) with hyperparameters fixed from DJ30/FX. If gains vanish, the framework overfits to benchmark-specific dynamics.
2. **Forecaster degradation test:** Replace XGBoost with a simpler forecaster (e.g., lagged return, random walk) to test whether the R² ≈ 0.01 threshold is genuinely sufficient or whether the benchmark's specific structure inflates gains.
3. **Transaction cost stress:** Increase fees from 0.1% to 0.3–0.5% per trade and add modeled slippage/spread. If gains disappear, the framework relies on unrealistically low friction.
4. **Regime breakdown:** Evaluate separately in bull, bear, and sideways subperiods. The single test year (2021) may not represent diverse regimes.
5. **Stochastic vs. deterministic ablation:** If the framework only works for stochastic policies (as observed), it may not generalize to production systems that prefer deterministic allocations for reproducibility.
6. **Capacity/impact analysis:** Scale portfolio size and test with realistic market-impact models. The price-taker assumption may fail at institutional scale.
7. **Failure threshold:** If Sharpe improvement over baseline is < 0.1 across > 3 independent datasets, the framework provides negligible economic value.
8. **Action on failure:** Retire the inference-time MPC approach for this paper's specific mechanism; investigate whether gains are driven by noise regularization rather than forecast quality.

## Crypto portability

**Adapted/unproven.** The mechanism is evaluated exclusively on U.S. equities (DJ30) and foreign exchange (FX). Portability to crypto markets requires adaptation:

- **Direct portability considerations:** Crypto perpetual futures allow symmetric long/short, enabling the framework to potentially exploit short-side allocations. Daily rebalancing is natural for crypto 24/7 markets.
- **Funding rate costs:** Crypto perpetuals have variable funding rates (sometimes > 0.1% per 8 hours) that are not modeled in the TradeMaster 0.1% flat fee. This could dominate or erase marginal gains.
- **Market impact:** Crypto markets (especially altcoins) have lower liquidity than DJ30 constituents; the price-taker assumption may fail.
- **24/7 timestamping:** Framework uses daily bars; adaptation to intraday crypto would require retraining the forecaster and re-tuning MPC parameters.
- **Volatility regime:** Crypto returns are far more volatile and heavy-tailed than DJ30; the downside risk penalty may need recalibration.
- **Venue fragmentation:** DJ30 is single-venue; crypto spans dozens of exchanges with varying liquidity, fees, and index/mark price conventions.

## Limitations

- **Benchmark-only evaluation:** Results limited to TradeMaster DJ30 and FX benchmarks. Real-world deployment on live markets, different asset classes, or different time periods is not demonstrated.
- **Low forecast quality:** XGBoost forecaster achieves R² ≈ 0.01, which the authors describe as "economically meaningful" but which is at the very low end of predictive signal quality. The practical significance in live trading (vs. benchmark) is uncertain.
- **Increased drawdown:** FinPILOT increases maximum drawdown for the best-performing stochastic policies (PPO, SAC), contradicting the risk-penalized objective's intent.
- **No market impact or slippage modeling:** TradeMaster benchmark omits these; real-world execution costs could erode gains.
- **Single test year:** DJ30 test period is only 2021; FX test is only 2019. Multi-year out-of-sample validation is absent.
- **Compute overhead:** Inference-time MPC requires E gradient update epochs at every trading step. While described as manageable, the per-step compute cost is not benchmarked against alternatives.
- **No code release:** The paper does not appear to release FinPILOT-specific code separately, limiting independent verification.
- **Threshold behavior unexplained:** The authors observe that gains are nearly identical at R² = 0.001 and R² = 0.01, but do not provide a theoretical explanation for this threshold.
- **Not independently reproduced.**

## Implementation status

`not-implemented` in our research stack. No PyBroker or Nautilus implementation exists. The TradeMaster benchmark code is available (Apache-2.0 license) but FinPILOT-specific code is not separately released.

## Adoption boundary

This record is research material only. It does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The framework is a meta-optimization method that enhances existing RL policies, not a standalone trading signal.

## Related Wiki records

- `[[quant/exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05]]` — RL-based pairs trading with optimal stopping; different mechanism but shares the RL-for-trading research domain.
- `[[quant/moira-language-driven-hierarchical-reinforcement-learning-pair-trading-2026-09-05]]` — Language-driven hierarchical RL for pair trading; different signal construction.
- `[[quant/decomposable-reward-forex-rl-mask-aware-doubledqn-2026-09-05]]` — Mask-aware DQN for forex; shares the FX evaluation domain.

## Sources

- Eun Go, Rohan Deb, Arindam Banerjee, "Plan Before You Trade: Inference-Time Optimization for RL Trading Agents", arXiv:2605.12653v1 [cs.LG], May 12 2026. DOI: 10.48550/arXiv.2605.12653. URL: https://arxiv.org/abs/2605.12653. PDF: https://arxiv.org/pdf/2605.12653.
- TradeMaster benchmark platform: Sun et al. (2023), "TradeMaster: A Holistic Quantitative Trading Platform Empowered by Reinforcement Learning", NeurIPS 2023. Apache-2.0 license.
