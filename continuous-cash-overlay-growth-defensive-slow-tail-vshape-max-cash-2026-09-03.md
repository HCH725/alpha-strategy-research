---
schema: strategy-research-record-v1
title: "Continuous Cash-Overlay Filters for a Static Growth-Defensive Risk Sleeve: Slow-Tail Compensation, V-Shape Crash Brakes, Walk-Forward Validation, and Max-Cash Combination"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - macro-timing
  - cash-overlay
  - drawdown-brake
  - regime-filter
  - portfolio-allocation
  - walk-forward
  - etf
status: research-only
confidence: medium
source_as_of: 2026-06-08
sources:
  - "https://arxiv.org/abs/2606.09025"
  - "https://doi.org/10.48550/arXiv.2606.09025"
  - "https://arxiv.org/html/2606.09025v1"
  - "https://github.com/shaun19920309/gd-cash-overlay-filters/commit/565c32aa42d10254fbb6aa46b044f5e70522160d"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Continuous Cash-Overlay Filters for a Static Growth-Defensive Risk Sleeve: Slow-Tail Compensation, V-Shape Crash Brakes, Walk-Forward Validation, and Max-Cash Combination

## Provenance

- **Canonical Academic Source:** Zheli Xiong (University of Science and Technology of China, USTC; `zlxiong@mail.ustc.edu.cn`), *"Continuous Cash-Overlay Filters for a Static Growth–Defensive Risk Sleeve: Slow-Tail Compensation, V-Shape Crash Brakes, Walk-Forward Validation, and Max-Cash Combination"*, arXiv preprint `arXiv:2606.09025v1 [q-fin.PM]`, submitted June 8, 2026. DOI: [10.48550/arXiv.2606.09025](https://doi.org/10.48550/arXiv.2606.09025). Full HTML text: [https://arxiv.org/html/2606.09025v1](https://arxiv.org/html/2606.09025v1).
- **Public Implementation Repository:** GitHub repository `shaun19920309/gd-cash-overlay-filters`, pinned immutable commit `565c32aa42d10254fbb6aa46b044f5e70522160d` (June 14, 2026). Key paths: `src/phase2_cash_filters/modes/slow_tail/run.py`, `src/phase2_cash_filters/modes/vshape/run.py`, `src/phase2_cash_filters/combined/max_cash/run.py`, `scripts/run_combined_max_cash.py`, and `docs/ARCHITECTURE.md`.
- **Pre-Write Deduplication Audit:** Repository-wide grep verified zero matches for `2606.09025`, `gd-cash-overlay-filters`, `cash-overlay`, or `slow-tail`. While the author's companion papers (`arXiv:2605.20636` in `continuous-macro-timing-growth-defensive-style-allocation-2026-09-02.md` and `arXiv:2607.06117` in `relief-gated-relative-rotation-qqq-dia-interaction-filter-2026-09-02.md`) address dynamic cross-sectional style rotation between growth and defensive sleeves or QQQ vs DIA, `arXiv:2606.09025` investigates a fundamentally distinct research question and mechanism: a defensive cash-overlay decision layer between a static, fixed 50/50 growth-defensive sleeve ($R$) and interest-bearing cash ($C$), combining two orthogonal risk filters (slow-tail compensation and fast V-shape crash brake) under a parameter-free max-cash aggregation rule.

## Economic mechanism

### Source-reported

The paper investigates whether and when an investor holding a transparent, static, equal-weight growth–defensive risky portfolio $R$ (50% Growth ETF basket + 50% Defensive ETF basket) should de-risk into interest-bearing cash $C$. Rather than attempting full-portfolio dynamic timing or unconstrained mean-variance optimization, the strategy restricts its action space to a one-dimensional continuous cash allocation $w_t^C \in [0, 1]$, where $w_t^R = 1 - w_t^C$.

The author formalizes two distinct, economically orthogonal risk shapes:
1. **Slow-Tail Compensation Risk (2022-Style Stagflation / Rate-Hike Regime):** Risky assets suffer not from a sudden liquidity shock, but from protracted macroeconomic headwinds—rising cash yields, aggressive policy rate increases ($\Delta TNX$), yield curve inversion, and compressed equity risk premia. Under these conditions, the expected forward excess return of equities over cash ($R - C$) deteriorates over multi-month horizons. The slow-tail filter identifies these regimes via historical analogue conditioning, evaluating future 63-day $R - C$ returns conditioned on historical bad-state scores.
2. **Fast V-Shape Crash Risk (2020 COVID / March 2025 Episodes):** Fast market drawdowns driven by severe volatility spikes (VIX percentile and changes), rate panic (concurrent flight-to-safety rate drops and rapid equity losses), and credit-market stress (HYG vs. SHY underperformance, BAA-AAA spread widening). These episodes develop rapidly and mean-revert quickly; they require an immediate crash brake that moves to cash without waiting for multi-month analogue confirmation, followed by smooth re-entry as panic abates.
3. **Max-Cash Aggregation without Parameter Fitting:** Rather than training a single complex regime classifier, the final overlay applies a parameter-free upper envelope rule: $w_t^C = \max(w_t^{C, slow}, w_t^{C, vshape})$. Each filter acts as an independent risk alarm. Empirical evidence demonstrates zero overlap between active cash triggers (0.00% across 2,208 trading days), validating the economic independence of the two failure channels.

### Research interpretation

This is an asymmetric drawdown-control and cash-overlay framework, not a standalone directional long/short alpha.

The falsifiable core hypothesis is: **Equity-over-cash excess return ($R - C$) suffers from two structural, statistically separable failure modes—slow macroeconomic compensation erosion and acute liquidity/volatility dislocations. Deploying independent, continuous cash-tilt filters designed specifically for each mode and taking their maximum cash demand ($w_t^C = \max(w_t^{C, slow}, w_t^{C, vshape})$) truncates downside tails, cuts maximum drawdown by roughly half (from -33.59% to -16.77%), and boosts risk-adjusted compound wealth net of realistic execution friction.**

Key economic boundaries and failure modes:
- **Cash Drag in Sustained Bull Markets:** In low-rate, low-volatility trending bull markets, any false-alarm cash allocation creates cash drag and forfeits equity compounding. The 30% material trade gate explicitly prevents frictional low-conviction rebalancing.
- **V-Shape Rebound Lag:** Because the V-shape filter operates as a crash brake and smooths its re-entry ($\eta_{exit} = 0.25$), a violent "V-shaped" market rebound causes the portfolio to hold cash while the risky sleeve surges, creating temporary underperformance during the initial bounce (e.g., -7.46% lag during the 2020 COVID recovery).
- **Turnover and Frictional Decay:** Annualized turnover is substantial (350% to 540%), meaning gross gains are heavily eroded if implementation suffers from high execution fees or wide bid-ask spreads.

## Signal

The strategy runs on daily close data and generates next-day target weights ($w_{t+1}^C, w_{t+1}^R$) using two decoupled component pipelines and a top-level max-cash combiner.

### 1. Static Risky Sleeve and Benchmark
- **Growth Basket ($G$):** Equal weight of 5 ETFs: `{QQQ, XLK, VGT, SPYG, VUG}`.
- **Defensive Basket ($D$):** Equal weight of 5 ETFs: `{SCHD, VYM, VTV, FDVV, COWZ}`.
- **Risky Sleeve Return:** $R_t^R = 0.5 G_t + 0.5 D_t$.
- **Cash Benchmark Return ($R_t^C$):** Contemporaneous risk-free return derived from 3-month Treasury / cash yield.
- **Target Excess Return:** $R_t^{R-C} = R_t^R - R_t^C$.

### 2. Standardization & Intensity Transformations
- **Expanding Standardization:** For any feature $x_t$, $z_t(x) = \frac{x_t - \mu_t^{exp}(x)}{\sigma_t^{exp}(x)}$, requiring an initial warmup of 252 trading days.
- **Smooth Directional Intensity:** $\text{softplus}(x) = \log(1 + \exp(x))$.

### 3. Filter 1: Slow-Tail Compensation Filter
- **Raw Primitives & Smooth Intensities:**
  - Cash Yield level: $CH_t = \text{softplus}(z_t(\text{CashYield}_t))$
  - Cash Yield 21-day change: $CR_t = \text{softplus}(z_t(\Delta \text{CashYield}_{21,t}))$
  - Rate Headwind (10Y Treasury): $RH_t = \text{softplus}(z_t(\Delta TNX_{21,t}))$
  - Curve Inversion: $CI_t = \text{softplus}(-z_t(\text{Curve}_{10y-3m,t}))$
  - Risky Drawdown: $DD_t = \text{softplus}(-z_t(RDrawdown_t))$
  - Volatility states: $HV_t = \text{softplus}(z_t(VIXPct_{756,t}))$, $LV_t = \text{softplus}(-z_t(VIXPct_{756,t}))$, $VS_t = \text{softplus}(z_t(\Delta VIX_{21,t}))$
  - Credit Risk-Off & Widening: $CRO_t = \text{softplus}(-z_t(HYGSHYRel_{21,t}))$, $CW_t = \text{softplus}(z_t(\Delta CS_{21,t}))$ where $CS_t = BAA_t - AAA_t$
  - Risky Sleeve Strength & Volatility: $RS_t = \text{softplus}(z_t(RTrailing_{63,t}))$, $RU_t = \text{softplus}(-z_t(RTrailing_{63,t}))$, $LVOL_t = \text{softplus}(-z_t(RVol_{63,t}))$
- **Selected `all_v4` Component Interaction Set ($K=11$):**
  - Compressed Risk Premium: $RS \times LVOL$, $RS \times LVOL \times LV$, $RS \times LV$, $CH \times RS \times LV$, $CH \times RS \times LVOL$
  - Rate Path Stress: $RH \times VS$, $RH \times CRO$, $RH \times RU$, $DD \times RH \times CRO$
  - Direct Level States: $CR$ (rising cash yield), $RH$ (rate headwind)
- **Bad-State Composite Score:**
  $$BadScore_t = \frac{1}{K}\sum_{k=1}^K z_t(Component_{k,t})$$
- **Historical Analogue Estimation:**
  Conditioned on today's $BadScore_t$, calculate the empirical mean future 63-day $R-C$ return among prior realized days where historical bad score $\ge BadScore_t$ (excluding the most recent 63 days to eliminate label overlap leakage; minimum tail sample $n=40$; minimum historical burn-in = 504 days). Let this historical conditional mean be $\hat{\mu}_{40,t}$.
- **Dynamics & Pressure Calculation:**
  $$\bar{\mu}_t = \text{EWMA}_{m=21}(\hat{\mu}_{40,t})$$
  $$\Delta \bar{\mu}_t = \bar{\mu}_t - \bar{\mu}_{t-21}$$
  $$Accel_t = (\bar{\mu}_t - \bar{\mu}_{t-21}) - (\bar{\mu}_{t-21} - \bar{\mu}_{t-42})$$
  $$Pressure_t = -z_t(\bar{\mu}_t) - 0.5 z_t(\Delta \bar{\mu}_t) - 0.5 z_t(Accel_t)$$
- **Raw Cash Weight Mapping:**
  $$CashRaw_t^{slow} = MaxCash \cdot \left[\frac{1}{1 + \exp(-Pressure_t / \tau)}\right]^\gamma$$
  Selected parameters: $MaxCash = 1.00$, $\tau = 1.00$, $\gamma = 4.0$.
- **Materiality Gate & Smoothing:**
  If $CashRaw_t^{slow} \ge 0.30$, cash enters immediately ($target\_cash = CashRaw_t^{slow}$). If $CashRaw_t^{slow} < 0.30$, exit back to $R$ is smoothed:
  $$w_{t, \text{target}}^{C, slow} = w_{t-1}^{C, slow} + 0.25 (0.0 - w_{t-1}^{C, slow})$$
  If $w_t^C < 0.01$, cash is fully deactivated to 0.

### 4. Filter 2: V-Shape Crash-Brake Filter
- **Standardized Primitives:**
  $VL_t = z_t(VIXPct_{756,t})$, $VS10_t = z_t(\Delta VIX_{10,t})$, $RR_t = z_t(-\Delta TNX_{21,t})$, $RL10_t = z_t(-RTrailing_{10,t})$, $CW_t = z_t(\Delta CS_{21,t})$, $CRO_t = z_t(-HYGSHYRel_{21,t})$, $DD_t = z_t(-RDrawdown_t)$.
- **Interaction Panic Primitives:**
  - $BrakeVIXLevel_t = z_t(VL_t)$
  - $BrakeVIXSpike_t = z_t(VS10_t)$
  - $RatePanic_t = 0.5 z_t(RR_t \cdot RL10_t \cdot VL_t) + 0.5 z_t(RR_t \cdot CRO_t)$
  - $CreditPanic_t = z_t(VS10_t \cdot CW_t)$
- **Brake Score:**
  $$BrakeScore_t = \left[\alpha_{vix} BrakeVIXLevel_t + (1 - \alpha_{vix}) BrakeVIXSpike_t\right] + \lambda_r RatePanic_t + \lambda_c CreditPanic_t$$
  Selected parameters: $\alpha_{vix} = 0.50$, $\lambda_r = 0.25$, $\lambda_c = 0.25$.
- **Raw Cash Weight Mapping:**
  $$BrakeZ_t = z_t(BrakeScore_t)$$
  $$CashRaw_t^{vshape} = MaxCash \cdot \left[\frac{1}{1 + \exp(-BrakeZ_t / \tau)}\right]^\gamma$$
  Selected parameters: $MaxCash = 0.75$, $\tau = 1.00$, $\gamma = 5.0$.
- **Materiality Gate & Asymmetric Smoothing:**
  If $CashRaw_t^{vshape} \ge 0.30$, immediate entry ($\eta_{enter} = 1.0$). When $CashRaw_t^{vshape} < 0.30$, smoothed exit back to $R$ with $\eta_{exit} = 0.25$:
  $$w_t^{C, vshape} = (1 - 0.25) w_{t-1}^{C, vshape} + 0.25 \cdot 0.0$$

### 5. Top-Level Max-Cash Combiner
- **Aggregation Rule:**
  $$w_{t+1}^C = \max(w_t^{C, slow}, w_t^{C, vshape})$$
  $$w_{t+1}^R = 1.0 - w_{t+1}^C$$
- **Execution Timing:** All signals formed on day $t$ close are executed at day $t+1$ close (`shift(1)`), ensuring zero look-ahead bias.

## Required data

- **Universe / Instruments:**
  - Growth Basket ($G$): `QQQ`, `XLK`, `VGT`, `SPYG`, `VUG` (US Large-Cap Growth / Tech ETFs).
  - Defensive Basket ($D$): `SCHD`, `VYM`, `VTV`, `FDVV`, `COWZ` (US Dividend / Value / Cash-Flow ETFs).
  - Credit Proxies: `HYG` (iShares High Yield Corporate Bond), `SHY` (iShares 1-3 Year Treasury Bond), Moody's Seasoned BAA and AAA Corporate Bond yields.
  - Rate / Macro Proxies: CBOE 10-Year Treasury Yield Index (`TNX`), CBOE 13-Week Treasury Bill Index (`IRX`), Treasury 10Y-3M yield curve spread.
  - Volatility Proxy: CBOE Volatility Index (`VIX`).
  - Cash / Risk-Free Asset ($C$): Daily risk-free return matching 3-month Treasury yield / BIL / SHV.
- **Venue:** US Equity and Index Options markets (NYSE Arca, NASDAQ, CBOE, FRED).
- **Timeframe & Session:** Daily closing prices; 252 trading days per calendar year.
- **Data Availability & PIT Hygiene:** All rolling percentiles (756d for VIX), trailing returns (10d, 21d, 63d, 126d), and expanding moments use strictly point-in-time observations available as of market close. The historical analogue lookup explicitly purges the most recent 63 trading days to prevent forward-looking overlap with future return targets.

## Execution assumptions

- **Execution Timing:** Next-day close execution ($w_{t+1} = \text{signal}_t$).
- **Frictional Costs:** Baseline 10 bps (0.10%) one-way transaction cost deducted from daily portfolio net returns on absolute turnover:
  $$\text{Daily Turnover}_t = |\Delta w_t^R|$$
  $$\text{Net Return}_t = \text{Gross Return}_t - \text{Daily Turnover}_t \times 0.0010$$
- **Borrow & Shorting:** Long-only portfolio; no leverage ($w^R + w^C = 1.0$, $w^R \ge 0$, $w^C \ge 0$). No short borrowing required.
- **Fill Model:** Market on close (MOC) at official ETF NAV/closing prices; high-liquidity ETF components ensure minimal slippage beyond the 10 bps deduction.

## Evidence

### Source-reported

All metrics below are directly cited from Zheli Xiong (*arXiv:2606.09025v1*, June 2026) and verified against repository tables generated under commit `565c32aa42d10254fbb6aa46b044f5e70522160d`, net of 10 bps one-way transaction costs.

#### 1. Selected Full-Sample Performance (Common Window: 2018-06-28 to 2026-04-30, Table 13)
| Strategy | CAGR | Sharpe | Max Drawdown | Ann. Turnover | Avg. Cash | Max Cash | Final Wealth |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Max-Cash Combined** | **20.45%** | **1.28** | **-16.77%** | **352.95%** | **6.85%** | **91.65%** | **510.36%** |
| Slow-Tail Only | 19.41% | 1.03 | -33.59% | 86.75% | 3.20% | 91.65% | 473.24% |
| V-Shape Only | 17.63% | 1.07 | -23.77% | 266.20% | 3.65% | 74.88% | 414.79% |
| **100% Risky Sleeve ($R$)** | 16.62% | 0.94 | -33.59% | 0.00% | 0.00% | 0.00% | 384.62% |

#### 2. Annual Calendar Diagnostics (Table 3)
| Year | 100% $R$ Return / DD | 100% $C$ Return | Slow-Tail Return / DD | V-Shape Return / DD | Max-Cash Return / DD | Avg. Cash |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2018 | -3.02% / -19.71% | 2.54% | -3.02% / -19.71% | -2.31% / -16.77% | -2.31% / -16.77% | 7.68% |
| 2019 | +32.90% / -8.03% | 2.55% | +32.90% / -8.03% | +32.39% / -8.03% | +32.39% / -8.03% | 0.57% |
| 2020 | +23.82% / -33.59% | 0.62% | +23.82% / -33.59% | +44.55% / -15.11% | **+44.55% / -15.11%** | 7.64% |
| 2021 | +31.04% / -4.92% | 0.00% | +31.04% / -4.92% | +29.36% / -4.92% | +29.36% / -4.92% | 0.84% |
| 2022 | -17.06% / -23.78% | 1.29% | **+2.41% / -13.55%** | -17.06% / -23.77% | **+2.41% / -13.55%** | 24.29% |
| 2023 | +28.14% / -9.73% | 5.13% | +27.26% / -9.73% | +28.14% / -9.73% | +27.26% / -9.73% | 3.01% |
| 2024 | +22.51% / -8.88% | 5.17% | +22.51% / -8.88% | +18.60% / -7.93% | +18.60% / -7.93% | 3.28% |
| 2025 | +17.31% / -19.66% | 5.13% | +17.71% / -19.66% | +15.79% / -14.64% | +16.18% / -14.64% | 7.87% |
| 2026 | +8.61% / -7.95% | 1.03% | +8.61% / -7.95% | +6.64% / -7.86% | +6.64% / -7.86% | 7.61% |

#### 3. Key Stress Event Diagnostics (Table 14)
- **COVID-19 Crash (2020-02-19 to 2020-03-23):**
  - Max-Cash Policy Return: -14.58% (Policy Max DD: -15.11%, Avg Cash: 58.64%) vs. 100% $R$ Return: -33.17% (DD: -33.59%). Benefit driven entirely by V-Shape Crash Brake.
- **Calendar Year 2022 (Stagflation / Rate Hikes):**
  - Max-Cash Policy Return: +2.41% (Policy Max DD: -13.55%, Avg Cash: 24.29%) vs. 100% $R$ Return: -17.06% (DD: -23.78%). Benefit driven entirely by Slow-Tail Compensation Filter.
- **Slow 2022 Drawdown Leg (2022-08-25 to 2022-09-26):**
  - Max-Cash Policy Return: -4.23% (Avg Cash: 72.19%) vs. 100% $R$ Return: -12.43%.
- **April 2025 Crash (2025-03-25 to 2025-04-08):**
  - Max-Cash Policy Return: -10.10% (Avg Cash: 19.33%) vs. 100% $R$ Return: -14.40%.

#### 4. Walk-Forward Out-of-Sample (OOS) Validation (Table 15)
Parameters re-selected every 63 trading days via multi-criteria grid optimization:
- **Main OOS Expanding Max-Cash:** CAGR 18.05%, Max DD -22.05%, Ann. Turnover 460.07%, Avg. Cash 10.23% vs. 100% $R$ CAGR 16.09%, Max DD -33.59%.
- **Main OOS Rolling Max-Cash (756d train):** CAGR 17.07%, Max DD -22.05%, Ann. Turnover 542.31%, Avg. Cash 12.28% vs. 100% $R$ CAGR 16.09%, Max DD -33.59%.
- **Post-2022 OOS Expanding Max-Cash:** CAGR 14.29%, Max DD -14.75%, Ann. Turnover 608.53%, Avg. Cash 15.11% vs. 100% $R$ CAGR 12.47%, Max DD -23.78%.
- **Post-2022 OOS Rolling Max-Cash:** CAGR 11.87%, Max DD -16.88%, Ann. Turnover 740.85%, Avg. Cash 17.57% vs. 100% $R$ CAGR 12.47%, Max DD -23.78%.

#### 5. Orthogonality of Risk Triggers (Table 16)
Over the 2,208-trading-day common sample:
- **Slow-Tail Only Active ($>1\%$ cash):** 179 days (8.11% of sample, Avg. Combined Cash 39.32%).
- **V-Shape Only Active ($>1\%$ cash):** 360 days (16.30% of sample, Avg. Combined Cash 22.25%).
- **Both Filters Active Simultaneously:** **0 days (0.00% of sample)**.
- **Neither Filter Active (100% $R$):** 1,669 days (75.59% of sample).

### Independently reproduced

Not independently reproduced. All figures and parameter tables cited above are source-reported by Zheli Xiong (*arXiv:2606.09025v1* and GitHub repository `shaun19920309/gd-cash-overlay-filters` at commit `565c32aa42d10254fbb6aa46b044f5e70522160d`).

### Negative evidence

1. **Rebound Lag in Sharp V-Bottoms:** As shown in Table 10, during the COVID recovery window, the V-shape strategy gained only +19.75% versus +27.21% for the benchmark (-7.46% excess return), because cash de-allocation was smoothed with $\eta_{exit} = 0.25$.
2. **Rolling Over-Defensiveness Post-2022:** Under rolling walk-forward validation (756d training window), post-2022 CAGR dropped to 11.87% versus 12.47% for the unmanaged risky sleeve. When recent history is heavily populated by stress regimes, the rolling selector over-allocates to cash during strong equity recoveries.
3. **Turnover Friction:** Annual turnover ranges from 352% in the selected common window to 740% in rolling post-2022 OOS. If one-way transaction costs exceed 25-30 bps, the CAGR advantage is largely consumed.

## Falsification plan

1. **Orthogonality Collapse / Placebo Test:** Randomly shift the macro state variables by $\pm 60$ trading days relative to equity returns. If the resulting max-cash overlay retains drawdown reduction or Sharpe enhancement, the effect is an artifact of unconditional volatility-timing rather than structural macro-regime conditioning.
2. **Transaction Cost Sensitivity Barrier:** Evaluate performance across 0, 10, 20, 30, 40, and 50 bps one-way turnover fees. Falsification occurs if net CAGR falls below 100% $R$ at $\le 25$ bps one-way cost.
3. **Whipsaw Stress in Sideways High-Vol Regimes:** Test on simulated or historical chop regimes (e.g. 2011 or 2015-2016 US equities) where VIX spikes repeatedly without persistent drawdown. The strategy should be falsified if false alarms trigger excessive turnover without mitigating $\ge 5\%$ drawdowns.
4. **Out-of-Sample Failure Rule:** In prospective live or out-of-sample forward trading, if the strategy suffers a drawdown exceeding 85% of the benchmark's drawdown over a rolling 1-year window, or if annual turnover exceeds 800%, the cash overlay must be halted.

## Crypto portability

- **Portability Classification:** `adapted / unproven`.
- **Porting Rationale:** The underlying mechanism—distinguishing slow compensation compression (negative basis / declining yield / tight liquidity) from acute liquidity liquidation cascades—is structurally relevant to crypto markets. However, the cited source exclusively evaluates US equity and Treasury ETF data.
- **Architectural Adaptations for Crypto:**
  - **Risky Sleeve ($R$):** A static market-cap or equal-weight basket of top-tier assets (e.g. 50% BTC + 50% ETH/SOL, or a defined crypto blue-chip basket).
  - **Cash Sleeve ($C$):** Yield-bearing USD stablecoins (e.g. Maker/Sky sUSDS, Ethena sUSDe, Mountain USDY, Ondo USDY) or tokenized US Treasuries (BUIDL, TBILL).
  - **State Primitives Substitution:**
    - VIX percentile $\rightarrow$ Deribit BTC/ETH DVOL rolling percentile.
    - Rate headwind ($\Delta TNX$) $\rightarrow$ Perpetual funding rate level and change ($\Delta \text{Funding Rate}$). Persistent negative funding signifies short crowding and compensation collapse; soaring positive funding signals overheating.
    - Credit risk-off (HYG/SHY) $\rightarrow$ Stablecoin peg discount or DEX-CEX basis spreads.
    - Risky drawdown $\rightarrow$ BTC/ETH rolling peak-to-trough drawdown.
- **Crypto-Specific Failure Risks:**
  - **24/7 Liquidity & Weekend Gap Risk:** Crypto markets do not close; sudden weekend cascades occur when fiat rails and traditional collateral are frozen.
  - **Stablecoin Depeg / Smart Contract Risk:** Moving to "cash" in crypto exposes capital to custodial or protocol failure rather than sovereign risk-free safety.
  - **Extreme Rebound Velocity:** Crypto market recoveries often happen within hours; an exit smoothing speed of $\eta_{exit} = 0.25$ over daily bars would cause severe upside tracking error.

## Limitations

- **Asset-Class Specificity:** Demonstrated empirically only on US equity ETFs and macroeconomic interest-rate/credit indices.
- **Fitted Component Grids:** The 2,916-configuration slow-tail grid and 216-configuration V-shape grid were structured based on historical knowledge of the 2020 and 2022 crises. While walk-forward tests re-select parameters out-of-sample, the candidate variable space itself was informed by the full historical sample.
- **Turnover Drag:** The overlay introduces significant turnover (350%–740% annualized), making it sensitive to broker commission schedules and ETF bid-ask spreads.
- **Rebound Lag:** Inherently sacrifices upside during the initial days of sharp V-bottom recoveries.

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live trading execution systems has been performed.

## Adoption boundary

`research-only`. This document is an upstream academic research capture for Hermes Research Intake Review. It does **not** constitute an approved trading strategy, does not warrant profitability, and does not authorize deployment in NautilusTrader, paper trading, demo/testnet, or live capital.

## Related Wiki records

- `[[quant/continuous-macro-timing-growth-defensive-style-allocation-2026-09-02]]` (Companion paper on G/D cross-sectional rotation, arXiv:2605.20636)
- `[[quant/relief-gated-relative-rotation-qqq-dia-interaction-filter-2026-09-02]]` (Companion paper on QQQ-DIA relative allocation, arXiv:2607.06117)
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/deflated-sharpe-ratio-multiple-testing-deflation-2026-08-28]]`

## Sources

1. Zheli Xiong. *"Continuous Cash-Overlay Filters for a Static Growth–Defensive Risk Sleeve: Slow-Tail Compensation, V-Shape Crash Brakes, Walk-Forward Validation, and Max-Cash Combination"*, arXiv preprint `arXiv:2606.09025v1 [q-fin.PM]`, June 8, 2026. DOI: `10.48550/arXiv.2606.09025`. URL: [https://arxiv.org/abs/2606.09025](https://arxiv.org/abs/2606.09025). Full text HTML: [https://arxiv.org/html/2606.09025v1](https://arxiv.org/html/2606.09025v1).
2. Zheli Xiong. GitHub repository `shaun19920309/gd-cash-overlay-filters`, commit `565c32aa42d10254fbb6aa46b044f5e70522160d` (June 14, 2026). URL: [https://github.com/shaun19920309/gd-cash-overlay-filters](https://github.com/shaun19920309/gd-cash-overlay-filters).
