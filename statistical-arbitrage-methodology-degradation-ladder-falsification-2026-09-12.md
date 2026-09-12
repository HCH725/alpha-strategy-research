---
schema: strategy-research-record-v1
title: "Statistical Arbitrage Methodology Degradation Ladder and Econometric Precondition Falsification"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - cointegration
  - look-ahead-bias
  - degradation-ladder
  - econometric-falsification
  - hedge-ratio-gate
  - multiple-testing
  - survivorship-bias
status: research-only
confidence: high
source_as_of: 2026-09-02
sources:
  - "Grant J. Kim, Statistical Arbitrage Backtester, GitHub repository grant-j-kim/statistical-arbitrage-backtester, commit a6135a14c86d0e9ca93d293802416310023f9980, September 2, 2026. Stable URL: https://github.com/grant-j-kim/statistical-arbitrage-backtester"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Statistical Arbitrage Methodology Degradation Ladder and Econometric Precondition Falsification

## Provenance

- **Primary Source:** Grant J. Kim (`grant-j-kim`), *"Statistical Arbitrage Backtester: Pairs trading backtester: cointegration-based pair discovery and an honest naive-vs-rigorous comparison showing what costs and look-ahead-bias fixes actually cost you"*, published and audited September 2, 2026 (`source-reported`).
  - GitHub Repository URL: [https://github.com/grant-j-kim/statistical-arbitrage-backtester](https://github.com/grant-j-kim/statistical-arbitrage-backtester)
  - Canonical Commit SHA: `a6135a14c86d0e9ca93d293802416310023f9980`
  - Core Modules:
    - Backtest Engine & Configuration: [`statarb/backtest.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/statarb/backtest.py)
    - Spread & Rolling Signals: [`statarb/spread.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/statarb/spread.py)
    - Cointegration & Half-Life Screening: [`statarb/cointegration.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/statarb/cointegration.py)
    - Stationarity Prechecks & Leg Concentration: [`statarb/stationarity.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/statarb/stationarity.py)
    - Institutional Friction & Borrow Model: [`statarb/costs.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/statarb/costs.py)
    - Universe & Date Partitions: [`statarb/universe.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/statarb/universe.py)
    - Test Suite (21 unit and property tests): [`tests/test_backtest.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/tests/test_backtest.py), [`tests/test_cointegration.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/tests/test_cointegration.py), [`tests/test_stationarity.py`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/tests/test_stationarity.py)
    - Verified Numerical Tables: [`results/clean/degradation_ladder.csv`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/results/clean/degradation_ladder.csv), [`results/clean/pairs_rigorous.csv`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/results/clean/pairs_rigorous.csv), [`results/clean/per_pair_rigorous.csv`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/results/clean/per_pair_rigorous.csv), [`results/clean/random_control_1000.csv`](https://github.com/grant-j-kim/statistical-arbitrage-backtester/blob/a6135a14c86d0e9ca93d293802416310023f9980/results/clean/random_control_1000.csv)
- **Primary Source Integrity Audit:** All metrics, ladder step deltas, p-values, t-statistics, and operational parameters were extracted directly from the raw codebase, commit message, and clean CSV audit artifacts at commit `a6135a14c86d0e9ca93d293802416310023f9980`. No search snippets, secondary blogs, or AI-generated summaries were used to extract strategy mechanics or empirical findings.
- **Repository Deduplication Audit:** A full search across `alpha-strategy-research` confirmed zero pre-existing captures of `grant-j-kim/statistical-arbitrage-backtester` or commit `a6135a14c86d0e9ca93d293802416310023f9980`. Adjacent records in the repository examine related statistical arbitrage concepts under distinct angles:
  - `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12.md` evaluates walk-forward ADF filtering across 92 ETF pairs, demonstrating formation-window variance compression bias;
  - `johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md` investigates multi-asset Johansen cointegration with execution friction asymmetry;
  - `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` explores one-sided Kalman filtering on crypto perpetuals.
  The current research artifact provides a distinct, foundational econometric decomposition: it isolates the 8-rung degradation ladder of backtest biases (separating full-sample signal look-ahead from execution timing lag), quantifies the failure modes of the $I(1)$ unit root precondition in Engle-Granger screening, and proves that cointegration testing acts primarily as a proxy for Ornstein-Uhlenbeck mean-reversion speed.

## Economic mechanism

### Source-reported

1. **The Methodological Degradation Thesis:** Statistical arbitrage literature frequently reports Sharpe ratios above 1.5 to 2.5 for cointegration-based pairs trading. However, much of this apparent edge is not structural market inefficiency, but an artifact of methodological design choices: full-sample z-score normalization (which informs the strategy of the spread's unconditional mean in advance), full-sample OLS hedge ratios, zero-cost assumptions, omitting borrow fees on short legs, and execution at the signal's closing price (`source-reported`).
2. **Decomposition of Look-Ahead Bias:** Common practitioner warnings heavily emphasize execution timing (same-bar close fill versus next-bar open fill). When measured within a unified single-engine event loop, same-bar execution bias accounts for a negligible reduction of 0.006 Sharpe. In contrast, full-sample z-score statistics account for a massive 0.412 Sharpe reduction, and full-sample hedge ratios cost an additional 0.323 Sharpe (`source-reported`).
3. **The Hedge-Ratio Instability & Sign-Flip Failure Mode:** Rolling hedge ratios ($\beta_t$) are subject to estimation error. When $|\beta_t| \to 0$, the short leg fails to hedge market risk, turning the position into an outright directional bet. When $|\beta_t| \to \infty$, the hedge leg overwhelms the signal leg. Crucially, $\beta_t$ can flip sign relative to the formation relationship ($\text{sign}(\beta_t) \ne \text{sign}(\beta_{\text{ref}})$), converting a long/short hedge into a long/long double-directional exposure that frequently stops out immediately. Introducing a hedge-ratio sanity gate recovers +0.169 Sharpe (`source-reported`).
4. **Econometric Precondition Violation ($I(1)$ Contamination):** Engle-Granger cointegration assumes both series are integrated of order 1 ($I(1)$). If one ticker is near-stationary ($I(0)$), regressing it on any partner produces an artificially stationary residual. In orientation-specific regressions, the near-stationary ticker on the dependent side generates false cointegration across the entire universe with collapsed slopes ($|\beta| \to 0$), contaminating 49% of significant pairs (`source-reported`).
5. **Power Collapse & Mean-Reversion Speed Confounding:** For 561 pairs over 1258 days, Engle-Granger screening power collapses from 99% at half-life 21 days to 28% at multiple-testing thresholds ($8.4 \times 10^{-5}$) and 1% at 42 days. Furthermore, the test statistic $\min p$ has a Spearman rank correlation of +0.910 with Ornstein-Uhlenbeck half-life ($R^2 = 0.754, t = 39.1$), meaning the cointegration filter does not identify structural equilibrium bonds, but merely acts as a high-speed mean-reversion filter (`source-reported`).

### Research interpretation

The statistical arbitrage "edge" in textbook equity pairs trading is dominated by look-ahead bias in the spread standardization process ($\mu$ and $\sigma$ calculation) rather than alpha in cointegration discovery. Knowing future spread drift enables the model to wait for extreme statistical excursions that are only identifiable in hindsight. When subjected to strictly causal rolling estimation, the strategy's Sharpe collapses from 1.23 to 0.49. Active risk engineering—specifically a hedge-ratio sanity gate (+0.17 Sharpe) and volatility-scaled sizing (+0.16 Sharpe)—partially restores profitability to Sharpe 0.73 ($t = 1.86$). However, because the screening mechanism is statistically underpowered and confounded with half-life speed, the final system cannot be confirmed as statistically distinct from zero ($t < 1.96$) once survivorship bias and multiple testing are accounted for.

## Signal

### Universe & Partitioning
- **Universe (`source-reported`):** 34 large-cap US equities selected strictly by sector membership (not price correlation):
  - 14 Financials: `JPM`, `BAC`, `WFC`, `C`, `GS`, `MS`, `USB`, `PNC`, `TFC`, `SCHW`, `BNY`, `STT`, `AXP`, `COF`.
  - 13 Consumer Staples: `KO`, `PEP`, `PG`, `CL`, `KMB`, `GIS`, `HSY`, `MDLZ`, `MO`, `PM`, `COST`, `WMT`, `KR`.
  - 7 Sanity Check / Structural: `GOOG`, `GOOGL`, `GLD`, `GDX`, `CVX`, `HD`, `LOW`.
  - Excluded Contaminated: `XOM` (dropped due to $I(1)$ precondition failure, ADF $p = 0.0054$).
- **Disjoint Partitioning (`source-reported`):**
  - Formation Window: `2015-01-01` to `2019-12-31` (1,258 trading days).
  - Out-of-Sample Trading Window: `2020-01-01` to `2026-08-01` (1,656 trading days).

### Formation Selection & Econometric Screening
1. **$I(1)$ Integration Precheck (`source-reported`):**
   - Run Augmented Dickey-Fuller (ADF) test with AIC lag selection and KPSS test with level stationarity (`regression="c"`, auto bandwidth) on log price levels for each asset.
   - Require both assets to satisfy the $I(1)$ precondition (reject ADF unit root $p > 0.05$ and fail to reject KPSS stationarity $p > 0.05$). Flag and drop $I(0)$ series.
2. **Engle-Granger Cointegration Testing (`source-reported`):**
   - For all 561 pairwise combinations, run Engle-Granger cointegration in both orientations:
     $$\text{Model 1: } \log(y_t) = \alpha_1 + \beta_1 \log(x_t) + \varepsilon_{1, t}$$
     $$\text{Model 2: } \log(x_t) = \alpha_2 + \beta_2 \log(y_t) + \varepsilon_{2, t}$$
   - Calculate Ornstein-Uhlenbeck mean-reversion half-life on residuals:
     $$\Delta \hat\varepsilon_t = \lambda \hat\varepsilon_{t-1} + c + u_t, \quad t_{1/2} = -\frac{\ln(2)}{\lambda} \quad (\text{valid for } \lambda < 0)$$
   - Retain the orientation yielding the minimum p-value: $\min\_p = \min(p_1, p_2)$.
   - Multiple testing adjustment: $p_{\text{adj}} = \min(2 \cdot \min\_p, 1.0)$ (`source-reported`).
3. **Pair Selection Funnel (`source-reported`):**
   - Filter to pairs with half-life $t_{1/2} \in [5, 60]$ trading days.
   - Cap ticker concentration at a maximum of 2 appearances per ticker across the portfolio.
   - Select top 10 pairs ranked by ascending $\min\_p$.

### Real-Time Signal Construction
1. **Spread Definition (`source-reported`):**
   $$\text{spread}_t = \log(y_t) - \beta_t \log(x_t)$$
   No constant intercept is subtracted because the intercept is not a tradeable cash flow; the rolling mean in the z-score absorbs the level.
2. **Rolling Estimation (`source-reported`):**
   - Trailing hedge ratio $\beta_t$: Computed via `RollingOLS` over a trailing window $W_\beta = 252$ trading days ending at day $t$ close.
   - Trailing z-score $z_t$: Computed over a trailing window $W_z = 60$ trading days ending at day $t$ close:
     $$z_t = \frac{\text{spread}_t - \mu_{\text{spread}, t}(60)}{\sigma_{\text{spread}, t}(60)}$$
     where $\sigma_{\text{spread}, t} > 10^{-8}$ is enforced to prevent numerical explosion during low-volatility regimes.
   - Trailing spread volatility: $\sigma_{\Delta \text{spread}, t} = \text{std}(\text{spread}_t - \text{spread}_{t-1}, W_z = 60)$.

### Execution Logic & State Machine
The system operates an explicit day-by-day event loop with execution at day $t+1$ open (`next_bar_open`) (`source-reported`):
- **Hedge-Ratio Sanity Gate (`source-reported`):**
  A new trade entry is permitted if and only if:
  1. $\beta_t$ is finite;
  2. $0.1 \le |\beta_t| \le 10.0$;
  3. $\text{sign}(\beta_t) == \text{sign}(\beta_{\text{ref}})$, where $\beta_{\text{ref}}$ is the pair's formation OLS slope.
  If the sanity gate is violated, new entries are blocked; existing open positions continue to be managed by exit rules.
- **Entry Triggers (`source-reported`):**
  - **Long Spread ($s_t = +1$):** Triggered when $z_t \le -2.0$ (`entry_z = 2.0`). Opens long position in $y$ and short position in $x$.
  - **Short Spread ($s_t = -1$):** Triggered when $z_t \ge 2.0$ (`entry_z = 2.0`). Opens short position in $y$ and long position in $x$.
- **Exit Triggers (`source-reported`):**
  - **Mean-Reversion Profit Exit:** Triggered when $|z_t| \le 0.5$ (`exit_z = 0.5`).
  - **Divergence Stop-Loss:** Forced unwind when $|z_t| \ge 4.0$ (`stop_z = 4.0`).
  - **Max Holding Period Time Stop:** Forced unwind after 126 trading days (`max_holding_days = 126`).
- **Execution Fill Timing (`source-reported`):**
  Signal generated at day $t$ market close; orders queue and fill at day $t+1$ market open. Share quantities are determined using entry prices and frozen $\beta_{\text{entry}}$. Realized P&L is tracked from daily price changes of physical share counts, never synthetic spread differencing.

### Position Sizing & Capital Allocation
- **Capital Allocation (`source-reported`):** Total portfolio equity $\$1,000,000$, partitioned equally into 10 independent pair slices ($\$100,000$ slice capital per pair).
- **Volatility & Conviction Sizing (`source-reported`):**
  $$\text{conviction} = \min\left(\frac{|z_t|}{\text{entry\_z}}, \text{max\_conviction} = 2.0\right)$$
  $$\text{vol\_scalar} = \text{clip}\left(\frac{\text{target\_spread\_vol} = 0.02}{\sigma_{\Delta \text{spread}, t}}, 0.25, 2.0\right)$$
  $$\text{Target Notional } S_y = \text{capital\_slice} \times \text{conviction} \times \text{vol\_scalar}$$
- **Gross Leverage Cap (`source-reported`):**
  Gross position is $S_y$ in asset $y$ plus $S_y |\beta_{\text{entry}}|$ in asset $x$, yielding gross notional $S_y (1 + |\beta_{\text{entry}}|)$. To enforce the maximum gross leverage constraint ($\text{max\_gross\_leverage} = 2.0$), the long-leg notional is strictly capped:
  $$S_{y, \text{exec}} = \min\left(S_y, \frac{\text{capital\_slice} \times 2.0}{1 + |\beta_{\text{entry}}|}\right)$$
  Physical shares allocated: $N_y = s \cdot \frac{S_{y, \text{exec}}}{P_{y, t+1}^{\text{open}}}$, $N_x = -s \cdot \frac{\beta_{\text{entry}} S_{y, \text{exec}}}{P_{x, t+1}^{\text{open}}}$.

## Required data

- **Instruments & Asset Class (`source-reported`):** US Large-Cap Equities listed on NYSE/NASDAQ from Financials and Consumer Staples sectors.
- **Data Granularity (`source-reported`):** Daily OHLCV bars. Open price required for execution fills ($t+1$); Close price required for signal formation ($t$).
- **Sample Window (`source-reported`):** `2015-01-01` to `2026-08-01` (2015–2019 formation; 2020–2026 out-of-sample trading).
- **Corporate Actions & Dividends (`source-reported`):** Split-adjusted and dividend-adjusted closing prices for signal estimation. Unadjusted open/close prices used for trade share sizing and cash settlement tracking.
- **Stock Loan / Borrow Rate (`source-reported`):** Continuous short-leg borrow rate model (calibrated at 50 bps/year).
- **Survivorship Gap (`source-reported`):** Primary research highlights that yfinance omits delisted names (e.g., `SIVB`, `SBNY`, `FRC`, `K`, `KLG`), creating structural survivorship bias. Point-in-time constituent databases (e.g., CRSP/Compustat) are documented as necessary to fully eliminate this bias.

## Execution assumptions

- **Signal-to-Order Timing (`source-reported`):** Signals generated at day $t$ close ($16:00$ EST). Limit/market orders executed at day $t+1$ open ($09:30$ EST).
- **Execution Frictions (`source-reported`):**
  - Broker Commission: 1.0 bp per leg per direction ($0.0001 \times \text{notional}$).
  - Bid-Ask Half-Spread: 2.0 bps per leg per direction ($0.0002 \times \text{notional}$).
  - Market Impact / Slippage: 1.0 bp per leg per direction ($0.0001 \times \text{notional}$).
  - Total One-Way Cost per Leg: 4.0 bps ($0.0004 \times \text{notional}$).
  - Total Round-Trip Cost (4 leg executions: buy $y$, sell $x$, sell $y$, buy $x$): 16.0 bps of traded notional.
- **Borrow Financing Cost (`source-reported`):**
  $$\text{Borrow Cost} = |\text{Notional}_x| \times 0.0050 \times \left(\frac{\text{Holding Days}}{252}\right)$$
  accrued continuously over the holding period.
- **Fill Reliability (`source-reported`):** 100% fill assumed at open price for liquid US large-caps.

## Evidence

### Source-reported

All performance figures, trade counts, drawdowns, and degradation step deltas trace directly to the clean primary data outputs (`results/clean/degradation_ladder.csv`, `results/clean/pairs_rigorous.csv`, `results/clean/per_pair_rigorous.csv`, and `results/clean/random_control_1000.csv`) generated across 1,656 trading days (2020-01-01 to 2026-08-01) on the corrected 34-ticker universe:

#### 1. The 8-Rung Methodological Degradation Ladder

| Rung # | Configuration Description | Sharpe | Sharpe SE | t-stat | Ann. Return | Ann. Vol | Max DD | Calmar | Win Rate | Trades | Avg Hold (d) | Turnover | Total Costs | Cost Drag | Gate Blocks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | Naive (correlation-selected, no rigor) | 0.781 | 0.391 | 2.00 | 6.48% | 8.30% | 10.69% | 0.607 | 81.25% | 32 | 97.0 | 1.60 | $0.00 | 0.0 bp | 0 |
| **2** | + Cointegration selection (peak naive) | **1.229** | 0.391 | 3.14 | 6.56% | 5.34% | 5.39% | 1.216 | 82.86% | 35 | 89.3 | 1.79 | $0.00 | 0.0 bp | 0 |
| **3** | + Trailing z-score statistics | 0.817 | 0.391 | 2.09 | 5.49% | 6.71% | 6.34% | 0.865 | 72.09% | 326 | 22.8 | 17.04 | $0.00 | 0.0 bp | 0 |
| **4** | + Rolling hedge ratio (OLS $\beta$) | 0.494 | 0.391 | 1.26 | 3.89% | 7.87% | 11.44% | 0.340 | 56.11% | 180 | 63.9 | 9.23 | $0.00 | 0.0 bp | 0 |
| **5** | + Hedge-ratio sanity gate | 0.663 | 0.391 | 1.70 | 4.92% | 7.42% | 7.07% | 0.697 | 58.08% | 167 | 63.5 | 8.74 | $0.00 | 0.0 bp | 312 |
| **6** | + $t+1$ execution timing lag | 0.657 | 0.391 | 1.68 | 4.90% | 7.46% | 7.08% | 0.693 | 56.29% | 167 | 63.5 | 8.74 | $0.00 | 0.0 bp | 310 |
| **7** | + Transaction costs & borrow fee | 0.573 | 0.391 | 1.47 | 4.28% | 7.47% | 7.74% | 0.552 | 56.29% | 167 | 63.5 | 8.74 | $41,004 | 410 bp | 310 |
| **8** | + Vol-scaled sizing (**full rigorous**) | **0.728** | 0.391 | 1.86 | 4.62% | 6.35% | 6.67% | 0.693 | 56.29% | 167 | 63.5 | 7.94 | $36,458 | 365 bp | 310 |

#### 2. Key Quantitative Findings & Bias Attribution
- **Peak-to-Rigorous Decay:** Sharpe falls from 1.229 to 0.728 ($\Delta = -0.501$ Sharpe, or a 40.8% loss of peak performance); the t-statistic declines from 3.14 to 1.86, dropping below the conventional 1.96 two-tailed significance boundary (`source-reported`).
- **Look-Ahead Bias Breakdown:**
  - Full-sample z-score normalization accounts for $-0.412$ Sharpe (loss of 33.5% of peak), while ballooning trade count from 35 to 326 as trailing estimates adapt to real-time mean drift (`source-reported`).
  - Full-sample OLS beta accounts for $-0.323$ Sharpe (`source-reported`).
  - Same-bar execution ($t$ close vs $t+1$ open) costs only $-0.006$ Sharpe (a negligible 0.5% of peak), disproving the assumption that fill timing is the dominant bias in daily statistical arbitrage (`source-reported`).
- **Remediation Alpha Boosts:**
  - The hedge-ratio sanity gate adds $+0.169$ Sharpe by suppressing 310 unstable or inverted trades (`source-reported`).
  - Volatility-scaled conviction sizing adds $+0.155$ Sharpe while reducing max drawdown from 7.74% to 6.67% (`source-reported`).
- **Cost Drag:** Institutional frictions (16 bps round-trip + 50 bps/yr borrow) consume $\$36,458$ (365 bps of capital over the test span), reducing Sharpe by $-0.084$ (`source-reported`).
- **Confounded Random Control:**
  - Across 1,000 random 10-pair draws, the null mean Sharpe is $0.151 \pm 0.315$. The cointegration-selected portfolio (Sharpe 0.728) lands in the 96.5th percentile ($p = (35+1)/(1000+1) = 0.036$) (`source-reported`).
  - However, Spearman rank correlation between $\min\_p$ and Ornstein-Uhlenbeck half-life is $\rho = +0.910$ ($R^2 = 0.754, t = 39.1$). When evaluated against pairs passing the same half-life filter ($N=170$), the empirical p-value rises to $p = 0.062$, failing the 5% threshold (`source-reported`).
- **Per-Pair Net P&L Distribution (Rigorous Portfolio):**
  - `BNY/SCHW`: Net P&L $\$61,191$, Sharpe 0.445, 14 trades, 78.6% win rate, 20.2% P&L share (`source-reported`).
  - `COF/PNC`: Net P&L $\$60,995$, Sharpe 0.469, 19 trades, 47.4% win rate, 20.1% P&L share (`source-reported`).
  - `CL/GDX`: Net P&L $\$52,427$, Sharpe 0.404, 13 trades, 61.5% win rate, 17.3% P&L share, 108 gate blocks (`source-reported`).
  - `COF/C`: Net P&L $\$49,587$, Sharpe 0.362, 17 trades, 58.8% win rate, 16.4% P&L share (`source-reported`).
  - `WFC/GS`: Net P&L $\$44,132$, Sharpe 0.391, 17 trades, 64.7% win rate, 14.6% P&L share (`source-reported`).
  - `CL/GLD`: Net P&L $\$24,936$, Sharpe 0.312, 14 trades, 57.1% win rate, 8.2% P&L share, 80 gate blocks (`source-reported`).
  - `HSY/PG`: Net P&L $\$21,365$, Sharpe 0.237, 13 trades, 53.8% win rate, 7.0% P&L share, 71 gate blocks (`source-reported`).
  - `LOW/COST`: Net P&L $\$10,394$, Sharpe 0.076, 20 trades, 60.0% win rate, 3.4% P&L share, 51 gate blocks (`source-reported`).
  - `TFC/BAC`: Net P&L $-\$6,163$, Sharpe -0.052, 22 trades, 45.5% win rate, -2.0% P&L share (`source-reported`).
  - `PNC/BAC`: Net P&L $-\$15,732$, Sharpe -0.163, 18 trades, 44.4% win rate, -5.2% P&L share (`source-reported`).

### Independently reproduced

`not independently reproduced`. All metrics, equity series, and diagnostic tables represent primary research outputs reported by Grant J. Kim in GitHub repository `grant-j-kim/statistical-arbitrage-backtester` (commit `a6135a14c86d0e9ca93d293802416310023f9980`). No internal simulation has been run in our stack.

### Negative evidence

- **Zero FDR Survivors Across Universe:** In the formation scan of 561 pairs, 35 pairs showed raw $\min\_p < 0.05$. Under a simulated correlated non-cointegrated null, 44.5 pairs are expected by pure noise (an actual deficit of $0.79\times$). After adjusting for dual-orientation min-p selection ($p_{\text{adj}} = \min(2 \cdot \min\_p, 1)$), exactly **zero pairs survive Benjamini-Hochberg FDR** ($q_{\min} = 0.841$) and zero survive Benjamini-Yekutieli ($q_{\min} = 1.000$) (`source-reported`).
- **Failure of Google Dual-Class Share Trade:** `GOOG/GOOGL` ranks 37th in the scan ($p = 0.051, \beta = 0.967$). The voting premium decayed monotonically from 2.86% in 2015 to 0.25% in 2019 (ADF on raw ratio $p = 0.67$), causing a persistent trend rather than mean reversion (`source-reported`).
- **Absurd Pairs Dominating Gate Blocks:** Cross-sector pairs `CL/GDX` and `CL/GLD` (return correlation 0.08 and -0.005) trigger 188 of the 310 hedge-ratio gate blocks (61% of all blocks from 20% of pairs), proving that unconstrained cointegration screens select economically uncoupled pairs with violently unstable hedge ratios (`source-reported`).
- **Structural Survivorship Bias:** 11 of 16 potential financial/staples candidates from 2015 are omitted from 2026 data vendors, including three major bank failures (`SIVB`, `SBNY`, `FRC`) that failed inside the trading window, biasing all reported returns upward (`source-reported`).

## Falsification plan

### Research-defined falsification threshold
The strategy hypothesis shall be considered falsified if:
1. **Out-of-Sample Sharpe Degradation:** Walk-forward out-of-sample Sharpe drops below $0.40$ (annualized) across any rolling 24-month period (`research-defined falsification threshold`).
2. **Precondition Rejection:** The percentage of pairs violating the $I(1)$ unit root precondition (via joint ADF/KPSS testing) exceeds 15% of the screening universe (`research-defined falsification threshold`).
3. **Half-Life Decoupling:** Out-of-sample realized Ornstein-Uhlenbeck half-life expands beyond $2.5\times$ its formation-window estimate for $>50\%$ of selected pairs (`research-defined falsification threshold`).
4. **Hedge-Ratio Gate Block Saturation:** Gate blocks exceed 40% of total entry opportunities in a live or walk-forward test, indicating persistent parameter breakdown (`research-defined falsification threshold`).
5. **Cost-Adjusted Net Alpha Dissipation:** When round-trip trading frictions exceed 25 bps (e.g., in lower-liquidity names or crypto perpetuals), net strategy return turns negative (`research-defined falsification threshold`).

### Operational Stress Tests
- **Look-Ahead Truncation Property Test:** Run backtest on price history truncated at date $T$ versus full history; verify bit-identical trade execution decisions before $T$ (`source-reported`).
- **Placebo / Shuffled Residual Test:** Randomly permute the daily residual returns while preserving leg variance; confirm that strategy returns collapse to zero (`research-proposed`).
- **Point-in-Time Universe Audit:** Re-run the selection pipeline using point-in-time constituent lists including delisted and bankrupt firms to quantify survivorship bias drag (`research-proposed`).

## Crypto portability

- **Portability Classification:** `adapted / unproven` (`research-proposed`). The mechanism was demonstrated exclusively on US large-cap cash equities; empirical validity on crypto markets is not established in the primary source.
- **Key Crypto-Specific Market Structure Differences:**
  1. **Perpetual Basis & Funding Drag:** In crypto perpetual pairs (e.g., `BTC/USDT` vs `ETH/USDT` or altcoin pairs), holding positions for 63.5 days subjects the trade to 8-hour funding payments. Asymmetric funding rates between pair legs can completely erode spread mean-reversion profits (`research-proposed`).
  2. **Shorting Mechanics:** In equities, shorting incurs a flat borrow fee (50 bps/yr). In crypto perpetuals, shorting is native, but requires margin management to avoid liquidation cascades during extreme spread excursions (`research-proposed`).
  3. **24/7 Continuous Trading & Session Boundaries:** The equity backtester assumes daily close signal calculation and open fill. Crypto operates 24/7 without session open/close; signals must be adapted to fixed hourly or 4-hour UTC candle boundaries (`research-proposed`).
  4. **Stationarity of Crypto Ratios:** Most crypto assets exhibit non-stationary drift against BTC/ETH driven by token unlock schedules, inflation, and speculative cycles. Pure cointegration relationships in crypto are transient and rarely survive past 30–60 days (`research-proposed`).
  5. **Execution Frictions & Fragmentation:** Binance VIP0 taker fees (5.0 bps) + slippage (2.0 bps) imply 14.0 bps round trip per leg (28 bps across two legs), almost double the equity friction (16 bps). Given the empirical sensitivity to costs, higher crypto fees will impose severe alpha decay (`research-proposed`).

## Limitations

- **Underspecified Delisting Universe:** Uses surviving 2026 large-cap constituents; excludes failed 2023 regional banks (`SIVB`, `SBNY`, `FRC`), introducing unquantified positive survivorship bias (`source-reported`).
- **Statistical Insignificance:** The final rigorous Sharpe of 0.728 carries a standard error of $\approx 0.39$ ($t = 1.86$), which falls short of the $1.96$ threshold ($p > 0.05$) (`source-reported`).
- **Underpowered Formation Screen:** At $N=1258$ days, Engle-Granger testing power collapses for half-lives above 21 days, meaning zero FDR survivors reflects test underpowering rather than proven absence of cointegration (`source-reported`).
- **Confounded Control Baseline:** Random control comparison is invalid as a screen test because ranking on $\min\_p$ correlates +0.910 with half-life speed (`source-reported`).
- **Single Realization Window:** The out-of-sample trading window covers only one continuous period (2020–2026), opening directly into the COVID market shock (`source-reported`).
- **Absence of Independent Reproduction:** Results have not yet been replicated inside our internal NautilusTrader or PyBroker execution stacks (`not independently reproduced`).

## Implementation status

`not-implemented`. This document represents an external research capture and econometric audit. No component of this strategy, backtester, or degradation ladder has been implemented in `nautilus-quant-system`, PyBroker, NautilusTrader, Paper, Testnet, or Live trading.

## Adoption boundary

`research-only`.
- Status: `research-only`
- Implementation Status: `not-implemented`
- Adoption: `not-approved`
- Approval Scope: `research-only`

This record is strictly research analysis and methodological reference. It does not authorize strategy adoption, automated execution, or allocation in paper, testnet, or live environments.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `[[pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12]]`
- `[[johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12]]`
- `[[crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]`
- `[[sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]`

## Sources

1. **Primary Research Repository:** Grant J. Kim (`grant-j-kim`). *"Statistical Arbitrage Backtester: Pairs trading backtester: cointegration-based pair discovery and an honest naive-vs-rigorous comparison showing what costs and look-ahead-bias fixes actually cost you"*, GitHub repository `grant-j-kim/statistical-arbitrage-backtester`, commit `a6135a14c86d0e9ca93d293802416310023f9980`, pushed September 2, 2026. URL: [https://github.com/grant-j-kim/statistical-arbitrage-backtester](https://github.com/grant-j-kim/statistical-arbitrage-backtester).
2. **Backtest Implementation:** `statarb/backtest.py` at commit `a6135a14c86d0e9ca93d293802416310023f9980`. Documenting `BacktestConfig`, event loop, next-bar open fill execution, beta sanity gate, and volatility-scaled sizing.
3. **Signal & Estimation Logic:** `statarb/spread.py` at commit `a6135a14c86d0e9ca93d293802416310023f9980`. Specifying trailing `RollingOLS` beta (252 days) and rolling z-score (60 days) without constant subtraction.
4. **Econometric Screen & Half-Life:** `statarb/cointegration.py` at commit `a6135a14c86d0e9ca93d293802416310023f9980`. Documenting Engle-Granger two-orientation testing, Ornstein-Uhlenbeck half-life fitting, and FDR correction.
5. **Unit Root Prechecks:** `statarb/stationarity.py` at commit `a6135a14c86d0e9ca93d293802416310023f9980`. Documenting joint ADF/KPSS testing and leg-concentration diagnostics.
6. **Execution Friction Model:** `statarb/costs.py` at commit `a6135a14c86d0e9ca93d293802416310023f9980`. Calibrating 1 bp commission, 2 bps half-spread, 1 bp slippage (16 bps round-trip across 4 executions), and 50 bps annual stock loan borrow.
7. **Empirical Numerical Tables:** Committed audit CSVs at commit `a6135a14c86d0e9ca93d293802416310023f9980`: `results/clean/degradation_ladder.csv`, `results/clean/pairs_rigorous.csv`, `results/clean/per_pair_rigorous.csv`, `results/clean/random_control_1000.csv`.
