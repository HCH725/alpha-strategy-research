---
schema: strategy-research-record-v1
title: "Crude Oil 3:2:1 Crack Spread Seasonally Adjusted Mean Reversion with Stop-Loss Re-Entry Lockout"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - commodity-futures
  - crack-spread
  - statistical-arbitrage
  - mean-reversion
  - seasonal-adjustment
  - ornstein-uhlenbeck
  - stop-lockout
status: research-only
confidence: high
source_as_of: 2026-09-06
sources:
  - "https://github.com/rudraakshreddy/petroquant-alpha/tree/71ecf936b106dc2e58df2881524b59510450bcd9"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crude Oil 3:2:1 Crack Spread Seasonally Adjusted Mean Reversion with Stop-Loss Re-Entry Lockout

## Provenance

- **Primary Source:** Yeddula Rudraaksh Reddy (primary/corresponding author, `yeddularudraaksh@gmail.com`) and S. N. Chakri (`snchakrim@gmail.com`), *"A Seasonally Adjusted Mean-Reversion System for the 3:2:1 Crude Oil Crack Spread"*, Technical Report and public research repository `rudraakshreddy/petroquant-alpha`, committed September 6, 2026 (`source-reported`).
- **Repository URL:** [https://github.com/rudraakshreddy/petroquant-alpha](https://github.com/rudraakshreddy/petroquant-alpha)
- **Immutable Commit SHA:** `71ecf936b106dc2e58df2881524b59510450bcd9`
- **Key Code & Specification Paths Audited:**
  - Configuration & Hyperparameters: [`config.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/config.py)
  - Spread Calculation & Gallon-to-Barrel Conversions: [`src/spread_construction.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/spread_construction.py)
  - Diagnostic Statistical Tests (ADF, KPSS, Hurst, OU): [`src/statistical_tests.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/statistical_tests.py)
  - Signal Generation & Re-Entry Lockout State Machine: [`src/signal_generation.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/signal_generation.py)
  - Event-Loop Backtester & Transaction Cost Accounting: [`src/backtester.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/backtester.py)
  - Empirical Metrics & Trade Audit: [`results/tables/performance_metrics.json`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/results/tables/performance_metrics.json)
  - Walk-Forward Grid Parameter Sweep: [`results/tables/parameter_sweep_results.csv`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/results/tables/parameter_sweep_results.csv)
  - Technical Paper PDF: [`report/petroquant_report.pdf`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/report/petroquant_report.pdf)
- **License:** Apache License 2.0 (`source-reported`).
- **Primary Source Verification:** All code files, module implementations, configuration dataclasses, empirical metric tables, and documentation in commit `71ecf936b106dc2e58df2881524b59510450bcd9` were directly fetched and audited. No secondary search snippets, marketing summaries, or model-generated synthetic approximations were used to populate strategy rules or empirical statistics.
- **Repository Deduplication Audit:** A full audit of all existing records in `alpha-strategy-research` confirmed zero matching records for `petroquant`, Yeddula Rudraaksh Reddy, S. N. Chakri, or the 3:2:1 crude oil crack spread mean-reversion system. Related relative-value records in the repository (`commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02.md`, `convex-cross-impact-transient-execution-relative-value-2026-09-08.md`) examine graph neural networks for intraday calendar spreads and convex cross-impact transient decay models on crude futures roll periods; neither implements expanding harmonic deseasonalization, state-machine stop re-entry suppression, or the physical 3:2:1 refinery margin cointegration structure.

## Economic mechanism

### Source-reported

1. **Refinery Margin Thermodynamic & Economic Equilibrium:**
   A standard North American refinery operates approximately on a $3:2:1$ volumetric yield: three 42-gallon barrels of crude oil are processed into roughly two barrels of gasoline and one barrel of distillate (heating oil / diesel). The $3:2:1$ crack spread represents the synthetic *gross refining margin* per barrel of crude processed:
   $$S_t = \frac{2 \cdot \text{RBOB}_t + \text{HO}_t - 3 \cdot \text{WTI}_t}{3} \quad [\$/\text{bbl}]$$
   where gasoline ($\text{RBOB}_t$) and distillate ($\text{HO}_t$) are quoted in $\$ /\text{gal}$ and converted to $\$ /\text{bbl}$ via multiplying by 42, while crude oil ($\text{WTI}_t$) is quoted directly in $\$ /\text{bbl}$.
   
   Economic theory dictates that this spread must mean-revert over intermediate horizons due to supply-demand balancing:
   - When refining margins are excessively high (spread too wide), refiners face powerful economic incentives to maximize crude distillation capacity utilization. This simultaneously surges crude oil feedstock demand (raising crude prices) and increases finished product supply in wholesale distribution hubs (depressing gasoline and distillate prices), compressing the margin back toward normal operating conversion costs.
   - When margins compress or turn negative, refiners throttle throughput, bring forward scheduled turnaround maintenance, or temporarily shutter uneconomic units. Reduced product supply and curtailed crude demand subsequently force the crack spread to expand back toward equilibrium.

2. **Annual Seasonal Cycle vs. Disequilibrium:**
   Refining margins exhibit a strong, predictable annual cycle driven by the northern hemisphere summer driving season (high gasoline demand), winter heating oil demand, and spring/autumn refinery maintenance turnarounds. The primary harmonic component of this seasonal cycle has an amplitude of $\approx \$4.55/\text{bbl}$ against a total sample standard deviation of $\$10.99/\text{bbl}$ (`source-reported`).
   A standard z-score calculated on the raw spread reads this annual oscillation as genuine disequilibrium, repeatedly taking contrarian positions against predictable seasonal swings. To correct this, the signal is computed on the deseasonalized residual of an expanding-window harmonic regression using historical data only:
   $$\widehat{S}_t^{\text{seas}} = c_0 + a_1 \sin\left(\frac{2\pi d_t}{365.25}\right) + b_1 \cos\left(\frac{2\pi d_t}{365.25}\right)$$
   Crucially, deseasonalization is applied *only to signal generation*; all strategy P&L is marked strictly on the actual traded, unadjusted market spread.

3. **Reconciling Conflicting Stationarity Diagnostics:**
   Diagnostic tests over the 2019–2024 sample (1,510 trading days) produce seemingly contradictory results:
   - Augmented Dickey-Fuller (ADF): test statistic $-2.28$, $p = 0.178 \implies$ cannot reject unit root (`source-reported`).
   - KPSS test: level statistic $2.04$, trend statistic $0.63$, both $p < 0.01 \implies$ rejects stationarity (`source-reported`).
   - Hurst exponent (Rescaled Range $R/S$): $H \approx 0.97 \implies$ persistent long memory (`source-reported`).
   - Ornstein-Uhlenbeck (OU) regression: $\Delta S_t = \kappa (\theta - S_t)\Delta t + \sigma \Delta W_t$, estimated drift $\beta = -0.0246$, $t = -4.34 \implies$ statistically significant mean reversion with half-life $\tau = \ln(2) / 0.0246 = 28.18 \approx 28.2$ trading days (`source-reported`).
   
   The authors reconcile this: over a multi-year horizon, the crack spread does not fluctuate around a static global constant. It underwent massive macro regime dislocations during the 2020 COVID demand collapse (WTI briefly turned negative while cracks spiked) and the 2022 European energy crisis / refining bottleneck (cracks reached $\$68.77/\text{bbl}$). The spread exhibits *local mean reversion toward a migrating equilibrium*. Rolling OU fits show finite mean-reversion half-lives (median 24.6 trading days) over $\approx 80\%$ of the historical sample, failing only across major macro transition boundaries.

4. **The Stop-Loss Re-Entry Latch:**
   In naive threshold-based mean-reversion systems where entry is triggered at $|z| > \theta_{\text{entry}}$ (e.g. 2.0) and stop-loss at $|z| > \theta_{\text{stop}}$ (e.g. 4.0), a severe flaw arises: because $\theta_{\text{stop}} > \theta_{\text{entry}}$, any market bar that trips the stop-loss *simultaneously satisfies the entry condition*. A standard stateless stop closes the position and immediately reopens it on the same bar, leaving exposure active and rendering risk management completely vacuous.
   The primary source designs a state-machine latch: when the stop-loss fires, the system transitions to a locked state that suppresses all subsequent re-entries until the deviation fully normalizes back below the entry threshold ($|z| < \theta_{\text{entry}}$).

### Research interpretation

- **Structural Bounds of Relative-Value Production Equivalence:**
  The 3:2:1 crack spread is an economic production function arbitrage rather than an econometric correlation artifact. Unlike arbitrary equity pairs that can drift apart indefinitely due to idiosyncratic corporate actions, the input (crude) and outputs (gasoline, distillate) are tethered by the physical replacement and operational costs of the global refining complex.
- **Deseasonalization as Causal Signal Isolation:**
  Extracting predictable seasonal cycles via an expanding harmonic filter strips out deterministic drift without introducing look-ahead bias. By marking P&L on the actual spread, the model avoids the pitfall of assuming synthetic fills.
- **Time Stop as Model Validity Boundary:**
  Enforcing a hard time exit at twice the fitted OU half-life ($2 \times 28.2 \approx 56$ trading sessions) operationalizes a falsification boundary: if a spread deviation fails to revert within two theoretical half-lives, the local mean-reversion hypothesis is assumed empirically invalid for that episode.

## Signal

The signal architecture operates as a discrete-state automaton on daily closing settlement prices (`source-reported`):

1. **Spread Construction (`source-reported`):**
   $$S_t = \frac{2 \cdot (\text{RBOB}_t \times 42) + 1 \cdot (\text{HO}_t \times 42) - 3 \cdot \text{WTI}_t}{3}$$
   where $\text{WTI}$ is CME CL front-month, $\text{RBOB}$ is CME RB front-month, and $\text{HO}$ is CME HO front-month futures settlement prices.

2. **Expanding-Window Seasonal Deseasonalization (`source-reported`):**
   - For day $t$ with day-of-year $d_t \in [1, 366]$:
     $$\widehat{S}_t^{\text{seas}} = c_0 + a_1 \sin\left(\frac{2\pi d_t}{365.25}\right) + b_1 \cos\left(\frac{2\pi d_t}{365.25}\right)$$
   - Minimum training window: $\text{min\_train} = 504$ trading days ($\approx 2$ years) before first estimation (`source-reported`).
   - Estimation discipline: Ordinary Least Squares (OLS) fitted strictly on the expanding history $s \in [0, t-1]$, refitted once annually at the start of each calendar year (`source-reported`).
   - Signal residual series: $u_t = S_t - \widehat{S}_t^{\text{seas}}$ for $t \ge 504$; NaN prior to warm-up.

3. **Rolling Z-Score Formulation (`source-reported`):**
   $$z_t = \frac{u_t - \mu_{t, w}}{\sigma_{t, w}}$$
   where $\mu_{t,w}$ and $\sigma_{t,w}$ are the rolling mean and sample standard deviation of $u_t$ over lookback window $w = 30$ trading days (selected via walk-forward sweep; minimum valid periods $w // 2 = 15$) (`source-reported`).

4. **State-Machine Trading Rules (`source-reported`):**
   At each settlement close $t$, given current state $\text{pos}_t \in \{-1, 0, +1\}$, session hold counter $\text{held}_t \in \mathbb{N}_0$, and latch flag $\text{locked}_t \in \{\text{True}, \text{False}\}$:
   - **Normal Exit:**
     - If $\text{pos}_t == +1$ and $z_t > -0.5 \implies \text{pos}_{t+1} = 0, \text{held}_{t+1} = 0$.
     - If $\text{pos}_t == -1$ and $z_t < +0.5 \implies \text{pos}_{t+1} = 0, \text{held}_{t+1} = 0$.
   - **Hard Stop-Loss with Latch:**
     - If $|z_t| > 4.0 \implies \text{pos}_{t+1} = 0, \text{held}_{t+1} = 0, \text{locked}_{t+1} = \text{True}$.
   - **Time Stop:**
     - If $\text{pos}_t \ne 0$ and $\text{held}_t \ge 56$ sessions ($2 \times \text{OU half-life}$) $\implies \text{pos}_{t+1} = 0, \text{held}_{t+1} = 0$.
   - **Lockout Release:**
     - If $\text{locked}_t == \text{True}$ and $|z_t| < 2.0 \implies \text{locked}_{t+1} = \text{False}$.
   - **Entry (permitted only from flat and unlocked state):**
     - If $\text{pos}_t == 0$ and $\text{locked}_t == \text{False}$:
       - If $z_t < -2.0 \implies \text{pos}_{t+1} = +1, \text{held}_{t+1} = 0$ (Long crack spread: buy 2 RBOB, buy 1 HO, sell 3 WTI).
       - If $z_t > +2.0 \implies \text{pos}_{t+1} = -1, \text{held}_{t+1} = 0$ (Short crack spread: sell 2 RBOB, sell 1 HO, buy 3 WTI).
   - If position maintained: $\text{held}_{t+1} = \text{held}_t + 1$.

5. **Execution Lag (`source-reported`):**
   Target position for execution is strictly lagged by one full trading day:
   $$\text{position\_exec}_t = \text{position}_{t-1}$$
   Signals calculated using settlement prices at close of day $t$ are entered at close of day $t+1$. P&L begins accumulating on day $t+2$.

6. **Position Sizing (`source-reported`):**
   Daily volatility-targeted sizing against trailing 20-day standard deviation of daily crack spread changes ($\sigma_{\text{crack}, 20}$):
   $$N_{\text{bbl}} = \max\left(1000, 1000 \cdot \left\lfloor \frac{0.01 \cdot \text{NAV}_t}{1000 \cdot \sigma_{\text{crack}, 20}} \right\rfloor\right)$$
   where each CME contract equals 1,000 barrels (`CONTRACT_SIZE_BBL = 1000`). Positions scale inversely with market volatility.

## Required data

- **Instruments (`source-reported`):**
  - Light Sweet Crude Oil Futures (CME / NYMEX: `CL=F`): front-month contract, quoted in USD per barrel ($\$ /\text{bbl}$), 1,000 barrels per contract.
  - RBOB Gasoline Futures (CME / NYMEX: `RB=F`): front-month contract, quoted in USD per gallon ($\$ /\text{gal}$), 42,000 gallons per contract (1,000 bbl equivalent).
  - New York Harbor Ultra-Low Sulfur Diesel / Heating Oil Futures (CME / NYMEX: `HO=F`): front-month contract, quoted in USD per gallon ($\$ /\text{gal}$), 42,000 gallons per contract (1,000 bbl equivalent).
- **Timeframe & Fields (`source-reported`):** Daily settlement closing prices.
- **Sample Period (`source-reported`):** January 2, 2019 to December 30, 2024 (1,510 trading days).
- **Calendar Alignment (`source-reported`):** Outer intersection of trading calendars across the three CME energy contracts ($99.9\%$ date coincidence). Missing entries dropped.
- **Conversion Factor (`source-reported`):** Exactly 42.0 US gallons per petroleum barrel (`GALLONS_PER_BARREL = 42`).
- **Point-in-Time Discipline (`source-reported`):** Daily settlement prices only; harmonic coefficients re-estimated once per year on historical data preceding day $t$; 1-day execution lag ensures zero same-bar look-ahead.

## Execution assumptions

- **Execution Model (`source-reported`):** Trades executed at the daily settlement price on day $t+1$ following a day $t$ signal trigger.
- **Transaction Costs (`source-reported`):**
  - Bid-Ask Slippage: $\$0.05 / \text{bbl}$ charged on entry and exit (`SLIPPAGE_PER_BBL = 0.05`).
  - Commission: $\$2.50 / \text{contract}$ round-trip charged across legs (`COMMISSION_PER_CONTRACT = 2.50`).
  - Roll Cost: $\$0.02 / \text{bbl}$ per monthly contract expiration boundary crossed while in a trade (`ROLL_COST_PER_BBL = 0.02`).
  - Total Backtest Costs Paid: $\$44,520.00$ ($4.45\%$ of starting capital) (`source-reported`).
- **Initial Capital (`source-reported`):** $\$1,000,000.00$ USD (`INITIAL_NAV`).
- **Risk-Free Rate (`source-reported`):** $5.0\%$ annualized (`RISK_FREE_RATE = 0.05`), calibrated to average 2019–2024 US Treasury yields.
- **Execution Caveats (`source-reported` limitation):** Fills assume full execution at published daily settlement with constant slippage. Does not incorporate market-impact models or liquidity degradation during extreme tail events (such as the April 2020 negative WTI settlement or the 2022 refining dislocation).

## Evidence

### Source-reported

All metrics trace directly to the primary source repository (`rudraakshreddy/petroquant-alpha`, commit `71ecf936b106dc2e58df2881524b59510450bcd9`, files `results/tables/performance_metrics.json`, `results/tables/parameter_sweep_results.csv`, `README.md`, and `report/petroquant_report.pdf`):

1. **Full-Sample Performance (2019-01-02 to 2024-12-30, 1,510 trading days):**
   - Initial Capital: $\$1,000,000.00$
   - Final NAV: $\$1,757,547.62$
   - Total Net P&L: $+\$757,547.62$
   - Total Net Return: $+75.75\%$
   - Compound Annual Growth Rate (CAGR): $9.87\%$ (vs. S&P 500 ETF $17.17\%$, WTI Buy & Hold $7.30\%$)
   - Annualized Volatility: $10.04\%$
   - Sharpe Ratio ($R_f = 5\%$): $0.4895 \approx 0.490$ (vs. S&P 500 ETF $0.647$, WTI Buy & Hold $-0.326$)
   - Sortino Ratio: $0.8979 \approx 0.898$
   - Calmar Ratio: $0.7758 \approx 0.776$ (vs. S&P 500 ETF $0.51$, WTI Buy & Hold $0.05$)
   - Maximum Drawdown: $-12.72\%$ (Peak: 2022-03-10, Trough: 2022-04-28, Drawdown duration: 49 days, Recovery: 146 days; vs. S&P 500 ETF $-33.72\%$, WTI Buy & Hold $-156.76\%$)
   - Value at Risk (Daily VaR 95% / 99%): $-0.6368\% / -1.7621\%$
   - Conditional Value at Risk (Daily CVaR 95%): $-1.2713\%$
   - Total Completed Trades: 28 (12 Long crack trades, 16 Short crack trades)
   - Win Rate (Hit Rate): $82.14\%$ (23 winning trades / 5 losing trades)
   - Profit Factor: $6.6945 \approx 6.69$
   - Average Win: $+\$38,876.17$
   - Average Loss: $-\$26,712.85$
   - Trade Expectancy: $+\$27,163.84$ per trade
   - Average Holding Period: $14.3$ trading days
   - Total Friction / Transaction Costs: $\$44,520.00$

2. **Rolling-Origin Walk-Forward Validation:**
   - Evaluated across 5 sequential walk-forward folds starting from an initial minimum 756-day training history. Parameters $(w \in [20, 60], \theta_{\text{entry}} \in [1.5, 2.5])$ were selected strictly on training folds and evaluated on held-out test data.
   - All 5 folds independently selected the same optimal parameter pair: $w = 30$ days, $\theta_{\text{entry}} = 2.0\sigma$.
   - Stitched Out-of-Sample (OOS) Return: $+36.4\%$
   - Stitched OOS Sharpe Ratio: $0.661$
   - Stitched OOS Maximum Drawdown: $-11.4\%$
   - Profitable Folds: $5 / 5$ ($100\%$)

3. **Component Ablation Analysis (`source-reported`):**
   - Baseline Raw Z-Score ($w=30, \theta=2.0$, no deseasonalization, stateless stop): Sharpe $0.188$, Max DD $-24.5\%$
   - $+$ Stop-Loss Re-Entry Suppression Lockout: Sharpe $0.386$, Max DD $-19.3\%$
   - $+$ Time Stop ($2 \times$ OU half-life $= 56$ days): Sharpe $0.386$, Max DD $-19.3\%$
   - $+$ Expanding Harmonic Deseasonalization ($K=1$): Sharpe $0.490$, Max DD $-12.7\%$

4. **Rejected Architectural Components (`source-reported` negative findings):**
   - Addition of Volatility Floor: Sharpe degraded to $0.358$, Max DD $-19.5\%$ (rejected)
   - Addition of Gross Leverage Cap: Sharpe degraded to $0.336$, Max DD $-19.0\%$ (rejected)
   - Addition of Asymmetric Short Entry Threshold: Sharpe degraded to $0.069$, Max DD $-21.8\%$ (rejected)
   - Addition of Rolling Half-Life Regime Gate: Sharpe collapsed to $-0.006$, Max DD $-24.4\%$ (rejected)

### Independently reproduced

`not independently reproduced`. All quantitative figures, backtest results, and diagnostic statistics cited in this record are third-party results reported by Reddy & Chakri (2026, GitHub commit `71ecf936b106dc2e58df2881524b59510450bcd9`). No independent reproduction inside our internal PyBroker or NautilusTrader simulation environments has been performed.

### Negative evidence

1. **Statistical Non-Stationarity and Unit-Root Persistence:**
   Full-sample econometric tests fail classical stationarity benchmarks (`source-reported`):
   - ADF test statistic $-2.28$ ($p = 0.178$) fails to reject the unit-root null hypothesis at the $5\%$ level.
   - KPSS level test statistic $2.04$ ($p < 0.01$) rejects stationarity outright.
   - Rescaled Range Hurst exponent $H \approx 0.97$ demonstrates intense long-memory persistence rather than pure mean reversion.
   These statistics establish that the 3:2:1 crack spread is subject to structural regime shifts, and any assumption of global, unvarying mean reversion is invalid.

2. **Stationary Bootstrap Statistical Insignificance:**
   A stationary bootstrap test (Politis & Romano, 1994) applied to the out-of-sample trading days yields a $95\%$ confidence interval for the out-of-sample Sharpe ratio of:
   $$[-0.160, 1.560]$$
   Because this interval spans zero, the hypothesis of zero excess return cannot be rejected at the $5\%$ significance level on 625 held-out trading days alone (`source-reported` caveat).

3. **Low Trade Count & Small-Sample Fragility:**
   The entire 6-year history generated only 28 completed trades (averaging $4.7$ trades per year). While the hit rate ($82.14\%$) and profit factor ($6.69$) appear strong, a strategy with fewer than 30 total degrees of freedom is vulnerable to small-sample estimation variance and regime clustering.

4. **Severe Component Failure on Ad-Hoc Filters:**
   Testing complex indicator additions (volatility floors, gross leverage limits, half-life regime filters) severely degraded or eliminated profitability, demonstrating that over-filtering causes structural under-trading.

## Falsification plan

The following operational tests would disconfirm or materially falsify the core alpha hypothesis:

1. **Seasonal Shuffling Placebo Test:**
   - Protocol: Randomly permute the day-of-year calendar indices $d_t$ in the harmonic expansion model across 1,000 Monte Carlo draws while keeping market settlement prices unaltered.
   - Failure Criterion: If the true calendar-aligned deseasonalized strategy does not achieve an information ratio or Sharpe ratio in the top $5\%$ of the placebo distribution, the claim that predictable annual refining cycles provide incremental alpha over raw mean reversion is falsified (`research-defined falsification threshold`: Empirical $p > 0.05$).

2. **Re-Entry Lockout Ablation Test:**
   - Protocol: Remove the `locked` latch from the state machine, allowing the strategy to immediately re-enter an active position on the exact same bar that triggers the $|z| > 4.0\sigma$ hard stop.
   - Failure Criterion: If the unlatched strategy achieves a maximum drawdown within $3.0\%$ percentage points of the latched system ($-12.72\%$), the claim that state-machine re-entry suppression is an essential structural defense is falsified (`research-defined falsification threshold`: $\Delta \text{MaxDD} < 3.0\%$).

3. **Out-of-Sample Horizon Extension (Post-2024 CME Data):**
   - Protocol: Run the frozen production parameter configuration ($w=30, \theta_{\text{entry}}=2.0, \theta_{\text{stop}}=4.0, \text{max\_hold}=56$) across 2025–2026 CME settlement data.
   - Failure Criterion: If the post-2024 realized net Sharpe ratio falls below $0.0$ or maximum drawdown exceeds $-18.0\%$, the local mean-reversion hypothesis is declared structurally broken (`research-defined falsification threshold`).

4. **Execution Friction & Roll-Yield Stress Test:**
   - Protocol: Escalate slippage from $\$0.05/\text{bbl}$ to $\$0.20/\text{bbl}$ and simulate negative roll decay of $-\$0.10/\text{bbl}$ per monthly expiration to reflect illiquid backwardation regimes.
   - Failure Criterion: If total net strategy P&L turns negative under these frictions, the strategy is deemed non-viable in live trading conditions (`research-defined falsification threshold`: Net P&L $< 0$).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven` (`research interpretation`).
- **Domain Boundaries & Disparities:**
  - *No Native Commodity Equivalent:* The 3:2:1 crack spread is grounded in the physical thermodynamics and chemical yield curves of petroleum refining ($3 \text{ crude} \to 2 \text{ gasoline} + 1 \text{ distillate}$). No physical crude or petroleum derivative trades natively on crypto venues.
  - *Candidate Crypto Synthetic Spreads (`research-proposed`):*
    1. *Proof-of-Work Mining Gross Margin:* The synthetic margin between Bitcoin market price and marginal production cost (estimated from network difficulty, global hashrate, hardware efficiency J/TH, and industrial electricity rate benchmarks). Similar to refinery margins, when mining margins turn negative, high-cost miners curtail operations, suppressing hash ribbons until margins recover.
    2. *Liquid Staking / Restaking Basis (stETH / wstETH / eETH vs. ETH):* Spreads between staked receipt tokens and spot ETH on decentralized AMMs (Curve, Uniswap) versus CEX perpetuals. When staking spreads dislocate beyond liquidity provisioning costs, arbitrage capital restores parity.
    3. *Quarterly-to-Perpetual Calendar Basis:* The term-structure basis spread between fixed-maturity quarterly futures and perpetual contracts.
  - *Portability Frictions & Structural Risks (`research interpretation`):*
    - *24/7 Session Structure:* Crypto operates continuously without daily CME settlement closes. Discrete 1-day lag execution must be adapted to continuous-time execution or fixed hourly observation bars.
    - *8-Hour Funding Rate Cash Drains:* Holding perpetual swap positions incurs perpetual funding rates every 8 hours. In extreme basis dislocations, persistent funding costs can exceed mean-reversion profits.
    - *Tail Kurtosis & Smart Contract Depegs:* In traditional commodities, physical storage and transport enforce hard upper/lower bounds. In crypto, synthetic spreads face smart contract hack risks, liquidation cascades, or stablecoin depegs where spreads dislocate beyond $10\sigma$ without reverting, destroying mean-reversion models.

## Limitations

- **Not Independently Reproduced:** All performance figures rely exclusively on third-party backtests published in `rudraakshreddy/petroquant-alpha`.
- **Small-Sample Trade Count:** Only 28 completed trades over 6 years. The $95\%$ bootstrap confidence interval for the Sharpe ratio spans $[-0.160, 1.560]$, failing to statistically rule out a zero-alpha null hypothesis.
- **Underspecified Microstructure & Liquidity Frictions:** Backtest assumes fills at daily settlement prices with constant $\$0.05/\text{bbl}$ slippage; does not model order book depth, market impact, or spread blowouts during volatility shocks.
- **Simplified Roll Accounting:** Uses a flat $\$0.02/\text{bbl}$ crossing fee rather than tracking exact calendar term-structure contango/backwardation curves.
- **Asset Class Boundary:** Commodity futures relative-value, requiring multi-asset margin management across three separate futures contracts.

## Implementation status

`not-implemented`.
No implementation of the PetroQuant Alpha system, 3:2:1 crack spread data ingestion, expanding harmonic deseasonalization, or re-entry lockout state machine exists in our internal research repository, `nautilus-quant-system`, PyBroker, or NautilusTrader codebases. This record serves strictly as normalized research capture.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This document represents an upstream research capture for ChatGPT Research Intake Review. It does not constitute approval for live trading, testnet deployment, paper trading, or production implementation.

## Related Wiki records

- `[[commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02]]` — Commodity futures multi-scale calendar spread learning.
- `[[convex-cross-impact-transient-execution-relative-value-2026-09-08]]` — Convex cross-impact and transient price decay in commodity roll spreads.
- `[[crypto-adaptive-trailing-stop-volatility-filtered-cointegrated-pairs-trading-2026-09-07]]` — Volatility-filtered cointegrated pairs trading with adaptive stop mechanisms.
- `[[statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]` — Deep learning factor replication and Ornstein-Uhlenbeck mean-reversion dynamics.
- `[[crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]` — Cointegration and statistical arbitrage falsification under transaction cost dissipation.

## Sources

1. **Primary Source Repository & Technical Report:**
   - Yeddula Rudraaksh Reddy and S. N. Chakri, *"A Seasonally Adjusted Mean-Reversion System for the 3:2:1 Crude Oil Crack Spread"*, Technical Report, September 2026.
   - Public GitHub Repository: [https://github.com/rudraakshreddy/petroquant-alpha](https://github.com/rudraakshreddy/petroquant-alpha)
   - Immutable Commit: `71ecf936b106dc2e58df2881524b59510450bcd9`
   - Exact Audited Files:
     - `README.md`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/README.md`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/README.md)
     - `config.py`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/config.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/config.py)
     - `src/spread_construction.py`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/spread_construction.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/spread_construction.py)
     - `src/statistical_tests.py`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/statistical_tests.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/statistical_tests.py)
     - `src/signal_generation.py`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/signal_generation.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/signal_generation.py)
     - `src/backtester.py`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/backtester.py`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/src/backtester.py)
     - `results/tables/performance_metrics.json`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/results/tables/performance_metrics.json`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/results/tables/performance_metrics.json)
     - `results/tables/parameter_sweep_results.csv`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/results/tables/parameter_sweep_results.csv`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/results/tables/parameter_sweep_results.csv)
     - `report/petroquant_report.pdf`: [`https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/report/petroquant_report.pdf`](https://github.com/rudraakshreddy/petroquant-alpha/blob/71ecf936b106dc2e58df2881524b59510450bcd9/report/petroquant_report.pdf)
   - Interactive Dashboard: [https://petroquant-alpha.streamlit.app](https://petroquant-alpha.streamlit.app)
