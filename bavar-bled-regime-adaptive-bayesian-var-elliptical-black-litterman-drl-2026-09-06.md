---
schema: strategy-research-record-v1
title: "BAVAR-BLED: Bayesian VAR + Elliptical Black-Litterman Regime-Adaptive DRL Portfolio Optimization"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - regime-adaptive
  - fat-tail
  - bayesian
  - deep-reinforcement-learning
  - elliptical-distributions
status: research-only
confidence: medium
source_as_of: 2026-06-08
sources:
  - "Mikriukov, Sun, Stefanidis, Su, Jiang (2026). 'Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian VAR and Elliptical Black-Litterman.' arXiv:2606.09104v1 [cs.LG / q-fin.PM]. https://arxiv.org/abs/2606.09104"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BAVAR-BLED: Bayesian VAR + Elliptical Black-Litterman Regime-Adaptive DRL Portfolio Optimization

## Provenance

- **Primary Source:** Daniil Mikriukov, Ruoyu Sun, Angelos Stefanidis, Jionglong Su, and Zhengyong Jiang, *"Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian VAR and Elliptical Black-Litterman"*, arXiv preprint `arXiv:2606.09104v1 [cs.LG / q-fin.PM]`, submitted June 8, 2026.
- **DOI:** [10.48550/arXiv.2606.09104](https://doi.org/10.48550/arXiv.2606.09104)
- **Stable Abstract URL:** https://arxiv.org/abs/2606.09104
- **Full Text HTML:** https://arxiv.org/html/2606.09104v1
- **Status:** Under review. Extends prior work presented at ICIC 2025 (Mikriukov et al., 2025) on Black-Litterman under Elliptical Distributions (BLED).
- **Primary Source Verification:** Full HTML text retrieved and inspected. All performance claims, hyperparameters, ablation results, and experimental design details match the primary text.

## Economic mechanism

### Source-reported

The authors identify two fundamental limitations in existing DRL portfolio optimization frameworks: (1) most approaches assume normally distributed returns, ignoring the well-documented fat-tailed nature of financial returns, leading to tail-risk underestimation; (2) historical data is treated uniformly, without accounting for temporal importance, causing models to fail during regime changes when asset relationships evolve. BAVAR-BLED addresses both by integrating Bayesian-Averaging Vector Autoregressive (BAVAR) methods for adaptive regime-aware priors with the Black-Litterman under Elliptical Distributions (BLED) framework using Student's t-distributions for fat-tail modeling, all within a TD3 reinforcement learning architecture.

### Research interpretation

The hypothesized alpha mechanism is a **regime-adaptive Bayesian prior that implicitly tracks structural shifts** through an ensemble of heterogeneous VAR models with continuously updated posterior weights. Unlike explicit regime-switching models that require predefined regime counts, the BAVAR ensemble adapts through Bayesian model averaging — models with poor predictive power receive lower weights, while well-performing models dominate. This provides a continuous, non-parametric regime-tracking signal that feeds into Black-Litterman optimization with fat-tailed (Student's t) return assumptions. The combination creates a portfolio allocator that (a) re-weights toward assets with better risk-adjusted expected returns during regime transitions, and (b) appropriately discounts tail-risk scenarios that Gaussian models underestimate.

Component decomposition:
- **Regime tracking:** BAVAR ensemble of 600 VAR models with HAR (daily/weekly/monthly) features, Bayesian model averaging for adaptive regime detection
- **Fat-tail modeling:** Black-Litterman under Elliptical Distributions (Student's t) replacing Gaussian covariance with dispersion matrix
- **View generation:** Transformer encoder generating investor views on expected returns
- **Risk aversion:** CNN estimating state-dependent risk aversion parameter δ
- **Policy optimization:** TD3 reinforcement learning for portfolio weight refinement

## Signal

- **Formation timestamp:** Daily rebalancing at adjusted close prices.
- **Lookback window:** 15 trading days of historical data per asset (state tensor: 29 × 15 × 12).
- **Features:** Adjusted close price, trading volume, 5 EMAs (10/20/50/100/200), MACD + signal line, RSI, Bollinger Bands — 12 features per asset.
- **HAR features:** Multi-scale returns: daily (previous day), weekly (5-day average), monthly (22-day average) — used as VAR regressors.
- **Long entry:** BAVAR-BLED computes posterior expected returns and dispersion matrix via Black-Litterman with elliptical distributions; optimal weights derived as w* = (1/δ) D_BL^{-1} μ_BL; TD3 actor refines BLED weights.
- **Short entry:** Permitted via absolute-value normalization: Σ|w_i| = 1, w_i ∈ [-1, 1]. Negative weights represent short positions.
- **Exit:** Continuous rebalancing at daily frequency; transaction costs penalize turnover at c = 0.0025 per unit turnover.
- **Holding period:** Daily rebalancing (no fixed holding period).
- **Position sizing:** Full investment constraint (each model invests its full available balance at every step); fractional shares permitted.
- **Parameters:** BAVAR ensemble size: 600 models; 9 hyperparameter combinations (α ∈ {0.01, 0.1, 1}, β ∈ {1, 10, 100}); burn-in ratio: 0.34; τ_BAVAR: 0.077; τ_BL: 0.039; σ²_Ω: 0.052; BAVAR update frequency: ~12 times/year (monthly, every 21 trading days); transformer d_model: 128, 2 heads, 4 layers; critic: 3 layers, hidden size 512.
- **Specification status:** Fully specified in primary source; parameters are tuned via Optuna/TPE over 40 trials, validated on 20% holdout, tested on final 20%.

## Required data

- **Instrument:** 29 DJIA constituent stocks (NVIDIA excluded as outlier).
- **Universe:** Dow Jones Industrial Average constituents as of the study period; no explicit reconstitution or survivorship-bias correction discussed.
- **Venue:** Not specified; data sourced from yfinance (Yahoo Finance adjusted close prices).
- **Market type:** US equities (spot).
- **Timeframe:** Daily bars.
- **Fields:** Adjusted close price, volume, 5 EMAs (10/20/50/100/200), MACD + signal line, RSI, Bollinger Bands.
- **Point-in-time:** Data spans January 2014 – December 2024; 60/20/20 chronological train/validation/test split (1640/547/547 days).
- **Timestamp:** Daily adjusted close prices; timezone not specified (likely US market hours).
- **Missing data:** Not explicitly addressed.
- **Funding/fee/spread:** Transaction cost of 0.25% per rebalance (calibrated for $100K portfolio trading liquid US equities, citing Frazzini et al. 2018). Market impact assumed zero. Slippage not modeled. Spread not modeled. Fill model: immediate execution at adjusted close prices.

## Execution assumptions

- **Signal-to-order timing:** Daily rebalancing at adjusted close; no intraday execution discussed.
- **Fill model:** Immediate execution at adjusted close prices (zero latency).
- **Market / limit orders:** Market orders assumed.
- **Fees:** 0.25% per rebalance (turnover-proportional).
- **Slippage:** Not modeled (source states "zero market impact" and "immediate execution without slippage").
- **Spread:** Not modeled.
- **Impact / capacity:** Zero market impact assumed. Capacity not discussed.
- **Leverage / margin:** Short selling permitted; absolute-value normalization constrains total exposure to 1.
- **Borrow / shorting:** Permitted in simulation.
- **Latency:** Zero latency assumed.
- **Partial fills / failures:** Not discussed.
- **Training:** 4x NVIDIA RTX 4090 GPUs, ~80 GPU-hours, 500 episodes per configuration. Inference: single CPU in real-time.

## Evidence

### Source-reported

All performance figures below are directly reported by Mikriukov et al. (arXiv:2606.09104v1, June 2026), evaluated on the held-out test set (last 20% of data, ~547 days):

- **BAVAR-BLED:** Total return 57.26%, Sharpe 1.72, Sortino 2.70, Max Drawdown -8.85%, Volatility 12.64%
- **Best transformer baseline (TimeXer):** Total return 47.77%, Sharpe 1.57, Sortino 2.48, MDD -8.49%, Vol 11.90%
- **Best DRL baseline (Risk-Adj DRL):** Total return 52.70%, Sharpe 1.21, Sortino 1.70, MDD -12.83%, Vol 17.46%
- **Dual MA:** Total return 48.14%, Sharpe 1.59, Sortino 2.53, MDD -9.22%, Vol 11.86%
- **Momentum:** Total return 48.03%, Sharpe 1.44, Sortino 2.19, MDD -11.08%, Vol 13.21%

Ablation study (`source-reported`): Removing BAVAR reduces Sharpe from 1.72 to 0.05, confirming BAVAR is the essential component. BAVAR provides adaptive regime-aware priors; without it, the model reverts to static historical estimates.

Statistical validation (`source-reported`): Binomial test for cumulative dominance shows significance (p < 0.05) against 15 of 16 benchmarks. Rolling Sharpe comparisons (30/60/90-day windows) via paired t-tests and sign tests confirm significance against all 16 benchmarks.

Cost treatment: Transaction cost of 0.25% per rebalance is included in the return calculation. Market impact, slippage, spread, and borrowing costs are assumed zero (`source-reported`).

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

1. **Out-of-sample extension test:** Apply the trained BAVAR-BLED model to a different stock universe (e.g., S&P 500, Nasdaq 100, or non-US equities) without retraining. `Research-defined failure threshold`: If Sharpe ratio drops below 0.5 or total returns become negative, the regime-adaptive hypothesis does not generalize beyond the DJIA sample.
2. **Cost stress test:** Re-evaluate with realistic market impact and slippage models (e.g., 5–10 bps per trade). `Research-defined failure threshold`: If Sharpe ratio drops below 1.0, the 0.25% cost assumption is insufficiently conservative.
3. **BAVAR component ablation:** Already conducted by source. Sharpe collapses from 1.72 to 0.05 without BAVAR. This confirms but does not independently verify the result.
4. **Regime-specific breakdown:** Analyze performance during identified regime shifts (e.g., COVID crash Mar 2020, 2022 rate hikes) vs. tranquil periods. If BAVAR-BLED underperforms baselines during the most volatile regimes, the regime-adaptive claim is weakened.
5. **Hyperparameter sensitivity:** Vary BAVAR ensemble size (e.g., 100 vs. 600 models) and update frequency (e.g., daily vs. monthly). If performance is highly sensitive to exact ensemble size, the robustness claim is weakened.
6. **Survivorship bias audit:** The DJIA universe is selected ex post and may exhibit survivorship bias. Re-run on a broader, survivorship-free universe. If performance degrades substantially, the results may partly reflect selection luck.
7. **Competing explanation test:** Compare against a simpler regime-detection baseline (e.g., HMM-based regime switching with the same Black-Litterman framework). If the simpler regime model achieves comparable Sharpe, the BAVAR ensemble complexity is not justified.
8. **What action follows failure:** If cost stress or out-of-sample tests fail, the strategy is rejected for implementation unless the framework can be adapted with tighter cost controls or broader universe validation.

## Crypto portability

`adapted`

The regime-adaptive Bayesian prior mechanism and fat-tail modeling are theoretically portable to crypto markets, where regime shifts are more frequent and return distributions are more fat-tailed than equities. However, the source provides no crypto evidence.

Crypto-specific portability risks:
- **Regime frequency:** Crypto markets exhibit more frequent and extreme regime shifts than DJIA equities; the HAR feature horizons (daily/weekly/monthly) may be insufficient for 24/7 crypto markets.
- **Liquidity and capacity:** The DJIA universe consists of highly liquid large-cap equities; crypto perpetual futures and altcoins have much thinner order books and higher market impact.
- **Funding costs:** Crypto perpetual futures incur funding fees every 1–8 hours, creating an unmodeled carry drag on long positions.
- **Market structure:** The study assumes spot equity execution; crypto perpetuals have mark/index prices, liquidation mechanics, and basis dynamics not captured.
- **Transaction costs:** The 0.25% cost assumption may be optimistic for smaller crypto assets but conservative for BTC/ETH perpetuals on major venues.
- **Short selling:** Crypto perpetuals allow easy shorting via perpetual contracts, which is structurally different from equity short selling with borrow costs.

## Limitations

- **Universe selection:** 29 DJIA constituents selected ex post; survivorship bias is possible (`data gap`).
- **Cost model oversimplification:** Market impact, slippage, spread, and borrowing costs assumed zero; only 0.25% turnover cost modeled (`underspecified`).
- **No independent reproduction:** All results are source-reported.
- **No crypto evidence:** Strategy is evaluated on US equities only; crypto portability is unproven (`unproven`).
- **Computational complexity:** Maintaining 600 VAR models requires significant computational resources during training (~80 GPU-hours); asynchronous BAVAR updates at monthly frequency are a practical compromise but may degrade performance (`data gap` for full-frequency vs. monthly update comparison).
- **HAR feature horizons:** Limited to daily/weekly/monthly due to computational constraints; longer horizons (quarterly, yearly) may improve regime detection (`underspecified`).
- **No regime labeling:** The paper does not label or identify specific regimes during the test period, making regime-specific performance analysis impossible from the source (`data gap`).
- **Full investment constraint:** The environment requires full investment at every step, which inflates volatility for the highest-performing model (BAVAR-BLED) since larger capital bases amplify fluctuations.

## Implementation status

`not-implemented`. No implementation in `nautilus-quant-system`, PyBroker, or NautilusTrader has been executed. No strategy family has been created, and no backtest campaign has been initiated.

## Adoption boundary

`research-only`. A record being present in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

## Related Wiki records

- [[quant/alpha-scheme-surrogate-guided-factor-mining-2026-09-04]] — AlphaSchema uses surrogate-guided factor mining; BAVAR-BLED uses Bayesian VAR ensemble for regime-adaptive priors.
- [[quant/adaptive-alpha-weighting-ppo-2026-09-03]] — Adaptive alpha weighting with PPO; BAVAR-BLED uses TD3 with Black-Litterman under elliptical distributions.
- [[quant/regime-switching-hmm-reinforcement-learning-etf-allocation-2026-09-04]] — HMM-based regime switching for ETF allocation; BAVAR-BLED uses implicit regime detection via Bayesian model averaging.

## Sources

1. Mikriukov, D., Sun, R., Stefanidis, A., Su, J., and Jiang, Z. (2026). "Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian VAR and Elliptical Black-Litterman." arXiv preprint `arXiv:2606.09104v1 [cs.LG / q-fin.PM]`, submitted June 8, 2026.
   - Stable URL: https://arxiv.org/abs/2606.09104
   - Full text HTML: https://arxiv.org/html/2606.09104v1
   - DOI: https://doi.org/10.48550/arXiv.2606.09104
2. Mikriukov, D., Sun, R., Stefanidis, A., Su, J., and Jiang, Z. (2025). "Black-Litterman under Elliptical Distributions" (BLED). Presented at ICIC 2025. Referenced as prior work in arXiv:2606.09104.
