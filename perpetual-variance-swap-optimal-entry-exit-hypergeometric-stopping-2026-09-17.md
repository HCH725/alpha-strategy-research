---
schema: strategy-research-record-v1
title: Perpetual Variance Swap Optimal Entry and Exit via Confluent Hypergeometric Optimal Stopping
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - variance-swap
  - optimal-stopping
  - variance-risk-premium
  - closed-form
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://arxiv.org/abs/2609.19102
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Perpetual Variance Swap Optimal Entry and Exit via Confluent Hypergeometric Optimal Stopping

## Provenance

- **Primary Source:** Jun Maeda (Warwick), *"Optimal entry and exit for variance swaps: closed-form rules for the perpetual contract"*, arXiv preprint `arXiv:2609.19102v1 [q-fin.MF]`, submitted September 16, 2026.
- **Canonical Identifier / Stable URL:** https://arxiv.org/abs/2609.19102
- **Canonical DOI:** [10.48550/arXiv.2609.19102](https://doi.org/10.48550/arXiv.2609.19102)
- **Full-Text HTML Source:** https://arxiv.org/html/2609.19102v1
- **Full-Text PDF Source:** https://arxiv.org/pdf/2609.19102v1
- **Source Verification:** The primary source preprint full text and analytical derivation were directly retrieved and audited. All equations, theorems, boundary conditions, parameter calibrations, and tables cited in this record trace directly to Sections 1–8, Appendices A–B, and Tables 1–4 of `arXiv:2609.19102v1`.
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.19102`, Jun Maeda, or closed-form confluent hypergeometric optimal stopping boundaries for perpetual variance swaps. Adjacent variance risk premium captures (`cross-asset-reconfiguration-premium-subdominant-eigenspace-vrp-2026-09-02.md`, `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12.md`, `equity-index-dispersion-correlation-risk-premium-spread-friction-falsification-2026-09-13.md`) investigate co-movement eigenspaces, synthetic crypto log-contract estimator fragility, or index dispersion baskets; none formulate or solve the entry and exit stopping times for perpetual variance swaps.

## Economic mechanism

### Source-reported

Under the risk-neutral pricing measure $\mathbb{Q}$, the mark-to-market of a variance swap is a martingale, so optimal early unwinding or market timing is degenerate (has zero expected excess reward). Under the physical measure $\mathbb{P}$, an empirical variance risk premium (VRP) exists: variance swap strikes persistently sit above forecast realized variance ($\theta_{\mathbb{Q}} > \theta_{\mathbb{P}}$, equivalently $\lambda := \kappa_{\mathbb{Q}} - \kappa_{\mathbb{P}} < 0$). This premium provides a positive drift to a short variance position ($\varepsilon = -1$).

However, entering and exiting the position are mathematically asymmetric:
1. **Unwind decision:** A short variance trader who holds a perpetual contract continuously accrues variance while paying a margin/carrying charge $c_m$ per unit time, facing transaction spreads upon unwind ($\bar{s}$). An optimal exit threshold $b^*$ exists only when the carrying charge exceeds a strict lower bound $c_m > c_m^* := \delta(\bar{s} + \inf_v D)$; otherwise, a perpetual position with positive carry and no expiry would be held indefinitely. Once $c_m > c_m^*$, the position is unwound when instantaneous variance collapses into the lower tail ($v_t \leq b^*$), because remaining expected premium cannot overcome ongoing carry costs.
2. **Entry decision:** A flat trader who is out of the market pays no carry and accrues no variance ($c_0 = 0$). Because waiting costs nothing in cash and the option to wait is valuable, the optimal entry threshold $d^*$ sits deep in the upper tail of the physical distribution (around the 95th percentile). An operational entry rule that triggers at more accessible percentiles requires modeling an opportunity cost of idle capital ($c_0 > 0$).

### Research interpretation

The core falsifiable hypothesis is **volatility-spike exhaustion with state-dependent carry attrition**:
- When spot variance spikes to extreme levels ($v_t \geq d^*$), implied variance swap rates reflect heightened panic and premium over future physical variance, creating an optimal entry window to sell variance.
- As volatility normalizes toward its physical long-run mean $\theta_{\mathbb{P}}$, the short position harvests the variance difference.
- However, as variance drops into low-volatility regimes ($v_t \leq b^*$), the incremental premium harvest approaches zero while fixed financing/margin carrying charges ($c_m$) continue to accrue, making it mathematically optimal to take profit and flatten rather than bleed carry during extended compression regimes.

## Signal

The strategy operates on instantaneous variance $v_t$ (or its duration-weighted observable proxy, the perpetual fair rate $K(v_t)$):

### 1. Underlying Diffusion and State Variable (`source-reported`)
Instantaneous variance $v_t$ is modeled as a CIR process under physical measure $\mathbb{P}$:
$$dv_t = \kappa_{\mathbb{P}}(\theta_{\mathbb{P}} - v_t) dt + \gamma \sqrt{v_t} dW^{\mathbb{P}}_t$$
and under pricing measure $\mathbb{Q}$:
$$dv_t = \kappa_{\mathbb{Q}}(\theta_{\mathbb{Q}} - v_t) dt + \gamma \sqrt{v_t} dW^{\mathbb{Q}}_t$$
linked by the affine market price of variance risk preserving the CIR form:
$$\kappa_{\mathbb{P}}\theta_{\mathbb{P}} = \kappa_{\mathbb{Q}}\theta_{\mathbb{Q}}, \qquad \lambda := \kappa_{\mathbb{Q}} - \kappa_{\mathbb{P}} < 0$$
with Feller condition $2\kappa_{\mathbb{P}}\theta_{\mathbb{P}} > \gamma^2$ holding under both measures.

### 2. Contract Specification (`source-reported`)
A perpetual, continuously settled variance swap paying floating realized variance against fixed strike $K$: $(v_t - K)dt$ per unit notional until independent exponential termination time $T_\delta$ with rate $\delta > 0$ (expected life $1/\delta$).
The perpetual fair rate at level $v$ is:
$$K(v) = \theta_{\mathbb{Q}} + (v - \theta_{\mathbb{Q}}) \frac{\delta}{\delta + \kappa_{\mathbb{Q}}}$$

### 3. Exit (Unwind) Rule (`source-reported`)
For a short variance swap ($\varepsilon = -1$), the reduced reward is affine:
$$\tilde{h}(v) = \alpha + \beta v$$
$$\beta = -\frac{\varepsilon \lambda}{(\delta + \kappa_{\mathbb{Q}})(\delta + \kappa_{\mathbb{P}})} = \frac{\lambda}{(\delta + \kappa_{\mathbb{Q}})(\delta + \kappa_{\mathbb{P}})} < 0$$
$$\alpha = -\left[\frac{\theta_{\mathbb{Q}}-\theta_{\mathbb{P}}}{\delta} - \frac{\theta_{\mathbb{Q}}}{\delta+\kappa_{\mathbb{Q}}} + \frac{\theta_{\mathbb{P}}}{\delta+\kappa_{\mathbb{P}}}\right] - \bar{s} + \frac{c_m}{\delta}$$
The continuation region is $(b^*, \infty)$ and the exercise region is $(0, b^*]$.
The unwind threshold $b^*$ is the unique root on $(0, \infty)$ of the smooth-pasting equation (Theorem 6.11(ii)):
$$\beta G(b^*) - \tilde{h}(b^*) G'(b^*) = 0$$
where $G(v) = \mathcal{U}(\mathsf{a}, \nu; \varsigma v)$ is the Tricomi confluent hypergeometric function with:
$$\mathsf{a} = \frac{\delta}{\kappa_{\mathbb{P}}}, \qquad \nu = \frac{2\kappa_{\mathbb{P}}\theta_{\mathbb{P}}}{\gamma^2}, \qquad \varsigma = \frac{2\kappa_{\mathbb{P}}}{\gamma^2}$$
- **Exit Trigger:** Close short position when $v_t \leq b^*$ (or perpetual fair rate $\sqrt{K(v_t)} \leq \sqrt{K(b^*)}$).

### 4. Entry Rule (`source-reported`)
The entry region is $[d^*, \infty)$ with $d^* > b^*$.
The entry obstacle $\rho(v)$ for $v > b^*$ is:
$$\rho(v) = \frac{\tilde{h}(b^*)}{G(b^*)} G(v) - \tilde{h}(v) - (\bar{s} + \bar{s}_e) + \frac{c_0}{\delta}$$
where $k = \bar{s} + \bar{s}_e$ is round-trip tear-up concession and $c_0 \ge 0$ is opportunity cost of idle capital.
The entry threshold $d^*$ is the unique root of the smooth-pasting equation (Theorem 7.8):
$$\rho'(d^*) F(d^*) - \rho(d^*) F'(d^*) = 0$$
$$\rho'(v) = \frac{\tilde{h}(b^*)}{G(b^*)} G'(v) - \beta$$
where $F(v) = M(\mathsf{a}, \nu; \varsigma v)$ is the Kummer confluent hypergeometric function.
- **Entry Trigger:** Open short position when $v_t \geq d^*$ (or perpetual fair rate $\sqrt{K(v_t)} \geq \sqrt{K(d^*)}$).

### 5. Operational Implementation Rules (`research-proposed`)
- Sampling frequency: Continuous-time $v_t$ is approximated using discrete bar observations (e.g., 5-minute or 1-hour bar closes) (`research-proposed`).
- Instantaneous variance filter: In practice, $v_t$ must be filtered from high-frequency returns or near-term listed option strips (e.g., 30-day implied variance or Deribit DVOL proxy) via extended Kalman filter or particle filter (`research-proposed`).
- Position sizing: 100% target vega notional allocated when entering at $v_t \geq d^*$; 0% when unwound at $v_t \leq b^*$ (`research-proposed`).

## Required data

- **Asset Class / Instrument:** Variance swaps or variance futures (e.g., Cboe S&P 500 Variance Futures `VA`, or synthetic replication via liquid options strip) (`source-reported`).
- **Variance Proxy / Inputs:**
  - Forward-looking option implied volatility surface (to calibrate $\mathbb{Q}$-parameters $\kappa_{\mathbb{Q}}, \theta_{\mathbb{Q}}$ and fair strike $K$) (`source-reported`).
  - High-frequency underlying price series $S_t$ (to measure realized variance $\sigma_R^2$ and estimate $\mathbb{P}$-parameters $\kappa_{\mathbb{P}}, \theta_{\mathbb{P}}, \gamma$) (`source-reported`).
- **Carrying and Financing Parameters:**
  - Carrying charge $c_m$ (cost of collateral, initial margin financing, exchange maintenance fees) (`source-reported`).
  - Opportunity cost of capital $c_0$ (hurdle rate or risk-free yield forgone while waiting flat) (`source-reported`).
  - Execution concessions / half-spreads $\bar{s}_e, \bar{s}$ (`source-reported`).
- **Timestamp & Alignment (`research-proposed`):** Synchronized UTC bar timestamps; zero look-ahead bias between variance estimation and trade submission.
- **Missing Data Handling (`research-proposed`):** Trading halts or missing option quotes hold previous state; no trade entry permitted during wide-spread data anomalies.

## Execution assumptions

- **Execution Mode (`source-reported`):** Continuous entry and tear-up unwinding against market counterparty or screen variance futures contract.
- **Transaction Costs (`source-reported`):**
  - Unwind tear-up concession: $\bar{s} = 0.002$ in variance units per year (approx. 0.5 volatility points at typical levels).
  - Entry concession: $\bar{s}_e = 0.002$.
  - Carrying charge: $c_m = 0.004$ (40 bps/year) to $0.012$ (120 bps/year).
- **Execution Timing (`research-proposed`):** Next-bar open fill or TWAP over subsequent 5-minute window following threshold breach to prevent instant fill look-ahead.
- **Slippage & Market Impact (`research-proposed`):** Additional 5 bps variance-point adverse execution buffer during high-volatility spikes ($v_t \ge d^*$).
- **Margin & Leverage (`research-proposed`):** Unleveraged or 1x vega-notional exposure; capital requirement set to cover 3-standard-deviation variance shock above $d^*$.

## Evidence

### Source-reported

All analytical and numerical results below are directly reported by Jun Maeda (`arXiv:2609.19102v1`, Sections 7.2, 7.3, 8.1, 8.2, and Tables 2–3):

1. **Existence Condition for Short Unwind Threshold (Proposition 7.1):**
   - For short variance ($\varepsilon = -1$), the exercise region is empty (position held indefinitely) unless carrying charge satisfies $c_m > c_m^* := \delta(\bar{s} + \inf_v D)$.
   - At base parameters ($\kappa_{\mathbb{Q}}=2.0, \theta_{\mathbb{Q}}=0.045, \gamma=0.26, \lambda=-0.15, \delta=0.5, \bar{s}=0.002$), $c_m^* = 0.00304$ (30.4 bps/yr), reproduced by numerical solver within 0.1 bp.
   - At $c_m = 0.0035$, exit rate is 19.7% vol; at $c_m = 0.008$, exit rate rises to 23.6% vol.

2. **Re-calibrated Window Parameters (Section 8.2):**
   - Slowing pricing reversion: $\kappa_{\mathbb{Q}} = 1.0, \theta_{\mathbb{Q}} = 0.045$ (21.2% vol), $\gamma = 0.20, \lambda = -0.60 \implies \kappa_{\mathbb{P}} = 1.60, \theta_{\mathbb{P}} = 0.02812$ (16.8% vol), $\nu = 2.25$, variance risk premium $= 3.07$ vol points.
   - Admissible carry charge window: $c_m \in [100, 210]$ bps.
   - At $c_m = 120$ bps and $c_0 = 0$:
     - Short entry threshold $d^*$: perpetual rate **22.62%** (corresponding to variance $d^* = 0.12161$, 94.8th percentile of stationary distribution under $\mathbb{P}$).
     - Short unwind threshold $b^*$: perpetual rate **18.20%** (12.4th percentile of stationary distribution under $\mathbb{P}$).
     - Simulated mean time from stationarity to entry: **4.0 years**.
     - Simulated mean time from entry to unwind: **2.3 years**.

3. **Lowest Entry Percentile Across Expected Contract Lives (Table 2, Section 8.2):**
   - Expected life $1/\delta = 1$ yr: $c_m = 135$ bp, exit pctile 6.6%, entry pctile 94.7% (entry/exit rate 27.03% / 20.47%).
   - Expected life $1/\delta = 2$ yr: $c_m = 135$ bp, exit pctile 6.9%, entry pctile 95.4% (entry/exit rate 25.66% / 21.63%).
   - Expected life $1/\delta = 4$ yr: $c_m = 135$ bp, exit pctile 6.3%, entry pctile 96.6% (entry/exit rate 24.74% / 22.33%).
   - Expected life $1/\delta = 8$ yr: $c_m = 135$ bp, exit pctile 5.5%, entry pctile 97.8% (entry/exit rate 24.14% / 22.73%).
   - Expected life $1/\delta = 16$ yr: $c_m = 145$ bp, exit pctile 13.9%, entry pctile 98.9% (entry/exit rate 23.79% / 23.00%).
   - Expected life $1/\delta = 32$ yr: $c_m = 145$ bp, exit pctile 13.8%, entry pctile 99.4% (entry/exit rate 23.54% / 23.10%).
   - *Key finding:* Longer contract life monotonically increases the entry percentile (makes entry rarer) and compresses the entry-exit rate spread from 6.5 vol points (1-yr) to under 0.5 vol points (32-yr).

4. **Sensitivity to Opportunity Cost of Idle Capital $c_0$ (Table 3, Section 7.3):**
   - At $c_m = 120$ bps:
     - $c_0 = 0$ bp/yr: entry rate 22.62% (94.8th percentile).
     - $c_0 = 25$ bp/yr: entry rate 21.17% (83.1th percentile).
     - $c_0 = 50$ bp/yr: entry rate 19.81% (58.0th percentile).
     - $c_0 \ge 100$ bp/yr: entry rate 17.32% (0.0th percentile, immediate entry).

### Independently reproduced

Not independently reproduced. All figures and performance metrics represent third-party analytical and numerical findings reported by Jun Maeda (`arXiv:2609.19102v1`).

### Negative evidence

- **Extreme Holding Inactivity at $c_0 = 0$:** In the absence of an explicit opportunity cost of idle capital ($c_0=0$), the optimal entry threshold remains pinned above the 94th percentile across all tested tenors (1 to 32 years). An unpenalized trader waits years (mean 4.0 years) for a rare volatility blow-up before entering.
- **Carrying Cost Degeneracy Window:** If carrying cost $c_m \le c_m^*$, the exit threshold is undefined ($b^* = 0$), meaning the trader never unwinds until contract termination; conversely, if $c_m$ exceeds the upper boundary of the admissible window (e.g. $>210$ bps in Section 8.2), the entry region empties because carrying friction overwhelms expected VRP harvest.
- **VRP Term Structure Disappearance:** As noted by Maeda citing Dew-Becker et al. (2017), empirical equity variance risk premia are concentrated at 1- to 2-month horizons and decay toward zero beyond 3 months. A perpetual swap that weights all horizons equally risks pricing a long-end premium that does not exist in real markets.

## Falsification plan

1. **Root-Finding Robustness and Boundary Check (`research-proposed`):**
   - Solve smooth-pasting equations (37) and (49) across perturbed parameter grids ($\kappa_{\mathbb{P}} \pm 20\%$, $\gamma \pm 20\%$, $\lambda \pm 30\%$).
   - *Failure Rule (`research-defined falsification threshold`):* If the numerical bisection solver fails to converge to a unique positive root $d^* > b^*$ across $>5\%$ of realistic parameter combinations, the closed-form one-sided boundary theorem is structurally fragile.

2. **Empirical PnL vs. Static Holding Benchmark (`research-proposed`):**
   - Implement the $(d^*, b^*)$ entry-exit stopping rule on historical daily S&P 500 variance swap proxies (2000–2026) using Cboe Variance Futures / strip data against two baselines: (a) continuous passive short variance, and (b) naive fixed-volatility entry/exit (e.g. enter above 25%, exit below 15%).
   - *Failure Rule (`research-defined falsification threshold`):* If the optimal-stopping rule achieves an annualized net Sharpe ratio less than or equal to the passive short baseline, or if net returns after 120 bps carrying cost and 20 bps half-spread turn negative, the timing hypothesis is falsified.

3. **Carrying Cost Sensitivity Stress Test (`research-proposed`):**
   - Vary simulated carrying charges $c_m$ from 50 bps to 300 bps and idle capital hurdle $c_0$ from 0 to 100 bps.
   - *Failure Rule (`research-defined falsification threshold`):* If entry/exit threshold stability collapses (e.g. entry percentile swings $>40$ percentile points under a 10 bps shift in $c_m$), the strategy is deemed un-tradable due to parameter hypersensitivity.

4. **Regime and Tail-Risk Drawdown Test (`research-proposed`):**
   - Evaluate maximum drawdown during severe volatility spikes (e.g., March 2020 COVID shock, 2008 GFC). Because the continuation region for a short is $(b^*, \infty)$, the model strictly stays short into rising variance spikes.
   - *Failure Rule (`research-defined falsification threshold`):* If maximum drawdown exceeds 50% of allocated vega equity without triggering an emergency circuit-breaker, the unbounded continuation assumption is rejected for risk-managed deployment.

## Crypto portability

**Label: adapted / unproven**

The primary paper evaluates variance swaps solely on equity index dynamics (S&P 500, Cboe Variance Futures). Direct application to cryptocurrency markets requires significant adaptation and remains completely unproven:

1. **Absence of Listed Continuous Variance Swaps (`research-proposed`):**
   - Unlike Cboe variance futures, major crypto derivatives venues (Deribit, Binance, OKX, Bybit) do not list perpetual variance swaps settled against realized variance.
   - A crypto implementation must rely on synthetic replication via:
     (a) rolling 30-day Deribit DVOL futures, or
     (b) dynamic log-contract replication using Deribit option strips, or
     (c) power perpetuals ($S^2$) with funding rates reflecting squared variance (`research-proposed`).
2. **Fat Tails and Extreme Volatility of Volatility ($\gamma$) (`research-proposed`):**
   - Crypto realized volatility regularly exhibits heavy-tailed jumps and rapid clustering ($\gamma_{\text{crypto}} \gg 0.40$). When $\gamma$ is elevated, the Feller parameter $\nu = 2\kappa\theta/\gamma^2$ frequently drops below 1, violating the boundary condition that keeps variance strictly positive and inflating the probability mass near zero.
3. **8-Hour Perpetual Funding and Margin Drag (`research-proposed`):**
   - In crypto perpetual derivatives, collateral is held in stablecoins (USDT/USDC) or coin-margined collateral. Crypto borrowing/margin rates frequently fluctuate between 5% and 30% annualized, far exceeding the 100–210 bps carrying cost window analyzed in the paper and potentially destroying the net VRP harvest.
4. **24/7 Continuous Jumps and Microstructure Noise (`research-proposed`):**
   - Crypto trades 24/7 without market open/close auctions, resulting in jump-diffusion noise that distorts continuous CIR diffusion filtering.

## Limitations

- **Theoretical Model Idealization:** The paper's closed-form solution rests on idealized continuous-time CIR/Heston diffusion and memoryless exponential contract lifetime ($T_\delta \sim \text{Exp}(\delta)$). Real variance contracts trade with fixed deterministic expiries.
- **Unbounded Continuation into Crashes:** Because the continuation region for short variance is $(b^*, \infty)$, the mathematical rule dictates holding the short position throughout catastrophic variance explosions, exposing the portfolio to severe left-tail drawdown risk.
- **Sensitivity to Idle Capital Cost $c_0$:** The operational viability of the entry rule depends critically on $c_0$; small changes in assumed hurdle rates (25–50 bps) cause dramatic shifts in the entry trigger level (from 95th to 58th percentile).
- **Data Gap for True Perpetual Contract:** No listed perpetual variance swap exists with continuous cash settlement; testing requires synthetic proxy constructions.
- **Not Independently Reproduced:** All numerical benchmarks originate solely from the primary paper's author calibration.

## Implementation status

`not-implemented`.

This research capture represents theoretical and quantitative analysis only. No implementation of the Kummer/Tricomi smooth-pasting solver, CIR parameter filter, or perpetual variance swap execution model exists in our research repository, PyBroker, or NautilusTrader pipelines.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This document is an external research evaluation and does not constitute approval or authorization for live, paper, or testnet trading. Any future implementation requires formal research review, synthetic crypto proxy validation, and approval through canonical governance channels.

## Related Wiki records

- `[[quant/cross-asset-reconfiguration-premium-subdominant-eigenspace-vrp-2026-09-02]]` — Cross-asset variance risk premium and co-movement eigenspace structures.
- `[[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12]]` — Empirical fragility and synthetic replication decay of crypto variance swaps.
- `[[quant/equity-index-dispersion-correlation-risk-premium-spread-friction-falsification-2026-09-13]]` — Index dispersion and variance risk premium execution frictions.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Canonical protocol for leakage-safe cross-validation of volatility and options signals.

## Sources

1. Jun Maeda. *"Optimal entry and exit for variance swaps: closed-form rules for the perpetual contract"*, arXiv preprint `arXiv:2609.19102v1 [q-fin.MF]`, submitted September 16, 2026.
   - Stable arXiv URL: https://arxiv.org/abs/2609.19102
   - HTML version: https://arxiv.org/html/2609.19102v1
   - PDF version: https://arxiv.org/pdf/2609.19102v1
   - Canonical DOI: [10.48550/arXiv.2609.19102](https://doi.org/10.48550/arXiv.2609.19102)
