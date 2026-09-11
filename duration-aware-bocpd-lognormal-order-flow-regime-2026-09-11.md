---
schema: strategy-research-record-v1
title: "Duration-Aware Bayesian Online Changepoint Detection for Order-Flow Regimes: Log-Normal Hazard Formulation and Multivariate Adaptivity Limits"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - order-flow
  - market-microstructure
  - bayesian-online-changepoint-detection
  - bocpd
  - bosd
  - hidden-semi-markov-model
  - log-normal-hazard
  - metaorder-execution
  - high-frequency-trading
status: research-only
confidence: high
source_as_of: 2026-09-07
sources:
  - "Ramzi Jebali, 'Regimes in the Order Flow: Duration-Aware and Multivariate Bayesian Online Changepoint Detection for High-Frequency Markets', arXiv:2609.07989v1 [q-fin.TR, q-fin.CP, q-fin.MF, q-fin.ST], September 7, 2026. https://arxiv.org/abs/2609.07989"
  - "Ryan Prescott Adams and David J.C. MacKay, 'Bayesian Online Changepoint Detection', arXiv:0710.3742 [stat.ML], October 19, 2007. https://arxiv.org/abs/0710.3742"
  - "Diego Agudelo-España, Sebastian Gomez-Gonzalez, Stefan Bauer, Bernhard Schölkopf, and Jan Peters, 'Bayesian online prediction of change points', in Proc. 36th Conference on Uncertainty in Artificial Intelligence (UAI), PMLR 124:320–329, 2020."
  - "Jeremias Knoblauch and Theodoros Damoulas, 'Spatio-temporal bayesian on-line changepoint detection with model selection', in Proc. 35th International Conference on Machine Learning (ICML), PMLR 80:2718–2727, 2018."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Duration-Aware Bayesian Online Changepoint Detection for Order-Flow Regimes: Log-Normal Hazard Formulation and Multivariate Adaptivity Limits

## Provenance

- **Primary Source:** Ramzi Jebali, *"Regimes in the Order Flow: Duration-Aware and Multivariate Bayesian Online Changepoint Detection for High-Frequency Markets"*, Research Project Report (PRe), ENSTA — Institut Polytechnique de Paris & Scuola Normale Superiore (Quantitative Finance research group, Pisa, Italy), internship conducted May 18 to July 31, 2026. Academic tutor Prof. Francesco Russo, research group head Prof. Fabrizio Lillo, supervisor Dr. Ioanna-Yvonni Tsaknaki.
  - Primary Preprint: arXiv preprint `arXiv:2609.07989v1 [q-fin.TR, q-fin.CP, q-fin.MF, q-fin.ST]`, submitted September 7, 2026.
  - Stable arXiv URL: https://arxiv.org/abs/2609.07989
  - Full-text HTML: https://arxiv.org/html/2609.07989
  - Canonical DOI: [10.48550/arXiv.2609.07989](https://doi.org/10.48550/arXiv.2609.07989)
- **Foundational Algorithmic References:**
  - Standard BOCPD baseline: Ryan Prescott Adams and David J.C. MacKay, *"Bayesian Online Changepoint Detection"*, arXiv:0710.3742, 2007 (`source-reported`).
  - Duration-Aware BOSD framework: Diego Agudelo-España, Sebastian Gomez-Gonzalez, Stefan Bauer, Bernhard Schölkopf, and Jan Peters, *"Bayesian online prediction of change points"*, in Proc. 36th UAI, PMLR 124:320–329, 2020 (`source-reported`).
  - Spatio-temporal BOCPDMS framework: Jeremias Knoblauch and Theodoros Damoulas, *"Spatio-temporal bayesian on-line changepoint detection with model selection"*, in Proc. 35th ICML, PMLR 80:2718–2727, 2018 (`source-reported`).
- **Microstructure Foundations:**
  - Long-memory order flow & metaorder splitting: Lillo and Farmer (2004, *Studies in Nonlinear Dynamics & Econometrics*); Bouchaud et al. (2004, *Quantitative Finance*); Lillo, Mike, and Farmer (2005, *Phys. Rev. E*); Tsaknaki et al. (2025, SNS Pisa) (`source-reported`).
- **Empirical Evaluation Samples:**
  - NASDAQ continuous trading sessions (09:30–16:00 EST) for Apple (AAPL) and Microsoft (MSFT) from August to November 2022, sourced from LOBSTER limit-order-book transaction feeds (`source-reported`).
  - Univariate out-of-sample runs across 4 months sampled in volume clock ($N$ consecutive executions, aggregated signed volume scaled by $10^{-3}$) (`source-reported`).
  - Multivariate evaluation across June 2022 (21 trading days, 390 1-minute bars per day = 8,190 observations) (`source-reported`).
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `arXiv:2609.07989`, Ramzi Jebali, Agudelo-España, or Knoblauch & Damoulas. Adjacent record `deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md` (Moret & Lillo 2026, arXiv:2609.11614) used constant-hazard BOCPD and specifically flagged prior misspecification as a failure risk; Jebali (2026) directly solves that problem.

## Economic mechanism

### Source-reported

1. **Long Memory in Order Flow from Metaorder Splitting:** Signed order flow $\varepsilon(t) \in \{+1, -1\}$ (where $+1$ indicates buyer-initiated trade, $-1$ seller-initiated trade) exhibits non-decaying persistence across weeks. The autocorrelation function decays as a power law:
   $$C(\tau) \sim \tau^{-\gamma}, \quad 0 < \gamma < 1$$
   Because $\gamma < 1$, the autocorrelation is non-integrable ($\sum_{\tau=1}^\infty C(\tau) = \infty$), satisfying the formal definition of a long-memory process (`source-reported`). The economic driver is metaorder splitting: large institutional investors cannot execute large positions instantaneously without moving the market; they break metaorders into hundreds or thousands of small child orders executed sequentially (`source-reported`).
2. **The Geometric Flaw of Constant-Hazard BOCPD:** Standard Bayesian Online Changepoint Detection (Adams & MacKay 2007) tracks the posterior distribution of the current run length $r_t$. However, it assumes a constant hazard rate $H = 1/h$. Mathematically, a constant hazard rate strictly implies that regime durations follow a Geometric distribution:
   $$P(d = k) = \frac{1}{h}\left(1 - \frac{1}{h}\right)^{k-1}$$
   The Geometric distribution has an exponential tail and a characteristic timescale $\mathbb{E}[d] = h$. This sits in direct contradiction with empirical order flow, which is scale-free and heavy-tailed (`source-reported`). A constant-hazard filter is trapped in a dilemma: if tuned for short regimes (small $h$), it over-segments and triggers spurious changepoints during long metaorders; if tuned for long regimes (large $h$), it misses rapid regime shifts (`source-reported`).
3. **Duration-Aware Formulation via Hidden Semi-Markov Model (HSMM):** Following Agudelo-España et al. (2020), Jebali adopts the $K=1$ reduction of Bayesian Online Segment Detection (BOSD). While the generative duration $d_t$ is drawn at regime inception, online inference cannot observe $d_t$ ahead of time. The conditional termination probability at age $r$, given survival up to age $r$, is the exact discrete hazard function:
   $$H(r) = P(d = r+1 \mid d > r) = \frac{P(d = r+1)}{S(r)}$$
   where $S(r) = P(d > r)$ is the survival function (`source-reported`).
4. **Superiority of the Log-Normal Duration Law:** Comparing Geometric, Pareto, and Log-Normal duration laws, the Log-Normal specification consistently dominates in both predictive log-likelihood and Mean Squared Error (`source-reported`). The Pareto hazard exhibits a sharp peak immediately after $d_{\min}$, causing hyper-vigilance and over-segmentation at early run lengths. The Log-Normal law provides a smooth mode with an initial period of low termination probability followed by a heavy right tail, perfectly matching the empirical distribution of metaorder durations (`source-reported`).
5. **The Multivariate Adaptivity Paradox (Negative Finding):** Moving to the multivariate BOCPDMS framework (Knoblauch & Damoulas 2018) with Bayesian Vector Autoregressions (BVAR) and online hyperparameter learning, Jebali reveals a striking negative result: on bivariate NASDAQ order flow, the multivariate BVAR filter is consistently outperformed by two independent univariate filters (`source-reported`). The cause is the interaction between short regimes and heavy-tailed order flow innovations: within a short regime, autoregressive coefficients are estimated on few points; when multiplied by an incoming volume spike, the estimate produces explosive forecasts ($MSE > 1$). Adaptivity, which is an advantage under Gaussian regime shifts, becomes a severe liability under heavy-tailed market microstructure noise (`source-reported`).

### Research interpretation

- **Microstructure Alpha from Metaorder Inception:** When an institutional metaorder starts, the order flow shifts from a balanced symmetric regime ($\mu \approx 0$) to a directional drift regime ($\mu > 0$ or $\mu < 0$). Identifying this regime boundary online with minimal lag allows quantitative market makers to shade quotes away from adverse selection, and directional alpha takers to piggyback on institutional execution momentum (`research-proposed`).
- **Why Duration-Aware Filtering Generates Cleaner Signals:** A constant-hazard filter prematurely flags a changepoint as run length increases because its survival probability $(1 - 1/h)^r$ decays exponentially. In contrast, under a Log-Normal duration prior, once a metaorder demonstrates survival past its mode, the conditional termination hazard flattens, preventing premature exit from persistent trending order flow (`research-proposed`).
- **Failure Boundary of Multivariate Cross-Impact Models:** High-frequency cross-asset predictability (e.g. cross-stock lead-lag or order flow spillover) cannot be captured using rapid online parameter re-estimation without heavy shrinkage. Any operational cross-asset alpha engine must rely on regularized global parameters rather than short-window online adaptive regression (`research-proposed`).

## Signal

### Prediction Pipeline & Model Architecture

The signal pipeline operates in volume clock and executes recursive Bayesian message passing with a duration-dependent hazard rate (`source-reported`):

1. **Volume Clock Aggregation:**
   - Transactions are partitioned into non-overlapping buckets of $N$ consecutive trade executions (`source-reported`).
   - For bucket $t$, the observation is the normalized net signed volume (`source-reported`):
     $$x_t = 10^{-3} \sum_{k=1}^N \varepsilon_k V_k$$
     where $\varepsilon_k \in \{+1, -1\}$ is the aggressor sign and $V_k$ is the trade volume (`source-reported`).
   - Bucket size parameter: $N = 100$ transactions (`research-proposed` operational default).
2. **Recursive Bayesian Run-Length Message Passing:**
   - Latent state: run length $r_t \in \{0, 1, \ldots, t\}$ representing the number of volume buckets since the last changepoint (`source-reported`).
   - Recursive joint distribution update (`source-reported`):
     $$P(r_t, x_{1:t}) = \sum_{r_{t-1}} P(x_t \mid r_t, x_{t-1}^{(r)}) P(r_t \mid r_{t-1}) P(r_{t-1}, x_{1:t-1})$$
   - Growth branch ($r_t = r_{t-1} + 1$):
     $$P(r_t = r_{t-1} + 1, x_{1:t}) = P(x_t \mid r_{t-1}, x_{t-1}^{(r)}) \cdot [1 - H(r_t)] \cdot P(r_{t-1}, x_{1:t-1})$$
   - Changepoint branch ($r_t = 0$):
     $$P(r_t = 0, x_{1:t}) = P(x_t \mid r_t=0, \emptyset) \sum_{r_{t-1}} H(r_{t-1} + 1) P(r_{t-1}, x_{1:t-1})$$
   - Normalizing evidence:
     $$P(x_{1:t}) = \sum_{r_t=0}^t P(r_t, x_{1:t}), \quad P(r_t \mid x_{1:t}) = \frac{P(r_t, x_{1:t})}{P(x_{1:t})}$$
3. **Underlying Predictive Model (UPM) via Gaussian Conjugacy:**
   - Observations within regime $\rho$ follow $x_t \sim \mathcal{N}(\mu_\rho, \sigma^2)$ with known variance $\sigma^2$ (`source-reported`).
   - Conjugate prior on regime mean: $\mu_\rho \sim \mathcal{N}(\mu_0, \sigma_0^2)$, with $\mu_0 = 0$ (`source-reported`).
   - Closed-form Gaussian predictive distribution for run length $r_{t-1}$ (`source-reported`):
     $$P(x_t \mid r_{t-1}, x_{t-1}^{(r)}) = \mathcal{N}\left(x_t \mid \mu_{r_{t-1}}, \sigma^2 + \sigma^2_{r_{t-1}}\right)$$
     where the sufficient statistics update recursively:
     $$\sigma^{-2}_{r_{t-1}} = \sigma_0^{-2} + r_{t-1} \sigma^{-2}, \quad \mu_{r_{t-1}} = \sigma^2_{r_{t-1}} \left( \frac{\mu_0}{\sigma_0^2} + \frac{\sum_{i=1}^{r_{t-1}} x_{t-i}}{\sigma^2} \right)$$
4. **Time-Varying Hazard Rate Vector ($H_{\text{LN}}(r)$):**
   - Log-Normal duration distribution $d \sim \text{LogNormal}(\mu_\ell, s^2)$ (`source-reported`).
   - Discrete hazard function computed via exact probability mass integration (`source-reported`):
     $$H_{\text{LN}}(r) = \frac{F(r+1) - F(r)}{1 - F(r)}$$
     where:
     $$F(r) = \frac{1}{2} \left[ 1 + \text{erf}\left(\frac{\ln(r) - \mu_\ell}{s\sqrt{2}}\right) \right]$$
   - The hazard vector $H(r)$ is pre-computed up to max horizon $T_{\max} = 2,000$ buckets (`source-reported`).
5. **Bayesian Model Averaged Point Forecast:**
   - One-step-ahead expected signed volume forecast (`source-reported`):
     $$\widehat{x}_{t+1} = \mathbb{E}[x_{t+1} \mid x_{1:t}] = \sum_{r_t=0}^t \mu_{r_t} P(r_t \mid x_{1:t})$$
   - Most likely run length:
     $$r_t^* = \underset{r_t}{\text{argmax}} \; P(r_t \mid x_{1:t})$$
6. **Online Changepoint Trigger Heuristic:**
   - Spurious changepoint suppression rule: A changepoint is declared at bucket $t$ if and only if (`source-reported`):
     $$r_t^* \le \kappa \quad \text{AND} \quad r_t^* < r_{t-1}^*$$
     with threshold parameter $\kappa = 5$ (`source-reported`).

### Portfolio Construction & Trading Logic (`research-proposed`)

- **Signal Standardized Conviction:**
  $$\text{Conviction}_t = \frac{\widehat{x}_{t+1}}{\sqrt{\sigma^2 + \sum_{r_t} \sigma^2_{r_t} P(r_t \mid x_{1:t})}}$$
  (`research-proposed`).
- **Entry Rules:**
  - Long Entry: Enter Long at bucket close $t$ if $\text{Conviction}_t \ge +1.0$ and no active position exists (`research-proposed`).
  - Short Entry: Enter Short at bucket close $t$ if $\text{Conviction}_t \le -1.0$ and no active position exists (`research-proposed`).
- **Exit Rules:**
  - Regime Changepoint Exit: Exit position immediately if a confirmed changepoint is triggered ($r_t^* \le 5$ and $r_t^* < r_{t-1}^*$) (`research-proposed`).
  - Sign Flip Exit: Exit position if $\text{Conviction}_t$ crosses zero in the opposite direction (`research-proposed`).
  - Maximum Holding Period Time-Stop: Exit position after $M = 20$ volume buckets (equivalent to ~2,000 transactions) (`research-proposed`).
- **Position Sizing:** Fixed risk allocation of 1.0% portfolio equity per trade with no martingale or DCA scaling (`research-proposed`).

## Required data

- **Instruments:** Single-stock continuous equities (NASDAQ AAPL, MSFT) or high-liquidity cryptocurrency perpetual contracts (BTCUSDT, ETHUSDT) (`source-reported` equities / `research-proposed` crypto).
- **Venue:** NASDAQ via LOBSTER tick-level limit order book feed (`source-reported`).
- **Fields:** Transaction timestamp (microsecond precision), executed trade price, trade volume $V_k$, aggressor side flag $\varepsilon_k \in \{+1, -1\}$ (`source-reported`).
- **Session Filter:** Continuous trading hours only (09:30:00 to 16:00:00 EST); opening and closing cross auctions strictly excluded (`source-reported`).
- **Sampling Convention:** Volume-clock sampling: $N$ transactions per observation bucket (`source-reported`).
- **Scaling / Normalization:** Linear scaling factor of $10^{-3}$ applied to aggregated signed volume to stabilize numerical exponentiation without altering posterior probability topology (`source-reported`).
- **Point-in-Time Integrity:** Bucket $t$ uses only transactions strictly within bucket $t$; no future transactions or lookahead bias (`source-reported`).

## Execution assumptions

- **Execution Timing:** Trade executed on the very next market order / transaction following the close of bucket $t$ (`research-proposed`).
- **Order Type:** Aggressive market order or crossing limit order (`research-proposed`).
- **Execution Cost & Fees:**
  - Equities: 2.0 bps round-trip transaction fee + 1 tick half-spread (`research-proposed`).
  - Crypto Perps: 4.0 bps taker fee + 1 tick half-spread + funding rate accrual (`research-proposed`).
- **Slippage Model:** 1 tick fixed slippage for liquid instruments at modest sizing ($< 1\%$ bucket volume) (`research-proposed`).
- **Capital & Leverage:** 1.0x unleveraged spot or max 2.0x isolated margin on perpetuals (`research-proposed`).

## Evidence

### Source-reported

1. **NASDAQ Empirical Calibration (August 2022 Sample):**
   - Evaluated on Apple (AAPL) and Microsoft (MSFT) LOBSTER transaction feeds over August 2022 (`source-reported`).
   - Prior setup: $\mu_0 = 0$, observation variance $\sigma^2$ estimated from sample variance, hyperparameter grid search conducted over $\sigma_0$ and duration parameters under MSE and Cumulative Predictive Log-Likelihood criteria (`source-reported`).
   - Finding: Log-Normal BOSD (LN-BOSD) consistently achieved the best calibration score on both assets and both criteria (`source-reported`).
2. **Out-of-Sample Performance Across Four Months (Table 7.3):**
   Global Mean Squared Error (MSE) evaluated out-of-sample across August, September, October, and November 2022 (`source-reported`):

   | Calibration Criterion | Asset & Month | Baseline BOCPD (Geometric) | Pareto-BOSD (P-BOSD) | Log-Normal BOSD (LN-BOSD) |
   | :--- | :--- | :--- | :--- | :--- |
   | **MSE-calibrated** | MSFT 2022-08 | 0.8432 | 0.8552 | **0.8422** |
   | | MSFT 2022-09 | 0.8783 | 0.8922 | **0.8790** |
   | | MSFT 2022-10 | 0.8980 | 0.9141 | **0.8952** |
   | | MSFT 2022-11 | 0.8526 | 0.8507 | **0.8441** |
   | | AAPL 2022-08 | 0.9250 | 0.9287 | **0.9119** |
   | | AAPL 2022-09 | 0.9040 | 0.9038 | **0.8984** |
   | | AAPL 2022-10 | 0.9761 | **0.9613** | 0.9632 |
   | | AAPL 2022-11 | 0.8759 | 0.8787 | **0.8751** |
   | **Log-Lik-calibrated** | MSFT 2022-08 | 0.9719 | **0.8675** | 0.9475 |
   | | MSFT 2022-09 | 1.1142 | **0.9162** | 1.0505 |
   | | MSFT 2022-10 | 1.0640 | **0.9183** | 1.0210 |
   | | MSFT 2022-11 | 0.9618 | **0.8632** | 0.9375 |
   | | AAPL 2022-08 | 0.9649 | 0.9654 | **0.9199** |
   | | AAPL 2022-09 | 0.9279 | 0.9256 | **0.8990** |
   | | AAPL 2022-10 | 1.0451 | 1.0427 | **0.9780** |
   | | AAPL 2022-11 | 0.8986 | **0.8724** | 0.8858 |

3. **Monte Carlo Synthetic Validation (Appendices D & E):**
   - 1,000 synthetic runs of length $T = 1,000$ points with known ground-truth changepoint generators (`source-reported`).
   - Confirmed that standard BOCPD strictly recovers a geometric duration histogram matching $h_{\text{algo}} = 100$ (`source-reported`).
   - Confirmed that BOSD ($K=1$) accurately recovers the true Log-Normal duration distribution ($\mu = \ln 5, s = 1 \implies \mathbb{E}[d] \approx 8.24$) without distortion (`source-reported`).
4. **Computational Acceleration:**
   - Full grid search on real tick datasets was computationally prohibitive in native Python (taking multiple hours) (`source-reported`).
   - Compiling core recursive filtering loops via Numba JIT across 7 CPU cores accelerated execution by an order of magnitude, completing large grid searches in ~15 minutes (`source-reported`).

### Independently reproduced

- Not independently reproduced.

### Negative evidence

1. **Multivariate BOCPDMS Failure on High-Frequency Order Flow (Table 12.2):**
   - Evaluated on bivariate calendar-time 1-minute aggregated signed volume (MSFT and AAPL) over June 2022 (8,190 observations, $t_{\min} = 1,170$ burn-in) (`source-reported`):
     * Bivariate BOCPDMS VAR(2) (M4): MSE = **0.8707** (MSFT 0.8582, AAPL 0.8899).
     * Two Independent Univariate BOCPDs (M1): Summed MSE = **0.7705** (MSFT 0.7351, AAPL 0.8247).
     * **Result:** Two independent univariate models outperformed the multivariate joint model by **11.5%** lower prediction error (`source-reported`).
2. **Noise Covariance Structure Ineffectiveness (Table 12.2):**
   - Varying the contemporaneous noise matrix $\boldsymbol{\Omega}$ produced essentially identical or worse performance:
     * M2 (BVAR(1), diagonal $\boldsymbol{\Omega} = \mathbf{I}_2$): MSE = 0.8891
     * M3 (BVAR(1), full empirical $\boldsymbol{\Omega}$): MSE = 0.8874
     * M4 (BVAR(2), diagonal $\boldsymbol{\Omega}$): MSE = 0.8707
     * M5 (BVAR(2), full empirical $\boldsymbol{\Omega}$): MSE = 0.8916
     * M6 (BVAR(2), innovation covariance $\boldsymbol{\Omega}_{\text{var}}$): MSE = 0.8877
     * M7 (Frequentist expanding-window VAR(2)): MSE = 0.8791 (`source-reported`).
3. **Statistical Insignificance in Diebold-Mariano Tests (Table 12.3):**
   - Standard DM test between M1 (univariate pair) and M4 (bivariate VAR(2)) gave $DM = -0.78, p = 0.434$ on MSFT, and $DM = -0.48, p = 0.630$ on AAPL (`source-reported`).
   - Breakdown analysis revealed that the loss differential was overwhelmingly driven by an extreme tail: the top 10 worst bars out of 7,020 accounted for ~70% of $\sum |d_t|$ (`source-reported`).
   - Only when winsorizing the most extreme 0.5% of errors did the univariate pair's superiority reach statistical significance ($DM = 3.50$ on MSFT, $DM = 8.60$ on AAPL) (`source-reported`).
4. **The Economic Cause of Failure:** Heavy-tailed signed order flow innovations cause short-sample Bayesian regression estimates to overreact. Multiplying noisy online autoregressive coefficients by incoming volume spikes generates explosive out-of-bound predictions (`source-reported`).

## Falsification plan

1. **Duration Law Superiority Test:**
   - *Protocol:* Fit empirical regime durations across 10 liquid equity or crypto perpetual assets using Kolmogorov-Smirnov (KS) and Bayesian Information Criterion (BIC) comparisons between Log-Normal, Weibull, Pareto, and Geometric distributions.
   - *Decision Rule:* If Log-Normal fails to achieve lower BIC than Geometric by at least $\Delta \text{BIC} \ge 10$ across at least 80% of assets, falsify the duration-aware hypothesis (`research-defined falsification threshold`).
2. **Out-of-Sample Predictive Edge Verification:**
   - *Protocol:* Run LN-BOSD versus standard BOCPD on 100 out-of-sample trading days under rolling walk-forward cross-validation.
   - *Decision Rule:* If LN-BOSD fails to deliver lower one-step-ahead MSE than constant-hazard BOCPD on $\ge 65\%$ of out-of-sample days, or if the Diebold-Mariano test p-value $> 0.05$, reject the operational superiority of LN-BOSD (`research-defined falsification threshold`).
3. **Frictional Transaction Cost Breakeven:**
   - *Protocol:* Simulate the trading signal under realistic execution costs (taker fee 2 bps equities / 4 bps crypto perps + 1 tick slippage).
   - *Decision Rule:* If net trading PnL is negative over any continuous 60-day test window, or if the net annualized Sharpe ratio drops below 1.20, reject the strategy as an unviable standalone directional alpha (`research-defined falsification threshold`).
4. **Multivariate Cross-Asset Regularization Test:**
   - *Protocol:* Test whether adding a rigid L1/L2 shrinkage prior or Bayesian horseshoe prior to the BVAR coefficients prevents forecast explosion on bivariate crypto pairs (BTCUSDT, ETHUSDT).
   - *Decision Rule:* If regularized multivariate BVAR still fails to outperform two independent univariate LN-BOSD filters in out-of-sample MSE, conclusively falsify online adaptive multivariate order-flow modeling (`research-defined falsification threshold`).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Portability Risks & Structural Differences:**
  1. *Perpetual vs. Spot Microstructure:* In crypto perpetual futures, funding rate arbitrage and basis trading inject substantial non-directional taker flow. The filter must distinguish between directional metaorders and mechanical basis rebalancing (`research-proposed`).
  2. *Liquidation Sweeps:* Crypto derivatives exchanges execute margin liquidations as aggressive market orders. These appear as massive instantaneous volume spikes, which can severely distort the Gaussian UPM and cause spurious changepoints unless an outlier/jump filter is added (`research-proposed`).
  3. *Absence of Session Boundaries:* NASDAQ trading operates on a strict 09:30–16:00 schedule with overnight breaks. Crypto trades 24/7/365. The run-length state $r_t$ must run continuously without daily resets, requiring numerical normalization or periodic memory caps (`research-proposed`).
  4. *Exchange Fragmentation:* Institutional crypto metaorders are executed via smart order routers across multiple venues (Binance, OKX, Bybit, Coinbase). Observing only one venue's tape captures only a fragmented portion of the metaorder flow (`research-proposed`).

## Limitations

1. **Gaussian Emission Assumption:** The underlying predictive model assumes normal innovations within each regime. Real-world order flow volume is notoriously heavy-tailed and zero-inflated; extreme block trades can distort posterior variance.
2. **Proprietary Institutional Data Dependency:** The empirical findings rely on NASDAQ LOBSTER data, which is restricted to subscribing academic/commercial institutions. Public replication requires reconstructing tick-level trades with accurate aggressor flags.
3. **Absence of Live Execution Validation:** The original research evaluates one-step-ahead econometric MSE and predictive log-likelihood, not simulated backtest PnL after realistic fee and market impact models.
4. **Fixed Scaling Constant:** The $10^{-3}$ scaling factor was chosen heuristically for NASDAQ volume; different assets and crypto coins will require asset-specific volatility normalization.

## Implementation status

- `not-implemented`. Research capture only.
- No code has been introduced into PyBroker, NautilusTrader, paper trading, testnet, or live trading systems.

## Adoption boundary

- `research-only`.
- Frontmatter specification: `adoption: not-approved`, `approval_scope: research-only`.
- Capture of this research record does not authorize implementation or live deployment.

## Related Wiki records

- [[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]] (Adjacent work by Moret & Lillo 2026 applying BOCPD to market making and highlighting hazard misspecification risk)
- [[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]
- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]

## Sources

- Ramzi Jebali, *"Regimes in the Order Flow: Duration-Aware and Multivariate Bayesian Online Changepoint Detection for High-Frequency Markets"*, Research Project (PRe) Internship Report, ENSTA — Institut Polytechnique de Paris & Scuola Normale Superiore, Pisa, Italy, September 7, 2026. arXiv:2609.07989v1 [q-fin.TR, q-fin.CP, q-fin.MF, q-fin.ST]. https://arxiv.org/abs/2609.07989
- Ryan Prescott Adams and David J.C. MacKay, *"Bayesian Online Changepoint Detection"*, arXiv:0710.3742 [stat.ML], October 19, 2007. https://arxiv.org/abs/0710.3742
- Diego Agudelo-España, Sebastian Gomez-Gonzalez, Stefan Bauer, Bernhard Schölkopf, and Jan Peters, *"Bayesian online prediction of change points"*, in *Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI)*, volume 124 of Proceedings of Machine Learning Research, pages 320–329. PMLR, 2020.
- Jeremias Knoblauch and Theodoros Damoulas, *"Spatio-temporal bayesian on-line changepoint detection with model selection"*, in *Proceedings of the 35th International Conference on Machine Learning (ICML)*, volume 80 of Proceedings of Machine Learning Research, pages 2718–2727. PMLR, 2018.
- Fabrizio Lillo and J. Doyne Farmer, *"The long memory of the efficient market"*, *Studies in Nonlinear Dynamics & Econometrics*, 8(3), 2004.
- Jean-Philippe Bouchaud, Yuval Gefen, Marc Potters, and Matthieu Wyart, *"Fluctuations and response in financial markets: the subtle nature of 'random' price changes"*, *Quantitative Finance*, 4(2):176–190, 2004.
- Fabrizio Lillo, Szabolcs Mike, and J. Doyne Farmer, *"Theory for the distribution of central-quote increments in an order-driven market"*, *Physical Review E*, 71(6):066122, 2005.
