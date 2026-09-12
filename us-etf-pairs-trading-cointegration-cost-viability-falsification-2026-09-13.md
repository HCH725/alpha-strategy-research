---
schema: strategy-research-record-v1
title: "US ETF and Fixed-Income Cointegration Pairs Trading: Empirical Falsification under Anti-Correlation of Cointegration and Cost Viability, Abstention Gate Artifact, and Fractional Nonstationarity"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - cointegration
  - etf-pairs
  - fixed-income
  - falsification
  - transaction-costs
  - benjamini-hochberg
  - kalman-filter
  - fractional-integration
status: research-only
confidence: high
source_as_of: 2026-08-22
sources:
  - "Michael M. Ross, 'Cost Viability and Cointegration Are Anti-Correlated in Liquid US ETF Pairs: A ground-truth-validated negative result for daily-frequency statistical arbitrage', 2026. DOI: https://doi.org/10.5281/zenodo.22059837. Repository: https://github.com/michaelmross/stat-arb/tree/771033c5e7084fb3693e83920c0936807a8c5e37"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# US ETF and Fixed-Income Cointegration Pairs Trading: Empirical Falsification under Anti-Correlation of Cointegration and Cost Viability, Abstention Gate Artifact, and Fractional Nonstationarity

## Provenance

- **Primary Source Research & Repository:** Michael M. Ross, *"Cost Viability and Cointegration Are Anti-Correlated in Liquid US ETF Pairs: A ground-truth-validated negative result for daily-frequency statistical arbitrage"*, 2026 (`source-reported`).
- **Canonical Repository URL:** [https://github.com/michaelmross/stat-arb](https://github.com/michaelmross/stat-arb) (`source-reported`).
- **Immutable Commit SHA:** `771033c5e7084fb3693e83920c0936807a8c5e37` (`source-reported`).
- **Canonical DOI:** [10.5281/zenodo.22059837](https://doi.org/10.5281/zenodo.22059837) (`source-reported`).
- **License:** MIT License for source code; CC BY 4.0 for research note and figures (`source-reported`).
- **Data As-Of Date:** 2026-08-21 (ETF panel from Tiingo, end-of-day adjusted closes 2010-01-04 to 2026-08-21; 1920 out-of-sample evaluation days from 2019-01-02 onward) (`source-reported`).
- **Primary Source Code Paths Audited:**
  - `code/scan.py`: Two-stage discovery/evaluation protocol, Benjamini–Hochberg FDR control, cost-viability ratio, noise-dominated ACF diagnostic (`source-reported`).
  - `code/backtest.py`: Walk-forward z-score backtester, frozen parameter out-of-sample execution, dollar-neutral leg weighting, tradability gate (`source-reported`).
  - `code/coint.py`: Engle–Granger two-step regression with MacKinnon (2010) cointegration response-surface critical values (`source-reported`).
  - `code/ou.py`: Exact conditional MLE for Ornstein–Uhlenbeck parameters, half-life, and stationary standard deviation (`source-reported`).
  - `code/kalman_variant.py`: Ungated online Kalman filter innovation trading variant and zero-cost attribution (`source-reported`).
  - `code/fractional_census.py`: Exact Local Whittle (Shimotsu–Phillips) memory-parameter ($d$) census across 130 spreads (`source-reported`).
  - `code/check_claims.py`: Adversarial mechanical confound tests, power sweeps, and OOS Sharpe t-statistics (`source-reported`).
  - `data/scan_v2.json`: Archived scan and walk-forward backtest outputs for 130 candidate pairs (`source-reported`).
  - `data/kalman_cost_attribution.json`: Friction-ablation decomposition for online Kalman variant (`source-reported`).
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `michaelmross/stat-arb`, Zenodo DOI `10.5281/zenodo.22059837`, Michael M. Ross, or the anti-correlation between cointegration p-values and cost viability. Adjacent records evaluating ETF pairs trading (e.g. `johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md` based on Shaunak Batra's `BasketTradingBO`) evaluate Johansen-based vector error-correction models on 60 pairs without testing the structural trade-off between statistical cointegration strength and cost viability, without fractional memory integration ($d$-census), without ungated online Kalman filter ablation of the abstention effect, and without March 2020 stress dislocation audits.

## Economic mechanism

### Source-reported

1. **The Theoretical Cointegration Arbitrage Premise:**
   Statistical arbitrage on structurally related ETF pairs (same-index wrappers, sector funds vs broad market parents, currency-hedged vs unhedged equivalents, and physical production margins) assumes that an underlying economic tether—such as authorized participant (AP) creation-redemption arbitrage or physical input-output substitution—restores price parity whenever supply-demand shocks drive prices apart. When log-prices $p_t$ and $q_t$ share a common stochastic trend, the spread $S_t = p_t - \alpha - \beta q_t$ is assumed to be an Ornstein–Uhlenbeck (OU) mean-reverting process with stationary variance $\sigma_S^2 = \sigma^2 / (2\kappa)$ and finite half-life $\tau_{1/2} = \ln(2)/\kappa$.

2. **The Fundamental Trade-off: Anti-Correlation of Cointegration and Cost Viability:**
   Ross (2026) demonstrates that in liquid US ETF pairs, cointegration strength and cost viability are fundamentally anti-correlated. Across 98 candidate pairs with sufficient history, the Spearman rank correlation between the Engle–Granger cointegration p-value and the cost-viability ratio is **+0.446 ($p = 4.2 \times 10^{-6}$)**. Pairs with strong, unambiguous cointegration (low p-values, e.g., same-index large-cap trackers SPY/IVV, SPY/VOO, IVV/VOO) have tiny spreads (5.3 to 12.0 bps stationary standard deviation) that are heavily consumed by execution frictions. Conversely, pairs with wide spreads that comfortably exceed trading costs (sector/parent, HOLDRs, cross-family pairs) exhibit weak, transient, or non-existent cointegration that fails statistical tests.

3. **Fractional Nonstationarity ($d \approx 0.51$):**
   Estimating the fractional integration memory parameter $d$ via Exact Local Whittle (Shimotsu–Phillips) across all 130 tested ETF spreads reveals that the 14 Benjamini–Hochberg discoveries possess a median memory parameter $\hat{d} = 0.51$. Because $\hat{d} > 0.50$, these spreads lie on the nonstationary side of the boundary: they are mean-reverting only over multi-month or multi-quarter horizons, not on the daily frequency required to outpace transaction fees.

4. **The Abstention Gate Artifact:**
   Standard walk-forward backtests reporting near-zero Sharpe ratios (median out-of-sample Sharpe of 0.00 to -0.08) create an illusion of low-risk equilibrium. Ross (2026) shows through an ungated online Kalman filter variant that this benign result is an *abstention artifact*: the strategy avoided severe losses solely because its tradability gate (requiring $p < 0.05$ and $1.0 < \tau_{1/2} < 60.0$ days) kept capital idle ~93% of the time. When the gate was removed and the system was forced to continuously adapt and trade (time in market 34.9%), the median out-of-sample Sharpe dropped to **-0.15**, with 3 of 10 pairs experiencing statistically significant negative performance ($|t| > 1.96$, reaching $t = -15.64$ on VCIT/IGIB).

5. **Structural Tether Breakdown in Extreme Regimes:**
   During the March 2020 liquidity shock, the NAV tether failed precisely where it was expected to be strongest: all 10 evaluated bond ETF pairs breached their 4$\sigma$ emergency stop, with peak z-scores ranging from **9.5$\sigma$ to 72.3$\sigma$**. On 2020-03-13, BND closed +4.2% while SPAB closed -0.6%—a single-day 480 bps divergence between two funds tracking near-identical aggregate bond indices against a pre-crisis spread standard deviation of 6.6 bps.

### Research interpretation

The empirical evidence directly falsifies the hypothesis that daily-frequency cointegration z-score trading on liquid US ETF pairs generates positive risk-adjusted excess returns net of realistic execution friction (2 bps/leg one-way). The ostensible edge in traditional backtests is driven by three distinct structural failures:
1. **Adverse Selection of Spreads:** A market equilibrium effect where cointegration is enforceable only when spreads are too narrow to trade profitably after retail/institutional brokerage fees.
2. **Abstention Shielding:** Strategies appear stable in backtests because conservative pre-trade gates reject trades during drifting regimes, resulting in near-zero active exposure rather than positive alpha.
3. **Slow Fractional Memory:** Cointegration tests (Engle–Granger, Johansen) mistake long-memory mean reversion ($d \approx 0.51$) for stationary $I(0)$ mean reversion, leading to severe holding-period mismatch where positions incur negative carry and drift before any reversion occurs.

## Signal

The normalized strategy logic follows the two-stage protocol implemented in `code/scan.py` and `code/backtest.py` (`source-reported`):

### 1. Discovery and Estimation Protocol (`source-reported`)
- **Sample Split:** Pre-split into an in-sample discovery window ($\le 2018\text{-}12\text{-}31$) and an out-of-sample evaluation period ($> 2018\text{-}12\text{-}31$, 1920 trading days).
- **Hedge Ratio Fitting:** Engle–Granger two-step regression of log-prices:
  $$\ln(P_t) = \alpha + \beta \ln(Q_t) + S_t$$
  Estimated via ordinary least squares (OLS) with a constant.
- **Cointegration Testing:** Augmented Dickey-Fuller unit-root test on spread residuals $S_t$ with MacKinnon (2010) response-surface p-values (via `statsmodels.tsa.stattools.coint`) with `autolag="aic"` (`source-reported`).
- **Multiple Testing Correction:** Benjamini–Hochberg False Discovery Rate (FDR) control at nominal false discovery rate $q = 0.05$ (`source-reported`).
- **Ornstein–Uhlenbeck Estimation:** Discretized Gaussian AR(1) conditional MLE:
  $$S_{t+1} = \mu + e^{-\kappa \Delta t}(S_t - \mu) + \epsilon_t, \quad \epsilon_t \sim \mathcal{N}\left(0, \frac{\sigma^2 (1 - e^{-2\kappa \Delta t})}{2\kappa}\right)$$
  Yielding mean-reversion speed $\kappa$, equilibrium mean $\mu$, half-life $\tau_{1/2} = \ln(2) / (\kappa \Delta t)$ steps, and stationary standard deviation $\sigma_S = \sigma / \sqrt{2\kappa}$ (`source-reported`).
- **Cost-Viability Ratio ($CVR$):**
  $$CVR = \frac{\text{Expected capture per round trip}}{\text{Round-trip cost}} = \frac{1.5 \cdot \sigma_S / (1 + |\beta|)}{2 \cdot \text{cost\_bps} / 10^4}$$
  Evaluated for an entry at $|z| = 2.0$ and exit at $|z| = 0.5$. If $CVR < 1.0$, the spread cannot cover round-trip transaction costs even under perfect mean reversion (`source-reported`).
- **Noise-Dominated Flag:** Spread autocorrelation check: flagged as noise-dominated if $\text{ACF}(1) > 0.02$ and $\text{ACF}(40) / \text{ACF}(1) > 0.50$ (flat ACF indicates a unit-root process contaminated by white noise rather than an exponential AR(1) decay) (`source-reported`).

### 2. Walk-Forward Execution and Tradability Gate (`source-reported`)
- **Rolling Window Parameters:** In-sample training window $L_{\text{train}} = 504$ trading days (~2 years); out-of-sample trading window $L_{\text{trade}} = 126$ trading days (~6 months) (`source-reported`).
- **Tradability Gate:** Re-evaluated at every 126-day refit. A pair is tradable in the subsequent window if and only if:
  1. Engle–Granger p-value $p < 0.05$ (`source-reported`).
  2. Half-life is bounded: $1.0 < \tau_{1/2} < 60.0$ trading days (`source-reported`).
  If either condition fails, the strategy stays in cash ($x_t = 0$) for that 126-day block (`source-reported`).
- **Spread Normalization:** Using parameters $\alpha, \beta, \mu, \sigma_S$ frozen from the in-sample window:
  $$z_t = \frac{\ln(P_t) - \alpha - \beta \ln(Q_t) - \mu}{\sigma_S}$$
- **State-Machine Trading Logic (`source-reported`):**
  - **Flat ($x_t = 0$):**
    - If $z_t > 2.0$: Enter short spread ($x_{t+1} = -1.0$).
    - If $z_t < -2.0$: Enter long spread ($x_{t+1} = +1.0$).
  - **In Position ($x_t \neq 0$):**
    - Normal Exit: Exit to cash ($x_{t+1} = 0.0$) when $|z_t| < 0.5$.
    - Emergency Stop: Exit to cash ($x_{t+1} = 0.0$) when $|z_t| > 4.0$.
- **Leg Allocation & Dollar Neutrality (`source-reported`):**
  For spread position state $x_t \in \{-1, 0, +1\}$:
  $$w_{P, t} = \frac{x_t}{1 + |\beta|}, \quad w_{Q, t} = -\frac{x_t \cdot \beta}{1 + |\beta|}$$
  Total gross notional exposure $|w_{P, t}| + |w_{Q, t}| = |x_t| \le 1.0$ (unit capital) (`source-reported`).
- **Execution Timing:** Signals observed at day $t$ close apply to returns earned from close $t$ to close $t+1$ (`source-reported`).

### 3. Ungated Online Kalman Filter Variant (`source-reported`)
- **State Evolution:** Random walk for time-varying vector $\mathbf{x}_t = [\alpha_t, \beta_t]^T$:
  $$\mathbf{x}_t = \mathbf{x}_{t-1} + \mathbf{w}_t, \quad \mathbf{w}_t \sim \mathcal{N}\left(\mathbf{0}, \frac{\delta}{1 - \delta} r \mathbf{I}_2\right)$$
- **Observation Model:** $\ln(P_t) = [1, \ln(Q_t)] \mathbf{x}_t + v_t, \quad v_t \sim \mathcal{N}(0, r)$.
- **State Noise Scale:** $\delta = 10^{-6}$ (strictly calibrated on synthetic ground truth only; never tuned on real data) (`source-reported`).
- **Burn-In Initialization:** 252-day OLS to initialize $\mathbf{x}_0$ and observation variance $r = \max(\text{Var}(\text{residuals}), 10^{-10})$ (`source-reported`).
- **Signal:** Standardized one-step-ahead innovation $z_t = e_t / \sqrt{S_t}$, where $e_t = \ln(P_t) - \hat{y}_t$ and $S_t = \mathbf{H}_t \mathbf{P}_{t|t-1} \mathbf{H}_t^T + r$ (`source-reported`).
- **Gating:** No tradability gate; continuous execution with turnover fee charged on all position adjustments and beta drift rebalancing (`source-reported`).

## Required data

- **Universe:** 114 US ETF tickers spanning 136 structural candidate pairs (98 evaluated in v1; 130 evaluated in v2 with fixed-income cohort) (`source-reported`).
  - Equity broad index: SPY, IVV, VOO, SPLG, QQQ, QQQM, IWM, VTWO, IJR, DIA, VTI, ITOT, SCHB, MDY, IJH (`source-reported`).
  - International equity: EFA, IEFA, VEA, SCHF, EEM, IEMG, VWO, SPEM (`source-reported`).
  - Fixed-income duration-disciplined buckets:
    - Aggregate bond: SCHZ, AGG, BND, SPAB (`source-reported`).
    - Long Treasury: TLT, VGLT, SPTL (`source-reported`).
    - Intermediate Treasury: IEF, VGIT, SPTI (`source-reported`).
    - Short Treasury: SHY, VGSH, SCHO, SPTS (`source-reported`).
    - TIPS broad: TIP, SCHP, SPIP (`source-reported`).
    - TIPS short: VTIP, STIP (`source-reported`).
    - IG corporate intermediate: VCIT, IGIB, SPIB (`source-reported`).
    - IG corporate short: VCSH, IGSB, SPSB (`source-reported`).
    - Mortgage-backed securities (MBS): MBB, VMBS, SPMB (`source-reported`).
    - EM USD sovereign: EMB, VWOB, PCY (`source-reported`).
    - Municipal: MUB, VTEB (`source-reported`).
    - Preferred stock: PFF, PGX, PSK (`source-reported`).
    - High yield: HYG, JNK, USHY (`source-reported`).
  - Commodities & real estate: GLD, IAU, GLDM, SGOL, SLV, SIVR, VNQ, IYR, SCHH, RWR (`source-reported`).
  - Controls (negative controls): GLD/SPY, TLT/SPY, etc. (`source-reported`).
- **Data Source:** Tiingo API (`source-reported`).
- **Field Required:** `adjClose` (end-of-day adjusted close incorporating splits and cash dividends) (`source-reported`).
  - *Data Integrity Caveat:* Unadjusted closes or split-only closes (e.g. raw Stooq) cannot be used; differing ex-dividend dates introduce artificial sawtooth jumps into log-spreads that mimic mean reversion but are unexecutable (`source-reported`).
- **Sample Range:** 2010-01-04 to 2026-08-21 (`source-reported`).
- **Sampling Frequency:** Daily closes (`source-reported`).
- **Timezone/Alignment:** US Eastern Time close (`source-reported`).
- **Missing Data Handling:** Pairwise inner join; pairs with fewer than 756 observations in the discovery window or fewer than 1920 observations in out-of-sample are dropped (`source-reported`).

## Execution assumptions

- **Execution Model:** End-of-day execution; signals computed at close $t$ take effect at close $t$ for return accrual from $t$ to $t+1$ (`source-reported`).
- **Transaction Costs:** 2.0 basis points per leg one-way (0.0002) on traded notional (`source-reported`).
  - Round-trip spread trade cost = $2 \times 2.0\text{ bps} = 4.0\text{ bps}$ total notional across both legs (`source-reported`).
  - In the Kalman variant, costs are assessed on all turnover including continuous $\beta_t$ rebalancing while holding positions (`source-reported`).
- **Order Type:** Assumed executed at close price without fill delay or market impact (`source-reported`).
- **Short Borrow:** Unconstrained borrow assumed available at zero borrow fee (`source-reported`).
- **Leverage / Margin:** Gross notional strictly bounded by 1.0 (unit capital; cash unencumbered) (`source-reported`).
- **Slippage Model:** 0.0 bps explicit slippage modeled beyond the 2.0 bps/leg fee (`source-reported`). *Scout note: in actual live trading, execution at exact close entails additional adverse selection or market-on-close (MOC) fees* (`research-proposed`).

## Evidence

### Source-reported

All statistics below trace directly to committed JSON artifacts and code execution in `michaelmross/stat-arb` (commit `771033c5e`):

1. **Empirical Anti-Correlation between Cointegration and Cost Viability:**
   Across all 98 testable structural pairs in scan v1:
   - Spearman rank correlation: $\rho = +0.446$ ($p = 4.2 \times 10^{-6}$, $n = 98$) (`source-reported`).
   - Pairs with tightest cointegration had median stationary standard deviation of only 5–12 bps, rendering $CVR < 1.0$ at 2 bps/leg costs (`source-reported`).
   - Breakdown by relation type (`data/scan_full.json`):
     - `same_index` ($n=43$): Median p-value = 0.29, median edge ratio = 9.2, median half-life = 11.8 days, 38/43 noise-dominated (`source-reported`).
     - `sector_parent` ($n=30$): Median p-value = 0.36, median edge ratio = 100.2, median half-life = 115.4 days, 30/30 noise-dominated (`source-reported`).
     - `hedged` ($n=11$): Median p-value = 0.52, median edge ratio = 90.3, median half-life = 57.1 days, 10/11 noise-dominated (`source-reported`).
     - `holdrs` ($n=10$): Median p-value = 0.54, median edge ratio = 152.8, median half-life = 141.7 days, 10/10 noise-dominated (`source-reported`).
     - `control` ($n=4$): Median p-value = 0.38, median edge ratio = 397.2, median half-life = 163.4 days, 4/4 noise-dominated (`source-reported`).

2. **Multiple Testing Screen (Benjamini–Hochberg at $q = 0.05$):**
   - In scan v1 ($n=98$): 17 pairs passed raw $p < 0.05$; only **8 pairs survived BH correction**—all 8 were `same_index` (`source-reported`).
   - In scan v2 ($n=130$, adding fixed-income cohort): 28 pairs passed raw $p < 0.05$; **14 pairs survived BH correction** (8 from v1 + 6 new fixed-income pairs: SCHZ/SPAB, SCHZ/AGG, VGSH/SCHO, IGSB/SPSB, VTIP/STIP, VCIT/IGIB) (`source-reported`).

3. **Out-of-Sample Walk-Forward Backtest Performance (2019–2026, 1920 days):**
   Out of 14 discoveries, only 10 cleared the half-life gate ($1.0 < \tau_{1/2} < 60.0$) and entered the walk-forward backtest (`data/scan_v2.json`):
   - **Median Out-of-Sample Sharpe Ratio:** **0.00** (against v1's -0.08) (`source-reported`).
   - Pair-level results:
     - `VTI/SCHB`: Sharpe = +0.25, Ann. Ret = +0.0067%, Ann. Vol = 0.027%, Max DD = 0.02%, Time in Market = 0.05% (only 5 round trips in 7.6 years) (`source-reported`).
     - `BND/SPAB`: Sharpe = +0.15, Ann. Ret = +0.032%, Ann. Vol = 0.21%, Max DD = 0.34%, Time in Market = 13.0%, 39 round trips (`source-reported`).
     - `AGG/SPAB`: Sharpe = -0.08, Ann. Ret = -0.011%, Ann. Vol = 0.14%, Max DD = 0.33%, Time in Market = 3.1%, 24 round trips (`source-reported`).
     - `SCHZ/AGG`: Sharpe = -0.13, Ann. Ret = -0.014%, Ann. Vol = 0.11%, Max DD = 0.29%, Time in Market = 5.4%, 20 round trips (`source-reported`).
     - `AGG/BND`: Sharpe = -0.37, Ann. Ret = -0.17%, Ann. Vol = 0.47%, Max DD = 1.52%, Time in Market = 16.8%, 53 round trips (`source-reported`).
     - `SCHZ/SPAB`: Sharpe = 0.00, Ann. Ret = 0.00%, Time in Market = 0.00% (`source-reported`).
     - `IGSB/SPSB`: Sharpe = 0.00, Ann. Ret = 0.00%, Time in Market = 0.00% (`source-reported`).
     - `VTIP/STIP`: Sharpe = 0.00, Ann. Ret = 0.00%, Time in Market = 0.00% (`source-reported`).
     - `VCIT/IGIB`: Sharpe = +0.53, Ann. Ret = +0.25%, Ann. Vol = 0.48%, Max DD = 0.28%, Time in Market = 11.4% ($t = 1.46$, not statistically significant, flagged noise-dominated) (`source-reported`).
     - `LQD/USIG`: Sharpe = **-1.19**, Ann. Ret = -0.46%, Ann. Vol = 0.39%, Max DD = 3.57%, Time in Market = 11.3%, 67 round trips ($t = -3.29$, statistically significant *negative*) (`source-reported`).

4. **Fractional Integration Memory Parameter Census ($d$-Census across 130 spreads):**
   - Exact Local Whittle estimates (`data/fractional_census_results.json`):
     - All tested spreads ($n=130$): Median $\hat{d} = 0.93$ (`source-reported`).
     - BH discoveries ($n=14$): Median $\hat{d} = \mathbf{0.51}$ (`source-reported`).
     - Non-discoveries ($n=116$): Median $\hat{d} = 0.94$ (`source-reported`).
     - Negative controls ($n=4$): Median $\hat{d} = 1.01$ (`source-reported`).
   - Findings: Even the best statistical discoveries have $\hat{d} > 0.50$, proving they are nonstationary and revert too slowly to trade at daily frequencies.

5. **Ablation: The Gate Attribution in Online Kalman Filtering:**
   Removing the tradability gate and running an online Kalman filter on the same 10 pairs (`data/kalman_cost_attribution.json`):
   - Median OOS Sharpe collapsed from 0.00 to **-0.15** (`source-reported`).
   - Mean time in market rose from ~7% to **34.9%** (`source-reported`).
   - 3 of 10 pairs exhibited statistically significant negative performance ($|t| > 1.96$): `VTIP/STIP` ($t = -2.53$), `IGSB/SPSB` ($t = -11.07$), and `VCIT/IGIB` ($t = -15.64$, where Sharpe collapsed from +0.53 to **-5.67**) (`source-reported`).
   - Friction decomposition: `churn` (overtrading on noise) accounted for the performance destruction on 9 of 10 pairs; `adverse level` accounted for the remaining pair (`source-reported`).

6. **Crisis Dislocation (March 2020 Stress Test):**
   - All 10 bond ETF pairs breached the 4$\sigma$ stop (`source-reported`).
   - Peak dislocations reached **9.5$\sigma$ to 72.3$\sigma$** (`source-reported`).
   - On 2020-03-13, BND (+4.2%) and SPAB (-0.6%) diverged by 480 bps in a single session against a 6.6 bps pre-crisis standard deviation (`source-reported`).

### Independently reproduced

Not independently reproduced. All metrics and findings represent source-reported results from Michael M. Ross (2026, commit `771033c5e7084fb3693e83920c0936807a8c5e37`, Zenodo DOI `10.5281/zenodo.22059837`).

### Negative evidence

- The entire study is an explicit, comprehensive negative finding: statistical cointegration does not translate to tradable alpha in liquid US ETF pairs.
- The only statistically significant result across 130 candidate pairs over 7.6 out-of-sample years was negative (LQD/USIG, Sharpe -1.19, $t = -3.29$).
- Removing the tradability gate in the Kalman filter variant increased market participation 5x but resulted in severe systematic capital destruction (Sharpe -5.67 on VCIT/IGIB).
- Production margins (crack 3:2:1 and soybean board crush) show that physical arbitrage anchors multi-quarter levels but exhibits half-lives of ~160 days, yielding zero tradable daily reversion (0 round trips for board crush over 7 years).

## Falsification plan

To falsify the conclusion that daily-frequency ETF cointegration stat-arb is unviable, an alternative implementation would need to demonstrate statistically significant positive risk-adjusted returns after costs under the following pre-declared criteria:

1. **Transaction Cost Invariance:**
   - *Test:* Evaluate candidate ETF pairs under realistic institutional fee schedules (minimum 1.5 bps/leg one-way plus realistic market-on-close slippage).
   - *Falsification Criterion:* If the net out-of-sample Sharpe ratio exceeds 1.0 with $t > 2.0$ across a pre-registered universe of at least 20 pairs, Ross's negative viability thesis is falsified (`research-defined falsification threshold`).

2. **Fractional Stationarity Verification:**
   - *Test:* Pre-screen spreads for true stationarity using Exact Local Whittle with memory parameter $\hat{d} < 0.40$ prior to backtesting.
   - *Falsification Criterion:* If pairs selected with $\hat{d} < 0.40$ generate positive net Sharpe while pairs with $\hat{d} \in [0.45, 0.55]$ fail, it confirms that fractional memory filtering resolves the look-ahead/slow-reversion defect (`research-defined falsification threshold`).

3. **Intraday Horizon / Microstructure Execution:**
   - *Test:* Port the same-index cointegration thesis from daily closes to intraday 1-minute or 5-minute bars with limit-order execution (capturing half the bid-ask spread rather than paying 2 bps taker fee).
   - *Falsification Criterion:* If intraday market-making/stat-arb on SPY/IVV or BND/SPAB achieves annualized Sharpe > 1.5 net of exchange taker fees and maker rebates, it proves the edge exists at higher frequencies even if dead at daily closes (`research-defined falsification threshold`).

## Crypto portability

- **Portability Status:** `adapted / unproven` (`research-proposed`).
- **Mechanism Mapping:**
  The structural analogue to ETF pairs in crypto is:
  1. Wrapped vs native tokens (e.g. WBTC vs BTC, cbBTC vs BTC, stETH vs WETH) (`research-proposed`).
  2. Cross-exchange perpetual contracts on the same underlying (e.g. BTC-USDT on Binance vs OKX vs Bybit vs Hyperliquid) (`research-proposed`).
  3. Stablecoin pairs with shared collateral or redemption mechanisms (e.g. USDT, USDC, USDS, PYUSD) (`research-proposed`).
- **Crypto-Specific Divergence & Hazards:**
  - *Absence of Authorized Participant Legal Arbitrage:* Crypto tokens lack legally binding redemption covenants like the 1940 Act ETF creation-redemption mechanism. De-pegging events (e.g. stETH in June 2022, USDC in March 2023) can produce persistent multi-month dislocations exceeding 50$\sigma$ (`research-proposed`).
  - *Funding Rate Asymmetry:* Cross-exchange perpetual pairs stat-arb incurs continuous funding payments. If the spread remains wide for extended periods, cumulative funding drag easily exceeds the mean-reversion profit (`research-proposed`).
  - *24/7 Liquidity Gaps and Flash Crashes:* Unlike regulated US ETF markets with trading halts and auction closes, crypto pairs experience sudden cascade liquidations that trigger stop-losses at the absolute worst price (`research-proposed`).
  - *Execution Friction:* While VIP taker fees on major centralized exchanges range from 1.5 to 3.0 bps, retail taker fees (4 to 5 bps) make daily-frequency pairs trading even more severely cost-prohibitive than in equities (`research-proposed`).

## Limitations

- **Not Independently Reproduced:** Relies on third-party empirical code, archived JSON outputs, and research notes from Michael M. Ross (2026).
- **Daily Frequency Only:** The study examines end-of-day closes. It does not evaluate intraday, tick-level, or high-frequency order-book mean reversion.
- **Fixed Cost Assumption:** Assumes a flat 2.0 bps/leg one-way cost. While appropriate for retail and mid-sized institutional accounts, market makers or high-volume APs may operate at lower net execution costs (e.g. rebate tiers).
- **Execution Fill Simplicity:** Assumes fills at exact closing marks without market impact or execution shortfall modeling.
- **Short-Sale Availability:** Assumes frictionless shorting on all ETF legs, whereas hard-to-borrow fees or borrow recalls can occur during severe market dislocations (e.g. March 2020).

## Implementation status

`not-implemented`. This strategy record is a research capture documenting an empirical negative result. No implementation has been created in NautilusTrader, PyBroker, paper trading, testnet, or live production.

## Adoption boundary

`research-only` / `not-approved`. This record serves as a benchmark and negative warning for any subsequent statistical arbitrage or pairs-trading research. Ingestion into the research pool does not constitute authorization for deployment or capital allocation.

## Related Wiki records

- `johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md` — Shaunak Batra (2026), BasketTradingBO: Johansen cointegration on 60 ETF pairs showing net exposure drift and friction asymmetry.
- `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md` — Multiple-testing corrections and comparison of Johansen vs Engle-Granger stat-arb in US equities.
- `tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12.md` — Gite (2026), TETHER pairs trading with FDR and half-life dynamic beta controls.
- `eurostoxx-pca-ou-stat-arb-trading-time-friction-falsification-2026-09-12.md` — Simone Cerrone (2026), Avellaneda-Lee PCA-OU stat-arb on European equities under trading friction.

## Sources

1. Michael M. Ross, *"Cost Viability and Cointegration Are Anti-Correlated in Liquid US ETF Pairs: A ground-truth-validated negative result for daily-frequency statistical arbitrage"*, 2026. DOI: [10.5281/zenodo.22059837](https://doi.org/10.5281/zenodo.22059837).
2. Primary GitHub Source Repository: [https://github.com/michaelmross/stat-arb](https://github.com/michaelmross/stat-arb) (commit `771033c5e7084fb3693e83920c0936807a8c5e37`).
3. Primary Code & Data Artifacts:
   - `code/scan.py`: Two-stage protocol, Benjamini-Hochberg FDR, cost-viability ratio, noise-dominated ACF check (`source-reported`).
   - `code/backtest.py`: Walk-forward z-score backtest, dollar-neutral leg weighting, tradability gate (`source-reported`).
   - `code/coint.py`: Engle-Granger two-step regression with MacKinnon (2010) critical values (`source-reported`).
   - `code/ou.py`: Exact Gaussian AR(1) conditional MLE for Ornstein-Uhlenbeck parameters (`source-reported`).
   - `code/kalman_variant.py`: Online Kalman filter innovation trading variant and zero-cost attribution (`source-reported`).
   - `code/fractional_census.py`: Exact Local Whittle memory parameter estimation across 130 spreads (`source-reported`).
   - `code/check_claims.py`: Mechanical confound check, power sweep, and t-statistic tests (`source-reported`).
   - `data/scan_v2.json`: Archived full evaluation results for 130 candidate pairs (`source-reported`).
   - `data/kalman_cost_attribution.json`: Cost-drag decomposition for online Kalman filter variant (`source-reported`).
