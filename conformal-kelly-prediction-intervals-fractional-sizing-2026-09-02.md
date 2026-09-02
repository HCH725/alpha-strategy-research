---
schema: strategy-research-record-v1
title: "Conformal Kelly: Conformal Prediction Intervals as the Robust Scale in Fractional Kelly Position Sizing"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - position-sizing
  - kelly-criterion
  - conformal-prediction
  - uncertainty-quantification
  - drawdown-control
  - etf-portfolios
  - out-of-sample-lockbox
  - negative-evidence
status: research-only
confidence: high
source_as_of: 2026-08-02
sources:
  - "Robert Jacob Ryan, 'Conformal Kelly: Conformal Prediction Intervals as the Scale in Fractional Kelly Position Sizing', arXiv:2608.01494v1 [q-fin.PM], August 2, 2026. DOI: https://doi.org/10.48550/arXiv.2608.01494. Full text: https://arxiv.org/abs/2608.01494, HTML: https://arxiv.org/html/2608.01494v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Conformal Kelly: Conformal Prediction Intervals as the Robust Scale in Fractional Kelly Position Sizing

## Provenance

- **Canonical Source:** arXiv:2608.01494v1 [q-fin.PM], submitted August 2, 2026.
- **Author:** Robert Jacob Ryan.
- **DOI:** [https://doi.org/10.48550/arXiv.2608.01494](https://doi.org/10.48550/arXiv.2608.01494)
- **Stable Source URLs:**
  - Abstract: [https://arxiv.org/abs/2608.01494](https://arxiv.org/abs/2608.01494)
  - Full Text HTML: [https://arxiv.org/html/2608.01494v1](https://arxiv.org/html/2608.01494v1)
  - PDF: [https://arxiv.org/pdf/2608.01494](https://arxiv.org/pdf/2608.01494)
- **Evaluation Code Scaffold:** GitHub commit blob SHA `f7ee273086f044e4d3f2fadaeca7ebc47adc4037` (`prepare.py` immutable benchmark harness).
- **Dataset:** Frozen Kaggle daily adjusted close prices snapshot (`malik1641/stocks-and-etfs-prices`, as of 2024-09-25) spanning 2006-05 to 2024-09-20 across eight liquid US ETFs (SPY, QQQ, DIA, MDY, GLD, SLV, USO, DBC).
- **Sample Partitioning & Protocol:**
  - **TRAIN:** Inception to 2015-12-31 (includes the 2008 Global Financial Crisis);
  - **DEV:** 2016-01-01 to 2021-12-31 (1,511 trading days; includes 2018 Q4 selloff and 2020 COVID crash; sole development loop window);
  - **LOCKBOX (Sealed OOS):** 2022-01-01 to 2024-09-20 (683 trading days; sealed prior to unsealing on 2026-07-30 under pre-registered protocol `paper/prereg.md`).

## Economic mechanism

### Source-reported

1. **Scale Estimation under Fat Tails:** Classical multi-asset Kelly position sizing specifies an allocation fraction $f_i \propto \hat{\mu}_i / \hat{\sigma}_i^2$. In empirical financial time series with fat tails and jump risks, standard deviation $\hat{\sigma}_i$ is acutely sensitive to extreme outliers. A single tail shock violently inflates sample variance, artificially collapsing position sizes right as volatility mean-reverts and high-expected-return opportunities emerge. Conformal prediction intervals $(1 - \alpha = 0.75)$ provide a non-parametric, rank-based quantile scale proxy that resists individual outlier distortion.
2. **Width Stability vs. Local Sharpness:** In standard time-series machine learning, practitioners prioritize "locally adaptive" conformal inference (e.g., volatility-scaled nonconformity scores, rolling adaptive intervals, or recency weighting) to produce sharp, dynamically expanding and contracting prediction bands. The author discovers that in sizing applications, this guidance backfires: every device accelerating interval adaptation reduces annual compounding growth by 0.7 to 5.3 percentage points. Because the Kelly objective integrates the scale term over time ($1/\hat{\sigma}^2$), sizing penalizes the variance of the scale estimator far more than it rewards local sharpness. Slower, geometrically anchored rolling quantiles minimize estimator variance drag.
3. **Downside Miscoverage as an Asymmetric Regime Dial:** While distribution-free exchangeability guarantees fail under overlapping financial returns, empirical miscoverage remains an informative state variable. Specifically, tracking the frequency with which realized returns penetrate the *downside* conformal bound ($d_t > \alpha/2$) detects negative distribution shift and structural liquidation pressure. Systematically de-leveraging when downside misses spike truncates portfolio drawdown tails without sacrificing typical recovery growth.

### Research interpretation

- **Convexity Drag in Sizing Denominators:** The transformation from scale to position size $g(\sigma) = \sigma^{-2}$ is strongly convex. By Jensen's inequality and error propagation, volatility in the estimate $\hat{\sigma}_t$ induces substantial negative compounding drag on portfolio wealth. A slowly updating conformal quantile functions as an effective low-pass filter, filtering out high-frequency estimation noise while preserving structural cross-sectional scale differences.
- **Cross-Sectional Allocation under Binding Leverage Constraints:** In the presence of a portfolio-level gross leverage cap (here fixed at 2.0), the book operates at the cap on 97.7% of development days. Consequently, individual scale estimators do not dictate gross market exposure; instead, they govern the cross-sectional risk allocation ratios $f_i / f_j$. Robust non-parametric scale estimation prevents a single turbulent asset from distorting the capital weights of the rest of the book.
- **Ported Hypothesis Note:** The empirical demonstrations in the source paper were conducted exclusively on liquid US equity and commodity ETFs. Transferring this mechanism to cryptocurrency perpetual futures or spot tokens constitutes an adapted, unproven research interpretation.

## Signal

### Signal formation and cadence
- **Decision Timestamp:** Signal generated at date $t$ post-market close using data available up to $t$.
- **Execution:** 1-day implementation lag enforced by the harness (trades execute on date $t+1$).
- **Rebalance Frequency:** Daily position updates; underlying forecaster and expanding anchor refitted every 21 trading days.

### Underlying return forecaster
For each asset $i \in \{1, \dots, A\}$ independently:
- **Model:** Expanding-window ridge regression with fixed regularization parameter $\lambda_{\text{ridge}} = 10$, refitted every 21 trading days, first prediction after 750 trading days.
- **Features (4 unstandardized inputs):**
  1. Momentum over 21 trading days ($r_{t-21, t}$);
  2. Momentum over 63 trading days ($r_{t-63, t}$);
  3. Momentum over 252 trading days ($r_{t-252, t}$);
  4. Exponentially weighted moving average volatility: $\text{EWMA}(20)$.
- **Target:** Forward $H$-day arithmetic return sum:
  $$R_{i,t}^{(H)} = \sum_{s=1}^H r_{i, t+s}$$
  with training strictly truncated at $\text{fit\_end} = t - H + 1$ to prevent forward label leakage.

### Multi-horizon ensemble
- Forecasts computed across 5 horizons: $H \in \{12, 16, 21, 27, 34\}$ trading days.
- Each horizon prediction is scaled to a common 21-day reference by $\sqrt{21/H}$.
- Component predictions are ensembled via conformal inverse-variance weighting: component $h$ receives weight:
  $$w_h \propto \frac{1}{q_h^2}$$
  where $q_h$ is the causal conformal half-width of that component's residual against the common 21-day target.

### Conformal scale estimator
1. **Nonconformity Score:** Absolute residual between realized 21-day forward return and point forecast:
   $$s_{i,t} = \left|R_{i,t}^{(21)} - \hat{\mu}_{i,t}\right|$$
2. **Rolling Conformal Quantile ($q^{roll}_{i,t}$):** $(1 - \alpha) = 0.75$ empirical quantile over the trailing window $W = 500$ landed scores:
   $$[t - H - W + 1, \, t - H + 1)$$
   ensuring no unlanded future outcomes enter the calibration set.
3. **Geometric Shrinkage toward Expanding Anchor:**
   $$q^{eff}_{i,t} = \left(q^{roll}_{i,t}\right)^{1 - \lambda} \left(q^{anchor}_{i,t}\right)^\lambda, \quad \lambda = 0.3$$
   where $q^{anchor}_{i,t}$ is the 0.75 quantile of all landed scores from inception to date, recomputed every 21 trading days and held stale in between.
4. **Volatility Proxy:**
   $$\hat{\sigma}_{i,t} = \frac{q^{eff}_{i,t}}{z_{1 - \alpha/2}}$$
   where $z_{1 - \alpha/2} = 1.2816$ (source notes a disclosed implementation convention: $\Phi^{-1}(0.90) = 1.2816$ corresponding to nominal $\alpha = 0.20$, which rescales effective leverage by a constant factor of $1.24$).

### Fractional Kelly position sizing
Raw position fraction for asset $i$ on day $t$:
$$f_{i,t} = \kappa \cdot \frac{\hat{\mu}_{i,t}}{\hat{\sigma}_{i,t}^2}, \quad \kappa = 0.15$$
subject to:
- Per-asset winsorization: $f_{i,t} \in [-0.75, +0.75]$;
- Portfolio gross leverage cap: $\sum_{i=1}^A |f_{i,t}| \le 2.0$. If the sum exceeds $2.0$, all weights are proportionally renormalized:
  $$w_{i,t}^{(A)} = 2.0 \cdot \frac{f_{i,t}}{\sum_{j=1}^A |f_{j,t}|}$$

### Drawdown dial (Config B)
Monitors the trailing one-sided downside miscoverage rate $d_t$ (fraction of realized residuals in trailing window $M = 21$ days where realized return fell below the lower conformal interval bound).
When downside breaks exceed the nominal one-sided break rate $\alpha/2 = 0.125$, gross leverage is scaled down via multiplier $m_t$:
$$m_t = \text{clip}\left(1 - \beta \cdot \frac{d_t - \alpha/2}{\alpha/2}, \, 0.25, \, 1.0\right), \quad \beta = 1.0$$
The Config B position is:
$$w_{i,t}^{(B)} = m_t \cdot w_{i,t}^{(A)}$$

## Required data

- **Universe:** 8 liquid US-listed ETFs:
  - Equities: SPY (S&P 500), QQQ (Nasdaq 100), DIA (Dow Jones Industrial Average), MDY (S&P MidCap 400);
  - Commodities: GLD (Gold), SLV (Silver), USO (Crude Oil), DBC (Commodity Index).
- **Venue:** US Equity Exchanges (standard national market system).
- **Timeframe:** Daily closing bars.
- **Fields:** Adjusted close prices, volume.
- **Point-in-Time Availability:** All inputs strictly respect causal boundaries. Landed residuals require an $H$-day delay ($t - H + 1$); execution enforces an additional 1-day implementation lag.
- **Missing Data Handling:** Synchronized US equity trading calendar from frozen Kaggle snapshot (`malik1641/stocks-and-etfs-prices`).
- **Cost & Fee Requirements:**
  - Turnover penalty: 5 bps ($0.0005$) per unit of turnover charged at each rebalance;
  - Financing overlay: Borrow cost on gross exposure exceeding $1.0$ quantified at $0\%$, $1\%$, $2\%$, and $4\%$ annualized.

## Execution assumptions

- **Execution Timing:** Next-day market execution following day $t$ close calculation (1-day implementation lag).
- **Order Model:** Daily rebalancing at closing auction or market-on-close.
- **Leverage Constraints:** Maximum aggregate gross leverage capped at $2.0\times$; individual asset exposure clipped at $\pm 0.75$.
- **Shorting / Borrow:** Unconstrained borrowing assumed available across liquid mega-cap ETFs.
- **Friction Model:** 5 bps one-way cost per unit of portfolio turnover ($0.05 \times \sum_i |\Delta w_{i,t}|$). Market impact is assumed negligible for these mega-cap ETF instruments at modest capital scale.

## Evidence

### Source-reported

All metrics below are reported directly by Robert Jacob Ryan (arXiv:2608.01494v1, August 2026) using the byte-identical immutable evaluation harness:

#### Development Sample (DEV 2016-01-01 to 2021-12-31, 1,511 trading days)
*Net of 5 bps turnover cost; financing on gross > 1 excluded from base harness:*

| Strategy / Configuration | Ann. Net Log Growth | Sharpe Ratio | Max Drawdown | Calmar Ratio | Annual Volatility | Mean Gross Leverage | Realized Coverage (Nominal 0.75) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Config A (Metric-Best)** | **0.2845** (28.45%) | **1.336** | **27.68%** | **1.127** | **23.36%** | **1.960** | **0.7483** |
| **Config B (Drawdown Dial)** | **0.2584** (25.84%) | **1.386** | **20.26%** | **1.376** | **20.12%** | **1.833** | **0.7483** |
| SPY Buy & Hold (Harness-capped 0.75) | 0.1226 | 0.976 | 26.10% | 0.505 | 13.50% | 0.750 | — |
| SPY Buy & Hold (Uncapped 1.0) | 0.1594 | 0.976 | 33.70% | 0.521 | 18.00% | 1.000 | — |
| Equal Weight ($1\times$ gross) | 0.1189 | 0.841 | 32.50% | 0.403 | 15.60% | 1.000 | — |
| Equal Weight ($2\times$ gross) | 0.2125 | 0.841 | 56.50% | 0.465 | 31.20% | 2.000 | — |
| Inverse-Vol Risk Parity ($2\times$ gross) | 0.2225 | 0.971 | 52.40% | 0.494 | 26.70% | 2.000 | — |
| Vol-Target Risk Parity (30% vol, gross 1.92) | 0.2074 | 1.047 | 38.80% | 0.600 | 22.20% | 1.917 | — |
| 4-Equity ETFs @ 0.5 (Post-hoc benchmark) | 0.2934 | 0.963 | 60.90% | 0.605 | 38.20% | 2.000 | — |
| 4-Commodity ETFs @ 0.5 (Post-hoc control) | 0.0892 | 0.430 | 68.70% | 0.228 | 36.50% | 2.000 | — |

- **Per-Asset Arithmetic Contribution (DEV Config A):** All 8 assets contributed positively: QQQ (+0.0836, 27% of total), SPY (+0.0585), DIA (+0.0568), USO (+0.0406 from a mean position of -0.039, confirming pure timing value), MDY (+0.0383), GLD (+0.0242), DBC (+0.0080), SLV (+0.0021). Sum of arithmetic net returns: $+0.3120$; subtracting variance drag $\sigma^2/2$ yields headline net log growth of $0.2845$.
- **$\sigma$-Estimator Ablation on DEV (Table 4):**
  - Rolling conformal quantile: $0.2821$ growth, $1.34$ Sharpe;
  - Rolling mean absolute deviation: $0.2693$ growth, $1.27$ Sharpe;
  - Conformal quantile frozen on TRAIN: $0.2669$ growth, $1.21$ Sharpe;
  - Rolling residual standard deviation: $0.2476$ growth, $1.19$ Sharpe.
  - At matched pre-cap gross: Rolling conformal quantile ($0.2774$, Sharpe $1.32$) beats residual standard deviation ($0.2566$, Sharpe $1.24$) by $+2.08$ percentage points of annual compounding growth.
- **Drawdown Dial Timing Significance:** Testing Config B's drawdown dial against 40 circular-shift placebo timings showed that zero out of 40 placebos beat the realized maximum drawdown of $20.26\%$ (null median drawdown was $27.68\%$, minimum $22.34\%$), establishing empirical rank-based significance ($p = 1/41$).

#### Sealed Out-of-Sample Lockbox (2022-01-01 to 2024-09-20, 683 trading days)
*Evaluated exactly once under pre-registered protocol `paper/prereg.md`:*

| Strategy / Configuration | Ann. Net Log Growth | Sharpe Ratio | Max Drawdown | Calmar Ratio | Annual Volatility | Realized Coverage (Nominal 0.75) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Config A Primary** | **+0.0847** (8.47%) | **0.453** | **36.60%** | **0.327** | **26.40%** | **0.7450** |
| **Config B Primary** | **+0.0701** (7.01%) | **0.422** | **31.70%** | **0.303** | **22.80%** | **0.7450** |
| Config A Secondary (trades final 21d) | +0.1147 | 0.565 | 36.60% | 0.410 | 26.60% | 0.7485 |
| Config B Secondary (trades final 21d) | +0.0968 | 0.537 | 31.70% | 0.389 | 22.90% | 0.7485 |
| SPY Buy & Hold (Harness-capped 0.75) | +0.0630 | 0.540 | 18.70% | 0.390 | 13.50% | — |
| Equal Weight ($2\times$ gross) | +0.1679 | 0.710 | 35.30% | 0.600 | 29.70% | — |
| 4-Commodity ETFs @ 0.5 ($2\times$ gross) | +0.1723 | 0.640 | 42.80% | 0.580 | 38.70% | — |
| 4-Equity ETFs @ 0.5 ($2\times$ gross) | +0.1079 | 0.480 | 46.20% | 0.380 | 37.00% | — |

- **Cost Sensitivity on Lockbox (Table L4):**
  - Config A net log growth: 0 bps ($+0.093$), 5 bps baseline ($+0.085$), 10 bps ($+0.077$), 20 bps ($+0.061$), 50 bps ($+0.013$);
  - Config B net log growth: 0 bps ($+0.079$), 5 bps baseline ($+0.070$), 10 bps ($+0.061$), 20 bps ($+0.044$), 50 bps ($-0.009$).
- **Financing Overlay on Lockbox (Cash borrow rate on gross > 1.0):**
  - Config A net growth: 0% borrow cost ($+0.085$), 1% ($+0.075$), 2% ($+0.066$), 4% ($+0.047$);
  - Config B net growth: 0% borrow cost ($+0.070$), 1% ($+0.062$), 2% ($+0.055$), 4% ($+0.041$).

### Independently reproduced

`not independently reproduced`

### Negative evidence

1. **Failure of Locally Adaptive Conformal Prediction:**
   - Volatility-scaled nonconformity scores degraded annual growth by $-5.3$ pp at 50-day scale and $-3.3$ pp at 100-day scale;
   - Adaptive Conformal Inference (Gibbs & Candès, 2021) degraded performance monotonically ($-1.6$ pp at $\gamma = 0.005$, collapsing to $0.128$ at $\gamma = 0.05$);
   - Recency-weighted conformal prediction (Barber et al., 2023) degraded growth by $-1.4$ pp at $\rho = 0.99$;
   - Asymmetric two-sided intervals and downside-only CQR lost $-1.6$ pp;
   - Mondrian within-asset-class calibration lost $-2.4$ pp.
   *Mechanism:* Rapidly adapting intervals introduce high variance into the denominator of the Kelly formula ($1/\hat{\sigma}_t^2$). Compounding wealth penalizes estimator variance far more than it rewards local interval sharpness.
2. **Failure of Conformal Predictive Decision Rules (Vovk & Bendtsen Expected Utility):** Solving expected log utility directly over the empirical calibration residual distribution yielded an inferior return of $0.1525$ (Sharpe $0.74$) in raw form, and $0.2411$ when mean-recentered (still $-3.6$ pp below baseline). The empirical distribution over-penalizes fat left tails, inducing excessive deleveraging on risky assets.
3. **Failure of Multivariate Kelly with Covariance Inversion:** Solving full multivariate Kelly $\mathbf{f} \propto \mathbf{\Sigma}^{-1} \hat{\boldsymbol{\mu}}$ collapsed annualized growth to between $0.023$ and $0.179$ across shrinkage intensities $0.0$ to $0.9$, while turnover exploded to $11\times$–$30\times$. Markowitz error amplification and cross-asset hedging severely eroded the portfolio's net equity risk premium.
4. **Lockbox Performance Decay:** While conformal coverage was remarkably stable out of sample ($0.7450$ realized vs. $0.7500$ nominal), compounding log growth degraded from $28.45\%$ on DEV to $8.47\%$ on LOCKBOX. During the 2022–2024 inflationary and aggressive Fed rate hike cycle, the strategy was outperformed on raw growth by passive equal-weight ($16.79\%$) and passive commodity ETF baskets ($17.23\%$).

## Falsification plan

1. **Coverage Calibration Stability Test:**
   - *Procedure:* In an expanding walk-forward test across subsequent out-of-sample data (2024 to present), calculate the realized marginal coverage rate across all 8 assets.
   - *Falsification Rule:* If realized marginal coverage deviates by more than $\pm 5.0$ percentage points from nominal (i.e. realized coverage $< 0.70$ or $> 0.80$ over a rolling 252-day window), reject the validity of the geometric anchor shrinkage calibration.
2. **Conformal vs. Realized Volatility Scale Sizing Horserace:**
   - *Procedure:* Compare Conformal Kelly directly against an identical portfolio sized with rolling 20-day realized standard deviation at matched gross leverage and transaction costs.
   - *Falsification Rule:* If the conformal scale estimator fails to achieve a higher Sharpe ratio or higher annualized net log growth than sample standard deviation over a minimum 500-day evaluation sample, reject the hypothesis that conformal quantiles provide a superior scale proxy.
3. **Downside Miscoverage Dial Placebo Test:**
   - *Procedure:* Generate 1,000 circular block-bootstrap resamples of the downside miscoverage multiplier series $m_t$ to destroy event timing while preserving the marginal distribution of leverage cuts.
   - *Falsification Rule:* If Config B's maximum drawdown fails to beat at least 95% of the synthetic placebos ($p > 0.05$), falsify the timing efficacy of the drawdown dial and attribute drawdown reductions to mechanical deleveraging.
4. **Leverage Cap Ablation:**
   - *Procedure:* Relax the $2.0\times$ gross leverage cap and simulate unconstrained fractional Kelly allocations.
   - *Falsification Rule:* If the unconstrained system experiences portfolio drawdowns exceeding $60\%$ or leverage spikes $> 5\times$, confirm that the empirical success of the reported strategy is conditionally dependent on the structural work of the 2.0 gross cap rather than the unassisted Kelly formula.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`
- **Porting Rationale & Structural Distinctions:**
  - *Session Structure & Timestamps:* Unlike US ETFs with standardized 16:00 EST closing auctions, crypto trades 24/7. Calculating daily forward return sums $R_{i,t}^{(H)}$ requires establishing an explicit convention (e.g. 00:00 UTC snapshot).
  - *Perpetual Funding Costs:* In crypto perpetual futures, maintaining a $2.0\times$ gross levered portfolio incurs dynamic 8-hour funding rates. In bullish regimes, positive funding creates significant drag on long positions, altering the net return definition $R_{i,t}^{(H)}$.
  - *Fat-Tailed Kurtosis & Flash Crashes:* Crypto assets exhibit extreme tail kurtosis and cascade liquidations that surpass commodity/equity ETF tails. While conformal prediction is non-parametric, severe regime clustering can lead to prolonged clustering of downside misses, triggering the drawdown dial to permanently minimize gross exposure to the floor ($0.25$).
  - *Margin Mechanics:* Dynamic mark-to-market collateral valuation and liquidation engines require wider margin buffers than the standard Regulation T equity framework.

## Limitations

- **Single Dataset & Survivorship Bias:** Evaluated on a single frozen Kaggle dataset of 8 highly liquid US ETFs; performance on less liquid individual equities or digital assets is completely unverified.
- **Structural Work of the 2.0 Gross Cap:** Because the gross leverage cap binds on 97.7% of development days, the mechanism acts primarily as a cross-sectional capital allocator rather than an unconstrained leverage optimizer. Findings may not generalize to unlevered or unconstrained portfolios.
- **Concentration in 2020 Performance:** Development results are heavily dominated by 2020 (+0.667 net log growth for Config A), which accounts for a disproportionate share of total compounding wealth.
- **Non-Exchangeability of Overlapping Returns:** Because forward returns are overlapping ($H = 21$), observations violate the exchangeability assumption fundamental to theoretical conformal prediction guarantees. Coverage is an empirical finding, not a mathematical certainty.
- **Closed Pre-Registration Repository:** The pre-registration protocol (`paper/prereg.md`) was conducted within a private Git repository rather than an independently timestamped public registry (e.g. OSF).

## Implementation status

- `not-implemented`. No implementation has been created in NautilusTrader, PyBroker, or any live execution harness. This document serves strictly as an upstream research capture.

## Adoption boundary

- `research-only`, `not-approved`. Capturing this strategy research does not authorize implementation, paper trading, testnet, or live deployment.

## Related Wiki records

- `[[kellyboost-growth-optimal-gbdt-portfolio-construction-2026-09-02]]`
- `[[small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02]]`
- `[[continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]]`

## Sources

1. Robert Jacob Ryan, *"Conformal Kelly: Conformal Prediction Intervals as the Scale in Fractional Kelly Position Sizing"*, arXiv preprint `arXiv:2608.01494v1 [q-fin.PM]`, August 2, 2026. DOI: [https://doi.org/10.48550/arXiv.2608.01494](https://doi.org/10.48550/arXiv.2608.01494). Full text HTML: [https://arxiv.org/html/2608.01494v1](https://arxiv.org/html/2608.01494v1). PDF: [https://arxiv.org/pdf/2608.01494](https://arxiv.org/pdf/2608.01494).
