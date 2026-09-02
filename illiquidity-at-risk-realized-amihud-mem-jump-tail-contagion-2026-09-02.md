---
schema: strategy-research-record-v1
title: "Illiquidity-at-Risk (IlliQaR): Tail Risk Forecasting and Discontinuous Liquidity Evaporation Contagion via Realized Amihud MEM-J"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - illiquidity-at-risk
  - realized-amihud
  - multiplicative-error-model
  - jump-diffusion
  - market-microstructure
  - bipower-variation
  - systemic-risk
  - risk-aversion
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - "Demetrio Lacava and Paolo Santucci de Magistris, 'Illiquidity at Risk', arXiv preprint arXiv:2609.00943v1 [q-fin.RM, econ.EM], September 1, 2026. DOI: 10.48550/arXiv.2609.00943. Stable URL: https://arxiv.org/abs/2609.00943"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Illiquidity-at-Risk (IlliQaR): Tail Risk Forecasting and Discontinuous Liquidity Evaporation Contagion via Realized Amihud MEM-J

## Provenance

- **Primary Source:** Demetrio Lacava (University of Rome Tor Vergata) and Paolo Santucci de Magistris (LUISS University), *"Illiquidity at Risk"*, arXiv preprint `arXiv:2609.00943v1 [q-fin.RM, econ.EM]`, submitted September 1, 2026. DOI: [10.48550/arXiv.2609.00943](https://doi.org/10.48550/arXiv.2609.00943). Stable URL: [https://arxiv.org/abs/2609.00943](https://arxiv.org/abs/2609.00943). Full text HTML: [https://arxiv.org/html/2609.00943v1](https://arxiv.org/html/2609.00943v1).
- **Core Empirical Datasets:**
  - **S&P 500 Index:** Daily realized volatility (RV, 5-minute sampling) sourced from Oxford-Man Institute of Quantitative Finance; daily trading volume sourced from Datastream. Sample period: January 3, 2005 to October 15, 2021 (4,226 trading days). In-sample calibration window: January 3, 2005 to October 15, 2015; out-of-sample evaluation window: October 16, 2015 to October 15, 2021.
  - **Cross-Sectional Individual Equities:** 25 large U.S. equities from January 3, 2012 to January 10, 2024. In-sample calibration window: January 3, 2012 to February 4, 2020; out-of-sample evaluation window: February 5, 2020 to January 10, 2024.
- **Related Foundational Literature:**
  - Amihud, Y. (2002), "Illiquidity and stock returns: Cross-section and time-series effects", *Journal of Financial Markets* 5(1), 31–56 — classical daily ratio of absolute returns to volume.
  - Ranaldo, A. & Santucci de Magistris, P. (2022) / Lacava, D. et al. (2026) — theoretical foundation of high-frequency realized Amihud converging to integrated illiquidity $\int_0^1 \ell(s) ds$.
  - Engle, R. F. (2002), "New frontiers for ARCH models", *Journal of Applied Econometrics* 17(5), 425–446 — Multiplicative Error Model (MEM).
  - Corsi, F. (2009), "A simple approximate long-memory model of realized volatility", *Journal of Financial Econometrics* 7(2), 174–196 — Heterogeneous Autoregressive (HAR) cascade.
  - Caporin, M., Rossi, E., & Santucci de Magistris, P. (2017), "Chasing volatility: A persistent multiplicative error model with jumps", *Journal of Econometrics* 198(1), 122–145 — MEM-J specification with compound Poisson jumps.
  - Barndorff-Nielsen, O. E. & Shephard, N. (2004), "Power and bipower variation with stochastic volatility and jumps", *Journal of Financial Econometrics* 2(1), 1–37 — bipower variation (BPV).
  - Bekaert, G., Hoerova, M., & Lo Duca, M. (2013), "Risk, uncertainty and monetary policy", *Journal of Monetary Economics* 60(7), 771–788 — VIX decomposition into uncertainty and risk aversion.

## Economic mechanism

### Source-reported

1. **Liquidity Risk vs. Price Risk:** Liquidity risk represents uncertainty regarding the ability to convert an asset into cash (or vice versa) without incurring prohibitive costs or large price dislocations. Sudden evaporation of liquidity transforms localized shocks into systemic flash crashes.
2. **Microstructure Origins of Discontinuous Illiquidity Bursts (Jumps):** Sudden liquidity evaporation is not a smooth diffusion; it occurs via abrupt discontinuities driven by:
   - Synchronous binding of dealer capital constraints (Brunnermeier & Pedersen 2009);
   - Rapid withdrawal of algorithmic 'phantom liquidity' during volatility spikes (Kirilenko et al. 2017);
   - Discrete shifts in adverse-selection risk following macroeconomic or earnings releases (Glosten & Milgrom 1985).
3. **Noise Reduction via High-Frequency Realized Amihud:** Low-frequency daily Amihud proxies are noisy, masking true tail behavior (error term variance is ~11 times larger). Realized Amihud, computed from 5-minute intraday returns as the ratio of realized volatility to volume ($\text{Illiq}_t = RV_t / \nu_t$), filters out microstructure noise and converges to latent integrated illiquidity.
4. **Purging Price Jumps via Bipower Variation:** Major news events shift reservation prices simultaneously across all participants with little volume (disagreement), mechanically inflating $RV$ without reflecting trading frictions. Replacing $RV$ with jump-robust bipower variation ($\text{Illiq}_t^C = BPV_t / \nu_t$) isolates true friction-driven illiquidity jumps.
5. **Systemic Contagion and Risk Aversion Transmission:** Market illiquidity exhibits strong asymmetry ('leverage effect', deteriorating more heavily following negative returns). Decomposition of the VIX reveals that IlliQaR violations are driven specifically by sudden spikes in risk aversion (causing capital withdrawal by liquidity providers), not by predictable volatility uncertainty. Crucially, S&P 500 IlliQaR violations act as a leading systemic indicator for idiosyncratic liquidity dry-ups across individual stocks.

### Research interpretation

The falsifiable alpha and risk-control thesis centers on **anticipating and hedging systemic liquidity evaporation shocks**:
1. **Dynamic Execution & Slippage Risk Mitigation:** Execution algorithms typically model slippage as a static or continuous function of volume and spread. Incorporating real-time 1-step ahead $\text{IlliQaR}_t(p)$ forecasts derived from G-AMEM-HAR-J allows an execution system to detect when a market is entering a discontinuous liquidity evaporation regime. When predicted $\text{IlliQaR}_t(5\%)$ breaches critical thresholds, order pacing should dynamically downscale, trade execution should transition from taker to passive maker with widened limits, or trading should be halted to avoid catastrophic transaction cost slippage.
2. **Index-to-Single-Stock Lead-Lag Contagion:** Because S&P 500 IlliQaR violations cluster and lead single-stock liquidity dry-ups, index-level IlliQaR spikes serve as an early warning trigger for cross-sectional inventory de-risking and cross-market liquidation cascades.
3. **Liquidity-Tail Risk Premium Harvesting:** Assets subject to severe discontinuous illiquidity jumps require an actuarial tail-risk premium. Portfolios dynamically tilted against high-IlliQaR assets (or shorting liquidity-tail exposed instruments while longing resilient ones) can capture the spread between transient liquidity shocks and subsequent mean-reverting liquidity recoveries.

## Signal

### Signal Definition and Mathematical Architecture

The signal framework operates in two distinct stages: (1) high-frequency realized illiquidity measurement, and (2) dynamic conditional quantile forecasting via the jump-augmented Multiplicative Error Model with Heterogeneous Autoregressive structure (G-AMEM-HAR-J).

#### 1. Realized Illiquidity Proxies
For day $t$, partition the trading day into $M$ intraday intervals of length 5 minutes. Let $r_{i,t}$ be the $i$-th 5-minute log return and $\nu_{i,t}$ the corresponding volume:
- **Total Realized Amihud:**
  $$\text{Illiq}_t = \frac{RV_t}{\nu_t} = \frac{\sqrt{\sum_{i=1}^M r_{i,t}^2}}{\sum_{i=1}^M \nu_{i,t}}$$
  *(Alternatively, realized power variation of order one $RPV_t = \sum_{i=1}^M |r_{i,t}|$ has $>99\%$ correlation with $RV_t$ and yields equivalent dynamics).*
- **Continuous (Price-Jump Purged) Realized Amihud:**
  $$\text{Illiq}_t^C = \frac{BPV_t}{\nu_t} = \frac{\frac{\pi}{2} \sum_{i=2}^M |r_{i,t}| |r_{i-1,t}|}{\sum_{i=1}^M \nu_{i,t}}$$

#### 2. G-AMEM-HAR-J Econometric Specification
The observed non-negative realized illiquidity $\text{Illiq}_t$ decomposes multiplicatively into conditional expectation $\mu_t$, compound Poisson jump factor $Z_t$, and continuous Gamma innovation $\epsilon_t$:
$$\text{Illiq}_t = \mu_t Z_t \epsilon_t, \quad \epsilon_t \overset{i.i.d.}{\sim} \Gamma(1, \vartheta)$$
where $\vartheta > 0$ is the shape parameter (with scale $1/\vartheta$, so $\mathbb{E}[\epsilon_t]=1, \text{Var}(\epsilon_t)=1/\vartheta$).

- **Conditional Mean $\mu_t$ (HAR cascade with leverage asymmetry):**
  $$\mu_t = \omega + \alpha_d \text{Illiq}_{t-1} + \alpha_w \text{Illiq}_{t-1:t-5} + \alpha_m \text{Illiq}_{t-1:t-21} + \beta \mu_{t-1} + \gamma D_{t-1} \text{Illiq}_{t-1}$$
  where $\text{Illiq}_{t-1:t-5} = \frac{1}{5}\sum_{k=1}^5 \text{Illiq}_{t-k}$, $\text{Illiq}_{t-1:t-21} = \frac{1}{21}\sum_{k=1}^{21} \text{Illiq}_{t-k}$, and $D_{t-1} = \mathbf{1}_{\{r_{t-1} < 0\}}$ captures downward leverage asymmetry.

- **Compound Poisson Jump Component $Z_t$:**
  - If jump count $N_t = 0$, $Z_t = d_{\kappa_t}$;
  - If $N_t > 0$, $Z_t = \sum_{j=1}^{N_t} Y_{j,t}$, where $Y_{j,t} \overset{i.i.d.}{\sim} \Gamma(d_{\kappa_t}, \zeta)$ with scale $d_{\kappa_t}/\zeta$;
  - Normalizing factor $d_{\kappa_t} = (e^{-\kappa_t} + \kappa_t)^{-1}$ ensures $\mathbb{E}[Z_t \epsilon_t \mid \mathcal{F}_{t-1}] = 1$.
  - Jump intensity $\kappa_t$ follows an autoregressive feedback process:
    $$\kappa_t = \phi_1 + \phi_2 \kappa_{t-1} + \phi_3 \xi_{t-1}$$
    where $\xi_{t-1} = \mathbb{E}[N_{t-1} \mid \mathcal{F}_{t-1}] - \kappa_{t-1}$ is the filtered jump innovation updated via Bayes' rule:
    $$\mathbb{P}(N_t = j \mid \mathcal{F}_t) = \frac{f(\text{Illiq}_t \mid N_t = j, \mathcal{F}_{t-1}) \mathbb{P}(N_t = j \mid \mathcal{F}_{t-1})}{\sum_{k=0}^\infty f(\text{Illiq}_t \mid N_t = k, \mathcal{F}_{t-1}) \mathbb{P}(N_t = k \mid \mathcal{F}_{t-1})}$$
    and conditional density $f(\text{Illiq}_t \mid N_t = j, \mathcal{F}_{t-1})$ is given in closed form via modified Bessel functions of the second kind $\mathcal{K}(\cdot)$.

#### 3. Illiquidity-at-Risk Quantile Calculation
The $p$-level Illiquidity-at-Risk $\text{IlliQaR}_t(p)$ satisfies:
$$\mathbb{P}(\text{Illiq}_t > \text{IlliQaR}_t(p) \mid \mathcal{F}_{t-1}) = p \iff F_{\text{MEM-J}}(\text{IlliQaR}_t(p) \mid \mathcal{F}_{t-1}) = 1 - p$$
where $F_{\text{MEM-J}}$ is the analytical mixture of Gamma (zero-jump) and Kappa (jump-active) cumulative distribution functions.

#### 4. Operational Trading and Risk Rules
- **Rule A (Execution Risk Throttle):** If forecasted 1-day ahead $\text{IlliQaR}_{t+1}(5\%) > \text{Threshold}_{\text{stress}}$ (calibrated as rolling 95th percentile of historical $\text{IlliQaR}$), curtail active market orders by 50–100%, expand TWAP/VWAP horizons from intraday to multi-day, and widen maker quoting spreads.
- **Rule B (Systemic Index-to-Stock Contagion Hedge):** When S&P 500 (or market index) realized illiquidity violates $\text{IlliQaR}_t(5\%)$, reduce single-stock gross exposure across constituents within the bottom quartile of depth/liquidity resiliency within the next trading session.
- **Rule C (Liquidity Reversal Alpha):** When single-stock $\text{Illiq}_t$ exceeds $\text{IlliQaR}_t(1\%)$ due to a transient idiosyncratic jump, enter contrarian mean-reversion liquidity-provision orders with a 1-to-3 day holding period as jump shocks dissipate.

## Required data

- **High-Frequency Market Data:**
  - Intraday 5-minute sampled OHLC prices to compute log returns $r_{i,t}$.
  - Intraday 5-minute trading volume $\nu_{i,t}$ and daily total trading volume.
  - Bipower variation ($BPV_t$) calculation requiring consecutive adjacent 5-minute returns $|r_{i,t}| |r_{i-1,t}|$.
- **Macro-Financial Exogenous Features (for determinant logit model):**
  - Cboe Volatility Index (VIX) level and lagged changes.
  - VIX decomposition into:
    - $\text{Uncertainty}_t = \widehat{\mathbb{E}[RV_t \mid \mathcal{F}_{t-1}]}$ (linear projection of $RV_t$ on lagged $RV$ and lagged VIX);
    - $\text{RiskAversion}_t = VIX_t^2 - \text{Uncertainty}_t$.
  - Economic Policy Uncertainty (EPU) index (Baker, Bloom, & Davis 2016).
  - TED spread (3-month LIBOR/SOFR vs. 3-month Treasury yield) as a funding liquidity proxy.
- **Timestamp & Timing Requirements:** Daily close observations derived from 09:30 to 16:00 EST equity trading sessions; point-in-time publication of high-frequency realized measures without look-ahead bias. Missing intraday bars handled by zero-return insertion for price continuity.

## Execution assumptions

- **Order Execution Type:** Primarily passive limit orders for liquidity-provision strategies; TWAP/VWAP execution adjustment for execution throttling.
- **Slippage Model:** Non-linear price impact scaling directly with $\text{Illiq}_t$; slippage is assumed to spike by $3\times$ to $10\times$ during realized $\text{IlliQaR}$ violation states.
- **Fees & Costs:** Standard exchange taker fee (e.g. 5–10 bps in equities, 2–5 bps in liquid futures) and maker rebates where applicable.
- **Latency Tolerance:** Daily rebalancing / daily forecast updates evaluated after the close for next-day execution; intraday 5-minute sampling requires low computational overhead (~seconds to evaluate G-AMEM-HAR-J closed-form likelihood).

## Evidence

### Source-reported

All figures, parameter estimates, and test statistics trace directly to Demetrio Lacava and Paolo Santucci de Magistris (arXiv:2609.00943v1, Sections 3.2–5.3, Tables 1–7):

1. **S&P 500 Model Estimation (Full Sample: 2005–2021, Table 2 Panel a):**
   - Model XI (G-AMEM-HAR-J, Realized Amihud):
     - $\omega = 0.0001$ ($t$-stat highly significant, std error $0.0000$);
     - Daily HAR component $\alpha_d = 0.2771$ ($0.0201$);
     - Weekly HAR component $\alpha_w = 0.0771$ ($0.0360$);
     - Monthly HAR component $\alpha_m = 0.0972$ ($0.0162$);
     - Autoregressive GARCH component $\beta_1 = 0.4724$ ($0.0376$);
     - Negative return asymmetry (leverage) $\gamma = 0.1018$ ($0.0071$);
     - Continuous Gamma shape $\vartheta = 18.1070$ ($0.5981$);
     - Jump size distribution parameter $\zeta = 18.4562$ ($0.3884$);
     - Jump intensity parameters: $\phi_1 = 0.0076$, $\phi_2 = 0.9712$ ($0.0211$), $\phi_3 = 0.1420$ ($0.0491$);
     - Log-likelihood = $26,052.75$ (highest across all tested specifications; vs. $24,753.09$ for baseline MEM, $25,830.86$ for AMEM-HAR, and $25,816.78$ for AMEM-J).
   - Unconditional jump arrival rate $\phi_1 / (1 - \phi_2) \approx 0.26$, implying a liquidity jump occurs on average once every 4 trading days.
   - Contrast with daily Amihud: When estimated on daily Amihud (low frequency), $\vartheta = 1.2266$ (vs. $18.1070$ for realized Amihud), demonstrating that low-frequency error variance is $\sim 11\times$ larger due to observation noise.
2. **Out-of-Sample Forecast Evaluation (2015–2021, Table 3):**
   - Evaluated via Hansen et al. (2011) Model Confidence Set (MCS) under QLIKE loss at 10% significance:
     - **1-step ahead ($h=1$):** G-AMEM-HAR-J is the **unique** model in the superior set ($p = 1.0000$); all non-jump models are eliminated ($p \le 0.0488$).
     - **5-step ahead ($h=5$):** AMEM-HAR ($p = 1.0000$), AMEM-HAR-J ($p = 0.7437$), and AHAR ($p = 0.7437$) survive; jump effects diminish as illiquidity mean-reverts.
     - **22-step ahead ($h=22$):** Linear HAR is top-performing ($p = 1.0000$).
3. **Berkowitz Tail Coverage Evaluation (Table 4 & Table 6):**
   - Under standard realized Amihud: baseline continuous models (HAR, MEM) are rejected across nearly all quantiles ($p$-values $< 0.01$). Jump-augmented models (MEM-J class) maintain adequate coverage ($p > 0.10$).
   - Purging price jumps with Bipower Variation ($Illiq^C = BPV / \nu$, Table 6):
     - At 1% quantile out-of-sample: MEM-J Berkowitz $p$-value improves from $0.183$ to $0.447$;
     - AMEM-HAR-J $p$-value improves from $0.041$ to $0.536$.
4. **Logit Determinants of Tail Illiquidity Events (Table 7):**
   - Downward price dummy $D_{t-1}$ increases IlliQaR violation probability with marginal effect $+0.0158$ ($p < 0.05$) in lagged specification, and $+0.0544$ ($p < 0.01$) in contemporaneous specification.
   - VIX Decomposition: In contemporaneous regressions, the **risk aversion** component is positive and highly significant (coefficient $+0.0012$, $p < 0.01$ full sample; $+0.0021$, $p < 0.01$ out-of-sample), whereas the predictable **volatility uncertainty** coefficient is negative ($-152.96$ full sample, $-99.48$ out-of-sample).
5. **Cross-Sectional Individual Equities (25 U.S. Stocks, 2012–2024, Section 5):**
   - Intercept $\omega \in [0.007, 0.015]$ is orders of magnitude higher than index ($0.0001$), reflecting higher baseline illiquidity.
   - Jump size parameter $\zeta \in [4, 9]$ (vs. $18$ for index), while jump arrival intensity is lower ($1\% - 5\%$ vs. $22\%$ for index), demonstrating that single-stock liquidity dry-ups are rarer but substantially more severe in magnitude.
   - Individual stock IlliQaR violations strongly cluster during index-level IlliQaR stress regimes.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- Over multi-week horizons ($h \ge 5$ and $h=22$), jump-augmented models lose their forecasting edge to simple linear HAR specifications because liquidity shocks mean-revert rapidly, as demonstrated by the Model Confidence Set results in Table 3.
- Unadjusted realized Amihud can conflate price jumps with illiquidity jumps during scheduled macroeconomic announcements where prices jump without volume, leading to false-positive IlliQaR warnings unless Bipower Variation is explicitly used.
- None identified in the reviewed source beyond the reported limitations; absence is not evidence of no negative result.

## Falsification plan

1. **Backtest Design:** Implement the G-AMEM-HAR-J execution throttling and contagion hedging rules on an expanding walk-forward basis across S&P 500 constituents and liquid ETFs (SPY, QQQ, IWM) from 2015 to 2026.
2. **Control Baselines:** Compare against: (a) static volume-weighted execution; (b) linear HAR illiquidity prediction; (c) standard VIX-level threshold throttling.
3. **Falsification Thresholds (pre-declared):**
   - If dynamic $\text{IlliQaR}$ throttling fails to reduce total execution slippage and transaction costs by at least 15% during market stress periods (VIX $> 25$) relative to the static baseline, reject the operational execution hypothesis.
   - If out-of-sample Berkowitz coverage test rejects the null hypothesis of correct tail coverage ($p < 0.05$) across more than 20% of cross-sectional universe assets, reject the MEM-J distributional specification.
   - If index-level IlliQaR exceedances fail to predict single-stock liquidity dry-ups with an AUC $> 0.60$ over a 1-to-3 day forward window, reject the systemic contagion mechanism.
4. **Stress & Sensitivity Checks:** Perturb 5-minute sampling to 1-minute and 15-minute grids; evaluate performance during the March 2020 COVID crash and 2022 rate-hiking regime.

## Crypto portability

- **Portability:** `adapted` (research interpretation; original empirical evidence is derived exclusively from U.S. equities and the S&P 500 index).
- **Crypto-Specific Adaptation Requirements:**
  - **24/7 Continuous Trading:** Unlike equity sessions with fixed 09:30–16:00 boundaries, crypto markets trade continuously. Realized Amihud must be calculated on rolling 24-hour windows or fixed UTC 00:00–24:00 daily intervals.
  - **Perpetual Funding Rate & Liquidations:** Crypto liquidity evaporation is heavily driven by perpetual futures liquidation cascades and funding-rate stress rather than equity market hours. Adding perpetual liquidation volume and funding rate velocity into the MEM-J intensity process $\kappa_t$ is a necessary structural adaptation.
  - **Cross-Venue Fragmentation:** High-frequency volume and volatility must be aggregated across major venues (Binance, Bybit, OKX, Coinbase) or evaluated on a single primary venue to avoid distorted illiquidity signals caused by off-exchange volume migration.
  - **Stablecoin De-pegging Risk:** Quotation currency shocks (e.g. USDT or USDC volatility) can artificially distort realized return numerators, requiring fiat-referenced or coin-margined data auditing.

## Limitations

- `not independently reproduced`;
- **Sample Selection:** The empirical cross-section is restricted to 25 large-cap U.S. equities, which may understate illiquidity jump frequencies in small-cap or illiquid altcoin assets;
- **Actuarial/Risk Metric Focus:** The paper introduces a tail-risk metric and structural econometric model rather than an end-to-end P&L backtested trading strategy; trading rules represent research-proposed operationalizations;
- **Computational Overhead of Mixture Estimation:** Estimating the MEM-J with time-varying jump intensity requires maximum likelihood evaluation of modified Bessel functions, which is more computationally intensive than OLS estimation of linear HAR models.

## Implementation status

- `not-implemented`. Research capture only; no live, paper, or testnet trading modules have been constructed or authorized.

## Adoption boundary

- `research-only`, `not-approved`.
- This record captures external econometrics research on market microstructure and liquidity tail risk. It does not constitute authorization for deployment in PyBroker, Nautilus, paper, testnet, or live trading systems.

## Related Wiki records

- `[[quant/crypto-cross-sectional-amihud-illiquidity-premium-2026-08-31]]` — Baseline cross-sectional low-frequency Amihud illiquidity premium.
- `[[quant/crypto-cross-sectional-systematic-liquidity-risk-beta-2026-08-31]]` — Systematic liquidity risk beta framework (Acharya-Pedersen).
- `[[quant/crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01]]` — Microstructure early warning for sudden liquidity drain.

## Sources

1. Demetrio Lacava and Paolo Santucci de Magistris, *"Illiquidity at Risk"*, arXiv preprint `arXiv:2609.00943v1 [q-fin.RM, econ.EM]`, submitted September 1, 2026. DOI: [10.48550/arXiv.2609.00943](https://doi.org/10.48550/arXiv.2609.00943). Stable URL: [https://arxiv.org/abs/2609.00943](https://arxiv.org/abs/2609.00943). Full text HTML: [https://arxiv.org/html/2609.00943v1](https://arxiv.org/html/2609.00943v1).
2. Amihud, Y. (2002), "Illiquidity and stock returns: Cross-section and time-series effects", *Journal of Financial Markets* 5(1), 31–56. DOI: [10.1016/S1386-4181(01)00024-6](https://doi.org/10.1016/S1386-4181(01)00024-6).
3. Caporin, M., Rossi, E., & Santucci de Magistris, P. (2017), "Chasing volatility: A persistent multiplicative error model with jumps", *Journal of Econometrics* 198(1), 122–145. DOI: [10.1016/j.jeconom.2017.02.002](https://doi.org/10.1016/j.jeconom.2017.02.002).
4. Corsi, F. (2009), "A simple approximate long-memory model of realized volatility", *Journal of Financial Econometrics* 7(2), 174–196. DOI: [10.1093/jjfinec/nbp001](https://doi.org/10.1093/jjfinec/nbp001).
5. Barndorff-Nielsen, O. E. & Shephard, N. (2004), "Power and bipower variation with stochastic volatility and jumps", *Journal of Financial Econometrics* 2(1), 1–37. DOI: [10.1093/jjfinec/nbh001](https://doi.org/10.1093/jjfinec/nbh001).
6. Bekaert, G., Hoerova, M., & Lo Duca, M. (2013), "Risk, uncertainty and monetary policy", *Journal of Monetary Economics* 60(7), 771–788. DOI: [10.1016/j.jmoneco.2013.06.003](https://doi.org/10.1016/j.jmoneco.2013.06.003).
