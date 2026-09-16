---
schema: strategy-research-record-v1
title: "AD-Seq-Vol: Adaptive Sequential Diffusion Models for Dynamic Implied-Volatility Surface Generation and Sparse Data-Driven Option Hedging"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - diffusion-models
  - implied-volatility
  - option-hedging
  - static-arbitrage
  - data-driven-hedging
status: research-only
confidence: medium
source_as_of: 2026-09-14
sources:
  - "Yinbin Han, Jack Yuxiang Zhang, Manuel Torres, Fernando Acero, and Renyuan Xu, 'Diffusion models for dynamic volatility surface generation and data-driven hedging', arXiv:2609.13402v1 [q-fin.CP, cs.LG, q-fin.MF, q-fin.RM, q-fin.TR], September 14, 2026. https://arxiv.org/abs/2609.13402"
  - "yinbinhan/volatility-surface-simulation GitHub repository, commit 9ba265ecbf32979d970b9beab7dfde3585163509, https://github.com/yinbinhan/volatility-surface-simulation"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AD-Seq-Vol: Adaptive Sequential Diffusion Models for Dynamic Implied-Volatility Surface Generation and Sparse Data-Driven Option Hedging

## Provenance

- **Primary Research Paper:**
  - Authors: Yinbin Han (Department of Mathematics, Imperial College London), Jack Yuxiang Zhang (Oxford-Man Institute of Quantitative Finance, University of Oxford), Manuel Torres (Department of Computing, Imperial College London), Fernando Acero (Department of Mathematics, Imperial College London), and Renyuan Xu (Department of Industrial and Systems Engineering, University of Southern California).
  - Title: *"Diffusion models for dynamic volatility surface generation and data-driven hedging"*.
  - Publication: arXiv preprint `arXiv:2609.13402v1 [q-fin.CP, cs.LG, q-fin.MF, q-fin.RM, q-fin.TR]`, submitted September 14, 2026.
  - Abstract URL: https://arxiv.org/abs/2609.13402
  - Full-Text HTML: https://arxiv.org/html/2609.13402v1
  - Full-Text PDF: https://arxiv.org/pdf/2609.13402v1
  - Canonical DOI: [10.48550/arXiv.2609.13402](https://doi.org/10.48550/arXiv.2609.13402)

- **Primary Source Code Repository:**
  - URL: https://github.com/yinbinhan/volatility-surface-simulation
  - Full Immutable Commit SHA: `9ba265ecbf32979d970b9beab7dfde3585163509`
  - Inspected Paths: `README.md`, `arbitrage_3way.py`, `backtest_diffusion.py`, `fine_tune.py`, `hedging.py`, `hedging_backtest_utils.py`, `summarize_hedging_results.py`, `train.py`, `config/config.py`.

- **Verification Integrity:**
  - The complete full-text HTML and 18-page PDF of `arXiv:2609.13402v1` as well as the exact public GitHub codebase at commit `9ba265ecbf32979d970b9beab7dfde3585163509` were directly retrieved and inspected.
  - All mathematical equations, Ornstein-Uhlenbeck forward/reverse diffusion formulations, static-arbitrage penalties ($\ell_1, \ell_2, \ell_3$), LASSO coordinate-descent solvers, empirical tracking error statistics, and baseline comparisons trace directly to primary source files and published text.
  - No search engine snippets, secondary summaries, or model-generated hallucinations were used to construct strategy rules or quantitative empirical claims.

- **Repository Deduplication Audit:**
  - Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `arXiv:2609.13402`, Yinbin Han, Jack Yuxiang Zhang, or the AD-Seq-Vol framework.
  - Related options records in the repository (`crypto-bitcoin-option-dynamic-hedging-whalley-wilmott-no-trade-band-2026-09-01.md`, `spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md`, `crypto-convolutional-vae-volatility-surface-completion-anomaly-2026-09-01.md`, `transformer-ddqn-straddle-option-volatility-trading-2026-09-05.md`) focus on parametric SVI calibration, asymptotic Whalley-Wilmott no-trade bands, deep Q-networks for single straddles, or static Conv-VAE surface completion. None implement adaptive sequential score-based diffusion with low-rank static-arbitrage fine-tuning and transaction-cost-regularized LASSO option panel selection.

## Economic mechanism

### Source-reported

Mainstream generative approaches to financial volatility surfaces (principally Generative Adversarial Networks [GANs] and Variational Autoencoders [VAEs]) suffer from fundamental limitations: GANs exhibit training instability and mode collapse, whereas VAEs tend to oversmooth complex distributions. More critically, prior models (such as VolGAN) model static surfaces or unconditional distributions, generating only one-step next-day surfaces from the current state without preserving multi-period temporal conditioning along evolving information filtrations.

AD-Seq-Vol resolves these deficiencies through a two-stage mechanism:
1. **Adaptive Sequential Diffusion Simulator:** Extends score-based diffusion models to high-dimensional objects by treating the daily implied volatility surface on an $11 \times 9$ moneyness-maturity grid jointly with the underlying asset return. The model is trained via denoising score matching on time-varying Ornstein-Uhlenbeck (OU) processes. By recursively updating the conditioning history with previously generated surfaces, it generates adapted, non-anticipative multi-day scenarios that preserve both cross-sectional skew/term structure and temporal path dependence.
2. **Static No-Arbitrage Fine-Tuning (AD-Seq-Vol-FT):** Real-world option prices must satisfy absence of static arbitrage (monotonicity in maturity, monotonicity in strike/moneyness, and convexity in moneyness). AD-Seq-Vol-FT employs Low-Rank Adaptation (LoRA) to fine-tune the pretrained diffusion score network with a reward function penalizing calendar-spread ($\ell_1$), call-spread ($\ell_2$), and butterfly-spread ($\ell_3$) violations, reducing static arbitrage violations to near zero.
3. **Data-Driven Sparse Hedging:** Rather than relying on rigid parametric assumptions (e.g., Black-Scholes Greeks that fail during severe market disruptions), the simulated conditional scenarios feed directly into an optimization-based hedging problem. The objective minimizes one-step scenario tracking error while penalizing rebalancing transaction costs scaled by half the bid-ask spread via an $L_1$ LASSO penalty. This yields sparse, cost-aware hedge portfolios across an available panel of underlying and option contracts.

### Research interpretation

The proposed alpha/hedging edge rests on **non-parametric conditional scenario generation combined with friction-aware sparse inventory control**:
- **Non-Parametric Greek Replacement:** Classical delta and delta-vega hedging assume instantaneous local linearities under Brownian underlying dynamics with constant or deterministic volatility. In real markets, volatility exhibits jumps, leverage effects, and severe regime shifts. By sampling from an adapted generative score model conditioned on the preceding 21 days of joint price-surface history, the scenario distribution implicitly incorporates empirical skew dynamics, volatility clustering, and smile deformation without requiring restrictive analytical SDE calibration.
- **Sparse LASSO Hedging as Cost Optimization:** Standard dynamic hedging with options requires frequent rebalancing across multiple strikes, incurring substantial bid-ask drag. Enforcing an $L_1$ transaction-cost penalty regularized by Akaike Information Criterion (AIC) forces the optimizer to trade only when expected variance reduction across diffusion scenarios exceeds the round-trip execution cost.
- **Stress-Regime Robustness:** During severe volatility spikes (e.g., March 2020 COVID shock), parametric Black-Scholes Greeks experience explosive breakdown, generating massive hedging tracking errors. Because the sequential diffusion model conditions on real-time historical trajectory updates, its generated scenario fan immediately widens and shifts, enabling the LASSO optimizer to position hedges that absorb tail moves without compounding losses.

## Signal

### Signal Formation and Timeline
- **Observation Window:** 21 consecutive trading days of joint underlying SPX log returns and log-implied volatility surfaces (`source-reported`).
- **Formation Timestamp:** Daily at market close ($t$), upon receipt of OptionMetrics end-of-day smoothed mid-quotes and underlying close prices (`source-reported`).
- **Rebalance Frequency:** Daily at close (`source-reported`).
- **Rebalance Execution:** One-day-ahead holding interval $[t, t+\Delta t]$, re-solved at each subsequent trading date until option expiry (`source-reported`).

### Target Portfolio and Hedging Universe
- **Target Position:** Long straddle (one call and one put) with strike $K = m_0 S_{t_1}$ initiated at date $t_1$, evaluated across initial moneyness levels $m_0 \in \{0.75, 0.80, 0.90, 1.10, 1.20, 1.25\}$ (`source-reported`).
- **Candidate Hedging Panel ($\mathcal{H}$):** 8 candidate instruments sharing the target straddle expiry date (`source-reported`):
  1. Underlying SPX index ($S_t$).
  2. Put option at strike $0.90 S_{t_1}$.
  3. Put option at strike $0.95 S_{t_1}$.
  4. Put option at strike $0.975 S_{t_1}$.
  5. Call option at strike $1.00 S_{t_1}$ (fixed ATM call).
  6. Call option at strike $1.025 S_{t_1}$.
  7. Call option at strike $1.05 S_{t_1}$.
  8. Call option at strike $1.10 S_{t_1}$.
- **Exclusion Rule:** Contracts comprising the target straddle are strictly excluded from the candidate hedging set (`source-reported`).

### Generative Scenario Sampling
- **State Vector $\mathbf{Y}_t$:** Tuple $(\mathbf{S}_t, \mathbf{X}_t)$, where $\mathbf{S}_t$ is the SPX log return and $\mathbf{X}_t \in \mathbb{R}^{11 \times 9}$ is the vectorized log-implied-volatility surface on an 11-moneyness by 9-maturity grid (`source-reported`).
- **Scenario Count:** Generate $N = 100$ one-step-ahead conditional scenarios $\{\mathbf{Y}_{t+\Delta t}^{(k)}\}_{k=1}^N$ using the trained AD-Seq-Vol or AD-Seq-Vol-FT score network via 200-step DDPM sampling (`source-reported`). (VolGAN requires $N = 1000$ scenarios for stability) (`source-reported`).
- **Option Revaluation:** Under each scenario $k$, revalue the target straddle $V_{t+\Delta t}^{(k)} = f(t+\Delta t, \mathbf{Y}_{t+\Delta t}^{(k)})$ and candidate hedging instruments $H_{t+\Delta t}^{i,(k)} = h_i(t+\Delta t, \mathbf{Y}_{t+\Delta t}^{(k)})$ using Black-Scholes pricing with implied volatility read from the simulated surface (`source-reported`). Compute simulated price changes $\Delta V_t^{(k)} = V_{t+\Delta t}^{(k)} - V_t$ and $\Delta H_t^{i,(k)} = H_{t+\Delta t}^{i,(k)} - H_t^i$ (`source-reported`).

### Hedge Optimization Objective
At each rebalancing date $t$, solve the transaction-cost-regularized LASSO problem via coordinate descent (`source-reported`):

$$\min_{A_t, \boldsymbol{\phi}_t} \frac{1}{N} \sum_{k=1}^N \left( \Delta V_t^{(k)} - A_t - \sum_{i \in \mathcal{H}} \phi_t^i \Delta H_t^{i,(k)} \right)^2 + \alpha \sum_{i \in \mathcal{H}} c_t^i g_0 |\phi_t^i - \phi_{t-\Delta t}^i|$$

where:
- $\phi_t^i$: Number of units held in instrument $i$ over $[t, t+\Delta t]$ (`source-reported`).
- $A_t$: Unpenalized intercept accounting for expected drift/carry (`source-reported`).
- $\phi_{t-\Delta t}^i$: Previous position in instrument $i$, with $\phi_0^i = 0$ (`source-reported`).
- $c_t^i$: Per-unit transaction cost, set to half the bid-ask spread of instrument $i$ at date $t$ ($c_t^i = \frac{1}{2}(\text{Ask}_t^i - \text{Bid}_t^i)$) (`source-reported`). For the underlying index, $c_t^{\text{underlying}} = 0.0$ (`source-reported` in codebase).
- $g_0$: Portfolio value scaling factor ($g_0 = V_t$), ensuring regularization strength $\alpha$ remains dimensionless across portfolio sizes (`source-reported`).
- $\alpha$: Regularization parameter selected dynamically at each rebalance step via Akaike Information Criterion (AIC) (`source-reported`).
- Solver specification: Coordinate descent with convergence tolerance `tol = 1e-10` and `max_iter = 1000` (`source-reported` in codebase).

### Static No-Arbitrage Constraints & Fine-Tuning
The implied volatility surface $\sigma_t(\mathbf{m}, \boldsymbol{\tau})$ across moneyness grid $\mathbf{m} = (m_1, \dots, m_{N_m})$ and maturity grid $\boldsymbol{\tau} = (\tau_1, \dots, \tau_{N_\tau})$ is mapped to normalized call prices $c_t(m_i, \tau_j)$. Absence of static arbitrage requires:
1. **Calendar Spread Condition ($\ell_1$):**
   $$\tau_j \frac{c_t(m_i, \tau_j) - c_t(m_i, \tau_{j+1})}{\tau_{j+1} - \tau_j} \le 0, \quad \forall j \in \{1, \dots, N_\tau - 1\}, i \in \{1, \dots, N_m\}$$
2. **Call Spread Condition ($\ell_2$):**
   $$\frac{c_t(m_{i+1}, \tau_j) - c_t(m_i, \tau_j)}{m_{i+1} - m_i} \le 0, \quad \forall j \in \{1, \dots, N_\tau\}, i \in \{1, \dots, N_m - 1\}$$
3. **Butterfly Spread Condition ($\ell_3$):**
   $$\frac{c_t(m_i, \tau_j) - c_t(m_{i-1}, \tau_j)}{m_i - m_{i-1}} - \frac{c_t(m_{i+1}, \tau_j) - c_t(m_i, \tau_j)}{m_{i+1} - m_i} \le 0, \quad \forall j \in \{1, \dots, N_\tau\}, i \in \{2, \dots, N_m - 1\}$$

Arbitrage penalty function:
$$L(\sigma_t(\mathbf{m}, \boldsymbol{\tau})) = \ell_1 + \ell_2 + \ell_3$$
where each component represents the sum of positive parts of the respective inequalities (`source-reported`).
- **Fine-Tuning (AD-Seq-Vol-FT):** Low-Rank Adaptation (LoRA) rank 8, 200 epochs, AdamW with initial learning rate $10^{-4}$, batch size 32, reward $-L(\cdot)$, KL divergence penalty weight 0.1 relative to pretrained weights (`source-reported`).

## Required data

- **Underlying Instrument:** S&P 500 Index (SPX) cash index (`source-reported`).
- **Option Instruments:** European-style SPX index options across standard expirations and strikes (`source-reported`).
- **Data Vendor & Source:** OptionMetrics IvyDB US (`source-reported`).
- **Sample Window:**
  - Full range: January 3, 2000 to February 28, 2023 (`source-reported`).
  - In-sample training window: January 3, 2000 to June 16, 2018 (4,621 rolling 22-day tensors) (`source-reported`).
  - Out-of-sample testing window: July 1, 2018 to February 28, 2023 (56 evaluation episodes including COVID, 51 excluding COVID) (`source-reported`).
  - COVID-19 stress window: February 13, 2020 to July 21, 2020 (`source-reported`).
- **Surface Discretization Grid:**
  - Moneyness $m = K / S$: 11 points: $\{0.60, 0.70, 0.80, 0.90, 0.95, 1.00, 1.05, 1.10, 1.20, 1.30, 1.40\}$ (`source-reported`).
  - Time-to-maturity $\tau$: 9 points: $\{1/252, 1/52, 2/52, 1/12, 1/6, 1/4, 1/2, 3/4, 1.0\}$ year (corresponding approximately to 1 day, 1 week, 2 weeks, 1 month, 2 months, 3 months, 6 months, 9 months, 1 year) (`source-reported`).
- **Quote Preprocessing:** Daily OptionMetrics option chains smoothed onto the common $11 \times 9$ grid using a vega-weighted Nadaraya-Watson kernel estimator with Gaussian kernel, followed by bilinear interpolation in moneyness and maturity (`source-reported`).
- **Interest Rate:** Risk-free discount rate derived daily as the median rate implied by put-call parity from option mid-prices (`source-reported`).
- **Missing Data Handling:** In OptionMetrics, raw quotes are volume-filtered; if a candidate hedging contract quote is missing on an intermediate date, the backtest records the gap without forward-imputing fabricated quotes (`source-reported` in codebase).

## Execution assumptions

- **Execution Timing:** Daily rebalance at closing mid-prices (`source-reported`). Signal generated after market close $t$; fill executed at recorded closing quote (`source-reported`).
- **Order Type & Fill Model:** Mid-price execution with transaction cost deductions (`source-reported`).
- **Transaction Costs:** Linear cost proxy $c_t^i$ equal to one-half of the quoted bid-ask spread: $c_t^i = \frac{1}{2}(\text{Ask}_t^i - \text{Bid}_t^i)$ (`source-reported`).
- **Underlying Cost Assumption:** Zero transaction cost on underlying SPX index ($c_t^{\text{underlying}} = 0.0$) (`source-reported` in codebase; `research-proposed` operational adjustment: in real index trading, SPX cash is uninvestable directly; traders use SPX mini/micro futures or SPY ETF with taker fee ~0.5–1.0 bps).
- **Borrow & Shorting:** Unconstrained short and long positions permitted in both options and underlying index (`source-reported`).
- **Margin & Leverage:** No margin constraints, haircut models, or borrowing financing rate penalties modeled (`source-reported`).
- **Market Impact:** No non-linear (square-root or quadratic) market impact model applied (`source-reported`).
- **Operational Execution Feasibility (`research-proposed`):** Live execution in live options markets requires resting limit orders inside the spread or paying full taker spread, crossing exchange fees (CBOE proprietary index fees of ~$0.50–$0.65 per contract), OCC clearing fees, and accommodating margin haircuts under portfolio margining rules.

## Evidence

### Source-reported

All empirical metrics below are directly reported by Han et al. (arXiv:2609.13402v1, Section 4, Tables 1–2, and repository summary files):

#### 1. Pooled Tracking-Error Statistics across All Moneyness ($m_0$)
One-step tracking error is defined as $\varepsilon_t = \Delta V_t - A_t - \sum_{i \in \mathcal{H}} \phi_t^i \Delta H_t^i$ (in USD per straddle contract):

| Evaluation Window | Hedging Method | Source | Mean | Median | Std | 5% VaR | 2.5% VaR | 1% VaR |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **COVID Included** | Unhedged | Han et al. | 5.15 | -7.26 | 118.95 | 170.38 | 230.04 | 276.87 |
| (56 episodes) | Delta | Han et al. | 1.40 | -1.78 | 41.09 | 30.53 | 40.63 | 51.46 |
| | Delta-vega | Han et al. | 0.15 | -0.04 | 15.53 | 15.37 | 21.77 | 29.66 |
| | VolGAN (published) | Cont & Vuletić [17] | 0.55 | -0.16 | 32.98 | 12.79 | 23.42 | 50.79 |
| | **AD-Seq-Vol** | **Han et al. (Ours)** | **1.04** | **-0.03** | **10.55** | **11.16** | **16.48** | **21.33** |
| | **AD-Seq-Vol-FT** | **Han et al. (Ours)** | **1.34** | **-0.01** | **12.01** | **11.74** | **16.93** | **21.11** |
| **COVID Excluded** | Unhedged | Han et al. | 2.53 | -7.24 | 107.72 | 167.78 | 222.38 | 264.62 |
| (51 episodes) | Delta | Han et al. | -2.62 | -1.78 | 17.41 | 27.39 | 35.75 | 46.50 |
| | Delta-vega | Han et al. | -1.18 | -0.05 | 8.20 | 14.81 | 21.53 | 32.72 |
| | VolGAN (published) | Cont & Vuletić [17] | -1.05 | -0.18 | 8.15 | 10.55 | 17.32 | 33.85 |
| | **AD-Seq-Vol** | **Han et al. (Ours)** | **0.78** | **0.02** | **8.33** | **10.72** | **16.97** | **21.54** |
| | **AD-Seq-Vol-FT** | **Han et al. (Ours)** | **1.00** | **0.08** | **8.55** | **11.11** | **16.41** | **20.35** |

*(Note: VaR is reported following the positive loss convention: $\text{VaR}_p = -\text{percentile}(\varepsilon, p)$).*

#### 2. High-Vega Near-Money Straddle Tracking Errors ($m_0 \in \{0.9, 1.1\}$)
For high-vega straddles where hedging is most sensitive to implied volatility smile shifts:
- **$m_0 = 0.90$ (COVID Included):**
  - Delta: Std 48.64, 5% VaR 32.90, 1% VaR 49.53.
  - Delta-vega: Std 20.43, 5% VaR 21.44, 1% VaR 45.57.
  - VolGAN (published): Std 68.66, 5% VaR 34.48, 1% VaR 80.78.
  - **AD-Seq-Vol:** Std **10.49**, 5% VaR **19.05**, 1% VaR **29.36**.
  - **AD-Seq-Vol-FT:** Std 15.09, 5% VaR **18.53**, 2.5% VaR **21.16** (lowest among all), 1% VaR 30.77.
- **$m_0 = 1.10$ (COVID Included):**
  - Delta: Std 33.24, 5% VaR 32.73, 1% VaR 53.83.
  - Delta-vega: Std 10.27, 5% VaR 10.13, 1% VaR 24.27.
  - VolGAN (published): Std 13.79, 5% VaR 19.17, 1% VaR 47.58.
  - **AD-Seq-Vol:** Std 8.45, 5% VaR 7.11, 1% VaR **10.26** (lowest among all).
  - **AD-Seq-Vol-FT:** Std **8.36**, 5% VaR **6.61**, 2.5% VaR **8.25**, 1% VaR 10.55.

#### 3. Hedge Sparsity and Instrument Selection
- Sparser Hedge Execution: AD-Seq-Vol selected an average of **4.73** instruments (median 5) out of the 8 candidates across rebalancing dates.
- VolGAN independent reimplementation required **5.51** instruments on average (median 6).
- Simulation Efficiency: AD-Seq-Vol stabilized with $N = 100$ generated scenarios, whereas VolGAN required $N = 1000$ scenarios to achieve numerical stability.

#### 4. Static Arbitrage Reduction via Fine-Tuning
- AD-Seq-Vol generated surfaces exhibited fewer static arbitrage violations than the raw training data across all three conditions ($\ell_1$ calendar, $\ell_2$ call vertical, $\ell_3$ butterfly spread).
- AD-Seq-Vol-FT reduced violation frequency and magnitude to **near zero** across all three constraints (Figure 3 in paper).

### Independently reproduced

Not independently reproduced. All figures, tables, and statistics cited above represent third-party empirical results reported by Han et al. (arXiv:2609.13402v1, September 2026) and their committed codebase (`yinbinhan/volatility-surface-simulation`). No independent simulation on OptionMetrics or live exchange quotes has been conducted in our research stack.

### Negative evidence

1. **No-Arbitrage Fine-Tuning Does Not Reduce Tracking Error Variance:** Despite driving static arbitrage violations to near zero, AD-Seq-Vol-FT does *not* improve overall tracking error standard deviation relative to un-fine-tuned AD-Seq-Vol (Std 12.01 vs 10.55 COVID-included, 8.55 vs 8.33 COVID-excluded). While fine-tuning slightly reduces deep tail loss (1% VaR drops from 21.33 to 21.11 COVID-included, and 2.5% VaR drops from 16.97 to 16.41 COVID-excluded), the overall dispersion of tracking error is marginally higher.
2. **VolGAN Baseline Implementation Sensitivity:** The authors noted that an independent reimplementation of VolGAN achieved a tracking error standard deviation of 12.10 (vs 32.98 in Cont & Vuletić 2025) because the reimplementation selected a denser portfolio (5.51 instruments vs 2–3 options in the original paper). This demonstrates that downstream LASSO hedging results are highly sensitive to instrument panel cardinality and regularization tuning, not purely generative model superiority.
3. **Severe Computational Overhead:** Sampling 100 scenarios from a 200-step DDPM diffusion process requires significant GPU latency per rebalance bar, making high-frequency or multi-asset real-time execution intractable without neural network distillation or fast one-step ODE samplers.

## Falsification plan

To falsify the claim that AD-Seq-Vol provides durable superior data-driven hedging over classical and GAN-based baselines, the following pre-declared operational tests must be executed:

1. **Out-of-Sample Extended Window Test (2023–2026 SPX Options):**
   - *Data:* SPX daily option chains from March 1, 2023 through August 31, 2026.
   - *Baseline:* Standard Black-Scholes Delta-Vega hedging and VolGAN.
   - *Decision Rule (`research-defined falsification threshold`):* If AD-Seq-Vol tracking error standard deviation exceeds Delta-Vega tracking error standard deviation by >10%, or if its 1% VaR exceeds Delta-Vega 1% VaR over the full post-2023 period, reject the thesis that generative sequential diffusion maintains superior option tracking out-of-sample.
2. **Execution Friction & Spread Widening Stress Test:**
   - *Protocol:* Re-evaluate the hedging backtest while replacing mid-price execution with full half-spread crossing on option rebalances plus exchange clearing fees ($0.50 per contract).
   - *Decision Rule (`research-defined falsification threshold`):* If the net cumulative hedging loss of AD-Seq-Vol exceeds that of Delta-Vega hedging due to turnover drag across the 5 candidate options, falsify the economic viability of multi-instrument diffusion hedging.
3. **No-Arbitrage Fine-Tuning Efficacy Ablation:**
   - *Protocol:* Compare AD-Seq-Vol and AD-Seq-Vol-FT across 500 bootstrapping episodes.
   - *Decision Rule (`research-defined falsification threshold`):* If a Diebold-Mariano test on tracking error loss differentials fails to reject the null hypothesis of equal tail-loss performance between AD-Seq-Vol and AD-Seq-Vol-FT ($p > 0.05$ on 1% and 2.5% VaR), falsify the claim that enforcing static no-arbitrage constraints adds meaningful economic value to downstream hedging.
4. **Historical Conditioning Ablation (Unconditional Scenario Control):**
   - *Protocol:* Replace the 21-day sequential conditioning tensor with an unconditional diffusion model sampled randomly from the empirical distribution.
   - *Decision Rule (`research-defined falsification threshold`):* If unconditional diffusion matches or beats AD-Seq-Vol tracking error standard deviation within 5%, reject the hypothesis that temporal path conditioning along the filtration drives hedging accuracy.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Primary Source Scope:** The primary paper and repository exclusively evaluate equity index options on the S&P 500 (SPX) traded on the CBOE and recorded via OptionMetrics. The authors do not examine crypto markets. Any port to cryptocurrency options is a research-proposed hypothesis, not proven empirical fact.
- **Porting Mechanics to Crypto (e.g., Deribit BTC / ETH Options):**
  1. *Contract Differences:* Deribit BTC/ETH options are coin-margined (inverse) or cash-settled European options. The underlying hedging instrument is typically a perpetual futures contract rather than a cash index. Delta hedging via perpetuals introduces funding rate risk ($f_t$) and spot-perpetual basis divergence.
  2. *Surface Discretization Grid:* Unlike SPX (which offers dense strikes and daily expiries), crypto option chains exhibit lower liquidity outside monthly expiries and extreme out-of-the-money skew. An $11 \times 9$ grid would require heavy kernel smoothing over sparse, stale bid-ask quotes, creating severe interpolation artifacts.
  3. *Fat Tails and Sudden Volatility Regime Jumps:* Crypto implied volatilities frequently jump 30–50 vol points in hours during liquidations. Standard Gaussian diffusion noise schedules ($g(u)$) may undershoot sudden jump dislocations unless augmented with jump-diffusion or heavy-tailed score processes.
  4. *24/7 Continuous Trading:* SPX options rebalance at a fixed 16:00 ET close. Crypto operates 24/7 without session closes, requiring a continuous or discrete hourly rebalance schedule with dynamic liquidity monitoring.

## Limitations

1. **Underspecified Live Market Fill Model (`source-reported`):** Backtests assume fills at closing mid-prices with zero market impact and half-spread linear penalty. In live option trading, limit orders face adverse selection (fills only when market moves against the quoter), while market orders cross wide spreads and incur exchange fees.
2. **Computational Latency:** 200-step DDPM sampling takes significant compute per episode, making real-time sub-minute hedge adjustments infeasible without model distillation.
3. **Quote Smoothing Dependency:** OptionMetrics quotes are smoothed using a Nadaraya-Watson kernel before diffusion training. The diffusion model learns the distribution of *smoothed* surfaces rather than actual discrete order-book states, potentially masking real-world microstructural noise.
4. **Limited Test Sample Window:** The out-of-sample evaluation comprises 56 rolling episodes between 2018 and 2023; larger cross-sectional panels across multiple underlying assets (e.g., NDX, single-stock equities) remain unvalidated.
5. **No Direct Alpha Capture:** The model is an option hedging and risk-minimization simulator, not a directional alpha or market-timing strategy.

## Implementation status

- Frontmatter status: `not-implemented`.
- This research record represents an external knowledge capture from arXiv preprint `arXiv:2609.13402v1` and repository `yinbinhan/volatility-surface-simulation`.
- Neither AD-Seq-Vol nor the transaction-cost LASSO hedging solver has been implemented in PyBroker, NautilusTrader, paper trading, testnet, or live production environments.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves solely as normalized research material for the quantitative strategy repository.
- Being present in this repository does **not** constitute validation, authorization for implementation, or approval for paper, testnet, or live trading.

## Related Wiki records

- `[[crypto-bitcoin-option-dynamic-hedging-whalley-wilmott-no-trade-band-2026-09-01]]`
- `[[spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]]`
- `[[crypto-convolutional-vae-volatility-surface-completion-anomaly-2026-09-01]]`
- `[[cast-cross-asset-state-space-collaborative-kalman-mpc-drawdown-control-2026-09-16]]`

## Sources

1. **Primary Research Paper:**
   - Authors: Yinbin Han, Jack Yuxiang Zhang, Manuel Torres, Fernando Acero, and Renyuan Xu.
   - Title: *"Diffusion models for dynamic volatility surface generation and data-driven hedging"*.
   - arXiv Preprint: `arXiv:2609.13402v1 [q-fin.CP, cs.LG, q-fin.MF, q-fin.RM, q-fin.TR]`, submitted September 14, 2026.
   - Stable URL: https://arxiv.org/abs/2609.13402
   - Full-Text PDF: https://arxiv.org/pdf/2609.13402v1
   - Full-Text HTML: https://arxiv.org/html/2609.13402v1
   - Canonical DOI: [10.48550/arXiv.2609.13402](https://doi.org/10.48550/arXiv.2609.13402)
2. **Primary Source Code Repository:**
   - GitHub: https://github.com/yinbinhan/volatility-surface-simulation
   - Full Immutable Commit SHA: `9ba265ecbf32979d970b9beab7dfde3585163509`
   - Path Inspection: `README.md`, `arbitrage_3way.py`, `backtest_diffusion.py`, `fine_tune.py`, `hedging.py`, `hedging_backtest_utils.py`, `summarize_hedging_results.py`, `train.py`, `config/config.py`.
3. **Downstream Hedging Methodology Reference:**
   - Authors: Rama Cont and Milena Vuletić.
   - Title: *"Data-driven hedging with generative models"*.
   - Journal: *Annals of Operations Research*, 2025.
   - DOI: [10.1007/s10479-025-06867-3](https://doi.org/10.1007/s10479-025-06867-3)
4. **Adaptive Sequential Diffusion Reference:**
   - Authors: Haoyang Cao, Minshuo Chen, Yinbin Han, and Renyuan Xu.
   - Title: *"Diffusion models for adaptive sequential data generation"*.
   - arXiv Preprint: `arXiv:2606.06007`, 2026.
   - Stable URL: https://arxiv.org/abs/2606.06007
