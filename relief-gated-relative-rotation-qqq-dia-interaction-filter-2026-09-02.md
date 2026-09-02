---
schema: strategy-research-record-v1
title: "Relief-Gated Relative Rotation for QQQ-DIA Allocation: Globally Screened Relative States, Fixed Position Mapping, and Incremental Interaction Admission"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - dynamic-asset-allocation
  - etf-portfolios
  - relative-value
  - growth-vs-value
  - macro-conditioning
  - interaction-screening
  - walk-forward-validation
  - newey-west-hac
  - turnover-control
status: research-only
confidence: high
source_as_of: 2026-07-07
sources:
  - "Zheli Xiong, 'Relief-Gated Relative Rotation for QQQ-DIA Allocation: Globally Screened Relative States, Fixed Position Mapping, Incremental Interaction Admission, and Walk-Forward Validation', arXiv:2607.06117v1 [q-fin.PM], July 7, 2026. DOI: https://doi.org/10.48550/arXiv.2607.06117. GitHub: https://github.com/shaun19920309/Relief-Gated-Relative-Rotation-for-QQQ-DIA-Allocation, commit a1e44c2e7d4cf23f63a8746c139f6265882291c0."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Relief-Gated Relative Rotation for QQQ-DIA Allocation: Globally Screened Relative States, Fixed Position Mapping, and Incremental Interaction Admission

## Provenance

- **Canonical Academic Source:** Zheli Xiong, *"Relief-Gated Relative Rotation for QQQ–DIA Allocation: Globally Screened Relative States, Fixed Position Mapping, Incremental Interaction Admission, and Walk-Forward Validation"*, arXiv preprint `arXiv:2607.06117v1 [q-fin.PM]`, submitted July 7, 2026.
- **Canonical DOI:** [10.48550/arXiv.2607.06117](https://doi.org/10.48550/arXiv.2607.06117).
- **Stable Source URLs:**
  - Abstract: [https://arxiv.org/abs/2607.06117](https://arxiv.org/abs/2607.06117)
  - Full Text HTML: [https://arxiv.org/html/2607.06117v1](https://arxiv.org/html/2607.06117v1)
  - Full Text PDF: [https://arxiv.org/pdf/2607.06117v1](https://arxiv.org/pdf/2607.06117v1)
- **Evaluation Code Scaffold & Replication Package:**
  - GitHub Repository: [https://github.com/shaun19920309/Relief-Gated-Relative-Rotation-for-QQQ-DIA-Allocation](https://github.com/shaun19920309/Relief-Gated-Relative-Rotation-for-QQQ-DIA-Allocation)
  - Immutable Commit SHA: `a1e44c2e7d4cf23f63a8746c139f6265882291c0`
  - Core Execution Script: `phase3/scripts/run_relief_gated_relative_rotation.py`
  - Input Feature Dataset: `data/phase3/qqq_dia_relative_weight_v1/inputs/phase3_qqq_dia_feature_panel.csv`
  - Verified Benchmark Tables: `data/phase3/qqq_dia_relative_weight_v1/tables/rgrr_policy_comparison.csv`
- **Sample Time Horizon:**
  - Raw data span: 2006-06-22 to 2026-07-02.
  - Aligned evaluation start: 2008-07-25 (actual rolling strategy start: 2009-07-27 post-756-day rolling training and 252-day expanding warmup) to 2026-07-02 (4,240 trading days).

## Economic mechanism

### Source-reported

1. **Growth vs. Value Relative Leadership Cycles:** In technology-driven bull markets, growth-heavy technology assets (proxied by the Nasdaq-100 ETF, QQQ) experience extended periods of strong relative outperformance over dividend/value/industrial-heavy assets (proxied by the Dow Jones Industrial Average ETF, DIA). However, following extended relative run-ups, windows emerge where growth momentum stalls and value/industrials catch up.
2. **Failure of Naive Standalone Reversal:** A mechanical contrarian rule that simply fades QQQ whenever it has led DIA and begins to stall fails out-of-sample. In univariate quartile diagnostic tests across 63-day forward horizons, the highest trailing 126-day relative momentum bucket (`rel_trailing_126d_z`) generates the lowest subsequent mean relative return, yet standalone relative reversal triggers frequent premature rotations during secular technology trends.
3. **Macro Relief-Gated Asymmetric Rotation:** The central empirical finding of the study is that relative reversal states become economically tradable only when conditioned upon macroeconomic relief or broad equity market distress states:
   - *Rate Relief (`rate_relief`):* Falling 10-year Treasury yields alleviate duration and discount rate compression on high-multiple growth equities.
   - *Broad Market Drawdown (`spy_drawdown`):* Deep S&P 500 corrections create asymmetric rebound elasticity where high-beta growth stocks recover faster once selling pressure exhausts.
   - *Volatility Stress Normalization (`high_vix`, `low_vix`, `vix_relief`):* Transitioning from peak volatility spikes into volatility contraction confirms supportive market liquidity.
   - *Credit Relief (`credit_relief`):* Narrowing corporate high-yield credit spreads confirms that declining yields reflect healthy monetary easing rather than systemic credit default panic.
4. **Separation of Signal Vocabulary from Portfolio Allocation:** The author enforces a strict methodological boundary: statistical screening identifies an invariant vocabulary of main effects and interactions globally, while the rolling walk-forward layer re-tunes only the combination weights ($\\lambda$) across admitted families under a turnover penalty, rather than re-screening candidate features or altering the position mapping inside the backtest loop.

### Research interpretation

- **Factor Timing via Macro Conditioning:** The QQQ–DIA relative return is fundamentally a factor spread portfolio: Fama–French five-factor plus Carhart momentum regressions confirm that QQQ has higher market beta ($\\beta_{\\text{MKT}} > 1$) and strong negative value exposure ($\\beta_{\\text{HML}} < 0$), whereas DIA is heavily loaded on value, operating profitability, and investment factors. Dynamically allocating between QQQ and DIA is therefore a systematic timing of the growth-versus-value factor premium conditioned on monetary and volatility regimes.
- **Convexity and Gating Benefits:** Conditioning relative reversal on rate relief acts as a high-order filter: during stagflationary rate-shock environments (e.g., 2022), the model tilts toward defensive value (DIA), shielding the portfolio from drawdowns (-23.62% vs -34.83% for QQQ). When yields ease and rate relief triggers, the model restores exposure to QQQ to harvest multiple expansion.
- **Ported Hypothesis Note:** This strategy was derived and validated exclusively on liquid US equity index ETFs (QQQ, DIA, SPY) and fixed-income/volatility benchmarks (TNX, VIX, HYG, SHY). Transferring this mechanism to cryptocurrency relative-value pairs (e.g., SOL/ETH high-beta tech sleeve vs BTC monetary reserve sleeve) constitutes an adapted, unproven research interpretation.

## Signal

### Decision Cadence and Core Algebra
- **Action Space:** Continuous asset allocation between two long-only equity ETFs: QQQ weight $w_t^Q \\in [0.0, 1.0]$, and DIA weight $w_t^D = 1.0 - w_t^Q$. No cash, no leverage, no borrowing.
- **Daily Net Return:**
  $$R_t = w_t^Q r_t^Q + (1 - w_t^Q) r_t^D - \\text{cost}_t$$
  where $r_t^Q$ and $r_t^D$ are daily close-to-close returns of QQQ and DIA, and the turnover cost is:
  $$\\text{cost}_t = c \\cdot \\text{Turnover}_t, \\quad c = 10\\text{ bps} = 0.0010$$
  $$\\text{Turnover}_t = 2.0 \\cdot |w_t^Q - w_{t-1}^Q|$$
  (The factor of 2 captures the necessary two-way transaction: selling one ETF sleeve and buying the corresponding dollar amount in the other).
- **Execution Convention:** 1-day implementation lag. At date $t$, the signal utilizes information available up to market close $t-1$ to compute the target weight, avoiding same-day lookahead bias.

### Feature Definitions and Expanding Standardization
All continuous state variables undergo expanding-window standardization with a minimum 252-day warmup:
$$Z(x_t) = \\frac{x_t - \\mu_{t-1}}{\\sigma_{t-1}}$$
where $\\mu_{t-1}$ and $\\sigma_{t-1}$ are sample mean and population standard deviation computed strictly over historical dates $s \\le t-1$.

Raw continuous input features:
1. `rel_mom126`: Trailing 126-day relative return $\\frac{QQQ_t / QQQ_{t-126}}{DIA_t / DIA_{t-126}} - 1$.
2. `rel_reversal`: Relative drawdown depth from historical peak ratio:
   $$\\text{rel\\_drawdown}_t = \\frac{\\text{Ratio}_t}{\\max_{s \\le t} \\text{Ratio}_s} - 1, \\quad \\text{Ratio}_t = \\frac{QQQ_t}{DIA_t}$$
3. `rate_relief`: Inverted 21-day change in 10-year Treasury yield: $-\\Delta TNX_{21, t} = -(TNX_t - TNX_{t-21})$.
4. `spy_drawdown`: SPY drawdown depth from peak: $\\frac{SPY_t}{\\max_{s \\le t} SPY_s} - 1$.
5. `high_vix`: 756-day rolling percentile rank of VIX ($vh$).
6. `low_vix`: Subdued volatility regime indicator ($-vh$).
7. `vix_relief`: Inverted 21-day change in VIX: $-\\Delta VIX_{21, t} = -(VIX_t - VIX_{t-21})$.
8. `credit_relief`: 21-day relative return of high-yield bonds vs short-term Treasuries: $\\frac{HYG_t / HYG_{t-21}}{SHY_t / SHY_{t-21}} - 1$.
9. `credit_stress`: Inverted credit relief (widening credit spreads).

### Two-Stage Statistical Screening and Interaction Selection

#### Stage 1: Global HAC Screening & De-duplication
Candidate main effects and second-order interactions are evaluated across forward horizons $h \\in \\{21, 63, 126\\}$ trading days using Newey–West/HAC regressions:
$$R_{t, t+h}^{Q-D} = \\alpha_h + \\beta_h x_{j, t} + \\epsilon_{t+h}$$
A candidate is admitted if $|t_{\\text{HAC}}| \\ge 2.0$ at its best horizon. Highly collinear terms with pairwise absolute correlation $|\\rho| \\ge 0.95$ are de-duplicated. Each admitted feature is assigned a fixed orientation $o_j = \\text{sign}(\\beta_h) \\in \\{-1.0, +1.0\\}$.

- **Admitted Main Effect (1 term):**
  - `rate_relief`: Best horizon $h = 126$, $n = 4,619$, $\\beta = +0.01315$, $t_{\\text{HAC}} = +2.357$, orientation $o = +1.0$.
- **Admitted Second-Order Interactions (9 terms):**
  1. `ix2__vix_relief__credit_stress`: $h = 126$, $n = 2,942$, $\\beta = -0.00405$, $t_{\\text{HAC}} = -3.623$, orientation $o = -1.0$.
  2. `ix2__rel_mom126__credit_relief`: $h = 126$, $n = 2,942$, $\\beta = -0.00455$, $t_{\\text{HAC}} = -2.793$, orientation $o = -1.0$.
  3. `ix2__rate_relief__low_vix`: $h = 21$, $n = 3,738$, $\\beta = -0.00503$, $t_{\\text{HAC}} = -2.751$, orientation $o = -1.0$.
  4. `ix2__rate_relief__credit_relief`: $h = 126$, $n = 2,942$, $\\beta = -0.00741$, $t_{\\text{HAC}} = -2.687$, orientation $o = -1.0$.
  5. `ix2__rel_reversal__high_vix`: $h = 126$, $n = 3,633$, $\\beta = -0.01382$, $t_{\\text{HAC}} = -2.499$, orientation $o = -1.0$.
  6. `ix2__rate_relief__spy_drawdown`: $h = 126$, $n = 4,367$, $\\beta = +0.02167$, $t_{\\text{HAC}} = +2.479$, orientation $o = +1.0$.
  7. `ix2__rel_reversal__rate_relief`: $h = 63$, $n = 4,430$, $\\beta = +0.01082$, $t_{\\text{HAC}} = +2.469$, orientation $o = +1.0$.
  8. `ix2__credit_relief__credit_stress`: $h = 21$, $n = 3,047$, $\\beta = -0.00082$, $t_{\\text{HAC}} = -2.311$, orientation $o = -1.0$.
  9. `ix2__rel_reversal__credit_relief`: $h = 126$, $n = 2,942$, $\\beta = +0.00767$, $t_{\\text{HAC}} = +2.189$, orientation $o = +1.0$.

#### Stage 2: Incremental Third-Order OOS Gate
While 26 third-order terms pass the initial global HAC screen, third-order terms carry severe overfitting risk. An incremental gate requires that any third-order candidate must:
1. Improve mean rolling OOS Sharpe versus the Main+IX2 base policy across 2018, 2020, and 2022 OOS evaluation windows;
2. Generate positive Sharpe delta in at least two of the three windows;
3. Survive economic-family de-duplication under a strict cap of 5 terms.

Only **2 third-order interactions** survive this gate:
1. `ix3__rel_mom126__rel_reversal__rate_relief`: $h = 126$, $\\beta = -0.01674$, $t_{\\text{HAC}} = -2.784$, orientation $o = -1.0$, mean $\\Delta\\text{Sharpe} = +0.0194$, positive in 3/3 periods.
2. `ix3__rel_reversal__rate_relief__spy_drawdown`: $h = 63$, $\\beta = +0.02838$, $t_{\\text{HAC}} = +4.093$, orientation $o = +1.0$, mean $\\Delta\\text{Sharpe} = +0.00003$, positive in 2/3 periods.

### Composite Score Assembly
The component group scores are defined by expanding standardization of oriented averages:
$$S_{\\text{main}, t} = Z(o_{\\text{main}} \\cdot x_{\\text{rate\\_relief}, t})$$
$$S_{\\text{ix2}, t} = Z\\left(\\frac{1}{9} \\sum_{j=1}^9 o_j \\cdot \\text{ix2}_{j, t}\\right)$$
$$S_{\\text{ix3}, t} = Z\\left(\\frac{1}{2} \\sum_{k=1}^2 o_k \\cdot \\text{ix3}_{k, t}\\right)$$

Given group weights $\\lambda = (\\lambda_{\\text{main}}, \\lambda_{\\text{ix2}}, \\lambda_{\\text{ix3}})$, the raw composite score is:
$$S_t(\\lambda) = Z\\left(\\lambda_{\\text{main}} S_{\\text{main}, t} + \\lambda_{\\text{ix2}} S_{\\text{ix2}, t} + \\lambda_{\\text{ix3}} S_{\\text{ix3}, t}\\right)$$

### Fixed Position Mapping
The position mapping parameters are treated as structural strategy attributes and are held invariant across all walk-forward windows:
- Maximum tilt: $M = 0.50$
- Response scale: $\\tau = 0.75$
- Daily exponential smoothing: $\\eta = 0.05$

1. **Target Weight:**
   $$w_{\\text{target}, t} = 0.5 + M \\cdot \\tanh\\left(\\frac{S_t(\\lambda)}{\\tau}\\right) \\in [0.0, 1.0]$$
2. **Lagged and Smoothed Weight:**
   $$w_t^Q = (1 - \\eta) w_{t-1}^Q + \\eta \\cdot w_{\\text{target}, t-1}$$
   with initial condition $w_0^Q = 0.5$.

### Rolling Walk-Forward Selection Engine
- **Training Window:** 756 trading days (approx. 3 calendar years).
- **Test Block:** 63 trading days (approx. 1 calendar quarter).
- **Grid Space:** Coarse positive search over $\\lambda_{\\text{main}}, \\lambda_{\\text{ix2}}, \\lambda_{\\text{ix3}} \\in \\{0.25, 0.50, 0.75, 1.00\\}$ (64 configurations).
- **Turnover-Penalized Objective:**
  $$\\text{Score}_{\\text{base}} = \\frac{1}{5}\\left[\\text{rank}(\\text{CAGR}) + \\text{rank}(\\text{Sharpe}) + \\text{rank}(\\text{Calmar}) + \\text{rank}(\\text{MDD}) + \\text{rank}(-\\text{Turnover})\\right]$$
  $$\\text{Score}_{\\text{adj}} = \\text{Score}_{\\text{base}} - 0.08 \\cdot \\max(0, \\text{AnnualTurnover} - 3.0)$$
  where turnover exceeding 300% annualized incurs a linear penalty ($\\kappa = 0.08$). The configuration maximizing $\\text{Score}_{\\text{adj}}$ over the training window is deployed out of sample for the subsequent 63-day block.

## Required data

- **Instruments:**
  - `QQQ`: Invesco QQQ Trust ETF (growth sleeve).
  - `DIA`: SPDR Dow Jones Industrial Average ETF (value/defensive sleeve).
  - `SPY`: SPDR S&P 500 ETF (broad-market anchor and drawdown reference).
  - `HYG`: iShares iBoxx High Yield Corporate Bond ETF (credit spread numerator).
  - `SHY`: iShares 1-3 Year Treasury Bond ETF (credit spread denominator).
- **Macro and Volatility Benchmark Indices:**
  - `TNX`: CBOE 10-Year Treasury Yield Index ($10 \\times \\text{yield}$).
  - `VIX`: CBOE Volatility Index.
  - `VXN`: CBOE Nasdaq-100 Volatility Index (diagnostic).
  - `IRX`: CBOE 13-Week Treasury Bill Index (risk-free reference).
- **Timeframe:** Daily close-to-close returns and index levels.
- **Point-in-Time Alignment:**
  - Every continuous signal uses an expanding standardization warmup of 252 trading days.
  - All Z-score normalization parameters ($\\mu_{t-1}, \\sigma_{t-1}$) and target weights $w_{\\text{target}, t-1}$ are strictly lagged by 1 trading day relative to portfolio return realization to guarantee no forward lookahead.
- **Missing Data Handling:** Forward-fill stale index values where market trading calendars differ slightly; drop dates with missing primary ETF quotes.

## Execution assumptions

- **Execution Cadence:** Daily rebalance at market close (or next-day open).
- **Order Types:** Market-on-Close (MOC) or liquid limit orders matching the closing auction price.
- **Transaction Costs:** Flat 10 basis points ($0.10\\%$) one-way turnover cost applied to both buying and selling legs ($c = 10\\text{ bps}$).
- **Shorting and Leverage:** Strictly long-only equity sleeves. No short selling, no margin, no cash buffer, gross market exposure identically $1.0$ ($w_t^Q + w_t^D = 1.0$).
- **Borrow Costs:** Not applicable (long-only).
- **Market Impact & Capacity:** Both QQQ and DIA represent mega-cap, highly liquid US ETF instruments with tens of millions in average daily trading volume and sub-penny spreads. Strategy capacity comfortably exceeds $100M without material market impact at the modeled daily turnover.

## Evidence

### Source-reported

All performance figures, drawdowns, Sharpe ratios, and turnover metrics below are cited directly from Zheli Xiong (*arXiv:2607.06117v1*, Table 16 and accompanying replication package `rgrr_policy_comparison.csv` at commit `a1e44c2e7d4cf23f63a8746c139f6265882291c0`), evaluated net of 10 bps one-way transaction costs:

#### 1. Full Sample Baseline (Actual Start: 2009-07-27 to 2026-07-02, $N = 4,240$ trading days)
*Note: Evaluated post-warmup following the requested 2008-07-25 inception.*

| Strategy / Benchmark | Final Wealth | CAGR | Ann. Vol | Sharpe | Sortino | Max Drawdown | Calmar | Annual Turnover | Avg QQQ Weight |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **RGRR (Final Policy)** | **13.73x** | **16.85%** | **17.63%** | **0.972** | **1.226** | **-29.25%** | **0.576** | **505.89%** | **48.83%** |
| 100% QQQ | 19.25x | 19.22% | 20.69% | 0.954 | 1.230 | -35.12% | 0.547 | 0.00% | 100.00% |
| 100% DIA | 8.90x | 13.88% | 17.30% | 0.837 | 1.069 | -36.71% | 0.378 | 0.00% | 0.00% |
| 50/50 QQQ–DIA | 13.55x | 16.75% | 17.94% | 0.953 | 1.200 | -32.28% | 0.519 | 0.00% | 50.00% |

#### 2. Rolling Out-of-Sample Windows (Aligned Comparison across Inception Dates)

- **2018 OOS Window (2018-06-28 to 2026-07-02, $N = 2,013$ trading days):**
  - *RGRR:* CAGR 18.33%, Ann. Vol 19.92%, **Sharpe 0.945**, Sortino 1.188, **Max DD -29.41%**, Calmar 0.623, Turnover 444.60%, Avg QQQ 49.38%, Final Wealth 3.84x.
  - *100% QQQ:* CAGR 20.50%, Ann. Vol 24.12%, Sharpe 0.894, Sortino 1.169, Max DD -35.12%, Calmar 0.584, Turnover 0.00%, Avg QQQ 100.00%, Final Wealth 4.44x.
  - *100% DIA:* CAGR 12.41%, Ann. Vol 18.78%, Sharpe 0.717, Sortino 0.864, Max DD -36.71%, Calmar 0.338, Turnover 0.00%, Avg QQQ 0.00%, Final Wealth 2.55x.
  - *50/50 QQQ–DIA:* CAGR 16.69%, Ann. Vol 20.38%, Sharpe 0.860, Sortino 1.069, Max DD -32.28%, Calmar 0.517, Turnover 0.00%, Avg QQQ 50.00%, Final Wealth 3.43x.
  - *Deltas vs Benchmarks:* RGRR vs QQQ: $\\Delta\\text{Sharpe} = +0.051$, $\\Delta\\text{CAGR} = -2.17\\%$, $\\Delta\\text{MDD} = +5.71\\%$. RGRR vs 50/50: $\\Delta\\text{Sharpe} = +0.085$, $\\Delta\\text{CAGR} = +1.64\\%$, $\\Delta\\text{MDD} = +2.87\\%$.

- **2020 OOS Window (2020-01-02 to 2026-07-02, $N = 1,633$ trading days):**
  - *RGRR:* CAGR 18.69%, Ann. Vol 20.72%, **Sharpe 0.931**, Sortino 1.171, **Max DD -29.41%**, Calmar 0.635, Turnover 408.16%, Avg QQQ 50.37%, Final Wealth 3.03x.
  - *100% QQQ:* CAGR 21.29%, Ann. Vol 25.06%, Sharpe 0.896, Sortino 1.181, Max DD -35.12%, Calmar 0.606, Turnover 0.00%, Avg QQQ 100.00%, Final Wealth 3.49x.
  - *100% DIA:* CAGR 11.98%, Ann. Vol 19.64%, Sharpe 0.675, Sortino 0.813, Max DD -36.71%, Calmar 0.326, Turnover 0.00%, Avg QQQ 0.00%, Final Wealth 2.08x.
  - *50/50 QQQ–DIA:* CAGR 16.88%, Ann. Vol 21.17%, Sharpe 0.843, Sortino 1.052, Max DD -32.28%, Calmar 0.523, Turnover 0.00%, Avg QQQ 50.00%, Final Wealth 2.75x.
  - *Deltas vs Benchmarks:* RGRR vs QQQ: $\\Delta\\text{Sharpe} = +0.035$, $\\Delta\\text{CAGR} = -2.60\\%$, $\\Delta\\text{MDD} = +5.71\\%$. RGRR vs 50/50: $\\Delta\\text{Sharpe} = +0.088$, $\\Delta\\text{CAGR} = +1.81\\%$, $\\Delta\\text{MDD} = +2.87\\%$.

- **2022 OOS Window (2022-01-03 to 2026-07-02, $N = 1,128$ trading days):**
  - *RGRR:* **CAGR 15.19%**, Ann. Vol 18.11%, **Sharpe 0.871**, Sortino 1.251, **Max DD -23.62%**, Calmar 0.643, Turnover 354.33%, Avg QQQ 54.03%, Final Wealth 1.88x.
  - *100% QQQ:* CAGR 14.65%, Ann. Vol 23.44%, Sharpe 0.700, Sortino 0.996, Max DD -34.83%, Calmar 0.421, Turnover 0.00%, Avg QQQ 100.00%, Final Wealth 1.84x.
  - *100% DIA:* CAGR 10.64%, Ann. Vol 15.07%, Sharpe 0.746, Sortino 1.074, Max DD -20.76%, Calmar 0.513, Turnover 0.00%, Avg QQQ 0.00%, Final Wealth 1.57x.
  - *50/50 QQQ–DIA:* CAGR 12.93%, Ann. Vol 18.28%, Sharpe 0.757, Sortino 1.069, Max DD -26.80%, Calmar 0.482, Turnover 0.00%, Avg QQQ 50.00%, Final Wealth 1.72x.
  - *Deltas vs Benchmarks:* RGRR vs QQQ: $\\Delta\\text{Sharpe} = +0.171$, $\\Delta\\text{CAGR} = +0.54\\%$, $\\Delta\\text{MDD} = +11.21\\%$. RGRR vs 50/50: $\\Delta\\text{Sharpe} = +0.114$, $\\Delta\\text{CAGR} = +2.26\\%$, $\\Delta\\text{MDD} = +3.18\\%$.

### Independently reproduced

Not independently reproduced. All metrics and parameter values cited above are source-reported by Zheli Xiong (*arXiv:2607.06117v1* and GitHub repository `shaun19920309/Relief-Gated-Relative-Rotation-for-QQQ-DIA-Allocation`, commit `a1e44c2e7d4cf23f63a8746c139f6265882291c0`).

### Negative evidence

1. **Failure of Standalone Contrarian Rotation:** Pure relative momentum reversal without macro gating fails out of sample. Simple strategies that attempt to short or underweight QQQ solely because it has outperformed DIA in recent months suffer acute performance drag during strong growth expansion regimes.
2. **Underperformance Against 100% QQQ During Bull Markets:** In strong, persistent technology bull markets (e.g., 2019, post-COVID 2020 rally, and 2023), rotating partially into DIA causes RGRR to lag 100% QQQ in total return (CAGR is 2.17% to 2.60% lower in 2018 and 2020 OOS starts). The strategy does **not** deliver unconditional return dominance; it functions strictly as a risk-adjusted allocation and drawdown-reduction tool.
3. **Severe High Turnover Friction:** Annualized portfolio turnover ranges between 354% and 506%. While net results survive the 10 bps fee model, any execution friction beyond 20–25 bps or high bid-ask spreads would materially erode the Sharpe advantage over the static 50/50 baseline.
4. **Attrition of High-Order Statistical Interactions:** Out of 26 statistically significant third-order candidate interactions identified in the global sample ($|t_{\\text{HAC}}| \\ge 2.0$), 24 failed to improve out-of-sample portfolio Sharpe when added to the lower-order policy base. Relying purely on in-sample or global regression significance without incremental OOS filtering leads to severe portfolio overfitting.

## Falsification plan

1. **Fee Sensitivity Stress Test:**
   - *Protocol:* Re-run the walk-forward evaluation scaling the one-way transaction cost $c$ across $[10\\text{ bps}, 15\\text{ bps}, 20\\text{ bps}, 25\\text{ bps}, 30\\text{ bps}]$.
   - *Falsification Rule:* If RGRR net Sharpe ratio falls below the static 50/50 QQQ–DIA Sharpe ratio at $c \\le 20\\text{ bps}$ in more than one OOS window, the economic thesis is rejected as an artifact of transaction-cost sensitivity.
2. **Turnover Smoothing Ablation:**
   - *Protocol:* Perturb the daily weight smoothing parameter $\\eta$ from $0.05$ to $0.20, 0.50, 1.00$ (disabling smoothing).
   - *Falsification Rule:* If annualized turnover exceeds 800% without a commensurate increase in gross information ratio, confirm that the model's low-pass filter ($\\eta = 0.05$) is structurally necessary to prevent turnover destruction.
3. **Macro State Shuffled-Label Placebo Test:**
   - *Protocol:* Permute the time indices of the macro state variables (`rate_relief`, `vix_relief`, `spy_drawdown`) while preserving the asset returns ($r_t^Q, r_t^D$).
   - *Falsification Rule:* If the synthetic randomized macro states generate an OOS Sharpe within $0.05$ of the true RGRR strategy, reject the hypothesis that macro conditioning provides genuine economic gating.
4. **Out-of-Sample Forward Regime Test (Post-July 2026):**
   - *Protocol:* Evaluate the locked parameter mapping and signal stack on unobserved post-July 2026 data.
   - *Falsification Rule:* Strategy fails if realized Sharpe over a 252-day forward window is negative or trails both 100% QQQ and 100% DIA during an equity market correction.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Structural Differences & Crypto Portability Risks:**
  - *Absence of True "Value" Anchors:* In traditional equities, DIA represents mature industrial, financial, and consumer companies with stable earnings, dividends, and tangible book value. In crypto, virtually all tokens exhibit high correlation to Bitcoin during market crashes; there is no structural equivalent to dividend-paying defensive value equities.
  - *Asset Pair Adaptation:* A conceptual crypto adaptation could rotate between a high-beta technology/smart-contract layer sleeve (e.g., SOL, ETH, AVAX) and a store-of-value/monetary reserve sleeve (BTC).
  - *Perpetual Funding and Basis Dynamics:* If implemented via perpetual futures, funding rate differentials and basis drift introduce continuous carry drag not present in ETF cash equities.
  - *24/7 Liquidity and Tail Shocks:* Crypto markets operate 24/7 without market-on-close auctions or regulatory halts; liquidation cascades can induce sudden 30%+ intra-day decoupling between alts and BTC that violates daily smoothed rebalancing assumptions.
  - *Governance & De-pegging Risks:* Smart contract vulnerabilities and protocol-specific risks do not exist in SEC-regulated index ETFs.

## Limitations

- **High Portfolio Turnover:** Annual turnover of 354% to 506% requires institutional-grade execution; unsuited for taxable retail accounts or illiquid venues.
- **CAGR Drag in Structural Tech Bull Markets:** The strategy structurally trails pure QQQ during uninterrupted technology rallies.
- **Multiple-Testing Exposure in Candidate Generation:** Although global screening uses Newey-West HAC standard errors and correlation de-duplication, the initial interaction pool was evaluated over the full historical sample before walk-forward testing. Formal Deflated Sharpe Ratio (DSR) or Hansen's Superior Predictive Ability (SPA) tests across all combinatorial paths were not reported.
- **Underspecified Real-Time Trading Gates:** The production script applies an ex-post turnover penalty during the rolling training phase, but lacks an intraday execution threshold or deadband buffer to suppress small daily weight adjustments.

## Implementation status

- **Frontmatter Status:** `not-implemented`.
- **State in Repository:** Research capture only. No implementation in NautilusTrader, PyBroker, paper trading, testnet, or live trading has been created or authorized.

## Adoption boundary

- **Scope:** Research capture only.
- **Boundary Conditions:** This strategy is not approved for live deployment, paper trading, or capital allocation. Presence in this repository indicates only that the research has been normalized into canonical Wiki Brain format for formal evaluation.

## Related Wiki records

- [[continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]] — Foundational continuous macro timing model on Growth vs Defensive baskets by the same author (arXiv:2605.20636).
- [[conformal-kelly-prediction-intervals-fractional-sizing-2026-09-02]] — Robust non-parametric position sizing and drawdown control under fat tails (arXiv:2608.01494).
- [[cross-asset-futures-timing-end-to-end-portfolio-transformer-2026-09-02]] — End-to-end deep parametric portfolio policies for multi-asset timing (arXiv:2607.00475).

## Sources

1. Zheli Xiong. *"Relief-Gated Relative Rotation for QQQ–DIA Allocation: Globally Screened Relative States, Fixed Position Mapping, Incremental Interaction Admission, and Walk-Forward Validation"*, arXiv preprint `arXiv:2607.06117v1 [q-fin.PM]`, submitted July 7, 2026. DOI: [10.48550/arXiv.2607.06117](https://doi.org/10.48550/arXiv.2607.06117). Stable URL: [https://arxiv.org/abs/2607.06117](https://arxiv.org/abs/2607.06117). Full HTML: [https://arxiv.org/html/2607.06117v1](https://arxiv.org/html/2607.06117v1).
2. GitHub Evaluation Code Repository: `shaun19920309/Relief-Gated-Relative-Rotation-for-QQQ-DIA-Allocation`, repository commit SHA `a1e44c2e7d4cf23f63a8746c139f6265882291c0`. URL: [https://github.com/shaun19920309/Relief-Gated-Relative-Rotation-for-QQQ-DIA-Allocation](https://github.com/shaun19920309/Relief-Gated-Relative-Rotation-for-QQQ-DIA-Allocation).
