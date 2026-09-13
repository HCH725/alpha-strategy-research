---
schema: strategy-research-record-v1
title: "S&P 500 Avellaneda-Lee Stat-Arb Residual Reversion: Implementable P&L Accounting Falsification, Trailing Alpha Drift Drag, and Pre-Registered Salvage Failure"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - mean-reversion
  - avellaneda-lee
  - s-score
  - equities
  - sp500
  - falsification
  - negative-results
  - accounting-artifacts
  - live-paper-audit
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - "Kristen Ho, 'From Sharpe 3.8 to Retirement: Auditing an Untradeable Stat-Arb Backtest' and 'alpha-lab', GitHub repository, commit 6a5589b07cf8dace7d18b1681561b2b166df5cd4, published 2026-09-12, accessed 2026-09-13. https://github.com/kristenharim/alpha-lab"
  - "Primary post-mortem case study: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/CASE_STUDY.md"
  - "Audit state and research log: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/audit-bundle/01-STATE-statarb.md"
  - "Paper book forward-test design spec: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/audit-bundle/02-design-spec.md"
  - "Recomputation formulas and benchmark table: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/audit-bundle/04-RECOMPUTE.md"
  - "Track state dossier: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/tracks/statarb/STATE.md"
  - "Residual signal & implementable hedged return engine: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/tracks/statarb/residual.py"
  - "Audited net P&L module: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/tracks/statarb/pnl.py"
  - "Diagnostic decomposition memo: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/memos/diagnostics-2026-07-10.md"
  - "Foundational paper: Marco Avellaneda and Jeong-Hyun Lee, 'Statistical arbitrage in the US equities market', Quantitative Finance, 10(7):761–782, 2010. DOI: 10.1080/14697680903124632"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# S&P 500 Avellaneda-Lee Stat-Arb Residual Reversion: Implementable P&L Accounting Falsification, Trailing Alpha Drift Drag, and Pre-Registered Salvage Failure

## Provenance

- **Repository:** https://github.com/kristenharim/alpha-lab
- **Author:** Kristen Ho (`kristenharim`, git author `Kristen Ho <kristenho@MacBook-Pro-744.local>`) (`source-reported`).
- **Canonical Immutable Commit SHA:** `6a5589b07cf8dace7d18b1681561b2b166df5cd4` (`source-reported`).
- **Commit Date:** 2026-09-12T23:55:21Z (`source-reported`).
- **Primary Source Files Directly Audited:**
  - `CASE_STUDY.md`: Formal walkthrough of the initial Sharpe 3.80 result, 7-audit validation gauntlet, diagnostic P&L accounting decomposition, engine rebuild, pre-registered salvage failure, and strategy retirement.
  - `audit-bundle/01-STATE-statarb.md`: Detailed audit timeline, pairs failure (−0.06 net Sharpe), residual baseline (2.67 net Sharpe), point-in-time membership retest (2.50 net Sharpe), and falling-knife stress testing.
  - `audit-bundle/02-design-spec.md`: Formal design specification for Alpaca paper-trading forward test of the residual reversion book on live S&P 500 constituents, defining the full vs floored spread ($s < -2\sigma$ premium) and dead-name drag ledger.
  - `audit-bundle/04-RECOMPUTE.md`: Mathematical definitions, exact formula derivations, and recomputation table of all headline figures from `05-residual-return-series.csv`.
  - `tracks/statarb/STATE.md`: Comprehensive strategy lifecycle dossier detailing HYP-005 and HYP-005b (PCA factor-1 testing), marking the permanent DEAD verdict.
  - `tracks/statarb/residual.py`: Source code implementing `rolling_beta`, `rolling_alpha`, `rolling_residual` (signal space), `hedged_returns` (implementable P&L space), and `drift_adjusted_s_score` (Avellaneda-Lee modified s-score).
  - `tracks/statarb/pnl.py`: Vectorized `equal_weight_net` module executing dollar-neutral implementable P&L and turnover cost accounting.
  - `memos/diagnostics-2026-07-10.md`: Core forensic diagnostic memo detailing the half-life monotonicity failure, the 4-part P&L identity decomposition, turnover cost drag, post-fix ablation re-run, and salvage results.
- **Primary Sample Period:** June 27, 2018 to July 6, 2026 (2,015 trading days); split subperiods 2018-06-27 to 2022-06-27 (1,008 days) and 2022-06-28 to 2026-07-06 (1,007 days) (`source-reported`).
- **Venue & Market Type:** US Equities (S&P 500 large-cap constituents and Sector SPDR ETFs) (`source-reported`).
- **Repository Deduplication Check:** Comprehensive grep across all existing Markdown records in `alpha-strategy-research` confirmed zero prior records citing `kristenharim`, `alpha-lab`, Kristen Ho, or commit `6a5589b07cf8`. While prior records examine pairs trading failures (`sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md`, `pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12.md`, `us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13.md`) or crypto PCA residual reversion (`crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12.md`, `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md`), this record is completely unique in identifying and mathematically proving the **residual-space vs implementable-hedged P&L accounting artifact** in Avellaneda & Lee (2010) US equity stat-arb, demonstrating how subtracting rolling unhedgeable alpha drift creates a phantom 16%/year return that masks negative net alpha.

## Economic mechanism

### Source-reported

1. **The Classical Stat-Arb Premise:** Avellaneda & Lee (2010) propose that idiosyncratic stock returns, obtained by stripping away market and sector factor risk via linear regression, follow mean-reverting Ornstein-Uhlenbeck (OU) processes. When an idiosyncratic cumulative residual deviates significantly from its historical mean (measured by an $s$-score), liquidity shocks or transient order imbalances are assumed to be temporary, creating an attractive statistical arbitrage opportunity to buy underperforming stocks and short outperforming stocks against a sector hedge.
2. **The Residual-Space Accounting Flaw:** In classical backtest implementations, portfolio P&L is frequently computed directly in residual space as $\text{position} \times \text{residual}$. However, by definition of the single-factor regression model:
   $$R_{i,t} = \alpha_{i,t-1} + \beta_{i,t-1} R_{f,t} + \epsilon_{i,t}$$
   the idiosyncratic residual is $\epsilon_{i,t} = R_{i,t} - \alpha_{i,t-1} - \beta_{i,t-1} R_{f,t}$. Scoring P&L as $\text{position} \times \epsilon_{i,t}$ implicitly credits the strategy with $-\text{position} \times \alpha_{i,t-1}$.
3. **The Unhedgeable Trailing Alpha Trap:** The trailing alpha $\alpha_{i,t-1}$ is each stock's own rolling drift estimate (the regression intercept). It is **not a systematic factor exposure**; an exchange-traded sector hedge ($-\beta_{i,t-1} R_{f,t}$) neutralizes factor variance, but cannot hedge away single-stock drift. Mechanically, the sharp price dislocation that triggers an entry drags the trailing 60-day alpha estimate negative. Entering a long position while $\alpha_{i,t-1} < 0$ means that subtracting $\alpha_{i,t-1}$ credits the position with roughly +6 bps/day of accounting profit regardless of whether the underlying stock recovers.
4. **Economic Reality of Implementable Cash Flows:** An actual executable long/short equity portfolio holds the stock and hedges with the sector ETF, earning the implementable hedged return:
   $$R_{\text{hedged}, i, t} = R_{i,t} - \beta_{i,t-1} R_{f,t} = \epsilon_{i,t} + \alpha_{i,t-1}$$
   In the author's audited S&P 500 portfolio, the trailing alpha drift term $\alpha_{i,t-1}$ contributed an unhedgeable **−15.9%/year drag**. The true gross reversion edge on daily large caps is only ~1.3%–1.6%/year (gross Sharpe ~0.28–0.30, 63% win rate). Daily one-way portfolio turnover of 5.3% incurs 5.34%/year in transaction costs at 10 bps/side, overwhelming gross returns by ~4x and producing a net Sharpe of **−0.88** (and **−1.12** under realistic production constraints).
5. **Failure of the Avellaneda-Lee Drift-Corrected Salvage:** Avellaneda & Lee (2010) proposed a theoretical "modified" s-score ($s_{\text{mod}} = s - \alpha/(\kappa \sigma)$) that subtracts expected drift. In pre-registered testing with zero tuned parameters, the modification modestly increased gross return (1.28% to 1.56%), but shortened average holding period (18.9d to 16.0d) and increased turnover churn, driving net Sharpe further negative to **−1.06**.
6. **Failure of Ornstein-Uhlenbeck Half-Life Screening:** Pre-registered testing of the Avellaneda-Lee $\kappa$ (mean-reversion speed) filter revealed inverted economics: the slowest-reverting quintile (Q5, median half-life 12.2 days) had higher win rate (73.9% vs 70.4%) and higher per-trade P&L (+0.0195 vs +0.0104) than the fastest-reverting quintile (Q1, median half-life 2.3 days). The filter was killed by its own pre-registered criterion.

### Research interpretation

This case study is a landmark forensic falsification that uncovers an insidious, widespread source of false precision in equity quantitative finance:
1. **Mathematical Divergence Between Signal Space and P&L Space:** In econometric signal construction, subtracting $\alpha_{t-1}$ is necessary to de-trend the cumulative residual into a stationary zero-mean OU process. However, conflating this de-trended econometric residual with cash-flow P&L creates a massive accounting fiction. A portfolio cannot trade an intercept; an investor receives cash returns $R_{s} - \beta R_{f}$, which fundamentally includes $\alpha_{t-1}$.
2. **Why Seven Standard Robustness Audits Failed to Catch the Flaw:** The author subjected the strategy to seven rigorous validation checks—look-ahead audits, return winsorization, universe restriction to S&P 500 mega-caps, 20-trial deflated Sharpe tests, point-in-time constituent membership, and falling-knife stress tests. Every audit passed with flying colors (net Sharpe remained 1.70 to 2.67) because all seven audits interrogated the *signal and the data*, while the fatal error resided one level deeper in the *P&L accounting equation*.
3. **Turnover-to-Edge Ratio in Daily Large-Cap Equity Reversion:** In contemporary US equities, daily-frequency mean reversion on liquid S&P 500 constituents offers an edge of roughly 1.3% gross per annum. Because capturing this micro-edge requires high portfolio turnover (~5.3% one-way daily, holding period ~15–19 days), execution frictions (10 bps per side taker/spread/impact plus 1 bp ETF overlay) consume over 5.3% per annum, making positive net alpha mathematically unachievable without unrealistic institutional execution advantages ($\le 2$ bps/side).

## Signal

### Source-reported

The core strategy is an equal-weight, dollar-neutral cross-sectional statistical arbitrage book executed on daily bars across S&P 500 constituents:

1. **Factor Model:** Single-factor rolling Ordinary Least Squares (OLS) regression of each stock's daily return on its corresponding Sector SPDR ETF return:
   $$R_{i,\tau} = \alpha_{i,t} + \beta_{i,t} R_{f(i),\tau} + \epsilon_{i,\tau}, \quad \tau \in [t - W + 1, t]$$
   - Rolling lookback window: $W = 60$ trading days (`source-reported`).
   - Sector factor matching: Each stock $i$ is mapped to its sector ETF $f(i)$ (e.g., XLK for technology, XLF for financials, XLE for energy) (`source-reported`).
2. **Causal Lagging:** Betas and alphas are strictly estimated on trailing window $W$ and lagged by 1 trading day before use: $\beta_{i,t-1}$ and $\alpha_{i,t-1}$ (`source-reported`).
3. **Signal Residual Formation:**
   $$\text{resid}_{i,t} = R_{i,t} - \alpha_{i,t-1} - \beta_{i,t-1} R_{f(i),t} \quad (\text{source-reported})$$
4. **Cumulative Residual & S-Score:**
   $$X_{i,t} = \sum_{\tau=1}^t \text{resid}_{i,\tau}$$
   $$s_{i,t} = \frac{X_{i,t} - \bar{X}_{i,t,W}}{\sigma(X)_{i,t,W}} \quad (\text{source-reported})$$
   where $\bar{X}_{i,t,W}$ and $\sigma(X)_{i,t,W}$ are the rolling 60-day mean and standard deviation of $X_{i,t}$.
5. **Entry Triggers:**
   - **Long Entry:** Enter long stock $i$ (and short $\beta_{i,t-1}$ of Sector ETF $f(i)$) when $s_{i,t} \le -1.25$ (`source-reported`).
   - **Short Entry:** Enter short stock $i$ (and long $\beta_{i,t-1}$ of Sector ETF $f(i)$) when $s_{i,t} \ge +1.25$ (`source-reported`).
6. **Exit Triggers:**
   - **Mean-Reversion Exit:** Close position when $s_{i,t}$ returns inside the neutral band $|s_{i,t}| \le 0.50$ (i.e. $-0.50 \le s_{i,t} \le +0.50$) (`source-reported`).
7. **Execution Timing:**
   - Evaluated at `skip = 1` day: signals observed at the close of day $t$ generate orders executed on day $t+2$ (or next-day close), eliminating bid-ask bounce contamination (`source-reported`).
8. **Avellaneda-Lee Drift-Corrected Modified S-Score (Pre-Registered Salvage):**
   $$s_{\text{mod}, i, t} = s_{i,t} - \frac{\alpha_{i,t-1}}{\kappa_{i,t} \sigma_{i,t}} \quad (\text{source-reported})$$
   where $\kappa_{i,t} = -\ln(b_{i,t})$ is the mean-reversion speed derived from rolling 60-day AR(1) regression $X_{i,\tau} = a + b X_{i,\tau-1} + \eta_\tau$, defined only when $b \in (0, 1)$ (`source-reported`).

### Research interpretation

The signal logic is mathematically closed, deterministic, and fully specified with zero discretionary parameters. The author's audited implementation in `tracks/statarb/residual.py` strictly separates:
- **Signal Space:** `rolling_residual` (uses $\alpha_{t-1}$ to construct stationary zero-mean $s$-scores),
- **Implementable Return Space:** `hedged_returns` ($R_i - \beta_{t-1} R_f$, which retains $\alpha_{t-1}$ as unhedgeable real-world cash flow).

## Required data

### Source-reported

- **Asset Universe:** S&P 500 index constituents (~503 stocks in survivor baseline; 505 stocks in point-in-time 2018 snapshot; 1,103 stocks in wide S&P 500 + S&P 600 tests) (`source-reported`).
- **Factor Assets:** 11 Sector SPDR ETFs (XLK, XLF, XLE, XLV, XLI, XLY, XLP, XLU, XLB, XLRE, XLC) and SPY (`source-reported`).
- **Data Vendor / Primary Feed:** EODHD daily prices (`panel_2005.parquet`) for historical research; Yahoo Finance (`yfinance`) for baseline free replication; Alpaca Market Data API for live forward paper-trading (`source-reported`).
- **Fields:** Daily Open, High, Low, Close, Volume, and Adjusted Close (`source-reported`).
- **Timeframe:** Daily (`1d`) bars (`source-reported`).
- **Point-in-Time Membership Data:** S&P 500 constituent historical changes maintained by fja05680 change-log, ingested via `core/data/universe.py::fetch_sp500_pit_changes` (`source-reported`).
- **Missing Data & Delisting Coverage:** The author explicitly identifies a critical free-data gap: of 505 S&P 500 members as of 2018-01-02, 144 had departed by 2026, and 120 of those have no price history in free APIs (acquired or bankrupted/failed) (`source-reported`).

### Research interpretation

All data inputs are publicly accessible. The author's point-in-time reconstitution successfully eliminates constituent *inclusion look-ahead* (156 current members added mid-window), but proves that free retail data feeds structurally suffer from *delisting survivorship* due to the missing price history of bankrupted companies (e.g., SIVB, FRC) (`research-proposed`).

## Execution assumptions

### Source-reported

- **Portfolio Sizing:** Equal-weight across all active positions, normalized daily to maintain dollar neutrality (`source-reported`):
  $$w_{i,t} = \frac{\text{held}_{i,t}}{\sum_j |\text{held}_{j,t}|} \quad (\text{source-reported})$$
- **Hedge Overlay Execution:** For each unit of stock $i$, short $\beta_{i,t-1}$ notional of its sector ETF $f(i)$ (`source-reported`).
- **Transaction Costs:**
  - Stock trades: 10 bps per side (20 bps round-trip) on turnover (`source-reported`).
  - Sector ETF hedge overlay rebalancing: 1 bp per side on overlay turnover (`source-reported`).
- **Turnover Metrics:** Daily one-way turnover averaged 5.3% of the notional book (annualized cost drag of 5.34%/year at 10 bps/side) (`source-reported`).
- **Median Holding Period:** 15.0 to 18.9 trading days (`source-reported`).
- **Production Layer Constraints:**
  - Liquidity filter: Exclude stocks with ADV < $5M USD (`source-reported`).
  - Concentration caps: Sector and single-name exposure constraints (`source-reported`).
  - Earnings blackout: Suppress new trade entries surrounding quarterly earnings announcements (`source-reported`).

### Research interpretation

- The 10 bps per side transaction cost assumption is highly realistic for retail margin or small institutional accounts trading large-cap equities (`research-proposed`).
- Even under an aggressive institutional assumption of 2 bps per side, transaction costs (~1.07%/year) would absorb over 70% to 85% of the gross reversion edge (~1.3%–1.5%/year), leaving negligible net alpha after market impact and short borrow fees (`research-proposed`).
- Short borrow availability was assumed 100% at zero borrow fee for all S&P 500 constituents; during acute idiosyncratic distress (the deep-dip long/short candidates), borrow fees and short recalls would introduce further negative drag in practice (`research-proposed`).

## Evidence

### Source-reported

All metrics below are directly extracted from Kristen Ho (`kristenharim/alpha-lab`, commits and audit dossiers `6a5589b07cf8`, 2018–2026, 2,015 trading days) (`source-reported`):

#### 1. The Flawed Residual-Space Headline (Initial Backtest)

Scored in residual space as $\text{position} \times \epsilon_{t}$ (`tracks/statarb/pnl.py` old engine) (`source-reported`):

| Configuration / Audit | Gross Sharpe | Net Sharpe (10 bps) | Ann. Return | Max Drawdown | Win Rate | Deflated Sharpe Prob ($n=20$) |
|---|---|---|---|---|---|---|
| Baseline Survivor S&P 500 | **3.80** | **2.67** | +12.50% | −6.30% | 60.10% | 1.0000 |
| Skip 0 → Skip 1 (execution delay) | 3.42 | 3.61 | — | — | — | — |
| Winsorize [−50%, +100%] | — | 2.66 | — | — | — | — |
| Point-in-Time (PIT) Membership | — | **2.50** | +11.51% | −5.49% | 58.36% | 1.0000 |
| PIT + Long Floor $-2.0\sigma$ | — | **1.69** | +7.15% | −5.04% | 56.77% | 0.9976 |
| Survivor + Long Floor $-1.75\sigma$ | — | **1.71** | +7.12% | −4.33% | 57.12% | 0.9981 |

*Subperiods (Residual Space):*
- Full Survivor: 2018-06-27 to 2022-06-27: Net Sharpe **2.91**; 2022-06-28 to 2026-07-06: Net Sharpe **2.40** (`source-reported`).
- Full PIT: 2018-06-27 to 2022-06-27: Net Sharpe **2.67**; 2022-06-28 to 2026-07-06: Net Sharpe **2.31** (`source-reported`).

#### 2. Diagnostic Accounting Decomposition (The Smoking Gun)

Evaluated on identical positions and identical data over the 2,015-day sample via the accounting identity $R_i = \epsilon_i + \alpha_{i,t-1} + \beta_{i,t-1} R_f$ (`memos/diagnostics-2026-07-10.md`) (`source-reported`):

| Book Component | Gross Sharpe | Ann. Return | Ann. Volatility |
|---|---|---|---|
| **Residual Book** (what the flawed backtest scored) | **3.80** | **+17.9%** | 4.7% |
| **Raw Stock Book** (unhedged, held in real accounts) | **0.30** | **+2.0%** | 6.5% |
| **Beta-Hedged Book** (stock − $\beta \cdot$ ETF, implementable) | **0.42** | **+2.0%** | 4.6% |
| **Trailing Alpha Drift Term** ($-\alpha_{i,t-1}$ phantom credit) | **−29.9** | **−15.9%** | 0.5% |

#### 3. Corrected Implementable P&L Engine (Ablation Re-Run)

Scored using implementable cash flows $R_i - \beta_{i,t-1} R_f$ minus 10 bps stock turnover and 1 bp ETF overlay (`CASE_STUDY.md`, `memos/diagnostics-2026-07-10.md`) (`source-reported`):

| Configuration | Flawed Sharpe (Residual Space) | Corrected Sharpe (Implementable) | Ann. Net Return | Max Drawdown | Win Rate | Note |
|---|---|---|---|---|---|---|
| Baseline (no costs) | 3.80 | **0.28** | +1.28% | −10.6% | 63.3% | Real gross edge ~1.3%/yr |
| + Costs (10 bps/side) | 2.67 | **−0.88** | −4.0% | −30.4% | 63.3% | Costs exceed gross edge ~4x |
| + Liquidity filter ($ADV > $5M) | 2.65 | **−0.89** | −4.0% | −30.4% | 63.3% | Drops illiquid tail |
| + Sector / name caps | 2.44 | **−1.10** | −5.0% | −35.0% | — | Portfolio risk limits |
| All On (+ Earnings Blackout) | 2.43 | **−1.12** | −5.0% | −35.0% | 64.0% | Deflated Sharpe prob = 0.00 |

#### 4. Pre-Registered Salvage Attempt: Drift-Corrected S-Score

Pre-registered as a single trial with zero tuned parameters using Avellaneda-Lee's formula $s_{\text{mod}} = s - \alpha/(\kappa \sigma)$ (`CASE_STUDY.md`, `memos/diagnostics-2026-07-10.md`) (`source-reported`):

| Variant | Gross Sharpe | Net Sharpe (10 bps) | Ann. Gross Return | Win Rate | Average Hold | Verdict |
|---|---|---|---|---|---|---|
| Plain $s$-score | 0.28 | **−0.88** | +1.28% | 63.3% | 18.9d | Failed net |
| Drift-corrected $s_{\text{mod}}$ | 0.35 | **−1.06** | +1.56% | 57.6% | 16.0d | **KILLED** (added churn worsened net) |

#### 5. Ornstein-Uhlenbeck Half-Life Screen Falsification

Pre-registered test across AR(1) half-life quintiles (`memos/diagnostics-2026-07-10.md`) (`source-reported`):
- Q1 (fastest reversion, median half-life 2.3d): Win rate 70.4%, Mean per-trade P&L = **+0.0104**.
- Q3 (median half-life 5.2d): Win rate 71.2%, Mean per-trade P&L = **+0.0130**.
- Q5 (slowest reversion, median half-life 12.2d): Win rate 73.9%, Mean per-trade P&L = **+0.0195**.
- Result: Slower-reverting stocks earned *more* per trade and had higher win rates, directly contradicting the theoretical premise that fast mean reversion isolates superior statistical arbitrage.

#### 6. Benchmark Distance Pairs (Gatev-Goetzmann-Rouwenhorst)

- 60 mega-caps (2018+, 252d formation / 126d trading, 20 pairs, 5 bps fee): Net Sharpe **−0.06**, ann. return −0.42%, max DD −28%, 1,883 obs. (Dead) (`source-reported`).
- S&P 500 + S&P 600 wide universe (1,103 names, within-sector formation, 50 pairs, 5 bps fee): Net Sharpe **0.23**, ann. return +0.90%, max DD −11%, hit rate 50%, deflated prob 74% (Below 0.50 kill bar) (`source-reported`).

### Independently reproduced

`not independently reproduced`

### Negative evidence

- The Avellaneda & Lee (2010) residual reversion stat-arb strategy fails completely to generate positive risk-adjusted returns on liquid S&P 500 equities after standard transaction costs, achieving an implementable net Sharpe of **−0.88** to **−1.12**.
- Apparent backtest Sharpes in excess of 2.50 to 3.80 in published or open-source implementations are attributable to an accounting flaw that credits the non-hedgeable single-stock drift term ($\alpha_{t-1}$) to the portfolio.
- Classical distance-based pairs trading in liquid US equities is confirmed dead (−0.06 net Sharpe), consistent with Do & Faff (2010) post-2002 decay findings.
- The theoretical drift-corrected modified $s$-score worsens net performance (−1.06 net Sharpe) due to increased turnover and transaction cost drag.

## Falsification plan

### Source-reported falsification criteria (completed by primary author)

1. **Implementable Cash-Flow Criterion:** If the beta-hedged portfolio ($R_i - \beta_{t-1} R_f$) net of 10 bps transaction costs fails to achieve a net Sharpe $> 0.50$, reject the strategy as an investable alpha. (Result: net Sharpe −0.88 to −1.12 -> **FALSIFIED / PERMANENTLY KILLED**).
2. **Pre-Registered Salvage Criterion:** If the drift-corrected modified s-score ($s_{\text{mod}}$) fails to achieve positive net Sharpe under implementable accounting without parameter tuning, permanently retire the track. (Result: net Sharpe −1.06 -> **FALSIFIED / RETIRED**).
3. **Half-Life Monotonicity Criterion:** If per-trade P&L does not decline with estimated AR(1) half-life and slow quintiles do not underperform, kill the OU $\kappa$ screen. (Result: slow quintiles outperformed -> **FALSIFIED / KILLED**).

### Research-defined falsification thresholds (for potential future adaptations)

1. **Ultra-Low Cost Sensitivity Stress Test:** Re-evaluate the implementable S&P 500 residual reversion book under institutional prime brokerage fee tiers (2 bps per side total cost including exchange fees, spread crossing, and borrowing). If the net Sharpe remains below 0.30, confirm that the residual reversion premium has permanently decayed below institutional viability (`research-defined falsification threshold`).
2. **Intraday Resolution Test:** Port the implementable hedged return architecture to 15-minute or 1-hour intraday bars. If the ratio of gross reversion return to round-trip execution cost does not exceed 3.0x, reject intraday adaptation (`research-defined falsification threshold`).

## Crypto portability

- **Portability Status:** `adapted` / `unproven` (`research-proposed`).
- **Porting Rationale:** The strategy was developed and evaluated exclusively on US equities and Sector SPDR ETFs. Porting to cryptocurrency markets is unproven and must be treated as an adapted research hypothesis rather than validated empirical evidence.
- **Crypto Microstructure & Structural Differences:**
  1. **Perpetual Futures vs. Equity Borrow:** Crypto perpetual swaps eliminate traditional equity borrow friction and short rebate locate constraints, simplifying two-sided execution. However, they introduce 8-hour funding rate cash flows; holding mean-reversion positions across funding settlements can incur severe adverse carry if trading against market sentiment (`research-proposed`).
  2. **Factor Architecture Fragmentation:** Unlike US equities where sector ETFs provide clean, liquid, low-cost factor baskets, crypto has no official sector ETFs. Constructing crypto factor hedges requires synthetic baskets (e.g., DeFi, Layer-1, AI indices) or high-dimensional PCA factors, which suffer from rapid idiosyncratic structural breaks and high rebalancing turnover (`research-proposed`).
  3. **Absence of Mean-Reverting Drift:** Prior repo records (`crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12.md` and `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md`) empirically proved that Avellaneda-Lee residual reversion fails completely in crypto (gross Sharpe −0.06, net Sharpe −0.58 to −2.13), as crypto assets exhibit persistent momentum cascades rather than bounded OU mean reversion (`research-proposed`).

## Limitations

- **Single-Factor Sector Specification:** The primary source evaluated single-factor sector ETF regressions. While preliminary HYP-005b experiments with PCA factor-1 doubled gross return (Sharpe 0.30 to 0.58), net performance remained firmly negative (−0.40 net Sharpe) due to rebalancing turnover (`source-reported`).
- **Free Data Delisting Gap:** 120 of 144 delisted S&P 500 constituents between 2018 and 2026 lacked historical price series in free APIs. While the author proved that deep-dip longs ($s < -2\sigma$) accounted for 43% of headline profits, precise quantification of bankruptcy losses requires CRSP/WRDS point-in-time pricing data (`source-reported`).
- **Execution Fill Model:** The backtest assumed execution at close (`skip = 1`) without detailed order-book queue simulation or intraday market impact modeling (`source-reported`).

## Implementation status

- `not-implemented`

No implementation of this strategy has been performed in our production research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). The strategy is documented as an authoritative negative-result falsification record to prevent regression into flawed residual-space accounting in future statistical arbitrage research.

## Adoption boundary

- `research-only`
- `not-approved`

This record is an empirical falsification capture. Presence in this repository confirms that the Avellaneda & Lee (2010) daily residual reversion framework is economically unviable in US equities after transaction costs. It does not authorize strategy adoption, implementation, paper trading, testnet, or live deployment.

## Related Wiki records

- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]`
- `[[quant/crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12]]`
- `[[quant/crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]`
- `[[quant/johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12]]`
- `[[quant/pairs-trading-adf-stationarity-filter-walk-forward-falsification-2026-09-12]]`
- `[[quant/us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13]]`
- `[[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]`

## Sources

1. Kristen Ho (`kristenharim`), *\"From Sharpe 3.8 to Retirement: Auditing an Untradeable Stat-Arb Backtest\"* and *\"alpha-lab\"*, GitHub repository, commit `6a5589b07cf8dace7d18b1681561b2b166df5cd4`, published September 12, 2026, accessed September 13, 2026.
   - Repository URL: https://github.com/kristenharim/alpha-lab
   - Primary Case Study: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/CASE_STUDY.md
   - StatArb Audit State: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/audit-bundle/01-STATE-statarb.md
   - Forward Paper Design: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/audit-bundle/02-design-spec.md
   - Recomputation & Formulas: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/audit-bundle/04-RECOMPUTE.md
   - StatArb Dossier: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/tracks/statarb/STATE.md
   - Residual Engine: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/tracks/statarb/residual.py
   - P&L Engine: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/tracks/statarb/pnl.py
   - Diagnostic Memo: https://github.com/kristenharim/alpha-lab/blob/6a5589b07cf8dace7d18b1681561b2b166df5cd4/memos/diagnostics-2026-07-10.md
2. Marco Avellaneda and Jeong-Hyun Lee, *\"Statistical arbitrage in the US equities market\"*, *Quantitative Finance*, Vol. 10, No. 7, pp. 761–782, 2010. DOI: [10.1080/14697680903124632](https://doi.org/10.1080/14697680903124632). (Foundational theoretical reference for residual mean reversion and modified s-scores).
3. Binh Do and Robert Faff, *\"Does Pairs Trading Still Work?\"*, *Financial Analysts Journal*, Vol. 66, No. 4, pp. 83–95, 2010. DOI: [10.2469/faj.v66.n4.1](https://doi.org/10.2469/faj.v66.n4.1). (Referenced in source analysis regarding post-2002 stat-arb profitability decay).
