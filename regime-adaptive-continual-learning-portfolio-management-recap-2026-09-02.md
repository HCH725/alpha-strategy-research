---
schema: strategy-research-record-v1
title: "Regime-Adaptive Continual Learning for Portfolio Management (ReCAP): CUSUM Change-Point Segmentation, Modular Policy Vectors, and Soft Gated Task Composition"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-management
  - continual-learning
  - reinforcement-learning
  - regime-detection
  - cusum
  - task-arithmetic
  - policy-library
status: research-only
confidence: high
source_as_of: 2026-06-01
sources:
  - "Chaofan Pan, Lvfeng Ren, Leibo Xiao, Yonghao Li, Wei Wei, Xin Yang, 'Regime-Adaptive Continual Learning for Portfolio Management', In Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26), arXiv:2606.00143v1 [cs.LG, q-fin.PM], June 1, 2026. DOI: 10.1145/3770855.3817620. https://arxiv.org/abs/2606.00143"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Regime-Adaptive Continual Learning for Portfolio Management (ReCAP): CUSUM Change-Point Segmentation, Modular Policy Vectors, and Soft Gated Task Composition

## Provenance

- **Primary Source:** Chaofan Pan (Southwestern University of Finance and Economics / Shanxi University), Lvfeng Ren (SWUFE), Leibo Xiao (SWUFE), Yonghao Li (SWUFE), Wei Wei (Shanxi University), and Xin Yang (SWUFE), *"Regime-Adaptive Continual Learning for Portfolio Management"*, Accepted to the *32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2026)*; arXiv preprint `arXiv:2606.00143v1 [cs.LG, q-fin.PM]`, published June 1, 2026. DOI: [10.1145/3770855.3817620](https://doi.org/10.1145/3770855.3817620). Full text: [https://arxiv.org/abs/2606.00143](https://arxiv.org/abs/2606.00143).
- **Code Repository:** [https://github.com/Dumail/ReCAP](https://github.com/Dumail/ReCAP).
- **Primary Subject Areas:** Machine Learning (`cs.LG`), Portfolio Management (`q-fin.PM`), Artificial Intelligence (`cs.AI`).
- **Context:** Financial time series exhibit severe non-stationarity, regime shifts, and structural breaks that cause static machine learning models and fixed-window reinforcement learning (RL) agents to suffer rapid "alpha decay". Existing remedies—such as rolling-window full retraining or naive continuous fine-tuning—suffer respectively from high computational overhead and catastrophic forgetting. Pan et al. formulate multi-asset portfolio management as a Continual Reinforcement Learning (CRL) problem under dynamic Markov Decision Processes (MDPs) with modular task arithmetic.

## Economic mechanism

### Source-reported

1. **Market Non-Stationarity and Regime Recurrence:** Asset return distributions, volatility clusters, and cross-asset correlations shift abruptly during macroeconomic shocks, crises, or monetary policy transitions. However, financial regimes (e.g., high-volatility sell-off, low-volatility trend, stagflationary chop) exhibit statistical recurrence.
2. **Knowledge Retention via Task Arithmetic:** Rather than retraining monolithic networks from scratch or overwriting weights via continuous SGD, fine-tuning an offline base policy $\theta_0$ on a detected stationary regime $\tau_k$ yields a compact "policy vector" $\mathbf{d}_k = \theta_k - \theta_0$. Policy vectors can be merged, pruned, and linearly combined without catastrophic forgetting.
3. **Dynamic Attention Gating:** A regime-gating network observes macro-level volatility and turbulence indicators, outputting attention weights $\boldsymbol{\alpha}_t$ across a preserved policy library $\mathbf{D}$. This allows zero-shot synthesis of customized trading policies tailored to the prevailing market state.

### Research interpretation

The falsifiable thesis is that **explicitly decoupling online adaptation into data-driven CUSUM regime segmentation, modular policy-vector library maintenance ($\mathbf{d}_k = \theta_k - \theta_0$), and macro-gated policy blending ($\theta_t = \theta_0 + \sum \alpha_t^k \mathbf{d}_k$) yields strictly higher out-of-sample risk-adjusted returns and lower maximum drawdowns than static RL (EIIE, SARL, AlphaGAT), rolling-window retraining, and standard continual learning baselines (EWC, Experience Replay, Constrained Rationals)**:
- Variable-length regime boundaries align neural parameter updates with genuine market state transitions rather than arbitrary calendar windows (e.g., quarterly or yearly rolls).
- Freezing base weights $\theta_0$ and the policy library $\mathbf{D}$ while updating only the regime gate $\phi$ and the active regime increment $\mathbf{d}_{\text{new}}$ guarantees bounded parameter drift and computational efficiency.

## Signal

### 1. Multi-Asset MDP & State Formulation

At each time step $t$, the portfolio agent manages $N$ tradable assets plus a cash reserve:
- **Asset-Level Trading State $\mathbf{s}_t \in \mathbb{R}^{B \times F \times N}$:**
  Each asset $i \in \{1, \dots, N\}$ provides $F=26$ features: OHLCV, MACD, Bollinger Bands (upper, lower), RSI-30, CCI-30, DX-30, 30-day and 60-day moving averages, multi-horizon adjusted price returns (5, 10, 15, 20, 25, 30 days), normalized open/high/low, close return, VIX, and financial turbulence index.
- **Action (Portfolio Weights) $\mathbf{w}_t \in \mathcal{A}$:**
  $$\mathbf{w}_t = [w_{t,0}, w_{t,1}, \dots, w_{t,N}]^\top, \quad \sum_{i=0}^N w_{t,i} = 1, \quad w_{t,i} \ge 0$$
- **Reward Function:** Log portfolio return accounting for proportional transaction costs:
  $$r_t = \log \left( \frac{V_t}{V_{t-1}} \right)$$

### 2. Adaptive Regime Detection (ARD) via Parallel CUSUM

To partition historical and streaming observations into approximately stationary regimes $\{\tau_1, \dots, \tau_M\}$, ARD applies parallel Cumulative Sum (CUSUM) change-point detection across market-level indicators $\mathbf{m}_t$ (VIX, turbulence, Bollinger bands, 5-day market return, RSI-30):
$$S_t^{(u)} = \max\left(0, S_{t-1}^{(u)} + (u_t - \mu_0) - \kappa \sigma_u\right)$$
where $\mu_0$ is the reference mean over a historical baseline window, $\kappa = 0.5$ is the drift sensitivity parameter, and $\sigma_u$ is feature standard deviation.
- **Regime Shift Trigger:** A change point is flagged whenever $S_t^{(u)} > h \sigma_u$ (with threshold multiplier $h = 2.5$).
- When triggered, the statistic is reset to zero, $\mu_0$ is recalibrated, and the completed interval $\tau_{k-1} = [t_{k-1}^{\text{start}}, t_{k-1}^{\text{end}}]$ forms a discrete continual learning task.

### 3. Policy Vector & Library Maintenance

- **Base Policy:** Offline pretraining on multi-year historical data yields base parameters $\theta_0$.
- **Policy Vector Extraction:** On regime $\tau_k$, initialize at $\theta_0$ and fine-tune via Proximal Policy Optimization (PPO) for $10^4$ steps to obtain $\theta_k$. Define the policy vector:
  $$\mathbf{d}_k = \theta_k - \theta_0 \in \mathbb{R}^P$$
- **Similarity Merging & Pruning:**
  - Compute pairwise cosine similarity $\cos(\mathbf{d}_i, \mathbf{d}_j)$. If $\cos(\mathbf{d}_i, \mathbf{d}_j) > \delta_s = 0.5$, merge via parameter averaging: $\mathbf{d}_{\text{merged}} = \frac{1}{2}(\mathbf{d}_i + \mathbf{d}_j)$.
  - Discard vectors with negligible $\ell_2$-norm $\|\mathbf{d}_k\|_2 < \epsilon$ or near-zero historical gating attention.
  - Store retained distinct vectors in the policy library $\mathbf{D} = [\mathbf{d}_1, \dots, \mathbf{d}_K] \in \mathbb{R}^{P \times K}$.

### 4. Regime-Gate Module (RGM) Composition

- At time $t$, RGM receives market-level regime features $\mathbf{m}_t$ and computes dynamic softmax attention weights:
  $$\boldsymbol{\alpha}_t = \operatorname{Softmax}\left(\operatorname{MLP}_\phi(\mathbf{m}_t)\right) = [\alpha_t^1, \dots, \alpha_t^K, \alpha_t^{\text{new}}]^\top$$
- **Effective Policy Synthesis:**
  $$\theta_t = \theta_0 + \sum_{k=1}^K \alpha_t^k \mathbf{d}_k + \alpha_t^{\text{new}} \mathbf{d}_{\text{new},t}$$
- **Weight Execution:** $\mathbf{w}_t = f_{\theta_t}(\mathbf{s}_t)$, generating allocation weights via the composite policy network.
- **Continual Update Rule:** During online trading, $\theta_0$ and $\mathbf{D}$ remain frozen; only gate parameters $\phi$ and the active regime vector $\mathbf{d}_{\text{new}}$ receive gradient updates.

## Required data

- **Universe:** Multi-asset equity indices and commodity baskets:
  - US Equities: DOW30 ($N=29$), NAS100 ($N=73$), S&P 500 ($N=398$).
  - Japanese Equities: NIKKEI30 ($N=29$).
  - Commodities: COMMODITY_ETF ($N=7$: GLD, SLV, DBC, USO, UNG, DBA, GSG).
- **Timeframe:** Daily OHLCV bars spanning 17 years (May 1, 2008 to April 29, 2025; 12 years offline pretraining 2008–2020, 5 years online evaluation 2020–2025).
- **Macro/Market Regimes:** CBOE Volatility Index (VIX), Financial Turbulence Index, Bollinger Band width, 5-day market return, RSI-30.
- **Point-in-Time Hygiene:** All normalization ($z$-scoring) and technical indicator computations strictly use expanding/rolling historical windows with no look-ahead.

## Execution assumptions

- **Execution Timing:** Daily close-to-close rebalancing.
- **Transaction Costs:** Proportional trading fee fixed at $10\text{ bps}$ ($0.10\%$) per trade notional.
- **Sensitivity Bounds:** Evaluated under cost stress at $+5\text{ bps}$ ($15\text{ bps}$ total) and $+10\text{ bps}$ ($20\text{ bps}$ total).
- **Position Limits:** Long-only portfolio weights $w_{t,i} \ge 0$, $\sum w_{t,i} = 1$, zero leverage, zero shorting.
- **Critic Reinitialization:** Policy vector learning applies strictly to the actor network (2-layer MLP, 64 hidden units, Tanh activations); the value critic is reinitialized at each regime shift to prevent value estimate contamination.

## Evidence

### Source-reported

All empirical figures below are directly reported by Chaofan Pan et al. (arXiv:2606.00143v1 / KDD 2026) across 10 random seeds on the 2020–2025 out-of-sample evaluation period:

1. **Comparison with Quantitative & Deep RL PM Baselines (Table 2 & Table 3):**
   - **NAS100 ($N=73$):** ReCAP achieves **164.89% Cumulative Return (CR)**, **1.14 Sharpe Ratio (SR)**, and **23.95% Maximum DrawDown (MDD)**, outperforming the strongest baseline Cross-Insight (124.24% CR, 0.92 SR, 30.12% MDD), PPO (112.45% CR, 0.86 SR), SAC (108.32% CR, 0.81 SR), and AlphaGAT (overfitting failure).
   - **DOW30 ($N=29$):** ReCAP achieves **84.32% CR**, **0.88 SR**, and **18.42% MDD** (vs Cross-Insight 74.15% CR, 0.79 SR, 22.15% MDD).
   - **S&P 500 ($N=398$):** ReCAP achieves **142.18% CR**, **1.05 SR**, and **21.30% MDD** (vs PPO 98.40% CR, 0.78 SR; ReCAP attains nearly double the average performance of standard baselines in high-dimensional state spaces).
   - **NIKKEI30 ($N=29$):** ReCAP achieves **133.29% CR**, **1.00 SR**, and **19.85% MDD** (vs Cross-Insight 127.70% CR, 0.95 SR).
   - **COMMODITY_ETF ($N=7$):** ReCAP achieves **68.45% CR**, **0.76 SR**, and **16.12% MDD**, outperforming all traditional heuristics (CRP, EG, UP, OLMAR, WMAMR).

2. **Comparison with Continual Learning (CL) Strategies (Table 4):**
   - Under matched PPO base updates ($10^4$ steps per regime), ReCAP demonstrates superior Average Performance (AP) and Forward Transfer (FT) over Elastic Weight Consolidation (EWC), Experience Replay (ER, buffer 3,000), Constrained Rationals (CoR), and standard rolling-window Retraining (12-year window).

3. **Ablation Studies on NAS100 (Figure 4):**
   - Removing ARD (`w/o-ARD`, using fixed-length calendar windows) causes the largest performance drop, confirming that data-driven regime alignment is the primary driver of CRL efficacy.
   - Removing Policy Library (`w/o-PL`, retaining only the single most recent policy vector) causes severe drop in Average Performance (AP), proving the necessity of historical policy vector retention.
   - Removing Regime Gate (`w/o-RGM`, using uniform/random weighting) degrades risk-adjusted return.

4. **Detector & Cost Sensitivity (Table 5 & Appendix B):**
   - Replacing CUSUM with a Hidden Markov Model (HMM) with BIC model selection yields **146.38% CR**, **1.10 SR**, and **24.22% MDD** on NAS100, proving the framework is robust to alternative regime detectors.
   - Under $+10\text{ bps}$ cost stress ($20\text{ bps}$ total friction), ReCAP maintains $>25\%$ return margin over baselines.

5. **Policy Library Interpretability (Seed 0 on NAS100):**
   - Starting with 12 pretraining vectors, over 37 online detected regimes, ARD/RGM performed 10 insertions, 12 merges, and 15 discards, stabilizing at 22 compact policy vectors. The top 5 vectors captured $85.4\%$ of total gate attention ($34.3\%, 26.1\%, 10.5\%, 10.2\%, 4.3\%$).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed paper; absence is not evidence of no negative result.
- Static mean-reversion heuristics (OLMAR, WMAMR) and complex two-stage architectures (AlphaGAT) suffered catastrophic drawdowns in trending/shifting equity regimes.

## Falsification plan

1. **Placebo / Shuffled Regime Boundary Test:** Replace ARD change points with random Poisson change points matching the empirical frequency ($\approx 7.4$ regimes/year). If ReCAP with shuffled boundaries performs on par with ARD, the CUSUM detection mechanism provides zero economic timing alpha.
2. **Static Equal-Weight Vector Baseline:** Replace dynamic RGM gate $\boldsymbol{\alpha}_t$ with fixed uniform weights $\alpha_t^k = 1/K$. If the uniform blend achieves comparable SR/MDD, the neural regime-gate adds unnecessary complexity.
3. **Severe Liquidity & Slippage Stress:** Increase execution costs from $10\text{ bps}$ to $50\text{ bps}$ (representative of mid-cap crypto perpetuals or high turnover). If turnover-induced drag erodes all excess return, the continuous weight adjustments fail execution viability.
4. **Failure Threshold:** If out-of-sample Sharpe ratio drops below $0.50$ or maximum drawdown exceeds $35\%$ across a 3-year walk-forward test, reject the strategy family.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Regime Frequency in Crypto:** Crypto markets exhibit significantly higher regime shift velocity (abrupt leverage flush-outs, funding rate spikes, liquidity dry-ups occurring over hours rather than weeks). CUSUM drift $\kappa$ and threshold $h$ must be calibrated to 1-hour or 4-hour bar intervals.
- **Regime Feature Adaptation:** VIX must be replaced by Crypto Implied Volatility indices (e.g., Deribit DVOL for BTC/ETH) and augmented with aggregate perpetual funding rates, Open Interest (OI) velocity, and stablecoin supply growth.
- **Shorting & Funding Friction:** Long-short portfolio weights and perpetual funding carry must be integrated into the log-reward function $r_t$.

## Limitations

- **Actor Architecture Simplicity:** Evaluated primarily on 2-layer MLPs; scaling policy vectors to large Transformer architectures (e.g., Decision Transformer) may inflate memory and merging complexity.
- **Lookback Lag in CUSUM:** Change-point detection requires a post-shift accumulation window of $S_t > h$, introducing an inherent detection delay before a new regime is declared.
- **Absence of Shorting:** The reported experiments enforce long-only constraints ($w_i \ge 0$), leaving market-neutral long-short dynamics unverified.

## Implementation status

`not-implemented` in the quantitative production stack.

## Adoption boundary

Research capture only. A record being present in this repository does not constitute authorization for deployment, implementation in PyBroker/Nautilus, or allocation of capital in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/equity-cross-regime-bayesian-optimisation-xgboost-tabnet-hybrid-2026-09-02]]`
- `[[quant/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02]]`
- `[[quant/portfolio-bayesian-parametric-policies-policy-risk-regularization-2026-09-02]]`

## Sources

1. Chaofan Pan, Lvfeng Ren, Leibo Xiao, Yonghao Li, Wei Wei, Xin Yang, *"Regime-Adaptive Continual Learning for Portfolio Management"*, In *Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26)*, arXiv preprint `arXiv:2606.00143v1 [cs.LG, q-fin.PM]`, June 1, 2026. DOI: [10.1145/3770855.3817620](https://doi.org/10.1145/3770855.3817620). Stable URL: [https://arxiv.org/abs/2606.00143](https://arxiv.org/abs/2606.00143).
2. Official Code Implementation: [https://github.com/Dumail/ReCAP](https://github.com/Dumail/ReCAP).
