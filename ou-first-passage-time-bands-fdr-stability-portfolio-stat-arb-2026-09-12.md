---
schema: strategy-research-record-v1
title: "Ornstein-Uhlenbeck Statistical Arbitrage: Diffusion First-Passage Time Optimal Bands, FDR-Corrected Split-Half Stability Selection, Estimation-Error Mean Floor, and Live Paper-Trading Verification"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - ornstein-uhlenbeck
  - first-passage-time
  - bertram-thresholds
  - false-discovery-rate
  - benjamini-hochberg
  - split-half-stability
  - estimation-error-floor
  - live-paper-audit
  - crypto-perpetuals
  - structural-break-stop
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "https://github.com/NDAR123909/ou-statarb (commit 61aa92e74e74ce9cd66c89ebe634e9a267e2873b, author Noah David Aguilar Riego, September 11, 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Ornstein-Uhlenbeck Statistical Arbitrage: Diffusion First-Passage Time Optimal Bands, FDR-Corrected Split-Half Stability Selection, Estimation-Error Mean Floor, and Live Paper-Trading Verification

## Provenance

- **Primary Source**: `NDAR123909/ou-statarb`, *"Ornstein-Uhlenbeck Pairs Trading with a Kalman-Filtered Hedge Ratio"*, open-source quantitative research and production-grade pairs trading framework (`source-reported`).
- **Repository URL**: `https://github.com/NDAR123909/ou-statarb` (`source-reported`).
- **Canonical Commit SHA**: `61aa92e74e74ce9cd66c89ebe634e9a267e2873b` (authored/tracked September 11, 2026; merge commit `972a77b62f6b86bb7881c15c545dd01a58c6bcfa` by repository creator Noah David Aguilar Riego) (`source-reported`).
- **Author**: Noah David Aguilar Riego (`NDAR123909`) (`source-reported`).
- **Publication / Last Commit Date**: September 11, 2026 (`source-reported`).
- **License**: MIT License (`source-reported`).
- **Directly Audited Core Code Paths**:
  - `statarb/thresholds.py`: Exact continuous diffusion first-passage time numerical integration for Ornstein-Uhlenbeck (OU) optimal entry/exit bands, tradeable cutoff, and sample-autocorrelation estimation-error floor (`source-reported`).
  - `statarb/selection.py`: Five-stage pairs selector: Benjamini-Hochberg False Discovery Rate (FDR) control across full candidate scans, split-half sub-window cointegration verification, hedge ratio drift tolerance, mean-crossing frequency filter, and variance-ratio Hurst exponent ceiling (`source-reported`).
  - `statarb/costs.py`: Two-leg execution cost accounting (commissions and half-spreads on both legs), daily short-borrow accrual, and square-root market impact capacity estimation (`source-reported`).
  - `statarb/ou.py`: Exact discrete AR(1) mapping for analytical OU parameter estimation ($\theta, \mu, \sigma, t_{1/2}, \sigma_{\text{eq}}$), Engle-Granger two-step cointegration testing, and event-driven backtesting engine with structural break exit (`stop_z`) and one-sided re-entry lockout (`source-reported`).
  - `statarb/portfolio.py`: Multi-pair walk-forward portfolio engine operating in dollar NAV terms, volatility-targeted position sizing, trailing adaptive z-score estimation, and portfolio gross leverage clipping (`source-reported`).
  - `statarb/kalman.py`: Dynamic two-state linear regression Kalman filter tracking time-varying hedge ratios with normalized innovation z-score generation (`source-reported`).
  - `statarb/risk.py`: Proportional Kelly-style position sizing, rolling half-life, and rolling Augmented Dickey-Fuller (ADF) regime gates (`source-reported`).
  - `statarb/walkforward.py`: Out-of-sample rolling walk-forward test harness with post-refit edge decay diagnostic (`source-reported`).
  - `deploy/run_strategy.py`: Live execution runner for daily market-close decisions with next-open fill execution (`source-reported`).
  - `PREREGISTRATION.md`: Pre-registered experimental protocol frozen on 2026-07-07 specifying hypothesis, 8 sector-restricted candidate pairs, exact sizing, costs, and a 6-month commitment window (`source-reported`).
  - `IMPROVEMENTS.md`: Documented architectural upgrades from v0.1 research to v0.2 production viability, out-of-sample empirical results on 31 large-cap equities (2006–2017), and explicit public disclosure of a prior optimization defect (`source-reported`).
  - `track_record/README.md` & `track_record/phase1_submission/REASONING_LOG.md`: Live track records across US equities (Alpaca paper trading, 47 recorded days) and crypto perpetual futures in LTP Liquidity Arena 2026 Phase I (1,000 USDT seed, 19 days of reconciled live fills, 22 scored refits) (`source-reported`).

## Economic mechanism

### Source-reported

1. **Physical Analogy of Harmonic Restoring Force**: Cointegrated asset prices share a stochastic trend driven by common macroeconomic or sector risk factors. When idiosyncratic order flow or liquidity imbalances cause the price spread to diverge, economic substitution and statistical arbitrage exert an elastic restoring force pulling the spread back toward equilibrium. This dynamic is modeled as a continuous-time Ornstein-Uhlenbeck diffusion:
   $$dX_t = \theta (\mu - X_t) dt + \sigma dW_t$$
   where $\theta > 0$ represents the mean-reversion speed (spring stiffness), $\mu$ is the long-run equilibrium level, $\sigma$ is the diffusion noise volatility, and $W_t$ is standard Brownian motion (`source-reported`).
2. **Cost-Aware First-Passage Trade Optimization**: Standard folklore pairs rules (e.g., enter at $|z| \ge 2.0$, exit at $|z| \le 0.5$) ignore the fundamental tradeoff between trade frequency and transaction costs. For a given reversion velocity $\theta$, noise $\sigma$, and round-trip trading friction $c$, there exists an optimal band pair $(a^*, b^*)$ that maximizes expected profit per unit of time ($E[\Pi] / E[\tau]$), where cycle duration $E[\tau]$ is the sum of first-passage times from entry to exit and return. When total trading costs exceed the expected reversion distance, the optimal profit rate is non-positive, and the pair is economically untradeable (`source-reported`).
3. **Multi-Testing False Discovery Elimination**: Exhaustive pairwise searches across $N$ assets test $N(N-1)/2$ combinations. Testing at nominal significance $\alpha = 0.05$ inherently admits a flood of false discoveries that appear stationary purely by sampling noise. Enforcing the Benjamini-Hochberg procedure bounds the expected proportion of false positives across the entire scan, while split-half stability verifies that the cointegrating vector represents a genuine, persistent structural relationship rather than a transient sample artifact (`source-reported`).
4. **Finite-Sample Estimation Uncertainty Floor**: Because an OU process exhibits serial autocorrelation, the effective number of independent observations is substantially smaller than the nominal sample size $n$. Measuring dislocation against a noisy sample mean can trigger entries inside estimation error, turning trades into coin flips. The entry band must therefore be lower-bounded by the standard error of the fitted mean (`source-reported`).

### Research interpretation

This framework represents a rigorous, methodologically grounded deconstruction of classical pairs trading, directly confronting the primary causes of empirical failure in live deployments:
1. **Resolution of Snooping and Overfitting**: Rather than relying on in-sample Sharpe maximization (which hand-picks the luckiest paths), candidate pairs must clear multiple independent hurdle layers: Benjamini-Hochberg FDR control, out-of-sample sub-window replication ($H_1$ and $H_2$), bounded parameter drift, and non-parametric oscillation checks (crossing counts and Hurst exponent).
2. **Integration of Microstructure Frictions into Signal Generation**: Many quantitative strategies treat friction as an afterthought applied post hoc to an idealized backtest. By embedding two-leg commissions, half-spreads, and daily short-leg borrow accrual directly into the first-passage band search, the algorithm automatically widens bands for high-cost pairs and explicitly filters out pairs where frictions consume the statistical edge.
3. **Asymmetric Risk Controls and Directional Lockouts**: The strategy explicitly guards against the catastrophic Long-Term Capital Management (LTCM) mode—where a spread continues diverging due to permanent structural breaks (e.g., bankruptcies, acquisitions, regulatory divergence)—by imposing a hard structural-break stop ($|z| \ge 3.5\sigma$) coupled with a one-sided re-entry lockout that blocks further trades on the losing side until the spread fully normalizes.

## Signal

### Mathematical Signal Construction

#### 1. Spread Definition and Exact AR(1) OU Parameter Estimation
- **Log Price Spread**:
  $$X_t = \ln(P_{A, t}) - \beta \ln(P_{B, t})$$
  where $\beta$ is estimated via Ordinary Least Squares (OLS) regression of $\ln(P_{A})$ on $\ln(P_{B})$ without look-ahead over the in-sample window (`source-reported`).
- **Exact Discrete AR(1) Representation**:
  Over discrete time step $\Delta t = 1$, the exact solution of the OU SDE is an AR(1) process without Euler approximation error:
  $$X_{t+1} = \mu (1 - b) + b X_t + \epsilon_{t+1}, \quad b = e^{-\theta \Delta t}$$
  $$\epsilon_{t+1} \sim \mathcal{N}\left(0, \frac{\sigma^2 (1 - b^2)}{2\theta}\right)$$
  Parameters are recovered analytically from OLS regression $X_{t+1} = a_0 + b X_t + \epsilon_{t+1}$:
  $$\theta = -\frac{\ln(b)}{\Delta t}, \quad \mu = \frac{a_0}{1 - b}, \quad \sigma = \sqrt{\frac{\text{Var}(\epsilon) \cdot 2\theta}{1 - b^2}}$$
  $$\text{Half-Life } t_{1/2} = \frac{\ln(2)}{\theta}, \quad \sigma_{\text{eq}} = \frac{\sigma}{\sqrt{2\theta}}$$
  If $b \le 0$ or $b \ge 1$, the spread is non-reverting and rejected ($\theta = \text{NaN}, t_{1/2} = \infty$) (`source-reported`).

#### 2. Candidate Selection Gates (Applied at Each Refit)
A candidate pair $(A, B)$ must satisfy all six filtering criteria:
1. **Economic Restriction**: Candidate universe is restricted to economically related assets (e.g., intra-sector equity pairs or same-layer crypto perpetuals) (`source-reported`).
2. **Benjamini-Hochberg FDR Control**: Across all $M$ candidate pairs tested, Augmented Dickey-Fuller (ADF) $p$-values $p_{(1)} \le p_{(2)} \le \dots \le p_{(M)}$ are screened. The discovery threshold is:
   $$k = \max \left\{ i : p_{(i)} \le \frac{i}{M} q \right\}, \quad q = 0.10 \text{ (`source-reported`)}$$
   Pairs with $p > p_{(k)}$ are rejected as false discoveries (`source-reported`).
3. **Split-Half Cointegration and Drift Stability**: The training panel of length $T$ is bisected into halves $T_1 = [1, T/2]$ and $T_2 = [T/2 + 1, T]$. Both halves must independently pass cointegration:
   $$p_{\text{ADF}}(T_1) < 0.15 \quad \text{and} \quad p_{\text{ADF}}(T_2) < 0.15 \text{ (`source-reported`)}$$
   The hedge ratio drift between halves must not exceed tolerance:
   $$\frac{|\beta_{T_1} - \beta_{T_2}|}{\max(|\beta|, 10^{-9})} \le 0.30 \text{ (`source-reported`)}$$
4. **Hedge Ratio Boundary**: $0.25 \le |\beta| \le 4.0$ to eliminate degenerate or extreme exposures (`source-reported`).
5. **Half-Life Window**: $3.0 \le t_{1/2} \le 50.0$ trading days for daily equity bars ($6.0 \le t_{1/2} \le 168.0$ hours for crypto perpetuals) (`source-reported`).
6. **Oscillation and Anti-Persistence Diagnostics**:
   - Mean-crossing frequency: $\ge 8.0$ crossings per year (`source-reported`).
   - Hurst exponent $H$ (via variance-of-differences): $H \le 0.47$, verifying anti-persistence independently of ADF (`source-reported`).

#### 3. First-Passage Time Optimal Band Search with Estimation Floor
- **Expected First-Passage Time Integral**:
  For an OU process standardized to resting width $\sigma_{\text{eq}} = 1$ ($dX_t = -\theta X_t dt + \sqrt{2\theta} dW_t$), the expected time $E[\tau(x_0 \to \text{target})]$ to first hit $\text{target}$ from $x_0$ ($x_0 < \text{target}$) is computed numerically via scale and speed densities:
  $$E[\tau(x_0 \to \text{target})] = 2 \int_{x_0}^{\text{target}} s'(y) \left[ \int_{-\infty}^y m(z) dz \right] dy$$
  $$s'(y) = \exp\left( \frac{\theta y^2}{\sigma^2} \right), \quad m(z) = \frac{1}{\sigma^2} \exp\left( -\frac{\theta z^2}{\sigma^2} \right)$$
  Using error function substitution, the inner integral evaluates to:
  $$\int_{-\infty}^y m(z) dz = \frac{1}{2\sigma^2} \sqrt{\frac{\pi}{k}} \left( 1 + \text{erf}\left( y \sqrt{k} \right) \right), \quad k = \frac{\theta}{\sigma^2}$$
  Downwards passage is symmetric: $E[\tau(x_0 \to \text{target})] = E[\tau(-x_0 \to -\text{target})]$ (`source-reported`).
- **Optimal Band Formulation**:
  For entry multiple $a$ and exit multiple $b$ (in units of $\sigma_{\text{eq}}$), the cycle duration is $T_{\text{cycle}}(a, b) = E[\tau(-a \to -b)] + E[\tau(-b \to -a)]$.
  Net profit per completed round trip in $z$-units is:
  $$\Pi_{\text{net}}(a, b) = (a - b) - \frac{c_{\text{rt}}}{\sigma_{\text{eq}}}$$
  where $c_{\text{rt}}$ is total round-trip friction in spread units (`source-reported`).
  The optimal band maximizes profit rate:
  $$(a^*, b^*) = \arg\max_{a, b} \frac{\Pi_{\text{net}}(a, b)}{T_{\text{cycle}}(a, b)}$$
  over grid $a \in [0.4, 3.0]$ (step $0.2$) and $b \in [0.0, 1.5]$ (step $0.25$) with $b \le a - 0.1$ (`source-reported`).
- **Estimation-Error Floor**:
  Because sample mean uncertainty on an autocorrelated AR(1) series has standard error:
  $$\text{SE}(\hat{\mu}) = \sigma_{\text{eq}} \sqrt{\frac{1 + \phi}{(1 - \phi) n}}, \quad \phi = e^{-\theta}$$
  the search enforces an entry band floor $a \ge \text{min\_entry\_se} \times \text{SE}(\hat{\mu}) / \sigma_{\text{eq}}$ with $\text{min\_entry\_se} = 1.0$, preventing entries inside the noise of the fitted mean (`source-reported`).
- **Tradeability Gate**: If $\max \frac{\Pi_{\text{net}}}{T_{\text{cycle}}} \le 0$, the pair is flagged untradeable and skipped (`source-reported`).

#### 4. Trailing Z-Score, Execution Triggers, and Risk Blocks
- **Rolling Lookback Window**: $W_z = \text{clip}(\text{round}(3.0 \times t_{1/2}), 15, T_{\text{train}}/2)$ (`source-reported`).
- **Trailing Z-Score**:
  $$z_t = \frac{X_t - \mu_{\text{rolling}, t}}{\sigma_{\text{rolling}, t}}$$
- **Entry Triggers**:
  - Long Spread: $z_t < -a^*$ and Longs Not Blocked (`source-reported`).
  - Short Spread: $z_t > a^*$ and Shorts Not Blocked (`source-reported`).
- **Exit Triggers**:
  - Mean Reversion: $|z_t| \le b^*$ (`source-reported`).
  - Maximum Hold: Holding duration exceeds $3.0 \times t_{1/2}$ (stale trade termination) (`source-reported`).
  - Refit Drop: Pair fails to clear re-selection at scheduled refit; open position flattened immediately (`source-reported`).
- **Structural Break Stop and Directional Re-Entry Lockout**:
  - Stop trigger: $|z_t| \ge 3.5$ (`source-reported`).
  - If long spread is stopped out ($z_t \le -3.5$), position is closed and long entries are blocked until $z_t > -a^*$ (`source-reported`).
  - If short spread is stopped out ($z_t \ge +3.5$), position is closed and short entries are blocked until $z_t < a^*$ (`source-reported`).

#### 5. Position Sizing and Portfolio Gross Leverage Cap
- **Volatility-Targeted Sizing**:
  $$g = \frac{\text{risk\_per\_pair\_bps} \times 10^{-4} \times \text{NAV}}{\text{daily\_spread\_vol}_t}$$
  where $\text{risk\_per\_pair\_bps} = 10.0$ bps ($0.10\%$ daily NAV risk) and $\text{daily\_spread\_vol}_t$ is rolling standard deviation of $\Delta X_t$ over window $W_z$ (`source-reported`).
- **Leg Dollar Notional**:
  - Long Spread: Long Asset $A$ with notional $\$g$; Short Asset $B$ with notional $\$g \cdot \beta$ (`source-reported`).
  - Short Spread: Short Asset $A$ with notional $\$g$; Long Asset $B$ with notional $\$g \cdot \beta$ (`source-reported`).
  - Dollar unit $g$ is locked at trade entry to prevent intra-trade volatility churning (`source-reported`).
- **Portfolio Gross Leverage Cap**: Total gross leverage $\frac{\sum |w_A| + |w_B|}{\text{NAV}}$ is capped at $4.0\times$ in equity backtests ($3.0\times$ in live paper trading, $2.0\times$ in crypto venue rules). If gross exceeds the cap, daily PnL and exposures are scaled down proportionally (`source-reported`).

## Required data

- **Instruments**:
  - *Equities*: US Large-Cap liquid equities organized into strict industry sector groupings (DJIA 31 names, S&P 500 constituents) (`source-reported`).
  - *Crypto Perpetuals*: Liquid USD/USDT-margined perpetual swap contracts (e.g., BTC, ETH, SOL, XRP, KAS, ETC) on institutional/retail exchanges (OKX, Binance) (`source-reported`).
- **Price Fields**: Split- and dividend-adjusted daily close prices for equities; 1-hour OHLCV klines for crypto perpetuals (`source-reported`).
- **Data Alignment & Frequency**:
  - Daily close for equities; signals formed post-close at ~21:35 UTC (`source-reported`).
  - Hourly bar boundaries for crypto perpetuals (`source-reported`).
  - Missing/NaN handling: Zero-tolerance; any series containing NaNs, infinite values, or zero standard deviation (halted/untraded) is immediately flagged degenerate and rejected with $p=1.0$ (ensuring it is counted in FDR multi-testing correction) (`source-reported`).
- **Funding & Borrow Data**:
  - Annualized equity short-borrow fee rate: modeled at flat 50 bps/year for general collateral (GC) liquid names (`source-reported`).
  - Crypto funding rates: 8-hour settlement cash flows tracked and credited/debited directly to NAV (`source-reported`).

## Execution assumptions

- **Order Timing & Lag**:
  - *Equities*: Daily signals computed at the close; market orders submitted during post-market hours and execute at the next market open (`source-reported`). This overnight execution lag is strictly modeled and preserved.
  - *Crypto Perpetuals*: Orders execute at the subsequent hourly bar open via taker/market orders (`source-reported`).
- **Transaction Costs (Two-Leg Model)**:
  - Commission: 0.5 bps per leg per trade ($0.005\%$) (`source-reported`).
  - Effective Half-Spread: 1.5 bps per leg per trade ($0.015\%$) (`source-reported`).
  - All-in turnover cost per leg: 2.0 bps ($0.020\%$), amounting to $4.0 \times (1 + |\beta|)$ bps per round-trip spread unit (`source-reported`).
- **Short Borrow Accrual**: Daily short borrowing cost charged on aggregate short notional at 50 bps/year:
  $$\text{Borrow Cost}_t = \text{Short Notional}_t \times \frac{0.0050}{252} \text{ (`source-reported`)}$$
- **Market Impact & Capacity Sanity Check**:
  Square-root market impact ceiling based on average daily volume (ADV) and 1% participation cap:
  $$\text{Cap} = \min\left(0.01 \times \text{ADV}, \left(\frac{\text{max\_impact\_bps}}{\text{impact\_coeff} \times \text{daily\_vol}}\right)^2 \times \text{ADV}\right) \text{ (`source-reported`)}$$
  with $\text{impact\_coeff} = 0.1$, $\text{max\_impact\_bps} = 2.0$ bps (`source-reported`).
- **Signal-to-Execution Assumptions Classified**:
  - Next-open fill model: `source-reported` (preserves realistic overnight execution lag).
  - Commission schedule ($0.5$ bps) and half-spread ($1.5$ bps): `source-reported`.
  - Borrow fee ($50$ bps/year GC flat): `source-reported` (identified as an empirical lower bound; hard-to-borrow names carry substantially higher fees).

## Evidence

### Source-reported

All quantitative figures below trace directly to the audited code, markdown disclosures, and committed run logs of `NDAR123909/ou-statarb`:

#### 1. Out-of-Sample Walk-Forward Portfolio on US Large Caps (2006–2017)
Conducted on 31 Dow Jones Industrial Average (DJIA) constituents across 19 rolling walk-forward folds (504 trading days training, 126 days testing, 8 candidate sectors, 42 intra-sector candidate pairs) under the full two-leg cost and borrow model (`source-reported` in `examples/real_data_portfolio.py` and `IMPROVEMENTS.md`):
- **Net Sharpe Ratio**: **0.36** (annualized, net of all commissions, half-spreads, and daily borrow fees) (`source-reported`).
- **Annual Return on NAV**: **1.07%** (`source-reported`).
- **Maximum Drawdown on NAV**: **-5.13%** (`source-reported`).
- **Friction Drag**: Total costs paid equaled **15%** of gross PnL (`source-reported`).
- **Average Gross Leverage**: **0.37x** (`source-reported`).
- **Selection Selectivity**: Only 20 pair-folds traded out of ~800 tested across folds; the multi-stage selector rejected **~97%** of candidate pairs (`source-reported`).

#### 2. Disclosure and Correction of Optimization Defect (2026-07-28)
The author publicly documented that prior versions of `statarb/thresholds.py` reported an inflated net Sharpe of **0.44** with 10% cost drag. Investigation revealed that the grid search compared a raw candidate rate against an incumbent profit rate stored in spread units ($\text{rate} \times \sigma_{\text{eq}}$). With $\sigma_{\text{eq}} \approx 0.03$, the acceptance hurdle was deflated by $\sim 30\times$, causing the optimizer to walk to the largest feasible grid cell rather than the true optimum. This resulted in an artificially wide entry band where the book was almost never active (average gross leverage of 0.02x). Correcting the comparison metric restored active trading (gross leverage 0.37x) and established the honest, uninflated net Sharpe of 0.36 (`source-reported` in `IMPROVEMENTS.md`).

#### 3. Live US Equities Paper-Trading Preregistration (Alpaca Bridge)
From 2026-07-07 to 2026-09-11 (47 trading days recorded in `track_record/equity.csv`):
- **Total Fills**: **0** (`source-reported`).
- **Current Equity**: $100,000.00 (+0.00% return, 0.00% max drawdown) (`source-reported`).
- **Mechanism of Restraint**: Across 8 frozen intra-sector candidate pairs (`V/MA`, `KO/PEP`, `XOM/CVX`, `HD/LOW`, `UPS/FDX`, `GS/MS`, `UNP/CSX`, `MCD/YUM`), the combination of Benjamini-Hochberg FDR control, split-half stability, and cost-aware first-passage optimization rejected all pairs during the live summer 2026 regime, preventing capital deployment into unfavorable risk-reward spreads (`source-reported`).

#### 4. Live Crypto Perpetuals Deployment (LTP Liquidity Arena 2026 Phase I)
Live execution from 2026-07-20 to 2026-08-21 on perpetual contracts with 1,000 USDT seed (`source-reported` in `track_record/phase1_submission/REASONING_LOG.md`):
- **Refit Pass Distribution**: Across 22 scored weekly refits over 15 candidate pairs, a mean of only **0.91 pairs** passed selection; exactly 1 pair passed 59% of the time, and **0 pairs passed 27% of the time**. Only 5 of 15 candidates ever cleared the selection gate (`source-reported`).
- **Execution Reconciliations**: 19 consecutive daily fill logs (`fills/fills_2026-08-02.json` to `2026-08-20.json`) reconciled against exchange transaction execution records to within 0.11 USDT across 11 round trips (`source-reported`).
- **Funding Rate Impact**: Net funding received was **+0.34 to +0.39 USDT** across ~96 eight-hour settlement intervals (positive carry contributing ~0.04% to NAV) (`source-reported`).
- **Falsification of Early Streak Metrics**: Early in the deployment, a low-variance streak across ~14 daily returns generated a headline Sharpe $> 9.0$. The authors documented that this was a small-sample statistical artifact: a single $-0.8\%$ daily loss arithmetic dropped the Sharpe to 5.66, demonstrating that short-window Sharpe figures are uninterpretable noise (`source-reported`).
- **Risk Gate Activation**: The one-sided re-entry lockout after a 3.5σ stop fired in double digits, actively suppressing re-entries into runaway spread divergences (`source-reported`).

### Independently reproduced

Not independently reproduced. All metrics reflect third-party reported backtests, pre-registered logs, and live execution reconciliations from `NDAR123909/ou-statarb`.

### Negative evidence

1. **Severe Degradation from Search Multiplicity**: Running pairs selection without FDR correction tests 465 pairs at $p < 0.05$ and admits $\sim 23$ false positives purely by chance. In-sample Sharpe sorting systematically hand-picks the most overfit noise paths (`source-reported`).
2. **Kalman Filter Drift Inefficiency on Constant-Beta Spreads**: In Monte Carlo simulations across 100 synthetic pairs with static true hedge ratios ($\text{drift} = 0$), the dynamic Kalman filter produced inferior out-of-sample Sharpe compared to frozen OLS, as the filter's observation variance introduced unnecessary estimation tracking noise (`source-reported` in `examples/demo_kalman.py`).
3. **Capacity Constraints and Friction Erosion**: In the 2006–2017 DJIA backtest, transaction costs and borrow fees erased 15% of gross PnL. For mid- or small-cap pairs, borrow rates of 1–10% annually completely eliminate the statistical arbitrage margin (`source-reported`).
4. **Single-Pair Concentration vs Portfolio Breadth**: The live crypto deployment demonstrated that trading a single pair at a time leaves the strategy vulnerable to idiosyncratic regime shifts. A positive net edge requires diversification across multiple uncorrelated sectors/pairs (`source-reported`).

## Falsification plan

To falsify the hypothesis that first-passage time optimal bands with FDR-controlled stability generate persistent statistical arbitrage alpha:

1. **Placebo Shuffled-Spread Test**: Randomly shuffle the temporal alignment of constituent return series while preserving marginal volatility distributions. If the FDR selector and optimal band engine yield a positive annualized Sharpe exceeding `0.10` (`research-defined falsification threshold`), the selection filters are failing to distinguish true cointegration from spurious correlation.
2. **Transaction Cost Escalation Stress**: Scale two-leg trading frictions from 2.0 bps to 6.0 bps per leg and short borrow from 50 bps to 200 bps/year. If the optimal bands fail to automatically reject pairs or if portfolio net Sharpe drops below `0.0` (`research-defined falsification threshold`) over the 2006–2017 benchmark panel, the cost-gating mechanism is invalidated.
3. **Estimation Floor Ablation**: Set $\text{min\_entry\_se} = 0.0$ (disabling the estimation-error floor). If out-of-sample Sharpe increases significantly, the hypothesis that entering inside parameter uncertainty degrades performance is disproven; if Sharpe collapses, the necessity of the estimation floor is validated (`research-proposed`).
4. **Structural Break Stop Evaluation**: Remove the 3.5σ stop and directional re-entry lockout. If portfolio maximum drawdown does not worsen during major macro dislocation events (e.g., 2008 Lehman collapse or March 2020 crash), the hypothesis that structural stops prevent catastrophic left-tail losses is falsified (`research-defined falsification threshold`).

## Crypto portability

- **Portability Status**: `direct` (`source-reported` empirical implementation and live deployment in LTP Liquidity Arena Phase I).
- **Crypto-Specific Adaptation Realities**:
  - *Timescale and Half-Life Compression*: Unlike equity pairs that operate on daily closes with half-lives of 3–50 days, crypto perpetual spreads operate on hourly bars with half-lives compressed to 6–168 hours (`source-reported`).
  - *24/7 Continuous Trading & Session Boundaries*: Eliminates overnight gap risk present in equities, allowing continuous monitoring of the 3.5σ stop and mean-reversion exit targets (`source-reported`).
  - *Funding Rate Integration*: Perpetual contracts incur periodic (typically 8-hour) funding payments. When holding long spread ($+A, -B$), if asset $B$'s funding rate exceeds asset $A$'s funding rate, the trade earns positive carry. While the live deployment captured net positive funding (+0.34 to +0.39 USDT), funding spreads can invert rapidly during directional market momentum, requiring explicit funding rate modeling in the cost hurdle (`research-proposed`).
  - *De-Peg and Delisting Risks*: Crypto tokens face acute tail risks from protocol insolvencies or exchange de-listings. The one-sided re-entry lockout is vital to prevent doubling down into terminal dislocations (`source-reported`).

## Limitations

- `underspecified`: Fixed 50 bps/year short borrow fee in equities is a stylized assumption; actual locate fees fluctuate dynamically and can spike past 20% on crowded shorts (`source-reported`).
- `data gap`: Pre-2026-08-02 crypto executions lack tick-level slippage data due to exchange API retention limits (`source-reported`).
- `unproven`: Portfolio breadth in crypto remains unproven; the live tournament ran a single pair at a time rather than the modeled multi-pair book (`source-reported`).
- `not independently reproduced`: All empirical performance figures reflect third-party reported backtests and live competition logs (`source-reported`).

## Implementation status

- Frontmatter status: `not-implemented`.
- This research record represents an external quantitative capture and forensic analysis. No strategy implementation has been committed to NautilusTrader, PyBroker, or internal execution engines.
- Paper, Testnet, or Live deployment within our proprietary stack has not been authorized.

## Adoption boundary

- Status: `research-only`.
- Adoption: `not-approved`.
- Approval Scope: `research-only`.
- Presence in this repository indicates that the research capture satisfies source provenance, econometric rigor, and falsification requirements. It does not constitute approval for capital allocation, paper trading, or live execution.

## Related Wiki records

- `[[quant/sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12]]`: Statistical arbitrage on S&P 500 sectors using causal residualization and PCA hedge ratios.
- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]`: Forensic audit of Kalman filter unbounded hedge ratio failures and phantom PnL.
- `[[quant/crypto-perpetual-pairs-trading-cointegration-hurst-halflife-walkforward-2026-09-12]]`: Cointegration and rolling Hurst exponent pairs trading on crypto perpetuals.
- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]`: Johansen basket cointegration and White's Reality Check multiple testing corrections.

## Sources

1. **GitHub Repository**: Noah David Aguilar Riego (`NDAR123909`), *"ou-statarb: Ornstein-Uhlenbeck Pairs Trading with a Kalman-Filtered Hedge Ratio"*, commit `61aa92e74e74ce9cd66c89ebe634e9a267e2873b` (dated September 11, 2026).
   - URL: https://github.com/NDAR123909/ou-statarb
2. **Code Implementation Modules**:
   - `statarb/thresholds.py`: Bertram-style exact first-passage time optimal bands and estimation error mean floor.
   - `statarb/selection.py`: Benjamini-Hochberg FDR correction and split-half stability filter.
   - `statarb/costs.py`: Two-leg execution cost model and borrow accrual.
   - `statarb/ou.py`: Exact discrete AR(1) OU estimation and structural-break stop engine.
   - `statarb/portfolio.py`: Out-of-sample walk-forward dollar-based portfolio engine.
   - `statarb/kalman.py`: Dynamic regression Kalman filter for drifting hedge ratios.
   - `deploy/run_strategy.py` & `quantconnect/main.py`: Production deployment implementations.
3. **Empirical and Research Documentation**:
   - `IMPROVEMENTS.md`: Architectural upgrades, 2006–2017 DJIA empirical results, and 2026-07-28 optimization bug disclosure.
   - `PREREGISTRATION.md`: Live paper-trading preregistration protocol (frozen 2026-07-07).
   - `track_record/phase1_submission/REASONING_LOG.md`: LTP Liquidity Arena 2026 Phase I crypto perpetuals live audit, refit pass rates, and fill reconciliations.
